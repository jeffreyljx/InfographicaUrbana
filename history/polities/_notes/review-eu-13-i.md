# Review of batch eu-13-i (Italy, part i)

Reviewed 2026-10-25 by the adversarial reviewer. Inputs: the five dossiers, the author's report and notes, and the existing neighbour dossiers (holy-roman-empire-minor-states, papal-states, house-of-habsburg, duchy-of-styria, crown-of-aragon, kingdom-of-france, republic-of-pisa, kingdom-of-spain, county-of-savoy, swiss-confederation, ottoman-empire, kingdom-of-sicily, despotate-of-epirus, byzantine-empire, principality-of-achaea, habsburg-monarchy, despotate-of-arta, duchy-of-bavaria; plus march-of-verona). republic-of-venice, republic-of-genoa, kingdom-of-hungary, iberian-union and kingdom-of-bohemia have no dossier yet (groups not run): events against them are exceptions.

Mechanical check: validate_dossier.py --resolve passes all five with 0 errors (warnings: unseeded slugs second-republic-of-pisa, republic-of-siena, lordship-of-milan, all listed by the author; gazetteer lacks Crema). Re-validated after the reviewer's edits: still 0 errors.

Verdicts: patriarchate-of-aquileia **fix**, republic-of-florence **fix**, kingdom-of-naples **fix**, duchy-of-milan **fail**, ambrosian-republic **fix**. 'fix' here means fixed in place by the reviewer; duchy-of-milan goes back to the author.

## patriarchate-of-aquileia: fix

Area: Neither Patria del Friuli nor Patriarchate of Aquileia gives an infobox area; the dossier says so.

Findings:
- `/identity/predecessors/0/slug and /ledger/0/counterpart` (applied by reviewer): Predecessor and found counterpart was kingdom-of-italy, which is the 1861-1946 Kingdom of Italy dossier. Evidence: Patria del Friuli page: Otto I added the Friulian territory to the March of Verona in 952 and after the 3 April 1077 grant 'the remaining parts of the March of Verona' went to Liutold of Eppenstein; march-of-verona /ledger/6 records a 1077 loss with counterpart patriarchate-of-aquileia. Fix: slug and counterpart changed to march-of-verona; predecessor note rewritten to say so.

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Patria_del_Friuli: confirmed: 'On 3 April 1077 at Pavia Henry ... vested Aquileian Patriarch Sieghard of Beilstein with immediate comital rights in the Friulian lands'
- `/ledger/1` https://en.wikipedia.org/wiki/March_of_Istria: confirmed: 'Aquileia regained Istria in 1209, when the Andechs margraves were banned' (also on Patria del Friuli: 'from the Dukes of Merania in 1209')
- `/ledger/5` https://en.wikipedia.org/wiki/Patria_del_Friuli: confirmed: 'On 23 July 1419 the Venetians conquered Cividale'
- `/ledger/7, /ledger/10` https://en.wikipedia.org/wiki/Patria_del_Friuli: confirmed: 'Udine fell to Venetians on 7 June 1420'; 'temporal authority of the patriarch was lost on 7 July 1420'
- `/ledger/3, /ledger/6` https://en.wikipedia.org/wiki/Patria_del_Friuli: confirmed: 1291 peace at Treviso, western Istrian coast to Venice; 'Muggia, Labin and Plomin, surrendered to Venice in 1420'

Gaps for a gap-filler (not faults; within the page budget):
- `/keyframe_review/5..8`: Cliopatria's edge changes of 1314, 1344, 1363 and 1385 (100-900 km2: Carnic cell, the Livenza cells near Oderzo) have no events; the 1260s-1390s wars with Gorizia, Treviso and Padua are not covered (3 of 5 pages used). Try https://en.wikipedia.org/wiki/County_of_Gorizia
- `/keyframe_review/2`: Cliopatria's 1260 outline includes Gorizia and Pordenone; the County of Gorizia and the Habsburg Pordenone enclave were separate lordships, so the ok verdict rests on an undrawn boundary. Try https://en.wikipedia.org/wiki/Pordenone
- `/identity/capitals`: The Patria del Friuli infobox lists the capitals as 'Aquileia; Cividale; Udine'; Cividale has no dated span in the dossier. Try https://en.wikipedia.org/wiki/Cividale_del_Friuli
- `/keyframe_review/12..13`: Who held the six Soca-valley cells 1422-1449 (Venice, Gorizia or a patriarchal residue). Try https://en.wikipedia.org/wiki/Tolmin

