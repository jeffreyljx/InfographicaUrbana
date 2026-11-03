# ea-03-f research notes (Three Kingdoms to Sui, part f): what could not be settled

Written 2026-10-19 by the ea-03-f Phase B research agent. Dossiers: western-wei, northern-qi, chen-dynasty, later-western-liang, northern-zhou, sui-dynasty (the six owned Cliopatria rows), plus eight new rebel-type dossiers for the Sui collapse: dou-jiande-s-xia, li-mi-s-wei, wang-shichong-s-zheng, liang-shidu-s-liang, liu-wuzhou-s-dingyang, xue-ju-s-qin, xiao-xian-s-liang, lin-shihong-s-chu. All 14 validate with 0 errors and 0 warnings, `--resolve` clean. 113 events, 49 source entries (20 distinct pages), all Wikipedia via WebFetch. No pre-existing dossiers for this batch were found. Every event, verdict and war cites a page opened in this run; where a page was silent the event is confidence 1 with "page silent".

## Cliopatria rows to move or split (the lives do not match the rows)

| slug | Cliopatria row | dossier life | what covers the difference |
|---|---|---|---|
| western-wei | 534..560 | 534/11 to 557/2 | 558-560 is Northern Zhou (northern-zhou_557) |
| northern-qi | 555..576 | 550/6 to 577/2 | 550-554 uses the last Eastern Wei shape; 577 = northern-qi_573 |
| chen-dynasty | 561..591 | 557/11 to 589/2 | 557-560 new keyframe _557; 589-591 belongs to the Sui |
| later-western-liang | 561..586 | 555 to 587 | new keyframes _555 and _560 |
| northern-zhou | 561..586 | 557/2 to 581/3 | 557-560 = Western Wei 560 shape; 581-586 belongs to the Sui |
| sui-dynasty | 587..627 (8 shapes) | 581/3 to 619 | 581-586 = Northern Zhou 580 shape (sui-dynasty_581); 620-627 is not Sui (see below) |

The Sui row's last three shapes are wrong as Sui: sui-dynasty_623 (623-625, 1.86 M km2) is the part of China outside Cliopatria's Tang 623 shape, that is Tang land in the south plus the Ordos; sui-dynasty_626 and _627 (109,171 km2) are Liang Shidu's Liang (liang-shidu-s-liang). The Tang dossier (group ea-04) must claim the 623 shape's land and should use the rebel slugs below as counterparts, not text names ("Dou Jiande (Xia)").

## Wikidata ids falsely shared with other rows

- Northern Qi Q1143524 is shared with Cliopatria's 'Qi' (Qi (state), -1046..-204). They are different states; the northern-qi dossier covers only 'Northern Qi'.
- Later Western Liang Q4186404 is shared with 'Western Liang' (407-409), Li Gao's Western Liang of the Sixteen Kingdoms. The later-western-liang dossier covers only 'Later Western Liang' (Wikipedia title 'Western Liang (555-587)'). The 407-409 row belongs to another part of ea-03.

## The Yangtze-Huai strip (Huainan)

Chen held the strip between the Yangtze and the Huai from 573 to the winter of 579-580, and Cliopatria draws none of it. It is approximated by Cliopatria's own Northern Qi 561 increment, expressed as `{"minus":[Northern Qi 569, Northern Qi 555]}` (northern Jiangsu, Anhui, south-east Henan, north-east Hubei); it reaches a little north of the Huai at Xuzhou. Used in northern-qi_550 (added to the Eastern Wei shape before 573), northern-qi_573 (removed), chen-dynasty_573/_580, northern-zhou_577/_580. A gap-filler with the Chen and Northern Qi military pages could replace it with a prefecture list.

## Page budget and pages not opened

