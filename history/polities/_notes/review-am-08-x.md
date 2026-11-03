# Review of batch am-08-x (additions: Latin America and the Caribbean from 1810)

Reviewer am-08-x, 2026-10-19. Machine copy: history/notes/phase-b/reviews/am-08-x.json. All 17 dossiers validate (with --resolve, no warnings). Spot checks were made with WebFetch on the cited pages; quotes below are what the pages say.

Verdict key: pass = could not break it; fix = accepted, with the fixes marked applied done by the reviewer and the others (applied: no) for the author; thin = honest but gaps a gap-filler should fill; fail = back to the author.

| dossier | verdict | applied by reviewer | for the author |
| --- | --- | --- | --- |
| mapuche | fix | 2 | 1 |
| kingdom-of-haiti | thin | 0 | 0 |
| republic-of-yucatan | fix | 1 | 1 |
| chan-santa-cruz | fix | 2 | 0 |
| third-republic-of-venezuela | thin | 0 | 0 |
| free-province-of-guayaquil | fix | 1 | 0 |
| cabanagem-rebels | fail | 0 | 2 |
| confederation-of-the-equator | pass | 0 | 0 |
| republic-of-spanish-haiti | pass | 0 | 0 |
| british-guiana | fix | 0 | 1 |
| british-honduras | fix | 0 | 2 |
| colony-of-jamaica | fix | 0 | 3 |
| west-indies-federation | fix | 1 | 2 |
| juliana-republic | pass | 0 | 0 |
| republic-of-cuba-in-arms-ten-years-war | pass | 0 | 0 |
| captaincy-general-of-cuba | fail | 0 | 3 |
| falkland-islands | fix | 1 | 0 |

## mapuche: fix

- **/ledger/8** (applied by reviewer): The 1881 loss of Neuquén was at confidence 1 with a note saying the page is silent on the land taken; the page names it. Evidence: Conquest_of_the_Desert: 'ordered a campaign during 1881 commanded by Colonel Conrado Villegas' ... 'Within a year Villegas conquered the Neuquén Province (he reached the Limay River).' Fix: Confidence raised to 3, region text and note rewritten with the page's sentence (tagged 'Reviewer am-08-x').
- **/keyframe_review/2/correction** (applied by reviewer): Chubut appears in the 1879 keyframe (and stays to 1884) but is absent from the 1810 and 1862 keyframes, and no event gains it: an unexplained extent change. Evidence: Conquest_of_the_Desert: the last group 'surrendered two months later in present Chubut Province' (after 18 October 1884), so Chubut was free Mapuche/Patagonian land throughout; the 1879-1884 keyframes and the 1884 loss already include it. Fix: Added {admin1: Chubut, country: Argentina} to the Argentine union of /keyframe_review/0 and /1, of the found region /ledger/0 and of the dissolve region /ledger/16; sentence added to /keyframe_review/0/note.
- **/ledger/16/counterpart** (for the author): The dissolve names republic-of-chile, but the last free land (Río Negro and Chubut, /ledger/15) passes to argentine-confederation in December 1884. Evidence: Conquest_of_the_Desert: last battle 18 October 1884, surrender 'two months later in present Chubut Province'; Occupation_of_Araucanía: Chile's side ends with 'Today the whole Araucanía is subjugated' (1 June 1883). Fix: Optional: set the dissolve counterpart to argentine-confederation, or keep Chile and say why in the note.
- Gap /ledger/0: The 1810 extent (Biobío frontier, Puelmapu provinces) rests on no page (confidence 1). Try: https://es.wikipedia.org/wiki/Ocupación_de_la_Araucanía
- Gap /keyframe_review/0: Puelmapu as La Pampa, Neuquén, Río Negro and Chubut is the researcher's reading; the Ranquel and Tehuelche lands are not separated. Try: https://es.wikipedia.org/wiki/Conquista_del_Desierto
- Spot checks: /ledger/2 confirmed; /ledger/10 confirmed; /ledger/11 confirmed; /ledger/12 confirmed; /ledger/13 confirmed; /ledger/7 confirmed; /ledger/8 confirmed and stronger than the note; /ledger/15 confirmed.
- Area: No area on the Mapuche or Occupation pages; the keyframe notes say so.

