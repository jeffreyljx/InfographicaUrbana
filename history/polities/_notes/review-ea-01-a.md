# Review: batch ea-01-a (Shang to Warring States, part a)

Reviewed 2026-10-18 by the Phase B adversarial reviewer. Dossiers: chu, shang-dynasty, zhou-dynasty, cai, chen, cao. All six validate (0 errors; warnings are the unknown places Shangcai, Xincai, Zhumadian and the not-yet-written slugs xia-dynasty and eastern-zhou). No context dossier (song, qin, wu, yue, lu, xu, zhu, later-zhou ...) exists yet, so events against them are exceptions. Pages opened: Chu (state) (three reads), King Ling of Chu, Bai Qi, Yue (state), Battle of Boju, Shang dynasty, Yinxu, Zhou dynasty, Western Zhou, Cai (state), Chen (state), Cao (state). Region checks used tools/gazetteer.py resolve.

Verdicts: chu **fail**, shang-dynasty **pass**, zhou-dynasty **thin**, cai **fail**, chen **thin**, cao **pass**.

Reviewer edits (applied, re-validated, read back): chu.json /ledger/13 and /ledger/14 regions (Fuyang, Anhui as coordinates) and the Ying capital_move (now /ledger/5, year 689). Nothing else was edited.

## chu: fail

Area: The Chu page has no area figure (checked); nothing to compare. The author quotes only Cliopatria areas, which match shapes.csv.

Findings:

