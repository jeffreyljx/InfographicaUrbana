# Notes, batch eu-16-i (Zaporozhian Cossacks, Sloboda Ukraine)

Written 2026-10-25. Pages opened with WebFetch: Zaporozhian Cossacks, Zaporozhian Sich, Treaty of Andrusovo, New Serbia (historical province), Treaty of the Pruth, Sloboda Ukraine, Sloboda Cossacks (the last repeated the Sloboda Ukraine text). Also opened and thin: Nova Serbia (disambiguation). Failed: https://en.wikipedia.org/wiki/New_Serbia_(Ukraine) (url_not_found; the article is New_Serbia_(historical_province)).

## zaporozhian-cossacks
- Neither Zaporozhian page gives an area or a boundary, so every Cliopatria outline is `ok` with the extent unverified. The one real move, 1752 (-91 cells, 23,000 km2, Kirovohrad/Poltava/Cherkasy), is New Serbia ('on the land of the Zaporizhian Sich'). Shape changes 1662-1683 are 1-4 cell jitter; 1769 is one cell.
- Start moved from Cliopatria's 1662 to 1552 (Sich page infobox c. 1552; Don Cossacks row also starts 1552) with a soft 100 km core round Zaporizhzhia (new keyframe `zaporozhian-cossacks_1552`, 1552-1661, confidence 2). The Sich page says the Cossacks were in the Kiev Voivodeship 1583-1657: delete the keyframe if the renderer must not draw a Cossack core inside the Commonwealth.
- End 1775 (manifesto of 3 August 1775), not Cliopatria's 1774: 1772 shape marked `adjust` (years only).
- Vassalage from the Zaporozhian side has no event type. The Sich infobox gives 'de jure vassal of Poland-Lithuania (1583-1654), Muscovy (1654-1709), the Ottoman Empire (1711-1734), and the Russian Empire (1734-1775)'; 1667 Andrusovo made the Sich 'a condominium of both states'. Suggest `vassal_start`/`vassal_end` with counterpart `zaporozhian-cossacks` in polish-lithuanian-commonwealth, tsardom-of-russia, ottoman-empire and russian-empire.
- Cross-checks: ottoman-empire 1677 'loss' of right-bank Ukraine to zaporozhian-cossacks (confidence 1) is not matched by a Zaporozhian gain (+2 cells in 1677); ottoman-empire 1739 'Zaporozhye region' ceded to Russia is not in any page opened here; the Cossacks page says the 1774 Kucuk Kaynarca treaty 'annexed the Crimean Khanate into Russia' (the crimean-khanate dossier has 1783): not used.
- Pages disagree on the Chortomlyk Sich: destroyed before Poltava (Sich page) or after (Cossacks page); the Sich page also has 'destroyed in 1711 by the Russian government'. The Sich table overlaps for 1728 (Chortomlyk 1728-1730, Kamianka c. 1728-1734); the capitals list uses Kamianka.
- Capital coordinates are approximate site positions (the sites are under the Kakhovka reservoir), not from the pages; years are the Sich page's table.
- Gazetteer: 'Danube Delta' (successor land of the Danubian Sich) is not in regions.jsonl.
- Needed from other groups: Cossack Hetmanate (1648-1764; the 1654 split and 1667 partition along the Dnieper) in eu-16-x; Danubian Sich (1775-1828); New Serbia (1752-1764); Novorossiya Governorate (admin unit of the Russian Empire, no dossier needed).
- Not opened for lack of budget: Russo-Polish War (1654-1667), Great Northern War, Treaty of Belgrade (1739), Russo-Turkish War (1768-1774), Eternal Peace of 1686, Cossack Hetmanate.

## sloboda-ukraine
- Different state from `ukraine` (1992-2024) although Cliopatria gives both Q598570; not merged. The id is kept as Cliopatria gives it.
- Written as `type: colony` (semiautonomous region under the tsar, a Great Russian prikaz from 1688); start 1650 (page: 'From 1650 to 1765 ... increasingly organized'), end 1765 month 7 (decree of 28 July 1765). Cliopatria runs 1670-1768: 1763 shape marked `adjust` (years only); new keyframe 1650-1669 carries the 1670 outline back at confidence 1.
- No area, boundary or regiment founding year on either page; the Izium and Belgorod lines, the regiments and Slavo-Serbia (1753-1764, 'to the south') need further pages. The tint after 1765 is the Sloboda Ukraine Governorate (Kharkov Viceroyalty 1780, abolished 1835): the Russian Empire dossier should cover it.
- Cliopatria's Tsardom of Russia shape has no cell in common with the Sloboda Ukraine shape: the tsardom dossier should state whether it counts this land.
