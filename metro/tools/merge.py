# Merge regional line facts (Wikipedia passes) with OpenStreetMap lines into the metro database files
import json, glob, csv, re, os, math, collections, unicodedata, urllib.parse, sys
from shapely.geometry import LineString
from shapely.ops import unary_union
from shapely.strtree import STRtree

def dedupe_tracks(parts, tol=30.0, share=0.8):
    """Keep one track per corridor: drop parts lying (80 %+) within 30 m of a longer part already kept, i.e. the other direction's track."""
    parts = [p for p in parts if len(p) >= 2]
    if len(parts) < 2:
        return parts
    lat0 = sum(p[0][1] for p in parts) / len(parts)
    kx, ky = 111320 * math.cos(math.radians(lat0)), 110570
    geoms = [LineString([(x * kx, y * ky) for x, y in p]) for p in parts]
    kept, bufs = [], []
    for i in sorted(range(len(parts)), key=lambda i: -geoms[i].length):
        g = geoms[i]
        if g.length == 0:
            continue
        if bufs:
            near = [bufs[j] for j in STRtree(bufs).query(g)]
            if near and g.intersection(unary_union(near)).length >= share * g.length:
                continue
        kept.append(i); bufs.append(g.buffer(tol, cap_style=2))
    return [parts[i] for i in sorted(kept)]
def track_km(parts):
    t = 0.0
    for p in parts:
        for (x1, y1), (x2, y2) in zip(p, p[1:]):
            c = math.cos(math.radians((y1 + y2) / 2))
            t += math.hypot((x2 - x1) * 111.32 * c, (y2 - y1) * 110.57)
    return t
SP = '/tmp/claude-0/-home-claude/f7631473-4717-56ca-bcd1-1eb0cd244a23/scratchpad/metro'
OV = '/tmp/claude-0/ov'
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{SP}/db'
os.makedirs(OUT, exist_ok=True)

systems = {s['system_id']: s for s in json.load(open(f'{SP}/systems.json'))}
lines, stages, dup = {}, [], []
for f in sorted(glob.glob(f'{SP}/workers/*.lines.jsonl')):
    grp = os.path.basename(f).split('.')[0]
    for ln in open(f, encoding='utf8'):
        r = json.loads(ln)
        r['_group'] = grp
        if r['line_id'] in lines:
            dup.append(r['line_id'])
        lines[r['line_id']] = r            # later row wins (workers sometimes rewrite a line)
# rulings made by this pass on the regional passes' open cases (logged in metro-definition.md section 9.5)
RULE_FIX = {
    'us-la-metro-rail:c': {'included': True, 'ruling_test': '', 'opened': '1995-08-12', 'ruling_note': 'In by the seven tests (definition 9.5): fully grade-separated light metro per en.wikipedia; 9.3 listed only the NTD heavy-rail lines. Check the section shared with the K Line for crossings.'},
    'kr-seoul-metropolitan-subway:everline': {'included': False, 'ruling_test': 'T2', 'ruling_note': 'Out on T2 (definition 9.5): runs single non-articulated cars (Bombardier ART 200), so it fails "at least two cars, or one articulated vehicle"; 9.3 had listed it in.'},
    'gb-london-underground:waterloo-city': {'opened': '1994-04-01', 'ruling_note': 'In from 1 Apr 1994, when it moved to London Underground (definition 9.5). From 8 Aug 1898 it was owned and run by the LSWR, the Southern Railway and British Rail (T7), recorded as predecessor. Tagged limited_service: no weekend trains. Check.'},
    'us-new-york-city-subway:b': {'opened': '1908', 'ruling_note': 'Brighton Line counted from 1908, when its last grade crossings were removed (definition 9.5); a surface excursion railway from 2 Jul 1878, recorded as predecessor.'},
    'us-new-york-city-subway:q': {'opened': '1908', 'ruling_note': 'Brighton Line counted from 1908, when its last grade crossings were removed (definition 9.5); a surface excursion railway from 2 Jul 1878, recorded as predecessor.'},
    'us-new-york-city-subway:l': {'opened': '1906-07-28', 'ruling_note': 'Canarsie Line counted from 28 Jul 1906, its first elevated rapid transit service (definition 9.5); a steam dummy line from 21 Oct 1865, recorded as predecessor. One gated crossing at East 105th Street lasted until about 1973. Check.'},
    'us-new-york-city-subway:s-franklin-avenue': {'opened': '1906', 'ruling_note': 'Franklin Avenue Line counted from 1906, when its last grade crossings near Park Place were removed (definition 9.5); a surface railway from 1878, recorded as predecessor.'},
    # identity ended when merged into another line; track still in service under that line (same as Ankara M2 and M3)
    'cn-beijing-subway:batong': {'status': 'closed', 'closed': '2021-08-29'},
    'hk-mtr:ma-on-shan': {'status': 'closed', 'closed': '2021-06-27'},
    'us-staten-island-railway:sir': {'opened': '1971-07-01', 'ruling_note': 'In from 1 Jul 1971, when the city bought the line and SIRTOA took over (definition 9.5). Before that it was a B&O subsidiary carrying freight (T7), recorded as predecessor from 1 Feb 1860, electric from 30 May 1925. Check.'},
}
for lid, fix in RULE_FIX.items():
    if lid in lines:
        lines[lid].update(fix)
for f in sorted(glob.glob(f'{SP}/workers/*.stages.jsonl')):
    for ln in open(f, encoding='utf8'):
        stages.append(json.loads(ln))
