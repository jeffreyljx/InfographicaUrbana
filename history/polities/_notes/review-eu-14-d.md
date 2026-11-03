# Review eu-14-d (2026-10-31): kingdom-of-denmark, jaemtland

Validator: both files pass with 0 errors, before and after the reviewer's edits. kingdom-of-denmark has one intended warning: keyframe 28 has an empty correction.

## kingdom-of-denmark: thin

The author kept to the 9-page budget. Every spot check came back confirmed: 17 events on 7 pages (Valdemar II, Valdemar IV, Cnut, History of Denmark, Canute VI, Sweyn Forkbeard, Sweyn II), including all the confidence-3 events that move the most land. I found nothing fabricated or mis-dated.
Area: the Danish Realm infobox gives 42,926 km2 for Denmark proper (modern, no year), against 57,037 km2 for the 936 core shape, a ratio of 1.33. The author acknowledges it.

### Fixes
- [applied] `/ledger/13/region`: The 1016 gain of 'all of England north of the Thames' was drawn as the whole of England. Evidence: Cnut page: 'all of England north of the Thames was to be the domain of the Danish prince'; the gazetteer has Mercia, Northumbria and East Anglia. Fix: Region set to union of Mercia, Northumbria and East Anglia with text 'all of England north of the Thames'.
- [applied] `/ledger/35/counterpart, /ledger/37/counterpart, /ledger/38/counterpart`: Counterpart was the free text 'mortgagees of the Danish crown lands', not a dossier, not nobody and not in counterparts_needing_dossiers. Evidence: Valdemar IV page: 'much of the kingdom had been pledged to Holstein nobles'; Vordingborg Castle was 'the main headquarters of the Holsteiners'. county-of-holstein exists. Fix: Counterpart set to county-of-holstein, with a reviewer line in each note.
- [open] `/ledger/35, /ledger/37, /ledger/38, /keyframe_review/22`: The gains of 1340, 1344 and 1346 take back land that no event and no keyframe ever removed. The 1332-1340 rule of the Holstein counts is missing, and /ledger/35 gains the whole 1352 shape in 1340. Evidence: History of Denmark: 'For eight years after Christopher's death, Denmark had no king, and was instead controlled by the counts'. Valdemar IV page: only 'the pawned province of Nørrejylland, one-quarter of the territory of Jutland' came back in 1340 (Helvig's dowry); North Friesland came back in 1344, Zealand in 1346, and the recovery was 'finally completed in 1360'. The notes for events 37 and 38 say 'the cells were inside Cliopatria's Danish shape all along'. county-of-holstein has no events for 1320-1350. Fix: Choose one of two. (a) Add 1332-8 occupation_start (or loss) events against county-of-holstein for the pledged provinces, adjust keyframe 22 to match, and pair each with occupation_end/gain events: 1340 Nørrejylland, 1344 North Friesland, 1346 Zealand, the rest by 1360. Narrow /ledger/35's region to Nørrejylland. (b) If the pledged provinces stay Danish land, drop the three gains and write the pledges in notes.
- [open] `/ledger (missing, 1227 and 1238)`: The Danish vassal tint on Estonia runs unbroken 1219-1346, but Estonia was lost in 1227 and returned in 1238. Evidence: danish-estonia /ledger/2 has a 1227 loss to livonian-brothers-of-the-sword ('In 1227, the Livonian Brothers of the Sword conquered all Danish territories in northern Estonia') and /ledger/3 has a 1238-6 gain (Treaty of Stensby, 7 June 1238), both at confidence 3. livonian-brothers-of-the-sword /ledger/9 has the 1227 gain with kingdom-of-denmark as counterpart. The author lists this as a gap. Fix: Add vassal_end danish-estonia 1227 and vassal_start danish-estonia 1238-6, sourced from https://en.wikipedia.org/wiki/Danish_Estonia.
- [open] `/ledger/12-16`: England stays Danish until 1018, but kingdom-of-england takes it back from Denmark in 1017. The two dossiers disagree on who draws England in 1017. Evidence: kingdom-of-england /ledger/22 has a 1017 gain with counterpart kingdom-of-denmark (Cnut crowned 'in London in 1017'). The Cnut page has Harald II as King of Denmark from 1014 until 'Harald II died in 1018', so Cnut's England was not part of Harald's Denmark. Fix: Add a 1017 loss of England to kingdom-of-england and make the 1018 loss to north-sea-empire Denmark only, or agree with eu-11 which side changes.
- [open] `/ledger/2, /keyframe_review/3`: The 970 shape draws all 119 Norwegian cells as direct Danish land for 970-994. old-kingdom-of-norway loses only Viken (77 cells), so 42 cells are drawn twice. Evidence: old-kingdom-of-norway /ledger/5: Haakon Sigurdsson ruled 'c. 970-995' Norway 'except Viken'. Harald Bluetooth page (as quoted in the dossier): rule in Norway lasted 'no more than a few years in the 970s'. Fix: Correct keyframe 3 to remove Norway outside the Viken counties that old-kingdom-of-norway uses. Carry Lade Norway as a vassal for the overlordship years, or leave it out.
- [open] `/ledger/21`: The 1185 vassal_start names duchy-of-pomerania, whose life starts in 1188. pomerania (1138-1187) instead dissolves into kingdom-of-denmark as direct land. Evidence: duchy-of-pomerania identity starts in 1188 and has no vassal events. pomerania /ledger/1: 1187 dissolve with counterpart kingdom-of-denmark ('Cliopatria folds Pomerania into the Danish realm'). Canute VI page: 'in 1185 forced Bogislaw to acknowledge Canute as his overlord'. Fix: Say in the event's note that the vassal is pomerania until 1187 and duchy-of-pomerania from 1188. Route to eu-15: pomerania needs a 1185 vassal_start and a dissolve to duchy-of-pomerania; duchy-of-pomerania needs vassal events for 1188-1227.
- [open] `/ledger/34, /ledger/41`: Halland is in Denmark's 1332 loss and 1360 gain but not in Sweden's matching events. Evidence: kingdom-of-sweden /ledger/11 (1332 gain) and /ledger/16-17 (1360 losses) cover Skåne and Blekinge only. Fix: Agree with kingdom-of-sweden on Halland, citing https://en.wikipedia.org/wiki/Magnus_IV_of_Sweden.
- [open] `/wars/11`: The Danish-Hanseatic war has empty zones, but the Treaty of Stralsund gave ground: the Scanian castles went to the Hansa. Evidence: Valdemar IV page: 'Valdemar was forced to sign the Treaty of Stralsund in 1370'. The author lists the Hanseatic hold on Scania as a gap. Fix: Add a Scania zone and a 1370-1385 occupation against hanseatic-league once that dossier exists.

