# Review of batch ea-01-d (zheng, zhu, yue, han, wei, zhao, kingdom-of-han)

Reviewer, 2026-10-18. Validator: all seven pass (0 errors); warnings only the han/kingdom-of-han shared-row verdicts and wei's two pre-403 wars, both explained by the author. Pages opened with WebFetch: Spring_and_Autumn_period, Zheng_(state), Zhu_(state), Chu_(state), Yue_(state), Teng_(state), Han_(Warring_States), Battle_of_Changping, Qin%27s_wars_of_unification, King_Zhaoxiang_of_Qin, King_Wuling_of_Zhao, Zhao_(state), Wei_(state), Kaifeng, Zhongshan_(state), Emperor_Gaozu_of_Han, Chu%E2%80%93Han_Contention. Every spot-checked event was on its page with its year; nothing fabricated was found.

Verdicts: zheng **thin**, zhu **thin**, yue **fix**, han **fail**, wei **fail**, zhao **fail**, kingdom-of-han **fail**.

## The main problem: the three Jin states

Cliopatria's Han, Wei and Zhao rows are garbled (gazetteer, 12 km discs): 'Han' 404 holds Anyi and Luoyang; 'Zhao' holds Pingyang, Changzhi and Ye; 'Wei' 404 holds Ye, Handan, Lingshou and Baoding, and 'Wei' 326/291 holds Dai, Datong, Lingshou and Baoding, Zhao's land. The author saw most of this and replaced shapes with discs, but the three corrected dossiers do not fit together:

- han and wei claim the same 66-134 cells every year 366-225: wei's Daliang disc (Kaifeng, 100 km) contains Han's capital Xinzheng (72 km away), and han's 366-338 corrections lack the Anyi minus, so Han holds Wei's capital.
- han holds 15 of the 20 cells of the Zhou royal domain (Luoyang) in every year to 256.
- han has no keyframe for 262-257, so the han_-337 correction (with Yiyang, lost 307, and Shangdang, lost 262) comes back; han and zhao then share 49 cells.
- wei's 403-382 shape is Cliopatria's whole Hebei shape including Handan, which zhao also holds (68 shared cells).
- after 381 the central Hebei plain (about 366 cells, 113.7-117.1 E, 36.9-40.2 N) belongs to no dossier: wei drops it, and zhao adds only Cliopatria's Zhongshan shape, which lies at 115.95-117.08 E and misses Lingshou (Pingshan), Zhengding and Dingzhou, the places the Zhongshan page names.

Recommendation: one agent redraws the three together, testing whether Cliopatria's 'Wei' shapes from 326 are Zhao's land under the wrong label.

## Fixes applied by the reviewer (re-validated, 0 errors)

- han /ledger/4, /ledger/5 and zhao /ledger/18: counterpart later-zhou (the 951-960 CE state) -> eastern-zhou.
- han /ledger/10 note: the Zhaoxiang page dates the Shangdang attack to 262, not 265.
- yue /keyframe_review/5 (verdict ok -> adjust) and /6: corrections now keep Tancheng, as the K5 note says Tan stays Yue's to 333.

## zheng: thin

- [to do] `/ledger/8`: The 450 gain names cao as counterpart, but the cao dossier ends Cao in 487 (dissolve to song), so Cao cannot cede land in 450. Evidence: cao.json: identity.end -487, ledger 'dissolve' cp song; Zheng page: no 5th-century gain ('that period lists only ruler reigns'). Fix: Keep at confidence 1 but name the holder of the cells in 450 (song, which took Cao in 487) or drop the event and mark zheng_-450 adjust; say in the note that Cao was gone by 487.
- [to do] `/ledger/9`: The 450 gain names cai as counterpart, but the cai dossier ends Cai in 447 (to chu) and marks Cai's Cliopatria shapes wrong (they sit around Xuchang/Xinzheng, inside Zheng's country). Evidence: cai.json: end -447, keyframe cai_-750 'wrong' ('inside Zheng's country'). Fix: Drop the event (the cells were never Cai's) or re-attribute; keep confidence 1.
- [to do] `/ledger/3..7/note`: Notes L3-L7 repeat L2's sentence 'the page does not say whether Hui is the Kuai some sources name', and the notes field says Kuai is on no page. Evidence: Zheng page: Duke Wu 'annexed the state of Eastern Guo and defeated Kuai'. Fix: Delete the repeated sentence from L3-L7; in L2 and notes quote the Zheng page's 'defeated Kuai'.

