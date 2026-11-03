# Review of batch eu-02-b (Hellenistic world, part b)

Reviewer: adversarial reviewer, Phase B, 2026-10-19 (brief filled 2026-10-18). Inputs: the author's brief, report and notes; the five dossiers; neighbour dossiers aetolian-league, greek-city-states, roman-republic, cimmerian-bosporus, scythia, athenian-coalition, mamertines and antigonid-dynasty, plus kingdom-of-epirus, peloponnesian-league, messene, massalia and syracuse for mirrors. ptolemaic-kingdom, seleucid-empire, kingdom-of-pergamon, kingdom-of-armenia, kingdom-of-bithynia, kingdom-of-pontus, greco-bactrian-kingdom and carthage are not written yet; their groups have not run, so their mirrors count as the brief's exception.

Validator: all five dossiers are valid with --resolve: 0 errors, and warnings only for the gazetteer names Agde and Laconia. achaean-league still validates after the reviewer's one edit.

Verdicts: achaean-league **fail** (two keyframe corrections misdraw land for 13-15 years), greek-colonies **thin**, illyrian-kingdom **thin**, rhodes **thin**, molossians **pass**.

## achaean-league: fail

Findings:
- `/keyframe_review/10/correction`: BLOCKING. The 206-165 correction is union(minus(clio@-206, Corinth), Peloponnese), which draws the whole Peloponnese, Corinth included, from 206. The dossier's own text and ledger say it holds only from 191. Evidence: The correction's own text reads '206-198 the league without Corinth; Argos lost to Nabis 198-195; Corinth back 197; Sparta 192; Messene and Elis 191: the whole Peloponnese from 191'. The ledger gains Argos in 195 (/ledger/22), Sparta in 192 (/ledger/24) and Messenia and Elis in 191 (/ledger/25), all land this keyframe already shows from 206. The peloponnesian-league dossier holds Laconia to its 192 dissolve and antigonid-dynasty holds Corinth to 196/197, so Laconia, Messenia, Elis and Corinth are drawn twice for 15 years. The overdraw is about 10 k km2 on an 11.8 k km2 shape. Fix: Make /keyframe_review/10 correction {"minus": [{"cliopatria": "Achaean League", "year": -206}, {"place": "Corinth", "km": 15}]} with text '206-192: the league without Corinth (Macedonian to 197); Argos with Nabis 198-195'. Add a new keyframe achaean-league_-191 (from -191, to -165, verdict adjust) with correction {"region": "Peloponnese", "text": "the whole peninsula from 191"}. Optionally add achaean-league_-198 (-198..-192) for the shape minus Argos, with Corinth back from 197.
- `/keyframe_review/8/correction`: BLOCKING. The 225-211 correction removes Argos and the Acte (a 35 km disc, about 3.8 k km2) for all 15 years, though its text limits that to 225-224. Megara (lost 223) and Heraea and Orchomenus (ceded to Macedon 224) stay in. Evidence: The text says 'for 225-224, less the Argolid cities that surrendered to Cleomenes'. /ledger/13 regains Argos in 224 ('The Argives revolted against Cleomenes, and the Achaean reinforcements took the whole city'). /ledger/14 loses Megara in 223, confirmed on the Achaean League page: 'In 223 BC, Megara in Attica deserted the Achaean League and joined the Boeotian Confederacy'. The next keyframe (/keyframe_review/9, 210-207) does subtract Megara. Fix: Keep /keyframe_review/8 as is for 225 only: an adjust whose text says the shape holds 225-225. Add a new keyframe achaean-league_-224 (from -224, to -211, verdict adjust) with correction minus(clio@-225, union(Corinth 15 km, Megara disc 10 km from 223)), the same as /keyframe_review/9. Heraea and Orchomenus to Macedon (infobox of the Cleomenean War) may go in its text.
- `/ledger/19/counterpart` (applied by reviewer): The 198 loss of Argos named peloponnesian-league. Argos went to Philip V first, and only in 197 to Nabis. Evidence: Nabis of Sparta page: 'During the Second Macedonian War, Nabis sided with King Philip V of Macedon and in return he received the city of Argos.' The event's own note: 'Argos went over to Philip V'. antigonid-dynasty /ledger/54 has the 198 gain from achaean-league, and /ledger/55 the 197 hand-over to peloponnesian-league. Fix: counterpart 'antigonid-dynasty' (applied by the reviewer; validates).
- `/ledger/25/counterpart`: The 191 gain of Messenia (Kalamata) and Elis (Pirgos) names greek-city-states, but messene has a dossier that loses Messenia to achaean-league in 191. Evidence: messene /ledger/3: -191 loss achaean-league, Messenia, c1; /ledger/4: dissolve. greek-city-states /ledger/68 has a 191 loss of 'Peloponnese' to achaean-league. Fix: Split /ledger/25 into a 191 gain of Kalamata from messene and a 191 gain of Pirgos (Elis) from 'Elis' or greek-city-states. Both stay at confidence 1.
- `/keyframe_review/6/correction`: Megalopolis (joined 235) and Tripoli (Orchomenus and Mantinea, c. 234) are added for all of 239-231, so they are drawn 4-5 years early. This is minor. Evidence: /ledger/6 is dated 235 (Achaean League page: 'Corinth was followed by Megalopolis in 235 BC'); /ledger/7 is c. 234, c1. Fix: Optional: a new keyframe achaean-league_-235 (-235..-231) carrying the additions, with /keyframe_review/6 reduced to clio@-239 for 239-236.
- `/wars`: The First Macedonian War (211-205) and the Roman-Seleucid War (192-188) are missing from wars[]. The league fought in both (Philopoemen at Mantinea 207; Messene and Elis added 191). Evidence: /keyframe_review/9 note: 'Philopoemen's victory at Mantinea (207) changed no border'. Fix: Add both wars, with empty zones for 211-205 and the note 'no ground changed hands'.

