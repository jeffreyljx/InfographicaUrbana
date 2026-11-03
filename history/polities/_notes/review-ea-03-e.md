# Review of batch ea-03-e (Northern Yan, Xia, Liu Song, Southern Qi, Liang, Eastern Wei, Hou Jing's Han, Xiao Ji)

Reviewer, 2026-10-19. Machine copy: history/notes/phase-b/reviews/ea-03-e.json.

## Verdicts
| slug | verdict | why |
| --- | --- | --- |
| northern-yan | pass | 4 events checked on Northern Yan and Feng Hong pages, all confirmed; no area on the page; mirrors in later-yan and northern-wei found. |
| xia | **fail** | The 418-426 correction draws land that no page or event gives Xia (below). Seven events checked, all confirmed. |
| liu-song-dynasty | **fail** | The 420-422 shape overlaps xia by about 158,000 km2 and the 423 shape drops that land with no event. Seven events checked, all confirmed. |
| southern-qi | fix (done) | Xiao Baojuan's reign moved from 499 to 498 (Emperor Ming page: Ming died 1 September 498, Baojuan succeeded him). Five events checked, all confirmed. |
| liang-dynasty | thin | Ten events checked, all confirmed. Gaps: Hefei before 506, Hanzhong 553, the 545 occupation, Sichuan 502-503. |
| eastern-wei | thin | Six events checked, all confirmed. Shouyang overlaps hou-jing-s-han in 549-550; 548 at confidence 1. |
| hou-jing-s-han | thin | Seven events checked, all confirmed. Same Shouyang overlap; the Western Wei's share of the 13 provinces in 547 is not recorded. |
| xiao-ji-s-rebel-state | pass | Three events checked on Xiao Ji and Emperor Yuan pages, all confirmed. |

The validator passes all eight with --resolve (0 errors, 0 warnings). No infobox carries an area (checked on all six state pages); every dossier says so.

## Blocking findings (author)

**xia /keyframe_review/6 and /7 (xia_418, xia_426).** The union of the Cliopatria 417 and 426 shapes and Pingliang is 1,618 H3 cells. Minus the 416 shape (803) and the gazetteer Guanzhong (239), 590 cells remain (about 150,000 km2) that no event names. Of these, 277 (about 70,000 km2) lie south of 34 N: the Qinling, Shangluo and the upper Han valley round Ankang. Cliopatria's xia_426 reaches 32.30 N, and 299 of its 1,084 cells lie south of 34 N. No page opened (Xia, Helian Bobo, Helian Chang, Taiwu) puts any of that in Xia; the Helian Chang page names none of Shangluo, Hanzhong, Weixing or Ankang. The keyframe note calls the shape "Guanzhong, Pingliang". The 427 loss region (/ledger/12) then hands the strip to the Wei as "Tongwancheng and the Ordos".
Fix: clip the Cliopatria 426 term to north of the Qinling, and say in the note which lands north of the Wei valley (Weibei, Longdong) come with the 418 gain. Clip /ledger/7, /ledger/12, /ledger/16 and /identity/successors/0/land the same way. Alternatively, add a sourced gain for the strip.

**liu-song-dynasty /keyframe_review/0 and /ledger/0 (420-422).** The shape is "Western Jin 420 minus Guanzhong". It keeps 627 cells that xia_418 holds in the same years: 350 north of 34 N (the loess plateau, 35-37 N, Xia's since 408-418 per the Helian Bobo page) and 277 south. From 423 the Cliopatria Liu Song 426 shape lacks them, with no event. Of the 1,083 cells between the 420 and 423 shapes, only the Luoyang, Xuchang and Jining discs are explained.
Fix: subtract the corrected Xia 418 shape instead of the gazetteer Guanzhong. Agree the Qinling strip with the xia fix: if Song held it, add it to the 423-451 corrections with a note.

## Applied by the reviewer
- southern-qi /identity/rulers/5/from: 499 -> 498, with note and source. Validated and read back.

## Gaps (gap-filler)
- liang-dynasty /ledger/5: Hefei is drawn as Liang's in 502-505, yet the ledger gains it in 506 with no earlier loss. Try Emperor Xuanwu of Northern Wei.
- liang-dynasty /ledger/28: Hanzhong lost in 553 at confidence 1. Try Yuwen Tai.
- liang-dynasty /ledger/14: occupation_start in 545 at confidence 1. early-ly-dynasty quotes the Lý Nam Đế page at confidence 2.
- liang-dynasty /ledger/1: the 503 gain of Sichuan comes from a southern-qi that dissolved in April 502 and gave Liang this land, and the 502 keyframe already draws Sichuan. Use Liu Jilian as the counterpart, and either remove Sichuan from 502-503 or record a contest 502-503.
- liang-dynasty /identity/wikidata: Q783489 is shared with later-liang-dynasty. Set it to null as xia did, or verify it.
- liang-dynasty notes item (6) says the court was "reduced to Jiankang's neighbourhood", but liang-dynasty_555 draws the whole south. Make the text match the correction.
- eastern-wei /ledger/10 and hou-jing-s-han /keyframe_review/2: both hold Shouyang (116.78 E, 32.55 N) in 549-550. Find who held it after Hou crossed the Yangtze (try Gao Cheng), then subtract the disc from one side.
- eastern-wei /ledger/9: the 548 regain of Henan is at confidence 1, and the Western Wei's Yingchuan (547-549) is not recorded. Try Gao Cheng.
- hou-jing-s-han /ledger/0: the Western Wei's share of the 13 provinces in 547 is not recorded (western-wei is not written yet).
- liu-song-dynasty /ledger/9: occupation_end in 446 at confidence 1.
- liu-song-dynasty /ledger/3 and /ledger/4: "Huatai" is drawn as an 80 km disc round Anyang city, which covers Ye north of the Yellow River. Centre it on Hua County (about 114.52 E, 35.58 N), together with northern-wei /ledger/11.
- xia /ledger/9: confidence 1 (western-qin has the same event at confidence 2). The 427-431 remnant has no page; the infobox gives Pingliang only to 430.
- southern-qi and eastern-wei are over their page budgets; their unverified fronts are thin by design.

## Cross-dossier (routed)
- northern-wei: no 431 regain from liu-song-dynasty (the author's notes wrongly say one exists); no 497 or 500 gains from southern-qi; no 506, 525 or 526 events with liang-dynasty; its 433 "Liaoxi" region contains the Yan capital.
- later-qin: the Ordos loss is dated 414 at confidence 1, where the Helian Bobo page has 408 (and 407 for the rising), and there is no 416 loss of Anding.
- western-jin: its 418 loss and 420 dissolve share the "Guanzhong only" reading behind the Xia/Liu Song overlap.
- Vassal events (Liu Song over Northern Yan 435-436; Liang over Hou Jing 547-548) appear on the suzerain side only, as the schema prescribes. They are recorded as exceptions.
- Not yet written: western-wei, northern-qi, chen-dynasty, later-western-liang.
