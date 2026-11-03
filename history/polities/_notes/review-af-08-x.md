# Review of batch af-08-x (2026-10-24)

Reviewer: adversarial review per history/briefs/reviewer-brief.md with the orchestrator's adjustments (spot-check budget 4 per dossier, small fixes applied by the reviewer and re-validated). Author's report and notes read first. All 14 dossiers validate with no errors before and after the edits.

Verdict scheme: `fix` = accepted; items marked APPLIED were made by the reviewer, items marked TODO are non-blocking fixes for the author. No dossier has an open blocking finding.

## french-west-africa: fix

Area: infobox 4,689,000 km2 (no year), keyframe about 4,971,000 km2, ratio 1.06. No Cliopatria shape (new state); the 1922-1958 keyframe (eight countries) resolves to about 4.97 M km2 against the infobox (no year given); ratio 1.06 stated in keyframe 3.

Spot checks: /ledger/1 French_West_Africa: confirmed; /ledger/5 History_of_Burkina_Faso: confirmed; /ledger/7 French_West_Africa: confirmed; /ledger/8 French_West_Africa: confirmed; /ledger/11 French_West_Africa: confirmed.

- APPLIED `/ledger/8/counterpart`: The 1904 Dahomey gain named the Kingdom of Dahomey, whose dossier ends in January 1894 (loss and dissolve to french-africa), ten years before the event. Evidence: French West Africa page: 'Dahomey was added in 1904, after having been put under colonial tutelage in 1892'; dahomey.json L17-L18 (1894/1 loss and dissolve, counterpart french-africa); the event's own note says the kingdom fell in 1894. Fix: Counterpart 'french-africa' (the colony of Dahomey was French land); reason appended to the note.
- TODO `/ledger/10/counterpart`: Niger's 1922 gain is from 'nobody', but the federation page says Niger was already a French Military Territory in 1904, so the land was French before 1922 and the 1904-1921 keyframe leaves it out. Evidence: French West Africa page: 'In 1904, both Mauritania and Niger were classed "Military Territories"'; also 'The future states of Mauritania and Niger remained out of the federation until the 1920s and 1940s respectively.' Fix: Optional: keep the History of Niger reading but name the counterpart 'french-africa' (the military territory) instead of 'nobody', or add Niger to keyframe 2 as the Military Territory from 1904; the note already records the disagreement.
- THIN `/ledger/0`: Dated French campaigns against Samory 1894-1898 (the contest_start is confidence 1) (try https://en.wikipedia.org/wiki/Samori_Ture)
- THIN `/keyframe_review/2`: Adrar and the northern Mauritanian conquest (1909-1912) and the Tuareg revolts in Niger, which bound the Saharan hold (try https://en.wikipedia.org/wiki/French_conquest_of_Mauritania)

## anglo-egyptian-sudan: fix

Area: infobox 2,505,800 km2 (1951), keyframe about 2,370,000 km2, ratio 0.95. Sudan plus South Sudan resolve to about 2.33 M km2 plus Halaib (about 20,000); infobox figure is for 1951; ratio stated in keyframe 4.

Spot checks: /ledger/1 Halaib_Triangle: confirmed; /ledger/2 Halaib_Triangle: confirmed; /ledger/3 Halaib_Triangle: confirmed; /ledger/4 Lado_Enclave: confirmed; /ledger/5 Lado_Enclave: confirmed; /ledger/8 Anglo-Egyptian_Sudan: confirmed; /ledger/10 Sarra_Triangle: confirmed.

- APPLIED `/ledger/4/counterpart`: The 1910 Lado gain named congo-free-state, a dossier that ends in November 1908; the enclave was held by the Belgian Congo from 1908 to 1910. Evidence: Lado Enclave page: 'a leased territory administered by the Congo Free State and later by the Belgian Congo that existed from 1894 until 1910'; infobox 'Belgian Congo (1908-1910)'; belgian-congo.json L1 (1910/6 loss of the Lado Enclave). Fix: Counterpart 'belgian-congo'; the note's last sentence rewritten to cite the page.
- TODO `/keyframe_review/4/correction`: The Sarra Triangle (about 30,000 km2) appears in keyframe 4 (1916) but in no earlier keyframe and in no gain event, so the 1916 change adds land the ledger does not explain. Evidence: Sarra Triangle page: the strip was 'originally claimed by Britain and added to Anglo-Egyptian Sudan' (no date); keyframes 0-3 omit it, keyframe 4 adds it, ledger has only the 1934 loss. Fix: Either add the Sarra Triangle to keyframes 0-3 with a note that the page gives no date for its attachment, or add a dated gain (counterpart nobody or french-africa) from a page that gives one (the Anglo-French declaration of 21 March 1899 / convention of 1919).
- THIN `/ledger/7`: Ali Dinar's Darfur as a tributary of the Condominium 1899-1916 (a vassal_start/vassal_end pair would draw it in the lighter tint) (try https://en.wikipedia.org/wiki/Ali_Dinar)
- THIN `/certainty/0`: The 1914 Sudan-Uganda exchange area and the Ilemi and Kafia Kingi edges (try https://en.wikipedia.org/wiki/Sudan%E2%80%93Uganda_border)

## french-equatorial-africa: fix

Area: infobox 2,500,000 km2 (no year), keyframe about 2,392,000 km2, ratio 0.96. Gabon, Congo, CAR and Chad resolve to about 2.39 M km2 (gazetteer cells); infobox gives no year.

Spot checks: /ledger/1 French_Equatorial_Africa: confirmed; /ledger/2 Wadai_War: confirmed; /ledger/3 Wadai_War: confirmed; /ledger/4 French_Equatorial_Africa: confirmed; /ledger/5 Neukamerun: confirmed; /ledger/7 Neukamerun: confirmed; /ledger/9 French_Equatorial_Africa: confirmed.

- TODO `/wars/1 and /ledger/8-9`: The Battle of Gabon is drawn as a contest between the federation and 'free-french', but the federation itself (minus Gabon) had rallied to Free France; the other side was Vichy Gabon. Evidence: French Equatorial Africa page: 'French Cameroon and the entirety of the AEF except for Gabon rallied to the Free French Forces in August 1940'; 'Gabon instead remained loyal to Vichy France until 12 November 1940'. Fix: Name the Vichy side as the counterpart (a 'vichy-france' slug, flagged as needing a dossier) or say in the war note that the counterpart string stands for the Free French forces fighting Vichy Gabon on the federation's behalf; the zone (Gabon) is right.
- TODO `/ledger/4`: Dar al Kuti is 'gained' in 1912 but the whole Central African Republic, Dar al Kuti included, is already in keyframe 0 (1910); the 1912 change is a status change, not new land. Evidence: French Equatorial Africa page: 'declaring the slaves in Dar al Kuti free ... and annexing the territory in 1912'; keyframe 0 = Gabon + Congo + CAR + Chad minus Ouaddai. Fix: Either remove Dar al Kuti from keyframe 0 (minus region) or model 1910-1912 as a vassal_start/vassal_end pair ending in 1912; keep the gain only if the keyframe is changed.
- THIN `/keyframe_review/1`: Dates of the occupation of Borkou, Ennedi and Tibesti (northern Chad), drawn French from 1912 (try https://en.wikipedia.org/wiki/Borkou)

## italian-libya: fix

Area: infobox 1,759,541 km2 (1939), keyframe about 1,376,000 km2, ratio 0.78. Country Libya resolves to 0.78 of the infobox (desert cell undercount, stated); the Aouzou strip (page: 'in 1935 under the Mussolini-Laval agreement Italy received the Aouzou strip, which was added to Libya') is deliberately not drawn and explained in notes.

Spot checks: /ledger/0 Italo-Turkish_War: confirmed; /ledger/2 Italo-Turkish_War: confirmed; /ledger/4 Italo-Turkish_War: confirmed; /ledger/5 Italo-Turkish_War: confirmed; /ledger/10 Second_Italo-Senussi_War: confirmed; /ledger/12 Second_Italo-Senussi_War: confirmed; /ledger/13 Second_Italo-Senussi_War: confirmed; /ledger/18 Italian_Libya: confirmed; /ledger/8 Tripolitanian_Republic: not on page (quote only; event supported by another sentence; fixed).

- APPLIED `/ledger/8/note`: The note quoted 'Italian rule was restored four years later' from the Tripolitanian Republic page; the sentence is not on the page. Evidence: Tripolitanian Republic page (searched for 'four years' and 'restored': neither occurs); the page says 'Italy reasserted control over the colony in the early 1920s' and 'By 1923, Italian control was effective in the territories of the Republic'. Fix: Quote replaced with the page's sentence (event is confidence 2 and otherwise supported).
- APPLIED `/ledger/11/confidence`: Confidence 3 on a gain drawn as the whole Tripolitania region while the page names only the Ghibla. Evidence: Second Italo-Senussi War page: 'By late 1928, the Italians had taken control of Ghibla, and its tribes were disarmed.' Fix: Confidence lowered to 2, reason appended to the note.
- TODO `/ledger (missing, 1925)`: No event for the Egyptian treaty of 6 December 1925, and the notes say no page had it cede land; the Italian Libya page says it did. Evidence: Italian Libya page: 'Egypt ceded Kufra and Jarabub districts to Italian Libya on December 6, 1925'; Egypt-Libya border page: the treaty 'finalised the border at its current position'. Fix: Add a 1925/12 gain from 'kingdom-of-egypt' of the Jaghbub (Jarabub) oasis area (place Al Jaghbub, about 50 km) at confidence 2-3, and correct the notes sentence.
- TODO `/wars (missing, 1940-1943)`: The Second World War Western Desert campaign, in which Cyrenaica changed hands (British February-April 1941, December 1941-January 1942, from November 1942), has no war and no contest events; the dossier jumps from 1934 to the 1943 losses. Evidence: italian-africa.json L60-L65 (Operation Theseus 1942/1, Gazala-Tobruk 1942/6, loss of Cyrenaica 1942/11, Fezzan 1943/1, end 1943/2); british-africa.json L47 (1943/2 occupation_start). Fix: Add a war 'Western Desert campaign' 1940-1943 (zones Cyrenaica, Marmarica) with contest_start 1940 and contest_end 1943, and the November 1942 loss of Cyrenaica, from the Western Desert campaign page.
- THIN `/wars`: Western Desert campaign 1940-1943 (contest zones and the November 1942 loss of Cyrenaica) (try https://en.wikipedia.org/wiki/Western_Desert_campaign)
- THIN `/keyframe_review/1`: Who held the interior 1912-1914 (the keyframe draws all Libya Italian although the Senussi held Cyrenaica's interior) (try https://en.wikipedia.org/wiki/First_Italo-Senussi_War)

## northern-nigeria-protectorate: fix

Area: infobox 660,000 km2 (1912), keyframe about 760,000 km2, ratio 1.15. Body text, not infobox: 'In 1912 ... approximately 660,000 square kilometres'; the twenty northern states resolve to about 0.76 M km2, ratio stated in keyframe 2.

Spot checks: /ledger/0 Northern_Nigeria_Protectorate: confirmed; /ledger/1 Northern_Nigeria_Protectorate: confirmed; /ledger/3 Colony_and_Protectorate_of_Nigeria: confirmed; /ledger/4 Colony_and_Protectorate_of_Nigeria: confirmed; /ledger/5 Northern_Nigeria_Protectorate: confirmed.

- TODO `/ledger (missing, 1902)`: identity.capitals moves from Lokoja to Zungeru in 1902 but the ledger has no capital_move event. Evidence: Northern Nigeria Protectorate page: 'Lokoja was the capital from 1900'; 'Zungeru became the headquarters for the protectorate in 1902 because it was the most northerly city accessible by river transport.' Fix: Add a 1902 capital_move (destination Zungeru in the note), source the protectorate page, confidence 3.

## colony-and-protectorate-of-nigeria: fix

Area: infobox 0 km2 (no year), keyframe about 981,000 km2, ratio 0.0. The page has no area (stated in notes); country Nigeria resolves to about 0.98 M km2 against Nigeria's 923,768 km2.

Spot checks: /ledger/0 Colony_and_Protectorate_of_Nigeria: confirmed; /ledger/1 Northern_Nigeria_Protectorate: confirmed; /ledger/2 British_Cameroons: confirmed; /ledger/6 Colony_and_Protectorate_of_Nigeria: confirmed.

- TODO `/wars/0 and /ledger`: The Kamerun campaign (1914-1916) is listed as a war with a zone but the ledger has no contest_start/contest_end for it, so the ground fought over in 1914-1916 is not drawn. Evidence: german-africa.json L17 (1914/8 contest_start, Allied invasion of Kamerun) and L33 (1916/3 contest_end, 'Infobox 6 August 1914 - 10 March 1916'). Fix: Add contest_start 1914/8 and contest_end 1916 with counterpart german-africa over the British Cameroons zone (Kamerun campaign page).
- TODO `/ledger/4-5 (mirror)`: The vassal relation over the British Cameroons (1922-1960) has no mirror in british-cameroons.json. Evidence: british-cameroons.json has no vassal_start/vassal_end; British Cameroons page: 'British Cameroons was still under the administration of Nigeria'; Colony and Protectorate page: '...were administered as part of Nigeria'. Fix: Fix on the british-cameroons side (see that verdict); no change here if the mirror is added there.

## german-east-africa: fix

Area: infobox 995,000 km2 (1912), keyframe about 862,000 km2, ratio 0.87. Tanzania + Rwanda + Burundi resolve to about 0.86 M km2 (lakes excluded); ratio stated in keyframe 3.

Spot checks: /ledger/0 German_East_Africa: confirmed; /ledger/1 German_East_Africa: confirmed; /ledger/4 German_East_Africa: confirmed; /ledger/5 Ruanda-Urundi: confirmed; /ledger/7 East_African_campaign_(World_War_I): confirmed; /ledger/10 East_African_campaign_(World_War_I): confirmed; /ledger/11 East_African_campaign_(World_War_I): confirmed; /ledger/12 East_African_campaign_(World_War_I): confirmed; /ledger/15 German_East_Africa: confirmed; /ledger/18 German_East_Africa: confirmed.

- TODO `/ledger/8-11,13-14,16-17/counterpart`: The 1916-1919 occupations name belgian-congo and british-africa as occupiers, while this batch's own ruanda-urundi and tanganyika-territory dossiers are founded in 1916 on the same land as the occupation regimes; the two models draw the land twice and none of the events pair. Evidence: Ruanda-Urundi page infobox 'Belgian occupation: 6 May 1916'; Tanganyika Territory infobox 'Occupied territory of the United Kingdom (1916-1922)'; ruanda-urundi.json L0/L2 (found/gain 1916), tanganyika-territory.json L0/L1 (found 1916, gain 1917/11), belgian-congo.json L4-L8 (occupation of Ruanda-Urundi from 1916, gain 1922). Fix: Pick one model for the batch: either the occupier counterparts here become 'ruanda-urundi' and 'tanganyika-territory' and those two dossiers record occupation_start/occupation_end of german-east-africa for 1916-1919, or ruanda-urundi and tanganyika-territory start in 1919 with GEA's dissolve. Then the 1919 loss to ruanda-urundi (L15) needs its mirror there.
- TODO `/ledger/6`: Burundi's 1897 gain (confidence 1) is six years before the kingdom-of-burundi dossier's end (1903, treaty of Kiganda, to german-africa). Evidence: Ruanda-Urundi page gives no year for Urundi; kingdom-of-burundi.json L2 (1903 dissolve, 'Mwezi IV is forced into the treaty of Ikiganda'). Fix: Move the Burundi gain to 1903 (vassal_start in 1897-1899 if a page dates the station at Usumbura), citing the History of Burundi page.
- TODO `/ledger (missing, 1916)`: No event for the Portuguese capture of the Kionga Triangle in April 1916, though keyframe 3 keeps Kionga German to 1919. Evidence: german-africa.json L37: 'It came under Portuguese control in April 1916 during World War I'; East African campaign page: after the war 'the Kionga Triangle was ceded to Portugal'. Fix: Add occupation_start 1916/4 (counterpart portuguese-mozambique, region Kionga Triangle) and occupation_end 1919/6.
- TODO `/keyframe_review/0 and /ledger/3`: Keyframe 0 (250 km round Bagamoyo) includes the Sultan of Zanzibar's 16 km coastal strip, which was not German until 1890; the 1890 gain names 'nobody'. Evidence: German East Africa page: 'The Sultan was forced to accept the German claims on the mainland outside a 16-kilometre (10 mi)-strip along the coast.' Fix: Note it in keyframe 0, or minus the coastal strip and add a 1890 gain of the coast from the Sultanate of Zanzibar (no dossier for 1856-1963 yet).
- TODO `/ledger (missing)`: identity.capitals moves Bagamoyo -> Dar es Salaam (1890) -> Tabora (1916) without capital_move events. Evidence: German East Africa infobox: 'Bagamoyo (1885-1890) Dar es Salaam (1890-1916) Tabora (1916, temporary)'. Fix: Add capital_move events for 1890 and 1916.
- THIN `/ledger/6`: A dated year for Urundi becoming a German district (try https://en.wikipedia.org/wiki/History_of_Burundi)
- THIN `/wars/1`: Maji Maji end year (1907) and zone; the page gives only 21 October 1905 (try https://en.wikipedia.org/wiki/Maji_Maji_Rebellion)

## ruanda-urundi: fix

Area: infobox 0 km2 (no year), keyframe about 46,000 km2, ratio 0.0. Page has no area (stated); Rwanda + Burundi resolve to about 46,000 km2 (54,000 km2 real, lakes and cell edges).

Spot checks: /ledger/0 Ruanda-Urundi: confirmed; /ledger/1 East_African_campaign_(World_War_I): confirmed; /ledger/2 Ruanda-Urundi: confirmed; /ledger/5 Ruanda-Urundi: confirmed; /ledger/6 Ruanda-Urundi: confirmed; /ledger/7 Ruanda-Urundi: confirmed.

- APPLIED `/identity/family`: Family 'belgium' is not a key of colours.json families. Evidence: colours.json families: africa, britain, france, germany, italy, portugal ... (no belgium); belgian-congo.json uses 'africa'. Fix: Family set to 'africa' (as belgian-congo).
- TODO `/ledger/0,2 (mirror)`: The 1916 found/gain from german-east-africa have no mirror: german-east-africa records the same land as occupied by belgian-congo and lost to ruanda-urundi only in 1919; belgian-congo records it as its own occupation and gain (1922). Evidence: german-east-africa.json L8, L9, L13-L15; belgian-congo.json L4-L8. Fix: Resolve with the German East Africa fix (one occupation model for the batch).

## somaliland: fix

Area: infobox 177,125 km2 (2024), keyframe about 203,000 km2, ratio 1.15. Natural Earth Somaliland polygon resolves to about 203,000 km2; stated in keyframe 0 with the reason (Sool and eastern Sanaag).

Spot checks: /ledger/0 Somaliland: confirmed; /ledger/3 Somaliland: confirmed; /ledger/4 SSC-Khatumo: confirmed; /ledger/5 SSC-Khatumo: confirmed.

- TODO `/ledger/3 and /keyframe_review/0`: Las Anod is gained from Puntland in 2007 but is already inside keyframe 0 from 1991, and Puntland's dossier never holds it or records the loss. Evidence: Somaliland page: 'In October 2007, Somaliland troops took control of the town' (holder not named; 'Puntland officials vowed to recapture Las Anod' in 2009); puntland.json has only a 2007/10 contest_end and its keyframes leave Sool out. Fix: Agree one reading with puntland.json: if Puntland held Las Anod before 2007, take the Laascaanood circle out of keyframe 0 for those years and add the 2007 loss in puntland.json; otherwise change L3 to a gain from 'nobody' or drop it (the contest_end already marks the end of the dispute).
- THIN `/ledger/4`: Month of the 2023 retreat from Las Anod (Goojacade, August 2023) (try https://en.wikipedia.org/wiki/Las_Anod_conflict_(2023%E2%80%93present))

## sahrawi-arab-democratic-republic: fix

Area: infobox 266,000 km2 (2024), keyframe about 220,000 km2, ratio 0.83. Claim 266,000 km2 vs resolved about 220,000; controlled 90,000 vs W. Sahara 84,000 (0.93). Acknowledged, but the cause is the missing Smara area (see fix).

Spot checks: /ledger/2 Sahrawi_Arab_Democratic_Republic: confirmed; /ledger/5 Western_Sahara_War: confirmed; /ledger/7 Western_Sahara_War: confirmed; /ledger/8 Western_Sahara_War: confirmed; /ledger/9 Sahrawi_Arab_Democratic_Republic: confirmed; /ledger/10 Western_Sahara_conflict: confirmed.

- TODO `/keyframe_review/0/correction`: The claim shape built from W. Sahara plus the Moroccan regions Laayoune-Boujdour-Sakia El Hamra and Oued el Dahab leaves out Es-Semara province (in the Guelmim - Es-Semara region), part of Saguia el-Hamra, and probably takes in the Tarfaya strip (Moroccan since 1958); the 0.83 ratio is put down to cell counting but is mostly this gap. Evidence: SADR infobox '266,000 km2 (claimed)'; gazetteer: W. Sahara 331 cells, Laayoune region 265, Oued el Dahab 273 (about 220,000 km2 at 253 km2 a cell); Natural Earth's 1997 Moroccan regions put Smara in Guelmim - Es-Semara. Fix: Ask for a gazetteer region 'Western Sahara' (the whole former Spanish Sahara) and use it for the keyframe and the occupation regions; until then say in the note that Smara is missing.
- TODO `/ledger/0-1`: The two 1976 occupation events have no month and so sort before the found event of 1976/2, occupying the republic's land before it exists. Evidence: SADR page: 'The SADR was proclaimed by the Polisario Front on 27 February 1976'; Western Sahara War page: 'On 26 February 1976, Spain officially announced its full withdrawal from the area.' Fix: Give both month 2 and place them after the found event.
- THIN `/ledger/1`: Date of the Moroccan-Mauritanian partition convention (April 1976) and Mauritania's actual zone (try https://en.wikipedia.org/wiki/Madrid_Accords)

## british-cameroons: fix

Area: infobox 89,526 km2 (1961), keyframe about 0 km2, ratio 0.0. The region 'British Cameroons' does not resolve (gazetteer lacks it); Nord-Ouest + Sud-Ouest alone resolve to about 48,000 km2.

Spot checks: /ledger/0 British_Cameroons: confirmed; /ledger/2 British_Cameroons: confirmed; /ledger/3 British_Cameroons: confirmed; /ledger/4 British_Cameroons: confirmed; /ledger/5 British_Cameroons: confirmed.

- TODO `/ledger (missing, 1922 and 1960)`: No mirror for colony-and-protectorate-of-nigeria's vassal_start 1922 and vassal_end 1960/10 with counterpart british-cameroons. Evidence: British Cameroons page: 'As French Cameroon gained independence, British Cameroons was still under the administration of Nigeria'; colony-and-protectorate-of-nigeria.json L4-L5. Fix: Add vassal_start 1922 and vassal_end 1960/10 with counterpart 'colony-and-protectorate-of-nigeria', region British Cameroons, confidence 2, source the British Cameroons page.
- THIN `/keyframe_review/0`: Separate extents of the Northern and Southern Cameroons and the 1916/1919 Anglo-French line (try https://en.wikipedia.org/wiki/Southern_Cameroons)

## tanganyika-territory: fix

Area: infobox 0 km2 (no year), keyframe about 0 km2, ratio 0.0. Page gives no area (stated); mainland Tanzania minus Zanzibar is about 0.94 M km2.

Spot checks: /ledger/0 Tanganyika_Territory: confirmed; /ledger/1 East_African_campaign_(World_War_I): confirmed; /ledger/2 Tanganyika_Territory: confirmed; /ledger/3 Tanganyika_Territory: confirmed; /ledger/4 Tanganyika_Territory: confirmed; /ledger/6 Tanganyika_Territory: confirmed.

- TODO `/ledger/0-1 (mirror)`: The 1916 found and 1917 gain from german-east-africa do not pair: german-east-africa records the same land as occupied by british-africa until 1919 and dissolves into this state only in June 1919. Evidence: german-east-africa.json L10, L11, L16-L18; Tanganyika Territory infobox 'Occupied territory of the United Kingdom (1916-1922)'. Fix: Resolve with the German East Africa fix (one occupation model for the batch).
- TODO `/ledger/3 (mirror)`: The 1921 Kigoma gain from belgian-congo pairs with an occupation_end in belgian-congo.json (L6, counterpart german-africa), not a loss to this state. Evidence: Tanganyika Territory page: 'On 22 March 1921 Belgium ceded the Kigoma District to Tanganyika'; belgian-congo.json L6. Fix: No change here; route to the belgian-congo owner (record the 1921 hand-over as a loss to tanganyika-territory).

## tripolitanian-republic: fix

Area: infobox 0 km2 (no year), keyframe about 0 km2, ratio 0.0. Page gives no area; seven Tripolitanian districts as drawn.

Spot checks: /ledger/0 Tripolitanian_Republic: confirmed; /ledger/2 Tripolitanian_Republic: not on page (quote only; fixed); /ledger/3 Tripolitanian_Republic: confirmed; /identity/capitals/0 Tripolitanian_Republic: confirmed.

- APPLIED `/ledger/2/note`: The note quoted 'Italian rule was restored four years later' than 1918; the sentence is not on the page. Evidence: Tripolitanian Republic page (searched for 'four years' and 'restored': neither occurs); it says 'Italy reasserted control over the colony in the early 1920s', infobox 'Disestablished: 1922'. Fix: Quote replaced with the page's sentence (event confidence 2, otherwise supported).

## puntland: fix

Area: infobox 212,510 km2 (2024), keyframe about 198,000 km2, ratio 0.93. Bari + Nugaal + Mudug resolve to about 198,000 km2; stated in keyframe 0.

Spot checks: /ledger/0 Puntland: confirmed; /ledger/1 Puntland: confirmed; /ledger/2 Somaliland: confirmed; /ledger/3 Puntland: confirmed.

- TODO `/ledger (missing, 2007/10)`: somaliland.json gains Las Anod from Puntland in October 2007 but this dossier records only a contest_end and never holds Sool. Evidence: somaliland.json L3; Somaliland page: 'In October 2007, Somaliland troops took control of the town' and Puntland officials 'vowed to recapture Las Anod'; Puntland page: disputes 'over the Sool, Sanaag and Ayn regions' since 1998. Fix: Agree with somaliland.json: if Puntland administered Las Anod before October 2007, add it (Laascaanood circle) to a keyframe for those years and a 2007/10 loss to somaliland from the Las Anod page; otherwise ask somaliland.json to drop the counterpart.
- TODO `/keyframe_review/0-1`: Whole Mudug is drawn Puntland's 1998-2024 although the page puts southern Mudug in Galmudug (from 2006). Evidence: Puntland page: 'In the south, according to the federal government of Somalia and CIA, the southern part of Mudug is part of Galmudug.' Fix: Split keyframes at 2006 and take southern Mudug out (or say in the note that the overshoot is kept for want of a named line).
- TODO `/identity/type`: Puntland is an autonomous federal member state of Somalia, not a breakaway: as a 'state' it is drawn over federal-republic-of-somalia, which has no 1998 event. Evidence: Puntland page infobox and text; federal-republic-of-somalia.json has no 1998 event. Fix: Consider modelling 1998-2024 as a vassal (autonomous region) of federal-republic-of-somalia and route a vassal_start 1998 to that dossier's owner; at least say so in notes.

## Cross-dossier matrix

| event | mirror | status | note |
|---|---|---|---|
| french-west-africa 1895 found french-africa | french-africa 1895 gain | exception | french-africa L34 records the federation's founding as its own gain; no split. Cliopatria continental aggregate: the counterpart's dossier hands the land to the aggregate row, not to this colony; overlap by design (author's problems list). |
| french-west-africa 1898 gain wassoulou-empire | wassoulou-empire 1898 dissolve | exception | Year agrees; mirror names french-africa. Cliopatria continental aggregate: the counterpart's dossier hands the land to the aggregate row, not to this colony; overlap by design (author's problems list). |
| french-west-africa 1901 gain mossi-kingdoms | mossi-kingdoms 1896 loss | mismatch | Five years apart: History of Burkina Faso says Ouagadougou captured 'in 1901' (confirmed); the mossi-kingdoms dossier ends in 1896 ('The French entered the area in 1896'). FWA's 1896-1901 contest covers the gap; route to the mossi-kingdoms owner to note the 1901 reading. |
| french-west-africa 1904 gain french-africa | dahomey 1894 dissolve | exception | Was counterpart 'dahomey' (kingdom ended 1894); reviewer set it to french-africa. Cliopatria continental aggregate: the counterpart's dossier hands the land to the aggregate row, not to this colony; overlap by design (author's problems list). |
| french-west-africa 1904 gain nobody |    | exception | Mauritania from nobody. |
| french-west-africa 1922 gain nobody |    | exception | Niger from nobody; the federation page has Niger a French Military Territory from 1904 (see fix). |
| french-west-africa 1934 vassal_start french-togoland |    | exception | No dossier; listed in the author's counterparts_needing_dossiers. |
| french-west-africa 1958 loss guinea | guinea 1958 found | mismatch | Year agrees; guinea's found names french-fifth-republic, not french-west-africa. |
| anglo-egyptian-sudan 1899 gain mahdist-state | mahdist-state 1899 loss | matched | mahdist-state 1899/11 loss to anglo-egyptian-sudan. |
| anglo-egyptian-sudan 1899 gain khedivate-of-egypt |    | exception | No dossier (groups me-10/af-01/af-02 not run). The Cliopatria row Khedivate of Egypt ends in 1884; its dossier must run to 1914 to carry the 1899 Suakin and 1902 Halaib losses. |
| anglo-egyptian-sudan 1902 gain khedivate-of-egypt |    | exception | As above (Halaib administrative line of 4 November 1902). |
| anglo-egyptian-sudan 1910 gain belgian-congo | belgian-congo 1910 loss | matched | Counterpart corrected from congo-free-state by the reviewer; belgian-congo L1 1910/6 names british-africa (aggregate) as the taker. |
| anglo-egyptian-sudan 1912 loss uganda-protectorate |    | exception | No dossier; listed (af-05). |
| anglo-egyptian-sudan 1914 loss uganda-protectorate |    | exception | No dossier; listed (af-05). |
| anglo-egyptian-sudan 1916 gain sultanate-of-darfur | sultanate-of-darfur 1916 dissolve | exception | Year agrees; mirror names british-africa. Cliopatria continental aggregate: the counterpart's dossier hands the land to the aggregate row, not to this colony; overlap by design (author's problems list). |
| anglo-egyptian-sudan 1934 loss italian-libya | italian-libya 1934 gain | matched | Sarra Triangle, 20 July 1934, both sides. |
| anglo-egyptian-sudan 1956 dissolve republic-of-sudan | republic-of-sudan 1956 found | matched | Mirror names british-africa. |
| french-equatorial-africa 1910 found french-africa | french-africa 1910  | exception | Cliopatria continental aggregate: the counterpart's dossier hands the land to the aggregate row, not to this colony; overlap by design (author's problems list). |
| french-equatorial-africa 1912 gain wadai-empire | wadai-empire 1912 dissolve | exception | Year agrees; mirror names french-africa. Cliopatria continental aggregate: the counterpart's dossier hands the land to the aggregate row, not to this colony; overlap by design (author's problems list). |
| french-equatorial-africa 1912 gain dar-al-kuti | dar-al-kuti 1912 dissolve | exception | Year agrees; mirror names french-africa. Cliopatria continental aggregate: the counterpart's dossier hands the land to the aggregate row, not to this colony; overlap by design (author's problems list). |
| french-equatorial-africa 1913 loss german-africa | german-africa 1911 gain | mismatch | Two years apart: german-africa L15 dates Neukamerun to the 4 November 1911 accord; the Neukamerun page says 'The transfer took two years, and was completed ... on June 1, 1913' (FEA's date). Route to german-africa's owner, or both cite the treaty and completion in notes. |
| french-equatorial-africa 1913 gain german-africa | german-africa 1911 loss | mismatch | Fort Lamy strip: german-africa L16 1911/11 vs FEA 1913/6; same cause. |
| french-equatorial-africa 1916 gain german-africa | german-africa 1916 loss | matched | Neukamerun back to France; mirror names french-africa. |
| italian-libya 1911 found ottoman-tripolitania | ottoman-tripolitania 1912 dissolve | exception | Mirror names italian-africa. Cliopatria continental aggregate: the counterpart's dossier hands the land to the aggregate row, not to this colony; overlap by design (author's problems list). |
| italian-libya 1912 gain ottoman-tripolitania | ottoman-tripolitania 1912 dissolve | exception | Treaty of Ouchy both sides; mirror names italian-africa. Cliopatria continental aggregate: the counterpart's dossier hands the land to the aggregate row, not to this colony; overlap by design (author's problems list). |
| italian-libya 1915 loss nobody |    | exception | Retreat to the coast; the Senussi (senussi-order, no dossier) drove the Italians out. |
| italian-libya 1923 gain tripolitanian-republic | tripolitanian-republic 1922 dissolve | matched | One year apart (infobox 1922 vs 'By 1923'). |
| italian-libya 1932 gain senussi-order |    | exception | No dossier; listed. |
| italian-libya 1934 gain anglo-egyptian-sudan | anglo-egyptian-sudan 1934 loss | matched | Sarra Triangle. |
| italian-libya 1943 loss free-french |    | exception | free-french (eu-21) not written; italian-africa L64 has the Fezzan lost 1943/1 to french-africa. |
| italian-libya 1943 loss british-africa | british-africa 1943 occupation_start | mismatch | Year agrees; british-africa records an occupation of italian-africa land (BMA), this dossier a loss. |
| northern-nigeria-protectorate 1900 found royal-niger-company | royal-niger-company 1900 loss | matched | 1900/1 both sides. |
| northern-nigeria-protectorate 1902 gain bornu-empire |    | exception | No dossier (af-03 Bornu not written). The Cliopatria row ends in 1894 and state-of-rabih-az-zubayr ends 1901/8: the Bornu dossier must carry the restored Shehu state to 1902, or this counterpart changes. |
| northern-nigeria-protectorate 1903 gain sokoto-caliphate | sokoto-caliphate 1903 dissolve | exception | Year agrees; mirror names british-africa. Cliopatria continental aggregate: the counterpart's dossier hands the land to the aggregate row, not to this colony; overlap by design (author's problems list). |
| northern-nigeria-protectorate 1914 dissolve colony-and-protectorate-of-nigeria | colony-and-protectorate-of-nigeria 1914 found | matched |  |
| colony-and-protectorate-of-nigeria 1914 merge niger-coast-protectorate | niger-coast-protectorate 1914 dissolve | matched | 1914/1 both sides. |
| colony-and-protectorate-of-nigeria 1916 occupation_start german-africa | german-africa 1916 occupation_start | matched | german-africa L35 1916/3 names british-africa as occupier. |
| colony-and-protectorate-of-nigeria 1922 occupation_end german-africa | german-africa 1919 occupation_end | mismatch | Three years apart: german-africa ends the occupation and loses the land in June 1919; Nigeria holds the occupation to the 1922 mandate. |
| colony-and-protectorate-of-nigeria 1922 vassal_start british-cameroons | british-cameroons   | missing | british-cameroons has no vassal_start (fix there). |
| colony-and-protectorate-of-nigeria 1960 vassal_end british-cameroons | british-cameroons   | missing | british-cameroons has no vassal_end (fix there). |
| colony-and-protectorate-of-nigeria 1960 dissolve federal-republic-of-nigeria | federal-republic-of-nigeria 1960 found | mismatch | Year agrees; federal-republic-of-nigeria's found names british-gold-coast (wrong slug in that dossier). |
| german-east-africa 1890 gain nobody |    | exception | Heligoland-Zanzibar Treaty; the Sultan's coastal strip is not separated (see fix). |
| german-east-africa 1894 gain portuguese-mozambique | portuguese-mozambique   | missing | portuguese-mozambique has no 1894 loss of the Kionga Triangle (its 1919 gain back exists). |
| german-east-africa 1897 gain kingdom-of-rwanda | kingdom-of-rwanda 1897 dissolve | exception | Year agrees; mirror names german-africa. Cliopatria continental aggregate: the counterpart's dossier hands the land to the aggregate row, not to this colony; overlap by design (author's problems list). |
| german-east-africa 1897 gain kingdom-of-burundi | kingdom-of-burundi 1903 dissolve | mismatch | Six years apart; GEA's 1897 is confidence 1 (page silent), kingdom-of-burundi dates the treaty of Kiganda 1903. |
| german-east-africa 1916 occupation_start belgian-congo | ruanda-urundi 1916 found | mismatch | Within the batch ruanda-urundi is founded on this land in 1916 (found/gain); belgian-congo L4 (1916/5) records the occupation as its own, with counterpart german-africa. One model needed. |
| german-east-africa 1916 occupation_start british-africa | tanganyika-territory 1916 found | mismatch | tanganyika-territory is founded on the Central Railway lands in 1916; GEA names british-africa as occupier. |
| german-east-africa 1917 occupation_start british-africa | tanganyika-territory 1917 gain | mismatch | Type and counterpart differ (occupation by british-africa vs gain by tanganyika-territory). |
| german-east-africa 1919 loss ruanda-urundi | ruanda-urundi 1919 rename | mismatch | ruanda-urundi has only a rename in 1919 (it already gained the land in 1916). |
| german-east-africa 1919 dissolve tanganyika-territory | tanganyika-territory 1916 found | mismatch | Successor founded three years before the dissolve. |
| ruanda-urundi 1916 found german-east-africa | german-east-africa 1916 occupation_start | mismatch | GEA names belgian-congo as occupier; see GEA fix. |
| ruanda-urundi 1916 gain german-east-africa | german-east-africa 1916 occupation_start | mismatch | Urundi, June 1916; GEA records an occupation by belgian-congo. |
| ruanda-urundi 1962 dissolve republic-of-rwanda | republic-of-rwanda 1962 found | matched | Mirror names belgian-congo. |
| somaliland 1991 found federal-republic-of-somalia | federal-republic-of-somalia 1991 loss | matched | 1991/5 both sides. |
| somaliland 2007 gain puntland | puntland 2007 contest_end | missing | puntland has no loss of Las Anod (fixes on both). |
| somaliland 2023 loss ssc-khatumo |    | exception | No dossier; listed. |
| sahrawi-arab-democratic-republic 1976 occupation_start morocco | morocco 1976 occupation_start | matched | morocco L25. |
| sahrawi-arab-democratic-republic 1976 occupation_start mauritania | mauritania 1976 gain | mismatch | mauritania records an annexation from francoist-spain, not an occupation of SADR land. |
| sahrawi-arab-democratic-republic 1979 occupation_end mauritania | mauritania 1979 loss | mismatch | mauritania records a loss to morocco. |
| sahrawi-arab-democratic-republic 1979 occupation_start morocco | morocco   | missing | morocco has no 1979 event for Tiris al-Gharbiya (annexed 11 August 1979). |
| sahrawi-arab-democratic-republic 1976 found kingdom-of-spain |    | exception | Spain's dossiers (eu groups) not written; morocco and mauritania name francoist-spain. |
| british-cameroons 1916 found german-africa | german-africa 1916 occupation_start | matched | german-africa L35 1916/3 (British zone held, occupier british-africa). |
| british-cameroons 1961 loss federal-republic-of-nigeria | federal-republic-of-nigeria 1961 gain | mismatch | Year agrees; federal-republic-of-nigeria's gain names british-gold-coast (wrong slug there). |
| british-cameroons 1961 loss republic-of-cameroon | republic-of-cameroon 1961 gain | mismatch | Year agrees; republic-of-cameroon's gain names british-gold-coast (wrong slug there). |
| tanganyika-territory 1916 found german-east-africa | german-east-africa 1916 occupation_start | mismatch | See GEA fix. |
| tanganyika-territory 1917 gain german-east-africa | german-east-africa 1917 occupation_start | mismatch | See GEA fix. |
| tanganyika-territory 1921 gain belgian-congo | belgian-congo 1921 occupation_end | mismatch | belgian-congo L6 ends an occupation of german-africa land rather than recording a loss to tanganyika-territory. |
| tanganyika-territory 1961 dissolve tanzania |    | exception | tanzania (Cliopatria row, af-08 part) not written yet. |
| tripolitanian-republic 1918 found italian-libya | italian-libya 1918 contest_start | matched |  |
| tripolitanian-republic 1922 dissolve italian-libya | italian-libya 1923 gain | matched | One year apart. |
| puntland 1998 found federal-republic-of-somalia | federal-republic-of-somalia   | missing | federal-republic-of-somalia has no 1998 event (loss or vassal) for Puntland. |
| puntland 2009 gain maakhir |    | exception | No dossier; listed. |

## Gazetteer names needed

- Halaib Triangle (region): anglo-egyptian-sudan
- Lado Enclave (region): anglo-egyptian-sudan
- Sarra Triangle (region): anglo-egyptian-sudan, italian-libya
- Suakin (place): anglo-egyptian-sudan
- Neukamerun (region): french-equatorial-africa
- Dar al-Kuti (region): french-equatorial-africa
- British Cameroons (region): colony-and-protectorate-of-nigeria, british-cameroons
- Northern Cameroons (region): british-cameroons
- Kionga Triangle (region): german-east-africa
- Maakhir (region): puntland
- Western Sahara (region): sahrawi-arab-democratic-republic (whole former Spanish Sahara, 266,000 km2, incl. Es-Semara; W. Sahara in Natural Earth is only the Free Zone)
- Zungeru (place): northern-nigeria-protectorate (capital 1902-1913)
- Al Jaghbub (place): italian-libya (for the missing 1925 event)

## Counterparts needing dossiers

- French Togoland: `french-togoland` 1916-1960
- Senussi Order: `senussi-order` 1880-1932
- Uganda Protectorate: `uganda-protectorate` 1894-1962
- Maakhir: `maakhir` 2007-2009
- SSC-Khatumo: `ssc-khatumo` 2023-2024
- Khedivate of Egypt (row ends 1884; dossier must run to 1914): `khedivate-of-egypt` 1867-1914
- Vichy France (if the FEA Gabon contest is re-pointed): `vichy-france` 1940-1944

## Problems

- No page failed to load. WebFetch summarises; the Tripolitanian Republic page was searched twice for the quoted 'four years later' sentence and it is not there.
- Every dossier validated with no errors before and after the reviewer's edits (python3 -I history/tools/validate_dossier.py --resolve); remaining warnings are unknown counterpart slugs and gazetteer names, all listed.
- None of the 14 dossiers has a Cliopatria shape, so cliopatria_km2 is 0 throughout; area_check compares the infobox with the keyframe resolved from gazetteer cells (about 253 km2 a cell), given as keyframe_km2.
- Context neighbours with a dossier (12 of 40): ashanti-empire, beylik-of-tunis, british-cape-colony, dutch-gold-coast, ethiopia, ethiopian-empire, free-orange-state, mahdist-state, morocco, natalia-republic, ottoman-tripolitania, regency-of-algiers; the other 28 belong to groups not run yet. The cross-checks also used the counterparts' own dossiers where they exist (french-africa, italian-africa, british-africa, german-africa, belgian-congo, congo-free-state, dahomey, mossi-kingdoms, wassoulou-empire, wadai-empire, dar-al-kuti, sultanate-of-darfur, sokoto-caliphate, royal-niger-company, niger-coast-protectorate, kingdom-of-rwanda, kingdom-of-burundi, portuguese-mozambique, federal-republic-of-nigeria, republic-of-cameroon, federal-republic-of-somalia, mauritania, guinea).
- Wrong counterpart slugs found in other groups' dossiers: federal-republic-of-nigeria L0-L1 and republic-of-cameroon L1 name 'british-gold-coast' for the Nigerian and Cameroons hand-overs of 1960-1961.
- The three-way model of the 1916-1922 occupations of German East Africa (german-east-africa: occupied by belgian-congo/british-africa; ruanda-urundi and tanganyika-territory: founded 1916; belgian-congo: occupation then 1922 gain) needs one decision by the orchestrator before the authors fix it.
- Verdict scheme used here: 'fix' = accepted; findings with applied true were made by the reviewer and validated, findings with applied false are non-blocking author fixes (blocking false). No dossier has an unapplied blocking finding, so none is 'fail'.
