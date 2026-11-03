# Review of batch eu-22-c

Reviewer run 2026-11-01 (brief filled 2026-10-31). Validator: all six dossiers valid; warnings only for the comoros counterpart and the open Turkish occupation of northern Cyprus. Neighbour dossiers read: every Context polity with a file (union-of-soviet-socialist-republics, kingdom-of-great-britain, united-kingdom, netherlands, people-s-democratic-republic-of-algeria, republic-of-tunisia, the af-08 West African states, west-berlin, allied-occupied-germany, saar-protectorate, nazi-germany, french-fourth-republic, republic-of-turkey). Not yet written (allowed exception): hungary, turkish-republic-of-northern-cyprus, socialist-federal-republic-of-yugoslavia, socialist-republic-of-romania, republic-of-lithuania, republic-of-belarus, slovakia, republic-of-brazil.

## german-democratic-republic: pass

Tried: mirror of all four events (allied-occupied-germany dissolve 1949-10, federated-republic-of-germany gain 1990-10, federal-republic-of-germany merge 1990-10 all present), keyframe areas (five shapes within 0.7 %, the 1973 blip acknowledged as noise), capital inside bbox, war with empty zones explained, certainty covering 1949-1990. Could not break it.

Area: infobox 108,333 km2 (no year) against Cliopatria 112,473 km2, ratio 1.04. infobox gives no year; compared with the 1953-1972 and 1976-1990 shape

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/East_Germany: confirmed: 'On 7 October 1949 the SED established the German Democratic Republic'
- `/ledger/1` https://en.wikipedia.org/wiki/East_Germany: confirmed: 'The GDR ceased to exist when its five states ("Länder") joined the Federal Republic of Germany'; 'its capital East Berlin united with West Berlin on 3 October 1990'
- `/ledger/3` https://en.wikipedia.org/wiki/East_Germany: confirmed: infobox 'Reunification: 3 October 1990'
- `/identity/rulers` https://en.wikipedia.org/wiki/East_Germany: confirmed: infobox list '1949–1971: Walter Ulbricht', '1971–1989: Erich Honecker', '1989: Egon Krenz', '1989–1990: Hans Modrow' (unlabelled, as the author said)

## federal-republic-of-germany: thin

Events, dates and areas hold; shape switches one year late on both ends are correctly marked adjust. Only gap: the 1963 Dutch return, missing on this side of the netherlands ledger.

Area: infobox 248,717 km2 (no year) against Cliopatria 247,306 km2, ratio 0.99.

Gaps for a gap-filler:
- `/ledger (after /ledger/1)` gain 1963-08 from netherlands: Elten, Selfkant and Suderwick returned to West Germany on 1 August 1963 (Treaty of The Hague, 8 April 1960); the netherlands dossier has the loss at /ledger/20 (confidence 3) with counterpart federal-republic-of-germany and no mirror here. The West Germany page is silent (checked), so this is a page-budget gap (budget 1-2 pages, 2 used). Page to try: https://en.wikipedia.org/wiki/Dutch_annexation_of_German_territory_after_World_War_II

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/West_Germany: confirmed: 'from its formation on 23 May 1949 until its reunification with East Germany on 3 October 1990'
- `/ledger/1` https://en.wikipedia.org/wiki/Saar_(protectorate): confirmed: 'On 27 October 1956 the Saar Treaty established that Saarland should be allowed to become a state of West Germany ... and so Saarland did on 1 January 1957'
- `/ledger/3` https://en.wikipedia.org/wiki/West_Germany: confirmed: reunification 3 October 1990
- `/keyframe_review/0/note` https://en.wikipedia.org/wiki/West_Germany: confirmed: infobox 248,717 km2, no year; West Berlin 'formally under the sovereignty of the Western Allies and separate from West Germany'

## hungarian-people-s-republic: pass

