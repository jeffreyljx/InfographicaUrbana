# Review of batch eu-14-h (2026-10-31)

Reviewer: adversarial review, Phase B. Dossiers: swedish-empire (fail), duchy-of-courland (fix, applied by the reviewer). Validator: both 0 errors; one warning (Wismar not in the gazetteer).

## swedish-empire: fail

Spot checks: /ledger/1 confirmed (Treaty_of_Stolbovo); /ledger/10, /ledger/11, /ledger/12 confirmed (Treaty_of_Br%C3%B6msebro_(1645)); /ledger/13 confirmed (sentence on page; double gain, see fixes) (Treaty_of_Br%C3%B6msebro_(1645)); /ledger/21, /ledger/22 confirmed (Treaty_of_Roskilde); /ledger/23, /ledger/24 confirmed (Swedish_Empire); /ledger/30, /ledger/31, /ledger/32 confirmed (Great_Northern_War); /ledger/35, /ledger/36 confirmed (Great_Northern_War); /ledger/38 confirmed (Great_Northern_War); /ledger/40 confirmed (Swedish_Empire).

Area: page 1100000 km2 (year 1661), Cliopatria 921329 km2, ratio 0.84, acknowledged.

### Findings

- **/ledger/17/counterpart** (applied by reviewer): Counterpart slug 'duchy-of-mecklenburg' is the 1806-1870 state (eu-20, not written); the Mecklenburg of 1648 is the dossier 'mecklenburg' (1170-1805). Evidence: mecklenburg.json L7: 1648 loss cp swedish-empire, 'the town of Wismar with Poel and Neukloster' (conf 3); mecklenburg dissolves into duchy-of-mecklenburg only in 1805. Fix: counterpart 'mecklenburg' (done; re-validated, 0 errors).
- **/ledger/4, /ledger/16** (author to fix): Pomerania is gained twice (1630 and October 1648, both from duchy-of-pomerania), and the 1648 counterpart no longer exists: duchy-of-pomerania records a Swedish occupation from 1630 and its own dissolution to swedish-empire in March 1637. Evidence: duchy-of-pomerania.json L8 1630 occupation_start cp swedish-empire (conf 3), L9 1637-3 occupation_end, L10 1637-3 dissolve cp swedish-empire; nothing mirrors L16. Swedish Empire page: Pomerania 'in its possession since the Treaty of Stettin (1630)'. Fix: Make L4 an occupation_start 1630 cp duchy-of-pomerania; add occupation_end + gain 1637-3 cp duchy-of-pomerania (Western Pomerania); turn L16 into no event (or a gain with a counterpart alive in 1648, e.g. brandenburg-prussia renouncing its claim, said so in the note). One gain of Western Pomerania in the ledger, not two.
- **/ledger/13, /ledger/18, /ledger/19** (author to fix): Bremen-Verden is gained twice (August 1645 from denmark-norway, October 1648 from the two bishoprics); no neighbour mirrors the 1645 gain from Denmark-Norway. Evidence: Brömsebro page does say 'The Imperial Prince-Bishopric of Verden and Bremen were transferred from Danish to Swedish control', but denmark-norway's 1645 losses (L17-L19) are Jämtland/Härjedalen, Gotland/Saaremaa and Halland only; prince-archbishopric-of-bremen L10-L11 records a Swedish occupation 1643 to 1648-5 and dissolve cp swedish-empire; holy-roman-empire-minor-states L65 a 1645 loss (conf 1). Fix: Make L13 an occupation_start 1645-8 cp prince-archbishopric-of-bremen (plus one cp prince-bishopric-of-verden), naming the Danish administrator in the note, and add the matching occupation_end events at 1648-10 before L18/L19, so the land is gained once.
- **/ledger/33** (author to fix): 1713 loss cp denmark-norway (conf 1) of 'Swedish Germany outside northern Pomerania' gives southern Pomerania to Denmark, and the same land is lost again in L35 (1719) and L36 (1720). Evidence: denmark-norway L28/L30: occupation of Bremen-Verden only, 1712-1715 (conf 3); electorate-of-hanover L3/L4: occupation 1715-1719; kingdom-of-prussia L4/L5: occupation of southern Swedish Pomerania 1715 to 1720-1. GNW page dates only the 1719 and early-1720 cessions. Fix: Replace L33 by occupation_start 1712 / occupation_end 1715 cp denmark-norway (Bremen-Verden), occupation_start 1715 / occupation_end 1719 cp electorate-of-hanover (Bremen-Verden, before L35), occupation_start 1713 or 1715 / occupation_end 1720-1 cp kingdom-of-prussia (southern Pomerania, before L36); keyframe 20 then needs no de facto loss.
- **/ledger (1715-1720), /keyframe_review/21, /keyframe_review/22** (author to fix): Northern Swedish Pomerania (Stralsund, Rügen) and Wismar, lost to the allies in December 1715 and 1716 and returned in 1720, have no occupation events; the 1714-1720 keyframes keep them Swedish. Evidence: Great Northern War page (opened by the author): Charles XII stayed in Stralsund 'until December 1715, escaping only days before Stralsund fell'; 'When Wismar surrendered in 1716, all of Sweden's Baltic and German possessions were lost.' Fix: Add occupation_start 1715-12 (Stralsund and Rügen) and 1716 (Wismar) cp denmark-norway / kingdom-of-prussia as the page names them, with occupation_end 1720 (Treaty of Frederiksborg / Stockholm); route the mirror to eu-14-g (denmark-norway has no such events).
- **/ledger (1679), /keyframe_review/14** (author to fix): The 1679 cession of the strip east of the Oder to Brandenburg is missing; keyframe 14 notes the two-cell change with 'no event behind it'. Evidence: brandenburg-prussia L9: 1679-6 gain cp swedish-empire, 'the former Swedish eastern bank of the Oder, except Gollnow and Damm' (conf 3). Swedish Empire page: Westphalia granted 'a strip of Farther Pomerania on the right side of the Oder'; Saint-Germain dated 29 June 1679. Fix: Add loss 1679-6 cp brandenburg-prussia, region the 1670 shape minus the 1683 shape (the strip east of the Oder), source the Swedish Empire page.
- **/ledger (1630-1653)** (author to fix): Farther Pomerania, held by Sweden until the Treaty of Stettin of 1653, has no Swedish event; brandenburg-prussia gains it from swedish-empire in 1653. Evidence: brandenburg-prussia L2/L5/L6: contest 1648-10 to 1653 and 1653 gain cp swedish-empire, 'Farther Pomerania' (conf 3). Swedish Empire page names 'the Treaty of Stettin in 1653'. Cliopatria does not draw it Swedish, so it is an occupation. Fix: Add occupation_start (1630 or 1637) and occupation_end 1653 for Farther Pomerania with counterpart brandenburg-prussia, or argue in notes why not and route to eu-09.
- **/ledger (1612-1617), /wars/0** (author to fix): The Swedish occupation of Novgorod (from July 1611) and Gdov (1614), returned at Stolbovo, is not in the ledger although the Ingrian War outcome names it. Evidence: tsardom-of-russia L42 1611-7 occupation_start 'Novgorod', L45 1614 'Gdov', L46/L47 1617-3 occupation_end, all cp swedish-empire, conf 3. Stolbovo page: 'Novgorod and other Swedish territorial gains during the war would be returned to Russia.' Fix: Add occupation_start 1612 (note: began July 1611, before this dossier) and 1614 (Gdov) cp tsardom-of-russia, and occupation_end 1617-3 for both.
- **/ledger (1658-1660), /wars** (author to fix): The Swedish hold on the Duchy of Courland 1658-1660 (this batch) has no mirror here, and the Second Northern War's Polish front (1655-1660) is not among the wars. Evidence: duchy-of-courland L1/L2: occupation_start 1658 / occupation_end 1660 cp swedish-empire; Courland page: 'The Swedish army captured Duke Jacob (1658–1660)'. Fix: Add occupation_start 1658 / occupation_end 1660 cp duchy-of-courland, and a war 'Second Northern War (Polish front)' 1655-1660 with that zone (PLC zones wait for eu-15).
- **/ledger/24, /keyframe_review/10** (author to fix): The 1661 Cardis 'gain' of Ingria, the whole of Estonia and Kexholm re-gains land Sweden held since 1612/1617: no 1656 event takes it away, so the 1653-to-1659 reduction of about 130 Baltic cells is unexplained and the region is too wide (northern Estonia was never lost). Evidence: Swedish Empire page: the Russo-Swedish War (1656–1658) 'was terminated by the Treaty of Cardis on 2 July 1661, through which the Tsar surrendered the Baltic provinces to Sweden'; tsardom-of-russia has no 1656-1661 event with Sweden. Fix: Add occupation_start 1656 cp tsardom-of-russia for the land Cliopatria drops (1653 shape minus 1659 shape, Baltic edge), make L24 the matching occupation_end with that region, and add the war Russo-Swedish War (1656-1658).
- **/ledger (1613-1619), /wars** (author to fix): The Kalmar War (1611-1613) and the Danish hold on Älvsborg until the ransom of 1619 are missing. Evidence: denmark-norway L9 1613-1 contest_end, L10 1613-1 occupation_start 'Älvsborg and Gullberg', L11 1619 occupation_end, all cp swedish-empire. Fix: Add the Kalmar War to wars (zone Älvsborg/Kalmar) and occupation_start 1613-1 / occupation_end 1619 cp denmark-norway for Älvsborg (roles reversed), or say why not.
- **/ledger (1803)** (author to fix): The 1803 pledge of Wismar to Mecklenburg is missing. Evidence: mecklenburg L8: 1803 gain cp swedish-empire, 'the town of Wismar with Poel and Neukloster' (conf 3). The author lists it as unverified. Fix: Add loss 1803 cp mecklenburg (Treaty of Malmö), source the mecklenburg dossier's page or the Wismar page.
- **/keyframe_review/28** (author to fix): The 13 Guadeloupe cells of the 1814 shape are 'left as drawn' with no gain event behind them. Evidence: shapes.csv swedish-empire_1814 bbox reaches lon -61.77, lat 15.91; no ledger event mentions Guadeloupe. Fix: Either remove the Caribbean cells from the correction (minus the Guadeloupe region) and leave them to a swedish-guadeloupe dossier, or add gain 1813 / loss 1814 events with a page.
- **/sources/0/note, /notes** (author to fix): The 1,100,000 km2 is quoted as the infobox area; the page has no area in its infobox, the figure is in the body text with no year. Evidence: Swedish Empire page (fetched 2026-10-31): 'The land area of Sweden was 1,100,000 km2.' in the text; infobox has no area. Fix: Say 'body text' instead of 'infobox' (non-blocking).

