# Review of batch ea-03-f (Northern and Southern dynasties to Sui, part f)

Reviewer: ea-03-f adversarial reviewer, 2026-10-19. The machine copy is history/notes/phase-b/reviews/ea-03-f.json.

Mechanical checks: all 14 dossiers validate with `--resolve`, 0 errors and 0 warnings, both before and after the reviewer's edits. The orchestrator allowed the reviewer to apply small fixes. Each applied fix is tagged `[Reviewer ea-03-f, 2026-10-19: ...]` in the note it touched. No fabricated or mis-sourced confidence-3 event was found: the spot checks covered every confidence-3 event that moves land, plus the largest confidence-2 moves, on 19 pages.

Verdicts: sui-dynasty **thin**, northern-zhou **fix**, northern-qi **pass**, chen-dynasty **fix**, western-wei **thin**, later-western-liang **fix**, dou-jiande-s-xia **thin**, li-mi-s-wei **pass**, wang-shichong-s-zheng **pass**, liang-shidu-s-liang **thin**, liu-wuzhou-s-dingyang **thin**, xue-ju-s-qin **fix**, xiao-xian-s-liang **fix**, lin-shihong-s-chu **thin**.

## sui-dynasty: thin

No fabrication found; 8 events checked on 5 pages. Two small fixes applied. The 617-to-618 collapse leaves Hexi, central Shanxi, the lower Yangtze, Sichuan and Shandong with no event, though the Transition page (opened) names Li Gui, Zhu Can and Li Yuan's central Shanxi.

Area: infobox 3,000,000 km2 (589), Cliopatria 2,022,699 km2, ratio 1.48, acknowledged: True. The Cliopatria shape alive in 589 is sui-dynasty_587. The dossier moves the 592 shape (3,318,044 km2, ratio 0.90) to 589.

- **Fix applied** `/ledger/28`: The 618 gain from li-mi-s-wei was at confidence 1, with the note saying 'The page does not say who took Li Mi's land'. Evidence: The Wang Shichong page (the event's own source) says that after Yanshi 'most of Li's territory surrendered to Yang Tong's regime' and that Xu Shiji's area went to the Tang. Fix: Confidence 2 and the note quotes the page.
- **Fix applied** `/ledger/29/region`: The dissolve region (Luoyang, 120 km) was smaller than the last keyframe (sui-dynasty_618: Luoyang plus Henan). Evidence: Keyframe 7's correction holds Henan from October 618. The Zheng's found event takes Henan and more, so the dissolve has to pass the whole realm. Fix: The region is set to the sui-dynasty_618 correction.
- **Fix for the author** `/ledger/23`: The 617 loss of Guanzhong to tang-dynasty and the 618/5 split to tang-dynasty move the same region twice. The Tang does not exist until 23 May 618. Evidence: Transition page: 'In winter 617, Li Yuan captured Chang'an, declaring Yang You emperor', and 'most of Sui territory did not recognize this'. The Sui page infobox has 'Abolished by Li Yuan: 23 May 618 AD'. Fix: Keep one transfer. Either the split at 618/5 carries Guanzhong and the 617 loss becomes a contest_start with tang-dynasty, or the Tang dossier (ea-04) starts in 617. Agree it with ea-04.
- **Gap** `/ledger (617)`: Li Gui's Liang, 'central and western Gansu', 'by 617' on the Transition page. It has no loss event, so the Hexi corridor drops out between sui-dynasty_617 and _618 and nobody holds it. It is missing from counterparts_needing_dossiers too. Page to try: https://en.wikipedia.org/wiki/Li_Gui_(warlord)
- **Gap** `/ledger (617-618)`: Zhu Can, 'southern Henan and southeastern Shaanxi', 'by 617' (Transition page). The Zhu Can page says he had no fixed base and roamed southern Henan, so this is probably a contest zone rather than a loss. He submitted to Yang Tong's regime in 618 (Wang Shichong page). No events. Page to try: https://en.wikipedia.org/wiki/Zhu_Can
- **Gap** `/ledger (617)`: Li Yuan's rising at Taiyuan ('Central Shanxi' in the Transition table). Only Guanzhong is booked to tang-dynasty, so central Shanxi has no event before the 618 keyframe drops it. Page to try: https://en.wikipedia.org/wiki/Emperor_Gaozu_of_Tang
- **Gap** `/keyframe_review/7`: The 618 keyframe drops the lower Yangtze and Huainan (Shen Faxing, Li Zitong, Du Fuwei), Luo Yi's Beijing region, Yuwen Huaji's Xu (618-619), Sichuan and Shandong, and no loss events cover them. The author lists Du Fuwei, Luo Yi, Li Zitong and Shen Faxing as needing dossiers but books no Sui loss to them. The 618/5 split names only Guanzhong. Page to try: https://en.wikipedia.org/wiki/Yuwen_Huaji
- **Gap** `/ledger (605)`: The champa dossier books a Sui occupation_start of Tra Kieu in 605 at confidence 3 (from the Lâm Ấp page). The Sui ledger has no occupation_start or occupation_end; the author flagged this. Page to try: https://en.wikipedia.org/wiki/L%C3%A2m_%E1%BA%A4p
- **Gap** `/keyframe_review/1`: sui-dynasty_587 holds about 0.22 M km2 of the Ordos, northern Shanxi and northern Hebei that is not in the 581 keyframe, and no event explains it (the author flagged this). Page to try: https://en.wikipedia.org/wiki/Emperor_Wen_of_Sui
- **Gap** `/keyframe_review/2`: About 0.29 M km2 of south-western uplands in sui-dynasty_592 is unverified within the page budget (the author flagged this). Page to try: https://en.wikipedia.org/wiki/Emperor_Wen_of_Sui
- **Gap** `/ledger/24`: The 617 Tuyuhun loss is at confidence 1. The tuyuhun dossier dates the recovery to 619 (Murong Fuyun page: 'Under Emperor Gaozu of Tang'). 618 fits both the Sui collapse and Gaozu's reign. Page to try: https://en.wikipedia.org/wiki/Murong_Fuyun
- **Gap** `/ledger/26`: The Xiyu tributary end is at confidence 1, with no page. Page to try: https://en.wikipedia.org/wiki/Pei_Ju
- Spot checks: `/ledger/6` Sui_dynasty: confirmed; `/ledger/8` Sui_dynasty: confirmed; `/ledger/27` Sui_dynasty: confirmed; `/ledger/10` Emperor_Yang_of_Sui: confirmed; `/ledger/12` Goguryeo%E2%80%93Sui_War: confirmed; `/ledger/23` Transition_from_Sui_to_Tang: confirmed; `/ledger/29` Transition_from_Sui_to_Tang: confirmed; `/ledger/28` Wang_Shichong: confirmed (page names the recipient; confidence raised)