# systems added by workers
ADDED = {'cn-hangzhou-haining-intercity': ('Hangzhou–Haining Intercity Railway', 'Hangzhou', 'China'),
         'eg-cairo-monorail': ('Cairo Monorail', 'Cairo', 'Egypt'),
         'jp-linimo': ('Linimo', 'Nagoya', 'Japan'),
         'my-express-rail-link': ('Express Rail Link (KLIA Ekspres, KLIA Transit)', 'Kuala Lumpur', 'Malaysia'),
         'th-bangkok-airport-rail-link': ('Airport Rail Link', 'Bangkok', 'Thailand'),
         'th-bangkok-srt-red-lines': ('SRT Red Lines', 'Bangkok', 'Thailand'),
         'tr-marmaray': ('Marmaray', 'Istanbul', 'Turkey'),
         've-los-teques-metro': ('Los Teques Metro', 'Los Teques', 'Venezuela')}
for r in lines.values():
    if r['system_id'] not in systems:
        nm_, ct_, co_ = ADDED.get(r['system_id'], ('', '', ''))
        systems[r['system_id']] = {'system_id': r['system_id'], 'system_name': nm_, 'city': ct_, 'country': co_, 'iso2': r['system_id'][:2].upper(),
                                   'in_wikipedia_list': 'no', 'ruling': 'added', 'ruling_test': '', 'ruling_note': 'added by the line pass', 'worker': r['_group']}

osm = json.load(open(f'{OV}/osm_lines_built.json'))

def norm(s):
    s = unicodedata.normalize('NFKC', s or '').casefold().replace('_', ' ')
    return re.sub(r'\s+', ' ', s).strip()
def wkey_url(u):
    m = re.match(r'https?://([a-z\-]+)\.(?:m\.)?wikipedia\.org/wiki/([^?#]+)', u or '')
    if not m:
        return None
    return (m.group(1), norm(urllib.parse.unquote(m.group(2))))
def wkey_tag(t):
    if not t or ':' not in t:
        return None
    lang, title = t.split(':', 1)
    return (lang.strip(), norm(title.split('#')[0]))

# 1) Wikipedia-title matches
key2lines = collections.defaultdict(set)
for lid, r in lines.items():
    for u in r.get('sources') or []:
        k = wkey_url(u)
        if k:
            key2lines[k].add(lid)
def refnorm(s):
    s = norm(s)
    s = re.sub(r'[<>()\[\]]', '', s).strip()
    s = re.sub(r'^(?:(?:linea|línea|linha|ligne|linie|lijn|line|lrt|mrt)\s*(?=\S)|[uml]\s*(?=\d))', '', s)
    s = re.sub(r'\s*(号线|號線|線|선|호선|line|线|linjen|linje)$', '', s).strip()
    return s
match = {}                                   # osm_line -> line_id
for o in osm:
    k = wkey_tag(o['wikipedia'])
    if not k or k not in key2lines:
        continue
    cands = key2lines[k]
    if len(cands) == 1:
        match[o['osm_line']] = next(iter(cands))
    else:
        same = [c for c in cands if refnorm(lines[c]['ref']) and refnorm(lines[c]['ref']) == refnorm(o['ref'])]
        if len(same) == 1:
            match[o['osm_line']] = same[0]

def nn(x):
    x = unicodedata.normalize('NFKD', x or '')
    x = ''.join(ch for ch in x if not unicodedata.combining(ch)).casefold()
    x = re.sub(r'[\(\[（].*?[\)\]）]', ' ', x)
    x = re.sub(r"\b(station|stn|metro|subway|underground|railway|terminal|stop)\b", ' ', x)
    x = re.sub(r'(站|駅|역)$', '', x.strip())
    x = re.sub(r"[^\w]+", ' ', x)
    return re.sub(r'\s+', ' ', x).strip()

# where each system is: its city's ScraperMap tower centroid, else a hand list of city centres (approximate, for the 60 km check below)
def _n(x):
    x = unicodedata.normalize('NFKD', x or ''); x = ''.join(c for c in x if not unicodedata.combining(c)).casefold()
    return re.sub(r'\s+', ' ', x).strip()
_tw = collections.defaultdict(list)
with open('/mnt/project-files/knowledge/data/skyscrapers_150m_master_geocoded.csv', encoding='utf8') as fh:
    for row in csv.DictReader(fh):
        try:
            _tw[(_n(row['city']), _n(row['country']))].append((float(row['lat']), float(row['lon'])))
        except ValueError:
            pass
