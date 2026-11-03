# Review: batch am-08-h (the republics from 1810, part h)

Reviewer am-08-h, 2026-10-19. Six dossiers; validator (with --resolve) 0 errors, one warning (Motozintla, gazetteer). Spot checks: 4-8 events per dossier on the pages cited; no fabricated or mis-dated event at confidence 3. Three small fixes applied in place by the reviewer and re-validated (marked applied below); everything else is for the author or a gap-filler.

## second-mexican-empire: FIX

Area: infobox None km2, Cliopatria 2006419 km2, ratio None, acknowledged True. The infobox gives no area (checked). Cliopatria's whole-country shape is a claim; all four keyframes are adjust to the held extent, and the note says so.

Fixes:
- `/ledger/2 (was /ledger/0)` [APPLIED by reviewer] The Monterrey occupation_start had no month, so it sorted before the found event of April 1864, and its note said no page dated the capture. Evidence: Second French intervention in Mexico page: 'Vidaurri's forces captured Monterrey on 15 August' (1864); the Federated Republic dossier's mirror (L38) is 1864-08. Fix: Set month 8, source to the Second French intervention page (already in sources[]), rewrote the note with the quote; the event now sits after the April 1864 events. Re-validated: 0 errors.
- `/keyframe_review/1/correction and /keyframe_review/2/correction` [author] The 1865 and 1866 corrected extents leave out the ports the pages say the Imperialists held, so the ledger's 1866 losses of Guaymas (/ledger/8), Matamoros (/ledger/10) and Mazatlán (/ledger/11) take away land the Empire is never drawn holding. Evidence: Gazetteer: the intersection of the K1 correction with a 60 km radius round Mazatlán, Guaymas and Matamoros is 0 cells (Tampico 4 cells out of about 45). Second French intervention page: 'Castagny went to Mazatlán to follow up on the Imperialist victory there from the previous November' (November 1864); Negrete 'retreated from Matamoros after facing Tomás Mejía and French troops' (1865); 'with Castagny hoping to capture Guaymas' (1865); 'The Mexican Gulf port of Tampico was captured by the French Navy on 11 August' (1863). K2's note says the 1866 losses 'trim' the shape, which they cannot do for land it does not hold. Fix: Add Mazatlán, Matamoros, Guaymas and Tampico (60 km radii, as in the losses) to the 1865 and 1866 corrections, each with an occupation_start (counterpart federated-republic-of-mexico) at the date the page gives (Mazatlán 1864-11, Tampico 1863-08 or the found event, Matamoros and Guaymas 1865) and turn the 1866 losses of those ports into the matching occupation_end, so the pairs validate; or, if the extent is kept, delete those losses.
- `/ledger/16/region` [author] The dissolve region of June 1867 still includes Querétaro, which the ledger loses in May 1867 (/ledger/15). Evidence: Second French intervention page: 'on the night of 14 May, he opened the gates of Querétaro to the Republicans'; /ledger/17 (occupation_end, same month) already omits Querétaro. Fix: Drop the Santiago de Querétaro radius from the dissolve region (Mexico City and Veracruz only).

Thin (for a gap-filler):
- `/ledger (no event)` The Empire as a client of France 1864-1867: the infobox says 'Independent monarchy, client state of France'; the vassal tie belongs in the second-french-empire ledger (eu-20, not written yet), from April 1864 to the French evacuation (Bazaine left Mexico City 5 February 1867). Page: https://en.wikipedia.org/wiki/Second_Mexican_Empire
- `/keyframe_review/1` Imperial extent in Puebla, Guanajuato, Michoacán, Yucatán and the Pacific coast in 1865 rests on cities named on two pages (page budget 2/2). Page: https://en.wikipedia.org/wiki/Siege_of_Quer%C3%A9taro

