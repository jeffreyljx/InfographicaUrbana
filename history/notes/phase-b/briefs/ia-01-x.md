# Research brief: group ia-01-x (Xiongnu to the Türks (part x))

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

(none)

Context (neighbours and counterparts you will read and cite as counterparts, but another group writes them; do not create or edit their files):

| slug | Cliopatria Name | first..last | shapes | max area (km2) | Wikipedia title | known problems | group |
| --- | --- | --- | --- | --- | --- | --- | --- |
| abbasid-caliphate | Abbasid Caliphate | 750..1259 | 37 | 8,151,272 | Abbasid Caliphate | shares Wikidata Q12536 with buyid-dynasty, abbasid-caliphate-buyid-dynasty: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | me-08 |
| avar-khaganate | Avar Khaganate | 561..805 | 22 | 1,022,315 | Pannonian Avars |  | eu-06 |
| balasagan | Balasagan | 638..646 | 2 | 74,449 | Balasagan |  | eu-19 |
| byzantine-empire | Byzantine Empire | 633..1474 | 91 | 2,337,636 | Byzantine Empire | the eastern-roman-empire dossier (395-632, done) hands over to this slug in 632/633 and asks for one colour and a found event written as a hand-over; Roman Empire, Eastern Roman Empire and Byzantine Empire are one continuous state in three Cliopatria rows; spans 841 years in one Cliopatria row: probably successive states, split if so | eu-05 |
| cao-cao | Cao Cao | 197..223 | 3 | 1,377,126 | Cao Cao | shares Wikidata Q204077 with cao: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | ea-03 |
| cao-wei | Cao Wei | 224..264 | 3 | 2,972,911 | Cao Wei | shares Wikidata Q320930 with wei: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | ea-03 |
| cimmerian-bosporus | Cimmerian Bosporus | -404..372 | 7 | 40,185 | Bosporan Kingdom | spans 776 years in one Cliopatria row: probably successive states, split if so | eu-01 |
| dai | Dai | -208..-204 | 2 | 57,016 | Eighteen Kingdoms | shares Wikidata Q5349053 with jibei, chang-shan, han-2, henan, jiaodong, jiujiang, liaodong, linjiang, sai, yin, yong: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | ea-02 |
| eastern-roman-empire | Eastern Roman Empire | 395..632 | 36 | 2,602,791 | Byzantine Empire | shares Wikidata Q12544 with roman-empire: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | eu-05 |
| eastern-wei | Eastern Wei | 534..554 | 2 | 623,760 | Eastern Wei |  | ea-03 |
| first-bulgarian-empire | First Bulgarian Empire | 682..1017 | 31 | 428,320 | First Bulgarian Empire |  | eu-18 |
| georgia | Georgia | 567..2024 | 17 | 86,640 | Georgia | 567..2024 runs from Iberia to the republic: split; 567-576 is Lazica (see the eastern-roman-empire dossier notes); spans 1457 years in one Cliopatria row: probably successive states, split if so | eu-19 |
| ghaznavid-empire | Ghaznavid Empire | 962..1209 | 18 | 2,994,472 | Ghaznavids |  | me-08 |
| ghurid-dynasty | Ghurid Dynasty | 1152..1209 | 6 | 2,143,165 | Ghurid dynasty |  | sa-04 |
| goguryeo | Goguryeo | -36..681 | 26 | 408,926 | Goguryeo | spans 717 years in one Cliopatria row: probably successive states, split if so | jk-02 |
| gojoseon | Gojoseon | -197..-92 | 3 | 81,320 | Gojoseon | shares Wikidata Q28405 with joseon: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | jk-02 |
| great-seljuk-empire | Great Seljuk Empire | 1040..1201 | 17 | 4,142,668 | Seljuk Empire |  | me-09 |
| greco-bactrian-kingdom | Greco-Bactrian Kingdom | -247..-127 | 7 | 1,364,110 | Greco-Bactrian Kingdom |  | me-05 |
| greek-city-states | Greek City-States | -800..83 | 52 | 206,488 | Polis | spans 883 years in one Cliopatria row: probably successive states, split if so | eu-01 |
| greek-colonies | Greek Colonies | -271..-226 | 6 | 82,558 | Greek colonisation |  | eu-02 |
| gupta-empire | Gupta Empire | 324..554 | 19 | 2,494,996 | Gupta Empire |  | sa-02 |
| halych-volhynia-occupation | Halych-Volhynia occupation | 1056..1240 | 10 | 452,468 | Kingdom of Galicia-Volhynia | shares Wikidata Q239502 with principality-of-galicia-volhynia, galicia-volhynia: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | eu-16 |
| hamdanid-emirates | Hamdanid Emirates | 936..1259 | 23 | 1,101,466 | Hamdanid dynasty | 936-1259 with a centroid in Pakistan/Iran; check | me-08 |
| han | Han | -404..-203 | 9 | 1,310,598 | Han (state) | slug collision: "Han" (-404..-203) is `han`; "Hán" (-206..-204) is `han-2`; shares Wikidata Q1968654 with beylik-of-saruhan: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | ea-01 |
| han-dynasty | Han Dynasty | -202..237 | 27 | 4,582,897 | Han dynasty | shares Wikidata Q1068371 with chauhan-dynasty: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | ea-02 |
| hunnic-empire | Hunnic Empire | 426..673 | 10 | 1,913,270 | Huns | shares Wikidata Q45813 with huns: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | eu-06 |
| indo-greeks | Indo-Greeks | -126..13 | 8 | 784,828 | Indo-Greek Kingdom |  | me-05 |
| indo-parthians | Indo-Parthians | 1..90 | 5 | 487,435 | Indo-Parthian Kingdom |  | sa-02 |
| indo-scythians | Indo-Scythians | -144..282 | 16 | 1,496,248 | Indo-Scythians |  | sa-02 |
| karkota-dynasty | Karkota Dynasty | 592..859 | 8 | 208,995 | Karkota dynasty |  | sa-03 |
| kashmir | Kashmir | 626..1343 | 26 | 201,742 | Kashmir | spans 717 years in one Cliopatria row: probably successive states, split if so | sa-03 |
| khwarezmid-dynasty | Khwarezmid Dynasty | 1094..1201 | 6 | 614,269 | Anushtegin dynasty |  | me-09 |
| khwarezmid-empire | Khwarezmid Empire | 1202..1235 | 6 | 4,017,837 | Khwarazmian Empire |  | me-09 |
| kievan-rus | Kievan Rus' | 882..1240 | 15 | 1,199,848 | Kievan Rus' | alive 1040-1235 beside its principalities (overlap); decide where it ends; shares Wikidata Q1108445 with rus: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | eu-16 |
| kingdom-of-lazica | Kingdom of Lazica | 638..777 | 6 | 23,545 | Lazica | shares Wikidata Q136884 with lazica: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | eu-19 |
| kushan-empire | Kushan Empire | 43..237 | 11 | 2,267,302 | Kushan Empire | shares Wikidata Q25979 with eastern-kushans, western-kushans: if the rows are one state, one dossier under the earlier slug with both Names in cliopatria_names; if they are different states, say so in notes | sa-02 |
| later-liang | Later Liang | 387..406 | 3 | 237,231 | Later Liang (Sixteen Kingdoms) |  | ea-03 |
| later-qin | Later Qin | 387..416 | 8 | 573,288 | Later Qin |  | ea-03 |
| later-yan | Later Yan | 387..409 | 6 | 502,851 | Later Yan |  | ea-03 |
| liao-dynasty | Liao Dynasty | 911..1125 | 9 | 1,924,516 | Liao dynasty |  | ea-05 |

