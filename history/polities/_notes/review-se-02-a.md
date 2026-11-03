# Review of batch se-02-a (Tarumanagara, Galuh, Srivijaya, Sunda, Mataram, Early Balinese)

Reviewed 2026-10-19. The validator (--resolve) gives 0 errors on all six; Srivijaya has 4 warnings, all for counterpart slugs with no dossier yet. Spot checks were made with WebFetch (a summariser), at 4 to 6 events per dossier, weighted to confidence-3 events and the largest moves. Under the orchestrator's small-fix rule I applied the edits marked 'applied' below, re-validated each file and read it back.

No Context polity of the author's brief (section 6) has a dossier yet, so those counterparts are exceptions ('group not run'). tambralinga.json, water-chenla.json and khmer-empire.json already name srivijaya and were cross-checked.

## Verdicts

### tarumanagara: fix
- Area: infobox None (None), Cliopatria 62498.7, ratio None; No infobox area; the dossier notes say so.
- Spot checks: /ledger/0 confirmed (Tarumanagara); /ledger/3 confirmed (Tarumanagara); /ledger/4 confirmed (Galuh_Kingdom); /ledger/5 confirmed (Tarumanagara)
- Fixes:
  - `/wars/0/to` [applied by reviewer]: The Srivijayan invasion war ran 669-686 while the state ends in 669, so the war lay outside the state's life. Evidence: Tarumanagara page: infobox 'Invasion by Sriwijaya: 669 AD'; text 'very likely ... attacked and defeated by Srivijaya around 686'. The two dates are alternative readings of one event, not a 17-year war. Fix: Set to 669 and add a sentence to the note keeping the c. 686 reading.
  - `/keyframe_review/3 and /keyframe_review/4/correction` [for the author]: The 612 and 666 shapes are kept whole, so the Galuh country east of the Citarum is drawn as Tarumanagara's direct land in 612-669. The ledger (/ledger/3 vassal_start 612, /ledger/4 vassal_end 669) makes it a vassal, and galuh-kingdom_612 draws the same land as Galuh's own. Evidence: Grid check in the author's notes: Tarumanagara 612-673 is exactly Cliopatria's Galuh 674 plus Sunda 674. galuh-kingdom.json keyframe 0 holds the Galuh 674 shape from 612, so the land is drawn twice and in two colours. Fix: Keyframe 3: verdict adjust, correction {"minus": [{"cliopatria": "Tarumanagara", "year": 612}, {"cliopatria": "Galuh Kingdom", "year": 674}], "text": "direct land west of the Citarum; Galuh, east of it, is a vassal 612-669 (ledger) with its own shape"}. Keyframe 4: the same minus on the 666 shape, for 666-669.
- Thin (for a gap-filler):
  - `/ledger/1`: The 534 widening (17,409 to 33,369 km2) is at confidence 1, on Cliopatria's year. The page dates Suryawarman (535-561) 'establish[ing] a new capital city eastward', which could carry the event at 535 at confidence 2. Try https://en.wikipedia.org/wiki/Tarumanagara

### galuh-kingdom: thin
- Area: infobox None (None), Cliopatria 36212.3, ratio None; No infobox area.
- Spot checks: /ledger/1 confirmed (Galuh_Kingdom); /ledger/2 confirmed (Galuh_Kingdom); /ledger/3 confirmed (Galuh_Kingdom); /ledger/8 confirmed (Sunda_Kingdom); /ledger/9 confirmed (Galuh_Kingdom)
- Fixes:
  - `/identity/capitals` [for the author]: Galuh's capital dots run without a break from 612 to 1482 (Karangkamulyan 612-1199, Kawali 1200-1482). Yet the ledger leaves Galuh with no land in 825-895 (/ledger/4) and 1028-1474 (/ledger/6), so a dot is drawn for a landless state. From 1371 it also sits on the same spot as Sunda's Kawali capital. Evidence: /ledger/4 loss 825, /ledger/5 gain 896, /ledger/6 loss 1028 and /ledger/8 gain 1475, all to or from sunda-kingdom; sunda-kingdom /identity/capitals/1 is Kawali 1371-1481. Fix: End the capital spans at the losses: Karangkamulyan 612-824 and 896-1027, then Kawali 1475-1482 (Sunda page: Ningrat Kancana ruled Galuh from Kawali 1475-1482). Keep the 13th-century Kawali remark in the note.
  - `/ledger/1` [for the author]: Type 'gain' for 669 re-gains land that Galuh has held since its 612 found event and keyframe 0. It is the vassal's side of Tarumanagara's vassal_end. Evidence: /ledger/0 and /ledger/1 have the same region (Galuh Kingdom 674). tarumanagara /ledger/4 is vassal_end 669 with Galuh as counterpart. Fix: Optional: say in the note that this is independence from Tarumanagara and that the land itself is unchanged. The mirror is accepted as it stands: the found event names the suzerain.
