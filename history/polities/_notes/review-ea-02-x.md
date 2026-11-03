# Review of batch ea-02-x (additions to Qin and Han)

Reviewed 2026-10-19 by the adversarial reviewer. Inputs: the author's report (history/notes/phase-b/reports/ea-02-x.json), notes (history/polities/_notes/ea-02-x.md), the 23 dossiers, and the neighbour ledgers that exist (han-dynasty, xin-dynasty, lulin, qin-dynasty, western-chu, jiujiang, xiongnu, nanyue and the Context list of the author's brief; cao-cao, eastern-wu and shu-han are ea-03 and not written yet). All 23 dossiers validate with --resolve (0 errors, 0 warnings). About 95 events were checked on the pages they cite; no event was found fabricated, and the years held. The faults are in the land and in links between dossiers: shapes that disagree with their own ledger, ground drawn for two states at once, vassal ties recorded on one side only, and one wrong province (Yong).

Verdicts: yellow-turbans **fail**, yuan-shao **fail**, gongsun-zan **thin**, yuan-shu **fix**, liu-biao **thin**, liu-zhang **thin**, zhang-lu **fail**, sun-ce **fail**, shi-xie **fail**, liang-province-rebels **pass**, han-sui **fail**, song-jian **pass**, qiang **pass**, chengjia **fix**, wei-ao **fail**, dou-rong **thin**, liu-yong **fix**, zhang-bu **fail**, peng-chong **fix**, lu-fang **thin**, zhang-chu **thin**, huainan **fix**, changsha-kingdom **thin**.

Policy used: **fail** = an unapplied finding the author must fix (wrong land, a keyframe the ledger contradicts, an overlap with a sister dossier, a mirror missing inside this batch). **thin** = valid and honest; gaps for a gap-filler. **fix** = the reviewer applied small verified fixes and nothing blocking is left. **pass** = nothing found.

## Problems and cross-group points