- sui-dynasty used six pages (Sui dynasty, Goguryeo-Sui War, Transition from Sui to Tang, Emperor Yang of Sui, the shared Chen dynasty page, and the Tuyuhun page, which was silent on 608-617). Not opened and therefore not on the ledger: 'Emperor Wen of Sui' (Sui-Turk wars 581-600, the submission of Lingnan and Jiaozhou 589-590, the rebellions of the former Chen lands), the Sui-Champa campaign of 605, the Ryukyu expedition. About 0.29 M km2 of south-western uplands in the 592 shape is named by no opened page: unverified: page budget.
- 'Sui conquest of the Chen': https://en.wikipedia.org/wiki/Sui_conquest_of_the_Chen returned URL_NOT_FOUND. No such article is linked from the Chen page. The Chen and Sui pages cover the 588-589 campaign.
- chen-dynasty: the Chen page does not use Lingnan, Lady Xian or Hengyang and does not say how far Chen power reached into Jiaozhou. A gap-filler could open 'Chen Baxian', 'Emperor Xuan of Chen', 'Hou Jing' and 'Xiao Zhuang' for the founding years.
- western-wei, northern-qi, northern-zhou, later-western-liang: thin pages, two to four each; the Western Wei page has almost no events (Shayuan 537, the Changle marriage). No separate articles exist for the Zhou-Qi wars.

## Disagreements and open points between dossiers (for the reviewer)

1. **Ordos / Hetao in 617: Eastern Gokturks vs Liang Shidu.** The eastern-gokturks dossier (group ia-01) books a conf-1 617 direct gain of the Ordos and Hetao from the Sui, and the Ordos leaves it again in 623 (conf 1, unverified: page budget). The liang-shidu-s-liang dossier gives the Ordos (Cliopatria's Sui 626 shape) to Liang Shidu, who on the Liang Shidu page submitted to Shibi Khan, 'Dadupiqie Qaghan'. They should reconcile: the Turks should record vassal_start events for liang-shidu-s-liang and for liu-wuzhou-s-dingyang ('created him Dingyang Khan') instead of, or beside, a direct gain. Neither rebel dossier carries a vassal event of its own, because the suzerain records it.
2. **Tuyuhun recovery.** The Tuyuhun dossier has the recovery from the Sui in 619; sui-dynasty books the loss at 617 (conf 1, bridged, "page silent": Transition page names no Tuyuhun year). Both use the same region, Cliopatria's Tuyuhun 602 shape.
3. **Goguryeo buffer zone.** The Goguryeo dossier books a conf-1 "buffer zone" loss to the Sui in 612; the Goguryeo-Sui War page names no recipient and no Sui land, so sui-dynasty does not book it, and sui-dynasty_612 drops Liaodong and North Korea from the shape.
4. **Xiangyang.** western-wei gains Xiangyang in 549 (Yuwen Tai page, winter 549); the liang-dynasty dossier books the loss in 550. A one-year difference between pages.
5. **Champa.** The champa dossier books a 605 Sui occupation of Tra Kieu; sui-dynasty has no matching occupation_start because the Lam Ap/Champa page was not opened. Sui should carry occupation_start/occupation_end (605) if a gap-filler confirms them.
6. **Western Wei vs Eastern Wei.** The Luoyang-region events in western-wei mirror the eastern-wei dossier's zone (conf 1 gain/loss); the Eastern Wei dossier carries the 537-538 and 543 fights.
7. **Hanzhong.** western-wei books the 553 Hanzhong gain from liang-dynasty at conf 1 (the Yuwen Tai page does not name Hanzhong); xiao-ji-s-rebel-state books the 553 loss of Sichuan, which western-wei follows.
8. **Later Western Liang vassalage.** The vassalage is recorded by the suzerains only: western-wei (555-557), northern-zhou (557-581) and sui-dynasty (581-587), counterpart later-western-liang. later-western-liang itself carries no vassal_* events. Xiao Xian's Liang (617-621) occupied the same land and is a separate state.

## States needing a dossier from another group (counterparts named by text in my ledgers)

- Wang Lin's regime (Xiao Zhuang's Liang), 557-560, held modern Hunan and eastern Hubei, backed by Northern Qi; suggested slug wang-lin-s-liang (rebel). Named in chen-dynasty by text. A one-year Ouyang He rising (569-570) and Xiao Bo's 557 rising are not states.
- Rebels on the Transition page whose land is not carved out of the Sui here (its rival-regime table gives: Wu of Li Zitong c. 619-621, Handong of Liu Heita c. 621-623, Lu of Xu Yuanlang c. 621-623, Song of Fu Gongshi 623-624; the page does not date Du Fuwei, Luo Yi's submission or Shen Faxing's end, and loosely places Shen and Li Zitong around 619-621): Du Fuwei (southern Anhui), Luo Yi (Beijing area), Li Zitong's Wu (Jiangdu), Shen Faxing's Liang (south of the Yangtze), Liu Heita's Handong, Xu Yuanlang's Lu, Fu Gongshi's Song. Suggested slugs in the report.
- Gao Kaidao: a Cliopatria row in ea-04 ('Gao Kaidao'); the Sui loss at 617 uses its 624 shape as the region.
- Xiyu kingdoms (Western Regions): tributary/vassal tint 609-618 in sui-dynasty, no dossier.
- Tang dynasty (ea-04): the sui-dynasty `split` (618, Tang founded) and the 617 Guanzhong loss name `tang-dynasty`; the Tang dossier needs the matching found/gain.

