# Review: batch eu-10-d (Kingdom of France)

Written 2026-10-25 by the adversarial reviewer for eu-10-d. Machine copy: history/notes/phase-b/reviews/eu-10-d.json.

## Verdict

kingdom-of-france: **fail** (back to the author). The validator passes (0 errors, 0 warnings with --resolve), the identity, capitals, rulers, certainty and most of the 18 spot-checked events hold, and the infobox area gap (10,000,000 km2 in 1714 including colonies against 528,772 km2) is acknowledged. It fails on one mis-dated confidence-3 event (the 1706 end of the occupation of Savoy) and on missing events that leave land lost but never gained (Charleroi 1668, Freiburg 1677/1713, Breisach and Kehl 1703, Lille 1713) or shape changes unexplained (the 1356-1361 apanages, Anjou 1480), most of them on pages the author had opened.

One fix was applied by the reviewer: /ledger/61 (Provence) moved from 1482 at confidence 1 to 1481 at confidence 2, from the Crown lands page's 1481 entry; the file re-validates.

## What was checked

- Mechanical: validate_dossier --resolve: valid, no warnings. Ledger sorted, found at 987 and dissolve at 1792, 8 contest pairs, rulers contiguous, capitals Paris/Versailles/Paris, certainty 987-1792.
- Area: Kingdom of France infobox gives only '1714 (including colonies): 10,000,000 km2'; Cliopatria 1713 shape 528,772 km2 (ratio 0.053); acknowledged in /keyframe_review/88 and /97.
- Cell checks with tools/grid.py (H3 res 5) for Lille, Tournai, Douai, Charleroi, Dunkirk, Freiburg, Breisach, Strasbourg, Ghent and Dutch towns in the shapes 1659-1734.
- Neighbour dossiers read: comtat-venaissin, house-of-bourbon, house-of-valois-anjou, duchy-of-bavaria (no France events), plus west-franks and new-france. The other 36 Context polities are not written yet (their groups have not run).

## Findings (author to act)

1. `/ledger/61` (APPLIED by reviewer). Provence gain dated 1482 at confidence 1 although the cited Crown lands page dates the Angevin inheritance to 1481.
   - Evidence: Crown lands of France, entry 1481: 'Charles IV, Duke of Anjou, Count of Maine, Guise, Mortain and Gien, who succeeded his uncle René I of Anjou as Duke of Anjou and Count of Provence and Forcalquier' (dies, lands to Louis XI); house-of-valois-anjou /ledger/13 dissolves in December 1481 with Provence to the crown.
   - Fix: Year 1481, confidence 2, note and region text quote the 1481 entry. Applied by the reviewer; file re-validated (0 errors, 0 warnings).
2. `/ledger/127` (to do). Occupation of Savoy ended in September 1706 at confidence 3, but the page does not say the French left Savoy then and implies they still held Savoy and Nice after 1707 (mis-dated confidence-3 event).
   - Evidence: War of the Spanish Succession page: 'by May 1706, the French held most of Savoy except Turin' and 'By the end of 1707, fighting in Italy ceased, apart from minor attempts by Victor Amadeus to recover Nice and Savoy.' The page only dates the relief of Turin (September 1706). The 'Savoy' of the page is the Savoyard state; /keyframe_review/94 (1702 shape) adds Piedmont 32, Italy 34 and Nice 13 cells and no Savoy-proper cells, while /ledger/126 occupies only region Savoy.
   - Fix: Split the occupation: /ledger/126 occupation_start 1703 (or 1704) of union Piedmont + County of Nice + Savoy (counterpart house-of-savoy, confidence 2); occupation_end 1706-09 for Piedmont only (Turin relieved); occupation_end for Savoy and County of Nice at Utrecht (1713-04) from a page that says so (Victor Amadeus II of Sardinia or Treaty of Utrecht); keyframes 1706-1712 keep Savoy and Nice as occupation, not solid. Do not keep confidence 3 on a 1706 end for Savoy.
