# Review of batch eu-15-x (2026-10-31)

Reviewer: adversarial review of the 17 additions dossiers (states that Cliopatria lacks: Hungary, Croatia, Royal Prussia, the Prussian and Austrian partition zones, and the Polish, Silesian and Bohemian duchies). All 17 validate with --resolve: 0 errors, 1 warning (west-ukrainian-people-s-republic has no dossier yet). The reviewer opened 24 Wikipedia pages and spot-checked 4-10 events per dossier. Shapes were checked with the gazetteer resolver: areas, overlaps between sibling dossiers, discs at key towns, and fractions inside the parent Cliopatria shapes.

How to read the verdicts: **fail** means a blocking shape or area error the author must fix. **fix** means non-blocking edits; those marked *(applied)* were made by the reviewer, and the others are for the author. **thin** means gaps for a gap-filler. **pass** means nothing to change.

## Summary

| slug | verdict | main reason |
|---|---|---|
| royal-hungary | thin | Events check out; Esztergom gained twice (1595, 1683) with no 1605 loss; 1687 bridge at confidence 1 |
| ottoman-hungary | thin | Nagyvárad fixed to 1660 by the reviewer; missing the 1605 Esztergom regain; 1687 bridge at confidence 1 |
| croatia-in-union-with-hungary | thin | Venice's Split (1327) and Nin (1329) are on the cited page but missing |
| royal-prussia | fail | Shape is the gazetteer 'West Prussia': leaves out Elbląg, draws Kuyavia, Bydgoszcz, Słupsk and Lębork |
| prince-bishopric-of-warmia | fail | Shape 12,645 km2 against about 4,500 (ratio 2.8), and the note says 4,000-5,000; capital is not the infobox's |
| hussite-bohemia | pass | Could not break it |
| duchy-of-pomerelia | fix | Bohemian rule 1300-1306 treated differently from duchy-of-sieradz |
| duchy-of-sieradz | fix | 6,322 km2 overlap with Łęczyca |
| duchy-of-eczyca-1231-1352 | fix | Source of the 1263 event fixed by the reviewer; overlap with Sieradz |
| kingdom-of-galicia-and-lodomeria | pass | Could not break it (area ratio 1.06) |
| south-prussia | fail | {region: Kuyavia} draws West Prussia's Toruń, Chełmno and Bydgoszcz (27,060 km2 overlap) |
| new-east-prussia | fix | Płock and Dobrzyń circles cross the Vistula (16% overlap with siblings) |
| west-prussia | fail | Draws southern Kuyavia (Polish until 1793; Congress Poland after 1815) and Posen's Bydgoszcz; ratio 1.94 not resolved |
| duchy-of-cieszyn | pass | Could not break it |
| domain-of-matthew-iii-csak | fix | KF1 is all of Slovakia although the page gives the north-east to the Abas; Visegrád lost but never held |
| duchy-of-oswiecim | fix | Toszek drawn from 1315; the page has it from 1405 |
| duchy-of-opava | pass | Could not break it |

## Per dossier

### royal-hungary: thin

Area: page None km2 (None), drawn 70812 km2, ratio None, acknowledged True. Neither the Royal Hungary infobox nor its text gives an area. The drawn KF0 (1538-1551) is 70,812 km2 and KF5 (1687-1698) is 145,418 km2, a confidence-1 bridge.

Gaps (for a gap-filler):
- `/ledger/4`: The 1595 gain of Esztergom and Visegrád has no reversal: the ledger gains Esztergom again in 1683 (/ledger/14) without losing it in between, and no keyframe shows the 1595 gain. The Ottoman recapture of 1605 is missing here (loss) and in ottoman-hungary (gain). The author flagged this. Try: https://en.wikipedia.org/wiki/Siege_of_Esztergom_(1605)
- `/ledger/1`: Esztergom is lost in 1552 at confidence 2, but Budin Eyalet lists the 1543-44 conquests without naming Esztergom, and Esztergom fell in 1543. As drawn, royal-hungary KF0 and ottoman-hungary KF1 both draw 2,276 km2 around Esztergom in 1543-1551. Try: https://en.wikipedia.org/wiki/Siege_of_Esztergom_(1543)
- `/ledger/18`: The 1687 gain of all central Hungary is a confidence-1 bridge. Great Turkish War names only Gyula (1688). Find the dates for Eger (1687), Székesfehérvár (1688), Kanizsa (1690) and Várad (1692), and redraw KF5 as steps. Try: https://en.wikipedia.org/wiki/Eger
- `/ledger/15`: The counterpart of the 1685 gain is the author's reading. principality-of-upper-hungary books its 1685-10 loss with habsburg-monarchy as counterpart. Try: https://en.wikipedia.org/wiki/Principality_of_Upper_Hungary
- `/keyframe_review/1`: The Bocskai principality of 1605 (north-east Hungary) is not drawn. The author flagged this. Try: https://en.wikipedia.org/wiki/Bocskai_uprising

Spot checks: `/ledger/0` confirmed (division only in 1538 by the Treaty of Nagyvárad; Habsburgs get the north and west); `/ledger/3` confirmed ('Győr and Komárom were captured in 1594'); `/ledger/4` confirmed ('In 1595, the Christians, led by Mansfeld, captured Esztergom and Visegrád'); `/ledger/5` confirmed (Eger conquered 1596); `/ledger/6` confirmed ('Austrians recaptured Győr and Komarom in 1598'); `/ledger/8` confirmed (Zsitvatorok 11 November 1606, 'gave the region of Vác'); `/ledger/11` confirmed (Érsekújvár conquered in September 1663); `/ledger/14` confirmed (Esztergom surrenders after Párkány, October 1683); `/ledger/16` confirmed (Érsekújvár fell 19 August 1685); `/ledger/17` confirmed (Buda fell 2 September 1686)

### ottoman-hungary: thin

Area: page 91250 km2 (None), drawn 91803 km2, ratio 1.01, acknowledged True. The 91,250 km2 is in the body of the Ottoman Hungary article, with no year. It is compared here with the drawn KF4 (1600-1662). There is no Cliopatria row.

Findings:
- `/ledger/12 (was /ledger/15)` *(applied)*: The Nagyvárad (Oradea) gain was dated 1664 with counterpart habsburg-monarchy. Várad was Transylvanian and fell in August 1660; Vasvár (1664) only recognised it. Evidence: Principality of Transylvania (1570-1711): 'The fall of Nagyvárad to the expansionist Ottomans on 27 August 1660 marked the decline of the Principality.' principality-of-transylvania /ledger/8 books the 1660-08 loss. Fix: Done: year 1660, month 8, counterpart principality-of-transylvania, confidence 3, source the Transylvania page (added to sources[]), and the event moved into ledger order. Still to do: KF5 (1663-) adds Oradea while KF4 (1600-1662) lacks it for 1660-1662; extend KF4 or note it.

