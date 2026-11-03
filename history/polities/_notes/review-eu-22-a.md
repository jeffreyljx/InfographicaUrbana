# Review of batch eu-22-a (2026-10-31)

Reviewer: adversarial review per history/briefs/reviewer-brief.md with the orchestrator's adjustments (spot-check budget 4 per dossier, small fixes applied in place). Machine copy: history/notes/phase-b/reviews/eu-22-a.json.

Mechanical: all six dossiers validate with `--resolve`, 0 errors. Warnings are the expected ones: counterparts allied-occupied-germany, saar-protectorate, free-territory-of-trieste (listed for eu-22-x) and Surtsey resolving to no cell.

Spot checks: 24 events and keyframe claims checked on 14 Wikipedia pages; every one is on its page with the stated year. Nothing fabricated or mis-dated.

## Verdicts

| slug | verdict | why |
| --- | --- | --- |
| french-fourth-republic | fail | keyframes 4 and 5 keep 9 German cells (Berlin among them) as French land; K5 drops the Tende circle |
| kingdom-of-greece | pass | 5 events checked; Dodecanese, civil war contest and coup all on the pages |
| people-s-socialist-republic-of-albania | pass | 4 of 4 events checked; area ratio 0.97 |
| republic-of-italy | fix (applied by reviewer) | Istria and Zone B both took the Koper/Piran cells |
| denmark | fix (applied by reviewer) | predecessor slug was denmark-norway (ends 1814) |
| republic-of-iceland | fix (applied by reviewer) | Cod Wars belligerent slug kingdom-of-great-britain (ends 1800) |

## french-fourth-republic (fail, back to the author)

1. `/keyframe_review/4/correction` (1950-55): `minus(shape, Saarland)` leaves 9 cells inside Germany as French land: the French-sector Berlin cell (52.54 N 13.28 E), two Lindau / Lake Constance cells (47.63 N 9.59 E, 47.65 N 9.82 E), two Upper Rhine border cells (47.67 N 7.53 E, 48.06 N 7.59 E) and four cells next to the Saarland (49.42 N 7.27 E, 49.58 N 6.55 E, 49.61 N 6.78 E, 49.64 N 7.01 E). The shapes.csv bbox of the 1950 and 1956 shapes still reaches 13.43 E / 52.59 N. K1-K3 subtract all of Germany; K4 should too. Write: `{"union":[{"minus":[{"cliopatria":"French Fourth Republic","year":1950},{"country":"Germany"}]},{"lon":7.6,"lat":44.08,"km":12}]}`.
2. `/keyframe_review/5/correction` (1956-57): the same 9 cells, and the Tende/La Brigue circle is missing although K2-K4 have it (cell 44.16 N 7.68 E would leave France in 1956 with no event). Write the same spec with year 1956.
3. `/notes` and _notes/eu-22-a.md: "Cliopatria draws one Berlin cell for 1945 only" is wrong: the cell is in all six shapes (resolved for 1945, 1946 and 1950).
4. `/ledger/6/region` (occupation_end 1949): it ends the occupation of the Berlin cell too; the French sector of Berlin stayed occupied to 1990. Take Berlin out of this region so the occupation runs to the end of the dossier (french-fifth-republic carries it on).
Thin (for a gap-filler, not blocking): `/ledger/0` found at confidence 1 (Provisional Government page); 1946 departmentalisation and the missing Reunion; French sector of Berlin dating (West Berlin page).
Checked and confirmed: Saar 16 Feb 1946 and 1 Jan 1957 (Saar (protectorate)); Austrian zone 9 July 1945 and 25 Oct 1955 (Allied-occupied Austria); dissolution 5 Oct 1958 (French Fourth Republic); Tende and La Brigue (Paris Peace Treaties, 1947). Area: infobox 14,200,000 km2 (1946, including colonies) vs 698,587: ratio 0.05, acknowledged in K0.

## kingdom-of-greece (pass)

Checked: Litochoro, 31 March 1946; III Division 70% of the Peloponnese 1948 and its summer-1948 defeat; 30 Aug / 16 Oct 1949 end; Dodecanese 'joined Greece in 1947'; 21 April 1967 coup. Resolve confirms 6 of the 9 Dodecanese cells in the 1945 shape and the 1949 shape equal to the 1945 one. The infobox has no area (checked). Thin, optional: `/ledger/0` found at confidence 1; the Kingdom page dates the return of the government to Athens after the German withdrawal of 12 October 1944, so a 1944.10 start at confidence 3 is available. The contest zones (four northern regions) could be narrowed from the Battle of Grammos-Vitsi page.

