#!/usr/bin/env python3
"""Fill the Phase B research briefs, one per batch (v2, 18 Oct 2026 11:00 UTC).

Reads data/research-groups.json, data/polities.csv, data/polities/<slug>.json and briefs/research-brief.md;
splits every group into small parts (-a, -b, ...) by founding year, capped at MAX_POLITIES owned leaf
polities and MAX_SHAPES Cliopatria shapes per part (v1 used 16/90: an agent's cost grows with the square of
its turns, so small batches are several times cheaper per state); groups with two or more parts get an
extra "-x" batch for the states Cliopatria lacks that the scope names. Writes notes/phase-b/briefs/<id>.md
and notes/phase-b/batches.json. Run from history/: python3 -I tools/fill_briefs.py [--date YYYY-MM-DD]
"""
import csv, json, sys, os, re
from collections import defaultdict

H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = '2026-10-18'
if '--date' in sys.argv:
    DATE = sys.argv[sys.argv.index('--date') + 1]
MAX_POLITIES = 6
MAX_SHAPES = 45
MAX_CONTEXT = 40

rows = list(csv.DictReader(open(f'{H}/data/polities.csv', encoding='utf-8')))
pol = {r['slug']: r for r in rows}
groups = json.load(open(f'{H}/data/research-groups.json'))
template = open(f'{H}/briefs/research-brief.md', encoding='utf-8').read()
owner_of = {s: g['id'] for g in groups for s in g['polities']}

# neighbours from the seeds (cached)
cache = '/tmp/claude-0/work/research-groups/neighbours-v2.json'
if os.path.exists(cache):
    NEIGH = json.load(open(cache))
else:
    NEIGH = {}
    for r in rows:
        if r['umbrella'] == '0':
            p = f"{H}/data/polities/{r['slug']}.json"
            if os.path.exists(p):
                NEIGH[r['slug']] = json.load(open(p)).get('neighbours', [])
    os.makedirs(os.path.dirname(cache), exist_ok=True)
    json.dump(NEIGH, open(cache, 'w'))

