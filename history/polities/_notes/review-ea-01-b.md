# Review of batch ea-01-b (jin, later-zhou, lu, qi, qin)

Reviewer run of 2026-10-18. The machine copy is history/notes/phase-b/reviews/ea-01-b.json. Validator: 0 errors on all five; the warnings are the five Eastern Zhou shapes on later-zhou (reviewed in eastern-zhou.json, checked) and the counterparts shu, ba, east-zhou on qin (listed by the author). No infobox gives an area.

## jin: thin

Findings:
- `/keyframe_review/1` (for the author): Jin jumps from the 15,000 km2 Linfen disc (jin_-1042, to -751) to Cliopatria's 136,796 km2 at -750 with no ledger event at -750, while /ledger/4 gains the Shanxi part of that same -750 shape in 676: the keyframe holds from 750 land the ledger gains 74 years later. Evidence: shapes.csv jin_-750 = 136,796 km2; /keyframe_review/0 correction is Linfen 70 km; /ledger/4 region = intersect(Jin -750, Shanxi (region)). The Jin page dates only Duke Xian's reign: 'He annexed 16 or 17 small states in Shanxi, dominated 38 others' (no extent, no years). qin.json handles the same situation with a -750 gain (/ledger/6). Fix: Either add a -750 gain (confidence 1, counterpart 'small states of Shanxi', note 'Cliopatria's first shape; no page dates the growth from the fief') and keep /ledger/4 as the dated step, or mark jin_-750 adjust with a correction limited to the Fen valley core (Linfen/Quwo) until 676 so that /ledger/4 adds the rest.
- `/ledger (missing, -404)` (for the author): qi.json /ledger/6 (29 cells) and lu.json /ledger/5 (13 cells) gain Jin's old cells at -404, but jin.json has no loss to qi or lu; its land passes only to han, wei, zhao by the -403 splits. Evidence: Same batch: qi /ledger/6 'gain jin -404' and lu /ledger/5 'gain jin -404', both confidence 1 from Cliopatria's cells; jin /ledger/9-11 split to han/wei/zhao only. Fix: Add -404 losses to qi (intersect(Qi -404, Jin -450)) and lu (intersect(Lu -404, Jin -450)) at confidence 1, or have qi and lu name the successor state as counterpart; the pair must agree.
- `/keyframe_review/0/note` (for the author): The note says the fief is 'a vassal tint of the Zhou until 751 (the zhou-dynasty dossier)', but zhou-dynasty.json has vassal_start events only for song, cao, cai, chen and chu, and jin.json has none. Evidence: zhou-dynasty.json ledger: vassal_start song/cao -1046, cai/chen -1045, chu -1030, vassal_end -751 for the same five; nothing for jin, lu, qi or qin. Fix: Add a vassal_start (-1042) / vassal_end (-751) pair with zhou-dynasty as counterpart (and ask for the mirror in zhou-dynasty), or delete the sentence.

Gaps for a gap-filler:
- `/ledger/4`: Duke Xian's 16-17 annexed Shanxi states (Geng, Huo, old Wei, Yu, Western Guo) have no year or place; confidence 1. Try https://en.wikipedia.org/wiki/Spring_and_Autumn_period
- `/ledger/6`: The -550 Hebei-plain strip from Qi (about 17,000 km2) has no page; confidence 1. Try https://en.wikipedia.org/wiki/Duke_Ping_of_Jin
- `/ledger/7`: The -450 Wey cells; confidence 1, page silent. Try https://en.wikipedia.org/wiki/Wey_(state)
- `/ledger/8`: The -450 Luhun-edge strip to Chu; confidence 1, and chu.json has no mirror. Try https://en.wikipedia.org/wiki/Chu_(state)
- `/identity/capitals`: Capital years (Tang, E, Jiang to 586; Xintian from 585) are the researcher's boundaries; the page lists the order only. Try https://en.wikipedia.org/wiki/Houma

Spot checks:
- `/ledger/2` confirmed on https://en.wikipedia.org/wiki/Jin_(Chinese_state): 'In 678 BC, Duke Wu of Quwo conquered Jin and killed Marquis Min of Jin (704-678).'
- `/ledger/9` confirmed on https://en.wikipedia.org/wiki/Partition_of_Jin: 'So, in 403 BCE, they divided the state's lands among themselves'; 'This same year, King Weilie of Zhou proclaimed Jin, Wei, Han, and Zhao as equals.' (also /ledger/10, /ledger/11)
- `/ledger/12` confirmed on https://en.wikipedia.org/wiki/Jin_(Chinese_state): 'generally consider 369 BC the final year of Jin's existence'; Duke Huan moved to Tunliu; infobox end 369 BC. Partition of Jin gives 386 and 349, Warring States 376, as the note says.
- `/ledger/5` confirmed on https://en.wikipedia.org/wiki/Eastern_Zhou: 'King Xiang turned to Duke Wen of Jin for help, who killed Prince Dai and was rewarded with rule over Henei and Yangfan' in the paragraph opening 'In 635 BC'; confidence 2 is right.
- `/ledger/4` confirmed on https://en.wikipedia.org/wiki/Jin_(Chinese_state): 'He annexed 16 or 17 small states in Shanxi, dominated 38 others, and absorbed a number of Rong tribes.' No years for the conquests, as the note says.

Area: The Jin page has no area in its infobox (checked); the dossier says so. The internal factor of nine at -750 is the first fix.

## later-zhou: thin

Gaps for a gap-filler:
- `/ledger (missing, 955)`: The Later Zhou conquest of Later Shu's northern prefectures (Qin, Feng, Cheng, Jie) is not in the ledger or the wars; the Later Zhou, Shizong and Later Shu pages are silent (reviewer re-checked Shizong: only 'some minor successes were made against the Southern Tang and Later Shu'). Try https://en.wikipedia.org/wiki/Meng_Chang
- `/wars/2`: The 959 campaign against the Liao (Ying and Mo prefectures, the Three Passes) has empty zones; the Shizong page says only 'nothing substantial came of it'. Try https://en.wikipedia.org/wiki/Sixteen_Prefectures
- `/ledger/3`: The number of Huainan prefectures ceded in 958 is not on the pages opened (the region is Cliopatria's Southern Wu cells, which is fine). Try https://en.wikipedia.org/wiki/Li_Jing_(Southern_Tang)

Spot checks:
- `/ledger/0` confirmed on https://en.wikipedia.org/wiki/Later_Zhou: Infobox 'Dynasty established: 13 February 951'; lead 'New Year's Day in 951' (the conflict is in the notes).
- `/ledger/1` confirmed on https://en.wikipedia.org/wiki/Southern_Tang: 'began the invasion of Huainan in early 956'; 'constructed a floating bridge to cross the Huai River at Zhengyang'.
- `/ledger/3` confirmed on https://en.wikipedia.org/wiki/Southern_Tang: 'Li Jing was forced to become a vassal of the Emperor Shizong of Later Zhou, cede all territory north of the Yangtze River'; 'By April 958 Shouchun had fallen' (also /ledger/2).
- `/ledger/4` confirmed on https://en.wikipedia.org/wiki/Southern_Tang: Infobox 'Forced to cede Huainan and become a vassal of Later Zhou: 958'.
- `/ledger/6` confirmed on https://en.wikipedia.org/wiki/Later_Zhou: Infobox 'Formal abdication: 3 February 960'; 'Zhao Kuangyin usurped the throne and declared himself emperor of the Great Song dynasty'.
- `/ledger/5` confirmed on https://en.wikipedia.org/wiki/Southern_Tang: 'In 960, the Southern Tang became a vassal of the newly established Northern Song dynasty.'

Area: No area in the Later Zhou infobox. Keyframe arithmetic checks: Later Han 947 (790,319) minus Northern Han 960 (26,506) plus Huainan gives the 960 shape (902,631); the five 'has no verdict' warnings are the Eastern Zhou shapes, which eastern-zhou.json reviews (checked: its keyframe_review lists exactly later-zhou_-750, -450, -404, -366, -350).

## lu: thin

Findings:
- `/ledger/3/confidence` (applied by the reviewer): The note quotes the Yue page's 'invaded Qi and Lu' as a Lu land loss, but the page's next sentence has Qi, not Lu, ceding land. Evidence: Yue (state) page: 'Qi and Lu made peace with Yue, with Qi ceding territory and allowing Yue to march triumphantly through the Lu capital.' Fix: Confidence lowered from 2 to 1 and the sentence added to the note (done by the reviewer; validated, 0 errors).
- `/ledger/3` (for the author): The keyframe corrections /keyframe_review/1-3 already remove the Yue-404 cells (Tan's land, 'to Yue' in 414) from Lu for the whole life of the pre-404 shapes, so /ledger/3 takes from Lu in 404 land the corrected shapes never held; /keyframe_review/4/note counts those 18 cells as 'explained in the ledger'. Evidence: /keyframe_review/1 correction = Lu -750 minus (Chu -404 union Yue -404); /ledger/3 region = intersect(Lu -450, Yue -404), the same cells. Fix: Delete /ledger/3 (the land was Tan's) or take the Yue cells out of the corrections and keep the loss, not both; fix the /keyframe_review/4 note to match.
- `/keyframe_review/1` (for the author): Lu grows from the 40 km Qufu disc (about 5,000 km2, lu_-1042 to -751) to Cliopatria's 750 shape (43,571 km2 less the Ju and Tan cells, about 35,000 km2) with no ledger event at -750. Evidence: shapes.csv lu_-750 43,571 km2; the ledger has only found (-1042) before -480. Fix: Add a -750 gain at confidence 1 ('Cliopatria's first shape; no page dates the growth'), as qin.json /ledger/6 does, or extend the disc keyframe's correction.
- `/ledger/7` (for the author): The -284 loss of 34 cells to Qi has no mirror in qi.json, although the qi_-284 shape contains those cells. Evidence: qi.json ledger at -284: occupation_start yan, loss chu only; /keyframe_review/7 note: the 284 shape adds 113 cells, 76 of them Song's (the rest are Lu's). Fix: Ask qi to add the mirror gain (see the qi finding) or drop the loss; the Lu note's own doubt (Qi was overrun by Yan in 284) should be repeated on the Qi side.
- `/ledger/5, /ledger/6` (for the author): The -404 gains from jin (13 cells) and from qi (8 cells) have no mirror: jin.json has no loss to lu, qi.json no loss to lu at -404. Evidence: Same batch; both events confidence 1 from Cliopatria's cell moves. Fix: Add the mirrors in jin and qi or drop these two gains (they are a few cells of Cliopatria noise).

