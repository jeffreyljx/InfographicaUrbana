# Review of batch jk-02-x (Korea additions: colonies, rebels, Manchurian states)

Reviewer: adversarial review, 2026-10-19. Read: the reviewer brief, the author's brief (sections 6 and 10), report and notes, and all 19 dossiers (by script). The neighbour dossiers present in polities/ were read: from the section-6 context list, xianbei, xiongnu, rouran-khaganate and warring-states-japan (none carries an event against this batch); from the Korean counterparts, goguryeo, gojoseon, dongye, dong-okjeo, baekje, silla, balhae, goryeo, tamna, empire-of-japan, republic-of-korea and democratic-people-s-republic-of-korea. All other section-6 context polities (han-dynasty, cao-wei, western-jin, tang-dynasty, liao-dynasty, mongol-empire, yuan-dynasty, former-yan and the rest) are not written yet; their events count as the brief's exception, a counterpart owned by a group that has not run yet.

Validator (`--resolve`): 0 errors in all 19. The warnings are the ones expected: Seocheon is not in the gazetteer, and murong-xianbei has no dossier.

Spot checks: 24 Wikipedia pages opened, at least 3 events per dossier (every event for the small ones), weighted to confidence-3 events and to the moves that shift the most land. No event was fabricated or mis-dated. One event had its direction reversed (Lelang 313). No infobox carries an area, and there is no Cliopatria row to compare against, so the area check is empty throughout. The author says so.

## Verdicts

