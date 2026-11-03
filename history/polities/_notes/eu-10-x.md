# eu-10-x (France, additions batch): what could not be settled

Ten new dossiers, all new states (`cliopatria_names: []`, every keyframe `adjust` with a new `shape_id`), all validate with 0 errors:
royal-domain-of-france (987-1620), burgundian-state (1363-1482), county-of-provence (947-1481), catholic-league-france (rebel, 1588-1598), duchy-of-bar (1033-1480), pale-of-calais (colony, 1347-1558), duchy-of-berry (1360-1416), duchy-of-orleans (1392-1498), county-of-ponthieu (926-1477), county-of-la-marche (958-1527).
140 ledger events, 41 sources. Every source is a Wikipedia page opened with WebFetch in this run. Each dossier's own `notes` field carries the per-state detail; this file lists what the next reader has to act on.

## Layers over Cliopatria rows (the compile must draw these on top)

- royal-domain-of-france is the lands the king held directly. It sits inside the Cliopatria Kingdom of France (990-1791), which also draws fiefs and apanages. Same treatment as duchy-of-francia.
- burgundian-state is a composite of the Duchy of Burgundy (1003-1481), Flanders to 1384, Brabant to 1430, Holland to 1362, Luxembourg 1429-1449 and the Free County of Burgundy 1333-1384. The compile should let it win where both exist.
- duchy-of-berry, duchy-of-orleans, county-of-ponthieu, county-of-la-marche are carve-outs of the royal domain or of the holder's land. Ponthieu and La Marche are drawn whole for their whole life; holder changes are `rename` events and the holders' dossiers carry the gains and losses.
- catholic-league-france is a rebel carve-out of kingdom-of-france. The Kingdom of France dossier has no matching loss events for 1588-1598.
- pale-of-calais is a colony of kingdom-of-england (family britain).

## Page problems

- `List_of_counts_of_Provence`: does not exist. `List_of_rulers_of_Provence` was used instead.
- Philippe Emmanuel de Lorraine, Duke of Mercoeur: the URL with the oe ligature failed; the percent-encoded `Philippe_Emmanuel,_Duke_of_Merc%C5%93ur` worked.
- Crown lands of France: the page has no infobox, and the first summary quotes of its rows were paraphrases. The royal-domain events were re-checked against a second fetch and now quote the page's own entries (1191, 1200, 1225, 1237, 1241, 1271, 1284, 1308, 1336, 1392, 1477, 1498, 1532). One error found in that check and fixed: 1498 does not "return" Blois. The page says "the county of Blois is integrated into the royal domain for the first time", so royal-domain-of-france has a separate 1498 Blois gain (shape: the last Cliopatria County of Blôis shape, 1395-1401) and duchy-of-orleans no longer claims Blois or Comminges. [Repair 2026-10-25: the reviewer showed that the Duke of Orléans was Count of Blois from 1397 on the same page, so the 1498 gain now names duchy-of-orleans.]

## Where pages disagree (the year used is the cited page's)

- Ponthieu: Crown lands page has 'conquest' in 1336 and a gift to England in 1360. The Ponthieu page has Eleanor of Castile in 1279, confiscation in 1294, Edward III in August 1346, Brétigny in 1360 and Charles V's conquest in April 1369, with no 1336 event. royal-domain-of-france draws the page-dated 1336, 1360, 1369, 1435 and 1477 changes of its own.
- La Marche / Angoulême: the Crown lands page has the 1308 purchase of Angoulême, Fougères and Lusignan from Yolande of Lusignan; the La Marche page calls 1308 a seizure on Count Guy's death. Two events, two counterparts.
- Burgundian State: Hainaut/Holland/Zeeland 1432 or 1433; Luxembourg 1441 or 1443; Namur 1421 bought or 1429 inherited; Flanders 1384 or 1382; the Burgundy apanage 1363 (Burgundian State, Philip the Bold) or 1364 (Crown lands).
- Brétigny: drafted 8 or 10 May 1360, ratified at Calais 24 October 1360. The loss is placed in October.
- Catholic League: Henry IV's welcome in Paris 27 February 1594 (League page) or 22 March 1594 (War of the Three Henrys); Henry III's death July / August / 1 August 1589.
- Pale of Calais: 8 January 1558 (Pale page) or 1-7 January (siege page).
- Provence: the Rulers list names Ramon Berenguer I in its table and Ramon Berenguer III in its text for the 1112 marriage. Rulers therefore start at 1112 with no earlier strip. The County page ends the state in 1486/1487; this dossier ends it in December 1481 so that the royal domain (Crown lands, 1481) and Provence do not both hold the land.

## Confidence 1 ("page silent") events

