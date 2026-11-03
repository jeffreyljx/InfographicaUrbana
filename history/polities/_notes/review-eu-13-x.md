# Review of batch eu-13-x (Italy additions)

Reviewer, 2026-10-31. Machine copy: history/notes/phase-b/reviews/eu-13-x.json. All 13 dossiers validate with --resolve (warnings only for counterpart slugs the author lists as needing dossiers). Spot checks: 4-8 events per dossier on the cited Wikipedia pages; no fabricated event found. Verdict meanings: fix = accepted once the listed fixes are made (applied: true means the reviewer already made it); fail = an unapplied blocking finding (wrong shape, missing event) goes back to the author; thin = honest but border moves unexplained, for a gap-filler.

| slug | verdict |
|---|---|
| republic-of-siena | thin |
| republic-of-siena-in-montalcino | pass |
| duchy-of-ferrara | fix |
| marquisate-of-montferrat | fail |
| duchy-of-mantua | fix |
| lordship-of-milan | fail |
| scaliger-lordship-of-verona | fix |
| carrara-lordship-of-padua | thin |
| viceroyalty-of-naples | fix |
| state-of-the-presidi | fix |
| republic-of-lucca | thin |
| duchy-of-urbino | thin |
| state-of-milan | fail |

## republic-of-siena: thin

- thin /keyframe_review/2: K1 (1260-1334: Siena 30 km plus a Montalcino circle) becomes K2 (1335: Siena and Grosseto provinces, about +4,500 km2) with only the 1335 Massa circle in the ledger; Grosseto, the ports of Talamone, Porto Ercole and Porto Santo Stefano (page: 'the conquest of the ports', no year), Montepulciano and Chiusi are undated (author flagged). Within the 5-page budget. Try: https://en.wikipedia.org/wiki/Grosseto
- thin /keyframe_review/2/correction: Siena province includes Montepulciano (Florentine for much of 1390-1555), the Chianti and Colle/Poggibonsi/San Gimignano, which republic-of-florence draws; the province reading needs dated subtractions or a note. Try: https://en.wikipedia.org/wiki/Montepulciano
- thin /ledger/4: 1547 Spanish governor (History of Siena) vs the Republic of Siena page's timeline 'Spanish Lordship 1548-1552'; confidence 2 is right, the year needs one more page. Try: https://en.wikipedia.org/wiki/Diego_Hurtado_de_Mendoza_(poet)
- spot checks: /ledger/0 confirmed; /ledger/3 confirmed; /ledger/5 confirmed; /ledger/6 confirmed; /ledger/8 confirmed; /ledger/9 confirmed
- area: no Cliopatria row; body text 'approximately 8,000 km2' (mid-16th century), no infobox area; compared with keyframe K2 (page 8000, Cliopatria None, ratio 0.98)

## republic-of-siena-in-montalcino: pass

Tried: both end dates (3 April 1559 war page, 1559 Siena page) and the start; Florence /ledger/14-15 mirror the 1559 end (by name); land equals the circle Siena's 1555 split hands over.

- spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed
- area: no area on any page; 15 km radius stated as a reading (page None, Cliopatria None, ratio None)

## duchy-of-ferrara: fix

