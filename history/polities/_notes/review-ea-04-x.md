# Review of batch ea-04-x

Reviewer: adversarial review, Phase B, 2026-10-19. Inputs: the 19 dossiers of history/notes/phase-b/reports/ea-04-x.json, the author's notes _notes/ea-04-x.md, and the neighbour ledgers (tang-dynasty, sui-dynasty, tibetan-empire, tibetans, qocho-kingdom, ganzhou-kingdom, western-gokturks, turgesh, xueyantuo, second-turkic-khaganate, kingdom-of-gaochang, kingdom-of-kucha, nanzhao, champa, ngo-dynasty, southern-han, later-liang-dynasty, later-tang, former-jin, yan-kingdom, min, southern-tang, wuyue, northern-song, western-xia; kingdom-of-dali is not written yet). The machine copy is history/notes/phase-b/reviews/ea-04-x.json.

Mechanical checks: validate_dossier.py --resolve on all 19, 0 errors and 0 warnings, before and after the reviewer's edits. No dossier owns a Cliopatria row, so there are no shape verdicts to check and no data/README.md rows apply. Spot checks: 4-6 events per dossier through WebFetch (82 in all), weighted to confidence 3 and the largest land moves; no fabricated event was found.

Verdict meanings in this review: **fix** = every dossier-local finding was applied by the reviewer (what remains is cross-dossier); **thin** = valid and honest, gaps listed for a gap-filler (any unapplied item is non-blocking); **fail** = an unapplied blocking finding: land drawn against the cited page or against the dossier's own ledger.

| dossier | verdict | in one line |
| --- | --- | --- |
| yan-an-lushan | fix | Dates checked against both pages; one confidence lowered. |
| qi-huang-chao | fix | All four checked events confirmed; keyframe split so the 882 loss shows. |
| guiyi-circuit | fail | Events confirmed, but the last keyframe holds Suzhou against the page's own statement and overlaps the Ganzhou kingdom. |
| protectorate-general-to-pacify-the-west | fix | Thirteen keyframes follow the page's dated swings; one capital span shortened. |
| beiting-protectorate | thin | Thin by design (stub page, page budget); both events confirmed. |
| protectorate-general-to-pacify-the-north | thin | Plateau 647-682 confirmed; the 682-784 rump is a gap. |
| protectorate-general-to-pacify-the-south | fail | A dated land move on the cited page is missing and misreported as absent. |
| jinghai-circuit | pass | All checked events confirmed; the 866-880 overlap with the Tang is a cross-dossier ownership question (cross_checks). |
| li-gui-s-liang | fix | One mis-dated confidence-2 event fixed. |
| liu-heita-s-handong | fix | Events confirmed; keyframe split to match the ledger. |
| fu-gongshi-s-song | pass | Tried the dates, the vassal pair and the 619/621 claims the author rejected: the page bears the author out. |
| xu-yuanlang-s-lu | fix | Events confirmed; the 621 submission added so that the gain follows a loss. |
| dingnan-circuit | fix | Events confirmed; keyframe start and capital span corrected. |
| zhao-five-dynasties-period | thin | Events confirmed; one keyframe for 160 years and a circle smaller than the page's prefecture list. |
| yiwu-five-dynasties | thin | All events confirmed; 900-910 not drawn. |
| qingyuan-circuit | pass | Events confirmed; the founding counterpart (min, which ended in 945) is a cross-dossier question. |
| lulong-circuit | fail | Events confirmed, but the keyframe does not carry the 898 gain or the 900 loss, which lies outside the drawn land. |
| weibo-circuit | thin | Events confirmed; the shape is a small reading of a six-prefecture circuit. |
| xiliangfu | pass | All events confirmed on the page. Note: family 'china' for a Tibetan polity, where the tibetans dossier uses 'india'; the orchestrator may want them alike. |

## yan-an-lushan: fix

Findings:

- `/ledger/8/confidence` (applied by the reviewer). The 759 gain of Bian (Kaifeng) and Luoyang was at confidence 3 although the cited page gives no year or season for the capture. Evidence: Shi Siming page (WebFetch): neither the sentence 'quickly captured Bian Prefecture ... and Luoyang' nor the one before it carries a date; the nearest dates are the Yecheng battle (7 April 759) and the Great Holy Prince of Yan claim. The year 759 is right by the narrative and the Tang dossier's 759 loss, but it is not on the page. Fix: Confidence 2, with a sentence in the note saying the year is read from the narrative.

Thin (for a gap-filler):

