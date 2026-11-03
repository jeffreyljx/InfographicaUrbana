# Review of am-06-b (spanish-empire)

Reviewer, 2026-10-19. Verdict: **fail** (back to the author).

No fabricated or mis-dated event found: 15 events checked on 6 pages plus the infobox area, all confirmed. Returned to the author for missing and inconsistent land events. Blocking: (1) the 1873/1877 corrections drop Fernando Po, Annobon and Ifni with no event; (2) the 1898 dissolve gives the Pacific islands to the US against the dossier's own note; (3) the Inca conquest after 1535 has no mirror for inca-empire's 1537, 1567-1571 and 1572 events. Also to fix: Michoacan dated 1530 by its dossier, Colonia and southern Brazil events, Annobon, Philippine certainty. One fix applied by the reviewer (Muisca slug).

Mechanical: validator 0 errors, 1 warning (place 'Sidi Ifni'); 76/76 Cliopatria shapes reviewed, 9 new keyframes with from/to/correction; ledger in order, found 1516, dissolve 1898-12; every contest paired and matched to a war.

## Findings (fixes)

- **/ledger/11/counterpart** (applied by reviewer): Counterpart was the free-text name 'Muisca Confederation' although the dossier history/polities/muisca-confederation.json now exists (its successors name spanish-empire and its 1538-08 loss mirrors this gain).
  - Why: history/polities/muisca-confederation.json identity.slug = 'muisca-confederation'; its /ledger/5 is a 1538-08 loss to spanish-empire.
  - Fix: counterpart 'muisca-confederation' (applied by the reviewer; re-validated: 0 errors, 1 warning Sidi Ifni). Drop Muisca from counterparts_needing_dossiers.
- **/keyframe_review/84/correction (spanish-empire_1873), /keyframe_review/75/correction (spanish-empire_1877), /ledger/96/region, /identity/successors** (author to do): The 1873 and 1877 corrections are seven countries (Philippines, Cuba, Puerto Rico, Guam, Northern Marianas, Micronesia, Palau) and silently drop Fernando Po/Annobon and Ifni, which this dossier gains in /ledger/46 (1778) and /ledger/85 (1860) and which its own 1861 and 1865 keyframes keep; no loss event and no successor carries them.
  - Why: keyframe 1861 note: '+4 Morocco cells (Sidi Ifni ...)'; 1865 correction = Cliopatria 1861 minus the Dominican Republic (keeps the 8 Equatorial Guinea and 4 Ifni cells); 1873 correction has no Morocco or Equatorial Guinea; /ledger/96 note: 'Spanish Africa lasted to 1976 and belongs to kingdom-of-spain'. Spanish Empire page (opened): Fernando Po 'ceded to Spain by the Portuguese in exchange for territory in South America'; 'ceded Sidi Ifni to Spain as a part of the Treaty of Tangiers'.
  - Fix: Add {"intersect":[{"cliopatria":"Spanish Empire","year":1861},{"union":[{"country":"Equatorial Guinea"},{"country":"Morocco"}]}]} to the union of both corrections (text: 'Fernando Po, Annobon and Ifni'), and add a successor kingdom-of-spain with that land (or a dated hand-over event) so the African posts pass on at the end instead of vanishing in 1873.
- **/ledger/96 (dissolve)** (author to do): The dissolve gives the Carolines, Palau and the Northern Marianas to united-states-of-america at confidence 3, contradicting its own note and identity.successors, which give them to german-empire on 12 February 1899; its region also repeats Cuba, Puerto Rico, Guam and the Philippines already lost in /ledger/94-95.
  - Why: /ledger/96 note: "'Sale of the remaining islands to Germany: 12 February 1899' (East Indies page)"; /identity/successors/2 = german-empire, 'sold on 12 February 1899'; keyframe 1873 note: Spain holds the Carolines '(1686-1899)' and Palau '(1574-1899)'.
  - Fix: Either end the dossier on 1899-02 (end.year 1899, month 2) with a 1899-02 loss to german-empire of {Micronesia, Palau, Northern Mariana Islands} (Spanish East Indies page) and the dissolve at 1899, or keep 1898-12 and make the dissolve's region and counterpart describe only what passes to whom (the Pacific islands are then Spanish beyond the end and must be said so in notes). Do not leave the US as the counterpart for the German sale.
