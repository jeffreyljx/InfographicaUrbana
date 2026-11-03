# Review of batch eu-13-e (Naples, Capua, Salerno, Emirate of Sicily, Arborea)

Reviewer, 2026-10-25. The validator passes all five dossiers (with --resolve; warnings are gazetteer misses only). Spot checks were made with WebFetch on the pages each event cites. Fixes marked applied were made by the reviewer in the dossier, re-validated, and carry a '[Reviewer eu-13-e, 2026-10-25: ...]' note.

| slug | verdict |
| --- | --- |
| duchy-of-naples | fix |
| principality-of-capua | fail |
| principality-of-salerno | fix |
| emirate-of-sicily | thin |
| giudicato-of-arborea | fix |

## duchy-of-naples: fix

Findings:
- `/ledger/5/counterpart and /ledger/6/counterpart` (applied by reviewer). The 1135-1139 contest names norman-italy, which no longer existed: the norman-italy dossier ends in December 1130 when Roger II was crowned and hands over to kingdom-of-sicily. Evidence: norman-italy.json ledger L27 '1130/12 dissolve' (successor kingdom-of-sicily); Sergius VII page: Naples rose on 24 April 1135 against Roger and 'Roger II incorporated the Duchy of Naples into his kingdom in 1139'. Fix: counterpart 'kingdom-of-sicily' on both events (pairing kept); reviewer note appended.

Gaps for a gap-filler:
- `/keyframe_review/2, /keyframe_review/3, /keyframe_review/7`: Cliopatria's 960 cut (1,059 to 770 km2), 980-989 bump (+96 km2) and 1085 trim (-24 km2) are unexplained (unverified: page budget, 5 of 5 pages used). Try: https://en.wikipedia.org/wiki/Duchy_of_Amalfi
- `/keyframe_review/0`: Early extent: Gaeta, Amalfi and Sorrento 'took their independence' in the early 9th century, undated; the 763-839 shape may include them. Try: https://en.wikipedia.org/wiki/Duchy_of_Gaeta
- `/identity/capitals/0`: Capital Naples at 14.25 E lies about 1 km west of the 1034-1138 shapes' bbox edge (14.263 E); check whether the corrected shape should keep the whole city (union with place Naples, small radius). Try: https://en.wikipedia.org/wiki/Naples

Spot checks: `/ledger/0` confirmed (Duchy_of_Naples); `/ledger/3` confirmed (Pandulf_IV_of_Capua); `/ledger/4` confirmed (County_of_Aversa); `/ledger/7` confirmed (Sergius_VII_of_Naples).
Area: No area in the Duchy of Naples infobox (checked); the author says so in notes. Largest Cliopatria shape 1058.8 km2.

## principality-of-capua: fail

