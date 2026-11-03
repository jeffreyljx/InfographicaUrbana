# Review: batch ea-03-x (Three Kingdoms to Sui, additions)

Reviewer, 2026-10-19. Fifteen new-state dossiers (cliopatria_names []), all validating with 0 errors and 0 warnings before and after the reviewer's edits (`validate_dossier.py --resolve`). 55 events spot-checked on 25 Wikipedia pages opened with WebFetch: no fabricated event; one keyframe contradicted by its own page (li-zitong-s-wu); one found event a year late (shen-faxing-s-liang, re-dated). No page gives an area, so there is nothing to compare for area; every dossier says so.

Verdicts: pass 3 (duan-qi, western-shu, zhai-wei); fix 2, applied by the reviewer (ran-wei, shen-faxing-s-liang); thin 9 (dai-sixteen-kingdoms, chouchi, duan-liaoxi, northern-liang-of-gaochang, yuwen-xianbei, dangchang-kingdom, dengzhi, cuan-clan, du-fuwei-s-regime); fail 1 (li-zitong-s-wu). The thin dossiers are within the page budget: the pages give a seat and a line of territory, not a frontier, so 'thin' here means 'a gap-filler may find more', not that the author was careless. Edits applied in place (tagged '[Reviewer ea-03-x: ...]' in the notes) are marked applied; the rest are for the author or a gap-filler.

## dai-sixteen-kingdoms: thin

- **/identity/capitals/2** (for the author): The capital Daning (Zhangjiakou, 327-336) lies about 160 km from Datong and 275 km from Hohhot, outside both discs of keyframe dai-sixteen-kingdoms_310 (Datong 140 km, Hohhot 120 km). Evidence: Dai page: 'In 327, threatened by Later Zhao, Hena shifted the capital again to Daning'; infobox capitals 'Daning (327-337)'; distance computed from the dossier's own coordinates (114.9 E 40.8 N) to the gazetteer's Datong. Fix: Split the keyframe at 327-337 and add {"place": "Zhangjiakou", "country": "China", "km": 60} to its union (or widen the Datong disc), so the seat lies inside the shape in those years.
- Thin, /ledger: Vassal years: the infobox has 'Vassal of Jin Dynasty, Later Zhao, Former Yan, Former Qin' without years; only Jin 310 is dated. The overlords' dossiers (western-jin from 310, later-zhao from Lady Qi's regency 321-325) carry no vassal_start with counterpart dai-sixteen-kingdoms. Page to try: https://en.wikipedia.org/wiki/Tuoba_Yilu
- Thin, /keyframe_review/0: One disc pair for 66 years; no page names a commandery. Pre-310 Tuoba (Shengle 258) and 377-385 under Former Qin not drawn. Page to try: https://en.wikipedia.org/wiki/Tuoba_Shiyiqian
- Spot checks: /ledger/0 confirmed (Dai_(Sixteen_Kingdoms)); /ledger/1 confirmed (Dai_(Sixteen_Kingdoms)); /ledger/2 confirmed (Dai_(Sixteen_Kingdoms)); /ledger/7 confirmed (Dai_(Sixteen_Kingdoms))

## chouchi: thin

- **/identity/capitals/3** (for the author): The capital Wuxing (Lueyang) is listed 477-552, but keyframe chouchi_506 (506-533) draws Yinping alone, so the seat lies 144 km outside the shape for 28 years. Evidence: Dossier's own keyframe 7 and capitals; the ruler table gap (Yang Shaoxian 503-506, 534-535) is the only evidence for 506-533. Fix: Either give Yinping (Wen County) as the seat for 506-533, or keep Wuxing in the 506-533 shape and drop the confidence-1 loss/gain pair.
- Thin, /ledger/6: 394 loss of Tianshui to western-qin is confidence 1; the Yang Ding page does not say who took Tianshui. Page to try: https://en.wikipedia.org/wiki/Western_Qin
- Thin, /ledger/11: 506 loss and 534 return of Wuxing rest on a gap in the ruler table (confidence 1). Page to try: https://en.wikipedia.org/wiki/Yang_Shaoxian
- Thin, /keyframe_review/3: 'Chouchi controlled a large part of the modern provinces of Gansu (east) and Shaanxi (south)' (Chouchi page) is undated; Yang Sheng and Yang Nandang's conquests (Hanzhong) are undrawn; the 442 Liu Song and 443 Wei conquests have no narrative. Page to try: https://en.wikipedia.org/wiki/Yang_Nandang
- Spot checks: /ledger/1 confirmed (Yang_Maosou); /ledger/2 confirmed (Yang_Maosou); /ledger/3 confirmed (Chouchi); /ledger/4 confirmed (Yang_Ding_(Chouchi)); /ledger/5 confirmed (Yang_Ding_(Chouchi)); /ledger/8 confirmed (Chouchi); /ledger/13 confirmed (Chouchi); /ledger/14 confirmed (Chouchi)