## republic-of-florence: fix

Area: Republic of Florence has no infobox area; the Grand Duchy of Tuscany figure (1852) against the 1734 shape, quoted correctly in /keyframe_review/13.

Findings:
- `/ledger/7` (applied by reviewer): The 1509 recovery of Pisa was at confidence 1 with the note 'Page silent', but the cited page dates it. Evidence: Republic of Florence page: 'the Secretary of War, Niccolò Machiavelli, recaptured Pisa in 1509', Pisa having 'been de facto independent since Charles VIII's invasion'. Fix: confidence 1 -> 3; note replaced with the quote.

Spot checks:
- `/ledger/4` https://en.wikipedia.org/wiki/Republic_of_Florence: confirmed: 'the army under Maso degli Albizzi took Pisa on 9 October 1406 after a long siege'
- `/ledger/5` https://en.wikipedia.org/wiki/Livorno: confirmed: 'on 28 August 1421 it was bought by the Republic of Florence'
- `/ledger/9` https://en.wikipedia.org/wiki/Grand_Duchy_of_Tuscany: confirmed as the page words it: 'Florence purchased the island of Elba from the Republic of Genoa (in 1548)' (counterpart doubtful, see thin)
- `/ledger/11, /ledger/13` https://en.wikipedia.org/wiki/Republic_of_Florence: confirmed: 'On 17 April 1555, Florence and Spain occupied the territory of Siena'; 'in July 1557 Philip II of Spain bestowed on Cosimo as a hereditary fiefdom'
- `/ledger/7` https://en.wikipedia.org/wiki/Republic_of_Florence: on page although the note said page silent: 'Niccolò Machiavelli, recaptured Pisa in 1509' (fixed)
- `/ledger/1, /ledger/2` https://en.wikipedia.org/wiki/Republic_of_Florence: confirmed: succession table '1254: Commune of Pistoia', '1361: Lordship of Volterra'

Gaps for a gap-filler (not faults; within the page budget):
- `/keyframe_review/0`: Extent of the commune 1115-1259 (a 25 km disc stands in); Montaperti 1260 and Campaldino 1289. Try https://en.wikipedia.org/wiki/Battle_of_Montaperti
- `/ledger (1254-1406)`: Acquisitions inside Cliopatria's constant 1260-1401 outline: Prato (1351), San Gimignano (1353), Colle, Montepulciano, Cortona (1411), the Casentino (Poppi 1440), Pietrasanta and Sarzana (1484-1494, 1513). Try https://en.wikipedia.org/wiki/Cortona
- `/ledger/9`: The Grand Duchy page says Elba was bought 'from the Republic of Genoa (in 1548)'; the usual account is that Cosimo received only Portoferraio, from Charles V and the Appiani of Piombino, while the rest of Elba stayed with Piombino and Spain. A gap-filler should confirm the counterpart and shrink the 15 km disc to Portoferraio if so. Try https://en.wikipedia.org/wiki/Portoferraio
- `/ledger/6`: The 30 km Pisa disc of 1494-1509 also covers Livorno, which was given up with Pisa in 1494 but back in Florentine hands from about 1495-1496; no page opened dates it. Try https://en.wikipedia.org/wiki/Livorno

## kingdom-of-naples: fix

Area: Kingdom of Naples infobox has population only, no area; the dossier says so.

