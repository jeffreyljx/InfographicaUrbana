# Review of batch jk-02-b (goguryeo, baekje, dong-okjeo, tamna)

Reviewer, 2026-10-19. Inputs: author brief notes/phase-b/briefs/jk-02-b.md, report notes/phase-b/reports/jk-02-b.json, notes _notes/jk-02-b.md. Neighbour dossiers that exist and were read: dongye, mahan, byeonhan, jinhan, xianbei, rouran-khaganate (plus gaya, gojoseon for counterparts). Not yet written (groups or parts not yet run): silla, unified-silla, han-dynasty, xin-dynasty, cao-wei, western-jin, former-yan, later-yan, northern-wei, sui-dynasty, tang-dynasty, goryeo, joseon, yuan-dynasty and the rest of section 6.

Validator (--resolve): 0 errors in all four. Warnings: goguryeo counterparts buyeo (4) and lelang-commandery (listed in counterparts_needing_dossiers) and the intentional empty correction of goguryeo_674; dong-okjeo lelang-commandery. Every Cliopatria shape has a verdict (goguryeo 26 + 3 new, baekje 6 + 4 new, dong-okjeo 4 + 1 new, tamna 3 + 2 new). Every area delta the author quotes was recomputed from shapes.csv and is right (e.g. goguryeo 154 +31,977 = Dong-okjeo 31,981; 392 +31,200 = Dongye; 410 +105,909; 555 -48,325 vs Silla +48,888; Baekje 392 -1,797, 395 -4,676, 476 -8,504).

Area check: none of the four pages has an infobox area (confirmed: Goguryeo has only '7th century: approx. 3,500,000' people; Baekje, Okjeo, Tamna none). Acknowledged in keyframe notes. Cliopatria maxima: goguryeo 408,926; baekje 49,731; dong-okjeo 32,149; tamna 1,959.

