# Review of batch eu-19-a (Urartu, Kingdom of Armenia, Colchis)

Reviewed 2026-10-31. Validator (--resolve): 0 errors and 0 warnings for all three dossiers. Region and shape overlaps were measured with tools/gazetteer.py (cells of about 253 km2). Vassal relations are read as the schema says (the suzerain holds the tint), so no mirror is expected in the vassal's ledger.

Verdicts: kingdom-of-urartu fail (one keyframe-consistency defect), kingdom-of-armenia fail (three event regions inconsistent with keyframes), colchis thin (within its 1-2 page budget).

## kingdom-of-urartu: fail

### Findings (applied: none)
- **/keyframe_review/3/correction, /keyframe_review/4, /keyframe_review/5/correction** (blocking): The -700 bridge (correction = Cliopatria 615 shape) and the -615 (ok) and -600 (adjust, years only) keyframes put back the west bank of the Euphrates round Kummuh and Melid that the -750 correction removes, and no ledger event regains it.  
  Why: Gazetteer: intersect(Kingdom of Urartu -615, Commagene + Malatya 100 km) = 65 cells, about 16,438 km2; the -600 shape gives the same 16,438 km2, and so does the -750 shape that the author trimmed. The dossier's own -750 text says Kummuh/Melid is 'Assyrian-held after' 743 (Sarduri II page: Tiglath-pileser III forced the Urartians 'back across the Euphrates'); the kummuh dossier has the land under Assyria from 743 and Sargon II invading in 708. Reviewer rule 4: the change from the trimmed -750 keyframe to the -700 keyframe has no explaining event.  
  Fix: Give keyframe 3 the correction {"minus":[{"cliopatria":"Kingdom of Urartu","year":-615},{"union":[{"region":"Commagene"},{"place":"Malatya","km":100}]}]}. Change keyframe 4 (-615) from ok to adjust with the same minus. Give keyframe 5 (-600) the minus on its -600 shape, keeping the 'valid to -590' text. Alternatively, add a dated gain of Kummuh with a page. Without one, keep the trim.
