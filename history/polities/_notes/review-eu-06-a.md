# Review of batch eu-06-a (huns, goths, burgundians, gothia)

Reviewed 2026-10-19 against history/briefs/reviewer-brief.md. Validator: all four pass with 0 errors (huns: 9 gazetteer warnings, all 'Pannonia'). Reviewer edits were applied in place and re-validated; they are marked applied below.

## huns: fail

Area: The Huns page has no infobox area (map caption only: 'Estimated territory under Hunnic political control under Attila, c. 450 CE'); the dossier notes do not mention the check. Cliopatria peak 1.91 M km2 (451).

Findings:
- [APPLIED] `/ledger/5`: The occupation_end of the 395 raid was a confidence-1 bridge at 396; the page that dates it gives 398. Evidence: Eutropius (consul 399): 'Eutropius' ascension to power was assisted by his defeat of a Hun invasion in 398.' eastern-roman-empire /ledger/6 closes the same occupation in 398. Fix: Year 398, confidence 2, source https://en.wikipedia.org/wiki/Eutropius_(consul_399) (added to sources), note and dossier notes updated.
- [BLOCKING] `/keyframe_review/14, /keyframe_review/15, /keyframe_review/16 and /ledger`: The belt of Germanic subject lands north of the Danube (Germany, Bohemia, Slovakia, southern Poland, up to 53.7 N and west to 6.8 E) enters the shape in 451 with no gain and leaves it in 455 with no loss: the largest land move in the dossier is not in the ledger. Evidence: Grid check (tools/grid.py, gazetteer): the 451 shape minus Gaul has about 2,650 res-5 cells (~670,000 km2) more than the 443 shape minus Moesia and Thrace; the 452 shape minus northern Italy has about 3,300 cells (~830,000 km2) that are neither in the 455 shape nor in the /ledger/17 Gepid regions, of which only ~300 are Pannonia (/ledger/18). The only 451 events are the Gaul occupation; the 452 note keeps the belt 'as drawn'. Fix: Either correct 451-454 to drop the belt and draw the subject peoples as vassals (vassal_start 451 or the year a page gives, vassal_end 454 at Nedao, rule 4), or add a dated gain for the belt (451, page needed) and losses in 454-455 to the peoples of Nedao (rugii-heruli-sciri, Ostrogoths, nobody for the north), so that every cell of the 452 shape that is not in the 455 shape leaves by an event.
- [BLOCKING] `/keyframe_review/2/correction`: The 373-375 correction (Huns 373 minus Gothia 372) keeps about 694 cells (~175,000 km2) that are in neither the Huns 371 shape nor Gothia 372, with no ledger event; its text says 'the Don-to-Caspian lands of the 371 shape', which the spec does not produce. Evidence: Grid check: 155 of the 157 cells of Cliopatria's Cimmerian Bosporus 372 shape and 539 cells of north-Azov and lower-Don steppe (32-43 E, 45-51 N) enter the Hun shape in 373. cimmerian-bosporus /ledger/23 has a 372 loss to huns that has no mirror here. Fix: Add a gain from cimmerian-bosporus at 372/373 (region intersect Huns 373 and Cimmerian Bosporus 372, mirroring its /ledger/23) and a dated gain (counterpart sarmatians or nobody, with a page) for the Azov/lower-Don steppe, or set the correction to the Huns 371 shape for 373-374 and fold the rest into dated gains.
- [BLOCKING] `/keyframe_review/3`: huns_378 (378-382) is marked ok although /ledger/3 gains the whole Gothia 373 shape in 376: 692 of its 1,157 cells (Banat, Crisana, Transylvania, west of 22.6 E) are not in the 378-382 shape and enter only in 383. Evidence: Grid check: Gothia 373 minus Huns 378 = 692 cells, all of them in Huns 383. gothia /keyframe_review/12 removes these cells from Gothia for 378-382 because 'the Huns' own shape also lies from 376', so in keyframes they belong to nobody while both ledgers give them to the Huns in 376. Fix: Mark huns_378 adjust with correction union(Huns 378, Gothia 373), or restrict /ledger/3 to intersect(Gothia 373, Huns 378) and add a dated gain for the rest (that gain then also explains the 383 growth).
- [BLOCKING] `/keyframe_review/8`: huns_407 grows by about 325 cells (~82,000 km2, 18.9-23 E: the Danube-Tisza interfluve and upper Tisza) with no ledger event, and 276 of those cells also leave in 455 with no loss. Evidence: Grid check Huns 407 minus Huns 383 = 325 cells; the 454 Gepid regions and Pannonia do not cover 276 of them. sarmatians.json dissolves to huns in 375 with 'the steppe between the Danube and the Tisza' (the Iazyges), which no huns event receives. Fix: Add a gain from sarmatians (Iazyges) for the interfluve, dated by a page (Iazyges page) or at Cliopatria's 407 at confidence 1, and its loss in 454/455.
- [BLOCKING] `/keyframe_review/11/correction`: The 426-440 correction adds Pannonia from 426, seven years before the cession it cites (/ledger/8, 433); its own text says 'from 433'. Evidence: Huns page: 'In 433 some parts of Pannonia were ceded to them by Flavius Aetius'; western-roman-empire /ledger/21 loses it in 433. Fix: Keep the 426 shape as drawn (verdict ok, Pannonia arrives with the 433 gain) or split it with a new keyframe hunnic-empire_433 (433-440) that adds Pannonia.
- [open, non-blocking] `/ledger/1/counterpart`: Counterpart 'Alans of the Don (Pontic Alans)' is not a slug; sarmatians.json now exists and carries the Alans of the Lower Volga and North Caucasus (alt name 'Alans (steppe)', successor huns). Evidence: Alans page: 'Around 370 ... the Huns attacked the Don Alans' and 'Following the Hunnic invasion in 370' (supports this dossier's 370); sarmatians dissolves to huns in 375. Fix: Set counterpart to sarmatians and drop the Alans from counterparts_needing_dossiers; the sarmatians author should date the loss of the Alan lands to 370 (or split 370/375).
- [open, non-blocking] `/ledger/9-12`: eastern-roman-empire records territorial losses to the Huns in 441 (Danube cities) and 447 (the strip from Singidunum to Novae) and gains back in 451 and 455; this dossier has only contest zones. Also contest_end 448 here against 449 in eastern-roman-empire and on the Huns page. Evidence: Huns page: 'a truce was concluded in 441', 'autumn 443 signed the Peace of Anatolius', 'The war came to an end in 449'; Utus page: the strip was 'a no man's land in the Roman territory' and the treaty 'in the fall of 447' or 'a year later in 448'. This dossier's reading follows the pages; the eastern-roman-empire side is the one to change. Fix: Route to eu-05: eastern-roman-empire should turn its 441 and 447 losses and 451/455 gains into contest or occupation events, or both dossiers agree on a cession. Consider 449 for /ledger/12 (Huns page).
- [open, non-blocking] `/ledger/17/counterpart`: The 454 loss names kingdom-of-the-gepids, whose Cliopatria row opens only in 510, while the author's report asks for a separate 'gepids' dossier for 454-509. Evidence: Author report counterparts_needing_dossiers: suggested_slug 'gepids', years 454-509. Fix: Use whichever slug the orchestrator assigns to the Gepids of 454-509 in both places.
- [open, non-blocking] `/identity/rulers`: Rulers have gaps (380-399, 410-411); the brief asks for contiguous rulers where given. Evidence: Balamber 370-379, Uldin 400-409, Charaton 412-419. Fix: State the gaps in the rulers' notes (no ruler recorded) or leave as is if the schema allows gaps.

Thin (for a gap-filler):
- `/ledger/0`: found 106 is Cliopatria's year at confidence 1 ('first reported living east of the Volga'). Try https://en.wikipedia.org/wiki/Xiongnu
- `/ledger/18`: 455 loss of Pannonia to the Ostrogoths at confidence 1 (Cliopatria's year). Try https://en.wikipedia.org/wiki/Ostrogoths

Spot checks:
- `/ledger/7` https://en.wikipedia.org/wiki/Uldin: confirmed ('forced to re-cross the Danube by March 23, 409')
- `/ledger/13` https://en.wikipedia.org/wiki/Battle_of_the_Catalaunian_Plains: confirmed (Rhine 'early in 451', Metz 7 April, final assault 14 June)
- `/ledger/14` https://en.wikipedia.org/wiki/Battle_of_the_Catalaunian_Plains: confirmed ('circa 20 June'; Gallic Chronicle 'withdrew to his homeland')
- `/ledger/20` https://en.wikipedia.org/wiki/Dengizich: confirmed (Marcellinus Comes and Chronicon Paschale quotes, 469)
- `/ledger/21` https://en.wikipedia.org/wiki/Battle_of_Nedao: confirmed ('decisively defeated in 469', 'After that point, the Huns cease to exist in European history.')
- `/ledger/17` https://en.wikipedia.org/wiki/Battle_of_Nedao: confirmed for 454 and the victors; the Gepids taking Dacia and the Tisza plain is not on the page (confidence 2 is right)
- `/ledger/2` https://en.wikipedia.org/wiki/Ermanaric: confirmed (invasion 'in the 370s', death 376 in the infobox); 'c. 375' is on the Goths page
- `/ledger/1` https://en.wikipedia.org/wiki/Alans: confirmed ('Around 370 ... the Huns attacked the Don Alans')
- `/ledger/8` https://en.wikipedia.org/wiki/Huns: confirmed ('In 433 some parts of Pannonia were ceded to them by Flavius Aetius')
- `/ledger/5` https://en.wikipedia.org/wiki/Eutropius_(consul_399): mis-dated (396 bridge; page has 398) - fixed

## goths: thin

Area: No infobox area on the Goths page (checked); acknowledged in the author's notes.

Findings:
- [open, non-blocking] `/ledger/2/counterpart`: Counterpart 'Ulmerugi (Rugii)' is neither a slug nor listed in counterparts_needing_dossiers. Evidence: Gothiscandza page: the Ulmerugi 'had arrived in the area already before the Goths' (Jordanes, undated). No dossier will be written for a 1st-century Jordanes tribe. Fix: Set counterpart to nobody and keep the Ulmerugi in the note, or list them in counterparts_needing_dossiers.

Thin (for a gap-filler):
- `/ledger/0`: 30 start is Cliopatria's (confidence 1); no page dates a Gothic polity in Sweden. Try https://en.wikipedia.org/wiki/Getica
- `/ledger/1`: 43 departure from Scandza is Cliopatria's year inside 'the first half of the 1st century CE' (confidence 1). Try https://en.wikipedia.org/wiki/Berig
- `/ledger/3`: 154 loss of the Pomeranian coast at confidence 1; the Wielbark page dates the Pomeranian abandonment to the first half of the 3rd century, not 154. Try https://en.wikipedia.org/wiki/Wielbark_culture
- `/ledger/5`: 206 end is Cliopatria's (confidence 1); Oium/Filimer undated. Try https://en.wikipedia.org/wiki/Filimer

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Gothiscandza: confirmed ('during the first half of the 1st century CE'; Jordanes' reliability 'called into question')
- `/ledger/2` https://en.wikipedia.org/wiki/Gothiscandza: confirmed (naming of Gothiscandza, Ulmerugi, Vandals defeated; undated)
- `/ledger/3` https://en.wikipedia.org/wiki/Wielbark_culture: confirmed quote ('Isolated pockets ... until the 5th century'); year 154 is Cliopatria's, the page dates the Pomeranian abandonment to the first half of the 3rd century
- `/ledger/4` https://en.wikipedia.org/wiki/Goths: confirmed ('Beginning in the middle of the 2nd century, the Wielbark culture shifted southeast towards the Black Sea')

## burgundians: fix

Area: No infobox area on the Burgundians or Kingdom of the Burgundians page (checked); acknowledged in the author's notes.

Findings:
- [APPLIED] `/ledger/2/counterpart`: Counterpart 'Alemanni' was not a slug; alemanni.json (213-461) now exists. Evidence: history/polities/alemanni.json identity slug 'alemanni'. Burgundians page: 'Burgundiones Alamannorum agros occupauere' (panegyric of 291). Fix: Counterpart set to alemanni. The alemanni dossier has no 291 loss to burgundians: routed in cross_checks.
- [open, non-blocking] `/ledger/4-6`: western-roman-empire models the 413 settlement as vassal_start of burgundian-kingdom (land stays Roman, tinted vassal) and has no 409-413 occupation; this dossier has a 409 occupation, a 413 occupation_end and a 413 gain from western-roman-empire. Evidence: western-roman-empire /ledger/16: 413 vassal_start, counterpart burgundian-kingdom. Kingdom of the Burgundians page: 'accepted as Roman foederati' after 413; infobox grant 411. Fix: Agree one model with eu-04: either this dossier's 413 gain becomes a vassal_start (counterpart western-roman-empire) or western-roman-empire adds the 409 occupation and a 413 loss to burgundians.

Thin (for a gap-filler):
- `/ledger/1`: 291 westward move over the Oder at confidence 1 (page: 'shifting westwards over the Oder', undated). Try https://en.wikipedia.org/wiki/Laterculus_Veronensis
- `/ledger/3`: 409 Rhine crossing at confidence 1: Burgundians page 'In about 406', Kingdom page 'before 409'. Try https://en.wikipedia.org/wiki/Crossing_of_the_Rhine

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Burgundians: confirmed ('between the Suevus (probably the Oder) and Vistula rivers'; year 154 is Cliopatria's)
- `/ledger/2` https://en.wikipedia.org/wiki/Burgundians: confirmed (panegyric of 291; 'Burgundiones Alamannorum agros occupauere')
- `/ledger/4` https://en.wikipedia.org/wiki/Burgundians: confirmed ('In 409, Saint Jerome first listed the Burgundians')
- `/ledger/6` https://en.wikipedia.org/wiki/Burgundians: confirmed (Prosper, 413: 'gave the Burgundians a part of it near the Rhine')
- `/ledger/7` https://en.wikipedia.org/wiki/Kingdom_of_the_Burgundians: confirmed (infobox 'Borbetomagus (411-437)'; grant 411 in the infobox timeline)

## gothia: fix

Area: 'Gothia' is a disambiguation page (checked); no infobox on the Goths, Thervingi or Greuthungi pages. Acknowledged in the author's notes.

Findings:
- [APPLIED] `/ledger/5, /keyframe_review/10/correction`: The loss of the Greuthungi steppe was dated 373 against huns /ledger/2 at 375, leaving the steppe stateless in 373-374. Evidence: Goths page (this dossier's source): 'Around 375 the Huns overran the Alans ... and then, along with Alans, invaded the territory of the Goths'; Alans page: 'These Alans successfully invaded the Goths in 375 together with the Huns'; Greuthungi page only 'in the early 370s'; Ermanaric infobox: died 376. Fix: Loss moved to 375 (source Goths page); gothia_373 correction now the Gothia 372 shape (steppe kept until the 375 loss); successor text and notes updated.
- [open, non-blocking] `/ledger/1/counterpart`: The 260 gain names nobody, but sarmatians.json loses the same land (Gothia 260 minus Gothia 207) to gothia in 260. Evidence: sarmatians ledger: 260 loss, counterpart gothia, region minus(Gothia 260, Gothia 207); its 207 loss to gothia is also unmatched here (the found event names goths). Fix: Set counterpart to sarmatians (and say in the found note that the 207 land came from the Sarmatian steppe).
- [open, non-blocking] `/keyframe_review/12/note`: The note says the Huns' own shape covers Dacia, Wallachia and Transylvania from 376; it does so only from 383 for 692 of the 1,157 Gothia 373 cells. Evidence: Grid check Gothia 373 minus Huns 378 = 692 cells, all in Huns 383. The fix belongs in huns (/keyframe_review/3); this note should not assert it. Fix: Reword once the huns fix is made.

Thin (for a gap-filler):
- `/ledger/0`: 207 start and 207-237 realm are Cliopatria's (confidence 1, keyframe unverified: page budget). Try https://en.wikipedia.org/wiki/Chernyakhov_culture
- `/ledger/1`: 260 eastward growth to the Don at confidence 1. Try https://en.wikipedia.org/wiki/Gothia_(Roman_province)
- `/keyframe_review/5-9`: Gothic holding of Dacia 270-372 unverified (Taifali, Victohali and Carpi share it). Try https://en.wikipedia.org/wiki/Taifals

Spot checks:
- `/ledger/2` https://en.wikipedia.org/wiki/Goths: confirmed ('In 270 ... Aurelian, who, however, did surrender Dacia beyond the Danube')
- `/ledger/5` https://en.wikipedia.org/wiki/Greuthungi: mis-dated relative to the Goths and Alans pages (373 vs 'Around 375'/'in 375') - fixed to 375
- `/ledger/6` https://en.wikipedia.org/wiki/Gothic_War_(376%E2%80%93382): confirmed ('In the summer of 376 ...'; 'placed the Thervings along the southern bank of the Danube in Lower Mœsia')
- `/ledger/9` https://en.wikipedia.org/wiki/Gothic_War_(376%E2%80%93382): confirmed ('peace was declared on 3 October 382'; Scythia, Mœsia and possibly Macedonia)
- `/ledger/3` https://en.wikipedia.org/wiki/Thervingi: confirmed (Valens attacked north of the Danube; 369 peace 'in the middle of the Danube'; 'Gothic War of 367-369' on the Gothic War page)

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| huns 370 gain (Alans of the Don (Pontic Alans)) | sarmatians 375 dissolve | mismatch | sarmatians.json now covers the Alans; 5 years apart. Alans page supports 370. Route the date to the sarmatians author; huns should name sarmatians. |
| huns 375 gain (gothia) | gothia 375 loss | matched | Gothia moved from 373 to 375 by the reviewer (Goths and Alans pages). |
| huns 376 gain (gothia) | gothia 376 loss | matched | Extent disagrees with huns_378 keyframe (692 cells); see huns fix. |
| huns 395 occupation_start (eastern-roman-empire) | eastern-roman-empire 395 occupation_start | matched |  |
| huns 398 occupation_end (eastern-roman-empire) | eastern-roman-empire 398 occupation_end | matched | huns moved from 396 to 398 by the reviewer. |
| huns 408 occupation_start (eastern-roman-empire) | eastern-roman-empire 408 occupation_start | matched |  |
| huns 409 occupation_end (eastern-roman-empire) | eastern-roman-empire 409 occupation_end | matched | Both March 409. |
| huns 433 gain (western-roman-empire) | western-roman-empire 433 loss | matched |  |
| huns 451 occupation_start (western-roman-empire) | western-roman-empire 451 occupation_start | matched | April 451 both. |
| huns 451 occupation_end (western-roman-empire) | western-roman-empire 451 occupation_end | matched | June 451 both. |
| huns 452 occupation_start (western-roman-empire) | western-roman-empire 452 occupation_start | matched |  |
| huns 452 occupation_end (western-roman-empire) | western-roman-empire 452 occupation_end | matched |  |
| huns 454 loss (kingdom-of-the-gepids) | kingdom-of-the-gepids  none | exception | No dossier; Cliopatria row opens 510; author lists the Gepids of 454-509 under counterparts_needing_dossiers (slug 'gepids' there). |
| huns 455 loss (ostrogoths) | ostrogoths 454 found | matched | ostrogoths found 454 (counterpart huns), predecessor land Pannonia 455. |
| eastern-roman-empire 441 loss (huns) | huns 441 contest_start | mismatch | ERE loses the Danube cities; huns has a contest only (Huns page: truce 441, no cession). Route to eu-05. |
| eastern-roman-empire 447 loss (huns) | huns 447 contest_start | mismatch | ERE loses the Singidunum-Novae strip; Utus page calls it 'a no man's land in the Roman territory'. Route to eu-05. |
| eastern-roman-empire 451 gain (huns) | huns  none | mismatch | Follows from the 447 loss; no huns loss. |
| eastern-roman-empire 455 gain (huns) | huns  none | mismatch | Danube bank re-established; no huns loss to ERE. |
| cimmerian-bosporus 372 loss (huns) | huns  none | missing | 155 Bosporan cells enter huns_373 with no gain; huns fix /keyframe_review/2. |
| sarmatians 375 dissolve (huns) | huns  none | missing | Iazyges' Danube-Tisza steppe never received by huns (huns_407 growth unexplained). |
| rugiland 454 found (huns) | huns  none | exception | huns successor note: Rugiland outside the Hun shapes; but the 452 belt is not released by any event (huns fix). |
| gothia 207 found (goths) | goths 206 dissolve | matched |  |
| sarmatians 207 loss (gothia) | gothia 207 found | exception | gothia's found names goths only; acceptable if gothia's note names the Sarmatian steppe. |
| gothia 260 gain (nobody) | sarmatians 260 loss | mismatch | Counterpart: gothia says nobody, sarmatians says gothia. Gothia should name sarmatians. |
| gothia 270 gain (roman-empire) | roman-empire 271 loss | mismatch | Year within one; roman-empire's counterpart is nobody (Dacia abandoned 271-275). Goths page: 270. Route to eu-04 to name gothia or keep nobody by agreement. |
| gothia 376 occupation_start (roman-empire) | roman-empire  none | missing | Roman Lower Moesia and Dobruja under the Thervingi 376-382: roman-empire has no occupation. Route to eu-04. |
| gothia 382 occupation_end (roman-empire) | roman-empire 382 contest_end | exception | roman-empire closes the war (3 Oct 382), not an occupation; resolves with the 376 item. |
| gothia 382 dissolve (roman-empire) | roman-empire 382 contest_end | exception | Foederati settled on Roman land; no land changes owner. |
| cimmerian-bosporus 330 loss (goths) | gothia  none | mismatch | Tanais 'devastated by Goths AD 330': goths ended in 206, the counterpart should be gothia (or nobody for a raid); no Gothia shape reaches the Don mouth. Route to eu-01. |
| goths 43 gain (Ulmerugi (Rugii)) |   none | exception | Legendary (Jordanes), confidence 1, no dossier; should be nobody or listed. |
| goths 206 dissolve (gothia) | gothia 207 found | matched |  |
| burgundians 291 gain (alemanni) | alemanni  none | missing | alemanni.json (213-461) has no 291 loss to burgundians. Route to the alemanni author. |
| burgundians 409 occupation_start (western-roman-empire) | western-roman-empire  none | missing | WRE has no Burgundian occupation 409-413. |
| burgundians 413 occupation_end (western-roman-empire) | western-roman-empire  none | missing | as above |
| burgundians 413 gain (western-roman-empire) | western-roman-empire 413 vassal_start | mismatch | WRE: vassal_start of burgundian-kingdom (land stays Roman); burgundians: gain. Agree one model. |
| burgundians 413 dissolve (burgundian-kingdom) | burgundian-kingdom  none | exception | burgundian-kingdom belongs to another part of eu-06, not written yet. |

## Other

- Neighbour dossiers read: roman-empire, western-roman-empire, eastern-roman-empire, sasanian-empire (no Hun or Gothic events for this batch), cimmerian-bosporus; also sarmatians, alemanni, ostrogoths, rugiland. Not written yet (counterparts owned by groups that have not run): vandals, caucasian-albania, caucasian-iberia, lazica, kingdom-of-armenia, burgundian-kingdom, kingdom-of-the-gepids.
- The author's 'Alans of the Don' and 'alemanni' requests are now covered by sarmatians.json and alemanni.json.
- hunnic-empire.json does not exist (good): huns.json reviews both Cliopatria rows; keep it that way.
- WebFetch failed for https://en.wikipedia.org/wiki/Eutropius_(consul) (as for the author); https://en.wikipedia.org/wiki/Eutropius_(consul_399) loaded.
- Grid checks used tools/grid.py polity_cells and the gazetteer; Pannonia cannot be resolved, so the Pannonian part of the huns figures is estimated (lon < 19 E, lat < 48.6 N).
- Reviewer edits applied in place and re-validated (0 errors, 0 warnings): huns /ledger/5 and sources/notes; gothia /ledger/5, /keyframe_review/10, successors text, notes; burgundians /ledger/2 counterpart.
- Gazetteer: Pannonia (region, huns) is needed in regions.jsonl.
