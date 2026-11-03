# Notes: group ea-03-x (Three Kingdoms to Sui, additions batch)

Written 2026-10-19 by the Phase B research agent for ea-03-x. The batch owns no Cliopatria row: fifteen dossiers for states Cliopatria lacks, all with `cliopatria_names: []`, every keyframe new, all validate (0 errors; the three lower-Yangtze dossiers cross-reference each other and are clean once all three exist). 37 source entries (36 distinct Wikipedia pages, opened with WebFetch) in all, 75 ledger events (after the second-pass fix of li-zitong-s-wu, below). Every event, verdict and war cites a page opened in this run; where a page was silent the event is confidence 1 and says so. Pages are thin for most of these states: shapes are discs round a named seat (a gazetteer name when one exists, a lon/lat radius otherwise) and every life is certainty soft.

## New slugs (none in polities.csv; counterparts already used by sibling dossiers)

dai-sixteen-kingdoms (310-376), chouchi (296-580), duan-liaoxi (307-338), duan-qi (350-356), ran-wei (350-352), western-shu (405-413, rebel), zhai-wei (388-392), northern-liang-of-gaochang (442-460), yuwen-xianbei (260-344), dangchang-kingdom (424-564), dengzhi (424-554), cuan-clan (327-602), du-fuwei-s-regime (616-620, rebel), shen-faxing-s-liang (619-620, rebel), li-zitong-s-wu (619-621, rebel). The slugs dai-sixteen-kingdoms, chouchi, ran-wei, duan-qi, zhai-wei, western-shu, northern-liang-of-gaochang are the counterpart strings the ea-03-a/b/c/d dossiers already use; du-fuwei-s-regime, shen-faxing-s-liang, li-zitong-s-wu are ea-03-f's suggestions.

## Events other dossiers should carry (reverse sides)

- dai-sixteen-kingdoms: vassal_start/vassal_end with counterpart dai-sixteen-kingdoms in western-jin (from 310, Duke of Dai), later-zhao (Lady Qi submits, under Heru 321-325, undated), former-yan (marriage alliance, undated) and former-qin (infobox only): none of the pages gives a year except 310; former-qin gain 376 (present); northern-wei found 386 (present, counterpart dai-sixteen-kingdoms).
- chouchi: later-qin vassal_start 405 (present) and loss of Tianshui (Longcheng, Jicheng) 389; western-qin gain 394 (Tianshui, confidence 1 here); liu-song-dynasty gain 442; northern-wei gain 443; western-wei gain 552 (Wuxing); northern-zhou gain 580 (Yinping); cheng-han vassal_start for Chouchi (undated, Yang Maosou page); former-zhao 322 war.
- duan-liaoxi: later-zhao and former-yan carry no events for the 338 conquest (they carry Duan Qi only); add gains from duan-liaoxi (Lingzhi and the cities to Zhao; Liaoxi households to Yan) and a contest pair January-April 338; western-jin vassal for the Duke of Liaoxi (303 or 307).
- duan-qi: later-zhao loss 350 and former-yan contest/gain 356 are present; former-yan dates contest_start 355, this dossier 356 (Murong Ke crossed the Yellow River in early 356; Duan Qi page); western-jin should carry the 351 vassal_start and a 356 vassal_end.
- ran-wei: later-zhao split 350 and former-yan gain 352 are present; later-zhao ends the Shi in 351 while the Conquest page has Xiangguo conquered by February 352.
- western-shu: western-jin events (loss 405, contest 412-413, gain 413) are present; contest_start here is summer 413 (the western-jin one is the late-412 commission); later-qin vassal_start c. 407 (Qiao Zong page) is missing from later-qin; western-jin draws Chongqing from 405, this dossier adds it in 410 (Badong).
- zhai-wei: later-yan gain 392 present; western-jin 390/394 shapes (276 cells of Hebei and Henan) overlap Zhai Wei's country; Cliopatria draws it as Jin land.
- northern-liang-of-gaochang: northern-liang (dissolve 442) and kingdom-of-gaochang (found 460, predecessor northern-liang) should name this slug as the predecessor/successor; liu-song-dynasty vassal_start 444 (Prince of Hexi); rouran-khaganate conquest of Gaochang 460.
- yuwen-xianbei: former-yan has no 344 gain from the Yuwen; the Buyeo conquest of 346 stays with jk-02's buyeo.
- dangchang-kingdom, dengzhi: northern-wei, liu-song-dynasty, southern-qi, liang-dynasty tribute and submission (undated); northern-zhou gain 564 (Dangchang); western-wei/tuyuhun 554 (Dengzhi). The northern-zhou page opened is silent on both.
- cuan-clan: sui-dynasty contest 597-602 (the Sui dossier names no Yunnan land); cheng-han/western-jin Ning Province claims after 333.
- du-fuwei-s-regime, li-zitong-s-wu, shen-faxing-s-liang: the tang-dynasty dossier is not written yet; it should carry Du Fuwei (Li Fuwei, Prince of Wu from summer 620) as a vassal tint 620-623 and the gain of Zhejiang from li-zitong-s-wu in winter 621; sui-dynasty carries none of the three. Second pass: tang-dynasty should also carry the 620 gain of Jiangdu (Yangzhou, 70 km) from li-zitong-s-wu (li-zitong-s-wu now has the matching 620 loss, counterpart tang-dynasty).

