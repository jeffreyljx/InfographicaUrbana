# Review of batch eu-09-k (brandenburg-prussia, kingdom-of-prussia), 2026-10-25

Reviewer: adversarial review, Phase B. Machine copy: history/notes/phase-b/reviews/eu-09-k.json. Validator: both dossiers 0 errors before and after the reviewer's fixes (brandenburg-prussia: 5 gazetteer warnings, unknown places Halberstadt, Minden, Świebodzin, Princess Town).

## brandenburg-prussia: fix

Area: infobox None (None), Cliopatria 124819.6, ratio None. The Brandenburg-Prussia page has no infobox area (checked); keyframe 1 says so and sums the predecessor rows instead.

### Findings

- APPLIED `/identity/start`: Start had no month although both predecessors end in August 1618, so the realm overlapped them for January-July 1618. Evidence: Margraviate_of_Brandenburg infobox: 'Brandenburg-Prussia: 27 August 1618'; duchy-of-prussia /ledger/1 and electorate-of-brandenburg /ledger/11 are dated 1618-08. Fix: start {year 1618, month 8}; /ledger/0 month 8; Margraviate of Brandenburg added to sources.
- APPLIED `/ledger/11/counterpart`: The 1680 Magdeburg gain names holy-roman-empire-minor-states, but a dossier for the land's holder exists: archbishopric-of-magdeburg ends in 1680 with brandenburg-prussia as successor. Evidence: archbishopric-of-magdeburg /ledger/4: 1680 dissolve, 'secularised by Brandenburg'; Brandenburg-Prussia page: 'the Duchy of Magdeburg (incorporated in 1680)'. Fix: counterpart archbishopric-of-magdeburg (note updated). The report's counterparts_needing_dossiers entry 'duchy-of-magdeburg' is therefore not needed for Magdeburg.
- APPLIED `/ledger/13/month`: Schwiebus gain had no month although the page dates the alliance. Evidence: Brandenburg-Prussia page: the alliance of 22 December 1686, in which Brandenburg-Prussia 'in turn received the Silesian County of Schwiebus'. Fix: month 12.
- APPLIED `/identity/rulers/0`: Rulers began in 1619, leaving 1618-1619 unnamed. Evidence: Margraviate_of_Brandenburg page: 'his son-in-law John Sigismund inherited the Duchy of Prussia' (1618); George William page: inherited in 1619. Fix: Added John Sigismund 1618-1619 with that source; George William's note updated.

### Thin (for a gap-filler)

- `/keyframe_review/4-8, /ledger/1, /ledger/4`: Years and extent of Swedish occupation of Brandenburg 1631-1648 (Cliopatria drops half to nearly all of the Mark in 1632-1635 and 1640-1647); carried as one contest around Frankfurt an der Oder (author flagged, page silent). Page to try: https://en.wikipedia.org/wiki/Swedish_occupation_of_Brandenburg
- `/ledger/8, /wars/4/zones`: Brandenburg's invasion of Swedish Pomerania began in 1675 after Fehrbellin (contest_start is 1677, the siege of Stettin), and the Swedish invasion of the Uckermark and Havelland (December 1674 - June 1675) and of Ducal Prussia (winter 1678-1679) are not in the zones. Page to try: https://en.wikipedia.org/wiki/Scanian_War
- `/wars/1/zones`: Second Northern War zone (East Prussia) has no contest events in the ledger; the Swedish invasion of Ducal Prussia in 1655-1656 and the Polish-Lithuanian raid of 1656 could be dated. Page to try: https://en.wikipedia.org/wiki/Second_Northern_War

### Spot checks

