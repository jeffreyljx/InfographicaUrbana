# Review of batch eu-11-i (2026-10-25)

Reviewer of Norman England, Angevin Empire, Kingdom of the Isles (with Kingdom of Mann), Powys Fadog and Powys Wenwynwyn. All five validate (0 errors, 0 warnings, --resolve). The machine copy is history/notes/phase-b/reviews/eu-11-i.json.

Verdicts: angevin-empire **fail**, norman-england **fix**, kingdom-of-the-isles **thin**, kingdom-of-powys-fadog **fail**, kingdom-of-powys-wenwynwyn **thin**.

Main points:
- angevin-empire FAIL: /ledger/19 (Auvergne 1189, confidence 3) claims the page's year, but the Angevin Empire page leaves the recognition undated. Other faults: Gascony is drawn twice with duchy-of-aquitaine 1204-1209, the 1152 counterpart is wrong (kingdom-of-france holds the mirror), the Leinster gain of 1171 is in no keyframe, the Vexin is lost in 1151 and never regained though France annexes it in 1200, the capital Angers falls outside the shape, and the Brittany events do not match.
- powys-fadog FAIL: Cliopatria's Fadog shape is 4 cells: 2 in Flintshire (Tegeingl, Mold), 2 in the Corwen/Ruthin column, none in Wrexham (Maelor) or at Llangollen. Keyframes marked 'ok' claim the commotes fit, the capital Dinas Brân lies outside the drawn land, and Gwynedd claims the Tegeingl cells.
- norman-england fixed by the reviewer: Cumbria (Carlisle) split off as a 1136 loss, and the 1141-1144 Normandy contest retargeted to 'angevins'.
- isles and wenwynwyn THIN: the Norwegian overlordship (1098-1266) is missing, and Wenwynwyn's 1210 restoration, 1212 eviction and 1263 vassalage are missing (Gwynedd already holds the other side of each).

## angevin-empire: fail