Tried: the 1949 and 1956-57 new keyframes (both real Cliopatria gaps, correctly filled), the contest zone (towns named on the page), Dunaújváros coordinates (18.94 E 46.97 N, correct), area. The only unmatched mirror is on the Soviet side (USSR ledger has no 1956 event), and hungary (eu-22, not written yet) is an allowed exception. Could not break it.

Area: infobox 93,011 km2 (no year) against Cliopatria 91,985 km2, ratio 0.99.

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Hungarian_People%27s_Republic: confirmed: 'When it was officially promulgated on 20 August, the country was renamed the "Hungarian People's Republic."'
- `/ledger/1` https://en.wikipedia.org/wiki/Hungarian_Revolution_of_1956: confirmed: 'At 02:00 on 24 October 1956, Soviet defence minister Georgy Zhukov ordered the Red Army to occupy Budapest'; zone towns on page: 'in and around the city of Pécs in the Mecsek Mountains', 'the industrial centre of Dunaújváros'
- `/ledger/2` https://en.wikipedia.org/wiki/Hungarian_Revolution_of_1956: confirmed: infobox '23 October – 11 November 1956', 'Soviet victory'; body 'Soviet victory on 10 November' (page inconsistent, as the note says)
- `/ledger/3` https://en.wikipedia.org/wiki/Hungarian_People%27s_Republic: confirmed: 'One of Szűrös' first acts was to officially proclaim the Republic of Hungary'

## republic-of-poland: fail

Dates and areas hold; the 1945 formation does not: the ledger's two land events disagree with nazi-germany (5 losses to Poland in 1945-01/03), the USSR (1945-08 loss to Poland) and the page's own Danzig/Pomerania/Silesia, leaving land in the 1945-1952 keyframe that no event explains.

Area: infobox 312,685 km2 (no year) against Cliopatria 314,574 km2, ratio 1.006.

Findings:
- `/identity/start and /ledger/0` [author] The state starts 1945-06 with a found from second-polish-republic (a state that ended in 1939), but nazi-germany already loses land to republic-of-poland in 1945-01 and 1945-03 and the cited page dates an earlier government. Evidence: Polish People's Republic page: 'On 1 January 1945, the committee was replaced by the Provisional Government of the Republic of Poland' (the author's notes list only 1944, June 1945 and 1947). nazi-germany /ledger/71 (1945-01 Wartheland, conf 2), /ledger/72 (1945-01 Katowice district, conf 3), /ledger/73 (1945-01 Ciechanów, conf 1), /ledger/77 (1945-03 Danzig, conf 3), /ledger/78 (1945-03 Danzig-West Prussia, conf 2) all name republic-of-poland as counterpart; this dossier has no event for any of them and did not exist on those dates. Fix: Start the state at 1945-01 (Provisional Government of the Republic of Poland, 1 January 1945, same page) and take the core by gains from nazi-germany that mirror its /ledger/71-78 (or, if June 1945 is kept, say so in notes and ask eu-21 to retarget the nazi-germany losses); the found counterpart should be the power the land came from, not second-polish-republic.
- `/ledger/0/region` [author] The found region (pre-war Poland inside the 1953 outline) includes the Białystok and Przemyśl areas that the USSR dossier cedes to Poland only in August 1945; no Polish event receives them. Evidence: union-of-soviet-socialist-republics /ledger/50: 1945-08 loss to republic-of-poland, region intersect(Second Polish Republic 1938, USSR 1940, country Poland), 'the Soviet Union returns the Bialystok area to Poland'. Territorial changes of Poland page: 'On August 16, 1945, a border agreement between Poland and the USSR was signed.' As written the two ledgers both hold that land from June to August 1945. Fix: Add gain 1945-08 from union-of-soviet-socialist-republics with the USSR event's region and the Territorial changes of Poland source (already in sources), and remove that land from the found region; or agree with eu-17 that the Soviet loss belongs at the found date.
- `/ledger/1/region` [author] The confidence-3 gain from Germany lists only five voivodeships and omits the former Free City of Danzig, the Pomeranian voivodeship's German part (Słupsk, Lębork, Bytów) and German Upper Silesia (Gliwice, Bytom, Zabrze), which the page names; no event in the ledger brings these lands to Poland although the 1945-1952 keyframe draws them. Evidence: Oder–Neisse line page: the line placed 'the former Free City of Danzig' within Poland in a sentence that also covers Silesia, Pomerania and southern East Prussia; Territorial changes of Poland: 'some 101,000 square kilometres' while the five voivodeships total about 90,400 km2. nazi-germany /ledger/77 loses Danzig to Poland 1945-03 with no Polish mirror. Fix: Write the gained land as {"minus": [{"cliopatria": "Republic of Poland", "year": 1953}, {"cliopatria": "Second Polish Republic", "year": 1939}], "text": "the German territories east of the Oder-Neisse line and the former Free City of Danzig"} (or add the Pomeranian and Silesian parts by name) and add the Danzig gain from nazi-germany at 1945-03 if the state starts before it; tell eu-21/allied-occupied-germany's owner so its /ledger/6 matches.