## kingdom-of-haiti: thin

- Gap /ledger/1: The 1807 contest zone (Artibonite) is confidence 1: no page opened says where the north-south front ran. Try: https://fr.wikipedia.org/wiki/Royaume_d'Haïti
- Gap /keyframe_review/0: The four northern departments are the researcher's reading; the State and Kingdom pages say only 'northern Haiti'. Try: https://fr.wikipedia.org/wiki/Henri_Christophe
- Spot checks: /ledger/0 confirmed; /ledger/3 confirmed; /ledger/2 confirmed; /ledger/4 confirmed.
- Area: No infobox area on State_of_Haiti; the keyframe note says the pages give none.

## republic-of-yucatan: fix

- **/keyframe_review/0/correction** (applied by reviewer): The 1840 keyframe and the found region held Yucatán state only, yet Quintana Roo appears in the 1841 keyframe with no event; centralist-mexico's June 1840 loss is of Yucatán, Campeche and Quintana Roo. Evidence: Republic_of_Yucatán: 'The area of the former republic includes the modern Mexican states of Yucatán, Campeche and Quintana Roo.' centralist-mexico /ledger/3 (1840-06 loss) region is the union of the three states. Fix: Added {admin1: Quintana Roo, country: Mexico} to /keyframe_review/0/correction and /ledger/0/region (Quintana Roo was then the east of the state of Yucatán); sentence added to the keyframe note.
- **/ledger/9/region** (for the author): The August 1848 merge hands over Yucatán and Campeche whole, while the 1848 keyframe holds only the Mérida and Campeche rings and the rest is the Maya contest zone. Evidence: Caste_War_of_Yucatán: 'By the spring of 1848, the Maya forces had taken over most of the Yucatán' 'except the walled cities of Campeche and Mérida and the southwest coast'. Fix: Optional: make the merge region the 1848 keyframe (the two rings) so the merge and the shape agree.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/4 confirmed; /ledger/5 confirmed; /ledger/6 confirmed; /ledger/7 confirmed; /ledger/10 confirmed.
- Area: No area on the page; keyframe note says so.

## chan-santa-cruz: fix

