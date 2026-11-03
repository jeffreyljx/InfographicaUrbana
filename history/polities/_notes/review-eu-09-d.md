# Review of batch eu-09-d (House of Habsburg, House of Ascania, House of Hohenstaufen)

Reviewer, 2026-10-25. Validator (--resolve): 0 errors for all three; warnings are unknown gazetteer places and the counterparts county-of-gorizia / county-of-tyrol (no dossiers yet, listed by the author). Neighbour dossiers read: duchy-of-bavaria, duchy-of-styria (also kingdom-of-france, house-of-valois-anjou, house-of-bourbon, ottoman-empire: none names a batch slug). The other Context polities have no file yet (groups not run).

## house-of-habsburg: fix (fixed by the reviewer)

Applied (re-validated, 0 errors, read back):
- /ledger/5 and /ledger/7: counterpart county-of-gorizia -> county-of-tyrol. County of Tyrol: "When their sons divided their estate in 1271, the elder Meinhard II took Tyrol"; "he received the Duchy of Carinthia with the Carniolan march in 1286"; "Henry II 1295–1335, son of Meinhard II, also Duke of Carinthia". The Gorizia line never held Carinthia.
- /ledger/8: counterpart county-of-tyrol -> duchy-of-bavaria. duchy-of-bavaria draws Tyrol 1342-1362 (its /ledger/4) and records the 1363 loss to house-of-habsburg (its /ledger/7); County of Tyrol: Margaret and Louis V "ruled Tyrol and Brandenburg in personal union".
- /keyframe_review/22 and /23: correction year 1449 -> 1431. The 1449 reference is the 1440 shape, whose six unsourced cells /keyframe_review/21 removes; 1450-1457 re-added them.
- /identity/rulers/0: Rudolf I from 1260 (infobox "Count of Habsburg 1239–1291").

Spot checks (all confirmed): 1311 Savinja, 1374 Pazin, 1382 Trieste (House of Habsburg); 1335 Carinthia/Carniola, 1282 Augsburg (Duchy of Austria); 1363 Tyrol, 1490, 1500 Gorizia (County of Tyrol); 1415 Aargau, 1460 Thurgau (Old Swiss Confederacy); 29 January and 28 October 1453, 23 November 1457 (Ladislaus the Posthumous); 1482, 1506, 1507-1530, 1515/1516 (Habsburg Netherlands); 1264 Kyburg, November 1276, 1286 Meinhard (Rudolf I). No area on the House of Habsburg infobox.

Thin (for a gap-filler; budget of 14 pages was spent):
- Rulers 1365-1404 missing (Albert III, Leopold III, Albert IV); Duchy of Austria gives no reign years. Try Albert_III,_Duke_of_Austria.
- /ledger/12 (1402, confidence 1): about 1,300 km2 at 9.0-10.5E, 46.6-48.0N, probably Vorarlberg (Feldkirch 1375, Bludenz 1394). Try Vorarlberg.
- /ledger/6 Savinja 1311 has no counterpart; the 1456 Celje inheritance (duchy-of-styria /ledger/6) is absent here. Try Counts_of_Celje.
- /keyframe_review/5 (1294, ok): Zug, Schwyz and part of Lucerne leave the shape with no event; Lucerne 1291/1332/1386, Zug 1352, Glarus 1388 have none. Try Growth_of_the_Old_Swiss_Confederacy.
- Breisgau and Freiburg (1368) have no gain but are used in the 1469 pawn region. Try Freiburg_im_Breisgau.
- /wars/5 (League of Cambrai) zones empty; Rovereto, Riva, Cortina taken 1509-1511. Try War_of_the_League_of_Cambrai.
- /ledger/29 (confidence 1) and the month of Vienna's fall 1485; Hungarian hold on Styria and Carinthia. Try Siege_of_Vienna_(1485).
- /ledger/31, /36, /37: bridging split/merge/dissolve between the House of Habsburg and Habsburg Monarchy rows: orchestrator decision.

Cross-dossier: duchy-of-styria draws Styria as its own polity 1180-1918 with new keyframes, while the Habsburg shapes contain Styria 1276-1515 (and duchy-of-styria's 1276 event is a rename, not a loss). Styria is claimed twice: orchestrator decision.

## house-of-ascania: fail

The author's diagnosis of the Cliopatria row is right (checked in shapes.csv: the Electorate of Saxony row stops in 1428 and resumes in 1487 with this row's bbox; this row grows by 5,700 km2 northward in 1429). The corrections are wrong in one respect that the author's own source contradicts:
- Orlamünde is drawn as Ascanian to 1486. House of Ascania: "Orlamünde was sold to the Wettins on April 25, 1344."; "In 1354, Orlamunde was annexed to the House of Wettin". Add a 1344 loss (Wettins; confidence 3), a new keyframe from 1344 (split /keyframe_review/5), and drop the Orlamünde disc after it and from /ledger/10.
- Weimar is drawn as Ascanian to 1486. Same page: "After Herman's death Weimar was annexed to the House of Wettin." (Herman VI d. 1372 in its table) and "By 1467, the Ascanians no longer held any possessions, as the Wettins took over everything." Add a 1372 loss, split /keyframe_review/7 (1370-1387), drop the Weimar disc after it and from /ledger/10. "Weimar-Orlamünde (until 1486)" in the branch list is the line's extinction, not land: fix the dissolve note, the successors text and the notes.
Smaller fixes for the author:
- /ledger/8 note says the Bernburg lands went to "the Anhalt-Dessau line"; Principality of Anhalt: "inherited by the princes of the sole remaining line, that of Anhalt-Zerbst".
- Counterparts "Bishopric of Halberstadt" (/ledger/3) and "House of Welf" (/ledger/6-7) are not slugs and not listed: use prince-bishopric-of-halberstadt and principality-of-luneburg (now listed in the review report).
- Lüneburg 1370-1388 was granted to the Saxe-Wittenberg dukes, whose land the dossier hands to electorate-of-saxony from 1363: say why it stays here, or move it.
Spot checks: 1307 Zerbst, 1370 and 1388 Lüneburg (House of Ascania), 1315 Aschersleben, 1468, 1471/1473 (Principality of Anhalt): confirmed; 1486 dissolve: year only. Thin: Lüneburg extent (War_of_the_Lüneburg_Succession); Weimar-Orlamünde extent (Thuringian_Counts'_War).

## house-of-hohenstaufen: thin

Spot checks confirmed (Duchy of Swabia): 1079-1268; "persisted until 1268, ending with the execution of the last Hohenstaufen duke Conradin"; 1266 pledge to Ulrich II of Württemberg; 1266 departure; no area in the infobox. Missing mirror: duchy-of-bavaria /ledger/1 records a 1268 gain from house-of-hohenstaufen; Louis the Strict (verified): "After the young prince's execution in Naples in 1268, Louis inherited some of Conradin's possessions in Swabia". Add a 1268 loss to duchy-of-bavaria (Bavaria's region: Duchy of Bavaria 1272 minus 1260; confidence 2) and duchy-of-bavaria in successors.

## Counterparts needing dossiers (beyond the author's list)
principality-of-luneburg (1269-1705), prince-bishopric-of-halberstadt (804-1648); the Wettin land 1260-1486 (author's margraviate-of-meissen) is also the counterpart of the missing Ascanian losses of 1344 and 1372.