Gaps for a gap-filler:
- `/keyframe_review/1`: The corrected pre-404 shape keeps the 130 cells that go to Qi in 404, reaching 120.6 E on the coast, while the page says Lu 'mainly covered the central and southwest regions of what is now Shandong'; the shape kept is about four times the 404 shape the author says matches that sentence. A page for Lu's eastern extent (Zhuanyu, Ju, Jie) is needed. Try https://en.wikipedia.org/wiki/Spring_and_Autumn_period
- `/ledger/1`: -480 loss to Song: confidence 1, page silent. Try https://en.wikipedia.org/wiki/Song_(state)
- `/ledger/2`: -450 gain from Zhu: confidence 1, page silent. Try https://en.wikipedia.org/wiki/Zhu_(state)
- `/ledger/4`: -404 loss to Qi: 'Lu was occupied by Qi' is undated; confidence 1. Try https://en.wikipedia.org/wiki/Duke_Mu_of_Lu
- `/ledger/7`: -284 loss to Qi: undated on the page; confidence 1. Try https://en.wikipedia.org/wiki/Warring_States_period
- `/notes`: Lu's own annexations (Ji 721, Xuqu 620, Zhuan 585, Yu 524, Lan 521) are not located. Try https://en.wikipedia.org/wiki/Spring_and_Autumn_period

