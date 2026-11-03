# Review of batch ea-03-c

Reviewer: adversarial reviewer, 2026-10-19. Dossiers: northern-wei, later-qin, former-qin, later-yan, later-liang. Validator (--resolve): 0 errors in all five; warnings only for counterparts without dossiers (dai-sixteen-kingdoms, six-garrisons-rebels, chouchi, zhai-wei) and the open chouchi vassalage in later-qin.

Verdict policy for this run: `fail` = an unapplied blocking finding (a keyframe verdict contradicted by the dossier's own cited page, a missing mirror for an existing neighbour's event, a fabricated or mis-dated confidence-3 event); `thin` = honest gaps and non-blocking fixes for a gap-filler; `fix` = every finding applied by the reviewer; `pass` = nothing found.

28 of 29 spot checks confirmed the note on the page; the one mis-dated event (later-yan /ledger/2, confidence 1) was fixed in place. No fabricated event was found.

## northern-wei: thin

Area: infobox 2000000 (450), Cliopatria 789976, ratio 0.39. Acknowledged in /keyframe_review/10 and partly repaired (Pingcheng, Shengle); corrected shape still about 0.47 of the infobox on the shapes.csv scale. The 451 shape (1,166,543) is within a factor of two.

Findings:

- `/keyframe_review/3`: The 395 shape (ok) adds about 154k grid km2 over the 394 shape, 136k of it Shanxi, and no ledger event moves Shanxi at all; the note itself says the gain cannot precede 396.  
  Evidence: Grid test: northern-wei_395 minus northern-wei_394 = 153,510 km2, Shanxi 135,554; later-yan_394 minus later-yan_395 = 153,763 km2, Shanxi 134,795 (Cliopatria hands Shanxi from Later Yan to Wei in 395). /ledger/1 (contest) and /ledger/3 (398 gain) use the Later Yan 395 shape, which holds no Shanxi. Neither the Northern Wei nor the Later Yan page dates a Shanxi (Bingzhou, Jinyang) transfer.  
  Fix: Add a 396 gain from later-yan, region Shanxi (Bingzhou round Taiyuan), with a page (gap-filler), and mark K3 adjust so the 395 year keeps the 394 outline (non-blocking: gap).
- `/ledger/11`: Luoyang, Hulao and Huatai, lost to Liu Song in 430, never return in the ledger; the 441-450 shape lacks Luoyang (point test) and only the 451 shape restores Henan, so the map shows Luoyang as Song land 430-450.  
  Evidence: Northern Wei page: 'Liu Song recovered the four cities of Luoyang, Hulao, Huatai and Qiao'ao'; the Wei recapture of 430-431 is not on the page (checked). The author flags this as a gap.  
  Fix: Add the Wei recapture (winter 430 to 431) as a gain from liu-song-dynasty from a page that dates it, e.g. Emperor Wen of Liu Song (non-blocking: gap).
- `/ledger/11/region`: The 80 km disc at Anyang stands for Huatai but also covers Ye and the land north of the Yellow River, which the page does not give to Liu Song.  
  Evidence: Northern Wei page names only Luoyang, Hulao, Huatai and Qiao'ao. Huatai is Hua County, about 60 km south of Anyang.  
  Fix: Use a Huatai/Hua County disc once the gazetteer has it (listed under gazetteer_names_needed) or shrink the disc (non-blocking).
- `/keyframe_review/4`: The 397-401 shape (ok) contains Chaoyang, which is Longcheng, the Later Yan capital 397-409; the same holds for the 387-396 shapes.  
  Evidence: Point test: Chaoyang (120.45 E, 41.57 N) lies inside northern-wei_387, _394, _395 and _397 and outside every Later Yan shape of 395-409 (0.28 degrees away).  
  Fix: Mark K4 (at least) adjust and remove a Liaoxi/Chaoyang disc; the later-yan dossier adds the same disc (non-blocking).
- `/keyframe_review/10/note`: The factor-of-two area gap is acknowledged but left unresolved.  
  Evidence: Infobox '450: 2,000,000 km2' against 789,976 km2 (shapes.csv) for 441-450, ratio 0.39. Measured on the project grid the raw shape is 951,409 km2 and the corrected shape 1,126,922 km2, which scales to about 0.94 M km2 on the shapes.csv measure: ratio about 0.47, still just beyond a factor of two.  
  Fix: After the Henan recapture (finding on /ledger/11) and the garrison belt are added, re-measure and state in the note which figure is followed and why (non-blocking: acknowledged).