Gaps for a gap-filler:
- `/keyframe_review/0 and /keyframe_review/1` the 1951 Polish-Soviet territorial exchange (about 480 km2, Ustrzyki Dolne for the Sokal area), dated by none of the pages opened; the 1945-1952 keyframe uses the post-exchange 1953 outline Page to try: https://en.wikipedia.org/wiki/1951_Polish%E2%80%93Soviet_territorial_exchange
- `/ledger` Czechoslovak border corrections (Trstená agreement of 20 May 1945, cut off on the Territorial changes page; Kłodzko, Głubczyce, Racibórz disputes, 1958 treaty) Page to try: https://en.wikipedia.org/wiki/Czech_Republic%E2%80%93Poland_border
- `/identity/rulers` no ruler strip Page to try: https://en.wikipedia.org/wiki/List_of_heads_of_state_of_Poland

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Polish_People%27s_Republic: confirmed for June 1945 ('The Provisional Government of National Unity ... was established in June 1945'), but the same page gives 'On 1 January 1945, the committee was replaced by the Provisional Government of the Republic of Poland' (see fixes)
- `/ledger/1` https://en.wikipedia.org/wiki/Oder%E2%80%93Neisse_line: confirmed date: 'Finally on 2 August 1945, the Potsdam Agreement ... placed the German territories east of the Oder–Neisse line formally under Polish administrative control'; region narrower than the page (Danzig, Pomerania, Silesia)
- `/ledger/2` https://en.wikipedia.org/wiki/Polish_People%27s_Republic: confirmed: infobox 'Capital: Łódź (1947–1949) Warsaw (1949–1989)'
- `/ledger/3` https://en.wikipedia.org/wiki/Polish_People%27s_Republic: confirmed: infobox 'July Constitution: 22 July 1952'
- `/ledger/4` https://en.wikipedia.org/wiki/Polish_People%27s_Republic: confirmed: 'The Parliament amended the Constitution on 29 December 1989'; infobox 'Disestablished: 29 December 1989'
- `/keyframe_review/1/note` https://en.wikipedia.org/wiki/Territorial_changes_of_Poland: confirmed: 'since 1945, a more westerly Poland covers 312,677 km2'; 'gained some 101,000 square kilometres ... in the west and north'

## french-fifth-republic: fix

Decolonisation dates all hold to the month; Algeria correction is right. Applied four small verified fixes; remaining items are cross-group mirrors (af-08) and the Bizerte gap the author flagged.

Area: infobox 643,801 km2 (no year) against Cliopatria 680,260 km2, ratio 1.06. 2024 shape; the 1961-2023 shape (3,029,276 km2, ratio 4.7) holds Algeria and is corrected by the 1963 and 1978 keyframes; the 1958 shape (11,258,064) against the Community infobox '1959: 11,000,000 km2', ratio 1.02