- **/ledger/0/counterpart** (applied by reviewer): The 1849 found event names republic-of-yucatan, which had ended in August 1848 (its dossier's end and dissolve). Evidence: Caste_War_of_Yucatán: 'Yucatán was officially reunited with Mexico on 17 August 1848.' republic-of-yucatan /identity/end 1848-08. Fix: Counterpart set to federated-republic-of-mexico (as the 1860 gain already does); note tagged 'Reviewer am-08-x'.
- **/ledger/0/region** (applied by reviewer): The found region was all of Quintana Roo while the first keyframe (1849-1859) is a 120 km ring round Felipe Carrillo Puerto. Evidence: Chan_Santa_Cruz gives no extent before 'the 1860s through the 1890s'; the keyframe note calls the ring the minimal reading. Fix: Found region set to the keyframe's ring {place: Felipe Carrillo Puerto, km: 120, country: Mexico}, text kept.
- Gap /keyframe_review/0: The 1849-1859 extent is a 120 km placeholder ring; no page dates the state's growth to its 1860s extent. Try: https://es.wikipedia.org/wiki/Chan_Santa_Cruz
- Gap /keyframe_review/1: The frontier with British Honduras (Hondo river, 1893 Spenser-Mariscal treaty) is not on the pages opened. Try: https://es.wikipedia.org/wiki/Tratado_Spenser-Mariscal
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed.
- Area: No area on the page; keyframe note says so (Quintana Roo 44,705 km2 quoted for scale).

## third-republic-of-venezuela: thin

- Gap /ledger/1: Margarita Island is gained only in February 1819 (confidence 1); the pages show it was patriot-held before ('Bolívar returned to Margarita Island, a secure republican redoubt', Venezuelan War of Independence) but do not date it, so it probably belongs in the 1817 keyframe. Try: https://es.wikipedia.org/wiki/Batalla_de_Matasiete
- Gap /keyframe_review/0: Bolívar state alone is the 1817-1818 extent; captaincy-general-of-venezuela's 1817 loss also gives up part of the Llanos, which this dossier never holds. Try: https://es.wikipedia.org/wiki/Campaña_de_Guayana
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed as far as it goes; /ledger/2 confirmed; /ledger/3 confirmed.
- Area: No infobox area; keyframe note says the page gives no territory.

## free-province-of-guayaquil: fix

- **/ledger/1** (applied by reviewer): The 1820 gain of the coastal provinces (no month) was listed before the found event of October 1820, i.e. the state gained land before it existed. Evidence: Free_Province_of_Guayaquil: 'After the independence revolution in Guayaquil on October 9, 1820, several municipalities immediately joined'. Fix: Gain given month 10 and moved after the found event (now /ledger/0 found, /ledger/1 gain); note tagged 'Reviewer am-08-x'.
- Gap /keyframe_review/0: Tumbes (now Peru) is in the page's list of provinces but not drawn; Esmeraldas and Los Ríos are drawn whole where the page says 'southern Esmeraldas' and 'most of Los Ríos'. Try: https://en.wikipedia.org/wiki/Free_Province_of_Guayaquil
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /wars/0 confirmed.
- Area: Infobox 53,000 km2 (no year; population given for 1822); keyframe note quotes it and the gazetteer area of the drawn union.

## cabanagem-rebels: fail

- **/ledger/1** (for the author): Confidence-3 event whose note says the rebel government 'yielded the government to imperial control, in the person of marshall Manuel Jorge Rodrigues in July 1835'; the page says the opposite: the handover did not happen. Evidence: Cabanagem: Vinagre 'would have yielded the government to imperial control, in the person of marshall Manuel Jorge Rodrigues' in July 1835 'If it were not for the intervention of his brother Antônio'; the rebels lost Belém later when, weakened by imperial forces and a naval squadron, 'the rebel forces were destroyed and retired toward the interior', before 'they again attacked Belém on August 14'. Fix: Rewrite the note with the page's sentences ('the rebel forces were destroyed and retired toward the interior'), drop the claim of a handover to Rodrigues, date the loss to July-August 1835 without a day (keep month 7 or 8 and say it is the page's sequence), and lower the confidence to 2.
- **/keyframe_review/1** (for the author): The 60-300 km ring round Belém appears in April 1836 with no gain event: the page names no interior place, so the extent is unexplained. Evidence: Cabanagem: the rebels 'decided to abandon the capital in favor of resistance from the interior' and 'continued to resist from the interior of the province' without naming any place. Fix: Either end the rebel shape at the April 1836 loss of Belém and leave the interior to empire-of-brazil's contest (1835-1840), or add a 1836-04 gain of the ring at confidence 1 with the page's words and list it as a gap.
- Gap /keyframe_review/1: Interior strongholds after 1836 (Santarém, Cametá, Vigia, Rio Negro) are not on the English page. Try: https://pt.wikipedia.org/wiki/Cabanagem
- Spot checks: /ledger/0 confirmed; /ledger/1 not on page; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed.
- Area: No area on the page; keyframe notes say so.

## confederation-of-the-equator: pass

- Gap /keyframe_review/0: Adherent villages in southern Ceará and Paraíba are not drawn (no page dates them); the page also says Pernambuco's rural population largely stayed loyal, so the whole province is an upper bound. Try: https://en.wikipedia.org/wiki/Confederation_of_the_Equator
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /keyframe_review/0 confirmed.
- Area: No area on the page; keyframe note says so.

## republic-of-spanish-haiti: pass

- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/3 confirmed; /ledger/4 confirmed; /ledger/5 confirmed.
- Area: Infobox 54,442 km2; keyframe note gives the gazetteer area of the drawn country and the ratio.

## british-guiana: fix

- **/ledger/3** (for the author): The 1899 'gain' from venezuela of four Guyanese regions records land the colony already holds in the 1814 keyframe, and venezuela's own dossier records the opposite transfer that year. Evidence: Guayana_Esequiba: 'On 3 October 1899 the Tribunal ruled largely in favour of Britain'; Venezuela received 'Barima Point at the mouth of the Orinoco'; British_Guiana: 'The tribunal awarded about 94% of the disputed territory to British Guiana.' venezuela /ledger/5: 1899-10 gain (the Orinoco mouth) with counterpart british-colonial-empire. Fix: Delete the gain (the contest_end of the same month carries the award) and add a 1899-10 loss to venezuela of Barima Point (a lon/lat/km point region, since Barima Point is not in the gazetteer, coordinates from a page), confidence 2, so it mirrors venezuela /ledger/5.
- Gap /keyframe_review/0: The Brazilian frontier (Pirara, 1904 award) and the New River Triangle are not on the pages opened. Try: https://en.wikipedia.org/wiki/Brazil–Guyana_border
- Gap /keyframe_review/0: The pre-1899 shape is modern Guyana; whether the colony administered land west of the Schomburgk line before the award is not on the pages. Try: https://en.wikipedia.org/wiki/Schomburgk_Line
- Spot checks: /ledger/0 confirmed (year); /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 date confirmed (3 October 1899), type wrong; /ledger/5 confirmed.
- Area: Infobox '1924: 231,800 km2'; the keyframe note compares it with the gazetteer's 208,600 km2 for modern Guyana.

## british-honduras: fix

- **/ledger/2** (for the author): The land from the Sibun to the Sarstoon (Stann Creek, Toledo, Cayo) enters the shape only in 1859, but the page puts the settlers there in the 1820s; 1859 is the treaty recognition. Evidence: Belizean–Guatemalan_territorial_dispute: 'the Baymen had expanded as far south as the Sarstoon River' in 'the 1820s'; 'In the Wyke–Aycinena Treaty of 1859, Guatemala agreed to recognize Britain's sovereignty over the area.' Fix: Add a gain of Stann Creek and Toledo (and Cayo if a page supports it) at about 1825, confidence 1-2, counterpart united-provinces-of-central-america (1824-1839), split /keyframe_review/1 at that year, and keep 1859 as a treaty note rather than a land gain (or keep it as the gain of whatever the 1820s settlement did not reach).
- **/ledger** (for the author): No vassal events for the dependency on Jamaica, which the page states and the colony-of-jamaica dossier (same batch) records. Evidence: British_Honduras: 'From 1749 until 1884, British Honduras was governed as a dependency of the British colony of Jamaica'; infobox 'No longer governed by Colony of Jamaica: 31 October 1884'. colony-of-jamaica /ledger/3 (vassal_start 1749) and /ledger/8 (vassal_end 1884-10). Fix: Add vassal_start 1783-11 (counterpart colony-of-jamaica; the 1749 date in the note) and vassal_end 1884-10 (counterpart colony-of-jamaica), confidence 3, source British_Honduras.
- Gap /keyframe_review/2: The Mexican frontier on the Hondo (1893 treaty) and the western line are not on the pages opened. Try: https://en.wikipedia.org/wiki/History_of_Belize
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 mis-dated; /ledger/3 confirmed; /ledger/5 confirmed; /ledger/6 confirmed.
- Area: No infobox area; keyframe note gives the gazetteer area of modern Belize.

## colony-of-jamaica: fix