KNOWN = {
    'han': 'slug collision: "Han" (-404..-203) is `han`; "Hán" (-206..-204) is `han-2`',
    'han-2': 'slug collision: this is "Hán" (-206..-204); "Han" (-404..-203) is `han`',
    'kingdom-of-great-britain': 'Cliopatria has no "United Kingdom" row: this Name runs 1709..2024; split into Great Britain 1707-1800 and the United Kingdom from 1801 (new slug); its 1969-2023 shapes also contain Oman (1,440 cells)',
    'french-fifth-republic': 'the 1961-2023 shape still contains Algeria (8,845 conflict cells at every anchor 1970-2020): correct it',
    'netherlands-antilles': 'the 1877-2023 shape includes Suriname (541 cells)',
    'estado-novo': 'runs 1926..2024 and its 2024 shape is a 6,900 km2 patch at Cabinda; Portugal has no shape of record after 1925 except via this row and (Portuguese Empire): fix the end year and give Portugal a dossier to 2024',
    'saint-kitts': 'the 1967..2024 polygon is drawn on Saint Croix (US Virgin Islands), not Saint Kitts',
    'mujahideen': 'dated 1987..2024 and jumps from Afghanistan to Syria/Iraq: probably two different things',
    'monaco': 'polygons are 94 km2 for a 2 km2 state',
    'seychelles': 'the 1976-2023 shape is drawn 0.1 degree west of Mahe and yields no land cell',
    'new-france': 'the 1629-31 shape is Saint Martin, not New France',
    'new-netherland': 'the 1800-02 shape is Saint Martin',
    'kievan-rus': 'alive 1040-1235 beside its principalities (overlap); decide where it ends',
    'brandenburg-prussia': 'drawn beside Kingdom of Prussia in 1710 (overlap)',
    'blue-horde': 'drawn beside Golden Horde in 1400 (6,581 overlapping cells)',
    'chinese-communist-party': '1938-45 shape overlaps the USSR (5,560 cells in 1940); decide whether it is a rebel polity',
    'kingdom-of-norway': 'drawn in 1940 together with Nazi Germany (occupation, not sovereignty)',
    'mughal-empire': '1811-56 shapes beside the British Empire (overlap)',
    'denmark-norway': 'dated 1864-1921, which is wrong (the union ended 1814)',
    'sultanate-of-malacca': 'alive 1600-1630 overlapping Mataram, although Malacca fell in 1511',
    'kingdom-of-axum': 'the 600 shape overlaps a Himyarite row',
    'hashemite-arab-federation': 'dated 1415-1439 in Iraq, which is nonsense (the real federation was 1958)',
    'mahdids': 'dated 1169-1506 centred on Oman; check',
    'hamdanid-emirates': '936-1259 with a centroid in Pakistan/Iran; check',
    'ptolemaic-kingdom': 'largest shape is 4.8M km2 centred in Iran: a mislabelled row',
    'french-india': 'the shape is the Mascarenes, not French India',
    'maynila': '1521-1599 with a Ryukyu centroid: mislabelled',
    'new-caledonia': '1856-1859 centred in Borneo: mislabelled',
    'protectorate-of-the-western-regions': 'dated 117-601, which is wrong',
    'kingdom-of-fiji': 'listed by Cliopatria in South America',
    'turgesh': 'probable label swap: Türgesh 692-749 lies in Mongolia and Turks 666-756 in Kazakhstan/Kyrgyzstan',
    'turks': 'probable label swap with Türgesh (see turgesh)',
    'tang-dynasty': 'Cliopatria row is 623..910 with 32 shapes; the worked example polities/_example-tang-dynasty.json has already reviewed all of them: copy it to tang-dynasty.json, check it, keep the example file',
    'sui-dynasty': 'Cliopatria row runs to 627 (the Sui court ended 618-619; later shapes are remnants)',
    'great-britain': 'if present: 1969-2023 shapes include Oman',
    'kingdom-of-italy': '587..1946 is Lombard, Carolingian, Napoleonic and Savoyard Italy in one row: split',
    'later-zhou': '-750..960 is the ancient Zhou plus the Five Dynasties Later Zhou: split',
    'georgia': '567..2024 runs from Iberia to the republic: split; 567-576 is Lazica (see the eastern-roman-empire dossier notes)',
    'elam': '-3200..-601: several Elamite states in one row',
    'papal-states': '755..1870 in one row; fine as one state if continuous, say so',
    'swiss-confederation': '1294..2024 in one row; decide the break at 1798/1848',
    'kingdom-of-sweden': '980..2024 in one row; decide the state breaks',
    'champa': '207..1652 in one row; several Cham polities',
    'zapotec-civilization': '-500..895 as one row',
    'anuradhapura': '-291..1017 as one row',
    'khmer-empire': '800..1867 in one row: split (Angkor, post-Angkor Cambodia)',
    'british-colonial-empire': '1706-1999 aggregate row; overlaps the colonies it contains',
    'kingdom-of-france': 'umbrella and leaf rows share the Name; 1260..1375 umbrella shapes had invalid geometry (repaired)',
    'byzantine-empire': 'the eastern-roman-empire dossier (395-632, done) hands over to this slug in 632/633 and asks for one colour and a found event written as a hand-over; Roman Empire, Eastern Roman Empire and Byzantine Empire are one continuous state in three Cliopatria rows',
    'lazica': 'Cliopatria row ends 545; the eastern-roman-empire dossier tints Lazica as its vassal 395-541, 551-617, 626-632 and asks for one lazica dossier that also covers the "Georgia" 567-576 row',
    'kingdom-of-soissons': 'the 476-479 shape seems to include Odoacer\'s northern Italy; Odoacer\'s kingdom 476-493 has no Cliopatria row (add it as a new state)',
}

wd = defaultdict(list)
for r in rows:
    if r['umbrella'] == '0' and r['wikidata']:
        for q in r['wikidata'].split(';'):
            wd[q].append(r['slug'])
shared = {}
for q, slugs in wd.items():
    if len(slugs) > 1:
        for s in slugs:
            shared.setdefault(s, []).append((q, [o for o in slugs if o != s]))

