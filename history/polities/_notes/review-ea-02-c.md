# Review of batch ea-02-c (Qin and Han, part c)

Reviewer, 2026-10-19. Dossiers: nanyue, sai, yin, yong, han-dynasty, xin-dynasty, lulin, chimei. Validator: 0 errors for all eight (han-dynasty 8 warnings: counterparts with no dossier). Machine copy: history/notes/phase-b/reviews/ea-02-c.json.

Verdicts: nanyue fix, sai thin, yin pass, yong pass, han-dynasty fail, xin-dynasty thin, lulin thin, chimei fail. 'fix' means fixed by the reviewer on the mount; 'fail' goes back to the author with the unapplied findings below; 'thin' goes to a gap-filler.

## nanyue: fix

- APPLIED `/identity/rulers`: No ruler strip although the Nanyue page has a dated rulers table; the notes said neither page gives a list. Evidence: Nanyue page rulers table: Zhao Tuo 203–137 BC, Zhao Mo 137–122, Zhao Yingqi 122–113, Zhao Xing 113–112, Zhao Jiande 112–111 BC. Fix: Added identity.rulers (five reigns, Zhao Tuo from 204 to match the founding year, source the Nanyue page) and corrected the notes sentence; validates 0 errors 0 warnings.
- THIN `/ledger/5`: 183 BC contest with the Han (the Changsha war) is a 2-cell border band at confidence 1; the place of the fighting is not named (try https://en.wikipedia.org/wiki/Changsha_Kingdom)
- THIN `/ledger/6`: 179 BC end of the Changsha war at confidence 1 (try https://en.wikipedia.org/wiki/Nanyue)
- THIN `/ledger/11`: 135 BC end of the Minyue invasion at confidence 1; the minyue dossier dates it 135 from the murder of the Minyue king (try https://en.wikipedia.org/wiki/Minyue)
- Spot check `/ledger/1` (Nanyue): confirmed
- Spot check `/ledger/8` (Nanyue): confirmed
- Spot check `/ledger/10` (Nanyue): confirmed
- Spot check `/ledger/12` (Nanyue): confirmed
- Spot check `/ledger/16` (Nanyue): confirmed
- Area: infobox None (None), Cliopatria 620249, ratio None; The Nanyue infobox gives no area (population 1,302,805 for 111 BC); extent sentence (Guangdong, Guangxi, Hainan, Hong Kong, Macau, southern Fujian, central to northern Vietnam) matches the corrected keyframes.

## sai: thin

- THIN `/identity/capitals/0`: Capital Yueyang is on no page opened (the Sima Xin page names Yueyang only as the county of his early career and where his head was displayed) and lies outside the drawn shape (intersect of Cliopatria's Sai with Shaanxi, lat 36.7-38.6 N); a page giving Sai's seat is needed, and the outline should then contain it (add a disc as for Yin) or the conflict be stated in the keyframe note (try https://en.wikipedia.org/wiki/Three_Qins)
- THIN `/keyframe_review/0`: The table puts Sai in 'northeastern Shaanxi' and Di (Zhai) in 'northern Shaanxi', while the Sima Xin page says the Three Qins 'occupied the Guanzhong region'; the partition of Guanzhong among the Three Qins is on no page opened (try https://en.wikipedia.org/wiki/Three_Qins)
- Spot check `/ledger/0` (Eighteen_Kingdoms): confirmed ('Sai | Sima Xin (Qin general) | northeastern Shaanxi | Defeated by Liu Bang')
- Spot check `/ledger/1` (Chu%E2%80%93Han_Contention): confirmed ('In 205 BCE, after conquering the Three Qins ... Sima Xin, the King of Sai, Dong Yi ... surrendered')
- Spot check `/identity/capitals/0` (Sima_Xin): not on page (Yueyang named only as his early posting; no capital given)
- Area: infobox None (None), Cliopatria 16521, ratio None; Eighteen Kingdoms page has no per-kingdom area.

## yin: pass

Tried and could not break: Years against the Sima Ang and Chu-Han pages, capital inside the drawn region (gazetteer), the mirror in kingdom-of-han (gain yin, April 205), the table's 'Allies with Liu Bang' conflict (noted by the author).

- Spot check `/identity/capitals/0` (Sima_Ang): confirmed ('capital at Zhaoge (present-day Qi County, Henan)'); the point lies inside the Hebi 90 km disc of the corrected outline
- Spot check `/ledger/1` (Chu%E2%80%93Han_Contention): confirmed ('In April–May 205 BCE, Liu Bang attacked Henei with help from Wei Bao')
- Spot check `/ledger/3` (Sima_Ang): confirmed ('In 205 BC, Han Xin conquered the Kingdom of Yin for the Han dynasty and captured Sima Ang')
- Spot check `/ledger/4` (Sima_Ang): confirmed ('The former Kingdom of Yin became the Henei Commandery')
- Area: infobox None (None), Cliopatria 14022, ratio None; No infobox area; the table's 'northern Henan, southern Hebei' justifies the Hebi disc added to Cliopatria's Hebei-only outline.

## yong: pass

Tried and could not break: Years on the Zhang Han and Chu-Han pages, capital Feiqiu inside the Cliopatria outline (gazetteer), mirror gain in kingdom-of-han 205.

- Spot check `/ledger/0` (Eighteen_Kingdoms): confirmed ('Yong | Zhang Han (Qin general) | central Shaanxi, and eastern Gansu')
- Spot check `/ledger/1` (Zhang_Han_(Qin_dynasty)): confirmed ('Later in 206 BC, Liu Bang's forces invaded Guanzhong and captured Zhang Han's kingdom in a surprise attack')
- Spot check `/ledger/3` (Zhang_Han_(Qin_dynasty)): confirmed ('in June or July 205 BC, the Han army flooded Feiqiu and Zhang Han committed suicide')
- Spot check `/ledger/4` (Chu%E2%80%93Han_Contention): confirmed (Feiqiu 'was guarded by Zhang Han, who committed suicide after his defeat', after the July–August 205 entry)
- Area: infobox None (None), Cliopatria 61876, ratio None; No infobox area.

## han-dynasty: fail

- APPLIED `/ledger/61`: 73 AD gain of Hami from the Xiongnu was at confidence 1 with the note 'The page does not say the Han took Hami in 73'. Evidence: Han-Xiongnu War page, one sentence: 'In 73 AD, General Dou Gu and his army departed from Jiuquan and advanced towards the Northern Xiongnu, defeating the Northern Xiongnu and pursuing them as far as Lake Barkol before establishing a garrison at Hami.' Fix: Confidence raised to 3 and the note rewritten with the quote; validates.
- APPLIED `/ledger/29/counterpart`: 107 BC gain (Xuantu) names gojoseon as counterpart, a state that dissolved in 108 BC; the gojoseon dossier has no 107 loss. Evidence: Four Commanderies page: 'In 107 BCE, Xuantu Commandery was also established in the place of Gojoseon's ally, Yemaek.' Fix: Counterpart changed to 'Yemaek' (no dossier expected) with a reviewer note; validates.
- TO DO `/identity/capitals/4 and /keyframe_review/40-44`: The capital Xuchang (196-220) lies outside every Han keyframe from 197 to 220: the keyframes keep Cliopatria's residual Han (the land outside its Cao Cao and Eastern Wu rows), so from 215 the 'Han' is drawn as Liu Bei's Yi Province while the emperor sits in Cao Cao's domain. Evidence: Gazetteer: a 5 km point at 113.85 E 34.03 N is outside {cliopatria: Han Dynasty} for 197, 207 and 215. The Han page: Cao Cao persuaded Emperor Xian 'to move the capital to Xuchang in 196 AD'; keyframe 44's own note: 'After this the shape is Liu Bei's domain, not the Han emperor's.' Fix: Pick one model and make capitals, keyframes and ledger agree. Recommended: from 196 the Han realm is the land governed in the emperor's name from Xuchang (Cliopatria's Cao Cao shapes for 197, 207, 215), with the other warlords' domains as losses to them (Yuan Shao, Liu Biao, Liu Zhang then Liu Bei, Sun Ce/Sun Quan, Ma Chao and Han Sui, the Gongsun), coordinated with ea-03 (cao-cao); or, if the residual model stays, say in keyframes 40-44 why the capital lies outside and get the orchestrator's sign-off. Either way keyframe 44 must not draw Liu Bei's Yi Province as the Han.
- TO DO `/keyframe_review/39 and /ledger/78`: Liaodong stays Han until 204, but the gongsun-liaodong dossier founds Gongsun Du's state on Liaodong in 190 with han-dynasty as counterpart, so 190-203 is drawn twice; no Han loss in 189/190. Evidence: Four Commanderies page: 'Gongsun Du was appointed Administrator of Liaodong Commandery by Dong Zhuo in 189'; gongsun-liaodong /ledger/0: 190 found, region {region: Liaodong}, counterpart han-dynasty. Fix: Add a 190 loss to gongsun-liaodong of {region: Liaodong} (Four Commanderies page, confidence 2), a new keyframe from 190 that removes it from the 184 shape, and narrow /ledger/78 (204) to Xuantu, Lelang and Daifang (what the gongsun-liaodong 204 gain carries).
- TO DO `/ledger/66 and /keyframe_review/33`: Hami (100 km disc) is gained as direct land in 89 and never lost in the ledger, yet the keyframes drop it from 107; the xiongnu dossier has the remnants taking Yiwu from han-dynasty in 119 and Ban Yong taking it back in 126, neither mirrored here. Evidence: xiongnu /ledger/38 (119 gain, counterpart han-dynasty, 'Remnants captured Yiwu') and /ledger/39 (126 loss, 'Ban Yong subjugated them'); the author's notes: 'han-dynasty carries 73, 77 and 89 only'. Fix: Add a loss of {place: Hami, km: 100} (107 with the Protectorate's abandonment, or 119 to xiongnu to mirror the xiongnu dossier, from the Xiongnu page it cites) and a 126 gain or vassal_start from xiongnu; make keyframes 33-35 agree.
- TO DO `/keyframe_review/16-23 and /ledger/57`: North Korea (Lelang) leaves the Han drawing in 23 with no loss event in either han-dynasty or xin-dynasty, and returns in 43 from goguryeo at confidence 1; the goguryeo dossier has Goguryeo taking Nangnang from han-dynasty in 37 and losing it to the Han in 44. Evidence: goguryeo /ledger/8 (37 gain, counterpart han-dynasty) and /ledger/10 (44 loss); Four Commanderies page is silent on 23-44 (checked); the 23 keyframe is built on Cliopatria's Xin 23 shape, which lacks Korea. Fix: Either keep Lelang Han from 23 to 37 (Gengshi and Guangwu) and add the 37 loss to goguryeo and the 44 (or 43) gain, or add the loss year the page gives (Wang Tiao's revolt, 25-30); open the Lelang Commandery or Emperor Guangwu pages and reconcile with goguryeo and lelang-commandery.
- TO DO `/ledger (192)`: No loss in 192 when Khu Liên's revolt takes Xianglin county (the south of Rinan commandery) and founds Lâm Ấp; the champa dossier founds on that land with han-dynasty as counterpart. Evidence: champa /ledger/0: 192 found, region {admin1: Thừa Thiên - Huế, country: Vietnam}, counterpart han-dynasty ('led a successful rebellion'). Fix: Add a 192 loss to champa of the same region (cite the Champa page the champa dossier used) and a new keyframe or an adjust note on the 184 shape.
- TO DO `/identity/capitals`: No capital for 23-24, although the dossier carries the Gengshi Han as land from October 23 (gain xin-dynasty) and keyframe 16 covers 23-24. Evidence: Wang Mang page: 'the provisional Han capital Wancheng' (Wan, Nanyang) in 23; the author's own capital note quotes the infobox 'Luoyang (23-190 AD, 196 AD)', 'which counts the Gengshi Emperor's court of 23-25'. Fix: Add the Gengshi seats (Wan 23, then Luoyang and Chang'an as a page dates them) or start Luoyang in 23 per the infobox, so capitals are contiguous over the years the state holds land.
- THIN `/ledger/2, /ledger/3`: 202 BC gains of Linjiang and Yan at confidence 1 (page silent) (try https://en.wikipedia.org/wiki/Zang_Tu)
- THIN `/ledger/4, /ledger/5`: 201 BC Hán exchanges at confidence 1 (mirrored by han-2) (try https://en.wikipedia.org/wiki/Chu%E2%80%93Han_Contention)
- THIN `/ledger/8, /ledger/9`: 183-179 BC Nanyue-Changsha contest at confidence 1 (try https://en.wikipedia.org/wiki/Changsha_Kingdom)
- THIN `/ledger/19-22, /ledger/24`: Yelang 111, Minyue 111-110 and south-western Sichuan 109 at confidence 1 (try https://en.wikipedia.org/wiki/Emperor_Wu_of_Han)
- THIN `/ledger/32, /ledger/34`: Lintun 82 BC (the page says 'Lintun was absorbed into Xuantu', not lost) and Xuantu's move 75 BC (page: 'due to resistance from the native people') at confidence 1 (try https://en.wikipedia.org/wiki/Xuantu_Commandery)
- THIN `/ledger/64, /ledger/73`: Ends of the 74 and 123 protectorates at confidence 1 (try https://en.wikipedia.org/wiki/Ban_Yong)
- THIN `/ledger/80`: 207 loss to Eastern Wu at confidence 1 (try https://en.wikipedia.org/wiki/Sun_Quan)
- THIN `/ledger/82`: 220 end of the Southern Xiongnu tie at confidence 1 (try https://en.wikipedia.org/wiki/Xiongnu)
- THIN `/keyframe_review/32`: 785 Ordos and Inner Mongolia cells dropped in 106 without an event (flagged unverified) (try https://en.wikipedia.org/wiki/Qiang_(historical_people))
- THIN `/identity/rulers`: No ruler strip (List of Han emperors lost its tables) (try https://en.wikipedia.org/wiki/List_of_emperors_of_the_Han_dynasty)
- THIN `/wars/9/zones`: Yellow Turban zones empty (provinces not named) (try https://en.wikipedia.org/wiki/Yellow_Turban_Rebellion)
- Spot check `/ledger/13` (Han_dynasty): confirmed ('In 121 BC, Han forces expelled the Xiongnu from a vast territory spanning the Hexi Corridor to Lop Nur')
- Spot check `/ledger/23` (Han_dynasty): confirmed ('Yunnan was brought into the Han realm with the conquest of the Dian Kingdom in 109 BC')
- Spot check `/ledger/29` (Four_Commanderies_of_Han): confirmed year; counterpart wrong (Yemaek, not Gojoseon): fixed
- Spot check `/ledger/37` (Han_dynasty): confirmed ('established the Protectorate of the Western Regions in 60 BC')
- Spot check `/ledger/38` (Han-Xiongnu_War): confirmed ('In 53 BC, Huhanye ... surrendered to Han empire rule'; the Han page has 51 BC, conflict noted by the author)
- Spot check `/ledger/52` (Emperor_Guangwu_of_Han): confirmed (Luomen fell in 'the winter of AD 34')
- Spot check `/ledger/54` (Emperor_Guangwu_of_Han): confirmed (Dou Rong 'turned over the lands under his control to Emperor Guangwu in AD 36')
- Spot check `/ledger/61` (Han-Xiongnu_War): under-rated: the page dates the Hami garrison to the 73 campaign; raised to 3
- Spot check `/ledger/66` (Han-Xiongnu_War): confirmed (Hami captured in the 89 AD campaign paragraph)
- Spot check `/ledger/69` (Protectorate_of_the_Western_Regions): confirmed ('On 29 July 107 ... Duan Xi was killed and the post was abandoned')
- Spot check `/ledger/72` (Protectorate_of_the_Western_Regions): confirmed ('restored from 123 to 124 by the son of Ban Chao, Ban Yong')
- Area: infobox 6000000 (-50), Cliopatria 4484370, ratio 0.75; Also 100 AD 6,500,000 km2 against the 91 shape's 4,582,897 (0.70); both quoted in keyframes 13 and 31.

## xin-dynasty: thin

- APPLIED `/ledger/3/source`: The 17 AD Lülin contest cited the Xin page, which gives no year. Evidence: Xin page: 'two insurgent bands in Hubei were recruited by Han loyalists' (no year); Wang Mang page: 'About AD 17 ... several rebellions began', 'Lülin rebels in modern Yichang, Hubei'. Fix: Source moved to the Wang Mang page (already in sources) with a reviewer note.
- APPLIED `/ledger/2/source`: The 10 AD break with the Xiongnu cited the Wang Mang page, which gives no year for it. Evidence: Wang Mang page: 'sometime before AD 10', declaration of war undated; Xin page: 'intended to intervene in China around 10/11 AD'. Fix: Source moved to the Xin page with a reviewer note.
- THIN `/ledger/4, /ledger/6, /wars/1/zones`: The Chimei contest zone is a placeholder of Shandong, Henan and Hubei cells (confidence 1, 'NO PAGE NAMES THE PLACE'), but the Wang Mang page, already in sources, says the Chimei 'roved through large swaths of territory in modern southern Shandong and northern Jiangsu'; replace with the same region the chimei dossier gets (e.g. intersect of the Xin 14-minus-23 cells with {place: Linyi, km: 150} and {place: Xuzhou, km: 100}: 432 cells, all inside the Xin 14 shape and outside Xin 23) at confidence 2 (try https://en.wikipedia.org/wiki/Wang_Mang)
- THIN `/keyframe_review/2`: Xin 14 to 23 loses 1.19 M km2 (Shandong, Henan, Hubei, Hunan, the south and south-west) with no loss events; within the 1-2 page budget (try https://en.wikipedia.org/wiki/Gengshi_Emperor)
- THIN `/ledger/0`: 9 AD Xiongnu tie at confidence 1 (the seal affair is undated: 'sometime before AD 10') (try https://en.wikipedia.org/wiki/Xiongnu)
- Spot check `/ledger/1` (Xin_dynasty): confirmed ('Wang Mang proclaimed emperor: 10 January 9')
- Spot check `/ledger/7` (Xin_dynasty): confirmed ('Chang'an captured: 5 October 23 AD')
- Spot check `/ledger/2` (Wang_Mang): not on cited page (year is the Xin page's): source moved
- Spot check `/ledger/3` (Xin_dynasty): not on cited page (year is the Wang Mang page's): source moved
- Spot check `/ledger/4` (Wang_Mang): not on page as claimed: the page names southern Shandong and northern Jiangsu
- Area: infobox None (None), Cliopatria 4465527, ratio None; Xin infobox has no area (checked); the author compared with the Han infobox (0.74).

## lulin: thin

- APPLIED `/ledger/0/source and /ledger/1/source`: The 17 AD rise of the Lülin cited the Xin page, which gives no year. Evidence: Wang Mang page: 'About AD 17 ... several rebellions began'; 'Lülin rebels in modern Yichang, Hubei'. Fix: Both sources moved to the Wang Mang page (already in sources) with reviewer notes; validates.
- THIN `/keyframe_review/0`: The Lülin land 17-22 is the whole of Hubei; the Wang Mang page names Yichang, Hubei, and no Lülin article was opened (budget) (try https://en.wikipedia.org/wiki/L%C3%BClin)
- THIN `/identity/wikipedia`: wikipedia is null although an article on the Lülin exists (try https://en.wikipedia.org/wiki/L%C3%BClin)
- Spot check `/ledger/0` (Wang_Mang): confirmed on the Wang Mang page ('About AD 17'; Yichang, Hubei); not on the cited Xin page: source moved
- Spot check `/ledger/3` (Wang_Mang): confirmed ('in early 23, Liu Xuan was proclaimed the Gengshi Emperor')
- Area: infobox None (None), Cliopatria None, ratio None; No Cliopatria row, no article opened.

## chimei: fail

- TO DO `/keyframe_review/0/correction, /ledger/0-2/region, /identity/predecessors/0/land, /wars/0/zones`: The Chimei land of 17-24 is a placeholder of Shandong, Henan and Hubei cells with the note 'NO PAGE NAMES THE CHIMEI'S LAND before 25', but the Wang Mang page cited by these very events names it, and Hubei is the Lülin's land. Evidence: Wang Mang page: the Chimei 'roved through large swaths of territory in modern southern Shandong and northern Jiangsu'; the Lülin were 'in modern Yichang, Hubei'. Fix: Replace the inner union [Shandong, Henan, Hubei] with southern Shandong and northern Jiangsu, e.g. {intersect: [{minus: [Xin 14, Xin 23]}, {union: [{place: Linyi, km: 150, country: China}, {place: Xuzhou, km: 100, country: China}]}]} (432 cells, all inside Xin 14 and outside Xin 23), with the page's words in text; raise /ledger/0-1 to confidence 2; make the same change in xin-dynasty /ledger/4, /ledger/6 and /wars/1/zones.
- THIN `/ledger/0`: Leaders, first base (Ju or Langya) and the march west 23-25 are on no page opened (try https://en.wikipedia.org/wiki/Red_Eyebrows)
- Spot check `/ledger/0` (Wang_Mang): year confirmed ('About AD 17'); region not as the note claims (the page names southern Shandong and northern Jiangsu)
- Spot check `/ledger/3` (Emperor_Guangwu_of_Han): confirmed ('the Gengshi Emperor's regime was destroyed by the Chimei' soon after Guangwu's accession in 25)
- Spot check `/ledger/6` (Xin_dynasty): confirmed ('The Red Eyebrows were defeated by Liu Xiu's forces in 27 AD')
- Area: infobox None (None), Cliopatria None, ratio None; No Cliopatria row, no article opened.

## Cross-dossier matrix (non-matched rows)

- missing: nanyue -183 vassal_start minyue: minyue (ea-01) has no vassal_start/vassal_end with nanyue for 183-135; route to ea-01
- missing: nanyue -183 vassal_start yelang: yelang has no vassal_start/vassal_end with nanyue for 183-111; route to the yelang owner
- mismatch: han-dynasty -202 gain yan: yan's dissolve has no counterpart and its successors name 'qin'; it should name han-dynasty (Zang Tu executed, Yan to Lu Wan as a Han vassal kingdom)
- exception: han-dynasty -107 gain Yemaek: counterpart corrected by the reviewer from gojoseon (dissolved 108) to Yemaek; no dossier expected
- mismatch: han-dynasty 9 vassal_end xiongnu: xiongnu ends its tie with han-dynasty in 10; han-dynasty ends it in January 9 and xin-dynasty carries 9-10; xiongnu (ia-01) should end the Han tie in 9 and pair 9-10 with xin-dynasty
- missing: xin-dynasty 9 vassal_start xiongnu: no xin-dynasty vassal events in the xiongnu dossier
- exception: han-dynasty -77 vassal_start protectorate-of-the-western-regions: protectorate-of-the-western-regions (another ea-02 part) not on the mount; also -60, 8, 74, 77, 91, 107, 123, 125
- exception: han-dynasty 29 gain zhang-bu: zhang-bu, liu-yong, peng-chong (29), wei-ao (34), chengjia, dou-rong (36): listed in counterparts_needing_dossiers for ea-02-x
- missing: goguryeo 37 gain han-dynasty: han-dynasty has no loss of Lelang in 37 (it drops North Korea in 23 with no event); see han-dynasty fixes
- missing: han-dynasty 48 vassal_start southern-xiongnu: southern-xiongnu (ia-01) has no vassal events with han-dynasty (48 start, 220 end)
- missing: han-dynasty 77 loss xiongnu: xiongnu has no 77 gain of Hami
- missing: han-dynasty 89 gain xiongnu: xiongnu has no 89 loss of Hami
- missing: xiongnu 119 gain han-dynasty: han-dynasty has no 119 loss of Hami/Yiwu
- missing: xiongnu 126 loss han-dynasty: han-dynasty has no 126 gain of Hami/Yiwu
- mismatch: gongsun-liaodong 190 found han-dynasty: gongsun-liaodong holds Liaodong from 190; han-dynasty keeps it to 204 (its 204 loss matches gongsun-liaodong's 204 gain of Lelang and Daifang)
- missing: champa 192 found han-dynasty: han-dynasty has no 192 loss of Xianglin (Thừa Thiên-Huế)
- exception: han-dynasty 197 loss cao-cao: cao-cao (also 207, 211), eastern-wu (207), cao-wei (220 dissolve): ea-03 has not run
- mismatch: qi -204 dissolve han-dynasty: qi (ea-01) names han-dynasty, which starts in 202; kingdom-of-han carries the Qi gain in 203

Matched: 33 of 51 rows (full list in the JSON).

## Problems

- han-dynasty's 196-220 model (residual Han outside Cao Cao's row, capital Xuchang inside Cao Cao's) needs a decision shared with ea-03, which owns cao-cao and has not run.
- protectorate-of-the-western-regions, cao-cao, cao-wei, shu-han and eastern-wu are not on the mount: their mirror events are unchecked.
- Neighbour dossiers owned elsewhere lack mirrors of this batch's events: minyue and yelang (Nanyue vassalage), xiongnu (77, 89 Hami; 9-10 Xin tie), southern-xiongnu (48-220 vassalage), qi (dissolve names han-dynasty), yan (dissolve without counterpart).
- Reviewer edits applied on the mount (each validated, read back unchanged): nanyue identity.rulers and notes; han-dynasty /ledger/29 counterpart and /ledger/61 confidence; xin-dynasty /ledger/2 and /ledger/3 sources; lulin /ledger/0 and /ledger/1 sources.
- No page failed to load; WebFetch opened Nanyue, Eighteen Kingdoms, Chu-Han Contention, Sima Ang, Sima Xin, Zhang Han (Qin dynasty), Han dynasty, Han-Xiongnu War, Emperor Guangwu of Han, Four Commanderies of Han, Protectorate of the Western Regions, Xin dynasty, Wang Mang.
