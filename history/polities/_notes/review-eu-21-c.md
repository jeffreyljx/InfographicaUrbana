# Review of batch eu-21-c (adversarial reviewer, 2026-10-31)

Inputs: the six dossiers, the author's report and notes, neighbour dossiers that exist (kingdom-of-great-britain, united-kingdom, kingdom-of-denmark-1814-1940, denmark, kingdom-of-italy, netherlands, albania, principality-of-monaco, french-africa, the Soviet SSR dossiers, portuguese-republic, portuguese-angola/-mozambique/-india/-timor, republic-of-india, republic-of-indonesia, east-timor, people-s-republic-of-china, people-s-republic-of-angola, mozambique, republic-of-cabo-verde, sao-tome-and-principe, republic-of-guinea-bissau, kingdom-of-spain, empire-of-japan, united-states-of-america). The other eu-21 parts, eu-20 and eu-17 have not written their dossiers yet: their events are listed as exceptions.

Validator: 0 errors for all six before and after the reviewer's edits; warnings are only counterpart slugs that need dossiers.

## nazi-germany: fail

Area: infobox 633786 km2 (1939), Cliopatria 699301 km2, ratio 1.1, acknowledged True. 1940: infobox 823,505 vs shape 1,637,988 (1.99), acknowledged and corrected in /keyframe_review/4.

