# Review of batch eu-12-f (2026-10-31)

Adversarial review of six dossiers by the Phase B reviewer. The machine copy is history/notes/phase-b/reviews/eu-12-f.json. All six validate (with --resolve: 0 errors, 0 warnings). None of the six Wikipedia articles has an infobox area. Spot checks: every event opened on its page said what its note claims, with the year. No fabrication found.

## Verdicts

### taifa-of-toledo: fix
- FIX (applied by reviewer) `/ledger/9/region`: The 1085 dissolve handed Castile the whole 1084 shape, including the Valencia cells that /ledger/8 had already given back to taifa-of-valencia in 1085. Evidence: /ledger/8 (1085 loss of Valencia) and keyframe taifa-of-toledo_1085 (minus Toledo 1084, Valencia 1085) already take Valencia out. The Taifa of Valencia page says 'Valencia began to slip from Toledo's control' and that Alfonso VI 'installed al-Qadir in Valencia as his vassal in 1086'. Fix: Region set to {minus:[Toledo 1084, Valencia 1085]}, the same as the keyframe correction. Re-validated: 0 errors, 0 warnings.
- THIN `/ledger/8`: The date Valencia left Toledo's control (1075-1085). The 1085 loss is a confidence-1 bridge. Try: https://es.wikipedia.org/wiki/Taifa_de_Valencia
- THIN `/ledger/0`: caliphate-of-cordoba loses Toledo in 1010 (confidence 1) but the Toledo page says 1018. The caliphate dossier should be aligned to 1018. Try: https://en.wikipedia.org/wiki/Taifa_of_Toledo
- Spot checks: /ledger/0 confirmed; /ledger/4 confirmed; /ledger/6 confirmed; /ledger/9 confirmed; /ledger/3 confirmed
- Area: No area in the infobox (re-read). The page's maximum-extent provinces (Toledo, Ciudad Real, Cuenca, northern Albacete, Cáceres, Guadalajara, Madrid) total about 100,000 km2, against 90,230 km2 for the 1066-1084 Cliopatria shape: a ratio of about 1.1. The author compared the same list.

### taifa-of-tortosa: pass
- THIN `/keyframe_review/2-4`: The shrinks from 8,034 to 6,768 km2 (1040, 1046, 1056: 4 to 5 cells on the western edge) have no event. The page is silent, so they are thin by design within the 5-page budget. Try: https://es.wikipedia.org/wiki/Taifa_de_Tortosa
- THIN `/ledger/5`: The real end and the Almoravid takeover. The sources disagree: the page has 1099, the ruler list runs to c.1115, and the Taifa overview has '1081/1082-1092 (to Denia)'. No campaign is known, and almoravid-dynasty has no Tortosa event. Try: https://es.wikipedia.org/wiki/Taifa_de_Tortosa
- Spot checks: /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed; /ledger/5 confirmed
- Area: No area in the infobox (re-read). The author says so.

