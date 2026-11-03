# Review, batch eu-03-a (etruscans, roman-kingdom)

Reviewer run of 2026-10-19. Validator (`--resolve`): 0 errors, 0 warnings for both files. The author's run of 2026-10-19 opened no page (both dossiers kept from the 2026-10-18 run); the reviewer opened 7 pages (Veii, Volsinii, Roman-Etruscan Wars, Etruscan civilization, Boii (Cisalpine Gaul), Roman Kingdom) and tested the Cliopatria geometry itself (cliopatria_polities_only_v021.geojson, shapely point-in-polygon), not only the bboxes in shapes.csv.

Verdicts: **etruscans fail**, **roman-kingdom fail**. Every page fact checked is on its page with its year; nothing is fabricated. Both fail on wrong shape corrections around Rome and Veii: the keyframe notes describe places as inside the Cliopatria shapes when the geometry does not contain them.

## The geometry around the lower Tiber (affects both dossiers)

Point-in-polygon tests on the Cliopatria shapes:

| place (lon, lat) | Etruscans -750/-650/-600 | Etruscans -550 .. -265 | Roman Kingdom -750/-700/-500 |
| --- | --- | --- | --- |
| Rome, Capitol (12.482, 41.893) | inside | outside | **outside** (shape's east edge is 12.452) |
| Alba Longa (12.65, 41.747) | inside | outside | outside |
| Fidenae (12.515, 41.99) | inside | outside | outside |
| Ostia (12.292, 41.756) | outside | outside | outside |
| Veii (12.396, 42.024) | outside | **outside, all 14 shapes** | **inside** |
| Caere (12.10, 41.995), Pyrgi (11.95, 42.01) | outside | outside, all 14 shapes | outside |
| Volsinii/Orvieto (12.11, 42.72) | inside | inside to -292; **outside -291 and -271** | n/a |

- The Roman Kingdom shape (6 vertices, 859 km2) lies 95 percent on the right bank of the Tiber. It is the ager Veientanus, not the ager Romanus: it holds Veii and neither Rome nor Alba Longa nor Ostia. The Republic's first Cliopatria shapes (-500, -480) are the same strip and contain Rome itself only from -337 (a matter for the roman-republic owner).
- From -550 on, every Etruscan mainland shape stops at 42.106 N east of 11 E. The 41.33 N south edge of the -530..-265 bboxes is Corsica's southern tip, not the Veii-Caere coast.
- The -750, -650 and -600 Etruscan shapes hold about 1,480 km2 of Latium vetus south and east of the Tiber, Rome and the Alban hills included. The corrections trim only Latina, Frosinone, Caserta and Napoli, so the corrected shape keeps Rome as Etruscan from -900 to -531. Keyframes 4 and 5 bring it back by unioning the -600 shape.

## etruscans: fail

Blocking (not applied):
1. `/keyframe_review/0`, `/1`, `/2`, `/3`, `/4`, `/5`: Latium vetus (Rome, Alba Longa, Fidenae) stays Etruscan from 900 to 531. That contradicts the dossier's own notes ("the Roman Kingdom under the Tarquins is drawn as Rome, not as Etruria"), the page ("roughly what is now Tuscany, western Umbria and northern Lazio"), and roman-kingdom (from 753) and latin-league. Fix: subtract the left bank of the lower Tiber from the -900, -750, -650 and -600 corrections and from the -600 shape where it is unioned into -550 and -540. Use a polygon or a union of discs: Rome 12.48/41.89, the Alban hills 12.68/41.75, the coast to Antium. Keyframe 3 becomes adjust.
2. `/keyframe_review/4` to `/16` and `/ledger/12`, `/22`, `/27`: the notes claim that Veii and Caere are in the shapes ("the Veii-Caere coast is back" at -530; "Etruria with Veii and Caere" at -424), but no Etruscan shape after -551 contains Veii, Caere or Pyrgi. The confidence-3 loss of Veii in 396 (`/ledger/12`), the Pyrgi loss in 300 and the Caere loss in 273 therefore remove land that no keyframe draws, and the -273 keyframe's 18 km minus disc (reaching 42.16 N) removes nothing from a shape whose mainland starts at 42.171 N. Fix: add Veii (disc 12.39/42.02, 12 km) to the corrections up to -397, and the Caere-Pyrgi country (disc about 12.05/42.0, 18 km) up to -274 (Pyrgi to -301). Correct the notes. Veii comes out of roman-kingdom (below).
3. `/keyframe_review/15`, `/17` and `/identity/capitals/0`: Cliopatria moves Orvieto and the Volsinian country into the Republic's -291 shape. The -291 and -271 corrections do not add it back, so the capital lies outside the state from 291 to 264, and the confidence-3 events `/ledger/28`-`/30` (265-264) fight over and lose land the keyframes have already dropped. Fix: add the Volsinii disc (12.11/42.72, 25 km) to the -291, -273 and -271 corrections up to 264, which is the dossier's own reading ("the land stays"). Or add a dated loss of 291/280 and move the capital. Either way, tell the roman-republic owner.

Non-blocking:
4. `/identity/type` "umbrella": the schema reserves umbrella for associations that are "never coloured as territory" (Cliopatria's parenthesised names). Etruscans is a leaf row with 14 shapes, colours.json already assigns it #348f4f, and this dossier draws and loses territory. Fix: "state". This is a pattern across eu-03 (samnites, latin-league, volsci, aequi, sabines, umbri, lucanians, picentes, adriatic-veneti are umbrella too), so the orchestrator should rule.
5. `/identity/family` "etruscan" is not a key of colours.json families. **Applied** by the reviewer: "italy" (hue 145-170, which contains the assigned h150). Re-validated: 0 errors, 0 warnings.
6. `/ledger/14` (-396, the largest land move, about 33,000 km2): the whole Po valley (Emilia, Lombardy, Venetia, Rimini) goes to boii. But boii's -396 found takes Emilia only, insubres found Lombardy in -400 from "nobody", senones found the ager Gallicus in -390 from umbri, and adriatic-veneti hold Venetia from -900. Fix: split the loss by counterpart (boii: Emilia; insubres: Lombardy; senones: Rimini) and settle Adria/Venetia with adriatic-veneti.
7. Shape trims with no loss event: -383 to -337 (1,108 km2 centred at 12.13/42.26, the Sutrium-Nepet country), -337 to -326 (567 km2 at 12.26/42.63), -326 to -291 (1,285 km2, Volsinii included; see 3). Only contest events cover these spans.
8. `/ledger/11`, `/12`: the quoted words differ from the current Veii page ("commence a siege lasting many years"; "slaughtered the entire adult male population and made slaves of all the women and children"). The facts and years match. Quote verbatim.
9. `/ledger/18` cites the Roman-Etruscan Wars page for "358 BC: Alliance of Tarquinia and Cerveteri against Rome". That line is in the Etruscan civilization timeline, not the Wars page. `/ledger/5`: the Wars page says "between 483 and 476 BC" (the dossier has 482, within a year).

Spot checks (all confirmed): `/ledger/11` and `/12` (Veii: war 406, fall 396); `/ledger/18` and `/19` (Wars: Fabius and 307 prisoners in 358, 8,000 prisoners in 356, surrender in 354, Caere's hundred-year truce in 353, forty-year truces in 351); `/ledger/28` and `/29` (Volsinii: 265 embassy, Gurges killed, Flaccus "a year later", "destroyed by the Romans in 264 BC"); `/ledger/14` (Boii: "Pliny instead date the start of the invasion to 396 BC" in a footnote, main text 390-386); `/ledger/0` (900 BC, "identifiably Etruscan"); `/ledger/22` ("300 BC: Pyrgi becomes a Roman colony"); `/ledger/27` (Brice: Caere 273); `/ledger/15` (Volsinii "made incursions into the Roman territory in 391 BC").

Area: the infobox gives no area. The Cliopatria maximum is 65,835 km2 (-530); the page's "Tuscany, western Umbria and northern Lazio" is about 32,000 km2 against 42,548 km2 for the -750 shape. Under a factor of two; acknowledged.

Thin (confidence 1): `/ledger/1` -650 and `/ledger/3` -550 (Padane Etruria; try History of Bologna, Mantua), `/ledger/15`-`/16` (391-390; the Volsinii page supports 391, so it can go to 2), `/ledger/17` Corsica 384 (a bridge date shared with carthage; try History of Corsica, Aléria).

## roman-kingdom: fail

Blocking (not applied):
1. `/keyframe_review/0` and `/1`, `/ledger/0`, `/1`, `/2`, `/4`, `/identity/capitals/0`: the Cliopatria shape is misplaced (see the table). The notes ("the ager Romanus between the Tiber mouth and the Anio, Alba Longa and Ostia already inside"; "Alba Longa lies inside Cliopatria's shape already"; Ostia "inside the drawn shape") are false. The capital Rome (12.48, 41.89) lies east of the shape's 12.452 E edge. Fix: give both keyframes verdict wrong with a correction that draws Rome and its ager on the left bank: a disc of about 12-15 km on 12.48/41.89, which matches the expansion page's "15 miles" as an upper bound, plus the Janiculum bank, and without the Veii disc (12.39/42.02, 12 km), which is Etruscan until 396. The -672 (Alba Longa) and -640 (Ostia) gains then add their discs. Use the same land for the found, dissolve and successor regions, and tell roman-republic, whose -509 keyframe copies this shape.

Non-blocking:
2. `/ledger/3` (-616 gain from nobody of the already-held shape) moves no land. Drop it or keep the facts in the notes.
3. Rulers: the page lists Numa to 672 and Tullus from 672, the same as the dossier. Fine.

Spot checks (all confirmed on the Roman Kingdom page): `/ledger/0` ("Founding of Rome: 753 BC"), `/ledger/1` (Alba Longa "completely destroyed", Tullus 672-640), `/ledger/2` (Ostia Antica, Ancus 640-616), `/ledger/3` ("doubling the size of Rome", Priscus 616-578), `/ledger/4` ("Monarchy overthrown: 509 BC", the first consuls, Porsena variant).

Area: the infobox gives no area; Cliopatria has 858.8 km2; acknowledged ("The page gives no km2 figure").

Thin: `/ledger/1`, `/2`, `/3` at confidence 1 (reign-start years); try Alba Longa, Ostia Antica, Lucius Tarquinius Priscus.

## Cross-dossier matrix

| event | mirror | status |
| --- | --- | --- |
| etruscans -540 gain greek-city-states (Corsica) | greek-city-states -540 loss | matched |
| etruscans -435 loss roman-republic (Fidenae) | roman-republic -435 gain "Fidenae (Latin town allied to Veii)" | mismatch: counterpart; Fidenae is in no Etruscan shape after -551 |
| etruscans -424 loss samnites (Campania) | samnites -424 gain | matched |
| etruscans -396 loss roman-republic (Veii) | roman-republic -396 gain | matched in the ledgers; neither side draws Veii as Etruscan |
| etruscans -396 loss boii (Po valley) | boii -396 found (Emilia only); insubres -400 found from nobody; senones -390 found from umbri | mismatch: land |
| etruscans -384 loss carthage (Corsica) | carthage -384 gain | matched (both confidence 1) |
| etruscans -300 loss roman-republic (Pyrgi) | none | missing |
| etruscans -273 loss roman-republic (Caere) | none | missing |
| etruscans -264 loss roman-republic (Volsinii) | roman-republic -264 gain | matched |
| etruscans -264 dissolve | roman-republic -264 vassal_start etruscans | exception (tint) |
| etruscans contest pairs -482/-474 ... -265/-264 (9) | none in roman-republic | missing |
| roman-kingdom -672 gain latin-league | latin-league -672 loss | matched |
| roman-kingdom -509 dissolve | roman-republic -509 found | matched |
| roman-kingdom -753 found from nobody | etruscans keyframes 0-5 hold Rome from 900 to 531 | mismatch (overlap) |

## For the orchestrator

- roman-republic (another eu-03 part, not yet reported): its Cliopatria -500 and -480 shapes do not contain Rome (Rome is in its shapes only from -337), and its -509 keyframe copies the misplaced Roman Kingdom shape. It is also missing the -435/-300/-273 Etruscan gains and every contest event with etruscans.
- The type umbrella and invented families (latin, italic, gallic, etruscan) recur across eu-03.