- `/ledger/0` (https://en.wikipedia.org/wiki/Margraviate_of_Brandenburg): confirmed (27 August 1618; month added)
- `/ledger/3` (https://en.wikipedia.org/wiki/Peace_of_Westphalia): confirmed: 'received Farther Pomerania, and the Bishoprics of Magdeburg, Halberstadt, Kammin, and Minden'; signed 24 October 1648
- `/ledger/6` (https://en.wikipedia.org/wiki/Brandenburg-Prussia): confirmed: border fixed at Stettin 1653, Farther Pomerania incorporated 1653
- `/ledger/7` (https://en.wikipedia.org/wiki/Brandenburg-Prussia): confirmed: Bromberg 1657 'gained Lauenburg-Bütow and Draheim'
- `/ledger/9` (https://en.wikipedia.org/wiki/Treaty_of_Saint-Germain-en-Laye_(1679)): confirmed: 29 June 1679, 'former Swedish eastern bank of the Oder river except for Gollnow and Damm'
- `/ledger/10` (https://en.wikipedia.org/wiki/Treaty_of_Saint-Germain-en-Laye_(1679)): confirmed: Stettin restored December 1679
- `/ledger/11` (https://en.wikipedia.org/wiki/Brandenburg-Prussia): confirmed: incorporated 1680 (counterpart corrected)
- `/ledger/12` (https://en.wikipedia.org/wiki/Brandenburg-Prussia): confirmed: company founded 7 March 1682, expedition July 1682
- `/ledger/13` (https://en.wikipedia.org/wiki/Brandenburg-Prussia): confirmed (22 December 1686; month added)
- `/ledger/14` (https://en.wikipedia.org/wiki/Brandenburg-Prussia): confirmed: returned 1694

## kingdom-of-prussia: fail

Area: infobox 348779 (1756), Cliopatria 171637.9, ratio 0.49. Infobox '1756: 348,779 km2' against the 1748-1756 shape; acknowledged in keyframes 1 and 9 (the figure matches Prussia's post-1866 area, 348,607 km2 on the North German Confederation page); Cliopatria's figure is plausible for 1756 and stands.

### Findings

- APPLIED `/ledger/1`: Neuchâtel gain dated 1709 (Cliopatria's year) at confidence 1, though the page dates it. Evidence: Kingdom_of_Prussia infobox status note: 'Associate of the Swiss Confederation (1707–1806, County of Neuchatel only)'. Fix: year 1707, confidence 2, note rewritten; /keyframe_review/3 note updated (gain falls inside the 1706-1708 shape).
- APPLIED `/ledger/36`: Neuchâtel's return dated 1815 at confidence 1, though the infobox dates it 1814. Evidence: Kingdom_of_Prussia infobox: 'Member of the Swiss Confederation (1814–1848; County of Neuchatel 1814–1857)'. Fix: year 1814, confidence 2 (inside the 1814 keyframe).
- APPLIED `/ledger/11`: Russian contest of East Prussia dated 1758 though the note itself cites Gross-Jägersdorf, 30 August 1757, in East Prussia (mis-dated at confidence 2). Evidence: Silesian_Wars: the Russians won 'the Battle of Gross-Jägersdorf on 30 August' 1757 in East Prussia and advanced through East Prussia in 1758. Fix: year 1757, month 8; war zone text updated.
- APPLIED `/ledger/4/month`: Invasion of Silesia had no month; habsburg-monarchy /ledger/68 has 1740-12. Evidence: Silesian_Wars: Frederick 'led Prussian troops across the lightly defended Silesian frontier on 16 December' 1740. Fix: month 12.
- APPLIED `/ledger/44, /ledger/48, /ledger/49, /wars/4/belligerents`: Counterpart denmark-norway is used for 1815 and 1864, but that dossier ends in January 1814 (successor kingdom-of-denmark-1814-1940). Evidence: denmark-norway identity.end 1814-01; kingdom-of-denmark-1814-1940 identity.start 1814-01, predecessor denmark-norway. Fix: counterpart kingdom-of-denmark-1814-1940 in all four places; notes field updated.
- APPLIED `/ledger/48, /ledger/49`: Second Schleswig War contest had no months (author gap) and cited pages that do not date it. Evidence: Second_Schleswig_War: 'The war began on 1 February 1864'; Treaty of Vienna 30 October 1864, 'Denmark ceded Schleswig, Holstein and Lauenburg to Prussia and Austria'. Fix: months 2 and 10, source set to the Second Schleswig War page (added to sources).
- FOR THE AUTHOR `/ledger (after /ledger/0) and a vassal_end`: No vassal_start for the Gold Coast colony in 1701 and no vassal_end: brandenburg-prussia /ledger/15 ends its relation on 15 January 1701 saying 'The relation continues as a colony of the Kingdom of Prussia', but this dossier never takes it up, so the colony is nobody's dependency 1701-1721. Evidence: Brandenburger_Gold_Coast (a source of the sister dossier): renamed Prussian Gold Coast Settlements 15 January 1701, abandoned 1717, sold to the Dutch in 1721; brandenburger-gold-coast /ledger/4, /ledger/7, /ledger/9. Fix: Add vassal_start 1701-01 counterpart brandenburger-gold-coast (region as brandenburg-prussia /ledger/12) and vassal_end 1721 (sale; or 1717, abandonment, with the reason in note); add the page to sources.
- FOR THE AUTHOR `/ledger (1801)`: Missing occupation of Hanover, April to October 1801, which electorate-of-hanover records with this state as occupier. Evidence: electorate-of-hanover /ledger/11-12 (c3): 'In 1801, there was an invasion of 24,000 Prussian soldiers that surprised Hanover', they stayed from April 'until October' (Electorate of Hanover page). Fix: Add occupation_start 1801-04 and occupation_end 1801-10, counterpart electorate-of-hanover, region the Electorate of Hanover (Cliopatria Electorate of Hanover 1801 shape), source https://en.wikipedia.org/wiki/Electorate_of_Hanover.
- FOR THE AUTHOR `/keyframe_review/32/note; /ledger (1864-10 to 1865-08)`: The 1864-1865 keyframe says Schleswig, Holstein and Lauenburg 'are carried by the occupation events', but no event covers them between the Treaty of Vienna (30 October 1864) and the Gastein Convention (14 August 1865), and Lauenburg (personal union from 1865) is carried by no event at all; kingdom-of-denmark-1814-1940 /ledger/8-9 gives them up on 30 October 1864, so the duchies are unpainted for ten months. Evidence: Second_Schleswig_War: 'Denmark ceded Schleswig, Holstein and Lauenburg to Prussia and Austria' (30 October 1864); Kingdom_of_Prussia: Prussia 'effectively annexed Saxe-Lauenburg' by a personal union. Fix: Add an event at 1864-10 carrying the joint Austro-Prussian holding of Schleswig, Holstein and Lauenburg (e.g. occupation_start counterpart austrian-empire, ended 1865-08 when /ledger/50 begins), and a Lauenburg event from the Gastein Convention (1865-08) to 1867; or say in the keyframe note that the duchies are left to another dossier and name it.
- FOR THE AUTHOR `/keyframe_review/21, /keyframe_review/22`: Cliopatria's 1803 and 1805 shapes lack Neuchâtel (shapes.csv bbox south edge 48.92 N and 49.05 N, against 46.87 N for the 1709-1802 shapes), but both keyframes are 'ok' while the ledger keeps Neuchâtel Prussian until /ledger/27 (February 1806). Evidence: shapes.csv bboxes; Treaty_of_Schönbrunn_(1805): Prussia 'had to cede Ansbach, the Duchy of Cleves and the Principality of Neuchâtel' (15 December 1805), so it held Neuchâtel in 1803-1805. Fix: Verdict adjust on both, correction {union: [the shape, {admin1: Neuchâtel, country: Switzerland}]} with text.

### Thin (for a gap-filler)

- `/ledger/2`: The 1713 Lower Rhine cells (confidence 1, counterpart a guess): Prussian Upper Guelders came from the Spanish Netherlands at Utrecht (dutch-republic /ledger/37 takes the Venlo share from habsburg-netherlands), Moers and Lingen from the Orange inheritance of 1702. Page to try: https://en.wikipedia.org/wiki/Upper_Guelders
- `/ledger/20`: The 1803 compensation lands (confidence 1): holy-roman-empire-minor-states /ledger/111 has them at confidence 3 (Hildesheim, Münster, Paderborn, Essen, Herford, Quedlinburg) from German_mediatisation. Page to try: https://en.wikipedia.org/wiki/German_mediatisation
- `/keyframe_review/18-22`: Prussia's left-bank Rhine lands (Cleves west of the Rhine, Moers, Upper Guelders) were occupied by France in 1794 and ceded in the secret articles of Basel (April 1795); Cliopatria's 1794-1805 shapes still reach 6.02 E and no event removes them (holy-roman-empire-minor-states /ledger/102 notes 'Prussia's left-bank lands go at Basel'). Page to try: https://en.wikipedia.org/wiki/Peace_of_Basel
- `/keyframe_review/4, /ledger/3, /wars`: Great Northern War (Prussia 1715-1720) missing from wars; Cliopatria's 1713 Swedish Pomerania cells match the 1713 sequestration of Stettin, which could be an occupation 1713-1720 instead of nothing. Page to try: https://en.wikipedia.org/wiki/Swedish_Pomerania
- `/wars/2/zones`: Third Silesian War zones omit Bohemia (Prussian invasion 1757; habsburg-monarchy /ledger/78-79 moves 19 Bohemian cells in 1757-1763), Silesia (Breslau 1757, Glatz 1760-1763), the Swedish front in Pomerania 1757-1762 and the French occupation of Cleves and Wesel 1757-1762 (holy-roman-empire-minor-states /ledger/97: 'evacuated Prussia's Rhineland territories'). Page to try: https://en.wikipedia.org/wiki/Seven_Years%27_War
- `/wars`: War of the First Coalition (1792-1795), the Wars of the Sixth and Seventh Coalitions (1813-1815, the reoccupation of Prussia's west, keyframe 26 unverified) and the First Schleswig War (1848-1851) are not listed. Page to try: https://en.wikipedia.org/wiki/War_of_the_Sixth_Coalition
- `/keyframe_review/33`: The 1866 cessions of Hesse-Homburg (from Hesse-Darmstadt) and of Orb, Gersfeld and Kaulsdorf (from Bavaria), named on the Austro-Prussian War page, are not drawn. Page to try: https://en.wikipedia.org/wiki/Austro-Prussian_War

### Spot checks

- `/ledger/1` (https://en.wikipedia.org/wiki/Kingdom_of_Prussia): mis-dated (1707 in the infobox note, not 1709); fixed
- `/ledger/4` (https://en.wikipedia.org/wiki/Silesian_Wars): confirmed (16 December 1740; month added)
- `/ledger/6` (https://en.wikipedia.org/wiki/Silesian_Wars): confirmed: Breslau 11 June 1742, most of Silesia and Glatz, about 35,000 km2
- `/ledger/8` (https://en.wikipedia.org/wiki/Silesian_Wars): confirmed: Bohemia 15 August - November 1744
- `/ledger/10` (https://en.wikipedia.org/wiki/Silesian_Wars): confirmed: Saxony invaded 29 August 1756, occupied late 1756
- `/ledger/11` (https://en.wikipedia.org/wiki/Silesian_Wars): mis-dated (1757, Gross-Jägersdorf); fixed
- `/ledger/13` (https://en.wikipedia.org/wiki/Silesian_Wars): confirmed: Treaty of Saint Petersburg 5 May 1762
- `/ledger/16` (https://en.wikipedia.org/wiki/Partitions_of_Poland): confirmed: 36,300 km2, Royal Prussia except Gdańsk, Warmia, Netze District, part of Kuyavia; ratified 22 September 1772
- `/ledger/18` (https://en.wikipedia.org/wiki/Partitions_of_Poland): confirmed: 23 January 1793, 57,100 km2, South Prussia
- `/ledger/19` (https://en.wikipedia.org/wiki/Partitions_of_Poland): confirmed: 24 October 1795, 48,000 / 55,000 km2
- `/ledger/21` (https://en.wikipedia.org/wiki/Treaty_of_Sch%C3%B6nbrunn_(1805)): confirmed: Prussia had occupied Hanover after the French crossed Ansbach in September 1805 (no month)
- `/ledger/24-27` (https://en.wikipedia.org/wiki/Treaty_of_Sch%C3%B6nbrunn_(1805)): confirmed: 15 December 1805, Treaty of Paris 15 February 1806; Ansbach, Cleves, Neuchâtel ceded
- `/ledger/30-34` (https://en.wikipedia.org/wiki/Treaties_of_Tilsit): confirmed: 9 July 1807; Duchy of Warsaw, Westphalia, Białystok, Cottbus, Danzig; 5,700 to 2,800 square miles
- `/ledger/38-45` (https://en.wikipedia.org/wiki/Congress_of_Vienna): confirmed: three-fifths of Saxony, Swedish Pomerania sold to Prussia after Denmark received it in 1814, Lower Rhine, Duchy of Westphalia from Hesse-Darmstadt, Berg, East Frisia to Hanover; Final Act 9 June 1815
- `/ledger/47` (https://en.wikipedia.org/wiki/Kingdom_of_Prussia): confirmed: Hohenzollern principalities 'annexed by Prussia in 1850'
- `/ledger/48-49` (https://en.wikipedia.org/wiki/Second_Schleswig_War): confirmed (1 February and 30 October 1864; months added)
- `/ledger/52-56` (https://en.wikipedia.org/wiki/Austro-Prussian_War): confirmed: Peace of Prague 23 August 1866; Hanover, Schleswig-Holstein, Hesse-Kassel, Nassau, Frankfurt annexed

## brandenburg-prussia: what I tried and could not break

Every gain names a counterpart with a mirror or an explained exception; the 1648, 1653, 1657, 1679, 1680, 1686 and 1694 events read as the pages say; the Thirty Years' War keyframes are honestly marked adjust with the gap named; the 1702-1717 overlap and the Ghana-only 1718 shape are handled; the Polish and Swedish fiefs over Ducal Prussia (1618-1657) belong in the overlords' ledgers under the schema and are routed to eu-15 and eu-14.

## kingdom-of-prussia: why it goes back

Four findings need the author: the Gold Coast relation dropped between the two dossiers of this batch, the 1801 occupation of Hanover that the electorate-of-hanover dossier records, the ten months in 1864-1865 when the ceded duchies belong to nobody although keyframe 32 says the events carry them (and Lauenburg throughout), and Neuchâtel missing from the 1803 and 1805 shapes while the ledger holds it. The rest of the ledger is sound: every confidence-3 event I opened (17 spot checks) reads as the note says.

## Cross-dossier matrix

- brandenburg-prussia 1618 found duchy-of-prussia <-> duchy-of-prussia 1618 merge: **matched**. Also electorate-of-brandenburg /ledger/11 dissolve 1618-08; start month now 8.
- brandenburg-prussia 1631 contest_start swedish-empire <-> -: **exception**. swedish-empire (eu-14) not written yet; also 1648 contest_start, 1653 contest_end and gain, 1677 contest_start, 1679 gain and contest_end.
- brandenburg-prussia 1648 gain holy-roman-empire-minor-states <-> holy-roman-empire-minor-states 1648 loss: **matched**. HRE minor states /ledger/67 (1648-10).
- brandenburg-prussia 1657 gain polish-lithuanian-commonwealth <-> -: **exception**. polish-lithuanian-commonwealth (eu-15) not written yet. Route to eu-15: the overlord should also carry vassal_start 1618 / vassal_end 1657 for Ducal Prussia (counterpart brandenburg-prussia; Brandenburg-Prussia page: 'held as a fief under the Polish Crown until 1656/7', Bromberg 'freed the electors of Polish vassalage'), and eu-14 the Swedish fief of January-November 1656 (Königsberg to Labiau). Per the schema the overlord records these, so brandenburg-prussia is not at fault.
- brandenburg-prussia 1680 gain archbishopric-of-magdeburg <-> archbishopric-of-magdeburg 1680 dissolve: **matched**. Counterpart corrected by the reviewer. holy-roman-empire-minor-states /ledger/78 also has a 1683 loss of Magdeburg to brandenburg-prussia (confidence 1, Cliopatria's year): mismatch on the HRE side, should be dropped or moved to 1680.
- brandenburg-prussia 1682 vassal_start brandenburger-gold-coast <-> brandenburger-gold-coast 1682 found: **exception**. The colony dossier has found 1682-05 with predecessor brandenburg-prussia and no vassal events of its own; the relation is carried on the overlord's side, as the schema says.
- brandenburg-prussia 1686 gain habsburg-monarchy <-> -: **missing**. habsburg-monarchy has no 1686 loss nor 1694 gain of Schwiebus (Brandenburg-Prussia page: received after the alliance of 22 December 1686, returned 1694). Route to the habsburg-monarchy author (eu-09).
- brandenburg-prussia 1694 loss habsburg-monarchy <-> -: **missing**. See the 1686 entry.
- brandenburg-prussia 1701 vassal_end brandenburger-gold-coast <-> kingdom-of-prussia None vassal_start: **missing**. The note says the relation continues under the Kingdom of Prussia, which has no vassal_start: fix listed on kingdom-of-prussia.
- dutch-gold-coast 1687 gain brandenburg-prussia <-> brandenburger-gold-coast 1687 loss: **mismatch**. dutch-gold-coast /ledger/16, 18, 19, 20, 21 (1687, 1698, 1711, 1712, 1721) name brandenburg-prussia, but brandenburg-prussia draws no Ghana cells (they are brandenburger-gold-coast's) and 1711-1721 are outside its life. Route to af-04: counterpart brandenburger-gold-coast.
- kingdom-of-prussia 1701 found brandenburg-prussia <-> brandenburg-prussia 1701 dissolve: **matched**. 
- kingdom-of-prussia 1707 gain Principality of Neuchâtel <-> -: **exception**. No dossier; listed as counterpart needing a dossier.
- kingdom-of-prussia 1713 gain holy-roman-empire-minor-states <-> -: **missing**. holy-roman-empire-minor-states has no 1713 loss to Prussia; the land (Upper Guelders) was Spanish: likely counterpart habsburg-netherlands (dutch-republic /ledger/37). Confidence 1, listed as thin.
- kingdom-of-prussia 1720 gain swedish-empire <-> -: **exception**. swedish-empire (eu-14) not written yet.
- kingdom-of-prussia 1740 contest_start habsburg-monarchy <-> habsburg-monarchy 1740 contest_start: **matched**. Both 1740-12 now.
- kingdom-of-prussia 1742 gain habsburg-monarchy <-> habsburg-monarchy 1742 loss: **matched**. 1742-06 both sides; contest_end matched too.
- kingdom-of-prussia 1744 gain holy-roman-empire-minor-states <-> -: **missing**. East Frisia 1744: holy-roman-empire-minor-states has no 1744 loss to kingdom-of-prussia. Route to the HRE minor states author, or to a county-of-east-frisia dossier.
- kingdom-of-prussia 1744 contest_start habsburg-monarchy <-> habsburg-monarchy 1744 loss: **mismatch**. habsburg-monarchy /ledger/75 records a confidence-1 loss of Bohemian cells to kingdom-of-prussia in 1744 with no return; Prussia held Bohemia only 15 August - November 1744 (Silesian Wars page): should be a contest on the Habsburg side.
- habsburg-monarchy 1757 loss kingdom-of-prussia <-> kingdom-of-prussia None None: **missing**. habsburg-monarchy /ledger/78-79 move 19 Bohemian cells to and from Prussia in 1757-1763 (confidence 1); kingdom-of-prussia has no 1757 Bohemian event (thin item there).
- kingdom-of-prussia 1756 occupation_start electorate-of-saxony <-> electorate-of-saxony 1756 occupation_start: **matched**. End 1763 matched (Saxony 1763-02).
- kingdom-of-prussia 1757 contest_start russian-empire <-> -: **exception**. russian-empire (eu-17) not written; also 1761 contest_start and 1762 contest_end; 1807 loss of Białystok.
- kingdom-of-prussia 1772 gain polish-lithuanian-commonwealth <-> -: **exception**. eu-15 not written; also 1793 and 1795.
- kingdom-of-prussia 1791 gain holy-roman-empire-minor-states <-> holy-roman-empire-minor-states 1791 loss: **matched**. 
- holy-roman-empire-minor-states 1794 loss french-first-republic <-> kingdom-of-prussia None loss: **missing**. The HRE note says Prussia's left-bank lands go at Basel in 1795; kingdom-of-prussia has no loss to french-first-republic (thin item).
- electorate-of-hanover 1801 occupation_start kingdom-of-prussia <-> kingdom-of-prussia None occupation_start: **missing**. electorate-of-hanover /ledger/11-12 (April-October 1801, confidence 3); fix listed on kingdom-of-prussia.
- kingdom-of-prussia 1803 gain holy-roman-empire-minor-states <-> holy-roman-empire-minor-states 1803 loss: **matched**. HRE side at confidence 3 (German_mediatisation); the Prussian side can be raised from 1.
- kingdom-of-prussia 1805 occupation_start kingdom-of-hanover <-> -: **exception**. kingdom-of-hanover (eu-20) not written; electorate-of-hanover ends 1802 with that successor. Also 1806 occupation_end and gain, 1815 loss of East Frisia, 1866 gain.
- holy-roman-empire-minor-states 1806 loss kingdom-of-prussia <-> kingdom-of-prussia 1806 gain: **mismatch**. HRE /ledger/121 passes 18 Lower Saxon cells to Prussia in 1806 (confidence 1, Cliopatria re-cut); kingdom-of-prussia takes Hanover from kingdom-of-hanover, not from the HRE lump. Orchestrator to decide which row owns those cells.
- kingdom-of-prussia 1806 loss kingdom-of-bavaria <-> -: **exception**. eu-20 not written; also grand-duchy-of-berg (1806, 1815), Principality of Neuchâtel (1806), first-french-empire (1806-1807, 1815), duchy-of-warsaw, kingdom-of-westphalia, kingdom-of-saxony, free-city-of-danzig (1807, 1815), grand-duchy-of-hesse (1815), principality-of-hohenzollern-sigmaringen (1850), austrian-empire (1865-1866), electorate-of-hesse, duchy-of-nassau, free-city-of-frankfurt (1866), north-german-confederation (1867).
- kingdom-of-prussia 1814 gain Principality of Neuchâtel <-> swiss-confederation 1815 gain: **mismatch**. swiss-confederation /ledger/44 takes Neuchâtel from kingdom-of-prussia in 1815, while kingdom-of-prussia keeps it to /ledger/46 (1848, loss to swiss-confederation): both paint Neuchâtel 1815-1848 (dual status: Prussian principality and Swiss canton). Orchestrator to pick one owner.
- kingdom-of-prussia 1815 gain kingdom-of-denmark-1814-1940 <-> -: **mismatch**. Swedish Pomerania: the Congress of Vienna page has Denmark receive it in 1814 and sell it to Prussia, but kingdom-of-denmark-1814-1940 never draws it (Sweden held it until the 1815 handover); its own /ledger/1 is a 1815 gain of Lauenburg from kingdom-of-prussia that has no Prussian loss (Congress page: Lauenburg went from Hanover to Denmark). Route to eu-14: the Swedish side should carry the 1815 loss to kingdom-of-prussia; the Danish Lauenburg counterpart should be kingdom-of-hanover.
- kingdom-of-prussia 1864 contest_start kingdom-of-denmark-1814-1940 <-> kingdom-of-denmark-1814-1940 1864 contest_start: **mismatch**. Dates agree (1864-02, 1864-10) but the Danish dossier names german-confederation (and austrian-empire) as counterpart, while kingdom-of-prussia treats the Confederation as an association; its 1864-10 losses go to german-confederation. Route to eu-14/eu-20: name kingdom-of-prussia and austrian-empire.

## Problems

- kingdom-of-prussia ends 1 July 1867 by a merge into north-german-confederation, though the page dates the kingdom 1701-1918; the author flags it. Orchestrator decision: if federal members (Prussia, Bavaria, Saxony) are to stay coloured inside the North German Confederation and the German Empire, extend the end to 1918 and make those rows umbrellas.
- kingdom-of-prussia uses German Confederation shapes (1820-1863) as Prussia's own land; the eu-20 german-confederation dossier must be an umbrella or the cells are painted twice (author flags it).
- The author's counterparts_needing_dossiers entry duchy-of-magdeburg is not needed for 1680: archbishopric-of-magdeburg exists and dissolves into brandenburg-prussia (reviewer changed the counterpart).
- Reviewer fixes applied in place to both dossiers; both re-validate with 0 errors (brandenburg-prussia keeps its 5 gazetteer warnings). Pages opened by the reviewer: Brandenburg-Prussia, Peace_of_Westphalia, Treaty_of_Saint-Germain-en-Laye_(1679), Margraviate_of_Brandenburg, Kingdom_of_Prussia, Silesian_Wars, Partitions_of_Poland, Treaties_of_Tilsit, Congress_of_Vienna, Austro-Prussian_War, Treaty_of_Schönbrunn_(1805), Second_Schleswig_War; none failed to load.
