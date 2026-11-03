# Review of batch eu-21-x (Europe 1914-1945, additions)

Reviewer: adversarial review, 2026-11-01. Validator: all 13 dossiers pass (`--resolve`: 6 gazetteer warnings in slovak-republic for Sobrance and Orava). Pages read with WebFetch; areas resolved with history/tools/gazetteer.py (252.9 km2 a cell). None of the 13 states has a Cliopatria row, so the area checks compare the page figure, where there is one, with the resolved new keyframe.

Verdicts: slovak-republic fail, protectorate-of-bohemia-and-moravia pass, saar-basin-territory pass, memel-territory pass, italian-social-republic pass, general-government thin, reichskommissariat-ukraine thin, reichskommissariat-ostland pass, territory-of-the-military-commander-in-serbia pass, italian-governorate-of-montenegro fix, hellenic-state fix, operational-zone-of-the-adriatic-littoral fix, operational-zone-of-the-alpine-foothills pass.

Reviewer edits made in place (each re-validated, read back unchanged): italian-governorate-of-montenegro (Ulcinj subtracted), hellenic-state (Dodecanese subtracted, Dodecanese page added to sources), operational-zone-of-the-adriatic-littoral (Pordenone added).

## slovak-republic: fail

- Finding /ledger (after /ledger/0) and before /ledger/9 (for the author): No vassal_start / vassal_end with nazi-germany, although nazi-germany /ledger/5 (vassal_start 1939-3, counterpart slovak-republic) and /ledger/85 (vassal_end 1945-5) carry the relation; the author left it out on purpose ('the overlord's dossier carries it'). Evidence: Reviewer brief check 3: a vassal_start of X is mirrored in X's ledger with the overlord as counterpart (the independent-state-of-croatia dossier does this). Slovak Republic page: the Treaty of Protection was 'signed on 23 March 1939, partially subordinated its foreign, military, and economic policy to that of Germany'. Fix: Add vassal_start {year 1939, month 3, region = the found region, counterpart 'nazi-germany', confidence 3, source the Slovak Republic page, note quoting the treaty sentence} and vassal_end {1945, 4, same region, counterpart 'nazi-germany'} before the dissolve; keep the 1944 occupation pair.
- Finding /keyframe_review/0/note (for the author): The note says the shape 'includes Orava and Spiš' and 'leaves out the eastern strip ceded to Hungary on 4 April 1939'; the resolved spec does the reverse. Evidence: Resolved with history/tools/gazetteer.py: the cells of Sobrance and Stakčín are inside the 136-cell shape; Jabłonka and Niedzica (Polish Orava and Spiš, Slovak 1939-1945) are outside, because country Slovakia is the modern state and 'Orava'/'Spiš' do not resolve. Fix: Say the shape is the state of 14 March 1939 (strip still Slovak, Orava and Spiš still Polish) and that /ledger/3 and /ledger/4 move them; keep the correction.
- Gap /ledger/7 to /ledger/8: The Red Army's advance through Slovakia, January-April 1945 (eastern Slovakia lost before Bratislava fell on 4 April); the state is drawn whole until April 1945. Page to try: https://en.wikipedia.org/wiki/Western_Carpathian_offensive
- Area: page 38055 km2 (1939), resolved 34394 km2, ratio 0.9.
- Spot checks: /ledger/0 confirmed ('Independence: 14 March 1939'); /ledger/3 confirmed ('cede 1,697 square kilometres'; 'War with Hungary: 23–31 March 1939'); /ledger/4 confirmed (agreement of November 21, 1939; 752 square kilometers); /ledger/9 confirmed ('Fall of Bratislava: 4 April 1945'; 'reintegrated into the recreated Third Czechoslovak Republic'); /ledger/6 confirmed at confidence 2 (Slovak page: 'the Germans occupied the country (from October 1944)'; the 29 August date is from the uprising page)

## protectorate-of-bohemia-and-moravia: pass

Tried: dates, area silence, capital, the found counterpart. Not this dossier's fault: czechoslovakia (eu-21-a) keeps the Czech lands as its own occupied land 1939-1945 and nazi-germany names czechoslovakia, so the land is claimed twice (cross_checks).

- Area: page none km2 (-), resolved 37935 km2, ratio n/a.
- Spot checks: /ledger/0 and /ledger/1 confirmed ('German occupation: 15 March 1939'); /ledger/2 and /ledger/3 confirmed ('German surrender: 8 May 1945'; 'came to an end with the surrender of Germany to the Allies in May 1945'); /keyframe_review/0 confirmed: no area on the page (author says so); resolved 37,935 km2

## saar-basin-territory: pass

Both transfers mirrored (weimar-republic /ledger/7, nazi-germany /ledger/1). Rulers left empty although the page lists the Commission chairmen; optional.

- Area: page none km2 (-), resolved 2782 km2, ratio n/a.
- Spot checks: /ledger/0 confirmed ('Treaty of Versailles took effect: 10 January 1920'); /ledger/1 confirmed ('On 1 March, Germany re-integrated the region'; 'Disestablished: 1 March 1935'); /keyframe_review/0 confirmed ('closely corresponds with the modern German state of Saarland, but was slightly smaller'); no infobox area

## memel-territory: pass

The 30 km circle resolves to 9 land cells (2,276 km2), not the 2,800 km2 the note quotes (geometric circle); the misfit is acknowledged and a 'Memelland' region requested.

- Area: page 2657 km2 (1920), resolved 2276 km2, ratio 0.86.
- Spot checks: /ledger/0 and /ledger/1 confirmed ('the French took over the temporary military administration of the region on 15 February 1920'); /ledger/5 confirmed ('On 19 January, the territory was annexed by Lithuania'); /ledger/2 confirmed ('Klaipėda Revolt: 10–15 January 1923'; body: 'On 9 January 1923 ... Lithuania occupied the territory'); /keyframe_review/0 confirmed (infobox 2,657 km2)

## italian-social-republic: pass

Tried: dates, the Operational Zones footnote ('Both OZAV and OZAK were still formally part of the RSI', flagged), Rome 10 September 1943, capital (page: 'Salò, Verona, and Milan (de facto)'). Southern Lazio and Abruzzo left out and acknowledged. kingdom-of-italy lacks the 1944 gains (cross_checks, eu-13).

- Area: page none km2 (-), resolved 142383 km2, ratio n/a.
- Spot checks: /ledger/0 confirmed ('The Italian Social Republic was proclaimed on 23 September 1943'); /ledger/2 confirmed ('The American forces took possession of Rome on 4 June 1944'); /ledger/3 confirmed ('succeeded in capturing it on 18 July'); /ledger/6 confirmed (final offensive 9 April 1945; 'On 21 April, Bologna was entered'); /ledger/8 confirmed ('held office from 23 September 1943 until 25 April 1945')

## general-government: thin

- Gap /ledger/3: Date and taker of the loss of the Lublin district and the Subcarpathian land (about 45,000 km2) at confidence 1; the counterpart republic-of-poland starts only in 1945-1, so the 1944 taker should be polish-committee-of-national-liberation (the author's own counterparts_needing_dossiers entry, eu-22). Page to try: https://en.wikipedia.org/wiki/Lublin–Brest_offensive
- Area: page 94000 km2 (1939), resolved 97114 km2, ratio 1.03.
- Spot checks: /ledger/0 confirmed ('Establishment: 26 October 1939'); 94,000 km2 confirmed on https://en.wikipedia.org/wiki/German-occupied_Poland; /ledger/2 confirmed ('Galicia added: 1 August 1941'); /ledger/5 confirmed ('USSR captures Warsaw: 17 January 1945'; 'Disintegration: 19 January 1945'); /identity/capitals confirmed ('Litzmannstadt (12 October – 4 November 1939) Krakau (4 November 1939 – 19 January 1945)')

## reichskommissariat-ukraine: thin

Minor: keyframe 1 (from 1943) is the year-end 1943 shape and keyframe 2 (1944) is identical; the 1943 losses carry the months, so left as is.

- Gap /ledger/4: Poltava oblast loss dated 1943-9 at confidence 1 (no page date). Page to try: https://en.wikipedia.org/wiki/Battle_of_the_Dnieper
- Gap /ledger/14: Vinnytsia, Khmelnytskyi, Mykolaiv and Kherson oblasts (about 100,000 km2) lost 1944-4 at confidence 1; the Dnieper–Carpathian page dates the sub-offensives (Proskurov–Chernovtsy, Uman–Botoșani, Bereznegovatoye–Snigirevka, Odessa: 4 March - 17 April 1944) but no captures, so the month may be March. Page to try: https://en.wikipedia.org/wiki/Uman–Botoșani_offensive
- Area: page 340000 km2 (1941), resolved 353301 km2, ratio 1.04.
- Spot checks: /ledger/0 confirmed ('On 20 August, Hitler established the Reichskommissariat Ukraine'); /ledger/2 confirmed ('transfer to civil administration in September 1942'); /ledger/10 confirmed ('Korosten fell on December 29, and Zhitomir followed on December 31'); /ledger/16 confirmed ('On 28 July 1944, the Red Army occupied the last part of the Reichskommissariat Ukraine in Brest'); /ledger/18 confirmed ('officially dissolved on 10 November 1944')

## reichskommissariat-ostland: pass

- Gap /ledger/9 and /ledger/10: West Lithuania (Samogitia) loss and end of the Lithuanian contest dated 1944-10 at confidence 1 (Memel offensive, 5-22 October 1944, not opened). Page to try: https://en.wikipedia.org/wiki/Baltic_offensive
- Area: page none km2 (-), resolved 282995 km2, ratio n/a.
- Spot checks: /ledger/0 confirmed ('Implement civil administration: 25 July 1941 at 12:00'); /ledger/2 confirmed ('Estonia added: 5 December 1941'); /ledger/3 confirmed ('On 1 April 1944, Generalbezirk Weißruthenien was detached', 'placed directly under the Reich Ministry for the Occupied Eastern Territories'); /ledger/5 confirmed ('lost when the city fell on 13 July'); /ledger/7 confirmed (Tallinn offensive 17–26 September 1944, 'to drive German forces from mainland Estonia'); /ledger/8 confirmed ('Soviets reoccupied Riga: 13 October 1944'); /ledger/13 confirmed ('held out in the Courland Pocket until 10 May 1945')

## territory-of-the-military-commander-in-serbia: pass

Who took Serbia in October 1944 differs between yugoslavia, yugoslav-partisans and this dossier (cross_checks); not this dossier's error.

- Area: page none km2 (-), resolved 60443 km2, ratio n/a.
- Spot checks: /ledger/0 confirmed ('On 22 April 1941, the Territory was placed under the supreme authority of the German Military Commander in Serbia'); extent 'most of modern central Serbia, along with the northern part of Kosovo and the Banat' confirmed; /ledger/2 confirmed ('Partisan arrival in Užice: 28 July 1941'; the page also has 'Fall of Užice: 24 September 1941'); /ledger/3 confirmed ('Puppet regime established: 29 August 1941'); /ledger/4 confirmed ('Conquered: 1 December 1941'); /ledger/6 confirmed ('Territory liberated: 20 October 1944'; administration 'evacuated from Serbia to Vienna in October 1944')

## italian-governorate-of-montenegro: fix

No loss before the dissolve: the land goes to the successor yugoslav-partisans by the dissolve; yugoslavia /ledger/20 books the gain from this dossier instead (cross_checks).

- Finding /keyframe_review/0/correction (and the same spec in /identity/predecessors/0/land, /identity/successors/0/land, /ledger/0, 1, 4, 5, 6, 7, /wars/0/zones/0) (applied by the reviewer): The shape subtracted only the Kotor bay and Plav, although the page's same sentence also lists 'the town of Ulcinj' (and a strip north of Lake Scutari, an area northeast of Podgorica, and 'including Bar') as lost to Albania. Evidence: https://en.wikipedia.org/wiki/Italian_governorate_of_Montenegro: 'Montenegro lost Metohija to Albania, including Bar', 'a strip of land north of Lake Scutari, the town of Ulcinj, an area northeast of Podgorica' 'and a significant amount of the Andrijevica district including Plav and Gusinje'. Fix: Added {admin1 Ulcinj, Montenegro} to the subtracted union in every copy of the spec (now about 11,400 km2), added Ulcinj to the region text, and wrote into the keyframe note that the strip, the area northeast of Podgorica and the Bar clause stay in the shape (no gazetteer unit; Bar unclear). Re-validated: OK.
- Area: page none km2 (-), resolved 11380 km2, ratio n/a.
- Spot checks: /ledger/1 confirmed ('Italian occupation: 18 April 1941'); /ledger/3 confirmed ('Governorate established: 3 October 1941'); /ledger/5 confirmed ('German occupation: 12 September 1943'); /ledger/6 confirmed ('German forces which withdrew in December 1944'); /keyframe_review/0 region incomplete (Ulcinj); fixed

## hellenic-state: fix

The found and 1944 loss counterpart kingdom-of-greece has no life before 1945 and first-hellenic-republic ends 1940-10 (cross_checks, eu-18/eu-22).

- Finding /keyframe_review/0/correction and /keyframe_review/1/correction (and the same spec in /identity/predecessors/0/land, /identity/successors/0/land, /ledger/0, 7, 10, 11, /wars/0/zones/0) (applied by the reviewer): country Greece (Natural Earth, modern) includes the Dodecanese (9 cells, about 2,300 km2), which were Italian in 1941-1943 and German-held after, so the shape overlapped the Italian possession; the keyframe note said the Dodecanese 'are not in Greece's modern boundaries' and the notes field said they were outside the shape. Evidence: Resolved with history/tools/gazetteer.py: intersect(country Greece, region Dodecanese) = 9 cells inside the 437-cell shape. https://en.wikipedia.org/wiki/Dodecanese: 'Italy formally annexed the Dodecanese' under the Treaty of Lausanne; 'they were formally united with Greece by the 1947 Peace Treaty with Italy'. Fix: Added {region Dodecanese} to the subtracted union in every 'Greece minus' spec (9 copies), corrected both keyframe notes (now about 108,200 and 95,300 km2) and added the Dodecanese page to sources. Re-validated: OK.
- Area: page none km2 (-), resolved 108241 km2, ratio n/a.
- Spot checks: /ledger/3 confirmed ('Bulgaria officially annexed the occupied territories on 14 May 1941'; 'eastern Macedonia and most of Western Thrace'); /ledger/5 and /ledger/6 confirmed ('After the Italian armistice in September 1943, the Italian zone was taken over by the Germans'); /ledger/8 confirmed ('German troops evacuated Athens on 12 October 1944'); /ledger/9 page says Crete was 'surrendered to the Allies by German garrisons in May and June 1945'; the 1944-10 end at confidence 2 is forced by the state's end and said in the note: accepted

## operational-zone-of-the-adriatic-littoral: fix

- Finding /keyframe_review/0/correction (and the same spec in /identity/predecessors/0/land, /identity/successors/0/land, /ledger/0-3) (applied by the reviewer): The shape used the modern Udine province, which leaves out Pordenone (about 2,300 km2), part of the 1943 Province of Udine; neither this zone nor the italian-social-republic drew Pordenone, a hole in Friuli 1943-1945. Evidence: https://en.wikipedia.org/wiki/Operational_Zone_of_the_Adriatic_Littoral: the Province of Udine (Central and Western Friuli) comprises 'today the provinces of Udine and Pordenone'; resolver: Pordenone's 9 cells were in neither shape. nazi-germany /ledger/50 includes Pordenone in the zone. Fix: Added {admin1 Pordenone, Italy} after Udine in all 7 copies of the spec, noted it in the region text and the keyframe note (area now about 19,500 km2, not the 21,000 km2 the note quoted). Re-validated: OK.
- Area: page none km2 (-), resolved 19473 km2, ratio n/a.
- Spot checks: /ledger/0 confirmed ('established, with its headquarters in Trieste, on 10 September 1943'; the six provinces); /ledger/1 confirmed ('attached to the Gau of Carinthia'); /ledger/2 confirmed (surrender to the New Zealand 2nd Division on 2 May; Partisans withdrew west of the Isonzo from 15 May)

## operational-zone-of-the-alpine-foothills: pass

- Area: page none km2 (-), resolved 16944 km2, ratio n/a.
- Spot checks: /ledger/0 confirmed ('OZAV was established on 10 September 1943'; 'provinces of Belluno, Bolzano and Trento'); /ledger/1 confirmed ('administered as part of the Reichsgau of Tirol-Vorarlberg'; Hofer); /ledger/2 confirmed at confidence 2 (no end day on the page; '41 people killed at Bolzano on 3 May 1945')

## Cross-dossier matrix

82 territorial events checked: 11 matched, 13 missing, 57 mismatch, 1 exception.

- missing: slovak-republic /ledger/6 1944 occupation_start (cp nazi-germany) -> none. nazi-germany has no occupation_start cp slovak-republic for 1944 (it records vassal_start 1939-3 /ledger/5 to vassal_end 1945-5 /ledger/85); route to the nazi-germany owner (eu-21-c).
- missing: slovak-republic /ledger/8 1945 occupation_end (cp nazi-germany) -> none. as above: no occupation_end cp slovak-republic in nazi-germany.
- missing: nazi-germany /ledger/5 1939 vassal_start (cp slovak-republic) -> none. slovak-republic has no vassal_start/vassal_end with nazi-germany (author chose not to repeat it); finding /ledger in slovak-republic, back to eu-21-x.
- missing: nazi-germany /ledger/85 1945 vassal_end (cp slovak-republic) -> none. as above.
- exception: czechoslovakia /ledger/13 1945 gain (cp slovak-republic) -> slovak-republic /ledger/9 1945 dissolve. slovak-republic ends by dissolve with successor czechoslovakia (land passes by identity.successors); no loss event, accepted.
- mismatch: protectorate-of-bohemia-and-moravia /ledger/0 1939 found (cp czechoslovakia) -> czechoslovakia /ledger/10 1939 occupation_start. czechoslovakia has no split/loss cp protectorate-of-bohemia-and-moravia: it keeps Bohemia and Moravia as its own land occupied by nazi-germany 1939-1945, so the Czech lands are claimed twice. Orchestrator to decide the model; then czechoslovakia (eu-21-a) adds split 1939-3 and gain 1945-5 cp protectorate, or the protectorate dossier is dropped.
- mismatch: protectorate-of-bohemia-and-moravia /ledger/1 1939 occupation_start (cp nazi-germany) -> nazi-germany /ledger/4 1939 occupation_start. nazi-germany names the occupied party czechoslovakia, not the protectorate.
- mismatch: protectorate-of-bohemia-and-moravia /ledger/2 1945 occupation_end (cp nazi-germany) -> nazi-germany /ledger/84 1945 occupation_end. as above.
- missing: memel-territory /ledger/1 1920 occupation_start (cp french-third-republic) -> none. french-third-republic (eu-20) has no occupation_start cp memel-territory for 1920-2; route to its owner.
- missing: memel-territory /ledger/4 1923 occupation_end (cp french-third-republic) -> none. french-third-republic has no occupation_end cp memel-territory for 1923-1.
- mismatch: italian-social-republic /ledger/1 1943 occupation_start (cp nazi-germany) -> nazi-germany /ledger/49 1943 occupation_start. nazi-germany names the occupied party kingdom-of-italy (author flagged).
- mismatch: italian-social-republic /ledger/2 1944 loss (cp kingdom-of-italy) -> kingdom-of-italy /ledger/40 1945 gain. kingdom-of-italy (eu-13) has no 1944 gain of Rome; its only gain from the RSI is the whole north in 1945 at confidence 1.
- mismatch: italian-social-republic /ledger/3 1944 loss (cp kingdom-of-italy) -> kingdom-of-italy /ledger/40 1945 gain. kingdom-of-italy (eu-13) has no 1944 gain of Ancona; its only gain from the RSI is the whole north in 1945 at confidence 1.
- mismatch: italian-social-republic /ledger/4 1944 loss (cp kingdom-of-italy) -> kingdom-of-italy /ledger/40 1945 gain. kingdom-of-italy (eu-13) has no 1944 gain of Umbria, Marche, Tuscany; its only gain from the RSI is the whole north in 1945 at confidence 1.
- mismatch: italian-social-republic /ledger/7 1945 occupation_end (cp nazi-germany) -> nazi-germany /ledger/86 1945 occupation_end. counterpart named kingdom-of-italy in nazi-germany.
- mismatch: general-government /ledger/1 1939 occupation_start (cp nazi-germany) -> nazi-germany /ledger/11 1939 occupation_start. nazi-germany names the occupied party second-polish-republic (which ends 1939-10).
- mismatch: general-government /ledger/2 1941 gain (cp ukrainian-soviet-socialist-republic) -> ukrainian-soviet-socialist-republic /ledger/38 1941 occupation_start. the Ukrainian SSR records German occupation of Lviv, Ivano-Frankivsk and Ternopil from 1941-6, not a loss to the General Government.
- mismatch: general-government /ledger/3 1944 loss (cp republic-of-poland) -> republic-of-poland /ledger/0 1945 found. republic-of-poland starts 1945-1, so it cannot gain in 1944-7; use polish-committee-of-national-liberation (no dossier, eu-22; the author listed it) or start republic-of-poland in 1944.
- mismatch: general-government /ledger/4 1944 loss (cp ukrainian-soviet-socialist-republic) -> ukrainian-soviet-socialist-republic /ledger/45 1944 occupation_end. Ukrainian SSR ends the occupation in 1944-10 with counterpart nazi-germany.
- mismatch: general-government /ledger/5 1945 occupation_end (cp nazi-germany) -> nazi-germany /ledger/68 1945 occupation_end. counterpart named second-polish-republic in nazi-germany.
- mismatch: general-government /ledger/6 1945 loss (cp republic-of-poland) -> republic-of-poland /ledger/0 1945 found. republic-of-poland founds 1945-1 from nazi-germany, not from the General Government.
- mismatch: reichskommissariat-ukraine /ledger/0 1941 found (cp ukrainian-soviet-socialist-republic) -> ukrainian-soviet-socialist-republic /ledger/38 1941 occupation_start. the Ukrainian SSR records occupation by nazi-germany (1941-6, 1941-10), no loss to the Reichskommissariat.
- mismatch: reichskommissariat-ukraine /ledger/1 1941 occupation_start (cp nazi-germany) -> nazi-germany /ledger/32 1941 occupation_start. nazi-germany names the Ukrainian SSR; it also draws the same land from Cliopatria 1942 (double drawing, author flagged).
- missing: reichskommissariat-ukraine /ledger/2 1942 gain (cp nazi-germany) -> none. nazi-germany has no loss cp reichskommissariat-ukraine for the September 1942 transfer of Taurien (an internal transfer; accept or add).
- mismatch: reichskommissariat-ukraine /ledger/4 1943 loss (cp ukrainian-soviet-socialist-republic) -> ukrainian-soviet-socialist-republic /ledger/43 1943 occupation_end. the Ukrainian SSR records occupation_end with counterpart nazi-germany (1943-11 east, 1944-10 west), not gains from the Reichskommissariat; USSR /ledger/31 gains Kyiv 1943-11 from nazi-germany.
- mismatch: reichskommissariat-ukraine /ledger/5 1943 loss (cp ukrainian-soviet-socialist-republic) -> ukrainian-soviet-socialist-republic /ledger/43 1943 occupation_end. the Ukrainian SSR records occupation_end with counterpart nazi-germany (1943-11 east, 1944-10 west), not gains from the Reichskommissariat; USSR /ledger/31 gains Kyiv 1943-11 from nazi-germany.
- mismatch: reichskommissariat-ukraine /ledger/6 1943 loss (cp ukrainian-soviet-socialist-republic) -> ukrainian-soviet-socialist-republic /ledger/43 1943 occupation_end. the Ukrainian SSR records occupation_end with counterpart nazi-germany (1943-11 east, 1944-10 west), not gains from the Reichskommissariat; USSR /ledger/31 gains Kyiv 1943-11 from nazi-germany.
- mismatch: reichskommissariat-ukraine /ledger/7 1943 loss (cp ukrainian-soviet-socialist-republic) -> ukrainian-soviet-socialist-republic /ledger/43 1943 occupation_end. the Ukrainian SSR records occupation_end with counterpart nazi-germany (1943-11 east, 1944-10 west), not gains from the Reichskommissariat; USSR /ledger/31 gains Kyiv 1943-11 from nazi-germany.
- mismatch: reichskommissariat-ukraine /ledger/10 1943 loss (cp ukrainian-soviet-socialist-republic) -> ukrainian-soviet-socialist-republic /ledger/45 1944 occupation_end. the Ukrainian SSR records occupation_end with counterpart nazi-germany (1943-11 east, 1944-10 west), not gains from the Reichskommissariat; USSR /ledger/31 gains Kyiv 1943-11 from nazi-germany.
- mismatch: reichskommissariat-ukraine /ledger/11 1944 loss (cp ukrainian-soviet-socialist-republic) -> ukrainian-soviet-socialist-republic /ledger/45 1944 occupation_end. the Ukrainian SSR records occupation_end with counterpart nazi-germany (1943-11 east, 1944-10 west), not gains from the Reichskommissariat; USSR /ledger/31 gains Kyiv 1943-11 from nazi-germany.
- mismatch: reichskommissariat-ukraine /ledger/12 1944 loss (cp ukrainian-soviet-socialist-republic) -> ukrainian-soviet-socialist-republic /ledger/45 1944 occupation_end. the Ukrainian SSR records occupation_end with counterpart nazi-germany (1943-11 east, 1944-10 west), not gains from the Reichskommissariat; USSR /ledger/31 gains Kyiv 1943-11 from nazi-germany.
- mismatch: reichskommissariat-ukraine /ledger/13 1944 loss (cp ukrainian-soviet-socialist-republic) -> ukrainian-soviet-socialist-republic /ledger/45 1944 occupation_end. the Ukrainian SSR records occupation_end with counterpart nazi-germany (1943-11 east, 1944-10 west), not gains from the Reichskommissariat; USSR /ledger/31 gains Kyiv 1943-11 from nazi-germany.
- mismatch: reichskommissariat-ukraine /ledger/14 1944 loss (cp ukrainian-soviet-socialist-republic) -> ukrainian-soviet-socialist-republic /ledger/45 1944 occupation_end. the Ukrainian SSR records occupation_end with counterpart nazi-germany (1943-11 east, 1944-10 west), not gains from the Reichskommissariat; USSR /ledger/31 gains Kyiv 1943-11 from nazi-germany.
- mismatch: reichskommissariat-ukraine /ledger/16 1944 loss (cp byelorussian-soviet-socialist-republic) -> byelorussian-soviet-socialist-republic /ledger/16 1944 occupation_end. Byelorussian SSR ends the occupation in 1944 with counterpart nazi-germany.
- mismatch: reichskommissariat-ukraine /ledger/17 1944 occupation_end (cp nazi-germany) -> nazi-germany /ledger/55 1944 occupation_end. counterpart named the Ukrainian SSR in nazi-germany.
- mismatch: reichskommissariat-ostland /ledger/0 1941 found (cp union-of-soviet-socialist-republics) -> union-of-soviet-socialist-republics /ledger/21 1941 loss. USSR loses the Baltic and Belarus to nazi-germany (1941-7); no loss cp reichskommissariat-ostland.
- mismatch: reichskommissariat-ostland /ledger/1 1941 occupation_start (cp nazi-germany) -> nazi-germany /ledger/35 1941 occupation_start. nazi-germany records occupation of the Lithuanian, Latvian, Estonian and Byelorussian SSRs (/ledger/33, 35-37), not of Ostland; double drawing with Cliopatria 1942 (author flagged).
- mismatch: reichskommissariat-ostland /ledger/2 1941 gain (cp estonian-soviet-socialist-republic) -> estonian-soviet-socialist-republic /ledger/1 1941 occupation_start. Estonian SSR records occupation by nazi-germany from 1941-7, no loss cp Ostland.
- missing: reichskommissariat-ostland /ledger/3 1944 loss (cp nazi-germany) -> none. nazi-germany has no gain cp reichskommissariat-ostland for the 1 April 1944 detachment of Weissruthenien (it keeps Belarus as occupied, /ledger/33).
- mismatch: reichskommissariat-ostland /ledger/5 1944 loss (cp lithuanian-soviet-socialist-republic) -> lithuanian-soviet-socialist-republic /ledger/2 1944 occupation_end. Lithuanian SSR ends the occupation in 1944-10 with counterpart nazi-germany.
- mismatch: reichskommissariat-ostland /ledger/6 1944 loss (cp lithuanian-soviet-socialist-republic) -> lithuanian-soviet-socialist-republic /ledger/2 1944 occupation_end. Lithuanian SSR ends the occupation in 1944-10 with counterpart nazi-germany.
- mismatch: reichskommissariat-ostland /ledger/9 1944 loss (cp lithuanian-soviet-socialist-republic) -> lithuanian-soviet-socialist-republic /ledger/2 1944 occupation_end. Lithuanian SSR ends the occupation in 1944-10 with counterpart nazi-germany.
- mismatch: reichskommissariat-ostland /ledger/7 1944 loss (cp estonian-soviet-socialist-republic) -> estonian-soviet-socialist-republic /ledger/2 1944 occupation_end. Estonian SSR ends the occupation in 1944 with counterpart nazi-germany.
- mismatch: reichskommissariat-ostland /ledger/12 1944 loss (cp estonian-soviet-socialist-republic) -> estonian-soviet-socialist-republic /ledger/2 1944 occupation_end. Estonian SSR ends the occupation in 1944 with counterpart nazi-germany.
- mismatch: reichskommissariat-ostland /ledger/8 1944 loss (cp latvian-soviet-socialist-republic) -> latvian-soviet-socialist-republic /ledger/3 1945 occupation_end. Latvian SSR ends the occupation in 1945 (no month) with counterpart nazi-germany; Riga fell 1944-10.
- mismatch: reichskommissariat-ostland /ledger/14 1945 occupation_end (cp nazi-germany) -> nazi-germany /ledger/89 1945 occupation_end. counterpart named the Latvian SSR in nazi-germany.
- mismatch: territory-of-the-military-commander-in-serbia /ledger/1 1941 occupation_start (cp nazi-germany) -> nazi-germany /ledger/26 1941 occupation_start. nazi-germany names the occupied party yugoslavia.
- mismatch: territory-of-the-military-commander-in-serbia /ledger/5 1944 loss (cp yugoslav-partisans) -> yugoslav-partisans /ledger/9 1944 gain. three dossiers disagree: yugoslavia /ledger/22 gains Serbia 1944-10 from this territory; yugoslav-partisans gains Belgrade 1944-10 and Serbia 1944-12 from nazi-germany (/ledger/9-10). Route to eu-21-a/e owners to agree on one taker.
- mismatch: territory-of-the-military-commander-in-serbia /ledger/6 1944 occupation_end (cp nazi-germany) -> nazi-germany /ledger/67 1945 occupation_end. nazi-germany ends the occupation of Serbia in 1945-1 (counterpart yugoslavia); the page has Territory liberated: 20 October 1944.
- mismatch: italian-governorate-of-montenegro /ledger/1 1941 occupation_start (cp kingdom-of-italy) -> kingdom-of-italy /ledger/26 1941 occupation_start. kingdom-of-italy names the occupied party yugoslavia.
- mismatch: italian-governorate-of-montenegro /ledger/4 1943 occupation_end (cp kingdom-of-italy) -> kingdom-of-italy /ledger/35 1943 occupation_end. as above.
- missing: italian-governorate-of-montenegro /ledger/5 1943 occupation_start (cp nazi-germany) -> none. nazi-germany has no occupation of Montenegro (1943-9 to 1944-12); it has Albania only (/ledger/51, 65). Route to eu-21-c.
- missing: italian-governorate-of-montenegro /ledger/6 1944 occupation_end (cp nazi-germany) -> none. as above.
- mismatch: yugoslavia /ledger/20 1944 gain (cp italian-governorate-of-montenegro) -> italian-governorate-of-montenegro /ledger/7 1944 dissolve. the governorate dissolves to its successor yugoslav-partisans, whose /ledger/7 gains Montenegro from nazi-germany; yugoslavia and yugoslav-partisans should agree on the taker.
- mismatch: hellenic-state /ledger/0 1941 found (cp kingdom-of-greece) -> first-hellenic-republic /ledger/38 1940 dissolve. kingdom-of-greece (eu-22) starts in 1945, first-hellenic-republic (eu-18) ends 1940-10: no Greek dossier holds 1940-10 to 1945, and kingdom-of-italy and principality-of-bulgaria name first-hellenic-republic as the occupied party in 1941-1944. Route to eu-18/eu-22.
- mismatch: hellenic-state /ledger/1 1941 occupation_start (cp nazi-germany) -> nazi-germany /ledger/29 1941 occupation_start. nazi-germany names kingdom-of-greece.
- mismatch: hellenic-state /ledger/2 1941 occupation_start (cp kingdom-of-italy) -> kingdom-of-italy /ledger/27 1941 occupation_start. kingdom-of-italy names first-hellenic-republic.
- mismatch: hellenic-state /ledger/3 1941 loss (cp principality-of-bulgaria) -> principality-of-bulgaria /ledger/32 1941 occupation_start. Bulgaria records occupation (not a gain) from 1941-4, counterpart first-hellenic-republic; the Axis page says Bulgaria officially annexed the land on 14 May 1941 (eu-18 to add a gain or this dossier to use occupation).
- mismatch: hellenic-state /ledger/4 1941 occupation_start (cp nazi-germany) -> nazi-germany /ledger/29 1941 occupation_start. Crete is inside nazi-germany's single Greek occupation.
- mismatch: hellenic-state /ledger/5 1943 occupation_end (cp kingdom-of-italy) -> kingdom-of-italy /ledger/36 1943 occupation_end. counterpart first-hellenic-republic.
- missing: hellenic-state /ledger/6 1943 occupation_start (cp nazi-germany) -> none. nazi-germany has no 1943-9 occupation_start for the former Italian zone of Greece.
- mismatch: hellenic-state /ledger/7 1944 occupation_end (cp nazi-germany) -> nazi-germany /ledger/83 1945 occupation_end. nazi-germany ends its Greek occupation in 1945-5 (Crete held to May 1945); this dossier closes all in 1944-10 because its life ends.
- mismatch: hellenic-state /ledger/8 1944 occupation_end (cp nazi-germany) -> nazi-germany /ledger/83 1945 occupation_end. nazi-germany ends its Greek occupation in 1945-5 (Crete held to May 1945); this dossier closes all in 1944-10 because its life ends.
- mismatch: hellenic-state /ledger/9 1944 occupation_end (cp nazi-germany) -> nazi-germany /ledger/83 1945 occupation_end. nazi-germany ends its Greek occupation in 1945-5 (Crete held to May 1945); this dossier closes all in 1944-10 because its life ends.
- mismatch: hellenic-state /ledger/10 1944 loss (cp kingdom-of-greece) -> kingdom-of-greece /ledger/0 1945 found. kingdom-of-greece founds in 1945 from first-hellenic-republic, not from the hellenic-state; within one year but different counterpart.
- missing: operational-zone-of-the-adriatic-littoral /ledger/0 1943 found (cp kingdom-of-italy) -> none. kingdom-of-italy has no loss cp operational-zone-of-the-adriatic-littoral (its 1943-9 losses go to italian-social-republic and nazi-germany); route to eu-13.
- mismatch: operational-zone-of-the-adriatic-littoral /ledger/1 1943 occupation_start (cp nazi-germany) -> nazi-germany /ledger/50 1943 occupation_start. nazi-germany records the two zones as occupation of kingdom-of-italy (one event, Udine to Trento).
- mismatch: operational-zone-of-the-adriatic-littoral /ledger/2 1945 occupation_end (cp nazi-germany) -> nazi-germany /ledger/87 1945 occupation_end. as above.
- missing: operational-zone-of-the-alpine-foothills /ledger/0 1943 found (cp kingdom-of-italy) -> none. kingdom-of-italy has no loss cp operational-zone-of-the-alpine-foothills (its 1943-9 losses go to italian-social-republic and nazi-germany); route to eu-13.
- mismatch: operational-zone-of-the-alpine-foothills /ledger/1 1943 occupation_start (cp nazi-germany) -> nazi-germany /ledger/50 1943 occupation_start. nazi-germany records the two zones as occupation of kingdom-of-italy (one event, Udine to Trento).
- mismatch: operational-zone-of-the-alpine-foothills /ledger/2 1945 occupation_end (cp nazi-germany) -> nazi-germany /ledger/87 1945 occupation_end. as above.

## Problems for the orchestrator

- Model conflict for the orchestrator: the Protectorate, General Government and both Reichskommissariats are drawn as states while nazi-germany draws the same land as occupation of czechoslovakia, second-polish-republic and the Soviet republics (and from Cliopatria's 1942 shape), and czechoslovakia keeps the Czech lands as its own occupied land; every occupation and Soviet-side mirror of these four dossiers is a counterpart mismatch (57 mismatches in cross_checks). One convention has to be chosen and applied to nazi-germany (eu-21-c), czechoslovakia (eu-21-a), the Soviet republics and these dossiers.
- No Greek state dossier covers 1940-10 to 1945: first-hellenic-republic (eu-18) ends 1940, kingdom-of-greece (eu-22) starts 1945, and the occupiers name either; hellenic-state uses kingdom-of-greece.
- Three reviewer edits applied to the mount (italian-governorate-of-montenegro, hellenic-state, operational-zone-of-the-adriatic-littoral), each re-validated and read back unchanged after about 14 seconds.
- No page failed to load.

## Gazetteer names wanted

Sobrance (place, slovak-republic), Orava (region, slovak-republic), Spiš (region, slovak-republic), Memelland (region, memel-territory), Zichenau (region, general-government), Kvarner (region, operational-zone-of-the-adriatic-littoral), Province of Ljubljana (region, operational-zone-of-the-adriatic-littoral), Tuzi (place, italian-governorate-of-montenegro).
