# Review of batch eu-15-g (Kingdom of Bohemia, Duchy of Kalisz)

Reviewed 2026-10-31 by the adversarial reviewer. Validator: 0 errors for both dossiers; 19 gazetteer warnings for kingdom-of-bohemia (five region names the gazetteer lacks), none for duchy-of-kalisz. Neighbour dossiers read: duchy-of-bohemia, kingdom-of-hungary, house-of-habsburg, patriarchate-of-aquileia, margraviate-of-brandenburg, electorate-of-brandenburg, margraviate-of-moravia, habsburg-monarchy, duchy-of-greater-poland, duchy-of-silesia, duchy-of-sandomierz, duchy-of-bytom, duchy-of-raciborz, holy-roman-empire, holy-roman-empire-minor-states, plus duchy-of-carinthia, duchy-of-styria, electoral-palatinate and teutonic-order (not in the Context table but named by the events). Not yet written (groups not run): kingdom-of-poland, duchy-of-opole, duchy-of-g-ogow, duchy-of-jawor, duchy-of-legnica, duchies-of-poland, galicia-volhynia, grand-duchy-of-krakow, duchy-of-wroc-aw, hussite-bohemia.

## kingdom-of-bohemia: fail

Strong keyframe work (all 33 Cliopatria shapes reviewed, four new keyframes, the Slovakia, early Silesia, early Lower Lusatia, Brandenburg and 1468-1491 errors caught) and every dated event I opened is on its page. It fails on one confidence-3 event that moves the wrong land (1335) and several ledger inconsistencies with its own events and its neighbours; most fixes are small. The reviewer applied five counterpart-slug fixes (marked applied below).

### Findings

