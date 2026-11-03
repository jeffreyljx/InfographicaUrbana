# ea-06-x (Yuan, additions batch): notes

Written 2026-10-24 by the Phase B agent for ea-06-x. Twelve new dossiers (cliopatria_names [] for all; every keyframe is new, verdict adjust): the Red Turban states (tianwan, han-song, chen-han, ming-xia, zhang-shicheng-s-wu, fang-guozhen-s-regime, ispah-rebellion), Zhu Yuanzhang's Wu (zhu-yuanzhang-s-wu), and the Yuan-era regimes Cliopatria lacks in Tibet and Yunnan (sakya-regime, mangyul-gungthang, principality-of-liang-yunnan, duan-governors-of-dali). All validate with python3 -I tools/validate_dossier.py --resolve (0 errors, 0 warnings). 23 distinct Wikipedia pages are cited (three more were opened and not used: Naghachu, Kaidu, and the Han-dynasty article that the title Principality_of_Liang leads to). Three URLs failed: Han_Lin'er with a raw apostrophe (retried as Han_Lin%27er), Wu_(Zhu_Yuanzhang) and Principality_of_Liang (wrong article); none of the dossiers cites them.

Method note for the reviewer: WebFetch returns a model's summary of the page. Text inside quotation marks in a note was kept only where the summary itself gave it in quotation marks; every other sentence of the pages is paraphrased without quotation marks (a script stripped the rest). No area figures exist on any of these pages (the infobox Area is "not given" for Chen Han, Ming Xia, Tianwan, Zhou, Wu and Mangyul Gungthang), so no keyframe could be compared with a figure; all shapes are circles round named cities or province unions.

## Cross-cutting

- yuan-dynasty (ea-06-a) and ming-dynasty (Ming group) are cited as counterparts throughout. The Yuan dossier should carry the relations that only the suzerain can record (vassal_start/vassal_end, counterpart = the vassal): Zhang Shicheng's submission (late 1357 to 1363, counterpart zhang-shicheng-s-wu), Fang Guozhen's titles from 1356, the Sakya regime (1264-1358, counterpart sakya-regime), the Duan governors of Dali (1256-1381, counterpart duan-governors-of-dali).
- The Ming dossier should list zhu-yuanzhang-s-wu as its first phase (same state and ruler; the Wu ends with the Ming proclamation, 23 January 1368 on the Hongwu Emperor and Ming pages, 12 January on the Red Turban page) and ming-xia (1371) and the principality of Liang and the Duan governors (1382-1383) as conquests. Cliopatria's Ming row starts in 1375.
- Tibet (ea-06-b): its 1354 and 1358 events name yuan-dynasty as counterpart; they should name sakya-regime. Its 1619 gain of Mangyül Gungthang uses the same circle as mangyul-gungthang here.
- The Red Turban Rebellions page is the umbrella; each rebel dossier lists it as a war with empty zones.

## tianwan (1351-1360)
- Pages: Tianwan (Xu Shouhui), Red Turban Rebellions, Chen Han, Ming Xia. Qishui or Qizhou for the first seat (pages differ); the Wuhan cities lost in 1352 (Red Turban page) or after Toqto'a's autumn 1353 campaign (Tianwan page); capital Hanyang from 1353 (infobox) or the winter of 1355/56 (text).
- The Tianwan page puts Ni Wenjun's January 1355 conquest at "Mianyang in Sichuan"; it is not mapped. The loss of the Yangtze and Jiangxi cities in 1353-55 is confidence 1. "Later parts of Shaanxi" are not placed.
- Sichuan under Ming Yuzhen is a vassal of Tianwan 1357-1360 (counterpart ming-xia).

## han-song (1355-1367)
- No Wikipedia article for the regime; read from Han Lin'er, Liu Futong, Red Turban Rebellions, Hongwu Emperor. Infobox era Longfeng 1355-1366, reign to January 1367 (used).
- The year of the Shandong province (somewhere in 1356-1359), what became of it, and the route of the 1357-58 expedition are not on the pages (confidence 1 for the Shandong gain of 1357 and loss of 1362). The Song court at Chuzhou from June 1363 lies inside Zhu's territory; render it as the vassal tint (vassal_start May 1356 to January 1367, counterpart zhu-yuanzhang-s-wu).

