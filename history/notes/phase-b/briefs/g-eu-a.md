# Research brief: gap batch g-eu-a (Swiss and Italian gaps)

Filled by the orchestrator on 2026-11-01. You are one of the Phase B research agents of the EmpireMap historical-borders project (history/README.md; the plan is history/master-plan.md). Your job: for every state in your owned list below, write one dossier (history/polities/<slug>.json) that draws its borders at yearly resolution from pages you actually open, plus a notes file for what you could not settle. The rendering agents will draw only what your dossiers say; what you leave out will not appear on the map.

Your final message is data for the orchestrator (section 11), not prose for a person.

## 1. The standard, in short, and what each rule needs from you

The map tells every state's story by the same twelve rules (master-plan.md, "The standard"). You collect what the rules need; you do not draw.

| Rule | What the map does | What the dossier must carry |
| --- | --- | --- |
| 1 Birth | The state appears in its founding year at its core, with a caption | `identity.start`, a `found` event whose `region` is the core and whose `note` is the caption ("618: Li Yuan proclaims the Tang at Chang'an") |
| 2 One colour for life | A dynasty change within a state keeps the colour; a new state on the same land takes a new one | One dossier per state, not per dynasty; a dynasty change is a `rename` event; `identity.family`; predecessors and successors with the land handed over |
| 3 Expansion | Land gained is outlined bright for its first year | A `gain` event for every acquisition, dated to the year (month when known) |
| 4 Levels of control | Vassals, protectorates, tributaries and clients are a lighter tint; occupied land is hatched; associations are never territory | `vassal_start`/`vassal_end` and `occupation_start`/`occupation_end` events naming the land and the counterpart; `type: umbrella` for associations |
| 5 Civil war and rebellion | Rebel-held land takes its own hatched colour until the rebels win or are crushed | `loss`/`gain` events against the rebel state as counterpart, and a dossier of `type: rebel` for the rebels (section 6) |
| 6 Contested land | Land two states fight over shows the blend of their colours until the fighting ends | `contest_start` (first campaign that takes or holds ground, not the declaration of war) and `contest_end` (treaty, last battle or de facto end) naming the zone; `wars[].zones` |
| 7 Collapse and partition | At the end the land passes to the successors with a caption | `identity.end`, `identity.successors[].land`, a `dissolve` event; `split`/`merge` where a state divides or absorbs |
| 8 Nobody's land | Stateless land is neutral grey; cultures before 3400 BCE are muted and dotted | `counterpart: "nobody"` when land came from or went to no state; `type: culture` for cultures |
| 9 Certainty | Treaty or survey borders are sharp; approximate frontiers soft | `certainty[]` covering the whole life, with the exceptions named |
| 10 Labels, capitals, rulers | The capital is a dot that moves; a ruler strip where the record supports one | `identity.capitals` with coordinates and years for every state; `identity.rulers` only where a documented list exists |
| 11 Pacing | Play slows in eventful years and pauses on captions | Every event dated to the year, with a one-sentence `note` the viewer can read |
| 12 The state page | Name, aliases, years, area over time, capitals, rulers, the ledger with sources, links to predecessors and successors | Everything above, and `sources[]` with every page opened |

The time step is one year. Give a `month` wherever the page gives one (the United States from 1784, Europe from 1789, both World Wars, and any dated battle or treaty); it costs nothing now and cannot be added later without re-reading.

## 2. The dossier

- Schema: `history/briefs/dossier.schema.json` (JSON Schema 2020-12, every field described). Read it once in full.
- Worked example: `history/polities/_example-tang-dynasty.json`, a real Tang dossier built from nineteen opened pages: 60 ledger events, 33 keyframe verdicts, 11 wars. Copy its habits, not its content.
- Six parts: `identity`, `keyframe_review` (one verdict per Cliopatria shape, plus new keyframes for periods Cliopatria lacks), `ledger` (dated events), `wars`, `certainty`, `sources`, and a free-text `notes`.
- Validate every dossier before you move on: `python3 -I history/tools/validate_dossier.py history/polities/<slug>.json`, and once more with `--resolve` to see which region names the gazetteer cannot yet resolve (those are warnings for the gazetteer agent, not errors for you, as long as the name is a real one). A dossier with errors is not finished.

