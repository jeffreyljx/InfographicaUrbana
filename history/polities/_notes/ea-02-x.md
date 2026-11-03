# Notes for group ea-02-x (additions to Qin and Han)

Written 2026-10-19 by the Phase B research agent for ea-02-x. The brief owns no Cliopatria row: this batch writes the states of the Qin-Han region and era that Cliopatria lacks (cliopatria_names [] for all 23, every keyframe new, verdict adjust). The states were chosen from the group scope (Yellow Turbans, the warlord domains of 190-220 with Yuan Shao, Liu Biao and Sun Ce, the Qiang, the 23-36 regimes) and from the counterparts that ea-02-a, ea-02-b, ea-02-c and ea-02-d asked ea-02-x to write (zhang-chu, huainan, hengshan, changsha-kingdom, zhang-bu, liu-yong, peng-chong, wei-ao, dou-rong, chengjia, qiang, yellow-turbans, warlord-domains). Seven further states were added because a page opened for another dossier gave them dated land: gongsun-zan, yuan-shu, liang-province-rebels, han-sui, song-jian, shi-xie, lu-fang (the last two also from pages opened for the Han ledger).

## Group-level points

- Every dossier validates (python3 -I history/tools/validate_dossier.py, 0 errors, 0 warnings; --resolve gives 0 warnings: every region name resolves in the gazetteer). No gazetteer name is missing; text-only place names (Bazhong, Julu, Luomen, Yijing, Meiyang, Shouchun, Fuhan, Heguan) are listed in the report because they are not used in region specs.
- None of the new states removes land from the Han Dynasty shapes of ea-02-c (han-dynasty_184 to 215), which keep Hebei, Jing, Yi, Liang and Jiangdong inside the Han until Cliopatria's own cuts (197, 207, 215). The rendering agents must carve each warlord, rebel and 23-36 regime out of the Han shape for its years; each dossier's predecessors[] names han-dynasty (or xin-dynasty, lulin, western-chu) with the land.
- Confidence: starts for zhang-bu, peng-chong, wei-ao (all 25) and lu-fang (24) are confidence 1 (the Guangwu page dates their fall, not their rise); bridges are marked PAGE SILENT in the event note.
- Pages that would not load, or were the wrong subject: Wei_Xiao, Wei_Ao, Dou_Rong (three tries, url_not_found), Deng_Zhi_(general) (url_not_found); Liu_Zhang is a disambiguation (the article is Liu_Zhang_(warlord)); Peng_Chong, Zhang_Er, Song_Jian are modern people; Lu_Fang is a disambiguation with a red link; Yan_Kingdom_(Han_dynasty), Longxi_Commandery and Luomen,_Wushan do not mention the 25-36 warlords. None was used as a source except where a dossier says so.
- Overlaps for the reviewer: sun-ce (195-206) is the early Wu of Sun Ce and Sun Quan and is continuous with Cliopatria's Eastern Wu row (from 207, ea-03): ea-03 should decide whether to extend eastern-wu back to 195 and drop sun-ce. yuan-shu has Sun Ce as a vassal 195-197 (194 on the Yuan Shu page). dou-rong ends 36 as in ea-02-c's han-dynasty (the Hexi Corridor page dates his submission to 29, and a Han client tie 29-36 may be added to han-dynasty). Hengshan (flagged by ea-02-b) is merged into changsha-kingdom because Wu Rui is one man (rename event at -202), with different land before and after.
- Not written (budget or no page): kingdom-of-zhao-zhang-er (the Zhang Er pages are silent on territory and the kingdom's end), Wang Lang (Handan 23-24), Lü Bu (Xu 196-198), Zhang Xiu (Wancheng 196-200), Dong Zhuo, Liu Yu (You 188-193), the Liu-house Changsha (-155..33) and Liu Chang's Huainan (-196..-174), which are Han vassal kingdoms inside the Han shape; the Tarim city states (Shanshan, Shule, Yanqi, Jushi) belong to ia-01 per ea-02-d; Wuhuan to ia-01.

## Per state

### yellow-turbans (Yellow Turbans, 184..205)

Yellow Turbans, rebel state (type rebel). Cliopatria has no row; its Han shape 184-196 keeps the whole empire (ea-02-c han-dynasty_184 ok). 2 pages opened (Yellow Turban Rebellion; Zhang Yan (Han dynasty)), within the 2-5 page budget for a state without a Cliopatria row.
Could not settle: (1) the English pages name no frontier, so the 184-185 shape is three place clusters (Xiangtai/Handan for Julu-Wei, Nanyang for Wancheng, Xuchang for Runan-Yingchuan), not a border; (2) the page lists the eight provinces only in the Chinese annotation (Qing, Xu, You, Ji, Jing, Yang, Yan, Yu), not in the English body, and the You and Yang attacks (Guo Xun killed; Shu County of Lujiang attacked) are not mapped; (3) the 186-187 and 193-205 Taihang shapes are placeholders (confidence 1): the Zhang Yan page gives no boundary; (4) the Heishan confederacy is a bandit league, not a state, kept inside the Yellow Turbans because Zhang Yan 'raised forces during the Yellow Turban revolt'.
Counterparts: han-dynasty exists (ea-02-c); cao-cao exists (Cliopatria 197-223, ea-03). No dossier needed for Cao Cao's Qingzhou Army. Gazetteer: all names resolve (Xiangtai is Natural Earth's spelling of Xingtai/Julu region).

