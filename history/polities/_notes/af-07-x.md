# af-07-x: Southern Africa (additions batch): notes for the reviewer and the gap-fillers

Written 2026-10-19. Fifty distinct English Wikipedia pages were loaded through WebFetch (a summarising relay: quotes in the dossiers are the sentences the relay presented in quotation marks, everything else is paraphrase); 45 of them are cited in the dossiers' source lists, five loaded but were too thin to cite (Transkei, Bamangwato, Ngwaketse, Venda people, Ovambo people). Twelve titles failed with URL_NOT_FOUND (listed below). wikidata.org, archive.org and github.com were not used. Cliopatria has no row for any of these states, so every dossier has cliopatria_names [], every keyframe is new (shape_id <slug>_<from>, verdict adjust) and every state is a new slug. 27 dossiers, 177 ledger events, all validate with 0 errors; the warnings left are unresolved gazetteer names and counterpart slugs of states with no dossier yet (listed below).

## Dossiers written (slug, years, events)

- kingdom-of-mapungubwe: Kingdom of Mapungubwe, 1220-1300, 4 events, 1 sources
- kingdom-of-zimbabwe: Kingdom of Zimbabwe, 1250-1450, 3 events, 1 sources
- kingdom-of-butua: Kingdom of Butua, 1425-1683, 4 events, 1 sources
- mutapa-empire: Mutapa Empire, 1430-1885, 16 events, 1 sources
- rozvi-empire: Rozvi Empire, 1683-1838, 8 events, 3 sources
- ndebele-kingdom: Ndebele Kingdom, 1823-1894, 13 events, 5 sources
- gaza-empire: Gaza Empire, 1824-1895, 5 events, 2 sources
- basutoland: Basutoland, 1822-1966, 14 events, 3 sources
- portuguese-mozambique: Portuguese Mozambique, 1505-1975, 21 events, 8 sources
- betsimisaraka-kingdom: Betsimisaraka Kingdom, 1710-1817, 5 events, 1 sources
- boina-kingdom: Boina Kingdom, 1690-1840, 4 events, 2 sources
- menabe-kingdom: Menabe Kingdom, 1540-1900, 12 events, 3 sources
- transvaal-colony: Transvaal Colony, 1902-1910, 3 events, 2 sources
- orange-river-colony: Orange River Colony, 1902-1910, 2 events, 1 sources
- pedi-empire: Pedi Empire, 1780-1882, 7 events, 1 sources
- mpondo-kingdom: Mpondo Kingdom, 1820-1894, 4 events, 1 sources
- griqualand-east: Griqualand East, 1862-1877, 4 events, 1 sources
- griqualand-west: Griqualand West, 1800-1880, 6 events, 1 sources
- british-kaffraria: British Kaffraria, 1860-1866, 3 events, 1 sources
- stellaland: Stellaland, 1882-1885, 4 events, 1 sources
- british-bechuanaland: British Bechuanaland, 1885-1895, 3 events, 1 sources
- mtetwa-paramountcy: Mtetwa Paramountcy, 1780-1817, 3 events, 2 sources
- ndwandwe-kingdom: Ndwandwe Kingdom, 1780-1820, 3 events, 1 sources
- swazi-kingdom: Swazi Kingdom, 1744-1885, 6 events, 2 sources
- lozi-kingdom: Lozi Kingdom, 1650-1911, 8 events, 3 sources
- makololo-kingdom: Makololo Kingdom, 1840-1864, 3 events, 3 sources
- xhosa-kingdom: Xhosa Kingdom, 1779-1878, 9 events, 2 sources

## Judgement calls the reviewer may want to overrule

- Start and end years that are bridges, not page dates: kingdom-of-zimbabwe ends 1450 (the page gives no end; the Butua dossier starts the Torwa state 1425); mutapa-empire 1430/1450/1470 (Mutapa expansion bridges), ends 1885 (Chidima annexed; the infobox says 'conquered by the Portuguese: 1884'); rozvi-empire ends 1838 (Ndebele conquest; the infobox says 1866); lozi-kingdom starts 1650 ('17th century'); swazi-kingdom starts 1744 ('after 1744'); xhosa-kingdom starts 1779 (the Fish River line), not the founding ('before the 15th century'); mpondo-kingdom starts 1820 (Faku, first dated act).
- Transvaal Colony and Orange River Colony start 31 May 1902 (Vereeniging), not 1900: the 1900-02 British occupation is already recorded as occupation events in the south-african-republic and free-orange-state dossiers (af-07-b). The af-07-b report suggested years 1900-1910 for both.
- The Union of South Africa (31 May 1910) is NOT written here: it belongs with af-08 `south-africa` (Cliopatria 1932+) because Cliopatria draws 1910-1931 inside British Africa. The transvaal-colony and orange-river-colony dossiers end 1910 with counterpart union-of-south-africa (a slug with no dossier).
- Stellaland and Goshen are one dossier (stellaland): Goshen merged into it in 1883 and held no land of its own the page dates.
- The 1881 Swazi loss (swazi-kingdom) draws the South African part of the ring as lost to south-african-republic and the Mozambican part (Nomahasha) lost at the same date as a confidence-1 bridge, so that the 1885 drawing matches the shape of af-07-b `swaziland`.
- Chartered companies are not dossiers: the Mozambique Company (1891-1942, Manica and Sofala) and the Niassa Company (1893-1929, Ruvuma to Lurio, over 160,000 km2) and the Zambezi prazos change no sovereignty; they are described in the portuguese-mozambique notes.
- Rulers are listed in pedi-empire and gaza-empire only (the pages carry king tables); the schema asks for a ruler strip only for documented lists, so the reviewer may drop them.

## Cross-batch mismatches (siblings written in parallel)