Rules the validator enforces beyond the schema: file name equals slug; ledger in (year, month) order; every `source` URL listed in `sources`; every Cliopatria shape of the slug reviewed; a `found` event at the start year and a `dissolve` event at the end year; a `vassal_start`, `contest_start` or `occupation_start` paired with a later `_end` with the same `counterpart` string.

## 3. Your inputs

- `history/data/polities.csv` (one row per Cliopatria Name: slug, years, number of shapes, largest area, Wikipedia title, Wikidata id, umbrella membership) and `history/data/shapes.csv` (one row per shape: shape_id, years, area, bbox, modern countries).
- `history/data/polities/<slug>.json`, the seed for each of your polities: its shapes in year order, its Cliopatria relations (allegiance, vassalage, union, umbrella membership) and its neighbours within 25 km with the years they touch. The neighbours list is your checklist of counterparts.
- `history/data/README.md`: the tables' columns, the slug collisions (`han` and `han-2`), the Cliopatria rows already known to be wrong (Later Zhou -750..960, Kingdom of Italy 587..1946, Georgia 567..2024, the French Fifth Republic shape that still contains Algeria, and more). If one of yours is listed there, start from that note.
- The Cliopatria file itself is not needed; the tables and the seed carry what you need. If you must look at a shape's outline, `python3 -I history/tools/gazetteer.py resolve '{"cliopatria": "<Name>", "year": <y>}'` prints its cell count and bounding box.

## 4. The region grammar

Regions are named, not drawn. A region is a JSON object, exactly one of these forms, and any form may also carry `"text"`, the source's own words (required in ledger regions and keyframe corrections):

```
{"country": name}                                  a modern country, Natural Earth spelling
{"admin1": name, "country": name}                  a province, state or oblast, Natural Earth spelling
{"place": name, "km": radius}                      a radius around a city (optional "country" to disambiguate)
{"lon": x, "lat": y, "km": r}                      a radius around a coordinate, only when no place name exists
{"cliopatria": Name, "year": y}                    that polity's Cliopatria shape in that year
{"region": historical-region-name}                 an entry of history/data/gazetteer/regions.jsonl ("Tarim Basin", "Aquitaine")
{"polygon": [[lon, lat], ...]}                     at most 12 points; fallback only, when nothing can be named
{"border_band": {"a": slug, "b": slug, "year": y, "width": cells}}   "the frontier" between two states
{"union": [...]}  {"minus": [A, B]}  {"intersect": [...]}            combinators
{"river": name, "km": r}  {"lake": name}           gazetteer extensions
```

Examples: `{"minus": [{"cliopatria": "Tang Dynasty", "year": 757}, {"region": "Hexi Corridor"}], "text": "..."}`; `{"union": [{"admin1": "Gansu", "country": "China"}, {"place": "Dunhuang", "km": 200}]}`; `{"region": "Transoxiana"}`.

Spellings: Natural Earth 10m is the reference for country and admin-1 names (`history/data/gazetteer/countries.jsonl`, `admin1.jsonl`; "Czechia", "United States of America", "Xinjiang", "Inner Mongol"). Historical regions are `regions.jsonl` (725 names with aliases on 2026-10-18); places are `places.jsonl` (Natural Earth populated places plus historical cities such as Gaochang, Suyab, Karashahr). Search a name before you use it: `python3 -I history/tools/gazetteer.py names <text>`. A name the gazetteer lacks is still allowed when it is a real, findable name: use it, say so in `notes`, and list it in your report under `gazetteer_names_needed`; the gazetteer agent adds it. Prefer a named region to a radius, a radius to a coordinate, and a coordinate to a polygon.

A correction in `keyframe_review` describes the whole corrected shape, not the delta: `{"minus": [{"cliopatria": Name, "year": y}, X]}` removes X; `{"union": [{"cliopatria": ...}, Y]}` adds Y; a verdict that changes only the years or the status (direct to vassal) gives the shape unchanged and says so in `text`.

