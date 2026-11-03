# Review: batch eu-06-d

Adversarial review, 2026-10-19, of visigothic-kingdom, vandal-kingdom, ostrogoths, rugiland, revolt-of-athanagild and revolt-of-hermenegild. Validator: all six 0 errors, 0 warnings with --resolve, before and after the reviewer edits. Neighbour dossiers read: eastern-roman-empire, western-roman-empire, byzantine-empire, kingdom-of-soissons (context list), plus huns, kingdom-of-odoacer, mauro-roman-kingdom and kingdom-of-the-aures as counterparts. The other context polities are not written yet (counterparts owned by groups or parts that have not run). The machine copy is history/notes/phase-b/reviews/eu-06-d.json.

Summary: visigothic-kingdom fix; vandal-kingdom fix; ostrogoths fail; rugiland fix; revolt-of-athanagild pass; revolt-of-hermenegild pass. Fixes marked [applied] were made by the reviewer in the dossier and re-validated; [author] items are for the author or the counterpart group.

## visigothic-kingdom: fix

Area: {"infobox_km2": 500000, "infobox_year": 484, "cliopatria_km2": 689151, "ratio": 1.38, "acknowledged": true, "second": {"infobox_km2": 600000, "infobox_year": 580, "cliopatria_km2": 438274, "ratio": 0.73}}

Findings:
- [applied] /identity/rulers/0/from: Wallia's entry started in 415, before the state's start (418); rulers must lie inside the life. Evidence: Ruler span 415-418 against start.year 418 (brief rule 2). Fix: Set from to 418 and keep the page's 415-418 in the note.
- [applied] /wars/8/zones: Liuvigild's reconquest (569-585) had empty zones although ground changed hands. Evidence: Liuvigild page: 'subdued Zamora, Palencia, and Leon' (569), Medina Sidonia the year after 570, 'seized Córdoba from the Byzantine Empire', 'In 585, Liuvigild conquered the Suebi peoples'. Fix: Zones added: Zamora, Palencia, Cádiz, Córdoba admin1 and the Kingdom of the Suebi 585 shape.
- [author] /wars/2/zones: The 456 campaign against the Suebi has empty zones although its own outcome says the Goths then held the Spanish provinces. Evidence: Brief rule 10: empty zones only where no ground changed hands. Fix: Add the Suebic land invaded (e.g. the Kingdom of the Suebi 456 shape, or Gallaecia with Braga) as the zone.
- [author] /ledger (missing vassal_start 418, vassal_end 475): The dossier records no vassalage to Rome, though its own 418 note quotes the page's 'Visigothic federates' and the western-roman-empire dossier has vassal_start visigothic-kingdom 418 (c3) and vassal_end 475 (c3). Evidence: Visigothic Kingdom page: 'In 418, Honorius rewarded his Visigothic federates'; western-roman-empire /ledger/19 and /ledger/57. Fix: Add vassal_start 418 and vassal_end 475 with counterpart western-roman-empire (the Euric page has Nepos recognising Euric's independence in 475).
- [author] /ledger/19: The Byzantine landing is dated 555 here, but the dossier's own war entry says 'Spania held 552-624' and eastern-roman-empire /ledger/49 has the gain in 552. Evidence: Spania page: 'The army was probably sent in 552 and made landfall in June or July'; a second force 'landed at Cartagena in early March 555'. Fix: Move the loss to 552 (coastal Baetica) or split it 552/555, and agree the year with eastern-roman-empire.
- [author] /ledger (missing gain c. 589-592 from eastern-roman-empire): Cliopatria's 592 shape adds 12 south-eastern cells and eastern-roman-empire /ledger/69 has a 592 loss to visigothic-kingdom, but this ledger has no event. Evidence: Spania page: Baza 'was Visigothic by 589'. Fix: Add a gain from eastern-roman-empire (Baza, by 589, confidence 2) and agree the year with the ERE dossier.
- [author] /ledger/38 and /keyframe_review/31: The 714 loss keeps Asturias Visigothic (minus Hispania, Asturias); the 718 keyframe then drops it with no ledger event, so Asturias is drawn Visigothic 714-717 and leaves without a counterpart. Evidence: Visigothic Kingdom page: 'Pelagius revolted in 718, and defeated the Muslims at the battle of Covadonga'; successors give Asturias and Cantabria to kingdom-of-asturias. Fix: Either include Asturias in the 714 loss to umayyad-caliphate, or add a 718 loss of Asturias to kingdom-of-asturias.
- [author] /ledger/26: Mérida is gained in 582 from 'Masona of Merida (Nicene bishop)', a person with no dossier, and the city was never lost before (it is inside the kingdom from 469), so the event changes nothing and has no counterpart. Evidence: Liuvigild page: 'Mérida, which had been under the political control of its popular bishop Masona since the early 570s'. Fix: Either add a confidence-1 loss of Mérida to Masona in the early 570s, or turn the event into a note; do not leave a non-polity counterpart.
- [author] /identity/predecessors: The 418-425 keyframe duplicates Cliopatria's 'visigoths' row (visigoths_417, 417-425, the same 35,099.5 km2 Aquitaine shape), but the dossier names only western-roman-empire as predecessor and does not mention the overlap. Evidence: shapes.csv: visigoths_417 35099.5 km2 bbox -1.25,43.41,1.90,46.28 = visigothic-kingdom_426. Fix: Name visigoths as predecessor and say in notes that the visigoths dossier (eu-06, another part) must end in 417 or the two overlap 418-425.

