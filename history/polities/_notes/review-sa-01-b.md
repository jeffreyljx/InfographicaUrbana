# Review of sa-01-b (2026-10-18)

Adversarial review of the six sa-01-b dossiers. Validator: 0 errors in all six; warnings only for Rajouri and Thanesar (not in the gazetteer). Neighbour dossier read: janapada-of-gandhara (janapada-of-vatsa is not written yet); also janapada-of-anga and janapada-of-cedi ledgers for the mirrors. Overlaps and island counts were computed by resolving the regions with tools/gazetteer.py. Twelve page reads (all nine pages the authors used, three of them read twice for extra quotes).

Verdicts: janapada-of-magadha **fail**, janapada-of-kosala **fail**, janapada-of-malla **fix**, janapada-of-kamboja **fail**, janapada-of-kuru **fail**, janapada-of-kasi **pass**.

## janapada-of-magadha: fail

Findings:
- `/keyframe_review/0` (for the author): Keyframe -600 is marked ok, but the Cliopatria disc does not hold the page's Magadha: the capital Rajgir (85.42E 25.03N) lies about 44 km outside the shape, Gaya district is missing, and the disc crosses the Ganga to the north (5 of 20 cells north of 25.62N, the Vaishali bank) and the Son to the west (to 84.51E). Evidence: Magadha page: 'The core of the kingdom was the area of Bihar south of the Ganges'; 'bounded to the north, west, and east respectively by the Gaṅgā, Son, and Campā rivers, and the eastern spurs of the Vindhya mountains formed its southern border'; 'Patna and Gaya districts'. shapes.csv janapada-of-magadha_-600 bbox 84.51-85.452E, 25.10-25.87N; gazetteer: nearest shape cell centre to Rajgir 43.8 km. The dossier's own capital is drawn outside its state. Fix: Verdict adjust with a correction on the page's bounds, e.g. {"intersect":[{"union":[{"place":"Patna","km":45},{"place":"Rajgir","km":35},{"place":"Gaya","km":45}]},{"polygon":[[84.85,24.3],[86.2,24.3],[86.2,25.3],[85.7,25.42],[85.2,25.58],[84.85,25.62],[84.85,24.3]]}]} (tested: 35 cells, about 8,850 km2, one piece, contains Rajgir), text quoting the Ganga/Son/Campa sentence; use the same base in /ledger/0, /keyframe_review/1, /ledger/3 and /identity/successors/0/land.
- `/keyframe_review/1/correction` (for the author): The -530 union resolves to two islands (the Magadha disc, 20 cells, and Anga plus Bhagalpur 60 km, 59 cells) with an unowned gap of about 90 km between Magadha and the Anga it has just annexed. Evidence: Gazetteer resolution of the correction gives 2 connected components; the Magadha page has the Campa as Magadha's eastern border, i.e. the two countries touch. Fix: Rebuild on the corrected -600 base (above) and close the gap to the Anga land (for example a place circle at Lakhisarai/Munger or a polygon to the Campa); check that the union is one component. Carry the same land into /ledger/3 and the successors entry.
- `/ledger/1/note` (applied by reviewer): Misquote: the note said 'according to the Mahavagga chronology'. Evidence: Haryanka page: 'Bimbisara reigned from 544 to 492 BCE, according to the Mahavamsa chronology.' Fix: Replaced with 'according to the Mahavamsa chronology'; re-validated (0 errors).

