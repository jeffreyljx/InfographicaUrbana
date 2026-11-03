# Review of batch eu-09-x (Phase B)

Reviewer: adversarial review, 2026-10-25, against history/briefs/reviewer-brief.md with the orchestrator's adjustments: 4 spot checks per dossier (6 above 20 shapes), weighted to confidence-3 events and big land moves; an event whose page does not say what its note claims is fabricated; small verified fixes applied in place and re-validated.

Inputs: the 88 dossiers listed in the author's report, the author's notes (history/polities/_notes/eu-09-x.md), the report (history/notes/phase-b/reports/eu-09-x.json) and the neighbour dossiers that exist in history/polities.

## Summary

| Verdict | Count |
|---|---|
| pass | 38 |
| fix | 28 |
| thin | 8 |
| fail | 14 |

All 88 dossiers validate with 0 errors, before and after the reviewer's edits. Cross-dossier matrix: 408 territorial rows (missing 174, matched 103, exception 101, mismatch 30).

Failed: electoral-palatinate, habsburg-netherlands, electorate-of-mainz, duchy-of-brunswick-luneburg, duchy-of-cleves, landgraviate-of-hesse-rheinfels, county-of-schaumburg, swabian-circle, franconian-circle, county-of-henneberg, duchy-of-saxe-gotha-altenburg, duchy-of-saxe-weissenfels, duchy-of-saxe-merseburg, county-of-stolberg.

## Batch-level problems

- Page that would not load for the reviewer: https://en.wikipedia.org/wiki/County_of_Rochefort (url_not_found).
- swabian-circle and franconian-circle are umbrella dossiers (Imperial Circles, 1500-1806); the brief says an umbrella is never a dossier of its own. Failed here; the orchestrator should drop them or keep them as non-drawn records.
- holy-roman-empire (dossier 962-1259) was used after 1259 as a counterpart or predecessor in seven dossiers. The reviewer changed five to holy-roman-empire-minor-states (1260-1806): principality-of-hohenzollern-hechingen, prince-bishopric-of-freising, county-of-hanau, duchy-of-arenberg and county-of-stolberg. Mecklenburg's Wallenstein occupation and the two circles are left to the author or the orchestrator.
- electorate-of-saxony (outside this batch) names the secundogenitures 'saxe-weissenfels', 'saxe-merseburg' and 'saxe-zeitz' instead of the duchy-of-saxe-* slugs. Its 1656 and 1657 loss regions (5,817 and 7,081 km2) are about twice what duchy-of-saxe-weissenfels and duchy-of-saxe-merseburg draw; both duchies fail here for that reason.
- Danish slugs: kingdom-of-denmark has no dossier (its Cliopatria row ends 1406). kalmar-union, denmark-norway and kingdom-of-denmark-1814-1940 (outside this batch) draw Schleswig as Danish land; denmark-norway also names holy-roman-empire-minor-states for Gottorp Schleswig, which was never in the Empire. duchy-of-schleswig draws the duchy as a separate fief 1058-1866. The orchestrator should decide which side draws it.
- Cliopatria rows saxe-altenburg (1806-70) and saxe-coburg-and-gotha overlap duchy-of-saxe-gotha-altenburg and duchy-of-saxe-coburg-saalfeld for 1806-26 (the author flagged this). Orchestrator decision.
- As the orchestrator allowed, the reviewer made 14 small fixes, each verified, to 13 dossiers in place: years, confidence and slugs. Every one was re-validated with validate_dossier.py (0 errors) and read back after more than ten seconds, and all persisted. A change to duchy-of-guelders L7 broke occupation pairing, so it was reverted and recorded as an unapplied fix.
- Mirror events are missing in dossiers outside this batch: brandenburg-prussia (1687 Burg), prince-bishopric-of-utrecht (the Zutphen fief), electorate-of-cologne (Vest Recklinghausen 1803), holy-roman-empire-minor-states (most found events), and others listed in cross_checks with status missing.

## Applied edits (in place, re-validated, read back)

- electoral-palatinate /keyframe_review/2/to: Keyframes left 1620-1622 without a shape (K2 ended 1619, K3 starts 1623). K2 'to' set to 1622.
- electoral-palatinate /ledger/5/confidence: The 1463 Bergstrasse gain is confidence 3 with a month, but the cited page gives no date; the Heppenheim page dates the pledge 1461. Confidence lowered to 2; the author should add the Heppenheim page and say 1461 (pledge) / 1463 (Zeilsheim) in the note.
- duchy-of-wurttemberg /ledger/2/counterpart: Counterpart written as the name 'Margraviate of Baden', not the slug of the dossier in this batch. counterpart 'margraviate-of-baden'.
- electorate-of-mainz /ledger/4/confidence: Confidence 3 with month October 1463, but the Mainz Diocesan Feud page gives no date for the Bergstrasse transfer. Confidence lowered to 2.
- county-of-hanau /identity/predecessors/0/slug: The 1429 predecessor named holy-roman-empire, whose dossier ends in 1259; the author's own note says the lordship lies inside Cliopatria's Holy Roman Empire Minor States from 1260. Changed to holy-roman-empire-minor-states (re-validated: 0 errors; the 2 warnings were there before).
- further-austria /ledger/7/counterpart: The 1805 dissolve gave the Breisgau to grand-duchy-of-baden, a row that starts in 1806; Baden was the Electorate of Baden (row 1803-1805) at Pressburg. counterpart 'electorate-of-baden'.
- prince-bishopric-of-trent /ledger/1/counterpart, /ledger/2/counterpart, /identity/successors/0/slug: The 1511 vassalage and the 1803 annexation name house-of-habsburg, whose dossier ends in 1515. Counterparts and successor set to habsburg-monarchy.
- prince-bishopric-of-brixen /ledger/4/counterpart, /ledger/5/counterpart, /identity/successors/0/slug: The 1511 vassalage and the 1803 annexation name house-of-habsburg (dossier ends 1515). Counterparts and successor set to habsburg-monarchy.
- prince-bishopric-of-speyer /ledger/10/counterpart: The 1801 left-bank loss names french-first-republic, a row that ends in 1795; France in 1801 is the French Consulate. counterpart 'french-consulate'.
- prince-bishopric-of-freising /ledger/0/counterpart and /identity/predecessors/0/slug: The 1294 found event and the predecessor named holy-roman-empire, whose dossier ends in 1259. Changed to holy-roman-empire-minor-states (re-validated: 0 errors, 0 warnings).
- principality-of-hohenzollern-hechingen /ledger/0/counterpart and /identity/predecessors/0/slug: The 1576 found event and the predecessor named holy-roman-empire, whose dossier ends in 1259; the land-carrying slug after 1259 is holy-roman-empire-minor-states (1260-1806). Counterpart and predecessor changed to holy-roman-empire-minor-states (re-validated: 0 errors, 0 warnings). A County of Hohenzollern dossier (before 1576) would be the better predecessor once it exists.
- duchy-of-saxe-weissenfels /ledger/3/counterpart: The 1687 sale of Burg named electorate-of-brandenburg, whose dossier ends in 1618. Changed to brandenburg-prussia (re-validated: 0 errors, 0 warnings); brandenburg-prussia has no 1687 gain of Burg to mirror it.
- duchy-of-arenberg /identity/predecessors/0/slug: The predecessor named holy-roman-empire, whose dossier ends in 1259 (the state starts 1549). Changed to holy-roman-empire-minor-states (re-validated: 0 errors, 0 warnings).
- county-of-stolberg /ledger/7/counterpart: The 1806 end named holy-roman-empire, whose dossier ends in 1259. Changed to holy-roman-empire-minor-states (re-validated: 0 errors, 0 warnings); the real 1806-07 successors (Prussia for Wernigerode, Saxony for Stolberg and Rossla, the Kingdom of Westphalia) still need a page and the empty successors list needs filling.

## Dossiers

### electoral-palatinate: fail

Fixes:
- `/keyframe_review/2/to` (applied). Keyframes left 1620-1622 without a shape (K2 ended 1619, K3 starts 1623). Evidence: Electoral Palatinate page: the land was occupied 1621-1622 and the Upper Palatinate forfeited afterwards (ledger L9 dates the loss 1623); the state held land in 1620-1622. Fix: K2 'to' set to 1622.
- `/keyframe_review/1/correction` (not applied). The Upper Palatinate circle (11.86E 49.44N, 70 km, about 15,400 km2) is 1.6 times the region it stands for. Evidence: Upper Palatinate page infobox: 9,692 km2; K1 minus K0 is about 16,400 km2 of resolved cells. Fix: Reduce the Amberg circle to about 55 km, or note the over-draw in the K1 note.
- `/ledger/5/confidence` (applied). The 1463 Bergstrasse gain is confidence 3 with a month, but the cited page gives no date; the Heppenheim page dates the pledge 1461. Evidence: Mainz Diocesan Feud page: Frederick I was given Lorsch, Heppenheim and Bensheim 'for his assistance', no year; Heppenheim page: 'an interruption from 1461 to 1623 when the fief was pledged to the Electorate of the Palatinate'. Fix: Confidence lowered to 2; the author should add the Heppenheim page and say 1461 (pledge) / 1463 (Zeilsheim) in the note.
- `/keyframe_review/3..5 and /ledger` (not applied, blocking). The Bergstrasse (Lorsch, Heppenheim, Bensheim; circle 8.62E 49.66N 20 km) is drawn Palatine to 1777, but the pledge ended in 1623 and the land was Mainz's until 1803. Evidence: Heppenheim page: pledged to the Palatinate 'from 1461 to 1623', then 'again remained an Electoral Mainz holding until 1803', then Hesse-Darmstadt (which this batch's Darmstadt dossier already gains from Mainz in 1803). Fix: Add a 1623 loss of the Bergstrasse to electorate-of-mainz (source Heppenheim page) and drop the 8.62E 49.66N circle from K3, K4, K5 and from the L10, L11 and L17 regions.

