# Review of batch eu-10-f (France part f): Poitou, Auvergne, Armagnac, Périgord, Touraine

Reviewer, 2026-10-25. Validator: all five dossiers 0 errors (warnings are the six unknown gazetteer names). Verdicts: county-of-poitou **thin**, county-of-auvergne **fail**, county-of-armagnac **thin**, county-of-perigord **thin**, county-of-touraine **fail**.
Every spot-checked event was on its page with its year; nothing fabricated. The two failures are modelling errors: land drawn for a state that its own pages say belonged to someone else.

## county-of-poitou: thin

Findings:
- `/ledger/2` (to do): The 1271 dissolve to kingdom-of-france is mirrored twice in kingdom-of-france: a 1250 gain of Poitou from county-of-poitou (c1, Cliopatria only) and a 1271 gain from the non-slug 'Alfonso, Count of Poitou (apanage)' (c3). Evidence: County of Auvergne page: 'On Alfonso's death in 1271, Auvergne, along with the County of Toulouse, Poitou and the Comtat Venaissin' reverted to the royal domain; Alphonse page: died at Savona 21 August 1271. kingdom-of-france /ledger/24 and /ledger/27. Fix: No change in this dossier; route to kingdom-of-france: drop its 1250 gain from county-of-poitou and set the 1271 gain's counterpart to county-of-poitou. Non-blocking.
- `/ledger/0` (to do): The dossier holds Poitou as one French county continuously from 1205, but kingdom-of-france has Louis VIII conquering Poitou from the English in 1224 (c3, Louis VIII page) and its 1204 gain says 'Poitou temporarily'; 1205-1225 is also the crown's own confiscated fief, not yet Alphonse's apanage, so it overlaps the France shape. Evidence: County of Poitou page: 'Poitou was conquered by King Philip II of France in 1205 after he declared it a confiscated fief of the crown' and 'Henry III of England failed to retake it in the Saintonge War' (no dates); kingdom-of-france /ledger/16 and /ledger/19. Fix: Open the Louis VIII page (the source of kingdom-of-france /ledger/19); if it puts Poitou back in English hands 1206-1224, add a 1206 loss and a 1224 gain against kingdom-of-england (or start the state at the 1225 apanage); otherwise record the disagreement in notes. Non-blocking (page budget).

