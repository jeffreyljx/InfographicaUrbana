# Review of batch ia-02-a (mongol-empire, chagatai-khanate)

Reviewer, 2026-10-19. Machine copy: history/notes/phase-b/reviews/ia-02-a.json. Both dossiers validate (0 errors; warnings: unpaired vassal_start x4 in mongol-empire, unknown slugs ogedeid-ulus/amirate-of-qazaghan in chagatai-khanate, both listed by the author).

## mongol-empire: fail

Area: infobox 23,500,000 km2 (1294) vs Cliopatria 27,210,839 km2, ratio 1.16; acknowledged. Infobox also 4.0 M km2 (1206) vs 2.46 M (0.62) and 13.5 M (1227) vs 14.12 M (1.05); all quoted correctly in the keyframe notes.

Findings:

- `/keyframe_review/11` The 1260 keyframe (and 12-14, the 1272, 1279 and 1285 shapes) is 'ok' with Korea 99% inside, but the ledger has no Goryeo event at all, and the goryeo dossier draws Goryeo as its own state 1260-1355 (new keyframes goryeo_1260, goryeo_1270, goryeo_1290) and says the vassalage is 'recorded by the suzerain'. Evidence: Your own 1260 keyframe note lists 'Korea (99%)'; goryeo.json keyframes goryeo_1260..goryeo_1356 are adjust corrections that keep the peninsula Goryeo's; Cliopatria has no Goryeo shape 1260-1362, so the two dossiers now paint Korea twice. Mongol Empire page: 'Ogedei agreed to end the conflict with Goryeo by making it a client state' (no year). Fix: Mark keyframes 11-14 adjust with correction = the Mongol shape minus Goryeo as goryeo.json draws it (Ssangseong/Hamgyong-namdo stays Mongol from 1258; the Pyongan Dongnyeong prefecture is Mongol 1270-1290). Add vassal_start goryeo 1259 (goryeo ledger/19: 'In the spring of 1259, a peace agreement was concluded', Mongol_invasions_of_Korea) and the mirrors listed in cross_checks.
- `/ledger (Goryeo mirrors)` Five goryeo events with counterpart mongol-empire have no mirror: contest_start 1231-08, loss of Ssangseong 1258, contest_end 1259, loss of Dongnyeong (Pyongan) 1270, gain of Dongnyeong 1290. Evidence: goryeo.json ledger/16, 18, 19, 21, 23 (sources Mongol_invasions_of_Korea and Goryeo_under_Mongol_rule). Your notes leave Goryeo 'to the goryeo dossier', which is not one of the accepted exceptions: that dossier exists. Fix: Add contest_start 1231 (North Pyongan), gain 1258 (admin1 Hamgyong-namdo, North Korea), contest_end 1259, gain 1270 (region Pyongan, as goryeo ledger/21), loss 1290 (same region), with goryeo's regions and pages.
- `/ledger (Alania mirror)` alania.json dissolves into mongol-empire in February 1240 after a contest from November 1239 (both confidence 3); the Mongol ledger has no Alania event. Evidence: alania.json ledger/1-3; your notes say Alania is 'left to the alania dossier', which exists. Fix: Add contest_start 1239-11, contest_end 1240-02 and gain 1240-02 from alania with alania's region (Karachay-Cherkess, Kabardin-Balkar ...) and its source page.
- `/ledger/20` The Kipchak steppe is gained in 1236 from kimek-kipchak-confederation only; cuman-kipchak-confederation dissolves into mongol-empire in 1241 after a 1238-1241 contest and has no Mongol mirror, and kimek's own loss is 1241 (plus c1 losses to mongol-empire in 1220 and 1227). Evidence: cuman-kipchak-confederation.json ledger/3-5 (c3); kimek-kipchak-confederation.json ledger/8-13. Shapes: the 1236 shape stops at 37.8E, the 1241 shape reaches 17.4E, so the Pontic (Cuman) steppe enters only in 1241. The Central Asia page (checked) supports the 1236 Kipchak incorporation. Fix: Keep 1236 for the Volga-Ural Kipchak land (c3), add gain 1241 from cuman-kipchak-confederation (Pontic steppe) with contest 1238-1241, and either mirror kimek's 1220/1227 c1 losses or record in notes that they are kimek's to drop; flag the kimek 1241 date to its group.
- `/identity/predecessors/3` yenisei-kyrgyz dissolves into mongol-empire in 1208, after this state's founding, but the ledger has no gain; the predecessor note implies the Central Asia page covers the Kyrgyz. Evidence: yenisei-kyrgyz.json ledger/5 (dissolve 1208, c2). WebFetch of Mongol_conquest_of_Central_Asia: the page 'never mentions Yenisei Kyrgyz'; the 'late 1208 or early 1209' expedition there is against the Merkits and Naimans on the Irtysh. Fix: Add gain 1208 from yenisei-kyrgyz (cliopatria Yenisei Kyrgyz 1206) citing the page the yenisei-kyrgyz dossier used, or at confidence 1; reword the predecessor note so it does not suggest the Central Asia page dates the Kyrgyz.
- `/keyframe_review/11` Sichuan (86%) and the rest of the 1250->1260 growth in western China enter the shape with no ledger event (only Dali, Iraq and the Nizari are explained). Evidence: Keyframe 11 note: 'now including Yunnan (93%), Sichuan (86%) ...'. Mongol Empire page: 'Mongol armies captured Siyang-yang, the Yangtze and Sichuan' (no year). Fix: Add gain from southern-song of Sichuan (admin1 Sichuan, China) at confidence 1 bridged on the 1260 step, or dated from a page such as Mongol conquest of the Song dynasty.
- `/wars/13` Dai Viet war has zones [] and 'defeated both times', but ngo-dynasty records Mongol occupations of Thang Long in 1258 (counterpart mongol-empire, c3) and in Feb-Jun 1285 and Feb-Mar 1288 (counterpart 'yuan-dynasty', i.e. this dossier after the 1271 rename); there is no 1257-58 war entry. Evidence: ngo-dynasty.json ledger/21-26. Fix: Add occupation_start/occupation_end pairs (place Hanoi, km 40) for 1258, 1285 and 1288 with ngo's pages, give war 13 a Hanoi zone and extend it to 1288, and add the 1257-1258 war.
- `/wars/12` Burma war says 'No land was gained', but pagan-kingdom records a contest 1283-12 to 1284-02 and a loss of northern Burma in February 1284 to 'yuan-dynasty' (this state in 1284); champa records a Yuan occupation of Vijaya 1283-02 to 1285-06 and the Mongol dossier has no Champa war. Evidence: pagan-kingdom.json ledger/8-10; champa.json ledger/29-30. Fix: Either add gain 1284 from pagan-kingdom (pagan's region) with contest 1283-1284 and an occupation pair for Vijaya 1283-1285 with a Champa war, or state on a page why not; ask the pagan, champa and ngo groups to write mongol-empire, not yuan-dynasty, for events before 1294.
- `/ledger/22` Counterpart 'Rus' principalities' (ledger/22-24) is not a slug, although Cliopatria has rows for each principality, all ending in 1240 with their land inside the 1241 Mongol shape. Evidence: polities.csv: principality-of-ryazan, principality-of-rostov-suzdal, principality-of-chernigov, principality-of-kiev, principality-of-pereyaslavl, principality-of-turov-and-pinsk, principality-of-galicia-volhynia (and halych-volhynia-occupation) all end 1240; war 4 already uses some of these slugs. Fix: Split ledger/22-24 into one event per principality slug so the eu-16 dossiers can mirror them; decide (and say in keyframe 8's note) whether that land is Mongol land or a vassal tint.
- `/identity/capitals/2` Khanbaliq from 1261 has no year on the page; the page's infobox keeps Karakorum to 1271 and Kublai's 1260 kurultai was at Kaiping. Evidence: Mongol Empire page: infobox 'Karakorum (1235-1271)'; 'Kublai moved his headquarters to Khanbaliq' (no year); 'he summoned his own kurultai at Kaiping'. Fix: Follow the infobox (Karakorum 1235-1271, Khanbaliq 1271-1293) or add Kaiping/Shangdu 1260-1271, and say which in the note.
- `/ledger/36` [APPLIED by reviewer] capital_move 1260 was at confidence 2 although the page gives no year for the move to Khanbaliq. Evidence: Mongol Empire page, checked: 'Kublai moved his headquarters to Khanbaliq ...' with no year; infobox Karakorum to 1271. Fix: Confidence lowered to 1 by the reviewer (note appended).
- `/identity/rulers/4` [APPLIED by reviewer] Kublai Khan's span ran to 1294, after the dossier's end year 1293. Evidence: Brief section 2.2: rulers inside the life; dossier end 1293. Fix: 'to' set to 1293 by the reviewer (note appended).
- `/wars/9` Ain Jalut outcome says 'No border changed', but the page has Hulagu's 'successful military advance into Syria' broken off in 1259-1260: Syria was held for part of 1260. Evidence: Mongol Empire page, checked: 'Hulagu broke off his successful military advance into Syria'; Aleppo and Damascus are not named there. Fix: Add an occupation pair for northern Syria in 1260 from a page that dates it (Battle of Ain Jalut or Mongol invasions of the Levant) with a zone, or drop the 'no border changed' claim.