Spot checks:
- `/ledger/0` confirmed on https://en.wikipedia.org/wiki/Lu_(state): Infobox 'Established: c. 1042 BC'; territory 'mainly covered the central and southwest regions of what is now Shandong Province'.
- `/ledger/8` confirmed on https://en.wikipedia.org/wiki/Lu_(state): 'In 249 BC King Kaolie of the state of Chu invaded and annexed Lu.'; infobox 'Annexed by Chu: 249 BC' (also /ledger/9).
- `/ledger/3` not on page on https://en.wikipedia.org/wiki/Yue_(state): The quoted sentence is there, but the next one has Qi ceding territory and Lu only letting Yue march through its capital; confidence was 2, lowered to 1 by the reviewer.
- `/ledger/4` confirmed on https://en.wikipedia.org/wiki/Warring_States_period: 'Smaller states like Lu would quickly fall under the power of bigger states (in this case, Lu was occupied by Qi.)', undated, as the note says (confidence 1).

Area: No area in the Lu infobox (checked). The rulers overlap Boqin to -997 / Duke Kao from -998 is the page's own table ('c. 1042-997 BC', '998-995 BC'), not an author error.

## qi: thin

Findings:
- `/keyframe_review/1` (for the author): Qi grows from the 60 km Zibo disc (about 11,000 km2, qi_-1046 to -751) to Cliopatria's 102,632 km2 at -750 with no ledger event. Evidence: shapes.csv qi_-750 102,632 km2; the ledger has found (-1046) and two capital moves before -550. Fix: Add a -750 gain at confidence 1 ('Cliopatria's first shape'; the page's 'annexed 35 neighboring polities' and the states table give no extent), as qin.json /ledger/6 does.
- `/ledger (missing, -284)` (for the author): No gain from lu at -284, although lu.json /ledger/7 loses 34 cells to Qi that year and qi_-284 contains them (113 new cells, only 76 of them Song's). Evidence: lu.json /ledger/7 region = intersect(Lu -404, Qi -284); qi /keyframe_review/7 note. Fix: Add a -284 gain from lu, confidence 1, region intersect(Lu -404, Qi -284), with the caveat that Yan was occupying Qi that year; or drop the Lu loss. The two dossiers must agree.
- `/keyframe_review/4/note, /ledger/5/note` (for the author): Both notes cite the Yue page's 'invaded Qi and Lu' in 404 as support for Qi's 404 growth, but the page says Qi lost land that year; the Yue page is not in qi's sources and no 404 loss to Yue is in the ledger. Evidence: Yue (state) page: 'Qi and Lu made peace with Yue, with Qi ceding territory and allowing Yue to march triumphantly through the Lu capital.' Fix: Correct both notes, add the Yue page to sources and a -404 loss to yue (confidence 1; the page names no land, so use whatever Qi land Cliopatria's Yue -404 shape takes, or say none can be drawn).
- `/ledger/10` (for the author): Qi loses the Song land to Chu 'by 284', but chu.json /ledger/40 gives Chu its share of Song straight from song in 286; the two disagree on year and counterpart. Evidence: chu.json /ledger/40: '286: Chu's share of Song' (gain, counterpart song); qi /ledger/10 counterpart chu, confidence 1; the King Min page does not name the attacker. Fix: Settle one version with the chu author: either Chu's 286 gain is from qi in 284, or Qi never held that land and /ledger/8 should take only Cliopatria's Qi part of Song.

