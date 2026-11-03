# Review: batch eu-13-h (County of Savoy, Kingdom of Sicily, Norman Italy, Republic of Pisa)

Reviewer, 2026-10-25. Machine copy: `history/notes/phase-b/reviews/eu-13-h.json`.

All four dossiers validated with 0 errors and 0 warnings before the review and still do after the reviewer's fixes (`validate_dossier.py --resolve`). I spot-checked 42 events on 14 Wikipedia pages, chosen among the confidence-3 events and the ones that move the most land. None of the pages has an infobox area, so no area comparison was possible. Each dossier already says so.

Verdicts: **fix** for all four. In each one I corrected a small defect in place and checked it on the page (a reviewer note marks every edit). Each one also has findings left for the author (`applied: false`) and gaps for a gap-filler. Copies of the files as they were before the review are in `/tmp/claude-0/work/eu-13-h/bak/`.

## kingdom-of-sicily: fix

Applied by the reviewer:

- **Naples was dated October 1137 at confidence 3; the page says 1139.** The Norman conquest page has "On 30 October 1137, the last Duke of Naples died in the king's service at the Battle of Rignano", then "However, it was two years between Sergius' death and Naples' incorporation by Sicily". The quoted "That year, Roger absorbed Naples into his kingdom" sits in the page's 1139 paragraph. Under the brief this is a fail-level defect. I moved the event to 1139 (it is now `/ledger/3`), removed keyframe `kingdom-of-sicily_1137` and extended `kingdom-of-sicily_1130` to 1130-1138. This also makes the event agree with duchy-of-naples, which loses Naples in 1139.

For the author:

- **Africa is drawn twice.** `kingdom-of-africa.json` (1146-1160) draws Tripoli, Mahdia, Sousse and Sfax. The Zirid dossier (L14-L16) loses them to kingdom-of-africa, and the Almohad dossier (L23, L25) gains them from it. This dossier draws the same towns in `/ledger/7-11` and in keyframes `_1146` and `_1155`. kingdom-of-africa was not in the author's Context list. The orchestrator should pick one owner. My recommendation: Sicily drops its African unions and events and keeps a note.
- **`/ledger/6` (1144, the Abruzzi): counterpart papal-states has no mirror.** The Roger II page only says the line was "fixed by a truce with the pope in October 1144". holy-roman-empire L33 loses the Abruzzo cells to this state in 1147, so the counterpart should be holy-roman-empire.

For a gap-filler:

- Djerba 1135. zirid-dynasty L12 loses it to this state, but there is no gain here. Page: Kingdom of Africa.
- Capua 1134-1137. The Roger II page: "Robert was expelled from Capua and Roger installed his third son, Alfonso of Hauteville, as Prince of Capua" (by July 1134). principality-of-capua starts its contest in 1134.
- Manfred's Albanian coast and Corfu, 1258-1259. despotate-of-epirus L23-L24 and nicaean-empire L51 lose them to this state, but there are no gains here.
- Malta 1283 is at confidence 1. house-of-anjou-sicily L4 has 8 July 1283 (Battle of Malta page), but it gives the island to crown-of-aragon.
- The Treaty of Villeneuve, 1372, is on the Kingdom page after all ("The division in the kingdom became permanent in 1372"). Cite it in the certainty note.

Confirmed on the pages:

- 1130 coronation, 1138 invasion of Capua, Mignano 1139 (with both dates).
- The October 1144 truce, Tripoli 1146, Cape Bona 1148, "mid-1150s", Mahdia 1160.
- 1194, 1266.
- The Vespers 1282 (date right; the quoted phrase is not on the Vespers page word for word), Messina October 1282, Calabria February 1283.
- Caltabellotta 1302, the 1410 infobox.

Overlap with crown-of-aragon. Aragon draws the island in 1282-1285 (L27, L29), in 1291-1295 (L32, L34) and from 1385 (L50, confidence 1). This dossier holds it from 1282 to 1410. The author flagged this.

## norman-italy: fix

Applied by the reviewer:

- `/ledger/27`: the 1130 dissolve now has counterpart `kingdom-of-sicily`, the successor whose found event names this state.

For the author:

- **Benevento is still drawn after 1081.** The ledger gives the city up in 1081 (`/ledger/19`: "In 1081, however, Guiscard relinquished Benevento"). But the corrections of `norman-italy_1085`, `_1091`, `_1094` and `_1126` keep it: all 3 cells of a 15 km disc round Benevento lie in Cliopatria's 1085 shape, and none in the 1072 shape. Subtract `{"place": "Benevento", "km": 15}` from those corrections (and from kingdom-of-sicily_1130), or find the event that brings it back.
- **`/ledger/1`, Capua 1038.** The page does say "In 1038 Ranulf invaded Capua". But the dossier then holds Capua until 1058, while its own `/ledger/5` has Richard besiege Capua in 1057. principality-of-capua has Conrad II give Capua to Guaimar of Salerno in May 1038 and Henry III restore Pandulf IV in 1047 (Pandulf IV page). Either lower the event or add a 1047 loss.

For a gap-filler:

- Syracuse and the rest of Sicily, 1085-1087, at confidence 1. emirate-of-sicily cites the Norman conquest page for Syracuse in 1086 at confidence 3.
- Guiscard's Balkan campaign of 1081-1085 (Dyrrhachium, Macedonia, Thessaly). The byzantine-empire dossier draws these as losses to norman-italy.
- Brindisi 1070 (catepanate-of-italy L6).
- The Benevento and Molise cells inside the 1046 shape, and their drop in 1056.

Confirmed on the pages:

- 1030 Aversa, 1038, 1043 Apulia, 1059 duchy, Messina 1061, Bari April 1071, Palermo 7 January 1072.
- Salerno 1077, Benevento 1078/1081, Noto February 1091, July 1127.

Two Byzantine dossiers, catepanate-of-italy and byzantine-empire, both lose southern Italy to this state. Their owners should settle which of them draws it.

## republic-of-pisa: fix

Applied by the reviewer:

- **The Balearic occupation ran from 1113 to 1184, read from the infobox's "Balearics from 1115 to 1184".** The 1113-1115 Balearic Islands expedition page says otherwise: the fleet left Pisa in August 1113, "raided Ibiza in June" 1114, "invested Palma de Majorca in August 1114", and Palma capitulated in April 1115. Then: "The conquest of the Balearics lasted no more than a few months" and "In 1115 they were reconquered by the Almoravids". The almoravid-dynasty and taifa-of-majorca dossiers hold the islands from 1115. The occupation now runs from June 1114 to 1115, with counterpart taifa-of-majorca and the expedition page added to `sources[]`.

For the author:

- **`/ledger/10` (1258) gives Pisa the whole Judicate of Cagliari.** The page says it was "partitioned in three parts that were assigned to the Della Gherardesca family, Arborea and Gallura". giudicato-of-gallura L6 gains the north-eastern third (Ogliastra, Sarrabus) in 1258, so that third is drawn twice until 1287.
- **`/ledger/15` ends the Gallura vassalage in 1324.** But giudicato-of-gallura ends in 1287, when the judicate passes to Pisa. Add a 1287 vassal_end and a gain, or the Gallura owner changes its date.

For a gap-filler:

- Bonifacio, 1202 (confidence 1).
- The 1299 sale of part of Sardinia to Genoa.
- Castel di Castro to June 1326 (giudicato-of-arborea L5, confidence 3).
- The Visconti years. duchy-of-milan L1 gains Pisa on 13 February 1399, while this dossier keeps Pisa as a renamed state, so Pisa is drawn twice in 1399-1402.

Confirmed on the pages:

- c. 1000, Corsica 1051-1052, Sardinia 1207-1324 and the dominion over the giudicati.
- Cagliari 1256 and 1258, Corsica to Genoa 1284 (Corsica page).
- 13 February 1399, Florence 1406.

## county-of-savoy: fix

Applied by the reviewer:

- `/ledger/6-9` and `/wars/0`: the counterpart changes from dauphine, whose dossier ends in 1351, to `kingdom-of-france`. The Amadeus VI page has Humbert II surrender "his title and principality to the future King Charles V of France" in 1349. The page does not name the other party of the 1355 treaty. kingdom-of-france (eu-10) has no 1355 mirror yet.

For the author:

- **The 1536 losses stop at Vaud.** swiss-confederation L31 gains the Pays de Gex and the Savoyard lands of the Genevan basin from Savoy in 1536 (Republic of Geneva page). This dossier keeps them inside its French-occupation region, so they are drawn twice in 1536-1559. Add the loss and take it out of `/ledger/17-18` and keyframe `_1536`.

For a gap-filler (thin within the 9-page budget):

- Aosta (confidence 1), the 1395 Piedmont cells and the 1402 cells (confidence 1), and the Burgundian-War losses of 1475-76, including the Lower Valais.
- The 1156 cession south of Lake Geneva. duchy-of-zahringen L3 loses it to Savoy.
- Faucigny under Peter II and its passing to the Dauphin's wife in 1268. dauphine L1 gains it from Savoy.
- Peter II's and Philip I's gains.
- Keyframes 1440-1533 are "unverified: page budget".

Confirmed on the pages:

- 1003, 1046, Vaud 1218 and Bresse 1272 (County page; Bresse in a map caption).
- Gex 1353, the 1355 treaty, Nice 1388, Geneva 1401.
- The duchy 1416, the 1536 occupation, Cateau-Cambrésis 1559.

Further cross-dossier conflicts:

- holy-roman-empire-minor-states keeps the Vaud, Ain and Haute-Savoie cells until 1402 (L27, confidence 1). Savoy draws them from 1218, 1272 and 1355 on page evidence, so eu-09 should move its losses.
- duchy-of-zahringen's 1218 dissolve does not name Savoy.

## Other notes

- `principality-of-capua.json` was rewritten by another agent at 17:05 during this review, and now runs 861-1139 with the Norman princes. The cross-checks use the new file: Norman Italy's 1058 loss and Sicily's 1139 gain now match it.
- republic-of-amalfi's 1131 dissolve names norman-italy, which ended in December 1130. It should name kingdom-of-sicily.
- papal-states draws no Benevento enclave. Both norman-italy and duchy-of-benevento lose the city to it in 1081.
- Gazetteer names still missing:
  - Regions: Maurienne, Tarentaise, Chablais, Faucigny, Genevois, Bresse, Bugey, Gex, Viennois.
  - Places: Aversa, Melfi, Mdina, Djerba, Bonifacio.