Findings:
- `/ledger/4, /ledger/5` (applied by reviewer): Charles VIII's hold on the kingdom (February-July 1495) was typed contest_start/contest_end, while kingdom-of-france records it as an occupation of this kingdom. Evidence: Italian War of 1494-1495 page: 'On February 22, King Charles occupied Naples without a fight'; Neapolitan recapture of Naples 6-7 July 1495. kingdom-of-france /ledger/72-73: occupation_start 1495 and occupation_end 1495-09 with counterpart kingdom-of-naples. Fix: types changed to occupation_start and occupation_end (same years, months, region and counterpart); notes say why.

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Kingdom_of_Naples: confirmed: infobox 'Sovereign state (1282-1442; 1458-1501 ...)'; 'Charles, however, maintained his possessions on the mainland'
- `/ledger/2` https://en.wikipedia.org/wiki/Kingdom_of_Naples: confirmed: 'Part of the Crown of Aragon (1442-1458)'; 'Alfonso V conquered the Kingdom of Naples'
- `/ledger/3` https://en.wikipedia.org/wiki/Kingdom_of_Naples: confirmed: 'At his death in 1458 ... Naples was inherited by Ferdinand I'
- `/ledger/7` https://en.wikipedia.org/wiki/Treaty_of_Granada_(1500): confirmed: Louis to receive 'the northern regions' (Abruzzo, Terra di Lavoro, Naples); 'in August Frederick surrendered Naples to the French'
- `/ledger/4, /ledger/5` https://en.wikipedia.org/wiki/Italian_War_of_1494–1495: confirmed: 22 February 1495 and 6-7 July 1495 (type corrected)

Gaps for a gap-filler (not faults; within the page budget):
- `/ledger (1282-1302)`: The Vespers war on the mainland: kingdom-of-sicily records Messina taken from Naples (1282-10), Malta (1283), a contest in Calabria (1283-02 to 1302-08) and Reggio (1313-1317); Naples has none of these. Try https://en.wikipedia.org/wiki/War_of_the_Sicilian_Vespers
- `/ledger (1435-1442)`: The War of the Neapolitan Succession: crown-of-aragon has contest_start 1441-11 and contest_end 1442-06 with this kingdom; Naples has only the 1442 loss. Try https://en.wikipedia.org/wiki/Alfonso_V_of_Aragon
- `/ledger (1400-1500)`: Ladislaus's occupation of Rome and the papal lands (1408-1414); the Angevin war of 1458-1462; the Ottoman occupation of Otranto (August 1480 to September 1481), which ottoman-empire also lacks. Try https://en.wikipedia.org/wiki/Ottoman_invasion_of_Otranto
- `/identity`: Angevin overseas holdings and suzerainties (Corfu to 1386, the Kingdom of Albania, suzerainty over Achaea) have no vassal events; the 1-2 page budget explains it. Try https://en.wikipedia.org/wiki/Kingdom_of_Albania_(medieval)

## duchy-of-milan: fail

Area: Duchy of Milan infobox has a 1600 population only, no area; the dossier's source note says so.

