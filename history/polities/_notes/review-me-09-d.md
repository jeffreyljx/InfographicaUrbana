# Review of batch me-09-d (2026-10-24)

Reviewer for Phase B. Mechanical check: validate_dossier.py --resolve gives 0 errors on all six. The warnings are counterpart slugs with no dossier (listed by the author) and the gazetteer place Corycus.
Under the orchestrator's rules for this run, I applied small fixes I verified on a page myself (marked applied); everything else goes to the author (fail) or a gap-filler (thin).

Verdicts: ayyubid-sultanate thin, kingdom-of-cyprus thin, khwarezmid-empire thin, rasulid-dynasty thin, mamluk-sultanate fail, bahrani-dynasty thin.

## ayyubid-sultanate: thin

Area: infobox 2000000 km2 (1190), Cliopatria 1830453 km2, ratio 0.92. Low-end estimate 1.7 M km2 for 1200 against the 1202 shape's 1.82 M km2 (ratio 1.07), also quoted correctly.

Gaps (for a gap-filler):
- `/ledger (after /ledger/14)`: No 1224 loss of Hadramawt. The Ayyubid dynasty page says 'In 1224 a local dynasty gained control of Hadramaut from the Ayyubids', but /ledger/6 (1180 gain) is never undone before the 1229 loss of Yemen. Keyframes 1220 and 1227 still draw Hadramawt for 1224-1228. The author's notes do not flag it. Page to try: https://en.wikipedia.org/wiki/Ayyubid_dynasty
- `/ledger (1173-1175)`: No occupation_start/occupation_end for Turan-Shah's 1173-1175 occupation of Lower Nubia (Qasr Ibrim), the mirror of makuria /ledger/4-5 (occupation_start 1173, occupation_end 1175, counterpart ayyubid-sultanate). Page to try: https://en.wikipedia.org/wiki/Makuria
- `/ledger (1226 or 1230)`: No loss of Akhlat to Jalal ad-Din or regain after it, the mirror of khwarezmid-empire /ledger/29 (1226 gain, counterpart ayyubid-sultanate). The Jalal ad-Din page has him take Akhlat 'from the Ayyubids' and move 'against Ahlat again in 1229'. Page to try: https://en.wikipedia.org/wiki/Jalal_ad-Din_Mingburnu
- `/ledger/14`: The 1202 vassal_end of the Zengids of Mosul is confidence 1. The Ayyubid page gives the March 1186 treaty (military support) but no end date. Page to try: https://en.wikipedia.org/wiki/Zengid_dynasty
- `/keyframe_review/7`: Fifth Crusade not coded (unverified: page budget). The Ayyubid page says 'In 1218, the fortress of Damietta ... was besieged by the Crusaders' and 'in 1221, the Crusaders were driven out of the Nile Delta'. Damietta is an occupation for about 1219-1221. Page to try: https://en.wikipedia.org/wiki/Fifth_Crusade
- `/ledger/18`: The 1239 Ayyubid recapture of Jerusalem and its 1243 cession to the Franks are not coded. The page gives only 1244-1245 ('as-Salih Ayyub gained possession of Jerusalem'). Page to try: https://en.wikipedia.org/wiki/Barons%27_Crusade

Spot checks:
- `/ledger/2` https://en.wikipedia.org/wiki/Ayyubid_dynasty: confirmed: 'In May 1174, Turan-Shah conquered Zabid and later that year captured Aden'
- `/ledger/6` https://en.wikipedia.org/wiki/Ayyubid_dynasty: confirmed: 'conquered the greater part of Hadramaut in 1180' (but see the thin item on 1224)
- `/ledger/9` https://en.wikipedia.org/wiki/Ayyubid_dynasty: confirmed: 'Saladin and Mas'ud negotiated a treaty in March 1186' with military support owed
- `/ledger/17` https://en.wikipedia.org/wiki/Ayyubid_dynasty: confirmed: 'accomplished in 1238 when Nur al-Din Umar captured Mecca'
- `/ledger/20` https://en.wikipedia.org/wiki/Ayyubid_dynasty: confirmed: 'killed him in April 1250'
- `/ledger/21` https://en.wikipedia.org/wiki/Ayyubid_dynasty: confirmed: 'In 1260, the Mongols sacked Aleppo and conquered the Ayyubids' remaining territories'; infobox 'Disestablished: 1260'

