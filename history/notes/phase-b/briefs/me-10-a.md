# Research brief: group me-10-a (Ottomans and the modern Middle East (part a))

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
| ottoman-empire | Ottoman Empire | 1305..1923 | 132 | 4,255,187 | Ottoman Empire | spans 618 years in one Cliopatria row: probably successive states, split if so | up to 14 pages |

Context (neighbours and counterparts you will read and cite as counterparts, but another group writes them; do not create or edit their files):

| slug | Cliopatria Name | first..last | shapes | max area (km2) | Wikipedia title | known problems | group |
| --- | --- | --- | --- | --- | --- | --- | --- |
| principality-of-wallachia | Principality of Wallachia | 1314..1858 | 22 | 74,680 | Wallachia |  | eu-18 |
| principality-of-moldavia | Principality of Moldavia | 1363..1858 | 29 | 256,733 | Moldavia |  | eu-18 |
| republic-of-venice | Republic of Venice | 705..1796 | 69 | 65,312 | Republic of Venice | spans 1091 years in one Cliopatria row: probably successive states, split if so | eu-13 |
| republic-of-ragusa | Republic of Ragusa | 1385..1808 | 6 | 1,540 | Republic of Ragusa |  | eu-18 |
| crimean-khanate | Crimean Khanate | 1450..1782 | 21 | 222,809 | Crimean Khanate |  | ia-02 |
| principality-of-guria | Principality of Guria | 1468..1829 | 11 | 4,827 | Principality of Guria |  | eu-19 |
| republic-of-genoa | Republic of Genoa | 1010..1795 | 38 | 28,150 | Republic of Genoa | spans 785 years in one Cliopatria row: probably successive states, split if so | eu-13 |
| kingdom-of-imereti | Kingdom of Imereti | 1468..1810 | 7 | 11,490 | Kingdom of Imereti |  | eu-19 |
| habsburg-monarchy | Habsburg Monarchy | 1487..1805 | 63 | 752,168 | Habsburg Austria;Habsburg monarchy |  | eu-09 |
| ethiopian-empire | Ethiopian Empire | 1272..1935 | 20 | 1,128,249 | Ethiopian Empire | spans 663 years in one Cliopatria row: probably successive states, split if so | af-01 |
| safavid-dynasty | Safavid Dynasty | 1502..1737 | 30 | 2,846,306 | Safavid dynasty |  | me-10 |
| principality-of-abkhazia | Principality of Abkhazia | 1468..1829 | 10 | 10,255 | Principality of Abkhazia |  | eu-19 |
| principality-of-mingrelia | Principality of Mingrelia | 1468..1810 | 9 | 13,251 | Principality of Mingrelia |  | eu-19 |
| kingdom-of-georgia | Kingdom of Georgia | 1010..1802 | 39 | 197,402 | Kingdom of Georgia | spans 792 years in one Cliopatria row: probably successive states, split if so | eu-19 |
| beylik-of-dulkadir | Beylik of Dulkadir | 1344..1515 | 8 | 30,831 | Beylik of Dulkadir |  | me-09 |
| qasimids | Qasimids | 1636..1802 | 9 | 360,698 | Rassid dynasty |  | me-10 |
| byzantine-empire | Byzantine Empire | 633..1474 | 91 | 2,337,636 | Byzantine Empire | the eastern-roman-empire dossier (395-632, done) hands over to this slug in 632/633 and asks for one colour and a found event written as a hand-over; Roman Empire, Eastern Roman Empire and Byzantine Empire are one continuous state in three Cliopatria rows; spans 841 years in one Cliopatria row: probably successive states, split if so | eu-05 |
| russian-empire | Russian Empire | 1721..1916 | 65 | 23,075,034 | Russian Empire |  | eu-17 |
| small-horde | Small Horde | 1564..1737 | 9 | 521,534 | Nogai Horde | shares Wikidata Q631210 with nogai-horde: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | ia-03 |
| spanish-empire | Spanish Empire | 1516..1879 | 76 | 11,353,699 | Spanish Empire;History of Spain (1808–1874) |  | am-06 |
| beylik-of-isfendiyar | Beylik of Isfendiyar | 1305..1462 | 9 | 49,106 | Candar dynasty | shares Wikidata Q2096678 with beylik-of-sinop: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | me-09 |
| kingdom-of-hungary | Kingdom of Hungary | 1000..1546 | 56 | 466,309 | Kingdom of Hungary |  | eu-15 |
| germiyanids | Germiyanids | 1305..1439 | 10 | 218,078 | Germiyanids |  | me-09 |
| beylik-of-karaman | Beylik of Karaman | 1305..1467 | 12 | 100,291 | Karamanids |  | me-09 |
| qajar-dynasty | Qajar Dynasty | 1788..1923 | 27 | 1,781,093 | Qajar dynasty |  | me-10 |
| ramadanid-emirate | Ramadanid Emirate | 1385..1515 | 5 | 24,477 | Ramadanid Emirate |  | me-09 |
| principality-of-transylvania | Principality of Transylvania | 1572..1695 | 10 | 111,717 | Principality of Transylvania (1570-1711) |  | eu-15 |
| empire-of-trebizond | Empire of Trebizond | 1206..1462 | 14 | 33,147 | Empire of Trebizond |  | eu-05 |
| saadi-sultanate | Saadi Sultanate | 1556..1740 | 10 | 841,482 | Saadi Sultanate |  | af-02 |
| kuwait | Kuwait | 1757..2024 | 5 | 17,395 | Kuwait | shares Wikidata Q817 with state-of-kuwait: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | me-10 |
| astrakhan-khanate | Astrakhan Khanate | 1468..1768 | 8 | 162,622 | Astrakhan Khanate |  | ia-02 |
| polish-lithuanian-commonwealth | Polish-Lithuanian Commonwealth | 1572..1793 | 45 | 950,896 | Polish-Lithuanian Commonwealth |  | eu-15 |
| zaporozhian-cossacks | Zaporozhian Cossacks | 1662..1774 | 8 | 121,080 | Zaporozhian Cossacks |  | eu-16 |
| aq-qoyunlu | Aq Qoyunlu | 1407..1511 | 10 | 1,701,512 | Aq Qoyunlu | shares Wikidata Q555994 with lu: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | me-09 |
| first-hellenic-republic | First Hellenic Republic | 1822..1940 | 23 | 206,605 | First Hellenic Republic |  | eu-18 |
| serbs | Serbs | 1805..1915 | 14 | 90,944 | Serbs |  | eu-18 |
| kingdom-of-kartli | Kingdom of Kartli | 1463..1705 | 3 | 130,082 | Kingdom of Kartli |  | eu-19 |
| don-cossacks | Don Cossacks | 1552..1641 | 4 | 126,354 | Don Cossacks |  | eu-16 |
| qara-qoyunlu | Qara Qoyunlu | 1375..1467 | 7 | 516,574 | Qara Qoyunlu |  | me-09 |
| despotate-of-epirus | Despotate of Epirus | 1206..1481 | 21 | 108,525 | Despotate of Epirus |  | eu-05 |