- **/keyframe_review/5 (spanish-empire_1540), /ledger/7-/ledger/10** (author to do): The conquest of the Inca lands is not mirrored: the 1540 keyframe adds 9,348 cells (about 2.5 M km2: Peru, Bolivia, northern Chile, NW Argentina, Ecuador) that the ledger explains only by city radii (Cuzco 250 km, Quito 150 km, Lima 120 km), while inca-empire's ledger records the loss to spanish-empire of 'the empire outside the Neo-Inca state' in 1537, a vassal_start 1567 / vassal_end 1571 and the 1572-06 loss and dissolve of the Neo-Inca State, none of which has a mirror here.
  - Why: history/polities/inca-empire.json /ledger/23 (1537 loss, region minus Inca 1534 / Inca 1540), /ledger/26-27 (vassal 1567-1571), /ledger/28-29 (1572-06 loss, dissolve, c3). Spanish /wars/1 runs 1532-1572 but the ledger stops at 1535 for the Inca.
  - Fix: Add a 1537 gain from inca-empire with region {"minus":[{"cliopatria":"Inca Empire","year":1534},{"cliopatria":"Inca Empire","year":1540}]}; vassal_start 1567 and vassal_end 1571 of inca-empire (Neo-Inca State, region {"cliopatria":"Inca Empire","year":1564}); a 1572-06 gain from inca-empire of the same region; cite a page (Spanish conquest of the Inca Empire or Neo-Inca State) and mark the 1540 keyframe adjust if the Bolivian/Argentine reach stays claim.
