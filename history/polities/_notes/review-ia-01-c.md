# Review of batch ia-01-c (2026-10-18)

Dossiers: rouran-khaganate (fail), white-huns (fail), gokturk-khaganate (thin), yenisei-kyrgyz (thin, two small reviewer fixes applied), eastern-gokturks (fail, one confidence fix applied). Machine copy: history/notes/phase-b/reviews/ia-01-c.json.

Mechanical: all five validate with --resolve (0 errors; warnings only for counterparts without dossiers: kingdom-of-gaochang, fufuluo, alchon-huns, xueyantuo). Neighbour dossiers present: wusun, kidarites (others not run). Tang mirrors checked against _example-tang-dynasty.json (tang-dynasty.json not written yet).

Spot checks (14 page reads, none failed): every event checked said what its note claims, with the year. Rouran 402 (Gaoche, 11 March 402), 460 (Rouran page, Kan Bozhou in the same paragraph as 'In 460'), 487 (Gaoche), 555 (Rouran page); Hephthalites 466, 474, 479 Sogdia and Turfan, 557, 560; Peroz I 484 (Nishapur, Herat, Marw); Kavad I 513; First Turkic 552, area 6.0 M km2 (557), 23 Sept 626, 11 Sept 615, 27 March 630; Eastern Turkic 553-572 Muqan and the Kyrgyz, 629 six armies, 630, Ordos Loop (undated, after 630), 639, 642, 645, area 4.0 M km2 (624); Western Turkic c. 567-576; Uyghur 840, Baikal-Irtysh (undated), 890; Kyrgyz Khaganate (Drompp: 'after their victories in the 840s', 1207/1208); Yenisei Kyrgyz homeland and 758. No fabricated or mis-dated event found.

Areas: Rouran 2.8 M km2 (405) vs 3.87 M (ratio 0.72); Göktürk 6.0 M (557) vs 4.98 M (1.20); Eastern Turks 4.0 M (624) vs 2.68 M (1.49); Hephthalites and Kyrgyz: no infobox area (checked). All acknowledged in keyframe notes.

Region numbers below are gazetteer cell counts (H3 r5, about 237 km2 per cell), computed with tools/gazetteer.py.

## rouran-khaganate: fail
1. /keyframe_review/9 and /10: the 480-533 and 534-545 keyframes keep Dzungaria (1,778 cells, about 420,000 km2) that /ledger/3 gives to the Fufuluo in 487 and /ledger/4 takes back in 541. Split K9 at 487 and K10 at 541 with Dzungaria removed for 487-540.
2. /keyframe_review/8-11: Turfan-Hami (619 cells) stays Rouran land 479-554 in every keyframe while white-huns /ledger/6 gains it in 479. The notes flag the disagreement, but the data now draws the same land for two states. Pick one reading and align both dossiers.
3. /keyframe_review/4: 268 Ordos cells leave in 426 with no event (K4 ok keeps them). The Rouran page puts 'a Wei offensive that drove the Rouran from the Ordos region' at the start of the conflict, so the simplest fix is minus-Ordos on K0-K4 too.
4. /ledger/7 and identity.successors: the dissolve spec (Cliopatria Rouran 554) still includes the Ordos (701 cells) and 1,972 Manchurian and North-China fringe cells that the Göktürk 555 shape does not take.
Thin: 479 vassal_end and 541 gain at confidence 1; the extent before 460; the 480 Liaoxi strip; Mumocheng unlocated.

## white-huns: fail
1. /ledger/6 (479 Turfan-Hami gain): no keyframe has a single Turfan cell, and no later event loses it. It conflicts with the Rouran keyframes (see above).
2. /ledger/5 (479 Sogdia gain from kidarites): kidarites.json ends in 467 (/ledger/10), with no 479 loss. Sogdia (813 cells, all inside Transoxiana) was already gained with Transoxiana in 466 (/ledger/3) and is in the 451 keyframe from 466. Fix the counterpart and remove the double gain.
3. /keyframe_review/2: the 451 shape applied from 466 holds all of Bactria (825 cells, 521 in the Kunduz core) although /ledger/4 dates Bactria to 474 (from the Sasanians, matching kidarites /ledger/9). Non-blocking: add a 466-473 keyframe or a note.
Thin: the Indian lands at confidence 1 (Alchon or Hephthalite); Turk Shahis 560 at confidence 1; the south-of-Oxus remainder (about 25% of the last shape) goes to no successor; the 534 loss to 'nobody'.

