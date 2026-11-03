# Review of batch ea-06-x (Yuan additions: Red Turban states, Tibet and Yunnan regimes)

Reviewed 2026-10-24 by the adversarial reviewer. All twelve dossiers validated with --resolve (0 errors, 0 warnings) before and after the reviewer's edits. The machine copy of this review is history/notes/phase-b/reviews/ea-06-x.json.

Method: each ledger was read event by event, and 4-8 events per dossier were checked on the cited Wikipedia pages (WebFetch). Every keyframe was resolved with the gazetteer and the batch's shapes were intersected year by year to find double-held land. Mirrors were checked against tibet, mongol-empire, kingdom-of-dali and northern-yuan, the dossiers that exist; yuan-dynasty (ea-06-a) and ming-dynasty (Ming group) are not written yet. No page opened gives an area for any of these states, so the area checks record the drawn size only.

## Verdicts

| slug | verdict | blocking |
| --- | --- | --- |
| zhu-yuanzhang-s-wu | fail | /keyframe_review/0/correction (the Nanjing 100 km circle, repeated in keyframes 1-6, /ledger/0, /ledger/20 and identity.successors) |
| han-song | thin | - |
| tianwan | fix | - |
| chen-han | fix | - |
| ming-xia | fix | - |
| zhang-shicheng-s-wu | fail | /keyframe_review/0/correction, /keyframe_review/1/correction, /keyframe_review/2/correction, /ledger/0, /ledger/1 (the Yangzhou 100 km circle) |
| fang-guozhen-s-regime | pass | - |
| sakya-regime | pass | - |
| ispah-rebellion | pass | - |
| principality-of-liang-yunnan | pass | - |
| mangyul-gungthang | thin | - |
| duan-governors-of-dali | fix | - |

Verdict key: 'fix' means the reviewer made the change on the mount and re-validated. 'fail' means the dossier goes back to the author for a shape change the reviewer may not make. 'thin' means honest but under-explained within the page budget.

## zhu-yuanzhang-s-wu: fail

- [BLOCKING] `/keyframe_review/0/correction (the Nanjing 100 km circle, repeated in keyframes 1-6, /ledger/0, /ledger/20 and identity.successors)`: The Nanjing circle reaches across the Yangtze to Yangzhou and Yizheng, about 69 km from Nanjing. It overlaps the zhang-shicheng-s-wu Yangzhou circle by 89 H3 cells (about 22,000 km2) every year from 1356 to 1362 and by 100 cells from 1363 to 1365. No contest event covers that land before 1364.
  - Why: A gazetteer resolve of both dossiers' keyframes, year by year. Zhu's own text says 'Jiqing/Yingtian (Nanjing) and its district'. Zhang's text says 'Gaoyou, Taizhou, Xinghua and Yangzhou north of the Yangtze'. No page opened gives Yangzhou to Zhu before 1366.
  - Fix: Make the two shapes disjoint, together with the zhang-shicheng-s-wu fix. For example, Zhu keeps the Nanjing circle south of the river plus Chuzhou and Hezhou, and Zhang's circle becomes {"minus": [{"place": "Yangzhou", "km": 100}, {"place": "Nanjing", "km": 100}]}. Write the change everywhere the circle appears.
- [open] `/ledger (between /ledger/4 and /ledger/5)`: Two chen-han events have no mirror here: chen-han /ledger/4 (1361, loss of Jiujiang to Zhu, confidence 2) and /ledger/5 (August 1361, the Han retake Jiujiang and Anqing, confidence 3).
  - Why: Chen Han page: 'The Han government took advantage of the situation and launched a counter-offensive, successfully retaking Jiujiang and Anqing in August 1361.'
  - Fix: Add a gain in 1361 (no month, confidence 2, Jiujiang 60 km, counterpart chen-han) and a loss in 1361/8 (confidence 3, Jiujiang 60 km plus Anqing 80 km, counterpart chen-han), both sourced to the Chen Han page.
