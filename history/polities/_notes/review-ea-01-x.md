# Review of batch ea-01-x (Shang to Warring States, additions)

Reviewer: adversarial reviewer, 2026-10-19. Machine copy: history/notes/phase-b/reviews/ea-01-x.json.

## Summary

- 38 dossiers, all valid (0 errors, 0 resolve warnings). 146 spot checks on 35 Wikipedia pages: no event was fabricated; every note's quotation was found on its page.
- Verdicts: 27 pass, 7 thin (by design within the page budget), 3 fix (applied by the reviewer: confidence 3 -> 2), 1 fail (lai: shape).
- Applied in place and re-validated: wu-geng /ledger/1, xing /ledger/1, xia-dynasty /ledger/2 (confidence 2, reviewer sentence appended to each note).
- Vassalage: the author put it only on the suzerain side, as the schema says (zeng under Chu from c. 632, east-zhou under Qin from 307, yelang under Nanyue 183-111, yiqu under Qin 327). Not a fault here; the chu and qin dossiers lack all of them.
- No infobox in the batch gives an area and no dossier has a Cliopatria shape: every area check is null, and the keyframe notes say the discs are stand-ins.

## Verdicts

### deng: pass
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/identity/predecessors/0/land` confirmed

### huang: pass
- thin `/ledger/0`: founding year: 704 is the first dated mention (confidence 1) (try https://en.wikipedia.org/wiki/List_of_Zhou_dynasty_states)
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/wars/0` confirmed

### shen: pass
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/keyframe_review/0/correction` confirmed

### tan: pass
- thin `/ledger/2`: the page has a 3-year Qi occupation (684-681) and then a Qi vassal; the dossier ends at 684 (author flagged). A gap-filler may model occupation 684-681 on the qi side and a qi vassal_start for the remnant. (try https://en.wikipedia.org/wiki/Tan_(state))
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/keyframe_review/0/correction` confirmed

