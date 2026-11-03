# Review of batch ea-02-a (Qin and Han, part a)

Reviewer run of 2026-10-19. Dossiers: qin-dynasty, western-chu, dai, zhai, chang-shan, jibei. Author report history/notes/phase-b/reports/ea-02-a.json and notes history/polities/_notes/ea-02-a.md read first.

Mechanical: the validator (with --resolve) gives 0 errors and 0 warnings for all six, before and after the reviewer's edits. Cliopatria names match polities.csv; every shape has a verdict; new keyframes carry from, to and a correction. The author's one-state-or-two calls (zhai_-208 is the Qin remnant, dai_-208 is Zhao Xie's Zhao, jibei_-208 is the revived Qi) hold up on the grid: Dai 206, Zhai 206 and Chang-shan 206 lie inside zhai_-208 or dai_-208 as claimed.

Spot checks: 24 events, rulers or keyframes checked on 14 pages opened; every one confirmed, none mis-dated, no fabrication. One quote ('carved out of the former Kingdom of Zhao', said to be on the Zhang Er page) is not on that page; the event it supports is right; fixed in place.

## Verdicts

### qin-dynasty: thin

Fixes:
- `/identity/rulers/0/from` (applied by reviewer): Qin Shi Huang's reign started at -221, before the dossier's start (-218), so the ruler span was outside the life. Evidence: Brief check 2: rulers inside the life. Qin page infobox: 'Accession of Qin Shi Huang: 221 BC'; the dossier starts at Cliopatria's 218 handoff from qin. Fix: Set from to -218 and say in the note that the accession was 221 (done).
- `/identity/rulers/1, /identity/rulers/2` (applied by reviewer): Qin Er Shi and Ziying had no source URL. Evidence: Qin page infobox '210–207 BC: Qin Er Shi'; table 'Ziying 207 BC'; 'Ziying surrendered to Liu Bang ... in 207 BC'. Fix: Add source https://en.wikipedia.org/wiki/Qin_dynasty to both (done; Qin Er Shi note now quotes the infobox).
- `/keyframe_review/3/correction/text` (applied by reviewer): The years the 214-210 realm holds were in the note only; the correction text did not say them, while keyframe 0 says 'holds 218-216', so 214-213 had no stated shape. Evidence: Nanyue page: 'In 214 BC ... the Qin court established the Nanhai, Guilin, and Xiang Commanderies'; schema: a verdict that changes the years says so in 'text'. Fix: Append '; holds 214-210 (it replaces the 212-211 step, and covers 214-213)' to the text (done). The author may prefer a new keyframe qin-dynasty_-214 (from -214, to -213) with the same correction.
- `/identity/successors` (for the author, not blocking): dai, wei and qi each record a 206 gain with counterpart qin-dynasty, but qin-dynasty's successors list only kingdom-of-han, yong, sai, zhai and western-chu. Evidence: dai /ledger/5 (-206 gain from qin-dynasty, Dai 206 shape, 302 of its 303 cells lie in the Qin remnant shape zhai_-208); wei /ledger/15 (-206 Western Wei); qi /ledger/13 (-206 Qi). Eighteen Kingdoms table: Dai (Zhao Xie), Western Wei (Wei Bao) and Qi (Tian Du) were created in 206. Fix: Add successors dai {cliopatria Dai -206}, wei {cliopatria Wei -206}, qi {cliopatria Qi -206}; list henan, yin, han-2, jiujiang, linjiang, jiaodong, jibei, yan/liaodong too when their land came from the Qin remnant. Not blocking.

Thin (for a gap-filler):
- `/ledger/3`: Confidence 1: Hunan (514 cells), Jiangxi (246), Hubei (119), northern Shanxi (268), Shaanxi (103) and the Fujian edge are dated 214 only because Cliopatria adds them between its 218 and 210 shapes. Cliopatria's Qin 222 and Chu 224 shapes also lack Hunan and Jiangxi, so whether they were Qin before 214 is open. The Changsha Commandery page says it was 'Established by the late Qin dynasty (210 BCE)' 'After the Qin conquest of Lingnan', which would date the Xiang valley (Hunan) at 214-210; northern Shanxi was Zhao's Yanmen and Dai, conquered 222 (the zhao dossier ends at Dai in 222). Page to try: https://en.wikipedia.org/wiki/Changsha_Commandery
- `/ledger/5`: Confidence 1: Yan's revolt (Han Guang) 209; the yan dossier dates it 209 at confidence 2 from its own page. Page to try: https://en.wikipedia.org/wiki/Han_Guang
- `/ledger/7`: Confidence 1: restored Wei (Wei Jiu) 208. Page to try: https://en.wikipedia.org/wiki/Wei_Jiu
- `/ledger/8`: Confidence 1: restored Han (Han Cheng) 208; the han dossier has 208 at confidence 2. Page to try: https://en.wikipedia.org/wiki/Han_Cheng
- `/ledger/9`: Confidence 1: Zhao (Wu Chen, then Zhao Xie) 209-208. Page to try: https://en.wikipedia.org/wiki/Wu_Chen
- `/ledger/10`: Confidence 1: revived Qi (Tian Dan) 209-208; land is jibei_-208 (all Shandong). Page to try: https://en.wikipedia.org/wiki/Tian_Dan_(Qin_dynasty)
- `/ledger/11`: Confidence 1: end of the Minyue occupation 207 here, 206 in minyue; no page dates the end of Minzhong Commandery. Page to try: https://en.wikipedia.org/wiki/Minyue

Spot checks:
- `/ledger/1` confirmed on https://en.wikipedia.org/wiki/Qin_dynasty: 'The region was conquered in 215 BC, and agriculture was established'
- `/ledger/2` confirmed on https://en.wikipedia.org/wiki/Nanyue: 'In 214 BC ... the Qin court established the Nanhai, Guilin, and Xiang Commanderies'
- `/ledger/4` confirmed on https://en.wikipedia.org/wiki/Nanyue: Nanyue page puts the Minyue attack in the campaign begun 'Around 218 BC' without its own year; the Qin page's 214 passage 'took the provinces of Fuzhou and Guilin' supports 214 at confidence 2
- `/ledger/6` confirmed on https://en.wikipedia.org/wiki/Xiang_Yu: 'In 208 BC, Xiang Liang installed Mi Xin as King Huai II of Chu'; Kuaiji page: Xiang Liang governor 209-208
- `/ledger/12` confirmed on https://en.wikipedia.org/wiki/Qin_dynasty: 'Ziying surrendered to Liu Bang upon the latter's arrival in Xianyang in 207 BC'; infobox 'Surrender to Liu Bang: 207 BC'
- `/keyframe_review/0` confirmed on https://en.wikipedia.org/wiki/Kuaiji_Commandery: 'captured in 222 BC'; 'ran from the south bank of the Yangtze through most of modern Zhejiang'

Area: infobox 2300000 (-220), Cliopatria 1632744, ratio 0.71. The shape alive in 220 BC is qin_-222 (Qin row, 1,523,240 km2, ratio 0.66), identical in cells to qin-dynasty_-218; the author's figures (1,632,744 and 2,132,724 km2, ratios 0.71 and 0.93) match shapes.csv. Within a factor of two, noted in keyframe 0 and 3.

### western-chu: thin

Fixes:
- `/ledger/10/counterpart, /ledger/11/counterpart` (applied by reviewer): The December 203 attack and the January 202 contest_end named kingdom-of-han, whose dossier ends in 203 and hands its realm to han-dynasty; the loss at /ledger/12 already names han-dynasty. Evidence: kingdom-of-han identity end {'year': -203}, /ledger/12 '-203 dissolve, counterpart han-dynasty'. Xiang Yu page: died 'c. January 202 BC'. Fix: Counterpart han-dynasty on both (done, so the pair stays matched).
- `/wars/1/zones` (for the author, not blocking): 'Xiang Yu's campaign against Tian Rong' has empty zones and does not say that no ground changed hands. Evidence: Timeline 205: 'Xiang Yu attacks Tian Rong'; Tian Rong was driven out and died, and Xiang Yu held Qi until he turned back for Pengcheng. Fix: Either add a zone (the Qi 206 shape, contest 205) or say in the war note that no ground stayed in Chu hands. Not blocking.

Thin (for a gap-filler):
- `/ledger/8`: Confidence 1: Jiujiang to Chu in 203 (412 of Jiujiang's 429 cells enter the 203 shape); no page opened names Ying Bu's defection to Han (204) and Chu's seizure of Jiujiang. Page to try: https://en.wikipedia.org/wiki/Ying_Bu
- `/ledger/9`: Confidence 1: Linjiang (Gong Ao) to Chu in 203 (468 of 980 cells); page silent. Page to try: https://en.wikipedia.org/wiki/Gong_Ao

Spot checks:
- `/ledger/1` confirmed on https://en.wikipedia.org/wiki/Chu%E2%80%93Han_Contention: 'In August 208 BC, Xiang Liang ... was defeated'; 'relocated King Huai II from Xuyi to a new capital in Pengcheng'
- `/ledger/2` confirmed on https://en.wikipedia.org/wiki/Timeline_of_the_Chu%E2%80%93Han_Contention: 206 BC: 'Xiang Yu declares himself Hegemon-King of Western Chu'
- `/ledger/3` confirmed on https://en.wikipedia.org/wiki/Eighteen_Kingdoms: Western Chu row: Jiangsu, northern Anhui, northern Zhejiang, eastern and southern Henan
- `/ledger/4` confirmed on https://en.wikipedia.org/wiki/Chu%E2%80%93Han_Contention: 'In September–October 205 BCE, the Chu capital, Pengcheng ... fell to a coalition force led by Liu Bang'
- `/ledger/6` confirmed on https://en.wikipedia.org/wiki/Timeline_of_the_Chu%E2%80%93Han_Contention: 204 BC: 'Xiang Yu defeats Peng Yue, conquers Xingyang, and besieges Liu Bang in Chenggao'
- `/ledger/12` confirmed on https://en.wikipedia.org/wiki/Xiang_Yu: 'c. January 202 BC' (29 Dec 203 BC to 27 Jan 202 BC); 'After Xiang Yu's death, the rest of Western Chu surrendered'

Area: infobox None (None), Cliopatria 354296, ratio None. Chu-Han Contention infobox has no area; Western_Chu redirects to Chu (state), no area. The author's shape areas match shapes.csv.

### dai: fix

Fixes:
- `/ledger/4/note` (applied by reviewer): The quote 'carved out of the former Kingdom of Zhao' is not on the Zhang Er page. Evidence: Zhang Er page (searched for 'carved': not present): 'Upon the fall of Qin in 206 BC' 'the Kingdom of Zhao was split into two' ... 'the Kingdom of Changshan (常山), which was given to Zhang Er'. Fix: Quote the page's words instead (done).
- `/ledger (after /ledger/6)` (for the author, not blocking): No rename back to Zhao in 205, though the state is Zhao again after Chen Yu's seizure of Changshan (the rulers note says so). Evidence: Eighteen Kingdoms footnote: 'In 205 BCE, Changshan was destroyed, and Zhao was restored with Zhao Xie as King of Zhao'; Chu-Han: 'Chen Yu then installed Zhao Xie, the King of Dai, as the new ruler of the Zhao territories'. Fix: Add {year -205, type rename, source Eighteen_Kingdoms, confidence 3, note 'Zhao restored ...'} after /ledger/6. Not blocking.

Thin (for a gap-filler):
- `/ledger/0`: Confidence 1: the year Zhao Xie became King of Zhao (208 is Cliopatria's first year; no page opened dates it). Page to try: https://en.wikipedia.org/wiki/Wu_Chen
- `/identity/capitals/1`: Dai's seat (Yu County) is on no page opened; it lies inside the dai_-206 shape. Page to try: https://en.wikipedia.org/wiki/Dai_Commandery

Spot checks:
- `/ledger/2` confirmed on https://en.wikipedia.org/wiki/Timeline_of_the_Chu%E2%80%93Han_Contention: 207 BC: 'A coalition rebel army led by Xiang Yu defeats Qin forces led by Zhang Han at the Battle of Julu'; Julu page: surrender 'in the summer of 207 BC'
- `/ledger/3` confirmed on https://en.wikipedia.org/wiki/Zhang_Er_(Eighteen_Kingdoms): 'Upon the fall of Qin in 206 BC' ... 'the Kingdom of Dai (代), which was given to Zhao Xie'
- `/ledger/5` confirmed on https://en.wikipedia.org/wiki/Eighteen_Kingdoms: Zhao row 'Zhao, briefly called Dai', Zhao Xie, northern Shanxi and northwestern Hebei, created 206
- `/ledger/6` confirmed on https://en.wikipedia.org/wiki/Zhang_Er_(Eighteen_Kingdoms): 'In 205 BCE, Chen Yu, believing that his merit was equal to that of Zhang Er' ... force 'to attack Changshan'; EK footnote 205
- `/ledger/7` confirmed on https://en.wikipedia.org/wiki/Battle_of_Jingxing: 'fought in October 205 BC'; Xia Yue 'defeated and killed'; 'pursued king Zhao Xie to Xiangguo and killed him there'. The page has Handan taken in 204.

Area: infobox None (None), Cliopatria 57016, ratio None. Eighteen Kingdoms page has no area.

### zhai: pass

Tried: years (found 206 = start, dissolve 205 = end), the mislabelled zhai_-208 (handled in qin-dynasty), mirror in kingdom-of-han (205 gain of zhai), capital inside the shape, wikidata null with reason. The 205 end year is the weaker reading (two pages say 206) but it is flagged and coordinated; see cross_checks.

Thin (for a gap-filler):
- `/identity/capitals/0`: Gaonu is on no page opened (flagged by the author); the point lies inside zhai_-206. Page to try: https://en.wikipedia.org/wiki/Eighteen_Kingdoms

Spot checks:
- `/ledger/0` confirmed on https://en.wikipedia.org/wiki/Eighteen_Kingdoms: Di (Zhai), Dong Yi, a Qin general, northern Shaanxi, one of the Three Qins, 206
- `/ledger/1` confirmed on https://en.wikipedia.org/wiki/Chu%E2%80%93Han_Contention: 'In 205 BCE, after conquering the Three Qins in the Guanzhong region'. Dong Yi page and Timeline put the surrender in 206 ('Dong Yi and Sima Xin then surrendered to Liu Bang'); the author records the disagreement and follows kingdom-of-han (205).
- `/identity/rulers/0` confirmed on https://en.wikipedia.org/wiki/Dong_Yi_(Qin_dynasty): surrender 206, defection 205, suicide 204 after the Si River

Area: infobox None (None), Cliopatria 25977, ratio None. No page gives an area; zhai_-208 (1.63 M km2) correctly marked wrong as the Qin remnant.

### chang-shan: fix

Fixes:
- `/identity/predecessors/0/note, /ledger/0/note` (applied by reviewer): Two notes quote 'carved out of the former Kingdom of Zhao' from the Zhang Er page; the phrase is not on it. Evidence: Zhang Er page: 'carved' not present; it says 'the Kingdom of Zhao was split into two' and Changshan 'was given to Zhang Er'. Fix: Quote the page's words (done). The region texts that paraphrase it without quote marks are left.
- `/identity/capitals/0` (for the author, not blocking): Xiangguo (114.50E 37.07N) lies outside Cliopatria's Chang-shan shape: no shape cell within 8 km (bbox min latitude 37.06). Evidence: gazetteer resolve of a 8 km disc at the point intersected with {cliopatria Chang-shan -206}: 0 cells. Fix: Say in the capital note that the seat lies just south of the Cliopatria outline, or adjust keyframe 0 to take in the Xingtai area if a page confirms Xiangguo. Not blocking.

Thin (for a gap-filler):
- `/identity/capitals/0`: Capital Xiangguo is from tradition, not on a page. Page to try: https://en.wikipedia.org/wiki/Xingtai

Spot checks:
- `/ledger/0` confirmed on https://en.wikipedia.org/wiki/Zhang_Er_(Eighteen_Kingdoms): 'the Kingdom of Changshan (常山), which was given to Zhang Er', 206; EK row: central Hebei
- `/ledger/1` confirmed on https://en.wikipedia.org/wiki/Chu%E2%80%93Han_Contention: 'In 205 BCE, Chen Yu defeated Zhang Er, the King of Changshan, and seized control of his kingdom'; EK footnote 205; Timeline 206 (noted by author)

Area: infobox None (None), Cliopatria 34632, ratio None. No page gives an area.

### jibei: fix

Fixes:
- `/identity/capitals/0` (for the author, not blocking): The capital point (117.12E 36.20N, Tai'an) lies outside the Jibei shape and inside Cliopatria's Qi 206 shape; the name 'Bogao' is likely a slip for Boyang (博陽), the seat the Shiji gives Tian An (reviewer's knowledge, not on a page opened). Evidence: gazetteer: 8 km disc at the point ∩ {cliopatria Jibei -206} = 0 cells, ∩ {cliopatria Qi -206} = 1 cell; jibei_-206 bbox min latitude 36.22. Fix: Check the name on a page (zh Wikipedia 济北国) and either move the point inside the shape or note that the seat lies on the Qi side of Cliopatria's line. Not blocking.

Thin (for a gap-filler):
- `/identity/capitals/0`: Capital name and place (Boyang?) not on any page opened. Page to try: https://zh.wikipedia.org/wiki/%E6%B5%8E%E5%8C%97%E5%9B%BD

Spot checks:
- `/ledger/0` confirmed on https://en.wikipedia.org/wiki/Eighteen_Kingdoms: Jibei, Tian An, a Qi rebel leader, northern Shandong; Tian Rong page: 'divided Qi into Qi, Jiaodong, and Jibei, appointing Tian Du, Tian Fu and Tian An'
- `/ledger/1` confirmed on https://en.wikipedia.org/wiki/Timeline_of_the_Chu%E2%80%93Han_Contention: 206 BC: 'Tian Rong sends Peng Yue to conquer the Kingdom of Jibei and kill its king, Tian An'; Chu-Han 'Merely six months after Qin dynasty's collapse'; Tian Rong page 205 (noted by author)

Area: infobox None (None), Cliopatria 44210, ratio None. No page gives an area; jibei_-208 (146,000 km2, all Shandong) correctly marked wrong as the revived Qi.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| qin-dynasty -215 gain (xiongnu) | none | mismatch | xiongnu (ia-01) starts in -209 (Modu) and has no 215 loss; it regains the Ordos in -203 from 'nobody'. Route to ia-01: start the Xiongnu earlier (Touman) with a 215 loss of the Ordos, or qin-dynasty names counterpart nobody. |
| qin-dynasty -214 gain (nobody) | none | exception | Lingnan, stateless tribes. |
| qin-dynasty -214 gain (nobody) | none | exception | Hunan, Jiangxi, Hubei, northern Shanxi etc.; confidence 1, see thin. |
| qin-dynasty -214 occupation_start (minyue) | minyue -214 occupation_start | matched |  |
| qin-dynasty -209 loss (yan) | yan -209 gain | matched |  |
| qin-dynasty -208 loss (western-chu) | western-chu -208 found | matched | same land (Western Chu 208 plus northern Zhejiang) on both sides |
| qin-dynasty -208 loss (wei) | wei -208 gain | matched |  |
| qin-dynasty -208 loss (han) | han -208 gain | matched |  |
| qin-dynasty -208 loss (dai) | dai -208 found | matched |  |
| qin-dynasty -208 loss (qi) | none | exception | qi (ea-01) has no event 221-206 and no shape for Shandong 208-207; listed in counterparts_needing_dossiers (extend qi with jibei_-208). Route to ea-01. |
| qin-dynasty -207 occupation_end (minyue) | minyue -206 occupation_end | matched | one year apart (207 here, 206 in minyue), both confidence 1; align when a page is found |
| western-chu -206 gain (wei) | wei -206 loss | matched | land differs: wei loses its whole 208 shape to western-chu, western-chu takes only its Henan part; the rest of restored Wei (Hebei, Shandong edge) has no taker in wei's ledger |
| western-chu -203 gain (jiujiang) | none | exception | jiujiang (ea-02 other part) not written when this review listed history/polities/ |
| western-chu -203 gain (linjiang) | none | exception | linjiang (ea-02 other part) not written yet |
| western-chu -202 loss (han-dynasty) | none | exception | han-dynasty (ea-02 other part) not written yet |
| western-chu -205 contest_start (kingdom-of-han) | none | missing | Pengcheng 205: kingdom-of-han (ea-01) has no 205 contest with western-chu; its contest starts 204 (Xingyang/Chenggao, matched). |
| western-chu -204 contest_start (kingdom-of-han) | kingdom-of-han -204 contest_start | matched | kingdom-of-han zone {region Henan (region)} against western-chu {place Zhengzhou km 70} |
| dai -206 loss (chang-shan) | chang-shan -206 found | matched | about 100 of Changshan's cells were in the Qin remnant (zhai_-208), not in dai_-208; minor |
| dai -206 gain (qin-dynasty) | qin-dynasty -207 dissolve | matched | mirror is the dissolve (302 of 303 Dai cells inside the Qin remnant); qin-dynasty successors lack dai (fix listed) |
| dai -205 gain (chang-shan) | chang-shan -205 loss | matched |  |
| dai -205 loss (kingdom-of-han) | kingdom-of-han -205 gain | mismatch | year matches; land differs: dai loses Dai 206 + Chang-shan 206, kingdom-of-han gains only {cliopatria Dai -206}; the Changshan part (Zhang Er's later Zhao) has no taker. Route to ea-01. |
| zhai -205 loss (kingdom-of-han) | kingdom-of-han -205 gain | mismatch | year matches; land differs: kingdom-of-han gains a 100 km disc at 109.7E 38.3N that shares 1 cell with zhai_-206 (127 cells). Route to ea-01: use {cliopatria Zhai -206}. Year: Dong Yi page and Timeline say 206; yong and sai (ea-02 other parts) should use the same year as zhai and kingdom-of-han. |
| chang-shan -205 loss (dai) | dai -205 gain | matched |  |
| jibei -206 loss (qi) | none | exception | qi (ea-01) exists but has no gain from jibei or jiaodong; listed in counterparts_needing_dossiers (qi to be extended). Route to ea-01. |

## Routing

- ea-01 kingdom-of-han: land of the 205 gains of zhai (use the Zhai 206 shape, not a disc at 38.3N) and dai (add the Changshan part); a 205 Pengcheng contest with western-chu.
- ea-01 qi: the revived Qi of 208-207 (jibei_-208) and the 206 gains of Jibei and Jiaodong.
- ia-01 xiongnu: the Ordos before 215 (Touman); qin-dynasty gains it from xiongnu in 215 but xiongnu starts in 209.
- ea-02 other parts (yong, sai): end year of the Three Qins; zhai and kingdom-of-han use 205, the Dong Yi page and the Timeline say 206.
- ea-02 other parts (jiujiang, linjiang, han-dynasty): mirrors of western-chu's 203 gains and 202 loss.

## Problems

- Validator: 0 errors, 0 warnings for all six (also --resolve), before and after the reviewer's edits.
- Reviewer edits applied in place and re-validated: qin-dynasty (rulers 0-2, keyframe_review/3 text), western-chu (ledger 10-11 counterpart), dai (ledger 4 note), chang-shan (predecessor note, ledger 0 note); read back after more than 10 s, unchanged.
- Verdict 'fix' here means the reviewer applied what it could; items with applied:false in a 'fix' or 'thin' verdict are non-blocking and need a short author pass. No blocking finding was left unapplied.
- Neighbour dossiers read (ledgers 225-200 BC): wei, minyue, yan, qi, xiongnu, han, plus kingdom-of-han, zhao, qin. Not written yet (other ea-02 parts, not run when the folder was listed): yin, henan, jiaodong, han-2, jiujiang, linjiang, sai, yong, han-dynasty.
- Cliopatria's late Warring States and Qin shapes (qin_-222, chu_-224, qin-dynasty_-218) leave out Hunan, Jiangxi and northern Shanxi; this touches the qin, chu and zhao dossiers (ea-01) as well as qin-dynasty's 214 gain.
- dai, chang-shan and jibei carry wikidata Q5349053, the Eighteen Kingdoms umbrella id shared by twelve rows; zhai sets null for the same reason. Not a fault; the orchestrator may want one rule.
- No page failed to load for the reviewer. Western_Chu redirects to Chu (state).
