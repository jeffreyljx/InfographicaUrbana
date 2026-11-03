# Review of batch eu-04-a (2026-10-19)

Reviewer: adversarial review, Phase B. One dossier: polities/roman-empire.json. Verdict: **fail** (back to the author for the unapplied findings below). Machine copy: notes/phase-b/reviews/eu-04-a.json.

## What held

- Validator: 0 errors, 2 warnings (Bosporan and Armenian vassal_start without end, both explained as lasting to 395). All 55 Cliopatria shapes have a verdict; roman-empire_395 is a proper new keyframe. Ledger sorted, found/dissolve at -27/395, certainty contiguous, rulers cover every year, capitals inside the shapes, family `rome` exists.
- Area: infobox 2.75 M km2 (25 BC), 5.0 M km2 (117), 3.4 M km2 (390) against Cliopatria 3.55, 5.26, 4.11 M km2 (ratios 1.29, 1.05, 1.21); all quoted correctly in the keyframe notes.
- Spot checks: 23 events on six pages (Crisis of the Third Century, Roman-Parthian Wars, Roman-Persian Wars, Germanic Wars, Theodosius I, Polemon II of Pontus). Every event was on its page with its year; nothing fabricated. The notes are honest about bridged years.
- Matched: roman-republic dissolve / found 16 Jan 27 BC; eastern-roman-empire found 395; galatia dissolve -25; thracian-kingdom dissolve 46; mauretania vassal_start -25 and vassal_end 40; kingdom-of-pontus dissolve 62 (after the fix below).

## Fixed by the reviewer (applied, re-validated)

1. /ledger/37-38 (were 38-39): Pontus's annexation moved from 68 (confidence 1, bridged from Cliopatria) to **62**, confidence 3, source Polemon II of Pontus ('In 62, Nero induced Polemon II to abdicate the Pontic throne, and Pontus, including Colchis, became a Roman province'), added to sources[]; matches kingdom-of-pontus's 62 dissolve. The author should update the notes/gaps lines and the roman-empire_68 keyframe note that still say 68.
2. /ledger/80: the 267 Palmyrene loss lowered to confidence 2. The page dates only 'Syria, Palestine, and Aegyptus' to 267; 'large parts of Asia Minor' (Cilicia, Galatia, Cappadocia in the region) carries no year and its section is headed 271-273.

## For the author (unapplied)

Blocking:

1. **/keyframe_review/33** (270-282): the correction is the 274-282 state, minus(union(270, 283), Dacia), applied to the whole span. For 270-273 it draws Gaul and Britain (about 715,000 km2, Gallic until /ledger/84 in 274) and the Palmyrene East (about 362,000 km2, lost /ledger/80 267, regained /ledger/83 273) as Roman, and drops Dacia a year before /ledger/81. Keyframes 32 and 50 use the start-of-span convention; this one does not. Fix: correction = the 270 shape minus the /ledger/80 region (Dacia handled by the 271 loss), letting /ledger/81-84 move it; or split into roman-empire_270 (270-273) and roman-empire_274 (274-282).
2. **/keyframe_review/51** (387-389): union(387, 371) draws Britain (about 161,000 km2) and Gaul (about 679,000 km2) as Roman in 387 though /ledger/106-107 and /ledger/111 hold them for Maximus until 388. Fix: remove Great Britain and Gaul from the correction and let /ledger/111 restore them, or split 387 / 388-389.
3. **/keyframe_review/31** (260): Cliopatria's one-year drop of 384 cells (about 97,000 km2) of Syria and upper Mesopotamia is kept with no ledger event (only the /ledger/77 contest_end); the cells return in 261 through keyframe 32. Fix: add them back (intersect of minus(247, 260) with the 270 shape) or add a sourced Sasanian occupation of 260.
4. **Bosporus 63-68**: cimmerian-bosporus /ledger/19-20 has the kingdom 'incorporated as a part of the Roman Province of Moesia Inferior from 63 to 68'. Add occupation_start 63 / occupation_end 68 (counterpart cimmerian-bosporus), or argue against it and tell eu-01; keep the Bosporan tint (/ledger/6) consistent.
5. **Kush**: kingdom-of-kush /ledger/15-18 has the war of -23..-22, the Dodekaschoinos to Rome in -22 (border at Hiera Sykaminos) and back to Kush 'after the Roman withdrawal in 298'. Roman side has nothing, so the strip is nobody's for 320 years. Add contest -23/-22, gain -22 and loss 298 of Lower Nubia within 115 km of Aswan, and a war, citing the Meroë, Kingdom of Kush and Yesebokheamani pages.
6. **Mauretania 40-44**: /ledger/29 gains Mauretania in 40; mauretania /ledger/13-16 keeps the kingdom contested (Aedemon's revolt, 'surrendered in 44 AD') and dissolves it in 44. Add contest_start 40 / contest_end 44 (counterpart mauretania) and a war, or agree with af-02 on 40.
7. **Wars**: the First Jewish-Roman War (66-73) is missing; Bar Kokhba (132-135), Boudica (60-61) and the Marcomannic Wars have empty zones without saying no ground changed hands. Add the war and the zones, or the sentence.

Not blocking:

8. /ledger/83: the East restored in 273; the page's 273 is the revolt 'against the restored Roman rule', so the reconquest is 272. Move with a page that dates it (Palmyrene Empire or Aurelian).
9. /ledger/17, /ledger/23: counterpart 'Germanic tribes between the Rhine and the Elbe' should be 'nobody' (decision 4) or be listed.
10. greek-city-states /ledger/79-80 (78 loss, 83 dissolve to roman-empire, confidence 1) have no Roman gain; add them at confidence 1 or agree with eu-01 to drop them.

## Thin (for a gap-filler)

Cantabrian Wars (/ledger/12, -25 bridged); Raetia (/ledger/16, -14 bridged); Pannonia (Hungary +155 cells in the 43 shape, no event); Agri Decumates occupation and final abandonment (/ledger/45, /ledger/93); Osroene 214 (/ledger/72); end of the Great Conspiracy (/ledger/102); Armenia's client status 117-161 (the page returns it to 'previous rulers and client-kings'); Cappadocia 17 and Commagene 17-38; Lycia 43, Lesser Armenia 72, Moesia's province (AD 6), the Gothic crossing of 376.

## Routed to other groups (cross_checks)

- eu-03 (thracian-kingdom): no Roman vassal relation at all; the AD 6 loss of Moesia (130 cells) to Rome is in no Roman shape before 51 and Rome gains the whole kingdom in 46, so the strip is nobody's 6-45. Drop the AD 6 loss or source a Roman gain.
- eu-01 (cimmerian-bosporus): no Roman vassal relation although Rome tints it from -27; greek-city-states 78/83 events (above).
- me-05 (galatia, kingdom-of-pontus): no Roman vassal relation before annexation.
- af-02 (mauretania): /ledger/10 ends the relation with roman-republic in -25, two years after the Republic dissolved; use roman-empire from -27.
- me-04 (sabaeans): -26..-25 against Rome's -25..-24; within a year, align when touched.

## Gazetteer names wanted

Singara (place, Sinjar 36.32 N 41.86 E; the 363 loss uses a 50 km radius), Transtigritania (the 299 polygon), Pannonia, Raetia.
