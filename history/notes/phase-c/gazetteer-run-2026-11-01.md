# Gazetteer run, 1 Nov 2026 (Phase C unresolved names)

Trigger: the Phase C compile of the 2,961 reviewed dossiers (`tools/compile_dossiers.py`) left 1,924 region specs it could not resolve, 565 distinct names (`notes/phase-c/unresolved_names.csv`, `unresolved_events.csv`). Brief: `briefs/gazetteer-brief.md`.

## Result

* Names: 565 before, **84** still failing (481 resolved or fixed): 67 are unknown to the gazetteer, 17 more exist in `places.jsonl` but resolve to an empty set (resolver problem 1 below). Events (region specs) with a failing name: 1,924 before, **287** after by my count from the failing leaf of each event (72 of them only because of an empty place). The Phase C compile was re-run by another agent after the tables landed: `notes/phase-c/unresolved_names.csv` now lists 67 names and 221 events, every one of them in the table below; it does not list names that resolve to an empty set, and it overwrote the original list.
* Added: **361 places** (`EXTRA_PLACES`, second block, `places.jsonl` regenerated with `build_gazetteer.py places`: 8,075 rows), **127 regions** (appended to `regions.jsonl`: 852 rows, 117 containing a polygon, 106 pure polygons), **5 aliases** on one existing admin-1 row (Lachin), 0 changes to the resolver.
* `python3 -I tools/gazetteer.py check --counts`: **852 of 852 resolve, empty 0, failed 0**. The 725 older regions give exactly the cells they gave before; 12,746 distinct spec fragments of the 284 flagged dossiers were resolved with the old and the new tables: 10,398 identical, 0 changed, 0 broken, 2,086 newly resolving, 262 still failing (the unresolved names below). Name collisions of the 1,444 new names/aliases against all 2,963 dossiers: no spec that resolved before resolves to anything else now.
* Border bands: all 272 `border_band` uses (80 distinct specs, 73 dossiers) resolve to non-empty cell sets.
* `data/gazetteer/resolved.jsonl`: the QA table, one line per distinct region spec in all 2,963 dossiers (n_cells, bbox, trace, used_in; errors carry an `error` field).

## What to look at first

* **The extents are not source-checked.** The WebFetch budget (400 an hour, shared by every agent, refilled one call every 9 s) ran out after about 330 calls during the run, and most Wikipedia articles returned through WebFetch carry no coordinates. The 361 place coordinates were all read from a page that showed them (the page is the comment on each `EXTRA_PLACES` tuple). The regions were composed from modern units wherever Natural Earth has one; **106 are pure polygons traced on the modern map**, and their notes say 'page not opened'. 39 regions have confidence 1 (a guess at the extent): see the table below. A reviewer should look at the confidence-1 rows and at the polygons of the Peloponnese, Ethiopia and South Africa before the borders are used.
* Size checks: each new region was resolved and its cell count and bounding box compared with the known area; nothing outside the expected country was found. Largest: Ngari (602 cells, 152,000 km2, confidence 1: the Ngari prefecture is about 300,000 km2, so this polygon takes the west half), Haud (575), Tiris al-Gharbiyya (401), British Bechuanaland (371), Raetia (329), Magna Graecia (295), Wollega (250), Bale (229), Dar al-Kuti (202).

## Resolver and data problems found (for the orchestrator)

1. **`Gazetteer.disk` returns nothing for a small radius at the coast.** It keeps land cells whose centre is within km and falls back to the containing cell only if that cell is land. It ignores the row's `cell`, which `build_gazetteer.py` moves to the nearest land cell (`cell_moved`). 17 names (88 events: Menton 18, Roquebrune-Cap-Martin 16, Akwidaa 14, Antibes 7, Aegina 7, Sorrento 4, Gramvousa 4, Taba 3, Kish 3, Qit'at Jaradah 3, Cobh 2, Erice 2, Skiathos 2, Preveza 1, Sanafir 1, Tiran 1) have correct place rows and still resolve empty. A fallback to the nearest land cell in `disk()` (if `out` is empty, take the nearest land cell among `grid_disk(c0, 3)`) fixes all 17 (tested in scratch: Menton gives the cell at 43.87 N 7.50 E). That is a resolver change; the schema, resolver and briefs change together, so it was not done here.
2. **Natural Earth mislabel:** the admin-1 row 'Lankaran' with 6 cells at 39.5-39.9 N, 46.1-46.5 E (ISO AZ-LAN, region 'Kalbajar-Lachin') is the Lachin district. It now carries the aliases Laçın, Lacin, Lachin, Lachin District, Lachin Rayon (edited by hand in `admin1.jsonl`; `build_gazetteer.py admin1` would drop it). `{"admin1": "Lankaran"}` still unions it with the real Lankaran (8 cells instead of 2); the republic-of-armenia dossier's GAZETTEER note ('Natural Earth lacks the Lachin district') is out of date.
3. **Western Sahara:** the country row 'Western Sahara' has 331 cells; Natural Earth gives Morocco the part west of the berm (Dakhla included). 'Tiris al-Gharbiyya' is cut from both rows (401 cells).
4. **No grammar form was missing.** A few dossiers (Australian Antarctic Territory, Ross Dependency, Swan Islands, Hawar Islands) need a way to say 'this event is not spatial' (Antarctic claims, Swan Islands, Hawar Islands); the compiler could skip a region whose spec resolves to nothing instead of treating it as an error.

