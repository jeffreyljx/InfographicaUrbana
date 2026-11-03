# Review of batch eu-06-x (Migration kingdoms, additions), 2026-10-24

Reviewer: adversarial review, Phase B. Nine new dossiers (no Cliopatria rows). Validator with `--resolve`: 0 errors, 0 warnings for all nine. 38 events or wars spot-checked on the pages cited: every one says what its note claims, with the year (no fabricated or mis-dated event). There are no infobox areas for these peoples, so every area check is null. Overlaps were measured by resolving each batch keyframe and the neighbours' keyframe corrections with `history/tools/gazetteer.py` (one cell is about 252.9 km2).

Verdicts: heruli **fail**, sciri **fix** (fixed by reviewer), danubian-suebi **fail**, gothic-foederati **pass**, thracian-goths **fail**, alans-of-orleans **fail**, kutrigurs **thin**, utigurs **fix** (fixed by reviewer), antes **pass**.

Every fail is a wrong or unflagged shape, not a wrong date.

## heruli (fail)

- `/keyframe_review/1/correction` (and ledger 4-8, successor land): the 70 km disc round Belgrade (57 cells) is mostly other dossiers' land. In 512-535 only 7 cells are in eastern-roman-empire_510; 16 are in kingdom-of-the-gepids_510 and 10 in ostrogothic-kingdom_510 (the Sirmium district, where Bassianae lies). In 539-567, 45 cells are in the Gepid keyframes. The Heruli page: "moved first to the area of Bassianae" (near Donji Petrovci, north of Belgrade), later "given land near Singidunum" after 527. Fix: draw Bassianae alone for 512, with the counterpart that holds Srem then (ostrogothic-kingdom) or a reason why it is Roman; draw the post-527 grant on the Roman side of Singidunum (the disc intersected with eastern-roman-empire_523); say what happens after the Gepids take the Singidunum area in 539.
- `/ledger/4/region`: the 512 gain already contains the post-527 Singidunum land, so the 527 gain (`/ledger/6`) re-gains the same disc. Split the regions.
- `/keyframe_review/0/correction`: the 40 km Bratislava disc crosses the Danube: 7 of its 49 cells are in ostrogoths_455 and 3 in danubian-suebi_453. Procopius puts the kingdom "north of the Danube". Use Slovak admin1 units (Bratislavsky, Trnavsky) or cut the south bank.
- Thin: 494 loss (conf 1, who held the land), 527 grant year, 567 end (last date, not a stated end).
- Confirmed on the Heruli page: 491 tribute, 494 Rodulf (estimates 493-511), 512 Marcellinus Comes and Bassianae, Singidunum after 527, Sinduald 566/567.

## sciri (fix, applied by reviewer)

- Applied: a sentence appended to `/keyframe_review/0/note`. 56 of 67 cells lie in kingdom-of-the-gepids_454 (454-472, the Cliopatria 510 shape carried back), and 7 Pest cells west of the Danube lie in ostrogoths_455. The Sciri page places Edeko's kingdom "in the Middle Alfold between the Middle Danube and the Tisza rivers", so the Gepid keyframe (eu-06-e) should give way. Re-validated: OK.
- Confirmed: Sciri page (kingdom; 468/469 defeat), Bolia page (468 infobox; "the Sciri met with crushing defeat near the Bolia river (468 A.D.)"; "the battle marked the end of the Sciri as a separate people"), Hunimund page (469; "gained control of territory of the Sciri and Quadi").

## danubian-suebi (fail)

- `/keyframe_review/0/correction`: 24 of the 25 cells lie in ostrogoths_454/455, the Pannonian shape the ostrogoths dossier keeps for 454-473. The kingdom is drawn on Gothic land for its whole life, and this is not flagged. The Hunimund page points across the Danube: "somewhere near the old settlement area of the Marcomanni and the Quadi"; the Goths "gained control of territory of the Sciri and Quadi"; the Suebi stole "Goth-owned cattle from Dalmatia". The Suebi page says "in or near north-eastern Pannonia". Fix: redraw on the Quadic side (e.g. admin1 Nitriansky, Slovakia: 23 cells, about 5,800 km2, overlapping neither heruli nor sciri), minus any ostrogoths_455 cells. If the author keeps the counties, flag them and ask eu-06-d to cut them for 453-468.
- Confirmed: Suebi page (Hunimund and Alaric, NE Pannonia, 469/470 flight), Bolia 468, Hunimund 469 and Nedao 454.

## gothic-foederati (pass)

Tried: the two confidence-3 events (3 October 382; "Scythia, Moesia and possibly Macedonia"; foederati, "under their own authority and were not dispersed") and the 395 end ("this peace held essentially unbroken until Theodosius died in 395"; Alaric "made a bid for the throne"). All confirmed. Years, certainty, war and federate model are consistent. 218 of 234 cells sit on roman-empire_390, as federates should. Not broken. Counterpart work (routed): roman-empire (eu-04-a) needs the 382/395 vassal pair; gothia (eu-06-a) should hand the land to gothic-foederati, not to roman-empire.

## thracian-goths (fail)

