# Review of batch eu-18-d

Reviewer, 2026-10-25. Six dossiers: principality-of-wallachia, serbian-empire, moravian-serbia, house-of-anjou-sicily, kingdom-of-syrmia, principality-of-valona. The validator passes all six with --resolve (0 errors, 0 warnings). Neighbour dossiers read (ledger greps): byzantine-empire, despotate-of-epirus, despotate-of-arta, principality-of-achaea, ottoman-empire, habsburg-monarchy, crown-of-aragon, kingdom-of-sicily, kingdom-of-naples, capetian-house-of-anjou, golden-horde, duchy-of-athens, catalan-company, eastern-hungarian-kingdom, house-of-habsburg. The other Context polities have no dossier yet (their groups have not run): their events count as exceptions.

Verdict scale for this run: fix means the reviewer made every needed change; fail means at least one change the author must make (shape, region or event) is still open. Items marked applied were edited in place by the reviewer and re-validated.

## Verdicts

- principality-of-wallachia: **fail**
- serbian-empire: **fail**
- moravian-serbia: **thin**
- house-of-anjou-sicily: **fail**
- kingdom-of-syrmia: **fail**
- principality-of-valona: **fail**

## principality-of-wallachia (fail)

Findings:

1. `/keyframe_review/5 and /keyframe_review/6` (open): Both keyframes are verdict ok and draw no Dobruja, but the ledger gains Dobruja and Silistra c. 1400 (/ledger/4) and loses them c. 1404 (/ledger/5): the keyframes contradict the ledger across a shape boundary (1402) for about 23,000 km2, some 30 percent of the state. Evidence: Wallachia page: Mircea I 'briefly extend[ed] his rule to the Danube Delta, Dobruja and Silistra (c. 1400-1404)'; the KF5 note itself says 'the shape does not show' it. Reviewer brief rule 4: an event with no trace in the keyframes is acceptable only inside one shape span and small, or with the keyframe marked adjust. Fix: Mark KF5 adjust (Cliopatria 1395 shape valid 1395-1399) and KF6 adjust (valid 1405-1421), and add a new keyframe principality-of-wallachia_1400 (from 1400, to 1404, verdict adjust) = union of the Cliopatria 1402 shape, {region: Dobruja} and {admin1: Silistra, country: Bulgaria}, text from the page.
2. `/ledger (1789-1791), /keyframe_review/18/note` (open): The Habsburg occupation of Wallachia in the war of 1788-1791 is missing; the 1791 keyframe note says the pages date no change. Evidence: Wallachia page (opened by the author): 'Habsburg troops, under Prince Josias of Coburg, again entered the country' and deposed Nicholas Mavrogenes in 1789; habsburg-monarchy.json /ledger/105: 'The Austrians had occupied Bosnia, Belgrade and Bucharest' (1788-91 war). Fix: Add occupation_start (1789, counterpart habsburg-monarchy, region Wallachia, confidence 2, Wallachia page) and occupation_end (1791, Treaty of Sistova, confidence 2), the war 'Austro-Turkish War (1788-1791)', and correct the KF18 note.
3. `/wars` (open): Wars named on the Wallachia page are missing: Mircea's war with Bayezid (Rovine, 1395) and Vlad III's war of 1462 (the KF7 note names the Night Attack). Evidence: Reviewer brief rule 10: each war in the sources appears, with empty zones where no ground changed hands, said so; ottoman-empire.json /ledger/21 cites Rovine 1395. Fix: Add both wars with zones [] and an outcome sentence saying no border moved on the page.

Gaps for a gap-filler:

- `/ledger/14`: 1601 loss of the Danube forts is a confidence-1 bridge (Michael the Brave page silent on their return to the Ottomans). Page to try: https://en.wikipedia.org/wiki/Long_Turkish_War
- `/keyframe_review/25 and /ledger/25`: The 1828-1833 keyframe starts in 1828 but the Russian occupation event is dated 14 September 1829 (treaty); the entry of Russian troops in 1828 is undated. Page to try: https://en.wikipedia.org/wiki/Russo-Turkish_War_(1828%E2%80%931829)
- `/ledger/26`: 1834 end of the Russian occupation is a confidence-1 bridge. Page to try: https://en.wikipedia.org/wiki/Regulamentul_Organic
- `/ledger/27`: 1848 occupation start is confidence 1; the Wallachia page gives 'Ottoman troops entered Bucharest on 13 September' (1848), which dates at least the Ottoman entry. Page to try: https://en.wikipedia.org/wiki/Wallachian_Revolution_of_1848
- `/ledger/29 and /ledger/30`: 1853 start and 1854 end of the Crimean War occupation are confidence-1 bridges. Page to try: https://en.wikipedia.org/wiki/Crimean_War
- `/keyframe_review/4/note`: Amlas, Fagaras and Ciceu (Transylvanian fiefs held 'for long') are undated and undrawn. Page to try: https://en.wikipedia.org/wiki/Mircea_I_of_Wallachia