- `/ledger/19` (for the author): The 24 August 1335 Treaty of Trentschin is recorded as a confidence-3 gain of the whole of Silesia from the Kingdom of Poland, but no land changed hands. Evidence: Treaty of Trentschin page: Casimir's representatives 'renounced all claims to Silesia in favour of Bohemia'; the Silesian duchies were already John's vassals (1327, 1329; /ledger/14, /ledger/16) and stay vassal tint until 1348 in this dossier's own keyframes 15-16, and the same page dates Jawor (Świdnica-Jawor) to Bohemia only in 1392 (/ledger/32). As written the event draws all Silesia as direct Bohemian land from 1335, including Świdnica-Jawor, and demands a phantom 1335 loss of Silesia in the kingdom-of-poland dossier. Fix: Remove the gain (keep the treaty and its quotes in the war 'Bohemian-Polish dispute over Silesia' and in certainty notes), or, if a page dates it, replace it with a gain of the Duchy of Wrocław only, on Henry VI's death in 1335 (counterpart the Wrocław duchy, not Poland).
- `/ledger/13` (for the author): The Egerland is gained twice (1266 and 1322) with no loss in between. Evidence: /ledger/6 quotes the Kingdom page: 'All of Ottokar's German possessions were lost in 1276'; the Egerland page has Cheb 'a free imperial city since 1277'; the Kingdom and Lands pages say it was 'obtained by King Wenceslaus II between 1291 and 1305' and 'definitely given in pawn to Bohemia by King Louis IV in 1322'. Fix: Add the Egerland to the 1276 loss (or a separate 1276/1277 loss, counterpart holy-roman-empire-minor-states), then either a confidence-1 regain under Wenceslaus II (1291-1305) or keep only the 1322 gain; the 1279-1321 keyframes then need a correction for the Egerland.
- `/ledger/34` (for the author): The 1402 pawn of the Neumark to the Teutonic Order is a loss in Bohemia's ledger, duplicating the vassal's own loss. Evidence: Brandenburg is vassal tint here (/ledger/30, keyframe 20 correction removes it from direct land), so Bohemia holds no Neumark to lose; margraviate-of-brandenburg /ledger/30 already has '1402 loss teutonic-order' (c3) and teutonic-order /ledger/18 gains it from margraviate-of-brandenburg. Fix: Delete /ledger/34 (mention the pawn in the note of /ledger/35 or of keyframe 21).
- `/ledger/10` (for the author): The 1306 loss of Greater Poland and Kuyavia names duchy-of-greater-poland, whose dossier ends in 1304. Evidence: duchy-of-greater-poland identity: end 1304, successors kingdom-of-poland, duchy-of-g-ogow, margraviate-of-brandenburg. Fix: Name the 1306 holder (Henry III of Głogów for Greater Poland: duchy-of-g-ogow; Władysław the Elbow-high for Kuyavia) from a page (Henry III of Głogów, Władysław I Łokietek), keeping confidence 1 if no page dates it.
- `/keyframe_review/13/correction` (for the author): The 1305-1313 correction drops the Kraków lands and Greater Poland/Kuyavia from 1305, but the ledger loses them only in 1306. Evidence: /ledger/9 and /ledger/10 date the losses to 1306; keyframe 12's correction adds Greater Poland and Kuyavia 1300-1306 but keyframe 13 does not carry them (or Lesser Poland) into 1305-1306. Fix: Add a union of Lesser Poland, Greater Poland and Kuyavia to the 1305 correction with text 'until 1306', or move the losses to 1305 if a page supports it.
- `/ledger/6` (for the author): The 1276 loss gives Friuli to the House of Habsburg. Evidence: Ottokar II page: he 'gave up all claims to Austria and the neighboring duchies'; Friuli was the Patriarchate's land (the dossier gains it from patriarchate-of-aquileia in /ledger/5), not a Habsburg duchy. Fix: Split Friuli out into a separate 1276 loss with counterpart patriarchate-of-aquileia (confidence 2).
- `/ledger (missing, 1445)` (for the author): No loss of Cottbus to Brandenburg in 1445. Evidence: electorate-of-brandenburg /ledger/2: '1445: Brandenburg acquires Cottbus from Bohemia. In 1445 Cottbus was acquired by the Margraviate of Brandenburg from Bohemia' (c3). Fix: Add '1445 loss electorate-of-brandenburg', region {"place": "Cottbus", "km": 20}, citing the page that electorate dossier cites.
- `/ledger/3` (applied by reviewer): Counterpart holy-roman-empire for a 1266 event; that dossier ends in 1259. Evidence: holy-roman-empire identity end 1259, successor holy-roman-empire-minor-states. Fix: counterpart 'holy-roman-empire-minor-states' (done by the reviewer, note appended).
- `/ledger/13` (applied by reviewer): Counterpart holy-roman-empire for a 1322 event; that dossier ends in 1259. Evidence: holy-roman-empire identity end 1259, successor holy-roman-empire-minor-states. Fix: counterpart 'holy-roman-empire-minor-states' (done by the reviewer, note appended).
- `/ledger/4` (applied by reviewer): Counterpart holy-roman-empire for the 1269 Carinthia/Carniola inheritance; the page names the duke of Carinthia and the HRE dossier ends in 1259. Evidence: Ottokar II page: 'In 1268 he signed an inheritance treaty with the Sponheim duke Ulrich III of Carinthia' and succeeded 'him in Carinthia, Carniola and the Windic March the next year'; duchy-of-carinthia exists (976-1335). Fix: counterpart 'duchy-of-carinthia' (done by the reviewer, note appended).
- `/ledger/17` (applied by reviewer): Free-form counterpart 'Görlitz lords (previous holder not named on the pages)' for the 1329 Görlitz gain. Evidence: Upper Lusatia page: 'In 1329 Duke Henry I of Jawor had to cede Görlitz to the Bohemian king, but retained the remaining towns.'; margraviate-of-brandenburg /ledger/18 gives eastern Upper Lusatia to duchy-of-jawor in 1319. Fix: counterpart 'duchy-of-jawor' (done by the reviewer, page quoted in the note).
- `/ledger/33` (applied by reviewer): Free-form counterpart for the 1401 loss of the Upper Palatinate although electoral-palatinate has a dossier. Evidence: Lands of the Bohemian Crown page: 'Charles' son Wenceslaus lost the area in 1401 to the Electoral Palatinate under King Ruprecht of Germany.'; history/polities/electoral-palatinate.json exists (1085-1777). Fix: counterpart 'electoral-palatinate' (done by the reviewer). The author should also decide /ledger/28 (1355), still a free string, and drop electoral-palatinate from counterparts_needing_dossiers.

### Gaps for a gap-filler