- [open] `/ledger (1363 and 1367)`: Two han-song events have no mirror here: han-song /ledger/13 (gain of a 40 km Chuzhou circle from Zhu in June 1363) and /ledger/15 (dissolve in January 1367, successor zhu-yuanzhang-s-wu). Zhu's shape also keeps that circle, so both states hold it from 1363 to 1367 (24 cells).
  - Why: Han Lin'er page: 'Han and his court were then relocated to Chuzhou' (June 1363) and 'Han resided there until January 1367'.
  - Fix: Either add a loss in 1363/6 (Chuzhou 40 km, counterpart han-song, confidence 1) and a gain back in 1367/1, or have han-song drop its 1363 gain and keep Chuzhou only as its capital. Agree the choice with the han-song dossier.
- [open] `/keyframe_review/4/correction`: Keyframe zhu-yuanzhang-s-wu_1364 holds all of Huguang from 1364, but the ledger takes only Wuchang in 1364/3 (/ledger/9) and gains Huguang in 1365/4 (/ledger/11).
  - Why: Chen Han page: 'the occupation of Hubei, Hunan, and Jiangxi dragged on until April 1365'.
  - Fix: Either make the 1364 keyframe the Wuhan circle and start Huguang in a 1365 keyframe, or move the Huguang gain to 1364/3 at confidence 2.
