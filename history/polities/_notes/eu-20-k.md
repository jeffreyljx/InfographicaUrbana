# eu-20-k notes (written 2026-10-31)

Six dossiers written, all validate (0 errors). Page budgets: netherlands 9 of 9, kingdom-of-the-two-sicilies 5 of 5, principality-of-andorra 5 of 5, the other three 1 page each. No page failed to load.

## netherlands
- Cliopatria folds the Grand Duchy of Luxembourg (11 grid cells, 29 before 1839 with the Belgian province of Luxembourg) into the Netherlands shapes 1815-1829 and 1840-1916. The dossier takes it out of every shape and draws it as a personal-union tint (counterpart `luxembourg`; vassal_start 1815, vassal_end/vassal_start 1839 at the partition, vassal_end 1890). Cliopatria keeps the cells to 1916 although the union ended in 1890. The Luxembourg dossier (row 1890-2024) should start in 1815, or the Grand Duchy 1815-1890 needs its own dossier; `duchy-of-luxembourg` (1411-1443) is a different state.
- Cliopatria 1830-1833 is the whole Grand Duchy plus the Netherlands (the Dutch claim); 1834-1839 drops Luxembourg and about 5 cells of Dutch Limburg around Maastricht, which the Dutch army held. Corrected in keyframe_review; contest events 1830-1839 for western Luxembourg and Limburg, occupation of the Antwerp citadel 1830-1832, contest of the Ten Days' Campaign (Aug 1831).
- 1940-1944: Cliopatria has no Netherlands shape and its Nazi Germany shapes contain 155 of the Netherlands' 157 cells. The occupation page says Reichskommissariat, not annexed. New keyframe netherlands_1940 (1940-1944) and occupation events with counterpart nazi-germany. The nazi-germany dossier (eu-21) should draw the Netherlands as occupied.
- Not settled: the small area changes 1922/1924/1930/1936 (no page opened explains them; Zuiderzee reclamation is a candidate); a ruler list (not collected; identity.rulers omitted); the Treaty of Maastricht (1843) is only mentioned.
- Counterpart `allied-occupied-germany` (1945-1949, the 1949 annexation of 69 km2) has no dossier.
- Gazetteer lacks Venlo, Elten, Selfkant, Suderwick.

## kingdom-of-the-two-sicilies
- Starts 1815 (Bourbon Restoration, 20 May 1815) to match Cliopatria; 8 December 1816 is a rename. Ends 1861 (Civitella del Tronto 20 March), one year after Cliopatria, with a rump keyframe 1861 (Gaeta, Civitella del Tronto, Messina citadel).
- Cliopatria's `italian-nationalists` row (1848) is Sicily; the revolt lasted to 15 May 1849 but the 1849 shape returns Sicily on 1 January (keyframe 1849 marked adjust, shape unchanged).
- 1860: Cliopatria's shape is the mainland without Sicily and Calabria; the dated ledger carries the steps. The counterpart for 1860 is `kingdom-of-sardinia`; Garibaldi's dictatorship has no row or dossier. Calabria's fall is confidence 1 (the page gives no date).
- Not recorded: the Austrian garrison after 1821 (no page dates its end); the 1820 constitution; Murat's landing in Calabria (1815).
- The Expedition page gives 17 March 1861 for Gaeta and Messina together, which conflicts with 13 February for Gaeta (Gaeta page).
- Gazetteer lacks Gaeta and Civitella del Tronto.

## principality-of-andorra
- One state with `co-principality-of-andorra` (eu-12-b, Cliopatria row 'County of Urgell' 1279-1808, ends 1812), broken by the annexation of 1812-1813. Starts 1814 (page-dated restoration) with a new keyframe; ledger has only the found event (no other change to the footprint). The orchestrator should decide whether to merge the two under one colour.
- Cliopatria's 1938 shape (404 km2) is a raster artefact. The 1933 French occupation and 1936-1940 garrison are not written as occupation events (France is a co-prince; no page dates the end of 1933).

## united-kingdoms-of-sweden-and-norway
- Starts 4 November 1814 (a year before Cliopatria's 1815 shape) with a new keyframe; Cliopatria's Swedish Empire (1814) and Kingdom of Norway (1814) rows overlap it, so the renderer should prefer the union from November 1814. Ends 26 October 1905; Cliopatria's Sweden and Norway rows restart in 1905. The page gives no area.

## free-city-of-frankfurt
- Cliopatria's two shapes (1820-1865) are one cell; the state runs 9 July 1815 to 20 September 1866 (two new keyframes). Predecessor `grand-duchy-of-frankfurt` (1810-13) has no row or dossier. Prussia's Cliopatria row ends 1863, so the 1866 annexation has no matching shape.
- Repair after review (2026-10-31): the reviewer was right that Cliopatria's cell is misplaced. shapes.csv gives bbox 8.2607-8.4306 E, 49.98-50.113 N and centroid 8.346 E 50.046 N; Frankfurt am Main is at 8.68 E 50.11 N (gazetteer 8.675/50.10), about 25 km east of the centroid and outside the box. All four keyframes are now verdict adjust with the correction {place Frankfurt, km 8, country Germany}; identity.successors[0].land uses the same region instead of the cell. I took km 8 (the reviewer allowed 7 or 8) because the ledger already uses 8 and the corrections should agree with it; 8 km is about 200 km2, the same order as the 178 km2 cell. The page (https://en.wikipedia.org/wiki/Free_City_of_Frankfurt, reopened 2026-10-31) still gives no total area, only the forest district (22,123 morgen, 4,480 ha) and the City Forest (almost 40 km2), so the radius is a reading, not a figure.
- Added occupation_start 1866-07 and occupation_end 1866-09 (counterpart kingdom-of-prussia, confidence 3): 'On 16 July 1866 the undefended city was occupied by the Prussian Army under their General Eduard Vogel von Falckenstein'; annexation 'by decree of the King of Prussia on 20 September'. The loss and dissolve events stay.
- Disagreement: none with the reviewer's findings. One extension: the successor land pointed at the same misplaced cell, so I corrected it too.
- Still open for others: kingdom-of-prussia (not my file) gains {cliopatria: Free City of Frankfurt, year 1820} in its ledger, the same misplaced cell; the Prussia owner should use {place Frankfurt} instead. grand-duchy-of-frankfurt still has no dossier.

## principality-of-lichtenberg
- Cliopatria 1820-1827 (179 km2) against the page's 1816-1834 and 537 km2; the cell omits the capital Sankt Wendel. Shape corrected with a 12 km radius around Sankt Wendel; keyframes added for 1816-1819 and 1828-1834. The page does not name the previous holder (counterpart `nobody`). Gazetteer lacks Sankt Wendel.