Gaps for a gap-filler (thin):

- `/ledger/7` Start of the Khwarazm war (1218, c1; the war began 1219) (try https://en.wikipedia.org/wiki/Mongol_invasion_of_the_Khwarazmian_Empire)
- `/ledger/8` End of the Qara Khitai and the Semirechye gain (1220, c1; ledger/9 too) (try https://en.wikipedia.org/wiki/Qara_Khitai)
- `/ledger/21` Volga Bulgaria conquest year (1236, c1) (try https://en.wikipedia.org/wiki/Mongol_invasion_of_Volga_Bulgaria)
- `/ledger/27` Tibet under the Mongols (1250, c1) (try https://en.wikipedia.org/wiki/Mongol_conquest_of_Tibet)
- `/ledger/28` Sultanate of Rum vassalage (1250, c1; Kose Dag is 1243) (try https://en.wikipedia.org/wiki/Battle_of_K%C3%B6se_Da%C4%9F)
- `/ledger/29` Georgian submission (1250, c1) (try https://en.wikipedia.org/wiki/Mongol_invasions_of_Georgia_and_Armenia)
- `/ledger/33` Dali annexation 1260 (c1, ledger/34 too) (try https://en.wikipedia.org/wiki/Mongol_conquest_of_the_Dali_Kingdom)
- `/keyframe_review/14` The 1285 shape loses 0.2 M km2 against 1279 (unverified: page budget) (try https://en.wikipedia.org/wiki/Yuan_dynasty)
- `/identity/rulers` Regency gaps 1227-1229, 1241-1246, 1248-1251 (Tolui, Toregene, Oghul Qaimish) not shown (try https://en.wikipedia.org/wiki/List_of_khans_of_the_Mongol_Empire)

Spot checks:

- `/ledger/11` https://en.wikipedia.org/wiki/Mongol_conquest_of_Central_Asia: confirmed: 'by 1221 all the territories of the former Khwarazmian Empire'
- `/ledger/6` https://en.wikipedia.org/wiki/Mongol_conquest_of_Central_Asia: confirmed: 'By 1218 the Mongols controlled all of Xinjiang'; Kuchlug killed 1218 in Badakhshan
- `/ledger/20` https://en.wikipedia.org/wiki/Mongol_conquest_of_Central_Asia: confirmed: 1236, Batu 'incorporated the Kipchak lands in Central Asia, Eastern Europe, and Western Siberia'
- `/ledger/18` https://en.wikipedia.org/wiki/Mongol_conquest_of_the_Jin_dynasty: confirmed: 'the Jin dynasty came to an end on February 9, 1234'; infobox 'North China annexed'
- `/ledger/4` https://en.wikipedia.org/wiki/Mongol_conquest_of_the_Jin_dynasty: confirmed: 'Zhongdu fell to the Mongols on June 1, 1215'
- `/ledger/13` https://en.wikipedia.org/wiki/Mongol_conquest_of_the_Jin_dynasty: confirmed: resistance rooted out in Shanxi, Hebei and Shandong 1217-1223
- `/ledger/32` https://en.wikipedia.org/wiki/Mongol_Empire: confirmed: Baghdad 'besieged and captured by the Mongols in 1258'
- `/ledger/30` https://en.wikipedia.org/wiki/Mongol_invasions_and_conquests: confirmed: 'made the Kingdom of Dali into a vassal state in 1253' (and Mongol Empire page)
- `/ledger/40` https://en.wikipedia.org/wiki/Mongol_invasions_and_conquests: confirmed: 'defeating the Song dynasty in 1279'
- `/ledger/15` https://en.wikipedia.org/wiki/Mongol_invasions_and_conquests: confirmed: Western Xia subjugated 1209, destroyed 1227
- `/ledger/38` https://en.wikipedia.org/wiki/Mongol_Empire: confirmed: edict of 18 December 1271
- `/ledger/31` https://en.wikipedia.org/wiki/Mongol_Empire: confirmed: Ismaili strongholds destroyed 1257, Girdkuh to 1271
- `/ledger/36` https://en.wikipedia.org/wiki/Mongol_Empire: no year on page for Khanbaliq; confidence lowered to 1

## chagatai-khanate: thin

Area: infobox 3,400,000 km2 (1310) vs Cliopatria 2,460,790 km2, ratio 0.72; acknowledged. Infobox '1310 or 1350 est.'; keyframe 0 quotes it correctly.

Findings:

- `/ledger/6` [APPLIED by reviewer] The 1361 gain of Transoxiana (c3) cited the Chagatai Khanate page, which dates the conquest 1360, not 1361. Evidence: Chagatai page: 'In 1360, Tughlugh invaded Transoxania and conquered it' (no 1361). Tughlugh Timur page: 'In 1361, however, Tughlugh Timur and his army rode into the region for the second time' ... 'appointed his son Ilyas Khoja as viceroy of Transoxiana'. Fix: Source moved to the Tughlugh Timur page and the note now quotes its 1361 sentences (reviewer).
- `/wars/0` [APPLIED by reviewer] War 'Kaidu and Duwa against the Yuan' started in 1275, before the dossier's first year 1294. Evidence: Brief section 2.2: wars inside the life. Fix: 'from' clipped to 1294 by the reviewer, the 1275 start kept in the note.
- `/ledger (Yuan vassal pair)` No vassal_start yuan-dynasty, although the page dates the submission and Cliopatria has the relation row (Allegiance of Chagatai Khanate to Yuan Dynasty, 1294-1374); the notes put it out of scope as 'the vassal_start belongs to yuan-dynasty'. Evidence: Chagatai page, checked: 'both Duwa and Kaidu's son Chapar recognized Yuan authority in 1303'. Brief section 2.3: a vassal_start of X is mirrored by a vassal_start in X's ledger. Fix: Add vassal_start 1303 (counterpart yuan-dynasty, region the whole khanate, c3) and a vassal_end from a page (the relation row ends 1374; the 1346 split or the Yuan fall are candidates), so the ea-06 yuan-dynasty dossier can mirror it.
- `/ledger (Qocho mirror)` qocho-kingdom records vassal_start to chagatai-khanate in 1335 and vassal_end plus dissolve into chagatai-khanate in 1370 (all c1); this ledger has neither. Evidence: qocho-kingdom.json ledger/10-12. Turfan enters this row's shape in 1363 (bbox east edge 90.83 to 92.69), where this ledger has a confidence-1 gain from 'nobody'. Fix: Agree one version with the qocho-kingdom group: either mirror (vassal_start 1335, vassal_end and gain 1370 of Turfan-Hami, c1) or have qocho drop them; consider qocho-kingdom as counterpart of the 1363 Turfan step.
- `/keyframe_review/5` The new keyframe 1360-1362 paints Transoxiana from 1360 while the ledger has contest 1360-1361 and the gain in 1361. Evidence: Ledger/4-6; Tughlugh Timur page: first invasion March 1360, second 1361 with Ilyas Khoja installed. Fix: Start the keyframe in 1361 (shape_id chagatai-khanate_1361) or move the gain to 1360 citing the Chagatai page.
- `/identity` The row holds the undivided khanate to 1346 and the eastern Moghul khanate 1347-1462 in one dossier; the page's infobox ends the Chagatai Khanate in 1347 and the Moghulistan page treats 1462 as a split of the same khanate (reunited 1469), not an end. Evidence: Chagatai page infobox: 'Disestablished: 1347'. Esen Buqa II page: 'His death caused a split amongst the Moghuls'. Research brief section 6: one dossier per state. Fix: No change needed now; the orchestrator should settle with the moghulistan author (ia-02) whether 1347-1462 stays here (Cliopatria break, as written) or moves to moghulistan, so the 1462 dissolve and the moghulistan found agree.

Gaps for a gap-filler (thin):

- `/ledger/0` Start of the khanate as a separate state (1294 bridged on Cliopatria; infobox 'Independent Khanate (1266-1347)') (try https://en.wikipedia.org/wiki/Duwa)
- `/ledger/8` The 1363 Tarim step (+0.23 M km2), gain from 'nobody' at c1 (try https://en.wikipedia.org/wiki/Dughlat_tribe)
- `/ledger/10` Timur's 1395 step (-0.12 M km2), c1 (try https://en.wikipedia.org/wiki/Timurid_conquests_and_invasions)
- `/ledger/11` The Oirat step of 1422 (-0.22 M km2: Dzungaria), c1 (try https://en.wikipedia.org/wiki/Oirats)
- `/ledger/15` End of the 1451-52 Tashkent campaign, c1 (try https://en.wikipedia.org/wiki/Esen_Buqa_II)
- `/keyframe_review/0` Afghan south of the 1294 shape (Kabul, Badakhshan, Gilgit) has no page; the Chagatai page places Dawud Khoja in eastern Afghanistan (1315 context), and the Duwa page says 'The northeast part of Duwa's realm was ceded to the Yuan dynasty' (undated, no ledger loss) (try https://en.wikipedia.org/wiki/Qara%27unas)
- `/identity/rulers` Rulers strip omitted (try https://en.wikipedia.org/wiki/List_of_Chagatai_khans)
- `/identity/capitals` Qarshi as second capital (years) (try https://en.wikipedia.org/wiki/Kebek)

Spot checks:

- `/ledger/4` https://en.wikipedia.org/wiki/Tughlugh_Timur: confirmed: 'invaded in March 1360'
- `/ledger/6` https://en.wikipedia.org/wiki/Chagatai_Khanate: mis-dated against its cited page (page: 1360); the Tughlugh Timur page gives 1361; source corrected by reviewer
- `/ledger/7` https://en.wikipedia.org/wiki/Chagatai_Khanate: confirmed: 'Following Tughlugh's death in 1363, Timur and Amir Husayn took over Transoxiana'; infobox 'Western portion annexed by Timur: 1363'
- `/ledger/2` https://en.wikipedia.org/wiki/Chagatai_Khanate: confirmed: 'In 1346 a tribal chief, Amir Qazaghan, killed Qazan'
- `/ledger/1` https://en.wikipedia.org/wiki/Chagatai_Khanate: confirmed: Yuan recognized 1303, Chapar surrendered his territory to Duwa in 1306
- `/ledger/13` https://en.wikipedia.org/wiki/Esen_Buqa_II: confirmed: Kashgar 'retaken in 1435'
- `/ledger/14` https://en.wikipedia.org/wiki/Esen_Buqa_II: confirmed: 'In 1451 he attacked Tashkent'
- `/ledger/16` https://en.wikipedia.org/wiki/Esen_Buqa_II: confirmed: died 1462; split between Yunus Khan and Dost Muhammad

## Cross-dossier matrix

- mongol-empire 1206 found (nobody) -> naiman 1204 dissolve: **exception**. naiman (1204), kerait (1203) and merkit (1200) dissolve into mongol-empire before it is founded; listed as predecessors. Their groups should use the found link, not a dissolve counterpart that does not exist yet.
- yenisei-kyrgyz 1208 dissolve (mongol-empire) -> mongol-empire - gain: **missing**. No gain in mongol-empire; finding /identity/predecessors/3.
- mongol-empire 1209 vassal_start (western-xia) -> western-xia - vassal_start: **exception**. western-xia (ea-05) not written yet; also 1227 vassal_end and gain.
- mongol-empire 1209 vassal_start (qocho-kingdom) -> qocho-kingdom 1209 vassal_start: **matched**. qocho ledger/8. qocho's vassal_end 1335 still names mongol-empire after its 1293 end: qocho group should hand it to yuan-dynasty/chagatai-khanate at 1294.
- mongol-empire 1215 gain (great-jin) -> great-jin - loss: **exception**. great-jin (ea-05) not written; also contests 1211-1223, 1230-1234 and gains 1223, 1234. Author flags the Cliopatria Jin row to 1235.
- mongol-empire 1216 contest_start (kara-khitans) -> kara-khitans 1216 contest_start: **matched**. contest_end 1220 matched too.
- mongol-empire 1218 gain (kara-khitans) -> kara-khitans - loss: **mismatch**. kara-khitans has no 1218 loss (contest to 1220, dissolve 1220); page confirms 'By 1218 the Mongols controlled all of Xinjiang'. Route to kara-khitans group; flagged by author.
- mongol-empire 1220 gain (kara-khitans) -> kara-khitans 1220 dissolve: **matched**. 
- mongol-empire 1221 gain (khwarezmid-empire) -> khwarezmid-empire - loss: **exception**. me-09 not written; also contest 1218-1221. Author flags the Cliopatria row to 1235.
- kimek-kipchak-confederation 1220 loss (mongol-empire) -> mongol-empire - gain: **missing**. kimek c1 losses 1220 and 1227 to mongol-empire unmirrored.
- mongol-empire 1236 gain (kimek-kipchak-confederation) -> kimek-kipchak-confederation 1241 loss: **mismatch**. 5 years apart; kimek also has contest 1236-1241. Finding /ledger/20.
- mongol-empire 1236 gain (volga-bulgaria) -> volga-bulgaria - loss: **exception**. no dossier yet (c1 bridge).
- mongol-empire 1237 contest_start (Rus' principalities) -> principality-of-ryazan - contest_start: **mismatch**. counterpart is not a slug; eu-16 dossiers not written. Finding /ledger/22.
- cuman-kipchak-confederation 1241 dissolve (mongol-empire) -> mongol-empire - gain: **missing**. also contest 1238-1241 unmirrored. Finding /ledger/20.
- alania 1240 dissolve (mongol-empire) -> mongol-empire - gain: **missing**. also contest 1239-11 to 1240-02. Finding /ledger (Alania mirror).
- mongol-empire 1241 contest_start (kingdom-of-hungary) -> kingdom-of-hungary - contest_start: **exception**. eu-15 not written.
- mongol-empire 1250 gain (tibetans) -> tibetans - loss: **exception**. ea-04 not written; c1. Rum and Georgia vassal_start 1250 likewise (not written).
- mongol-empire 1253 vassal_start (kingdom-of-dali) -> kingdom-of-dali - vassal_start: **exception**. not written; 1260 vassal_end/gain likewise.
- mongol-empire 1257 gain (Nizari Ismaili state) -> nizari-ismaili-state - loss: **exception**. listed under counterparts_needing_dossiers.
- mongol-empire 1258 gain (abbasid-caliphate) -> abbasid-caliphate - loss: **exception**. me-08 not written.
- goryeo 1231 contest_start (mongol-empire) -> mongol-empire - contest_start: **missing**. also contest_end 1259. Finding /ledger (Goryeo mirrors).
- goryeo 1258 loss (mongol-empire) -> mongol-empire - gain: **missing**. Ssangseong.
- goryeo 1270 loss (mongol-empire) -> mongol-empire - gain: **missing**. Dongnyeong; and goryeo gain 1290 needs a Mongol loss 1290.
- ngo-dynasty 1258 occupation_start (mongol-empire) -> mongol-empire - occupation_start: **missing**. Thang Long 1258; also 1285 and 1288 occupations that ngo names 'yuan-dynasty' (this dossier before 1294).
- pagan-kingdom 1284 loss (yuan-dynasty) -> mongol-empire - gain: **mismatch**. pagan names yuan-dynasty, whose Cliopatria row starts 1294; this dossier's war 12 says no land gained.
- champa 1283 occupation_start (yuan-dynasty) -> mongol-empire - occupation_start: **mismatch**. Vijaya 1283-1285; no Champa war or event here.
- mongol-empire 1260 contest_start (Ariq Böke) -> ariq-boke - contest_start: **exception**. listed under counterparts_needing_dossiers.
- mongol-empire 1279 gain (southern-song) -> southern-song - loss: **exception**. ea-05 not written; also 1276.
- mongol-empire 1293 dissolve (yuan-dynasty) -> chagatai-khanate 1294 found: **matched**. Chagatai found 1294 from mongol-empire; yuan-dynasty, golden-horde, ilkhanate not written (exception).
- chagatai-khanate 1306 merge (ogedeid-ulus) -> ogedeid-ulus - merge: **exception**. listed under counterparts_needing_dossiers.
- chagatai-khanate 1346 split (amirate-of-qazaghan) -> amirate-of-qazaghan - split: **exception**. listed; also 1360-1361 contest, 1361 gain, 1363 loss.
- qocho-kingdom 1335 vassal_start (chagatai-khanate) -> chagatai-khanate - vassal_start: **missing**. and qocho vassal_end + dissolve 1370 into chagatai-khanate; all c1 on qocho's side.
- chagatai-khanate 1303 vassal_start (yuan-dynasty) -> yuan-dynasty - vassal_start: **missing**. Not written on either side; the Chagatai page dates it 1303; yuan-dynasty (ea-06) not written.
- chagatai-khanate 1395 loss (timurid-empire) -> timurid-empire - gain: **exception**. ia-02 part not written; also 1429 loss, 1435 gain, 1451-1452 contest.
- chagatai-khanate 1422 loss (four-oirats) -> four-oirats - gain: **exception**. ia-02 part not written.
- chagatai-khanate 1462 dissolve (moghulistan) -> moghulistan - found: **exception**. ia-02 part not written; see the identity note on the 1347/1462 boundary.

## Problems and routing

- No page failed to load. Neighbour dossiers read (ledgers grepped): goryeo, alania, kara-khitans, qocho-kingdom, kimek-kipchak-confederation, cuman-kipchak-confederation, naiman, kerait, merkit, yenisei-kyrgyz, ngo-dynasty, pagan-kingdom, champa, empire-of-trebizond, nicaean-empire. Of the section-6 Context list only empire-of-trebizond, goryeo, ngo-dynasty and nicaean-empire exist; the rest belong to groups that have not run.
- Routing: pagan-kingdom, champa and ngo-dynasty name 'yuan-dynasty' for events of 1283-1288; Cliopatria's yuan-dynasty starts in 1294 and this batch records Kublai's state to 1293 as mongol-empire (rename 18 Dec 1271). The orchestrator should tell those groups to use mongol-empire before 1294, or have mongol-empire mirror them.
- Routing: kara-khitans (Xinjiang lost 1218 per the Central Asia page, no loss in its ledger), kimek-kipchak-confederation (loss 1241 vs Mongol gain 1236), qocho-kingdom (vassal_end 1335 still names mongol-empire, which ends 1293).
- Reviewer applied 4 small fixes (mongol-empire /identity/rulers/4 and /ledger/36; chagatai-khanate /ledger/6 and /wars/0); both files re-validated with 0 errors and were read back.
