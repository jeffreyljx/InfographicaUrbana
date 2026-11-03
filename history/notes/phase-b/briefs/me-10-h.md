# Research brief: group me-10-h (Ottomans and the modern Middle East (part h))

Filled by the orchestrator on 2026-10-18. You are one of the Phase B research agents of the EmpireMap historical-borders project (history/README.md; the plan is history/master-plan.md). Your job: for every state in your owned list below, write one dossier (history/polities/<slug>.json) that verifies, corrects and densifies its Cliopatria shapes to yearly resolution from pages you actually open, plus a notes file for what you could not settle. The rendering agents will draw only what your dossiers say; what you leave out will not appear on the map.

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

Owned (you write these dossiers; one per state):

| slug | Cliopatria Name | first..last | shapes | max area (km2) | Wikipedia title | known problems | page budget |
| --- | --- | --- | --- | --- | --- | --- | --- |
| french-mandate-for-syria-and-lebanon | French Mandate for Syria and Lebanon | 1920..1945 | 11 | 210,022 | Mandate for Syria and the Lebanon | shares Wikidata Q139708 with lebanon: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | up to 5 pages |
| kingdom-of-egypt | Kingdom of Egypt | 1922..1952 | 9 | 1,007,437 | Kingdom of Egypt |  | up to 5 pages |
| pahlavi-dynasty | Pahlavi Dynasty | 1924..1978 | 8 | 1,624,335 | Pahlavi dynasty |  | up to 5 pages |
| republic-of-turkey | Republic of Turkey | 1924..2024 | 11 | 768,279 | Turkey |  | up to 5 pages |
| kingdom-of-hejaz-and-nejd | Kingdom of Hejaz and Nejd | 1926..1935 | 2 | 1,653,414 | Kingdom of Hejaz and Nejd |  | 1-2 pages |

Context (neighbours and counterparts you will read and cite as counterparts, but another group writes them; do not create or edit their files):