_tw_pts = {k: (sorted(p[0] for p in v)[len(v)//2], sorted(p[1] for p in v)[len(v)//2]) for k, v in _tw.items()}
CITY_LL = {'yerevan': (40.18, 44.51), 'minsk': (53.90, 27.56), 'brussels': (50.85, 4.35), 'brasilia': (-15.79, -47.88), 'porto alegre': (-30.03, -51.23),
    'recife': (-8.05, -34.88), 'hohhot': (40.84, 111.75), 'jinhua': (29.08, 119.65), 'taizhou': (28.66, 121.42), "xi'an": (34.34, 108.94), 'prague': (50.08, 14.44),
    'copenhagen': (55.68, 12.57), 'quito': (-0.18, -78.47), 'helsinki': (60.17, 24.94), 'lille': (50.63, 3.06), 'marseille': (43.30, 5.37), 'rennes': (48.11, -1.68),
    'toulouse': (43.60, 1.44), 'tbilisi': (41.72, 44.79), 'hamburg': (53.55, 10.00), 'munich': (48.14, 11.58), 'nuremberg': (49.45, 11.08), 'thessaloniki': (40.64, 22.94),
    'budapest': (47.50, 19.04), 'agra': (27.18, 78.01), 'ahmedabad': (23.02, 72.57), 'bhopal': (23.26, 77.41), 'gurgaon': (28.46, 77.03), 'indore': (22.72, 75.86),
    'jaipur': (26.91, 75.79), 'kanpur': (26.45, 80.33), 'kochi': (9.93, 76.27), 'meerut': (28.98, 77.71), 'nagpur': (21.15, 79.09), 'navi mumbai': (19.03, 73.03),
    'noida': (28.54, 77.39), 'patna': (25.59, 85.14), 'pune': (18.52, 73.86), 'palembang': (-2.98, 104.75), 'isfahan': (32.65, 51.67), 'mashhad': (36.30, 59.61),
    'shiraz': (29.59, 52.58), 'karaj': (35.84, 50.94), 'brescia': (45.54, 10.21), 'catania': (37.50, 15.09), 'genoa': (44.41, 8.93), 'naples': (40.85, 14.27),
    'rome': (41.90, 12.50), 'kyoto': (35.01, 135.77), 'oslo': (59.91, 10.75), 'lahore': (31.55, 74.34), 'lima': (-12.05, -77.04), 'manila': (14.60, 120.98),
    'lisbon': (38.72, -9.14), 'bucharest': (44.43, 26.10), 'kazan': (55.80, 49.11), 'nizhny novgorod': (56.30, 43.94), 'novosibirsk': (55.03, 82.92),
    'saint petersburg': (59.94, 30.31), 'samara': (53.20, 50.15), 'gwangju': (35.16, 126.85), 'stockholm': (59.33, 18.07), 'lausanne': (46.52, 6.63),
    'taoyuan': (25.00, 121.30), 'adana': (37.00, 35.32), 'bursa': (40.19, 29.06), 'dnipro': (48.46, 35.05), 'kharkiv': (49.99, 36.23), 'glasgow': (55.86, -4.25),
    'honolulu': (21.31, -157.86), 'washington, d.c.': (38.90, -77.04), 'san juan': (18.47, -66.11), 'maracaibo': (10.65, -71.64), 'liverpool': (53.41, -2.99),
    'malaga': (36.72, -4.42), 'palma': (39.57, 2.65), 'newcastle': (54.98, -1.61), 'los teques': (10.34, -67.04)}
CITY_LL_C = {('valencia', 'venezuela'): (10.16, -68.00), ('valencia', 'spain'): (39.47, -0.38)}
def km(a, b):
    p = math.radians((a[0]+b[0])/2)
    return math.hypot((a[1]-b[1])*111.32*math.cos(p), (a[0]-b[0])*110.57)
REF = {}
for sid, s_ in systems.items():
    c, co = _n(s_.get('city')), _n(s_.get('country'))
    REF[sid] = CITY_LL_C.get((c, co)) or _tw_pts.get((c, co)) or CITY_LL.get(c)
def o_pts(o):
    pts = [(st['lat'], st['lon']) for st in o['stations'] if st.get('lat') is not None]
    if not pts and o.get('geometry'):
        pts = [(y, x) for part in o['geometry']['coordinates'] for x, y in part[::10]]
    return pts
def near(o, sid, lim=80):
    """an OSM line belongs near its system: some station within lim km of the system's city (unknown city or no points: allowed)"""
    ref = REF.get(sid); pts = o_pts(o)
    return ref is None or not pts or min(km(p, ref) for p in pts) <= lim
far_dropped = 0
for o in osm:
    if o['osm_line'] in match and not near(o, lines[match[o['osm_line']]]['system_id']):
        del match[o['osm_line']]; far_dropped += 1
GENERIC = {'metro', 'subway', 'underground', 'rail', 'railway', 'transit', 'rapid', 'mass', 'system', 'line', 'lines', 'lrt', 'mrt', 'light', 'the', 'de', 'of',
           'city', 'urban', 'metropolitan', 'u', 'bahn', 'metrorail', 'metrolink', 'skytrain', 'skyline', 'and', 'metropolitano', 'metropolitana', 'del', 'la', 'el'}

# 2) which system each OSM line belongs to: Wikipedia match, then shared station names with the system's stages and termini, then network majority
sys_of = {}
for o in osm:
    if o['osm_line'] in match:
        sys_of[o['osm_line']] = lines[match[o['osm_line']]]['system_id']
sys_names = collections.defaultdict(set)
for t in stages:
    sid = lines[t['line_id']]['system_id'] if t['line_id'] in lines else t['line_id'].split(':')[0]
    for x in (t.get('from_station'), t.get('to_station')):
        if x and len(nn(x)) >= 3:
            sys_names[sid].add(nn(x))
for r in lines.values():
    for x in re.split(r'[–—/\-]| to ', r.get('termini') or ''):
        if len(nn(x)) >= 3:
            sys_names[r['system_id']].add(nn(x))
line_names = collections.defaultdict(set)
for t in stages:
    for x in (t.get('from_station'), t.get('to_station')):
        if x and len(nn(x)) >= 2:
            line_names[t['line_id']].add(nn(x))
for lid, r in lines.items():
    for x in re.split(r'[–—/\-]| to ', r.get('termini') or ''):
        if len(nn(x)) >= 2:
            line_names[lid].add(nn(x))
# system or city named in the OSM line's own tags (word-bounded): "Chengdu Metro Line 7", "en:Line 13 (Chengdu Metro)"
city_sys = collections.defaultdict(set)
for sid, s_ in systems.items():
    if norm(s_.get('city')):
        city_sys[norm(s_['city'])].add(sid)
def tag_text(o):
    return ' | '.join(norm(o.get(k) or '') for k in ('name_en', 'name', 'network', 'wikipedia', 'operator'))
tag_hits = 0
for o in osm:
    if o['osm_line'] in sys_of:
        continue
    txt = tag_text(o)
    words = set(re.findall(r'\w+', _n(txt)))
    hit = []
    for sid, s_ in systems.items():
        nm_ = norm(s_.get('system_name'))
        toks = set(re.findall(r'\w+', _n(nm_)))
        if (len(nm_) >= 5 and re.search(r'(?<!\w)' + re.escape(nm_) + r'(?!\w)', txt)) or (toks - GENERIC and toks <= words):
            hit.append(sid)
    hit = [sid for sid in hit if near(o, sid)]
    if not hit:
        hit = [next(iter(v)) for c, v in city_sys.items() if len(v) == 1 and len(c) >= 4 and re.search(r'(?<!\w)' + re.escape(c) + r'(?!\w)', txt)]
        hit = [sid for sid in hit if near(o, sid)]
    if len(hit) == 1:
        sys_of[o['osm_line']] = hit[0]; tag_hits += 1
    elif len(hit) > 1:
        best = max(hit, key=lambda x: len(systems[x].get('system_name') or ''))
        sys_of[o['osm_line']] = best; tag_hits += 1
name_hits = 0
for o in osm:
    if o['osm_line'] in sys_of:
        continue
    names = {nn(st['name']) for st in o['stations']} | {nn(st['name_en']) for st in o['stations']}
    names.discard('')
    if not names:
        continue
    sc = sorted(((len(names & v), k) for k, v in sys_names.items() if near(o, k)), reverse=True)
    if sc and sc[0][0] >= 2 and (len(sc) == 1 or sc[0][0] >= 2 * sc[1][0]):
        sys_of[o['osm_line']] = sc[0][1]; name_hits += 1
net_votes = collections.defaultdict(collections.Counter)
for o in osm:
    if o['osm_line'] in sys_of and o['network']:
        net_votes[o['network']][sys_of[o['osm_line']]] += 1
net2sys = {n: c.most_common(1)[0][0] for n, c in net_votes.items() if c.most_common(1)[0][1] >= 1}
for o in osm:
    if o['osm_line'] not in sys_of and net2sys.get(o['network']) and near(o, net2sys[o['network']]):
        sys_of[o['osm_line']] = net2sys[o['network']]
# last check: nothing assigned far from its system's city
for o in osm:
    if o['osm_line'] in sys_of and not near(o, sys_of[o['osm_line']]):
        del sys_of[o['osm_line']]; far_dropped += 1

# 3) within a system, match remaining OSM lines by ref, then by name
by_sys = collections.defaultdict(list)
for lid, r in lines.items():
    by_sys[r['system_id']].append(lid)
taken = collections.Counter(match.values())
r_exact = {}
match_strong = {k: True for k in match}       # Wikipedia matches are strong
match_score = {k: 10 for k in match}
for o in osm:
    if o['osm_line'] in match:
        continue
    sid = sys_of.get(o['osm_line'])
    if not sid:
        continue
    o_names = {nn(st['name']) for st in o['stations']} | {nn(st['name_en']) for st in o['stations']}
    o_names.discard('')
    ovs = sorted((len(o_names & line_names[lid]) for lid in by_sys[sid]), reverse=True) + [0, 0]
    best_ov, second_ov = ovs[0], ovs[1]
    cands = []
    for lid in by_sys[sid]:
        r = lines[lid]
        score = 0; strong = False
        wk = {refnorm(r['ref']), refnorm(r['name_en'])} - {''}
        ok = {refnorm(o['ref']), refnorm(o['name']), refnorm(o['name_en'])} - {''}
        if r['ref'] and norm(r['ref']) == norm(o['ref']):
            score += 4; strong = True; r_exact[(o['osm_line'], lid)] = True
        elif wk & ok:
            score += 3; strong = True
        ov = len(o_names & line_names[lid])
        if ov >= 2 and ov == best_ov and ov > second_ov and ov >= 0.25 * len(line_names[lid]):
            score += 2
        nm = norm(r['name_en']); nl = norm(r['name_local'])
        on = norm(o['name']) + ' | ' + norm(o['name_en'])
        if nm and len(nm) > 3 and nm in on:
            score += 2; strong = True
        if nl and len(nl) > 1 and nl in on:
            score += 2; strong = True
        if r.get('colour_hex') and o['colour'] and norm(r['colour_hex']) == norm(o['colour']):
            score += 1
        # a train route (through service, commuter or intercity line) needs its own line number or name to match
        if score >= 2 and (strong or o['route'] != 'train'):
            cands.append((score, strong, lid))
    cands.sort(reverse=True)
    if cands and (len(cands) == 1 or cands[0][0] > cands[1][0]):
        match[o['osm_line']] = cands[0][2]
        match_strong[o['osm_line']] = cands[0][1]
        match_score[o['osm_line']] = cands[0][0] + (2 if r_exact.get((o['osm_line'], cands[0][2])) else 0)
    elif not cands and o['route'] != 'train':
        # a system with a single line: its metro route is that line (Glasgow, DLR, Jakarta MRT)
        inc = [lid for lid in by_sys[sid] if lines[lid]['included'] is True and not lines[lid].get('closed')]
        exc = [lid for lid in by_sys[sid] if lines[lid]['included'] is not True]
        if len(inc) == 1 and (o['route'] == 'subway' or not exc):
            match[o['osm_line']] = inc[0]

line2osm = collections.defaultdict(list)
for o in osm:
    if o['osm_line'] in match:
        line2osm[match[o['osm_line']]].append(o)
# where a line has routes matched by its own number or name, drop routes matched only by shared stations
# (through services onto other railways, express variants of neighbours)
for lid, os_ in list(line2osm.items()):
    if any(match_strong.get(o['osm_line']) for o in os_):
        keep = [o for o in os_ if match_strong.get(o['osm_line'])]
        for o in os_:
            if not match_strong.get(o['osm_line']):
                del match[o['osm_line']]
        line2osm[lid] = keep
        # and where one route carries the line's exact number, drop the others matched only by name (through services)
        if any(r_exact.get((o['osm_line'], lid)) or match_score.get(o['osm_line']) == 10 for o in keep):
            keep2 = [o for o in keep if r_exact.get((o['osm_line'], lid)) or match_score.get(o['osm_line']) == 10]
            for o in keep:
                if o not in keep2:
                    del match[o['osm_line']]
            line2osm[lid] = keep2

# a line with subway routes drops light-rail routes matched only by shared stations (Stockholm's Tvärbanan on the Green line)
for lid, os_ in list(line2osm.items()):
    if any(o['route'] == 'subway' for o in os_):
        keep = [o for o in os_ if o['route'] != 'light_rail' or match_strong.get(o['osm_line'])]
        for o in os_:
            if o not in keep:
                del match[o['osm_line']]
        line2osm[lid] = keep
# a line matched to routes of its system's main network drops routes of a minor network that share its number (Paris 2 and CDGVAL's LISA, ref 2)
sys_nets = collections.defaultdict(collections.Counter)
for lid, os_ in line2osm.items():
    for o in os_:
        if o['network']:
            sys_nets[lines[lid]['system_id']][o['network']] += 1
minor_dropped = 0
for lid, os_ in list(line2osm.items()):
    c = sys_nets[lines[lid]['system_id']]; tot = sum(c.values())
    main = {n for n, k in c.items() if k >= 0.25 * tot}
    if any(o['network'] in main for o in os_):
        keep = [o for o in os_ if not o['network'] or o['network'] in main]
        for o in os_:
            if o not in keep:
                del match[o['osm_line']]; minor_dropped += 1
        line2osm[lid] = keep

# ---- opening dates per station and per segment, from the stages ----
_ABBR = {'st': 'street', 'av': 'avenue', 'ave': 'avenue', 'rd': 'road', 'sq': 'square', 'blvd': 'boulevard', 'pkwy': 'parkway', 'univ': 'university',
         'road': 'lu', 'street': 'jie', 'square': 'guangchang', 'park': 'gongyuan', 'bridge': 'qiao', 'east': 'dong', 'west': 'xi', 'south': 'nan',
         'north': 'bei', 'lake': 'hu', 'gate': 'men', 'village': 'cun'}
def ck(x):
    """compact key: ordinals, abbreviations and common English/pinyin words folded, spaces removed ("42nd St" = "42 Street", "Guiyang Lu" = "Guiyang Road")"""
    w = re.sub(r'\b(\d+)(st|nd|rd|th)\b', r'\1', nn(x)).split()
    w = [_ABBR.get(t, t) for t in w]
    w = [_ABBR.get(t, t) for t in w]
    return ''.join(w)
def alts(x):
    x = x or ''
    out = [x] + re.findall(r'[\(\[（]([^\)\]）]+)[\)\]）]', x) + [p for p in re.split(r'\s+/\s+|;\s*', x) if p != x]
    return [a for a in out if nn(a)]
def find(names, info):
    hit = set()
    for q0 in alts(names):
        q = nn(q0); qk = ck(q0)
        hit |= {k for k, d in info.items() if q in (nn(d['name']), nn(d['name_en'])) or (len(qk) >= 3 and qk in (ck(d['name']), ck(d['name_en'])))}
        if hit:
            return hit
    for q0 in alts(names):
        q = nn(q0)
        if len(q) >= 4:
            hit |= {k for k, d in info.items() if any(len(c) >= 4 and (c.startswith(q) or q.startswith(c)) for c in (nn(d['name']), nn(d['name_en'])))}
        if hit:
            return hit
    return hit
stages_by_line = collections.defaultdict(list)
for t in stages:
    stages_by_line[t['line_id']].append(t)
st_open = {}          # (line_id, station key) -> (date, basis)
seg_rows = []
stage_hits = collections.Counter()
for lid, os_ in line2osm.items():
    info = {}; seqs = []
    for o in os_:
        for st in o['stations']:
            info.setdefault(st['osm_station'], st)
        for rel, seq in (o.get('variant_seq') or {}).items():
            seqs.append((rel, seq))
    segd = {}
    for t in sorted(stages_by_line.get(lid, []), key=lambda t: t['date'] or ''):
        if t['event'] not in ('open', 'extension', 'reopening', 'infill_station') or not t['date']:
            continue
        a = find(t['from_station'], info); b = find(t['to_station'], info) if t['to_station'] else set()
        if t['event'] == 'infill_station' or not t['to_station']:
            for k in a:
                st_open[(lid, k)] = (t['date'], 'stage')
            stage_hits['matched' if a else 'unmatched'] += 1
            continue
        done = False
        for rel, seq in seqs:
            ia = [i for i, k in enumerate(seq) if k in a]; ib = [i for i, k in enumerate(seq) if k in b]
            if not ia or not ib:
                continue
            i, j = sorted((ia[0], ib[0]))
            for k in seq[i:j+1]:
                if (lid, k) not in st_open or st_open[(lid, k)][0] > t['date']:
                    st_open[(lid, k)] = (t['date'], 'stage')
            for x, y in zip(seq[i:j], seq[i+1:j+1]):
                key = tuple(sorted((x, y)))
                if key not in segd or segd[key][0] > t['date']:
                    segd[key] = (t['date'], rel)
            done = True
        stage_hits['matched' if done else 'unmatched'] += 1
    # stations the stages didn't reach: (1) a line opened in one stage gives every station that date; (2) a station between two stations
    # of the same date takes it; (3) OpenStreetMap's own start_date, if not before the line's start. Segments between two dated stations take the later date.
    opening = sorted({t['date'] for t in stages_by_line.get(lid, []) if t['event'] in ('open', 'extension', 'reopening') and t['date']})
    infill = any(t['event'] == 'infill_station' for t in stages_by_line.get(lid, []))
    lo = RULE_FIX.get(lid, {}).get('opened') or lines[lid].get('opened') or ''
    if len(opening) == 1 and not infill:
        for k in info:
            if (lid, k) not in st_open:
                st_open[(lid, k)] = (opening[0], 'line_single_stage')
    for rel, seq in seqs:
        ds = [st_open.get((lid, k), ('', ''))[0] for k in seq]
        for i, k in enumerate(seq):
            if ds[i]:
                continue
            prev = next((ds[j] for j in range(i - 1, -1, -1) if ds[j]), '')
            nxt = next((ds[j] for j in range(i + 1, len(seq)) if ds[j]), '')
            if prev and prev == nxt and (lid, k) not in st_open:
                st_open[(lid, k)] = (prev, 'between_stations_of_same_date')
    for k, d in info.items():
        sd = (d.get('start_date') or '').strip()
        if (lid, k) not in st_open and re.fullmatch(r'(18|19|20)\d\d(-\d\d(-\d\d)?)?', sd) and (not lo or sd >= lo):
            st_open[(lid, k)] = (sd, 'osm_start_date')
    for (x, y), (d, rel) in segd.items():
        seg_rows.append({'line_id': lid, 'from_station_id': f"{lines[lid]['system_id']}:{x}", 'to_station_id': f"{lines[lid]['system_id']}:{y}",
                         'from_name': info[x]['name'], 'to_name': info[y]['name'], 'opened': d, 'opened_basis': 'stage',
                         'from_lat': info[x]['lat'], 'from_lon': info[x]['lon'], 'to_lat': info[y]['lat'], 'to_lon': info[y]['lon'], 'osm_route': rel})
    for rel, seq in seqs:
        for x, y in zip(seq, seq[1:]):
            key = tuple(sorted((x, y)))
            if key in segd or (lid, x) not in st_open or (lid, y) not in st_open or x == y:
                continue
            d = max(st_open[(lid, x)][0], st_open[(lid, y)][0])
            segd[key] = (d, rel)
            seg_rows.append({'line_id': lid, 'from_station_id': f"{lines[lid]['system_id']}:{key[0]}", 'to_station_id': f"{lines[lid]['system_id']}:{key[1]}",
                             'from_name': info[key[0]]['name'], 'to_name': info[key[1]]['name'], 'opened': d, 'opened_basis': 'end_stations',
                             'from_lat': info[key[0]]['lat'], 'from_lon': info[key[0]]['lon'], 'to_lat': info[key[1]]['lat'], 'to_lon': info[key[1]]['lon'], 'osm_route': rel})

# ScraperMap cities (tower centroids) for station city attribution
towers = collections.defaultdict(list)
with open('/mnt/project-files/knowledge/data/skyscrapers_150m_master_geocoded.csv', encoding='utf8') as fh:
    for row in csv.DictReader(fh):
        try:
            towers[(row['city'], row['country'])].append((float(row['lat']), float(row['lon'])))
        except ValueError:
            pass
city_pts = {k: (sorted(p[0] for p in v)[len(v)//2], sorted(p[1] for p in v)[len(v)//2]) for k, v in towers.items()}
def km(a, b):
    p = math.radians((a[0]+b[0])/2)
    return math.hypot((a[1]-b[1])*111.32*math.cos(p), (a[0]-b[0])*110.57)
def nearest_city(lat, lon):
    best = min(city_pts.items(), key=lambda kv: km((lat, lon), kv[1]))
    d = km((lat, lon), best[1])
    return (best[0][0], round(d, 1)) if d <= 40 else ('', round(d, 1))

# ---- outputs ----
L_FIELDS = ['line_id', 'system_id', 'system_name', 'city', 'country', 'ref', 'name_en', 'name_local', 'colour_hex', 'termini',
            'included', 'ruling_test', 'ruling_note', 'status', 'opened', 'latest_extension', 'closed',
            'length_km', 'length_km_osm', 'track_km_osm', 'stations', 'stations_osm',
            'annual_ridership_m', 'ridership_daily_k', 'ridership_year', 'ridership_note',
            'rolling_stock', 'car_type', 'cars_per_train', 'power_supply', 'gauge_mm', 'automation', 'technology', 'express', 'national_mode',
            'operator', 'tunnel_share_osm', 'bridge_share_osm', 'osm_relations', 'osm_wikidata', 'geometry_status', 'sources', 'notes']
def yn(b):
    return 'yes' if b is True else 'no' if b is False else ''
rows = []
geo_lines = []
station_rows = []
for lid in sorted(lines, key=lambda l: (lines[l]['system_id'], l)):
    r = lines[lid]; s = systems[r['system_id']]
    os_ = line2osm.get(lid, [])
    geom_parts = []
    for o in os_:
        if o['geometry']:
            geom_parts += o['geometry']['coordinates']
    st_seen = set(); seq = 0
    for o in os_:
        for st in o['stations']:
            if st['osm_station'] in st_seen:
                continue
            st_seen.add(st['osm_station']); seq += 1
            c, d = nearest_city(st['lat'], st['lon']) if st['lat'] is not None else ('', None)
            station_rows.append({'station_id': f"{r['system_id']}:{st['osm_station']}", 'line_id': lid, 'seq': seq, 'name': st['name'], 'name_en': st['name_en'],
                                 'lat': st['lat'], 'lon': st['lon'], 'scrapermap_city': c, 'km_to_city_centre': d, 'osm_station': st['osm_station'],
                                 'osm_route': st.get('osm_route', st.get('variant')), 'wikidata': st.get('wikidata', ''), 'start_date_osm': st.get('start_date', ''),
                                 'opened': st_open.get((lid, st['osm_station']), ('', ''))[0], 'opened_basis': st_open.get((lid, st['osm_station']), ('', ''))[1]})
    geom_parts = dedupe_tracks(geom_parts)
    lens = [o['length_km_osm'] for o in os_ if o['length_km_osm']]
    tun = [o['tunnel_share'] for o in os_ if o['geometry']]
    brg = [o['bridge_share'] for o in os_ if o['geometry']]
    status = 'ok' if geom_parts else ('no_osm_match' if r['included'] else 'excluded')
    if os_ and any(o['ways_missing'] for o in os_):
        status = 'ok_with_gaps' if geom_parts else 'missing'
    rows.append({
        'line_id': lid, 'system_id': r['system_id'], 'system_name': s.get('system_name', ''), 'city': s.get('city', ''), 'country': s.get('country', ''),
        'ref': r['ref'], 'name_en': r['name_en'], 'name_local': r['name_local'], 'colour_hex': r['colour_hex'] or next((o['colour'] for o in os_ if o['colour']), ''),
        'termini': r['termini'], 'included': yn(r['included']), 'ruling_test': r['ruling_test'], 'ruling_note': r['ruling_note'], 'status': r['status'],
        'opened': r['opened'], 'latest_extension': r['latest_extension'], 'closed': r['closed'],
        'length_km': r['length_km'], 'length_km_osm': round(max(lens), 2) if lens else '', 'track_km_osm': round(track_km(geom_parts), 2) if geom_parts else '', 'stations': r['stations'], 'stations_osm': len(st_seen) if os_ else '',
        'annual_ridership_m': r['annual_ridership_m'], 'ridership_daily_k': r['ridership_daily_k'], 'ridership_year': r['ridership_year'], 'ridership_note': r['ridership_note'],
        'rolling_stock': r['rolling_stock'], 'car_type': r['car_type'], 'cars_per_train': r['cars_per_train'], 'power_supply': r['power_supply'], 'gauge_mm': r['gauge_mm'],
        'automation': r['automation'], 'technology': r['technology'], 'express': yn(r['express']), 'national_mode': r['national_mode'], 'operator': r['operator'],
        'tunnel_share_osm': round(sum(tun)/len(tun), 2) if tun else '', 'bridge_share_osm': round(sum(brg)/len(brg), 2) if brg else '',
        'osm_relations': ' '.join(o['osm_line'] for o in os_), 'osm_wikidata': ' '.join(sorted({o['wikidata'] for o in os_ if o['wikidata']})),
        'geometry_status': status, 'sources': ' '.join(r['sources'] or []), 'notes': r['notes']})
    if geom_parts:
        geo_lines.append({'type': 'Feature', 'properties': {'line_id': lid, 'system_id': r['system_id'], 'name': r['name_en'], 'ref': r['ref'],
                          'colour': rows[-1]['colour_hex'], 'opened': r['opened'], 'closed': r['closed'], 'included': r['included']},
                          'geometry': {'type': 'MultiLineString', 'coordinates': geom_parts}})

with open(f'{OUT}/metro_lines.csv', 'w', newline='', encoding='utf8') as fh:
    w = csv.DictWriter(fh, L_FIELDS); w.writeheader(); w.writerows(rows)

# systems
S_FIELDS = ['system_id', 'system_name', 'city', 'country', 'iso2', 'ruling', 'ruling_test', 'ruling_note', 'in_wikipedia_list',
            'opened_year_wikipedia', 'last_expansion_wikipedia', 'stations_wikipedia', 'length_km_wikipedia', 'annual_ridership_m', 'ridership_year',
            'lines_included', 'lines_excluded', 'lines_with_geometry', 'length_km_lines', 'first_opened']
srows = []
for sid, s in sorted(systems.items()):
    mine = [x for x in rows if x['system_id'] == sid]
    inc = [x for x in mine if x['included'] == 'yes']
    opened = sorted(x['opened'] for x in inc if x['opened'])
    ruling = {k: s.get(k, '') for k in ('ruling', 'ruling_test', 'ruling_note')}
    if not mine:
        ruling['ruling_note'] = (ruling['ruling_note'] + '; ' if ruling['ruling_note'] else '') + 'line facts not collected yet'
    elif not inc:
        tests = collections.Counter(x['ruling_test'] for x in mine if x['ruling_test'])
        ruling = {'ruling': 'out', 'ruling_test': '/'.join(t for t, _ in tests.most_common()),
                  'ruling_note': 'no line passes: ' + '; '.join(f"{x['ref'] or x['name_en']} ({x['ruling_test']})" for x in mine)}
    elif len(inc) == len(mine):
        ruling['ruling'] = 'in'
    else:
        ruling['ruling'] = 'partial'
        if not ruling['ruling_note']:
            ruling['ruling_note'] = 'out: ' + '; '.join(f"{x['ref'] or x['name_en']} ({x['ruling_test']})" for x in mine if x['included'] != 'yes')
    srows.append({k: s.get(k, '') for k in S_FIELDS} | ruling | {
        'lines_included': len(inc), 'lines_excluded': len(mine) - len(inc),
        'lines_with_geometry': sum(1 for x in inc if x['geometry_status'].startswith('ok')),
        'length_km_lines': round(sum(float(x['length_km']) for x in inc if x['length_km'] not in ('', None)), 1),
        'first_opened': opened[0] if opened else ''})
with open(f'{OUT}/metro_systems.csv', 'w', newline='', encoding='utf8') as fh:
    w = csv.DictWriter(fh, S_FIELDS); w.writeheader(); w.writerows(srows)

# stages
T_FIELDS = ['line_id', 'event', 'date', 'from_station', 'to_station', 'length_km', 'stations_added', 'note', 'source']
with open(f'{OUT}/metro_stages.csv', 'w', newline='', encoding='utf8') as fh:
    w = csv.DictWriter(fh, T_FIELDS, extrasaction='ignore'); w.writeheader()
    for t in sorted(stages, key=lambda t: (t['line_id'], t['date'] or '')):
        w.writerow(t)

# interchanges: stop areas of one system that are the same station (same Wikidata item within 600 m, or the same name within 200 m) share one station id
parent = {}
def _find(x):
    while parent.get(x, x) != x:
        parent[x] = parent.get(parent[x], parent[x]); x = parent[x]
    return x
def _union(a, b):
    ra, rb = _find(a), _find(b)
    if ra != rb:
        parent[max(ra, rb)] = min(ra, rb)
pos = {}
by_sys_st = collections.defaultdict(dict)
for row in station_rows:
    if row['lat'] is None:
        continue
    by_sys_st[lines[row['line_id']]['system_id']][row['station_id']] = row
for sid_, sts in by_sys_st.items():
    items = list(sts.values())
    by_wd = collections.defaultdict(list); by_nm = collections.defaultdict(list)
    for row in items:
        if row['wikidata']:
            by_wd[row['wikidata']].append(row)
        for nmx in {nn(row['name']), nn(row['name_en'])} - {''}:
            by_nm[nmx].append(row)
    for group, lim in [(by_wd, 0.6), (by_nm, 0.2)]:
        for rows_ in group.values():
            for a_ in range(len(rows_)):
                for b_ in range(a_ + 1, len(rows_)):
                    A, B = rows_[a_], rows_[b_]
                    if A['station_id'] != B['station_id'] and km((A['lat'], A['lon']), (B['lat'], B['lon'])) <= lim:
                        _union(A['station_id'], B['station_id'])
merged_ids = 0
for row in station_rows:
    c_ = _find(row['station_id'])
    if c_ != row['station_id']:
        row['station_id'] = c_; merged_ids += 1
for row in seg_rows:
    row['from_station_id'] = _find(row['from_station_id']); row['to_station_id'] = _find(row['to_station_id'])

# stations (one row per station and line)
# where this pass moved a line's start to the day it became metro, its earlier stages are predecessor (definition 6.1), so its
# stations and segments can't open before that day. Other lines keep their stage dates: a segment that served another line first keeps its date.
line_open = {lid: fix['opened'] for lid, fix in RULE_FIX.items() if fix.get('opened')}
clamped = 0
for row in station_rows + seg_rows:
    lo = line_open.get(row['line_id'], '')
    if lo and row['opened'] and row['opened'] < lo:
        row['opened'] = lo; clamped += 1
ST_FIELDS = ['station_id', 'line_id', 'seq', 'name', 'name_en', 'lat', 'lon', 'opened', 'opened_basis', 'scrapermap_city', 'km_to_city_centre', 'osm_station', 'osm_route', 'wikidata', 'start_date_osm']
with open(f'{OUT}/metro_stations.csv', 'w', newline='', encoding='utf8') as fh:
    w = csv.DictWriter(fh, ST_FIELDS); w.writeheader(); w.writerows(station_rows)

SEG_FIELDS = ['line_id', 'from_station_id', 'to_station_id', 'from_name', 'to_name', 'opened', 'opened_basis', 'from_lat', 'from_lon', 'to_lat', 'to_lon', 'osm_route']
with open(f'{OUT}/metro_segments.csv', 'w', newline='', encoding='utf8') as fh:
    w = csv.DictWriter(fh, SEG_FIELDS); w.writeheader(); w.writerows(sorted(seg_rows, key=lambda r: (r['line_id'], r['opened'])))
json.dump({'type': 'FeatureCollection', 'features': geo_lines}, open(f'{OUT}/metro_lines.geojson', 'w'), ensure_ascii=False, separators=(',', ':'))
uniq = {}
for s in station_rows:
    if s['lat'] is None:
        continue
    u = uniq.setdefault(s['station_id'], {'type': 'Feature', 'properties': {'station_id': s['station_id'], 'name': s['name'], 'name_en': s['name_en'], 'lines': [], '_p': []},
                                          'geometry': {'type': 'Point', 'coordinates': [s['lon'], s['lat']]}})
    if s['line_id'] not in u['properties']['lines']:
        u['properties']['lines'].append(s['line_id'])
    u['properties']['_p'].append((s['lon'], s['lat']))
for u in uniq.values():          # an interchange sits at the centre of its lines' stop areas
    p_ = u['properties'].pop('_p')
    u['geometry']['coordinates'] = [round(sum(x for x, _ in p_) / len(p_), 7), round(sum(y for _, y in p_) / len(p_), 7)]
json.dump({'type': 'FeatureCollection', 'features': list(uniq.values())}, open(f'{OUT}/metro_stations.geojson', 'w'), ensure_ascii=False, separators=(',', ':'))

# report for the README and the thread
unmatched_osm = [o for o in osm if o['osm_line'] not in match and o['route'] in ('subway', 'light_rail')]
rep = {
    'systems': len(systems), 'systems_with_lines': len({x['system_id'] for x in rows}),
    'lines': len(rows), 'lines_included': sum(1 for x in rows if x['included'] == 'yes'),
    'lines_included_with_geometry': sum(1 for x in rows if x['included'] == 'yes' and x['geometry_status'].startswith('ok')),
    'stages': len(stages), 'station_line_rows': len(station_rows), 'stations_unique': len(uniq),
    'osm_lines': len(osm), 'osm_lines_assigned_to_system': len(sys_of), 'osm_lines_assigned_by_station_names': name_hits, 'osm_lines_assigned_by_tags': tag_hits, 'osm_lines_dropped_as_far_from_system': far_dropped, 'osm_routes_dropped_as_minor_network': minor_dropped, 'segments_dated': len(seg_rows), 'dates_clamped_to_line_start': clamped, 'station_rows_merged_into_interchanges': merged_ids, 'stage_matches': dict(stage_hits), 'stations_dated': sum(1 for x in station_rows if x['opened']), 'osm_lines_matched': len(match), 'osm_subway_lightrail_unmatched': len(unmatched_osm),
    'duplicate_line_ids': dup,
    'included_without_geometry': [x['line_id'] for x in rows if x['included'] == 'yes' and not x['geometry_status'].startswith('ok')],
    'systems_without_lines': [s for s in systems if not any(x['system_id'] == s for x in rows)],
}
json.dump(rep, open(f'{OUT}/_report.json', 'w'), ensure_ascii=False, indent=1)
with open(f'{OUT}/_osm_unmatched.csv', 'w', newline='', encoding='utf8') as fh:
    w = csv.writer(fh); w.writerow(['osm_line', 'route', 'network', 'ref', 'name', 'wikipedia', 'wikidata', 'length_km_osm', 'system_guess'])
    for o in unmatched_osm:
        w.writerow([o['osm_line'], o['route'], o['network'], o['ref'], o['name'], o['wikipedia'], o['wikidata'], o['length_km_osm'], sys_of.get(o['osm_line'], '')])
print(json.dumps({k: (v if not isinstance(v, list) else len(v)) for k, v in rep.items()}, indent=1))
