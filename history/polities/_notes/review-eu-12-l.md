# Review of batch eu-12-l (crown-of-castile, emirate-of-granada, kingdom-of-majorca)

Reviewer, 2026-10-25. Machine copy: history/notes/phase-b/reviews/eu-12-l.json. All three dossiers validate with --resolve (0 errors, 0 warnings), before and after the one reviewer fix.

## crown-of-castile: fail (one blocking finding)
- BLOCKING, not applied. Missing loss of Gibraltar to the Marinids in 1333. The ledger gains Gibraltar in 1309 (/ledger/19) and again in 1462 (/ledger/32) with no loss in between, so Castile holds Gibraltar 1333-1462 on the map although the notes say "Castilian 1309-1333". History of Gibraltar: "the starving inhabitants of Gibraltar had already surrendered to the Moors of Fez" (June 1333). marinid-sultanate /ledger/14 has the 17 June 1333 gain from crown-of-castile at confidence 3. Fix: insert {1333, month 6, loss, marinid-sultanate, place Gibraltar km 15, History_of_Gibraltar, confidence 3} after /ledger/20.
- APPLIED by the reviewer. /ledger/22 (Algeciras, 26 March 1344): counterpart emirate-of-granada -> marinid-sultanate, confidence 2 -> 3. Siege of Algeciras page: "In 1329 the city was taken over by the King of Morocco, who made it the capital of his European domains"; Emirate page: Muhammad IV ceded "Ronda and Algeciras again in 1327 and 1328, respectively". Matches marinid-sultanate /ledger/17.
- Not blocking. /ledger/56 Oran 1507 (confidence 1): zayyanid-dynasty dates Mers el-Kebir 1505 and Oran 1509 (Spanish Oran infobox). Replace by two events and set keyframe 30 to adjust.
- Not blocking. /ledger/26 contest_end with Aragon 1369 against crown-of-aragon /ledger/43 at 1375 (Treaty of Almazan): agree one year.
- Not blocking. identity.predecessors lists kingdom-of-leon, whose dossier ends in 1230 merging into kingdom-of-castile; drop it or explain.
- Thin (gap-filler): Zahara has a 1481 loss and no earlier gain (taken 1407); confidence-1 events /ledger/20 (Olvera-Teba; Alfonso XI page silent, checked), 34, 46, 55, 59, 61, 62; the Algarve 1263-1267.
- Spot checks confirmed: Seville 22 Dec 1248, Murcia 1243, Priego and Alcala la Real 1342, Algeciras 26 March 1344 (date), Biscay 1370 (Crown table), Puerto Rico 1508, Navarre 1512 (annexed 7 July 1515), Melilla 1497, Gibraltar 1309.
- Area: infobox 335,000 km2 (1300) against Cliopatria 1294 shape 353,152 km2, ratio 1.05, acknowledged in keyframe notes.

## emirate-of-granada: fail
- BLOCKING, not applied. Missing losses of Ronda (1327) and Algeciras (1328) to the Marinids, on the dossier's main page: "to whom he ceded Ronda and Algeciras again in 1327 and 1328, respectively, to use as a base" (Emirate of Granada); "In 1329 the city was taken over by the King of Morocco" (Siege of Algeciras). Keyframes 7 (1294) and 8 (1333) are "ok" and keep both districts Granadan. Add both losses (confidence 3), set those keyframes to adjust, and find Ronda's return to Granada before the 1485 loss (/ledger/22).
- Not applied. /ledger/14, the 1344 loss of Algeciras to Castile: the city was Marinid from 1328/1329, so delete it once the 1328 loss is in (Castile /ledger/22 now names the Marinids).
- Not blocking. No mirror for Castile's 1333 confidence-1 gain of the Olvera-Teba cells (keyframe 8 describes it). Add a confidence-1 loss.
- Thin: Almeria and Guadix (1489, confidence 1; the page gives only "after the Spanish capture of Baeza [Baza] in November 1489"); Ronda's return; Setenil and Zahara 1407.
- Spot checks confirmed: Granada 17 April 1238; Marinids 1275 (Algeciras, Tarifa, Ronda); Malaga 1278 and 1279; cession of Algeciras and Ronda (year from the adjacent 1294 sentence); Priego and Alcala la Real 1342; Gibraltar to Granada 1374 (History of Gibraltar). /ledger/14 is contradicted by its page.
- Area: no area in the infobox; the page's "provinces of Granada, Almeria, and Malaga" (about 29,000 km2) fits the 31,456 km2 1241 shape.

## kingdom-of-majorca: thin (inside a budget of 1-2 pages)
- Every event spot-checked on the Kingdom of Majorca page was confirmed: 1276, 1286, May 1343, 1344, the 1349 sale to the King of France, and Llucmajor on 25 October 1349.
- Not blocking. /ledger/0 and /ledger/2 use region "Balearic Islands" (with Menorca), while keyframes 0-3 leave Menorca out until 1305 (_1279 bbox ends at 3.52 E) and /ledger/3 gains it in 1305. The 1295 gain also returns Ibiza and Menorca, which /ledger/1 (Mallorca only) never lost. Make them agree once a page dates Menorca: Alfonso III took it in 1287, and it was restored under Argelers in 1298.
- Not blocking. Type mismatch with crown-of-aragon: here loss and gain of Mallorca (1286, 1295), there occupation_start and occupation_end.
- Thin: Menorca (confidence 1), the 1298 handover, Peter III's 1285 occupation of Roussillon, the 1344 contest_end (confidence 1).

## Cross-dossier routing
- marinid-sultanate (af-02): add Granada's 1275, 1278, 1279, 1294, 1327, 1328 and 1374 events. Its 1294 entry has the Marinids gaining Tarifa from Castile, the reverse of Castile taking Tarifa from them in October 1292.
- crown-of-aragon (eu-12): no Murcia contest 1296-1305, no Menorca, occupation against loss/gain for Mallorca, and the 1375 end of the war against Castile's 1369.
- kingdom-of-france (eu-10): Montpellier 1349. taifa-of-cordoba: 1236 loss of Cordoba to Castile. taifa-of-murcia: the 1264-1266 contest.
