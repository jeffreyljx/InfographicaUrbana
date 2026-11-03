# Research brief: new-state batch n-mod (states and territories since 1950)

Filled by the orchestrator on 2026-11-02. You are one of the Phase B research agents of the EmpireMap historical-borders project (history/README.md; the plan is history/master-plan.md). Your job: for every state in your owned list below, write one dossier (history/polities/<slug>.json) that draws its borders at yearly resolution from pages you actually open, plus a notes file for what you could not settle. The rendering agents will draw only what your dossiers say; what you leave out will not appear on the map.

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
- Validate every dossier before you move on: `python3 -I -B history/tools/validate_dossier.py history/polities/<slug>.json`, and once more with `--resolve` to see which region names the gazetteer cannot yet resolve (those are warnings for the gazetteer agent, not errors for you, as long as the name is a real one). A dossier with errors is not finished.

Rules the validator enforces beyond the schema: file name equals slug; ledger in (year, month) order; every `source` URL listed in `sources`; every Cliopatria shape of the slug reviewed; a `found` event at the start year and a `dissolve` event at the end year; a `vassal_start`, `contest_start` or `occupation_start` paired with a later `_end` with the same `counterpart` string.

## 3. Your inputs

- `history/data/polities.csv` (one row per Cliopatria Name: slug, years, number of shapes, largest area, Wikipedia title, Wikidata id, umbrella membership) and `history/data/shapes.csv` (one row per shape: shape_id, years, area, bbox, modern countries).
- `history/data/polities/<slug>.json`, the seed for each of your polities: its shapes in year order, its Cliopatria relations (allegiance, vassalage, union, umbrella membership) and its neighbours within 25 km with the years they touch. The neighbours list is your checklist of counterparts.
- `history/data/README.md`: the tables' columns, the slug collisions (`han` and `han-2`), the Cliopatria rows already known to be wrong (Later Zhou -750..960, Kingdom of Italy 587..1946, Georgia 567..2024, the French Fifth Republic shape that still contains Algeria, and more). If one of yours is listed there, start from that note.
- The Cliopatria file itself is not needed; the tables and the seed carry what you need. If you must look at a shape's outline, `python3 -I -B history/tools/gazetteer.py resolve '{"cliopatria": "<Name>", "year": <y>}'` prints its cell count and bounding box.

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

Spellings: Natural Earth 10m is the reference for country and admin-1 names (`history/data/gazetteer/countries.jsonl`, `admin1.jsonl`; "Czechia", "United States of America", "Xinjiang", "Inner Mongol"). Historical regions are `regions.jsonl` (725 names with aliases on 2026-10-18); places are `places.jsonl` (Natural Earth populated places plus historical cities such as Gaochang, Suyab, Karashahr). Search a name before you use it: `python3 -I -B history/tools/gazetteer.py names <text>`. A name the gazetteer lacks is still allowed when it is a real, findable name: use it, say so in `notes`, and list it in your report under `gazetteer_names_needed`; the gazetteer agent adds it. Prefer a named region to a radius, a radius to a coordinate, and a coordinate to a polygon.

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

- **`trust-territory-of-somaliland`** (new; keep this slug unless it names no real state). Requested by:
  - window p1950-p1959: new dossier: Italian-administered UN Trust Territory of Somaliland, 1 April 1950 to 1 July 1960 (colony row of Italy in data/colonies.csv); then drop patch events/6 and events/7 Why: no dossier for the territory: the compile left it British to 1952 and nobody's land to 1959; the patch draws it only as Italian occupation of unowned land Page: https://en.wikipedia.org/wiki/Trust_Territory_of_Somaliland
- **`bophuthatswana`** (new; keep this slug unless it names no real state). Requested by:
  - window p1980-p1989: a dossier for Bophuthatswana, declared independent on 6 December 1977 (south-africa ledger 7 vassal_start, source Bantustan page) to 1994; Transkei, Venda and Ciskei have dossiers and show as South African vassals, Bophuthatswana does not (no relation at the 1990 anchor) Why: a whole state is missing; its homeland land is drawn as plain South Africa Page: https://en.wikipedia.org/wiki/Bantustan
- **`aruba`** (new; keep this slug unless it names no real state). Requested by:
  - window p1980-p1989: a dossier for Aruba as a constituent country of the Kingdom of the Netherlands from 1 January 1986 (one cell; 179 km2) Why: no Aruba dossier exists; the Antilles' ledger 16 loses the cell to nobody, and the patch draws it as Dutch land (events/1) in the meantime Page: https://en.wikipedia.org/wiki/Aruba
  - window p2010-p2019: New dossier: Aruba as a separate country within the Kingdom since 1 January 1986 (1 cell) Why: ledger/16 of netherlands-antilles names it; the cell is still owned by the Antilles at the p2010 anchor and becomes nobody's land in October 2010 Page: https://en.wikipedia.org/wiki/Dissolution_of_the_Netherlands_Antilles
- **`curacao`** (new; keep this slug unless it names no real state). Requested by:
  - window p2010-p2019: New dossier: Curacao as a constituent country of the Kingdom of the Netherlands from 10 October 2010 (3 cells) Why: ledger/17 of netherlands-antilles names it as counterpart but no dossier exists, so its cells become nobody's land Page: https://en.wikipedia.org/wiki/Dissolution_of_the_Netherlands_Antilles
