# Review: batch eu-09-j (duchy-of-prussia, union-of-utrecht, dutch-republic)

Reviewed 2026-10-25 by the Phase B adversarial reviewer. Machine copy: history/notes/phase-b/reviews/eu-09-j.json.

Mechanical checks: `validate_dossier.py --resolve`: 0 errors on all three, before and after the reviewer's edits. The warnings are unknown gazetteer places (the 24 towns the author listed) and the counterpart slugs habsburg-netherlands and prince-bishopric-of-munster, which have no dossier yet.

## Verdicts

| slug | verdict | why |
| --- | --- | --- |
| duchy-of-prussia | fix (done by reviewer) | Every event confirmed. The month of the 1618 inheritance was added. |
| union-of-utrecht | fix (done by reviewer) | Every event confirmed. War years clipped to the life. Two thin items. |
| dutch-republic | thin | One mis-dated event and its keyframes fixed by the reviewer. Two war entries are missing and seven confidence-1 gaps remain for a gap-filler. |

## duchy-of-prussia

- Applied: `/identity/end`, `/ledger/1` and `/ledger/2` now carry month 8. Margraviate of Brandenburg page, infobox: 'Brandenburg-Prussia: 27 August 1618'. The merge cites that page, which is added as `/sources/2`. This matches electorate-of-brandenburg `/ledger/11` (1618-08).
- Confirmed on the Duchy of Prussia page: 10 April 1525, the year 1618, and the infobox area of 30,000 km2 (no year given; Cliopatria 38,518 km2, ratio 1.28; about 31,300 km2 once Warmia is removed). The page has Warmia as 'part of Poland', which supports subtracting it. The capital, Königsberg, lies inside the shape's bbox.
- The suzerain's side: the duchy was a Polish fief from 1525 to 1657. Under the schema, house-of-jagiellon and later polish-lithuanian-commonwealth (eu-15, not written yet) record `vassal_start` with counterpart duchy-of-prussia, and brandenburg-prussia carries the relation on from 1618.
- teutonic-order is owned by eu-14, not unowned as the author's report says. Its 1521-1525 shape should subtract Warmia too.

## union-of-utrecht

- Applied: `/wars/0` was 1566-1648 and is now 1579-1581, with the full war dates moved into the note.
- Confirmed on the Union of Utrecht page: 23 January 1579; joins in the summer of 1579 and 'in the following months'; Lier, Bruges and the city of Groningen in February 1580; Overijssel and Drenthe in April 1580. Act of Abjuration of 26 July 1581 on the Eighty Years' War page. No area on the page.
- Thin, within the 1-2 page budget: Rennenberg's defection in March 1580 took Groningen city and much of the north-east to Spain, and it has no loss event. Breda's loss in 1581 is not dated anywhere. These dates are the reviewer's own knowledge and must be confirmed on the page. Pages to try: George_van_Lalaing,_Count_of_Rennenberg and Eighty_Years'_War,_1576–1588.
- Type rebel is acceptable.

## dutch-republic

Applied by the reviewer, all re-validated:

