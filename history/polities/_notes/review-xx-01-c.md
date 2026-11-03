# Review of batch xx-01-c (cultures 6000-3400 BCE, part c)

Reviewer run of 2026-10-18. 18 dossiers, all type culture, no Cliopatria rows. Validator (--resolve): 0 errors; 2 warnings (successor slugs machalilla-culture and ancient-pueblo-peoples without dossiers, both listed by the author). Gazetteer check: no keyframe of this batch shares a cell with any other dossier keyframe (new-keyframe dossiers starting before 500 CE) in overlapping years.

Spot checks: every ledger event of every dossier was opened on its cited page (WebFetch, 2026-10-18), up to the 4-per-dossier budget (Tichitt: all 5). Every confidence-3 event (A-Group 3500 and 3100, Nabta 5500 and 4500, Cochise 3500 and 1500, Watson Brake 3500 and 2800, Valdivia Phase A 3000, Tichitt 2600/1900/1600/1000/400) is on the page with its year and land. No fabricated or mis-dated event found.

## Verdicts

### norte-chico-civilization: pass

- Tried: All 3 events opened: 3500 first city at Huaricanga, 'By around 2200 BCE' influence to Chillon/El Paraiso and Santa valley, decline c. 1800 BCE: all on the page. Keyframes match ledger (gain at 2200 explains K0->K1).
- Area: No infobox; page: 'The three principal valleys cover only 1,800 km2'; keyframe 0 (30 cells, about 7,600 km2) acknowledges the overstatement in its note.

### valdivia-culture: pass

- Tried: Infobox 'Dates: 3800 - 1500 BC', 'Followed by: Machalilla culture, Cotocollao culture', Phase A 'dated to 3000-2700 BC' all confirmed; the 3500 prose date is acknowledged.
- Thin at `/identity/predecessors`: Las Vegas culture (Santa Elena, before 3800 BCE) has no dossier; Santa Elena blank -6000..-3801 Page to try: https://en.wikipedia.org/wiki/Real_Alto
- Area: No infobox area; Santa Elena province (13 cells) as stated.

### chinchorro-culture: fix

- Tried: 'lasted from 9,100 to 3,500 years BP (7,000 to 1,500 BCE)', 'The end of the Chinchorro culture is set around 3500 BP', 'Followed by: Wankarani' confirmed.
- Fix (applied by reviewer) at `/keyframe_review/0/correction (and /ledger/0/region, /ledger/1/region)`: The four 70 km discs (Ilo, Arica, Iquique, Antofagasta) left a 240 km gap between Iquique and Antofagasta although the region text quotes the page's continuous strip 'from Ilo, southern Peru, to Antofagasta'. Evidence: Chinchorro_culture page: 'spread across the arid coastal regions of the Atacama Desert' 'from Ilo, southern Peru, to Antofagasta in northern Chile'; gazetteer: Iquique -20.25, Antofagasta -23.65 (380 km apart). Change: Added {"place": "Tocopilla", "km": 70} to the three unions and updated the keyframe note (158 land cells, was 128); revalidated with 0 errors.
- Area: No infobox area; five coastal discs.

### maritime-archaic: pass

- Tried: 'began in approximately 7000 BC and lasted until approximately 3500 BC' confirmed; Paleo-Eskimo claim flagged [citation needed] as the note says.
- Area: No infobox; whole provinces (2,165 cells) for a coastal culture, overstatement acknowledged in notes. The page names 'Newfoundland, the Canadian Maritimes and northern New England', 'as far south as Maine and as far north as Labrador'.

### watson-brake-culture: pass

- Tried: Both confidence-3 events confirmed: 'Mound construction began at approximately 3500 BCE' (infobox 'Built: 3500 BCE'), 'abandoned around 2800 BCE'; occupation 'around 4000 BCE'.
- Area: No area on the page; one 80 km disc round Monroe (page: 'near present-day Monroe in northern Louisiana').

### oshara-tradition: pass

