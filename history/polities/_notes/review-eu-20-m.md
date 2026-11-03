# Review of batch eu-20-m (Europe 1789-1914, part m)

Reviewer brief filled 2026-10-31; review run 2026-11-01. Dossiers: french-second-republic, italian-nationalists, hungarian-nationalists, republic-of-baden, second-french-empire, austria-hungary. Machine copy: history/notes/phase-b/reviews/eu-20-m.json.

## Summary

- Validator (--resolve): no errors in any dossier. Warnings: roman-republic-1849 and state-of-slovenes-croats-and-serbs have no dossier (listed below); 'Menton' unknown to the gazetteer.
- 15 pages re-opened; every event spot-checked (5 or more per dossier, weighted to confidence 3 and large land moves) says what its note claims. No fabricated or mis-dated confidence-3 event found.
- Verdicts: french-second-republic fix (reviewer-applied), italian-nationalists pass, hungarian-nationalists thin, republic-of-baden pass, second-french-empire thin (two reviewer fixes applied), austria-hungary fail (1918 hand-off).
- Reviewer edits applied in place and re-validated: french-second-republic /identity/rulers/1-3 source; second-french-empire /ledger/1 (1853 -> 1852/12, confidence 2, Roman Republic page), /ledger/7 (Menton page, confidence 2) and a new sources[] entry.

## french-second-republic: fix

Area: infobox none (-), Cliopatria 629765, ratio -; No area in the infobox (re-read). 629,765 km2 = metropolitan France plus Guiana, Antilles, Reunion, French India; Algeria drawn by other rows; plausible.