Findings:
- `/keyframe_review/8/correction and /keyframe_review/9/correction` (for the author): The 1944 and 1945 corrections are identical and still hold Alsace-Lorraine, Eupen-Malmedy, Luxembourg and the Bialystok district (Podlachian), lost between July and November 1944, and the annexed Polish lands lost January-March 1945. Evidence: The two corrections compare equal (only text differs); the union includes {region: Alsace}+Metz, the Eupen disc, country=Luxembourg and admin1=Podlachian. The ledger itself removes Luxembourg only in 1945/2 (/ledger/51). Fix: Make the 1945 keyframe the Reich at 1 January 1945 (drop Alsace-Lorraine, Eupen-Malmedy, Bialystok; keep Luxembourg until February if the page says so) and add the dated losses below.
- `/ledger (after /ledger/48)` (for the author): No loss events for the annexed lands: Eupen-Malmedy (1944/9), Bialystok district (1944/7), Alsace-Lorraine (1944/11), Memel (1945/1), Wartheland, Danzig-West Prussia, Ciechanow and Katowice districts and Danzig (1945/1-3), Lower Styria and the Sudetenland (1945/5). They were gained at /ledger/3, 6, 8, 9, 12, 13, 24, 26 and simply vanish at the dissolve. Evidence: /ledger/65 dissolve region is union(Germany, Austria) while its text says 'plus the Sudetenland'; the 1945 contest (/ledger/49, 63) covers only Nazi Germany 1938 cut to Poland and Russia, i.e. pre-1938 eastern Germany, not the 1939 annexations. Fix: Add a loss (or contest_start/contest_end + loss) for each annexed land with its month and the counterpart that took it back (french-third-republic/provisional French government, kingdom-of-belgium, second-polish-republic or the Polish successor, union-of-soviet-socialist-republics, yugoslavia, czechoslovakia); make the dissolve region match its text.
- `/ledger (1943-1944)` (for the author): Occupations of Albania (8 Sep 1943 - 29 Nov 1944) and Monaco (8 Sep 1943 - 3 Sep 1944) are missing, though both dates are in the occupation table of a page the author cited. Evidence: German-occupied Europe table: 'Albania: 8 Sep 1943 - 29 Nov 1944', 'Monaco: 8 Sep 1943 - 3 Sep 1944'; albania /ledger/19 and /ledger/21 and principality-of-monaco /ledger/20 and /ledger/21 already mirror them with counterpart nazi-germany. Fix: Add occupation_start/occupation_end pairs: albania 1943/9-1944/11, principality-of-monaco 1943/9-1944/9 (confidence 3, source German-occupied Europe).
- `/ledger (1940-1945)` (for the author): Channel Islands (30 Jun / 1 Jul 1940 - 9 May 1945) and Tunisia (Nov 1942 - May 1943) are noted but not recorded; the Tunisian cells were removed from the 1943 shape with no event. Evidence: German-occupied Europe table gives the Channel Islands dates; french-africa /ledger/75 and /ledger/80 record occupation_start 1942/11 and occupation_end 1943/5 by nazi-germany. Fix: Add occupation pairs: united-kingdom (Guernsey, Jersey) 1940/6-1945/5; french-africa (Tunisia) 1942/11-1943/5.
- `/ledger/38` (for the author): Occupation of the Vichy free zone dated 1943 (confidence 1), from the growth of Cliopatria's shape; the occupation (Case Anton) began 11 November 1942. Evidence: The German-occupied Europe page has no date for it (WebFetch: 'not on page'); french-africa dates the parallel Tunisian occupation 1942/11. Fix: Open Case Anton and redate to 1942/11 (and keep the 1944/8 end).
- `/ledger/0 and weimar-republic /ledger/18` (for the author): Two months of overlap: nazi-germany is founded 1933/1 while weimar-republic dissolves 1933/3 into it. Evidence: Nazi Germany infobox: 'Seizure of power: 30 January 1933', 'Enabling Act: 23 March 1933'; Weimar Republic lead: 'from 9 November 1918 to 23 March 1933'. Fix: Found nazi-germany at 1933/3 (Enabling Act), or end Weimar at 1933/1; the two dossiers must agree.
- `/ledger/4 and /ledger/58` (for the author): Occupation counterpart is the Protectorate itself, a German creation, not the state whose land was occupied. Evidence: German occupation of Czechoslovakia: rump Czecho-Slovakia was occupied 15 March 1939 and the Protectorate proclaimed on 16 March. Fix: Use counterpart czechoslovakia (or record vassal_start protectorate-of-bohemia-and-moravia instead of an occupation).
- `/ledger/14 and /ledger/53` (for the author): Counterpart 'denmark' is a dossier that starts 1945/5; the 1814-1940 Danish dossier (kingdom-of-denmark-1814-1940) dissolves 1940/4 into nazi-germany. Evidence: kingdom-of-denmark-1814-1940 /ledger/12 dissolve 1940/4 counterpart nazi-germany, yet its note says 'The Danish state went on under occupation'. Fix: Keep the occupation reading; orchestrator to have eu-14 extend the Danish dossier to 1945 (or start 'denmark' in 1940) and then point these events at it.
- `/ledger/24, 30-34, 39, 42, 43, 62` (for the author): Soviet counterpart is union-of-soviet-socialist-republics (no dossier) while the SSR dossiers already mirror these occupations with counterpart nazi-germany; the Baltic end is lumped at 1945/5 although Estonia and Lithuania were retaken in 1944. Evidence: estonian-ssr /ledger/2 (1944), lithuanian-ssr /ledger/2 (1944/10), latvian-ssr /ledger/3 (1945), ukrainian-ssr /ledger/45 (1944/10), byelorussian-ssr /ledger/16 (1944), RSFSR /ledger/46-56. Fix: Split the occupations by SSR (estonian-, latvian-, lithuanian-, byelorussian-, ukrainian-soviet-socialist-republic, russian-soviet-federative-socialist-republic) with their own end years.
- `/ledger/41` (for the author): Italy 1943/9: Germany records an occupation of northern Italy; kingdom-of-italy records a loss to nazi-germany of Dalmatia and the Ljubljana Province (/ledger/38) and of the north to italian-social-republic (/ledger/39). Evidence: kingdom-of-italy ledger 38-39. Fix: Add the Operational Zones (Adriatic Coast, Alpine Foothills) as occupation or gain from kingdom-of-italy, and decide with eu-21-x whether the north is an RSI vassal or an occupation.

