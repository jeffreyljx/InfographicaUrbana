# Review of batch jk-02-a (Korea, part a)

Reviewed 2026-10-19 by the adversarial reviewer. Dossiers: gojoseon, korean-jin, mahan, byeonhan, jinhan, dongye, gaya. Machine copy: history/notes/phase-b/reviews/jk-02-a.json.

## Verdicts

| slug | verdict | why |
| --- | --- | --- |
| gojoseon | fix (by reviewer) | Yan war (-300) was outside the life: moved to notes. All five checked events confirmed. |
| korean-jin | pass | All five events confidence 1 and honest; one advisory on the Ye coast. |
| mahan | fix (by reviewer) | identity.wikipedia 'Mahan' is a disambiguation page: now 'Mahan confederacy'. |
| byeonhan | fix (by reviewer) | Eight Port Kingdoms War (c. 209-212) moved in from gaya, inside this life. |
| jinhan | fix (by reviewer) | Predecessor land text misquoted the page: now 'specifically claimed successorship over Jin state'. |
| dongye | fix (by reviewer) | Two notes misquoted 'appears in history as a vassal state of Goguryeo': corrected. |
| gaya | fix (by reviewer) | Eight Port Kingdoms War removed (outside 301-562), moved to byeonhan. |

All seven validate with 0 errors after the edits. The warnings left are the intended split of the Byeonhan row (byeonhan has no verdict for byeonhan_534/561, gaya none for byeonhan_-91; together they review all three).

## What was tried and did not break

- Spot checks (4-5 per dossier, all confidence-3 events and the land-moving ones): every quote and year checked on the page was there. Gojoseon 194, 109 and 108 BCE (Gojoseon, Wiman Joseon, Four Commanderies pages); Jin's 'somewhat contradictory' end and both succession statements; Mahan's infobox, Mokji/Cheonan, the 246 record, Geunchogo; Byeonhan's infobox and 13 statelets; Jinhan's 1st c. BCE and 108 BCE statements, Silla's 377; Eastern Ye's 82 BC independence, 'early 5th-century' annexation, the three provinces, the AD 40/60 footnotes; Gaya's 532 (Gaya and Geumgwan pages) and 562 (Daegaya, Kim Isabu).
- Area: no infobox in the batch gives an area (Gojoseon, Jin, Mahan, Byeonhan, Jinhan, Gaya, Eastern Ye all checked); each dossier says so. Cliopatria deltas the authors quote check against shapes.csv (silla_534 +3,113, byeonhan_534 -3,061, goguryeo_392 +31,200, Jin = Samhan + Dongye within 200 km2).
- Years, certainty and capitals lie inside each life; capitals sit inside their shapes' bboxes (Pyongyang, Cheonan, Gangneung, Gimhae, Goryeong).

## Advisories (not blocking, not applied)

- korean-jin /keyframe_review/0 and gojoseon: the correction cuts the Ye coast (25,776 km2) from Jin from -197, but the page dates an owner only from 129 BCE ('It belonged to the Wiman Joseon in 129 BC'); gojoseon's shapes stop at 128.05E and carry no subject-Ye event, so the coast is nobody's -197..-109. Keep the cut, say so in the K0 note; a gap-filler may give gojoseon the subject Ye to 128 BCE (Namnyeo's defection, Canghai Commandery).
- mahan /wars/1 runs to 375, past the end in 346 (Geunchogo's reign): end it at 346 or say why.
- dongye /ledger/1 (401) and the new keyframe dongye_392 overlap Cliopatria's goguryeo_392, which takes the Ye land in 392. 401 fits the page ('early 5th-century') better than 391; the goguryeo dossier must keep the Ye out of its 392-401 shapes and gain it in 401 with counterpart dongye, or both move to 391. Goguryeo should also carry the Taejo vassalage of the Ye (undated, r. 53-146).

## Thin (for gap-fillers; all within the page budget, so thin by design)

- gojoseon: subject Ye 129-128 BCE (Canghai_Commandery); start -197 (Gija_Joseon).
- korean-jin: start and end (Proto-Three Kingdoms period).
- mahan: Baekje's growth inside Mahan before 346 (18 BCE, Mokji 1st c. CE, 20 statelets in the late 3rd c., Goi 234-286); end 346 (Geunchogo_of_Baekje).
- byeonhan / gaya: split year 300/301.
- jinhan: Saro's growth (57 BCE; Pasa's conquests of 102); end 377 (Naemul_of_Silla).
- dongye: +3,240 km2 at -36 unexplained; Taejo vassalage undated; end 401.
- gaya: Takgitan (529) and Ara Gaya not placed; Goguryeo pressure 391-412 (Gwanggaeto_Stele).

## Cross-dossier

Matched: korean-jin -92 splits to mahan, jinhan, byeonhan (their -91 found events); byeonhan 300 to gaya 301. Every other counterpart (han-dynasty ea-02; goguryeo, baekje, silla jk-02) has not run yet: exceptions, with the routing notes in the JSON (Han must gain the Gojoseon land in 108 BCE although Cliopatria's Han lacks it to -91; Silla must gain Gimhae in 532 and Daegaya in 562, Cliopatria has 534 and 567).

Counterparts needing dossiers (jk-02-x): lelang-commandery (-108..313), xuantu-commandery (-107..319), lintun-commandery (-107..-82), daifang-commandery (204..315).