## 5. Sources

- Open pages with the WebFetch tool and cite the page you read. The only route to Wikipedia is WebFetch (curl is refused; wikidata.org, openhistoricalmap.org, overpass, archive.org and github.com are unreachable). Ask WebFetch for dated sentences and quote them in `note`.
- A search snippet is not a source. Neither is memory: if you know a date but the page does not give it, open the page that does, or record the event at confidence 1 and say the page is silent.
- Order of sources: the Wikipedia article of the state and the articles of its wars, treaties, campaigns and protectorates; then the works those articles cite, where a page is thin; then the Seshat polity page linked from Cliopatria's SeshatID.
- Every ledger event, keyframe verdict and war cites one page URL, which must appear in `sources[]` with the date you read it. One page per event; a second page goes in `note`.
- The infobox area is a sanity check on Cliopatria's `Area`: compare the infobox figure (with its year) against `shapes.csv` `area_km2` for the shape alive in that year. Within a factor of two is fine; beyond it, say so in the keyframe's `note` and decide whether the shape or the infobox is wrong. The Tang infobox gives 5.4 M km2 for 715 against Cliopatria's 4.03 M km2 (ratio 0.75); its 661 shape of 8.73 M km2 reaches Khorasan and was marked adjust.
- Confidence: 3 when the page dates the event and names the land; 2 when the year is the page's but the region is your reading; 1 when you are bridging a silence. Do not inflate; the reviewer treats 1 as a gap, not a fault.

When a page will not load: retry once with the exact URL; try the title the search box would redirect to (for example "Anxi Protectorate" and "Protectorate General to Pacify the West" are one article); try the Wikipedia article in the other direction (the war instead of the state); try the Seshat page. If nothing loads, record the URL in `notes` and in your report's `pages_failed`, keep the Cliopatria shape with verdict `ok` and a note saying it is unverified, and move on. Never fill the gap from memory as if it were a page.

## 6. Your polities

Owned (you write these dossiers; one per state; every one is new: `cliopatria_names: []`, every keyframe new):