Gaps for a gap-filler:
- `/keyframe_review/2`: The 1241 Cliopatria change: Alphonse's investiture with Poitou in 1241 and the Saintonge War of 1242 (named on the County of Poitou page without dates; not entered as a war). Try https://en.wikipedia.org/wiki/Saintonge_War
- `/ledger/0`: Who held Poitou 1206-1224 (Angevin recovery after the 1206 truce; Louis VIII's 1224 conquest). Try https://en.wikipedia.org/wiki/Louis_VIII_of_France

Spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed; `/ledger/2 (month)` confirmed.
Area: infobox None, Cliopatria 23634, ratio None. County of Poitou infobox has no area (established 778, merged with the crown 1416). Corrected region Poitou (Vendee, Deux-Sevres, Vienne) is about 19,700 km2; the Cliopatria polygon includes Charente, as the author says.

## county-of-auvergne: fail

Findings:
- `/keyframe_review/8 to /keyframe_review/12; /ledger/5, /ledger/6, /ledger/8; /identity/successors/0` (to do): From 1360 to 1415 the dossier merges John of Berry's Duchy of Auvergne (the Terre royale) into the County of Auvergne by a 1360 gain from kingdom-of-france and a 1416 loss to house-of-bourbon, drawing the whole Cliopatria block (19,677 km2) where the county held only the Vic-le-Comte remnant plus Boulogne (about 3,500 km2): a wrong shape for 56 years, a factor of about 5.6 in area. Evidence: Duchy of Auvergne page (cited by the dossier): 'In 1356, King John II of France made the Terre d'Auvergne a Duchy ... while the County of Auvergne continued to exist in parallel'; Joan I page: 'Successor: Philip of Rouvres' (the county did not pass to Berry); the dossier's own /ledger/7 note: Marie I, Countess of Auvergne, 'is not Marie, daughter of Berry and Duchess of Auvergne'. kingdom-of-france /ledger/41 gives the 1360 land to 'Duchy of Berry (John, Duke of Berry's apanage)' and lists that duchy as needing a dossier; house-of-bourbon /ledger/7 takes it in 1416 from 'Duchy of Auvergne (John, Duke of Berry)'. Fix: Delete /ledger/6 (1360 gain) and /ledger/8 (1416 loss); make /ledger/5 a rename for the 1360 succession of Philip of Rouvres (Joan I page) or delete it; set /keyframe_review/8, 9, 10, 11 and 12 to verdict adjust with correction {union: [{intersect: [{cliopatria: County of Auvergne, year: 1402}, {place: Vic-le-Comte, km: 30}]}, {cliopatria: County of Auvergne, year: 1440}]} (as /keyframe_review/13), noting that the rest of the block is the Duchy of Berry and Auvergne; remove the house-of-bourbon successor (the remnant's successor is kingdom-of-france only); list 'Duchy of Berry and Auvergne (apanage of John, Duke of Berry), 1360-1416' under counterparts_needing_dossiers. Blocking.
- `/identity/capitals/0` (to do): Riom is the count's capital 1206-1212 although the dossier's own /ledger/1 has Riom occupied by Philip II through 1213. Evidence: Duchy of Auvergne page: 'the French King Philip Augustus occupied part of Auvergne (including the capital Riom) in 1195'. Fix: Start Vic-le-Comte in 1206 (or say in the note that Riom was the count's seat only in name after 1195).
- `/wars/0/from` (applied by reviewer): War began in 1195, outside the life (start 1206). Evidence: Duchy of Auvergne page: Philip Augustus 'occupied part of Auvergne (including the capital Riom) in 1195'; brief section 2.2 requires wars inside the life. Fix: Set from to 1206 and keep 1195 in the note. Applied by the reviewer; the dossier re-validates with 0 errors, 0 warnings.
- `/keyframe_review/9/note` (to do): Says 'The Auvergne page has no infobox and no area'; the page's infobox gives 26,013 km2. Evidence: Auvergne page infobox: 'Total: 26,013 km2' and 'Auvergne is generally regarded as conterminous with the land area of the historical Province of Auvergne'. Against the 1363 shape (19,677 km2) the ratio is 1.32, within a factor of two. Fix: Quote the infobox figure in the note when the keyframe is rewritten. Non-blocking.

Gaps for a gap-filler:
- `/ledger/4`: How and when Boulogne came to the counts of Auvergne (Cliopatria 1260; confidence 1). Try https://en.wikipedia.org/wiki/Robert_V,_Count_of_Auvergne
- `/ledger/11`: What happened to the remnant and Lauragais in 1501 (confidence 1; the Boulogne page has Anne holding the lands to 1524). Try https://en.wikipedia.org/wiki/John_III,_Count_of_Auvergne
- `/ledger/0`: Founding (confidence 1, Cliopatria's first year) and the boundary of the count's remnant after 1213 (a 30 km radius of the author's). Try https://fr.wikipedia.org/wiki/Comt%C3%A9_d%27Auvergne

Spot checks: `/ledger/3` confirmed; `/ledger/3 (Vic-le-Comte)` confirmed; `/ledger/5` confirmed (the year), but 'it' is Alphonse's appanage, the royal land; the Duchy page says the county continued in parallel; `/ledger/9` confirmed; `/ledger/10` confirmed.
Area: infobox 26013, Cliopatria 19677, ratio 1.32. Infobox is the modern region, conterminous with the province; within a factor of two. The real area problem is 1360-1415 (fix 1).

## county-of-armagnac: thin

Findings:
- `/ledger/9; /keyframe_review/7` (to do): The Bigorre (Hautes-Pyrenees) cells are gained in 1385 from 'unknown: pages silent', but two neighbour dossiers have Gaston Febus holding Bigorre 1379-1390 and ceding it to the crown on 5 January 1390. Evidence: county-of-foix /ledger/6-7 and county-of-bearn /ledger/1-2 (c3/c2); county-of-foix /ledger/10 quotes the Bigorre page: 'In 1407, it belonged to Bernard VII of Armagnac, who sold it that year to John I, Count of Foix'. Fix: Move the Bigorre gain to 1390 or later with counterpart kingdom-of-france, and adjust /keyframe_review/7 to leave Bigorre out until then; or keep 1385 and say in notes that it conflicts with foix and bearn. Non-blocking (confidence 1, flagged in the author's notes).
- `/ledger/2; /ledger/3` (to do): The whole county is 'lost' to kingdom-of-england in 1360 and 'regained' in 1369, though the count kept ruling; the Brétigny page does not list Armagnac. Evidence: Armagnac page: 'the southern part of France, including Armagnac, was ceded to England by the Treaty of Brétigny (1360)' and 'the count of Armagnac appealed to the French king for help in 1369'; Treaty of Brétigny page lists 'Guyenne, Gascony, Poitou, Saintonge and Aunis, Agenais, Périgord, Limousin, Quercy, Bigorre ... Rouergue', not Armagnac. Fix: Keep (it follows the page and Cliopatria's 1363-1374 gap), but the orchestrator should decide one convention for Brétigny fiefs across county-of-armagnac, county-of-perigord and duchy-of-aquitaine (loss to kingdom-of-england here; gain by duchy-of-aquitaine from kingdom-of-france there); vassal_start/vassal_end with duchy-of-aquitaine would keep the count's colour. Non-blocking.

Gaps for a gap-filler:
- `/ledger/4 to /ledger/7`: Real dates of the Rodez, Lomagne-Auvillars, Lot and Charolais acquisitions (the page credits Jean I, 1319-1373, and his successors; 1375 is Cliopatria's year, confidence 1); Carlat is on the page but in no shape. Try https://en.wikipedia.org/wiki/John_I,_Count_of_Armagnac
- `/ledger/8`: The 1385 loss of Lot and Tarn-et-Garonne cells (confidence 1, counterpart unknown). Try https://en.wikipedia.org/wiki/John_II,_Count_of_Armagnac
- `/ledger/13`: What became of Comminges after 1418 (confidence 1). Try https://en.wikipedia.org/wiki/County_of_Comminges
- `/ledger/15`: Louis XI's confiscation after the 1473 siege and the restoration of the line before 1497: the ledger has only the contest. Try https://en.wikipedia.org/wiki/John_V,_Count_of_Armagnac

Spot checks: `/ledger/1` confirmed; `/ledger/2` confirmed; `/ledger/12` confirmed; `/ledger/14` confirmed; `/ledger/16` confirmed.
Area: infobox None, Cliopatria 23633, ratio None. No infobox area (capital Auch, created before 960); the author reads the shapes by gazetteer cells.

## county-of-perigord: thin

Findings:
- `/ledger/1; /ledger/4` (to do): Brétigny loss (1360) and return (1378) name kingdom-of-england, but duchy-of-aquitaine draws the same Dordogne land as its 1360 gain from kingdom-of-france and its 1377 loss to kingdom-of-france. Evidence: Treaty of Brétigny page names Périgord among the lands Edward III was 'to hold these free and clear, without doing homage', ratified at Calais 24 October 1360; duchy-of-aquitaine /ledger/18 and /ledger/22. Fix: Orchestrator to fix one convention with county-of-armagnac and duchy-of-aquitaine; if duchy-of-aquitaine keeps drawing the Brétigny lands, set the counterpart of /ledger/1 and /ledger/4 to duchy-of-aquitaine and align 1378 with 1377 (or vice versa). Non-blocking.
- `/ledger/8` (to do): Dissolve to county-of-foix in 1481; county-of-foix has the matching gain in 1484. Evidence: county-of-foix /ledger/15 (1484, quoting the House of Albret page: 'In 1470, they inherited the County of Périgord and the Viscounty of Limoges'). Fix: Align the year with county-of-foix (or say which page gives 1481); confidence stays 1 until a page is opened. Non-blocking.
- `/keyframe_review/2; /keyframe_review/4` (to do): The ledger leaves the county landless from October 1360 and in 1398-1399, inside the spans of the 1333..1362 and 1385..1401 shapes, which stay adjusted to the whole Dordogne. Evidence: /ledger/1 (1360 loss), /ledger/5 (1398 loss), /ledger/6 (1400 gain). Fix: Say in both keyframe notes that the correction holds only to 1360 and to 1397. Non-blocking.

Gaps for a gap-filler:
- `/keyframe_review/6`: The 1440 doubling of the shape (8,593 to 18,176 km2, adding Correze and Haute-Vienne) has no event; probably the county joined to the Viscounty of Limoges under a new holder after the Orleans (1437?). Try https://en.wikipedia.org/wiki/Viscounty_of_Limoges
- `/ledger/8`: Holders 1408-1481 and the handover to the Albrets (confidence 1). Try https://en.wikipedia.org/wiki/Alain_I_of_Albret
- `/ledger/0`: Founding (confidence 1, Cliopatria's first year); the counts (list pages failed for the author). Try https://en.wikipedia.org/wiki/P%C3%A9rigord

Spot checks: `/ledger/1` confirmed; `/ledger/5` confirmed; `/ledger/6` confirmed; `/ledger/7` confirmed.
Area: infobox None, Cliopatria 18223, ratio None. County of Perigord page has no infobox; the Dordogne is about 9,060 km2 against Cliopatria's 8,593-12,105 km2 before 1440.

## county-of-touraine: fail

Findings:
- `/keyframe_review/0 to /keyframe_review/9; /ledger/0, /ledger/2, /ledger/6, /ledger/7` (to do): The dossier draws Touraine as a separate state for all of 1205-1491, but its own pages put the duchy in the crown's hands for most of those years and the kingdom-of-france dossier draws the same land: the corrections give the royal domain to this state (about 250 of 286 years overlap kingdom-of-france), and the hand-backs to the crown are coded as renames. Evidence: Philip the Bold page: 'He was created Duke of Touraine in 1360, but in 1363, he returned this duchy to the crown' (coded as rename /ledger/2); Charles VII infobox: 'Duke of Touraine Count of Poitou 1417 - 21 October 1422: Vacant Merged in the crown' (rename /ledger/6); Touraine page: 'In 1205, Philip II Augustus of France regained Touraine' and 'At this time, Touraine was made into a royal duchy'. kingdom-of-france /ledger/16 gains Touraine in 1204 from angevin-empire and /ledger/44 loses it to county-of-touraine only in 1361; house-of-valois-anjou /ledger/2 gains it from county-of-touraine in 1370. Fix: Draw the state only while an apanage holder had it: gain from kingdom-of-france 1360 (Philip), loss to kingdom-of-france 1363, gain 1386 and loss 1392 (Louis of Orléans), gain 1417 and dissolve or loss into the crown 21 October 1422, with the Louis of Anjou years (1370-) left to house-of-valois-anjou or mirrored as a loss; mark the Cliopatria keyframes wrong with no correction outside those spans, and make the 1205 'found' the 1360 apanage (or 1205 only if the orchestrator rules the royal duchy a separate state, in which case kingdom-of-france must drop Touraine). Orchestrator: also decide whether the Cliopatria row, which is geometrically La Marche (bbox 0.90-2.60 E, 45.56-46.55 N in shapes.csv), should become the county-of-la-marche dossier. Blocking.
- `/wars/0` (to do): A treaty with no zones is entered as a war. Evidence: Hundred Years' War page: Edward renounced Normandy, Touraine, Anjou and Maine at Brétigny; no fighting in Touraine is cited. Fix: Drop it or move the sentence to notes. Non-blocking.

Gaps for a gap-filler:
- `/ledger/7`: Any page for the 1491 end (confidence 1; the Touraine page says the royal duchy became a province in 1584). Try https://en.wikipedia.org/wiki/Touraine
- `/ledger/2`: Holders 1363-1386 (Louis I of Anjou, duke of Touraine from 1370, per house-of-valois-anjou), 1392-1417 and 1422-1491 (Archibald Douglas 1423-24, Margaret of Scotland's dower). Try https://en.wikipedia.org/wiki/Louis_I,_Duke_of_Anjou

Spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed (year), but the page says the duchy was returned to the crown, coded as a rename; `/ledger/5; /ledger/6` confirmed (years), but the infobox says 'Merged in the crown', coded as a rename.
Area: infobox None, Cliopatria 10300, ratio None. Touraine page has no area. Verified in shapes.csv: every County of Touraine shape has bbox from 0.90 E, 45.56 N, about 150 km south-east of Tours (47.39 N); the author's 'wrong place' finding stands.

## Cross-dossier matrix

- county-of-poitou 1205 found (angevin-empire) / none: **exception**. angevin-empire not written (eu-11, not run); kingdom-of-france 1204 gain from angevin-empire says 'Poitou temporarily'.
- county-of-poitou 1271 dissolve (kingdom-of-france) / kingdom-of-france 1271 gain: **mismatch**. France's 1271 gain names 'Alfonso, Count of Poitou (apanage)', not the slug; France also has a 1250 gain from county-of-poitou (c1) with no loss here. Fix on the France side.
- kingdom-of-france 1224 gain (kingdom-of-england) / county-of-poitou None None: **mismatch**. France conquers Poitou from England in 1224 (Louis VIII page) while county-of-poitou holds Poitou as French from 1205.
- county-of-auvergne 1206 occupation_start (kingdom-of-france) / kingdom-of-france None None: **missing**. No occupation of Riom (1195-1213) in kingdom-of-france.
- county-of-auvergne 1213 loss (kingdom-of-france) / kingdom-of-france None None: **missing**. No 1213 gain of the Terre royale d'Auvergne in kingdom-of-france (Duchy of Auvergne page dates it 1213).
- county-of-auvergne 1260 gain (county-of-boulogne) / none: **exception**. county-of-boulogne is owned by another eu-10 part and not written yet.
- county-of-auvergne 1360 gain (kingdom-of-france) / kingdom-of-france 1360 loss: **mismatch**. France gives the land to 'Duchy of Berry (John, Duke of Berry's apanage)', a separate state needing a dossier; the Duchy page says the county continued in parallel. Fix here (Auvergne fix 1).
- county-of-auvergne 1416 loss (house-of-bourbon) / house-of-bourbon 1416 gain: **mismatch**. Bourbon's gain names 'Duchy of Auvergne (John, Duke of Berry)', not the county. Fix here (Auvergne fix 1).
- county-of-auvergne 1477 loss (kingdom-of-france) / kingdom-of-france None None: **missing**. No 1477 gain of Boulogne in kingdom-of-france (County of Boulogne page: 'annexed to the royal domain itself in 1477').
- county-of-auvergne 1477 gain (kingdom-of-france) / kingdom-of-france None None: **missing**. No 1477 loss of the Lauragais in kingdom-of-france.
- county-of-auvergne 1501 dissolve (kingdom-of-france) / kingdom-of-france None None: **missing**. No 1501 gain in kingdom-of-france (confidence 1 here).
- county-of-armagnac 1360 loss (kingdom-of-england) / none: **exception**. kingdom-of-england not written (eu-11). duchy-of-aquitaine 1360 gain lists Gers inside a union minus Gascony; convention to settle (Armagnac fix 2).
- county-of-armagnac 1369 gain (kingdom-of-england) / none: **exception**. kingdom-of-england not written (eu-11).
- county-of-armagnac 1375 gain (County of Rodez) / none: **exception**. Listed by the author under counterparts_needing_dossiers.
- county-of-armagnac 1375 gain (Viscounties of Lomagne and Auvillars) / none: **exception**. Listed by the author under counterparts_needing_dossiers.
- county-of-armagnac 1375 gain (unknown: pages silent) / none: **missing**. Lot cells, confidence 1; no counterpart.
- county-of-armagnac 1375 gain (County of Charolais) / none: **exception**. Listed by the author under counterparts_needing_dossiers.
- county-of-armagnac 1385 loss (unknown: pages silent) / none: **missing**. Lot and Tarn-et-Garonne cells, confidence 1.
- county-of-armagnac 1385 gain (unknown: pages silent) / county-of-foix 1390 loss: **mismatch**. Bigorre: county-of-foix and county-of-bearn have Febus holding it 1379-1390 and ceding it to the crown in January 1390; Armagnac gains it in 1385.
- county-of-armagnac 1390 loss (duchy-of-burgundy) / none: **exception**. duchy-of-burgundy owned by another eu-10 part, not written yet.
- county-of-armagnac 1407 loss (county-of-foix) / county-of-foix 1407 gain: **matched**. county-of-bearn also has the 1407 gain from 'Bernard VII, Count of Armagnac (holder of Bigorre)'.
- county-of-armagnac 1412 gain (County of Comminges) / none: **exception**. Listed by the author under counterparts_needing_dossiers.
- county-of-armagnac 1418 loss (unknown: page silent) / none: **missing**. Comminges after Bernard VII's death, confidence 1.
- county-of-armagnac 1497 dissolve (kingdom-of-france) / kingdom-of-france None None: **missing**. No 1497 gain of Armagnac in kingdom-of-france.
- county-of-perigord 1360 loss (kingdom-of-england) / duchy-of-aquitaine 1360 gain: **mismatch**. duchy-of-aquitaine gains the Dordogne in 1360 from kingdom-of-france; kingdom-of-england not written.
- county-of-perigord 1378 gain (kingdom-of-england) / duchy-of-aquitaine 1377 loss: **mismatch**. duchy-of-aquitaine loses the Brétigny lands to kingdom-of-france in 1377.
- county-of-perigord 1398 loss (kingdom-of-france) / kingdom-of-france None None: **missing**. No 1398 gain of Perigord in kingdom-of-france.
- county-of-perigord 1400 gain (kingdom-of-france) / kingdom-of-france None None: **missing**. No 1400 loss in kingdom-of-france (grant to Louis of Orleans).
- county-of-perigord 1481 dissolve (county-of-foix) / county-of-foix 1484 gain: **mismatch**. Three years apart; foix quotes the House of Albret page (inherited 1470).
- duchy-of-aquitaine 1259 gain (kingdom-of-france) / county-of-perigord None None: **mismatch**. Aquitaine draws the Dordogne 1259-1324 (Treaty of Paris, Perigueux) while county-of-perigord holds it throughout; suzerainty versus domain, orchestrator to settle.
- kingdom-of-france 1224 gain (kingdom-of-england) / county-of-perigord None None: **mismatch**. France's 1224 conquest region includes the Dordogne, which county-of-perigord holds from 1206.
- county-of-touraine 1205 found (angevin-empire) / kingdom-of-france 1204 gain: **mismatch**. Both kingdom-of-france (1204) and county-of-touraine (1205) take Touraine from the Angevins; angevin-empire not written.
- kingdom-of-france 1250 loss (capetian-house-of-anjou) / county-of-touraine None None: **mismatch**. France loses Touraine to capetian-house-of-anjou (c1) while county-of-touraine holds it; capetian-house-of-anjou has no Touraine gain.
- kingdom-of-france 1361 loss (county-of-touraine) / county-of-touraine 1360 rename: **mismatch**. No gain in county-of-touraine, which already holds the land; Philip the Bold page gives 1360.
- house-of-valois-anjou 1370 gain (county-of-touraine) / county-of-touraine None None: **missing**. No 1370 loss to house-of-valois-anjou in county-of-touraine.
- county-of-touraine 1491 dissolve (kingdom-of-france) / kingdom-of-france None None: **missing**. No 1491 gain in kingdom-of-france; confidence 1.

## Counterparts needing dossiers

- County of La Marche (`county-of-la-marche`, 1206-1491): Cliopatria's 'County of Touraine' polygons are La Marche (verified bbox); without it the land is stateless.
- Duchy of Berry and Auvergne (apanage of John, Duke of Berry) (`duchy-of-berry`, 1360-1416): kingdom-of-france 1360 loss and house-of-bourbon 1416 gain already name it; county-of-auvergne must stop carrying it.
- County of Charolais (`county-of-charolais`, 1314-1493)
- County of Comminges (`county-of-comminges`, 1412-1418)
- County of Rodez (`county-of-rodez`, 1375-1497)
- Viscounties of Lomagne and Auvillars (`viscounty-of-lomagne`, 1375-1384)

## Problems

- No page failed for the reviewer; 15 Wikipedia pages opened, 22 events spot-checked, all confirmed in year (none fabricated); two (Touraine /ledger/2, /ledger/6) confirmed in year but coded as renames where the page says the duchy went back to the crown.
- Neighbour dossiers not yet written (counted as exceptions): kingdom-of-england, angevin-empire (eu-11); county-of-boulogne, duchy-of-burgundy (other eu-10 parts).
- Cross-dossier conventions the orchestrator must fix for group eu-10: (1) Brétigny fiefs (county-of-armagnac and county-of-perigord lose to kingdom-of-england; duchy-of-aquitaine gains the same land from kingdom-of-france); (2) royal-domain land versus apanage polities (county-of-touraine, county-of-poitou 1205-1225, the Duchy of Berry and Auvergne) overlapping kingdom-of-france.
- Reviewer applied one fix: county-of-auvergne /wars/0/from 1195 to 1206 (note keeps 1195); re-validated with 0 errors, 0 warnings.