- merina-kingdom (af-07-a) uses the string counterparts 'Sakalava kingdom of Menabe' and 'Sakalava kingdom of Boina', 'Betsileo kingdoms', 'northern Tanala', 'rival Merina principalities'; this batch's slugs are menabe-kingdom and boina-kingdom (betsimisaraka-kingdom already matches). The Merina 1824 shape (Cliopatria) has Morondava inside, against the Menabe page's conquest dates 1834 and 1846 (menabe-kingdom dossier).
- british-cape-colony (af-07-b) uses the strings 'Xhosa chiefdoms', 'Mpondo kingdom', 'Griqualand West' and 'British Kaffraria' as counterparts instead of the slugs xhosa-kingdom, mpondo-kingdom, griqualand-west and british-kaffraria; it has no mirror of the Cape annexation of Griqualand East (1877, griqualand-east). The Cape dossier's 1835 annexation of Queen Adelaide Province carries a month (10 May 1835) that the Xhosa Wars extract read here did not show; xhosa-kingdom has the year only.
- free-orange-state (af-07-b) dates the end of the 1858 Basutoland contest to 15 October 1858; basutoland here uses 1 June 1858 (Free State-Basotho Wars page). Reviewer: pick one.
- zululand (af-07-b) names mtetwa-paramountcy as predecessor (extent unknown) and ndwandwe-kingdom as the 1820 counterpart: both slugs now exist. The Zulu 1816-1819 core overlaps the Mthethwa shape in 1816 (the last Mthethwa year) and the Ndwandwe box for 1818-1819.
- swaziland (af-07-b) starts 1885 with a 'found' event; swazi-kingdom ends 1885 with a dissolve (counterpart swaziland). south-african-republic (af-07-b) records the 1894-1899 vassal events with swaziland but not the 1881 Pretoria Convention loss of Swazi land.
- The mutapa-empire dossier ends 1885, while the Chioko rising (1897-1902) is entered only in portuguese-mozambique against the counterpart mutapa-empire.
- portuguese-mozambique (type colony, family portugal) may overlap the Portuguese shapes of eu-12 (kingdom-of-portugal, estado-novo, portuguese-republic) and the af-08 colonial group; the colour agent should seed it from the Portuguese family.
- The Union-era and BSAC counterparts british-south-africa-company (ndebele-kingdom, lozi-kingdom) has no dossier; british-africa is Cliopatria's.

## Capital points that are stand-ins (flagged APPROXIMATE in each capital's note)

Great Zimbabwe-era and Butua capitals use gazetteer points; Danamombe (rozvi-empire, 29.2/-19.9, the Danangombe page gives no coordinates); Gaza capitals (Chaimite: the page is a disambiguation without coordinates; Xai-Xai and Chimoio stand in); Kokstad, Griquatown and King William's Town coordinates are the researcher's own knowledge (griqualand-east, griqualand-west, british-kaffraria); Pedi (Polokwane), Mpondo (Port St. Johns), Mthethwa (Ulundi), Ndwandwe (Vryheid), Swazi (Hlatikulu for Shiselweni, Manzini for Zombodze), Lozi (Mongu for Lealui), Makololo (Sesheke for Linyanti), Xhosa (Bhisho). Boxes whose edges are the researcher's own reading of a river or place named by a page: the Mthethwa box (Umkhomazi to Hluhluwe), the Ndwandwe box (Pongola to Black Umfolozi), the Gcalekaland box (Great Kei to Mthatha) and the Pedi Thulare box.

## Pages that failed (URL_NOT_FOUND)

Betsimisaraka_Kingdom, Sakalava_Kingdom, Menabe_Kingdom, Kingdom_of_Menabe, French_conquest_of_Madagascar, Pedi_Empire, Xhosa_Kingdom, Mpondo_Kingdom, Ndwandwe_Kingdom, Land_Goshen, Republic_of_Goshen, Goshen_(Boer_republic). Alternative titles were used (Betsimisaraka people, Sakalava people, Menabe, Pedi people, Pondoland, Ndwandwe, Xhosa Wars and Xhosa people, Stellaland).

## Pages that loaded but were too thin to cite

Transkei (nothing on the 19th century), Bamangwato (no founding date, no rulers), Ngwaketse (Kanye 1853 only), Venda people (no Singo dynasty, no 1898 annexation), Ovambo people (no kingdoms). No dossier was written for the Tswana states (Ngwato, Ngwaketse, Kwena, Tawana), the Venda kingdom or the Ovambo kingdoms (Ondonga, Oukwanyama): every dated land fact would have been 'page silent'. Herero and Oorlam Namibia, Maravi and the Ngoni states of Malawi, Bemba and the short-lived Boer republics of Zoutpansberg, Lydenburg and Utrecht (a few years each, below the 10-year bar) were not attempted.

## Counterparts and successors that need dossiers

kingdom-of-barue, manyika-kingdom, dande, Teve (Kiteve) (mutapa-empire); british-south-africa-company (ndebele-kingdom, lozi-kingdom; and Southern Rhodesia); klipdrift-republic (1870, griqualand-west; under a year, probably not a dossier); union-of-south-africa (af-08); Bechuanaland Protectorate (af-08); Mankoroane's Tlhaping and Montshiwa's Rolong (stellaland); Venda and Nambya successors of the Rozvi; Nxaba's Ngoni kingdom; antankarana-kingdom (Madagascar); Voortrekkers.

## Gazetteer names needed

Regions: Sekhukhuneland (pedi-empire, swazi-kingdom), Pondoland and Xesibeland (mpondo-kingdom), Griqualand East, Griqualand West, British Kaffraria (british-kaffraria, xhosa-kingdom, and the af-07-b Cape dossier), British Bechuanaland, Conquered Territory (basutoland, and af-07-b free-orange-state), Kionga Triangle (portuguese-mozambique). Places: Sena (portuguese-mozambique), Danamombe, Chaimite, Mossurize, Bilene, Mandhlakazi, Kokstad, Thaba Bosiu, Foulpointe, King William's Town, Griquatown, Barberton, Zombodze, Linyanti, Lealui. Rivers: Black Umfolozi, Umkhomazi, Great Fish, Keiskamma. Descriptive names not in the gazetteer: Bulozi/Barotseland, Gcalekaland, Transkei, Ciskei, Zuurveld, Nomahasha.

## Notes, per dossier (the `notes` field of each file, verbatim)

### kingdom-of-mapungubwe (Kingdom of Mapungubwe, 1220-1300)