Gaps for a gap-filler:
- `/ledger/4`: Xue and Pi (418) and the other annexed small states (Zhu 768, Guo 670, Zhang 664, Yang 660, Tan 684, Sui 681, Ji 690, Lai 567, Cheng 408) are not located; confidence 1. Try https://en.wikipedia.org/wiki/Spring_and_Autumn_period
- `/ledger/6`: -404 gain of 29 Jin cells: page silent; no jin mirror. Try https://en.wikipedia.org/wiki/Battle_of_Guiling
- `/ledger/13`: Tian Dan's 209 restoration of Qi after the Qin collapse is not in the ledger; the dossier re-opens Qi only in 206. Try https://en.wikipedia.org/wiki/Tian_Dan
- `/ledger/14`: -204 dissolve at confidence 1: Han Xin's invasion of Qi is not on the pages opened. Try https://en.wikipedia.org/wiki/Battle_of_Wei_River
- `/identity/capitals`: Yingqiu and Bogu use Linzi's coordinates as a placeholder (flagged by the author). Try https://en.wikipedia.org/wiki/Linzi

Spot checks:
- `/ledger/1` confirmed on https://en.wikipedia.org/wiki/Qi_(state): Infobox 'Yingqiu (11 c.-866 BCE) Bogu (866-859 BCE) Linzi (859-221 BCE)' (also /ledger/2).
- `/ledger/7` confirmed on https://en.wikipedia.org/wiki/Qi_(state): 'In 386, the house of Tian fully replaced the house of Jiang as rulers of Qi.'
- `/ledger/9` confirmed on https://en.wikipedia.org/wiki/King_Min_of_Qi: Linzi 'was invaded and sacked in 284 BC by General Yue Yi of Yan'; 'All but two cities of Qi were conquered'; Ju and Jimo unoccupied.
- `/ledger/11` confirmed on https://en.wikipedia.org/wiki/Warring_States_period: 'Yan would hold control over Qi until 279 BC, whereupon the state of Qi would be restored'.
- `/ledger/12` confirmed on https://en.wikipedia.org/wiki/Qi_(state): Infobox 'Conquered by Qin: 221 BCE'; body 'in 222' (the note records the conflict).
- `/ledger/8` confirmed on https://en.wikipedia.org/wiki/King_Min_of_Qi: 'In 286 BC, King Min attacked and destroyed Song'; the King Min page does not name who took the land after.
- `/keyframe_review/4` not on page on https://en.wikipedia.org/wiki/Yue_(state): The Yue page is cited for Qi's 404 growth but says Qi ceded territory (see fixes).