Thin (for a gap-filler):
- `/ledger/8`: Why Zheng's shape doubles in 450 (25 cells from Cliopatria's Cao and Cai rows); page silent, confidence 1 (try https://en.wikipedia.org/wiki/Song_(state))
- `/ledger/9`: Same 450 change, Cai cells (try https://en.wikipedia.org/wiki/Cai_(state))
- `/keyframe_review/3`: zheng_-450 kept 'unverified: page budget' (not a fault) (try https://en.wikipedia.org/wiki/Zheng_(state))

Spot checks: `/ledger/0` confirmed: 'Zheng was founded in 806 BC when King Xuan of Zhou ...', lands in the royal domain near Hua County; `/ledger/4` confirmed: 'Eastern Guo (東虢): 767 BCE: to Zheng'; `/ledger/7` confirmed: 'Dai (戴): 713 BCE: to Zheng'; `/ledger/10` confirmed: 'In 375 BCE ... Zheng was annexed by Han state'; SA table '375 BCE: to Han'

Area: Zheng infobox gives no area; author's quoted areas (5,278; 10,403; 10,227; 10,125 km2) match shapes.csv.

## zhu: thin

- [to do] `/ledger/1`: The 450 loss names xu as counterpart, but the xu dossier ends Xu in 512 (conquered by Wu) and marks xu_-450 wrong. Evidence: xu.json: end -512, keyframe xu_-450 'wrong' ('Xu was extinguished', 512). Fix: Drop the event or re-attribute the 5 cells; keep confidence 1.

Thin (for a gap-filler):
- `/ledger/1`: 450 loss of 5 cells (Cliopatria only) (try https://en.wikipedia.org/wiki/Lu_(state))
- `/ledger/2`: 450 loss of 2 cells to Lu (Cliopatria only; Lu mirrors at confidence 1) (try https://en.wikipedia.org/wiki/Lu_(state))
- `/ledger/3`: Year of the Zhu-to-Zou rename (page gives Duke Mu of Lu's reign 417-377 only) (try https://en.wikipedia.org/wiki/Duke_Mu_of_Lu)

Spot checks: `/ledger/0` confirmed: infobox 'Regional State (1046-4th century BCE)'; 'King Wu of Zhou granted Cao Xia ... control'; `/ledger/3` confirmed: 'During the reign of Duke Mu of Lu (417 BC - 377 BC), Zhu's name was changed to Zou'; `/ledger/4` confirmed: 'Defeated and annexed the Zuo state around 348 BC'; table 'About 348 BC / Zou'; `/wars/0` confirmed: 659 BC meeting at Cheng, Lu defeats Zhu 'in the area of Yan'

Area: Zhu infobox gives no area (page: 'Its territory is now the county-level city of Zoucheng'); 6,650/5,422 km2 match shapes.csv.

## yue: fix

- [applied] `/keyframe_review/5`: yue_-404 was verdict ok with no correction, so Tan (Tancheng) drops out in 404 with no loss event, although the note says 'Tan (414) stays Yue's until the partition'. Evidence: Gazetteer: Tancheng cells are in yue_-450 and in the yue_-414 correction but not in Cliopatria's Yue 404 shape; SA table 'Tan (郯): 414 BCE: to Yue'. Fix: Applied by reviewer: verdict adjust, correction union[{cliopatria Yue -404}, Tancheng 30 km disc]; note amended.
- [applied] `/keyframe_review/6`: yue_-337 correction was the bare 337 shape, which also lacks Tancheng. Evidence: Same as above. Fix: Applied by reviewer: correction union[{cliopatria Yue -337}, Tancheng 30 km disc].
- [to do] `/ledger (missing, 414)`: No event for Yue's conquest of Teng in 414, which the teng dossier records (occupation_start cp yue, 414; occupation_end 333). Evidence: https://en.wikipedia.org/wiki/Teng_(state) infobox 'Conquered by Yue: 414 BCE'; 'It was conquered by King Zhugou of the Yue state'; 'Then its nobility re-established the country' (undated). Fix: Add a 414 gain (or occupation_start, matching teng) of Teng (Tengzhou, ~25 km) citing the Teng page, add the page to sources, and add Teng to the 414-333 corrections; the end of Yue's hold is undated (confidence 1).
- [to do] `/ledger/1`: Yue records 482-473 as contest_start/contest_end around the Wu capital while the wu dossier records occupation_start/occupation_end (cp yue) for the same years: the two disagree on the status of the land. Evidence: wu.json L5 482 occupation_start yue, L6 473 occupation_end yue; SA: 'In 482 ... Yue captured the Wu capital'. Fix: Agree one form with the wu dossier's owner (occupation of the capital 482-473 fits 'captured the Wu capital'); route to orchestrator.

Thin (for a gap-filler):
- `/ledger/0`: Founding date (infobox 'Established: ?'; Fu Tan is the fourth listed ruler and the first dated) (try https://en.wikipedia.org/wiki/Goujian)
- `/ledger/4`: Year of the court's move to Wu (Suzhou); page gives none (try https://en.wikipedia.org/wiki/Goujian)
- `/ledger/7`: 404 gain of 18 Lu cells (Cliopatria only) (try https://en.wikipedia.org/wiki/Lu_(state))
- `/ledger/8`: 404 loss of 35 cells to Chu (Cliopatria only; no chu mirror) (try https://en.wikipedia.org/wiki/Chu_(state))

Spot checks: `/ledger/1` confirmed: 'In 482, King Fuchai of Wu held an interstate conference ..., but Yue captured the Wu capital'; `/ledger/3` confirmed: 'Wu (吳): 473 BCE: to Yue'; 'King Goujian destroyed and annexed Wu in 473'; `/ledger/5` confirmed: 'Tan (郯): 414 BCE: to Yue'; `/ledger/11` confirmed: infobox 'Conquered by Chu: 333 BC'; 'Yue was partitioned by Chu and Qi in 333 BC' (Chu page table has '334 BC / Yue'; the dossier notes 334 or 333)

Area: Yue infobox gives no area; quoted areas match shapes.csv.

## han: fail

- [BLOCKING] `/keyframe_review/2/correction and /keyframe_review/3/correction`: The 366-338 corrections are union[Cliopatria Han 366/350, Yangzhai, Yiyang, Changzhi, Zheng] without the Anyi minus that K0/K1 apply, so Han holds Wei's capital Anyi in 366-338. Evidence: Gazetteer: Anyi (111.22, 35.14) is inside the han corrected shape at -360 and -345 (not at -372); Wei page: Anyi first capital, moved to Daliang 361 (Kaifeng page); Qin takes 'the former Wei capital Anyi in 286' (Zhaoxiang page). The author's notes say the dossier 'removes Anyi'. Fix: Wrap K2 and K3 corrections in minus[..., {lon 111.22, lat 35.14, km 45}] as in K0.
- [BLOCKING] `/keyframe_review/0..8/correction`: Every corrected Han shape keeps the Cliopatria Han cells around Luoyang: 15 of the 20 cells of the Zhou royal domain (eastern-zhou dossier) are Han's for 403-256. Evidence: Gazetteer overlap of the han corrected shape with eastern-zhou's shape: 15-16 cells at -400..-261 (13 at -300); Luoyang inside the han shape every year; eastern-zhou.json holds Luoyang/Wangcheng to 256. The author's notes flag Luoyang in Cliopatria's Han but the corrections do not remove it. Fix: Add minus {cliopatria: 'Later Zhou', year: <same year>} (the eastern-zhou shape) to every Han correction to 257.
- [BLOCKING] `/keyframe_review (missing 262-257)`: No keyframe covers 262-257: Cliopatria's han_-337 (span -337..-257) applies, and its correction re-adds Yiyang (lost to Qin 307) and the Shangdang disc (lost to Zhao 262). Evidence: Gazetteer: the han shape at -260 and -258 is han_-337's correction and contains Yiyang and Changzhi; overlap with the zhao shape 49 cells at -261. K4's note 'right for 337-308 only' is not machine-readable. Changping page: 262 Wang He 'invaded Shangdang'; Zhaoxiang page: Yiyang 'Captured ... in 307 BC'. Fix: Add a new keyframe han_-262 (from -262, to -257) with minus[union[Han -337, Yangzhai, Zheng], Qinyang disc] (no Yiyang, no Changzhi).
- [applied] `/ledger/4/counterpart, /ledger/5/counterpart`: Counterpart was 'later-zhou', the Five Dynasties Later Zhou (951-960); the Zhou royal domain is the eastern-zhou dossier (cliopatria_names ['Later Zhou'], -750..-256). Evidence: later-zhou.json identity 951-960; eastern-zhou.json -750..-256. Fix: Applied by reviewer: counterpart 'eastern-zhou' (re-validated, 0 errors).
- [applied] `/ledger/10/note`: The note said 'the Zhaoxiang page has Qin attacking Shangdang in 265'. Evidence: https://en.wikipedia.org/wiki/King_Zhaoxiang_of_Qin: the Shangdang attack is dated 262 ('Bai Qi attacked and cut off the Shangdang Commandery'); the 265 entry has Qin capture 'three cities' from Zhao. Fix: Applied by reviewer: note now says the Zhaoxiang page dates the Shangdang attack to 262.
- [to do] `/ledger/1`: The 376 gain of Jin's last land does not match the jin dossier, which dissolves Jin in 369 to han (confidence 2); zhao (and per the Warring States page quoted in this note, wei) has no 376 share. Evidence: SA table: 'Jin (晉): 376 BCE: to Han and Zhao'; jin.json L12 -369 dissolve cp han. Fix: Keep 376 (SA table) and tell the jin owner, or note the 369 alternative; add the zhao mirror (see zhao).
- [to do] `/identity/capitals, /identity/rulers`: Capitals and rulers end in 230 while the state is revived 208-207 (Han Cheng) with no capital or ruler. Evidence: https://en.wikipedia.org/wiki/Eighteen_Kingdoms lists Han Cheng as king of Hán (206). Fix: Add Han Cheng 208-207 to rulers (source Eighteen Kingdoms) or say in notes why not.

Thin (for a gap-filler):
- `/ledger/4`: 366 gain of 2 Zhou-domain cells (Cliopatria only; eastern-zhou has no loss) (try https://en.wikipedia.org/wiki/Eastern_Zhou)
- `/ledger/5`: 350 gain of 9 Zhou-domain cells (Cliopatria only) (try https://en.wikipedia.org/wiki/Eastern_Zhou)
- `/ledger/6`: 350 Han-Zhao exchange (Cliopatria only; zhao has no mirror) (try https://en.wikipedia.org/wiki/Han_(Warring_States))
- `/ledger/7`: 350 Han-Zhao exchange (Cliopatria only) (try https://en.wikipedia.org/wiki/Han_(Warring_States))
- `/ledger/8`: 337 loss of 34 cells to Qin (Cliopatria only; no qin mirror) (try https://en.wikipedia.org/wiki/Shang_Yang)
- `/ledger/14`: 247 loss of 2 cells to Chu (Cliopatria only) (try https://en.wikipedia.org/wiki/Chu_(state))
- `/ledger/16`: Year of Han Cheng's restoration (208 is Cliopatria's) (try https://en.wikipedia.org/wiki/Zhang_Liang_(Western_Han))
- `/ledger/17`: End of the restored Han in 207 (handoff to han-2 is Cliopatria's) (try https://en.wikipedia.org/wiki/Eighteen_Kingdoms)

Spot checks: `/ledger/2` confirmed: Han defeated and annexed Zheng in 375 and 'moved its capital there'; `/ledger/9` confirmed: Yiyang 'Captured the year before in 307 BC'; `/ledger/11` confirmed: 'Qin attacked the State of Han and captured Qinyang, which effectively cut off Han's Shangdang Commandery' (265); `/ledger/12` confirmed: 'the Qin army, led by Wang He, invaded Shangdang, and Feng Ting had to evacuate'; Feng Ting 'decided to offer the region to Zhao' (Han page dates the invasion 260; noted); `/ledger/15` confirmed: 'In 230 BC, the Qin army led by Neishi Teng ... conquered the Han capital Zheng'

Area: Han (Warring States) infobox gives no area; quoted areas match shapes.csv.

## wei: fail

- [BLOCKING] `/keyframe_review/3,4,5,6,7,8,9,10,11/correction`: The Daliang disc {place: Kaifeng, km: 100} used for 361-225 contains Han's capital Xinzheng (about 72 km from Kaifeng) and most of Zheng's former land, which the han dossier holds from 375. Evidence: Gazetteer: Xinzheng inside the wei corrected shape at -340, -290, -260, -240; overlap wei/han 66-134 cells every year 361-225 (134 at -360). Han page: capital 'Xinzheng (after 375 BC)' to 230. Fix: Shrink the Daliang disc (about 50 km) or minus the han shape (or {cliopatria: 'Zheng', year: -383}) from every Wei correction 361-225.
- [BLOCKING] `/keyframe_review/0/correction`: For 403-382 the correction keeps Cliopatria's whole Wei 404 shape, which contains Handan and Xingtai; the zhao dossier holds a Handan disc from 403, so 68 cells are claimed by both. Evidence: Gazetteer: Handan and Xingtai inside the wei shape at -400; overlap wei/zhao 68 cells at -400, 25 at -380. Zhongshan page supports only Zhongshan (407-381) for Wei on the plain; Handan page: Zhao capital from 386. Fix: Restrict the 403-382 Hebei part to Zhongshan (e.g. intersect Cliopatria Wei 404 with a disc around Lingshou/Pingshan and Dingzhou) and minus the zhao Handan disc.
- [to do] `/keyframe_review/1..11/correction`: After 381 the corrections hold no land in Hebei or Shandong although the Wei page says Wei 'included parts of modern-day Henan, Hebei, Shanxi, and Shandong'; the discs also omit Henei, the land north of the Yellow River between Anyi and Daliang. Evidence: https://en.wikipedia.org/wiki/Wei_(state): territory 'parts of modern-day Henan, Hebei, Shanxi, and Shandong'; Qin's wars page: Ye and Anyang taken from Zhao only in 236 (so where Wei's Hebei land lay is page-silent). Fix: State in the K1/K3 notes that the Hebei and Shandong parts are page-silent and left out, or add them from a page (e.g. Ximen Bao / Ye) if one is opened.
- [to do] `/ledger/13`: Western Wei's 206 gain names counterpart 'nobody', but the land (southern Shanxi) came out of the Qin collapse and Xiang Yu's division, not from stateless land. Evidence: https://en.wikipedia.org/wiki/Eighteen_Kingdoms: kingdoms 'created by military leader Xiang Yu in 206 BCE'. Fix: Use counterpart qin-dynasty (or western-chu as the allocator), confidence 2.
- [to do] `/ledger (missing)`: No mirror for the wey dossier's losses to wei (404 one cell; 320 'Wey controlled only the county of Puyang', confidence 1). Evidence: wey.json L6 -404 loss cp wei, L9 -320 loss cp wei. Fix: Add confidence-1 gains or tell the wey owner the cells are Cliopatria artefacts.

Thin (for a gap-filler):
- `/ledger/11`: Wei Jiu's restoration year and land (208 by inference) (try https://en.wikipedia.org/wiki/Wei_Jiu)
- `/ledger/12`: 206 transfer of the Henan lands to Western Chu (undated beyond the division) (try https://en.wikipedia.org/wiki/Eighteen_Kingdoms)
- `/wars/5`: 273 cession of 'Nanyang' not located (try https://en.wikipedia.org/wiki/Battle_of_Huayang)

Spot checks: `/ledger/1` confirmed: 'in 381, Zhongshan won its independence back'; conquered by Wei 407-406; `/ledger/2` confirmed: 'In 361 BC, King Hui of Wei relocated the Wei capital from the city of An ...'; `/ledger/7` confirmed: 'forced Wei to concede 400 li of Hedong lands' (290); `/ledger/8` confirmed: 'the former Wei capital' Anyi taken in 286; `/ledger/10` confirmed: 225 entry, Daliang flooded, 'King Jia of Wei surrendered'; `/ledger/14` confirmed: 'In October-November 205 BCE, Wei Bao ... lost the battle and was captured'

Area: Wei (state) infobox gives no area; quoted areas match shapes.csv.

## zhao: fail

- [BLOCKING] `/keyframe_review/7..13/correction`: After the 296 annexation Zhongshan is added as Cliopatria's Zhongshan 292 shape, which lies at 115.95-117.08 E, 38.57-39.99 N and does not contain Lingshou (Pingshan County), Zhengding or the Taihang foothills that the Zhongshan page names; together with the wei dossier's removal of Cliopatria's 'Wei' Hebei plain from 381, about 366 cells (~90,000 km2, 113.7-117.1 E, 36.9-40.2 N: Shijiazhuang, Dingzhou, Baoding, Hengshui) belong to no dossier for 381-222. Evidence: https://en.wikipedia.org/wiki/Zhongshan_(state): Lingshou capital 'until 296, when Zhongshan was conquered'; tombs at Pingshan County; Dongyuan in Zhengding County; Great Wall in Baoding. Gazetteer: Lingshou not in {cliopatria: Zhongshan, year: -292}; orphan check of {cliopatria: Wei, year: -326/-291} against all dossiers: 366-370 cells unclaimed at -300..-250. Fix: Add the Zhongshan core (Lingshou/Pingshan, Zhengding, Dingzhou, Baoding: e.g. intersect {cliopatria: Wei, year: -291} with Hebei, or discs) to the 296-229 corrections; note that Cliopatria's 'Wei' shapes from 326 contain Dai, Datong, Lingshou and Baoding and are probably Zhao's land mislabelled, and say who holds the plain 381-297.
- [to do] `/ledger (missing, 376)`: No event for Zhao's share of Jin's last land in 376, which the han dossier records from the same table. Evidence: SA table: 'Jin (晉): 376 BCE: to Han and Zhao'. Fix: Add a 376 gain cp jin (confidence 2, small disc, region the researcher's reading).
- [to do] `/ledger (missing, 350)`: No mirror for han's 350 gain from and loss to Zhao (confidence 1), although K3's note counts '22 from Han' and '15 to Han'. Evidence: han.json L6/L7 -350 cp zhao. Fix: Add the two confidence-1 events (intersect forms as in han) or drop them on both sides.
- [to do] `/ledger/8/region`: The 305 gain gives the whole Zhongshan shape while the page says 'parts of Zhongshan were annexed', and the keyframes add Zhongshan only from 296. Evidence: https://en.wikipedia.org/wiki/King_Wuling_of_Zhao: 'In the next year, parts of Zhongshan were annexed'. Fix: Narrow the region to a border part (e.g. a disc on the Zhao-Zhongshan border) or say the land is unlocated; keep confidence 2.
- [to do] `/ledger/18 and /keyframe_review/10,11/correction`: The 256 gain of 17 Zhou-domain cells conflicts with eastern-zhou, which loses Wangcheng to Qin in 256; K10/K11 keep those cells in Zhao. Evidence: eastern-zhou.json L4 -256 loss cp qin (confidence 3); Zhao is ~250 km from Luoyang. Fix: Drop the event or re-attribute to qin, and minus {cliopatria: 'Later Zhou', year: -257} from K10/K11.
- [applied] `/ledger/18/counterpart`: Counterpart was 'later-zhou' (951-960 CE); the Zhou royal domain is eastern-zhou. Evidence: later-zhou.json 951-960; eastern-zhou.json -750..-256. Fix: Applied by reviewer: counterpart 'eastern-zhou' (re-validated).
- [to do] `/keyframe_review/1/note`: K1 says Handan 'is added' in 386, but K0's correction already holds the Handan disc from 403. Evidence: K0 correction union includes {place: Handan, km: 60}. Fix: Say in K0 that Handan was the Zhao clan's before it became the capital, or drop the disc from K0.
- [to do] `/ledger/25`: Qin's mirror for 222 uses counterpart 'Dai (Prince Jia of Zhao)' rather than 'zhao'. Evidence: qin.json L39 -222 gain cp 'Dai (Prince Jia of Zhao)'. Fix: Route to the qin owner: counterpart should be 'zhao' (this dossier keeps Prince Jia's Dai).

Thin (for a gap-filler):
- `/ledger/2`: 366 loss of 62 cells to Zhongshan (Cliopatria only) (try https://en.wikipedia.org/wiki/Zhongshan_(state))
- `/ledger/3`: 350 gain of 79 cells of Cliopatria's 'Wei' Hebei shape (Cliopatria only) (try https://en.wikipedia.org/wiki/Battle_of_Guiling)
- `/ledger/4`: 350 loss of 38 cells to Qin (Cliopatria only) (try https://en.wikipedia.org/wiki/Zhao_(state))
- `/ledger/5`: 337 loss of 76 cells to Qin (Cliopatria only) (try https://en.wikipedia.org/wiki/Zhao_(state))
- `/ledger/15`: Who held Shangdang after Changping; the Zhaoxiang page says 'The combined forces recaptured Hedong, Anyang, Taiyuan, Pilao, Wu'an, Shangdang and Runan' (undated, after 257) (try https://en.wikipedia.org/wiki/King_Zhaoxiang_of_Qin)
- `/ledger/19`: 247 gain of 30 Wey cells (Cliopatria only; no wey mirror) (try https://en.wikipedia.org/wiki/Wey_(state))

Spot checks: `/ledger/7` confirmed: 'In 306 BCE the Zhao military launched expeditions into the northern territories'; Loufan and Linhu under a governor of Dai; `/ledger/9` confirmed: 'In 304 BCE the upper reaches of the Yellow River were invaded and taken from the Hu tribes'; Yunzhong and Jiuyuan 302; `/ledger/10` confirmed: 'After ten years of war Zhao annexed them in 296'; Wuling page 'In 296 BC'; Zhao page 295 (noted); `/ledger/13` confirmed: 'In April, the Zhao army first encountered the Qin army west of Gaoping Pass'; infobox April 262 - July 260; `/ledger/20` confirmed: 236 invasion, 'Zhao lost nine cities', Huan Yi 'captured Ye and Anyang'; `/ledger/22` confirmed: 'Qin captured King Youmiao and defeated Zhao in 228 BC'; `/ledger/25` confirmed: 'In 222 BC, Wang Ben led Qin forces to conquer Dai and captured Prince Jia'

Area: Zhao (state) infobox gives no area; quoted areas match shapes.csv.

## kingdom-of-han: fail

- [BLOCKING] `/keyframe_review/0/correction, /keyframe_review/1/correction, /ledger/0/region, /identity/predecessors/0/land`: Bashu is drawn as {region: 'Sichuan (region)'} (2,328 cells, 97.4-110.1 E, 26.2-34.2 N), which includes about 740 cells west of 102.5 E (the Ganzi/Aba plateau) outside both Cliopatria Han shapes; the corrected 206 shape (2,425 cells) is larger than Cliopatria's whole 206 shape (2,341 cells), which the K0 note calls 'far larger'. Evidence: Gazetteer: Sichuan region minus Cliopatria Han 206 = 934 cells, 740 of them west of 102.5 E; minus Han 203 = 889 cells. Eighteen Kingdoms table: 'Sichuan, Chongqing, southern Shaanxi' (modern-province words, not the Qin Ba and Shu commanderies). Fix: Replace the region with {intersect: [{cliopatria: 'Han', year: -206}, {region: 'Sichuan (region)'}]} (plus the Hanzhong disc) in K0, K1, L0 and the predecessor land, and correct the K0 note's area statement.
- [to do] `/ledger/5 vs /keyframe_review/2`: The Dai (Zhao Xie) gain is dated November 205 but the 204 keyframe (K2: Cliopatria Han 206 + Western Wei) does not hold Dai; it first appears in the 203 shape. Evidence: https://en.wikipedia.org/wiki/Chu%E2%80%93Han_Contention: 'In November 205 BCE, after Han Xin's victory at the Battle of Jingxing ...'. Fix: Add {cliopatria: 'Dai', year: -206} to K2's correction, or make the 205 event a vassal/occupation that the keyframes need not show.
- [to do] `/ledger/8`: The Yan gain is put in 203 (Cliopatria) although the page dates Yan's surrender to 204. Evidence: https://en.wikipedia.org/wiki/Chu%E2%80%93Han_Contention: 'In 204 BCE, after the Kingdom of Yan had surrendered to him, Liu Bang made Zhang Er the new King of Zhao'. Fix: Move to 204 at confidence 2 (or record it as a vassal_start of yan, since Yan kept its king), and add it to the 204 keyframe.
- [to do] `/identity`: The dossier says the Kingdom of Han and the Han dynasty are 'the same state under a new title'; rule 2 (one dossier per state, a title change is a rename) would put 206-203 in han-dynasty, and two dossiers will change colour in 202. Evidence: notes field; research brief section 6 rules. Fix: Orchestrator decision: fold kingdom-of-han into han-dynasty (ea-02) as its 206-203 years with a 202 rename, or give both the same colour.

Thin (for a gap-filler):
- `/ledger/9`: Year of Han Xin's conquest of Qi (page's 204 narrative, no explicit year) (try https://en.wikipedia.org/wiki/Battle_of_Wei_River)
- `/ledger/8`: Yan's status after 204 (client king) and its land (try https://en.wikipedia.org/wiki/Zang_Tu)

Spot checks: `/ledger/1` confirmed: 'By August or September 205 BC, the Three Qins and the Guanzhong region had come under Liu's control'; `/ledger/4` confirmed: Oct-Nov 205 Wei Bao captured; `/ledger/5` confirmed: 'In November 205 BCE, after Han Xin's victory at the Battle of Jingxing'; `/ledger/6` confirmed: 'In April-May 205 BCE, Liu Bang attacked Henei with help from Wei Bao'; `/ledger/10` confirmed: in 203 Liu Bang 'renounced the Treaty of Hong Canal'

Area: Wikipedia field is 'Han dynasty', whose infobox area is for CE years outside this life; not compared. Quoted areas (454,874; 1,310,598 km2) match shapes.csv.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| zheng -769 gain cp=Hui/Yan/Eastern Guo/Hu/Ji/Dai (769-713) | - | exception | Small Zhou states without dossiers; listed under counterparts_needing_dossiers (ea-01-x). |
| zheng -450 gain cp=cao | cao -487 dissolve | mismatch | Cao ended 487 (to song); no Cao land to cede in 450. Confidence 1. |
| zheng -450 gain cp=cai | cai -447 dissolve | mismatch | Cai ended 447 (to chu); cai marks its Cliopatria shapes wrong. Confidence 1. |
| zheng -375 loss cp=han | han -375 gain | matched |  |
| song -366 gain cp=zheng | zheng -375 dissolve | mismatch | Song takes Zheng cells in 366 but Zheng ended 375 (to han); song-side, confidence 1. |
| zhu -450 loss cp=xu | xu -512 dissolve | mismatch | Xu ended 512 (xu dossier marks xu_-450 wrong). Confidence 1. |
| zhu -450 loss cp=lu | lu -450 gain | matched | Both confidence 1. |
| qi -418 gain cp=zhu | - | mismatch | Qi records Xue and Pi as Zhu's; SA table lists 'Xue/Pi (薛/邳): 418 BCE: to Qi' as their own states; zhu has no loss. Route to qi owner. |
| zhu -348 loss cp=chu | chu -348 gain | matched |  |
| yue -482 contest_start cp=wu | wu -482 occupation_start | mismatch | Same years, different status (contest vs occupation of the Wu capital). |
| yue -473 gain cp=wu | wu -473 dissolve | matched |  |
| teng -414 occupation_start cp=yue | - | missing | Yue has no Teng event; Teng page infobox 'Conquered by Yue: 414 BCE'. Also teng -333 occupation_end. |
| yue -414 gain cp=Tan | - | exception | No dossier (ea-01-x). |
| yue -404 gain cp=lu | lu -404 loss | matched | Both confidence 1. |
| yue -404 loss cp=chu | - | missing | No 404 gain from yue in chu.json; confidence 1 (Cliopatria only). |
| yue -333 loss cp=qi | - | missing | qi.json has no 333 gain from yue. |
| yue -333 dissolve cp=chu | chu -333 gain | matched |  |
| han -403 found cp=jin | jin -403 split | matched |  |
| wei -403 found cp=jin | jin -403 split | matched |  |
| zhao -403 found cp=jin | jin -403 split | matched |  |
| han -376 gain cp=jin | jin -369 dissolve | mismatch | Jin ends 369 to han in jin.json; SA table gives 376 'to Han and Zhao'. Zhao lacks its share. |
| han -366 gain cp=eastern-zhou | - | missing | Slug fixed from later-zhou; eastern-zhou has no loss before 314. Confidence 1. |
| han -350 gain cp=eastern-zhou | - | missing | As above. |
| han -350 gain cp=zhao | - | missing | Same batch: zhao has no 350 loss to han. |
| han -350 loss cp=zhao | - | missing | Same batch: zhao has no 350 gain from han. |
| han -337 loss cp=qin | - | missing | qin.json silent; confidence 1. |
| han -307 loss cp=qin | - | missing | Yiyang, page-dated (Zhaoxiang page); qin.json lacks a 307 gain from han. |
| han -265 loss cp=qin | - | missing | Qinyang, page-dated (Changping page); qin.json lacks a 265 gain from han. |
| han -262 loss cp=zhao | zhao -262 gain | matched |  |
| han -247 loss cp=chu | - | missing | chu.json silent; confidence 1. |
| han -230 loss cp=qin | qin -230 gain | matched |  |
| han -208 gain cp=qin-dynasty | - | exception | qin-dynasty and han-2 are ea-02, not run yet. |
| qin -409 loss cp=wei | - | exception | Before wei's start (403); wei's found region includes Xihe and its war 409-406 is noted. |
| wei -381 loss cp=zhongshan | - | exception | zhongshan.json not written yet (ea-01, another part). |
| wei -328 loss cp=qin | qin -328 gain | matched |  |
| wei -290 loss cp=qin | qin -290 gain | matched |  |
| wei -286 loss cp=qin | qin -286 gain | matched |  |
| wei -225 loss cp=qin | qin -225 gain | matched |  |
| wey -404 loss cp=wei | - | missing | wei has no mirror; confidence 1. |
| wey -320 loss cp=wei | - | missing | wei has no mirror; confidence 1. |
| wei -206 loss cp=western-chu | - | exception | ea-02, not run yet. |
| wei -205 dissolve cp=kingdom-of-han | kingdom-of-han -205 gain | matched |  |
| zhao -366 loss cp=zhongshan | - | exception | No zhongshan dossier yet; also -305/-296 gains. |
| zhao -350 gain cp=wei | - | missing | Same batch: wei marks the source shape wrong and has no loss; confidence 1. |
| zhao -350 loss cp=qin | - | missing | qin.json silent; confidence 1. |
| zhao -337 loss cp=qin | - | missing | qin.json silent; confidence 1. |
| wey -366 loss cp=zhao | - | missing | zhao has no mirror; confidence 1. |
| zhao -306 gain cp=Loufan and Linhu | - | exception | Steppe peoples, no dossier; also Hu tribes 304. |
| zhao -260 loss cp=qin | qin -260 gain | matched | Both confidence 1. |
| zhao -256 gain cp=eastern-zhou | eastern-zhou -256 loss | mismatch | eastern-zhou loses to qin, not zhao. |
| zhao -247 gain cp=wey | - | missing | wey.json silent; confidence 1. |
| zhao -236 loss cp=qin | - | missing | Page-dated (Qin's wars: nine cities, Ye and Anyang); qin.json lacks a 236 gain from zhao. |
| zhao -228 loss cp=qin | qin -228 gain | matched |  |
| zhao -222 dissolve cp=qin | qin -222 gain | mismatch | qin uses counterpart 'Dai (Prince Jia of Zhao)'; should be zhao. |
| kingdom-of-han -205 gain cp=yong/sai/zhai/dai/yin | - | exception | ea-02, not run yet. |
| kingdom-of-han -205 gain cp=wei | wei -205 dissolve | matched |  |
| kingdom-of-han -203 gain cp=yan | - | missing | yan.json ends 202 with no loss to kingdom-of-han; page dates Yan's surrender 204. |
| kingdom-of-han -203 gain cp=qi | qi -204 dissolve | mismatch | qi dissolves 204 to han-dynasty; koh gains Qi in 203 (confidence 1). |

## Other problems

- Reviewer applied small fixes and re-validated (0 errors): han L4/L5 and zhao L18 counterpart later-zhou -> eastern-zhou; han L10 note (Zhaoxiang page dates Shangdang to 262); yue K5/K6 corrections now keep Tancheng (verdict ok -> adjust on yue_-404).
- Cliopatria's Warring States rows for Han, Wei and Zhao are garbled (gazetteer: Cliopatria 'Han' 404 holds Anyi and Luoyang; 'Zhao' holds Pingyang, Changzhi and Ye; 'Wei' 326/291 holds Dai, Datong, Lingshou, Baoding). The batch's disc-based corrections double-claim land (han/wei 66-134 cells every year 366-225; wei/zhao 17-68; han/eastern-zhou 15) and leave ~366 cells of the central Hebei plain unclaimed 381-222. A joint redraw of the three Jin states by one agent, with the Cliopatria shapes possibly relabelled (Wei 326+ as Zhao), is recommended over per-dossier patches.
- Overlaps inherited from neighbours, not this batch's fault: the chu dossier's shape covers Xinzheng and Yuzhou (Chu's oversized Cliopatria shape to 34.7 N; han/chu 52-66 cells); zhao/yan 59 cells from Cliopatria's Zhao 404 shape.
- No infobox in this batch gives an area (Zheng, Zhu, Yue, Han (Warring States), Wei (state), Zhao (state)); area_check is recorded as not applicable.
- Teng_(state) was opened to confirm the teng dossier's 414 Yue conquest (not one of the author's pages).
- zhongshan, qin-dynasty, han-2, han-dynasty, western-chu, yong, sai, zhai, dai, yin are not written yet (zhongshan: ea-01 part not yet run; the rest ea-02); their mirrors are exceptions.
