# Review eu-09-c: holy-roman-empire-minor-states

Reviewer, 2026-10-25. Verdict: **fail**. The dossier goes back to the author for two blocking findings: wartime holds are recorded as cessions with keyframes accepted as drawn. The rest of the dossier held up: every confidence-3 event checked was on its page with the right year, and the validator passes with --resolve (0 errors, 0 warnings).

## What I tried
- Validator with --resolve: valid, 414 regions resolved.
- Walked all 99 keyframes against shapes.csv areas. Every change of 15 or more cells has a ledger event or an adjust, except the wartime holds below.
- Opened 10 pages: Three Bishoprics, Peace of Westphalia, War of the First Coalition, German mediatisation (twice), Thirty Years' War, Holy Roman Empire (twice), Livonian War, Treaty of Ryswick, Margraviate of Brandenburg, Liechtenstein.
- Area: the infobox has 1,100,000 km2 for 1150 only, which is before this row. The author acknowledges this in keyframe 0.
- Cross-checked 110 territorial events against the existing neighbour dossiers (see the report's cross_checks).

## Findings
### /ledger/102, /ledger/103, /keyframe_review/94
- What: BLOCKING. The 1796 French advance into Swabia and Franconia (60 cells: Baden-Wurttemberg 48, Bavaria 6, Hesse 4) is recorded as a loss to french-directory and a 1797 gain back, and the 1796 keyframe is accepted as drawn, so the map shows southern Germany as French for a year.
- Why: War of the First Coalition page (opened): Jourdan reached Amberg in late August, Moreau reached Bavaria and the edge of Tyrol by September, then 'both armies were forced to retreat back across the Rhine'. The keyframe note itself calls the cells 'the ground the armies of Moreau and Jourdan reached', and wars[6].zones[1] already treats it as a war zone. Master plan: fought-over land is a contest blend, and occupied land becomes the occupier's only if annexed. The author handled the Swedish hold of 1632-1635 this way but not this one.
- Fix: Replace /ledger/102 and /ledger/103 with contest_start 1796 and contest_end 1796 (or 1797), counterpart french-directory, region wars[6].zones[1], confidence 2. Set /keyframe_review/94 to verdict adjust with correction {"union":[{"cliopatria":"Holy Roman Empire Minor States","year":1796},{"intersect":[{"cliopatria":"Holy Roman Empire Minor States","year":1794},{"cliopatria":"French Directory","year":1796}]}],"text":"the 1796 shape with the ground the French armies crossed, still Imperial"}.

### /ledger/93, /ledger/94, /ledger/96, /keyframe_review/85, /keyframe_review/86
- What: BLOCKING. French-held Hesse, Westphalia and the Rhineland in the Seven Years' War are recorded as losses to kingdom-of-france (1757: 20 cells, conf 1; 1762: 37 cells, conf 2) and a 1763 gain of 122 cells, and the 1757 and 1762 keyframes are accepted as drawn.
- Why: Seven Years' War page as quoted in /ledger/96: Louis XV 'evacuated Prussia's Rhineland territories, ending France's involvement in the war in Germany'. /ledger/94 cites the French capture of Marburg (1760) and Brunswick 'taking Cassel' (1762), which describe an army's hold during the fighting. No cession is on the page. wars[5].zones[0] calls the land 'held by the French'. The kingdom-of-france dossier records these years as occupations (1757 occupation_start, 1762 occupation_end), not gains.
- Fix: Replace with an occupation_start (1757, or the first year the page dates French troops in Hesse/Westphalia) and an occupation_end (1763-02), both with counterpart kingdom-of-france and region wars[5].zones[0]; mark /keyframe_review/85 and /86 adjust as union(this row's shape of the year, intersect(Holy Roman Empire Minor States 1752, Kingdom of France of the year)) so the cells stay Imperial and hatched. Leave the Hanover cells (/ledger/92, /95, /97) at confidence 1 as Cliopatria re-cuts, or treat them the same way if a page supports it.

### /ledger/57, /ledger/58, /keyframe_review/54
- What: Same pattern (confidence 2): the Danish hold of the Lower Saxon Circle 1626-1628 (55 cells) is a loss to denmark-norway; 19 cells return in 1629 and the other 36 fall into no shape.
- Why: Thirty Years' War page: Christian IV was elected military commander of the Lower Saxon Circle in May 1625, lost at Lutter in August 1626, and at Lubeck (1629) kept Schleswig and Holstein 'in return for relinquishing Bremen and Verden'. The circle's lands stayed Imperial estates, and wars[3].zones[0] is this same land.
- Fix: Make it contest_start 1626 / contest_end 1629-06 (counterpart denmark-norway, region wars[3].zones[0]) and mark /keyframe_review/54 adjust to keep the 55 cells; say where the 36 cells are in 1629-1631 (in this row, by correction of /keyframe_review/55).

### /ledger/63, /ledger/68, /ledger/66, /ledger/69
- What: Same pattern (confidence 1): Mecklenburg drawn Swedish 1642-1648 and 18 Swabian cells drawn French 1645-1648 are recorded as loss and gain, though the dossier's own 1648 notes say Westphalia gives Sweden no Mecklenburg and the Swabian cells simply return.
- Why: Peace of Westphalia page (opened): Sweden received Western Pomerania, Wismar and Bremen-Verden; France the Three Bishoprics and the Decapole. Neither got Mecklenburg or Swabia.
- Fix: Record both as occupation_start/occupation_end pairs (swedish-empire 1642-1648, kingdom-of-france 1645-1648) with adjust verdicts on /keyframe_review/60 and /61, as was done for 1632.

### /ledger/59/note, /ledger/60/note (applied by reviewer)
- What: The notes said the Peace of Prague 'hands back' the 424 Swedish-held cells. The page does not say that.
- Why: Thirty Years' War page: Nordlingen 'cost Sweden control of southern Germany' (September 1634), and the Peace of Prague is the leagues disbanding in return for withdrawing the Edict of Restitution; no land is returned by it.
- Fix: Reworded both notes to quote the Nordlingen sentence and to say the page names no land returned at Prague (dates kept: 1632 / 1635-05). Re-validated: 0 errors.

### /ledger/86 (applied by reviewer)
- What: Liechtenstein dated 1721 (Cliopatria) at confidence 1. The Liechtenstein dossier and page date it 1719.
- Why: Liechtenstein page: 'On 23 January 1719, after the lands had been purchased, Charles VI, Holy Roman Emperor, decreed that Vaduz and Schellenberg' were united. The principality-of-liechtenstein dossier is founded 1719-01 with this state as counterpart.
- Fix: Moved to 1719-01, source https://en.wikipedia.org/wiki/Liechtenstein (added to sources[]), confidence 3, note rewritten; the 1-cell change stays inside the 1713-1720 shape. Re-validated: 0 errors, 0 warnings.

### /ledger/99
- What: 52 cells to duchy-of-bavaria dated 1780 (Cliopatria, confidence 1), while the duchy-of-bavaria dossier dates the Bavarian-Palatine union to 1777 (gain from electoral-palatinate, confidence 3).
- Why: duchy-of-bavaria ledger: 1777 gain, counterpart electoral-palatinate, confidence 3.
- Fix: Re-date to 1777 and name the Palatinate lands in the note, citing Bavaria's page; keep or adjust /keyframe_review/89 (1775-1777) so that it agrees.

### /ledger (1681)
- What: Missing event: the French seizure of Strasbourg in 1681. The 6 Strasbourg cells leave the row only in the 1683 keyframe and have no event.
- Why: The kingdom-of-france dossier has a 1681 gain from holy-roman-empire (Strasbourg, confidence 2). /keyframe_review/62 says the 7 Bas-Rhin cells are 'imperial until Cliopatria drops them in 1683'. The Ryswick page: 'France kept Strasbourg'.
- Fix: Add a 1681 loss to kingdom-of-france of Strasbourg, citing the France dossier's page (or https://en.wikipedia.org/wiki/R%C3%A9unions).

### /identity/capitals
- What: Prague (1355-1378, 1576-1612) and Vienna (1550-1575) are inside the shapes.csv bbox, but they lie in the Kingdom of Bohemia and Habsburg leaf shapes, not in this residual row, so a capital marker will sit outside the row's polygon.
- Why: From 1272 the row excludes the Bohemian leaf and from 1492 the Habsburg one (author's notes, 'WHAT THE ROW IS').
- Fix: Add a sentence to each capital's note saying the seat lies in the member's leaf shape, so the compiler does not test it against this row.

## Thin (for a gap-filler)
- /identity/rulers: rulers strip omitted (the HRE page gives reign years for four emperors only). Try https://en.wikipedia.org/wiki/List_of_Holy_Roman_Emperors
- /identity/capitals: court seat 1260-1354, 1379-1549 and 1613-1662; Vienna 1550-1575 is approximate. Try https://en.wikipedia.org/wiki/Hofburg
- /ledger/2, /ledger/3, /ledger/16: 1272 and 1333 Bohemia cut-outs (111 and more cells) and the 1272 Papal States cut (46 cells): confidence 1, no dating page. Try https://en.wikipedia.org/wiki/Kingdom_of_Bohemia
- /ledger/26, /ledger/27: 1402 Milan (148 cells) and Savoy (42 cells) leaf cuts; Gian Galeazzo Visconti's ducal title of 1395 should date the Milan cut. Try https://en.wikipedia.org/wiki/Duchy_of_Milan
- /ledger/28: 1407 Venice (48 cells): the Venetian Terraferma conquests of 1404-1405. Try https://en.wikipedia.org/wiki/Republic_of_Venice
- /ledger/33, /ledger/34: 1431 Lorraine (75) and Trier (25) leaf cuts. Try https://en.wikipedia.org/wiki/Duchy_of_Lorraine
- /ledger/44, /ledger/46, /ledger/48: 1529-1552 Habsburg Low Countries cuts (39, 27, 17 cells). Try https://en.wikipedia.org/wiki/Habsburg_Netherlands
- /ledger/74, /ledger/75: 1673 Habsburg (30) and France (33) cuts; Franco-Dutch War not opened. Try https://en.wikipedia.org/wiki/Franco-Dutch_War
- /ledger/83: 1709 Hanover cut (93 cells); the electorate-of-hanover dossier has no mirror. Try https://en.wikipedia.org/wiki/Electorate_of_Hanover
- /ledger/88, /ledger/89, /ledger/90, /ledger/91: 1741-1748 Habsburg and French swings (79 cells out, then back); France's dossier calls 1741-1744 an occupation. Try https://en.wikipedia.org/wiki/War_of_the_Austrian_Succession
- /ledger/92, /ledger/95, /ledger/97: 1757-1763 Hanover shape taking 81 cells of Hesse and Westphalia: page silent, and the Hanover dossier has Hanover itself occupied by France instead. Try https://en.wikipedia.org/wiki/Electorate_of_Hanover
- /ledger/100: 1791 Prussian gain of Franconia (31 cells): Ansbach-Bayreuth passing to Prussia. Try https://en.wikipedia.org/wiki/Principality_of_Ansbach
- /ledger/104, /ledger/111: 1797 Cisalpine Republic (29 cells) and 1805 First French Empire (34 cells) cuts. Try https://en.wikipedia.org/wiki/Peace_of_Pressburg_(1805)
- /ledger (1714): Rastatt/Baden 1714 returns (France's dossier has a 1713 gain and a 1714 loss with the Empire); not in this ledger. Try https://en.wikipedia.org/wiki/Treaty_of_Rastatt
- /ledger (vassal rows): Cliopatria relation rows (Bohemia vassal 1314-1452, Teutonic Order 1305-1401, Swiss 1326-1458, Brandenburg 1422-1458) not written for lack of a page. Try https://en.wikipedia.org/wiki/Imperial_immediacy

## Spot checks
- /ledger/49: confirmed (Toul 13 April, Metz entry 18 April, Verdun 12 June 1552; Treaty of Chambord 15 January 1552; prince-bishoprics 'until they were seized') (https://en.wikipedia.org/wiki/Three_Bishoprics)
- /ledger/50, /ledger/51: confirmed (siege 19 October 1552 to 2 January 1553) (https://en.wikipedia.org/wiki/Three_Bishoprics)
- /ledger/67: confirmed ('Brandenburg-Prussia received Farther Pomerania, and the Bishoprics of Magdeburg, Halberstadt, Kammin, and Minden'; signed 24 October 1648) (https://en.wikipedia.org/wiki/Peace_of_Westphalia)
- /ledger/101: confirmed (Fleurus 1794 'gained all of the Austrian Netherlands and the Rhineland for France'; Basel 5 April 1795; Campo Formio October 1797) (https://en.wikipedia.org/wiki/War_of_the_First_Coalition)
- /ledger/102, /ledger/103: confirmed facts, but the page has the armies retreating, so loss/gain is the wrong type (fix 1) (https://en.wikipedia.org/wiki/War_of_the_First_Coalition)
- /ledger/105 to /ledger/110: confirmed (25 February 1803, Diet 24 March, ratified 27 April; the award tables list every place named, including the Grand Duke of Salzburg and the imperial cities given to Wurttemberg; 'Baden received over seven times as much, Prussia nearly five times') (https://en.wikipedia.org/wiki/German_mediatisation)
- /ledger/117: confirmed ('On 6 August 1806, Emperor Francis II abdicated and formally dissolved the empire') (https://en.wikipedia.org/wiki/Holy_Roman_Empire)
- /ledger/12, /ledger/13, /ledger/42, /ledger/72: confirmed (Henry VII elected 27 November 1308; Louis IV king 1314; renaming to 'Holy Roman Empire of the German Nation'; Perpetual Diet at Regensburg 1663-1806) (https://en.wikipedia.org/wiki/Holy_Roman_Empire)
- /ledger/59, /ledger/60: dates confirmed (June 1630, September 1631, April 1632, Nordlingen 1634, Prague 1635); the claim that the Peace of Prague returned the land is not on the page (note fixed) (https://en.wikipedia.org/wiki/Thirty_Years%27_War)
- /ledger/79, /keyframe_review/72: confirmed (20 September to 30 October 1697; Freiburg, Breisach, Philippsburg and Lorraine returned, Palatinate claims dropped; France kept Strasbourg) (https://en.wikipedia.org/wiki/Treaty_of_Ryswick)
- /keyframe_review/18: confirmed (hereditary control 1411; recognised margrave and elector 1415; the electorate-of-brandenburg dossier starts 1415-04, consistent with the correction) (https://en.wikipedia.org/wiki/Margraviate_of_Brandenburg)
- /keyframe_review/43: confirmed (Order 'dissolved by the second Treaty of Vilnius in 1561'; lands to Lithuania, Sweden and Denmark-Norway). The author's report and notes add that Livonia 'was never Imperial'; that is not on the page and overstates it (Terra Mariana held as an Imperial fief), but the correction for 1564-1571 stands on the 1561 dissolution. (https://en.wikipedia.org/wiki/Livonian_War)
- /ledger/86: mis-dated (1721 for the 23 January 1719 decree), fixed by reviewer (https://en.wikipedia.org/wiki/Liechtenstein)

## Cross-dossier mismatches to route
- /ledger/4 1272 loss duchy-of-bavaria: missing. duchy-of-bavaria dossier exists but has no event with this state within a year.
- /ledger/5 1272 loss margraviate-of-brandenburg: missing. Margraviate dossier has only a 1272 gain from duchy-of-greater-poland; no gain from this state.
- /ledger/6 1272 gain duchy-of-styria: missing. duchy-of-styria dossier exists but has no event with this state within a year.
- /ledger/9 1294 gain house-of-habsburg: missing. house-of-habsburg dossier exists but has no event with this state within a year.
- /ledger/10 1294 gain house-of-luxembourg: missing. house-of-luxembourg dossier exists but has no event with this state within a year.
- /ledger/11 1294 gain duchy-of-bavaria: missing. duchy-of-bavaria dossier exists but has no event with this state within a year.
- /ledger/17 1344 loss house-of-habsburg: missing. house-of-habsburg dossier exists but has no event with this state within a year.
- /ledger/19 1352 loss duchy-of-bavaria: missing. duchy-of-bavaria dossier exists but has no event with this state within a year.
- /ledger/29 1415 loss county-of-brabant: mismatch. This dossier has the row losing cells to Brabant in 1415, while the Brabant dossier records its own 1415 loss to "unknown (page silent)". The two disagree on direction and counterpart.
- /ledger/30 1422 gain county-of-brabant: missing. county-of-brabant dossier exists but has no event with this state within a year.
- /ledger/31 1422 loss electorate-of-brandenburg: missing. electorate-of-brandenburg dossier exists but has no event with this state within a year.
- /ledger/32 1429 loss duchy-of-luxembourg: missing. duchy-of-luxembourg dossier exists but has no event with this state within a year.
- /ledger/35 1440 gain electorate-of-brandenburg: missing. electorate-of-brandenburg dossier exists but has no event with this state within a year.
- /ledger/37 1459 loss swiss-confederation: missing. swiss-confederation dossier exists but has no event with this state within a year.
- /ledger/43 1526 loss kingdom-of-spain: mismatch. Spain names "Friesland" as counterpart, not this state.
- /ledger/45 1529 loss swiss-confederation: missing. swiss-confederation dossier exists but has no event with this state within a year.
- /ledger/47 1540 loss kingdom-of-france: missing. kingdom-of-france dossier exists but has no event with this state within a year.
- /ledger/49 1552 loss kingdom-of-france: mismatch. France agrees on Metz, Toul and Verdun in 1552 but names the predecessor slug holy-roman-empire (which ends 1259); route to eu-10 to change the slug.
- /ledger/55 1609 gain dutch-republic: missing. dutch-republic dossier exists but has no event with this state within a year.
- /ledger/62 1640 loss kingdom-of-france: mismatch. France records a 1640 gain of "Picardy and Alsace (holder not named by the pages opened)"; substance agrees, counterpart unnamed.
- /ledger/64 1642 loss kingdom-of-france: missing. 
- /ledger/66 1645 loss kingdom-of-france: mismatch. France records its Alsace and Three Bishoprics gains from holy-roman-empire in 1648, while this dossier loses Alsace in 1640/1645 and records a 1648 gain from France; the two ledgers disagree on the year and direction of the Alsace transfer.
- /ledger/69 1648 gain kingdom-of-france: mismatch. France gains from holy-roman-empire in 1648 (Westphalia); this dossier records a 1648 gain from France (Cliopatria returns 37 cells). Opposite directions in the same year.
- /ledger/70 1648 gain kingdom-of-spain: missing. kingdom-of-spain dossier exists but has no event with this state within a year.
- /ledger/75 1673 loss kingdom-of-france: missing. France has occupation events with dutch-republic and kingdom-of-spain in 1672-1674, none with this state.
- /ledger/77 1683 gain kingdom-of-france: mismatch. France gains Strasbourg from holy-roman-empire in 1681; this dossier has no 1681 loss (the 6 Strasbourg cells leave only in the 1683 keyframe, without an event) and records a 1683 gain from France.
- /ledger/78 1696 loss kingdom-of-france: mismatch. France models the Nine Years War as a contest with holy-roman-empire 1688-1697; this dossier records a 1696 loss.
- /ledger/79 1697 gain kingdom-of-france: mismatch. Substance matches (Ryswick return, 1697) but France names the predecessor slug holy-roman-empire.
- /ledger/80 1702 loss kingdom-of-france: mismatch. France records a 1702 loss to and 1703 gain from holy-roman-empire; this dossier records a 1702 loss to France; directions disagree.
- /ledger/83 1709 loss electorate-of-hanover: missing. 
- /ledger/87 1734 loss kingdom-of-spain: missing. kingdom-of-spain dossier exists but has no event with this state within a year.
- /ledger/89 1741 loss kingdom-of-france: mismatch. France records an occupation of "German lands" 1741-1744; this dossier records a loss and a gain.
- /ledger/90 1744 gain kingdom-of-france: mismatch. see 1741
- /ledger/92 1757 loss electorate-of-hanover: mismatch. Hanover dossier has Hanover itself occupied by France 1757-1758, not a Hanoverian gain of 81 cells of Hesse and Westphalia.
- /ledger/93 1757 loss kingdom-of-france: mismatch. France records an occupation of electorate-of-hanover in 1757, not a gain from this state.
- /ledger/94 1762 loss kingdom-of-france: mismatch. France ends an occupation of "Hesse" in 1762; this dossier records a 1762 loss to France. Reviewer fix 2: make this an occupation.
- /ledger/95 1762 loss electorate-of-hanover: missing. 
- /ledger/96 1763 gain kingdom-of-france: mismatch. see 1762
- /ledger/97 1763 gain electorate-of-hanover: missing. 
- /ledger/99 1780 loss duchy-of-bavaria: mismatch. Bavaria dates the union with the Palatinate to 1777 (gain from electoral-palatinate, conf 3); this dossier has 52 cells to Bavaria in 1780 (conf 1, Cliopatria). Three years and a different counterpart.
- /ledger/105 1803 loss duchy-of-bavaria: mismatch. Bavaria names prince-bishopric-of-wurzburg, -bamberg, -freising, -augsburg and -passau as counterparts; this dossier treats the bishoprics as its own land and lists them under the umbrella slug ecclesiastical-states-of-the-empire. The slugs must be harmonised (eu-09-x).

## Problems
- kingdom-of-france (eu-10) uses the predecessor slug holy-roman-empire, which ends 1259, for 13 events from 1552 to 1714. They should name holy-roman-empire-minor-states. Route this to eu-10.
- duchy-of-bavaria (eu-09) gives the 1803 Bavarian gains to per-bishopric slugs (prince-bishopric-of-wurzburg and four others) that have no dossier, while this dossier treats them as its own land. eu-09-x must harmonise these slugs.
- Dossier edited by the reviewer, as the orchestrator allows: notes of /ledger/59 and /ledger/60 reworded; /ledger/86 moved to 1719 with the Liechtenstein page added to sources. The file re-validated with 0 errors and 0 warnings and was read back after 10 s.
- The verdict is fail for the two blocking type and shape findings (1796-1797 and 1757-1763), which the reviewer cannot apply. The rest of the dossier is careful: every confidence-3 event checked was on its page with the right year.