- `/ledger/36`: End of the Moravian vassal tint dated 1415 at confidence 1 as a bridge to Cliopatria; the Jobst page gives his reign '12 November 1375 – 18 January 1411', successor Sigismund. Find when Moravia returned to the king (1411 or later). Try: https://en.wikipedia.org/wiki/List_of_rulers_of_Moravia
- `/ledger/31`: Moravia was a separate margraviate fief under John Henry from 1349, not first from Jobst in 1375; the margraviate-of-moravia dossier (1182-1918) has no vassal relation to Bohemia at all. Try: https://en.wikipedia.org/wiki/John_Henry,_Margrave_of_Moravia
- `/keyframe_review/1-6`: Upper Lusatia (Budissin Land) was Bohemian from 1158/1160 to 1253-1262 (Upper Lusatia page: 'the investiture with Ortenburg Castle and Land Budissin'; 'Between the death of King Wenceslaus I of Bohemia in 1253 and 1262, the Ascanian margraves of Brandenburg attained Budissin Land'); not in the shapes or the ledger, and margraviate-of-brandenburg /ledger/2 gains it from Bohemia (1262, c1). Try: https://en.wikipedia.org/wiki/Upper_Lusatia
- `/ledger (1252-1254)`: Bohemian holding of (part of) Styria before 1254: the Ottokar page says 'Ottokar would yield large parts of Styria to Béla' (undated) and 'Béla now ceded Styria back to Ottokar' (1260); kingdom-of-hungary /ledger/38 gains Styria from Bohemia on 1 May 1254. Try: https://en.wikipedia.org/wiki/Peace_of_Buda_(1254)
- `/ledger (1290)`: Kłodzko Land returning to Bohemia in 1290 (duchy-of-silesia /ledger/29 loses it to Bohemia, c2). Try: https://en.wikipedia.org/wiki/Kłodzko_Land
- `/ledger/10`: Loss of Greater Poland and Kuyavia in 1306 is confidence 1 (page silent). Try: https://en.wikipedia.org/wiki/Henry_III_of_Głogów
- `/keyframe_review/12`: Homage of the Upper Silesian dukes to Wenceslaus II (c. 1289-1292); the Wenceslaus II page is silent. Try: https://en.wikipedia.org/wiki/Duchy_of_Bytom

### Spot checks

- `/ledger/1` https://en.wikipedia.org/wiki/Ottokar_II_of_Bohemia: confirmed: 'The same year Ottokar entered Austria, where the estates acclaimed him as Duke' (1251)
- `/ledger/2` https://en.wikipedia.org/wiki/Ottokar_II_of_Bohemia: confirmed: Kressenbrunn July 1260, 'Béla now ceded Styria back to Ottokar'
- `/ledger/4` https://en.wikipedia.org/wiki/Ottokar_II_of_Bohemia: confirmed: 1268 treaty, Carinthia, Carniola and the Windic March 'the next year'
- `/ledger/5` https://en.wikipedia.org/wiki/Ottokar_II_of_Bohemia: confirmed: 'In 1272 he also acquired Friuli' (c2, previous holder not named)
- `/ledger/6` https://en.wikipedia.org/wiki/Ottokar_II_of_Bohemia: confirmed: November 1276 treaty, 'retaining for himself only Bohemia and Moravia'
- `/ledger/7` https://en.wikipedia.org/wiki/Wenceslaus_II_of_Bohemia: confirmed: 'In 1291, High Duke Przemysł II of Poland ceded the sovereign Duchy of Kraków to Wenceslaus.'
- `/ledger/12` https://en.wikipedia.org/wiki/Kingdom_of_Bohemia: confirmed: Upper Lusatia 'incorporated by ... King John of Bohemia in 1319' and '1329 (Görlitz)'
- `/ledger/14,16,18,20,21,32` https://en.wikipedia.org/wiki/Treaty_of_Trentschin: confirmed: 1327 Wrocław and Opole, 1329 five duchies, 1331 Głogów annexed, Ziębice 1336, Nysa 1342, Jawor 1392
- `/ledger/19` https://en.wikipedia.org/wiki/Treaty_of_Trentschin: date confirmed (24 August 1335), but the page describes a renunciation of claims, not a land transfer: see fixes
- `/ledger/28,29,33` https://en.wikipedia.org/wiki/Lands_of_the_Bohemian_Crown: confirmed: Upper Palatinate 1355 and lost 1401 to the Electoral Palatinate; Lower Lusatia 1367
- `/ledger/30,34,35` https://en.wikipedia.org/wiki/Margraviate_of_Brandenburg: confirmed: 'attached (but did not incorporate) Brandenburg to the Crown of Bohemia'; Neumark pawned to the Teutonic Knights (1402); 'granted hereditary control over Brandenburg in 1411'
- `/ledger/41,42` https://en.wikipedia.org/wiki/Matthias_Corvinus: confirmed: 'They solemnly ratified the peace treaty at their meeting in Olomouc on 21 July 1478'; the Kingdom page says 1479 (disagreement flagged by the author)
- `/ledger/43` https://en.wikipedia.org/wiki/Lands_of_the_Bohemian_Crown: confirmed: 'Upon the death of King Matthias in 1490, Vladislas ruled the Bohemian crown lands.'
- `/ledger/36` https://en.wikipedia.org/wiki/Jobst_of_Moravia: mis-dated at confidence 1: Jobst's reign ends 18 January 1411 (successor Sigismund); the 1415 year is a bridge to Cliopatria, listed under thin

