# Review of gap batch g-eu-a (Swiss and Italian gaps), 2026-11-01

Adversarial review of six new dossiers (no Cliopatria rows). Validator with --resolve: no errors; two expected slug warnings (prince-bishopric-of-sion, prince-bishopric-of-geneva). Spot checks opened Graubünden, Three_Leagues, Old_Swiss_Confederacy, Scuol, Canton_of_Valais, Seven_Tithings, Republic_of_Geneva, Duchy_of_Massa_and_Carrara, Cesare_Borgia, Romagna, March_of_Tuscany and Republic_of_Florence. No event was found fabricated; every confidence-3 event checked says what its note claims.

Verdicts: three-leagues **fail**, sieben-zenden **fail**, republic-of-geneva **fail**, duchy-of-massa-and-carrara **pass**, duchy-of-romagna **fail**, march-of-tuscany **pass**.

Main reasons for the fails: (1) the vassal_start/vassal_end events that swiss-confederation and papal-states record against three-leagues, sieben-zenden, republic-of-geneva and duchy-of-romagna have no mirror, although the author's brief listed them under 'Cited by'; (2) sieben-zenden misses four land events that the Canton of Valais page dates (1476 Évian, Thonon, Monthey; 1477 loss; 1536 regain; 1569 Treaty of Thonon), and its notes wrongly say no page dates them. No dossier was edited by the reviewer.

## three-leagues: fail