- **/notes and history/polities/_notes/eu-19-a.md (Urartu section)** (non-blocking): The notes say that the Assyrian suzerainty of 645-635 and the Scythian conquest are 'neither ... on the pages opened here'. The Urartu page, which is in sources, has both.  
  Why: Urartu page: 'As a result, it became dependent on Assyria, as evidenced by Rusa II's son Sarduri III (645–635 BC) referring to the Assyrian king Ashurbanipal as his "father"', and 'Late during the 7th century BC (during or after Sarduri III's reign), Urartu was invaded by Scythians and their allies—the Medes.'  
  Fix: Correct the note and quote both sentences. Under the schema the suzerain holds the vassal tint (neo-assyrian-empire /ledger/48-49), so Urartu needs no vassal event. Record the Scythian-Median invasion as a war or contest at confidence 1 (the page gives no date), or say why it is left out, because scythia /ledger/5 has a gain of all Urartu in -635.

### Thin (for a gap-filler)
- /ledger/5: The -750 peak gain (Lake Urmia and Tabriz side, about 107,000 km2) is confidence 1, has no year on the page and has a string counterpart (Mannai and others). Page to try: https://en.wikipedia.org/wiki/Mannaeans
- /ledger/4: The year of Sarduri II's Melid and Kummuh conquest, which the page gives without a date ('conquering the northern region of Colchis, as well as Melid and Kummuh'). Page to try: https://en.wikipedia.org/wiki/Kummuh
- /keyframe_review/3: The 700-616 extent is bridged. The Cimmerian raids of 714 and the Scythian-Median invasion of the late 7th century are not placed on the map. Page to try: https://en.wikipedia.org/wiki/Rusa_II
- /ledger (Musasir, Diauehi, Qulha): The annexation of Musasir (c. 820-800), the vassalage of Diauehi under Menua and the northern Colchis (Qulha) conquest under Sarduri II are not mapped. Page to try: https://en.wikipedia.org/wiki/Musasir

### Spot checks
- /ledger/11 (https://en.wikipedia.org/wiki/Urartu): confirmed: 'The Medes then took over the Urartian capital of Van in 590 BC, effectively ending the sovereignty of Urartu'
- /ledger/2 (https://en.wikipedia.org/wiki/Urartu): confirmed: 'moved the capital to Tushpa'; infobox 'Tushpa (after 832 BC)'
- /ledger/6 (https://en.wikipedia.org/wiki/Sarduri_II): confirmed: 'In 743 BC, at a battle located somewhere in Kummuh, the Assyrians, under Tiglath-pileser III, defeated Sarduri'
- /ledger/3 (https://en.wikipedia.org/wiki/Argishti_I): confirmed: 'expanded his kingdom north to Lake Sevan, conquering much of Diauehi and the Ararat Valley'; 'founded the citadel of Erebuni in 782 BC'
- /ledger/9, /ledger/0, /ledger/1 (https://en.wikipedia.org/wiki/Urartu): confirmed (714 Sargon II and Rusa I at Lake Urmia, Musasir sacked; Arame c. 860-843; Sarduri I c. 832 new dynasty)

Area: infobox None (None), Cliopatria 161552, ratio 0.31, acknowledged True. The infobox has no area. The body's undated 520,000 km2 is acknowledged in keyframe 2 and resolved (the shape is kept).

## kingdom-of-armenia: fail

### Findings (applied: none)
- **/ledger/33/region** (blocking): The 299 gain paints all of the Atropatene region, although the page gives only 'up to the fortress of Zintha, in Media' and the note says the outline does not change.  
  Why: Gazetteer: Atropatene = 496 cells (about 125,400 km2), and minus(Atropatene, Kingdom of Armenia 287) = 316 cells (about 79,900 km2); the same 79,900 km2 lie outside the 306 shape. Keyframes 27 (287) and 28 (306) are 'ok', so about 80,000 km2 of Media turn Armenian in 299 and drop out in 306 with no loss event (reviewer rules 4 and 8). Narseh page: 'The semi-independent kingdom of Armenia was to be extended up to the fortress of Zintha, in Media.'  
  Fix: Set the region to {"intersect":[{"region":"Atropatene"},{"cliopatria":"Kingdom of Armenia","year":287}],"text":"...up to the fortress of Zintha, in Media"}, or to a place radius once Zintha is in the gazetteer. Keep confidence 2.
- **/ledger/9/region (and /keyframe_review/16, /keyframe_review/17)** (blocking): The -87 gain paints all of Atropatene, but the -87 keyframe (adjust, years only) and the -83 bridge keyframe hold only part of it.  
  Why: Gazetteer: minus(Atropatene, Kingdom of Armenia -87) = 322 cells, about 81,400 km2 (27% of the 300,627 km2 shape). The event is inside one shape span but is not small, and keyframe 16 is adjusted for its years, not for this land (reviewer rule 4).  
  Fix: Either intersect the event region with the -87 shape, or, if Tigranes held all of Media Atropatene ('retook Adiabene, Gordyene, and Media Atropatene'), give keyframes 16 and 17 a union with the Atropatene region. Be consistent with /ledger/33.
- **/ledger/8 and /keyframe_review/15** (blocking): The -95 gain of Sophene has no trace in the -91 keyframe, which is marked ok and lacks most of Sophene.  
  Why: Gazetteer: minus(Sophene, Kingdom of Armenia -91) = 75 cells, about 19,000 km2 of a 24,500 km2 region. Sophene would be Armenian in -95..-92 (by the event), not Armenian in -91..-88 (keyframe 15 ok) and Armenian again from -87, with no loss between. kingdom-of-sophene /ledger/3 dissolves to Armenia in -95.  
  Fix: Mark keyframe 15 (-91) adjust with {"union":[{"cliopatria":"Kingdom of Armenia","year":-91},{"region":"Sophene"}]}. Say in keyframe 14 that -95..-92 carries the event.
- **/keyframe_review/37, /keyframe_review/38** (non-blocking): The Principality of Armenia shapes of 638-646 (outside the kingdom's life) are 'adjust, shape unchanged'. The Marzpanate shape of 451, rejected for the same reason, is 'wrong'.  
  Why: Both notes say the land is not the Kingdom of Armenia. An adjust that keeps the shape reads as this state's land.  
  Fix: Use verdict 'wrong' for 638 and 644 as for 451, and keep the text that names the Principality as the owner.
- **/identity/rulers** (non-blocking): The ruler list has gaps where the pages name kings: -159..-95 (Artavasdes I, Tigranes I), 12..52, 186..217 and 287..298. Tiridates III is restored in 287 by /ledger/32 but listed from 298.  
  Why: Kingdom page: 'in 287, Tiridates III the Great was brought to power by the Roman armies'. Reviewer rule 9 asks for contiguous rulers.  
  Fix: Fill the gaps from the Artaxiad and Arsacid lists, or note them as interregna. Start Tiridates III in 287 (the infobox gives 298) or say why not.
- **/keyframe_review/18 (-77 shape, ok to -67)** (non-blocking): Syria stays Armenian to -67, but seleucid-empire /ledger/83 restores the rump kingdom in -69.  
  Why: seleucid-empire /ledger/83 (confidence 2) quotes 'Following the Roman general Lucullus' defeat of both Mithridates and Tigranes in 69 BC, a rump Seleucid kingdom was restored'. The Tigranes page is silent on Syria after 83 (checked).  
  Fix: Agree a year with me-05. If 69 stands, add a -69 loss of the Seleucid rump to seleucid-empire and mark keyframe 18 adjust from -69.

### Thin (for a gap-filler)
- /ledger/6: The -110 eastern loss (about 92,000 km2) is dated only by the Cliopatria change; the page dates the 'seventy valleys' cession c. 96/95, and parthian-empire has no -110 gain. Page to try: https://en.wikipedia.org/wiki/Mithridates_II_of_Parthia
- /ledger/14: The -77 step from about 389,000 to 519,631 km2 is confidence 1, with no named land or year. Page to try: https://en.wikipedia.org/wiki/Artaxiad_dynasty
- /ledger/19: The -63 western widening (west edge from 40.48 to 38.74 E, Sophene) is confidence 1, and roman-republic has no mirror. Pompey's disposal of Sophene and Gordyene is not on the pages opened. Page to try: https://en.wikipedia.org/wiki/Tigranes_the_Younger
- /ledger/38: The eastern strip dropped in 387 (Cliopatria east edge from 48.93 to 47.12 E) is confidence 1. Page to try: https://en.wikipedia.org/wiki/Peace_of_Acilisene
- /keyframe_review/1..9: The Orontid and early Artaxiad outlines (326-127) are unverified within the page budget. Page to try: https://en.wikipedia.org/wiki/Orontid_dynasty

### Spot checks
- /ledger/18 (https://en.wikipedia.org/wiki/Tigranes_the_Great): confirmed: 'In 66 BC, Pompey advanced into Armenia'; 'Pompey allowed him to retain his kingdom shorn of his conquests'; '6,000 talents'
- /ledger/26 (https://en.wikipedia.org/wiki/Roman_Armenia): confirmed: 'In 114, Emperor Trajan incorporated Armenia into the Empire, making it a full Roman province'
- /ledger/27 (https://en.wikipedia.org/wiki/Roman_Armenia): confirmed: 'In 118, Hadrian gave Armenia up, and installed Parthamaspates as its king'
- /ledger/31 (https://en.wikipedia.org/wiki/Kingdom_of_Armenia_(antiquity)): confirmed: 'The Sassanid Persians occupied Armenia in 252.'
- /ledger/39 (https://en.wikipedia.org/wiki/Marzpanate_period): confirmed: 'In 428, Armenian nobles petitioned Bahram V to depose Artaxias IV'; 'Bahram V abolished the Kingdom of Armenia and appointed Veh Mihr Shapur as marzban'
- /ledger/12 (https://en.wikipedia.org/wiki/Kingdom_of_Armenia_(antiquity)): confirmed: 'In 83 BC ... he entered Syria'; peak 'from 83 to 69 BC'; Tigranes page: Syrians 'offered him the crown of Syria' (83 BC)
- /ledger/33 (https://en.wikipedia.org/wiki/Narseh): confirmed text and year ('extended up to the fortress of Zintha, in Media'; '298/9 after the Peace of Nisibis (299)'); the region is overstated (see fixes)
- /ledger/1, /ledger/4, /ledger/9-11, /ledger/20 (https://en.wikipedia.org/wiki/Kingdom_of_Armenia_(antiquity)): confirmed (321 kingdom; Orontes IV overthrown 201/200; 'Between 88 and 85 BC, he retook Adiabene, Gordyene, and Media Atropatene' (Tigranes page); Antony 34 BC)

Area: infobox 900000 (-70), Cliopatria 519631, ratio 0.58, acknowledged True. Second infobox figure: 311,000 km2 c. 300 AD against 218,561 km2 (287 shape), ratio 0.70. Both are within a factor of two and noted in keyframes 18 and 27.

## colchis: thin

### Thin (for a gap-filler)
- /ledger/0: The birth in -301 is Cliopatria's year (confidence 1); the Colchis page is silent on 301-231 and dates the kingdom from the 6th century BC. Page to try: https://en.wikipedia.org/wiki/Kingdom_of_Iberia
- /ledger/1: The end in -110 is a bridge (confidence 1). The Pontus page gives no year. The Colchis infobox (as read by WebFetch) gives 'Conquest of Mithridates VI: After 70 BC', which the dossier does not mention and which conflicts with the body's 83 BC uprising. Page to try: https://en.wikipedia.org/wiki/Mithridates_VI_Eupator
- /keyframe_review/3: The 231 outline is carried to -111 (120 years) with no page for the extent. Page to try: https://en.wikipedia.org/wiki/Mithridates_VI_Eupator
- /keyframe_review/0: The shape reaches 44.96 E. Gazetteer: about 10,600 km2 of it lies in Shida Kartli, Mtskheta-Mtianeti, Kvemo Kartli, Tbilisi and Kakheti, the core of Iberia under Pharnavaz I. The author flagged this but left it unverified within the page budget. Page to try: https://en.wikipedia.org/wiki/Pharnavaz_I_of_Iberia

### Spot checks
- /ledger/1 (https://en.wikipedia.org/wiki/Kingdom_of_Pontus): confirmed as stated: 'inheriting Lesser Armenia from King Antipater (precise date unknown, c.115–106)' and 'conquering the Kingdom of Colchis', with no year; confidence 1 is honest
- /ledger/0 (https://en.wikipedia.org/wiki/Colchis): confirmed as stated: no statement on 301-231; Kuji '325–280 BC'; kingdom 'in the sixth century BC'
- /identity/capitals/0 (https://en.wikipedia.org/wiki/Colchis): confirmed: infobox 'Capital: Aea'

Area: infobox None (None), Cliopatria 44265, ratio None, acknowledged True. No area on the page.

## Cross-dossier matrix

| event | mirror | status | note |
|---|---|---|---|
| kingdom-of-urartu -782 gain (Diauehi) | diauehi - - | exception | No dossier; listed in counterparts_needing_dossiers (eu-19-x). |
| kingdom-of-urartu -750 vassal_start (kummuh) | kummuh -750 vassal_start | matched | kummuh /ledger/3. Under the schema only the suzerain records vassal events, and kummuh's mirror, which names urartu as counterpart, reads the other way round (me-04). |
| kingdom-of-urartu -750 gain (neighbouring states (Mannai and others)) | mannai - - | exception | String counterpart, confidence 1; Mannai listed in counterparts_needing_dossiers. |
| kingdom-of-urartu -743 vassal_end (kummuh) | kummuh -743 vassal_end | matched | kummuh /ledger/4. |
| kingdom-of-urartu -590 dissolve (median-kingdom) | median-kingdom - - | missing | median-kingdom (me-05) has no Urartu event; it should gain the Urartian lands in -590. |
| neo-assyrian-empire -645 vassal_start (kingdom-of-urartu) | kingdom-of-urartu - - | exception | The suzerain holds the tint (schema). The Urartu page confirms it ('it became dependent on Assyria ... Sarduri III (645–635 BC)'); the Urartu notes wrongly say the page lacks it. |
| scythia -635 gain (kingdom-of-urartu) | kingdom-of-urartu - - | mismatch | scythia gains all Urartu in -635 and loses it to the Medes in -600. Urartu keeps its -615 outline ('ok') to -590. The Urartu page has only an undated Scythian-Median invasion 'late during the 7th century'. The orchestrator should pick one reading. |
| kingdom-of-armenia -260 split (kingdom-of-sophene) | kingdom-of-sophene -256 found | mismatch | 4 years apart: the Orontid infobox gives 260; Cliopatria and the sophene dossier give 256. |
| kingdom-of-armenia -110 loss (parthian-empire) | parthian-empire - - | missing | parthian-empire has a -120 vassal_start and a -95 gain but no -110 gain; the Armenian event is a confidence-1 bridge. |
| kingdom-of-armenia -95 loss (parthian-empire) | parthian-empire -95 gain | matched | Arran lies wholly outside the -110 outline (0 cells), so the loss is a no-op on the Armenian side. |
| kingdom-of-armenia -95 gain (kingdom-of-sophene) | kingdom-of-sophene -95 dissolve | matched | kingdom-of-sophene /ledger/3. |
| kingdom-of-armenia -87 gain (atropatene) | atropatene - - | missing | atropatene (me-05) has no event between -147 and 6. parthian-empire /ledger/31 records the loss of Media Atropatene to Armenia, and /ledger/34 a vassal_end of atropatene. |
| kingdom-of-armenia -87 gain (kingdom-of-gordyene) | kingdom-of-gordyene -87 vassal_start | mismatch | Gain against vassal_start (me-06). Gordyene ends Armenian overlordship in -69; Armenia keeps the land to -67 and loses it in -66. |
| kingdom-of-armenia -87 gain (kingdom-of-adiabene) | kingdom-of-adiabene -87 vassal_start | mismatch | Gain against vassal_start; Adiabene's vassal_end is -66 (me-06). |
| kingdom-of-armenia -83 gain (seleucid-empire) | seleucid-empire -83 loss | matched | seleucid-empire /ledger/82. |
| seleucid-empire -69 gain (kingdom-of-armenia) | kingdom-of-armenia -66 loss | mismatch | The Seleucid rump is restored in -69 (seleucid-empire /ledger/83); Armenia keeps Syria to -67. |
| kingdom-of-armenia -77 gain (parthian-empire) | parthian-empire - - | missing | parthian-empire has no -77 loss (its loss is at -87); the Armenian event is a confidence-1 bridge. |
| kingdom-of-armenia -66 loss (roman-republic) | roman-republic -66 vassal_start | mismatch | Split counterparts: roman-republic gains Cilicia in -64 (/ledger/169) and takes Armenia as a client in -66; parthian-empire gains Mesopotamia in -66 (/ledger/36). No single mirror for the whole loss. |
| kingdom-of-armenia -63 gain (roman-republic) | roman-republic - - | missing | Confidence-1 bridge; roman-republic has no -63 loss of western Armenia/Sophene. |
| roman-republic -34 occupation_start (kingdom-of-armenia) | kingdom-of-armenia -34 contest_start | mismatch | Rome hatches Armenia as occupied -34..-32; Armenia records a contest that opens and closes in -34. |
| kingdom-of-armenia 114 loss (roman-empire) | roman-empire 114 gain | matched | roman-empire /ledger/68. |
| kingdom-of-armenia 118 gain (roman-empire) | roman-empire 117 loss | matched | Within one year (Roman Armenia page: 118). |
| kingdom-of-armenia 252 loss (sasanian-empire) | sasanian-empire 253 gain | matched | Within one year. |
| kingdom-of-armenia 287 gain (sasanian-empire) | sasanian-empire 299 loss | mismatch | 12 years apart: the Kingdom page gives 287; sasanian-empire (me-06) gives 299 (Peace of Nisibis). |
| kingdom-of-armenia 299 gain (sasanian-empire) | sasanian-empire 299 loss | mismatch | Same year but different land: the Sasanian loss is the whole Armenian outline, while the Armenian gain is Atropatene (overstated, see fixes). |
| sasanian-empire 363 contest_start (kingdom-of-armenia) | kingdom-of-armenia 368 contest_start | mismatch | 363 against 368 (start) and 371 against 370 (end). |
| sasanian-empire 379 gain (kingdom-of-armenia) | kingdom-of-armenia - - | missing | sasanian-empire /ledger/45 brings Greater Armenia back under Sasanian rule in 379-383; Armenia carries the 370 outline to 386 with no loss. |
| kingdom-of-armenia 387 loss (roman-empire) | roman-empire 387 vassal_start | mismatch | Armenia loses the western share to Rome; roman-empire records a vassal_start of Armenia instead. |
| kingdom-of-armenia 387 loss (sasanian-empire) | sasanian-empire 387 vassal_start | mismatch | Armenia's confidence-1 eastern strip is a loss; sasanian-empire records the rest of Armenia as a vassal from 387. |
| kingdom-of-armenia 428 dissolve (sasanian-empire) | sasanian-empire 428 gain | matched | sasanian-empire /ledger/52-53. |
| seleucid-empire/parthian-empire/roman-republic/roman-empire/sasanian-empire None vassal_start (kingdom-of-armenia) | kingdom-of-armenia - - | exception | Vassal tints over Armenia (-212..-188, -120..-87, -66..-32, 1..114, 161..163, 163..252, 299..363, 387..428) are held by the suzerains, as the schema says; no mirror is expected in Armenia. |
| colchis -110 dissolve (kingdom-of-pontus) | kingdom-of-pontus -110 gain | mismatch | kingdom-of-pontus /ledger/11 gains Colchis against 'nobody'; it should name colchis (me-05). |

## Routing and problems
- WebFetch answers come from a small model summarising each page. The Colchis infobox reading 'Conquest of Mithridates VI: After 70 BC' is unconfirmed.
- No fixes were applied: every finding is either a region or shape correction or a cross-dossier choice, which this run leaves to the author.
- Cross-dossier mismatches to route: median-kingdom (no -590 gain of Urartu), scythia against urartu (-635), atropatene (no -87 loss), sasanian-empire (287/299, 363/368, 379), roman-empire and sasanian-empire (387 vassal against loss), seleucid-empire (-69 rump), kingdom-of-pontus (counterpart nobody, should be colchis).