Spot checks:

- `/ledger/18` (https://en.wikipedia.org/wiki/Oltenia): confirmed (split from Wallachia and annexed as the Banat of Craiova; infobox 24,095 km2; Austrian occupation 'by 1716' also confirms /ledger/16)
- `/ledger/19` (https://en.wikipedia.org/wiki/Treaty_of_Belgrade): confirmed (signed 18 September 1739; Banat of Craiova ceded to the Ottomans; Wallachia page: Oltenia 'was returned to Wallachia in 1739'; the Oltenia page's 1737 is flagged in the author's notes)
- `/ledger/24` (https://en.wikipedia.org/wiki/Treaty_of_Adrianople_(1829)): confirmed (14 September 1829; Danube thalweg; 'the rule of the rayas of Turnu, Giurgiu and Braila' to Wallachia)
- `/ledger/3` (https://en.wikipedia.org/wiki/Basarab_I_of_Wallachia): confirmed (Posada 9-12 November 1330, ending Hungarian suzerainty); /ledger/1 (1325, Banate of Severin) and /ledger/0 (c. 1310 / 1304-1324) also confirmed
- `/ledger/8` (https://en.wikipedia.org/wiki/Michael_the_Brave): confirmed (18 October 1599); /ledger/7 (autumn 1594 Danube citadels) and /ledger/9 (Iasi 6 May 1600) also confirmed
- `/ledger/31` (https://en.wikipedia.org/wiki/Wallachia): confirmed ('neutral Austrian administration (1854-1856)'); /ledger/4 (c. 1400-1404), /ledger/28 ('until 1851') and /ledger/33 (5 February 1859) also confirmed

Area: No infobox area; the body gives 'approximately 77,000 km2' without a year, compared with the 1857 shape. The Oltenia step (24,164 km2 against the Oltenia infobox 24,095 km2) checks out.

## serbian-empire (fail)

Findings:

1. `/keyframe_review/4/correction` (open): The 1356-1371 correction removes {country: Albania} (about 28,700 km2, some 15 percent of the 1352 shape) but no ledger event removes Albania, and no page opened dates its loss. Evidence: Stefan Uros V page: no mention of Albania seceding, Karl Thopia or Durres; Serbian Empire page: losses undated ('gradually losing much of the conquered territory'); only the Maritsa page says that by 1371 Albania 'had entirely seceded'. /ledger/5 (Valona, 1355) covers only Valona. Fix: Either add loss event(s) for Albania with counterparts (Karl Thopia's lordship, the Balsic north, principality-of-valona) at a confidence that matches the undated secession, citing the Maritsa page and a page that dates it (Karl Thopia, Balsic), or keep Albania in the correction until a dated event.
2. `/ledger/8/region` (open): Region Epirus is not what the page says Simeon took in 1356: the page has him seize Kostur (Kastoria) and proclaim himself Tsar; Epirus went to Nikephoros II Orsini in 1356. Evidence: Stefan Uros V page: Simeon 'seized Kostur and proclaimed himself Tsar' and was 'retaking Epirus and Thessaly in 1359' (so he had lost them); despotate-of-epirus.json /ledger/45: 'Spring 1356: Nikephoros II restores the despotate'. Fix: Region of /ledger/8 = Kastoria ({lon: 21.27, lat: 40.52, km: 30, text: 'Kostur'}); add Epirus to /ledger/7's region (counterpart despotate-of-epirus), citing the Despotate of Epirus page in the note.
3. `/ledger/7/counterpart and /wars/3/belligerents` (applied by the reviewer): Counterpart 'Nikephoros II Orsini' is a person; the land went to the restored Despotate of Epirus, which has a dossier that records the mirror gain. Evidence: Stefan Uros V page: 'In the spring of 1356, Nikephoros Orsini landed a force on the coast of Thessaly and quickly overran it'; despotate-of-epirus.json /ledger/45 gains from serbian-empire in 1356. Fix: counterpart 'despotate-of-epirus' (done by the reviewer, with a sentence added to the note; the war's belligerent changed to match).
4. `/ledger/0/region and /ledger/5/region` (open): The Valona vassal region is Cliopatria's 'Principality of Valona and Kanina' 1395 shape, which lies east of Vlore and Kanine (bbox 19.70-21.21 E, 39.97-40.87 N; Vlore is at 19.49 E) and so leaves out the capital. Evidence: shapes.csv principality-of-valona-and-kanina_1395 bbox; Principality of Valona page: 'Area: the modern counties of Vlore (Valona), Fier, and Berat'. Fix: Region = union of {admin1: Vlore}, {admin1: Fier}, {admin1: Berat} (country Albania), text from the page.
5. `/ledger/3` (open): The 1348 Thessaly gain names only byzantine-empire, but the Catalan Duchy of Neopatras held southern Thessaly and its dossier records the loss to serbian-empire in 1348. Evidence: catalan-company.json /ledger/6: 'Most of the Duchy's possessions in Thessaly were lost when the region was conquered by the Serbs' (1348). Fix: Add a 1348 gain from catalan-company for the Catalan part of Thessaly (Neopatras), or say in the note why the Catalan land is excluded.

Gaps for a gap-filler:

- `/keyframe_review/0 and /identity/predecessors`: The date of the Serbian conquest of Albania (title 'King of Serbia, Albania and the coast' in 1343) is not on the pages. Page to try: https://en.wikipedia.org/wiki/Karl_Thopia
- `/ledger/10`: contest_end December 1371 is a confidence-1 bridge. Page to try: https://en.wikipedia.org/wiki/Marko_Mrnjav%C4%8Devi%C4%87

Spot checks:

- `/ledger/2` (https://en.wikipedia.org/wiki/Stefan_Du%C5%A1an): confirmed ('In 1347, Dusan conquered Epirus, Aetolia and Acarnania'); /ledger/3 (1348 Thessaly), /ledger/4 (1354, no district named: confidence 2 is right) and /ledger/6 (May 1355) also confirmed
- `/ledger/7` (https://en.wikipedia.org/wiki/Stefan_Uro%C5%A1_V): confirmed (spring 1356); /ledger/8: the quote is on the page but its region (Epirus) is not, see fixes
- `/ledger/11` (https://en.wikipedia.org/wiki/Serbian_Empire): confirmed (died childless 4 December 1371; empire 'effectively ended'); /ledger/1 (16 April 1346, Skopje) also confirmed; no infobox area
- `/ledger/0` (https://en.wikipedia.org/wiki/Principality_of_Valona): confirmed (vassal of the Serbian Empire 1346-1355); /ledger/5 (independent after Dusan's death in 1355) also confirmed

Area: No area on the Serbian Empire page (caption only: greatest extent circa 1355); the author says so in the 1352 keyframe note.

## moravian-serbia (thin)

Findings:

1. `/identity/rulers/1/source` (applied by the reviewer): Ruler Stefan Lazarevic had no source. Evidence: Serbian Despotate page: Stefan's death on 19 July 1427; Moravian Serbia page: despot title and state renamed in 1402. Fix: source https://en.wikipedia.org/wiki/Serbian_Despotate (done by the reviewer; URL already in sources).

Gaps for a gap-filler:

- `/keyframe_review/6`: The 1415 step (+20,228 km2) has no event. shapes.csv explains it: Cliopatria's Serbian Despots row drops from 27,340 km2 (Montenegro, Kosovo, Albania; serbian-despots_1402) to 6,993 km2 (Montenegro, Albania; serbian-despots_1415) in the same year (-20,347 km2), so the step is the Kosovo part of that row (the Brankovic lands) passing into this one. A gain from serbian-despots or the Brankovic district c. 1412-1415 with a page is needed. Page to try: https://en.wikipedia.org/wiki/District_of_Brankovi%C4%87
- `/ledger (1427)`: A loss is missing on a page the author opened: Serbian Despotate page, 'in the summer of 1427 ... The Ottomans occupied Krusevac and Nis'; also 'Fort Golubac ... lost ... in 1427'. Small (Krusevac about 4 percent of the shape; Cliopatria shows -0.7 percent in 1429), so a gap-filler can add it at confidence 3. Page to try: https://en.wikipedia.org/wiki/Serbian_Despotate
- `/ledger/7`: 1405 vassal_start of Zeta is confidence 1 (year of Balsa III's turn to Stefan not given). Page to try: https://en.wikipedia.org/wiki/Bal%C5%A1a_III
- `/ledger/1 and /ledger/5`: The 1375 shape's bbox starts at 19.1077 E, the same western edge as Kingdom of Syrmia's Macva, so Macva may already be inside the 1375 shape while /ledger/5 gains it only in 1404; the Moravian Serbia page also has the Drina as the north-western border and the state reaching the Sava and Danube. The 1379 Branicevo gain (/ledger/1, previous holder 'a Hungarian vassal' on the page) may likewise already be in the 1375 shape. Check against the geometry. Page to try: https://en.wikipedia.org/wiki/Banate_of_Ma%C4%8Dva

Spot checks:

- `/ledger/2` (https://en.wikipedia.org/wiki/Moravian_Serbia): confirmed (1386; the page's words are 'led much larger forces that took Nis from Lazar'); /ledger/0 (1371), /ledger/1 (1379 Branicevo and Kucevo) and the 1390 vassalage also confirmed; no area on the page
- `/ledger/5` (https://en.wikipedia.org/wiki/Serbian_Despotate): confirmed (Sigismund awarded Belgrade, Macva and Golubac, 1404)
- `/ledger/13` (https://en.wikipedia.org/wiki/Serbian_Despotate): confirmed (Smederevo fell 18 August 1439); /ledger/14 (Peace of Szeged 15 August 1444, 'borders were the same as before 1437'), /ledger/11 (Belgrade returned 1427), /ledger/12 (1428-1430) also confirmed
- `/ledger/15` (https://en.wikipedia.org/wiki/Serbian_Despotate): confirmed (Novo Brdo fell 1 June 1455); /ledger/17 (20 June 1459) confirmed; /ledger/16 confirmed with no date on the page (confidence 2 right)

Area: No area on the Moravian Serbia or Serbian Despotate pages (checked); the author says so.

## house-of-anjou-sicily (fail)

Findings:

1. `/keyframe_review/1 and /keyframe_review/2` (open): The 1279 (ok) and 1285 (adjust, 'unchanged shape, valid 1285-1288') keyframes keep the Albanian interior and Achaea, and no keyframe covers 1289-1293, so the 30,957 km2 shape is drawn to 1293, although the ledger loses the interior by 1282 (/ledger/3), Durres in 1288 (/ledger/5) and Achaea in 1289 (/ledger/6), and the note says 1289-1293 is the 725 km2 patch. Evidence: Kingdom of Albania (medieval) page: the Byzantine offensive 'drove the Angevins out of the interior by 1281'; 'Durres fell in Byzantine hands in 1288'; Principality of Achaea: granted to Isabelle and Florent in 1289. shapes.csv: house-of-anjou-sicily_1285 runs to 1293, bbox to 42.11 N (northern Albania). Fix: KF1 adjust: from 1282 without the Albanian interior (minus Albania except Durres and Vlore/Kanine), as a new keyframe 1282-1284 if needed; KF2 correction = the 1285 shape minus the Albanian interior, valid 1285-1288; new keyframe house-of-anjou-sicily_1289 (1289-1293) = the KF3 correction (Corfu, Butrint, Kanine).
2. `/ledger (1279)` (open): A gain on a page the author opened is missing: in March 1279 Nikephoros I of Epirus surrendered Sopot and Butrint to Charles. Evidence: Kingdom of Albania (medieval) page: 'in March 1279 Despot Nikephoros I declared himself a vassal of Charles of Anjou and surrendered to him the castles of Sopot and Butrint'; despotate-of-epirus.json /ledger/31 records the 1279 loss to house-of-anjou-sicily. Fix: Add gain 1279-03 (counterpart despotate-of-epirus, {place: Butrint ...} or a radius, confidence 3, that page); and either mirror despotate-of-epirus /ledger/33 (1294 dowry fortresses), /ledger/34 (1304 Butrinto and Naupaktos lost to Epirus) and /ledger/35 (1307) or say in notes that the Taranto lands are outside this row so the Epirus dossier can change its counterpart.
3. `/identity/capitals/0` (open): The capital Naples (14.27 E, 40.85 N) lies outside every shape of this row (the 1279 bbox starts at 14.34 E, and the land there is Malta). Evidence: Reviewer brief rule 9; Kingdom of Albania (medieval) infobox: 'Capital: Durazzo'. Fix: Capital Durres (19.45 E, 41.32 N) for the years the row holds it (1272-1288, 1304-1368, that page), and a seat inside the shapes for the other years (Corfu, or the Achaean capital for 1373-1383) from a page.
4. `/ledger/4/counterpart` (open): Malta's 1283 counterpart disagrees with the other side: this dossier says crown-of-aragon, kingdom-of-sicily.json /ledger/16 gains Malta in 1283 from kingdom-of-naples (confidence 1). Evidence: Battle of Malta (1283) page: 8 July 1283, the city put itself 'in the keeping and the command of the King of Aragon'; the page does not say which crown. Fix: Agree one pair with eu-12/kingdom-of-sicily: either crown-of-aragon here and a gain in crown-of-aragon, or kingdom-of-sicily here and house-of-anjou-sicily as that dossier's counterpart.
5. `/ledger/8/month` (applied by the reviewer): Month missing for the Angevin return to Durres. Evidence: Kingdom of Albania (medieval) page: Serbs expelled in summer 1304 and in September the city 'submitted themselves to Angevin rule'. Fix: month 9 (done by the reviewer).
6. `/ledger/3` (open): 'By 1282' differs from the Kingdom of Albania page's 'by 1281'. Evidence: Kingdom of Albania (medieval) page: 'drove the Angevins out of the interior by 1281'; the event cites the Capetian House of Anjou page, which the reviewer did not reopen. Fix: Check the cited page; use 1281 if it does not say 1282 (confidence 2 either way).

Gaps for a gap-filler:

- `/keyframe_review/5-7`: Corfu after 1292 is undated; the 1375-1383 shape leaves Corfu out although it stayed Angevin (Taranto line) until Venice took it in 1386. Page to try: https://en.wikipedia.org/wiki/Corfu
- `/keyframe_review/7`: The 1375 shape reaches central Greece, Euboea and the Cyclades (bbox to 25.57 E, 39.00 N), unsupported by the Achaea page; to settle with principality-of-achaea. Page to try: https://en.wikipedia.org/wiki/Principality_of_Achaea

Spot checks:

- `/ledger/1` (https://en.wikipedia.org/wiki/Kingdom_of_Albania_(medieval)): confirmed (Berat Byzantine from 1274; siege December 1280); /ledger/0 (late February 1272) also confirmed
- `/ledger/5` (https://en.wikipedia.org/wiki/Kingdom_of_Albania_(medieval)): confirmed ('Durres fell in Byzantine hands in 1288'); /ledger/7 (Kanine 'the last to fall to the Byzantines probably in 1294'), /ledger/8 (1304) and /ledger/9 (1368, Karl Thopia) also confirmed
- `/ledger/4` (https://en.wikipedia.org/wiki/Battle_of_Malta_(1283)): confirmed (8 July 1283, some sources 8 June; homage of the city and island; Gozo surrendered)

Area: No area on the dynasty or Kingdom of Albania pages; the author says so.

## kingdom-of-syrmia (fail)

Findings:

1. `/ledger/1/region and /keyframe_review/0-3` (open): The 1284 gain includes Usora and Soli ({place: Tuzla, km 40} and {admin1: Doboj}), roughly a quarter of the state's area, but every keyframe is the bare Cliopatria shape, whose bbox starts at 19.11 E: Tuzla (18.67 E) and Doboj (18.1 E) are outside it, so the ledger and the keyframes disagree for the whole life. Evidence: Stefan Dragutin page: 'Ladislaus IV of Hungary granted Macva, Usora and Soli to Dragutin in the second half of 1284'; shapes.csv kingdom-of-syrmia_1285/1294/1314 bbox 19.1077-22.1134 E. Fix: Either union Usora and Soli into KF0-KF3 (verdict adjust) for as long as the ledger holds them, or drop them from the gain region and say in the note and certainty that they were Hungarian fiefs (a vassal tint for Hungary's dossier).
2. `/keyframe_review/2` (open): Rudnik lost in 1301 and regained about 1312 (/ledger/3, /ledger/4; a 30 km radius, about 12 percent of the shape) sits inside the 1294-1313 shape marked ok. Evidence: Dragutin page: 'open war broke out and Milutin occupied Rudnik after taking it from Dragutin' (1301); peace 'most probably in 1312' restored 'his Serbian appanage (including the silver mine at Rudnik)'. Fix: Mark KF2 adjust with the 1301-1311 years drawn without Rudnik (a new keyframe), or say in the KF2 note why the step is left to the ledger.

Gaps for a gap-filler:

- `/keyframe_review/3, /ledger/6-7`: What happened to the land after Dragutin's death in 1316 (Milutin's seizure, Charles Robert's campaign of 1319) is on neither page; the shape runs unchanged to 1325. Page to try: https://en.wikipedia.org/wiki/Stefan_Vladislav_II
- `/ledger/2/counterpart`: The previous holders of Branicevo are named on the Dragutin page (Darman and Kudelin) but the counterpart reads 'Braničevo lords (page silent)'. Page to try: https://en.wikipedia.org/wiki/Darman_and_Kudelin
- `/identity/start`: The Syrmia page says 'Between 1282 and 1316, Syrmia was ruled by Stefan Dragutin' (tagged unreliable) and the Dragutin page has him keep the northern region including Rudnik at Dezevo in 1282; the 1284 start is defensible but the notes should mention 1282. Page to try: https://en.wikipedia.org/wiki/Stefan_Dragutin

Spot checks:

- `/ledger/1` (https://en.wikipedia.org/wiki/Stefan_Dragutin): confirmed (second half of 1284; 'unofficially styled King of Syrmia'; first Serbian monarch to rule Belgrade)
- `/ledger/3` (https://en.wikipedia.org/wiki/Stefan_Dragutin): confirmed (1301); /ledger/2 (1291 or 1292) and /ledger/4 (peace most probably 1312) also confirmed
- `/ledger/5` (https://en.wikipedia.org/wiki/Syrmia): confirmed ('In 1324, Vladislav II was defeated by Stefan Uros III Decanski'; Lower Syrmia disputed)
- `/ledger/6` (https://en.wikipedia.org/wiki/Syrmia): confirmed as 'Stefan Vladislav II (1316-1325)' (the page does not say 'ruling until 1325' in those words; confidence 2 right)

Area: The Syrmia page is the region's article and gives no area, capital or boundary for Dragutin's realm (checked).

## principality-of-valona (fail)

Findings:

1. `/keyframe_review/0-5/correction` (open): Every correction is Cliopatria's 'Principality of Valona and Kanina' 1395 shape, which lies east of the capital: its bbox is 19.70-21.21 E, 39.97-40.87 N, so Vlore (19.49 E), Kanine (19.52 E) and Fier (19.56 E) are outside it and it runs east to 21.21 E; the notes describe it as the three counties, which it is not. Evidence: shapes.csv principality-of-valona-and-kanina_1395 bbox; Principality of Valona page: capital Valona; 'Area: the modern counties of Vlore (Valona), Fier, and Berat'; the gazetteer has admin1 Vlore, Fier and Berat for Albania. Fix: Draw from the gazetteer instead: union of {admin1: Vlore}, {admin1: Fier}, {admin1: Berat} (country Albania) for 1346-1371, text from the page; verdict adjust on the two 1395 and 1415 shapes as well.
2. `/ledger (by 1372), /keyframe_review/2-5` (open): The page says the principality shrank after Berat fell to the Muzaka, but the dossier has no event and draws the full shape to 1417: about 6,000 km2 against Vlore county's 2,300-2,700 km2, a factor of more than two, unacknowledged. Evidence: Principality of Valona page: Berat 'had already fallen to the Muzaka', and the principality was 'confined to the area around Vlore, with Kanine, Himare and the fort of Pyrgos' (a footnote quoting a Montenegrin dictionary puts Berat in the 1372 dowry: the sources conflict, which the notes should say). Fix: Add a loss of Berat (and Fier) to the Muzaka by 1372 (confidence 2, that page; counterpart the Muzaka lordship of Berat, listed in counterparts_needing_dossiers or albanian-principalities), and a new keyframe 1372-1417 = {admin1: Vlore, country: Albania} with the page's words.
3. `/identity/rulers/1-5/source` (applied by the reviewer): Five rulers had no source. Evidence: Principality of Valona infobox lists the six rulers with these years. Fix: source https://en.wikipedia.org/wiki/Principality_of_Valona (done by the reviewer).

Spot checks:

- `/ledger/0` (https://en.wikipedia.org/wiki/Principality_of_Valona): confirmed ('Valona fell in late 1345 or early 1346'; Serbian conquest 1346)
- `/ledger/1` (https://en.wikipedia.org/wiki/Principality_of_Valona): confirmed (1372, Vlore and Kanine as Comita Muzaka's dowry)
- `/ledger/2` (https://en.wikipedia.org/wiki/Principality_of_Valona): confirmed (Savra 1385; Comita Muzaka 1385-1396); /ledger/3 and /ledger/4 also confirmed
- `/ledger/5` (https://en.wikipedia.org/wiki/Principality_of_Valona): confirmed ('until the Ottomans took the city in 1417')

Area: The infobox area is the three counties (no km2; gazetteer about 5,058 km2), close to the 1395 shape's size but not its place (the shape excludes Vlore); after 1372 the page's extent is Vlore county, about 2,300-2,700 km2, ratio about 2.2-2.6 against Cliopatria, not acknowledged.

## Cross-dossier matrix

| event | counterpart | mirror | status | note |
| --- | --- | --- | --- | --- |
| principality-of-wallachia 1325 gain | kingdom-of-hungary | none | exception | counterpart has no dossier yet; owned by a group that has not run yet (eu-15) |
| principality-of-wallachia 1400 gain | ottoman-empire | none | missing | ottoman-empire.json (me-10) has no c. 1400 loss of Dobruja/Silistra to Wallachia (nor the 1404 regain) |
| principality-of-wallachia 1404 loss | ottoman-empire | none | missing | see 1400 |
| principality-of-wallachia 1594 gain | ottoman-empire | none | missing | ottoman-empire.json has no 1594 loss of Giurgiu, Braila, Harsova, Silistra (nor the 1601 regain) |
| principality-of-wallachia 1601 loss | ottoman-empire | none | missing | see 1594; confidence-1 bridge on this side |
| principality-of-wallachia 1599 occupation_start | principality-of-transylvania | none | exception | counterpart has no dossier yet; owned by a group that has not run yet (eu-15); the author asks for the reverse event |
| principality-of-wallachia 1600 occupation_start | principality-of-moldavia | none | exception | counterpart has no dossier yet; owned by a group that has not run yet (eu-18) |
| principality-of-wallachia 1716 occupation_start | habsburg-monarchy | none | missing | habsburg-monarchy.json (eu-09) has no 1716 occupation of Oltenia (it starts the war at 1716-08 as a contest with ottoman-empire) |
| principality-of-wallachia 1718 loss | habsburg-monarchy | habsburg-monarchy 1718 gain | matched | habsburg-monarchy /ledger/67, 21 July 1718, Oltenia |
| principality-of-wallachia 1739 gain | habsburg-monarchy | habsburg-monarchy 1739 loss | matched | habsburg-monarchy /ledger/80, 18 September 1739 |
| principality-of-wallachia 1769 occupation_start | russian-empire | none | exception | counterpart has no dossier yet; owned by a group that has not run yet (eu-17); the same for the occupations of 1806, 1829, 1848 and 1853 |
| principality-of-wallachia 1789 occupation_start | habsburg-monarchy | none | missing | not in either dossier: habsburg-monarchy /ledger/105 says the Austrians occupied Bucharest in the 1788-91 war; Wallachia needs the event (see its fixes) |
| principality-of-wallachia 1829 gain | ottoman-empire | none | missing | ottoman-empire.json /ledger/175 (1829) records only losses to russian-empire, not the rayas of Turnu, Giurgiu and Braila to Wallachia |
| principality-of-wallachia 1854 occupation_start | austrian-empire | none | exception | counterpart has no dossier yet; owned by a group that has not run yet (eu-20) |
| principality-of-wallachia 1859 merge | principality-of-moldavia | none | exception | counterpart has no dossier yet; owned by a group that has not run yet (eu-18) |
| serbian-empire 1346 vassal_start | principality-of-valona | none | exception | suzerain-side event per the schema (counterpart is the vassal); principality-of-valona need not mirror it |
| serbian-empire 1347 gain | byzantine-empire | byzantine-empire 1352 loss | mismatch | byzantine-empire.json (eu-05) has only /ledger/179, a confidence-1 loss of Macedonia to serbian-empire in 1352; no 1347 Epirus/Aetolia-Acarnania or 1348 Thessaly loss, although its /ledger/177 has Epirus Byzantine again from 1340 |
| serbian-empire 1348 gain | byzantine-empire | none | missing | see 1347; also catalan-company /ledger/6 loses its Thessalian possessions to serbian-empire in 1348 with no mirror here |
| serbian-empire 1354 occupation_start | kingdom-of-hungary | none | exception | counterpart has no dossier yet; owned by a group that has not run yet (eu-15) |
| serbian-empire 1356 loss | despotate-of-epirus | despotate-of-epirus 1356 gain | matched | after the reviewer changed the counterpart from the person Nikephoros II Orsini; despotate-of-epirus /ledger/45 |
| serbian-empire 1356 loss | Simeon Uroš (Emperor of Serbs and Greeks) | none | mismatch | listed in the author's counterparts_needing_dossiers, but despotate-of-epirus.json treats Simeon as serbian-empire (/ledger/46 and /ledger/48: 1359 losses to serbian-empire; /ledger/49: 1367 gain from serbian-empire); one reading must win (eu-05 and eu-18) |
| serbian-empire 1371 contest_start | ottoman-empire | ottoman-empire 1371 gain | matched | ottoman-empire /ledger/12 (26 September 1371, gain from serbian-empire); this side carries it as a contest and the dissolve successor ottoman-empire for Macedonia |
| moravian-serbia 1379 gain | Braničevo lords (Radič Branković Rastislalić, ousted 1379) | none | missing | no dossier and not in counterparts_needing_dossiers; the page calls Radic a Hungarian vassal (kingdom-of-hungary, eu-15) or use nobody |
| moravian-serbia 1386 loss | ottoman-empire | ottoman-empire 1386 gain | mismatch | ottoman-empire /ledger/15 has the 1386 Nis gain with counterpart serbian-despots (likewise /ledger/17 1390 vassal, /ledger/46-47 1459): me-10 should use moravian-serbia for Lazar's and the Despots' state |
| moravian-serbia 1397 gain | Vuk Branković | none | missing | no dossier and not listed; Cliopatria's Serbian Despots row (serbian-despots, eu-18) looks like the Brankovic district plus Zeta (see the 1415 step), so serbian-despots may be the counterpart |
| moravian-serbia 1404 gain | kingdom-of-hungary | none | exception | counterpart has no dossier yet; owned by a group that has not run yet (eu-15); also 1411 and 1427 |
| moravian-serbia 1421 gain | serbian-despots | none | exception | counterpart has no dossier yet; owned by a group that has not run yet (eu-18) |
| moravian-serbia 1439 occupation_start | ottoman-empire | none | missing | ottoman-empire.json has no 1439-1444 occupation of Serbia |
| moravian-serbia 1455 loss | ottoman-empire | none | missing | ottoman-empire.json has no 1455 Novo Brdo gain |
| moravian-serbia 1458 loss | kingdom-of-bosnia | none | exception | counterpart has no dossier yet; owned by a group that has not run yet (eu-18) |
| moravian-serbia 1459 dissolve | ottoman-empire | ottoman-empire 1459 gain | mismatch | ottoman-empire /ledger/46 gains in 1459 from serbian-despots (confidence 1): counterpart should be moravian-serbia |
| house-of-anjou-sicily 1274 loss | byzantine-empire | none | missing | byzantine-empire.json has no 1274 Berat, 1281/82 Albanian interior, 1288 Durres or 1294 Kanine gain from house-of-anjou-sicily (its /ledger/160 gains Albania c. 1280 from despotate-of-epirus instead) |
| house-of-anjou-sicily 1278 gain | principality-of-achaea | principality-of-achaea 1278 rename | mismatch | principality-of-achaea (eu-05) keeps Achaea as its own state under Angevin princes (renames 1278, 1289, 1383) and draws 1279-1293 and 1326-1384 itself with new keyframes, asking this row to drop it; this dossier draws Achaea 1279-1288 and 1375-1383: double draw (flagged by the author) |
| house-of-anjou-sicily 1289 loss | principality-of-achaea | principality-of-achaea 1289 rename | mismatch | see 1278 |
| house-of-anjou-sicily 1373 gain | principality-of-achaea | none | mismatch | see 1278; principality-of-achaea has no 1373 event |
| house-of-anjou-sicily 1279 gain | despotate-of-epirus | despotate-of-epirus 1279 loss | missing | despotate-of-epirus /ledger/31 loses Butrint to house-of-anjou-sicily in 1279; no gain here (page has it). Also unmirrored: Epirus /ledger/33 (1294 loss), /ledger/34 (1304 gain), /ledger/35 (1307 loss), /ledger/39 (1331 overlordship) |
| house-of-anjou-sicily 1283 loss | crown-of-aragon | kingdom-of-sicily 1283 gain | mismatch | crown-of-aragon.json has no 1283 Malta gain; kingdom-of-sicily /ledger/16 gains Malta in 1283 from kingdom-of-naples (confidence 1) |
| crown-of-aragon 1282 gain | house-of-anjou-sicily | none | mismatch | crown-of-aragon /ledger/27 takes Sicily from house-of-anjou-sicily, but Sicily is not in this row (it is kingdom-of-sicily / kingdom-of-naples): eu-12 should change the counterpart |
| house-of-anjou-sicily 1304 gain | kingdom-of-serbia | none | exception | counterpart has no dossier yet; owned by a group that has not run yet (eu-18) |
| house-of-anjou-sicily 1368 loss | Karl Thopia (Principality of Albania) | none | missing | no dossier and not in counterparts_needing_dossiers; possibly albanian-principalities (Cliopatria from 1375, eu-18) |
| kingdom-of-syrmia 1284 gain | kingdom-of-hungary | none | exception | counterpart has no dossier yet; owned by a group that has not run yet (eu-15) |
| kingdom-of-syrmia 1291 gain | Braničevo lords (page silent) | none | missing | the page names Darman and Kudelin; not listed in counterparts_needing_dossiers |
| kingdom-of-syrmia 1301 loss | kingdom-of-serbia | none | exception | counterpart has no dossier yet; owned by a group that has not run yet (eu-18); also the 1312 gain |
| principality-of-valona 1346 found | byzantine-empire | none | missing | byzantine-empire.json has no 1345/46 loss of Valona (or Albania) to serbian-empire |
| principality-of-valona 1417 dissolve | ottoman-empire | none | missing | ottoman-empire.json has no 1417 gain of Valona |

## Problems for the orchestrator

- No page failed to load for the reviewer.
- Reviewer edits (all re-validated, 0 errors, 0 warnings): serbian-empire /ledger/7 counterpart and /wars/3 belligerent -> despotate-of-epirus; moravian-serbia /identity/rulers/1 source; principality-of-valona /identity/rulers/1-5 source; house-of-anjou-sicily /ledger/8 month 9. Backups in /tmp/claude-0/work/review-eu-18-d/bak/.
- Naming conflict across groups: ottoman-empire (me-10) calls Lazar's and the Despots' state serbian-despots (1386 Nis, 1390 vassal, 1459 gain and vassal_end) while this batch splits Cliopatria's Serbian Empire row into serbian-empire and moravian-serbia; Cliopatria's Serbian Despots row (1375-1421) looks like the Brankovic district plus Zeta (its 1415 drop of 20,347 km2 equals moravian-serbia's 1415 gain of 20,228 km2). The orchestrator should fix which slug means what before eu-18 writes serbian-despots.
- Double draw of Achaea: principality-of-achaea (eu-05) draws 1279-1293 and 1326-1384 with new keyframes and treats the Angevin years as renames; house-of-anjou-sicily draws Achaea 1279-1288 and 1375-1383. One of the two must give way.
- despotate-of-epirus (eu-05) counts Simeon Uros as serbian-empire after 1356 (1359 losses, 1367 gain); serbian-empire treats him as a breakaway ruler from 1356. Needs one reading.
- crown-of-aragon (eu-12) /ledger/27 takes Sicily in 1282 from house-of-anjou-sicily, which never held Sicily in this row.
- byzantine-empire (eu-05), ottoman-empire (me-10) and habsburg-monarchy (eu-09) lack many mirror events (see cross_checks with status missing).
- kingdom-of-serbia (eu-18) still draws 1346-1351 as the kingdom while serbian-empire starts in April 1346 (author's flag, still open: kingdom-of-serbia has no dossier yet).

## Gazetteer names needed

- Kastoria (Kostur) (place, serbian-empire)
- Kruševac (place, moravian-serbia)
- Smederevo (place, moravian-serbia)
- Niš (place, moravian-serbia)
- Golubac (place, moravian-serbia)
- Srebrenica (place, moravian-serbia)
- Zeta (region, moravian-serbia)
- Kanina (place, principality-of-valona)
- Butrint (place, house-of-anjou-sicily)
- Usora and Soli (region, kingdom-of-syrmia)
- Aetolia and Acarnania (region, serbian-empire)
- Turnu Măgurele (place, principality-of-wallachia)
- Rudnik (place, kingdom-of-syrmia)
