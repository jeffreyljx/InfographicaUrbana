# Review of batch eu-18-c (2026-10-31)

Adversarial review of kingdom-of-serbia and second-bulgarian-empire (author notes: _notes/eu-18-c.md). Machine copy: history/notes/phase-b/reviews/eu-18-c.json.

Mechanical: both validate with 0 errors; --resolve warns only on 'Rhodope Mountains' (10 times, second-bulgarian-empire). All 19 and 22 Cliopatria shapes have verdicts. Spot checks: 6 Serbian and 9 Bulgarian events opened; every one is on its page with its year. Nothing fabricated. Both dossiers go back to the author for unmirrored or self-contradicting territorial events.

## kingdom-of-serbia: fail

Area: Serbian Kingdom (medieval) has no infobox area or capital (checked); author says so. Cliopatria peak 102,416 km2 (1326).

### Findings

- `/ledger/22, /ledger/26, /keyframe_review/16` (blocking): The same Syrmian land is gained twice (1316 and 1324) with no loss between, and the 1316 gain is drawn by no keyframe (kingdom-of-serbia_1314 has verdict ok although its note says it understates 1316-1325). Evidence: Stefan Dečanski page: 'Vladislav II had been released from prison upon Milutin's death' (1321) and recovered the Syrmia throne; war 1323, Vladislav 'defeated in battle in late 1324'. The kingdom-of-syrmia dossier holds the land to 1325 with no 1316 loss. The Syrmia shape is about 23,000 km2, not a small event. Fix: Either (a) add a 1321 loss to kingdom-of-syrmia (Vladislav II restored, Dečanski page) and turn kingdom-of-serbia_1314 into adjust with a new keyframe 1316-1320 = 1314 shape + Cliopatria Syrmia 1318 (minus Belgrade and Mačva from 1319), and ask the Syrmia owner for the mirrored 1316 loss / 1321 gain; or (b) drop the 1316 gain and 1319 loss as Syrmian events and say so in the notes. Keep the 1324 gain.
- `/ledger/12` (blocking): 1250 gain of the Niš country from second-bulgarian-empire (confidence 1) has no loss in the Bulgarian ledger of this same batch. Evidence: second-bulgarian-empire ledger has nothing between the 1246 losses to Nicaea and the 1254 war; its 1250 keyframe drops the west without an event naming Serbia. Fix: Add the mirrored 1250 loss to kingdom-of-serbia in second-bulgarian-empire (confidence 1, same region), or change this counterpart to nicaean-empire/nobody with a note.
- `/ledger/11` (blocking): 1227 loss of the Skopje country to second-bulgarian-empire has no gain in the Bulgarian ledger, and the Bulgarian keyframe for 1221-1229 does not hold Skopje (its note: 'Who held the Skopje country in 1227-1229 is on no page opened'). Evidence: Within-batch mismatch: the land is lost by Serbia to Bulgaria but held by nobody in either dossier's keyframes 1227-1229. Fix: Pick one holder for 1227-1229: add a 1227 gain from kingdom-of-serbia to the Bulgarian ledger and its keyframe, or set this loss's counterpart to despotate-of-epirus (which held Macedonia before 1230) or nobody.
- `/ledger (missing, 1230 and 1241)` (blocking): No vassal_start/vassal_end with second-bulgarian-empire, while the Bulgarian ledger has vassal_start kingdom-of-serbia 1230 (/ledger/22) and vassal_end 1241 (/ledger/24). Evidence: Rule 3 of the reviewer brief: a vassal_start of X is a vassal_start in X's ledger with this state as counterpart. Keyframe 7's note mentions the 1230 suzerainty 'entered in' the Bulgarian dossier only. Fix: Add vassal_start (1230) and vassal_end (1241) with counterpart second-bulgarian-empire, confidence 1, same source as the Bulgarian events.
- `/ledger (missing, 1301 and 1312)` (to do): No mirror for kingdom-of-syrmia /ledger/3 (1301 loss to kingdom-of-serbia, confidence 3, Rudnik) and /ledger/4 (1312 gain back, confidence 2). Evidence: kingdom-of-syrmia ledger (lon 20.5, lat 44.13, 30 km); the author read that dossier (Braničevo 1291/1292 in the notes) but did not mirror these. Fix: Add a 1301 gain and 1312 loss with counterpart kingdom-of-syrmia (Rudnik), or explain in notes why not.
- `/ledger (missing, 1329)` (to do): No mirror for banate-of-bosnia /ledger/9 (1329 gain of Nevesinje and Zagorje from kingdom-of-serbia, confidence 3). Evidence: Stefan Dušan page: Dušan was 'defeating Bosnian forces in 1329 during the War of Hum' and 'The Ban soon took over Nevesinje' (undated). Fix: Add a 1329 loss to banate-of-bosnia (Nevesinje, Zagorje) at confidence 2, or say in notes that the Dušan page has Serbia winning in 1329 and the Bosnian dossier should move it.
- `/ledger/17` (to do): Split to kingdom-of-syrmia dated 1282; the Syrmia dossier's found event is 1284. Evidence: Serbian Kingdom (medieval) page: Dragutin 'abdicated in favour of his younger brother Milutin, in 1282', after which the Hungarian king 'gave him lands in northeastern Bosnia, the region of Mačva, and the city of Belgrade'. Fix: Agree one year with the Syrmia owner (eu-18): either 1282 here and found 1282 there, or 1284 in both, and say which lands Dragutin kept in 1282.
- `/identity/rulers` (to do): Ruler list has a gap 1202-1203 (Vukan ruled in Stefan's place). Evidence: Stefan's own entry notes 'Vukan ruled in his place until 1204'. Fix: Add Vukan Nemanjić 1202-1203, title Grand Prince, source Stefan_the_First-Crowned.
- `/wars/0` (to do): War runs from 1183, five years before the dossier's start (1188). Evidence: Reviewer brief rule 2: wars inside the life. Fix: Set from 1188 and say in the outcome that it began in 1183 under grand-principality-of-serbia.

### Gaps for a gap-filler (thin)

- `/ledger/8`: 1216 Kosovo gain at confidence 1, no dated page (try https://en.wikipedia.org/wiki/Prizren)
- `/ledger/10, /ledger/11`: Skopje country 1220 and 1227, confidence 1 (try https://en.wikipedia.org/wiki/Skopje)
- `/ledger/12`: Niš country 1250, confidence 1 (try https://en.wikipedia.org/wiki/Ni%C5%A1)
- `/ledger/21`: Durrës lost 1304, confidence 1 (Angevin side) (try https://en.wikipedia.org/wiki/Kingdom_of_Albania_(medieval))
- `/ledger/6`: Zeta under Vukan 1204-1216, confidence 1 (try https://en.wikipedia.org/wiki/Vukan_Nemanji%C4%87)
- `/ledger/14`: end of the 1268 Mačva contest, confidence 1 (try https://en.wikipedia.org/wiki/Stefan_Uro%C5%A1_I)
- `/keyframe_review/1 (Hum)`: Hum conquered by Hungary 1198 and Serbian again by 1326: no event dates the return (try https://en.wikipedia.org/wiki/Zachlumia)

### Spot checks

- `/ledger/31` https://en.wikipedia.org/wiki/Stefan_Du%C5%A1an: confirmed: 'Peace was concluded on 26 August 1334'; gains in Ohrid, Prilep, Strumitsa, Siderokastron, Chermen and Prosek
- `/ledger/32` https://en.wikipedia.org/wiki/Stefan_Du%C5%A1an: confirmed: 'the Hungarians temporarily lost Mačva and Belgrade in 1335'
- `/ledger/29` https://en.wikipedia.org/wiki/Stefan_Du%C5%A1an: confirmed: 1333, 'Dušan sold Ston and its envisions, including the Pelješac peninsula'
- `/ledger/35` https://en.wikipedia.org/wiki/Stefan_Du%C5%A1an: confirmed: Serres 'had been conquered on 25 September 1345'
- `/ledger/27` https://en.wikipedia.org/wiki/Stefan_De%C4%8Danski: confirmed: 'by the end of the same year, Serbia lost the region of Hum to Bosnia' (1326); same page gives Vladislav II's 1321 restoration (finding 1)
- `/ledger/37` https://en.wikipedia.org/wiki/Stefan_Du%C5%A1an: confirmed: 'On 16 April 1346 (Easter), Dušan convoked a huge assembly at Skopje'

## second-bulgarian-empire: fail

Area: Shape alive in 1230 is _1227 (228,826 km2); the author marks it wrong and uses the 1236 outline (312,296 km2, ratio 1.07) from 1230.

### Findings

- `/ledger/49/region` (applied by reviewer): 1371 loss included Sofia city (Grad Sofiya), which the page does not name; Sofia fell in 1382 or 1385 (/ledger/51). Evidence: Second Bulgarian Empire page: the Ottomans 'conquered northern Thrace, the Rhodopes, Kostenets, Ihtiman, and Samokov'. Fix: Region element replaced by admin1 Sofia (province) only; note marked.
- `/ledger/50/region` (applied by reviewer): 1373 regain included Sofia city, which was never lost in 1371. Evidence: As above; the note's own quote names Ihtiman and Samokov. Fix: Region replaced by admin1 Sofia (province) only; note marked.
- `/ledger/43/confidence` (applied by reviewer): Confidence 3 with a region (Burgas coast, 60 km) the page does not name. Evidence: Battle of Velbazhd page: 'in 1332 the Bulgarians defeated the Byzantines in the battle of Rusokastro and regained many territories in Thrace' (no town named). Fix: Lowered to 2.
- `/ledger/37/confidence` (applied by reviewer): Confidence 3 with a region element (80 km around Edirne) the page does not name. Evidence: Theodore Svetoslav page: in 1304 he 'captured the fortresses of northeastern Thrace, including Mesembria, Anchialos, Sozopolis, and Agathopolis'; Adrianople is not named. Fix: Lowered to 2 (the redraw is the next finding).
- `/ledger (missing vassal events)` (blocking): No vassal events for the Mongol tribute (1242), the Horde vassalage (c. 1280 to 1300) or the Ottoman vassalage (1373 to 1393); /wars/6 note says the suzerain's dossier should carry them, which is not the rule. Evidence: ulus-of-jochi /ledger/12 (vassal_start 1280) and /ledger/15 (vassal_end 1293), ottoman-empire /ledger/13 (vassal_start 1376) and /ledger/18 (vassal_end 1393) all name second-bulgarian-empire; the Second Bulgarian Empire page: 'forced Bulgarians to pay a yearly tribute' (1242), 'The Mongol influence ended with Theodore Svetoslav's rise', 'forced to become an Ottoman vassal'. Reviewer brief rule 3: both ledgers carry vassal_start. Fix: Add vassal_start/vassal_end pairs: mongol-empire 1242 (to the hand-over to ulus-of-jochi or 1280), ulus-of-jochi 1280 then golden-horde to 1300, ottoman-empire 1373 (Ivan Shishman page; note the Ottoman dossier's 1376) to 1393.
- `/ledger (missing, 1227 and 1250)` (blocking): No mirrors for the Serbian dossier's 1227 loss to Bulgaria (Skopje country) and 1250 gain from Bulgaria (Niš country); see the kingdom-of-serbia findings /ledger/11 and /ledger/12. Evidence: Same author, same batch: kingdom-of-serbia /ledger/11 and /ledger/12 name second-bulgarian-empire; this ledger has neither event. Fix: Resolve together with the Serbian dossier (add the mirrors here or change the Serbian counterparts).
- `/ledger/35, /keyframe_review/21-22` (to do): 1300 gain of southern Bessarabia (Budjak) is drawn by no keyframe and never ends (no loss, no adjust keyframe; its note says Cliopatria's shape does not reach it). Evidence: Second Bulgarian Empire page: 'secured Southern Bessarabia as far as Bolgrad to Bulgaria' (1300). Keyframes 1294 and 1305 are verdict ok without it. The Budjak is about 12,000 km2, not a small event. Fix: Add adjust keyframes from 1300 that union the Budjak, and a dated loss (with page) or an explicit end and note; if no page dates its loss, end it with a confidence-1 loss and say so.
- `/ledger/36, /ledger/37, /ledger/38, /ledger/42` (to do): The 80 km circle around Edirne draws Adrianople and southern Thrace as Bulgarian in 1304 and 1331, which no page says and which the keyframes contradict. Evidence: Cell check of Cliopatria shapes: Edirne is outside every Bulgarian shape 1305-1343 (south edge 41.72 N); Theodore Svetoslav page names only northeastern Thrace and the four coastal towns; the Bulgarian article has no 1331 Adrianople campaign. Fix: Redraw 'northeastern Thrace' north of the Sakar and Strandzha (for example admin1 Yambol plus the Burgas coast) and keep Adrianople out; confidence 2 for /ledger/42 unless the Ivan Alexander page names the towns.
- `/wars/5` (to do): Zones empty although the war outcome quotes the Bulgarians 'conquered the territories to the west of the Maritsa'; latin-empire has contest_start 1235 and contest_end 1236 and a 1230 loss naming this state, with no mirror here. Evidence: Reviewer brief rule 10: empty zones only where no ground changed hands, and said so. Fix: Give the war a zone (Thrace west of the Maritsa / the approaches of Constantinople) and mirror the Latin contest events, or explain in the war's note why none are needed.
- `/ledger/34/note` (to do): The quote is cut before '... and several cities in Thrace, including Philippopolis'. Evidence: Second Bulgarian Empire page: 'A major Byzantine invasion in 1263 led to the loss of the coastal towns Messembria and Anchialus, and several cities in Thrace—including Philippopolis.' The dossier's shapes from 1246 do not hold Plovdiv (cell check), so the page and the drawing disagree silently. Fix: Restore the full sentence and say in the 1250 keyframe note which reading is drawn (Philippopolis Byzantine from 1246, or Bulgarian 1254-1263 with a 1263 loss).
- `/ledger (missing, 1246 Epirus)` (to do): despotate-of-epirus /ledger/19 has a 1246 gain from this state (Albania and northwestern Macedonia); this ledger's 1246 losses name only nicaean-empire. Evidence: Epirus dossier note: 'Michael II also took advantage of the opportunity to expand into Albania and northwestern Macedonia'. Fix: Add a 1246 loss to despotate-of-epirus (western Macedonia, Albania) at confidence 1-2, or explain.
- `/ledger/41/counterpart` (to do): 1323 Vidin gain names despotate-of-vidin (a 1356-1396 state) while the 1261 loss of Vidin went to kingdom-of-hungary; the chain has no holder change between. Evidence: The author's own counterparts_needing_dossiers proposes 'vidin-1261' for 1261-1323. Fix: Use one counterpart for both ends of Vidin's 1261-1323 separation (the proposed vidin-1261, or nobody) and say so.

### Gaps for a gap-filler (thin)

- `/ledger/8`: 1202 loss of Belgrade and Braničevo to Hungary, confidence 1 (try https://en.wikipedia.org/wiki/Kaloyan_of_Bulgaria)
- `/ledger/16, /ledger/17, /ledger/18`: 1216 and 1220 losses to Serbia and Epirus, confidence 1 (try https://en.wikipedia.org/wiki/Boril_of_Bulgaria)
- `/ledger/22, /ledger/24`: Serbian vassalage 1230-1241, confidence 1 (try https://en.wikipedia.org/wiki/Stefan_Vladislav)
- `/ledger/26`: end of the Thessalonica vassalage 1246, confidence 1 (try https://en.wikipedia.org/wiki/Empire_of_Thessalonica)
- `/identity/rulers`: ruler strip omitted (1241-1300 reigns not on the pages opened) (try https://en.wikipedia.org/wiki/List_of_Bulgarian_monarchs)
- `/keyframe_review/19-21`: shapes 1279-1304 verified only as unchanged (page budget); Ivaylo's revolt undated (try https://en.wikipedia.org/wiki/Uprising_of_Ivaylo)
- `/ledger/48`: who held Anchialus, Mesembria and Sozopolis after the 1366 Savoyard crusade (counterpart is a non-state) (try https://en.wikipedia.org/wiki/Savoyard_crusade)

### Spot checks

- `/ledger/7` https://en.wikipedia.org/wiki/Second_Bulgarian_Empire: confirmed: 'In 1201, Kaloyan captured Varna'
- `/ledger/11` https://en.wikipedia.org/wiki/Second_Bulgarian_Empire: confirmed: 'the Bulgarians retook most of Thrace, including the important city of Philippopolis'
- `/ledger/25` https://en.wikipedia.org/wiki/Second_Bulgarian_Empire: confirmed: 'the Nicaean army conquered large areas in southern Thrace, the Rhodopes, and Macedonia' (1246)
- `/ledger/49` https://en.wikipedia.org/wiki/Second_Bulgarian_Empire: confirmed (26 September 1371; Kostenets, Ihtiman, Samokov); Sofia city not on page, region fixed
- `/ledger/43` https://en.wikipedia.org/wiki/Battle_of_Velbazhd: confirmed year; region not named, confidence lowered to 2
- `/ledger/37` https://en.wikipedia.org/wiki/Theodore_Svetoslav_of_Bulgaria: confirmed 1304 and the four towns; Adrianople not named, confidence lowered to 2
- `/ledger/15` https://en.wikipedia.org/wiki/Second_Bulgarian_Empire: confirmed: 'in 1211, Boril was forced to cede Belgrade and Braničevo to Hungary'
- `/ledger/34` https://en.wikipedia.org/wiki/Second_Bulgarian_Empire: confirmed 1263; the note truncates the sentence (Philippopolis omitted)
- `/ledger/35` https://en.wikipedia.org/wiki/Second_Bulgarian_Empire: confirmed: 'secured Southern Bessarabia as far as Bolgrad to Bulgaria'

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| kingdom-of-serbia 1188 found grand-principality-of-serbia | grand-principality-of-serbia 1187 dissolve | matched | hand-over; the GPS dissolve has counterpart null and names kingdom-of-serbia in its note |
| kingdom-of-serbia 1203 loss second-bulgarian-empire | second-bulgarian-empire 1203 gain | matched |  |
| kingdom-of-serbia 1216 gain second-bulgarian-empire | second-bulgarian-empire 1216 loss | matched | both confidence 1 |
| kingdom-of-serbia 1220 gain second-bulgarian-empire | second-bulgarian-empire 1220 loss | matched | both confidence 1 |
| kingdom-of-serbia 1227 loss second-bulgarian-empire | second-bulgarian-empire   | missing | no Bulgarian gain; Bulgarian keyframe 1221-1229 excludes Skopje (within batch) |
| second-bulgarian-empire 1230 vassal_start kingdom-of-serbia | kingdom-of-serbia   | missing | no vassal_start in the Serbian ledger (within batch) |
| second-bulgarian-empire 1241 vassal_end kingdom-of-serbia | kingdom-of-serbia   | missing | no vassal_end in the Serbian ledger (within batch) |
| kingdom-of-serbia 1250 gain second-bulgarian-empire | second-bulgarian-empire   | missing | no Bulgarian loss (within batch) |
| kingdom-of-serbia 1204 vassal_start Zeta (Vukan, then Đorđe) | zeta   | exception | no dossier; listed in counterparts_needing_dossiers |
| kingdom-of-serbia 1282 gain byzantine-empire | byzantine-empire 1285 loss | mismatch | 3 years apart; the Byzantine side is confidence 1, the Serbian Kingdom page has 1282 (route to eu-05) |
| kingdom-of-serbia 1282 split kingdom-of-syrmia | kingdom-of-syrmia 1284 found | mismatch | 2 years apart; agree a year (eu-18) |
| kingdom-of-serbia 1296 gain house-of-anjou-sicily | house-of-anjou-sicily   | missing | no 1296 loss in house-of-anjou-sicily (eu-18) |
| kingdom-of-serbia 1304 loss house-of-anjou-sicily | house-of-anjou-sicily 1304 gain | matched |  |
| kingdom-of-syrmia 1301 loss kingdom-of-serbia | kingdom-of-serbia   | missing | Rudnik; Serbian ledger lacks the 1301 gain |
| kingdom-of-syrmia 1312 gain kingdom-of-serbia | kingdom-of-serbia   | missing | Rudnik; Serbian ledger lacks the 1312 loss |
| kingdom-of-serbia 1316 gain kingdom-of-syrmia | kingdom-of-syrmia   | mismatch | Syrmia holds the land to 1325 with no 1316 loss; Serbia regains it again in 1324 without a 1321 loss |
| kingdom-of-serbia 1319 loss kingdom-of-hungary | kingdom-of-hungary   | missing | no 1319 Belgrade/Mačva gain in kingdom-of-hungary (eu-15) |
| kingdom-of-serbia 1324 gain kingdom-of-syrmia | kingdom-of-syrmia 1325 dissolve | matched | within one year |
| banate-of-bosnia 1324 gain kingdom-of-serbia | kingdom-of-hungary 1324 loss | mismatch | Usora and Soli: Bosnia names Serbia, Hungary names itself as the loser, Syrmia loses Tuzla/Doboj to Bosnia in 1325; the Bosnian counterpart should be kingdom-of-syrmia or kingdom-of-hungary (eu-18 Bosnia owner) |
| kingdom-of-serbia 1326 loss banate-of-bosnia | banate-of-bosnia 1326 gain | matched |  |
| banate-of-bosnia 1329 gain kingdom-of-serbia | kingdom-of-serbia   | missing | Nevesinje and Zagorje; Serbian ledger lacks a 1329 loss |
| kingdom-of-serbia 1333 loss republic-of-ragusa | republic-of-ragusa   | missing | no 1333 Ston/Pelješac gain in republic-of-ragusa |
| kingdom-of-serbia 1334 gain byzantine-empire | byzantine-empire   | missing | no 1334 loss in byzantine-empire (eu-05) |
| kingdom-of-serbia 1335 gain kingdom-of-hungary | kingdom-of-hungary   | missing | no 1335 loss in kingdom-of-hungary (eu-15) |
| kingdom-of-serbia 1345 gain byzantine-empire | byzantine-empire   | missing | Macedonia to Kavala and Serres: no Byzantine loss (eu-05) |
| kingdom-of-serbia 1346 dissolve serbian-empire | serbian-empire 1346 found | matched |  |
| second-bulgarian-empire 1187 gain byzantine-empire | byzantine-empire 1187 loss | matched |  |
| second-bulgarian-empire 1189 gain byzantine-empire | byzantine-empire 1191 loss | mismatch | 2 years apart |
| second-bulgarian-empire 1195 gain byzantine-empire | byzantine-empire   | missing | no Byzantine loss (eu-05) |
| second-bulgarian-empire 1199 gain byzantine-empire | byzantine-empire 1202 loss | mismatch | 3 years; the Bulgarian page has 1199, the Byzantine dossier 1202 (author noted) |
| second-bulgarian-empire 1201 gain byzantine-empire | byzantine-empire 1201 loss | matched | Varna |
| second-bulgarian-empire 1202 loss kingdom-of-hungary | kingdom-of-hungary 1202 gain | matched |  |
| second-bulgarian-empire 1203 gain kingdom-of-hungary | kingdom-of-hungary 1206 loss | mismatch | 3 years; Hungary confidence 1 (eu-15) |
| second-bulgarian-empire 1205 gain latin-empire | latin-empire 1205 loss | matched |  |
| second-bulgarian-empire 1208 loss latin-empire | latin-empire 1208 gain | matched |  |
| second-bulgarian-empire 1211 loss kingdom-of-hungary | kingdom-of-hungary 1216 gain | mismatch | 5 years; the Bulgarian page says 1211 (eu-15 should move) |
| second-bulgarian-empire 1220 loss despotate-of-epirus | despotate-of-epirus 1217 gain | mismatch | 3 years; both confidence 1 |
| second-bulgarian-empire 1221 gain kingdom-of-hungary | kingdom-of-hungary 1236 loss | mismatch | 15 years; Maria's dowry 1221 per the Ivan Asen II page (eu-15 should move) |
| second-bulgarian-empire 1230 gain despotate-of-epirus | despotate-of-epirus 1230 loss | matched | Klokotnitsa |
| latin-empire 1230 loss second-bulgarian-empire | second-bulgarian-empire   | missing | no 1230 gain from latin-empire here |
| second-bulgarian-empire 1230 vassal_start empire-of-thessalonica | empire-of-thessalonica   | missing | no vassal_start in empire-of-thessalonica (eu-05) |
| second-bulgarian-empire 1232 loss kingdom-of-hungary | kingdom-of-hungary 1255 gain | mismatch | 23 years; Ivan Asen II page has late 1231 or 1232 (eu-15 should move) |
| latin-empire 1235 contest_start second-bulgarian-empire | second-bulgarian-empire   | missing | Bulgarian war 1235-1236 has empty zones and no contest events |
| nicaean-empire 1237 loss second-bulgarian-empire | second-bulgarian-empire   | missing | Tzurulum 1237; no Bulgarian gain |
| second-bulgarian-empire 1246 loss nicaean-empire | nicaean-empire 1246 gain | matched |  |
| despotate-of-epirus 1246 gain second-bulgarian-empire | second-bulgarian-empire   | missing | Albania and NW Macedonia; no Bulgarian loss to Epirus |
| second-bulgarian-empire 1246 vassal_end empire-of-thessalonica | empire-of-thessalonica   | missing | eu-05 |
| second-bulgarian-empire 1254 gain nicaean-empire | nicaean-empire 1255 loss | matched | 1254-1256 war matched on both sides |
| second-bulgarian-empire 1256 loss nicaean-empire | nicaean-empire 1256 gain | matched |  |
| second-bulgarian-empire 1260 gain kingdom-of-hungary | kingdom-of-hungary   | missing | Vidin 1260/1261: no Hungarian events (eu-15) |
| second-bulgarian-empire 1263 loss byzantine-empire | byzantine-empire   | missing | eu-05 |
| ulus-of-jochi 1280 vassal_start second-bulgarian-empire | second-bulgarian-empire   | missing | Bulgarian ledger lacks the vassal_start (finding) |
| ulus-of-jochi 1293 vassal_end second-bulgarian-empire | second-bulgarian-empire   | missing | bookkeeping end; Bulgarian ledger lacks it |
| second-bulgarian-empire 1300 gain golden-horde | golden-horde   | missing | Budjak; no golden-horde loss (ia-02) |
| second-bulgarian-empire 1304 gain byzantine-empire | byzantine-empire   | missing | eu-05 |
| second-bulgarian-empire 1322 loss byzantine-empire | byzantine-empire   | missing | 1322 loss and 1323 regain; eu-05 |
| second-bulgarian-empire 1323 gain despotate-of-vidin | despotate-of-vidin   | exception | no dossier yet (eu-18 part not run); counterpart slug questionable (finding) |
| second-bulgarian-empire 1331 gain byzantine-empire | byzantine-empire   | missing | 1331 and 1332; eu-05 |
| second-bulgarian-empire 1344 gain byzantine-empire | byzantine-empire 1344 loss | matched |  |
| second-bulgarian-empire 1356 split despotate-of-vidin | despotate-of-vidin   | exception | no dossier yet (eu-18) |
| second-bulgarian-empire 1356 split despotate-of-dobruja | despotate-of-dobruja   | exception | no dossier yet (eu-18) |
| second-bulgarian-empire 1366 loss despotate-of-dobruja | despotate-of-dobruja   | exception | no dossier yet (eu-18) |
| second-bulgarian-empire 1371 loss ottoman-empire | ottoman-empire   | missing | Chernomen conquests; no Ottoman gain naming Bulgaria (me-10) |
| ottoman-empire 1376 vassal_start second-bulgarian-empire | second-bulgarian-empire 1373 gain | mismatch | Bulgarian ledger has a 1373 gain but no vassal_start; Ottoman has 1376 vassal_start and no 1373 loss |
| second-bulgarian-empire 1385 loss ottoman-empire | ottoman-empire 1385 gain | matched | Sofia |
| second-bulgarian-empire 1388 loss ottoman-empire | ottoman-empire   | missing | me-10 |
| second-bulgarian-empire 1393 loss ottoman-empire | ottoman-empire 1393 gain | matched | Tarnovo |
| ottoman-empire 1393 vassal_end second-bulgarian-empire | second-bulgarian-empire   | missing | Bulgarian ledger lacks the vassal_end |
| second-bulgarian-empire 1395 dissolve ottoman-empire | ottoman-empire   | missing | Nikopol 1395: the Ottoman ledger ends Bulgaria in 1393 |

## Problems

- No page failed to load for the reviewer. Pages opened: Second_Bulgarian_Empire (twice), Battle_of_Velbazhd, Theodore_Svetoslav_of_Bulgaria, Stefan_Dušan, Stefan_Dečanski, Serbian_Kingdom_(medieval).
- Reviewer applied four small fixes to second-bulgarian-empire (/ledger/49 and /ledger/50 regions, /ledger/37 and /ledger/43 confidence 3 to 2); the file validates (0 errors, 0 warnings without --resolve). kingdom-of-serbia was not edited.
- No fabricated or mis-dated event found: all 15 spot checks matched their pages. Both verdicts are fail for unmirrored and internally inconsistent territorial events (within the batch and against kingdom-of-syrmia, ottoman-empire, ulus-of-jochi), not for sourcing.
- Many mirrors are missing on the other side (byzantine-empire eu-05, kingdom-of-hungary eu-15, republic-of-ragusa, house-of-anjou-sicily, golden-horde, ottoman-empire me-10); the kingdom-of-hungary dossier dates the Belgrade-Braničevo transfers 3 to 23 years away from the Bulgarian pages and should be corrected there.
- despotate-of-vidin, despotate-of-dobruja, albanian-principalities, austria-hungary and united-principalities-of-moldavia-and-wallachia have no dossier yet (groups not run).