## Names whose meaning differed between dossiers or from an existing entry

* **Lüneburg:** the town (8 place events, now `Lüneburg` in `places.jsonl`) and the territory (2 region events, read as the Principality of Lüneburg, with alias 'Principality of Luneburg' etc.; the Hanoverian departement of 1810-13 is the same area).
* **Kish:** the Persian Gulf island (salghurids, `Kish Island`, alias Kish, with `"country": "Iran"`) against Sumerian Kish (Iraq), which keeps the bare name.
* **Banda:** the town in Uttar Pradesh (janapada-of-cedi, `Banda, Uttar Pradesh`, alias Banda, `"country": "India"`) against the Banda Islands (Banda Neira), which keeps the bare name.
* **Moree** (Dutch Gold Coast fort, `"country": "Ghana"`) against Moree, Australia; **Hyères** (Greek colonies, Massalia) now carries the alias Olbia for the Greek colony, while the bare name Olbia keeps meaning Olbia in Italy (then Ukraine); **Philadelphia** for Alasehir (Turkey) against the U.S. city; **Sunchon/Suncheon**, **Fort William/Anomabu**, **Old Oyo/Oyo-Ile**: aliases were added only where a country qualifier separates the meanings, so a bare name keeps the entry it had.
* **Karelia / Ladoga Karelia, Bechuanaland / British Bechuanaland:** new regions were added beside the old ones; the old names keep their meaning.
* Forms with and without a country qualifier for the same place (Abbeville, Menton, Gaeta, Venlo, Lüneburg, Ranthambore) are the same place; qualifying every `place` with a country is what the brief asks, and an unqualified one now only works while the name is unique.
* **Kaulsdorf, Lauenburg:** several places of the name (Kaulsdorf, for example a Berlin district and a village in Thuringia; Lauenburg/Elbe and Lauenburg in Pomerania = Lebork). The ascania dossier means Lauenburg/Elbe.

## Still unresolved (84 names)

Classes: **coordinates** = No coordinates added. The Wikipedia page was not found, or WebFetch returned the article without any coordinates (the page converter drops the infobox coordinates of many articles), or the shared WebFetch budget (400 an hour) ran out before it could be tried. Nothing was typed from memory. Author should: Leave the place as written: the next gazetteer run adds it once a page with coordinates is opened. Where a region already stands in for it (Lauenburg -> region 'Duchy of Saxe-Lauenburg'), the author may use that.

**resolver** = The place is in places.jsonl with correct coordinates, but the radius in the dossier (3-20 km) is smaller than the grid spacing and the point's own cell has its centre at sea, so Gazetteer.disk returns no cell. It ignores the row's moved `cell`. Author should: Nothing in the dossier; the resolver needs a nearest-land-cell fallback in disk() (tested in scratch: every one of these then resolves to the one nearest cell).

**sub-grid** = Island/shoal smaller than a cell, no land cell of its own (Bahrain/Qatar dispute zone); a place row cannot resolve. Author should: drop it from the ledger or treat it as non-spatial.

**region** and **ambiguous** rows carry their own reason in the last column.

