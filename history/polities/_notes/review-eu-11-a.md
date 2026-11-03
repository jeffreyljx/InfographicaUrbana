# Review of batch eu-11-a (2026-10-25)

Dossiers: brythons (fail), anglo-saxon-england (fail). Both validate with --resolve, 0 errors, 0 warnings. Spot checks (10 events, all confidence-3 events included) found every quoted sentence on its page with its year; no fabricated event. The failures are missing events and shape/ledger inconsistencies, most of them at the edges with neighbour dossiers. Cell counts below come from history/tools/gazetteer.py on Cliopatria shapes and gazetteer regions.

## brythons: fail

Applied by the reviewer (re-validated): /wars/4 belligerents were "Cadwallon (Britons)"; now kingdom-of-gwynedd, kingdom-of-mercia, kingdom-of-northumbria. The note said the Bernicia page does not name Mercia or Penda; the page says Edwin "was defeated and killed by Cadwallon ap Cadfan of Gwynedd and Penda of Mercia". The ledger's Mercian events are 617 and 628, not 633.

For the author:

1. Missing event 875 (brythons_870 to brythons_875). The 17 cells that leave the shape all lie in Cliopatria's Gwynedd 875 shape, and the keyframe note says so, but the ledger has no event. Add a loss to kingdom-of-gwynedd in 875: intersect Brythons 870 with Kingdom of Gwynedd 875, confidence 1. Page to try: Rhodri the Great.
2. Missing loss of Cumbria in 1085. 18 cells north of the Eamont (Carlisle and the Eden valley) leave in 1085 to no Cliopatria row, and no event records it. The brythons_1085 note says "18 unassigned" without saying where they are. The Celtic Britons page says Strathclyde fell "in the 1090s when it was effectively divided between England and Scotland". Add the loss, either in 1085 (Cliopatria) or in 1092 (Carlisle) with an adjust keyframe for 1085-1091. The counterpart is norman-england, or nobody with a note.
3. Kent double claim, 455-479. brythons_455/462/469 keep 9 of the 18 cells of Cliopatria's Kent (west Kent). kingdom-of-kent draws its whole 490 shape from 455, and anglo-saxon-england hands Kent over in 455. Add a 455 loss to kingdom-of-kent (Kingdom of Kent page, "Established: c. 455") and set those keyframes to adjust, minus Kingdom of Kent 490.
4. Sussex double claim, 477-479. brythons_469 holds all of Sussex (16 of 16 cells of region Sussex; anglo-saxon-england_469 holds none). kingdom-of-sussex draws region Sussex from 477. Add a 477 loss to kingdom-of-sussex, plus a new keyframe brythons_477 (477-479) that is brythons_469 minus Sussex. anglo-saxon-england's 477 split goes.
5. Missing 592 split to kingdom-of-dunoting: 6 cells. Dunoting's dossier records "found 592, counterpart brythons".
6. Rheged year: this dossier splits Rheged off in 592, while kingdom-of-rheged founds itself in 550 and draws its 592 shape for 550-591. All 43 cells stay in the Brythons shapes until 591. One side must change; the orchestrator routes it.
7. Rheged 638: kingdom-of-rheged has a 638 gain from brythons (2 cells, named in the brythons_638 note). Add the matching loss (confidence 1), or agree that it is noise.

Thin by design (budget 14 of 14 pages): 21 events at confidence 1. Pages to try: Kingdom of Powys, Hwicce, Waroch II, Hen Ogledd, Penda of Mercia, Seisyllwg, Cumbria (kingdom), Gruffydd ap Llywelyn, Deheubarth, Lordship of Galloway (for the 1235 end). Shapes 644-869, 960-1084 and 1099-1235 rest on Cliopatria alone. That is noted as "unverified: page budget" and is not a fault.

Area: the Celtic Britons and Sub-Roman Britain pages have no infobox area (checked); acknowledged.

Cross-group: salian-franks (eu-07) takes "Brittany minus its 500 shape" from brythons in 501 (Clovis "led his troops to Armorica"). brythons keeps 84 Brittany cells until 586, so 501-509 is a double claim. Isle of Wight: 2 cells leave brythons_523 for Cliopatria's Wihtgar row in 523, but wihtgar founds itself in 534 from nobody, so the island belongs to no dossier in 523-533 (minor). breton-kingdoms names its counterpart as nobody where brythons names a 587 loss to it.

## anglo-saxon-england: fail

1. /ledger/2, the 477 split to kingdom-of-sussex, is of land this state does not hold. Its own anglo-saxon-england_469 note says "Sussex ... is not inside this shape yet", and 0 of the 16 Sussex cells are in that shape (all 16 are in brythons_469). Delete the split; Sussex comes from Brythons land (brythons item 4).
2. The anglo-saxon-england_441 correction (minus Kent) covers the whole span 441-461, but Kent is founded in 455. The 9 Kent cells inside the shape therefore belong to no dossier in 441-454. Set _441 to ok and add a new keyframe anglo-saxon-england_455 (455-461) that carries the minus-Kent correction.
3. Successors 3 and 4 and the notes say East Anglia (44 cells) and Essex (18 cells) are in no Cliopatria shape of 534. That is false: kingdom-of-east-anglia_534 (52 cells) and kingdom-of-essex_534 (16 cells) both start in 534, wholly inside the 533 shape. Only 19 of its 290 cells are in no 534 row. Use the Cliopatria specs for these successors and correct the texts.
4. Essex: kingdom-of-essex founds itself in 527 from this state ("Established: 527"), but this dossier keeps Essex to 533. Either add a 527 split with a keyframe anglo-saxon-england_527 (527-533) minus Essex, or agree 534 with the Essex author.
5. Deira: kingdom-of-deira founds itself c. 450 from this state and draws its 555 shape for 450-533. Of its 54 cells, 19 are in ASE and 35 in Brythons before 480, and 52 are in ASE from 480 to 533. This dossier names Deira only as a 534 successor. The author flagged this in the notes but left the double claim; the orchestrator must pick one start and route the matching events to both dossiers.

Thin: /ledger/3 (the 480 growth of 144 cells, undated; the Sub-Roman page puts the York-Bournemouth line after Badon "around 490") and /ledger/4 (the 533 hand-over). Area: no infobox area on History of Anglo-Saxon England (checked); acknowledged.

## Spot checks (all confirmed)

brythons: 441 (Anglo-Saxon settlement), 547 (Bernicia), 577 (Battle of Deorham), 638 (Gododdin), 900 (Rheged; the page names no counties, so confidence 2 is right), 1094 (Norman invasion of Wales). anglo-saxon-england: 441, 455 (Kingdom of Kent), 477 (Kingdom of Sussex; year confirmed, counterpart wrong), 480 (Sub-Roman Britain, page silent on the year as stated). One note was not on its page: /wars/4 (fixed).