## people-s-socialist-republic-of-albania (pass)

Checked: 11 Jan 1946, December 1976 constitution, 29 April 1991, infobox 28,748 km2 (ratio 0.97), Sazan to Albania in 1947 by the Paris treaty. Predecessor albania dissolves 1946.1 naming this slug: matched.

## republic-of-italy (fix, applied by reviewer)

Applied: `/ledger/2/region` was `region: Istria` plus Rijeka and Zadar, which overlapped the Koper and Piran cells that `/ledger/3` gives to the Free Territory (2 cells, 45.45 N 13.54 E and 45.46 N 13.76 E). Istria is now `minus [Istria, Koper+Piran]`; the Free Territory page puts Zone B in 'the north-western part of the Istrian peninsula'. Re-validated: 0 errors.
Checked: 2 June 1946 referendum; Zone A 222.5 / Zone B 515.5 km2, 15 Sep 1947, 5 and 26 Oct 1954; Istria, Fiume, Zara, Pola, Tende, Dodecanese, Trieste on the Paris treaties page; Sazan 1947. Area 301,340 vs 288,839: ratio 0.96. Resolve confirms Trieste (2 cells) missing from the Italian shape and present in Cliopatria's SFRY row (1960). Note: the Tende circle cell 44.16 N 7.68 E stays in every Italian shape after the 1947 loss while French K2-K4 also hold it (a one-cell overlap; a Tende gazetteer entry would settle it).

## denmark (fix, applied by reviewer)

Applied: predecessor and found counterpart `denmark-norway` changed to `kingdom-of-denmark-1814-1940`. denmark-norway.json ends January 1814; kingdom-of-denmark-1814-1940.json ends April 1940 and names `denmark` as successor. Notes updated. Re-validated: 0 errors.
Checked: occupation 9 April 1940, liberation May 1945, infobox 43,094 km2 (ratio 1.24 for 1945, acknowledged; realm 1.03); Greenland 'cut off from Danish control' and 'After the war, Denmark resumed control' (History of Greenland). Thin, within the 1-2 page budget: canada.json lists the Hans Island dispute (1974-2023) with belligerent denmark; Denmark has no war (Hans_Island page). British occupation of the Faroes to September 1945.

## republic-of-iceland (fix, applied by reviewer)

Applied: Cod Wars belligerents `kingdom-of-great-britain` (the 1707-1800 dossier) and free-text "West Germany" changed to `united-kingdom` and `federal-republic-of-germany`. Re-validated: 0 errors.
Checked: plebiscite 20 May 1944, republic 17 June 1944, Surtsey 8 Nov 1963 to 5 June 1968, infobox 103,125 km2 (ratio 1.09). The page says Operation Fork came 'a month later' than the April 1940 invasion of Denmark, so May 1940 is datable if a gap-filler wants the pre-1944 occupation in the predecessor's dossier.

## Cross-dossier matrix

| event | mirror | status |
| --- | --- | --- |
| france 1947 gain Tende from italy | italy 1947.9 loss | matched |
| greece 1947 gain Dodecanese from italy | italy 1947.9 loss | matched |
| albania 1947 gain Sazan from italy | italy 1947 loss | matched |
| italy 1947 loss to socialist-federal-republic-of-yugoslavia | not written (eu-22 part not run) | exception |
| italy 1947 loss / 1954 gain with free-territory-of-trieste | no dossier (eu-22-x) | exception |
| france 1945/1955 occupation in second-republic-of-austria | not written (eu-22 part not run); its row starts 1946, so it must start in 1945 | exception |
| france 1945/1949 occupation in allied-occupied-germany, 1946/1957 vassal saar-protectorate | no dossiers (eu-22-x) | exception |
| iceland 1963 gain Surtsey from nobody | n/a | exception |
| canada war Hans Island dispute (denmark) | none in denmark | mismatch (thin) |
| kingdom-of-italy, albania, kingdom-of-denmark-1814-1940 successors | italy, PSRA, denmark found | matched (denmark after fix) |