Area: No area in the Qi infobox (checked). One dossier for the old Qi (to 221) and Tian Du's Qi (206-204) with a 220-207 gap: acceptable as written, the orchestrator may prefer to split it.

## qin: thin

Findings:
- `/ledger/1` (for the author): The 822 gain of Quanqiu names zhou-dynasty as counterpart, but zhou-dynasty.json has no loss to qin, and the note itself calls it a recovery of land lost to the Xirong. Evidence: Qin page: 'King Xuan formally awarded them the territory of Quanqiu'; zhou-dynasty.json has no qin event. Fix: Make the counterpart Xirong (as /ledger/3 does) or ask zhou-dynasty for a mirror loss.
- `/ledger/43, /identity/end` (for the author): The state is renamed at -221 (same state) and then 'dissolves' into qin-dynasty at -219 at confidence 1, a Cliopatria row boundary rather than an event; the Qin page infobox gives dissolution 207 BC. Evidence: polities.csv: qin -750..-219, qin-dynasty 'Qin Dynasty' -218..-209 (ea-02, not written); Qin page infobox 'Dissolution 207 BC'. Fix: Orchestrator decision, not an author fault: either fold the Qin Dynasty row into this dossier (one state, renamed 221) or end it at -221 with qin-dynasty starting 221; the -219 dissolve should then go.
- `/ledger/40` (for the author): Counterpart 'Yue remnants (Wuyue region)' has no dossier and is not in counterparts_needing_dossiers; the source sentence is dated only 'the following year' and tagged [citation needed] on the unification page. Evidence: Qin's wars of unification: 'The following year, Wang Jian and Meng Wu led Qin forces to attack the Wuyue region' (citation needed). Fix: List the counterpart (or use 'nobody'); confidence 2 can stay.
- `/ledger (missing, after 257)` (for the author): No loss after 257, although the cited King Zhaoxiang page says 'The combined forces recaptured Hedong, Anyang, Taiyuan, Pilao, Wu'an, Shangdang and Runan' (undated); the author flagged it. Evidence: King Zhaoxiang of Qin page, read by the reviewer. Fix: A gap-filler should date it (the 247 coalition) and add the losses and their re-gains before 230.