## kingdom-of-cyprus: thin

Area: infobox None km2 (None), Cliopatria 11437 km2, ratio None. No infobox area (the author says so). The 11,437 km2 island shape is 1.24 times the island's 9,251 km2, under the factor of two.

Findings:
- `/ledger/6/counterpart` (applied by reviewer): Corycus's 1448 loss named ramadanid-emirate as the taker, which was a Cliopatria-neighbour reading. Evidence: The Corycus page: 'From 1448 or 1454 it belonged alternately to the Karamanids, the Egyptians'. The Ramadanids are not named on it. Fix: counterpart beylik-of-karaman, with a reviewer note; https://en.wikipedia.org/wiki/Corycus added to sources

Gaps (for a gap-filler):
- `/ledger/7`: The 1464 return of Famagusta is confidence 1 (bridging). The Kingdom of Cyprus, Famagusta and James II of Cyprus pages are all silent on how and when James II recovered it. Page to try: https://en.wikipedia.org/wiki/Charlotte,_Queen_of_Cyprus
- `/ledger/2, /ledger/5`: The page does not name who lost Antalya in 1361 or took it in 1373. beylik-of-teke is a Cliopatria reading. Page to try: https://en.wikipedia.org/wiki/Beylik_of_Teke
- `/wars`: The Genoese war of 1373-74 and its treaty (Famagusta's cession) are not coded. The Famagusta page gives only 'In 1372 the port was seized by Genoa'. Page to try: https://en.wikipedia.org/wiki/Peter_II_of_Cyprus

Spot checks:
- `/ledger/2` https://en.wikipedia.org/wiki/Kingdom_of_Cyprus: confirmed: 'Antalya between 1361 and 1373'
- `/ledger/3` https://en.wikipedia.org/wiki/Kingdom_of_Cyprus: confirmed: 'Corycus between 1361 and 1448' (the Corycus page has Peter I take suzerainty in 1360)
- `/ledger/4` https://en.wikipedia.org/wiki/Famagusta: confirmed: 'In 1372 the port was seized by Genoa and in 1489 by Venice'
- `/ledger/5` https://en.wikipedia.org/wiki/Kingdom_of_Cyprus: confirmed: Antalya to 1373
- `/ledger/6` https://en.wikipedia.org/wiki/Corycus: confirmed year 1448; counterpart corrected to the Karamanids
- `/ledger/8` https://en.wikipedia.org/wiki/Kingdom_of_Cyprus: confirmed: reign table ends Catherine on 26 February 1489; 'forced to sell the island to Venice'
- `/ledger/7` https://en.wikipedia.org/wiki/James_II_of_Cyprus: not on page (the Famagusta return); the event is already confidence 1

## khwarezmid-empire: thin

Area: infobox 2300000 km2 (1210), Cliopatria 2805068 km2, ratio 1.22. The 1218 estimate of 3.6 M km2 against the 1216 shape's 4.02 M km2 (ratio 1.12) was also confirmed; the extra 0.5 M km2 in Pakistan is corrected in /keyframe_review/3.

Gaps (for a gap-filler):
- `/ledger/29`: The 1226 gain of Akhlat from the Ayyubids has no matching loss, though the note says 'it was not held', so Akhlat stays Khwarazmian to 1231. The Ayyubid side has no mirror. The Khwarazmian page gives no year ('capturing the town Ahlat'). The likely capture was in 1230 after the siege, with the loss after Yassıçemen in August 1230. Page to try: https://en.wikipedia.org/wiki/Battle_of_Yass%C4%B1%C3%A7emen
- `/ledger/20`: The fall of Gurganj is confidence 1. Neither the Mongol conquest page nor the Khwarazmian page dates it. Page to try: https://en.wikipedia.org/wiki/Siege_of_Gurganj
- `/ledger/22, /ledger/24`: The Punjab years (gain 1221-11, loss 1223) need reconciling: the Jalal ad-Din page also says 'first in the Punjab from 1222 to 1224'. Page to try: https://en.wikipedia.org/wiki/Jalal_ad-Din_Mingburnu
- `/identity/capitals`: No capital for 1221-1225 (Ghazni ends 1221, Tabriz begins 1225). Page to try: https://en.wikipedia.org/wiki/Khwarazmian_Empire
- `/keyframe_review/0, /ledger/1`: Khorasan 1202-1204 conflicts with the Ghurid dossier. ghurid-dynasty /ledger/33 records a 1204 loss of 'Khorasan, except Herat and Balkh' to this state at confidence 3, while this dossier's 1202 shape already holds Khorasan and records only a contest_start in 1204. Page to try: https://en.wikipedia.org/wiki/Ghurid_dynasty
- `/keyframe_review/2, /ledger/10`: The 1210 shape ('ok', running 1-2 years ahead of the conquest, as the note admits) gives Transoxiana and the lower Syr Darya from 1210. kara-khitans /ledger/20 and kimek-kipchak-confederation /ledger/7 record 1210 losses to this state, but the ledger's only gain is from the Kara-Khanids in 1212. Page to try: https://en.wikipedia.org/wiki/Ala_ad-Din_Muhammad_II

Spot checks:
- `/ledger/10` https://en.wikipedia.org/wiki/Ala_ad-Din_Muhammad_II: confirmed: 'Almost all of Transoxiana including cities like Sighnaq, Otrar and Uzkend were annexed by 1211-1212'
- `/ledger/14` https://en.wikipedia.org/wiki/Ala_ad-Din_Muhammad_II: confirmed: 'In November-December 1215, Muhammad went to Afghanistan'; Ghazni 1216-1217 as the note says
- `/ledger/15` https://en.wikipedia.org/wiki/Ala_ad-Din_Muhammad_II: confirmed: 'By late 1217, he controlled all of Persian Iraq'
- `/ledger/28` https://en.wikipedia.org/wiki/Jalal_ad-Din_Mingburnu: confirmed: Tabriz 'on 25 July 1225'
- `/ledger/29` https://en.wikipedia.org/wiki/Jalal_ad-Din_Mingburnu: on page in the 1226 context ('captured the town of Akhlat ... from the Ayyubids'), but with no year in the sentence; see thin
- `/ledger/32` https://en.wikipedia.org/wiki/Jalal_ad-Din_Mingburnu: confirmed: 'he was killed in 15 August 1231'

## rasulid-dynasty: thin

Area: infobox None km2 (None), Cliopatria 377950 km2, ratio None. The infobox gives no area (confirmed).

Findings:
- `/ledger/1` (applied by reviewer): The 1238 gain of Mecca was confidence 1 and cited the Rasulid page, which gives no year. Evidence: The Ayyubid dynasty page dates it: the Rasulids moved 'to end Ayyubid suzerainty in the Hejaz, which they accomplished in 1238 when Nur al-Din Umar captured Mecca'. Fix: confidence 2, source https://en.wikipedia.org/wiki/Ayyubid_dynasty (added to sources), reviewer note appended

Gaps (for a gap-filler):
- `/ledger/3`: The 1350 loss of Mecca to the Mamluks is confidence 1. The page says only that 'al-Mujahid Ali was captured by Egyptian Mamluks in Mecca' in 1350, which is not a transfer of Mecca. When Rasulid Mecca ended is still open, and the Mamluk dossier has no mirror gain. Page to try: https://en.wikipedia.org/wiki/Sharif_of_Mecca
- `/keyframe_review/1`: When Sanaa was first taken under Yusuf I (1249-1295) and how Hadramawt and Dhofar were held are undated. Page to try: https://en.wikipedia.org/wiki/Al-Muzaffar_Yusuf_I

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Rasulid_dynasty: confirmed: infobox 'Established: 1229'; 'al-Malik al-Mas'ud, left Yemen ... in 1229'
- `/ledger/2` https://en.wikipedia.org/wiki/Rasulid_dynasty: confirmed: 'Zaidi forces took Sanaa in 1324'
- `/ledger/4` https://en.wikipedia.org/wiki/Rasulid_dynasty: confirmed: 'Lahij fell to the Tahir clan in 1443'
- `/ledger/5` https://en.wikipedia.org/wiki/Rasulid_dynasty: confirmed: 'followed by Aden in 1454'
- `/ledger/6` https://en.wikipedia.org/wiki/Tahirid_Sultanate: confirmed: 'in 1454, the important port of Aden was swiftly taken'; the last Rasulid 'withdrew to Mecca in the same year'
- `/ledger/1` https://en.wikipedia.org/wiki/Ayyubid_dynasty: confirmed 1238 (fixed)

## mamluk-sultanate: fail

Area: infobox None km2 (None), Cliopatria 1854465 km2, ratio None. The infobox lists no area (confirmed); the author says so at /keyframe_review/1.

Findings:
- `/keyframe_review/2` (NOT applied, for the author): The keyframe mamluk-sultanate_1260 is marked ok, but its shape (north edge 34.2 N) leaves Aleppo and northern Syria outside the Mamluk state for 1260-1271, and no other state holds them then. Evidence: Battle of Ain Jalut page: 'the Mamluks captured Damascus five days later after Ain Jalut, followed by Aleppo within a month'; infobox 'The Mongols withdraw from the Levant and cede occupied territories to the Mamluk Sultanate'. mongol-empire /ledger/76 ends its Aleppo occupation in October 1260. Fix: verdict adjust; correction {"union":[{"cliopatria":"Mamluk Sultanate","year":1260},{"region":"Aleppo (region)"}],"text":"1260-1271: Egypt, the Hejaz and Syria with Aleppo from October 1260"}; add https://en.wikipedia.org/wiki/Battle_of_Ain_Jalut to sources
- `/ledger/12` (NOT applied, for the author): The 1271 gain of the Aleppo region from mongol-empire (confidence 2) is mis-dated by 11 years and misreads its page. Evidence: Mongol invasions of the Levant: in 1271 the Mongols 'moved southwards from Rûm and captured Aleppo' and then 'retreated back beyond the Euphrates when ... Baibars marched on them', so it was a raid on a city that was already Mamluk. Battle of Ain Jalut: Aleppo was Mamluk 'within a month' of 3 September 1260. Fix: Move the gain to 1260 (month 10), citing Battle_of_Ain_Jalut, or fold Aleppo into /ledger/3's region, and delete the 1271 gain (a raid moves no border).
- `/ledger/9` (NOT applied, for the author): The 1268 gain of 'Jaffa + Antakya' names principality-of-antioch, but Jaffa belonged to the Kingdom of Jerusalem. Evidence: The dossier's own quote: 'In 1268, the Mamluks captured Jaffa before conquering the Crusader stronghold of Antioch on 18 May'. Fix: Split it into a 1268 (March) gain of Jaffa (counterpart kingdom-of-jerusalem) and the 1268-5 gain of Antakya (counterpart principality-of-antioch).
- `/ledger/28` (NOT applied, for the author): The occupation_start of 1399 follows the Mamluk page ('Barquq died in 1399 ... That year, Timur invaded Syria'), but timurid-empire /ledger/8 dates the sacks of Aleppo and Damascus to 1400 from the Timur page. Evidence: Both are within a year, so they pair, but the two dossiers should agree. Fix: Use 1400 (Aleppo sacked in 1400), citing the Timur page, or give the conflict in the note. Not blocking.
- `/ledger/4, /ledger/5` (applied by reviewer): The 1262 Homs and c.1263 Kerak gains named ayyubid-sultanate, whose dossier ends in 1260. Evidence: Ayyubid dynasty page: al-Ashraf Musa had been allowed to keep governing Homs; 'After al-Ashraf Musa's death in 1262, the new Mamluk sultan, Baibars, annexed Homs'; 'The next year, al-Mughith Umar was tricked into surrendering Karak to Baibars'. Fix: counterparts 'Ayyubid emirate of Homs (al-Ashraf Musa; no dossier)' and 'Ayyubid emirate of Kerak (al-Mughith Umar; no dossier)', with reviewer notes

Gaps (for a gap-filler):
- `/ledger/1`: Hama as a vassal from 1260 is confidence 1. The Ayyubid page has Hama restored to Abu al-Fida in 1310 and 'formally placed under Mamluk rule' in 1341. Page to try: https://en.wikipedia.org/wiki/Abu%27l-Fida
- `/ledger/27`: The 1385 loss of the Cilician plain to the Ramadanids is confidence 1. The Cilicia page says only 'they were unable to hold it'. Page to try: https://en.wikipedia.org/wiki/Ramadanid_Emirate
- `/ledger/34`: The 1485 contest_start with the Ottomans is confidence 1, and the page does not name the land fought over. Page to try: https://en.wikipedia.org/wiki/Ottoman%E2%80%93Mamluk_War_(1485%E2%80%931491)
- `/ledger/37`: The 1516 gain of Tahirid Yemen is confidence 1. The Tahirid page gives the sultan's death 'on 15 May' with no year, and its infobox ends the Tahirids in 1517. Page to try: https://en.wikipedia.org/wiki/Tahirid_Sultanate
- `/ledger/14`: The 1276 gain of Lower Nubia has no mirror loss in makuria, which instead moves its court to Gebel Adda in Lower Nubia in 1365. The Makuria page: Mashkouda had to 'transfer Lower Nubia to Baybars', but it does not say the transfer was carried out. Page to try: https://en.wikipedia.org/wiki/Makuria

Spot checks:
- `/ledger/10` https://en.wikipedia.org/wiki/Mamluk_Sultanate: confirmed: 'In 1271, Baybars captured the major Krak des Chevaliers fortress from the County of Tripoli'
- `/ledger/12` https://en.wikipedia.org/wiki/Mongol_invasions_of_the_Levant: mis-dated: the 1271 sentence is a Mongol raid that captured Aleppo; Battle_of_Ain_Jalut puts Aleppo under the Mamluks in 1260
- `/ledger/14` https://en.wikipedia.org/wiki/Makuria: confirmed: 'transfer Lower Nubia to Baybars'
- `/ledger/25` https://en.wikipedia.org/wiki/Armenian_Kingdom_of_Cilicia: confirmed: 'Sis conquered by the Egyptian Mamluks: April 13, 1375'
- `/ledger/28` https://en.wikipedia.org/wiki/Mamluk_Sultanate: on page as written ('Barquq died in 1399 ... That year, Timur invaded Syria'); the Timurid dossier gives 1400
- `/ledger/29` https://en.wikipedia.org/wiki/Mamluk_Sultanate: confirmed: 'Timur ended his occupation of Syria in 1402'
- `/ledger/38` https://en.wikipedia.org/wiki/Ottoman%E2%80%93Mamluk_War_(1516%E2%80%931517): confirmed: 'The Battle of Marj Dabiq (24 August) was decisive'; 'Syria fell under the rule of the Ottomans'
- `/ledger/39` https://en.wikipedia.org/wiki/Mamluk_Sultanate: confirmed: infobox 'Ottoman conquest of Cairo: 22 January 1517'

## bahrani-dynasty: thin

Area: infobox None km2 (None), Cliopatria 73757 km2, ratio None. No area on the Usfurids or Jabrids infobox (confirmed).

Gaps (for a gap-filler):
- `/keyframe_review/2, /keyframe_review/3, /keyframe_review/4`: The small shape changes of 1440, 1468 and 1475 are unexplained (unverified: page budget). Page to try: https://en.wikipedia.org/wiki/Jabrids
- `/ledger`: Hormuz's suzerainty over Bahrain and Jabrid tribute are undated. The Jabrids page says most of the Omani coast 'remained under the rule of Hormuz'. Page to try: https://en.wikipedia.org/wiki/Kingdom_of_Ormus
- `/ledger/5`: The state closes in 1521 although the Jabrids infobox gives 'Disestablished: 1524', with successors Al-Muntafiq and Lahsa Eyalet, so the mainland in 1522-1524 is drawn for nobody. Consider ending in 1524 with the dissolve to the Muntafiq. Page to try: https://en.wikipedia.org/wiki/Jabrids
- `/identity/capitals`: No capital after 1417 (the Jabrid seat). Page to try: https://en.wikipedia.org/wiki/Jabrids
- `/keyframe_review/1`: The Qatar and northern-UAE parts of the Cliopatria shape are unsupported (the author flagged this). Page to try: https://en.wikipedia.org/wiki/Usfurids

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Usfurids: confirmed: 'in 1253 gained control of Eastern Arabia, including the islands of Bahrain'; infobox 'Established: 1253', capital al-Ahsa
- `/ledger/1` https://en.wikipedia.org/wiki/Usfurids: confirmed: infobox 'Disestablished: 1392'; 'overthrown by the Jarwanids'
- `/ledger/3` https://en.wikipedia.org/wiki/Jabrids: confirmed: 'Established: 1417'; 'deposing and killing the last Jarwanid ruler in Qatif'
- `/ledger/4` https://en.wikipedia.org/wiki/Jabrids: confirmed: 'an invasion of Bahrain by the Portuguese in 1521'
- `/ledger/5` https://en.wikipedia.org/wiki/Jabrids: partly: the infobox ends the Jabrids in 1524, which the note acknowledges; see thin

## Cross-dossier matrix

- ayyubid-sultanate 1229 loss (rasulid-dynasty) / rasulid-dynasty 1229 found: **matched**. Rasulid found counterpart ayyubid-sultanate.
- ayyubid-sultanate 1250 loss (mamluk-sultanate) / mamluk-sultanate 1250 found: **matched**. Months differ: Ayyubid page April 1250, Mamluk infobox 2 May 1250.
- ayyubid-sultanate 1238 vassal_end (sharifate-of-mecca) / rasulid-dynasty 1238 gain: **exception**. sharifate-of-mecca has no dossier (listed). The Rasulid 1238 gain of Mecca names the same counterpart and is now sourced to the Ayyubid page.
- khwarezmid-empire 1226 gain (ayyubid-sultanate) / ayyubid-sultanate None None: **missing**. Both dossiers are in this batch. The Ayyubid ledger has no Akhlat loss, and the Khwarezmid ledger never loses Akhlat again.
- rasulid-dynasty 1350 loss (mamluk-sultanate) / mamluk-sultanate None None: **missing**. Confidence 1. The Mamluk ledger has no gain of Mecca (the Hejaz is not coded there).
- mamluk-sultanate 1262 gain (Ayyubid emirate of Homs (al-Ashraf Musa; no dossier)) / ayyubid-sultanate 1260 dissolve: **exception**. Was ayyubid-sultanate, which ends in 1260; reviewer changed the counterpart.
- mamluk-sultanate 1263 gain (Ayyubid emirate of Kerak (al-Mughith Umar; no dossier)) / ayyubid-sultanate 1260 dissolve: **exception**. Was ayyubid-sultanate, which ends in 1260; reviewer changed the counterpart.
- mamluk-sultanate 1426 vassal_start (kingdom-of-cyprus) / kingdom-of-cyprus 1426 war note: **matched**. The schema has the overlord record vassalage (counterpart = the vassal). The Cyprus war 'Mamluk campaigns against Cyprus' points to it. Same for vassal_end 1489.
- ayyubid-sultanate 1174 gain (zengid-dynasty) / zengid-dynasty None None: **exception**. zengid-dynasty (me-09, another part) not written yet. Same for the 1175 and 1182 gains, the 1186 vassal_start and the 1202 vassal_end.
- ayyubid-sultanate 1187 gain (kingdom-of-jerusalem) / kingdom-of-jerusalem None None: **exception**. kingdom-of-jerusalem (me-09) not written yet. Same for 1192 loss, 1229 loss, 1244 gain.
- ayyubid-sultanate 1174 gain (Zabid, Aden and Sanaa / Hamdanids of Sanaa) / hamdanids-of-sanaa None None: **exception**. Listed in the author's counterparts_needing_dossiers.
- makuria 1173 occupation_start (ayyubid-sultanate) / ayyubid-sultanate None None: **missing**. makuria /ledger/4-5: Ayyubid occupation 1173-1175. The Ayyubid ledger lacks occupation_start/occupation_end with counterpart makuria.
- abbasid-caliphate 1202 vassal_start (ayyubid-sultanate) / ayyubid-sultanate None None: **matched**. Overlord-side record, per the schema; vassal_end 1250 likewise. The Ayyubid notes mention it.
- mongol-empire 1260 occupation_start (ayyubid-sultanate) / ayyubid-sultanate 1260 dissolve: **mismatch**. mongol-empire occupies Ayyubid Aleppo and Damascus (Jan-Oct 1260, occupation, not annexation). ayyubid-sultanate dissolves in 1260 with counterpart mongol-empire and no occupation event. mamluk-sultanate /ledger/3 gains Syria from mongol-empire in 1260-9. Align the three: either the Ayyubid ledger takes an occupation_start (counterpart mongol-empire) before its dissolve, or the Mongol dossier takes a gain and a loss.
- mamluk-sultanate 1260 gain (mongol-empire) / mongol-empire 1260 occupation_end: **mismatch**. Types differ (see above); the years agree.
- mamluk-sultanate 1271 gain (mongol-empire) / mongol-empire None None: **mismatch**. No Mongol event. The Mamluk event is mis-dated: Aleppo became Mamluk in 1260 (fail finding).
- khwarezmid-empire 1206 gain (ghurid-dynasty) / ghurid-dynasty 1206 loss: **matched**. ghurid /ledger/36 (Herat and Ghor).
- khwarezmid-empire 1209 vassal_start (ghurid-dynasty) / ghurid-dynasty 1206 vassal_start: **mismatch**. Three years apart: the Ghurid dossier dates the vassalage to 1206 (coinage table), the Khwarezmid to c.1209 (page gives no year).
- khwarezmid-empire 1215 gain (ghurid-dynasty) / ghurid-dynasty 1215 dissolve: **matched**. Also vassal_end 1215 on both sides.
- ghurid-dynasty 1204 loss (khwarezmid-empire) / khwarezmid-empire 1204 contest_start: **mismatch**. Ghurid (confidence 3): Khorasan except Herat and Balkh lost to Khwarazm in 1204. The Khwarezmid 1202 shape already holds Khorasan and the ledger has no 1204 gain.
- ghurid-dynasty 1206 loss (khwarezmid-empire) / khwarezmid-empire None None: **mismatch**. ghurid /ledger/41 Balkh (confidence 1); no Khwarezmid Balkh event.
- kara-khitans 1210 loss (khwarezmid-empire) / khwarezmid-empire 1212 gain: **mismatch**. The Khwarezmid ledger has only contest_end 1210 with kara-khitans and a 1212 gain from kara-khanid-khanate. The 1210 Khwarezmid shape ('ok') holds the land from 1210.
- kara-khitans 1216 loss (khwarezmid-empire) / khwarezmid-empire None None: **mismatch**. Kara-Khitan side confidence 1; no Khwarezmid 1216 gain.
- kimek-kipchak-confederation 1210 loss (khwarezmid-empire) / khwarezmid-empire None None: **mismatch**. Lower Syr Darya, Kipchak side confidence 1; no Khwarezmid event, though its 1210 shape holds it.
- khwarezmid-empire 1220 loss (mongol-empire) / mongol-empire 1221 gain: **matched**. One Mongol gain in 1221 covers the 1220 and 1221 losses (Transoxiana, Khwarezm, Khorasan).
- khwarezmid-empire 1231 dissolve (mongol-empire) / mongol-empire None None: **missing**. The mongol-empire dossier has no 1230-1231 contest with, or gain from, Jalal ad-Din's realm (Chormaqan's campaign).
- khwarezmid-empire 1207 vassal_start (burhanids-of-bukhara) / burhanids-of-bukhara None None: **exception**. Listed. Same for kara-khanid-khanate 1212/1213, eldiguzids 1217/1225, Kerman 1224.
- mamluk-sultanate 1276 vassal_start (makuria) / makuria 1276 vassal_start: **matched**. 
- mamluk-sultanate 1276 gain (makuria) / makuria None None: **mismatch**. makuria has no loss of Lower Nubia, and moves its court to Gebel Adda in Lower Nubia in 1365. Route to af-01.
- mamluk-sultanate 1366 vassal_end (makuria) / makuria 1365 vassal_end: **matched**. Within a year.
- mamluk-sultanate 1399 occupation_start (timurid-empire) / timurid-empire 1400 occupation_start: **matched**. Within a year; occupation_end 1402 against 1401 likewise. Recommend agreeing on 1400.
- mamluk-sultanate 1299 contest_start (ilkhanate) / ilkhanate 1299 contest_start: **mismatch**. Contest end: Mamluk 1322 (treaty), Ilkhanate 1303 (Marj al-Saffar). The Mongol invasions page has both ('April 1303'; treaty 'ratified in 1322/1323'). Not territorial.
- mamluk-sultanate 1265 gain (kingdom-of-jerusalem) / kingdom-of-jerusalem None None: **exception**. me-09 Crusader states not written yet. Same for 1266, 1291 (Jerusalem), 1268 (principality-of-antioch, but Jaffa belongs to Jerusalem), and 1271 and 1289 (county-of-tripoli).
- mamluk-sultanate 1285 vassal_start (armenian-kingdom-of-cilicia) / armenian-kingdom-of-cilicia None None: **exception**. Not written yet (me-09). Same for 1292 vassal_end and 1375 gain.
- mamluk-sultanate 1385 loss (ramadanid-emirate) / ramadanid-emirate None None: **exception**. Not written yet (me-09). Same for aq-qoyunlu 1433/1472, beylik-of-dulkadir 1471, tahirid-sultanate 1516 (me-09) and ottoman-empire 1516 (me-10).
- mamluk-sultanate 1271 gain (nizari-ismaili-state) / nizari-ismaili-state None None: **exception**. Listed (me-09-x). Likewise ayyubid-principality-of-hama 1260/1341.
- kingdom-of-cyprus 1361 gain (beylik-of-teke) / beylik-of-teke None None: **exception**. Not written yet (me-09). Same for armenian-kingdom-of-cilicia 1361, teke 1373, and beylik-of-karaman 1448 (counterpart corrected by reviewer from ramadanid-emirate).
- kingdom-of-cyprus 1372 loss (republic-of-genoa) / republic-of-genoa None None: **exception**. Owned by another group, not written yet; 1464 gain likewise. republic-of-venice for the 1489 dissolve likewise.
- byzantine-empire 1192 loss (kingdom-of-cyprus) / kingdom-of-cyprus 1192 found: **matched**. Cyprus's predecessor is byzantine-empire.
- rasulid-dynasty 1324 loss (imamate-of-yemen) / imamate-of-yemen None None: **exception**. The imamate-of-yemen row covers 1814-1872 only; the medieval Zaydi state is listed.
- rasulid-dynasty 1443 loss (tahirid-sultanate) / tahirid-sultanate None None: **exception**. Not written yet (me-09). Same for 1454.
- uyunid-emirate 1253 dissolve (usfurids) / bahrani-dynasty 1253 found: **mismatch**. Years agree, but the Uyunid dossier names 'usfurids', which is not a slug. It should name bahrani-dynasty. Route to me-08.
- bahrani-dynasty 1521 loss (portuguese-empire) / portuguese-empire None None: **missing**. The portuguese-empire dossier exists but has no 1521 gain of Bahrain.

## Problems

- Most me-09 neighbours are not written yet (zengid-dynasty, kingdom-of-jerusalem, principality-of-antioch, county-of-tripoli, armenian-kingdom-of-cilicia, beylik-of-teke, beylik-of-karaman, ramadanid-emirate, beylik-of-dulkadir, aq-qoyunlu, tahirid-sultanate), nor are ottoman-empire, republic-of-genoa, republic-of-venice and imamate-of-yemen, so their mirrors count as exceptions (groups not run).
- Reviewer-applied fixes (validated, 0 errors, read back): mamluk-sultanate /ledger/4 and /ledger/5 counterparts; rasulid-dynasty /ledger/1 confidence and source (plus a source entry); kingdom-of-cyprus /ledger/6 counterpart (plus a source entry).
- The neighbour dossiers mongol-empire, makuria, ghurid-dynasty, kara-khitans, kimek-kipchak-confederation, uyunid-emirate and portuguese-empire carry mismatches routed in cross_checks; they were not edited.
- WebFetch summaries of Mongol_conquest_of_Khwarezmia gave few dates (no Gurganj or Merv month), so /ledger/19 and /ledger/21 of khwarezmid-empire were only partly checked.
- No pages failed to load.
