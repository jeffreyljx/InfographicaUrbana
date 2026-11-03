# Notes for batch eu-12-l (Iberia and the taifas, part l)

Written 2026-10-25 by the Phase B research agent. States: crown-of-castile, emirate-of-granada, kingdom-of-majorca. All three dossiers validate with `python3 -I tools/validate_dossier.py --resolve` (0 errors, 0 warnings).

## Pages that would not load
- https://en.wikipedia.org/wiki/Siege_of_Antequera (url_not_found) and https://en.wikipedia.org/wiki/Siege_of_Antequera_(1410) (url_not_found). Replaced by https://en.wikipedia.org/wiki/Ferdinand_I_of_Aragon, which gives only "he conquered the town of Antequera (1410)"; the siege dates, Setenil and Zahara of 1407 and the truce are unsourced.

## Page budget
- crown-of-castile: 16 pages opened, budget 9. Five are shared with the Granada dossier (Emirate of Granada, Granada War, Siege of Algeciras, History of Gibraltar, Ferdinand I of Aragon), two give capital and rulers (Kingdom of Castile, List of Castilian monarchs), one (Alfonso XI) was opened for the 1333 strip and was silent. The Murcia and Alfonso X pages were thin.
- emirate-of-granada: 8 pages, budget 9.
- kingdom-of-majorca: 2 pages, budget 1-2.