(87 more distant or short-lived neighbours omitted; the seeds data/polities/<slug>.json list them all; data/research-groups.json names every group's states.)

Rules for the list:

- One dossier per state, not per dynasty. A dynasty that replaces a dynasty on the same land without a break stays in the state's dossier as a `rename` event (Capetian to Valois; Tang to Wu Zhou to Tang). A new state on the same land (Yuan to Ming) gets its own dossier. Where Cliopatria has one row for successive states (Later Zhou -750..960, Kingdom of Italy 587..1946, Georgia 567..2024), split it: one dossier per state, each listing the Cliopatria Name in `cliopatria_names` and reviewing only the shapes of its own years; the slug of a split-off state is `slugify(<its name>)` (`history/tools/slug.py`), and your report lists every new slug under `new_slugs` so the colour agent can seed it.
- Where Cliopatria has two rows for one state (the 115 shared Wikidata ids in data/README.md: "Abbasid Caliphate" and "Abbasid Caliphate/Buyid Dynasty", "Kingdom of Navarre" and "Kingdom of Pamplona"), write one dossier under the slug of the earlier row, list both Names in `cliopatria_names`, and review both rows' shapes.
- Umbrella and relation entities (Names in parentheses, slugs `rel-...`) are not territory; do not write dossiers for them. Use them: the "(Allegiance of X to Y)" rows in your seed's `relations[]` are vassalage evidence that still needs a page to confirm the years.
- States Cliopatria lacks (a rebel state that held land, a protectorate's suzerain relation, a kingdom in sub-Saharan Africa, Oceania or the pre-Columbian Americas, a steppe polity): write a dossier anyway. `cliopatria_names: []`; every keyframe is a new one (`shape_id: "<slug>_<from year>"`, `from`, `to`, `correction` = the shape as a region spec with `text`, `verdict: "adjust"`); the ledger and the rest as usual. Slug: `slugify(name)`; check `polities.csv` and `history/polities/` that it is free, and report it under `new_slugs`. Rebel states that held land for a year or more (An Lushan's Yan, Huang Chao's Qi, the Taiping, the Confederacy) are `type: rebel`; their fighting zone is the government dossier's contest events.

## 7. Where to write

- `history/polities/<slug>.json`, one per state, exactly as the validator accepts it.
- `history/polities/_notes/me-10-a.md`: what you could not settle, per state: Cliopatria rows to split or merge, pages that would not load, disagreements between pages, states that need a dossier from another group, region names the gazetteer lacks. The reviewer and the gap-fillers read it first.
- Scratch, caches and downloads: `/tmp/claude-0/work/research-me-10-a/` (create it). Nothing else goes anywhere else: no files in `history/data/`, `history/tools/`, `history/compiled/` or `history/colours.json`, and nothing in the git repository at /home/claude/SkyscraperMaps.

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

- This is part a of 13 of group me-10 (Ottomans and the modern Middle East), split by founding year so that one agent carries at most 6 states or 45 Cliopatria shapes. The other parts run in parallel and write the group's other states (safavid-dynasty, yarubid-dynasty, qasimids, afsharid-iran, emirate-of-diriyah, sultanate-of-oman, zand-dynasty, bahrain, kuwait, house-of-khalifa, qajar-dynasty, muhammad-ali-dynasty, imamate-of-yemen, qatar-dynasty, trucial-states, emirate-of-nejd, emirate-of-jabal-shammar, khedivate-of-egypt, sultanate-of-muscat-and-oman, imamate-of-oman, qatar, kingdom-of-hejaz, asir, north-yemen, french-mandate-for-syria-and-lebanon, kingdom-of-egypt, pahlavi-dynasty, republic-of-turkey, kingdom-of-hejaz-and-nejd, kingdom-of-iraq, kingdom-of-saudi-arabia, lebanon, second-syrian-republic, kingdom-of-jordan, qatar-protectorate, palestinians, state-of-israel, republic-of-egypt, arab-federation, united-arab-republic, iraqi-republic, republic-of-syria, state-of-kuwait, ba-athist-syria, arab-socialist-ba-ath-party, people-s-democratic-republic-of-yemen, arab-republic-of-egypt, kingdom-of-bahrain, state-of-qatar, syria, united-arab-emirates, islamic-republic-of-iran, republic-of-yemen, gaza-hamas, republic-of-iraq); do not write or edit those. The states Cliopatria lacks that the scope names are written by the group's additions batch me-10-x; you add only rebel states and direct counterparts of your own states that no row covers, and list the rest under counterparts_needing_dossiers.

- Page budget per state (last column of the owned table; by number of Cliopatria shapes: up to 3 shapes 1-2 pages, up to 12 shapes up to 5 pages, up to 30 shapes up to 9 pages, more up to 14 pages). Open the state's article first, then the war and treaty pages the border moves need, until the budget is spent; keyframes you could not verify within the budget get verdict ok with the note 'unverified: page budget'. The reviewer knows the budget and judges thin against it.

- Earlier runs were cut short by the account's usage limit. If history/polities/<slug>.json already exists for one of your states, validate it (python3 -I history/tools/validate_dossier.py <file> --json); if it passes, keep it unchanged, read only its identity, the first ten ledger lines and its notes (not the whole file), count it in dossiers_written with validates true and 'kept from an earlier run' in its name field, and move on; if it fails, fix it. Notes from the earlier runs may exist as history/polities/_notes/<other-id>.md; read one only if it names your state.

- Keep your context small, because every turn re-reads it: never print a whole dossier, the schema or the example back into the conversation (read the example once, the schema once; grep what you need later); write each dossier with one heredoc or a short Python script; ask WebFetch for the specific dated facts (years, places, treaties) and quote only those; do not read other agents' dossiers in full (grep their ledger for the year you need). Write each dossier to the mount as soon as it validates, most eventful states first; if you run low on context, stop cleanly: write the notes file, list the unwritten states under gaps with why 'not reached: context', and return the report.

- Run Python from your scratch directory with PYTHONDONTWRITEBYTECODE=1 and python3 -I. WebFetch is the only route to Wikipedia (curl is refused). Natural Earth spellings for countries and provinces are in data/gazetteer/countries.jsonl and admin1.jsonl. Known-bad Cliopatria rows for your states are in the owned table's known-problems column and in data/README.md; start from those notes.

- Also save your final JSON report to history/notes/phase-b/reports/me-10-a.json before returning it (same content), so that it survives if the message is cut.

## 11. The report you return

Your final message is one JSON object and nothing else:

```json
{
  "group_id": "me-10-a",
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
  "notes_path": "history/polities/_notes/me-10-a.md",
  "problems": ["anything the orchestrator must know: tool failures, rows that should be reassigned, a state that is really two"]
}
```

`python3 -I history/tools/validate_dossier.py history/polities/<slug>.json --json` prints the per-dossier counts in this shape.