Gaps (for a gap-filler):
- `/ledger/6`: The 1595 loss of Esztergom has no matching regain (Ottoman recapture, 1605) before the 1683 loss (/ledger/17); the keyframes ignore both moves. Try: https://en.wikipedia.org/wiki/Siege_of_Esztergom_(1605)
- `/ledger/20`: The 1687 loss of all central Hungary (confidence 1) bridges towns lost from 1687 to 1695 (Eger 1687, Székesfehérvár 1688, Kanizsa 1690, Várad 1692, Gyula 1695). KF9 (Banat only, 1687-1698) is too small for 1687-1690. Try: https://en.wikipedia.org/wiki/Great_Turkish_War
- `/ledger/1`: The counterpart of the 1543-44 conquests is kingdom-of-hungary, but Esztergom and Fehérvár were held for Ferdinand, and royal-hungary exists from 1538. Which holder lost which town is on no page opened. Try: https://en.wikipedia.org/wiki/Siege_of_Esztergom_(1543)
- `/keyframe_review/5`: No page opened dates the founding of the Varat and Uyvar eyalets. Try: https://en.wikipedia.org/wiki/Varat_Eyalet

Spot checks: `/ledger/0` confirmed ('on 29 August 1541 he took control of the city'); `/ledger/1` confirmed ('In the years 1543–44, the Ottomans conquered the fortresses of Nógrád, Vác, Fehérvár, Pécs and Siklós'); `/ledger/2` confirmed ('In 1552 the eyalet was expanded with new territories in the North'; region is a reading, confidence 2); `/ledger/3` confirmed (Eyalet of Temeşvar established 1552); `/ledger/7` confirmed (Eğri eyalet 1596; Long Turkish War: Eger conquered 1596); `/ledger/9` confirmed (Kanije eyalet 1600); `/ledger/12` mis-dated (was 1664 with counterpart Habsburg; Nagyvárad fell 27 August 1660); fixed by the reviewer; `/ledger/14` confirmed (September 1663)

### croatia-in-union-with-hungary: thin

Area: page None km2 (None), drawn 53362 km2, ratio None, acknowledged True. No area on the page. The drawn KF0 is 53,362 km2 (modern Croatia as the base shape).

Gaps (for a gap-filler):
- `/ledger (after /ledger/4)`: Two losses to Venice that are on the cited page are missing: Split in 1327 and Nin in 1329 ('Venice took control over Split in 1327 and Nin in 1329'). Without them, Dalmatia is gained in 1180 and again in 1358 with no loss in between. The notes say that 'the Croatia page names only the Zadar sack of 1202', which is wrong. Add loss events for 1327 ({place: Split, km 25}, confidence 3) and 1329 (Nin as lon/lat, confidence 3), counterpart republic-of-venice, and end KF4 at 1326. Try: https://en.wikipedia.org/wiki/Croatia_in_union_with_Hungary
- `/keyframe_review/4`: Venetian Dalmatia 1202-1357 beyond Zadar, Split and Nin (Šibenik, Trogir) is undrawn. The author flagged this. Try: https://en.wikipedia.org/wiki/Venetian_Dalmatia
- `/ledger/5`: The 1327 Cetina-Neretva loss is a confidence-2 reading. banate-of-bosnia books the land in 1326 as gains from nobody (Završje) and from kingdom-of-serbia (Hum), never from Croatia. Try: https://en.wikipedia.org/wiki/Stephen_II,_Ban_of_Bosnia