## crown-of-castile
- Start 1236 (Cliopatria; Córdoba), not 1230: the Kingdom of Castile dossier ends in 1235 and names this state as successor; the 1230 union is carried there and in the Leon dossier. End 1515 follows Cliopatria and the Kingdom of Spain dossier (starts March 1516); the Crown page keeps the Crown of Castile to 1716.
- Cliopatria shapes to correct: 1236 and 1241 hold Jaén, Arjona and (1241) a ring round Seville before the pages (Arjona 1244, Jaén March 1246, Seville 22 December 1248): corrected by `_1236`, `_1241` and new `_1244`, `_1246`, `_1248`. 1363-1374 holds the Aragonese lands five years past the page's end of the war (1369): `_1363` adjusted, new `_1370`. 1407, 1415, 1463, 1482, 1487 start one to five years after the pages (Fuerteventura and El Hierro 1405, Antequera 1410, Gibraltar August 1462, Gran Canaria 29 April 1483, Málaga August 1487): years-only adjusts. 1490 is new (Baza, Guadix, Almería before the 1492 surrender).
- Unverified shape moves (page silent, verdict ok): 1252-1260 cell swaps, 1285 (seven cells on the Aragonese frontier near Requena), 1305 (the Alicante-Vinalopó cells given to Castile although Torrellas awarded Aragon "many cities north of the Segura"), 1333 and 1352 (northern Granada frontier, Olvera-Teba line), 1440, 1502 (western Hispaniola), 1507 (rest of Hispaniola, Oran), 1512 (Jamaica, eastern Cuba, Tripoli, Béjaïa). Confidence-1 events carry them.
- The 1497-1512 shapes bundle Castilian and Aragonese conquests (Tripoli, Béjaïa) with the Caribbean; Cliopatria has no separate Aragon overlay for the Mediterranean posts.
- Vassalage of Granada: three start dates on the pages (1238 Ferdinand III page "a tributary arrangement", 1243 Nasrid page "tribute-paying vassals from 1243", March 1246 Treaty of Jaén). The ledger uses 1246 to 1482 as one span although the vassalage lapsed in war years (1264, 1340, 1405-1410). Murcia 1243-1266 and Niebla/Huelva 1238-1262 are also vassal spans.
- Baeza, Andújar and Martos: the Kingdom of Castile dossier (Ferdinand III page) has them Castilian-occupied from 1225, while the Emirate page has Baeza and Jaén accept Muhammad I in 1232. Baeza is left out of the Granada early keyframes and stays in Castile's shape.
- Not in the ledger: the Algarve (Alfonso X page: captured, returned "In 1263", Treaty of Badajoz 1267; year of capture ambiguous), the Treaty of Alcáçovas (1479) and Tordesillas (7 June 1494), the personal union with Aragon (1479; Cliopatria's relation row 1475-1515 is an umbrella).
- Capital: no page names one; Toledo stands in (Kingdom of Castile page: no settled capital, Burgos, Valladolid and Toledo as centres).

## emirate-of-granada
- Start 1232 July (Arjona), end 2 January 1492; Cliopatria has 1241-1491. New keyframes: 1232, 1238, 1239 (early realm: Jaén, Arjona, Guadix, then Granada, Almería, Málaga), 1244 and 1246 (Arjona and Jaén lost), 1369 (Algeciras back), 1482, 1485, 1486 (Granada War steps), 1490 (the city of Granada alone).
- The Strait cells (Gibraltar to Tarifa, four cells) are in Cliopatria's Granada shape from 1241 to 1462; the pages put Gibraltar with Granada to July 1309, Castile 1309-1333, the Marinids 1333-1374, Granada 1374-August 1462. The ledger carries those; the shapes were not split.
- Cliopatria's 1363 and 1375 shapes return and remove eight cells including the Priego-Alcalá la Real line, which the pages never return to Granada (Castile took it in 1342).
- Almería and Guadix: the Emirate page gives no year for their surrender; 1489 is a confidence-1 bridge. Loja: only the "second Loja siege" of 1486 is on the page. Ronda: year inferred from the sequence.
- Ceuta (Muhammad III, 1306 or 1307, Emirate page) is not drawn.
- The Alpujarras principality offered to Boabdil is not drawn (offer only).
- Cliopatria's Almohad shape (114 of 120 cells of the 1241 shape) and Taifa of Almería (6 cells) cover Granada's land until 1240.

## kingdom-of-majorca
- Start 1276 (infobox "Established: 1276"; Cliopatria 1279), end 25 October 1349 (Llucmajor; Cliopatria ends 1343). The page's infobox ends the kingdom in 1715 (Nueva Planta) and its table ends James III in 1344.
- Cliopatria's three shapes lack Montpellier and show no loss of Mallorca in 1286-1295; corrected by new keyframes 1276, 1286, 1295, 1343, 1344.
- The vassalage to Aragon from 1279 belongs in the Crown of Aragon dossier (see below). Peter III's 1285 occupation of the mainland and the Treaty of Argelers (1298) are on neither page. Menorca's date (Cliopatria 1305) and the 1349 sale (the page says "French possessions") need a page. Carlat is not drawn.

## Mirror events other dossiers should carry
- crown-of-aragon (eu-12): vassal_start/vassal_end for kingdom-of-majorca from 1279; gain of Mallorca 1286 and loss 1295 (June); Peter IV's conquest of the Balearic Islands (May 1343), Roussillon and Cerdanya (1344); Torrellas gain 1304-08 and contest 1296-1305, War of the Two Peters contests 1357-1361 and 1363-1369 (Tarazona, Cariñena, Teruel, Segorbe, Morvedre, Alicante, Caudete, Elda, Gandia); the Granada War (Aragonese forces) 1482-1492; personal union with Castile from 1479.
- taifa-of-almeria: loss of Almería to emirate-of-granada in 1238. taifa-of-cordoba: loss of Córdoba to crown-of-castile in 1236. taifa-of-murcia: vassal span 1243-1266 and annexation 1266. taifa-of-niebla: vassal span 1238-1262 and annexation 1262.
- almohad-caliphate (af-02): the pages name it nowhere; Cliopatria's Almohad shape covers Granada's land to 1240 and Seville to 1248, so Seville (1248) and Jaén/Arjona hold-ups carry the counterpart "almohad-caliphate" as a placeholder.
- marinid-sultanate (af-02): occupation of Algeciras, Tarifa and Ronda (1275), Málaga (1278-1279), cession of Algeciras and Ronda to Granada (1294), Tarifa lost to Castile (October 1292), Gibraltar (1333; handed to Granada 1374), Algeciras 1344.
- kingdom-of-navarre (eu-12): loss of Upper Navarre to Castile in 1512.
- wattasid-dynasty, zayyanid-dynasty, hafsid-dynasty (af-02): Melilla 1497, Oran 1507 and the Béjaïa/Tripoli posts 1510 (all confidence 1 or 2).
- kingdom-of-france (eu-10): Montpellier bought from James III in 1349.

## States without a dossier
- "Lordship of Biscay (Señorío de Vizcaya)": joined the Crown in 1370 (Crown page table). Cliopatria has no row.
- The Guanche kings of the Canary Islands and the Peraza-Herrera lordship (seigneurial phase 1402-c.1477): no row.
- The Muslim rulers of Jerez (1261): no row.

## Gazetteer names needed (coordinates were used instead so the dossiers resolve)
Places: Alcalá la Real, Priego de Córdoba, Antequera, Ronda, Guadix, Baza, Baeza, Tarifa, Vélez-Málaga, Alhama de Granada, Zahara de la Sierra, Jerez de la Frontera, Tarazona, Orihuela, Niebla, Menorca. Regions: Cerdanya (Pyrenean valley, 1.5-2.2 E, 42.3-42.5 N), Alpujarras.

## Repair pass, 2026-10-25 (eu-12-l, after the adversarial review)
This section supersedes the lines above where they differ (the 1507 Oran event, the confidence-1 Olvera-Teba event of 1333, the missing Gibraltar, Ronda and Algeciras losses, the 1344 loss of Algeciras, the Leon predecessor). kingdom-of-majorca was not touched (verdict thin). Both repaired dossiers validate on the mount with --resolve: crown-of-castile 0 errors, 0 warnings (69 events, 32 keyframes, 28 sources); emirate-of-granada 0 errors, 0 warnings (42 events, 27 keyframes, 16 sources).

### Applied
- crown-of-castile: (1) loss of Gibraltar to the Marinids, 17 June 1333, confidence 3 (Abu al-Hasan page: 'On 17 June 1333, Vasco Perez surrendered Gibraltar after agreeing terms with Abd al-Malik'; History of Gibraltar: 'had already surrendered to the Moors of Fez'). (2) Oran 1507 replaced by Mers el-Kebir 1505 (Mers El Kebir page: 'captured it in 1505 under Cardinal Cisneros') and Oran 1509 (Spanish Oran page: 'Spanish conquest: 1509'), both from zayyanid-dynasty at confidence 2; keyframe 1507 is adjust. (3) contest_end with Aragon kept at 1369, the note now quotes the Peter IV page (1375). (4) kingdom-of-leon dropped from predecessors; the kingdom-of-castile predecessor note says Leon's land arrives through it.
- crown-of-castile, from the thin list and now page-dated: Olvera and neighbours June 1327 and Teba 30 August 1330 (Muhammad IV of Granada page) replace the confidence-1 gain of 1333; keyframe 1333 is adjust. Zahara gained 1407 (Zahara de la Sierra page, 'ruled by Arabs until 1407', confidence 2) and 1483 (confidence 3). Jamaica 1509 (Colony of Santiago page) and eastern Cuba 1511 (Velazquez page, Baracoa by August 1511), both confidence 2, replace the confidence-1 events of 1512; the 1512 keyframe text says so.
- emirate-of-granada: losses of Ronda (1327, confidence 3), Marbella (1327, 2) and Algeciras (1328, 3) to the Marinids; keyframes 1294 and 1333 adjust, new keyframes 1327, 1328-1329, 1330-1332; keyframes 1344, 1352, 1363, 1369 keep Ronda and Marbella out; new keyframe 1374-1378. The 1344 loss of Algeciras to Castile is deleted (the siege stays in wars[]). Mirror losses to Castile: the Olvera line June 1327 and Teba 30 August 1330. Zahara lost 1407 and 1483.

### Where I differ from, or went beyond, the reviewer
- Ronda's return to Granada is on no page: Emirate, Ronda, Marinid Sultanate, Muhammad IV, Muhammad V, Yusuf I, Nasrid dynasty, Abu al-Hasan and Abu Inan Faris were opened; the Spanish Ronda pages do not load. It is a confidence-1 bridge at 1374, the one dated Marinid hand-over (Gibraltar, History of Gibraltar). The Marinids still held Ronda in 1340 and 'the Marinid Iberian territories' in 1349 (Yusuf I page), and Ronda is Nasrid at its fall in 1485 (Ronda page). Ronda and Marbella are therefore out of Granada's keyframes 1327-1373. A gap-filler should date the return.
- Marbella is added to the Ronda loss: Muhammad IV page 'he had to surrender Ronda and Marbella, followed by Algeciras in the next year'; Yusuf I page 'he had to yield Ronda, Marbella and Algeciras'. The reviewer named only Ronda and Algeciras.
- The Gibraltar loss cites the Abu al-Hasan page rather than History of Gibraltar: it gives the day (17 June); the Gibraltar page only says the relief force of June 1333 found it already surrendered, and the Emirate page says 'captured it in June'.
- Oran: the reviewer proposed Spanish Oran as the source for both events; that page has 1509 only ('Mers El Kebir: Not on page'), so Mers el-Kebir 1505 cites the Mers El Kebir page. The Spanish Oran page says 'Spanish Empire', not the Crown of Castile, hence confidence 2.
- 1369 or 1375: War of the Two Peters page 'The war lasted from 1356 to 1369' (no Almazan); Peter IV of Aragon page 'It ended in 1375 with the Treaty of Almazan, without a winner'; the Treaty of Almazan page does not load. Both are page-backed and cannot be reconciled from the pages opened. crown-of-castile keeps 1369 and its 1370-1374 keyframe; crown-of-aragon /ledger/43 has 1375. The map will show the contest over in Castile's dossier six years before Aragon's.
- Gibraltar and Algeciras: Granada's keyframes still contain the Strait cells (Gibraltar, Tarifa) for 1309-1373 and 1462; only Ronda, Marbella and Algeciras were cut out. The ledger carries Gibraltar as before.
- Still no page: Almeria and Guadix (the Muhammad XIII page does not mention them; 1489 stays a bridge), La Gomera (page: 1489 end of the conquest, no incorporation year), western Hispaniola (Captaincy General page: Ovando 1502 only), Bejaia (no page), Setenil 1407, the Algarve (Treaty of Badajoz page: 20 September 1264 renunciation of rights, signed 16 February 1267; no Castilian conquest described, so no event), Tripoli (Spanish Tripoli page: 1510, 'under the jurisdiction of Sicily', so Aragonese; the Castile event stays at confidence 1).

### Pages that would not load in the repair pass
- https://en.wikipedia.org/wiki/Abu_Salim_Ali, https://en.wikipedia.org/wiki/Treaty_of_Almaz%C3%A1n, https://es.wikipedia.org/wiki/Ronda_(M%C3%A1laga), https://es.wikipedia.org/wiki/Historia_de_Ronda (all url_not_found).

### Mirror events other dossiers should carry (additions to the list above)
- marinid-sultanate (af-02): gains of Ronda and Marbella (1327) and Algeciras (1328) from emirate-of-granada (Emirate page; Muhammad IV page); its /ledger/13 has Algeciras in 1329 from crown-of-castile at confidence 2, which the pages opened contradict (the city was Granada's until 1328 and Castile took it from the Marinids in 1344); loss of Ronda and Marbella to Granada (bridge 1374); Gibraltar 17 June 1333 is its /ledger/14 and matches.
- crown-of-aragon (eu-12): /ledger/43 ends the war with Castile in 1375, crown-of-castile in 1369 (see above).
- zayyanid-dynasty (af-02): /ledger/11 and /ledger/12 (Mers el-Kebir 1505, Oran 1509) match crown-of-castile's new events.
- kingdom-of-leon (eu-12): nothing to change; its only successor is kingdom-of-castile.

### Gazetteer names needed (additions; coordinates were used so the dossiers resolve)
Places: Olvera, Pruna, Torre Alhaquime, Teba, Mers El Kebir (Mazalquivir, 35.73 N, -0.70 E).