- burgundian-state 1463 loss: Philip gives up land to Louis XI, the page names none.
- burgundian-state 1477 loss: Upper Alsace, no page opened dates its fate.
- catholic-league-france 1594 loss (Normandy) and 1596 loss (Aix): pages silent on when they returned.

## Resolution warnings

Unknown places in the gazetteer: Montargis (royal-domain Gâtinais), Abbeville (royal-domain Ponthieu, county-of-ponthieu), Boulogne-sur-Mer (royal-domain 1478, burgundian-state). Radii are 30-40 km round them, so the map is right once they are added. County/department names (Eure, Eure-et-Loir, Charente, Gard, Hérault, Aude, Meuse, Creuse, Haute-Vienne, Ardennes) resolved without warning.

## Counterpart slugs with no dossier (new-state candidates)

No Cliopatria row and no dossier (the validator warns on the first four): county-of-sens (1055), viscounty-of-bourges (1101), county-of-chartres (1284) in royal-domain-of-france; county-of-forcalquier (1246) in county-of-provence. "County of Namur" and "Duchy of Guelders" are free-text counterpart names in burgundian-state; neither has a Cliopatria row or a dossier, and County of Hainaut is used there only as a region name. They belong to the Low Countries group (eu-09).
Cliopatria row but no dossier (fine as they stand): county-of-blois (its last shape, 1395-1401, is the land of the 1498 gain), county-of-boulogne, county-of-champagne, county-of-flanders, county-of-nevers, duchy-of-burgundy, free-county-of-burgundy, county-of-savoy, kingdom-of-england, kingdom-of-majorca, angevin-empire.

## Not covered (brief scope, left for a later batch)

- Three Bishoprics (Metz, Toul, Verdun) and Lorraine's transfers to France: not written. The Duchy of Bar dossier covers only the Bar part.
- Landgraviate of Upper Alsace and the Alsace transfers of 1648/1681: not written; the Burgundian State carries the 1469-1477 pledge only.
- Plantagenet / Angevin holdings and the English Aquitaine: other groups' dossiers; the royal domain records the Brétigny cession and the reconquest as events against kingdom-of-england.
- Wars of Religion beyond the League: Huguenot zones (Cliopatria 1622-1631) are already in the dataset; the League's land coverage here is thin (Paris, Dijon, Normandy, Aix, Nantes only). A gap-filler should open Siege of Rouen (1591-1592), Siege of Paris (1590) and the Sainte Union city lists.
- Also not drawn: County of Bigorre, Principality of Dombes, Auxerre, Nemours, Valois, Perche, Comminges (1462-1498), the Comtat Venaissin (named in the 1271 Crown lands entry; half ceded 1274), Touraine in 1361, the Burgundy gain of 1034.

## Resolution limits

- pale-of-calais: the infobox area is about 52 km2; the grid's smallest resolvable shape is about 500 km2 (a 15 km disc), the gazetteer region about 1,500 km2. The compile should draw a one- or two-cell exclave.
- duchy-of-bar: drawn as the department of Meuse in one keyframe; the county also held land east of the Meuse and 13th-15th century acquisitions the pages do not give.
- Kingdom of France lacks a `vassal_start` for duchy-of-bar (Treaty of Bruges, 1301).

## Repair pass 2026-10-25 (reviewer verdict fail on royal-domain-of-france)

Only royal-domain-of-france was touched (63 events, 16 sources, 46 keyframes, 0 errors, 57 warnings: 54 unknown places, 3 counterparts without dossiers). The counterpart dossiers (verdicts fix or thin) were left as they are, so the mirror events they lack are listed below instead of written. Five pages opened in this pass: Duchy of Anjou, County of Vermandois, Charles VII of France, Counts and dukes of Angoulême, Arthur III Duke of Brittany (silent on Paris); Treaty of Troyes and Crown lands of France were read again. The reviewer's suggested https://en.wikipedia.org/wiki/County_of_Angoul%C3%AAme does not exist (url_not_found); the "Counts and dukes of Angoulême" article was used.

