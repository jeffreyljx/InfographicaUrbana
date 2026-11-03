# Review of batch eu-11-h: Kingdom of England

Reviewer: adversarial review, 2026-10-25. Dossier: `history/polities/kingdom-of-england.json` (927-1707, 112 events, 69 keyframes, 14 wars, 14 sources).

## Verdict: fail

No fabrication found: 7 events checked on 6 pages plus the Kingdom page, all dated and placed as the notes say. Validator 0 errors, 2 warnings (first-barons-war-rebels, listed). Fails on unapplied blocking findings: the 1284 gain contradicts its own page and doubles the principality-of-wales colony; the dependency double drawing (Ireland, Calais, Wales, Gascony) needs a ruling; the 1277 Aberconwy gain is missing though on an opened page and mirrored by Gwynedd; keyframe 1582 leaves 33 Munster cells to nobody in 1584-1587. One region text repaired by the reviewer.

Mechanical: validator 0 errors, 2 warnings (`first-barons-war-rebels` has no dossier; listed by the author). Ledger sorted, found 927 and dissolve 1707 at the life's ends, capitals contiguous (Winchester 927-1065, London 1066-1707), certainty covers 927-1707, rulers contiguous except the honest 1649-1653 gap. Every Cliopatria shape (56) has a verdict; 13 new keyframes carry from, to and correction.

Area: the Kingdom of England infobox has no area (confirmed on the page); the dossier says so. Cliopatria's 1609-1708 shapes include Scotland, which every correction removes and notes.

## Fixes (author)

1. `/ledger/49/region/text` (applied by the reviewer)
   - What: The region text was a broken slice of the note ('s deposition in July 1296 Edward forced over 1,800 nobles to swear homage and was '), not the source's words.
   - Why: First War of Scottish Independence page: 'By July, John was deposed as king and sent into exile'; Edward forced over 1,800 Scottish nobles to swear homage, 'thus making him, in effect, ruler of Scotland'.
   - Fix: Replaced with: Scotland: 'By July, John was deposed as king and sent into exile'; Edward forced over 1,800 Scottish nobles to swear homage, 'thus making him, in effect, ruler of Scotland'. Re-validated: 0 errors.

2. `/ledger/45`
   - What: The 1284 Statute of Rhuddlan is typed as a gain of the Kingdom of England although the cited page says the opposite, and the principality-of-wales dossier (colony, 1283-1542, founded from kingdom-of-gwynedd) draws the same land, so Wales is drawn twice 1284-1541 (England keyframes 21-46 hold the 48 Welsh cells).
   - Why: Conquest of Wales by Edward I: the lands were declared 'annexed and united' to the English crown, 'although they did not become part of the Kingdom of England', and were 'incorporated into the new Principality of Wales'. The note of /ledger/45 itself says so.
   - Fix: Following the ruling on dependencies (next fix): make /ledger/45 a vassal_start with counterpart principality-of-wales (1284, conf 3 on this page), add vassal_end principality-of-wales at 1542 beside the existing 1542 gain, and subtract principality-of-wales_1283's region from the corrections of keyframes 21-46 (1284-1541), marking them adjust.

3. `/keyframe_review/13 to /keyframe_review/68`
   - What: England's corrections keep as direct English land every cell that five dependency dossiers now draw: lordship-of-ireland (1171-1541), kingdom-of-ireland (1542-1707), pale-of-calais (1347-1558), principality-of-wales (1283-1541) and duchy-of-aquitaine (English Gascony 1204-1453). The author left the Irish case to the reviewer and did not mention Calais, Wales or Gascony.
   - Why: Schema: colony is 'a dependency ruled from elsewhere, drawn as a vassal tint of the metropole'. lordship-of-ireland and kingdom-of-ireland notes ask England to subtract them; duchy-of-aquitaine notes raise 'Double drawing (open question for the orchestrator)' for 1210-1458; pale-of-calais is founded 1347/8 on the Calais cells England gains in 1347.
   - Fix: Needs an orchestrator ruling for group eu-11/eu-10. Recommended: the dependency owns its cells. England then subtracts each dependency keyframe's region from its corrections for those years and replaces its own gains/losses of that land with vassal_start/vassal_end against the dependency slug (Ireland from 1210, Calais 1347-1558, Wales 1284-1542); for duchy-of-aquitaine (type state) choose one owner of Gascony and rename the other dossier's events. If instead the renderer is to draw the colony tint over the metropole, record that rule in notes and leave the shapes.