- Tried: Infobox 'ca. 5,440 BCE to 460 CE', Bajada '6,750 to 5,150 years BP', En Medio '2,750 to 1,550 years BP', 'Followed by: Ancient Pueblo People' confirmed; BP conversions correct; San Jose overlap noted by the author.
- Area: No infobox area; New Mexico and Colorado whole (1,878 cells, about 475,000 km2) per infobox 'Geographical range: New Mexico, Colorado'; overstatement acknowledged.

### cochise-culture: pass

- Tried: Both confidence-3 phases confirmed ('between about 3500 and 1500 BC', 'San Pedro flourishing from about 1500 to 200 BC'); 'from circa 5000 until circa 200 BC' confirmed. No overlap with oshara-tradition (gazetteer check).
- Area: No area on the page; Arizona plus a 150 km disc in south-west New Mexico ('Arizona and western New Mexico').

### old-copper-complex: pass

- Tried: 'Artifacts from some of these sites have been dated from 6500 to 1580 BCE' and 'can be dated to around 6,500 BCE' confirmed; the conflicting 4000-2000 BC burial-ground date is acknowledged.
- Area: No infobox; Wisconsin plus 150 km disc at Hancock (868 cells). Page names Wisconsin, Lake Superior, Isle Royale, the Keweenaw Peninsula and the Brule River.

### aboriginal-australians: thin