- `/keyframe_review/0/correction` (every region): `{region: Thrace}` (287 cells, about 72,600 km2) includes Constantinople and Edirne. The Eastern capital is drawn as contested in 471-473 and 474-481, and as the Goths' sole land in 473-474 and 481-484. The Strabo page names only Philippi/Philippopolis, Arcadiopolis and Stabulum Diomedis near Philippi. Fix: subtract admin1 Istanbul at least; better, draw the Thracian plain (Plovdiv, Stara Zagora, Haskovo, Edirne, Kirklareli).
- `/ledger/2`: outside the contest windows, the land is drawn twice: 269 of 287 cells are in eastern-roman-empire_469, with no vassal or contest on either side. The 473 peace (an annual 2,000 lb of gold, magister militum) fits the batch's own federate model. Fix: vassal pair or continued contest for 473-474; end in 481, or make 481-484 federate or contested.
- Confirmed: 471 revolt and the two cities, the 473 peace, January 474, 481 death.

## alans-of-orleans (fail)

- `/keyframe_review/0/correction`: 73 of the 84 cells lie in kingdom-of-soissons_480 (476-486) and in salian-franks_486 to _501 (486-509), so for 476-503 the Orleanais is drawn twice, and this is not flagged. western-roman-empire's 476 loss gives northern Gaul to Soissons. The 503 end is a confidence-1 bridge built on an Armorica item ("Around 502-503 Clovis attacked Armorica but was defeated by the Alans"); the Sangiban page has the Alans of Aurelianum "conquered by the Visigoths a few years later". Fix: dissolve by 476, handing over to kingdom-of-soissons, or draw 476-503 as a vassal of Soissons and then salian-franks, with requests to those dossiers.
- `/ledger/3`, `/ledger/4`, `/wars/3`, `/wars/4`, successor: kingdom-of-the-franks should be salian-franks, which holds Clovis's realm to 509 and adds Armorica in 501.
- Thin: 476 vassal_end (bridge), 503 end.
- Confirmed: 442 Orleanais (conf 3), Sangiban as Goar's successor at Aurelianum, the 463 Orleans battle, the 466 battle with Childeric, the 502-503 text.

## kutrigurs (thin)

All three events are confidence 1, by design: the pages do not date a Kutrigur realm. Confirmed: 551 Chinialon "from the western side of the Maeotic Lake", "By 562 the Avars controlled ... the steppes north of the Black Sea", the Kutrigurs page's "towards the end of the 6th century", and Zabergan 558/559. Gap-filler: the Bayan I and Sinnion pages. avar-khaganate (eu-06-f) has no gain from kutrigurs.

## utigurs (fix, applied by reviewer)

- Applied: a sentence appended to `/keyframe_review/0/note`. The author guessed the gokturk dossier might not carry the Pontic steppe, but gokturk-khaganate_561 (verdict ok, "the Kazakh and Pontic steppe to the Don") holds 335 of the 405 cells for 561-576. The 576 year is page-backed (Anagai at Bosporos), so ia-01-c should keep the land out until 576. Re-validated: OK.
- Thin: 558 found (conf 1). Confirmed: Pohl quote 558/59, 576 Anagai, Turk rule, Bosporos c. 579.

## antes (pass)

Tried: 518 first contact, the 560s Avar war and Mezamir (fl. 562), 602 Apsich ("destroy the nation of the Antes"), "never again appear" (612), and 533-545/545. All confirmed. The 562-602 contest is the honest reading against avar-khaganate's sole holding of 349 of 358 cells from 561. Not broken. Thin: 518 found (conf 1). Route to eu-06-f: avar-khaganate needs the contest with the Antes and a 602 gain.

## Cross-dossier matrix (summary; machine copy in the report)

| batch event | counterpart | status |
| --- | --- | --- |
| heruli 491 vassal_start, 494 vassal_end, 494 loss | lombards (eu-06-e) | missing |
| heruli 512 gain / vassal_start, 527 gain, 567 vassal_end | eastern-roman-empire (eu-05-a) | 512 gain mismatch (holds 7 of 57 cells); others missing |
| heruli_512 land 539-567 | kingdom-of-the-gepids (eu-06-e) | mismatch (45 of 57 cells) |
| sciri_454 land | kingdom-of-the-gepids_454 (eu-06-e) | mismatch (56 of 67 cells); gepids should give way |
| sciri 468 loss | ostrogoths (eu-06-d) | missing |
| danubian-suebi 468 loss | ostrogoths (eu-06-d) | mismatch (ostrogoths already hold 24 of 25 cells) |
| danubian-suebi 453 found | marcomanni 453 dissolve (cp danubian-suebi) | exception (explained) |
| gothic-foederati 382 found | gothia 382 dissolve (cp roman-empire) | mismatch (eu-06-a) |
| gothic-foederati 382 vassal_start / 395 vassal_end | roman-empire (eu-04-a) | missing |
| thracian-goths contests 471/473/474/481 | eastern-roman-empire (eu-05-a) | missing |
| alans-of-orleans 442 vassal_start | western-roman-empire (eu-04-b) | missing |
| alans-of-orleans 476 vassal_end | western-roman-empire 476 loss to kingdom-of-soissons | mismatch |
| alans-of-orleans 503 loss | kingdom-of-the-franks (no dossier); salian-franks holds the land from 486 | mismatch |
| kutrigurs 561 loss | avar-khaganate 561 found (cp nobody) (eu-06-f) | missing |
| utigurs 576 loss | gokturk-khaganate (ia-01-c) holds the land from 561 | mismatch |
| antes 562 contest_start, 602 contest_end, 602 loss | avar-khaganate (eu-06-f) holds the land from 561 | mismatch / missing |

## Reviewer edits

`history/polities/sciri.json` and `history/polities/utigurs.json`: one sentence appended to `/keyframe_review/0/note` in each, re-validated (0 errors, 0 warnings) and read back after a minute. No other file in `history/` was changed apart from this notes file and `history/notes/phase-b/reviews/eu-06-x.json`.