Area: The Kingdom of Bohemia infobox gives no area (confirmed); the author says so in notes. Cliopatria 1502-1525 shape quoted for reference.

## duchy-of-kalisz: thin

Thin by design (two Cliopatria shapes, page budget 1-2, both pages used). Events follow the Greater Poland infobox windows and are on the pages; borders are placeholders. The 1234-1238 window and the 1229 date conflict with the Greater Poland and Silesia dossiers and need reconciling.

### Findings

- `/ledger/6` (for the author): The 1234 gain (and keyframe 6, 1234-1238) gives Kalisz back to an independent duchy, but in 1234 Kalisz went to Henry the Bearded of Silesia. Evidence: duchy-of-greater-poland /ledger/20 (c3): Odonic 'had to relinquish all the territories south and west of the Warta River, which included Kalisz' to Henry (22 September 1234); duchy-of-silesia /ledger/14 gains it; GP /ledger/23 regains Kalisz only in 1244. The author's own keyframe 6 note quotes the GP page on Henry conquering 'most of Odonic's lands from 1234 onward'. Fix: Either drop the 1234-1238 window (Kalisz is Silesian land 1234-1244) or keep it with counterpart duchy-of-silesia and a page that names a duke of Kalisz in those years; reconcile with the GP and Silesia dossiers.
- `/ledger/5` (for the author): The 1229 end of Odonic's Kalisz (confidence 3 from an infobox range) disagrees with the Greater Poland dossier's 1217 return of Kalisz. Evidence: GP page infobox: 'Internally divided into Poznań, Gniezno and Kalisz: ... 1207–1229 ...' (no sentence); duchy-of-greater-poland /ledger/15 cites Odonic's infobox 'Duke of Kalisz 1207-1217'. Fix: Open the Władysław Odonic page and date the loss (1217 or 1229); lower to confidence 2 if only the infobox range supports it.

### Gaps for a gap-filler

- `/keyframe_review/0-9`: Every keyframe uses the Cliopatria 1210 outline (2,819 km2) as a placeholder; no page gives the duchy's borders. Thin by design (budget 1-2 pages). Try: https://en.wikipedia.org/wiki/Kalisz_Land
- `/identity/rulers`: No ruler strip: dukes between Casimir II (1177-1181) and Przemysł II (1273-1279) (Mieszko the Younger 1191-1193, Odon 1193-1194, Władysław Odonic 1207-1217, Bolesław the Pious). Try: https://en.wikipedia.org/wiki/Władysław_Odonic
- `/ledger/1-12`: The lose-all/regain-all windows follow the GP infobox; the GP dossier has mirrors only for 1207 (and 1181 with another counterpart). A gap-filler should reconcile the windows with duchy-of-greater-poland (1191, 1194, 1238/1244, 1247, 1250, 1253, 1257, 1277). Try: https://en.wikipedia.org/wiki/Bolesław_the_Pious

### Spot checks