## Disagreements between pages

- Dai: Western Jin grant of 'five counties north of the mountain ranges' (Dai page) against 'five commanderies' (Tuoba Yilu page). Chouchi: established 296 (infobox) against c. January 297 (Yang Maosou page); Wudu restoration 443 (text) against 448 (infobox). Duan Wuwuchen's Duke of Liaoxi 307 (Duan Wuwuchen page) against 303 (Book of Jin, Zizhi Tongjian, same page). Duan Qi contest start 355 (former-yan) against early 356. Ran Wei: Shi end 351 (later-zhao) against February 352 (Conquest page). Yuwen: destroyed 344 (Conquest page, February or March) against 345 (Book of Wei; Yuwen page infobox). Gaochang exile: the Northern Liang page puts the occupation of Gaochang in 442, kingdom-of-gaochang's note says 439. Cuan Chen: 338 (Timeline of Yunnan-Guizhou) against 339 (Cuanman); Baiman/Wuman split 570 (Timeline) against 602 (Cuanman). Du Fuwei page 'Jiangling' against Li Zitong page 'Jiangdu' for the fall 619 siege.

## Not settled, per state

- dai-sixteen-kingdoms: no page gives the land; the shape is two radii (Hohhot 120 km, Datong 140 km). Year of the Later Zhao and Former Yan vassalage. Pre-310 Tuoba (Shengle occupied 258, three-way division, reunification 307) is not drawn; a Tuoba Xianbei dossier from 258 would be needed. 377-385 land under Former Qin (the Dai page does not mention the Liu Kuren and Liu Weichen division).
- chouchi: no boundary on any page; the Yang Sheng and Nandang expansion ('a large part of eastern Gansu and southern Shaanxi', undated) is a 100 km disc; Hanzhong after 314; the 442 Liu Song and 443 Northern Wei conquests have no narrative; Wuxing's 506-534 gap is a ruler-table inference (confidence 1). One dossier carries the Wuxing and Yinping branches in parallel after 477 (two discs, one colour); a later agent may split them. Mount Chouchi, Licheng, Wudu, Lueyang and Wen County coordinates are approximate.
- duan-liaoxi: Duan rise before the title; Pidi's seat; the land lost in 321; the 338 split between Zhao and Yan. Infobox territory (Yuyang to the Liao River) drawn as three regions.
- duan-qi, ran-wei, zhai-wei: no boundaries beyond named cities and commanderies; Zhai Wei 386-387 pre-state and the 390 Jin counterattack (Juancheng) left out.
- western-shu: whether Badong was Western Shu land from 405; the Mao Qu page failed.
- northern-liang-of-gaochang: who held Gaochang before 442; whether Loulan stayed Juqu land (Shanshan page: Bilong's king fled to Qiemo; 'Zhenda' king 441-445).
- yuwen-xianbei: 'pre-state' clan; the 260 start is the first reign in the ruler table (confidence 1); the infobox region 'central Liaoning and eastward' is not drawn; rulers between 293 and 333 are dated only 'late 3rd century'/'early 4th century' and are omitted.
- dangchang-kingdom, dengzhi: founding dates ('c. 4th century'; '5th century'); 424 is the first dated mention (confidence 1); one page each; ruler strips list only fully dated reigns.
- cuan-clan: a clan chiefdom, not clearly a state; start 327 is the first dated ruler (infobox formation c. 225); no capital on the page; successors (Six Zhao of Yunnan) have no dossier.
- the three Jiangnan rebels: tiny dossiers (1-2 pages each); overlapping discs in the lower Yangtze; month data are seasons only.

## Pages that failed (URL_NOT_FOUND on the title tried)

Mao_Qu, Liu_Jingxuan, Yang_Ding_(Di_chieftain) (the page loaded as Yang_Ding_(Chouchi)), Yang_Nandang, Revolt_of_the_Six_Garrisons, Shanshan_(kingdom) (the page loaded as Shanshan), Liang_Miding, Xiang_Yanheng.

## Gazetteer names the dossiers would prefer (discs were used instead, so nothing is unresolved)

Loulan, Mount Chouchi / Longnan, Wudu, Lueyang, Wen County, Licheng, Qujing (Nanning), Hua County (Huatai), Qian'an (Lingzhi), Jiuzhaigou, Tanchang, Xinghe, Fanshi. 'Ye' must be written with country China (the bare name resolves to Myanmar): used so in ran-wei.

## Rows and states left for others (counterparts without a dossier)

Shanshan (Loulan, Qiemo; ia-01 per ea-02-d, slug kingdom-of-shanshan), Tarim city-states under Wei/Jin (266-328), Six Garrisons rebels (523-525) and the Northern Wei rebel regimes to 534, Wang Lin's Liang (557-560), Luo Yi's regime (Youzhou, 619), Xiyu kingdoms (609-618), Tuoba Xianbei before 310, Sun En's rebels (399-402), Huan Xuan's Chu (403-404), Nanzhong rebels (222-225), Yao Xiang's Luoyang (356), Wuhuan, Gaoche, the Six Zhao of Yunnan, Baiman and Wuman. Under ten years or outside the batch's scope; not written.

## Second pass, 2026-10-19: reviewer findings applied (review-ea-03-x.md, reviews/ea-03-x.json)

Only li-zitong-s-wu (verdict fail) was reopened; pass, fix and thin dossiers are untouched. Pages reopened with WebFetch: https://en.wikipedia.org/wiki/Li_Zitong and https://en.wikipedia.org/wiki/Du_Fuwei. Result: validates, 0 errors, 0 warnings (`--resolve`).

- Keyframe li-zitong-s-wu_620 (620-621) redrawn as Zhejiang (region) plus the Changzhou 80 km disc, without the Yangzhou disc (finding /keyframe_review/1/correction, applied). The Li Zitong page puts the whole sequence in 620 ('In 620, Li crossed the Yangtze to attack Shen'; Piling and Danyang taken; Fu Gongshi, Kan Leng and Wang Xiongdan sent by Li Fuwei; 'abandoned Jiangdu, heading first to Jingkou'; Shen's suicide; capital Yuhang). Infobox: Central Jiangsu 619-620, Southern Jiangsu 620, Zhejiang 620-621. Du Fuwei page: 'Li Zitong abandoned Jiangdu and fled to Jingkou', in the passage after Du's summer 620 title change. Neither page gives a month, so the Jiangdu disc is dropped for all of 620.
- identity.successors[0].land and the 621 dissolve region: Yangzhou removed, same Zhejiang plus Changzhou land; the successor note says Jiangdu was lost in 620.
- Ledger (finding /ledger 620, applied): added a 620 loss of the Yangzhou 70 km disc, confidence 3, source the Li Zitong page, second page (Du Fuwei) in the note.
- Beyond the findings, to keep the file coherent: the war 'Li Fuwei's campaign against Li Zitong' now runs 620-621 (was 621) with the Yangzhou disc added to its zone, because the pages date Fu Gongshi's attack to 620 and the Jiangdu loss came out of it; the Du Fuwei page is added to sources.

Where I differ from the finding's wording: the finding names du-fuwei-s-regime as the counterpart of the loss and wants that dossier to add the matching gain. I used tang-dynasty. Reason: the Du Fuwei page places the attack after 'In summer 620, Emperor Gaozu changed Du Fuwei's title to Prince of Wu' ('Later that year' ...), and the du-fuwei-s-regime dossier already ends at that title change with a dissolve into tang-dynasty, so by the time of the attack the attacker is the Tang's Prince of Wu (the finding allows 'or to tang-dynasty'). Du-fuwei-s-regime was not touched (verdict thin), so it carries no gain; if the orchestrator prefers du-fuwei-s-regime as counterpart, the change is one word in li-zitong-s-wu's ledger plus a 620 gain (Yangzhou 70 km, counterpart li-zitong-s-wu) in du-fuwei-s-regime. The tang-dynasty dossier (ea-04, not written) needs the mirror gain; listed under counterparts_needing_dossiers.

Still open from the review, not for the author: du-fuwei-s-regime keyframe_0 (one 130 km disc round Nanjing for 616-620 overlaps li-zitong-s-wu_619 at Jiangdu) and its fall 619 submission to the Tang, both thin findings left to a gap-filler.
