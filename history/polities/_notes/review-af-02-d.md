# Review of batch af-02-d (Almohads, Kingdom of Africa, Hafsids, Zayyanids, Marinids)

Reviewed 2026-10-19 against the reviewer brief. The validator (with --resolve) passed all five dossiers with 0 errors and 0 warnings before and after the reviewer edits. Neighbour dossiers read for mirrors: almoravid-dynasty, hammadid-dynasty, spanish-empire (context list) and zirid-dynasty (counterpart of the Kingdom of Africa); the other context polities are not written yet (eu-12, me-09, me-10, am-06 parts, af-02 parts).

Verdicts: almohad-caliphate fail; kingdom-of-africa thin; hafsid-dynasty fix; zayyanid-dynasty fix; marinid-sultanate fix.

Reviewer edits applied in place (small, verified on the page opened): hafsid-dynasty /ledger/10-11 and marinid-sultanate /ledger/23-24 (the 1357 Tunis occupation was ended before it was started; the start now precedes the end and its month is in the note), zayyanid-dynasty /identity/rulers/38/to 1557 to 1551. Every other finding below is for the author (applied: no).

## almohad-caliphate: fail

Findings:

- `/ledger/46 and /keyframe_review/14/note` (for the author). Blocking: the confidence-1 bridge gives the Algarve and Alentejo to Portugal in 1241 and its note says the page lists no Portuguese gain between Alcacer do Sal (1217) and the fall of Seville (1248); the cited page lists two. Evidence: Almohad Caliphate page (re-read twice on 2026-10-19), in the list that follows 'The departure of al-Ma'mun in 1228 marked the end of the Almohad era in Spain': 'Merida and Badajoz in 1230 (to Leon), Mallorca in 1230 (to Aragon), Beja in 1234 (to Portugal)' and 'Silves in 1242 (to Portugal)'. KF14 also calls these cells 'undated on every page opened'. Fix: Replace /ledger/46 with a 1234 loss of Beja (admin1 Beja, Portugal) and a 1242 loss of Silves and the Algarve (admin1 Faro), counterpart kingdom-of-portugal, confidence 3, source the Almohad page; rewrite the KF14 note.
- `/ledger/36 and /keyframe_review/12/note` (for the author). Blocking: the confidence-1 bridge dates the Extremadura loss to Leon to 1227 and says the page is silent; the page dates it to 1230. Evidence: Almohad Caliphate page: 'Merida and Badajoz in 1230 (to Leon)'. The KF12 note says the 77 cells 'are undated on every page opened'. Fix: Date the loss 1230, region admin1 Badajoz (Spain) with the text of the page, counterpart kingdom-of-leon, confidence 3; extend the KF12 correction (or add a keyframe) so the Badajoz cells stay Almohad 1227-1229.
- `/ledger/45 and /keyframe_review/14/note` (for the author). Blocking: the confidence-1 bridge gives the south of Iberia to the Emirate of Granada in 1241 and says no page dates these places; the Almohad and Las Navas pages date several of them. Evidence: Almohad Caliphate page: 'Niebla-Huelva, 1238 (to Leon)', 'Murcia in 1243 (to Castile)', 'Jaen, 1246 (to Castile)', 'Alicante, 1248 (to Castile)'. Las Navas de Tolosa page: 'Jaen in 1246'. Fix: Replace the bridge with the dated losses (Niebla-Huelva 1238 to kingdom-of-leon or crown-of-castile, Jaen 1246 and Alicante 1248 to crown-of-castile); keep a bridge only for Granada, Malaga and Almeria and say which page is silent.
- `/ledger/33` (for the author). The 1212 loss takes the whole province of Jaen; the pages give only Baeza and Ubeda in 1212 and Jaen itself in 1246. Evidence: Las Navas page: 'Shortly after the battle, the Castilians took Baeza and then conquered Ubeda' and 'Jaen in 1246'; the Almohad page lists 'Jaen, 1246 (to Castile)'. Fix: Region: union of places Baeza and Ubeda (about 25 km each), confidence 3; add a 1246 loss of Jaen to crown-of-castile, confidence 3.
- `/ledger/37 to /ledger/50, /keyframe_review/13 and /keyframe_review/14` (for the author). Blocking: the Iberian side 1228-1248 is inconsistent: the page ends the Almohad era in Spain in 1228 and the dossier records Murcia leaving that year, yet keeps Cordoba to 1236, Valencia to 1238 and the south to 1241/1248 as Almohad using the page's list of Christian conquests selectively. Evidence: Almohad Caliphate page: 'In October 1228, with Spain practically all lost, al-Ma'mun abandoned Seville' and 'The departure of al-Ma'mun in 1228 marked the end of the Almohad era in Spain', followed by the dated list of conquests (author's notes flag the disagreement but the ledger uses only part of the list). Fix: State in notes which parts of al-Andalus remained Almohad after 1228 (with a page), then either remove Iberia from the corrections from 1228/1229 with losses to the Andalusi rulers who took it, or keep the Cliopatria shapes and date every place from the list; the counterparts of /ledger/43, /ledger/44 and /ledger/50 must follow that choice.
- `/ledger/41 and /ledger/42` (for the author). Algiers and the Chelif are lost twice: to the Hafsids in 1235 (/ledger/41) and again inside the Cliopatria Zayyanid 1236 shape handed to the Zayyanids in 1236 (/ledger/42). Evidence: The Zayyanid 1236 shape reaches 4.67 E (shapes.csv bbox) and zayyanid-dynasty /keyframe_review/0 says it 'overlaps what the Hafsid page has annexed in 1235'; hafsid-dynasty /ledger/2 gains Alger and Chlef in 1235. Fix: Give /ledger/42 the region {"minus": [Zayyanid dynasty 1236, union(admin1 Alger, admin1 Chlef)]} (or the Oranais the Zayyanid found event uses), consistent with the Hafsid fix.
- `/ledger/28 and /ledger/31` (for the author). Contest_start/contest_end 1184-1188 against an occupation in the almoravid-dynasty ledger (/ledger/48 occupation_start 1184-11, /ledger/51 occupation_end 1188, counterpart almohad-caliphate): the types disagree. Evidence: Brief rule 3: an occupation of X's land is an occupation in X's ledger. Banu Ghaniya page: campaigns 'from November 1184'; the Almohad page: Ifriqiya 'reconquered ... in 1187-1188'. Fix: Retype to occupation_start (1184, month 11) and occupation_end (1188), counterpart almoravid-dynasty, region Bejaia, Constantine, Algiers and Tunisia as the Almoravid side has; keep the war.

