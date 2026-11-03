# Notes for group eu-21-b (Europe 1914 to 1945, part b)

Six dossiers written from pages opened on 2026-11-01: hungarian-republic, kingdom-of-lithuania, kingdom-of-romania, republic-of-austria, second-polish-republic, yugoslavia. All validate (`validate_dossier.py`, `--resolve` clean except the warnings below). Pages opened: Romania 6, Hungary 7, Lithuania 6, Austria 2, Poland 6, Yugoslavia 6; several pages are shared between dossiers (Axis occupation of Yugoslavia, Trianon, Hungarian-Romanian War, Vilnius Region, Invasion of Poland, Democratic Federal Yugoslavia).

## Cliopatria rows to rename, split or merge
- Kingdom of Lithuania (1919-1939, Q1656775): the row is interwar Lithuania, not the Kingdom of Lithuania of the Wikipedia article it links (mostly the 1251-1263 kingdom; the 1918 monarchy is one paragraph). The dossier is the Republic of Lithuania, 16 February 1918 to July 1940, under the slug `kingdom-of-lithuania`. Suggest renaming the display name; the 1990-2024 row `republic-of-lithuania` is a different (restored) state.
- Kingdom of Romania (1919-1947) and Romania (1990-2024) share Q203493: not one state (the 1948-1989 communist state has its own row). Not merged. The Old Kingdom 1881-1918 is the united-principalities dossier; this dossier starts December 1918 (Greater Romania).
- Yugoslavia (1919-1945) and Socialist Federal Republic of Yugoslavia (1946-1991) share Q83286: not one state (monarchy abolished 29 November 1945, republic proclaimed the same day). Not merged; the SFRY dossier already names `yugoslavia` as predecessor.
- Hungarian Republic (1919-1943): the Hungary of the regency (a kingdom without a king from 29 February 1920 to 1 February 1946), not a republic; Q28513 belongs to other rows. The Cliopatria shapes stop in 1943; new keyframes cover 1944 and 1945-1946.
- Republic of Austria (1919-1937) runs to the Anschluss of March 1938 (new 1938 keyframe).

## Shape problems found (keyframe verdicts 'adjust')
- Hungarian Republic 1919 (119,603 km2) reaches into Slovakia and Ruthenia; replaced by the post-Trianon rump plus a June 1919 contest and the Romanian occupation.
- Kingdom of Romania 1941 and 1942-43: Bessarabia and Northern Bukovina are back from July 1941; Transnistria (Dniester-Bug) is an occupation, not part of the shape. 1945-1946 has no shape (new keyframe = the 1947 shape).
- Yugoslavia: 1941-1944 has no shape (new keyframe: the occupied rump), the 1920 shape still holds Zadar, 1945 unverified at Istria.
- Second Polish Republic 1919 lacks Eastern Galicia and western Volhynia (both Polish by end-1919).
- Lithuania 1939 lacks Vilnius (October 1939); the 1940 keyframe is new.
- Republic of Austria 1919 holds South Tyrol (20 cells); the 1920 shape holds Burgenland a year before the page's 1921.

## Counterparts without a dossier (see the report)
state-of-slovenes-croats-and-serbs (Oct-Dec 1918), central-lithuania (Oct 1920-Mar 1922), the Moldavian Democratic Republic / Sfatul Tarii (1917-1918), Carpatho-Ukraine (March 1939). Existing dossiers used as counterparts (including the eu-21-x ones for Serbia, Montenegro and the General Government): czechoslovakia, weimar-republic, nazi-germany, slovak-republic, memel-territory, lithuanian-soviet-socialist-republic, independent-state-of-croatia, principality-of-bulgaria, kingdom-of-italy, albania, montenegro, ukrainian-people-s-republic, republics-of-the-soviet-union, union-of-soviet-socialist-republics, yugoslav-partisans, socialist-federal-republic-of-yugoslavia, second-hungarian-republic, territory-of-the-military-commander-in-serbia, italian-governorate-of-montenegro, general-government.

## Dating differences with neighbours' dossiers (not errors)
- Transylvania, Banat: after the fix pass Romania books only the Trianon recognition (4 June 1920, 'Transylvania (broad)'), matching the Hungarian loss; the 1918 unions of Bessarabia, Bukovina and Transylvania are booked by the united-principalities-of-moldavia-and-wallachia dossier (ledger 22, 27, 28).
- Burgenland: Hungary's loss and Austria's gain are both 1921 (no month); Cliopatria's Austrian 1920 shape includes it already.
- Trans-Olza: Poland's page gives 1 October 1938, the Czechoslovak dossier 2 October.
- Vilnius: 10 October 1939 (treaty, Vilnius Region page) versus 28 October (handover, Invasion of Poland page); the ledger carries October with both dates in the note.
- Slovak-Hungarian War: after the fix pass the start is March 1939 at confidence 2 (First Vienna Award page: Hungary 'on March 23 launched a larger attack on eastern Slovakia') and the end 4 April 1939 (negotiations 'March 27 - April 4'), as in the slovak-republic dossier (23 March - 4 April).
- Bulgarian zone in Yugoslavia: the Axis occupation page says annexed on 14 May 1941; the Bulgarian dossier models an occupation to 1944; this batch mirrors the Bulgarian dossier and notes the annexation.