4. `/ledger/42`
   - What: The Treaty of Aberconwy (November 1277) moved land to Edward but the ledger has only a contest_end; no gain, no keyframe change (Cliopatria's shape changes only in 1285).
   - Why: The page the author opened: 'By the Treaty of Aberconwy in November 1277, Llywelyn was left only with the western part of Gwynedd'; 'Eastern Gwynedd was split between Edward and Llywelyn's brother Dafydd'. kingdom-of-gwynedd /ledger/55-57 record three 1277/11 losses to kingdom-of-england (conf 2-3).
   - Fix: Add a gain 1277/11 from kingdom-of-gwynedd, conf 2, region Edward's share of the Perfeddwlad (Tegeingl and Rhos: {"admin1": "Flintshire"} plus the Conwy-east part, text quoting the page), and make keyframe 20 (1279) start in 1277 with that land added (adjust), or narrow it so the 1277-1283 years carry it.

5. `/keyframe_review/54`
   - What: Keyframe 1582 ('ok', 1582-1587) keeps 33 Munster cells out of England until 1587, though the ledger ends the Desmond contest in 1583 and nothing explains their return in 1588; in 1584-1587 nobody holds them.
   - Why: /ledger/90-91: 'the Earl of Desmond was killed in 1583'. earldom-of-desmond /ledger/4 dissolves 1583/11 with successor kingdom-of-england, land Munster ('forfeit to the English Crown'). Keyframe 55 (1588) says 'Munster back after the rebellion'.
   - Fix: Mark keyframe 54 adjust for 1582-1583 and keyframe 55 adjust from 1584 (the 1579/1588 shape), or add a gain 1583/11 from earldom-of-desmond (region Munster) and shorten keyframe 54 to 1582-1583.

6. `/keyframe_review/7`
   - What: Keyframe 1015 draws the halved kingdom from 1015, while the loss that halves it is dated 1016/10 (/ledger/20); the note itself says the shape 'is too early for 1015'.
   - Why: Keyframe 7 note: 'It is too early for 1015, when Edmund still fought in the Midlands'; Cnut page: partition after Assandun (1016).
   - Fix: Mark keyframe 6 (980) adjust for 980-1015 with the shape unchanged, and start keyframe 7 in 1016 (1016 only).

7. `/ledger/58`
   - What: The Breton holding is a direct gain of 1344 (conf 1) ended by a 1402 loss to kingdom-of-france (/ledger/67, conf 1) whose region contains the 22 Breton cells; the duchy-of-brittany dossier has an English occupation of Brest 1343-1397 at conf 3.
   - Why: duchy-of-brittany /ledger/12: 'A large permanent English garrison was held at Brest' (1343); /ledger/17: 'In 1397, Duke John IV finally managed to extricate Brest from English control'.
   - Fix: Replace /ledger/58 by occupation_start 1343 counterpart duchy-of-brittany and add occupation_end 1397 with the same counterpart and region; take the Breton cells out of /ledger/67's region (intersect with France) and mark keyframes 33 (1395) and 34 (1402) adjust so Brittany leaves in 1397.

8. `/ledger/60`
   - What: The Desmond vassalage starts in 1352 (Cliopatria's year, conf 1) and the Ulster vassalage (/ledger/55) in 1326 (conf 1), while the counterparts' dossiers date the earldoms' creation from England to 1329 and 1263.
   - Why: earldom-of-desmond /ledger/0: 'Maurice was created Earl of Desmond by Letters Patent' 27 August 1329, predecessor kingdom-of-england; earldom-of-ulster /ledger/0: 'Granted the earldom in 1263', predecessor kingdom-of-england.
   - Fix: Move vassal_start earldom-of-desmond to 1329/8 and vassal_start earldom-of-ulster to 1263 (or 1264, within a year), regions = those dossiers' first keyframes; keep the 1326 and 1352 Cliopatria cell changes as losses (to Gaelic Irish lordships) if they stay. Re-sort the ledger.

9. `/ledger/108`
   - What: The Irish contest closes 1649/5 at conf 1 while the irish-catholic-confederation dossier closes its contest with England at the Cessation of Arms, 15 September 1643 (conf 3).
   - Why: irish-catholic-confederation /ledger/2: 'The Confederates and Royalists signed a truce, or Cessation of Arms' (15 September 1643).
   - Fix: Date /ledger/108 1643/9 with the ICC's page or say in the note why the king's contest continues to 1649.

10. `/ledger/103`
   - What: The Civil War contests of 1642-1648 (/ledger/103-106) and the war's belligerents use counterpart commonwealth-of-england, a state whose dossier begins on 19 May 1649.
   - Why: commonwealth-of-england identity.start 1649/5; the Commonwealth page dates the state 1649-1660.
   - Fix: Use a counterpart alive in 1642-1648: a free-text 'Parliamentarians (Long Parliament)' in all four events and the war, or ask eu-11-x for a rebel dossier; keep the 1649 merge with commonwealth-of-england.

11. `/ledger/65/region`
   - What: The 1385 loss to kingdom-of-france is Cliopatria 1384 minus 1385, which also holds 6 Irish cells; likewise /ledger/46 (1294) holds 2 British cells.
   - Why: Cell diff of the Cliopatria shapes: 1384->1385 loses 75 French and 6 Irish cells; 1293->1294 loses 18 Gascon and 2 British cells.
   - Fix: Intersect both regions with {"country": "France"} and put the Irish cells in a separate conf-1 loss (Gaelic Irish lordships) or drop them.

12. `/keyframe_review/12`
   - What: England keeps the five-cell Hastings-Pevensey bridgehead for 1066-1071 while duchy-of-normandy /ledger/10 gains it from kingdom-of-england in 1066/10 and keeps its 1066 Cliopatria shape; the contest also ends 1066/12 here and 1071 there.
   - Why: duchy-of-normandy /ledger/10-11; England keyframe 12 note ('Neither piece is lost for 1066-1071').
   - Fix: Agree with the Normandy author (eu-10): either England loses the bridgehead 1066/10 (loss, duchy-of-normandy) or Normandy drops its gain; align the contest_end year.

## Thin (gap-filler)

- `/ledger (30 confidence-1 events)`: Pages for the Irish steps 1236, 1250, 1272, 1326, 1395, 1540, 1547, 1552, 1556, 1564, 1579, 1600 (Cliopatria's years, page silent). Try https://en.wikipedia.org/wiki/Gaelic_resurgence
- `/ledger/46`: The 1294-1303 Gascon war: the 1294 confiscation and the 1303 Treaty of Paris restitution (no regain event; keyframes 22-24 keep Gascony reduced). Try https://en.wikipedia.org/wiki/Gascon_War
- `/ledger (1224-1324)`: Poitou and La Rochelle lost 1224 (France /ledger/19), the Treaty of Paris 1259, the Agenais 1279, the War of Saint-Sardos 1324 (duchy-of-aquitaine /ledger/11,13,16). Try https://en.wikipedia.org/wiki/Treaty_of_Paris_(1259)
- `/ledger/63-65,67,72-73`: Caroline-war and Lancastrian-war dates for the 1375, 1385, 1402, 1429, 1431 French cells (1375 against France's 1380 and Aquitaine's 1377). Try https://en.wikipedia.org/wiki/Caroline_War
- `/ledger (1313-1482)`: Isle of Man 1290-1399 (Scotland /ledger/10-19, isle-of-man 1346/1399) and Berwick 1296, 1318, 1333, 1461, 1482. Try https://en.wikipedia.org/wiki/Berwick-upon-Tweed
- `/ledger (1318-1357)`: The 1318-1328 border war and the Treaty of Edinburgh-Northampton (1 May 1328, on the page already opened), and the Second War of Scottish Independence with Balliol's 1334 cession of the southern counties. Try https://en.wikipedia.org/wiki/Second_War_of_Scottish_Independence
- `/ledger (1400-1409)`: Glyndwr's rising, if Wales stays direct English land (glyndwr-s-wales is drawn against principality-of-wales). Try https://en.wikipedia.org/wiki/Glynd%C5%B5r_rising
- `/ledger (1513-1662)`: Tournai 1513-1519, Boulogne 1544-1550, the Rough Wooing occupation of southern Scotland 1547-1550, Dunkirk 1658-1662. Try https://en.wikipedia.org/wiki/Rough_Wooing
- `/keyframe_review/68`: The two Barcelona-area cells of the 1706 shape (author flagged, unverified: page budget); they are also in /ledger/111 and successors[0].land. Try https://en.wikipedia.org/wiki/Siege_of_Barcelona_(1705)
- `/ledger/8,9,15,10`: End years of the Eamont vassalages (Strathclyde 937, Gwynedd 939, Seisyllwg 959) and the 947 Cornish cells. Try https://en.wikipedia.org/wiki/Hywel_Dda
- `/ledger/100`: Date of the Scots' withdrawal from Northumberland and Durham (1641). Try https://en.wikipedia.org/wiki/Treaty_of_London_(1641)

## Spot checks

- `/ledger/3` (https://en.wikipedia.org/wiki/%C3%86thelstan): confirmed: 'at Eamont, near Penrith, on 12 July 927', Constantine II of Alba, Hywel Dda and Ealdred 'accepted Æthelstan's overlordship' (/ledger/5 confirmed on the same page)
- `/ledger/16` (https://en.wikipedia.org/wiki/Lothian): confirmed: Edgar 'granted Laudian to Kenneth II, King of Scots in 973'; 'widely accepted ... the point at which Lothian became part of Scotland'
- `/ledger/49` (https://en.wikipedia.org/wiki/First_War_of_Scottish_Independence): confirmed: 'By July, John was deposed'; 'in effect, ruler of Scotland' (also /ledger/47 March 1296, /ledger/50 11 Sep 1297, /ledger/51 22 Jul 1298, /ledger/52-53 Feb 1304, /ledger/54 1314)
- `/ledger/79` (https://en.wikipedia.org/wiki/Hundred_Years%27_War): confirmed: Castillon 17 July 1453, 'Bordeaux fell to the French on 19 October' (also /ledger/59 1347, /ledger/61 8 May 1360, /ledger/68 22 Sep 1415, /ledger/69 1417, /ledger/70 19 Jan 1419, /ledger/75 1449, /ledger/77 30 Jun 1451, /ledger/78 23 Oct 1452); the page has no 1375 event (/ledger/63-64 rightly conf 1)
- `/ledger/97` (https://en.wikipedia.org/wiki/Tudor_conquest_of_Ireland): confirmed: 'by 1603 the entire country was under English rule'; Mellifont 'signed mere days after the death of Elizabeth I'
- `/ledger/45` (https://en.wikipedia.org/wiki/Conquest_of_Wales_by_Edward_I): confirmed for year and land (Statute of Rhuddlan 1284, 'annexed and united' to the crown), but the page adds 'although they did not become part of the Kingdom of England' and 'incorporated into the new Principality of Wales': the event type is wrong (see fixes)
- `/ledger/86` (https://en.wikipedia.org/wiki/Kingdom_of_England): confirmed: 'Calais ... was lost in 1558' (year only, no month on this page); /ledger/107 19 May 1649 and /ledger/111 'Union with Scotland: 1 May 1707' also confirmed

## Cross-dossier matrix (mismatches and missing mirrors)

- kingdom-of-england 927 vassal_start kingdom-of-gwynedd -> missing: kingdom-of-gwynedd ledger has no 927 vassal_start with kingdom-of-england (its 10th-century events are 942 and 950 against kingdom-of-seisyllwg). Route to the Gwynedd author.
- kingdom-of-england 939 vassal_end kingdom-of-gwynedd -> missing: No mirror in kingdom-of-gwynedd (see 927).
- kingdom-of-england 1066 contest_end duchy-of-normandy -> mismatch: duchy-of-normandy /ledger/10 gains the five-cell Hastings-Pevensey bridgehead from kingdom-of-england in 1066/10 and closes the contest in 1071; England keeps the bridgehead in its 1066-1071 keyframe (adjust) and closes the contest 1066/12. The five cells are drawn by both 1066-1071.
- kingdom-of-england 1236 gain kingdom-of-connacht -> mismatch: Connacht /ledger/2 (conf 3) loses Connacht in 1235 to lordship-of-ireland, and lordship-of-ireland /ledger/7 gains it in 1235; England gains it in 1236 at conf 1. Land claimed twice (England direct and the Lordship colony).
- kingdom-of-england 1272 loss kingdom-of-connacht -> missing: kingdom-of-connacht has no 1272 gain (its next event is the 1474 dissolve).
- kingdom-of-england 1284 gain kingdom-of-gwynedd -> mismatch: Gwynedd dissolves 1283/6 naming kingdom-of-england as successor, but principality-of-wales /ledger/0 is founded 1283 from kingdom-of-gwynedd on the same land, and the Conquest of Wales page says the Rhuddlan lands did not become part of the Kingdom of England. Double claim 1284-1541.
- kingdom-of-gwynedd 1277 loss kingdom-of-england -> missing: Gwynedd /ledger/55-57 (1277/11, conf 2-3) lose the Perfeddwlad, the tributary lands and Builth to England by the Treaty of Aberconwy; England has only a contest_end (/ledger/42) and no gain. The page England opened says eastern Gwynedd was split between Edward and Dafydd.
- kingdom-of-gwynedd 1211 loss kingdom-of-england -> missing: Gwynedd 1211 loss, 1212 gain, 1241/8 loss, 1256/12 gain against England have no mirror in England (Cliopatria England shapes do not move in Wales 1210-1284).
- kingdom-of-england 1294 loss kingdom-of-france -> mismatch: kingdom-of-france has no 1294 gain; duchy-of-aquitaine /ledger/14-15 has a French occupation 1294/5-1303/5. England has no 1303 restitution.
- kingdom-of-scotland 1313 gain kingdom-of-england -> missing: Scotland /ledger/10,12,13,17 (Isle of Man 1313 gain, 1314 loss, 1317 gain, 1333 loss, conf 2-3) and /ledger/15 (Berwick 1318 gain), /ledger/22 (Berwick 1482 loss) have no mirror in England; author acknowledges (no page opened).
- isle-of-man 1346 found kingdom-of-england -> missing: isle-of-man is founded 1346 from kingdom-of-england and dissolves 1399 into it; England has no 1346 loss/split and no 1399 gain, and its shapes carry Man only 1285-1293, 1326-1332, 1402-1414 and from 1662.
- kingdom-of-england 1326 vassal_start earldom-of-ulster -> mismatch: earldom-of-ulster is founded 1263 with predecessor kingdom-of-england; England starts the vassalage in 1326 (conf 1, Cliopatria year). 63 years apart.
- kingdom-of-england 1326 loss kingdom-of-leinster -> missing: kingdom-of-leinster has no 1326 gain from England (its later event is a 1375 gain from lordship-of-ireland).
- kingdom-of-england 1344 gain duchy-of-brittany -> mismatch: Brittany /ledger/12 (conf 3): English garrison at Brest from 1343 as an occupation; England records a direct gain in 1344 (conf 1).
- kingdom-of-england 1402 loss kingdom-of-france -> mismatch: The 1402 loss region (Cliopatria 1401 minus 1402) holds the 22 Breton cells, but Brittany /ledger/17 (conf 3) has Brest returned to the Duke of Brittany in 1397, not to France.
- earldom-of-desmond 1329 found kingdom-of-england -> mismatch: Desmond is founded 27 Aug 1329 from kingdom-of-england (and /ledger/1 loses Dunamark to England 1331); England starts the Desmond vassalage in 1352 (conf 1, Cliopatria year) and has no 1331 gain.
- kingdom-of-england 1375 loss kingdom-of-france -> mismatch: France gains the Brétigny lands 1380/9 (conf 2), duchy-of-aquitaine loses them 1377 (conf 2), England 1375 (conf 1, Cliopatria year). The Hundred Years' War page gives only 'by the time Charles V died in 1380, the English held only Calais and a few other ports'.
- kingdom-of-england 1385 loss kingdom-of-france -> missing: No 1385 gain in kingdom-of-france; region also includes 6 Irish cells.
- kingdom-of-england 1415 gain kingdom-of-france -> missing: France has no 1415 loss (Harfleur, 22 September 1415, confirmed on the Hundred Years' War page).
- kingdom-of-england 1417 gain kingdom-of-france -> mismatch: France treats 1417 (Caen) as contest_start, England as a gain.
- kingdom-of-england 1420 gain kingdom-of-france -> mismatch: Treaty of Troyes lands: England 1420 (conf 2), France 1422/10 (conf 2). Two years apart.
- kingdom-of-england 1429 gain kingdom-of-france -> missing: No mirror in France (conf 1 on England's side).
- kingdom-of-england 1431 loss kingdom-of-france -> missing: No mirror in France (conf 1 on England's side).
- kingdom-of-england 1451 loss kingdom-of-france -> mismatch: France models Bordeaux 1451-1453 as a contest (no gain until 1453); England has loss 1451/6, gain 1452/10 (no France mirror), loss 1453/10.
- kingdom-of-france 1224 gain kingdom-of-england -> missing: France /ledger/19 (conf 3) conquers Poitou, La Rochelle, Limousin, Perigord and Quercy from England in 1224; England has no 1224 loss.
- kingdom-of-england 1649 contest_end irish-catholic-confederation -> mismatch: ICC closes its contest with England at the Cessation of Arms, 15 September 1643 (conf 3); England closes it 1649/5 (conf 1).

Matched: Wessex 927, Norman England 1072, Angevin Empire 1210, the four Scottish occupation events 1296-1314, France 1347/1360/1419/1435/1449-1450/1453/1558, Principality of Wales 1542, Desmond 1583, Ulster 1333, Irish Catholic Confederation 1642, Commonwealth 1649 and 1660. Exceptions: counterparts without a dossier yet (danelaw, kingdom-of-northumbria, kingdom-of-alba, strathclyde, kingdom-of-seisyllwg, cornwall, kingdom-of-denmark, north-sea-empire, denmark-england, kingdom-of-great-britain, first-barons-war-rebels) and free-text Irish counterparts.

## For the orchestrator

- Orchestrator ruling needed (eu-11 and eu-10): five dependency dossiers (lordship-of-ireland, kingdom-of-ireland, pale-of-calais, principality-of-wales, duchy-of-aquitaine) draw land that kingdom-of-england also draws as direct territory, 1210-1707. Either England subtracts them and carries vassal events, or the renderer lets the colony tint win; duchy-of-aquitaine (type state) and England cannot both own Gascony.
- kingdom-of-england has no land of its own in 1018-1041, 1072-1209 and 1649-1659 by design (north-sea-empire, denmark-england, norman-england, angevin-empire, commonwealth-of-england draw it); north-sea-empire and denmark-england have no dossier yet, so 1018-1041 is blank until they exist.
- France /ledger/17-18 models Louis's 1216-1217 invasion as a France-England contest while England uses a rebel counterpart (first-barons-war-rebels, no dossier): one model should be chosen.
- deheubarth (920-1283) and the undrafted kingdom-of-seisyllwg (Cliopatria 878-959) overlap for Hywel Dda's realm; England and Gwynedd both use kingdom-of-seisyllwg.
- Reviewer applied one fix in place (/ledger/49 region text) and re-validated (0 errors); no page failed to load.
