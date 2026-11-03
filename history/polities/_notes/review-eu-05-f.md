# Review of batch eu-05-f (Despotate of Arta, House of Tocco, Despotate of Angelokastron and Lepanto)

Reviewer eu-05-f, 2026-10-19. Machine copy: history/notes/phase-b/reviews/eu-05-f.json.

Mechanical: all three validate with 0 errors and 0 warnings (also with --resolve) as delivered. After the reviewer's fixes below, despotate-of-arta carries two expected warnings ('hospitaller-rhodes' has no dossier yet; requested under counterparts_needing_dossiers).

Neighbour dossiers read (ledgers 1350-1425): despotate-of-epirus, principality-of-achaea, byzantine-empire, plus catalan-company and domain-of-rhodes for counterpart checks. Not written yet (exception: group not run): crown-of-aragon, ottoman-empire, republic-of-florence, albanian-principalities, house-of-anjou-sicily, republic-of-venice, kingdom-of-naples.

Pages opened (WebFetch): Despotate of Arta, Gjin Bua Shpata, Muriq Shpata, Carlo I Tocco, Leonardo I Tocco, County Palatine of Cephalonia and Zakynthos, Peter Losha, Nafpaktos. All loaded. No infobox area on any of them.

## Verdicts

- despotate-of-arta: FAIL (one unapplied blocking finding, Nafpaktos; four fixes applied by the reviewer).
- house-of-tocco: FAIL (missing 1408 Glarentza gain; one fix applied by the reviewer).
- despotate-of-angelokastron-and-lepanto: FAIL (its only keyframe and every region include Nafpaktos, which the pages give to Serbia and then the Catalans until 1376/77).

## despotate-of-arta

Applied by the reviewer (re-validated):
1. /ledger/3, /ledger/4, /wars/2/belligerents: counterpart 'domain-of-rhodes' is Leo Gabalas's lordship (dossier 1204-1250), not the Hospitallers. Gjin Bua Shpata page: 'the Knights Hospitallers of Juan Fernandez de Heredia' took Nafpaktos and Vonitsa in April 1378. Now 'hospitaller-rhodes' (the Order's state on Rhodes, 1310-1522; no Cliopatria row, no dossier yet; the domain-of-rhodes dossier's notes already ask for it).
2. /ledger/5: was '1407 loss to house-of-tocco'. Muriq Shpata page: Pal Shpata 'in 1406 called in Ottoman assistance' and 'Paul ceded Angelokastron to the Ottomans (only for Carlo Tocco to capture it within less than a year)'. Now 1406, counterpart ottoman-empire. The event lies inside the 1402 shape's span and is one circle, so the keyframes stand.
3. /ledger/2: counterpart was 'unnamed holders of Nafpaktos (page silent)'. Nafpaktos page: 'In 1361 the town was captured by the Catalans of the Duchy of Athens'; 'In 1376 or 1377 it fell to John Bua Spata'. Now catalan-company, source the Nafpaktos page (added to sources[]).
4. /identity/rulers/1-4 had no source; the Despotate of Arta rulers table gives exactly these names and years (Gjin 1374-1399, Skurra 1399-1403, Muriq 1403-1415, Jakob 1415-1416). Source added.

Not applied, blocking (author):
5. Nafpaktos is drawn as Shpata land before the 1376 gain. /keyframe_review/1 (1375 shape applied from 1374), /ledger/1 region and /identity/predecessors/1 land are 'the 1375 shape minus the Arta half', which contains the 15 km Nafpaktos circle; the ledger (now sourced to the Nafpaktos page) gains it only in 1376 from the Catalans. Fix: subtract {lon 21.83, lat 38.39, km 15} from /ledger/1 region and /identity/predecessors/1 land, and give 1374-1375 a corrected shape without Nafpaktos (a new keyframe despotate-of-arta_1374, 1374-1375, = 1375 shape minus the circle, and say in /keyframe_review/1 text that the Cliopatria shape holds from 1376); keep the 1376 gain. Do the same in the sibling dossier (below) so that the 1374 merge hands over the same land.