- **`three-leagues`** (no Cliopatria row; the slug the citing dossiers already use, so keep it exactly unless it names no real state). Cited by:
  - cisalpine-republic/ledger/4: 1797 gain: 22 October 1797: the Valtellina joins the Republic. 'On 1 Brumaire (22 October), Bonaparte announced the union
  - helvetic-republic lists it as predecessor () Absorbed on 21 April 1799 as the canton of Raetia; the Three Leagues have no dos
  - helvetic-republic/ledger/6: 1799 gain: 21 April 1799: the Three Leagues join. Infobox 'Annexed to the Helvetic Republic: 21 April 1799'; 'the Three L
  - swiss-confederation/ledger/19: 1497 vassal_start: 1497: the Three Leagues of Graubunden ally with the Confederacy (the Grey League in 1497, the others in 1498: 
  - swiss-confederation/ledger/25: 1512 vassal_start: 1512: the Valtellina becomes a subject territory of the Three Leagues, the Confederacy's associate ('Valtellin
  - swiss-confederation/ledger/33: 1620 vassal_end: 1620: the Valtellina leaves the Three Leagues. 'On the evening of 18/19 July 1620, a force of Valtellina rebel
  - swiss-confederation/ledger/34: 1639 vassal_start: 1639: the Valtellina returns to the Three Leagues. 'On 3 September 1639 the Leagues agreed with Spain to bring
  - swiss-confederation/ledger/36: 1797 vassal_end: 1797: the Valtellina leaves the Three Leagues. 'the districts were annexed to the Cisalpine Republic on 10 Oct
  - swiss-confederation/ledger/40: 1798 vassal_end: 1798: the Three Leagues end their association. The Leagues were 'absorbed into the Helvetic Republic in 1799 a
- **`sieben-zenden`** (no Cliopatria row; the slug the citing dossiers already use, so keep it exactly unless it names no real state). Cited by:
  - helvetic-republic lists it as predecessor () The Republic of the Seven Tithings (Upper Valais) and its Lower Valais subjects;
  - helvetic-republic/ledger/0: 1798 gain: 1798: the Valais joins. 'Valais was incorporated into the Helvetic Republic until 1802'; the Lower Valais dist
  - swiss-confederation/ledger/8: 1416 vassal_start: 1416: the Upper Valais (Sieben Zenden) becomes a Zugewandter Ort (associate) of the Confederacy: 'Became a Zug
  - swiss-confederation/ledger/15: 1475 vassal_start: 1475: the Valais extends its associate land. 'At the outbreak of the Burgundian Wars in 1475, the bishop of Si
  - swiss-confederation/ledger/38: 1798 vassal_end: 1798: the associate ends with the Confederacy. 'Valais was incorporated into the Helvetic Republic until 1802'
  - swiss-confederation/ledger/39: 1798 vassal_end: 1798: the Lower Valais, the associate's land since November 1475, ends with the Confederacy: the Lower Valais 
  - swiss-confederation/ledger/47: 1815 gain: 1815: the Valais becomes a canton. 'On 4 August 1815, Valais finally entered the Swiss Confederation as a cant
- **`republic-of-geneva`** (no Cliopatria row; the slug the citing dossiers already use, so keep it exactly unless it names no real state). Cited by:
  - french-directory/ledger/17: 1798 gain: 26 August 1798: Geneva is made part of France. 'On 26 August 1798, Geneva was detached from the new republic a
  - swiss-confederation/ledger/29: 1526 vassal_start: 1526: Geneva allies with Bern and Fribourg. 'The treaty was ratified in Geneva in February 1526, despite the p
  - swiss-confederation/ledger/41: 1798 vassal_end: 1798: France annexes Geneva. 'The wish would be granted on 15 April 1798 when the Genevan government is coerce
  - swiss-confederation/ledger/46: 1815 gain: 1815: Geneva joins the Confederacy. 'Geneva was admitted as a canton to the Swiss Confederation' (infobox: 19 
- **`duchy-of-massa-and-carrara`** (no Cliopatria row; the slug the citing dossiers already use, so keep it exactly unless it names no real state). Cited by:
  - principality-of-lucca-and-piombino/ledger/1: 1806 gain: 1806: Massa and Carrara and the Garfagnana annexed. 'In 1806 the former Duchy of Massa and Carrara and the for
  - cispadane-republic lists it as predecessor () Listed in the infobox as a predecessor; the page says nothing else about it, so 
  - duchy-of-modena-and-reggio/ledger/1: 1815 gain: December 1815: Francis IV takes the Este fiefs in Lunigiana from his mother. 'In December 1815 he obtained the
  - duchy-of-modena-and-reggio/ledger/2: 1829 gain: 1829: Modena inherits Massa and Carrara. 'On her death in 1829, he also inherited the Duchy of Massa and Carra
- **`duchy-of-romagna`** (no Cliopatria row; the slug the citing dossiers already use, so keep it exactly unless it names no real state). Cited by:
  - duchy-of-urbino/ledger/3: 1502 loss: 1502: Cesare Borgia takes Urbino. 'After the short rule by Cesare Borgia in 1502-03, the dukedom went to the d
  - duchy-of-urbino/ledger/4: 1503 gain: 1503: the Borgia rule ends (page: 'in 1502-03'); the dukedom passes to the Della Rovere in 1508 on Guidobaldo'
  - papal-states/ledger/15: 1500 vassal_start: 1500: Cesare Borgia carves out the Duchy of Romagna. In 1500 Cesare Borgia 'carved out for himself an ephemera
  - papal-states/ledger/16: 1503 vassal_end: 1503: the Duchy of Romagna falls with the Borgia. Page silent on the year: After Alexander VI died, his lands 
- **`march-of-tuscany`** (no Cliopatria row; the slug the citing dossiers already use, so keep it exactly unless it names no real state). Cited by:
  - republic-of-lucca lists it as predecessor () Infobox predecessor 'March of Tuscany'; the city 'bought the feudal rights from 
  - republic-of-lucca/ledger/0: 1160 found: 1160: Lucca buys its feudal rights from Welf VI. The city 'bought the feudal rights from Margrave Welf VI in 1
  - republic-of-siena lists it as predecessor () Infobox predecessors: Bishop of Siena (within Tuscany); March of Tuscany; Republ
  - republic-of-siena/ledger/0: 1125 found: 1125: the Republic of Siena is founded. 'The foundation of the Republic of Siena is traditionally dated to 112

Context (the dossiers that cite your states; read their cited ledger lines with grep, cite them as counterparts, and do not edit them):

| slug | name | years |
| --- | --- | --- |
| cisalpine-republic | Cisalpine Republic | 1797..1802 |
| cispadane-republic | Cispadane Republic | 1796..1797 |
| duchy-of-modena-and-reggio | Duchy of Modena and Reggio | 1814..1859 |
| duchy-of-urbino | Duchy of Urbino | 1443..1631 |
| french-directory | French Directory | 1795..1799 |
| helvetic-republic | Helvetic Republic | 1798..1803 |
| papal-states | Papal States | 756..1870 |
| principality-of-lucca-and-piombino | Principality of Lucca and Piombino | 1805..1815 |
| republic-of-lucca | Republic of Lucca | 1160..1805 |
| republic-of-siena | Republic of Siena | 1125..1555 |
| swiss-confederation | Swiss Confederation | 1291..2024 |

Rules for the list:

- One dossier per state, not per dynasty. A dynasty that replaces a dynasty on the same land without a break is a `rename` in the state's dossier.
- Before writing, list `history/polities/` and grep `history/data/polities.csv` for the state under another spelling: if a dossier for the same state already exists under another slug, do not write a second one; report it under `problems` as "alias: <cited slug> = <existing slug>" and move on.
- If the cited name is not a state that held land (a loose league of city states, a religious order with no territory, an era), say so under `gaps` with why, and propose what the citing dossiers should use instead (`nobody`, an existing slug, or a named culture); do not invent borders for it. A body that did govern land (the Senussi order's Cyrenaican interior, a chartered company's territory) is a state for this map: `type: state` (or `colony` for a company that ruled for a metropole, with the metropole as suzerain in a `vassal_start`).
- The citing dossiers' events give the years and the regions your ledger must match: your `loss` to them where they record a `gain` from you, and the reverse.

## 7. Where to write

- `history/polities/<slug>.json`, one per state, exactly as the validator accepts it.
- `history/polities/_notes/g-eu-a.md`: what you could not settle, per state: Cliopatria rows to split or merge, pages that would not load, disagreements between pages, states that need a dossier from another group, region names the gazetteer lacks. The reviewer and the gap-fillers read it first.
- Scratch, caches and downloads: `/tmp/claude-0/work/research-g-eu-a/` (create it). Nothing else goes anywhere else: no files in `history/data/`, `history/tools/`, `history/compiled/` or `history/colours.json`, and nothing in the git repository at /home/claude/SkyscraperMaps.

## 8. Shared-folder rules

`/mnt/project-files/history/` is a network mount other agents write to in parallel. Listing is cheap; each read downloads the file; keep files small and few. Before changing a file that already exists there, re-read it; keep the edit small; about ten seconds after writing an existing file, read it back and re-apply your change if another writer replaced it. Delete temporary files you created there. Touch only the files this brief names. Run Python that reads downloaded files with `python3 -I`. Do not call any mcp__hearthbot__ tool and do not spawn subagents.

## 9. Order of work, per state

1. Read the seed (`data/polities/<slug>.json`) and the polity row: years, shapes, relations, neighbours. Note the neighbours' years; every gain from a neighbour in your ledger must have a counterpart there.
2. Open the state's Wikipedia article with WebFetch. Take identity, capitals, the infobox area and dates, and the names of its wars, treaties and campaigns.
3. Open the pages for those wars, treaties and campaigns (and the protectorate, province or region pages they lead to) until every shape change in `shapes.csv` has an event that explains it. The Tang needed nineteen pages for 288 years; a minor state may need two.
4. Write `identity`; then `keyframe_review` in shape order; then the `ledger` in year order; then `wars`, `certainty`, `sources`, `notes`.
5. Validate; fix every error; run `--resolve` and note unknown names; move to the next state.
6. Spend your effort where the border moves: a state with 60 shapes in 300 years needs every transition explained; a state with 3 shapes in 400 years needs its start, its end and the few events the sources give.

Quality bar the reviewer will hold you to: years in order; every border move between two keyframes explained by at least one event; every `gain` names a counterpart that should carry the matching `loss` (or `nobody`, or a state you flag as needing a dossier); every event, verdict and war cites a page in `sources`; keyframe corrections and ledger events agree; the infobox area was compared; `certainty` covers the whole life; no event rests on a search snippet or on memory.

## 10. Orchestrator notes for this batch

- This is a gap-filling batch of the CartaHistoria historical-borders project (the site mode was called EmpireMap before 1 Nov 2026; the older text above uses that name). All 441 research batches are finished, reviewed and fixed. A cross-dossier audit found states that two or more dossiers cite as a counterpart, predecessor or successor but that nobody wrote; your batch writes 6 of them: Swiss and Italian gaps. Each held land on the map, so without a dossier their land shows as the neighbours' or as nobody's.
- Page budget: 2-5 pages per state; open the state's article first, then the pages for the events the citing dossiers name.
- The yearly borders are now compiled by `history/tools/compile_dossiers.py` (not yours to run), which resolves every region spec with the gazetteer; `python3 -I history/tools/validate_dossier.py <file> --resolve` tells you whether yours resolve. The gazetteer (`history/data/gazetteer/README.md`) now also takes `{"place": "<name>", "km": <radius>}` and admin-1 names.
- Keep your context small, because every turn re-reads it: never print a whole dossier, the schema or the example back into the conversation; write each dossier with one heredoc or a short Python script; ask WebFetch for the specific dated facts and quote only those; grep the citing dossiers for the lines above rather than reading them in full. Write each dossier to the mount as soon as it validates. If you run low on context, stop cleanly: write the notes file, list unwritten states under gaps with why 'not reached: context', and return the report.
- Run Python from your scratch directory with PYTHONDONTWRITEBYTECODE=1 and python3 -I. WebFetch is the only route to Wikipedia (curl is refused). Natural Earth spellings for countries and provinces are in data/gazetteer/countries.jsonl and admin1.jsonl.
- Also save your final JSON report to history/notes/phase-b/reports/g-eu-a.json before returning it (same content), so that it survives if the message is cut.

## 11. The report you return

Your final message is one JSON object and nothing else:

```json
{
  "group_id": "g-eu-a",
  "dossiers_written": [
    {"slug": "...", "path": "history/polities/<slug>.json", "name": "...", "years": [start, end],
     "cliopatria_names": ["..."], "new_state": false, "keyframes_reviewed": 0, "keyframe_verdicts": {"ok": 0, "adjust": 0, "wrong": 0},
     "events": 0, "low_confidence_events": 0, "wars": 0, "sources": 0, "validates": true, "resolve_warnings": 0}
  ],
  "events_total": 0,
  "sources_total": 0,
  "new_slugs": [{"slug": "...", "name": "...", "why": "split from <Cliopatria Name> | state Cliopatria lacks | rebel state"}],
  "gazetteer_names_needed": [{"name": "...", "kind": "region | place", "used_in": "<slug>", "hint": "what it is, roughly where"}],
  "pages_failed": ["https://..."],
  "gaps": [{"slug": "...", "what": "...", "why": "page silent | page failed | out of scope"}],
  "counterparts_needing_dossiers": [{"name": "...", "suggested_slug": "...", "years": [a, b], "group": "which group should own it, if known"}],
  "notes_path": "history/polities/_notes/g-eu-a.md",
  "problems": ["anything the orchestrator must know: tool failures, rows that should be reassigned, a state that is really two"]
}
```

`python3 -I history/tools/validate_dossier.py history/polities/<slug>.json --json` prints the per-dossier counts in this shape.