Findings:
- `/ledger/44` [applied by reviewer] Comoros loss was undated (1975, confidence 1) with a note saying the French Community page is silent; the page dates it. Evidence: French Community page chronology: '6 July 1975 – Comorian President Ahmed Abdallah declares the whole archipelago independent of France'; 'the French refuse to recognise the inclusion of Mayotte in the new state'. Fix: month 7, confidence 3, note rewritten with the quotes; the notes field sentence on it updated.
- `/ledger/3 and /ledger/4` [applied by reviewer] Notes said French Cameroun and French Togoland 'enter the French Community as an autonomous state'; the page says they were associated UN trust territories, not members. Evidence: French Community page: 'Associated with the Community were the United Nations trust territories of French Cameroun and French Togoland'. Fix: Notes rewritten to say associated UN trust territory; confidence 2 kept.
- `/ledger/2, /ledger/5 to /ledger/14` [applied by reviewer] Eleven vassal_start events were confidence 3 although the client status is the author's own reading (the author's report says 'page silent on the word client'). Evidence: French Community page gives each date ('becomes an autonomous state within the Community') but no vassal or client relation; brief section 2.7. Fix: confidence lowered to 2 with a reviewer remark in each note.
- `/ledger/42 and /ledger/43` [author] (advisory, non-blocking) The Mers El Kébir base is drawn as a 15 km disc round Oran, which takes in the city of Oran (independent Algeria) as French-held 1962-1967. Evidence: Algerian War page names only 'the naval base of Mers-el-Kebir'; Mers El Kébir lies about 7 km west-north-west of Oran (gazetteer Oran -0.6219, 35.7119). Fix: Centre the disc on Mers El Kébir (about -0.70, 35.73) with km 5; also ask af-08 to add the mirror occupation in people-s-democratic-republic-of-algeria.
- `/ledger/5` [author] (advisory, non-blocking) The 1958-11 vassal_start names mali-federation as counterpart, but the Mali Federation was formed on 4 April 1959; in November 1958 the clients were the Sudanese Republic and Senegal. Evidence: French Community page: '24 November – The French Sudan becomes an autonomous state ... as the Sudanese Republic', '25 November – Senegal becomes an autonomous state', '4 April – Senegal and the Sudanese Republic form a union as the Mali Federation'. The note already says so. Fix: Keep (the validator pairs it with the 1960 vassal_end) or split once af-08 writes Senegal and the Sudanese Republic for 1958-1959.

Gaps for a gap-filler:
- `/ledger (1961-1963)` France's side of the Bizerte base: republic-of-tunisia has contest_start 1961-07, contest_end 1963-10 and gain 1963-10 (Bizerte base) with french-fifth-republic as counterpart; this dossier has no hold, loss or contest for it (author flagged: page budget) Page to try: https://en.wikipedia.org/wiki/Bizerte_crisis
- `/ledger/1` confidence-1 occupation_start of the French sector of Berlin (the west-berlin mirror is confidence 3); a page naming the French sector Page to try: https://en.wikipedia.org/wiki/West_Berlin
- `/ledger/2 to /ledger/14` the 13 vassal_start events (1958-10 to 1958-12) have no mirror: every counterpart dossier (af-08: madagascar, republic-of-cameroon, togo, mali-federation, republic-of-chad, gabon, republic-of-the-congo, mauritania, central-african-republic, republic-of-benin, republic-of-cote-d-ivoire, burkina-faso, republic-of-the-niger) starts in 1960; either af-08 starts them at autonomy with a vassal_start, or this dossier drops the client tint Page to try: https://en.wikipedia.org/wiki/French_Community

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/French_Fifth_Republic: confirmed: 'It was established on 4 October 1958'; infobox 643,801 km2 (no year)
- `/ledger/41` https://en.wikipedia.org/wiki/Algerian_War: confirmed: 'De Gaulle pronounced Algeria an independent country on 3 July'; 'The Provisional Executive, however, proclaimed 5 July'
- `/ledger/43` https://en.wikipedia.org/wiki/Algerian_War: confirmed: 'the last French forces did not leave the naval base of Mers El Kébir until 1967'
- `/ledger/3` https://en.wikipedia.org/wiki/French_Community: not on page: note said Cameroun entered the Community as an autonomous state; page says an associated trust territory (confidence 2; note corrected)
- `/ledger/5` https://en.wikipedia.org/wiki/French_Community: confirmed dates 24/25 November; counterpart anachronistic (federation formed 4 April 1959)
- `/ledger/44` https://en.wikipedia.org/wiki/French_Community: mis-dated (undated at confidence 1): page gives 6 July 1975; fixed

