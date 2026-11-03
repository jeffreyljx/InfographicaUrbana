# Review of batch sa-02-b (2026-10-19)

Adversarial review of six dossiers by the Phase B reviewer. Machine copy: history/notes/phase-b/reviews/sa-02-b.json. All six validate (0 errors; 2 warnings for the unwritten slug abhira-dynasty).

| slug | verdict | blocking | reviewer-applied |
| --- | --- | --- | --- |
| satavahana-dynasty | fail | 4 | 1 |
| mahameghavahana-dynasty | thin | 0 | 0 |
| shunga-empire | thin | 0 | 0 |
| kanva-dynasty | thin | 0 | 0 |
| indo-scythians | fail | 2 | 1 |
| indo-parthians | thin | 0 | 1 |

## satavahana-dynasty: fail

Area: infobox None (None), Cliopatria 890254, ratio None. No infobox area on the Satavahana dynasty page (re-checked); Cliopatria max 890,254 km2 (106..126).

Findings:

- [BLOCKING] `/keyframe_review/6 .. /keyframe_review/14`: The Krishna-Guntur coast (Amaravati, Guntur, Vijayawada; about 78,000 km2 at 14.2-17.9N, 78.8-83.4E) leaves the shape at -31 and no Cliopatria polity holds it to 223, yet every keyframe from -31 to 215 is marked ok and no event explains the -31 drop. Evidence: Satavahana dynasty page: capitals 'Pratishthana (Paithan) and Amaravati (Dharanikota)'; after Rudradaman the dominions were 'limited to their original base in the Deccan and eastern central India around Amaravati'; Sri Yajna's inscriptions at 'Nashik, Kanheri and Guntur'. H3 check: Amaravati is inside the -225..-50 shapes and outside every shape from -31 to 215 (held by no polity); Guntur and Vijayawada are outside the -27..215 shapes; the dossier's own successor lands for andhra-ikshvaku (Guntur 120 km, Vijayawada 100 km) and chutu-dynasty (Banavasi) lie outside the 215 shape. Fix: Mark -31..215 adjust with union[{cliopatria: 'Satavahana Dynasty', year: <shape year>}, {place: 'Guntur', km: 120}, {place: 'Vijayawada', km: 100}] (at the least from 127, where the page puts the base 'around Amaravati'), text quoting the page; check whether Banavasi belongs in the 184..215 shapes; if instead a loss is meant, add it with a page.
- [BLOCKING] `/ledger/1, /ledger/2`: Both Malwa gains name shunga-empire as counterpart, but that dossier ends in -73 (dissolve to the Kanvas) and has no loss; neither gain shows in the keyframes at its year (Ujjain enters the shapes only at -31, Vidisha only at -27; the -50 shape equals the -91 one), and /ledger/2 (eastern Malwa, Bhopal/Vidisha) duplicates /ledger/3 (-28, the Vidisha country from the Kanvas) and collides with the Kanva capital Besnagar (Vidisha) held to -28. Evidence: Satavahana page: Satakarni II 'captured eastern Malwa from the Shungas' (Ollett ca. 88-42 BCE); Kanva page: the Kanvas 'allowed the kings of the Shunga dynasty to continue to rule in obscurity in a corner of their former dominions'; Shunga page: 'The Andhras did indeed destroy the last remains of the Sunga state in central India somewhere around Vidisha'. /ledger/1 note says 'the lands lie inside Cliopatria's shape from -225', which is false for Ujjain (23.18N; the -225..-32 shapes stop at 22.72N). The indo-scythians -77 shape also holds Ujjain. Fix: Either (a) keep the years, set the counterpart to the holder of the cells (kanva-dynasty from -73, or a named 'Shunga remnant at Vidisha (no dossier)'), add the mirror losses there, and mark the Satavahana -91/-66/-50 keyframes adjust to add Ujjain from -70 (and Vidisha from -50 only if the Kanva shapes lose it then); or (b) move the gains to Cliopatria's years (-31 western Malwa, -27 Vidisha) at confidence 1 and drop /ledger/2 as a duplicate of /ledger/3. Correct the /ledger/1 note.
- [BLOCKING] `/keyframe_review/7, /keyframe_review/8 and a missing ledger event`: Chhattisgarh (Raipur, Bilaspur) is inside the -27..126 shapes while the sibling mahameghavahana-dynasty holds Chhattisgarh (South Kosala) -50..109 and loses it to this state in 110 (its /ledger/2); the two dossiers overlap by about 94,000 km2 for -27..109 and this ledger has no 110 gain. Evidence: Mahameghavahana dynasty page: 'South Kosala was later conquered by Gautamiputra Satakarni of the Satavahana dynasty in the early part of the 2nd century CE'. Overlap computed by resolving both dossiers' active keyframes with tools/gazetteer.py at -20, 60 and 100. The author lists the missing mirror under gaps (page budget), but the source page is already in this batch. Fix: Mark the -27 and 106 keyframes adjust: minus[{cliopatria: 'Satavahana Dynasty', year: <y>}, {admin1: 'Chhattisgarh', country: 'India'}] until 109; add {year: 110, type: gain, counterpart: mahameghavahana-dynasty, region: {admin1: 'Chhattisgarh', country: 'India'}, source: Mahameghavahana_dynasty, confidence: 2}.
- [BLOCKING] `/keyframe_review/9`: The 127 shape (verdict ok) drops Nashik and Sopara, but the page and this dossier's own /ledger/5 note keep Poona and Nasik Satavahana after Rudradaman's victories. Evidence: Rudradaman I page: 'Rudradaman regained all the former territories previously held by Nahapana, except for the southern territory of Poona and Nasik'. H3 check: Nashik is outside satavahana-dynasty_127 (and back inside 154). Fix: Mark keyframe 127 adjust: union[{cliopatria: 'Satavahana Dynasty', year: 127}, {place: 'Nasik', km: 100}], text quoting the page; adjust /ledger/5 region to minus Nasik as well.
- [to do] `/ledger/4`: The 124 gain of Konkan, Vidarbha and Malwa from the Western Satraps has no trace in the keyframes (the -27..126 shapes already hold all three and no earlier loss to the Kshaharatas is entered), and the page does not say Vidarbha was taken from Nahapana. Evidence: Gautamiputra Satakarni page: the Nashik prashasti lists 'Asika, Asaka, Mulaka, Suratha, Kukura, Aparanta, Anupa, Vidabha, Akaravanti' and says he 'uprooted the Kshaharata (or Khagarata) family'; nothing ties Vidarbha (Berar) to Nahapana; the Satavahana page credits Satakarni I with Vidarbha. Flagged by the author as a gap (Kshatrapa seizure undated). Fix: Remove {region: 'Vidarbha'} from the region and its text; then either enter the Kshaharata loss (Konkan/Aparanta, Malwa, the Nashik-Pune country) with a dated page (Nahapana) and adjust keyframes -27/106 for those years, or lower /ledger/4 to confidence 1 and say in keyframe 106's note that the gain repeats land Cliopatria never removed.
- [APPLIED] `/ledger/5/note, /keyframe_review/9/note`: The quoted sentence was given as a firm statement; the page hedges it. Evidence: Gautamiputra Satakarni page: 'It is possible that by the end of his reign, Gautamiputra lost some of his territory to the Kardamakas'. Fix: Quote corrected in both notes to the page's wording (applied by the reviewer; validator: 0 errors).

