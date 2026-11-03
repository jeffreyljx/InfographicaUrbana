# Review of batch eu-14-f (Phase B)

Reviewed 2026-10-25 by the adversarial reviewer. Validator (--resolve) passed all six dossiers (only the two intended empty-correction warnings in house-of-oldenburg). Pages were opened with WebFetch on 2026-10-25. The machine copy is history/notes/phase-b/reviews/eu-14-f.json.

Verdict convention for this run: `fix` = everything needed was applied by the reviewer; a finding marked *author* must be done by the author; *advisory* findings are recommended or routed to another dossier.

## Verdicts

- **teutonic-order**: fail
- **danish-magnates**: thin
- **kalmar-union**: thin
- **livonian-conference**: fail
- **house-of-oldenburg**: fail
- **prussian-confederation**: fail

## teutonic-order (fail)

Findings:
- `/ledger (1466-10, 1525-4)` [author]: No vassal_start/vassal_end for the Order's status as a Polish fief 1466-1525, although the suzerain's dossier carries both. Evidence: Second Peace of Thorn (1466) page: 'The eastern part remained with the Teutonic Order as a fief of the Polish Crown' (signed 19 October 1466); house-of-jagiellon ledger has 1466-10 vassal_start and 1525-4 vassal_end with counterpart teutonic-order. The reviewer brief (item 3) requires the vassal's own ledger to mirror them; 'vassalage belongs in the suzerain's dossier' is not an accepted exception. Fix: Add {year:1466, month:10, type:vassal_start, counterpart:house-of-jagiellon, region:{cliopatria:'Teutonic Order', year:1468, text:'the eastern part ... as a fief of the Polish Crown'}, source: Second_Peace_of_Thorn_(1466), confidence:3} and a vassal_end 1525-4 with the same counterpart before the dissolve (Prussian Homage, State page).
- `/identity/capitals/0-1` [author]: Capitals Acre (1230-1290) and Venice (1291-1308) lie outside every Teutonic shape: they are the Order's headquarters, not a seat of the Prussian state, and would plot the state's capital in Palestine and Italy. Evidence: Reviewer brief item 9: capitals must fall inside the state's shapes in those years; shapes.csv bbox of teutonic-order_1236..1305 is 17.1-29.3 E, 52.9-59.9 N; Acre is 35.07 E 32.93 N, Venice 12.33 E 45.44 N. The author's own capital notes say 'Headquarters of the Order, not of the Prussian state'. Fix: Drop the two entries (capitals start in 1309 at Marienburg) or replace them with a Prussian seat from a page (Thorn/Torun or Elbing, the Landmeister's seat), and move Acre/Venice to the notes.
- `/ledger/18/counterpart` [author]: Gotland 1398 is gained from 'kingdom-of-sweden', which is not alive in 1398: that dossier merges into kalmar-union in June 1397 and reappears only in 1502. Evidence: Teutonic Order page: 'King Albert of Sweden ceded Gotland to the Order as a pledge'; 'An invasion force under Grand Master Konrad von Jungingen conquered the island in 1398'. Albert was the deposed Mecklenburg king (deposed 1389); kingdom-of-sweden ledger: 1397-6 merge into kalmar-union, 1502 split. Fix: Use a free-text counterpart for the pledge-holder (e.g. 'Albert of Mecklenburg / Victual Brothers') and list it under counterparts_needing_dossiers, or 'nobody' with a note; do not cite a dossier that is dead in 1398.
- `/keyframe_review/2 and /ledger/3` [author]: K2 removes the Pskov and Leningrad cells from the 1241 shape from 1241 on, yet L3 records their loss in 1242: the ledger loses land the keyframes never draw. Evidence: K2 correction = 1241 shape minus Pskov and Leningrad oblasts for 1241-1249; L3 (1242, conf 1) loses the same intersect. One of the two is wrong. Fix: Either keep the cells (or Pskov alone) in a new 1241-1242 keyframe and let L3 remove them in 1242 (the Order held Pskov 1240-1242, see the Battle on the Ice page), or delete L3 and keep K2 as is.
- `/keyframe_review/1` [advisory]: K1 (1236-1240) adds the Swordbrothers' land from 1236, a year before the 1237 union recorded in L2; livonian-brothers-of-the-sword also draws it to 1237, so 1236 is double-drawn. Evidence: L2 gain 1237 (Livonian Order page: 'most of the former Swordbrothers became members of the Teutonic Order' in 1237); livonian-brothers-of-the-sword ledger: 1237 merge/dissolve teutonic-order. Fix: Keep the 1236 shape alone for 1236 (verdict ok for 1236) and add a new keyframe teutonic-order_1237 (1237-1240) with the union correction.
- `/ledger/29/counterpart` [applied by reviewer]: Neumark 1455 was sold to 'margraviate-of-brandenburg', whose dossier ends in March 1414; the live counterpart is electorate-of-brandenburg, which records the 1455 gain from teutonic-order. Evidence: Thirteen Years' War page: 'In 1454 and 1455, the Teutonic Knights first pawned, then sold the Neumark back to the Margraviate of Brandenburg'; margraviate-of-brandenburg end 1414-3, successor electorate-of-brandenburg; electorate-of-brandenburg ledger 1455 gain cp teutonic-order. Fix: counterpart: electorate-of-brandenburg (applied by the reviewer; file re-validated).

Gaps for a gap-filler:
- `/ledger/25`: 1422 split of the Livonian branch is Cliopatria's (conf 1); no page dates it. Try: https://en.wikipedia.org/wiki/Treaty_of_Melno
- `/ledger/3`: What the Order held east of the Narva in 1240-1242 (Pskov, Koporye) and when it was lost. Try: https://en.wikipedia.org/wiki/Battle_on_the_Ice
- `/ledger (1392-1411)`: Dobrzyn Land pledges 1392-1405 and 1409-1411, Treaty of Salynas 1398 and Peace of Raciaz 1404 (Samogitia), Peace of Brzesc Kujawski 1435. Try: https://en.wikipedia.org/wiki/Dobrzy%C5%84_Land
- `/ledger (1317-1343)`: Michalow Land, relinquished by Poland at Kalisz 1343 (page: 'relinquishes Pomerelia, Chelmno Land and Michalow Land'), has no gain event. Try: https://en.wikipedia.org/wiki/Micha%C5%82%C3%B3w_Land
- `/notes`: Whether Harrien-Wierland stayed under the Prussian Grand Master to 1525 (Plettenberg page) or passed to the Livonian branch in 1347; affects the 1422 split. Try: https://en.wikipedia.org/wiki/Wolter_von_Plettenberg
- `/identity/rulers`: No Grand Master list (rulers null). Try: https://en.wikipedia.org/wiki/Grand_Master_of_the_Teutonic_Order

Spot checks:
- `/ledger/15` (https://en.wikipedia.org/wiki/Treaty_of_Kalisz_(1343)): confirmed: 'signed on 8 July 1343'; Poland 'regains Kuyavia and Dobrzyn Land'
- `/ledger/18` (https://en.wikipedia.org/wiki/Teutonic_Order): confirmed: 'conquered the island in 1398' after Albert's pledge (counterpart wrong, see fixes)
- `/ledger/20` (https://en.wikipedia.org/wiki/State_of_the_Teutonic_Order): confirmed: table 'Neumark | 1402-1455'; 'the Luxembourgs gave the region in pawn'
- `/ledger/32` (https://en.wikipedia.org/wiki/Second_Peace_of_Thorn_(1466)): confirmed: 19 October 1466; Gdansk/Eastern Pomerania, Chelmno Land, Elbing and Marienburg, Warmia to Poland
- `/ledger/29` (https://en.wikipedia.org/wiki/Thirteen_Years%27_War_(1454%E2%80%931466)): confirmed: pawned 1454, sold 1455
- `/ledger/30` (https://en.wikipedia.org/wiki/Thirteen_Years%27_War_(1454%E2%80%931466)): confirmed: 'On 6 June 1457, the castles of Marienburg, Dirschau, and Eylau were transferred to the Polish army'
- `/ledger/17` (https://en.wikipedia.org/wiki/Danish_Estonia): confirmed: sold 1346 for 19,000 marks; sovereignty shifted 1 November 1346

Area: Neither the Teutonic Order nor the State of the Teutonic Order infobox has an Area field (read 2026-10-25); the author's source note says 'no area figure'.

## danish-magnates (thin)

Findings:
- `/keyframe_review/2` [advisory]: K2 (Cliopatria 1344 shape, span 1344-1351) adds the Estonian province for the whole span, though Estonia was sold on 1 November 1346; teutonic-order K12 draws it from 1346, so 1347-1351 is drawn twice unless the window agent applies L3 inside the span. Evidence: Danish Estonia page: 'The shift of sovereignty from Denmark to the Teutonic Order took place on 1 November 1346'; K2 note itself says 'The Estonian province is added for 1344-1346'. Fix: Give the Estonian addition its own new keyframe danish-magnates_1344 limited to 1344-1346 and a new keyframe danish-magnates_1347 (1347-1351) = the 1344 shape alone; or say in K2's text that L3 removes Estonia in November 1346.
- `/identity/end and /ledger/3/counterpart` [advisory]: The row's polity (Denmark 'subdued by various mortgagees' after Christopher II) lasted eight years on the page, i.e. to 1340, but the dossier holds Estonia to 1346 and Jutland to 1351; the 1346 seller was the restored crown, not the mortgagees. Evidence: Christopher II page: 'Upon his death Denmark ceased being a formal kingdom, and for the next eight years it was subdued by various mortgagees'; successor in the infobox 'Valdemar IV Atterdag'; the Danish Estonia page lists a new captain (Konrad Preen) from 1340. The teutonic-order L17 note itself says 'The seller is the Danish crown'. Fix: Open Valdemar IV's page and decide: end the dossier in 1340 with the Estonian province and the Jutland sliver passing to kingdom-of-denmark (then the 1346 sale belongs to kingdom-of-denmark, which is not written yet), or keep Cliopatria's span and state in notes that 1340-1351 is a Cliopatria construct.

Gaps for a gap-filler:
- `/ledger/4`: 1351 end and the 4,720 km2 southern-Jutland sliver of 1344-1351 (conf 1, page silent). Try: https://en.wikipedia.org/wiki/Valdemar_IV_of_Denmark
- `/identity/end`: Date of Valdemar IV's accession and the end of the mortgagee regime (1340). Try: https://en.wikipedia.org/wiki/Valdemar_IV_of_Denmark

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Christopher_II_of_Denmark): confirmed: 'Died: 2 August 1332'; mortgagees 'for the next eight years'
- `/ledger/1` (https://en.wikipedia.org/wiki/Danish_Estonia): confirmed: Reval and Wesenberg 'handed over to the Order by the pro-German party on 16 May 1343'
- `/ledger/2` (https://en.wikipedia.org/wiki/Danish_Estonia): confirmed: sovereignty shifted 1 November 1346
- `/ledger/3` (https://en.wikipedia.org/wiki/Danish_Estonia): confirmed: 'sold for 19,000' Cologne marks to the Teutonic Order in 1346

Area: The article (Christopher II) is a person's; no area. Author's estimate: Harju + Laane-Viru + Ida-Viru about 11,000 km2 against 13,776 km2 (ratio about 1.23), noted in K1.

## kalmar-union (thin)

Findings:
- `/wars/8/to` [applied by reviewer]: Swedish War of Liberation ended 1524, a year after the union's end (1523-6); wars must lie inside the life. Evidence: Swedish War of Liberation page: infobox Date '1521-23'; 'Stockholm was taken on 17 June' 1523; Gustav Vasa proclaimed king 6 June 1523. Fix: to: 1523 (applied by the reviewer; the outcome still mentions the Treaty of Malmo of 1 September 1524; file re-validated).
- `/keyframe_review/1,2,4,5 vs /keyframe_review/6` [advisory]: The 1402-1428 shapes are marked ok although their own notes say Sweden and Finland are 'drawn only in part (1,617 of 2,440 and 797 of 1,695 cells)'; the 1429 shape adds about 315,000 km2 of northern Sweden, Finland and Norway with no ledger event, so the change between K5 and K6 is unexplained. Evidence: shapes.csv: kalmar-union_1422 954,515 km2, kalmar-union_1429 1,269,468 km2; the sum of the predecessors' 1395-1401 shapes (Sweden 349,561 + Norway 519,922 + Denmark 95,830) is about 965,000, and Sweden's own 1526 shape (673,138) already holds the north. No page dates a 1429 change (K6 note). Fix: Pick one reading and make keyframes and ledger agree: mark K0-K5 adjust with the northern cells added (union with the Kalmar 1429 shape's Swedish, Finnish and Norwegian cells) if the north was already the kingdoms' in 1397, or add a 1429 gain from 'nobody' at confidence 1 saying the north enters the drawing; coordinate with kingdom-of-sweden, whose 1375 shape lacks the same north.
- `/wars/1/zones` [advisory]: Engelbrekt rebellion (1434-1436) has empty zones and its outcome does not say no ground changed hands; the rebels took Sweden's castles and deposed Eric. Evidence: Reviewer brief item 10: empty zones only where no ground changed hands, and said so. Kalmar page (W1 outcome as written): it 'led to Eric's overthrow in Denmark and Sweden in 1439'. Fix: Add a contest_start/contest_end pair over the Swedish realm (Kingdom of Sweden 1502 shape) for 1434-1436 from the Engelbrekt page, with the war's zone, or state why no ground moved.

Gaps for a gap-filler:
- `/keyframe_review/6`: Dated evidence for the northern lands (Norrland, Lapland, Ostrobothnia) in 1397-1428. Try: https://en.wikipedia.org/wiki/Treaty_of_N%C3%B6teborg
- `/ledger/3`: Greenland cells leave in 1429 (conf 1) while norse-greenland dissolves in 1408; align the two. Try: https://en.wikipedia.org/wiki/Hvalsey_Church
- `/wars/1`: Engelbrekt rebellion's dates and ground. Try: https://en.wikipedia.org/wiki/Engelbrekt_rebellion
- `/notes`: Eric of Pomerania on Gotland 1439-1449; capital dates; ruler list; Iceland and the Faroes. Try: https://en.wikipedia.org/wiki/Eric_of_Pomerania

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Kalmar_Union): confirmed: 'Inception: 17 June 1397'
- `/ledger/8` (https://en.wikipedia.org/wiki/Christian_I_of_Denmark): confirmed: February 1449 part of the Norwegian council backed Karl
- `/ledger/10` (https://en.wikipedia.org/wiki/Christian_I_of_Denmark): confirmed: Swedish reign '23 June 1457 - 23 June 1464'
- `/ledger/11` (https://en.wikipedia.org/wiki/Christian_I_of_Denmark): confirmed: 'in Ribe 5 March 1460'; Duke of Schleswig and Count of Holstein that year
- `/ledger/12` (https://en.wikipedia.org/wiki/Christian_I_of_Denmark): confirmed: reign in Sweden ended 23 June 1464
- `/ledger/13` (https://en.wikipedia.org/wiki/Kalmar_Union): confirmed: 'in 1472 the Kingdom of Scotland annexed the islands' (footnote 1470)
- `/ledger/17` (https://en.wikipedia.org/wiki/Swedish_War_of_Liberation): confirmed: 'The war began in January 1521'
- `/ledger/18` (https://en.wikipedia.org/wiki/Swedish_War_of_Liberation): confirmed: proclaimed king at Strangnas on 6 June 1523

Area: The Kalmar Union infobox has no Area field (read 2026-10-25); the author's K1 note says so.

## livonian-conference (fail)

Findings:
- `/ledger (1559, 1561-11)` [author]: No vassal_start/vassal_end for Livonia's Polish-Lithuanian protection 1559-1561, although house-of-jagiellon carries vassal_start 1559-6 and vassal_end 1561-11 with counterpart livonian-conference. Evidence: Livonian War page: 'In June 1559, the estates of Livonia came under Polish-Lithuanian protection through the first Treaty of Vilnius' (the author's war note gives 31 August 1559; the house-of-jagiellon dossier uses June). Fix: Add vassal_start 1559 (month 6 per the Livonian War page, or 8 if the Treaty of Vilnius (1559) page is opened and says 31 August) counterpart house-of-jagiellon over the remaining Livonian lands, and vassal_end 1561-11 before the dissolve.
- `/ledger (1560)` [author]: The Russian conquest of Fellin (Viljandi) and the defeat at Ergeme in August 1560 are missing: land moved between the 1559 and 1561 keyframes with no event. Evidence: Livonian War page: 'The Livonian knights suffered a disastrous defeat by the Russians at the Battle of Ergeme in August 1560'; the tsar's forces took Fellin (Viljandi) in the same campaign (no month). Fix: Add a 1560 loss (and extend the Russian contest zone) of Fellin/Viljandi county to tsardom-of-russia, confidence 2, and carry it into keyframes K5 (to 1560) and K6.
- `/ledger/4/region` [author]: The 1559 sale is of the Bishopric of Osel-Wiek, but the region is Saare county only (Wiek and Dago are left in the confederation); denmark-norway's mirror gain takes Osel-Wiek and Pilten. Evidence: Livonian War page: the bishop of 'Osel-Wiek' signed on 26 September 1559 giving Frederick II the right to nominate the bishop, 'a sale for 30,000 thalers'; denmark-norway ledger 1559 gain cp livonian-conference text 'the Bishopric of Osel-Wiek and Courland's Pilten'. Fix: Region: union of Estonia admin1 Saare, Hiiu and Laane (Osel-Wiek), carried into K5 and K6; settle Pilten with the denmark-norway author.
- `/wars/1/to` [applied by reviewer]: Livonian War listed to 1583, after the confederation's end (1561-11); wars must lie inside the life. Evidence: Livonian War page: the Order 'was dissolved by the second Treaty of Vilnius in 1561'. Fix: to: 1561 (applied by the reviewer, with a note that the war itself ran to 1583; file re-validated).

Gaps for a gap-filler:
- `/ledger/0`: 1422 start (conf 1): pages give the Diet of 1419 and the Walk agreement of 4 December 1435, not 1422. Try: https://en.wikipedia.org/wiki/Treaty_of_Melno
- `/wars/0`: Russo-Livonian War 1501-1503 (pages failed); zones empty with status quo. Try: https://en.wikipedia.org/wiki/Battle_of_Smolino

Spot checks:
- `/ledger/1` (https://en.wikipedia.org/wiki/Livonian_Confederation): confirmed (page served as Terra Mariana): agreement 'signed in Walk on 4 December 1435'
- `/ledger/2` (https://en.wikipedia.org/wiki/Livonian_War): confirmed: Dorpat and Narva taken in 1558 (May/July, footnote reverses the order)
- `/ledger/4` (https://en.wikipedia.org/wiki/Livonian_War): date confirmed (26 September 1559); region incomplete: the page names Osel-Wiek
- `/ledger/5` (https://en.wikipedia.org/wiki/Livonian_War): confirmed: 1561, Harrien-Wierland and Jerwen yielded to Sweden; Reval accepted Swedish rule
- `/ledger/6` (https://en.wikipedia.org/wiki/Livonian_War): year confirmed: 'dissolved by the second Treaty of Vilnius in 1561' (no day on this page)

Area: No infobox area; the Terra Mariana text gives about 67,000 km2 for the Order and about 41,000 km2 for the Church by the mid-14th century; compared with the 1422 shape in K0.

## house-of-oldenburg (fail)

Findings:
- `/identity` [author]: A dynasty dossier for a house that succeeded on the same land without a break; it draws nothing (both shapes wrong with empty corrections) and its land is already corrected inside kalmar-union (K9, K10, rename 1448-9). Evidence: Schema, identity.type: 'a dynasty that merely succeeds another on the same land without a break is not a new dossier (master plan rule 2)'; the author's own report: 'house-of-oldenburg is not a separate state ... The orchestrator may prefer to merge it'. Both rows share Seshat sv_kalmar_union. Fix: Merge: add 'House of Oldenburg' to kalmar-union's cliopatria_names, move the two shape verdicts (house-of-oldenburg_1450, _1453: wrong, land handled by kalmar-union K9/K10/K11) into kalmar-union's keyframe_review, and withdraw house-of-oldenburg.json (orchestrator's call).
- `/wars/0/from` [applied by reviewer]: Contest for Norway began in 1449, before this row's start (1450-8); wars must lie inside the life. Evidence: Christian I page: Karl crowned in Trondheim 20 November 1449; Christian crowned there 2 August 1450. Fix: from: 1450 with a note that the contest began in February 1449 (applied by the reviewer; file re-validated). Moot if the dossier is merged.
- `/ledger/0/counterpart` [advisory]: The found event names kingdom-of-sweden, which is not alive in 1450 in its own dossier (merged into kalmar-union 1397-6 until 1502). Evidence: kingdom-of-sweden ledger: 1397-6 merge, 1502 split, nothing for 1448-1457. Fix: Leave as is if the kingdom-of-sweden dossier is given its 1448-1457 reign (cross-check routed); otherwise moot after the merge.

Gaps for a gap-filler:
- `/ledger/1`: 1458 end is Cliopatria's (conf 1); no page will date it because the row is an artefact. Try: https://en.wikipedia.org/wiki/House_of_Oldenburg

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Christian_I_of_Denmark): confirmed: 'on 2 August he was crowned king of Norway in Trondheim' (1450)

Area: A dynasty article; no area. Both shapes are marked wrong.

## prussian-confederation (fail)

Findings:
- `/ledger (1454-3)` [author]: The Confederation's lands were incorporated into Poland and its delegates swore allegiance to Casimir IV in March 1454, but the dossier records no relation to house-of-jagiellon: it stands as an independent rebel state for twelve years, and house-of-jagiellon's own contest over the same land (1454-3 contest_start cp teutonic-order) has no link to it. Evidence: Prussian Confederation page: the King 'signed an act of incorporation in Krakow in March 1454' and the delegates 'pledged allegiance to the Polish King'; Thirteen Years' War page: 'delegates of the Prussian Confederation pledged allegiance to Casimir on 6 March 1454'. The author's report asks house-of-jagiellon to carry this vassal_start, but neither dossier does. Fix: Either add vassal_start 1454-3 counterpart house-of-jagiellon (region West Prussia) and vassal_end 1466-10, or end the dossier in March 1454 with a merge into house-of-jagiellon and move the Order's contest counterpart to house-of-jagiellon from 1454-3 (matching house-of-jagiellon's contest_start). State the choice in notes.
- `/identity/successors/0` [advisory]: The successor's land (West Prussia) is recorded by house-of-jagiellon as a 1466-10 gain from teutonic-order, not from prussian-confederation. Evidence: house-of-jagiellon ledger: 1466-10 gain cp teutonic-order (two events). Fix: Follows from the fix above; if the Confederation stays a vassal, ask the house-of-jagiellon author to note that the land came through the Confederation.

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Prussian_Confederation): confirmed: 'In February 1454, the Prussian Confederation rose against the Teutonic Order's rule'
- `/ledger/1` (https://en.wikipedia.org/wiki/Thirteen_Years%27_War_(1454%E2%80%931466)): confirmed: rebellion two days after 4 February 1454
- `/ledger/2` (https://en.wikipedia.org/wiki/Second_Peace_of_Thorn_(1466)): confirmed: signed 19 October 1466 (war page text says 10 October; month unaffected)
- `/ledger/3` (https://en.wikipedia.org/wiki/Prussian_Confederation): confirmed: 'ceased to exist as such' after the 1466 peace (no exact date)

Area: New state with no Cliopatria row; the page has no infobox.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| teutonic-order 1230 found (duchy-of-masovia) | - | exception | duchy-of-masovia not written (eu-15 has not run). |
| teutonic-order 1237 gain (livonian-brothers-of-the-sword) | livonian-brothers-of-the-sword 1237 merge | matched | K1 draws the land from 1236 (see fixes). |
| teutonic-order 1242 loss (novgorod-republic) | - | exception | novgorod-republic not written (eu-16); L3 loses cells K2 never draws. |
| teutonic-order 1308 gain (kingdom-of-poland) | - | exception | kingdom-of-poland not written (eu-15); also 1332 gain, 1343 loss, 1422 loss (Nieszawa). |
| teutonic-order 1309 gain (margraviate-of-brandenburg) | margraviate-of-brandenburg 1309 loss | matched | Pomerelia, Treaty of Soldin. |
| teutonic-order 1346 gain (danish-magnates) | danish-magnates 1346 loss | matched | Estonia, 1 November 1346; the seller was arguably the restored crown (kingdom-of-denmark), see danish-magnates fixes. |
| teutonic-order 1398 gain (kingdom-of-sweden) | kingdom-of-sweden 1397 merge | mismatch | Gotland: kingdom-of-sweden is merged into kalmar-union from 1397-6 and has no 1398 event; counterpart is not alive. |
| teutonic-order 1398 gain (grand-duchy-of-lithuania) | - | exception | grand-duchy-of-lithuania not written (eu-15); also the 1411 loss of Samogitia. |
| teutonic-order 1402 gain (margraviate-of-brandenburg) | margraviate-of-brandenburg 1402 loss | matched | Neumark pawned. |
| teutonic-order 1408 loss (kalmar-union) | kalmar-union 1408 gain | matched | Gotland. |
| teutonic-order 1422 split (livonian-conference) | livonian-conference 1422 found | matched | Both at confidence 1 (Cliopatria's boundary). |
| teutonic-order 1455 loss (electorate-of-brandenburg) | electorate-of-brandenburg 1455 gain | matched | After the reviewer's counterpart fix (was margraviate-of-brandenburg, dead since 1414). |
| teutonic-order 1457 loss (house-of-jagiellon) | house-of-jagiellon | missing | Marienburg 6 June 1457: house-of-jagiellon has no 1457 gain (its 1454-3 contest covers the land); small. |
| teutonic-order 1466 loss (house-of-jagiellon) | house-of-jagiellon 1466 gain | matched | West Prussia and Warmia (two events each side). |
| house-of-jagiellon 1466 vassal_start (teutonic-order) | teutonic-order | missing | teutonic-order has no vassal_start 1466 / vassal_end 1525 (fix listed). |
| teutonic-order 1525 dissolve (duchy-of-prussia) | duchy-of-prussia 1525 found | matched | April 1525. |
| duchy-of-pomerania 1329 loss (teutonic-order) | teutonic-order | missing | duchy-of-pomerania records Stolp lands lost to the Order 1329, regained 1341, and Lauenburg-Butow gained from the Order 1466; teutonic-order has none of these. Route to both authors to verify. |
| house-of-jagiellon 1454 contest_start (teutonic-order) | teutonic-order 1454 contest_start | mismatch | teutonic-order's Thirteen Years' War contest names prussian-confederation only (1454-2); house-of-jagiellon's names teutonic-order (1454-3). |
| teutonic-order 1454 contest_start (prussian-confederation) | prussian-confederation 1454 contest_start | matched | Ends 1466-10 on both sides. |
| prussian-confederation 1454 vassal_start (house-of-jagiellon) | - | missing | Allegiance to Casimir IV 6 March 1454 recorded in neither dossier. |
| prussian-confederation 1466 dissolve (house-of-jagiellon) | house-of-jagiellon 1466 gain | mismatch | house-of-jagiellon gains West Prussia from teutonic-order, not from prussian-confederation. |
| danish-magnates 1332 found (kingdom-of-denmark) | - | exception | kingdom-of-denmark not written yet (eu-14 sibling part); also the 1351 dissolve. |
| kalmar-union 1397 found (kingdom-of-denmark) | kingdom-of-sweden 1397 merge | matched | kingdom-of-sweden 1397-6 merge cp kalmar-union; old-kingdom-of-norway 1397-6 dissolve with successor kalmar-union; kingdom-of-denmark not written. |
| kalmar-union 1408 gain (teutonic-order) | teutonic-order 1408 loss | matched | Gotland. |
| kalmar-union 1429 loss (nobody) | norse-greenland 1408 dissolve | mismatch | Kalmar keeps 20 Greenland cells to 1428 (conf 1); norse-greenland dissolves in 1408 to nobody. Align. |
| kalmar-union 1435 loss (Counts of Holstein (Holstein-Rendsburg)) | duchy-of-schleswig | mismatch | Counterpart has no dossier (listed county-of-holstein), but duchy-of-schleswig exists and draws Schleswig as a Danish vassal 1058-1864 with no change in 1435 or 1460: the two models of Schleswig conflict. Route to duchy-of-schleswig's group. |
| kalmar-union 1448 loss (kingdom-of-sweden) | kingdom-of-sweden | mismatch | kingdom-of-sweden is absorbed 1397-1502; it has no 1448 secession, 1457 return, 1464 secession, 1497 return, 1520 return or 1521-1523 contest. Route to kingdom-of-sweden: rows for 1448-1457, 1464-1497, 1501-1520, 1521-1523. |
| kalmar-union 1449 contest_start (kingdom-of-sweden) | kingdom-of-sweden | missing | Norway contest 1449-2 to 1450-8 (Karl Knutsson); same root cause. |
| kalmar-union 1460 gain (Counts of Holstein (Holstein-Rendsburg)) | holy-roman-empire-minor-states 1459 loss | mismatch | HRE minor states lose 32 Holstein cells to kalmar-union in 1459 (conf 1); Kalmar names the Counts of Holstein. Year within one; counterpart naming differs. |
| kalmar-union 1472 loss (kingdom-of-scotland) | kingdom-of-scotland 1472 gain | matched | Orkney and Shetland. |
| kalmar-union 1501 loss (kingdom-of-sweden) | kingdom-of-sweden 1502 split | matched | Within a year; kingdom-of-sweden's split is conf 1. |
| kalmar-union 1523 dissolve (denmark-norway) | denmark-norway 1526 found | mismatch | denmark-norway starts 1526 (conf 1); 1523-1525 undrawn. Route to denmark-norway: start 1523. |
| livonian-conference 1422 found (teutonic-order) | teutonic-order 1422 split | matched | conf 1 both. |
| pskov-republic 1422 loss (livonian-conference) | livonian-conference | missing | Two Cliopatria cells, conf 1; small, inside livonian K0. |
| livonian-conference 1558 loss (tsardom-of-russia) | - | exception | tsardom-of-russia not written (eu-16); also the contest 1558-1561. |
| livonian-conference 1559 loss (denmark-norway) | denmark-norway 1559 gain | mismatch | Land differs: Livonian gives Saare only, denmark-norway Osel-Wiek and Pilten. |
| house-of-jagiellon 1559 vassal_start (livonian-conference) | livonian-conference | missing | Livonian ledger has no vassal_start 1559 / vassal_end 1561-11. |
| livonian-conference 1561 loss (kingdom-of-sweden) | kingdom-of-sweden 1561 gain | matched | Sweden has month 6 and omits Ida-Viru (Narva held by Russia since 1558). |
| livonian-conference 1561 loss (house-of-jagiellon) | house-of-jagiellon 1561 gain | matched | November 1561. |
| livonian-conference 1561 loss (duchy-of-courland) | - | exception | No dossier; listed in counterparts_needing_dossiers (Cliopatria row covers only 1734-1793). |
| house-of-oldenburg 1450 found (kingdom-of-sweden) | kingdom-of-sweden | mismatch | Same root cause as the Kalmar-Sweden mismatches. |

## Gazetteer names wanted

Pomesania (region, teutonic-order), Samland (region, teutonic-order), Chelmno Land (region, teutonic-order), Dobrzyn Land (region, teutonic-order), Neumark (region, teutonic-order), Michalow Land (region, teutonic-order), Nieszawa (place, teutonic-order), Kwidzyn (place, teutonic-order), Harrien-Wierland (region, danish-magnates), Osel-Wiek (region, livonian-conference)

## Counterparts needing dossiers

- Royal Prussia (Polish province) (royal-prussia, 1454-1772)
- Counts of Holstein (Holstein-Rendsburg) (county-of-holstein, 1326-1460)
- Duchy of Courland and Semigallia (duchy-of-courland, 1561-1795)
- Duchy of Livonia (duchy-of-livonia, 1561-1621)
- Free imperial city of Riga (riga, 1561-1581)

## Problems

- Verdict convention for this run: 'fix' = everything needed was applied by the reviewer; findings with applied false and blocking true need the author; blocking false are advisory or routed. Four small fixes were applied and re-validated (teutonic-order /ledger/29 counterpart; kalmar-union /wars/8/to; livonian-conference /wars/1/to; house-of-oldenburg /wars/0/from).
- No infobox on the Teutonic Order, State of the Teutonic Order, Kalmar Union or Christopher II pages carries an Area field; area checks for those are recorded as null.
- The Livonian_Confederation URL serves the Terra Mariana article (as the author reported).
- Sibling dossiers outside this batch need work found here: kingdom-of-sweden (no 1448-1523 secessions), denmark-norway (starts 1526 not 1523), duchy-of-schleswig (no 1435/1460 change), norse-greenland vs kalmar-union Greenland cells, house-of-jagiellon (no 1457 Marienburg gain; prussian-confederation link), duchy-of-pomerania (Stolp, Lauenburg-Butow) - see cross_checks.
- Page budget: teutonic-order used 10 pages for itself against 9 (author reported); not counted as a fault.