def problems(slug):
    r = pol[slug]
    out = []
    if slug in KNOWN:
        out.append(KNOWN[slug])
    span = int(r['last_year']) - int(r['first_year'])
    if span >= 600 and r['umbrella'] == '0':
        out.append(f'spans {span} years in one Cliopatria row: probably successive states, split if so')
    for q, others in shared.get(slug, []):
        out.append(f'shares Wikidata {q} with {", ".join(others)}: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes')
    return '; '.join(out)

def budget(n):
    n = int(n)
    return '1-2 pages' if n <= 3 else 'up to 5 pages' if n <= 12 else 'up to 9 pages' if n <= 30 else 'up to 14 pages'

def row_md(slug, with_budget=False, with_group=False):
    r = pol[slug]
    area = r['max_area_km2']
    try:
        area = f"{float(area):,.0f}"
    except Exception:
        pass
    extra = f" | {budget(r['n_shapes'])}" if with_budget else (f" | {owner_of.get(slug, '?')}" if with_group else '')
    return f"| {slug} | {r['name']} | {r['first_year']}..{r['last_year']} | {r['n_shapes']} | {area} | {r['wikipedia']} | {problems(slug)}{extra} |"

def table(slugs, with_budget=False, with_group=False):
    leaf = [s for s in slugs if not s.startswith('rel-')]
    rel = [s for s in slugs if s.startswith('rel-')]
    head = "| slug | Cliopatria Name | first..last | shapes | max area (km2) | Wikipedia title | known problems" + (" | page budget |" if with_budget else " | group |" if with_group else " |")
    head += "\n| --- | --- | --- | --- | --- | --- | ---" + (" | --- |" if (with_budget or with_group) else " |")
    md = head + '\n' + '\n'.join(row_md(s, with_budget, with_group) for s in leaf) if leaf else '(none)'
    if rel:
        md += '\n\nUmbrella and relation rows (context only, never a dossier): ' + ', '.join(f"`{s}` ({pol[s]['name']}, {pol[s]['first_year']}..{pol[s]['last_year']})" for s in rel)
    return md

def nshapes(s):
    return int(pol[s]['n_shapes'])

def context_for(owned, group):
    """Neighbours of the owned states (seed neighbours[]), other groups' and other parts' alike, by overlap length."""
    score = defaultdict(int)
    for s in owned:
        for n in NEIGH.get(s, []):
            if n['slug'] in owned:
                continue
            score[n['slug']] += max(1, int(n['to']) - int(n['from']) + 1)
    ranked = sorted(score, key=lambda k: -score[k])
    return ranked[:MAX_CONTEXT], len(ranked)

COMMON_NOTES = [
    "Page budget per state (last column of the owned table; by number of Cliopatria shapes: up to 3 shapes 1-2 pages, up to 12 shapes up to 5 pages, up to 30 shapes up to 9 pages, more up to 14 pages). Open the state's article first, then the war and treaty pages the border moves need, until the budget is spent; keyframes you could not verify within the budget get verdict ok with the note 'unverified: page budget'. The reviewer knows the budget and judges thin against it.",
    "Earlier runs were cut short by the account's usage limit. If history/polities/<slug>.json already exists for one of your states, validate it (python3 -I history/tools/validate_dossier.py <file> --json); if it passes, keep it unchanged, read only its identity, the first ten ledger lines and its notes (not the whole file), count it in dossiers_written with validates true and 'kept from an earlier run' in its name field, and move on; if it fails, fix it. Notes from the earlier runs may exist as history/polities/_notes/<other-id>.md; read one only if it names your state.",
    "Keep your context small, because every turn re-reads it: never print a whole dossier, the schema or the example back into the conversation (read the example once, the schema once; grep what you need later); write each dossier with one heredoc or a short Python script; ask WebFetch for the specific dated facts (years, places, treaties) and quote only those; do not read other agents' dossiers in full (grep their ledger for the year you need). Write each dossier to the mount as soon as it validates, most eventful states first; if you run low on context, stop cleanly: write the notes file, list the unwritten states under gaps with why 'not reached: context', and return the report.",
    "Run Python from your scratch directory with PYTHONDONTWRITEBYTECODE=1 and python3 -I. WebFetch is the only route to Wikipedia (curl is refused). Natural Earth spellings for countries and provinces are in data/gazetteer/countries.jsonl and admin1.jsonl. Known-bad Cliopatria rows for your states are in the owned table's known-problems column and in data/README.md; start from those notes.",
]