Findings:
- `/ledger/17, /ledger/18, /ledger/21` (NOT applied, author to do): Losses of Ticino (1515), the Valtellina (1515) and Parma-Piacenza (1521) are of land the duchy did not hold: the 1512 gain (/ledger/16) and the 1521 gain (/ledger/20) are both of the 1526 outline, which their own region text says is 'without Parma and Piacenza, the Valtellina and Ticino', and the 1499 loss (/ledger/15) already gave the whole 1497 outline to France. Evidence: swiss-confederation /ledger/21 (Bellinzona 1500, from kingdom-of-france), /ledger/23 (Locarno, Lugano, Mendrisio 1512, from kingdom-of-france), /ledger/25 (Valtellina to the Three Leagues 1512); papal-states /ledger/22 (Parma and Piacenza to the pope, May 1512). Duchy of Milan page ties the Swiss retention to Marignano, i.e. after the land had already passed. These lands left the Milanese state while it was French (1499-1512). Fix: Delete /ledger/17, /ledger/18 and /ledger/21 and say in /ledger/16's note that Ticino, the Valtellina and Parma-Piacenza left the Milanese state under French rule (1500-1512) and are recorded in the Swiss and papal dossiers.
- `/ledger (1512-1515)` (NOT applied, author to do): No vassal_start/vassal_end for the Swiss protectorate over Maximilian Sforza's duchy, although /ledger/16's note says the Swiss cantons 'de facto controlled the duchy' until 1515. Evidence: swiss-confederation /ledger/26 vassal_start 1513 and /ledger/27 vassal_end 1515-09 with counterpart duchy-of-milan (Battle of Marignano page: 'to make Milan a protectorate of Switzerland'). Fix: Add vassal_start (1512-12 or 1513, counterpart swiss-confederation, region the 1526 outline, source War_of_the_League_of_Cambrai or Battle_of_Marignano) and vassal_end 1515-09.
- `/ledger (1439-1441)` (NOT applied, author to do): No loss of the Leventina valley to Uri. Evidence: swiss-confederation /ledger/10: 'Uri conquered the Leventina Valley in 1440' (Ticino page, confidence 3), counterpart duchy-of-milan. Fix: Add a 1440 loss, counterpart swiss-confederation, region the Leventina (upper Ticino valley), sourced to https://en.wikipedia.org/wiki/Ticino.
- `/ledger/1, /ledger/2, /keyframe_review/1` (NOT applied, author to do): Pisa is drawn inside the duchy 1399-1402, while republic-of-pisa /ledger/18 keeps Pisa a state in 1399 (a rename under the Visconti) to its 1406 annexation by Florence; the two dossiers overlap. Evidence: Gian Galeazzo Visconti page: 'Lord of Pisa: 13 February 1399 - 3 September 1402' is a title separate from Duke of Milan, passed to Gabriele Maria by the testament ('To his illegitimate son, Gabriele Maria, went Pisa and Crema'). Fix: Agree one reading with the republic-of-pisa author: either Pisa stays out of the duchy (drop it from /keyframe_review/1 and /ledger/1-2, and record a vassal_start of republic-of-pisa 1399-02 to 1402-09) or Pisa records a 1399 loss to the duchy.

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Duchy_of_Milan: confirmed: 'The duchy was officially established on 11 May 1395' (infobox gives the diploma as 1 May 1395)
- `/ledger/5` https://en.wikipedia.org/wiki/Wars_in_Lombardy: confirmed: peace 'signed on 30 December 1426 in Venice', Brescia 'went to Venice'
- `/ledger/8` https://en.wikipedia.org/wiki/Wars_in_Lombardy: confirmed: Visconti 'recognized the independence of Genoa', Peace of Cremona 20 November 1441
- `/ledger/12` https://en.wikipedia.org/wiki/Republic_of_Genoa: confirmed: 'The Milanese then changed sides, conquering Genoa in 1464'
- `/ledger/24, /ledger/26` https://en.wikipedia.org/wiki/Duchy_of_Milan: confirmed: 'on 24 July 1526 the citadel fell to the Imperial forces'; 'Francesco II Sforza died without heirs in 1535'
- `/ledger/17` https://en.wikipedia.org/wiki/Duchy_of_Milan: confirmed as worded ('the Swiss managed to retain the territories along the road that leads from the Gotthard Pass to the gates of Como', tied to Marignano 1515), but the event double-counts land, see fixes

Gaps for a gap-filler (not faults; within the page budget):
- `/keyframe_review/0..2`: Gian Galeazzo's Siena (1399-1404), Perugia (1400-1403) and Bologna (1402-1403) are not in the 1395-1402 keyframes; the Gian Galeazzo page names them only as 'claims to Perugia and Siena' and the Casalecchio victory, so this is a gap, not a fault. Try https://en.wikipedia.org/wiki/Republic_of_Siena
- `/ledger/2 and /keyframe_review/2..3`: The 1402-1421 break-up (Vicenza to Venice 1404, Verona 1405; Brescia and Bergamo under Pandolfo Malatesta 1404-1421; Cremona under Cabrino Fondulo; Parma and Reggio to the Este 1409) and Filippo Maria's recovery; /ledger/2 is confidence 1. Try https://en.wikipedia.org/wiki/Pandolfo_III_Malatesta
- `/ledger (1427)`: Vercelli ceded to Savoy in December 1427; county-of-savoy has only confidence-1 Vercelli cells. Try https://en.wikipedia.org/wiki/Amadeus_VIII,_Duke_of_Savoy
- `/ledger/8`: Genoa's revolt of December 1435 (the page's 1441 date is the recognition at the Peace of Cremona). Try https://en.wikipedia.org/wiki/Battle_of_Ponza_(1435)
- `/ledger/11`: Confidence 1: when Lodi and Piacenza returned from Venice (Piacenza was sacked by Sforza for the Ambrosian Republic in 1447). Try https://en.wikipedia.org/wiki/Peace_of_Lodi
- `/ledger (1500)`: Ludovico Sforza's return to Milan, February-April 1500. Try https://en.wikipedia.org/wiki/Battle_of_Novara_(1500)

## ambrosian-republic: fix

Area: No infobox area (map caption only); the dossier says so.