## gokturk-khaganate: thin (budget 1-2 pages)
1. /keyframe_review/1: 4,967 cells of the 555 shape (Kazakh Steppe 3,334, Semirechye 942, Altai 567; about 1.18 M km2) lie outside the Rouran land and have no event. A 555 gain cp=nobody at confidence 1 would close it; a gap-filler should date Istämi's campaigns.
2. /ledger/4: the 555 gain spec is the full Rouran 554 shape, including the Ordos the Rouran dossier removes (701 cells; 692 are in the Göktürk 555 shape).
Six confidence-1 events (553/586 Kyrgyz vassalage, 561 steppe, 586 split and dissolve) are honest bridges.

## yenisei-kyrgyz: thin (reviewer fixes applied)
Applied: capital Ordu-Baliq ends 849, not 925 (the dossier's own 850 loss leaves no Kyrgyz land on the Orkhon; Drompp on the page: no significant presence 'after their victories in the 840s'), and the K4 note now reads '(ledger 763; the Uyghur conquest itself is 758)'. Re-validated, 0 errors.
Open: for 840-849 the Ordu-Baliq point is still 50-100 km outside the 840 correction (22 of the 289 Orkhon cells; bbox lat min 47.66). Add the Orkhon Valley to K5 and /ledger/2, or drop the point. The Orkhon war zone (/wars/2) has no contest events.
Thin: 850-1205 is one shape with no event; three events at confidence 1; no seat for 555-839 and 850-1208 (the Kyrgyz Khaganate infobox names the Uybat River settlement, Kemičket from 925 and Khagan-Kirghiz).

## eastern-gokturks: fail (reviewer fix applied)
Applied: /ledger/5-7 (629-630) confidence 3 -> 2. The page names no land for the campaign, only 'a 1,200 km front'.
1. /keyframe_review/7: the 630 Ordos keyframe (884 cells) has no gain behind it. The ledger strips every cell of the 628 shape in 630 (intersect(Ordos, EG 630) = 0), and /ledger/7 hands the Tang the 136 Ordos cells that K7 keeps. Add a 630 gain cp=tang-dynasty of the Ordos (the resettlement) and exclude the Ordos from /ledger/7.
2. /keyframe_review/9-10: in 639 the 679 Ordos cells outside the Hetao leave with no event, and in 642 they return with no event. /ledger/10's Hetao loss also removes the 205 Hetao cells inside the Ordos that K10 keeps. Add a 639 loss and a 642 gain of minus[Ordos, Hetao] against the Tang, and write /ledger/10 as minus[Hetao, Ordos].
3. Cross-dossier: the 639 gain from the Tang has no Tang loss in the worked example (the Tang records 630-645 only as a vassal tint). ea-04 and this dossier must use one convention.
Thin: 617/623 Ordos at confidence 1 (probably Liang Shidu's Shuofang regime under the Turks); 627 contest_end at confidence 1; the 612 cells (unverified: page budget, not a fault); no seat 631-645.

## Cross-dossier
Matched: Rouran-Göktürk 552-555; Kidarites-Hephthalites 450-466; Hephthalites-Göktürk 557-560; Göktürk split into the Eastern Turks 586/587; Eastern Turks-Tang 630 and 645 (against the example). Mismatches: Turfan 479 (Rouran keeps it, Hephthalites gain it); Sogdia 479 from the dissolved Kidarites; Hetao 639 (no Tang mirror). Everything else is an exception: counterpart nobody, listed new states (kingdom-of-gaochang, fufuluo, alchon-huns, xueyantuo, second-turkic-khaganate, principality-of-chaghaniyan), or groups not run yet (sasanian-empire me-06, gupta-empire sa-02, turk-shahis sa-03, sui-dynasty ea-03, tang-dynasty ea-04, western-gokturks/uyghur-khaganate ia-01-d, mongol-empire ia-02). Vassal events are suzerain-only by the schema, so the Kyrgyz vassalage has no mirror by design.
