# eu-14-f: Teutonic Order, Danish Magnates, Kalmar Union, Livonian Conference, House of Oldenburg (+ Prussian Confederation)

Written 2026-10-25 by the Phase B agent for batch eu-14-f. All six dossiers validate (`python3 -I history/tools/validate_dossier.py`); `--resolve` finds no unknown name except the two intentional empty corrections (now in kalmar-union, see REVIEW REPAIRS at the end: house-of-oldenburg is merged into it). Pages are Wikipedia, opened with WebFetch in this run (accessed 2026-10-25).

## teutonic-order (1230..1525, 35 events, 28 keyframes, 21 pages listed: budget 9, 10 used in the first pass, the rest opened for the review repairs)
- Cliopatria has one row for Prussia plus Livonia to 1421; from 1422 the Livonian branch is the separate row `livonian-conference` (the split is Cliopatria's, page silent: ledger `split` 1422 at confidence 1).
- Shape dates and page dates differ (Pomerelia 1308-09 vs shape 1314; Kuyavia-Dobrzyn 1329-32 vs 1333; Estonia 1 Nov 1346 vs 1352; Gotland and Samogitia 1398 vs 1402; Neumark sold 1455 vs 1459; Marienburg lost 1457 and Warmia 1466 vs 1463/1468); the dossier adds keyframes with page dates. 1241 shape reaches Pskov and Leningrad oblasts; no page says the Order held them (adjusted out, low confidence).
- Capitals disagree: Order page Marienburg 1309-1466; State page Marienburg 1308-1454, Konigsberg from 1454; war page: Marienburg castle handed to the Polish army 6 June 1457. Followed the State page. No seat in Prussia before 1309 is named on any page opened; Acre and Venice (headquarters) were dropped from the capitals on review.
- Unsettled: Treaties of Salynas (1398), Raciaz (1404) and Brest (1435), the Dobrzyn pledges (1392-1405, 1409-1411: only the State page's table), the end of the Great Prussian Uprising (page: central tribes surrendered by 1277), Sudovia 1283 (left unpopulated, not drawn). Grand Master list added on review (Grand Master page).
- Conflict to check: the Wolter von Plettenberg page says Harju, Virumaa and Tallinn were under the Prussian Grand Master until 1525; the Livonian Order page says the Livonian order bought Estonia in 1346; the State and Danish Estonia pages say the Teutonic Order did. Cliopatria draws Estonia in the Livonian row from 1422. Not adopted (one page).
- The Order's fief of Poland 1466-1525 is a vassal_start/vassal_end pair here too since the review (counterpart house-of-jagiellon, which carries the mirror); the Holy Roman Empire dossiers carry Cliopatria's allegiance of the Order 1305-1401 and umbrella membership 1236-1458.
- The first Pomerelia URL ("Teutonic takeover of Pomerelia") did not load; "Teutonic takeover of Danzig (Gdansk)" did.

## danish-magnates (1332..1351, 5 events, 3 keyframes, 2 pages)
- Not the modern Denmark: Cliopatria gives both the Wikidata id Q350186 (data/README.md), but the modern row is 1945-2024. This row is the Danish interregnum's fragment, a member of the umbrella (Kingdom of Denmark), and is its own dossier.
- Row content: the Estonian province 1333-1343 and a 4,720 km2 sliver of southern Jutland 1344-1351. The Estonian province was Danish until 1 Nov 1346 (sale), so 1332 and 1344-1346 are added by correction. The 1344-1351 Jutland sliver is unverified (page silent; Christopher II page only says mortgagees held Denmark for "the next eight years").
- Pages give no date for Waldemar IV's accession (1340), Scania's pledge to Sweden, or Bornholm.

## kalmar-union (1397..1523, 20 events, 25 keyframes, 9 pages; untouched by the review except the Oldenburg merge)
- Union dated 17 June 1397 (page) against Cliopatria's 1402; ends 6 June 1523 (Gustav Vasa elected) against Cliopatria's 1525; Denmark-Norway "established 1523" per the infobox while Cliopatria's Denmark-Norway row starts 1526 (1524-1525 undrawn: the denmark-norway dossier should start in 1523 or take the union's Danish-Norwegian shape).
- Personal union of three kingdoms: with start 1397 it overlaps the Old Kingdom of Norway and Kingdom of Sweden rows (to 1401) and Kingdom of Denmark (to 1406).
- Sweden and Finland were the union's only 1397-1447, June 1457-June 1464, Oct 1497-Aug 1501 and Nov 1520-1523 (contested from Jan 1521). Cliopatria draws them in the union through 1459-1501 and 1521-1525 and has a Kingdom of Sweden row only for 1502-1520: the kingdom-of-sweden dossier should draw Sweden for 1448-1457, 1464-1497, 1501-1520, 1521-1523.
- Schleswig: ceded to the count of Holstein 17 July 1435, regained by Christian I in 1460 (Ribe, 5 March). Counterpart "Counts of Holstein (Holstein-Rendsburg)" has no dossier.
- Orkney and Shetland to Scotland 1472 (footnote 1470). Gotland bought from the Teutonic Order 1408 (State of the Teutonic Order page). Greenland cells in the 1402-1428 shape dropped in 1429: page silent (conf 1).
- Not settled: the +315,000 km2 jump of 1429 (northern lands entering the drawing), the +58-cell Finnish jump of 1475, Eric of Pomerania's ten years on Gotland (no dates), the capital (undated), a ruler list, Iceland and the Faroes.

## house-of-oldenburg (1450..1458, 2 events, 2 keyframes, 2 pages) - SUPERSEDED: merged into kalmar-union on review; the file is still on the mount because the author's delete was refused
- Not a separate state: Cliopatria's Kalmar Union and House of Oldenburg rows share the Seshat polity sv_kalmar_union and one realm under Christian I. Dynasty change is a `rename` (1 Sept 1448) in the kalmar-union dossier; both Oldenburg shapes are marked wrong with an empty correction (the validator's --resolve warns "resolves to no cells" twice, intentionally). The 1450 shape also wrongly includes Sweden and Finland (Karl Knutsson ruled Sweden 1448-1457); the 1453 shape is Sweden proper and southern Finland, right only from 23 June 1457. If the renderer wants a separate dynasty colour the lands would be Norway 1450-1456 and the Swedish realm 1457-1458 (and the Kalmar keyframes must drop them).
- The 1458 end is Cliopatria's (page silent, confidence 1).