Findings:
- `/ledger/2/region` (applied by reviewer): The found event already subtracted Pavia, Lodi and Piacenza, which /ledger/0 and /ledger/1 then lose again in 1447, and duchy-of-milan /ledger/9 hands over its whole 1440 outline. Evidence: Golden Ambrosian Republic page: 'previously Milanese cities including Pavia, Lodi, and Piacenza defected or declared their independence' after the proclamation of 14 August 1447; duchy-of-milan /ledger/9 loses region {cliopatria: Duchy of Milan, 1440} to this state. Fix: found region changed to the whole outline {cliopatria: Ambrosian Republic, year 1450} with the page's words; the keyframe correction still subtracts the three provinces for the span.

Spot checks:
- `/ledger/2` https://en.wikipedia.org/wiki/Golden_Ambrosian_Republic: confirmed: Filippo Maria 'died on 13 August 1447'; republic proclaimed 'On the morning of the 14th'; infobox 'Established: 1447'
- `/ledger/3` https://en.wikipedia.org/wiki/Golden_Ambrosian_Republic: confirmed: coup 'on 24 February 1450'; 'On 22 March 1450, he had himself declared capitano del popolo'
- `/ledger/0, /ledger/1` https://en.wikipedia.org/wiki/Golden_Ambrosian_Republic: confirmed undated: 'Pavia, Lodi, and Piacenza defected'; 'Venice, now occupying Lodi and Piacenza'; Pavia kept by Sforza 'with the title of Count'
- `/identity/successors/0/note` https://en.wikipedia.org/wiki/Wars_in_Lombardy: confirmed: 'Francesco Sforza entered Milan in triumph (May 1450)' (the page disagreement is noted by the author)