Spot checks: `/ledger/0` confirmed ('Coloman was crowned in Biograd in 1102'); `/ledger/1` confirmed (1116: Biograd, Split, Trogir, Šibenik, Zadar); `/ledger/2` confirmed (1133, 'except Zadar'); `/ledger/3` confirmed (1167; held until Manuel I's death, 1180); `/ledger/5` confirmed in substance (Cetina-Neretva annexed c. 1327-1329; confidence 2); `/ledger/7` confirmed (1409, 100,000 ducats); `/ledger/8` confirmed (1482, strongholds in the Neretva valley); `/ledger/9` confirmed (Knin, 29 May 1522); `/ledger/10` confirmed (Cetin, 1 January 1527)

### royal-prussia: fail

Area: page None km2 (None), drawn 41476 km2, ratio None, acknowledged False. No area on the page. The drawn 41,476 km2 includes about 9,000 km2 of Kuyavia and Greater Poland plus Słupsk and Lębork, and leaves out Elbląg.

Findings:
- `/keyframe_review/0/correction (also /ledger/0, /ledger/2, /ledger/4 regions, identity predecessors and successors)`: The shape does not match its own text ('Pomerelia, Chełmno Land, the Elbląg and Malbork districts'). The gazetteer region 'West Prussia' is the Pomeranian plus Kuyavian-Pomeranian voivodeships: it leaves Elbląg out and draws Crown Kuyavia and Greater Poland land (Włocławek, Inowrocław, Bydgoszcz: the Brześć Kujawski and Inowrocław voivodeships) and Pomeranian-duchy land (Słupsk; Lębork and Bytów, which the notes say are not drawn). Evidence: Resolver test, 3 km discs: Elbląg is outside the shape; Włocławek, Inowrocław, Bydgoszcz, Słupsk and Lębork are inside. 7,600 km2 (18%) of the 41,476 km2 lies outside Cliopatria's Polish-Lithuanian Commonwealth shape for 1600. Peace of Thorn (1466): Poland received Pomerania, the Chełmno Land, Elbing, Marienburg and Warmia, not Kuyavia. Fix: Redraw: Pomeranian voivodeship minus Słupsk, Lębork and Bytów (a polygon west of about 17.7E); plus the Kuyavian-Pomeranian land north of the Vistula and Noteć (Chełmno Land, Toruń, Świecie, Grudziądz, Tuchola); plus {place: Elblag, km 20}. Or ask the gazetteer agent for a 'Royal Prussia' region separate from 'West Prussia'. Apply the same land in /ledger/0, /ledger/2 and /ledger/4.

Gaps (for a gap-filler):
- `/keyframe_review/0`: Swedish occupations are missing: Elbing, Marienburg and the Vistula delta under the Truce of Altmark (1629-1635), and the Deluge (1655-1660). Try: https://en.wikipedia.org/wiki/Truce_of_Altmark
- `/identity/capitals`: No capital (the page states none). The Prussian diet's seats are on no page opened. Try: https://en.wikipedia.org/wiki/Royal_Prussia

Spot checks: `/ledger/0` confirmed (infobox 'Established: 19 October 1466'); `/ledger/1` confirmed ('integrated fully into the Kingdom of Poland' by the Union of Lublin); `/ledger/2` confirmed (infobox 'Dissolved: 1 July 1772'; annexed by Prussia); `/ledger/3` confirmed ('but not the cities of Danzig (Gdańsk) and Thorn (Toruń)')

### prince-bishopric-of-warmia: fail

Area: page 4500 km2 (None), drawn 12645 km2, ratio 2.81, acknowledged False. The 4,500 km2 is from the Warmia region article; the bishopric's own page gives no area. The note claims the stand-in is 4,000-5,000 km2, which is false.

Findings:
- `/keyframe_review/0 (correction and note; also /ledger/0-2 and identity regions)`: The shape is 2.8 times the size of Warmia, and the keyframe note misstates it. The gazetteer 'Warmia' region (Warmian-Masurian voivodeship cut to a 19.3-21.3E, 53.6-54.5N box) resolves to 12,645 km2, but the note says 'about 4,000-5,000 km2'. Evidence: Warmia article: 'The region covers an area of around 4,500 km2'. 7,840 km2 (62%) of the drawn shape lies inside Cliopatria's Duchy of Prussia shape for 1600. Resolver discs put Elbląg (Royal Prussia) and Ostróda, Pasłęk, Morąg and Bartoszyce (Ducal Prussia) inside the bishopric. Fix: Redraw to about 4,500 km2: a polygon of at most 12 points through Braniewo, Frombork, Lidzbark Warmiński, Reszel, Barczewo and Olsztyn, intersected with Warmian-Masurian; keep Elbląg out. Correct the note's area. Report the gazetteer region 'Warmia' to the gazetteer agent: it is about 3 times too large.
- `/identity/capitals`: The capital in the infobox, Lidzbark Warmiński (Heilsberg), is missing. Frauenburg is given as capital 1280-1772, but the page says only that the see (the cathedral) moved there in 1280. Evidence: Prince-Bishopric of Warmia infobox: capital Lidzbark Warmiński (no years). Text: the see at Braunsberg from 1251, moved to Frauenburg in 1280 after Old Prussian attacks. Fix: Add Heilsberg/Lidzbark Warmiński (20.58, 54.13) for the years a page gives for the bishops' residence (Lidzbark Warmiński article), and keep Frauenburg only as the see. Cover 1243-1250 or say why there is no capital.
- `/ledger/0`: The counterpart old-prussians disagrees with the neighbours and with the note. The note says the bishopric was founded 'after the Teutonic Knights' conquest'. old-prussians loses Warmia to teutonic-order only in 1253 and regains it in 1260-1277 (Great Prussian Uprising); teutonic-order gains Warmia in 1249 (Christburg). The dossier books no 1260-1274 uprising, although the page says the see left Braunsberg in 1280 'after attacks by Old Prussians'. Evidence: old-prussians /ledger/5 (1253 loss), /ledger/10 (1260 gain), /ledger/12 (1277 loss); teutonic-order /ledger/3 (1249 gain). Fix: Name teutonic-order (or 'nobody') as the 1243 counterpart, or book Warmia as contested 1260-1274 with old-prussians, and settle it with the old-prussians and teutonic-order owners.

Gaps (for a gap-filler):
- `/ledger`: There is no event between 1243 and 1772: nothing for the 1466 recognition by Poland, the 1479 Treaty of Piotrków, or the 1525 change. The author flagged this. Try: https://en.wikipedia.org/wiki/Warmia

Spot checks: `/ledger/0` confirmed ('founded as the Bishopric of Ermland by William of Modena in 1243'); `/ledger/1` confirmed (annexed and secularised by Prussia after the First Partition, 1772); `/identity/capitals` not on page as claimed (the infobox capital is Lidzbark Warmiński; Frauenburg is the see from 1280)

### hussite-bohemia: pass

Area: page None km2 (None), drawn 50580 km2, ratio None, acknowledged True. Neither page gives an area. KF1 lies 98% inside Cliopatria's Kingdom of Bohemia shape for 1425.

Tried and could not break: Tried: dates against both pages, the KF1 extent against the Plzeň loyalists, overlap with siblings (none). kingdom-of-bohemia still lacks the mirror events (see cross_checks).

Gaps (for a gap-filler):
- `/ledger/2`: Confidence 1: East Bohemia (Hradec Králové) in 1420. The page says only that the town was Utraquist and adopted Tábor doctrine in 1423-24. The event has no effect on the keyframes (KF1 is all Bohemia except Plzeň). Try: https://en.wikipedia.org/wiki/Orebites

Spot checks: `/ledger/0` confirmed (infobox '30 July 1419'); `/ledger/3` confirmed (after Vítkov, July 1420, 'almost all Bohemia fell into the hands of the Hussites'; Plzeň the loyalist centre); `/ledger/4` confirmed ('in August 1421 laid siege to the town of Žatec'); `/ledger/5` confirmed (Lipany, 30 May 1434; the region is a reading at confidence 2)

### duchy-of-pomerelia: fix

Area: page None km2 (None), drawn 21749 km2, ratio None, acknowledged True. No area on the page. The stand-in is the Pomeranian voivodeship.

Findings:
- `/ledger (1300 and 1306)`: This dossier treats Bohemian rule differently from duchy-of-sieradz in the same batch. The Pomerelia page says Władysław 'lost control of Greater Poland and Pomerelia in 1300 after a nobility revolt' and Wenceslaus captured them (ruler list: Wenceslaus II 1299-1305, Wenceslaus III 1305-1306), and that 'Pomerelia was recaptured by Władysław I the Elbow-high in 1306'. duchy-of-sieradz books the same Bohemian rule as a loss in 1299 and a gain in 1306; this dossier books nothing. Evidence: Duchy of Pomerelia page (ruler list and text). Fix: Either book a loss in 1300 and a gain in 1306 (counterpart kingdom-of-bohemia, region Pomerelia, confidence 3), or book both duchies' Bohemian years as vassalage in the overlord's ledger. The two dossiers should agree.

Gaps (for a gap-filler):
- `/keyframe_review/0`: The Duchy of Świecie (Wartislaw), 1227-1270, is drawn inside KF0. The author flagged this. Try: https://en.wikipedia.org/wiki/Duchy_of_Pomerelia
- `/ledger/4`: The 1308 Brandenburg occupation covers the whole region at confidence 2; margraviate-of-brandenburg books a 1307 gain of Pomerelia with counterpart 'nobody'. Try: https://en.wikipedia.org/wiki/Teutonic_takeover_of_Danzig_(Gda%C5%84sk)

Spot checks: `/ledger/0` confirmed ('In 1227, the duchy gained independence from Poland'); `/ledger/1` confirmed (infobox: unification of Gdańsk and Świecie, 1270); `/ledger/2` confirmed at confidence 2 (Wartislaw expelled 1270/71 with the margraves' aid; the margraves 'refused to leave Gdańsk'); `/ledger/3` confirmed ('Brandenburg returned Gdańsk to Mestwin', treaty of 1273); `/ledger/9` confirmed (annexed 'into the Teutonic Order state in 1309')

### duchy-of-sieradz: fix

Area: page None km2 (None), drawn 16438 km2, ratio None, acknowledged True. No area on the page; the radius is a stand-in.

Findings:
- `/keyframe_review/0, /keyframe_review/1 (and the ledger regions)`: The Sieradz 70 km circle (18.73, 51.6) and the Łęczyca 60 km circle (19.2, 52.06) overlap by 6,322 km2 in 1263-1338: 38% of the Sieradz shape and 51% of the Łęczyca KF1. Both duchies draw the same land, including Łódź, which belonged to Łęczyca. Evidence: Resolver overlap of duchy-of-sieradz KF0 and KF1 with duchy-of-eczyca-1231-1352 KF1. Fix: Make the two duchies disjoint, for example Sieradz = {minus: [{lon 18.73, lat 51.6, km 70}, {lon 19.2, lat 52.06, km 60}]}, or use named lands (ask the gazetteer for 'Sieradz Land' and 'Łęczyca Land'). Use the same spec in the found and dissolve events.

Spot checks: `/ledger/0` confirmed ('created based on part of the Duchy of Łęczyca in 1263'); `/ledger/1` confirmed (1299 Władysław 'had to cede Sieradz'; Wenceslaus II 1299-1305); `/ledger/2` confirmed (Wenceslaus III to 1306; reunited 1306); `/ledger/3` confirmed (incorporated 1339)

### duchy-of-eczyca-1231-1352: fix

Area: page None km2 (None), drawn 12392 km2, ratio None, acknowledged True. No area on the page; the radius is a stand-in.

Findings:
- `/ledger/1/source` *(applied)*: The 1263 split-off was sourced to the Łęczyca page, which says 1264 (text and infobox). The 1263 date is on the Sieradz page. Evidence: Duchy of Łęczyca: 'In 1264 the Duchy of Sieradz was split from it' (infobox 'Split off Sieradz: 1264'). Duchy of Sieradz: 'created based on part of the Duchy of Łęczyca in 1263'. Fix: Done: source set to the Duchy of Sieradz page, with a reviewer note added.
- `/keyframe_review/1 (and /ledger/2-3 regions)`: The Sieradz 70 km circle (18.73, 51.6) and the Łęczyca 60 km circle (19.2, 52.06) overlap by 6,322 km2 in 1263-1338: 38% of the Sieradz shape and 51% of the Łęczyca KF1. Both duchies draw the same land, including Łódź, which belonged to Łęczyca. Evidence: Resolver overlap with duchy-of-sieradz KF0 and KF1. Fix: Make the two duchies disjoint, as in the duchy-of-sieradz fix (one spec, used by both dossiers).

Spot checks: `/ledger/0` confirmed ('created around 1231 ... by Konrad I of Masovia'; confidence 2); `/ledger/1` mis-dated against the cited page (1264); 1263 is on the Sieradz page; source fixed by the reviewer; `/ledger/2` confirmed (after Władysław the Hunchback's death in 1352)

### kingdom-of-galicia-and-lodomeria: pass

Area: page 78497 km2 (None), drawn 83457 km2, ratio 1.06, acknowledged True. Compared with KF6 (1849-1917). First Partition page: Austria's 1772 share was 83,000 km2, against 81,687 km2 drawn in KF0.

Tried and could not break: Tried: all ten events against the Kingdom page, the Kraków in/out sequence 1772-1846, overlap with siblings (none). The Russian and Polish counterparts book the land against austrian-empire or habsburg-monarchy (see cross_checks).

Gaps (for a gap-filler):
- `/ledger/2`: West Galicia (1795) is the Lublin and Świętokrzyskie voivodeships at confidence 2; the page names no boundary. Try: https://en.wikipedia.org/wiki/West_Galicia

Spot checks: `/ledger/0` confirmed (First Partition, 5 August 1772); `/ledger/1` confirmed (Bukovina 'became part of Galicia as the Bukowiner Kreis' in 1786); `/ledger/3` confirmed (Schönbrunn 1809: 'all of its third partition gains'); `/ledger/4` confirmed (Tarnopol to Russia, 1809; returned 1815); `/ledger/6` confirmed ('Austria annexed the Free City of Cracow', 1846); `/ledger/7` confirmed (Bukovina part of the Kingdom 1786-1849); `/ledger/8` confirmed ('Claimed by West UPR: 19 October 1918'); `/ledger/9` confirmed ('Joined to Poland: 14 November 1918')

### south-prussia: fail

Area: page 53000 km2 (1806), drawn 75364 km2, ratio 1.42, acknowledged True. The excess is acknowledged (as 1.3), but its cause, the double-drawn Chełmno Land, Toruń and Bydgoszcz, is not.

Findings:
- `/keyframe_review/0, /keyframe_review/1 (and /ledger/0, /ledger/3-6, identity regions)`: The shape draws West Prussia's land, against the dossier's own note and against the page. {region: Kuyavia} is the whole Kuyavian-Pomeranian voivodeship (19,726 km2): Toruń, Chełmno, Grudziądz and Bydgoszcz fall inside. The notes say Thorn is 'in west-prussia, not here'. Evidence: South Prussia page: from Kuyavia only 'the Kuyavian voivodeship of Brześć' (with Greater Poland, Sieradz, Łęczyca, Dobrzyń, parts of Płock and Rawa). Resolver: overlap with west-prussia KF1 is 27,060 km2 in 1793-94 (38% of the 71,318 km2 shape) and 22,761 km2 in 1795-1806. Drawn 75,364 km2 against the infobox's '1806: 53,000 km2' (ratio 1.42). Fix: Replace {region: Kuyavia} with the Brześć Kujawski and Inowrocław land south of the Vistula and Noteć (for example Kuyavian-Pomeranian intersected with a polygon south of about 52.95N and east of 17.9E), then subtract west-prussia's 1793 shape. Recompute the area note. Coordinate the line with west-prussia, which overreaches the other way.
- `/ledger/3/counterpart`: The 1806 contest_start names duchy-of-warsaw, which did not exist until the Treaty of Tilsit (9 July 1807, page). Evidence: South Prussia page: the uprising followed 'Napoleon's victory in the War of the Fourth Coalition'. kingdom-of-prussia /ledger/36 books the 1807 contest_end with first-french-empire. Fix: Name first-french-empire as the counterpart of the 1806 contest_start and the 1807 contest_end; keep duchy-of-warsaw for the 1807 loss and dissolve.

Gaps (for a gap-filler):
- `/keyframe_review/1`: The 1795-96 borders with West Galicia and New Silesia are not on the pages. The author flagged this. Try: https://en.wikipedia.org/wiki/New_Silesia

Spot checks: `/ledger/0` confirmed ('2nd Polish Partition: 25 September 1793'); `/ledger/1` confirmed ('Annexed Warsaw: 1795'); `/ledger/2` confirmed (Dobrzyń and Płock 'northeast of the Vistula' to New East Prussia; the page gives no date); `/ledger/5` confirmed (Tilsit, 9 July 1807)

### new-east-prussia: fix

Area: page 55000 km2 (1806), drawn 45522 km2, ratio 0.83, acknowledged True. The infobox says 'less than 55,000 km2'.

Findings:
- `/keyframe_review/0 (and /ledger/1, /ledger/3-4, identity regions)`: The Płock (45 km) and Dobrzyń (30 km) circles cross the Vistula: Włocławek (Brześć Kujawski, South Prussia's) falls inside. The shape overlaps south-prussia KF1 by 2,782 km2 and west-prussia KF1 by 4,299 km2 (16% of 45,522 km2). Evidence: South Prussia page: the lands of Dobrzyń and Płock 'northeast of the Vistula river were transferred to New East Prussia'. Fix: Subtract the south-prussia (1795) and west-prussia (1793) shapes from the two circles, or clip them with a polygon along the Vistula, in the keyframe and in /ledger/1 and /ledger/3-4.

Gaps (for a gap-filler):
- `/keyframe_review/0`: The 1796 border with New Silesia and West Galicia is not on the pages. The author flagged this. Try: https://en.wikipedia.org/wiki/New_Silesia

Spot checks: `/ledger/0` confirmed (Third Partition, 24 October 1795); `/ledger/1` confirmed (transfer of Dobrzyń and Płock); `/ledger/2` confirmed ('The area around Białystok was ceded to the Russian Empire', 9 July 1807); `/ledger/3` confirmed (Płock Department and rest of Białystok Department to the Duchy of Warsaw)

### west-prussia: fail

Area: page 25580 km2 (1910), drawn 49568 km2, ratio 1.94, acknowledged True. Acknowledged in the KF0 and KF4 notes but not resolved; part of the excess is land of Posen and Congress Poland.

Findings:
- `/keyframe_review/0 (and /ledger/0, identity predecessors)`: The 1773-1792 shape draws Polish land: the gazetteer region 'West Prussia' contains the whole Kuyavian-Pomeranian voivodeship, so Włocławek and the Brześć Kujawski voivodeship, which stayed Polish until 1793, are inside. Evidence: First Partition page: Prussia took Royal Prussia, the Netze District 'and northern Kuyavia', and its share was 36,000 km2 (here 46,534 km2 without Warmia). South Prussia page: 'the Kuyavian voivodeship of Brześć' passed only in 1793. Resolver: 10,369 km2 (22%) of KF0 lies inside Cliopatria's Polish-Lithuanian Commonwealth shape for 1780; the Włocławek disc is inside KF0. Fix: Draw Royal Prussia without Kuyavia (see the royal-prussia fix), plus a Netze District spec and the Inowrocław area (northern Kuyavia) only.
- `/keyframe_review/1`: In 1793-1806 the shape and south-prussia's draw 22,761-27,060 km2 of the same land. Evidence: Resolver overlap with south-prussia KF0 and KF1. Fix: Settle one Kuyavia line with south-prussia: Brześć Kujawski to South Prussia, Chełmno Land and Toruń to West Prussia.
- `/keyframe_review/3, /keyframe_review/4`: The 1815-1918 shapes keep the 70 km Netze circle (17.4, 53.1) and southern Kuyavia: Bydgoszcz and Inowrocław (Province of Posen after 1815) and Włocławek (Congress Poland) fall inside. The area is 49,568 km2 against 25,580 km2 (ratio 1.94). The note acknowledges the excess but does not resolve it. Evidence: Province of West Prussia page: of the Netze District, some areas were added to West Prussia; 'The remainder became part of the Grand Duchy of Posen.' Resolver discs at Bydgoszcz, Inowrocław and Włocławek fall inside KF3. Fix: After 1815, keep only the Deutsch Krone and Flatow part of the Netze District; drop Bydgoszcz, Inowrocław and southern Kuyavia; drop Słupsk and Lębork (Province of Pomerania). Bring the area near 25,600 km2 or explain what remains.

Gaps (for a gap-filler):
- `/identity/capitals`: The page says the capital 'alternated between Marienwerder ... and Danzig' with no years; only Marienwerder is booked, for 1773-1919. Try: https://en.wikipedia.org/wiki/Kwidzyn

Spot checks: `/ledger/0` confirmed ('established as a province of the Kingdom of Prussia in 1773'; month 9 from the First Partition cession of 18 September 1773); `/ledger/1` confirmed (Second Partition, 1793); `/ledger/2` confirmed (Danzig a Free City 1807-1814); `/ledger/3` confirmed (Thorn and Kulm to the Duchy of Warsaw, 1807); `/ledger/5` confirmed ('Danzig, Kulm, and Thorn were returned' by the Vienna Congress); `/ledger/6` confirmed (combined into the Province of Prussia in 1829); `/ledger/7` confirmed (re-established 1878); `/ledger/8` confirmed ('West Prussia was dissolved in 1919'; the body says 1920)

### duchy-of-cieszyn: pass

Area: page None km2 (None), drawn 3035 km2, ratio None, acknowledged True. No area on the page; the radii are stand-ins.

Tried and could not break: Tried: all four territorial events against the Teschen page, the sibling overlap with duchy-of-oswiecim (none), the 1290 mirror in duchy-of-raciborz (matched).

Gaps (for a gap-filler):
- `/keyframe_review/0`: The separation of the Pless (Pszczyna) state country is not on the page; it lies outside the 30 km circle, so the circle stands in for a smaller duchy than the 1290-1517 one. Try: https://en.wikipedia.org/wiki/Pszczyna

Spot checks: `/ledger/0` confirmed ('After another partition in 1290, Mieszko took his residence in Cieszyn'); `/ledger/1` confirmed (Oświęcim split off about 1315); `/ledger/2` confirmed (infobox 'Split off Bielsko: 1572'; sold 'as a state country to the Princes of Pless'); `/ledger/6` confirmed ('merged into the Austrian Silesia crown land in 1849')

### domain-of-matthew-iii-csak: fix

Area: page None km2 (None), drawn 49316 km2, ratio None, acknowledged True. No area on the page. KF1 lies 97% inside Cliopatria's Kingdom of Hungary shape for 1315.

Findings:
- `/keyframe_review/1 (and /ledger/1-2, /ledger/4-6 regions)`: KF1 (1311-1320) is the whole of Slovakia. That includes the north-east, which the cited page gives to the Abas, and leaves out Matthew's Hungarian castles in Nógrád and Hont. Evidence: Matthew III Csák page: Amade Aba was 'the powerful oligarch of the north-eastern parts of the kingdom'; when Matthew invaded Szepes he was defeated by Philip Drugeth; after 1301 'he also took several castles in Nógrád and Hont counties'. Fix: Use Slovakia minus the Košice and Prešov regions (Natural Earth admin1 spellings) plus Nógrád (Hungary) and Visegrád at confidence 2, and give the Kingdom of Hungary page's 'fourteen counties' reading in text.
- `/ledger/3`: The 1315 loss of Visegrád is on the page ('King Charles also invaded Matthew's domain and occupied Visegrád', 1314-15 campaigns), but Visegrád is in no keyframe and in no gain, so the loss removes land the domain never drew. Evidence: KF0 and KF1 regions do not contain (18.97, 47.79). Fix: Add Visegrád ({lon 18.97, lat 47.79, km 15}) to KF0 and KF1 and the found or gain region, or book its gain with a page.

Gaps (for a gap-filler):
- `/ledger/1`: The 14-county peak is undated beyond 'around 1311'; the 1316-1317 losses (Jókő and others) are not booked. The author flagged this. Try: https://en.wikipedia.org/wiki/Matthew_III_Cs%C3%A1k

Spot checks: `/ledger/0` confirmed (1301: Wenceslaus 'granted him Trencsén and Nyitra counties'; confidence 2); `/ledger/1` confirmed in substance ('14 counties ... and about 50 castles'; 'greatest territorial extent around 1311'); region overreaches (see fix); `/ledger/2` confirmed (25 June 1311 march on Buda); `/ledger/3` confirmed (Visegrád occupied in the 1314-15 campaigns); `/ledger/6` confirmed ('Died: 18 March 1321'; the domain overtaken within months)

### duchy-of-oswiecim: fix

Area: page None km2 (None), drawn 6575 km2, ratio None, acknowledged True. No area on the page; the radii are stand-ins.

Findings:
- `/keyframe_review/0 and /ledger/0`: The 1315 found region and KF0 include a 25 km circle at Toszek (18.5, 50.45). Toszek is not in the land duchy-of-cieszyn loses in 1315 (the mirror event), and the Oświęcim page puts Toszek with Przemysław only 'from 1405'. Evidence: Duchy of Oświęcim page, ruler table: Przemysław 'from 1405 also in Toszek'; duchy-of-cieszyn /ledger/1 and KF0 contain no Toszek land. Fix: Drop Toszek from the 1315 found and from KF0; add it as a gain c. 1405 (confidence 2, counterpart from a page, for example the Bytom/Koźle duchy) or leave it out until the 1445 division.

Spot checks: `/ledger/0` confirmed ('established about 1315 on the Lesser Polish lands east of the Biała river'); `/ledger/1` confirmed (1445: duchies of Zator and Toszek created); `/ledger/2` confirmed (1457 sale to Casimir for 3,000,000 Prague groschen)

### duchy-of-opava: pass

Area: page None km2 (None), drawn 4299 km2, ratio None, acknowledged True. No area on the page; the radii are stand-ins.

Tried and could not break: Tried: all five territorial events and the four renames against the page. The counterparts duchy-of-raciborz, margraviate-of-moravia and kingdom-of-prussia lack the mirror events (see cross_checks).

Gaps (for a gap-filler):
- `/ledger/9`: The dossier ends at the 1742 division, but the infobox runs 1269-1918 and the Austrian part stayed a duchy (Liechtenstein to 1918). duchy-of-cieszyn, in the same position, is kept to 1849. Make the two consistent if the colour agent wants Habsburg duchies drawn. Try: https://en.wikipedia.org/wiki/Duchy_of_Opava

Spot checks: `/ledger/0` confirmed ('split off from the Margraviate of Moravia before 1269'; confidence 2); `/ledger/2` confirmed (Racibórz 1336 in the body, 1337 in the lead); `/ledger/3` confirmed (1377: John I 'separated Opava from the duchies of Racibórz and Krnov'); `/ledger/8` confirmed (Treaty of Breslau, 1742: the part north of the Opava river, including Głubczyce and Hlučín, to Prussia)

## Cross-dossier matrix: missing and mismatched mirrors

Matched pairs and exceptions are listed in the machine report (history/notes/phase-b/reviews/eu-15-x.json).

- royal-hungary 1538 found (counterpart kingdom-of-hungary): **mismatch**, mirror: kingdom-of-hungary 1538 loss (to eastern-hungarian-kingdom). kingdom-of-hungary lives to 1546 and books no loss to royal-hungary, so both draw the north-west in 1538-1546. The author did not flag this overlap (only the habsburg-monarchy one).
- royal-hungary 1685 gain (counterpart principality-of-upper-hungary): **mismatch**, mirror: principality-of-upper-hungary 1685 loss (to habsburg-monarchy). Same year and land, different slug: the Upper Hungary dossier names habsburg-monarchy.
- royal-hungary 1699 dissolve (counterpart habsburg-monarchy): **mismatch**, mirror: habsburg-monarchy 1547 gain (from kingdom-of-hungary). habsburg-monarchy draws the same land from 1527/1547 on. The author flagged the overlap for the colour agent.
- ottoman-hungary 1541 found (counterpart kingdom-of-hungary): **mismatch**, mirror: kingdom-of-hungary 1541 loss (to ottoman-empire). Same month and land; the counterpart is the metropole slug (colony tint).
- ottoman-hungary 1543 gain (counterpart kingdom-of-hungary): **missing**, mirror: none. kingdom-of-hungary books no 1543-44 loss; the towns may have been royal-hungary's (see thin).
- ottoman-hungary 1552 gain (counterpart habsburg-monarchy): **mismatch**, mirror: habsburg-monarchy 1552 loss (to ottoman-empire). Same year and land (Banat); the slug is the metropole.
- ottoman-hungary 1660 gain (counterpart principality-of-transylvania): **mismatch**, mirror: principality-of-transylvania 1660 loss (to ottoman-empire). After the reviewer fix: same month and land; the slug is the metropole.
- ottoman-hungary 1699 dissolve (counterpart ottoman-empire): **missing**, mirror: none. ottoman-empire books no event naming ottoman-hungary. The Banat reverts to the metropole that the colony tints, so this may be an exception for the colour agent.
- croatia-in-union-with-hungary 1167 loss (counterpart byzantine-empire): **mismatch**, mirror: byzantine-empire 1167 gain (from kingdom-of-hungary). Same year; the Byzantine dossier names kingdom-of-hungary (Sirmium, Bosnia, ...).
- croatia-in-union-with-hungary 1180 gain (counterpart byzantine-empire): **missing**, mirror: none. byzantine-empire books only a vassal_end with kingdom-of-hungary in 1180, no loss of Dalmatia.
- croatia-in-union-with-hungary 1327 loss (counterpart banate-of-bosnia): **mismatch**, mirror: banate-of-bosnia 1326 gain (from nobody / kingdom-of-serbia). Bosnia books Završje from nobody and Hum from Serbia in 1326; nothing from Croatia.
- croatia-in-union-with-hungary 1482 loss (counterpart ottoman-empire): **missing**, mirror: none. ottoman-empire books 1482 gains from kingdom-of-bosnia only.
- croatia-in-union-with-hungary 1522 loss (counterpart ottoman-empire): **missing**, mirror: none. ottoman-empire books no 1522 Knin gain.
- croatia-in-union-with-hungary 1527 loss (counterpart habsburg-monarchy): **missing**, mirror: none. habsburg-monarchy books no 1527 gain naming croatia-in-union-with-hungary; kingdom-of-hungary /ledger/86 books the 1527 loss of Croatia to habsburg-monarchy itself (overlap 1102-1527, flagged by the author).
- croatia-in-union-with-hungary 1527 dissolve (counterpart habsburg-monarchy): **missing**, mirror: none. As /ledger/10.
- royal-prussia 1466 found (counterpart teutonic-order): **mismatch**, mirror: teutonic-order 1466 loss (to house-of-jagiellon). Same month and land; the Order names house-of-jagiellon.
- royal-prussia 1772 loss (counterpart kingdom-of-prussia): **mismatch**, mirror: kingdom-of-prussia 1772 gain (from polish-lithuanian-commonwealth). Prussia names the Commonwealth, month 8 (5 August treaty) against the infobox month 7.
- royal-prussia 1772 dissolve (counterpart kingdom-of-prussia): **mismatch**, mirror: kingdom-of-prussia 1772 gain (from polish-lithuanian-commonwealth). As /ledger/2.
- prince-bishopric-of-warmia 1243 found (counterpart old-prussians): **mismatch**, mirror: old-prussians 1253 loss (to teutonic-order). Old Prussians lose the land to the Order in 1253 and regain it 1260-1277; teutonic-order gains Warmia in 1249.
- prince-bishopric-of-warmia 1772 loss (counterpart kingdom-of-prussia): **mismatch**, mirror: kingdom-of-prussia 1772 gain (from polish-lithuanian-commonwealth). Same year; Prussia names the Commonwealth.
- prince-bishopric-of-warmia 1772 dissolve (counterpart kingdom-of-prussia): **mismatch**, mirror: kingdom-of-prussia 1772 gain (from polish-lithuanian-commonwealth). As /ledger/1.
- hussite-bohemia 1419 found (counterpart kingdom-of-bohemia): **missing**, mirror: none. counterpart predates this addition; mirror to add there
- hussite-bohemia 1420 gain (counterpart kingdom-of-bohemia): **missing**, mirror: none. counterpart predates this addition; mirror to add there
- hussite-bohemia 1420 gain (counterpart kingdom-of-bohemia): **missing**, mirror: none. counterpart predates this addition; mirror to add there
- hussite-bohemia 1421 gain (counterpart kingdom-of-bohemia): **missing**, mirror: none. counterpart predates this addition; mirror to add there
- hussite-bohemia 1434 loss (counterpart kingdom-of-bohemia): **missing**, mirror: none. counterpart predates this addition; mirror to add there
- hussite-bohemia 1437 loss (counterpart kingdom-of-bohemia): **missing**, mirror: none. counterpart predates this addition; mirror to add there
- hussite-bohemia 1437 dissolve (counterpart kingdom-of-bohemia): **missing**, mirror: none. counterpart predates this addition; mirror to add there
- duchy-of-pomerelia 1271 occupation_start (counterpart margraviate-of-brandenburg): **missing**, mirror: none. margraviate-of-brandenburg books no 1271 Gdańsk occupation (its 1272 gain is from duchy-of-greater-poland).
- duchy-of-pomerelia 1273 occupation_end (counterpart margraviate-of-brandenburg): **missing**, mirror: none. As /ledger/2.
- duchy-of-pomerelia 1308 occupation_start (counterpart margraviate-of-brandenburg): **mismatch**, mirror: margraviate-of-brandenburg 1307 gain (from nobody). Brandenburg books a 1307 gain from nobody; Pomerelia books a 1308 occupation.
- duchy-of-pomerelia 1308 loss (counterpart teutonic-order): **mismatch**, mirror: teutonic-order 1308 gain (from kingdom-of-poland). Same month; the Order names kingdom-of-poland.
- duchy-of-pomerelia 1309 occupation_end (counterpart margraviate-of-brandenburg): **mismatch**, mirror: margraviate-of-brandenburg 1309 loss (to teutonic-order). Brandenburg ends its hold by a loss to the Order; Pomerelia by an occupation_end. Both are 1309-9.
- duchy-of-pomerelia 1309 loss (counterpart teutonic-order): **mismatch**, mirror: teutonic-order 1309 gain (from margraviate-of-brandenburg). Same month; the Order names Brandenburg (Soldin).
- duchy-of-pomerelia 1309 dissolve (counterpart teutonic-order): **mismatch**, mirror: teutonic-order 1309 gain (from margraviate-of-brandenburg). As /ledger/9.
- duchy-of-sieradz 1299 loss (counterpart kingdom-of-bohemia): **mismatch**, mirror: kingdom-of-bohemia 1300 gain (from duchy-of-greater-poland: Greater Poland and Kujavia). Bohemia books no gain from Sieradz; its 1300 gain names Greater Poland.
- duchy-of-sieradz 1306 gain (counterpart kingdom-of-bohemia): **mismatch**, mirror: kingdom-of-bohemia 1305 loss (to kingdom-of-poland: Kujavia incl. Sieradz-Łęczyca). Within a year; Bohemia names kingdom-of-poland.
- kingdom-of-galicia-and-lodomeria 1809 loss (counterpart russian-empire): **mismatch**, mirror: russian-empire 1809 gain (from austrian-empire). Same year and land (Tarnopol); the slug is the metropole.
- kingdom-of-galicia-and-lodomeria 1815 gain (counterpart russian-empire): **mismatch**, mirror: russian-empire 1815 loss (to austrian-empire). Same year and land; the slug is the metropole.
- new-east-prussia 1807 loss (counterpart russian-empire): **mismatch**, mirror: russian-empire 1807 gain (from kingdom-of-prussia). Same year and land (Białystok); the slug is the metropole.
- west-prussia 1773 found (counterpart royal-prussia): **mismatch**, mirror: royal-prussia 1772 dissolve (to kingdom-of-prussia). Same author: royal-prussia ends 1772-7 handing over to kingdom-of-prussia; west-prussia starts 1773-9 from royal-prussia (14 months later).
- domain-of-matthew-iii-csak 1301 found (counterpart kingdom-of-hungary): **mismatch**, mirror: kingdom-of-hungary 1305 loss (counterpart string "Matthew III Csak", confidence 1). 4 years apart and a string counterpart. The Matthew page supports 1297 (de facto) and 1301 (grant). kingdom-of-hungary should name the slug and use 1301.
- domain-of-matthew-iii-csak 1311 gain (counterpart kingdom-of-hungary): **mismatch**, mirror: kingdom-of-hungary 1305 loss (string counterpart). Hungary books one 1305 loss of all Slovakia; the domain books a 1301 core and a 1311 peak.
- domain-of-matthew-iii-csak 1315 loss (counterpart kingdom-of-hungary): **missing**, mirror: none. No Visegrád gain in kingdom-of-hungary 1314-1315.
- domain-of-matthew-iii-csak 1321 loss (counterpart kingdom-of-hungary): **mismatch**, mirror: kingdom-of-hungary 1321 gain (string counterpart). Same year; kingdom-of-hungary should name the slug.
- domain-of-matthew-iii-csak 1321 dissolve (counterpart kingdom-of-hungary): **mismatch**, mirror: kingdom-of-hungary 1321 gain (string counterpart). As /ledger/4.
- duchy-of-opava 1269 found (counterpart margraviate-of-moravia): **missing**, mirror: none. counterpart predates this addition; mirror to add there
- duchy-of-opava 1336 gain (counterpart duchy-of-raciborz): **missing**, mirror: none. counterpart predates this addition; mirror to add there
- duchy-of-opava 1377 loss (counterpart duchy-of-raciborz): **missing**, mirror: none. counterpart predates this addition; mirror to add there
- duchy-of-opava 1742 loss (counterpart kingdom-of-prussia): **mismatch**, mirror: kingdom-of-prussia 1742 gain (from habsburg-monarchy). Same year; Prussia names the overlord.
- duchy-of-opava 1742 dissolve (counterpart habsburg-monarchy): **missing**, mirror: none. counterpart predates this addition; mirror to add there

## Problems for the orchestrator

- Reading the verdicts: a 'fix' verdict whose findings are all applied:true was fixed by the reviewer. A 'fix' verdict with any applied:false finding (pomerelia, sieradz, leczyca's overlap, new-east-prussia, matthew-iii-csak, oswiecim) means non-blocking edits the author still has to make. 'fail' is for blocking shape or area errors.
- The reviewer made two edits, both re-validated (0 errors, 0 warnings) and read back after 10 s: ottoman-hungary (Nagyvárad gain moved from 1664/habsburg-monarchy to 1660-08/principality-of-transylvania; source added; ledger indices 12-15 shifted), and duchy-of-eczyca-1231-1352 /ledger/1/source (now the Sieradz page).
- Gazetteer: region 'Warmia' resolves to 12,645 km2, about 2.8 times the 4,500 km2 of the Warmia article; it takes in Elbląg and Ducal Prussian towns (Ostróda, Pasłęk, Morąg, Bartoszyce). Region 'West Prussia' (alt name 'Royal Prussia') = Pomeranian + Kuyavian-Pomeranian voivodeships: it leaves out Elbląg and takes in southern Kuyavia, Bydgoszcz, Słupsk and Lębork. Region 'Kuyavia' = the whole Kuyavian-Pomeranian voivodeship, including Chełmno Land, Toruń and Bydgoszcz. These three entries caused most of the shape failures (royal-prussia, warmia, south-prussia, west-prussia) and will mislead other dossiers; route them to the gazetteer agent.
- royal-hungary overlaps kingdom-of-hungary 1538-1546 (Hungary lives to 1546 and books no loss to royal-hungary); the author flagged only the habsburg-monarchy overlap. croatia-in-union-with-hungary overlaps kingdom-of-hungary 1102-1527 (flagged).
- Counterpart dossiers written before these additions (kingdom-of-hungary, kingdom-of-bohemia, teutonic-order, kingdom-of-prussia, habsburg-monarchy, ottoman-empire, byzantine-empire, margraviate-of-brandenburg, old-prussians, duchy-of-raciborz, margraviate-of-moravia, principality-of-upper-hungary, principality-of-transylvania, russian-empire, banate-of-bosnia) book these lands against the metropole or an older slug. 21 mirrors are missing and 30 disagree on the slug (see cross_checks). kingdom-of-hungary's 'Matthew III Csak' 1305 events (string counterpart, confidence 1) are not supported by the Matthew III Csák page (1297/1301).
- kingdom-of-croatia, banate-of-bosnia and russian-empire appeared on the mount during this review and were cross-checked as found. kingdom-of-poland, polish-lithuanian-commonwealth, republic-of-venice, duchy-of-warsaw, free-city-of-danzig, free-city-of-krakow, second-polish-republic and austrian-empire have no dossier yet (counted as exceptions).
- No page failed to load for the reviewer. 24 WebFetch pages were opened.

## Gazetteer names needed

- Chełmno Land (region): royal-prussia / west-prussia (suggested fix)
- Netze District (region): west-prussia (suggested fix)
- Brześć Kujawski Voivodeship (region): south-prussia (suggested fix)
- Royal Prussia (region): royal-prussia (now an alt_name of 'West Prussia', which is drawn differently)
- Sieradz Land (region): duchy-of-sieradz
- Łęczyca Land (region): duchy-of-eczyca-1231-1352
- Nin (place): croatia-in-union-with-hungary (missing 1329 event)
- Lidzbark Warmiński (place): prince-bishopric-of-warmia (capital)
- Włocławek (place): south-prussia / west-prussia / new-east-prussia
- Toszek (place): duchy-of-oswiecim
- Visegrád (place): royal-hungary / ottoman-hungary / domain-of-matthew-iii-csak
- Esztergom (resolves) / Vác (place): royal-hungary / ottoman-hungary
