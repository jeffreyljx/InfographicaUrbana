# Review of eu-06-b (vandals, visigoths, saxons, alans, angles)

Reviewer, 2026-10-19. Machine copy: history/notes/phase-b/reviews/eu-06-b.json.

All five validate with --resolve (0 errors, 0 warnings), before and after the reviewer's edits. No infobox on any of the five pages gives an area; every dossier says so. Every confidence-3 event I opened was on its page with its year (25 spot checks, none fabricated or mis-dated).

## Verdicts

| slug | verdict | why |
| --- | --- | --- |
| vandals | fix | two area figures corrected by the reviewer; 409-411 counterparts and the 410 overlap with alans left for the author |
| visigoths | fix | one area figure corrected; 395-401 type disagrees with eastern-roman-empire; Toulouse capital; 417-418 Baetica/Lusitania holder |
| saxons | thin | the 455 jump (6,335 to 82,798 km2) and the 283 start are confidence 1 with every page of the 9-page budget spent; everything else checks |
| alans | fix | 418 loss raised 1 -> 2 by the reviewer; war/contest start 417 and the 409 counterpart left for the author |
| angles | thin | all three events confidence 1 by design (2-page budget); capital lies outside the shape |

## Reviewer edits (applied, re-validated, read back)

- vandals /keyframe_review/4/note: 99,896 -> 91,608 km2 (shapes.csv vandals_407).
- vandals /keyframe_review/8/note: 63,984 -> 68,460 km2 (shapes.csv vandals_417).
- visigoths /keyframe_review/10/note: 13,910 -> 12,698 km2 (shapes.csv visigoths_414).
- alans /ledger/1: confidence 1 -> 2 (Alans page: 'soundly defeated by the Visigoths in 418 CE'; the provinces are named on the page).

## For the authors (not applied)

### vandals
1. /ledger/3, /ledger/4, /ledger/5: the neighbours give Gaul 408-411 to constantine-iii-usurper and Hispania 409-411 to maximus-usurper (western-roman-empire /ledger/9-10; maximus-usurper /ledger/0). The Hasdingi page names the giver of 411: 'the rebel Roman military leader of Hispania, Gerontius'. Use maximus-usurper for /ledger/4 and /ledger/5 and constantine-iii-usurper for /ledger/3.
2. /keyframe_review/5 and /ledger/4: the 410 keyframe (whole peninsula) overlaps alans_409 (409-413, Lusitania and Carthaginensis) from this same batch, and nothing gives up the rest of the peninsula when the shape drops from 420,482 to about 96,000 km2 in 411. Subtract the Alans 414 shape from the 410 correction and add a 411 loss of the remainder (Tarraconensis, western Gallaecia).
3. /ledger/6: the 417 loss of Baetica goes to western-roman-empire, which has no matching gain, while visigoths draws Baetica as its own 417-418 ground. Agree one holder with visigoths.

### visigoths
1. /ledger/1-5: the note of /ledger/2 calls 396 'A plunder zone, not annexed land', and eastern-roman-empire records 395-397 Greece and 397-401 Epirus as occupation by visigoths, but this dossier types them found/gain/loss. Same years; agree the type with eu-05 (occupation_start/_end with counterpart eastern-roman-empire would mirror it exactly).
2. /identity/capitals/0: Toulouse (418) lies outside the 417-418 ground (Baetica and Lusitania) and is visigothic-kingdom's seat from 418. Drop it or say so.
3. /keyframe_review/12: Baetica and Lusitania are drawn as Gothic ground with only contest events; vandals hands Baetica to western-roman-empire in 417 and alans keeps Lusitania to 418. Either add 417 gains and 418 losses or say in the note that the ground is the contest zone, and align with vandals /ledger/6.

### alans
1. /wars/0: runs 418-418 though its own note dates the campaign 417-418; visigoths has contest_start alans 417 and contest_end 418. Start the war in 417 and add the contest pair.
2. /ledger/0 and the predecessor: maximus-usurper rather than western-roman-empire for 409 (as vandals 1).

### angles
1. /identity/capitals/0: Schleswig/Haithaby at 54.492 N is south of the Angles shape (bbox 54.545-54.885 N) and rests only on Aethelweard (about 1000). Drop it or move it inside Angeln with a note.

### saxons
Nothing to change. Gaps for a gap-filler: the 455 expansion (try Bructeri, Chauci), the 283 start, Nordalbingia 785-792 and 795-797, and the Frankish campaigns into Nordalbingia 795-799 (only the Obotrite contest is recorded). The 449 split (and angles' 441 split) names land in Britain, outside the state's shape: harmless, but it is a migration, not a loss of land.

## Cross-dossier routing (details in the JSON cross_checks)

- western-roman-empire (eu-04) lacks mirrors for most Vandal and Gothic moves: vandals 406 Pannonia, 419 and 429 Baetica, 429-432 Africa (WRE has the African loss only in 435 and names 'vandals', which ends in 434: it should be vandal-kingdom; its 429 mauro-roman-kingdom loss overlaps the vandals' Mauretania); visigoths 403-412 (Pannonia, Noricum, southern Italy), 415 Barcelona. WRE ends the 402 Gothic contest in 407 (c1) against the visigoths' 402; WRE regains Septimania in 417 (c1) against the visigoths' 415 withdrawal (Athaulf page).
- eastern-roman-empire (eu-05): occupation vs gain/loss for 395-401 (see visigoths 1).
- vandal-kingdom and visigothic-kingdom list only western-roman-empire as predecessor; each should also list vandals / visigoths.
- Counterparts not yet written (exceptions): kingdom-of-the-franks (eu-07-b), obotrites (eu-07-d), kingdom-of-the-suebi (eu-06-c), anglo-saxon-england (eu-11-a), scandinavian-minor-kingdoms (eu-14-a).

## Spot checks (all confirmed)

vandals /ledger/2, 4, 5, 13, 14 and rulers/0; visigoths /ledger/2, 4, 10, 15, 16, 19, 25; saxons /ledger/1, 6, 9, 13, 14-17, 18-19; alans /ledger/0-3; angles /ledger/0-2 and keyframe 0. One note quotation is not verbatim on the page (alans /ledger/2 'The Alans joined in 418'); the substance is there.
