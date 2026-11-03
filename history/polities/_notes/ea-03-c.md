# Notes for group ea-03-c (Three Kingdoms to Sui, part c)

Written 2026-10-19 by the ea-03-c research agent. Five dossiers: northern-wei, later-qin, former-qin, later-yan, later-liang. All validate (0 errors) and resolve through the gazetteer. Each dossier's `notes` field has the detail; read this file first.

## Cliopatria rows that are wrong or need correcting
- Northern Wei (387..533): none of the 14 shapes of 402-533 contains Pingcheng (Datong, capital 398-493) or Shengle (Hohhot), checked by intersecting each shape with a 30 km disc; the 387-397 shapes do. The 451-475 shape already holds Shandong and Xuzhou, which the Emperor Ming of Liu Song page gives to Wei only in 466 (Xu, Yan) and 468 (Qing, Ji). The 426-438 shape has none of the Xia land (427, 431), Liaoxi (433, 436). State runs 386..534 (shape 387..533). Infobox area 2.0 M km2 (450) against 0.79 M (shape of 441-450): ratio 0.39, unexplained; the 451 shape (1.17 M) is within a factor of two.
- Later Qin (387..416): runs 384..417; the 387-393 shape lacks Chang'an (Yao Chang took it in 386); the 394-401 shapes hold half of Henan although Luoyang came only in 399; Hexi appears in 407 though Later Liang surrendered in 403.
- Former Qin (353..393): runs 351..394; the 383-386 single shape spans the collapse (replaced by 383, 384, 385-386 keyframes); the 387-393 shapes (Chang'an, Luoyang, Kaifeng) are contradicted by the pages and marked wrong. Wikidata Q1471995 is shared with the row `qin` (Qin state, -750..-219): different states, Cliopatria's collision; no merge.
- Later Yan (387..409): runs 384..409; the 395-401 shape holds the pre-Wei-invasion empire for seven years (replaced by a 397-401 keyframe with the 402 remnant); the 402 shape keeps Liaodong until 406 though Goguryeo took it in 404; the 407 shape is the same set of cells as the Northern Yan 410 shape. The bbox to 82.9 E / 51 N is five stray cells.
- Later Liang (387..406): runs 386..403; the 402 shape holds three years past the state's end. `later-liang-dynasty` (911-925, Five Dynasties) is another state with a shared Wikidata id; not touched.

## Pages that would not load or were thin
- https://en.wikipedia.org/wiki/Six_Garrisons_Rebellion, https://en.wikipedia.org/wiki/Revolt_of_the_Six_Garrisons and https://en.wikipedia.org/wiki/Battle_of_Chaibi: not found. The Six Garrisons revolt rests on two sentences of the Northern Wei page; Chaibi on one sentence of the Later Qin page.
- Goguryeo, Eastern Wei and the Liu Song dynasty page were thin (no 400/404/405 Later Yan wars; no Wei partition detail; Henan and Huaibei not named).

## Disagreements between pages
- Northern Wei end: Eastern Wei 8 November 534 (Eastern Wei page) against 8 November 535 (Northern Wei infobox); 534 used. Luoyang capital move 25 October 493 (infobox) against 494 (text). Daowu's imperial title 24 January 399 (infobox).
- Later Yan end: 6 November 409 (infobox) against Feng Ba replacing Murong Yun in 407 (text); the Northern Yan page says its own start is 407 or 409. 409 used; a `rename` event at 407.
- Later Qin 400: the Later Qin page says it conquered Western Qin; the Western Qin page says Gangui surrendered to Southern Liang and later fled to Later Qin, keeping his territory.
- Lü Guang: sent to the Western Regions 382 (Former Qin page), 383 (Later Liang page); conquered Kucha 384. Lü Guang's imperial claim 387 (text) vs 396 (infobox) on the Later Liang page.
- Later Qin Hexi loss: Later Qin page gives it to Southern Liang (undated); Northern Liang page has Guzang as its capital from 412. Recorded at confidence 1.

## Not settled for want of pages (see dossier gaps)
- Wei: Western Regions conquests of the 440s (Shanshan, Yanqi, Kucha), the Tuyuhun frontier, Henan south of the Yellow River 431-465 (the 451 shape gives it to Wei; no page dates it), the Southern Qi frontier, the Wei-Rouran frontier shifts, the rebel states of 524-534.
- Former Qin: the extent of Fu Deng's domain 387-394 (replaced by discs at the seats the infobox names; the location of Fort Hukong is not on the page and my coordinates for it are a guess), Lü Guang's Western Regions campaign, Former Liang's vassalage before 376.
- Later Qin: where Yao Chang was 384-385; the Chouchi and Western Shu relations (Western Shu has no event: its end is not on any page opened); Helian Bobo's rebellion (407 in the infobox, undated in the text).
- Later Yan: extent in 384-386; Shandong and Liaodong hold in 387-394; Goguryeo wars of 400 and 405.
- Later Liang: Western Liang (400), the Western Regions.

## Counterparts without a dossier
dai-sixteen-kingdoms (Tuoba Dai 310-376; Cliopatria's Dai is -208..-204), chouchi (Di state, conquered 371, Later Qin vassal 405), zhai-wei (Dingling state at Huatai 388-392), six-garrisons-rebels (rebel state or states 523-525 and after), western-shu (submitted to Later Qin 407). All are used as counterpart strings; the validator warns for dai-sixteen-kingdoms, six-garrisons-rebels, zhai-wei, chouchi.

## Gazetteer names
All region and place names used in region specs resolve (checked with --resolve). Capital names that are not in the gazetteer and not used in a spec: Shengle (Horinger, near Hohhot), Longcheng (alias of Chaoyang), Zhongshan (old Dingzhou), Nan'an (Longxi), Tongwancheng (Jingbian, Shaanxi), Fort Hukong (unlocated). Place 'Ye' resolves only with country China (not used).

## Vassal tints written in the suzerain ledger
later-qin: later-liang (401-403), chouchi (405-), southern-yan (407-410). former-qin: western-qin (387-394). later-liang: western-qin (395-397).

## Fixes after review (later-yan, 2026-10-19)
Reviewer verdict for later-yan was fail (one blocking finding). Four of the five findings were open (the 386 -> 385 re-dating of /ledger/2 was applied by the reviewer). Pages re-opened with WebFetch: Later Yan, Murong Bao (twice), Emperor Daowu of Northern Wei, Gwanggaeto the Great, Murong Chui. later-yan.json validates with --resolve: 0 errors, 1 warning (zhai-wei has no dossier). This section supersedes the "Not settled" line on Later Yan above for Shandong and the Goguryeo wars.

What changed
- Shandong (blocking). The Later Yan page: "Then, he sent his generals to capture Shandong from the Eastern Jin dynasty" after the 394 Western Yan campaign. Keyframes 385-386, 387-389 and 390-393 are now the Cliopatria shapes minus Shandong (verdict adjust for 387 and 390); a 394 gain from western-jin (Shandong, confidence 2: the year is the page's sequence, the sentence has none) mirrors western-jin /ledger/42; the 385 gain from Former Qin lost Shandong from its region. Liaoning and Liaodong before "by 394" remain undated on every page opened.
- Shanxi. Keyframe 395-396 is the Cliopatria 395 shape plus the Shanxi cells of the 394 shape (intersect), because Cliopatria hands Shanxi to the Wei in 395 but the pages do not. New 396 loss to northern-wei from the Murong Bao page: "In fall 396 ... Tuoba Gui ... made a surprise attack on Bing Province", "defeating Murong Nong and forcing him to flee back to Zhongshan" (Bing Province glossed "modern central and northern Shanxi"). Confidence 2: neither the Murong Bao nor the Emperor Daowu page says the Wei held the province afterwards, and neither names Jinyang or Taiyuan. The 396 contest start and the 398 contest end, and the Northern Wei-Later Yan war zone, now include the same Shanxi land.
- Longcheng. Keyframes 397-401, 402-406 and 407-409 add a 60 km disc at Chaoyang (the Cliopatria shapes stop 0.28 degrees short of it); 402 and 407 became verdict adjust for that reason only.
- Goguryeo. The single 385-404 zone is split: a contest of 385 alone (the Goguryeo page gives only 385), and a second contest 400-406 from the Gwanggaeto the Great page (400: Later Yan attacks Goguryeo and is repulsed; 402: Goguryeo takes Sukgunseong near the Later Yan capital; 405 and 406: Later Yan attacks Liaodong fortresses and is defeated twice; "Gwanggaeto conquered all of Liaodong", no year). Two wars in wars[] instead of one.
- Sources: Gwanggaeto the Great, Murong Bao, Emperor Daowu of Northern Wei, Murong Chui added (11 in all). Murong Chui: 384 Ye besieged, "many cities" captured (none named), end of 385 "largely in control of the territory north of the Yellow River"; keyframe 384 keeps its Luoyang disc (the page does not mention Xingyang).

What I disagree with
- The reviewer proposed closing the Gwanggaeto contest in 404. I closed it in 406: the Gwanggaeto page has Later Yan attacking Goguryeo's Liaodong fortresses in 405 and in 406, and goguryeo /ledger/26-27 end the fight in 406. The Liaodong loss stays at 404, the Later Yan page's own year; the two pages differ by two years and the contest spans both.
- The reviewer's fix for Shanxi was a loss "from a page"; the page gives the attack and the governor's flight, not the hold, so the event is confidence 2 and says so.

Page disagreements found
- Western Yan's end: Murong Chui page "winter of 393", Later Yan and Western Yan pages 394 (394 kept).
- Longcheng: the Murong Bao page glosses it as modern Jinzhou, Liaoning; the Later Yan page's capital and this dossier use Chaoyang.
- Liaodong lost: 404 (Later Yan page) against conquered after 406 (Gwanggaeto page; goguryeo dossier 406). Route to jk-02 if the 404 is to be harmonised.

Left for others
- northern-wei (thin, not touched in this pass) still has no 396 gain of Bing Province (Shanxi) from later-yan; the later-yan loss is /ledger/9 and the Murong Bao page above is its source.
- zhai-wei has no dossier (later-yan /ledger/5, 392).
- Still unsettled for want of a page: Later Yan's ground in 384 and 385-386; Liaoning and Liaodong before 394; who held Bing Province after fall 396.