- **/ledger/3** (for the author): vassal_start of british-honduras in 1749, but the british-honduras dossier starts in 1783 (the counterpart does not exist yet) and has no mirror vassal event. Evidence: Colony_of_Jamaica infobox: attachment of British Honduras '1749' (by order of the listed names); British_Honduras: 'From 1749 until 1884 ... a dependency of the British colony of Jamaica'; british-honduras /identity/start 1783-11. Fix: Move the vassal_start to 1783-11 (the dependency's dossier start) and keep 1749 in the note; the british-honduras author adds the mirror pair (see that dossier). The 2 October 1884 detachment (/ledger/8) differs from British_Honduras's '31 October 1884': say so in the note.
- **/ledger/1** (for the author): The 1670 'gain' from spanish-empire moves no land (the island is held since 1655, as the note says) and spanish-empire records the transfer as its 1655 loss. Evidence: Colony_of_Jamaica: 'England gained formal possession of Jamaica from Spain in 1670 through the Treaty of Madrid'; spanish-empire /ledger/32: 1655 loss of Jamaica (counterpart english-colonial-empire). Fix: Drop the event and put the Treaty of Madrid in the found event's note or in certainty (soft 1655-1670, sharp after), so no gain without a mirror remains.
- **/ledger** (for the author): No event for Jamaica's membership of the West Indies Federation (1958-1962), so two dossiers (this colony and west-indies-federation, type state) hold Jamaica in 1958-1962 with no relation between them. Evidence: West_Indies_Federation: 'Established: 3 January 1958', 'Disestablished: 31 May 1962'; west-indies-federation lists colony-of-jamaica both as predecessor and as successor. Fix: Record the relation the project uses for federations of colonies (e.g. vassal_start 1958-01 / vassal_end 1962-05 with counterpart west-indies-federation), agreed with the west-indies-federation dossier.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed by infobox order; /ledger/9 confirmed by infobox order; /ledger/6 confirmed; /ledger/11 confirmed.
- Area: No infobox area; keyframe note gives the gazetteer area of Jamaica.

## west-indies-federation: fix

- **/ledger/0/note** (applied by reviewer): The note quoted 'The West Indies Federation consisting of Jamaica and nine other colonies was formed in 1958', which is not on the cited page. Evidence: West_Indies_Federation: 'The federation was created by the United Kingdom in 1958 from most of the British West Indies'; 'made up of ten provinces, all British colonial possessions'. Fix: Quote replaced with the page's sentences (tagged 'Reviewer am-08-x'); date and confidence unchanged.
- **/keyframe_review/0** (for the author): The Cayman Islands and the Turks and Caicos Islands are excluded as 'not members', but the page's provinces table lists both. Evidence: West_Indies_Federation provinces table: 'Cayman Islands (attached to Jamaica)', 'Turks and Caicos Islands (attached to Jamaica)'; they 'had been separated from Jamaica upon the latter's independence in 1962'. Fix: Add {country: Cayman Islands} and {country: Turks and Caicos Islands} to the keyframe, found and dissolve regions (the gazetteer resolves both: colony-of-jamaica uses them), and correct the predecessor note.
- **/identity/predecessors/0** (for the author): colony-of-jamaica is both predecessor and successor while that colony lives on through 1958-1962: the overlap has no relation event in either dossier. Evidence: colony-of-jamaica runs 1655-1962 with no 1958 event; this dossier's found event names british-colonial-empire. Fix: Agree one relation with colony-of-jamaica (see that dossier's fix) and keep the predecessor/successor entries only if land actually changes hands.
- Spot checks: /ledger/0 confirmed (date); /ledger/1 confirmed; /identity/capitals/0 confirmed; /keyframe_review/0 area confirmed.
- Area: Provinces-table total 20,239 km2 quoted in the keyframe note with the gazetteer area.

## juliana-republic: pass

- Gap /keyframe_review/0: The 50 km ring round Laguna is a placeholder; the page names only Laguna and the failed attack on Desterro. Try: https://pt.wikipedia.org/wiki/República_Juliana
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /identity/capitals/0 confirmed.
- Area: No area on the page; keyframe note says so.

## republic-of-cuba-in-arms-ten-years-war: pass