- **`sint-maarten`** (new; keep this slug unless it names no real state). Requested by:
  - window p2010-p2019: New dossier: Sint Maarten as a constituent country of the Kingdom of the Netherlands from 10 October 2010 (1 cell) Why: ledger/18 of netherlands-antilles names it as counterpart but no dossier exists, so its cell becomes nobody's land Page: https://en.wikipedia.org/wiki/Dissolution_of_the_Netherlands_Antilles
- **`al-shabaab`** (new; keep this slug unless it names no real state). Requested by:
  - window p2010-p2019: New rebel-state dossier: Al-Shabaab, in control of most of central and southern Somalia c. 2009-2012 (Mogadishu until Aug 2011, Kismayo until Oct 2012), then rural 'semi-territorial' control Why: the map draws all of Somalia as the Federal Republic of Somalia in 2010-2012 Page: https://en.wikipedia.org/wiki/Al-Shabaab_(militant_group)
- **`syrian-opposition`** (new; keep this slug unless it names no real state). Requested by:
  - window p2010-p2019: New rebel dossier for the opposition-held land of the Syrian civil war (Raqqa 2013, Idlib from 2015, Aleppo until 2016, Ghouta until 2018) Why: the Syria ledger uses it as counterpart in 4 events; the land goes to nobody (20 Idlib cells to the end of the window) Page: https://en.wikipedia.org/wiki/Syrian_civil_war
- **`ssc-khatumo`** (new; keep this slug unless it names no real state). Requested by:
  - window p2020-p2029: a new dossier for SSC-Khatumo (the Dhulbahante administration of Las Anod, 2023, later the North Eastern State of Somalia) Why: somaliland /ledger/4 and /5 hand Las Anod and the Sool, Sanaag and Togdheer lands to a counterpart with no dossier, so 151 cells are ownerless in 2023 and pass to Somalia only through its 2024 keyframe; page cited by the somaliland dossier, not opened by me. Page: https://en.wikipedia.org/wiki/SSC-Khatumo

Rules for the list:

- One dossier per state, not per dynasty.
- Before writing, list `history/polities/` and grep `history/data/polities.csv` for the state under another spelling: if a dossier for the same state already exists under another slug, do not write a second one; report it under `problems` as "alias: <requested slug> = <existing slug>" and move on.
- If the requested name is not a state or culture that held land, say so under `gaps` with why; do not invent borders for it. A rebel administration that governed land is `type: rebel`; a dependency is a state with a `vassal_start` under its suzerain (or `type: colony` for a colony, with the metropole as suzerain).
- Match your neighbours: where an existing dossier records a `gain` from your state, write the `loss`, and the reverse; name existing slugs as counterparts. Read their lines with grep, and do not edit them.

## 7. Where to write

- `history/polities/<slug>.json`, one per state, exactly as the validator accepts it.
- `history/polities/_notes/n-mod.md`: what you could not settle, per state: Cliopatria rows to split or merge, pages that would not load, disagreements between pages, states that need a dossier from another group, region names the gazetteer lacks. The reviewer and the gap-fillers read it first.
- Scratch, caches and downloads: `/tmp/claude-0/work/research-n-mod/` (create it). Nothing else goes anywhere else: no files in `history/data/`, `history/tools/`, `history/compiled/` or `history/colours.json`, and nothing in the git repository at /home/claude/SkyscraperMaps.

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

- This is a new-state batch of the CartaHistoria historical-borders project (the site mode was called EmpireMap before 1 Nov 2026; the older text above uses that name). All research, fix and window rounds are finished; the 119 window agents found these 8 states or cultures missing (states and territories since 1950), so their land shows as nobody's or as a neighbour's.
- Page budget: 2-5 pages per state; open the state's article first.
- The yearly borders are compiled by `history/tools/compile_dossiers.py` (not yours to run), which resolves every region spec with the gazetteer; `python3 -I -B history/tools/validate_dossier.py <file> --resolve` tells you whether yours resolve. The gazetteer (`history/data/gazetteer/README.md`) takes countries, admin-1 names, named regions, `{"place": "<name>", "km": <radius>}` and `{"lon": x, "lat": y, "km": r}`. A very small territory (Aruba, Curacao, Sint Maarten) may be one to three cells: use a `{"lon", "lat", "km"}` disc that covers its cells.
- Keep your context small, because every turn re-reads it: never print a whole dossier, the schema or the example back into the conversation; write each dossier with one heredoc or a short Python script; ask WebFetch for the specific dated facts and quote only those. Write each dossier to the mount as soon as it validates. If you run low on context, stop cleanly: write the notes file, list unwritten states under gaps with why 'not reached: context', and return the report.
- Run Python from your scratch directory as python3 -I -B. WebFetch is the only route to Wikipedia (curl is refused).
- Also save your final JSON report to history/notes/phase-b/reports/n-mod.json before returning it (same content), so that it survives if the message is cut.

## 11. The report you return

Your final message is one JSON object and nothing else:

```json
{
  "group_id": "n-mod",
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
  "notes_path": "history/polities/_notes/n-mod.md",
  "problems": ["anything the orchestrator must know: tool failures, rows that should be reassigned, a state that is really two"]
}
```

`python3 -I -B history/tools/validate_dossier.py history/polities/<slug>.json --json` prints the per-dossier counts in this shape.