Findings:
- `/identity/rulers/1/source, /identity/rulers/2/source, /identity/rulers/3/source` (applied by reviewer): Arago, Cavaignac and Louis-Napoleon Bonaparte cited no page (only Dupont de l'Eure did). Evidence: French Second Republic infobox: 'May-June 1848: Francois Arago', 'June-December 1848: Louis-Eugene Cavaignac', '1848-1852: Louis-Napoleon Bonaparte'. Fix: source = https://en.wikipedia.org/wiki/French_Second_Republic on the three entries.

Gaps (thin):
- `/ledger/4`: Confidence 1 occupation_end of Rome at 1852/12 is a dossier boundary (the garrison stayed to 1870); nothing to find, kept at 1 because the occupation did not really end. second-french-empire /ledger/1 now reopens it at the same month. Page to try: https://en.wikipedia.org/wiki/Roman_Republic_(1849)

Spot checks: /ledger/0 confirmed (French_Second_Republic); /ledger/1 confirmed (Roman_Republic_(1849)); /ledger/2 confirmed (Roman_Republic_(1849)); /ledger/3 confirmed (Roman_Republic_(1849)); /ledger/5 confirmed (French_Second_Republic)

## italian-nationalists: pass

Area: infobox none (-), Cliopatria 21788, ratio -; No area on the page; 21,788 km2 is Sicily (about 25,700 km2) without the Messina corner, matching 'never able to control the well fortified city of Messina'.

Spot checks: /ledger/0 confirmed (Sicilian_revolution_of_1848); /ledger/1 confirmed (Sicilian_revolution_of_1848); /ledger/2 confirmed (Sicilian_revolution_of_1848); /ledger/3 confirmed (Sicilian_revolution_of_1848)

## hungarian-nationalists: thin

Area: infobox none (-), Cliopatria 271818, ratio -; No area in the infobox (re-read: dates 15 March 1848 - 4 October 1849 only). 271,818 km2 is the Kingdom of Hungary without Croatia-Slavonia, plausible for the claimed extent.

Gaps (thin):
- `/ledger/6`: Confidence 1: month of the Russian entry into Hungary (June 1849 is a bridge); the Hungarian Revolution page is silent. Page to try: https://en.wikipedia.org/wiki/Summer_Campaign_(1849)
- `/ledger/7, /ledger/8, /ledger/9, /ledger/10`: Day of the capitulation at Vilagos (13 August 1849 in the austrian-empire dossier, not on this page); all four at confidence 2. Page to try: https://en.wikipedia.org/wiki/Summer_Campaign_(1849)
- `/keyframe_review/1`: The 1849 keyframe draws the whole claimed extent all year; January-April 1849 (Austrian-held west including Pest) and the summer 1849 Austro-Russian advance are not drawn beyond the Pest point events. Thin by design within a 1-2 page budget. Page to try: https://en.wikipedia.org/wiki/Summer_Campaign_(1849)
- `/identity/capitals/1`: Seat after the recapture of Buda (21 May 1849): the page does not say where the government sat from June 1849 (Pest, then Szeged and Arad in July-August are the usual account, unverified). Page to try: https://en.wikipedia.org/wiki/Summer_Campaign_(1849)

Spot checks: /ledger/1 confirmed (Hungarian_Revolution_of_1848); /ledger/3 confirmed (Hungarian_Revolution_of_1848); /ledger/4 confirmed (Hungarian_Revolution_of_1848); /ledger/5 confirmed (Hungarian_Revolution_of_1848); /ledger/7 confirmed (Hungarian_Revolution_of_1848)

## republic-of-baden: pass

Area: infobox 15070 (1925), Cliopatria 17733, ratio 1.18; No area on the Baden Revolution page; the author's proxy is the 1918-1945 Republic of Baden page (15,070 km2, 1925), not re-read by the reviewer. The excess is the 16 Palatinate cells the correction removes.

Spot checks: /ledger/0 confirmed (Baden_Revolution); /ledger/1 confirmed (Baden_Revolution); /ledger/2 confirmed (Baden_Revolution); /ledger/3 confirmed (Baden_Revolution); /ledger/4 confirmed (Baden_Revolution)

## second-french-empire: thin

Area: infobox none (-), Cliopatria 671292, ratio -; No infobox area (re-read). The body says that 'in 1870 they covered almost a million square kilometres, and controlled nearly five million inhabitants' in the overseas-empire passage; even read as the whole state that is 1.5 times the 1863 shape, under a factor of two, and Algeria, Senegal, Cochinchina and New Caledonia are drawn by other rows.

Findings:
- `/ledger/1` (applied by reviewer): The Rome occupation reopened in 1853 (no month, confidence 1) left a gap after the Republic's dossier-boundary end of 1852/12. Evidence: Second French Empire infobox 'Empire proclaimed: 2 December 1852'; Roman Republic (1849) page: 'French soldiers propped up the papal administration in Rome until they were withdrawn' at the outbreak of the Franco-Prussian War in 1870. Fix: year 1852, month 12, confidence 2, source the Roman Republic (1849) page, note rewritten.
- `/ledger/7 and /sources` (applied by reviewer): Menton and Roquebrune gain was confidence 1 with a page (Second French Empire) that does not mention it. Evidence: Menton page: 'Napoleon III paid 4 million francs in compensation to the prince of Monaco, who renounced his rights in perpetuity on 2 February 1861'; Menton 'was an exclave of the Principality of Monaco until the disputed French plebiscite of 1860'; the towns seceded in 1848 and were administered by the House of Savoy for ten years. Fix: source https://en.wikipedia.org/wiki/Menton (added to sources[]), confidence 2 (the de facto passage came with the 1860 plebiscite), note rewritten. Region place 'Menton' still needs the gazetteer.
- `/keyframe_review/1/correction, /keyframe_review/2 (verdict ok), /keyframe_review/3/correction, /keyframe_review/4/correction, /keyframe_review/5/correction` (for the author or gap-filler): The corrected shapes for 1856-1870 omit Reunion and French India (13 cells of the 1853 shape), which no page says France lost; flagged by the author but left standing. Evidence: shapes.csv: Cliopatria moves those cells into new-caledonia_1856 (bbox 55.1-168.0 E, -22.4-22.8 N), and the new-caledonia dossier (oc-02) marks that shape 'wrong' as a 'multi-part French overseas aggregate', so from 1856 no dossier draws Reunion or French India. Fix: Gap-filler: open the Reunion and French India pages; if French throughout 1856-1870, add the 13 cells back to each correction, e.g. union with {'minus': [{'cliopatria': 'Second French Empire', 'year': 1853}, {'cliopatria': 'Second French Empire', 'year': 1856}]}, and turn the 1860 verdict into adjust.

Gaps (thin):
- `/keyframe_review/1-5`: Reunion and French India 1856-1870 (see fixes): a page that keeps them French so the corrections can include them. Page to try: https://en.wikipedia.org/wiki/R%C3%A9union
- `/ledger/1, /ledger/18`: The Rome garrison is drawn continuous 1849-1870; the September Convention withdrawal (December 1866) and the return after Mentana (autumn 1867) are not in the ledger (Roman Republic page silent; reviewer's reading, unverified). Page to try: https://en.wikipedia.org/wiki/September_Convention
- `/ledger/17`: Confidence 1: end of the French hold on Puebla bridged to the general embarkation of 12 March 1867. Page to try: https://en.wikipedia.org/wiki/Second_French_intervention_in_Mexico
- `/ledger (Mexico)`: federated-republic-of-mexico /ledger/39 and /ledger/43 record a French occupation of Chihuahua (1865/8 - 1867/3) that has no event here. Page to try: https://en.wikipedia.org/wiki/Second_French_intervention_in_Mexico

Spot checks: /ledger/0 confirmed (Second_French_Empire); /ledger/2 confirmed (Crimean_War); /ledger/3 confirmed (Crimean_War); /ledger/6 confirmed (Treaty_of_Turin_(1860)); /ledger/7 confirmed (after the reviewer's source change; the original source did not mention it) (Menton); /ledger/8 confirmed (Second_French_intervention_in_Mexico); /ledger/9 confirmed (year from context) (Second_French_intervention_in_Mexico); /ledger/10 confirmed (Second_French_intervention_in_Mexico); /ledger/11 confirmed (Second_French_intervention_in_Mexico); /ledger/12 confirmed (year from context) (Second_French_intervention_in_Mexico); /ledger/14 confirmed (year from context) (Second_French_intervention_in_Mexico); /ledger/16 confirmed (Second_French_intervention_in_Mexico); /ledger/21 confirmed (Second_French_Empire)

## austria-hungary: fail

Area: infobox 621538 (1905), Cliopatria 677899, ratio 1.09; Re-read: '1905: 621,538 km2'. The 1905 shape holds occupied Bosnia, the Sanjak and Tianjin; the corrected 1873 outline is 623,093 km2 (ratio 1.00).

Findings:
- `/identity/successors, /ledger/24, /ledger/26 (and new split events)` (BLOCKING, for the author): The 1918 hand-off covers only Czechia, Austria, modern Hungary and Slovenia-Croatia-Bosnia: Galicia, Bukovina, Transylvania-Banat-Crisana-Maramures, Slovakia, Transcarpathia and Vojvodina (roughly 1,000 of the 1912 outline's cells, about 40 percent) pass to no successor, and the successor list lacks the infobox's Polish and West Ukrainian successors. Evidence: Austria-Hungary infobox successors: German-Austria, Hungary, Czechoslovakia, State of Slovenes Croats and Serbs, Kingdom of Yugoslavia, Kingdom of Italy, Polish Liquidation Committee, Kingdom of Poland, West Ukrainian People's Republic. Neighbours already take land from austria-hungary after its 1918/10 end: united-principalities-of-moldavia-and-wallachia /ledger/27 (Bukovina, 28 November 1918) and /ledger/28 (Transylvania, 1 December 1918); serbs /ledger/28-29 (Syrmia, Banat-Backa-Baranja, 24-25 November 1918); czechoslovakia /ledger/0 (found 1918/10 with Bohemia, Moravia and Slovakia); kingdom-of-italy /ledger/15-16 (1919). Fix: Add successors with land and split events dated at the dissolution: second-polish-republic (western Galicia; Polish Liquidation Committee, 28 October 1918), west-ukrainian-people-s-republic (eastern Galicia and northern Bukovina, 1 November 1918, new slug), kingdom-of-romania or the Romanian dossier's slug (southern Bukovina, Transylvania, Banat, Crisana, Maramures), serbs (Vojvodina), kingdom-of-italy (Trentino, South Tyrol, Littoral); widen /ledger/24 to Czechia + Slovakia to match the czechoslovakia dossier and this dossier's own successor text; keep hungarian-republic for what remains. Cite the infobox and each successor's page.
- `/ledger/34` (for the author or gap-filler): split to republic-of-austria dated 1918/11, after the dissolve event (1918/10, infobox 'Empire dissolved: 31 October 1918'). Evidence: Austria-Hungary infobox: 'Empire dissolved: 31 October 1918'; the event's own note gives 12 November for the republic. Fix: Date the split 1918/10 (German-Austria as a state, 30 October 1918, from the German-Austria page) or explain the gap; a split cannot follow the end of the state.
- `/ledger/20` (for the author or gap-filler): occupation_end of the remaining Russian-held Galicia/Bukovina in 1917 names russian-empire, whose dossier ends 1917/3 (dissolve to russian-republic); the July 1917 counter-offensive was against the Russian Republic. Evidence: russian-empire identity.end 1917/3 and /ledger/137 (dissolve, russian-republic); Eastern Front page: the Kerensky offensive was thrown back and 'the Austrians counterattacked and drove them almost entirely out of Austria-Hungary'. Fix: Close the russian-empire occupation at 1917/3 (boundary) and add occupation_start/occupation_end with counterpart russian-republic 1917/3 - 1917/7 (or the month a page gives).
- `/ledger/18` (for the author or gap-filler): End of the Romanian incursion bridged to 1916/12 at confidence 1; the Romanian dossier dates it 25 October 1916 at confidence 3. Evidence: united-principalities-of-moldavia-and-wallachia /ledger/16, Romanian Campaign page: 'by 25 October the Romanian army was back to its initial positions'. Fix: month 10, source https://en.wikipedia.org/wiki/Romanian_Campaign_(World_War_I) (add to sources), confidence 2 or 3 after reading it.
- `/identity/rulers/1` (for the author or gap-filler): Charles I cites no page. Evidence: Franz Joseph's entry cites the Austria-Hungary page; Charles's does not. Fix: Add source https://en.wikipedia.org/wiki/Austria-Hungary.

Gaps (thin):
- `/ledger/3, /ledger/21`: Confidence 1: Tianjin concession gain (Cliopatria's 1905) and loss (1917); the concession dates from 1901-1902 and was seized by China in August 1917 (unverified). Page to try: https://en.wikipedia.org/wiki/Austro-Hungarian_concession_of_Tianjin
- `/ledger (1915-1918)`: No event for the Austro-Hungarian occupation zone in Russian Poland (Military General Government of Lublin, 1915-1918); Cliopatria does not draw it either. Page to try: https://en.wikipedia.org/wiki/Military_General_Government_of_Lublin
- `/ledger/30, /ledger/31, /ledger/32, /ledger/33`: Confidence 1 occupation ends bridged to November 1918; the montenegro dossier dates its end October 1918 (confidence 3) and albania September 1918 (confidence 2). Page to try: https://en.wikipedia.org/wiki/Montenegrin_campaign
- `/ledger/22, /ledger/23, /keyframe_review/11-12`: Extent and dates of the Italian (post-Caporetto), Ukrainian and Wallachian zones are Cliopatria's cells (author: unverified, page budget). Page to try: https://en.wikipedia.org/wiki/Operation_Faustschlag
- `/ledger (1915-1917)`: The Italian-held strip on the Isonzo (Gorizia, August 1916) is not recorded; small. Page to try: https://en.wikipedia.org/wiki/Italian_front_(World_War_I)

Spot checks: /ledger/2 confirmed (Condominium_of_Bosnia_and_Herzegovina); /ledger/4 confirmed (Condominium_of_Bosnia_and_Herzegovina); /ledger/5 confirmed (Condominium_of_Bosnia_and_Herzegovina); /ledger/6 confirmed (Austria-Hungary); /ledger/7 confirmed (Eastern_Front_(World_War_I)); /ledger/9 confirmed (Eastern_Front_(World_War_I)); /ledger/10 confirmed (Serbian_campaign_of_World_War_I); /ledger/11 confirmed (Serbian_campaign_of_World_War_I); /ledger/13 confirmed (Montenegrin_campaign); /ledger/14 confirmed (Montenegrin_campaign); /ledger/16 confirmed (Montenegrin_campaign); /ledger/17 confirmed (Eastern_Front_(World_War_I)); /ledger/19 confirmed (Austria-Hungary); /ledger/27 confirmed (Austria-Hungary); /ledger/28 confirmed (Serbian_campaign_of_World_War_I)

What could not be broken: italian-nationalists and republic-of-baden (dates, Messina, the Palatinate removal, the rebel type and the Cliopatria mislabelling are all as the pages say); the Mexican occupation dates of second-french-empire; the Bosnia/Sanjak occupation-annexation sequence and the WWI campaign dates of austria-hungary.

## Cross-dossier matrix

- french-second-republic 1849 occupation_start <-> papal-states: missing. papal-states (eu-13) records no French garrison 1849-1870; it should carry occupation_start 1849/7 (counterpart french-second-republic), a boundary pair at 1852/12, and second-french-empire 1852/12-1870/8.
- french-second-republic 1852 occupation_end <-> papal-states: exception. Dossier boundary only (the garrison stayed); reopened by second-french-empire /ledger/1 at 1852/12.
- french-second-republic 1849 contest_start <-> roman-republic-1849: exception. No dossier; listed in counterparts_needing_dossiers (papal-states uses the same slug).
- italian-nationalists 1848 gain <-> kingdom-of-the-two-sicilies: matched. /ledger/4, 1848/1.
- italian-nationalists 1849 loss <-> kingdom-of-the-two-sicilies: matched. /ledger/5, 1849/5.
- hungarian-nationalists 1849 loss <-> austrian-empire: mismatch. Pest lost 1849/1 and retaken 1849/5 (/ledger/3, /ledger/5) and the final loss 1849/8 have no gain/loss in austrian-empire, which holds the whole zone as contested 1848/12 (/ledger/34) - 1849/8 (/ledger/38). No drawing conflict; eu-20 owner may add point events or the orchestrator may accept contest-as-mirror for rebel states.
- hungarian-nationalists 1849 gain <-> austrian-empire: mismatch. See above: inside the austrian-empire contest; no loss of Buda in that ledger.
- republic-of-baden 1849 gain <-> grand-duchy-of-baden: matched. /ledger/3, 1849/5.
- republic-of-baden 1849 loss <-> grand-duchy-of-baden: matched. /ledger/7, 1849/7.
- second-french-empire 1852 occupation_start <-> papal-states: missing. Same as the Republic's: papal-states has no French occupation events (eu-13).
- second-french-empire 1870 occupation_end <-> papal-states: missing. papal-states ends 1870/9 with no occupation_end for the French garrison (eu-13).
- second-french-empire 1860 gain <-> kingdom-of-sardinia: matched. /ledger/47, 1860/3.
- second-french-empire 1861 gain <-> principality-of-monaco: matched. /ledger/17, 1861/2 (Menton page).
- second-french-empire 1862 occupation_start <-> federated-republic-of-mexico: matched. Veracruz, /ledger/33.
- second-french-empire 1863 occupation_start <-> federated-republic-of-mexico: matched. Puebla: 1863/5 (surrender) here, 1863/3 (siege start) in /ledger/35; Mexico City 1863/6 both (/ledger/36).
- second-french-empire 1864 occupation_start <-> federated-republic-of-mexico: missing. Mazatlan 1864/11 - 1866/11 and Guaymas 1865/3 - 1866/9 have no events in federated-republic-of-mexico (am-08).
- federated-republic-of-mexico 1865 occupation_start <-> second-french-empire: missing. Chihuahua 1865/8 - 1867/3 (/ledger/39, /ledger/43) has no event in second-french-empire (thin item).
- second-french-empire 1867 occupation_end <-> federated-republic-of-mexico: matched. Mexico City 1867/2 (/ledger/40), Veracruz 1867/2 vs 1867/3 (/ledger/41), Puebla 1867/3 (/ledger/42).
- second-french-empire 1870 contest_start <-> north-german-confederation: exception. No dossier yet; owned by eu-20 (not yet written).
- austria-hungary 1867 found <-> austrian-empire: matched. /ledger/60, 1867/3.
- austria-hungary 1878 occupation_start <-> ottoman-empire: mismatch. Bosnia: A-H records occupation 1878/7 - 1908/10 then gain (Condominium page); ottoman-empire /ledger/191 records a loss in 1878/7 and nothing in 1908. me-10 should record occupation_start 1878/7 and loss 1908/10 (counterpart austria-hungary).
- austria-hungary 1878 occupation_start <-> ottoman-empire: missing. Sanjak of Novi Pazar 1878-1909: no occupation pair in ottoman-empire (me-10); its /ledger/191 note mentions the garrison right only.
- austria-hungary 1908 gain <-> ottoman-empire: missing. No Ottoman loss of Bosnia in 1908 (it was booked in 1878).
- austria-hungary 1905 gain <-> qing-dynasty: missing. Tianjin concession; both sides undocumented (A-H confidence 1); ea-08.
- austria-hungary 1917 loss <-> republic-of-china: missing. Tianjin concession seized 1917; no gain in republic-of-china (ea-08); A-H side confidence 1.
- austria-hungary 1914 occupation_start <-> russian-empire: matched. /ledger/131 (1914/9) and /ledger/135 end 1915/5 match A-H /ledger/7 and /ledger/9.
- austria-hungary 1914 occupation_start <-> russian-empire: missing. The remainder of Galicia/Bukovina held to 1917 (A-H /ledger/8, /ledger/20) has no event in russian-empire (eu-17); after 1917/3 it belongs to russian-republic (A-H fix).
- austria-hungary 1915 occupation_start <-> serbs: matched. /ledger/24 1915/10; end 1918/11 both (/ledger/27).
- austria-hungary 1916 occupation_start <-> montenegro: matched. /ledger/11 1916/1; end 1918/10 there vs 1918/11 here (A-H confidence 1).
- austria-hungary 1916 occupation_start <-> albania: matched. /ledger/4; end 1918/9 there vs 1918/11 here (A-H confidence 1).
- austria-hungary 1916 occupation_start <-> united-principalities-of-moldavia-and-wallachia: matched. Romanian incursion into Transylvania, /ledger/14 1916/8; end 1916/10 there (/ledger/16) vs 1916/12 here (fix).
- austria-hungary 1916 occupation_start <-> united-principalities-of-moldavia-and-wallachia: mismatch. Wallachia: A-H records its own occupation 1916/12 - 1918/11; the Romanian dossier records only german-empire and principality-of-bulgaria occupations (/ledger/15, 17, 18, 20, 23-26). eu-18 should add austria-hungary or the A-H zone should be dropped as German-led.
- united-principalities-of-moldavia-and-wallachia 1918 gain <-> austria-hungary: mismatch. /ledger/27 (Bukovina 1918/11) and /ledger/28 (Transylvania 1918/12) gain from austria-hungary after its 1918/10 end; A-H has no split or successor for those lands (A-H blocking fix).
- serbs 1918 gain <-> austria-hungary: mismatch. /ledger/28-29 (Syrmia, Banat-Backa-Baranja, 1918/11) gain from austria-hungary after its end; A-H has no split or successor for Vojvodina.
- austria-hungary 1917 occupation_start <-> kingdom-of-italy: mismatch. Caporetto zone: A-H occupation 1917/10 - 1918/11; kingdom-of-italy /ledger/14 books it as a loss with no recovery event (eu-13 should use occupation_start/end).
- kingdom-of-italy 1919 gain <-> austria-hungary: mismatch. /ledger/15-16 gain Trentino-Alto Adige and Trieste from austria-hungary in 1919; A-H lists kingdom-of-italy as successor with land but no split event; acceptable once the A-H hand-off is completed.
- austria-hungary 1918 occupation_start <-> ukrainian-people-s-republic: missing. The ukrainian-people-s-republic dossier exists (eu-17, 1917/11-1921/3) and has no Central Powers occupation events in 1918.
- austria-hungary 1918 split <-> czechoslovakia: mismatch. Dates match (1918/10) but land differs: czechoslovakia /ledger/0 founds on Bohemia, Moravia and Slovakia; A-H /ledger/24 splits off Czechia only.
- austria-hungary 1918 split <-> state-of-slovenes-croats-and-serbs: exception. No dossier; listed in counterparts_needing_dossiers.
- austria-hungary 1918 split <-> hungarian-republic: exception. Polities row (1919-1943) owned by eu-21; no dossier yet.
- austria-hungary 1918 split <-> republic-of-austria: exception. Polities row (1919-1937) owned by eu-21; no dossier yet.

## Routing

- eu-13 (papal-states): add the French garrison in Rome as occupation events 1849/7 - 1870/8 (counterparts french-second-republic, then second-french-empire from 1852/12). kingdom-of-italy: Caporetto zone as occupation (1917/10 - 1918/11), not loss.
- me-10 (ottoman-empire): Bosnia as occupation 1878/7 - 1908/10 then loss 1908/10; Sanjak of Novi Pazar occupation 1878 - 1909.
- eu-17 (russian-empire, russian-republic, ukrainian-people-s-republic): the Galicia/Bukovina remainder held to 1917; the 1918 Central Powers occupation of Ukraine.
- eu-18 (united-principalities-of-moldavia-and-wallachia, serbs): the 1918 gains from austria-hungary fall after its 1918/10 end; agree counterparts once austria-hungary completes its hand-off. Romania: Austro-Hungarian share of the Wallachia occupation.
- am-08 (federated-republic-of-mexico): Mazatlan (1864/11 - 1866/11) and Guaymas (1865/3 - 1866/9) occupations.
- ea-08: Tianjin concession (qing-dynasty loss, republic-of-china gain 1917).
- oc-02 (new-caledonia): its 1856 aggregate holds Reunion and French India, which second-french-empire also leaves out; one of the two must draw them.

## Gazetteer

- place 'Menton' (second-french-empire /ledger/7; Menton and Roquebrune, 43.78 N 7.50 E).

## Counterparts needing dossiers

- Roman Republic (1849) (roman-republic-1849, 1849-1849)
- State of Slovenes, Croats and Serbs (state-of-slovenes-croats-and-serbs, 1918-1918)
- Provisional Government of the Palatinate (Palatine Uprising) (provisional-government-of-the-palatinate, 1849-1849)
- West Ukrainian People's Republic (west-ukrainian-people-s-republic, 1918-1919)

## Problems

- WebFetch returns a small model's summary; quotes above are its quoted sentences.
- The author's report lists ukrainian-people-s-republic as a counterpart without a dossier; a dossier now exists (eu-17, 1917/11-1921/3) but has no Central Powers occupation events for 1918.
- Reviewer edits applied in place: french-second-republic (ruler sources), second-french-empire (/ledger/1, /ledger/7, sources[]); both re-validated with no errors.
- Blocking item outside this batch's power: the 1918 hand-off of Austria-Hungary must be agreed with eu-18 (Romania, serbs) and eu-21 (successor republics) dossiers.