Gaps for a gap-filler (not faults; within the page budget):
- `/ledger/0, /ledger/1`: Confidence 1: dates of the defection of Pavia, Lodi and Piacenza (the page dates none). Counterpart of /ledger/0 is free text ('Pavia ... then Sforza's county') with no dossier: Sforza held it as the republic's count. Try https://en.wikipedia.org/wiki/Francesco_I_Sforza
- `/keyframe_review/0`: The page says Sforza sacked Piacenza (taking it back from Venice for the republic) and captured Crema; the correction subtracts Piacenza for the whole span and there is no gain event for Piacenza or Crema. Try https://en.wikipedia.org/wiki/Piacenza

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| patriarchate-of-aquileia 1077 found (march-of-verona) | march-of-verona 1077 loss | matched | after the reviewer's slug fix (was kingdom-of-italy, the 1861-1946 state) |
| patriarchate-of-aquileia 1209 gain (Dukes of Merania (House of Andechs)) |  | exception | counterpart listed in the author's counterparts_needing_dossiers |
| patriarchate-of-aquileia 1291 loss (republic-of-venice) |  | exception | counterpart owned by an eu-13 part that has not run yet (no dossier in history/polities/) |
| patriarchate-of-aquileia 1419 loss (republic-of-venice) |  | exception | counterpart owned by an eu-13 part that has not run yet (no dossier in history/polities/); Cividale 23 July 1419 |
| patriarchate-of-aquileia 1420 loss (republic-of-venice) |  | exception | counterpart owned by an eu-13 part that has not run yet (no dossier in history/polities/); three 1420 losses (Istrian towns, Udine, rest of Friuli) |
| republic-of-florence 1254 gain (Commune of Pistoia) |  | exception | counterpart listed in the author's counterparts_needing_dossiers |
| republic-of-florence 1361 gain (Commune of Volterra) |  | exception | counterpart listed in the author's counterparts_needing_dossiers |
| republic-of-florence 1384 gain (Commune of Arezzo) |  | exception | counterpart listed in the author's counterparts_needing_dossiers |
| republic-of-florence 1406 gain (republic-of-pisa) | republic-of-pisa 1406 dissolve | matched | Pisa's dissolve names republic-of-florence |
| republic-of-florence 1421 gain (republic-of-genoa) |  | exception | counterpart owned by an eu-13 part that has not run yet (no dossier in history/polities/); Livorno |
| republic-of-florence 1494 loss (second-republic-of-pisa) |  | exception | counterpart listed in the author's counterparts_needing_dossiers |
| republic-of-florence 1509 gain (second-republic-of-pisa) |  | exception | counterpart listed in the author's counterparts_needing_dossiers |
| republic-of-florence 1548 gain (republic-of-genoa) |  | exception | counterpart owned by an eu-13 part that has not run yet (no dossier in history/polities/); Elba, counterpart doubtful (Piombino/Charles V) |
| republic-of-florence 1555 occupation_start (republic-of-siena) |  | exception | counterpart listed in the author's counterparts_needing_dossiers |
| republic-of-florence 1557 gain (kingdom-of-spain) | kingdom-of-spain | missing | kingdom-of-spain (eu-12) has no 1555 occupation of Siena and no 1557 loss of Siena to Florence |
| holy-roman-empire-minor-states 1556 loss (republic-of-florence) | republic-of-florence 1555 occupation_start | mismatch | HRE minor states /ledger/52 (confidence 1, Cliopatria-driven) gives Siena and Grosseto to Florence in 1556; Florence takes them from republic-of-siena (occupation April 1555) and kingdom-of-spain (July 1557). Route to eu-09. |
| republic-of-florence 1559 gain (Republic of Siena in Montalcino) |  | exception | counterpart listed in the author's counterparts_needing_dossiers |
| kingdom-of-naples 1282 found (kingdom-of-sicily) | kingdom-of-sicily 1282 split | matched |  |
| kingdom-of-sicily 1282 gain (kingdom-of-naples) | kingdom-of-naples | missing | Sicily /ledger/15 Messina 1282-10 and /ledger/16 Malta 1283 (confidence 1) gained from Naples; Naples' found region is the mainland only and it has no losses; also Sicily's contests 1283-1302 and 1313-1317 have no mirror in Naples |
| kingdom-of-naples 1442 loss (crown-of-aragon) | crown-of-aragon 1442 gain | matched | Aragon also has contest 1441-11 to 1442-06 that Naples lacks |
| kingdom-of-naples 1458 gain (crown-of-aragon) | crown-of-aragon 1458 split | matched | types differ (split/gain), same land and year |
| kingdom-of-naples 1495 occupation_start (kingdom-of-france) | kingdom-of-france 1495 occupation_start | matched | after the reviewer's type fix; end 1495-07 here against 1495-09 in France |
| kingdom-of-naples 1501 loss (crown-of-aragon) | crown-of-aragon 1500 gain | matched | Aragon dates it to the treaty (11 November 1500), Naples to the conquest (1501): within a year |
| kingdom-of-naples 1501 loss (kingdom-of-france) | kingdom-of-france 1501 gain | matched | July against August 1501 |
| duchy-of-milan 1395 found (lordship-of-milan) |  | exception | counterpart listed in the author's counterparts_needing_dossiers |
| holy-roman-empire-minor-states 1402 loss (duchy-of-milan) | duchy-of-milan 1395 found | mismatch | HRE minor states /ledger/26 (confidence 1) gives Lombardy to Milan in 1402 because Cliopatria's Milan row starts then; Milan's dossier has the duchy from the Visconti lordship in 1395. Route to eu-09. |
| duchy-of-milan 1399 gain (republic-of-pisa) | republic-of-pisa 1399 rename | mismatch | Pisa keeps its land in 1399 (rename under the Visconti); Milan draws it inside the duchy 1399-1402. See duchy-of-milan fixes. |
| duchy-of-milan 1402 loss (Visconti heirs' lordships (Filippo Maria, Gabriele Maria)) |  | missing | free-text counterpart, no dossier and not listed; confidence 1 |
| duchy-of-milan 1421 gain (republic-of-genoa) |  | exception | counterpart owned by an eu-13 part that has not run yet (no dossier in history/polities/); also 1441, 1464, 1478, 1488 |
| duchy-of-milan 1426 loss (republic-of-venice) |  | exception | counterpart owned by an eu-13 part that has not run yet (no dossier in history/polities/); also 1429 and 1453 |
| swiss-confederation 1440 gain (duchy-of-milan) | duchy-of-milan | missing | Leventina to Uri (confidence 3); Milan has no 1440 loss |
| duchy-of-milan 1447 loss (ambrosian-republic) | ambrosian-republic 1447 found | matched | after the reviewer's fix to the found region |
| duchy-of-milan 1450 gain (ambrosian-republic) | ambrosian-republic 1450 dissolve | matched |  |
| ambrosian-republic 1447 loss (republic-of-venice) |  | exception | counterpart owned by an eu-13 part that has not run yet (no dossier in history/polities/); Lodi and Piacenza |
| ambrosian-republic 1447 loss (Pavia (independent commune, then Sforza's county)) |  | missing | free-text counterpart, no dossier and not listed |
| swiss-confederation 1497 gain (duchy-of-milan) | duchy-of-milan | missing | Blenio, confidence 1 on the Swiss side; Milan's /keyframe_review/12 notes undated Ticino cells |
| duchy-of-milan 1499 loss (kingdom-of-france) | kingdom-of-france 1499 gain | matched |  |
| duchy-of-milan 1512 gain (kingdom-of-france) | kingdom-of-france 1512 loss | matched |  |
| swiss-confederation 1513 vassal_start (duchy-of-milan) | duchy-of-milan | missing | Swiss protectorate 1513 to 1515-09 (/ledger/26-27); Milan has no vassal events |
| duchy-of-milan 1515 loss (swiss-confederation) | swiss-confederation 1500 gain | mismatch | Swiss take Bellinzona 1500 and Locarno, Lugano, Mendrisio 1512 from kingdom-of-france; Milan's 1515 loss is of land it did not hold |
| duchy-of-milan 1515 loss (Three Leagues (Grisons)) | swiss-confederation 1512 vassal_start | mismatch | Valtellina to the Three Leagues in 1512 (from France) per swiss /ledger/25; Three Leagues is listed for a dossier |
| duchy-of-milan 1515 loss (kingdom-of-france) | kingdom-of-france 1515 gain | matched | October against September 1515 |
| duchy-of-milan 1521 gain (kingdom-of-france) | kingdom-of-france 1521 loss | matched |  |
| duchy-of-milan 1521 loss (papal-states) | papal-states 1512 gain | mismatch | papal-states /ledger/22 takes Parma and Piacenza in May 1512 with counterpart duchy-of-milan (should be kingdom-of-france, which held Milan); Milan's 1521 loss is of land it did not hold |
| duchy-of-milan 1524 loss (kingdom-of-france) | kingdom-of-france | missing | France (eu-10) has no October 1524 gain of Milan |
| duchy-of-milan 1525 gain (kingdom-of-france) | kingdom-of-france | missing | France (eu-10) has no February 1525 loss of Milan (Pavia) |
| duchy-of-milan 1526 loss (kingdom-of-spain) | kingdom-of-spain | missing | kingdom-of-spain (eu-12) has no 1526 gain or 1529 loss of Milan |
| duchy-of-milan 1529 gain (kingdom-of-spain) | kingdom-of-spain | missing | see 1526 |
| duchy-of-milan 1535 dissolve (kingdom-of-spain) | kingdom-of-spain 1535 gain | matched |  |

## For the orchestrator

- No page failed for the reviewer; one transient Input/output error reading ambrosian-republic.json on the mount, gone on retry.
- Reviewer applied four small fixes in place (Aquileia predecessor slug, Florence 1509 confidence, Naples 1495 occupation types, Ambrosian found region); all five dossiers re-validate with 0 errors.
- Orchestrator decision needed (rule 'one dossier per state, not per dynasty'): republic-of-florence ends with a dissolve on 9 July 1737 although the Grand Duchy continued under Lorraine to 1801/1859; Cliopatria's grand-duchy-of-tuscany row starts 1797, so 1737-1796 Tuscany has no dossier. Likewise duchy-of-milan ends 1535 (Duchy of Milan page runs the duchy to 1796; kingdom-of-spain absorbs it from 1535 and habsburg-monarchy from 1707) and kingdom-of-naples ends 1501 (Kingdom of Naples page runs to 1816). The author flagged all three.
- Mirror events missing on other groups' side: kingdom-of-france (eu-10) lacks Milan's October 1524 gain and February 1525 loss; kingdom-of-spain (eu-12) lacks Siena 1555-1557 and Milan 1526-1529; papal-states /ledger/22 (1512 Parma-Piacenza) names duchy-of-milan where kingdom-of-france held the land; holy-roman-empire-minor-states /ledger/26 and /ledger/52 are confidence-1 Cliopatria transfers that disagree with Milan's 1395 founding and Florence's 1555/1557 Siena events.
- republic-of-venice and republic-of-genoa have no dossier yet; 14 events of this batch wait on them (exceptions in cross_checks).
