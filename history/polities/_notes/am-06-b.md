# am-06-b: Spanish Empire (research notes)

One state, one dossier: `history/polities/spanish-empire.json` (Cliopatria row 'Spanish Empire', 1516..1879, 76 shapes; the dossier runs 1516 to February 1899 after the repair of 2026-10-19). 92 keyframe verdicts (21 ok, 70 adjust, 1 wrong; 16 of them are new keyframes), 126 ledger events (1 at confidence 1), 26 wars, 36 sources. Validates with 0 errors; `--resolve` gives 2 warnings (the place 'Sidi Ifni' is not in the gazetteer; the vassal_start of sultanate-of-sulu has no end because it lasts to the end of the state).

Written by am-06-b from 14 Wikipedia pages opened with WebFetch on 2026-10-19 (the page budget; one more URL failed, see below), then repaired the same day with 22 more pages (section 'Repair 2026-10-19' at the end). Every shape cites a page; in shapes 1572, 1659 and 1670 (and the Amazon block of 1778) a block of cells could not be checked within the budget and the note says 'unverified: page budget'. Many shape changes are dated by the pages only to the year or the span, so the evidence for a keyframe is usually 'the page gives the event, and Cliopatria's shape year matches it within a year'. Before the repair, confidence 1 marked seven events where the pages opened were silent and the year was Cliopatria's (Michoacán 1534, Yucatán 1547, Havana 1762 and 1763, Trinidad 1797, Venezuela 1812 and 1814); all seven now rest on pages. The one event at confidence 1 is the Treaty of Madrid block (1750).

## One row, not two

Cliopatria's rel-spanish-empire is an umbrella (1516..1931) and is not a state. The state is the 'Spanish Empire' row; the Kingdom of Spain row (1516..2024, the peninsula) and the First Spanish Republic row (1873..1876, one shape that holds Spain, Cuba and the Philippines) are separate rows to be handled by the dossier owners of those slugs. This dossier ends the colonial empire in February 1899 (Treaty of Paris signed 10 December 1898, Pacific islands sold to Germany on 12 February 1899, African posts passed to the Kingdom of Spain) though Cliopatria's row ends in 1879; the colonies from 1873 to 1899 are described in the new keyframes spanish-empire_1873, _1878 and _1899 and they overlap the First Spanish Republic and Kingdom of Spain rows (the owner of those slugs should drop the colonies from them, or the renderer should let this dossier win).

## The thin ending

Cliopatria's shape 1877 has one cell and is marked wrong; the 1865 and 1873 keyframes replace Cliopatria's colonies-only shapes 1853..1879 with the Dominican Republic removed (1865) and the Pacific islands added (1873, Guam, Northern Marianas, Carolines, Palau; the page gives Spain holding them to 1899).

## Portuguese lands 1582-1639

Cliopatria's Spanish Empire shapes 1582-1639 hold the Portuguese overseas lands (Brazil, Angola, Mozambique, Goa, Malacca and the rest). The Iberian Union page says the empires stayed separately administered. Every shape 1582..1636 carries an 'adjust' verdict whose geometry is unchanged and whose text says the Portuguese lands are a personal-union tint, and the ledger records them as vassal_start 1581 and vassal_end 1640 with counterpart portuguese-empire (portuguese-empire, am-06-a, records the same two dates as a loss in 1581 and a gain in 1640-12: the dates match, the event type does not; the earlier sentence that the two dossiers 'match' was true of the dates only). The renderer should draw the tint, not Spanish rule. The country list used to build the tint (PORT_COUNTRIES) is the researcher's reading of the 1595 shape and may omit small enclaves; nothing in the dossier removes cells.

## Louisiana is missing from cliopatria

the Spanish Empire row has no Louisiana at any date. The Louisiana (New Spain) page says France transferred Louisiana on 23 November 1762 and the transfer back to France took place on 30 November 1803 (the date Spain 'lost' it de facto; San Ildefonso 1800 is the de jure retrocession). Shapes 1762-1803 are 'adjust' with the gazetteer region 'Louisiana' added (about 10,200 cells). The French-Louisiana row (slug french-louisiana) should end 1762 and resume 1803 in its dossier; this dossier names it as the counterpart of the 1803 loss and new-france for 1762. The gazetteer region 'Louisiana' is the Louisiana Purchase by whole states and overshoots (its own note: Montana, Wyoming and Colorado are whole states, Minnesota east of the Mississippi is not included), so the added area is larger than the 2.28 million km2 that the page gives for the colony; the gazetteer agent may refine it.

