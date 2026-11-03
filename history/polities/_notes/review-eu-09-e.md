# Review of batch eu-09-e (2026-10-25)

Reviewer: adversarial review, Phase B. Dossiers: margraviate-of-brandenburg, house-of-luxembourg, house-of-wittelsbach.
Mechanical: `validate_dossier.py --resolve` gives 0 errors for all three. Warnings are only the gazetteer names Altmark, Lower Lusatia and Neumark (19 in Brandenburg) and the counterpart slugs knights-templar and county-of-namur, which have no dossier yet.
Method: town membership was probed on the H3 grid (`tools/grid.py polity_cells`) for each Cliopatria shape. Spot checks were made with WebFetch on the cited pages.

## margraviate-of-brandenburg: FAIL (back to the author; the fixes are narrow)

I could not break the spot checks. Every event I opened says what its note claims: 1261 Soldin (Neumark), 1303 Lower Lusatia (Lower Lusatia), 1316-1317 Dresden and 1319 Zullichau/Schwiebus (Waldemar), 1319 southern Lower Lusatia to Jawor, 1323 grant (Louis IV and Margraviate), 1367 Lower Lusatia sold, 1368 Deutsch Krone ("A year later" after 1367), and 1402 Neumark pawned. The 1272 Neumark gain is honestly at confidence 1 (the Neumark page has no 1272).
Grid probes confirm the author's Cliopatria findings: Stendal and Tangermunde are missing from 1326 on; Deutsch Krone is drawn 1272-1344; Landsberg, Soldin and Kustrin are still drawn in 1402-1414 while Arnswalde and Dramburg are dropped. The Bavarian lump of 1326-1351 is also confirmed.

The cited pages contradict the dossier in three places:
1. **Miedzyrzecz castellany is never lost.** Margraviate page: in February 1322 Henry IV of Zagan "controlled the eastern edge of Lubusz Land, including Torzym and Sulecin, plus the Miedzyrzecz castellany", which "was ultimately reintegrated with Poland". The ledger gains it in 1297 (/ledger/4) and has no loss. The Miedzyrzecz cell is in every Cliopatria outline from 1314 to 1414, and every correction (/keyframe_review/5-13) keeps it.
   Fix: add a loss in 1322 (confidence 2; counterpart the Duchy of Zagan, i.e. the Glogow line, or kingdom-of-poland). Use the /ledger/4 region with the Miedzyrzecz town cell, and subtract it in the corrections from 1322 on.
2. **Northern Lower Lusatia, 1319-1323.** Lower Lusatia page: "In the northern part, in 1319, Gubin was unsuccessfully besieged by King John of Bohemia, and eventually fell to the Dukes of Saxe-Wittenberg"; "In 1324, the northern part passed to the House of Wittelsbach". The dossier keeps northern Lower Lusatia continuously from 1303 to 1367 (/keyframe_review/4 says "for 1319-1325").
   Fix: add a loss in 1319 to house-of-ascania (its dossier is the Ascanian lands with Saxe-Wittenberg 1260-1362) and a gain in 1324 from house-of-ascania, both confidence 2.
3. **/ledger/8 region is mislabelled.** The region is the whole 1314-minus-1305 delta: 10 cells at 14.67-15.54 E, 52.13-52.41 N (Rzepin, Torzym, Sulecin, Miedzyrzecz, and one cell by Schwiebus). It is labelled "Zullichau and Schwiebus". Zullichau (15.63 E, 52.08 N) is in no outline. The Margraviate page treats Torzym Land and Sulecin as Brandenburg's Lubusz Land, taken in the interregnum by Wartislaw IV (1319) and Henry IV of Zagan (1322).
   Fix: give /ledger/8 a circle round Schwiebus and Zullichau (about 15.55 E, 52.17 N, 20 km). Let the 1314 outline stand from 1314 (/keyframe_review/4 note).

Not blocking, but should be fixed while the file is open:
- /ledger/12: the Lower Lusatia page says "From 1364, entire Lower Lusatia was ruled by the Duchy of Jawor-Swidnica", and the Margraviate page says Otto had "already pledged [it] to the Wettin dynasty". Neither is in the note. Keep 1367 (confidence 3 holds for the sale) but say this in the note.
- The 1319-1323 interregnum is mostly absent. The Margraviate page has Wartislaw IV taking "the New March, including Torzym Land and northern Lubusz Land" in 1319, and in 1320 "a large portion of the Lubusz Land" (not "part") passing to Henry I of Jawor. Book them at confidence 2 with the page's names.
- wars[2] belligerent "Mecklenburg" is a name, not a slug; use mecklenburg, as in the counterparts list.

