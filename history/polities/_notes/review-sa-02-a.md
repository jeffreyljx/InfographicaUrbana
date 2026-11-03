# Review of batch sa-02-a (2026-10-19)

Reviewer: adversarial review, Phase B. Machine copy: history/notes/phase-b/reviews/sa-02-a.json. Validator: all six dossiers 0 errors (one expected warning, `ruhuna`). Neighbour dossiers read: macedonian-empire (the only Context polity written), plus nanda-empire and kingdom-of-tambapanni as predecessors; satavahana-dynasty, seleucid-empire and greco-bactrian-kingdom are not written yet (groups not run).

| slug | verdict | in one line |
| --- | --- | --- |
| maurya-empire | fail | the Northwest keyframes give Gedrosia to 316 instead of 302 and leave out Paropamisadae |
| kalinga | pass | all four checks confirmed; Dantapura point is a placeholder |
| anuradhapura | fix (reviewer applied) | Sena and Guththika moved from -247 to -237; 993 confidence 2; predecessor Tambapanni added; 1017 region aligned |
| early-cholas | thin (by design) | founding and end at Cliopatria's years |
| early-cheras | fix (reviewer applied) | founding confidence 2 lowered to 1 |
| early-pandyas | thin (by design) | founding and end at Cliopatria's years |

## maurya-empire: fail (back to the author)

Spot checks confirmed on the pages: -316 Northwest (timeline '317-316 BCE'), -302 cession ('ca. 302 BCE', satrapy list), -261 Kalinga (Kalinga War 'c. 261 BCE'), -224 Kalinga breaks away (Kalinga region page), -185 end (infobox). Area: infobox 3.4 M km2 (261 BCE) and 5.0 M km2 (250 BCE) against Cliopatria 3.82 M and 3.95 M, acknowledged.

What breaks it is the drawing of the Northwest. I counted the Cliopatria cells of each enlargement against the admin-1 gazetteer:

- -315 minus -318 (1,561 land cells, the -316 gain): Baluchistan 852, Sindh 384, Pakistani Punjab 297, Khyber Pakhtunkhwa 0. So most of it is eastern Gedrosia, which the Maurya Empire page ('certainly Gandhara, Parapamisadae, and the eastern parts of Gedrosia') and the Seleucid-Mauryan war page (Aria, Arachosia, Gedrosia, Paropamisadae ceded) put in the cession of c. 302. K2 is marked ok and says nothing about it.
- -301 minus -315 (1,799 cells, the 302 cession): Pakistani Punjab 448, Khyber Pakhtunkhwa 265, Baluchistan 211, Jammu and Kashmir 124, Northern Areas 123, FATA 96, Indian Punjab 97, Himachal 87. The whole -301 shape holds about 290 cells of Afghanistan (Kabul 2, Kandahar 21). The event text says 'Afghanistan south of the Hindu Kush and the Baluchistan coast'; the geometry holds neither, and Paropamisadae, which the page says was 'certainly' ceded, is missing from every Ashokan keyframe.

Fixes for the author (none applied):
1. /keyframe_review/2: adjust; correction = Cliopatria -315 minus admin1 Baluchistan (Pakistan), text 'the Indus valley (Sindh, southern Punjab)'.
2. /ledger/4: the same subtraction and text.
3. /ledger/7: region = (Cliopatria -301 minus -315) plus Baluchistan plus Paropamisadae as Afghan admin-1 (Kabul, Kapisa, Parwan, Panjshir, Wardak, Logar, Nangarhar, Laghman, Kunar); Arachosia (Kandahar, Zabul, Uruzgan, Ghazni) only with a note, since the page says 'possibly'; text rewritten to match.
4. /keyframe_review/3: adjust with the same additions; /keyframe_review/4-6: add them to the existing corrections (to -226).
5. /ledger/13: the -225 loss must include the added Afghan lands.
6. /identity/rulers/1..8: add the Maurya Empire page as source (the infobox gives the reigns).
7. Agree the land of the 317/316 conquest with macedonian-empire: its /ledger/52 (-317) loses Gandhara and the Punjab, whereas this dossier's gain holds no Khyber Pakhtunkhwa until 302.