- **/ledger/9** (author to do): Michoacan is gained in 1534 at confidence 1 (Cliopatria's year) although the michoacan dossier dates the Spanish takeover to 14 February 1530 at confidence 3 from a page: a four-year mismatch.
  - Why: history/polities/michoacan.json /ledger/13-14: 1530-02 loss and dissolve to spanish-empire, source https://en.wikipedia.org/wiki/Michoac%C3%A1n ('killed Tanganxoan II in 1530'). Spanish colonization of the Americas (opened by the reviewer) names 'the conquest of the Purepecha of Michoacan' with no date, so the current source does not support any year.
  - Fix: Move the event to 1530, month 2, source https://en.wikipedia.org/wiki/Michoac%C3%A1n (add to sources after opening it), confidence 2 or 3 as the page supports; mark keyframe spanish-empire_1529 adjust (add the Michoacan row's 1529 shape from 1530).
- **/ledger (1680-1777), /keyframe_review/44 note, /keyframe_review/45 note** (author to do): Colonia del Sacramento and the southern Brazil frontier change hands repeatedly with no ledger event here: the 1762 keyframe note has Colonia 'in (Uruguay +32)' and the 1763 note has it leave, and portuguese-empire records the 1706 loss and 1713 gain of Colonia, the 1762 loss and 1763 gain, and two 1777-10 gains from spanish-empire (Santa Catarina; Rio Grande do Sul outside the missions).
  - Why: portuguese-empire.json /ledger/46, 47, 60, 61, 65, 66 (counterpart spanish-empire). First Treaty of San Ildefonso (opened): Spain 'returned Santa Catarina island' and 'acknowledged Portuguese control of Southern Brazil'.
  - Fix: Add gain 1705/1706 and loss 1713/1715 (Utrecht) of {place Colonia del Sacramento, 25 km}; gain 1762 (Cevallos) and loss 1763 (Paris) of Colonia; gain 1763 and loss 1776 of Rio Grande (Vila do Rio Grande) and gain 1777-02 / loss 1777-10 of Santa Catarina island, each with a page (Colonia del Sacramento; First Treaty of San Ildefonso).
- **/ledger/20, /ledger/24, /keyframe_review/11 note, notes** (author to do): The Iberian Union is a vassal_start/vassal_end of portuguese-empire here but a loss (1581) and gain (1640-12) to spanish-empire in the portuguese-empire dossier; the author's notes say the two dossiers match, which is true of the dates only.
  - Why: portuguese-empire.json /ledger/25 (1581 loss to spanish-empire) and /ledger/26 (1640-12 gain from spanish-empire); this dossier's 1582 keyframe note itself says 'portuguese-empire's ledger records the same lands as a loss'. Iberian Union page (opened): 'Spain left the administration of Portugal and its empire largely to the Portuguese themselves'.
  - Fix: Orchestrator to choose one representation for both dossiers (the page supports the personal-union tint, i.e. vassal events on both sides); correct the sentence in the notes.
- **/ledger/46/region** (author to do): The region is {place Malabo, 60 km}, which covers Bioko only, while the text says 'Fernando Po (Bioko) and Annobon'; the mirror in portuguese-empire has both islands and month 3 (Treaty of El Pardo, March 1778).
  - Why: portuguese-empire.json /ledger/68: 1778-03 loss, union of admin1 Annobon and Bioko Norte/Sur; Spanish Empire page (opened) places the cession in the Treaty of El Pardo.
  - Fix: Region union [{place Malabo, 60 km}, {admin1 'Annobón', country Equatorial Guinea}] and month 3 once a page gives the month.
- **/certainty/2, /keyframe_review/84/correction** (author to do): 1826-1898 is 'sharp' and the 1873 correction is the whole Philippines although the author's note says the pages do not say how far Spanish control reached inland, and the Sulu sultanate (Cliopatria row to 1879) was outside Spanish rule until the 1876 capture of Jolo and the 1878 protectorate.
  - Why: /certainty/2 note: 'the pages opened do not describe how far Spanish control reached inland in the Philippines'; polities.csv sultanate-of-sulu 1459..1879 overlaps the 1873 correction 1873-1879.
  - Fix: Level 'soft' for the Philippine interior (or split the band), and either remove the Sulu Archipelago from the 1873 correction until 1878 with a vassal_start of sultanate-of-sulu, or say in the note that it overlaps the Sulu row.

## Thin (for a gap-filler)

- /keyframe_review/42 (spanish-empire_1752): +8,864 cells (2.2 M km2: western Amazon, Beni, Santa Cruz, Bolivar, Meta, the northern Chaco) with no event; author: 'probably a change of Cliopatria's source map'. It runs opposite to portuguese-empire's 1750-01 gain from spanish-empire of the Brazilian interior (Treaty of Madrid). Try https://en.wikipedia.org/wiki/Treaty_of_Madrid_(13_January_1750)
- /keyframe_review/50 (spanish-empire_1778): Amazon block of 4,591 cells (1.2 M km2) unverified; portuguese-empire records a 1778 gain of the western Amazon from spanish-empire (c1), so the two dossiers draw the same land on opposite sides. Try https://en.wikipedia.org/wiki/First_Treaty_of_San_Ildefonso
- /ledger/9: Michoacan, confidence 1 (see fix: 1530). Try https://en.wikipedia.org/wiki/Michoac%C3%A1n
- /ledger/13: Yucatan 1547 confidence 1; later-mayan-city-states dates the end of the conquest to 1546 at confidence 3. Try https://en.wikipedia.org/wiki/Spanish_conquest_of_Yucat%C3%A1n
- /ledger/37, /ledger/40: British occupation of Havana 1762-1763, confidence 1, no month. Try https://en.wikipedia.org/wiki/Siege_of_Havana
- /ledger/52: Trinidad 1797, confidence 1. Try https://en.wikipedia.org/wiki/Invasion_of_Trinidad_(1797)
- /ledger/65, /ledger/66: Venezuela 1812 and 1814, confidence 1 (First and Second Republic fall). Try https://en.wikipedia.org/wiki/Venezuelan_War_of_Independence
- /keyframe_review/0 note; ledger 1516-1792: North African presidios in the shapes (Algeria 12, Libya 2 cells: Oran, Tripoli) with no events (Tripoli to the Knights 1530, Oran lost 1708, regained 1732, given up 1792). Try https://en.wikipedia.org/wiki/Plazas_de_soberan%C3%ADa
- /wars, /ledger 1859-1898: Wars and events of the late empire: the Philippine Revolution 1896-1898 (contest on Luzon, declaration 12 June 1898), the Hispano-Moroccan War 1859-1860 behind /ledger/85, the Chincha Islands War 1864-1866 (occupation of the Chincha Islands), Jolo 1876 and the Sulu protectorate 1878. Try https://en.wikipedia.org/wiki/Philippine_Revolution
- /keyframe_review/9, 24, 25, 28: Blocks of cells in shapes 1572 (Caracas coast), 1659 (Arauca/Casanare, Chihuahua), 1670 (Caribbean Nicaragua/Honduras) and 1687 (Sonora, Chihuahua) unverified: page budget. Try https://en.wikipedia.org/wiki/Spanish_missions_in_Mexico
- /keyframe_review/53-/keyframe_review/69: Northern frontier of New Spain and the western Adams-Onis line (author's gap). Try https://en.wikipedia.org/wiki/Adams%E2%80%93On%C3%ADs_Treaty
- /ledger (1529, 1606-1663): Moluccas: the 1529 Treaty of Zaragoza (portuguese-empire records a gain from spanish-empire) and Spanish Ternate/Tidore 1606-1663. Try https://en.wikipedia.org/wiki/Treaty_of_Zaragoza

## Spot checks

- /ledger/77: confirmed: 'Declaration of Independence: 28 September 1821'; 'At its conclusion in 1821, the viceroyalty was dissolved and the Mexican Empire was established' (https://en.wikipedia.org/wiki/New_Spain)
- /ledger/28: confirmed: 'Pueblo Revolt in 1680, expelling the Spanish, who retreated to Paso del Norte'; 'the return of the Spanish in 1692' (https://en.wikipedia.org/wiki/New_Spain)
- /ledger/20: confirmed: 'recognized as king by the Cortes of Tomar in 1581'; separate administration quoted correctly (https://en.wikipedia.org/wiki/Iberian_Union)
- /ledger/39: confirmed: infobox 'Transfer by France: 23 November 1762' (https://en.wikipedia.org/wiki/Louisiana_(New_Spain))
- /ledger/55: confirmed: transfer 'at the Cabildo in New Orleans on 30 November 1803' (infobox also has 'Returned to France: 21 March 1801'; de facto date used, acceptable) (https://en.wikipedia.org/wiki/Louisiana_(New_Spain))
- /ledger/80: confirmed: Ayacucho 9 December 1824 (https://en.wikipedia.org/wiki/Spanish_American_wars_of_independence)
- /ledger/71, /ledger/82: confirmed: 'By 10 February, San Martin had control of northern and central Chile'; Olaneta 'died in Tumusla on 2 April 1825' (https://en.wikipedia.org/wiki/Spanish_American_wars_of_independence)
- /ledger/17: confirmed: 'conquest of Chiloe Archipelago in 1567' (region Ancud 100 km is approximate) (https://en.wikipedia.org/wiki/Spanish_colonization_of_the_Americas)
- /ledger/21: confirmed: New Mexico 'starting in 1598' (https://en.wikipedia.org/wiki/Spanish_colonization_of_the_Americas)
- /ledger/9: not on page (no date for Michoacan; honest at confidence 1, but see fix) (https://en.wikipedia.org/wiki/Spanish_colonization_of_the_Americas)
- /ledger/45, /ledger/53: confirmed: 1 October 1777 cessions; 'Portugal regained the Misiones Orientales in the Treaty of Badajoz (1801)' (https://en.wikipedia.org/wiki/First_Treaty_of_San_Ildefonso)
- /ledger/46, /ledger/85: confirmed: Fernando Po ceded 'in exchange for territory in South America' (El Pardo); 'ceded Sidi Ifni to Spain as a part of the Treaty of Tangiers' (https://en.wikipedia.org/wiki/Spanish_Empire)

## Area

Infobox 13,700,000 km2 (1780) against Cliopatria spanish-empire_1780 11.01 M km2: ratio 0.80, acknowledged. Shape spanish-empire_1780 = 11.01 M km2; acknowledged in the 1778 keyframe note. New Spain page 7,657,000 km2 (1790) confirmed; the sub-unit ratio 0.32 is acknowledged in the 1788 keyframe note and the author's notes.

## Cross-dossier matrix

- spanish-empire 1521 gain (aztec-triple-alliance) -> aztec-triple-alliance 1521 loss: **matched**. /ledger/2 1521-08 vs aztec-triple-alliance /ledger/34-35 1521-08 loss and dissolve.
- spanish-empire 1524 gain (later-mayan-city-states) -> later-mayan-city-states 1525 loss: **matched**. /ledger/3 Guatemala vs later-mayan-city-states /ledger/4 (1525).
- later-mayan-city-states 1529 loss (spanish-empire) -> none: **missing**. later-mayan-city-states /ledger/6 (c1, small) has no mirror in spanish-empire.
- spanish-empire 1547 gain (later-mayan-city-states) -> later-mayan-city-states 1546 loss: **matched**. /ledger/13 (c1) vs later-mayan-city-states /ledger/10-11 (1546, c3); spanish-empire could adopt 1546.
- spanish-empire 1534 gain (inca-empire) -> inca-empire 1534 loss: **matched**. /ledger/8 Cuzco and Quito vs inca-empire /ledger/20 (Quito 1534); Cajamarca loss 1533-07 (/ledger/18) falls within a year.
- spanish-empire 1535 gain (inca-empire) -> inca-empire 1535 loss: **matched**. /ledger/10 Lima vs inca-empire /ledger/21 (1535-01).
- inca-empire 1537 loss (spanish-empire) -> none: **missing**. inca-empire /ledger/23: the empire outside the Neo-Inca State; no gain in spanish-empire (its 1540 keyframe adds the land without an event).
- inca-empire 1567 vassal_start (spanish-empire) -> none: **missing**. inca-empire /ledger/26-27 vassal 1567-1571 (Neo-Inca State); no vassal events in spanish-empire.
- inca-empire 1572 loss (spanish-empire) -> none: **missing**. inca-empire /ledger/28-29 1572-06 loss and dissolve (Vilcabamba, c3); no gain in spanish-empire.
- spanish-empire 1534 gain (michoacan) -> michoacan 1530 loss: **mismatch**. /ledger/9 1534 (c1, Cliopatria year) vs michoacan /ledger/13-14 1530-02 (c3, Michoacan page): four years apart.
- spanish-empire 1538 gain (muisca-confederation) -> muisca-confederation 1538 loss: **matched**. /ledger/11 (counterpart corrected to the slug by the reviewer) vs muisca-confederation /ledger/5 1538-08; its 1539 losses of Tunja and Sogamoso are near the Bogota 150 km radius.
- spanish-empire 1697 gain (itza-mayans) -> itza-mayans 1697 dissolve: **matched**. /ledger/31 vs itza-mayans /ledger/4 1697-03 (spanish-empire lacks the month).
- portuguese-empire 1529 gain (spanish-empire) -> none: **missing**. portuguese-empire /ledger/13 Moluccas (Zaragoza); spanish-empire has no Moluccas event (claim land outside its shapes; at most a claim loss).
- spanish-empire 1581 vassal_start (portuguese-empire) -> portuguese-empire 1581 loss: **mismatch**. /ledger/20 vassal_start vs portuguese-empire /ledger/25 loss to spanish-empire: same year, different type.
- spanish-empire 1640 vassal_end (portuguese-empire) -> portuguese-empire 1640 gain: **mismatch**. /ledger/24 1640-12 vassal_end vs portuguese-empire /ledger/26 1640-12 gain from spanish-empire.
- portuguese-empire 1706 loss (spanish-empire) -> none: **missing**. portuguese-empire /ledger/46 Colonia lost to Spain (c1) and /ledger/47 regained 1713 (c1); no events in spanish-empire.
- portuguese-empire 1750 gain (spanish-empire) -> none: **mismatch**. portuguese-empire /ledger/54 1750-01 gain of the Brazilian interior from spanish-empire (Madrid); spanish-empire has no 1750 loss and its 1752 shape grows by 2.2 M km2 instead.
- spanish-empire 1756 loss (portuguese-empire) -> portuguese-empire 1756 occupation_start: **mismatch**. /ledger/35 loss of the seven missions to Portugal vs portuguese-empire /ledger/58 occupation_start with counterpart jesuit-reducciones: counterpart and type disagree.
- spanish-empire 1761 gain (portuguese-empire) -> portuguese-empire 1759 occupation_end: **mismatch**. /ledger/36 (El Pardo 1761) vs portuguese-empire /ledger/59 occupation_end 1759 (counterpart jesuit-reducciones): two years and the counterpart disagree.
- portuguese-empire 1762 loss (spanish-empire) -> none: **missing**. portuguese-empire /ledger/60 Colonia 1762 and /ledger/61 regained 1763; spanish-empire's 1762 and 1763 keyframe notes show Colonia in and out but the ledger has no event.
- spanish-empire 1777 gain (portuguese-empire) -> portuguese-empire 1777 loss: **matched**. /ledger/45 1777-10 vs portuguese-empire /ledger/64 1777-10.
- portuguese-empire 1777 gain (spanish-empire) -> none: **missing**. portuguese-empire /ledger/65 (Santa Catarina) and /ledger/66 (Rio Grande do Sul outside the missions), 1777-10; no loss in spanish-empire, which also lacks the 1763 and 1777-02 captures.
- portuguese-empire 1778 gain (spanish-empire) -> none: **mismatch**. portuguese-empire /ledger/67 western Amazon from spanish-empire (c1) while spanish-empire's 1778 keyframe adds a 1.2 M km2 Amazon block: same land, opposite directions.
- spanish-empire 1778 gain (portuguese-empire) -> portuguese-empire 1778 loss: **matched**. /ledger/46 Fernando Po vs portuguese-empire /ledger/68 1778-03 (spanish-empire's region lacks Annobon).
- spanish-empire 1801 loss (portuguese-empire) -> none: **missing**. /ledger/53 Misiones Orientales to Portugal (Badajoz 1801, confirmed on the San Ildefonso page); portuguese-empire has no 1801 gain from spanish-empire.
- spanish-empire 1516 found (crown-of-castile) -> none: **exception**. crown-of-castile not written yet (predecessor; land described).
- spanish-empire 1565 gain (kingdom-of-france) -> none: **exception**. Fort Caroline/St Augustine; kingdom-of-france not written yet.
- spanish-empire 1571 gain (namayan) -> none: **exception**. namayan not written yet.
- spanish-empire 1599 loss (Mapuche (Araucanía)) -> none: **exception**. listed in counterparts_needing_dossiers (also /ledger/14, /ledger/17).
- spanish-empire 1642 loss (dutch-republic) -> none: **exception**. eu-09, not written yet.
- spanish-empire 1655 loss (english-colonial-empire) -> none: **exception**. am-07, not written yet (also /ledger/32, 1704).
- spanish-empire 1680 loss (Pueblo peoples (Pueblo Revolt)) -> none: **exception**. listed in counterparts_needing_dossiers (also /ledger/29, 1692).
- spanish-empire 1697 loss (kingdom-of-france) -> none: **exception**. western Hispaniola (Ryswick); kingdom-of-france not written yet.
- spanish-empire 1762 occupation_start (british-colonial-empire) -> none: **exception**. Havana and Manila; eu-11 not written yet (also /ledger/41 1763, /ledger/48 1781, /ledger/50 1783, /ledger/52 1797).
- spanish-empire 1762 gain (new-france) -> none: **exception**. Louisiana; am-07 not written yet.
- spanish-empire 1767 gain (jesuit-reducciones) -> none: **exception**. am-06 other part, not written yet.
- spanish-empire 1795 loss (united-states-of-america) -> none: **exception**. am-07 not written yet (also /ledger/75 1821, /ledger/94-96 1898).
- spanish-empire 1801 loss (haiti) -> none: **exception**. am-08 not written yet.
- spanish-empire 1803 loss (french-louisiana) -> none: **exception**. am-06 other part, not written yet.
- spanish-empire 1809 gain (first-french-empire) -> none: **exception**. not written yet.
- spanish-empire 1810 loss (new-granada) -> none: **exception**. independence states owned by am-08, none written yet: new-granada, republic-of-chile, rio-de-la-plata, republic-of-venezuela, paraguay, gran-colombia, republic-of-peru, first-mexican-empire, federated-republic-of-mexico, bolivia (/ledger/59-84).
- spanish-empire 1821 loss (Central America (Act of Independence)) -> none: **exception**. listed in counterparts_needing_dossiers.
- spanish-empire 1860 gain (morocco) -> none: **exception**. af-02, not written yet.
- spanish-empire 1861 gain (dominican-republic) -> none: **exception**. not written yet (also /ledger/89, 1865).

## Problems

- Spanish_American_wars_of_independence: WebFetch read 100,000 of 101,726 characters (the events checked were in the part read).
- The reviewer brief says reviewers do not edit dossiers; the orchestrator's adjustment allows small verified fixes: one applied (/ledger/11 counterpart slug), dossier re-validated (0 errors, 1 warning: Sidi Ifni).
- portuguese-empire (am-06-a) needs the mirror of /ledger/53 (1801 Misiones) and the Iberian Union type decided with this dossier; route the Colonia, Amazon 1750/1778 and Misiones 1756-1761 mismatches to both authors.
