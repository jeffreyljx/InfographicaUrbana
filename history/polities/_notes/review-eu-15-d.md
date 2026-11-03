# Review of batch eu-15-d (Duchy of Łęczyca, Duchy of Greater Poland, Duchy of Masovia), 2026-10-31

Reviewer: adversarial review per history/briefs/reviewer-brief.md with the orchestrator's adjustments (reviewer may apply small verified fixes; page budget judged for thin). Validator with --resolve: 0 errors, 0 warnings on all three before and after review.

Verdicts: duchy-of-eczyca **fix** (one note fix applied by the reviewer); duchy-of-greater-poland **fail**; duchy-of-masovia **fail**.

Method: ledgers read line by line; 10 pages opened (Salomea of Berg, Łęczyca Voivodeship, Mieszko III the Old, Casimir II the Just, Władysław Odonic, Bolesław the Pious, Duchy of Greater Poland, Konrad I of Masovia, Duchy of Masovia, Bolesław IV the Curly); keyframe/ledger overlaps measured with tools/grid.py polity_cells (H3 r5 cells). Every spot-checked event's year and claim was on its page; the failures are about what the dossiers leave out or draw twice, not invented events.

## duchy-of-eczyca: fix

Area: infobox 4080 km2 (1339), Cliopatria 8826 km2, ratio 2.16; acknowledged True. Infobox area is for the later voivodeship (established 1339 or 1352, no year on the figure); ratio acknowledged and argued in /keyframe_review/1/note.

### Findings

1. **/identity/predecessors/0/note** (applied by reviewer): The note credited a 'Duchy of Łęczyca page' with saying the duchy came 'out of the territory' set aside by the testament; no such page was a source, and the sentence on the cited Łęczyca Voivodeship page says the voivodeship was formed from the duchy's territory.
   - Evidence: Łęczyca Voivodeship page: the voivodeship was created out of the territory of the Duchy of Łęczyca, which 'had been established after the 1138 Testament of Bolesław III Wrymouth'.
   - Fix: Note rewritten to cite the Łęczyca Voivodeship page with that sentence; re-validated (0 errors, 0 warnings).

### Spot checks