Fixes:
- `/ledger/19` (author to do): 1189 loss of Auvergne at confidence 3 whose note says 'the year 1189 is the page's', but the page gives no year. Evidence: Angevin Empire page: 'Richard also recognised Auvergne as being in Philip's royal demesne and not as part of the Duchy of Aquitaine, as Henry had claimed.' No year in the sentence or near it; it only comes after the account of Richard's 1189 coronation. The same false quote with the year ('In 1189 Richard recognised Auvergne...') is in /keyframe_review/7/note. The Richard I page does not mention Auvergne. The recognition is usually dated to the Treaty of Louviers (December 1195 or January 1196), not 1189. Fix: Lower to confidence 1 and say the page does not date it, or find a page that dates the recognition (Treaty of Louviers) and move the year. Correct the quote in /keyframe_review/7/note and the Auvergne removal in keyframes _1192 and _1202 to match.
- `/keyframe_review/9` (author to do): Gascony is drawn as Angevin 1206-1209 (keyframe _1206 'ok' and the 1209 dissolve), but duchy-of-aquitaine draws the same Gascon core from 1204, so the land is drawn twice in 1204-1209. Evidence: duchy-of-aquitaine /ledger/10: 1204 gain from angevin-empire of 'the Gascon core of Aquitaine kept by John after 1204'; its keyframe duchy-of-aquitaine_1204 covers 1204-1258. Angevin keyframe _1202 (1202-1205) and _1206 (1206-1209) both include Gascony. Fix: Agree with eu-10 on one owner. Either add a 1204 loss (or merge) of Gascony to duchy-of-aquitaine and remove Gascony from the _1202 (from 1204) and _1206 corrections, or have duchy-of-aquitaine move its gain to 1210.
- `/ledger/3` (author to do): The 1152 gain of Aquitaine names duchy-of-aquitaine as counterpart, but that dossier holds no land in 1152. kingdom-of-france holds the mirror. Evidence: duchy-of-aquitaine /ledger/8-9: 1137 loss and vassal_end to kingdom-of-france, then nothing until 1204. kingdom-of-france /ledger/12: 1152 loss to angevin-empire, 'the same 585 cells of Aquitaine leave the shape'. The Angevin note itself says 'Cliopatria draws this land as Kingdom of France in 1139-1151'. Fix: Counterpart kingdom-of-france, keeping Eleanor's inheritance in the note; or have eu-10 give duchy-of-aquitaine a 1152 event.
- `/keyframe_review/4` (author to do): Keyframe _1169 (1169-1176) is 'ok', but the shape has no Irish cells, and /ledger/10 gains Leinster and Waterford in October 1171 at confidence 3. No keyframe draws Ireland before 1177. Evidence: shapes.csv angevin-empire_1169: modern_countries 'France;United Kingdom', bbox west edge -5.77. Ireland first appears in _1177. Fix: Add a keyframe angevin-empire_1171 (1171-1176) = the 1169 shape plus Leinster and Waterford, and end _1169 at 1170 (adjust).
- `/ledger/2` (author to do): The 1151 loss of the Norman Vexin is never reversed in the ledger, yet kingdom-of-france annexes the Norman Vexin from angevin-empire in 1200. The two ledgers contradict each other. Evidence: kingdom-of-france /ledger/15 (1200): 'Norman Vexin annexed; Evreux and Issoudun annexed', counterpart angevin-empire. The Richard I page says 'the Norman Vexin was lost to Philip during Richard's captivity' (1193). The Angevin ledger has no recovery of Gisors and the Vexin (1160, Margaret's dowry), no 1193 loss and no Évreux loss in 1200. Fix: Add the 1160 recovery of the Norman Vexin, its 1193 loss (Richard I page) and Évreux 1200 (Le Goulet), or explain why the Vexin stays French from 1151.
- `/identity/capitals/0` (author to do): Angers is the capital for 1144-1209, but it lies outside the dossier's land in 1144-1146 and after 1204. Evidence: Keyframe _1144 (1144-1146) is Normandy only, with Anjou in Cliopatria's 'Angevins' row. /ledger/25 loses Anjou in 1204, and the _1206 shape is England, Ireland and Gascony. Fix: Rouen for 1144-1146 (The Anarchy: 'Rouen, the capital of the duchy'), Angers (or Chinon) for 1147-1204, and an English seat (Westminster) for 1204-1209, or end the capital spans at the losses.
- `/wars/0` (author to do): The war 'Geoffrey of Anjou's conquest of Normandy' (1136-1144) lies before the dossier's start in 1144. Evidence: Section 2.2: wars must fall inside the state's life. The dossier itself names the 1136-1144 belligerent 'angevins', and norman-england carries the same war. Fix: Drop it here, or clip it to 1144 and leave the 1136-1143 phase to norman-england and the angevins dossier.
- `/ledger/8` (author to do): Brittany is a vassal 1166-1206 here, but duchy-of-brittany has an occupation 1166-1181 and three Angevin events that have no mirror here. Evidence: duchy-of-brittany /ledger/5 1158-09 loss of 'Nantes and its surrounding territories' to angevin-empire (confidence 3); /ledger/6 1164 loss of 'lands along the Brittany-Normandy border'; /ledger/7-8 occupation 1166-1181; /ledger/9 1185 gain of Nantes from angevin-empire (confidence 3). The Angevin ledger has no Nantes gain in 1158, no 1164 gain and no 1185 loss. Fix: Add the Nantes gain of 1158 (and the 1164 border lands) and the 1185 Nantes loss, and agree the relation type and dates (vassal or occupation, 1181 or 1206) with eu-10.