- Tried: Arrival '50,000 to 65,000 years ago', Madjedbebe 'as early as 65,000 years BP' confirmed; Torres Strait 'about 4,000 years ago' confirmed (the page also gives 2,500 years ago for the ancestors' arrival).
- Thin at `/ledger/0`: Confidence-1 placement of the whole mainland; the page gives no dated extent 6000-3400 BCE (it says only that density was greatest in the south and east). Page to try: https://en.wikipedia.org/wiki/Prehistory_of_Australia
- Thin at `/ledger/1`: Dissolve at -3400 is the group horizon, not an end on the page: the culture continues to 1788, so mainland Australia is blank from 3399 BCE until the colonial dossiers. Extend the end (to 1788, successor the first colony) or have the colonial group take the land. Page to try: https://en.wikipedia.org/wiki/Indigenous_Australians
- Area: No infobox area; Australia less Tasmania (31,226 cells, about 7.9 M km2).

### aboriginal-tasmanians: thin

- Tried: 'Around 6000 BCE, rising sea levels flooded the Bass Strait and separated Tasmania from mainland Australia' confirmed, and the page's own conflicting 14,000-12,000 BCE date for the Bassian Plain, which the notes flag.
- Thin at `/ledger/1`: Dissolve at -3400 is the group horizon; the page carries the people, isolated 'for about 8,000 years', to 'British colonisation in 1803'. Extend end to 1803 with the colony as successor so Tasmania is not blank 3399 BCE-1803. Page to try: https://en.wikipedia.org/wiki/Aboriginal_Tasmanians
- Area: No area on the page; Tasmania admin1 (233 cells).

### kuk-swamp-agriculture: thin

- Tried: 'beginning about 9,000 years ago' and bananas/sugar cane '6,900 - 6,400 years ago' confirmed; site 12-13 km NE of Mount Hagen at 1,550 m.
- Thin at `/ledger/2`: Dissolve at -3400 is the group horizon; the page gives no end for Kuk farming. A gap-filler should find an end date or extend the dossier with the Highlands farmers. Page to try: https://en.wikipedia.org/wiki/Agriculture_in_Papua_New_Guinea
- Area: Page gives the 116 ha site only; the 40 km disc (19 cells) is acknowledged in the keyframe note as overstating the site by orders of magnitude.

### capsian-culture: pass

- Tried: 'in Algeria and Tunisia from ca. 9000 to 5400 cal BC' and the Neolithic of Capsian Tradition sentence confirmed; Iberomaurusian page confirms 'In Algeria, Tunisia, and Libya, but not in Morocco' and the Cardial in 'Morocco and western Algeria'.
- Area: No area on the page; Tunisia plus north-east Algeria (1,204 cells).

### nabta-playa-neolithic: pass

- Tried: Both confidence-3 events confirmed ('From 5500 BC the Late Neolithic period began'; 'a megalith period ... between about 4500 BC to 3600 BC'); 'circa 7500 BC' and 'about 100 kilometers west of Abu Simbel' confirmed. The 3600 end is the last dated megalith, as the note says.
- Area: No area on the page; 100 km disc cut at the Egyptian border and less the Naqada Nile band (75 cells).

### tenerian-culture: fix

- Tried: 'Phase III dates from 5200 BCE to 2200 BCE', 'interruption ... from 6200-5200 BCE', Phase IV '2500 BCE to 300 BCE', infobox 'Abandoned c. 3000 BCE' and the other range '6250 BCE to 2550 BCE' all on the page; the author flags the conflict.
- Fix (applied by reviewer) at `/ledger/0/counterpart`: The found event had counterpart 'nobody' while green-sahara-cultures /ledger/1 records a loss of the same Gobero disc to tenerian-culture in -5200, so the transfer was unmatched. Evidence: green-sahara-cultures /ledger/1: -5200 loss, counterpart tenerian-culture, region {lon 9.517, lat 17.083, km 100}; tenerian-culture /ledger/0: -5200 found, same region, counterpart nobody. Change: Set /ledger/0/counterpart to "green-sahara-cultures"; revalidated with --resolve, 0 errors 0 warnings.
- Area: No area on the page; 100 km disc at the Gobero coordinates (117 cells).

### khartoum-mesolithic-and-neolithic: pass

- Tried: 'Early Khartoum (8800 to 5000 BP)', 'c. 5700-3550 BP, approximately 3750-1600 BC' and the page's slip '3700-3550 BC' confirmed; Nubia page 'from the ninth to the sixth millennia cal BC' confirmed; Khartoum_Mesolithic returns URL_NOT_FOUND for me too.
- Area: No area on the page; 100 km disc round Omdurman (Shaheinab 'approximately 50 km north of Omdurman on the west bank of the Nile').

### a-group-culture: pass

- Tried: Both confidence-3 events confirmed on the Nubia page ('Around 3500 BC ... Early A-Group culture, arose in Lower Nubia'; 'Around 3100 BC, the A-group transitioned from the Early to Classical phases'); end 'c. 2900 BC' and 'apparently destroyed by the First Dynasty rulers of Egypt' confirmed; 'between the First and Second Cataracts' confirmed. Verified the trim: naqada-culture's keyframes put 54 cells in Lower Nubia down to 22.14 N; the Early Dynastic Cliopatria shape in -3000 puts 10 there.
- Area: No infobox; Lower Nubia less the Egyptian Nile band and the Early Dynastic shape (134 of 188 cells), trim acknowledged and routed to the Egypt group.

### tichitt-tradition: pass

- Tried: All five confidence-3 events confirmed word for word: Pre-Tichitt 2600-1900, Early 1900-1600, Classic 1600-1000, Late 1000-400 BCE; the 'between 2000 BCE and 300 BCE' range is acknowledged.
- Area: No area on the page; two 100 km discs (Dhar Tichitt coordinates, Oualata) for the 'Tichitt-Oualata region' (264 cells).

### green-sahara-cultures: thin

- Tried: 'The AHP led to the widespread settlement of the Sahara', 'ended 6,000-5,000 years ago during the Piora Oscillation', '5,500 years ago in the Sahel, Arabia, and East Africa', Acacus domestication 'by around 7000 BP' and Gobero Phase III from 5200 BCE all confirmed. No cell overlap with khartoum (Sahara stops at 16.0 N) or any other dossier.
- Thin at `/ledger/0`: Confidence-1 found over the whole gazetteer Sahara less Egypt and the Capsian country (27,973 cells, about 7.1 M km2): the African humid period page says the AHP 'led to the widespread settlement of the Sahara' but dates and maps no extent. A gap-filler should replace it with dated sites or regions (Acacus, Tassili, Wadi Howar, Ennedi) or drop it. Page to try: https://en.wikipedia.org/wiki/Tassili_n'Ajjer
- Thin at `/keyframe_review/0`: No page gives the extent of Saharan herding outside Nabta Playa, Gobero and the Acacus; the soft border is the dossier's. Page to try: https://en.wikipedia.org/wiki/Wadi_Howar
- Area: No page area; the whole-desert placement is acknowledged as confidence 1 in the notes and the author's problems.

## Cross-dossier matrix

- green-sahara-cultures -5200 loss -> tenerian-culture: matched; mirror tenerian-culture -5200 found. Was a mismatch (tenerian found had counterpart nobody); fixed by the reviewer, counterpart now green-sahara-cultures; same Gobero disc on both sides.
- norte-chico-civilization -2200 gain -> nobody: exception; mirror none. Counterpart nobody; no other dossier draws the Chillon to Santa coast in -2200.
- valdivia-culture -1500 dissolve -> machalilla-culture: exception; mirror none. Successor has no dossier; listed in the author's counterparts_needing_dossiers.
- oshara-tradition 460 dissolve -> ancient-pueblo-peoples: exception; mirror none. Successor has no dossier; listed in the author's counterparts_needing_dossiers (North America group).
- a-group-culture -2900 dissolve -> nobody: exception; mirror early-dynastic-period-of-egypt None none. Page: 'apparently destroyed by the First Dynasty rulers of Egypt', not annexed; early-dynastic-period-of-egypt (me-03, 3 events) records no Lower Nubia gain, consistent.
- a-group-culture -3500 found -> nobody: mismatch; mirror naqada-culture -4000 found. Land overlap, not a transfer: naqada-culture (xx-01-a) draws Upper Egypt intersect Nile 40 km in both keyframes (-4000..-3000), 54 cells of which lie in Lower Nubia south of Aswan down to 22.14 N; early-dynastic-period-of-egypt's Cliopatria shape in -3000 holds 10 more. a-group-culture is trimmed to avoid them. Route to xx-01-a/me-03: stop the Egyptian bands at the First Cataract (Aswan, about 24.1 N), after which the A-Group can take back those cells (page: 'Early hubs ... Kubaniyya in the north ... with Aswan, Sayala, Toshka and Qustul in between').
- nabta-playa-neolithic -6000 found -> nobody: exception; mirror naqada-culture -4000 found. Nabta disc trimmed of 14 cells of the same naqada Nile band along the Lake Nasser arms; same routing as above.
- capsian-culture -5400 dissolve -> nobody: exception; mirror none. Neolithic of Capsian Tradition has no dates or extent; Tunisia and north-east Algeria blank -5399 onward (green-sahara-cultures keeps excluding it).
- aboriginal-australians -3400 dissolve -> nobody: exception; mirror none. Horizon stop, not an end; see thin. Mainland Australia blank until the colonies.
- aboriginal-tasmanians -3400 dissolve -> nobody: exception; mirror none. Horizon stop; page carries the people to 1803.
- kuk-swamp-agriculture -3400 dissolve -> nobody: exception; mirror none. Horizon stop; page gives no end.

## Gazetteer names needed

Nabta Playa (place, nabta-playa-neolithic), Gobero (place, tenerian-culture), Ténéré (region, tenerian-culture), Dhar Tichitt (place, tichitt-tradition), Silver City (place, oshara-tradition), Abu Simbel (place, nabta-playa-neolithic), Torres Strait (region, aboriginal-australians)

## Problems

- No page failed for me except https://en.wikipedia.org/wiki/Khartoum_Mesolithic (URL_NOT_FOUND, as the author reported).
- Two small fixes applied by the reviewer and revalidated: tenerian-culture /ledger/0/counterpart nobody -> green-sahara-cultures; chinchorro-culture Tocopilla 70 km disc added to the keyframe and both ledger regions (128 -> 158 cells).
- Cross-group: naqada-culture (xx-01-a) Upper Egypt Nile band runs into Lower Nubia to 22.14 N (54 cells); stop it at the First Cataract so a-group-culture and nabta-playa-neolithic can be redrawn untrimmed.
- Three Oceanian dossiers stop at -3400 by convention; Australia, Tasmania and the New Guinea highlands are blank from 3399 BCE until colonial dossiers unless extended (orchestrator decision).
- No dossier in this batch has Cliopatria shapes or an infobox area, so area checks compare page figures (where given) with the keyframe cells.