Findings:
- `/identity/end, /identity/successors, /ledger/9, /ledger/10` (NOT applied: author to do). The state is dissolved in 1058 into norman-italy, but its own page and the neighbour dossier continue the principality under its Norman princes, leaving Capua and Aversa with no owner after 1058. Evidence: Principality of Capua page: infobox rulers 'Atenulf I (887-910)' to 'Robert II (1127-1156)', events '1058 Richard of Aversa conquers Capua', '1127 Roger II claims overlordship', end 1139 in the body / 1156 in the infobox; Landulf VIII 'recorded as prince until 12 May 1062' (Norman conquest page). norman-italy.json L6 '1058 loss cp=principality-of-capua: Aversa and Capua ... are the Principality of Capua's'. Rule 2 of the brief: a dynasty that replaces another on the same land stays in the dossier as a rename. Fix: Extend the dossier through the Norman principality: 1058 rename (Drengot princes), 1058 gain of Aversa from norman-italy (mirror of its L6), 1058-1062 contest with Landulf VIII if drawn, end at 1139 (Roger II takes the title; or 1156, say which) with successor kingdom-of-sicily; review Cliopatria's 1056-1065 shape for 1058-1065 and add keyframes to the end. If the orchestrator rules Norman Capua into norman-italy instead, norman-italy's L6 must change; either way one of the two must move.
- `/keyframe_review/0,1,2,3,4,5,6,8,11,12 (the single-cell shapes) and /identity/capitals/0` (NOT applied: author to do). The capital Capua (14.21 E, 41.11 N) lies outside every single-cell Capua shape: the Cliopatria cell's bbox is 13.79-14.11 E, about 8 km west of the city; unflagged. Evidence: shapes.csv: principality-of-capua_840/875/990/1015 bbox '13.7918,41.068,14.112,41.2625'; only the 1028 and 1034 shapes reach east of 14.21 E. Capua sits at about 41.10 N 14.22 E. Fix: Correct each single-cell keyframe to union[{cliopatria Capua <year>}, {place: Capua, km: 10-15}] with text saying the city lies east of Cliopatria's cell, or explain why the cell stands.
- `/ledger/6/region, /ledger/7, /keyframe_review/10/note` (NOT applied: author to do). Gaeta is lost twice: the May 1038 loss gives away Cliopatria's 1034 shape, which carries the Gaeta cells (K9), and L7 loses Gaeta again in June 1040, while K10 says Capua has no land 1038-1046. Evidence: Guaimar IV page: 'In June 1040, he took Gaeta, which had been conquered by Pandulf in 1032', so Gaeta was not part of the 1038 grant. The Salerno dossier's 1038 gain now (reviewer fix) excludes Gaeta. Fix: L6 region = minus[{cliopatria Principality of Capua 1034}, {place Gaeta, km 15}] (matching principality-of-salerno L9); keep Gaeta with Capua 1038-1040 in a new keyframe (place Gaeta) ending with L7, or recast L7, and amend K10's note.

Gaps for a gap-filler:
- `/ledger (1034)`: Sorrento, 'conquered by Pandulf in 1034' (Guaimar IV page) and taken by Guaimar in July 1039, is not in the ledger; the republic-of-amalfi dossier also puts Amalfi under Capua 1034-1039 (occupation), which this dossier lacks. Try: https://en.wikipedia.org/wiki/Duchy_of_Sorrento
- `/keyframe_review/3, /keyframe_review/5`: The 900-989 and 1010-1014 keyframes draw Capua separately while Cliopatria's Benevento shapes of those years (+336 km2) contain the Capua cell and the Benevento dossier gains Capua in 899 and 1010; one of the two must give way (orchestrator decision). Try: https://en.wikipedia.org/wiki/Pandulf_Ironhead

Spot checks: `/ledger/0` confirmed (Principality_of_Capua); `/ledger/4` confirmed (Pandulf_IV_of_Capua); `/ledger/5` confirmed (Pandulf_IV_of_Capua); `/ledger/6` confirmed (year on the Pandulf page, May on the Guaimar page) (Guaimar_IV_of_Salerno); `/ledger/9` confirmed as a conquest, but the page continues the principality to 1139/1156 (Principality_of_Capua).
Area: No area in the infobox (checked). Largest Cliopatria shape 1154.1 km2.

## principality-of-salerno: fix

Findings:
- `/ledger/9/region and /keyframe_review/7/correction` (applied by reviewer). The May 1038 gain and the 1038-1046 keyframe used Cliopatria's 1034 Capua shape, which carries the Gaeta cells, so Gaeta was drawn as Salerno's for 1038-1046 although the keyframe note says it is not drawn and L12/L13 date the hold June 1040 to October 1041. Evidence: Guaimar IV page: 'In June 1040, he took Gaeta, which had been conquered by Pandulf in 1032'; after October 1041 Guaimar stops appearing in Gaeta's records. Capua K9: 'Cliopatria's 1034 shape adds two cells on the Gaeta coast'. Fix: Capua part = minus[{cliopatria Principality of Capua 1034}, {place Gaeta, km 15, country Italy}] in both places; reviewer notes appended.
- `/ledger/5/confidence` (applied by reviewer). The c. 968 loss to the Byzantines was at confidence 2, but the cited page does not make the land Salerno's. Evidence: Theme of Lucania page: 'established probably c. 968', 'was formed to encompass Lombard-populated areas of the theme of Longobardia'; Salerno is not named; the region is Cliopatria's 970 cut. Fix: confidence 1; note appended.

