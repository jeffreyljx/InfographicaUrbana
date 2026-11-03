# Notes for group ea-03-b (Three Kingdoms to Sui, part b)

Written 2026-10-19 by the ea-03-b research agent. Six dossiers: tuyuhun, cheng-han, former-zhao, former-liang, former-yan, later-zhao. Each notes field in the dossiers has the detail; this file lists what the reviewer and gap-fillers should read first.

## Cliopatria rows that are wrong or need splitting
- Former Zhao (306..336): the 306 shape is far larger than the pages allow for 304-307; the 311 shape holds Guanzhong 311-315 though Jin held Chang'an until 316; the state ended in 329 (Han-Zhao page) but the shapes run to 336. Different state from Zhao (Warring States) although Wikidata Q1574107 is shared: Cliopatria's Wikidata mapping is wrong.
- Former Yan (337..370): the 337 shape (498k km2) already holds Hebei, Shandong, Beijing, Tianjin and parts of Henan, Anhui, Jiangsu; the pages give those lands to Yan only from 350 (Jicheng, Hebei), 352 (Ye), 357 (Shandong), 365 (Henan, Luoyang). The 353 shape has Shandong and Henan early. Different state from Yan (Warring States) although Wikidata Q1472004 is shared.
- Later Zhao (337..352): the shape is the Former Zhao polygon and does not contain Xiangguo (Xingtai), the capital, nor Shandong; the state runs 319..351. Corrected with Hebei and Shandong (infobox 2.5 M km2 is not reconcilable; see the dossier).
- Cheng Han (306..346): the three shapes are one outline holding Chongqing (from 310), Hanzhong (from 314) and Yunnan/Guizhou (Ning Province, from 333) for years in which pages show Cheng did not hold them; the state is 304..347.
- Former Liang (324..377): the page dates the state 301..376; carried-back keyframe 301-323 added. Overlaps the Western Jin vassal tint (317-323) and the Former Zhao vassal tint (323-329).
- Tuyuhun (287..665): 22 shapes, most differ by vertex noise. Real steps at 426 (dated 430 by the Western Qin page), 439, 469, 476, 638, 641 (undated by any page opened). The 602-627 shape ignores the Sui seizure of 608-619. Ends 663 (Tibetan Empire page; 669 and 670 on other pages).

## Pages that would not load or were thin
- https://en.wikipedia.org/wiki/Shanshan_(kingdom) and https://en.wikipedia.org/wiki/Murong_Kualu: not found (retried with the plain Shanshan title, which loaded and was thin).
- The Tuyuhun, Shanshan and Northern Zhou pages are thin on dates (Northern Zhou has no Tuyuhun sentence). Tuyuhun used the full 9-page budget.

## Disagreements between pages
- Tuyuhun end: Tibetan Empire 663, Battle of Dafeichuan 669, Tuyuhun infobox 670, Cliopatria 665 (663 used; the Tibetan Empire page's 667 sentence fits it).
- Tuyuhun start: infobox 284, but the same page has the Murong crossing the Yellow River in 307-313.
- Later Zhao page (346: Shi Hu took Liang land south of the Yellow River) against the Shi Hu page (the 346 and 347 attacks were repelled): Later Zhao page followed, confidence 2.
- Cheng-Han: ruler table Li Xiong from 303, text 304. Former Liang: Zhang Tianxi 363 (infobox) or 364 (table).

## Counterparts without a dossier
- ran-wei (Ran Wei, 350-352), duan-qi (Duan Qi, Shandong, 350s), Duan Liaoxi, Dai (Tuoba, vassal of Later Zhao), Yuwen, Buyeo, Chouchi, Shanshan (Loulan and Qiemo), Kucha and Yanqi (Tarim states), Tiele tribes. The ea-03-x batch or ea-02 should own the first two; jk-02 the Korean ones.

## Gazetteer names needed
- Places: Lishi (Lüliang, Shanxi), Liting, Puzi (Xi County, Shanxi), Shanggui (Tianshui, Gansu), Xiangguo (alias of Xingtai/Xiangtai), Guanggu (Qingzhou, Shandong), Fangtou, Fuqi (Gonghe, Qinghai), Jicheng (棘城, Liaoxi), Longcheng (Chaoyang). 'Ye' resolves only with country China.
- Regions: none missing; all region names used resolved with tools/gazetteer.py.

## Vassal tints written in the suzerain ledger
- former-zhao: Former Liang 323-329. later-zhao: Former Liang 330-351 (confidence 2/1). former-liang: Kucha and the Western Regions oasis states from 335, Yanqi from 346 (ends 376, confidence 1). former-yan: Goguryeo from 342 (ends 370, confidence 1). The Tuyuhun's Tang vassalage (634/635) is in tang-dynasty.json.