| dossier | verdict | in one line |
| --- | --- | --- |
| lelang-commandery | fix (applied) | 313 'gain' from Goguryeo reversed to 'loss'; region set to the 204 keyframe (Hwanghae was Daifang's). Open: Gyeonggi placeholder drops at 204 with no event |
| xuantu-commandery | thin | 75 BCE placements and the Fushun retreat at confidence 1; the founding sentence also says 'part of the Liaodong Peninsula', which KF0 ignores |
| daifang-commandery | pass | all four events confirmed on the Daifang and Four Commanderies pages |
| lintun-commandery | pass | confirmed; note misquotes Four Commanderies as 107 BCE (the page says 108 for all three), harmless |
| zhenfan-commandery | thin | the site is unknown on the page; the Gyeonggi placeholder is honest at confidence 1 |
| wang-tiao | pass | 25 and 30 CE confirmed on the Lelang page |
| gongsun-liaodong | thin | 209 'seized some of its territory' is modelled as a same-year contest with no gain |
| buyeo | thin | the 285 eastern branch has no gain event; the -86 split land lies outside Buyeo's own KF0; three confidence-1 bridges |
| eastern-buyeo | pass | 86 BCE and 22 CE confirmed; possible overlap with Cliopatria goguryeo_-36 is a lead for goguryeo |
| dongdan | pass | 926, 928, 936 confirmed; family 'korea' for a Liao puppet is a colour question |
| jeongan | fix (applied) | found counterpart dongdan to liao-dynasty; 986 events confidence 3 to 2 (no site on the page) |
| ungjin-commandery | pass | 660-671, July 670, 671 confirmed |
| baekje-restoration-movement | thin | 660-661 'Baekje (core)' placeholder overlays all of Ungjin; Juryu's fall undated; silla has no 663 gain |
| protectorate-general-to-pacify-the-east | pass | 668-12, 676-2, 676 (Taedong, Gibeolpo November) confirmed; stale note about Ungjin |
| ssangseong-prefecture | pass | 1258 and 1356 confirmed |
| dongnyeong-prefecture | fix (applied) | the page dates the rising and surrender to October 1269; month 10 added to the found and to start |
| sambyeolcho | thin | 1271 Jindo-to-Jeju move is a confidence-1 bridge |
| united-states-army-military-government-in-korea | pass | 9 Sep 1945 to 15 Aug 1948 confirmed |
| soviet-civil-administration | pass | 24 Aug 1945, 8 Feb 1946, 9 Sep 1948 confirmed |

## Fixes the reviewer applied (re-validated: 0 errors, 0 warnings)

- **lelang-commandery /ledger/17**: the 313 event was `gain` with counterpart goguryeo, so Lelang gained land from Goguryeo. The pages say the reverse: Lelang page 'In 313, the territory of Lelang was annexed by Goguryeo under King Micheon'; Four Commanderies 'Goguryeo attacked and annexed the commandery in 313'. The type is now `loss`. The region was the four-province union including Hwanghae, which Lelang had already lost to Daifang in 204 (/ledger/9, KF4); it is now the 204..313 keyframe's land (Pyongyang, South Pyongan, Wonsan 80 km). /ledger/18 (dissolve) got the same region. Reviewer notes were added to the event.
- **jeongan /ledger/0**: the counterpart changed from dongdan to liao-dynasty. Dongdan was annexed by Liao in 936 (Dongdan page; dongdan /ledger/2), so the land in 938 was Liao's. Dongdan stays the predecessor.
- **jeongan /ledger/3, /ledger/4**: confidence lowered from 3 to 2. The page dates 986 but gives Jeongan only as 'a state in Manchuria'; the Yalu radius is a placeholder.
- **dongnyeong-prefecture /ledger/0 and identity.start**: month 10 added. The Dongnyeong page says the rising and surrender happened in October 1269; the note had said the sentence gives no year.

## Open findings for the author or a gap-filler (not applied; none blocking)

- **lelang KF4**: Gyeonggi, the Zhenfan placeholder held since -82, disappears at 204 with no event. Add it to the 204 loss to daifang-commandery at confidence 1 (Gongsun Kang page: Daifang made 'by separating the southern half'), or add a 204 loss to nobody.
- **xuantu KF0 and /ledger/0**: the page reads 'established in 107 BCE in the northern Korean Peninsula and part of the Liaodong Peninsula'. Add the Liaodong part at confidence 1, or say in the KF0 note why it is left out.
- **buyeo KF1**: add a 285 `gain` from nobody of the eastern branch (region as /ledger/6, confidence 2). Source: the Eastern Buyeo page, 'Dongbuyeo was briefly revived by a small state established around 285 by refugees of Buyeo'. Also, /ledger/1 (the -86 split at Yanji) is outside Buyeo's own -200..284 keyframe: say so in its note.
- **gongsun-liaodong /ledger/2-3**: Gongsun Kang page, 'Kang invaded Goguryeo again in 209 and seized some of its territory'. A confidence-1 gain (placeholder) with a goguryeo mirror would carry this. As written, nothing moves.
- **baekje-restoration-movement KF0**: 'Baekje (core)' at confidence 1 for 660-661, under the rule that the rebel patch wins, paints all of Baekje as rebel for two years. A gap-filler should find what the loyalists actually held before 662. /ledger/2: silla has no 663 gain. Either silla adds one, or the counterpart becomes ungjin-commandery, whose outline covers Juryu.
- **protectorate notes**: the notes field still says 'Not covered: the Ungjin Commandery ... no page opened here dates it', but ungjin-commandery is in this batch.
- **dongdan identity.family** 'korea', and the 1945-48 governments' 'korea': this is a question for the colour agent. The author's stated rule is that colonies take the metropole's tint.
- **eastern-buyeo**: the KF0 note checks only goguryeo_23. goguryeo_-36 (-36..22, kept 'ok' by the goguryeo dossier) has a bbox containing the Yanji placeholder, so the two may overlap for -36..22. This could not be tested without geometry; if it holds, the fix belongs to goguryeo.

## Confidence-1 gaps (thin)

Zhenfan's site (Korean Wikipedia https://ko.wikipedia.org/wiki/진번군); Xuantu's 75 BCE coast and Tonghua seat and the undated Fushun retreat (현도군); the Jin takeovers of Lelang and Daifang (265 bridges); Buyeo's founding (-200), restoration (286) and the end of the Yan campaign (348); Jeongan's location ('the former land of Goguryeo' is on the page and not quoted); the restoration's 660 rising and 660-661 extent; the Sambyeolcho's move from Jindo to Jeju (1271).

## Cross-dossier matrix (summary; the full list is in the JSON report)

- Matched inside the batch: lelang and zhenfan (-82), xuantu and lintun (-82), lelang and xuantu (-75), lelang and wang-tiao (25, 30), lelang and daifang (204), buyeo and eastern-buyeo (-86); with neighbours: buyeo and goguryeo (410), lelang and goguryeo (313, after the reviewer fix), protectorate and goguryeo (668), dongdan and balhae (926), ungjin and baekje (660).
- Naming mismatches: the neighbour names the metropole, not this batch's colony. gojoseon -108 names han-dynasty (jk-02-a). dongye -82 names han-dynasty (should be lintun-commandery). goguryeo 37/44 names han-dynasty and 22 names buyeo (jk-02-b). silla 671/676 names tang-dynasty (jk-02-c). goryeo 1258/1270/1290/1356 names mongol-empire or yuan-dynasty (jk-02-c; 1270 against the page's October 1269). empire-of-japan 1945 names USA/USSR (jk-01). republic-of-korea and democratic-people-s-republic-of-korea 1948 name USA/USSR (jk-02-d).
- Missing mirrors: goguryeo 314 (daifang), 319 (xuantu). dongye and dong-okjeo 245 vassal_start under Lelang. silla 663 (restoration). goryeo 1270, 1271 and 1273 (sambyeolcho). tamna 1271 (sambyeolcho).
- Disagreements: goguryeo 491 against buyeo 494 (the Buyeo page says 494; goguryeo's 491 is confidence 1). silla 660 occupation_start of all of 'Baekje (core)' double-covers the Ungjin colony 660-671. dong-okjeo -36 names lelang-commandery, which holds no Hamgyong land then.
- Exceptions: groups that have not run (han-dynasty, cao-wei, tang-dynasty, liao-dynasty), and murong-xianbei, which needs a dossier.

## Gazetteer

Seocheon (place: ungjin-commandery, baekje-restoration-movement), Jindo (place: sambyeolcho, currently a lon/lat radius), Kumya (place: ssangseong-prefecture).