Gaps for a gap-filler:
- `/ledger/5`: Who held the Basilicata and Cosenza interior before c. 968 (Salerno or Byzantine Longobardia), and when Cosenza was lost. Try: https://en.wikipedia.org/wiki/Longobardia
- `/ledger/17`: End of Guaimar's 1040 hold on Benevento (confidence 1, placed at 1047). Try: https://en.wikipedia.org/wiki/Pandulf_III_of_Benevento
- `/ledger (1039)`: Sorrento, taken by Guaimar in July 1039 and given to his brother Guy (Guaimar IV page), is not in the ledger or the 1038-1046 keyframe. Try: https://en.wikipedia.org/wiki/Guaimar_IV_of_Salerno
- `/keyframe_review/0`: 840-850 extent: the dossier draws 40 km round Salerno, while the Benevento dossier gives Salerno 'mostly the western half of the old duchy' from 840 (its L6); the land between is nobody's. Try: https://en.wikipedia.org/wiki/Siconulf_of_Salerno
- `/keyframe_review/5`: 978-983: neighbours record Salerno as gained by Benevento (978-981) and occupied by Amalfi (981-983); this dossier draws it as Salerno under foreign princes (rename). Orchestrator to choose one model. Try: https://en.wikipedia.org/wiki/Pandulf_Ironhead

Spot checks: `/ledger/3` confirmed (Principality_of_Salerno); `/ledger/5` not on page as a loss of Salerno (the note said so); confidence lowered to 1 (Theme_of_Lucania); `/ledger/10` confirmed (Guaimar_IV_of_Salerno); `/ledger/11` confirmed (Principality_of_Benevento); `/ledger/19` confirmed (Norman_conquest_of_southern_Italy); `/ledger/20` confirmed (Norman_conquest_of_southern_Italy).
Area: No area in the infobox (checked). Largest Cliopatria shape 17791.0 km2.

## emirate-of-sicily: thin

Gaps for a gap-filler:
- `/wars/1/zones`: The Maniakes war is drawn with no zone and 'no territorial result', but the Emirate page says he 'managed to snatch Messina and Syracuse from Arab rule' for 'a very short time' and that 'the subsequent Muslim counter-offensive reconquered all the cities'; add the zone (Messina, Syracuse) and a contest_start 1038 / contest_end pair with byzantine-empire (end year from the Maniakes page). Try: https://en.wikipedia.org/wiki/George_Maniakes
- `/ledger/25`: Interior collapse placed at 1085 at confidence 1; the Norman conquest page does date some of it: 'In 1079 Taormina was besieged', Trapani 'soon surrendered', 'in 1081 Jordan ... conquered Catania'. Agrigento, Castrogiovanni (Enna) and Butera need a page. Try: https://en.wikipedia.org/wiki/Roger_I_of_Sicily
- `/keyframe_review/11, /keyframe_review/12`: Cliopatria's 1066 and 1072 shapes stop at 15.21 E and so exclude Taormina (15.29 E), which the Norman conquest page has still besieged in 1079; correct to keep Taormina to 1079. Try: https://en.wikipedia.org/wiki/Norman_conquest_of_southern_Italy
- `/ledger/2`: Agrigento at confidence 1: the Muslim conquest page places it in the 828 campaign ('one part of the army took Agrigento after Mineo surrendered'), which supports confidence 2. Try: https://en.wikipedia.org/wiki/Muslim_conquest_of_Sicily
- `/identity`: The Aghlabid mainland emirates (Bari 847-871, Taranto) and the Ibn Qurhub revolt of 912-917 (the Fatimid dossier has a contest with this state) are not covered. Try: https://en.wikipedia.org/wiki/Emirate_of_Bari