- Reviewer applied small fixes in place (orchestrator's adjustment to the brief): counterparts lulin->han-dynasty in liu-yong /ledger/2, wei-ao /ledger/0, zhang-bu /ledger/0, peng-chong /ledger/0; han-dynasty->western-chu in huainan /ledger/0; confidence 3->2 in chengjia /ledger/3 and lu-fang /ledger/1; yuan-shu /ledger/8 note rewritten. All re-validated (0 errors, 0 warnings, --resolve) and read back; backups in /tmp/claude-0/work/review-ea-02-x/backup/.
- Cross-group, for ea-02-c: han-dynasty /ledger/98 (196 loss of Yong to han-sui) uses the Guanzhong too, but Yong of 194-213 was the Hexi commanderies (Yong Province page); /ledger/90 (Yuan Shu, 191) and /ledger/54 (Liu Yong, 29) disagree by two years with the dossiers here; many found events of this batch (yellow-turbans, yuan-shao 199, shi-xie, qiang, the 23-25 regimes) have no han-dynasty mirror.
- Cross-group, for ea-02-c and ea-03: this batch gives the warlords' land to cao-cao (204-215) while han-dynasty /ledger/102-103 gives the same land to han-dynasty (207, 211); one model must be chosen before rendering.
- Overlaps between contemporaneous dossiers of this batch (same ground drawn for two states): yuan-shao Hebei vs gongsun-zan Baoding (193-198) and yellow-turbans Taihang (193-204); han-sui Gansu vs song-jian Linxia (189-214); liu-zhang Sichuan vs zhang-lu Guangyuan (194-214); zhang-bu Shandong vs liu-yong (25-29). Fixes are listed on yuan-shao, han-sui, zhang-lu and zhang-bu.
- Identity note: the slug 'qiang' names a whole people but the dossier covers only Dianlian's rebel state 107-118; a later dossier for the Qiang as neighbours would need another slug.
- No Wikipedia infobox in this batch gives an area and no dossier has a Cliopatria row, so every area_check is empty by necessity.
- No page failed to load for the reviewer.

## Per dossier

### yellow-turbans: fail

- **TO FIX** `/ledger (after /ledger/4); /keyframe_review/0`: Nanyang (Wancheng, 70 km circle) is held in K0 184-185 and gone in K1, but no ledger event loses it. Evidence: Yellow Turban Rebellion page: 'By the beginning of 185, the rebellion had mostly been suppressed following Zhu Jun's recapture of Wancheng in Nanyang Commandery'; Zhao Hong was killed during or after October 184. Fix: Add a loss, 185 month 1 (or 184), counterpart han-dynasty, region the Nanyang 70 km circle, source the Yellow Turban Rebellion page, confidence 2.
- **TO FIX** `/keyframe_review/0/correction`: The Xuchang 90 km circle (Runan-Yingchuan) is drawn as held territory for 184-185, but the ledger has only a contest_start (184/5) and contest_end (184/6) there, no gain. Evidence: Rule 4: a held area needs a gain/loss; a contest zone is not ownership. The page has Bo Cai fighting at Changshe, Yangzhai and Xihua, not holding a territory. Fix: Drop the Xuchang circle from K0 (leave it as the contest zone), or add a gain 184/5 and a loss 184/6.
- **TO FIX** `/keyframe_review/1`: The Taihang circle (Shijiazhuang 120 km) appears in 186 with no ledger gain; the state then lasts to 205 on Zhang Yan's Heishan alone. Evidence: Zhang Yan page: he 'raised forces during the Yellow Turban revolt', raided Julu in 185, and his group 'became known as the Heishan bandits'; the page never says the Heishan were Yellow Turbans. Fix: Add a gain (185, confidence 1 or 2, Zhang Yan page) for the Taihang ground, and state in notes and identity why the Heishan confederacy is carried in this dossier rather than as its own rebel entry.
- **TO FIX** `/keyframe_review/2/correction`: Shandong (admin1) is drawn as held 188-192, but the ledger only opens and closes a contest there (/ledger/5 contest_start 188/11, /ledger/6 contest_end 192/5). Evidence: Page: 'In c.November 188, there was a resurgence in Yellow Turban rebels in both Qing and Xu provinces, and they raided numerous counties'; raids, not a held province. Fix: Keep Shandong out of the K2 shape (contest zone only) or replace the contest pair with a gain 188/11 and a loss 192/5 of a named smaller area.
- **TO FIX** `/keyframe_review/3/correction`: The Shijiazhuang 120 km circle (193-205) lies inside yuan-shao's admin1 Hebei (191-204): the same ground is drawn for both states. Evidence: yuan-shao.json /keyframe_review/0-3 use admin1 Hebei. Fix: Resolve with yuan-shao (fix listed there): either yuan-shao takes 'minus' this circle or this keyframe is narrowed to the Taihang range itself.
- thin `/keyframe_review/1, /keyframe_review/3`: Extent of the Heishan/Taihang holding 186-205 (confidence-1 placeholder). Page to try: https://en.wikipedia.org/wiki/Heishan_bandits
- thin `/keyframe_review/0`: The eight provinces of the 184 rising and the You and Yang fronts are not mapped. Page to try: https://en.wikipedia.org/wiki/Yellow_Turban_Rebellion
- spot checks: /ledger/0 confirmed ('In March, Zhang Jue started the Yellow Turban Rebellion with roughly 360,000 followers'); /ledger/4 confirmed ('the main Yellow Turban Rebellion ended by February 185'); /ledger/5 confirmed ('In c.November 188, there was a resurgence ... in both Qing and Xu provinces'); /ledger/6 confirmed ('Around May 192' paragraph; 300,000 surrendered to Cao Cao in Jibei); /ledger/7 confirmed ('In the summer of 205 ... Zhang Yan brought his 100,000 followers' and surrendered; Heishan not called Yellow Turbans)
- area: no infobox area, no Cliopatria row.

### yuan-shao: fail

- **TO FIX** `/keyframe_review/0/correction, /keyframe_review/1/correction, /keyframe_review/2/correction, /ledger/0/region`: Ji Province is drawn as the whole of admin1 Hebei for 191-198, which includes northern Hebei (Baoding, Langfang, Tangshan, Zhangjiakou, Chengde, Qinhuangdao) that belonged to You Province: gongsun-zan draws a Baoding 100 km circle (Yijing) for 193-199, and yellow-turbans a Shijiazhuang 120 km circle for 193-205, so the same ground is in two states. Evidence: gongsun-zan.json /keyframe_review/0 (union Beijing, Tianjin, Baoding 100 km, 193-199); Yuan Shao page: You Province came to Yuan Shao only after Yijing fell in 199; Gongsun Zan page: 'he retreated to Yijing where he prepared strong defences'. Fix: Write K0-K2 (and /ledger/0) as {"minus": [Hebei, union(Baoding 100 km, the You commanderies of northern Hebei)]} for 191-198 so that You is added only at /ledger/5 (199); decide the Taihang circle with yellow-turbans (minus it here for 193-204, or narrow it there).
- **TO FIX** `/ledger/2`: The 193 gain of Qing has counterpart gongsun-zan, but gongsun-zan's ledger and shape hold no Qing ground, so the gain has no mirror. Evidence: Yuan Shao page: 'driving out Gongsun Zan's general Tian Kai in 193' (the counterpart is right); gongsun-zan notes: 'Qing and Ji claims not drawn'. Fix: Keep the counterpart; gongsun-zan must add the Qing claim (Tian Kai, Pingyuan) and a loss in 193 (listed under gongsun-zan). Alternatively mark the exception in notes.
- thin `/ledger/4`: Date Bing Province was taken (199 at confidence 1). Page to try: https://en.wikipedia.org/wiki/Gao_Gan
- thin `/keyframe_review/4, /keyframe_review/5`: Holder of You Province 204-207 (Yuan Xi) and its extent. Page to try: https://en.wikipedia.org/wiki/Yuan_Xi
- spot checks: /ledger/0 confirmed (Ji Province taken from Han Fu in 191); /ledger/2 confirmed ('driving out Gongsun Zan's general Tian Kai in 193'); /ledger/3 confirmed ('Yuan Tan managed to seize Beihai State from Kong Rong in the east in 196' (note's quote not verbatim)); /ledger/4 confirmed (bridge: four provinces by early 199; Bing Province not named, no date (confidence 1 is honest)); /ledger/9 confirmed ('after conquering Ye city in 204'); /ledger/10 confirmed ('Gao Gan also surrendered Bing Province to Cao Cao' in the early-204 narrative); /ledger/11 confirmed (Battle of Nanpi, first lunar month of 205 (7 Feb to 7 Mar 205)); /ledger/12 confirmed ('completely eliminated Yuan Shao's heirs and remnants by 207')
- area: no infobox area, no Cliopatria row.

### gongsun-zan: thin

- thin `/ledger (193)`: Gongsun Zan's Qing claim: Tian Kai was his Inspector of Qing and was driven out by Yuan Tan in 193; yuan-shao /ledger/2 gains Qing from gongsun-zan in 193 with no mirror here (add the claim and a loss 193 cp yuan-shao). Page to try: https://en.wikipedia.org/wiki/Yuan_Tan
- thin `/identity/capitals/0`: Yijing as capital from 193: the page says only that he 'retreated to Yijing' (undated); Ji (Beijing) may be the seat before. Page to try: https://en.wikipedia.org/wiki/Battle_of_Yijing
- spot checks: /ledger/0 confirmed (infobox Inspector of You 193 - March 199 (self-appointed); Liu Yu's killing undated (confidence 2 is honest)); /ledger/2 confirmed ('In 199, Yuan Shao besieged Yijing'; occupied in the 3rd month of Jian'an 4 (14 April to 12 May 199)); /ledger/3 confirmed; /ledger/4 confirmed
- area: no infobox area, no Cliopatria row.

### yuan-shu: fix

- **APPLIED** `/ledger/8/note`: The note quoted 'The article doesn't describe what happened to his territory' as if it were page text (it is the fetch tool's summary) and said he died at Shouchun. Evidence: Yuan Shu page: he 'died shortly thereafter of starvation' after being forced back to Shouchun; a footnote puts the death at Jiangting, 80 li from Shouchun. Fix: Rewrote the note without the pseudo-quotation and with Jiangting; tagged [Reviewer ea-02-x].
- thin `/keyframe_review/1`: K1 (192) still holds Nanyang although /ledger/1 loses it in 192; and the holder of Nanyang after Yuan Shu is unknown. Page to try: https://en.wikipedia.org/wiki/Zhang_Xiu_(warlord)
- thin `/keyframe_review/2`: Yuan Shu's Yu Province lands (Runan, Chen) and Lujiang/Guangling 193-199 are not drawn. Page to try: https://en.wikipedia.org/wiki/Yuan_Shu
- spot checks: /ledger/2 confirmed ('moved his residence to Chenliu, and extended his influence into Yang Province in 192'); /ledger/3 confirmed ('In early 193, Yuan Shu suffered repeated defeats, such as the Battle of Fengqiu'); /ledger/4 confirmed (fled to Shouchun, deposed Chen Wen (no year on the page; confidence 2 honest)); /ledger/5 confirmed ('From 194 to early 197, Sun Ce ... conquered many territories in Jiangdong on Yuan Shu's behalf' (194 on page, 195 in dossier: within a year)); /ledger/6 confirmed ('declared himself emperor ... in early 197'); /ledger/9 confirmed (6th month of Jian'an 4 = 11 July to 9 August 199)
- area: no infobox area, no Cliopatria row.