## Pages that said nothing (recorded at confidence 1 or left out)
- Hungary: the November 1918 proclamation, the April 1941 date of the Backa annexation, the Soviet occupation and Allied Control Commission 1944-1947, the January 1945 armistice, the 1945 return of southern Slovakia, Ruthenia and Backa (events written at confidence 1 or 2 and bridged to the 1947 treaty).
- Romania: the 1923 border exchange with Yugoslavia (no area), the date of the name 'Legionary Romania', the extent of the Transnistria Governorate, the end date of the Romanian administration (1944).
- Yugoslavia: the date and boundary of each annexation of April 1941, Istria/Rijeka/Zadar/Julian March in 1945, the Carinthian plebiscite (Kingdom page: 'opted to remain in Austria', no date), Lower Styria and the Sudeten cessions.
- Poland: the Posen/Pomerelia transfer date (10 January 1920), the Upper Silesia partition (1922; written at confidence 1 from the German dossier), the Spisz/Orava arbitration (Czechoslovak land), Belarus in 1919 (Grodno, Pinsk, Vilnius), the 1923 recognition (the ambassadors' decision is dated 14 March 1923 on the Polish-Ukrainian War page).
- Lithuania: capitals (Vilnius to Kaunas), presidents, the July 1918 election of Wilhelm of Urach, the Suwalki agreement and Zeligowski dates, 1915-1918.
- Austria: the 12 November 1918 proclamation, no area figure on either page (infobox comparison impossible).

## Pages that did not load
None failed. The URL `Interwar_Lithuania` redirected to a general Lithuania history page (no 1918-1940 section); only its 16 February 1918 sentence was used.

## Gazetteer names needed (all used with a fallback)
Cieszyn Silesia / Trans-Olza (region; a coordinate disc intersected with Moravskoslezsky is used), Cieszyn (place), Orava and Spisz (regions; a coordinate disc is used for Gorna Orawa and Tatranska Javorina), Prekmurje (region; Murska Sobota used), Hertsa region (inside Bukovina), Sudetenland, Suwalki, Vilnius Region and Klaipeda Region (radius around the city is used), Lower Styria (Maribor radius used), Banovina of Croatia (not used).

## Fix pass after review eu-21-b (2026-11-01)

Dossiers touched: hungarian-republic, kingdom-of-romania, yugoslavia (verdict fail). Not touched: kingdom-of-lithuania and republic-of-austria (pass), second-polish-republic (thin). Pages opened again or for the first time in the fix pass: Hungarian-Romanian War, Treaty of Trianon, First Vienna Award, Hungary in World War II, Hungarian occupation of Yugoslav territories, First Austrian Republic, Julian March, Yugoslav Front (twice, text cut off; not cited), Transnistria Governorate, Banat, Kingdom of Yugoslavia, Axis occupation of Yugoslavia, Operational Zone of the Adriatic Littoral, Second Vienna Award. All three dossiers validate with `--resolve` (0 errors, 0 warnings). Details are in each dossier's `notes`.

### hungarian-republic
- Applied (blocking): the Romanian contest (1919/4-1919/8) and occupation (1919/8-1920) regions and the Hungarian-Romanian War zones now lie in Hungary: contest = the 1920 shape within Hajdu-Bihar, Szabolcs-Szatmar-Bereg and Bekes (58 cells, about 14,700 km2; the page: 'the entire east bank of the Tisza River'); occupation = the 1920 shape minus a 60 km disc at lon 17.75, lat 46.85 (314 cells; the page: 'all of Hungary except for an area around Lake Balaton'). Not drawn: Csongrad and Jasz-Nagykun-Szolnok east of the river (the page names towns, not counties).
- Applied by the reviewer and checked: Slovak-Hungarian War start 1939/3, confidence 2; the war note (which still said the page did not date the fighting) is corrected.
- Month of the 1941 annexation of Yugoslav land: 4 (Hungarian occupation page: 'The occupation began on 11 April 1941'; 'Annexed by Hungary: 14 December 1941'); confidence 2 because the formal annexation is December.
- The 1944 loss of Yugoslav land is split: Backa and Baranja to yugoslav-partisans in October 1944 (page: Soviet troops took the area in October 1944 and 'ceded full control of the region to the Partisans'), Medjimurje and Prekmurje to yugoslavia in 1945 ('remained occupied until the last weeks of the war'). The yugoslavia dossier mirrors the second.
- German occupation ends 1945/4 at confidence 3 (Hungary in World War II page: 'Officially, Soviet operations in Hungary ended on 4 April 1945, when the last German troops were expelled'). New: Soviet conquest (contest 1944/9 - 1945/4 with union-of-soviet-socialist-republics, a war), Soviet occupation 1945/4 - 1946/2 (confidence 2: the pages name no Allied Control Commission and date no start). The armistice of 20 January 1945 is in the contest note.
- Not changed: the 1945 loss of southern Slovakia and Ruthenia to czechoslovakia (confidence 1): no page opened dates it. czechoslovakia books the strip from slovak-republic, so the mirror must be fixed there.
- Dating difference left: nazi-germany ends its occupation of Hungary in May 1945 (its own dossier), this one on 4 April 1945 (page).

### kingdom-of-romania
- Applied (blocking): ledger events 0, 1 and 3 (Bessarabia 1918, Bukovina 1918/11, Transylvania 1918/12) deleted; united-principalities-of-moldavia-and-wallachia ledger 22, 27, 28 book them and the found event's region holds them. The Banat-only gain of 1920 is recast as the Trianon recognition: 1920/6, 'Transylvania (broad)', counterpart hungarian-republic, source the Trianon page ('Romania gained all of Transylvania'; 'The central parts of Banat were later assigned to Romania'; Crisana and Maramures are the researcher's reading, so confidence 2). The austria-hungary predecessor note says the land came through the united principalities.
- Applied (blocking): the same Romanian contest and occupation regions and war zones as in hungarian-republic.
- Applied by the reviewer and checked: /ledger 19 (Bessarabia and Northern Bukovina loss) confidence 2.
- Transnistria occupation end: 1944/3, confidence 2 (Transnistria Governorate page: 'A Romanian civilian administration governed the territory from 19 August 1941 to 29 January 1944'; the Red Army 'entered Transnistria on 14 March 1944'; withdrawal ordered 15 March 1944; infobox 'Disestablished: 1 April 1944'; the three dates differ).
- Optional fix applied: the Soviet administration of Northern Transylvania is an occupation pair with the Soviet Union, 1944/10 - 1945/3 (Second Vienna Award page: 'The Soviet Union kept administrative control until 9 March 1945, when it was reverted to Romania'; the start month is a bridge).
- Not settled: the 1923 border exchange with the Kingdom of Serbs, Croats and Slovenes (Banat page does not mention it; the Kingdom page names it without an area).