### yuan-shao (Yuan Shao, 191..207)

Yuan Shao, warlord state of the four northern provinces 191-207. 5 pages opened (Yuan Shao, End of the Han dynasty, Yuan Tan, Gao Gan, Gongsun Zan), the 3-12-shape budget; the state has no Cliopatria row.
Settled: Ji 191; Qing 193 (Yuan Tan); Beihai 196; You after Yijing in April-May 199; the four provinces by 199; Ye and Bing 204; Nanpi and Qing 205; heirs eliminated 207.
Unsettled: (1) Bing Province's date of taking is not on any opened page (199 at confidence 1); (2) 203 (Gao Gan page) against 204 (End of the Han) for Gao Gan's surrender; (3) Tian Kai driven out of Qing in 193 (Yuan Shao page) against only a truce in 193 (Yuan Tan page); (4) who held You Province 204-207 (Yuan Xi?) is not on the pages, the 204 and 205-206 keyframes are confidence 1; (5) provinces are drawn as modern provinces; (6) Yuan Shao died on 28 June 202 (infobox): no land moved, the sons split Ye (Yuan Shang) and Pingyuan (Yuan Tan); no ledger event carries it because the schema has no event type for a succession.
Counterparts: han-dynasty and cao-cao exist; gongsun-zan is written by this batch. Liaodong's Gongsun Du (gongsun-liaodong exists) was outside Yuan's lands. Not mapped: Yuan Shu (south of the Huai from 191), Zhang Yan's Heishan men.

### gongsun-zan (Gongsun Zan, 193..199)

Gongsun Zan, You Province 193-199. 4 pages opened (Gongsun Zan, End of the Han dynasty, Yuan Shao, Yuan Tan); no Cliopatria row.
Unsettled: (1) the 193 start is the infobox's term of office; the body gives no year for Liu Yu's death; (2) the infobox ends the office in March 199 against the footnote's 3rd month of Jian'an 4 = 14 April-12 May 199 (April used); (3) the capital: the page names only the fortress at Yijing; (4) the Qing and Ji claims (Tian Kai, Yan Gang) are not drawn; (5) the Liaodong of Gongsun Du (gongsun-liaodong) lay beyond him.
Counterparts: yuan-shao is written by this batch; han-dynasty exists.

### yuan-shu (Yuan Shu, 189..199)

Yuan Shu, Nanyang then the Huai country, 189-199. 2 pages opened (Yuan Shu, End of the Han dynasty); no Cliopatria row. Unsettled: (1) the page gives no borders ('built up a powerful warlord state'), the Huainan and Hefei circles are a stand-in; (2) who held Nanyang after 192 and Shouchun after 199 (nobody entered, confidence 1); (3) 194 (Yuan Shu page) against 195 (sun-ce dossier) for Sun Ce's crossing: the vassal tie is entered at 195; (4) the page says the Zhong dynasty was proclaimed at Shouchun (End of the Han page), not on the Yuan Shu page; (5) Lujiang and Liu Xun.
Counterparts: han-dynasty, cao-cao exist; sun-ce and yuan-shao are written by this batch; lu-bu and liu-bei have no dossier (lu-bu held Xu Province 196-198: a candidate).

### liu-biao (Liu Biao, 190..208)

