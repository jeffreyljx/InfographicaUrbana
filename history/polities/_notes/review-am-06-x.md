# Review of batch am-06-x (2026-10-19)

Adversarial review of the twelve new colonial dossiers (Spanish and Portuguese America, French Saint-Domingue). Validator: 0 errors in all twelve; warnings only for the planned counterparts pueblo-revolt and mapuche. Every keyframe was resolved with the gazetteer and the batch was checked for cells drawn by two dossiers in the same year; 23 Wikipedia pages were opened for spot checks. No fabricated or mis-dated event was found; the failures are shape problems.

## Verdicts

### viceroyalty-of-new-spain: thin

Gaps for a gap-filler:
- `/keyframe_review/0-/keyframe_review/4`: Dates of the conquest/settlement of Michoacan, Oaxaca, Yucatan, Nueva Vizcaya, Nuevo Leon, Coahuila, Sonora and Sinaloa: the keyframes 1535-1767 grow with Cliopatria's Spanish Empire shape inside Mexico (472,000 km2 in 1535, 671,000 in 1548, 1.47 M in 1598) with only Nueva Galicia and New Mexico dated. Author flagged it; thin by design within the 5-page budget. Try https://en.wikipedia.org/wiki/Nueva_Vizcaya
- `/ledger/8, /ledger/9`: Alta California: the 1768 event is the order to occupy San Diego and Monterey and the 1776 event is the creation of the Commandancy General (Provincias Internas page: 'formally created in 1776'; the Californias are not named in the 1776 decree). The occupation itself (San Diego 1769, Monterey 1770, San Francisco 1776) is not dated by a page opened. Try https://en.wikipedia.org/wiki/Alta_California

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Viceroyalty_of_New_Spain): confirmed: 'created by royal decree on 12 October 1535'
- `/ledger/3` (https://en.wikipedia.org/wiki/Santa_Fe_de_Nuevo_M%C3%A9xico): confirmed: 'the Spanish expelled from Nuevo México for a period of 12 years' (Pueblo Revolt 1680); founding 'On July 12, 1598' also confirmed for /ledger/2
- `/ledger/7` (https://en.wikipedia.org/wiki/Spanish_Texas): confirmed: Treaty of Fontainebleau 'November 3, 1762', France ceded Louisiana west of the Mississippi
- `/ledger/14` (https://en.wikipedia.org/wiki/Viceroyalty_of_New_Spain): confirmed: 'At its conclusion in 1821, the viceroyalty was dissolved'
- `/ledger/9` (https://en.wikipedia.org/wiki/Provincias_Internas): year confirmed ('formally created in 1776'); the Californias are in the 1768 plan, not the 1776 decree: the land gain is the researcher's reading, c2 is honest

Area: infobox None (None), drawn 3652129 km2, ratio None. No area on the New Spain page (checked whole text); the 1776-1821 keyframe resolves to 3.65 M km2. The Santa Fe page's 603,345 km2 is 1842 Mexican New Mexico; author says so.

### captaincy-general-of-guatemala: fail

Findings:
- [BLOCKING] `/keyframe_review/1/correction`: The 1543-1821 shape includes all of modern Guatemala, so it draws the Peten over the Itza kingdom, which held it until March 1697 (itza-mayans dossier: /ledger/3-4 contest_end and dissolve 1697-3, successor spanish-empire). Evidence: Gazetteer: the 1543 keyframe overlaps the Cliopatria Itza Mayans shape by 21,500 km2 (of 31,100) and the Peten region by 35,700 km2 for 154 years; the captaincy dossier has no 1697 event and its notes do not mention the Itza. Fix: Subtract {"region": "Peten"} (or the Itza Mayans shape) from the 1543 keyframe for 1543-1696, add a keyframe captaincy-general-of-guatemala_1697 without the subtraction, and add a 1697-3 gain cp itza-mayans (open https://en.wikipedia.org/wiki/Spanish_conquest_of_Pet%C3%A9n for the date; the itza-mayans dossier already cites it).
- [non-blocking] `/ledger (missing, 1803)`: No mirror for viceroyalty-of-new-granada /ledger/6 (1803-11 gain of the Mosquito Coast strip, counterpart captaincy-general-of-guatemala). Evidence: Viceroyalty_of_New_Granada page: 'A strip along the Atlantic Ocean in Mosquito Coast was added by the Royal Decree of 20 November 1803'. The Guatemala dossier keeps Atlantico Norte, Atlantico Sur and Gracias a Dios inside its 1543-1821 shape. Fix: Either add a 1803-11 loss cp viceroyalty-of-new-granada (region as in the New Granada event, confidence 2, source the New Granada page) and a keyframe from 1803 without the strip, or agree with the New Granada author to drop the event; the Spanish never held that coast (the Guatemala notes say so).

Gaps for a gap-filler:
- `/keyframe_review/1`: Conquest dates of Costa Rica (1560s), Nicaragua and Honduras: the shape draws them from 1543 (author flagged). Try https://en.wikipedia.org/wiki/Spanish_conquest_of_Costa_Rica
- `/ledger/5`: Occupation_end 1821 at confidence 1 is only the captaincy's end (Belize stayed British); fine as a closure but no page. Try https://en.wikipedia.org/wiki/British_Honduras

Spot checks:
- `/ledger/1` (https://en.wikipedia.org/wiki/Captaincy_General_of_Guatemala): confirmed: 'In 1543 the territory of the kingdom was defined with the establishment of the Audiencia of Guatemala'; country list in the lead
- `/ledger/2` (https://en.wikipedia.org/wiki/Captaincy_General_of_Guatemala): confirmed: 'In 1609 the area became a captaincy general'
- `/ledger/3` (https://en.wikipedia.org/wiki/Captaincy_General_of_Guatemala): confirmed: Antigua 'ordered abandoned in 1776'
- `/ledger/6` (https://en.wikipedia.org/wiki/Captaincy_General_of_Guatemala): confirmed: infobox 'Disestablished: 15 September 1821'
- `/ledger/4` (https://en.wikipedia.org/wiki/British_Honduras): confirmed: infobox 'Treaty of Versailles (1783): 25 November 1783'; Hondo-Belize logwood rights

Area: infobox None (None), drawn 501754 km2, ratio None. No area on the page; 1543-1821 keyframe resolves to 501,754 km2.

### spanish-louisiana: fix

Findings:
- [non-blocking] `/keyframe_review/0/correction and /ledger/0/region`: The gazetteer region 'Louisiana' includes the Florida Parishes east of the Mississippi (Baton Rouge district), which were British West Florida from 1763 and Spanish West Florida after 1779; the keyframe note itself says 'The east bank went to Britain in 1763; New Orleans and its island stayed Spanish'. Evidence: Gazetteer: this keyframe and spanish-florida's 1783-1809 keyframe overlap by 18,968 km2 at lon -91.7..-89.65, lat 30.0..30.98. Fix: Subtract {"region": "West Florida"} (keep New Orleans' island with the 40 km disc) from the keyframe and the found/dissolve regions.
- [non-blocking] `/keyframe_review/0/correction`: The region 'Louisiana' (whole US states, incl. all of Colorado) overlaps New Spain's 'New Mexico (province)' by 92,814 km2 at lat 37.0-38.5 N, lon -109.0..-102.1 for 1762-1801. Evidence: Gazetteer overlap between this keyframe and viceroyalty-of-new-spain keyframes _1716 (from 1762), _1768 and _1776. Fix: Subtract {"region": "New Mexico (province)"} from the Louisiana keyframe (the Louisiana page says the treaties 'never defined the boundaries precisely'; New Mexico's settlements are the older Spanish holding).

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Louisiana_(New_Spain)): confirmed: infobox 'Transfer by France: 23 November 1762' (treaty of 3 November per the note)
- `/ledger/1` (https://en.wikipedia.org/wiki/Louisiana_(New_Spain)): confirmed: 'by 1768, a rebellion erupted'
- `/ledger/2` (https://en.wikipedia.org/wiki/Louisiana_(New_Spain)): confirmed: the uprising was not suppressed 'until 1769' (O'Reilly)
- `/ledger/3` (https://en.wikipedia.org/wiki/Louisiana_(New_Spain)): confirmed: infobox 'Returned to France: 21 March 1801'; handover 30 November 1803 also on the page (author notes it)

Area: infobox 2275940 (None), drawn 2604617 km2, ratio 0.87. Body text 'an area of 878,745 square miles (2,275,940 km2)'; no Cliopatria row, the keyframe resolves to 2.60 M km2; author compares the two in the keyframe note.

### viceroyalty-of-new-granada: fail

Findings:
- [BLOCKING] `/keyframe_review/0/correction, /ledger/0/region, /ledger/1/region`: The first viceroyalty (1717-1723) is drawn without Quito (Ecuador); the keyframe note quotes the page as 'Quito 1739 to 1822', but the page lists 'Quito (1717 to 1723 and 1739 to 1822)'. Evidence: Viceroyalty_of_New_Granada province list (read 2026-10-19): Quito '(1717 to 1723 and 1739 to 1822)'; only Panama is dated 'incorporated in 1739'. Fix: Add {"intersect": [{"cliopatria": "Spanish Empire", "year": 1717}, {"country": "Ecuador"}]} to the 1717 keyframe, the 1717 found and the 1723 loss; the Peru dossier must then subtract Ecuador in viceroyalty-of-peru_1717 and its /ledger/1-2.
- [BLOCKING] `/keyframe_review (gaps 1810-1815 and 1819-1822)`: No keyframe covers 1810-1815 or 1819-1822 although the state is alive: the 1810 loss is only Cliopatria's patriot 'New Granada' shape, and the 1822 dissolve hands over Ecuador, Panama and Colombia, so the royalist land (Quito, Panama, Santa Marta, Pasto; Panama and Cartagena to 1821, Quito to May 1822) is drawn by nobody. Evidence: Keyframes: _1803 ends 1809, _1816 runs 1816-1818, nothing after; the author's note (2) says the page names no extent but does not mention the missing keyframes. Fix: Add viceroyalty-of-new-granada_1810 (Spanish Empire 1810 inside Colombia, Ecuador and Panama minus Cliopatria New Granada 1811 and Cundinamarca 1814) for 1810-1815 and viceroyalty-of-new-granada_1819 (Ecuador, Panama, Narino/Pasto and the Caribbean coast) for 1819-1822, with the 1821 losses (Cartagena, Panama 28 November 1821) from pages such as https://en.wikipedia.org/wiki/Independence_of_Panama_from_Spain and https://en.wikipedia.org/wiki/Battle_of_Pichincha.
- [non-blocking] `/keyframe_review/2/to`: Maynas (Loreto, 326,747 km2) is drawn by both New Granada (_1777 runs to 1802) and Peru (_1802 keyframe) in 1802. Evidence: Gazetteer overlap at 1802; the ledger loss is 1802 ('1739-1802' on the page). Fix: End _1777 at 1801 and start the next keyframe in 1802 (new shape_id), or move the Peru keyframe to 1803.
- [non-blocking] `/keyframe_review/3/correction, /keyframe_review/4/correction`: Guayas (11,128 km2) is drawn by New Granada and by Peru from 1803 to 1818 although /ledger/5 gives it to Peru in 1803. Evidence: Gazetteer overlap with viceroyalty-of-peru _1803 and _1810; the keyframe note admits it ('a gap-filler should subtract them'). Fix: Wrap both corrections in a minus with {"admin1": "Guayas", "country": "Ecuador"} (the gazetteer resolves it; the Peru dossier uses it).
- [non-blocking] `/ledger/6`: The 1803 Mosquito Coast gain has no trace in the keyframes and no mirror in captaincy-general-of-guatemala; its confidence 1 understates the page. Evidence: Page: 'A strip along the Atlantic Ocean in Mosquito Coast was added by the Royal Decree of 20 November 1803' (year and month are the page's; the region is the researcher's reading). Fix: Raise to confidence 2 and either draw the strip from 1803 or drop the event; coordinate with the Guatemala mirror.
- [non-blocking] `/identity/capitals`: No capital after 1819 although the dossier runs to 1822-05. Evidence: Royalist seat after Boyaca was Quito/Panama (not on the page). Fix: Add the royalist seat for 1819-1822 from a page or note the gap.

Gaps for a gap-filler:
- `/keyframe_review/4`: Which provinces Spain held in 1816-1819 and 1819-1822 (the page names none); only one page was opened for a 105-year state (budget 2-5). Try https://en.wikipedia.org/wiki/Spanish_reconquest_of_New_Granada

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Viceroyalty_of_New_Granada): date confirmed ('27 May 1717'); region wrong: page includes Quito 1717-1723
- `/ledger/1` (https://en.wikipedia.org/wiki/Viceroyalty_of_New_Granada): confirmed: infobox 'Suppressed: 5 November 1723'
- `/ledger/2` (https://en.wikipedia.org/wiki/Viceroyalty_of_New_Granada): confirmed: infobox 'Reestablished: 20 August 1739'; 'Panama was incorporated in 1739'
- `/ledger/9` (https://en.wikipedia.org/wiki/Viceroyalty_of_New_Granada): confirmed: 'Battle of Boyacá, on 7 August 1819'
- `/ledger/3` (https://en.wikipedia.org/wiki/Viceroyalty_of_New_Granada): confirmed: infobox 'Separation of Venezuela: 8 September 1777'

Area: infobox 2300000 (1778), drawn 1471878 km2, ratio 1.56. Infobox '1778: 2,300,000 km2'; the 1777-1802 keyframe resolves to 1.47 M km2. Inside the factor of two, but the dossier never quotes the infobox area: add it to the _1777 note.

### viceroyalty-of-the-rio-de-la-plata: fix

Findings:
- [applied by reviewer] `/ledger/4/region, /ledger/4/counterpart`: The 1801 loss used the whole gazetteer region 'Jesuit Missions' (120,633 km2, half of it Argentine Misiones and southern Paraguay, never lost) and named portuguese-empire, which has no 1801 gain; colonial-brazil /ledger/13 is the mirror. Evidence: Page: 'From 1801 to 1802, within the framework of the War of the Oranges, the Misiones Orientales were captured by Portuguese forces'; the region text already said 'the seven missions east of the Uruguay'. Fix: Applied: region set to intersect(Jesuit Missions, Brazil) (59,432 km2), counterpart colonial-brazil, reviewer note appended; validator 0 errors, 0 warnings.
- [non-blocking] `/keyframe_review/0/correction`: The Misiones Orientales (Jesuit Missions inside Brazil, ~59,400 km2) are drawn by nobody in 1776-1800: this keyframe is limited to Argentina, Bolivia, Paraguay, Uruguay and Antofagasta, and colonial-brazil _1775 subtracts them. Evidence: Gazetteer check of the two corrections; the 1801 loss (page-dated) is otherwise land the shape never had. Fix: Add {"intersect": [{"region": "Jesuit Missions"}, {"country": "Brazil"}]} to the 1776-1809 keyframe and end it in 1800 (new keyframe from 1801 without them).
- [non-blocking] `/ledger/0/counterpart (Cuyo)`: Cuyo enters with the 1776 found whose counterpart is viceroyalty-of-peru, but captaincy-general-of-chile /ledger/11 gives Cuyo to this viceroyalty in 1776. Evidence: Page: 'on 1 August 1776 the king gave him control over the Royal Audiencia of Charcas and the corrigimiento of Cuyo'. Fix: Add a 1776-8 gain {"region": "Cuyo"} cp captaincy-general-of-chile (confidence 3, this page), or name Chile for Cuyo in the found note.
- [non-blocking] `/identity/capitals`: Buenos Aires 1776-1810 overlaps Cordoba 1806-1806. Evidence: Capitals must be contiguous. Fix: Split Buenos Aires into 1776-1805 and 1807-1810 around Cordoba 1806 (cite the page sentence on Sobremonte's move), or drop Cordoba.

Gaps for a gap-filler:
- `/keyframe_review/0`: Patagonia and the Chaco are drawn as viceroyalty land from Cliopatria's shape (author flagged). Try https://en.wikipedia.org/wiki/Patagonia

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Viceroyalty_of_the_R%C3%ADo_de_la_Plata): confirmed: 'Organised: 1 August 1776'
- `/ledger/1` (https://en.wikipedia.org/wiki/Viceroyalty_of_the_R%C3%ADo_de_la_Plata): confirmed: 'On 1 October 1777' Portugal 'recognised Spanish sovereignty over Colonia del Sacramento and San Gabriel Island'
- `/ledger/3` (https://en.wikipedia.org/wiki/Viceroyalty_of_the_R%C3%ADo_de_la_Plata): confirmed: 'The Intendancy of Puno became part of the Viceroyalty of Peru in 1796'
- `/ledger/4` (https://en.wikipedia.org/wiki/Viceroyalty_of_the_R%C3%ADo_de_la_Plata): year confirmed; region over-wide (fixed by reviewer)
- `/ledger/14` (https://en.wikipedia.org/wiki/Viceroyalty_of_the_R%C3%ADo_de_la_Plata): confirmed: infobox 'Fall of Montevideo: 23 June 1814' (body says 23 May 1814; author noted)

Area: infobox None (None), drawn 3582581 km2, ratio None. No area on the page (only the 1801 census); the 1776-1809 keyframe resolves to 3.58 M km2.

### viceroyalty-of-peru: fail

Findings:
- [BLOCKING] `/keyframe_review/0-/keyframe_review/4 (correction), /ledger/4/region`: Peru's 1542-1775 shapes include all of Argentina, so Cuyo (Mendoza, San Juan, San Luis) is drawn by both Peru and captaincy-general-of-chile from 1550 to 1775, and Peru's 1776 loss hands Cuyo to the Rio de la Plata a second time. Evidence: Gazetteer overlap Peru x Chile: 140,107 km2 in 1560, 252,394 km2 in 1622-1775. Chile /ledger/11 (Chile page: 'The Mendoza and San Juan territories were transferred to ... the Rio de la Plata in 1776'); RdlP page: the king gave Cevallos 'the corrigimiento of Cuyo' on 1 August 1776. Fix: Subtract {"region": "Cuyo"} from keyframes _1542, _1600, _1717, _1723 and _1739 and from the 1776 loss region.
- [BLOCKING] `/keyframe_review/0-/keyframe_review/3 (correction), /ledger/1/region, /ledger/2/region`: All of Venezuela is drawn inside Peru in 1542-1716 and 1723-1738, contradicting the dossier's own notes ('Venezuela is out of the Peruvian shape throughout') and the Venezuela page. Evidence: Captaincy_General_of_Venezuela: Venezuela was 'previously under the jurisdiction of the Audiencia of Santo Domingo'; Cumana, Margarita and Caracas were supervised by Santo Domingo, Maracaibo, Guayana and Trinidad by the Bogota Audiencia. Fix: Remove the Santo Domingo provinces (Caracas, Cumana, Margarita: the central and eastern Venezuelan admin1 units) from those keyframes and events, keeping Maracaibo and Guayana if the Bogota link is wanted, or remove Venezuela and keep the notes as they are.
- [non-blocking] `/wars/1/to, /wars/2/to`: Two wars end in 1825 and 1826, after the dossier's end (1824-12). Evidence: Wars must lie inside the life; the Peruvian independence page: Callao 'would surrender in January 1826'. Fix: Clip to 1824 and say in the war note that Callao held to January 1826 (or extend the dossier to 1826-01 for the Real Felipe holdout).

Gaps for a gap-filler:
- `/keyframe_review/1`: No page dates any Peruvian boundary change 1563-1717; the 1600-1716 keyframe (3.65 M km2) is Cliopatria's shape (author flagged). Try https://en.wikipedia.org/wiki/Real_Audiencia_of_Charcas

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Viceroyalty_of_Peru): confirmed: 'Established: 20 November 1542'; lead 'modern-day Peru and most of the Spanish Empire in South America'
- `/ledger/9` (https://en.wikipedia.org/wiki/Peruvian_War_of_Independence): confirmed: junta 'on 3 August in Cuzco' (1814)
- `/ledger/12` (https://en.wikipedia.org/wiki/Peruvian_War_of_Independence): confirmed: 'On 7 September the Liberation expedition arrived on the bay of Pisco' (1820)
- `/ledger/18` (https://en.wikipedia.org/wiki/Viceroyalty_of_Peru): confirmed: infobox 'Dissolved: 30 December 1824'
- `/ledger/11` (https://en.wikipedia.org/wiki/Viceroyalty_of_Peru): confirmed: 'Guayaquil proclaimed itself an independent state in 1820'

Area: infobox 1340000 (None), drawn 2222485 km2, ratio 0.6. Infobox 1,340,000 km2 with no year; the 1542 keyframe resolves to 2.22 M km2 (0.60) and the 1600-1716 one to 3.65 M (0.37); the author flags the mismatch in the _1542 note as the modern country's area.

### captaincy-general-of-venezuela: fix

Findings:
- [non-blocking] `/identity/capitals/0`: Caracas is the capital 1777-1823, but it lies outside the drawn shape in 1810-1811 and 1813 (patriot zones subtracted) and in 1821-1823 (keyframe _1821 is Falcon, Zulia and Puerto Cabello only). Evidence: Venezuelan independence page: Caracas council deposed the governor on 19 April 1810; 'Bolivar entered Caracas on 6 August 1813'; Carabobo 1821. Fix: End Caracas in 1820 (with breaks for 1810-1811 and 1813) and give the royalist seat after Carabobo from a page, or leave the gap and say so.
- [non-blocking] `/keyframe_review/8/note`: The 1821-1823 holdouts (Falcon/Coro and Zulia/Maracaibo) are not named by the war page after Carabobo: it names Cumana ('fell shortly thereafter') and Puerto Cabello ('capitulating in October 1823'); Coro and Maracaibo appear only in the belligerents list and the 1823 lake battle. Evidence: Venezuelan_War_of_Independence read 2026-10-19. Fix: Say so in the note (Maracaibo was patriot from early 1821 and royalist again 1822-1823); keep confidence 2.

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Captaincy_General_of_Venezuela): confirmed: 'created on September 8, 1777, through the Royal Decree of Graces of 1777'
- `/ledger/1` (https://en.wikipedia.org/wiki/Captaincy_General_of_Venezuela): confirmed: 'Control of the Province of Trinidad was lost to the British in 1797'
- `/ledger/3` (https://en.wikipedia.org/wiki/Venezuelan_War_of_Independence): confirmed: 'Miranda capitulated to Monteverde and signed an armistice on 25 July 1812'
- `/ledger/4` (https://en.wikipedia.org/wiki/Venezuelan_War_of_Independence): confirmed: 'Bolívar entered Caracas on 6 August 1813'
- `/ledger/9` (https://en.wikipedia.org/wiki/Captaincy_General_of_Venezuela): confirmed: infobox 'Capitulation: 24 July 1823'

Area: infobox None (None), drawn None km2, ratio None. No area on the page; author says so.

### captaincy-general-of-chile: fix

Findings:
- [applied by reviewer] `/keyframe_review/1/to`: No keyframe covered 1599-1603 (_1550 ended 1598, _1604 began 1604), so the state vanished from the map for five years. Evidence: Keyframe coverage check; the Arauco War page dates the losses 1599, 1600, 1602, 1603 and 1604 inside the 1598-1604 uprising. Fix: Applied: _1550 now runs to 1603 (reviewer note appended); the 1599-1603 losses are small discs inside the Mapuche contest of 1598-1604. Validator 0 errors.
- [non-blocking] `/identity/capitals/0`: Santiago is the capital 1541-1826 but was patriot-held 1810-1814 and from February 1817; keyframes _1817-_1823 are discs around Concepcion, Valdivia, Osorno and Castro only. Evidence: Chilean independence page: Chacabuco 12 February 1817, 'Patriots regained Santiago'. Fix: End Santiago in 1816 (and note 1810-1814) and add the royalist seat for 1817-1826 (Valdivia to 1820, then Chiloe) from a page, or leave the gap.
- [non-blocking] `/ledger/8/note`: The quoted sentence 'the river became La Frontera the de facto border...' is not on the Arauco War page. Evidence: Arauco_War read 2026-10-19: 'Afterward the two forces established a clear frontier between the Spanish domains and the land of the independent Mapuche.' Fix: Replace the quote with the page's sentence (the event's year 1604 is confirmed).

Gaps for a gap-filler:
- `/ledger/2`: Founding years of Angol, La Imperial, Villarrica, Valdivia, Osorno, Castro and Mendoza/San Juan (all bundled at 1550, confidence 1). Try https://en.wikipedia.org/wiki/Destruction_of_the_Seven_Cities
- `/ledger/20`: Osorno 1823 (confidence 1). Try https://en.wikipedia.org/wiki/Chilo%C3%A9_Province

Spot checks:
- `/ledger/3` (https://en.wikipedia.org/wiki/Arauco_War): confirmed: 'on December 21, 1598, Oñez de Loyola became the second governor of Chile to die'
- `/ledger/4-/ledger/8` (https://en.wikipedia.org/wiki/Arauco_War): confirmed: Coya, Valdivia, Los Infantes 1599; La Imperial 1600; Villa Rica 1602; Osorno 1603; San Felipe de Araucan 1604
- `/ledger/15` (https://en.wikipedia.org/wiki/Chilean_War_of_Independence): confirmed: 'Battle of Chacabuco, on February 12, 1817'
- `/ledger/17` (https://en.wikipedia.org/wiki/Chilean_War_of_Independence): confirmed: 'In 1820, Cochrane administered a stunning blow' (no month)
- `/ledger/21` (https://en.wikipedia.org/wiki/Chilean_War_of_Independence): confirmed: Chiloé 'was not conquered until 1826'
- `/ledger/13` (https://en.wikipedia.org/wiki/Chilean_War_of_Independence): confirmed: First Government Junta 'September 18, 1810'

Area: infobox None (None), drawn None km2, ratio None. No area on the page; author says so.

### spanish-florida: fix

Findings:
- [non-blocking] `/ledger/0`: The gain from French Florida (Fort Caroline) has no month and so sorts before the found (1565-9), although Fort Caroline fell after St. Augustine was founded. Evidence: Spanish_Florida gives no date for the attack; St. Augustine 'On September 8, 1565'. Fort Caroline fell on 20 September 1565 (Fort Caroline page, not opened by the author). Fix: Open https://en.wikipedia.org/wiki/Fort_Caroline, add month 9 to the gain and put it after the found.

Gaps for a gap-filler:
- `/keyframe_review/1, /ledger/2`: The mission belt 1630-1705 is drawn as the whole gazetteer Florida, including south Florida that Spain never held (author flagged). Try https://en.wikipedia.org/wiki/Spanish_missions_in_Florida
- `/ledger/11, /ledger/13`: The 1783-1795 disputed band and the 1810 Baton Rouge district are stand-ins (polygon; 'West Florida without Mobile and Pensacola'). Try https://en.wikipedia.org/wiki/Republic_of_West_Florida

Spot checks:
- `/ledger/1` (https://en.wikipedia.org/wiki/Spanish_Florida): confirmed: 'On September 8, 1565, Admiral Pedro Menéndez de Avilés landed ... to found St. Augustine'
- `/ledger/7` (https://en.wikipedia.org/wiki/Spanish_Florida): confirmed: infobox 'Transferred to Britain: 10 February 1763'
- `/ledger/10` (https://en.wikipedia.org/wiki/Spanish_Florida): confirmed: Spain gained West Florida and regained East Florida 'in the Peace of Paris of 1783'
- `/ledger/12` (https://en.wikipedia.org/wiki/Spanish_Florida): confirmed: Pinckney's Treaty 1795, 'Spain recognized the 31st parallel as the border'
- `/ledger/17` (https://en.wikipedia.org/wiki/Spanish_Florida): confirmed: Adams-Onís treaty 'took effect on July 17, 1821'
- `/ledger/14` (https://en.wikipedia.org/wiki/Spanish_Florida): confirmed: 'by 1812, the Mobile District was absorbed into the U.S. territory of Mississippi'

Area: infobox None (None), drawn None km2, ratio None. No area on the page; author says so.

### colonial-brazil: thin

Gaps for a gap-filler:
- `/keyframe_review/6 -> /keyframe_review/7`: The shape grows from 540,000 km2 (1654-1699) to 977,000 km2 (1700-1751) with no event: the bandeirante and gold-rush interior (Minas Gerais 1690s, Mato Grosso 1718, Goias 1725) is undated (author flagged; within the 5-page budget). Try https://en.wikipedia.org/wiki/Bandeirantes
- `/ledger (1761-1777)`: The Treaty of El Pardo (1761, nullifying Madrid; Treaty of Madrid page confirms the nullification) and the Spanish occupation of Rio Grande (1763-1776) are not in the ledger; the 1752-1774 keyframe keeps the 1750 gains, including the Misiones Orientales via Cliopatria's shape. Try https://en.wikipedia.org/wiki/Treaty_of_El_Pardo_(1761)

Spot checks:
- `/ledger/6` (https://en.wikipedia.org/wiki/Colonial_Brazil): confirmed: 'From 1630 to 1654, the Dutch set up more permanently in commercial Recife and aristocratic Olinda'
- `/ledger/8` (https://en.wikipedia.org/wiki/Colonial_Brazil): confirmed: 'In 1652, the State of Maranhão was extinguished, and its territory was briefly added to the State of Brazil'
- `/ledger/11` (https://en.wikipedia.org/wiki/Treaty_of_Madrid_(13_January_1750)): confirmed: 'undisputed sovereignty of the gold and diamond districts of Goiás and Mato Grosso' and 'the retention of the Rio Grande do Sul'
- `/ledger/12` (https://en.wikipedia.org/wiki/Colonial_Brazil): confirmed: 'In 1775 all Brazilian States (Brasil, Maranhão and Grão-Pará) were unified into the Viceroyalty of Brazil'
- `/ledger/5` (https://en.wikipedia.org/wiki/Colonial_Brazil): confirmed: 'In 1621, an administrative reorganization took place, and the Governorate General of Brazil became known as the State of Brazil'

Area: infobox 8100200 (None), drawn 7303752 km2, ratio 1.11. Infobox 8,100,200 km2 with no year; the 1821-1822 keyframe resolves to 7.30 M km2 (1778: 7.12 M). Author quotes both.

### state-of-maranhao-and-grao-para: pass

Gaps for a gap-filler:
- `/keyframe_review/1 -> /keyframe_review/2`: Growth from 281,000 km2 (1654) to 356,000 km2 (1700) with no event (Cliopatria's shape); small, within budget. Try https://en.wikipedia.org/wiki/Captaincy_of_Gr%C3%A3o-Par%C3%A1

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/State_of_Maranh%C3%A3o_(colonial)): confirmed: 'The state was created on 13 June 1621 by Philip II of Portugal'
- `/ledger/1` (https://en.wikipedia.org/wiki/State_of_Maranh%C3%A3o_(colonial)): confirmed: 'extinguished in 1652 and in 1654 reconstituted as Maranhão and Grão-Pará'
- `/ledger/2` (https://en.wikipedia.org/wiki/State_of_Maranh%C3%A3o_(colonial)): confirmed (same sentence)
- `/ledger/3` (https://en.wikipedia.org/wiki/State_of_Maranh%C3%A3o_(colonial)): confirmed: Belém 'formally designated the state capital in 1737' (the page also gives the 1751 move; author notes both)
- `/ledger/5` (https://en.wikipedia.org/wiki/State_of_Maranh%C3%A3o_(colonial)): confirmed: 1751 'had its name changed to Grão-Pará and Maranhão'

Area: infobox None (None), drawn 1499444 km2, ratio None. No area on the pages; 1750-1775 keyframe resolves to 1.50 M km2.

### saint-domingue: fix

Findings:
- [applied by reviewer] `/ledger/2/confidence`: Confidence 3 with a region (the Centre department) the page does not name. Evidence: Treaty_of_Aranjuez_(1777): 'Spain made substantial gains in the upper Artibonite Valley in middle section of the island'; no place or boundary named; the keyframe note itself calls Centre 'the researcher's reading'. Fix: Applied: confidence 3 -> 2, reviewer note appended; validator 0 errors.
- [non-blocking] `/wars/1/to`: The Haitian Revolution war runs 1791-1804, past the dossier's end (1791-08), with no zones. Evidence: Wars must lie inside the life (the dossier hands the land to haiti in 1791). Fix: Clip the war to 1791 with a note that it continues in the haiti dossier, or extend the dossier as the author's note (1) offers.

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Saint-Domingue): confirmed: 'The settlement on Tortuga was officially established in 1659 under the commission of King Louis XIV'
- `/ledger/1` (https://en.wikipedia.org/wiki/Saint-Domingue): confirmed: 'Spain tacitly recognized the French presence in the western third of the island in the 1697 Treaty of Ryswick' (infobox 'Ceded by Spain: 1697')
- `/ledger/2` (https://en.wikipedia.org/wiki/Treaty_of_Aranjuez_(1777)): date confirmed ('signed on 3 June 1777'); region not named: confidence lowered to 2
- `/ledger/3` (https://en.wikipedia.org/wiki/Saint-Domingue): confirmed: 'the August 1791 slave uprising'

Area: infobox 21550 (None), drawn 33636 km2, ratio 0.64. Infobox 21,550 km2; the 1697-1776 keyframe (modern Haiti) resolves to 33,636 km2; author compares them in the _1697 note (1936 frontier).

## Cross-dossier matrix

- viceroyalty-of-new-spain 1680 loss -> pueblo-revolt: exception (-) no dossier; listed in counterparts_needing_dossiers
- viceroyalty-of-new-spain 1692 gain -> pueblo-revolt: exception (-) no dossier; listed in counterparts_needing_dossiers
- viceroyalty-of-new-spain 1821 dissolve -> first-mexican-empire: exception (-) counterpart owned by a group that has not run yet (am-08)
- captaincy-general-of-guatemala 1783 occupation_start -> british-colonial-empire: exception (-) counterpart owned by a group that has not run yet (eu-11)
- captaincy-general-of-guatemala 1821 dissolve -> first-mexican-empire: exception (-) counterpart owned by a group that has not run yet (am-08)
- itza-mayans 1697 dissolve -> spanish-empire: missing (captaincy-general-of-guatemala) Guatemala draws the Peten from 1543 and has no 1697 gain; see the Guatemala finding
- spanish-louisiana 1762 found -> new-france: exception (-) counterpart owned by a group that has not run yet (am-07)
- spanish-louisiana 1801 dissolve -> french-louisiana: mismatch (french-louisiana 1800 found) french-louisiana (am-06-c) founds in 1800 from spanish-empire, and spanish-empire (am-06-b) keeps Louisiana to the handover of 30 November 1803; three dossiers disagree on the end (1800/1801/1803) and on the counterpart
- viceroyalty-of-new-granada 1717 found -> viceroyalty-of-peru: matched (viceroyalty-of-peru 1717 loss) years agree; both omit Quito, which the New Granada page lists for 1717-1723
- viceroyalty-of-new-granada 1723 loss -> viceroyalty-of-peru: matched (viceroyalty-of-peru 1723 gain) same Quito caveat
- viceroyalty-of-new-granada 1739 gain -> viceroyalty-of-peru: matched (viceroyalty-of-peru 1739 loss) 
- viceroyalty-of-new-granada 1777 loss -> captaincy-general-of-venezuela: matched (captaincy-general-of-venezuela 1777 found) 
- viceroyalty-of-new-granada 1802 loss -> viceroyalty-of-peru: matched (viceroyalty-of-peru 1802 gain) keyframes double-draw Loreto in 1802
- viceroyalty-of-new-granada 1803 loss -> viceroyalty-of-peru: matched (viceroyalty-of-peru 1803 gain) New Granada keyframes still draw Guayas 1803-1818
- viceroyalty-of-new-granada 1803 gain -> captaincy-general-of-guatemala: missing (-) Guatemala has no 1803 loss of the Mosquito Coast
- viceroyalty-of-new-granada 1810 loss -> new-granada: exception (-) counterpart owned by a group that has not run yet (am-08)
- viceroyalty-of-new-granada 1816 gain -> new-granada: exception (-) counterpart owned by a group that has not run yet (am-08)
- viceroyalty-of-new-granada 1819 loss -> gran-colombia: exception (-) counterpart owned by a group that has not run yet (am-08)
- viceroyalty-of-new-granada 1822 dissolve -> gran-colombia: exception (-) counterpart owned by a group that has not run yet (am-08)
- viceroyalty-of-the-rio-de-la-plata 1776 found -> viceroyalty-of-peru: matched (viceroyalty-of-peru 1776 loss) Peru's loss region includes Cuyo, which Chile also gives up in 1776
- captaincy-general-of-chile 1776 loss -> viceroyalty-of-the-rio-de-la-plata: mismatch (viceroyalty-of-the-rio-de-la-plata 1776 found) the RdlP found takes Cuyo with counterpart viceroyalty-of-peru; no RdlP event names Chile
- viceroyalty-of-the-rio-de-la-plata 1777 gain -> portuguese-empire: mismatch (portuguese-empire 1777 loss) portuguese-empire's 1777-10 loss names spanish-empire (empire vs viceroyalty layering)
- viceroyalty-of-the-rio-de-la-plata 1777 loss -> portuguese-empire: mismatch (portuguese-empire 1777 gain) portuguese-empire's 1777-10 gains name spanish-empire
- viceroyalty-of-the-rio-de-la-plata 1796 loss -> viceroyalty-of-peru: matched (viceroyalty-of-peru 1796 gain) 
- viceroyalty-of-the-rio-de-la-plata 1801 loss -> colonial-brazil: matched (colonial-brazil 1801 gain) fixed by the reviewer (was portuguese-empire, whole Jesuit Missions region)
- viceroyalty-of-the-rio-de-la-plata 1810 loss -> viceroyalty-of-peru: matched (viceroyalty-of-peru 1810 gain) 
- viceroyalty-of-the-rio-de-la-plata 1810 loss -> rio-de-la-plata: exception (-) counterpart owned by a group that has not run yet (am-08)
- viceroyalty-of-the-rio-de-la-plata 1811 loss -> paraguay: exception (-) counterpart owned by a group that has not run yet (am-08)
- viceroyalty-of-the-rio-de-la-plata 1814 dissolve -> rio-de-la-plata: exception (-) counterpart owned by a group that has not run yet (am-08)
- viceroyalty-of-peru 1542 found -> spanish-empire: exception (-) internal unit of the empire; spanish-empire records no transfer (layering question, see problems)
- viceroyalty-of-peru 1820 loss -> Free Province of Guayaquil: exception (-) name only, no dossier planned
- viceroyalty-of-peru 1821 loss -> republic-of-peru: exception (-) counterpart owned by a group that has not run yet (am-08)
- viceroyalty-of-peru 1824 dissolve -> republic-of-peru: exception (-) counterpart owned by a group that has not run yet (am-08)
- captaincy-general-of-venezuela 1797 loss -> british-colonial-empire: exception (-) counterpart owned by a group that has not run yet (eu-11)
- captaincy-general-of-venezuela 1810 loss -> republic-of-venezuela: exception (-) counterpart owned by a group that has not run yet (am-08); also 1812 gain, 1813 loss, 1814 gain, 1817 loss
- captaincy-general-of-venezuela 1819 loss -> gran-colombia: exception (-) counterpart owned by a group that has not run yet (am-08); also 1821 loss, 1823 dissolve
- captaincy-general-of-chile 1599 loss -> mapuche: exception (-) no dossier; listed in counterparts_needing_dossiers (also 1600, 1602, 1603, 1604 losses, 1645 and 1796 gains)
- captaincy-general-of-chile 1810 loss -> republic-of-chile: exception (-) counterpart owned by a group that has not run yet (am-08); also 1814, 1817, 1820, 1822, 1823, 1826
- spanish-florida 1565 gain -> French Florida (Fort Caroline): exception (-) name; listed as french-florida in counterparts_needing_dossiers
- spanish-florida 1763 loss -> british-colonial-empire: exception (-) counterpart owned by a group that has not run yet (eu-11); British East and West Florida suggested as gap-filler dossiers
- spanish-florida 1783 gain -> british-colonial-empire: exception (-) counterpart owned by a group that has not run yet (eu-11)
- spanish-florida 1810 loss -> united-states-of-america: exception (-) counterpart owned by a group that has not run yet; also 1812 loss, 1821 dissolve
- colonial-brazil 1630 loss -> dutch-brazil: mismatch (dutch-brazil 1630 found) dutch-brazil (am-06-c) founds from portuguese-empire, not colonial-brazil (layering)
- colonial-brazil 1652 gain -> state-of-maranhao-and-grao-para: matched (state-of-maranhao-and-grao-para 1652 loss) 
- colonial-brazil 1654 loss -> state-of-maranhao-and-grao-para: matched (state-of-maranhao-and-grao-para 1654 gain) 
- colonial-brazil 1654 gain -> dutch-brazil: mismatch (dutch-brazil 1654 dissolve) dutch-brazil dissolves to portuguese-empire
- colonial-brazil 1750 gain -> spanish-empire: missing (-) spanish-empire (am-06-b) has no 1750 loss (Treaty of Madrid)
- state-of-maranhao-and-grao-para 1750 gain -> spanish-empire: missing (-) spanish-empire has no 1750 loss
- colonial-brazil 1775 merge -> state-of-maranhao-and-grao-para: matched (state-of-maranhao-and-grao-para 1775 dissolve) 
- colonial-brazil 1821 gain -> federal-league: exception (-) counterpart owned by a group that has not run yet (am-08)
- colonial-brazil 1822 dissolve -> empire-of-brazil: exception (-) counterpart owned by a group that has not run yet (am-08)
- state-of-maranhao-and-grao-para 1621 found -> portuguese-empire: exception (-) internal unit; portuguese-empire records no transfer
- saint-domingue 1659 found -> spanish-empire: exception (-) claim-only Spanish land; spanish-empire records nothing
- saint-domingue 1697 gain -> spanish-empire: mismatch (spanish-empire 1697 loss) spanish-empire's 1697 loss names kingdom-of-france, not saint-domingue
- saint-domingue 1777 loss -> spanish-empire: missing (-) spanish-empire has no 1777 Hispaniola gain
- saint-domingue 1791 dissolve -> haiti: exception (-) counterpart owned by a group that has not run yet (am-08)

## Problems for the orchestrator

- Verdict semantics used here: 'fix' means accepted; findings with applied:true were made by the reviewer and validated; findings with applied:false and blocking:false are small author follow-ups that do not block acceptance. 'fail' dossiers (captaincy-general-of-guatemala, viceroyalty-of-new-granada, viceroyalty-of-peru) carry blocking:true findings.
- Reviewer edits applied (each re-validated, 0 errors, read back): viceroyalty-of-the-rio-de-la-plata /ledger/4 (region and counterpart), captaincy-general-of-chile /keyframe_review/1/to 1598->1603, saint-domingue /ledger/2 confidence 3->2.
- Layering: these twelve colony dossiers draw land that spanish-empire and portuguese-empire (am-06-a/b) also draw from Cliopatria's empire shapes; the author subtracts sub-units only from their nominal parent. The orchestrator must decide whether colonies are drawn over the empire or subtracted from it; until then counterpart naming disagrees systematically (saint-domingue 1697, RdlP 1777, dutch-brazil 1630/1654, french-louisiana 1800).
- Louisiana end date conflicts across three dossiers: spanish-louisiana ends 1801-03, french-louisiana (am-06-c) starts 1800, spanish-empire (am-06-b) keeps Louisiana to 30 November 1803.
- Guatemala's Peten overlap involves itza-mayans (am-02), already written; spanish-empire also needs a 1750 loss (Madrid) and a 1777 Hispaniola gain if the empire-level ledger is to mirror these colonies.
- No page failed to load; WebFetch summaries were used for quotes (Viceroyalty of New Spain page was read to 100,000 of 101,201 characters).

## Counterparts needing dossiers

- Pueblo Revolt (Pueblo peoples) (pueblo-revolt, 1680-1692)
- Mapuche (independent Araucania) (mapuche, 1598-1883)
- French Florida (Fort Caroline) (french-florida, 1564-1565)
- Captaincy General of Santo Domingo (Spanish Hispaniola; also Venezuela's audiencia before 1717/1739) (captaincy-general-of-santo-domingo, 1535-1821)
- British West Florida (british-west-florida, 1763-1783)
- British East Florida (british-east-florida, 1763-1783)

## Gazetteer names needed

- Arauco (San Felipe de Araucan) (place, captaincy-general-of-chile)
- Santa Cruz de Coya (place, captaincy-general-of-chile)
- Mosquito Coast (region, viceroyalty-of-new-granada)
- Maynas (region, viceroyalty-of-new-granada)
- Neutral Ground (Sabine-Arroyo Hondo) (region, viceroyalty-of-new-spain)
- Upper Artibonite (region, saint-domingue)
- Misiones Orientales (region, viceroyalty-of-the-rio-de-la-plata)