Thin (gap-filler, not blocking):
- Serbian suzerainty: the Peter Losha infobox has 'Despot of Arta Under the Serbian Empire 1359-1374' and Simeon Uros granted the despot titles in 1360 (both pages). A vassal_start/vassal_end pair with Simeon Uros's state (the Epirus dossier uses serbian-empire for him) may be due. Page to try: https://en.wikipedia.org/wiki/Simeon_Uro%C5%A1
- Vonko's seizure of Arta, 1399-1400 (Muriq Shpata page: 'A few days after Skurra took over Arta, however, the town was captured by the adventurer Vonko'; Muriq evicted him). No event. Page to try: https://en.wikipedia.org/wiki/Muriq_Shpata (already a source) and https://en.wikipedia.org/wiki/Gjon_Zenebishi
- Ottoman vassalage of the Spata after the 1380s: not checked by the author (page budget). Page to try: https://en.wikipedia.org/wiki/Despotate_of_Epirus

Spot checks: /ledger/0 (April 1359, infobox) confirmed; /ledger/1 (1374 union, 'the Albanian despotates of Arta and Angelocastron were united under the rule of Gjin Bua Shpata') confirmed; /ledger/2-4 (Nafpaktos 1376/77, April 1378, 'again master of Nafpaktos by 1380') confirmed; /ledger/5 mis-dated and wrong counterpart (fixed); /ledger/6 (sold to Venice 1407-08) confirmed; /ledger/7-8 (4 October 1416; 'In 1416, he defeated Jakob Bua Shpata and conquered Arta thus annexing the Despotate') confirmed. Capital Arta (20.985 E 39.16 N) lies in the 1375 bbox. Area: no infobox area; Cliopatria 10,868 km2 (1375), consistent with 'from the Corinth Gulf to Acheron River'.

## house-of-tocco

Applied by the reviewer:
1. /ledger/2: counterpart despotate-of-arta to ottoman-empire (Muriq Shpata page, as above: Carlo took Angelokastron from the Ottomans within a year of the 1406 cession). Year 1407 kept.

