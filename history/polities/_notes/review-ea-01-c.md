# Review of batch ea-01-c (song, teng, wey, wu, xu, yan)

Written 2026-10-18 by the Phase B adversarial reviewer. Inputs: the author's report and notes (ea-01-c), the six dossiers, the neighbour dossiers that exist (lu, qi, jin, chu, cao, chen, xiongnu; also qin, zhou-dynasty for counterparts). Zheng, zhu, wei, zhao, yue, zhongshan, han, dai, jibei, chang-shan, liaodong and zhai are not written yet: events with them are exceptions ('a counterpart owned by a group that has not run yet').

Mechanical: `validate_dossier.py --resolve` passes all six (0 errors); warnings are the intentional empty Xu corrections (3) and the 'xing' counterpart (1). No infobox of the six pages gives an area (checked on each page).

## Verdicts

- **yan**: fail
- **song**: thin
- **wey**: thin
- **wu**: thin
- **xu**: thin
- **teng**: fix

## yan (fail)

Findings:
- `/keyframe_review/2, /keyframe_review/3, /keyframe_review/5, /ledger/3` [BLOCKING]: Cliopatria's yan_-404, yan_-291 and yan_-208 shapes leave out Ji (116.37E, 39.89N), the capital the dossier itself holds -650..-227 and -208..-202, and Xiadu (c. 115.5E), yet yan_-404 and yan_-208 are passed 'ok' and yan_-291 is corrected only for 226-222; /ledger/3 hands this western block (60 cells, about 10,400 km2) to Zhao in 404. Evidence: shapes.csv bbox: yan_-750 starts at 115.8648E (Ji inside), but yan_-404, yan_-291 and yan_-208 all start at 116.7002E, west of which lie Ji and Xiadu. Yan page: 'Yan absorbed the State of Ji ... and moved its capital to Ji'; /ledger/10 quotes Qin's wars page: Qin 'conquered the Yan capital Ji' in 226, so Yan held Ji until 226. /ledger/3 has Cliopatria give the block to Zhao in 404 (zhao_-404 bbox reaches 117.12E, 40.10N); afterwards the bboxes of zhongshan_-366/-301 (to 40.10N) and wei_-291 (to 40.42N) also cover Beijing. The KF1 note checks the capital only against the 750 shape. Fix: Mark yan_-404 adjust with correction union({cliopatria: Yan, year: -404}, minus({cliopatria: Yan, year: -405}, {cliopatria: Yan, year: -404})) (that is, the 750 shape), yan_-291 adjust with the same western cells added (keep the 226-222 note), yan_-208 adjust with the same; delete /ledger/3 or cut it to cells the pages let Zhao hold (none named: then delete); add the restored cells to the regions of /ledger/10 (Qin 226) and /ledger/13 (208); say in notes that Cliopatria's Zhao, Zhongshan and Wei rows over Beijing are wrong (for those groups).
- `/keyframe_review/2 vs /ledger/6, /ledger/7` [not blocking]: The c. 300 gains of Liaodong and the Donghu land (about 66,000 km2: 105,154 minus 39,183) have no keyframe until yan_-291, while yan_-404 is passed 'ok' through -292. Evidence: Qin Kai page: 'around 300 BC, he defeated the Donghu and conquered Liaodong Peninsula'; shapes.csv yan_-404 runs -404..-292 at 39,183 km2, yan_-291 starts -291 at 105,154 km2. Rule 4: a large event inside one shape's span needs the keyframe marked adjust. Fix: Add a new keyframe yan_-300 (from -300, to -292) with the yan_-291 shape (plus the Ji fix), and say in yan_-404's note that it ends at -301; or date /ledger/6-7 to -291 with the 'around 300' quote in the note.
- `/ledger/1 vs /keyframe_review/0, /keyframe_review/1` [not blocking]: The -650 gain of the State of Ji (place Beijing) adds land the keyframes already give Yan from -1046: yan_-1046 carries the 750 shape back, and it contains Beijing. Evidence: shapes.csv yan_-750 bbox 115.86-121.23E, 38.55-40.94N contains Beijing; Yan page: Yan 'absorbed the State of Ji, a smaller kingdom to the north'. Fix: Either cut a Ji (Beijing) circle out of yan_-1046 and the first years of yan_-750 until -651 (a new keyframe split at -650), or say in /ledger/1's note that the Ji gain is an event only and the shapes include Ji from the start.