Thin (for a gap-filler):

- `/ledger/12 to /ledger/19`: Confidence-1 taifa gains all at 1152; Almeria was Castilian 1147-1157 and taken by the Almohads only in 1157 (author gap); Badajoz, Niebla, Carmona dates. Page to try: https://en.wikipedia.org/wiki/Almer%C3%ADa
- `/ledger (after /ledger/32)`: No event for the Banu Ghaniya hold on Ifriqiya after 1188 (Yahya ibn Ghaniya in Tunis and Mahdia about 1203, the reconquest by al-Nasir about 1205-1206); the Almohad page is silent. Page to try: https://en.wikipedia.org/wiki/Muhammad_al-Nasir
- `/keyframe_review/7 and /keyframe_review/8`: Extremadura cells lost 1188 and back 1202 (unverified: page budget). Page to try: https://en.wikipedia.org/wiki/Battle_of_Alarcos
- `/ledger/27`: Valencia 1172 is a confidence-1 bridge. Page to try: https://en.wikipedia.org/wiki/Taifa_of_Valencia
- `/ledger/7 and /ledger/52`: Confidence-1 bridges for the rest of Morocco in 1147 and 1269. Page to try: https://en.wikipedia.org/wiki/Abu_Yusuf_Yaqub_ibn_Abd_al-Haqq
- `/identity`: No ruler list (author gap). Page to try: https://en.wikipedia.org/wiki/List_of_rulers_of_Morocco

Spot checks: /ledger/1 confirmed; /ledger/5 confirmed; /ledger/25 confirmed; /ledger/29 confirmed; /ledger/32 confirmed; /ledger/35 confirmed; /ledger/40 confirmed; /ledger/44 confirmed; /ledger/50 confirmed; /ledger/42 confirmed; /ledger/36 mis-dated; /ledger/46 mis-dated; /ledger/45 not on page; /ledger/33 mis-dated.