- Gap /keyframe_review/1: Rebel-held ground after Bayamo is not named; Oriente and Camagüey in modern provinces are an upper bound. Try: https://es.wikipedia.org/wiki/Guerra_de_los_Diez_Años
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed; /ledger/6 confirmed.
- Area: No area on either page; keyframe note says so.

## captaincy-general-of-cuba: fail

- **/ledger** (for the author): Missing event on the dossier's own main page: the British capture of Havana and occupation of western Cuba (1762-1763); the notes say the pages give no event between 1607 and 1868 except the 1764 restructuring. Evidence: Captaincy_General_of_Cuba: 'The British captured Havana after a three-month siege and controlled the western part of the island for a year', Cuba returned in the Treaty of Paris (1763). Fix: Add occupation_start 1762 and occupation_end 1763 (counterpart kingdom-of-great-britain, slug of polities.csv 1709-2024), region the western provinces round Havana (e.g. La Habana, Artemisa, Mayabeque or a Havana ring), confidence 2, source the Captaincy page; correct the sentence in notes.
- **/ledger/1/region** (for the author): The Ten Years' War contest zone is Oriente only, while the rebel dossier of this batch gains Camagüey and Ciego de Ávila in November 1868 and contests Las Villas from February 1869. Evidence: Ten_Years%27_War: Camagüey 'rose up in arms during the Las Clavellinas Uprising' (4 November 1868); 'in early February 1869, Las Villas followed'. republic-of-cuba-in-arms-ten-years-war /ledger/2 and /ledger/4. Fix: Extend the contest zone to Camagüey and Ciego de Ávila (from 1868-11) and add a contest for Sancti Spíritus, Villa Clara and Cienfuegos 1869-02 to 1878-02, so the government's contest matches the rebels' land.
- **/ledger/6** (for the author): The December 1898 'loss' to united-states-of-america does not match that dossier, which records an occupation of Cuba from 17 July 1898 (counterpart spanish-empire) and then an occupation (counterpart republic-of-cuba). Evidence: united-states-of-america /ledger/74 (1898-07 occupation_start, Cuba) and /ledger/82 (1898-12 occupation_start); Captaincy_General_of_Cuba: the War of Independence 'became the Spanish–American War' and 'the United States took control of the island'. Fix: Add occupation_start 1898-07 (counterpart united-states-of-america, Santiago ring or Oriente) before the December loss, or explain in the note why the colony's end is a loss and not an occupation.
- Gap /ledger/4: The 1897 autonomy and the 1898 US landing are dated only by year; no page opened gives the July 1898 landing. Try: https://en.wikipedia.org/wiki/Spanish–American_War
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/4 confirmed; /ledger/6 confirmed (date).
- Area: No area on the page; keyframe note gives the gazetteer area of Cuba.

## falkland-islands: fix

- **/wars/0/belligerents/2** (applied by reviewer): Mis-typed slug 'kingdom-of-the-united-kingdom': no such dossier or polities.csv row (the note itself said it was not a checked slug). Evidence: polities.csv: kingdom-of-great-britain, 'Kingdom of Great Britain', 1709-2024 (the United Kingdom); no 'kingdom-of-the-united-kingdom' row. Fix: Set to kingdom-of-great-britain and rewrote the sentence in the war note (tagged 'Reviewer am-08-x').
- Gap /ledger/4: South Georgia (a dependency in 1982) was also occupied by Argentina in April 1982 (argentine-republic /ledger/3 includes 'S. Geo. and the Is.'); the Falkland page says only 'the Falklands and other British territories in the South Atlantic'. Try: https://en.wikipedia.org/wiki/Invasion_of_South_Georgia
- Gap /ledger/3: The Antarctic parts of the Dependencies (Graham Land, South Orkneys, South Shetlands, 1908-1962) are not drawn. Try: https://en.wikipedia.org/wiki/Falkland_Islands_Dependencies
- Spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/4 confirmed; /ledger/5 confirmed; /ledger/6 confirmed; /ledger/3 confirmed.
- Area: Infobox 12,173 km2; keyframe note gives the gazetteer area and ratio.