Not applied, blocking (author):
2. Missing event: Glarentza. principality-of-achaea /ledger/35 records a 1408 loss to house-of-tocco ('Leonardo and Carlo conquered Glarentza in 1408', confidence 3) and /ledger/36 its recovery in 1414 ('Centurione was able to retake Glarentza and expel the Toccos'); the Carlo I Tocco page has 'in 1407-1408 his brother Leonardo seized and plundered the fortress of Glarentza'. The end is therefore known (1414, from the Achaea dossier's page). Fix: add a 1408 gain of Glarentza (a circle, about 21.15 E 37.94 N, 10-15 km; place name Glarentza/Kyllini) with counterpart principality-of-achaea, source the Carlo I Tocco page (and the page the Achaea dossier cites for 1408/1414); add it to /keyframe_review/3 correction (from 1408) and to /identity/successors/0 land so that it passes to despotate-of-epirus in February 1411. The Epirus dossier then needs a 1414 loss of Glarentza to principality-of-achaea, and Achaea's 1414 gain should name despotate-of-epirus (routed in cross_checks).

Not blocking, advice:
3. /ledger/0 and /identity/predecessors/0: counterpart kingdom-of-naples is a reading. The County Palatine page: 'After the death of John II Orsini in 1335, the islands were occupied by the Anjou', who held suzerainty 'as rulers of Achaea'; Robert of Taranto, who ceded the islands in 1357, was prince of Achaea and Taranto, not king of Naples, and Cliopatria's Kingdom of Naples shape is Italy only. principality-of-achaea (Robert's principality, dossier exists) or house-of-anjou-sicily (Cliopatria's Angevin row for Greece and Albania) fits the page better; pick one and say why.

Thin (gap-filler):
- Scope 1185-1357 (Margaritus of Brindisi, Orsini, Angevin occupation 1335/36-1357; County Palatine page) is not in the dossier, as the author flagged: extend backwards with rename events (counterparts_needing_dossiers).
- /ledger/1 counterpart 'previous holders of Lefkada and Vonitsa (page silent)': who held Lefkada before ca. 1362. Page to try: https://en.wikipedia.org/wiki/Lefkada
- Corinth and Megara 'seized in 1395' (Carlo I Tocco page) not drawn because the end is unknown. Page to try: https://en.wikipedia.org/wiki/Theodore_I_Palaiologos (or Corinth).
- Vonitsa (held by ca. 1362/1373, Hospitallers April 1378 per the Gjin Bua Shpata page) not drawn; one circle could be added for 1362-1378.

Spot checks: /ledger/0 (1357; 'As a reward, in 1357, Robert named him Count palatine of Cephalonia, Zakynthos and possibly Ithaca as well'; County page 'In 1357, Robert of Taranto ceded Cephalonia, Zakynthos and Ithaca') confirmed; /ledger/1 ('Probably by ca. 1362, and certainly before 1373 ... Lefkada and the port of Vonitsa') confirmed; /ledger/2 date confirmed, counterpart wrong (fixed); /ledger/3 (February 1411, Ioannina) confirmed. Capital (20.57 E 38.12 N) in the bbox. Area: no infobox area; Cliopatria 2,210 km2 (1375-1406) against about 1,640 km2 of real island land (Cephalonia, Zakynthos, Ithaca, Lefkada): grid inflation, under a factor of two.

## despotate-of-angelokastron-and-lepanto

Not applied, blocking (author):
1. Nafpaktos inside the state 1359-1374. /keyframe_review/0 correction, /ledger/0-2 regions, /identity/predecessors/0 and /identity/successors/0 land, /wars/0 zone are 'the 1375 Arta shape minus the Arta half', which contains Nafpaktos. Nafpaktos page: 'The town briefly became part of the Serbian Empire during the 1350s'; 'In 1361 the town was captured by the Catalans of the Duchy of Athens'; 'In 1376 or 1377 it fell to John Bua Spata'; Gjin Bua Shpata page: 'In 1376 or 1377, Shpata conquered Nafpaktos', and its infobox gives 'Nafpaktos or "Lepanto" (1377-78; 1380-?)'. The 'Angelokastron and Lepanto' title in the two infoboxes is a label, not a dated holding. Fix: subtract {lon 21.83, lat 38.39, km 15} from every region of the dossier (keyframe, found, merge, dissolve, predecessor and successor land, war zone), say so in the keyframe note, and keep the name (it is the infobox's). Coordinate with despotate-of-arta finding 5.

Thin (gap-filler):
- Serbian recognition: Gjin was 'recognized in early 1360s as a Despot of Aetolia and Acarnania by Simeon Uros'; a vassal pair with Simeon Uros's state may be due. Page to try: https://en.wikipedia.org/wiki/Simeon_Uro%C5%A1

Spot checks: /ledger/0 (infobox 'Despot of Angelokastron and Lepanto 1359-1374'; raids 1358; 1360 Simeon Uros) confirmed; /ledger/1-2 (1374 union) confirmed; /keyframe_review/0 line between the halves confirmed on the Peter Losha page footnote ('Despot of Arta, Rogoi and the region of Amphilochia' against 'Despot of Acheloos and Angelokastron'). Capital Angelokastron (21.2 E 38.55 N) in the shape. No article, no area.

## Cross-dossier routing

- despotate-of-epirus /ledger/47 (1359 loss to despotate-of-arta) covers both Albanian halves; it should also name despotate-of-angelokastron-and-lepanto (or split the region) now that the sibling exists.
- catalan-company has no 1361 gain of Nafpaktos and no 1376 loss of it to despotate-of-arta (Nafpaktos page). Route to the catalan-company author.
- principality-of-achaea /ledger/36 (1414 gain of Glarentza from house-of-tocco): the Tocco county ended in February 1411 inside despotate-of-epirus; the counterpart should be despotate-of-epirus, which needs the matching 1414 loss.
- despotate-of-epirus keyframes: the 1395 shape (1395-1414) lacks the Tocco islands after the February 1411 merge and the 1415 shape (1415-1421) lacks Arta after the 1416 gain (both flagged by the author).
- byzantine-empire_1352 (1352-1362) overlaps three cells of Zakynthos and Cephalonia (author's flag).
- New dossier needed: hospitaller-rhodes (Knights Hospitaller, 1310-1522): 1378 gain and 1380 loss of Nafpaktos (and Vonitsa, April 1378) against the Spata.