Gaps for a gap-filler:
- `/ledger/6`: -750 gain of Guanzhong and middle Shaanxi from the Quanrong at confidence 1 (Cliopatria's year); the 11 adjusted keyframes to -277 rest on the researcher's reading at confidence 1-2. Try https://en.wikipedia.org/wiki/Duke_Wen_of_Qin
- `/ledger/17`: Gansu conquests ('almost all western territories', 4th century) undated; confidence 1. Try https://en.wikipedia.org/wiki/Yiqu
- `/ledger/19`: Hanzhong 312 bridged at confidence 1. Try https://en.wikipedia.org/wiki/Battle_of_Danyang
- `/ledger/25`: Shangdang and Taiyuan 260 at confidence 1; the King Zhaoxiang page has Qin taking Shangdang's cut-off region in 262. Try https://en.wikipedia.org/wiki/Battle_of_Changping
- `/ledger/43`: -219 dissolve at confidence 1 (see fixes). Try https://en.wikipedia.org/wiki/Qin_dynasty

Spot checks:
- `/ledger/0` confirmed on https://en.wikipedia.org/wiki/Qin_(state): 'It is traditionally dated to 897 BC'; Feizi.
- `/ledger/14` confirmed on https://en.wikipedia.org/wiki/Qin_(state): 'first Qin ruler to adopt the title of "King" in 325 BC'.
- `/ledger/15` confirmed on https://en.wikipedia.org/wiki/Qin_(state): 'In 316 BC, Qin completed the conquests of the southern states of Ba and Shu, in modern Sichuan.' (also /ledger/16)
- `/ledger/9` confirmed on https://en.wikipedia.org/wiki/Qin_(state): 'conquered some Qin territories west of the Yellow River' under Duke Jian (the 413-409 span is the note's).
- `/ledger/27` confirmed on https://en.wikipedia.org/wiki/King_Zhaoxiang_of_Qin: 'overthrew the Eastern Zhou dynasty in 256 BC'; Jiu broke 'into Wangcheng'; the Duke conceded 'all his lands'.
- `/ledger/24` confirmed on https://en.wikipedia.org/wiki/King_Zhaoxiang_of_Qin: 'capture of the Chu capital city of Ying in 278 BC'; Nan Commandery (also /ledger/22 '400 li of Hedong lands', /ledger/23 Anyi 286).
- `/ledger/37` confirmed on https://en.wikipedia.org/wiki/Qin%27s_wars_of_unification: 'In 223 BC, Wang Jian conquered the Chu capital Shouchun.'
- `/ledger/34` confirmed on https://en.wikipedia.org/wiki/Qin%27s_wars_of_unification: 225: Daliang flooded, 'King Jia of Wei surrendered'.
- `/ledger/29` confirmed on https://en.wikipedia.org/wiki/Qin%27s_wars_of_unification: 230: Neishi Teng took Han; 'reorganised to form the Qin Empire's Yingchuan Commandery'.
- `/ledger/32` confirmed on https://en.wikipedia.org/wiki/Qin%27s_wars_of_unification: 228: 'Qin forces occupied Handan, captured King Qian'; Prince Jia to Dai, Dai conquered 222 (also /ledger/39).
- `/ledger/38` confirmed on https://en.wikipedia.org/wiki/Qin%27s_wars_of_unification: 'In 222 BC, Qin forces led by Wang Ben and Li Xin invaded the Liaodong Peninsula', King Xi captured.
- `/ledger/41` confirmed on https://en.wikipedia.org/wiki/Qin%27s_wars_of_unification: 'By 221 BC, Qi was the only state yet to be conquered'; Tian Jian surrendered.
- `/ledger/28` confirmed on https://en.wikipedia.org/wiki/Qin%27s_wars_of_unification: 'In 249, King Zhuangxiang of Qin conquered East Zhou.'

Area: No area in the Qin (state) infobox (checked). The jump 90,198 to 632,084 km2 (326 to 315) is Shu and Ba (316); 714k to 1,321k to 1,523k is Wei, Chu, Yan, Dai, Qi 225-221: all explained.

## Cross-dossier matrix

- jin -676 gain small states of Shanxi -> no dossier: exception. Listed in the author's counterparts_needing_dossiers.
- jin -635 gain eastern-zhou -> eastern-zhou -635 loss: matched. Henei and Yangfan, both confidence 2.
- jin -550 gain qi -> qi -550 loss: matched. Hebei-plain strip, both confidence 1.
- jin -450 gain wey -> no dossier: exception. wey.json not written yet (ea-01, another part).
- jin -450 loss chu -> chu (none): missing. chu.json has no gain from jin near -450 (21 Luhun-edge cells).
- jin -403 split han / wei / zhao -> no dossier: exception. han, wei, zhao not written yet (ea-01, another part); they should start from 403.
- lu -480 loss song -> no dossier: exception. song.json not written yet.
- lu -450 gain zhu -> no dossier: exception. zhu.json not written yet.
- lu -404 loss yue -> no dossier: exception. yue.json not written yet; the reviewer lowered the event to confidence 1 (the Yue page has Qi, not Lu, ceding land) and it duplicates the keyframe corrections.
- lu -404 loss qi -> qi -404 gain: matched. Lu's eastern half, both confidence 1.
- lu -404 gain jin -> jin (none): missing. jin.json has no loss to lu at -404.
- lu -404 gain qi -> qi (none): missing. qi.json has no loss to lu at -404 (8 cells).
- lu -284 loss qi -> qi (none): missing. qi.json has no gain from lu at -284, though the qi_-284 shape holds the cells.
- lu -249 loss chu -> chu -249 gain: matched. Both confidence 3.
- qi -418 gain zhu -> no dossier: exception. zhu.json not written yet.
- qi -404 gain jin -> jin (none): missing. jin.json has no loss to qi at -404 (29 cells).
- qi -404 loss (missing) yue -> no dossier: missing. Yue page: 'Qi ceding territory' in 404; no event on either side (yue.json not written).
- qi -286 gain song -> chu -286 gain: mismatch. song.json not written; chu.json /ledger/40 also gains Song land in 286 directly from song, while qi says Chu took it from Qi by 284.
- qi -284 occupation_start yan -> no dossier: exception. yan.json not written yet; it should mirror 284-279.
- qi -284 loss chu -> chu -286 gain: mismatch. Chu's side has counterpart song and year 286.
- qi -221 loss qin -> qin -221 gain: matched. Both confidence 3.
- qi -206 gain qin-dynasty -> no dossier: exception. qin-dynasty (ea-02) not written yet.
- later-zhou 958 gain southern-tang -> no dossier: exception. southern-tang (ea-04) not written yet; vassal_start 958 / vassal_end 960 likewise.
- qin -822 gain zhou-dynasty -> zhou-dynasty (none): missing. zhou-dynasty.json has no loss to qin; the note calls it a recovery from the Xirong.
- qin -776 gain Xirong -> no dossier: exception. Listed in counterparts_needing_dossiers.
- qin -750 gain Quanrong -> zhou-dynasty -771 loss: exception. Quanrong listed; zhou-dynasty gives the land to the Quanrong in 771, consistent (also /ledger/5, -770).
- qin -409 loss wei -> no dossier: exception. wei.json not written yet (also -328, -290, -286, -225 gains from wei).
- qin -316 gain shu / ba -> no dossier: exception. Listed (ea-01-x).
- qin -316 gain Western Rong tribes; Rong, Shu and Chu border lands -> no dossier: exception. Free-text counterparts, not listed; suggest 'nobody' or a Rong dossier.
- qin -312 gain chu -> chu -312 loss: matched. Hanzhong, both confidence 1.
- qin -301 gain chu -> chu -301 loss: matched. 
- qin -299 gain chu -> chu -299 loss: matched. 
- qin -278 gain chu -> chu -278 loss: matched. Ying.
- qin -260 gain zhao -> no dossier: exception. zhao.json not written yet (also -228).
- qin -256 gain eastern-zhou -> eastern-zhou -256 loss: matched. Both confidence 3.
- qin -249 gain east-zhou -> no dossier: exception. No dossier; eastern-zhou.json /ledger/3 splits to the same name 'east-zhou' at -314, so the name agrees; listed by the author.
- qin -230 gain han -> no dossier: exception. han.json not written yet.
- qin -226 gain yan -> no dossier: exception. yan.json not written yet (also -222).
- qin -223 gain chu -> chu -223 dissolve: matched. Chu dissolves to qin; contest 224-223 matched too.
- qin -222 gain Dai (Prince Jia of Zhao) -> no dossier: exception. Listed.
- qin -222 gain Yue remnants (Wuyue region) -> no dossier: missing. Not listed in counterparts_needing_dossiers.
- zhou-dynasty -1046 vassal_start jin / lu / qi / qin -> no dossier: missing. zhou-dynasty.json tints song, cao, cai, chen, chu as vassals to 751 but not the four fiefs of this batch; neither side has the events (jin and qi notes claim a tint exists).

## Problems

- No page failed to load. Every infobox checked (Jin, Later Zhou, Lu, Qi, Qin) has no area figure, so area ratios are null.
- Reviewer edit applied: lu.json /ledger/3 confidence 2 to 1 with the Yue page's next sentence added to the note; re-validated (0 errors, 0 warnings) and read back.
- All confidence-3 events spot-checked (Jin 678/403/369, Later Zhou 951/956/958/960, Lu 249, Qi 866/859/386/284/279/221, Qin 325/316/256/249/230/228/225/223/222/221) were on their pages with the year; nothing fabricated.
- Systematic fault in jin, lu, qi: each new pre-750 fief keyframe (a disc of 5,000-15,000 km2) is followed by Cliopatria's full -750 shape with no ledger event at -750; qin handles it with a confidence-1 -750 gain.
- zhou-dynasty.json (another batch) gives vassal tints to song, cao, cai, chen, chu but not to jin, lu, qi, qin; route to whoever owns zhou-dynasty.
- qin and qin-dynasty: Cliopatria splits one state at -219/-218; the orchestrator should decide whether the qin-dynasty dossier (ea-02) continues this one.