## Cross-dossier matrix (mismatches and missing mirrors)

- mapuche 1862 loss -> republic-of-chile: mismatch (mirror: republic-of-chile 1862 gain). Land (Angol ring) and year agree; Chile's gains of 1861-12 and 1862 name counterpart 'nobody': re-point to mapuche (am-08 Chile author).
- mapuche 1881 loss -> republic-of-chile: missing (mirror: none). No 1881 Araucanía gain in republic-of-chile (Temuco, Victoria, the Malleco-Cautín country).
- mapuche 1882 loss -> republic-of-chile: missing (mirror: none). No 1882 gain (Lonquimay forts) in republic-of-chile; small.
- mapuche 1883 loss -> republic-of-chile: mismatch (mirror: republic-of-chile 1883 gain). Chile's 1883-06 gain of Araucania names 'nobody'; re-point to mapuche.
- mapuche 1879 loss -> argentine-confederation: mismatch (mirror: argentine-confederation 1879 gain). Year and land agree; argentine-confederation names 'nobody' (am-08-d): re-point to mapuche.
- mapuche 1881 loss -> argentine-confederation: mismatch (mirror: argentine-confederation 1881 gain). Neuquén; argentine-confederation names 'nobody'.
- mapuche 1884 loss -> argentine-confederation: mismatch (mirror: argentine-confederation 1884 gain). Río Negro and Chubut; argentine-confederation (1884-10) names 'nobody'.
- kingdom-of-haiti 1807 contest_start -> haiti: missing (mirror: none). haiti has no 1807-1810 contest with kingdom-of-haiti (not territorial; low priority).
- republic-of-yucatan 1848 merge -> federated-republic-of-mexico: missing (mirror: none). federated-republic-of-mexico has no 1848 Yucatán event; its 1846-08 gain of Cliopatria's Centralist Mexico 1845 shape may also include the peninsula, overlapping the republic in 1846-1848 (am-08-e).
- chan-santa-cruz 1849 found -> federated-republic-of-mexico: missing (mirror: none). Counterpart corrected by the reviewer from republic-of-yucatan; federated-republic-of-mexico has no 1849 event.
- chan-santa-cruz 1860 gain -> federated-republic-of-mexico: missing (mirror: none). No 1860 loss in federated-republic-of-mexico (am-08-e).
- chan-santa-cruz 1901 loss -> mexico: missing (mirror: none). mexico (1867-2024) has no 1900-1902 gain of Quintana Roo.
- third-republic-of-venezuela 1817 found -> captaincy-general-of-venezuela: mismatch (mirror: captaincy-general-of-venezuela 1817 loss). The captaincy's 1817 loss names republic-of-venezuela (Cliopatria row 1811-1814) and includes part of the Llanos, which this dossier never holds: re-point to third-republic-of-venezuela and agree the land (am-08-a).
- third-republic-of-venezuela 1819 gain -> captaincy-general-of-venezuela: missing (mirror: none). No 1819 loss of Margarita in the captaincy; the gain itself is probably mis-dated (thin).
- third-republic-of-venezuela 1819 merge -> gran-colombia: mismatch (mirror: gran-colombia 1819 found). gran-colombia's 1819-12 found names new-granada only; add third-republic-of-venezuela (am-08-c).
- free-province-of-guayaquil 1820 gain -> spanish-empire: missing (mirror: none). spanish-empire loses Ecuador only in 1822-05 (to gran-colombia); no 1820 loss of the Guayaquil coast (am-06).
- free-province-of-guayaquil 1822 merge -> gran-colombia: mismatch (mirror: gran-colombia 1822 gain). gran-colombia's 1822 gain of Ecuador names spanish-empire; Guayaquil's provinces should name free-province-of-guayaquil (am-08-c).
- republic-of-spanish-haiti 1821 found -> spanish-empire: mismatch (mirror: spanish-empire 1821 loss). spanish-empire's 1821-12 loss of the Dominican Republic names 'nobody': re-point to republic-of-spanish-haiti (am-06).
- british-guiana 1814 found -> essequibo: mismatch (mirror: essequibo 1814 dissolve). essequibo and berbice dissolve with counterpart british-colonial-empire; re-point to british-guiana (am-06-c).
- british-guiana 1899 gain -> venezuela: mismatch (mirror: venezuela 1899 gain). Opposite directions: venezuela gains the Orinoco mouth from british-colonial-empire; british-guiana should record a loss of Barima Point (fix listed).
- british-honduras 1783 found -> spanish-empire: missing (mirror: none). spanish-empire has no 1783 Belize event (am-06).
- british-honduras 1786 gain -> spanish-empire: missing (mirror: none). No 1786 loss in spanish-empire (am-06).
- british-honduras 1859 gain -> guatemala: missing (mirror: none). guatemala has no 1858-1860 event; the land move is the 1820s (fix listed).
- colony-of-jamaica 1655 found -> spanish-empire: mismatch (mirror: spanish-empire 1655 loss). spanish-empire's loss names english-colonial-empire; acceptable for a colony drawn in the metropole's tint, or re-point to colony-of-jamaica (am-06).
- colony-of-jamaica 1670 gain -> spanish-empire: missing (mirror: none). No land change; drop (fix listed).
- colony-of-jamaica 1749 vassal_start -> british-honduras: mismatch (mirror: none). british-honduras starts in 1783 and has no vassal events (fixes listed on both).
- colony-of-jamaica 1884 vassal_end -> british-honduras: missing (mirror: none). british-honduras page gives 31 October 1884.
- captaincy-general-of-cuba 1898 loss -> united-states-of-america: mismatch (mirror: united-states-of-america 1898 occupation_start). The US records occupation from 1898-07 (counterpart spanish-empire) and from 1898-12 (counterpart republic-of-cuba), not a gain (fix listed).