### yugoslavia
- Applied (blocking): the November 1918 gain of Montenegro deleted (Kingdom page: Montenegro 'absorbed into Serbia the previous month'); serbs added as first predecessor and as the found counterpart (the 'serbia' dossier stays as a second predecessor; drop it if the orchestrator removes it).
- Applied (blocking): the 1944 gains of Backa, Montenegro and Serbia deleted; the 1945/3 merge with yugoslav-partisans now carries the Partisan-held land (region widened to the 1944 shape plus Montenegro, Serbia without Srem, North Macedonia, Kosovo and Dalmatia, clipped to the 1945 shape; confidence 2). The 1945 gain of Kosovo from albania deleted for the same reason (albania ledger 20: Partisans, 1944, confidence 1).
- 1945 return of the Italian-annexed lands: counterpart nazi-germany (Operational Zone of the Adriatic Littoral page: established 10 September 1943 and comprising the Ljubljana province; the Axis page puts former Italian Montenegro under German occupation); region reduced to the Ljubljana Province and the Bay of Kotor; Dalmatia left to the merge (Partisan coast) and to the NDH gain.
- Serbian loss region = the Territory dossier's found region; London dropped from capitals and the capital_move folded into the April 1941 note.
- Added: gain of Lower Styria (1919/9) and Carinthian contest (1919 - 1920/10) mirroring republic-of-austria (First Austrian Republic page); Julian March occupation by the Yugoslav army 1945/5 - 1945/11 (Julian March page: 'In May 1945, the Yugoslav Army entered Trieste'; 'Zone B was under Yugoslav administration'); Medjimurje and Prekmurje gain 1945.
- Not settled (all confidence 1, no page gives a date): end of the German occupation of northern Slovenia, return of the Ljubljana Province and the Bay of Kotor, Partisan entry into Kosovo. Pages tried: Yugoslav Front (the fetched text stops before 1945), Axis occupation of Yugoslavia, Operational Zone of the Adriatic Littoral, Julian March.

### Routing for the orchestrator (not mine to write)
- yugoslav-partisans: no Backa and Baranja gain (October 1944), no Kosovo, dissolve names no counterpart (should be yugoslavia); nazi-germany: no occupation of northern Slovenia 1941-1945, ends the Hungarian occupation in May 1945 (page: 4 April); czechoslovakia: books southern Slovakia from slovak-republic, not from hungarian-republic; union-of-soviet-socialist-republics: no mirror of the Romanian occupation of Transnistria (1941-1944), the Soviet administration of Northern Transylvania (1944/10 - 1945/3), or the contest and occupation of Hungary (1944/9 - 1946/2); kingdom-of-italy: books South Tyrol from austria-hungary, not republic-of-austria.
- Gazetteer: the region names used in the fix pass all exist ('Transylvania (broad)', admin1 names, Lake Balaton by coordinate); none new.