3. `/keyframe_review/97` (to do). Lille comes back into the 1713 shape with no event: the ledger loses Lille in 1708 (/ledger/128) and never regains it, and the 1713 note does not mention it.
   - Evidence: Cell check (grid.polity_cells): Lille's H3 cell is inside the 1702 and 1706 shapes, outside the 1709 shape and inside the 1713 and 1734 shapes. /ledger/129 (1713) only cedes Ypres, Tournai, Menen, Veurne, Knokke and Warneton; the War of the Spanish Succession page is silent on Lille's return.
   - Fix: Add a 1713-04 gain of Lille (place Lille, km 30) citing a page that states its return at Utrecht (Treaty of Utrecht, Lille or Siege of Lille (1708)); name a real counterpart for /ledger/128 and the new gain (the Dutch Republic held Lille 1708-1713: dutch-republic) instead of 'Allies (the page names no state)'.
4. `/ledger/111` (to do). The 1678 loss returns Charleroi (and Ghent) that the ledger never gained: the 1668 War of Devolution gains are missing.
   - Evidence: Franco-Dutch War page: 'The retention of border towns like Charleroi and Tournai in 1668 allowed Louvois to pre-position supply dumps.' Cell check: Lille, Tournai and Dunkirk are outside the 1659 and 1662 shapes and inside the 1670 shape (/keyframe_review/84 'which Flemish towns these cells are is not stated'); no event between 1662 and 1670 adds them. The page names Charleroi and Tournai; it is one the author opened.
   - Fix: Add a 1668-05 gain from kingdom-of-spain (Treaty of Aix-la-Chapelle) of Charleroi and Tournai (and Lille, Douai etc. from a page that lists them: War of Devolution or Treaty of Aix-la-Chapelle (1668)); add an occupation_start for Ghent (taken March 1678) or drop Ghent from /ledger/111; add the War of Devolution to wars[].
5. `/ledger/132` (to do). Freiburg, Breisach and Kehl are lost twice (1697 /ledger/125 and 1714 /ledger/132) and never gained; Landau is 'retained' with no event.
   - Evidence: Franco-Dutch War page: 'the French commander succeeded in capturing Freiburg in November 1677.' War of the Spanish Succession page: '[Villars] then captured Kehl and Breisach' (1703), 'during the 1703 campaign French forces retook Landau', 'after the loss of Landau and Freiburg in November 1713', 'France retained Landau'. Both pages are in sources[]. Cell check: Freiburg is outside every France shape 1659-1734.
   - Fix: Add a 1677-11 gain (or occupation_start confirmed by Nijmegen 1679) of Freiburg from holy-roman-empire; a 1703 occupation_start/gain of Breisach, Kehl and Landau; a 1713-11 capture of Freiburg and Landau; keep the 1714 return of Freiburg, Breisach and Kehl; mark the keyframes 1677-1696 adjust (or note) for the Freiburg cells Cliopatria lacks.
