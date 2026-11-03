# Review of batch eu-09-f: swiss-confederation

Reviewed 2026-10-25 against history/briefs/reviewer-brief.md. Validator: valid, 0 errors, 9 warnings (all counterparts listed in counterparts_needing_dossiers: three-leagues, sieben-zenden, republic-of-geneva).

## Verdict: fail

Three blocking findings stay with the author (keyframe 1564-1571, the pre-1481 Solothurn and Fribourg cells, the 1803-1814 Mediation land). The reviewer applied two counterpart corrections (/ledger/7 and /ledger/13 to house-of-habsburg), re-validated, and read the file back.

What held: 26 events checked on their pages; every confidence-3 event checked says what its note claims, with the year (1291, 1351-1353, 1415, 1426, 1440, 1460, 1500, 1501, 1512, 1513, September 1515, November 1516, February 1526, 1536, 1564, March and April 1798, February 1803, May 1815, March 1848). The infobox area matches (41,291 against 40,677 km2, ratio 1.015, acknowledged). The family, slug, Cliopatria row and 59 verdicts plus 2 new keyframes check out.

## Findings

### /keyframe_review/27/correction (blocking)

- What: The correction for Cliopatria's 1564 shape (valid 1564-1571) keeps the Savoyard lands of the Genevan basin (Haute-Savoie and Ain cells, about 2,300 km2), but /ledger/31 loses them to house-of-savoy in 1564; the keyframe contradicts the ledger for 1564-1571.
- Why: Republic_of_Geneva page: 'only in the Treaty of Lausanne of 1564 did Savoy recover the lands around Geneva, while losing forever the Pays de Vaud to Bern.' The keyframe's own note says Bern holds them 'until the Treaty of Lausanne of 1564', yet the shape keeps them to 1571 (Cliopatria drops them in 1572). Brief 2.4: a correction must agree with the ledger.
- Fix: Add the Genevan-basin intersect used in /ledger/31 ({intersect: [{cliopatria: Swiss Confederation, year: 1540}, {union: [Haute-Savoie, Ain]}]}) to the minus-union of keyframe 27's correction and say in text that Savoy recovered the lands around Geneva by the Treaty of Lausanne of 1564 (or, if the handover is to be dated later, add a new keyframe swiss-confederation_1565 for 1565-1571 without them, as was done for 1353).

### /keyframe_review/6 to /keyframe_review/13 (verdicts) (blocking)

- What: Verdict ok on the 1363-1475 shapes, which by the author's own notes already hold Solothurn (from 1363) and Fribourg (from 1459), while /ledger/17 gains Fribourg and Solothurn only in 1481 at confidence 3; the land is shown Swiss 18 to 118 years before the ledger's gain and the 1363 and 1459 increases are unexplained for those cells.
- Why: History_of_Switzerland accession list: '1481 - Fribourg, Solothurn'. Keyframe 6 note: '21 new cells (Bern, Lucerne, Obwalden, Solothurn)'; keyframe 11 note: '... plus Fribourg and more of Bern'. Rule 4 (associations are not territory) is applied to Valais, Graubunden and Geneva but silently not to these two Bernese allies.
- Fix: Mark keyframes 6-13 adjust with corrections {minus: [{cliopatria: Swiss Confederation, year: Y}, {admin1: Solothurn}]} for 1363-1458 and minus Solothurn and Fribourg for 1459-1475 (keep any Bernese bailiwick cells), text quoting the 1481 accession; or explain in each note why those cells are Swiss before 1481 and lower /ledger/17 accordingly.

### /ledger/38 and /ledger/40 (blocking)

- What: The dossier keeps the state alive but landless 1798-1815 and places a rename at 19 February 1803 (Act of Mediation) while leaving the 1803-1814 land with helvetic-republic, a state the cited page says was abolished that day; the August 1815 gain 'from helvetic-republic' is from a state that had not existed for twelve years.
- Why: Helvetic_Republic page: 'On 19 February 1803, the Act of Mediation abolished the Helvetic Republic and restored the cantons.' Cliopatria's Helvetic Republic row has Mediation-era shapes helvetic-republic_1803 (1803-1805, 34,675 km2), _1806, _1811 and _1814. The author flagged the seam (notes, problems) but left the decision to eu-20.
- Fix: Add a gain from helvetic-republic dated 1803-02 (source Helvetic_Republic, the sentence above) with region {cliopatria: Helvetic Republic, year: 1803} (minus any Valais, Geneva, Jura or Neuchatel cells, which were not in the Mediation), add new keyframes swiss-confederation_1803/_1806/_1811/_1814 from those shapes, and turn /ledger/40 into the 1814-15 gains of Valais, Neuchatel, Geneva and the Jura from their actual holders; tell eu-20 that helvetic-republic ends 19 February 1803. If the orchestrator instead rules that 1803-1814 stays with helvetic-republic, delete the landless 1803 rename and say so in notes.