Area: Infobox: 2,300,000 km2 (1150, high-end peak estimate) and 2,000,000 km2 (1200, low-end peak); shapes alive: almohad-caliphate_1147 (504,938, ratio 0.22) and _1188 (925,048, ratio 0.46). KF4 and KF5 acknowledge the factor (against the 1152 and 1169 shapes) and attribute it to Saharan land; accepted.

## kingdom-of-africa: thin

Thin (for a gap-filler):

- `/keyframe_review/1 to /keyframe_review/2`: Thin by design (1-2 page budget): the step from four town circles (1148-1151) to the 39,613 km2 coastal belt in 1152 has no event; Gabes is lost in /ledger/6 but never gained; Kerkennah fell to Roger (undated on the page); the 1152 fleet against Bone has no outcome. Page to try: https://en.wikipedia.org/wiki/George_of_Antioch
- `/ledger/1`: Tunis tribute from 1148 is a confidence-1 bridge (page undated). Page to try: https://en.wikipedia.org/wiki/Roger_II_of_Sicily

Spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/4 confirmed; /ledger/5 confirmed; /ledger/8 confirmed.

Area: The page has no infobox (re-checked); the dossier says the area is uncompared.

## hafsid-dynasty: fix

Findings:

- `/ledger/10 and /ledger/11` (applied by reviewer). The occupation_end of Tunisia (1357) stood before its own occupation_start (August 1357), so the August 1357 occupation never closed. Evidence: Hafsid page: 'captured Tunis in August 1357'; Abu Inan Faris page: 'he was forced to retreat from Tunisia in 1357' (no month). Fix: Applied by the reviewer: occupation_start moved before occupation_end, its month dropped (August kept in the note). Re-validated: 0 errors, 0 warnings.
- `/ledger/2, /ledger/18 and /keyframe_review/0/correction` (for the author). Algiers and the Chelif are gained in 1235 and gained again in 1410 from nobody with no loss between, and no keyframe correction draws them (Cliopatria's Hafsid shapes stop at 4.39 E, shapes.csv bbox; Algiers is at 3.06 E); the Zayyanid shape holds them from 1236. Evidence: Hafsid page: 'In 1235 he captured Algiers and then established his authority as far as the Chelif River' and 'He annexed ... Algiers (1410-1411)'; zayyanid-dynasty /keyframe_review/0 flags the overlap. Fix: Either add a loss of Algiers and Chlef (to zayyanid-dynasty, year from a page such as the Algiers article; confidence 1 if bridged) and give /ledger/18 the Zayyanids as counterpart (with a mirror loss there), or draw Algiers in the corrections from 1235 and cut it from the Zayyanid side; fix /keyframe_review/0 so it includes Algiers in 1235 or move the gain.
- `/ledger/13` (for the author). The 1370 merge (counterpart Hafsid branch of Tunis) follows the 1318 merge with no split between, so it merges a branch that never split off; the counterpart is not in counterparts_needing_dossiers. Evidence: Hafsid page: reunification 'under Abu Yahya Abu Bakr II (r. 1318-1346)' and 'the emir of Bejaia and Constantine, conquered Tunis in 1370'. Fix: Add the split (Bejaia and Constantine again apart after 1346 or during the Marinid occupations, with a page) or recast /ledger/13 using the same branch name as /ledger/5 and /ledger/6.

Thin (for a gap-filler):

- `/ledger/4`: End of the 1242 hold on Tlemcen bridged to 1249 (confidence 1); the Zayyanid ruler likely became a Hafsid vassal soon after 1242. Page to try: https://en.wikipedia.org/wiki/Yaghmurasen_Ibn_Zyan
- `/ledger/6 and /ledger/13`: 1318 reunion (confidence 1) and the second split before 1370. Page to try: https://en.wikipedia.org/wiki/Abu_Yahya_Abu_Bakr_II
- `/ledger/20`: End of the Tlemcen client period bridged to 1434 (confidence 1). Page to try: https://en.wikipedia.org/wiki/Hafsid_dynasty
- `/ledger/27`: Constantinois to Algiers bridged to 1530 (confidence 1). Page to try: https://en.wikipedia.org/wiki/Constantine,_Algeria
- `/keyframe_review/6`: Tripolitania 1453-1457 before the 1458 conquest. Page to try: https://en.wikipedia.org/wiki/Ottoman_Tripolitania

Spot checks: /ledger/1 confirmed; /ledger/7 confirmed; /ledger/9 confirmed; /ledger/10 confirmed; /ledger/14 confirmed; /ledger/21 confirmed; /ledger/23 confirmed; /ledger/24 confirmed; /ledger/25 confirmed; /ledger/32 confirmed.

Area: The Hafsid page has no area (re-checked); the dossier says so.

## zayyanid-dynasty: fix

Findings:

- `/identity/rulers/38/to` (applied by reviewer). The last ruler ran to 1557, six years past the state's end (1551). Evidence: Zayyanid page: 'By 1551, the Ottomans had occupied Tlemcen'; the ruler's own note calls him a ruler in exile after 1551. Fix: Applied by the reviewer: to = 1551, note kept. Re-validated: 0 errors, 0 warnings.
- `/ledger (after /ledger/8)` (for the author). The Marinid occupations of 1370-1372 and 1387-1389 are missing, though marinid-sultanate /ledger/27-28 and /ledger/31-32 record them with this state as counterpart and the author's notes say they were recorded on both sides. Evidence: Marinid page chronology: '1370: Third seizure of Tlemcen' and the 1387 entry 'to reconquer Tlemcen and Algiers'; Zayyanid ruler table: Abu Zayyan II 1370-1372 and 1387 between the reigns of Abu Hammu II. Fix: Add occupation_start 1370 (confidence 3, Marinid page) and occupation_end 1372 (confidence 1, ruler table), occupation_start 1387 (Tlemcen and Algiers, confidence 3) and occupation_end 1389 (confidence 1), counterpart marinid-sultanate, regions as in the Marinid ledger; add the two wars.
- `/keyframe_review/0` (for the author). The shape keeps Algiers and the Chelif from 1236 while hafsid-dynasty gains them in 1235 and again in 1410; no event explains who held them. Evidence: See hafsid-dynasty /ledger/2 and /ledger/18; this dossier records no gain or loss of Algiers. Fix: Resolve together with the Hafsid fix: a gain of Algiers from the Hafsids (year from a page) and its loss in 1410, or a correction that leaves Algiers out.

Thin (for a gap-filler):

- `/ledger/2 and /ledger/10`: Ends of the Hafsid hold (1249) and client period (1434) are confidence-1 bridges. Page to try: https://en.wikipedia.org/wiki/Yaghmurasen_Ibn_Zyan
- `/keyframe_review/5`: Cells near Cherchell leave 1512 and return 1519, unexplained. Page to try: https://en.wikipedia.org/wiki/Cherchell
- `/ledger (1509-1551)`: Spanish protectorate over Tlemcen after 1518 and the Saadian occupation of Tlemcen before 1551 have no events. Page to try: https://en.wikipedia.org/wiki/Saadi_Sultanate

Spot checks: /ledger/0 confirmed; /ledger/4 confirmed; /ledger/6 confirmed; /ledger/7 confirmed; /ledger/8 confirmed; /ledger/12 confirmed; /ledger/13 confirmed; /ledger/15 confirmed.

Area: The Zayyanid infobox has no area (re-checked).

## marinid-sultanate: fix

Findings:

- `/ledger/23 and /ledger/24` (applied by reviewer). The occupation_end of Tunisia (1357) stood before its own occupation_start (August 1357), as in the Hafsid ledger. Evidence: Hafsid page: 'captured Tunis in August 1357'; Abu Inan Faris page: 'forced to retreat from Tunisia in 1357'. Fix: Applied by the reviewer: occupation_start moved before occupation_end, its month dropped (August kept in the note). Re-validated: 0 errors, 0 warnings.
- `/ledger/16` (for the author). The 1344 loss to Castile includes Gibraltar (researcher's reading), but the dossier regains Gibraltar in 1333 (/ledger/14) and the cited page keeps Gibraltar in Marinid hands after 1344. Evidence: Marinid page: 'after its reconquest from Christian forces in 1333' and the chronology entry '1462: Ferdinand IV of Castile takes over Gibraltar'; the page dates only Algeciras to 1344. Fix: Remove Gibraltar from /ledger/16; add the loss of Gibraltar to emirate-of-granada in 1374 from a page (History of Gibraltar), or to crown-of-castile in 1462 per the Marinid page with a note on the conflict.
- `/ledger/8 and /ledger/14` (for the author). Gibraltar is gained in 1294 and again in 1333 with no loss between. Evidence: Marinid page: 'By the year 1294 they had occupied Rota, Tarifa, and Gibraltar' and the 1333 'reconquest from Christian forces'. Fix: Add the intervening loss (Castile took Gibraltar in 1309: open Siege of Gibraltar (1309)) or drop Gibraltar from /ledger/8.
- `/ledger/13` (for the author). The 1329 gain of Algeciras names crown-of-castile as the loser, but the page says only that the Marinids defeated the Castilians at Algeciras, and the dossier's own /ledger/17 has Castile taking Algeciras only in March 1344. Evidence: Marinid page: 'The Marinids defeat the Castilians in Algeciras' (1329); the dossier's /ledger/17 quotes the Abu al-Hasan page: Alfonso XI 'taking Algeciras in March 1344' (not re-opened by the reviewer). Fix: Counterpart emirate-of-granada (if a page says Granada ceded it) or nobody, confidence 2.
- `/keyframe_review/6/correction` (for the author). The 1344 shape (with the Tlemcen kingdom) is kept unchanged for 1344-1351 although the note says the Zayyanids ruled Tlemcen again from 1348. Evidence: Zayyanid page: 'Marinid occupation of Tlemcen between 1337 and 1359 (with an interruption from 1348 to 1352)'. Fix: Add a new keyframe marinid-sultanate_1348 (1348-1351) with the Morocco-only shape (Cliopatria Marinid Sultanate 1363), and limit the 1344 verdict to 1344-1347.

Thin (for a gap-filler):

- `/ledger/7`: Sijilmassa regained 1274 with no loss after 1255. Page to try: https://en.wikipedia.org/wiki/Sijilmasa
- `/ledger/6`: Rest of Morocco in 1269 is a confidence-1 bridge. Page to try: https://en.wikipedia.org/wiki/Abu_Yusuf_Yaqub_ibn_Abd_al-Haqq
- `/ledger/28 and /ledger/32`: Ends of the 1370 and 1387 occupations bridged (confidence 1). Page to try: https://en.wikipedia.org/wiki/Zayyanid_dynasty
- `/ledger/12`: Holder of Ceuta before 1309 not named. Page to try: https://en.wikipedia.org/wiki/Ceuta

Spot checks: /ledger/2 confirmed; /ledger/4 confirmed; /ledger/5 confirmed; /ledger/8 confirmed; /ledger/10 confirmed; /ledger/12 confirmed; /ledger/21 confirmed; /ledger/29 confirmed; /ledger/16 not on page.

Area: The Marinid infobox has no area (re-checked).

## Cross-dossier matrix: what did not match

- almohad-caliphate /ledger/1 1132 gain (counterpart almoravid-dynasty): missing. almoravid-dynasty (written, af-02-c) has no loss in 1121-1143 (its ledger jumps from 1118 to 1144); route the Aghmat 1132 and Rif 1139 losses to its author
- almohad-caliphate /ledger/2 1139 gain (counterpart almoravid-dynasty): missing. almoravid-dynasty (written, af-02-c) has no loss in 1121-1143 (its ledger jumps from 1118 to 1144); route the Aghmat 1132 and Rif 1139 losses to its author
- almohad-caliphate /ledger/28 1184 contest_start (counterpart almoravid-dynasty): mismatch against almoravid-dynasty /ledger/48 1184 occupation_start. type differs: almohad contest_start, almoravid occupation_start 1184-11 (Bejaia, Constantine, Algiers, Tunisia); fix listed under almohad-caliphate
- almohad-caliphate /ledger/31 1188 contest_end (counterpart almoravid-dynasty): mismatch against almoravid-dynasty /ledger/51 1188 occupation_end. type differs: almohad contest_end, almoravid occupation_end 1188
- almohad-caliphate /ledger/42 1236 loss (counterpart zayyanid-dynasty): mismatch against zayyanid-dynasty /ledger/0 1236 found. years agree; land differs: almohad hands over the whole Cliopatria Zayyanid 1236 shape (incl. Algiers and Chlef, already lost to the Hafsids in 1235), the Zayyanid found event names the Oranais
- kingdom-of-africa /ledger/0 1146 found (counterpart zirid-dynasty): mismatch against zirid-dynasty /ledger/13 1146 vassal_end. zirid-dynasty records 1146 as vassal_end with counterpart 'Tripolitania', not kingdom-of-africa; neither page names Tripoli's ruler in 1146; route to the zirid-dynasty author to name kingdom-of-africa
- hafsid-dynasty /ledger/29 1535 occupation_start (counterpart spanish-empire): missing. spanish-empire (am-06, written) has no North African event; the Tunis/La Goulette occupation 1535-1574 belongs there or in kingdom-of-spain (eu-12, not yet written); route
- hafsid-dynasty /ledger/31 1569 occupation_end (counterpart spanish-empire): missing. spanish-empire (am-06, written) has no North African event; the Tunis/La Goulette occupation 1535-1574 belongs there or in kingdom-of-spain (eu-12, not yet written); route
- hafsid-dynasty /ledger/34 1573 occupation_start (counterpart spanish-empire): missing. spanish-empire (am-06, written) has no North African event; the Tunis/La Goulette occupation 1535-1574 belongs there or in kingdom-of-spain (eu-12, not yet written); route
- hafsid-dynasty /ledger/35 1574 occupation_end (counterpart spanish-empire): missing. spanish-empire (am-06, written) has no North African event; the Tunis/La Goulette occupation 1535-1574 belongs there or in kingdom-of-spain (eu-12, not yet written); route
- marinid-sultanate /ledger/27 1370 occupation_start (counterpart zayyanid-dynasty): missing. zayyanid-dynasty (this batch) lacks the 1370-1372 and 1387-1389 occupations; fix listed under zayyanid-dynasty
- marinid-sultanate /ledger/28 1372 occupation_end (counterpart zayyanid-dynasty): missing. zayyanid-dynasty (this batch) lacks the 1370-1372 and 1387-1389 occupations; fix listed under zayyanid-dynasty
- marinid-sultanate /ledger/31 1387 occupation_start (counterpart zayyanid-dynasty): missing. zayyanid-dynasty (this batch) lacks the 1370-1372 and 1387-1389 occupations; fix listed under zayyanid-dynasty
- marinid-sultanate /ledger/32 1389 occupation_end (counterpart zayyanid-dynasty): missing. zayyanid-dynasty (this batch) lacks the 1370-1372 and 1387-1389 occupations; fix listed under zayyanid-dynasty

Totals: 151 territorial events; exception 66, matched 71, mismatch 4, missing 10. Exceptions are counterpart nobody, counterparts in the author's counterparts_needing_dossiers, or counterparts owned by groups not yet written (eu-12, me-10, other af-02 parts).

## Problems

- WebFetch answers are a model extraction of the page; quotes are as reported, and the Almohad list of conquests was re-read with a second, verbatim prompt before the fail.
- Reviewer edits made in place (all re-validated with --resolve: 0 errors, 0 warnings): hafsid-dynasty /ledger/10-11 and marinid-sultanate /ledger/23-24 (1357 start/end order), zayyanid-dynasty /identity/rulers/38/to (1557 to 1551).
- almoravid-dynasty (written in af-02-c) lacks the 1132 Aghmat and 1139 Rif losses that mirror almohad-caliphate /ledger/1-2, and records 1184-1188 as an occupation where the Almohad side has a contest.
- zirid-dynasty /ledger/13 (1146 vassal_end, counterpart 'Tripolitania') does not name kingdom-of-africa, whose found event names zirid-dynasty.
- spanish-empire (am-06) carries no North African events; hafsid-dynasty names it for the Tunis/La Goulette occupation 1535-1574; the orchestrator should decide whether kingdom-of-spain (eu-12) carries the presidios.
- Agree with the author: Cliopatria 'Almohad Caliphate' rows 1260, 1285 and 1333 are the Marinid state and should be reassigned to marinid-sultanate; 'Marinid Sultanate' 1352-1362 (737,941 km2) is wrong.
- Page budgets exceeded by the author for hafsid-dynasty (7 of 5) and zayyanid-dynasty (8 of 5); not counted against them.

## Gazetteer

Places drawn as coordinates that the gazetteer should add: Tinmel, Aghmat, Taroudannt, Tarifa, Rota, Ksar es-Seghir.