- /ledger/0: confirmed: 'Bolesław III died on 28 October 1138'; 'Salomea received the town of Łęczyca, several castles and towns throughout Poland' (https://en.wikipedia.org/wiki/Salomea_of_Berg)
- /ledger/1: confirmed: 'Salomea died at her mansion in Łęczyca on 27 July 1144'; 'her province of Łęczyca reverted to the Senoriate' (https://en.wikipedia.org/wiki/Salomea_of_Berg)
- /ledger/2: confirmed (same sentences; no separate duchy after 1144 on the page) (https://en.wikipedia.org/wiki/Salomea_of_Berg)
- /identity/predecessors/0/note: mis-attributed page and sentence; fixed by reviewer (https://en.wikipedia.org/wiki/Łęczyca_Voivodeship)

## duchy-of-greater-poland: fail

Area: infobox None km2 (None), Cliopatria 34081 km2, ratio None; acknowledged True. The Duchy of Greater Poland page has no area figure (checked); the author says so in the notes.

### Findings

1. **/keyframe_review/16 and a missing ledger event between /ledger/20 and /ledger/21** (for the author): BLOCKING: no 1238/1239 loss; the 1236 shape (67-cell rump with Poznań and Gniezno) is kept as Greater Poland for 1236-1242 although both pages the author cites say the rump went to Silesia in 1239, and the author's gap entry calls the page silent.
   - Evidence: Duchy of Greater Poland page: 'When Henry I was succeeded by his son Henry II the Pious in 1238, ... Odonic was reduced to controlling only the area around Ujście. He died the following year, after which High Duke Henry II assumed control over all of Greater Poland.' Władysław Odonic page: 'In 1239, a new war broke out and once again, Władysław was defeated. This time, he lost the rest of Greater Poland, with the exception of Ujście and Nakło' (footnote: he kept Gniezno and Poznań until his death on 5 June 1239). duchy-of-silesia /ledger/19 has the 5 June 1239 gain from this duchy at confidence 3, so 1239-1242 is drawn twice. The 1243 gain ('regained most of the Duchies of Poznań and Gniezno') presupposes the loss.
   - Fix: Add a 1239/6 loss to duchy-of-silesia of the 1236 rump (c3, GP page sentence above); end keyframe 16 at 1238 and add a 1239-1242 keyframe (Ujście-Nakło only or empty, said in the note); make the 1241 contest and the 1243 gain cover Poznań and Gniezno (the 1243 region must include the rump); correct the report gap 'page silent'.
2. **/keyframe_review/2/correction, /ledger/1, /ledger/2 (1173-1177); /keyframe_review/14/correction, /ledger/16, /ledger/17 (1228-1229)** (for the author): The Seniorate region (Cliopatria Greater Poland 1177/1227 shape minus 1139 shape) contains all 29 cells of Cliopatria's Duchy of Kuyavia row, which the Masovia dossier in this batch draws as Leszek's in 1173-1176 (its keyframe 6) and Konrad's in 1227-1229 (its keyframe 14): in-batch double-draw.
   - Evidence: Grid count (tools/grid.py polity_cells): Greater Poland 1177 and 1227 shapes each hold 29 of the 29 Kuyavia 1205 cells. Bolesław IV page: succeeded 'in the Masovian-Kujavian principality by ... Leszek'; Konrad I page: 'in 1205, the adjacent lands of Kuyavia as well'.
   - Fix: Subtract {"cliopatria": "Duchy of Kuyavia", "year": 1188} from those corrections and event regions.
3. **/ledger/11 (and duchy-of-masovia /ledger/7)** (for the author): Kuyavia leaves Greater Poland in 1199 to duchy-of-masovia, but the Masovia dossier gains it only in 1205 from duchy-of-kuyavia: in-batch mismatch of six years and of counterpart.
   - Evidence: GP page: 'compelled to cede it to Duke Konrad of Masovia, son of Casimir II, in 1199'; Konrad I page: 'In 1199, he received Masovia and in 1205, the adjacent lands of Kuyavia as well'; Mieszko III page: 'compelled to cede Kuyavia to Casimir's sons' in 1198.
   - Fix: Agree one reading in both dossiers. Suggested: set this loss's counterpart to duchy-of-kuyavia (Cliopatria's row holds the land 1199-1205, mirrored by Masovia's 1205 gain) and keep the page disagreement in the note; or move Masovia's gain to 1199 (c2) and add Kuyavia to its keyframes 8-9.
4. **/ledger/25** (for the author): The 1249 gain of Wieluń (confidence 3) is never drawn and never lost: the Wieluń cell lies outside every Greater Poland keyframe from 1250 to 1304.
   - Evidence: Grid: the H3 cell at 51.22N 18.57E is in neither the Greater Poland 1250 nor the 1294 shape; no later Wieluń event in the ledger.
   - Fix: Union the Wieluń circle into keyframes 18-25 until a dated loss (page to find), or record the loss/hand-back with its year.
5. **/keyframe_review/18** (for the author): Keyframe 1244-1249 uses the 1250 shape, which already holds Santok, while /ledger/24 gains Santok in 1247.
   - Evidence: Grid: the Santok cell (52.74N 15.37E) is in the 1250 shape and not in the 1236 shape; Bolesław the Pious page: 'in 1244 Kalisz, in 1247 Santok, and in 1249 Wieluń'.
   - Fix: Split at 1247: 1244-1246 = the 1250 shape minus the Santok circle used in /ledger/24.
6. **ledger (missing events after /ledger/35); /keyframe_review/25** (for the author): No loss of Deutsch Krone (1296) or the Międzyrzecz castellany (1297) to Brandenburg; the margraviate-of-brandenburg dossier has both as gains from this duchy.
   - Evidence: margraviate-of-brandenburg /ledger/5 and /ledger/6, Margraviate of Brandenburg page: 'Brandenburg annexed the Międzyrzecz castellany from Greater Poland in 1297, and Deutsch Krone in 1296.' This dossier's own dissolve names Brandenburg (3 cells) among the successors.
   - Fix: Add the two losses (c2, that page added to sources) and subtract the Międzyrzecz cells (Brandenburg 1305 minus 1272 shape) from keyframe 25 for 1297-1304.
7. **/ledger/36** (for the author): 1300 recorded as a rename while kingdom-of-bohemia /ledger/8 gains Greater Poland from this duchy in 1300 (and /ledger/10 loses it back to it in 1306, after this dossier's end): Greater Poland is drawn by both 1300-1304.
   - Evidence: GP page: 'both Piasts were compelled to renounce their claims in favor of King Wenceslaus II of Bohemia'.
   - Fix: Agree with the Bohemia dossier: record 1300 as a loss to kingdom-of-bohemia (ending the drawn shape in 1300) or as a vassal_start, or have Bohemia drop its gain; route to the colour agent if both stand.

### Thin (for a gap-filler)

- /ledger/37: The 1304 dissolve is a map boundary at confidence 1; who held Greater Poland 1305-1314 (Henry III of Głogów, Łokietek) is not dated. Page to try: https://en.wikipedia.org/wiki/Władysław_I_the_Elbow-high
- /ledger/35: Pomerelia 1296: the page does not say who took it; Łokietek succeeded in Greater Poland in 1296 and may have kept Pomerelia, which would make this no loss at all. Page to try: https://en.wikipedia.org/wiki/Władysław_I_the_Elbow-high
- /ledger/24, /ledger/25: Previous holders of Santok (1247) and Wieluń (1249) ('unnamed holder (page silent)'), and when Wieluń left the duchy. Page to try: https://en.wikipedia.org/wiki/Przemysł_I_of_Greater_Poland

### Spot checks

- /ledger/1: confirmed: 'In 1173, after the death of his elder brother Bolesław IV the Curly, Mieszko became High Duke of Poland' (https://en.wikipedia.org/wiki/Mieszko_III_the_Old)
- /ledger/3: confirmed: 'in 1181, he was able to conquer the eastern Greater Polish lands of Gniezno and Kalisz' (https://en.wikipedia.org/wiki/Mieszko_III_the_Old)
- /ledger/4: confirmed: 'upon Leszek's death in 1186, he took the Kuyavia region' (https://en.wikipedia.org/wiki/Mieszko_III_the_Old)
- /ledger/9, /ledger/10: confirmed: 'In 1198, he was finally allowed to return to Lesser Poland'; 'In 1199 ... again deposed Mieszko'; infobox reigns 1198-1199 and 1202 ('three years later ... Mieszko was able to return') (https://en.wikipedia.org/wiki/Mieszko_III_the_Old)
- /ledger/2, /ledger/5, /ledger/6: confirmed: 1177 'Casimir assumed control of Kraków and thereby the seniorate'; 1191 Mieszko 'managed to take control over Wawel Castle'; infobox High Duke 1177-1191, 1191-1194 (https://en.wikipedia.org/wiki/Casimir_II_the_Just)
- /ledger/11, /ledger/29, /ledger/36: confirmed (1199 cession to Konrad; 1279 reunification; 1300 renunciation in favour of Wenceslaus II) (https://en.wikipedia.org/wiki/Duchy_of_Greater_Poland)
- /ledger/14, /ledger/15, /ledger/20: confirmed: Kalisz 'in 1207'; infobox Kalisz 1207-1217 (successor Spindleshanks); 22 September 1234 'relinquish all the territories south and west of the Warta River' (https://en.wikipedia.org/wiki/Władysław_Odonic)
- /ledger/22-/ledger/28: confirmed: 'By 1243 the brothers regained most of the Duchies of Poznań and Gniezno'; 'in 1244 Kalisz, in 1247 Santok, and in 1249 Wieluń'; 'In early 1265 Brandenburg occupied the main city of Santok'; Drezdenko 'captured by Brandenburg in 1270' (https://en.wikipedia.org/wiki/Bolesław_the_Pious)
- /keyframe_review/16: not on page: the page has Henry II take all of Greater Poland after Odonic's death (1239); the keyframe keeps the rump to 1242 (https://en.wikipedia.org/wiki/Duchy_of_Greater_Poland)

## duchy-of-masovia: fail

Area: infobox None km2 (None), Cliopatria 31448 km2, ratio None; acknowledged True. The Duchy of Masovia page has no area figure (checked); the author says so in the notes.

### Findings

1. **/ledger/8, /ledger/10, /keyframe_review/14, /keyframe_review/15** (for the author): BLOCKING: the 1229 gain and 1232 loss use the 1146 region 'Kraków and the Seniorate Province, Silesia and the Łęczyca land' (Masovia 1147 shape minus 1139 shape), giving Konrad I Silesia, which was Henry the Bearded's; and keyframes 14-15 do not draw the gain at all, so Kraków is drawn by no dossier of the batch in 1229-1231.
   - Evidence: Grid: the region holds 553 cells, 123 of them inside Cliopatria's Silesia 1169 shape. Konrad I page: he 'assumed the title of a Polish High Duke in 1229' and Henry I 'finally prevailed as High Duke at Kraków in 1232', no land named. Greater Poland keyframe 13 draws Greater Poland proper only for 1229-1233, Sandomierz lost Kraków in 1227, Silesia gains it in 1232.
   - Fix: Give both events the Kraków land ({"admin1": "Lesser Poland", "country": "Poland"}, as in the war zone, or the Greater Poland Seniorate region minus Kuyavia) and draw it in a 1229-1232 keyframe (split keyframe 14 at 1229); or, if the title carried no land, recast them as contest events and say so in the notes.
2. **/ledger/3** (for the author): The 1173 loss of the Seniorate to Greater Poland uses the same 1146 region, which includes Silesia, lost in 1163 (/ledger/2), and Kuyavia, which stays with Leszek (keyframe 6).
   - Evidence: Bolesław IV page: Silesia restored to Władysław's sons 'not before 1163'; Leszek succeeded 'in the Masovian-Kujavian principality'.
   - Fix: Use keyframe 5's correction minus keyframe 6's correction as the region.
3. **/ledger/12, /ledger/13** (for the author): Konrad's 1241-1243 hold on Kraków is only a contest here, while duchy-of-silesia /ledger/23 loses Kraków to this duchy on 10 July 1241 and duchy-of-sandomierz /ledger/21 gains it from this duchy on 25 May 1243 (Suchodoły).
   - Evidence: Konrad I page infobox: High Duke 1241-1243; Sandomierz dossier (Bolesław V page): 'On 10 July 1241 Konrad entered Kraków'; 'At the Battle of Suchodoły, Bolesław's forces defeated Konrad's Masovian troops, and Bolesław regained' Kraków.
   - Fix: Add a 1241/7 gain from duchy-of-silesia and a 1243/5 loss to duchy-of-sandomierz of the Kraków land (c2, Bolesław V page added to sources) with a 1241-1243 keyframe, or route the neighbours to a contest reading.
4. **/ledger/16, /keyframe_review/19-/keyframe_review/23** (for the author): The 1332 loss of the Dobrzyń Land to the Teutonic Order (c1) disagrees with teutonic-order /ledger/10 (gain from kingdom-of-poland) and with the cited Dobrzyń Land page, which gives the land to the Kuyavian Piasts from the second half of the 13th century; keyframes 1250-1332 still draw it as Masovian.
   - Evidence: Dobrzyń Land page as quoted by the author; teutonic-order /ledger/10.
   - Fix: Find when Dobrzyń left Masovia, drop its cells from the keyframes from that year with a loss event, and delete or re-counterpart the 1332 loss (flagged by the author; needs a page).
5. **/ledger/7 (and duchy-of-greater-poland /ledger/11)** (for the author): Kuyavia: this dossier gains it in 1205 from duchy-of-kuyavia, the Greater Poland dossier gives it to this duchy in 1199.
   - Evidence: Konrad I page (1205) versus Duchy of Greater Poland page (1199).
   - Fix: See the Greater Poland finding; both dossiers must carry the same reading.

### Thin (for a gap-filler)

- /ledger/15: 1326 Lithuanian strip at confidence 1: the page names no land. Page to try: https://en.wikipedia.org/wiki/Wenceslaus_of_P%C5%82ock
- /ledger/16: When the Dobrzyń Land passed to the Kuyavian line (confidence 1). Page to try: https://en.wikipedia.org/wiki/Casimir_I_of_Kuyavia
- ledger 1235-1239: The Radom district taken from Sandomierz in June 1235 and given up at Przedbórz on 9 July 1239 (duchy-of-sandomierz /ledger/17-18) has no mirror here; the author explains it lies outside the shape. Page to try: https://en.wikipedia.org/wiki/Boles%C5%82aw_V_the_Chaste
- /identity/rulers: Ruler strip ends in 1294 with gaps 1247-1248 and 1262-1264; 1294-1351 undated. Page to try: https://en.wikipedia.org/wiki/Boles%C5%82aw_II_of_Masovia
- /keyframe_review/19, /keyframe_review/21, /keyframe_review/22: 1250, 1279 and 1305 one-to-seven-cell changes unexplained (ok, unverified: page budget; not a fault). Page to try: https://en.wikipedia.org/wiki/Duchy_of_Masovia

### Spot checks

- /ledger/1, /ledger/2, /ledger/3: confirmed: 'The Duchy of Silesia and the Seniorate Province at Kraków were taken by Bolesław'; Silesia 1146-1163; 'Not before 1163 ... restored'; died 5 January 1173, succeeded by Mieszko III as High Duke and by Leszek in Masovia-Kuyavia (https://en.wikipedia.org/wiki/Boles%C5%82aw_IV_the_Curly)
- /ledger/4, /ledger/5: confirmed: 'In 1186, Duke Leszek of Masovia died'; 'Casimir could only take possession of Masovia proper'; 'Mieszko III occupied the lands of Kuyavia up to the Vistula River' (https://en.wikipedia.org/wiki/Casimir_II_the_Just)
- /ledger/6, /ledger/7, /ledger/8, /ledger/10: confirmed: 'In 1199, he received Masovia and in 1205, the adjacent lands of Kuyavia as well'; High Duke 1229; Henry I 'finally prevailed as High Duke at Kraków in 1232' (no land named for 1229) (https://en.wikipedia.org/wiki/Konrad_I_of_Masovia)
- /ledger/9, /ledger/11, /ledger/14, /ledger/17: confirmed: Chełmno Land 'to the knights in 1230'; 'In 1233 Konrad gave Kujawy to his second son Casimir I'; Czersk from 1262 (text: Konrad II 1264-1294 moved his residence); 'in 1351 he and his brother Casimir became vassals of the Polish kings' (https://en.wikipedia.org/wiki/Duchy_of_Masovia)

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| duchy-of-eczyca 1144 loss (duchy-of-silesia) | none | missing | Silesia dossier has no 1144 gain of the Łęczyca land; 1145-1146 is a 35-cell hole unless Silesia adds it (author flagged). |
| duchy-of-greater-poland 1173 gain (duchy-of-masovia) | duchy-of-masovia 1173 loss | matched | Regions disagree: Masovia's includes Silesia (lost 1163); both include Kuyavia, which Masovia keeps (see fixes). |
| duchy-of-greater-poland 1177 loss (duchy-of-sandomierz) | duchy-of-sandomierz 1177 gain | matched |  |
| duchy-of-greater-poland 1181 gain (duchy-of-sandomierz) | duchy-of-kalisz 1181 loss | mismatch | No Sandomierz loss of Gniezno/Kalisz in 1181/1182; duchy-of-kalisz /ledger/1 books the 1181 loss as its own. |
| duchy-of-greater-poland 1186 gain (duchy-of-masovia) | duchy-of-masovia 1186 loss | matched |  |
| duchy-of-greater-poland 1191 gain (duchy-of-sandomierz) | none | missing | Sandomierz has no 1191 loss of Kraków (Casimir II page: Mieszko took Wawel in 1191). |
| duchy-of-greater-poland 1191 loss (duchy-of-sandomierz) | none | missing | Sandomierz has no 1191 regain. |
| duchy-of-greater-poland 1198 gain (duchy-of-sandomierz) | duchy-of-sandomierz 1198 loss | matched |  |
| duchy-of-greater-poland 1199 loss (duchy-of-sandomierz) | duchy-of-sandomierz 1199 gain | matched | Sandomierz also has a 1199 loss of Kraków back to Greater Poland at c1, which the Mieszko III page does not support (return 'three years later', infobox 1202). |
| duchy-of-greater-poland 1199 loss (duchy-of-masovia) | duchy-of-masovia 1205 gain | mismatch | Masovia gains Kuyavia in 1205 from duchy-of-kuyavia; pages disagree (1198/1199/1205). In-batch fix required. |
| duchy-of-greater-poland 1202 gain (duchy-of-sandomierz) | duchy-of-sandomierz 1199 loss | mismatch | Sandomierz dates Mieszko's return 1199 (c1); Mieszko III page supports 1202. |
| duchy-of-greater-poland 1206 loss (duchy-of-sandomierz) | duchy-of-sandomierz 1206 gain | matched |  |
| duchy-of-greater-poland 1207 loss (duchy-of-kalisz) | duchy-of-kalisz 1207 gain | matched |  |
| duchy-of-greater-poland 1217 gain (duchy-of-kalisz) | duchy-of-kalisz 1229 loss | mismatch | Kalisz dossier keeps the duchy separate 1207-1229 (GP infobox division window); Odonic infobox gives Kalisz 1207-1217. |
| duchy-of-greater-poland 1228 gain (duchy-of-sandomierz) | duchy-of-sandomierz 1227 loss | matched | Sandomierz 1227/11 at c1. |
| duchy-of-greater-poland 1229 loss (duchy-of-masovia) | duchy-of-masovia 1229 gain | matched | Masovia's region includes Silesia; see Masovia fixes. |
| duchy-of-masovia 1232 loss (duchy-of-silesia) | duchy-of-silesia 1232 gain | mismatch | Silesia /ledger/13 gives the counterpart as duchy-of-greater-poland; both batch dossiers have Konrad holding the Seniorate 1229-1232. Silesia should re-counterpart to duchy-of-masovia. |
| duchy-of-greater-poland 1234 loss (duchy-of-silesia) | duchy-of-silesia 1234 gain | matched | duchy-of-kalisz /ledger/6 also books a 1234 gain from Greater Poland for the Kalisz cells. |
| duchy-of-silesia 1239 gain (duchy-of-greater-poland) | none | missing | No 1239 loss in Greater Poland; blocking finding on Greater Poland. |
| duchy-of-greater-poland 1243 gain (duchy-of-silesia) | duchy-of-silesia 1241 loss | mismatch | Silesia loses in 1241 (c1), Greater Poland regains by 1243 (contest from 1241). |
| duchy-of-greater-poland 1244 gain (duchy-of-silesia) | duchy-of-kalisz 1238 loss | mismatch | Silesia has no 1244 loss of Kalisz; the Kalisz dossier ends its 1234-1238 division in 1238 with a loss to Greater Poland. |
| duchy-of-greater-poland 1247 gain (unnamed holder (page silent)) | none | exception | Page names no previous holder of Santok. |
| duchy-of-greater-poland 1249 gain (unnamed holder (page silent)) | none | exception | Page names no previous holder of Wieluń; the gain is never drawn. |
| duchy-of-greater-poland 1265 loss (margraviate-of-brandenburg) | margraviate-of-brandenburg 1272 gain | mismatch | Brandenburg books the Santok-Drezdenko country only in 1272 at c1 (Cliopatria date); its own note cites Zantoch castellany 1270. |
| duchy-of-greater-poland 1270 loss (margraviate-of-brandenburg) | margraviate-of-brandenburg 1272 gain | mismatch | Same Brandenburg event; two years apart. |
| margraviate-of-brandenburg 1296 gain (duchy-of-greater-poland) | none | missing | Deutsch Krone: no loss in Greater Poland. |
| margraviate-of-brandenburg 1297 gain (duchy-of-greater-poland) | none | missing | Międzyrzecz castellany: no loss in Greater Poland. |
| duchy-of-greater-poland 1279 merge (Duchy of Kalisz and Gniezno (Bolesław the Pious)) | duchy-of-kalisz 1279 merge | matched | Kalisz dossier's other division windows (1191-1194, 1247-1250, 1253-1257, 1277-1279) have no mirror here: the Greater Poland dossier treats the appanages as internal; colour agent to decide. |
| duchy-of-greater-poland 1290 gain (grand-duchy-of-krakow) | duchy-of-silesia 1290 loss | mismatch | Silesia /ledger/31 books the bequest of Kraków as its own loss to Greater Poland; grand-duchy-of-krakow has no dossier yet (eu-15 part not run). |
| duchy-of-greater-poland 1290 loss (kingdom-of-bohemia) | kingdom-of-bohemia 1291 gain | mismatch | Bohemia gains Kraków from grand-duchy-of-krakow, not from Greater Poland. |
| duchy-of-greater-poland 1294 gain (Mestwin II (Duchy of Pomerelia)) | none | exception | Listed under counterparts_needing_dossiers (duchy-of-pomerelia). |
| duchy-of-greater-poland 1296 loss (duchies-of-poland) | none | exception | duchies-of-poland not written yet (eu-15 part not run). |
| kingdom-of-bohemia 1300 gain (duchy-of-greater-poland) | duchy-of-greater-poland 1300 rename | mismatch | Greater Poland keeps the land to 1304 as a rename; double-draw 1300-1304. |
| kingdom-of-bohemia 1306 loss (duchy-of-greater-poland) | none | mismatch | Greater Poland ends in 1304. |
| duchy-of-greater-poland 1304 dissolve (kingdom-of-poland) | none | exception | kingdom-of-poland not written yet (eu-15 part not run). |
| duchy-of-masovia 1146 gain (duchy-of-silesia) | duchy-of-silesia 1146 loss | matched |  |
| duchy-of-masovia 1163 loss (duchy-of-silesia) | duchy-of-silesia 1163 gain | matched |  |
| duchy-of-masovia 1186 loss (duchy-of-sandomierz) | duchy-of-sandomierz 1186 gain | matched |  |
| duchy-of-masovia 1199 gain (duchy-of-sandomierz) | duchy-of-sandomierz 1200 loss | matched | Sandomierz 'c. 1200' at c2. |
| duchy-of-masovia 1205 gain (duchy-of-kuyavia) | none | exception | duchy-of-kuyavia not written yet (eu-15 part not run); conflicts with Greater Poland 1199. |
| duchy-of-masovia 1230 loss (teutonic-order) | teutonic-order 1230 found | matched | Teutonic Order founded on the Chełmno Land, counterpart duchy-of-masovia. |
| duchy-of-masovia 1233 loss (Casimir I of Kuyavia) | none | exception | Listed under counterparts_needing_dossiers (duchy-of-kuyavia-casimir-i-line). |
| duchy-of-sandomierz 1235 loss (duchy-of-masovia) | none | missing | Radom district: no gain in Masovia (author explains: outside the Masovia shape). |
| duchy-of-sandomierz 1239 gain (duchy-of-masovia) | none | missing | Radom district given up at Przedbórz: no loss in Masovia. |
| duchy-of-silesia 1241 loss (duchy-of-masovia) | duchy-of-masovia 1241 contest_start | mismatch | Masovia has a contest, not a gain, of Kraków. |
| duchy-of-sandomierz 1243 gain (duchy-of-masovia) | duchy-of-masovia 1243 contest_end | mismatch | Masovia has a contest_end, not a loss. |
| mongol-empire 1241 keyframe ok (duchy-of-masovia) | duchy-of-masovia 1241 keyframe adjust | mismatch | Mongol keyframe 9 (1241 shape) is ok although its note says no European land west of the Rus' is a Mongol gain; Masovia restores the 11 Masovian cells: double-draw 1241-1249 (route to ia-02). |
| duchy-of-masovia 1326 loss (grand-duchy-of-lithuania) | none | exception | grand-duchy-of-lithuania not written yet (eu-15 part not run). |
| duchy-of-masovia 1332 loss (teutonic-order) | teutonic-order 1332 gain | mismatch | Teutonic Order takes Dobrzyń from kingdom-of-poland, not Masovia; the Dobrzyń Land page has it Kuyavian. |
| duchy-of-masovia 1351 dissolve (kingdom-of-poland) | none | exception | kingdom-of-poland not written yet (eu-15 part not run). |

## Problems

- No page failed to load. WebFetch returns summaries with quotes capped at 125 characters, so long sentences were checked in two passes.
- Neighbour dossiers not yet written (counted as the brief's exception): grand-duchy-of-lithuania, kievan-rus, duchy-of-g-ogow, duchies-of-poland, duchy-of-opole, principality-of-volhynia, kingdom-of-denmark, kingdom-of-poland, principality-of-halych, galicia-volhynia, duchy-of-legnica, duchy-of-wroc-aw, duchy-of-kuyavia, grand-duchy-of-krakow.
- Neighbour-side defects found (route to their owners): duchy-of-silesia lacks the 1144 Łęczyca gain and gives the 1232 Kraków counterpart as Greater Poland instead of Masovia; duchy-of-sandomierz's 1199 c1 return of Mieszko III is contradicted by the Mieszko III page (1202) and it lacks the 1181 and 1191 Kraków/Gniezno-Kalisz events; mongol-empire keyframe 9 keeps Masovian cells it says are not Mongol; margraviate-of-brandenburg dates the Santok-Drezdenko loss 1272 against the pages' 1265/1270; duchy-of-kalisz models Greater Polish appanages as a separate state on windows the Greater Poland dossier treats as internal.
