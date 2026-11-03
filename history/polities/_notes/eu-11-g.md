# Notes, group eu-11-g (England, Scotland, Wales, Ireland, part g)

Written 2026-10-25 by the Phase B agent. States: kingdom-of-northumbria, strathclyde, cornwall, danelaw, kingdom-of-seisyllwg, kingdom-of-alba. All six validate (python3 -I history/tools/validate_dossier.py, with --resolve: no unknown names; two intended "resolves to no cells" warnings in danelaw). Quotation marks in the dossiers enclose strings the fetch tool returned as quotations; other wording paraphrases its summary of the page (WebFetch only; no raw page text was available).

## Convention used for new keyframes
New keyframes (shape_id not in shapes.csv) are meant to override the Cliopatria shape in the years they cover (danelaw 915-946, kingdom-of-northumbria 867-869 and 936-954, kingdom-of-seisyllwg 905-910, kingdom-of-alba 1136-1156). Where a Cliopatria shape is right only for part of its span, the verdict is adjust with the valid years in the correction text; the renderer must read that text. Two Danelaw keyframes (927-938, 944-946) are deliberately empty.

## kingdom-of-northumbria (612-954, 17 keyframes, 27 events)
- Start 612 is Cliopatria's; pages put the union of Bernicia and Deira at c. 604 (Bernicia, Aethelfrith pages) or 654 (Northumbria infobox). The Bernicia/Deira dossiers carry 604-612.
- Year 633 has no Northumbria shape; ledger loss/gain pairs with kingdom-of-bernicia and kingdom-of-deira (633/634).
- Lindsey is inside every shape from 626 to 681; pages support 627-633 (Edwin, "eastern Mercia"), 655-659 (inside Oswiu's Mercia) and 674-679 (Ecgfrith) only. 634-673 doubtful, not cut. The Mercia dossier cites a Mercian Supremacy page dating a Mercian loss of Lindsey to 661.
- Oswine's separate Deira (to c. 651) and the Norse client kings of Bernicia (867-872) are not drawn. Mercian revolt 657 or late 659 (Oswiu page) vs 658 (Mercia dossier). Elmet 616 or 626 (Edwin page) vs 616/617 (Elmet dossier).
- Ends 954, not Cliopatria's 935: the England dossier carries Bamburgh as a vassal 927-954; keyframe 936-954 reuses the 935 shape.
- Tiny shape moves at 705 (+2 cells) and 750 (-1 cell) are page-silent (confidence 1). Six cells of Cumbria near Carlisle pass to Strathclyde c. 900 (event; the shapes are corrected in the repair section below).
- Ten pages opened (budget nine): Gododdin added for the 638 step. Rulers: see the repair section.

## strathclyde (644-1033, 7 keyframes, 5 events)
- Page: established 5th century; Cliopatria and the Brythons dossier start it at 644.
- Cumbria is drawn by Cliopatria in the Brythons row (20 cells at 900), not in Strathclyde. Rheged page ("around 900") and Strathclyde page ("early 10th century") put it under Strathclyde: the 870-1033 shapes are adjusted to add it; the Brythons dossier should drop it.
- 647-749 shape has a 12-cell northern salient to 56.7 N (Loch Lomond/Cowal) beyond the page's northern limit; it goes to Dal Riata's shape in 750 (page silent). Kyle taken by Northumbria 750 (inside the shape, 6 of East Ayrshire's 7 cells: corrected in the repair section).
- Eamont: 27 July 927 (Strathclyde page) vs 12 July 927 (Aethelstan page). 945 grant to Malcolm I (recovered "soon") and Carham 1018 are war entries only; no border result on the pages (the 927-937 Eamont tie is now an event: repair section).
- Capitals Dumbarton then Govan (the page hedges the move). Rulers omitted (see the repair section).
- Pages failed: https://en.wikipedia.org/wiki/%C3%93engus_I_of_the_Picts and https://en.wikipedia.org/wiki/Óengus_I_of_the_Picts (url_not_found); the unaccented Oengus_I_of_the_Picts loaded.

## cornwall (710-946, 2 keyframes, 2 events)
- Short ledger by design: no opened page dates a Cornish border move. Cornwall page: Egbert raided 815, Gafulforda 825, Hingston Down 838 (Cornish and Danes defeated), Dumgarth drowned 875, Aethelstan set the Tamar boundary 936 (doubted on the Aethelstan page). The Wessex dossier carries the vassal tie from 825 (its vassal_end is missing).
- Shape = modern Cornwall less one north-eastern cell (14 cells, 3,541 km2; infobox 3,562 km2). The page's William of Malmesbury story implies Cornish land east of the Tamar before 936; the shape does not show it.
- No capital and no rulers: no opened page names a seat. Dumnonia dossier ends 710 and hands over here; the England dossier gains Cornwall in 947 (Cliopatria's year).

## danelaw (878-954, 13 keyframes, 18 events)
- Cliopatria's row (878-959) is the Danelaw to 918 and the York remnant to 959, but keeps the whole to 921 and the remnant through English years. New keyframes 915, 917, 918 follow Edward the Elder's reconquest (Bedford 915; Northampton, Cambridge, East Anglia, Derby 917; Leicester, Stamford, Nottingham 918; Lincoln unclear). No land at all 927-938 and 944-946 (York English); Olaf Guthfrithson holds York 939-943.
- The England dossier holds York 927-947 continuously and lacks the 939-944 interlude (Aethelstan page: York chose Olaf after 27 October 939; York page: Eadmund expelled the Viking leaders in 944). A gap-filler should add it there. Its contest 947-954 is mirrored here.
- Tettenhall 910 (Edward and York pages) vs 911 (Danelaw timeline). Treaty of Alfred and Guthrum dated between 878 and 890; the 880 growth (+43 cells, the later Five Boroughs) is page-silent (confidence 1).
- Ends 954 (page: "Viking rule ended ... in 954"), not 959. The Danelaw as a legal region outlasts this. Capital York is a convention (note in the dossier). Rulers omitted.

## kingdom-of-seisyllwg (878-920, 6 keyframes, 4 events)
- Seisyllwg ends 920 when Hywel Dda merges it with Dyfed into Deheubarth (Seisyllwg and Hywel pages; the deheubarth dossier starts 920). Cliopatria's 922 and 947 shapes are marked wrong: they add Gwynedd's cells (922) and Powys's (947) to Hywel's realm. The 900-910 shape swallows Powys (page-silent) and is corrected to the 878 shape; Dyfed is added from 905 (Cadell and Hywel pages say 904-905; Cliopatria 911).
- Cadell's death 909 (Cadell, Hywel pages) vs 911 (Seisyllwg page). Cadell reigns from 872 (page) vs Cliopatria 878.
- England/Wessex dossiers name kingdom-of-seisyllwg in vassal events at 918 (Wessex), 927 and 959 (England); after 920 the counterpart should be deheubarth, and the 918 tie needs a vassal_end at 920. The Hywel Dda page does not mention Eamont.
- No capital (no page), no rulers.

## kingdom-of-alba (900-1293, 11 keyframes, 15 events)
- Page: Alba runs "between the deaths of Donald II in 900 and of Alexander III in 1286"; Cliopatria 900-1293, then the Kingdom of Scotland row. A rename event marks 1286, the dissolve is 1293 (confidence 1).
- Moray: page says not part of Alba until the early 13th century and Alba lay "between the Firth of Forth and the River Spey"; the shape holds all of Moray and 67 of 108 Highland cells from 900. Not cut (no year on the page). Gap-filler: tint Moray as a vassal or cut it.
- The English counties David I held (Carlisle/Cumberland from 1136, Northumberland earldom from 1139, given up 1157) are not in any Cliopatria Alba shape; new keyframes 1136 and 1139 add them. Cumbria is the whole admin1 (the page names Carlisle and Cumberland), a coarse reading. The Norman England dossier has its own side (1092, 1136, 1139): reconcile; I did not open a page for 1092.
- Lothian: event 973 (Bernicia page; England dossier mirrors); Carham 1018 or 1016 and Edgar's "beneficence" are historians' alternatives (Carham page). Galloway 1234 (Lordship page) vs shape 1236 vs a 1135 revolt (Alba page). Hebrides 1266 (Treaty of Perth, 2 July) vs shape 1272; the Isle of Man is settled by the treaty but is in no Alba shape.
- Not opened (budget): Abernethy 1072, Cnut about 1031, Falaise 1174 and Canterbury 1189 (Angevin dossier has the ties), the 1098 treaty with Magnus Barelegs. The fetch showed no infobox: no area, no capital. Rulers omitted.

## Region names the gazetteer lacks (optional additions; all were expressed with existing names)
Elmet (West Riding: Leeds, Bradford, Wakefield, Kirklees, Calderdale used), Lindsey (Cliopatria's Kingdom of Lindsey used), Pictland (north of the Forth), Galloway, Kyle (East Ayrshire used), Cumbria north of the Eamont.

## States needing a dossier
Moray (mormaerdom/kingdom, c. 900-1230), see the Alba note. No other counterpart is missing: every slug named exists as a dossier file.

## Repair of 2026-10-25 (review eu-11-g: kingdom-of-northumbria and strathclyde failed; the other four are untouched)
Both dossiers validate with --resolve, 0 errors and 0 warnings. Pages reopened with WebFetch on 2026-10-25: Oengus I of the Picts, Egbert of Wessex, Rheged, Aethelstan, Northumbria, Mercia, Dunoding, Dal Riata, Edmund I, List of monarchs of Northumbria, List of kings of Strathclyde. Two guessed Kyle URLs (Kyle,_Scotland and Kyle_(district)) failed (url_not_found); no page on Kyle itself was read.

### kingdom-of-northumbria (now 18 keyframes, 32 events, 34 rulers)
- Keyframes 926-935 and 936-954 are adjust: the shape less the six Cumbrian cells near Carlisle. The 870 keyframe is valid 870-899; a new keyframe 900-925 draws the shape without Cumbria. The 954 dissolve region is the corrected shape.
- Ledger: the 927 rename is now vassal_start (month 7, kingdom-of-england) with a vassal_end at 954, mirroring England's ledger 2 and 14. Added: 750 gain of Kyle from strathclyde (Oengus I page, confidence 3; keyframes 750 and 866 hold East Ayrshire); 867 loss of Kyle to nobody (confidence 1: no page says what became of Kyle after 750; it is my bridge, the earliest year the drawn kingdom shrinks); 829 vassal_start and 830 vassal_end with kingdom-of-wessex (Egbert of Wessex page: "Later in 829 ... Ecgberht received the submission of the Northumbrians at Dore"; the Northumbria page is silent; the end year is Wessex's own bridge, confidence 1).
- Thin items: Dunoting 626 stays confidence 1. The Dunoding page is about the Welsh Dunoding (Eifionydd and Ardudwy, "until the line of rulers descended from Dunod expired in c. 925") and does not mention Northumbria; Cliopatria's Kingdom of Dunoting shape lies in the Yorkshire Dales (about 2.39-1.89 W, 53.66-54.41 N), so the row's Wikipedia title does not fit its shape (for the Dunoting author and the gazetteer/Cliopatria notes). Rheged 647 stays at 1 ("annexed by Northumbria, some time before AD 730"; marriage "probably in 638 ... possible that it was a peaceful takeover"). The 705 (+2 cells) and 750 (-1 cell) moves stay at 1: Mercia and Northumbria pages silent.
- Rulers 612-872 from the List of monarchs of Northumbria (unified kings and Ecgberht I). Not carried: the page's later entries are split between a York column and a Bamburgh column with gaps (877-895, 918-947), and several are marked "possibly".
- Disagreement: none with the reviewer. Note the Wessex dossier cites "Egbert,_King_of_Wessex"; I opened "Egbert_of_Wessex" (the same article).

### strathclyde (now 8 keyframes, 7 events)
- Kyle is out of the shapes from 750 (keyframe 750 adjust: minus East Ayrshire; the 870-1028 corrections carry the minus; no page returns it). The two notes that said Kyle was outside the shape are rewritten.
- The 870 keyframe is the Clyde shape less Kyle (valid 870-899). A new keyframe 900-959 and the 960, 980 and 1028 corrections add Cumbria as the union of the Brythons part (20 cells) and the Northumbria part (6 cells), 26 of the admin1's 30 cells; ledger 900 has the same region. Corrected shapes: 34 cells (870), 60 cells with Cumbria.
- Dissolve: counterpart kingdom-of-alba, region the corrected 1028 shape.
- Added vassal_start 927 (month 7) and vassal_end 937 with kingdom-of-england (Aethelstan page: 12 July 927; "In the autumn they joined with the Strathclyde Britons under Owain to invade England", 937). England's own end is confidence 1; mine is 2.
- Not done: the 945 grant is not coded (Edmund I page: "gave the kingdom to Malcolm I of Scotland in return for a pledge to defend it on land and on sea", with two scholarly readings of the tie and no duration; Dyfnwal's recovery is the Strathclyde page's, undated). The 750 Dal Riata loss stays confidence 1 (Dal Riata and Oengus I pages silent; the dal-riata dossier has no gain to mirror it). No ruler strip: the List of kings of Strathclyde prints reign years only for 633-816 and 859 (some marked uncertain), and only death or floruit dates for the later kings.

### For neighbour authors (not edited here)
- kingdom-of-alba ledger 1034 takes the 40-cell Clyde shape (and one Cumbrian cell) from Strathclyde; the 25 other Cumbrian cells reach no Alba shape until norman-england ledger 4 (1092).
- brythons: the 900 Cumbria row (its ledger 24) now duplicates Strathclyde's gain; Cliopatria's Brythons shape still holds 18 Cumbrian cells in 1034.
- dal-riata has no 750 gain from Strathclyde; kingdom-of-england's 937 end for Strathclyde could take confidence 2 from the Aethelstan page.
- kingdom-of-dunoting: its Wikipedia title (Dunoding) is the Welsh realm.