## Other

- No page failed to load. The validator (with --resolve) gave no errors or warnings for any of the 17 dossiers before or after the reviewer's edits.
- Reviewer edits applied in place and re-validated (each tagged 'Reviewer am-08-x' in the touched note): mapuche (/ledger/8 confidence 1->3; Chubut added to /keyframe_review/0,/1 and /ledger/0,/16), republic-of-yucatan (Quintana Roo added to /keyframe_review/0 and /ledger/0), chan-santa-cruz (/ledger/0 counterpart and region), free-province-of-guayaquil (gain month 10, moved after found), falkland-islands (/wars/0 belligerent slug), west-indies-federation (/ledger/0 misattributed quote). Pre-edit copies are in /tmp/claude-0/work/review-am-08-x/backup/.
- Counterpart dossiers of other groups name 'nobody' or name strings where this batch's new slugs now exist: republic-of-chile and argentine-confederation (mapuche), empire-of-brazil ('Cabanagem rebels', 'Confederation of the Equator', riograndense-republic for Juliana), captaincy-general-of-venezuela (republic-of-venezuela), gran-colombia (new-granada, spanish-empire), spanish-empire (nobody for Santo Domingo; no events for Belize 1783/1786 or Guayaquil 1820), essequibo and berbice (british-colonial-empire), federated-republic-of-mexico and mexico (no Yucatán or Chan Santa Cruz events), guatemala (no 1859 event). Route to am-08-a/b/c/d/e, am-06 and am-06-c.
- Owners not yet run (exception, not mismatch): kingdom-of-spain (eu-12), british-colonial-empire and kingdom-of-great-britain (eu-11); belize and guyana (am-08 Cliopatria rows, no dossier file yet).
- west-indies-federation (type state) and colony-of-jamaica overlap on Jamaica 1958-1962 with no relation event; the orchestrator may prefer one project-wide convention for federations of colonies.
