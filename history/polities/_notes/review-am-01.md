# Review of batch am-01 (Mesoamerica before 900)

Reviewer: Phase B adversarial reviewer, 2026-10-18. Inputs: the author's report (notes/phase-b/reports/am-01.json), the author's notes (_notes/am-01.md), the nine dossiers. The author's brief lists no Context polities, so there were no neighbour dossiers to read. The machine copy of this review is notes/phase-b/reviews/am-01.json.

Mechanical check: `validate_dossier.py --resolve` passes all nine with 0 errors and 0 warnings. Ledgers are sorted, `found` and `dissolve` sit at start and end, capitals and certainty spans cover each life. Shapes were checked by resolving every keyframe on the project grid with `tools/gazetteer.py`, and capitals were tested against those cells. That test found the main faults below.

| slug | verdict | in one line |
| --- | --- | --- |
| teotihuacan | fail | Cliopatria shape is mostly the Puebla–Tlaxcala valley; it excludes the capital and claims Cholula and Cacaxtla; the 200..649 "Valley of Mexico" takes in the Toluca valley (4.2x) |
| olmec-civilization | fix (applied) | San Lorenzo fell about 13 km outside the reused -650 shape; a 20 km circle was added |
| epi-olmec-culture | pass | nothing broken |
| zapotec-civilization | fix (applied) | the 602 shape excluded Monte Albán; the 40 km valley radius was added for 602..900 |
| classic-veracruz-culture | fail | the shapes do not contain El Tajín (about 38 km from the nearest cell), so the "El Tajín polity" identification rests on a misreading |
| cholula | fail | its 25 km circle claims Cacaxtla's capital in 650..749; Postclassic vassal events missing (thin) |
| cacaxtla | pass | consistent; the overlaps are the other two dossiers' to fix |
| xochicalco | fix (applied) | found/dissolve lowered from confidence 3 to 2 (no territory on the page) |
| western-mexico-shaft-tomb-tradition | pass | nothing broken; Teuchitlán tradition gap |

## teotihuacan: fail

1. **/keyframe_review/1, /2, /4, /5: the Cliopatria shape is in the wrong place.** On the grid the shape has 20 cells: 7 in México state, 5 in Tlaxcala and 8 in Puebla. Its centroid (polities.csv -98.51, 19.295) is about 55 km SSE of the city. Only 1 of the 3 cells of the dossier's own 15 km city circle falls inside it. The capital (19.69 N, 98.84 W) is about 11 km outside. Cholula's capital cell (295380) and Cacaxtla's (295354) are inside. The K1 note's "the eastern Basin of Mexico around the city" is therefore wrong. No page opened puts Cholula under Teotihuacan: the Cholula page says "a major center contemporaneous with Teotihuacan", and the Teotihuacan page says that after the fall "Cholula, Xochicalco, and Cacaxtla competed to fill the power void". **Fix:** mark the four keyframes adjust and redraw them around the city, either as `{"place":"Teotihuacan","km":40,"country":"Mexico"}` or as the Cliopatria shape united with the city circle, minus Cholula 25 km and, from 650, minus Cacaxtla 10 km. Bring /ledger/1 and /ledger/5 into line with the new shapes.
2. **/keyframe_review/3, /ledger/2, /ledger/5: "Valley of Mexico" is too broad.** The gazetteer resolves it to all of México state plus the Distrito Federal: 81 cells, about 20,485 km2, west to 100.43 W, with the whole Toluca valley inside. That makes the 200..649 keyframe about 23,770 km2, 4.2 times Cliopatria's shape, with no page giving that extent. The Cuicuilco page sends Cuicuilco's people "towards Toluca and Teotihuacan", which keeps Toluca separate. The note admits the region is too broad and names the substitute but does not use it. **Fix:** use `{"place":"Teotihuacan","km":60,"country":"Mexico"}` (40 cells, about 10,100 km2, no overlap with Cholula or Cacaxtla) with the Cuicuilco page's "the center of the Basin of Mexico".
3. **/keyframe_review/4: no keyframe for 650..655.** K3 ends at 649, K2 covers only 106..199, and K4 (ok) starts at Cliopatria's 656. **Fix:** make K4 adjust with "unchanged shape; years 650..691" (the page says "Period IV describes the time period between 650 and 750 CE").
- Spot checks, all confirmed: L0 (c. 100 BCE), L2 (Cuicuilco abandoned "around AD 150 to 200"), L3 (14 January 378; 13 September 379), L5 (Period IV 650–750), L6 (infobox "Abandoned: 750 CE"). L4 (426) is derived from the 47-year reign, and the note says so.
- Area: the infobox gives 3,381.71 ha for the archaeological zone, which cannot be compared with the state's land; the note says so.
- Thin: L1 (-50, confidence 1); the sphere beyond Tikal has no dated events.