1. **Venlo and Roermond, 1637 not 1648.** The old `/ledger/25` (loss, 1648, c1, Cliopatria's year) is now `/ledger/22` (1637, c2), sourced to the Cardinal-Infante Ferdinand page: 1637, 'taking the Dutch towns of Venlo and Roermond in the Meuse valley'. The Eighty Years' War, Generality Lands, Venlo and Frederick Henry pages are silent on it. The region is unchanged (the cells of the 1645 core missing from the 1648 core). The keyframes for 1637, 1640, 1642 and 1645 (`/keyframe_review/20-23`) now subtract that region, and each note says so. Ledger indices 22-24 moved up one, to 23-25.
2. `/wars/0`: the Eighty Years' War now starts in 1582 instead of 1566, with the full dates in the note.
3. `/wars/2`: 'Siege of Lille (1708)' (1708-1713) is renamed 'War of the Spanish Succession' (1702-1713). The Dutch Republic page gives those years. The Lille zone and the siege dates are kept.

For the author or a gap-filler (not applied):

- Missing wars: the Dutch Republic page names the War of the First Coalition (1792-1797) and the Nine Years' War. The 1794 losses happened in the First Coalition war. Add it, clipped to 1795, with zones for Staats-Brabant, Staats-Vlaanderen, Maastricht and Venlo. Add the Nine Years' War with empty zones and a note.
- `/wars/8` (Batavian Revolution) has empty zones, although the French overran the Republic in the winter of 1794/95.
- `/sources/10` Flanders_campaign is a disambiguation page that nothing cites. Drop or replace it.
- Gaps at confidence 1, already flagged by the author. Pages to try:
  - 1588 loss (`/ledger/2`): the eastern towns were lost between 1580 and 1587, not in 1588. From the reviewer's memory, to be confirmed: Groningen 1580, Steenwijk 1582, Zutphen 1583, Nijmegen 1585, Deventer 1587. Page: Eighty_Years'_War,_1576–1588.
  - 1606 (`/ledger/12-13`): which towns Spinola took. Page: Ambrogio Spinola.
  - Sluis 1604 is missing (the start of Staats-Vlaanderen), and Zeeland's south bank is missing from the 1609-1621 shapes. Page: Siege_of_Sluis_(1604).
  - 1619 and 1622 (`/ledger/14-15`). Page: Twelve_Years'_Truce.
  - Maastricht's return in 1678 (`/ledger/35`). Page: Treaties_of_Nijmegen.
  - Zeelandic Flanders 1747 (`/ledger/40`), plus the missing French captures of Bergen op Zoom (1747) and Maastricht (1748).
  - The Barrier, 1715-1781 (`/ledger/39`, `/ledger/42`): the page names only Dendermonde. The French took the Barrier towns in 1745-46 (reviewer's knowledge, to be confirmed).
  - 1794 (`/ledger/43`): the Siege of Maastricht (1794) page dates the fall of Sluis to 24 August 1794. The other towns are undated. Page: War_of_the_First_Coalition.
  - No rulers are written (the stadtholders).
- Spot checks: all confirmed except the one fixed above. Breda 1590; the 1591, 1592, 1594 and 1597 towns; Ostend 1601-04; Breda 1625 and 1637; the Meuse towns 1632; Sas van Gent 1644 and Hulst 1645 (Eighty Years' War page). Utrecht and Naarden in June 1672; Groningen 21 July-27 August 1672; Maastricht 30 June 1673; Naarden September 1673; Munster's peace in April 1674 (Franco-Dutch War page). Lille 1708-1713 (Lille page). Venlo and Echt 1713 (Generality Lands page). The Barrier on 15 November 1715 (Barrier Treaty page). Maastricht 4 November 1794.
- Area: the Dutch Republic page has no area (checked). The clipped core, about 33,000-39,000 km2, is plausible.

## Cross-dossier matrix: mismatches and missing mirrors

- kingdom-of-france (eu-10):
  - Maastricht: no 1673 gain from dutch-republic and no 1678 loss to it.
  - Lille is recorded as a 1708 loss and a 1713 gain. It should be `occupation_start`/`occupation_end` with counterpart dutch-republic (the Lille page: 'the Dutch continued to occupy the city').
  - No 1747-48 occupation of Zeelandic Flanders.
  - The 1672 occupation matches. The end is 1674 in France's dossier against 1673 here, within one year; the Franco-Dutch War page favours late 1673.
- Exceptions:
  - habsburg-netherlands (every gain and loss with Spain from 1579 to 1713, and the Barrier) and prince-bishopric-of-munster: no dossier, listed as needed.
  - brandenburg-prussia (eu-09, not written yet): the 1618-08 merge.
  - french-first-republic and batavian-republic (eu-20, not run yet).
  - The Polish suzerains (eu-15, not run yet).