| name | kind | events | dossiers | class | why / author should |
|---|---|---|---|---|---|
| Lauenburg | place | 19 | 1 | coordinates |  |
| Menton (France) | place | 17 | 1 | resolver |  |
| Roquebrune-Cap-Martin (France) | place | 16 | 1 | resolver |  |
| Akwidaa (Ghana) | place | 14 | 2 | resolver |  |
| Muara Kaman (Indonesia) | place | 12 | 3 | coordinates |  |
| Lambsar | place | 11 | 1 | coordinates |  |
| Hawar Islands | region | 9 | 2 | region | 51 km2 archipelago 1.5 km off Qatar; smaller than one grid cell, and the nearest land cell is on Qatar's mainland, so any cell-level spec would hand Qatari land to Bahrain (or to the contested zone). Author should: drop the region from the Bahrain/Qatar ledger and keyframes, or let the compiler treat it as non-spatial; a place row 'Hawar Islands' exists with the real coordinates. |
| Keta (Ghana) | place | 9 | 3 | coordinates |  |
| Khawabi (Syria) | place | 9 | 1 | coordinates |  |
| Dewangiri (Bhutan) | place | 8 | 3 | coordinates |  |
| Aegina | place | 7 | 2 | resolver |  |
| Akwamufie (Ghana) | place | 7 | 2 | coordinates |  |
| Antibes | place | 7 | 2 | resolver |  |
| Sarra Triangle | region | 7 | 2 | region | The Wikipedia article (opened) gives only 'Kufra District, about 30,000 km2, ceded by Britain to Italy in 1934' and no coordinates or border line; Libya's whole Kufra district is far larger. Author should: give a polygon or a lat/lon box from the 1934 Rome agreement map; the gazetteer will add it. |
| Alzira (Spain) | place | 6 | 1 | coordinates |  |
| Fasht ad Dibal | place | 6 | 2 | sub-grid |  |
| Kherla (India) | place | 6 | 1 | coordinates |  |
| Kutai Lama (Indonesia) | place | 6 | 2 | coordinates |  |
| Rusafa (Syria) | place | 6 | 1 | coordinates |  |
| Tututepec | place | 6 | 1 | coordinates |  |
| Ullaiqah (Syria) | place | 6 | 1 | coordinates |  |
| Souda | place | 5 | 1 | coordinates |  |
| Usvyaty | place | 5 | 1 | coordinates |  |
| Apam (Ghana) | place | 4 | 1 | coordinates |  |
| Baitag Bogd | place | 4 | 2 | coordinates |  |
| Cormantin (Ghana) | place | 4 | 1 | coordinates |  |
| Decelea | place | 4 | 2 | coordinates |  |
| Dolon Nur | place | 4 | 2 | coordinates |  |
| Fatagar | region | 4 | 2 | region | Article opened: south of Lasta, separating Ifat from Shewa, 'now part of modern Shewa southeast of Addis Ababa' [citation needed]; no coordinates, no river names. Author should: give a centre and radius (Ziway or Debre Zeyit side) with a source, or a polygon. |
| Gramvousa | place | 4 | 1 | resolver |  |
| Janan Island | place | 4 | 2 | sub-grid |  |
| Nevel | place | 4 | 1 | coordinates |  |
| Sawankhalok (Thailand) | place | 4 | 1 | coordinates |  |
| Seocheon | place | 4 | 1 | coordinates |  |
| Sorrento (Italy) | place | 4 | 1 | resolver |  |
| Swan Islands | region | 4 | 1 | region | Three islets (about 7 km2) off Honduras, 17.4 N 83.9 W; no land cell, Honduras has none there. Author should: treat as non-spatial or drop; no cell can carry it. |
| Weldiya | place | 4 | 2 | coordinates |  |
| Bonampak (Mexico) | place | 3 | 1 | coordinates |  |
| Cempoala | place | 3 | 1 | coordinates |  |
| Julfar | place | 3 | 1 | coordinates |  |
| Kish (Iran) | place | 3 | 1 | resolver |  |
| Monfragüe (Spain) | place | 3 | 1 | coordinates |  |
| Neukamerun | region | 3 | 1 | region | German article (opened) gives 295,000 km2 ceded in 1911 'now part of Gabon, Congo, CAR' and the Logone-Chari duck's beak as separate; it gives no coordinates or border points, and no modern admin-1 unit matches. Author should: give a union of admin-1 units after checking a map (Congo: Sangha, Likouala; CAR: Sangha-Mbaere, Lobaye; Gabon: Woleu-Ntem are candidates, not verified), or a polygon. |
| Qit'at Jaradah | place | 3 | 1 | resolver |  |
| Taba (Egypt) | place | 3 | 1 | resolver |  |
| Argos | place | 2 | 1 | coordinates |  |
| Bagys (Kazakhstan) | place | 2 | 2 | coordinates |  |
| Barentu | place | 2 | 1 | coordinates |  |
| Bophuthatswana | region | 2 | 1 | region | Seven separate enclaves of the old homeland in North West and neighbouring provinces; Natural Earth has only 'North West' (106,000 km2), about 2.5 times the homeland. Author should: give discs round the seven parts (Mmabatho/Mafikeng, Brits, Odi, Moretele and others) or accept North West at confidence 1. |
| Cobh | place | 2 | 1 | resolver |  |
| Colhuacan | place | 2 | 1 | coordinates |  |
| Coronea | place | 2 | 1 | coordinates |  |
| Egya (Ghana) | place | 2 | 1 | coordinates |  |
| Erice | place | 2 | 1 | resolver |  |
| Haj Omran (Iraq) | place | 2 | 1 | coordinates |  |
| Halin (Myanmar) | place | 2 | 1 | coordinates |  |
| Ilaro (Nigeria) | place | 2 | 1 | coordinates |  |
| Karangan (Indonesia) | place | 2 | 1 | coordinates |  |
| Los Arcos | place | 2 | 1 | coordinates |  |
| Mancanegara | region | 2 | 2 | region | Javanese 'outer districts' of Yogyakarta and Surakarta taken by the Dutch in 1830 (Madiun, Kediri, Banyumas, Bagelen, Pacitan...); a list of districts, not one unit; no page opened. Author should: name the districts and use admin-1/regency discs, or a polygon with a source. |
| Moorea | place | 2 | 1 | coordinates |  |
| Oyón | place | 2 | 1 | coordinates |  |
| Phlius | place | 2 | 1 | coordinates |  |
| Sikyon | place | 2 | 1 | coordinates |  |
| Skiathos | place | 2 | 1 | resolver |  |
| Akisene | region | 1 | 1 | region | Not an attested spelling; the dossier names Acilisene (exists) and 'Akisene', 'possibly Anzitene'. Probably a variant or a typo of Acilisene/Anzitene. Author should: check the source: use Acilisene or give the coordinates of the place meant. |
| Arsuf | place | 1 | 1 | coordinates |  |
| Artajona | place | 1 | 1 | coordinates |  |
| Australian Antarctic Territory | region | 1 | 1 | region | Antarctica has no land cells in the grid (524,441 land cells exclude the ice sheet). Author should: treat as non-spatial; or Antarctica needs its own grid. |
| Coixtlahuaca | place | 1 | 1 | coordinates |  |
| Cuitlahuac | place | 1 | 1 | coordinates |  |
| Kaulsdorf (Germany) | place | 1 | 1 | ambiguous | More than one Kaulsdorf in Germany (a Berlin district, a village in Thuringia...); the dossier gives only 'Germany' and 6 km, and no page with coordinates was read. Author should: add the admin-1 (state) or the Prussian district to the spec text; the gazetteer needs the coordinates of the one meant. |
| Lingen (Germany) | place | 1 | 1 | coordinates |  |
| Massango | region | 1 | 1 | region | The dossier text says 'Massonge and Gimirra'; Massonge/Massango is not in the gazetteer and no page was opened for it. Gimirra exists. Author should: check the spelling and give a centre/radius with a source. |
| Menton | place | 1 | 1 | resolver |  |
| Mirebeau | place | 1 | 1 | coordinates |  |
| Ningo (Ghana) | place | 1 | 1 | coordinates |  |
| Preveza | place | 1 | 1 | resolver |  |
| Ross Dependency | region | 1 | 1 | region | Same: Antarctica has no land cells. Author should: treat as non-spatial. |
| Sanafir Island | place | 1 | 1 | resolver |  |
| Saqqaq | place | 1 | 1 | coordinates |  |
| Tiran Island | place | 1 | 1 | resolver |  |
| Uzengi-Kuush (Kyrgyzstan) | place | 1 | 1 | coordinates |  |
| Wej | region | 1 | 1 | region | Medieval Ethiopian province (1572 loss); no page opened, no unit matches. Author should: give a centre/radius or polygon with a source. |