## olmec-civilization: fix, applied by the reviewer

- **/keyframe_review/0 and /ledger/0.** The -1200..-651 keyframe reuses the -650 shape, and its note says San Lorenzo is inside. The capital's cell (17.75 N, 94.76 W) is about 13 km outside. The San Lorenzo page puts the site "in the southeast portion of the Mexican state of Veracruz" and calls it the largest city "from roughly 1200 BCE until 900 BCE". **Applied:** the correction and the found region are now `{"union":[{"cliopatria":"Olmec Civilization","year":-650},{"lon":-94.76,"lat":17.75,"km":20}]}`, with the note extended. Re-validated with 0 errors and 0 warnings; the capital is inside.
- Spot checks, all confirmed on the Olmecs page: c. 1200–400 BC; San Lorenzo abandoned c. 900 BC as La Venta rose; "By about 400 BC the major centres ... had been abandoned".
- The `culture` type after 3400 BCE needs the orchestrator's ruling (the author flagged it).

## epi-olmec-culture: pass

Tried: both events against the page ("Concentrated in the Papaloapan River basin", "from roughly 300 BCE to roughly 250 CE"; "By 250 CE, Cerro de las Mesas, Remojadas ... had eclipsed Tres Zapotes"); Tres Zapotes inside the region; no overlap with the Zapotec shapes; predecessor and successor entries agree with olmec-civilization. Could not break it.

## zapotec-civilization: fix, applied by the reviewer

- **/keyframe_review/5 (and /6, /ledger/3).** Cliopatria's 602 shape was marked ok as "the Valley of Oaxaca again", but it lies east and south of Monte Albán. Only 10 of its 31 cells fall within 40 km of Oaxaca, and the capital's cell is about 17 km outside. The Monte Albán page says the city "lost its political pre-eminence by the end of the Late Classic (c. AD 500–750)" and was "largely abandoned" only "By the end of the same period (c. AD 900–1000)". The ledger's 602 loss already keeps the 40 km Oaxaca radius. **Applied:** K5 is now adjust with `{"union":[{"cliopatria":"Zapotec Civilization","year":602},{"place":"Oaxaca","km":40,"country":"Mexico"}]}`, and the same union with year 892 goes in K6 and the dissolve region. Re-validated with 0 errors and 0 warnings; 39 cells, about 9,860 km2, capital inside.
- Spot checks, all confirmed on the Monte Albán page: founding c. 500 BC on an empty hill; Monte Albán II c. 100 BCE – CE 200, with the Cañada de Cuicatlán, Ejutla and Sola de Vega; pre-eminence lost c. 500–750, so 602 is Cliopatria's year and confidence 1 is honest; abandonment c. 900–1000. The Isthmus and the coast are not on either page, which supports removing Tehuantepec.
- Area: no figure on either page. The Zapotec page's "dominated much of the territory which today is known as the Mexican state of Oaxaca" fits the adjusted -91..601 shape of about 47,300 km2.
- Thin: L2 (602, confidence 1).
- Remark, not a fault: the -100 gain comes 9 years before Cliopatria's -91 expansion and K1 stays ok to -92. That is within a decade.

## classic-veracruz-culture: fail

- **/keyframe_review/0, /1, /2 and /notes.** The dossier calls Cliopatria's row "four shapes centred on El Tajín" and writes it as the El Tajín polity "by its shapes and years". The shapes do not contain El Tajín. The site (infobox 20°26′53″N 97°22′42″W) lies outside the bbox of all four shapes (-97.3534..-96.3824, 19.5719..20.4077) and about 38 km from the nearest cell of the 555 shape. That shape's cells centre on 19.94 N, 96.89 W, the Nautla–Misantla coast. A 40 km circle around El Tajín shares one cell with it. The 705 shape centres on 19.37 N, 96.63 W, the central Veracruz coast. The page's core, "between the Cazones and Tecolutla Rivers", lies north of every shape. **Fix (author's choice):** (a) keep El Tajín and redraw: K0 and K2 as `{"place":"El Tajín","km":40}` with that text, K1 as the circle united with the 705 shape, ledger regions to match; or (b) write the row as the Classic Veracruz culture (type culture, "roughly 100 to 1000 CE"), whose central-Veracruz shapes these are, and add an `el-tajin` slug.
- Spot checks, all confirmed on the El Tajín page: a city by 600; apogee 900–1100; destroyed by fire "early years of the 13th century" with no exact year. L1's extent has no date beyond "From 600 to 1200 CE", so confidence 1 is honest.
- Area: the infobox gives 240 ha for the site, which cannot be compared with the state's land; the note says so.