- **/keyframe_review/0/correction** (for the author): Comacchio is missing from K0-K2 (1208-1481) and from the found region, then appears in K3 (1482) with no gain event. Evidence: War of Ferrara (1482-1484): in 1482 Ferrara 'had begun to take control over the saltworks at Comacchio' and Venetian troops were 'quickly overrunning Comacchio'; Duchy of Ferrara: in 1597 'Ferrara was claimed as a vacant fief by the Pope, as was Comacchio'. Fix: Add the Comacchio circle (12.18, 44.69, 15 km) to K0-K2 and /ledger/0 from a dated acquisition, or add a gain event (confidence 1 if undated) before 1482.
- **/ledger/0** (for the author): papal-states /ledger/8 (1208 vassal_start, counterpart duchy-of-ferrara) and /ledger/24 (1597 vassal_end) have no vassal_start/vassal_end mirror here; this ledger has found and loss only. Evidence: Brief rule 3: a vassal_start of X needs a vassal_start in X's ledger. Duchy of Ferrara page: Ferrara 'was claimed as a vacant fief by the Pope'. Fix: Add vassal_start 1208 and vassal_end 1597, counterpart papal-states, source Duchy_of_Ferrara, confidence 2.
- thin /ledger/2: 1438 return of Rovigo to the Este is a bridge (confidence 1). Try: https://en.wikipedia.org/wiki/Polesine
- thin /ledger/8: 1509 Este recovery of Rovigo is undated on the Rovigo page (confidence 1). Try: https://en.wikipedia.org/wiki/War_of_the_League_of_Cambrai
- thin /identity: Este Modena and Reggio (1288-1814) drawn by nobody (author flagged; duchy-of-modena-and-reggio is eu-20's 1815-1859 row). Try: https://en.wikipedia.org/wiki/Duchy_of_Modena_and_Reggio
- spot checks: /ledger/0 confirmed; /ledger/3 confirmed; /ledger/5 confirmed; /ledger/6 confirmed; /ledger/9 confirmed; /ledger/10 confirmed
- area: body text 'about 1,100 km2 south of the lower Po'; compared with the 19 km circle; Rovigo (north of the Po) excluded from the figure (page 1100, Cliopatria None, ratio 1.03)

## marquisate-of-montferrat: fail

- **/keyframe_review/0/correction** (for the author): K0-K2 draw the whole Alessandria and Asti provinces for 967-1708, the modern region, not the state; Alessandria province is drawn at the same time by this batch's lordship-of-milan (K2-K10, a1:Alessandria from 1313) and lies inside the Cliopatria Duchy of Milan shapes 1402-1539 (bbox 7.92-10.6 E, 44.19-46.7 N). Evidence: Montferrat page: 'It comprises roughly (and its extent has varied over time) the modern provinces of Alessandria and Asti' (present tense, the region); its only place-specific sentence is 'the countryside near Casale Monferrato'. Visconti of Milan: after 1313 the Visconti became lords of 'Bergamo, Tortona, Alessandria, Vercelli, and Piacenza'. Fix: Redraw the state as the Casale/Monferrato core plus named towns, and subtract the land Milan holds (Alessandria, Tortona and their districts from 1313) or record dated gains and losses; say in the note which reading was chosen.
- **/ledger** (for the author): Missing mirror of a confidence-3 event in this batch: lordship-of-milan /ledger/16 (1356, Mondovi and Chieri lost to marquisate-of-montferrat) has no gain here; the same page also gives Montferrat Asti and Pavia after the peace of 8 June 1358. Evidence: Lordship of Milan page (war begun 1356): '...also took Mondovi and Chieri from the Visconti'; after the peace of 8 June 1358 'Asti and Pavia remained to the Marquis of Montferrat'; Visconti of Milan: 'In 1359, Pavia surrendered to Galeazzo II'. Fix: Add gain 1356 (circles at Mondovi 7.82/44.39 and Chieri 7.82/45.01, counterpart lordship-of-milan, confidence 3, source Lordship_of_Milan), the Asti and Pavia holdings of 1356/1358 and the 1359 loss of Pavia to lordship-of-milan, with keyframes.
- **/ledger/4** (for the author): duchy-of-mantua /ledger/3 (vassal_start 1536) and /ledger/6 (vassal_end 1708) name this state as counterpart; here 1536 is a rename and 1708 a loss, with no vassal events. Evidence: Brief rule 3 (vassal mirrors). Marquisate of Montferrat page: Charles V 'restored it to Federico II, Duke of Mantua ... in 1536'. Fix: Add vassal_start 1536 and vassal_end 1708 with counterpart duchy-of-mantua (or have Mantua drop its pair); one model in both dossiers.
- **/identity/capitals/0** (for the author): Chivasso (7.89, 45.19) lies in Turin province, outside every keyframe (Alessandria plus Asti). Evidence: Rule 9: capitals inside the state's shapes. Marquisate page: 'The capital of Montferrat at this time was Chivasso' (13th century). Fix: Add a Chivasso circle to K0 for the years it was the capital, or give a capital inside the shape (Casale) with a page.
- **/keyframe_review/1** (for the author): Trino and Alba appear in K1 (1536) with no gain event; K0 lacks them although Trino was Montferrat's before 1628. Evidence: War of the Mantuan Succession: 'Savoyard forces captured Trino in April' (1628); infobox 'Savoy annexes Trino and Alba' (1631). Fix: Include Trino and Alba in K0 from a dated acquisition, or add the gain events.
- **/wars/0/belligerents/5** (applied by reviewer): holy-roman-empire names a dossier that ends in 1259; the Empire after 1260 is holy-roman-empire-minor-states. Evidence: holy-roman-empire identity: end 1259, successor holy-roman-empire-minor-states. Fix: Replaced with holy-roman-empire-minor-states.
- thin /ledger: No territorial event between 967 and 1533 (568 years) apart from the 1305 dynasty change; author flagged that no page dates acquisitions. Try: https://en.wikipedia.org/wiki/Casale_Monferrato
- spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/7 confirmed (year from context, 1628); /ledger/9 confirmed; /ledger/11 confirmed
- area: no area on either page; the two provinces are the region, see fix 1 (page None, Cliopatria None, ratio None)

## duchy-of-mantua: fix

- **/wars/0/from** (applied by reviewer): War dated from 1627; the page says 1628-1631. Evidence: War of the Mantuan Succession: infobox '1628-1631'; lead 'The War of the Mantuan Succession, 1628 to 1631'. Fix: from 1628 (the December 1627 extinction stays in the outcome text).
- **/ledger/4/counterpart** (applied by reviewer): Counterpart holy-roman-empire (also /ledger/5 and /wars/0/belligerents) is a dossier that ends in 1259. Evidence: holy-roman-empire identity: end 1259, successor holy-roman-empire-minor-states (1260-1806). Fix: Replaced with holy-roman-empire-minor-states in /ledger/4, /ledger/5 and /wars/0/belligerents.
- thin /keyframe_review/0: One keyframe (Mantova province) for 1328-1707; the Gonzaga cadet states (Sabbioneta, Bozzolo, Castiglione, Guastalla), Venetian Asola and Gianfrancesco's 'Upper Mantua' additions are undated; no page gives an area. Try: https://en.wikipedia.org/wiki/Sabbioneta
- spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/4 confirmed; /ledger/7 confirmed; /ledger/3 page says 1531 (marriage), Montferrat page 1536; acknowledged in the note, confidence 2
- area: no area on the pages (page None, Cliopatria None, ratio None)

## lordship-of-milan: fail

- **/ledger/15** (applied by reviewer): Note said the page is silent on the end of the Genoa lordship (confidence 1); it is not. Evidence: Visconti of Milan: 'In 1356 Genoa regained its independence.' Fix: Note rewritten with the quote; confidence 1 -> 2 (the Ligurian extent stays a reading).
- **/ledger/14** (for the author): The 1354 split and /ledger/17 1385 merge move a1:Pavia out of and back into the state, while K7-K10 keep Pavia and the K7 note says the division is 'one realm for the map'; the ledger and keyframes contradict each other for 1354-1385. Evidence: Rule 4. Also Visconti of Milan: 'In 1359, Pavia surrendered to Galeazzo II', so Pavia was not a Visconti share in 1354. Fix: Retype /ledger/14 and /ledger/17 as rename (no region) or drop them; keep the division in notes.
- **/keyframe_review/2/correction** (for the author): Pavia is drawn as Visconti land 1313-1386 (K2-K7) but the cited pages put it outside Visconti rule until 1359, with Montferrat in 1358; no event records the 1359 gain. Evidence: Visconti of Milan: 'In 1359, Pavia surrendered to Galeazzo II'; Lordship of Milan: after the peace of 8 June 1358 'Asti and Pavia remained to the Marquis of Montferrat' (author's notes flag this as unexplained). Fix: Remove a1:Pavia from K2-K7 (at least 1356-1358) and add gain 1359 (Pavia, counterpart marquisate-of-montferrat or the Commune of Pavia, confidence 3, source Visconti_of_Milan); split K7 at 1359.
- **/ledger/11** (for the author): The whole Cuneo province (about 6,900 km2, including Saluzzo and Alba) is gained in 1347 and kept, less a Mondovi circle, until 1395, on a page that names only the line 'until Mondovi and Cuneo'. Evidence: Visconti of Milan: 'in 1347 he extended the western border of the Visconti dominions along a stretch of land until Mondovi and Cuneo'; Lordship of Milan: Mondovi and Chieri lost in 1356; no page keeps Cuneo to 1395. Fix: Replace a1:Cuneo by circles at Cuneo and Mondovi and record when Cuneo was lost (or mark the extension 1356-1395 confidence 1 in the keyframe note).
- **/keyframe_review/0/correction** (for the author): K0 (1259-1270) contains Como (gained December 1263), Lodi (1270) and Brescia, Cremona and Novara (no gain event) from 1259. Evidence: Lordship of Milan: 'In December 1263 Filippo annexed Como'; 'In April 1270 Milan waged war on Lodi which fell 3 months later'. Fix: Start K0 with Milan only and split at 1263 and 1270, or add the gains of Brescia, Cremona and Novara with a page.
- thin /ledger/6: 1313 gain of seven provinces at confidence 1; the page lists Bergamo, Tortona, Alessandria, Vercelli and Piacenza and says pro-Visconti regimes settled in Como, Novara and Pavia, undated. Try: https://en.wikipedia.org/wiki/Matteo_I_Visconti
- spot checks: /ledger/1 confirmed; /ledger/3 confirmed; /ledger/8 confirmed; /ledger/12 confirmed; /ledger/16 confirmed (1356); /ledger/20 confirmed; /ledger/21 confirmed (infobox 5 September 1395); /ledger/15 page not silent: 'In 1356 Genoa regained its independence' (fixed)
- area: no area on any page (page None, Cliopatria None, ratio None)

## scaliger-lordship-of-verona: fix

- **/keyframe_review/3/correction** (applied by reviewer): K3 (1321-1327) dropped the Monselice-Este-Montagnana circle with no ledger event. Evidence: Cangrande I della Scala: Padua 'on 12 February 1318 ceded Monselice, Este, Castelbaldo and Montagnana to Cangrande for life'; he died 22 July 1329; the page records no return. Fix: Monselice circle added back to K3, note rewritten.
- **/ledger/8** (for the author): One event for Parma and Lucca with the string counterpart 'Parma and Lucca (sellers not named by the page)'; republic-of-lucca /ledger/5 records the 1335 loss of Lucca to this dossier. Evidence: Mastino II: 'Parma (1335) in Lombardy and Lucca (1335) in Tuscany'. Fix: Split into a Parma gain (counterpart as now) and a Lucca gain with counterpart republic-of-lucca.
- **/ledger/13** (for the author): Belluno is given to Venice in 1339; the Venice ledger gains only Treviso and Bassano that year (/ledger/28), and Belluno is Venetian only from 1404 (/ledger/48). Evidence: Della Scala and Mastino II pages name no taker; republic-of-venice /ledger/28 'Treviso and Bassano del Grappa in 1339'. Fix: Limit the Venice loss to a1:Treviso and give Belluno its own loss (counterpart not named, confidence 1).
- thin /ledger/13: Taker of Treviso/Belluno/Feltre in 1339 not on the pages (confidence 1). Try: https://en.wikipedia.org/wiki/Belluno
- thin /ledger/14: Parma and Lucca lost 1339 to unnamed League members (confidence 1); Lucca is drawn by nobody 1339-1370. Try: https://en.wikipedia.org/wiki/Parma
- spot checks: /ledger/1 confirmed; /ledger/2 confirmed; /ledger/5 confirmed; /ledger/6 confirmed; /ledger/8 confirmed; /ledger/15 confirmed
- area: no area on the pages (page None, Cliopatria None, ratio None)

## carrara-lordship-of-padua: thin

- **/ledger/0** (for the author): The found region already excludes the Monselice circle, and /ledger/1 loses the same circle again in February 1318. Evidence: Both events carry the same circle (11.6, 45.23, 20 km). Fix: Make the found region a1:Padova and keep /ledger/1 as the loss (or drop /ledger/1).
- thin /keyframe_review/1: House of Carrara: 'Under their rule, Padua conquered Verona, Vicenza, Treviso, Feltre, Belluno, Bassano, Aquileia and Udine'; none is in the ledger or keyframes (Padova only 1337-1405) and the author's notes do not flag it. Try: https://en.wikipedia.org/wiki/Francesco_I_da_Carrara
- spot checks: /ledger/0 confirmed; /ledger/3 confirmed (infobox 1329-1337; Carrara page 1338, acknowledged); /ledger/5 confirmed; /ledger/6 confirmed
- area: no area on the pages (page None, Cliopatria None, ratio None)

## viceroyalty-of-naples: fix

- **/ledger/0/counterpart** (for the author): Found counterpart kingdom-of-france, but France's ledger loses Naples to crown-of-aragon at the end of 1503 (/ledger/78) and crown-of-aragon /ledger/69 holds the whole kingdom from 1503; the viceroyalty takes over from Aragon. Evidence: Kingdom of Naples: 'left Ferdinand in full control of the kingdom by 1504'. Fix: Counterpart crown-of-aragon (keep France among predecessors), or have crown-of-aragon record the hand-over.
- thin /ledger/2: End of the 1647 revolt: Kingdom of Naples page 'suppressed later that year' (1647) vs the viceroy list's 1648 (confidence 2, acknowledged). Try: https://en.wikipedia.org/wiki/Neapolitan_Republic_(1647%E2%80%931648)
- spot checks: /ledger/0 confirmed; /ledger/1 confirmed (infobox 7 July 1647); /ledger/4 confirmed; /ledger/5 confirmed
- area: no area on the page; reuses Cliopatria Kingdom of Naples 1497-1501 shape (68,688 km2) (page None, Cliopatria 68688, ratio None)

## state-of-the-presidi: fix

- **/ledger/2** (applied by reviewer): Overlord change dated 26 September 1733 (the Treaty of Turin promise); the transfer is the conquest of May 1735 on the same page, and habsburg-monarchy /ledger/74 and kingdom-of-naples-bourbon /ledger/1 date it 1735. Evidence: State of the Presidi: 'During the subsequent War of the Polish Succession in May 1735, a Spanish and allied army under the Duke of Montemar...'. Fix: Year 1735, month 5, note rewritten (treaty promise kept in the note).
- **/keyframe_review/0/correction** (for the author): Porto Longone (Elba circle) is drawn from 1557; the 1557 state is the five mainland towns and the Porto Longone fortress is later. Evidence: State of the Presidi: 'the five towns of Porto Ercole and Porto Santo Stefano ..., as well as Orbetello, Talamone and Ansedonia' ; construction of Fort San Giacomo at Porto Longone 'began in March 1605'. Fix: Split K0 at 1605 (or the year a page gives) and add a gain event for Porto Longone (confidence 2).
- spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 mis-dated: promise 1733, transfer May 1735 (fixed); /ledger/3 confirmed
- area: body 'about 300 square kilometres' and 'about 287 km2' (1557 act) (page 300, Cliopatria None, ratio 1.43)

## republic-of-lucca: thin

- thin /keyframe_review/1: Whole Lucca province 1370-1805; the page says the Guinigi-era war 'led it to lose parts of its former territories' (no year): Garfagnana to the Este, Pietrasanta and the Versilia to Florence; no event. Try: https://en.wikipedia.org/wiki/Garfagnana
- thin /ledger/6: 1335-1370: Verona loses Lucca in 1339 (its /ledger/14) and Lucca regains it from Pisa in 1370 (counterpart a reading); no event gives Lucca to Pisa or Florence, so nobody draws it 1339-1370 (page: Pisa acquired it, lord Giovanni dell'Agnello, undated). Try: https://en.wikipedia.org/wiki/Giovanni_dell%27Agnello
- spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/6 confirmed; /ledger/9 confirmed; /ledger/11 confirmed; /ledger/5 confirmed
- area: no area in the infobox (population only) (page None, Cliopatria None, ratio None)

## duchy-of-urbino: thin

- thin /keyframe_review/1: Senigallia appears in K1 (1503) with no event, and K0-K1 draw the whole Pesaro e Urbino province from 1443 including Pesaro; the page says Francesco Maria I della Rovere (from 1508) 'was also able to expand the state with Senigallia and, above all, Pesaro' (undated). Exclude a Pesaro circle until a dated gain. Try: https://en.wikipedia.org/wiki/Pesaro
- thin /ledger/9: Devolution 1625 (lead) vs 1631 (body, infobox); author flagged. Try: https://en.wikipedia.org/wiki/Francesco_Maria_II_della_Rovere
- spot checks: /ledger/0 confirmed; /ledger/3 confirmed; /ledger/8 confirmed; /ledger/9 confirmed (lead says 1625; acknowledged)
- area: page 'an area of 5,556 square kilometers' at the last legation census (undated) (page 5556, Cliopatria None, ratio 0.59)

## state-of-milan: fail

- **/keyframe_review/0/correction** (for the author): The 1535 Duchy of Milan shape is held unchanged to 1795 and /certainty says the frontier never changed; the state lost its western lands to Savoy/Sardinia in 1707-1713, 1738 and 1743-1748. Author opened 1 page of a 2-5 budget. Evidence: War of the Polish Succession: 'Charles Emmanuel III of Sardinia received territories in the western part of the Duchy of Milan west of the Ticino' 'including Novara and Tortona' (Treaty of Vienna, November 1738); habsburg-monarchy /ledger/60 (11 April 1713: 'parts of the Duchy of Milan' to Savoy), /ledger/72 and /ledger/77-78 (1733-1738 occupation and loss) and house-of-savoy /ledger/24 (1713) record losses this dossier lacks. Fix: Add loss 1707/1713 (Alessandria, Valenza, Lomellina, Valsesia; counterpart house-of-savoy), the 1733-1738 Franco-Sardinian occupation, loss 1738 (Novara, Tortona; counterpart kingdom-of-sardinia), loss 1743/1748 (Vigevano, Oltrepo Pavese; Treaty of Worms, Aix-la-Chapelle), and split K0 at each; rewrite /certainty.
- **/ledger/0** (for the author): The state double-draws Milan with kingdom-of-spain /ledger/4 (1535 gain of Milan) and habsburg-monarchy /ledger/54 (1707 gain), which draw the duchy as their own land; neither records a vassal relation with state-of-milan. Evidence: Cross-check of the three ledgers. Fix: Orchestrator decision (see problems): either the colony layer is drawn and the sovereign dossiers record vassal_start/vassal_end with counterpart state-of-milan, or the colony dossier is dropped.
- spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed
- area: infobox 'Estimate' with no figure; reused Cliopatria duchy-of-milan_1534 shape (17,546 km2) (page None, Cliopatria 17546, ratio None)

## Cross-dossier matrix

- republic-of-siena 1547 occupation_start cp=kingdom-of-spain -> kingdom-of-spain None None: **missing** kingdom-of-spain has no Italian event 1533-1557 (also /ledger/5 1552 occupation_end).
- republic-of-siena 1555 loss cp=kingdom-of-spain -> republic-of-florence 1555 occupation_start: **mismatch** Spain has no 1555 gain; Florence /ledger/11 records the occupation with counterpart republic-of-siena and /ledger/13 a 1557 gain from kingdom-of-spain (no Spanish loss). Either Spain adds gain 1555/loss 1557 or Siena names republic-of-florence.
- republic-of-siena 1555 loss cp=republic-of-florence -> republic-of-florence 1555 occupation_start: **mismatch** Massa (February 1555) is a loss here; Florence has only the April occupation of the whole territory.
- republic-of-siena 1555 split cp=republic-of-siena-in-montalcino -> republic-of-siena-in-montalcino 1555 found: **matched** 
- republic-of-siena-in-montalcino 1559 loss cp=republic-of-florence -> republic-of-florence 1559 gain: **matched** Florence /ledger/15 names the string 'Republic of Siena in Montalcino'; should use the slug.
- duchy-of-ferrara 1395 loss cp=republic-of-venice -> republic-of-venice 1395 gain: **mismatch** Venice /ledger/42 counterpart 'holder not named by the page'; should be duchy-of-ferrara.
- duchy-of-ferrara 1438 gain cp=republic-of-venice -> republic-of-venice 1438 loss: **matched** 
- duchy-of-ferrara 1482 loss cp=republic-of-venice -> republic-of-venice 1482 gain: **matched** 
- duchy-of-ferrara 1484 loss cp=republic-of-venice -> republic-of-venice 1484 gain: **matched** 
- duchy-of-ferrara 1509 gain cp=republic-of-venice -> republic-of-venice 1509 loss: **matched** 
- duchy-of-ferrara 1514 loss cp=republic-of-venice -> republic-of-venice 1514 gain: **matched** 
- duchy-of-ferrara 1597 loss cp=papal-states -> papal-states 1597 gain: **matched** papal-states /ledger/25; its /ledger/8 (1208 vassal_start) and /ledger/24 (1597 vassal_end) have no vassal mirror in Ferrara (fix listed).
- marquisate-of-montferrat 1533 occupation_start cp=kingdom-of-spain -> kingdom-of-spain None None: **missing** Also 1536 occupation_end. The page says 'the Spanish under Emperor Charles V'; Spain's ledger has nothing.
- marquisate-of-montferrat 1631 loss cp=house-of-savoy -> house-of-savoy 1631 gain: **mismatch** Savoy /ledger/11 names duchy-of-mantua as the loser; land agrees (Trino, Alba).
- marquisate-of-montferrat 1708 loss cp=house-of-savoy -> house-of-savoy 1708 gain: **mismatch** Savoy /ledger/20 names duchy-of-mantua.
- lordship-of-milan 1356 loss cp=marquisate-of-montferrat -> marquisate-of-montferrat None None: **missing** Montferrat has no 1356 gain of Mondovi and Chieri (fix listed in Montferrat).
- duchy-of-mantua 1536 vassal_start cp=marquisate-of-montferrat -> marquisate-of-montferrat 1536 rename: **mismatch** Montferrat records a rename, not a vassal_start (also 1708 vassal_end vs loss).
- duchy-of-mantua 1630 occupation_start cp=holy-roman-empire-minor-states -> holy-roman-empire-minor-states None None: **missing** Counterpart corrected by the reviewer from holy-roman-empire (ends 1259); no mirror for 1630/1631.
- duchy-of-mantua 1708 loss cp=habsburg-monarchy -> habsburg-monarchy 1708 gain: **matched** Habsburg /ledger/56 names the string 'Duchy of Mantua'; should use the slug.
- lordship-of-milan 1337 gain cp=scaliger-lordship-of-verona -> scaliger-lordship-of-verona 1337 loss: **matched** 
- lordship-of-milan 1353 vassal_start cp=republic-of-genoa -> republic-of-genoa None None: **missing** Genoa has no 1353 vassal_start or 1356 vassal_end naming lordship-of-milan.
- lordship-of-milan 1387 gain cp=scaliger-lordship-of-verona -> scaliger-lordship-of-verona 1387 loss: **matched** 
- lordship-of-milan 1388 gain cp=carrara-lordship-of-padua -> carrara-lordship-of-padua 1388 loss: **matched** 
- lordship-of-milan 1390 loss cp=carrara-lordship-of-padua -> carrara-lordship-of-padua 1390 gain: **matched** 
- lordship-of-milan 1395 dissolve cp=duchy-of-milan -> duchy-of-milan 1395 found: **mismatch** Lordship ends September 1395 (5 Sept, infobox); duchy-of-milan is founded May 1395 (11 May): both alive May-September.
- scaliger-lordship-of-verona 1318 gain cp=carrara-lordship-of-padua -> carrara-lordship-of-padua 1318 loss: **matched** 
- scaliger-lordship-of-verona 1328 gain cp=carrara-lordship-of-padua -> carrara-lordship-of-padua 1328 loss: **matched** 
- scaliger-lordship-of-verona 1335 gain cp=Parma and Lucca (sellers not named by the page) -> republic-of-lucca 1335 loss: **mismatch** Lucca names scaliger-lordship-of-verona; Verona's counterpart is a string.
- scaliger-lordship-of-verona 1337 loss cp=carrara-lordship-of-padua -> carrara-lordship-of-padua 1337 gain: **matched** 
- scaliger-lordship-of-verona 1339 loss cp=republic-of-venice -> republic-of-venice 1339 gain: **mismatch** Venice /ledger/28 gains Treviso and Bassano (counterpart string 'Scaliger rulers at Verona'); Verona also gives it Belluno, which Venice takes only in 1404. Venice /ledger/27 (1337, Mestre) has no Verona mirror (Mestre not drawn by Verona).
- carrara-lordship-of-padua 1405 loss cp=republic-of-venice -> republic-of-venice 1405 gain: **matched** Venice /ledger/49 names the string 'Carrara lordship of Padua'; should use the slug.
- viceroyalty-of-naples 1504 found cp=kingdom-of-france -> crown-of-aragon 1503 gain: **mismatch** France /ledger/78 loses Naples to crown-of-aragon (end 1503); Aragon /ledger/69 holds it; Aragon (to 1515), kingdom-of-spain (/ledger/2 merge 1516 'with Naples') and habsburg-monarchy (/ledger/55, 1707) all draw Naples as own land.
- viceroyalty-of-naples 1734 loss cp=kingdom-of-naples-bourbon -> kingdom-of-naples-bourbon 1735 found: **mismatch** Bourbon /ledger/0 founded 1735 with counterpart habsburg-monarchy; habsburg-monarchy /ledger/73 also loses Naples in 1734.
- state-of-the-presidi 1801 loss cp=kingdom-of-etruria -> kingdom-of-etruria 1801 found: **mismatch** Etruria /ledger/0 found 1801 with counterpart grand-duchy-of-tuscany; no gain of the Presidi.
- state-of-the-presidi 1735 rename cp=None -> kingdom-of-naples-bourbon 1735 gain: **matched** After the reviewer's fix the overlord change (May 1735) matches Bourbon /ledger/1 and habsburg-monarchy /ledger/74, both of which draw the Presidi as own land (double drawing).
- republic-of-lucca 1314 occupation_start cp=republic-of-pisa -> republic-of-pisa None None: **missing** Pisa (1000-1406) has no Lucca events: also 1316 occupation_end and 1370 gain.
- republic-of-lucca 1370 gain cp=republic-of-pisa -> republic-of-pisa None None: **missing** No Pisan gain of Lucca (1342) or loss (1369/1370).
- republic-of-lucca 1799 occupation_start cp=french-directory -> french-directory None None: **exception** Cliopatria row of a group that has not run yet (also /ledger/10 and state-of-milan /ledger/3).
- duchy-of-urbino 1502 loss cp=duchy-of-romagna -> duchy-of-romagna None None: **exception** No dossier; listed in the author's counterparts_needing_dossiers (also 1503 gain).
- duchy-of-urbino 1516 loss cp=papal-states -> papal-states None None: **missing** Papal States has no 1516 gain / 1521 loss of Urbino.
- duchy-of-urbino 1631 loss cp=papal-states -> papal-states 1631 gain: **matched** 
- state-of-milan 1535 found cp=duchy-of-milan -> duchy-of-milan 1535 dissolve: **matched** But kingdom-of-spain /ledger/4 (1535 gain from duchy-of-milan) also takes the land.
- habsburg-monarchy 1713 loss cp=house-of-savoy -> state-of-milan None None: **missing** Habsburg /ledger/60 (parts of Milan to Savoy 1713) and /ledger/78 (Novara, Tortona 1738) have no loss in state-of-milan.
- holy-roman-empire-minor-states 1402 loss cp=duchy-of-milan -> lordship-of-milan None None: **mismatch** HRE Minor States (Cliopatria) draws Lombardy until 1402, the Veneto until 1407 (/ledger/28), Siena-Grosseto until 1556 (/ledger/52) and Mantua until 1797; the new dossiers draw the same land from 1259, 1262, 1318, 1125 and 1328.
- republic-of-siena 1260 gain cp=Montalcino -> None None None: **exception** Counterpart is a town or commune with no dossier; acceptable.
- republic-of-siena 1335 gain cp=Republic of Massa -> None None None: **exception** Counterpart is a town or commune with no dossier; acceptable.
- lordship-of-milan 1263 gain cp=communes of Lombardy (Como, Lodi, Cremona, Parma, Pepoli Bologna, Piedmont lords) -> None None None: **exception** Counterpart is a town or commune with no dossier; acceptable.
- scaliger-lordship-of-verona 1312 gain cp=communes of the Veneto (Padua, Feltre, Belluno, Treviso, Brescia) -> None None None: **exception** Counterpart is a town or commune with no dossier; acceptable.

## Problems for the orchestrator

- Systemic double drawing 1: holy-roman-empire-minor-states (Cliopatria, eu-09) still draws Lombardy to 1402 (/ledger/26), the Veneto to 1407 (/ledger/28), Siena and Grosseto to 1556 (/ledger/52) and Mantua, Modena, Reggio and Parma to 1797 (/ledger/93, /ledger/105), the same land as lordship-of-milan (1259-1395), scaliger-lordship-of-verona, carrara-lordship-of-padua, republic-of-siena and duchy-of-mantua; none of these dossiers records the overlap. Needs an orchestrator rule (suzerain layer with vassal events, or subtract).
- Systemic double drawing 2: the colony dossiers viceroyalty-of-naples (1504-1734), state-of-milan (1535-1796) and state-of-the-presidi (1557-1801) draw land that crown-of-aragon (Naples 1503-1515), kingdom-of-spain (Naples from the 1516 merge, Milan from 1535 /ledger/4), habsburg-monarchy (Milan and Naples from 1707, /ledger/54-55) and kingdom-of-naples-bourbon (Presidi from 1735, /ledger/1) already draw as their own; no sovereign dossier has vassal events naming the colonies. The author flagged it.
- kingdom-of-spain (1516-) has no event for Siena (1547-1557) or Montferrat (1533-1536); republic-of-pisa has none for Lucca; republic-of-genoa none for the 1353-1356 Visconti lordship; papal-states none for Urbino 1516-1521 (see cross_checks).
- WebFetch: Treaty_of_Vienna_(1738) does not mention Milan; the 1738 cession was read on War_of_the_Polish_Succession.
- Reviewer edits (re-validated with validate_dossier.py --resolve, read back unchanged after >10 s): duchy-of-mantua /wars/0 and /ledger/4-5; marquisate-of-montferrat /wars/0/belligerents/5; lordship-of-milan /ledger/15; scaliger-lordship-of-verona /keyframe_review/3; state-of-the-presidi /ledger/2. Files re-serialised in the original 1-space indent, no trailing newline.
- Gazetteer: every region resolves; the author suggests adding Montalcino, Massa Marittima, Orbetello, Mantua (place), Trino, Alba, Comacchio as places (now circles).