6. `/keyframe_review/29` (to do). The 1363 shape drops 379 cells but the ledger records only the Bretigny cessions and Burgundy: the apanage detachments of 1356-1361 (Anjou and Maine, Berry and Auvergne, Touraine) and the return of Anjou in 1480 have no events.
   - Evidence: /keyframe_review/28-29 cite the Crown lands page for 'Berry 1360, Touraine 1361' and list Maine 38, Anjou 31, Auvergne 69, Touraine 13 among the cells lost. house-of-valois-anjou /ledger/0 founds the house in 1356 from kingdom-of-france with Anjou and Maine; its /ledger/9-10 have a French occupation of Anjou 1474-1476 and /ledger/11 a 1480-07 loss of Anjou to kingdom-of-france ('Louis XI again added Anjou to the royal domain'); the France ledger mirrors none of them (the 1482 keyframe's +31 Anjou cells are explained only by Maine 1481).
   - Fix: Add loss events: Anjou and Maine to house-of-valois-anjou (1356, or 1360 if the Crown lands page so dates the apanage); Berry and Auvergne (1360) and Touraine (1361) to their apanage holders (needs a counterpart slug, e.g. duchy-of-berry, or flag in counterparts_needing_dossiers); occupation_start 1474 / occupation_end 1476 of Anjou and a 1480-07 gain of Anjou from house-of-valois-anjou.
7. `/ledger/58` (to do). The 1453 gain from kingdom-of-england includes Bearn, which was not English and which the page does not name; the 1453-1588 keyframes then draw Bearn solid French although the dossier itself treats Bearn as Navarre's until 1620.
   - Evidence: Hundred Years' War page: 'Bordeaux fell to the French on 19 October and there were no more hostilities afterwards'; WebFetch found no mention of Bearn on the page. The note admits 'Bearn cells in the shape are Cliopatria's'. /ledger/88 (vassal_start 1589) and /ledger/91-92 (1620 'merged into the Kingdom of France') contradict a French Bearn from 1453; /keyframe_review/70 cuts Bearn only from 1595.
   - Fix: Drop {region: Bearn} from /ledger/58; cut Bearn from the solid shapes 1453-1588 (/keyframe_review/43-69: minus region Bearn, as the 1595 correction does) or justify it with a page; check the 7 Bearn cells of the 1285 shape the same way.
8. `/ledger/106` (to do). Occupation region {country: Netherlands} at confidence 3 is the whole Republic; the page has the French in Utrecht and Gelderland only.
   - Evidence: Franco-Dutch War page: 'the council of Utrecht delivered the keys of the gates', 'On 19 June, the French took the fortress of Naarden', 'After Nijmegen had been taken on 9 July', 'he also did not continue his advance to the west', 'the province of Overijssel surrendered as a whole to the bishop of Münster'. The 1673 shape has 41 Netherlands cells, a fraction of the country.
   - Fix: Replace the region in /ledger/106 and /ledger/107 with union admin1 Utrecht + Gelderland (Netherlands) (+ Naarden, which the gazetteer lacks), and keep confidence 3 only with that region.
9. `/ledger/75` (to do). Milan lost in February 1525 (Pavia) at confidence 2, but the page dates the loss of Milan to November 1521.
   - Evidence: Italian Wars page: in November 1521 an Imperial-Papal army 'captured Milan and restored Francesco II Sforza as duke'; 'a French attempt to retake Milan was ended by defeat at Bicocca on 27 April' 1522; the page does not say Milan was retaken in 1524.
   - Fix: Loss year 1521, month 11; mark /keyframe_review/57 (1521 shape) adjust with Lombardy removed from 1522 (or a new keyframe 1522-1525); if a 1524 reoccupation is wanted, find a page for it.
10. `/ledger/97` (to do). Roussillon is gained twice from Spain (1642 and again 1659, /ledger/102) and Artois twice (1640 /ledger/95 and 1659) with no loss between.
   - Evidence: Kingdom of France page: 'formalised France's seizure (1642) of ... Roussillon' and 'County of Artois (1659)': the 1642 and 1640 events are military seizures, the 1659 events the cessions.
   - Fix: Make the 1642 Roussillon event (and the 1640 Artois part) an occupation_start or contest_start closed by the 1659 gain.
11. `/ledger` (to do). The French occupations of the Comtat Venaissin (1663, 1668, 1768-1774) recorded by comtat-venaissin have no mirror in this ledger.
   - Evidence: comtat-venaissin /ledger/3-8: occupation_start/end with counterpart kingdom-of-france, citing the Comtat Venaissin infobox 'French occupation: 1663, 1668, 1768-1774'.
   - Fix: Add occupation_start/occupation_end pairs for 1663, 1668 and 1768-1774 (region Comtat Venaissin, source the Comtat Venaissin page).
12. `/ledger/76` (to do). Bourbon lands: this ledger gains them in 1531, house-of-bourbon loses them in August 1523; the 1564 loss to house-of-bourbon (/ledger/85) has no mirror there; Bourbon's 1327 foundation and La Marche gains (1327, 1477) from kingdom-of-france have no mirror here.
   - Evidence: Crown lands page: '1531: possessions of the disgraced Charles III, Duke of Bourbon are confiscated'; house-of-bourbon /ledger/7: 'In August 1523, all the disputed lands were sequestered from Bourbon'; house-of-bourbon /ledger/0, /ledger/1, /ledger/5.
   - Fix: Agree with the house-of-bourbon owner: e.g. occupation_start 1523-08 (sequestration) and gain 1531 here, occupation in Bourbon's ledger; give /ledger/85 a page or drop it; add the 1327 and 1477 mirrors or explain why the Bourbonnais fief is not removed from the shape.
13. `/keyframe_review/88` (to do). A 28-cell Gulf of St Lawrence strip is kept in the metropolitan shape 1683-1762 with no page, against the dossier's own rule of cutting colonies (1791), and /ledger/139 loses it in 1763.
   - Evidence: Note of /keyframe_review/88: 'no page opened describes them; kept'. new-france (existing dossier) carries Cape Breton and New France to 1763.
   - Fix: Cut the Canada cells from /keyframe_review/88-103 (intersect with country Canada removed) and drop /ledger/139, or cite a page and confirm no overlap with new-france's keyframes.
14. `/identity/predecessors/0` (to do). Start 987 overlaps west-franks, which ends in 989.
   - Evidence: west-franks /ledger/35 dissolve 989: 'the traditional end of West Francia is the Capetian election of June 987'.
   - Fix: No change here; the west-franks owner should end in 987 (route to that group).

## Thin (for a gap-filler; within the page budget, not faults)

- `/ledger/1`: 990 vassal_start of Aquitaine rests on the Cliopatria relation row (confidence 1). Try https://en.wikipedia.org/wiki/Duchy_of_Aquitaine
- `/ledger/2`: 1003 loss and 1018 gain of Burgundy (confidence 1); the succession war of 1003-1016. Try https://en.wikipedia.org/wiki/Robert_II_of_France
- `/ledger/10`: 1138/1139 Aquitaine union and 1152 loss (confidence 1); the marriage was 1137, the annulment March 1152. Try https://en.wikipedia.org/wiki/Eleanor_of_Aquitaine
- `/ledger/23`: 1250 apanages of Toulouse/Poitou and Anjou/Maine/Touraine (confidence 1). Try https://en.wikipedia.org/wiki/Alphonse,_Count_of_Poitiers
- `/ledger/31`: 1305 Limousin addition (confidence 1). Try https://en.wikipedia.org/wiki/Limousin_(province)
- `/ledger/46`: 1402 and 1407 additions (Guyenne, Orleanais, Gascony; Auvergne, Languedoc) at confidence 1. Try https://en.wikipedia.org/wiki/John,_Duke_of_Berry
- `/ledger/64`: 1482 Franche-Comte/Artois entry and 1497 exit (confidence 1); the treaties are Arras 1482 and Senlis 1493. Try https://en.wikipedia.org/wiki/Treaty_of_Senlis
- `/ledger/69`: 1497 loss of Roussillon (confidence 1) has no prior gain; Roussillon enters the 1463 shape unexplained (Treaty of Bayonne 1462, returned by the Treaty of Barcelona 1493). Try https://en.wikipedia.org/wiki/Treaty_of_Barcelona_(1493)
- `/ledger/85`: 1564 exit of the Bourbon block (confidence 1). Try https://en.wikipedia.org/wiki/House_of_Bourbon
- `/ledger/93`: Lorraine occupation 1636-1659 (confidence 1); restitution by the Treaty of Vincennes 1661. Try https://en.wikipedia.org/wiki/Duchy_of_Lorraine
- `/ledger/95`: 1640 Artois, Picardy and Alsace additions (confidence 1). Try https://en.wikipedia.org/wiki/Siege_of_Arras_(1640)
- `/ledger/133`: 1741-1744 German-lands occupation (confidence 1); War of the Austrian Succession not in wars[]. Try https://en.wikipedia.org/wiki/War_of_the_Austrian_Succession
- `/wars/6`: French Wars of Religion has 0 zones; the group scope asks for the Wars of Religion zones (1562-1598). Try https://en.wikipedia.org/wiki/French_Wars_of_Religion
- `/keyframe_review/83`: Dunkirk (bought from England in 1662) enters the shape by 1670 with no event. Try https://en.wikipedia.org/wiki/Dunkirk
- `/keyframe_review/98`: 1734 additions (Germany 7, Lorraine 8): War of the Polish Succession (Kehl, Philippsburg, Lorraine to Stanislaw 1737) absent from ledger and wars. Try https://en.wikipedia.org/wiki/War_of_the_Polish_Succession
- `/keyframe_review/10`: Lyonnais cells added 1188, 1314, 1540 unexplained (Lyon annexed 1312). Try https://en.wikipedia.org/wiki/Lyonnais

## Spot checks

- `/ledger/4`: confirmed (Crown_lands_of_France)
- `/ledger/42`: confirmed (Crown_lands_of_France)
- `/ledger/61`: mis-dated (Crown_lands_of_France)
- `/ledger/19`: confirmed (Louis_VIII_of_France)
- `/ledger/52`: confirmed (Hundred_Years%27_War)
- `/ledger/58`: confirmed (Hundred_Years%27_War)
- `/ledger/127`: not on page (War_of_the_Spanish_Succession)
- `/ledger/128`: confirmed (War_of_the_Spanish_Succession)
- `/ledger/129`: confirmed (War_of_the_Spanish_Succession)
- `/ledger/132`: confirmed (War_of_the_Spanish_Succession)
- `/ledger/106`: confirmed (Franco-Dutch_War)
- `/ledger/111`: confirmed (Franco-Dutch_War)
- `/ledger/75`: mis-dated (Italian_Wars)
- `/ledger/70`: confirmed (Italian_Wars)
- `/ledger/71`: confirmed (Italian_Wars)
- `/ledger/79`: confirmed (Italian_Wars)
- `/ledger/78`: confirmed (Crown_lands_of_France)
- `/ledger/140`: confirmed (Kingdom_of_France)

Detail: 1034 Burgundy ('1034: the king gives the Duchy of Burgundy to his brother Robert'), 1364 ('Philip the Bold receives in appanage the Duchy of Burgundy'), 1224 ('By the end of summer 1224, Louis had conquered Limousin, Perigord, and Quercy'), 1435 (the Treaty of Arras 'returned Paris to the King of France'; the page gives no 1436), 1453 (Bordeaux 19 October; no Bearn on the page), 1499/1501/1536/1532/1766 as noted. Mis-dated: 1706 Savoy (page implies Savoy and Nice still French after 1707), 1525 Milan (page: November 1521), 1482 Provence (page: 1481, fixed).

## Cross-dossier matrix (summary)

- mismatch: kingdom-of-france 987 found / west-franks <-> west-franks 989 dissolve. west-franks dissolves 989 (its /ledger/35); this dossier starts July 987; 987-989 claimed by both. West-franks should end 987.
- matched: kingdom-of-france 1481 gain / house-of-valois-anjou <-> house-of-valois-anjou 1481 dissolve. Maine; mirror is Valois-Anjou's December 1481 dissolve.
- matched: kingdom-of-france 1481 gain / house-of-valois-anjou <-> house-of-valois-anjou 1481 dissolve. Provence (moved from 1482 by the reviewer).
- missing: house-of-valois-anjou 1356 found / kingdom-of-france <-> none. Anjou and Maine leave the crown in 1356 in Valois-Anjou's ledger; no loss in kingdom-of-france (the 1363 keyframe drops them).
- missing: house-of-valois-anjou 1474 occupation_start / kingdom-of-france <-> none. French occupation of Anjou 1474-1476 not in kingdom-of-france.
- missing: house-of-valois-anjou 1480 loss / kingdom-of-france <-> none. Anjou to the crown July 1480; kingdom-of-france has no 1480 gain of Anjou.
- mismatch: kingdom-of-france 1531 gain / house-of-bourbon <-> house-of-bourbon 1523 loss. Bourbon's ledger loses the lands by sequestration in August 1523; Crown lands page dates the confiscation 1531.
- missing: kingdom-of-france 1564 loss / house-of-bourbon <-> none. Confidence-1 event from the shapes; house-of-bourbon has no 1564 gain from kingdom-of-france.
- matched: kingdom-of-france 1589 gain / house-of-bourbon <-> house-of-bourbon 1589 dissolve. Henry IV's accession; Bourbon dissolves 2 August 1589.
- missing: house-of-bourbon 1327 gain / kingdom-of-france <-> none. Bourbon's 1327 foundation and La Marche gains (1327, 1477) from kingdom-of-france have no loss here; the France shape keeps the Bourbonnais (overlap noted by the author).
- matched: kingdom-of-france 1791 gain / comtat-venaissin <-> comtat-venaissin 1791 dissolve. Comtat dissolves 14 September 1791.
- missing: comtat-venaissin 1663 occupation_start / kingdom-of-france <-> none. French occupations of 1663, 1668 and 1768-1774 are not in kingdom-of-france.
- missing: kingdom-of-france 1708 loss / Allies (the page names no state) <-> none. Descriptive counterpart, not in counterparts_needing_dossiers; the Dutch Republic held Lille 1708-1713 (dutch-republic, eu-09, not yet written). The 1713 regain is missing.
- missing: kingdom-of-france 1191 gain / Artois (holder not named by the page) <-> none. Descriptive counterpart not in counterparts_needing_dossiers; Artois came from the Flemish inheritance: county-of-flanders (eu-10, not yet written), not county-of-artois (row starts 1241).
- missing: kingdom-of-france 1271 gain / Alfonso, Count of Poitou (apanage) <-> none. Descriptive counterpart; use county-of-toulouse / county-of-poitou (eu-10, not yet written).
- missing: kingdom-of-france 1402 gain / Guyenne, Orleanais and Gascony cells (holder not named by the pages opened) <-> none. Confidence-1 shape addition with no holder; listed under thin.
- missing: kingdom-of-france 1407 gain / Auvergne and Languedoc (holder not named by the pages opened) <-> none. Confidence-1 shape addition with no holder; listed under thin.
- missing: kingdom-of-france 1640 gain / Artois, Picardy and Alsace (holder not named by the pages opened) <-> none. Confidence-1; holder is kingdom-of-spain for Artois and the Empire/Habsburgs for Alsace; also double-counts the 1659 Artois gain.
- exceptions: every other counterpart is owned by a group not yet run (eu-08, eu-09, eu-10, eu-11, eu-12, eu-13) or is listed in the author's counterparts_needing_dossiers; see the JSON for the per-counterpart event lists.

## Notes on the author's notes

- The notes flag the Cliopatria overlaps (Navarre, Brittany, Naples, Lorraine, Catalonia, colonies) and the unexplained Lyonnais and Limousin cells; they do not flag Bearn 1453-1588, the Lille return, the Freiburg/Breisach/Kehl gains or the 1356-1361 apanages.
- The notes attribute the 1532 Brittany union to the Kingdom of France page; the reviewer's read of that page found no 1532 date (the Crown lands page, which the ledger cites, has it). Correct the attribution.
- Gazetteer names needed: the author's 24 plus Naarden and Dunkirk.
