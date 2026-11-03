# Historical borders master plan

18 Oct 2026 · written by the "Historical empire borders" thread for Jeffrey. Also a Claude Doc: https://claude.ai/code/artifact/e1b82c1d-d4e2-4aa7-bc81-e5c5439052fe

## What the reference videos do well

The six distinct videos (one link was sent twice) split into two kinds: five "every year" or "every month" animations, which are what we are building, and one narrated documentary. The container cannot play YouTube, so the notes below come from each video's page metadata plus the channels' established house style; points marked "house style" are inferred from the channel, not seen in that video.

| Video | Span and step | What it does well | What to avoid |
| --- | --- | --- | --- |
| [China: 3,000 Years of History in a Minute](https://www.youtube.com/watch?v=zdHkY3XYHKA) (EarthDirect, 2013) | c. 1000 BCE to today, one frame per dynasty map | A fixed viewport over China and Inner Asia makes the pulse of unification and fragmentation legible in one glance. Built on Pojanji's Wikipedia dynasty maps (CC BY 3.0), so each frame is sourced. | Jumps between maps with nothing in between; neighbours, vassals and the steppe are blank. |
| [The History of Tang Dynasty: Every Year](https://www.youtube.com/watch?v=jdqO4bMhLIk) (EC, 2018) | 618 to 907, yearly, Wu Zhou 690 to 705 marked as its own era | Treats a dynastic interruption as an era, not a new state. House style: ruler portrait and reign dates beside the map, protectorates (Anxi, Beiting, Annam) in a lighter tint, rebellions (An Lushan) as their own colour, neighbours (Tibet, Türks, Uyghurs, Nanzhao, Silla) all coloured. | Posts an erratum for a wrong ruler in 860: the ruler strip needs its own source check. |
| [The Abbasid Caliphate: Every Year (745 to 1262)](https://www.youtube.com/watch?v=-ETEcnxuZe0) (Anwoo Mapping History, 2023) | 745 to 1262, yearly, 20 captioned chapters from the Third Fitna to the continuation in Cairo | Separates nominal from effective control: autonomous dynasties (Tahirids, Samanids, Buyids, Seljuks) sit inside the caliphate as allegiance tints. Every chapter is a dated event caption, and the sources are in a linked document. Keeps the "shadow caliphate" in Cairo as a continuation. | None to avoid; this is the closest model for our event ledger and vassal tints. |
| [The USSR: Summary on a map](https://www.youtube.com/watch?v=cUvpE_8A9kU) (Geo History, 2022) | 1914 to 1991, 14 narrated chapters | Fronts move as animated lines and arrows; chapters give the story a spine. | A documentary, not a yearly dataset: no fixed time step, so nothing here is reusable as data. |
| [Territorial History of the USA: Every Month for 400 Years](https://www.youtube.com/watch?v=9UE9uu9fKSg) (EarthDirect, 2013) | 1629 to 2013, monthly; state borders from 1784 | Finer than a year where the sources allow it. Year and month fixed top right. Grey for unorganised or independent land that was later absorbed. Built from the Newberry Library's Atlas of Historical County Boundaries, so counties are the building blocks: a cell-based approach, which is what we adopt. | Monthly steps only work where a dated administrative record exists (USA, modern Europe); elsewhere a year is the honest step. |
| [The History of England and the United Kingdom: Every Year](https://www.youtube.com/watch?v=jpO9lsbefWE) (EmperorTigerstar, 2017) | Roman Britain to 2017, yearly, ending with the Commonwealth | The genre's reference style (house style): flat fills on a plain basemap, year counter in a corner, one canonical colour per state for its whole life, striped fill for occupied or contested land, pauses and captions at key events, the Commonwealth shown as an association rather than control. | Colour changes that are not explained; a Commonwealth-style association must never read as territory. |

What we copy: a fixed year counter; one colour per state kept for its whole life; a lighter tint of the suzerain's colour for vassals and protectorates; striped or blended fill for contested land; dated captions for the events that move a border; a ruler strip where the record supports it; a visible source for every shape; and play speed that slows in eventful years, as ScraperMap's Time capsule already does.

What we add that none of them have: every state on one map at once, so neighbours are never blank; a slider the viewer controls instead of a fixed film; a page per state with its area over time; and an edge style that says how certain a border is.

## The standard: how the map tells each state's story

Every state is drawn by the same twelve rules from its first year to its last, so a viewer can read any century without a legend. The research agents collect what these rules need; the rendering agents apply them.

1. **Birth.** A state appears in its founding year at its core, labelled, with a caption naming the event ("618: Li Yuan proclaims the Tang at Chang'an").
2. **One colour for life.** A state keeps its colour from first year to last. A change of dynasty within the same state (Tang to Wu Zhou to Tang, Capetian to Valois) keeps the colour; a new state on the same land (Yuan to Ming) takes a new one. Successors that claim continuity after a split (Western and Eastern Rome) take related hues; unrelated successors take distinct ones.
3. **Expansion.** Land gained is outlined bright for its first year, as the Time capsule rings new towers, so Play shows where a state is moving.
4. **Levels of control.** Directly ruled land is the full colour. Vassals, protectorates, tributaries and client states are a lighter tint of the suzerain's colour with their own outline and label. Occupied land is hatched in the occupier's colour over the owner's. Spheres of influence and associations (the Commonwealth, the Holy Roman Empire after 1648) are never coloured as territory.
5. **Civil war and rebellion.** Rebel-held land takes its own hatched colour until the rebels win, and become a state, or are crushed.
6. **Contested land.** Land two states are fighting over shows the blend of their two colours and merges into the winner's colour when the fighting ends or the treaty is signed (rules below).
7. **Collapse and partition.** When a state ends, its land passes to its successors in that year with a caption; land that falls out of every state's control returns to the neutral colour.
8. **Nobody's land.** Territory outside any state (hunter-gatherers, stateless peoples, unorganised land) is a neutral grey, never blank, so emptiness is a statement rather than a gap. Before 3400 BCE, archaeological cultures (Ubaid, Yangshao, Vinča, Naqada) are drawn in muted hatched tones and labelled as cultures, not states.
9. **Certainty.** Borders fixed by treaty or survey are drawn sharp; approximate frontiers (steppe, forest, desert, most of the ancient world) are drawn soft or dashed, and the state's page says which.
10. **Labels, capitals and rulers.** Label size follows area. The capital is a dot that moves when it moves (Rome to Constantinople, Nara to Kyoto). A ruler strip shows where the record supports one (China, Rome, the caliphates, Europe from about 800).
11. **Pacing.** Play slows in years with more change, like the Time capsule's per-year delay, and pauses on captioned events.
12. **The state page.** Clicking a state opens a page like the tower and station pages: name and aliases, years, area over time as a chart, capitals, rulers, the dated ledger of territorial events with their sources, and links to predecessors and successors.

The time step is one year everywhere. Where a dated administrative record supports it (the United States from 1784, Europe from 1789, both World Wars), events carry a month as well, so a finer step can be added later without re-collecting.

## Spatial representation: cells, keyframes and a ledger

A border is not stored as hand-placed coordinate chains. It is stored in three layers, and only the first is written by hand.

1. **The truth layer: a dossier per state.** Dated keyframe shapes (a polygon per period, from Cliopatria or drawn where none exists), plus a ledger of dated territorial events that name regions in words: "1066: gains the Kingdom of England", "751: loses the Tarim Basin west of Kucha to the Abbasids", "1803: buys Louisiana (the Mississippi basin west of the river)", "within 150 km of Samarkand". A gazetteer turns those names into cells, so a researcher never types coordinates and a correction is a sentence, not a redraw.
2. **The compiled layer: a hexagon grid.** The world's land is cut into H3 hexagons at resolution 5: 524,441 land cells of about 253 km² each, 10 km across (counted from Natural Earth's 50 m land by the Phase A grid builder; an earlier estimate of 214,699 was wrong). Each cell carries a timeline: (year, owner, status), where status is direct, vassal, occupied or contested with a second claimant. Resolution 6 (about 3.7 million cells, 36 km², 3.7 km across) is used where borders are fine and well documented: Europe, the Levant, Mesoamerica, Japan, the eastern United States. H3 cells nest, so the two resolutions mix cleanly.
3. **The display layer.** For each year in which anything changes, the cells of each state are merged into polygons, smoothed, clipped to the modern coastline and packed by era for the static site. Edge style (sharp or soft), tint (vassal), hatch (occupied) and blend (contested) are properties of the polygons, so the map needs no computation at view time.

Why cells rather than polygons as the working form: no slivers or overlaps between neighbours; merging conquered land is set union; a year's change is a short list of cells, so yearly storage is small; a contested cell simply has two claimants; and adjacency between states, which the colour rule needs, is read off the grid. It is also how the US video was built, from counties.

Time is an integer year, negative for BCE, as Cliopatria does; an event may carry a month. Sizes: Cliopatria's raw shapes are 173 MB of GeoJSON with 3.8 million vertices; the compiled cell timelines should pack to about 10 MB, and the display chunks to a few MB per era, loaded on demand like the metro data.

## Foundation data: what already exists

The single most important finding of this review: an open, citable dataset of every polity's borders from 3400 BCE to 2024 already exists, and we can build on it instead of drawing 5,400 years of borders from scratch. [Cliopatria](https://github.com/Seshat-Global-History-Databank/cliopatria) (Seshat Global History Databank, published in [Scientific Data, 2025](https://www.nature.com/articles/s41597-025-04516-9)), licence CC BY 4.0, downloaded and inspected today (v0.2.1).

| Source | What it holds | Licence | Reachable from the container | Use |
| --- | --- | --- | --- | --- |
| Cliopatria v0.2.1 | 1,637 named polities, 13,797 dated shapes, 3400 BCE to 2024; each row has a Wikipedia title and Wikidata id; 93 umbrella entities (British Empire, Holy Roman Empire) and "Allegiance of X to Y" relations give the vassal hierarchy | CC BY 4.0 | Yes (raw.githubusercontent.com) | The keyframe foundation for every state |
| Natural Earth 10m and 50m | Coastlines, lakes, rivers, modern countries and provinces | Public domain | Yes (S3) | Coastline clipping, the gazetteer, the modern layer check |
| [historical-basemaps](https://github.com/aourednik/historical-basemaps) (Ourednik) | About 40 world snapshots from 123,000 BCE to 2010 with cultural regions and a border-precision field | GPL-3 | Yes | Cross-check only; the licence does not fit copying into the site |
| Wikipedia | Articles, infobox areas, campaign and treaty dates, dynasty lists | CC BY-SA 4.0 | Through WebFetch only (not curl) | The event ledger, rulers, capitals |
| Wikidata, OpenHistoricalMap, Overpass, Zenodo, archive.org | Structured dates, crowd-drawn historical borders | various | No | Not used |

What Cliopatria gives us, measured on the file: the 1,544 leaf polities (umbrella entities removed) form a near-partition of the land, with overlaps below 2 percent of total area in every sampled year, so they can be loaded straight into the cell grid. The median shape lasts 8 years; 40 percent of shapes last 5 years or less and 64 percent 10 years or less. Between 1700 and 2024 the spacing is close to yearly for the great powers; the Tang has 32 shapes over 288 years, the Abbasids 74 over 510, the Russian Empire 65 over 196, the Ottomans 138 over 619, the Mali Empire 9 over 376.

What it lacks, which the research step supplies: nothing before 3400 BCE; year-by-year change between its keyframes; wars and contested zones; capitals, rulers and captions; thin coverage of Oceania (4 polities), sub-Saharan Africa (82), the pre-Columbian Americas and the steppe; some rows to check (Later Zhou dated 750 BCE to 960, Kingdom of Italy 587 to 1946, Georgia 567 to 2024, the Dutch East Indies overlapping the Batavian Republic in 1800); and its names mix dynasties and states, which the dossiers normalise.

Attribution: the site's method page and the map's corner will carry "Boundaries: Cliopatria, Seshat Global History Databank, CC BY 4.0, adapted", and every state page cites the dossier's own sources.

## Collection method: the dossier each research agent writes

Each research agent owns a region and era, receives the Cliopatria polities that fall in it (name, years, number of shapes, Wikipedia title) and writes one dossier per state to history/polities/, plus a notes file saying what it could not settle. A dossier has six parts.

| Part | Content | Rule |
| --- | --- | --- |
| Identity | Slug, name, native and alternative names, type (state, dynasty, culture, colony, rebel), civilisation family, start and end year (month if known), predecessors and successors with the land handed over, capitals with years and coordinates, rulers where a documented list exists | One dossier per state, not per dynasty, unless the dynasty is a new state |
| Keyframe review | For each Cliopatria shape: ok, adjust or wrong, with the correction written as a region ("should not include Sogdia before 751"); missing periods get new keyframes described the same way | Every verdict cites the page it rests on |
| Event ledger | Dated events: gain, loss, contest start and end, vassal start and end, occupation start and end, capital move, rename, split, merge. Each names the region in words, the counterpart state, the source and a confidence of 1 to 3 | Every border move between two keyframes is explained by at least one event |
| Wars | Name, years, belligerents, the zones fought over, outcome | Feeds the contested-territory rule |
| Certainty | Per era: sharp (treaty or survey) or soft (approximate frontier) | Drives the edge style |
| Sources | Every page opened, with URL | A search snippet is not a source |

Regions are named, not drawn: a province, a river basin ("between the Oxus and the Jaxartes"), a modern administrative unit, a radius around a city, or an existing Cliopatria shape ("the Tahirid territory of 830"). A gazetteer agent compiles every region name used in the ledgers into cells, from Cliopatria's own shapes, Natural Earth provinces and rivers, and city coordinates with a radius. Only when a region cannot be named does a researcher give a fallback polygon of up to 12 points.

Sources, in order: Wikipedia through WebFetch (the only route open to the agents; infobox areas double as a sanity check on Cliopatria's Area field), then the Wikipedia article's own cited works where the page is thin, then the Seshat polity pages linked from Cliopatria's SeshatID. Agents open pages; they do not quote search results.

Verification: every dossier goes to an adversarial reviewer agent that tries to break it: years out of order, a gain with no matching loss in the neighbour's dossier, a keyframe that contradicts the ledger, an area a factor of two off the infobox. Failures go back to the author. A second round of gap-filler agents is run for every state the reviewers mark thin, until a round adds nothing.

## Colours

One registry, history/colours.json, gives every state one colour for its whole life, and no two states that touch in any year may have colours a reader could confuse. The registry is owned by one colour agent; rendering agents may not invent colours.

- **Conventional colours first.** About 200 major states take the colours readers already know from Wikipedia, Euratlas and the reference videos, where those do not collide: Rome red, Byzantium purple, France blue, England and Britain pink-red, Spain yellow-orange, Portugal green, the Ottomans olive, Russia dark green, the Mongols a warm brown, the Chinese dynasties a warm family (Han vermilion, Tang gold, Song teal-green, Ming a deeper red, Qing imperial yellow). Where two conventions clash on a shared border (Russia and the Ottomans are both green by convention), the smaller state moves.
- **Families.** Dynastic continuity within a state keeps the hue (Tang and Wu Zhou). A successor that claims continuity (Eastern Rome after 395) takes a neighbouring hue; an unrelated successor takes an unrelated one.
- **The neighbour rule.** For every year the compiled grid gives the adjacency graph of states; the colour agent checks that every pair of neighbours differs by at least a set distance in OKLab (a perceptual colour space) and resolves clashes by recolouring the smaller state everywhere, so the colour-for-life rule holds. Small states without a convention are coloured from a 24-hue wheel by graph colouring, lightest in dense regions (the Holy Roman Empire's minor states, the taifas, the Warring States).
- **Status tints.** A vassal or protectorate is its suzerain's colour at reduced saturation and raised lightness, with its own outline. Occupied land is the occupier's colour hatched over the owner's. Contested land is the OKLab midpoint of the two claimants (blue and red give purple, as asked) with a fine diagonal hatch so the blend also reads for colour-blind viewers. Nobody's land is a warm neutral grey. Cultures before 3400 BCE are desaturated pastels with a dotted fill.
- **The map's own colours.** The basemap carries no modern borders or labels, only land, water, rivers and relief, so the state colours are the only colours on the map.

## Contested territory

Land that two states are fighting over is drawn in the blend of their two colours from the first campaign that takes ground until the fighting ends, then merges into the winner. The ledger carries this as a pair of events, contest start and contest end, naming the zone and both claimants.

- **When a contest starts.** With the first campaign that actually takes or holds ground, not with a declaration of war. A war with no territorial result (most of them) shades nothing.
- **What the zone is.** The land that changed hands, or was fought over and kept, as the sources describe it: English Aquitaine and Normandy in the Hundred Years' War; Sicily, then Iberia, in the Punic Wars; the Hexi corridor and the Tarim in the Tang-Tibetan wars; Hungary between the Ottomans and the Habsburgs; Alta California and New Mexico in 1846 to 1848. Where a source says only "the frontier", the gazetteer takes a band one or two cells wide on either side of the border.
- **When it ends.** At the treaty, the last battle or the de facto end of fighting, whichever the sources date. The cells go to the winner in full colour with the bright first-year edge; land that returns to its old owner simply reverts.
- **Occupation is not contest.** Land held without active fighting (German-occupied France 1940 to 1944, the Allied zones of Germany 1945 to 1949) is hatched in the occupier's colour over the owner's, and becomes the occupier's only if annexed.
- **Civil wars and rebellions.** The rebels are a state of type rebel with their own colour; land they hold is theirs; the fighting zone between them and the government takes the blend. If they win, the rebel colour becomes the state's new colour (a new state) or the old colour is kept (a restoration), by the colour-for-life rule.
- **Long fronts.** For wars with a documented front that moved year by year (both World Wars, the Taiping, the Eastern Front), the ledger gives the front by year, and the decade agents draw the occupied and contested zones from it.

The blend is the midpoint of the two colours in OKLab, so blue against red gives purple, as asked, with a fine hatch so the zone also reads without colour.

## Rendering plan: 76 century agents and 43 decade agents

The map builders take the verified dossiers and produce the year-by-year cell ownership, one agent per window: 76 centuries from 6000 BCE to 1600 and 43 decades from 1600 to 2030, as asked. They run in parallel because the handoff years are fixed before they start.

1. **Anchors first (a script, not an agent).** A compiler loads the reviewed keyframes and the gazetteered ledger and computes the full cell ownership at every window boundary: each century start before 1600 and each decade start after. These 119 anchors are the fixed handoff states.
2. **Each window agent** receives its start and end anchors, the dossiers of every state alive in its window, the colour registry and the gazetteer, and writes history/compiled/\<window>.json: for each year, the cells that change owner or status, the contests open that year, the captions for events in the window, and a handoff note listing anything in the dossiers that disagrees with the end anchor. It applies the twelve rules of the standard; it does not invent borders or colours. Windows with no events are nearly empty; the busy ones (the 1200s, every decade from 1790) get the most effort.
3. **Seam checks.** For each of the 118 seams a checker agent compares the last year of one window with the first year of the next: same owners on every cell, same colours, open contests carried over. Disagreements go back to both agents with the seam noted, and the pair is re-run until the seam is clean. This is the neighbour-to-neighbour communication asked for, made mechanical so it cannot be skipped.
4. **Colour check per window.** Each window's years are checked against the neighbour rule; any clash goes to the colour agent, which recolours the smaller state everywhere.
5. **Visual QA.** Every hundred years (every ten after 1600) a snapshot is rendered and compared with Cliopatria's own shape and with a reference map; a reviewer agent lists the differences and whether each is a correction or an error.
6. **Packaging.** The window files are merged into the site's per-era chunks and the per-state pages' data (area per year from the cells, the ledger, the captions).

Time step: one year everywhere; events with a month are kept, so a monthly step can be added later for the United States and the World Wars without re-collecting.

## Site integration: a fourth mode

The finished map becomes a fourth mode in the menu under the logo, beside ScraperMap, TransitMap and IndustryMap: CartaHistoria at /history/ (Jeffrey named it on 1 Nov 2026, replacing the default EmpireMap; the /history/ path is the default that matches /metro/ and /industry/). It joins MODES in src/lib/modes.ts and gets its own page title, as the metro page did.

- **The year dock** is the metro map's MetroYears dock adapted: the range runs 6000 BCE to 2026, the bar chart shows the area that changed hands each year, Play slows in eventful years and pauses on captions, and the slider has two speeds (centuries before 1500, years after) so the modern era is not crushed into a sliver. The URL carries ?year= as the Time capsule does.
- **The map** is MapLibre, as the other modes, but on a plain basemap: land, water, rivers and relief only, no modern borders or labels, since those are anachronistic on a map of 800. The satellite view stays available. States are fill layers from the per-era chunks, labels sized by area, capitals as dots.
- **The state panel and pages** follow the tower and station pattern: click a state for its panel; /history/\<slug>/ holds the full page with the area chart, rulers, ledger and sources. Search finds a state by any of its names and jumps to its first year.
- **Branch and deploy.** The work goes on a branch off origin/main (history), building Vercel previews; merging to main, which is production, waits for Jeffrey's go-ahead and is coordinated with the Metro history map thread, which owns the merge order.
- **Data size.** The cell timelines pack to about 10 MB and the display chunks to a few MB per era, loaded on demand like the metro data (2 MB).

## Orchestration

This thread is the master. It runs the agents as workflows (Ultracode), 16 at a time, in six phases; each phase's output is checked before the next starts.

| Phase | Agents | Produces | Checked by |
| --- | --- | --- | --- |
| A. Foundation (now) | 4: ingest, gazetteer, colour seed, compiler | Cliopatria loaded into the polity table and the cell grid; gazetteer v0 from Cliopatria shapes, Natural Earth provinces and rivers; the dossier schema and the agent briefs; colours.json seeded with the conventional 200 | This thread, on sample years |
| B. Research | 76 regional agents (roster below), then one reviewer per dossier batch, then gap-fillers until a round adds nothing | history/polities/\<slug>.json, one per state, with notes | Adversarial reviewers; neighbour consistency (every gain has a loss) |
| C. Anchors | script | Cell ownership at the 119 handoff years | Area per state against the dossiers |
| D. Rendering | 76 century + 43 decade agents, 118 seam checkers, the colour agent | history/compiled/\<window>.json | Seam checks, colour rule, visual QA every 100 (then 10) years |
| E. Site | 3: data packer, page builder, reviewer | The CartaHistoria mode on a preview URL | Build, smoke test, Jeffrey's review |
| F. Go-live | this thread | Merge to main | Jeffrey's go-ahead |

Research roster, 76 agents, weighted by how many polities Cliopatria holds in each region (Europe with Anatolia and the Caucasus has 735 of the 1,637):

| Region | Agents | Split |
| --- | --- | --- |
| Europe, Anatolia, Caucasus | 22 | Bronze Age and Greece; Hellenistic world; Roman Republic; Roman Empire; Byzantium; migration kingdoms; Franks and Carolingians; Holy Roman Empire to 1250; German states 1250 to 1806; France; England, Scotland, Wales, Ireland; Iberia and the taifas; Italy; Scandinavia and the Baltic; Poland, Lithuania, Bohemia, Hungary; Rus and Russia to 1721; Russian Empire and USSR; Balkans and Ottoman Europe; Caucasus; Europe 1789 to 1914; Europe 1914 to 1945; Europe 1945 to 2026 |
| Middle East and Egypt | 10 | Sumer to Akkad; Babylon and Assyria; Egypt to the New Kingdom; Hittites, Levant, Israel; Achaemenids and Seleucids; Parthia and the Sasanians; Rashidun to Umayyad; Abbasids and the autonomous dynasties; Turks, Crusaders, Mamluks; Ottomans and the modern Middle East |
| East Asia | 8 | Shang to Warring States; Qin and Han; Three Kingdoms to Sui; Tang and the Five Dynasties; Song, Liao, Jin, Xia; Yuan; Ming; Qing to the People's Republic |
| Inner Asia and the steppe | 3 | Xiongnu to the Türks; Mongols and successor khanates; Central Asian khanates to the republics |
| Japan and Korea | 2 | Japan; Korea |
| South Asia | 6 | Indus to the Mahajanapadas; Maurya to Gupta; medieval kingdoms; Delhi Sultanate; Mughals and Marathas; British Raj to the republics |
| South-east Asia | 4 | Mainland (Khmer, Pagan, Siam, Vietnam); Maritime (Srivijaya, Majapahit, Malacca); colonial; modern |
| Africa | 8 | Nubia, Kush, Axum, Ethiopia; Carthage and the Maghreb; Sahel empires; Forest states; Swahili and the Great Lakes; Central Africa; Southern Africa; partition and independence |
| Americas | 8 | Olmec to Teotihuacan; Maya; Toltec and Aztec; Andes to the Inca; North America before contact; Spanish and Portuguese America; United States and Canada; the republics from 1810 |
| Oceania | 2 | Polynesian and Melanesian states; Australia, New Zealand and the colonial Pacific |
| Cross-cutting | 3 | Cultures 6000 to 3400 BCE; the gazetteer; wars and fronts index |

Every agent gets the same brief: the standard, the dossier schema, its polity list from Cliopatria, the sources rule (open the page, cite it) and the file rules for the shared folder. A thread that starts cold reads history/README.md first.

Quality gates, in order: a dossier is accepted only after its reviewer passes it; a window is accepted only when both its seams are clean; the site ships only after the visual QA list has been read and every difference is explained.

## Decisions and defaults

One decision changes the shape of the whole project and is Jeffrey's: whether to build on Cliopatria. Everything else below is a default already taken; say the word to change any of it.

- [ ] **Build on Cliopatria (recommended) or draw every border from scratch.** Building on it means the 76 research agents verify, correct and densify 1,544 existing shapes to yearly resolution and add what it lacks, and the site credits Seshat under CC BY 4.0. Drawing from scratch means the same agents describe every border of every state from sources alone, which is slower, less consistent and still ends up checked against Cliopatria.

* **Start at 6000 BCE as asked**, showing archaeological cultures (Ubaid, Halaf, Yangshao, Hemudu, Mehrgarh, Vinča, Cucuteni, Naqada) in a muted dotted style labelled as cultures until the first states appear in 3400 BCE.
* **Time step** is one year everywhere; months are stored where known.
* **Grid** is H3 resolution 5 (10 km across) worldwide, resolution 6 where borders are fine and documented.
* **Mode name** CartaHistoria at /history/ (his name, 1 Nov 2026); the basemap shows no modern borders or labels.
* **Colours** follow convention for the major states and the neighbour rule for the rest; contested land is the blend of the two claimants.
* **historical-basemaps** is used only to cross-check (GPL-3); Wikipedia is the agents' source of record, read page by page.
* **Rulers** are collected only for states with a documented list; capitals for all.
* **Production** changes only with Jeffrey's go-ahead, after a preview.