- [thin] `/ledger/2`: The 1356-1357 conquests are bridged at confidence 1: Zhenjiang, Changzhou, Ningguo, Huizhou, Chizhou and Yangzhou. The Hongwu page gives only the holding at the start of 1360. (try https://en.wikipedia.org/wiki/Xu_Da)
- [thin] `/ledger/12`: The 1366 cities north of the Yangtze and in Huzhou are at confidence 1. (try https://en.wikipedia.org/wiki/Xu_Da)
- Spot checks: `/ledger/0` confirmed: 'In April 1356, Zhu successfully entered Jiqing, which he renamed Yingtian'; `/ledger/1` confirmed: 'In Zhejiang, from 1358 to 1359, Zhu controlled four impoverished inland prefectures' (confidence 2 is right); `/ledger/3` confirmed: 'In 1361, Han appointed Zhu as Duke of Wu'; `/ledger/8` confirmed: 'proclaimed himself King of Wu (Wu wang) on 4 February 1364'; `/ledger/5` confirmed: September 1361, Zhu's forces 'defeated the Han's fleet before Jiujiang, captured the city'; `/ledger/14` confirmed: Zhu 'captured Hangzhou in December 1366'; `/ledger/15` confirmed: 'In October 1367, the city was captured, and all of Wu was pacified' (the Zhang Shicheng page gives 1 October 1367); `/ledger/20` confirmed: 'On 23 January 1368, Zhu proclaimed himself emperor and renamed his state'
- Area: No Cliopatria row and no infobox area on any page opened (checked); the author says so in notes. The largest drawn shape is about 896,000 km2.

## han-song: thin

- [open] `/ledger/11 and /ledger/13`: Two of this dossier's events have no mirror in the other dossier. The loss of Anfeng to zhang-shicheng-s-wu (February 1363) has no gain in Zhang's ledger. The gain of Chuzhou from zhu-yuanzhang-s-wu (June 1363) has no loss in Zhu's ledger.
  - Why: Liu Futong page: 'Zhang Shicheng's general Lü Zhen captured Anfeng and killed Liu Futong in February 1363'. Han Lin'er page: 'Han and his court were then relocated to Chuzhou'.
  - Fix: No change is needed here; the mirrors go into zhang-shicheng-s-wu and zhu-yuanzhang-s-wu (see their fixes). If the Zhu dossier drops Chuzhou as a cession, drop /ledger/13 and keep keyframe han-song_1363 only as the capital.
- [thin] `/ledger/2`: The year of the Shandong province (Mao Gui) is at confidence 1. The Han Lin'er page has only 'five provinces between 1356 and 1359' and Mao's death in 1359. (try https://en.wikipedia.org/wiki/Mao_Gui)
- [thin] `/ledger/10`: The loss of Shandong in 1362 is at confidence 1. (try https://en.wikipedia.org/wiki/Chaghan_Temur)
- [thin] `/ledger/13`: The Chuzhou seat in 1363 is drawn as Song land at confidence 1; the page gives only a relocation. (try https://en.wikipedia.org/wiki/Han_Lin%27er)
- Spot checks: `/ledger/0` confirmed: 'proclaimed emperor of a restored Song dynasty in Bozhou (in western Anhui) on 16 March 1355'; `/ledger/1` confirmed: 'In May 1356, Han Lin'er appointed Zhu as the head of Jiangnan Province'; `/ledger/3` confirmed: 'captured Kaifeng ... in June 1358'; `/ledger/7` confirmed: 'Chaghan Temur recaptured Kaifeng in September 1359' (the Red Turban page gives 10 September 1359); `/ledger/11` confirmed: Anfeng taken and Liu killed in February 1363; `/ledger/12` confirmed: 'In June 1363 ... Han and his court were then relocated to Chuzhou'; `/ledger/15` confirmed: 'until January 1367, when he drowned in the Yangtze River'
- Area: No Cliopatria row and no infobox area on any page opened (checked); the author says so in notes. The largest drawn shape is about 307,000 km2.

## tianwan: fix

- [APPLIED] `/ledger/7 and /keyframe_review/4`: Jiangxi was gained in 1356 at confidence 2. The Tianwan page gives no year for it, and the Chen Han page dates Chen Youliang's rule in Jiangxi from 1357.
  - Why: Tianwan page: 'Tianwan's power now extended to all of Huguang, Jiangxi, and later parts of Shaanxi' (undated). Chen Han page: 'founded in Jiangxi in 1360 by Chen Youliang, who had been ruling there since 1357'.
  - Fix: Done. /ledger/7 is now the 1356 gain of Huguang only. A new /ledger/8 is the 1357 gain of Jiangxi (confidence 2, Chen Han page). Keyframe tianwan_1356 now runs 1356-1356 with Huguang, and a new keyframe tianwan_1357 runs 1357-1360 with Huguang and Jiangxi.
- [APPLIED] `/ledger/9, /ledger/10, /identity/successors/1/land`: The Sichuan vassal region used the gazetteer's Sichuan (region). That region reaches 97.4 E and includes 1,021 cells (about 258,000 km2) of Kham.
  - Why: Tibet under Yuan rule page: 'Tuosima (Amdo) and Tuogansi (Kham) were organized into Routes/Circuits'. Kham was a Yuan Tibetan route, not part of Sichuan. The sakya-regime dossier by the same author also keeps Kham apart.
  - Fix: Done. Every Sichuan (region) is now {"minus": [{"region": "Sichuan (region)"}, {"region": "Kham"}]}, the same change as in ming-xia.
- [thin] `/ledger/4`: The 1353 loss of the Wuhan, Jiujiang, Nanchang and Changsha cities is at confidence 1. (try https://en.wikipedia.org/wiki/Toqto%27a_(Yuan_dynasty))
- Spot checks: `/ledger/0` confirmed: 'In September, Zou captured the city of Qishui in southern Hubei and enthroned Xu Shouhui as emperor'; `/ledger/1` confirmed: 'In the early spring of 1352, he seized Hanyang'; `/ledger/3` confirmed: summer 1353 campaign; 'By fall, Toqto'a's forces had captured the Tianwan capital of Qishui'; `/ledger/7` mis-dated: Jiangxi is undated on the page and dated 1357 on the Chen Han page; fixed; `/ledger/11` confirmed: 'In June of that year, he launched an attack on Hanyang and killed Xu' (1360)
- Area: No Cliopatria row and no infobox area on any page opened (checked); the author says so in notes. Drawn maximum after the fix: Huguang plus Jiangxi. The largest drawn shape is about 625,000 km2.

## chen-han: fix

- [APPLIED] `/ledger/1 (now /ledger/7)`: The ledger moved the capital to Wuchang in 1360 at confidence 2, but identity.capitals and the Chen Han page put Jiujiang as capital until Zhu took it in September 1361.
  - Why: Chen Han page: 'Zhu Yuanzhang successfully captured Jiujiang and blocked the remaining forces of Chen Youliang in Wuchang'. The September 1361 fleet 'captured the city'. The Red Turban page gives the move to Wuchang without a year.
  - Fix: Done. The capital_move is now dated 1361/9, sourced to the Chen Han page, and placed after the 1361/9 loss of Jiujiang.
- [open] `/ledger/4 and /ledger/5`: These two events have no mirror in zhu-yuanzhang-s-wu.
  - Why: See the zhu-yuanzhang-s-wu fixes.
  - Fix: Nothing to change here.
- Spot checks: `/ledger/0` confirmed: 'In early 1360, Chen declared himself King of Han ... with his capital at Jiujiang'; `/ledger/1` confirmed: 'declared himself emperor of the Great Han in June 1360 and occupied most of the Tianwan territories'; `/ledger/5` confirmed: 'successfully retaking Jiujiang and Anqing in August 1361' (the Han government is the subject); `/ledger/6` confirmed: September 1361, Zhu 'captured the city'; `/ledger/8` confirmed: early 1362 Hu Mei surrendered Nanchang; 'This surrender solidified Zhu's control over Jiangxi'; `/ledger/10` confirmed: 'approached Wuchang in March 1364, the helpless emperor surrendered'
- Area: No Cliopatria row and no infobox area on any page opened (checked); the author says so in notes. The largest drawn shape is about 625,000 km2.

## ming-xia: fix

- [APPLIED] `/keyframe_review/0/correction, /ledger/0, /ledger/4, /ledger/5, /identity/predecessors/0/land, /identity/successors/0/land`: The gazetteer's Sichuan (region) reaches 97.4 E and includes 1,021 cells (about 258,000 km2, 44 percent of the shape) of the Kham highlands. The Yuan administered Kham as a Tibetan route, not as Sichuan.
  - Why: Tibet under Yuan rule page: 'Tuosima (Amdo) and Tuogansi (Kham) were organized into Routes/Circuits'. A gazetteer intersect of Sichuan (region) with Kham gives 1,021 cells. The sakya-regime dossier by the same author also leaves Kham to the Yuan.
  - Fix: Done. Every Sichuan (region) is now {"minus": [{"region": "Sichuan (region)"}, {"region": "Kham"}]}. The shape falls from 2,328 to 1,307 cells, and the notes record the change.
- Spot checks: `/ledger/0` confirmed: 'In 1360, Ming Yuzhen declared himself King of Longshu and ruled independently'; `/ledger/1` confirmed: 'in 1362, he became emperor of the Great Xia with its capital in' Chongqing; `/ledger/3` confirmed: 'By August, they had reached Chongqing, and ... Ming Sheng and his mother surrendered'; `/ledger/5` confirmed: 'In September, the defenders of Chengdu also surrendered'
- Area: No Cliopatria row and no infobox area on any page opened (checked); the author says so in notes. Drawn shape after the Kham trim; it was 589,000 km2 before. The largest drawn shape is about 330,000 km2.

## zhang-shicheng-s-wu: fail

- [BLOCKING] `/keyframe_review/0/correction, /keyframe_review/1/correction, /keyframe_review/2/correction, /ledger/0, /ledger/1 (the Yangzhou 100 km circle)`: The Yangzhou circle crosses the Yangtze to Zhenjiang and reaches west to Chuzhou. It overlaps zhu-yuanzhang-s-wu by 89 to 100 cells (about 22,000-25,000 km2) every year from 1356 to 1365, and the han-song Chuzhou seat by 9 cells from 1363 to 1365. This contradicts the dossier's own text 'north of the Yangtze'.
  - Why: A gazetteer resolve of both dossiers' keyframes, year by year. Yangzhou is about 69 km from Nanjing, and both circles are 100 km. Zhu held Zhenjiang and Chuzhou (Hongwu Emperor page: 'southwestern part of Jiangsu' at the start of 1360).
  - Fix: Make the circle disjoint from Zhu's shape, for example {"minus": [{"place": "Yangzhou", "km": 100}, {"place": "Nanjing", "km": 100}]}, or use circles round Gaoyou, Taizhou and Xinghua. Coordinate with the zhu-yuanzhang-s-wu fix.
- [open] `/ledger (1363)`: The ledger has no gain of Anfeng, so han-song /ledger/11 (loss of Anfeng to this state, February 1363) has no mirror.
  - Why: Liu Futong page: 'Zhang Shicheng's general Lü Zhen captured Anfeng and killed Liu Futong in February 1363'. Han Lin'er page: Han 'was saved by the arrival of Zhu Yuanzhang's army'.
  - Fix: Add a gain in 1363/2 (confidence 3, {"lon": 116.78, "lat": 32.58, "km": 60}, counterpart han-song, Liu Futong page) and a loss to zhu-yuanzhang-s-wu later in 1363 (confidence 2), or say in a note who held Anfeng afterwards.
- [thin] `/keyframe_review/1`: The ledger has no loss to Zhu in 1356-1357, so the 1356-1362 shape keeps Changzhou to 1362. Zhang Shicheng page: 'after several defeats from troops loyal to Zhu in 1356–57'. (try https://en.wikipedia.org/wiki/Xu_Da)
- [thin] `/ledger/7`: Northern Jiangsu in 1363 is at confidence 1. The Zhou page: 'instead occupied northern Jiangsu' (undated). (try https://en.wikipedia.org/wiki/Zhou_(Zhang_Shicheng))
- [thin] `/ledger/11`: The 1366 losses north of the Yangtze and at Huzhou are at confidence 1. (try https://en.wikipedia.org/wiki/Xu_Da)
- Spot checks: `/ledger/0` confirmed: 'In 1354, Zhang declared the establishment of the state of Zhou'; `/ledger/3` confirmed: 'captured the first major city, Changshu, in February 1356'; `/ledger/4` confirmed: 'followed by Suzhou ... in March'; `/ledger/6` confirmed: 'abdicated his royal title in late 1357 and submitted to the Yuan government'; `/ledger/8` confirmed: 'In 1363, Zhang took control of Hangzhou and declared himself Prince of Wu'; `/ledger/9` confirmed: 'declared himself King of Wu (吳王) in October 1363'; `/ledger/12` confirmed: 'his taking Gaoyou ... on April 24, 1366'; `/ledger/15` confirmed: 'on October 1, 1367, when Suzhou fell to Zhu Yuanzhang's troops'
- Area: No Cliopatria row and no infobox area on any page opened (checked); the author says so in notes. The largest drawn shape is about 118,000 km2.

## fang-guozhen-s-regime: pass

- [open] `/keyframe_review/1/correction (the Shaoxing 50 km circle)`: The Shaoxing circle overlaps Zhu's inland-Zhejiang circle by 12 cells (1358-1366) and Zhang's Hangzhou circle by 17 cells (1363-1365). The overlap is small and is explained by the page.
  - Why: Fang Guozhen page: 'his de facto control over Ningbo and Shaoxing'.
  - Fix: None required. A gap-filler may trim the Shaoxing circle when the Zhu and Zhang shapes are redrawn.
- [thin] `/ledger/1`: The years Fang took Qingyuan, Taizhou and Wenzhou are unknown; the page says only 'By 1356' (confidence 1). (try https://en.wikipedia.org/wiki/Fang_Guozhen)
- Spot checks: `/ledger/0` confirmed: 'created a pirate band in 1348 that operated off offshore islands'; the land circle is a reading at confidence 2; `/ledger/1` confirmed: 'By 1356, Fang permanently controlled three coastal prefectures in Zhejiang'; `/ledger/3` confirmed: Taizhou captured in October 1367; `/ledger/4` confirmed: Wenzhou in November; `/ledger/7` confirmed: 'drove Fang out of Ningbo, securing his surrender in December'
- Area: No Cliopatria row and no infobox area on any page opened (checked); the author says so in notes. The largest drawn shape is about 42,000 km2.

## sakya-regime: pass

- Spot checks: `/ledger/0` confirmed: 'In 1264, the feudal reign over Tibet was given to Drogön Chögyal Phagpa by Kublai Khan'; `/ledger/2` confirmed: 'a revolt of the Drikung Kagyu sect ... in 1285'; `/ledger/3` confirmed: 'The revolt was suppressed in 1290'; `/ledger/4` confirmed: 'superseded Sakya in the period 1354–1358'; `/ledger/7` confirmed: 'The succession of Sakya lamas in Tibet came to an end in 1358'
- Area: No Cliopatria row and no infobox area on any page opened (checked); the author says so in notes. The infobox has Capital: Sakya Monastery (1268–1354) and no area; the dossier dates the capital 1264-1358, which is a minor reading. The largest drawn shape is about 834,000 km2.

## ispah-rebellion: pass

- [open] `/ledger/0 and /ledger/1`: The undated Putian gain and the contest_start sort before the found event of 1357/3, so the ledger takes land before the state exists. This is cosmetic.
  - Why: The validator sorts events without a month first. Ispah page: 'The rebel army seized control of Quanzhou, Putian, and even reached the provincial capital Fuzhou' (undated, after March 1357).
  - Fix: Optional: fold Putian into the found region at confidence 2, or leave it for the renderer to treat the found as the first event.
- [thin] `/ledger/0`: The dates of Putian and of the approach to Fuzhou are at confidence 1. (try https://en.wikipedia.org/wiki/Chen_Youding)
- Spot checks: `/ledger/2` confirmed: 'In March 1357, Sayf ad-Din and Amir ad-Din ... control Quanzhou'; `/ledger/3` confirmed: 'In 1362, the Ispah army collapsed into internal conflict'; Yawuna became leader; `/ledger/5` confirmed: 'In 1366, it was eventually crushed by ... Chen Youding'; `/ledger/0` confirmed undated; confidence 1 is honest
- Area: No Cliopatria row and no infobox area on any page opened (checked); the author says so in notes. The largest drawn shape is about 10,600 km2.

## principality-of-liang-yunnan: pass

- Spot checks: `/ledger/0` confirmed: 'Before the Yuan dynasty's fall in 1368, Basalawarmi had been the Yuan Viceroy of Yunnan'; from Kunming he 'led one of the last pockets of Yuan resistance'; `/ledger/1` confirmed: 1381, 'Some 250,000 to 300,000 Han and Hui Muslim troops were mobilized'; `/ledger/2` confirmed: 'committed suicide himself on January 6, 1382'; `/ledger/3` confirmed: 'The Prince of Liang, Basalawarmi, committed suicide on January 6, 1382'
- Area: No Cliopatria row and no infobox area on any page opened (checked); the author says so in notes. The largest drawn shape is about 321,000 km2.

## mangyul-gungthang: thin

- [thin] `/keyframe_review/0`: One 90 km circle stands for 354 years. Overlords and extent between 1358 and 1612 (Phagmodrupa, Rinpungpa) are unrecorded; the page says only 'subject to a variety of Central Asian overlords down to 1620'. This is thin by design under the page budget. (try https://en.wikipedia.org/wiki/Rinpungpa)
- Spot checks: `/ledger/0` confirmed: 'established under Sakya overlordship in Southwest Tibet around 1265'; `/ledger/1` confirmed: 'In 1612–13 he led an expedition to Ngari (West Tibet), where Mangyül Gungthang was subjugated'; `/ledger/2` confirmed: 'the Mangyül Gungthang kingdom was definitely incorporated in 1619'; `/ledger/3` confirmed with a variant: the kingdom page says 'destroyed by the King of Tsang' in 1620, and the author notes the 1619/1620 disagreement
- Area: No Cliopatria row and no infobox area on any page opened (checked); the author says so in notes. The largest drawn shape is about 14,900 km2.

## duan-governors-of-dali: fix

- [APPLIED] `/ledger/1`: The 1274 rename was at confidence 3. The page dates Ajall's appointment and the tusi system to 1274 but does not say the Duan title changed that year.
  - Why: Dali Kingdom page: 'In 1274, Ajall Shams al-Din Omar was assigned by Kublai to stabilize Yunnan' and 'He instituted a native chieftain system that came to be known as tusi'. The Duan title appears only as 'Governor-General of Dali', undated.
  - Fix: Done. Confidence lowered to 2, with an explanatory sentence added to the note.
- Spot checks: `/ledger/0` confirmed: 'In 1256, Duan Xingzhi surrendered' and 'was enfeoffed as Maharaja'; `/ledger/1` over-confident: the 1274 date belongs to Ajall and the tusi system, not to a Duan title change; lowered to 2; `/ledger/3` confirmed: 'In 1382 Lan Yu and Mu Ying's forces attacked and crushed Duan's realm'; `/ledger/5` confirmed: 'The last Dali stronghold of Dengchuan fell to the Ming in February 1383'
- Area: No Cliopatria row and no infobox area on any page opened (checked); the author says so in notes. The largest drawn shape is about 42,700 km2.

## Cross-dossier matrix

- zhu-yuanzhang-s-wu 1361 gain -> chen-han: **matched** (mirror: chen-han 1361 loss). Jiujiang, September 1361, on both sides.
- zhu-yuanzhang-s-wu 1362 gain -> chen-han: **matched** (mirror: chen-han 1362 loss). Jiangxi, early 1362.
- zhu-yuanzhang-s-wu 1364 gain -> chen-han: **matched** (mirror: chen-han 1364 dissolve). Wuchang, March 1364.
- zhu-yuanzhang-s-wu 1365 gain -> chen-han: **matched** (mirror: chen-han 1364 dissolve). Huguang: the Chen Han dissolve is 1364/3 and Zhu's gain 1365/4, 13 months apart. Zhu's keyframe 1364 already holds Huguang (see the zhu fix).
- chen-han 1361 loss -> zhu-yuanzhang-s-wu: **missing** (mirror: zhu-yuanzhang-s-wu None None). Zhu has no gain of Jiujiang before August 1361.
- chen-han 1361 gain -> zhu-yuanzhang-s-wu: **missing** (mirror: zhu-yuanzhang-s-wu None None). August 1361, the Han retake Jiujiang and Anqing; Zhu has no matching loss.
- zhu-yuanzhang-s-wu 1366 gain -> zhang-shicheng-s-wu: **matched** (mirror: zhang-shicheng-s-wu 1366 loss). Northern Jiangsu and Huzhou (confidence 1 on both sides), Gaoyou 1366/4 and Hangzhou 1366/12.
- zhu-yuanzhang-s-wu 1367 gain -> zhang-shicheng-s-wu: **matched** (mirror: zhang-shicheng-s-wu 1367 dissolve). Suzhou, October 1367.
- zhu-yuanzhang-s-wu 1367 gain -> fang-guozhen-s-regime: **matched** (mirror: fang-guozhen-s-regime 1367 loss). Zhu records one gain in December; Fang records losses in October (Taizhou), November (Wenzhou) and December (Ningbo, Shaoxing). Same year.
- zhu-yuanzhang-s-wu 1356 found -> yuan-dynasty: **mismatch** (mirror: zhang-shicheng-s-wu None None). The two shapes overlap: the Nanjing and Yangzhou circles share 89-100 cells from 1356 to 1365 with no event. Blocking for both dossiers.
- han-song 1356 vassal_start -> zhu-yuanzhang-s-wu: **exception** (mirror: zhu-yuanzhang-s-wu None None). By the schema, the suzerain records the vassalage (the counterpart is the vassal). Zhu's dossier does not contradict it.
- han-song 1363 loss -> zhang-shicheng-s-wu: **missing** (mirror: zhang-shicheng-s-wu None None). Anfeng, February 1363 (Liu Futong page); Zhang has no gain.
- han-song 1363 gain -> zhu-yuanzhang-s-wu: **missing** (mirror: zhu-yuanzhang-s-wu None None). The Chuzhou seat (40 km) stays in Zhu's shape too, so 24 cells are double-held from 1363 to 1367.
- han-song 1367 dissolve -> zhu-yuanzhang-s-wu: **missing** (mirror: zhu-yuanzhang-s-wu None None). Zhu records no gain of Chuzhou in January 1367 (the land never left Zhu's shape).
- tianwan 1357 vassal_start -> ming-xia: **exception** (mirror: ming-xia 1360 found). The suzerain records the vassalage. Ming Xia is founded in 1360 with tianwan as counterpart; its 1357-1360 years exist only as Tianwan's vassal tint.
- tianwan 1360 dissolve -> chen-han: **matched** (mirror: chen-han 1360 gain). June 1360.
- ming-xia 1360 found -> tianwan: **matched** (mirror: tianwan 1360 vassal_end). 1360.
- chen-han 1360 found -> tianwan: **matched** (mirror: tianwan 1360 dissolve). Early 1360 at Jiujiang, while Tianwan lives to 1360/6. Tianwan records no split. Minor.
- sakya-regime 1264 found -> mongol-empire: **mismatch** (mirror: mongol-empire 1250 gain). mongol-empire gains Tibet from tibetans in 1250 as direct land and has no vassal_start for sakya-regime, so both draw Ü-Tsang as their own from 1264 to 1293. Route to the mongol-empire owner: add vassal_start sakya-regime 1264. The yuan-dynasty owner (ea-06-a, not written) must do the same for 1294-1358.
- sakya-regime 1354 contest_start -> tibet: **mismatch** (mirror: tibet 1354 found). tibet /ledger/0 founds Tibet in 1354 on the whole Sakya shape (3,298 cells), with counterpart yuan-dynasty. It should found on the Phagmodrupa core (Nedong), contest with sakya-regime from 1354 to 1358, and take the rest in 1358. Route to ea-06-b.
- sakya-regime 1358 loss -> tibet: **mismatch** (mirror: tibet 1358 gain). The year matches, but tibet /ledger/1 names yuan-dynasty, not sakya-regime. Route to ea-06-b.
- sakya-regime 1265 vassal_start -> mangyul-gungthang: **matched** (mirror: mangyul-gungthang 1265 found). c. 1265; the suzerain records the vassalage.
- mangyul-gungthang 1619 dissolve -> tibet: **mismatch** (mirror: tibet 1619 gain). The year and the 59 cells match exactly, but tibet /ledger/6 gives the counterpart as the string 'Mangyül Gungthang'. It should be the slug mangyul-gungthang (ea-06-b).
- mangyul-gungthang 1612 contest_start -> tibet: **mismatch** (mirror: tibet 1612 gain). tibet /ledger/5 gains other West Tibetan regimes in 1612 (0 cells shared with Gungthang) and records no contest with mangyul-gungthang. Minor (ea-06-b).
- duan-governors-of-dali 1256 found -> mongol-empire: **mismatch** (mirror: mongol-empire 1260 gain). mongol-empire records vassal_end and a gain of kingdom-of-dali in 1260 as direct land, so the Duan circle is double-held 1260-1293. kingdom-of-dali /identity/successors names only mongol-empire. Route to their owners: add duan-governors-of-dali as a vassal from 1256 and as a successor of kingdom-of-dali.
- principality-of-liang-yunnan 1368 found -> yuan-dynasty: **exception** (mirror: northern-yuan 1368 found). yuan-dynasty is not written (ea-06-a). Its Cliopatria shape yuan-dynasty_1363 (to 1374) covers Yunnan, and ea-06-a must carve Liang out from 1368. northern-yuan has no vassal_start for Liang (Ayushiridara's confirmation is undated).
- principality-of-liang-yunnan 1382 dissolve -> ming-dynasty: **exception** (mirror: ming-dynasty None None). The Ming group has not run. Cliopatria's ming-dynasty_1375 shape reaches lat 18.2 and probably covers Yunnan before 1382; the Ming dossier must start Yunnan in 1382.
- ming-xia 1371 loss -> ming-dynasty: **exception** (mirror: ming-dynasty None None). The Ming group has not run. Cliopatria's Ming row starts in 1375.
- duan-governors-of-dali 1382 loss -> ming-dynasty: **exception** (mirror: ming-dynasty None None). The Ming group has not run.
- zhu-yuanzhang-s-wu 1368 dissolve -> ming-dynasty: **exception** (mirror: ming-dynasty None None). The Ming group has not run. The Ming dossier should absorb zhu-yuanzhang-s-wu as its first phase (author's note).
- han-song 1358 gain -> yuan-dynasty: **exception** (mirror: yuan-dynasty None None). yuan-dynasty is not written (ea-06-a has not produced it). This covers every yuan-dynasty counterpart in the batch: the founding and gains of tianwan, han-song, zhang-shicheng-s-wu, fang-guozhen-s-regime, ispah-rebellion and zhu-yuanzhang-s-wu, 1348-1366, and Zhang's (1357-1363) and Fang's (from 1356) vassalage, which the suzerain must record.

## For other owners

- Cross-batch mismatches for other owners: tibet (ea-06-b) names yuan-dynasty instead of sakya-regime in 1354/1358 and founds on the whole Sakya shape in 1354, and its 1619 counterpart is a name, not the slug mangyul-gungthang. mongol-empire has no vassal relation for sakya-regime or duan-governors-of-dali and draws both as direct land. kingdom-of-dali's successors omit duan-governors-of-dali.