(42 more distant or short-lived neighbours omitted; the seeds data/polities/<slug>.json list them all; data/research-groups.json names every group's states.)

Rules for the list:

- One dossier per state, not per dynasty. A dynasty that replaces a dynasty on the same land without a break stays in the state's dossier as a `rename` event (Capetian to Valois; Tang to Wu Zhou to Tang). A new state on the same land (Yuan to Ming) gets its own dossier. Where Cliopatria has one row for successive states (Later Zhou -750..960, Kingdom of Italy 587..1946, Georgia 567..2024), split it: one dossier per state, each listing the Cliopatria Name in `cliopatria_names` and reviewing only the shapes of its own years; the slug of a split-off state is `slugify(<its name>)` (`history/tools/slug.py`), and your report lists every new slug under `new_slugs` so the colour agent can seed it.
- Where Cliopatria has two rows for one state (the 115 shared Wikidata ids in data/README.md: "Abbasid Caliphate" and "Abbasid Caliphate/Buyid Dynasty", "Kingdom of Navarre" and "Kingdom of Pamplona"), write one dossier under the slug of the earlier row, list both Names in `cliopatria_names`, and review both rows' shapes.
- Umbrella and relation entities (Names in parentheses, slugs `rel-...`) are not territory; do not write dossiers for them. Use them: the "(Allegiance of X to Y)" rows in your seed's `relations[]` are vassalage evidence that still needs a page to confirm the years.
- States Cliopatria lacks (a rebel state that held land, a protectorate's suzerain relation, a kingdom in sub-Saharan Africa, Oceania or the pre-Columbian Americas, a steppe polity): write a dossier anyway. `cliopatria_names: []`; every keyframe is a new one (`shape_id: "<slug>_<from year>"`, `from`, `to`, `correction` = the shape as a region spec with `text`, `verdict: "adjust"`); the ledger and the rest as usual. Slug: `slugify(name)`; check `polities.csv` and `history/polities/` that it is free, and report it under `new_slugs`. Rebel states that held land for a year or more (An Lushan's Yan, Huang Chao's Qi, the Taiping, the Confederacy) are `type: rebel`; their fighting zone is the government dossier's contest events.

## 7. Where to write

- `history/polities/<slug>.json`, one per state, exactly as the validator accepts it.
- `history/polities/_notes/ia-01-x.md`: what you could not settle, per state: Cliopatria rows to split or merge, pages that would not load, disagreements between pages, states that need a dossier from another group, region names the gazetteer lacks. The reviewer and the gap-fillers read it first.
- Scratch, caches and downloads: `/tmp/claude-0/work/research-ia-01-x/` (create it). Nothing else goes anywhere else: no files in `history/data/`, `history/tools/`, `history/compiled/` or `history/colours.json`, and nothing in the git repository at /home/claude/SkyscraperMaps.

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

- Group scope (from data/research-groups.json): Researches the steppe from the Scythians to the eve of Chinggis Khan: Scythia, Xiongnu, Yuezhi, Wusun, Xianbei, Rouran, the Iranian Huns (Kidarites, Xionites, Hephthalites), the Türk khaganates, Uyghurs, Yenisei Kyrgyz, Karluks, Karakhanids, the Tarim oasis states, Khazars, Bulgars, Oghuz, Kimek and Cumans, and the Qara Khitai. Cliopatria lacks the Sarmatians and Alans of the Pontic steppe, the Sakas, the Hephthalite-Sasanian frontier, the Pechenegs, the Cumans beyond one tiny shape, the Naiman, Kerait and Merkit before 1206, and the Tarim states beyond Khotan and Qocho; add them.

- This is the additions batch of group ia-01 (Xiongnu to the Türks): you own no Cliopatria row. Your job is the states Cliopatria lacks that the scope names (and any other state of this region and era that held land for ten years or more and has a Wikipedia article), each as a new dossier: cliopatria_names [], every keyframe new (shape_id <slug>_<from>, from, to, correction as a region spec with text, verdict adjust), ledger, wars, certainty, sources as usual, 2-5 pages per state. Check polities.csv and history/polities/ that the slug is free, and list every one under new_slugs. Aim for the 6-10 most important first (most land for the longest). The group's Cliopatria states are written by parts a, b, c, d, e, f, g in parallel; do not write those; cite them as counterparts.

- Page budget per state (last column of the owned table; by number of Cliopatria shapes: up to 3 shapes 1-2 pages, up to 12 shapes up to 5 pages, up to 30 shapes up to 9 pages, more up to 14 pages). Open the state's article first, then the war and treaty pages the border moves need, until the budget is spent; keyframes you could not verify within the budget get verdict ok with the note 'unverified: page budget'. The reviewer knows the budget and judges thin against it.

- Earlier runs were cut short by the account's usage limit. If history/polities/<slug>.json already exists for one of your states, validate it (python3 -I history/tools/validate_dossier.py <file> --json); if it passes, keep it unchanged, read only its identity, the first ten ledger lines and its notes (not the whole file), count it in dossiers_written with validates true and 'kept from an earlier run' in its name field, and move on; if it fails, fix it. Notes from the earlier runs may exist as history/polities/_notes/<other-id>.md; read one only if it names your state.

- Keep your context small, because every turn re-reads it: never print a whole dossier, the schema or the example back into the conversation (read the example once, the schema once; grep what you need later); write each dossier with one heredoc or a short Python script; ask WebFetch for the specific dated facts (years, places, treaties) and quote only those; do not read other agents' dossiers in full (grep their ledger for the year you need). Write each dossier to the mount as soon as it validates, most eventful states first; if you run low on context, stop cleanly: write the notes file, list the unwritten states under gaps with why 'not reached: context', and return the report.

- Run Python from your scratch directory with PYTHONDONTWRITEBYTECODE=1 and python3 -I. WebFetch is the only route to Wikipedia (curl is refused). Natural Earth spellings for countries and provinces are in data/gazetteer/countries.jsonl and admin1.jsonl. Known-bad Cliopatria rows for your states are in the owned table's known-problems column and in data/README.md; start from those notes.

- Also save your final JSON report to history/notes/phase-b/reports/ia-01-x.json before returning it (same content), so that it survives if the message is cut.

## 11. The report you return

Your final message is one JSON object and nothing else:

```json
{
  "group_id": "ia-01-x",
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
  "notes_path": "history/polities/_notes/ia-01-x.md",
  "problems": ["anything the orchestrator must know: tool failures, rows that should be reassigned, a state that is really two"]
}
```

`python3 -I history/tools/validate_dossier.py history/polities/<slug>.json --json` prints the per-dossier counts in this shape.