Gaps for a gap-filler:
- `/ledger/10, 11`: General Government creation and end of the Polish campaign at confidence 1 (https://en.wikipedia.org/wiki/General_Government)
- `/ledger/13`: Eupen-Malmedy annexation 18 May 1940 at confidence 1 (https://en.wikipedia.org/wiki/Eupen-Malmedy)
- `/ledger/27, 56`: Croatia client status at confidence 1 (https://en.wikipedia.org/wiki/Independent_State_of_Croatia)
- `/ledger/45, 46`: Liberation of France dated 1944/8 at confidence 1 (https://en.wikipedia.org/wiki/Liberation_of_France)
- `/ledger/48`: End of the General Government occupation 1945/1 at confidence 1 (https://en.wikipedia.org/wiki/Vistula–Oder_offensive)
- `/keyframe_review/5-7`: Libyan and Tunisian cells removed without a page (https://en.wikipedia.org/wiki/North_African_campaign)

Spot checks: /ledger/3 confirmed (Territorial_evolution_of_Germany); /ledger/37 confirmed (Territorial_evolution_of_Germany); /ledger/49 confirmed (German-occupied_Europe); /ledger/52 confirmed (German-occupied_Europe); /ledger/44 confirmed (German-occupied_Europe); /ledger/2 confirmed (Nazi_Germany); /ledger/38 not on page (German-occupied_Europe)

## weimar-republic: fix

Area: infobox 468787 km2 (1925), Cliopatria 456893 km2, ratio 0.97, acknowledged True. 

Findings:
- `/keyframe_review/0/correction` (applied by reviewer): The 1918 keyframe left out the Allied-occupied Rhineland (Cliopatria's 1920 shape omits it), so the Rhineland appeared in the 1920 keyframe with no event. Evidence: Occupation of the Rhineland: occupied from 1 December 1918, sovereignty stayed German; the author's own 1920 correction adds 'Weimar 1932 minus the Saar'. Fix: Added {minus: [Weimar Republic 1932, Saarland]} to the union and to text.
- `/ledger/0/region` (applied by reviewer): The found region (1920 shape + Alsace-Lorraine) lacked the Rhineland and the treaty lands (Posen, West Prussia, Danzig, Memel, the Saar, Eupen-Malmedy, Hultschin) that /ledger/5-11 later remove. Evidence: Losses of land the found region never held. Fix: Set the region equal to the corrected 1918 keyframe.
- `/ledger/2, /ledger/16` (applied by reviewer): Counterpart kingdom-of-great-britain ends in 1800. Evidence: united-kingdom /ledger/15 (1918/12) and /ledger/21 (1926/1) mirror the Cologne zone. Fix: Changed to united-kingdom.
- `/ledger/5` (applied by reviewer): Counterpart 'denmark' is a dossier starting 1945. Evidence: kingdom-of-denmark-1814-1940 /ledger/11 gains Northern Schleswig 1920/7 from weimar-republic. Fix: Changed to kingdom-of-denmark-1814-1940.

Gaps for a gap-filler:
- `/ledger/3, /ledger/17`: The Koblenz zone was American until January 1923 and evacuated in November 1929, and Belgium held a zone at Aachen 1918-1929; all are carried as one French occupation to 30 June 1930 (the note admits it) (https://en.wikipedia.org/wiki/Occupation_of_the_Rhineland)
- `/wars/1`: Greater Poland Uprising has a zone but no contest event; Posen was de facto Polish from early 1919 (https://en.wikipedia.org/wiki/Greater_Poland_uprising_(1918–1919))
- `/ledger/5-9`: Transfer months for Northern Schleswig, Posen, West Prussia, Danzig, Memel, the Saar (confidence 2, treaty date) (https://en.wikipedia.org/wiki/Schleswig_plebiscites)

Spot checks: /ledger/1 confirmed (Territorial_evolution_of_Germany); /ledger/10 confirmed (Treaty_of_Versailles); /ledger/11 confirmed (Treaty_of_Versailles); /ledger/14 confirmed (Occupation_of_the_Rhineland); /ledger/16 confirmed (Occupation_of_the_Rhineland); /ledger/17 confirmed (Occupation_of_the_Rhineland)

## estado-novo: fix

Area: infobox 92212 km2 (no year), Cliopatria 2201913 km2, ratio 23.88, acknowledged True. Infobox gives the metropole only, no year; the shape is the metropole plus the colonies; acknowledged in /keyframe_review/0 and used for the 1976+ keyframes.

Findings:
- `/keyframe_review/8` (applied by reviewer): 1958 shape marked ok though it still holds Dadra and Nagar Haveli, lost in 1954 (/ledger/5). Evidence: Annexation of Goa: 'Between 22 July and 2 August 1954, armed activists attacked and forced the surrender of Portuguese forces stationed in Dadra and Nagar Haveli'; Nagar Haveli surrendered 11 August 1954. Fix: Verdict adjust; correction minus(Estado Novo 1958, the ledger's Dadra disc).
- `/keyframe_review/9/correction` (applied by reviewer): The 1960 correction removed Goa, Daman and Diu for the whole shape, though they were Portuguese until 17-19 December 1961; nothing in 1958-1960 explained their loss. Evidence: Annexation of Goa infobox '17-19 December 1961'; /ledger/9 already carries the loss. Fix: Correction now removes only Dadra and Nagar Haveli.
- `/keyframe_review/14/correction` (applied by reviewer): The 1979-2023 correction was Portugal alone though Macau was Portuguese until 20 December 1999; it relied on an overlapping new keyframe. Evidence: Handover of Macau: 'The colony remained under de jure Portuguese rule until 20 December 1999'. Fix: Correction union(Portugal, Macao); /ledger/19 removes Macau.
- `/ledger/14` (applied by reviewer): Counterpart 'cape-verde' has no dossier; republic-of-cabo-verde exists and founds itself from estado-novo in 1975/7. Evidence: republic-of-cabo-verde /ledger/0. Fix: Changed to republic-of-cabo-verde.
- `/wars/2/belligerents` (applied by reviewer): Belligerent kingdom-of-great-britain ends in 1800. Evidence: kingdom-of-great-britain dossier 1707-1800. Fix: Changed to united-kingdom.

Gaps for a gap-filler:
- `/ledger/16-18`: East Timor: east-timor founds itself 1975/11 from estado-novo and Indonesia's contest and gain are with east-timor; this dossier keeps Timor to 1976/7 and contests it with Indonesia. Decide one reading (loss to east-timor 1975/11 is what both neighbours expect) (https://en.wikipedia.org/wiki/Portuguese_Timor)
- `/ledger/11`: No contest for Portuguese Guinea 1963-1974 (PAIGC held 'a large area of the rural countryside'); republic-of-guinea-bissau has contest_start 1973/9 and contest_end 1974/9 with estado-novo (https://en.wikipedia.org/wiki/Guinea-Bissau_War_of_Independence)
- `/ledger/5`: Dadra and Nagar Haveli went to Free Dadra and Nagar Haveli (India's gain is 1961 from it; portuguese-india names the United Front of Goans and Azad Gomantak Dal), not directly to India; Dadra fell in July (https://en.wikipedia.org/wiki/Dadra_and_Nagar_Haveli)
- `/ledger/12-15`: Independence months: Mozambique 25 June, Cape Verde 5 July, Sao Tome 12 July, Angola 11 November 1975 (neighbour dossiers carry them) (https://en.wikipedia.org/wiki/Decolonisation_of_Portuguese_Africa)
- `whole dossier`: The colonies are drawn as Portuguese land while colony dossiers portuguese-angola, portuguese-mozambique, portuguese-india and portuguese-timor (type colony) hold the same land to 1961/1975; neighbours found from those colony dossiers. Orchestrator decision needed (vassal relation or one layer) (https://en.wikipedia.org/wiki/Portuguese_Empire)

Spot checks: /ledger/5 confirmed (Annexation_of_Goa); /ledger/9 confirmed (Annexation_of_Goa); /ledger/11 confirmed (Portuguese_Colonial_War); /ledger/12 confirmed (Estado_Novo_(Portugal)); /ledger/19 confirmed (Handover_of_Macau); /ledger/6 confirmed (Estado_Novo_(Portugal))

## republic-of-latvia: fix

Area: infobox 64589 km2 (2024), Cliopatria 67931 km2, ratio 1.05, acknowledged True. 

Findings:
- `/ledger/8, /ledger/9` (applied by reviewer): Annexation counterpart union-of-soviet-socialist-republics has no dossier, while latvian-soviet-socialist-republic exists and founds itself 1940/7 from republic-of-latvia and dissolves 1991/8. Evidence: Latvia page: 'The Soviet Union incorporated Latvia on 5 August 1940, as the Latvian Soviet Socialist Republic'; 'Restored: 21 August 1991'. Fix: Changed both counterparts to latvian-soviet-socialist-republic (the 1940 occupation pair stays with the USSR).

Gaps for a gap-filler:
- `/keyframe_review/2`: Five border cells in the 1936-1938 shape and the Valka arbitration of 1920 not explained (https://en.wikipedia.org/wiki/Valka)

Spot checks: /ledger/1 confirmed (Latvian_War_of_Independence); /ledger/2 confirmed (Latvian_War_of_Independence); /ledger/4 confirmed (Latvian_War_of_Independence); /ledger/5 confirmed (Latvian_War_of_Independence); /ledger/8 confirmed (Latvia); /ledger/9 confirmed (Latvia)

## second-spanish-republic: thin

Area: infobox 0 km2 (no year), Cliopatria 854092 km2, ratio 0.0, acknowledged True. No area in the infobox (confirmed).

Findings:
- `/ledger/2/confidence` (applied by reviewer): Confidence 3 for the whole Balearic Islands, which the page does not name; Menorca stayed Republican and the 1936 keyframe keeps its cells. Evidence: Spanish Civil War: 'Goded and Franco immediately took control of the islands to which they were assigned'; Menorca not on the page. Fix: Lowered to 2.

Gaps for a gap-filler:
- `/keyframe_review/2, /keyframe_review/3`: Cliopatria's 1936 and 1938 shapes keep Spanish Sahara, Ifni and Spanish Guinea (about 300,000 km2) for the Republic; they sided with the Nationalists from July-September 1936. Flagged by the author, page budget (https://en.wikipedia.org/wiki/Spanish_Guinea)
- `/ledger/2`: Menorca stayed Republican until February 1939; the 1936/7 loss should exclude it and a 1939/2 loss add it (https://en.wikipedia.org/wiki/Menorca)
- `/ledger/9`: 1938 Aragon loss at confidence 1, from the shape difference (https://en.wikipedia.org/wiki/Aragon_Offensive)
- `/ledger/5-7`: Northern campaign months (Bilbao June, Santander August, Asturias October 1937) (https://en.wikipedia.org/wiki/War_in_the_North)
- `/ledger/13`: The 1939/3 loss and the 1939/4 dissolve carry the same region twice; keep one (https://en.wikipedia.org/wiki/Final_offensive_of_the_Spanish_Civil_War)

Spot checks: /ledger/1 confirmed (Spanish_Civil_War); /ledger/2 not on page (Spanish_Civil_War); /ledger/4 confirmed (Second_Spanish_Republic); /ledger/8 confirmed (Second_Spanish_Republic); /ledger/14 confirmed (Second_Spanish_Republic)

## irish-free-state: fix

Area: infobox 70000 km2 (no year), Cliopatria 74990 km2, ratio 1.07, acknowledged True. 

Findings:
- `/identity/predecessors/0/slug, /ledger/0/counterpart` (applied by reviewer): Predecessor and found counterpart kingdom-of-great-britain ends in 1800. Evidence: united-kingdom /ledger/19 loses the Free State 1922/12. Fix: Changed both to united-kingdom.

Gaps for a gap-filler:
- `/wars`: The Irish Civil War is on the Irish Free State page (June 1922 - April 1923) but not recorded; a war entry with empty zones (no land changed hands after 6 December 1922) would close it; Treaty Ports occupation not recorded (https://en.wikipedia.org/wiki/Irish_Civil_War)

Spot checks: /ledger/0 confirmed (Irish_Free_State); /ledger/1 confirmed (Irish_Free_State)

## Cross-dossier matrix

| event | mirror | status | note |
|---|---|---|---|
| nazi-germany 1935 gain saar-basin-territory |    | exception | no dossier; in author's counterparts_needing_dossiers (eu-21-x) |
| nazi-germany 1938 gain republic-of-austria |    | exception | eu-21 part not run yet |
| nazi-germany 1938 gain czechoslovakia |    | exception | eu-21 part not run yet |
| nazi-germany 1939 occupation_start protectorate-of-bohemia-and-moravia |    | exception | needs dossier (eu-21-x); counterpart should be czechoslovakia |
| nazi-germany 1939 vassal_start slovak-republic |    | exception | needs dossier (eu-21-x) |
| nazi-germany 1939 gain kingdom-of-lithuania |    | exception | eu-21 part not run yet |
| nazi-germany 1939 gain free-city-of-danzig |    | exception | eu-20 not run yet |
| nazi-germany 1939 gain second-polish-republic |    | exception | eu-21 part not run yet (also contest and occupation) |
| nazi-germany 1940 gain french-third-republic |    | exception | eu-20 not run yet; Alsace-Lorraine |
| nazi-germany 1940 gain kingdom-of-belgium |    | exception | eu-20 not run yet; Eupen-Malmedy, also 1940/5 occupation |
| nazi-germany 1940 occupation_start denmark | kingdom-of-denmark-1814-1940 1940 dissolve | mismatch | the Danish dossier dissolves into nazi-germany 1940/4; 'denmark' starts 1945/5; nothing covers Denmark 1940-1945 as a state |
| nazi-germany 1940 occupation_start netherlands | netherlands 1940 occupation_start | matched | end 1945/5 matched (netherlands /ledger/18) |
| nazi-germany 1940 occupation_start luxembourg |    | exception | eu-20 not run yet (also 1942 gain, 1945 loss) |
| nazi-germany 1940 occupation_start kingdom-of-norway |    | exception | no dossier yet |
| nazi-germany 1940 occupation_start vichy-france |    | exception | eu-21 part not run yet; June 1940 land was the Third Republic's |
| nazi-germany 1941 occupation_start union-of-soviet-socialist-republics | lithuanian-soviet-socialist-republic 1941 occupation_start | mismatch | SSR dossiers (byelorussian, estonian, latvian, lithuanian, ukrainian, RSFSR) mirror with counterpart nazi-germany; nazi-germany names the USSR (eu-17 not run); end years differ by months (Baltic 1945/5 vs 1944, Ukraine 1944/1 vs 1944/10) |
| nazi-germany 1941 occupation_start kingdom-of-greece | kingdom-of-greece   | missing | kingdom-of-greece dossier starts 1945; no Greek state dossier covers 1941 |
| nazi-germany 1941 occupation_start yugoslavia |    | exception | eu-21 part not run yet (also Slovenia gain, Croatia vassal) |
| nazi-germany 1943 occupation_start kingdom-of-italy | kingdom-of-italy 1943 loss | mismatch | Italy records a loss of Dalmatia and Ljubljana to nazi-germany and of the north to italian-social-republic; Germany records an occupation of the north |
| nazi-germany 1944 occupation_start hungarian-republic |    | exception | eu-21 part not run yet |
| nazi-germany 1945 contest_start united-states-of-america | united-states-of-america   | missing | USA has only 1945/6 occupation_start nazi-germany (after the dissolve) |
| albania 1943 occupation_start nazi-germany | nazi-germany   | missing | nazi-germany lacks the Albania occupation 1943/9-1944/11 |
| principality-of-monaco 1943 occupation_start nazi-germany | nazi-germany   | missing | nazi-germany lacks the Monaco occupation 1943/9-1944/9 |
| french-africa 1942 occupation_start nazi-germany | nazi-germany   | missing | nazi-germany lacks the Tunisia occupation 1942/11-1943/5 |
| weimar-republic 1918 loss french-third-republic |    | exception | eu-20 not run yet |
| weimar-republic 1918 occupation_start united-kingdom | united-kingdom 1918 occupation_start | matched | UK side names german-empire; should name weimar-republic. End 1926/1 matched |
| weimar-republic 1918 occupation_start french-third-republic |    | exception | eu-20 not run yet (also Ruhr 1923-1925) |
| weimar-republic 1920 loss kingdom-of-denmark-1814-1940 | kingdom-of-denmark-1814-1940 1920 gain | matched | after reviewer slug fix |
| weimar-republic 1920 loss second-polish-republic |    | exception | eu-21 part not run yet (also Upper Silesia 1922) |
| weimar-republic 1920 loss saar-basin-territory |    | exception | needs dossier |
| weimar-republic 1920 loss free-city-of-danzig |    | exception | eu-20 not run yet |
| weimar-republic 1920 loss memel-territory |    | exception | needs dossier |
| weimar-republic 1920 loss kingdom-of-belgium |    | exception | eu-20 not run yet |
| weimar-republic 1921 loss czechoslovakia |    | exception | eu-21 part not run yet |
| estado-novo 1926 found portuguese-republic | portuguese-republic 1926 dissolve | matched |  |
| estado-novo 1942 occupation_start empire-of-japan | empire-of-japan 1942 occupation_start | matched | end 1945 vs 1945/9 matched; portuguese-timor also records it |
| estado-novo 1954 loss republic-of-india | portuguese-india 1954 loss | mismatch | India gains Dadra in 1961 from Free Dadra and Nagar Haveli; portuguese-india loses it 1954/7-8 to the liberation groups |
| estado-novo 1961 loss republic-of-dahomey |    | exception | needs dossier (af-08) |
| estado-novo 1961 loss republic-of-india | republic-of-india 1961 gain | mismatch | India's gain names portuguese-india (colony dossier), not estado-novo |
| estado-novo 1974 loss republic-of-guinea-bissau | republic-of-guinea-bissau 1973 found | mismatch | Guinea-Bissau founds itself 1973/9 from estado-novo with a contest to 1974/9; estado-novo has no contest |
| estado-novo 1975 loss people-s-republic-of-angola | people-s-republic-of-angola 1975 found | mismatch | Angola founds itself from portuguese-angola |
| estado-novo 1975 loss mozambique | mozambique 1975 found | mismatch | Mozambique founds itself from portuguese-mozambique |
| estado-novo 1975 loss republic-of-cabo-verde | republic-of-cabo-verde 1975 found | matched | after reviewer slug fix |
| estado-novo 1975 loss sao-tome-and-principe | sao-tome-and-principe 1975 found | matched |  |
| estado-novo 1976 loss republic-of-indonesia | east-timor 1975 found | mismatch | east-timor founds itself 1975/11 from estado-novo; Indonesia's contest and gain are with east-timor |
| estado-novo 1999 loss people-s-republic-of-china | people-s-republic-of-china 1999 gain | matched | PRC side names 'portugal' |
| republic-of-latvia 1918 contest_start latvian-socialist-soviet-republic |    | exception | needs dossier (eu-21-x); also 1920/2 gain of Latgale |
| republic-of-latvia 1940 occupation_start union-of-soviet-socialist-republics |    | exception | eu-17 not run yet |
| republic-of-latvia 1940 loss latvian-soviet-socialist-republic | latvian-soviet-socialist-republic 1940 found | matched | after reviewer counterpart fix |
| republic-of-latvia 1991 gain latvian-soviet-socialist-republic | latvian-soviet-socialist-republic 1991 dissolve | matched | after reviewer counterpart fix |
| second-spanish-republic 1931 found kingdom-of-spain | kingdom-of-spain 1931 loss | matched |  |
| kingdom-of-spain 1931 vassal_end spanish-morocco | second-spanish-republic   | mismatch | kingdom-of-spain says Spanish Morocco and the Sahara pass to the Republic as vassals; the Republic holds them as its own land with no vassal_start |
| second-spanish-republic 1936 loss spanish-nationalists |    | exception | eu-21 part not run yet (all 1936-1939 losses; dissolve to francoist-spain) |
| irish-free-state 1922 found united-kingdom | united-kingdom 1922 loss | matched | after reviewer slug fix |
| irish-free-state 1937 dissolve eire |    | exception | eu-21 part not run yet |

## Problems

- WebFetch returns model-written extracts; quotes in this review are the extract's rendering.
- Greece 1941-1945 has no state dossier: kingdom-of-greece starts 1945; nazi-germany's occupation counterpart has nothing to mirror it.
- Denmark 1940-1945 has no state dossier: kingdom-of-denmark-1814-1940 dissolves 1940/4 into nazi-germany, and denmark starts 1945/5 (eu-14 owner).
- Colony layer: estado-novo (and second-spanish-republic) draw the colonies as their own land, while colony dossiers portuguese-angola, portuguese-mozambique, portuguese-india and portuguese-timor hold the same land and neighbours found from them; kingdom-of-spain models Spanish Morocco and the Sahara as vassals. Needs one project-wide rule.
- united-kingdom /ledger/15 and /ledger/21 name german-empire for the Cologne zone from December 1918; weimar-republic starts 9 November 1918.
- Reviewer applied small fixes in place to weimar-republic, estado-novo, republic-of-latvia, second-spanish-republic and irish-free-state (each marked 'Reviewer eu-21-c' in the note); all re-validate with 0 errors.