Spot checks:
- `/ledger/2 (Monterrey, 1864)` mis-dated: page dates it 15 August 1864; month added (fix applied) (https://en.wikipedia.org/wiki/Second_French_intervention_in_Mexico)
- `/ledger/4 (Chihuahua, 1865-08)` confirmed: 'He entered Chihuahua City ... on 15 August' (https://en.wikipedia.org/wiki/Second_French_intervention_in_Mexico)
- `/ledger/5 (Tampico, 1866-07)` confirmed: 'The French held the port but surrendered in July' (https://en.wikipedia.org/wiki/Second_French_intervention_in_Mexico)
- `/ledger/7 (Saltillo, 1866-08)` confirmed: 'Monterrey was evacuated by the Imperialists on 25 July, and Saltillo on 4 August' (https://en.wikipedia.org/wiki/Second_French_intervention_in_Mexico)
- `/ledger/11 (Mazatlán, 1866-11)` confirmed: 'On 13 November, the French completed the evacuation of Mazatlán' (https://en.wikipedia.org/wiki/Second_French_intervention_in_Mexico)
- `/ledger/13 (Guadalajara, 1866-12)` confirmed: 'abandoned by the French on 12 December 1866' (https://en.wikipedia.org/wiki/Second_French_intervention_in_Mexico)
- `/ledger/15 (Querétaro, 1867-05)` confirmed: 'on the night of 14 May' (https://en.wikipedia.org/wiki/Second_French_intervention_in_Mexico)
- `/ledger/16 (dissolve, 1867-06)` confirmed: 'formally ended on 19 June 1867' (https://en.wikipedia.org/wiki/Second_Mexican_Empire)

## republic-of-colombia: FIX

Area: infobox 1141748 km2, Cliopatria 1149958 km2, ratio 1.007, acknowledged True. 

Fixes:
- `/ledger/4 and /ledger/5` [author] The Peruvian seizure of Leticia is coded only as a contest; the Peru dossier codes it as an occupation of Colombian land (republic-of-peru L30 occupation_start 1932-09, L31 occupation_end 1933-05), and an occupation must be recorded by the owner with the roles reversed. Evidence: Colombia-Peru War page: 'In the early hours of September 1, 1932, what is now known as the Leticia Incident took place'; 'lasted from September 1, 1932, to May 24, 1933'. Leticia page: 'The conflict lasted until May 1933, when a cease-fire negotiated by the League of Nations went into effect'; 'The League finally awarded the disputed area to Colombia in June 1934.' Schema: 'the owner records the same event with the roles reversed'. Fix: Add occupation_start 1932-09 and occupation_end 1933-05 (counterpart republic-of-peru, the Leticia region already used), sourced to the Colombia-Peru War page; keep the contest pair only if fighting outside Leticia is wanted (it then ends 1933-05 with the cease-fire, not 1934-06), and say in the note that the League commission held Leticia until June 1934.

Thin (for a gap-filler):
- `/wars/0` Thousand Days' War (1899-1902): no zones; the Colombia page dates the war and its end in 1902 only. Page: https://en.wikipedia.org/wiki/Thousand_Days%27_War
- `/ledger/2` Leticia handover date (1930) and the 1922 treaty text: the author's two failed URLs misspell the title (Salómon); the article is 'Salomón–Lozano Treaty'. Page: https://en.wikipedia.org/wiki/Salom%C3%B3n%E2%80%93Lozano_Treaty
- `/ledger (no events)` Venezuelan frontier (1891 Spanish award, 1922 Swiss award, 1941 treaty) and Ecuadorian frontier (1916 treaty); Cliopatria shows no change, so these are dates for the certainty notes, not border moves. Page: https://en.wikipedia.org/wiki/Colombia%E2%80%93Venezuela_border

Spot checks:
- `/ledger/1 (split, 1903-11)` confirmed: 'formalized on 3 November 1903' (https://en.wikipedia.org/wiki/Separation_of_Panama_from_Colombia)
- `/ledger/2 (Leticia gain, 1928)` confirmed: 'despite the treaty's ratification in 1928' (no month) (https://en.wikipedia.org/wiki/Leticia,_Amazonas)
- `/ledger/4 (contest_start, 1932-09)` confirmed: 'September 1, 1932' (https://en.wikipedia.org/wiki/Colombia%E2%80%93Peru_War)
- `/ledger/5 (contest_end, 1934-06)` confirmed: 'awarded the disputed area to Colombia in June 1934'; the cease-fire is May 1933 (https://en.wikipedia.org/wiki/Leticia,_Amazonas)
- `/ledger/3 (gain from Brazil, 1928)` confirmed: the 1928 treaty is on the page; which side gained is not (confidence 2 is right) (https://en.wikipedia.org/wiki/Brazil%E2%80%93Colombia_border)

## mexico: FIX

Area: infobox 1972550 km2, Cliopatria 1995099 km2, ratio 1.011, acknowledged True. 

Fixes:
- `/identity/wikidata` [author] identity.wikidata is Q5062192, which is the Centralist Republic's item, as the dossier's own notes say. Evidence: polities.csv: centralist-mexico 'Centralist Republic of Mexico', Q5062192; the Mexico row borrows it. The notes field: 'the Q5062192 id is the Centralist Republic's and should not be used for the state page link'. Fix: Set identity.wikidata to Mexico's own item (Q96, to be confirmed by whoever can reach Wikidata) or to null.
- `/ledger/4/region, /ledger/5/region, /wars/0/zones/0` [author] The Maderista zone is drawn as the whole state of Chihuahua (about 247,000 km2), against the 28,831 km2 zone the keyframe note describes and the 34,589 km2 Maderistas row. Evidence: keyframe_review/5 note: 'Cliopatria cuts a Maderista zone of 28,831 km2 in Chihuahua'; shapes.csv maderistas_1911 34,588.9 km2, bbox -107.86..-105.25, 27.48..29.41. Fix: Use {"cliopatria": "Maderistas", "year": 1911} (or the minus of Mexico 1912 and Mexico 1911) with the same text in both events and the war zone.
- `/ledger (missing events)` [author] The US occupation of Veracruz in 1914 is on two pages the author opened but is not in the ledger; the notes say the revolution pages 'name no zones'. Evidence: Mexican Revolution page: 'the seizure and occupation of the port of Veracruz by U.S. Marines and sailors' (April 1914), 'a seven-month stalemate', 'American forces eventually left Veracruz in the hands of the Carrancistas'; Mexico page: 'Wilson ordered troops to occupy the strategic port of Veracruz in 1914.' Fix: Add occupation_start 1914-04 and occupation_end 1914-11 (counterpart united-states-of-america, {"place": "Veracruz", "km": 30}), the end month from the 'seven-month' span at confidence 2; the Pershing expedition (March 1916 to early 1917, Chihuahua) may be added the same way.
- `/ledger/8 and /ledger/9` [author] The 1970 and 2009 Rio Grande exchanges are coded one way only. Evidence: Mexico-United States border page: 1970 treaty 'transferred an area of Mexican territory to the U.S., near Presidio and Hidalgo' and 'the U.S. ceded other land to Mexico, including five parcels near Presidio'; 24 November 2009 'the U.S. ceded 6 islands in the Rio Grande to Mexico' while 'Mexico ceded 3 islands and 2 bancos to the U.S.' Fix: Add a 1970 gain (counterpart united-states-of-america, {"place": "Ojinaga", "km": 10} or the Rio Grande region, the page's words) and a 2009-11 loss (3 islands and 2 bancos). Both are below one cell; confidence 2.

Thin (for a gap-filler):
- `/ledger/4` Maderista loss is confidence 1: the page dates no capture and no extent before May 1911. Page: https://en.wikipedia.org/wiki/Battle_of_Ciudad_Ju%C3%A1rez_(1911)
- `/keyframe_review/7` 1913-1919 is the whole country: Villa's Chihuahua (governor 1914), Zapata's Morelos and the Convention's capital (December 1914) are on the Mexican Revolution page without extents. Page: https://en.wikipedia.org/wiki/Convention_of_Aguascalientes
- `/keyframe_review/1` The Caste War: 'The Caste War continued to flare up in Yucatán' (Restored Republic page); the Maya state of Chan Santa Cruz held eastern Yucatán until 1901 and has no row or dossier. Page: https://en.wikipedia.org/wiki/Caste_War_of_Yucat%C3%A1n
- `/ledger (no event)` Belize-Mexico treaty (1893) and Clipperton (1931; below the grid). Page: https://en.wikipedia.org/wiki/Belize%E2%80%93Mexico_border

Spot checks:
- `/ledger/0 (found, 1867-07)` confirmed: 'President Juárez entered the city on the morning of July 15' (https://en.wikipedia.org/wiki/Restored_Republic)
- `/ledger/1 (loss, 1873)` confirmed: 'By 1873 ... cut off approximately 2.4 square kilometers' (https://en.wikipedia.org/wiki/Mexico%E2%80%93United_States_border)
- `/ledger/3 (gain Motozintla, 1882-09)` confirmed: 'September 27 of 1882'; 'Mexico received the county of Motozintla' (https://en.wikipedia.org/wiki/Guatemala%E2%80%93Mexico_border)
- `/ledger/5 (gain from Maderistas, 1911-05)` confirmed: 'signed on 21 May 1911'; 'Díaz resigned in May 1911' (https://en.wikipedia.org/wiki/Mexican_Revolution)
- `/ledger/9 (gain, 2009-11)` confirmed: 'On November 24, 2009, the U.S. ceded 6 islands in the Rio Grande to Mexico' (the reverse transfer is missing, see fixes) (https://en.wikipedia.org/wiki/Mexico%E2%80%93United_States_border)

## brazilian-republic: THIN

Area: infobox 8510346 km2, Cliopatria 8530587 km2, ratio 1.002, acknowledged True. 

Fixes:
- `/ledger/4/region` [APPLIED by reviewer] The land Brazil gave Bolivia was a 60 km radius round -65.4,-10.0 (about 11,300 km2), almost four times the page's figure, and did not match Bolivia's mirror. Evidence: Treaty of Petrópolis page: 'over 3,000 km2 of Brazilian territory between the Abuna River and Madeira River'; bolivia L16 uses {"place": "Abunã", "km": 31}. Fix: Region set to {"place": "Abunã", "km": 31, "country": "Brazil"} with the same text, reviewer remark added to the note. Re-validated: 0 errors, 0 warnings.
- `/ledger/7` [author] A 1928 gain of one cell from Peru near Tabatinga cites the Brazil-Colombia border page, which says nothing about Peru's land; the Peru dossier has no matching loss. Mexico's dossier treats changes of this size as grid noise with no event. Evidence: Brazil-Colombia border page: the only mention of Peru is the phrase 'Brazilian-Peruvian antecedent'; republic-of-peru has no 1928 event with brazilian-republic. Fix: Delete the event and say in /keyframe_review/4 that the cell is grid noise, or keep it at confidence 1 and send the mirror to republic-of-peru; not blocking.

Thin (for a gap-filler):
- `/ledger/5` The Roraima gain of 1904 is confidence 1: the page gives the award (15 June 1904) but not what Brazil kept. Page: https://en.wikipedia.org/wiki/Pirara
- `/ledger/10, /ledger/11, /ledger/12` 1936 Porto Murtinho cell changes (Paraguay, Bolivia) are confidence 1 with no page; neither neighbour's ledger has them. Page: https://en.wikipedia.org/wiki/Brazil%E2%80%93Paraguay_border
- `/ledger/9, /ledger/17` Renames of 1932 and 1967 are confidence 1 (Cliopatria's labels; the dates of the 1934 and 1967 constitutions are not opened). Page: https://en.wikipedia.org/wiki/Constitution_of_Brazil
- `/ledger (no events)` Amapá (1 December 1900 Swiss award against France) and Palmas (1895 Cleveland award against Argentina) are inside the 1890 shape with no event; the Peru treaty of 1909 is not opened. Page: https://en.wikipedia.org/wiki/Argentina%E2%80%93Brazil_border
- `/wars` Rebel-held land of the Federalist Revolution (1893-1895), Canudos (1896-1897), the Contestado (1912-1916) and the São Paulo Constitutionalist zone of 1932 (zones: []) is not coded. Page: https://en.wikipedia.org/wiki/Constitutionalist_Revolution
- `/ledger/1` The Acrean rebels (Republic of Acre, 1899-1903) are the counterpart Brazil occupied in 1903; no dossier (author's counterparts_needing_dossiers). Page: https://en.wikipedia.org/wiki/Acre_War

Spot checks:
- `/ledger/3 (gain Acre, 1903-11)` confirmed: 'signed on November 17, 1903'; 'the territory of Acre (191,000 km2)' (https://en.wikipedia.org/wiki/Treaty_of_Petr%C3%B3polis)
- `/ledger/4 (loss to Bolivia, 1903-11)` confirmed: date confirmed; region over-drawn, fixed (https://en.wikipedia.org/wiki/Treaty_of_Petr%C3%B3polis)
- `/ledger/1 (occupation, 1903)` confirmed: Rio Branco 'ordered the Acre occupation' after 27 January 1903 (https://en.wikipedia.org/wiki/Acre_War)
- `/ledger/5 (Roraima, 1904-06)` confirmed: award 'June 15, 1904', 'ruled in favor of Britain'; Brazil's share not given (confidence 1 is honest) (https://en.wikipedia.org/wiki/Brazil%E2%80%93Guyana_border)
- `/ledger/16 (rename, 1964-04)` confirmed: 'deposed in April 1964 by a coup' (https://en.wikipedia.org/wiki/Brazil)
- `/ledger/19 (rename, 1988-10)` confirmed: 'promulgated on 5 October 1988' (https://en.wikipedia.org/wiki/Brazil)

## cuban-nationalists: PASS

Area: infobox None km2, Cliopatria 56839 km2, ratio None, acknowledged True. No infobox area on the Republic of Cuba in Arms page; the shape is Oriente and Camagüey, consistent with the page's 1897 sentence.

Tried and could not break: Years against two pages (all five confirmed), the Spain counterpart against Cliopatria's rows (Kingdom of Spain holds Cuba after 1879, the Spanish Empire row ends 1879), keyframe corrections against the shape cell counts, capital inside the bbox, certainty span. The Spain slug conflict with the spanish-empire dossier and the US counterpart are other dossiers' problems (cross_checks).

Thin (for a gap-filler):
- `/keyframe_review/1` No page gives the extent of rebel-held land ('the Republic lacked control over stable territory'); the 1897 sentence 'the liberation army maintained a privileged position in Camagüey and Oriente, where the Spanish controlled only a few cities' supports the shape but not a border. Page: https://en.wikipedia.org/wiki/Spanish%E2%80%93American_War
- `/identity/capitals/0` No seat: the Council of Government 'operated in the field, relocating frequently'; the Camagüey dot is a reading (the author says so). Page: https://en.wikipedia.org/wiki/Republic_of_Cuba_in_Arms

Spot checks:
- `/ledger/0 (found, 1895-02)` confirmed: 'The insurrection began on February 24, 1895'; Oriente (https://en.wikipedia.org/wiki/Cuban_War_of_Independence)
- `/ledger/1 (gain Camagüey, 1895-06)` confirmed: 'By the end of June, all of Camagüey was at war' (https://en.wikipedia.org/wiki/Cuban_War_of_Independence)
- `/ledger/3 (contest_start, 1896-01)` confirmed: 'arrived at the westernmost tip of the island on January 22, 1896' (https://en.wikipedia.org/wiki/Cuban_War_of_Independence)
- `/ledger/4 (contest_end, 1898-12)` confirmed: 'On December 10, 1898, the United States and Spain signed the Treaty of Paris' (https://en.wikipedia.org/wiki/Cuban_War_of_Independence)
- `/ledger/5 (dissolve, 1899-04)` confirmed: 'the dissolution of the Representative Assembly on April 4, 1899' (https://en.wikipedia.org/wiki/Republic_of_Cuba_in_Arms)

## republic-of-cuba: FIX

Area: infobox 110860 km2, Cliopatria 123918 km2, ratio 1.118, acknowledged True. Infobox 110,860 km2 (undated) on both the Cuba and Republic of Cuba pages; Cliopatria 120,880 (1905) to 124,490 (1960); the author's notes give the coastal-cell reason.

Fixes:
- `/ledger/1` [APPLIED by reviewer] The Guantánamo lease was a 30 km radius round Guantánamo city (about 2,800 km2, centred inland, 20 km from the base) at confidence 1 with no month, sourced to a page that gives no year. Evidence: Guantanamo Bay Naval Base page: agreement 'signed 16 February 1903; 23 February 1903' (second part 2 July 1903); the base lies 'on 45 square miles (117 km2) of land and water on the shore of Guantánamo Bay'. The gazetteer has the Natural Earth unit 'USNB Guantanamo Bay'. Fix: Set month 2, region {"country": "USNB Guantanamo Bay"} with the page's words, source the Guantanamo Bay Naval Base page (added to sources[], accessed 2026-10-19), confidence 3, note rewritten. Re-validated: 0 errors, 0 warnings. The US dossier's mirror (L89, 1903-12, 30 km radius) should take the same region.

Thin (for a gap-filler):
- `/ledger (no event)` Sugar Intervention 1917-1922: 'in 1917, U.S. Marines returned to Cuba to quell a revolution' (Republic of Cuba page), with no place; an occupation of part of Oriente if a page names it. Page: https://en.wikipedia.org/wiki/Sugar_Intervention
- `/ledger (no event)` Client state of the United States 1902-1934 ('From 1902 to 1934, Cuban and U.S. law included the Platt Amendment'; Treaty of Relations 29 May 1934): by the schema the vassal_start/vassal_end belong in the US ledger (am-07), counterpart republic-of-cuba. Page: https://en.wikipedia.org/wiki/Platt_Amendment

Spot checks:
- `/ledger/0 (found, 1902-05)` confirmed: 'Cuba gained formal independence on 20 May 1902, as the Republic of Cuba' (https://en.wikipedia.org/wiki/Republic_of_Cuba_(1902%E2%80%931959))
- `/ledger/2 (occupation_start, 1906-09)` confirmed: Provisional Government 29 September 1906 (https://en.wikipedia.org/wiki/Second_Occupation_of_Cuba)
- `/ledger/3 (occupation_end, 1909-01)` confirmed: Gómez took office 28 January 1909; 'last American forces leaving ... on 6 February 1909' is in the note (https://en.wikipedia.org/wiki/Second_Occupation_of_Cuba)
- `/ledger/4 (gain Isle of Pines, 1925-03)` confirmed: 'ratified by the United States Senate on March 13, 1925'; infobox 'Effective: 23 March 1925' (https://en.wikipedia.org/wiki/Hay%E2%80%93Quesada_Treaty)
- `/ledger/6 (gain from rebels, 1959-01)` confirmed: 'fled Cuba by air for the Dominican Republic just hours later on 1 January 1959' (https://en.wikipedia.org/wiki/Cuban_Revolution)
- `/ledger/1 (Guantánamo, 1903)` mis-dated: year right, no month and an over-drawn region at confidence 1; fixed (https://en.wikipedia.org/wiki/Guantanamo_Bay_Naval_Base)

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| second-mexican-empire 1864 found (mexican-monarchists) | mexican-monarchists 1864 dissolve | matched | both April 1864 |
| second-mexican-empire 1864 occupation_start (federated-republic-of-mexico) | federated-republic-of-mexico 1864 occupation_start | matched | April 1864, Mexican Monarchists 1864 shape on both sides |
| second-mexican-empire 1864 occupation_start (federated-republic-of-mexico) | federated-republic-of-mexico 1864 occupation_start | mismatch | Monterrey, August 1864 on both sides (after the reviewer's month fix), but the land differs: a 100 km radius round Monterrey here, all of Nuevo León and Coahuila in the Federated Republic (L38) |
| second-mexican-empire 1865 occupation_start (federated-republic-of-mexico) | federated-republic-of-mexico - - | missing | Oaxaca (1865) not in the Federated Republic ledger (am-08-c) |
| second-mexican-empire 1865 occupation_start (federated-republic-of-mexico) | federated-republic-of-mexico - - | missing | Chihuahua (15 August 1865) not in the Federated Republic ledger (am-08-c) |
| second-mexican-empire 1866 occupation_end (federated-republic-of-mexico) | federated-republic-of-mexico 1867 occupation_end | mismatch | Monterrey evacuated 25 July 1866 here; the Federated Republic keeps Nuevo León and Coahuila occupied until June 1867 (L45) |
| second-mexican-empire 1866 occupation_end (federated-republic-of-mexico) | federated-republic-of-mexico - - | missing | Oaxaca retaken 1 November 1866: no mirror (no start either) |
| second-mexican-empire 1866 loss (federated-republic-of-mexico) | federated-republic-of-mexico - gain | missing | The eight 1866-1867 Republican recaptures (Tampico 1866-07, Saltillo 1866-08, Guaymas 1866-09, Matamoros, Mazatlán, Durango 1866-11, Guadalajara 1866-12, Querétaro 1867-05) have no mirror; the Federated Republic ledger keeps its whole occupation to June 1867 (am-08-c) |
| second-mexican-empire 1867 occupation_end (federated-republic-of-mexico) | federated-republic-of-mexico - - | missing | Chihuahua retaken March 1867: no mirror |
| second-mexican-empire 1867 occupation_end (federated-republic-of-mexico) | federated-republic-of-mexico 1867 occupation_end | matched | June 1867, the central core (L44) |
| second-mexican-empire 1867 dissolve (mexico) | mexico 1867 found | matched | June / July 1867 |
| republic-of-colombia 1886 found (united-states-of-colombia) | united-states-of-colombia 1886 dissolve | matched | 1886, same shape |
| republic-of-colombia 1903 split (republic-of-panama) | republic-of-panama - - | exception | republic-of-panama has no dossier yet; another part of am-08 owns it (not run) |
| republic-of-colombia 1928 gain (republic-of-peru) | republic-of-peru 1928 loss | matched | Peru gives March 1928; the Leticia page gives no month |
| republic-of-colombia 1928 gain (brazilian-republic) | brazilian-republic 1928 loss | matched | 3 cells on the Apaporis, both confidence 2 |
| republic-of-colombia 1932 contest_start (republic-of-peru) | republic-of-peru 1932 occupation_start | mismatch | Peru codes an occupation of Leticia 1932-09 to 1933-05 (L30-L31); Colombia codes a contest 1932-09 to 1934-06 and no occupation (fix listed) |
| mexico 1867 found (second-mexican-empire) | federated-republic-of-mexico 1867 dissolve | matched | both predecessors dissolve into mexico in June 1867 |
| mexico 1873 loss (united-states-of-america) | united-states-of-america - gain | missing | 2.4 km2 cut off by the Rio Grande; no mexico events in the US ledger (am-07) |
| mexico 1882 gain (guatemala) | guatemala - loss | missing | Motozintla, treaty of 27 September 1882; the Guatemala ledger has only the 1842 Soconusco loss (am-08 part) |
| mexico 1911 loss (maderistas) | maderistas - - | exception | maderistas has no dossier yet; another part of am-08 owns it (not run) |
| mexico 1911 gain (maderistas) | maderistas - - | exception | as above |
| mexico 1963 gain (united-states-of-america) | united-states-of-america - loss | missing | Chamizal; also the 1963 loss, the 1970 loss and the 2009-11 gain have no US mirror (am-07). All below one cell |
| brazilian-republic 1889 found (empire-of-brazil) | empire-of-brazil 1889 dissolve | matched | 15 November 1889 |
| brazilian-republic 1903 occupation_start (bolivia) | bolivia - occupation_start | missing | Brazil's occupation of Acre (ordered after 27 January 1903): Bolivia's ledger has no occupation (am-08 part) |
| brazilian-republic 1903 gain (bolivia) | bolivia 1903 loss | matched | Acre, 17 November 1903, both confidence 3 |
| brazilian-republic 1903 loss (bolivia) | bolivia 1903 gain | matched | Abunã strip; the land now agrees (reviewer fix, 31 km on both sides) |
| brazilian-republic 1904 gain (nobody) | nobody - - | exception | Roraima north-east, confidence 1 |
| brazilian-republic 1928 gain (republic-of-peru) | republic-of-peru - loss | missing | one cell near Tabatinga, confidence 1, probably grid noise (fix listed) |
| brazilian-republic 1936 gain (paraguay) | paraguay - loss | missing | Porto Murtinho cells, confidence 1; also the 1936 loss to Paraguay |
| brazilian-republic 1936 gain (bolivia) | bolivia - loss | missing | 4 cells, confidence 1 |
| cuban-nationalists 1895 found (kingdom-of-spain) | spanish-empire 1895 contest_start | mismatch | kingdom-of-spain has no dossier (eu-12, not run), but the spanish-empire dossier (life to 1899-02, successors include cuban-nationalists) holds Cuba until 1899 and codes a contest over all of Cuba from 1895 (L116) with no loss. Cliopatria's Spanish Empire row ends in 1879 and its Kingdom of Spain row holds Cuba after; the orchestrator must say which slug owns Spain's Cuba in 1895-1899 |
| cuban-nationalists 1896 contest_start (kingdom-of-spain) | spanish-empire 1895 contest_start | mismatch | here January 1896 over Cuba minus the rebel zone; spanish-empire 1895 over all of Cuba; different Spain slug |
| cuban-nationalists 1898 contest_end (kingdom-of-spain) | spanish-empire 1898 contest_end | matched | 10 December 1898 on both sides (different Spain slug) |
| cuban-nationalists 1899 dissolve (united-states-of-america) | united-states-of-america 1898 occupation_start | mismatch | the US ledger occupies Cuba from 1898-12 with counterpart republic-of-cuba (L82), a state that did not exist until 1902; the counterpart should be the Spain slug or cuban-nationalists (am-07) |
| republic-of-cuba 1902 found (united-states-of-america) | united-states-of-america 1902 occupation_end | matched | 20 May 1902 |
| republic-of-cuba 1903 loss (united-states-of-america) | united-states-of-america 1903 gain | matched | lease February 1903 here, possession 10 December 1903 in the US (L89); the US region (30 km radius) should become 'USNB Guantanamo Bay' |
| republic-of-cuba 1906 occupation_start (united-states-of-america) | united-states-of-america 1906 occupation_start | matched | September 1906 |
| republic-of-cuba 1909 occupation_end (united-states-of-america) | united-states-of-america 1909 occupation_end | matched | January 1909 |
| republic-of-cuba 1925 gain (united-states-of-america) | united-states-of-america - loss | missing | Isle of Pines, Hay-Quesada effective 23 March 1925; the US ledger lacks the loss (author flagged; am-07) |
| republic-of-cuba 1958 loss (cuban-communists) | cuban-communists - - | exception | cuban-communists has no dossier yet; another part of am-08 owns it (not run); also the 1959-01 gain |
| republic-of-cuba 1902 vassal_start (united-states-of-america) | united-states-of-america - vassal_start | missing | not an event in either ledger: Cuba as a US client 1902-1934 (Platt Amendment; Treaty of Relations 29 May 1934) belongs in the US ledger (am-07) |

## Problems for the orchestrator

- Reviewer applied three small fixes in place and re-validated each (0 errors): second-mexican-empire /ledger/2 (month 8 and source), brazilian-republic /ledger/4 (region), republic-of-cuba /ledger/1 (month, region, source, confidence; one source added).
- Spain in Cuba 1880-1899: the spanish-empire dossier (another group) extends to February 1899 and codes the Cuban contest, while Cliopatria's Spanish Empire row ends in 1879 and cuban-nationalists uses kingdom-of-spain (eu-12, not written). The orchestrator must pick one slug and route the fix.
- united-states-of-america (am-07): no events with mexico after 1854 (1873, 1963, 1970, 2009 Rio Grande changes; 1914 Veracruz and 1916 Pershing occupations), no Isle of Pines loss (March 1925), no vassal events for Cuba 1902-1934, and its 1898-12 Cuba occupation names republic-of-cuba as counterpart.
- federated-republic-of-mexico (am-08-c) and second-mexican-empire disagree on the Empire's extent after 1864: the Federated Republic has no 1865 occupations (Oaxaca, Chihuahua) and no 1866 Republican recaptures.
- The author's failed Salomón-Lozano URLs misspell the title (Salómon); the right title is 'Salomón–Lozano Treaty'.
- Wikidata could not be reached to confirm Mexico's item id (Q96); action=info on Wikipedia failed to load.

Counterparts needing dossiers: Republic of Acre (republic-of-acre, [1899, 1903]); Chan Santa Cruz (Maya state of the Caste War) (chan-santa-cruz, [1850, 1901])