## duan-liaoxi: thin

- **/wars/2/to** (applied by reviewer): War 'Conquest of the Duan' ran to 339, after the state's end (338). Evidence: Conquest of the Duan page: infobox 'January - April 338'; Duan Liao's surrender from Mount Miyun is January 339, the aftermath. Fix: to: 338 (note keeps the 339 surrender).
- **/ledger/2** (for the author): The 321 loss removes the Beijing 70 km disc, but keyframe duan-liaoxi_314 (314-338) keeps the same disc (as 'Yuyang') to 338, so ledger and keyframe contradict each other. Evidence: Duan tribe page: after 321 'the Duan's state of Liaoxi stretched from Yuyang Commandery to the Liao River'; Yuyang's seat is in Miyun, NE of Beijing, not Jicheng. Fix: Give the 321 loss a small Jicheng disc (Beijing 25 km) and draw Yuyang as a separate disc round Miyun in the keyframe, or split the keyframe at 321.
- **/ledger/1/counterpart** (for the author): Counterpart 'Wang Jun (You Province)' is neither a dossier slug nor listed in counterparts_needing_dossiers. Evidence: Duan tribe page: Wang Jun, Jin's Inspector of You Province, 'was defeated by Shi Le in 314'; Pidi, 'backing the Jin court', seized Jicheng. Fix: Use western-jin (Wang Jun held You Province for the Jin) and route the 314 loss to the western-jin dossier, or keep the name and list it.
- Thin, /ledger/2: Land lost in 321 is confidence 1 (the page gives only Pidi's capture); the later-zhao dossier dates Pidi's defeat 323. Page to try: https://en.wikipedia.org/wiki/Duan_Pidi
- Thin, /ledger/5: The 338 division of the Duan land between Later Zhao (Lingzhi, 'more than forty cities', Yuyang, Shanggu, Dai) and Former Yan (Liaoxi households) is not mirrored in later-zhao or former-yan. Page to try: https://en.wikipedia.org/wiki/Conquest_of_the_Duan
- Spot checks: /ledger/0 confirmed (Duan_Wuwuchen); /ledger/1 confirmed (Duan_tribe); /ledger/2 confirmed (Duan_tribe); /ledger/4 confirmed (Conquest_of_the_Duan)

## duan-qi: pass

Tried and could not break: Years, months and the Jin vassalage all on the page; mirrors in later-zhao (350 loss) and former-yan (355 contest, 356 gain and contest_end) found; the whole-Shandong region for 'central and eastern Shandong' is acknowledged in the keyframe note. The 351 Jin vassalage belongs in the western-jin ledger (vassal_start/vassal_end, counterpart duan-qi), routed below.

- Spot checks: /ledger/0 confirmed (Duan_Qi); /ledger/1 confirmed (Duan_Qi); /ledger/2 confirmed (Duan_Qi); /ledger/3 confirmed (Duan_Qi)

## ran-wei: fix

- **/ledger/3/note** (applied by reviewer): The note quoted the page as 'Ran Min had exterminated the Shi clan and conquered Xiangguo' and omitted from whom: the page continues 'from his general-turned-rebel, Liu Xian'. Evidence: Conquest of Ran Wei by Former Yan page, Background section. Fix: Holder named in the note; counterpart kept as later-zhao (Liu Xian held Xiangguo as the Zhao remnant after killing Shi Zhi in 351).
- Thin, /identity/successors: The Ran Wei infobox gives 'Succeeded by: Former Yan, Eastern Jin'; the dossier names only former-yan. Which land (if any) Ran Wei's generals handed to the Jin in 352 is not on the pages opened. Page to try: https://en.wikipedia.org/wiki/Ran_Min
- Spot checks: /ledger/0 confirmed (Ran_Wei); /ledger/3 confirmed (Conquest_of_Ran_Wei_by_Former_Yan); /ledger/4 confirmed (Conquest_of_Ran_Wei_by_Former_Yan); /ledger/5 confirmed (Conquest_of_Ran_Wei_by_Former_Yan)

## western-shu: pass

Tried and could not break: All four checked events are on the page with the year; contest pair and dissolve mirror western-jin (412 contest_start within a year, 413 gain and contest_end). Two counterpart gaps are routed, not faults here: later-qin lacks the c. 407 vassal_start (counterpart western-shu) and western-jin draws Chongqing lost in 405 while this dossier gains Badong only in 410.

- Spot checks: /ledger/0 confirmed (Qiao_Zong); /ledger/1 confirmed (Qiao_Zong); /ledger/2 confirmed (Qiao_Zong); /ledger/5 confirmed (Qiao_Zong)

## zhai-wei: pass

Tried and could not break: Every event (3 of 3) is on the page with its year; later-yan carries the 392 gain. The 386-387 Liyang pre-state is acknowledged in notes. The 389 Yingyang loss is missing from western-jin (routed).

- Spot checks: /ledger/0 confirmed (Zhai_Wei); /ledger/1 confirmed (Zhai_Wei); /ledger/2 confirmed (Zhai_Wei)

## northern-liang-of-gaochang: thin

- **/ledger/1/counterpart** (applied by reviewer): Counterpart 'Gaochang (holder not named)' and the note's 'Neither page names who held the city' are wrong: the cited page names the holder. Evidence: Juqu Wuhui page: 'In fall 442, Juqu Wuhui made a surprise attack on Gaochang, capturing it, and [Kan Shuang] fled to Rouran'; Kan Shuang had refused him entry. Fix: Counterpart 'Kan Shuang (Gaochang)'; note corrected.
- Thin, /keyframe_review/1: The Loulan disc drawn in 442 disappears in keyframe 443-460 with no ledger loss; the pages do not say when or to whom Loulan passed (Shanshan page: 'Zhenda' king 441-445; 'the Northern Wei installed a Chinese king in Loulan' in the 5th century). Page to try: https://en.wikipedia.org/wiki/Shanshan
- Spot checks: /ledger/0 confirmed (Shanshan); /ledger/1 confirmed (Juqu_Wuhui); /ledger/2 confirmed (Juqu_Anzhou); /ledger/3 confirmed (Juqu_Anzhou)

## yuwen-xianbei: thin

- Thin, /ledger/0: Founding 260 is the first reign in the ruler table (confidence 1); 84 years drawn as one Chifeng disc; the page's region 'from the central part of the present day Liaoning province and eastward' is not drawn; the Yuwen-Murong wars (302 onward) moved no land in the dossier. Page to try: https://en.wikipedia.org/wiki/Murong_Hui
- Spot checks: /ledger/0 confirmed (Yuwen); /ledger/1 confirmed (Yuwen); /ledger/2 confirmed (Conquest_of_the_Yuwen)

## dangchang-kingdom: thin

- Thin, /ledger/0: Founding 'c. 4th century' (infobox); 424 is the first recorded interaction (confidence 1); 140 years as one 70 km disc; tribute and submission to Northern Wei, Liu Song, Southern Qi and Liang undated. Page to try: https://en.wikipedia.org/wiki/Liang_Miding
- Spot checks: /ledger/0 confirmed (Dangchang_Kingdom); /ledger/1 confirmed (Dangchang_Kingdom)

## dengzhi: thin

- Thin, /ledger/0: Founding by Xiang Shuzhi undated ('5th century'); 424 is Xiang Qudan's first reign year (confidence 1); 130 years as one 60 km disc; whether the land went to Western Wei, Tuyuhun or Northern Zhou ('by 557 ... Deng province had been established') is unsettled. Page to try: https://en.wikipedia.org/wiki/Tuyuhun
- Spot checks: /ledger/0 confirmed (Dengzhi); /ledger/1 confirmed (Dengzhi)

## cuan-clan: thin

- **/ledger/2/type** (applied by reviewer): The 570 event was typed 'split' with counterpart 'Wuman (Cuan Zhen)' and a Qujing disc, which would cut eastern Yunnan out of the Cuan shape, while keyframe cuan-clan_338 keeps one colour to 596. Evidence: Timeline of Yunnan-Guizhou, 570: 'Cuan Zan splits his realm into the Wuman/Black Mywa, ruled by his son Cuan Zhen' in the east and the White Mywa under his eldest son Cuan Wan in the west: both halves stay Cuan. Fix: type 'rename' (no counterpart, no region), note rewritten.
- Thin, /ledger/1: 338 gain of Yunnan from 'nobody' overlaps the cheng-han dossier's Ning Province (gain 333, held to 347); the pages do not say from whom Cuan Chen took Nanzhong. Page to try: https://en.wikipedia.org/wiki/Ning_Province
- Thin, /ledger/0: Start 327: the notes call Cuan Liang 'the first dated ruler', but the Cuanman infobox lists Cuan Xi 231 and Cuan Gu 265 (formation c. 225); the migration into Yunnan is 'in the 320s'. The capital 'Nanning (Qujing)' is named on the page only for 621. Page to try: https://en.wikipedia.org/wiki/Cuanman
- Spot checks: /ledger/1 confirmed (Timeline_of_Yunnan-Guizhou); /ledger/2 confirmed (Timeline_of_Yunnan-Guizhou); /ledger/3 confirmed (Timeline_of_Yunnan-Guizhou); /ledger/4 confirmed (Timeline_of_Yunnan-Guizhou)

## du-fuwei-s-regime: thin

- Thin, /keyframe_review/0: One 130 km disc round Nanjing for 616-620 includes Jiangdu (Yangzhou, about 75 km away), which was Emperor Yang's seat to 618, Chen Leng's to 619 and Li Zitong's 619-620, so it overlaps li-zitong-s-wu_619; the growth from Liuhe (fall 616) to Liyang (after the spring 617 victory over Chen Leng) and Danyang (620) is undrawn. Page to try: https://en.wikipedia.org/wiki/Du_Fuwei
- Thin, /ledger: 620: Li Zitong 'abandoned Jiangdu and fled to Jingkou' under attack by Du's general Fu Gongshi (Du Fuwei page): a gain of Jiangdu (counterpart li-zitong-s-wu) is missing here, mirror of the loss li-zitong-s-wu lacks. The page also has Du submit to the Tang in fall 619 (the dossier ends summer 620, confidence 2). Page to try: https://en.wikipedia.org/wiki/Li_Zitong
- Spot checks: /ledger/0 confirmed (Du_Fuwei); /ledger/1 confirmed (Du_Fuwei)

## shen-faxing-s-liang: fix

- **/identity/start, /ledger/0** (applied by reviewer): The state was dated from fall 619 (the King of Liang title), but the page gives the land from 618: after Emperor Yang's death Shen, governor of Wuxing Commandery, 'occupied more than 10 commanderies', Piling among them; infobox territory 'Zhejiang/Southern Jiangsu, 618-620'. Evidence: Shen Faxing page, opened twice. Fix: start 618; found event 618 with the 618 quote; a 619 rename for the King of Liang title and the Piling capital; capitals Wuxing Commandery (Huzhou) 618 then Piling 619-620; ruler, keyframe (shape_id shen-faxing-s-liang_618) and certainty from 618.
- Spot checks: /ledger/0 confirmed (Shen_Faxing); /ledger/1 confirmed (Shen_Faxing); /ledger/2 confirmed (Shen_Faxing)

## li-zitong-s-wu: fail

- **/keyframe_review/1/correction** (for the author): Keyframe li-zitong-s-wu_620 (620-621) keeps the Jiangdu disc (Yangzhou 70 km) beside Zhejiang, but the cited page says Li Zitong abandoned Jiangdu in 620. Evidence: Li Zitong page: 'he abandoned Jiangdu, heading first to Jingkou'; infobox titles 'Emperor of China (Central Jiangsu), 619-620; (Southern Jiangsu), 620; (Zhejiang), 620-621'. Du Fuwei page: 'Li Zitong abandoned Jiangdu and fled to Jingkou', the fighting led by Du's general Fu Gongshi. Fix: Redraw keyframe 620-621 as Shen Faxing's former land (Zhejiang region plus the Changzhou disc) without Yangzhou, and drop Yangzhou from identity.successors[0].land.
- **/ledger (620)** (for the author): No event for the 620 loss of Jiangdu. Evidence: Same two pages. Fix: Add a 620 loss, region the Yangzhou 70 km disc ('abandoned Jiangdu, heading first to Jingkou'), counterpart du-fuwei-s-regime (Fu Gongshi's attack; Du was already the Tang's vassal, so tang-dynasty if the ea-04 dossier carries it), source the Li Zitong page, confidence 3; du-fuwei-s-regime adds the matching gain.
- Spot checks: /ledger/0 confirmed (Li_Zitong); /ledger/1 confirmed (Li_Zitong); /ledger/2 confirmed (Li_Zitong); /keyframe_review/1 not on page (Li_Zitong)

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| dai-sixteen-kingdoms 310 found (western-jin) | western-jin None None | missing | Duke of Dai under the Jin from 310: western-jin should carry vassal_start (counterpart dai-sixteen-kingdoms) 310 and a vassal_end; later-zhao, former-yan, former-qin vassalage undated on the page. |
| dai-sixteen-kingdoms 376 dissolve (former-qin) | former-qin 376 gain | matched |  |
| chouchi 313 gain (western-jin) | western-jin 314 loss | mismatch | western-jin L17 has Hanzhong lost to cheng-han in 314 ('rebelling refugees in Hanzhong surrendered the region to Cheng'); chouchi has Yang Nandi take Hanzhong from Jin in 313 and lose it to a local revolt in 314 (Yang Maosou page). western-jin should add a 313 loss to chouchi; the 314 holder is cheng-han in both readings. |
| chouchi 314 loss (nobody) | - | exception | local revolt (Yang Maosou page); see the 313 row: the revolt's land went to cheng-han, whose dossier could carry the 314 gain from chouchi. |
| chouchi 371 loss (former-qin) | former-qin 371 gain | matched |  |
| chouchi 385 gain (former-qin) | former-qin None None | missing | former-qin has no 385 loss of the Chouchi core. |
| chouchi 389 gain (later-qin) | later-qin None None | missing | Longcheng and Jicheng taken from Later Qin's commanders (Yang Ding page); later-qin lacks the 389 loss. |
| chouchi 394 loss (western-qin) | western-qin 394 gain | mismatch | western-qin's 394 gain is from former-qin (Longxi), not from chouchi; chouchi's event is confidence 1. |
| chouchi 405 vassal_start (in later-qin) (chouchi) | later-qin 405 vassal_start | exception | recorded in the overlord's ledger as the schema asks; nothing needed in chouchi. |
| chouchi 442 loss (liu-song-dynasty) | liu-song-dynasty None None | missing | liu-song-dynasty has no 442 gain of Chouchi. |
| chouchi 443 gain (northern-wei) | northern-wei None None | missing | northern-wei has no 443 conquest/loss of Chouchi. |
| chouchi 506 loss (northern-wei) | northern-wei None None | missing | confidence 1 on both counts. |
| chouchi 534 gain (northern-wei) | northern-wei None None | missing | confidence 1; northern-wei ends 534. |
| chouchi 552 loss (western-wei) | western-wei None None | missing | western-wei has no 552 gain of Wuxing. |
| chouchi 580 dissolve (northern-zhou) | northern-zhou None None | missing | northern-zhou has no 580 gain of Yinping. |
| duan-liaoxi 307 found (western-jin) | western-jin None None | missing | Duke of Liaoxi, a Jin vassal: western-jin should carry vassal_start (counterpart duan-liaoxi). |
| duan-liaoxi 314 gain (Wang Jun (You Province)) | - | exception | name without a dossier, not listed; Wang Jun was Jin's Inspector of You Province: western-jin is the natural counterpart. |
| duan-liaoxi 321 loss (later-zhao) | later-zhao 323 gain | mismatch | later-zhao L1 323 'Shi Le defeated Duan Pidi and took Shandong from Cao Ni', counterpart Cao Ni: two years apart and different land (Jicheng disc here, Shandong there). |
| duan-liaoxi 338 dissolve (later-zhao) | later-zhao None None | missing | neither later-zhao nor former-yan carries the 338 conquest of the Duan (contest January-April 338, gains of Lingzhi and Liaoxi). |
| duan-qi 350 found (later-zhao) | later-zhao 350 loss | matched |  |
| duan-qi 356 contest_start (former-yan) | former-yan 355 contest_start | matched | one year apart (early 356 crossing vs 355 commission), within tolerance. |
| duan-qi 356 dissolve (former-yan) | former-yan 356 gain | matched |  |
| duan-qi 351 vassal (Jin) (duan-qi) | western-jin None None | missing | western-jin should carry vassal_start 351 and vassal_end 356 with counterpart duan-qi. |
| ran-wei 350 found (later-zhao) | later-zhao 350 split | matched |  |
| ran-wei 352 gain (later-zhao) | later-zhao 351 dissolve | matched | later-zhao ends 351 (successor ran-wei); Xiangguo fell to Ran Min by February 352 from Liu Xian, the Zhao remnant: within a year. |
| ran-wei 352 dissolve (former-yan) | former-yan 352 gain | matched |  |
| western-shu 405 found (western-jin) | western-jin 405 loss | matched |  |
| western-shu 410 gain (western-jin) | western-jin None None | mismatch | western-jin's 405 loss already includes Chongqing (Yi Province 'Sichuan and Chongqing'); western-shu takes Badong only in 410. One of the two must change: western-jin keeps Badong to 410 with a 410 loss, or western-shu draws Chongqing from 405. |
| western-shu 407 vassal (Later Qin) (western-shu) | later-qin None None | missing | later-qin should carry vassal_start c. 407 (counterpart western-shu) and vassal_end 413. |
| western-shu 413 dissolve (western-jin) | western-jin 413 gain | matched | contest_start 413 here vs late 412 in western-jin: within a year. |
| zhai-wei 389 gain (western-jin) | western-jin None None | missing | western-jin lacks the 389 loss of Yingyang; its 390 Cliopatria-based gain from former-qin covers Hebei/Henan cells that overlap Zhai Wei. |
| zhai-wei 392 dissolve (later-yan) | later-yan 392 gain | matched |  |
| northern-liang-of-gaochang 442 found (Shanshan) | - | exception | Shanshan has no dossier; listed by the author (suggested slug kingdom-of-shanshan, ia-01). Other dossiers spell it 'Shanshan (Loulan)' and 'Shanshan (Loulan and Qiemo)': the owner should pick one slug. |
| northern-liang-of-gaochang 442 gain (Kan Shuang (Gaochang)) | - | exception | a local governor who fled to Rouran; no state. |
| northern-liang-of-gaochang 442 found (predecessor) (northern-liang) | northern-liang 442 dissolve | matched | northern-liang names this slug as successor. |
| northern-liang-of-gaochang 460 dissolve (kingdom-of-gaochang) | kingdom-of-gaochang 460 found | mismatch | kingdom-of-gaochang L0 names counterpart northern-liang (and its note dates the Juqu flight to 439); it should name northern-liang-of-gaochang. rouran-khaganate carries the 460 vassal_start of kingdom-of-gaochang but no conquest of the Juqu. |
| northern-liang-of-gaochang 444 vassal (Liu Song) (northern-liang-of-gaochang) | liu-song-dynasty None None | missing | Prince of Hexi from Liu Song (444): liu-song-dynasty could carry a vassal_start. |
| yuwen-xianbei 344 dissolve (former-yan) | former-yan None None | missing | former-yan has no 344 gain of the Yuwen land. |
| dangchang-kingdom 564 dissolve (northern-zhou) | northern-zhou None None | missing | northern-zhou has no 564 gain (Dang province). |
| dengzhi 554 dissolve (western-wei) | western-wei None None | missing | western-wei and tuyuhun carry nothing for 554. |
| cuan-clan 338 gain (nobody) | cheng-han 333 gain | mismatch | cheng-han L6 gains Ning Province from western-jin in 333 and holds it to 347; cuan-clan takes Yunnan from 'nobody' in 338: overlapping claims 338-347. |
| cuan-clan 597 contest_start (sui-dynasty) | sui-dynasty None None | missing | sui-dynasty has no Yunnan contest 597-602. |
| du-fuwei-s-regime 616 found (sui-dynasty) | sui-dynasty None None | missing | sui-dynasty's 617 losses to the rebels do not include du-fuwei-s-regime. |
| du-fuwei-s-regime 620 dissolve (tang-dynasty) | - | exception | tang-dynasty belongs to ea-04, which has not run yet. |
| du-fuwei-s-regime 620 gain (missing) (li-zitong-s-wu) | li-zitong-s-wu None None | missing | Jiangdu abandoned by Li Zitong in 620 (both pages); neither dossier carries it. |
| shen-faxing-s-liang 618 found (sui-dynasty) | sui-dynasty None None | missing | after the reviewer's re-dating; sui-dynasty has no loss to shen-faxing-s-liang. |
| shen-faxing-s-liang 620 dissolve (li-zitong-s-wu) | li-zitong-s-wu 620 gain | matched |  |
| li-zitong-s-wu 619 found (sui-dynasty) | sui-dynasty 619 dissolve | exception | Jiangdu was held by Chen Leng, a Sui remnant, after sui-dynasty's summer 619 dissolve; no mirror needed. |
| li-zitong-s-wu 621 dissolve (tang-dynasty) | - | exception | tang-dynasty belongs to ea-04, not run yet; the conqueror was Du Fuwei's general Wang Xiongdan for the Tang. |

## For the owners of the counterpart dossiers

- western-jin (ea-02/ea-03): vassal_start for dai-sixteen-kingdoms (310), duan-liaoxi (307, or 303), duan-qi (351-356); loss of Hanzhong to chouchi 313; loss of Yingyang to zhai-wei 389; Badong/Chongqing: keep to 410 or let western-shu draw it from 405.
- later-zhao and former-yan: the 338 conquest of the Duan (contest January-April 338; Lingzhi and 'more than forty cities' to Zhao, Liaoxi households to Yan); former-yan the 344 gain of the Yuwen land.
- former-qin 385 loss, later-qin 389 loss, liu-song-dynasty 442 gain, northern-wei 443, western-wei 552, northern-zhou 580 and 564 (Dangchang): the Chouchi and Dangchang mirrors.
- later-qin: vassal_start c. 407 for western-shu. kingdom-of-gaochang: predecessor and found counterpart should be northern-liang-of-gaochang, not northern-liang. sui-dynasty: losses to du-fuwei-s-regime (616), shen-faxing-s-liang (618) and the Yunnan contest with cuan-clan 597-602. cheng-han: reconcile Ning Province 333-347 with cuan-clan's 338 Yunnan.
- tang-dynasty (ea-04, not run): Du Fuwei as a vassal from 619/620; the 621 gain of Zhejiang from li-zitong-s-wu; Jiangdu from Li Zitong in 620 if Du's land is drawn as Tang's by then.

## Pages that would not load

None of the 25 pages failed. The Duan tribe infobox did not show in one WebFetch pass; a second pass found its sentences in the body.