## West florida and the floridas

the Cliopatria shape drops Spanish Florida in 1763 and 1702-1708 is misdated (the missions fell 1702-1704; the shape drops Florida 1702 to 1708). West Florida (Baton Rouge, Natchez, Mobile, Pensacola) is added in 1779-1781 by war and in 1783 by treaty; Natchez and the Mississippi/Alabama strip north of 31 N is left in the Spanish shape until the Pinckney Treaty (1795) by the keyframes 1783..1794. Adams-Onís: signed 22 February 1819, in force 17 July 1821 (Spanish Florida page). The pages opened give no western boundary line, so the 1819 line in the west is not drawn and the Texas and California edges stay as Cliopatria draws them.

THE MISIONES ORIENTALES (Rio Grande do Sul): Cliopatria keeps the seven missions in the Spanish shape from 1757 to 1810. The Guaraní War page: Treaty of Madrid 1750 gave them to Portugal, the war ran 1754-1756 (Caiboaté, 10 February 1756), and Spain ended the treaty (the page says 1759 in one place and El Pardo in 1761 in another). San Ildefonso (1 October 1777) returned them; Portuguese forces took them in 1801-1802 (Río de la Plata page), so the Cliopatria shape still holds them to 1810. Keyframes 1801-1805 give the corrected shape; the 1801 loss has the Rio Grande do Sul intersect.

## Peru and upper peru

the Cliopatria shapes of 1822 and 1824 remove the Peruvian highlands and Upper Peru early. The Independence page: Lima entered 12 July 1821, but Ayacucho (9 December 1824) and Tumusla (2 April 1825) end the royalist hold. Keyframes 1822 and 1824 correct this. Veracruz, Callao and Chiloé, which 'resisted until 1825-1826' (the page gives no finer dates; the ledger puts Veracruz in 1825, Callao and Chiloé in 1826 as confidence 2), are an enclaves keyframe (1825-1826). The Cliopatria shape 1853 and its later spans are the island colonies only. The mainland leftovers Cliopatria keeps to 1852 are removed by the keyframe 1827.

## Chile 1810-1820

the Independence page has the juntas of 1810, royalists in control 1814-1817 and San Martín in control of northern and central Chile by 10 February 1817. Cliopatria's shape drops central Chile in 1812 (moved to 1810 here), restores it in 1814 (confirmed by the page) and drops it in 1820 (moved to 1817 here). The cell sets are Cliopatria's own differences intersected with the gazetteer's country Chile, because the page names fronts, not borders. South of the Bío-Bío the Mapuche kept their land; the ledger records the 1599 loss (page: 'Destruction of the Seven Cities in 1599-1604') and the Araucanía counterpart needs a dossier.

## New spain claim vs control

the Spanish Empire infobox gives 13.7 million km2 for 1780, the Cliopatria shape 1780 holds 11.0 million km2 (Louisiana and the Floridas missing); the New Spain page gives 7.66 million km2 (1790) but Cliopatria's Mexico, Central America and borderlands cells hold about 2.4 million km2 (ratio 0.32), because the page counts the Spanish claim to the interior (Texas to California, the north) and Cliopatria draws the area under control. This dossier leaves the northern frontier as Cliopatria draws it and records the Pueblo Revolt (1680-1692), the California missions (1769) and the Jesuit expulsion (1767, Paraguay reducciones) as events; the Tordesillas line, the Amazon and the Chaco frontier are in the soft certainty band.

## Dates that disagree between pages

Formosa fell on 26 August 1642 (East Indies page) but a sidebar of the same page says Spain held it 'from 1575 until the Dutch invasion in 1646'; the 1642 date is used. The Spanish Empire page lists 'Jamaica (1655)' as an English colony and Cliopatria keeps both Jamaica and Taiwan in the Spanish shape to 1658 (new keyframes 1642 and 1655 take them out). The Spanish Empire page gives the Cuban wars as 1868-1878 and 1895-1898. Santo Domingo: Basel 1795, French rule from 1801 (Toussaint), Palo Hincado 7 November 1808, French capitulation 9 July 1809, independence proclaimed 1 December 1821 (Haiti invades 9 February 1822), annexation 18 March 1861 to July 1865; Cliopatria keeps the Spanish shape on Hispaniola until 1872.

