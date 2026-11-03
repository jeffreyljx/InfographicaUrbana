# Review of batch eu-20-g (reviewer, 2026-10-31)

Dossiers: kingdom-of-bavaria, kingdom-of-saxony, kingdom-of-wurttemberg, principality-of-hohenzollern-sigmaringen, principality-of-lippe, principality-of-regensberg. All six validate (`--resolve`: 0 errors; the only warnings are the unwritten slug grand-duchy-of-frankfurt in Bavaria /ledger/12 and Regensberg /ledger/2). Neighbour dossiers read: kingdom-of-prussia, italian-republic, holy-roman-empire-minor-states (Context list), plus the predecessors duchy-of-bavaria, electorate-of-saxony, electorate-of-wurttemberg, county-of-lippe, electorate-of-mainz, electorate-of-salzburg, principality-of-hohenzollern-hechingen. The other Context polities (austrian-empire, grand-duchy-of-wurzburg, first-french-empire, grand-duchy-of-hesse, german-empire...) have no dossier yet: counterparts owned by groups that have not run.

Pages opened (WebFetch): Tyrolean Rebellion; Kingdom of Bavaria; Austro-Prussian War; Treaty of Munich (1816); Grand Duchy of Würzburg; Kingdom of Saxony; Kingdom of Württemberg; Peace of Pressburg (1805); Hohenzollern-Sigmaringen; Province of Hohenzollern; Principality of Lippe; Principality of Regensburg; Grand Duchy of Frankfurt. None failed.

Verdicts: Bavaria thin (3 region fixes applied by the reviewer), Saxony thin, Württemberg thin, Hohenzollern-Sigmaringen FAIL, Lippe pass, Regensberg FAIL.

## kingdom-of-bavaria: thin (reviewer applied 3 fixes)

Spot checks, all confirmed with year: /ledger/0 Augsburg (Pressburg page), /ledger/2 Tyrol handed over 11 Feb 1806 and "The area awarded to Bavaria included Trentino" (Tyrolean page), /ledger/5 Bergisel 1 Nov 1809, /ledger/8 28 Feb 1810 cession, /ledger/10 Treaty of Paris 30 May 1814 (Bavaria infobox), /ledger/11 treaty of 3 June 1814 (Würzburg page), /ledger/13-15 Treaty of Munich 14 April 1816 (bailiwicks only promised: confidence 1 is right), /ledger/18 Bad Orb, Gersfeld, Kaulsdorf (Austro-Prussian War page and Bavaria page). Area: infobox 75,865 km2 (1910) against 72,632 (1870 shape) / 76,433 (1868 shape): ratio 0.96-1.01, acknowledged.

Fixes applied (validated, read back):
1. /ledger/13 (1816 loss to Austria): the region was Salzburg only though the note and the Munich page ("the parts of the Upper Austrian quarters of Hausruckviertel and Innviertel") cede the Innviertel too, so the 1809 Innviertel gain (/ledger/4) was never returned. Now `minus(union(Salzburg, the /ledger/4 disc), Kingdom of Bavaria 1820)` (the minus keeps the 6 core Bavarian cells of the disc and the Rupertiwinkel cell).
2. /ledger/10 (1814 loss of Tyrol and Vorarlberg): the region was all of Tirol + South Tyrol + Vorarlberg, but the gazetteer's "South Tyrol" is Bozen + Trento, and the Trentino/southern Tyrol had gone to Italy and Lienz to Illyria in 1810 (/ledger/8, Tyrolean page). Now `intersect(Kingdom of Bavaria 1811, union(Tirol, South Tyrol, Vorarlberg))` = 58 cells (43 Tirol, 5 Bozen, 10 Vorarlberg).
3. /ledger/8 (1810 loss to Italy): the region "South Tyrol" (Bozen + Trento, 54 cells) included the Brixen cells Bavaria kept to 1814. Now `minus(South Tyrol, Kingdom of Bavaria 1811)` = 49 cells.