Cliopatria has no Mapungubwe. One page (the state's article) was opened under the 1-2 page budget for a state with no Cliopatria shapes. The page dates only the move to Mapungubwe Hill (c. 1220) and the abandonment (c. 1300); the earlier sacral kingship at Mapela Hill ('nearly 200 years earlier') and the K2/Schroda phases (from c. 900-1000) are not drawn as a state because the infobox starts the kingdom at c. 1220. Area: infobox and text give 30,000 km2 with no year (text attaches it to the 1250 population figure); the outline is a 98 km disc around the hill, not the page's frontier. The Venda rulers in the infobox (Shiriyadenga, Tshidziwelele) are 'according to some Venda traditions' and are not entered as a ruler strip. The successor link to kingdom-of-zimbabwe is political, not territorial: the basin was abandoned. Gazetteer: all names resolve (place Mapungubwe).

### kingdom-of-zimbabwe (Kingdom of Zimbabwe, 1250-1450)

Cliopatria has no Great Zimbabwe. Budget: one page (the state's article). Dates are the weakest of the batch: the page gives no founding year, no founder and no end year, only 'By 1250 ... an important trade centre', 'Around 1300 ... replaced Mapungubwe', decline 'from the early 15th century', and infobox bounds '13th century' and '16th/17th century'. The dossier runs 1250-1450: 1250 is the one year the page gives for the rise; 1450 is a bridging choice (confidence 1) that sits after the Butua founding (c. 1425, Butua page) and the first Mutapa activity. Area: 50,000 km2 (undated) drawn as a 126 km disc; the 7.22 km2 city figure is not territory. The Mutapa page says some Karanga from Great Zimbabwe migrated to the northern plateau in the 14th-15th centuries (Beach and Pikirayi) and Mutapa's founder is Nyatsimba Mutota only 'according to tradition'. Gazetteer: all names resolve (place Great Zimbabwe).

### kingdom-of-butua (Kingdom of Butua, 1425-1683)

Cliopatria has no Butua. Budget: one page (the state's article). Not settled: the date Khami became the capital; the 1450 Great Zimbabwe gain (page silent, confidence 1); the extent toward the Makgadikgadi Pan. Portuguese records of 1520 'state that Butua was a vassal of Mwenemutapa' (the Mutapa page also notes 4,000 cows gifted in 1493) but the same page has Butua warring on Mutapa until 1512, so no vassal event is entered. The 'Torwa dynasty' is one dynasty within the state; 'Rozvi' is a new state (rozvi-empire), not a rename, because the page says Changamire 'founded the Rozwi Empire' with its capital at Danamombe. No area is given by the page. Gazetteer: all names resolve (region Matabeleland, place Great Zimbabwe).

### mutapa-empire (Mutapa Empire, 1430-1885)

Cliopatria has no Mutapa. Budget: one article opened, with three further passes over the same cached page. The page gives no start year (infobox: 'Established: 15th century'; Beach and Pikirayi: 14th-15th century), so 1430 is a bridge at confidence 1 and Matope's and Mukombero's conquests are placed by bridge years (1450, 1470) at confidence 1. The end is 1885 (Chidima annexed, Dzuda in exile); the infobox says 'Conquered by the Portuguese: 1884' and the resistance of Chioko Dambamupute (1897-1902) falls after the end year and is recorded only as a war in the Portuguese Mozambique dossier (counterpart mutapa-empire). The 1890 British ultimatum 'led to the partition of Mutapa's former territories' between Britain and Portugal: the plateau side was Rozvi and then Ndebele ground by then, so no Mutapa loss to Britain is entered. Counterparts needing dossiers: kingdom-of-barue (Barue), manyika-kingdom (Manyika), and 'dande' (a principality of c. 1760), plus the Teve/Kiteve kingdom. The 1629 vassalage is entered from the Mutapa side as the loss of the Tete territory; the vassal tint itself belongs on the portuguese-mozambique ledger (vassal_start 1629 / vassal_end 1678, counterpart mutapa-empire). Capital coordinates are stand-ins (Mashonaland Central; Tete). Gazetteer: names resolve (region Mashonaland; admin1 Tete, Manica, Manicaland, Zambezia, Sofala; river Zambezi).

### rozvi-empire (Rozvi Empire, 1683-1838)

Cliopatria has no Rozvi. Budget: one article (the state's), one thin page for Danamombe (no coordinates, 17th-18th century dating only). The page's own span is c. 1683-1866 (infobox: 'Surrender of Tohwechipi: 1866'); the dossier ends in 1838, when the page says the state was 'conquered and subdued ... by Mzilikazi's Ndebele', because later the Rozvi hold only a remnant (the upper Save Valley by 1857) that the page does not outline. The Rozvi remnant (Tohwechipi, to 1866) is the only Rozvi presence after 1838. Successor states named in the infobox but not entered as land: the Venda Kingdom (Changamire dynasty migrated south in the late 17th century), the Nambya state (Sawanga migrated north to the Lower Gwai in the early 18th century), the Shangwe Confederacy. Counterpart names without dossiers: ngoni groups (Zwangendaba, Nyamazana, Nxaba), Mpanga's Sotho. The Mutapa vassalage (1712, from the Mutapa page; the Rozvi page has 1702 raids) is only 'influence and vassalage' per the page, not full control. The Danamombe point is approximate (see capital note). Region names: Zimbabwe Plateau is the gazetteer's country-of-Zimbabwe alias.

### ndebele-kingdom (Ndebele Kingdom, 1823-1894)

Cliopatria has no Ndebele kingdom. Budget: four pages for a no-shape state (Mthwakazi, Mzilikazi, First Matabele War, Northern Ndebele people) plus the Rozvi page for the 1838 conquest. The Mthwakazi page gives no founding year ('Established' empty), so 1823 is the Mzilikazi page's reign start and departure from Nguniland; the 1823-25 location is the researcher's (Mpumalanga, confidence 1). Not on any opened page, so not entered: Vegkop (1836), the Zulu attack of 1837, the dates of Inyati and Bulawayo as capitals, Lobengula's accession (the Mthwakazi page gives 'only in 1870 after a period of serious civil war'), tribute from Mashonaland, the Moffat treaty (February 1888) and Rudd Concession (October 1888) as a protectorate (the page says a 'treaty of friendship'), the 1896-97 rising (Northern Ndebele page: March 1896 to October 1897, 'the First War of Independence'), and the Griqua lands taken in 1831. The Northern Ndebele page says Mzilikazi 'reigned from 1823' and the Mzilikazi page gives death 9 September (infobox) or 5 September (body) 1868. Counterparts needing dossiers: british-south-africa-company (BSAC rule 1889-1923) and then Southern Rhodesia; Voortrekkers are only a name (the South African Republic dossier starts 1852). Gazetteer: names resolve (place Pretoria, Rustenburg; admin1 Mpumalanga, Midlands; region Matabeleland, Transvaal).

### gaza-empire (Gaza Empire, 1824-1895)

Cliopatria has no Gaza. Budget: Gaza Empire article (opened four times for different passes) and the Gungunhana page, with a disambiguation page for Chaimite that gave nothing. The infobox says 'Independent Kingdom (1824-1882), Portuguese protectorate (1882-1895)'; the protectorate is a Portuguese-side vassal_start 1882 / vassal_end 1895 (counterpart gaza-empire) and is NOT in this ledger, because the schema puts the vassal tint on the suzerain's dossier; the portuguese-mozambique dossier carries it. Not settled: the date of the Limpopo crossing; the 1830 subjugation year (page silent, confidence 1); the Zimbabwean part of Soshangane's realm (the page puts his capital 'in the highlands of the middle Sabi River' in present-day Zimbabwe, Today part of: 'Mozambique Zimbabwe South Africa'); the flight of Mzila's followers to the Soutpansberg ('to leave Mozambique and flee to the Soutpansberg Mountains in the Transvaal'); the 1884-85 and 1890-91 treaties (not on the pages). Capital coordinates are stand-ins. Counterpart names: Nxaba's Ngoni kingdom (a short-lived state inland from Sofala, 1830s). Gazetteer: names resolve (admin1 Gaza, Inhambane, Maputo, Sofala, Manica of Mozambique).

### basutoland (Basutoland, 1822-1966)

Cliopatria has no Basutoland: its Lesotho row (slug lesotho, written by af-08) begins in 1967; this dossier is the state before it, and the Cape Colony and Orange Free State dossiers (af-07-a and af-07-b) already cite it as counterpart 'basutoland'. Budget: Basutoland, Moshoeshoe I and Free State-Basotho Wars (three pages for a no-shape state; the Moshoeshoe page was thin on territory). Not on any page opened: the founding at Butha-Buthe, the move to Thaba Bosiu (1824), the Warden Line and Sovereignty (1848-49), the 1851 Viervoet and 1852 Berea battles beyond their dates, the 1869 treaty's name ('Convention of Aliwal North' per FSB), the Letsie rulers, the 1910 High Commission Territory status (mentioned, not dated to a boundary). The British protection of 1868-71 and the protectorate from 1884 to 1966 are British-side vassal events (counterpart basutoland, suzerain british-colonial-empire or british-cape-colony), which this ledger shows only as a rename (1868) and the Cape annexation (loss 1871, gain 1884). Region name 'Conquered Territory' is not yet in the gazetteer (the Free State dossier uses it too); the Free State is ordinary admin1. The Moshoeshoe page and the FSB page differ on the Treaty of Thaba Bosiu terms (arable land ceded vs no land specified): the ledger keeps the transfer at 1869. Sibling dossiers date the 1858 contest end to 15 October 1858 (their page); this ledger uses the 1 June armistice from the FSB page.

### portuguese-mozambique (Portuguese Mozambique, 1505-1975)

Cliopatria draws Mozambique only inside the Portuguese empire shapes (slug kingdom-of-portugal and the umbrella rel-portuguese-empire, other groups) and as 'Mozambique' from 1976; this dossier is the colony as its own state (type colony). Budget: seven pages (Portuguese Mozambique, Mutapa, Gaza, Gungunhana, the 1891 treaty, Mozambique Company, Niassa Company, Prazo); the prazo and company pages gave no territorial dates. Not entered as typed events because they change no sovereignty: the Mozambique Company (founded 11 February 1891, 'Manica and Sofala', 50-year concession, passed to the Portuguese authorities 18 July 1942), the Niassa Company (charter March 1893, Ruvuma to Lúrio, over 160,000 km2, extension refused 27 October 1929), the Zambezia prazos (no founding date on the Prazo page: 'known since the 16th century'; the Mutapa page: 1634 Tete prazos; in the 19th century 32 prazeiros owned 57 prazos in Tete Province). Not settled: when Portugal first held Sena and Quelimane (the Sena position is a gazetteer gap), the plateau feiras of the 1580s-1690s, the Manicaland claim (the 1891 treaty page: Manicaland 'passed from Portuguese to British control', undated before), the Rovuma boundary with German East Africa, the 1836-91 status name, the Pink Map (1885, 'Rose Coloured Map'). The Chioko rising is entered against 'mutapa-empire' although that dossier ends in 1885 (the infobox of the Mutapa page lists Chioko as 1890s-1902 ruler). Gazetteer names needed: place Sena (Mozambique, Zambezi), region Kionga Triangle (north bank of the Rovuma mouth, Cabo Delgado). The Kionga counterpart german-africa is a Cliopatria polity (af-08).

### betsimisaraka-kingdom (Betsimisaraka Kingdom, 1710-1817)

Cliopatria has no Betsimisaraka kingdom. The article 'Betsimisaraka Kingdom' did not load (URL_NOT_FOUND, tried https://en.wikipedia.org/wiki/Betsimisaraka_Kingdom); the 'Betsimisaraka people' article was used instead and is thin on territory: no frontier, no area, no end date for the kingdom (it mentions the 1817 colonisation and an 1825 rebellion). The af-07-a Merina dossier enters the Toamasina gain of 1817 against this slug; this ledger adds the rest of the coast at confidence 2. Not settled: Ratsimilaho's election year and reign length, the 'fractured' state after his death, the French at Ile Sainte-Marie (no dates), the Anglo-Merina treaty (1817) role. Gazetteer: names resolve (admin1 Analanjirofo, Atsinanana, place Toamasina).

### boina-kingdom (Boina Kingdom, 1690-1840)

Cliopatria has no Boina. Two pages: Boina Kingdom (thin: founding c. 1690, Boina Bay, tributary 1820-1832, annexed 1840) and Sakalava people (Mahajanga 1824, division of the Sakalava kingdom). They disagree about the annexation (infobox 1840 against 'never annexed'); the dossier follows the Boina page. The Boina page has no capital other than 'Boina Bay', no Marovoay, no area. The af-07-a Merina dossier enters 'Sakalava kingdom of Boina' (a name, not this slug) for the Mahajanga gain of 1824; it should read boina-kingdom. Counterpart needing a dossier: the Antankarana kingdom (tributary to Boina, far north; the Boina page gives no dates). Gazetteer: names resolve (admin1 Boeny, Sofia, Betsiboka; place Mahajanga).

### menabe-kingdom (Menabe Kingdom, 1540-1900)

Cliopatria has no Menabe; the af-07-a Merina dossier enters 'Sakalava kingdom of Menabe' as a counterpart name (it should read menabe-kingdom). Pages: Menabe (the region article, with a short history section) and Sakalava people. The articles 'Menabe Kingdom', 'Kingdom of Menabe' and 'Sakalava Kingdom' do not exist (URL_NOT_FOUND). The Menabe page's dates (founding c. 1540, 1610-1685, campaigns of 1820-22, 1834, 1846, 1897, 1900) disagree with the Sakalava page ('first significant Sakalava kingdoms were formed around the 1650s'; the kingdom split 'After Andriantonkafo', 1722-1742); this dossier takes the Menabe page for the kingdom and mentions the Boina founding date from the Boina page. Merina conquest: the Menabe page has the Merina taking southern Menabe in 1834 and winning in 1846, which makes the Cliopatria Merina shape of 1824 (Morondava inside, per af-07-a) too early by a decade; no vassal event is entered for the post-1846 Merina governor (the Merina side's job). Ends 1900 (pacification). Gazetteer: names resolve (admin1 Menabe, Melaky, Boeny, Sofia, Betsiboka; place Morondava).

### transvaal-colony (Transvaal Colony, 1902-1910)

Cliopatria has no Transvaal Colony: British Africa covers the region. The dossier starts at the Treaty of Vereeniging (31 May 1902), not the 1 September 1900 proclamation, because the South African Republic dossier (af-07-b) already carries the British occupation of 1900-1902 as occupation_start/end by british-colonial-empire and dissolves the republic on 31 May 1902. Not typed: responsible government (infobox 6 December 1906; Het Volk won the election of 20 February 1907 and Botha became Prime Minister), Swaziland's transfer to the Transvaal (1903, Swaziland dossier), Chinese labour (1904-10). Area not on the page. Counterpart needing a dossier: union-of-south-africa (1910-1961), whose Cliopatria row 'South Africa' begins in 1932 (af-08 owns south-africa; the 1910-1931 years are drawn as British Africa). Gazetteer: names resolve (region Transvaal, places Vryheid and Volksrust).

### orange-river-colony (Orange River Colony, 1902-1910)

Cliopatria has no Orange River Colony. Starts at the Treaty of Vereeniging (31 May 1902) because the Free Orange State dossier (af-07-b) carries the occupation from 13 March 1900. The page's dates disagree with its sibling's: annexation 'on 6 October 1900' (this page) against 28 May 1900 (Orange Free State page, in the free-orange-state ledger); the intro says 'annexed (1902)'. Not typed: self-government on 27 November 1907 (Abraham Fischer premier). No boundary or area on the page. Counterpart needing a dossier: union-of-south-africa (see transvaal-colony). Gazetteer: 'Orange Free State' is a region alias of admin1 Free State.

### pedi-empire (Pedi Empire, 1780-1882)

Cliopatria has no Pedi. One page opened (Pedi people; the article Pedi_Empire did not load: URL_NOT_FOUND). The page gives no capital and no area; the capital point is a stand-in; the Thulare box is the page's three place names (Rustenburg, lowveld, Vaal) turned into a polygon. The end date is 1882 (monarchy dismantled); the page offers 1879 (defeat), 1882 and 1885 (a small reserve) as markers. The Zwide/Ndwandwe invasion has no date on the page. Counterparts needing dossiers: ndwandwe-kingdom (c. 1790-1820), swazi-kingdom (written below), and union-of-south-africa for the later land. Gazetteer name needed: region Sekhukhuneland (Limpopo/Mpumalanga, south of the Steelpoort River).

### mpondo-kingdom (Mpondo Kingdom, 1820-1894)

Cliopatria has no Mpondo kingdom. One page: Pondoland (the article Mpondo_Kingdom did not load: URL_NOT_FOUND). The page is thin: no founding date, no kings other than Faku in 1820, no Mfecane, no 1844 treaty, no Port St Johns cession of 1878, no area. The state is dated from 1820 because that is the first dated ruler action; it is certainly older. The af-07-a Cape dossier enters 'Mpondo kingdom' (a name, not this slug) for the 1886 and 1894 gains. Gazetteer names Pondoland and Xesibeland are used by the Cape dossier too (to be added). Capital is a stand-in.

### griqualand-east (Griqualand East, 1862-1877)

Cliopatria has no Griqualand East. One page opened. Dates conflict inside the page (1860-63 trek; 1862 laager; Kokstad 1872) and the annexation is a span (British control 1874, Act 1877, promulgation 17 September 1879); the dossier ends at the 1877 act, matching the Cape dossier's gain of 1877. The event 'capital_move' in 1874 is a marker for the British assumption of control, not a move (the page gives no second capital). Capital coordinate is the researcher's own, flagged. Region name Griqualand East is used by the Cape dossier too (gazetteer to add). The 1878 rising is not on the page.

### griqualand-west (Griqualand West, 1800-1880)

Cliopatria has no Griqualand West (the af-07-a Cape dossier draws it as part of the Cape from 1871). One page opened. Not on the page: the 1867 diamond discovery, the 17 October 1871 Keate Award date, the 1876 compensation figure (only 'in full satisfaction of all claims', July 1876), Hay, the 1878 rising. The Free State claim is not typed as a contest because no campaign is described. The Klipdrift Republic (30 July 1870) is a counterpart needing a dossier (a short-lived digger republic). The pre-1871 Griqua polity (Adam Kok I, Waterboer, Klaarwater) has only the infobox year 1800 for its start; the Griquatown point is the researcher's own knowledge. Region name Griqualand West is a gazetteer name still to be added.

### british-kaffraria (British Kaffraria, 1860-1866)

Cliopatria has no British Kaffraria. The dossier covers only 1860-1866 (a separate Crown colony); before that the area was Cape land from 17 December 1847 ('the area was again seized by the new British Governor Harry Smith') and, in 1835-36, the Queen Adelaide Province (all in the Cape dossier). The page's infobox says 'Established: 1835', the lead 1847: unreconciled. Also: Xhosa cattle-killing 1856-57, German settlers 1858-59 and 1877-78. King William's Town point is the researcher's own. Gazetteer region British Kaffraria is used by the Cape dossier too.

### stellaland (Stellaland, 1882-1885)

Cliopatria has no Stellaland or Goshen. One dossier covers both: the page 'Stellaland' (and British Bechuanaland) say the two republics merged in 1883 as the United States of Stellaland; the Goshen article did not load (Land_Goshen, Republic_of_Goshen and Goshen_(Boer_republic) all URL_NOT_FOUND), so Goshen's own founding (1882) is not dated here. The South African Republic's brief annexation of 16 September 1884 is in the war entry; the SAR dossier has no matching event. Counterparts without dossiers: Mankoroane's chiefdom (the Tlhaping) and Montshiwa's Rolong (the page does not name them). Gazetteer: Mmabatho stands in for Rooigrond; the British Bechuanaland region is used for the first-keyframe text only.

### british-bechuanaland (British Bechuanaland, 1885-1895)

Cliopatria has no British Bechuanaland. One page opened (British Bechuanaland; Stellaland read too). The Bechuanaland Protectorate to the north has no date on the page and is the af-08 dossier's matter. Montshiwa and Mankoroane are not named on the page. Area 133,190 km2 comes from the body text (not the infobox). Gazetteer: region name British Bechuanaland is used by the Cape dossier too (to be added).

### mtetwa-paramountcy (Mtetwa Paramountcy, 1780-1817)

Cliopatria has no Mthethwa row; the sibling zululand dossier names mtetwa-paramountcy as predecessor with 'extent unknown', so this slug is kept. Three pages: Mthethwa_Paramountcy (thin: infobox c. 1780-1817, no area, no capital, no rivers), Dingiswayo (the only extent: Umkhomazi to Hluhluwe, Etherington 2005; reign 1806-1817 in the infobox but also c. 1800-1818 and a 'late 1810' death in the text), Ndwandwe (1817/1818 Mbuzi Hill). The box bounds 30.2S and 28.0S are the researcher's own knowledge of Umkhomazi and Hluhluwe (neither is in the gazetteer); the box is clipped to KwaZulu-Natal. It overlaps the Ndwandwe box and the sibling Zulu core of 1816 by design of the sources (Hluhluwe lies north of the Black Umfolozi, inside the Ndwandwe range). The 1811 joining of the Zulu and Buthelezi clans (Mthethwa page: 'About 1811, the Buthelezi and other Nguni groups, including the then still marginal Zulu clan led by Senzangakona, joined a confederacy dominated by the Mthethwa') is not a ledger event because the page names no land. Gazetteer names needed: Umkhomazi (river), Hluhluwe (place), Oyengweni.

### ndwandwe-kingdom (Ndwandwe Kingdom, 1780-1820)

Cliopatria has no Ndwandwe row; the sibling zululand dossier already names ndwandwe-kingdom as counterpart for its 1820 gain, so this slug is kept. Two pages: Ndwandwe (the title Ndwandwe_Kingdom did not load: URL_NOT_FOUND) and Dingiswayo for context. The page gives no area, no capital, no coordinates and no Pedi or Nxaba (it lists 'Langa KaXaba' as the pre-1805 ruler). End year: 1820 (defeat at Mhlatuze, land passes to the Zulu) against the infobox's 1825. The box limits are the researcher's own estimate of the two river lines; the gazetteer has a Pongola river but no Black Umfolozi. Counterparts: zululand (Cliopatria/af-07-b), mtetwa-paramountcy (written in this batch), swazi-kingdom (written in this batch), pedi-empire (written in this batch). Gazetteer names needed: Black Umfolozi (river), Ngome.

### swazi-kingdom (Swazi Kingdom, 1744-1885)

Cliopatria's Swaziland row starts only in 1885; af-07-b writes it. This dossier covers the Swazi kingdom before it: Mfecane-era Swazi state of Ngwane III, Sobhuza I, Mswati II and Mbandzeni. Two pages: History_of_Eswatini (dated reigns and treaties) and the Eswatini article (opened as Kingdom_of_Eswatini; the capital sentences and the 'twice its current size' line). Not recorded because the land is not named: the 1846 and 1855 land sales to the Dutch republics (170 cattle each; 'the wording was vague'), the Swazi-Pedi, Swazi-Ndwandwe conflicts (undated: 'conflict with the Ndwandwe under Zwide pushed the Swazi north'), and Mswati II's 1850s campaigns. The ring is area-matched, not surveyed. Mpumalanga after 1881 is not drawn as Swazi. Rulers (History page): Dlamini III c. 1720-1744; Ngwane III (accession year not given); Ndvungunye 1780-1815; Sobhuza I 1815-1839; Mswati II 1839-1865; regency (Tsandzile Ndwandwe) to 1875; Mbandzeni from 1875 (the 1872 note: Ludvonga died, Mbandzeni chosen). Counterparts: south-african-republic and portuguese-mozambique (this batch), swaziland (af-07-b), ndwandwe-kingdom and pedi-empire (this batch), zululand (af-07-b), lydenburg-republic (no dossier). Gazetteer names needed: Barberton, Zombodze, Shiselweni (site), Nomahasha.

### lozi-kingdom (Lozi Kingdom, 1650-1911)

Cliopatria has no Lozi row. Two pages: Barotseland (area, concessions, Order of 1899, losses of 1905 and 1911, the 1911 merger) and Lozi people (Makololo date 'about 1830'; reign of Lewanika). The 'Barotseland Protectorate' as a named entity is not on the pages. Year conflicts recorded: Makololo conquest (1830, c. 1840, 1838 settling at Victoria Falls, by 1845), Lawley concession (1898 on the page, 1900 elsewhere), Portuguese occupation 1895 vs. 1905 loss. The Western Province of Zambia and the 352 km Mongu disc are stand-ins; the Kwito and Kafue limits are not drawn. Counterparts: makololo-kingdom (this batch), british-south-africa-company (no dossier; also Ndebele), portuguese-angola and german-africa and british-africa (Cliopatria). Gazetteer names needed: Bulozi / Barotseland (region), Lealui, Limulunga, Kwito (river).

### makololo-kingdom (Makololo Kingdom, 1840-1864)

Cliopatria has no Makololo row. Pages: Makololo, Sebetwane, Barotseland. Dates: migration north from 1823, defeat at Dithubaruba 1826 by the Ngwaketse, to the Okavango 1834, victory over the Batawana 1835, near Victoria Falls 1838, Lozi plain c. 1840 (pages say c. 1830, 1838, c. 1840, by 1845); Sebetwane died 7 July 1851 at Linyati; succeeded by his daughter Mamochisane, who abdicated for Sekeletu; end 1864. The Linyanti capital is outside Zambia (not drawn); the Western Province stand-in covers only the Barotse Plain. Pre-1840 Makololo state in Botswana (1823-40) held no land the pages bound and is not drawn. Counterpart: lozi-kingdom (this batch). Gazetteer name needed: Linyanti.

### xhosa-kingdom (Xhosa Kingdom, 1779-1878)

Cliopatria has no Xhosa row; the Cape dossier names 'Xhosa chiefdoms' (a string, not a slug) as counterpart six times and this slug is the dossier for it. Two pages: Xhosa Wars (every date and land above) and Xhosa people (the kingdom 'founded before the 15th century' by Tshawe; Amatola and Winterberg; Kei and Fish rivers; cattle-killing 1856-1858, which is not a land event). The Xhosa_Kingdom title did not load (URL_NOT_FOUND). The Transkei page was opened and has nothing on the 19th century. The start year 1779 is a bridge (first Xhosa land date), not the founding. Gcalekaland is drawn as a box (Great Kei to Mthatha) since no page gives its boundaries; Tembuland, Fingoland, Griqualand East and Pondoland are outside it. The page does not say the Cape annexed Gcalekaland in 1878-79; the successor is the Cape by the page's 'administered as a British territory'. Counterpart: british-cape-colony (af-07-b), whose events use the string 'Xhosa chiefdoms'. Gazetteer names needed: British Kaffraria (flagged by the Cape dossier too), Gcalekaland, Transkei, Ciskei, Zuurveld, Great Fish (river), Keiskamma (river).


## Repairs after review (2026-10-19): what the author changed, and where the author disagrees

Seven dossiers were failed by the reviewer (review-af-07-x.md) and are repaired here; the other twenty were not touched. The per-dossier `notes` fields in the JSON files carry the same text, marked "Repair 2026-10-19". The tables above (events, keyframes) describe the first version. Every dossier below validates with 0 errors. Pages reopened: Mutapa Empire, Nyatsimba Mutota, Kingdom of Barue, Soshangane, Gaza Empire, Sekwati, Sekhukhune, Niassa Company, Portuguese Mozambique, Anglo-Portuguese Treaty of 1891, Sena (Mozambique), Barotseland, Lewanika, Lozi people, Basutoland, Griqualand West, Griqua people. Not loading: Nyanhehwe_Matope, Uteve, Sekhukhune_I (URL_NOT_FOUND).

### mutapa-empire (fail, 3 findings, all applied)
- /ledger/6 (1632 loss of the lower Zambezi valley) DELETED. The page says only 'a Portuguese captain led an army to subdue the Valley from Quelimane to Sena'; it never says the Valley was Mutapa's, and no keyframe draws it. The one hint (not used): 'the Tonga of the Lower Zambezi had been in rebellion against Mutapa since c. 1550'. portuguese-mozambique /ledger/6 now gains the valley from 'nobody'.
- K1 split at 1470: mutapa-empire_1450 (1450-1469, plateau and Tete) and mutapa-empire_1470 (1470-1606, adding Manica and Manicaland), so the keyframe and /ledger/2 agree. Both years remain bridges at confidence 1.
- Chidima capital (1723-1885) moved from Tete town to the gazetteer's Luangwa (Mozambique, Tete province, about 340 km up-river, inside the 1696 and 1760 shapes), flagged APPROXIMATE. The page says only 'the region of Chidima' and links Zumbo with it; no coordinates. Disagreement: none; but the stand-in is chosen to lie inside the shape, not to locate Chidima.
- Thin: Nyatsimba Mutota gives reign '1420-1450', founding 'mid-15th century', campaigns 'around 1440' (no founding year; 1430 stays a bridge, confidence 1). Kingdom of Barue: 'In 1608, Barue ceased paying tribute'; no Mukombwe suzerainty, no end of it (1692 stays a bridge). Matope and Uteve pages did not load.

### gaza-empire (fail, 2 findings, both applied)
- Overlap with portuguese-mozambique SETTLED in Portugal's favour: the Sofala (30 km), Inhambane (25 km) and Delagoa Bay (40 km) posts and the 60 km Zambezi strip in Sofala province are subtracted from Gaza K1 (and from the 1837 and 1895 ledger regions); portuguese-mozambique keeps them (K5-K7) and enters no loss. About 21,000 km2 by the gazetteer (the reviewer said about 25,000; Gaza K1 is now 238,000 km2, not the author's 272,000, which the gazetteer puts at 259,000 for the whole five provinces). Reason: the Gaza page says 'overran' without a year or a later status; the Soshangane page dates the fort destructions (Lourenço Marques 28 October 1833, Inhambane 3 November 1834, Sofala October 1836) and has the Portuguese pay tribute in the 1840s-50s, with Sena and Tete 'forced to pay tax' (no year). No page dates a Portuguese loss or recovery, so no dated event is entered; the alternative (dated losses in portuguese-mozambique, or a contest) would invent dates.
- Coast gain /ledger/1 moved from 1830 to 1834 (confidence stays 1) and K0 split (gaza-empire_1824 to 1833; gaza-empire_1834 to 1836, adding Inhambane and Maputo without the posts). The reviewer offered 1837 or a split at 1830; 1834 follows the Soshangane page's dated fort destructions. Disagreement between pages: Soshangane puts Nxaba's removal at 1835, the Gaza page at 1837 (kept); Soshangane puts the lower Limpopo residence at 1827-1835/6, the Gaza infobox gives Chaimite 1828-1834.
- Capital for 1824-1827 added (a tributary of the Nkomati north of Lourenço Marques, in Maputo province, outside K0; dot at Xai-Xai).

### basutoland (fail, 1 finding, applied)
- K1 ends in 1870; basutoland_1884 (1884-1966, Lesotho) added; 1871-1883 is the Cape's. The dossier keeps its life and colour through the gap (rule 2). The reviewer's alternative (a vassal relation) was not taken: the page says 'annexed to the Cape Colony by Act No. 12 of 1871', and the Cape dossier agrees. The Gun War contest (1880-81) is unchanged.

### portuguese-mozambique (fail, 4 findings, all applied)
- North of Mozambique: new gains from nobody, each with a keyframe: Nampula 1891 (confidence 1, a bridge: the Portuguese Mozambique page names it only as 'the colony of Moçambique' and dates no occupation; the reviewer asked for confidence 2, which the treaty page does not support for Nampula), Zambezia 11 June 1891 (confidence 2: the treaty gave Portugal 'more territory in the Zambezi valley'; the province is my reading), Cabo Delgado and Niassa March 1893 (confidence 2: the Niassa Company charter, 'from the Ruvuma River to the Lúrio River'). These are claims: the Niassa Company occupied the inland only in 1900-1902 and again 1909-1912, and Portugal 'secured political control over most of its territory in 1918'; the certainty note says so. Keyframes portuguese-mozambique_1891 and _1893 added; K7 now ends 1890; the 1895 shape is the whole country.
- Chioko: /ledger contest_start 1897, contest_end 1902 and wars/2 now name the string "Chioko's Mutapa-Barue coalition" (mutapa-empire ends in 1885).
- 1632 gain from nobody (see mutapa-empire).
- Gaza overlap settled in Portugal's favour (see gaza-empire). The K6 (1781) note says so.
- Thin: the Sena page gives no 1530s year ('In the early 1500s the Portuguese took over the region') but the town's coordinates (17.4417S, 35.0272E, east bank of the Zambezi) for the gazetteer's Sena entry.
- Kionga Triangle: inside the Cabo Delgado province as drawn from 1893 although the page has it transferred from German East Africa only on 28 June 1919; the overlap is small (no area on the pages) and is left for af-08 (german-africa).

### pedi-empire (fail, 3 findings, all applied; two dates improved)
- eSwatini subtracted from the K0 box, /ledger/0 and /ledger/1 (the swazi-kingdom overlap, about 11,000 km2).
- Loss of the outer lands moved from 1820 to 1826 and counterpart from ndwandwe-kingdom to nobody (confidence 1 to 2). The Sekwati page: 'Around 1826, the Ndebele under Mzilikazi seized the opportunity and overthrew the Pedi regime'; the Pedi people page's 'Ndwandwe invaders' have no year. ndebele-kingdom /ledger/1 gains Rustenburg and Pretoria from nobody in 1826, so the pair now matches. The reviewer suggested keeping 1820 and using nobody or a Ndwandwe string; the new page dates the event, so 1826 is used. K0 now ends 1825; K1 is pedi-empire_1826.
- Capital: no gazetteer place lies in Sekhukhuneland (the only places in 24-25.6S, 29.2-30.6E are Lebowakgomo, Polokwane and Tzaneen), so the stand-in is the centre of the author's hint box (30.0E, 24.7S), APPROXIMATE. Two entries from the Sekwati page: Manganeng on the Steelpoort River (to 1826), then Phiring and Thaba Mosego (1827-1882; the move to Thaba Mosego after the 1852 siege). Sekhukhune lived on Thaba Leolo (Sekhukhune page, no years).
- Month of the 1879 defeat added (November 1879, Sekhukhune page).
- Thin: the 1826-1876 extent remains Sekhukhuneland alone; both pages are silent except for the Steelpoort boundary with the Lydenburg Republic (undated treaty).

### griqualand-west (fail, 1 finding, applied)
- /ledger 1871-10 is now a 'rename' (Griqua state to British territory), not a loss to british-colonial-empire; K0 stays to 1880. The page (reopened): 'British Colony (1871-1880)' with its own capital from 1873; it does not say the Cape held the territory before 18 October 1880. ROUTING: british-cape-colony (af-07-b) still has an 1871-10 gain from 'Griqualand West'; it should go (the merge of 1880-10 stays).
- Thin: the Griqua people page gives no boundaries, no Griqua founding year and no Keate Award; the pre-1871 outline stays at confidence 1.

### lozi-kingdom (fail, 2 findings, both applied)
- K0 split: lozi-kingdom_1650 (1650-1839) and lozi-kingdom_1864 (1864-1877); no Lozi shape in 1840-1863 (makololo-kingdom K0 draws the Western Province).
- Caprivi: the K2 and K3 notes (lozi-kingdom_1899 and _1905) and the 1878 note say the strip overlaps Cliopatria's german-africa from 1890. DISAGREEMENT/UNVERIFIED: the Barotseland page (reopened) gives only the 1911 loss and nothing for 1890-1910; the 1890 start is the reviewer's statement about Cliopatria's row, not a page, and is recorded as such for af-08.
- Typed the 1895 Portuguese occupation (occupation_start 1895, occupation_end 1905, portuguese-angola) over the same western region as the 1905 loss; Barotseland: 'In 1895, the Portuguese occupied some of the Lozi's western territory'. The region is my reading.
- Thin: Lozi people 'founded in the 17th century' (no year); Lewanika gives only his reign (no 1878 extent, rivers or tributaries).

### Still open after the repairs
- Cape (af-07-b): Griqualand West 1871-10 gain; Gcalekaland 1878; the Pedi contest 1876-77 and the Swazi gain 1881 (reviewer's list, unchanged).
- eu-12 / af-08: portuguese-empire gains the Gaza lands in 1895 as portuguese-mozambique does.
- Gazetteer: Sena (place, 17.4417S 35.0272E from its page), Sekhukhuneland (region), Conquered Territory, Griqualand West, Kionga Triangle (unchanged); Manganeng, Phiring, Thaba Mosego, Thaba Leolo (places, no coordinates on the pages).