Thin (for a gap-filler):
- `/ledger/1`: 1147 merge of Anjou, Maine and Touraine (confidence 1, dated by the shape only). Geoffrey held Anjou from 1129 and Normandy from 1144. Try: https://en.wikipedia.org/wiki/Geoffrey_Plantagenet,_Count_of_Anjou
- `/ledger/26`: 1204 loss of Maine and Touraine (confidence 1); the John page names only Anjou and Poitou. Try: https://en.wikipedia.org/wiki/Philip_II_of_France
- `/ledger/27-28`: 1206 end of the Brittany relation and the 1206 loss of the rest of the continental lands (confidence 1, dated by the shape). Try: https://en.wikipedia.org/wiki/Philip_II_of_France
- `/ledger/29`: 1209 dissolve (confidence 1, Cliopatria's row end). The infobox events run to the Truce of Chinon (28 September 1214). Try: https://en.wikipedia.org/wiki/Battle_of_Bouvines
- `/keyframe_review/8`: The 1202 Irish cells (west Munster, Connacht) match no dated event. Try: https://en.wikipedia.org/wiki/Lordship_of_Ireland
- `/ledger (1160, 1193, 1200; missing)`: Norman Vexin recovered in 1160 and lost in 1193, Évreux lost in 1200 (see fixes /ledger/2). Try: https://en.wikipedia.org/wiki/Treaty_of_Le_Goulet

Spot checks:
- `/ledger/3` https://en.wikipedia.org/wiki/Angevin_Empire: confirmed ('Henry married Eleanor of Aquitaine in 1152, acquiring the Duchy of Aquitaine')
- `/ledger/7` https://en.wikipedia.org/wiki/Angevin_Empire: confirmed (1159 campaign: 'Henry did capture Cahors along with castles in the Garonne valley in the Quercy region')
- `/ledger/19` https://en.wikipedia.org/wiki/Angevin_Empire: not on page: the recognition of Auvergne is undated; the note's claim that 1189 is the page's year is false (confidence 3)
- `/ledger/25` https://en.wikipedia.org/wiki/John,_King_of_England: confirmed ('By August, Philip had taken Normandy and advanced south to occupy Anjou and Poitou as well')
- `/ledger/11` https://en.wikipedia.org/wiki/Angevin_Empire: confirmed ('In 1173 in Limoges, Raymond finally gave up ... He paid homage to Henry')
- `/ledger/17` https://en.wikipedia.org/wiki/Angevin_Empire: confirmed ('in 1183, Count Raymond had taken Cahors back')
- `/ledger/21` https://en.wikipedia.org/wiki/Angevin_Empire: confirmed ('the county was lost completely by the time of the accession of John in 1199')
- `/ledger/23` https://en.wikipedia.org/wiki/John,_King_of_England: confirmed (Normandy taken by August 1204)

Area: infobox None km2, Cliopatria 426192 km2, ratio None. The Angevin Empire infobox has no area or established/disestablished fields (checked). The author says so; the lead's 'roughly all of present-day England, half of France, and parts of Ireland and Wales' fits the 1202 shape.

## norman-england: fix

Fixes:
- `/ledger/15 (was /ledger/15, now /ledger/15-16)` (applied by reviewer): Cumbria (Carlisle) was dated with Northumbria to the 1139 Treaty of Durham, but the page has David keeping Carlisle under the first agreement after his invasion on Henry I's death (1135-1136). Evidence: The Anarchy page: David 'invaded the north on the news of Henry's death, taking Carlisle, Newcastle, and other key strongholds'; 'An agreement was made under which David would return most of the territory he had taken, with the exception of Carlisle.' The 1139 treaty is the next stage ('Northumbria and Cumbria would effectively be granted to David and his son Henry'). Fix: Split: new /ledger/15 is a 1136 loss of Cumbria to kingdom-of-alba (confidence 2, note quoting the page). /ledger/16 is now the 1139 loss of Northumberland only. Re-validated: 0 errors, 0 warnings, 22 events.
- `/ledger/17, /ledger/18, /wars/8` (applied by reviewer): The 1141 contest_start and January 1144 contest_end over Normandy named angevin-empire, which does not exist until January 1144. The Angevin dossier names this belligerent 'angevins'. Evidence: angevin-empire starts 1144-01. Its own /wars/0 has belligerents ['angevins', 'norman-england'] for 1136-1144. The 'angevins' Cliopatria row (1126-1146) is Geoffrey of Anjou's. Fix: Counterpart and war belligerent changed from angevin-empire to angevins. The 1144 loss to angevin-empire (/ledger/19) is unchanged. Re-validated with --resolve: 0 errors, 0 warnings.

Thin (for a gap-filler):
- `/ledger/2`: 1085 gain of 35 Welsh cells from kingdom-of-brycheiniog (confidence 1, the shape's year). The Brycheiniog dossier has its land falling to lordship-of-brecon in April 1093, not to this state in 1085. Try: https://en.wikipedia.org/wiki/Bernard_de_Neufmarch%C3%A9
- `/ledger/5, /ledger/9`: 1094-1099 occupation of north and mid Wales (confidence 1). Gwynedd mirrors it, but no page dates it. Try: https://en.wikipedia.org/wiki/Gruffudd_ap_Cynan
- `/ledger/3, /ledger/6, /ledger/10-13`: Normandy 1087-1106 has no owning dossier: duchy-of-normandy ends in 1071. The author lists it under counterparts_needing_dossiers. Try: https://en.wikipedia.org/wiki/Robert_Curthose

Spot checks:
- `/ledger/4` https://en.wikipedia.org/wiki/William_II_of_England: confirmed (1092: 'taking control of Cumberland and Westmorland, which had previously been claimed by the Scots')
- `/ledger/6` https://en.wikipedia.org/wiki/William_II_of_England: confirmed (1096: 'pledged his lands in Normandy to William in return for a payment of 10,000 marks')
- `/ledger/3` https://en.wikipedia.org/wiki/William_II_of_England: confirmed (1087: 'Robert inherited Normandy')
- `/ledger/10` https://en.wikipedia.org/wiki/William_II_of_England: confirmed ('Robert returned in September 1100')
- `/ledger/16 (old /ledger/15)` https://en.wikipedia.org/wiki/The_Anarchy: mis-dated for Cumbria (Carlisle held from the 1136 agreement), confirmed for Northumbria 1139; fixed by the reviewer
- `/ledger/17-19 (old 16-18)` https://en.wikipedia.org/wiki/The_Anarchy: confirmed ('Geoffrey took all the duchy south of the River Seine and east of the Risle', mid-1141; 'in January 1144 he advanced into Rouen')

Area: infobox None km2, Cliopatria 199096 km2, ratio None. The article (Norman Conquest) is an event page with no area. The author says so.

## kingdom-of-the-isles: thin

Thin (for a gap-filler):
- `/ledger (1098 and 1266; missing)`: Norwegian overlordship: the page says Magnus 'had re-established direct Norwegian overlordship by 1098' and the 1266 Treaty of Perth ended it. This ledger has no vassal_start (1098, old-kingdom-of-norway) or vassal_end (1266). The author leaves both to the eu-14 Norway dossier, but the mirror rule needs both sides. Try: https://en.wikipedia.org/wiki/Magnus_Barefoot
- `/ledger/1`: 1085 Hebrides gain from viking-settlements (confidence 1, the shape's year). Try: https://en.wikipedia.org/wiki/Godred_Crovan
- `/ledger/2-3`: Dublin 1094-1095 (confidence 1): Godred Crovan's kingship of Dublin and his ouster by Muirchertach Ua Briain are undated on the page. Try: https://en.wikipedia.org/wiki/Godred_Crovan
- `/ledger (1164-1266)`: No events between 1164 and 1266: the sons of Somerled, the 1249 Scottish campaign, Haakon's 1263 expedition and Largs. No rulers. Try: https://en.wikipedia.org/wiki/Treaty_of_Perth

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Kingdom_of_the_Isles: confirmed ('succeeded in taking the island from Fingal in 1079')
- `/ledger/4` https://en.wikipedia.org/wiki/Kingdom_of_the_Isles: confirmed (Battle of Epiphany 1156; the southern Inner Hebrides, Kintyre and the Clyde islands go to Somerled's sons)
- `/ledger/6` https://en.wikipedia.org/wiki/Kingdom_of_the_Isles: confirmed ('Somerled met his death in 1164'; Godred 're-took possession of his pre-1158 territories')
- `/ledger/7` https://en.wikipedia.org/wiki/Kingdom_of_the_Isles: confirmed ('1266 Treaty of Perth'; infobox 'Transferred to the Kingdom of Scotland: 1265', which the author notes)

Area: infobox 8374 km2, Cliopatria 6003 km2, ratio 0.72. No infobox area. The body gives the islands' land as about 8,374 km2, and the author quotes it. Cliopatria's shapes are 12,242 (1085), 14,607 (1094) and 6,003 (1169-1271) km2, all within a factor of two. The merge with kingdom-of-mann is accepted: shared Q459188, and kingdom-of-mann_1177 has the same area and bbox as kingdom-of-the-isles_1169.

## kingdom-of-powys-fadog: fail

Fixes:
- `/keyframe_review/1, /keyframe_review/2, /keyframe_review/3` (author to do): Keyframes _1169 and _1210 are 'ok' and _1216 reuses the shape, but Cliopatria's Fadog shape lies mostly outside the commotes the page names. Half its cells are Tegeingl (Mold), and none is in Maelor (Wrexham) or at Llangollen. The note's claim that the commotes 'fit the shape' is wrong. Evidence: gazetteer resolve of {cliopatria: Kingdom of Powys Fadog, 1169}: 4 cells, bbox -3.42..-3.10 W, 52.96..53.23 N. 2 cells are in admin1 Flintshire (bbox 53.11-53.23 N, Mold), 2 in Denbighshire (Corwen and Ruthin column), 0 in Wrexham. The 1210 shape has 5 cells, still 0 in Wrexham. Powys Fadog page: Maelor and Yale, later Nanheudwy, Cynllaith, Glyndyfrdwy and Mochnant Is Rhaeadr; Tegeingl is not among them. kingdom-of-gwynedd claims the Mold and Holywell cells for 1169-1210 and from 1212 and says 'the Powys Fadog dossier must give them up'. Fix: Mark all three keyframes adjust. Write a correction of the Fadog commotes: Wrexham county (Maelor, Yale, Chirk/Nanheudwy) plus the Llangollen, Corwen (Glyndyfrdwy) and Llansilin/Mochnant cells, minus Flintshire and minus the Ruthin (Dyffryn Clwyd) cell. Use the same region for the found and loss events.
- `/identity/capitals/0` (author to do): Castell Dinas Brân (52.977 N, 3.175 W) is outside every shape the dossier draws. Evidence: gazetteer: the intersect of an 8 km circle at the capital with the Fadog 1169 shape is 0 cells, and with the 1210 shape also 0 cells. Fix: Fixed when the keyframe corrections above include the Llangollen cell.

Thin (for a gap-filler):
- `/ledger (1277; missing)`: The page has Warwick's army entering northern Powys in early 1277, Dinas Brân taken on 10 May 1277, and the realm divided under the terms of surrender. There is no event (occupation or vassal_start to kingdom-of-england), and the capital span ends in 1277 without one. Try: https://en.wikipedia.org/wiki/Powys_Fadog
- `/keyframe_review/3`: The relation to Gwynedd 1216-1284 (alliance by 1215, 'forced into an alliance' in 1258) is undecided, and Cliopatria's Gwynedd 1216 shape contains all Fadog cells. The author flags it for the orchestrator. Try: https://en.wikipedia.org/wiki/Llywelyn_ap_Gruffudd
- `/keyframe_review/2`: The 1210 one-cell change is undated (small, page budget). Try: https://en.wikipedia.org/wiki/Madog_ap_Gruffydd_Maelor

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Powys_Fadog: confirmed ('Powys split in two in 1160 following the death of Prince Madog ap Maredudd')
- `/ledger/1` https://en.wikipedia.org/wiki/Powys_Fadog: confirmed ('became known as Powys Fadog after the accession in 1191 of his son prince Madog ap Gruffudd')
- `/ledger/2` https://en.wikipedia.org/wiki/Powys_Fadog: confirmed (Statute of Rhuddlan 1284: 'all of the remaining former princely titles and territories in Wales were abolished')
- `/ledger/3` https://en.wikipedia.org/wiki/Powys_Fadog: confirmed (infobox 1160 - 1284)

Area: infobox None km2, Cliopatria 1294 km2, ratio None. No area on the page (checked).

## kingdom-of-powys-wenwynwyn: thin

Thin (for a gap-filler):
- `/ledger (1210 gain and 1212 loss; missing)`: Both pages say Gwenwynwyn held land again between 1208 and 1215. Llywelyn page: 'John sent troops to help restore Gwenwynwyn to the rule of southern Powys' (in the 1210 narrative). Wenwynwyn page: 'In 1212 Gwenwynwyn's ancient royal seat at Mathrafal was destroyed and he was evicted from his territories.' The author treats 1208 and 1212 as a disagreement; they are two evictions. kingdom-of-gwynedd /ledger/35 has a 1210 loss to this state with no mirror here, and the capital Mathrafal runs to 1212 while the ledger has no land 1208-1214. Try: https://en.wikipedia.org/wiki/Gwenwynwyn_ab_Owain
- `/ledger (1263 vassal_start, 1274-1277 vassal_end; missing)`: The page has 'He transferred his allegiance back to Llywelyn ap Gruffudd in 1263 before returning to England's protection again after 1276'. kingdom-of-gwynedd /ledger/52 (vassal_start 1263-12) and /ledger/54 (vassal_end 1274) name this state; the author did not repeat them, but the mirror rule needs both sides. Try: https://en.wikipedia.org/wiki/Gruffydd_ap_Gwenwynwyn
- `/keyframe_review/4`: Keyframe 1241-1284 is constant, but Gruffudd was driven out by Llywelyn ap Gruffudd in 1257 and again in 1274, and restored in 1263 and 1277. kingdom-of-gwynedd /ledger/48 has a 1257 gain of the Powys lands. Neither date is on the Wenwynwyn page. Try: https://en.wikipedia.org/wiki/Gruffydd_ap_Gwenwynwyn
- `/ledger/5`: 1241 gain counterpart: the page credits the investiture to Henry III, and kingdom-of-gwynedd /ledger/44 loses 'all his lands outside Gwynedd' to kingdom-of-england in August 1241. Counterpart kingdom-of-england (or a note) needed. Try: https://en.wikipedia.org/wiki/Treaty_of_Gwerneigron

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Powys_Wenwynwyn: confirmed ('Gwenwynwyn seized the cantref of Arwystli in 1197')
- `/ledger/2` https://en.wikipedia.org/wiki/Llywelyn_the_Great: confirmed ('In 1208 ... summoned him to Shrewsbury in October and then arrested him'; 'Llywelyn took the opportunity to annex southern Powys')
- `/ledger/3` https://en.wikipedia.org/wiki/Powys_Wenwynwyn: confirmed ('restored to his realm in 1215, making a new capital at Welshpool')
- `/ledger/4` https://en.wikipedia.org/wiki/Powys_Wenwynwyn: confirmed ('In 1216 he was defeated in battle with the forces of Llywelyn')
- `/ledger/5` https://en.wikipedia.org/wiki/Powys_Wenwynwyn: confirmed (return in 1241 and investiture with Arwystli, Cyfeiliog, Mawddwy, Caereinion, Ystrad Marchell and Upper Mochnant)

Area: infobox None km2, Cliopatria 3122 km2, ratio None. No area on the page (checked). The shape resolves to 16 cells in the Severn and Dyfi valleys, with Mathrafal and Welshpool inside.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| angevin-empire 1144 found / norman-england | norman-england 1144 loss | matched | norman-england /ledger/19 (January 1144) |
| angevin-empire 1147 merge / angevins | - | exception | angevins (eu-10) has no dossier yet |
| angevin-empire 1151 loss / kingdom-of-france | kingdom-of-france 1200 gain | mismatch | France has no 1151 Vexin gain; it annexes the Norman Vexin from angevin-empire in 1200 (/ledger/15) |
| angevin-empire 1152 gain / duchy-of-aquitaine | kingdom-of-france 1152 loss | mismatch | duchy-of-aquitaine holds nothing 1137-1203; kingdom-of-france /ledger/12 is the mirror |
| angevin-empire 1154 gain / kingdom-of-france | - | missing | Vernon and Neuf-Marché: no France event |
| angevin-empire 1154 gain / norman-england | norman-england 1154 loss | matched | norman-england /ledger/20 |
| angevin-empire 1157 gain / kingdom-of-alba | - | exception | kingdom-of-alba (eu-11) not written yet |
| angevin-empire 1159 gain / county-of-toulouse | - | missing | county-of-toulouse has no event 1155-1195 (Quercy 1159, homage 1173, Cahors 1183, 1188) |
| angevin-empire 1166 vassal_start / duchy-of-brittany | duchy-of-brittany 1166 occupation_start | mismatch | type differs; Brittany's occupation ends in 1181, the Angevin vassal_end is 1206 |
| angevin-empire 1167 gain / kingdom-of-france | - | missing | Auvergne: no France event |
| angevin-empire 1171 gain / Kingdom of Leinster | - | exception | listed in counterparts_needing_dossiers (eu-11-x) |
| angevin-empire 1173 vassal_start / county-of-toulouse | - | missing | Toulouse side |
| angevin-empire 1174 vassal_start / kingdom-of-alba | - | exception | Alba not written yet |
| angevin-empire 1175 vassal_start / Ruaidri Ua Conchobair | - | exception | listed (kingdom-of-connacht, eu-11-x) |
| angevin-empire 1177 gain / Kingdom of Ulaid | - | exception | listed (eu-11-x) |
| angevin-empire 1177 gain / Kingdom of Desmond and Thomond | - | exception | listed (eu-11-x) |
| angevin-empire 1177 vassal_end / Ruaidri Ua Conchobair | - | exception | listed (eu-11-x) |
| angevin-empire 1183 loss / county-of-toulouse | - | missing | Toulouse side |
| angevin-empire 1188 vassal_end / county-of-toulouse | - | missing | Toulouse side |
| angevin-empire 1189 loss / kingdom-of-france | - | missing | Auvergne: no France event; the Angevin year itself is unsourced (see fixes) |
| angevin-empire 1189 vassal_end / kingdom-of-alba | - | exception | Alba not written yet |
| angevin-empire 1199 loss / kingdom-of-france | kingdom-of-france 1200 gain | matched | France /ledger/15 (Issoudun; Berry) |
| angevin-empire 1202 contest_start / kingdom-of-france | - | missing | no France contest events |
| angevin-empire 1204 loss / kingdom-of-france | kingdom-of-france 1204 gain | matched | France /ledger/16 (Normandy, Touraine, Anjou, Saintonge) |
| angevin-empire 1206 loss / kingdom-of-france | kingdom-of-france 1204 gain | mismatch | France takes the rest in 1204, the Angevin ledger in 1206 (confidence 1) |
| angevin-empire 1206 vassal_end / duchy-of-brittany | duchy-of-brittany 1181 occupation_end | mismatch | 25 years apart; type differs |
| duchy-of-brittany 1158 loss / angevin-empire | - | missing | Nantes (confidence 3): no Angevin gain |
| duchy-of-brittany 1164 loss / angevin-empire | - | missing | border lands: no Angevin gain |
| duchy-of-brittany 1185 gain / angevin-empire | - | missing | Nantes: no Angevin loss |
| duchy-of-aquitaine 1204 gain / angevin-empire | - | mismatch | Angevin keeps Gascony to its 1209 dissolve, so Gascony is drawn twice 1204-1209 |
| norman-england 1072 found / kingdom-of-england | - | exception | kingdom-of-england (eu-11) not written yet |
| norman-england 1072 gain / duchy-of-normandy | duchy-of-normandy 1071 dissolve | matched | Normandy 1071 dissolve, 'absorbed in the Anglo-Norman realm' |
| norman-england 1085 gain / kingdom-of-brycheiniog | kingdom-of-brycheiniog 1093 loss | mismatch | Brycheiniog loses its land to lordship-of-brecon in April 1093; the norman-england gain is confidence 1 |
| norman-england 1087 loss / duchy-of-normandy | - | exception | duchy-of-normandy ends 1071; Robert Curthose's duchy 1087-1106 listed in counterparts_needing_dossiers (eu-10). Same for 1096 and 1100 occupation and 1105-1106 contest and gain. |
| norman-england 1092 gain / kingdom-of-alba | - | exception | Alba not written yet |
| norman-england 1094 occupation_start / kingdom-of-gwynedd | kingdom-of-gwynedd 1094 occupation_start | matched | Gwynedd /ledger/25 |
| norman-england 1097 contest_start / county-of-maine | - | missing | county-of-maine has no 1097-1099 events |
| norman-england 1099 occupation_end / kingdom-of-gwynedd | kingdom-of-gwynedd 1099 occupation_end | matched | Gwynedd /ledger/26 |
| norman-england 1136 loss / kingdom-of-alba | - | exception | Cumbria; Alba not written yet (event split by the reviewer) |
| norman-england 1139 loss / kingdom-of-alba | - | exception | Northumbria; Alba not written yet |
| norman-england 1141 contest_start / angevins | - | exception | retargeted by the reviewer from angevin-empire; angevins (eu-10) not written yet |
| norman-england 1154 loss / angevin-empire | angevin-empire 1154 gain | matched | angevin-empire /ledger/5 |
| kingdom-of-the-isles 1085 gain / viking-settlements | - | exception | viking-settlements (eu-14) not written yet |
| kingdom-of-the-isles 1094 gain / Kingdom of Dublin | - | exception | not in the author's counterparts_needing_dossiers; the reviewer adds it |
| kingdom-of-the-isles 1095 loss / Muirchertach Ua Briain (Kingdom of Munster) | - | exception | the reviewer adds it to counterparts_needing_dossiers |
| kingdom-of-the-isles 1156 loss / Somerled | - | exception | listed (eu-11-x); also the 1158-1164 occupation |
| kingdom-of-the-isles 1266 loss / kingdom-of-alba | - | exception | Alba not written yet |
| kingdom-of-the-isles 1098 vassal_start (missing) / old-kingdom-of-norway | - | missing | missing on both sides; eu-14 not run |
| kingdom-of-powys-fadog 1160 found / kingdom-of-powys | kingdom-of-powys 1160 dissolve | matched | Powys /ledger/16 names Owain Cyfeiliog and Iorwerth Goch as heirs, not Gruffydd Maelor (Fadog page); eu-11 to reconcile |
| kingdom-of-powys-fadog 1284 loss / kingdom-of-england | - | exception | England not written yet |
| kingdom-of-gwynedd 1169 gain (Tegeingl cells) / kingdom-of-powys-fadog | - | mismatch | Gwynedd claims the Mold and Holywell cells 1169-1210 and from 1212; the Fadog keyframes keep them 1160-1284 (double claim) |
| kingdom-of-powys-wenwynwyn 1160 found / kingdom-of-powys | kingdom-of-powys 1160 dissolve | matched | Powys /ledger/16 |
| kingdom-of-powys-wenwynwyn 1197 gain / Arwystli (previous holder not named on the page) | - | exception | holder unnamed on the page |
| kingdom-of-powys-wenwynwyn 1208 loss / kingdom-of-gwynedd | kingdom-of-gwynedd 1208 gain | matched | Gwynedd /ledger/34 (1208-10) |
| kingdom-of-gwynedd 1210 loss / kingdom-of-powys-wenwynwyn | - | missing | no 1210 gain in Wenwynwyn (John's restoration, Llywelyn page) |
| kingdom-of-powys-wenwynwyn 1215 gain / kingdom-of-gwynedd | - | mismatch | Gwynedd returns the land in 1210 (/ledger/35), not 1215; no 1212 event on either side |
| kingdom-of-powys-wenwynwyn 1216 loss / kingdom-of-gwynedd | kingdom-of-gwynedd 1216 gain | matched | Gwynedd /ledger/41 |
| kingdom-of-powys-wenwynwyn 1241 gain / kingdom-of-gwynedd | kingdom-of-gwynedd 1241 loss | mismatch | Gwynedd /ledger/44 loses its outer lands to kingdom-of-england, not to this state |
| kingdom-of-gwynedd 1263 vassal_start / kingdom-of-powys-wenwynwyn | - | missing | no mirror in Wenwynwyn (page has 1263); also vassal_end 1274 |
| kingdom-of-powys-wenwynwyn 1284 loss / kingdom-of-england | - | exception | England not written yet |

## Counterparts needing dossiers (author's list plus two)

- Duchy of Normandy under Robert Curthose (and William II's pledge 1096-1100) (duchy-of-normandy, 1087-1106, eu-10 (extend or split from duchy-of-normandy, which ends 1071))
- Kingdom of the Isles / Argyll under Somerled and his sons (kingdom-of-argyll-and-the-isles-somerled, 1156-1164, eu-11-x)
- Kingdom of Leinster (kingdom-of-leinster, 1171-1171, eu-11-x)
- Kingdom of Ulaid (kingdom-of-ulaid, 1177-1177, eu-11-x)
- Kingdom of Desmond and Thomond (kingdom-of-desmond, 1177-1177, eu-11-x)
- Ruaidri Ua Conchobair's Kingdom of Connacht (kingdom-of-connacht, 1175-1177, eu-11-x)
- Lordship of Ireland (lordship-of-ireland, 1177-1209, eu-11-x)
- Kingdom of Alba (must carry Northumbria and Cumbria: gain 1139, loss 1157) (kingdom-of-alba, 1139-1157, existing Scotland dossier)
- Kingdom of Norway (vassal_start about 1098, vassal_end 1266 for the Isles) (kingdom-of-norway, 1098-1266, eu-14)
- Duchy of Brittany (own land 1188-1205 while a protectorate of the Angevins) (duchy-of-brittany, 1188-1205, eu-10-a)
- Kingdom of Gwynedd (must not double-claim Powys Fadog's cells 1216-1284) (kingdom-of-gwynedd, 1216-1284, existing Wales dossier)
- Lordship of Powis (Powys Wenwynwyn after 1284, to 1309) (lordship-of-powis, 1285-1309, gap-filler)
- Kingdom of Dublin (Norse-Gael, under Godred Crovan c.1091-1094 and after) (kingdom-of-dublin, 1094-1095, eu-11-x)
- Kingdom of Munster (Muirchertach Ua Briain) (kingdom-of-munster, 1095-1095, eu-11-x)

## Problems

- WebFetch answers come from a summarising model; quotes above are what it returned.
- Richard I of England page opened to date the Auvergne recognition: it does not mention Auvergne (Treaty of Louviers given as December 1195).
- kingdom-of-alba, kingdom-of-england, angevins, viking-settlements and old-kingdom-of-norway have no dossier yet: their mirrors count as exceptions.
- county-of-toulouse (eu-10) has no events 1155-1195 although Henry II took Quercy in 1159 and Raymond V did homage in 1173. Route to eu-10.
- Reviewer edits: only history/polities/norman-england.json (2 fixes, re-validated with --resolve, read back unchanged).