Thin (for a gap-filler):
- `/ledger/2`: Year of the Anga annexation (-530 is borrowed from the Anga dossier; confidence 1). Try https://en.wikipedia.org/wiki/Bimbisara
- `/wars`: The earlier Anga-Magadha war (Anga's Brahmadatta against Bhattiya of Magadha) that the Anga dossier carries as a contest over Magadha land -600..-543 has no war entry here. Try https://en.wikipedia.org/wiki/Bimbisara
- `/ledger/0`: Founding is a confidence-1 bridge at Cliopatria's -600; the dissolve at /ledger/3 is Cliopatria's row change. Try https://en.wikipedia.org/wiki/Brihadratha_dynasty

Spot checks:
- `/ledger/1` (https://en.wikipedia.org/wiki/Haryanka_dynasty): confirmed ('Established: 544 BCE'; 'Bimbisara is considered to be the founder of the dynasty'); note misquote fixed
- `/ledger/2` (https://en.wikipedia.org/wiki/Mahajanapadas): confirmed ('Anga was annexed by Magadha in the time of Bimbisara'; 'This was the one and only conquest of Bimbisara'); undated on the page, confidence 1 is honest
- `/ledger/0` (https://en.wikipedia.org/wiki/Magadha): confirmed ('Patna and Gaya districts'), but the drawn region does not hold it (see /keyframe_review/0)
- `/identity/capitals/0` (https://en.wikipedia.org/wiki/Magadha): confirmed ('its first capital was Rajagriha (modern day Rajgir)'); coordinates lie outside the shape

Area: No infobox area on the Magadha page (author says so). Cliopatria 5040.0 km2; ratio None.

## janapada-of-kosala: fail

Findings:
- `/keyframe_review/0/correction` (for the author): The Awadh correction (also in /keyframe_review/1/correction, /ledger/0/region, /ledger/2/region and /identity/successors/0/land) runs south across the Ganga and the Yamuna and west across the Gomti, swallowing two neighbouring Mahajanapadas: 14 of the 15 cells of Cliopatria's Vatsa disc (Kausambi, -600..-451) and about 57 cells (about 14,400 km2) of the Cedi dossier's corrected land (Banda 90 km + Rewa 50 km, -600..-451). The note acknowledges only the west. Evidence: Kosala page: 'Kosala was bounded by the Gomti River in the west, Sarpika River in the south, Sadanira in the east' and 'the Nepal Hills in the north'. The gazetteer's Awadh is Uttar Pradesh intersected with 79.5-83.5E, 25.4-28.5N (about 118,600 km2). Cell overlaps computed with tools/gazetteer.py against janapada-of-vatsa_-600 and janapada-of-cedi ledger/0. Fix: Cut Awadh to the page's bounds, e.g. {"union":[{"intersect":[{"region":"Awadh"},{"polygon":[[80.9,26.2],[81.6,26.0],[82.4,25.9],[83.5,25.9],[83.5,28.5],[80.9,28.5],[80.9,26.2]]}]},{"cliopatria":"Janapada of Kāśī","year":-600}]} with a minus of {"cliopatria":"Janapada of Vatsa","year":-600} (tested: 233 cells, about 58,900 km2, one piece, 2 Vatsa cells before the minus, 0 Cedi cells); apply it in all five places and say in the note which neighbours it borders.
- `/ledger/1/note` (for the author): Says the Kosala page has the Kashi annexation 'in the 6th century BCE'; the page gives no century for it (also in /keyframe_review/0/note). Evidence: Kosala page: 'It annexed the powerful kingdom of Kashi' (undated) and 'By the 5th century BCE under the reign of King Mahakosala, the neighboring Kingdom of Kashi had been conquered'; its '6th century' sentences are about Kosala's rise ('By the 6th century BCE, it had consolidated into one of the four great powers'). Fix: Quote the Mahakosala sentence instead; the confidence-2 year rests on the Kāśī infobox, which is right.

Thin (for a gap-filler):
- `/ledger/2`: Year of Kosala's absorption by Magadha (page: '5th century BCE'; -451 is Cliopatria's), confidence 1. Try https://en.wikipedia.org/wiki/Ajatashatru
- `/ledger`: Viḍūḍabha's annexations of the Sakya and Koliya republics and the Kālāmas ('Shortly after the Buddha's death', undated; no event and no counterpart dossiers). Try https://en.wikipedia.org/wiki/Shakya
- `/ledger/0`: Founding is a confidence-1 bridge at -600 (infobox 'Established: c. 7th century BCE'). Try https://en.wikipedia.org/wiki/Kosala

Spot checks:
- `/ledger/1` (https://en.wikipedia.org/wiki/K%C4%81%C5%9B%C4%AB_(kingdom)): confirmed (infobox 'Conquered by Kaṃsa of Kosala: c. 600 BCE')
- `/ledger/0` (https://en.wikipedia.org/wiki/Kosala): confirmed sentence ('roughly corresponds to modern-day Awadh region'), but the page's own borders exclude the drawn south
- `/ledger/2` (https://en.wikipedia.org/wiki/Kosala): confirmed undated ('finally defeated and absorbed into the Magadha kingdom in the 5th century BCE'; 'Viḍūḍabha was defeated and killed by the Māgadhī king Ajātasattu')
- `/wars/0` (https://en.wikipedia.org/wiki/K%C4%81%C5%9B%C4%AB_(kingdom)): confirmed undated ('Pasenadi revoked his rights over the village in Kāśī, after which a war between Kosala and Magadha ensued')

Area: No infobox area. The 24x enlargement is acknowledged but leaves the overshoot into Vatsa and Cedi unresolved (see fixes). Cliopatria 4989.7 km2; ratio 24.1.

## janapada-of-malla: fix

Findings:
- `/keyframe_review/1/note` (applied by reviewer): Inverted wording: 'the disc is right but ends 17 years early' (Cliopatria's disc runs 17 years too long, to -451; the dossier ends at -468). Evidence: Malla page: Magadha able 'to finally defeat the Vajjika League by 468 BCE'; Cliopatria row ends -451. Fix: Replaced with 'the disc is right but Cliopatria keeps it 17 years too long (to -451)'; re-validated (0 errors).

Thin (for a gap-filler):
- `/ledger/1`: The Mallas' own fall is dated by the Vajjika League's (468 BCE); confidence 2. Try https://en.wikipedia.org/wiki/Ajatashatru
- `/ledger/0`: Founding is a confidence-1 bridge at -600 (infobox 'Established: c. 7th century BCE'). Try https://en.wikipedia.org/wiki/Malla_(tribe)

Spot checks:
- `/ledger/1` (https://en.wikipedia.org/wiki/Malla_(tribe)): confirmed ('declared war on the Vajjika League in 484 BCE'; 'to finally defeat the Vajjika League by 468 BCE'; 'The Mallas also became part of Ajatashatru's Māgadhī empire')
- `/ledger/0` (https://en.wikipedia.org/wiki/Malla_(tribe)): confirmed ('The Mallas lived in the region now covered by the Kushinagar district')
- `/wars/0` (https://en.wikipedia.org/wiki/Malla_(tribe)): confirmed (484-468 BCE)
- `/identity/capitals/0` (https://en.wikipedia.org/wiki/Mahajanapadas): confirmed ('Kushinagar (modern Kasia near Gorakhpur) as its capital'); inside the shape (4.8 km from a cell centre)

Area: No infobox area; Cliopatria disc kept. Cliopatria 5485.7 km2; ratio None.

## janapada-of-kamboja: fail

Findings:
- `/keyframe_review/0/correction` (for the author): The Kamboja land (also /keyframe_review/1/correction, /ledger/0/region, /ledger/2/region, /identity/successors/0/land) overlaps the Gandhara dossier's: the 50 km circle at Rajouri takes 6 cells of Gandhara's Kashmir Valley (Srinagar 70 km) and Nuristan 2 more cells of Gandhara's own region, for -600..-518 (and the Kashmir Valley passes to the Achaemenids with Gandhara's -518 dissolve while Kamboja still holds it to -501). Evidence: Gazetteer resolution: Kamboja correction 66 cells, Gandhara correction (janapada-of-gandhara /keyframe_review/0, /ledger/0, /ledger/2 include {"region":"Kashmir Valley"}) overlap 8 cells, Rajouri circle alone 6. The author read the Gandhara dossier (notes say so) and did not flag the overlap. Fix: Subtract the Gandhara land, e.g. {"minus":[<current union>,{"union":[{"region":"Kashmir Valley"},{"region":"Gandhara"}]}]}, or agree a Pir Panjal line with the Gandhara owner (sa-01-a) and note it.

Thin (for a gap-filler):
- `/ledger/1`: Date of Cyrus's destruction of Kapisi (page: 'is said to have destroyed', undated; confidence 1). Lead, not checked on a page: ancient Kapisi (Begram) may lie in modern Parwan rather than Kapisa province. Try https://en.wikipedia.org/wiki/Begram
- `/ledger/2`: Whether and when Kamboja became Achaemenid (Mahajanapadas page's 'twentieth satrapy' against the conquest page, where the twentieth province is 'The Indians'); end year is Cliopatria's. Try https://en.wikipedia.org/wiki/Achaemenid_Empire
- `/ledger/0`: Founding and extent are confidence 1 (capital 'site remains unknown'; Lamotte 'from Kafiristan to the southwestern part of Kashmir'); the land is three separate islands (Nuristan, Kapisa, Rajouri). Try https://en.wikipedia.org/wiki/Kambojas

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Mahajanapadas): confirmed ('The capital of Kamboja was probably Rajapura (modern Rajori) in the south-west of Kashmir'; Kambojas page: Lamotte 'from Kafiristan to the southwestern part of Kashmir')
- `/ledger/1` (https://en.wikipedia.org/wiki/Mahajanapadas): confirmed undated ('Cyrus II is said to have destroyed the famous Kamboja city called Kapisi (modern Begram) in Paropamisade'); confidence 1 honest
- `/ledger/2` (https://en.wikipedia.org/wiki/Mahajanapadas): confirmed sentence ('Kamboja and Gandhara formed the twentieth and richest satrapy'); contradicted by the conquest page, flagged by the author
- `/wars/0` (https://en.wikipedia.org/wiki/Achaemenid_conquest_of_the_Indus_Valley): confirmed (infobox belligerents 'Gandhara Sindhu-Sauvīra Kambojas'; 'Around 518 BCE ... up to the Jhelum River')

Area: No infobox on the Kambojas page. The corrected land is about 16,700 km2 (3.3 times the disc) and the notes do not give its size; add it to the /keyframe_review/0 note. Cliopatria 5086.8 km2; ratio 3.3.

## janapada-of-kuru: fail

Findings:
- `/keyframe_review/0/correction` (for the author): The union Delhi + Meerut 40 km + Thanesar 40 km (also /keyframe_review/1, /keyframe_review/2, /ledger/0/region, /ledger/1/region) resolves to three separate islands (5, 19 and 18 cells; two today, as Thanesar is not in the gazetteer), leaving Ghaziabad and the Sonipat-Panipat-Karnal country unowned and dropping Cliopatria's disc around Delhi; the page describes one country. Evidence: Mahajanapadas page: 'The country of the Kurus roughly corresponded to the modern Thanesar, state of Delhi, and Meerut district'. Gazetteer resolution: 3 connected components. Fix: A contiguous union, e.g. {"union":[{"admin1":"Delhi","country":"India"},{"place":"Ghaziabad","km":30},{"place":"Meerut","km":40},{"place":"Sonipat","km":35},{"place":"Panipat","km":35},{"place":"Karnal","km":45}]} (tested: one piece, 65 cells, about 16,400 km2; shrink the radii to taste), Karnal standing for Thanesar until the gazetteer has it.
- `/keyframe_review/2/note` (for the author): Says Cliopatria's Shaishunaga row 'covers this country'; it does not. Evidence: shapes.csv magadha-shaishunaga-dynasty_-404 bbox reaches only 27.672N (Kuru lies at 28.25-29.97N); gazetteer: 0 cells shared with the Kuru disc or the Kuru correction. Fix: Delete the claim and the 'may overlap' line in the report: the -404..-346 extension does not collide with the Shaishunaga shape.

Thin (for a gap-filler):
- `/ledger/1`: Who took the Kuru land at c. 345 BCE (counterpart nobody; the infobox end-year likely reflects Mahapadma Nanda's conquests). Try https://en.wikipedia.org/wiki/Mahapadma_Nanda
- `/ledger/0`: Founding is a confidence-1 bridge at -600. Try https://en.wikipedia.org/wiki/Kuru_Kingdom

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Mahajanapadas): confirmed ('roughly corresponded to the modern Thanesar, state of Delhi, and Meerut district')
- `/ledger/1` (https://en.wikipedia.org/wiki/Kuru_Kingdom): confirmed (infobox 'c. 1900 BCE – c. 345 BCE'); the end is not explained on the page
- `/keyframe_review/2` (https://en.wikipedia.org/wiki/Mahajanapadas): confirmed ('Kautiliya's Arthashastra also attests the Kurus'); the words '4th century BCE' were not in the extract
- `/identity/capitals/0` (https://en.wikipedia.org/wiki/Mahajanapadas): confirmed ('the capital of the Kurus was Indraprastha (Indapatta) near modern Delhi'); inside the Cliopatria disc

Area: No infobox area; author notes the correction is about 10,500 km2, twice the disc. Cliopatria 5231.7 km2; ratio 2.0.

## janapada-of-kasi: pass

Thin (for a gap-filler):
- `/ledger/0`: Founding is a confidence-1 bridge at -600 (infobox 'Established: c. 1375 BCE'); the one-year life rests on the infobox 'c. 600 BCE' (confidence 2). Try https://en.wikipedia.org/wiki/K%C4%81%C5%9B%C4%AB_(kingdom)

Spot checks:
- `/ledger/1` (https://en.wikipedia.org/wiki/K%C4%81%C5%9B%C4%AB_(kingdom)): confirmed (infobox 'Conquered by Kaṃsa of Kosala: c. 600 BCE'; 'finally conquered for good by Kosala under the latter's king Kaṃsa, shortly before the time of the Buddha')
- `/ledger/0` (https://en.wikipedia.org/wiki/K%C4%81%C5%9B%C4%AB_(kingdom)): confirmed ('The capital of Kāśī was the city of Vārāṇasī'; Sarpikā/Syandikā and Son borders)
- `/keyframe_review/1` (https://en.wikipedia.org/wiki/K%C4%81%C5%9B%C4%AB_(kingdom)): confirmed ('Kāśī was a full part of the kingdom of Kosala by the time of its king Mahākosala'; Ajātasattu 'annexed Kosala')
- `/wars/0` (https://en.wikipedia.org/wiki/K%C4%81%C5%9B%C4%AB_(kingdom)): confirmed (conquest by Kaṃsa); Mahajanapadas page 'during Buddha's time' is the conflict the author flagged

Area: No infobox area; '300 leagues' is a length (author says so). Cliopatria 5039.9 km2; ratio None.

## Cross-dossier matrix

- janapada-of-magadha -530 gain -> janapada-of-anga: matched (janapada-of-anga -530 dissolve). Same land (Cliopatria Anga + Bhagalpur 60 km).
- janapada-of-anga -600 contest_start -> janapada-of-magadha: missing (janapada-of-magadha None war). Anga contests Magadha land -600..-543 (Bimbisara page); Magadha has no war for it. Routed as thin to Magadha.
- janapada-of-kosala -600 gain -> janapada-of-kasi: matched (janapada-of-kasi -600 dissolve). Same land (Cliopatria Kāśī -600).
- janapada-of-magadha -501 dissolve -> magadha-haryanka-dynasty: exception (magadha-haryanka-dynasty None found). Haryanka dossier owned by another sa-01 part that has not run; the author argues both are one state (see problems).
- janapada-of-kosala -451 dissolve -> magadha-haryanka-dynasty: exception (magadha-haryanka-dynasty None gain). Haryanka not written yet; Cliopatria's Haryanka -450 shape (335,215 km2, to 80.90E 27.80N) does take Kosala in -450.
- janapada-of-malla -468 dissolve -> magadha-haryanka-dynasty: exception (magadha-haryanka-dynasty None gain). Haryanka not written yet; its Cliopatria shape reaches the Malla latitude only in -450, so the Haryanka dossier needs a -468 gain.
- janapada-of-kamboja -530 loss -> achaemenid-empire: exception (achaemenid-empire None gain). Achaemenid dossier belongs to the Iran group, not run yet.
- janapada-of-kamboja -501 dissolve -> achaemenid-empire: exception (achaemenid-empire None gain). Iran group not run. Gandhara (same 'twentieth satrapy' sentence) dissolves to the Achaemenids at -518; the two years differ by 17.
- janapada-of-kuru -345 dissolve -> nobody: exception (nobody None None). Counterpart nobody; who took the land is a gap (thin).
- janapada-of-kosala -600 found -> janapada-of-vatsa: mismatch (janapada-of-vatsa -600 found). Land overlap: Kosala's Awadh holds 14 of 15 cells of Vatsa's Cliopatria disc, -600..-451. Vatsa (sa-01) not written yet.
- janapada-of-kosala -600 found -> janapada-of-cedi: mismatch (janapada-of-cedi -600 found). Land overlap: about 57 cells of Cedi's corrected land (Banda 90 km + Rewa 50 km) inside Kosala's Awadh, -600..-451.
- janapada-of-kamboja -600 found -> janapada-of-gandhara: mismatch (janapada-of-gandhara -600 found). Land overlap of 8 cells (Rajouri circle vs Kashmir Valley; Nuristan vs Gandhara region), -600..-518.

## Problems for the orchestrator

- janapada-of-magadha and magadha-haryanka-dynasty are one state by the research brief's one-state-per-dossier rule (Haryanka 'Established: 544 BCE' falls inside the Magadha row); the assignment split them, so the Magadha dossier carries a -544 rename to Haryanka and then a -501 dissolve into Haryanka. The orchestrator should decide whether the Haryanka dossier continues this one.
- The gazetteer's Awadh region (Uttar Pradesh within 79.5-83.5E, 25.4-28.5N) reaches south of the Ganga and Yamuna; historical Awadh lies north of the Ganga. Worth tightening at the gazetteer, beyond the Kosala fix.
- Kamboja/Gandhara overlap needs the Gandhara owner (sa-01-a) too.
- The author's worry that Kuru's extension to -345 overlaps Cliopatria's Shaishunaga row is unfounded: 0 shared cells.
- Applied two note-text fixes in place (janapada-of-magadha /ledger/1/note, janapada-of-malla /keyframe_review/1/note); both re-validated with 0 errors.
- Quotes checked come from WebFetch extracts (a small model reads the page); no page failed to load.
