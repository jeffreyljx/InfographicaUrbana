# Review of batch eu-09-l (2026-10-25)

Dossiers: electorate-of-hanover (verdict: fix, applied by the reviewer), principality-of-liechtenstein (verdict: fail, one missing occupation).
Validator (--resolve): 0 errors on both; warnings are the unresolved gazetteer names and the counterpart slugs with no dossier yet.
Neighbour dossiers present: kingdom-of-france, swiss-confederation. All other Context polities are not written yet (exception: owned by a group that has not run).
Pages opened by the reviewer: Electorate of Hanover, History of Liechtenstein, Liechtenstein, Kingdom of Hanover, Battle of Minden, Göttingen. Grid test with tools/grid.py polity_cells at Otterndorf, Stade, Osnabrück, Kassel, Paderborn, Münster.

## electorate-of-hanover: fix (applied)

Spot checks on the Electorate of Hanover page, all confirmed:
- /ledger/0 1692 found: infobox "Elevation to Electorate: 1692"; predecessors in infobox "Principality of Calenberg; Principality of Lüneburg".
- /ledger/1 and /ledger/2 1705 gains: "In 1705, Elector George I Louis inherited the Principality of Lüneburg with the Duchy of Saxe-Lauenburg".
- /ledger/3 1715 occupation: "In 1715, he purchased the duchies of Bremen-Verden from King Frederick IV of Denmark" (infobox "Acquired Bremen-Verden: 1715").
- /ledger/5 1719 gain: "Hanover acquired Bremen-Verden in 1719."
- /ledger/6 1731 gain: "In 1731, Hanover also gained Hadeln."
- /ledger/9 1757 occupation: "In the summer of 1757, the French invaded Hanover"; "The following year" the allies expelled them; "Hanover remained unaffected for the rest of the war."
- /ledger/11 and /ledger/12 1801: "invasion of 24,000 Prussian soldiers"; "In April they arrived at ... Stade, and stayed there until October."

Fix applied:
- /identity/successors/0/land/text said "38,487 km2 in 1803"; shapes.csv gives kingdom-of-hanover_1803 = 32,047.6 km2 (1803-1804); 38,487.5 is the 1842-1863 shape. Now "32,048 km2 in 1803-1804, 38,487 km2 at its largest in 1842-1863". Re-validated: 0 errors.

Keyframes: the 1757-1761 (47,680 km2) and 1762 (42,903 km2) shapes as wrong is upheld. The 1757 shape takes in Paderborn and reaches the Münster cell, and is larger than Cliopatria's own Kingdom of Hanover after the 1814-15 gains of Hildesheim, East Frisia, Osnabrück, Lingen and north Münster (38,487 km2; Kingdom of Hanover page lists those gains). Osnabrück is already in the 1762 shape as well as from 1763; the 1763-1802 adjust verdicts are consistent with the page ("25 February 1803 ... received the Prince-Bishopric of Osnabrück in real union").

Area: the Electorate page has no infobox area, and neither does the Kingdom of Hanover page. The author's Bremen-Verden comparison (6,685 km2 on the page against Cliopatria's +6,039 km2, ratio 0.90) stands.

Thin (not blocking, for a gap-filler or the orchestrator):
- /ledger/13 dissolve 1802 (confidence 1) is Cliopatria's row boundary. The page has the electorate alive in 1803 (Osnabrück) and its infobox gives "Merged into Kingdom of Westphalia: 1807", "Re-established as Kingdom of Hanover: 1814". Orchestrator decision: either one dossier for both rows, or keep the boundary and let kingdom-of-hanover take the electorate's colour, as the author asks.
- /wars/1 Seven Years' War ends 1759 in the dossier. The pages opened stop at Minden ("ended the French threat to Hanover for the remainder of that year"). The 1760-1762 campaigns in southern Hanover (Göttingen, Münden) and the treaty year are unchecked. The author flagged this.
- /ledger/6 Land Hadeln: Cliopatria's 1721 shape, the new 1719 keyframe and the Bremen-Verden region of /ledger/3-5 (1721 minus 1713) already contain the Otterndorf cell (53.81 N, 8.90 E), 12 years before the 1731 gain. Once the gazetteer has Land Hadeln, make keyframe 1719 and the 1721 shape (for 1721-1730) adjust minus Land Hadeln, and Bremen-Verden minus Land Hadeln. Small (about 1 cell).
- /ledger/9 1757 occupation covers the whole 1744 shape. The Klosterzeven page calls it a "partial occupation", and the Hanoverian army stayed at Stade. Gap-filler: name the unoccupied districts (Stade/Bremen) or keep confidence 2.
- Osnabrück Hanoverian prince-bishops (1662-1802, alternating) are the author's gap.

Cross-checks: 1757 occupation and 1758 occupation_end match kingdom-of-france /ledger/165-166. France has no contest event for Hastenbeck (contest events are outside the matrix, noted only). Every other counterpart (swedish-empire, holy-roman-empire-minor-states, kingdom-of-prussia, principality-of-luneburg, duchy-of-saxe-lauenburg, principality-of-calenberg) has no dossier yet: exception.

## principality-of-liechtenstein: fail

Spot checks, both confirmed:
- /ledger/0 found 23 January 1719: Liechtenstein infobox "Union between Vaduz and Schellenberg: 23 January 1719"; "Charles VI, Holy Roman Emperor, decreed that Vaduz and Schellenberg were united".
- /ledger/1 loss 1949: History page "In 1949, Liechtenstein ceded the Ellhorn mountain to Switzerland as a result of Swiss demands" (Balzers refused in November 1948, the Landtag approved the following month).

Blocking finding, not applied:
- Missing French occupation of 1799, on the History of Liechtenstein page the author used: "France invaded the country on 6 March 1799 and plundered several towns"; Austrian and Vorarlberg militias "defeated 18,000 French troops stationed in Liechtenstein" and liberated the country by 14 May. Add occupation_start {year 1799, month 3, counterpart "french-directory", region {"country": "Liechtenstein", "text": ...}, confidence 3, source History_of_Liechtenstein} and occupation_end {year 1799, month 5, same counterpart}. Add the war "War of the Second Coalition" (1799-1799; belligerents principality-of-liechtenstein, french-directory, habsburg-monarchy; zone the country), with contest events if the author wants the fighting drawn.

Area: infobox 160.50 km2 against Cliopatria 136.9 km2, ratio 0.85; acknowledged in keyframe 1721.

Thin: no ruler strip (princes 1719-1814), the date Vaduz became the seat, the day of the 1949 cession. All are the author's gaps.

Cross-check: the 1949 loss to swiss-confederation has no mirror. The swiss-confederation dossier exists (1291-2024) and has no ledger event after 1900. Route a 1949 gain of the Ellhorn from principality-of-liechtenstein to its owner (eu-09).

## Gazetteer names needed
Principality of Calenberg, Principality of Grubenhagen, County of Diepholz, County of Hoya, Principality of Lüneburg, Duchy of Saxe-Lauenburg, Land Hadeln (electorate-of-hanover); Ellhorn (principality-of-liechtenstein).