- **/ledger**: No vassal_start/vassal_end mirrors the swiss-confederation associate events that name this state: /ledger/19 (1497 vassal_start), /ledger/40 (1798-03 vassal_end), and the Valtellina tint /ledger/25 (1512), /ledger/33 (1620-07), /ledger/34 (1639-09), /ledger/36 (1797-10).  
  Why: Rule 3 (a vassal_start of X is a vassal_start in X's ledger with this state as counterpart); the author's brief listed all six under 'Cited by' and said the ledger must match them. Old Swiss Confederacy page: the Three Leagues 'became an associates of the Old Swiss Confederacy in 1497/98'. The g-eu-b review failed central-lithuania for the same omission.  
  Fix: Add vassal_start 1497 counterpart swiss-confederation, region {admin1 Graubünden}, source Old_Swiss_Confederacy, confidence 2 (page '1497/98'); add vassal_end 1799-04 (or 1798-03 to match swiss-confederation /ledger/40, saying which in the note). For the Valtellina either add vassal_start/vassal_end pairs on {admin1 Sondrio} at 1512, 1620-07, 1639-09, 1797-10 mirroring the Swiss events, or state under problems that swiss-confederation /ledger/25, 33, 34, 36 duplicate this dossier's own gains and losses and should be dropped by its owner.
- **/ledger/7** (non-blocking): The 1649 return of the Lower Engadine (confidence 2) is mis-dated: the Lower Engadine bought its freedom from Austria in 1652.  
  Why: Scuol page (chief town of the Lower Engadine): 'In 1621/1622 the village was devastated by Austrian troops; in 1652 it bought its freedom from Austria.' The Graubünden page only says 'Treaties with Austria in 1649 and 1652, brought the Müstair and Lower Engadine valleys back' without assigning years.  
  Fix: Move the Lower Engadine and Müstair circles to a 1652 gain from habsburg-monarchy citing https://en.wikipedia.org/wiki/Scuol (add it to sources[]); keep the Prättigau at 1649 (confidence 1, /ledger/8) so the ledger reads 1649 then 1652; split /keyframe_review/5 into 1649-1651 (Graubünden minus the Lower Engadine and Müstair circles, plus Sondrio) and 1652-1796.
- **/ledger/1/counterpart** (non-blocking): The 1512 gain of the Valtellina names duchy-of-milan, which did not hold it in 1512: duchy-of-milan /ledger/17 loses the duchy to kingdom-of-france in 1499 and its 1512 regain (/ledger/18) excludes the Valtellina, while kingdom-of-france /ledger/79 sends all of 'Lombardy' to duchy-of-milan in 1512.  
  Why: The author's own note: 'In 1512 Milan was French-held until the Holy League drove the French out'. Neither neighbour records the Valtellina passing to the Leagues.  
  Fix: Name kingdom-of-france as counterpart (holder 1499-1512) and say under problems that kingdom-of-france /ledger/79 should except Sondrio and add a 1512 loss of it to three-leagues.
- Thin /ledger/8: Year the Prättigau returned from Austria (confidence 1, bridged at 1649). (try https://en.wikipedia.org/wiki/League_of_the_Ten_Jurisdictions)
- Thin /ledger (1624-1637): The French occupations of the Valtellina (Coeuvres 1624-1626, Rohan 1635-1637) are not in the ledger or wars; the valley is drawn as nobody's 1620-1639 by default. (try https://en.wikipedia.org/wiki/Henri,_Duke_of_Rohan)
- Spot checks: /ledger/0 confirmed (Graub%C3%BCnden); /ledger/1 confirmed (Old_Swiss_Confederacy); /ledger/2 confirmed (Graub%C3%BCnden); /ledger/4 confirmed (Graub%C3%BCnden); /ledger/6 confirmed (Graub%C3%BCnden); /ledger/7 mis-dated (Scuol); /ledger/9 confirmed (Three_Leagues); /ledger/10 confirmed (Three_Leagues)
- Area: No infobox area on Three_Leagues; no Cliopatria row. Drawn Graubünden + Sondrio (43 cells, about 10,800 km2) against 7,105 + 3,196 km2 for the modern canton and province: consistent.

## sieben-zenden: fail

- **/ledger/1/region**: The November 1475 gain draws the whole Lower Valais down to Saint-Maurice and Monthey (25 km circle at 46.15N 7.00E intersected with Valais) at confidence 3, but the page stops at Martigny.  
  Why: Canton of Valais page: 'In November of the same year, they seized all Lower or Savoyard Valais up to Martigny.' Saint-Maurice fell in March 1476 and Monthey was held only 1476-1477 and from 1536 (next finding).  
  Fix: Redraw /ledger/1 as the Valais between the Morge of Conthey and Martigny (for example a circle at Martigny 46.10N 7.07E, about 12 km, intersected with Valais and minus a Saint-Maurice circle), and redraw /keyframe_review/1 accordingly.
- **/ledger (1476-1569)**: Four page-dated land events are missing and the notes wrongly say 'Monthey and the Chablais side are not dated by any page'.  
  Why: Canton of Valais page (already in sources[]): 'In March 1476, after the victory of Grandson, they advanced and captured St Maurice, Évian, Thonon and Monthey.' 'They had to give up the last three districts in 1477 but won them again in 1536.' 'In the treaty of Thonon in 1569, Monthey, Val-d'llliez, and Le Bouveret were permanently annexed to Valais.'  
  Fix: Widen /ledger/2 (1476-03, county-of-savoy) to Saint-Maurice, Monthey, Évian and Thonon (the Chablais east of the Dranse, about 46.38N 6.55E); add 1477 loss of Évian, Thonon and Monthey to county-of-savoy; 1536 gain of the same three from county-of-savoy; 1569 loss of Évian and Thonon to house-of-savoy (Monthey, Val-d'Illiez and Le Bouveret kept); add keyframes 1476, 1477-1535, 1536-1568, 1569-1797; correct the notes and gaps.
- **/ledger**: No vassal_start/vassal_end mirrors swiss-confederation /ledger/8 (1416 vassal_start), /ledger/15 (1475-11 vassal_start, Lower Valais), /ledger/38 and /ledger/39 (1798-03 vassal_end).  
  Why: Rule 3; the author's brief listed them under 'Cited by'. Old Swiss Confederacy page: 'Became a Zugewandter Ort in 1416 through an alliance with Uri, Unterwalden and Lucerne'.  
  Fix: Add vassal_start 1416 counterpart swiss-confederation (region as /ledger/0, source Old_Swiss_Confederacy), vassal_start 1475-11 for the Lower Valais (region as the corrected /ledger/1), and vassal_end 1798-03 for both, so each start pairs with an end.
- **/wars/0** (non-blocking): The Raron affair is dated 1414-1420 but the state's life starts in 1416.  
  Why: Rule 2: wars inside the life.  
  Fix: Start the war at 1416 with a note that the rising began in 1414 (Canton of Valais page: 'from 1414 to 1420').
- Thin /identity/start: Before 1634 the Upper Valais was nominally the Bishop of Sion's; the 1416 start and the prince-bishopric-of-sion counterpart need a dossier or page. (try https://en.wikipedia.org/wiki/Roman_Catholic_Diocese_of_Sion)
- Spot checks: /ledger/0 confirmed (Old_Swiss_Confederacy); /ledger/1 confirmed (Canton_of_Valais); /ledger/2 confirmed (Canton_of_Valais); /ledger/3 confirmed (Seven_Tithings); /ledger/4 confirmed (Seven_Tithings); /ledger/5 confirmed (Seven_Tithings)
- Area: Seven_Tithings infobox has no area; drawn Valais 21 cells (about 5,300 km2) against the canton's 5,224 km2.

## republic-of-geneva: fail

- **/ledger**: No vassal_start/vassal_end mirrors swiss-confederation /ledger/29 (1526-02 vassal_start) and /ledger/41 (1798-04 vassal_end), both naming this state.  
  Why: Rule 3; the author's brief listed both under 'Cited by'. Old Swiss Confederacy page lists 'Republic of Geneva– 1536 treaty with Bern and a 1584 treaty with Zürich and Bern' among the associates. The Swiss 1526 date also precedes this state's 1534 start.  
  Fix: Add vassal_start counterpart swiss-confederation at 1534 (the founding; or 1536 per the Old Swiss Confederacy page, said in the note) on {place Geneva, km 10}, and vassal_end 1798-04 with the annexation; under problems, ask the swiss-confederation owner to move its /ledger/29 from 1526 to the same year.
- Spot checks: /ledger/0 confirmed (Republic_of_Geneva); /ledger/1 confirmed (Republic_of_Geneva); /ledger/2 confirmed (Republic_of_Geneva); /ledger/3 confirmed (Republic_of_Geneva); /ledger/4 confirmed (Republic_of_Geneva)
- Area: No infobox area; one grid cell, acknowledged in /keyframe_review/0.

## duchy-of-massa-and-carrara: pass

Tried: every land event against the duchy page (all five confirmed with year), the 1473/1664 start choice (explained as renames), the French gap, the Lunigiana transfer (mirrored by duchy-of-modena-and-reggio /ledger/1), capital inside the shape. Remaining mismatches are on the neighbours' side and were flagged by the author.

- Thin /ledger/4: Which state held the land 1797-1805 (Cisalpine Republic, Italian Republic); cispadane-republic records no gain. (try https://en.wikipedia.org/wiki/Cisalpine_Republic)
- Spot checks: /ledger/0 confirmed (Duchy_of_Massa_and_Carrara); /ledger/3 confirmed (Duchy_of_Massa_and_Carrara); /ledger/4 confirmed (Duchy_of_Massa_and_Carrara); /ledger/5 confirmed (Duchy_of_Massa_and_Carrara); /ledger/9 confirmed (Duchy_of_Massa_and_Carrara)
- Area: No infobox area; two cells for Massa and Carrara.

## duchy-of-romagna: fail

- **/ledger**: No vassal_start/vassal_end mirrors papal-states /ledger/15 (1500 vassal_start) and /ledger/16 (1503 vassal_end), both naming this state.  
  Why: Rule 3; the author's brief listed both under 'Cited by'. The dossier's own /ledger/3 note quotes the title created 'by the Apostolic authority of Pope Alexander VI'.  
  Fix: Add vassal_start 1500 counterpart papal-states (region as /ledger/0) and vassal_end 1503 (confidence 1, as /ledger/8), and say in the note that the papal tint covers the later gains.
- **/wars/0** (non-blocking): The war runs from 1499, before the state's 1500 start.  
  Why: Rule 2: wars inside the life; Cesare Borgia page: 'Lord of Imola 1499–1503', 'Lord of Forlì 1499–1503'.  
  Fix: Start the war at 1500 with a note that the Imola campaign began in 1499, or move the start to 1499 if a page dates Imola's fall.
- Thin /ledger/8: Date the papacy took back Imola, Forlì and Cesena (confidence 1 at 1503; the fortresses were handed over later). (try https://en.wikipedia.org/wiki/Forl%C3%AC)
- Thin /ledger/9: Dissolution year (confidence 1). (try https://en.wikipedia.org/wiki/Cesena)
- Spot checks: /ledger/0 confirmed (Romagna); /ledger/1 confirmed (Cesare_Borgia); /ledger/2 confirmed (Cesare_Borgia); /ledger/3 confirmed (Cesare_Borgia); /ledger/4 confirmed (Cesare_Borgia); /ledger/5 confirmed (Cesare_Borgia); /ledger/8 confirmed (Romagna)
- Area: Duke of Romagna page has no infobox. The 1501 Faenza circle adds no cell (absorbed by the Imola circle), harmless.

## march-of-tuscany: pass

Tried: the infobox dates and capitals (Lucca to 1057, Florence 1057-1116, San Miniato), the Florence 1115/1185/1197 sequence, Lucca and Siena mirrors (matched), the duchy-of-tuscia predecessor (explained in its note). The Florence mirrors are missing on republic-of-florence's side (cross_checks).

- Thin /ledger/7: Dates for Arezzo, Pistoia, Volterra, Prato and Poggibonsi leaving the march (all held to 1197 by default). (try https://en.wikipedia.org/wiki/Pistoia)
- Thin /ledger/0: Advisory: the march is drawn sovereign 846-1197 over land that middle-franks, kingdom-of-italy-medieval and holy-roman-empire also draw; the project models few such overlord relations (march-of-verona does), so not a fault here. (try https://en.wikipedia.org/wiki/Kingdom_of_Italy_(Holy_Roman_Empire))
- Spot checks: /ledger/0 confirmed (March_of_Tuscany); /ledger/2 confirmed (Republic_of_Florence); /ledger/5 confirmed (Republic_of_Florence); /ledger/6 confirmed (Republic_of_Florence); /ledger/7 confirmed (March_of_Tuscany)
- Area: No infobox area; region Tuscany 86 cells against the modern region's 22,987 km2; the south and Lunigiana are acknowledged as unproven.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| three-leagues 1512 gain duchy-of-milan | none | mismatch | duchy-of-milan lost the duchy to kingdom-of-france in 1499 (/ledger/17) and its 1512 regain excludes the Valtellina; kingdom-of-france /ledger/79 sends 'Lombardy' to duchy-of-milan in 1512. Route: kingdom-of-france should lose Sondrio to three-leagues in 1512. |
| three-leagues 1620 loss Valtellina rebels | none | exception | text counterpart, no dossier; valley nobody's 1620-1639 |
| three-leagues 1620 contest_start kingdom-of-spain | none | missing | kingdom-of-spain has no 1620-1639 Valtellina events |
| three-leagues 1622 loss habsburg-monarchy | none | missing | habsburg-monarchy has no 1622 gain of the Prättigau, Lower Engadine, Müstair |
| three-leagues 1626 contest_end kingdom-of-spain | none | missing |  |
| three-leagues 1639 gain kingdom-of-spain | none | missing | kingdom-of-spain and state-of-milan record no 1639 loss; author flagged |
| three-leagues 1649 gain habsburg-monarchy | none | missing | habsburg-monarchy has no 1649/1652 losses; the Lower Engadine should be 1652 (Scuol page) |
| three-leagues 1797 loss cisalpine-republic | cisalpine-republic 1797 gain | matched | cisalpine /ledger/4 1797-10 |
| three-leagues 1799 loss helvetic-republic | helvetic-republic 1799 gain | matched | helvetic /ledger/6 1799-04 |
| swiss-confederation 1497 vassal_start three-leagues | none | missing | no mirror in three-leagues (finding) |
| swiss-confederation 1512 vassal_start three-leagues | none | missing | Valtellina tint; no mirror |
| swiss-confederation 1620 vassal_end three-leagues | none | missing | no mirror |
| swiss-confederation 1639 vassal_start three-leagues | none | missing | no mirror |
| swiss-confederation 1797 vassal_end three-leagues | none | missing | no mirror |
| swiss-confederation 1798 vassal_end three-leagues | none | mismatch | no mirror; and 13 months before three-leagues' end 1799-04 (infobox 21 April 1799) |
| sieben-zenden 1416 found prince-bishopric-of-sion | none | exception | no dossier; listed in counterparts_needing_dossiers |
| sieben-zenden 1475 gain county-of-savoy | none | missing | county-of-savoy /ledger/15 1475 loss goes to swiss-confederation (Lake Neuchâtel cell); no Lower Valais loss |
| sieben-zenden 1476 gain county-of-savoy | none | missing | no loss of Saint-Maurice (and Monthey, Évian, Thonon) in county-of-savoy; also 1477, 1536 and 1569 events still to be written |
| sieben-zenden 1798 loss helvetic-republic | helvetic-republic 1798 gain | matched | helvetic /ledger/0 1798 |
| swiss-confederation 1416 vassal_start sieben-zenden | none | missing | no mirror (finding) |
| swiss-confederation 1475 vassal_start sieben-zenden | none | missing | no mirror (finding) |
| swiss-confederation 1798 vassal_end sieben-zenden | none | missing | /ledger/38 and /ledger/39; no mirror |
| swiss-confederation 1815 gain sieben-zenden | none | mismatch | sieben-zenden ended 1798-05; first-french-empire /ledger/64 already loses the Valais to swiss-confederation in 1814-04. Route to swiss-confederation: counterpart first-french-empire, date reconciled. |
| republic-of-geneva 1534 found prince-bishopric-of-geneva | none | exception | no dossier; listed |
| republic-of-geneva 1754 gain kingdom-of-sardinia | none | missing | kingdom-of-sardinia has no 1754 loss; author flagged |
| republic-of-geneva 1798 loss french-directory | french-directory 1798 gain | matched | french-directory /ledger/17 is 1798-08; Republic of Geneva infobox gives 15 April 1798, route month to french-directory |
| republic-of-geneva 1813 gain first-french-empire | none | missing | first-french-empire has no 1813 loss of Geneva |
| republic-of-geneva 1815 loss swiss-confederation | swiss-confederation 1815 gain | matched | swiss /ledger/46 1815-05 |
| swiss-confederation 1526 vassal_start republic-of-geneva | none | mismatch | no mirror, and 1526 precedes Geneva's 1534 start; Old Swiss Confederacy page dates the Bern treaty 1536 |
| swiss-confederation 1798 vassal_end republic-of-geneva | none | missing | no mirror (finding) |
| duchy-of-massa-and-carrara 1796 loss cispadane-republic | none | missing | cispadane lists the duchy as predecessor but has no gain; it starts 1796-10 |
| duchy-of-massa-and-carrara 1806 loss principality-of-lucca-and-piombino | principality-of-lucca-and-piombino 1806 gain | matched | /ledger/1 |
| duchy-of-massa-and-carrara 1814 gain principality-of-lucca-and-piombino | principality-of-lucca-and-piombino 1814 loss | mismatch | lucca-piombino /ledger/3 sends its 1814 loss to austrian-empire |
| duchy-of-massa-and-carrara 1815 gain nobody | none | exception | Lunigiana fiefs from the Congress |
| duchy-of-massa-and-carrara 1815 loss duchy-of-modena-and-reggio | duchy-of-modena-and-reggio 1815 gain | matched | /ledger/1 1815-12 |
| duchy-of-massa-and-carrara 1829 loss duchy-of-modena-and-reggio | duchy-of-modena-and-reggio 1829 gain | matched | /ledger/2 |
| duchy-of-romagna 1500 gain Lordship of Rimini | none | exception | text counterpart, no dossier |
| duchy-of-romagna 1501 gain Lordship of Faenza | none | exception | text counterpart, no dossier |
| duchy-of-romagna 1502 gain duchy-of-urbino | duchy-of-urbino 1502 loss | matched | /ledger/3 |
| duchy-of-romagna 1502 gain Camerino | none | exception | text counterpart, no dossier |
| duchy-of-romagna 1503 loss duchy-of-urbino | duchy-of-urbino 1503 gain | matched | /ledger/4 |
| duchy-of-romagna 1503 loss republic-of-venice | none | missing | republic-of-venice has no 1503 gain of Faenza and Rimini (only the 1509 loss of Ravenna) |
| duchy-of-romagna 1503 loss papal-states | papal-states 1503 vassal_end | matched | papal /ledger/16; consistent once the vassal mirrors are added |
| papal-states 1500 vassal_start duchy-of-romagna | none | missing | no mirror in duchy-of-romagna (finding); papal region also includes Ravenna province, which the pages do not give to Borgia |
| papal-states 1503 vassal_end duchy-of-romagna | none | missing | no mirror (finding) |
| march-of-tuscany 846 found middle-franks | none | missing | middle-franks has no 846 event; the relation is overlordship, not a loss; author flagged |
| march-of-tuscany 1000 loss republic-of-pisa | republic-of-pisa 1000 found | mismatch | pisa /ledger/0 found names no counterpart; should name march-of-tuscany |
| march-of-tuscany 1115 loss republic-of-florence | republic-of-florence 1115 found | mismatch | florence /ledger/0 found names no counterpart; should name march-of-tuscany |
| march-of-tuscany 1125 loss republic-of-siena | republic-of-siena 1125 found | matched |  |
| march-of-tuscany 1160 loss republic-of-lucca | republic-of-lucca 1160 found | matched |  |
| march-of-tuscany 1185 gain republic-of-florence | none | missing | republic-of-florence has no 1185 loss (Republic_of_Florence page: margraves 'reacquired Florence and its townlands'); not flagged by the author |
| march-of-tuscany 1197 loss republic-of-florence | none | missing | republic-of-florence has no 1197 gain; not flagged by the author |

## Problems and routing

- No dossier was edited: every unapplied finding needs new events or keyframes, beyond the small-fix scope.
- None of the six Wikipedia pages (Three_Leagues, Seven_Tithings, Republic_of_Geneva, Duchy_of_Massa_and_Carrara, Duke of Romagna, March_of_Tuscany) gives an area; area checks compare the drawn cells with modern units only.
- Engadine is a disambiguation page and Engadin has no history; the 1652 date for the Lower Engadine comes from the Scuol page.
- Convention question for the orchestrator: swiss-confederation draws the Zugewandte Orte (Three Leagues, Sieben Zenden, Geneva) as vassals; three dossiers here fail only partly for missing mirrors of that choice. If the project prefers no associate tint, route the change to swiss-confederation (/ledger/8, 15, 19, 25, 29, 33, 34, 36, 38-41) instead.
- Neighbour fixes to route: swiss-confederation /ledger/47 (1815 gain names sieben-zenden, ended 1798; first-french-empire /ledger/64 already gives the Valais in 1814-04); swiss-confederation /ledger/29 (1526, before Geneva's 1534 start); republic-of-florence lacks the 1185 loss and 1197 gain against march-of-tuscany; republic-of-pisa and republic-of-florence found events name no counterpart; kingdom-of-france /ledger/79 sends the Valtellina to duchy-of-milan in 1512.

Gazetteer names needed: Prättigau, Lower Engadine, Val Müstair, Valtellina, Lower Valais, Saint-Maurice, Martigny, Monthey, Chablais, Imola, Faenza, Camerino.
