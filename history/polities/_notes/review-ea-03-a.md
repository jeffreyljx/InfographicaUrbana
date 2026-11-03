# Review: batch ea-03-a (cao-cao, shu-han, cao-wei, eastern-wu, western-jin)

Reviewer: Phase B adversarial review, 2026-10-19. The machine copy is history/notes/phase-b/reviews/ea-03-a.json.

Method: validator with --resolve on all five (0 errors, 0 warnings); ledgers, keyframes, identity and wars read by script; mirrors looked up in every existing counterpart dossier (yuan-shao, liu-biao, liu-zhang, han-sui, zhang-lu, sun-ce, gongsun-liaodong, shi-xie, lelang-commandery, han-dynasty, goguryeo, champa, xianbei, protectorate-of-the-western-regions). The Sixteen Kingdoms states (cheng-han, former-zhao, later-zhao, former-yan, former-liang, former-qin, later-yan, southern-yan, later-qin, xia, liu-song-dynasty) have no dossier yet: their counterparts count as exceptions. Pages opened: Three Kingdoms, Cao Cao, Shu Han, Cao Wei, Gongsun Yuan, Sun Quan, Shi Xie, Eastern Wu, Conquest of Wu by Jin, Conquest of Shu by Wei, Jin dynasty (266-420), Sixteen Kingdoms, Emperor Wu of Liu Song, Cheng-Han, Battle of Fei River.

## Verdicts

### cao-cao: pass

Area: infobox None (None), Cliopatria 1377126, ratio None. No area in the Cao Cao infobox (fief described as parts of Hebei and Henan); confirmed by the reviewer.

Gaps for a gap-filler:
- `/ledger/5`: Bing Province 205 is confidence 1 and its note says the page is silent; the Cao Cao page is not: it has Gao Gan, who had surrendered and rebelled, beaten at Hu Pass in spring 206. Cite that sentence and settle 204/205 (yuan-shao dates the surrender to 204). Page to try: https://en.wikipedia.org/wiki/Gao_Gan
- `/ledger/19`: Liang Province (Hexi, 1,088 Gansu cells) in 215 rests on Cliopatria alone (confidence 1); need a page that dates the submission of Liang after Tong Pass. Page to try: https://en.wikipedia.org/wiki/Han_Sui