### What changed in royal-domain-of-france
- Anjou and Maine: 1225 loss removed. Now 1246 loss to capetian-house-of-anjou (Duchy of Anjou page), 1328 regain from county-of-anjou (same page; Maine from the Crown lands bullet that follows its 1322 entry and has no year of its own), 1360-10 loss to house-of-valois-anjou (letters patent of 25 October 1360), 1480-7 regain of Anjou (René d. 10 July 1480), 1481-12 regain of Maine (Crown lands 1481).
- Paris: 1418 loss to burgundian-state removed (burgundian-state never draws Paris). Loss to kingdom-of-england on 21 May 1420 (Troyes), regain in 1436 (Charles VII page, year only); capital_move moved to 1436.
- Arras 1435: loss widened to Ponthieu (Abbeville), the Amiens disc, Vermandois (Péronne disc plus the rest) and Auxerre, counterpart burgundian-state. Ponthieu returns in 1477 (counterpart county-of-ponthieu, whose dissolve event is the mirror); the rest returns in 1482-12 with Burgundy and Picardy (counterpart burgundian-state, mirror of its /ledger/19).
- Vermandois split to match county-of-vermandois: Péronne disc 1191, the rest 1213. Auxerre disc bought 1371 (new event) and subtracted from the County of Sens (Yonne) before that.
- Counterparts corrected: 1364 and 1482 Burgundy to burgundian-state; 1498 Blois to duchy-of-orleans; 1223 Artois to kingdom-of-france (the heir's own land); 1481 Provence split off with counterpart county-of-provence (region copied from county-of-provence /ledger/8).
- Angoumois (Charente) regained 1531 (Counts and dukes of Angoulême: "Louise (1515-1531)" then "Royal domain").
- Notes added on the Cliopatria rows that disagree with the Crown lands dates: County of Vexin 990-1084 (the Crown lands entry is 1077), County of Poitou 1206-1249 (gain 1223, loss 1241), Dauphiné 1260-1351 (sale 1343-1349).
- All keyframes regenerated from the ledger (the 1225, 1418 and 1435 cuts moved; new cuts at 1213, 1246, 1328, 1371, 1420, 1436, 1480, 1531).

### Where I disagree with the reviewer, and why
- Crown lands "reunited" bullet: the reviewer places it at Philip VI's accession. The page gives that bullet no year (it follows the 1322 entry). The year 1328 is the Duchy of Anjou page's ("Anjou itself was united to the royal domain again in 1328, but was detached in 1360").
- Louis I of Anjou: the Duchy page dates his countship to 22 August 1350 and the letters patent to 25 October 1360; house-of-valois-anjou /ledger/0 founds the house in 1356 (Louis I page). The loss is placed at the letters patent (1360-10) as the reviewer asked; the 1356 vs 1350 conflict is for that dossier's owner. Philip VI's gift of Anjou to John the Good (17 February 1332) is not drawn.
- Paris to England in 1420: the Troyes page says Paris was under Burgundian control since May 1418 and that Henry V and Charles VI entered it together on 1 December 1420; it does not say England took it. Date and place are the page's, the holder is my reading (confidence 2).
- Ledger /44 (Abbeville 1477): the reviewer offered a 1477 loss in burgundian-state or a move to 1482. I took a third route that needs no change there: counterpart county-of-ponthieu (dissolves into the royal domain in 1477), because the County of Ponthieu page ("In 1477 Ponthieu was reconquered by King Louis XI") and the Crown lands page both say 1477.
- Charente: the reviewer says "back in 1515". The Angoulême page keeps the duchy with Louise of Savoy to 1531 and lists "Royal domain" only after her, so the gain is 1531.
- Cliopatria neighbour dates: the reviewer's years (Vexin 1082, Poitou 1205-1271) differ from data/polities.csv (Vexin 990-1084, Poitou 1206-1249). The csv values are in the notes.
- Arthur III page (tried for the April 1436 recapture): silent. The Charles VII page gives 1436 only; no month.

### Not done (and who has to do it)
- duchy-of-orleans (thin, not touched): no Blois land. Louis I was Count of Blois from 1397 (Crown lands 1392 entry), and royal-domain's 1498 Blois gain now names duchy-of-orleans, so that dossier needs a 1397 gain and a 1498 hand-over.
- burgundian-state (thin, not touched): its keyframes drop the Somme in 1463 (confidence 1, no land named) and never return it, so from 1463 to 1481 neither dossier draws the Amiens and Vermandois land. It needs the 1465 return (Treaty of Conflans) or royal-domain a 1463 regain; no opened page dates either. It also records the 1477 January contest with kingdom-of-france but royal-domain-of-france has no mirror contest events (no opened page gives the royal side's campaign).
- Touraine to Philip in 1361 (Crown lands), Montpellier after 1365, the Dauphin's land 1422-1435: not drawn, because no opened page dates their return or extent.
- Counterparts without a dossier: county-of-sens, viscounty-of-bourges, county-of-chartres (earlier list), county-of-anjou (Cliopatria row 990-1332, the Valois holder before 1328), "County of Auxerre" (1371), "Duchy of Angoulême" (Angoumois, 1308-1531).
- Gazetteer: Péronne is a new unknown place (used in royal-domain-of-france, three regions); Montargis, Abbeville and Boulogne-sur-Mer as before.
