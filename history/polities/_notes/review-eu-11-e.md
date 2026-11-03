# Review of batch eu-11-e (Gwynedd, Gwent, Morgannwg)

Reviewer, 2026-10-25. Validator (`--resolve`): 0 errors in all three; Gwynedd has 4 warnings for the counterpart `marcher-lordships` (listed under counterparts needing dossiers). Pages opened (WebFetch): Kingdom of Gwynedd, Llywelyn the Great (twice), Dafydd ap Llywelyn, Llywelyn ap Gruffudd, Gruffydd ap Llywelyn, Kingdom of Gwent, Glywysing, Iestyn ap Gwrgant, Norman invasion of Wales. Every spot-checked event was on its page with its year; nothing fabricated. No dossier was edited.

## kingdom-of-gwynedd: fail (back to the author)
Confirmed: 855 Powys, 872 Seisyllwg, 878 division, 942/950 Hywel Dda, 1039, 1055, 1081, 1094-1100, 1208, 1241 (Aug), 1245 (Mar), 1247 (Apr), 1256 (Dec), 1259, 1260 (Jan), 1263 (12 Dec), 1274.
Blocking findings:
1. Southern Powys 1210-1215 (keyframes 23-24). Llywelyn the Great page: in 1210 "John sent troops to help restore Gwenwynwyn to the rule of southern Powys"; in 1216 Llywelyn "drove him out of southern Powys once more". The ledger has the 1208 gain but no 1210 loss and no 1216 gain, and the 1210-1215 shapes keep southern Powys. Add both events (counterpart kingdom-of-powys-wenwynwyn) and correct the 1210-1215 keyframes.
2. Owain Gwynedd's moves are missing (keyframes 21-22: 1099-1207 with no ledger events). Gwynedd page: Ceredigion 1136 (Llanfihangel, Aberystwyth, Llanbadarn) and 1137 (Ystrad Meurig, Lampeter); Mold in Tegeingl 1146; 1157 "resign Tegeingl and Rhuddlan to Chester"; "recovered Tegeingl for Gwynedd by 1169". The Powys Fadog reason in the notes covers only 1169-1215 and not Ceredigion. Add the events (the end of the Ceredigion hold needs a page: Owain Gwynedd), and say in the notes that the Powys Fadog dossier must give up the Tegeingl cells.
3. wars[8] (1157-1163): the outcome says the invasion failed and zones are empty, but the page has Owain cede Tegeingl and Rhuddlan in 1157.
Other fixes:
4. ledger[26]: the 1099 occupation_end returns the 1085 shape, but the 1099 shape (ok) is four cells smaller (Meirionnydd-Edeirnion) and no event removes them.
5. keyframe_review[30] and [31]: 1277-1283 drawn as the 1169 shape; the 1277 losses leave the 1085 shape (used for 1241-1255 too). Use the 1085 shape, or add a loss.
6. ledger[40], [48]: counterpart "Deheubarth (Dinefwr)" should be the slug `deheubarth` that the report asks for.
7. ledger[8]: 872 gain names kingdom-of-seisyllwg; the brythons dossier gives the same cells to Gwynedd in 875 (Cliopatria). Agree on the counterpart. Brythons should move to 872.
Thin: 705 (confidence 1), Brycheiniog 1055/1063 (confidence 1), the end of the Ceredigion hold, Perfeddwlad 1195-1211.
Area: no area on the page (author says so). The shapes are plausible.

## kingdom-of-gwent: thin
Confirmed: 926 Hereford (Wye border, Cantref Coch), 942 union, 1055, 1063, 1074. Capital Caerwent is inside the shapes.
Gaps: 577 and 705 Archenfield cell (confidence 1; the brythons ledger has no 577 loss to Gwent; try Ergyng). Unflagged: the Gwent infobox "Various unions with Glywysing: 6th century-c. 745" (also in the Glywysing infobox) is not mentioned anywhere; try Meurig ap Tewdrig. The 926 loss is of land outside the drawn shape and has no mirror in kingdom-of-wessex: keep it as a note, or Wessex adds the gain. The 931 submission to Athelstan belongs in the England dossier (not written yet).

## kingdom-of-morgannwg: thin
Confirmed: 942 union, 974 separation, 1063 restoration, 1086 Caerleon, c. 1090 Iestyn deposed. Capital Cardiff is inside the shapes.
Gaps: the Glywysing "Union with Gwent: 6th century-c. 745" is unflagged. Striguil (a Norman castle by 1071) lies inside the 1074-1085 shape, and the Gwent contest_end note says the fight "passes to Morgannwg", but there is no contest event here. Upland Glamorgan stayed Welsh after 1090 (Iestyn page: Caradog ap Iestyn between the Neath and the Afan) and has no successor.

## Cross-dossier mismatches to route
- brythons 875 loss to Gwynedd against Gwynedd 872 gain from kingdom-of-seisyllwg (counterpart and year).
- brythons 1066 gain from Gwynedd against Gwynedd 1063 loss: brythons should use 1063.
- brythons 1216 loss of 9 south-west cells to Gwynedd against Gwynedd 1215 gain from marcher-lordships (counterpart).
- brythons has no 577 loss to Gwent.
- kingdom-of-wessex has no 926 gain of Cantref Coch.
Matched: the Powys events 854/855, 878, 1039 and 1063; the Gwent-Morgannwg events 942, 975 and 1074; Gwynedd-Gwent-Morgannwg 1055 and 1063; brythons 1055/1056; the 540 splits.