## chen-han (1360-1364)
- Chen Han page infobox: Jiujiang then Wuchang, 1360-1364. The Red Turban page's line that Chen's state "took Chongqing and held all of Sichuan" in 1357-59 conflicts with the Tianwan and Ming Xia pages and is not used. Anqing (retaken August 1361) is in the contest zone only.

## ming-xia (1360-1371)
- Start: infobox 1362; the page also dates the Longshu kingship 1360 or 1362; Sichuan was Ming Yuzhen's from 1357. The dossier starts in 1360 (confidence 2). The page names "Wenzhou" and "Mianzhou" for May 1371 (Mianzhou read as Mianyang; Wenzhou not mapped). No capital is named for 1360-61.

## zhang-shicheng-s-wu (1354-1367)
- Revised 2026-10-24 after the review (shapes made disjoint from Zhu's, Anfeng mirrored): see 'Repairs after the review' at the end.
- Wikipedia splits it into Zhou (1354-1357) and Wu (1363-1367); here one state with renames in 1357 and 1363. Disagreements: Yangzhou's capture (1354 on the Zhang page, a failed Yuan attack in summer 1354 on the Zhou page); Zhang Shide's death (1357 in Zhu's prison on the Red Turban page, 1366 after a fall on the Zhang page); Hangzhou (attempt failed 1356; taken 1363; taken by Zhu December 1366).
- Not on the pages: the cities of the 1366 northern campaign and of Zhang's Zhejiang territory; northern Jiangsu and "influence as far as Shandong" are undated (confidence 1 for those events).

## fang-guozhen-s-regime (1348-1367)
- Start 1348 (flight to the islands) although the page gives land only "by 1356"; the 1356 gain is confidence 1. A gap-filler could start the state in 1356. No capital is named on any page (Ningbo is a flagged reading). The northern Fujian stretch of the coast (Red Turban page) is not mapped.

## zhu-yuanzhang-s-wu (1356-1368)
- Revised 2026-10-24 after the review (Nanjing circle cut back at the Yangtze, Jiujiang/Anqing, Anfeng and Chuzhou mirrors, Huguang from 1365): see 'Repairs after the review' at the end.
- No article for the state (the Hongwu Emperor page is the source). Shapes are rough: Wannan and inland Zhejiang are circles; the dates of the 1356-1359 conquests are not on the pages (the 1359 and 1366 gains are confidence 1). The Hongwu page also says Zhu "occupied southern Jiangxi" in 1355-57, which conflicts with the Chen Han page's Jiangxi surrender of 1362 and is not used. Titles: Duke of Wu 1361, King of Wu 4 February 1364.

## sakya-regime (1264-1358)
- Requested by the ea-06-b report as "Sakya regime under the Yuan, 1354-1358"; widened to 1264 (Sakya page: Kublai gave Phagpa the rule of Tibet in 1264). The Tibet under Yuan rule infobox ends Yuan rule in 1354, its text and the Phagmodrupa page give 1358 / 1354-1358. The shape is Ü-Tsang as the Tibet dossier draws it; Kham and Amdo were Yuan Routes. No ruler list was found. Mangyül Gungthang is its vassal (c. 1265 to 1358; the end date is a bridge, confidence 1).
- Counterpart Drikung Kagyu (1285-1290 revolt) has no dossier.

## ispah-rebellion (1357-1366)
- A rebellion article, not a state (infobox: Quanzhou Persian Shi'a army, Dates 1357-1366, Result Yuan victory, capital not stated); written as a rebel state because it held Quanzhou for nine years. The extent beyond Quanzhou and Putian, the dates of Putian and Fuzhou, and the date of the massacre are not on the pages. Chen Youding's Yuan-loyal Fujian (1366-67) is not a separate dossier.

## principality-of-liang-yunnan (1368-1382)
- No article for the principality (the Basalawarmi page links to a "Liang (realm)" article, section Yuan Principality, not opened). The start 1368 is when the Yuan left China proper; the grant of the title and the Northern Yuan khan's confirmation are undated. The Dali district is left out (Duan realm). Ming troops 250,000-300,000 (two pages).

## mangyul-gungthang (c. 1265-1619)
- From the ea-06-b counterpart list. The infobox ends the kingdom in 1620, the Tsangpa and Karma Phuntsok Namgyal pages in 1619 (used). Extent, rulers and partitions are not on the pages: one circle round Gyirong (the Tibet dossier's) stands for 354 years. The Tsangpa page does not name Gungthang among the 1612-13 conquests; the Karma Phuntsok Namgyal page does.

## duan-governors-of-dali (1256-1383)
- Covers the gap between Cliopatria's Kingdom of Dali (ends 1259; the kingdom-of-dali dossier ends 1256) and the Ming conquest. The Dali page says the Duan "governed Yunnan's various indigenous peoples", which would be far wider than the 120 km circle drawn; the end is 1382 (realm crushed) or February 1383 (Dengchuan).

## Not written (gaps)
- Naghachu's Liaodong holdout (Mongol warlord, to 1387): the Naghachu page gives no seat, no independence date and no infobox ("dominance over Mongol tribes across a wide area, including much of Rehe and Liaoning" by the mid-1380s), so it could not be dated; page silent.
- Kaidu's Ögedeid realm is already in ogedeid-ulus (ia-02); the Okinawan Sanzan in chuzan, hokuzan, nanzan; Qocho and Kumul have dossiers.

## Repairs after the review (2026-10-24, zhu-yuanzhang-s-wu and zhang-shicheng-s-wu, both verdict fail)

Pages re-opened with WebFetch for this pass: Chen Han, Liu Futong, Han Lin'er, Red Turban Rebellions, Hongwu Emperor, Wu (Zhang Shicheng), Zhou (Zhang Shicheng), Xu Da. Both dossiers validate with --resolve (zhu 26 events, 9 keyframes, 9 sources; zhang 18 events, 4 keyframes, 8 sources; 0 errors, 0 warnings). A year-by-year gazetteer intersection of all keyframes now gives 0 shared cells between zhu-yuanzhang-s-wu and zhang-shicheng-s-wu for 1354-1366 and 0 between zhu and han-song for 1363-1366 (the 1367 overlaps are the end-year transitions: Suzhou taken in October, the Song ending in January). Mirrored events were checked cell by cell: the 1366 Zhang losses and Zhu gains are equal sets.

Applied:
- Blocking, the double-held Yangtze land. The review found the Nanjing 100 km circle and the Yangzhou 100 km circle sharing 89-100 cells every year 1356-1365. Zhang's north-bank district is now three circles (Gaoyou 50 km, Taizhou 40 km, Xinghua 40 km; the first reaches Yangzhou on the north bank and stops short of Zhenjiang and Yizheng), and Zhu's circle is {minus: [Nanjing 100 km, that district]} in all keyframes, /ledger/0, /ledger/20 and identity. Three more Zhang pieces met Zhu's shape and were cut back (the review did not list them): Changzhou 60 km against Zhu's Nanjing district and southwestern Jiangsu (17 and 8 cells), the northern Jiangsu circle against Zhu's Nanjing district (23 cells), and Hangzhou 60 km against Zhu's inland-Zhejiang circle (10 cells). The same specs are used in Zhu's gains of 1366, so the mirrors stay equal.
- 1361 Jiujiang and Anqing (zhu): added the gain (1361, conf 2) and the loss (August 1361, conf 3) mirroring chen-han /ledger/4-5, from the Chen Han page.
- 1363 Anfeng: zhang gains it in February 1363 (conf 3, Liu Futong page) and loses it to zhu in March 1363 (conf 1); zhu gains it in March 1363 (conf 1) and its shape holds a 60 km Anfeng circle from 1363; the dissolve region and the Ming successor land carry it.
- 1363 and 1367 Chuzhou (zhu): loss of the 40 km court-seat circle to han-song in June 1363 (conf 1), gain back in January 1367 (conf 2), and the circle is carved out of Zhu's keyframes for 1363-1366.
- Huguang (zhu): the old 1364-1365 keyframe is split; 1364 holds the Wuchang circle only (ledger /9), 1365 holds Huguang (ledger /11, April 1365, Chen Han page: the occupation of Hubei, Hunan and Jiangxi 'dragged on until April 1365'). Keyframe 1362-1363 is also split (1362 / 1363) so the Chuzhou carve-out starts in 1363.

Where I disagree with the reviewer, or with my first version:
- The reviewer's example for Zhang, {minus: [Yangzhou 100, Nanjing 100]}, was not used: Yangzhou is 69 km from Nanjing, so it would take Yangzhou city out of Zhang's shape although the Zhang Shicheng page and /ledger/1 give it to Zhang. (The Zhou page disagrees: it has only the failed Yuan attack of summer 1354 and says nothing of Zhang holding Yangzhou; the keyframe follows the Zhang Shicheng page, as before.)
- Anfeng loss to Zhu: the review asked for confidence 2. I used 1. The Liu Futong page says Zhu and Xu Da 'rescued Han Lin'er in March'; the Liu Futong, Han Lin'er, Hongwu Emperor, Red Turban and Wu pages are all silent on who held Anfeng afterwards, so the transfer is bridging a silence. The attack is February 1363 on the Liu Futong page and January 1363 on the Hongwu Emperor page (the mirror in han-song uses February).
- Chuzhou: I took the review's first option (loss and gain back) because han-song is not touched in this pass, but the pages argue for the second. The Red Turban page says Zhu gained Chuzhou in 1353 and that the court 'continued to exist in safety' there; the Han Lin'er page does not say who controlled Chuzhou and gives no month for the move (it follows Chen Youliang's attack of June 1363, so June is the earliest month; han-song's June 1363 and the month 6 used here rest on that). Zhu did not lose control of Chuzhou on any page. A gap-filler should prefer: han-song drops its 1363 gain and the Chuzhou land of its dissolve and keeps Chuzhou as a capital only; then delete here the 1363/6 loss, the 1367/1 gain and the Chuzhou carve-out (keyframes 1363-1366, circle {lon 118.32, lat 32.3, km 40}).
- Jiujiang/Anqing: the review asked for a Jiujiang-only gain and a loss of Jiujiang plus Anqing. A loss of land never gained is incoherent, so both events map Jiujiang 60 km and Anqing 80 km. The Chen Han page says the Han were 'retaking Jiujiang and Anqing in August 1361' (so Zhu held both) and nowhere says how Zhu got Anqing, which is why the gain is confidence 2. chen-han /ledger/5 maps Jiujiang only; its Anqing part stays unmirrored until that dossier maps Anqing.
- Anqing is also the one place where zhu's shape does not follow the ledger: the 1360-1361 keyframe has no Jiujiang or Anqing circle (it held them for weeks, and Jiujiang from September), as before.

Thin items, not improved: the Xu Da page is silent on every campaign of 1355-1367 asked about (it gives only 1353, 1368 and 1370); the Zhou page is silent on defeats by Zhu in 1356-1357 and does not date northern Jiangsu; the Wu page names no city of 1366 except the Suzhou siege (December 1366 to October 1367); the Hongwu Emperor page is silent on Zhu taking Zhenjiang, Changzhou, Yangzhou, Chizhou, Huizhou or Ningguo and gives only the holding 'in the beginning of 1360'. The 1356-1359 conquests, Changzhou's loss before 1362, northern Jiangsu in 1363 and the 1366 cities north of the Yangtze and at Huzhou therefore stay at confidence 1.

Overlaps left alone (outside the findings, in dossiers that passed): zhu and fang-guozhen-s-regime share 12 cells in 1358-1366 (Fang's Shaoxing circle against Zhu's inland-Zhejiang circle) and zhang and fang share 14 (17 before this pass) in 1363-1365; zhu and chen-han share 10 cells in 1360-1361 and zhu and tianwan 10 in 1360 (Zhu's Wannan circle against the Han and Tianwan Jiangxi/Huguang regions). The Suzhou mirror is not equal (Zhu gains a 120 km circle, Zhang's last shape is 90 km); that was matched by the review and is unchanged.

Gazetteer names used by coordinate in this pass: Xinghua, Jiangsu (32.91 N 119.84 E) and Taizhou, Jiangsu (32.49 N 119.90 E; the gazetteer's single Taizhou resolves there but is ambiguous with Taizhou in Zhejiang).