### /ledger/7/counterpart - applied by reviewer

- What: Counterpart was holy-roman-empire-minor-states; the Aargau was taken from the Habsburg dukes and house-of-habsburg's dossier already carries the 1415 loss to swiss-confederation.
- Why: Old_Swiss_Confederacy page: 'In both cases, the Swiss profited from weakness in the Habsburg dukes' (Aargau 1415, Thurgau 1460); house-of-habsburg /ledger/13: 1415 loss, counterpart swiss-confederation.
- Fix: Counterpart set to house-of-habsburg and the sentence added to the note (reviewer edit, validated).

### /ledger/13/counterpart - applied by reviewer

- What: Counterpart was holy-roman-empire-minor-states; the Thurgau was taken from the Habsburgs and house-of-habsburg already carries the 1460 loss.
- Why: Old_Swiss_Confederacy page, same sentence; house-of-habsburg /ledger/20: 1460 loss, counterpart swiss-confederation.
- Fix: Counterpart set to house-of-habsburg and the sentence added to the note (reviewer edit, validated). The author's notes still list Aargau 1415 and Thurgau 1460 among the HRE minor states' loss sides; drop them there.

### /ledger/42/region

- What: The 1816 gain from kingdom-of-sardinia names the whole canton of Geneva (admin1 Geneve), which hands the Sardinia dossier a loss of the whole canton; only the Savoyard parishes came from Sardinia, and the six French parishes came from France.
- Why: Republic_of_Geneva page: 'Geneva's territory was extended to cover fifteen Savoyard and six French parishes'; the Treaty of Turin (16 March 1816) is the Savoyard cession. The 1815 keyframe already adds the full modern canton, a year early for these parishes.
- Fix: Narrow the region to the Savoyard communes south and east of the city (e.g. a coordinate radius on Carouge, about 46.18 N 6.14 E, 8 km, clipped to Geneve) with text 'fifteen Savoyard parishes'; record the six French parishes (Versoix area) as a gain from bourbon-kingdom-of-france in 1815, or say in the note that they are inside the 1815 Geneva gain.

### /ledger/43 and /keyframe_review/43

- What: Neuchatel is left outside the Confederation 1815-1847 although the dossier's own 1815 note quotes 'Valais, Neuchatel, and Geneva also joined Switzerland as new cantons' and Geneva is added on that ground; the treatment of the two new cantons is inconsistent.
- Why: Principality_of_Neuchatel page: 'on 12 September 1814 obtained the Swiss Federal Diet's acceptance of Neuchatel as the twenty-first canton'; History_of_Switzerland: Valais, Neuchatel and Geneva 'joined Switzerland as new cantons'.
- Fix: Either add Neuchatel to the 1815-1847 correction (canton of the Confederation, Prussian prince) and make the 1848 event a rename/caption with no land, or keep it out and say in keyframe 43's note why a member canton is drawn as Prussian; kingdom-of-prussia (eu-09) must mirror whichever is chosen.

### /ledger/8/region

- What: The 1416 associate tint covers the whole canton of Valais, but the Sieben Zenden held only the upper Valais until November 1475; the lower Valais was Savoyard 1416-1475.
- Why: The event's own note: 'the whole canton area is the associate from 1475' (Burgundian Wars page, Battle on the Planta); Old_Swiss_Confederacy: the Sieben Zenden 'Became a Zugewandter Ort in 1416'.
- Fix: Region for 1416: Valais minus the lower Valais below the Morge (coordinate radius on Saint-Maurice/Martigny until a gazetteer 'Upper Valais' exists); add a 1475 event extending the tint to the lower Valais (counterpart county-of-savoy).

### /ledger/20/counterpart and /ledger/27/counterpart