Thin (for a gap-filler):
- /ledger/1: 451 gain (c1): no page dates the 455-shape growth (try https://en.wikipedia.org/wiki/Theodoric_I)
- /ledger/3: 459 loss (c1): Majorian's peace undated on the page opened (try https://en.wikipedia.org/wiki/Majorian)
- /ledger/14: 510 loss of Provence to the Ostrogoths (c1) (try https://en.wikipedia.org/wiki/Provence)
- /ledger/29: 602 northern gain (c1): Cantabria/Asturias undated (try https://en.wikipedia.org/wiki/Witteric)
- /ledger/30: 612 northern gain (c1) (try https://en.wikipedia.org/wiki/Sisebut)
- /ledger/33: 661 loss of the Rioja-Navarre-Aragon belt to the Vascones (c1) (try https://en.wikipedia.org/wiki/Wamba_(king))
- /keyframe_review/14: 523-554 shapes unverified (Amalaric's 531 defeat at Narbonne) (try https://en.wikipedia.org/wiki/Amalaric)

Spot checks: /ledger/0 Visigothic_Kingdom confirmed; /ledger/5 Visigothic_Kingdom confirmed; /ledger/7 Visigothic_Kingdom confirmed; /ledger/32 Visigothic_Kingdom confirmed; /ledger/9 Euric confirmed; /ledger/11 Battle_of_Vouillé confirmed; /ledger/28 Liuvigild confirmed; /ledger/42 Umayyad_conquest_of_Hispania confirmed

## vandal-kingdom: fix

Area: {"infobox_km2": null, "infobox_year": null, "cliopatria_km2": 271182, "ratio": null, "acknowledged": true, "note": "No area on the Vandal Kingdom page (checked); the author says so in notes."}

Findings:
- [applied] /wars/0/from: The war 'Vandal conquest of Roman Africa' ran 429-439, starting before the state's start (435). Evidence: Brief rule 2: wars inside the life; Vandal Kingdom page: treaty of 435, Carthage 439. Fix: from set to 435, with a note that 429-435 belongs to the years before the state (the 'vandals' row).
- [applied] /ledger/14: The 533 loss counted Sardinia as lost to Godas, but the Vandals recovered the island before Tricamarum and never lost it until the conquest. Evidence: Vandalic War page: Tzazon had been 'successful in re-establishing Vandal authority and killing Godas' and then 'left Sardinia and landed in Africa, joining up with Gelimer at Bulla'. Fix: Region cut to Tripolitania, counterpart 'Pudentius (Tripolitania)', note extended.
- [author] /identity/predecessors: The dossier starts in 435 but does not mention Cliopatria's 'vandals' row (vandals_426, 426-438, a 68,460 km2 shape in southern Spain), which overlaps 435-438; western-roman-empire /ledger/22 records its 435 loss to 'vandals', not to vandal-kingdom. Evidence: shapes.csv vandals_426 bbox -7.50,36.03,-2.38,38.55 (Spain); WRE /ledger/22 counterpart 'vandals'. Fix: Add vandals as predecessor and a note that the vandals dossier (eu-06, another part) must end by 435 (the Vandals left Spain in 429), and ask the WRE author to re-point its 435 loss to vandal-kingdom.

Thin (for a gap-filler):
- /ledger/6: 455 occupation_end of Rome (c1): the page gives no end date for the sack (try https://en.wikipedia.org/wiki/Sack_of_Rome_(455))

Spot checks: /ledger/2 Gaiseric confirmed; /ledger/3 Vandal_Kingdom confirmed; /ledger/4 Gaiseric confirmed; /ledger/7 Gaiseric confirmed; /ledger/8 Gaiseric confirmed; /ledger/10 Mauro-Roman_Kingdom confirmed; /ledger/17 Vandalic_War confirmed

## ostrogoths: fail

Area: {"infobox_km2": null, "infobox_year": null, "cliopatria_km2": 417631, "ratio": null, "acknowledged": false, "note": "No infobox area on the Ostrogoths page (checked). The corrected 490-499 shape (120,380 km2) is half the Italian part of the successor's 500 shape (246,830 km2) with no event; not acknowledged."}

Findings:
- [author] [blocking] /keyframe_review/5/correction: The 490-499 correction intersect(Ostrogoths 490, Italy) resolves to 476 cells, about 120,380 km2, with its southern edge at 43.76 N: it leaves out Rome, all of southern Italy and Sicily, although the note says 'only Italy is kept' and 'the shape is that of the Ostrogothic Kingdom from 493'. Evidence: gazetteer resolve: intersect(Ostrogoths 490, Italy) = 120,380 km2, bbox 6.68-13.87 E, 43.76-47.07 N; the Ostrogothic Kingdom 500 shape inside Italy is 246,830 km2 (factor 2.05); kingdom-of-odoacer /ledger/7 hands all of Italy (country Italy) to ostrogoths in March 493; Theodoric the Great page: he 'ruled most of Italy for thirty-three years'. Fix: Keep the north-Italian shape for 490-492 (the war with Odoacer), add a new keyframe 493-499 with Odoacer's realm (Italy without Vandal Sardinia, with Sicily; Dalmatia if a page dates it), and make the 493 gain from kingdom-of-odoacer that land, not Ravenna alone.
- [author] /ledger (missing gain 491): The Vandal Kingdom dossier (/ledger/11) loses Lilybaeum to ostrogoths in 491; this ledger has no matching gain. Evidence: Gaiseric page footnote: 'except for a toehold on the far west coast, Lilybaeum, which was ceded in 491 to Theodoric'. Fix: Add a 491 gain of Lilybaeum (Marsala, 40 km) from vandal-kingdom, and Sicily from kingdom-of-odoacer if a page dates its passing.
- [author] /ledger (missing vassal_start/vassal_end with eastern-roman-empire): The Goths on East Roman soil are drawn as land gained from the Empire (474 Moesia, 479 Epirus) with no vassalage, while eastern-roman-empire has vassal_start ostrogoths 483 and vassal_end 488 and no losses in 474 or 479. Evidence: Ostrogoths page: 'His kingdom, now based on the Lower Danube in Moesia, was recognized as a federate kingdom'; Theodoric the Great page: in 483 'he commanded the Danubian provinces of Dacia Ripensis and Moesia Inferior'; ERE /ledger/22-23. Fix: Record the federate status as vassal_start (counterpart eastern-roman-empire) from 474/476 or 483 to vassal_end 488, and agree with the ERE author whether 474/479 are gains or vassal land.

Thin (for a gap-filler):
- /ledger/11: 499 dissolve to ostrogothic-kingdom (c1), a bridging end; settle the 493-499 overlap with the Ostrogothic Kingdom dossier (try https://en.wikipedia.org/wiki/Ostrogothic_Kingdom)

Spot checks: /ledger/3 Theodoric_the_Great confirmed; /ledger/4 Ostrogoths confirmed; /ledger/6 Theodoric_the_Great confirmed; /ledger/9 Ostrogoths confirmed

## rugiland: fix

Area: {"infobox_km2": null, "infobox_year": null, "cliopatria_km2": 14526, "ratio": null, "acknowledged": true, "note": "No area on the Rugiland page (checked)."}

Findings:
- [applied] /notes: The notes said the page names no capital, but the Rugiland infobox gives 'Capital: Vindobona'. Evidence: Rugiland page infobox: 'Capital: Vindobona'. Vindobona (Vienna, 48.21 N) lies south of the Danube, below the shapes' southern edge (48.26 N). Fix: Notes corrected: the infobox's Vindobona is outside the Rugian land north of the Danube, so no capital is drawn.

Spot checks: /ledger/0 Rugiland confirmed; /ledger/1 Rugiland confirmed; /ledger/2 Rugiland confirmed

## revolt-of-athanagild: pass

Area: {"infobox_km2": null, "infobox_year": null, "cliopatria_km2": null, "ratio": null, "acknowledged": true, "note": "Rebel with no Cliopatria row; a 100 km disc round Seville, the only place the pages name. Tried: mirror events in visigothic-kingdom (551 loss, 554 gain, same region), the 554/555 discrepancy (noted), type and family; could not break it."}

Spot checks: /ledger/0 Athanagild confirmed; /ledger/1 Athanagild confirmed; /identity/capitals/0 Spania confirmed

## revolt-of-hermenegild: pass

Area: {"infobox_km2": null, "infobox_year": null, "cliopatria_km2": null, "ratio": null, "acknowledged": true, "note": "Rebel with no Cliopatria row; Baetica. Tried: mirrors in visigothic-kingdom (580 loss, 584 gain of Baetica), the 579/580 start (page: fell out 579, revolted the following year), the 584 end and 585 execution; could not break it."}

Spot checks: /ledger/0 Hermenegild confirmed; /ledger/1 Hermenegild confirmed

## Cross-dossier matrix

- visigothic-kingdom 418 found (counterpart western-roman-empire) -> western-roman-empire 418 vassal_start: mismatch - WRE models 418-475 as vassalage (vassal_start 418, vassal_end 475, both c3); the Visigothic ledger has no vassal events.
- visigothic-kingdom 451 gain (counterpart western-roman-empire) -> western-roman-empire 455 loss: mismatch - 4 years apart, both confidence 1.
- visigothic-kingdom 456 gain (counterpart western-roman-empire) -> western-roman-empire 458 loss: mismatch - 2 years apart (WRE: Tarraconensis 458).
- visigothic-kingdom 459 loss (counterpart western-roman-empire) -> western-roman-empire 459 gain: matched
- visigothic-kingdom 461 gain (counterpart western-roman-empire) -> western-roman-empire 462 loss: matched - Narbonne; within a year.
- visigothic-kingdom 469 gain (counterpart western-roman-empire) -> western-roman-empire 469 loss: matched
- visigothic-kingdom 471 gain (counterpart western-roman-empire) -> western-roman-empire 471 loss: mismatch - Land differs: Visigoths gain Berry, WRE loses Arles; each side lacks the other land.
- visigothic-kingdom 472 gain (counterpart western-roman-empire) -> western-roman-empire 472 loss: matched - Tarraconensis (WRE also Baetica).
- visigothic-kingdom 475 gain (counterpart western-roman-empire) -> western-roman-empire 475 loss: matched - Auvergne / Gaul.
- visigothic-kingdom 475 gain (counterpart western-roman-empire) -> western-roman-empire 472 loss: mismatch - Barcelona region: WRE loses all Tarraconensis in 472; Visigoths take the Barcelona region only in 475 (Euric page).
- visigothic-kingdom 475 gain (counterpart western-roman-empire) -> western-roman-empire 475 gain: mismatch - Provence: Visigoths gain it in 475 (Euric page: Nepos renounced Provence in 475); WRE regains Arles/Provence in 475 and loses it in 476. Opposite directions.
- visigothic-kingdom 507 loss (counterpart kingdom-of-the-franks) -> no mirror: exception - eu-07 has not run.
- visigothic-kingdom 508 loss (counterpart kingdom-of-the-franks) -> no mirror: exception - eu-07 has not run.
- visigothic-kingdom 510 loss (counterpart ostrogothic-kingdom) -> no mirror: exception - Owned by another eu-06 part, not written yet.
- visigothic-kingdom 551 loss (counterpart revolt-of-athanagild) -> revolt-of-athanagild 551 found: matched
- visigothic-kingdom 554 gain (counterpart revolt-of-athanagild) -> revolt-of-athanagild 554 dissolve: matched
- visigothic-kingdom 555 loss (counterpart eastern-roman-empire) -> eastern-roman-empire 552 gain: mismatch - 3 years apart; the Visigothic war entry itself says Spania held 552-624.
- visigothic-kingdom 569 gain (counterpart kingdom-of-the-suebi) -> no mirror: exception - Owned by another eu-06 part, not written yet.
- visigothic-kingdom 571 gain (counterpart eastern-roman-empire) -> eastern-roman-empire 572 loss: matched - ERE 572 loss covers 561-577 shape difference.
- visigothic-kingdom 572 gain (counterpart eastern-roman-empire) -> eastern-roman-empire 572 loss: matched
- visigothic-kingdom 577 gain (counterpart eastern-roman-empire) -> eastern-roman-empire 572 loss: mismatch - Orospeda 577: ERE dates all its 561-577 losses 572; 5 years apart.
- visigothic-kingdom 580 loss (counterpart revolt-of-hermenegild) -> revolt-of-hermenegild 580 found: matched
- visigothic-kingdom 582 gain (counterpart Masona of Merida (Nicene bishop)) -> no mirror: mismatch - Non-polity counterpart, not in counterparts_needing_dossiers, and no prior loss of Mérida.
- visigothic-kingdom 584 gain (counterpart revolt-of-hermenegild) -> revolt-of-hermenegild 584 dissolve: matched
- visigothic-kingdom 585 gain (counterpart kingdom-of-the-suebi) -> no mirror: exception - Owned by another eu-06 part, not written yet.
- eastern-roman-empire 592 loss (counterpart visigothic-kingdom) -> no mirror: missing - No Visigothic gain c. 589-592 (Spania page: Baza Visigothic by 589).
- visigothic-kingdom 615 gain (counterpart eastern-roman-empire) -> eastern-roman-empire 615 loss: matched
- visigothic-kingdom 624 gain (counterpart eastern-roman-empire) -> eastern-roman-empire 624 loss: matched
- visigothic-kingdom 661 loss (counterpart Vascones) -> no mirror: exception - Listed in counterparts_needing_dossiers.
- visigothic-kingdom 712 loss (counterpart umayyad-caliphate) -> no mirror: exception - me-07 has not run (712-720 losses and the 721 dissolve).
- visigothic-kingdom 718 loss (none) (counterpart kingdom-of-asturias) -> no mirror: missing - Asturias leaves the Visigothic shape at the 718 keyframe with no event; kingdom-of-asturias (Cliopatria 724) not written.
- vandal-kingdom 435 found (counterpart western-roman-empire) -> western-roman-empire 435 loss: mismatch - WRE /ledger/22 names the counterpart vandals (the people row), not vandal-kingdom.
- vandal-kingdom 439 gain (counterpart western-roman-empire) -> western-roman-empire 439 loss: matched
- vandal-kingdom 442 gain (counterpart western-roman-empire) -> western-roman-empire 442 loss: matched
- western-roman-empire 441 loss (counterpart vandal-kingdom) -> no mirror: mismatch - WRE loses Sicily to the Vandals in 441 (c1); the Gaiseric page has the 440 siege of Panormus repulsed and Sicily occupied only in 468. WRE side.
- vandal-kingdom 455 gain (counterpart western-roman-empire) -> western-roman-empire 458 loss: mismatch - Sardinia: WRE 458 (c1) against 455 (Gaiseric page, c3). WRE side.
- vandal-kingdom 455 occupation_start (counterpart western-roman-empire) -> no mirror: missing - WRE has no occupation of Rome in 455.
- western-roman-empire 459 gain (counterpart vandal-kingdom) -> no mirror: mismatch - WRE regains Sicily from the Vandals in 459 and loses it again in 462 (c1); the Vandals hold no Sicily before 468 on the Gaiseric page. WRE side.
- vandal-kingdom 468 gain (counterpart western-roman-empire) -> western-roman-empire 462 loss: mismatch - Sicily: 6 years apart; WRE side.
- vandal-kingdom 476 loss (counterpart kingdom-of-odoacer) -> kingdom-of-odoacer 476 gain: matched
- vandal-kingdom 477 loss (counterpart mauro-roman-kingdom) -> no mirror: missing - mauro-roman-kingdom has no event 470-535.
- vandal-kingdom 484 loss (counterpart kingdom-of-the-aures) -> kingdom-of-the-aures 484 found: matched
- vandal-kingdom 491 loss (counterpart ostrogoths) -> no mirror: missing - Ostrogoths ledger has no 491 gain of Lilybaeum (Gaiseric page: ceded in 491 to Theodoric).
- vandal-kingdom 510 loss (counterpart Frexenses / Laguatan) -> no mirror: exception - Listed in counterparts_needing_dossiers.
- vandal-kingdom 533 loss (counterpart Pudentius (Tripolitania)) -> no mirror: exception - A rebellion of a few months before the Byzantine landing; no polity.
- vandal-kingdom 533 loss (counterpart eastern-roman-empire) -> eastern-roman-empire 533 gain: matched - September 533, Carthage.
- vandal-kingdom 533 loss (counterpart eastern-roman-empire) -> eastern-roman-empire 534 gain: matched - December 533 / March 534.
- vandal-kingdom 534 dissolve (counterpart eastern-roman-empire) -> eastern-roman-empire 534 gain: matched
- ostrogoths 454 found (counterpart huns) -> huns 455 loss: matched - Pannonia, both low confidence.
- western-roman-empire 455 loss (counterpart ostrogoths) -> no mirror: mismatch - WRE also loses Pannonia to the Ostrogoths in 455 (c1), while ostrogoths and huns have it as Hunnic land. One holder must go.
- ostrogoths 474 gain (counterpart eastern-roman-empire) -> eastern-roman-empire 483 vassal_start: mismatch - ERE has no 474 loss; it records the Goths in Moesia as vassals from 483.
- ostrogoths 479 gain (counterpart eastern-roman-empire) -> no mirror: missing - ERE has no 479 event for Epirus.
- ostrogoths 488 loss (counterpart eastern-roman-empire) -> eastern-roman-empire 488 vassal_end: mismatch - Same year, different type (loss against vassal_end).
- ostrogoths 489 contest_start (counterpart kingdom-of-odoacer) -> kingdom-of-odoacer 489 contest_start: matched
- ostrogoths 490 gain (counterpart kingdom-of-odoacer) -> no mirror: missing - Odoacer dossier has no 490 loss of northern Italy.
- ostrogoths 493 gain (counterpart kingdom-of-odoacer) -> kingdom-of-odoacer 493 dissolve: mismatch - Odoacer hands all of Italy; ostrogoths take Ravenna only and keep a shape cut at 43.76 N.
- eastern-roman-empire 493 vassal_start (counterpart ostrogothic-kingdom) -> no mirror: mismatch - ERE names ostrogothic-kingdom for 493 while ostrogoths holds Italy 493-499 (the overlap the author flagged).
- ostrogoths 499 dissolve (counterpart ostrogothic-kingdom) -> no mirror: exception - Not written yet; overlap 493-499 flagged by the author.
- rugiland 454 found (counterpart huns) -> no mirror: missing - huns lists rugiland among successors but has no ledger event; low priority.
- rugiland 487 loss (counterpart kingdom-of-odoacer) -> kingdom-of-odoacer 488 gain: matched - Within a year (Odoacer page 487/488).
- rugiland 487 dissolve (counterpart lombards) -> no mirror: exception - Successor lombards owned by another eu-06 part, not written yet.

## Problems

- Verdict 'fix' on visigothic-kingdom, vandal-kingdom and rugiland: the reviewer applied the small verified fixes (applied: true) and re-validated (0 errors, 0 warnings, --resolve). The applied: false items on visigothic-kingdom and vandal-kingdom are non-blocking reconciliations with other dossiers (vassalage 418-475, the 552/555 landing, Baza, Asturias 714-718, Mérida, the visigoths/vandals people rows); they also appear in cross_checks for routing.
- ostrogoths fails on one blocking finding (the 490-499 correction leaves out half of Italy, factor 2.05 against the successor's Italian land, against its own note) plus two missing mirrors; back to the author.
- Cliopatria people rows overlap the kingdoms and no dossier mentions it: visigoths_417 (417-425) is the same shape as the visigothic-kingdom 418-425 keyframe; vandals_426 (426-438, southern Spain) overlaps vandal-kingdom 435-438. The other eu-06 parts writing visigoths and vandals must end them by 417 and 435.
- western-roman-empire (eu-04) carries several Vandal and Visigothic events that the pages contradict (Sicily 441/459/462, Sardinia 458, Provence 475/476, Tarraconensis 458, Pannonia 455 to the Ostrogoths) and no occupation of Rome in 455; routed via cross_checks.
- Pannonia does not resolve as a gazetteer region (unknown region), although the huns dossier (/ledger/18) uses {"region": "Pannonia"}; Zeugitana and Orospeda do not resolve either (the authors used stand-ins).
- WebFetch returns an extraction, not raw text; the quotations in the spot checks are the extraction's wording.