STATES THAT NEED A DOSSIER OF THEIR OWN (counterparts used here): the rebel state Republic of Cuba in Arms (1868-1878) and cuban-nationalists (1895-1899) for Cuba; the Mapuche (Araucanía) and the Muisca Confederation as native states; Pueblo peoples (Pueblo Revolt); the Chichimeca peoples (war 1550-1591); Central America (Act of Independence), federal Provinces; and the Jesuit reducciones (slug jesuit-reducciones exists; its owner should take 1609..1767 and the Guaraní War). Slugs used and present in data/polities.csv: kingdom-of-portugal, aztec-triple-alliance, inca-empire, michoacan, later-mayan-city-states, itza-mayans, namayan, jesuit-reducciones, portuguese-empire, new-france, french-louisiana, british-colonial-empire, english-colonial-empire, dutch-republic, kingdom-of-france, haiti, first-french-empire, rio-de-la-plata, paraguay, new-granada, republic-of-venezuela, republic-of-chile, gran-colombia, first-mexican-empire, republic-of-peru, bolivia, federated-republic-of-mexico, morocco, dominican-republic, cuban-nationalists, united-states-of-america, german-empire.

## Pages that failed or were thin

Treaty_of_San_Ildefonso_(1777) did not exist (URL_NOT_FOUND); the page First_Treaty_of_San_Ildefonso (1 October 1777) was used instead. Treaty_of_Madrid_(1750) is a disambiguation-style stub with no treaty terms; its terms are taken from the Guaraní War page. Neither page gives the Amazon frontier. Cliopatria's 1778 shape adds about 4,600 cells in the Amazon basin (Amazonas and Acre in Brazil, Venezuela, Colombia, Ucayali) that the pages opened neither confirm nor refute; the keyframe keeps them (probably claim, not control) and its verdict is adjust only for Louisiana. A page on the Amazon boundary of 1777-1778 is needed.

## Gazetteer names the gazetteer lacks