| slug | Cliopatria Name | first..last | shapes | max area (km2) | Wikipedia title | known problems | group |
| --- | --- | --- | --- | --- | --- | --- | --- |
| union-of-soviet-socialist-republics | Union of Soviet Socialist Republics | 1922..1991 | 26 | 24,600,085 | Soviet Union |  | eu-17 |
| british-africa | British Africa | 1885..1960 | 33 | 10,639,583 | Scramble for Africa |  | af-08 |
| iraqi-republic | Iraqi Republic | 1960..2005 | 6 | 456,521 | Iraq | shares Wikidata Q796 with republic-of-iraq: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | me-10 |
| kingdom-of-iraq | Kingdom of Iraq | 1932..1957 | 5 | 434,052 | Kingdom of Iraq |  | me-10 |
| syria | Syria | 1973..2024 | 7 | 186,752 | Syria | shares Wikidata Q41137 with assyria: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | me-10 |
| kingdom-of-great-britain | Kingdom of Great Britain | 1709..2024 | 38 | 1,005,115 | Great Britain | Cliopatria has no "United Kingdom" row: this Name runs 1709..2024; split into Great Britain 1707-1800 and the United Kingdom from 1801 (new slug); its 1969-2023 shapes also contain Oman (1,440 cells) | eu-11 |
| third-hellenic-republic | Third Hellenic Republic | 1976..2024 | 3 | 122,017 | Third Hellenic Republic |  | eu-22 |
| kingdom-of-afghanistan | Kingdom of Afghanistan | 1926..1972 | 7 | 644,005 | Kingdom of Afghanistan |  | ia-03 |
| islamic-republic-of-iran | Islamic Republic of Iran | 1979..2024 | 7 | 1,626,457 | Iran |  | me-10 |
| people-s-republic-of-bulgaria | People's Republic of Bulgaria | 1948..1990 | 3 | 109,612 | People's Republic of Bulgaria | shares Wikidata Q121932 with republic-of-bulgaria: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | eu-22 |
| republic-of-bulgaria | Republic of Bulgaria | 1991..2024 | 3 | 109,708 | Bulgaria | shares Wikidata Q121932 with people-s-republic-of-bulgaria: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | eu-22 |
| nazi-germany | Nazi Germany | 1936..1944 | 8 | 3,309,320 | Nazi Germany |  | eu-21 |
| georgia | Georgia | 567..2024 | 17 | 86,640 | Georgia | 567..2024 runs from Iberia to the republic: split; 567-576 is Lazica (see the eastern-roman-empire dossier notes); spans 1457 years in one Cliopatria row: probably successive states, split if so | eu-19 |
| republic-of-armenia | Republic of Armenia | 1992..2024 | 3 | 41,382 | Armenia | shares Wikidata Q399 with armenia: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | eu-19 |
| republic-of-azerbaijan | Republic of Azerbaijan | 1992..2024 | 3 | 78,526 | Azerbaijan | shares Wikidata Q227 with azerbaijan-democratic-republic: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | eu-19 |
| islamic-republic-of-pakistan | Islamic Republic of Pakistan | 1947..2024 | 11 | 1,021,669 | Pakistan |  | sa-06 |
| british-raj | British Raj | 1859..1947 | 20 | 4,938,693 | British Raj |  | sa-06 |
| italian-africa | Italian Africa | 1890..1943 | 14 | 3,514,816 | Italian Empire |  | af-08 |
| kingdom-of-greece | Kingdom of Greece | 1945..1966 | 6 | 122,017 | Kingdom of Greece |  | eu-22 |
| principality-of-bulgaria | Principality of Bulgaria | 1880..1944 | 12 | 171,194 | Principality of Bulgaria |  | eu-18 |
| kingdom-of-italy | Kingdom of Italy | 587..1946 | 48 | 455,534 | Kingdom of Italy | 587..1946 is Lombard, Carolingian, Napoleonic and Savoyard Italy in one row: split; spans 1359 years in one Cliopatria row: probably successive states, split if so | eu-13 |
| state-of-kuwait | State of Kuwait | 1961..1989 | 3 | 17,395 | Kuwait | shares Wikidata Q817 with kuwait: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | me-10 |
| united-states-of-america | United States of America | 1776..2024 | 73 | 12,189,755 | United States |  | am-07 |
| kingdom-of-saudi-arabia | Kingdom of Saudi Arabia | 1936..2024 | 13 | 1,929,199 | Saudi Arabia |  | me-10 |
| first-hellenic-republic | First Hellenic Republic | 1822..1940 | 23 | 206,605 | First Hellenic Republic |  | eu-18 |
| second-syrian-republic | Second Syrian Republic | 1946..1957 | 4 | 187,924 | Second Syrian Republic |  | me-10 |
| mujahideen | Mujahideen | 1987..2024 | 5 | 644,005 | Mujahideen | dated 1987..2024 and jumps from Afghanistan to Syria/Iraq: probably two different things | ia-03 |
| republic-of-iraq | Republic of Iraq | 2014..2024 | 2 | 438,702 | Iraq | shares Wikidata Q796 with iraqi-republic: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | me-10 |
| north-yemen | North Yemen | 1919..1989 | 5 | 181,353 | North Yemen |  | me-10 |
| sultanate-of-muscat-and-oman | Sultanate of Muscat and Oman | 1900..1946 | 8 | 323,401 | Muscat and Oman |  | me-10 |
| british-colonial-empire | British Colonial Empire | 1706..1999 | 90 | 13,690,182 | British Empire | 1706-1999 aggregate row; overlaps the colonies it contains; shares Wikidata Q8680 with british-empire: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | eu-11 |
| united-arab-republic | United Arab Republic | 1958..1972 | 4 | 1,199,345 | United Arab Republic |  | me-10 |
| greek-junta | Greek junta | 1967..1975 | 2 | 123,711 | Greek junta |  | eu-22 |
| kingdom-of-jordan | Kingdom of Jordan | 1947..2024 | 13 | 103,706 | Jordan |  | me-10 |
| republic-of-afghanistan | Republic of Afghanistan | 1973..1978 | 2 | 644,005 | Republic of Afghanistan (1973–1978) |  | ia-03 |
| arab-socialist-ba-ath-party | Arab Socialist Ba'ath Party | 1967..1972 | 2 | 185,909 | Arab Socialist Ba'ath Party - Syria Region |  | me-10 |
| state-of-israel | State of Israel | 1948..2024 | 13 | 90,386 | Israel |  | me-10 |
| french-third-republic | French Third Republic | 1871..1939 | 14 | 673,774 | French Third Republic |  | eu-20 |
| ottoman-empire | Ottoman Empire | 1305..1923 | 132 | 4,255,187 | Ottoman Empire | spans 618 years in one Cliopatria row: probably successive states, split if so | me-10 |
| kingdom-of-hejaz | Kingdom of Hejaz | 1916..1925 | 7 | 434,096 | Kingdom of Hejaz |  | me-10 |

