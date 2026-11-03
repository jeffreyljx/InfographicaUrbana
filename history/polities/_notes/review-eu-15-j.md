# Review eu-15-j: polish-lithuanian-commonwealth

Reviewer, 2026-10-31 brief, run 2026-11-01. One dossier (45 Cliopatria shapes, 49 keyframes, 71 events, 14 sources). Verdict: **fail**. Two shape-consistency findings with neighbour dossiers are still open (Courland, Livonia). Three small fixes were applied by the reviewer.

## Mechanical
- validate --resolve: 0 errors, 0 warnings before and after the reviewer edits. All 45 shapes have a verdict; the new keyframes 1569, 1582, 1625 and 1794 carry from, to and a correction. The ledger is in order; found is at 1569-07 and dissolve at 1795-10; there are 11 contest pairs, 8 occupation pairs and 4 vassal pairs.

## Spot checks (6 events, plus extra events on the same pages)
- /ledger/17, 1625 loss of northern Livonia: confirmed on Polish-Swedish War (1626-1629): 'in 1625 Gustavus compelled him to cede Livonia north of the Daugava river'.
- /ledger/44, 1667-01 Andrusovo: confirmed: 'January 1667'; 'ceded to Russia the fortress of Smolensk and Ukraine on the left bank of the Dnieper River (including Kiev)'. The same page confirms /ledger/35 (Polotsk 17 July 1654), /ledger/37 (Ludza and Rezekne in December) and /ledger/38 (Minsk 3 July, Vilnius 31 July 1655).
- /ledger/49, 1672-10 Buczacz: confirmed (October 1672; Bracław, Podole and part of the Kiev voivodeship). The infobox confirms /ledger/50, Żurawno 1676: 'regains Bila Tserkva and Pavoloch'.
- /ledger/57, 1772-08 First Partition: confirmed ('decided on 5 August 1772'; Dvina-Dnieper line; Polish Livonia). The same page confirms /ledger/62 (23 January 1793) and /ledger/67 (24 October 1795, 120,000 km2 'with Vilnius').
- /ledger/27, 1649-08 Zboriv: confirmed (19 August 1649; Kyiv, Bratslav, Chernihiv).
- /ledger/33, 1654-01 Pereiaslav (confidence 2): the quote is NOT on the page. 'the Commonwealth lost the Cossack-held territories' appears neither on Khmelnytsky Uprising nor on the main article. The date is supported (infobox '18 January 1654'; 'early 1654'; 'Emergence of the Cossack Hetmanate'). FIXED by the reviewer: the note quotes the page now, and the same false quote was removed from /keyframe_review/21/note and /wars/6/outcome.
- Main article, also confirmed: capitals 'Kraków (1569–1596); Warsaw (1596–1795)'; Moscow 'driven out on 4 November 1612'; Bromberg 1657 'renounce its suzerainty over Protestant Prussia'.

## Area
The infobox gives 815,000 km2 (1582), 1,000,000 (1618) and 733,500 (1700). Cliopatria has 777,106 (_1579, alive in 1582), ratio 0.95; 950,896 (_1612), ratio 0.95; 791,370 (_1700 with Saxony), ratio 1.08. No factor of two. The author's figures are right.

## Fixes applied by the reviewer (re-validated, 0 errors)
1. /identity/predecessors, /ledger/0, /ledger/1: the predecessors were kingdom-of-poland and grand-duchy-of-lithuania, but both dossiers end in 1449 and name house-of-jagiellon as successor. house-of-jagiellon (1450-1569-07) names this state as successor and has 'merge polish-lithuanian-commonwealth' at 1569-07. The predecessor is now house-of-jagiellon, and the counterpart of found and merge is house-of-jagiellon.
2. /ledger/33/note (+ /keyframe_review/21/note, /wars/6/outcome): the false quote is replaced by the page's words.
3. /ledger/27/region/text: 'with eastern Volhynia and Podolia up to the Sluch' is neither on the page nor in the drawn regions. Cut to the page's 'Kyiv, Bratslav and Chernihiv'.