Liu Biao, Jing Province 190-208. 3 pages opened (Liu Biao, Jing Province, End of the Han dynasty). No Cliopatria row; the Han shape (ea-02-c) carries Jing until 207.
Unsettled: (1) Nanyang (south-west Henan) was one of Jing's seven commanderies but Wancheng was Zhang Xiu's 196-199 (End of the Han page: he surrendered Wancheng to Cao Cao in 197) and no page says whether Liu Biao held it: left out; (2) the Liu Biao page gives no year for the move to Xiangyang or the first seat; (3) the Huang Zu / Sun Quan fighting over Jiangxia is undated on the pages opened and not in the ledger; (4) the month 9 on 208 follows the page's footnote (8th month of Jian'an 13 = 29 Aug-27 Sep).
Counterparts: han-dynasty, cao-cao, eastern-wu, shu-han exist (ea-03 will write the last three); Sun Jian, Yuan Shu and Liu Bei have no dossier (Yuan Shu, south of the Huai from 191, is a candidate).

### liu-zhang (Liu Zhang, 188..214)

Liu Zhang, Yi Province under Liu Yan and Liu Zhang 188-214. 3 pages opened (Liu Zhang (warlord), End of the Han dynasty, Liu Bei); no Cliopatria row. 'Liu Zhang' (the bare title) is a disambiguation page, the article is 'Liu Zhang (warlord)'.
Unsettled: (1) 214 (Liu Zhang and Liu Bei pages) against 215 (End of the Han page) for the surrender: 214 used; (2) 188 is 'c. 188' on the End of the Han page and Liu Yan's own page was not opened; (3) the Liu Zhang page gives Zhao Wei's revolt as 200 and the break with Zhang Lu as 'from this point on', no territory; (4) Hanzhong was an Yi Province commandery that Zhang Lu took in 194 with Liu Yan's nominal sanction: it is Zhang Lu's, not in this shape; (5) the south-west (Yunnan, Guizhou commanderies) is not on any page.
Counterparts: han-dynasty exists; shu-han is ea-03's (Cliopatria Shu Han 224..262); zhang-lu is written by this batch.

### zhang-lu (Zhang Lu, 194..215)

Zhang Lu, the Hanzhong theocracy 194-215. 3 pages opened (Zhang Lu (Han dynasty), Way of the Celestial Masters, Battle of Yangping); no Cliopatria row.
Unsettled: (1) the Zhang Lu page gives no years; 194 is the Celestial Masters page's ('After the success of the rebellion in 194'); (2) the Zhang Lu page says Zhang Lu 'nominally followed the orders of Liu Yan' and was recognised by the court, so he could be drawn as a Han vassal rather than independent: recorded as independent (the Celestial Masters page: 'enjoying full independence'); (3) the extent beyond Hanzhong Commandery and the Bazhong refuge is not on any page (the End of the Han page says only 'Hanzhong'); (4) the surrender range 9 December 215 - 6 January 216 straddles the year line: 215 month 12 used, and the End of the Han page's 'January 216' for the Cao Cao handover is noted but not used; (5) when Liu Bei occupied Bazhong is undated.
Counterparts: han-dynasty, cao-cao, shu-han exist or are in ea-03; liu-zhang (Yi Province) is written by this batch.
Gazetteer names needed: Bazhong (city in Sichuan) is used only in text; Guangyuan stands for it.

### sun-ce (Sun Ce, 195..206)