- `/keyframe_review/2/correction` (BLOCKING). chu_-700 (700-481) keeps the whole Cliopatria 700 shape except the Cai and Chen enclaves, so from 700 Chu already holds the land of every state the ledger annexes later (Shen 688, Xi 684, Huang 648, Jiang 623, Liao 622, Jiang 617, Shuliao 601, Shuyong 574, Lai 538, Xu 512); the step from chu_-750 (Huguang core) to chu_-700 is explained by no event at 700. Evidence: Resolver (tools/gazetteer.py): Cliopatria Chu 700 minus Huguang = about 247,800 km2 (cell estimate) that appears in 700, against a 750 core of about 171,700 km2; the ledger's 688-512 gain circles (Nanyang 50, Xinyang 80, Fuyang-Anhui 70, Hefei 80, Xu 512) cover only about 60,700 km2 of it and all lie inside the 700 shape already (Nanyang 40 km circle 6,070 km2 inside, Xinyang 5,817, Hefei 4,046). The keyframe's own note (K1) says the 353,243 km2 shape 'is Chu at the end of the Spring and Autumn period, not in 750'; Chu page table dates the annexations 688-512. Fix: Rewrite chu_-700 as the land Chu held in 700, not the end-of-period shape, e.g. {"minus": [{"cliopatria": "Chu", "year": -700}, {"union": [the radius regions of Shen, Xi, Huang, Jiang, Liao, Jiang, Shuliao, Shuyong, Lai, the Xu shape, Shangcai 35, Xincai 30, Zhoukou 40]}]} or simply the Huguang core of K1 plus Quan (704), and say in the note that the ledger gains rebuild the Cliopatria extent by 512; the remaining Henan/Anhui land the ledger never gains needs either a dated event or to be cut until chu_-480.
- `/keyframe_review/0/correction` (BLOCKING). The Huguang core of chu_-1030 (1030-751) and chu_-750 (/keyframe_review/1/correction, 750-701) already contains the Hubei states the ledger gains later: E (Wuhan, 863), Quan (Jingmen, 704), Luo and Deng (Xiangyang, 690/678) and Yong (Shiyan, 611); K1's note says these gains 'carry the state from this core into southern Henan', but they lie inside the core. Evidence: Resolver: Cliopatria Chu 750 ∩ Huguang ∩ (Wuhan 70 ∪ Jingmen 40 ∪ Xiangyang 50 ∪ Shiyan 70) = about 42,200 km2. The gain events are therefore no-ops on the map for 1030-611. Fix: Cut those circles out of the K0 and K1 corrections (K0 also minus Wuhan 70 until 863), or replace the core with a region around Danyang and Ying (Jingzhou/Yichang radius) so the ledger gains add the Han valley in their years.
- `/ledger` (BLOCKING). Missing dated annexation: Lù (六) in 622 BC, listed in the Chu page's table of annexed states, is not in the ledger (the other 622 entry, Liao, is). Evidence: Chu (state) page, table of annexed states: '622 BC Lù (六).' (read 2026-10-18). Dao ('after 643 BC'), Ruo ('after 622 BC'), Zhongli ('Sometime in the 6th century BC') and Sui ('after 506 BC') are also in the table but undated (thin). Fix: Add {year: -622, type: gain, counterpart: 'Lu (六, state)', region: a radius around modern Lu'an, Anhui (not in the gazetteer: use Hefei 80 or request Lu'an), text 'Lù (六)', confidence 2, source the Chu page}; list Lù under counterparts_needing_dossiers.
- `/ledger/13/region` (applied by reviewer). Region {place: 'Fuyang', km: 70, country: 'China'} (Liao, 622) resolves to Fuyang, Zhejiang (119.95 E, 30.06 N, near Hangzhou), 400 km from the intended Fuyang, Anhui; same for /ledger/14/region (Jiang 蔣, 617, km 60). Evidence: gazetteer.py resolve: 'matched: place: Fuyang (China, 119.95 30.06) within 70 km', bbox [119.27, 29.46, 120.64, 30.68]; places.jsonl has two Fuyangs in China (Anhui pop 170,023; Zhejiang pop 771,000) and the country key cannot separate them. The notes place Liao near Gushi and Jiang near Huaibin, on the upper Huai. Fix: Applied: both regions now {lon: 115.82, lat: 32.9, km: 70|60} (Fuyang, Anhui, from places.jsonl), text kept, a reviewer remark appended to each note; re-validated (0 errors).
- `/ledger/5` (applied by reviewer). The capital_move to Ying was dated 695 (old /ledger/4) while identity.capitals switches Danyang to Ying at 690/689, so the caption and the dot disagreed by six years. Evidence: Chu (state) page: 'sometime between 695 and 689 BC, the Chu capital moved south-east from Danyang to Ying'; King Wen ('ruled 689–677 BC') 'moved the capital to Ying'. Fix: Applied: event year set to -689 (King Wen), note rewritten with both quotes, event moved after the 690 Luo gain (now /ledger/5; Luo is /ledger/4); re-validated.
- `/keyframe_review/3/correction` (non-blocking). chu_-480 (480-451) cuts out only Cai (Huainan 30), so Huaiyang is Chu's in 480 while chen's keyframe chen_-480 holds it for 480-479 and the ledger gains Chen only in 479: a one-year double claim. Evidence: Chu page: 'Chu annexed Chen in 479 BC'; chen.json /keyframe_review/2 'valid 480 to 479 BC only'. Fix: Add {place: 'Zhoukou', km: 40} to the minus union (the /ledger/27 gain then adds it in 479).
- `/ledger/22` (non-blocking). The 529 loss returns Xincai, which Chu never gained (it gained Shangcai at /ledger/20, and chu_-700 already excludes Xincai); after Cai moves to Xiacai (493, cai /ledger/4) nothing gives Xincai to Chu until the 480 keyframe. Evidence: chu /ledger/20 region Shangcai 35; /ledger/22 region Xincai 30; /keyframe_review/2 minus Shangcai, Xincai, Zhoukou; cai /ledger/4 capital_move 493 with no land event. Fix: Say in the /ledger/22 note that Chu keeps Shangcai and Cai is restored at Xincai; add a 493 gain of Xincai (counterpart cai, confidence 1) mirroring the cai fix.

Thin (for a gap-filler):

- `/ledger/1`: E's site and the 863 annexation (confidence 1) (try https://en.wikipedia.org/wiki/Ezhou)
- `/ledger/31`: Pi 'after 418' (confidence 1) (try https://en.wikipedia.org/wiki/Chu_(state))
- `/ledger/18`: Lai 538 unlocated (confidence 1) (try https://en.wikipedia.org/wiki/Chu_(state))
- `/ledger/21`: 529 restorations of Chen and Cai under King Ping (confidence 1) (try https://en.wikipedia.org/wiki/King_Ping_of_Chu)
- `/ledger/34`: 312 Hanzhong, 301 Chongqiu and 299 eight cities lost to Qin (confidence 1, /ledger/34-36) (try https://en.wikipedia.org/wiki/King_Huai_of_Chu)
- `/ledger/38`: 279 Yan, Deng and Yiling, the Nan Commandery and the 277 Qianzhong/Wu commandery losses (Battle of Yanying failed; Bai Qi gives only 278) (try https://en.wikipedia.org/wiki/King_Qingxiang_of_Chu)
- `/ledger`: 598 annexation and restoration of Chen by King Zhuang; 306 campaign against Yue; undated annexations Dao, Ruo, Zhongli, Sui (try https://en.wikipedia.org/wiki/King_Zhuang_of_Chu)
- `/ledger/10`: Cao as Chu's vassal 'About 630' (confidence 1, start year set to 633) (try https://en.wikipedia.org/wiki/Battle_of_Chengpu)

Spot checks:

- `/ledger/20` https://en.wikipedia.org/wiki/King_Ling_of_Chu: confirmed: 'In 531 BC, King Ling tricked and captured Marquis Ling of Cai'; 'Qiji was made Duke of Cai'
- `/ledger/33` https://en.wikipedia.org/wiki/Yue_(state): confirmed: 'Yue was partitioned by Chu and Qi in 333 BC'; infobox 'Conquered by Chu: 333 BC' (the Chu page says 'in either 334')
- `/ledger/38` https://en.wikipedia.org/wiki/Bai_Qi: confirmed: 'In 278 BC, he led the Qin army to capture Ying (郢), the capital city of Chu'; the page has nothing on 279 or 277
- `/ledger/24` https://en.wikipedia.org/wiki/Battle_of_Boju: confirmed: 506 BC, 'the Wu army captured Ying'; 'In 505 BC, the Qin and Chu armies jointly defeated Wu'; King Zhao 'returned to the capital Ying' (/ledger/25)
- `/ledger/27` https://en.wikipedia.org/wiki/Chu_(state): confirmed: 'Chu annexed Chen in 479 BC and overran Cai to the north in 447 BC' (/ledger/28 too)
- `/ledger/40` https://en.wikipedia.org/wiki/Chu_(state): confirmed: 'Lu was conquered by King Kaolie in 249 BC'
- `/ledger/3` https://en.wikipedia.org/wiki/Chu_(state): confirmed: the table dates E 863, Quan 704, Luo 690, Shen 688-680, Xi 684-680, Deng 678, Huang 648, Jiang 623, Liao 622, Jiang 617, Yong 611, Shuliao 601, Shuyong 574, Lai 538, Xu 512, Qi 445, Ju 431, Pi after 418, Zou about 348 as the ledger has them; Lù (六) 622 is missing from the ledger
- `/ledger/5` https://en.wikipedia.org/wiki/Chu_(state): mis-dated (fixed): page 'between 695 and 689'; King Wen 689-677 'moved the capital to Ying'; capitals strip used 689, the event 695

## shang-dynasty: pass

Area: Infobox 'c. 1122 BC: 1,250,000 km2' read on the page; the shape alive then is shang-dynasty_-1240 (154,175 km2). The author's K0 note states the factor and resolves it (the infobox counts the Erligang cultural sphere); resolution accepted.

Thin (for a gap-filler):

- `/identity/rulers`: No ruler strip: only Wu Ding and Di Xin carry absolute dates on the page (try https://en.wikipedia.org/wiki/List_of_Chinese_monarchs)
- `/identity/capitals/0`: Capitals before Yin (Bo, Ao, Yan, Xiang) are undated; one dot at Zhengzhou to 1251 (try https://en.wikipedia.org/wiki/Shang_dynasty)
- `/keyframe_review/0`: Erligang outposts (Panlongcheng on the middle Yangtze) not drawn; an adjust for 1600-1400 is possible (try https://en.wikipedia.org/wiki/Panlongcheng)

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Shang_dynasty: confirmed: infobox 'Established: c. 1600 BC'; 'identified the establishment of the dynasty with the foundation of an Erligang culture walled city at Yanshi'; Mingtiao undated
- `/ledger/1` https://en.wikipedia.org/wiki/Yinxu: confirmed: 'Yin served as the capital during the Late Shang period (c. 1250 – c. 1046 BCE)', 12 kings; Pan Geng's move undated; coordinates 36°07′21″N 114°19′07″E match the capital dot
- `/ledger/2` https://en.wikipedia.org/wiki/Shang_dynasty: confirmed: 'Battle of Muye: c. 1046 BC'; Nivison and Shaughnessy 'argue for an end date of 1045 BC'; Wu Geng 'to rule the Shang as a vassal kingdom'; Weiziqi enfeoffed 'as the Duke of Song'

## zhou-dynasty: thin

Area: Neither the Zhou dynasty nor the Western Zhou page has an area figure (checked); the dossier's notes say so.

Findings:

- `/keyframe_review/0/correction` (non-blocking). The new keyframe zhou-dynasty_-1046 (1046-1001) is the full Cliopatria 1000 shape, which includes Shandong, while /ledger/6 gains 'Shandong (region)' only in 1039: the gain is a no-op and the map shows Shandong as Zhou from 1046. Evidence: Western Zhou page: 'After three years they had regained the lost areas and expanded their domain over an area stretching into Shandong' (undated); K0's own note says the shape 'already includes the Shandong reach of the Duke of Zhou's campaign (ledger, c. 1039)'. Fix: Either make K0 {"minus": [{"cliopatria": "Zhou Dynasty", "year": -1000}, {"region": "Shandong (region)"}]} (the 1046 gain of the Shang shape keeps western Shandong) or turn /ledger/6 into a note. Non-blocking: confidence 1, inferred year, 7 years.
- `/ledger/1` (non-blocking). The Shang lands are gained as direct Zhou territory in 1046, although the event's own note and the Shang page say Wu Geng ruled them 'as a vassal kingdom' until the rebellion. Evidence: Shang dynasty page: 'allowed Di Xin's son Wu Geng to rule the Shang as a vassal kingdom'. Fix: Write it as vassal_start (counterpart the Wu Geng remnant, the suggested slug wu-geng) in 1046 and vassal_end plus gain at the rebellion's end (1040 or 1039), or say in K0's text that the Shang core is vassal tint until then. Non-blocking.
- `/wars/0` (non-blocking). Wu Geng's rebellion runs 1042-1040 but the gain it produces (/ledger/6) is dated 1039, after the war ends; both years are inferred. Evidence: Zhou dynasty page: King Cheng '1042–1021 BC'; Western Zhou page: 'After three years ...' (no year). Fix: Use one inferred year for both (war to -1039 or gain at -1040). Non-blocking.

Thin (for a gap-filler):

- `/ledger`: vassal_start/vassal_end for the other fengjian fiefs inside the shape (Jin, Qi, Lu, Wey, Zheng, Yan, Qin, Xu, Teng, Zhu); the status split now rests on K1/K2 text only (try https://en.wikipedia.org/wiki/Jin_(Chinese_state))
- `/ledger/3`: Cao's enfeoffment year (confidence 1: 'sometime in the 11th century BC') (try https://en.wikipedia.org/wiki/Cao_(state))
- `/ledger/6`: Duke of Zhou's eastern campaign undated (confidence 1) (try https://en.wikipedia.org/wiki/Duke_of_Zhou)
- `/ledger/11`: vassal_end x5 and dissolve at 751 (/ledger/11-16) are Cliopatria handoff years, confidence 1; they disappear if the Eastern Zhou is merged into this dossier (try https://en.wikipedia.org/wiki/Eastern_Zhou)

Spot checks:

- `/ledger/1` https://en.wikipedia.org/wiki/Zhou_dynasty: confirmed: 'defeated Di Xin at the Battle of Muye, marking the beginning of the Zhou dynasty'; 'A date of 1046 BC ... supported by the Xia–Shang–Zhou Chronology Project'; 'military control over territories centered on the Wei River valley and North China Plain'
- `/ledger/8` https://en.wikipedia.org/wiki/Western_Zhou: confirmed: 'ended in 771 BC when Quanrong mercenaries hired by the rebel Marquis of Shen sacked the Zhou capital Fenghao'; 'forced to evacuate the Wei River valley and relocate east to Luoyi'
- `/ledger/9` https://en.wikipedia.org/wiki/Zhou_dynasty: confirmed: 'The capital was moved eastward to Wangcheng, marking the beginning of the Eastern Zhou period'; infobox 'Wangcheng (771–510 BC; 314–256 BC)'
- `/ledger/10` https://en.wikipedia.org/wiki/Zhou_dynasty: confirmed: 'The Eastern Zhou period (771–256 BC)'; 'The Quanrong put an end to the Western Zhou in 771 BC'
- `/ledger/6` https://en.wikipedia.org/wiki/Western_Zhou: confirmed as undated: 'After three years they had regained the lost areas and expanded their domain over an area stretching into Shandong'; the year 1039 is the author's inference at confidence 1, as flagged

## cai: fail

Area: No area on the Cai page (checked). K0's 35 km radius (about 3,850 km2) matches Cliopatria's 3,683; K1's union is about 6,700 km2 (see fix).

Findings:

- `/keyframe_review/1/correction` (BLOCKING). cai_-750 (750-481) is corrected to union(Shangcai 35, Xincai 30) for the whole span, so Cai holds Xincai from 750 (before its move there) and keeps Xincai through Chu's 531-529 annexation, because /ledger/1 removes only Shangcai; the 529 gain of Xincai (/ledger/3) is then a no-op and the state is drawn at about 6,700 km2, nearly twice the size the author chose for K0. Evidence: King Ling of Chu page: 'In 531 BC, King Ling tricked and captured Marquis Ling of Cai'; 'Qiji was made Duke of Cai' (the whole state Chu's); Cai page: Chu 'relocated Cai several times, first to Xincai (lit. "New Cai") in 531 BC'. A static union cannot carry the correction's own text 'Shangcai to 531 BC, then Xincai'. Fix: Make the correction {"place": "Shangcai", "km": 35, "text": ...} (to 531) and let the ledger carry the rest: /ledger/1 loss of Shangcai 531 (the whole state), /ledger/3 gain of Xincai 529 (as written).
- `/ledger/4` (non-blocking). The 493 move to Xiacai is only a capital_move: Cai's land stays at Xincai until the cai_-480 keyframe (Huainan 30) takes over in 480, 13 years after the dot moves. Evidence: cai /keyframe_review/2 correction Huainan 30 from 480; Cai page: 'later to Xiacai (lit. "Lower Cai") at present-day Fengtai in Anhui' (no year). Fix: Add at 493 a loss of Xincai (counterpart chu) and a gain of Xiacai ({place: Huainan, km: 30}, counterpart wu or nobody), confidence 1 like the move, with the mirror gain in chu. Non-blocking: the year rests on no page.

Thin (for a gap-filler):

- `/ledger/3`: 529 restoration at Xincai inferred from the ruler list (confidence 1) (try https://en.wikipedia.org/wiki/Marquis_Ping_of_Cai)
- `/ledger/4`: 493 move to Xiacai (Zhoulai) and the 494 Chu siege rest on no page (confidence 1; Marquis Zhao of Cai failed) (try https://en.wikipedia.org/wiki/King_Zhao_of_Chu)
- `/identity/successors/0`: Gaocai rump near Changde 447-c.367 not drawn (try https://en.wikipedia.org/wiki/Cai_(state))

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Cai_(state): confirmed: infobox 'Established: c. 1045 bce'; 'Cai Shu Du, was enfeoffed at present-day Shangcai'
- `/ledger/1` https://en.wikipedia.org/wiki/King_Ling_of_Chu: confirmed: 531, Marquis Ling captured, Qiji made Duke of Cai
- `/ledger/2` https://en.wikipedia.org/wiki/Cai_(state): confirmed: 'first to Xincai (lit. "New Cai") in 531 BC'
- `/ledger/5` https://en.wikipedia.org/wiki/Cai_(state): confirmed: 'In 447 BC, King Hui of Chu conquered Cai completely, but allowed the marquesses to settle near Changde in Hunan ... Gaocai'; infobox 'Conquered by Chu: 447 bce'
- `/ledger/4` https://en.wikipedia.org/wiki/Cai_(state): no year on page, as the dossier says (confidence 1, flagged); the page says 'Fengtai', not 'Fengtai County'

## chen: thin

Area: No area on the Chen page (checked). The 40 km radius (about 5,000 km2) keeps Cliopatria's size.

Thin (for a gap-filler):

- `/ledger`: 598 annexation of Chen by King Zhuang of Chu and its restoration the same year (the Chen page shows only Xia Zhengshu 599 and a footnote) (try https://en.wikipedia.org/wiki/King_Zhuang_of_Chu)
- `/ledger/2`: 529 restoration inferred from the ruler table (Duke Hui '529—506'), confidence 1 (try https://en.wikipedia.org/wiki/King_Ping_of_Chu)

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Chen_(state): confirmed: 'After the conquest of the Shang dynasty in 1046/45 BC, King Wu of Zhou enfeoffed his son-in-law Gui Man'; infobox 'c. 1045 BC'; capital Wanqiu
- `/ledger/1` https://en.wikipedia.org/wiki/King_Ling_of_Chu: confirmed: 'In 534 BC, the State of Chen suffered internal disorder'; 'King Ling made Chen a prefecture of Chu' (undated, as the note says); Chen table 'Gongzi Liu ... 534, from March to November'
- `/ledger/3` https://en.wikipedia.org/wiki/Chen_(state): confirmed: 'It was finally unified with the Chu in 479 BC'; 'It existed from c. 1045 BC–479 BC'; Duke Min '501—478' in the table, as the note says
- `/keyframe_review/1` https://en.wikipedia.org/wiki/Chen_(state): confirmed: 'At its peak, Chen encompassed fourteen cities in modern-day Henan and Anhui'; Cliopatria's bbox centre (34.58 N) is about 95 km north of Huaiyang, the misplacement is real

## cao: pass

Area: No area on the Cao page (checked). The 35 km radius (about 3,850 km2) keeps Cliopatria's size.

Thin (for a gap-filler):

- `/ledger/1`: who took Cao's land in 487 (Song is the researcher's reading at confidence 2; the page names no annexer) (try https://en.wikipedia.org/wiki/Duke_Jing_of_Song)
- `/identity/rulers`: no ruler strip (the page's table is Chinese with partial years) (try https://en.wikipedia.org/wiki/Cao_(state))

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Cao_(state): confirmed: 'founded sometime in the 11th century BC by Shu Zhenduo of Cao'; infobox 'Established: 11th century BC'; confidence 2 for the conquest year is fair
- `/ledger/1` https://en.wikipedia.org/wiki/Cao_(state): confirmed: 'the State of Cao was exterminated in 487 BC after the capture of Duke Fei of Cao'; 'Duke Jing of Song attacked Cao'; the page does not say Song took the land, as the note admits
- `/keyframe_review/1` https://en.wikipedia.org/wiki/Cao_(state): confirmed: 'roughly the area of modern-day Dingtao County'; 'about 50 miles east of the point where the current course of the Yellow River changes'; 'To the northwest was Wey, to the northeast Lu and to the southeast Song'; Cliopatria's bbox centre is about 70 km west of Dingtao
- `/wars/0` https://en.wikipedia.org/wiki/Cao_(state): confirmed: 'About 630 it was a vassal or ally of Chu'; 'After Jin defeated Chu at the Battle of Chengpu in 632 BC, Jin crushed the State of Cao'

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| shang-dynasty -1046 dissolve (zhou-dynasty) | zhou-dynasty -1046 gain | matched | the Shang shape of 1046 passes to the Zhou on both sides |
| shang-dynasty -1600 found (xia-dynasty) | - | exception | counterpart has no dossier yet and is listed in the author's counterparts_needing_dossiers (group ea-01-x) |
| zhou-dynasty -1046 vassal_start (song) | - | exception | counterpart owned by a group that has not run yet (no dossier in history/polities/) (song, ea-01) |
| zhou-dynasty -1046 vassal_start (cao) | cao -1046 found | matched | schema: vassal events live in the suzerain's ledger only (counterpart = the vassal); the vassal's mirror is its found event naming the suzerain |
| zhou-dynasty -1045 vassal_start (cai) | cai -1045 found | matched | schema: vassal events live in the suzerain's ledger only (counterpart = the vassal); the vassal's mirror is its found event naming the suzerain |
| zhou-dynasty -1045 vassal_start (chen) | chen -1045 found | matched | schema: vassal events live in the suzerain's ledger only (counterpart = the vassal); the vassal's mirror is its found event naming the suzerain |
| zhou-dynasty -1030 vassal_start (chu) | chu -1030 found | matched | schema: vassal events live in the suzerain's ledger only (counterpart = the vassal); the vassal's mirror is its found event naming the suzerain; chu's /ledger/2 note says the vassalage ends with the 704 kingship, but zhou-dynasty ends it at 751 (handoff), so eastern-zhou must carry 751-704 |
| zhou-dynasty -1039 gain (Wu Geng (Shang remnant) and the eastern peoples) | - | exception | counterpart has no dossier yet and is listed in the author's counterparts_needing_dossiers (group ea-01-x) (wu-geng) |
| zhou-dynasty -771 loss (Quanrong) | - | exception | counterpart has no dossier yet and is listed in the author's counterparts_needing_dossiers (group ea-01-x); qin (ea-01, not run) should also carry the Wei valley from 750 |
| zhou-dynasty -751 vassal_end (song|cao|cai|chen|chu) | - | exception | Cliopatria handoff year, confidence 1; the vassalage continues under the Eastern Zhou, which has no dossier (orchestrator decision, see problems) |
| zhou-dynasty -751 dissolve (eastern-zhou) | - | exception | same state continuing; later-zhou is owned by an ea-01 part that has not run (see problems) |
| chu -863 gain (E (state)) | - | exception | counterpart has no dossier yet and is listed in the author's counterparts_needing_dossiers (group ea-01-x) |
| chu -704 gain (Quan, Luo 690, Shen 688, Xi 684, Deng 678, Huang 648, Jiang 623, Liao 622, Jiang 617, Yong 611, Shuliao 601, Shuyong 574, Lai 538, Qi 445, Ju 431, Pi 418) | - | exception | counterpart has no dossier yet and is listed in the author's counterparts_needing_dossiers (group ea-01-x); Lù (六) 622 is missing from the ledger (fix) |
| chu -633 vassal_start (cao) | cao None None | exception | suzerain-side record (schema); cao's dossier is silent on Chu (its war note quotes 'a vassal or ally of Chu'); paired vassal_end 632 |
| chu -534 gain (chen) | chen -534 loss | matched | Zhoukou 40 on both sides |
| chu -531 gain (cai) | cai -531 loss | matched | Shangcai 35 on both sides |
| chu -529 loss (chen) | chen -529 gain | matched | both confidence 1 (restoration inferred from Chen's ruler table) |
| chu -529 loss (cai) | cai -529 gain | mismatch | years and region agree (Xincai), but chu gained Shangcai in 531 and returns Xincai, which it never held; cai's keyframe already holds Xincai from 750 (see the cai and chu fixes) |
| chu -512 gain (xu) | - | exception | counterpart owned by a group that has not run yet (no dossier in history/polities/) (xu, ea-01); Cliopatria's Xu row runs to 285 |
| chu -506 occupation_start (wu) | - | exception | counterpart owned by a group that has not run yet (no dossier in history/polities/) (wu, ea-01); paired occupation_end 505 |
| chu -479 gain (chen) | chen -479 dissolve | matched | Chen's dissolve names chu as successor |
| chu -447 gain (cai) | cai -447 dissolve | matched | Huainan 30 (Xiacai) on both sides |
| chu -348 gain (zhu) | - | exception | counterpart owned by a group that has not run yet (no dossier in history/polities/) (zhu, ea-01) |
| chu -333 gain (yue) | - | exception | counterpart owned by a group that has not run yet (no dossier in history/polities/) (yue, ea-01) |
| chu -312 loss (qin) | - | exception | counterpart owned by a group that has not run yet (no dossier in history/polities/) (qin, ea-01); also 301, 299, 278 losses and the 223 dissolve |
| chu -286 gain (song) | - | exception | counterpart owned by a group that has not run yet (no dossier in history/polities/) (song, ea-01) |
| chu -249 gain (lu) | - | exception | counterpart owned by a group that has not run yet (no dossier in history/polities/) (lu, ea-01) |
| cai -1045 found (zhou-dynasty) | zhou-dynasty -1045 vassal_start | matched | schema: vassal events live in the suzerain's ledger only (counterpart = the vassal); the vassal's mirror is its found event naming the suzerain |
| chen -1045 found (zhou-dynasty) | zhou-dynasty -1045 vassal_start | matched | schema: vassal events live in the suzerain's ledger only (counterpart = the vassal); the vassal's mirror is its found event naming the suzerain |
| cao -1046 found (zhou-dynasty) | zhou-dynasty -1046 vassal_start | matched | schema: vassal events live in the suzerain's ledger only (counterpart = the vassal); the vassal's mirror is its found event naming the suzerain |
| cao -487 dissolve (song) | - | exception | counterpart owned by a group that has not run yet (no dossier in history/polities/) (song, ea-01); the annexer is the researcher's reading at confidence 2 |

## Problems for the orchestrator

- zhou-dynasty and the ancient part of Cliopatria's 'Later Zhou' row are one state (the Zhou royal house, 1046-256; this ledger already has the 771 rename to Eastern Zhou). The dossier ends at 751 with a dissolve and five vassal_end events that are only Cliopatria's handoff year. Recommendation to the orchestrator: have the ea-01 part that splits later-zhou extend zhou-dynasty to 256 (add 'Later Zhou' to cliopatria_names for -750..-256, drop the 751 dissolve/vassal_end events) rather than start an eastern-zhou dossier (rule 2, one dossier and one colour per state).
- Brief/schema conflict: reviewer-brief section 2.3 asks for a vassal_start mirror in the vassal's ledger with the suzerain as counterpart, but the schema says vassal events name the vassal as counterpart 'in both events' (the suzerain's ledger). Cross-checks here treat the vassal's found event naming the suzerain as the mirror (status matched/exception, not mismatch).
- Gazetteer: a place name with two entries in the same country (Fuyang: Anhui and Zhejiang) resolves silently to the more populous one; the region grammar has no admin1 key for places. The resolver should warn on ambiguous places or accept admin1.
- Pages that failed for the author (Battle_of_Yanying, Marquis_Zhao_of_Cai) were not retried by the reviewer; all pages the reviewer opened loaded.
- No context dossier (song, zheng, later-zhou, jin, qin, lu, wey, wu, qi, han, yue, zhao, minyue) exists in history/polities/ yet; every event against them is an exception until those parts run.
- Reviewer-applied edits: chu.json only (/ledger/13 and /ledger/14 regions, /ledger/5 capital_move year and position); re-validated with 0 errors and read back.

Gazetteer names needed: Shangcai (place, cai, chu, zhou-dynasty); Xincai (place, cai, chu); Zhumadian (place, chu); Fuyang (Anhui) (place, chu (two Fuyangs in China; the resolver takes Zhejiang's; the reviewer used coordinates)); Lu'an (place, chu (for the missing Lù 六 annexation of 622)).

New counterpart: Lù (六), suggested slug lu-2, annexed by Chu 622 BC. The author's counterparts_needing_dossiers list (reports/ea-01-a.json) stands.