### Thin (gap-filler)

- /ledger/40, /keyframe_review/26: Finnish War 1808-1809: the Russian occupation of Finland from February 1808 and the war itself (the dossier's largest single land loss has only the 1809 cession, no month) (try https://en.wikipedia.org/wiki/Finnish_War)
- /keyframe_review/25: Pomeranian War 1757-1762 and the 1762 shape's 12 extra German cells (try https://en.wikipedia.org/wiki/Pomeranian_War)
- /wars: Second Northern War Polish front 1655-1660 (Swedish occupation of Poland and Royal Prussia) and the Russo-Swedish War of 1788-1790 (try https://en.wikipedia.org/wiki/Second_Northern_War)
- /keyframe_review/1, /keyframe_review/2: Livonia 1621-1628 (Riga taken September 1621; swedish-livonia starts 1621-9) before the Altmark gain of 1629 (try https://en.wikipedia.org/wiki/Polish%E2%80%93Swedish_War_(1621%E2%80%931625))
- /keyframe_review/16: Eastern Livonia and Estonia lost 1704-1706 (Dorpat, Narva) are not dated (try https://en.wikipedia.org/wiki/Siege_of_Narva_(1704))
- /ledger (1807-1810): French occupation of Swedish Pomerania 1807-1810 (try https://en.wikipedia.org/wiki/Swedish_Pomerania)
- /identity/rulers: Rulers stop at 1721 (Frederick I 'to 1721') while the life runs to 1814; Gustavus Adolphus starts 1611, before the dossier's start (try https://en.wikipedia.org/wiki/List_of_Swedish_monarchs)
- /ledger/5, /ledger/7, /ledger/33: Confidence-1 events (German zone 1632-1636, the 1713 loss) need a page (try https://en.wikipedia.org/wiki/Thirty_Years%27_War)

## duchy-of-courland: fix

Spot checks: /ledger/0 confirmed (Duchy_of_Courland_and_Semigallia); /ledger/1, /ledger/2 confirmed (Duchy_of_Courland_and_Semigallia); /ledger/3, /ledger/4 confirmed (Duchy_of_Courland_and_Semigallia); /identity/capitals/0 confirmed (Duchy_of_Courland_and_Semigallia).

Area: page 27290 km2 (year None), Cliopatria 28201 km2, ratio 1.03, acknowledged.

### Findings

- **/identity/predecessors/1** (applied by reviewer): bishopric-of-courland was listed as a predecessor carrying the whole Courland region, but the bishopric passed its land to Denmark-Norway in 1560 and its Pilten district stayed outside the duchy until 1795 (the entry's own note). Evidence: bishopric-of-courland.json: end 1560-5, successor denmark-norway (Pilten); duchy note: 'the Pilten district of the bishopric stayed outside the duchy until 1795'. Fix: Removed the entry; the infobox wording is kept in the livonian-conference predecessor note. Re-validated, 0 errors.

### Thin (gap-filler)

- /ledger (1701-1710): Swedish and Russian hold on Courland in the Great Northern War (page silent) (try https://en.wikipedia.org/wiki/Great_Northern_War)
- /keyframe_review/2: The 1772 one-cell (250 km2) change is unexplained (unverified: page budget) (try https://en.wikipedia.org/wiki/First_Partition_of_Poland)
- /notes: Courland's colonies (Gambia from 1651, Tobago from 1652 to 1689, both on the duchy's page) have no counterpart dossiers (try https://en.wikipedia.org/wiki/Couronian_colonization)
- /ledger/3: Second Partition (1793) and the March 1795 Landtag/abdication are not dated on the pages opened (try https://en.wikipedia.org/wiki/Third_Partition_of_Poland)

## Cross-dossier matrix

- swedish-empire 1617 gain cp tsardom-of-russia -> tsardom-of-russia 1617 loss: matched. L1 / tsardom L48
- swedish-empire 1629 gain cp polish-lithuanian-commonwealth -> none: exception. L2, L3 Livonia and Elbląg; PLC is eu-15, not run
- swedish-empire 1635 loss cp polish-lithuanian-commonwealth -> none: exception. L6 Elbląg; PLC is eu-15, not run
- swedish-empire 1630 gain cp duchy-of-pomerania -> duchy-of-pomerania 1630 occupation_start: mismatch. L4 gain against an occupation; the duchy dissolves to swedish-empire 1637-3 (L10), which Sweden does not record
- swedish-empire 1648 gain cp duchy-of-pomerania -> none: missing. L16: counterpart dissolved in 1637; no mirror
- swedish-empire 1632 occupation_start cp holy-roman-empire-minor-states -> holy-roman-empire-minor-states 1632 occupation_start: matched. L5 / HRE L59; end L7 1636 against HRE L60 1635-5
- swedish-empire 1639 occupation_start cp electorate-of-saxony -> electorate-of-saxony 1642 occupation_start: mismatch. L8 1639-4 against Saxony L19 1642; Saxony ends it 1645-9 (L20) with Leipzig/Torgau garrisons to 1650-6 (L21-L22), Sweden at 1648-10 (L14)
- swedish-empire 1642 occupation_start cp holy-roman-empire-minor-states -> holy-roman-empire-minor-states 1642 occupation_start: matched. L9 / HRE L63; end L15 / HRE L68 1648-10
- swedish-empire 1645 gain cp denmark-norway -> denmark-norway 1645 loss: matched. L10 Gotland and Saaremaa / D-N L18; L11 Jämtland / D-N L17
- swedish-empire 1645 occupation_start cp denmark-norway -> denmark-norway 1645 loss: mismatch. L12 Halland pledged for 30 years (Brömsebro page) against D-N L19 loss; L20 occupation_end 1658 has no D-N mirror. Sweden's reading follows the page; route to eu-14-g
- swedish-empire 1645 gain cp denmark-norway -> none: mismatch. L13 Bremen-Verden: no D-N loss; prince-archbishopric-of-bremen L10 occupation_start 1643, HRE L65 1645 loss (conf 1)
- swedish-empire 1648 gain cp mecklenburg -> mecklenburg 1648 loss: matched. L17 after the reviewer's slug fix / mecklenburg L7
- swedish-empire 1648 gain cp prince-archbishopric-of-bremen -> prince-archbishopric-of-bremen 1648 occupation_end: matched. L18 1648-10 / Bremen L11-L12 1648-5 (occupation_end, dissolve)
- swedish-empire 1648 gain cp prince-bishopric-of-verden -> prince-bishopric-of-verden 1648 dissolve: mismatch. L19 / Verden L2 names counterpart kingdom-of-sweden, not swedish-empire
- swedish-empire 1658 gain cp denmark-norway -> denmark-norway 1658 loss: matched. L21-L22 1658-3 (N.S.) / D-N L23-L25 1658-2 (O.S.)
- swedish-empire 1660 loss cp denmark-norway -> denmark-norway 1660 gain: matched. L23 / D-N L26
- swedish-empire 1661 gain cp tsardom-of-russia -> none: missing. L24: tsardom has no 1656-1661 event with Sweden; neither side records the 1656 conquests
- swedish-empire 1675 occupation_start cp brandenburg-prussia -> brandenburg-prussia 1677 contest_start: mismatch. L25-L26 occupation 1675-1679-6 against B-P contest 1677 to 1679-12
- swedish-empire 1703 loss cp tsardom-of-russia -> tsardom-of-russia 1703 gain: matched. L27 / tsardom L77
- swedish-empire 1706 occupation_start cp electorate-of-saxony -> electorate-of-saxony 1706 occupation_start: matched. L28-L29 / Saxony L26-L27
- swedish-empire 1710 loss cp tsardom-of-russia -> tsardom-of-russia 1710 gain: matched. L30-L32 / tsardom L78-L80
- swedish-empire 1713 loss cp denmark-norway -> denmark-norway 1712 occupation_start: mismatch. L33 loss (conf 1, includes southern Pomerania) against D-N occupation of Bremen-Verden 1712-1715
- swedish-empire 1714 occupation_start cp tsardom-of-russia -> tsardom-of-russia 1713 occupation_start: matched. L34 / tsardom L83, one year apart; end L37 / tsardom L84 1721-9
- swedish-empire 1719 loss cp electorate-of-hanover -> electorate-of-hanover 1719 gain: matched. L35 / Hanover L5; Hanover's occupation_start 1715 (L3) has no Swedish mirror
- swedish-empire 1720 loss cp kingdom-of-prussia -> kingdom-of-prussia 1720 gain: matched. L36 / Prussia L6 1720-1; Prussia's occupation_start 1715 (L4) has no Swedish mirror
- swedish-empire 1721 loss cp russian-empire -> russian-empire 1721 gain: matched. L38 / RE L0
- swedish-empire 1743 loss cp russian-empire -> russian-empire 1743 gain: matched. L39 / RE L13
- swedish-empire 1809 loss cp russian-empire -> russian-empire 1809 gain: matched. L40 / RE L52 1809-9
- tsardom-of-russia 1611 occupation_start cp swedish-empire -> none: missing. tsardom L42/L45/L46/L47 Novgorod and Gdov 1611-1617; no Swedish mirror
- denmark-norway 1613 occupation_start cp swedish-empire -> none: missing. D-N L9-L11 Kalmar War end and Älvsborg 1613-1619; also D-N L8 contest_start 1611 predates swedish-empire (should be kingdom-of-sweden)
- denmark-norway 1658 contest_start cp swedish-empire -> none: missing. D-N L21-L22 Zealand 1658-2; no Swedish contest events
- brandenburg-prussia 1653 gain cp swedish-empire -> none: missing. B-P L6 Farther Pomerania (conf 3)
- brandenburg-prussia 1679 gain cp swedish-empire -> none: missing. B-P L9 strip east of the Oder (conf 3)
- mecklenburg 1803 gain cp swedish-empire -> none: missing. mecklenburg L8 Wismar pledge (conf 3)
- duchy-of-courland 1658 occupation_start cp swedish-empire -> none: missing. Courland L1-L2 1658-1660, same batch
- denmark-norway 1814 loss cp swedish-empire -> none: exception. D-N L37 1814-1 loss of Norway to swedish-empire; Sweden writes no gain (Norway independent until the union of 4 November 1814, founded as united-kingdoms-of-sweden-and-norway L0 cp swedish-empire). Route to eu-14-g: counterpart kingdom-of-norway
- habsburg-monarchy 1632 loss cp swedish-empire -> none: mismatch. Habsburg L31-L32 Silesia 1632-1635 and L35-L36 north Bohemia 1639-1642 as loss/gain; Sweden records occupations cp HRE minor states / Saxony. Route to eu-09
- holy-roman-empire-minor-states 1636 loss cp swedish-empire -> none: mismatch. HRE L61 1636-3 loss of 30 Pomeranian/Mecklenburg cells and L65 1645 loss of Bremen-Verden (both conf 1); route to eu-09
- duchy-of-bavaria 1632 occupation_start cp swedish-empire -> swedish-empire 1632 occupation_start: exception. Bavaria L18-L19, Bamberg L1-L2 (1631-1634), Würzburg L1-L2 (1633-1634): Sweden's German zone is one event cp holy-roman-empire-minor-states; owners per cell not on the pages (author's gap)
- danish-gold-coast 1658 found cp swedish-empire -> none: exception. Also dutch-gold-coast L10 (1656) and L13 (1665) cp swedish-empire: the Gold Coast is removed from Sweden's base shape and carried by swedish-gold-coast; route to af-04 to use that slug
- united-kingdoms-of-sweden-and-norway 1814 found cp swedish-empire -> swedish-empire 1814 dissolve: matched. UK L0 1814-11 / SE L41
- duchy-of-courland 1561 found cp livonian-conference -> livonian-conference 1561 loss: matched. Courland L0 1561-11 / livonian-conference L10 1561-11
- duchy-of-courland 1795 loss cp russian-empire -> russian-empire 1795 gain: matched. Courland L3 / RE L36
- house-of-jagiellon 1562 vassal_start cp duchy-of-courland-and-semigallia -> none: mismatch. house-of-jagiellon L33-L34 (1562 to 1569-7) use slug 'duchy-of-courland-and-semigallia'; the dossier is 'duchy-of-courland'. Route to that group. PLC suzerainty 1569-1795 waits for eu-15

## Verdict reasoning

swedish-empire: no event was fabricated or mis-dated (16 events checked on 5 pages, all confirmed), but the ledger gains Pomerania and Bremen-Verden twice, gives southern Pomerania to Denmark, gains in 1661 land it never lost, and lacks the mirrors of seven page-backed neighbour events (Novgorod 1611-1617, Älvsborg 1613-1619, Farther Pomerania 1653, the Oder strip 1679, the German occupations 1715-1720, Wismar 1803, Courland 1658-1660). Back to the author with the list above.

duchy-of-courland: four events confirmed on the duchy's page, area ratio 1.03, stable outline within a 1-2 page budget; one identity fix applied (bishopric predecessor). Accepted.
