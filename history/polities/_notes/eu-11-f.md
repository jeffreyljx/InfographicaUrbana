# eu-11-f: notes (written 2026-10-25)

Six dossiers: kingdom-of-powys, kingdom-of-bernicia, hwicce, kingdom-of-dunoting, kingdom-of-rheged, dumnonia. All validate (0 errors). Every event, verdict and war cites a page opened with WebFetch in this run; WebFetch returns a model's answer over the page, so quotes are as returned. 24 distinct pages opened, 1 failed (https://en.wikipedia.org/wiki/Dunoting, url_not_found twice). Repair pass 2026-10-25 (bernicia, rheged): 3 pages opened (Gododdin, Elmet, Kingdom of Strathclyde), Bernicia and Rheged re-read, 2 failed (https://en.wikipedia.org/wiki/Rhun_ap_Urien, https://en.wikipedia.org/wiki/Rhun_of_Rheged, url_not_found).

## Read first (cross-dossier items for the orchestrator and gap-fillers)
- Powys ends 1160 (Powys infobox and Madog page); Cliopatria's Powys row runs to 1168 and Powys Fadog / Wenwynwyn start 1169. Years 1161-1168 are empty unless the successors start in 1160 or the Powys end is moved to 1168.
- Hwicce ends 628 (independent state). The Hwicce page keeps a client sub-kingdom under Mercia to the 780s; the Mercia dossier should carry vassal_start / vassal_end with counterpart 'hwicce' (628..c. 780s) or the land is blank.
- Rheged now starts c. 550: Cliopatria's Brythons shapes of 540-591 hold the same land (Brythons dossier to subtract it).
- One-year overlaps with successors' first Cliopatria shapes: Bernicia 634 (Northumbria 634), Dumnonia 710 (Cornwall 710, Wessex 710), Hwicce 628 (Mercia 628). The successors' shapes should win in those years.
- Powys 1063-1084 and 900-910 new keyframes overlap Cliopatria's Gwynedd (1066-1084, 10,721 km2, contains Powys) and possibly Seisyllwg (900-910: 8,914 km2); the Gwynedd and Seisyllwg dossiers should say who holds the land.
- Dunoting: Cliopatria's Wikipedia link 'Dunoding' and Wikidata Q2264840 point at the Welsh kingdom of Eifionydd and Ardudwy, not at the Yorkshire Dales shape. wikipedia is null in the dossier; the Q-id is kept as given and should be checked.

## kingdom-of-powys (13 shapes, 9 pages: Powys, Chester, Wat's Dyke, Pillar of Eliseg, Pengwern, Rhodri Mawr, Cadwgan ap Bleddyn, Norman invasion of Wales, Madog ap Maredudd; Penda also cited)
- Row not split: the pages show one continuing kingdom (Gwertherion, Manaw, Mathrafal lines). Cliopatria's gaps (860-877, 900-910, 947-959, 1040-1084, 1094-1098) are years when Powys lies inside another shape; handled as loss/gain events (854, 878, 942, 960, 1039, 1063, 1085, 1094/1099) and two new keyframes (900-910, 1063-1084).
- Unverified (confidence 1 or 'unverified: page budget'): founding 540; the 705 eastern cut (pages tie it to Offa or the dykes, probably later than 705); 626-632 trims; the 960 return; the 1039 loss. Not opened: Offa's Dyke, Hywel Dda, Gruffydd ap Llywelyn, Bleddyn ap Cynfyn, Powys Fadog, Powys Wenwynwyn, Mathrafal.
- Disagreements: Cyngen died 854 (Powys) or 855 (Pillar of Eliseg); Chester 613 (Powys infobox, Annals of Ulster) or 616 (Powys text); Cadwgan died 1103 (Cadwgan infobox) or 1111 (its text); Gwynedd's conquest 'before 886' (infobox) against Rhodri becoming king of Powys in 854 (text).
- The 1149-1157 sequence (Cyfeiliog given to Owain Cyfeiliog and Meurig 1149; Owain Gwynedd takes Iâl c. 1150; Madog 'regained many Welsh lands' 1157) changes no Cliopatria shape; left in a war entry.
- Gazetteer: region 'Iâl' (war zone) is not in regions.jsonl.

