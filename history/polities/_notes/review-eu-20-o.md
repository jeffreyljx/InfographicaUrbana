# Review of batch eu-20-o (2026-10-31)

Dossier: portuguese-republic (Cliopatria "Portuguese Republic", 1911..1925, 7 shapes; page budget 5). Verdict: **thin** (reviewer fixes applied; one large confidence-1 step left for a gap-filler).

## Mechanical
- validate_dossier.py --resolve: 0 errors, 0 warnings, before and after the reviewer's edits.
- File name = slug; cliopatria_names matches polities.csv; all 7 Cliopatria shapes reviewed; new keyframes 1910 and 1926 carry from/to/correction. Ledger sorted; found 1910-10, dissolve 1926-05; contest and occupation pairs in order. Lisbon inside the shapes' bbox.
- data/README.md issue (Estado Novo 1926..2024 / Portuguese Republic only to 1925) is flagged by the author (1926 keyframe and hand-over note).

## Spot checks (pages opened by the reviewer)
- /ledger/0, /ledger/11 (First Portuguese Republic): "Established 5 October 1910", "Disestablished 29 May 1926", "on 28 May 1926 the Portuguese Revolution of 1926 took place". Confirmed. Infobox has no area. President list confirmed (seven names, Machado twice).
- /ledger/2 (Portuguese Angola): "The Germans returned in December and captured Naulila, forcing the Portuguese to withdraw from the Humbe region." Confirmed; the page does not say who held Humbe afterwards.
- /ledger/3 (campaigns page): "On 7 July 1915, Portuguese forces reoccupied Humbe". Date confirmed; confidence lowered 3 -> 2 (region is a Cunene proxy; no page says Germans held Humbe). APPLIED.
- /ledger/5: "On 4 September, Pereira d'Eca occupied Ondjiva, capital of the Cuanhama kingdom" (1915 by context). Confirmed.
- /ledger/6: "Portugal occupied the Kionga Triangle on 10 April 1916." Confirmed.
- /ledger/7, /ledger/8 (East African campaign): "on 23 November, Lettow-Vorbeck crossed into Mozambique" (lead: November 1917), "nine months", "returned to German East Africa and crossed into Rhodesia in August 1918". Confirmed.
- /ledger/9, /ledger/10: Portuguese Mozambique page: "on 28 June 1919, the Treaty of Versailles transferred the Kionga Triangle, a 1,000 km2 (390 sq mi) territory south of the Rovuma River from German East Africa to Mozambique". Month 6 added, source changed to that page (added to sources[]), gain confidence 1 -> 3, occupation_end 1 -> 2; Kionga war outcome updated. APPLIED. (The Kionga Triangle page itself gives only "April 1916" and no treaty date.)

## Identity
- portuguese-empire (Cliopatria "Portuguese Empire" + "Portuguese Colonies") dissolves in 1910 naming portuguese-republic as successor with the Colonies' 1910 shape; Cliopatria's Portuguese Colonies 1908-1910 shape (24,277 km2, 72.9-127.2 E) is the Goa+Timor land the Republic's 1911 shape adds (+23,661 km2 over the Kingdom's 1908 shape). Added portuguese-empire to identity.predecessors. APPLIED.
- Rulers start in 1911: the 1910-1911 provisional government is missing (author flagged). Thin.

## Area
- Infobox of First Portuguese Republic: no area. Portuguese Angola page: 1,246,700 km2 (undated); Portuguese Mozambique page: 801,590 km2. Cliopatria total 1.965 M (1911-13) and 2.202 M km2 (1914-25); no factor-of-two gap. The author's Angola comparison (ratio 0.72 for 1911-13) is in the keyframe note.

## Thin (for a gap-filler)
- /ledger/1 (1914 gain from nobody, confidence 1, +236,000 km2 in Cuando Cubango and east Moxico, the largest land move in the dossier). Lead the author missed on a page already opened: the campaigns page says Joao de Almeida, governor of Huila from 1909, "also established forts in Cuangar, Dirico and Mucusso by the border with German Southwest Africa" (1909 context). The Okavango line was thus garrisoned under the Kingdom; Cliopatria's 1914 step may be a lag, in which case the 1911 and 1912 keyframes should become adjust (include Cuando Cubango) and the gain move earlier or go. Pages to try: Cuando_Cubango_Province, Moxico_Province, Joao_de_Almeida.
- /identity/rulers: provisional government 5 October 1910 to August 1911 (List of presidents of Portugal).
- Timor, Goa, Macau, Guinea, Sao Tome: no dated events (page budget; thin by design).

## Advisories (not blocking)
- /ledger/2-3: the Humbe "German occupation" is an inference: the pages say the Portuguese withdrew from the Humbe region and the Ovambo (German-backed) revolted; neither says German troops held it. Consider a contest with the Cuanhama kingdom from December 1914 instead. german-africa (af-08) has no mirror event for Naulila/Humbe either way.
- Occupation pairing: the ledger holds two overlapping occupation pairs with the same counterpart string "german-africa" in opposite directions (Kionga 1916-04..1919-06, Portugal occupier; northern Mozambique 1917-11..1918-08, Germany occupier, owner's record). A compiler pairing FIFO by counterpart would cross them; pair by (counterpart, region spec). Direction cannot be inferred from geometry for Kionga (Cliopatria's Mozambique already contains it); read the note.
- Double owners: portuguese-mozambique (af-08) also records the 1919 Kionga gain; german-africa's Kionga and Lettow-Vorbeck events name portuguese-mozambique, not portuguese-republic, as counterpart; portuguese-mozambique has no 1916 or 1917-18 occupation events of its own.

## Cross-dossier matrix
| event | mirror | status |
| --- | --- | --- |
| PR 1910-10 found (kingdom-of-portugal) | kingdom-of-portugal /ledger/37 1910-10 dissolve -> portuguese-republic | matched |
| PR 1910 predecessor portuguese-empire (added) | portuguese-empire /ledger/85 1910 dissolve -> portuguese-republic | matched after fix |
| PR 1914 gain nobody | - | exception (nobody) |
| PR 1914-12 occupation_start german-africa (Humbe) | none in german-africa | missing (af-08) |
| PR 1915-07 occupation_end german-africa (Humbe) | none in german-africa | missing (af-08) |
| PR 1915-08/09 contest Cuanhama kingdom | no dossier; portuguese-angola /ledger/24 1915 gain from Cuanhama | exception |
| PR 1916-04 occupation_start german-africa (Kionga) | german-africa /ledger/37 1916-04 occupation_start portuguese-mozambique | matched (counterpart slug differs) |
| PR 1917-11 occupation_start german-africa (N Mozambique) | german-africa /ledger/42 1917-11 | matched (counterpart slug differs) |
| PR 1918-08 occupation_end german-africa | german-africa /ledger/44 1918-08 | matched (counterpart slug differs) |
| PR 1919-06 occupation_end german-africa (Kionga) | german-africa /ledger/52 1919-06 | matched |
| PR 1919-06 gain german-africa (Kionga) | german-africa /ledger/59 1919-06 loss portuguese-mozambique; portuguese-mozambique /ledger/21 1919-06 gain | matched (double recipient) |
| PR 1926-05 dissolve estado-novo | estado-novo not written | exception (group not run) |