For a gap-filler:

- `/keyframe_review/3`: The Wei capture of Bingzhou (Jinyang, Shanxi) in 396 (https://en.wikipedia.org/wiki/Emperor_Daowu_of_Northern_Wei)
- `/ledger/11`: The Wei recapture of Luoyang, Hulao and Huatai, 430-431 (https://en.wikipedia.org/wiki/Emperor_Wen_of_Liu_Song)
- `/ledger/21`: 441 gain of western Hexi (Jiuquan, Dunhuang) at confidence 1; the Northern Liang page gives only infobox capitals Jiuquan 440-441 and Dunhuang 441-442 (https://en.wikipedia.org/wiki/Juqu_Wuhui)
- `/ledger/32`: Six Garrisons revolt start (523) at confidence 1 and the rebel land 523-530 (https://en.wikipedia.org/wiki/Erzhu_Rong)
- `/ledger`: Wei conquests of Shanshan, Yanqi and Kucha (440s) and the 445 Tuyuhun campaign; none on the Northern Wei page (checked) (https://en.wikipedia.org/wiki/Emperor_Taiwu_of_Northern_Wei)

Spot checks: /ledger/16 Northern_Yan confirmed; /ledger/18 Northern_Yan confirmed; /ledger/20 Northern_Liang confirmed; /ledger/28 Emperor_Ming_of_Liu_Song confirmed; /ledger/7 Northern_Wei confirmed; /ledger/31 Northern_Wei confirmed

## later-qin: thin

Area: infobox None (None), Cliopatria 573288, ratio None. No area in the Later Qin infobox (checked).

Findings:

- `/ledger/15`: The Hexi (Guzang) loss to Southern Liang is put in 412 at confidence 1, but Guzang was already Northern Liang's by 411, so the cession must be earlier; the 407 and 410 keyframes (ok) keep Wuwei.  
  Evidence: Northern Liang page: 'The inhabitants of Guzang later surrendered to him in 411, and in 412, he made the city his new capital'; Later Qin page: Yao Xing gave up 'his holdings in the Hexi to the Southern Liang' (no year).  
  Fix: Date the cession from the Southern Liang page (standard accounts give 406), move the event, and mark K7/K8 adjust minus Wuwei (non-blocking: confidence 1).
- `/ledger/16`: The Ordos loss to Xia is put in 414 at confidence 1, though Xia was founded by Helian Bobo's rebellion in the Ordos in 407 (author's own notes: infobox 407).  
  Evidence: Later Qin page describes the rebellion without a year; ea-03-c notes give 407 from the infobox.  
  Fix: Date it from the Xia or Helian Bobo page (407) and mark K7 adjust (non-blocking: confidence 1).
- `/ledger`: Missing vassal_start for Western Shu in 407, although the page gives the year in the sentence the author used for Southern Yan.  
  Evidence: Later Qin page: 'In 407, he received Southern Yan and Western Shu's submissions.' western-jin /ledger/50 has Jin retake Sichuan from western-shu in 413.  
  Fix: Add vassal_start 407 cp western-shu (Later_Qin, confidence 3) and vassal_end 413 at Jin's conquest (non-blocking).
- `/ledger`: Missing loss of the twelve commanderies on the Han River ceded to Liu Yu (Eastern Jin).  
  Evidence: Later Qin page mentions the cession of twelve commanderies around the Han River to Liu Yu, with no year.  
  Fix: Add a loss cp western-jin at confidence 1 with the year from a page (non-blocking: gap).
- `/ledger/3/region`: The 386 contest zone is Cliopatria's Former Qin 387 shape, which former-qin marks wrong and which holds Later Qin's own capital Chang'an (later-qin K1/K2 give Chang'an to Later Qin from 386).  
  Evidence: former-qin /keyframe_review/8: the 387 shape is 'contradicted by the pages'; Later Qin page: 'In 386, Yao Chang occupied the city'.  
  Fix: Draw the zone between Chang'an and Fu Deng's seats (Pingliang, Tianshui), matching the former-qin corrections (non-blocking: confidence 1).

For a gap-filler:

- `/ledger/15`: Year of Yao Xing's cession of Guzang/Hexi to Southern Liang (https://en.wikipedia.org/wiki/Southern_Liang_(Sixteen_Kingdoms))
- `/ledger/16`: Year of the Ordos loss to Helian Bobo's Xia (https://en.wikipedia.org/wiki/Helian_Bobo)
- `/ledger/3`: Where the Later Qin-Former Qin fighting of 386-394 lay (Dajie 389, Feiqiao 394) (https://en.wikipedia.org/wiki/Yao_Chang)
- `/ledger`: Western Shu vassalage 407-413 and the Han River cession to Jin (https://en.wikipedia.org/wiki/Yao_Xing)

Spot checks: /ledger/6 Later_Qin confirmed; /ledger/7 Later_Qin confirmed; /ledger/8 Later_Qin confirmed; /ledger/10 Later_Qin confirmed; /ledger/11 Later_Qin confirmed; /ledger/12 Later_Qin confirmed

## former-qin: thin

Area: infobox None (None), Cliopatria 1798334, ratio None. No area in the Former Qin infobox (checked).

Findings:

- `/ledger/23/region`: The 394 loss to Later Qin (and the /ledger/24 dissolve) uses Cliopatria's Former Qin 392 shape minus Henan, the shape /keyframe_review/10 marks wrong; Fu Deng's corrected remnant (Longxi and Pingliang discs, Xining in 394) is handed to nobody.  
  Evidence: Grid test: the 392-minus-Henan region (142,888 km2) lies entirely inside later-qin's corrected 394 keyframe already, while only 14,415 of the 72,329 km2 remnant discs fall in it. Former Qin page: Fu Deng's 'main forces were destroyed' at Feiqiao (394); Fu Chong was killed by Western Qin.  
  Fix: Set /ledger/23 to the Pingliang (Fort Hukong) part of the K10 correction and /ledger/24 to the K11 correction; give Huangzhong (Xining) to western-qin; change later-qin /ledger/4 to match (non-blocking, but do both dossiers together).
- `/ledger/17`: The 385 loss of 'Longxi' (150 km disc) to Western Qin conflicts with the corrected keyframes 385-394, which keep a 100 km Longxi disc as Former Qin land.  
  Evidence: Western Qin page infobox: capital 'Yongshicheng (385-388)', then Jincheng (388-395); Former Qin page: Western Qin formed 'in the Longxi', Fu Deng acclaimed at Nan'an (386).  
  Fix: Put the Western Qin loss at its seat Yongshicheng (Yuzhong, near Lanzhou) or drop the Longxi disc from the 387-394 corrections (non-blocking).
- `/ledger`: Missing 385 loss to Chouchi: the Chouchi land gained in 371 (/ledger/4) never leaves the ledger.  
  Evidence: Former Qin page: 'In 385, the Qifu-Xianbei tribe formed the Western Qin dynasty in the Longxi and the Chouchi state was restored.' The author quoted the first half of this sentence in /ledger/17.  
  Fix: Add a 385 loss cp chouchi, region as /ledger/4 (Tianshui 200 km), confidence 2, source Former_Qin (non-blocking).
- `/wars`: Huan Wen's 354 northern expedition against Former Qin is missing.  
  Evidence: western-jin /ledger/29-30 records a 354 contest_start/contest_end with former-qin over Guanzhong (confidence 3).  
  Fix: Add the war (zone Guanzhong, contest 354) or explain its absence in notes (non-blocking).

For a gap-filler:

- `/ledger/11`: When Jin recovered Sichuan after 383 (confidence 1, pages silent) (https://en.wikipedia.org/wiki/Sixteen_Kingdoms)
- `/ledger/22`: End of the Western Qin vassalage (confidence 1) (https://en.wikipedia.org/wiki/Qifu_Qiangui)
- `/keyframe_review/8`: Extent of Fu Deng's domain 387-394 and the location of Fort Hukong (https://en.wikipedia.org/wiki/Fu_Deng)
- `/ledger`: Lu Guang's Western Regions campaign 382-384 (Kucha 384 is on the Later Liang page) (https://en.wikipedia.org/wiki/L%C3%BC_Guang)

Spot checks: /ledger/2 Former_Qin confirmed; /ledger/5 Former_Qin confirmed; /ledger/9 Former_Qin confirmed; /ledger/15 Battle_of_Fei_River confirmed; /ledger/18 Former_Qin confirmed; /ledger/21 Western_Qin confirmed

## later-yan: fail

Area: infobox None (None), Cliopatria 502851, ratio None. No area in the Later Yan infobox (checked).

Findings:

- `/keyframe_review/2`: BLOCKING: the 387-389 and 390-393 shapes (ok, /keyframe_review/2 and /3) hold Shandong, but the dossier's own cited page has Later Yan take Shandong from Jin only after the 394 conquest of Western Yan; the matching 394 gain is missing.  
  Evidence: Later Yan page: 'Then, he sent his generals to capture Shandong from the Eastern Jin dynasty' (after the 394 Western Yan campaign). Grid test: 198,526 of the 387 shape's 473,428 grid km2 are Shandong. western-jin /ledger/42 records the 394 loss of Shandong to later-yan; later-yan has no gain. The K2 note says 'No page opened dates Later Yan's hold on Shandong'.  
  Fix: Mark /keyframe_review/2 and /3 adjust with correction {minus: [Later Yan 387 or 390 shape, {admin1: Shandong, country: China}]}; add a 394 gain cp western-jin, region admin1 Shandong, confidence 2, source Later_Yan.
- `/ledger/2` (APPLIED): The 'page silent' gain from Former Qin was dated 386 at confidence 1; the page dates it to late 385.  
  Evidence: Later Yan page: 'Fu Pi finally abandoned Ye for Jinyang in late 385. Later Yan captured the city, and at this point had occupied most of Hebei.'  
  Fix: Year 386 -> 385, confidence 1 -> 2, note quotes the page (applied by the reviewer, revalidated: 0 errors).
- `/keyframe_review/5`: The 395-396 correction (Later Yan 395 shape) drops Shanxi (about 135k grid km2) with no loss event, although the page has Shanxi annexed in 394 and nothing moves it before the 396 Wei invasion.  
  Evidence: Grid test: later-yan_394 minus later-yan_395 = 153,763 km2, Shanxi 134,795. Later Yan page: 'annexing Shanxi for Later Yan' (394); Bingzhou/Jinyang in 396 not on page (checked).  
  Fix: Keep Shanxi in the 395 keyframe and add a 396 loss cp northern-wei, region Shanxi, from a page (non-blocking: gap; pairs with northern-wei).
- `/identity/capitals/1`: The capital Longcheng (120.45 E, 41.57 N) lies outside every Later Yan shape alive in 397-409, and the corrected keyframes K6-K8 do not add it.  
  Evidence: Point test: 0.28 degrees outside later-yan_395, _402 and _407; Cliopatria's Northern Wei 387-401 shapes hold Chaoyang instead.  
  Fix: Add {place: Chaoyang, km: 60} (or region Liaoxi) to the K6-K8 corrections (non-blocking).
- `/ledger/1`: The Goguryeo contest runs 385-404 as one 19-year zone; the Goguryeo page gives only the 385 invasion.  
  Evidence: Goguryeo page: Gogukyang 'invaded Later Yan ... in 385'; no later year. The goguryeo dossier dates the Liaodong fighting 405-406 from the Gwanggaeto page.  
  Fix: Close the 385 contest in 385 and open a second one for the Gwanggaeto wars (400-404) from the Gwanggaeto the Great page (non-blocking).

For a gap-filler:

- `/keyframe_review/5`: The 396 Wei capture of Bingzhou (Shanxi) from Later Yan (https://en.wikipedia.org/wiki/Murong_Bao)
- `/ledger/1`: Gwanggaeto's wars with Later Yan, 400-405 (https://en.wikipedia.org/wiki/Gwanggaeto_the_Great)
- `/keyframe_review/0`: Where Murong Chui held ground in 384 (Xingyang, the siege of Ye) (https://en.wikipedia.org/wiki/Murong_Chui)

Spot checks: /ledger/2 Later_Yan mis-dated; /ledger/4 Later_Yan confirmed; /ledger/5 Later_Yan confirmed; /ledger/12 Later_Yan confirmed; /ledger/14 Later_Yan confirmed; /ledger/15 Later_Yan confirmed

## later-liang: pass

Area: infobox None (None), Cliopatria 237231, ratio None. No area in the infobox (checked). Tried and failed to break: validator clean, capital Guzang inside every shape, the 386 gain and 403 loss mirrored by former-qin /ledger/18 and later-qin /ledger/10, the 401-403 Later Qin overlordship carried as vassal_* in later-qin (the schema puts vassal events in the suzerain's ledger) and as a contest here.

Spot checks: /ledger/0 Later_Liang_(Sixteen_Kingdoms) confirmed; /ledger/3 Western_Qin confirmed; /ledger/6 Later_Liang_(Sixteen_Kingdoms) confirmed; /ledger/8 Later_Qin confirmed; /ledger/9 Later_Liang_(Sixteen_Kingdoms) confirmed

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| northern-wei 386 found dai-sixteen-kingdoms | former-qin 386 loss | matched | former-qin /ledger/19 gives Hohhot to northern-wei; dai-sixteen-kingdoms is listed under counterparts_needing_dossiers |
| northern-wei 397 gain later-yan | later-yan 397 loss | matched |  |
| northern-wei 398 gain later-yan | later-yan 398 loss | matched |  |
| northern-wei 423 gain liu-song-dynasty |  | exception | liu-song-dynasty not written yet (ea-03 part that has not run) |
| northern-wei 427 gain xia |  | exception | xia not written yet (ea-03 part that has not run) |
| northern-wei 430 loss liu-song-dynasty |  | exception | liu-song-dynasty not written yet (ea-03 part that has not run) |
| northern-wei 431 gain xia |  | exception | xia not written yet (ea-03 part that has not run) |
| northern-wei 433 gain northern-yan |  | exception | northern-yan not written yet (ea-03 part that has not run) |
| northern-wei 436 gain northern-yan |  | exception | northern-yan not written yet (ea-03 part that has not run) |
| northern-wei 439 gain northern-liang |  | exception | northern-liang not written yet (ea-03 part that has not run) |
| northern-wei 441 gain northern-liang |  | exception | northern-liang not written yet (ea-03 part that has not run) |
| northern-wei 466 gain liu-song-dynasty |  | exception | liu-song-dynasty not written yet (ea-03 part that has not run) |
| northern-wei 468 gain liu-song-dynasty |  | exception | liu-song-dynasty not written yet (ea-03 part that has not run) |
| northern-wei 505 gain liang-dynasty |  | exception | liang-dynasty not written yet (ea-03 part that has not run) |
| northern-wei 534 split western-wei |  | exception | western-wei not written yet (ea-03 part that has not run) |
| northern-wei 534 split eastern-wei |  | exception | eastern-wei not written yet (ea-03 part that has not run) |
| northern-wei 396 gain (missing) later-yan |  | missing | Cliopatria moves Shanxi from Later Yan to Wei in 395; neither dossier has an event (both findings) |
| former-qin 370 gain former-yan | former-yan 370 dissolve | matched |  |
| former-qin 371 gain chouchi |  | exception | chouchi listed under counterparts_needing_dossiers |
| former-qin 373 gain western-jin | western-jin 373 loss | matched |  |
| former-qin 376 gain dai-sixteen-kingdoms |  | exception | listed under counterparts_needing_dossiers |
| former-qin 376 gain former-liang | former-liang 376 dissolve | matched |  |
| former-qin 379 gain western-jin | western-jin 379 loss | matched |  |
| former-qin 383 loss western-jin | western-jin 383 gain | matched | former-qin splits it in two (/ledger/11 Sichuan c1, /ledger/12); western-jin /ledger/37 takes the 383-minus-373 difference |
| former-qin 384 loss later-yan | later-yan 385 gain | matched | later-yan /ledger/0 found 384 cp former-qin and /ledger/2 gain, moved from 386 to 385 by this review |
| former-qin 384 loss later-qin | later-qin 384 found | matched |  |
| former-qin 385 loss western-yan |  | exception | western-yan not written yet (ea-03 part that has not run) |
| former-qin 385 loss western-qin |  | exception | western-qin not written yet (ea-03 part that has not run) |
| former-qin 385 loss (missing) chouchi |  | missing | Former Qin page: 'the Chouchi state was restored' in 385; no event in former-qin |
| former-qin 386 loss later-liang | later-liang 386 gain | matched |  |
| former-qin 386 loss northern-wei | northern-wei 386 found | matched | northern-wei names dai-sixteen-kingdoms as the found counterpart |
| former-qin 387 vassal_start western-qin |  | exception | western-qin not written yet (ea-03 part that has not run); schema puts vassal events in the suzerain's ledger only |
| former-qin 394 loss later-qin | later-qin 394 gain | mismatch | same spec on both sides, but it is the Former Qin 392 shape that former-qin marks wrong; the corrected remnant is handed to nobody (finding /ledger/23) |
| later-qin 386 gain western-yan |  | exception | western-yan not written yet (ea-03 part that has not run); former-qin /ledger/15 gives Chang'an to western-yan in 385 |
| later-qin 399 gain western-jin |  | missing | western-jin has no 399 loss of Luoyang to later-qin (Later Qin page: Luoyang captured in 399); route to the western-jin author |
| later-qin 400 gain western-qin |  | exception | western-qin not written yet (ea-03 part that has not run) |
| later-qin 401 vassal_start later-liang | later-liang 401 contest_start | exception | schema: vassal_* only in the suzerain's ledger; later-liang carries the siege as a contest |
| later-qin 403 gain later-liang | later-liang 403 loss | matched |  |
| later-qin 405 vassal_start chouchi |  | exception | listed under counterparts_needing_dossiers |
| later-qin 407 vassal_start southern-yan |  | exception | southern-yan not written yet (ea-03 part that has not run) |
| later-qin 409 loss western-qin |  | exception | western-qin not written yet (ea-03 part that has not run) |
| later-qin 412 loss southern-liang |  | exception | southern-liang not written yet (ea-03 part that has not run); year doubtful (finding) |
| later-qin 414 loss xia |  | exception | xia not written yet (ea-03 part that has not run); year doubtful (finding) |
| later-qin 416 loss western-jin | western-jin 417 gain | matched | western-jin /ledger/52 contest 416, /ledger/53 gain 417 covers Luoyang and Guanzhong |
| later-qin 417 loss western-jin | western-jin 417 gain | matched |  |
| later-yan 392 gain zhai-wei |  | exception | listed under counterparts_needing_dossiers |
| later-yan 394 gain western-yan |  | exception | western-yan not written yet (ea-03 part that has not run) |
| later-yan 394 gain (missing) western-jin | western-jin 394 loss | missing | western-jin /ledger/42 loses Shandong to later-yan in 394 (Later Yan page); later-yan has no gain and holds Shandong from 387 (blocking finding) |
| later-yan 394 gain (missing) western-jin | western-jin 394 loss | mismatch | western-jin /ledger/41 (c1) also loses Hebei and Henan to later-yan in 394 after gaining them from former-qin in 390 (/ledger/40, c1); neither former-qin nor later-yan has these events and Hebei was Later Yan's from 385; route to the western-jin author |
| later-yan 397 loss northern-wei | northern-wei 397 gain | matched |  |
| later-yan 398 loss northern-wei | northern-wei 398 gain | matched |  |
| later-yan 398 split southern-yan |  | exception | southern-yan not written yet (ea-03 part that has not run) |
| later-yan 404 loss goguryeo | goguryeo 406 gain | mismatch | two years apart: Later Yan page 'even losing Liaodong to Goguryeo in 404'; goguryeo /ledger/25 itself has Later Yan attack Goguryeo's Liaodong fortresses in 405; route to jk-02 to move its gain to 404 |
| later-liang 386 gain former-qin | former-qin 386 loss | matched |  |
| later-liang 395 vassal_start western-qin |  | exception | western-qin not written yet (ea-03 part that has not run) |
| later-liang 397 loss northern-liang |  | exception | northern-liang not written yet (ea-03 part that has not run) |
| later-liang 397 loss southern-liang |  | exception | southern-liang not written yet (ea-03 part that has not run) |
| later-liang 403 loss later-qin | later-qin 403 gain | matched |  |

## Problems

- WebFetch returns a model summary of the page, not raw text; quotes were checked against the summary's quotations.
- Neighbour dossiers not yet written (ea-03 parts that have not run): liu-song-dynasty, western-qin, xia, southern-qi, northern-yan, western-yan, liang-dynasty, southern-liang, northern-liang, southern-yan; their mirrors are exceptions.
- western-jin (another ea-03 part) has three events this batch cannot mirror: /ledger/40 (390 gain of Hebei and Henan from former-qin, c1), /ledger/41 (394 loss of the same to later-yan, c1), and no 399 loss of Luoyang to later-qin.
- goguryeo (jk-02) dates the Liaodong gain from later-yan to 406; the Later Yan page says 404.
- Area comparisons on the project grid (cells x 252.9 km2) read about 20 percent above shapes.csv areas in this latitude band; ratios use the shapes.csv scale.
- Reviewer applied one fix in place: later-yan /ledger/2 (year 386 -> 385, confidence 1 -> 2), revalidated with 0 errors and read back after 10 s.

Gazetteer names needed: Huatai, Longcheng, Yongshicheng, Shengle, Zhongshan, Nan'an, Tongwancheng, Fort Hukong.