Thin (gap-filler): the Neumark gain of 1272 at confidence 1 (17 West Pomeranian cells by HRE-minor-states' count, not only Greater Poland); the Storkow-Beeskow cells from 1333 on; Upper Lusatia (Bautzen, Gorlitz) and the Land of Stargard, which are in no outline and not in the dossier, though the Waldemar page has Stargard surrendered at Templin in 1317; Pomerelia, Schlawe and Stolp 1307-1317; 1157-1259 not covered by any dossier.

Area: no infobox area. The body says "By 1535, the electorate had an area of some 10,000 square miles (26,000 km2)", against 35.6 k (the 1407 shape, ratio 0.73) and 42.3 k (the Electorate's 1529 shape, ratio 0.61). Both are inside a factor of two, and the author acknowledged it (/keyframe_review/12).
Identity: this is the same state as electorate-of-brandenburg (Q148499). Both dossiers say so and their 1414/1415 ends match. The orchestrator should merge them or give them one colour.

## house-of-luxembourg: FIX (fixed by the reviewer)

Spot checks, all confirmed:
- 1260 and 1264 (Henry V infobox: "Marquis of Namur 1256-1264").
- 1353 (Duchy page: "The ducal lands had been formed in 1353 by integration of the old County of Luxembourg, the Marquisate of Arlon, the counties of Durbuy and Laroche, and the districts of Thionville, Bitburg, and Marville").
- 1354-03 (Wenceslaus I infobox: "13 March 1354").
- 1411 (Duchy page).
- Prény 1266.

Grid: the 1363 enlargement adds Marville, Thionville, Durbuy and cells toward Bitburg, which fits the 1353 list. Namur is only in the 1260 shape.

Applied by the reviewer. The file re-validates: 0 errors, 1 warning (county-of-namur).
- /wars/1/belligerents: county-of-bar -> duchy-of-bar. The dossier exists, 1033-1480, with alt name "County of Bar". The author's counterparts_needing_dossiers entry for the County of Bar should be dropped.
- /notes: the same slug correction.
- /ledger/2/region/text: added "the county of Durbuy". Durbuy is on the Duchy page's 1353 list, in the Wenceslaus I infobox ("Count of Luxembourg, Arlon and Durbuy", 1353-1354) and in the 1363 cells.

Remark: the page says "integration" in 1353, not acquisition. The /ledger/2 gain at confidence 2 is the author's reading that Cliopatria draws these districts 10 years late; acceptable as long as the note says it.
Thin: 1384-1410 (the pledges to Jobst of Moravia and Louis of Orleans are on no page opened); 1059-1259 not covered; the one-cell loss of 1294 is unexplained (small).
Area: no infobox area on any page; the 10.2 k shape matches Cliopatria's Duchy of Luxembourg row (10.3 k).

## house-of-wittelsbach: PASS

Spot checks, all confirmed:
- 1255 partition (Henry XIII: "The brothers divided their land in 1255 against the law").
- 1340 (Louis IV: "With the death of duke John I in 1340 Louis inherited Lower Bavaria and then reunited the duchy of Bavaria").
- Ottokar in August 1257.
- Landshut residence.

The 1340 loss mirrors duchy-of-bavaria /ledger/3. Rulers are contiguous. Landshut is inside the outline.
Observations for a gap-filler: the K1 note's claim that Burghausen lies in the outline does not hold on the grid (the Burghausen cell is outside, at the Salzach edge), and Passau, a prince-bishopric, is inside. Both are soft-certainty precision, not faults. The undated -2% changes of 1272-1294 are thin by design.

## Cross-dossier routing
- margraviate-of-meissen (exists) has no 1303 loss of Lower Lusatia and no 1316-1317 occupation of Dresden. Both are sourced on the Brandenburg side (Lower Lusatia page; Waldemar page).
- holy-roman-empire-minor-states:
  - Its 1294 "gain from house-of-luxembourg" (27 cells) is an overlap artefact: Luxembourg's outline loses one cell in 1294, and the HRE lump overlaps Luxembourg in every year.
  - It has no 1353 loss for Luxembourg's /ledger/2.
  - Its 1272 loss to Brandenburg (17 West Pomeranian cells) disagrees with Brandenburg's 1272 gain from duchy-of-greater-poland (both confidence 1).
- stem-duchy-of-bavaria names its successor "duchy-of-lower-bavaria"; it should be house-of-wittelsbach.
