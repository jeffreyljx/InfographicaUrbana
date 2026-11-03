# Review of batch eu-10-a (Brittany, Gascony, Normandy, Anjou)

Reviewer run of 2026-10-25. Validator: 0 errors on all four (2 warnings on duchy-of-brittany: county-of-nantes has no dossier yet, listed as needed). Spot checks weighted to confidence-3 events and the largest land moves; no fabricated or mis-dated confidence-3 event found. Verdict 'thin' on all four: the remaining items are missing mirror events and gaps a gap-filler can add from the pages named. Small fixes the reviewer verified on the page were applied in place and re-validated (marked applied).

## duchy-of-brittany: thin

Fixes:
- `/ledger/20/region` (applied by reviewer): The 1488 French occupation covered the whole of Ille-et-Vilaine and Loire-Atlantique, which put Rennes and Nantes under French garrisons in 1488-1491. Evidence: Mad War page: Charles VIII withdrew his forces 'except in the town garrisons of the territories pledged by Francis'; the only towns it has the French take are 'On 12 July, royal forces captured Fougères and then Dinan'. The dossier's own capital note has Anne crowned in Rennes on 10 February 1489. Fix: Region narrowed to the points Fougères with Saint-Aubin-du-Cormier (-1.25, 48.32, 20 km) and Dinan (-2.05, 48.45, 15 km), with a reviewer note; confidence stays 2.
- `/ledger/21/region` (applied by reviewer): The occupation_end carried the same over-wide region. Evidence: As /ledger/20. Fix: Same region as /ledger/20.
- `/ledger (missing loss, 1020)` (for the author or gap-filler): Normandy's gain of the land between the Sélune and the Couesnon, with Mont-Saint-Michel (duchy-of-normandy /ledger/5, counterpart duchy-of-brittany) has no loss here, and the Normandy dossier's 936 and 990 corrections take the strip out of Normandy until 1020, so nobody draws it 936-1019. Evidence: History of Normandy: 'Between 1009 and 1020, the Normans continued their westward expansion, taking all the land between the rivers Sélune and Couesnon, including Mont Saint-Michel'. Fix: Add the strip (point -1.51, 48.64, 10 km, as in Normandy's correction) to keyframes _939, _947 and _990 by union, and a loss in 1020 to duchy-of-normandy at confidence 2 with that sentence.
- `/ledger (missing vassal_start, 1491)` (for the author or gap-filler): kingdom-of-france /ledger/71 has a vassal_start of duchy-of-brittany in 1491 (personal union, confidence 3); this dossier records only the end of the French garrisons in December 1491. Evidence: Rule 3: a vassal_start of X needs a vassal_start in X's ledger. The dossier's own model (personal union 1492-1532) is the same relation. Fix: Add vassal_start 1491, month 12, counterpart kingdom-of-france, region the 1491 shape, source the Anne of Brittany page (marriage of 6 December 1491); the 1532 dissolve then ends it.

Thin (for a gap-filler):
- `/ledger/1`: 960 loss of Nantes rests on the counts' list only (confidence 1); the House of Nantes (Hoël I 960-981, Guerech 981-c.988) also held the ducal title, so the 960-990 split of Brittany needs a page. Try: https://en.wikipedia.org/wiki/Hoël_I,_Duke_of_Brittany
- `/keyframe_review/1`: The Duchy page: after Alan II 'the dukes no longer ruled over the regions of Cotentin, Avranchin, and Mayenne'; no dated event for the Mayenne edge. Try: https://en.wikipedia.org/wiki/Alan_II,_Duke_of_Brittany
- `/keyframe_review/12`: 1344-1401 shapes drop the west; the WBS page says 'The English now controlled Brest, Quimper, and Vannes' (after La Roche-Derrien, 1347), but only Brest (30 km) is occupied in the ledger. Try: https://en.wikipedia.org/wiki/Battle_of_La_Roche-Derrien
- `/ledger/6`: 1164 border lands lost with no regain (the page names no place; region is a reading); fold into the 1166-1181 occupation or add a regain. Try: https://en.wikipedia.org/wiki/Henry_II_of_England
- `/identity/rulers`: Rulers strip not compiled (optional). Try: https://en.wikipedia.org/wiki/List_of_rulers_of_Brittany

Spot checks: `/ledger/5` confirmed; `/ledger/9` confirmed; `/ledger/12` confirmed (garrison sentence has no year; it sits in the 1343 Truce of Malestroit passage); `/ledger/15` confirmed; `/ledger/17` confirmed; `/ledger/18` confirmed; `/ledger/20` confirmed date; region overstated (fixed); `/ledger/22` confirmed.
Area: No area on the Duchy of Brittany page; the 37.4k km2 shapes are plausible for historic Brittany with the Pays nantais.

## duchy-of-gascony: thin

Fixes:
- `/ledger/6/note` (applied by reviewer): The quoted sentence is not the page's wording. Evidence: Duchy of Gascony page: 'the definite detachment of Pamplona from the Duchy in 824'; it does not say 'The Pamplonese were definitively detached'. Fix: Quote replaced with the page's words; year, region and confidence unchanged.
- `/ledger (missing vassal_start 1032, vassal_end 1035)` (for the author or gap-filler): kingdom-of-pamplona /ledger/14 and /ledger/20 hold Gascony as a vassal 1032-1035; this dossier has no mirror (the author's notes say so but the rule needs both sides). Evidence: Duchy of Gascony page: Gascony was brought under 'suzerain to King Sancho III of Navarre for a short period up to 1035'; 1032 is Sans VI Guilhem's death on the same page. Fix: Add vassal_start 1032 and vassal_end 1035, counterpart kingdom-of-pamplona, region the 1028 shape, confidence 2, source the Duchy of Gascony page.
- `/ledger/9` (for the author or gap-filler): The 1058 merge into duchy-of-aquitaine does not match duchy-of-aquitaine /ledger/3, a 1053 gain of Gascony at confidence 3. Evidence: William VIII page: 'He became Duke of Gascony in 1052' and Duke of Aquitaine 'between 1058 and 1086'; the Duchy of Gascony infobox gives the Basque duchy '864-1053'; the Duchy of Aquitaine page has the union 'from 1053'. Fix: Not a fault in this dossier (1058 is sourced); the orchestrator should have one side move so both name the same year: 1058 here, or 1053 in both with the 1052 rename kept.

Thin (for a gap-filler):
- `/keyframe_review/7`: Nothing drawn 825-863 (dukes under Carolingian counts); the 864 gain from west-franks has no loss in west-franks. Try: https://en.wikipedia.org/wiki/Sancho_II_Sánchez_of_Gascony
- `/ledger/2`: 793 loss at confidence 1, no page. Try: https://en.wikipedia.org/wiki/Sancho_I_of_Gascony
- `/identity/rulers`: Rulers 1032-1052 missing (Odo of Aquitaine 1032-1039, Bernard II Tumapaler 1039-1052 per the page lists); 846-852 also empty. Try: https://en.wikipedia.org/wiki/Bernard_II,_Count_of_Armagnac
- `/identity/capitals/0`: Bordeaux (lat 44.84) lies outside every shape before 864 (768 shape tops out at lat 44.78, 806 shape at 43.41); start the capital in 864 or note it as the dukes' seat outside the drawn land. Try: https://en.wikipedia.org/wiki/Seguin_I_of_Gascony

Spot checks: `/ledger/6` confirmed (quote paraphrased; fixed); `/ledger/8` confirmed; `/ledger/7` confirmed; `/ledger/3` confirmed; `/ledger/5` confirmed; `/ledger/1` confirmed: page dates Louis's kingdom 781; event follows Cliopatria's 783 and says so.
Area: No area on the Duchy of Gascony page.

## duchy-of-normandy: thin

Fixes:
- `/ledger (missing gain 1063, loss 1070)` (for the author or gap-filler): county-of-anjou /ledger/9 loses Maine to duchy-of-normandy in 1063 (confidence 3), but this dossier has no Maine event, no Maine war and no word on it in its notes, so about 13,500 km2 is drawn by nobody 1063-1065. Evidence: Maine (province) page: 'William invaded Maine in force in 1063' and 'he controlled the county by the beginning of 1064'; 'In 1069 the citizens of Le Mans revolted against the Normans', expelled in 1070 with Hugh V proclaimed count. Fix: Add gain 1063 from county-of-anjou (Maine, the Cliopatria County of Maine shape) with keyframe _990 adjusted to add Maine 1063-1065 and _1066 to 1069, and loss 1070 to county-of-maine; or, if county-of-maine (Cliopatria 1066-1110) is to draw Maine, make it a vassal_start 1063 / vassal_end 1070 and have county-of-anjou name county-of-maine. Agree it with the county-of-maine author.
- `/ledger/7, /ledger/8` (for the author or gap-filler): Contest ends 1050 and Passais is taken from county-of-maine, while county-of-anjou /ledger/7 ends the same contest in 1052 with Anjou the holder. Evidence: Geoffrey II page: Geoffrey 'seized the towns of Domfront and Alençon'; William besieged Domfront 'throughout the winter of 1052' and then 'rapidly retook Alençon and then Domfront'. History of Normandy: 'completed these campaigns in 1050 by taking Passais'. Alençon page: 1049-1051. Fix: Pick one year with the Anjou author (1051 or 1052 fits both Alençon and Geoffrey II pages) and name county-of-anjou as the 1050/1052 counterpart for Domfront.

Thin (for a gap-filler):
- `/keyframe_review/4`: 990 shape's growth south (Alençon, Bellême, Mortagne) has no event; within the 5-page budget. Try: https://en.wikipedia.org/wiki/Lords_of_Bellême
- `/ledger/3`: 942 occupation is a placeholder year (confidence 1); Richard I page: after 17 December 942 Louis 'seized the lands of the Duchy', giving lower Normandy to Hugh the Great, no year. Try: https://en.wikipedia.org/wiki/Louis_IV_of_France
- `/wars`: Battles of Mortemer (1054) and Varaville (1057) and the conquest of Maine (1063-1064) are in county-of-anjou's wars with duchy-of-normandy as belligerent but not here. Try: https://en.wikipedia.org/wiki/Battle_of_Mortemer
- `/notes`: Vexin, Évreux, Eu and the Channel Islands not covered (author's gap). Try: https://en.wikipedia.org/wiki/Duke_of_Normandy

Spot checks: `/ledger/1` confirmed; `/ledger/2` confirmed; `/ledger/5` confirmed; `/ledger/4` confirmed; `/ledger/6` confirmed (1049-1051); `/ledger/10` confirmed; `/ledger/11` confirmed.
Area: No area on the Duchy of Normandy page; 37.9k km2 is about 1.27x modern Normandy (29.9k), the extra being the Bellême-Mortagne cells noted in /keyframe_review/4.

## county-of-anjou: thin

Fixes:
- `/ledger/7/note` (applied by reviewer): The note said William's winter siege of Domfront failed. Evidence: Geoffrey II page: after the winter of 1052 William 'rapidly retook Alençon and then Domfront, driving Count Geoffrey back across the Norman border into Maine'. Fix: Note rewritten to the page's outcome, marked as a reviewer correction.
- `/ledger/8` (for the author or gap-filler): Saintonge is lost in 1062 but never gained or drawn (no keyframe holds it), and duchy-of-aquitaine draws Saintonge from 990 with no 1062 gain. Evidence: County of Anjou page: Fulk 'allowed Saintonge to be taken in 1062 by the duke of Aquitaine' and had earlier held Saintonge as an appanage; no acquisition year on the page. Fix: Add the Angevin acquisition of Saintonge (Geoffrey Martel, 1030s) as a gain from duchy-of-aquitaine with keyframes adjusted, or keep the 1062 event and say in the note that the land is not drawn; route the 1062 mirror to duchy-of-aquitaine.

Thin (for a gap-filler):
- `/ledger/1`: Saumur 1026 counterpart is a string; the page's sentence ('while Odo was besieging Montboyau, Fulk surprised and took Saumur') makes Odo II of Blois the likely holder: county-of-blois. Try: https://en.wikipedia.org/wiki/Odo_II,_Count_of_Blois
- `/ledger (Loudun)`: duchy-of-aquitaine /ledger/1 loses the Loudunais and Mirebalais to county-of-anjou (confidence 1); no mirror here. County page: Geoffrey Greytunic obtained 'the concession in fief of the district of Loudun' (before 990). Try: https://en.wikipedia.org/wiki/Fulk_III,_Count_of_Anjou
- `/keyframe_review/5`: 1294 shape (bbox to lon 3.62, lat 49.32) carries 11 cells outside Anjou and Maine, verdict ok; probably Charles of Valois's other fiefs (Valois, Alençon, Perche, Chartres): adjust to Anjou and Maine. Try: https://en.wikipedia.org/wiki/Charles,_Count_of_Valois
- `/ledger/11`: 1126-1290 dormant span (merge into angevins at confidence 1); orchestrator to confirm the one-state reading. Try: https://en.wikipedia.org/wiki/Geoffrey_Plantagenet,_Count_of_Anjou

Spot checks: `/ledger/4` confirmed; `/ledger/7` year confirmed; outcome misreported (fixed); `/ledger/8` confirmed; `/ledger/9` confirmed; `/ledger/10` confirmed; `/ledger/12` confirmed; `/ledger/13` confirmed; `/ledger/1` confirmed.
Area: No area on the County of Anjou page ('roughly co-extensive with the diocese of Angers'); 9.8k km2 in 990 fits.

## Cross-dossier matrix

- duchy-of-brittany 939 found (kingdom-of-brittany) -> kingdom-of-brittany 939 dissolve: matched. Both August 939.
- duchy-of-brittany 960 loss (county-of-nantes) -> county-of-nantes - -: exception. No dossier; listed in counterparts_needing_dossiers.
- duchy-of-brittany 990 gain (county-of-nantes) -> county-of-nantes - -: exception. As above.
- duchy-of-brittany 1158 loss (angevin-empire) -> angevin-empire - -: exception. eu-11 has not run.
- duchy-of-brittany 1164 loss (angevin-empire) -> angevin-empire - -: exception. eu-11 has not run.
- duchy-of-brittany 1166 occupation_start (angevin-empire) -> angevin-empire - -: exception. eu-11 has not run (end 1181).
- duchy-of-brittany 1185 gain (angevin-empire) -> angevin-empire - -: exception. eu-11 has not run.
- duchy-of-brittany 1343 occupation_start (kingdom-of-england) -> kingdom-of-england - -: exception. eu-11 has not run (end 1397).
- duchy-of-brittany 1488 occupation_start (kingdom-of-france) -> kingdom-of-france - -: missing. kingdom-of-france (written) has no occupation of Brittany 1488-1491 nor the 1378-1379 contest; route to its author.
- kingdom-of-france 1491 vassal_start (duchy-of-brittany) -> duchy-of-brittany - -: missing. France /ledger/71 (confidence 3); Brittany has no vassal_start: fix listed for duchy-of-brittany.
- duchy-of-brittany 1532 dissolve (kingdom-of-france) -> kingdom-of-france 1532 gain: matched. France /ledger/85-86 vassal_end and gain 1532; this resolves the author's 1491-or-1532 question: France already treats 1491-1532 as personal union.
- duchy-of-normandy 911 found (west-franks) -> west-franks 911 loss: matched. 
- duchy-of-normandy 924 gain (west-franks) -> west-franks 924 loss: matched. west-franks /ledger/31 also loses the rest of the 926 cells at confidence 1.
- duchy-of-normandy 933 gain (kingdom-of-brittany) -> kingdom-of-brittany 933 loss: matched. 
- duchy-of-normandy 942 occupation_start (west-franks) -> west-franks - -: missing. west-franks (eu-07, written) has no occupation of Normandy 942-946.
- duchy-of-normandy 1020 gain (duchy-of-brittany) -> duchy-of-brittany - -: missing. Same batch: Brittany has no 1020 loss; fix listed for duchy-of-brittany.
- duchy-of-normandy 1050 gain (county-of-maine) -> county-of-maine - -: exception. county-of-maine is another eu-10 part, not yet written; the Geoffrey II page makes Anjou the holder (see Normandy fix).
- duchy-of-normandy 1049 contest_start (county-of-anjou) -> county-of-anjou 1049 contest_start: mismatch. Starts agree; ends differ: Normandy 1050, Anjou 1052.
- duchy-of-normandy 1066 gain (kingdom-of-england) -> kingdom-of-england - -: exception. eu-11 has not run.
- duchy-of-normandy 1071 dissolve (norman-england) -> norman-england - -: exception. eu-11 has not run; norman-england must carry continental Normandy from 1072.
- county-of-anjou 1063 loss (duchy-of-normandy) -> duchy-of-normandy - -: missing. Same batch: Normandy has no Maine gain; fix listed for duchy-of-normandy.
- county-of-anjou 1026 gain (lord of Saumur (page silent)) -> None - -: exception. String counterpart; likely county-of-blois (thin).
- county-of-anjou 1044 gain (county-of-blois) -> county-of-blois - -: exception. county-of-blois is another eu-10 part, not yet written.
- county-of-anjou 1051 gain (county-of-maine) -> county-of-maine - -: exception. Not yet written.
- county-of-anjou 1062 loss (duchy-of-aquitaine) -> duchy-of-aquitaine - -: missing. duchy-of-aquitaine (written) has no 1062 gain and draws Saintonge from 990.
- duchy-of-aquitaine 1030 loss (county-of-anjou) -> county-of-anjou - -: missing. Loudunais and Mirebalais (confidence 1); no gain in Anjou (thin).
- county-of-anjou 1110 gain (county-of-maine) -> county-of-maine - -: exception. Not yet written.
- county-of-anjou 1126 merge (angevins) -> angevins - -: exception. angevins is another eu-10 part, not yet written.
- county-of-anjou 1290 gain (capetian-house-of-anjou) -> capetian-house-of-anjou - -: exception. Not yet written.
- county-of-anjou 1328 merge (kingdom-of-france) -> kingdom-of-france 1322 gain: mismatch. France /ledger/32 has 'Valois and Anjou' rejoin the domain in 1322 from capetian-house-of-anjou; the County page gives 1 April 1328 (Philip VI). France's side should move.
- duchy-of-gascony 783 loss (kingdom-of-the-franks) -> kingdom-of-the-franks 783 gain: matched. 
- duchy-of-gascony 793 loss (kingdom-of-the-franks) -> kingdom-of-the-franks - -: missing. Franks (eu-07, written) have no 793 gain (both sides silent; confidence 1).
- duchy-of-gascony 806 loss (kingdom-of-the-franks) -> kingdom-of-the-franks - -: missing. Franks have no 806 gain.
- duchy-of-gascony 824 loss (kingdom-of-pamplona) -> kingdom-of-pamplona 824 found: mismatch. Pamplona's found names kingdom-of-the-franks, and the Franks lose Pamplona in 825 (confidence 1): the land of Gascony's 806 shape is claimed by both; route to eu-12 and eu-07.
- duchy-of-gascony 864 gain (west-franks) -> west-franks - -: missing. west-franks has no 864 loss of Gascony.
- kingdom-of-pamplona 1032 vassal_start (duchy-of-gascony) -> duchy-of-gascony - -: missing. Gascony has no vassal_start 1032 / vassal_end 1035; fix listed for duchy-of-gascony.
- duchy-of-gascony 1058 merge (duchy-of-aquitaine) -> duchy-of-aquitaine 1053 gain: mismatch. Five years apart; both sourced (William VIII page 1058; Aquitaine page 1053).

## For the orchestrator

- No page failed to load; WebFetch returns a summarising model's reading, so quotes were checked for sense and year, not character by character.
- None of the four state pages gives an area; area checks compare with modern regions only.
- Reviewer fixes applied in place and re-validated (0 errors): duchy-of-brittany /ledger/20-21 regions, county-of-anjou /ledger/7 note, duchy-of-gascony /ledger/6 quote.
- duchy-of-normandy ends 1071 though the duchy lasted to 1204: orchestrator to confirm that norman-england (eu-11) carries continental Normandy from 1072.
- county-of-anjou is drawn 990-1125 and 1290-1328 with a dormant span (merge into angevins 1126 at confidence 1): orchestrator to confirm one state, or split at 1290.
- Gascony/Aquitaine union year (1058 here, 1053 in duchy-of-aquitaine) needs one decision for both dossiers.
- Brittany's 1532 end agrees with kingdom-of-france (vassal 1491-1532, gain 1532), so the author's overlap worry is resolved once Brittany adds the 1491 vassal_start.
- Written dossiers outside this batch with missing mirrors: kingdom-of-france (Brittany 1378-1379 contest, 1488-1491 occupation; Anjou 1328 dated 1322), west-franks (Normandy 942-946 occupation, Gascony 864), kingdom-of-the-franks (Gascony 793, 806), duchy-of-aquitaine (Saintonge 1062; Gascony 1053 vs 1058), kingdom-of-pamplona (824 found counterpart).