Gaps for a gap-filler:
- `/ledger/7`: The year and source for Orchomenus and Mantinea joining (c. 234, confidence 1). Try https://en.wikipedia.org/wiki/Mantinea
- `/ledger/25`: The year Messene and Elis joined (191 by the usual chronology; the page says 'no dates given'). Try https://en.wikipedia.org/wiki/Messene

Spot checks:
- `/ledger/6` (https://en.wikipedia.org/wiki/Achaean_League): confirmed: 'Corinth was followed by Megalopolis in 235 BC'
- `/ledger/8` (https://en.wikipedia.org/wiki/Achaean_League): confirmed: '... and Argos in 229 BC'
- `/ledger/14` (https://en.wikipedia.org/wiki/Achaean_League): confirmed: 'In 223 BC, Megara in Attica deserted the Achaean League and joined the Boeotian Confederacy'
- `/ledger/22` (https://en.wikipedia.org/wiki/Nabis_of_Sparta): confirmed: 'Nabis was forced to surrender both Argos and the port of Gytheum' after Flamininus's ultimatum (195)
- `/ledger/17` (https://en.wikipedia.org/wiki/Social_War_(220%E2%80%93217_BC)): confirmed: 'At the turn of 219/18 BC' Philip 'stormed the city of Psophis and handed it over to his Achaean ally Aratus the Younger'; infobox 'Psophis and Lasion to Achaea'

Area: infobox None, Cliopatria 11769.5 km2, ratio None. The infobox gives no area (re-founded 280, conquered 146). The author's notes say the 206-145 polygon is undersized against the whole Peloponnese, which is acknowledged but drawn wrongly (see /keyframe_review/10).

## greek-colonies: thin

Findings:
- `/keyframe_review (whole dossier)`: The same aggregate is drawn twice for 271-226: greek-city-states /keyframe_review/60-61 (greek-city-states_-271 and the -257 piece) draw clio:Greek Colonies@-271 for the same years. Evidence: greek-city-states K60 note: 'The orchestrator must decide whether eu-02 writes greek-colonies as a separate dossier (then this keyframe is dropped)'. The author of this dossier flags the duplicate too. Fix: Orchestrator: keep one. If this dossier stays, greek-city-states drops K60 and K61. If not, withdraw this dossier and fold its six reviewed shapes into greek-city-states.
- `/keyframe_review/5/correction`: If this dossier replaces the greek-city-states bridge, Attica after Athens's liberation in 229 is in neither dossier. Evidence: greek-city-states K60/K61 add Attica (union) to the aggregate, and antigonid-dynasty /ledger/31 has a 229 vassal_end of Attica with greek-city-states. This dossier's corrections never add Attica. Fix: If kept: add {"region": "Attica"} to /keyframe_review/5 (230-226) and say in its text that Athens is free from 229.
- `/keyframe_review/0/correction and /keyframe_review/1/correction`: Messana (the Mamertines' to 257) is not carved, but greek-city-states carves a 25 km disc at 15.55 E 38.19 N out of the same clio:Greek Colonies@-271 shape. Evidence: greek-city-states K60 correction minus(..., pt(15.55,38.19,25km)) for 271-258; the mamertines dossier draws Messana to 257. Fix: Carve the Mamertine disc out of K0 and K1 (271-257), or say in the note that the Sicilian cluster does not reach Messina.
- `/keyframe_review/2/correction`: Antipolis and Nikaia are carved from 256, while massalia gains them in 250 (massalia /ledger/3). For six years they are in neither dossier. This is negligible. Evidence: The Massalia page dates Antipolis and Nikaia 'c. mid-3rd c.'. Fix: Either carve them only from the 247 shape or leave it with a note.

Gaps for a gap-filler:
- `/ledger/1`: Who took the 13 inland Carian cells around 264 (Ptolemaic, Seleucid or Rhodian). Try https://en.wikipedia.org/wiki/Caria
- `/ledger/2`: The Carian and Sicilian cells that left around 256. Try https://en.wikipedia.org/wiki/Caria
- `/ledger/3`: The Propontic and Aegean cells added around 239. Try https://en.wikipedia.org/wiki/Cyzicus
- `/ledger/4`: The Colchian coast (Dioscurias), Elis and the Propontic cells added around 230. Try https://en.wikipedia.org/wiki/Dioscurias
- `/keyframe_review/0`: The West Pontic, Olbia, Crimean, Cretan, Iberian and Propontic clusters (unverified: page budget). Try https://en.wikipedia.org/wiki/Olbia,_Ukraine

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Greek_colonisation): confirmed: 'particularly during the 8th-6th centuries BCE'; 'usually independent of the metropolis and had their own governance'; 'did not involve demanding tribute or laying claim to the hinterland'
- `/ledger/2` (https://en.wikipedia.org/wiki/Hiero_II_of_Syracuse): confirmed: 'in 263 he concluded a treaty with Rome, by which he was to rule over the south-east of Sicily ... the eastern coast as far as Tauromenium'
- `/keyframe_review/2` (https://en.wikipedia.org/wiki/Massalia): confirmed: Tauroentium '(early 3rd c.)', Antipolis and Nikaia '(c. mid-3rd c.)', 'persisted as an independent colony', 'faithful ally of Rome during all of the Punic Wars (264-146 BC)'
- `/ledger/4` (https://en.wikipedia.org/wiki/Chersonesos_Taurica): confirmed as paraphrase (confidence 1): the page has a classical democracy and a civic oath 'from the 3rd century BC onwards', and names neither Colchis nor Dioscurias, as the note says

Area: infobox None, Cliopatria 82557.7 km2, ratio None. An aggregate row; the Greek colonisation page is not about a state and has no infobox area.

## illyrian-kingdom: thin

Findings:
- `/ledger (213) and /keyframe_review/4`: The 213 loss of Lissus 'and the surrounding territories' to Philip V is missing. /keyframe_review/4 freezes 228-197, yet /ledger/10 regains Lezhe from antigonid-dynasty in 196 without the dossier ever losing it. Evidence: First Macedonian War page, 213-212 campaign: 'by capturing Lissus and its seemingly impregnable citadel, after which the surrounding territories surrendered'; 'he took Dassaretis, Atintani and Parthini, and the town of Dimale'. antigonid-dynasty /ledger/45 is a 213 gain from illyrian-kingdom of union(Lezhe, Ohrid), c2. Fix: Add a -213 loss to antigonid-dynasty, region Lezhe (admin-1), source First_Macedonian_War, confidence 2. Add a new keyframe illyrian-kingdom_-213 (-213..-197) that subtracts Lezhe, with /keyframe_review/4 ending in 214.
- `/ledger/7 and /ledger/8`: The 229-228 losses go to roman-republic, but roman-republic /ledger/43 records a 228 vassal_start of 'Greek cities of the Illyrian coast (Epidamnos, Apollonia, Corcyra, Issa)' and no gain. The author's own counterparts_needing_dossiers lists Corcyra, Epidamnos and the Parthini as the receivers. Evidence: First Illyrian War page: 'The Romans had gained control of the strategic ports of Epidamnos, Apollonia and Corcyra'; 'The Parthini and Atintani became Roman clients'. Fix: Agree with roman-republic. Either name the client cities (free text, as in roman-republic /ledger/43) as counterparts of /ledger/7 and /ledger/8, or ask eu-03 for a 228 gain. Routed to the orchestrator.
- `/ledger/12`: The 168 loss to roman-republic is mirrored in roman-republic /ledger/71 as a vassal_start of 'Illyria (the three cantons of Gentius' kingdom)', not a gain. Evidence: Gentius page: 'the Romans split the region into three administrative divisions' (meris). Fix: Align with eu-03: either loss to the cantons (free text) with roman-republic's vassal_start, or a roman-republic gain.
- `/identity/rulers/1 and /identity/rulers/2`: Agron ends and Pinnes starts in 231, while the Illyrian kingdom page lists Agron '250 BC to 230 BC' and Pinnes 'B.C 230~B.C 217'. The author's notes record the 231/230 conflict. This is a note-only fix. Evidence: Illyrian kingdom page, list of rulers. Fix: Say in the ruler note that the kingdom page gives 230 and the Agron page 231.

Gaps for a gap-filler:
- `/ledger/0`: The founding year (256 is Cliopatria's) and the extent for 256-248. Try https://en.wikipedia.org/wiki/Ardiaei
- `/ledger/1`: The date of Agron's northern extension to Narona (247 is Cliopatria's year). Try https://en.wikipedia.org/wiki/Agron_of_Illyria
- `/ledger/2`: The date of the Epirote coast and Epidamnus annexation (239 is Cliopatria's year); no mirror in kingdom-of-epirus. Try https://en.wikipedia.org/wiki/Epirus_(ancient_state)
- `/ledger/10`: The land restored in 196 (Livy has Lychnidus and the Parthini given to Pleuratus); Lissus is a bridge. Try https://en.wikipedia.org/wiki/Pleuratus_III
- `/ledger (219)`: The Second Illyrian War (220-219): Demetrius of Pharos's Pharos and Dimale to Roman protection (roman-republic /ledger/48, 219 vassal_start). Try https://en.wikipedia.org/wiki/Second_Illyrian_War
- `/keyframe_review/4`: The extent for 228-197 (unverified: page budget). Try https://en.wikipedia.org/wiki/Scerdilaidas

Spot checks:
- `/ledger/3` (https://en.wikipedia.org/wiki/First_Illyrian_War): confirmed: 'In 231 BC, the fleet and army attacked Elis and Messenia'; 'On the way home, Teuta sent her general Scerdilaidas to capture the city of Phoenice'; the capture is dated only by sequence, as the note says
- `/ledger/5 and /ledger/7` (https://en.wikipedia.org/wiki/First_Illyrian_War): confirmed: the siege in the 229 narrative; 'Corcyra was surrendered and was occupied by a garrison under the command of Demetrius of Pharos'; 'Corcyra welcomed the Romans and, with the aid of Demetrius, surrendered its garrison'
- `/ledger/8` (https://en.wikipedia.org/wiki/First_Illyrian_War): confirmed: 'Before the end of winter, Teuta's envoys appeared in Rome and a treaty was concluded' (war 229-228); 'forced to give up all their recent conquests south of the Drin'; 'not to sail south of Lissus'
- `/ledger/11` (https://en.wikipedia.org/wiki/Gentius): confirmed: 'the Dalmatae and Daorsi declared themselves independent from his rule' (180)
- `/ledger/12` (https://en.wikipedia.org/wiki/Gentius): confirmed: 'he was defeated at Scodra by a Roman force under L. Anicius Gallus' (168); 'He ruled in 181-168 BC'; three meris

Area: infobox None, Cliopatria 49700.7 km2, ratio None. The infobox has no area (Established c. 500 BC, Disestablished 135 BC). The end of 168 against the infobox's 135 is flagged in the author's notes.

## rhodes: thin

Findings:
- `/ledger (164)`: The author's notes ask roman-republic to carry a 164 vassal_start on Rhodes, but Rhodes's own ledger has no such event. A vassal pair must appear in both ledgers. Evidence: Rhodes page: a formal alliance with Rome in 164 BC sharply limited Rhodes's freedom in foreign affairs, but 'Rhodes continued to remain nominally independent'. Fix: Either add a 164 vassal_start with roman-republic (confidence 2, Rhodes page) and a vassal_end at the end year, or withdraw the request in the notes and treat the alliance as no change of level.
- `/ledger/1 and /ledger/2 against /keyframe_review/1`: In 188 the same land (the mainland less the Cnidus-Kaunos strip) is both gained outright (/ledger/1, c3) and made tributary (/ledger/2, c1), and /keyframe_review/1 ('ok') draws all of it as full Rhodian territory. Evidence: Rhodian Peraia page: 'the entirety of Caria and Lycia south of the Maeander River came under Rhodian rule'; 'During this time, the Peraia comprised the fully incorporated portion, lying between Cnidus and Kaunos, and the remainder of Caria and Lycia, which were tributary to Rhodes'. Fix: Choose one level for 188-167. Either gain only the incorporated strip and record the rest as vassal_start (dropping it from /keyframe_review/1 with a correction), or drop /ledger/2 and /ledger/3 and keep the gain.

Gaps for a gap-filler:
- `/keyframe_review/0`: The mainland Peraia held before 188 (the Cnidian and Trachea peninsulas; Caunus bought c. 191; Stratonicea). The page says only that it 'grew with the addition of various vassal regions', undated. Try https://en.wikipedia.org/wiki/Kaunos
- `/ledger/2 and /ledger/3`: The dating of the tributary remainder of Caria and Lycia (confidence 1). Try https://en.wikipedia.org/wiki/Treaty_of_Apamea
- `/ledger/6`: The end of Rhodian self-rule. 39 is a bridge; the Rhodes page says only 'After losing its independence', undated. The free city lasted into the Principate. Try https://en.wikipedia.org/wiki/Lycia_et_Pamphylia

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Rhodes): confirmed: 'In 408 BC, the cities united to form one territory', with a new capital at the northern end
- `/ledger/1` (https://en.wikipedia.org/wiki/Rhodian_Peraia): confirmed: 'It reached its greatest extent after the Treaty of Apamea in 188 BC', Caria and Lycia south of the Maeander
- `/ledger/4` (https://en.wikipedia.org/wiki/Rhodian_Peraia): confirmed: 'when Rhodes submitted to Rome in 167 BC, this region was lost again'
- `/ledger/5` (https://en.wikipedia.org/wiki/Rhodian_Peraia): confirmed: 'Rhodes retained a portion of its old domains in Asia until 39 BC, when they were ceded to Stratonicea'

Area: infobox 1400.68, Cliopatria 25801.4 km2, ratio 18.42. The infobox is the modern island only. /keyframe_review/0 compares the island (about 1,517 km2, ratio 1.08) and /keyframe_review/1 explains the mainland Peraia.

## molossians: pass

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Third_Macedonian_War): confirmed: infobox 'Molossians (from 170 BC)' on the Macedonian side; 'Molossians in Epirus, on the west coast of Greece, went over to the Macedonians'
- `/ledger/1` (https://en.wikipedia.org/wiki/Molossians): confirmed: 'The Molossians sided with the Macedonians against Rome in the Third Macedonian War (171-168 BC) and were defeated'; 150,000 enslaved, undated
- `/ledger/2` (https://en.wikipedia.org/wiki/Molossians): confirmed: no 167 date on the Molossians or Third Macedonian War pages (Pydna 168; 'Troops were sent to seventy cities' undated)
- `/identity/capitals/0` (https://en.wikipedia.org/wiki/Molossians): confirmed: Pyrrhus 'transferred the capital of his kingdom from Passaron to Ambracia' (295)

Area: infobox None, Cliopatria 4707.9 km2, ratio None. No area on either page. The shape lies inside kingdom-of-epirus's Epirus keyframe (K8, 231-167): the double drawing is routed to the orchestrator under problems, not a fault of this dossier.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| achaean-league -275 gain (antigonid-dynasty) | antigonid-dynasty -275 loss | matched | Aegium |
| achaean-league -251 gain (greek-city-states) | greek-city-states -251 loss | matched | Sicyon |
| achaean-league -243 gain (antigonid-dynasty) | antigonid-dynasty -243 loss | matched | Corinth |
| achaean-league -243 gain (greek-city-states) | greek-city-states -243 loss | matched | Megara, Epidaurus, Troezen |
| achaean-league -235 gain (greek-city-states) | greek-city-states -235 loss | matched | Megalopolis |
| achaean-league -234 gain (greek-city-states) | greek-city-states -234 loss | matched | Tripoli (Orchomenus, Mantinea), both c1 |
| achaean-league -229 gain (antigonid-dynasty) | antigonid-dynasty -229 loss | mismatch | Land differs: achaean gains Argos (22.72 E 37.63 N, 25 km); antigonid-dynasty /ledger/32 loses 'Tripoli' (Arcadia). antigonid-dynasty should name Argos. |
| achaean-league -226 loss (peloponnesian-league) | - | missing | Mantinea to Cleomenes (Cleomenes III page); peloponnesian-league has no 226 gain (its /ledger/53 is a 229 gain of Tripoli from greek-city-states). Route to eu-01. |
| achaean-league -225 loss (peloponnesian-league) | peloponnesian-league -225 gain | matched | Argolid and Corinth |
| achaean-league -224 loss (antigonid-dynasty) | antigonid-dynasty -224 gain | matched | Acrocorinth |
| achaean-league -224 gain (peloponnesian-league) | peloponnesian-league -222 loss | mismatch | Argos returns in 224 (Cleomenean War page); peloponnesian-league /ledger/56 has the loss in 222 at c1. eu-01 should move it to 224. |
| achaean-league -223 loss (Boeotian League) | - | exception | No dossier; not in the author's counterparts_needing_dossiers, so the reviewer adds it. |
| achaean-league -218 gain (Elis) | - | exception | No dossier; the reviewer adds Elis to counterparts_needing_dossiers (antigonid-dynasty /ledger/39 also names it). |
| achaean-league -198 loss (antigonid-dynasty) | antigonid-dynasty -198 gain | matched | After the reviewer's fix (counterpart was peloponnesian-league). |
| achaean-league -197 gain (antigonid-dynasty) | antigonid-dynasty -196 loss | mismatch | antigonid-dynasty /ledger/58 gives Corinth (with Chalcis and Demetrias) to roman-republic in 196, while achaean-league has Corinth rejoin in 197 under a Roman garrison. |
| achaean-league -197 occupation_start (roman-republic) | - | missing | roman-republic has no occupation of Corinth 197-194 (nor its occupation_end). Route to eu-03. |
| achaean-league -195 gain (peloponnesian-league) | peloponnesian-league -195 loss | matched | Argos |
| achaean-league -192 gain (peloponnesian-league) | peloponnesian-league -192 dissolve | matched | Sparta |
| achaean-league -191 gain (greek-city-states) | greek-city-states -191 loss | mismatch | Matched with greek-city-states /ledger/68, but messene /ledger/3 also loses Messenia to achaean-league in 191: two dossiers give up the same land. Split /ledger/25 (see fixes). |
| achaean-league -146 loss (roman-republic) | roman-republic -146 gain | matched | Peloponnese |
| greek-colonies -271 found (greek-city-states) | greek-city-states -271 keyframe greek-city-states_-271 | mismatch | The same aggregate is drawn by both dossiers 271-226 (duplicate); the orchestrator keeps one. |
| greek-colonies -264 loss (undetermined (page silent)) | - | exception | Carian cells, confidence 1. |
| greek-colonies -256 loss (undetermined (page silent)) | - | exception | Carian and Sicilian cells, confidence 1. |
| greek-colonies -239 gain (nobody) | - | exception | Propontic cells, confidence 1. |
| greek-colonies -230 gain (nobody) | - | exception | Colchis, Elis and Propontis cells, confidence 1. |
| illyrian-kingdom -247 gain (nobody) | - | exception | Narona extension, confidence 1. |
| illyrian-kingdom -239 gain (kingdom-of-epirus) | - | missing | kingdom-of-epirus K7 (271-232) keeps union(Epirus, Arta) and has no loss to illyrian-kingdom. |
| illyrian-kingdom -231 gain (kingdom-of-epirus) | - | missing | Phoenice; no mirror in kingdom-of-epirus. |
| illyrian-kingdom -230 loss (kingdom-of-epirus) | - | missing | Phoenice returned; no mirror in kingdom-of-epirus. |
| illyrian-kingdom -229 gain (Corcyra (Corfu)) | - | exception | Listed in counterparts_needing_dossiers. |
| illyrian-kingdom -229 loss (roman-republic) | roman-republic -228 vassal_start | mismatch | roman-republic /ledger/43 makes Corcyra a client city (vassal_start of 'Greek cities of the Illyrian coast'), not a roman-republic gain. |
| illyrian-kingdom -228 loss (roman-republic) | roman-republic -228 vassal_start | mismatch | Same: Epidamnos and Apollonia become client cities in roman-republic's ledger; no gain. |
| antigonid-dynasty -213 gain (illyrian-kingdom) | - | missing | illyrian-kingdom has no 213 loss of Lissus (First Macedonian War page confirms the capture). |
| illyrian-kingdom -196 gain (antigonid-dynasty) | - | missing | antigonid-dynasty has no 196 loss to illyrian-kingdom (its /ledger/59 loses Dytiki Makedonia and other land to nobody). |
| roman-republic -219 vassal_start (Illyrian towns under Roman protection (Pharos, Dimale)) | - | missing | illyrian-kingdom has nothing in 220-219 (Second Illyrian War not opened); thin. |
| illyrian-kingdom -180 loss (Dalmatae) | - | exception | Listed in counterparts_needing_dossiers. |
| illyrian-kingdom -168 loss (roman-republic) | roman-republic -168 vassal_start | mismatch | roman-republic /ledger/71 makes 'Illyria (the three cantons of Gentius' kingdom)' a vassal, not a gain. |
| rhodes -408 found (greek-city-states) | - | missing | greek-city-states never subtracts the island of Rhodes (no keyframe of 85 names it), so the island is drawn twice from 408. Route to eu-01, as the author asks. |
| rhodes -188 gain (seleucid-empire) | - | exception | seleucid-empire (me-05) has not run. |
| rhodes -188 vassal_start (Caria and Lycia (tributary communities)) | - | exception | Listed as lycian-league in counterparts_needing_dossiers. |
| rhodes -167 loss (nobody) | - | exception | Caria and Lycia freed. |
| rhodes -39 loss (Stratonicea) | - | exception | Listed in counterparts_needing_dossiers. |
| molossians -170 found (kingdom-of-epirus) | - | mismatch | kingdom-of-epirus K8 (231-167, Epirus) still draws the Molossis and has no 170 split or loss: the Molossis is drawn by both dossiers 170-168. |
| antigonid-dynasty -170 vassal_start (molossians) | - | mismatch | antigonid-dynasty /ledger/67 (c3) and /ledger/68 make the Molossians vassals; the Third Macedonian War page says they 'went over to the Macedonians' (an ally on the infobox). molossians has no vassal pair. Route to eu-02-a: drop the pair or lower it. |
| molossians -168 loss (roman-republic) | roman-republic -167 gain | matched | Within a year; roman-republic /ledger/73 gains all of Epirus from molossians, wider than the Molossian shape. |

## Counterparts needing dossiers

- Elis (elis), -245..-191; named as free text by achaean-league /ledger/17 and antigonid-dynasty /ledger/39; not in the author's list
- Boeotian League (boeotian-league), -245..-146; achaean-league /ledger/14 (Megara 223); antigonid-dynasty /ledger/60; not in the author's list
- Corcyra (Corfu) (corcyra), -229..-228
- Epidamnos and Apollonia (Roman-protected Greek towns) (epidamnos), -229..-228
- Parthini and Atintani (parthini), -229..-228
- Dalmatae and Daorsi (dalmatae), -180..-168
- Lycian and Carian communities tributary to Rhodes (lycian-league), -188..-167
- Stratonicea (stratonicea), -39..-39
- Chersonesos Taurica (chersonesos), -271..-110

## Gazetteer names needed

- Agde (place), greek-colonies
- Laconia (region), greek-colonies
- Phoenice (Finiq) (place), illyrian-kingdom
- Rhizon (Risan) (place), illyrian-kingdom
- Cnidus (place), rhodes
- Kaunos (place), rhodes
- Passaron (place), molossians

## Problems

- Neighbour dossiers read: aetolian-league, greek-city-states, roman-republic, cimmerian-bosporus, scythia, athenian-coalition, mamertines, antigonid-dynasty, plus kingdom-of-epirus, peloponnesian-league, messene, massalia and syracuse for mirrors. Not written yet, so their mirrors count as the brief's exception: ptolemaic-kingdom, seleucid-empire, kingdom-of-pergamon, kingdom-of-armenia, kingdom-of-bithynia, kingdom-of-pontus, greco-bactrian-kingdom, carthage.
- Double drawing for the orchestrator: greek-colonies and the greek-city-states bridge keyframes K60-K61 (271-226) draw the same aggregate; molossians and kingdom-of-epirus K8 both draw the Molossis 170-168; greek-city-states never subtracts the island of Rhodes (rhodes from 408).
- antigonid-macedonia was not written: it is merged into antigonid-dynasty (eu-02-a), which lists both Names. The slug should be recorded as merged.
- achaean-league was kept from an earlier run (file of 2026-10-18), and its two blocking keyframe faults (K8, K10) predate this batch. The reviewer applied one counterpart fix (/ledger/19) and the file re-validates.
- WebFetch returns a model summary: quoted strings in this review are those the tool returned as quotations. The Achaean League, Illyrian kingdom and Molossians pages have no infobox area. No page failed to load.

What I tried and could not break, for molossians: I opened both cited pages. Kephalos's switch to Perseus c. 170, the defeat in the 171-168 war, the undated enslavement, and the absence of any 167 date are all as the notes say. The capital is a stated stand-in inside the shape's bbox. The single keyframe trims Cliopatria's 165 to 168 in its text. The only open questions are cross-dossier: the overlap with kingdom-of-epirus and antigonid-dynasty's vassal pair.