- `/ledger/0` https://en.wikipedia.org/wiki/Duchy_of_Kalisz: confirmed: 'The duchy was established in 1177, following the partition of the Duchy of Greater Poland'
- `/ledger/1` https://en.wikipedia.org/wiki/Duchy_of_Greater_Poland: confirmed: infobox 'Acquired Kalisz and Gniezno: 1181'; body: Mieszko III 'successfully seized the adjacent territories of Gniezno and Kalisz' in 1181
- `/ledger/2,3` https://en.wikipedia.org/wiki/Duchy_of_Greater_Poland: confirmed: infobox window 1191–1194; Mieszko the Younger installed as Duke of Kalisz (1191); Odon held Kalisz 1193–94
- `/ledger/10` https://en.wikipedia.org/wiki/Duchy_of_Greater_Poland: confirmed: 'Bolesław was reinstated as Duke of Kalisz and Gniezno' (1253)
- `/ledger/13` https://en.wikipedia.org/wiki/Duchy_of_Kalisz: confirmed: 'It existed in this form until 1279, when it was united with the duchies of Gniezno and Poznań under the rule of Przemysł II.'
- `/ledger/5` https://en.wikipedia.org/wiki/Duchy_of_Greater_Poland: infobox range only ('1207–1229'); no sentence; see fixes

