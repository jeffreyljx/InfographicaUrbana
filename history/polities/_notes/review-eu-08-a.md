# Review of batch eu-08-a (Kingdom of Germany, Kingdom of Arles)

Reviewer, 2026-10-25. Both dossiers validate with 0 errors (`--resolve`). Warnings: Germany: open vassal_start for duchy-of-bohemia (950) and obotrites (947), both running to the state's end in 962 (fine); unknown place "Brandenburg an der Havel" (gazetteer). Arles: `county-of-provence` has no polity or dossier yet (listed by the author under counterparts_needing_dossiers).

Neighbour dossiers that exist and were cross-checked: west-franks, east-franks, upper-burgundy, lower-burgundy, obotrites (eu-07), kingdom-of-france, house-of-bourbon (eu-10). All other Context polities belong to groups that have not run yet (eu-08-b holy-roman-empire, eu-09, eu-13, eu-14, eu-15, eu-18 and the rest of eu-10).

Neither page set gives an infobox area (Kingdom of Germany has no infobox; East Francia's has no area; Kingdom of Arles has none), so no area ratio could be computed. The author said so.

## kingdom-of-germany: thin

Valid, honest and well sourced; every event I opened says what its note claims. Four confidence-1 events carry the two biggest unexplained moves (947, 960), all within the 5-page budget, so thin by design.

Spot checks (all confirmed):
- /ledger/0 911 found: East Francia, "on 10 November 911 elected one of their own".
- /ledger/2-3 921: Henry the Fowler, Arnulf "in 921 renounced the crown and submitted to Henry".
- /ledger/6 925 gain Lotharingia: Kingdom of Germany, "in 925 Lotharingia was finally ceded to East Francia by Rudolph of West Francia".
- /ledger/8 928: Henry the Fowler, "In the winter of 928 he marched against the Slavic Hevelli tribes and seized their capital, Brandenburg".
- /ledger/10 929 and /ledger/11 934: Henry the Fowler, Wenceslaus forced "to resume the annual payment of tribute" in 929; "also conquered Schleswig in 934".
- /ledger/20-21 950, /ledger/22 951, /ledger/24-25 952, /ledger/26-27 955, /ledger/30 961, /ledger/31 962: Otto I page (Boleslaus war "not concluded until 950"; Pavia 23 September 951; Augsburg 952, Friuli ceded and "reorganized ... into the March of Verona"; Obotrites "invaded Saxony in the fall of 955", Recknitz 16 October; Italy August 961, King of Italy at Christmas; Rome 31 January 962).

Checked and not broken: ledger sorted, found at 911-11 and dissolve at 962-02; keyframe walk (911/922 same, 926 +Lotharingia -Basel strip, 928 and 934 new keyframes, 936 +Billung/Gero marches, 947 +Obotrite and Elbe-Oder cells, 952 +Verona, 960 +Austria/Slovenia, 961 +Italy) is explained event by event; capital Frankfurt (8.68 E, 50.11 N) inside every shape's bbox; rulers 911-918, 919-936, 936-962; certainty covers 911-962.

Thin (for a gap-filler):
1. /ledger/18-19 (947, c1): the Obotrite vassalage and the Elbe-Oder gain are undated. Try https://en.wikipedia.org/wiki/Billung_March and https://en.wikipedia.org/wiki/Marca_Geronis.
2. /ledger/28 (960, c1) and /keyframe_review/0, 1, 5: the 960 growth (Austria 169, Slovenia 58, Carinthia 22 cells) is undated, and Carinthia (Carantania) may have been Bavarian, so German, all through 911-959, in which case the "ok" keyframes 911, 922 and 936 miss it. Try https://en.wikipedia.org/wiki/Duchy_of_Carinthia and https://en.wikipedia.org/wiki/Margraviate_of_Austria.
3. /ledger/12 (936 loss of Hedeby to Denmark, c1): the Mark of Schleswig's end is a Cliopatria bridge; check whether the march outlived 936. Try https://en.wikipedia.org/wiki/Hedeby.
4. Basel 916-926: upper-burgundy has Rudolph II occupying Basel in 916 (from "Duchy of Swabia") and gaining it in 926. Swabia is inside this dossier's shapes, so this dossier should carry occupation_start 916 / occupation_end 926 (counterpart upper-burgundy) before the 926 loss, or the eu-08-x Swabia dossier must. Page: https://en.wikipedia.org/wiki/Rudolph_II_of_Burgundy.

Minor: the 928 Gana (Glomacze) counterpart is not in counterparts_needing_dossiers (added below as optional).

## kingdom-of-arles: thin (reviewer applied three small fixes)

Valid and honest. The main finding (Cliopatria's eleven "Kingdom of Arles" rows 1034..1384 are Duchy of Burgundy land, all marked wrong) is consistent with shapes.csv (bbox 3.60-5.59 E, 46.09-47.99 N, 18-21,000 km2 against 117,000 km2 before) and is flagged in notes. Spot checks all confirmed on the Kingdom of Arles, Rudolph III and County of Provence pages.

Applied by the reviewer (re-validated, 0 errors):
1. /identity/predecessors/0/slug, /ledger/0/counterpart, /ledger/1/counterpart: `kingdom-of-lower-burgundy` -> `lower-burgundy`. eu-07 folded the row "Kingdom of Lower Burgundy" into the lower-burgundy dossier (its cliopatria_names list both Names), so the old slug will never have a dossier.
2. /identity/predecessors/1/slug: `upper-burgundy-and-italy` -> `upper-burgundy`. The upper-burgundy dossier (888-935) lists "Upper Burgundy" and "Upper Burgundy and Italy" and names kingdom-of-arles its successor; the predecessor note said eu-07 had still to decide, and it has.
3. /ledger/4/confidence 3 -> 2: the County of Provence page says the county was "a fiefdom of the Holy Roman Empire, which it remained until 1246", but its own infobox has "Holy Roman Empire (1032-1481)"; the Kingdom of Arles page says only that Charles of Anjou "succeeded in acquiring the County of Provence" and not that it left the kingdom. Note amended.

Not applied (for the author or gap-filler; not blocking while the drawing of the post-1032 shell is undecided):
4. /ledger/4/region, /keyframe_review/14-22/correction, /ledger/9/region: region "Provence" resolves to all of Provence-Alpes-Cote-d'Azur, which takes Hautes-Alpes (also in the gazetteer's Dauphine, removed again in 1349) and Vaucluse (the Comtat Venaissin, Toulouse's marquisate, which the counts of Toulouse "ceded ... in 1274 to Pope Gregory X", County of Provence page) out of the shell in 1246. Use the union of admin1 Bouches-du-Rhone, Var, Alpes-de-Haute-Provence and Alpes-Maritimes for the 1246 county, and add a 1274 loss of the Comtat Venaissin (Vaucluse) to papal-states (source County of Provence).
5. /identity/capitals/0: Arles (4.63 E, 43.68 N) is in Bouches-du-Rhone, which the 1246 loss removes, so the capital lies outside the state for 1246-1384. Either end the capital at 1245 and say there was no seat after, or keep Provence in the nominal shell (infobox: imperial fief to 1481; the 1365 coronation at Arles) and drop the 1246 loss.
6. /identity/rulers: the list stops in 1039 while the life runs to 1384; add the emperor-kings or say in the note why the list stops.

Thin (gap-filler):
- /ledger/9 dissolve 1384 (c1, Cliopatria's last year; the page says "Disestablished: 15th century"). Try https://de.wikipedia.org/wiki/K%C3%B6nigreich_Burgund.
- /wars/1/zones: Odo II's districts 1032-1034 (no zone, no contest). Try https://de.wikipedia.org/wiki/Odo_II._(Blois).
- 1034-1245: 211 years without an event; Free County of Burgundy (Barbarossa 1156, 1178) and the Swiss lands leaving the shell. Try https://en.wikipedia.org/wiki/Free_County_of_Burgundy and https://en.wikipedia.org/wiki/Old_Swiss_Confederacy.

For the orchestrator (author flagged both): the post-1032 shell overlaps Cliopatria's Holy Roman Empire shape (482 of 484 cells to 1259); decide whether to draw it. The 1032 dynasty change is a `rename` per rule 2, so the HRE dossier (eu-08-b) has no event to mirror; it should record Arles as a component kingdom from 1032/1034.

## Cross-dossier matrix

Matched:
- germany 923 contest_start / 925 contest_end / 925 gain from west-franks <-> west-franks 923 / 925 / 925 loss.
- germany 911 found from east-franks <-> east-franks 911-09 dissolve, successor kingdom-of-germany.

Mismatches (route to eu-07):
- **arles 933 found + gain <-> upper-burgundy 933 gain of Lower Burgundy + rename, alive to 935 (c1 end).** Both dossiers hold the united kingdom 933-935 (485 cells drawn twice), and lower-burgundy's 933 loss names upper-burgundy. Arles' 933 start is page-backed ("established in 933"); upper-burgundy's 935 end is a Cliopatria bridge. Recommended: upper-burgundy ends in 933 into kingdom-of-arles (drop its 933 gain and 933-935 keyframe), lower-burgundy's 933 loss names kingdom-of-arles; Arles may then name upper-burgundy as the found counterpart.
- **germany 947 vassal_start obotrites (c1) and 955 contest obotrites (c3) <-> obotrites ends 946** (dissolve, c1, Cliopatria bridge). The Otto I page has the Obotrites invading Saxony in 955, so the obotrites dossier should run past 955 with a 947 vassal_start to kingdom-of-germany and the 955 contest.
- **west-franks 911 gain of Lotharingia from kingdom-of-germany <-> none.** Germany is born (911-11) without Lotharingia; the loss belongs to east-franks (ended 911-09 with no loss). west-franks should name east-franks and east-franks should carry the 911 loss.
- germany 926 loss (Basel strip) to upper-burgundy <-> upper-burgundy 926 gain from "Duchy of Swabia": same year and land, counterpart label differs; also upper-burgundy's 916 occupation of Basel has no mirror (see thin 4 above).

Mismatch (route to eu-10):
- arles 1349 loss of the Dauphine to kingdom-of-france <-> kingdom-of-france 1349 gain from `dauphine`. Same year and land, different counterparts (nominal kingdom vs the Dauphine state); settle with the shell rule.

Missing (route to eu-10):
- arles 1306 loss of the Vivarais and 1312 loss of the Lyonnais to kingdom-of-france: the France ledger has no 1306 or 1312 gain.

Exceptions (counterpart not yet written or listed): germany 928 Hevelli, 928 Gana, 929/936/950 duchy-of-bohemia, 934 scandinavian-minor-kingdoms, 936 kingdom-of-denmark, 936/947 nobody, 951-961 kingdom-of-italy, 960 principality-of-hungary, 962 holy-roman-empire; arles 1006 and 1361 holy-roman-empire, 1246 county-of-provence.