For the gap-filler:
- Ansbach: kingdom-of-prussia /ledger/32 has a confidence-3 loss of Ansbach to kingdom-of-bavaria in February 1806; Bavaria has no matching gain (the cells are inside the found region, so the map is right, but the mirror is missing). Add a 1806/2 gain from kingdom-of-prussia (Ansbach is not a gazetteer place: use a disc at about 10.57E 49.30N).
- Lienz and the Hochpustertal to the Illyrian Provinces, 28 Feb 1810: on the Tyrolean Rebellion page the author opened and in the /ledger/8 and /keyframe_review/17 notes, but no ledger event. Add a loss (counterpart Illyrian Provinces, listed under counterparts_needing_dossiers): `minus({admin1: Tirol}, Kingdom of Bavaria 1811)`.
- Losses to Württemberg 1810 (Ulm and the Swabian border): the Bavaria page says Bavaria "from 1810 to 1814 lost territory to Württemberg and Italy"; no event. Page to try: Ulm, or Treaty of Paris (1810).
- Wars: the War of the Fifth Coalition (Austria invaded Bavaria in April 1809) and the War of the Sixth Coalition (Bavaria changed sides in 1813) are missing from `wars`; the Schönbrunn page is already in sources.
- /ledger/15 confidence 1 (the Hesse/Baden bailiwicks): the real transfer year is not on any page.

Cross-dossier (not counted against this dossier): duchy-of-bavaria /ledger/40-41 already gains Tyrol (from habsburg-monarchy) and Augsburg in December 1805; this dossier gains them again in 1806 (/ledger/0, /ledger/2) although both lie inside its own found region of 1806/1. The two authors should keep one date: either the treaty (Dec 1805, in the electorate) or the handover (11 Feb 1806, in the kingdom, with the found region minus Tyrol). Also electorate-of-salzburg /ledger/6 cedes the Eichstätt and Passau parts to kingdom-of-bavaria in December 1805, before this state exists; that counterpart should be duchy-of-bavaria.

## kingdom-of-saxony: thin

Spot checks confirmed: /ledger/1 Cottbus ceded by Prussia at Tilsit 1807; /ledger/2 "Occupied by Prussia: 1813"; /ledger/3 Final Act 9 June 1815, "about 60% of its land"; /ledger/5 Prussia invaded Saxony on 15 June 1866 (Austro-Prussian War page). The Saxony infobox gives no area; the 1820-1870 shape is 18,212 km2. Mirrors with kingdom-of-prussia match for 1807 and 1815.

For the gap-filler: /keyframe_review/2 (the 1809-1810 13-cell dip around Bautzen and Hoyerswerda, kept as the 1807 shape without a page: try War of the Fifth Coalition, Austrian and Brunswick troops in Saxony in June-July 1809); /ledger/4 and /ledger/6 (confidence 1: when the Prussian occupations of 1813-1815 and 1866 ended; try Frederick Augustus I of Saxony and John of Saxony); rulers (try List of rulers of Saxony).

## kingdom-of-wurttemberg: thin

Spot checks confirmed: /ledger/0 Pressburg passes "the scattered Austrian holdings in Swabia" to Württemberg; /ledger/1 King on 1 January 1806; /ledger/2 joined the Confederation and "received further territory with 160,000 inhabitants"; /ledger/3-4 "The Prussians occupied northern Württemberg and negotiated a peace in August 1866" (also on the Austro-Prussian War page: battle of 24 July). Area: 19,508 km2 (1813) against 16,916 km2: ratio 0.87, acknowledged. Mirror with holy-roman-empire-minor-states /ledger/116 matches.

For the gap-filler: /ledger/0 and /ledger/2 carry the same region from two counterparts (the split between Austrian Swabia and the mediatised lands; try Further Austria); the 1810 exchanges (Ulm from Bavaria, cessions to Baden), which the Bavaria page confirms in general terms; the Württemberg page does mention the 1813 treaty at Fulda (confirmation of the acquisitions), contrary to the author's note.

## principality-of-hohenzollern-sigmaringen: FAIL

Spot checks confirmed: /ledger/0 (Confederation 1806-1813), /ledger/1 "Prussian troops arrived in August 1849", /ledger/3 possession of Sigmaringen on 6 April 1850, /ledger/4 province with seat at Sigmaringen. kingdom-of-prussia /ledger/54 mirrors the 1850 loss.