## Region names the gazetteer lacks

None. Every region resolves (`--resolve` 0 warnings on all 14). Ambiguity: the place `Ye` also exists in Myanmar, so Ye is given with "country":"China". Cliopatria-shape arithmetic ({"cliopatria":Name,"year":y}, minus, union) is used for most corrections; named regions only where a page gives a province.

## Rebel dossiers (type rebel, cliopatria_names [], wikidata null)

dou-jiande-s-xia (Xia, 617/2-621/5, Hebei north of the Yellow River, without Gao Kaidao's northern strip), li-mi-s-wei (Wei, 617-618/10, central and eastern Henan without Luoyang), wang-shichong-s-zheng (Zheng, 619-621, Henan, northern Jiangsu and northern Anhui), liang-shidu-s-liang (Liang, 617-628/6, the Ordos and the Yellow River bend), liu-wuzhou-s-dingyang (Dingyang, 617-620, northern Shanxi, then also Taiyuan in 619), xue-ju-s-qin (Qin, 617/5-618/11, eastern Gansu), xiao-xian-s-liang (Liang, 617-621, northern Hunan in 617, then Hubei, Hunan, Guangxi and northern Vietnam from 618), lin-shihong-s-chu (Chu, 617/1-622, Jiangxi and Guangdong). Each has one or two keyframes and 3 to 5 events; regions are readings of the modern-province spans on each leader's page and the Transition page ('by 617' is the regime's start, not each acquisition). Each wikipedia field is the leader's article. Liang Shidu's and Liu Wuzhou's pages say they took Turkic titles; the vassal events belong in the eastern-gokturks dossier (see above).

## Confidence-1 events (10, each says "page silent")

sui-dynasty 3 (the 617 loss to tuyuhun; the 618 vassal_end of the Xiyu kingdoms; the October 618 gain from li-mi-s-wei), northern-zhou 1 (571 loss to later-western-liang), later-western-liang 1 (571 gain from northern-zhou, the mirror), western-wei 5 (the 537 gain, 538 loss, 538 contest_end and 543 contest_end mirrored from the eastern-wei dossier's zone, and the 553 Hanzhong gain from liang-dynasty).

## Sui shapes: what the pages and the shapes say

The Cliopatria 612 shape includes Liaodong and North Korea, while the Goguryeo-Sui War page records a Goguryeo victory; sui-dynasty_612 is the 602 shape without that land plus the Tuyuhun land. sui-dynasty_609 (609-611) is the 602 shape plus the Tuyuhun land seized in 608; sui-dynasty_587 (valid 587-588) and _592 (valid 589-601) keep their shapes and only fix the years (Chen fell in February 589); _617 keeps its shape for 617 only. sui-dynasty_618 (618-619) is Luoyang plus, from October 618, the Henan land retaken from Li Mi. The 587 shape holds about 0.22 M km2 of the Ordos, northern Shanxi and northern Hebei that is not in the Northern Zhou shape; Cliopatria removes only the Ordos in 617, and the 617 ledger events carve northern Shanxi and Hebei out through the rebel dossiers.
