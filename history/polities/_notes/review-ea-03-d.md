# Review of batch ea-03-d (Western Qin, Western Yan, Northern Liang, Southern Liang, Southern Yan, Western Liang)

Reviewer, 2026-10-19. Machine copy: history/notes/phase-b/reviews/ea-03-d.json.

Mechanical checks: `validate_dossier.py --resolve` passes all six with no errors and no warnings (also after the reviewer's edits). File names equal slugs; `cliopatria_names` match polities.csv; every Cliopatria shape has a verdict; new keyframes carry from, to and a correction; ledgers are sorted with `found` at start and `dissolve` at end. No infobox of the six gives an area, so no factor-of-two test was possible (the author says so). Neighbour dossiers read: tuyuhun, rouran-khaganate, later-qin, protectorate-of-the-western-regions, western-jin, later-liang, northern-wei, former-qin, later-yan; xia and liu-song-dynasty are not written yet (group ea-03, exception).

Pages opened by the reviewer: Western Qin, Northern Liang, Western Liang (Sixteen Kingdoms), Southern Liang (Sixteen Kingdoms), Western Yan, Southern Yan, Qifu Chipan, Juqu Wuhui. Grid tests used tools/grid.py (H3 r5).

## Verdicts

| slug | verdict | in short |
| --- | --- | --- |
| western-qin | fail | 387 keyframe grows sixfold with no event; 426 loss names the wrong counterpart and disagrees with the Tuyuhun dossier |
| western-yan | pass | four events checked, all on the page |
| northern-liang | thin | two confidence fixes applied by the reviewer; the 439-441 holdout is overstated (Juqu Wuhui page) |
| southern-liang | pass | four events checked; the wrong-shape verdict confirmed by grid test |
| southern-yan | pass | five events checked, all on the page |
| western-liang | fix | applied by the reviewer: 421 dissolve confidence 2 to 3 (Dunhuang is on the page) |

## western-qin: fail

- `/keyframe_review/1` (blocking). The 387 shape is marked ok (516 grid cells, about 114,000 km2, Lanzhou to Tianshui) although the 385-386 keyframe is a Lanzhou 80 km disc and `/ledger/2` says the whole of Longxi was taken only in 394 ("the gain is already in the 387 shape"). The map grows about sixfold in 387 with no ledger event.
  Evidence: grid test, only 32 of the 387 shape's 516 cells lie within 80 km of Lanzhou (129 within 150 km). Western Qin page: "The Qifu occupied the whole of Longxi after killing Fu Chong and the Chouchi ruler, Yang Ding" (394). Between 385 and 394 the ledger has only the 388 capital move. The Former Qin dossier (`/ledger/17`) gives "Longxi" (150 km disc) to the Western Qin in 385, a third reading.
  Fix: mark K1 adjust with a 387-393 correction that is the founding core as a page dates it (for example Lanzhou 150 km, "Yuanchuan, Jincheng and the Yongshi River area"), so that the 394 gain draws the rest of Longxi; or, if a page puts the Qifu across Longxi before 394, add that gain with its year and narrow `/ledger/2` to Fu Deng's last land. Make `/ledger/0` and Former Qin's 385 loss describe the same land.
- `/ledger/9` (blocking). The 426 loss of the Huangshui land to the Tuyuhun (confidence 1, bridged from Cliopatria) names the wrong counterpart and disagrees with the Tuyuhun dossier.
  Evidence: Qifu Chipan page: in 426 Helian Chang "sent his general Hulu Gu" against Yuanchuan and Wei Fa against Nan'an; "Nan'an fell, at great loss"; "In winter 426, Xia forces commanded by Hulu and Wei attacked Fuhan, forcing Qifu Chipan to move the capital to Dinglian"; "Hulu and Wei then captured another important Western Qin city, Xiping", and then withdrew. No Tuyuhun in 426. Grid test: all 131 cells the Western Qin shape drops in 426 are in Cliopatria's Tuyuhun 426 shape, and tuyuhun `/ledger/1` gains exactly that land (Tuyuhun 426 minus 414) in 430, from the Western Qin page's "the rest of Qin's territory was conquered by the Tuyuhun".
  Fix: replace `/ledger/9` with the Xia raid of 426 (contest_start/contest_end with xia over Nan'an and Xiping, or a loss and a regain if the author reads a holding), source https://en.wikipedia.org/wiki/Qifu_Chipan (add to sources); keep the Huangshui (Xining 100 km) in `/keyframe_review/8` for 426-429; let `/ledger/12` (430 loss to tuyuhun) include the Huangshui, matching tuyuhun `/ledger/1`.
- `/identity/predecessors` (non-blocking). The Southern Liang, absorbed in 414 (`/ledger/8`), is missing; southern-liang lists western-qin as successor. Add it with the Huangshui land.
- `/identity/capitals` (non-blocking). Qifu Chipan page: capital to Dinglian in winter 426 and "In 427, Qifu Chipan moved his capital back to Fuhan"; the dossier has Fuhan 412-428 unbroken. Add or note.
- Spot checks: `/ledger/2` 394 confirmed; `/ledger/4` 400 confirmed (page also tells the surrender to Southern Liang); `/ledger/8` 414 confirmed (Southern Liang page, Qifu Chipan page); `/ledger/9` 426 not on page as claimed (see above); `/ledger/12` 430 confirmed; `/ledger/13` 431 confirmed. Capitals match the infobox.
- Thin: Xicheng and Tanjiao share a placeholder coordinate (105.22, 35.15); the 410 commanderies are unnamed (author's gaps).

## northern-liang: thin (reviewer fixes applied)

- Applied `/ledger/11`: the 441 loss to the Northern Wei rested on Cliopatria alone (confidence 1). Juqu Wuhui page: "In spring 440, Juqu Wuhui tried to recapture Jiuquan", "soon capturing it", and "by winter 441, Jiuquan fell to Northern Wei forces". Confidence 2, source https://en.wikipedia.org/wiki/Juqu_Wuhui, added to `sources[]`.
- Applied `/ledger/8`: confidence 2 to 3. Western Liang page: Li Xun "succeeded him in Dunhuang" and "the city eventually fell and Li Xun committed suicide in 421".
- End year: keep 442. The Northern Liang page says 397-439 but its infobox gives Jiuquan 440-441 and Dunhuang 441-442, and the Juqu Wuhui page: "in 442, Juqu Wuhui abandoned Dunhuang". The Northern Wei dossier's 441 gain (including Dunhuang) is within a year of the 442 dissolve.
- Thin (gap-filler) `/ledger/9`, `/keyframe_review/7`: the holdout of 439-441 is overstated. The Juqu Wuhui page has Wuhui flee Jiuquan after the 439 attacks "first to Jinchang, then to Dunhuang", retake Jiuquan in spring 440 and lose it by winter 441. The dossier keeps Cliopatria's 439 shape (Zhangye to Dunhuang) for 439-440 and loses only Wuwei in 439. Suggested ledger: 439 loss of Guzang, Zhangye and Jiuquan to northern-wei; 440 gain of Jiuquan from northern-wei; 441 loss of Jiuquan; 442 dissolve at Dunhuang; K7 becomes Dunhuang and Jinchang (439) plus Jiuquan (440); the Northern Wei dossier mirrors.
- Thin `/identity/rulers`: no ruler for 439-442 (Mujian ends 439; Wuhui given 442 only). The Juqu Wuhui page names him leader of the holdout but gives no start year (infobox reign 443-444; succession box Prince of Hexi 442-444).
- Thin `/ledger/1`: the commanderies Mengxun took in 398 (author's gap).
- Spot checks: `/ledger/3` 400, `/ledger/4` 401, `/ledger/5` 411, `/ledger/7` 420, `/ledger/9` 439 and `/ledger/11` 441 all confirmed. Capitals match the infobox.

## southern-liang: pass

- Grid test confirms the author: only 6 of the Cliopatria shape's 139 cells lie within 120 km of Xining, so `wrong` with a Xining disc is right; the disc (about 31,000 km2) matches Cliopatria's area.
- Spot checks: `/ledger/0` 397, `/ledger/3` 406 Guzang ("In 406, Qin rewarded Rutan's loyalty by handing him control over Guzang"), `/ledger/5` 410, `/ledger/7` 414 all confirmed.
- Tried and did not break: capitals against the infobox (the brief Ledu seat of 398-399 is acknowledged in `/ledger/1`), the 404-408 suspension (vassalage is the suzerain's event; Later Qin lacks it, see the matrix), coordinates.
- Neighbour faults (not this dossier's): later-qin `/ledger/15` dates the Guzang hand-over 412 at confidence 1 (should be 406, counterpart southern-liang); later-liang `/ledger/7` draws the 397 breakaway with Cliopatria's misplaced Southern Liang shape (Linxia-Lintao), which this dossier marks wrong.
- Optional lead for a gap-filler: the page is silent on Jincheng (Lanzhou), which other accounts give to Tufa Wugu in 397.

## southern-yan: pass

- Spot checks: `/ledger/0` 398 Huatai, `/ledger/1` 399 Huatai to Wei through a traitor, `/ledger/2` 399 Qing Province ("corresponds to modern central and eastern Shandong"), `/ledger/5` and `/ledger/6` 410 Guanggu all confirmed; capitals Huatai 398-399 and Guanggu 399-410 as the infobox.
- Neighbour faults: northern-wei lacks the 399 gain of Huatai; western-jin lacks the 399 loss of Qing Province.

## western-yan: pass

- Spot checks: `/ledger/1` 385 Chang'an, `/ledger/3` 386 abandonment (the page names no taker; later-qin has the gain), `/ledger/4` 386 Zhangzi ("Yong then occupied Fu Pi's capital at Zhangzi"), `/ledger/6` 394 all confirmed.
- Neighbour fault: former-qin has no 386 loss of Zhangzi to the Western Yan.

## western-liang: fix (applied by the reviewer)

- Applied `/ledger/4`: confidence 2 to 3; the page has Li Xun succeed "in Dunhuang" before the city fell in 421 (answers the author's gap).
- Spot checks: `/ledger/0` 400, `/ledger/1` 401, `/ledger/3` 420 (infobox "Fall of Jiuquan: 420"), `/ledger/4` 421 confirmed. The Wikidata clash with later-western-liang is handled in notes.

## Cross-dossier matrix: what needs routing

- Mismatch: western-qin 426 loss to tuyuhun (no mirror; tuyuhun gains the same land in 430). Fix on the Western Qin side.
- Mismatch: western-qin 385 found (Lanzhou 80 km) against former-qin 385 loss "Longxi" (150 km); former-qin has no 394 loss to western-qin (only a confidence-1 vassal_end).
- Mismatch: southern-liang 406 gain of Guzang against later-qin 412 loss (confidence 1): later-qin should move it to 406.
- Mismatch on land: later-liang 397 loss to southern-liang uses the misplaced Cliopatria shape.
- Missing: former-qin 386 loss of Zhangzi to western-yan; northern-wei 399 gain of Huatai from southern-yan; western-jin 399 loss of Qing Province to southern-yan.
- Missing suzerain events: later-qin vassal_start/vassal_end southern-liang (404-408); northern-wei vassal_start northern-liang (431-439).
- Contest on one side only: later-liang contest with western-qin 391-395; western-qin's war has empty zones and says no land changed hands.
- Exceptions: western-qin 431 dissolve to xia (xia not written yet, ea-03).
- Everything else matched within a year (see the JSON).