### liu-biao: thin

- thin `/ledger (208)`: Jiangxia lost to Sun Quan (Huang Zu killed at the Battle of Jiangxia, spring 208) before Liu Biao's death: a loss cp sun-ce/eastern-wu is missing. Page to try: https://en.wikipedia.org/wiki/Battle_of_Jiangxia
- thin `/ledger (c. 198-201)`: Zhang Xian's revolt of Changsha, Lingling and Guiyang against Liu Biao (a contest or loss and recovery). Page to try: https://en.wikipedia.org/wiki/Huang_Zhong
- thin `/keyframe_review/0`: Single keyframe for 190-208; Nanyang (Zhang Xiu as Liu Biao's ally 197-199) and the move of the seat to Xiangyang are undated. Page to try: https://en.wikipedia.org/wiki/Zhang_Xiu_(warlord)
- spot checks: /ledger/0 confirmed ('in 190 CE, when Dong Zhuo appointed him to the position'); /ledger/1 confirmed (died 8th month of Jian'an 13 (29 Aug to 27 Sep 208); Liu Cong surrendered later that year); /ledger/2 confirmed (Liu Cong 'surrendered and ceded the province to the warlord Cao Cao in the same year' (208); split after Red Cliffs)
- area: no infobox area, no Cliopatria row.

### liu-zhang: thin

- thin `/ledger (200-201)`: Zhao Wei's rebellion against Liu Zhang (200) and Zhang Lu's break with him (the Liu Zhang page implies 200) are not in the ledger. Page to try: https://en.wikipedia.org/wiki/Liu_Zhang_(warlord)
- thin `/keyframe_review/0`: Yi Province's southern commanderies (Yizhou, Yongchang, Zangke, Yuexi: Yunnan, Guizhou) are not drawn; Liu Yan's own page not opened for 188-194. Page to try: https://en.wikipedia.org/wiki/Liu_Yan_(warlord)
- thin `/keyframe_review/0`: Overlap with zhang-lu's Guangyuan circle (inside admin1 Sichuan) 194-214: resolved by the fix listed under zhang-lu, or by a 'minus' here. Page to try: https://en.wikipedia.org/wiki/Battle_of_Yangping
- spot checks: /ledger/0 confirmed ('Liu Yan was commissioned as the Governor of Yi Province' (188 reform; confidence 2 honest)); /ledger/1 confirmed ('In the spring of 213, Liu Zhang sent Liu Gui, Ling Bao, Zhang Ren, Deng Xian, Wu Yi ... to stop him at Fu'); /ledger/2 confirmed ('by 214 they had surrounded Yi Province's capital, Chengdu'); /ledger/4 confirmed (succeeded Liu Zhang as Governor; summary table 214)
- area: no infobox area, no Cliopatria row.

### zhang-lu: fail

- **TO FIX** `/keyframe_review/0/correction and /ledger/0-4/region`: Every region is Hanzhong 100 km plus a Guangyuan 80 km circle standing for Bazhong, held 194-215; Guangyuan lies in Sichuan, inside liu-zhang's admin1 Sichuan for 188-214, so the two states overlap for twenty years, and the opened pages put Zhang Lu in Bazhong only as his 215 refuge. Evidence: Battle of Yangping page: 'Between 9 December 215 and 6 January 216, Zhang Lu led his followers out of Bazhong'; no opened page gives Zhang Lu land south of Hanzhong before 215; liu-zhang.json /keyframe_review/0 = union(Sichuan, Chongqing) 188-214. Fix: Make K0 (194-214) the Hanzhong circle only; if the Bazhong refuge is kept, add a 215 keyframe/event with place 'Bazhong' (gazetteer name needed) instead of the Guangyuan stand-in; or have liu-zhang take 'minus' that circle.
- thin `/ledger/1`: Month 8 for the contest_start is not on the page (campaign launched 17 April-15 May 215; the Yangping fighting is undated in the text). Page to try: https://en.wikipedia.org/wiki/Battle_of_Yangping
- spot checks: /ledger/0 confirmed ('After the success of the rebellion in 194, they founded the theocratic state of Zhang Han in the Hanzhong Valley'); /ledger/2 confirmed (9 December 215 - 6 January 216 surrender); /ledger/3 confirmed (Nanzheng occupied, Hanning renamed Hanzhong (undated)); /ledger/4 confirmed ('In 215, Zhang Lu submitted to Cao Cao')
- area: no infobox area, no Cliopatria row.

### sun-ce: fail

- **TO FIX** `/keyframe_review/0/correction, /keyframe_review/1/correction, /keyframe_review/2/correction`: Wu Commandery (Suzhou-Wuxi, southern Jiangsu) is in no keyframe at all, and Kuaiji enters only in 197, although the page has the whole region south-east of the Yangtze conquered within a year of Niuzhu (195). Evidence: Sun Ce page: 'from the occupation of Niuzhu to the conquest of the entire region southeast of the Long River, took less than a year' (Niuzhu in 195); Liu Yao, Xu Gong (Wu) and Wang Lang (Kuaiji) are beaten in that campaign (undated). Fix: Add Wu Commandery (e.g. place Suzhou 100 km) to every keyframe from 196 with a gain 196 (confidence 2) cp han-dynasty; consider Kuaiji in 196 at confidence 2 (the infobox's Administrator of Kuaiji 197 is an office date).
- **TO FIX** `/ledger (195, 197)`: No vassal tie to Yuan Shu, although yuan-shu /ledger/5 (vassal_start 195, cp sun-ce) and /ledger/7 (vassal_end 197) assert one: the mirror is missing. Evidence: Sun Ce page: he went to Yuan Shu in 194 (infobox allegiance 'Yuan Shu's forces') and in 197, when Yuan Shu declared himself emperor, he 'denounced the move and broke ties'. Fix: Add vassal_start 195 cp yuan-shu and vassal_end 197 cp yuan-shu (Sun Ce page, confidence 2) with the 195 region.
- thin `/ledger/2`: Yuzhang and Luling are undated on the page; the whole of Jiangxi is entered in 199 at confidence 2 (1 would be honest for Jiangxi; Wan County is 199). Page to try: https://en.wikipedia.org/wiki/Hua_Xin
- thin `/ledger/3`: End year 206 is a bridge (confidence 1) to Cliopatria's Eastern Wu (ea-03); Sun Quan's 200-206 holdings undated. Page to try: https://en.wikipedia.org/wiki/Sun_Quan
- spot checks: /ledger/0 confirmed ('successfully occupied the strategic position of Niuzhu' in 195); /ledger/1 confirmed (infobox Administrator of Kuaiji 197-198; Wang Lang's surrender undated); /ledger/2 confirmed (Wan County captured after Yuan Shu's death (199); Yuzhang/Luling undated); /keyframe_review/0 not on page (K0's Wuhu-Nanjing-only extent contradicts 'the entire region southeast of the Long River' within a year)
- area: no infobox area, no Cliopatria row.

### shi-xie: fail

- **TO FIX** `/keyframe_review/0`: K0 (187-209) draws the seven commanderies (Vietnam, Guangdong, Guangxi) from 187, but /ledger/0 founds the state on Jiaozhi only (Hanoi 100 km) and /ledger/1 gains the seven commanderies c. 207 (confidence 1): for twenty years the keyframe holds some 400,000 km2 the ledger does not give. Evidence: Shi Xie page: 'In 187 ... reassigned him to be the Administrator of Jiaozhi'; the decree for the seven commanderies is undated and follows the killing of Zhu Fu (200); the brothers' posts are undated. Fix: Split K0: 187 to the year before the gain = Jiaozhi only (the /ledger/0 region); from the gain (c. 201-207, confidence 1) to 209 = the family's commanderies.
- **TO FIX** `/keyframe_review/0-1/correction, /ledger/1, /ledger/5, /ledger/6`: admin1 Guangxi (Cangwu, Yulin) is drawn as Shi family land 207-227, but the page names the family's posts as Jiaozhi (Shi Xie), Hepu (Shi Yi), Jiuzhen (Shi Wei) and Nanhai (Shi Wu); Cangwu's Administrator was Wu Ju, beheaded by Bu Zhi in 210. Evidence: Shi Xie page body and footnotes 11 and 14 (Bu Zhi sent in Jian'an 15 = 210; Shi Xie and his brothers submitted to him; Bu Zhi beheaded Wu Ju, Administrator of Cangwu). Fix: Replace Guangxi with Hepu (coastal Guangxi round Beihai-Qinzhou) and keep Guangdong only as Nanhai; from 210 drop Cangwu, which Bu Zhi took.
- **TO FIX** `/ledger/2`: The 210 submission to Sun Quan's governor is typed 'rename'; it is a change of overlord. Evidence: Shi Xie page footnote 14: Shi Xie and his brothers submitted to Bu Zhi, sent by Sun Quan in Jian'an 15 (210). Fix: Retype as vassal_start, counterpart eastern-wu (ea-03, not yet run), with the 210 region; keep the 227 loss as the end.
- thin `/ledger/1`: Date of the seven-commandery decree and of the brothers' appointments (after 200). Page to try: https://en.wikipedia.org/wiki/Shi_Yi_(Han_dynasty)
- spot checks: /ledger/0 confirmed (187, Administrator of Jiaozhi); /ledger/1 confirmed (decree undated (confidence 1 honest)); /ledger/2 confirmed (Jian'an 15 (210) in footnote 14); /ledger/5 confirmed (227 executions; split into Jiao and Guang (no date for the split))
- area: no infobox area, no Cliopatria row.

### liang-province-rebels: pass

Tried and could not break: years, keyframe-ledger walk (187 gain explains K1), mirrors with han-dynasty (187 matched), han-sui and song-jian (189 split matched), capital inside the shape.

- spot checks: /ledger/0 confirmed ('The rebellion began in the winter of 184'; Jincheng the main stronghold); /ledger/2 confirmed ('For the first time, the rebels extended their sway over the entire Liang Province' (187)); /ledger/3 confirmed ('In spring 189, Wang Guo's men became worn out and abandoned the siege'); /ledger/4 confirmed ('finally splintered into three groups' after spring 189 (no explicit year on the page))
- area: no infobox area, no Cliopatria row.

### han-sui: fail

- **TO FIX** `/ledger/3, /ledger/5, /keyframe_review/1/correction`: 'Guanzhong' (the Wei valley round Chang'an) stands for Yong Province and is given to Han Sui 197-211, but Yong of 194-213 was the Hexi commanderies, and no page gives Han Sui or Ma Teng Chang'an or the Guanzhong. Evidence: Yong Province page: 'In AD 194, the Eastern Han government established a Yongzhou Inspectorate' over 'Wuwei, Zhangye, Jiuquan, Dunhuang, and Xihai ... west of the Liang River', seat Guzang; the Three Adjuncts joined it only in 213. Ma Teng page: they controlled Liang Province and tried and failed to seize Chang'an. End of the Han page (197): Cao Cao 'was able to persuade Ma Teng and Han Sui, who controlled Yong and Liang provinces' to submit. Fix: Drop region Guanzhong from /ledger/3, /ledger/5 and K1 (Hexi is already inside the Gansu admin1); make the 197 event a vassal_start cp han-dynasty (submission to the court) rather than a gain; keep the Baoji circle for Ma Teng's Wei-valley group if wanted. Tell ea-02-c that han-dynasty /ledger/98 (196 loss of Yong to han-sui) carries the same error.
- **TO FIX** `/keyframe_review/0-2/correction`: admin1 Gansu (189-215) contains song-jian's Fuhan (Linxia 80 km circle, 189-214): the two states overlap for 25 years. Evidence: song-jian.json /keyframe_review/0; Liang Province rebellion page: Song Jian 'ruled in isolated autonomy for almost thirty years' at Fuhan. Fix: Write K0-K2 as {"minus": [Gansu (and Baoji), Linxia 80 km circle]} for 189-214.
- **TO FIX** `/ledger/5/note`: The note quotes 'Ma Chao and Han Sui held Liang and Yong until 211' from the End of the Han page; the page has no such sentence. Evidence: End of the Han page: a coalition of north-western warlords 'who controlled Liang and Yong provinces, led by Ma Chao and Han Sui, was defeated by Cao Cao at the Battle of Tong Pass in 211'; their territories 'were annexed by Cao over the next few years'. Fix: Replace the quotation with the page's wording; the year 211 stands.
- **TO FIX** `/keyframe_review/1/correction`: Ningxia appears in K1 (197) with no event; K0 (189-196) lacks it although liang-province-rebels held it to 189. Evidence: Rule 4 keyframe walk. Fix: Either include Ningxia from 189 (as the rebels' successor) or add the event that brings it in.
- thin `/keyframe_review/2`: Extent 211-215 (confidence-1 shape) and Ma Chao's 212-214 campaign in Liang (siege of Jicheng). Page to try: https://en.wikipedia.org/wiki/Ma_Chao
- spot checks: /ledger/1 confirmed ('Early in 192, the two of them submitted ...'; defeat 'west of Chang'an'); /ledger/3 confirmed (197 submission confirmed; the land (Guanzhong for Yong) is wrong: see fixes); /ledger/4 confirmed ('Battle of Tong Pass in September 211'); /ledger/5 confirmed (year confirmed; the quotation in the note is not on the page); /ledger/7 confirmed (5th month of Jian'an 20 = 15 June to 13 July 215)
- area: no infobox area, no Cliopatria row.

### song-jian: pass

Tried and could not break: years, start vs 'almost thirty years' (flagged by the author), capital Linxia inside the shape; the overlap with han-sui is that dossier's fix.

- spot checks: /ledger/0 confirmed ('Song Jian's group in Fuhan' after spring 189 (confidence 2 honest)); /ledger/1 confirmed (Xiahou Yuan's 214 expedition; 'his capital of Fuhan was captured'); /ledger/2 confirmed
- area: no infobox area, no Cliopatria row.

### qiang: pass

Tried and could not break: years, 117 vs 118 (flagged by the author), contest pair mirrored in han-dynasty /ledger/78-79; note for the orchestrator: the slug 'qiang' names a whole people but the dossier is only Dianlian's 107-118 rebel state.

- spot checks: /ledger/0 confirmed ('In 107 CE, the Xianlian Qiang rebelled against Han authority'); /ledger/2 confirmed ('In 109 CE, he conquered Longxi'); /ledger/3 confirmed ('this First Great Qiang Rebellion was quelled in 118'); /ledger/5 confirmed (resettlement 'from 129 to 144')
- area: no infobox area, no Cliopatria row.

### chengjia: fix

- **APPLIED** `/ledger/3/confidence`: Wei Ao's submission to Gongsun Shu is dated 30 at confidence 3, but the page attaches no year to the submission (it follows the summer-30 campaign sentence). Evidence: Emperor Guangwu page: 'formally submitted to Gongsun and accepted a princely title - Prince of Shuoning - from him', no year on the sentence. Fix: Lowered to confidence 2 and tagged the note [Reviewer ea-02-x].
- thin `/ledger/2`: Whether Hou Dan's 26 attempt on Hanzhong succeeded (gain at confidence 1, K1 holds Hanzhong 26-36). Page to try: https://en.wikipedia.org/wiki/Hou_Dan
- spot checks: /ledger/0 confirmed ('in 24 proclaimed himself king of Shu'); /ledger/1 confirmed ('in 25 asserted independence by adopting the title of Emperor of Cheng'); /ledger/2 confirmed ('In 26, Gongsun Shu sent general Hou Dan to conquer the region of Hanzhong' (outcome not on page; confidence 1 honest)); /ledger/5 confirmed ('In 35, Emperor Guangwu ordered an army to conquer Chengjia'); /ledger/6 confirmed (December 36; died 24 December 36); /ledger/3 confirmed (submission confirmed, year not attached: confidence lowered)
- area: no infobox area, no Cliopatria row.

### wei-ao: fail

- **TO FIX** `/ledger (30, 34)`: No vassal tie to Chengjia, although chengjia /ledger/3 (vassal_start 30, cp wei-ao) and /ledger/4 (vassal_end 34) assert one: the mirror is missing in the same batch, from this dossier's only source. Evidence: Emperor Guangwu page: Wei 'formally submitted to Gongsun and accepted a princely title - Prince of Shuoning - from him'. Fix: Add vassal_start 30 (confidence 2) cp chengjia and vassal_end 34 cp chengjia, region as K0.
- **APPLIED** `/ledger/0/counterpart`: Counterpart 'lulin' for a 25 event; the lulin dossier ends in 23 (absorbed by the Gengshi Han, carried as han-dynasty). Evidence: lulin.json identity.end 23, /ledger/3 dissolve cp han-dynasty; xin-dynasty /ledger/7 (23) loss cp han-dynasty. Fix: Changed to han-dynasty and tagged the note.
- thin `/ledger/0`: Wei Ao's rise (23 in Tianshui), his nominal submission to Liu Xiu before 30, and extent beyond eastern Gansu (start at confidence 1). Page to try: https://en.wikipedia.org/wiki/Gengshi_Emperor
- spot checks: /ledger/1 confirmed ('in the summer of AD 30'); /ledger/2 confirmed ('In the winter of AD 34, Shuoning's capital Luomen ... fell, and Wei Chun surrendered'); /ledger/3 confirmed; /ledger/4 confirmed
- area: no infobox area, no Cliopatria row.

### dou-rong: thin

- thin `/ledger (29)`: Dou Rong's submission to the Eastern Han in 29 is on the page already cited but not in the ledger: add vassal_start 29 cp han-dynasty (vassal_end 36 with the handover). Page to try: https://en.wikipedia.org/wiki/Hexi_Corridor
- thin `/wars`: His part in Guangwu's 32 campaign against Wei Ao is not recorded (no land moved). Page to try: https://en.wikipedia.org/wiki/Emperor_Guangwu_of_Han
- spot checks: /ledger/0 confirmed ('came under the control of warlord Dou Rong' after the Xin collapse in 23 CE (footnote: from A.D. 24)); /ledger/1 confirmed ('turned over the lands under his control to Emperor Guangwu in AD 36'); /ledger/2 confirmed
- area: no infobox area, no Cliopatria row.

### liu-yong: fix

- **APPLIED** `/ledger/2/counterpart`: Counterpart 'lulin' for the 25 conquest of six commanderies; the lulin dossier ends in 23 (absorbed by the Gengshi Han, carried as han-dynasty). Evidence: lulin.json identity.end 23; Liu Yong page places the conquest under the Gengshi Emperor's reign. Fix: Changed to han-dynasty and tagged the note.
- thin `/keyframe_review/2`: Tanhai (Linyi 70 km) appears in 27 with no gain event; its location and when Liu Yong took it are not on the page. Page to try: https://en.wikipedia.org/wiki/Liu_Yong_(Xin_dynasty)
- thin `/ledger/2`: The six-commandery conquest (Zhou Jian) is undated (confidence 1), between 23 and 25 in the narrative. Page to try: https://en.wikipedia.org/wiki/Liu_Yong_(Xin_dynasty)
- spot checks: /ledger/0 confirmed (Prince of Liang, Suiyang, 23); /ledger/1 confirmed ('In AD 25 ... Liu Yong proclaimed himself emperor'); /ledger/4 confirmed ('In the spring of AD 27, Liu Yong named Zhang Bu as Prince of Qi'); /ledger/6 confirmed (Suiyang surrounded, Liu Yong killed by Qing Wu (27 implied, no month)); /ledger/7 confirmed ('during August AD 29, Liu Yu's Tanhai Commandery was captured')
- area: no infobox area, no Cliopatria row.

### zhang-bu: fail

- **TO FIX** `/ledger/1`: The 27 appointment as Prince of Qi by Liu Yong is typed 'rename', while liu-yong /ledger/4 and /ledger/5 record it as vassal_start/vassal_end with zhang-bu: the mirror is missing. Evidence: Liu Yong page: 'In the spring of AD 27, Liu Yong named Zhang Bu as Prince of Qi'; the dossier's own note says 'nominal vassalage to Liu Yong'. Fix: Retype /ledger/1 as vassal_start 27 cp liu-yong (region as K0) and add vassal_end 27 cp liu-yong at Liu Yong's death (liu-yong /ledger/5).
- **TO FIX** `/keyframe_review/0/correction and /ledger/0, /ledger/2, /ledger/3 regions`: admin1 Shandong (25-29) contains liu-yong's ground: south-west Shandong (Jiyin, Shanyang, inside liu-yong's Shangqiu 120 km circle, 25-26) and Tanhai (liu-yong's Linyi 70 km circle, 27-29). Evidence: Liu Yong page: his general attacked 'Jiyin, Shanyang, Pei, Chu, Huaiyang, and Runan Commanderies'; liu-yong.json /keyframe_review/1-2. Fix: Write the shape as {"minus": [Shandong, liu-yong's circles]} (split K0 at 27), or narrow it to Qi's commanderies of north and central Shandong.
- **APPLIED** `/ledger/0/counterpart`: Counterpart 'lulin' for a 25 event; the lulin dossier ends in 23. Evidence: lulin.json identity.end 23. Fix: Changed to han-dynasty and tagged the note.
- thin `/ledger/0`: Zhang Bu's rise (c. 23-25 in Langya and Qi), capital (Ju) and the 27-29 campaign (start at confidence 1). Page to try: https://en.wikipedia.org/wiki/Geng_Yan
- spot checks: /ledger/1 confirmed (spring 27, Prince of Qi); /ledger/2 confirmed ('surrendered and was created a marquess' (29); 'independently controlled the modern Shandong region'); /ledger/3 confirmed
- area: no infobox area, no Cliopatria row.

### peng-chong: fix

- **APPLIED** `/ledger/0/counterpart`: Counterpart 'lulin' for a 25 event; the lulin dossier ends in 23. Evidence: lulin.json identity.end 23; Peng Chong held Yuyang for the Gengshi and then the Eastern Han before his revolt. Fix: Changed to han-dynasty and tagged the note.
- thin `/ledger/0`: Start year: Peng Chong revolted against Liu Xiu in 26 and took the title Prince of Yan later; the Guangwu page dates neither (confidence 1 at 25). Page to try: https://en.wikipedia.org/wiki/Peng_Chong_(Han_dynasty)
- spot checks: /ledger/1 confirmed ('Also in AD 29, Peng's slaves assassinated him'); /ledger/2 confirmed; /ledger/0 confirmed (title Prince of Yan on the page with no year (confidence 1 honest))
- area: no infobox area, no Cliopatria row.

### lu-fang: thin

- **APPLIED** `/ledger/1/confidence`: The 42 loss gives Ordos and Hetao to the Xiongnu at confidence 3; the page says only that Lu Fang (by then the Han's Prince of Dai) fled to the Xiongnu. Evidence: Emperor Guangwu page: after initially submitting he was made 'the Prince of Dai' (no year) and 'eventually fled to Xiongnu in AD 42'. Fix: Lowered to confidence 2 and tagged the note; the counterpart stays for the gap-filler (see thin).
- thin `/ledger (c. 40)`: Lu Fang's submission to the Han and title Prince of Dai (c. 40): a vassal_start cp han-dynasty, and then the counterpart of the 42 loss (han-dynasty rather than xiongnu, which has no mirror). Page to try: https://en.wikipedia.org/wiki/Emperor_Guangwu_of_Han
- thin `/ledger/0`: Rise year and capital (Jiuyuan); the only source for 24 is a disambiguation entry with a red link ('fl. 24-41'). Page to try: https://en.wikipedia.org/wiki/Lu_Fang
- spot checks: /ledger/1 confirmed (year 42 confirmed; land to the Xiongnu not on page: confidence lowered); /ledger/0 confirmed (disambiguation page: 'Lu Fang (warlord) (fl. 24-41)', red link (confidence 1 honest))
- area: no infobox area, no Cliopatria row.

### zhang-chu: thin

- thin `/keyframe_review/0`: Territory beyond Chen County: the towns taken in 209 BC (Daze, Qi, Zhi, Cuo, Ku, Zhe, Qiao) and the fronts at Xingyang and in Zhao; only Chen is drawn. Page to try: https://en.wikipedia.org/wiki/Chen_Sheng_and_Wu_Guang_uprising
- spot checks: /ledger/0 confirmed (August or September 209 BC; King of Rising Chu 'only months after'; capital Chen); /ledger/1 confirmed ('assassinated by his guard Zhuang Jia in c.January 208 BC'; holder of Chen afterwards not on page (confidence 1 honest)); /ledger/2 confirmed
- area: no infobox area, no Cliopatria row.

### huainan: fix

- **APPLIED** `/ledger/0/counterpart`: The -203 found gives the land from han-dynasty, whose dossier starts in -202; the page has Ying Bu take Jiujiang from Chu. Evidence: Ying Bu page: Long Ju had conquered Jiujiang; 'later that year' (203 BC) Ying Bu 'led an army to attack Jiujiang and conquered many cities ... and persuaded Zhou Yin to defect from Chu to Han'. Fix: Changed to western-chu and tagged the note. The author should also add western-chu to identity.predecessors.
- thin `/ledger (-203)`: Huainan was a kingdom instated by Liu Bang: a vassal_start -203 cp kingdom-of-han (then han-dynasty from -202), ended by the -196 revolt, is missing. Page to try: https://en.wikipedia.org/wiki/Ying_Bu
- thin `/identity/predecessors`: western-chu (Jiujiang taken from Chu in -203) is not listed. Page to try: https://en.wikipedia.org/wiki/Ying_Bu
- spot checks: /ledger/0 confirmed (infobox King of Huainan c. August 203 BC; capital Lu; Jiujiang, Lushan, Hengshan, Yuzhang); /ledger/1 confirmed ('started a rebellion in August or September 196 BCE'); /ledger/2 confirmed (killed at Zi Village, Poyang; 12 Nov - 10 Dec 196 BC); /ledger/3 confirmed (Liu Chang installed as Prince of Huainan (no separate date))
- area: no infobox area, no Cliopatria row.

### changsha-kingdom: thin

- thin `/ledger (-202..-157)`: The dossier calls Changsha a Han vassal kingdom but carries no vassal_start -202 / vassal_end -157 with han-dynasty. Page to try: https://en.wikipedia.org/wiki/Changsha_Kingdom
- thin `/ledger/4`: Zhao Tuo 'twice invaded Changsha, occupying a few counties' (183 BC): a loss to nanyue (and the return) could replace the confidence-1 contest; the end year 179 is not on the Changsha page. Page to try: https://en.wikipedia.org/wiki/Nanyue
- spot checks: /ledger/0 confirmed (King of Hengshan 'one year later' after 207 BC; Eighteen Kingdoms row: 'eastern Hubei, Jiangxi'); /ledger/1 confirmed (Hengshan and Yuzhang under Huainan in 203 BC); /ledger/3 confirmed ('in 203 or 202 BC'; 'present-day Hunan and some surrounding areas'); /ledger/6 confirmed ('dying in 157 BC without male issue'; 'In 155 BC, the kingdom was reestablished')
- area: no infobox area, no Cliopatria row.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| yuan-shao 193 gain > gongsun-zan | - | missing | gongsun-zan draws no Qing; fix in gongsun-zan (thin) or note the exception |
| yuan-shao 199 gain > gongsun-zan | gongsun-zan 199 loss | matched |  |
| yuan-shu 195 vassal_start > sun-ce | - | missing | sun-ce has no vassal events; fix listed under sun-ce |
| yuan-shu 197 vassal_end > sun-ce | - | missing | as above |
| chengjia 30 vassal_start > wei-ao | - | missing | wei-ao has no vassal events; fix listed under wei-ao |
| chengjia 34 vassal_end > wei-ao | wei-ao 34 loss | mismatch | wei-ao has the 34 loss to han-dynasty but no vassal_end |
| liu-yong 27 vassal_start > zhang-bu | zhang-bu 27 rename | mismatch | zhang-bu types it rename; fix listed under zhang-bu |
| liu-yong 27 vassal_end > zhang-bu | - | missing | as above |
| changsha-kingdom -203 loss > huainan | huainan -203 found | matched | huainan found covers Hengshan and Yuzhang |
| han-sui 189 found > liang-province-rebels | liang-province-rebels 189 dissolve | matched |  |
| song-jian 189 found > liang-province-rebels | liang-province-rebels 189 dissolve | matched |  |
| yellow-turbans 184 found > han-dynasty | - | missing | route to ea-02-c (han-dynasty has no event) |
| yellow-turbans 184 gain > han-dynasty | - | missing | route to ea-02-c (han-dynasty has no event) |
| yellow-turbans 185 loss > han-dynasty | - | missing | route to ea-02-c (han-dynasty has no event) |
| yuan-shao 191 found > han-dynasty | han-dynasty 191 loss | matched |  |
| yuan-shao 196 gain > han-dynasty | han-dynasty 196 loss | matched |  |
| yuan-shao 199 gain > han-dynasty | - | missing | route to ea-02-c (han-dynasty has no event) (Bing Province) |
| yuan-shao 204 loss > cao-cao | han-dynasty 207 gain | mismatch | yuan-shao gives Ye/Bing (204) and Qing (205) to cao-cao (ea-03, not run); han-dynasty /ledger/102 gains the Yuan lands from yuan-shao in 207. ea-02-c and ea-03 must agree who receives the land and when |
| gongsun-zan 193 found > han-dynasty | han-dynasty 193 loss | matched |  |
| yuan-shu 189 found > han-dynasty | han-dynasty 191 loss | mismatch | han-dynasty /ledger/90 loses the Huai country to yuan-shu in 191; yuan-shu holds Nanyang from 189 and gains the Huai only in 193 (Yuan Shu page). Route to ea-02-c |
| yuan-shu 192 gain > han-dynasty | - | missing | route to ea-02-c (han-dynasty has no event) (Chenliu) |
| yuan-shu 193 gain > han-dynasty | han-dynasty 191 loss | mismatch | 2 years apart; as above |
| yuan-shu 193 loss > cao-cao | - | exception | counterpart owned by ea-03, not yet run |
| yuan-shu 192 loss > nobody | - | exception | nobody |
| yuan-shu 199 loss > nobody | - | exception | nobody |
| liu-biao 190 found > han-dynasty | han-dynasty 190 loss | matched |  |
| liu-biao 208 loss > cao-cao | - | exception | counterpart owned by ea-03, not yet run |
| liu-zhang 188 found > han-dynasty | han-dynasty 188 loss | matched |  |
| liu-zhang 214 loss > shu-han | - | exception | counterpart owned by ea-03, not yet run (Liu Bei before 221: shu-han or a liu-bei dossier) |
| zhang-lu 194 found > han-dynasty | han-dynasty 194 loss | matched |  |
| zhang-lu 215 loss > cao-cao | - | exception | counterpart owned by ea-03, not yet run |
| sun-ce 195 found > han-dynasty | han-dynasty 195 loss | matched |  |
| sun-ce 197 gain > han-dynasty | han-dynasty 196 loss | matched |  |
| sun-ce 199 gain > Liu Xun (Lujiang) and the Han governors of Yuzhang | - | exception | free-text counterpart, no dossier; listed in counterparts_needing_dossiers |
| shi-xie 187 found > han-dynasty | - | missing | route to ea-02-c (han-dynasty has no event) |
| shi-xie 207 gain > han-dynasty | - | missing | route to ea-02-c (han-dynasty has no event) |
| shi-xie 227 loss > eastern-wu | - | exception | counterpart owned by ea-03, not yet run |
| liang-province-rebels 184 found > han-dynasty | - | missing | route to ea-02-c (han-dynasty has no event) |
| liang-province-rebels 187 gain > han-dynasty | han-dynasty 187 loss | matched |  |
| han-sui 197 gain > han-dynasty | han-dynasty 196 loss | mismatch | years match, but both sides put Yong in the Guanzhong; Yong of 194-213 was the Hexi commanderies (Yong Province page): fix in han-sui, and ea-02-c should correct /ledger/98 |
| han-sui 211 loss > cao-cao | han-dynasty 211 gain | mismatch | han-dynasty /ledger/103 gains from han-sui; han-sui loses to cao-cao (ea-03): same land, two receivers |
| song-jian 214 loss > cao-cao | - | exception | counterpart owned by ea-03, not yet run |
| qiang 107 found > han-dynasty | han-dynasty 107 contest_start | missing | han-dynasty has only the contest pair (107/118), no loss of Hanyang; route to ea-02-c |
| qiang 109 gain > han-dynasty | - | missing | route to ea-02-c (han-dynasty has no event) (Longxi) |
| qiang 118 loss > han-dynasty | - | missing | route to ea-02-c (han-dynasty has no event) |
| chengjia 24 found > xin-dynasty | - | missing | xin-dynasty ends 23/10 with its land to han-dynasty; no chengjia event. Route to ea-02-c |
| chengjia 26 gain > nobody | - | exception | nobody |
| chengjia 36 loss > han-dynasty | han-dynasty 36 gain | matched |  |
| wei-ao 25 found > han-dynasty | - | missing | route to ea-02-c (han-dynasty has no event) (counterpart changed from lulin by the reviewer) |
| wei-ao 34 loss > han-dynasty | han-dynasty 34 gain | matched |  |
| dou-rong 23 found > xin-dynasty | - | missing | xin-dynasty has no dou-rong event; route to ea-02-c |
| dou-rong 36 loss > han-dynasty | han-dynasty 36 gain | matched |  |
| liu-yong 23 found > lulin | - | missing | lulin (ends 23) has no liu-yong event; route to ea-02-c |
| liu-yong 25 gain > han-dynasty | - | missing | route to ea-02-c (han-dynasty has no event) (counterpart changed from lulin by the reviewer) |
| liu-yong 27 loss > han-dynasty | han-dynasty 29 gain | mismatch | han-dynasty /ledger/54 gains Liu Yong's land in 29; Suiyang fell in 27 (Liu Yong page), Tanhai in August 29. ea-02-c should split its event |
| zhang-bu 25 found > han-dynasty | - | missing | route to ea-02-c (han-dynasty has no event) |
| zhang-bu 29 loss > han-dynasty | han-dynasty 29 gain | matched |  |
| peng-chong 25 found > han-dynasty | - | missing | route to ea-02-c (han-dynasty has no event) |
| peng-chong 29 loss > han-dynasty | han-dynasty 29 gain | matched |  |
| lu-fang 24 found > xin-dynasty | - | missing | xin-dynasty ended 23; no event; route to ea-02-c |
| lu-fang 42 loss > xiongnu | - | mismatch | xiongnu (ia-01) has no 42 gain, and the page does not give the land to the Xiongnu (Lu Fang had submitted to the Han as Prince of Dai); counterpart likely han-dynasty |
| zhang-chu -209 found > qin-dynasty | - | missing | qin-dynasty has no zhang-chu event (its -209 loss is to yan); route to the qin-dynasty group |
| zhang-chu -208 loss > qin-dynasty | - | missing | as above |
| huainan -203 found > western-chu | western-chu -203 gain | mismatch | counterpart changed to western-chu by the reviewer; western-chu /ledger/8 instead gains Jiujiang in -203 (c1) and records no loss to huainan. Route to ea-02-b |
| huainan -196 loss > han-dynasty | - | missing | route to ea-02-c (han-dynasty has no event) (Liu Chang's Huainan is a Han vassal inside the Han shape) |
| changsha-kingdom -206 found > western-chu | - | missing | western-chu has no Hengshan event in -206; route to ea-02-b |
| changsha-kingdom -202 gain > han-dynasty | - | missing | route to ea-02-c (han-dynasty has no event); a vassal tie is the better model (thin) |
| changsha-kingdom -183 contest_start > nanyue | nanyue -183 contest_start | matched | nanyue and han-dynasty carry the same war with han-dynasty as counterpart |

Gazetteer names needed (text only in the dossiers): Bazhong, Julu, Luomen, Yijing, Shouchun, Fuhan.