For a gap-filler:
- `/ledger/3`: Any page for a Yan loss to Zhao in 404 (and which cells); expected none, so the event should go (see fixes). Try: https://en.wikipedia.org/wiki/Zhao_(state)
- `/ledger/5`: The year Qi's troops were driven out after 314 (312 is taken from the reign list). Try: https://en.wikipedia.org/wiki/King_Zhao_of_Yan
- `/ledger/7`: The extent of the land taken from the Donghu c. 300 and the Yan walls and five commanderies (the Yan page names Shanggu, Yuyang, Youbeiping, Liaoxi and Liaodong, undated: 'At the turn of the 3rd century BC'). Try: https://en.wikipedia.org/wiki/Donghu_people
- `/ledger/13`: Han Guang's year (209 or 208) and extent. Try: https://en.wikipedia.org/wiki/Han_Guang
- `/ledger/14`: Any page for the 5 cells Cliopatria passes to the Xiongnu at 208 (xiongnu.json has no gain from Yan). Try: https://en.wikipedia.org/wiki/Modu_Chanyu
- `/ledger/1, /ledger/2`: The year of the absorption of Ji and the move from Liulihe (7th century only). Try: https://en.wikipedia.org/wiki/Ji_(state)

Spot checks:
- `/ledger/4` confirmed (https://en.wikipedia.org/wiki/Yan_(state)): 'in 314 BC Qi invaded and in a little over several months practically conquered the country'; 'a revolt eventually drove them away' (no year).
- `/ledger/6` confirmed (https://en.wikipedia.org/wiki/Qin_Kai_(general)): 'After returning to Yan, around 300 BC, he defeated the Donghu and conquered Liaodong Peninsula, wrestling it from Gojoseon.'
- `/ledger/12` confirmed (https://en.wikipedia.org/wiki/Yan_(state)): 'In 222 BC, Liaodong fell as well, and Yan was overrun by Qin'; infobox 'Conquered by Qin: 222 BC'.
- `/ledger/16` confirmed (https://en.wikipedia.org/wiki/Zang_Tu): 'Zang Tu attacked Han Guang and killed him at Wuzhong, thereby becoming king of a united Yan kingdom' (right after the 206 division, no own year).
- `/ledger/17` confirmed (https://en.wikipedia.org/wiki/Zang_Tu): Rebelled 202 'in c.August', captured 'in c.October', executed by Liu Bang; succeeded by Lu Wan. end.month 10 matches.

Area: No area in the Yan infobox (checked: area absent). The internal area problem is the Ji/Beijing block, first fix. Cliopatria max 105,154 km2.

## song (thin)

Findings:
- `/ledger/3` [not blocking]: The 20 cells of Cliopatria's old Xu row that Song gains in 450 are given counterpart 'nobody', but by this batch's own chain the land was Wu's from 512 (wu.json /ledger/2 gains the whole Xu shape) and Yue's from 473 (wu.json /ledger/7). Evidence: xu.json /ledger/1 dissolve 512 to wu; wu.json /ledger/2 region = Xu -750 shape; wu.json dissolve 473 to yue. Fix: Counterpart 'yue' (confidence 1, note 'Xu's old land, Wu's from 512 and Yue's from 473 by the batch's dossiers; page silent'), or keep 'nobody' and say in the note why not Yue.

For a gap-filler:
- `/ledger/2, /ledger/4, /ledger/5, /ledger/6`: Pages for Cliopatria's small moves with Lu (480: 24 cells; 404: 1 cell), Qi (404: 1 cell) and Zheng (366: 3 cells); all confidence 1, page silent. Try: https://en.wikipedia.org/wiki/Lu_(state)
- `/ledger/9 and identity.successors`: How Qi, Chu and Wei divided Song in 286 (King Kang page: 'Finally, Song was partitioned by Qi, Chu and Wei', no shares). Try: https://en.wikipedia.org/wiki/King_Min_of_Qi
- `/wars/0`: King Kang's conquests ('beating troops from Chu, Wei and Qi and annexing Teng', no years, no land on the Song or King Kang pages); Battle of the Hong River page not opened. Try: https://en.wikipedia.org/wiki/Battle_of_Hong_River

Spot checks:
- `/ledger/1` confirmed (https://en.wikipedia.org/wiki/Cao_(state)): 'the State of Cao was exterminated in 487 BC after the capture of Duke Fei'; 'Duke Jing of Song attacked Cao'. The Spring and Autumn table, in sources, says 'Cao ... 487 BCE: to Song', so the author's 'the page never says conquered by Song' is too cautious; confidence 2 may rise to 3.
- `/ledger/7` confirmed (https://en.wikipedia.org/wiki/Song_(state)): 'In 328, Dai Yan, a younger brother of Ticheng, took the throne and declared himself to be King Kang of Song'; the King Kang page: 'In 318 BC, Yan declared himself to be King of Song' (conflict flagged by the author).
- `/ledger/8` confirmed (https://en.wikipedia.org/wiki/Teng_(state)): 'Finally it was annihilated by King Kang of Song in 297 BC'; infobox 'Conquered by Song: 297 BCE'.
- `/ledger/9` confirmed (https://en.wikipedia.org/wiki/Song_(state)): Infobox 'Conquered by Qi: 286 BC'; 'annexed by Qi in 286, with troops from Chu and Wei serving on behalf of Qi'; no partition on the Song page.

Area: No area in the Song infobox (checked). Cliopatria max 34,727 km2.

## wey (thin)

Findings:
- `/ledger/2 vs /keyframe_review/1, /keyframe_review/2` [not blocking]: The 635 gain of Xing's land at Liaocheng (confidence 3) has no trace in any keyframe: wey_-750 and wey_-550 stay Cliopatria's shape, which lies about 40 km from Liaocheng (author's note), so the gained land is never drawn and never lost. Evidence: Xing page: 'In 635 BCE ... the State of Xing was wiped out by the State of Wey'; 'Duke Huan of Qi relocated Xing southeast to a place known as Yiyi (modern day Liaocheng City, Shandong)'. Rule 4: an event that is not small and lies outside the shapes needs a keyframe marked adjust. Fix: Add a new keyframe wey_-635 (-635..-551) = union({cliopatria: Wey, year: -750}, the Liaocheng circle), carry it into wey_-550 (adjust) and close it with a confidence-1 loss at the first Cliopatria change, or keep the shapes and say in /keyframe_review/1's note that the Xing gain is drawn as an event only.
- `/keyframe_review/10 (wey_-241) vs /ledger/10-11` [not blocking]: The new Yewang keyframe adds land no event gives Wey: the ledger loses Puyang to Qin and moves the capital, but has no gain of Yewang. Evidence: Wey page: 'In 241 BCE ... Qin captured Puyang during its attack on Wei'; 'Wey's ruler was relocated to Yewang'. Fix: Add a -241 gain, counterpart 'qin', region the Yewang circle (lon 112.93, lat 35.09, km 20), confidence 2, quoting the relocation sentence.

For a gap-filler:
- `/ledger/9`: Who took Wey's land before 320 and when ('by 320 BCE ... Wey controlled only the county of Puyang'); 'wei' is a guess at confidence 1. Try: https://en.wikipedia.org/wiki/Wei_(state)
- `/ledger/4, /ledger/5, /ledger/6, /ledger/7`: Pages for Cliopatria's 1-9 cell moves to Jin (550, 450), Wei (404) and Zhao (366); page silent. Try: https://en.wikipedia.org/wiki/Jin_(Chinese_state)
- `identity.rulers`: Ruler strip (the table was garbled for the author). Try: https://en.wikipedia.org/wiki/Wey_(state)

Spot checks:
- `/ledger/1` confirmed (https://en.wikipedia.org/wiki/Wey_(state)): Infobox 'Chuqiu (659-629 BCE)'; 'with the aid of Duke Huan of Qi ... the state was eventually restored, with its capital moved to Chuqiu'.
- `/ledger/2` confirmed (https://en.wikipedia.org/wiki/Xing_(state)): 'In 635 BCE ... the State of Xing was wiped out by the State of Wey'; Yiyi = 'modern day Liaocheng City'. The Spring and Autumn table gives 632 (author flags it).
- `/ledger/8` confirmed (https://en.wikipedia.org/wiki/Wey_(state)): 'In 346 BCE, the duke of Wey degraded his title to marquis'; 'By 320 BCE, the ruler further downgraded to jun (lord), and Wey controlled only the county of Puyang'.
- `/ledger/10` confirmed (https://en.wikipedia.org/wiki/Wey_(state)): 'In 241 BCE (year 6 of King Zheng of Qin's reign), Qin captured Puyang during its attack on Wei'; 'Wey's ruler was relocated to Yewang'.
- `/ledger/12` confirmed (https://en.wikipedia.org/wiki/Wey_(state)): Infobox 'Annexed by Qin: 209 BCE'; Qin Er Shi 'deposed Lord Jiao'; modern revision 'Lord Jiao's reign ended in 221 BCE'.

Area: No area in the Wey infobox (checked). The text check (Puyang county only by 320) is acknowledged and acted on in wey_-350/-320. Cliopatria max 7,027 km2.

## wu (thin)

Findings:
- `/ledger/5, /ledger/6` [APPLIED by reviewer]: Confidence 3 on the 482 and 473 Yue occupation events whose region is Cliopatria's 539-cell southern block, which no page names. Evidence: Wu page: Yue 'launched a surprise attack on Wu in 482 BC and conquered the capital'; Spring and Autumn page: 'Yue captured the Wu capital'; 'besieged and died when the city fell in 473'. Rule 7. Fix: Confidence lowered to 2 with a reviewer note on both events (done; the dossier re-validated with 0 errors, 0 warnings).
- `/keyframe_review/2 (wu_-584)` [not blocking]: The shape jumps from the Wuxi-Suzhou core of wu_-750's correction (two 60 km circles, under 23,000 km2) to Cliopatria's 193,280 km2 at -584, and the only event is the gain of Zhoulai (a 40 km circle, /ledger/1): about 170,000 km2 is unexplained. Evidence: shapes.csv wu_-750 193,279.7 km2; /keyframe_review/1 correction union(Wuxi 60 km, Suzhou 60 km); /ledger/1 region place Huainan 40 km. Wu page: 'Wu rose to power in the 6th century BC' (no extent). Fix: Add a confidence-1 gain at -584 (counterpart 'nobody', region minus({cliopatria: Wu, year: -750}, the two core circles, the Huainan circle), note 'Cliopatria's extent; the page dates only the rise in the 6th century') or keep the core shape after 584 until a page dates the growth.
- `/ledger/2 vs /keyframe_review/3, /keyframe_review/4` [not blocking]: The 512 conquest of Xu (confidence 3, region = Xu's Cliopatria shape plus the Sihong and Pizhou circles) is not added to Wu's keyframes: wu_-550 is passed 'ok' and tops out at 34.94N, while Xu's shape reaches 35.07N. Evidence: shapes.csv wu_-550 bbox 116.10-122.03E, 29.47-34.94N; xu_-750 bbox 116.65-117.97E, 34.42-35.07N; Xu page: 'Xu was eventually conquered by Wu in 512 BC'. Fix: Add a new keyframe wu_-512 (-512..-483) = union({cliopatria: Wu, year: -550}, the /ledger/2 region), and add the same region to wu_-480's correction.

For a gap-filler:
- `/keyframe_review/2, /keyframe_review/3`: Wu's frontier in the 6th and 5th centuries (Huai valley, Zhejiang border with Yue); Cliopatria's Yue row overlaps Wu's core 500-481. Try: https://en.wikipedia.org/wiki/Goujian
- `/ledger/1`: The location of Zhoulai (the author's Huainan placing; Fengtai County area). Try: https://en.wikipedia.org/wiki/Zhoulai
- `/ledger/0`: Founding year (century only) and capital moves (Meili, Gusu). Try: https://en.wikipedia.org/wiki/Taibo

Spot checks:
- `/ledger/1` confirmed (https://en.wikipedia.org/wiki/Battle_of_Boju): 'in 584 BC defeated Chu for the first time and annexed the Chu city of Zhoulai'.
- `/ledger/2` confirmed (https://en.wikipedia.org/wiki/Xu_(state)): 'Reduced to its heartland, Xu was eventually conquered by Wu in 512 BC'; infobox 'Conquered by Wu: 512 BC'.
- `/ledger/4` confirmed (https://en.wikipedia.org/wiki/Battle_of_Boju): 'In 505 BC, the Qin and Chu armies jointly defeated Wu in several battles'; 'King Zhao of Chu then returned to the capital Ying'.
- `/ledger/5` confirmed (https://en.wikipedia.org/wiki/Wu_(state)): 'launched a surprise attack on Wu in 482 BC and conquered the capital'; the region is not named (confidence lowered, applied).
- `/ledger/7` confirmed (https://en.wikipedia.org/wiki/Wu_(state)): 'Yue absorbed the state in 473 BC'; infobox 'Defeated by Yue: 473 BC'.

Area: No area in the Wu infobox (checked). The internal jump at 584 is the second fix. Cliopatria max 193,280 km2.

## xu (thin)

Findings:
- `/ledger (missing, -530) and /wars` [not blocking]: King Ling of Chu's siege and conquest of Xu's capital is on the Xu page but in neither the ledger nor the wars. Evidence: Xu page: 'King Ling of Chu led another army to besiege and conquer Xu's capital in order to prepare an invasion of Wu' (530 BC); chu.json /ledger/22 quotes the Chu page: 'In winter 529 BC, King Ling set off to attack the State of Xu' before his fall. Fix: Add a war (Chu, Xu, 530-529) and occupation_start (counterpart 'chu', region the Sihong circle) at -530 with occupation_end at -529 (King Ling's fall), confidence 2 and 1, or say in notes why it is left out.

For a gap-filler:
- `/ledger (missing, 645-512)`: Xu's losses before 512: 'losing control over the Huai River to Chu', 'Reduced to its heartland', Chu's invasion of 645 and the Battle of Loulin ('Xu was severely weakened'), Zhongli's victory (644-600), Wu's attack of 584; all on the Xu page, undated as land. Try: https://en.wikipedia.org/wiki/Xu_(state)
- `/keyframe_review/2, /keyframe_review/3, /keyframe_review/4`: What Cliopatria's Warring States 'Xu' row (116.5-117.4E, 34.9-35.5N, on Teng and Zhu land) stands for; a lead: the state of Xue near Tengzhou, or the other Xu (許, Xuchang) of the Spring and Autumn table ('c. 5th century BCE: to Chu'), which does not fit the place. Try: https://en.wikipedia.org/wiki/Xue_(state)
- `identity.capitals`: The Spring and Autumn table places Xu (徐) at Tancheng County, Shandong, against the Xu page's Sihong; the capital and its moves need a page. Try: https://en.wikipedia.org/wiki/Huaiyi

Spot checks:
- `/ledger/0` confirmed (https://en.wikipedia.org/wiki/Xu_(state)): 'Xu's existence is first reliably reported by the Yi Zhou Shu for 1042 BC'; 'Xu participated in the Rebellion of the Three Guards'.
- `/ledger/1` confirmed (https://en.wikipedia.org/wiki/Xu_(state)): 'conquered by Wu in 512 BC'; 'Hereby, Xu was extinguished'; Spring and Autumn table 'Xu ... 512 BCE: to Wu'.
- `/wars/1` confirmed (https://en.wikipedia.org/wiki/Xu_(state)): 'By 944 BC, Lord Yan of Xu managed to unite thirty-six Dongyi and Huaiyi states'; 850 counter-offensive; 822 campaign.
- `/wars/2` confirmed (https://en.wikipedia.org/wiki/Xu_(state)): 'Chu retaliated in 645 BC, and launched an invasion of Xu'.

Area: No area in the Xu infobox (checked). Cliopatria max 4,637 km2.

## teng (fix)

Findings:
- `/ledger/2` [APPLIED by reviewer]: Yue's occupation of Teng was ended in 297, 36 years after Yue itself fell: the Yue page has Yue partitioned by Chu and Qi in 333, so no Yue hold could last to 297. Evidence: Yue page: 'Yue was partitioned by Chu and Qi in 333 BC'; infobox 'Conquered by Chu: 333 BC'. The event was confidence 1 ('no page opened says when Yue's rule ended'). Fix: Moved the occupation_end to -333 (confidence 1, source the Yue page, added to sources) with a reviewer note; re-validated with 0 errors, 0 warnings. The 297 dissolve is unchanged.

For a gap-filler:
- `/ledger/1, /ledger/2`: The page contradicts itself (lead and infobox: conquered by Yue in 414, 'during the reign of Goujian' and 'by King Zhugou'; text: annihilated by Song in 297); when Teng recovered from Yue is on no page opened. Try: https://en.wikipedia.org/wiki/Mencius
- `notes (vassal of Lu)`: 'Teng was a vassal of the Lu state' (undated): lu.json has no vassal_start for Teng. Try: https://en.wikipedia.org/wiki/Lu_(state)

Spot checks:
- `/ledger/0` confirmed (https://en.wikipedia.org/wiki/Teng_(state)): Infobox 'Established: 1046 BCE'; founder 'Shu Xiu of Cuo'; 'Its territory corresponds to the present-day county-level city of Tengzhou'.
- `/ledger/1` confirmed (https://en.wikipedia.org/wiki/Teng_(state)): Infobox 'Conquered by Yue: 414 BCE'; 'It was conquered by King Zhugou of the Yue state'.
- `/ledger/2` mis-dated (https://en.wikipedia.org/wiki/Yue_(state)): Confidence-1 end of the Yue occupation in 297 outlives Yue (partitioned 333): moved to -333 (applied).
- `/ledger/3` confirmed (https://en.wikipedia.org/wiki/Teng_(state)): 'Finally it was annihilated by King Kang of Song in 297 BC'; infobox 'Conquered by Song: 297 BCE'; Spring and Autumn table 'Teng ... 297 BCE: to Song'.

Area: No area in the Teng infobox (checked). Cliopatria max 4,324 km2.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| yan -650 gain Ji (state) | - | exception | Listed in the author's counterparts_needing_dossiers (ji-state). |
| yan -404 loss zhao | - | exception | zhao is owned by another ea-01 part not yet written; the event itself should go (Ji/Beijing was Yan's capital to 226, see yan fixes). |
| yan -314 occupation_start qi | - | missing | qi.json has no 314 occupation of Yan (Yan page: 'in 314 BC Qi invaded and ... practically conquered the country'); author flagged it. Route to Qi's group. |
| yan -312 occupation_end qi | - | missing | Pair of the above; missing in qi.json. |
| yan -300 gain gojoseon | - | exception | gojoseon is owned by jk-02-a (not run); its Cliopatria row starts -197, so its dossier must reach back to c. 300 for this loss. |
| yan -300 gain Donghu | - | exception | Listed in counterparts_needing_dossiers (donghu, ia-01). |
| yan -284 occupation_start qi | qi -284 occupation_start | matched | qi.json /ledger/9 (cp yan). |
| yan -279 occupation_end qi | qi -279 occupation_end | matched | qi.json /ledger/11. |
| yan -226 loss qin | qin -226 gain | matched | qin.json /ledger/33. Land: both sides should include Ji once the yan fix is made. |
| yan -222 loss qin | qin -222 gain | matched | qin.json /ledger/38. |
| yan -208 gain qin-dynasty | - | exception | qin-dynasty owned by ea-01-e/ea-02-a, not run. |
| yan -208 loss xiongnu | - | missing | xiongnu.json (ia-01, written) has no gain from Yan at 208; its -208 gain is from the Donghu. Confidence 1 on both sides; either add the mirror or drop the 5 cells. |
| yan -206 split liaodong | - | exception | liaodong owned by ea-02-b, not run; it should end in 206 (Zang Tu page). |
| yan -206 gain liaodong | - | exception | As above. |
| yan -202 dissolve han-dynasty | - | exception | Successor han-dynasty not yet written (ea-02). |
| song -487 gain cao | cao -487 dissolve | matched | cao.json /ledger/1 dissolve, counterpart song; Spring and Autumn table 'Cao ... 487 BCE: to Song'. |
| song -480 gain lu | lu -480 loss | matched | lu.json /ledger/1. |
| song -450 gain nobody | - | exception | Counterpart nobody; by the batch's chain (Xu to Wu 512, Wu to Yue 473) it may be yue (song fix). |
| song -404 gain lu | - | missing | lu.json has no -404 loss to Song (1 cell, confidence 1). |
| song -404 loss qi | - | missing | qi.json's -404 gains are from lu and jin only (1 cell, confidence 1). |
| song -366 gain zheng | - | exception | zheng not yet written (another ea-01 part). |
| song -297 gain teng | teng -297 dissolve | matched | teng.json /ledger/3, counterpart song. |
| song -286 dissolve qi | qi -286 gain | matched | qi.json /ledger/8. |
| song -286 dissolve chu | chu -286 gain | matched | chu.json /ledger/40. |
| song -286 dissolve wei | - | exception | wei not yet written. |
| wey -635 gain xing | - | exception | Listed in counterparts_needing_dossiers (xing). |
| wey -550 loss jin | - | missing | jin.json has no -550 gain from Wey (1 cell, confidence 1). |
| wey -450 loss jin | jin -450 gain | matched | jin.json /ledger/7. |
| wey -404 loss wei | - | exception | wei not yet written. |
| wey -366 loss zhao | - | exception | zhao not yet written. |
| wey -320 loss wei | - | exception | wei not yet written; counterpart is the author's guess (confidence 1). |
| wey -252 vassal_start wei | - | exception | Not in wey.json by design (schema: the suzerain records vassal_start with the vassal as counterpart); Wei's dossier, not yet written, needs vassal_start 'wey' 252 (Wey page: 'making Wey a dependency of Wei'). |
| wey -241 loss qin | - | missing | qin.json has no 241 gain of Puyang from Wey and no vassal_start 'wey' (Wey page: 'In 241 BCE ... Qin captured Puyang'; Wey survived 'nominally as a Qin vassal'). Route to Qin's group. |
| wey -209 dissolve qin-dynasty | - | exception | qin-dynasty not yet written. |
| wu -584 gain chu | - | missing | chu.json has no -584 loss of Zhoulai to Wu (Battle of Boju page: 'annexed the Chu city of Zhoulai'). |
| wu -512 gain xu | xu -512 dissolve | matched | xu.json /ledger/1, counterpart wu. |
| chu -512 gain xu | xu -512 dissolve | mismatch | chu.json /ledger/24 also gains Xu in 512, but xu.json and wu.json give Xu to Wu (Xu page infobox 'Conquered by Wu: 512 BC'; Spring and Autumn table 'Xu ... 512 BCE: to Wu'). The same table lists a second Xu (許, Xuchang) that went 'to Chu' in the 5th century: chu.json may confuse the two. Route to Chu's group. |
| wu -506 occupation_start chu | chu -506 occupation_start | matched | chu.json /ledger/25. |
| wu -505 occupation_end chu | chu -505 occupation_end | matched | chu.json /ledger/26. |
| wu -482 occupation_start yue | - | exception | yue not yet written (another ea-01 part); its first shape should start 482/473. |
| wu -473 occupation_end yue | - | exception | yue not yet written. |
| wu -473 dissolve yue | - | exception | yue not yet written. |
| xu -512 dissolve wu | wu -512 gain | matched | wu.json /ledger/2. |
| teng -414 occupation_start yue | - | exception | yue not yet written. |
| teng -333 occupation_end yue | - | exception | yue not yet written (moved from 297 by the reviewer; Yue partitioned 333). |
| teng -297 dissolve song | song -297 gain | matched | song.json /ledger/8. |
| teng None vassal_start lu | - | missing | Teng page: 'Teng was a vassal of the Lu state' (undated); lu.json has no vassal_start 'teng'. |

## Problems and routing

- Applied by the reviewer: wu.json /ledger/5 and /ledger/6 confidence 3 to 2; teng.json /ledger/2 moved from -297 to -333 with the Yue (state) page added to sources. Both re-validated (0 errors, 0 warnings) and read back.
- Every Cliopatria Yan shape from 404 to 207 starts at 116.70E, leaving out Beijing (Yan's capital Ji, 116.37E); the block goes to Zhao in 404 (yan.json /ledger/3; zhao_-404 bbox reaches 117.12E, 40.10N), and the bboxes of zhongshan_-366/-301 (115.86-117.12E, 38.55-40.10N) and wei_-291 (to 117.23E, 40.42N) cover it later: check those rows. The zhao, zhongshan and wei dossiers (other ea-01 parts) must cut Beijing out, and yan.json must add it back.
- Missing mirrors in written dossiers: qi.json (Yan 314-312 occupation; Song 404 cell), lu.json (Song 404 cell; vassal Teng), jin.json (Wey 550 cell), qin.json (Wey 241 Puyang and vassal Wey), chu.json (Zhoulai 584 to Wu; its 512 Xu gain conflicts with Wu), xiongnu.json (Yan 208 cells).
- The author's one-year-offset question (Cliopatria -285/-223 against 286/222 BC) is not settled here; it affects every BC event matched to shapes.
- gojoseon (jk-02-a) must start by c. 300 BC to carry the Liaodong loss to Yan; its Cliopatria row starts -197.
- No page failed to load for the reviewer (13 pages opened).

## Gazetteer names wanted

- Sihong (place, xu, wu)
- Pizhou (place, xu, wu)
- Tengzhou (place, teng, song)
- Yewang (place, wey)
- Zhaoge (place, wey)
- Chuqiu (place, wey)
- Liulihe (place, yan)
- Xiadu (place, yan)
- Zhoulai (place, wu)
- Huai River valley (region, xu)