- Thin (for a gap-filler):
  - `/ledger/4`: 825 loss to Sunda: Cliopatria's year at confidence 1. The Galuh page has Galuh 'absorbed and incorporated within the Sunda kingdom around the 10th century', which neither 825 nor 1028 fits. Try https://en.wikipedia.org/wiki/Carita_Parahyangan
  - `/ledger/5`: 896 separation again (confidence 1, page silent). Try https://en.wikipedia.org/wiki/Carita_Parahyangan
  - `/ledger/6`: 1028 union with Sunda (confidence 1). The longest move in the dossier (446 years) has no dated page. Sri Jayabhupati's 1030 inscription is the nearest dated anchor. Try https://en.wikipedia.org/wiki/Sunda_Kingdom
  - `/ledger/7`: Capital move to Kawali dated only 'by the 13th century' (confidence 1). Try https://en.wikipedia.org/wiki/Galuh_Kingdom

### srivijaya: thin
- Area: infobox 1200000 (1200), Cliopatria 456771.7, ratio 0.38; Acknowledged in keyframe_review/7 (and /4): the infobox follows the maximum maritime extent, and the shape is kept as the core.
- Spot checks: /ledger/1 confirmed (Srivijaya); /ledger/2 confirmed (region broader than the page; confidence lowered to 2) (Kota_Kapur_inscription); /ledger/3 confirmed (Melayu_Kingdom); /ledger/5 confirmed (Chola_invasion_of_Srivijaya); /ledger/10 confirmed (Melayu_Kingdom); /ledger/11 confirmed for the date; page does not name Palembang or Srivijaya (confidence lowered to 2) (Pamalayu)
- Fixes:
  - `/ledger/11/confidence` [applied by reviewer]: Confidence 3 on a Palembang occupation_end, but the cited page names neither Palembang nor Srivijaya. Evidence: Pamalayu page: 'the expedition returned to Java on 3 May 1293'. Neither 'Palembang' nor 'Srivijaya' appears on the page (checked). Fix: Confidence 2.
  - `/ledger/2/confidence` [applied by reviewer]: Confidence 3 for the whole of Jambi province plus Bangka-Belitung. The page names only 'the hinterland of Jambi and the island of Bangka', so the region is the author's reading. Evidence: Kota Kapur inscription page: Coedes, Srivijaya 'had just conquered the hinterland of Jambi and the island of Bangka' (608 Saka, 28 February 686). Fix: Confidence 2.
  - `/ledger/1/counterpart` [for the author]: The free-text counterpart 'Kedah (Kadaram), pre-1139' should be the slug the author proposes in counterparts_needing_dossiers. Evidence: Author's report: suggested_slug kedah-kingdom. Fix: counterpart 'kedah-kingdom'.
  - `/ledger/2 and /ledger/3` [for the author]: Jambi is gained twice: in 686 (region admin1 Jambi, counterpart nobody) and again in 692 (merge, region admin1 Jambi, counterpart melayu-kingdom). The 682 shape (bbox from 101.87E) already holds most of Jambi from 682. Evidence: Srivijaya page: Kedukan Bukit (605 Saka, 683) has Dapunta Hyang lead '20,000 troops ... to Jambi and Palembang'. The Melayu infobox has 'Annexed by Srivijaya: 692'. The Srivijaya page has Melayu integrated 'possibly ... in the 680s'. Fix: Add a 682 gain (confidence 2, Srivijaya page, Kedukan Bukit) for the 682 shape's new land, which explains keyframe 2. Narrow /ledger/2 to Bangka, with the Jambi hinterland in text. Make /ledger/3 the merge of the Melayu polity, not a second gain of the same province.
  - `/ledger/4 and /ledger/8` [for the author]: The Isthmus strip (the 718 shape's land north of 7.0N, Ligor/Chaiya) is Tambralinga's land. tambralinga.json has Srivijaya occupying it 775-969 (confidence 2, Tambralinga page); this dossier has it gained in 718 from 'langkasuka' and lost in 1139 (both confidence 1, Cliopatria's years). Langkasuka (Pattani, below 7N) already lies inside the 692 shape. Evidence: tambralinga.json /ledger/1 occupation_start 775 and /ledger/4 occupation_end 969, counterpart srivijaya: 'Formed Srivijaya Empire: 775-969', 'Late Independent: 970-1277'. shapes.csv: srivijaya_692 reaches 7.036N, srivijaya_718 9.865N. The author flagged this and left the choice to the reviewer: prefer the Tambralinga page. Fix: Retype /ledger/4 as occupation_start 775, counterpart tambralinga, confidence 2 (or gain 775 if Srivijaya is read as annexing). Move /ledger/8 to 969 (occupation_end or loss, counterpart tambralinga). Mark srivijaya_718 adjust (without the strip before 775) and srivijaya_860 adjust with a new keyframe 970-1138 without it. Kedah stays to 1138.
  - `/identity/successors` [for the author]: The infobox successor, the Melayu Kingdom, is missing. Evidence: Srivijaya infobox: successor 'Melayu Kingdom'. The ledger already has Jambi leaving in 1202. Fix: Add melayu-kingdom (Jambi) as a successor, or say in the notes why it is left out.
  - `/ledger/9/note` [for the author]: The note does not record that the Melayu page's infobox gives 'Independence restored: 1028' and its text says Jambi had 'broken away' by the end of the 12th century. Evidence: Melayu Kingdom page infobox and text. Fix: Add both to the note. 1202 can stay at confidence 2 on the Srivijaya page's 'early 13th century'.
- Thin (for a gap-filler):
  - `/keyframe_review/3`: The 692 shape adds about 313,000 km2 (the peninsula from Johor to 7N, plus central Sumatra and Riau), but the 692 ledger event's region is Jambi only and the 685 Kedah gain is about 9,500 km2. No event explains the peninsula south of Kedah or central Sumatra. Try https://en.wikipedia.org/wiki/Langkasuka
  - `/ledger/4`: 718 gain at confidence 1 (see the Tambralinga fix). The Ligor inscription (c. 775) dates the Isthmus. Try https://en.wikipedia.org/wiki/Tambralinga
  - `/ledger/7`: 1139 Kedah loss at confidence 1 (Cliopatria's year). The Chola page says Kedah 'disappeared from Indian sources' after c. 1120. Try https://en.wikipedia.org/wiki/Kedah_Sultanate
  - `/ledger/8`: 1139 loss of the strip at confidence 1. The Tambralinga page gives 969/970. Try https://en.wikipedia.org/wiki/Tambralinga
  - `/ledger/12`: Dissolve 1293 at confidence 1 (Cliopatria's year). The pages give disintegration after 1025, 'weak remains' in 1275 (Singhasari page) and Majapahit ending 'efforts to revive Srivijaya' in 1377 (Melayu page). Try https://en.wikipedia.org/wiki/Melayu_Kingdom

### sunda-kingdom: fix
- Area: infobox None (None), Cliopatria 121224.6, ratio None; No infobox area. The 121,225 km2 shape (732-740) is corrected to Sunda alone.
- Spot checks: /ledger/5 confirmed (Sunda_Kingdom); /ledger/7 confirmed (Sunda_Kingdom); /ledger/8 confirmed (Sultanate_of_Cirebon); /ledger/10 confirmed (Sunda_Kingdom); /ledger/12 confirmed (Sunda_Kingdom); /ledger/11 not on page (quote); fixed at confidence 1 (Sunda_Kingdom)
- Fixes:
  - `/ledger/11` [applied by reviewer]: The note quotes the Sunda page as 'The Banten conquest began in the 1570s', which is not on the page. The year 1572 is Cliopatria's, yet the event was at confidence 2. Evidence: Sunda Kingdom page, read twice: neither '1570s' nor '1572' occurs. It has 'The kingdom has fallen apart, particularly after 1576 due to constant pressure from Banten' and 'finally collapsed completely in 1579'. The Banten page has Banten comprising 'all of Sunda, except for Cirebon and Sumedang Larang' at Hasanuddin's death (1570). Fix: Confidence 1; the note rewritten with the pages' actual sentences.
  - `/keyframe_review/13/note` [applied by reviewer]: The same unsupported 'Banten conquest beginning in the 1570s' attributed to the Sunda page. Evidence: As above. Fix: Replaced with the page's 'particularly after 1576 due to constant pressure from Banten'.
  - `/identity/capitals/1` [for the author]: Kawali is Sunda's capital until 1481, but in 1475-1481 Sunda alone (Susuk Tunggal) ruled from Pakuan. Kawali (108.37E) lies outside the 1475 Sunda shape (bbox 105.37-107.51E). Evidence: Sunda page rulers table: Susuk Tunggal 1475-1482 ruling Sunda from Pakuan; Ningrat Kancana (Galuh) 1475-1482 from Kawali. shapes.csv sunda-kingdom_1475 bbox. Fix: Kawali 1371-1474; Pakuan from 1475. Add a 1475 capital_move, or say in /ledger/7's note that the 1482 move is the united court's.
  - `/keyframe_review/11` [for the author]: The 1519 shape keeps Banten and Sunda Kalapa to 1528, but the ledger loses both in 1527. Evidence: /ledger/9 and /ledger/10 are at 1527; sunda-kingdom_1529 starts in 1529. Fix: Mark 1519 adjust for 1519-1526, or start the corrected 1529 shape (keyframe 12) at 1527.
- Thin (for a gap-filler):
  - `/ledger/1`: 825 union with Galuh (confidence 1, Cliopatria's year; unverified within the page budget). Try https://en.wikipedia.org/wiki/Carita_Parahyangan
  - `/ledger/2`: 896 separation (confidence 1). Try https://en.wikipedia.org/wiki/Carita_Parahyangan
  - `/ledger/3`: 1028 union (confidence 1). Try https://en.wikipedia.org/wiki/Sunda_Kingdom
  - `/ledger/11`: 1572 loss of the west, now at confidence 1. Maulana Yusuf's campaign has no year on the pages opened. Try https://en.wikipedia.org/wiki/Banten_Sultanate

### mataram-kingdom: fix
- Area: infobox None (None), Cliopatria 59609.7, ratio None; No infobox area.
- Spot checks: /ledger/0 confirmed (Mataram_Kingdom); /ledger/3 confirmed (accession date; the conquest itself undated, so confidence 1 is right) (Mataram_Kingdom); /ledger/4 confirmed (Mataram_Kingdom); /ledger/8 confirmed (Mataram_Kingdom); /ledger/2 confirmed (Galuh_Kingdom)
- Fixes:
  - `/wars/2/to` [applied by reviewer]: The Wurawari revolt war ran to 1017, past the state's end in 1016. Evidence: Mataram page: the Pucangan inscription dates the revolt 1016-1017; the infobox ends the kingdom in 1016. Fix: Set to 1016 and add a sentence to the note keeping the 1016-1017 span.
  - `/identity/rulers` [for the author]: The ruler strip stops at Wawa (924-929), although the state lasts to 1016, and has gaps 746-760, 850-855 and 885-898. Evidence: Mataram infobox: '985 AD-1016 (last)' (Dharmawangsa); the page names Mpu Sindok from c. 929. Fix: Add Sindok to Dharmawangsa from the page, or say in the notes that the strip is partial.
  - `/notes` [for the author]: data/README.md lists 'Mataram Kingdom / Mataram Sultanate' among near-duplicate Names, and the dossier does not say they are different states. Evidence: history/data/README.md, 'Duplicate or near-duplicate Names'. Fix: Add one sentence to the notes: the Mataram Sultanate (16th-18th c., se-02) is a different state.
- Thin (for a gap-filler):
  - `/ledger/3`: 898 East Java gain is at confidence 1 on Balitung's accession (10 May 898, confirmed). The page has him 'incorporat[ing] parts of east Java' without a year. Try https://en.wikipedia.org/wiki/Balitung
  - `/ledger/6`: 990 Bali vassal_start at confidence 1. The Mataram page has Bali 'probably as vassal'; the year is a bridge. Try https://en.wikipedia.org/wiki/Udayana_Warmadewa
  - `/ledger/7`: 1016 Bali vassal_end at confidence 1 (page silent). Try https://en.wikipedia.org/wiki/Udayana_Warmadewa

### early-balinese-kingdoms: pass
- Area: infobox None (None), Cliopatria 7748.1, ratio None; No infobox area; the island fixes the land.
- Spot checks: /ledger/0 confirmed (Bali_Kingdom); /ledger/1 confirmed (Singhasari); /ledger/3 confirmed (Majapahit); /ledger/4 confirmed (Majapahit); /ledger/6 confirmed (Bali_Kingdom)
- Thin (for a gap-filler):
  - `/ledger/2`: 1293 regained independence is at confidence 1, but the Bali Kingdom page (already in sources) says 'After the 1292 rebellion and the fall of Singhasari, Java could not assert its rule over Bali'. It can be cited at confidence 2. Try https://en.wikipedia.org/wiki/Bali_Kingdom

### What I tried and could not break (early-balinese-kingdoms)

914 (Belanjong pillar, infobox 13 or 27 February 914), 1284 (the Singhasari page states the Pabali integration as fact), 1342-1343 (Majapahit page: seven months of battles, Bedulu taken in 1343) and the 1343 vassal phase (infobox) all confirmed. Bedulu lies inside the bbox. The shared Wikidata id with the Balinese Kingdom is handled in the notes. Optional: the capital dot runs through 1284-1292, when the dossier gives Bali no land.

## Cross-dossier matrix

- tarumanagara 612 vassal_start -> galuh-kingdom | mirror: galuh-kingdom 612 found | **matched** Vassal events live in the suzerain's ledger; Galuh's found names tarumanagara. The shapes overlap 612-669 (see the tarumanagara keyframes fix).
- tarumanagara 669 vassal_end -> galuh-kingdom | mirror: galuh-kingdom 669 gain | **matched** Galuh records independence as a gain of its own land.
- tarumanagara 669 dissolve -> sunda-kingdom | mirror: sunda-kingdom 670 found | **matched** 
- galuh-kingdom 723 loss -> mataram-kingdom | mirror: mataram-kingdom 723 gain | **matched** 
- galuh-kingdom 739 gain -> mataram-kingdom | mirror: mataram-kingdom 739 loss | **matched** 
- galuh-kingdom 825 loss -> sunda-kingdom | mirror: sunda-kingdom 825 gain | **matched** Both at confidence 1 (Cliopatria's year).
- galuh-kingdom 896 gain -> sunda-kingdom | mirror: sunda-kingdom 896 loss | **matched** Both at confidence 1.
- galuh-kingdom 1028 loss -> sunda-kingdom | mirror: sunda-kingdom 1028 gain | **matched** Both at confidence 1.
- sunda-kingdom 1475 split -> galuh-kingdom | mirror: galuh-kingdom 1475 gain | **matched** 
- sunda-kingdom 1482 gain -> galuh-kingdom | mirror: galuh-kingdom 1482 dissolve | **matched** 
- sunda-kingdom 1482 loss -> sultanate-of-cirebon | mirror: - | **exception** counterpart owned by a group that has not run yet (se-02 part); Cirebon's infobox says 1479 and its body 2 April 1482.
- sunda-kingdom 1527 loss -> sultanate-of-banten | mirror: - | **exception** counterpart owned by a group that has not run yet (se-02 part); Banten's infobox: 'Syarif Hidayatullah conquered Banten: 1526', 'Conquest of the Sunda Kingdom: 1527'.
- sunda-kingdom 1527 loss -> demak-sultanate | mirror: - | **exception** counterpart owned by a group that has not run yet (se-02 part)
- sunda-kingdom 1572 loss -> sultanate-of-banten | mirror: - | **exception** counterpart owned by a group that has not run yet (se-02 part); year is Cliopatria's (confidence 1).
- sunda-kingdom 1579 loss -> sultanate-of-banten | mirror: - | **exception** counterpart owned by a group that has not run yet (se-02 part)
- mataram-kingdom 990 vassal_start -> early-balinese-kingdoms | mirror: early-balinese-kingdoms None None | **exception** Vassal events live in the suzerain's ledger. Bali's keyframe 2 names Mataram (to 1016) as probable suzerain; the Bali page: 'either Bali had allied with East Java, or Bali was Java's vassal'.
- mataram-kingdom 1016 vassal_end -> early-balinese-kingdoms | mirror: early-balinese-kingdoms None None | **exception** As above.
- mataram-kingdom 1016 dissolve -> kahuripan | mirror: - | **exception** counterpart owned by a group that has not run yet (se-02 part)
- srivijaya 685 gain -> Kedah (Kadaram), pre-1139 | mirror: - | **exception** No dossier; listed as kedah-kingdom in counterparts_needing_dossiers (se-02-x).
- srivijaya 686 gain -> nobody | mirror: - | **exception** Counterpart nobody, but the Jambi half of the region is gained again in 692 from melayu-kingdom (see the fix).
- srivijaya 692 merge -> melayu-kingdom | mirror: - | **exception** melayu-kingdom needs a dossier (se-02-x).
- srivijaya 718 gain -> langkasuka | mirror: tambralinga 775 occupation_start | **mismatch** The 718 delta (7.0-9.9N, Ligor/Chaiya) is Tambralinga's land. tambralinga.json /ledger/1 has Srivijaya occupying it from 775 (confidence 2); Srivijaya has it from 718 (confidence 1), 57 years apart.
- srivijaya 1139 loss -> tambralinga | mirror: tambralinga 969 occupation_end | **mismatch** tambralinga.json /ledger/4: independence 969/970 (confidence 2) against 1139 here (confidence 1), 170 years apart. Srivijaya should move.
- srivijaya 1139 loss -> sultanate-of-kedah | mirror: - | **exception** counterpart owned by a group that has not run yet (se-02 part)
- srivijaya 1202 loss -> melayu-kingdom | mirror: - | **exception** No dossier yet (se-02-x). The Melayu infobox says 'Independence restored: 1028'.
- srivijaya 1288 occupation_start -> singhasari | mirror: - | **exception** counterpart owned by a group that has not run yet (se-02 part)
- srivijaya 1293 occupation_end -> singhasari | mirror: - | **exception** counterpart owned by a group that has not run yet (se-02 part)
- srivijaya 1293 dissolve -> majapahit | mirror: - | **exception** counterpart owned by a group that has not run yet (se-02 part)
- early-balinese-kingdoms 1284 loss -> singhasari | mirror: - | **exception** counterpart owned by a group that has not run yet (se-02 part); the Singhasari page states the 1284 integration of Bali as fact.
- early-balinese-kingdoms 1293 gain -> singhasari | mirror: - | **exception** counterpart owned by a group that has not run yet (se-02 part)
- early-balinese-kingdoms 1343 loss -> majapahit | mirror: - | **exception** counterpart owned by a group that has not run yet (se-02 part); Majapahit should carry Bali as a vassal 1343-1478.
- water-chenla 780 contest_start -> srivijaya | mirror: srivijaya None None | **missing** Not in Srivijaya, and should not be: the Water Chenla page names 'the Javanese Shailendra dynasty'. water-chenla.json (se-01) should point at sailendra-dynasty (needs a dossier, se-02-x) or mataram-kingdom. The same applies to its 790 contest_end, its 790 dissolve and its successors entry.
- khmer-empire 803 gain -> srivijaya | mirror: srivijaya None None | **missing** Confidence 1. The land (Water Chenla) was never in a Srivijaya shape; route to se-01: the counterpart should be the Javanese Sailendra, not srivijaya.

## Routing

- se-01 (water-chenla, khmer-empire): the 780-790 Javanese attack and the 803 Khmer gain name srivijaya. The Water Chenla page says 'the Javanese Shailendra dynasty', so point them at sailendra-dynasty (se-02-x) or mataram-kingdom, not srivijaya.
- se-02 parts not run: Majapahit should carry Bali (vassal 1343-1478), Palembang 1377 and the post-1293 Sumatran land. Kahuripan should not draw Bali 1028-1045 as direct land (the Bali dossier keeps it). Banten, Cirebon and Demak should mirror the Sunda losses of 1482, 1527, 1572 and 1579.
- se-02-x: melayu-kingdom, kedah-kingdom, langkasuka, kantoli, sumedang-larang, sailendra-dynasty.

## Problems

- No Context polity in section 6 of the author's brief has a dossier yet (majapahit, kediri-kingdom, sultanate-of-kedah, sultanate-of-cirebon, kingdom-of-janggala, singhasari, sultanate-of-banten, demak-sultanate, sultanate-of-malacca, kahuripan, kingdom-of-pajana): all count as counterparts owned by a group that has not run yet. Cross-checked instead against tambralinga, water-chenla and khmer-empire, which name srivijaya.
- Reviewer edits (orchestrator's small-fix rule), all re-validated with 0 errors and read back: tarumanagara /wars/0/to 686->669; srivijaya /ledger/2 and /ledger/11 confidence 3->2; sunda-kingdom /ledger/11 confidence 2->1 with its quote corrected, and /keyframe_review/13/note quote corrected; mataram-kingdom /wars/2/to 1017->1016.
- WebFetch answers through a summariser. The Sunda '1570s' quote was checked twice with different prompts before it was judged not on the page.
- The Tarumanagara invasion (infobox 669) comes before Srivijaya's founding (c. 671, Srivijaya infobox). The conflict is in the pages; both dates are noted in the dossiers.