Blocking finding (a shape correction, left to the author): the Cliopatria shape (5 cells) contains the one cell of principality-of-hohenzollern-hechingen (its keyframe `{lon 8.97, lat 48.35, km 10}`, 1576-1849): `intersect(Sigmaringen 1811, Hechingen disc)` = 1 cell. Cliopatria drew both principalities as one; the 1,310 km2 matches the 1,142 km2 of the two principalities together (Province of Hohenzollern infobox, 1939), and the keyframe notes misread this as a grid effect. Fix: /keyframe_review/0 and /1 to `adjust`, and /0, /1, /2 corrections to `minus({cliopatria: "Principality of Hohenzollern-Sigmaringen", year: <y>}, {lon: 8.97, lat: 48.35, km: 10})`, with the notes rewritten (the shape is both Hohenzollern principalities; Hechingen is its own dossier).

## principality-of-lippe: pass

Tried: /ledger/0 (infobox Confederation of the Rhine 1806-1813; text 1807, both noted), /ledger/1 (1871), rulers (Leopold II 1802-1851 with the regency to 1820; Leopold III 1851-1875), the 1866 one-cell drop (the page records only the North German Confederation entry, so keeping the 1820 shape is supported), area 1,215 km2 (1910) against 829 km2 (ratio 0.68, acknowledged), the county-of-lippe hand-over in 1806 (matches). Could not break it within its budget.

## principality-of-regensberg: FAIL

Spot checks confirmed: /ledger/0 created 27 April 1803 (Regensburg infobox); /ledger/1 lost the electoral status in 1806 and joined the Confederation; /ledger/3 ceded 6 January 1810, "formally incorporated the city on 22 May 1810"; /ledger/4. The main finding (Cliopatria's "Principality of Regensberg" and "Grand Duchy of Würzburg" rows carry each other's land) is right: the Regensberg shapes' bbox is 9.27-10.44E, 49.18-50.51N (Würzburg), Regensburg at 12.1E lies outside it.

Blocking finding: Frankfurt is missing 1806-1810. The Grand Duchy of Frankfurt page, the source of /ledger/2: "Frankfurt lost its status as a free imperial city in 1806 ... The city was granted to ... Dalberg", and in 1810 "his remaining territories of Aschaffenburg, Wetzlar, Fulda, Hanau, and Frankfurt were combined". The /ledger/2 note (confidence 3) says Frankfurt is a gain "of the new state, not of this one", which its own page contradicts; the Frankfurt cell is in neither the /keyframe_review/0-1 corrections nor the /ledger/2 region (`intersect(Grand Duchy of Würzburg 1807, Frankfurt 8 km)` = 0 cells). Fix: add a 1806 gain of Frankfurt (counterpart holy-roman-empire-minor-states or the Free City; region `{place: Frankfurt, km: 8}`, 1 cell), add the Frankfurt cell to /keyframe_review/0 and /1 (from 1806; the 1803-1805 keyframe stays without it), add it to the /ledger/2 split region, and correct the /ledger/2 note.

Non-blocking: /keyframe_review/2-3 (1811-1813, after the state's end) give another state's shape as the correction; the text says "this state no longer exists", which the compiler must honour. The Regensburg page says Dalberg "also acquired the newly created Principality of Aschaffenburg", which supports the separate principality-of-aschaffenburg that electorate-of-mainz names as its successor: the author flagged this; the orchestrator should decide where Aschaffenburg lives 1803-1810.

## Cross-dossier summary for routing

Missing on kingdom-of-prussia's side (eu-09): occupations of Saxony 1813-1815 and 1866, of northern Württemberg 1866, of Hohenzollern-Sigmaringen 1849-1850. Missing on holy-roman-empire-minor-states' side: the 1803 loss of the Regensburg territories to principality-of-regensberg. Missing on Bavaria's side: Ansbach 1806 (Prussia /ledger/32). Double transfer: Tyrol and Augsburg in duchy-of-bavaria (Dec 1805) and kingdom-of-bavaria (1806). Wrong-era counterpart: electorate-of-salzburg /ledger/6 names kingdom-of-bavaria for December 1805. Overlap: hohenzollern-sigmaringen and hohenzollern-hechingen claim the same cell 1806-1849.