## livonian-conference (1422..1561, 15 events, 8 keyframes, 10 pages after the review repairs)
- Cliopatria's Wikipedia title ("Livonian language") and Wikidata id (Q33698) are the language's. Article used: Livonian Confederation (the URL returned the Terra Mariana article, which gives the 1419 Diet, the Walk agreement of 4 Dec 1435, areas of about 67,000 km2 for the Order and 41,000 km2 for the Church).
- Start 1422 is Cliopatria's boundary (page silent); end 28 Nov 1561 (Treaty of Vilnius) against Cliopatria's 1563. Livonian War partition is drawn by keyframes 1558, 1559, 1561 (Dorpat and Narva to Russia 1558; Osel to Denmark 26 Sept 1559; northern Estonia to Sweden 1561; Livonia and Courland to Poland-Lithuania 28 Nov 1561).
- The Russo-Livonian War (1501-1503) pages ("Russo-Livonian_War_(1501-1503)", "Russo-Livonian_War") did not load; the Wolter von Plettenberg page gave the 1503 status quo.
- Wanted from other groups: house-of-jagiellon vassal/protectorate for 31 Aug 1559 (first Treaty of Vilnius); a duchy-of-courland dossier starting 1561 (Cliopatria row is 1734-1793); Duchy of Livonia (1561-1621) and Riga (free imperial city, Polish from 1581) have no rows.