- `/ledger/12`: Bian (Kaifeng) after 759: the 762 loss is confidence 1 (page silent); a page that dates the Tang recovery of Bian is needed (try https://en.wikipedia.org/wiki/Shi_Chaoyi)
- `/ledger/10`: Shi Siming's return to Fanyang is dated 759.5 (his enthronement); the Shi Siming page's own chronology of his re-rebellion (Wu Cheng'en plot, Wei Prefecture) could not be read cleanly through WebFetch; a page dating his break with the Tang (758 in most accounts) would let the 758 keyframe carry northern Hebei (try https://en.wikipedia.org/wiki/Shi_Siming)

Spot checks: `/ledger/3` confirmed: 'captured the "Eastern Capital" city of Luoyang on 18 January 756'; `/ledger/6` confirmed: 'recaptured both Chang'an and Luoyang in late 757'; `/ledger/7` confirmed: submission after the winter 757 events, 'holding only Yecheng and its surrounding region'; `/ledger/8` land confirmed, year not on page (lowered to confidence 2); `/ledger/13` confirmed: 'dying on 17 February 763, ending the eight-year-long rebellion'.

Area: No infobox area on the An Lushan rebellion page (infobox gives only dates and 'Northern China'); keyframes 31,000-400,000 km2.

## qi-huang-chao: fix

Findings:

- `/keyframe_review/0` (applied by the reviewer). The single keyframe 881-883 (Guanzhong, about 60,000 km2) kept Tong and Hua prefectures through 883, although the 882 loss of the Weinan circle (about 18,000 km2, 30 percent of the shape) is in the ledger; an event that large needs a keyframe. Evidence: Huang Chao Rebellion page: 'By fall 882, the Qi general Zhu Wen, in charge of Tong Prefecture' surrendered; 'By winter 882, Hua Prefecture also surrendered to Tang'. Gazetteer: Weinan 70 km lies wholly inside Guanzhong (18,000 of 60,000 km2). Fix: Split into qi-huang-chao_881 (881, Guanzhong) and qi-huang-chao_882 (882-883, Guanzhong minus Weinan 70 km), notes updated.

Spot checks: `/ledger/0` confirmed: 'fled toward Xichuan Circuit on January 8, 881'; Qi proclaimed after Huang moved into the palace; `/ledger/2` confirmed: fall 882 (Tong, Zhu Wen) and winter 882 (Hua, Wang Yu); `/ledger/3` confirmed: 'In summer 883, Li Keyong entered Chang'an'; `/ledger/4` confirmed: July 13, 884, killed by his nephew Lin Yan after fleeing into Langhu Valley (Laiwu).

Area: No infobox area (location 'Jiangnan and part of the Yellow River Basin'; troop strengths only).

## guiyi-circuit: fail

Findings:

- `/keyframe_review/9 and /ledger/14/region` (not applied, for the author). The last keyframe (914-1036) and the 1036 dissolve keep the Suzhou (Jiuquan) circle as Guiyi land to the end, and the dissolve text calls Shazhou, Guazhou and Suzhou 'the Cao family's remaining prefectures'; the cited page says the opposite for at least the last four decades. Evidence: Guiyi Circuit page (WebFetch): 'By the end of the 10th century, the Guiyijun was only able to keep the prefectures of Guazhou and Shazhou'; the page does not list Suzhou as Guiyi land in the Cao period. The Suzhou circle overlaps the ganzhou-kingdom shape by about 55,000 km2 (gazetteer, year 950), so the two dossiers draw the same land for 1036-894=142 years. Fix: Add a loss of the Suzhou circle {lon 98.49, lat 39.74, km 120} with counterpart ganzhou-kingdom (or nobody), confidence 1, at the latest 1000 ('by the end of the 10th century'; earlier if a page dates it, e.g. with the Ganzhou Uyghurs after 894); split keyframe 9 into 914-999 and 1000-1036 (Dunhuang 200 km only); set /ledger/14/region to {place Dunhuang, km 200, text 'Shazhou and Guazhou'} and the same in /identity/successors/0/land; say in /notes that the Suzhou years before 1000 are a reading.
- `/ledger/13` (not applied, for the author). The 914 loss of Yizhou and Xizhou (confidence 1, bridging at the Cao accession) disagrees with the Qocho dossier, which ends the Guiyi occupation in 911. Evidence: qocho-kingdom /ledger/3-4: occupation_start 904, occupation_end 911, counterpart guiyi-circuit; the Guiyi page gives no date for the loss. Fix: Use 911 for the loss (confidence 1, note: 'mirror of qocho-kingdom 911'), or ask the Qocho owner (ia-01) for its page; and either side should make the type agree (gain/loss here, occupation there).

Thin (for a gap-filler):

- `/ledger/9`: Lanzhou, Shanzhou, Hezhou, Minzhou, Kuozhou after 882 (confidence 1, page silent) (try https://en.wikipedia.org/wiki/Zhang_Huaishen)
- `/ledger/13`: the loss of Yizhou and Xizhou after 904 (confidence 1) (try https://en.wikipedia.org/wiki/Kingdom_of_Qocho)
- `/keyframe_review/9`: the year Suzhou left the Guiyi (page: only Gua and Sha by the end of the 10th century) (try https://en.wikipedia.org/wiki/Ganzhou_Uyghur_Kingdom)

Spot checks: `/ledger/1` confirmed: 'By 850 ... Ganzhou, Suzhou, and Yizhou'; `/ledger/2` confirmed: 'Zhang captured Xizhou' in 851; `/ledger/5` confirmed: 'In 863, Zhang Yichao led a group of 7,000 ... to capture Liang Prefecture'; `/ledger/10` confirmed: 'In 904, Zhang Chengfeng attacked Qocho and seized Yizhou' and Xizhou; `/ledger/14` year confirmed (1030 surrender, 1036 annexation); region not on page: the page has only Guazhou and Shazhou left by the end of the 10th century.

Area: No infobox area readable on the Guiyi Circuit page; keyframes 121,000-432,000 km2.

## protectorate-general-to-pacify-the-west: fix

Findings:

- `/identity/capitals/5/to` (applied by the reviewer). The seat Qiuci ran to 790 while the 787 loss of Qiuci takes the Kuqa circle out of the 787-789 keyframe, so the capital lay outside the drawn state for four years. Evidence: Same page: 'In 787 the Tibetan Empire conquered Qiuci' (and 'remain until the protectorate's demise around 790', with the monk Wukong's 789 account as the conflicting reading). Fix: Capital Qiuci to 786, with both readings in the note.

Thin (for a gap-filler):

- `/ledger/5`: Dzungaria and Semirechye in 657 (confidence 2; the page names neither) (try https://en.wikipedia.org/wiki/Ashina_Helu)
- `/keyframe_review/9`: the Anxi Tarim Basin and the Beiting Turfan-Hami/Dzungaria regions overlap by about 92,000 km2 in 702-786 (gazetteer, year 720); a 'Tarim Basin minus Turfan-Hami' correction would separate them (try https://en.wikipedia.org/wiki/Beiting_Protectorate)

Spot checks: `/ledger/8` confirmed: 670 Dafei River, Qiuci captured, seat to Suyab; `/ledger/11` confirmed: 677 Tibet captured Qiuci again; `/ledger/13` confirmed: 686 withdrawal, 687 Tibetan control; `/ledger/14` confirmed: 692 Wang Xiaojie re-established the protectorate at Qiuci; `/ledger/17` confirmed: 719 the Turgesh captured Suiye; `/ledger/19` confirmed: 787 Qiuci; 790 'last vestiges'; 792 Yutian.

Area: No infobox or area figure on the page; peak keyframe 1,807,000 km2 (Tarim, Dzungaria, Semirechye).

## beiting-protectorate: thin

Thin (for a gap-filler):

- `/ledger`: the 742 Beiting Jiedushi, the 764-790 isolation, the Uyghur-Tibetan fighting for Beiting in 789-792 and the fate of Xizhou after 790: the Beiting article is a stub (try https://en.wikipedia.org/wiki/Uyghur_Khaganate)
- `/keyframe_review/1`: the 790-790 keyframe repeats the 702 shape; harmless, but a page on the 790 siege of Beshbalik could date the fall within the year (try https://en.wikipedia.org/wiki/Sino-Tibetan_relations_during_the_Tang_dynasty)

Spot checks: `/ledger/0` confirmed: 'Wu Zetian set up the Beiting Protectorate at Ting Prefecture' in 702; `/ledger/1` confirmed: 'In 790 A.D, Tibet occupied the four towns in Anxi and Beiting in the west'.

Area: No area on any page; stub article.

## protectorate-general-to-pacify-the-north: thin

Findings:

- `/identity/start/month and /ledger/0/month` (applied by the reviewer). The found event and start were dated January 647 (the tribes' surrender); the page dates the protectorate itself to 10 April 647. Evidence: Protectorate General to Pacify the North page: 'on 9 January 647, thirteen Tiele and Uyghur tribes surrendered to the Tang' and the Yanran Protectorate 'was set up on 10 April' of that year. Fix: Month 4 in both, with the April date in the note.

Thin (for a gap-filler):

- `/ledger (682-784)`: the protectorate's later seats, which the page names and dates (Yunzhong 698 near Horinger, Shouxiang 714 near Baotou, Zhenbei 757, end 784 in the infobox), are not drawn; a Hetao rump 698-784 needs an extent (try https://en.wikipedia.org/wiki/Protectorate_General_to_Pacify_the_North)

Spot checks: `/ledger/0` confirmed with month corrected (set up 10 April 647); `/ledger/1` confirmed: 'On 5 February 663' renamed Hanhai; `/ledger/2` confirmed: 'In August 669 ... renamed the Protectorate General to Pacify the North'; `/ledger/3` confirmed: 'It controlled the Mongolian Plateau from 647 to 682'.

Area: No infobox area; the page gives the bounds (Baikal, Gobi, Khingan, Altai).

## protectorate-general-to-pacify-the-south: fail

Findings:

- `/ledger (803, missing) and /keyframe_review/0` (not applied, for the author). The dossier has no 803 loss of southern Annan to Champa, and the author's notes say 'neither page opened mentions' it; the cited protectorate page does, and the tang-dynasty and champa dossiers both draw it, so the 679-866 keyframe holds Nghe An and Ha Tinh in 803-808 against the page and two neighbours. Evidence: Protectorate General to Pacify the South page (WebFetch): 'In 803, a northern state of Champa, Huanwang, seized southern Annan.' tang-dynasty /ledger/72 (803 loss) and /ledger/73 (809 gain), champa /ledger/12-13 (803 gain, 809 loss), both with region Nghệ An + Ha Tinh and source https://en.wikipedia.org/wiki/Champa ('The Chinese barely defeated the Cham and recovered lost regions in 809'). The protectorate page does not mention the 809 recovery. Fix: Add an 803 loss (counterpart champa, region {union [admin1 Nghệ An, admin1 Hà Tĩnh]} as in the champa dossier, confidence 2, source the protectorate page with the quoted sentence) and an 809 gain (counterpart champa, confidence 2, source https://en.wikipedia.org/wiki/Champa, added to sources); split keyframe 0 into 679-802, 803-808 (minus Nghệ An and Hà Tĩnh) and 809-866; correct /notes and _notes/ea-04-x.md, which say no page mentions 803.

Thin (for a gap-filler):

- `/ledger/1`: which parts of Annan Phung Hung's rebels held in 785-791 (the contest covers the whole protectorate) (try https://en.wikipedia.org/wiki/Ph%C3%B9ng_H%C6%B0ng)

Spot checks: `/ledger/0` confirmed: 679 Annan replaced Jiaozhou, seat Songping; `/ledger/1` confirmed: 785 rising of Do Anh Han, Phung Hung, Phung An; `/ledger/2` confirmed: 'Tang forces retook Annan in 791'; `/ledger/5` confirmed: Gao Pian 'renamed the region of Annan to Jinghai Jun'; `/ledger (803)` on page but missing from the dossier: 'In 803, a northern state of Champa, Huanwang, seized southern Annan'.

Area: No infobox area; the shape (Tonkin, Thanh Hoa, Nghe An, Ha Tinh) is about 2.2 times Cliopatria's Ngô 947 shape (62,155 km2), which the keyframe note calls probably over-wide.

## jinghai-circuit: pass

Thin (for a gap-filler):

- `/ledger/3`: the capture of Khúc Thừa Mỹ: 930 (Bạch Đằng page, used) versus autumn 923 (Dương Đình Nghệ page, which says Chinese sources give 930) (try https://en.wikipedia.org/wiki/Kh%C3%BAc_Th%E1%BB%ABa_M%E1%BB%B9)

Spot checks: `/ledger/1` confirmed: 'In 880, the army in Annan mutinied, taking the city of Đại La'; `/ledger/3` confirmed: October 930 attack on the Jinghai circuit; `/ledger/4` confirmed: 931, took the fortress and proclaimed himself governor; `/ledger/5` confirmed: 'In the spring, March of 937' murdered by Kiều Công Tiễn; `/ledger/6` confirmed: spring 939 king, capital Co Loa.

Area: No page for the circuit; the note acknowledges the 2.2x gap to Cliopatria's Ngô 947 shape (62,155 km2) and leaves the shape unverified.

## li-gui-s-liang: fix

Findings:

- `/ledger/1/year` (applied by the reviewer). The gain of Zhangye, Dunhuang, Xiping and Fuhan was dated 618; the page puts it right after the fall 617 rising, and the keyframe already draws the land from 617. Evidence: Li Gui (warlord) page: 'In fall 617' he rose (infobox 14 August 617) and 'Li Gui soon took four other commanderies'; the 618 entries on the page are the imperial title (winter 618). Fix: Year 617, month 8 as a sort key, note rewritten.

Spot checks: `/ledger/0` confirmed: fall 617, infobox 14 August 617; `/ledger/1` mis-dated (618 for 617), fixed; `/ledger/2` confirmed: emperor in winter 618, Anle era from 26 November 618; `/ledger/3` confirmed: 'In June 619', infobox 29 June 619.

Area: No area on the page.

## liu-heita-s-handong: fix

Findings:

- `/keyframe_review/0` (applied by the reviewer). The one keyframe drew all of Hebei from 621, while the ledger founds the state in 621 on a Handan circle and gains Hebei only in 622. Evidence: Liu Heita page: 'In fall 621, they officially rose and captured Zhangnan'; the former Xia territory was recovered 'around the new year 622'. Fix: Split into liu-heita-s-handong_621 (621, the found circle) and liu-heita-s-handong_622 (622-623, Hebei).

Spot checks: `/ledger/0` confirmed: fall 621, Zhangnan; `/ledger/1` confirmed: 'around the new year 622'; `/ledger/4` confirmed: 'In summer 622, Liu, with Turkish reinforcements' returned; `/ledger/5` confirmed: spring 623, Rao Prefecture, Zhuge Dewei.

Area: No area on the page.

## fu-gongshi-s-song: pass

Spot checks: `/ledger/0` confirmed: fall 623, Emperor of Song at Danyang; `/ledger/1` confirmed: Zhang Shan'an submitted in fall 623, 'northern Jiangxi and eastern Hubei'; `/ledger/2` confirmed: 'In winter 623, Zhang was captured by the Tang general Li Daliang'; `/ledger/3` confirmed: 624, Li Xiaogong, captured at Wukang.

Area: No area on the page.

## xu-yuanlang-s-lu: fix

Findings:

- `/ledger/1 (inserted)` (applied by the reviewer). The 621 gain from the Tang had no preceding loss: the dossier holds the land from 617 and then 'gains' it from the Tang in 621. Evidence: Xu Yuanlang page: after Dou Jiande fell, Xu 'submitted to Tang', 'was made the commandant of Yan Prefecture' and again Duke of Lu (621), then joined Liu Heita's revolt later in 621. Fix: Inserted a 621 loss (counterpart tang-dynasty, same three circles, confidence 2, the page's sentence) before the gain; the old /ledger/1-5 are now /ledger/2-6.

Spot checks: `/ledger/0` confirmed: 'in or before spring 617', Dongping, Langye; `/ledger/2` confirmed: captured Sheng Yanshi, 'eight prefectures', late 621; `/ledger/3` confirmed: winter 621 Prince of Lu; `/ledger/6` confirmed: siege of Yan spring 623, killed 26 March 623 (infobox).

Area: No area on the page.

## dingnan-circuit: fix

Findings:

- `/keyframe_review/1/from` (applied by the reviewer). The second keyframe (id dingnan-circuit_985) started in 982 and drew Yinzhou for 982-984, three years before the 985 gain that brings it. Evidence: Western Xia page: Li Jipeng surrendered Dingnan in 982; 'In 984, the Song attacked his camp'; he captured Yinzhou the following year, 985. Fix: from 985 (nothing drawn 982-984), note updated.
- `/identity/capitals/0/to` (applied by the reviewer). Xiazhou stayed the capital to 990 although the 982 loss gives the whole circle, Xiazhou included, to the Song and the 985-990 shape is the Yinzhou circle about 90 km away. Evidence: Western Xia page: 982 surrender of Dingnan Jiedushi to the Song. Fix: Capital to 981, with the reason in the note.

Thin (for a gap-filler):

- `/keyframe_review/0`: the extent of the four prefectures 881-981 (a 120 km circle); Xia Prefecture's 933 siege by the Later Tang (try https://en.wikipedia.org/wiki/Tuoba_Sigong)

Spot checks: `/ledger/0` confirmed: 'was granted in 881 control of Xiazhou, Youzhou, Suizhou, Yinzhou', called Dingnan Jiedushi; `/ledger/1` confirmed: Li Jipeng 'fled to the Song court and surrendered control of Dingnan Jiedushi' (982); `/ledger/2` confirmed: 984 Song attack, Yinzhou captured the following year; `/ledger/3` confirmed: 990 'King of the Xia State' from the Liao.

Area: The Western Xia infobox area (1,000,000 km2, 1100; the lead says 800,000 at its peak) is for the later state; the keyframe note says so.

## zhao-five-dynasties-period: thin

Findings:

- `/keyframe_review/0/correction` (not applied, for the author). The Shijiazhuang 80 km circle leaves out Shen and Ji prefectures, which the cited page names as the state's, and the 910 Later Liang seizure of Shen and Ji is not in the ledger. Evidence: Wang Rong (warlord) page: prefectures Zhen and Zhao (Shijiazhuang) and 'Shen and Ji, in modern Hengshui, which Later Liang forces seized in 910'; infobox 'Shijiazhuang/Hengshui region'. Gazetteer: Hengshui 50 km lies wholly outside the drawn circle. Fix: Union the correction with {place Hengshui, km 50} (also in /ledger/0, /ledger/5 regions and the identity land, coordinating with former-jin /ledger/7), and add the 910 loss of the Hengshui circle to later-liang-dynasty with its return (Boxiang, 911) if a page dates it; not applied because it changes another dossier's counterpart region.

Thin (for a gap-filler):

- `/keyframe_review/0`: 763-883: no events (Li Baozhen, Li Weiyue, Wang Wujun, Wang Tingcou; the 782 split of Yiwu from Chengde; the 781-782 and 821-822 risings) (try https://en.wikipedia.org/wiki/Wang_Wujun)
- `/ledger (910-911)`: Later Liang's 910 seizure of Shen and Ji and the 911 Battle of Boxiang (try https://en.wikipedia.org/wiki/Emperor_Zhuangzong_of_Later_Tang)

Spot checks: `/ledger/0` confirmed: 'Li Baozhen kept control of the Chengde Circuit'; `/ledger/1` confirmed: 883, 'only six-years-old'; `/ledger/2` confirmed: renamed Wushun; Prince of Zhao (907); `/ledger/3` confirmed: 910 Wushun and Yiwu 'renounced their loyalty to Later Liang'; `/ledger/5` confirmed: 'by fall 922 Zhen Prefecture had fallen'.

Area: No area on the page; the infobox says 'Shijiazhuang/Hengshui region', wider than the drawn circle.

## yiwu-five-dynasties: thin

Thin (for a gap-filler):

- `/identity/start`: 900-910: Wang Chuzhi governed Yiwu from 900 (de facto independent like the Chengde circuit, which this batch counts from 763); the dossier starts at the de jure break of 910 (try https://en.wikipedia.org/wiki/Wang_Chuzhi)

Spot checks: `/ledger/0` confirmed: 'became independent de jure as well in 910'; `/ledger/1` confirmed: 'overthrown in 921 by his adoptive son Wang Du'; `/ledger/2` confirmed: 'in early 929, Wang Du's officer Ma Rangneng opened the city gates'; Wang Du's suicide.

Area: No area; 'controlled Yiwu around modern Baoding'.

## qingyuan-circuit: pass

Thin (for a gap-filler):

- `/ledger/5`: 977 (text) versus 978 (infobox) for Chen Hongjin's surrender; confidence 2 already (try https://en.wikipedia.org/wiki/Chen_Hongjin)

Spot checks: `/ledger/1` confirmed: autumn 946, 'expelled Lin from Zhang'; `/ledger/2` confirmed: 949 Qingyuan Circuit with its headquarters at Quan; `/ledger/3` confirmed: summer 963; `/ledger/4` confirmed: 964 renamed Pinghai; `/ledger/5` confirmed as stated: 977 in the text, infobox 963-978.

Area: No area; two 60 km circles.

## lulong-circuit: fail

Findings:

- `/keyframe_review/0 with /ledger/2 and /ledger/3` (not applied, for the author). The single keyframe (Cliopatria's Yan Kingdom 911 shape, 763-911) never carries the two land events of the ledger: the 900 loss of Ying, Mo and Jing (the 80 km circle at 116.0 E 38.2 N, about 28,000 km2) lies wholly outside the drawn shape, so the dossier loses land it never drew, and the 898 gain of Cang Prefecture (about 28,000 km2, only about 3,000 inside) is never drawn. Evidence: Liu Rengong page: in 898 Liu Shouwen took Yichang's capital Cang Prefecture; in winter 900 'Zhang Cunjing captured Lulong's Ying and Mo Prefectures and Yichang's Jing Prefecture'; Cang 'fell in 910, so Liu Shouguang took Yichang under his control as well'. Gazetteer: Yan Kingdom 911 bbox 114.98-119.65 E, 38.68-41.45 N; overlap with the Hejian circle 0 km2, with Cangzhou 80 km about 3,000 km2. Fix: Draw Ying and Mo as Lulong's in the keyframes before 900 (e.g. 763-897: Yan Kingdom 911 plus the Hejian circle, if that is the reading for the whole span; say so), add Cangzhou from 898 (Liu Shouwen's Yichang, or else record 898 as a vassal/ally event, not a gain), take the Hejian circle out from 900, and settle Yichang 909-910 (Liu Shouwen captured at Jisu 909; Cang falls to Liu Shouguang 910); each change a new keyframe.

Thin (for a gap-filler):

- `/keyframe_review/0`: 763-893: no events (Li Huaixian killed 768, Zhu Xicai, Zhu Ci, Liu Ji, Zhang Zhongwu, Li Kuangwei); no Lulong Circuit article (try https://en.wikipedia.org/wiki/Zhu_Ci)

Spot checks: `/ledger/1` confirmed: spring 895 Li Keyong at You Prefecture; summer 895 Liu military governor; `/ledger/2` confirmed: 898 Cang taken from Lu Yanwei; `/ledger/3` confirmed: winter 900 Ying, Mo (Lulong) and Jing (Yichang); `/ledger/4` confirmed: 'In 911, he claimed the title of Emperor of Yan'.

Area: No page for the circuit; the Yan Kingdom 911 shape (about 89,000 km2) stands for 148 years.

## weibo-circuit: thin

Thin (for a gap-filler):

- `/keyframe_review/0`: the circuit's extent: the 80 km Daming circle (about 27,000 km2) leaves out Bei Prefecture (Qinghe, about 115.67 E 37.06 N), which the Luo Shaowei page names; the Weibo page says it 'controlled the southern Hebei and northern Shandong regions' and Luo Shaowei 'six prefectures and 43 counties' (suggest adding Liaocheng 50 km and a Qinghe coordinate circle) (try https://en.wikipedia.org/wiki/Luo_Shaowei)
- `/ledger (763-888)`: Tian Chengsi's successors, the 781-782 rising, Shi Xiancheng 821-822, Li Tongjie's 827 rising (try https://en.wikipedia.org/wiki/Tian_Chengsi)

Spot checks: `/ledger/0` confirmed: 'he took control of Weibo in 763 and rebelled against the court twice'; `/ledger/1` confirmed: 888 mutiny, Luo Hongxin; `/ledger/3` confirmed: 904 renamed Tianxiong, Prince of Ye; `/ledger/4` confirmed: died 910, Luo Zhouhan appointed; An Lushan rebellion page: 'integrated with the Later Liang state in 910'.

Area: No area; the page's description is wider than the circle (noted under thin).

## xiliangfu: pass

Thin (for a gap-filler):

- `/ledger/7`: 1016 (Xiliangfu page) versus 1032 (Western Xia page: 'In 1032, he annexed the Tibetan confederation of Xiliangfu'): who held Liangzhou 1016-1032 (try https://en.wikipedia.org/wiki/Ganzhou_Uyghur_Kingdom)

Spot checks: `/ledger/0` confirmed: established 906, capital Liangzhou; `/ledger/1` confirmed: 'In 1001, Panluozhi came to power'; `/ledger/2` confirmed: 1003 Li Jiqian occupied Liangzhou and 'failed to hold the city'; `/ledger/5` confirmed: Tanguts captured Liangzhou in 1015; `/ledger/6` confirmed: 1016 the Ganzhou Uyghur Kingdom ousted them.

Area: No infobox area.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| yan-an-lushan 755 gain (tang-dynasty) | tang-dynasty 755 loss | matched | Tang counterpart string 'Yan (An Lushan)' should become slug yan-an-lushan (ea-04 Tang owner). |
| yan-an-lushan 756 gain (tang-dynasty) | tang-dynasty 756 loss | matched | Luoyang (January) and Guanzhong (July): Tang /ledger/56-57. |
| yan-an-lushan 757 loss (tang-dynasty) | tang-dynasty 757 gain | matched | Chang'an and Luoyang, Tang /ledger/58. |
| yan-an-lushan 757 loss (tang-dynasty) | - | missing | Hebei minus Ye to the Tang on Shi Siming's submission: no Tang gain (ea-04 tang-dynasty owner); flagged by the author. |
| yan-an-lushan 759 gain (tang-dynasty) | tang-dynasty 759 loss | matched | Bian and Luoyang, Tang /ledger/59 (counterpart string 'Yan (Shi Siming)'). |
| yan-an-lushan 759 gain (tang-dynasty) | - | missing | Fanyang and northern Hebei back to Shi Siming: no Tang loss; flagged by the author. |
| yan-an-lushan 762 loss (tang-dynasty) | tang-dynasty 762 gain | matched | Luoyang, Tang /ledger/60; the confidence-1 Bian loss has no mirror (Tang text names Luoyang only). |
| yan-an-lushan 763 dissolve (tang-dynasty) | tang-dynasty 763 gain | matched | Hebei to the Tang /ledger/62; lulong, weibo and zhao found from yan-an-lushan in 763 (successor lists agree). |
| qi-huang-chao 881 gain (tang-dynasty) | tang-dynasty 881 loss | matched | Tang /ledger/83 (string 'Qi (Huang Chao)'). |
| qi-huang-chao 882 loss (tang-dynasty) | - | missing | Tong and Hua back to the Tang in fall/winter 882: no Tang gain; flagged by the author. |
| qi-huang-chao 883 loss (tang-dynasty) | tang-dynasty 883 gain | matched | Tang /ledger/84. |
| guiyi-circuit 848 found (tibetans) | tibetans 848 loss | matched | tibetans counterpart string 'Guiyi Circuit (Zhang Yichao)' should become guiyi-circuit; tang-dynasty /ledger/74 also gains the same land in 848, from tibetan-empire (which ends 842): double owner. |
| guiyi-circuit 850 gain (tibetans) | tibetans 850 loss | matched | tang-dynasty /ledger/75 gains the same land: double owner (author flagged; orchestrator to pick the owner, Tang as vassal tint from 851). |
| guiyi-circuit 851 gain (tibetans) | - | missing | Xizhou 851: no tibetans loss; tang-dynasty /ledger/76 gains it instead. |
| guiyi-circuit 861 gain (tibetans) | tibetans 861 loss | mismatch | tibetans /ledger/4 gives Liangzhou (Wuwei) in 861; guiyi gains the eastern prefectures in 861 and Liangzhou in 863 (Zhang Yichao page: 863). The tibetans owner (ea-04) should split its 861 loss and date Liangzhou 863. |
| guiyi-circuit 866 loss (qocho-kingdom) | qocho-kingdom 866 gain | matched |  |
| guiyi-circuit 876 loss (qocho-kingdom) | qocho-kingdom 876 gain | matched |  |
| guiyi-circuit 882 loss (nobody) | ganzhou-kingdom 894 found | mismatch | ganzhou-kingdom founds in 894 from guiyi-circuit; the Guiyi page has Ganzhou slip away in 881-882 (author flagged; ia-01 owner). |
| guiyi-circuit 904 gain (qocho-kingdom) | qocho-kingdom 904 occupation_start | mismatch | Type differs (gain here, occupation there). |
| guiyi-circuit 914 loss (qocho-kingdom) | qocho-kingdom 911 occupation_end | mismatch | Three years apart; guiyi 914 is confidence 1 bridging (see fixes). |
| guiyi-circuit 1036 dissolve (western-xia) | western-xia 1036 gain | matched |  |
| protectorate-general-to-pacify-the-west 640 found (kingdom-of-gaochang) | kingdom-of-gaochang 640 dissolve | exception | Mirror names tang-dynasty: the protectorate is a Tang internal unit (type colony); the orchestrator decides the owner. Same for every Anxi, Beiting and northern-protectorate row below marked exception. |
| protectorate-general-to-pacify-the-west 648 gain (Karasahr (Tarim oasis kingdom)) | - | exception | No dossier; listed in counterparts_needing_dossiers (ia-01/ea-02 Tarim states). Tang dossier dates Karasahr 644. |
| protectorate-general-to-pacify-the-west 648 gain (kingdom-of-kucha) | kingdom-of-kucha 648 dissolve | exception | Mirror counterpart tang-dynasty. |
| protectorate-general-to-pacify-the-west 650 gain (western-gokturks) | western-gokturks 648 loss | mismatch | western-gokturks loses the Tarim to tang-dynasty in 648; Anxi gains it in 650 ("By 650 the entire Western Region had submitted") on top of the 648 Kucha/Karasahr gains: two years and the counterpart differ. |
| protectorate-general-to-pacify-the-west 657 gain (western-gokturks) | western-gokturks 657 loss | exception | Mirror counterpart tang-dynasty. |
| protectorate-general-to-pacify-the-west 659 vassal_start (Sogdian and Tokharistan principalities) | - | exception | No dossier; listed by the author. |
| protectorate-general-to-pacify-the-west 670 loss (tibetan-empire) | tibetan-empire 670 gain | exception | tibetan-empire has the event with counterpart tang-dynasty (same year and land). |
| protectorate-general-to-pacify-the-west 673 gain (tibetan-empire) | tibetan-empire 673 loss | exception | tibetan-empire has the event with counterpart tang-dynasty (same year and land). |
| protectorate-general-to-pacify-the-west 677 loss (tibetan-empire) | tibetan-empire 677 gain | exception | tibetan-empire has the event with counterpart tang-dynasty (same year and land). |
| protectorate-general-to-pacify-the-west 679 gain (tibetan-empire) | tibetan-empire 679 loss | exception | tibetan-empire has the event with counterpart tang-dynasty (same year and land). |
| protectorate-general-to-pacify-the-west 687 loss (tibetan-empire) | tibetan-empire 687 gain | exception | tibetan-empire has the event with counterpart tang-dynasty (same year and land). |
| protectorate-general-to-pacify-the-west 692 gain (tibetan-empire) | tibetan-empire 692 loss | exception | tibetan-empire has the event with counterpart tang-dynasty (same year and land). |
| protectorate-general-to-pacify-the-west 787 loss (tibetan-empire) | tibetan-empire 787 gain | exception | tibetan-empire has the event with counterpart tang-dynasty (same year and land). |
| protectorate-general-to-pacify-the-west 790 loss (tibetan-empire) | tibetan-empire 790 gain | exception | tibetan-empire has the event with counterpart tang-dynasty (same year and land). |
| protectorate-general-to-pacify-the-west 792 dissolve (tibetan-empire) | tibetan-empire 792 gain | exception | tibetan-empire has the event with counterpart tang-dynasty (same year and land). |
| protectorate-general-to-pacify-the-west 702 split (beiting-protectorate) | beiting-protectorate 702 found | matched |  |
| protectorate-general-to-pacify-the-west 719 loss (turgesh) | - | missing | turgesh has no 719 gain of Suyab/Semirechye (ia-01 owner). |
| beiting-protectorate 790 dissolve (tibetan-empire) | tibetan-empire 790 gain | exception | tibetan-empire /ledger/37 gains Beshbalik from tang-dynasty. |
| protectorate-general-to-pacify-the-north 647 found (xueyantuo) | xueyantuo 646 dissolve | exception | xueyantuo dissolves to tang-dynasty in August 646. |
| protectorate-general-to-pacify-the-north 682 dissolve (second-turkic-khaganate) | second-turkic-khaganate 682 found | exception | second-turkic-khaganate founds from tang-dynasty. |
| protectorate-general-to-pacify-the-south 803 loss (missing) (champa) | champa 803 gain | missing | champa /ledger/12 and tang-dynasty /ledger/72 have the 803 seizure of Nghe An; this dossier lacks it (see fixes). |
| protectorate-general-to-pacify-the-south 863 occupation_start (nanzhao) | nanzhao 863 occupation_start | exception | nanzhao occupies with counterpart tang-dynasty; tang-dynasty uses loss/gain 863/866 where nanzhao and this dossier use occupation events. |
| protectorate-general-to-pacify-the-south 866 dissolve (jinghai-circuit) | jinghai-circuit 866 found | matched |  |
| jinghai-circuit 866 found (protectorate-general-to-pacify-the-south) | tang-dynasty 866 gain | mismatch | tang-dynasty gains Annan from nanzhao in 866 and never loses it to the Jinghai circuit (880 mutiny or 906 Khúc recognition), so Tang and Jinghai (type state) both draw Annan 866-907; ea-04 Tang owner or the orchestrator to settle. |
| jinghai-circuit 930 occupation_start (southern-han) | southern-han 930 occupation_start | matched | southern-han counterpart string 'Jinghai circuit' should become slug jinghai-circuit. |
| jinghai-circuit 939 dissolve (ngo-dynasty) | ngo-dynasty 939 found | mismatch | ngo-dynasty founds from southern-han (se-01 owner); its predecessor should be jinghai-circuit. |
| li-gui-s-liang 617 found (sui-dynasty) | - | missing | sui-dynasty has no 617 loss to Li Gui (ea-03 owner). |
| li-gui-s-liang 617 gain (sui-dynasty) | - | missing | Hexi commanderies (was 618, now 617): no sui-dynasty loss. |
| li-gui-s-liang 619 dissolve (tang-dynasty) | tang-dynasty 619 gain | matched | Tang string 'Li Gui (Liang of Hexi)' should become li-gui-s-liang. |
| liu-heita-s-handong 621 found (tang-dynasty) | tang-dynasty 622 loss | matched | Tang /ledger/11 (string 'Liu Heita (Handong)'). |
| liu-heita-s-handong 622 loss (tang-dynasty) | - | missing | Li Shimin's 622 recovery and the summer 622 re-loss are not in the Tang ledger; flagged by the author. |
| liu-heita-s-handong 623 dissolve (tang-dynasty) | tang-dynasty 623 gain | matched |  |
| fu-gongshi-s-song 623 found (tang-dynasty) | - | missing | No Tang 623 loss (Tang has only the 624 gain); flagged by the author. |
| fu-gongshi-s-song 623 vassal_start (Zhang Shan'an) | - | exception | Name only; added to counterparts_needing_dossiers here (the author listed it in the notes only). |
| fu-gongshi-s-song 624 dissolve (tang-dynasty) | tang-dynasty 624 gain | matched | Tang string 'Fu Gongshi (Song)'. |
| xu-yuanlang-s-lu 617 found (sui-dynasty) | - | missing | No sui-dynasty loss (ea-03). |
| xu-yuanlang-s-lu 621 loss/gain (tang-dynasty) | - | missing | No Tang gain/loss for the 621 submission and rising (ea-04 Tang owner). |
| xu-yuanlang-s-lu 623 dissolve (tang-dynasty) | - | missing | No Tang 623 gain. |
| dingnan-circuit 881 found (tang-dynasty) | - | missing | No Tang loss (Tang shape covers Xiazhou to 907); flagged by the author. |
| dingnan-circuit 982 loss (northern-song) | - | missing | northern-song has no 982 gain of the Dingnan prefectures (ea-05 owner). |
| dingnan-circuit 985 gain (northern-song) | - | missing | northern-song has no 985 loss of Yinzhou. |
| dingnan-circuit 990 dissolve (western-xia) | western-xia 990 found | mismatch | western-xia founds from northern-song (ea-05); its predecessor should be dingnan-circuit. |
| zhao-five-dynasties-period 922 dissolve (former-jin) | former-jin 922 gain | matched |  |
| yiwu-five-dynasties 910 found (later-liang-dynasty) | - | missing | later-liang-dynasty has no 910 loss of Yiwu (ea-04 owner). |
| yiwu-five-dynasties 929 dissolve (later-tang) | - | missing | later-tang has no 929 gain of Dingzhou nor the Wang Du war with yiwu-five-dynasties; flagged by the author. |
| qingyuan-circuit 946 found (min) | min 945 dissolve | mismatch | min ends in October 945, dissolving all Fujian to southern-tang; Qingyuan founds from min in 946. Either Qingyuan's counterpart becomes southern-tang (Quan under the Southern Tang's nominal rule before Liu Congxiao) with a southern-tang loss or vassal pair, or min ends Quan and Zhang separately. |
| qingyuan-circuit 946 gain (Lin Zanyao) | - | exception | Name only; added to counterparts_needing_dossiers here. |
| qingyuan-circuit 978 dissolve (northern-song) | - | missing | northern-song has a 978 gain from wuyue only; no gain of Quan and Zhang (ea-05). southern-tang draws Quan and Zhang inside its own shape (about 19,000 km2 overlap in 960) with no vassal pair. |
| lulong-circuit 898 gain (Lu Yanwei (Yichang)) | - | exception | yichang-circuit listed by the author. |
| lulong-circuit 900 loss (Zhu Quanzhong (Xuanwu)) | - | exception | xuanwu-circuit listed by the author. |
| lulong-circuit 911 dissolve (yan-kingdom) | yan-kingdom 911 found | mismatch | yan-kingdom founds from tang-dynasty (ea-04); its predecessor should be lulong-circuit. |
| weibo-circuit 910 dissolve (later-liang-dynasty) | - | missing | later-liang-dynasty has no 910 gain of Weibo/Tianxiong yet loses Tianxiong to former-jin in 915 (/ledger/4): a loss with no prior gain (ea-04 owner). |
| xiliangfu 1003 occupation_start (western-xia) | - | missing | western-xia has no 1003-1004 or 1015-1016 occupation of Liangzhou (ea-05). |
| xiliangfu 1016 dissolve (ganzhou-kingdom) | - | missing | ganzhou-kingdom has only a 1009-1010 contest with xiliangfu, no 1016 gain (ia-01). |
| xiliangfu 1016 dissolve (ganzhou-kingdom) | western-xia 1032 gain | mismatch | western-xia /ledger/2 gains Liangzhou from xiliangfu in 1032, sixteen years after the Xiliangfu dossier ends (pages disagree; author flagged). |

## Gazetteer names needed

Jiuquan (Suzhou) (place, guiyi-circuit), Guazhou (Gansu) (place, guiyi-circuit), Yulin (Shaanxi) (place, dingnan-circuit), Mizhi (Yinzhou) (place, dingnan-circuit), Daming (Weizhou) (place, weibo-circuit, yan-an-lushan), Qinghe (Beizhou, Hebei) (place, weibo-circuit), Hejian (Yingzhou) (place, lulong-circuit), Tongguan (place, qi-huang-chao), Huayin (place, qi-huang-chao), Fanyang / Youzhou (alias of Beijing) (place, yan-an-lushan, lulong-circuit), Hedong (Shanxi) (region, yan-an-lushan), Dongping / Langye / Yanzhou (aliases of Heze, Linyi, Jining) (place, xu-yuanlang-s-lu).

## Counterparts needing dossiers

Wuping Circuit (wuping-circuit, 952-963), Guge (guge, 912-1630), Maryul (Ladakh) (maryul, 930-1460), Karasahr (Tarim oasis kingdom) (karasahr, 644-648), Sogdian and Tokharistan principalities (sogdian-and-tokharistan-principalities, 659-751), Phung Hung's rebels (Annan) (phung-hung-s-rebels, 785-791), Lu Yanwei's Yichang circuit (yichang-circuit, 897-910), Zhu Quanzhong's Xuanwu circuit (xuanwu-circuit, 880-907), Tsongkha (Qingtang) (tsongkha, 1016-1104), Zhang Shan'an (northern Jiangxi, eastern Hubei) (zhang-shan-an, 623-623), Lin Zanyao (Zhang Prefecture rebel) (lin-zanyao, 946-946).

## Problems

- WebFetch returns a small model's summary, not the page text. On the Shi Siming page the summaries put 'summer 759' (Wu Cheng'en's plot) before '7 April 759' and the Great Holy Prince claim in 'spring 760' with an Old Book of Tang date of 3 February (which is 759), so the page's chronology of his 758-759 re-rebellion could not be checked; yan-an-lushan /ledger/10 (759, confidence 2) was left as written.
- No page opened in this batch has an infobox area for the state itself (only the Western Xia, for c. 1100), so every area_check has infobox_km2 null; drawn_km2 is the gazetteer resolution of the largest or last keyframe.
- Reviewer edits made in place (each re-validated with --resolve, 0 errors 0 warnings, and read back): yan-an-lushan, qi-huang-chao, protectorate-general-to-pacify-the-west, protectorate-general-to-pacify-the-north, li-gui-s-liang, liu-heita-s-handong, xu-yuanlang-s-lu (ledger indices from 1 on shifted by one), dingnan-circuit.
- Verdicts used here: fix = every dossier-local finding applied by the reviewer (remaining items are cross-dossier, in cross_checks); thin = valid, with gaps for a gap-filler, and any unapplied item is non-blocking; fail = an unapplied blocking finding (land drawn against the cited page or against the dossier's own ledger).
- Design question for the orchestrator, not a fault of any one dossier: the four Tang protectorate dossiers, guiyi-circuit 848-861 and jinghai-circuit 866-907 draw land the tang-dynasty dossier also gains, and most neighbours' mirrors name tang-dynasty, not the protectorate; these rows are marked exception in cross_checks.