XX01 = {
    'a': "Near East, Egypt and Europe: Hassuna, Samarra, Halaf, Ubaid and Uruk (Mesopotamia), the Pre-Pottery and Pottery Neolithic Levant (Jericho, Çatalhöyük and the Anatolian Neolithic), Badari, Naqada I-II and the Faiyum/Merimde Neolithic (Egypt), Starčevo-Körös-Criș, Linear Pottery, Vinča, Cucuteni-Trypillia, Lengyel, Funnelbeaker, Cardial Ware, the megalith builders of Atlantic Europe and Sredny Stog / early Yamnaya on the steppe.",
    'b': "Asia: Peiligang, Cishan, Yangshao, Dawenkou, Hemudu, Majiabang, Songze, Liangzhu (its start), Hongshan, Daxi, Qujialing (China); Jōmon (Japan); Chulmun (Korea); Mehrgarh and the early Indus (Ravi/Hakra phases); Jeitun, Anau and the Kelteminar culture (Central Asia); the Hoabinhian and the Neolithic of mainland South-East Asia where dated.",
    'c': "Africa, the Americas and Oceania: the Saharan cattle herders (Pastoral Neolithic, Nabta Playa), the Khartoum Mesolithic and Neolithic, the Capsian, the Tichitt precursors where dated; Norte Chico's precursors and the Valdivia culture (Americas), the Archaic Southwest and Eastern Woodlands Archaic (Watson Brake), the Chinchorro culture; the Lapita precursors are too late, so Oceania before 3400 BCE is the Australian Aboriginal cultures and New Guinea's Kuk agriculture, drawn as cultures.",
}

