# Review of batch eu-09-a (2026-10-24, adversarial reviewer)

Dossiers: duchy-of-bavaria, county-of-brabant, county-of-holland. The validator found 0 errors in all three; its warnings are counterpart slugs that have no dossier yet and four gazetteer names (Innviertel, Neuburg an der Donau, Kufstein, Freising). None of the neighbour dossiers in section 6 of the author's brief exists yet, so every mirror outside the batch counts as an exception (group not run yet). No infobox gives an area (Duchy of Bavaria, Electorate of Bavaria, Duchy of Brabant and County of Holland pages all read), and the authors say so.

Verdicts: duchy-of-bavaria **thin**, county-of-brabant **thin** (one small fix applied by the reviewer), county-of-holland **thin**. I found no fabricated or mis-dated confidence-3 event: 20 events were checked on 9 pages.

## duchy-of-bavaria (thin)

What I tried and could not break: all 32 Cliopatria shapes are reviewed, and the 9 new keyframes carry from, to and a correction. The ledger is in order. Munich lies inside every bbox. Cliopatria's lumps (Brandenburg and Tyrol in 1352-1362, Brandenburg and the Dutch counties in 1363-1384, the Dutch counties in 1385-1449, Luxembourg in 1422-1428) are explained and corrected under one stated rule. Nine events were confirmed with their year:
- Pavia 1329 (Duchy page)
- Lower Bavaria 1340 and Tyrol 1342 (Louis IV page)
- Baden 1714, the Palatinate union of 30 December 1777, the French in 1792 and Lunéville on 9 February 1801 (Electorate page)
- Tyrol and Vorarlberg, and Augsburg, on 26 December 1805 (Pressburg page)

Not faults:
- The Upper Palatinate gain is dated 1623 while Cliopatria draws it from 1622; the keyframe note says so.
- Tyrol and Vorarlberg are in the ledger in December 1805 but not in the 1805 outline; the note says so.

Thin (for a gap-filler):
1. /keyframe_review/24 (1632-1635): the outline drops 20.4 k km2, namely the Upper Palatinate north of 49.25 N and a strip west of 10.45 E. The ledger only hatches Munich, which lies inside the outline that is kept, and the end in 1635 is confidence 1. Find what the Swedes held and when they left (Nördlingen, 1634). Then mark the keyframe adjust to the 1626 outline with a hatched occupation, or make the occupation region the 1626-minus-1632 difference. Page to try: Swedish intervention in the Thirty Years' War.
2. /keyframe_review/40 (1805): the outline is 8.6 k km2 smaller and the ledger has no Würzburg cession. The Pressburg page gives Würzburg to the Salzburg elector, and the Electorate page says "Würzburg, obtained in 1803, was to be ceded by Bavaria to the elector of Salzburg in exchange for Tyrol". Add a loss in 1805-12 to electorate-of-salzburg (confidence 2), symmetric with the Tyrol gain.
3. /ledger/20 and /ledger/22: the western strip of 1702-1705 is confidence 1. The Electorate page names no seizure (I read it). Try the Maximilian II Emanuel page for Ulm.
4. /ledger/21: the occupation start in 1704 is confidence 1, because the Ilbersheim date is not on the page.
5. /ledger/1: the 1268 Conradin inheritance is in Swabia on the page, but in the Nordgau and Palatinate by the cells (the author flagged this). Try the Conradin page.
6. Small unexplained outline changes in 1279 (-0.4 k km2) and 1791 (-1.8 k km2).

## county-of-brabant (thin; one fix applied)

Applied by the reviewer: /ledger/1, the contest start. It was June 1288 and the note said "The page dates no earlier campaign". The Battle of Worringen page says "Between 1283 and 1288, the conflict was delayed by several smaller confrontations between both sides" and dates the claim's sale to John of Brabant to "September 1283". I moved the event to September 1283, rewrote the note, and changed /wars/0 to from 1283 with the name "War of the Limburg Succession (Battle of Worringen)". It re-validated with 0 errors.

Confirmed: Limburg 1289 and Guelders' renunciation (Worringen page), Anthony's accession in 1406 (Anthony page), and the 1430 inheritance (Duchy of Brabant page).

Thin:
1. /keyframe_review/5, /ledger/4 and /ledger/6: the 1402-1414 strip (4.25-4.57 E, 49.5-49.8 N) is the County of Rethel. Rethel is at 4.37 E, 49.51 N. The Anthony page that these events cite opens with "was Count of Rethel (1402–1406), Duke of Brabant, Lothier and Limburg (1406–1415)", and its table gives Rethel 1402-1407. So the notes' "page silent" is wrong. Rethel was a French fief that Anthony held before he became duke, never Brabant. To fix:
   - Set /keyframe_review/5 to verdict adjust with the correction {cliopatria: County of Brabant, year: 1305}.
   - Delete /ledger/4 and /ledger/6.
   - Cite the Anthony page in the keyframe note.
2. /wars/1: the Treaty of Ath, which gave Antwerp and Mechelen to Flanders, is undated, and so is Antwerp's return. Try War of the Brabantine Succession.

## county-of-holland (thin)

Confirmed: 1299 (Hainaut page: Jean II, and "Hainaut, Holland and Zeeland: 1299–1356"), 1345 (Louis IV page) and 1433 (Holland page). The 1363-1432 keyframe takes back exactly the land that duchy-of-bavaria removes.

Thin:
1. /keyframe_review/0: the 1260 outline holds West Friesland. The Holland page that the note quotes has the counts' "150-year-long war against the inhabitants of the area living at the east side of North Holland", and "It was not until 1289 that Count Floris V was able to bring this long war to an end". Correct keyframe 0 for 1260-1288 without West Friesland, and add a 1289 gain (counterpart nobody). West Friesland is a gazetteer name to add.
2. Burgundian "effective control" from 1428 and the Treaty of Delft are not entered. A vassal or occupation pair with duchy-of-burgundy for 1428-1433 may be due. Try the Jacqueline of Hainaut page.
3. Zeeland was shared with Flanders, per a footnote on the Holland page. The date is not given.

## Cross-dossier notes for the orchestrator

- Bavaria and Holland agree on the Dutch counties for 1363-1432. For 1433-1449 nobody draws them until duchy-of-burgundy (eu-10) takes Holland from 1433 (and Brabant from 1430).
- Luxembourg is removed from Brabant for 1415-1421 and from Bavaria for 1422-1428. duchy-of-luxembourg (eu-09) must cover 1411-1428.
- house-of-wittelsbach (eu-09) must run to 1339, or Lower Bavaria is nobody's in 1333-1339.
- margraviate-of-brandenburg (eu-09) must remove Bavaria from its shapes for 1326-1351.
- electoral-palatinate (eu-09-x) must end or stop drawing in December 1777, the Bavarian union. The 1505 Neuburg loss is Palatinate-Neuburg, a separate principality.
- The French occupation pair 1792-1801 names french-first-republic, whose row ends in 1795. eu-20 must carry it through the Directory and the Consulate.
- county-of-hainaut, if written, must leave out the 3.8 k km2 round Mons that the Holland outline holds for 1299-1433.
