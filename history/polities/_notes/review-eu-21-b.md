# Review of batch eu-21-b (2026-11-01)

Reviewer: adversarial review per history/briefs/reviewer-brief.md. Validator (--resolve) clean on all six; the only warnings are central-lithuania (no dossier yet, listed by the author). Spot checks were weighted to confidence-3 events and the largest land moves; regions were resolved with the gazetteer to see where they actually land.

| slug | verdict |
| --- | --- |
| hungarian-republic | fail |
| kingdom-of-lithuania | pass |
| kingdom-of-romania | fail |
| republic-of-austria | pass |
| second-polish-republic | thin |
| yugoslavia | fail |

## hungarian-republic: fail

Area: infobox 172149 km2 (1941) against Cliopatria 174011 km2, ratio 1.01. 

Findings:

- **/ledger/2, /ledger/5, /ledger/6, /ledger/7 (region) and /wars/0/zones/0** (not applied; blocking): The Romanian contest and occupation of 1919-1920 are drawn on the wrong land: the region spec lands in Slovakia and Ruthenia, not in Hungary east of the Tisza and around Budapest as the text says.  
  Evidence: The spec {minus:[Hungarian Republic 1919, Hungarian Republic 1920]} resolves to 116 cells (29,195 km2): 53 in Ukraine (Ruthenia), 34 in Slovakia, 9 in Hungary, 0 in Romania; the 1920 shape holds 35 cells within 60 km of Debrecen that the spec leaves out. Hungarian-Romanian War page: 'On the evening of 1 May, the entire east bank of the Tisza River was under the control of the Romanian Army'; 'Romania occupied all of Hungary except for an area around Lake Balaton'; 'In early 1920, Romanian troops departed Hungary'. The 1919 keyframe note says the occupation is to be drawn from the ledger, so the 1920 anchor would hatch Czechoslovak Slovakia and Ruthenia and leave Hungary proper clear.  
  Fix: Contest 1919/4-1919/8 ('the entire east bank of the Tisza'): {"intersect":[{"cliopatria":"Hungarian Republic","year":1920},{"union":[{"admin1":"Hajdú-Bihar","country":"Hungary"},{"admin1":"Szabolcs-Szatmár-Bereg","country":"Hungary"},{"admin1":"Békés","country":"Hungary"}]}]} (resolves to 58 cells, 14,876 km2; add the parts of Csongrád and Jász-Nagykun-Szolnok east of the river if wanted). Occupation 1919/8-1920 ('all of Hungary except for an area around Lake Balaton'): {"minus":[{"cliopatria":"Hungarian Republic","year":1920},{"lon":17.75,"lat":46.85,"km":60}]}. Use the same specs in the war zone.
- **/ledger/14** (applied by reviewer): Slovak-Hungarian War start recorded at confidence 1 with no month, the note claiming the page does not date the fighting.  
  Evidence: First Vienna Award page (a source of this dossier): Hungary 'on March 23 launched a larger attack on eastern Slovakia'.  
  Fix: month 3, confidence 2, note extended with the quote.
- **/ledger/25** (not applied): 1945 loss of southern Slovakia and Ruthenia to czechoslovakia (confidence 1) has no mirror: czechoslovakia/ledger/13 books the southern-Slovak strip as a 1945 gain from slovak-republic and czechoslovakia/ledger/15 loses Ruthenia to the USSR in 1945/6.  
  Evidence: Cross-dossier check; the same defect is already listed against czechoslovakia in review eu-21-a.  
  Fix: No change needed here once czechoslovakia books the strip from hungarian-republic; keep the 1945 date until a page dates the return (Soviet conquest December 1944-April 1945).

Gaps for a gap-filler:

- /ledger/24, /ledger/25: Date of the end of German occupation and of the de facto return of southern Slovakia, Ruthenia and Backa (confidence 1); no event or war for the Soviet conquest and occupation of 1944-1945, although the Kingdom page says 'Under Soviet occupation, the fate of the Kingdom of Hungary was already determined'. (try https://en.wikipedia.org/wiki/Hungary_in_World_War_II)
- /ledger/19: Month of the 1941 annexations (the Kingdom page's infobox gives 'Invasion of Yugoslavia: 11 April 1941'). (try https://en.wikipedia.org/wiki/Hungarian_occupation_of_Yugoslav_territories)

Spot checks: /ledger/13 confirmed; /ledger/15 confirmed; /ledger/14 mis-dated (page gives 23 March 1939; fixed); /ledger/18 confirmed; /ledger/23 confirmed (page adds Soviet administration until 9 March 1945); /ledger/21 confirmed; /ledger/26 confirmed; /ledger/6 confirmed in date and words; region drawn on the wrong land (see fixes)

## kingdom-of-lithuania: pass

Area: infobox None km2 (None) against Cliopatria 62642 km2, ratio None. No infobox area: the linked Kingdom of Lithuania page is the 1251-1263 kingdom, Interwar_Lithuania redirects to a general history without area and History_of_Lithuania_(1918-1940) did not resolve. The Cliopatria shapes exclude Vilnius (2 of the cells within 20 km) and the 1924 shape is 62,642 km2; no factor-two question arises.

Gaps for a gap-filler:

- /ledger (1918-1919): The Soviet-Lithuanian War and the Bermontian episode (Bolshevik forces held Vilnius and eastern Lithuania from January 1919): no contest; the 1919 shape shows the whole country. (try https://en.wikipedia.org/wiki/Lithuanian_Wars_of_Independence)
- /identity/rulers: Presidents 1919-1940 (Smetona, Stulginskis, Grinius); only Mindaugas II for 1918. (try https://en.wikipedia.org/wiki/President_of_Lithuania)

Spot checks: /ledger/3 confirmed; /ledger/5 confirmed; /ledger/9 confirmed; /ledger/10 confirmed; /ledger/11 confirmed; /ledger/0 confirmed (URL redirects to History of Lithuania, as the author says)

## kingdom-of-romania: fail

Area: infobox 295049 km2 (1940) against Cliopatria 301073 km2, ratio 1.02. 

Findings:

- **/ledger/0, /ledger/1, /ledger/3** (not applied; blocking): Three gains duplicate the predecessor dossier's own gains and predate this dossier's start or name a different counterpart: Bessarabia (1918, April by the predecessor), Bukovina (1918/11, before the start 1918-12) and Transylvania (1918/12 from hungarian-republic).  
  Evidence: united-principalities-of-moldavia-and-wallachia/ledger/22 (1918/4 Bessarabia), /27 (1918/11 Bukovina) and /28 (1918/12 Transylvania from austria-hungary) already carry them, and austria-hungary/ledger/35 splits Transylvania and Bukovina to that dossier in 1918/10; hungarian-republic has no 1918-1919 loss of Transylvania. This dossier's found event (/ledger/2, region = the 1919 shape) already holds all three lands.  
  Fix: Delete /ledger/0, /1 and /3. Recast /ledger/8 as Trianon's recognition: year 1920, month 6, region {"region":"Transylvania (broad)"} (it already contains the Romanian Banat: 96 Banat cells inside it), counterpart hungarian-republic, mirroring hungarian-republic/ledger/9. Say in the austria-hungary predecessor note that the land came through the united principalities.
- **/ledger/4, /ledger/5, /ledger/6, /ledger/7 (region) and /wars/0/zones/0** (not applied; blocking): Same misplaced region as hungarian-republic: the Romanian advance and occupation of 1919-1920 are drawn in Slovakia and Ruthenia.  
  Evidence: The spec {minus:[Hungarian Republic 1919, Hungarian Republic 1920]} resolves to 116 cells (29,195 km2): 53 in Ukraine (Ruthenia), 34 in Slovakia, 9 in Hungary, 0 in Romania; the 1920 shape holds 35 cells within 60 km of Debrecen that the spec leaves out. Hungarian-Romanian War page: 'On the evening of 1 May, the entire east bank of the Tisza River was under the control of the Romanian Army'; 'Romania occupied all of Hungary except for an area around Lake Balaton'; 'In early 1920, Romanian troops departed Hungary'. The 1919 keyframe note says the occupation is to be drawn from the ledger, so the 1920 anchor would hatch Czechoslovak Slovakia and Ruthenia and leave Hungary proper clear.  
  Fix: Contest 1919/4-1919/8 ('the entire east bank of the Tisza'): {"intersect":[{"cliopatria":"Hungarian Republic","year":1920},{"union":[{"admin1":"Hajdú-Bihar","country":"Hungary"},{"admin1":"Szabolcs-Szatmár-Bereg","country":"Hungary"},{"admin1":"Békés","country":"Hungary"}]}]} (resolves to 58 cells, 14,876 km2; add the parts of Csongrád and Jász-Nagykun-Szolnok east of the river if wanted). Occupation 1919/8-1920 ('all of Hungary except for an area around Lake Balaton'): {"minus":[{"cliopatria":"Hungarian Republic","year":1920},{"lon":17.75,"lat":46.85,"km":60}]}. Use the same specs in the war zone.
- **/ledger/19** (applied by reviewer): Loss of Bessarabia and Northern Bukovina dated August 1944 at confidence 3; the page describes a gradual loss from early 1944.  
  Evidence: Soviet occupation of Bessarabia and Northern Bukovina page: 'In early 1944, the Soviet Union gradually took over the territory'; 23 August 1944 is the date of the coup only.  
  Fix: confidence 2, note extended.
- **/ledger/21** (not applied): Northern Transylvania counted Romanian from October 1944 at confidence 3 while the page puts it under Soviet administration until March 1945.  
  Evidence: Second Vienna Award page: 'The Soviet Union kept administrative control until 9 March 1945, when it was reverted to Romania.'  
  Fix: Optional: an occupation_start (counterpart union-of-soviet-socialist-republics) 1944/10 and occupation_end 1945/3, or keep the gain and leave the note as is.

Gaps for a gap-filler:

- /ledger/17: End of the Transnistria Governorate (confidence 1); the Romanian withdrawal from the Dniester-Bug land in spring 1944. (try https://en.wikipedia.org/wiki/Transnistria_Governorate)
- /ledger (1923): The 1923 exchange of border settlements with the Kingdom of Serbs, Croats and Slovenes (the Kingdom page names it, no area). (try https://en.wikipedia.org/wiki/Banat)

Spot checks: /ledger/10 confirmed; /ledger/15 confirmed; /ledger/19 mis-dated (gradual from early 1944; confidence lowered to 2); /ledger/12 confirmed; /ledger/21 confirmed (with Soviet administration to 9 March 1945); /ledger/1 confirmed on the page, but a duplicate of the predecessor's event (see fixes); /ledger/22 confirmed

## republic-of-austria: pass

Area: infobox None km2 (None) against Cliopatria 85624 km2, ratio None. First Austrian Republic page has no area (checked). Keyframe 2 is marked ok while holding Burgenland a year before /ledger/5; its note says so.

Gaps for a gap-filler:

- /ledger/1: Start of the Carinthian dispute (confidence 1): Yugoslav troops entered southern Carinthia in late 1918. (try https://en.wikipedia.org/wiki/Carinthian_plebiscite)
- /ledger (1919-1920): The page says Saint-Germain also 'ceded German-populated regions in Sudetenland to Czechoslovakia'; not recorded (consistent with a found region that never held them, but Lower Styria, also never held, is recorded as a loss). Small cessions to Czechoslovakia (Valtice, Vitorazsko) are absent. (try https://en.wikipedia.org/wiki/Treaty_of_Saint-Germain-en-Laye_(1919))

Spot checks: /ledger/2 confirmed; /ledger/3 confirmed ('a portion of the Alpine provinces'; confidence 2 is right); /ledger/4 confirmed; /ledger/5 confirmed; /ledger/6 confirmed

## second-polish-republic: thin

Area: infobox 388634 km2 (None) against Cliopatria 373209 km2, ratio 0.96. Infobox gives 388,634 km2 with no year; the body gives 389,720 km2 after Trans-Olza. Compared with the 1924-1935 shape.

Findings:

- **/ledger/25** (applied by reviewer): Slovak seizure of the southern border areas recorded with no month.  
  Evidence: Second Polish Republic page ties it to the start of the invasion: 'On that day, Germany and Slovakia attacked Poland' (1 September 1939); the Slovak dossier's November date is the formal annexation.  
  Fix: month 9, note extended.
- **/ledger/19 (and the 60 km discs of /ledger/11, /12, /20, /21)** (not applied): The 1922 annexation of the Vilnius Region is drawn as a 100 km disc around Vilnius, half of which is Lithuanian land.  
  Evidence: The disc resolves to 144 cells (31,432 km2); 73 of them (15,855 km2) lie inside kingdom-of-lithuania's 1924 Cliopatria shape and 2 within 15 km of Kaunas, the Lithuanian capital; only 71 cells lie inside Poland's own 1924 shape. The 60 km disc puts 26 cells (5,655 km2) inside Lithuania.  
  Fix: Clip to Polish land: {"intersect":[{"place":"Vilnius","km":100},{"cliopatria":"Second Polish Republic","year":1924}]} (or the gazetteer's 'Vilnius Region' when it exists); clip the 60 km discs the same way.
- **/ledger/22, /ledger/23** (not applied): The 1922 gain of 'eastern Upper Silesia' (confidence 1) is drawn as the whole of Upper Silesia.  
  Evidence: {"region":"Upper Silesia"} resolves to 117 cells, 28,203 km2 (92 of them in modern Poland, including Opole Silesia, which stayed German); the Polish share was about a third of the plebiscite area. weimar-republic/ledger/12 says 'East Upper Silesia, the part awarded to Poland'.  
  Fix: {"intersect":[{"region":"Upper Silesia"},{"cliopatria":"Second Polish Republic","year":1924}]} (26 cells, 6,235 km2), with a page for the date.
- **/keyframe_review/2/note** (not applied): The 1920-1923 shape, marked ok, already holds the 26 East Upper Silesian cells two years before the 1922 partition; the note does not say so.  
  Evidence: Intersect of the 1920 shape with Upper Silesia = 26 cells, the same as the 1924 shape.  
  Fix: Say so in the note (or adjust for 1920-1921).

Gaps for a gap-filler:

- /ledger/22, /ledger/23: Upper Silesia plebiscite (20 March 1921) and partition (transfer June 1922): confidence 1, taken from the German dossier. (try https://en.wikipedia.org/wiki/Upper_Silesia_plebiscite)
- /ledger (1920, 1938): The Spa division of Spisz and Orava (28 July 1920) and the Polish annexation of Slovak border villages in autumn 1938 (the Second Polish Republic page: areas 'which Poland had annexed from Czechoslovakia in October 1938'); no gain events. (try https://en.wikipedia.org/wiki/Polish%E2%80%93Czechoslovak_border_conflicts)
- /ledger/0: Month of the Greater Poland uprising (27 December 1918); without it the contest sorts before the found event. (try https://en.wikipedia.org/wiki/Greater_Poland_uprising_(1918%E2%80%931919))

Spot checks: /ledger/18 confirmed; /ledger/13 confirmed; /ledger/3 confirmed; /ledger/24 confirmed; /ledger/16 confirmed; /ledger/4 confirmed (23 January 1919); /ledger/19 confirmed (date); region spills into Lithuania (see fixes); /ledger/25 confirmed; month added

## yugoslavia: fail

Area: infobox 247542 km2 (1941) against Cliopatria 246055 km2, ratio 0.99. 

Findings:

- **/ledger/0** (not applied; blocking): Gain of Montenegro in November 1918 (confidence 3) before the state existed; the page says Montenegro was absorbed into Serbia.  
  Evidence: Kingdom of Yugoslavia page: 'Established: 1 December 1918' and 'Montenegro having been absorbed into Serbia the previous month'. serbs/ledger/30 (1918/11 gain cp montenegro) and montenegro/ledger/13 (1918/11 merge cp serbs) already carry it.  
  Fix: Delete the event (the found event's region holds Montenegro); add serbs, the Kingdom of Serbia dossier that dissolves 1918-12, to predecessors (the 'serbia' dossier was failed in review eu-21-a as a duplicate of serbs).
- **/ledger/19, /ledger/20, /ledger/22** (not applied; blocking): Land retaken in 1944 (Backa, Montenegro, Serbia) is given to the Kingdom, whose government sat in London, while the counterpart dossiers give it to the Partisans; the 1945/3 merge (/ledger/27) then brings the same land in a second time.  
  Evidence: territory-of-the-military-commander-in-serbia/ledger/5 (1944/10 loss to yugoslav-partisans); yugoslav-partisans/ledger/9-10 (Belgrade 1944/10, Serbia 1944/12) and /7 (Risan and Podgorica); italian-governorate-of-montenegro/ledger/6-7 (German occupation ends, dissolves 1944/12, no Yugoslav counterpart). This dossier's own notes say 'the Partisans hold Montenegro' and 'The Red Army took the city on 20 October' with the Partisans.  
  Fix: Drop the three gains and let /ledger/27 (merge with yugoslav-partisans, 1945/3) carry the Partisan-held land, or move them to the Partisans dossier; hungarian-republic/ledger/20 then names yugoslav-partisans.
- **/ledger/25** (not applied): 1945 gain of Ljubljana Province, Dalmatia and Kotor from kingdom-of-italy (confidence 1), which had lost them in 1943.  
  Evidence: kingdom-of-italy/ledger/38: 1943/9 loss of these lands to nazi-germany; this dossier's own note dates their release to the armistice of 8 September 1943.  
  Fix: Counterpart nazi-germany (or independent-state-of-croatia for the Dalmatian part, which the NDH took in September 1943), or let the merge carry it.
- **/ledger/26** (not applied): 1945 gain of Kosovo from albania (confidence 1) disagrees with albania/ledger/20, a 1944 loss to yugoslav-partisans.  
  Evidence: Cross-dossier check.  
  Fix: Agree year and counterpart with albania (1944, the Partisans, carried by the 1945/3 merge).
- **/ledger (1919-1920)** (not applied): No mirror for Austria's losses: no gain of Lower Styria (republic-of-austria/ledger/3, 1919/9) and no contest over southern Carinthia (republic-of-austria/ledger/1 and /4).  
  Evidence: Same batch; the Kingdom page itself says Carinthia 'opted to remain in Austria'.  
  Fix: Add gain 1919/9 cp republic-of-austria {"place":"Maribor","km":40} (confidence 2), contest_start 1919 and contest_end 1920/10 cp republic-of-austria {"place":"Klagenfurt","km":35}, source https://en.wikipedia.org/wiki/First_Austrian_Republic (add to sources).
- **/ledger/15** (not applied): The Serbian loss is drawn as the whole modern Republic of Serbia, which overlaps the Backa loss to Hungary (/ledger/7), Srem in the NDH (/ledger/11) and the Pirot occupation (/ledger/14).  
  Evidence: Region spec {"country":"Republic of Serbia"} includes Vojvodina and Pirot.  
  Fix: Use the Territory dossier's found region, or minus the other three regions.
- **/identity/capitals/1** (not applied): London (government in exile) 1941-1944 is a capital outside every shape of the state.  
  Evidence: Rule: capitals lie inside the state's shapes in those years.  
  Fix: Drop the London entry (say the exile in notes) or end Belgrade in 1941 with no capital until 1944.

Gaps for a gap-filler:

- /keyframe_review/5: The 1945 shape holds 21 cells not in the 1936 shape, 18 of them Istria and the Slovene Littoral (lon 13.5-14.1, lat 44.9-46.1, about 4,500 km2), with no ledger event (marked unverified: page budget); the SFRY dossier begins an occupation of the Julian March in 1945/11 against kingdom-of-italy, so an occupation_start 1945/5 belongs here. (try https://en.wikipedia.org/wiki/Julian_March)
- /ledger/24, /ledger/25, /ledger/26: Dates of the end of German occupation of northern Slovenia and of the return of the Italian-annexed lands and Kosovo (confidence 1). (try https://en.wikipedia.org/wiki/Yugoslav_Front)

Spot checks: /ledger/2 confirmed; /ledger/4 confirmed; /ledger/3 confirmed in substance; the quoted list is stitched from several sentences, not verbatim; /ledger/27 confirmed; /ledger/17 confirmed; /ledger/5 confirmed; /ledger/0 not on page as an event of this state: the page says Montenegro was absorbed into Serbia (see fixes)

## Cross-dossier matrix: mismatches and missing mirrors

- hungarian-republic 1920 loss (cp kingdom-of-romania): mismatch. romania/ledger/8 gains only the Banat; it books Transylvania in 1918/12 (/ledger/3), a duplicate of united-principalities/ledger/28; fix in kingdom-of-romania
- hungarian-republic 1944 loss (cp yugoslavia): mismatch. yugoslavia/ledger/19 mirrors it, but the Partisans, not the exiled Kingdom, retook Backa; counterpart should become yugoslav-partisans (whose dossier lacks Backa)
- hungarian-republic 1945 loss (cp czechoslovakia): missing. czechoslovakia/ledger/13 books the strip from slovak-republic; route to czechoslovakia (already in review eu-21-a)
- kingdom-of-lithuania 1920 gain (cp republics-of-the-soviet-union): missing. republics-of-the-soviet-union (eu-17) has no loss of Vilnius to Lithuania in 1920
- kingdom-of-lithuania 1920 loss (cp central-lithuania): exception. no dossier; in the author counterparts_needing_dossiers
- kingdom-of-lithuania 1939 gain (cp union-of-soviet-socialist-republics): missing. USSR (eu-17) gains eastern Poland in 1939/9 but has no 1939/10 loss of Vilnius to Lithuania
- kingdom-of-lithuania 1940 occupation_start (cp union-of-soviet-socialist-republics): mismatch. USSR/ledger/17 has a 1940/8 gain only; no occupation_start 1940/6 (route eu-17)
- kingdom-of-lithuania 1940 occupation_end (cp union-of-soviet-socialist-republics): mismatch. as above
- kingdom-of-romania 1918 gain (cp Sfatul Țării (National Council of Bessarabia)): mismatch. no dossier for the counterpart, but the predecessor books the same gain (ledger/22, 1918/4); delete here
- kingdom-of-romania 1918 gain (cp austria-hungary): mismatch. austria-hungary/ledger/35 splits Bukovina to united-principalities, which books the gain (ledger/27); delete here
- kingdom-of-romania 1918 gain (cp hungarian-republic): mismatch. hungarian-republic has no 1918-1919 loss; united-principalities/ledger/28 books Transylvania from austria-hungary; delete here and date the Trianon recognition 1920/6
- kingdom-of-romania 1941 occupation_start (cp union-of-soviet-socialist-republics): mismatch. USSR/ledger/26 loses Ukraine (with the Dniester-Bug land) to nazi-germany in 1941/9; no Romanian occupation (route eu-17)
- kingdom-of-romania 1944 occupation_end (cp union-of-soviet-socialist-republics): mismatch. as above
- republic-of-austria 1919 loss (cp kingdom-of-italy): mismatch. kingdom-of-italy/ledger/15 gains South Tyrol in 1919 from austria-hungary, which split it to Italy in 1918/10 (austria-hungary/ledger/37); Austria's loss is the treaty renunciation; Italy (eu-13) could name republic-of-austria
- republic-of-austria 1919 loss (cp yugoslavia): missing. yugoslavia has no gain from Austria (same batch; fix listed under yugoslavia)
- second-polish-republic 1919 gain (cp ukrainian-people-s-republic): missing. western Volhynia: ukrainian-people-s-republic/ledger/15 is Eastern Galicia only (route eu-17)
- second-polish-republic 1920 vassal_start (cp central-lithuania): exception. no dossier; in counterparts_needing_dossiers
- second-polish-republic 1920 occupation_start (cp republics-of-the-soviet-union): missing. Kiev, May-June 1920: no mirror in republics-of-the-soviet-union (eu-17)
- second-polish-republic 1920 occupation_end (cp republics-of-the-soviet-union): missing. as above
- second-polish-republic 1921 gain (cp republics-of-the-soviet-union): missing. Riga: republics-of-the-soviet-union has no loss to Poland (its 1920/7 gain from Poland has no Polish loss either; the Polish contest covers it)
- second-polish-republic 1922 gain (cp central-lithuania): exception. no dossier
- second-polish-republic 1922 vassal_end (cp central-lithuania): exception. no dossier
- yugoslavia 1918 gain (cp montenegro): mismatch. montenegro/ledger/13 merges into serbs; serbs/ledger/30 books the gain; delete here
- yugoslavia 1941 occupation_start (cp nazi-germany): mismatch. nazi-germany/ledger/26 is Serbia; this event is northern Slovenia, which the German dossier does not record
- yugoslavia 1944 gain (cp hungarian-republic): mismatch. matched by hungarian-republic/ledger/20, but the land went to the Partisans (see yugoslavia fixes)
- yugoslavia 1944 gain (cp italian-governorate-of-montenegro): mismatch. governorate dissolves 1944/12 with no counterpart; yugoslav-partisans/ledger/7 takes Podgorica
- yugoslavia 1944 gain (cp territory-of-the-military-commander-in-serbia): mismatch. territory/ledger/5 loses Serbia to yugoslav-partisans
- yugoslavia 1945 occupation_end (cp nazi-germany): mismatch. nazi-germany/ledger/67 (1945/1) ends the occupation of Serbia, not of northern Slovenia
- yugoslavia 1945 gain (cp kingdom-of-italy): mismatch. kingdom-of-italy/ledger/38 lost these lands to nazi-germany in 1943/9
- yugoslavia 1945 gain (cp albania): mismatch. albania/ledger/20 loses Kosovo to yugoslav-partisans in 1944
- yugoslavia 1945 merge (cp yugoslav-partisans): mismatch. yugoslav-partisans/ledger/16 dissolves 1945/3 with counterpart None; it should name yugoslavia

All other territorial events found their mirror within a year (47 matched).

## Routing and problems

- Lithuania has no area figure to compare: Kingdom_of_Lithuania is the 1251-1263 kingdom, Interwar_Lithuania redirects to History of Lithuania without one, and History_of_Lithuania_(1918%E2%80%931940) returned url_not_found. First_Austrian_Republic has no area either.
- Routing for eu-17: republics-of-the-soviet-union lacks the 1920 loss of Vilnius to Lithuania, the Polish occupation of Kiev (May-June 1920) and the Riga loss (1921/3); union-of-soviet-socialist-republics lacks the 1939/10 loss of Vilnius to Lithuania, a 1940/6 occupation of Lithuania and the Romanian occupation of Transnistria 1941-1944; ukrainian-people-s-republic lacks the 1919 loss of western Volhynia to Poland.
- Routing for eu-21 (czechoslovakia): its 1945 gain of southern Slovakia names slovak-republic, so hungarian-republic/ledger/25 has no mirror (already in review eu-21-a). For yugoslav-partisans: its 1945/3 dissolve names no counterpart (should be yugoslavia), and it has no Backa gain in 1944. For nazi-germany (failed in eu-21-c): no record of the occupation of northern Slovenia 1941-1945. For kingdom-of-italy (eu-13): South Tyrol in 1919 is booked from austria-hungary, not republic-of-austria.
- The Romanian 1919-1920 occupation region error is shared: fixing hungarian-republic/ledger/2,5,6,7 needs the same change in kingdom-of-romania/ledger/4-7 and both war zones.
- Fixes applied by the reviewer (all re-validated): hungarian-republic/ledger/14 (month 3, confidence 2), kingdom-of-romania/ledger/19 (confidence 2), second-polish-republic/ledger/25 (month 9).