Reviewer edits (small, verified on the page opened, each re-validated: 0 errors):
- goguryeo /ledger/5 (22, Dongbuyeo): confidence 1 -> 2. The Daemusin page dates it: 'He annexed Dongbuyeo and killed its king Daeso in 22 AD'; only the place is a placeholder.
- goguryeo /ledger/47 note: removed 'Li Ji crossed the Yalu'; the Goguryeo-Tang War page has no Yalu crossing by Li Shiji (only Qibi Heli's 661 battle there).
- baekje /keyframe_review/3 note: 'holds no Hwanghae' contradicted the Geunchogo page ('parts of Gangwon and Hwanghae Provinces'); now quotes it and keeps the outline.
- baekje /identity/capitals: the 132 capital_move had no destination in capitals; split Wiryeseong at 131 and added Bukhansanseong 132..370 (Baekje page: 'King Gaeru is believed to have moved the capital north of the river to Bukhansanseong in 132'), Seoul coordinate as for the other Seoul capitals.
- tamna /wars/0/zones: was empty, but the page has the rebellion end 'on Jeju Island in 1274'; zone set to Jeju.

## goguryeo: thin

Spot checks (all confirmed with year): 26 Gaema-guk 'along the Amnok River'; 37 'destroyed Nangnang'; 44 Han 'captured it in 44'; 313 'annexed by Goguryeo under King Micheon'; -36/-33/-28 Biryu, Haeng-in, Northern Okjeo; 406 'conquered all of Liaodong' (no year in the sentence, after 405-406: c2 right); 410 'attacked Eastern Buyeo to the northeast' (outcome not stated: c2 acceptable); 468 Gangwon, 475 Wiryeseong, 489 '7 walled cities' North Gyeongsang; 645 crossing 1 May, withdrawal 13 October; Pyongyang 22 October (668 from context); 612 buffer zone sentence (undated: c1 right); 491 'completely annexed Buyeo' (no year: c1 right). Nothing fabricated. Capitals inside the shapes' bboxes.

Gaps for a gap-filler (the dossier is honest; these are what the ledger does not explain):
- /keyframe_review/8 goguryeo_306 (+7,189 km2): no event. Try https://en.wikipedia.org/wiki/Micheon_of_Goguryeo (his attacks on Xuantu and the Liaodong border before 313).
- /ledger/39, /ledger/42: the 612 loss and 617 recovery of 52,939 km2 are confidence 1 (the Sui War page gives only 'gave up the buffer zone that he had acquired after the war of 598'). Try https://en.wikipedia.org/wiki/Yeongyang_of_Goguryeo.
- Missing small events found on pages already opened: 398 'Gwanggaeto conquered the Sushen people to the northeast' (Gwanggaeto page; inside the 395..401 shape, probably part of the 410 increment); Taejo's 'Galsa in 68, Jona in 72, and Juna in 74' (Taejo page; inside 60..153). Add as gains (counterpart nobody), confidence 2.
- Other confidence-1 events: /ledger/1, /ledger/2 (Biryu, Haengin unplaced: try https://en.wikipedia.org/wiki/Dongmyeong_of_Goguryeo), /ledger/11 (Ye vassal from 53), /ledger/21-24 (401 annexations of the Ye and Okjeo: try https://en.wikipedia.org/wiki/Gwanggaeto_Stele), /ledger/31 (468 end of the Silla protectorate), /ledger/34 (491 Buyeo: try https://en.wikipedia.org/wiki/Munjamyeong_of_Goguryeo).

Advisories (not blocking):
- /keyframe_review/19 goguryeo_480 is 'ok' although the ledger dates its +18,364 km2 to 468 and 489; 'adjust' with the years would be more honest.
- /ledger/8, /ledger/10 name han-dynasty for Nangnang in 37/44 while /ledger/15 names lelang-commandery for the same land in 313; once jk-02-x writes lelang-commandery (-108..313) all three should use it, or the 37/44 events should say why Han.
- /ledger/37: the 553 loss region (523 shape minus 555 shape) includes the Gyeonggi land already lost to Baekje in 551 (/ledger/35); subtract Gyeonggi from it.
- Dongye: dongye_392 runs to 401 and the Dongye dossier ends 401, while goguryeo draws the Ye from 401 (K13 valid to 400): a one-year overlap in 401 (also flagged by the jk-02-a review). One side should move.

## baekje: fix (fixed by the reviewer)

Spot checks (confirmed): founding 18 BCE by Onjo, 'initially belonged to the Mahan confederacy'; 132 Bukhansanseong; 369 'The remaining tribes of Mahan were annexed in 369 ... Jeolla'; 475 'the Seoul region fell to Goguryeo', Ungjin 475-538; 538 Sabi; 551 'Baekje regained its original capital in 551'; Hwangsanbeol infobox 9 July 660, 'surrounded Gongju and King Uija surrendered'; Tamna 476 (text) / 498 (infobox). Rename to Nambuyeo has no year on the Seong page (c1 right).

Advisories (not blocking, mostly for the Mahan dossier, jk-02-a):
- /ledger/3 (369 gain, counterpart mahan): the Mahan dossier ends 346, so for 347..368 Jeolla (removed from baekje_347 by /keyframe_review/2) is drawn by nobody, and the 369 counterpart no longer exists. The page supports 'remaining tribes of Mahan' to 369: the Mahan dossier should carry a Jeolla-only remnant 347..369 with a 369 dissolve or loss to baekje.
- /ledger/0, /ledger/2: the Mahan dossier draws the whole Mahan shape to 346 with no loss, so it overlaps baekje_-18 and baekje_234 (Gyeonggi and Chungcheong); Mahan should lose the Baekje core (or the overlap rule should be written down).
- /wars/5 (restoration, 660..663) runs past the end (660). The Baekje page gives the movement a base at Juryu but no held territory or duration, so 'war only' is defensible; either clip to 660 with the 663 end in note or move it to the Tang/Silla dossiers.
Gaps: /ledger/2 (234, c1: try https://en.wikipedia.org/wiki/Goi_of_Baekje), /ledger/13 (538 rename, c1), the 642 campaign of Uija against Silla's western fortresses (absent from the Baekje page; try https://en.wikipedia.org/wiki/Uija_of_Baekje).

## dong-okjeo: thin (by design)

Okjeo page confirmed: 'perhaps the 2nd century BCE to the 5th century CE'; 'roughly the area of the Hamgyong provinces'; Gojoseon to 108 BCE, Xuantu 107 BCE, 'eastern part of the Lelang Commandery'; Taejo 'reduced Okjeo to a tributary' (1st or 2nd century); 'In early 5th century, Okjeo was completely conquered by Gwanggaeto'. Taejo page: 'Eastern Okjeo in 56'. Both ledger events are confidence 1 and honest; the 154..400 vassal keyframe is consistent with goguryeo (K6..K13 subtract it to 400). The vassal events live only in the suzerain's ledger, which is what the schema prescribes ('counterpart is the vassal itself in both events'); the dossier's notes say so. Gaps: /ledger/0 (when Okjeo left Lelang: try the Lelang Commandery page on the eastern division), /ledger/1 (the 401 year: try https://en.wikipedia.org/wiki/Gwanggaeto_Stele).

## tamna: fix (fixed by the reviewer)

Tamna page confirmed: no founding record, first reference 'may come in the 3rd century CE' (Sanguozhi); 476 Baekje tribute; infobox Silla 662-925, independent 925-938, Goryeo vassal 938-1105, local autonomy 1105-1275 and 1301-1392, Yuan Tamna Prefecture 1275-1301, Joseon 1392-1404; 1274 Sambyeolcho end; 1402 Go Bong-rye; 1404 end. One state, the split question answered correctly; the extension to 1404 and keyframes 682..935 and 1279..1404 rest on the infobox. /ledger/0 (263) is c1 and probably cannot be improved. The suzerain events (Silla 662, Goryeo 938, Yuan 1275, Joseon 1392) must go into those dossiers, none written yet; unified-silla_682..935 must subtract Jeju.

## Cross-dossier

Goguryeo-Baekje pairs all match (392 gain/loss and contest 392-396, 395, 475, 551 gain/loss and contest 551-553). Goguryeo 401 gains from dongye and dong-okjeo mirror their 401 dissolves (successor goguryeo). Vassal events (goguryeo over dongye 53, dong-okjeo 56, silla 400; baekje over tamna 476) are suzerain-side only, per the schema. Mismatches: baekje-mahan (above). Everything else waits for unwritten dossiers: silla (400, 468, 489, 553), han-dynasty (37, 44), cao-wei (244-245), later-yan (405-406), sui-dynasty (612-617), tang-dynasty (645, 667-668, 660 and 668 successors), joseon (1404), and the jk-02-x additions buyeo, lelang-commandery, northern-okjeo, protectorate-general-to-pacify-the-east.
