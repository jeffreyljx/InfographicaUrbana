# Review of batch ea-05 (2026-10-19)

Reviewer: adversarial review per history/briefs/reviewer-brief.md with the orchestrator's adjustments (4 spot checks per dossier; small page-verified fixes applied in place). Validator: 0 errors, 0 warnings for all twelve dossiers (`--resolve`). Keyframe steps measured with tools/gazetteer.py (H3 cells; areas approximate).

| slug | verdict |
| --- | --- |
| northern-song | fail |
| liao-dynasty | fail |
| great-jin | fail |
| western-xia | thin |
| kingdom-of-dali | thin |
| tsongkha | thin |
| khitan-confederation | thin |
| jurchen-confederation | thin |
| great-qi | thin |
| eastern-xia | fail |
| eastern-liao | fix |
| great-chu | pass |

## northern-song: fail

Findings:
- `/keyframe_review/3` (blocking): K3 (965-969) says Cliopatria's Northern Song 970 shape 'already contains Sichuan, Hubei and Hunan'; it does not contain Hunan, so the Song shape drops Hunan for 965-975 although L1 gained it in 963 and no event loses it. Evidence: Gazetteer resolve: 220 of the 224 thousand grid-km2 of admin1 Hunan lie outside {cliopatria: Northern Song, 970}; all but 4 lie inside {cliopatria: Southern Tang, 975}, a shape the southern-tang dossier marks 'wrong' (keyframes southern-tang_960/970) and excludes Hunan from (it lost Hunan to Wuping in 952-12). So Hunan 965-975 is in nobody's corrected shape; L4 (976) then re-gains it from the Southern Tang shape. Fix: K3, K4 and K5: union {admin1: Hunan, country: China} into the corrections (K4 northern-song_970 verdict ok -> adjust, its note's 'with Sichuan, Hubei and Hunan' corrected); /ledger/4 region = the southern-tang dossier's corrected 970 keyframe (or {minus: [ST975, Hunan, Fujian]}).
- `/keyframe_review/6` (blocking): K6 (976-977) and L4 take all of Fujian from the raw Cliopatria Southern Tang 975 shape two years early: Fuzhou was Wuyue's and Quanzhou-Zhangzhou Qingyuan Circuit's until 978. Evidence: All 138 thousand grid-km2 of admin1 Fujian lie inside {cliopatria: Southern Tang, 975}; wuyue.json gives Fuzhou (80 km disc) to northern-song in 978 and qingyuan-circuit.json dissolves in 978 with successor northern-song (Quanzhou, Zhangzhou discs); Five Dynasties page: 'Wuyue and Qingyuan Jiedushi gave up their land to Northern Song in 978'. The Song ledger has no event with counterpart qingyuan-circuit. Fix: Use the southern-tang dossier's corrected shape for /ledger/4 and K6; add gain 978 cp qingyuan-circuit (Quanzhou and Zhangzhou 60 km discs, Five Dynasties page) and the Fuzhou disc to the 978 Wuyue gain (/ledger/5); K7 = K6 plus both.
- `/keyframe_review/18` (blocking): Between K17 (1126-1129) and K18 (1130-1138) the Song loses about 600 thousand km2 (Henan, Shandong, Shaanxi, eastern Gansu, the Huai-north strip of Jiangsu and Anhui, and the Linxia, Lanzhou and Xining discs) with no loss event. Evidence: Ledger has only contest_start 1127-01 (Henan, Shandong, Shaanxi) and the 1139 gain back; no loss 1127-1130. Grid measure: K17 3,008k -> K18 2,231k cells-km2. Jin-Song wars page: 'Da Qi was formed late in 1130'; Zhang Jun 'was defeated by Wuzhu near Xi'an in late 1130'. great-qi is founded on part of it (counterpart great-jin) and great-jin's 1139 keyframes take the rest with no event, so the Huai-north strip, eastern Gansu and the NW discs belong to nobody in 1130-1138. Fix: Add loss 1130 (confidence 2, Jin-Song wars page) cp great-jin, region {minus: [<K17 correction>, {cliopatria: Southern Song, year: 1139}]}; great-jin adds the matching gain and the split to great-qi (see great-jin).
- `/keyframe_review/20` (blocking): K20 (Southern Song 1139 shape, valid from 1140) drops Henan and Shaanxi, gained in 1139 (/ledger/34), with only a contest_start in 1140; the loss is recorded in October 1142, two years after the keyframe and after the Jin's gain (great-jin /ledger/25, 1140). Evidence: Jin page: 'In 1140, the Jin retook Shaanxi and Henan'. Grid measure: K19 2,556k -> K20 2,231k cells-km2. Fix: Add loss 1140 cp great-jin of {union: [Henan, Shaanxi]} (Jin page, confidence 3), keep the 1142 loss for the rest of the Qinling-Huai renunciation (or narrow it), so that great-jin /ledger/25 is matched.
- `/ledger/12` (not blocking; route or fix with the neighbour): Ly-Song war: the Song side has contest 1075-1077 only, while ngo-dynasty records an occupation of Qinzhou, Lianzhou and Yongzhou 1075-1082 (cp northern-song) and a loss 1077 / gain 1082 of Quang Nguyen (Cao Bang, Lang Son) to and from the Song. Evidence: ngo-dynasty L12/L16 occupation_start 1075 / occupation_end 1082, L15 loss 1077, L17 gain 1082. Schema: the owner records an occupation 'with the roles reversed'. Ly-Song War page: 'In 1082 ... returned Yong, Qin, and Lian prefectures back to Song authorities', the Song 'relinquished its control of four prefectures and the county ... including ... Quang Nguyen'. Fix: Add occupation_start 1075 / occupation_end 1082 cp ngo-dynasty (Qinzhou and Nanning discs), gain 1077 and loss 1082 cp ngo-dynasty ({admin1: Cao Bang} and {admin1: Lang Son}, Vietnam); keep or end the contest at 1077.
- `/keyframe_review/12/note` (not blocking; route or fix with the neighbour): The note reads the 1056 step (+34.6 thousand km2) as Quang Nguyen, but the Song 1056 shape lies wholly in China. Evidence: shapes.csv northern-song_1056 modern_countries 'China'; the added cells (bbox 105.6-108.4 E, 21.9-25.5 N) are in Guangxi; the Ly-Song War page puts Quang Nguyen in Cao Bang and has the Song hold it only 1077-1082. Fix: Rewrite the note: the 1056 step is a Guangxi border adjustment the pages do not date; Quang Nguyen is handled by the 1077/1082 events above.
- `/ledger` (not blocking; route or fix with the neighbour): Great Chu (great-chu found 1127-04 cp northern-song, dissolve 1127-05 with successor northern-song) has no Song mirror; the Song keyframe K17 keeps Kaifeng throughout. Evidence: great-chu ledger L0/L1 and identity.successors; Zhang Bangchang infobox: reign 20 April 1127 - 23 May 1127. Fix: Add loss 1127-04 and gain 1127-05 cp great-chu of {place: Kaifeng, km: 100}, or state in notes that the one-month puppet is drawn inside the contested zone (exception).

Gaps for a gap-filler:
- `/ledger/18`: 1113 loss of Qingtang (Xining) to Western Xia at confidence 1; the Tsongkha page has the Song there in 1108 and the Jin ceding it to Xia in 1136 (try https://en.wikipedia.org/wiki/Song%E2%80%93Xia_wars)
- `/ledger/46`: 1260 loss of western Sichuan at confidence 1; no page dates it (try https://en.wikipedia.org/wiki/Siege_of_Diaoyu_Castle)
- `/keyframe_review/22`: the 1250 step (10 thousand km2 in Sichuan) is unverified (try https://en.wikipedia.org/wiki/Mongol_conquest_of_the_Song_dynasty)
- `/ledger`: Song gains in Henan in 1234 (the great-jin dossier's /ledger/45 note: the Song got 'parts of Henan'); none in the Song ledger (try https://en.wikipedia.org/wiki/Mongol_conquest_of_the_Jin_dynasty)

Spot checks: `/ledger/1` confirmed (Five_Dynasties_and_Ten_Kingdoms_period: 'The kingdom fell to advancing armies of the Song in 963'; Wuping: 'In 963, the region was annexed by Song dynasty'); `/ledger/3` confirmed (Five_Dynasties_and_Ten_Kingdoms_period: '... Later Shu in 965, Southern Han in 971, and Southern Tang in 975'); `/ledger/43` confirmed (Mongol_conquest_of_the_Song_dynasty: Xiangyang 'capitulated in 1236'); `/ledger/45` confirmed (Mongol_conquest_of_the_Song_dynasty: 'The only permanent gain was Chengdu for the Mongols in 1241'); `/ledger/52` confirmed (Mongol_conquest_of_the_Song_dynasty: 'Yangzhou in 1276, Chongqing in 1277 and Hezhou in 1279'); `/ledger/19` confirmed (Sixteen_Prefectures: 'In 1123, the Jin ceded most of the territories except Yunzhou to the Song' ... 'retook them ... in 1125'); `/ledger/37` confirmed (Treaty_of_Shaoxing: 'formally ratified on 11 October 1142').
Area: infobox 3100000 (980) against Cliopatria 2765922, ratio 0.89; acknowledged True. 

## liao-dynasty: fail

Findings:
- `/ledger` (blocking): No vassal pair for the Later Jin (936-942), the Liao's best-known client; the later-jin dossier records it inverted (vassal_start 936-11, vassal_end 942 with counterpart liao-dynasty). Evidence: Schema (ledger.type): vassal events go in the suzerain's dossier with 'counterpart' the vassal itself. Liao page: 'In 938, the puppet emperor of Later Jin transferred the Sixteen Prefectures over to the Khitans'; later-jin L1 note: 'the Later Jin is founded as a Liao client' (28 November 936), L8: 'Summer 942: Shi Chonggui breaks the subordination'. Fix: Add vassal_start 936-11 and vassal_end 942 cp later-jin, region {cliopatria: Later Jin, year: 936} (minus the Sixteen Prefectures from 938), sources the Later Jin and Shi Chonggui pages; ask ea-04 to drop its inverted pair.
- `/ledger/9` (not blocking; route or fix with the neighbour): 947: the Liao records only an occupation of a 100 km Kaifeng disc with counterpart later-jin, while later-jin loses its whole realm to the Liao (947-01) and later-han gains the Central Plain from the Liao (947). Evidence: later-jin L11 947-01 loss cp liao-dynasty ('annihilated the Later Jin and annexed its former territories in 947'); later-han L0 947 gain cp liao-dynasty. An occupation needs an owner, and later-jin dissolves in 947-01. Fix: Either: gain 947-01 cp later-jin ({cliopatria: Later Jin, year: 936} minus the Sixteen Prefectures) and loss 947 cp later-han, replacing the occupation pair; or keep the occupation and have ea-04 change later-jin's loss to a dissolve and later-han's gain counterpart. Route to ea-04.
- `/ledger` (not blocking; route or fix with the neighbour): goryeo records a loss of the Sinuiju area to the Liao in 1014 and a gain back in 1031; the Liao has no mirror. Evidence: goryeo L9 1014 loss cp liao-dynasty ({place: Sinuiju, km: 50}), L11 1031 gain cp liao-dynasty. Fix: Add gain 1014 / loss 1031 cp goryeo if the pages support them, otherwise route to jk-02 to justify the goryeo pair.
- `/ledger/26` (not blocking; route or fix with the neighbour): The 1124 split gives the Kara-Khitans the whole Mongolian Plateau, while kara-khitans.json founds on the Orkhon Valley only, and K11 (1122-1125) keeps the steppe in the Liao shape. Evidence: kara-khitans L0 1124 found region {region: Orkhon Valley}; Liao K11 has no 1124 change. Fix: Make /ledger/26 {region: Orkhon Valley} (or agree a wider region with ia-01) and remove it from the Liao shape for 1124-1125.
- `/ledger/20` (not blocking; route or fix with the neighbour): contest_start 1114-11 names great-jin, which did not exist until January 1115; jurchen-confederation carries the 1114-11 to 1115-01 contest with the Liao. Evidence: Wanyan Aguda page: 'In January 1115 ... Aguda proclaimed himself emperor'; jurchen-confederation L5/L6. Fix: contest_start 1114-11 and contest_end 1115-01 cp jurchen-confederation, then contest_start 1115-01 cp great-jin (paired with /ledger/27).

Gaps for a gap-filler:
- `/ledger/3`: 922 steppe gain at confidence 1 (199 thousand km2 of Inner Mongolia, undated) (try https://en.wikipedia.org/wiki/Emperor_Taizu_of_Liao)
- `/ledger/5`: 926 Mongolian steppe gain at confidence 1 (try https://en.wikipedia.org/wiki/Emperor_Taizu_of_Liao)
- `/ledger/18`: 1074 Jurchen vassal_start at confidence 1 ('by the 11th century') (try https://en.wikipedia.org/wiki/Jurchen_people)

Spot checks: `/ledger/8` confirmed (Liao_dynasty: 'In 938, the puppet emperor of Later Jin transferred the Sixteen Prefectures over to the Khitans'); `/ledger/14` confirmed (Liao_dynasty: treaty signed 'January 1005'; 'finalize the location of their disputed border'); `/ledger/26` confirmed (Liao_dynasty: 'In 1124 the successor state established by Yelü Dashi in the Western Regions'); `/ledger/22` confirmed (Jin_dynasty_(1115%E2%80%931234): 'The Jin captured the Supreme Capital in mid-1120'); `/ledger/17` confirmed (Liao_dynasty: 'In 1066 Emperor Daozong of Liao reintroduced the dynastic name Great Liao').
Area: infobox 2600000 (947) against Cliopatria 1924516, ratio 0.74; acknowledged True. 

## great-jin: fail

Findings:
- `/keyframe_review/5` (blocking): The Jin never gains the Song lands north of the Qinling-Huai line, yet its vassal Qi is founded on them in 1130 (great-qi: predecessor and counterpart great-jin) and the Jin takes them back from Qi in 1137 (/ledger/21). Evidence: Jin ledger has contest_start 1127-01 and vassal_start 1130 cp great-qi, no gain 1127-1130; K5 (1126-1136) = the 1126 shape plus Hebei and Shanxi only. Jin page: Liu Yu 'defected to the Jin in 1128'; Jin-Song wars page: 'Da Qi was formed late in 1130, and the Jin enthroned Liu as its emperor'. Fix: Add gain 1130 cp northern-song, region {minus: [<northern-song K17 correction>, {cliopatria: Southern Song, year: 1139}]} (the same spec as the Song's new 1130 loss), then split 1130 cp great-qi with Qi's K0 region; extend K5 for 1130-1136 by the part not given to Qi (eastern Gansu, Huai-north Jiangsu and Anhui, the Linxia, Lanzhou and Xining discs).
- `/keyframe_review/7` (blocking): The 1139 keyframes (K7, K8) add about 145 thousand km2 that the 1137 keyframe lacks, with no event. Evidence: Gazetteer resolve of K7 minus K6: Gansu 80k, Ningxia 38k, Jiangsu 26k, Anhui 25k, Inner Mongolia 12k grid-km2 (grid overstates true area by about a fifth). No 1137-1139 event names these lands. Fix: The 1130 gain above explains it; if the author keeps the plain-only reading instead, add a gain naming {admin1: Gansu}, Ningxia and the Huai-north strip.
- `/ledger` (not blocking; route or fix with the neighbour): western-xia /ledger/14 gains the Xining area from the Jin in 1136; the Jin has no loss (and never held it). Evidence: Tsongkha page: 'The area was later conquered by the Jin dynasty ... which ceded the area to the Western Xia in 1136'. Fix: After the 1130 gain, add loss 1136 cp western-xia ({place: Xining, km: 100}).
- `/keyframe_review/14` (not blocking; route or fix with the neighbour): great-jin_1227 is marked adjust with 'unchanged shape; use the 1223 and 1231 keyframes instead': the shape is valid in no year, so a compiler may draw its 784 thousand km2 for 1227-1230 over the 1223 keyframe. Evidence: K12 (1223-1230) and K13 (1231-1232) remove Hebei, Shanxi, Shandong and Shaanxi; K14 has no from/to. Fix: Verdict wrong, correction = the K12 spec, text 'superseded 1227-1230 by the 1223 keyframe and from 1231 by the 1231 and 1233 keyframes'.

Spot checks: `/ledger/3` confirmed (Jin_dynasty_(1115%E2%80%931234): 'The Jin captured the Supreme Capital in mid-1120'); `/ledger/6` confirmed (Jin_dynasty_(1115%E2%80%931234): 'In the winter, Aguda took the Southern Capital' (winter 1122)); `/ledger/8` confirmed (Jin_dynasty_(1115%E2%80%931234): 'declared himself a vassal of Jin in 1124'); `/ledger/15` confirmed (Jin_dynasty_(1115%E2%80%931234): 'in 1126, the king of Goryeo declared himself a Jin vassal (tributary)'); `/ledger/25` confirmed (Jin_dynasty_(1115%E2%80%931234): 'In 1140, the Jin retook Shaanxi and Henan'); `/ledger/41` confirmed (Mongol_conquest_of_the_Jin_dynasty: 'Zhongdu fell to the Mongols on June 1, 1215'); `/ledger/43` confirmed (Mongol_conquest_of_the_Jin_dynasty: 'In 1231, the Mongols attacked again and finally took Fengxiang').
Area: infobox 3610000 (1142) against Cliopatria 2117224, ratio 0.59; acknowledged True. 1186: 4,750,000 against 2,118,396 (ratio 0.45), acknowledged in K5's note (the infobox counts the tribal sphere)

## western-xia: thin

Gaps for a gap-filler:
- `/ledger/13`: 1113 gain of Qingtang at confidence 1; the pages disagree (Song-Xia wars 1113; Tsongkha page: Jin cession 1136); neither gain is drawn (try https://en.wikipedia.org/wiki/Tsongkha)
- `/ledger`: xiliangfu.json records Western Xia occupations of Liangzhou 1003-1004 and 1015-1016 (cp western-xia); no Xia mirror (try https://en.wikipedia.org/wiki/Xiliangfu)
- `/ledger/2`: 1032 gain names xiliangfu, which ends in 1016 in xiliangfu.json (dissolve cp ganzhou-kingdom); the Western Xia page has 'In 1032, Yuanhao annexed the Tibetan confederation of Xiliangfu'. Flagged by the author; the two dossiers must agree on who held Liangzhou in 1016-1032 (try https://en.wikipedia.org/wiki/Xiliangfu)
- `/identity/capitals/0`: capital before 1038 (Yinzhou is an approximate site; page silent); Li Deming's move to Xingzhou is the lead (try https://en.wikipedia.org/wiki/Li_Deming)

Spot checks: `/ledger/2` confirmed (Western_Xia: 'In 1032, Yuanhao annexed the Tibetan confederation of Xiliangfu'); `/ledger/3` confirmed (Western_Xia: 'By 1036, he had annexed both the Ganzhou Uyghur Kingdom and the Guiyi Circuit'); `/ledger/11` confirmed (Song%E2%80%93Xia_wars: 'In October, Li Xian took Lanzhou' (summer 1081 invasion)); `/ledger/18` confirmed (Mongol_conquest_of_Western_Xia: 'In August 1226 ... his troops approached' Wuwei; 'took Liangzhou'); `/ledger/20` confirmed (Mongol_conquest_of_Western_Xia: 'In September 1227, Emperor Mozhu surrendered to the Mongols').
Area: infobox 1000000 (1100) against Cliopatria 473560, ratio 0.47; acknowledged True. body gives 800,000 at its peak (ratio 0.59); K3 keeps the shape with reasons

## kingdom-of-dali: thin

Gaps for a gap-filler:
- `/identity/rulers`: rulers 944-1094 and 1096-1256 (the list pages failed); the Dali Kingdom page's ruler section and the Duan Xingzhi page are the leads (try https://en.wikipedia.org/wiki/Duan_Xingzhi)
- `/certainty/0`: no boundary on any page; Cliopatria's shape carried as drawn (try https://en.wikipedia.org/wiki/Dali_Kingdom)
- `/ledger/5`: mongol-empire has vassal_start 1253 cp kingdom-of-dali and vassal_end + gain 1260 at confidence 1, after Dali's 1256 end; the two dossiers should agree (route to ia-02) (try https://en.wikipedia.org/wiki/Dali_Kingdom)

Spot checks: `/ledger/0` confirmed (Dali_Kingdom: 'Duan Siping seized power in 937, establishing himself at Dali'); `/ledger/1` confirmed (Dali_Kingdom: 1094: Gao Shengtai 'renamed the Dali Kingdom to "Dazhong Kingdom"'); `/ledger/2` confirmed (Dali_Kingdom: 1096: Duan Zhengchun 'restored the kingdom's former name'); `/ledger/5` confirmed (Dali_Kingdom: 'In 1256, Duan Xingzhi surrendered and presented to Möngke maps of Yunnan').
Area: infobox None (None) against Cliopatria 360583, ratio None; acknowledged True. the infobox gives no area

## tsongkha: thin

Gaps for a gap-filler:
- `/keyframe_review/1`: the 1032 step adds the Xining disc with only a capital_move; the page has Gusiluo 'enthroned at Kuozhou' in 1008 and 'relocated to Miaochuan' in 1025 (both Hehuang), so the Xining area was held from 1008: add a gain (cp nobody) in 1008 and start the Xining disc then (try https://en.wikipedia.org/wiki/Tsongkha)
- `/identity/capitals`: capitals 1008-1031 (Kuozhou, Miaochuan) left out because the gazetteer lacks them; capitals need only coordinates (try https://en.wikipedia.org/wiki/Gusiluo)
- `/ledger/0`: found 997 at confidence 1; rulers start in 1008 (try https://en.wikipedia.org/wiki/Gusiluo)

Spot checks: `/ledger/1` confirmed (Tsongkha: 'In 1032 Gusiluo relocated to Qingtang'); `/ledger/4` confirmed (Tsongkha: 'In 1072 ... Wang Shao attacked Mucheng and gained control of Wushengjun (Xizhou) and Hezhou'); `/ledger/5` confirmed (Tsongkha: 1099: Wang Shan defeated Longza and occupied Tsongkha); `/ledger/7` confirmed (Tsongkha: 'In 1103, the Song dispatched Wang Hou to conquer Tsongkha').
Area: infobox None (None) against Cliopatria None, ratio None; acknowledged True. no Cliopatria shape, no infobox area

## khitan-confederation: thin

Gaps for a gap-filler:
- `/keyframe_review/0`: one keyframe for 628-906; Xianzhi Khagan's subjugation of the Kumo Xi and Shiwei (860?-882?) and the Yaonian expansion are not placed (try https://en.wikipedia.org/wiki/Khitan_people)
- `/ledger`: the Uyghur overlordship 755-840 belongs in uyghur-khaganate.json, which has no Khitan event; the Tang's Songmo commandery (648) and the 696-714 war have no counterpart events in tang-dynasty.json (try https://en.wikipedia.org/wiki/Uyghur_Khaganate)
- `/notes`: the notes call Cliopatria's Liao 911 shape 374 thousand km2; shapes.csv has 265,794 km2 (374 is a grid-cell count) (try https://en.wikipedia.org/wiki/Liao_dynasty)

Spot checks: `/ledger/0` confirmed (Khitan_people: 'The Dahe Confederation submitted to the Tang in both 628 and 648'); `/ledger/1` confirmed (Khitan_people: 'In 696, a famine occurred in Khitan territory ... sparking a rebellion'); `/ledger/2` confirmed (Khitan_people: 'from 700 to 714 before the Tang were able to reassert control over the Khitans'); `/ledger/3` confirmed (Khitan_people: 'The rebellion of Ketuyu ended Dahe supremacy in 730').
Area: infobox None (None) against Cliopatria None, ratio None; acknowledged True. no Cliopatria shape, no infobox area

## jurchen-confederation: thin

Gaps for a gap-filler:
- `/keyframe_review/1`: K1 (1104-1106) adds Hamgyong-namdo with only a contest_start; the Timeline page's 1104 entry ('defeat Im Gan, taking Chongju castle') supports a gain (cp goryeo, whose ledger also has only a contest_start) (try https://en.wikipedia.org/wiki/Timeline_of_the_Jurchens)
- `/ledger`: the Jurchen tribes and lands before 1074 (748 onward) are not drawn (try https://en.wikipedia.org/wiki/Jurchen_people)

Spot checks: `/ledger/0` confirmed (Timeline_of_the_Jurchens: '1074: Wugunai of the Wanyan clan unites the Jurchens of eastern and northern Manchuria'); `/ledger/1` confirmed (Timeline_of_the_Jurchens: 1104: 'Wanyan clan enters Goryeo territory ... taking Chongju castle'); `/ledger/2` confirmed (Timeline_of_the_Jurchens: 1107: 'Goryeo invasion led by Yun Kwan ... builds Nine Fortresses' (the month is from the Jurchen page, not reopened)); `/ledger/3` confirmed (Timeline_of_the_Jurchens: 1108: 'Goryeo returns the Nine Fortresses region to the Wanyan clan').
Area: infobox None (None) against Cliopatria None, ratio None; acknowledged True. no Cliopatria shape, no infobox area

## great-qi: thin

Gaps for a gap-filler:
- `/identity/capitals`: first capital Daming (1130-1131) left out because the gazetteer lacks it; Daming (Hebei) also lies outside the Qi shape, which leaves out Hebei (try https://en.wikipedia.org/wiki/Jin%E2%80%93Song_wars)
- `/keyframe_review/0`: extent is a reading (no Wikipedia article): the Huai-north strip and eastern Gansu are not in Qi and must go to the Jin in 1130 (see great-jin and northern-song), or be added here (try https://en.wikipedia.org/wiki/Yue_Fei)

Spot checks: `/ledger/0` confirmed (Jin%E2%80%93Song_wars: 'Da Qi was formed late in 1130, and the Jin enthroned Liu as its emperor'); `/ledger/2` confirmed (Emperor_Gaozong_of_Song: 'With Jin support, Da Qi invaded the Song in November 1133'); `/ledger/3` confirmed (Emperor_Gaozong_of_Song: 'In 1134, Yue Fei defeated Li and retook Xiangyang and its surrounding prefectures'); `/ledger/5` confirmed (Jin%E2%80%93Song_wars: 'In late 1137, the Jin reduced Liu Yu's title to that of a prince and abolished the state of Qi').
Area: infobox None (None) against Cliopatria None, ratio None; acknowledged True. no article, no Cliopatria shape

## eastern-xia: fail

Findings:
- `/keyframe_review/0` (blocking): The 1215-1216 capital Dongjing (Liaoyang, 123.18 E 41.28 N, /identity/capitals/0) lies outside the 1215-1216 shape (Jilin, Heilongjiang, Primorye); the capital marker would fall in Eastern Liao's Liaoning. Evidence: Eastern Xia page: Puxian Wannu 'founded the Eastern Xia dynasty in Dongjing' in 1215; Puxian Wannu page: 'In 1217 he moved from Dongjing to the Tumen River basin'. The Eastern Liao page also has Yelu Liuge occupy the Jin eastern capital in 1215 (flagged in the author's notes, but left inconsistent). Fix: Add {place: Liaoyang, km: 60} to K0's union for 1215-1216, and record the overlap with eastern-liao (contest_start 1215 / contest_end 1217 over the Liaoyang disc, cp eastern-liao, in both dossiers); or, if the author reads Liaoyang as Eastern Liao's, end the Dongjing capital entry and say why.

Gaps for a gap-filler:
- `/ledger/3`: 1217 gain of Hamgyong-namdo at confidence 1 (who held it before is not on the page) (try https://en.wikipedia.org/wiki/Puxian_Wannu)
- `/ledger`: Mongol vassalage (hostage 1216, revolts 1217 and 1222) belongs in mongol-empire.json, which has no eastern-xia event (try https://en.wikipedia.org/wiki/Eastern_Xia)

Spot checks: `/ledger/0` confirmed (Eastern_Xia: Puxian Wannu 'founded the Eastern Xia dynasty in Dongjing' in 1215; 'a short-lived kingdom established in Manchuria'); `/ledger/1` confirmed (Puxian_Wannu: 1217 paragraph: 'He again named his kingdom Eastern Xia or Dongxia'); `/ledger/3` confirmed (Puxian_Wannu: same 1217 paragraph: 'His domain extended north to Laoyeling Mountains, south to Hamgyŏngnamdo'); `/ledger/6` confirmed (Puxian_Wannu: 'In 1233 Ögedei's son Güyük attacked Eastern Xia ... and captured Puxian Wannu').
Area: infobox None (None) against Cliopatria None, ratio None; acknowledged True. no Cliopatria shape, no infobox area

## eastern-liao: fix

Findings:
- `/identity/rulers` (applied by reviewer): Rulers stopped at 1238 and left 1220-1226 empty although the page lists all of them; the note said 'The page names no ruler for 1220-1226'. Evidence: Eastern Liao infobox: '1238-1259: Yelü Shouguonu'; '1259-1269: Yelü Gunai'; rulers table: 'Empress Yaoli ... 1220-1226', footnote 'Regent'. Fix: Added Empress Yaoli (regent) 1220-1226, Yelu Shouguonu 1238-1259 and Yelu Gunai 1259-1269 with the page as source; corrected Yelu Xuedu's note. Re-validated: 0 errors, 0 warnings.
- `/identity/capitals` (applied by reviewer): No capital although the page names one (the author left it out because the gazetteer lacks Kaiyuan; capitals need only coordinates). Evidence: Infobox 'Capital: Zhongjing'; 1214: Liuge 'set his capital at modern Kaiyuan and named it Zhongjing'. Fix: Added Zhongjing (modern Kaiyuan, Liaoning), 124.04 E 42.55 N, 1214-1269. Re-validated: 0 errors, 0 warnings.
- `/keyframe_review/0` (not blocking; route or fix with the neighbour): K0 holds all of Liaoning 1212-1269, including Dongjing (Liaoyang), which eastern-xia uses as its 1215-1216 capital. Evidence: Eastern Liao page: 'In 1215, Yelü Liuge occupied the eastern capital'; the same page and the Eastern Xia page put the Eastern Xia founding at Dongjing in 1215. Fix: Settle with eastern-xia (see its fix): a contest over the Liaoyang disc 1215-1217 in both dossiers.

Gaps for a gap-filler:
- `/ledger/5`: 1216 Later Liao contest at confidence 1 with 'the page gives no land'; the page says Later Liao was 'based in modern Haicheng' (Haicheng is not in the gazetteer) (try https://en.wikipedia.org/wiki/Eastern_Liao)
- `/keyframe_review/0`: all of Liaoning for 57 years is a reading; the page gives no territory after 1215 (try https://en.wikipedia.org/wiki/Eastern_Liao)
- `/ledger`: Mongol vassalage from 1220 ('became a vassalage of the Mongol Empire') belongs in mongol-empire.json, which has no eastern-liao event (try https://en.wikipedia.org/wiki/Eastern_Liao)

Spot checks: `/ledger/0` confirmed (Eastern_Liao: 'rebelled against the rule of the Jurchen-led Jin dynasty in 1212'); `/ledger/1` confirmed (Eastern_Liao: 'In 1213, Yelü Liuge proclaimed himself king'); `/ledger/2` confirmed (Eastern_Liao: 1214: 'set his capital at modern Kaiyuan and named it Zhongjing'); `/ledger/6` confirmed (Eastern_Liao: 'In the spring of 1219, the Later Liao ruler Yelü Hanshe committed suicide'); `/ledger/7` confirmed (Eastern_Liao: 'In 1269, the Yuan dynasty abolished the title').
Area: infobox None (None) against Cliopatria None, ratio None; acknowledged True. no Cliopatria shape, no infobox area

## great-chu: pass

Spot checks: `/ledger/0` confirmed (Jin%E2%80%93Song_wars: 'In 1127, the Jurchens installed a former Song official, Zhang Bangchang'); `/ledger/1` confirmed (Da_Chu: 'abolished scarcely a month after its formation'; Zhang Bangchang infobox 'Reign: 20 April 1127 - 23 May 1127').
Area: infobox None (None) against Cliopatria None, ratio None; acknowledged True. no territory on any page; the Jiankang capital conflict is flagged in notes; tried: dates, rulers, predecessor/successor chain (the missing Song mirror is listed under northern-song)

## Cross-dossier matrix (mismatches and missing mirrors only)

- northern-song 976 gain cp southern-tang -> southern-tang 976 loss: **mismatch**. Song gains the raw Cliopatria ST975 shape (with Hunan, all Fujian, Guangxi); southern-tang loses its corrected realm only
- northern-song 978 gain cp wuyue -> wuyue 978 dissolve: **mismatch**. wuyue's successor land includes the Fuzhou disc; the Song's gain region (Wuyue 977 shape) does not
- qingyuan-circuit 978 dissolve cp northern-song -> northern-song - -: **missing**. no Song gain cp qingyuan-circuit (Quanzhou, Zhangzhou)
- ngo-dynasty 1075 occupation_start cp northern-song -> northern-song 1075 contest_start: **mismatch**. Song should record the occupation (roles reversed) to 1082
- ngo-dynasty 1077 loss cp northern-song -> northern-song - -: **missing**. Quang Nguyen (Cao Bang, Lang Son) to the Song
- ngo-dynasty 1082 gain cp northern-song -> northern-song - -: **missing**. Quang Nguyen back to Dai Viet; occupation_end 1082 also unmirrored
- great-chu 1127 found cp northern-song -> northern-song - -: **missing**. one-month puppet on the Kaifeng disc; no Song loss/gain
- northern-song 1130 loss (absent) cp great-jin -> great-jin - -: **missing**. K17->K18 drops ~600k km2 north of the Qinling-Huai line with no loss; Jin has no gain; great-qi founded 1130 cp great-jin
- great-qi 1130 found cp great-jin -> great-jin 1130 vassal_start: **mismatch**. Jin never held the land it gives Qi; needs a Jin gain from the Song and a split
- great-jin 1140 gain cp northern-song -> northern-song 1139 contest_end: **mismatch**. the Song has no 1140 loss of Henan and Shaanxi; its 1139 gain is undone only by the 1142 loss
- northern-song 1236 loss cp mongol-empire -> mongol-empire - -: **missing**. Xiangyang; route to ia-02
- northern-song 1239 gain cp mongol-empire -> mongol-empire - -: **missing**. Xiangyang retaken; route to ia-02
- northern-song 1273 loss cp mongol-empire -> mongol-empire - -: **missing**. Xiangyang/Fancheng; route to ia-02
- later-jin 936 vassal_start cp liao-dynasty -> liao-dynasty - -: **missing**. inverted: the Liao (suzerain) must carry vassal_start 936-11 / vassal_end 942 cp later-jin
- liao-dynasty 947 occupation_start cp later-jin -> later-jin 947 loss: **mismatch**. later-jin loses its realm to the Liao; later-han gains it from the Liao (947); the Liao records only a Kaifeng occupation
- later-han 947 gain cp liao-dynasty -> liao-dynasty - -: **missing**. no Liao loss to later-han
- goryeo 1014 loss cp liao-dynasty -> liao-dynasty - -: **missing**. Sinuiju area; route both ways (jk-02)
- goryeo 1031 gain cp liao-dynasty -> liao-dynasty - -: **missing**. Sinuiju area back to Goryeo
- liao-dynasty 1124 split cp kara-khitans -> kara-khitans 1124 found: **mismatch**. Liao splits off the Mongolian Plateau; kara-khitans founds on the Orkhon Valley only
- great-jin 1231 loss cp mongol-empire -> mongol-empire 1230 contest_start: **missing**. Shaanxi; route to ia-02
- western-xia 1032 gain cp xiliangfu -> xiliangfu 1016 dissolve: **mismatch**. xiliangfu ends 1016 (dissolve cp ganzhou-kingdom); 16 years apart; pages disagree (flagged by author)
- xiliangfu 1003 occupation_start cp western-xia -> western-xia - -: **missing**. also 1004 end, 1015 start, 1016 end
- western-xia 1136 gain cp great-jin -> great-jin - -: **missing**. Jin cession of Xining; the Jin never gains it
- khitan-confederation 755 vassal (absent) cp uyghur-khaganate -> uyghur-khaganate - -: **missing**. uyghur-khaganate should carry vassal_start 755 / vassal_end 840 cp khitan-confederation (ia group)
- eastern-liao 1220 vassal (absent) cp mongol-empire -> mongol-empire - -: **missing**. mongol-empire should carry the vassal pairs of eastern-liao and eastern-xia (ia-02)

## Problems

- No page failed for the reviewer; WebFetch's summariser was used for quotes, so a few 'confirmed' quotes are the summariser's excerpt of the sentence.
- Vassal mirrors were judged by the schema rule (vassal events only in the suzerain's dossier, counterpart = the vassal); reviewer-brief check 3's wording (a vassal_start in both ledgers) conflicts with it. later-jin.json (ea-04) uses the inverted convention.
- Keyframe area steps were measured with history/tools/gazetteer.py resolve on H3 cells (about 253 km2 each); cell areas overstate true km2 by roughly a fifth at these latitudes, so the km2 quoted in findings are approximate.
- Most fail findings form one chain: the Song-Jin-Qi transfer of 1130 (northern-song, great-jin) and the Hunan/Fujian unification shapes (northern-song with ea-04's southern-tang, wuyue, qingyuan-circuit); the authors should fix them together with one shared region spec.
- Reviewer edit: history/polities/eastern-liao.json identity.rulers and identity.capitals (re-validated, read back).