Spot checks:
- `/ledger/3` (https://en.wikipedia.org/wiki/Cao_Cao): confirmed: 'Between spring and autumn in 204, Cao Cao attacked Yuan Shang in his base at Ye and conquered the city'
- `/ledger/10` (https://en.wikipedia.org/wiki/Three_Kingdoms): confirmed: 'In 209, Zhou Yu captured Jiangling' (the note's quote is a paraphrase)
- `/ledger/13` (https://en.wikipedia.org/wiki/Three_Kingdoms): confirmed: 211, Battle of Huayin, 'capturing the territory around Chang'an' (note's quote is a paraphrase)
- `/ledger/17` (https://en.wikipedia.org/wiki/Three_Kingdoms): confirmed: 'In 215, Cao Cao captured Hanzhong after attacking and receiving the surrender of Zhang Lu'
- `/ledger/22` (https://en.wikipedia.org/wiki/Three_Kingdoms): confirmed: 'In 219, Liu Bei seized Hanzhong by defeating and killing General Xiahou Yuan'
- `/ledger/15 and /ledger/20` (https://en.wikipedia.org/wiki/Cao_Cao): confirmed: Duke of Wei 213, King of Wei 216 (infobox); Three Kingdoms page has 214 and 217, flagged by the author

### shu-han: thin

Area: infobox None (None), Cliopatria 880369, ratio None. Infobox gives population only (221: 900,000; 263: 1,082,000); no area.

Gaps for a gap-filler:
- `/keyframe_review/0, /keyframe_review/1, /keyframe_review/2, /ledger/10`: Jiangling 210-219: the Three Kingdoms page (already a source) says that after Zhou Yu's death in 210 'Sun Quan was forced to cede the territory around Jiangling to Liu Bei', and that in 219 Lu Meng sailed up the Yangtze 'towards Jiangling ... resulting in its capture'. Add a 210 gain (counterpart eastern-wu), put Jiangling in the 209 (from 210), 214 and 215 shapes, and include it in the 219 loss region. Page to try: https://en.wikipedia.org/wiki/Three_Kingdoms
- `/ledger (228-234)`: Wudu and Yinping: the Shu Han page lists 'the Wudu and Yinping commanderies' among the gains of the Northern Expeditions (228-234) without a year; add the gain (counterpart cao-wei; traditionally 229, needs a page) once a page dates it. Page to try: https://en.wikipedia.org/wiki/Zhuge_Liang%27s_Northern_Expeditions
- `/identity/capitals`: No capital for 209-213 (Liu Bei's seat before Chengdu). Page to try: https://en.wikipedia.org/wiki/Liu_Bei
- `/ledger/0`: The 209 found names liu-biao, but liu-biao's ledger hands all of Jing ('Hubei and Hunan') to cao-cao in 208-9; the southern commanderies submitted to Cao Cao in 208. Either the counterpart becomes cao-cao or liu-biao/cao-cao settle the southern Jing land. Page to try: https://en.wikipedia.org/wiki/Three_Kingdoms

Spot checks:
- `/ledger/2` (https://en.wikipedia.org/wiki/Three_Kingdoms): confirmed: 'In the summer of 214, Liu Bei received the surrender of Liu Zhang, capturing Yi Province'
- `/ledger/7` (https://en.wikipedia.org/wiki/Shu_Han): confirmed: 'wrestled control of Hanzhong from his rival, Cao Cao, in 219'
- `/ledger/10` (https://en.wikipedia.org/wiki/Shu_Han): confirmed: 'Liu Bei lost his territories in Jing Province to Sun Quan' (alliance broken in 219)
- `/ledger/12` (https://en.wikipedia.org/wiki/Three_Kingdoms): confirmed: 'On 15 May 221, Liu Bei responded by proclaiming himself as the Emperor of Han'
- `/ledger/15` (https://en.wikipedia.org/wiki/Shu_Han): confirmed: 'launched an expeditionary force there in 225 to quell local rebellions'
- `/ledger/20` (https://en.wikipedia.org/wiki/Conquest_of_Shu_by_Wei): confirmed: Chengdu falls in the window 18 November - 17 December 263; Shu Han infobox c. Dec 263

### cao-wei: thin

Area: infobox None (None), Cliopatria 2092804, ratio None. Infobox gives population 4,432,881 (260, disputed); no area.

Fixes:
- `/ledger/5, /ledger/21` (for the author): The Western Regions vassal pair names protectorate-of-the-western-regions as the vassal, but that (ea-02) dossier draws nothing for 176-334 and says the Tarim of 224-305 is drawn by the Cao Wei and Western Jin shapes; the protectorate is the Chinese office itself, not a vassal state. Non-blocking (confidence 1, flagged by the author). Evidence: Protectorate dossier keyframe _197: 'For 224-305 Cliopatria draws the Tarim inside its Cao Wei and Western Jin shapes ... this dossier adds nothing there'; its ledger has a 176 loss and a 335 gain, nothing between. Chief Official page: 're-established and maintained by the Cao Wei and the Western Jin until around 328'. Fix: Either restore the Tarim to the cao-wei_224/_238/_263 corrections and drop the pair, or keep the tint with the Tarim oasis states as counterpart (no dossier: list it) and tell ea-02; agree one model with western-jin.

Gaps for a gap-filler:
- `/ledger (228-234)`: Loss of Wudu and Yinping to Shu during the Northern Expeditions (mirror of the missing shu-han gain). Page to try: https://en.wikipedia.org/wiki/Zhuge_Liang%27s_Northern_Expeditions
- `/ledger/5`: Western Regions start year 224 is Cliopatria's (confidence 1). Page to try: https://en.wikipedia.org/wiki/Chief_Official_of_the_Western_Regions
- `/ledger`: Xianbei (Kebineng) and Wuhuan frontier events; none read. Page to try: https://en.wikipedia.org/wiki/Kebineng

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Cao_Wei): confirmed: 'Abdication of Emperor Xian of Han: 11 December 220 AD'
- `/ledger/1` (https://en.wikipedia.org/wiki/Sun_Quan): confirmed: Sun Quan a Wei vassal after Liu Bei's proclamation in 221; 'on 23 September 221 he appointed Sun Quan the King of Wu'
- `/ledger/7` (https://en.wikipedia.org/wiki/Gongsun_Yuan): confirmed: 'In 228, a grown-up Gongsun Yuan seized power'; infobox Administrator of Liaodong 228, monarch Cao Rui
- `/ledger/14` (https://en.wikipedia.org/wiki/Gongsun_Yuan): confirmed: siege 3 Sep / fall 19 Sep 238; 'Liaodong and present-day northwest Korea became Wei territories'
- `/ledger/19` (https://en.wikipedia.org/wiki/Conquest_of_Shu_by_Wei): confirmed: infobox 'Cao Wei victory; Fall of Shu Han', late 263
- `/ledger/22` (https://en.wikipedia.org/wiki/Cao_Wei): confirmed: 'Abdication of Cao Huan: 4 February 266 AD'

### eastern-wu: thin

Area: infobox None (None), Cliopatria 1399547, ratio None. Infobox gives population only (238: 2,567,000; 280: 2,535,000); no area.

Fixes:
- `/ledger/5, /ledger/16, /ledger/17, /ledger/18, /ledger/19, /wars (Lu Dai's reconquest of Jiaozhi)` (APPLIED by reviewer): Counterpart strings 'Shi Xie (Jiaozhi)' and 'Shi Hui (Jiaozhi)' replaced by the slug shi-xie. Evidence: history/polities/shi-xie.json exists (written 08:09, before this dossier) and carries the mirror events: vassal_start 210, vassal_end 227, loss 227, all with counterpart eastern-wu. Fix: counterpart: shi-xie (6 occurrences)
- `/ledger/5/source` (APPLIED by reviewer): The 210 vassal_start (confidence 3) cited the Sun Quan page, which gives no year for Bu Zhi's appointment; the year comes from the Shi Xie page. Evidence: Sun Quan page: Bu Zhi appointed Inspector after Zhou Yu died in 210, no year. Shi Xie page: 'Shi Xie led his followers to submit to Bu Zhi's governorship', footnote 14 Jian'an 15 = 210. Fix: source: https://en.wikipedia.org/wiki/Shi_Xie (already in sources)
- `/ledger (221-9 and 222-11)` (for the author): No vassal_start/vassal_end with cao-wei, although cao-wei carries both and this dossier's own rename notes say Wu was 'nominally Wei's vassal until November 222'. Non-blocking. Evidence: Eastern Wu page: Wu was a vassal state under Cao Wei from 220 to 222; Sun Quan page: King of Wu 23 September 221, independence November 222. Fix: Add vassal_start 221-9 and vassal_end 222-11, counterpart cao-wei, region as cao-wei /ledger/1, source Sun_Quan, confidence 3.

Gaps for a gap-filler:
- `/keyframe_review/1, /keyframe_review/2, /ledger (210)`: Jiangling ceded to Liu Bei after Zhou Yu's death in 210 and retaken by Lu Meng in 219 (Three Kingdoms page, a source here). eastern-wu_209 should hold Jiangling for 209 only, 210-218 without it, and the 219 gain should include it. Add a 210 loss (counterpart shu-han). Page to try: https://en.wikipedia.org/wiki/Three_Kingdoms
- `/ledger (248)`: The champa dossier (se-01) has a 248 gain of 'most of Rinan' from eastern-wu (confidence 2); this ledger has no matching loss and the Eastern Wu page lists Rinan as a Wu commandery without Linyi. Settle with se-01. Page to try: https://en.wikipedia.org/wiki/L%C3%A2m_%E1%BA%A4p
- `/ledger/0`: Found 207 is Cliopatria's year (confidence 1); Sun Quan inherited Jiangdong in 200 and the sun-ce dossier (195-206) asks ea-03 whether eastern-wu should start in 195/200. Orchestrator decision. Page to try: https://en.wikipedia.org/wiki/Sun_Ce
- `/ledger/1`: liu-biao has no loss of Jiangxia to eastern-wu in 208 (it hands all of Jing to cao-cao). Page to try: https://en.wikipedia.org/wiki/Huang_Zu

Spot checks:
- `/ledger/5` (https://en.wikipedia.org/wiki/Shi_Xie): confirmed after source fix: Jian'an 15 (210) footnote on the Shi Xie page; the cited Sun Quan page has no year
- `/ledger/8` (https://en.wikipedia.org/wiki/Eastern_Wu): confirmed: 219, Lu Meng invades Jing; domain extended to 'the southern part of Jing Province, which covered roughly present-day Hunan and parts of Hubei'
- `/ledger/18` (https://en.wikipedia.org/wiki/Shi_Xie): confirmed: 'In 227, when Shi Hui learnt about the new arrangements, he refused to comply'; executed by Lu Dai in 227
- `/ledger/24` (https://en.wikipedia.org/wiki/Eastern_Wu): confirmed: 'In 248, the people of Jiaozhi and Jiuzhen commanderies rebelled'
- `/ledger/29` (https://en.wikipedia.org/wiki/Conquest_of_Wu_by_Jin): confirmed: 'On 3 April 280, Du Yu managed to break through Wu Yan's defences and conquer Jiangling County'
- `/ledger/31` (https://en.wikipedia.org/wiki/Conquest_of_Wu_by_Jin): confirmed: 'Sun Hao would issue his final imperial edict the very next day, 1 May 280'

### western-jin: fail

Area: infobox 3100000 (280), Cliopatria 2972633, ratio 0.96. Cliopatria's shape alive in 280 is western-jin_265 (2,972,633; ratio 0.96); the author's 280 shape is western-jin_283 (4,372,893; ratio 1.41, stated as 0.71 the other way round). 347: infobox 2,800,000 against western-jin_347 2,339,997 (0.84). Within a factor of two, acknowledged.

Fixes:
- `/keyframe_review/20, /keyframe_review/21, /ledger/48` (for the author): Sichuan 405-412 is drawn as Jin although the cited page dates Western Shu's secession; the confidence-3 gain of 413 takes back land the keyframes already give to Jin (no trace in the keyframes, large). Blocking. Evidence: Emperor Wu of Liu Song page (a source here): 'In spring 405, Mao Qu's soldiers' rebelled and Qiao Zong established an independent Western Shu; Zhu Lingshi took Chengdu 'in 413 and annexing Western Shu back into Jin'. The KF20 note's 'the page does not date its start' is wrong. Fix: Add a 405 loss of Sichuan and Chongqing (counterpart western-shu, listed as needing a dossier); new keyframe western-jin_405 (the 402 shape minus Sichuan/Chongqing) for 405-409; western-jin_410 adjust to hold 410-412 without Sichuan and a new keyframe western-jin_413 (the 410 shape) from 413; fix the KF20/KF21 notes.
- `/ledger/25` (for the author): vassal_end of the Murong (former-yan) dated 337 at confidence 3, but the quoted page says the Murong were then still Jin vassals; the break is 352. Mis-dated confidence-3 event. Blocking. Evidence: Sixteen Kingdoms page: 'In 337, while still claiming to be a vassal of Jin, their chieftain, Murong Huang took the title of Prince'; 'In 352 ... Murong Jun thereupon broke away from the Eastern Jin and proclaimed himself as emperor.' Fix: Year 352, note quoting the 352 sentence, move the event after the 347 events; change 'until 337' to 'until 352' in the /keyframe_review/8 note.
- `/ledger/21, /keyframe_review/8/note` (for the author): The quote 'The Eastern Jin lost the north to the Sixteen Kingdoms' is on neither the Jin page nor the Sixteen Kingdoms page; the counterpart later-zhao was founded only in 319. Evidence: Jin page has no such sentence; its infobox has 'Eastern Jin begins; evacuation south of the Huai River: 317'. Sixteen Kingdoms page: Shi Le founded Later Zhao in 319. Fix: Quote the Jin infobox line and cite the Jin URL; counterpart former-zhao (Shi Le was Han-Zhao's general until 319), keep confidence 1.
- `/ledger/1, /ledger/10` (for the author): Western Regions vassal pair: counterpart protectorate-of-the-western-regions holds no land 176-334 in its own dossier, which expects the Wei and Jin shapes to draw the Tarim; the 306 end contradicts the cited page ('until around 328'), and 306-334 the Tarim is drawn by nobody. Evidence: Protectorate dossier keyframes _197 and _306 and its ledger (176 loss, 335 gain); Chief Official page 'maintained by the Cao Wei and the Western Jin until around 328'. Fix: Same model as cao-wei (restore the Tarim to the shapes, or Tarim oasis states as counterpart), end about 328 at confidence 1, coordinate with ea-02.
- `/identity/predecessors` (for the author): eastern-wu is missing: eastern-wu lists western-jin as its successor and its land passes to Jin in 280. Evidence: eastern-wu /identity/successors; /ledger/3-5 gains from eastern-wu. Fix: Add {slug: eastern-wu, land: Wu's Yang, Jing, Jiao and Guang provinces, 280}.
- `/keyframe_review/10/note` (for the author): Says Hebei, Shandong, Liaoning and the Huai country 'go to Former Yan' in 337; in 337 most of the north was Later Zhao's. Evidence: Sixteen Kingdoms page: Shi Le destroyed Han-Zhao in 329, 'placing most of northern China under his control'; Former Yan took Hebei only around 352 ('In 352, his brother, Murong Ke defeated and captured Ran Min'). Fix: Name Later Zhao (and Former Yan for Liaoning) in the note.
- `/identity/rulers` (for the author): Gap 311-313 between Huai (to 311) and Min (from 313). Evidence: Huai was taken with Luoyang in 311 (Disaster of Yongjia, /ledger/13); Min reigns from 313 (Jin page table). Fix: Extend Huai to the date of his death if the Han-Zhao page gives it, or note the interregnum.

Gaps for a gap-filler:
- `/ledger/40, /ledger/41, /ledger/42`: Later Yan / Former Qin transfers of 387, 390 and 394 are Cliopatria's (confidence 1, 'unverified: page budget'). Page to try: https://en.wikipedia.org/wiki/Later_Yan
- `/ledger/16`: Daifang 314 (confidence 2): goguryeo has no matching gain; goguryeo's 313 Lelang gain names lelang-commandery, not western-jin. Page to try: https://en.wikipedia.org/wiki/Daifang_Commandery
- `/ledger/23`: Murong vassal start 317 (confidence 1). Page to try: https://en.wikipedia.org/wiki/Murong_Hui
- `/wars (Sun En's rebellion)`: Extent of Sun En's rebels (399-402, Lu Xun after him); Wang Dun's and Su Jun's rebellions are named on the Jin page without years or land. Page to try: https://en.wikipedia.org/wiki/Sun_En
- `/ledger (347)`: champa has a 347 gain of northern Rinan from western-jin (confidence 1); no matching loss here. Page to try: https://en.wikipedia.org/wiki/L%C3%A2m_%E1%BA%A4p

Spot checks:
- `/ledger/5` (https://en.wikipedia.org/wiki/Conquest_of_Wu_by_Jin): confirmed: 1 May 280
- `/ledger/8` (https://en.wikipedia.org/wiki/Cheng-Han): confirmed: 'In 304, Li Xiong ousted Luo Shang from Chengdu, where he declared himself the King of Chengdu'
- `/ledger/17` (https://en.wikipedia.org/wiki/Cheng-Han): confirmed: 'in 314, a group of rebelling refugees in Hanzhong surrendered the region to Cheng'
- `/ledger/21` (https://en.wikipedia.org/wiki/Jin_dynasty_(266%E2%80%93420)): not on page (quote); the event is supported by the infobox 'Eastern Jin begins; evacuation south of the Huai River: 317' (confidence 1)
- `/ledger/25` (https://en.wikipedia.org/wiki/Sixteen_Kingdoms): mis-dated: the page has the Murong still Jin vassals in 337 and breaking away in 352
- `/ledger/27` (https://en.wikipedia.org/wiki/Cheng-Han): confirmed: 'in 347, he reached Chengdu and forced Li Shi to surrender'
- `/ledger/35, /ledger/36` (https://en.wikipedia.org/wiki/Battle_of_Fei_River): confirmed: 'in 373 seized modern Sichuan and Chongqing from Jin'; 'In 379, the strategically important city of Xiangyang ... fell to Qin'
- `/ledger/46` (https://en.wikipedia.org/wiki/Emperor_Wu_of_Liu_Song): confirmed: 'In spring 410, Liu Yu captured Guanggu, ending Southern Yan'
- `/ledger/48` (https://en.wikipedia.org/wiki/Emperor_Wu_of_Liu_Song): confirmed for 413, but the same page dates the secession to spring 405 (see fixes)
- `/ledger/53` (https://en.wikipedia.org/wiki/Sixteen_Kingdoms): confirmed: 'Helian Bobo took the opportunity to seize the Guanzhong region as Liu Yu returned to the south in 418'

## Cross-dossier matrix (unmatched and disputed rows only; full list in the JSON)

- cao-cao 208 gain / liu-biao -> liu-biao 208 loss: mismatch. land: liu-biao loses all of Jing ('Hubei and Hunan') to cao-cao; cao-cao gains only northern Jing (Nanyang, Xiangyang). Southern Jing 208-209 is nobody's; shu-han then founds from liu-biao in 209 and eastern-wu gains Jiangxia from liu-biao in 208, neither mirrored in liu-biao.
- yuan-shu 193 loss / cao-cao -> none: mismatch. yuan-shu loses Chenliu to cao-cao in 193, but cao-cao starts in October 196; route to the yuan-shu author: counterpart han-dynasty, or the orchestrator decides whether cao-cao starts in 192.
- shu-han 209 found / liu-biao -> liu-biao 208 dissolve: mismatch. liu-biao dissolves to cao-cao with all of Jing; the Xiang commanderies Liu Bei took in 209 had submitted to Cao Cao in 208.
- zhang-lu 215 gain / shu-han -> none: missing. zhang-lu has Bazhong gained from shu-han in 215 (confidence 1); shu-han has no loss. Route to zhang-lu's author.
- cao-wei 221 vassal_start / eastern-wu -> none: missing. eastern-wu has no vassal_start with cao-wei (only a rename note); same batch, fix listed under eastern-wu
- cao-wei 222 vassal_end / eastern-wu -> none: missing. as above, November 222
- cao-wei 224 vassal_start / protectorate-of-the-western-regions -> protectorate-of-the-western-regions 176 loss: mismatch. protectorate (ea-02) draws nothing 176-334 and expects the Wei/Jin shapes to draw the Tarim 224-305; cao-wei subtracts it and tints it as the protectorate's vassalage. Land falls through. Agree one model.
- cao-wei 266 vassal_end / protectorate-of-the-western-regions -> none: mismatch. as above
- cao-wei 228 vassal_start / gongsun-liaodong -> none: missing. gongsun-liaodong has no vassal_start with cao-wei 228 (Gongsun Yuan, Administrator of Liaodong under Cao Rui, Gongsun Yuan page). Route to gongsun-liaodong's author.
- cao-wei 237 vassal_end / gongsun-liaodong -> none: missing. as above (King of Yan, 237)
- eastern-wu 208 gain / liu-biao -> none: missing. liu-biao has no loss of Jiangxia to eastern-wu (see the 208 liu-biao mismatch)
- champa 248 gain / eastern-wu -> none: missing. champa (se-01) gains 'most of Rinan' from eastern-wu in 248 (confidence 2); eastern-wu has no loss
- champa 347 gain / western-jin -> none: missing. champa gains northern Rinan from western-jin in 347 (confidence 1); western-jin has no loss
- western-jin 266 vassal_start / protectorate-of-the-western-regions -> none: mismatch. as for cao-wei 224; the 306 end also contradicts the cited Chief Official page ('until around 328')
- western-jin 313 loss / goguryeo -> goguryeo 313 gain: mismatch. goguryeo names lelang-commandery as the counterpart; lelang-commandery (a colony dossier to 313) also draws Lelang 238-313 as its own while cao-wei and western-jin shapes include it. Compiler: one owner for Lelang.
- western-jin 314 loss / goguryeo -> none: missing. Daifang; no 314 gain in goguryeo
- western-jin 413 gain / Western Shu (Qiao Zong) -> none: mismatch. no dossier (listed), and this dossier has no 405 loss to it: the gain takes back land the dossier never lost (fix listed)

## Counterparts needing dossiers

- Western Shu (Qiao Zong): western-shu [405, 413]
- Wuhuan confederation (Liaoxi): wuhuan [207, 207]
- Nanzhong rebels (Yong Kai and the tribal chiefs): nanzhong-rebels [222, 225]
- Yao Xiang's Luoyang: yao-xiang [356, 356]
- Sun En's rebels: sun-en-rebellion [399, 402]
- Tarim oasis states (only if the Western Regions tint keeps a vassal counterpart): tarim-city-states [224, 328]

## Problems and decisions for the orchestrator

- Not a problem of these dossiers alone: shi-xie.json exists (08:09), so the author's counterparts_needing_dossiers entry for Shi Xie is obsolete; the reviewer changed eastern-wu's counterparts to shi-xie.
- Notes in all five dossiers put short paraphrases of the Three Kingdoms page in quotation marks ('Zhou Yu captures Jiangling', 'Cao Cao wins at Huayin, taking the Chang'an area'); the page's prose says the same with the same years, but the wording is not the page's.
- Orchestrator decisions pending: whether eastern-wu starts 195/200 (sun-ce dossier asks), whether cao-cao or han-dynasty draws 196-220, whether Western Jin is split at 317, and who owns Lelang 238-313 (lelang-commandery vs cao-wei/western-jin) and the Tarim 224-334 (protectorate vs cao-wei/western-jin).
- Page budget for western-jin is 9 (19 Cliopatria shapes); the 405 secession is on a page the author already opened, so it is not a budget gap.
- No page failed to load. The Western_Jin_dynasty URL listed in western-jin sources returns the Jin dynasty article (author noted).

## What I tried and could not break

- Every confidence-3 event spot-checked in cao-cao, shu-han, cao-wei and eastern-wu is on its page with its year (one source URL corrected in eastern-wu). The author's date disagreements (King of Wei 216/217, Shi Hui 226/227, Sun Hao 1/31 May 280, Xiaoting 221/222, King of Wu 220/221) are real and correctly flagged.
- No infobox area exists on the Cao Cao, Shu Han, Cao Wei or Eastern Wu pages (population figures only); the Jin areas (3.1 M km2 in 280, 2.8 M km2 in 347) are within a factor of two of the shapes.
- Years in order, found/dissolve at start/end, contest pairs closed, wars inside the lives, certainty spans complete, capitals inside the shapes' bboxes, families valid, every region resolves.