## prussian-confederation (new rebel state, 1454..1466, 6 events, 1 keyframe)
- League of Prussian towns and nobles (founded at Marienwerder 14 March 1440), in revolt from Feb 1454, incorporated into Poland (act of March 1454), ended with the Second Peace of Thorn (19 Oct 1466; the war page's text says 10 Oct). Counterpart of the Order's contest events. Its land is the "West Prussia" region (approximation; no year-by-year map on the pages); no capital named; Wikidata id unknown.

## Gazetteer names wanted
Pomesania (region), Neumark (region), Samland (region), Chelmno Land (region), Dobrzyn Land (region), Harrien-Wierland / Harria and Vironia (region), Nieszawa (place), Kwidzyn (place).

## REVIEW REPAIRS 2026-10-25 (author, batch eu-14-f-fixed; read with review-eu-14-f.md)

Pages re-opened with WebFetch on 2026-10-25 for every date, region or source changed. All five touched files validate (0 errors; kalmar-union has the 2 intentional 'resolves to no cells' warnings).

### Applied
- teutonic-order: vassal_start 1466-10 and vassal_end 1525-4 (counterpart house-of-jagiellon; Second Peace of Thorn page 'The eastern part remained with the Teutonic Order as a fief of the Polish Crown', 19 October 1466; State page 'Prussian Homage ... 10 April 1525'). Capitals Acre and Venice dropped and the 1291 capital_move deleted (no page names a Prussian seat before 1309; the 1230-1308 stretch has no capital). Gotland 1398 counterpart is now the free text 'Victual Brothers' (Victual Brothers page: occupied Gotland 1394, driven out 1398; Teutonic Order page: Albert's pledge). K1 split: teutonic-order_1236 valid for 1236 only, new teutonic-order_1237 (1237-1240) with the union. Grand Master rulers added. Samogitia 1398 dated 12 October 1398 (Treaty of Salynas page, confidence 3).
- livonian-conference: vassal_start 1559-8 / vassal_end 1561-11 (counterpart house-of-jagiellon); Fellin (Viljandi county) lost to Russia in 1560 with a second Russian contest pair, new keyframe livonian-conference_1560, carried into 1561; the 1559 sale takes the whole Bishopric of Osel-Wiek (Saare, Hiiu, Lääne), in the ledger, the keyframes and the Danish successor; the 1559 keyframe is 1559 only.
- prussian-confederation: vassal_start 1454-3 / vassal_end 1466-10 (counterpart house-of-jagiellon). Of the reviewer's two options I took the first (keep the dossier, client of Poland), because the Prussian Confederation page has it 'ceased to exist as such' only after 1466; the pages say incorporation, not vassalage, so confidence 2.
- house-of-oldenburg: merged into kalmar-union (cliopatria_names, both shape verdicts moved, notes). The delete of house-of-oldenburg.json was refused by the permission system, so the file stays with a SUPERSEDED note in its notes; the orchestrator should delete it.

### Disagreements, with the page
- Pskov and Leningrad cells (teutonic-order K2 vs L3): the review read the Battle on the Ice page as the Order holding Pskov 1240-1242. The page says Pskov fell in September 1240 to Prince Yaroslav 'and the men from the bishopric of Dorpat', does not name the holder of Koporye, and has Alexander 'retake both Votia and Pskov' 'during the campaign of 1241'. I kept K2 (cells removed from 1241) and deleted the 1242 loss, the reviewer's second option.
- First Treaty of Vilnius: the Livonian War page says June 1559 and never mentions 31 August (the earlier note's 31 August came from the Treaty of Vilnius (1561) page: 'the Treaty of Vilnius of 31 August 1559'). livonian-conference uses 1559-8 from that page; house-of-jagiellon has 1559-6. The Treaty_of_Vilnius_(1559) and Pacta_subjectionis pages do not load.
- Fellin: the Livonian War page says 'The Tsar's forces took important fortresses like Fellin (Viljandi)' without a date; the Viljandi page gives 1560 ('Andrey Kurbsky ... succeeded in seizing'); the Battle of Ērģeme page (2 August 1560) does not mention Fellin. So the loss is year-only, confidence 2, and the review's 'August 1560' is the battle, not the capture.
- Pilten: not added to the livonian-conference 1559 loss. The Livonian War page says only that Magnus 'later' bought the Bishopric of Courland; the Magnus of Livonia and Osel-Wiek pages give no date for it and the Osel-Wiek page does not mention Pilten. denmark-norway's 1559 gain names 'Courland's Pilten' at confidence 2 and its author should date or drop it.

### Thin items worked
- Michałów Land: lien 1303, bought 1317 from the Duke of Kuyavia, back to Poland after the Second Peace of Thorn (Michałów Land page; no mention of Kalisz). No event: Cliopatria's Teutonic Order shape holds the Nowe Miasto Lubawskie area (3 of 3 cells of a 15 km circle at 19.59 E 53.42 N) from 1236, and the 1466 loss already covers it through the Chełmno region.
- Dobrzyń Land: the State page's table is the only source for 1392-1405 and 1409-1411; the Dobrzyń Land page confirms 1326-1332, the 1343 return and 'temporarily regained control' in 1409-1411 and a return under the Peace of Thorn. Not drawn: Cliopatria's Teutonic Order shapes of 1352-1415 hold 1 of the 52 cells (13,151 km2) of Kuyavia-Dobrzyń, no page names the pledger or the terms of 1392, and the gazetteer has no Dobrzyń Land. A gap-filler needs new keyframes for 1392-1405 and 1409-1410 and a name.
- Peace of Brześć Kujawski (31 December 1435): 'did not change borders determined by the Treaty of Melno'; no event. Treaty of Melno (27 September 1422): 'separated the Teutonic Knights in Prussia from their branch in Livonia' and nothing about a split; the 1422 split and found events stay confidence 1.
- Harrien-Wierland: the Wolter von Plettenberg page again says Harju, Virumaa and Tallinn were 'under the sovereignty of the Grand Master in Prussia' until 1525; the Danish Estonia page has the sovereignty pass to the Teutonic Order on 1 November 1346 and no 1347 transfer. Still open; Cliopatria's 1422 split unchanged.
- Grand Master list: Grand Master of the Teutonic Order page (1209-1525; Burchard 1282 or 1283 and Ludwig von Erlichshausen 1449 or 1450 given as the later year).

### Pages that did not load
Peace of Raciąż (1404) under 'Treaty_of_Raci%C4%85%C5%BC' and 'Peace_of_Raci%C4%85%C5%BC'; Russo-Livonian War (1501-1503) under 'Russo-Livonian_War_(1501%E2%80%931503)', 'Battle_of_Smolino' and 'Battle_of_Lake_Smolino'; 'Treaty_of_Vilnius_(1559)' (returned only a reference list) and 'Pacta_subjectionis'.

### For other batches
- house-of-jagiellon (eu-15): vassal_start 1454-3 / vassal_end 1466-10 with counterpart prussian-confederation to mirror it.
- denmark-norway: date or drop Pilten in the 1559 gain; livonian-conference now loses the whole bishopric (Saare, Hiiu, Lääne).
- tsardom-of-russia (eu-16): gains Fellin (Viljandi) in 1560 from livonian-conference; duchy-of-livonia already carries the contest from 1561.
- Counterparts needing dossiers: Victual Brothers (Gotland 1394-1398), plus the earlier list (royal-prussia, county-of-holstein, duchy-of-courland, duchy-of-livonia, riga).