## cholula: fail

1. **/keyframe_review/0: Cholula's circle claims Cacaxtla's capital in 650..749.** The -300..749 circle (Cholula 25 km) contains cell 295354, Cacaxtla's capital and one of the two cells of its 650..749 core. The Cacaxtla page says "Cacaxtla and Xochitecatl prospered 650–900 CE". The 750..900 keyframe already subtracts Cacaxtla; 650..749 does not. **Fix:** end K0 at 649; add keyframe `cholula_650` for 650..749 = Cholula 25 km minus Cacaxtla 10 km; add a 650 loss (counterpart cacaxtla, confidence 2) and change cacaxtla /ledger/0's counterpart to cholula. Shrinking the circle to 20 km also works.
2. **Overlap with teotihuacan.** Teotihuacan's shapes contain 5 of Cholula's 7 cells; the fix is teotihuacan's fix 1. If a page makes Cholula a Teotihuacan dependency, add vassal events in both dossiers instead.
- Thin: L3 (900 regain, confidence 1). The Postclassic subjection is not in this ledger, though the page has it: "Sometime between 1200 and 1517, Cholula was conquered by the neighboring city-state of Tlaxcala" and "In 1517, Cholula seceded from the Tlaxcala Triple Alliance, opting to join the far more powerful Aztec equivalent". The mirror rule wants vassal events here as well as in the overlords' dossiers (tlaxcala, aztec-triple-alliance; am-03).
- Spot checks, all confirmed: L0 (pyramid 300 BCE); L1 (Olmeca-Xicallanca capital, 700–1200); L2 (Cacaxtla page, Cholula's fall c. 650–750); L4 ("In CE 1200, ethnic Tolteca-Chichimeca conquered Cholula"); L5 (transfer to Spain after the war, no year on the page, as the note says).

## cacaxtla: pass

All three events are confirmed on the Cacaxtla page: prospered 650–900; hegemony after Cholula's fall c. 650–750; ascendancy ended c. 900. Its 750 gain and 900 end mirror cholula. The double claims on its land are teotihuacan's and cholula's to fix. If cholula adds the 650 loss, /ledger/0's counterpart becomes cholula. Thin: no founding date, coordinates or extent on the page; the Xochitécatl page was not opened.

## xochicalco: fix, applied by the reviewer

- **/ledger/0 and /ledger/1 confidence 3 -> 2.** The page dates both events ("founded in about 650 AD by the Olmeca-Xicallanca"; "around 900 CE ... burned and destroyed") but names no territory, and the 30 km radius is the researcher's reading. Re-validated with 0 errors and 0 warnings.
- Thin: no extent. The page's "towns that paid tribute to Xochicalco", carved on the pyramid, could bound it.

## western-mexico-shaft-tomb-tradition: pass

Both events are confirmed ("developed around 300 BCE"; "between 300 BCE and 400 CE", end disputed), and so is the region (Jalisco, Nayarit, "to a lesser extent" Colima, Tequila valleys the core). Thin: the Teuchitlán tradition (300 BCE–900 CE) on the same land has no dossier. The author's URL carried an accent; try https://en.wikipedia.org/wiki/Teuchitlan_tradition.

## Cross-dossier matrix (summary)

- Matched: cholula 750 loss with cacaxtla 750 gain; cholula 900 gain with cacaxtla 900 dissolve (counterpart cholula); olmec-civilization to epi-olmec-culture succession.
- Exceptions:
  - counterpart nobody: teotihuacan -50 and 650, zapotec -100 and 602, classic-veracruz 705 and 1100;
  - Cuicuilco (teotihuacan 200; listed as needing a dossier);
  - mayan-city-states (teotihuacan 378/426; am-02 not yet run);
  - spanish-empire (cholula 1521; not yet run).
- Missing: cholula's own vassal events for Tlaxcala (between 1200 and 1517) and the Aztecs (1517).
- Land mismatches:
  - teotihuacan (-50..704) with cholula (5 of 7 cells, capital included);
  - teotihuacan (650..704) with cacaxtla (whole 10 km core);
  - cholula (650..749) with cacaxtla (capital cell).

## Gazetteer and counterparts

- Gazetteer names needed: a hydrological Basin of Mexico without the Toluca valley; San Lorenzo Tenochtitlán; Valley of Oaxaca; Cañada de Cuicatlán; Isthmus of Tehuantepec; Papantla; Tequila.
- Counterparts needing dossiers: cuicuilco (-150..200), tlaxcala (1200..1521), el-tajin (600..1200, if the row becomes the culture), teuchitlan-tradition (-300..900), zaachila (900..1521), totonacapan (1200..1519).
