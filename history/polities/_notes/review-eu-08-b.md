# Review eu-08-b: holy-roman-empire (Cliopatria 'Holy Roman Empire' 962..1259 and the stray 1619..1621 shape)

Reviewer, 2026-10-25. Verdict: THIN, with one fix applied by the reviewer and seven unapplied, non-blocking fixes for the author (or a gap-filler). No fabricated or mis-sourced event was found.

## What I tried and could not break
- Validator (--resolve): 0 errors; warnings only for counterpart 'lutici' (no dossier; listed by the author) and the place 'Burg Stargard' (gazetteer).
- Schema and shape: file name = slug; cliopatria_names = ['Holy Roman Empire']; all 26 shapes reviewed; the 6 new keyframes (983, 1157, 1164, 1185, 1198, 1227) carry from, to and a correction; family 'germany' is a colours.json family; capital Frankfurt (8.68 E, 50.11 N) is inside every shape's bbox.
- Keyframe walk: every area change of 10,000 km2 or more has a ledger event (983, 1002-1003, 1010, 1029/1033/1034, 1094, 1139, 1147, 1157, 1164, 1185, 1188, 1198/1203, 1227); the adjust corrections agree with the events.
- Area: infobox 1,100,000 km2 for 1150 against the 1147-1151 shape 873,727 km2 (ratio 1.26), acknowledged in /keyframe_review/15.
- Spot checks (WebFetch, all pages loaded): /ledger/4 (Great Slav Rising: Havelberg 29 June 983, Brandenburg three days later, Northern and Billung Marches lost), /ledger/7 (Henry II: conquest west of the Oder 1002 after Eckard's murder), /ledger/19 and /ledger/21 (Conrad II: Mieszko's 1028 invasion; surrender in the fall of 1031), /ledger/26 (Conrad II: 'On 1 August 1034, Conrad officially incorporated Burgundy'), /ledger/28 and /ledger/40 (Holy Roman Empire: Salian line ends 1125; Bohemia 'raised to a kingdom in 1198'), /ledger/35 (margraviate 1157), /ledger/36-38 and /ledger/46 (Duchy of Pomerania: Verchen 1164, Danish vassal 1184-1185, Bornhoved 1227), /ledger/42 (Valdemar II: 1203 in the body, 1207 in the lead), /ledger/48 (Duchy of Pomerania: 'hand over most of his duchy to Brandenburg immediately, that was the Burg Stargard Land and adjacent areas', Kremmen 1236). All confirmed; /ledger/16 is on the page but mis-dated (below).

## Fix applied by the reviewer
1. /ledger/42 (1203 loss of Holstein and Lubeck to Denmark): confidence 3 -> 2, note amended. The Valdemar II page says 'In 1203 Valdemar invaded and conquered Lybeck and Holstein' in the body and 'In 1207, Valdemar invaded and conquered Lybeck and Holstein' in the lead. Re-validated: 0 errors.

## Fixes for the author (not applied; none blocking)
1. /ledger/16 (vassal_start kingdom-of-poland 1018), with /ledger/11, /ledger/17 and /keyframe_review/6-7. The Henry II page dates the fief to the Peace of Merseburg, 1013: 'requiring in part that Boleslaw I recognize Henry II as his overlord in exchange for receiving the March of Lusatia and the March of Meissen as fiefs'; Bautzen (30 January 1018) only let him 'keep the contested marches ... on purely nominal terms of vassalage'. Fix: vassal_start at 1013 with that quote; end the 1004 contest in 1013 and open a second contest 1015-1018 (or say in the note why one contest spans the 1013-1015 peace); amend the 1018 keyframe text.
2. /ledger/13 (1010 gain from kingdom-of-poland, conf 1) and /keyframe_review/5-6. The Henry II page (already a source) puts Bohemia's recovery in the 1004 campaign: 'Forcing Boleslaw I to flee, Jaromir occupied Prague with a German army and proclaimed himself Duke'; it gives no return of Meissen and Lusatia before the Merseburg treaty of 1031/1033 (Conrad II page). Fix: a 1004 gain of Bohemia from kingdom-of-poland (conf 2, Henry II page) with a new keyframe 1004 (the 1003 shape plus Bohemia); restrict the 1010 gain to the cells Cliopatria adds besides (the Austrian cells, conf 1); mark keyframe 1010 adjust so that Meissen and Lusatia are Poland's 1010-1012 and vassal tint from 1013.
3. /ledger/3 and /ledger/32 (983 loss to, 1147 gain from 'obotrites'). The obotrites dossier (eu-07) runs 793-946 and ends with a dissolve (successor kingdom-of-germany), so neither event can have a mirror; the notes say 'The Obotrites have a dossier (eu-07)' without noticing. Fix: retarget to the revived Obotrite confederation of 983-1160s (listed by the reviewer under counterparts_needing_dossiers) or have eu-07 decide whether obotrites gets a second dossier.
4. Missing mirror of kingdom-of-arles /ledger/2: 'Rudolph in 1006 ceded the city of Basel to his nephew Henry II' (Rudolph III of Burgundy page, confirmed by the eu-08-a reviewer). The author flagged it as not on the Henry II page. Fix: add a 1006 gain, counterpart kingdom-of-arles, region {"place": "Basel", "km": 15}, source https://en.wikipedia.org/wiki/Rudolph_III_of_Burgundy (add to sources).
5. /ledger/26 (1034 gain of the Kingdom of Burgundy from kingdom-of-arles, conf 3, confirmed). The kingdom-of-arles dossier has no 1034 loss, merge or vassal event and keeps the whole kingdom (its 1033 extent less Basel) as its own shape 1034-1384, while this dossier draws 480 of the same cells as direct territory 1034-1259: a double claim. The eu-08-a reviewer asked that eu-08-b record Arles 'as a component'; a gain does not do that. Orchestrator decision: either a vassal_start kingdom-of-arles in 1034 here (and keyframes 1034-1250 drawing Arles as tint), or a 1034 merge in the Arles dossier.
6. /keyframe_review/31 (1619 shape, wrong): the correction points to the Minor States shape of 1619 for 'the Empire in 1619-1621', a year outside this dossier's life (ends 1259). Fix: say the shape is dropped from this dossier; the Empire in 1619-1621 belongs to holy-roman-empire-minor-states (eu-09) and the Bohemian Revolt fragment to the Bohemia owners (eu-15/eu-16).
7. /identity/successors/0 and /ledger/52: the notes call the two Q12548 rows 'one empire' yet the dossier dissolves in 1259, which is not what the brief's rule for shared Wikidata ids says (one dossier under the earlier slug, both Names in cliopatria_names); data/README.md classes 'Holy Roman Empire Minor States' as an aggregate carried as a leaf. Orchestrator decision; until then the dissolve note should not claim 'same state'.
8. Minor: Bohemia and Moravia are drawn as direct land 1010-1197 although the Holy Roman Empire page lists the Duchy of Bohemia in the Empire 'from 1002' as a duchy (a fief); only the 1198 royal title changes. Consider a vassal tint from 1004 (keyframes 1010-1188 adjust) or say in the 1010 note why the shape keeps it direct.