Sun Ce, Jiangdong 195-206. 3 pages opened (Sun Ce, Eastern Wu, End of the Han dynasty); no Cliopatria row. The state is the early Wu of Sun Ce and Sun Quan: ea-03 should decide whether to extend eastern-wu back to 195; if so this dossier is dropped and its events moved.
Unsettled: (1) the Sun Ce page dates only the crossing (195), the Kuaiji office in the infobox (197-198) and the death (5 May 200); Yuzhang, Luling, Lujiang and Wan County (199) are not dated beyond 'between 194 and 199'; (2) Wang Lang, Liu Yao, Yan Baihu and Xu Gong were Han officials or bandit leaders, not states; (3) 206 as end is a bridge to the Cliopatria row at 207: no page dates anything 201-206; (4) the Eastern Wu page gives no 200-209 territory or the Huang Zu fight over Jiangxia; (5) Wuhu, Nanjing, Anqing circles and the two modern provinces stand for the commanderies.
Counterparts: han-dynasty and eastern-wu exist; Yuan Shu (Sun Ce's former master, south of the Huai) has no dossier.

### shi-xie (Shi Xie, 187..227)

Shi Xie, the Jiaozhi of the Shi family, 187-227. 2 pages opened (Shi Xie, Eastern Wu); no Cliopatria row. Cliopatria's Han rows (to 237; ea-02-c marks the 224-237 row wrong) and its Eastern Wu shape from 238 (reaching 16.9 N) cover the land; Eastern Wu's 207-237 shape (609,286 km2, south to 22.5 N) does not reach Vietnam, so Vietnam 224-237 is only in the Han row that ea-02-c marked wrong.
Unsettled: (1) the decree giving him the seven commanderies is undated (c. 207 is his promotion: confidence 1); (2) the page does not define the seven commanderies beyond naming Jiaozhi, Jiuzhen, Rinan, Hepu, Nanhai, Cangwu (Yulin only in the later split); (3) the capital is not on the Shi Xie page; (4) the page gives no 210 month for the submission to Bu Zhi; (5) the Book of Liang names a different administrator in 226 (Wu Miao): footnote conflict; (6) the Trung sisters (43-50, se-01) and the Lin-yi/Champa foundation (192, se-01) are neighbours; neither is reconciled here.
Counterparts: han-dynasty, eastern-wu exist.

### liang-province-rebels (Liang Province rebels, 184..189)

Liang Province rebels, 184-189 (rebel). 1 page used for events (Liang Province rebellion) plus the Han Sui and Ma Teng pages for the succession. No Cliopatria row; the Han shape keeps Liang Province throughout.
Unsettled: (1) 'winter of 184' against 'October or November 184' (no month entered); (2) the page does not say when Longxi and Hanyang were taken, only that they were besieged or defected by 187; (3) the page says only that after Emperor Ling's death on 13 May 189 the rebellion 'finally splintered' by year's end, so the dissolve has no month; (4) Qiang and Lesser Yuezhi participants are not given a territory of their own.
Counterparts: han-dynasty exists; han-sui and song-jian are written by this batch.

### han-sui (Han Sui, 189..215)

Han Sui and Ma Teng, the Liang warlords 189-215. 4 pages opened (Han Sui, Ma Teng, Liang Province rebellion, End of the Han dynasty). No Cliopatria row; ea-02-c's han-dynasty has Cao Cao taking Liang and Yong in 211 and drops the Hexi etc. in 215.
Unsettled: (1) the extent of 'Yong' beyond Guanzhong and when the warlords held it; (2) the Han Sui and Ma Teng pages disagree with the End of the Han page on 197 (the Han Sui page puts the peace in 200 and has no 197 submission); (3) the 211-215 shape is a placeholder (confidence 1): Ma Chao's flight to Zhang Lu in Hanzhong (Zhang Lu page, after Tong Pass) and his later years are outside the pages' dates; (4) Ma Teng's execution is June or July 212 on his page (not 211); (5) Cao Cao's nominal overlordship of the two from 197 (End of the Han) and 200 (Han Sui) could be a vassal tie in cao-cao's dossier: not entered here.
Counterparts: han-dynasty, cao-cao exist; liang-province-rebels and song-jian are written by this batch.

### song-jian (Song Jian, 189..214)

Song Jian, the Fuhan kingdom 189-214. 1 page used (Liang Province rebellion); the English Wikipedia 'Song Jian' is an engineer. Unsettled: the year of the royal title (page silent); 'almost thirty years' against the 189 split; Heguan's place; the extent. Counterparts: cao-cao exists; liang-province-rebels is written by this batch.

### qiang (Qiang, 107..118)

Qiang rebels of Dianlian and Lianchang, 107-118 (rebel). 2 pages opened (Qiang (historical people), Liang Province); no Cliopatria row; the Han Dynasty dossier (ea-02-c) carries a contest 107-118 with 'qiang'.
Unsettled: (1) the Qiang page's end (117, Lianchang killed 'the next year' after 116) against the Liang Province page's 118: 118 used; (2) the Qiang page gives the year for Longxi (109) and Hanzhong (110) but none for the Hanyang victory or Dianlian's title; (3) the extent of the rebel-held ground is not on any page (Hexi and Guanzhong uprisings are on the Protectorate page ea-02-c cites, not opened here); (4) no capital is named; (5) the Xianlian's earlier and later revolts (167, the Dongqiang 167-169) are not in this dossier's life; the Shaodang chieftain Dianyu's 57 invasion of Jincheng is outside it too.
Counterparts: han-dynasty exists; 'qiang' is the slug ea-02-c and ea-02-d proposed.

### chengjia (Chengjia, 24..36)

Chengjia, Gongsun Shu's empire in Yi Province, 24-36. 3 pages opened (Gongsun Shu, Emperor Guangwu of Han, Gengshi Emperor); no Cliopatria row. The article title is 'Gongsun Shu'; the infobox state name is 'Chengjia'.
Unsettled: (1) whether Hou Dan's 26 attempt on Hanzhong succeeded (no page; confidence 1, holder entered as nobody); (2) the page gives Yi Province as 'modern Sichuan' (and Chongqing, parts of nearby provinces) without a boundary; (3) the Guangwu page puts the Eastern Han unification at 25 December 36 and the Gongsun Shu page the death at 24 December (month 12 on both); (4) Yunnan commanderies are not mentioned.
Counterparts: han-dynasty (ea-02-c has the 36 gain); xin-dynasty exists; liu-zhang (written by this batch) later held the same province.

### wei-ao (Wei Ao, 25..34)

Wei Ao (Wei Xiao), the Shuoning regime of eastern Gansu 25-34. 1 page used for events (Emperor Guangwu of Han), with the Gengshi Emperor page and the Longxi Commandery, Luomen (Wushan) pages opened and silent on him; Wei_Xiao, Wei_Ao and Dou_Rong (the last, a first time) returned URL_NOT_FOUND. Slug wei-ao follows the counterpart used in ea-02-c's han-dynasty dossier. Unsettled: start year (confidence 1); the extent (Tianshui, Longxi, Anding?); Wei's earlier service under Gengshi. Counterparts: han-dynasty and lulin exist; chengjia is written by this batch (its vassal tie: Wei submitted to Gongsun Shu in 30).

### dou-rong (Dou Rong, 23..36)

Dou Rong, Hexi 23-36. 2 pages opened (Emperor Guangwu of Han; Hexi Corridor); no English article of his own (the first fetch of 'Dou Rong' returned URL_NOT_FOUND), no Cliopatria row. The pages disagree: the Hexi page has his submission in 29 and his start in 23 (24 in a footnote), the Guangwu page has the handover of his lands in 36. 36 is used for the end, as in ea-02-c's han-dynasty dossier; a Han vassal tie 29-36 is plausible (ea-02-c or a gap-filler may add vassal events). The Hexi page names no Dou Rong capital. Counterparts: han-dynasty and xin-dynasty exist.

### liu-yong (Liu Yong, 23..29)

Liu Yong, the Liang of Suiyang 23-29. 2 pages opened (Liu Yong (Xin dynasty), Emperor Guangwu of Han); no Cliopatria row. Not the Liu Yong (Three Kingdoms) page.
Unsettled: (1) the six-commandery conquest (28 cities) has no date on the page (confidence 1 at 25); (2) the Yuzhou, Yanzhou, Qingzhou and Xuzhou 'part of the Commandery area' is not mapped beyond Shangqiu and Xuzhou circles; (3) the page gives Liu Yong's death as 27 (no month) and Liu Yu's last stand at Tanhai to August 29 (Tanhai placed by Linyi, not by the page); (4) Dong Xian, Prince of Haixi, named with Zhang Bu in spring 27, has no dossier and no region on the page.
Counterparts: han-dynasty and lulin exist (ea-02-c); zhang-bu is written by this batch.

### zhang-bu (Zhang Bu, 25..29)

Zhang Bu, Qi 25-29. 2 pages opened (Emperor Guangwu of Han; Liu Yong (Xin dynasty)); no Wikipedia article of his own was found, and Cliopatria has no row. Unsettled: the start year (confidence 1; the Guangwu page gives no date for his rise); the Qi capital (not on any page); the campaign by which the Eastern Han took Shandong. Counterparts: han-dynasty and lulin exist; liu-yong is written by this batch. The 27 'rename' only marks the title; it moves no land.

### peng-chong (Peng Chong, 25..29)

Peng Chong, Yan 25-29. 1 page opened (Emperor Guangwu of Han); the English Wikipedia 'Peng Chong' is a different man (a CCP official) and 'Yan Kingdom (Han dynasty)' does not mention him; no article of his own found. Cliopatria has no row. Unsettled: start year (confidence 1), the capital (Ji is the Han Yan capital, not named for him on any page), the commanderies he held, his alliances.

### lu-fang (Lu Fang, 24..42)

Lu Fang, Inner Mongolia under Xiongnu patronage, 24-42. 2 pages opened (Emperor Guangwu of Han; the Lu Fang disambiguation page, which lists 'Lu Fang (warlord)' as a red link). No Cliopatria row, no article. Unsettled: everything but the control of central and western Inner Mongolia and the flight in 42: the rise year (24 is the disambiguation page's 'fl.'), the title, the capital, his stay as Prince of Dai, the Xiongnu tie (the page says the chanyu Yu supported him: a client relation to record in the xiongnu dossier). Counterparts: xin-dynasty, xiongnu exist.

### zhang-chu (Zhang Chu, -209..-208)

Zhang Chu, Chen Sheng's rebel kingdom, -209..-208 (about half a year; under the ten-year line but flagged by ea-02-a). 2 pages opened (Chen Sheng; Chen Sheng and Wu Guang uprising); both are silent on the territory held, on Wu Guang's siege of Xingyang and on the Zhou Wen march, and neither uses the name 'Zhang Chu' or 'Enlarger of Chu' (they give 'King of Rising Chu', 張楚王). The Dazexiang page's start month is the 7th (9 Aug to 7 Sep 209 BC); the death 4 Jan to 1 Feb 208 BC (the Chen Sheng page: c. January 208 BC). The six rebel kingdoms that broke away (Zhao, Wei, Yan, Qi, Han, Chu) are Cliopatria's rows from -208; the pages opened do not date their founding.

### huainan (Huainan, -203..-196)

Huainan, Ying Bu's Han vassal kingdom, -203..-196. 3 pages opened (Ying Bu; Eighteen Kingdoms; Changsha Kingdom for Yuzhang). Cliopatria's Jiujiang (-206..-204) is the earlier kingdom of the same man; ea-02-b's jiujiang dossier ends in 204 (Long Ju). Unsettled: the Ying Bu page gives no territory table of its own beyond the four commanderies; the Eighteen Kingdoms page has no Huainan row; the capital while King of Jiujiang is not named; the later Han Kingdom of Huainan (Liu Chang, from 196) is not dossiered. Counterparts: han-dynasty, jiujiang exist; changsha-kingdom is written by this batch.

### changsha-kingdom (Changsha Kingdom, -206..-157)

Changsha Kingdom (Hengshan -206..-203, Changsha -202..-157): the Wu family's Han vassal kingdom. 3 pages opened (Changsha Kingdom; Eighteen Kingdoms; Ying Bu). I merged the Hengshan of the Eighteen Kingdoms (flagged 'hengshan' by ea-02-b) with Changsha because Wu Rui is one man (rename event), but their lands differ (Hengshan eastern Hubei and Jiangxi, Changsha Hunan). The Liu-house Changsha (155 BC - AD 33, Liu Fa to Liu Xing) is not dossiered: it sits inside the Han shape and the page gives its end as the demotion of Liu Xing in AD 33. Unsettled: the end of Hengshan (the pages give none); Wu Rui's reign 203-202 against 202; the dates of Zhao Tuo's invasions (the page gives 183 for the embargo only). Counterparts: han-dynasty, nanyue, western-chu exist; huainan is written by this batch.

## Repair pass (ea-02-x-fixed, 2026-10-19)

Written after the adversarial review (history/polities/_notes/review-ea-02-x.md). Eight dossiers had verdict fail and were repaired: yellow-turbans, yuan-shao, zhang-lu, sun-ce, shi-xie, han-sui, wei-ao, zhang-bu. The pass/fix/thin dossiers were not touched. Every finding was checked against a reopened page before the fix; all eight validate with --resolve (zhang-lu has 4 warnings, all the one unknown place name Bazhong). The per-state sections above describe the first pass; where they differ from this section, this section is current.

### What was changed, per dossier

- **yellow-turbans** (3 pages now: Yellow Turban Rebellion, Zhang Yan (Han dynasty), Heishan bandits). Nanyang loss added (185/1, confidence 2: the page says 'By the beginning of 185 ... following Zhu Jun's recapture of Wancheng', no date for the recapture, Zhao Hong killed 'during or after October 184'). Xuchang circle dropped from the held shape (it stays the contest zone of /ledger/2-3 and of the war). Taihang gain added (185, confidence 1). Shandong dropped from 188-192 (contest only), so the three Taihang keyframes merged into yellow-turbans_185 (185-205); K0 is now 184 only. The 192 contest_end note joined two sentences of the page ('Around May 192 ... swarmed into Yan Province' and the undated Jibei surrender): corrected, month dropped, confidence 2.
- **yuan-shao** (5 pages, the same five). Ji Province is southern Hebei, not all of Hebei: the Yuan Shao page says Ji is 'present day southern Hebei' and You '(present day northern Hebei)'. K0-K2 and /ledger/0 and the 204 loss are Hebei minus (Baoding 100 km, the northern arcs of You, the Heishan's Taihang circle); You enters only at 199 (/ledger/5, K3-K5, dissolve, successors) as Beijing, Tianjin and the same northern Hebei, without the Taihang circle; Bing is Shanxi minus the Taihang circle. Overlap checked with the gazetteer: 0 cells shared with yellow-turbans, and with gongsun-zan only in 199, the year Yijing falls (a transition year). 193 Qing mirror: kept the counterpart and wrote the exception into /ledger/2 (gongsun-zan is thin and was not touched). Bing: the Gao Gan page gives 'about seven years' to 206, i.e. about 199, an inference; confidence stays 1. You Province 204-207: the Yuan Shao page's list of sons has Yuan Xi 'moved to You Province after Yuan Shao's death' (undated); the Yuan Xi page was not opened (five-page budget).
- **zhang-lu** (3 pages). Guangyuan circle removed from 194-214; K0 is Hanzhong 100 km cut at the Sichuan border. Bazhong kept as a 215 refuge (keyframe zhang-lu_215, a gain at confidence 1 with counterpart shu-han, the dissolve region), with the place name 'Bazhong' that the gazetteer lacks. The Battle of Yangping page: 'Zhang Lu retreated to Bazhong' when Yangping Pass fell, 'led his followers out of Bazhong' 9 December 215 - 6 January 216, Liu Bei 'occupied Bazhong after Zhang Lu left'; it does not say how or when Zhang Lu held Bazhong. contest_start month 8 kept as the first half of the 13 August - 10 September window for reaching Yangping Pass (confidence 2); the campaign was launched 17 April - 15 May and the page dates no fighting at Yangping.
- **sun-ce** (5 pages now: + Hua Xin, Sun Quan). Wu Commandery (Suzhou, Jiangsu 100 km) gained 196 (confidence 2) and Kuaiji moved from 197 to 196 (confidence 2) on the Sun Ce page's 'less than a year' from Niuzhu (195); the infobox 197-198 is an office date. vassal_start 195 and vassal_end 197 with yuan-shu added (mirrors yuan-shu /ledger/5, /7). Yuzhang is dated 199 by the Sun Quan page ('In 199, Sun Quan followed his brother to conquer Lujiang and Yuzhang'); the Hua Xin page is silent on the date; Luling stays undated. The 206 end stays a bridge (Sun Quan page: inheritance 200, Shanyue fortress 206, Huang Zu 208).
- **shi-xie** (2 pages; Shi Yi page not found). K0 split: Jiaozhi alone 187-206, the family's five commanderies (Jiaozhi, Jiuzhen and Rinan as the Vietnam part of the Han 197 shape, Hepu as Beihai 100 km, Nanhai as Guangdong) 207-227. Guangxi (Cangwu, Yulin) removed: the page gives the family Jiaozhi, Hepu, Jiuzhen and Nanhai; Wu Ju (Cangwu) was Liu Biao's man, killed by Bu Zhi in 210. The 210 rename is a vassal_start with eastern-wu, and a vassal_end 227 added. The seven-commandery decree is still undated: it follows Zhu Fu's death (200) and Zhang Jin's governorship (203, footnote 10) and precedes the 207 promotion, which the page calls 'further'; 207 is kept as a ceiling at confidence 1.
- **han-sui** (5 pages now: + Yong Province). The Guanzhong is removed (Yong Province page: the 194 Yongzhou Inspectorate covered Wuwei, Zhangye, Jiuquan, Dunhuang and Xihai; the Three Guardians joined Yongzhou only in 213). The 197 event is a vassal_start to han-dynasty, with a new vassal_end 211/9. Keyframes merged to han-sui_189 (189-210) and han-sui_211 (211-215); Ningxia is in from 189 (the rebels' shape); Song Jian's Fuhan (Linxia 80 km) and Zhang Lu's Hanzhong (100 km) are cut out of every shape (0 cells shared, checked). The 211 loss is now the Baoji circle only (the pages give no Guanzhong holding); Gansu and Ningxia are annexed 'over the next few years' (dissolve 215). The wrong quotation in /ledger loss 211 is replaced by the page's wording.
- **wei-ao** (1 page). vassal_start 30 (confidence 2: 'In response' to the summer-30 campaign, the sentence has no year of its own) and vassal_end 34 with chengjia added; the identity predecessor lulin changed to han-dynasty, like the ledger counterpart the reviewer had already fixed.
- **zhang-bu** (3 pages now: + Geng Yan). The 27 rename is a vassal_start with liu-yong plus a vassal_end 27. The shape is Shandong minus liu-yong's three circles (Shangqiu 120 km, Xuzhou 100 km, Linyi 70 km) for the whole of 25-29. Capital added: Ju (Geng Yan page: 'based in Ju County'). The identity predecessor lulin changed to han-dynasty.

### Where I disagree with the reviewer, or went further

- **yellow-turbans, Heishan.** The reviewer asked to add the Taihang gain and say why the Heishan are carried here. Done, but the reopened Heishan bandits page says the founders were 'unrelated to the Yellow Turban movement'; only the Zhang Yan page ties Zhang Yan to the revolt ('raised forces during the Yellow Turban revolt'). The strip is therefore a confidence-1 placeholder kept for the rebellion page's end year (205). A separate Heishan entry would be the cleaner home (listed under gaps).
- **zhang-bu, one shape instead of a split at 27.** The reviewer proposed splitting K0 at 27. After Liu Yong's death the Jiyin-Shanyang country belongs to the Eastern Han (liu-yong's 27 loss), so a split would hand it back to Zhang Bu with no event. One keyframe with all three circles cut avoids that; the cost is a Linyi hole in 25-26 because the Liu Yong page names no holder of Tanhai before Liu Yu (it has Dong Xian as Prince of Haixi without locating Haixi). Also the Liu Yong page attributes the attack on Jiyin, Shanyang, Pei, Chu, Huaiyang and Runan to Zhou Jian, not directly to Liu Yong.
- **han-sui, reviewer's quotation.** The reviewer quotes the End of the Han page as 'a coalition who controlled Liang and Yong provinces, led by Ma Chao and Han Sui, was defeated ... at Tong Pass in 211'. On the reopened page 'who controlled' belongs to the sentence before (the warlords' suspicions); the Tong Pass sentence is 'was defeated by Cao Cao at the Battle of Tong Pass in 211, and their territories were annexed by Cao over the next few years'. The 197 sentence ('Cao Cao was able to persuade Ma Teng and Han Sui, who controlled Yong and Liang provinces') is as quoted. The Ma Teng page does say Cao Cao 'feared Ma Teng's influence in Guanzhong' (208) and has Liang Province 'covering parts of present-day Shaanxi and Gansu': that supports the Baoji circle, which stays, not the Guanzhong.
- **han-sui, vassal_end 211.** The reviewer asked only for a vassal_start 197 cp han-dynasty; the validator needs a paired end, so a vassal_end 211/9 cp han-dynasty was added (Ma Teng page: Tong Pass, September 211). The pages date no formal revocation.
- **sun-ce, Kuaiji at 196.** The reviewer said 'consider'. Done at confidence 2 because the Sun Ce page puts the whole region southeast of the Long River within a year of Niuzhu (195); the only date it gives for Kuaiji is the 197-198 office.
- **yuan-shao, Qing mirror.** Not fixed in gongsun-zan (thin, not touched); the exception is written into /ledger/2. gongsun-zan's shape also stops at Baoding 100 km, so the northern arcs of Hebei that yuan-shao now cuts out of Ji (191-198) are drawn for nobody in 193-198: a gap-filler should extend gongsun-zan's You to them.
- **zhang-lu, circle cut at the Sichuan border.** The Hanzhong 100 km circle shared 19 of its 141 cells with liu-zhang's Sichuan; cut out.

### Points for the other groups

- ea-02-c, han-dynasty: /ledger/98 (196 loss of Yong to han-sui) and /ledger/103 (211 gain from han-sui) still treat Yong as the Guanzhong; han-sui no longer holds the Guanzhong, and loses only the Baoji circle at 211. han-dynasty also lacks the mirrors listed in the review matrix (yellow-turbans, yuan-shao 199, shi-xie, qiang, the 23-25 regimes).
- ea-03: shu-han is the counterpart of zhang-lu's 215 Bazhong gain and of liu-zhang's 214 loss; eastern-wu is the counterpart of shi-xie's 210 vassal_start and 227 events and cp of sun-ce's dissolve; cao-cao keeps the Yuan, Liu Biao, Zhang Lu and Song Jian losses. Nothing was written for them.
- Gazetteer: 'Bazhong' (place; prefecture-level city in north-eastern Sichuan, about 31.9 N 106.8 E) is used in zhang-lu. 'Suzhou, Jiangsu' (the gazetteer's alias for the Jiangsu Suzhou) is used in sun-ce, because plain 'Suzhou' resolves to Suzhou in Anhui.
- Pages that failed: https://en.wikipedia.org/wiki/Shi_Yi_(Han_dynasty) (URL_NOT_FOUND).
- Thin items not worked, with reason: yuan-shao You Province 204-207 (Yuan Xi page: five-page budget); han-sui 211-215 (Ma Chao page: five-page budget); wei-ao rise and nominal submission before 30 (Gengshi Emperor page was opened in the first pass and is silent); sun-ce 200-206 holdings (Sun Quan page gives none); shi-xie brothers' appointment dates (Shi Yi page not found; the Shi Xie page is silent).