### Gaps for a gap-filler
- `/ledger/1`: The 960 gain of Scania, Halland and Blekinge has confidence 1 and only Cliopatria's year. The Sweyn Forkbeard page credits Sweyn (from c. 986) with extending 'Danish control east of the strait of Øresund into Skane'. Page to try: https://en.wikipedia.org/wiki/History_of_Scania
- `/ledger/5`: The 986 move of the seat to Roskilde has no year on any page (confidence 1). The History of Denmark infobox also lists 'Lejre in Zealand'. Page to try: https://en.wikipedia.org/wiki/Roskilde
- `/ledger/10`: The 1015 end of the Norwegian overlordship (confidence 1). Page to try: https://en.wikipedia.org/wiki/Olaf_II_of_Norway
- `/ledger/22`: The 1185 Mecklenburg overlordship (confidence 1, 'the 1180s'). mecklenburg has no vassal events. Page to try: https://en.wikipedia.org/wiki/Borwin_I,_Lord_of_Mecklenburg
- `/ledger/34`: The 1332 loss of Scania to Sweden (confidence 1, year undated within the reign). Page to try: https://en.wikipedia.org/wiki/Magnus_IV_of_Sweden
- `/ledger/36, /ledger/40`: The 1344 split to and 1352 return from danish-magnates (confidence 1, Cliopatria's years). Page to try: https://en.wikipedia.org/wiki/Christopher_II_of_Denmark
- `/ledger (1332 pledges)`: Which provinces went to which Holstein count in 1326-1332, and when each came back. Page to try: https://en.wikipedia.org/wiki/Gerhard_III,_Count_of_Holstein-Rendsburg
- `/ledger (1227, 1238)`: Estonia lost in 1227 and returned by the Treaty of Stensby on 7 June 1238. Page to try: https://en.wikipedia.org/wiki/Danish_Estonia
- `/keyframe_review/15, /keyframe_review/19, /keyframe_review/20`: The 1206-1209 Saaremaa shape and the 1236 and 1250 keyframes are marked 'unverified: page budget'. Page to try: https://en.wikipedia.org/wiki/Livonian_Crusade
- `/wars/11`: The terms of the Treaty of Stralsund (1370): the Scanian castles held by the Hansa for 15 years. Page to try: https://en.wikipedia.org/wiki/Treaty_of_Stralsund_(1370)
- `/identity/rulers`: Rulers are missing for 1076-1182, 1241-1319 and 1375-1387, and there is no interregnum entry for 1332-1340. Page to try: https://en.wikipedia.org/wiki/List_of_Danish_monarchs

### Spot checks
- `/ledger/25` https://en.wikipedia.org/wiki/Valdemar_II_of_Denmark: confirmed (1203; the lead also says 1207, which the author flagged)
- `/ledger/26` https://en.wikipedia.org/wiki/Valdemar_II_of_Denmark: confirmed (1216 Hamburg)
- `/ledger/27` https://en.wikipedia.org/wiki/Valdemar_II_of_Denmark: confirmed (15 June 1219)
- `/ledger/30` https://en.wikipedia.org/wiki/Valdemar_II_of_Denmark: confirmed (22 July 1227, loss of the north German territories)
- `/ledger/35` https://en.wikipedia.org/wiki/Valdemar_IV_of_Denmark: confirmed date (24 June 1340); region over-broad, see fixes
- `/ledger/38` https://en.wikipedia.org/wiki/Valdemar_IV_of_Denmark: confirmed (1346 Vordingborg, all of Zealand)
- `/ledger/41` https://en.wikipedia.org/wiki/Valdemar_IV_of_Denmark: confirmed (Helsingborg 1360; Halland, Blekinge, Scania undated)
- `/ledger/42` https://en.wikipedia.org/wiki/Valdemar_IV_of_Denmark: confirmed (Gotland 1361)
- `/ledger/12` https://en.wikipedia.org/wiki/Cnut_the_Great: confirmed ('submitted to Cnut late in 1015')
- `/ledger/16` https://en.wikipedia.org/wiki/Cnut_the_Great: confirmed (Harald II died 1018, Danish accession 1018)
- `/ledger/17` https://en.wikipedia.org/wiki/Cnut_the_Great: confirmed (12 November 1035, Harthacnut succeeds)
- `/ledger/33` https://en.wikipedia.org/wiki/History_of_Denmark: confirmed ('the Rugian principality stayed with Denmark until 1325')
- `/ledger/43` https://en.wikipedia.org/wiki/History_of_Denmark: confirmed (infobox 'Incorporated into the Kalmar Union: 17 June 1397')
- `/ledger/21` https://en.wikipedia.org/wiki/Canute_VI_of_Denmark: confirmed (1185 Bogislaw acknowledges Canute as overlord)
- `/ledger/7` https://en.wikipedia.org/wiki/Sweyn_Forkbeard: confirmed (overlord 'c. 986 - c. 994 and from c.1000'; Svold '999 or 1000')
- `/ledger/8` https://en.wikipedia.org/wiki/Sweyn_Forkbeard: confirmed (August 1013)
- `/ledger/19` https://en.wikipedia.org/wiki/Sweyn_II_of_Denmark: confirmed ('King of Denmark from 1047'; Magnus died 1047)

## jaemtland: fix (fixed by reviewer)

Four spot checks, all confirmed: the 947 founding at confidence 1 (the page gives only the half-century), the 1178 conquest, the 1178 dissolve, and the infobox area of 34,009 km2 (ratio 0.76). The 1178 end matches old-kingdom-of-norway's 1178 gain.
### Fixes
- [applied] `/identity/capitals/0`: The capital was the label 'Frösön (placeholder: no seat is attested)', sourced to the runestone page. Evidence: The Jämtland page names the site: the farthings' assemblies were 'all parallel with the common assembly on Frösön', and 'Frösön acquired the position as regional centre'. Fix: Name set to 'Frösön', source set to the Jämtland page, note rewritten with the quotes.
### Gaps
- `/ledger/0`: The founding year 947 is Cliopatria's (confidence 1); the pages give only 'the first half of the 10th century'. Page to try: https://en.wikipedia.org/wiki/History_of_J%C3%A4mtland
- `/ledger (none)`: The saga tribute to Norwegian kings (Håkon Adalsteinsfostre, Øystein Magnusson) has no year on the page and could be a vassal tint. Page to try: https://en.wikipedia.org/wiki/History_of_J%C3%A4mtland

## Cross-dossier matrix

| event | mirror | status | note |
|---|---|---|---|
| kingdom-of-denmark 936 found scandinavian-minor-kingdoms | scandinavian-minor-kingdoms 936 loss | matched | kingdom-of-germany 936 loss of Hedeby also matches the predecessor entry. |
| kingdom-of-denmark 960 gain scandinavian-minor-kingdoms | scandinavian-minor-kingdoms 960 loss | matched | Both at Cliopatria's year. |
| kingdom-of-denmark 970 gain old-kingdom-of-norway | old-kingdom-of-norway 970 loss | mismatch | Disagree on the land: Denmark takes all 119 Norwegian cells of its 970 shape, Norway gives up only Viken (77 cells). |
| kingdom-of-denmark 974 loss holy-roman-empire | - | missing | holy-roman-empire (eu-08) has no 974 gain of Hedeby or the Danevirke. |
| kingdom-of-denmark 983 gain holy-roman-empire | - | missing | holy-roman-empire has no 983 loss of Hedeby to Denmark. |
| kingdom-of-denmark 995 loss old-kingdom-of-norway | old-kingdom-of-norway 995 gain | matched | Viken only on Norway's side (see 970). |
| kingdom-of-denmark 1000 vassal_start old-kingdom-of-norway | old-kingdom-of-norway 1000 loss | mismatch | Type and land differ: Denmark makes all of Norway a vassal, Norway loses Viken as direct land. The author flagged it. |
| kingdom-of-denmark 1015 vassal_end old-kingdom-of-norway | old-kingdom-of-norway 1015 gain | mismatch | Same disagreement as in 1000. |
| kingdom-of-denmark 1013 contest_start kingdom-of-england | kingdom-of-england 1013 contest_start | matched | Contest ends in 1014 on both sides. |
| kingdom-of-denmark 1015 contest_start kingdom-of-england | kingdom-of-england 1015 contest_start | matched |  |
| kingdom-of-denmark 1015 gain kingdom-of-england | kingdom-of-england 1016 loss | matched | Denmark gains Wessex in 1015-12, England records its loss in 1016-10 (within a year). |
| kingdom-of-denmark 1016 gain kingdom-of-england | kingdom-of-england 1016 loss | matched |  |
| kingdom-of-england 1017 gain kingdom-of-denmark | - | mismatch | England takes itself back from Denmark in 1017 (Cnut crowned in London). Denmark keeps England until the 1018 loss to north-sea-empire. Harald II was king of Denmark until 1018. |
| kingdom-of-denmark 1018 loss north-sea-empire | north-sea-empire 1018 found | matched |  |
| kingdom-of-denmark 1035 gain north-sea-empire | north-sea-empire 1035 dissolve | matched | Both 1035-11. |
| kingdom-of-denmark 1040 loss denmark-england | denmark-england 1040 found | matched | denmark-england's found event names only kingdom-of-england as counterpart, but its region includes Denmark (1040-6). |
| kingdom-of-denmark 1047 gain norway-denmark | norway-denmark 1047 dissolve | matched | norway-denmark has 25 October 1047; Denmark could add month 10. |
| kingdom-of-denmark 1168 vassal_start principality-of-rugen | principality-of-rugen 1168 vassal_start | matched |  |
| kingdom-of-denmark 1185 vassal_start duchy-of-pomerania | pomerania 1187 dissolve | mismatch | duchy-of-pomerania starts in 1188 and has no vassal events. pomerania dissolves in 1187 into kingdom-of-denmark as direct land. Route to eu-15. |
| kingdom-of-denmark 1185 vassal_start mecklenburg | - | missing | mecklenburg has no Danish vassal events for 1185-1227. |
| kingdom-of-denmark 1201 contest_start holy-roman-empire | holy-roman-empire 1201 contest_start | matched | county-of-holstein instead has a 1201 occupation_start against Denmark (it ends in 1227), against Denmark's contest 1201 and gain 1203: a mismatch the author flagged. |
| kingdom-of-denmark 1203 gain holy-roman-empire | holy-roman-empire 1203 loss | matched |  |
| kingdom-of-denmark 1216 gain holy-roman-empire | - | missing | holy-roman-empire has no 1216 loss of Hamburg. |
| kingdom-of-denmark 1219 vassal_start danish-estonia | danish-estonia 1219 found | mismatch | danish-estonia is founded against ancient-estonia and records no vassal tie to Denmark. |
| kingdom-of-denmark 1223 contest_start holy-roman-empire | holy-roman-empire 1223 contest_start | matched |  |
| kingdom-of-denmark 1227 loss holy-roman-empire | holy-roman-empire 1227 gain | matched | county-of-holstein's 1227 occupation_end also matches. |
| kingdom-of-denmark 1227 vassal_end mecklenburg | - | missing |  |
| kingdom-of-denmark 1227 vassal_end duchy-of-pomerania | - | missing | duchy-of-pomerania has no vassal events. |
| livonian-brothers-of-the-sword 1227 gain kingdom-of-denmark | danish-estonia 1227 loss | mismatch | The loss is in danish-estonia, which should be the counterpart. Denmark lacks vassal_end 1227 and vassal_start 1238 for danish-estonia. |
| danish-estonia 1238 gain teutonic-order | - | missing | Denmark has no 1238 vassal_start for danish-estonia (Treaty of Stensby). |
| duchy-of-schleswig 1058 vassal_start kingdom-of-denmark | - | mismatch | Schleswig is a Danish vassal from 1058 in duchy-of-schleswig (confidence 1), but Denmark draws it as direct land and records no vassal. Decide which way with the owner of duchy-of-schleswig. |
| kingdom-of-denmark 1325 vassal_end principality-of-rugen | principality-of-rugen 1325 vassal_end | matched | holy-roman-empire-minor-states gains the Rügen cells from kingdom-of-denmark in 1326 (confidence 1). Denmark never drew them, so this is an exception. |
| kingdom-of-denmark 1332 loss kingdom-of-sweden | kingdom-of-sweden 1332 gain | mismatch | The two sides disagree on Halland: Sweden gains Skåne and Blekinge only. |
| danish-magnates 1332 found kingdom-of-denmark | - | mismatch | danish-magnates draws Estonia from 1332, while Denmark keeps it with danish-estonia to 1346. The author flagged the double drawing. |
| kingdom-of-denmark 1340 gain county-of-holstein | - | missing | Counterpart corrected by the reviewer. county-of-holstein has no 1326-1346 pledge events, and Denmark has no 1332 loss for these gains. |
| kingdom-of-denmark 1344 split danish-magnates | - | missing | danish-magnates has no 1344 event for the southern-Jutland sliver. |
| kingdom-of-denmark 1344 gain county-of-holstein | - | missing | North Friesland, as for 1340. |
| kingdom-of-denmark 1346 gain county-of-holstein | - | missing | Zealand, as for 1340. |
| kingdom-of-denmark 1346 vassal_end danish-estonia | danish-estonia 1346 dissolve | matched | danish-estonia has 1 November 1346; Denmark could add month 11. |
| kingdom-of-denmark 1352 gain danish-magnates | danish-magnates 1351 dissolve | matched | danish-magnates' dissolve has no counterpart; it should name kingdom-of-denmark. |
| kingdom-of-denmark 1360 gain kingdom-of-sweden | kingdom-of-sweden 1360 loss | matched | Halland is absent on Sweden's side. |
| kingdom-of-denmark 1361 gain kingdom-of-sweden | kingdom-of-sweden 1361 loss | matched |  |
| kingdom-of-denmark 1397 dissolve kalmar-union | kalmar-union 1397 found | matched | Both 1397-6. |
| jaemtland 1178 loss old-kingdom-of-norway | old-kingdom-of-norway 1178 gain | matched |  |
| jaemtland 1178 dissolve old-kingdom-of-norway | old-kingdom-of-norway 1178 gain | matched | Successor entry agrees. |

Routing:

- eu-08 holy-roman-empire: add the 974, 983 and 1216 events.
- eu-15 pomerania and duchy-of-pomerania: add the vassal events for 1185-1227.
- mecklenburg: add vassal events for 1185 and 1227.
- eu-11 kingdom-of-england: agree on England in 1017.
- old-kingdom-of-norway: agree on Viken versus all of Norway, and on vassal versus loss.
- kingdom-of-sweden: agree on Halland.
- county-of-holstein: add the 1326-1346 pledges.
- danish-magnates: add the 1344 event, give its 1351 dissolve a counterpart, and settle the Estonia double drawing.
- livonian-brothers-of-the-sword: change the 1227 counterpart to danish-estonia.
- duchy-of-schleswig: agree with Denmark whether Schleswig is a vassal or direct land.