Spot checks: `/ledger/11` confirmed (Muslim_conquest_of_Sicily); `/ledger/14` confirmed (Muslim_conquest_of_Sicily); `/ledger/24` confirmed (Emirate_of_Sicily); `/ledger/27` confirmed (Norman_conquest_of_southern_Italy); `/ledger/13` confirmed (Muslim_conquest_of_Sicily); `/ledger/23` confirmed (Emirate_of_Sicily).
Area: No area in the infobox (checked); the 878 shape is close to the island's 25,700 km2. Largest Cliopatria shape 22527.6 km2.

## giudicato-of-arborea: fix

Findings:
- `/ledger/1/type and /ledger/2/type` (applied by reviewer). Mujahid's 1015-1016 landing was recorded as loss and gain, while the page describes a one-year occupation and the Cagliari, Logudoro and Gallura dossiers record the same events as occupation_start/occupation_end with taifa-of-denia. Evidence: Mujahid al-Amiri page: 'He landed with 120 ships and occupied the southern coastal plain'; 'In May 1016 ... Mujahid, facing mutiny among his men, fled by sea'; no annexation described. Fix: types occupation_start (1015) and occupation_end (May 1016), counterpart taifa-of-denia kept; reviewer notes appended.

Gaps for a gap-filler:
- `/ledger/0`: Start 866 at confidence 1 (infobox: 'Established: 11th century'); the same Cliopatria date is used by the Cagliari, Gallura and Logudoro dossiers, so one group decision is needed. Try: https://en.wikipedia.org/wiki/Judicates
- `/keyframe_review/5`: Arborea's share of Cagliari in 1258 and of Logudoro after 1259: both neighbours list Arborea as a successor but no gain is in this ledger (pages silent on extent). Try: https://en.wikipedia.org/wiki/William_of_Capraia
- `/keyframe_review/6`: Cliopatria's 1326-1343 shape adds 290 km2; no event explains it. Try: https://en.wikipedia.org/wiki/Hugh_II_of_Arborea
- `/wars/2`: The war runs from 1353 but the first contest_start is 1368; the crown-of-aragon dossier opens its contest in 1353 (Marianus IV's break, Alghero 1353-1354). Try: https://en.wikipedia.org/wiki/Marianus_IV_of_Arborea
- `/keyframe_review/10`: 1388-1390 extent after the peace (the pre-1368 core is the researcher's reading). Try: https://en.wikipedia.org/wiki/Eleanor_of_Arborea

Spot checks: `/ledger/3` confirmed (Judicate_of_Arborea); `/ledger/7` confirmed (Aragonese_conquest_of_Sardinia); `/ledger/10` confirmed (Aragonese_conquest_of_Sardinia); `/ledger/12` confirmed (Judicate_of_Arborea); `/ledger/14` confirmed (Judicate_of_Arborea); `/ledger/8` confirmed (Aragonese_conquest_of_Sardinia).
Area: No area in the infobox (checked); the 26,138 km2 maximum is the whole-island shape the author marks wrong. Largest Cliopatria shape 26138.0 km2.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| duchy-of-naples 763 found (byzantine-empire) | byzantine-empire - - | missing | Byzantine dossier has no 763 event for Naples (papal suzerainty). |
| duchy-of-naples 1027 loss (principality-of-capua) | principality-of-capua 1027 gain | matched |  |
| duchy-of-naples 1029 gain (principality-of-capua) | principality-of-capua 1029 loss | matched |  |
| duchy-of-naples 1030 loss (norman-italy) | norman-italy 1030 found | matched | norman-italy is founded on Aversa from Naples. |
| duchy-of-naples 1135 contest_start (kingdom-of-sicily) | kingdom-of-sicily - - | exception | kingdom-of-sicily (eu-13) not written yet; counterpart changed from norman-italy by the reviewer. |
| duchy-of-naples 1139 loss (kingdom-of-sicily) | kingdom-of-sicily - - | exception | kingdom-of-sicily not written yet. |
| principality-of-capua 861 found (principality-of-salerno) | principality-of-salerno 861 loss | matched |  |
| principality-of-capua 1032 gain (Duchy of Gaeta) | duchy-of-gaeta - - | exception | listed under counterparts_needing_dossiers. |
| principality-of-capua 1038 loss (principality-of-salerno) | principality-of-salerno 1038 gain | mismatch | Same year and parties; land now differs: Salerno (reviewer fix) excludes Gaeta, Capua still gives the whole 1034 shape. |
| norman-italy 1038 gain (principality-of-capua) | principality-of-capua 1038 loss | mismatch | norman-italy L1 has Ranulf gaining Capua in 1038 (confidence 2); Capua and Salerno both give Capua to Guaimar IV of Salerno in May 1038. norman-italy should drop or recast it. |
| principality-of-capua 1040 loss (principality-of-salerno) | principality-of-salerno 1040 gain | mismatch | Capua says it lost Gaeta to Salerno; Salerno says it took Gaeta from the Duchy of Gaeta. |
| principality-of-capua 1047 gain (principality-of-salerno) | principality-of-salerno 1047 loss | matched |  |
| principality-of-capua 1058 dissolve (norman-italy) | norman-italy 1058 loss | mismatch | Opposite directions: Capua dissolves into norman-italy, norman-italy L6 hands Aversa and Capua to principality-of-capua. Capua and Aversa have no owner after 1058. See Capua fix 1. |
| duchy-of-benevento 899 gain (principality-of-capua) | principality-of-capua - - | mismatch | Benevento gains Capua in 899 (and again 1010, losses 990 and 1015, all confidence 1); Capua draws itself separately 900-989 and 1010-1014 (personal union, not drawn). Double drawing; orchestrator to choose. |
| duchy-of-benevento 1034 loss (principality-of-capua) | principality-of-capua - - | missing | Benevento loses its western edge to Capua in 1034 (confidence 1); Capua explains its 1034 growth by Gaeta (1032) only. |
| republic-of-amalfi 1034 occupation_start (principality-of-capua) | principality-of-capua - - | missing | Amalfi dossier has Amalfi under Capua 1034-1039; Capua has no Amalfi event (its pages are silent). |
| principality-of-salerno 840 found (duchy-of-benevento) | duchy-of-benevento 840 loss | mismatch | Benevento loses the western half to Salerno in 840; Salerno takes only 40 km round Salerno until 851. Land between is unowned 840-850. |
| principality-of-salerno 840 contest_start (duchy-of-benevento) | duchy-of-benevento 840 contest_start | matched | contest_end 851 matched too. |
| principality-of-salerno 851 gain (duchy-of-benevento) | duchy-of-benevento 840 loss | mismatch | Year: Salerno 851, Benevento 840. |
| principality-of-salerno 968 loss (byzantine-empire) | byzantine-empire - - | missing | Byzantine dossier has no c. 968 Lucania gain (now confidence 1 on the Salerno side). |
| duchy-of-benevento 978 gain (principality-of-salerno) | principality-of-salerno 978 rename | mismatch | Benevento annexes Salerno 978-981; Salerno keeps its own keyframe 980-989 with renames. Double drawing 978-981. |
| republic-of-amalfi 981 occupation_start (principality-of-salerno) | principality-of-salerno 981 rename | mismatch | Amalfi occupies Salerno 981-983; Salerno records a rename. If occupation stands, Salerno should carry occupation_start/end 981/983 with republic-of-amalfi. |
| principality-of-salerno 1039 gain (republic-of-amalfi) | republic-of-amalfi 1039 occupation_start | mismatch | Type: Salerno annexes, Amalfi says occupied (and under Capua 1034-1039, not independent). |
| principality-of-salerno 1040 gain (duchy-of-benevento) | duchy-of-benevento 1040 contest_start | mismatch | Type: Salerno gain vs Benevento contest; end 1047 at confidence 1 on both sides. |
| principality-of-salerno 1040 gain (Duchy of Gaeta) | duchy-of-gaeta - - | exception | No dossier; listed. 1041 loss likewise. |
| principality-of-salerno 1043 vassal_start (norman-italy) | norman-italy - - | exception | Vassal events sit on the suzerain only (schema); vassal_end 1047 likewise. |
| principality-of-salerno 1052 loss (republic-of-amalfi) | republic-of-amalfi 1073 occupation_end | mismatch | 21 years apart: Guaimar IV page makes him Duke of Amalfi 1039-1052; the Amalfi dossier ends the Salerno occupation in 1073 at confidence 1. Amalfi should move to 1052. |
| principality-of-salerno 1077 loss (norman-italy) | norman-italy 1077 gain | matched | Salerno city 1076/12 and citadel 1077/5; norman-italy 1077. |
| emirate-of-sicily 827 found (byzantine-empire) | aghlabid-dynasty 827 contest_start | mismatch | The Aghlabid dossier, not the Emirate, holds the 827 war in the Byzantine and Aghlabid ledgers. |
| emirate-of-sicily 831 gain (byzantine-empire) | byzantine-empire 831 loss | mismatch | Byzantine loses Palermo to aghlabid-dynasty; the Aghlabid dossier also gains it (and Enna 859, Malta 870, Syracuse 878). Sicily is double-claimed 831-909 by aghlabid-dynasty and emirate-of-sicily; unflagged by the Emirate author. Orchestrator to choose (e.g. Aghlabid vassal_start over the Emirate). |
| emirate-of-sicily 859 gain (byzantine-empire) | byzantine-empire 859 loss | mismatch | Counterpart: Byzantine names aghlabid-dynasty. |
| emirate-of-sicily 870 gain (byzantine-empire) | byzantine-empire 870 loss | mismatch | Counterpart: Byzantine names aghlabid-dynasty. |
| emirate-of-sicily 878 gain (byzantine-empire) | byzantine-empire 878 loss | mismatch | Counterpart: Byzantine names aghlabid-dynasty. |
| emirate-of-sicily 902 gain (byzantine-empire) | byzantine-empire 902 loss | mismatch | Counterpart: Byzantine names aghlabid-dynasty. |
| emirate-of-sicily 843 gain (byzantine-empire) | byzantine-empire - - | missing | Messina 843, Modica 845, Lentini 846, Ragusa 848, Cefalu 857 and Agrigento 828 have no Byzantine mirror. |
| byzantine-empire 900 loss (aghlabid-dynasty) | emirate-of-sicily - - | mismatch | Byzantine loses Catania in 900 (confidence 3); the Muslim conquest page has only an unsuccessful siege of Catania in 900. Byzantine side to check. |
| fatimid-caliphate 909 gain (emirate-of-sicily) | emirate-of-sicily 909 rename | mismatch | Fatimid annexes Sicily 909-948; the Emirate draws itself 911-959 as its own state. Double drawing 909-948 (the Emirate author flagged the Cliopatria overlap). |
| fatimid-caliphate 912 contest_start (emirate-of-sicily) | emirate-of-sicily - - | missing | Fatimid contest 912-917 (Ibn Qurhub) has no Emirate side. |
| fatimid-caliphate 948 vassal_start (emirate-of-sicily) | emirate-of-sicily 948 rename | matched | Suzerain carries it, as the Emirate author asked; vassal_end 1044 (confidence 1) likewise. |
| emirate-of-sicily 965 contest_end (byzantine-empire) | byzantine-empire - - | missing |  |
| emirate-of-sicily 1061 loss (norman-italy) | norman-italy 1061 gain | matched | contest_start 1061/5 matched too. |
| emirate-of-sicily 1071 loss (norman-italy) | norman-italy - - | missing | Catania 1071 (Emirate page) has no norman-italy gain. |
| emirate-of-sicily 1072 loss (norman-italy) | norman-italy 1072 gain | matched |  |
| emirate-of-sicily 1085 loss (norman-italy) | norman-italy 1085 gain | matched | both confidence 1 |
| emirate-of-sicily 1086 loss (norman-italy) | norman-italy 1091 gain | mismatch | Syracuse: Emirate 1086/3 (page: capitulated March 1086); norman-italy takes it only with Noto in 1091/2. |
| emirate-of-sicily 1091 loss (norman-italy) | norman-italy 1091 gain | matched | Malta and Noto; contest_end and dissolve 1091/2 matched. |
| giudicato-of-arborea 866 found (byzantine-empire) | byzantine-empire 840 loss | mismatch | Byzantine loses Sardinia to nobody in 840 (confidence 1); the four judicates are founded from byzantine-empire in 866 (confidence 1). |
| giudicato-of-arborea 1015 occupation_start (taifa-of-denia) | taifa-of-denia 1015 occupation_start | missing | Denia records occupations of Logudoro and Gallura only, not Arborea or Cagliari. |
| giudicato-of-cagliari 1258 dissolve (republic-of-pisa) | giudicato-of-arborea - - | missing | Cagliari and Logudoro (1259) name Arborea as a successor; no gain in Arborea (pages silent on extent). |
| giudicato-of-arborea 1323 contest_start (republic-of-pisa) | republic-of-pisa - - | exception | republic-of-pisa (eu-13) not written yet; contest_end 1326 likewise. |
| giudicato-of-arborea 1323 vassal (Hugh II to James II) (crown-of-aragon) | crown-of-aragon - - | missing | Crown of Aragon has no vassal_start 1323 counterpart giudicato-of-arborea (the author asked for it). |
| crown-of-aragon 1353 contest_start (giudicato-of-arborea) | giudicato-of-arborea 1368 contest_start | mismatch | 15 years: Crown opens the contest in 1353, Arborea in 1368; Crown runs it unbroken to 1420, Arborea 1368-1388 and 1391-1410. |
| giudicato-of-arborea 1368 gain (crown-of-aragon) | crown-of-aragon 1368 loss | matched |  |
| giudicato-of-arborea 1388 loss (crown-of-aragon) | crown-of-aragon - - | missing | No Crown gain in 1388. |
| giudicato-of-arborea 1391 gain (crown-of-aragon) | crown-of-aragon - - | missing | No Crown loss in 1391. |
| giudicato-of-arborea 1410 loss (crown-of-aragon) | crown-of-aragon - - | missing | No Crown gain in 1410 (Oristano, the Marquisate of Oristano to Cubell). |
| giudicato-of-arborea 1420 loss (crown-of-aragon) | crown-of-aragon 1420 gain | matched | dissolve 1420/8 matched by the Crown gain. |

## For the orchestrator

- WebFetch returns a small-model digest; every spot check was read from the digest's quotations, not the raw page.
- Neighbours not written yet (owned by eu-13 parts that have not run or not finished): republic-of-pisa, republic-of-genoa, papal-states, kingdom-of-sicily, duchy-of-gaeta. Their mirrors are exceptions.
- fatimid-caliphate and zirid-dynasty are not in the author's Context list but were read as counterparts of the Emirate.
- Orchestrator decisions needed across groups: (1) Norman Capua 1058-1139: principality-of-capua or norman-italy (both dossiers now disclaim it); (2) Sicily 831-909 double-claimed by aghlabid-dynasty and emirate-of-sicily, 909-948 by fatimid-caliphate and emirate-of-sicily; (3) the Capua-Benevento personal unions (900-981, 1010-1014) drawn by both duchy-of-benevento and principality-of-capua; (4) Salerno 978-983 drawn by Salerno and claimed by Benevento and Amalfi.

Gazetteer names needed: Mazara del Vallo, Agrigento, Lentini, Taormina, Cefalù, Gaeta, Aversa, Alghero (and 'Oristano', spelled 'Oristrano' in admin1, per the author).