(6 more distant or short-lived neighbours omitted; the seeds data/polities/<slug>.json list them all; data/research-groups.json names every group's states.)

Rules for the list:

- One dossier per state, not per dynasty. A dynasty that replaces a dynasty on the same land without a break stays in the state's dossier as a `rename` event (Capetian to Valois; Tang to Wu Zhou to Tang). A new state on the same land (Yuan to Ming) gets its own dossier. Where Cliopatria has one row for successive states (Later Zhou -750..960, Kingdom of Italy 587..1946, Georgia 567..2024), split it: one dossier per state, each listing the Cliopatria Name in `cliopatria_names` and reviewing only the shapes of its own years; the slug of a split-off state is `slugify(<its name>)` (`history/tools/slug.py`), and your report lists every new slug under `new_slugs` so the colour agent can seed it.
- Where Cliopatria has two rows for one state (the 115 shared Wikidata ids in data/README.md: "Abbasid Caliphate" and "Abbasid Caliphate/Buyid Dynasty", "Kingdom of Navarre" and "Kingdom of Pamplona"), write one dossier under the slug of the earlier row, list both Names in `cliopatria_names`, and review both rows' shapes.
- Umbrella and relation entities (Names in parentheses, slugs `rel-...`) are not territory; do not write dossiers for them. Use them: the "(Allegiance of X to Y)" rows in your seed's `relations[]` are vassalage evidence that still needs a page to confirm the years.
- States Cliopatria lacks (a rebel state that held land, a protectorate's suzerain relation, a kingdom in sub-Saharan Africa, Oceania or the pre-Columbian Americas, a steppe polity): write a dossier anyway. `cliopatria_names: []`; every keyframe is a new one (`shape_id: "<slug>_<from year>"`, `from`, `to`, `correction` = the shape as a region spec with `text`, `verdict: "adjust"`); the ledger and the rest as usual. Slug: `slugify(name)`; check `polities.csv` and `history/polities/` that it is free, and report it under `new_slugs`. Rebel states that held land for a year or more (An Lushan's Yan, Huang Chao's Qi, the Taiping, the Confederacy) are `type: rebel`; their fighting zone is the government dossier's contest events.

## 7. Where to write

- `history/polities/<slug>.json`, one per state, exactly as the validator accepts it.
- `history/polities/_notes/me-10-h.md`: what you could not settle, per state: Cliopatria rows to split or merge, pages that would not load, disagreements between pages, states that need a dossier from another group, region names the gazetteer lacks. The reviewer and the gap-fillers read it first.
- Scratch, caches and downloads: `/tmp/claude-0/work/research-me-10-h/` (create it). Nothing else goes anywhere else: no files in `history/data/`, `history/tools/`, `history/compiled/` or `history/colours.json`, and nothing in the git repository at /home/claude/SkyscraperMaps.

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

## 10. Orchestrator notes for this group

- Group scope (from data/research-groups.json): Researches the Ottoman Empire for its whole life, Safavid to Pahlavi and Islamic Iran, the Gulf and Arabian states, Muhammad Ali's Egypt and its successors, the mandates and the modern states of the Middle East with their wars. Cliopatria lacks the Ottoman provinces and the Ottoman-Safavid frontier year by year, the Mamluk beys of Egypt and the mamluks of Baghdad as autonomous rulers, the Zaydi and Omani imamates' internal frontiers, the British and French mandates as occupations, the Arab-Israeli war lines of 1948, 1967 and 1973, and the Syrian and Iraqi wars after 2011 as contested zones; add them.

- This is part h of 13 of group me-10 (Ottomans and the modern Middle East), split by founding year so that one agent carries at most 6 states or 45 Cliopatria shapes. The other parts run in parallel and write the group's other states (ottoman-empire, safavid-dynasty, yarubid-dynasty, qasimids, afsharid-iran, emirate-of-diriyah, sultanate-of-oman, zand-dynasty, bahrain, kuwait, house-of-khalifa, qajar-dynasty, muhammad-ali-dynasty, imamate-of-yemen, qatar-dynasty, trucial-states, emirate-of-nejd, emirate-of-jabal-shammar, khedivate-of-egypt, sultanate-of-muscat-and-oman, imamate-of-oman, qatar, kingdom-of-hejaz, asir, north-yemen, kingdom-of-iraq, kingdom-of-saudi-arabia, lebanon, second-syrian-republic, kingdom-of-jordan, qatar-protectorate, palestinians, state-of-israel, republic-of-egypt, arab-federation, united-arab-republic, iraqi-republic, republic-of-syria, state-of-kuwait, ba-athist-syria, arab-socialist-ba-ath-party, people-s-democratic-republic-of-yemen, arab-republic-of-egypt, kingdom-of-bahrain, state-of-qatar, syria, united-arab-emirates, islamic-republic-of-iran, republic-of-yemen, gaza-hamas, republic-of-iraq); do not write or edit those. The states Cliopatria lacks that the scope names are written by the group's additions batch me-10-x; you add only rebel states and direct counterparts of your own states that no row covers, and list the rest under counterparts_needing_dossiers.

- Page budget per state (last column of the owned table; by number of Cliopatria shapes: up to 3 shapes 1-2 pages, up to 12 shapes up to 5 pages, up to 30 shapes up to 9 pages, more up to 14 pages). Open the state's article first, then the war and treaty pages the border moves need, until the budget is spent; keyframes you could not verify within the budget get verdict ok with the note 'unverified: page budget'. The reviewer knows the budget and judges thin against it.

- Earlier runs were cut short by the account's usage limit. If history/polities/<slug>.json already exists for one of your states, validate it (python3 -I history/tools/validate_dossier.py <file> --json); if it passes, keep it unchanged, read only its identity, the first ten ledger lines and its notes (not the whole file), count it in dossiers_written with validates true and 'kept from an earlier run' in its name field, and move on; if it fails, fix it. Notes from the earlier runs may exist as history/polities/_notes/<other-id>.md; read one only if it names your state.

- Keep your context small, because every turn re-reads it: never print a whole dossier, the schema or the example back into the conversation (read the example once, the schema once; grep what you need later); write each dossier with one heredoc or a short Python script; ask WebFetch for the specific dated facts (years, places, treaties) and quote only those; do not read other agents' dossiers in full (grep their ledger for the year you need). Write each dossier to the mount as soon as it validates, most eventful states first; if you run low on context, stop cleanly: write the notes file, list the unwritten states under gaps with why 'not reached: context', and return the report.

- Run Python from your scratch directory with PYTHONDONTWRITEBYTECODE=1 and python3 -I. WebFetch is the only route to Wikipedia (curl is refused). Natural Earth spellings for countries and provinces are in data/gazetteer/countries.jsonl and admin1.jsonl. Known-bad Cliopatria rows for your states are in the owned table's known-problems column and in data/README.md; start from those notes.

- Also save your final JSON report to history/notes/phase-b/reports/me-10-h.json before returning it (same content), so that it survives if the message is cut.

## 11. The report you return

Your final message is one JSON object and nothing else:

```json
{
  "group_id": "me-10-h",
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
  "notes_path": "history/polities/_notes/me-10-h.md",
  "problems": ["anything the orchestrator must know: tool failures, rows that should be reassigned, a state that is really two"]
}
```

`python3 -I history/tools/validate_dossier.py history/polities/<slug>.json --json` prints the per-dossier counts in this shape.