batches = []
for g in groups:
    gid = g['id']
    if gid in ('xx-02', 'xx-03'):
        continue
    owned_all = g['polities']
    leaf = sorted([s for s in owned_all if not s.startswith('rel-')], key=lambda s: (int(pol[s]['first_year']), s))
    rel = [s for s in owned_all if s.startswith('rel-')]
    parts = []
    cur, cur_sh = [], 0
    for s in leaf:
        n = nshapes(s)
        if cur and (len(cur) >= MAX_POLITIES or cur_sh + n > MAX_SHAPES):
            parts.append(cur); cur, cur_sh = [], 0
        cur.append(s); cur_sh += n
    if cur or not parts:
        parts.append(cur)
    letters = 'abcdefghijklmnopqrstuvwxyz'
    plan = [(letters[i], p, False) for i, p in enumerate(parts)]
    if gid == 'xx-01':
        plan = [(k, [], True) for k in 'abc']
    elif len(parts) >= 2:
        plan.append(('x', [], True))
    for key, part, is_add in plan:
        single = (len(plan) == 1)
        bid = gid if single else f'{gid}-{key}'
        notes = [f"Group scope (from data/research-groups.json): {g['scope']}"]
        if gid == 'xx-01':
            notes.append(f"You own no Cliopatria row: every dossier is a new one of type culture (cliopatria_names: [], new keyframes as region specs with text and dated from/to, found and dissolve events, certainty mostly 1-2, the Wikipedia page of the culture as the source; 2-3 pages per culture). This is part {key} of 3 of the cultures group; your cultures: {XX01[key]} Aim for 8-14 dossiers, the best documented first; slugs from tools/slug.py; list every one under new_slugs. The map before the first states must never be blank.")
            context, n_ctx = (g['context'], len(g['context']))
        elif is_add:
            notes.append(f"This is the additions batch of group {gid} ({g['name']}): you own no Cliopatria row. Your job is the states Cliopatria lacks that the scope names (and any other state of this region and era that held land for ten years or more and has a Wikipedia article), each as a new dossier: cliopatria_names [], every keyframe new (shape_id <slug>_<from>, from, to, correction as a region spec with text, verdict adjust), ledger, wars, certainty, sources as usual, 2-5 pages per state. Check polities.csv and history/polities/ that the slug is free, and list every one under new_slugs. Aim for the 6-10 most important first (most land for the longest). The group's Cliopatria states are written by parts {', '.join(k for k, _, a in plan if not a)} in parallel; do not write those; cite them as counterparts.")
            context, n_ctx = context_for([], g)  # none
            context = [s for s in g['context'] if not s.startswith('rel-')][:MAX_CONTEXT]
            n_ctx = len(g['context'])
        else:
            if not single:
                sib = [s for k, p, a in plan for s in p if k != key]
                notes.append(f"This is part {key} of {len([1 for k, p, a in plan if not a])} of group {gid} ({g['name']}), split by founding year so that one agent carries at most {MAX_POLITIES} states or {MAX_SHAPES} Cliopatria shapes. The other parts run in parallel and write the group's other states ({', '.join(sib)}); do not write or edit those. The states Cliopatria lacks that the scope names are written by the group's additions batch {gid}-x; you add only rebel states and direct counterparts of your own states that no row covers, and list the rest under counterparts_needing_dossiers.")
            else:
                notes.append("You are the only agent of this group: the states Cliopatria lacks that the scope names are yours to add after your owned states, 2-5 pages each.")
            context, n_ctx = context_for(part, g)
        if gid == 'ea-04' and 'tang-dynasty' in part:
            notes.append("polities/_example-tang-dynasty.json is a finished Tang dossier (618-907, 60 events, 19 pages). Copy it to polities/tang-dynasty.json, verify its ledger against the pages it cites only where you doubt it, keep the example file untouched, and spend your effort on the other states.")
        notes += COMMON_NOTES
        notes.append(f"Also save your final JSON report to history/notes/phase-b/reports/{bid}.json before returning it (same content), so that it survives if the message is cut.")
        owned_md = table(part + (rel if key == 'a' or single else []), with_budget=True) if (part or rel) else '(none: this batch writes new dossiers only, see the orchestrator notes)'
        ctx_md = table(context, with_group=True) if context else '(none within 25 km in this era; your counterparts are the states you add)'
        if n_ctx > len(context):
            ctx_md += f"\n\n({n_ctx - len(context)} more distant or short-lived neighbours omitted; the seeds data/polities/<slug>.json list them all; data/research-groups.json names every group's states.)"
        txt = (template.replace('{{group_id}}', bid).replace('{{group_name}}', g['name'] + ('' if single else f' (part {key})'))
               .replace('{{date}}', DATE).replace('{{owned_polities}}', owned_md)
               .replace('{{context_polities}}', ctx_md)
               .replace('{{orchestrator_notes}}', '\n\n'.join(f'- {n}' for n in notes)))
        assert '{{' not in txt, re.findall(r'\{\{[a-z_]+\}\}', txt)
        open(f'{H}/notes/phase-b/briefs/{bid}.md', 'w', encoding='utf-8').write(txt)
        batches.append({'id': bid, 'group': gid, 'region': gid.split('-')[0], 'name': g['name'], 'part': None if single else key,
                        'additions': is_add, 'owned': part, 'shapes': sum(nshapes(s) for s in part), 'context_n': len(context),
                        'brief': f'history/notes/phase-b/briefs/{bid}.md', 'bytes': len(txt.encode())})

# region round-robin order so that early results cover the world
order = ['eu', 'me', 'ea', 'ia', 'jk', 'sa', 'se', 'af', 'am', 'oc', 'xx']
byreg = {r: [b for b in batches if b['region'] == r] for r in order}
ordered = []
while any(byreg.values()):
    for r in order:
        if byreg[r]:
            ordered.append(byreg[r].pop(0))
json.dump({'date': DATE, 'version': 2, 'max_polities': MAX_POLITIES, 'max_shapes': MAX_SHAPES, 'batches': ordered}, open(f'{H}/notes/phase-b/batches.json', 'w'), indent=1)
print('batches', len(ordered), 'additions batches', sum(b['additions'] for b in ordered), 'owned total', sum(len(b['owned']) for b in ordered), 'shapes', sum(b['shapes'] for b in ordered))
print('brief bytes min/median/max', min(b['bytes'] for b in ordered), sorted(b['bytes'] for b in ordered)[len(ordered)//2], max(b['bytes'] for b in ordered))
print('ids:', json.dumps([b['id'] for b in ordered]))
