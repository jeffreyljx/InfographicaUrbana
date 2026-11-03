# Review: batch sa-01-a (Indus to the Mahajanapadas, part a)

Adversarial review, 2026-10-18. Machine copy: history/notes/phase-b/reviews/sa-01-a.json. All six dossiers validate (`--resolve`; warnings only for gazetteer names the gazetteer lacks: Mehrgarh, Maheshwar, Banda (India), Rewa (India)). None of the neighbour dossiers (janapada-of-vatsa, janapada-of-kamboja) exists yet, nor do the counterparts (janapada-of-magadha, magadha-shaishunaga-dynasty, achaemenid-empire), so every mirror is an exception for a group that has not run yet.

Spot checks: 21 events and keyframes on 11 pages (Indus Valley Civilisation, Periodisation, Mohenjo-daro, Harappa, Cemetery H, Anga, Bimbisara, Asmaka, Avanti (region), Shishunaga, Cedī (tribe), Gandhāra (kingdom), Achaemenid conquest of the Indus Valley, Mahajanapadas). Every quote and date matched the page. Nothing fabricated. No page gives an area, so all area checks were made by extent.

## Verdicts

| dossier | verdict | in one line |
| --- | --- | --- |
| indus-valley-civilization | fail | the keyframe corrections leave Harappa out from -2800 to -2301, and the Late shape adds about 43,000 km2 in the east with no event |
| janapada-of-anga | fix (applied) | successor land now includes Champa; the contest over Magadha (confidence 1) stays thin |
| janapada-of-asmaka | fix (applied) | successor land moved from Adilabad to the corrected Godavari shape; the Mulaka annexation and the end stay thin |
| janapada-of-avanti | fix (applied) | successor land is now the corrected Malwa + Mahishmati + Vatsa; the Vatsa date stays thin |
| janapada-of-cedi | thin | the end (-451, confidence 1) goes against the infobox's c. 300 BCE; no conqueror is named |
| janapada-of-gandhara | fix (applied) | the -535 loss no longer double-counts Taxila; area figure corrected |

## indus-valley-civilization: fail (back to the author)

1. `/keyframe_review/2/correction`: K2 (-2800..-2501) is the bare Cliopatria -2700 shape. Harappa (30.63N; the shape stops at 29.60N) and Mehrgarh drop out after K1, with no ledger loss. Gazetteer: intersect(Harappa 20 km, IVC -2700) = 0 cells. Harappa page: 'Kot Dijian (Early Harappan) phase, c. 2800 - 2600 BC'. Fix: union(IVC -2700, Harappa 60, Mehrgarh 50).
2. `/keyframe_review/3` is marked ok, yet the -2500 shape (city-core islands, 40,149 km2) does not contain Harappa at all (0 cells). It touches Mohenjo-daro by only one cell, although ledger/3's text says 'the Punjab around Harappa'. Fix: adjust, union(IVC -2500, Harappa 60, Mohenjo-daro 40).
3. `/keyframe_review/6/correction` (also K7-K10): the Late Harappan shape adds about 43,246 km2 outside the Mature shape at -1900 (eastern Haryana about 20,000, eastern Indian Punjab about 11,600, Delhi 80 km about 18,000; these overlap), with no gain event. K4 and K5 are marked ok, though the -2300/-2000 shape stops at 76.95E while the page says the height reached 'to western Uttar Pradesh in the east'. Fix, preferred: K4 and K5 adjust with the eastern margin added, so -1900 is a pure loss. Alternative: a -1900 gain from nobody, region minus(K6, IVC -2000), source Cemetery H.
4. Thin: ledger/4 (-2300 full extent, confidence 1, the largest move in the batch). Try https://en.wikipedia.org/wiki/List_of_Indus_Valley_Civilisation_sites. The end year (1300 against 1500/1400) is a declared dispute.
5. Not a fault: the flagged 'reach to 36.7N' of the -1800 shape is one 253 km2 cell.
6. Routing: the author proposes cemetery-h-culture -1900..-1300 for sa-01-x, but this dossier already draws the Cemetery H range as its Late Harappan Punjab Phase in those years. A separate dossier would double-draw it.

## janapada-of-anga: fix (applied by the reviewer)

- `/identity/successors/0/land` was Cliopatria's -531 shape, which stops 20 km short of Champa. It is now the dissolve region union(Anga -600, Bhagalpur 60): 'Campa became the seat of a Magadhi viceroy'.
- Thin: ledger/1-2, the contest over Magadha -600..-543 at confidence 1. Dadhivahana's conquest is undated, and the close at Bimbisara's accession in 543 is an inference. Try https://en.wikipedia.org/wiki/Haryanka_dynasty.

## janapada-of-asmaka: fix (applied by the reviewer)

- `/identity/successors/0/land` was Cliopatria's -351 Adilabad shape, which the dossier itself moves 130 km. It is now union(Nizamabad 70, Nanded 80).
- Thin: ledger/1, Mulaka (undated, confidence 1; the Mulaka page failed for the reviewer too; try https://en.wikipedia.org/wiki/Paithan). Also ledger/2, the end at 425 or 345 with no conqueror named: try https://en.wikipedia.org/wiki/Nanda_Empire for Mahapadma's Puranic conquest list.

## janapada-of-avanti: fix (applied by the reviewer)

- `/identity/successors/0/land` was the 5,104 km2 Ujjain core, though its own note says the corrected shape. It is now union(Malwa, Maheshwar 60, Vatsa -451).
- Thin: ledger/1, Vatsa under Palaka at Cliopatria's -450 (confidence 1). Palaka acceded on the day of Mahavira's death by Jain tradition, possibly much earlier. Try https://en.wikipedia.org/wiki/Pradyota_dynasty.
- The war with Gandhara (Pradyota against Pukkusati) is mirrored in janapada-of-gandhara/wars/1.

## janapada-of-cedi: thin

- ledger/1: the end at -451 is Cliopatria's year, at confidence 1, with no successor, while the page's only date is 'Disestablished c. 300 BCE'. A gap-filler should settle the conqueror and year (try https://en.wikipedia.org/wiki/Nanda_Empire). Nothing else to break. The correction will not resolve until the gazetteer has Banda (India) and Rewa.

## janapada-of-gandhara: fix (applied by the reviewer)

- `/ledger/1/region` was {region: Gandhara}, but the gazetteer's Gandhara already contains Taxila 60 km (10,622 km2 overlap). The ledger thus lost Taxila in -535 while K1 keeps it to -519. It is now minus(Gandhara, Taxila 60), matching 'a large region to the west of the Indus River'.
- The area quoted in K0 and in notes is corrected from 'about 74,000' to 'about 63,000 km2' (resolved union).
- The Kamboja agent (sa-01) should read K0's note: the Rajapura ('modern Rajori') location is confirmed on the Mahajanapadas page.
- Thin: who held Kashmir after -518 (left to nobody by the successor land, which is consistent).