## Open findings (back to the author)
A. BLOCKING. Courland is drawn twice in 1569-1733. Keyframes 0-34 keep Courland (105-108 cells, the author's note 7) inside the Commonwealth shape. duchy-of-courland (eu-14, reviewed) draws the duchy itself from 1561 to 1733 (keyframe duchy-of-courland_1561, the 1734 shape), and /ledger/2 makes it a vassal. Fix: subtract {"cliopatria": "Duchy of Courland", "year": 1734} from every correction of 1569-1733, as was done for Saxony and Tobago; ok verdicts become adjust. eu-15-i gave house-of-jagiellon the same ruling.
B. BLOCKING, not flagged. Livonia is drawn twice in 1582-1628. duchy-of-livonia (state, 1561-1629, accepted in eu-14-x with the ruling that 'the Commonwealth's Livonian province holds the land in this project') draws Livonia 1582-1628 and books:
   - the 1582 gain from tsardom-of-russia (its /ledger/5), the same as /ledger/6 here;
   - losses to swedish-livonia in 1621-1629 (its /ledger/10-14), against /ledger/17 here (1625 to swedish-empire);
   - a 1629-09 dissolve with successor polish-lithuanian-commonwealth (Inflanty, region Latgale), which has no mirror here.
   Fix: subtract the duchy-of-livonia keyframes from keyframes 0-13. Book the duchy as a dependency (vassal_start duchy-of-livonia 1569-07, vassal_end 1629-09) and add a 1629-09 gain (or merge) of Latgale from duchy-of-livonia. Recast /ledger/6 and /ledger/17 so that the land moves only once. If the orchestrator rules instead that the Commonwealth holds Livonia, retype duchy-of-livonia.
C. /ledger/3 and /ledger/40: the vassal pair keeps duchy-of-prussia until 1657, but that dossier ends 1618-08 (merge into brandenburg-prussia). Add vassal_end duchy-of-prussia 1618-08 and vassal_start brandenburg-prussia 1618-08 (Ducal Prussia), and set /ledger/40 to counterpart brandenburg-prussia. Cite the Duchy of Prussia page. eu-09-j asked for the same.
D. /ledger/44: the 1667 cession repeats the left bank already lost to zaporozhian-cossacks in /ledger/33 (1654). Kyiv is booked in 1667 here, but in 1686 by tsardom-of-russia (/ledger/70, 'Gain of Kiev and Zaporizhzhia', Territorial evolution of Russia). Say in the note that the 1667 left-bank part is a de jure renunciation, or limit the 1667 region to Smolensk and Kyiv. Coordinate Kyiv's year with eu-16.
E. Royal Prussia (royal-prussia, colony) and Warmia (prince-bishopric-of-warmia, state) are drawn by eu-15-x inside this shape until 1772. This dossier has no event for:
   - the 1637 Lauenburg-Bütow gain (royal-prussia /ledger/6, confidence 3);
   - the 1657 loss of Lauenburg-Bütow and Draheim to brandenburg-prussia (brandenburg-prussia /ledger/7 and royal-prussia /ledger/12, confidence 3);
   - the Swedish occupation of Royal Prussia in 1655-1660 (royal-prussia /ledger/7-17).
   Add them, and have the orchestrator settle the Warmia overlap.

## Thin (gap-filler)
- rulers are missing (List of Polish monarchs).
- Confidence 1: /ledger/3, /ledger/42, /ledger/43, /ledger/46, /ledger/66.
- Riga 1621 and Mitawa 1622: no events here, though the war has a zone.
- Smolensk's month (2 June 1611) is on Polish–Russian War (1609–1618), the title that loaded for the tsardom-of-russia author.
- Sevsk 1585 and Trubchevsk 1644: tsardom-of-russia books them as gains from the Commonwealth.

## Cross-checks (summary; full matrix in the JSON report)
- Matched: Russia 1579, 1582, 1610-12, 1611, 1618/19, 1634, 1655, 1661/62, 1667; Sweden 1655-60; Ottomans 1672, 1699; Pro-Swedish Poland 1706, 1709; partitions 1772, 1793, 1795 with Russia, Austria and Prussia.
- Missing on the other side:
  - zaporozhian-cossacks has none of the 1648-1654 events (eu-16);
  - tsardom-of-russia has no 1654 Polotsk/Vitebsk or Latgale occupation;
  - ottoman-empire has no 1676 Żurawno loss;
  - swedish-empire has no 1626-1629 contest;
  - duchy-of-courland and duchy-of-prussia have no vassal events.
- Type mismatches:
  - Smolensk 1654: tsardom-of-russia books a gain, this dossier an occupation;
  - the Prussian ports 1629-35: swedish-empire books gain/loss, this dossier occupation;
  - 1792: russian-empire books a contest, this dossier an occupation.
- Year mismatches:
  - northern Livonia: swedish-empire 1622-11 against this dossier's 1625;
  - Kyiv: 1686 against 1667.
- Land mismatch: nalyvaiko-uprising books 1595 gains from this state (confidence 2/1); this dossier books a contest only.
- The Saxony gap is already covered: electorate-of-saxony has keyframes from 1657 and for 1718-1762.
