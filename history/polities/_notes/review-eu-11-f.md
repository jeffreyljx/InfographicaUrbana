# Review of eu-11-f (2026-10-25)

Reviewer: adversarial pass on six dossiers. Validator (--resolve): 0 errors in all six; one warning (Powys /wars/4/zones/0 'Iâl' not in the gazetteer). Only one neighbour dossier exists (kingdom-of-deira); every other counterpart belongs to an eu-11 part that has not run, so those cross-checks are exceptions. No infobox in this batch gives an area (checked on each page), so the area check could not be made; every author note says so.

| slug | verdict | why |
| --- | --- | --- |
| kingdom-of-powys | pass | 5 spot checks confirmed (854, 942, by 1086, 1099, 1160). Confidence-1 events listed as thin. |
| kingdom-of-bernicia | fail | 604 merge disagrees with Deira's 604 vassal_start and draws Deira twice; no 612 event before the 633 gain from Northumbria. |
| hwicce | pass | 577, 628 and the Penda 628 battle confirmed; 587 gain honestly confidence 1. |
| kingdom-of-dunoting | thin | No article; all years Cliopatria's (confidence 1), within a 1-2 page budget. Quotes from Hen Ogledd confirmed. |
| kingdom-of-rheged | fail | War 572-593 lies before the 592 start; the page has Rheged under Urien c. 550-590, so the start is mis-dated (confidence 1). |
| dumnonia | fix (applied) | 658 (confidence 3), 681-685, 710 confirmed; reviewer added the missing explanation for the empty 710 war zones. |

## kingdom-of-bernicia (fail)
1. /ledger/1: 604 is a `merge` with kingdom-of-deira (region Kingdom of Deira 592). The Deira dossier has 604 `vassal_start` (counterpart kingdom-of-bernicia), 612 `vassal_end` and a 612 `merge` into Northumbria, and keeps its own 592-611 shape. With Bernicia's 555 keyframe left `ok`, the merge adds 12,958 km2 that no keyframe shows, and Deira is drawn twice in 604-611. Fix: match Deira. Use a 604 `vassal_start` with counterpart kingdom-of-deira (confidence 2) and a 612 `vassal_end` (confidence 1). Or keep the merge, but then Deira ends in 604 and Bernicia's 555 keyframe becomes `adjust`; the orchestrator decides which side changes.
2. Missing 612 event: the state lives 547-634 and no shape is drawn for 612-632, yet nothing hands Bernicia to Northumbria. As a result the 633 gain from Northumbria has no earlier loss to match. Fix: add a 612 `merge` with counterpart kingdom-of-northumbria (region Kingdom of Bernicia 555, confidence 1), matching kingdom-of-deira /ledger/3.
- Spot checks confirmed on the Bernicia page: Ida about 547; Deira united by force around 604 (infobox: shared crown 604, merged 654); Eanfrith 633-634; Oswald's union in 634.
- Thin: Catraeth and Din Eidyn (638) are not covered (try Gododdin).

## kingdom-of-rheged (fail)
1. /wars/0 runs 572-593, but identity.start is 592, so the war starts before the state's life does. The 592 start is Cliopatria's (confidence 1) and the Rheged page contradicts it: the infobox era is 'c.500' and the body has 'Urien Rheged, (c. 550 - 590)'. Fix: move the start to c. 550, together with /ledger/0, the capital's `from`, the certainty span and the predecessor year. Add a new keyframe kingdom-of-rheged_550 for 550-591 (`adjust`, correction Kingdom of Rheged 592). Or keep 592 and drop the war, which stays in Bernicia.
- Confirmed on the page: 'annexed by Northumbria, some time before AD 730'; Oswiu's marriage 'probably in 638', a possible peaceful takeover; Royth 'possibly the last king'; capital Carlisle (inside the shape bbox).
- Thin: the 638 growth and the 646 annexation are confidence 1. The second successor, Strathclyde, takes no Rheged land in 646-647.

## dumnonia (fix, applied by reviewer)
- /wars/2/note: the zones were empty and the note did not say why, although /ledger/3 moves Devon in 710. Prepended: 'Zones left empty: the Dumnonia page says only ... names no land ...; the ledger's 710 loss of Devon is Cliopatria's (confidence 1).' Re-validated with 0 errors and 0 warnings, and read back.
- Confirmed: Peonnum in 658 (infobox c. 660), the advance 'to the River Parrett, annexing eastern and central Somerset' (confidence 3 holds); the Parrett border 'until 681-685', then Somerset 'west and north to the Bristol Channel'; 'In 710 Geraint was defeated in battle by King Ine of Wessex'; capital Tintagel.
- Thin: the 602 found, the 710 Devon loss and the 710 dissolve are confidence 1. The infobox location adds 'parts of ... Dorset', which no keyframe mentions. Cross-group: the Wessex dossier must not draw eastern Somerset before 658, because the new keyframe dumnonia_602b gives all of Natural Earth's Somerset to Dumnonia.

## kingdom-of-powys (pass)
- Tried: the 854 Rhodri takeover, the 942 Hywel Dda takeover, Rhydwhiman 'by 1086', Cadwgan's recovery in the year after 1098, and the death of Madog (about 9 February 1160). All match the notes. The row was not split, which is justified: the pages show one continuing kingdom, and the gaps are periods of absorption, handled with paired events and two new keyframes.
- Thin (confidence 1): the 540 found, the 550 capital move, the 705 eastern cut (try Offa's Dyke), the 960 return (try Hywel Dda) and the 1039 loss (try Gruffydd ap Llywelyn). The ruler list has a gap from 617 to 694.
- For the orchestrator: years 1161-1168 are empty between Powys (ends 1160) and Powys Fadog / Wenwynwyn (start 1169). The Gwynedd dossier should drop Powys from its 1066-1084 shape (see keyframe kingdom-of-powys_1063). Gazetteer: Iâl.

## hwicce (pass)
- Confirmed: established 577 after Deorham; a client of Mercia after 628 (Cirencester); assimilated in the 780s; Penda took over the Severn valley in 628. The 587 gain is honestly confidence 1, since the page says only that occupation 'may have ended as early as 584' (try Battle of Fethanleag).
- Cross-group: Mercia should carry vassal_start / vassal_end for hwicce, 628 to the 780s.

## kingdom-of-dunoting (thin, by design)
- The quotes from Hen Ogledd are confirmed ('Regio Dunutinga', Dunaut, Dent). https://en.wikipedia.org/wiki/Dunoting is url_not_found for the reviewer too. Both events are Cliopatria's at confidence 1 (try Vita Sancti Wilfrithi, Craven). The capital, Dent, is a name-place 4 km outside the shape. The Wikidata id Q2264840 probably belongs to the Welsh Dunoding.

## Cross-dossier matrix (summary)
- Mismatch: Bernicia 604 merge (counterpart deira) against Deira 604 vassal_start (counterpart bernicia).
- Missing: Deira 612 vassal_end (counterpart bernicia) has no mirror in Bernicia.
- Every other territorial event is an exception, because its counterpart dossier has not been written yet: Mercia, Wessex, Gwynedd, Seisyllwg, Northumbria, Norman England, Brythons, Cornwall, Powys Fadog and Powys Wenwynwyn. The machine copy is history/notes/phase-b/reviews/eu-11-f.json.