### taifa-of-valencia: fix
- FIX (applied by reviewer) `/keyframe_review/11/verdict`: The 1241-1249 shape was marked 'adjust', but its correction says the cells are 'not this state's'. In the schema that is 'wrong': the shape should not be used for these years. Evidence: Taifa of Valencia page: 'The city surrendered to James I's forces on 29 September 1238'. The state ends in 1238-09, before the shape begins. Fix: Verdict set to 'wrong' and the correction text kept. Re-validated: 0 errors, 0 warnings. Keyframe counts are now ok 3, adjust 7, wrong 2 (the author's report says 3/8/1).
- THIN `/ledger/6`: The date Valencia slipped from Toledo (between 1075 and 1086). The 1085 gain is a confidence-1 bridge. Try: https://es.wikipedia.org/wiki/Taifa_de_Valencia
- THIN `/ledger (1232-1235)`: Who held Morella, Borriana and Peñíscola before James I took them in 1232-1233. crown-of-aragon gains 1236 land from taifa-of-valencia (confidence 1) that this dossier does not lose. Try: https://en.wikipedia.org/wiki/James_I_of_Aragon
- Spot checks: /ledger/5 confirmed; /ledger/9 confirmed; /ledger/10 confirmed; /ledger/11 confirmed; /ledger/14 confirmed ('occupying nearby Puig in 1236'); /ledger/16 confirmed; /ledger/1 confirmed
- Area: No area in the infobox (re-read). The 53,704 km2 shape of 1147-1151 is marked wrong and explained.

### kingdom-of-aragon: fail
- FIX (author) `/ledger (between /ledger/5 and /ledger/6)`: The conquest of Huesca (1096) is missing, although the dossier moves its capital there in 1096 (/ledger/6, identity.capitals). Evidence: Kingdom of Aragon page: 'the capital city moved from Jaca to Huesca (1096)', infobox 'Huesca (1096–1118)'. taifa-of-zaragoza /ledger/9 has a 1096-11 loss to kingdom-of-aragon (Zaragoza 1085 minus 1099). The 10 cells that Cliopatria's Aragon shape gains in 1099 lie at 42.0-42.4 N, 0.28-1.05 W (the Huesca plain towards Ayerbe and Almudévar). None is near Barbastro (0.13 E), which is already in the 1046 shape. Fix: Add a 1096 (month 11) gain from taifa-of-zaragoza. Region: Huesca plus the 1099-minus-1085 cells, e.g. {union:[{place:Huesca,km:20},{minus:[Aragon 1099, Aragon 1085]}]}. Source: open Battle_of_Alcoraz or Peter_I_of_Aragon_and_Navarre for the date. Add the siege of Huesca (1094-1096) as a war.
- FIX (author) `/keyframe_review/3/correction and /ledger/3/region`: The 1085 shape, drawn from 1076, and the 1076 gain from Pamplona include the Huesca cell (42.17 N, 0.41 W) twenty years before Huesca fell. Evidence: Sancho Ramírez page: 'He perished in 1094 at the battle of Huesca'. Kingdom page: capital moved to Huesca in 1096. Grid check: the Huesca cell is absent from the 1046 shape and present from the 1085 shape on. Fix: For 1076-1095, use the 1085 shape minus Huesca ({place:Huesca,km:20} or that cell). Remove the same area from the /ledger/3 region and let the new 1096 gain add it.
- FIX (author) `/keyframe_review/2/correction and /ledger/1/region`: The 1046 shape, drawn from 1043, and the 1043 Sobrarbe-Ribagorza gain already contain 7 cells south of 42.25 N around Barbastro (42.09 N 0.11 E) and Graus (42.23-42.25 N, 0.18-0.37 E). Yet the ledger gains Graus only in 1083 (/ledger/4) and Barbastro only in 1100 (/ledger/7). Those two gains therefore add land the keyframes already hold, and the land is drawn 40-57 years early. Evidence: Ramiro I page: 'Ramiro died at the Battle of Graus in 1063 while trying to take the city'. Sancho Ramírez page: 'Graus in 1083'. Lérida page: 'In 1100, Peter ... captured Barbastro ... and Sariñena'. Fix: For 1043-1082, set the KF2 correction to the 1046 shape minus the Graus-Barbastro cells (e.g. minus [{place:Graus,km:15},{place:Barbastro,km:25}]), and remove the same from the /ledger/1 region. Do the same for the KF3 correction. Then the 1083 and 1100 gains add them back. Check that the 1099 and 1111 shapes agree.
- FIX (author) `/keyframe_review/4/note and /ledger/7/note`: The note says the 1099 shape's 10 new cells are the 1100 Barbastro capture. They are not: they lie west of Huesca (see the first finding). Evidence: Grid comparison of Cliopatria kingdom-of-aragon 1099 against 1085. Fix: Rewrite both notes. The 1099 growth is the Huesca conquest of 1096. Barbastro and Sariñena (1100) belong to the cut-back cells of the third finding.
- FIX (author) `/ledger/10/counterpart`: Tudela's counterpart is the free text 'Muslim holders of Tudela'. /ledger/11 (Calatayud 1120, same campaign, same page silence) uses almoravid-dynasty. Evidence: almoravid-dynasty /ledger/25 holds the Taifa of Zaragoza from 1110-05. Alfonso I page: Tudela is 'named among his conquests without a date'. Fix: Use counterpart almoravid-dynasty. Not blocking.
- FIX (author) `/identity/rulers/2/to`: Peter I is given to 1103, but Alfonso I starts in 1104 and the dossier's own notes say 'Peter I (1094-1104)'. Evidence: Internal inconsistency. No page opened gives Peter I's death year. Fix: Open Peter_I_of_Aragon_and_Navarre and set to 1104 if confirmed. Not blocking.
- THIN `/ledger/12`: When Alfonso I acquired his Castilian possessions and how far they reached. The page says he used the imperial title from his 1109 marriage and lost the lands in 1127; the dossier dates the gain 1126 at confidence 1. Try: https://en.wikipedia.org/wiki/Urraca_of_Le%C3%B3n_and_Castile
- THIN `/ledger/2`: The year of Tafalla and Sangüesa (confidence 1; the page has only 1036-1043). Try: https://es.wikipedia.org/wiki/Ramiro_I_de_Arag%C3%B3n
- THIN `/ledger/10`: The year Tudela was taken (confidence 1, bridged to 1119). Try: https://es.wikipedia.org/wiki/Tudela
- THIN `/ledger (1064-1065)`: Barbastro was taken in 1064 (Sancho Ramírez page) and lost in 1065. It is not in the ledger. Try: https://en.wikipedia.org/wiki/Siege_of_Barbastro
- THIN `/wars`: The 1146 Tauste contest that kingdom-of-navarre records against Aragon. It is not in this dossier. Try: https://en.wikipedia.org/wiki/Kingdom_of_Navarre
- Spot checks: /ledger/1 confirmed ('In 1043, apparently with the approval of García, he annexed Sobrarbe and Ribagorza'); /ledger/2 confirmed (no year, as the note says); /ledger/3 confirmed; /ledger/5 confirmed ('Monzón in 1089'); /ledger/8 confirmed; /ledger/13 confirmed; /ledger/4 confirmed; /ledger/7 confirmed for the year; the land attribution is wrong (see fixes); /ledger/11 confirmed; /ledger/14 confirmed
- Area: No area in the infobox (re-read: no Area or Population field). The author says so.

### taifa-of-albarracin: pass
- THIN `/ledger`: Thin by design (5 one-cell variants of an 8,800 km2 shape, 3 pages, 2 titles failed): no event is recorded between 1012 and 1104 (relations with Zaragoza, Valencia, El Cid, Castile). Try: https://es.wikipedia.org/wiki/Taifa_de_Albarrac%C3%ADn
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/1 confirmed ('Albarracín: 1011–1104 (to Almoravids)')
- Area: No area in the infobox (re-read). The author says so.

### taifa-of-almeria: thin
- THIN `/ledger/5`: The date and the land of the Seville campaigns that took the 16 north-eastern cells (14,798 to 10,927 km2, -26%). The confidence-1 bridge sits at Cliopatria's 1085. The page says only 'several campaigns of the Taifa of Seville diminished its territory in the north'. taifa-of-seville has no matching gain. Try: https://es.wikipedia.org/wiki/Taifa_de_Almer%C3%ADa
- THIN `/ledger/7`: The second taifa of 1145-1147 rests only on the Taifa overview list ('Almería: 1145–1147 (briefly to Castile and then to Almohads)'). Its ruler and extent are unknown. Try: https://en.wikipedia.org/wiki/Al-Mu%27tamid_ibn_Abbad
- Spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/4 confirmed; /ledger/6 confirmed; /ledger/8 confirmed (17 October 1147); /ledger/7 confirmed
- Area: No area in the infobox (re-read). The author says so.

## Cross-dossier mismatches and missing mirrors (route to the owners)

- mismatch: taifa-of-toledo 1018 found (caliphate-of-cordoba). The caliphate loses Toledo in 1010 (confidence 1). The Toledo page says 'In 1018, Ismail expelled the governor'. The caliphate dossier should move this to 1018.
- missing: taifa-of-toledo 1080 loss (taifa-of-badajoz). taifa-of-badajoz (eu-12, exists) has no 1080 gain of Toledo (infobox 'incorporated to the taifa of Badajoz: 1080–1081').
- missing: taifa-of-toledo 1081 gain (taifa-of-badajoz). taifa-of-badajoz has no 1081 loss of Toledo.
- mismatch: taifa-of-toledo 1085 dissolve (kingdom-of-castile). The years agree (1085-05). The land does not: Castile's gain region is Cliopatria's Toledo 1085 shape (47,127 km2, south of 40.36 N), which the Toledo dossier calls unsupported. Toledo hands over the 1084 shape minus Valencia (about 78,000 km2). Castile should use {minus:[Toledo 1084, Valencia 1085]}.
- mismatch: taifa-of-lerida 1081 vassal_start (taifa-of-tortosa). The two dossiers model the same man differently. Lérida draws Tortosa as its vassal 1081-1090, with al-Mundhir as hājib. Tortosa draws an independent taifa under that same al-Mundhir, who per the Lérida page 'inherited Lérida also'. The orchestrator should pick one model.
- missing: taifa-of-tortosa 1092 loss (almoravid-dynasty). almoravid-dynasty (af-02, exists) has no 1092 gain of Dénia/Tortosa land (Dénia infobox 'Almoravids: 1092–1224').
- missing: taifa-of-tortosa 1099 dissolve (almoravid-dynasty). almoravid-dynasty has no Tortosa gain (1099 per the Tortosa page).
- missing: kingdom-of-castile 1086 vassal_start (taifa-of-valencia). Castile has no vassal_start for al-Qadir's Valencia, 1086-1092 (Valencia page: 'installed al-Qadir in Valencia as his vassal in 1086'). The author flagged it.
- mismatch: kingdom-of-castile 1099 gain (taifa-of-valencia). Double claim for 1099-1102. Castile gains Valencia/Castellón from taifa-of-valencia in 1099 and loses it to the Almoravids in 1102-04. The Valencia dossier keeps Valencia under Jimena to the April-May 1102 evacuation (page: Jimena took charge; evacuated 'with the help of Alfonso VI') and has no 1099 loss. One side must change: Castile should drop the 1099 gain and the 1102 loss, or the two should agree on a vassal relation.
- mismatch: crown-of-aragon 1236 gain (taifa-of-valencia). Crown gains land from Valencia in 1236 (confidence 1). Valencia has only a contest_start at Puig. The northern conquests of 1232-1235 have no holder on either side.
- mismatch: crown-of-aragon 1241 gain (taifa-of-valencia). The counterpart ended 1238-09. The Crown's 1241 and 1244 gains from taifa-of-valencia should name another holder (the Valencia KF11 cells are now marked wrong).
- mismatch: kingdom-of-aragon 1043 gain (county-of-ribagorza). Two years apart. The Ramiro I page has 'In 1043 ... he annexed Sobrarbe and Ribagorza'. county-of-ribagorza (eu-12) has its loss and dissolve in 1045 and should re-check against that page.
- missing: kingdom-of-aragon 1043 gain (kingdom-of-pamplona). Sangüesa (confidence 1). kingdom-of-pamplona has no loss.
- mismatch: kingdom-of-aragon 1089 gain (taifa-of-lerida). Monzón. The Sancho Ramírez page has 'Monzón in 1089'. The Lérida page has 'between 1087 and 1093' and the Lérida dossier uses 1093. Lérida should move to 1089.
- missing: taifa-of-zaragoza 1096 loss (kingdom-of-aragon). Huesca, 1096-11. The Aragon dossier has no gain (blocking finding on kingdom-of-aragon).
- exception: kingdom-of-aragon 1119 gain (Muslim holders of Tudela (the page names none)). The counterpart is free text. It should be almoravid-dynasty (holder of the Zaragoza taifa from 1110), and the Almoravid dossier then needs the loss.
- exception: kingdom-of-aragon 1119 gain (holders of the Soria towns (the page names none)). Repopulation ('populated the region of Soria'). 'nobody' would fit better.
- missing: kingdom-of-aragon 1120 gain (almoravid-dynasty). almoravid-dynasty has no 1120 loss of Calatayud and Daroca.
- missing: kingdom-of-aragon 1126 gain (kingdom-of-castile). Confidence 1. kingdom-of-castile has no loss to Aragon. The Alfonso I page dates the imperial title, and so the Castilian holdings, from 1109.
- missing: kingdom-of-aragon 1127 loss (kingdom-of-castile). Alfonso I page: 'In 1127 ... lost all his Castilian possessions'. kingdom-of-castile has no 1127 gain.
- missing: kingdom-of-navarre 1146 contest_start (kingdom-of-aragon). Tauste. The Aragon dossier has no contest.
- missing: taifa-of-albarracin 1104 dissolve (almoravid-dynasty). almoravid-dynasty has no 1104 gain of Albarracín.
- missing: taifa-of-almeria 1085 loss (taifa-of-seville). Confidence-1 bridge. taifa-of-seville has no gain of Almería's north.
- mismatch: taifa-of-almeria 1147 dissolve (kingdom-of-castile). The dates agree (1147-10). Castile names its counterpart 'Almería's Muslim holders (the page names none)'; it should be taifa-of-almeria.

## What I tried and could not break

- Toledo: the 1018, 1075, 1080 and 6 May 1085 dates and the Valencia annexation (1064 on the Toledo page, 1065 on the Valencia page). Córdoba 1075-1077 matches Seville within a year.
- Tortosa: 1060 to Zaragoza, 1081 restoration, the Dénia lands 1081-1092 (Dénia infobox) and the 1099 end are all on the pages.
- Valencia: 1065, Almenara 1097, the April-May 1102 evacuation, March 1145, Puig 1236 and 29 September 1238 are on the page. The Almería and Murcia transfers mirror exactly.
- Albarracín: 1012-1104 on the page. Thin by design.
- Almería: 1012, 1038-1041, 1091 and 17 October 1147 are confirmed. The 1236 and 1241 rows are rightly rejected (the shapes lie in the Jaén uplands).