## What `resolved.jsonl` shows beyond the 565 names

25,328 distinct region specs in 2,963 dossiers (63,071 uses); 281 specs (487 uses) carry an `error`: 146 fail with an unknown name and 135 resolve to no cells.
* The unknown names are all in the table above except four that were not in the original list (dossiers added or changed since the compile): `Baghelkhand` (region; chandela-kingdom/wars/1/zones/1), `Sadiya` (place; kamarupa-kingdom/identity/successors/2/land), `Kirtipur` (place; kathmandu/wars/0/zones/1) and `Iâl` (region; kingdom-of-powys/wars/4/zones/0). Not added: no page was opened for them.
* Empty specs: 97 are `minus: [X, X]` of the same Cliopatria shape or region (a polity minus itself, written in the dossier; empty by construction), 14 are the sub-radius places of resolver problem 1, and 24 are islands or discs smaller than a cell or at sea (Norfolk Island, Kermadec Islands, Wake, Midway, Penghu, Saba, St. Eustatius, Paracel Islands, Seychelles Outer Islands, Peleliu and Angaur, a Kiribati polygon pair that misses the country's cell centres, the Torres Strait polygon, six small `lon/lat/km` discs, and Western Satraps in 476 and 480). They are for the authors and the compiler to review: filter `resolved.jsonl` on `error`.

## Regions added (127)

Cells are the 253 km2 H3 cells of the land grid. `units` = composed from Natural Earth units, places, countries; `polygon` = a polygon of at most 12 points; page opened = the note names the article. Notes with the extent reasoning are in `regions.jsonl`.

| region | conf | cells | basis | source |
|---|---|---|---|---|
| Laconia | 2 | 15 | polygon | page not opened |
| Messenia | 2 | 10 | polygon | page not opened |
| Argolid | 2 | 7 | polygon | page not opened |
| Arcadia | 2 | 18 | polygon | page not opened |
| Elis | 2 | 10 | polygon | page not opened |
| Achaea | 2 | 9 | polygon | page not opened |
| Acarnania | 2 | 4 | polygon | page not opened |
| Aetolia | 2 | 14 | polygon | page not opened |
| Phocis | 2 | 7 | polygon | page not opened |
| Locris | 1 | 3 | polygon | page not opened |
| Chalcidice | 2 | 17 | units+polygon | page not opened |
| Thyreatis | 1 | 1 | polygon | page not opened |
| Rhodope Mountains | 2 | 29 | polygon | page not opened |
| Magna Graecia | 2 | 295 | units | page not opened |
| Aeolis | 1 | 23 | polygon | page not opened |
| Acilisene | 1 | 48 | polygon | page not opened |
| Characene | 1 | 87 | units+polygon | page not opened |
| Shephelah | 2 | 9 | polygon | page not opened |
| Awsan | 1 | 46 | polygon | page not opened |
| Maakhir | 1 | 129 | polygon | page not opened |
| Hadiya | 1 | 23 | polygon | page not opened |
| Kaffa | 2 | 76 | polygon | page not opened |
| Gimirra | 1 | 73 | polygon | page not opened |
| Wollega | 2 | 250 | polygon | page not opened |
| Illubabor | 2 | 152 | polygon | page not opened |
| Gurage | 1 | 37 | polygon | page not opened |
| Kambata | 1 | 12 | polygon | page not opened |
| Welayta | 1 | 28 | polygon | page not opened |
| Gofa | 1 | 47 | polygon | page not opened |
| Sidamo | 2 | 90 | polygon | page not opened |
| Borana | 1 | 199 | polygon | page not opened |
| Arsi | 2 | 114 | polygon | page not opened |
| Bale | 2 | 229 | polygon | page not opened |
| Dawaro | 1 | 191 | polygon | page not opened |
| Semien | 2 | 42 | polygon | page not opened |
| Damot | 1 | 108 | polygon | page not opened |
| Western Tigray | 2 | 63 | polygon | page not opened |
| Haud | 2 | 575 | polygon | page not opened |
| Transkei | 2 | 132 | polygon | page not opened |
| Ciskei | 1 | 39 | polygon | page not opened |
| Venda | 2 | 30 | polygon | page not opened |
| British Kaffraria | 2 | 50 | polygon | page not opened |
| Pondoland | 2 | 23 | polygon | page not opened |
| Xesibeland | 1 | 17 | polygon | page not opened |
| Griqualand East | 2 | 33 | polygon | page not opened |
| Griqualand West | 2 | 196 | polygon | page not opened |
| Conquered Territory | 2 | 27 | units+polygon | page not opened |
| British Bechuanaland | 1 | 371 | units+polygon | page not opened |
| Sekhukhuneland | 2 | 37 | polygon | page not opened |
| Kionga Triangle | 1 | 3 | polygon | page not opened |
| Kagera Salient | 1 | 13 | polygon | page not opened |
| Lado Enclave | 2 | 119 | polygon | page not opened |
| Aouzou Strip | 2 | 120 | units+polygon | page not opened |
| Tiris al-Gharbiyya | 2 | 401 | units+polygon | page not opened |
| Parrot's Beak | 1 | 31 | polygon | page not opened |
| Dar al-Kuti | 1 | 202 | polygon | page not opened |
| Jebel Nafusa | 2 | 52 | polygon | page not opened |
| Southern Cameroons | 3 | 191 | units | page not opened |
| Northern Cameroons | 1 | 171 | polygon | page not opened |
| British Cameroons | 1 | 362 | units | page not opened |
| Lower Lusatia | 2 | 39 | polygon | page not opened |
| Upper Lusatia | 2 | 25 | polygon | page not opened |
| Neumark | 2 | 63 | polygon | page not opened |
| Altmark | 2 | 28 | polygon | page not opened |
| Upper Palatinate | 2 | 51 | polygon | page not opened |
| Egerland | 2 | 8 | polygon | page not opened |
| Bremen-Verden | 2 | 30 | polygon | page not opened |
| Land Hadeln | 1 | 2 | polygon | page not opened |
| Principality of Lüneburg | 2 | 51 | polygon | page not opened |
| Lüneburg | 2 | 51 | units | page not opened |
| Duchy of Saxe-Lauenburg | 2 | 8 | polygon | page not opened |
| County of Hoya | 2 | 12 | polygon | page not opened |
| County of Diepholz | 2 | 6 | polygon | page not opened |
| Principality of Calenberg | 2 | 22 | polygon | page not opened |
| Principality of Grubenhagen | 2 | 12 | polygon | page not opened |
| Bentheim | 2 | 10 | polygon | page not opened |
| East Frisia | 2 | 19 | polygon | page not opened |
| Münsterland | 2 | 29 | polygon | page not opened |
| Innviertel | 2 | 20 | polygon | page not opened |
| Mühlviertel | 2 | 20 | polygon | page not opened |
| East Tyrol | 2 | 13 | polygon | page not opened |
| Savinja | 2 | 8 | units | page not opened |
| Kvarner | 2 | 16 | units | page not opened |
| Cieszyn Silesia | 2 | 14 | polygon | page not opened |
| Sudetenland | 1 | 117 | units+polygon | page not opened |
| Southern Slovakia | 2 | 48 | units+polygon | page not opened |
| Orava | 2 | 13 | polygon | page not opened |
| Spiš | 2 | 14 | polygon | page not opened |
| Transdanubia | 3 | 138 | units | page not opened |
| Pokuttya | 1 | 29 | polygon | page not opened |
| Yedisan | 2 | 105 | polygon | page not opened |
| Faucigny | 2 | 13 | polygon | page not opened |
| Berguedà | 2 | 6 | polygon | page not opened |
| Lauragais | 2 | 13 | polygon | page not opened |
| Nébouzan | 2 | 10 | polygon | page not opened |
| Comminges | 2 | 24 | polygon | page not opened |
| Charolais | 2 | 13 | polygon | page not opened |
| La Bureba | 2 | 13 | polygon | page not opened |
| Lunigiana | 2 | 9 | units | page not opened |
| Ellhorn | 1 | 1 | units | page not opened |
| Karelian Isthmus | 2 | 70 | polygon | page not opened |
| Ladoga Karelia | 2 | 74 | polygon | page not opened |
| Petsamo | 2 | 42 | polygon | page not opened |
| Rybachy Peninsula | 1 | 5 | polygon | page not opened |
| Salla | 1 | 33 | polygon | page not opened |
| Setomaa | 2 | 10 | polygon | page not opened |
| Franz Josef Land | 2 | 65 | polygon | page not opened |
| Tsushima | 2 | 1 | polygon | page not opened |
| Iki | 2 | 1 | polygon | page not opened |
| Yaeyama Islands | 2 | 3 | polygon | page not opened |
| Miyako Islands | 2 | 1 | polygon | page not opened |
| Amami Islands | 2 | 5 | polygon | page not opened |
| Naning | 1 | 4 | polygon | page not opened |
| Dabie Mountains | 2 | 99 | polygon | page not opened |
| Ngari | 1 | 602 | polygon | page not opened |
| Cooch Behar | 2 | 15 | polygon | page not opened |
| Bengal Duars | 2 | 32 | polygon | page not opened |
| Assam Duars | 1 | 47 | polygon | page not opened |
| Halaib Triangle | 1 | 53 | polygon | page not opened |
| Puna de Atacama | 1 | 322 | polygon | page not opened |
| Soconusco | 2 | 31 | polygon | page not opened |
| Samurzakano | 2 | 8 | polygon | page not opened |
| Tao | 1 | 32 | polygon | page not opened |
| Raetia | 2 | 329 | units+polygon | page not opened |
| Zeelandic Flanders | 2 | 3 | units+polygon | page not opened |
| Gu-edena | 1 | 2 | units | page not opened |
| Bete Amhara | 1 | 160 | units+polygon | page opened |

## Places added (361), by country

Coordinates read from the Wikipedia article named in the comment beside each tuple in `tools/build_gazetteer.py`; 55 rows sit in a coastal cell whose centre is at sea and were moved to the nearest land cell (`cell_moved`).

* **Austria** (4): Kitzbühel, Kufstein, Lienz, Rattenberg
* **Bahrain** (2): Hawar Islands, Qit'at Jaradah
* **Belgium** (10): Bouillon, Dendermonde, Eupen, Lier, Malmedy, Mechelen, Menen, Ostend, Tournai, Ypres
* **Bulgaria** (1): Slivnitsa
* **China** (8): Bazhong, Loulan, Ruili, Shangcai, Suide, Xincai, Yan'an, Zhumadian
* **Croatia** (4): Knin, Pazin, Rovinj, Vrgorac
* **Egypt** (2): Aydhab, Taba
* **Eritrea** (2): Badme, Tsorona
* **Ethiopia** (4): Chifra, Kombolcha, Shire, Zalambessa
* **Finland** (1): Hanko
* **France** (31): Abbeville, Agde, Antibes, Blois, Boulogne-sur-Mer, Bram, Chabanais, Chartres, Château-Thierry, Châteaudun, Confolens, Douai, Gex, Hyères, Lectoure, Loudun, Menton, Montargis, Montbéliard, Orchies, Provins, Péronne, Rethel, Riom, Roquebrune-Cap-Martin, Ruffec, Saint-Jean-Pied-de-Port, Saverdun, Valenciennes, Vendôme, Vic-le-Comte
* **Georgia** (1): Kobuleti
* **Germany** (32): Anklam, Aschersleben, Bad Homburg vor der Höhe, Bad Orb, Bautzen, Bernburg, Boppard, Brandenburg an der Havel, Burg Stargard, Dessau, Elten, Freising, Gersfeld, Halberstadt, Hoym, Köthen, Landau, Lüneburg, Minden, Montabaur, Neuburg an der Donau, Orlamünde, Prüm, Ratzeburg, Saarlouis, Sankt Wendel, Selfkant, Stade, Suderwick, Wernigerode, Wismar, Zerbst
* **Ghana** (16): Ada, Akwidaa, Anomabu, Assin Fosu, Axim, Beyin, Butre, Dixcove, Elmina, Komenda, Moree, Princes Town, Senya Beraku, Shama, Takoradi, Teshie
* **Greece** (38): Aegina, Arta, Cephalonia, Chaeronea, Epidaurus, Gramvousa, Gytheio, Koroni, Kythira, Lefkada, Lemnos, Mantineia, Megalopolis, Megara, Melos, Methoni, Monemvasia, Mykonos, Nafpaktos, Nafplio, Naxos, Orchomenus, Oropos, Preveza, Pylos, Rethymno, Salamis, Samos, Samothrace, Skiathos, Skopelos, Skyros, Spinalonga, Tegea, Thasos, Tinos, Troezen, Zakynthos
* **Greenland** (4): Aasiaat, Maniitsoq, Nanortalik, Qeqertarsuatsiaat
* **India** (36): Anahilapataka, Banda, Uttar Pradesh, Barmer, Basavakalyan, Bathinda, Bhadrajun, Champaner, Dhar, Dwarka, Gagron, Idar, Jalore, Janjira, Junagadh, Junnar, Kalimpong, Kalinjar, Karwar, Khajuraho, Maheshwar, Mahuli, Mandalgarh, Merta, Mount Abu, Nadol, Nagaon, Nagaur, Phalodi, Pokhran, Raisen, Rajouri, Ranthambore, Rewa, Sirohi, Thane, Vasai
* **Indonesia** (1): Amlapura
* **Iran** (7): Alamut, Gerdkuh, Kish Island, Mehran, Minab, Rudkhan, Tabas
* **Iraq** (7): Adab, Hawija, Isin, Larsa, Majnoon Island, Sinjar, Umma
* **Ireland** (3): Buncrana, Castletownbere, Cobh
* **Israel** (2): Ascalon, Safed
* **Italy** (31): Agrigento, Alghero, Aversa, Bagnone, Bassano del Grappa, Carrara, Cefalù, Civitella del Tronto, Crema, Erice, Este, Feltre, Fivizzano, Gaeta, Gela, Gorizia, Guastalla, Lamezia Terme, Lentini, Manfredonia, Massa, Mazara del Vallo, Mestre, Orbetello, Piombino, Policoro, Pontremoli, Sibari, Sorrento, Sutri, Taormina
* **Japan** (1): Yoshino
* **Kazakhstan** (1): Zhalanashkol
* **Kyrgyzstan** (1): Khan Tengri
* **Lebanon** (1): Beaufort Castle
* **Libya** (1): Tarhuna
* **Mauritania** (1): Arguin
* **Mexico** (5): Metztitlán, Mixquic, Motozintla, Tilantongo, Xochimilco
* **Montenegro** (1): Perast
* **Morocco** (3): Asilah, Ksar es-Seghir, Sidi Ifni
* **Mozambique** (1): Sena
* **Myanmar** (2): Beikthano, Kengtung
* **Nepal** (1): Nuwakot
* **Netherlands** (18): Amersfoort, Breda, Coevorden, Delfzijl, Deventer, Echt, Enschede, Groenlo, Hulst, Naarden, Nijmegen, Oldenzaal, Ootmarsum, Roermond, Sas van Gent, Steenwijk, Venlo, Zutphen
* **Nigeria** (2): Igboho, Jebba
* **Oman** (1): Qalhat
* **Pakistan** (1): Mehrgarh
* **Papua New Guinea** (1): Buka
* **Poland** (18): Cieszyn, Czeladź, Głogów, Kalisz, Koźle, Kłodzko, Legnica, Oświęcim, Racibórz, Radom, Siewierz, Strzegom, Toszek, Wieluń, Wiślica, Środa Śląska, Świdnica, Świebodzin
* **Portugal** (1): Mértola
* **Russia** (7): Gdov, Kexholm, Pereslavl-Zalessky, Serpeysk, Sevsk, Trubchevsk, Velizh
* **Saudi Arabia** (2): Sanafir Island, Tiran Island
* **Slovakia** (1): Sobrance
* **South Korea** (3): Jinju, Naju, Suncheon
* **Spain** (16): Albarracín, Alcañiz, Almenar, Alpuente, Barbastro, Ciudad Real, Dénia, Graus, Hondarribia, Laguardia, Lleida, Monzón, Olivenza, Sariñena, Tauste, Xàtiva
* **Sri Lanka** (2): Hanwella, Wattala
* **Sudan** (2): Abu Hamed, Suakin
* **Switzerland** (1): Kyburg
* **Syria** (6): Afrin, Kafartab, Kahf, Masyaf, Qadmus, Shaizar
* **Thailand** (1): Dan Sai
* **Turkey** (9): Alaşehir, Corycus, Divriği, Elbistan, Hasankeyf, Imbros, Mayyafariqin, Tenedos, Şebinkarahisar
* **Uganda** (1): Wadelai
* **Yemen** (2): Kamaran, Socotra

## Checks run

* `python3 -I tools/gazetteer.py check --counts` (mount tables): 852 regions, resolve 852, empty 0, failed 0.
* Old against new tables over the 284 flagged dossiers: identical where resolved before (see Result); over all 2,963 dossiers for every leaf whose name or alias is new: 536 leaves, 524 newly resolving, 11 identical, 1 failing, 0 changed.
* `build_gazetteer.py places` run in scratch with the new block reproduces the old `places.jsonl` exactly plus the 361 rows (no other row changed).
* Two collisions were found and removed before writing: a bare 'Banda' would have moved from the Banda Islands to Uttar Pradesh (row renamed `Banda, Uttar Pradesh`), and 'Old Oyo' would have moved from Oyo-Ile to Igboho (alias dropped).

## Files changed

`data/gazetteer/places.jsonl` (regenerated by the builder), `regions.jsonl` (127 rows appended), `admin1.jsonl` (one row, aliases), `resolved.jsonl` (new), `README.md` (counts, a section 'Added on 1 Nov 2026', three known gaps), `tools/build_gazetteer.py` (second block of `EXTRA_PLACES`, 361 tuples). Nothing else on the mount was written.