## republic-of-cyprus: fix

All four events confirmed with their months; mirrors in united-kingdom and republic-of-turkey match. The Q229 split from cyprus-condominium is right.

Area: infobox 9,251 km2 (no year) against Cliopatria 11,438 km2, ratio 1.24.

Findings:
- `/ledger/1` [applied by reviewer] contest_start 1974-07 at confidence 3 with the whole north as zone, though the page names only the Kyrenia-Nicosia corridor (3 % of the island) for July. Evidence: Turkish invasion of Cyprus: Turkish forces landed on 20 July and 'captured 3% of the island before a ceasefire was declared'; the second offensive began 14 August. Fix: confidence lowered to 2 with a reviewer remark.
- `/keyframe_review/0-3/correction and /ledger/0/region` [author] (advisory, non-blocking) The two Sovereign Base Area discs are 12 km in radius (about 450 km2 each); the page gives the bases as 2.74 % of the island (about 250 km2 for both), and the Akrotiri disc centred 32.95, 34.62 reaches Limassol (about 10.6 km away). Evidence: Cyprus page: 'Akrotiri and Dhekelia, covering the remaining 2.74%'. The united-kingdom dossier /ledger/29 uses the same 12 km discs, so a one-sided change would leave a gap. Fix: Change both dossiers together to km 6 (or drop the bases as below the grid), coordinated with the united-kingdom owner (eu-11).

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Cyprus: confirmed: 'Cyprus officially attained independence on 16 August 1960'; infobox 9,251 km2
- `/ledger/1` https://en.wikipedia.org/wiki/Turkish_invasion_of_Cyprus: confirmed date: landing 20 July 1974; zone broader than page (confidence lowered)
- `/ledger/2` https://en.wikipedia.org/wiki/Turkish_invasion_of_Cyprus: confirmed: infobox '20 July – 18 August 1974'; second offensive 14 August
- `/ledger/3` https://en.wikipedia.org/wiki/Turkish_invasion_of_Cyprus: confirmed: infobox 'Turkey occupies 36.2% of Cyprus'

## Cross-dossier matrix (unmatched and exceptions)