Thin (for a gap-filler):

- `/ledger/0`: start year: page 'c. late 2nd cent. BCE' (infobox), range 271-30 BCE; -225 kept from Cliopatria at confidence 1 (try https://en.wikipedia.org/wiki/Satavahana_dynasty)
- `/ledger/6`: year of the Aparanta dowry (154 is Cliopatria's) (try https://en.wikipedia.org/wiki/Vashishtiputra_Satakarni)
- `/ledger/7`: year of Yajna Sri's recovery (reign variants 152-203) (try https://en.wikipedia.org/wiki/Yajna_Sri_Satakarni)
- `/ledger/8`: year of the Abhira seizure near Nashik (199 = end of Sen's reign 170-199) (try https://en.wikipedia.org/wiki/Abhira_dynasty)
- `/keyframe_review/2, 4, 5, 11, 13, 14`: shape changes at -144, -66, -50, 161, 207 and 215 have no dated event (author's gap; within the 9-page budget) (try https://en.wikipedia.org/wiki/Western_Satraps)
- `/ledger (missing)`: Nahapana's seizure of the western Deccan and Malwa, needed to make /ledger/4 a real gain (try https://en.wikipedia.org/wiki/Nahapana)

Spot checks:

- `/ledger/2` https://en.wikipedia.org/wiki/Satavahana_dynasty: confirmed. 'captured eastern Malwa from the Shungas'; Ollett ca. 88-42 BCE; but counterpart and keyframe trace wrong (see fixes)
- `/ledger/4` https://en.wikipedia.org/wiki/Gautamiputra_Satakarni: confirmed. 'M. K. Dhavalikar dates this event to c. 124 CE'; Vidarbha not on the page as Kshaharata land
- `/ledger/5` https://en.wikipedia.org/wiki/Rudradaman_I: confirmed. r. 130-150; 'except for the southern territory of Poona and Nasik'; the Kardamaka sentence is hedged on the Gautamiputra page (fixed)
- `/ledger/8` https://en.wikipedia.org/wiki/Satavahana_dynasty: confirmed. 'the Abhiras captured the northern parts of the kingdom, around Nashik region'; Yajna Sri 170-199 (Sen)
- `/ledger/9` https://en.wikipedia.org/wiki/Satavahana_dynasty: confirmed. infobox 'c. 224 CE'; text 'until c. 225 CE'; five successor kingdoms

## mahameghavahana-dynasty: thin

Area: infobox 700000 (-20), Cliopatria 1655395, ratio 2.36. Only Cliopatria shape is -170..-165; the infobox figure has a map caption 'circa 20 BCE'. Author replaced the shape (corrected about 0.3 M km2, ratio 0.43, stated as a floor).

Findings:

- [to do] `/ledger/1/counterpart`: The -50 gain of Chhattisgarh names 'South Kosala (no state named on the page)', but Cliopatria's Kanva shapes hold Chhattisgarh then (Raipur, Bilaspur, Ambikapur inside kanva-dynasty_-50 and _-30), so the sibling kanva-dynasty keeps the same land -50..-28 (overlap about 188,000 km2 at -40) and has no loss; the notes flag the Satavahana overlap but not this one. Evidence: Mahameghavahana dynasty page: 'In the first century B.C. conquered Kalinga and Kosala'; H3/gazetteer overlap of the active keyframes of both dossiers at -40. Fix: Set the counterpart to kanva-dynasty (the Cliopatria holder) and have kanva-dynasty enter the mirror loss and adjust its -50/-30 keyframes minus Chhattisgarh (see kanva-dynasty); mention it in notes (e).
- [to do] `/ledger/3`: Dissolve at 350 (confidence 1) while the page gives the dynasty's span as ending in the 'early 4th century CE'; the note quotes only the infobox century. Evidence: Mahameghavahana dynasty page: '2nd or 1st century BC to early 4th century CE'; infobox 'Disestablished: 4th century CE'. Fix: Either move the end into the early 4th century (e.g. 320; change identity.end, keyframe 110's 'to', certainty and capital spans) or quote 'early 4th century CE' in the note and say why 350 is kept.
- [to do] `/keyframe_review/0/note`: The note says the infobox area has 'no year given'; the infobox map is captioned 'Extent of the Maha-Meghavahanas, circa 20 BCE'. Evidence: Mahameghavahana dynasty page infobox. Fix: Add the c. 20 BCE caption year to the area comparison (no shape change).

Thin (for a gap-filler):

- `/ledger/0`: founding year: page founder 140 BCE and '2nd or 1st century BC'; -170 kept for the kalinga handover (confidence 1) (try https://en.wikipedia.org/wiki/Kharavela)
- `/ledger/3`: end of the dynasty (confidence 1) (try https://en.wikipedia.org/wiki/Hathigumpha_inscription)
- `/keyframe_review/1`: peak extent against the infobox 700,000 km2 (c. 20 BCE); corrected shapes are about 0.3 M km2 (ratio 0.43, acknowledged) (try https://en.wikipedia.org/wiki/Kalinga_(historical_region))

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Mahameghavahana_dynasty: confirmed. '140 BCE: Mahameghavahana (founder)'; 'Established: 2nd or 1st century BC'; confidence 1 is honest
- `/ledger/1` https://en.wikipedia.org/wiki/Mahameghavahana_dynasty: confirmed. 'In the first century B.C. conquered Kalinga and Kosala'; Kharavela 50 BCE in the infobox
- `/ledger/2` https://en.wikipedia.org/wiki/Mahameghavahana_dynasty: confirmed. 'in the early part of the 2nd century CE'
- `/ledger/3` https://en.wikipedia.org/wiki/Mahameghavahana_dynasty: mis-dated. page: 'early 4th century CE'; 350 at confidence 1

## shunga-empire: thin

Area: infobox None (None), Cliopatria 1155730, ratio None. No infobox area (only a map 'Territory of the Shungas c. 150 BCE'). Mathura correctly outside all Shunga shapes ('never seems to have been under the direct control of the Shungas').

Thin (for a gap-filler):

- `/ledger/1`: the -91 gain (+56,000 km2, Punjab-Haryana edge) has no page; confidence 1, recorded to explain the shape (try https://en.wikipedia.org/wiki/Pushyamitra_Shunga)
- `/keyframe_review/3`: the -144 shrink (-39,000 km2) has no event (within the 5-page budget) (try https://en.wikipedia.org/wiki/Shunga_Empire)
- `/identity/end`: the Shunga remnant 'in a corner of their former dominions' after -73, destroyed by the Andhras 'somewhere around Vidisha' (author's note b); needed to give satavahana-dynasty /ledger/1-2 a living counterpart (try https://en.wikipedia.org/wiki/Kanva_dynasty)

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Shunga_Empire: confirmed. 'the Shunga dynasty was established in 184 BCE'; infobox assassination 185 BCE
- `/ledger/1` https://en.wikipedia.org/wiki/Shunga_Empire: not on page. no c. 91 BCE gain on the page; the note says so (confidence 1, honest)
- `/ledger/2` https://en.wikipedia.org/wiki/Shunga_Empire: confirmed. 'The Shungas were succeeded by the Kanva dynasty around 73 BCE'; Kanva page '73 BCE'

## kanva-dynasty: thin

Area: infobox None (None), Cliopatria 1155441, ratio None. No infobox area.

Findings:

- [to do] `/keyframe_review/2, /keyframe_review/3`: The -50 and -30 shapes (ok, unverified) hold Chhattisgarh (South Kosala), which the sibling mahameghavahana-dynasty holds from -50 on page evidence; about 188,000 km2 overlap -50..-28 and no Kanva loss. Evidence: Mahameghavahana dynasty page: 'In the first century B.C. conquered Kalinga and Kosala'; H3 check: Raipur, Bilaspur, Ambikapur inside kanva-dynasty_-50 and _-30; gazetteer overlap at -40. Fix: Mark -50 and -30 adjust: minus[{cliopatria: 'Kanva Dynasty', year: <y>}, {admin1: 'Chhattisgarh', country: 'India'}] and add {year: -50, type: loss, counterpart: mahameghavahana-dynasty, confidence: 1}; or, if the author keeps Chhattisgarh Kanva, start the Mahameghavahana keyframe at -28.
- [to do] `/identity/capitals/1`: Besnagar (Vidisha) is a Kanva seat to -28 while satavahana-dynasty /ledger/2 has the Satavahanas take the Vidisha-Bhopal country 'from the Shungas' in -50. Evidence: Kanva page: coins 'primarily found in and around the region of Vidisha'; infobox 'Capital: Pataliputra and Besnagara'. Fix: No change here if satavahana-dynasty drops or re-dates /ledger/2 (see that dossier); otherwise add the mirror loss.

Thin (for a gap-filler):

- `/keyframe_review/1`: extent of the Kanva realm (Cliopatria repeats the Shunga outline; page gives coins only) (try https://en.wikipedia.org/wiki/Kanva_dynasty)
- `/ledger/1`: the Ganges-plain part of the realm after -28 has no Cliopatria successor (Mitra dynasty of Kaushambi 'hegemony' over Magadha) (try https://en.wikipedia.org/wiki/Kaushambi)

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Kanva_dynasty: confirmed. 'The Kanva dynasty was established by Vasudeva Kanva in 73 BCE'
- `/ledger/1` https://en.wikipedia.org/wiki/Kanva_dynasty: confirmed. 'brought to an end by the Satavahanas in 28 BCE'; 'a localised event in Central India'
- `/identity/rulers` https://en.wikipedia.org/wiki/Kanva_dynasty: confirmed. 73-64, 64-50, 50-38, 38-28 BCE

## indo-scythians: fail

Area: infobox None (None), Cliopatria 1496248, ratio None. No infobox area on the Indo-Scythians page (re-checked).

Findings:

- [BLOCKING] `/keyframe_review/11, /keyframe_review/12, /keyframe_review/13, /ledger/10, /ledger/13`: Arachosia (Kandahar) is inside the Indo-Scythian 1, 14, 43, 51 and 91 shapes, so this dossier keeps it 20..74 while the sibling indo-parthians gains it from this state in 20 and holds it to 226 (about 111,000 km2 overlap at 60); /ledger/10's note says 'Arachosia and Seistan lie outside Cliopatria's Indo-Scythian shape', which is false for Arachosia; /ledger/13 then loses Kandahar to the Kushans in 75 although indo-parthians keeps it. Evidence: H3 check: the Kandahar cell is in indo-scythians shapes at -100..95; gazetteer overlap of the two dossiers' active keyframes at 60 = 442 cells; Indo-Parthian page: 'Gondophares became the ruler of areas comprising Arachosia, Seistan, Sindh, Punjab, and the Kabul valley'. Fix: From 20, mark keyframes 14, 43 and 51 adjust minus {region: 'Arachosia'}; add {region: 'Arachosia'} to /ledger/10's region and fix its note; remove Arachosia from /ledger/13's region (minus[{cliopatria: 'Indo-Scythians', year: 51}, {place: 'Mathura', km: 200}, {region: 'Arachosia'}]).
- [BLOCKING] `/ledger/8, /keyframe_review/6, /keyframe_review/7`: The -58 loss of Ujjain uses the cells -66 minus -50, which are the eastern Punjab belt (Lahore, Ludhiana and Sialkot leave the shape at -50; 826 cells, mean 29.8N 75.3E), not Ujjain: Ujjain is already outside the -66 shape (it leaves between -77 and -66). Keyframe 7's note 'Fits the Indo-Scythians page: Vikrama retook Ujjain' is therefore wrong, and the -50 Punjab loss is unexplained. Evidence: Indo-Scythians page: 'the Indian king Vikrama retook Ujjain from the Indo-Scythians', 'establishing the Vikrama era in 58 BCE' (year confirmed). H3 check: Ujjain in indo-scythians_-77 only; Lahore, Ludhiana, Sialkot in _-66 and not in _-50. Fix: Set /ledger/8 region to {place: 'Ujjain', km: 150} (text 'Ujjain'); mark keyframe -66 adjust to keep the Ujjain cells until -58 (union with {place: 'Ujjain', km: 100}) or say Cliopatria drops them early; enter the -50 eastern Punjab loss as its own event (counterpart indo-greeks, confidence 1 unless a page dates the Indo-Greek recovery) and correct keyframe 7's note.
- [to do] `/ledger/2/counterpart`: The -110 gain names parthian-empire, but of the 1,530 cells gained 1,325 were held by no Cliopatria polity at -111, 200 by indo-greeks and 4 by parthian-empire; no page dates it. Evidence: Cell-by-cell check of indo-scythians -110 minus -126 against every polity alive at -111. Fix: Counterpart 'nobody' (or split off the 200 Indo-Greek cells); this removes a false 400,000 km2 mirror request to me-06.
- [to do] `/ledger/6/counterpart`: The -77 gain (+1,000,000 km2) names indo-greeks for all of it; 1,607 of 3,896 cells were Indo-Greek at -78, the other 2,286 (Gujarat, Sindh coast, Malwa) held by nobody. Evidence: Cell-by-cell check of indo-scythians -77 minus -87 against polities alive at -78. Fix: Split into an indo-greeks part and a 'nobody' part, or say in the note that most of the land had no holder so me-05 is not asked to mirror 1 M km2.
- [to do] `/wars/0/zones`: 'Saka invasions of Parthia' has no zone although its outcome says 'the Saka kept Drangiana (Sakastan)'. Evidence: The war's own outcome text and /ledger/1. Fix: Add zone {region: 'Sistan', text: 'Drangiana (Sakastan)'}.
- [APPLIED] `/ledger/10`: Dated 20 CE at confidence 2 with the note 'The page dates the conquests only within his reign (c. 19-46)', but the Indo-Parthian page dates them 'Around 20-10 BC'. Evidence: Indo-Parthian Kingdom page: 'Around 20–10 BC, he made conquests in the former Indo-Scythian kingdom, perhaps after the death of the important ruler Azes.' Fix: Note corrected to quote the page and confidence lowered to 1 (applied by the reviewer; validator: 0 errors).

Thin (for a gap-filler):

- `/ledger/1`: year and extent of the Saka settlement of Drangiana (confidence 1) (try https://en.wikipedia.org/wiki/Sakastan)
- `/ledger/2`: the -110 growth (+400,000 km2) has no page (try https://en.wikipedia.org/wiki/Indo-Scythians)
- `/ledger/6`: who held Gujarat, the Sindh coast and Malwa -77..42 (confidence 1) (try https://en.wikipedia.org/wiki/Western_Satraps)
- `/ledger/11`: the 43 cut (-326,000 km2) to the Western Satraps (confidence 1) (try https://en.wikipedia.org/wiki/Western_Satraps)
- `/ledger/12`: year of Kujula's Kabul-Gandhara conquest (51 is Cliopatria's; confidence 1) (try https://en.wikipedia.org/wiki/Kujula_Kadphises)

Spot checks:

- `/ledger/5` https://en.wikipedia.org/wiki/Indo-Scythians: confirmed. 'Maues first conquered Gandhara and Taxila ... c. 80 BCE'; Taxila from Apollodotus II
- `/ledger/7` https://en.wikipedia.org/wiki/Northern_Satraps: confirmed. 'From around 70 BCE, the region of Mathura fell to the Indo-Scythian Northern Satraps under Hagamasha, Hagana'
- `/ledger/8` https://en.wikipedia.org/wiki/Indo-Scythians: confirmed. year and Ujjain confirmed; the region spec is wrong (see fixes)
- `/ledger/9` https://en.wikipedia.org/wiki/Northern_Satraps: confirmed. 'Rajuvula conquered the last remaining Indo-Greek kingdom, under Strato II, around 10 CE, and took his capital city, Sagala'
- `/ledger/13` https://en.wikipedia.org/wiki/Indo-Scythians: confirmed. 'The Kushans regained northwestern India c. 75 CE and the Mathura region c. 100'
- `/ledger/10` https://en.wikipedia.org/wiki/Indo-Parthian_Kingdom: mis-dated. page: conquests 'Around 20–10 BC' (fixed: confidence 1, note)

## indo-parthians: thin

Area: infobox None (None), Cliopatria 487435, ratio None. No infobox area.

Findings:

- [APPLIED] `/ledger/1`: Dated 20 CE at confidence 2 with the note 'The page dates the conquests only within the reign (c. 19-46)'; the page dates them 'Around 20–10 BC'. Evidence: Indo-Parthian Kingdom page: 'Around 20–10 BC, he made conquests in the former Indo-Scythian kingdom, perhaps after the death of the important ruler Azes.' Fix: Note corrected to quote the page and confidence lowered to 1 (applied by the reviewer; validator: 0 errors).
- [to do] `/keyframe_review/0`: Cliopatria's 1..13 shape is marked wrong on the 19/20 founding, citing Senior as 'one view', but the same page also has Gondophares' conquests 'Around 20–10 BC' and lists 'Gondophares II Sarpedones (first years AD – c. 20 AD)'. Evidence: Indo-Parthian Kingdom page (ruler list and the sentence quoted above). Fix: State the page's own conflicting lines in the note; either keep 19 as the infobox date with that conflict said, or accept the 1 CE shape (verdict ok, start 1) and move indo-scythians /ledger/10 accordingly.
- [to do] `/keyframe_review/1/correction/text, /ledger/2`: K1 calls the Cliopatria shape '(Punjab, Sindh, Kabul valley)' and /ledger/2 loses Kabulistan, but Kabul is outside every Indo-Parthian shape (north edge 34.42N; the Kabul cell is yuezhi at -100..30 and kushan-empire at 45..60). Evidence: H3 check of Kabul (34.53N 69.17E) against all polities at -100..60. Fix: Either add {region: 'Kabulistan'} to keyframes 14 and 43 (19..49) with the page's 'Kabul valley', or drop Kabulistan from /ledger/2 and /ledger/3 and the K1 text.

Thin (for a gap-filler):

- `/ledger/3`: year of the Kushan conquest of Punjab and Sindh (90 is Cliopatria's; confidence 1) (try https://en.wikipedia.org/wiki/Vima_Takto)
- `/keyframe_review/5`: Turan is not placed; the Sakastan remnant 91..226 is Cliopatria's Indo-Scythian 91 cells (Helmand/Kandahar), while Zaranj itself is Cliopatria's Parthian row (me-06 to confirm) (try https://en.wikipedia.org/wiki/Sakastan)

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Indo-Parthian_Kingdom: confirmed. 'The kingdom was founded in 19/20 when the governor of Drangiana' declared independence; infobox 19-226
- `/ledger/1` https://en.wikipedia.org/wiki/Indo-Parthian_Kingdom: mis-dated. page: 'Around 20–10 BC' (fixed: confidence 1, note)
- `/ledger/2` https://en.wikipedia.org/wiki/Indo-Parthian_Kingdom: confirmed. 'from the middle of the 1st century AD the Kushans under Kujula Kadphises began absorbing the northern Indian part'
- `/ledger/4` https://en.wikipedia.org/wiki/Indo-Parthian_Kingdom: confirmed. 'until its conquest by the Sasanian Empire in c. 224/5'; Turan and Sakastan 'circa 230 CE'; infobox 226

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| satavahana-dynasty -225 found (maurya-empire) | maurya-empire -225 loss | matched |  |
| satavahana-dynasty -70 gain (shunga-empire) | - | mismatch | shunga-empire ends -73 and has no loss; land per Cliopatria is outside the Shunga/Kanva shapes (Ujjain) and enters Satavahana only at -31 |
| satavahana-dynasty -50 gain (shunga-empire) | - | mismatch | shunga-empire ends -73; Vidisha is in kanva-dynasty shapes and capitals to -28; duplicates satavahana -28 gain |
| satavahana-dynasty -28 gain (kanva-dynasty) | kanva-dynasty -28 dissolve | matched | Kanva dissolve region is the whole realm; only the Central Indian 200,000 km2 passes to the Satavahanas (explained in the Kanva successors note) |
| satavahana-dynasty 124 gain (western-satraps) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (sa-02) |
| satavahana-dynasty 127 loss (western-satraps) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (sa-02) |
| satavahana-dynasty 154 gain (western-satraps) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (sa-02) |
| satavahana-dynasty 184 gain (western-satraps) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (sa-02) |
| satavahana-dynasty 199 loss (abhira-dynasty) | - | exception | in the author's counterparts_needing_dossiers |
| mahameghavahana-dynasty -170 found (kalinga) | kalinga -171 dissolve | matched |  |
| mahameghavahana-dynasty -50 gain (South Kosala (no state named on the page)) | - | mismatch | Cliopatria's kanva-dynasty -50/-30 shapes hold Chhattisgarh; Kanva has no loss (about 188,000 km2 overlap -50..-28) |
| mahameghavahana-dynasty 110 loss (satavahana-dynasty) | - | missing | no 110 gain in satavahana-dynasty; its -27..126 shapes already hold Chhattisgarh (about 94,000 km2 overlap -27..109) |
| mahameghavahana-dynasty 350 dissolve (gupta-empire) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (sa-02) |
| shunga-empire -184 found (maurya-empire) | maurya-empire -185 dissolve | matched |  |
| shunga-empire -91 gain (indo-greeks) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (me-05) |
| shunga-empire -73 dissolve (kanva-dynasty) | kanva-dynasty -73 found | matched |  |
| indo-scythians -144 found (greco-bactrian-kingdom) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (me-05) |
| indo-scythians -126 gain (parthian-empire) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (me-06); 623 of 1,036 cells were Parthian in Cliopatria |
| indo-scythians -110 gain (parthian-empire) | - | mismatch | no dossier yet (me-06), but 1,325 of 1,530 cells had no holder and only 4 were Parthian: counterpart should be nobody |
| indo-scythians -100 loss (parthian-empire) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (me-06) |
| indo-scythians -88 gain (indo-greeks) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (me-05); all 205 cells Indo-Greek in Cliopatria |
| indo-scythians -80 gain (indo-greeks) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (me-05) |
| indo-scythians -77 gain (indo-greeks) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (me-05); only 1,607 of 3,896 cells Indo-Greek, rest unheld |
| indo-scythians -70 gain (Mathura's local rulers (not named on the page)) | - | exception | named non-dossier counterpart; Mathura unheld in Cliopatria at -80/-70 |
| indo-scythians -58 loss (Vikrama of Ujjain (no state named on the page)) | - | exception | named non-dossier counterpart; region spec wrong (see fixes) |
| indo-scythians 10 gain (indo-greeks) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (me-05) |
| indo-scythians 20 loss (indo-parthians) | indo-parthians 20 gain | mismatch | years agree; land differs: the Indo-Parthian gain includes Arachosia, the Indo-Scythian loss does not and its keyframes keep Arachosia to 74 |
| indo-scythians 43 loss (western-satraps) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (sa-02) |
| indo-scythians 51 loss (kushan-empire) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (sa-02) |
| indo-scythians 75 loss (kushan-empire) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (sa-02); the region includes Kandahar, which indo-parthians keeps to 226 |
| indo-scythians 100 dissolve (kushan-empire) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (sa-02) |
| indo-parthians 19 found (parthian-empire) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (me-06); Zaranj is Parthian in Cliopatria through 150+ |
| indo-parthians 50 loss (kushan-empire) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (sa-02) |
| indo-parthians 90 loss (kushan-empire) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (sa-02) |
| indo-parthians 226 dissolve (sasanian-empire) | - | exception | counterpart owned by a group that has not run yet; no dossier in history/polities/ (me-06) |
| kanva-dynasty -73 found (shunga-empire) | shunga-empire -73 dissolve | matched |  |
| kanva-dynasty -28 dissolve (satavahana-dynasty) | satavahana-dynasty -28 gain | matched |  |

## Problems

- WebFetch returns a model's extraction of each Wikipedia page, not the raw text; quotes above are the extraction's verbatim quotes.
- Shunga Empire and Kanva Dynasty: under the rule in the author's brief section 6 ('a dynasty that replaces a dynasty on the same land without a break stays in the state's dossier as a rename event'), the Kanva usurpation of 73 BCE (minister of the last Shunga, same capitals Pataliputra and Vidisha, identical Cliopatria cells) is a rename inside one state; the reviewer agrees with the author that they should be merged into shunga-empire with a -73 rename, and asks the orchestrator to decide.
- The Chhattisgarh (South Kosala) overlap spans three dossiers of this batch (mahameghavahana-dynasty, kanva-dynasty, satavahana-dynasty) and the Arachosia overlap two (indo-scythians, indo-parthians); route each set to one author together.
- Reviewer-applied fixes (all validated, 0 errors): satavahana-dynasty /ledger/5 and /keyframe_review/9 notes (hedged quote); indo-parthians /ledger/1 and indo-scythians /ledger/10 (confidence 2 to 1, note quoting 'Around 20–10 BC').
- Neighbour dossiers read: maurya-empire, kalinga, yuezhi (ledger) and greek-city-states (no batch counterpart); parthian-empire, kushan-empire, western-satraps, indo-greeks, greco-bactrian-kingdom, eastern-kushans, western-kushans, sasanian-empire, indo-sasanian-empire are not written yet (exceptions).
- Spatial checks used tools/grid.py polity_cells and tools/gazetteer.py resolve on H3 r5 cells (about 252 km2 per cell); overlaps are approximate.

## Gazetteer names wanted

- Turan (region, indo-parthians)
- Dakshina Kosala (South Kosala) (region, mahameghavahana-dynasty)
- Paithan (place, satavahana-dynasty)
- Dharanikota (place, satavahana-dynasty)
- Junnar (place, satavahana-dynasty)
- Banavasi (place, satavahana-dynasty)
- Vidisha (place, shunga-empire)
- Kaushambi (place, kanva-dynasty)
- Kalinganagara (place, mahameghavahana-dynasty)
- Pushkalavati (place, indo-scythians)
