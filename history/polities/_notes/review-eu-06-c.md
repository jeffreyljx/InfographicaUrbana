# Review of batch eu-06-c (2026-10-19 brief, run 2026-10-20)

Reviewer: adversarial review of burgundian-kingdom, kingdom-of-the-suebi, frankish-burgundy. Validator: 0 errors for all three; the only warnings are the expected 'no verdict' warnings for the sibling's shapes of the shared Cliopatria row 'Burgundian Kingdom'. Neighbour dossiers read: western-roman-empire, visigothic-kingdom, ostrogothic-kingdom, kingdom-of-alamannia, vandals, alans, burgundians, huns, kingdom-of-odoacer, ostrogoths. kingdom-of-the-franks, austrasia and neustria have no files (eu-07 has not run): those counterparts are exceptions.

## burgundian-kingdom: fail

Area: infobox none; Cliopatria largest/relevant shape 120,408 km2. The infobox gives no area; the dossier says so.

Findings:
- `/ledger/15` (BLOCKING, for the author). The 524 gain (confidence 1) takes minus(Provence, Burgundian Kingdom 500): 88 cells, about 22,255 km2, of which 86 lie inside Cliopatria's Ostrogothic Kingdom 523 shape; no page gives that extent, and the 523 keyframe (523-533, adjusted for years only) does not hold Provence, so ledger and keyframe disagree for 524-534. Evidence: Kingdom of the Burgundians page: Godomar II's reign included 'the recovery of territory south of the Durance' (no year, no bounds). ostrogothic-kingdom holds Provence from its /ledger/3 (510 gain) to /ledger/12 (540 loss to the Franks) and has no 524 loss to the Burgundians. Gazetteer: the region resolves to 88 cells, 86 of them in the Ostrogothic Kingdom 523 shape. Fix: Shrink the region to what the page says, for example intersect(minus(Provence, Burgundian Kingdom 500), {river: Durance, km: 20}) with text 'territory south of the Durance', and add that same strip to the 523 correction from the event year (note it), or keep the event without the Provence region. Keep confidence 1 and list the Ostrogothic loss for the ostrogothic-kingdom author.
- `/ledger/2/confidence` (applied by reviewer). The 443 Sapaudia gain was confidence 3, but the region (Cliopatria's 443 shape) reaches the Yonne and Nievre, land neither page names. Evidence: Kingdom page: Sapaudia 'included Geneva, and Neuchatel' in Maxima Sequania. Sapaudia page: 'It originally covered the territory around Lake Neuchatel', bounded by the Vosges, the Aar, the upper Rhone and the Saone valley. The 443 shape runs west to 2.95 E (about 60 of 334 cells lie west of 4.3 E). Fix: Confidence lowered to 2 and the reason added to the note.
- `/wars/4/belligerents` (applied by reviewer). 'Odoacer' was free text although kingdom-of-odoacer.json exists (476-493); 'ostrogothic-kingdom' starts in 500, so in 490 Theoderic's people are ostrogoths (454-499). Evidence: Gundobad page: the Burgundians invaded Liguria 'in the early months of 490' while Odoacer and Theoderic fought; identity years of kingdom-of-odoacer, ostrogoths, ostrogothic-kingdom. Fix: Belligerents set to burgundian-kingdom, kingdom-of-odoacer, ostrogoths.
- `/ledger/11-14, /keyframe_review/12/correction, /wars/6/zones` (for the author, not blocking). The 507-509 Provence region (Provence minus the 500 shape) includes Arles, which the Burgundians never took; visigothic-kingdom keeps Provence to 510. Evidence: Gundobad page: 'the Ostrogothic army arrived to relieve the Burgundian siege of Arles'; the Burgundians had 'lost all their conquered territories and hope of acquiring Arles and Avignon'. visigothic-kingdom /ledger/14 loses Provence to ostrogothic-kingdom only in 510; it has no 507 loss to the Burgundians. Fix: Subtract {place: Arles, km: 30} from the region in the four ledger events, the 507 keyframe correction and the war zone; list the 507 Provence loss for the visigothic-kingdom author.
- `/ledger/0-1` (for the author, not blocking). western-roman-empire models 413-436 as a vassalage (its /ledger/16 vassal_start and /ledger/23 vassal_end, counterpart burgundian-kingdom); this dossier has no vassal events. Evidence: This dossier's own 413 note: 'the Burgundians were accepted as Roman foederati'. Review eu-06-a raised the same point for burgundians. Fix: Add vassal_start 413 and vassal_end 436, counterpart western-roman-empire (Kingdom page), or agree a single model with eu-04.
- `/keyframe_review/2 and /ledger/8` (for the author, not blocking). The 443 keyframe (ok) already holds the land of the mid-470s campaign, so the 475 gain moves no cell; the ledger and keyframes disagree on when the Langres and Lugdunensis I land became Burgundian. Evidence: Kingdom page: by the mid-470s the Burgundians fought the Alemanni in the Langres-Besancon-Jura region, 'eventually incorporating much of Maxima Sequanorum and parts of Lugdunensis I'. The 443 shape holds about 60 cells west of 4.3 E (Nievre, Yonne, western Cote-d'Or), and the Sapaudia page already puts Franche-Comte inside Sapaudia. Fix: Either adjust the 443-469 keyframes to leave out the Lugdunensis I cells until 475 and make /ledger/8 their gain (counterpart western-roman-empire or nobody: kingdom-of-alamannia, founded 462 between Strasbourg and Augsburg, records no loss), or mark the 443 shape 'unverified: page budget' and drop Franche-Comte from the 475 region.

Gaps for a gap-filler:
- `/ledger/15`: Year and extent of Godomar II's recovery south of the Durance, and the Ostrogothic occupation of 523 (Tuluin) that it reversed (try https://en.wikipedia.org/wiki/Tuluin)
- `/identity/rulers`: No ruler for 437-456; the Kingdom page names Gundioc in the campaign of 456 (try https://en.wikipedia.org/wiki/Gundioc)
- `/ledger/1`: Holder of the Rhine land after about 436 (try https://en.wikipedia.org/wiki/Flavius_Aetius)

Spot checks: `/ledger/1` confirmed; `/ledger/2` confirmed (year); region wider than the page, confidence lowered; `/ledger/4` confirmed; `/ledger/7` confirmed ('later 460s', as the note says); `/ledger/9-10` confirmed; `/ledger/11` confirmed (year); region includes Arles, see fixes; `/ledger/15` confirmed as undated; region not on page; `/ledger/18` confirmed.

## kingdom-of-the-suebi: fix

Area: infobox none; Cliopatria largest/relevant shape 248,614 km2. No area on the page (map caption only: greatest extent c. 455); the dossier says so.

Findings:
- `/ledger/6/confidence` (applied by reviewer). The 441 gain of Seville and Baetica was confidence 3, but the Kingdom page doubts the hold of Baetica. Evidence: Kingdom of the Suebi page: 'It has been said, however, that the Suevi conquest of Baetica and Carthaginensis was limited to raids'; the Rechila page has Seville taken in 441. Fix: Confidence lowered to 2 and the quote added to the note.
- `/ledger/1/confidence` (applied by reviewer). The 411 gain was confidence 3, but the region also holds land south of the Douro that no page gives the Suebi. Evidence: Kingdom page: the Suebi shared Gallaecia with the Hasding Vandals, 'by lot'. The region (the 414 shape plus Pontevedra and La Coruna) has 77 of the shape's 197 cells south of 41.1 N, reaching 39.8 N in Roman Lusitania. Fix: Confidence lowered to 2 and the reason added to the note.
- `/identity/rulers/1-15/source` (applied by reviewer). 15 of 16 rulers cited no page. Evidence: The Kingdom of the Suebi page's list of rulers gives every name and year as in the dossier, from Rechila 438-448 to Malaric 585. Fix: Source set to https://en.wikipedia.org/wiki/Kingdom_of_the_Suebi for the 15 rulers.
- `/keyframe_review/7 and /ledger/9` (for the author, not blocking). The 458 correction removes the Lisbon cells (7 cells) that the 426, 439 and 441 keyframes (all ok) hold, but no ledger event loses them: /ledger/9 is minus(457, 458), and both Cliopatria shapes contain Lisbon. Evidence: Kingdom page: Lisbon was captured in 469, 'surrendered by its leader, Lusidio'. Gazetteer: intersect(Suebi 458, Lisboa) is 7 cells; intersect(Suebi 441, Lisboa) is 9. Fix: Either drop the Lisbon cells from the 426-457 keyframes (the page gives the Suebi Lisbon only in 469), or add a 458 loss of intersect(Suebi 457, Lisboa) at confidence 1.
- `/keyframe_review/8-10` (for the author, not blocking). The 469, 476 and 577 corrections keep Lisbon Suebian to 585, but visigothic-kingdom gains 'the west of the peninsula' in 469 and its 469-587 shapes hold 6 of the 7 Lisbon cells: two dossiers claim the same land for 117 years. Evidence: visigothic-kingdom /ledger/5 (469 gain, counterpart western-roman-empire) and keyframes 469 to 577; gazetteer: intersect(Visigothic Kingdom 480 or 570, Suebi 458, Lisboa) is 6 cells. The 476 note admits the page records no Suebi hold of Lisbon after 469, only no loss. Fix: Agree with the visigothic-kingdom author: either add a 476 loss of Lisbon (confidence 1) and drop it from the 476 and 577 corrections, as Cliopatria draws it, or ask visigothic-kingdom to subtract Lisbon for 469-585.
- `/ledger/13` (for the author, not blocking). The 576 tribute treaty is only a contest_end here; the dossier asks visigothic-kingdom to carry a vassal_start but has none itself. Evidence: Leovigild page: 'Miro rapidly agreeing to a treaty which included paying tribute, if but for a short period.' Fix: Add vassal_start 576, counterpart visigothic-kingdom (Leovigild page, confidence 2 or 3), and a vassal_end (confidence 1; 583 or the 585 dissolve).

Gaps for a gap-filler:
- `/ledger/3`: Any Suebi hold south of the Mondego before 439 (page: Heremigarius plundered Lusitania in 429) (try https://en.wikipedia.org/wiki/Heremigarius)
- `/keyframe_review/6`: Whether Baetica was held in 441-458 or only raided (the largest shape of the dossier, 248,614 km2) (try https://en.wikipedia.org/wiki/Rechiar)
- `/ledger (569-576)`: Leovigild's undated conquests of Sabaria, Braganza and Torre de Moncorvo; Braganza (41.8 N, 6.76 W) is inside the 476 shape, so this is a Suebi loss (try https://en.wikipedia.org/wiki/Miro_of_Galicia)
- `/identity/rulers`: Gap 469-550; the page lists Hermeneric fl. c. 485 and Veremund fl. 535 (try https://en.wikipedia.org/wiki/Kingdom_of_the_Suebi)
- `/identity/capitals`: Dates of the returns to Braga after Merida and after Lugo (try https://en.wikipedia.org/wiki/Braga)

Spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed (year); region not named, confidence lowered; `/ledger/2` confirmed; `/ledger/4` confirmed; `/ledger/6` confirmed (Seville 441); Baetica doubted on the Kingdom page, confidence lowered; `/ledger/7` confirmed (5 October, Braga 28 October); `/ledger/9` confirmed (July 458); `/ledger/11` confirmed; `/ledger/13` confirmed; `/ledger/14` confirmed.

## frankish-burgundy: thin

Area: infobox none; Cliopatria largest/relevant shape 583,653 km2. No Wikipedia article for this state; the Kingdom of Burgundy page has no infobox.

Findings:
- `/ledger/1/note, /ledger/1/region, /keyframe_review/1` (for the author, not blocking). The 595 note's quote is not the page's, and 'The other cities are not named' is wrong: the page names ten civitates, and the 595-599 keyframe adds only three. Evidence: Theuderic II page: 'He also received the lordship of the cities (civitates) of Toulouse, Agen, Nantes, Angers, Saintes, Angouleme,' then Perigueux, Blois, Chartres and Le Mans. Fix: Quote the sentence correctly and add Angers, Saintes, Angouleme, Perigueux, Blois, Chartres and Le Mans (60 km radii, like the others) to /ledger/1/region and the 595 correction, and to the nested copies in /ledger/2/region and /wars/0/zones.
- `/identity and /keyframe_review/6-8` (for the author, not blocking). From 639 the polity drawn is Neustria and Burgundy (Paris, Rouen, Soissons, Flanders, Artois), not Burgundy; the name and notes do not say so. Evidence: Francia page: 'Clovis II, Dagobert's successor in Neustria and Burgundy, which were thereafter attached yet ruled separately'. Cliopatria's Kingdom of the Franks for 644-660 is Austrasia only (132,986 km2). Fix: Say in identity notes (and alt_names) that 639-660 is the Neustro-Burgundian realm, and tell eu-07 that kingdom-of-the-franks then holds only Austrasia; or leave the choice to the orchestrator.
- `/ledger/2-6` (for the author, not blocking). The counterparts are kingdom-of-the-franks, but the page gives Chlothar II of Neustria (600) and Theudebert II of Austrasia (610-612), which the author lists as austrasia in counterparts_needing_dossiers. Evidence: Theuderic II page: 'In 610, he lost Alsace, the Saintois, the Thurgau, and Champagne to his brother'; Toul c. 611, Tolbiac 612. Fix: When eu-07 settles its slugs, use austrasia or neustria as counterparts.

Gaps for a gap-filler:
- `/ledger/9`: End of Burgundy as a separate realm (660 is only Cliopatria's last year, confidence 1) (try https://en.wikipedia.org/wiki/Kingdom_of_Burgundy)
- `/ledger/7-8`: Burgundy 614-638: the state has no land, ruler or capital; it kept its own mayor of the palace under Chlothar II (try https://en.wikipedia.org/wiki/Warnachar)
- `/identity/capitals`: Capital after 639 (none given); Metz for 612-613 ('his Austrasian capital of Metz') (try https://en.wikipedia.org/wiki/Neustria)

Spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed (year); quote and city list wrong, see fixes; `/ledger/2` confirmed; `/ledger/3` confirmed; `/ledger/5` confirmed; `/ledger/6` confirmed; `/ledger/7` confirmed (died late 613; Francia: Sigebert II heir in 613); `/ledger/8` confirmed.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| burgundian-kingdom 413 found (western-roman-empire) | western-roman-empire 413 vassal_start | mismatch | WRE /ledger/16 vassal_start of burgundian-kingdom 413 and /ledger/23 vassal_end 436; this dossier has no vassal events (non-blocking fix). |
| burgundian-kingdom 436 loss (western-roman-empire) | western-roman-empire 436 gain | matched | WRE /ledger/24. |
| burgundian-kingdom 443 gain (western-roman-empire) | western-roman-empire 443 loss | matched | WRE /ledger/30. |
| burgundian-kingdom 456 gain (western-roman-empire) | western-roman-empire 456 loss | matched | WRE /ledger/39. |
| burgundian-kingdom 458 loss (western-roman-empire) | western-roman-empire - none | missing | WRE has no 458/459 gain of Lyon from the Burgundians (its 459 gains name visigothic-kingdom). Route to eu-04. |
| burgundian-kingdom 462 gain (western-roman-empire) | western-roman-empire 462 loss | matched | WRE /ledger/48 (confidence 1). |
| burgundian-kingdom 475 gain (kingdom-of-alamannia) | kingdom-of-alamannia - none | missing | kingdom-of-alamannia has only 462 found and 496 loss; the event moves no cell here. Route to eu-06-e or change the counterpart. |
| burgundian-kingdom 507 gain (visigothic-kingdom) | visigothic-kingdom - none | mismatch | visigothic-kingdom keeps Provence until its /ledger/14 (510 loss to ostrogothic-kingdom). Route to eu-06-d. |
| burgundian-kingdom 509 loss (ostrogothic-kingdom) | ostrogothic-kingdom 510 gain | mismatch | ostrogothic-kingdom /ledger/3 gains Provence in 510 from visigothic-kingdom, not from the Burgundians. |
| burgundian-kingdom 524 gain (ostrogothic-kingdom) | ostrogothic-kingdom - none | missing | ostrogothic-kingdom holds Provence 510-540 and has no loss; region overlap is a blocking fix in burgundian-kingdom. |
| burgundian-kingdom 534 dissolve (kingdom-of-the-franks) | kingdom-of-the-franks - none | exception | kingdom-of-the-franks belongs to eu-07, not run yet. |
| kingdom-of-the-suebi 411 gain (western-roman-empire) | western-roman-empire - none | missing | WRE has no 409-411 loss of Gallaecia to the Suebi. Route to eu-04. |
| kingdom-of-the-suebi 419 gain (vandals) | vandals 419 loss | matched | vandals /ledger/10. |
| kingdom-of-the-suebi 427 gain (western-roman-empire) | western-roman-empire - none | missing | Confidence 1 raid; WRE silent. |
| kingdom-of-the-suebi 439 gain (western-roman-empire) | western-roman-empire - none | missing | WRE has no 439 loss of Merida to the Suebi. Route to eu-04. |
| kingdom-of-the-suebi 441 gain (western-roman-empire) | western-roman-empire - none | missing | WRE has no 441 loss of Seville/Baetica to the Suebi. Route to eu-04. |
| kingdom-of-the-suebi 458 loss (visigothic-kingdom) | visigothic-kingdom 456 gain | mismatch | visigothic-kingdom /ledger/2 gains the Spanish provinces in 456 from western-roman-empire, and /ledger/3 leaves Spain in 459; the Kingdom of the Suebi page dates the Gothic arrival in Baetica to July 458. Route to eu-06-d. |
| kingdom-of-the-suebi 469 gain (western-roman-empire) | western-roman-empire 469 loss | matched | WRE /ledger/53; but visigothic-kingdom /ledger/5 (469) and its shapes to 587 also hold 6 of the 7 Lisbon cells (double claim, non-blocking fix). |
| kingdom-of-the-suebi 569 contest_start (visigothic-kingdom) | visigothic-kingdom 569 gain | mismatch | visigothic-kingdom /ledger/20 gains Zamora, Palencia and Leon from the Suebi; the Suebi shape never reaches them, so a contest here (explained by the author). |
| kingdom-of-the-suebi 576 contest_end (visigothic-kingdom) | visigothic-kingdom - none | missing | The tribute treaty should be a vassal_start in both dossiers; neither has one. |
| kingdom-of-the-suebi 585 dissolve (visigothic-kingdom) | visigothic-kingdom 585 gain | matched | visigothic-kingdom /ledger/28. |
| frankish-burgundy 561 found (kingdom-of-the-franks) | kingdom-of-the-franks - none | exception | eu-07 not run; Cliopatria Kingdom of the Franks 561-601 also holds this land. |
| frankish-burgundy 595 gain (kingdom-of-the-franks) | kingdom-of-the-franks - none | exception | eu-07 not run. |
| frankish-burgundy 600 gain (kingdom-of-the-franks) | kingdom-of-the-franks - none | exception | eu-07 not run; the page counterpart is Chlothar II (Neustria). |
| frankish-burgundy 610 loss (kingdom-of-the-franks) | kingdom-of-the-franks - none | exception | eu-07 not run; page counterpart is Theudebert II of Austrasia (suggested slug austrasia). |
| frankish-burgundy 612 gain (kingdom-of-the-franks) | kingdom-of-the-franks - none | exception | eu-07 not run; Austrasia. |
| frankish-burgundy 613 loss (kingdom-of-the-franks) | kingdom-of-the-franks - none | exception | eu-07 not run. |
| frankish-burgundy 639 gain (kingdom-of-the-franks) | kingdom-of-the-franks - none | exception | eu-07 not run; Cliopatria Kingdom of the Franks 617-643 holds the same land. |
| frankish-burgundy 660 dissolve (kingdom-of-the-franks) | kingdom-of-the-franks - none | exception | eu-07 not run. |

## Problems

- None of the three articles gives an infobox area (frankish-burgundy has no article), so no area ratio could be computed.
- The author's counterparts_needing_dossiers names odoacers-kingdom-of-italy, but history/polities/kingdom-of-odoacer.json already exists (476-493); the reviewer used that slug in burgundian-kingdom /wars/4.
- hunnic-empire was not written: confirmed that huns.json lists both 'Huns' and 'Hunnic Empire' and reviews 12 hunnic-empire shapes, so drop hunnic-empire from the dossier list.
- frankish-burgundy and kingdom-of-the-franks (eu-07, not written) draw the same land for 561-601 and 617-643 in Cliopatria; eu-07 must subtract Burgundy (and Neustria for 639-660) or the orchestrator must choose.