## kingdom-of-bernicia (2 shapes, budget 1-2; 7 pages cited after the repair pass)
- Dossier life 547-634 (Ida to Oswald) against Cliopatria's 555-611 and 633. 612-632 are Cliopatria's Northumbria years; no keyframe added so Bernicia is not drawn twice.
- REPAIRED (review fail): the 604 `merge` with Deira is now a 604 `vassal_start` (counterpart kingdom-of-deira) closed by a 612 `vassal_end`, plus a 612 `merge` into kingdom-of-northumbria, mirroring the Deira dossier (604 vassal_start, 612 vassal_end, 612 merge). I took the reviewer's first option, so the Deira dossier is untouched. Bernicia page re-read: 'united Deira with his own kingdom by force around 604', infobox 'Shared crown with Deira: 604', 'merged with Deira: 654', body 'In the early 7th century, it merged with its southern neighbour, Deira' and 'from 634 onward'.
- Disagreement kept: the reviewer's wording has Edwin ruling both kingdoms 616-633 'on the page'; the Bernicia page only lists 616-633 as 'Under Deiran rule' and says 'Edwin then became king'. The 'king not just of Deira but of Bernicia as well' quote is from the Aethelfrith page (first run), so the 612 note cites it as a second page.
- Gododdin page opened (thin item): Catraeth 'in around 600', an 'Angle stronghold, perhaps Catterick'; the page names no Anglian kingdom there, so it is a war entry with belligerents 'Gododdin' and 'Angles of Catraeth', not a Bernician war. The 638 siege of Eidyn lies after the 634 end and is not entered; the page says the Gododdin 'seem to have come under the rule of Bernicia around this time', which sits better with the infobox's 654 than with the 634 end. The Northumbria dossier should carry Lothian.
- Infobox gives 654 for the merger with Deira, the body 634; the Northumbria page gives 651/654. Not opened: Bamburgh.

## hwicce (5 shapes, 4 pages: Hwicce, Deorham, Ceawlin, Penda)
- 587 expansion toward Bath is Cliopatria's (page: West Saxon occupation 'may have ended as early as 584'). Confidence 1.
- Not opened: Tribal Hidage, Mercia history of the 628 settlement, Wessex.

## kingdom-of-dunoting (2 shapes, 3 pages; page failed)
- All years are Cliopatria's (confidence 1); no opened page dates the kingdom. Only the Latin 'Regio Dunutinga' (Life of Wilfrid), the eponym Dunaut / Dunot and a Dent / North Yorkshire location are on the Hen Ogledd and Dent pages. Needs a page on the Life of Wilfrid or on Craven / Elmet.
- The shape lies about 4 km east of Dent; left as drawn.

## kingdom-of-rheged (4 shapes plus 1 new keyframe; 5 pages, then Elmet and Strathclyde in the repair pass)
- REPAIRED (review fail): the war 572-593 lay before the 592 start. The start is now c. 550 (confidence 1, a bridge): the Rheged page lists 'Urien Rheged, (c. 550 – 590)' and gives no founding year (infobox era 'c.500' is the Hen Ogledd). Changed: identity.start, the found event, the Carlisle capital's from, the certainty span, the Brythons predecessor year (549), and a new keyframe kingdom-of-rheged_550 (550-591, adjust, correction = Cliopatria's 592 shape). The extent before 592 is unknown. I did not move to c. 500: the page dates no king before Urien and treats Coel Hen as doubtful.
- CROSS-DOSSIER: Cliopatria's Brythons shapes of 540-591 contain Rheged's land (Brythons falls from 64,870 to 51,613 km2 in 592 as Rheged and Dunoting begin), so the Brythons dossier must remove Rheged's land from c. 550 or the land is drawn twice.
- Thin items: Rhun ap Urien and Rhun of Rheged returned url_not_found, so the 638 growth (230 km2) is still unreported. The Elmet page names Rheged but gives no annexation year and not 646 (it dates Edwin's overrunning of Elmet to 616 or 617). The end 646 stays Cliopatria's, confidence 1; the Rheged page says only 'annexed by Northumbria, some time before AD 730' and a possible peaceful takeover after Oswiu's marriage 'probably in 638'.
- Strathclyde successor: the Strathclyde page says it 'expanded south to the Cumbrian Mountains, into the former lands of Rheged' (undated) and at its 10th-century greatest extent reached 'the River Eamont at Penrith'. Cliopatria's Strathclyde shapes all end at lat 54.953 and never overlap Rheged, so the land spec is now Rheged's land north of Penrith (a polygon fallback, 8 cells) and the note says it is not a 646 handover. Disagreement kept: the infobox lists Strathclyde as a successor at the same level as Northumbria; the schema defines successors as those who took the land at the end, which only Northumbria did on any page.
- The shape has no Dumfries and Galloway and runs south of Rochdale; both are uncertain on the page. The Strathclyde dossier should say whether Galloway was Rheged's.
- Ruler list not given: the infobox names Meirchion Gul, Cynfarch Oer, Urien and Owain mab Urien; regnal dates only for Urien.

## dumnonia (2 shapes, 2 pages: Dumnonia, Peonnum)
- Cliopatria's shape is constant 602-709; the pages show West Saxon advances at c. 658 (to the Parrett) and 681-685 (to the Bristol Channel). Corrected with new keyframes dumnonia_602b (Somerset added before 658) and dumnonia_685 (Somerset removed); Somerset is Natural Earth's county.
- End 710 is the battle year; the page has no end date (rump state after 813-822, last king 875, Athelstan c. 936). Devon's take-over in 710 is Cliopatria's, the page does not support it that early.
- Not opened: Geraint of Dumnonia, Hehil, Ine, Wessex.

## Counterparts that need dossiers or care
- Welsh Dunoding (Eifionydd and Ardudwy, 5th-10th c.): no Cliopatria row; the Gwynedd dossier may cover it.
- Kingdom of Elmet: no Cliopatria row; named on the Hen Ogledd page ('managed to survive into the early 7th century').