Area: Duchy of Kalisz page gives no area (confirmed); placeholders acknowledged in notes.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| kingdom-of-bohemia 1198 found duchy-of-bohemia | duchy-of-bohemia 1002 dissolve | mismatch | Duchy dossier ends 1002 (successors HRE and kingdom-of-bohemia); 1003-1197 uncovered; flagged by the author; route to the duchy-of-bohemia group. |
| holy-roman-empire 1198 vassal_start kingdom-of-bohemia | kingdom-of-bohemia   | missing | HRE dossier makes Bohemia its vassal 1198-1259 (c2); Bohemia records no vassalage (author: not territorial). Decide once for the project. |
| kingdom-of-bohemia 1251 gain holy-roman-empire | holy-roman-empire   | missing | No 1251 loss of Austria in the HRE dossier (eu-08). |
| kingdom-of-hungary 1254 gain kingdom-of-bohemia | kingdom-of-bohemia   | missing | Hungary gains Styria from Bohemia 1 May 1254; Bohemia never holds Styria before 1260 (listed under thin). |
| kingdom-of-bohemia 1260 gain kingdom-of-hungary | kingdom-of-hungary 1261 loss | matched | One year apart (Kressenbrunn July 1260 / Peace of Vienna 31 March 1261). duchy-of-styria treats Styria as its own state throughout (renames 1254, 1260, 1276): double drawing to resolve in eu-09/eu-13. |
| kingdom-of-bohemia 1266 gain holy-roman-empire-minor-states | holy-roman-empire-minor-states   | missing | Egerland; counterpart corrected by the reviewer from holy-roman-empire. |
| kingdom-of-bohemia 1269 gain duchy-of-carinthia | duchy-of-carinthia   | missing | duchy-of-carinthia (976-1335) has no 1269 loss or 1276 change; holy-roman-empire-minor-states /ledger/2 loses Carinthia to Bohemia in 1272 (c1): three years off and a third claimant. |
| kingdom-of-bohemia 1272 gain patriarchate-of-aquileia | patriarchate-of-aquileia   | missing | No Friuli events in the Aquileia dossier (eu-13). |
| kingdom-of-bohemia 1276 loss house-of-habsburg | house-of-habsburg 1276 gain | matched | Friuli should go back to patriarchate-of-aquileia, not Habsburg (fix listed). |
| margraviate-of-brandenburg 1262 gain kingdom-of-bohemia | kingdom-of-bohemia   | missing | Budissin Land (Upper Lusatia) lost by Bohemia 1253-1262; not in Bohemia ledger or shapes (thin). |
| duchy-of-silesia 1290 loss kingdom-of-bohemia | kingdom-of-bohemia   | missing | Kłodzko Land to Bohemia 1290; Bohemia has no gain (thin). |
| kingdom-of-bohemia 1291 gain grand-duchy-of-krakow | duchy-of-greater-poland 1290 loss | mismatch | grand-duchy-of-krakow has no dossier yet (eu-15 part not run); duchy-of-greater-poland loses Kraków to Bohemia in 1290 instead. Counterpart to settle in eu-15. |
| duchy-of-sandomierz 1292 rename kingdom-of-bohemia | kingdom-of-bohemia 1291 gain | mismatch | Sandomierz treats Wenceslaus II's takeover as a rename (keeps drawing the land); Bohemia gains Lesser Poland in 1291. |
| kingdom-of-bohemia 1300 gain duchy-of-greater-poland | duchy-of-greater-poland 1300 rename | mismatch | GP records a rename and keeps the land to 1304: Greater Poland drawn twice 1300-1304. |
| kingdom-of-bohemia 1306 loss kingdom-of-poland | kingdom-of-poland   | exception | kingdom-of-poland not written yet (eu-15 part not run). |
| kingdom-of-bohemia 1306 loss duchy-of-greater-poland | duchy-of-greater-poland   | mismatch | GP dossier ends 1304; counterpart must be a 1306 holder (fix listed). |
| kingdom-of-bohemia 1319 gain margraviate-of-brandenburg | margraviate-of-brandenburg 1319 loss | matched | Western Upper Lusatia. |
| kingdom-of-bohemia 1322 gain holy-roman-empire-minor-states | holy-roman-empire-minor-states   | missing | Egerland pledge; counterpart corrected by the reviewer. |
| kingdom-of-bohemia 1327 vassal_start duchy-of-silesia | duchy-of-silesia   | mismatch | duchy-of-silesia (which also holds the Duchy of Wrocław row) ends 1304, though its own note says the Wrocław duchy lived to 1335; route to eu-15. |
| kingdom-of-bohemia 1327 vassal_start duchy-of-opole | duchy-of-opole   | exception | No dossier yet (eu-15 part not run). |
| kingdom-of-bohemia 1329 vassal_start Silesian duchies of Legnica, Żagań, Oleśnica, Ścinawa and Brzeg | None   | exception | Free string; listed under counterparts_needing_dossiers (duchy-of-legnica is an eu-15 slug not yet written). |
| kingdom-of-bohemia 1329 gain duchy-of-jawor | duchy-of-jawor   | exception | No dossier yet (eu-15 part not run); counterpart corrected by the reviewer; consistent with margraviate-of-brandenburg 1319 loss to duchy-of-jawor. |
| kingdom-of-bohemia 1331 gain duchy-of-g-ogow | duchy-of-g-ogow   | exception | No dossier yet (eu-15 part not run). |
| kingdom-of-bohemia 1335 gain kingdom-of-poland | kingdom-of-poland   | exception | No dossier yet, but the event itself is wrong (renunciation, not a transfer): fix listed. |
| kingdom-of-bohemia 1336 vassal_start Duchy of Ziębice (Münsterberg) | None   | exception | Listed under counterparts_needing_dossiers. |
| kingdom-of-bohemia 1342 vassal_start Duchy of Nysa (Neisse) | None   | exception | Listed under counterparts_needing_dossiers. |
| holy-roman-empire-minor-states 1333 loss kingdom-of-bohemia | kingdom-of-bohemia   | mismatch | HREMS follows Cliopatria cells (Lower Silesia, Saxony) at c1; Bohemia treats Silesia as vassal tint from 1327/1329. |
| holy-roman-empire-minor-states 1344 loss kingdom-of-bohemia | kingdom-of-bohemia 1367 gain | mismatch | HREMS loses Brandenburg cells to Bohemia in 1344 (Cliopatria artefact); Bohemia's keyframe 17 removes Lower Lusatia until 1367 (gained from margraviate-of-brandenburg). |
| kingdom-of-bohemia 1355 gain Electoral Palatinate (Wittelsbach; seller not named on the page) | electoral-palatinate   | missing | electoral-palatinate now has a dossier (1085-1777) with no 1355 loss; author should use the slug if a page names the seller. |
| kingdom-of-bohemia 1367 gain margraviate-of-brandenburg | margraviate-of-brandenburg 1367 loss | matched | Lower Lusatia. |
| kingdom-of-bohemia 1373 vassal_start margraviate-of-brandenburg | margraviate-of-brandenburg 1373 rename | mismatch | Brandenburg records the Luxembourg purchase as a rename, not a vassalage. |
| kingdom-of-bohemia 1375 vassal_start margraviate-of-moravia | margraviate-of-moravia   | mismatch | margraviate-of-moravia (1182-1918) records no vassal relation and covers Moravia as its own land throughout, overlapping Bohemia's direct Moravia 1198-1374 and 1415-1526; route to eu-15. |
| kingdom-of-bohemia 1401 loss electoral-palatinate | electoral-palatinate   | missing | No 1401 gain in electoral-palatinate; counterpart corrected by the reviewer. |
| kingdom-of-bohemia 1402 loss teutonic-order | teutonic-order 1402 gain | mismatch | teutonic-order gains the Neumark from margraviate-of-brandenburg, which has the matching loss; Bohemia's loss is a duplicate (fix listed). |
| kingdom-of-bohemia 1411 vassal_end margraviate-of-brandenburg | margraviate-of-brandenburg 1411 rename | mismatch | Type disagreement as in 1373. |
| kingdom-of-bohemia 1415 vassal_end margraviate-of-moravia | margraviate-of-moravia   | missing | Confidence 1; Jobst died 18 January 1411. |
| electorate-of-brandenburg 1445 gain kingdom-of-bohemia | kingdom-of-bohemia   | missing | Cottbus; Bohemia lacks the loss (fix listed). |
| kingdom-of-bohemia 1468 contest_start kingdom-of-hungary | kingdom-of-hungary 1468 contest_start | matched | margraviate-of-moravia dates its contest 1469-1479. |
| kingdom-of-bohemia 1478 loss kingdom-of-hungary | kingdom-of-hungary 1478 gain | matched | 21 July 1478 on both sides (Kingdom/Lands pages: 1479). |
| kingdom-of-bohemia 1490 gain kingdom-of-hungary | kingdom-of-hungary 1491 loss | matched | One year apart (Matthias died 1490; Peace of Pressburg 1491). |
| kingdom-of-bohemia 1526 dissolve None | habsburg-monarchy 1526 gain | matched | Successor takes Bohemia in 1526. |
| duchy-of-kalisz 1177 found duchy-of-greater-poland | duchy-of-greater-poland 1177 loss | mismatch | GP's 1177 loss names duchy-of-sandomierz (Casimir II), not Kalisz. |
| duchy-of-kalisz 1181 loss duchy-of-greater-poland | duchy-of-greater-poland 1181 gain | mismatch | GP gains Gniezno and Kalisz from duchy-of-sandomierz; counterpart disagreement. |
| duchy-of-kalisz 1191 gain duchy-of-greater-poland | duchy-of-greater-poland   | missing | No GP mirror. |
| duchy-of-kalisz 1194 loss duchy-of-greater-poland | duchy-of-greater-poland   | missing | No GP mirror. |
| duchy-of-kalisz 1207 gain duchy-of-greater-poland | duchy-of-greater-poland 1207 loss | matched | Odonic receives Kalisz. |
| duchy-of-kalisz 1229 loss duchy-of-greater-poland | duchy-of-greater-poland 1217 gain | mismatch | 12 years apart (fix listed). |
| duchy-of-kalisz 1234 gain duchy-of-greater-poland | duchy-of-greater-poland 1234 loss | mismatch | GP loses Kalisz to duchy-of-silesia in 1234, not to Kalisz (fix listed); duchy-of-silesia /ledger/14 gains it. |
| duchy-of-kalisz 1238 loss duchy-of-greater-poland | duchy-of-greater-poland 1244 gain | mismatch | GP regains Kalisz from duchy-of-silesia in 1244. |
| duchy-of-kalisz 1247 gain duchy-of-greater-poland | duchy-of-greater-poland   | missing | No GP mirror (also 1250 loss, 1253 gain, 1257 loss, 1277 gain). |
| duchy-of-kalisz 1279 merge duchy-of-greater-poland | duchy-of-greater-poland 1279 merge | matched | GP names a free string 'Duchy of Kalisz and Gniezno (Bolesław the Pious)'; should use the duchy-of-kalisz slug. |

## Problems

- WebFetch returns a small-model summary; quotes above are what it returned.
- Reviewer applied five counterpart-slug fixes to kingdom-of-bohemia.json (/ledger/3, 4, 13, 17, 33); the file re-validated with 0 errors and 0 warnings in non-resolve mode.
- electoral-palatinate now has a dossier: drop it from the author's counterparts_needing_dossiers.
- Cross-batch conflicts outside this batch: margraviate-of-moravia (1182-1918) draws Moravia as its own land throughout, overlapping kingdom-of-bohemia; duchy-of-styria, kingdom-of-hungary and kingdom-of-bohemia all claim Styria 1254-1276; duchy-of-carinthia and holy-roman-empire-minor-states both lack the 1269 Carinthia transfer; duchy-of-silesia ends 1304 though the Wrocław duchy lasted to 1335.