### lai: fail
- FIX (author) `/keyframe_review/0/correction (and the same region in /ledger/0-2 and /identity/successors/0/land)`: The {place: Weifang, km: 80} member of the Lai union reaches 9 km past Linzi, Qi's capital (Weifang-Linzi 71 km), and deep into the qi dossier's own founding disc (Zibo 60 km), so Lai is drawn over Qi's capital for 1046-567. Evidence: Lai page: 'Lai is on the tip of the Shandong Peninsula bordering Qi'; capitals Changle and Linqu lie only 48 and about 37 km from Linzi. Gazetteer: Weifang 119.10, 36.72; Linzi 118.31, 36.81. Fix: Keep the Longkou and Yantai discs and replace the Weifang 80 km disc by a disc that stops short of Linzi, e.g. {lon: 118.95, lat: 36.75, km: 45} (Changle/Weifang), or wrap the union as {minus: [union, {place: Zibo, km: 35}]}; use the same region in the ledger and successors and tell ea-01-b (qi) to carve Lai out of its -750 shape until 567.
- thin `/ledger/0`: founding (Established ?); 1046 is a bridge (try https://en.wikipedia.org/wiki/List_of_Zhou_dynasty_states)
- spot checks: `/ledger/1` confirmed; `/ledger/2` confirmed; `/ledger/0` confirmed; `/keyframe_review/0/correction` confirmed

### quanrong: pass
- thin `/ledger/4`: end of the Quanrong hold (750 is the last date a page shows Rong holding land; confidence 1) (try https://en.wikipedia.org/wiki/Xirong)
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/ledger/3` confirmed

### xianyun: thin
- thin `/ledger/0`: start is a bridge (first dated attack); confidence 1 (try https://en.wikipedia.org/wiki/King_Xuan_of_Zhou)
- thin `/ledger/2`: end of the Zhou campaigns; confidence 1 (try https://en.wikipedia.org/wiki/King_Xuan_of_Zhou)
- thin `/ledger/3`: end of the people: 771 is a bridge; the page says Western Zhou fell to pressure from the Xianyun or the Quanrong (try https://en.wikipedia.org/wiki/Xirong)
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/keyframe_review/0/correction` confirmed

### western-guo: pass
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/keyframe_review/0/correction` confirmed

### yu: pass
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed

### zeng: thin
- thin `/ledger/0`: founding year: a bound (1045), confidence 1 (try https://en.wikipedia.org/wiki/Zeng_(state))
- thin `/ledger/1`: year of the Chu annexation: -401 is the last year of the 5th century; the Marquis Yi of Zeng tomb (433 BC) shows Zeng still a polity then (try https://en.wikipedia.org/wiki/Marquis_Yi_of_Zeng)
- thin `/ledger/2`: same bound as /ledger/1 (try https://en.wikipedia.org/wiki/Chu_(state))
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/notes` confirmed

### qi-henan: thin
- thin `/keyframe_review/0`: the move to Shandong is undated, so the single Kaifeng shape for 1046-445 is unexplained late in the life (author flagged); also the dossier's own capital (Qi County, 114.78, 34.55) lies 2 km outside the Kaifeng 50 km disc: recentre the disc on Qi County (and tell ea-01-a, whose 445 gain uses the same disc) (try https://en.wikipedia.org/wiki/List_of_Zhou_dynasty_states)
- thin `/ledger/0`: founding: bridge at 1046 (try https://en.wikipedia.org/wiki/Qi_(Henan))
- spot checks: `/ledger/1` confirmed; `/ledger/2` confirmed; `/ledger/0` confirmed; `/keyframe_review/0/correction` confirmed

### ji-beijing: thin
- thin `/ledger/1`: year Yan absorbed Ji (c. 7th century; 650 shared with the yan dossier) (try https://en.wikipedia.org/wiki/Yan_(state))
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/keyframe_review/0/correction` confirmed

### yelang: pass
- thin `/ledger/0`: founding: 281 is the first dated mention (try https://en.wikipedia.org/wiki/Zhuang_Qiao)
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/notes` confirmed

### xi: pass
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/wars/0` confirmed

### zhongli: thin
- thin `/ledger/0`: founding: bound (try https://en.wikipedia.org/wiki/Zhongli_(state))
- thin `/ledger/1`: year of the Chu conquest (bound 538) (try https://en.wikipedia.org/wiki/King_Liao_of_Wu)
- thin `/ledger/2`: same bound (try https://en.wikipedia.org/wiki/Chu_(state))
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/keyframe_review/0/correction` confirmed

### pi: thin
- thin `/ledger/0`: founding: bridge at 1046 (try https://en.wikipedia.org/wiki/Pi_(state))
- thin `/ledger/1`: year of the Chu annexation (bound after 418) (try https://en.wikipedia.org/wiki/List_of_Zhou_dynasty_states)
- thin `/ledger/2`: same bound (try https://en.wikipedia.org/wiki/Chu_(state))
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/keyframe_review/0/correction` confirmed

### luo: pass
- thin `/ledger/0`: founding: bridge; site Yicheng (infobox) vs Luoshan, Henan (text) unresolved (author flagged) (try https://en.wikipedia.org/wiki/Luo_(state))
- spot checks: `/ledger/1` confirmed; `/ledger/2` confirmed; `/ledger/0` confirmed; `/ledger/1` confirmed

### east-zhou: pass
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/keyframe_review/0/correction` confirmed

### jiang-zhengyang: pass
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed

### jiang-gushi: pass
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed

### liu-lu-an: pass
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed

### yong-hubei: pass
- thin `/ledger/0`: start: list gives '?'; 1046 bridge (try https://en.wikipedia.org/wiki/List_of_Zhou_dynasty_states)
- thin `/wars/0`: the list names Chu, Qin and Ba as conquerors; neither ba nor qin carries a 611 event (try https://en.wikipedia.org/wiki/Ba_(state))
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed

### eastern-guo: pass
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/keyframe_review/0/correction` confirmed

### ji-shandong: pass
- thin `/ledger/0`: start: the list gives '?', 'Shang Era' or 'Xia Era'; 1046 bridge (try https://en.wikipedia.org/wiki/List_of_Zhou_dynasty_states)
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/keyframe_review/0/correction` confirmed

### sui-ningyang: pass
- thin `/ledger/0`: start: the list gives '?', 'Shang Era' or 'Xia Era'; 1046 bridge (try https://en.wikipedia.org/wiki/List_of_Zhou_dynasty_states)
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/keyframe_review/0/correction` confirmed

### hu-luohe: pass
- thin `/ledger/0`: start: the list gives '?', 'Shang Era' or 'Xia Era'; 1046 bridge (try https://en.wikipedia.org/wiki/List_of_Zhou_dynasty_states)
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/keyframe_review/0/correction` confirmed

### kuai: pass
- thin `/ledger/0`: start: the list gives '?', 'Shang Era' or 'Xia Era'; 1046 bridge (try https://en.wikipedia.org/wiki/List_of_Zhou_dynasty_states)
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/keyframe_review/0/correction` confirmed

### ba: thin
- thin `/ledger/0`: founding: Established ? (703 is the first dated mention) (try https://en.wikipedia.org/wiki/Ba_(state))
- thin `/ledger/1`: date of the move from Hubei to the Sichuan basin (500 is a bridge; the keyframe split at -500 depends on it) (try https://en.wikipedia.org/wiki/Ba_(state))
- thin `/ledger/2`: same bridge as /ledger/1 (try https://en.wikipedia.org/wiki/Chongqing)
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/3` confirmed; `/ledger/4` confirmed

### shu: pass
- thin `/ledger/0`: founding: Established ? (bridge at 1046) (try https://en.wikipedia.org/wiki/Sanxingdui)
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/wars/1` confirmed

### sanxingdui-culture: pass
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed
- area: No area on the page beyond the 3.6 km2 walled city; the 100 km Chengdu Plain disc is a stand-in for the culture range.

### dian: pass
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed
- area: No area on the page and no Cliopatria shape (cliopatria_names []); the keyframe note says the disc is a stand-in. The infobox shows '8th century BCE' near 'Established' (the Dian culture); the dossier notes say so and keep 279 for the kingdom.

### xia-dynasty: fix
- FIX (applied) `/ledger/2/confidence`: Confidence 3 on the c. 1600 dissolve whose region (Henan and Shanxi) the Xia page does not name. Evidence: Research brief: 3 only when the page dates the event and names the land; the Henan-Shanxi extent is from the Erlitou culture page ('widely spread throughout Henan and Shanxi'), the Xia page only places Erlitou near Yanshi. Fix: confidence 2, with a reviewer sentence appended to the note
- thin `/ledger/1`: Erlitou spread as a Xia gain is a bridge (confidence 1) (try https://en.wikipedia.org/wiki/Erlitou_culture)
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed

### yiqu: pass
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/3` confirmed; `/ledger/5` confirmed; `/ledger/6` confirmed
- area: No area on the page and no Cliopatria shape (cliopatria_names []); the keyframe note says the disc is a stand-in. Page: 'they may have numbered over twenty' cities; no area.

### xianyu: pass
- thin `/ledger/0`: founding year of Xianyu (660 is the Di settlement after the Wey sack) (try https://en.wikipedia.org/wiki/Northern_Di)
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/3` confirmed; `/ledger/4` confirmed

### wu-geng: fix
- FIX (applied) `/ledger/1/confidence`: Confidence 3 on a derived end year (1041) that the page does not state and partly contradicts ('in three years'). Evidence: Rebellion of the Three Guards page: no BC year for the end; 'second year of the rebellion' and 'defeated the rebels in three years'; zhou-dynasty /ledger/6 dates the reconquest to 1039. Fix: confidence 2 with a reviewer sentence appended to the note (year kept: the page's 'second year' reading)
- spot checks: `/ledger/0` confirmed; `/ledger/1` mis-dated
- area: No area on the page; no Cliopatria shape; the Anyang 80 km disc for Yin is a stand-in (the page calls Wu Geng 'deputy ruler of the east' and says Yin was destroyed).

### dai-baidi: pass
- thin `/ledger/0`: founding: bridge (6th century) (try https://en.wikipedia.org/wiki/Northern_Di)
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/keyframe_review/0/correction` confirmed
- area: No infobox on the page; no Cliopatria shape; the 90 km disc is a stand-in.

### ju: pass
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed
- area: No area on the page and no Cliopatria shape (cliopatria_names []); the keyframe note says the disc is a stand-in. Note: the Rizhao 70 km disc puts the capital Ju County 59 km from its centre; the chu dossier's 431 gain uses Linyi 70 km (109 km away): one of the two should move onto Ju County (118.83, 35.58).

### xing: fix
- FIX (applied) `/ledger/1/confidence`: Confidence 3 on the 662 move to Yiyi, which the page does not date. Evidence: Xing page: only the Red Di threat is dated 662; the relocation sentence follows undated. Fix: confidence 2 with a reviewer sentence appended to the note
- thin `/ledger/2`: who held the Xingtai plain after the move (Red Di; confidence 1) (try https://en.wikipedia.org/wiki/Beidi)
- thin `/ledger/3`: whose land Yiyi was and the year of the move (the Zuo zhuan tradition is 659; not on the page) (try https://en.wikipedia.org/wiki/Duke_Huan_of_Qi)
- spot checks: `/ledger/0` confirmed; `/ledger/1` mis-dated; `/ledger/4` confirmed; `/ledger/5` confirmed
- area: No area on the page and no Cliopatria shape (cliopatria_names []); the keyframe note says the disc is a stand-in. 'Xiangtai' is the Natural Earth spelling of Xingtai (gazetteer alt_names), not a typo.

## Cross-dossier matrix

| event | mirror | status | note |
|---|---|---|---|
| deng -678 loss -> chu | chu -678 gain | matched | Xiangyang 40 km both sides; land agrees, year agrees |
| huang -648 loss -> chu | chu -648 gain | mismatch | regions differ: Huangchuan 45 km here, chu Xinyang 80 km (92 km apart; Huangchuan outside chu disc); year agrees, land disagrees: route to ea-01-a to reconcile regions |
| shen -688 loss -> chu | chu -688 gain | matched | same Nanyang 50 km disc; land agrees, year agrees |
| qi-henan -445 loss -> chu | chu -445 gain | matched | same Kaifeng disc (capital Qi County 2 km outside it); land agrees, year agrees |
| xi -684 loss -> chu | chu -684 gain | mismatch | regions differ: Xi County 35 km here, chu Xinyang 45 km (66 km apart); year agrees, land disagrees: route to ea-01-a to reconcile regions |
| pi -418 loss -> chu | chu -418 gain | mismatch | regions differ: Zaozhuang 40 km here, chu Xuzhou 60 km (76 km apart); year agrees, land disagrees: route to ea-01-a to reconcile regions |
| luo -690 loss -> chu | chu -690 gain | matched | same disc; land agrees, year agrees |
| jiang-zhengyang -623 loss -> chu | chu -623 gain | mismatch | regions differ: Zhengyang coordinate here, chu Zhumadian 40 km; year agrees, land disagrees: route to ea-01-a to reconcile regions |
| jiang-gushi -617 loss -> chu | chu -617 gain | mismatch | regions differ: Gushi coordinate here, chu (115.82, 32.9) 60 km, 84 km apart; year agrees, land disagrees: route to ea-01-a to reconcile regions |
| liu-lu-an -622 loss -> chu | chu -622 gain | matched | same Luan 40 km disc; land agrees, year agrees |
| yong-hubei -611 loss -> chu | chu -611 gain | mismatch | regions differ: Shangyong coordinate 60 km here, chu Shiyan 70 km; the list also names Qin and Ba as conquerors; year agrees, land disagrees: route to ea-01-a to reconcile regions |
| ju -431 loss -> chu | chu -431 gain | mismatch | regions differ: Rizhao 70 km here, chu Linyi 70 km (109 km apart); year agrees, land disagrees: route to ea-01-a to reconcile regions |
| eastern-guo -767 loss -> zheng | zheng -767 gain | mismatch | zheng uses Zhengzhou 25 km; the list locates Eastern Guo at Xingyang: year agrees, land disagrees; route to ea-01-d (counterpart string should become the slug) |
| hu-luohe -763 loss -> zheng | zheng -763 gain | mismatch | zheng uses Zhengzhou 25 km; the list locates Hu at Luohe, about 140 km south: year agrees, land disagrees; route to ea-01-d (counterpart string should become the slug) |
| kuai -769 loss -> zheng | zheng -769 gain | mismatch | zheng names it 'Hui (鄶)' with Zhengzhou 25 km; the list locates Kuai at Xinmi: year agrees, land disagrees; route to ea-01-d (counterpart string should become the slug) |
| ji-beijing -650 loss -> yan | yan -650 gain | matched | both Beijing 30 km; both a bridge year (c. 7th century) |
| east-zhou -249 loss -> qin | qin -249 gain | matched | qin uses (112.8, 34.77) 20 km, here (112.98, 34.77) 20 km: near enough |
| east-zhou -367 found -> eastern-zhou | eastern-zhou -314 split | mismatch | Eastern Zhou (state) infobox 'Independence from Western Zhou: 367 BCE'; the eastern-zhou dossier (ea-01-d) splits at 314: move to 367 |
| east-zhou -307 vassal (page) -> qin | - | missing | 'Since 307 BC, Eastern Zhou became a vassal state of Qin': the qin dossier (ea-01-b) needs vassal_start 307 / vassal_end 249 with counterpart east-zhou (schema: suzerain side) |
| quanrong -771 found -> zhou-dynasty | zhou-dynasty -771 loss | matched | Guanzhong both sides |
| quanrong -750 loss -> qin | qin -750 gain | matched | Guanzhong both sides |
| quanrong -770 (none) -> qin | qin -770 gain | mismatch | qin /ledger/5 gains Baoji 60 km from 'Quanrong' at 770 for King Ping's promise of the land west of Qishan; a promise is not land and the quanrong dossier has no 770 loss (its 766 contest_start covers that zone): route to ea-01-b |
| tan -684 loss -> qi | - | missing | the qi dossier (ea-01-b) has no event between -700 and -560; it needs a gain from tan at -684 (author flagged). Qi's Cliopatria shape qi_-750 (102,632 km2, bbox to 122.71 E) already covers Lai and the small states: qi needs adjust keyframes carving them out until conquest |
| lai -567 loss -> qi | - | missing | the qi dossier (ea-01-b) has no event between -700 and -560; it needs a gain from lai at -567 (author flagged). Qi's Cliopatria shape qi_-750 (102,632 km2, bbox to 122.71 E) already covers Lai and the small states: qi needs adjust keyframes carving them out until conquest |
| ji-shandong -690 loss -> qi | - | missing | the qi dossier (ea-01-b) has no event between -700 and -560; it needs a gain from ji-shandong at -690 (author flagged). Qi's Cliopatria shape qi_-750 (102,632 km2, bbox to 122.71 E) already covers Lai and the small states: qi needs adjust keyframes carving them out until conquest |
| sui-ningyang -681 loss -> qi | - | missing | the qi dossier (ea-01-b) has no event between -700 and -560; it needs a gain from sui-ningyang at -681 (author flagged). Qi's Cliopatria shape qi_-750 (102,632 km2, bbox to 122.71 E) already covers Lai and the small states: qi needs adjust keyframes carving them out until conquest |
| xing -662 gain -> qi | - | missing | confidence 1 on both counts; qi has no 662 loss of Yiyi (route to ea-01-b, low priority) |
| xing -635 loss -> wey | wey -635 gain | matched | Liaocheng 40 km here, 30 km there: same place |
| western-guo -655 loss -> jin | jin -676 gain | mismatch | jin /ledger/4 is a 676 catch-all 'small states of Shanxi (Geng, Huo, old Wei, Yu, Western Guo)'; the Western Guo page gives 655 for Guo and Yu: route to ea-01-b to split out a 655 gain with counterparts western-guo and yu |
| yu -655 loss -> jin | jin -676 gain | mismatch | jin /ledger/4 is a 676 catch-all 'small states of Shanxi (Geng, Huo, old Wei, Yu, Western Guo)'; the Western Guo page gives 655 for Guo and Yu: route to ea-01-b to split out a 655 gain with counterparts western-guo and yu |
| xianyu -489 loss -> jin | - | missing | jin has no 489 gain (Zhao Yang conquers Xianyu): route to ea-01-b |
| xianyu -407 dissolve -> wei | - | mismatch | the page says Wei troops under Yue Yang, but the wei dossier starts at -403, so no dossier receives the land in 407 (jin has no event either). Same pre-403 lineage problem as qin /ledger/9 (409 loss to wei). Orchestrator to decide: counterpart jin before 403, or start wei earlier |
| dai-baidi -457 loss -> zhao | - | mismatch | the zhao dossier starts at -403 and jin has no 457 gain; same pre-403 lineage problem as xianyu 407 |
| zeng -401 loss -> chu | chu -480 gain | mismatch | both bounds: chu /ledger/29 is a c. 480 bridge naming 'Sui'; the Chu list says 'after 506 BC Sui'. Also missing on chu: vassal_start for Zeng c. 632 (Zeng page) - route to ea-01-a |
| zhongli -538 loss -> chu | chu -480 gain | mismatch | both bounds: chu c. 480 bridge vs the Zhongli page (Chu holds it by 538; Wu takes it twenty years later); route to ea-01-a |
| ba -500 loss -> chu | - | missing | chu has no gain near 500 from Ba (both bridges, confidence 1); route to ea-01-a |
| ba -316 loss -> qin | qin -316 gain | matched | qin /ledger/16 |
| shu -316 loss -> qin | qin -316 gain | matched | qin /ledger/15 |
| yiqu -327 loss -> qin | - | missing | qin has no Yiqu event (its 316 'Western Rong tribes' gain may stand for 315); it needs gains 327 (county; the page also says 'became its vassal'), 315 (twenty-five cities) and 272 (the rest, Ordos): route to ea-01-b |
| yiqu -315 loss -> qin | - | missing | qin has no Yiqu event (its 316 'Western Rong tribes' gain may stand for 315); it needs gains 327 (county; the page also says 'became its vassal'), 315 (twenty-five cities) and 272 (the rest, Ordos): route to ea-01-b |
| yiqu -272 loss -> qin | - | missing | qin has no Yiqu event (its 316 'Western Rong tribes' gain may stand for 315); it needs gains 327 (county; the page also says 'became its vassal'), 315 (twenty-five cities) and 272 (the rest, Ordos): route to ea-01-b |
| xia-dynasty -1600 dissolve -> shang-dynasty | shang-dynasty -1600 found | matched |  |
| wu-geng -1041 dissolve -> zhou-dynasty | zhou-dynasty -1039 gain | mismatch | two years apart; the page gives no BC end year (see wu-geng fix); one side should move |
| yelang -111 loss -> han-dynasty | - | exception | han-dynasty (ea-02) not written yet; listed in the author's counterparts_needing_dossiers |
| yelang -183 vassal (page) -> nanyue | - | exception | Nanyue suzerainty 183-111 belongs on the unwritten nanyue dossier (ea-02), schema suzerain side |
| dian -109 loss -> han-dynasty | - | exception | han-dynasty (ea-02) not written yet |
| zhou-dynasty fiefs -1046 found -> zhou-dynasty | zhou-dynasty -1045 vassal_start | missing | zhou-dynasty tints song, cao, cai, chen and chu as vassals until 751 but none of the fiefs founded here (tan, western-guo, yu, ju, xing, zeng, shen, ji-beijing, qi-henan, eastern-guo); route to ea-01-a if the vassal tint is meant to cover the fengjian states |

## Routed to other groups

- ea-01-b (qi): no events between -700 and -560; add gains from tan 684, ji-shandong 690, sui-ningyang 681, lai 567 (and the Yiyi loss to xing 662, low priority); carve Lai and the small states out of qi_-750 until each conquest.
- ea-01-b (jin): split the 676 'small states of Shanxi' gain: western-guo and yu at 655 (Western Guo page); add the 489 gain from xianyu.
- ea-01-b (qin): vassal_start/vassal_end east-zhou 307/249; Yiqu gains 327, 315, 272; the 770 'Quanrong' gain is a promise, not land (quanrong has a 766 contest instead).
- ea-01-a (chu): regions for huang, xi, jiang-zhengyang, jiang-gushi, pi, ju, yong-hubei disagree with the located discs here; the c. 480 bridge for Zhongli and Sui/Zeng vs zhongli 538 and zeng 401; vassal_start zeng c. 632; gain from ba c. 500 (bridge).
- ea-01-a (zhou-dynasty): wu-geng ends 1041 here vs your 1039 gain; consider vassal tints for the fiefs founded in this batch if the tint is meant to cover the fengjian states.
- ea-01-d (eastern-zhou): the split creating east-zhou is 367 (Eastern Zhou (state) infobox), not 314. (zheng): counterpart strings Hui/Eastern Guo/Hu -> kuai/eastern-guo/hu-luohe and their located discs.
- orchestrator: pre-403 Zhao and Wei (dai-baidi 457 -> zhao, xianyu 407 -> wei, qin 409 -> wei) name dossiers that start in -403.
- ea-02: nanyue (Yelang suzerain 183-111) and han-dynasty (Yelang 111, Dian 109) not written yet.