## Thin (conf-1 events and budget gaps: pages a gap-filler should try)
- /ledger/1, /ledger/6 Spoleto lands to Benevento 970 and back 990: https://en.wikipedia.org/wiki/Duchy_of_Spoleto
- /ledger/2, /ledger/27, /ledger/31, /ledger/34 Corsica 970, 1094, 1139, 1147: https://en.wikipedia.org/wiki/Corsica
- /ledger/9 Austrian cells to Poland 1003 (and back 1010/1028): https://en.wikipedia.org/wiki/Margraviate_of_Austria
- /ledger/14-15 Pisa and Genoa 1010: https://en.wikipedia.org/wiki/Republic_of_Pisa
- /ledger/25 end of the Burgundian contest with Odo II 1034: https://en.wikipedia.org/wiki/Odo_II,_Count_of_Blois
- /ledger/29 Lubusz 1126: https://en.wikipedia.org/wiki/Lubusz_Land
- /ledger/30 Hohenstaufen 1138: https://en.wikipedia.org/wiki/Conrad_III_of_Germany
- /ledger/33 Abruzzo to Sicily 1147: https://en.wikipedia.org/wiki/Roger_II_of_Sicily
- /ledger/39 46 cells of south-eastern France 1188: https://en.wikipedia.org/wiki/Frederick_Barbarossa
- Mecklenburg 1160-1236 (Niklot, Obotrite submission): https://en.wikipedia.org/wiki/Niklot
- Lombard League and the Peace of Constance 1183 (war zones empty): https://en.wikipedia.org/wiki/Lombard_League
- Austria and Styria under Frederick II 1236: https://en.wikipedia.org/wiki/Frederick_II,_Duke_of_Austria
- identity.rulers omitted: https://en.wikipedia.org/wiki/List_of_Holy_Roman_emperors
- /ledger/50-52 (1259 row-boundary closures, conf 1) are by design.

## Cross-dossier matrix (summary; the report has every row)
- Matched: found 962 <- kingdom-of-germany dissolve 962-02 (successor holy-roman-empire).
- Mismatch: 983 loss / 1147 gain 'obotrites' (dossier ends 946); 1034 gain from kingdom-of-arles (Arles keeps the land 1034-1384); kingdom-of-arles 1361 loss and 1384 dissolve name holy-roman-empire, which ends 1259 (eu-08-a should retarget to holy-roman-empire-minor-states, or the orchestrator merges the rows).
- Missing: kingdom-of-arles 1006 Basel (no gain here); 1188 loss to kingdom-of-france (no 1188 gain in that dossier; this side is conf 1, Cliopatria only).
- Exceptions (counterpart's group not run, or listed): lutici; kingdom-of-italy; duchy-of-benevento, republic-of-pisa, republic-of-genoa, kingdom-of-sicily (eu-13); kingdom-of-poland, kingdom-of-bohemia, pomerania (eu-15); kingdom-of-denmark (eu-14); county-of-blois (eu-10, not written); holy-roman-empire-minor-states (eu-09, not written). Caveat: Cliopatria's Pomerania row ends 1187, so the 1227, 1236 and 1259 events need eu-15 to carry the duchy past 1187.

## Gazetteer
- place 'Burg Stargard' (the Stargard Land by Neubrandenburg, about 53.5 N, 13.3 E), /ledger/48.