Thin (gap-filler): -291 southern gain (1.2 M km2, confidence 1; Edicts of Ashoka page), the -225 losses (2.1 M km2 to nobody and the Deccan to the Satavahanas, confidence 1; Dasharatha Maurya, Satavahana dynasty pages), the eastern extent.

## kalinga: pass

Tried: the 322 BCE break from Magadha (confirmed, 'Kalingas broke away from the empire of Magadha in 322 BCE'), the 261 annexation (confirmed), the 224 break from the Mauryas (confirmed), the -171 end to the Mahameghavahana (infobox '170 BCE: Mahameghavahana (founder)', confirmed). Mirror events with maurya-empire match in year and region; the Odisha union follows the page ('all of Odisha and some part of northern Andhra Pradesh'). Not broken. Leads: Dantapura's point is the shape centroid (flagged); the smaller re-emerged shape after 224 is unexplained (flagged); whether the Mahameghavahana are a rename of Kalinga is a group decision. Cross-group: nanda-empire has no -322 loss of Kalinga and lists only maurya-empire as successor.

## anuradhapura: fix (applied by the reviewer, re-validated)

- /ledger/1: the page puts Sena and Guththika's overthrow in the reign of 'Suratissa (247-237 BC)' and gives them 22 years, so 237 (to 215, then Asela); the dossier had -247 at confidence 3. Now -237, confidence 2; the phrase in `notes` updated.
- /ledger/13: confidence 3 to 2: the page says 'the north'; the districts are the author's reading.
- /ledger/14: the 1017 dissolve region was the whole island; set to the 993..1017 keyframe (island minus the north) to match its own text.
- /identity/predecessors: kingdom-of-tambapanni added (Tambapanni page: 'Kingdom moved to Anuradhapura: 437 BC', 'Succeeded by: Anuradhapura Kingdom'; that dossier dissolves to anuradhapura at -437).
- Not applied, non-blocking: /identity/capitals/2 Anuradhapura (492..1017) lies inside the land lost in 993; end it at 992 with a seat in Ruhuna from a page that names one, or keep it with a note.

Confirmed: Elara 205, Dutthagamani 161, the five Dravidians 103 and Valagamba 89, Vasabha 66 AD, the 433 invasion and Dhatusena 459, Manavanna 684, Rajaraja 993, Rajendra 1017. Thin: the 492 return from Sigiriya (confidence 1); the extent before 161 BCE.

## early-cholas, early-cheras, early-pandyas

Within the 1-2 page budget the pages date no frontier; Cliopatria's shapes do not change. Confirmed: Chenguttuvan 'c. 180 CE' with the Malabar Coast and Kongu (Chera page); Urayur 'their oldest capital'; Sangam age 'c. 300 CE' and the Kalabhra displacement undated; the Pandya extent quote. The Kongu transfer pairs correctly (early-cholas loss and early-cheras gain at 180). One suggestion, not a fault: the Chera page also says the early Chera capital was Karur in the Kongu country and that the pre-Pallava Chera country included Kongu, which would put Kongu with the Cheras from -291 rather than from 180.

Applied: early-cheras /ledger/0 confidence 2 to 1 (the infobox gives 'c. 3rd century BCE'; -291 is Cliopatria's year, as in the Chola and Pandya dossiers).

## Cross-checks and routing

Matched: Maurya-Nanda (-322), Maurya-Kalinga (-261, -224), Cholas-Cheras (180), Tambapanni-Anuradhapura (-437). Mismatch: Maurya -316 gain against macedonian-empire -317 loss (land); nanda-empire's successor list lacks kalinga. Exceptions (groups not run or dossiers not written): seleucid-empire, satavahana-dynasty, shunga-empire, mahameghavahana-dynasty, kalabhra-dynasty, chola-empire (needs a 993 gain of the north of Sri Lanka), ruhuna.