Spot checks:
- `/ledger/7` [https://en.wikipedia.org/wiki/Electoral_Palatinate]: confirmed (occupied by Spanish and Bavarian troops 1621-1622)
- `/ledger/9` [https://en.wikipedia.org/wiki/Upper_Palatinate]: confirmed in substance; no year on either page for the land transfer (1623 is the electoral transfer), c2 is honest
- `/ledger/10` [https://en.wikipedia.org/wiki/Electoral_Palatinate]: confirmed (regained the Lower Palatinate at Westphalia 1648)
- `/ledger/17` [https://en.wikipedia.org/wiki/Electoral_Palatinate]: confirmed (personal union with Bavaria from 1777, electorates combined)
- `/ledger/5` [https://en.wikipedia.org/wiki/Mainz_Diocesan_Feud]: confirmed in substance, undated on the page (confidence lowered to 2); Heppenheim page gives 1461

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No Cliopatria row and no infobox area; resolved K0 11,128 km2, K1 27,566 km2; Upper Palatinate alone 9,692 km2 (page).

### duchy-of-wurttemberg: fix

Fixes:
- `/ledger/2/counterpart` (applied). Counterpart written as the name 'Margraviate of Baden', not the slug of the dossier in this batch. Evidence: County of Württemberg page: Stuttgart 'was included within the county as a result of the marriage between Ulrich I and Mechthild of Baden in 1251'; margraviate-of-baden is in this batch. Fix: counterpart 'margraviate-of-baden'.

Thin (for a gap-filler):
- `/ledger/10`: 1648 end of the Imperial occupation (confidence 1; the Nördlingen page cannot date it); also the 1634-1648 Habsburg grant of Württemberg lands to Catholic lords (page to try: https://en.wikipedia.org/wiki/Eberhard_III,_Duke_of_W%C3%BCrttemberg)
- `/ledger/1`: what the 1250-60 expansion took (confidence 2 and a Stuttgart circle); Urach, Tübingen (1342), Göppingen, Böblingen purchases are not in the ledger (page to try: https://en.wikipedia.org/wiki/W%C3%BCrttemberg)

Spot checks:
- `/ledger/2` [https://en.wikipedia.org/wiki/County_of_W%C3%BCrttemberg]: confirmed (1251, marriage to Mechthild of Baden)
- `/ledger/4` [https://en.wikipedia.org/wiki/County_of_W%C3%BCrttemberg]: confirmed in substance (betrothal 1397, Montbéliard absorbed after Henriette died in 1444)
- `/ledger/7` [https://en.wikipedia.org/wiki/Duchy_of_W%C3%BCrttemberg]: confirmed (6 February 1520 the Swabian League sold the duchy to Charles V)
- `/ledger/12` [https://en.wikipedia.org/wiki/Duchy_of_W%C3%BCrttemberg]: confirmed (raised to Electorate 1803)

Area: infobox 8000 km2 (None), Cliopatria 9863 km2, ratio 1.23, acknowledged True. No Cliopatria row; body text 'over 8,000 square kilometres' undated; K4 resolves to 9,863 km2 with Montbéliard.

### landgraviate-of-hesse: thin

Thin (for a gap-filler):
- `/ledger`: the 1450 Ziegenhain and Nidda inheritance (the county joined Upper and Lower Hesse) and the 1360 Schmalkalden half from Henneberg (county-of-henneberg L6 names landgraviate-of-hesse as gainer, no mirror here) (page to try: https://en.wikipedia.org/wiki/County_of_Ziegenhain)
- `/wars/0`: the war runs 1247-1264, before the state's start (it is the founding war: acceptable, but say so in its outcome) (page to try: https://en.wikipedia.org/wiki/War_of_the_Thuringian_Succession)

Spot checks:
- `/ledger/2` [https://en.wikipedia.org/wiki/Landgraviate_of_Hesse]: confirmed (divided 1308-1311)
- `/ledger/4` [https://en.wikipedia.org/wiki/Landgraviate_of_Hesse]: confirmed (again from 1458)
- `/ledger/6` [https://en.wikipedia.org/wiki/Landgraviate_of_Hesse]: confirmed (re-unified under William II in 1500)
- `/ledger/7` [https://en.wikipedia.org/wiki/Landgraviate_of_Hesse]: confirmed (1567 division between the sons)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No infobox area; resolved K0 17,703 km2, K1 21,749 km2 (radius reading, soft).

### landgraviate-of-hesse-kassel: fix

Fixes:
- `/ledger/5` (not applied). One event gives both Schaumburg and the Hersfeld abbey lands (9.71E 50.87N) to county-of-schaumburg as counterpart; that dossier ends in 1640, and Hersfeld was a separate imperial abbey. Evidence: Hesse-Kassel page: at Westphalia it 'gained most of the County of Schaumburg and the secularized Hersfeld Abbey'; county-of-schaumburg ends 1640 with its partition (author's own problems list). Fix: Split into two gains: Schaumburg share (counterpart 'nobody' or the Schaumburg successor, with the 1640 partition explained in the note) and Hersfeld (counterpart 'imperial-abbey-of-hersfeld', listed under counterparts_needing_dossiers).
- `/ledger/1` (not applied). The 1583 Rheinfels inheritance was 'shared between the other three' lines, but only Kassel gains; neither Darmstadt nor Marburg records a share. Evidence: Hesse-Kassel page: 'The Rheinfels branch died out in 1583 and was shared between the other three.' Fix: Say in the note which part Kassel took (Rheinfels/St. Goar) and add small 1583 gains to the Darmstadt and Marburg dossiers, or state that their shares are not drawn.

Spot checks:
- `/ledger/2` [https://en.wikipedia.org/wiki/Landgraviate_of_Hesse-Kassel]: confirmed (1604 Maurice inherited Hesse-Marburg)
- `/ledger/5` [https://en.wikipedia.org/wiki/Landgraviate_of_Hesse-Kassel]: confirmed (most of Schaumburg and Hersfeld at Westphalia)
- `/ledger/7` [https://en.wikipedia.org/wiki/Seven_Years%27_War]: confirmed for Marburg ('The French captured Marburg in Hesse' 1760); Kassel is implied by the 1761 siege and 1762 capture of Cassel
- `/ledger/9` [https://en.wikipedia.org/wiki/Landgraviate_of_Hesse-Kassel]: confirmed (1801 forced to cede land to France; the page names no towns, c2 honest)

Area: infobox 6100 km2 (1583), Cliopatria 7840 km2, ratio 1.29, acknowledged True. Infobox has none; footnote (Wilson) gives 6,100 km2 for the senior line after the Rheinfels division; K1 resolves to 7,840 km2.

### landgraviate-of-hesse-darmstadt: fix

Fixes:
- `/ledger/6` (not applied). The 1803 gains name Cologne and Mainz but not the Prince-Bishopric of Worms, whose dossier (this batch) dissolves in 1802 into this state. Evidence: Hesse-Darmstadt page: territories 'from the Prince-Archbishop of Mainz and the Prince-Bishop of Worms'; prince-bishopric-of-worms L3 1802 dissolve, counterpart landgraviate-of-hesse-darmstadt. Fix: Add a 1803 gain from prince-bishopric-of-worms (the right-bank Worms lands round Lampertheim), or widen L6's note and counterpart list.
- `/ledger/7` (not applied). The 1803 loss of Hanau-Lichtenberg to France is not on the Hesse-Darmstadt page; it rests on the Hanau-Lichtenberg page only. Evidence: Hesse-Darmstadt page does not mention the loss; the left-bank Alsace lands were French from 1792-1801 (Lunéville). Fix: Check the year on County of Hanau-Lichtenberg (the left-bank part was lost by 1801 at Lunéville); keep c2.

Spot checks:
- `/ledger/3` [https://en.wikipedia.org/wiki/Landgraviate_of_Hesse-Darmstadt]: confirmed (1648 Marburg to the Kassel line)
- `/ledger/4` [https://en.wikipedia.org/wiki/Landgraviate_of_Hesse-Darmstadt]: confirmed (Hanau-Lichtenberg inherited 1736)
- `/ledger/5` [https://en.wikipedia.org/wiki/Landgraviate_of_Hesse-Darmstadt]: confirmed (Duchy of Westphalia 1803)
- `/ledger/2` [https://en.wikipedia.org/wiki/Landgraviate_of_Hesse-Darmstadt]: confirmed as c2 (1627 agreement, no land named)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No infobox area; resolved 3,288-13,657 km2 across keyframes.

### habsburg-netherlands: fail

Fixes:
- `/ledger/39/region and /keyframe_review/17` (not applied, blocking). Ryswick (1697) is drawn returning Ypres, Tournai, Oudenaarde and Veurne, which the note itself calls 'a bridging assumption'; the treaty page names only Luxembourg, Mons and Kortrijk. Evidence: Peace of Ryswick page: 'French forces also evacuated Catalonia, Luxembourg, Mons and Kortrijk in the Spanish Netherlands'; Ypres, Tournai, Menin and Veurne stayed French until the Utrecht settlement (1713). Fix: Limit L39 to Luxembourg, Mons and Kortrijk (and Diksmuide if the Reunions page supports it); keep Ypres, Tournai, Menin and Veurne out of K17 until a 1713 gain from kingdom-of-france sourced on the Treaty of Utrecht or Barrier Treaty page; split K17 at 1713.
- `/keyframe_review/9..17 and /ledger` (not applied, blocking). The 1637 events are missing: the Dutch retook Breda and Spain retook Venlo and Roermond; Upper Guelders (Roermond) is drawn Dutch from 1632 to 1795 although the K10 note admits Spain retook it in 1637. Evidence: Eighty Years' War page: 'the Dutch took it back in 1637' (Breda); Spanish Netherlands page lists the Upper Quarter of Guelders round Venlo and Roermond among the Habsburg territories; dutch-republic records both a 1637 gain and a 1637 loss against habsburg-netherlands. Fix: Add 1637 loss of Breda and 1637 gain of Venlo and Roermond (counterpart dutch-republic); keep Breda inside K9-K10 until 1637; draw Upper Guelders (Roermond, Venlo until 1713/15) in K10-K17 and add the Utrecht-era transfers (Geldern to Prussia, Venlo to the Dutch) when sourced.
- `/ledger/10, /ledger/11 and 1588-1606` (not applied, blocking). The north-east (Groningen, Overijssel, Drenthe) is drawn lost in 1580 and never regained, while dutch-republic records gains from habsburg-netherlands in 1588, 1591, 1592, 1594, 1597, 1604, 1606 that this ledger never mirrors (Rennenberg's 1580 defection put Groningen back under Spain until 1594). Evidence: Union of Utrecht page dates Groningen's and Overijssel/Drenthe's signatures to February and April 1580 (confirmed), but the dutch-republic dossier's ledger takes those lands from habsburg-netherlands in 1591-1597; one of the two is wrong and they cannot both be drawn. Fix: Open the Eighty Years' War and George van Lalaing (Rennenberg) pages; add the 1580 regain of Groningen and the north-east and the 1590s losses to the Dutch (Maurice's campaigns), or argue in notes why the Dutch dossier is wrong.
- `/wars/0 and /keyframe_review/5` (not applied). The Revolt is entered only from 1579; Holland and Zeeland, in rebel hands from 1572 and under the States General from 1576, are drawn plain Habsburg until 1578. Evidence: Eighty Years' War page: the war runs from 1568; the war entry here starts 1579. Fix: Start the war in 1568 and add a 1572 contest_start (or occupation) for Holland and Zeeland with the page's dates.
- `/ledger/22` (not applied). Dunkirk's counterpart is kingdom-of-england in 1659, but England was the Commonwealth/Protectorate then; commonwealth-of-england records a 1658 gain of Dunkirk from kingdom-of-france. Evidence: Spanish Netherlands page: under the Treaty of the Pyrenees 1659 'Dunkirk was ceded to the English'; commonwealth-of-england ledger: 1658 gain, counterpart kingdom-of-france. Fix: Enter Dunkirk lost in 1658 (taken after the Battle of the Dunes and handed to the English) with counterpart commonwealth-of-england, or keep 1659 with counterpart commonwealth-of-england and a note.
- `/wars/5/zones` (not applied). Nine Years' War has no zones, but Mons (1691-1697) and Namur (1692-1695) changed hands on this front. Evidence: Peace of Ryswick page: France 'evacuated ... Mons'. Fix: Add zones round Mons and Namur, or occupation events.

Thin (for a gap-filler):
- `/ledger/29`: Courtrai's return 1678 is confidence 1 (page to try: https://en.wikipedia.org/wiki/Treaties_of_Nijmegen)
- `/ledger/46`: end of the Barrier garrisons 1781 is confidence 1 (page to try: https://en.wikipedia.org/wiki/Barrier_Treaty)

Spot checks:
- `/ledger/15` [https://en.wikipedia.org/wiki/Eighty_Years%27_War]: confirmed (Breda retaken 1625)
- `/ledger/16` [https://en.wikipedia.org/wiki/Eighty_Years%27_War]: confirmed ('s-Hertogenbosch 1629)
- `/ledger/17` [https://en.wikipedia.org/wiki/Eighty_Years%27_War]: confirmed (Venlo, Roermond, Maastricht 1632)
- `/ledger/19` [https://en.wikipedia.org/wiki/Eighty_Years%27_War]: confirmed (Hulst 1645)
- `/ledger/22` [https://en.wikipedia.org/wiki/Spanish_Netherlands]: confirmed (1659 Dunkirk ceded to the English)
- `/ledger/40` [https://en.wikipedia.org/wiki/Spanish_Netherlands]: confirmed (Anglo-Dutch condominium from 1706)
- `/ledger/10` [https://en.wikipedia.org/wiki/Union_of_Utrecht]: confirmed as written (Lier, Bruges and Groningen city sign February 1580)
- `/ledger/39` [https://en.wikipedia.org/wiki/Peace_of_Ryswick]: not on page for Ypres, Tournai, Oudenaarde, Veurne (page: Luxembourg, Mons, Kortrijk)

Area: infobox 70000 km2 (1560), Cliopatria 85733 km2, ratio 1.22, acknowledged True. Spanish Netherlands infobox: 70,000 km2 (1560), 46,000 km2 (1600); K5 85,733 and K8 57,155 km2 resolved (ratios 1.22 and 1.24); author quotes 77,000/53,000.

### electorate-of-cologne: pass

Thin (for a gap-filler):
- `/ledger/2`: capital move to Bonn is confidence 1 at 1288; the infobox gives Bonn only 1597-1794 (page to try: https://en.wikipedia.org/wiki/Bonn)

Spot checks:
- `/ledger/1` [https://en.wikipedia.org/wiki/Duchy_of_Westphalia]: confirmed (1180 Barbarossa gave the duchy to Philip of Heinsberg)
- `/ledger/4` [https://en.wikipedia.org/wiki/Duchy_of_Westphalia]: confirmed (Werl-Arnsberg sold 1368)
- `/ledger/7` [https://en.wikipedia.org/wiki/Duchy_of_Westphalia]: confirmed (Soest to Cleves after the feud, 1449)
- `/ledger/12` [https://en.wikipedia.org/wiki/Electorate_of_Cologne]: confirmed (occupied by France 1794)
- `/ledger/15` [https://en.wikipedia.org/wiki/Electorate_of_Cologne]: confirmed (Westphalia to Hesse-Darmstadt 1803)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No infobox area; resolved 6,322-11,633 km2.

Tried: Years against two pages, the Worringen loss against free-imperial-city-of-cologne (matched), the 1803 loss against Darmstadt (matched); the 1449 Soest loss has no mirror in duchy-of-cleves (a fault of that dossier).

### electorate-of-mainz: fail

Fixes:
- `/ledger/4/confidence` (applied). Confidence 3 with month October 1463, but the Mainz Diocesan Feud page gives no date for the Bergstrasse transfer. Evidence: Mainz Diocesan Feud page: Lorsch, Heppenheim and Bensheim given to Frederick I, no year; Heppenheim page: pledge 1461-1623. Fix: Confidence lowered to 2.
- `/keyframe_review/4..7 and /ledger` (not applied, blocking). No 1623 return of the Bergstrasse: K5-K7 leave Lorsch/Heppenheim/Bensheim outside Mainz until 1803, while Darmstadt's 1803 gain from Mainz is drawn exactly there. Evidence: Heppenheim page: the pledge to the Palatinate lasted 'from 1461 to 1623', then 'an Electoral Mainz holding until 1803'. Fix: Add a 1623 gain of the Bergstrasse from electoral-palatinate (source Heppenheim page), split K4 at 1623 and add the 8.62E 49.66N circle to the keyframes from 1623 and to the 1803 loss.
- `/ledger/13` (not applied). The Rheingau circle (8.05E 50.02N) is given to Hesse-Darmstadt in 1803; the page gives the Main lands below Frankfurt to Hesse-Darmstadt 'and the Nassau princes'. Evidence: Electorate of Mainz page: 'its right bank areas along the Main below Frankfurt to Hesse-Darmstadt' and the Nassau princes; the Rheingau went to Nassau-Usingen. Fix: Split L13: the Rheingau to county-of-nassau (this batch; it needs the mirror gain), the Main and Bergstrasse lands to landgraviate-of-hesse-darmstadt.

Spot checks:
- `/ledger/2` [https://en.wikipedia.org/wiki/Electorate_of_Mainz]: confirmed (Free City 1242-1462)
- `/ledger/3` [https://en.wikipedia.org/wiki/Mainz_Diocesan_Feud]: confirmed (night of 28 October 1462)
- `/ledger/4` [https://en.wikipedia.org/wiki/Mainz_Diocesan_Feud]: confirmed in substance, undated (lowered to 2)
- `/ledger/12` [https://en.wikipedia.org/wiki/Electorate_of_Mainz]: confirmed (Eichsfeld and Erfurt to Prussia 1803)
- `/ledger/14` [https://en.wikipedia.org/wiki/Electorate_of_Mainz]: confirmed (Dalberg kept Aschaffenburg)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No infobox area (population 336,000 in 1760); resolved 8,852-11,128 km2.

### prince-bishopric-of-munster: fix

Fixes:
- `/ledger/2/counterpart` (not applied). Cloppenburg (1403) is taken from county-of-oldenburg, which records no such loss; the page names no seller. Evidence: Prince-Bishopric of Münster page: 'the Cloppenburg district' gained 1403, no seller; county-of-oldenburg has no 1403 event. Fix: Counterpart 'county-of-tecklenburg' (the usual seller; already a counterpart in county-of-lippe) with a page, or 'nobody' with a note; keep c2.
- `/ledger/10` (not applied). The 1803 dissolve gives the whole remainder to Prussia; the page shares it among Prussia, Oldenburg, Arenberg, Looz-Corswarem, Salm and Croÿ. Evidence: Page: Prussia 'took possession in March 1803'; 'Arenberg, Looz-Corswarem, Salm, and Croÿ received other parts as compensation'. Fix: Limit the Prussian share to the Oberstift round Münster (the Erbmünsterland) and add losses to Salm (Bocholt, Ahaus), Looz-Corswarem (Rheine-Wolbeck) and Croÿ (Dülmen), listed under counterparts_needing_dossiers.
- `/wars/2/zones` (not applied). The Franco-Dutch War entry has no zones, but Galen's troops held Dutch land (Overijssel, the siege of Groningen) in 1672-1674. Evidence: Christoph Bernhard von Galen page (cited by the dossier) and the war's own name; 'no zones' needs a note that no ground changed hands, which is not the case. Fix: Add a zone (Overijssel and Drenthe) or say in the war's outcome that the occupied Dutch land is drawn in the Dutch dossier.

Spot checks:
- `/ledger/1` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_M%C3%BCnster]: confirmed (1252 Vechta and Meppen)
- `/ledger/3` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_M%C3%BCnster]: confirmed (Ahaus and Stromberg 1406)
- `/ledger/4` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_M%C3%BCnster]: confirmed (Wildeshausen in pledge from Bremen 1429)
- `/ledger/8` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_M%C3%BCnster]: confirmed (Oldenburg received Vechta and Cloppenburg)
- `/ledger/12` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_M%C3%BCnster]: confirmed (Prussia took possession March 1803)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved K6 15,427 km2 (likely generous: the 45 km Münster circle alone is 6,360 km2).

### county-of-tyrol: fix

Fixes:
- `/keyframe_review/1/correction` (not applied). K1 takes all of the Tirol and Bozen admin units, which contain the Prince-Bishopric of Brixen drawn in this batch (circle round Brixen), so the two double-draw 1271-1362. Evidence: prince-bishopric-of-brixen K1 1091-1802 lies inside admin1 Bozen/Tirol; the County of Tyrol page does not say Meinhard took the bishops' lands. Fix: Subtract the Brixen circle from K1 (or draw Brixen as a Tyrolean vassal there and say so).
- `/wars/1` (not applied). The Tyrolean succession war runs 1363-1369, after the state's end; it is the Habsburg-Wittelsbach war over the land, not this state's war. Evidence: County of Tyrol page: 1363 Margaret 'bequeathed the county to Rudolph IV'. Fix: Move it to the Habsburg and Bavarian dossiers or cut it to 1363.

Thin (for a gap-filler):
- `/ledger/2`: how the county grew from the Meran circle (K0) to all of Tyrol (K1) is one confidence-1 event at 1271 with unnamed counterparts (Andechs inheritance 1248, the bishops' advocacies) (page to try: https://en.wikipedia.org/wiki/Meinhard_II_of_Tyrol)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_Tyrol]: confirmed (documented from about 1140)
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Tyrol]: confirmed (1253 Meinhard of Gorizia inherits)
- `/ledger/3` [https://en.wikipedia.org/wiki/County_of_Tyrol]: confirmed (1342 marriage to Louis V)
- `/ledger/4` [https://en.wikipedia.org/wiki/County_of_Tyrol]: confirmed (1363 bequeathed to Rudolph IV)

Area: infobox 26482 km2 (1914), Cliopatria 19979 km2, ratio 0.75, acknowledged True. Infobox 26,482 km2 is the crown land with Trentino; K1 19,979 km2 without the Trent bishopric.

### duchy-of-brunswick-luneburg: fail

Fixes:
- `/ledger/9 and /identity/end` (not applied, blocking). The 1692 dissolve hands all six Welf circles, Wolfenbüttel and Lüneburg included, to electorate-of-hanover, which itself takes only Calenberg in 1692 and Lüneburg in 1705; Wolfenbüttel is then drawn by nobody until 1806. Evidence: Duchy of Brunswick-Lüneburg page: Wolfenbüttel 'retained its independence' through 1806; Lüneburg united with Calenberg on George William's death in 1705; electorate-of-hanover ledger: 1692 found from principality-of-calenberg, 1705 gain from principality-of-luneburg. Fix: Give only Calenberg-Göttingen to Hanover in 1692; carry Lüneburg to 1705 and Wolfenbüttel to 1806 (either continue this dossier as the Wolfenbüttel duchy, or end it at the 1269 partition and list principality-of-luneburg, principality-of-calenberg and principality-of-brunswick-wolfenbuttel under counterparts_needing_dossiers, as Hanover's predecessors expect).

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Duchy_of_Brunswick-L%C3%BCneburg]: confirmed (1235 Court of Mainz)
- `/ledger/4` [https://en.wikipedia.org/wiki/Hildesheim_Diocesan_Feud]: confirmed (Quedlinburg Recess 13 May 1523)
- `/ledger/5` [https://en.wikipedia.org/wiki/Hildesheim_Diocesan_Feud]: confirmed (Great Stift Ämter to Wolfenbüttel and Calenberg)
- `/ledger/8` [https://en.wikipedia.org/wiki/Hildesheim_Diocesan_Feud]: confirmed (1643 Main Treaty returned most territories)
- `/ledger/9` [https://en.wikipedia.org/wiki/Duchy_of_Brunswick-L%C3%BCneburg]: mis-drawn: 1692 electorate confirmed, but Wolfenbüttel stayed separate and Lüneburg joined only in 1705

Area: infobox 21170 km2 (1635), Cliopatria 26302 km2, ratio 1.24, acknowledged True. Infobox 21,170 km2 (1635) against K3 26,302 km2.

### margraviate-of-baden: fix

Fixes:
- `/ledger (1535)` (not applied). The 1771 merge of the 'Baden-Baden line' has no matching 1535 split. Evidence: Margraviate of Baden page: 'a fresh division of their inheritance' in 1535 created Baden-Baden and Baden-Durlach; 'The two parts were reunited in 1771'. Fix: Add a 1535 split (no new dossier; both lines kept inside, as the notes say) so the 1771 merge has its start.
- `/ledger/1` (not applied). The 1190 event is a gain from 'nobody' at confidence 1, but the page gives 1190 as the founding of the Hachberg cadet line, not an acquisition; the Markgräflerland (Sausenberg, Rötteln) circle is drawn from 1190. Evidence: Page: Baden-Hochberg 'Founded in 1190' and lasted until 1418. Fix: Re-type L1 as a split (or note), and date the Hachberg return (1415/1418) and the Rötteln-Sausenberg inheritance (1503) with a page, moving the 7.65E 47.75N circle to its true start.

Thin (for a gap-filler):
- `/ledger/1`: how and when the Breisgau and Markgräflerland lands came (Hachberg 1190/1415, Sausenberg 1306/1503) (page to try: https://en.wikipedia.org/wiki/Margraviate_of_Baden-Hachberg)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Margraviate_of_Baden]: confirmed (named a margraviate in 1112)
- `/ledger/2` [https://en.wikipedia.org/wiki/Margraviate_of_Baden]: confirmed (seat to Pforzheim 1219)
- `/ledger/3` [https://en.wikipedia.org/wiki/Margraviate_of_Baden]: confirmed (half of Lahr and Mahlberg 1442)
- `/ledger/6` [https://en.wikipedia.org/wiki/Margraviate_of_Baden]: confirmed (reunited 1771)

Area: infobox 3500 km2 (1771), Cliopatria 3035 km2, ratio 0.87, acknowledged True. Text: 3,500 km2 after 1771; K2 3,035 km2.

### prince-bishopric-of-wurzburg: thin

Thin (for a gap-filler):
- `/keyframe_review/0`: one 40 km stand-in circle for 635 years; no territorial events between 1168 and 1803 (the page gives none); the Swedish occupation is dated 1633 (the duchy grant) while the sibling Bamberg dossier starts it in 1631 (page to try: https://en.wikipedia.org/wiki/Duchy_of_Franconia_(1633))

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_W%C3%BCrzburg]: confirmed (1168 ducal rights in Eastern Franconia)
- `/ledger/1` [https://en.wikipedia.org/wiki/Bernhard_of_Saxe-Weimar]: confirmed (1633 granted Würzburg and Bamberg; c2 honest, citation-needed on the page)
- `/ledger/2` [https://en.wikipedia.org/wiki/Bernhard_of_Saxe-Weimar]: confirmed (Würzburg lost in the debacle of 1634)
- `/ledger/3` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_W%C3%BCrzburg]: confirmed (25 February 1803 to Bavaria)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; stand-in circle 5,311 km2 (acknowledged in notes).

### prince-bishopric-of-bamberg: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Bamberg]: confirmed (immediacy about 1245)
- `/ledger/1` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Bamberg]: confirmed as c2 (bishop fled in 1631)
- `/ledger/3` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Bamberg]: confirmed (Carinthian estates sold to Maria Theresa 1759)
- `/ledger/4` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Bamberg]: confirmed (Bavarian occupation 1802)
- `/ledger/6` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Bamberg]: confirmed (25 February 1803 annexed to Bavaria)

Area: infobox 3580 km2 (1802), Cliopatria 4552 km2, ratio 1.27, acknowledged True. Text 3,580 km2 at mediatisation; K1 4,552 km2 resolved (the author calibrated the circle to the page).

Tried: Five events on the page, the 1803 mirror in duchy-of-bavaria (matched), the Carinthian sale (the Habsburg dossier has no 1759 mirror: that dossier's gap). Could not break.

### duchy-of-julich-berg: pass

Spot checks:
- `/ledger/1` [https://en.wikipedia.org/wiki/Duchy_of_J%C3%BClich]: confirmed (1356 William V raised to duke)
- `/ledger/2` [https://en.wikipedia.org/wiki/Duchy_of_J%C3%BClich]: confirmed (amalgamated with Berg 1423)
- `/ledger/3` [https://en.wikipedia.org/wiki/Duchy_of_J%C3%BClich]: confirmed (Ravensberg 1437)
- `/ledger/5` [https://en.wikipedia.org/wiki/War_of_the_J%C3%BClich_Succession]: confirmed (23 July 1609 Jülich to Archduke Leopold)
- `/ledger/6` [https://en.wikipedia.org/wiki/War_of_the_J%C3%BClich_Succession]: confirmed (garrison surrendered 1 September 1610)
- `/ledger/8` [https://en.wikipedia.org/wiki/War_of_the_J%C3%BClich_Succession]: confirmed (12 November 1614, Ravensberg to Brandenburg)
- `/ledger/13` [https://en.wikipedia.org/wiki/Duchy_of_J%C3%BClich]: confirmed (Lunéville 1801 cession)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 3,035-8,346 km2.

Tried: Seven events against two pages, the Berg (1423) and Ravensberg (1437) mirrors (matched), the capital Düsseldorf inside the Berg circle; could not break. The 1614 mirror in electorate-of-brandenburg names 'julich-cleves-berg' (that dossier's fault, flagged by the author).

### duchy-of-cleves: fail

Fixes:
- `/ledger (1449) and /keyframe_review/1` (not applied, blocking). Soest, lost by Cologne to Cleves at the end of the Soest Feud, is missing: no 1449 gain, and the Mark circle (7.55E 51.52N 31 km) stops about 40 km short of Soest, so the town is drawn by nobody 1449-1614. Evidence: Duchy of Westphalia page: Soest 'passed to the Duchy of Cleves after the Soest Feud, which lasted until 1449'; electorate-of-cologne L7 1449 loss, counterpart duchy-of-cleves, has no mirror here. Fix: Add a 1449 gain from electorate-of-cologne (Soest, 8.11E 51.57N 15 km, source Duchy of Westphalia page), split K1 at 1449 and add the circle to K1-K2 and the 1614 dissolve; add the Soest Feud to wars.

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Duchy_of_Cleves]: confirmed (first documented lord 1092)
- `/ledger/1` [https://en.wikipedia.org/wiki/Duchy_of_Cleves]: confirmed (1368 to Adolf III of the Marck)
- `/ledger/2` [https://en.wikipedia.org/wiki/Duchy_of_Cleves]: confirmed (personal union with Mark from 1391)
- `/ledger/3` [https://en.wikipedia.org/wiki/Duchy_of_Cleves]: confirmed (duchy 1417)
- `/ledger/6` [https://en.wikipedia.org/wiki/War_of_the_J%C3%BClich_Succession]: confirmed (Cleves-Mark to Brandenburg, 12 November 1614)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 3,035 / 6,828 km2.

### duchy-of-guelders: fix

Fixes:
- `/ledger/7` (not applied). The 1492 occupation end names duchy-of-burgundy, which ends in 1482; the page has Maximilian (Habsburg) ruling Guelders until the 1492 recognition of Charles of Egmond. Evidence: Duchy of Guelders page: 'Guelders was ruled by Habsburg Holy Roman Emperor Maximilian I'; in 1492 the citizens, 'disillusioned with Maximilian', recognized Charles of Egmond; duchy-of-burgundy's dossier ends 1482. Fix: Add a 1482 occupation_end (duchy-of-burgundy) and occupation_start (habsburg-netherlands), and make L7's counterpart habsburg-netherlands; habsburg-netherlands needs the mirror occupation 1482-1492. (Changing L7 alone leaves the validator's pairing broken, so the reviewer did not apply it.)

Thin (for a gap-filler):
- `/ledger/2`: the growth from the Geldern and Zutphen circles to the whole duchy (Veluwe, Nijmegen, Betuwe, Upper Quarter) is one confidence-1 event at 1339; the page says Veluwe and Nijmegen came as collateral, undated (page to try: https://en.wikipedia.org/wiki/Nijmegen)

Spot checks:
- `/ledger/1` [https://en.wikipedia.org/wiki/Duchy_of_Guelders]: confirmed (Gerard II 'in 1127 acquired the County of Zutphen')
- `/ledger/3` [https://en.wikipedia.org/wiki/Duchy_of_Guelders]: confirmed (duke 1339)
- `/ledger/6` [https://en.wikipedia.org/wiki/Duchy_of_Guelders]: confirmed (to Burgundy on Arnold's death 1473)
- `/ledger/9` [https://en.wikipedia.org/wiki/Duchy_of_Guelders]: confirmed (1543 Treaty of Venlo)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; gazetteer region Guelders about 9,100 km2.

### county-of-hainaut: pass

Spot checks:
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Hainaut]: confirmed (1067 Baldwin VI rules Hainaut and Flanders)
- `/ledger/5` [https://en.wikipedia.org/wiki/County_of_Hainaut]: confirmed as c2 (Bavaria-Straubing 1356-1432)
- `/ledger/8` [https://en.wikipedia.org/wiki/County_of_Hainaut]: confirmed (1432 cession to Philip; infobox 1432)
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_Hainaut]: confirmed (consolidation ±880, c2)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 7,334 km2 (modern province Hainaut 3,786 km2 plus Valenciennes and Avesnes circles).

Tried: Dynastic years on the page, the 1432 dissolve against duchy-of-burgundy (matched). The county lived on inside the Burgundian/Habsburg Netherlands to 1797 (page), which habsburg-netherlands draws; ending here in 1432 is consistent.

### duchy-of-pomerania: fix

Fixes:
- `/ledger/2/counterpart` (not applied). Counterpart is the sentence 'page names no previous holder', not a slug. Evidence: Duchy of Pomerania page: 'extended by the Lands of Schlawe and Stolp in 1317', no cedent named. Fix: Use 'nobody' with the explanation in the note, or margraviate-of-brandenburg with a page for the Treaty of Templin cession.
- `/ledger/6` (not applied). Lauenburg and Bütow dated 1466 (c2) while the duchy page gives 1455. Evidence: Duchy of Pomerania page: the land was added 'in 1455'. Fix: Say in the note that 1455 is the pledge and 1466 the Second Peace of Thorn, citing the Lauenburg and Bütow Land page sentence; keep c2.

Spot checks:
- `/ledger/1` [https://en.wikipedia.org/wiki/Duchy_of_Pomerania]: confirmed (Landin: lost the Uckermark)
- `/ledger/4` [https://en.wikipedia.org/wiki/Duchy_of_Pomerania]: confirmed (Stolp pawned to the Teutonic Order 1329-1341)
- `/ledger/3` [https://en.wikipedia.org/wiki/Duchy_of_Pomerania]: confirmed (Rügen 1325)
- `/ledger/8` [https://en.wikipedia.org/wiki/Duchy_of_Pomerania]: confirmed (Swedish occupation 1630)
- `/ledger/10` [https://en.wikipedia.org/wiki/Duchy_of_Pomerania]: confirmed (Bogislaw XIV died 10 March 1637)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 23,773-31,360 km2 from Cliopatria's 1187 Pomerania outline.

### county-of-oldenburg: pass

Thin (for a gap-filler):
- `/ledger/8`: the 1805 end is confidence 1 (a cut to meet the eu-20 duchy-of-oldenburg row in 1806; the page gives no 1805 event) (page to try: https://en.wikipedia.org/wiki/Duchy_of_Oldenburg)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_Oldenburg]: confirmed (first mentioned 1108)
- `/ledger/2` [https://en.wikipedia.org/wiki/County_of_Oldenburg]: confirmed (1624 Knipphausen and Varel)
- `/ledger/3` [https://en.wikipedia.org/wiki/County_of_Oldenburg]: confirmed (1647 Delmenhorst finally united)
- `/ledger/5` [https://en.wikipedia.org/wiki/County_of_Oldenburg]: confirmed (duchy 1774)
- `/ledger/7` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_M%C3%BCnster]: confirmed (Vechta and Cloppenburg to Oldenburg)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 2,529-6,575 km2.

### prince-bishopric-of-hildesheim: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Hildesheim]: confirmed (Mainz Reichstag 15 August 1235)
- `/ledger/2` [https://en.wikipedia.org/wiki/Hildesheim_Diocesan_Feud]: confirmed (Quedlinburg Recess 13 May 1523)
- `/ledger/3` [https://en.wikipedia.org/wiki/Hildesheim_Diocesan_Feud]: confirmed (Small Stift: 4 of 22 Ämter, Hildesheim, Peine)
- `/ledger/5` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Hildesheim]: confirmed (1643 restitution, Aerzen and Grohnde kept by the Welfs)
- `/ledger/6` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Hildesheim]: confirmed (1803 to Prussia)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 506-3,541 km2.

Tried: Feud and restitution dates on two pages, the 1523 and 1643 mirrors in duchy-of-brunswick-luneburg (matched), the Small Stift circles against the page's four Ämter; could not break. The 1803 Prussian mirror names holy-roman-empire-minor-states (Prussia's dossier).

### prince-bishopric-of-osnabruck: thin

Thin (for a gap-filler):
- `/keyframe_review/0`: a 30 km stand-in circle for 1225-1802; the page gives no area or districts (Wiedenbrück exclave, Fürstenau, Iburg) (page to try: https://de.wikipedia.org/wiki/Hochstift_Osnabr%C3%BCck)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Osnabr%C3%BCck]: confirmed (created on collapse of Saxony 1225)
- `/ledger/1` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Osnabr%C3%BCck]: confirmed (1648 alternation with Brunswick-Lüneburg bishops)
- `/ledger/2` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Osnabr%C3%BCck]: confirmed (1803 into the Electorate of Hanover); note electorate-of-hanover's dossier ends 1802

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; stand-in 3,288 km2.

### prince-bishopric-of-paderborn: thin

Thin (for a gap-filler):
- `/keyframe_review/0`: a 28 km stand-in circle for 1281-1801; no territorial events (the page gives none) (page to try: https://de.wikipedia.org/wiki/Hochstift_Paderborn)
- `/wars/0`: Soest Feud entry has no zones and no note that no Paderborn ground changed hands (page to try: https://en.wikipedia.org/wiki/Soest_Feud)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Paderborn]: confirmed (1281 regalia from Rudolph of Habsburg)
- `/ledger/1` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Paderborn]: confirmed (1802 became Prussian)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; stand-in 2,782 km2.

### principality-of-ansbach: thin

Thin (for a gap-filler):
- `/keyframe_review/0`: a 28 km stand-in circle for 1398-1791; the 1420-1440 reunion with Bayreuth under Frederick VI (page: 11 June 1420) is not entered (page to try: https://en.wikipedia.org/wiki/Principality_of_Ansbach)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Principality_of_Ansbach]: confirmed (21 January 1398)
- `/ledger/1` [https://en.wikipedia.org/wiki/Principality_of_Ansbach]: confirmed (21 September 1440 division, Albert gets Ansbach)
- `/ledger/2` [https://en.wikipedia.org/wiki/Principality_of_Ansbach]: confirmed (2 December 1791 sold to Prussia)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; stand-in 2,782 km2.

### principality-of-bayreuth: thin

Thin (for a gap-filler):
- `/keyframe_review/0`: two stand-in circles for 1398-1791; no territorial events (page to try: https://de.wikipedia.org/wiki/F%C3%BCrstentum_Bayreuth)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Principality_of_Bayreuth]: confirmed (21 January 1398)
- `/ledger/1` [https://en.wikipedia.org/wiki/Principality_of_Bayreuth]: confirmed (Bayreuth from 1604)
- `/ledger/2` [https://en.wikipedia.org/wiki/Principality_of_Bayreuth]: confirmed (20 January 1769 inherited by Ansbach)
- `/ledger/3` [https://en.wikipedia.org/wiki/Principality_of_Bayreuth]: confirmed (2 December 1791)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; stand-in 3,794 km2.

### county-of-east-frisia: fix

Fixes:
- `/keyframe_review/0` (not applied). K0 draws the Jeverland inside East Frisia from 1464, but the page says it was not part of the county; Edzard I only gained a contested hold on Jever in 1517. Evidence: County of East Frisia page: 'Edzard I gained control of Jever in 1517 ... contested'; in 1575 East Frisia 'definitively lost the Jeverland to Oldenburg'. Fix: Split K0 at 1517 (Jever circle only from 1517, or drawn as contested), and add a 1517 gain (counterpart 'lordship-of-jever', needing a dossier, or 'nobody').

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_East_Frisia]: confirmed (imperial count 1464)
- `/ledger/2` [https://en.wikipedia.org/wiki/County_of_East_Frisia]: confirmed (1575 Jeverland lost to Oldenburg)
- `/ledger/3` [https://en.wikipedia.org/wiki/County_of_East_Frisia]: confirmed (Treaty of Berum 1600)
- `/ledger/4` [https://en.wikipedia.org/wiki/County_of_East_Frisia]: confirmed (Accord of Osterhusen 1611, Leerort garrison)
- `/ledger/7` [https://en.wikipedia.org/wiki/County_of_East_Frisia]: confirmed (personal union with Prussia from 25 May 1744)

Area: infobox 1800 km2 (1800), Cliopatria 2023 km2, ratio 1.12, acknowledged True. Infobox 1,800 km2 (1800) against K2 2,023 km2.

### mecklenburg: fix

Fixes:
- `/ledger/5 and /ledger/6` (not applied). Wallenstein's occupation names holy-roman-empire, whose dossier ends in 1259. Evidence: holy-roman-empire dossier runs 962-1259; Mecklenburg was granted to Wallenstein by Emperor Ferdinand II (1628-1631). Fix: Counterpart habsburg-monarchy (the Emperor's state) or a Wallenstein entry listed under counterparts_needing_dossiers.
- `/ledger/4` (not applied). Mecklenburg takes the County of Schwerin in 1358 while county-of-schwerin (this batch) lasts to 1368: the two draw the county twice for ten years. Evidence: County of Schwerin page: 'bought by Albrecht II of Mecklenburg in the Treaty of Plüschow (7 December 1368)'; the Mecklenburg-Schwerin page used here says 1358. Fix: Agree one date in both dossiers (or enter 1358-1368 as a contest) and cite both pages in the note.
- `/ledger/1/counterpart` (not applied). Counterpart is the sentence 'page names no previous holder'. Evidence: Schema counterpart is a slug, 'nobody' or a name. Fix: Use 'nobody' and keep the explanation in the note.

Thin (for a gap-filler):
- `/keyframe_review/2..5`: the Lordship of Werle (Güstrow, Parchim, Waren), inherited 1436, is never drawn: the circles stop about 40 km short of Güstrow, so central and southern Mecklenburg are empty 1436-1805 (the notes admit the south is under-drawn) (page to try: https://en.wikipedia.org/wiki/Lordship_of_Werle)
- `/ledger/9`: 1805 end is confidence 1 (cut to meet eu-20's duchy-of-mecklenburg) (page to try: https://en.wikipedia.org/wiki/Duchy_of_Mecklenburg-Schwerin)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Mecklenburg]: confirmed as c2 (recognized as prince of the Empire 1170)
- `/ledger/3` [https://en.wikipedia.org/wiki/Mecklenburg]: confirmed (dukes 8 July 1348)
- `/ledger/4` [https://en.wikipedia.org/wiki/County_of_Schwerin]: conflict: page gives Treaty of Plüschow 7 December 1368 (the dossier's 1358 rests on another page)
- `/ledger/5` [https://en.wikipedia.org/wiki/Mecklenburg-G%C3%BCstrow]: confirmed ('In 1628 he and his brother at Schwerin were stripped of their duchies by order of Emperor Ferdinand II' in favour of Wallenstein)
- `/ledger/6` [https://en.wikipedia.org/wiki/Mecklenburg-G%C3%BCstrow]: confirmed (Wallenstein 'dismissed by the Emperor three years later'; the dukes 'with the support of Swedish troops were restored'; John Albert II '(restored) 1631-1636')

Area: infobox 15500 km2 (1800), Cliopatria 11128 km2, ratio 0.72, acknowledged True. Page: 'about two-thirds of the geographical size' of Mecklenburg-Vorpommern (23,295 km2), about 15,500 km2; K3/K5 11,128 km2; the author notes the south is under-drawn.

### united-belgian-states: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/United_Belgian_States]: confirmed (11 January 1790, eight provinces, not Luxembourg)
- `/ledger/1` [https://en.wikipedia.org/wiki/United_Belgian_States]: confirmed (Namur taken 24 October 1790)
- `/ledger/2` [https://en.wikipedia.org/wiki/United_Belgian_States]: confirmed (West Flanders two days later)
- `/ledger/3` [https://en.wikipedia.org/wiki/United_Belgian_States]: confirmed (surrender of Brussels 2 December 1790)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 26,302 km2 (Belgium minus Liège and Luxembourg provinces).

Tried: All four events on the page; type rebel is right; habsburg-netherlands mirrors the January loss and December regain (the October losses of Namur and West Flanders have no Habsburg gains, within a year of the December gain).

### palatinate-neuburg: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Palatinate-Neuburg]: confirmed (1505 after the Landshut War, Kölner Spruch)
- `/ledger/1` [https://en.wikipedia.org/wiki/Palatinate-Neuburg]: confirmed (Jülich and Berg from 1614, personal union)
- `/ledger/2` [https://en.wikipedia.org/wiki/Palatinate-Neuburg]: confirmed (merged with the Electorate 1685)

Area: infobox 2750 km2 (1600), Cliopatria 3794 km2, ratio 1.38, acknowledged True. Page 'about 2,750 km2'; circle 3,794 km2 resolved, noted in K0.

Tried: All events on the page, the 1685 mirror in electoral-palatinate (matched), the Jülich-Berg personal union kept in duchy-of-julich-berg; could not break.

### landgraviate-of-hesse-marburg: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Landgraviate_of_Hesse-Marburg]: confirmed (1567; Marburg, Gießen, Nidda, Eppstein)
- `/ledger/1` [https://en.wikipedia.org/wiki/Landgraviate_of_Hesse-Marburg]: confirmed as c2 (equal shares to Kassel and Darmstadt; towns not named)
- `/ledger/2` [https://en.wikipedia.org/wiki/Landgraviate_of_Hesse-Marburg]: confirmed (1604; Maurice seized the whole area, settled 1648)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page ('approximately ... Upper Hesse'); resolved 5,564 km2.

Tried: Checked found/dissolve years and the shares against the page and the Kassel and Darmstadt mirrors (1604 gains in both): could not break.

### landgraviate-of-hesse-rheinfels: fail

Fixes:
- `/keyframe_review/0/correction` (not applied, blocking). The 14 km St. Goar circle (about 760 km2 resolved) misses the right-bank Ämter the note itself names (Braubach, Reichenberg, Hohenstein) and is far below 'about an eighth' of old Hesse (about 2,500 km2 on the author's own Hesse shape). Evidence: Hesse-Rheinfels page: 'about an eighth of his father's territories, mainly the former Lower County of Katzenelnbogen ... Braubach, Reichenberg, and Hohenstein' on the right bank. Fix: Union the St. Goar circle with a right-bank circle covering Braubach and Hohenstein (about 7.85E 50.22N, 15 km) and say in the note that the page's eighth is not an area; do the same in Hesse-Kassel's 1583 gain region.

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Landgraviate_of_Hesse-Rheinfels]: confirmed (1567, Lower County of Katzenelnbogen, Rheinfels/St. Goar, Braubach, Reichenberg, Hohenstein)
- `/ledger/1` [https://en.wikipedia.org/wiki/Landgraviate_of_Hesse-Kassel]: confirmed (1583 'died out ... shared between the other three'); c2 honest

Area: infobox None km2 (None), Cliopatria None km2, ratio 0.29, acknowledged False. No area on the page; 'an eighth' of the author's 1479-1566 Hesse (21,749 km2) is about 2,700 km2 against 759 km2 drawn.

### county-of-hanau: fix

Fixes:
- `/identity/predecessors/0/slug` (applied). The 1429 predecessor named holy-roman-empire, whose dossier ends in 1259; the author's own note says the lordship lies inside Cliopatria's Holy Roman Empire Minor States from 1260. Evidence: holy-roman-empire.json ends 1259; holy-roman-empire-minor-states.json runs 1260-1806. Fix: Changed to holy-roman-empire-minor-states (re-validated: 0 errors; the 2 warnings were there before).

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_Hanau]: confirmed (1429 Sigismund made Reinhard II a count)
- `/ledger/2` [https://en.wikipedia.org/wiki/County_of_Hanau]: confirmed (1642 Hanau-Münzenberg line extinct, Lichtenberg heir)
- `/ledger/4` [https://en.wikipedia.org/wiki/County_of_Hanau]: confirmed (Hanau-Lichtenberg to Hesse-Darmstadt 1736)
- `/ledger/5` [https://en.wikipedia.org/wiki/County_of_Hanau]: confirmed (Hanau-Münzenberg to Hesse-Kassel 1736)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 1,517 / 3,288 km2.

Tried: Four events on the page, both 1736 mirrors in Hesse-Kassel and Hesse-Darmstadt (matched). The 1680 French vassalage of the Alsatian half has no vassal_end (ends with the state in 1736; the land passes to Darmstadt still under French sovereignty, which Darmstadt's notes leave open).

### county-of-katzenelnbogen: pass

Thin (for a gap-filler):
- `/keyframe_review/0`: both counties are drawn from 1095 although the page says the county 'grew from the Neckar to the Moselle over nearly four centuries'; acquisition dates of the Upper County and Rheinfels are not on the page (page to try: https://de.wikipedia.org/wiki/Grafschaft_Katzenelnbogen)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_Katzenelnbogen]: confirmed (first mentioned 1095)
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Katzenelnbogen]: confirmed (divided 1260)
- `/ledger/2` [https://en.wikipedia.org/wiki/County_of_Katzenelnbogen]: confirmed (1479 extinction, to Hesse)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 4,046 km2.

### county-of-schaumburg: fail

Fixes:
- `/keyframe_review/0/correction` (not applied, blocking). The 22 km Rinteln circle (about 1,520-1,770 km2) is 2.3-2.6 times the area the page gives, and the note says the page gives none. Evidence: County of Schaumburg page: the county's territory was 'roughly the same as today's Schaumburg district' (Landkreis Schaumburg, about 676 km2). Fix: Redraw as a circle of about 15 km centred between Rinteln, Bückeburg and Stadthagen (about 9.15E 52.27N), in the keyframe, both ledger regions and the successors' land; landgraviate-of-hesse-kassel's Schaumburg share should use a part of it.
- `/identity/successors and Hesse-Kassel L5` (not applied). The page dates the three-way partition to 1640 and makes Schaumburg-Lippe the largest share, while Hesse-Kassel gains 'most of the County' in 1648 from this dossier, which no longer exists then. Evidence: County of Schaumburg page: partition 1640, 'the largest part became Schaumburg-Lippe', the eastern Hessian portion in personal union with Hesse-Kassel; Hesse-Kassel page: 'most of the County of Schaumburg' at Westphalia. Fix: Say in both notes that the pages disagree; date the Hessian share 1640 (or 1647/48 with a page) and draw the three shares as parts of the corrected circle.

Thin (for a gap-filler):
- `/ledger/0`: the 1110 start is confidence 1 (the page's 1110 is the Holstein enfeoffment; the lordship dates to about 1106) (page to try: https://en.wikipedia.org/wiki/Adolf_I,_Count_of_Schauenburg_and_Holstein)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_Schaumburg]: confirmed as c1 (infobox 1110; lordship about 1106)
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Schaumburg]: confirmed as c2 (Reformation under Otto IV in 1559; no rename on the page)
- `/ledger/2` [https://en.wikipedia.org/wiki/County_of_Schaumburg]: confirmed (1640 extinction and partition)

Area: infobox 676 km2 (1640), Cliopatria 1770 km2, ratio 2.6, acknowledged False. Page: 'roughly the same as today's Schaumburg district' (about 676 km2); the circle resolves to 1,770 km2.

### swabian-circle: fail

Fixes:
- `/identity/type` (not applied, blocking). A dossier of type umbrella: an Imperial Circle is an association of estates, not territory, and the reviewer standard says an umbrella is never a dossier of its own. Evidence: Reviewer brief rule 9 ('umbrella is never a dossier of its own'); research brief rule 4 ('associations are never territory'); the dossier's K0 lays Baden-Württemberg, Augsburg and Franconia over the member states drawn by their own dossiers (Württemberg, Baden, Augsburg, Constance, Ulm, Oettingen, Hohenzollern-Hechingen). Fix: Orchestrator decision: drop the file (the scope line in the group brief asked for the circle, so the author is not at fault), or keep it only if the compiler skips umbrella dossiers; if kept, its found/dissolve counterpart holy-roman-empire (dossier ends 1259) needs a post-1259 umbrella slug.

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Swabian_Circle]: confirmed ('established in 1500 on the territory of the former German stem-duchy of Swabia'); the page treats it as an imperial circle of 88 territories, not a state
- `/ledger/1` [https://en.wikipedia.org/wiki/Swabian_Circle]: confirmed (directorship to Baden after the 1803 Reichsdeputationshauptschluss)
- `/ledger/2` [https://en.wikipedia.org/wiki/Swabian_Circle]: confirmed for 1806 (infobox 'Dissolution of the Holy Roman Empire: 1806'; it also gives 'Disestablished: 1808')
- `/keyframe_review/0/correction` [https://en.wikipedia.org/wiki/Swabian_Circle]: the region includes region:Franconia, the neighbouring circle's land

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. Not checked: umbrella, not drawn as territory.

### franconian-circle: fail

Fixes:
- `/identity/type` (not applied, blocking). A dossier of type umbrella: an Imperial Circle is an association of estates, never a dossier of its own. Evidence: Reviewer brief rule 9; research brief rule 4; K0 (region Franconia) overlays Bamberg, Würzburg, Eichstätt, Ansbach, Bayreuth, Nuremberg and Henneberg, each drawn by its own dossier in this batch. Fix: Orchestrator decision: drop the file or keep it only as a non-drawn record; holy-roman-empire (ends 1259) cannot be its 1500/1806 counterpart.

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Franconian_Circle]: confirmed ('On 2 July 1500, at the Reichstag of Augsburg')
- `/ledger/1` [https://en.wikipedia.org/wiki/Franconian_Circle]: confirmed (infobox 'Disestablished: 1806'); the page presents it as a grouping of states

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. Not checked: umbrella.

### further-austria: fix

Fixes:
- `/ledger/7/counterpart` (applied). The 1805 dissolve gave the Breisgau to grand-duchy-of-baden, a row that starts in 1806; Baden was the Electorate of Baden (row 1803-1805) at Pressburg. Evidence: Further Austria page: after Pressburg 1805 'Breisgau went to Baden'; polities.csv: electorate-of-baden 1803-1805, grand-duchy-of-baden 1806-1870. Fix: counterpart 'electorate-of-baden'.
- `/identity/capitals` (not applied). Ensisheim is the capital to 1805, but it lay in the Sundgau, French from 1648; the infobox also lists Freiburg im Breisgau. Evidence: Further Austria page: residence at Ensisheim; 'the Sundgau became part of France' at Westphalia; infobox lists Freiburg as a capital. Fix: End Ensisheim in 1648 and add Freiburg from 1648 (or the year a page gives) with a capital_move event.

Thin (for a gap-filler):
- `/keyframe_review`: Burgau, Hohenberg, Nellenburg and Vorarlberg, which the page lists as parts of Further Austria, are never drawn (acknowledged in notes: undated on the page); the Breisgau is confidence 1 (1368) and its 1803 return confidence 1 (page to try: https://en.wikipedia.org/wiki/Margraviate_of_Burgau)
- `/ledger/1`: confidence-1 gain in 1368: After 1368 (page gives no exact year): Freiburg im Breisgau. It 'became part of the holdings after 1368'. The seller is not named on the page. (page to try: https://en.wikipedia.org/wiki/Further_Austria)
- `/ledger/6`: confidence-1 gain in 1803: 1803 (page silent): the Breisgau returns to the Habsburg side. The page says only that Ercole III died 'two years later' than 1801 and does not say who held the (page to try: https://en.wikipedia.org/wiki/Further_Austria)

Spot checks:
- `/ledger/2` [https://en.wikipedia.org/wiki/Further_Austria]: confirmed (Sundgau to France at Westphalia)
- `/ledger/3` [https://en.wikipedia.org/wiki/Further_Austria]: confirmed (Tettnang 1780)
- `/ledger/4` [https://en.wikipedia.org/wiki/Further_Austria]: confirmed (Fricktal Habsburg until 1797)
- `/ledger/5` [https://en.wikipedia.org/wiki/Further_Austria]: confirmed (Lunéville 1801 Breisgau to Ercole III)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 759-6,070 km2, which leaves out Vorarlberg and Swabian Austria (acknowledged).

### prince-bishopric-of-augsburg: fix

Fixes:
- `/keyframe_review/0` (not applied). K0 draws Dillingen and Füssen from 888, but the ledger gains them in 1248 and 1309; the gains move most of the shape and leave no trace in the keyframes. Evidence: Prince-Bishopric of Augsburg page: Bishop Hartmann (1248-1286) left the church 'the town and castle of Dillingen'; Frederick I (1309-1331) 'acquired ... Füssen'. Fix: Split K0 at 1248 and 1309 (888-1247: the bishops' core round Augsburg, then with Dillingen, then with Füssen), or move the gains to 888 with a note.
- `/ledger/4 and /ledger/5` (not applied). The Swedish occupation names kingdom-of-sweden while the sibling dossiers (Würzburg, Bamberg, Pomerania) name swedish-empire for the same years. Evidence: polities.csv has both rows; swedish-empire (1612-1814) is the one the batch uses elsewhere. Fix: Use swedish-empire.

Thin (for a gap-filler):
- `/ledger/1`: Dillingen and Füssen gains are confidence 1 (undated on the page) (page to try: https://en.wikipedia.org/wiki/Dillingen_an_der_Donau)
- `/ledger/2`: confidence-1 gain in 1309: From 1309 (page gives only the episcopate 1309-1331): Füssen. Frederick I 'acquired for his see the castle and stronghold of Füssen.' Entered at the start of hi (page to try: https://en.wikipedia.org/wiki/Prince-Bishopric_of_Augsburg)

Spot checks:
- `/ledger/3` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Augsburg]: confirmed (withdrew to Dillingen after the 1537 decree)
- `/ledger/4` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Augsburg]: confirmed (occupied by Sweden 1632-1635)
- `/ledger/6` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Augsburg]: confirmed (25 February 1803; possession 1 December 1802)
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Augsburg]: confirmed (immediacy c. 888)

Area: infobox 2365 km2 (1802), Cliopatria 2529 km2, ratio 1.07, acknowledged True. Text 2,365 km2 at annexation; K0 2,529 km2.

### prince-bishopric-of-constance: pass

Thin (for a gap-filler):
- `/keyframe_review/0`: one stand-in circle 1155-1803; the scattered lands (Reichenau 1540, Öhningen) are not traced (page to try: https://de.wikipedia.org/wiki/Hochstift_Konstanz)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Constance]: confirmed (1155 Barbarossa's deed)
- `/ledger/1` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Constance]: confirmed (Meersburg 1527)
- `/ledger/2` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Constance]: confirmed (1803 to Baden)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; stand-in 1,517 km2.

### prince-bishopric-of-strasbourg: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Strasbourg]: confirmed (imperial immediacy 982)
- `/ledger/1` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Strasbourg]: confirmed (left bank annexed by France 1681)
- `/ledger/2` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Strasbourg]: confirmed (Oberkirch, Ettenheim, Oppenau to Baden 1803)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 4,299 / 1,770 km2.

Tried: Three events on the page; the 1681 mirror in kingdom-of-france names holy-roman-empire (France's dossier). Capital Strasbourg lay in a free imperial city from 1262 (no dossier overlaps it).

### prince-bishopric-of-eichstatt: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Eichst%C3%A4tt]: confirmed (1305 Hirschberg inheritance)
- `/ledger/1` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Eichst%C3%A4tt]: confirmed (1802 mediatised under Salzburg; 1803 to Ferdinand)

Area: infobox 1100 km2 (1802), Cliopatria 1517 km2, ratio 1.38, acknowledged True. Page about 1,100 km2; 19 km circle resolves to 1,517 km2.

### prince-bishopric-of-halberstadt: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Bishopric_of_Halberstadt]: confirmed (state from 1180)
- `/ledger/1` [https://en.wikipedia.org/wiki/Bishopric_of_Halberstadt]: confirmed (Aschersleben 1315; Anhalt implied by the link)
- `/ledger/2` [https://en.wikipedia.org/wiki/Bishopric_of_Halberstadt]: confirmed (1648 Principality of Halberstadt to Brandenburg-Prussia)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 2,023-2,529 km2.

Tried: All three events on the page; the 1315 mirror in principality-of-anhalt (matched); brandenburg-prussia's 1648 gain names holy-roman-empire-minor-states (that dossier's counterpart).

### prince-abbey-of-fulda: pass

Thin (for a gap-filler):
- `/keyframe_review/0`: one 25 km stand-in circle 1221-1802 (page to try: https://de.wikipedia.org/wiki/Hochstift_Fulda)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Fulda_Abbey]: confirmed (1221 imperial estate)
- `/ledger/1` [https://en.wikipedia.org/wiki/Fulda_Abbey]: confirmed (from 1752 Prince-Bishopric)
- `/ledger/2` [https://en.wikipedia.org/wiki/Fulda_Abbey]: confirmed as c2 (dissolved 1802; joined Orange-Nassau, undated)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; stand-in 2,276 km2.

### prince-bishopric-of-trent: fix

Fixes:
- `/ledger/1/counterpart, /ledger/2/counterpart, /identity/successors/0/slug` (applied). The 1511 vassalage and the 1803 annexation name house-of-habsburg, whose dossier ends in 1515. Evidence: Prince-Bishopric of Trent page: June 1511 'perpetual confederate' among 'Austrian possessions'; 1803 secularized, 'later part of the County of Tyrol', an Austrian crown land; house-of-habsburg runs 1260-1515, habsburg-monarchy 1487-1805. Fix: Counterparts and successor set to habsburg-monarchy.

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Trent]: confirmed (1027 from the Veronese march)
- `/ledger/1` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Trent]: confirmed as c2 (June 1511 perpetual confederate)
- `/ledger/2` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Trent]: confirmed (1803 secularized)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. Page: roughly present-day Trentino (6,207 km2); resolved 5,311 km2.

### prince-bishopric-of-brixen: fix

Fixes:
- `/ledger/4/counterpart, /ledger/5/counterpart, /identity/successors/0/slug` (applied). The 1511 vassalage and the 1803 annexation name house-of-habsburg (dossier ends 1515). Evidence: Prince-Bishopric of Brixen page: 'In 1803 the principality was secularized, and annexed to Austria'; Trent page: 1511 confederation with the Austrian possessions. Fix: Counterparts and successor set to habsburg-monarchy.
- `/keyframe_review/1` (not applied). K1 keeps the Puster valley circle to 1802 although L2 loses Inntal and Puster lands to Andechs-Meran in 1165 (the note admits the circles do not subtract it). Evidence: Brixen page: lost 'in 1165 territory in the Inntal and the Puster Valley to the Counts of Andechs-Meran'. Fix: Split K1 at 1165 and shrink the Puster circle, or turn L2 into a vassal grant with a note; county-of-tyrol's K1 should also stop overlapping the Brixen circles.

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Brixen]: confirmed (1027 Norital)
- `/ledger/1` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Brixen]: confirmed (1091 Puster Valley from Henry IV)
- `/ledger/2` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Brixen]: confirmed (1165 to Andechs-Meran)
- `/ledger/3` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Brixen]: confirmed (1179 prince of the Empire)
- `/ledger/5` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Brixen]: confirmed (1803 annexed to Austria)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 1,264-2,529 km2.

### prince-bishopric-of-passau: pass

Thin (for a gap-filler):
- `/ledger/1`: the 1803 share north of the Danube and Ilz to the Electorate of Salzburg is not entered (the dissolve gives all to Bavaria; the successors list names Salzburg) (page to try: https://en.wikipedia.org/wiki/Prince-Bishopric_of_Passau)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Passau]: confirmed (recognised as prince at Nuremberg, January 1217)
- `/ledger/1` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Passau]: confirmed (1803; city and right-bank lands to Bavaria)

Area: infobox 5442 km2 (2020), Cliopatria 1012 km2, ratio 0.19, acknowledged True. The 5,442 km2 on the page is the modern diocese, not the principality; not comparable.

### prince-bishopric-of-speyer: fix

Fixes:
- `/ledger/10/counterpart` (applied). The 1801 left-bank loss names french-first-republic, a row that ends in 1795; France in 1801 is the French Consulate. Evidence: Speyer page: 'French troops conquered the left-bank territories in 1801/1802'; polities.csv french-first-republic 1792-1795, french-consulate 1800-1804. Fix: counterpart 'french-consulate'.
- `/ledger (1676)` (not applied). The 1676 Imperial recapture of Philippsburg is missing between the 1648 loss and the 1679 return. Evidence: Speyer page: 'Imperial troops recaptured the fortress' in 1676; 1679 'officially returned to the Bishop and the Empire'. Fix: Add a 1676 occupation of Philippsburg by the Imperial side (or say in L4's note that the return was de facto from 1676).

Spot checks:
- `/ledger/1` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Speyer]: confirmed (French captured Philippsburg 1644)
- `/ledger/2` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Speyer]: confirmed (France 'gained the fortress in the 1648 Peace of Westphalia')
- `/ledger/4` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Speyer]: confirmed (Nijmegen 1679 returned)
- `/ledger/5` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Speyer]: confirmed as c2 (1681 Reunion annexation)
- `/ledger/7` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Speyer]: confirmed (returned 1697)
- `/ledger/9` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Speyer]: confirmed (Bruchsal 1723)

Area: infobox 1540 km2 (1789), Cliopatria 1770 km2, ratio 1.15, acknowledged True. Page about 1,540 km2; K0/K2 1,770 km2.

### prince-bishopric-of-verden: fix

Fixes:
- `/ledger/2/counterpart` (not applied). The 1648 dissolve names kingdom-of-sweden while the batch uses swedish-empire for Sweden in these years (Pomerania 1630-1637, Würzburg, Bamberg). Evidence: polities.csv: swedish-empire 1612-1814 and kingdom-of-sweden 980-2024 are both rows; one Sweden per year is needed for the mirrors. Fix: Use swedish-empire (and in identity.successors), unless the orchestrator maps both.

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Verden]: confirmed (1180)
- `/ledger/1` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Verden]: confirmed (Rotenburg residence since 1195)
- `/ledger/2` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Verden]: confirmed (15 May 1648)

Area: infobox 730 km2 (1806), Cliopatria 1012 km2, ratio 1.39, acknowledged True. Infobox 730 km2 (1806); circle 1,012 km2 resolved.

### prince-bishopric-of-minden: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Minden]: confirmed (1180)
- `/ledger/1` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Minden]: confirmed as c2 (possessed Hamelin 1259-77)
- `/ledger/2` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Minden]: confirmed as c2
- `/ledger/3` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Minden]: confirmed (1648 to Brandenburg)

Area: infobox 1100 km2 (1789), Cliopatria 1770 km2, ratio 1.61, acknowledged True. Page 1,100 km2 (1789) in the K0 note; 19 km circle resolves to 1,770 km2.

### county-of-nassau: thin

Thin (for a gap-filler):
- `/keyframe_review/0`: two stand-in circles for 1159-1805 covering all Nassau lines; the 1803 gains of Nassau-Usingen and Nassau-Weilburg (the Rheingau and other Mainz, Cologne and Trier lands) and the Orange-Nassau lands' passage to Nassau-Orange-Fulda (1803) and into the duchy (October 1806) are not entered (page to try: https://en.wikipedia.org/wiki/Nassau-Usingen)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_Nassau]: confirmed (title acknowledged by the Bishop of Worms 1159)
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Nassau]: confirmed (Prima divisio 17 December 1255)
- `/ledger/2` [https://en.wikipedia.org/wiki/County_of_Nassau]: confirmed (Usingen and Weilburg form the duchy 1806)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; stand-in 4,299 km2.

### principality-of-anhalt: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Principality_of_Anhalt]: confirmed (split off Saxony 1212)
- `/ledger/1` [https://en.wikipedia.org/wiki/Principality_of_Anhalt]: confirmed (prince 1218)
- `/ledger/3` [https://en.wikipedia.org/wiki/Principality_of_Anhalt]: confirmed (1315 Aschersleben to Halberstadt)
- `/ledger/4` [https://en.wikipedia.org/wiki/Principality_of_Anhalt]: confirmed (reunited 1570; split 1603)
- `/ledger/6` [https://en.wikipedia.org/wiki/Principality_of_Anhalt]: confirmed (duchies 1806)

Area: infobox 2300 km2 (1806), Cliopatria 2276 km2, ratio 0.99, acknowledged True. Page 2,300 km2 for the later duchy; K1 2,276 km2.

### county-of-lippe: pass

Thin (for a gap-filler):
- `/ledger/2`: Schwalenberg is confidence 1 at 1332; the page gives 'between 1332 and 1358' (c2 possible) (page to try: https://en.wikipedia.org/wiki/County_of_Lippe)
- `/ledger/7`: the 1806 end is confidence 1 (the page makes it a principality in 1789, already entered) (page to try: https://en.wikipedia.org/wiki/Principality_of_Lippe)

Spot checks:
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Lippe]: confirmed (Rheda 1190)
- `/ledger/3` [https://en.wikipedia.org/wiki/County_of_Lippe]: confirmed (1401 Rheda to Tecklenburg)
- `/ledger/4` [https://en.wikipedia.org/wiki/County_of_Lippe]: confirmed (rest of Sternberg 1405)
- `/ledger/6` [https://en.wikipedia.org/wiki/County_of_Lippe]: confirmed (Principality 1789)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 1,770-2,276 km2.

### duchy-of-berg: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Duchy_of_Berg]: confirmed (1101 junior Ezzonen line)
- `/ledger/1` [https://en.wikipedia.org/wiki/Duchy_of_Berg]: confirmed (1160 split, one part later the Mark)
- `/ledger/2` [https://en.wikipedia.org/wiki/Duchy_of_Berg]: confirmed (1280 court moved to Düsseldorf)
- `/ledger/3` [https://en.wikipedia.org/wiki/Duchy_of_Berg]: confirmed (dukes 1380)
- `/ledger/4` [https://en.wikipedia.org/wiki/Duchy_of_Berg]: confirmed (union with Jülich after 1423; the page's text also says 1348, a conflict on the page)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 3,035 km2 after 1160.

Tried: All five events on the page; the 1160 mirror in county-of-mark and the 1423 mirror in duchy-of-julich-berg (matched). The Berg-Ravensberg personal union (1346/1348) is not drawn by either dossier, consistently.

### county-of-mark: pass

Thin (for a gap-filler):
- `/ledger/1`: seat move is confidence 1; the page says Burg Mark near Hamm 'in the 1220s' (c2 possible) (page to try: https://en.wikipedia.org/wiki/County_of_Mark)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_Mark]: confirmed (Berg-Altena 1160)
- `/ledger/2` [https://en.wikipedia.org/wiki/County_of_Mark]: confirmed (Adolph III inherited Mark 1391; united 1394)
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Mark]: not checked: a confidence-1 capital move with no land; listed under thin

Area: infobox 3000 km2 (1391), Cliopatria 3794 km2, ratio 1.26, acknowledged True. Page about 3,000 km2; 31 km circle resolves to 3,794 km2.

### county-of-ravensberg: pass

Thin (for a gap-filler):
- `/ledger/1`: Bielefeld seat is confidence 1 (page: c. 1240-50) (page to try: https://en.wikipedia.org/wiki/Sparrenburg)
- `/ledger/2`: the page has Ravensberg 'inherited by the Duchy of Berg in 1346' (personal union 1348-1395) before Jülich-Berg in 1437; the dossier keeps it independent to 1437 without saying so (page to try: https://en.wikipedia.org/wiki/County_of_Ravensberg)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_Ravensberg]: confirmed (Otto I 1140)
- `/ledger/2` [https://en.wikipedia.org/wiki/County_of_Ravensberg]: confirmed as c2 (with Jülich-Berg from 1437)
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Ravensberg]: not checked: a confidence-1 capital move with no land; listed under thin

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 1,770 km2.

### burgraviate-of-nuremberg: thin

Fixes:
- `/identity/end` (not applied, to be done in free-imperial-city-of-nuremberg). The dossier ends in 1398, but the page has the burgraviate held until it was 'sold to city' in 1427, and free-imperial-city-of-nuremberg gains from this dossier in 1427. Evidence: Burgraviate of Nuremberg page: 1427 'sold to city, exc. Blutgericht'; Frederick VI burgrave until 1427. Fix: Keep the 1398 end (the lands went to Ansbach and Kulmbach) but tell the city dossier to name principality-of-ansbach (Frederick VI) as the 1427 seller, or end this dossier in 1427 with only the castle district.

Thin (for a gap-filler):
- `/keyframe_review/0`: the Ansbach and Bayreuth circles are drawn from 1105, but the burgraves acquired Bayreuth (1248), Ansbach (1331) and Kulmbach (1340) much later; the page gives none of these dates (page to try: https://de.wikipedia.org/wiki/Burggrafschaft_N%C3%BCrnberg)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Burgraviate_of_Nuremberg]: confirmed (1105 granted to the House of Raabs)
- `/ledger/1` [https://en.wikipedia.org/wiki/Burgraviate_of_Nuremberg]: confirmed (Frederick I of Hohenzollern 1192; infobox 1191)
- `/ledger/2` [https://en.wikipedia.org/wiki/Burgraviate_of_Nuremberg]: confirmed (princely status 1363)
- `/ledger/4` [https://en.wikipedia.org/wiki/Burgraviate_of_Nuremberg]: confirmed (1398 Frederick VI Ansbach, John III Kulmbach)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 6,575 km2 (the two principalities' circles).

### free-imperial-city-of-nuremberg: fix

Fixes:
- `/ledger/1/counterpart` (not applied). The 1427 seller is burgraviate-of-nuremberg, whose dossier ends in 1398. Evidence: Imperial City of Nuremberg page: the city bought the castle ruins and forest in 1427, seller not named; burgraviate-of-nuremberg ends 1398 (its lands passed to Ansbach and Kulmbach). Fix: Counterpart principality-of-ansbach (Frederick VI) with a page, or 'nobody' with a note; keep c3 for the year.
- `/ledger/2/counterpart` (not applied). The New District (1504) is from 'unnamed (page silent)', but the page says it was land gained in the Landshut War while siding with Albert IV, i.e. from Bavaria-Landshut. Evidence: Imperial City of Nuremberg page: the New District 'is made up of the territory gained by Nuremberg in the Landshut War of Succession'. Fix: Counterpart duchy-of-bavaria (Bavaria-Landshut is inside that dossier), so Bavaria can carry the loss.

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Imperial_City_of_Nuremberg]: confirmed (1219 Great Letter of Freedom)
- `/ledger/1` [https://en.wikipedia.org/wiki/Imperial_City_of_Nuremberg]: confirmed (1427 castle ruins and forest bought)
- `/ledger/2` [https://en.wikipedia.org/wiki/Imperial_City_of_Nuremberg]: confirmed as c2 (New District from the Landshut War)
- `/ledger/3` [https://en.wikipedia.org/wiki/Imperial_City_of_Nuremberg]: confirmed (handed to Bavaria from 8 September 1806)

Area: infobox 1200 km2 (1600), Cliopatria 1264 km2, ratio 1.05, acknowledged True. Page some 1,200 km2; K2 1,264 km2.

### free-imperial-city-of-ulm: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Free_Imperial_City_of_Ulm]: confirmed as c2 (infobox Reichsfreiheit 1181; text 1155)
- `/ledger/1` [https://en.wikipedia.org/wiki/Free_Imperial_City_of_Ulm]: confirmed (1802 to Bavaria; infobox 1803)

Area: infobox 780 km2 (1800), Cliopatria 1012 km2, ratio 1.3, acknowledged True. Page about 780 km2; 15.8 km circle resolves to 1,012 km2.

Tried: Both events on the page; duchy-of-bavaria has no 1802/1803 gain from Ulm (Bavaria's gap).

### free-imperial-city-of-cologne: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Free_Imperial_City_of_Cologne]: confirmed (Worringen 1288)
- `/ledger/1` [https://en.wikipedia.org/wiki/Free_Imperial_City_of_Cologne]: confirmed (formally free imperial city 1475)
- `/ledger/2` [https://en.wikipedia.org/wiki/Free_Imperial_City_of_Cologne]: confirmed (occupied 1794; month not on the page)
- `/ledger/4` [https://en.wikipedia.org/wiki/Free_Imperial_City_of_Cologne]: confirmed (annexed by France 28 May 1796)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. City only; resolved 506 km2 (12 km circle).

Tried: All events on the page and the 1288 mirror in electorate-of-cologne (matched). The 1796 counterpart french-first-republic is a Cliopatria row that ends 1795 (french-directory 1796-1799): an orchestrator naming question shared by several dossiers.

### county-of-henneberg: fail

Fixes:
- `/ledger/6` (not applied, blocking). Schmalkalden is lost to landgraviate-of-hesse in 1360 at confidence 3, but the page it quotes says it 'fell to Landgrave William IV of Hesse-Kassel' under a 1360 inheritance treaty: the treaty is 1360, the transfer came with the extinction of 1583 (William IV ruled 1567-1592). Mis-dated at confidence 3. Evidence: County of Henneberg page: 'The Lordship of Schmalkalden fell to Landgrave William IV of Hesse-Kassel' under a 1360 inheritance treaty; landgraviate-of-hesse records no 1360 gain. Fix: Move the loss to 1583 with counterpart landgraviate-of-hesse-kassel (and give it in the dissolve, not to Saxony), or, if a page dates a 1360 half-share purchase, cite it and draw the half only; split K3 accordingly.
- `/ledger/7/region` (not applied). The 1583 dissolve hands the Schmalkalden circle to electorate-of-saxony although K3 removed it in 1360 and the page gives it to Hesse-Kassel. Evidence: County of Henneberg page: 'Most of the territory was inherited by the Saxon House of Wettin' ... 'Schmalkalden went to Hesse-Kassel'. Fix: Drop the Schmalkalden circle from the Saxon dissolve; add the Hesse-Kassel share.

Thin (for a gap-filler):
- `/ledger/0`: 1037 start is confidence 1 (infobox 'c. 1037') (page to try: https://de.wikipedia.org/wiki/Henneberger)

Spot checks:
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Henneberg]: confirmed (Schmalkalden from Henry III of Meissen 1247)
- `/ledger/2` [https://en.wikipedia.org/wiki/County_of_Henneberg]: confirmed (Coburg after the Andechs line ended 1248)
- `/ledger/5` [https://en.wikipedia.org/wiki/County_of_Henneberg]: confirmed (Coburg to the Wettins through the 1347 marriage)
- `/ledger/6` [https://en.wikipedia.org/wiki/County_of_Henneberg]: mis-dated (the page's 1360 is the treaty; the land fell to Hesse-Kassel under William IV)
- `/ledger/4` [https://en.wikipedia.org/wiki/County_of_Henneberg]: confirmed (princely status 1310)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 2,276-2,782 km2.

### county-of-waldeck: fix

Fixes:
- `/ledger/2` (not applied). The 1431 Hessian overlordship runs to 1806 with landgraviate-of-hesse as suzerain, but that dossier ends in 1567. Evidence: County of Waldeck page: the two lines came under Hesse's sovereignty in 1431 and 1438, revoked only in 1847 (in practice from 1807); landgraviate-of-hesse 1264-1567. Fix: Add a 1567 vassal_end (landgraviate-of-hesse) and vassal_start (landgraviate-of-hesse-kassel), the Kassel line holding the fief; say in the note that it outlasts the dossier.

Thin (for a gap-filler):
- `/ledger/6`: 1806 end is confidence 1 (the page dates the Rhine Confederation entry 1807) (page to try: https://en.wikipedia.org/wiki/Principality_of_Waldeck_and_Pyrmont)

Spot checks:
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Waldeck]: confirmed (imperial immediacy 1349)
- `/ledger/2` [https://en.wikipedia.org/wiki/County_of_Waldeck]: confirmed (Hessian sovereignty 1431/1438)
- `/ledger/3` [https://en.wikipedia.org/wiki/County_of_Waldeck]: confirmed (Pyrmont 1626)
- `/ledger/4` [https://en.wikipedia.org/wiki/County_of_Waldeck]: confirmed (Arolsen 1655)
- `/ledger/5` [https://en.wikipedia.org/wiki/County_of_Waldeck]: confirmed (6 January 1712 prince)

Area: infobox 1121 km2 (1905), Cliopatria 1517 km2, ratio 1.35, acknowledged True. Page 1,121 km2 (1905, Waldeck-Pyrmont); K1 1,517 km2.

### county-of-mansfeld: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_Mansfeld]: confirmed (counts appointed after the 1069 revolt)
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Mansfeld]: confirmed (Heldrungen purchased 1479)
- `/ledger/2` [https://en.wikipedia.org/wiki/County_of_Mansfeld]: confirmed (Allstedt acquired 1526)
- `/ledger/3` [https://en.wikipedia.org/wiki/County_of_Mansfeld]: confirmed as c2 (assets confiscated 1579, mediatised by Saxony by 1580)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 1,770-2,023 km2.

Tried: All four events on the page; electorate-of-saxony has no 1580 gain from Mansfeld (that dossier's gap; Magdeburg's share also unrecorded).

### county-of-hoya: pass

Thin (for a gap-filler):
- `/ledger/3`: the 1582 remainder to Lüneburg and Hesse-Kassel is not entered (the dissolve gives all to Brunswick-Lüneburg) (page to try: https://en.wikipedia.org/wiki/County_of_Hoya)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_Hoya]: confirmed (1202 vassal of Hartwig II)
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Hoya]: confirmed (Nienburg 1215)
- `/ledger/2` [https://en.wikipedia.org/wiki/County_of_Hoya]: confirmed (1345 division)
- `/ledger/3` [https://en.wikipedia.org/wiki/County_of_Hoya]: confirmed (1582, majority to Calenberg)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 2,276 km2.

### county-of-diepholz: fix

Fixes:
- `/ledger/6 and /ledger/7` (not applied). The 1585 end of the Auburg fief and the loss of Auburg name landgraviate-of-hesse, which ends in 1567; in 1585 the claimant was Hesse-Kassel. Evidence: County of Diepholz page: 'Auburg and its surroundings went to the Landgraviate of Hesse' (branch not named); landgraviate-of-hesse 1264-1567. Fix: Add a 1567 vassal_end/vassal_start pair moving the Auburg fief to landgraviate-of-hesse-kassel and make L6/L7 name it; Hesse-Kassel then needs the 1585 gain.

Thin (for a gap-filler):
- `/ledger/0`: 1070 start is confidence 1 (the page has earlier grants c. 890 and the name from 1160) (page to try: https://en.wikipedia.org/wiki/County_of_Diepholz)
- `/ledger/4`: Auburg fief is confidence 1 with a 6 km stand-in (the page does not locate Auburg) (page to try: https://de.wikipedia.org/wiki/Auburg)

Spot checks:
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Diepholz]: confirmed (1285 Blankena patrimony)
- `/ledger/2` [https://en.wikipedia.org/wiki/County_of_Diepholz]: confirmed (1291 Vicecomitat of Sudholte)
- `/ledger/3` [https://en.wikipedia.org/wiki/County_of_Diepholz]: confirmed (1510 Brunswick-Lüneburg as liege lord)
- `/ledger/8` [https://en.wikipedia.org/wiki/County_of_Diepholz]: confirmed (1585, most of the county to Brunswick-Lüneburg)

Area: infobox 810 km2 (1585), Cliopatria 1012 km2, ratio 1.25, acknowledged True. Page gives 47 km by 22 km (about 810 km2 as an ellipse); resolved 1,012 km2.

### prince-bishopric-of-freising: fix

Fixes:
- `/ledger/0/counterpart and /identity/predecessors/0/slug` (applied). The 1294 found event and the predecessor named holy-roman-empire, whose dossier ends in 1259. Evidence: holy-roman-empire.json ends 1259; holy-roman-empire-minor-states.json runs 1260-1806. Fix: Changed to holy-roman-empire-minor-states (re-validated: 0 errors, 0 warnings).

Thin (for a gap-filler):
- `/keyframe_review/0`: Werdenfels ('late 13th century') and the Innichen holding's 1803 fate are not dated on the page (page to try: https://en.wikipedia.org/wiki/County_of_Werdenfels)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Freising]: confirmed (prince-bishop and imperial immediacy 1294)
- `/ledger/1` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Freising]: confirmed (Styrian and Slovenian enclaves taken by Austria 1802-03)
- `/ledger/2` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Freising]: confirmed (Bavarian troops entered November 1802)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page (15,000 subjects in 1800); resolved 2,276 km2 of scattered circles.

### prince-bishopric-of-worms: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Worms]: confirmed as c2 (Reichsfreiheit 861)
- `/ledger/1` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Worms]: confirmed (Ladenburg from 1400)
- `/ledger/2` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Worms]: confirmed (left bank occupied and annexed 1795)
- `/ledger/3` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_Worms]: confirmed (secularised to Hesse-Darmstadt 1802)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 759 / 253 km2.

Tried: All four events on the page; landgraviate-of-hesse-darmstadt has no gain from Worms (recorded as a fix there).

### prince-bishopric-of-lubeck: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_L%C3%BCbeck]: confirmed (imperial state 1180)
- `/ledger/1` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_L%C3%BCbeck]: confirmed (Eutin residence 1309)
- `/ledger/2` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_L%C3%BCbeck]: confirmed (Holstein-Gottorp administrators since 1586)
- `/ledger/3` [https://en.wikipedia.org/wiki/Prince-Bishopric_of_L%C3%BCbeck]: confirmed (1803 to Oldenburg)

Area: infobox 541 km2 (1803), Cliopatria 759 km2, ratio 1.4, acknowledged True. Page 541 km2; 13.1 km circle resolves to 759 km2.

Tried: All four events on the page; county-of-oldenburg's 1803 gain mirrors the dissolve (matched).

### county-of-schwerin: pass

Fixes:
- `/ledger/1` (not applied, to be done in mecklenburg). The 1368 end conflicts with mecklenburg's 1358 gain of the county (both in this batch): ten years drawn twice. Evidence: County of Schwerin page: 'bought by Albrecht II of Mecklenburg in the Treaty of Plüschow (7 December 1368)'; mecklenburg L4 1358 from the Mecklenburg-Schwerin page. Fix: Keep 1368 here (page-supported) and settle the pair in mecklenburg (see that dossier).

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_Schwerin]: confirmed (created 1161 after Henry the Lion's conquest)
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Schwerin]: confirmed (Treaty of Plüschow 7 December 1368)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 2,023 km2.

### principality-of-rugen: pass

Thin (for a gap-filler):
- `/ledger/4`: terra Wolgast loss is confidence 1 ('before 1250'); duchy-of-pomerania has no mirror gain (page to try: https://en.wikipedia.org/wiki/Wolgast)

Spot checks:
- `/ledger/1` [https://en.wikipedia.org/wiki/Principality_of_R%C3%BCgen]: confirmed (Arkona 1168, Danish vassals)
- `/ledger/3` [https://en.wikipedia.org/wiki/Principality_of_R%C3%BCgen]: confirmed (half of terra Wolgast 1235)
- `/ledger/5` [https://en.wikipedia.org/wiki/Principality_of_R%C3%BCgen]: confirmed (Schlawe fief 1270)
- `/ledger/7` [https://en.wikipedia.org/wiki/Principality_of_R%C3%BCgen]: confirmed (sold to Brandenburg by 1277)
- `/ledger/9` [https://en.wikipedia.org/wiki/Principality_of_R%C3%BCgen]: confirmed (Wizlaw III died 1325, to the Griffins)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 1,770-2,782 km2 (Rügen island is 926 km2 plus mainland).

### duchy-of-saxe-lauenburg: pass

Thin (for a gap-filler):
- `/ledger/5`: the 1803 end is confidence 1: the page has a French occupation 1803-1805 inside a personal union with Hanover (1705-1803), not a dissolution; electorate-of-hanover gains the duchy in 1705, so the two draw it twice 1705-1803 unless one treats it as personal union (page to try: https://en.wikipedia.org/wiki/Saxe-Lauenburg)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Saxe-Lauenburg]: confirmed (deed of 20 September 1296)
- `/ledger/1` [https://en.wikipedia.org/wiki/Saxe-Lauenburg]: confirmed (Treaty of Perleberg 23 August 1420, to Hamburg and Lübeck)
- `/ledger/2` [https://en.wikipedia.org/wiki/Saxe-Lauenburg]: confirmed (Steinhorst to Gottorp 1575)
- `/ledger/4` [https://en.wikipedia.org/wiki/Saxe-Lauenburg]: confirmed (Hadeln kept in imperial custody 1689)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 2,276-3,288 km2 (Herzogtum Lauenburg district is 1,263 km2 plus Hadeln and Darzing).

### county-of-oettingen: pass

Thin (for a gap-filler):
- `/ledger/0`: confidence-1 found in 1147: About 1147 (page silent on a founding date; 'The Oettingen family was first mentioned in 1147 with Ludovicus comes de Otingen, who was granted the county surrou (page to try: https://en.wikipedia.org/wiki/County_of_Oettingen)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_Oettingen]: confirmed (first mentioned 1147; c1 appropriate)
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Oettingen]: confirmed (1522 partition into Oettingen-Oettingen and Oettingen-Wallerstein; the page also gives 1557 in another passage, c2 appropriate)
- `/ledger/2` [https://en.wikipedia.org/wiki/County_of_Oettingen]: confirmed (raised to principality 1674)
- `/ledger/3` [https://en.wikipedia.org/wiki/County_of_Oettingen]: confirmed (mediatised to Bavaria 1806)

Area: infobox 850 km2 (1806), Cliopatria None km2, ratio 1.19, acknowledged True. Resolved circle 16.4 km = about 1,012 km2 against 850 km2 on the page; within tolerance.

### prince-provostry-of-berchtesgaden: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Prince-Provostry_of_Berchtesgaden]: confirmed (imperial immediacy 1194 from Frederick Barbarossa)
- `/ledger/1` [https://en.wikipedia.org/wiki/Prince-Provostry_of_Berchtesgaden]: confirmed (provosts raised to princes of the Empire 1380)
- `/ledger/2` [https://en.wikipedia.org/wiki/Prince-Provostry_of_Berchtesgaden]: confirmed (Salzburg occupation 1611, expelled by Bavaria the same year)
- `/ledger/4` [https://en.wikipedia.org/wiki/Prince-Provostry_of_Berchtesgaden]: confirmed (secularised 1803 to the Electorate of Salzburg)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; 12 km circle (about 450 km2) is a fair stand-in for the Berchtesgaden Land valley.

### princely-abbey-of-corvey: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Corvey_Abbey]: confirmed (founded 822/826 at the present site; c2 appropriate)
- `/ledger/1` [https://en.wikipedia.org/wiki/Corvey_Abbey]: confirmed (raised to prince-bishopric 1792)
- `/ledger/2` [https://en.wikipedia.org/wiki/Corvey_Abbey]: confirmed (secularised 1803 to the Prince of Nassau-Orange-Fulda)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; 15 km circle round Corvey and Hoxter.

### quedlinburg-abbey: pass

Thin (for a gap-filler):
- `/ledger/2`: the 1236 loss of Duderstadt is confidence 1, derived as 974 plus 262 years; the page names neither the year nor the taker (page to try: https://en.wikipedia.org/wiki/Duderstadt)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Quedlinburg_Abbey]: confirmed ('It was founded in 936 on the initiative of Saint Matilda')
- `/ledger/1` [https://en.wikipedia.org/wiki/Quedlinburg_Abbey]: confirmed ('In 974 the locality of Duderstadt ... was acquired, which the abbey owned for 262 years')
- `/ledger/2` [https://en.wikipedia.org/wiki/Quedlinburg_Abbey]: confirmed as arithmetic only; the note says so and the confidence is 1
- `/ledger/3` [https://en.wikipedia.org/wiki/Quedlinburg_Abbey]: confirmed ('It was disestablished in 1802/3'; mediatisation of 1802 and 1803)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. The page's 90 ha is the World Heritage site, not the territory; the resolved 253 km2 (one cell) is the minimum the gazetteer draws.

### principality-of-hohenzollern-hechingen: fix

Fixes:
- `/ledger/0/counterpart and /identity/predecessors/0/slug` (applied). The 1576 found event and the predecessor named holy-roman-empire, whose dossier ends in 1259; the land-carrying slug after 1259 is holy-roman-empire-minor-states (1260-1806). Evidence: holy-roman-empire.json ends 1259; holy-roman-empire-minor-states.json runs 1260-1806/8; the page: 'The County of Hohenzollern-Hechingen was created in 1576, upon the partition of the County of Hohenzollern'. Fix: Counterpart and predecessor changed to holy-roman-empire-minor-states (re-validated: 0 errors, 0 warnings). A County of Hohenzollern dossier (before 1576) would be the better predecessor once it exists.

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Hohenzollern-Hechingen]: confirmed ('created in 1576, upon the partition of the County of Hohenzollern')
- `/ledger/1` [https://en.wikipedia.org/wiki/Hohenzollern-Hechingen]: confirmed ('The county was raised to a principality in 1623')
- `/ledger/2` [https://en.wikipedia.org/wiki/Hohenzollern-Hechingen]: confirmed ('on 6 August 1849, Hohenzollern was occupied by Prussian forces')
- `/ledger/4` [https://en.wikipedia.org/wiki/Hohenzollern-Hechingen]: confirmed ('On 12 March 1850, Hohenzollern-Hechingen officially became part of Prussia'; sold 7 December 1849)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area in the infobox (population only); 10 km circle resolves to 253 km2.

### duchy-of-schleswig: fix

Fixes:
- `/ledger/1 and /ledger/4 (counterpart)` (not applied). The 1058-1864 fief names kingdom-of-denmark, which has no dossier and whose Cliopatria row ends in 1406, so the vassal pair cannot mirror; the Danish crown is carried by existing dossiers kalmar-union (1397-1523), denmark-norway (1526-1814) and kingdom-of-denmark-1814-1940. Evidence: No kingdom-of-denmark.json in history/polities; denmark-norway.json and kingdom-of-denmark-1814-1940.json exist; kingdom-of-denmark is not in the author's counterparts_needing_dossiers. Fix: Write the fief as a chain: vassal_end kingdom-of-denmark at the row's end, vassal_start/end kalmar-union, denmark-norway, and kingdom-of-denmark-1814-1940 (vassal_end 1864), or list kingdom-of-denmark as a needed dossier; the owners of the Danish dossiers then add the mirrors.
- `/ledger (1435-1460)` (not applied). The neighbour kalmar-union draws Schleswig ceded to the Counts of Holstein in 1435 and regained in 1460 (L5, L11); this dossier has only a 1460 rename, so the two disagree on who held the duchy for 25 years. Evidence: kalmar-union L5 1435/7 loss ('Under the 1435 treaty, the Duchy of Schleswig was ceded to the count of Holstein') and L11 1460/3 gain (Ribe, 5 March 1460). Fix: Add a 1435 vassal/rename step to the Holstein counts and its 1460 end, or have the orchestrator settle which dossier draws the duchy in those years.

Thin (for a gap-filler):
- `/ledger/0`: the 1058 founding is confidence 1 (infobox date only; the page is silent on the event) (page to try: https://en.wikipedia.org/wiki/History_of_Schleswig-Holstein)
- `/ledger/1`: the start of the Danish fief is confidence 1 (entered at the start year) (page to try: https://en.wikipedia.org/wiki/Southern_Jutland)
- `/ledger/5`: the 1864-65 occupation is joint (the page: 'governed jointly by Austria and Prussia'; Gastein 1865 gave Prussia Schleswig); only kingdom-of-prussia is named, while kingdom-of-prussia's own ledger starts the occupation in October 1864 against austrian-empire (page to try: https://en.wikipedia.org/wiki/Gastein_Convention)

Spot checks:
- `/ledger/2` [https://en.wikipedia.org/wiki/Duchy_of_Schleswig]: confirmed ('The title of duke of Schleswig was inherited in 1460 by the hereditary kings of Norway')
- `/ledger/3` [https://en.wikipedia.org/wiki/Duchy_of_Schleswig]: confirmed ('Between 1544 and 1713/20, the ducal reign had become a common dominium')
- `/ledger/5` [https://en.wikipedia.org/wiki/Duchy_of_Schleswig]: confirmed (joint Austro-Prussian government after the Second Schleswig War; February 1864 from the Holstein page per the note)
- `/ledger/7` [https://en.wikipedia.org/wiki/Duchy_of_Schleswig]: confirmed ('Disestablished: 1866'; annexed by Prussia into the Province of Schleswig-Holstein)
- `/keyframe_review/0` [https://en.wikipedia.org/wiki/Duchy_of_Schleswig]: confirmed ('covering the area between about 60 km (35 miles) north and 70 km (45 mi) south of the current border')

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; the clipped polygon resolves to 11,128 km2 (the duchy is usually given as about 9,000-9,500 km2, ratio about 1.2); the west-Funen sliver and the missing Als, Aero and Fehmarn are acknowledged in the keyframe note.

### county-of-zutphen: fix

Fixes:
- `/ledger/3` (not applied). The 1138 passing to Guelders disagrees by 11 years with duchy-of-guelders L1, a confidence-3 gain of Zutphen in 1127, so 1127-1138 is drawn twice. Evidence: County of Zutphen page: 'ruled by the Counts of Zutphen between 1046 and 1138, and then formed a personal union with Guelders' (infobox 'Personal Union with County of Guelders (1138-1339)'); Duchy of Guelders page: Gerard II 'in 1127 acquired the County of Zutphen'. Fix: The two pages disagree; keep 1138 here (the county's own page) and lower duchy-of-guelders L1 to confidence 2 with the year moved to 1138, or note the conflict in both dossiers and let the orchestrator pick one year.

Thin (for a gap-filler):
- `/ledger/2`: the end of the Utrecht fief is put at 1138, while the page's footnote on Utrecht's territories lists 'County of Zutphen (until 1182)'; prince-bishopric-of-utrecht has no Zutphen events to mirror the fief (page to try: https://en.wikipedia.org/wiki/Bishopric_of_Utrecht)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_Zutphen]: confirmed (infobox 'Established: 1046')
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Zutphen]: confirmed ('formed in the eleventh century as a fief of the Bishop of Utrecht'; no year, c2 appropriate)
- `/ledger/2` [https://en.wikipedia.org/wiki/County_of_Zutphen]: confirmed for 1138 as the union date; the page's footnote has Utrecht's tie until 1182
- `/ledger/3` [https://en.wikipedia.org/wiki/County_of_Zutphen]: confirmed (personal union with Guelders from 1138)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; 18 km circle resolves to 1,517 km2 for northern Hamaland.

### county-of-montbeliard: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_Montb%C3%A9liard]: confirmed ('established in 1042 by Emperor Henry III on the territory of the County of Burgundy')
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Montb%C3%A9liard]: confirmed ('upon Henriette's death in 1444, Montbéliard was adjudicated to their son Count Ludwig I of Württemberg-Urach'; infobox 'Acquired by County of Württemberg: 1444')
- `duchy-of-wurttemberg /ledger/4 and /ledger/11` [https://en.wikipedia.org/wiki/County_of_Montb%C3%A9liard]: confirmed (Württemberg holds it from 1444 and loses it to the French Republic in 1793; the hand-over is mirrored)
- `/identity` [https://en.wikipedia.org/wiki/County_of_Montb%C3%A9liard]: the 1407 marriage (Henriette and Eberhard IV) is on the page and not entered; harmless, since the county stayed separate until 1444

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; 20 km circle resolves to 1,012 km2.

### principality-of-nassau-orange-fulda: fix

Fixes:
- `/ledger/2, /ledger/3, /ledger/4 (counterpart)` (not applied). The 1803 gains from the Free Imperial City of Dortmund, Weingarten Abbey and Dietkirchen Abbey name counterparts with no dossier that are not in the author's counterparts_needing_dossiers. Evidence: No such files in history/polities; the author's report lists 40 needed counterparts, none of these three. Fix: Add the three to counterparts_needing_dossiers (the reviewer lists them) or name the umbrella that holds them, holy-roman-empire-minor-states (1260-1806), and have it mirror the losses.
- `/identity/successors` (not applied). Only kingdom-of-westphalia is named, but per the page Fulda stayed under French control until 19 May 1810 (then the Grand Duchy of Frankfurt) and Dortmund went to the Grand Duchy of Berg on 1 March 1808; only Corvey went to Westphalia (7 December 1807). Evidence: Principality of Nassau-Orange-Fulda page, 'Later fate' passages as quoted in the spot checks. Fix: Successors: first-french-empire (Fulda, Dortmund 1806), kingdom-of-westphalia (Corvey), grand-duchy-of-berg (Dortmund); keep the dissolve counterpart first-french-empire.

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Principality_of_Nassau-Orange-Fulda]: confirmed (Reichsdeputationshauptschluss of 25 February 1803; infobox 25 February 1803)
- `/ledger/1` [https://en.wikipedia.org/wiki/Principality_of_Nassau-Orange-Fulda]: confirmed (Corvey among the transferred lands)
- `/ledger/5` [https://en.wikipedia.org/wiki/Principality_of_Nassau-Orange-Fulda]: confirmed ('On 12 July 1806' he 'lost the Lordship of Weingarten', which went to Württemberg)
- `/ledger/7` [https://en.wikipedia.org/wiki/Principality_of_Nassau-Orange-Fulda]: confirmed ('Fulda was occupied by French troops on 27 October 1806')

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 4,046 km2 (1803-05) and 3,541 km2 (1806). The page's Hofen priorate, St. Gerold and Bendern (sold to Austria 1804) are not drawn; they are tiny.

### duchy-of-saxe-weimar: pass

Thin (for a gap-filler):
- `/keyframe_review/0 and /keyframe_review/1`: Gotha (circle 10.72E 50.95N) is drawn in Saxe-Weimar from 1572; the Saxe-Coburg-Eisenach page names only Coburg and Eisenach for the 1572 share and never mentions Gotha, so the holder of Gotha 1572-1638 is unverified (page to try: https://en.wikipedia.org/wiki/Division_of_Erfurt)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Saxe-Weimar]: confirmed ('In 1572 Maximilian II enforced the Division of Erfurt')
- `/ledger/1` [https://en.wikipedia.org/wiki/Saxe-Weimar]: confirmed ('Upon his death in 1602 Saxe-Weimar was again divided'; the page has no 1603)
- `/ledger/2` [https://en.wikipedia.org/wiki/Saxe-Weimar]: confirmed ('When in 1638 the Ernestine Saxe-Eisenach and Saxe-Coburg branch became extinct')
- `/ledger/3` [https://en.wikipedia.org/wiki/Saxe-Weimar]: confirmed (1640 partition with Ernest I and Albert IV)
- `/ledger/7` [https://en.wikipedia.org/wiki/Saxe-Weimar]: confirmed ('Another rearrangement of the Ernestine lands took place in 1672')
- `/ledger/8` [https://en.wikipedia.org/wiki/Saxe-Weimar]: confirmed (Jena 'reverted to Saxe-Weimar upon the death of ... Johann Wilhelm in 1690')

Area: infobox 1612 km2 (1800), Cliopatria None km2, ratio 0.94, acknowledged True. Resolved 1,517 km2 for 1690-1805 against the infobox 1,612 km2 (1800). The 1741 personal union with Eisenach ('united only in the person of the duke' until 1809) is correctly left to a Saxe-Eisenach dossier.

### duchy-of-saxe-gotha-altenburg: fail

Fixes:
- `/keyframe_review/3/correction and /keyframe_review/4/correction (Coburg circle 10.96E 50.26N 10 km)` (not applied, blocking). The 1699 stand-in circle sits on Coburg itself and stays to 1825, but duchy-of-saxe-coburg-saalfeld (same batch) draws the same circle from 6 August 1735, so Coburg is drawn twice for 90 years and this dossier has no 1735 loss. Evidence: Saxe-Coburg-Saalfeld page: the 1699 dispute 'was not settled until 1735'; 'Coburg and Saalfeld united: 6 August 1735'; this dossier's own K3 note: 'The page names no territory; the 10 km Coburg circle is a stand-in'. Fix: Add a 1735/8 loss of the Coburg circle to duchy-of-saxe-coburg-saalfeld (and drop it from K4 from 1735), or move the 1699 stand-in off Coburg to the share Gotha actually received; then name duchy-of-saxe-gotha-altenburg as the counterpart of duchy-of-saxe-coburg-saalfeld L1.
- `/keyframe_review/1 and /ledger/2` (not applied). The 1672-1679 shape has only Gotha, Altenburg and Saalfeld, and the 1680 partition records only the Saalfeld loss, so the other five shares of Ernest the Pious (Coburg, Meiningen, Romhild, Eisenberg, Hildburghausen) are undrawn 1672-1680 and their 1680 losses are missing. Evidence: Saxe-Gotha-Altenburg page: 'Ernest the Pious ... inherited the major part of his possessions' in 1672 and 'Ernest's combined duchy was divided again after his death in 1675', the division completed in 1680; the author's notes name the five shares. Fix: Add the 1672 lands (at least Coburg and Eisenberg from the Altenburg inheritance) and the 1680 losses to the five new duchies (counterparts needing dossiers), or say in the K1 note that they are left out and why.

Thin (for a gap-filler):
- `/ledger/3`: the 1699 gain is confidence 1 with no territory named (page to try: https://en.wikipedia.org/wiki/Saxe-Coburg)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Saxe-Gotha-Altenburg]: confirmed ('In 1640 the sons of the late Ernestine duke John II of Saxe-Weimar divided their paternal heritage')
- `/ledger/1` [https://en.wikipedia.org/wiki/Saxe-Gotha-Altenburg]: confirmed (1672, Frederick William III of Saxe-Altenburg died)
- `/ledger/2` [https://en.wikipedia.org/wiki/Saxe-Coburg-Saalfeld]: confirmed ('divided on 24 February 1680 among his seven surviving sons')
- `/ledger/4` [https://en.wikipedia.org/wiki/Saxe-Gotha-Altenburg]: confirmed ('upon the death of Duke Christian of Saxe-Eisenberg in 1707')
- `/ledger/5` [https://en.wikipedia.org/wiki/Saxe-Gotha-Altenburg]: confirmed (1826 arbitration: Altenburg to the Duke of Saxe-Hildburghausen)

Area: infobox 3007 km2 (1800), Cliopatria None km2, ratio 1.26, acknowledged True. Resolved 3,794 km2 for 1707-1825 against the infobox 3,007 km2 (1800); the author quotes 3,140 km2 in circles. Within tolerance, but about 250-300 km2 of it is the double-drawn Coburg circle.

### duchy-of-saxe-coburg-saalfeld: fix

Fixes:
- `/ledger/1/counterpart` (not applied). The 1735 gain of Coburg names 'Saxe-Coburg (extinct 1699; no dossier)', a duchy that no longer existed; within this batch duchy-of-saxe-gotha-altenburg holds the same Coburg circle from 1699. Evidence: Saxe-Coburg-Saalfeld page: the dispute after 1699 'was not settled until 1735'; duchy-of-saxe-gotha-altenburg K3 (1699-1706) and K4 (1707-1825) draw the Coburg circle 10.96E 50.26N 10 km. Fix: Name duchy-of-saxe-gotha-altenburg (or the disputing duchies) as the counterpart once that dossier carries the matching 1735 loss.

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Saxe-Coburg-Saalfeld]: confirmed ('divided on 24 February 1680 among his seven surviving sons')
- `/ledger/1` [https://en.wikipedia.org/wiki/Saxe-Coburg-Saalfeld]: confirmed ('Coburg and Saalfeld united: 6 August 1735')
- `/ledger/2` [https://en.wikipedia.org/wiki/Saxe-Coburg-Saalfeld]: confirmed ('From November 1806 until the Peace of Tilsit in July 1807, the Principality was occupied by the French')
- `/ledger/4` [https://en.wikipedia.org/wiki/Saxe-Coburg-Saalfeld]: confirmed ('In 1815 ... the Congress of Vienna sent an area'; c2 for the land)
- `/ledger/6` [https://en.wikipedia.org/wiki/Saxe-Coburg-Saalfeld]: confirmed ('On 12 November 1826 the decision, from the arbitration')

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 759-1,770 km2.

### duchy-of-saxe-weissenfels: fail

Fixes:
- `/keyframe_review/0/correction, /keyframe_review/1/correction, /keyframe_review/2/correction` (not applied, blocking). The shapes leave out six of the duchy's Ämter that the page names: Freyburg, Sachsenburg (Oldisleben), Sangerhausen, Eckartsberga, Weissensee and Langensalza; none of them falls in the drawn cells, so about 3,000 km2 is undrawn 1656-1746 and the omission is not acknowledged. Evidence: Saxe-Weissenfels page: 'Beside Weissenfels the duchy comprised the ämter of Freyburg, Sachsenburg (present-day Oldisleben), Sangerhausen, Eckartsberga, Weißensee and Langensalza'; the neighbour electorate-of-saxony L23 (1656/10) loses 5,817 km2 to the duchy against 2,782 km2 drawn here. Fix: Add circles (or the Saxony L23 region) for Freyburg 11.77E 51.21N, Oldisleben 11.17E 51.31N, Sangerhausen 11.30E 51.47N, Eckartsberga 11.56E 51.12N, Weissensee 11.07E 51.20N and Langensalza 10.65E 51.11N to all three keyframes and to the found event.
- `/ledger/0` (not applied). The Magdeburg lordships are gained from archbishopric-of-magdeburg in 1656, but the page says they had been 'adjudicated to Saxony by the 1635 Peace of Prague', and electorate-of-saxony L16 gains them from Magdeburg in 1635; the event also sits before the found event. Evidence: Saxe-Weissenfels page as quoted; electorate-of-saxony L16 1635/5 gain from archbishopric-of-magdeburg. Fix: Fold the four lordships into the found event's region (counterpart electorate-of-saxony) and delete L0, or name electorate-of-saxony as its counterpart and put it after L1.
- `/ledger/3/counterpart` (applied). The 1687 sale of Burg named electorate-of-brandenburg, whose dossier ends in 1618. Evidence: Saxe-Weissenfels page: 'Johann Adolf I sold Burg to Brandenburg in 1687'; brandenburg-prussia.json runs 1618/8-1701/1. Fix: Changed to brandenburg-prussia (re-validated: 0 errors, 0 warnings); brandenburg-prussia has no 1687 gain of Burg to mirror it.

Spot checks:
- `/ledger/1` [https://en.wikipedia.org/wiki/Saxe-Weissenfels]: confirmed ('Death of elector Johann Georg I: 8 October 1656'; 'upon his death the Duchies of Saxe-Zeitz, Saxe-Merseburg and Saxe-Weissenfels arose')
- `/ledger/2` [https://en.wikipedia.org/wiki/Saxe-Weissenfels]: confirmed ('In 1659 Augustus also acquired the County of Barby')
- `/ledger/3` [https://en.wikipedia.org/wiki/Saxe-Weissenfels]: confirmed ('Johann Adolf I sold Burg to Brandenburg in 1687')
- `/ledger/4` [https://en.wikipedia.org/wiki/Saxe-Weissenfels]: confirmed ('Ducal line extinct: 16 May 1746'; passed to the Electorate of Saxony)
- `/keyframe_review/0` [https://en.wikipedia.org/wiki/Saxe-Weissenfels]: not on page as drawn: six named Ämter lie outside the shape

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged False. No area on the page; the drawn 2,782-3,035 km2 is about half of electorate-of-saxony's 1656 loss region (5,817 km2), which covers the named Ämter.

### duchy-of-saxe-merseburg: fail

Fixes:
- `/keyframe_review/0/correction and /ledger/0` (not applied, blocking). The Lower Lusatia part is a 22 km circle at Lübben, which leaves out Doberlug and Finsterwalde, two of the three towns the page names, and the rest of the margraviate; Delitzsch and Bitterfeld are also outside, so the neighbour electorate-of-saxony's 1657 loss of 7,081 km2 is drawn here as 4,299 km2 and the rest is undrawn 1657-1738. Evidence: Saxe-Merseburg page: 'the Margraviate of Lower Lusatia, including the cities and castles of Lübben, Doberlug, Finsterwalde'; electorate-of-saxony L24 (1657/4) loses 'Merseburg and Lützen', 'Delitzsch and Bitterfeld', 'Lower Lusatia west: Lübben, Doberlug, Finsterwalde' and Lower Lusatia east; the K0 note does not acknowledge the gap. Fix: Draw the whole margraviate (ask for a gazetteer 'Lower Lusatia' region; until then reuse the electorate-of-saxony L24 union) plus the Delitzsch-Bitterfeld circle, in K0 and in L0 and L1.

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Saxe-Merseburg]: confirmed ('friend-brotherly main treaty' in Dresden on 22 April 1657; 'existed from 1656 or 1657 to 1738')
- `/ledger/1` [https://en.wikipedia.org/wiki/Saxe-Merseburg]: confirmed ('After the death of the last male heir of the Saxon branch line in 1738'; fell back to the Electorate)
- `/keyframe_review/0` [https://en.wikipedia.org/wiki/Saxe-Merseburg]: not on page as drawn: Doberlug and Finsterwalde lie outside the shape
- `electorate-of-saxony /ledger/24 and /ledger/29` [https://en.wikipedia.org/wiki/Saxe-Merseburg]: years mirror (1657/4 and 1738), but Saxony names the counterpart 'saxe-merseburg', not this slug

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged False. No area on the page; drawn 4,299 km2 against the neighbour's 7,081 km2 for the same 1657 hand-over.

### duchy-of-saxe-zeitz: fix

Fixes:
- `/ledger/1/counterpart` (not applied). The 1660 gain of Schleusingen, Suhl and Kühndorf names county-of-henneberg, whose dossier ends in 1583 and dissolves into electorate-of-saxony. Evidence: county-of-henneberg L-last: 1583 dissolve, counterpart electorate-of-saxony; Saxe-Zeitz page: 'He also received the city of Schleusingen in 1660'. Fix: Name electorate-of-saxony (the Albertine share of the Henneberg condominium) as the counterpart; note that electorate-of-saxony already gives Schleusingen and Suhl away in its 1657 loss (L25), three years early.
- `/keyframe_review/0/correction and /keyframe_review/1/correction` (not applied). The 22 km Zeitz circle does not reach Naumburg, one of the three districts the page names, although the K0 note says it covers them. Evidence: Saxe-Zeitz page: 'received the districts of Zeitz, Naumburg and Haynsburg'; a 1 km point at Naumburg (11.81E 51.15N) resolves to a cell outside the K0 cells. Fix: Add a Naumburg circle (11.81E 51.15N, 10-12 km) to K0, K1, L0 and L2.

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Saxe-Zeitz]: confirmed ('established in 1657'; treaty of 22 April 1657)
- `/ledger/1` [https://en.wikipedia.org/wiki/Saxe-Zeitz]: confirmed ('He also received the city of Schleusingen in 1660'; Suhl and Kühndorf named)
- `/ledger/2` [https://en.wikipedia.org/wiki/Saxe-Zeitz]: confirmed ('the first of the three Saxon secundogenitures to die out in 1718')
- `electorate-of-saxony /ledger/25 and /ledger/28` [https://en.wikipedia.org/wiki/Saxe-Zeitz]: years mirror (1657/4, 1718), counterpart string 'saxe-zeitz' instead of this slug

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 1,770-2,782 km2, equal to electorate-of-saxony's 2,782 km2 loss region.

### duchy-of-arenberg: fix

Fixes:
- `/ledger/6` (not applied). The 1803 gain of the Vest Recklinghausen and Meppen names counterpart nobody, but within this batch prince-bishopric-of-munster L9 (1803/2) loses land to duchy-of-arenberg, and the Vest Recklinghausen belonged to the Electorate of Cologne. Evidence: Duchy of Arenberg page: 'the Duke of Arenberg received in 1803 new lands: the county of Vest Recklinghausen, the county of Meppen, and later the lordship of Dülmen' (no giver named); prince-bishopric-of-munster L1 (1252, Meppen bought by the see) and L9 (1803 loss to duchy-of-arenberg). Fix: Split L6 into a Meppen gain from prince-bishopric-of-munster (1803/2) and a Recklinghausen gain from electorate-of-cologne (1803), confidence 2; electorate-of-cologne then needs the mirror loss.
- `/identity/predecessors/0/slug` (applied). The predecessor named holy-roman-empire, whose dossier ends in 1259 (the state starts 1549). Evidence: holy-roman-empire.json ends 1259; holy-roman-empire-minor-states.json runs 1260-1806. Fix: Changed to holy-roman-empire-minor-states (re-validated: 0 errors, 0 warnings).

Thin (for a gap-filler):
- `/ledger/3`: the French occupation 'around 1798' is confidence 1 with no year on the page (page to try: https://en.wikipedia.org/wiki/Treaty_of_Campo_Formio)
- `/ledger/4 and /ledger/5`: the end of the occupation and the cession of the Ahr lands are confidence 1 and both put at 1803; the Treaty of Lunéville (1801) is the likelier cession (page to try: https://en.wikipedia.org/wiki/Treaty_of_Lun%C3%A9ville)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/Duchy_of_Arenberg]: confirmed ('became an immediate (reichsunmittelbar) state of the Holy Roman Empire in 1549')
- `/ledger/1` [https://en.wikipedia.org/wiki/Duchy_of_Arenberg]: confirmed ('raised to a princely county in 1576')
- `/ledger/2` [https://en.wikipedia.org/wiki/Duchy_of_Arenberg]: confirmed ('then became a duchy in 1645')
- `/ledger/6` [https://en.wikipedia.org/wiki/Duchy_of_Arenberg]: confirmed for the year and the land; the page names no giver, and 'nobody' is wrong (see fixes)
- `/ledger/7 and /ledger/8` [https://en.wikipedia.org/wiki/Duchy_of_Arenberg]: confirmed ('France annexing Dülmen and Meppen, and the Grand Duchy of Berg annexing Recklinghausen' in 1810)

Area: infobox 413 km2 (1802), Cliopatria None km2, ratio 1.23, acknowledged True. Resolved 506 km2 for 1549-1802 against the infobox 413 km2 (pre-Napoleonic duchy).

### county-of-wied: pass

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_Wied]: confirmed (infobox 'Established / Reichsfreiheit: 1093'; c2 appropriate)
- `/ledger/1` [https://en.wikipedia.org/wiki/County_of_Wied]: confirmed ('From 1243-1462, Wied was united with an Isenburgian County as Isenburg-Wied')
- `/ledger/3 and /ledger/4` [https://en.wikipedia.org/wiki/County_of_Wied]: confirmed ('partitioned twice: between itself and Wied-Dierdorf in 1631, and between Wied-Neuwied and Wied-Runkel in 1698')
- `/ledger/5` [https://en.wikipedia.org/wiki/County_of_Wied]: confirmed ('incorporated into the Duchy of Nassau in 1806'; the infobox says Nassau-Weilburg)

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; 16 km circle resolves to 759 km2.

### county-of-stolberg: fail

Fixes:
- `/keyframe_review/4/correction (Königstein circle 8.47E 50.18N 8 km) and /ledger` (not applied, blocking). Königstein is drawn in Stolberg from 1535 to 1805, but it belonged to the Electorate of Mainz by 1581; no loss is entered and electorate-of-mainz (same batch) has no gain, so the land is mis-assigned for over two centuries. Evidence: Königstein im Taunus page: 'By 1581, Königstein belonged to the Electorate of Mainz, which had incorporated the old County through a legal dispute'; the County of Stolberg page dates no loss. Fix: Add a 1581 loss of the Königstein circle to electorate-of-mainz (confidence 2, source the Königstein im Taunus page), split K4 at 1581, and add the mirror gain to electorate-of-mainz.
- `/ledger/7/counterpart` (applied). The 1806 end named holy-roman-empire, whose dossier ends in 1259. Evidence: holy-roman-empire.json ends 1259; holy-roman-empire-minor-states.json runs to 1806/8. Fix: Changed to holy-roman-empire-minor-states (re-validated: 0 errors, 0 warnings); the real 1806-07 successors (Prussia for Wernigerode, Saxony for Stolberg and Rossla, the Kingdom of Westphalia) still need a page and the empty successors list needs filling.

Thin (for a gap-filler):
- `/ledger/7`: the 1806 end is confidence 1: the page does not mention the mediatisation (page to try: https://en.wikipedia.org/wiki/Stolberg-Wernigerode)
- `/keyframe_review/4`: Rochefort (1544) is kept to 1805 with no loss; the page dates none and the County of Rochefort page would not load (page to try: https://en.wikipedia.org/wiki/Rochefort,_Belgium)

Spot checks:
- `/ledger/0` [https://en.wikipedia.org/wiki/County_of_Stolberg]: confirmed (castle 'first mentioned in 1210'; infobox 'Established: 1210')
- `/ledger/2` [https://en.wikipedia.org/wiki/County_of_Stolberg]: confirmed ('the lower County of Hohnstein (1417)')
- `/ledger/3` [https://en.wikipedia.org/wiki/County_of_Stolberg]: confirmed ('inherited the County of Wernigerode in 1429')
- `/ledger/4` [https://en.wikipedia.org/wiki/County_of_Stolberg]: confirmed ('the County of Königstein in 1535')
- `/ledger/5` [https://en.wikipedia.org/wiki/County_of_Stolberg]: confirmed ('the County of Rochefort in 1544')
- `/ledger/6` [https://en.wikipedia.org/wiki/County_of_Stolberg]: confirmed ('On 19 March 1548 the line was split')

Area: infobox None km2 (None), Cliopatria None km2, ratio None, acknowledged True. No area on the page; resolved 1,012-2,782 km2.

## Cross-dossier matrix: rows that are not matched

| Event | Counterpart | Mirror | Status | Note |
|---|---|---|---|---|
| electoral-palatinate 1085 found | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch); found/dissolve listed for routing only |
| electoral-palatinate 1621 occupation_start | kingdom-of-spain |  | missing | no mirror in kingdom-of-spain (outside this batch) |
| electoral-palatinate 1622 occupation_start | duchy-of-bavaria | duchy-of-bavaria 1623 gain | mismatch | mirror within a year but of type gain (outside this batch) |
| electoral-palatinate 1648 occupation_end | duchy-of-bavaria | duchy-of-bavaria 1329 loss | mismatch | nearest mirror is loss 1329, 319 years off (outside this batch) |
| electoral-palatinate 1652 occupation_end | kingdom-of-spain |  | missing | no mirror in kingdom-of-spain (outside this batch) |
| duchy-of-wurttemberg 1081 found | stem-duchy-of-swabia |  | missing | no mirror in stem-duchy-of-swabia (outside this batch); found/dissolve listed for routing only |
| duchy-of-wurttemberg 1250 gain | stem-duchy-of-swabia |  | missing | no mirror in stem-duchy-of-swabia (outside this batch) |
| duchy-of-wurttemberg 1251 gain | margraviate-of-baden |  | missing | no mirror in margraviate-of-baden (in this batch) |
| duchy-of-wurttemberg 1442 split |  |  | exception | internal partition; no counterpart named |
| duchy-of-wurttemberg 1482 merge | Württemberg-Urach |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| duchy-of-wurttemberg 1520 loss | habsburg-monarchy |  | missing | no mirror in habsburg-monarchy (outside this batch) |
| duchy-of-wurttemberg 1534 gain | habsburg-monarchy |  | missing | no mirror in habsburg-monarchy (outside this batch) |
| duchy-of-wurttemberg 1634 occupation_start | habsburg-monarchy |  | missing | no mirror in habsburg-monarchy (outside this batch) |
| duchy-of-wurttemberg 1648 occupation_end | habsburg-monarchy |  | missing | no mirror in habsburg-monarchy (outside this batch) |
| duchy-of-wurttemberg 1793 loss | french-first-republic |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| landgraviate-of-hesse 1308 split |  |  | exception | internal partition; no counterpart named |
| landgraviate-of-hesse 1311 merge | Upper Hesse |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| landgraviate-of-hesse 1458 split |  |  | exception | internal partition; no counterpart named |
| landgraviate-of-hesse 1500 merge | Upper Hesse |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| landgraviate-of-hesse 1567 split |  |  | exception | internal partition; no counterpart named |
| landgraviate-of-hesse-kassel 1648 gain | county-of-schaumburg |  | missing | no mirror in county-of-schaumburg (in this batch) |
| landgraviate-of-hesse-kassel 1760 occupation_start | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| landgraviate-of-hesse-kassel 1763 occupation_end | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| landgraviate-of-hesse-kassel 1801 loss | french-consulate |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| landgraviate-of-hesse-darmstadt 1567 found | landgraviate-of-hesse |  | missing | no mirror in landgraviate-of-hesse (in this batch); found/dissolve listed for routing only |
| landgraviate-of-hesse-darmstadt 1803 loss | french-consulate |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| habsburg-netherlands 1482 found | duchy-of-burgundy |  | missing | no mirror in duchy-of-burgundy (outside this batch); found/dissolve listed for routing only |
| habsburg-netherlands 1493 gain | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| habsburg-netherlands 1524 gain | Albertine Saxony |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| habsburg-netherlands 1528 gain | prince-bishopric-of-utrecht |  | missing | no mirror in prince-bishopric-of-utrecht (outside this batch) |
| habsburg-netherlands 1536 gain | Lordship of Groningen |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| habsburg-netherlands 1581 split |  |  | exception | internal partition; no counterpart named |
| habsburg-netherlands 1659 loss | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| habsburg-netherlands 1659 loss | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| habsburg-netherlands 1659 loss | kingdom-of-england |  | missing | no mirror in kingdom-of-england (outside this batch) |
| habsburg-netherlands 1668 loss | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| habsburg-netherlands 1677 loss | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| habsburg-netherlands 1678 gain | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| habsburg-netherlands 1678 occupation_start | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| habsburg-netherlands 1678 loss | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| habsburg-netherlands 1678 occupation_end | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| habsburg-netherlands 1678 gain | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| habsburg-netherlands 1683 loss | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| habsburg-netherlands 1684 loss | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| habsburg-netherlands 1697 gain | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| habsburg-netherlands 1706 occupation_start | dutch-republic | dutch-republic 1585 loss | mismatch | nearest mirror is loss 1585, 121 years off (outside this batch) |
| habsburg-netherlands 1744 occupation_start | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| habsburg-netherlands 1748 occupation_end | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| habsburg-netherlands 1794 occupation_start | french-first-republic |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| habsburg-netherlands 1795 occupation_end | french-first-republic |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| electorate-of-cologne 953 found | kingdom-of-germany |  | missing | no mirror in kingdom-of-germany (outside this batch); found/dissolve listed for routing only |
| electorate-of-cologne 1180 gain | stem-duchy-of-saxony |  | missing | no mirror in stem-duchy-of-saxony (outside this batch) |
| electorate-of-cologne 1368 gain | county-of-arnsberg |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| electorate-of-cologne 1449 loss | duchy-of-cleves |  | missing | no mirror in duchy-of-cleves (in this batch) |
| electorate-of-cologne 1794 occupation_start | french-first-republic |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| electorate-of-cologne 1801 occupation_end | french-first-republic |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| electorate-of-cologne 1801 loss | french-consulate |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| electorate-of-mainz 780 found | kingdom-of-the-franks |  | missing | no mirror in kingdom-of-the-franks (outside this batch); found/dissolve listed for routing only |
| electorate-of-mainz 1022 gain | nobody |  | exception | counterpart 'nobody' |
| electorate-of-mainz 1242 loss | city-of-mainz |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| electorate-of-mainz 1462 gain | city-of-mainz |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| electorate-of-mainz 1664 gain | city-of-erfurt |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| electorate-of-mainz 1792 occupation_start | french-first-republic |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| electorate-of-mainz 1793 occupation_end | french-first-republic |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| electorate-of-mainz 1795 occupation_start | french-first-republic |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| electorate-of-mainz 1801 occupation_end | french-first-republic |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| electorate-of-mainz 1801 loss | french-consulate |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| electorate-of-mainz 1802 loss | kingdom-of-prussia |  | missing | no mirror in kingdom-of-prussia (outside this batch) |
| electorate-of-mainz 1803 loss | kingdom-of-prussia |  | missing | no mirror in kingdom-of-prussia (outside this batch) |
| prince-bishopric-of-munster 1180 found | stem-duchy-of-saxony |  | missing | no mirror in stem-duchy-of-saxony (outside this batch); found/dissolve listed for routing only |
| prince-bishopric-of-munster 1252 gain | county-of-vechta |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| prince-bishopric-of-munster 1403 gain | county-of-oldenburg | county-of-oldenburg 1803 gain | mismatch | nearest mirror is gain 1803, 400 years off (in this batch) |
| prince-bishopric-of-munster 1406 gain | Lordship of Ahaus |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| prince-bishopric-of-munster 1429 gain | prince-archbishopric-of-bremen |  | missing | no mirror in prince-archbishopric-of-bremen (outside this batch) |
| prince-bishopric-of-munster 1534 loss | anabaptist-kingdom-of-munster |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| prince-bishopric-of-munster 1535 gain | anabaptist-kingdom-of-munster |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| prince-bishopric-of-munster 1802 occupation_start | kingdom-of-prussia |  | missing | no mirror in kingdom-of-prussia (outside this batch) |
| prince-bishopric-of-munster 1803 loss | duchy-of-arenberg |  | mismatch | duchy-of-arenberg L6 gains Meppen and Recklinghausen in 1803 from 'nobody' instead of this dossier; no mirror in duchy-of-arenberg (in this batch) |
| prince-bishopric-of-munster 1803 dissolve | kingdom-of-prussia |  | missing | no mirror in kingdom-of-prussia (outside this batch); found/dissolve listed for routing only |
| prince-bishopric-of-munster 1803 occupation_end | kingdom-of-prussia |  | missing | no mirror in kingdom-of-prussia (outside this batch) |
| prince-bishopric-of-munster 1803 loss | kingdom-of-prussia |  | missing | no mirror in kingdom-of-prussia (outside this batch) |
| county-of-tyrol 1140 found | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch); found/dissolve listed for routing only |
| county-of-tyrol 1271 gain | unnamed Adige and Inn valley lords |  | exception | the page names no counterpart (unnamed Adige and Inn valley lords) |
| county-of-tyrol 1363 dissolve | house-of-habsburg | house-of-habsburg 1286 loss | mismatch | nearest mirror is loss 1286, 77 years off (outside this batch) |
| duchy-of-brunswick-luneburg 1235 found | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch); found/dissolve listed for routing only |
| duchy-of-brunswick-luneburg 1692 dissolve | electorate-of-hanover |  | missing | no mirror in electorate-of-hanover (outside this batch); found/dissolve listed for routing only |
| margraviate-of-baden 1112 found | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch); found/dissolve listed for routing only |
| margraviate-of-baden 1190 gain | nobody |  | exception | counterpart 'nobody' |
| margraviate-of-baden 1442 gain | lordship-of-lahr-mahlberg |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| margraviate-of-baden 1771 merge | Baden-Baden line |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| prince-bishopric-of-wurzburg 1168 found | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch); found/dissolve listed for routing only |
| prince-bishopric-of-wurzburg 1633 occupation_start | swedish-empire |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| prince-bishopric-of-wurzburg 1634 occupation_end | swedish-empire |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| prince-bishopric-of-bamberg 1245 found | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch); found/dissolve listed for routing only |
| prince-bishopric-of-bamberg 1631 occupation_start | swedish-empire |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| prince-bishopric-of-bamberg 1634 occupation_end | swedish-empire |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| prince-bishopric-of-bamberg 1759 loss | habsburg-monarchy |  | missing | no mirror in habsburg-monarchy (outside this batch) |
| prince-bishopric-of-bamberg 1802 occupation_start | duchy-of-bavaria | duchy-of-bavaria 1803 gain | mismatch | mirror within a year but of type gain (outside this batch) |
| duchy-of-julich-berg 1003 found | duchy-of-lower-lorraine |  | missing | no mirror in duchy-of-lower-lorraine (outside this batch); found/dissolve listed for routing only |
| duchy-of-julich-berg 1609 occupation_start | habsburg-monarchy |  | missing | no mirror in habsburg-monarchy (outside this batch) |
| duchy-of-julich-berg 1610 occupation_end | habsburg-monarchy |  | missing | no mirror in habsburg-monarchy (outside this batch) |
| duchy-of-julich-berg 1614 loss | electorate-of-brandenburg |  | missing | no mirror in electorate-of-brandenburg (outside this batch) |
| duchy-of-julich-berg 1794 occupation_start | french-first-republic |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| duchy-of-julich-berg 1801 occupation_end | french-first-republic |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| duchy-of-julich-berg 1801 loss | french-consulate |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| duchy-of-cleves 1092 found | duchy-of-lower-lorraine |  | missing | no mirror in duchy-of-lower-lorraine (outside this batch); found/dissolve listed for routing only |
| duchy-of-cleves 1614 dissolve | electorate-of-brandenburg |  | missing | no mirror in electorate-of-brandenburg (outside this batch); found/dissolve listed for routing only |
| duchy-of-guelders 1096 found | duchy-of-lower-lorraine |  | missing | no mirror in duchy-of-lower-lorraine (outside this batch); found/dissolve listed for routing only |
| duchy-of-guelders 1127 gain | county-of-zutphen | county-of-zutphen 1138 dissolve | mismatch | the two pages disagree: Duchy of Guelders page 1127, County of Zutphen page 1138 (personal union 1138-1339); 1127-1138 drawn twice; nearest mirror is dissolve 1138, 11 years off (in this batch) |
| duchy-of-guelders 1339 gain | nobody |  | exception | counterpart 'nobody' |
| duchy-of-guelders 1473 occupation_start | duchy-of-burgundy | duchy-of-burgundy 1473 gain | mismatch | mirror within a year but of type gain (outside this batch) |
| duchy-of-guelders 1492 occupation_end | duchy-of-burgundy | duchy-of-burgundy 1473 gain | mismatch | nearest mirror is gain 1473, 19 years off (outside this batch) |
| county-of-hainaut 880 found | west-franks |  | missing | no mirror in west-franks (outside this batch); found/dissolve listed for routing only |
| duchy-of-pomerania 1188 found | pomerania |  | missing | no mirror in pomerania (outside this batch); found/dissolve listed for routing only |
| duchy-of-pomerania 1250 loss | margraviate-of-brandenburg | margraviate-of-brandenburg 1317 loss | mismatch | nearest mirror is loss 1317, 67 years off (outside this batch) |
| duchy-of-pomerania 1317 gain | page names no previous holder |  | exception | the page names no counterpart (page names no previous holder) |
| duchy-of-pomerania 1329 loss | teutonic-order |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| duchy-of-pomerania 1341 gain | teutonic-order |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| duchy-of-pomerania 1466 gain | teutonic-order |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| duchy-of-pomerania 1478 merge | Pomerania-Wolgast and Pomerania-Stettin lines |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| duchy-of-pomerania 1630 occupation_start | swedish-empire |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| duchy-of-pomerania 1637 occupation_end | swedish-empire |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| county-of-oldenburg 1108 found | stem-duchy-of-saxony |  | missing | no mirror in stem-duchy-of-saxony (outside this batch); found/dissolve listed for routing only |
| county-of-oldenburg 1624 gain | lordship-of-varel |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| county-of-oldenburg 1647 gain | county-of-delmenhorst |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| prince-bishopric-of-hildesheim 1235 found | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch); found/dissolve listed for routing only |
| prince-bishopric-of-hildesheim 1803 dissolve | kingdom-of-prussia |  | missing | no mirror in kingdom-of-prussia (outside this batch); found/dissolve listed for routing only |
| prince-bishopric-of-osnabruck 1225 found | stem-duchy-of-saxony |  | missing | no mirror in stem-duchy-of-saxony (outside this batch); found/dissolve listed for routing only |
| prince-bishopric-of-osnabruck 1803 dissolve | electorate-of-hanover |  | missing | no mirror in electorate-of-hanover (outside this batch); found/dissolve listed for routing only |
| prince-bishopric-of-paderborn 1281 found | stem-duchy-of-saxony |  | missing | no mirror in stem-duchy-of-saxony (outside this batch); found/dissolve listed for routing only |
| prince-bishopric-of-paderborn 1802 dissolve | kingdom-of-prussia |  | missing | no mirror in kingdom-of-prussia (outside this batch); found/dissolve listed for routing only |
| principality-of-ansbach 1791 dissolve | kingdom-of-prussia |  | missing | no mirror in kingdom-of-prussia (outside this batch); found/dissolve listed for routing only |
| principality-of-bayreuth 1791 dissolve | kingdom-of-prussia |  | missing | no mirror in kingdom-of-prussia (outside this batch); found/dissolve listed for routing only |
| county-of-east-frisia 1464 found | frisia |  | missing | no mirror in frisia (outside this batch); found/dissolve listed for routing only |
| county-of-east-frisia 1600 gain | lordship-of-harlingerland |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| county-of-east-frisia 1611 occupation_start | dutch-republic |  | missing | no mirror in dutch-republic (outside this batch) |
| county-of-east-frisia 1744 occupation_end | dutch-republic |  | missing | no mirror in dutch-republic (outside this batch) |
| county-of-east-frisia 1744 dissolve | kingdom-of-prussia |  | missing | no mirror in kingdom-of-prussia (outside this batch); found/dissolve listed for routing only |
| mecklenburg 1170 found | stem-duchy-of-saxony |  | missing | no mirror in stem-duchy-of-saxony (outside this batch); found/dissolve listed for routing only |
| mecklenburg 1301 gain | page names no previous holder |  | exception | the page names no counterpart (page names no previous holder) |
| mecklenburg 1312 gain | lordships of Rostock and Stargard |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| mecklenburg 1358 gain | county-of-schwerin | county-of-schwerin 1368 dissolve | mismatch | page conflict: Mecklenburg page 1358, County of Schwerin page 7 December 1368 (Treaty of Plüschow); ten years drawn twice; nearest mirror is dissolve 1368, 10 years off (in this batch) |
| mecklenburg 1628 occupation_start | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch) |
| mecklenburg 1631 occupation_end | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch) |
| mecklenburg 1648 loss | swedish-empire |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| mecklenburg 1803 gain | swedish-empire |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| palatinate-neuburg 1505 found | duchy-of-bavaria |  | missing | no mirror in duchy-of-bavaria (outside this batch); found/dissolve listed for routing only |
| landgraviate-of-hesse-marburg 1567 found | landgraviate-of-hesse |  | missing | no mirror in landgraviate-of-hesse (in this batch); found/dissolve listed for routing only |
| landgraviate-of-hesse-rheinfels 1567 found | landgraviate-of-hesse |  | missing | no mirror in landgraviate-of-hesse (in this batch); found/dissolve listed for routing only |
| county-of-hanau 1480 gain | barony-of-lichtenberg |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| county-of-hanau 1680 vassal_start | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| county-of-schaumburg 1110 found | stem-duchy-of-saxony |  | missing | no mirror in stem-duchy-of-saxony (outside this batch); found/dissolve listed for routing only |
| swabian-circle 1500 found | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch); found/dissolve listed for routing only |
| swabian-circle 1806 dissolve | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch); found/dissolve listed for routing only |
| franconian-circle 1500 found | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch); found/dissolve listed for routing only |
| franconian-circle 1806 dissolve | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch); found/dissolve listed for routing only |
| further-austria 1278 found | house-of-habsburg |  | missing | no mirror in house-of-habsburg (outside this batch); found/dissolve listed for routing only |
| further-austria 1368 gain | unnamed seller (page silent) |  | exception | the page names no counterpart (unnamed seller (page silent)) |
| further-austria 1648 loss | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| further-austria 1780 gain | unnamed seller (page silent) |  | exception | the page names no counterpart (unnamed seller (page silent)) |
| further-austria 1797 loss | unnamed recipient (page silent) |  | exception | the page names no counterpart (unnamed recipient (page silent)) |
| further-austria 1801 loss | duchy-of-modena |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| further-austria 1803 gain | duchy-of-modena |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| prince-bishopric-of-augsburg 1248 gain | nobody |  | exception | counterpart 'nobody' |
| prince-bishopric-of-augsburg 1309 gain | nobody |  | exception | counterpart 'nobody' |
| prince-bishopric-of-augsburg 1632 occupation_start | kingdom-of-sweden |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| prince-bishopric-of-augsburg 1635 occupation_end | kingdom-of-sweden |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| prince-bishopric-of-strasbourg 1681 loss | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| prince-bishopric-of-halberstadt 1648 dissolve | brandenburg-prussia |  | missing | no mirror in brandenburg-prussia (outside this batch); found/dissolve listed for routing only |
| prince-bishopric-of-trent 1027 found | march-of-verona | march-of-verona 1004 loss | mismatch | nearest mirror is loss 1004, 23 years off (outside this batch) |
| prince-bishopric-of-trent 1511 vassal_start | habsburg-monarchy |  | missing | no mirror in habsburg-monarchy (outside this batch) |
| prince-bishopric-of-trent 1803 dissolve | habsburg-monarchy |  | missing | no mirror in habsburg-monarchy (outside this batch); found/dissolve listed for routing only |
| prince-bishopric-of-brixen 1027 found | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch); found/dissolve listed for routing only |
| prince-bishopric-of-brixen 1091 gain | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch) |
| prince-bishopric-of-brixen 1165 loss | Counts of Andechs-Meran (no dossier) |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| prince-bishopric-of-brixen 1511 vassal_start | habsburg-monarchy |  | missing | no mirror in habsburg-monarchy (outside this batch) |
| prince-bishopric-of-brixen 1803 dissolve | habsburg-monarchy |  | missing | no mirror in habsburg-monarchy (outside this batch); found/dissolve listed for routing only |
| prince-bishopric-of-passau 1217 found | duchy-of-bavaria | duchy-of-bavaria 1803 gain | mismatch | nearest mirror is gain 1803, 586 years off (outside this batch) |
| prince-bishopric-of-speyer 1644 occupation_start | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| prince-bishopric-of-speyer 1648 loss | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| prince-bishopric-of-speyer 1648 occupation_end | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| prince-bishopric-of-speyer 1679 gain | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| prince-bishopric-of-speyer 1681 loss | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| prince-bishopric-of-speyer 1688 occupation_start | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| prince-bishopric-of-speyer 1697 gain | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| prince-bishopric-of-speyer 1697 occupation_end | kingdom-of-france |  | missing | no mirror in kingdom-of-france (outside this batch) |
| prince-bishopric-of-speyer 1801 loss | french-consulate |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| prince-bishopric-of-verden 1180 found | stem-duchy-of-saxony |  | missing | no mirror in stem-duchy-of-saxony (outside this batch); found/dissolve listed for routing only |
| prince-bishopric-of-minden 1180 found | stem-duchy-of-saxony |  | missing | no mirror in stem-duchy-of-saxony (outside this batch); found/dissolve listed for routing only |
| prince-bishopric-of-minden 1259 gain | unnamed (page silent) |  | exception | the page names no counterpart (unnamed (page silent)) |
| prince-bishopric-of-minden 1277 loss | unnamed (page silent) |  | exception | the page names no counterpart (unnamed (page silent)) |
| prince-bishopric-of-minden 1648 dissolve | brandenburg-prussia |  | missing | no mirror in brandenburg-prussia (outside this batch); found/dissolve listed for routing only |
| principality-of-anhalt 1212 found | stem-duchy-of-saxony |  | missing | no mirror in stem-duchy-of-saxony (outside this batch); found/dissolve listed for routing only |
| county-of-lippe 1190 gain | nobody |  | exception | counterpart 'nobody' |
| county-of-lippe 1332 gain | county-of-schwalenberg |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| county-of-lippe 1401 loss | county-of-tecklenburg |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| county-of-lippe 1405 gain | county-of-sternberg |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| duchy-of-berg 1101 found | duchy-of-lower-lorraine |  | missing | no mirror in duchy-of-lower-lorraine (outside this batch); found/dissolve listed for routing only |
| burgraviate-of-nuremberg 1105 found | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch); found/dissolve listed for routing only |
| free-imperial-city-of-nuremberg 1219 found | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch); found/dissolve listed for routing only |
| free-imperial-city-of-nuremberg 1427 gain | burgraviate-of-nuremberg |  | missing | no mirror in burgraviate-of-nuremberg (in this batch) |
| free-imperial-city-of-nuremberg 1504 gain | unnamed (page silent) |  | exception | the page names no counterpart (unnamed (page silent)) |
| free-imperial-city-of-ulm 1181 found | stem-duchy-of-swabia |  | missing | no mirror in stem-duchy-of-swabia (outside this batch); found/dissolve listed for routing only |
| free-imperial-city-of-ulm 1802 dissolve | duchy-of-bavaria |  | missing | no mirror in duchy-of-bavaria (outside this batch); found/dissolve listed for routing only |
| free-imperial-city-of-cologne 1794 occupation_start | french-first-republic |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| free-imperial-city-of-cologne 1796 occupation_end | french-first-republic |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| county-of-henneberg 1247 gain | margraviate-of-meissen |  | missing | no mirror in margraviate-of-meissen (outside this batch) |
| county-of-henneberg 1248 gain | House of Andechs (no dossier) |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| county-of-henneberg 1347 loss | margraviate-of-meissen |  | missing | no mirror in margraviate-of-meissen (outside this batch) |
| county-of-henneberg 1360 loss | landgraviate-of-hesse |  | missing | no mirror in landgraviate-of-hesse (in this batch) |
| county-of-henneberg 1583 dissolve | electorate-of-saxony |  | missing | no mirror in electorate-of-saxony (outside this batch); found/dissolve listed for routing only |
| county-of-waldeck 1431 vassal_start | landgraviate-of-hesse |  | missing | no mirror in landgraviate-of-hesse (in this batch) |
| county-of-waldeck 1626 gain | county-of-pyrmont |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| county-of-mansfeld 1479 gain | nobody |  | exception | counterpart 'nobody' |
| county-of-mansfeld 1526 gain | nobody |  | exception | counterpart 'nobody' |
| county-of-mansfeld 1580 dissolve | electorate-of-saxony |  | missing | no mirror in electorate-of-saxony (outside this batch); found/dissolve listed for routing only |
| county-of-hoya 1215 gain | nobody |  | exception | counterpart 'nobody' |
| county-of-diepholz 1285 gain | Hermann von Blankena (cousin; no dossier) |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| county-of-diepholz 1291 gain | Vicecomitat of Sudholte (no dossier) |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| county-of-diepholz 1510 vassal_start | duchy-of-brunswick-luneburg | duchy-of-brunswick-luneburg 1584 gain | mismatch | nearest mirror is gain 1584, 74 years off (in this batch) |
| county-of-diepholz 1521 vassal_start | landgraviate-of-hesse |  | missing | no mirror in landgraviate-of-hesse (in this batch) |
| county-of-diepholz 1585 vassal_end | duchy-of-brunswick-luneburg | duchy-of-brunswick-luneburg 1584 gain | mismatch | mirror within a year but of type gain (in this batch) |
| county-of-diepholz 1585 vassal_end | landgraviate-of-hesse |  | missing | no mirror in landgraviate-of-hesse (in this batch) |
| county-of-diepholz 1585 loss | landgraviate-of-hesse |  | missing | no mirror in landgraviate-of-hesse (in this batch) |
| prince-bishopric-of-freising 1294 found | holy-roman-empire-minor-states |  | missing | no mirror in holy-roman-empire-minor-states (outside this batch); found/dissolve listed for routing only |
| prince-bishopric-of-freising 1802 loss | habsburg-monarchy |  | missing | no mirror in habsburg-monarchy (outside this batch) |
| prince-bishopric-of-worms 861 found | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch); found/dissolve listed for routing only |
| prince-bishopric-of-worms 1795 loss | french-first-republic |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| prince-bishopric-of-worms 1802 dissolve | landgraviate-of-hesse-darmstadt |  | missing | no mirror in landgraviate-of-hesse-darmstadt (in this batch); found/dissolve listed for routing only |
| prince-bishopric-of-lubeck 1180 found | stem-duchy-of-saxony |  | missing | no mirror in stem-duchy-of-saxony (outside this batch); found/dissolve listed for routing only |
| county-of-schwerin 1368 dissolve | mecklenburg | mecklenburg 1358 gain | mismatch | page conflict with mecklenburg L4 (1358); keep 1368 here; nearest mirror is gain 1358, 10 years off (in this batch) |
| principality-of-rugen 1168 vassal_start | kingdom-of-denmark |  | missing | kingdom-of-denmark has no dossier and its Cliopatria row ends 1406; the Danish crown is carried by kalmar-union, denmark-norway and kingdom-of-denmark-1814-1940, which treat Schleswig as their own land |
| principality-of-rugen 1235 gain | page silent |  | exception | the page names no counterpart (page silent) |
| principality-of-rugen 1250 loss | duchy-of-pomerania | duchy-of-pomerania 1325 gain | mismatch | nearest mirror is gain 1325, 75 years off (in this batch) |
| principality-of-rugen 1270 gain | page silent |  | exception | the page names no counterpart (page silent) |
| principality-of-rugen 1275 gain | Detlef von Gadebusch line (no dossier) |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| principality-of-rugen 1277 loss | margraviate-of-brandenburg |  | missing | no mirror in margraviate-of-brandenburg (outside this batch) |
| principality-of-rugen 1325 vassal_end | kingdom-of-denmark |  | missing | kingdom-of-denmark has no dossier and its Cliopatria row ends 1406; the Danish crown is carried by kalmar-union, denmark-norway and kingdom-of-denmark-1814-1940, which treat Schleswig as their own land |
| duchy-of-saxe-lauenburg 1296 found | stem-duchy-of-saxony |  | missing | no mirror in stem-duchy-of-saxony (outside this batch); found/dissolve listed for routing only |
| duchy-of-saxe-lauenburg 1420 loss | free-city-of-lubeck |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| duchy-of-saxe-lauenburg 1575 loss | Holstein-Gottorp (no dossier) |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| duchy-of-saxe-lauenburg 1689 loss | imperial custody (Hadeln; no dossier) |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| county-of-oettingen 1147 found | stem-duchy-of-swabia |  | missing | no mirror in stem-duchy-of-swabia (outside this batch); found/dissolve listed for routing only |
| prince-provostry-of-berchtesgaden 1194 found | duchy-of-bavaria |  | missing | no mirror in duchy-of-bavaria (outside this batch); found/dissolve listed for routing only |
| prince-provostry-of-berchtesgaden 1611 occupation_start | prince-archbishopric-of-salzburg |  | missing | no mirror in prince-archbishopric-of-salzburg (outside this batch) |
| prince-provostry-of-berchtesgaden 1611 occupation_end | prince-archbishopric-of-salzburg |  | missing | no mirror in prince-archbishopric-of-salzburg (outside this batch) |
| quedlinburg-abbey 974 gain | page silent |  | exception | the page names no counterpart (page silent) |
| quedlinburg-abbey 1236 loss | page silent |  | exception | the page names no counterpart (page silent) |
| quedlinburg-abbey 1802 dissolve | kingdom-of-prussia |  | missing | no mirror in kingdom-of-prussia (outside this batch); found/dissolve listed for routing only |
| principality-of-hohenzollern-hechingen 1576 found | holy-roman-empire-minor-states |  | missing | no mirror in holy-roman-empire-minor-states (outside this batch); found/dissolve listed for routing only |
| principality-of-hohenzollern-hechingen 1849 occupation_start | kingdom-of-prussia |  | missing | no mirror in kingdom-of-prussia (outside this batch) |
| principality-of-hohenzollern-hechingen 1850 occupation_end | kingdom-of-prussia |  | missing | no mirror in kingdom-of-prussia (outside this batch) |
| principality-of-hohenzollern-hechingen 1850 dissolve | kingdom-of-prussia |  | missing | no mirror in kingdom-of-prussia (outside this batch); found/dissolve listed for routing only |
| duchy-of-schleswig 1058 vassal_start | kingdom-of-denmark |  | missing | kingdom-of-denmark has no dossier and its Cliopatria row ends 1406; the Danish crown is carried by kalmar-union, denmark-norway and kingdom-of-denmark-1814-1940, which treat Schleswig as their own land |
| duchy-of-schleswig 1864 vassal_end | kingdom-of-denmark |  | missing | kingdom-of-denmark has no dossier and its Cliopatria row ends 1406; the Danish crown is carried by kalmar-union, denmark-norway and kingdom-of-denmark-1814-1940, which treat Schleswig as their own land |
| duchy-of-schleswig 1864 occupation_start | kingdom-of-prussia |  | missing | kingdom-of-prussia never names duchy-of-schleswig: its L55 contest_start 1864/2 is against kingdom-of-denmark-1814-1940 and its L57 occupation_start 1864/10 against austrian-empire (joint Austro-Prussian rule from the Treaty of Vienna); no mirror in kingdom-of-prussia (outside this batch) |
| duchy-of-schleswig 1866 occupation_end | kingdom-of-prussia |  | missing | kingdom-of-prussia L63 occupation_end and L64 gain (1866/8) name austrian-empire, not duchy-of-schleswig; no mirror in kingdom-of-prussia (outside this batch) |
| duchy-of-schleswig 1866 dissolve | kingdom-of-prussia |  | missing | no mirror in kingdom-of-prussia (outside this batch); found/dissolve listed for routing only |
| county-of-zutphen 1046 vassal_start | prince-bishopric-of-utrecht |  | missing | no mirror in prince-bishopric-of-utrecht (outside this batch) |
| county-of-zutphen 1138 vassal_end | prince-bishopric-of-utrecht |  | missing | no mirror in prince-bishopric-of-utrecht (outside this batch) |
| county-of-zutphen 1138 dissolve | duchy-of-guelders | duchy-of-guelders 1127 gain | mismatch | the two pages disagree: County of Zutphen page 1138, Duchy of Guelders page 1127; nearest mirror is gain 1127, 11 years off (in this batch) |
| county-of-montbeliard 1042 found | free-county-of-burgundy |  | missing | no mirror in free-county-of-burgundy (outside this batch); found/dissolve listed for routing only |
| principality-of-nassau-orange-fulda 1803 gain | Free Imperial City of Dortmund (no dossier) |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| principality-of-nassau-orange-fulda 1803 gain | Weingarten Abbey (no dossier) |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| principality-of-nassau-orange-fulda 1803 gain | Dietkirchen Abbey (no dossier) |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| principality-of-nassau-orange-fulda 1806 loss | kingdom-of-wurttemberg |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| principality-of-nassau-orange-fulda 1806 loss | duchy-of-nassau |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| duchy-of-saxe-weimar 1602 loss | Saxe-Altenburg (1603-1672; no dossier) |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| duchy-of-saxe-weimar 1638 gain | Saxe-Eisenach and Saxe-Coburg branch (extinct 1638; no dossier) |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| duchy-of-saxe-weimar 1640 loss | Saxe-Eisenach (no dossier) |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| duchy-of-saxe-weimar 1644 gain | Saxe-Eisenach (no dossier) |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| duchy-of-saxe-weimar 1662 loss | Saxe-Eisenach (no dossier) |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| duchy-of-saxe-weimar 1672 loss | Saxe-Jena (no dossier) |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| duchy-of-saxe-weimar 1690 gain | Saxe-Jena (no dossier) |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| duchy-of-saxe-gotha-altenburg 1672 gain | Saxe-Altenburg (no dossier) |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| duchy-of-saxe-gotha-altenburg 1699 gain | Saxe-Coburg (extinct 1699; no dossier) |  | mismatch | stand-in Coburg circle; duchy-of-saxe-coburg-saalfeld gains the same circle in 1735/8 and this dossier never loses it; no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| duchy-of-saxe-gotha-altenburg 1707 gain | Saxe-Eisenberg (no dossier) |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| duchy-of-saxe-gotha-altenburg 1826 loss | Saxe-Hildburghausen (no dossier) |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| duchy-of-saxe-coburg-saalfeld 1735 gain | Saxe-Coburg (extinct 1699; no dossier) |  | mismatch | the same Coburg circle is held by duchy-of-saxe-gotha-altenburg from 1699 (K3, K4) with no 1735 loss, so Coburg is drawn twice 1735-1825; no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| duchy-of-saxe-coburg-saalfeld 1806 occupation_start | first-french-empire |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| duchy-of-saxe-coburg-saalfeld 1807 occupation_end | first-french-empire |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| duchy-of-saxe-coburg-saalfeld 1815 gain | nobody |  | exception | counterpart 'nobody' |
| duchy-of-saxe-coburg-saalfeld 1826 loss | saxe-meiningen |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| duchy-of-saxe-weissenfels 1656 gain | archbishopric-of-magdeburg |  | mismatch | the Magdeburg lordships were Saxony's from 1635 (electorate-of-saxony L16 gains them from archbishopric-of-magdeburg); the 1656 counterpart should be electorate-of-saxony; no mirror in archbishopric-of-magdeburg (outside this batch) |
| duchy-of-saxe-weissenfels 1656 found | electorate-of-saxony | electorate-of-saxony 1656 loss | mismatch | electorate-of-saxony L23 loses 5,817 km2 to 'saxe-weissenfels' in 1656/10; this dossier draws 2,782 km2; electorate-of-saxony's mirror names 'saxe-weissenfels' instead of the slug duchy-of-saxe-weissenfels (outside this batch) |
| duchy-of-saxe-weissenfels 1659 gain | County of Barby (no dossier) |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| duchy-of-saxe-weissenfels 1687 loss | brandenburg-prussia |  | missing | no mirror in brandenburg-prussia (outside this batch) |
| duchy-of-saxe-weissenfels 1746 dissolve | electorate-of-saxony | electorate-of-saxony 1746 gain | mismatch | electorate-of-saxony's mirror names 'saxe-weissenfels' instead of the slug duchy-of-saxe-weissenfels (outside this batch) |
| duchy-of-saxe-merseburg 1657 found | electorate-of-saxony | electorate-of-saxony 1657 loss | mismatch | electorate-of-saxony L24 loses 7,081 km2 to 'saxe-merseburg' in 1657/4; this dossier draws 4,299 km2; electorate-of-saxony's mirror names 'saxe-merseburg' instead of the slug duchy-of-saxe-merseburg (outside this batch) |
| duchy-of-saxe-merseburg 1738 dissolve | electorate-of-saxony | electorate-of-saxony 1738 gain | mismatch | electorate-of-saxony's mirror names 'saxe-merseburg' instead of the slug duchy-of-saxe-merseburg (outside this batch) |
| duchy-of-saxe-zeitz 1657 found | electorate-of-saxony | electorate-of-saxony 1657 loss | mismatch | electorate-of-saxony's mirror names 'saxe-zeitz' instead of the slug duchy-of-saxe-zeitz (outside this batch) |
| duchy-of-saxe-zeitz 1660 gain | county-of-henneberg |  | mismatch | county-of-henneberg ends in 1583 (dissolve to electorate-of-saxony), so it cannot lose land in 1660; electorate-of-saxony L25 gives Schleusingen and Suhl away in 1657, three years before this gain; no mirror in county-of-henneberg (in this batch) |
| duchy-of-saxe-zeitz 1718 dissolve | electorate-of-saxony | electorate-of-saxony 1718 gain | mismatch | electorate-of-saxony's mirror names 'saxe-zeitz' instead of the slug duchy-of-saxe-zeitz (outside this batch) |
| duchy-of-arenberg 1798 occupation_start | french-directory |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| duchy-of-arenberg 1803 occupation_end | french-directory |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| duchy-of-arenberg 1803 loss | french-consulate |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| duchy-of-arenberg 1803 gain | nobody |  | mismatch | prince-bishopric-of-munster L9 (1803/2) loses land to duchy-of-arenberg, but this gain names 'nobody'; the Vest Recklinghausen came from electorate-of-cologne, which has no loss to Arenberg; counterpart 'nobody' |
| duchy-of-arenberg 1810 loss | first-french-empire |  | exception | Cliopatria row with no dossier yet (owned by a group that has not run yet, or by none) |
| county-of-wied 1093 found | holy-roman-empire |  | missing | no mirror in holy-roman-empire (outside this batch); found/dissolve listed for routing only |
| county-of-stolberg 1413 gain | page silent |  | exception | the page names no counterpart (page silent) |
| county-of-stolberg 1417 gain | county-of-hohnstein (no dossier) |  | exception | no dossier yet; listed in the author's counterparts_needing_dossiers |
| county-of-stolberg 1429 gain | County of Wernigerode (no dossier) |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| county-of-stolberg 1535 gain | County of Konigstein (no dossier) |  | missing | Königstein belonged to the Electorate of Mainz by 1581 (Königstein im Taunus page); neither Stolberg nor electorate-of-mainz records the change; no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| county-of-stolberg 1544 gain | County of Rochefort (no dossier) |  | missing | no dossier and not in the author's list; see the reviewer's counterparts_needing_dossiers |
| county-of-stolberg 1806 dissolve | holy-roman-empire-minor-states |  | missing | no mirror in holy-roman-empire-minor-states (outside this batch); found/dissolve listed for routing only |

## Counterparts needing dossiers (reviewer additions)

- Kingdom of Denmark (before the Kalmar Union) (`kingdom-of-denmark`), years [1058, 1406]. Cliopatria row ends 1406 and no dossier exists; duchy-of-schleswig's 1058 fief names it. Needed span shown.
- Free Imperial City of Dortmund (`free-imperial-city-of-dortmund`), years [1803, 1803]. needed at the 1803 hand-over to Nassau-Orange-Fulda; full life not checked on a page
- Weingarten Abbey (`weingarten-abbey`), years [1803, 1803]. needed at 1803; full life not checked
- Dietkirchen Abbey (`dietkirchen-abbey`), years [1803, 1803]. tiny; could instead be named holy-roman-empire-minor-states
- County of Barby (`county-of-barby`), years [1659, 1659]. needed at the 1659 gain by Saxe-Weissenfels
- County of Wernigerode (`county-of-wernigerode`), years [1429, 1429]. inherited by Stolberg 1429
- County of Königstein (Eppstein-Königstein) (`county-of-konigstein`), years [1535, 1535]. inherited by Stolberg 1535; Mainz's by 1581
- County of Rochefort (`county-of-rochefort`), years [1544, 1544]. inherited by Stolberg 1544; the County of Rochefort page would not load
- Duchy of Saxe-Coburg (1680-1699) (`duchy-of-saxe-coburg`), years [1680, 1699]. one of the 1680 shares of Ernest the Pious; its 1699 extinction feeds Gotha-Altenburg and (1735) Coburg-Saalfeld
- Duchy of Saxe-Jena (`duchy-of-saxe-jena`), years [1672, 1690]. 
- Duchy of Saxe-Eisenberg (`duchy-of-saxe-eisenberg`), years [1680, 1707]. 
- Duchy of Saxe-Hildburghausen (`duchy-of-saxe-hildburghausen`), years [1680, 1826]. 
- Duchy of Saxe-Coburg-Eisenach (`duchy-of-saxe-coburg-eisenach`), years [1572, 1638]. the 'Saxe-Eisenach and Saxe-Coburg branch' extinct 1638 in duchy-of-saxe-weimar L2
- County of Hohenzollern (Swabian, before 1576) (`county-of-hohenzollern`), years [1576, 1576]. predecessor of principality-of-hohenzollern-hechingen; holy-roman-empire-minor-states stands in
- Principality of Calenberg (`principality-of-calenberg`), years [1692, 1692]. electorate-of-hanover's 1692 predecessor; duchy-of-brunswick-luneburg's 1692 dissolve should hand only Calenberg-Göttingen to Hanover
- Principality of Salm (1803 share of Münster: Bocholt, Ahaus) (`principality-of-salm`), years [1803, 1810]. 
- County of Rheina-Wolbeck (Looz-Corswarem, 1803 share of Münster) (`county-of-rheina-wolbeck`), years [1803, 1806]. 
- Croÿ share of Münster (Dülmen) (`duchy-of-croy-dulmen`), years [1803, 1806]. 
- Lordship of Werle (`lordship-of-werle`), years [1436, 1436]. named in the mecklenburg notes, not in the author's report; needed at Mecklenburg's 1436 inheritance
- Duchy of Holstein-Gottorp (`duchy-of-holstein-gottorp`), years [1575, 1575]. duchy-of-saxe-lauenburg's 1575 Steinhorst counterpart
- Counts of Andechs-Meran (`county-of-andechs`), years [1165, 1165]. prince-bishopric-of-brixen L2 (1165) and county-of-tyrol
- Landgraviate of Upper Hesse (`landgraviate-of-upper-hesse`), years [1308, 1500]. landgraviate-of-hesse's splits and merges (1311, 1500) name 'Upper Hesse'
- Württemberg-Urach (`wurttemberg-urach`), years [1442, 1482]. duchy-of-wurttemberg L3 split counterpart
- Margraviate of Baden-Baden (`margraviate-of-baden-baden`), years [1535, 1771]. margraviate-of-baden's 1771 merge has no 1535 split

## Gazetteer names needed

311 names do not resolve in the gazetteer (author's list re-tested with place km=10 and region forms, plus the reviewer's additions); the full list is in the report JSON.