- netherlands 1963 loss -> federal-republic-of-germany: missing. netherlands /ledger/20 (1963-08, conf 3, Elten, Selfkant, Suderwick); no gain in the FRG ledger (thin, page budget)
- hungarian-people-s-republic 1949 found -> hungary: exception. hungary is in group eu-22, another part, not written yet
- hungarian-people-s-republic 1956 contest_start -> union-of-soviet-socialist-republics: missing. USSR ledger (eu-17) has no event 1955-1957; route to eu-17
- hungarian-people-s-republic 1956 contest_end -> union-of-soviet-socialist-republics: missing. as above
- republic-of-poland 1945 found -> second-polish-republic: exception. no dossier (eu-21, Cliopatria row 1919-1939); listed by the author. But see the nazi-germany and USSR mismatches below
- nazi-germany 1945 loss -> republic-of-poland: mismatch. nazi-germany /ledger/71 (1945-01, Wartheland, conf 2); republic-of-poland starts 1945-06 and has no gain from nazi-germany; resolve in republic-of-poland (start 1945-01) or eu-21
- nazi-germany 1945 loss -> republic-of-poland: mismatch. nazi-germany /ledger/72 (1945-01, Katowice district, conf 3); republic-of-poland starts 1945-06 and has no gain from nazi-germany; resolve in republic-of-poland (start 1945-01) or eu-21
- nazi-germany 1945 loss -> republic-of-poland: mismatch. nazi-germany /ledger/73 (1945-01, Ciechanów district, conf 1); republic-of-poland starts 1945-06 and has no gain from nazi-germany; resolve in republic-of-poland (start 1945-01) or eu-21
- nazi-germany 1945 loss -> republic-of-poland: mismatch. nazi-germany /ledger/77 (1945-03, Danzig, conf 3); republic-of-poland starts 1945-06 and has no gain from nazi-germany; resolve in republic-of-poland (start 1945-01) or eu-21
- nazi-germany 1945 loss -> republic-of-poland: mismatch. nazi-germany /ledger/78 (1945-03, Danzig-West Prussia, conf 2); republic-of-poland starts 1945-06 and has no gain from nazi-germany; resolve in republic-of-poland (start 1945-01) or eu-21
- union-of-soviet-socialist-republics 1945 loss -> republic-of-poland: missing. USSR /ledger/50 (1945-08, Białystok area, conf 2); republic-of-poland already holds it by its 1945-06 found; add the gain in republic-of-poland
- french-west-africa 1958 dissolve -> french-fifth-republic: exception. FFR found (cp french-fourth-republic) covers the AOF land; counterparts differ but land and month agree
- french-equatorial-africa 1958 dissolve -> french-fifth-republic: exception. AEF dissolves 1958-09 to FFR, which begins 1958-10; one month, land covered by the FFR found
- french-africa 1957 dissolve -> french-fifth-republic: mismatch. french-africa (af-08) dissolves 1957 (conf 1) to a state founded 1958-10; FFR lists french-africa as predecessor; fix on the af-08 side
- guinea 1958 found -> french-fifth-republic: mismatch. Guinea independent 2 October 1958, before the Fifth Republic (4 October); FFR rightly excludes it; guinea's counterpart should be french-fourth-republic (af-08)
- french-fifth-republic 1958 vassal_start -> madagascar: mismatch. FFR 1958-10; madagascar (af-08) starts 1960 with a found against FFR and has no vassal_start
- french-fifth-republic 1958 vassal_start -> republic-of-cameroon: mismatch. FFR 1958-10; republic-of-cameroon (af-08) starts 1960 with a found against FFR and has no vassal_start
- french-fifth-republic 1958 vassal_start -> togo: mismatch. FFR 1958-10; togo (af-08) starts 1960 with a found against FFR and has no vassal_start
- french-fifth-republic 1958 vassal_start -> mali-federation: mismatch. FFR 1958-11; mali-federation (af-08) starts 1960 with a found against FFR and has no vassal_start
- french-fifth-republic 1958 vassal_start -> republic-of-chad: mismatch. FFR 1958-11; republic-of-chad (af-08) starts 1960 with a found against FFR and has no vassal_start
- french-fifth-republic 1958 vassal_start -> gabon: mismatch. FFR 1958-11; gabon (af-08) starts 1960 with a found against FFR and has no vassal_start
- french-fifth-republic 1958 vassal_start -> republic-of-the-congo: mismatch. FFR 1958-11; republic-of-the-congo (af-08) starts 1960 with a found against FFR and has no vassal_start
- french-fifth-republic 1958 vassal_start -> mauritania: mismatch. FFR 1958-11; mauritania (af-08) starts 1960 with a found against FFR and has no vassal_start
- french-fifth-republic 1958 vassal_start -> central-african-republic: mismatch. FFR 1958-12; central-african-republic (af-08) starts 1960 with a found against FFR and has no vassal_start
- french-fifth-republic 1958 vassal_start -> republic-of-benin: mismatch. FFR 1958-12; republic-of-benin (af-08) starts 1960 with a found against FFR and has no vassal_start
- french-fifth-republic 1958 vassal_start -> republic-of-cote-d-ivoire: mismatch. FFR 1958-12; republic-of-cote-d-ivoire (af-08) starts 1960 with a found against FFR and has no vassal_start
- french-fifth-republic 1958 vassal_start -> burkina-faso: mismatch. FFR 1958-12; burkina-faso (af-08) starts 1960 with a found against FFR and has no vassal_start
- french-fifth-republic 1958 vassal_start -> republic-of-the-niger: mismatch. FFR 1958-12; republic-of-the-niger (af-08) starts 1960 with a found against FFR and has no vassal_start
- french-fifth-republic 1962 occupation_start -> people-s-democratic-republic-of-algeria: missing. Mers El Kébir 1962-07 to 1967: Algeria (af-08) has no occupation events
- french-fifth-republic 1967 occupation_end -> people-s-democratic-republic-of-algeria: missing. as above
- french-fifth-republic 1975 loss -> comoros: exception. no Cliopatria row or dossier; listed in counterparts_needing_dossiers
- republic-of-tunisia 1963 gain -> french-fifth-republic: missing. Tunisia /ledger/2-4: Bizerte contest 1961-07 to 1963-10 and gain 1963-10; no event in FFR (author-flagged gap)

