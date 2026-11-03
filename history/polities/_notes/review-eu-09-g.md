# Review of batch eu-09-g (2026-10-25)

Dossiers: electorate-of-trier (fix, fixed by the reviewer), free-county-of-burgundy (pass), electorate-of-saxony (fail: one structural finding for the author; one small fix applied).
Validator: 0 errors on all three (Trier warnings are the unknown places Boppard, Prüm, Montabaur and the new slugs prum-abbey, nassau-weilburg; Saxony warnings are the saxe-* slugs).
Neighbour dossiers read (ledger grep): holy-roman-empire-minor-states, holy-roman-empire, house-of-ascania, margraviate-of-meissen, archbishopric-of-magdeburg, county-of-artois, kingdom-of-arles, kingdom-of-france, kingdom-of-germany, landgraviate-of-thuringia, kingdom-of-lotharingia-zwentibold. Not written yet (the brief's exception): habsburg-monarchy, swedish-empire, kingdom-of-prussia, duchy-of-burgundy, first-french-empire, french-first-republic, kingdom-of-saxony.

## electorate-of-trier: fix

- FIX (applied by reviewer) `/ledger/0/counterpart; /identity/predecessors/0/slug`: The 898 found event and the predecessor named kingdom-of-germany, whose dossier starts in 911. Evidence: Electorate of Trier page: 'Radbod received complete immunity from all taxes for the entire episcopal territory, granted by Zwentibold' (King of Lotharingia 895-900; dossier kingdom-of-lotharingia-zwentibold 895-900). kingdom-of-germany dossier: start 911. Fix: counterpart and predecessor slug set to kingdom-of-lotharingia-zwentibold; predecessor note rewritten.
- FIX (applied by reviewer) `/ledger/2/counterpart`: The 1309 Boppard gain named holy-roman-empire, whose dossier ends in 1259. Evidence: holy-roman-empire.json: end 1259, successor holy-roman-empire-minor-states (1260-1806), which draws the imperial cities after 1260. Fix: counterpart set to holy-roman-empire-minor-states; reviewer note appended.
- FIX (applied by reviewer) `/wars/3/note`: The note said the page does not name the wars of the French occupations. Evidence: Electorate of Trier page: 'Warfare returned to the Electorate in 1673 during the Franco-Dutch War'; 'War of Palatinate Succession in 1688'; 'During the War of the Spanish Succession in 1702'; 'the War of the Polish Succession started in 1734; the following year Trier was again occupied'. Fix: note rewritten to name the four wars.
- THIN `/ledger/3`: Confidence-1 bridging gain of 1333: dates and manner of the acquisition of the Moselle towns (Wittlich, Cochem, Zell, Bernkastel, Saarburg, Oberwesel), Montabaur and the Limburg share before Cliopatria's 1333. Try: https://de.wikipedia.org/wiki/Kurtrier
- THIN `/wars/3`: French occupations of Trier begun 1684, 1688 and 1702 are on the page but not in the ledger (no end dates); a bridging end at the Treaty of Ryswick (1697) would let them be hatched. Try: https://en.wikipedia.org/wiki/Treaty_of_Ryswick
- THIN `/ledger/8`: After 'Spanish troops retook Trier by surprise in 1635 and imprisoned Sötern' the Spanish hold on the city (to about 1645) is not drawn. Try: https://en.wikipedia.org/wiki/Philipp_Christoph_von_S%C3%B6tern
- Spot check `/ledger/0` (https://en.wikipedia.org/wiki/Electorate_of_Trier): confirmed (infobox 'Imperial immediacy: 898'; immunity 'granted by Zwentibold')
- Spot check `/ledger/7` (https://en.wikipedia.org/wiki/Electorate_of_Trier): confirmed ('French troops captured the city in 1632 to help Sötern')
- Spot check `/ledger/8` (https://en.wikipedia.org/wiki/Electorate_of_Trier): confirmed ('Spanish troops retook Trier by surprise in 1635')
- Spot check `/ledger/9` (https://en.wikipedia.org/wiki/Electorate_of_Trier): confirmed ('Warfare returned to the Electorate in 1673 ... occupied Trier and stayed until 1675')
- Spot check `/ledger/14` (https://en.wikipedia.org/wiki/Electorate_of_Trier): confirmed (war 'started in 1734; the following year Trier was again occupied by the French, who stayed until 1737')
- Spot check `/ledger/16` (https://en.wikipedia.org/wiki/Electorate_of_Trier): confirmed ('In August 1794, French Republican troops took Trier')
- Spot check `/ledger/18` (https://en.wikipedia.org/wiki/German_mediatisation): confirmed (Lunéville 9 February 1801; table: France 'Trier: left bank')
- Spot check `/ledger/19` (https://en.wikipedia.org/wiki/German_mediatisation): confirmed (Final Recess of 25 February 1803; table: Princes of Nassau 'Trier: right bank'; the prose names no Nassau-Weilburg)
- Area: infobox None (None), Cliopatria 16954.3, ratio None; The page has no area. Cliopatria's 1333-1618 shapes (16,110-17,088 km2, bbox 7.02-13.03 E, 48.79-50.18 N) cannot contain Trier (6.64 E) or Koblenz (50.36 N): the misplaced-block finding is confirmed from shapes.csv; all ten marked wrong and replaced by the Moselle reading (about 8,350 km2).

## free-county-of-burgundy: pass

- THIN `/keyframe_review/0`: Limits of the county 982-1328 (Besançon, Salins after the 1237 exchange, Montbéliard, Belfort); the modern Franche-Comté region is a reading. Try: https://fr.wikipedia.org/wiki/Comt%C3%A9_de_Bourgogne
- THIN `/ledger (1295-1315)`: The 1295 cession of the county to the French crown's administration (Otto IV, Treaty of Vincennes) is named in the notes but not drawn; a vassal or control span 1295-1315 may be due. Try: https://en.wikipedia.org/wiki/Otto_IV,_Count_of_Burgundy
- Spot check `/ledger/0` (https://en.wikipedia.org/wiki/County_of_Burgundy): confirmed ('The county was formed in 982 by count Otto-William')
- Spot check `/ledger/1` (https://en.wikipedia.org/wiki/County_of_Artois): confirmed ('Upon her death in 1329, Artois passed to ... Countess Joan II')
- Spot check `/ledger/2` (https://en.wikipedia.org/wiki/County_of_Artois): confirmed (Joan II 'died in 1330', bequest to Joan III; the page's 'marrying Odo IV of Burgundy in 1330' is quoted correctly)
- Spot check `/ledger/5` (https://en.wikipedia.org/wiki/County_of_Burgundy): confirmed ('In 1382, she bequeathed her estates to her son Count Louis II of Flanders')
- Spot check `/ledger/6` (https://en.wikipedia.org/wiki/County_of_Artois): confirmed ('In 1384 all Flanders, Artois and Franche-Comté finally became part of the ... Duchy of Burgundy'); infobox 'Personal union of Philip the Bold with Duchy of Burgundy: 1384'
- Area: infobox None (None), Cliopatria 22596.7, ratio None; County of Burgundy page has no area field. Author compares the Franche-Comté part (59 cells) with the modern region and identifies the other 32 cells as Cliopatria's Artois; consistent with the 1.58-6.99 E, 46.28-51.11 N bbox.

## electorate-of-saxony: fail

- FIX (author to do) `/ledger/8; /keyframe_review/7-11; /ledger/10-11; /wars/1`: 1485-1547: the dossier keeps the Albertine Duchy of Saxony (Dresden, Leipzig, Meissen) inside the electorate, so the electorate is drawn at about 34,000 km2 where the electoral (Ernestine) state held roughly half of it; the Partition of Leipzig is logged as a rename. Evidence: Electorate of Saxony page: 'The Ernestines retained the title of elector' and 'Albert resided in Dresden as Duke of Saxony and was dominant in the east' (Partition of Leipzig, 11 November 1485). One dossier per state (research brief section 6): the Albertine duchy 1485-1547 is a separate state; the author's own wars/1 has the electorate fighting 'Ernestine Saxony (John Frederick I)' in 1547, when John Frederick was the elector. Fix: Replace /ledger/8 with a split (or loss) in November 1485 to a new counterpart albertine-duchy-of-saxony (region: the Albertine share, e.g. the Cliopatria 1556 shape minus the 1363 Saxe-Wittenberg shape, as /ledger/2 already reads Meissen); end keyframe 7 in 1485 and mark shapes 1487, 1492, 1502 and 1529 adjust with a correction that removes that region; at 19 May 1547 add a merge (or gain) of the Albertine duchy with Maurice's accession beside the existing loss of the Ernestine lands; correct /wars/1 belligerents (electorate = John Frederick I; Maurice = Albertine duke); list albertine-duchy-of-saxony (1485-1547) under counterparts_needing_dossiers.
- FIX (applied by reviewer) `/ledger/13/source`: The 1635 gain of Jüterbog, Dahme, Burg and Querfurt cited the Peace of Prague page, which puts those towns under the 1636 Traditionsrezess annex, not the 1635 treaty. Evidence: Peace of Prague (1635) page: 'Under the Traditionsrezess annex of 1636, Ferdinand ceded both territories in perpetuity, plus the towns of Jüterbog, Dahme and Burg Querfurt.' Saxe-Weissenfels page: 'adjudicated to Saxony by the 1635 Peace of Prague ... as well as the exclaves of Jüterbog, Dahme and Burg'. Fix: Source set to the Saxe-Weissenfels page (already in sources); note now records both pages' dates. Year and confidence 2 kept.
- THIN `/ledger/17`: Confidence-1 bridging end (October 1648) of the Swedish occupation outside Leipzig; the 1645 Truce of Kötzschenbroda is undated. Try: https://de.wikipedia.org/wiki/Waffenstillstand_von_K%C3%B6tzschenbroda
- THIN `/ledger/18`: Confidence-1 bridging start (1648) of the Leipzig garrison; the Swedes held Leipzig from 1642. Try: https://en.wikipedia.org/wiki/Leipzig
- THIN `/keyframe_review/15-17`: Cliopatria changes of 1564, 1579 and 1588 (Vogtland 1569, Mansfeld sequestration, Henneberg share 1583) undated within the page budget. Try: https://en.wikipedia.org/wiki/Vogtland
- THIN `/keyframe_review/34`: Seven cells missing from the 1746-1805 shapes against 1648 (Burg sold to Brandenburg 1687 per the Saxe-Weissenfels page is one candidate, not in the ledger). Try: https://en.wikipedia.org/wiki/Saxe-Weissenfels
- Spot check `/ledger/3` (https://en.wikipedia.org/wiki/Electorate_of_Saxony): confirmed ('After the death in 1440 of Frederick IV ... the Landgraviate of Thuringia reverted to the Electorate')
- Spot check `/ledger/5-6` (https://en.wikipedia.org/wiki/Frederick_II,_Elector_of_Saxony): confirmed ('in 1446 to the Saxon Brother War, which found an end only on 27 January 1451 with the peace of Naumburg'); /ledger/4 1445 and /ledger/7 1482 also confirmed there
- Spot check `/ledger/12` (https://en.wikipedia.org/wiki/Electorate_of_Saxony): confirmed ('In September 1620 Saxon troops marched into the two Lusatian territories and occupied them')
- Spot check `/ledger/13` (https://en.wikipedia.org/wiki/Peace_of_Prague_(1635)): mis-dated on the cited page (towns under the 1636 annex); confirmed for 1635 on the Saxe-Weissenfels page; source fixed
- Spot check `/ledger/15` (https://en.wikipedia.org/wiki/Peace_of_Prague_(1635)): confirmed ('Under the Traditionsrezess annex of 1636, Ferdinand ceded both territories in perpetuity')
- Spot check `/ledger/16` (https://en.wikipedia.org/wiki/Peace_of_Prague_(1635)): confirmed ('In 1642, Sweden won a decisive victory at Breitenfeld, and overran Saxony')
- Spot check `/ledger/19` (https://en.wikipedia.org/wiki/Electorate_of_Saxony): confirmed (tribute paid 'on 30 June 1650' before 'the last of the Swedes leave Leipzig')
- Spot check `/ledger/20, /ledger/27` (https://en.wikipedia.org/wiki/Saxe-Weissenfels): confirmed (infobox 'Death of elector Johann Georg I: 8 October 1656'; 'Ducal line extinct: 16 May 1746')
- Spot check `/ledger/23` (https://en.wikipedia.org/wiki/Electorate_of_Saxony): confirmed ('The Swedes occupied Electoral Saxony in 1706/07')
- Spot check `/ledger/10-11` (https://en.wikipedia.org/wiki/Electorate_of_Saxony): confirmed (Capitulation of Wittenberg 19 May 1547; Ernestines kept 'Weimar, Jena, Saalfeld, Weida, Gotha, Eisenach and Coburg')
- Area: infobox 39425 (1805), Cliopatria 33682.8, ratio 0.85; Body text, not infobox: 'In 1805 the Electorate of Saxony covered 39,425 square kilometres'; ratio is Cliopatria/page, acknowledged in keyframe_review 35 and 38. Separately, 1485-1547 is drawn at about twice the electoral state's size (fix 1).

## Free County of Burgundy: what I tried
Every dated event (982, 1329, 1330, 1361, 1382, 1384) is on its cited page with the year. The personal-union handling is uneven (1330 union with the duchy is a rename, the 1384 one a dissolve), but it follows Cliopatria's rows and is stated in the notes; the county's continuation to 1678 is acknowledged. Nothing to change.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| electorate-of-trier 1018 gain (holy-roman-empire) | holy-roman-empire   | missing | HRE dossier (eu-08, 962-1259) logs no 1018 grant of Koblenz; an imperial grant inside the Empire, so the owner may record it as no loss; route to eu-08. |
| electorate-of-trier 1309 gain (holy-roman-empire-minor-states) | holy-roman-empire-minor-states   | missing | Counterpart corrected by the reviewer from holy-roman-empire (ends 1259). Minor-states dossier has no Boppard event; route to eu-09 (minor states). |
| electorate-of-trier 1333 gain (holy-roman-empire-minor-states) | holy-roman-empire-minor-states 1431 loss | mismatch | Trier: confidence-1 bridging gain of the Moselle land in 1333. Minor-states logs a 1431 loss of 25 cells to Cliopatria's misplaced Trier row (moot once the row is not drawn); minor-states should instead stop drawing the Moselle land when this dossier draws it. |
| electorate-of-trier 1576 gain (prum-abbey) | prum-abbey   | exception | No dossier; listed in counterparts_needing_dossiers. |
| electorate-of-trier 1632 occupation_start (kingdom-of-france) | kingdom-of-france   | missing | France dossier (eu-10) has no occupation of Trier; route to eu-10. |
| electorate-of-trier 1673 occupation_start (kingdom-of-france) | kingdom-of-france   | missing | France dossier (eu-10) has no occupation of Trier; route to eu-10. |
| electorate-of-trier 1705 occupation_start (kingdom-of-france) | kingdom-of-france   | missing | France dossier (eu-10) has no occupation of Trier; route to eu-10. |
| electorate-of-trier 1735 occupation_start (kingdom-of-france) | kingdom-of-france   | missing | France dossier (eu-10) has no occupation of Trier; route to eu-10. |
| electorate-of-trier 1794 occupation_start (french-first-republic) | french-first-republic   | exception | No dossier (owner group not run). Cliopatria row French First Republic is 1792-1795, so the 1801 annexation needs whichever dossier draws France in 1801. |
| electorate-of-trier 1801 loss (french-first-republic) | french-first-republic   | exception | As above. |
| electorate-of-trier 1803 loss (nassau-weilburg) | nassau-weilburg   | exception | No dossier; listed in counterparts_needing_dossiers (Duchy of Nassau row starts 1806). |
| free-county-of-burgundy 1329 gain (county-of-artois) | county-of-artois 1332 dissolve | mismatch | Pages (County of Artois) put Artois with the Countess of Burgundy from 1329; county-of-artois (eu-10) dissolves into this state in 1332. Flagged by the author; county-of-artois should end in 1329. |
| free-county-of-burgundy 1333 (none) (holy-roman-empire-minor-states) | holy-roman-empire-minor-states 1333 loss | mismatch | Minor-states logs a 1333 loss of Franche-Comté to this state (confidence 1); this dossier draws the county from 982, so minor-states should not draw Franche-Comté in 1260-1332. Flagged by the author. |
| free-county-of-burgundy 1384 dissolve (duchy-of-burgundy) | duchy-of-burgundy   | exception | No duchy-of-burgundy dossier yet (eu-10, not written). |
| electorate-of-saxony 1356 found (house-of-ascania) | house-of-ascania 1363 split | mismatch | Saxony starts at the Golden Bull (10 January 1356, confirmed); house-of-ascania renames in 1356 but splits Saxe-Wittenberg off only in 1363, and minor-states logs a 1363 loss of 21 cells to Saxony. Saxe-Wittenberg is drawn twice 1356-1362; route to house-of-ascania and minor-states authors (move to 1356). |
| electorate-of-saxony 1423 gain (margraviate-of-meissen) | margraviate-of-meissen 1423 dissolve | matched | Meissen dissolves in 1423 with successor electorate-of-saxony. |
| electorate-of-saxony 1440 gain (Landgraviate of Thuringia (Wettin line)) | landgraviate-of-thuringia   | exception | Existing landgraviate-of-thuringia ends 1264; the Wettin landgraviate of 1440-1482 is listed in counterparts_needing_dossiers. |
| electorate-of-saxony 1445 loss (Landgraviate of Thuringia (Wettin line)) | landgraviate-of-thuringia   | exception | Existing landgraviate-of-thuringia ends 1264; the Wettin landgraviate of 1440-1482 is listed in counterparts_needing_dossiers. |
| electorate-of-saxony 1482 gain (Landgraviate of Thuringia (Wettin line)) | landgraviate-of-thuringia   | exception | Existing landgraviate-of-thuringia ends 1264; the Wettin landgraviate of 1440-1482 is listed in counterparts_needing_dossiers. |
| electorate-of-saxony 1485 rename ((should be albertine-duchy-of-saxony)) | albertine-duchy-of-saxony   | missing | See fix 1: the Partition of Leipzig created the Albertine duchy; no dossier exists. |
| electorate-of-saxony 1547 loss (holy-roman-empire-minor-states) | holy-roman-empire-minor-states 1556 gain | mismatch | Capitulation of Wittenberg 19 May 1547 (confirmed); minor-states records the Ernestine lands arriving at Cliopatria's 1556 re-cut. Route to minor-states: 1547. The Ernestine lands also need their own dossier (listed). |
| electorate-of-saxony 1620 occupation_start (habsburg-monarchy) | habsburg-monarchy   | exception | No habsburg-monarchy dossier yet (eu-09 part not written). |
| electorate-of-saxony 1635 gain (archbishopric-of-magdeburg) | archbishopric-of-magdeburg 1648 loss | mismatch | Saxe-Weissenfels page: the towns were adjudicated to Saxony by the 1635 Peace of Prague (the Peace of Prague page: 1636 annex). Magdeburg dossier dates the loss 1648; route to its author (1635 or 1636). Flagged by the author. |
| electorate-of-saxony 1636 gain (habsburg-monarchy) | habsburg-monarchy   | exception | No dossier yet. |
| electorate-of-saxony 1642 occupation_start (swedish-empire) | swedish-empire   | exception | No swedish-empire dossier yet (eu-14). |
| electorate-of-saxony 1648 occupation_start (swedish-empire) | swedish-empire   | exception | No swedish-empire dossier yet (eu-14). |
| electorate-of-saxony 1706 occupation_start (swedish-empire) | swedish-empire   | exception | No swedish-empire dossier yet (eu-14). |
| electorate-of-saxony 1656 loss (saxe-weissenfels) | saxe-weissenfels   | exception | No dossier; listed in counterparts_needing_dossiers (not in eu-09-x's list). |
| electorate-of-saxony 1657 loss (saxe-merseburg) | saxe-merseburg   | exception | No dossier; listed in counterparts_needing_dossiers (not in eu-09-x's list). |
| electorate-of-saxony 1657 loss (saxe-zeitz) | saxe-zeitz   | exception | No dossier; listed in counterparts_needing_dossiers (not in eu-09-x's list). |
| electorate-of-saxony 1718 gain (saxe-zeitz) | saxe-zeitz   | exception | No dossier; listed in counterparts_needing_dossiers (not in eu-09-x's list). |
| electorate-of-saxony 1738 gain (saxe-merseburg) | saxe-merseburg   | exception | No dossier; listed in counterparts_needing_dossiers (not in eu-09-x's list). |
| electorate-of-saxony 1746 gain (saxe-weissenfels) | saxe-weissenfels   | exception | No dossier; listed in counterparts_needing_dossiers (not in eu-09-x's list). |
| electorate-of-saxony 1756 occupation_start (kingdom-of-prussia) | kingdom-of-prussia   | exception | No kingdom-of-prussia dossier yet (eu-09 part not written). |
| electorate-of-saxony 1806 occupation_start (first-french-empire) | first-french-empire   | exception | No dossier yet (eu-20). |

## Counterparts needing dossiers
- Albertine Duchy of Saxony (albertine-duchy-of-saxony, 1485-1547) new from this review (fix 1 on electorate-of-saxony)
- Ernestine Saxony (lands of John Frederick I's line after 1547) (ernestine-saxony, 1547-1572) 
- Landgraviate of Thuringia (Wettin, William III) (landgraviate-of-thuringia, 1440-1482) existing dossier ends 1264: extend or new slug
- Saxe-Weissenfels (saxe-weissenfels, 1656-1746) 
- Saxe-Merseburg (saxe-merseburg, 1657-1738) 
- Saxe-Zeitz (saxe-zeitz, 1657-1718) 
- Prüm Abbey (prum-abbey, 1222-1576) 
- Nassau-Weilburg (nassau-weilburg, 1803-1806) 

## Gazetteer names needed
Boppard (place, electorate-of-trier), Prüm (place, electorate-of-trier), Montabaur (place, electorate-of-trier), Lusatia (region, electorate-of-saxony), Upper Lusatia (region, electorate-of-saxony), Lower Lusatia (region, electorate-of-saxony), Merseburg (place, electorate-of-saxony), Zeitz (place, electorate-of-saxony), Naumburg (place, electorate-of-saxony), Weißenfels (place, electorate-of-saxony), Torgau (place, electorate-of-saxony), Sangerhausen (place, electorate-of-saxony), Querfurt (place, electorate-of-saxony), Jüterbog (place, electorate-of-saxony), Lübben (place, electorate-of-saxony), Guben (place, electorate-of-saxony)

## Problems
- No page failed for the reviewer. The author's failed page (Truce of Kötzschenbroda) was not retried.
- None of the Saxe-*, Prüm, Nassau-Weilburg, Ernestine or Albertine counterparts is in eu-09-x's additions list: the orchestrator must assign them.
- Reviewer applied four small fixes in place (Trier /ledger/0 and /identity/predecessors/0, /ledger/2, /wars/3/note; Saxony /ledger/13); both files re-validate with 0 errors.