place 'Sidi Ifni' (1860 gain; Cliopatria's 1861 shape already adds the Ifni cells, so the keyframes are unaffected). Names that resolved: region 'Louisiana', 'Yucatan', 'Peten'.

## Not covered

the European possessions (the peninsula belongs to the Kingdom of Spain row; Cliopatria's Spanish Empire shapes are overseas lands plus 30 cells of Spain in the late shapes), the Canary Islands, and everything after December 1898 (Spanish Morocco, Spanish Guinea, Spanish Sahara). Fernando Pó and Annobón (ceded by Portugal, 1778) are in the ledger as a gain; the later Cliopatria shapes carry 8 Equatorial Guinea cells.

## Open items for the reviewer and the gap-fillers

- Amazon block of the 1778 shape (about 4,600 cells): page silent, unverified.
- Northern frontier of New Spain (Texas to California) and the 1819 western line: pages give claims, not lines.
- (closed by the repair) Michoacán, Yucatán, Havana, Trinidad and Venezuela now have pages; see the repair section.
- The gazetteer region 'Louisiana' overshoots (whole states of Montana, Wyoming, Colorado).
- Dossiers wanted for the counterparts named in the report: Republic of Cuba in Arms (1868-1878), Mapuche (Araucanía), Muisca Confederation, the Pueblo rebels of 1680-1692, the Chichimeca peoples. The slug united-provinces-of-central-america (1824-1839) should take over from the 'Central America (Act of Independence)' counterpart of 1821.

## Repair 2026-10-19 (after the reviewer's fail)

Reviewer's verdict was fail (no fabricated or mis-dated event; missing and inconsistent land events). Eight unapplied fixes were done and ten thin items worked, from 22 pages opened for the purpose with WebFetch (36 sources in all). The dossier validates (0 errors; 2 warnings, see above) and the mount copy was read back after twelve seconds.

### What changed, by finding

1. African posts (Fernando Po, Annobon, Ifni): the 1873 and 1877 corrections and the new keyframes 1878 and 1899 carry the intersect of the 1861 shape with Equatorial Guinea and Morocco (12 cells); kingdom-of-spain is a successor with that land and the dissolve of February 1899 names it as counterpart. Page: Spanish Empire ('keeping only its African territories' after the German sale; Ifni returned to Morocco in 1969; Spanish Sahara withdrawn 1976).
2. Dissolve/US: the dossier now ends 1899-02. The 1898-12 losses (Puerto Rico, Guam, Philippines; Cuba) stay with the United States; a 1899-02 loss gives {Micronesia, Palau, Northern Mariana Islands} to german-empire (German-Spanish Treaty page: signed 12 February 1899, 25 million pesetas, Guam excluded); the dissolve (1899-02) hands only the African posts to kingdom-of-spain. The old dissolve (US as counterpart for the German sale) is gone.
3. Inca lands: 1537 gain (Spanish conquest page: Almagro seizes Cuzco in 1537, Manco flees to Vilcabamba), vassal_start 1567 and vassal_end 1571 (Neo-Inca State page: infobox 'Vassal of the Spanish Empire (1567–1571)', Acobamba 1566) and the 1572-06 gain (24 June 1572), all mirroring inca-empire. Keyframe 1540 is adjust with unchanged geometry: the Chilean, Bolivian and Argentine reach is claim (the page calls Almagro's Chile expedition 'a complete failure' and does not mention Bolivia).
4. Michoacán: moved from 1534 (confidence 1) to 14 February 1530 at confidence 3, source the Tarascan state page ('the king was executed on February 14, 1530'; the Michoacán page agrees on the year only). Nueva Galicia (Aguascalientes, Guanajuato, Colima, Jalisco, Nayarit, Zacatecas: 335 of the 446 Mexican cells the 1534 shape adds) is dated c. 1531 from the Nueva Galicia page (confidence 2, counterpart nobody). New keyframes 1530 and 1531; keyframe 1529 is adjust (unchanged for 1529). 111 cells (Sinaloa 43, rest of Michoacán 31, Querétaro 27, Hidalgo 8, Durango 1, México 1) are still unverified.
5. Colonia and southern Brazil: gain 1705-03 (14 March 1705), loss 1713, gain 1762-10 (11 October), loss 1763-12 (27 December) of Colonia (Colonia del Sacramento page); gain 1763 and loss 1776-02 of Rio Grande, gain 1777-02 and loss 1777-10 of Santa Catarina island (1776-1777 war page, First Treaty of San Ildefonso page); wars 'Fantastic War' and 'Spanish–Portuguese War (1776–1777)'; keyframes 1763, 1769, 1772, 1775 add Rio Grande, new keyframe 1777 adds Santa Catarina.
6. Iberian Union: the dossier keeps the vassal_start 1581 / vassal_end 1640-12 (personal-union tint). The Iberian Union page says 'Spain left the administration of Portugal and its empire largely to the Portuguese themselves', which supports the tint on both sides; portuguese-empire records a loss (1581) and a gain (1640-12) instead. Orchestrator: choose one representation for both; I recommend vassal events in both (portuguese-empire would then be the vassal, with a vassal_start of the same string).
7. Fernando Po: region now {Malabo 60 km} plus {admin1 Annobón}, month 3 (Treaty of El Pardo page: 'signed on 11 March 1778').
8. Philippines: certainty 1826-1898 is now soft (Spanish East Indies page: highlands of Luzon outside Spanish control into the early 19th century, Mindanao 'nominally under Spanish control', southern Palawan only in the late 1890s) with a sharp era for 1899. The 1873 and 1877 corrections leave the Sulu archipelago out (Cliopatria's Sultanate of Sulu row, cells that fall in the Philippines: 9, i.e. Sulu, Tawi-Tawi and Basilan) until the Treaty of Licup (22 July 1878; Spanish–Moro conflict page): contest 1876-02 to 1878-07 and vassal_start 1878-07 for sultanate-of-sulu; new keyframe 1878 has the whole Philippines.

### Thin items worked

Yucatán moved to 1546 at confidence 2 (page: late-1546 uprising, final conquest of the northern peninsula); Havana occupation 14 August 1762 at confidence 3 and return 1763 at confidence 2 (the page says February in one passage and April in another); Trinidad 18 February 1797; Venezuela 25 July 1812, Caracas lost 6 August 1813, royalist return 1814 (confidence 2); Oran loss 1708, gain 1732, loss 1792 with keyframes 1709-1727, 1732, 1778-1791 and 1792 (Spanish Oran page); Treaty of Madrid (13 January 1750) block as a gain from nobody at confidence 1 (the page does not say how the western Amazon was shared; the Spanish and Portuguese blocks of 1752 and of 1778 do not overlap); Treaty of Zaragoza (1529-04) loss of the Moluccas claim, drawn only where Cliopatria gives Portugal the Ambon patch; Philippine Revolution (contests 1896-08/1897-12 and 1898-05/1898-12 on Luzon); Hispano-Moroccan War (war entry only); Chincha Islands War (occupation 14 April 1864 to 1866 round Pisco).

### Where I disagree, or decided differently from the reviewer

- Dissolve option: I took the reviewer's first option (end 1899-02), because the Spanish Empire page itself says the Pacific islands were sold in 1899 and the African posts were kept.
- Colonia 1713 (reviewer: 1713/1715): the page's table gives Spain to 1713 and Portugal from 1714 and its text has possession taken on 10 February 1718, so the page disagrees with itself; I kept 1713 at confidence 2 (the table's last Spanish year, Cliopatria's year and portuguese-empire's year), source the Colonia del Sacramento page.
- Rio Grande 1763-1776 (reviewer): the Fantastic War page says Spain gave back all conquests except two forts, whereas the 1776-1777 war page has Spain withdrawing from the whole Rio Grande area in February 1776; I followed the later page. The fort sites (Santa Teresa, San Miguel) are in Uruguay inside the Spanish shape.
- Sulu 1878: the Spanish–Moro conflict page makes the Treaty of Licup a submission 'establishing Spanish sovereignty'; the Sultanate of Sulu page has a protectorate and a capitulation. I drew a vassal (the reviewer's proposal) and recorded the other reading in the note. The Sultanate of Sulu page does not describe an 1878 Spanish protectorate treaty: its 1878 instruments are the Overbeck agreement of 22 January 1878 over North Borneo (not Spanish) and a 'formal surrender and capitulation' with no document; it dates a Spanish protectorate 1851-1899 only in its infobox.
- Michoacán month: the Michoacán page (reviewer's source) gives only the year; the month comes from the Tarascan state page, which michoacan's author also cites for the dissolve.
- Treaty of Madrid mirror: portuguese-empire records its 1750-01 block as a gain from spanish-empire; the shapes show Cliopatria drawing both blocks from land neither side drew, so the Spanish event has counterpart nobody, not portuguese-empire. The orchestrator or the author of portuguese-empire should align the counterpart.

### Cross-dossier follow-ups for the orchestrator

portuguese-empire (am-06-a): Colonia (1706 loss and 1713 gain are Cliopatria's years at confidence 1; the page dates the Spanish capture to 14 March 1705 and the 1762 capture to 11 October 1762); 1801 gain of the Misiones Orientales from spanish-empire is still missing there; the 1750 and 1778 Amazon blocks (counterpart nobody, not spanish-empire); Iberian Union representation (item 6). Kingdom-of-Spain (eu-12) should list spanish-empire as predecessor for the African posts in 1899 and the Oran, Ceuta and Melilla stretch is theirs. inca-empire: mirrors now exist for 1537, 1567-1571 and 1572-06. The Sultanate of Sulu row (se-02) overlaps this land in 1878-1879 and should mirror the contest 1876-02 to 1878-07 and the vassalage from 1878-07.

### Pages that failed

https://en.wikipedia.org/wiki/Spanish%E2%80%93Portuguese_War_(1761%E2%80%931763) and https://en.wikipedia.org/wiki/Spanish%E2%80%93Portuguese_War_(1762%E2%80%931763) (URL_NOT_FOUND; the Fantastic War page was used). Not opened in the repair (still gaps): Spanish missions in Mexico (blocks of the 1572, 1659, 1670 and 1687 shapes), Adams–Onís Treaty (western line), pages on Béjaïa (1510-1555), the Peñón of Algiers (to 1529), Tripoli (1530) and Spanish Ternate and Tidore (1606-1663).

### New counterparts and gazetteer names

Counterpart needing a dossier: the Philippine revolutionaries (Katipunan, Republic of Biak-na-Bato, First Philippine Republic, 1896-1901). The Muisca Confederation dossier now exists (reviewer's fix, applied to /ledger counterpart). Gazetteer: place 'Chincha Islands' (replaced by a 30 km radius round Pisco), place 'Sidi Ifni' (as before).