Matched: german-democratic-republic 1949 found / allied-occupied-germany dissolve; german-democratic-republic 1990 loss / federated-republic-of-germany gain; german-democratic-republic 1990 merge / federal-republic-of-germany merge; federal-republic-of-germany 1949 found / allied-occupied-germany split; federal-republic-of-germany 1957 gain / saar-protectorate dissolve; federal-republic-of-germany 1990 dissolve / federated-republic-of-germany found; republic-of-poland 1945 gain / allied-occupied-germany loss; french-fifth-republic 1958 found / french-fourth-republic dissolve; french-fifth-republic 1958 occupation_start / west-berlin occupation_start; french-fifth-republic 1960 loss / republic-of-cameroon found; french-fifth-republic 1960 loss / togo found; french-fifth-republic 1960 loss / madagascar found; french-fifth-republic 1960 loss / mali-federation found; french-fifth-republic 1960 loss / republic-of-chad found; french-fifth-republic 1960 loss / gabon found; french-fifth-republic 1960 loss / republic-of-the-congo found; french-fifth-republic 1960 loss / central-african-republic found; french-fifth-republic 1960 loss / republic-of-benin found; french-fifth-republic 1960 loss / republic-of-cote-d-ivoire found; french-fifth-republic 1960 loss / burkina-faso found; french-fifth-republic 1960 loss / republic-of-the-niger found; french-fifth-republic 1960 loss / mauritania found; french-fifth-republic 1962 loss / people-s-democratic-republic-of-algeria found; french-fifth-republic 1977 loss / republic-of-djibouti found; french-fifth-republic 1990 occupation_end / west-berlin occupation_end; republic-of-cyprus 1960 found / united-kingdom loss; republic-of-cyprus 1974 contest_start / republic-of-turkey contest_start; republic-of-cyprus 1974 contest_end / republic-of-turkey contest_end; republic-of-cyprus 1974 occupation_start / republic-of-turkey occupation_start

## Problems

- No page failed to load. The edits applied to french-fifth-republic.json and republic-of-cyprus.json were re-validated (valid, only the expected warnings: comoros has no dossier; Cyprus occupation open to 2024) and read back after the write.
- republic-of-poland's 1945 formation conflicts with nazi-germany (eu-21) and the USSR (eu-17) ledgers; whichever side changes, the other must be told.
- The 13 French Community vassal_start events have no mirror because the af-08 dossiers start at independence in 1960; the orchestrator should decide the convention (client tint from autonomy in 1958, or none) for both groups.
- Akrotiri/Dhekelia discs (12 km) are shared by republic-of-cyprus and united-kingdom (eu-11): change both or neither.