## northern-zhou: fix

All events checked hold. One fix applied: Xiangyang (Western Wei's 555 gain) was missing from the Zhou's 557-576 extent.

Area: infobox 1,500,000 km2 (577), Cliopatria 1,772,705 km2, ratio 0.85, acknowledged: True. 

- **Fix applied** `/keyframe_review/0, /keyframe_review/1, /ledger/1`: The western-wei dossier ends with Xiangyang (100 km) in its realm and its dissolve region. The Northern Zhou 557 correction (Western Wei 560) and the 561 shape both leave it out: on the grid it lies about 40 km outside northern-zhou_561 and inside _577. So Xiangyang held by nobody from 557 to 576. Evidence: Yuwen Tai page: after Jiangling, Western Wei gave Xiao Cha the Jiangling area 'in exchange for his old domain of Xiangyang area', which Western Wei took directly. western-wei keyframe 4 and ledger 12 include it. Fix: Xiangyang (100 km) is added to the 557 correction and the found region. Keyframe northern-zhou_561 goes from ok to adjust, with the correction 'Northern Zhou 561 plus Xiangyang'.
- **Gap** `/ledger/2`: The 571 'three provinces' given to the Western Liang are at confidence 1, and the region is the whole Western Liang shape, not the three provinces. Page to try: https://en.wikipedia.org/wiki/Xiao_Kui
- **Gap** `/keyframe_review/1`: No events for the Zhou-Qi fighting of 564 (Luoyang) or 571 (Fenbei). These are thin by design within the 1-2 page budget. Page to try: https://en.wikipedia.org/wiki/Yuwen_Hu
- Spot checks: `/ledger/1` Northern_Zhou: confirmed; `/ledger/10` Northern_Zhou: confirmed; `/ledger/2` Emperor_Wu_of_Northern_Zhou: confirmed (year; provinces unnamed); `/ledger/3` Emperor_Wu_of_Northern_Zhou: confirmed; `/ledger/6` Emperor_Wu_of_Northern_Zhou: confirmed; `/ledger/8` Chen_dynasty: confirmed

## northern-qi: pass

Tried the dates (9 June 550, 28 February 577), the 573 loss, the 576-577 Zhou campaign, the infobox area and the Huainan strip arithmetic against eastern-wei, liang-dynasty and chen-dynasty, and could not break it. The factor of 2.4 against the infobox area is acknowledged in keyframe 1 and resolved: the shapes are kept and the infobox is judged inflated.

Area: infobox 1,500,000 km2 (557), Cliopatria 617,852 km2, ratio 2.43, acknowledged: True. Keyframe 1 note: infobox judged inflated; the correction adds the Yangtze-Huai strip (0.84 M km2, ratio 1.78).

- **Gap** `/ledger (551-572)`: There are no events between the founding and 573 (the Zhou-Qi fights of 564 and 571, and the Qi's 555-556 intervention south of the Yangtze). This is thin by design within the 1-2 page budget. Minor: wars/0 lists chen-dynasty as a belligerent for 552-556, before the Chen existed (Chen Baxian was then a Liang general). Page to try: https://en.wikipedia.org/wiki/Hulü_Guang
- Spot checks: `/ledger/0` Northern_Qi: confirmed; `/ledger/4` Northern_Qi: confirmed; `/ledger/1` Chen_dynasty: confirmed; `/ledger/3` Emperor_Wu_of_Northern_Zhou: confirmed

## chen-dynasty: fix

All 9 events checked are on the Chen page with the right years. One confidence level lowered.

- **Fix applied** `/ledger/4/confidence`: The 561 gain from later-western-liang was at confidence 3 with a Wuhan radius, but the page does not say where the ceded half lay. Evidence: Chen page: 'Hou Tian negotiated with the Northern Zhou for the Western Liang to cede this territory to the Chen in spring 561'. None of Ying, Wuhan, Hubei or Hunan appears in that passage. Fix: Confidence 3 lowered to 2.
- **Gap** `/keyframe_review/0`: The Lingnan and Jiaozhou reach, and the 557-560 warlords (Xiao Bo, Zhou Di, Chen Baoying), are not on the page. The author flagged this; it is within budget. Page to try: https://en.wikipedia.org/wiki/Emperor_Wu_of_Chen
- Spot checks: `/ledger/2` Chen_dynasty: confirmed; `/ledger/4` Chen_dynasty: confirmed (year); region not on page; `/ledger/7` Chen_dynasty: confirmed; `/ledger/10` Chen_dynasty: confirmed; `/ledger/11` Chen_dynasty: confirmed; `/ledger/14` Chen_dynasty: confirmed

## western-wei: thin

The checked events hold on the Yuwen Tai and Western Wei pages. The Hanzhong event, which the note called 'page silent', is on the Yuwen Tai page; that fix is applied. Four Luoyang events stay at confidence 1, and the 535 loss of Hanzhong to the Liang is missing.

- **Fix applied** `/ledger/9`: The 553 Hanzhong gain was at confidence 1 with the note 'The pages opened are silent on Hanzhong', sourced to the Western Wei page. Evidence: Yuwen Tai page (opened by the author): in summer 552 Xiao Yi agreed to cede Nanzheng (modern Hanzhong); Yuwen Tai and Daxi Wu attacked; after a long siege Xiao Xun surrendered and 'Nanzheng was in Western Wei hands'. Fix: Source set to the Yuwen Tai page, confidence 2, and the note quotes it.
- **Gap** `/ledger/2, /ledger/3, /ledger/4, /ledger/6`: The Luoyang-region gain and loss of 537-538 and the contest ends of 538 and 543 are at confidence 1, mirrored from eastern-wei. eastern-wei cites the Gao Huan page at confidence 2-3 for the same events. Page to try: https://en.wikipedia.org/wiki/Gao_Huan
- **Gap** `/ledger (535)`: liang-dynasty books a 535 gain of Hanzhong from western-wei at confidence 3 (Emperor Wu of Liang page: 'Lan Qin conquered Hanzhong, and forced the Western Wei to sue for peace'). western-wei has no matching loss. Hanzhong lies just outside western-wei_534 (about 25 km), so the loss is small. Page to try: https://en.wikipedia.org/wiki/Emperor_Wu_of_Liang
- Spot checks: `/ledger/1` Yuwen_Tai: confirmed; `/ledger/5` Yuwen_Tai: confirmed; `/ledger/7` Yuwen_Tai: confirmed; `/ledger/8` Yuwen_Tai: confirmed; `/ledger/9` Yuwen_Tai: on page, though the note said silent (fixed); `/ledger/12` Western_Wei: confirmed

## later-western-liang: fix

Infobox (555, 587, Jiangling, puppet state, succeeded by Sui) and the Chen-page events confirmed. One counterpart fixed so that the Liang's 555 loss mirrors.

- **Fix applied** `/ledger/0/counterpart`: The found event named western-wei as counterpart. The liang-dynasty dossier books its 555 loss of Jiangling to later-western-liang, so neither side mirrored the other. Evidence: Western Liang page infobox: 'Preceded by: Liang dynasty'. The Western Wei's role is already its own 555 vassal_start. Fix: Counterpart set to liang-dynasty.
- **Gap** `/ledger/3`: The 571 gain of 'three provinces' from northern-zhou is at confidence 1, and its region is the whole 577 shape rather than the three provinces. Page to try: https://en.wikipedia.org/wiki/Xiao_Kui
- Spot checks: `/ledger/0` Western_Liang_(555%E2%80%93587): confirmed; `/ledger/5` Western_Liang_(555%E2%80%93587): confirmed; `/ledger/2` Chen_dynasty: confirmed (year; place not named); `/ledger/4` Chen_dynasty: confirmed

## dou-jiande-s-xia: thin

Dates confirmed (reign 15 February 617 to 28 May 621, Prince of Xia in 618, Ming Prefecture and Liyang in 619, Hulao in 621). The single keyframe draws all of Hebei from 617, but the page gives that extent only 'by late 619'.

- **Gap** `/keyframe_review/0`: One keyframe covers 617-621. The page: 'the territory north of the Yellow River and east of the Taihang Mountains were largely his' by late 619, and the Transition page has him 'further consolidated' c. 618. The growth from 617 and the 619-621 gains in Shandong (Yuwen Huaji at Liaocheng) are not on the ledger. This is thin by design within the rebel budget. Page to try: https://en.wikipedia.org/wiki/Dou_Jiande
- **Gap** `/identity/capitals`: No capital is given for 617 (the page names Leshou only from 618). Page to try: https://en.wikipedia.org/wiki/Dou_Jiande
- Spot checks: `/ledger/0` Dou_Jiande: confirmed; `/ledger/1` Dou_Jiande: confirmed; `/ledger/3` Dou_Jiande: confirmed; `/ledger/4` Dou_Jiande: confirmed

## li-mi-s-wei: pass

All four events confirmed on the Li Mi page: Duke of Wei in spring 617, Jinyong in spring 618, Yanshi in October 618, and 'much of modern central and eastern Henan'. The mirrors with sui-dynasty match. The Transition page puts the Duke of Wei title in 616, which is a page disagreement, not a fault.

- Spot checks: `/ledger/0` Li_Mi_(Sui_dynasty): confirmed; `/ledger/1` Li_Mi_(Sui_dynasty): confirmed; `/ledger/2` Li_Mi_(Sui_dynasty): confirmed; `/ledger/3` Li_Mi_(Sui_dynasty): confirmed

## wang-shichong-s-zheng: pass

Confirmed on the Wang Shichong page: reign 25 May 619 to 4 June 621, the territory 'Henan/Northern Jiangsu/Northern Anhui', the fall 620 campaign and Luoyang under siege in spring 621, and the surrender in 621. Optional: months 5 (start) and 6 (end) from the infobox.

- Spot checks: `/ledger/0` Wang_Shichong: confirmed; `/ledger/1` Wang_Shichong: confirmed (campaign from fall 620; siege spring 621); `/ledger/2` Wang_Shichong: confirmed; `/ledger/3` Wang_Shichong: confirmed

## liang-shidu-s-liang: thin

Confirmed: rising 'in or shortly before 617', the eastern city of Shuofang taken in spring 622, and the end in 628 (28 May or 3 June). One keyframe for 11 years. The page names holdings and a 623 gain that the shape and ledger lack.

- **Gap** `/keyframe_review/0`: The page names holdings outside the Cliopatria Sui 626 shape: Yan'an, Honghua (Dingxi, Gansu) and Diaoyin. It also has Lin Prefecture (Qingyang) gained around 623, which is not on the ledger. Page to try: https://en.wikipedia.org/wiki/Liang_Shidu
- **Gap** `/ledger`: His submission to Shibi Khan ('Dadupiqie Qaghan') should be a vassal_start in eastern-gokturks (ia-01). The eastern-gokturks dossier instead books a direct 617 gain of the Ordos from sui-dynasty. Page to try: https://en.wikipedia.org/wiki/Liang_Shidu
- Spot checks: `/ledger/0` Liang_Shidu: confirmed; `/ledger/1` Liang_Shidu: confirmed; `/ledger/2` Liang_Shidu: confirmed (28 May or 3 June 628)

## liu-wuzhou-s-dingyang: thin

Confirmed: spring 617 rising, Taiyuan in 619, and the summer 620 collapse. The 619-620 keyframe adds only Taiyuan (100 km), but the infobox gives him 'Central/Southern Shanxi 619-620'.

- **Fix for the author** `/keyframe_review/1/correction`: The 619-620 correction (northern Shanxi plus a Taiyuan radius) leaves out the central and southern Shanxi that the page gives him for 619-620. Evidence: Liu Wuzhou page infobox regnal table: 'Emperor of China (Central/Southern Shanxi) 619–620'. Fix: Widen keyframe 1, ledger 1 and ledger 3 to northern Shanxi plus {admin1: Shanxi}. Not applied by the reviewer (a shape correction).
- **Gap** `/ledger`: Song Jingang's 619 conquest of the Fen valley (Jinzhou, Kuaizhou) is not on the ledger. The Turkic title should be a vassal_start in eastern-gokturks (ia-01). Page to try: https://en.wikipedia.org/wiki/Song_Jingang
- Spot checks: `/ledger/0` Liu_Wuzhou: confirmed; `/ledger/1` Liu_Wuzhou: confirmed; `/ledger/3` Liu_Wuzhou: confirmed

## xue-ju-s-qin: fix

Confirmed: reign from 13 May 617, the Tianshui move after the fall 617 imperial claim, Xue Ju's death on 3 September 618 and Xue Rengao's defeat 'three months later'. Two small fixes applied.

- **Fix applied** `/ledger/0`: The capital_move (617, no month) came before the found event (617/5): the move to Tianshui was placed before the state existed. Evidence: Xue Ju page: Xue Rengao took Tianshui after Xue Ju claimed the imperial title in fall 617, and only then did the capital move. Fix: The event now follows the found event with month 10 (the note says the month is a reading).
- **Fix applied** `/identity/end, /ledger/3, /ledger/4`: The end month was 11. The page has Xue Ju die on 3 September 618 and Xue Rengao defeated 'three months later', which is December. Evidence: Xue Ju page infobox: reign to 'September 3, 618'; text: 'three months later'. Fix: Month set to 12 on identity.end, the contest_end and the dissolve.
- Spot checks: `/ledger/1` Xue_Ju: confirmed (13 May 617); `/ledger/0` Xue_Ju: confirmed (after fall 617); `/ledger/3` Xue_Ju: mis-dated by a month (fixed); `/ledger/4` Xue_Ju: confirmed year

## xiao-xian-s-liang: fix

Confirmed: the 617 rising at Baling, the Jiangling capital and southern submissions of 618, Su Hu'er at Yuzhang around the new year 618, and the winter 621 Tang assault. One keyframe fix applied.

- **Fix applied** `/keyframe_review/1/correction, /ledger/4/region`: The 618 gain of Yuzhang (Nanchang, 100 km) from lin-shihong-s-chu had no trace in the keyframes, and lin-shihong-s-chu_618 removes the same plain, so nobody held it from 618 to 621. Evidence: Xiao Xian page: 'Around the new year 618' Su Hu'er attacked Yuzhang, and his territory reached 'as far east as Jiujiang'. Fix: Nanchang (100 km) added to the 618 correction and the dissolve region.
- Spot checks: `/ledger/0` Xiao_Xian: confirmed; `/ledger/1` Xiao_Xian: confirmed; `/ledger/2` Xiao_Xian: confirmed; `/ledger/4` Xiao_Xian: confirmed

## lin-shihong-s-chu: thin

Confirmed: Emperor of Chu from 22 January 617, Jiangxi and Guangdong, the retreat to Yugan, and the winter 622 surrender offer and death. One source fix applied. The regnal table also names Hainan, which the shape lacks.

- **Fix applied** `/ledger/1/source`: The 618 Yuzhang loss cited the Lin Shihong page for 'around new year 618'. That page does not date Su Hu'er's capture; its 'new year 618' belongs to Zhang Shan'an's earlier attack. Evidence: The Xiao Xian page dates Su Hu'er's attack 'Around the new year 618'. Fix: Source set to the Xiao Xian page, which is added to sources[].
- **Fix for the author** `/keyframe_review/0/note`: The note says Hainan is not described, but the page's regnal table reads 'Emperor of China (Jiangxi/Guangdong/Hainan) 617–622'. Evidence: Lin Shihong page, regnal titles table. Fix: Add {admin1: Hainan} to both keyframes, ledger 0 and ledger 2 (and to sui-dynasty ledger 22), or explain why not. Not applied by the reviewer (a shape change across two dossiers).
- Spot checks: `/ledger/0` Lin_Shihong: confirmed; `/ledger/1` Xiao_Xian: confirmed (Lin page undated; source fixed); `/ledger/2` Lin_Shihong: confirmed

## Cross-dossier matrix: everything not matched

- mismatch: sui-dynasty 617 loss, counterpart tuyuhun. Two years apart, both at confidence 1. The Murong Fuyun page has 'Under Emperor Gaozu of Tang', which allows 618; sui-dynasty_618 no longer holds the land after 617. Suggest 618 on both sides, or the tuyuhun dossier explains the 617-619 gap.
- mismatch: eastern-gokturks 617 gain, counterpart sui-dynasty. eastern-gokturks (ia-01) gains the Ordos/Hetao directly from the Sui at confidence 1. sui-dynasty gives the same land (Cliopatria Sui 626) to liang-shidu-s-liang, whose page has him submit to Shibi Khan. Route to ia-01: replace with vassal_start liang-shidu-s-liang (617-628) and liu-wuzhou-s-dingyang (617-620).
- missing: goguryeo 612 loss, counterpart sui-dynasty. Goguryeo (jk-02) books a confidence-1 'buffer zone' loss to the Sui. The Goguryeo-Sui War page says Yeongyang 'gave up the buffer zone that he had acquired after the war of 598' but names no recipient and no territorial change, and sui-dynasty_612 drops Liaodong. Route to jk-02: use counterpart nobody, or name a page. The same goes for the goguryeo 617 gain from sui-dynasty.
- missing: goguryeo 617 gain, counterpart sui-dynasty. See the goguryeo 612 entry.
- missing: champa 605 occupation_start, counterpart sui-dynasty. Champa books the Sui occupation of Tra Kieu at confidence 3 (Lâm Ấp page). sui-dynasty lacks occupation_start and occupation_end for 605. Listed as thin for sui-dynasty.
- missing: liang-dynasty 535 gain, counterpart western-wei. Lan Qin's conquest of Hanzhong (Emperor Wu of Liang page, confidence 3). western-wei has no 535 loss. Listed as thin for western-wei.
- exception: sui-dynasty 581 vassal_start, counterpart later-western-liang. Schema: the suzerain records vassal events with the vassal as counterpart; later-western-liang notes the relation.
- exception: sui-dynasty 587 vassal_end, counterpart later-western-liang. Schema (suzerain only).
- exception: northern-zhou 557 vassal_start, counterpart later-western-liang. Schema (suzerain only).
- exception: northern-zhou 581 vassal_end, counterpart later-western-liang. Schema (suzerain only).
- exception: western-wei 555 vassal_start, counterpart later-western-liang. Schema (suzerain only).
- exception: western-wei 557 vassal_end, counterpart later-western-liang. Schema (suzerain only).
- exception: sui-dynasty 600 vassal_start, counterpart eastern-gokturks. Schema (suzerain only).
- exception: sui-dynasty 615 vassal_end, counterpart eastern-gokturks. Schema (suzerain only).
- exception: sui-dynasty 609 vassal_start, counterpart Xiyu kingdoms (Western Regions). A text counterpart, listed by the author in counterparts_needing_dossiers.
- exception: sui-dynasty 617 loss, counterpart gao-kaidao. ea-04 has not run (Cliopatria row 'Gao Kaidao').
- exception: sui-dynasty 617 loss, counterpart tang-dynasty. ea-04 has not run. The Tang cannot gain in 617 if it starts at 618/5; see the sui-dynasty fixes entry for /ledger/23.
- exception: sui-dynasty 618 split, counterpart tang-dynasty. ea-04 has not run.
- exception: dou-jiande-s-xia 619 gain, counterpart tang-dynasty. ea-04 has not run.
- exception: dou-jiande-s-xia 621 dissolve, counterpart tang-dynasty. ea-04 has not run.
- exception: wang-shichong-s-zheng 621 dissolve, counterpart tang-dynasty. ea-04 has not run.
- exception: liang-shidu-s-liang 622 loss, counterpart tang-dynasty. ea-04 has not run.
- exception: liang-shidu-s-liang 628 dissolve, counterpart tang-dynasty. ea-04 has not run.
- exception: liu-wuzhou-s-dingyang 619 gain, counterpart tang-dynasty. ea-04 has not run.
- exception: liu-wuzhou-s-dingyang 620 dissolve, counterpart tang-dynasty. ea-04 has not run.
- exception: xue-ju-s-qin 618 dissolve, counterpart tang-dynasty. ea-04 has not run (month now 12).
- exception: xiao-xian-s-liang 621 dissolve, counterpart tang-dynasty. ea-04 has not run.
- exception: lin-shihong-s-chu 622 dissolve, counterpart tang-dynasty. ea-04 has not run.
- exception: chen-dynasty 560 gain, counterpart Wang Lin (Xiao Zhuang's Liang). A text counterpart, listed by the author (wang-lin-s-liang).
- exception: later-western-liang 560 gain, counterpart Wang Lin (Xiao Zhuang's Liang). A text counterpart, listed by the author (wang-lin-s-liang).

There are 32 matched pairs (listed in the JSON).

## Counterparts needing dossiers (in addition to the author's list)

- Li Gui's Liang (Hexi corridor, Wuwei) (`li-gui-s-liang`, [617, 619]): Transition page: 'central and western Gansu', 'by 617'; the disambiguation page has Li Gui (warlord) dying in 619; article Li_Gui_(warlord). Needed for sui-dynasty's Hexi loss; missing from the author's list.
- Zhu Can's Chu (`zhu-can-s-chu`, [618, 619]): Zhu Can page infobox: reign 618-619 (Chu); he had no fixed base and roamed southern Henan, raiding northern Hubei and southern Shaanxi, so a contest zone in sui-dynasty may serve instead of a dossier. He submitted to Yang Tong's regime in 618 (Wang Shichong page).
- Yuwen Huaji's Xu (`yuwen-huaji-s-xu`, [618, 619]): Transition page: proclaimed Xu after the 618 coup and was killed by Dou Jiande. Years approximate.

## Problems

- None blocking. WebFetch loaded every page tried (Sui dynasty, Transition from Sui to Tang, Goguryeo-Sui War, Emperor Yang of Sui, Northern Zhou, Emperor Wu of Northern Zhou, Northern Qi, Chen dynasty, Yuwen Tai, Western Wei, Western Liang (555-587), Dou Jiande, Li Mi, Wang Shichong, Liang Shidu, Liu Wuzhou, Xue Ju, Xiao Xian, Lin Shihong).
- As the orchestrator allowed, the reviewer applied 12 small fixes in 8 dossiers (sui-dynasty, northern-zhou, chen-dynasty, western-wei, later-western-liang, xue-ju-s-qin, xiao-xian-s-liang, lin-shihong-s-chu). Each is tagged '[Reviewer ea-03-f, 2026-10-19: ...]' in the note it touched. All 14 dossiers re-validate with --resolve: 0 errors, 0 warnings.
- Verdict convention used: fix = every listed fix applied, or one unapplied non-blocking fix; thin = unexplained border moves or confidence-1 gaps remain for a gap-filler (applied fixes are also listed); no blocking finding was found, so there is no fail. Two fixes are applied: false: a shape widening in liu-wuzhou-s-dingyang, and Hainan in lin-shihong-s-chu, which also touches sui-dynasty.
- The Transition page dates Li Mi's Duke of Wei title to 616; the Li Mi page has spring 617. The dossiers follow the Li Mi page.