- What: Bellinzona (1500) is gained from duchy-of-milan and the Ossola (November 1516) lost to duchy-of-milan, but kingdom-of-france holds the duchy of Milan from 6 October 1499 to 1512 and again from September 1515.
- Why: kingdom-of-france /ledger/76 (1499 gain of Lombardy), /ledger/79 (1512 loss), /ledger/80 (1515 gain); Battle_of_Marignano page: 'Only the Ossola valley was passed back to Milan' after Francis I took Milan.
- Fix: Use kingdom-of-france as counterpart for both (consistent with the dossier's own 1512 gains from France), or explain in the notes why duchy-of-milan is kept; the France dossier (eu-10) then needs the matching loss 1500 and gain 1516.

### /ledger/6, /ledger/12, /ledger/21 (counterpart)

- What: Counterparts 'Appenzell', 'Schaffhausen' and 'Basel' are neither slugs nor listed in counterparts_needing_dossiers, so nothing will carry the other side.
- Why: Brief 2.3: a counterpart without a dossier must be listed in counterparts_needing_dossiers; the report lists only three-leagues, sieben-zenden, republic-of-geneva, the Abbey of St. Gall and Neuchatel.
- Fix: Point them to holy-roman-empire-minor-states (Cliopatria's holder of those cells) or list Appenzell, Schaffhausen and the city of Basel under counterparts_needing_dossiers.

## Thin (for a gap-filler)

- /ledger/5: 1395 cells near Aarau, Biel/Bienne and the Jura foot, confidence 1 (page silent); likely Sempach-war and Bernese acquisitions of 1386-1394. Page to try: https://en.wikipedia.org/wiki/Battle_of_Sempach
- /ledger/19: Blenio entering the shape in 1497, confidence 1; the Ticino page names no Blenio conquest. Page to try: https://en.wikipedia.org/wiki/Blenio_District
- /ledger/23: Ossola taken by the Swiss in 1512, confidence 1. Page to try: https://en.wikipedia.org/wiki/Ossola
- /ledger/32 and /identity/capitals/1: Diet seat 1712-1798 given as Zurich at confidence 1; the Diet is usually placed at Frauenfeld after 1712 (none of the opened pages says so; Old_Swiss_Confederacy says only that Zurich held the chair and Baden was the seat); 1815-1847 has no capital (rotating Vorort Zurich-Bern-Lucerne). Page to try: https://en.wikipedia.org/wiki/Frauenfeld
- /ledger/35: End of the Valais association in 1798, confidence 1 (Helvetic_Republic page silent on the Valais). Page to try: https://en.wikipedia.org/wiki/Canton_of_Valais
- /ledger/24 and /ledger/33: The Valtellina tint runs 1512-1797 without a break; History_of_Switzerland says the Leagues lost the Valtellina in 1623 and it became their dependency again only after a later treaty, so a vassal_end 1623 (or 1620) and a vassal_start at the recovery are missing. Page to try: https://en.wikipedia.org/wiki/Valtellina
- /keyframe_review/14, 15, 16, 21, 22, 23: Undated cell changes of 1482, 1487, 1492, 1519, 1526 and 1529 (Sargans, Rheintal, Werdenberg, Jura, Tyrol/Vorarlberg fringe) kept as drawn: unverified, page budget. Page to try: https://en.wikipedia.org/wiki/Canton_of_St._Gallen
- /ledger/30: Chablais, Ternier and Gaillard cells of the 1536-1564 Bernese occupation rest on the author's reading of Cliopatria; the page names only the Pays de Gex. Page to try: https://en.wikipedia.org/wiki/Chablais

## Spot checks

- /ledger/0: confirmed (https://en.wikipedia.org/wiki/History_of_Switzerland)
- /ledger/2: confirmed (https://en.wikipedia.org/wiki/History_of_Switzerland)
- /ledger/3: confirmed (https://en.wikipedia.org/wiki/History_of_Switzerland)
- /ledger/4: confirmed (https://en.wikipedia.org/wiki/History_of_Switzerland)
- /ledger/7: confirmed (https://en.wikipedia.org/wiki/Baden,_Switzerland)
- /ledger/9: confirmed (https://en.wikipedia.org/wiki/Baden,_Switzerland)
- /ledger/10: confirmed (https://en.wikipedia.org/wiki/Ticino)
- /ledger/13: confirmed (https://en.wikipedia.org/wiki/Old_Swiss_Confederacy)
- /ledger/19: not on page (confidence 1; the note says page silent) (https://en.wikipedia.org/wiki/Ticino)
- /ledger/20: confirmed (https://en.wikipedia.org/wiki/Ticino)
- /ledger/21: confirmed (https://en.wikipedia.org/wiki/History_of_Switzerland)
- /ledger/22: confirmed (https://en.wikipedia.org/wiki/Ticino)
- /ledger/25: confirmed (https://en.wikipedia.org/wiki/Battle_of_Marignano)
- /ledger/26: confirmed (https://en.wikipedia.org/wiki/Battle_of_Marignano)
- /ledger/27: confirmed (https://en.wikipedia.org/wiki/Battle_of_Marignano)
- /ledger/28: confirmed (https://en.wikipedia.org/wiki/Republic_of_Geneva)
- /ledger/29: confirmed (https://en.wikipedia.org/wiki/Old_Swiss_Confederacy)
- /ledger/31: confirmed (https://en.wikipedia.org/wiki/Republic_of_Geneva)
- /ledger/32: not on page (confidence 1; the page gives no seat or year) (https://en.wikipedia.org/wiki/Tagsatzung)
- /ledger/34: confirmed (https://en.wikipedia.org/wiki/Helvetic_Republic)
- /ledger/37: confirmed (https://en.wikipedia.org/wiki/Republic_of_Geneva)
- /ledger/38: confirmed (https://en.wikipedia.org/wiki/Helvetic_Republic)
- /ledger/39: confirmed (https://en.wikipedia.org/wiki/Republic_of_Geneva)
- /ledger/40: confirmed (https://en.wikipedia.org/wiki/History_of_Switzerland)
- /ledger/42: confirmed (https://en.wikipedia.org/wiki/Republic_of_Geneva)
- /ledger/43: confirmed (https://en.wikipedia.org/wiki/Principality_of_Neuch%C3%A2tel)

## Area

- Infobox 41291 km2 (no year) against Cliopatria 40677 km2 (1950-2024): ratio 1.015, acknowledged in keyframe 59.

## Cross-dossier matrix

- 1332 gain <- holy-roman-empire-minor-states: exception. Lucerne: holy-roman-empire-minor-states (eu-09) has no dossier yet; the loss side is owed there.
- 1351 gain <- holy-roman-empire-minor-states: exception. Zurich: holy-roman-empire-minor-states (eu-09) has no dossier yet; the loss side is owed there.
- 1352 gain <- holy-roman-empire-minor-states: exception. Glarus, Zug: holy-roman-empire-minor-states (eu-09) has no dossier yet; the loss side is owed there.
- 1353 gain <- holy-roman-empire-minor-states: exception. Bern: holy-roman-empire-minor-states (eu-09) has no dossier yet; the loss side is owed there.
- 1395 gain <- holy-roman-empire-minor-states: exception. border cells: holy-roman-empire-minor-states (eu-09) has no dossier yet; the loss side is owed there.
- 1481 gain <- holy-roman-empire-minor-states: exception. Fribourg, Solothurn: holy-roman-empire-minor-states (eu-09) has no dossier yet; the loss side is owed there.
- 1411 gain <- Appenzell: missing. Counterpart is free text and not in counterparts_needing_dossiers.
- 1415 gain <- house-of-habsburg: matched (mirror house-of-habsburg 1415 loss). Counterpart corrected by the reviewer from holy-roman-empire-minor-states; house-of-habsburg /ledger/13.
- 1416 vassal_start <- sieben-zenden: exception. Listed in counterparts_needing_dossiers (eu-09-x).
- 1440 gain <- duchy-of-milan: exception. duchy-of-milan (eu-13) not written yet.
- 1454 gain <- Imperial Abbey of St. Gall: exception. Listed in counterparts_needing_dossiers as imperial-abbey-of-st-gall.
- 1454 gain <- Schaffhausen: missing. Counterpart is free text and not in counterparts_needing_dossiers.
- 1460 gain <- house-of-habsburg: matched (mirror house-of-habsburg 1460 loss). Counterpart corrected by the reviewer; house-of-habsburg /ledger/20 (confidence 2).
- 1476 gain <- county-of-savoy: exception. county-of-savoy (eu-13) not written yet; Grandson and Echallens were Chalon (Burgundian) lordships, so duchy-of-burgundy (eu-10) may be the truer counterpart.
- 1497 vassal_start <- three-leagues: exception. Listed in counterparts_needing_dossiers (eu-09-x).
- 1497 gain <- duchy-of-milan: exception. Blenio; duchy-of-milan (eu-13) not written yet.
- 1500 gain <- duchy-of-milan: exception. duchy-of-milan not written yet, but kingdom-of-france holds Milan from 6 October 1499 (its /ledger/76); counterpart should probably be kingdom-of-france.
- 1501 gain <- Basel: missing. Counterpart is free text and not in counterparts_needing_dossiers.
- 1512 gain <- kingdom-of-france: mismatch (mirror kingdom-of-france 1512 loss). France /ledger/79 loses Lombardy to duchy-of-milan in 1512; it has no loss of the Ticino bailiwicks to swiss-confederation (route to eu-10).
- 1512 gain <- kingdom-of-france: mismatch (mirror kingdom-of-france 1512 loss). Ossola: same as above; France has no loss of the Ossola to the Swiss.
- 1512 vassal_start <- three-leagues: exception. Valtellina; three-leagues listed in counterparts_needing_dossiers.
- 1513 vassal_start <- duchy-of-milan: exception. duchy-of-milan (eu-13) not written yet; consistent with France /ledger/79.
- 1515 vassal_end <- duchy-of-milan: exception. duchy-of-milan not written yet; consistent with France /ledger/80 (gain of Milan, September 1515).
- 1516 loss <- duchy-of-milan: exception. duchy-of-milan not written yet, but Milan is French from September 1515 per kingdom-of-france /ledger/80; counterpart should probably be kingdom-of-france, which then needs a 1516 gain of the Ossola.
- 1526 vassal_start <- republic-of-geneva: exception. Listed in counterparts_needing_dossiers (eu-09-x).
- 1536 gain <- county-of-savoy: exception. Vaud; county-of-savoy (eu-13) not written yet.
- 1536 gain <- county-of-savoy: exception. Genevan basin and Pays de Gex; county-of-savoy not written yet.
- 1564 loss <- house-of-savoy: exception. house-of-savoy (eu-13) not written yet; Cliopatria house-of-savoy row starts 1564.
- 1797 vassal_end <- three-leagues: exception. Listed in counterparts_needing_dossiers.
- 1798 loss <- helvetic-republic: exception. helvetic-republic (eu-20) not written yet; its Cliopatria row starts 1799 and must start 1798 to own the land.
- 1798 vassal_end <- sieben-zenden: exception. Listed in counterparts_needing_dossiers.
- 1798 vassal_end <- three-leagues: exception. Listed in counterparts_needing_dossiers.
- 1798 vassal_end <- republic-of-geneva: exception. Listed in counterparts_needing_dossiers.
- 1815 gain <- republic-of-geneva: exception. Listed in counterparts_needing_dossiers.
- 1815 gain <- helvetic-republic: exception. helvetic-republic (eu-20) not written yet; the Helvetic Republic was abolished on 19 February 1803, so the 1803-1814 land should pass to this dossier in 1803 (see fixes).
- 1816 gain <- kingdom-of-sardinia: exception. kingdom-of-sardinia (eu-13) not written yet; region overclaims the whole canton (see fixes).
- 1848 gain <- kingdom-of-prussia: exception. kingdom-of-prussia (eu-09) not written yet; Neuchatel was a canton from 1814 (see fixes).

## Gazetteer names needed

Grandson, Echallens, Airolo, Leventina, Blenio, Valtellina, Chiavenna, Bormio, Ossola, Toggenburg, Chablais, Pays de Gex, Upper Valais

## Problems

- Of the 40 context polities in the author's brief only kingdom-of-france, house-of-habsburg and united-states-of-america have dossiers; all other counterparts (holy-roman-empire-minor-states, duchy-of-milan, county-of-savoy, house-of-savoy, kingdom-of-sardinia, kingdom-of-prussia, helvetic-republic) belong to groups that have not run, so their mirrors are exceptions, not mismatches.
- Reviewer applied two counterpart edits to history/polities/swiss-confederation.json (/ledger/7 and /ledger/13 -> house-of-habsburg); the file re-validated (0 errors, the same 9 warnings) and the edit was read back after 10 s.
- Seam for the orchestrator: helvetic-republic (eu-20) must run 12 April 1798 to 19 February 1803 for this dossier's 1798 loss and the proposed 1803 gain to meet; Cliopatria's helvetic-republic_1803/_1806/_1811/_1814 shapes are Mediation-era Swiss Confederation land.
- WebFetch returns model summaries, so quotations were checked by asking for exact sentences; Republic_of_Geneva first returned 'In 1525 they secured an alliance' and only on a second, targeted request the February 1526 ratification sentence the note quotes.
