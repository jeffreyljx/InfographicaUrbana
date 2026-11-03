# Review of batch sa-03-d (pala-empire, rashtrakuta-dynasty), 2026-10-19

Validator: both dossiers valid, 0 errors; warnings only for placeholder counterpart slugs. Area: neither infobox gives an area (checked), so no ratio. Keyframe walk done on the gazetteer grid (land cells, 252.9 km2 each). Spot checks: 7 Pala and 6 Rashtrakuta events; every confidence-3 event checked was confirmed on its page with the year. Both dossiers fail on unexplained keyframe changes and missing mirror events, not on fabrication.

## pala-empire: fail

### Fixes (all for the author)

- `/keyframe_review/14/correction`: The 947 correction (Cliopatria 947 minus Bangladesh) also drops 82,951 km2 outside Bangladesh (51,592 km2 of it in Bihar: north Bihar above 25.6 N and a western strip), and no ledger event loses it; /ledger/12 and /ledger/13 explain only the 106,977 km2 inside Bangladesh.
  - Evidence: Gazetteer: K13 (900 shape) 306,009 km2, K14 116,081 km2, loss 189,928 km2, of which 106,977 in Bangladesh. The note justifies only the Kamboja and Chandra losses; the Pala page says Mahipala I recovered 'northern and eastern Bengal', nothing about Bihar.
  - Fix: Make K14 and K15 {"minus": [{"cliopatria": "Pala Empire", "year": 900}, {"country": "Bangladesh"}]} (the core minus the Kamboja and Chandra losses), or add a dated loss of north Bihar with counterpart and page.
- `/keyframe_review/16`: K16 (Cliopatria 980 shape, ok, 72,582 km2 for 978-980) loses a further 43,246 km2 of south-west Bengal (bbox 86.4-90.9 E, 21.7-25.4 N) against K15 with no event, and the 981 keyframe gains 164,385 km2 of which /ledger/14 and /ledger/15 explain only 65,248.
  - Evidence: The author's own reading (Pala page: Mahipala I 'recovered northern and eastern Bengal within three years of ascending the throne in 978 CE') leaves Radha in Pala hands; nothing on the pages opened takes it away in 978-980.
  - Fix: Set K16 verdict adjust with the same correction as K14/K15, so the 981 change is exactly /ledger/14 + /ledger/15; recheck K17 against the 1000 shape.
- `/keyframe_review/20`: 1000 to 1056 the shape grows 25,796 km2 (11,128 km2 in Bangladesh, the rest north Bengal and Meghalaya edge) with no ledger event; kamarupa-kingdom /ledger/22 records a 1056 loss with counterpart pala-empire for exactly this.
  - Evidence: Gazetteer: K19 236,967 km2, K20 261,752 km2. kamarupa-kingdom /ledger/22: '1056: the west of the Kamarupa shape falls to the Pala shape' (c1).
  - Fix: Add {year 1056, type gain, counterpart kamarupa-kingdom, region minus(Pala 1056, Pala 1000), confidence 1, source Pala_Empire, note: Cliopatria's year, mirror of kamarupa-kingdom /ledger/22}, or mark K20 adjust to the 1000 shape and tell the Kamarupa author.
- `/ledger/16`: The 1072 loss to the Kaivarta rebels takes all of Bengal (141,371 km2): 29,842 km2 of West Bengal (Radha) and 76,376 km2 of Bangladesh, most of it east Bengal, not Varendra.
  - Evidence: Ramapala page: 'At the very beginning, Ramapala reigned over a small territory comprising part of Magadha and Radha.' Pala page: the Kaivarta revolt occupied 'the Varendra region'; 'The Varmans occupied eastern Bengal during his reign' (Vigrahapala III, 1043-1070 in the ruler strip).
  - Fix: Restrict /ledger/16 to Varendra (intersect Pala 1056 with union(Rajshahi, Rangpur)); make /keyframe_review/21 adjust = union(Pala 1072, West Bengal); add a loss of east Bengal to the Varmans inside Vigrahapala III's reign (c1, source Pala_Empire, counterpart listed under counterparts_needing_dossiers).
- `/ledger/18`: The 1085 gain from the Kaivartas includes West Bengal (Radha), which the Ramapala page says Ramapala held from the start.
  - Evidence: Ramapala page: 'a small territory comprising part of Magadha and Radha'; Pala page: the rebels held 'the Varendra region'.
  - Fix: Region = union(Rajshahi, Rangpur) (Varendra) only; Radha stays in the keyframes from 1072.
- `/keyframe_review/22`: 1072 to 1085 Cliopatria drops 33,636 km2 (24,531 km2 in Bihar; bbox 83.3-87.1 E, 23.6-27.4 N, north Bihar) and the K22 correction keeps the drop, but no event loses it.
  - Evidence: Pala page: Ramapala 'lost Mithila to a Karnat chief named Nanyadeva' (undated). The author's notes list it as undated and left it out, yet the keyframe drops the land.
  - Fix: Add a loss of Mithila (north Bihar) at confidence 1, counterpart 'Karnat dynasty of Mithila' (list it), year 1085 (Cliopatria) or a bridge in Ramapala's reign, source Pala_Empire; or keep north Bihar in the K22 correction until a dated loss.
- `/ledger/19`: The 1159 loss to the Senas covers 110,264 km2, of which only 17,703 km2 lies inside the Pala keyframe it removes land from (K25 correction); the rest is east Bengal (Vanga), which this dossier's own keyframes no longer hold after 1072.
  - Evidence: Sena page: 'their territory had expanded to include Vanga and a part of Varendra by the end of Vijayasena's reign' (r. 1096-1159); it does not say Vanga was taken from the Palas. Pala page: the Varmans held east Bengal and Ramapala only 'forced the Varman king of east Bengal to accept his suzerainty'.
  - Fix: Region = the Varendra part only, e.g. intersect(K25 correction, Rajshahi), text 'a part of Varendra'.
- `/ledger`: Ramapala's conquest of western Kamarupa and its loss are missing: kamarupa-kingdom /ledger/26 (1100 loss, counterpart pala-empire, c2) and /ledger/27 (1126 gain from pala-empire, c2) have no mirror here.
  - Evidence: Pala page and Ramapala page: 'He brought Kamarupa and Rar under his control'; Pala page: Vaidyadeva 'practically created a separate kingdom' after Kumarapala's death.
  - Fix: Add 1100 gain (or vassal_start) and 1126 loss (or vassal_end) with counterpart kamarupa-kingdom, region as in the Kamarupa dossier, c1, source Pala_Empire; add the land to K22/K23 corrections if drawn as direct.
- `/ledger/10`: vassal_end of Utkala (and /ledger/11 of Kamarupa) dated 840, inside Devapala's reign; the Pala page puts the loss under Narayanapala. kamarupa-kingdom /ledger/15 ends it in 860.
  - Evidence: Pala page: 'Narayanapala lost control of Assam and Orissa'; Narayanapala 873-927 in the dossier's ruler strip (Ganguly), 860-917 Sircar.
  - Fix: Move /ledger/10 and /ledger/11 to 860 (Sircar, matching kamarupa-kingdom) or 873 (the strip), quote the sentence, keep confidence 1.
- `/ledger/9`: vassal_start of Kamarupa in 825 against kamarupa-kingdom /ledger/14 in 810: 15 years apart.
  - Evidence: Both are bridges inside Devapala's reign (Pala page: 'Pragjyotisa or Assam accepted the suzerainty of Devapala', reign 810-850 Majumdar, 806-845 Ganguly).
  - Fix: Agree a year with the Kamarupa author (810, Devapala's accession by Majumdar, or 825).
- `/ledger/8`: Counterpart 'Utkala (Odisha)' (/ledger/8, /ledger/10) is neither a slug nor in the report's counterparts_needing_dossiers.
  - Evidence: Report counterparts_needing_dossiers lists Ayudha, Kamboja, Kaivarta etc. but not Utkala; notes mention it only in passing.
  - Fix: Name the Odisha state (Bhauma-Kara dynasty) and list it under counterparts_needing_dossiers, or use 'nobody'.

### Thin (for a gap-filler)

- `/ledger/1`: 778 Bihar gain (194,227 km2) is Cliopatria's year at confidence 1, counterpart nobody (try https://en.wikipedia.org/wiki/Khalimpur_copper_plate)
- `/ledger/8`: Utkala and Kamarupa vassalage years (825-840/860), confidence 1 (try https://en.wikipedia.org/wiki/Bhauma-Kara_dynasty)
- `/ledger/12`: Kamboja and Chandra take-over of Varendra and east Bengal at Cliopatria's 947, confidence 1 (try https://en.wikipedia.org/wiki/Chandra_dynasty)
- `/ledger/16`: Varendra rebellion start and end (1072, 1085 are bridges, confidence 1) (try https://en.wikipedia.org/wiki/Varendra_Rebellion)
- `/ledger/17`: Ramavati founding year and site (confidence 1) (try https://en.wikipedia.org/wiki/Ramavati)
- `/ledger`: Ramapala's suzerainty over the Varman king of east Bengal (Pala page, undated) has no vassal_start (try https://en.wikipedia.org/wiki/Varman_dynasty_(Bengal))
- `/keyframe_review/23`: 1111 +14,162 km2, 1147 -14,162 km2, 1152 -13,151 km2 (Cliopatria) with no events; small, but Madanapala's Munger capture and the Gahadavala frontier are undated (try https://en.wikipedia.org/wiki/Gahadavala_dynasty)

### Spot checks

- `/ledger/0` https://en.wikipedia.org/wiki/Pala_Empire: confirmed ('Gopala's ascension in 750 CE'; infobox Established 750)
- `/ledger/3` https://en.wikipedia.org/wiki/Tripartite_struggle: confirmed ('He thus returned to the South in 790')
- `/ledger/4` https://en.wikipedia.org/wiki/Tripartite_struggle: confirmed ('invading the kingdom of Kannauj around 791'; Chakrayudha 'as his vassal')
- `/ledger/7` https://en.wikipedia.org/wiki/Tripartite_struggle: confirmed ('In 816, Nagabhata II invaded the Doab, and defeated king Chakrayudha')
- `/ledger/14` https://en.wikipedia.org/wiki/Pala_Empire: confirmed ('recovered northern and eastern Bengal within three years of ascending the throne in 978 CE'; Gauda 'lost to the Kambojas')
- `/ledger/16` https://en.wikipedia.org/wiki/Ramapala: confirmed undated as the note says; region contradicts the page (Radha held by Ramapala from the start)
- `/ledger/19` https://en.wikipedia.org/wiki/Sena_dynasty: confirmed for the year (Vijayasena r. 1096-1159, 'Vanga and a part of Varendra'); the page does not say Vanga was Pala

## rashtrakuta-dynasty: fail

### Fixes (all for the author)

- `/keyframe_review/11`: 850 to 860 Gujarat leaves the shape (107,988 km2; 105,459 km2 in Gujarat, 99.8 percent inside Cliopatria's Gurjara-Pratihara 860 shape) and no ledger event loses it.
  - Evidence: Gazetteer: K10 897,542 km2, K11 790,060 km2. gurjara-pratihara-dynasty /ledger/20: '860: Bhoja's Gujarat, as Cliopatria draws it', a gain with counterpart rashtrakuta-dynasty. The K11 note only says the vassal tint continues.
  - Fix: Add {year 860, type loss, counterpart gurjara-pratihara-dynasty, region minus(Rashtrakuta 850, Rashtrakuta 860), confidence 1, source https://en.wikipedia.org/wiki/Gurjara-Pratihara_dynasty (add to sources)}, and end or explain the Gujarat vassal tint (/ledger/18-/ledger/25) over Pratihara-held land after 860.
- `/ledger/25/note`: Year 888 is on the page, but the cited Dynasty page says the branch ended by being brought under direct Rashtrakuta rule, while the note relies on the Gurjara-Pratihara page (not in sources[]) for an 'extermination'.
  - Evidence: Rashtrakuta dynasty page: 'Rashtrakutas of Gujarat (757-888)'; Krishna II 'ended the independent status of the Gujarat branch and brought it under direct control from Manyakheta'.
  - Fix: Quote the Dynasty sentence; say why no 888 gain of Gujarat is drawn (Cliopatria and the Pratihara page give Gujarat to Bhoja from 860); add the Gurjara-Pratihara page to sources if it stays quoted.
- `/ledger/33/counterpart`: The 982 dissolve hands Indra IV's remnant to western-chalukya-empire, but the remnant (Cliopatria 980 shape, 22,508 km2) lies wholly in the Mysore region (Gangavadi) and nowhere in Cliopatria's Western Chalukya 980 shape.
  - Evidence: Tailapa II page: he consolidated 'the western Deccan region between the Narmada and the Tungabhadra rivers'; Indra IV and 'the Ganga chief Marasimha' opposed him. western-ganga-dynasty holds Gangavadi to 998 (/ledger/12, Chola).
  - Fix: Counterpart western-ganga-dynasty (or nobody), with the /keyframe_review/19 and /keyframe_review/20 text saying the remnant stood in Ganga country.
- `/ledger/2`: Gangavadi is direct Rashtrakuta land 757-972 here (gain 757, c1; contest 816-821), but western-ganga-dynasty has /ledger/8 780 occupation_start, /ledger/9 819 occupation_end, /ledger/10 819 vassal_start and /ledger/11 982 vassal_end, all with counterpart rashtrakuta-dynasty and no mirror here.
  - Evidence: Krishna I page: 'acquired territory in Gangavadi' (undated, reign 756-774); the Ganga page via the WG dossier: 'by 819, a Ganga resurgence gained them partial control over Gangavadi'; Rashtrakuta page calls the Gangas 'their loyal feudatory'.
  - Fix: Agree with the western-ganga-dynasty author: either add 819 loss + vassal_start and 982 vassal_end (and drop the Mysore region from K8-K17 from 819), or keep direct rule and have the WG dossier record a loss; align 757 vs 780.
- `/ledger/5`: Counterpart 'rulers of Kalinga and Kosala' (/ledger/5, /ledger/24) is free text and not listed under counterparts_needing_dossiers.
  - Evidence: Report's counterparts_needing_dossiers omits it; validator does not flag free text.
  - Fix: Use 'nobody' or name the states (Bhauma-Kara dynasty of Utkala, Somavamshis of Kosala) and list them.
- `/ledger/13`: contest_end 800 (and /ledger/27 917) disagree with gurjara-pratihara-dynasty /ledger/15 (814) and /ledger/24 (926).
  - Evidence: GP: '814: Govinda III dies and the Rashtrakuta threat ends'; '926: Kannauj is back in Pratihara hands' (Cliopatria). All four are confidence 1-2 bridges.
  - Fix: Align each pair within a year with the Pratihara author.
- `/ledger/6`: Vengi is drawn as direct land from 772 (/ledger/4, K3-K9) and also as a vassal tint from 784 (/ledger/6) over the same Vijayawada disc until 850.
  - Evidence: Krishna I page names only Vishnuvardhana IV, not Vengi; Dynasty page: Dhruva 'brought the Eastern Chalukyas and Gangas of Talakad under his control'.
  - Fix: Choose one: direct (drop /ledger/6 and /ledger/23) or vassal (drop /ledger/4 and /ledger/22, adjust K3-K9).

### Thin (for a gap-filler)

- `/keyframe_review/17`: 936 to 947 the shape loses 18,462 km2 (16,186 km2 in south Gujarat) with no event; small (try https://en.wikipedia.org/wiki/Lata_(region))
- `/ledger/4`: 772 Vengi, Kalinga, Kosala gains and 850 losses are Cliopatria's years at confidence 1 (try https://en.wikipedia.org/wiki/Eastern_Chalukyas)
- `/ledger/17`: 806 Gujarat gain at confidence 1 (813 inscription only) (try https://en.wikipedia.org/wiki/Govinda_III)
- `/ledger/19`: Manyakheta foundation year (confidence 1) (try https://en.wikipedia.org/wiki/Manyakheta)
- `/ledger/31`: 967 loss of Tondaimandalam at confidence 1 (try https://en.wikipedia.org/wiki/Parantaka_II)
- `/keyframe_review/19`: location of Indra IV's remnant 973-982 (Cliopatria shape kept, confidence 1) (try https://en.wikipedia.org/wiki/Indra_IV)

### Spot checks

- `/ledger/25` https://en.wikipedia.org/wiki/Rashtrakuta_dynasty: confirmed year ('Rashtrakutas of Gujarat (757-888)'); note omits 'brought it under direct control from Manyakheta'
- `/ledger/10` https://en.wikipedia.org/wiki/Tripartite_struggle: confirmed ('He thus returned to the South in 790')
- `/ledger/1` https://en.wikipedia.org/wiki/Krishna_I: confirmed ('defeating the last Badami Chalukya emperor Kirtivarman II in 757', plate of 807)
- `/ledger/32` https://en.wikipedia.org/wiki/Tailapa_II: confirmed ('In 973, Tailapa dethroned Karka and established a new dynasty')
- `/ledger/28` https://en.wikipedia.org/wiki/Krishna_III: confirmed ('Tondaimandalam was secured by 944'; Siddalingamadam plates of 944)
- `/ledger/33` https://en.wikipedia.org/wiki/Rashtrakuta_dynasty: confirmed ('Sallekhana at Shravanabelagola on 20 March 982 CE')

## Cross-dossier matrix (not matched only)

- pala-empire 825 vassal_start cp=Utkala (Odisha) / mirror None None None: **missing**. free-text counterpart not listed for a dossier
- pala-empire 825 vassal_start cp=kamarupa-kingdom / mirror kamarupa-kingdom 810 vassal_start: **mismatch**. 15 years apart; both bridges in Devapala reign
- pala-empire 840 vassal_end cp=kamarupa-kingdom / mirror kamarupa-kingdom 860 vassal_end: **mismatch**. Pala page: Narayanapala lost Assam and Orissa; Pala side should move
- pala-empire 840 vassal_end cp=Utkala (Odisha) / mirror None None None: **missing**. free-text counterpart
- kamarupa-kingdom 1056 loss cp=pala-empire / mirror pala-empire None None: **missing**. Pala K20 grows 25,796 km2 with no event
- kamarupa-kingdom 1100 loss cp=pala-empire / mirror pala-empire None None: **missing**. Ramapala brought Kamarupa under his control (Pala page)
- kamarupa-kingdom 1126 gain cp=pala-empire / mirror pala-empire None None: **missing**. Vaidyadeva
- chalukya-dynasty 750 loss cp=rashtrakuta-dynasty / mirror rashtrakuta-dynasty None None: **mismatch**. before the Rashtrakuta start (753); Chalukya and Rashtrakuta authors to agree whether Dantidurga held Malwa and south Gujarat in 750
- gurjara-pratihara-dynasty 750 contest_start cp=rashtrakuta-dynasty / mirror rashtrakuta-dynasty None None: **mismatch**. GP contest 750-756 predates the Rashtrakuta start 753
- rashtrakuta-dynasty 757 gain cp=western-ganga-dynasty / mirror western-ganga-dynasty 780 occupation_start: **mismatch**. 23 years and type differ; WG also has 819 occupation_end and vassal_start, 982 vassal_end with no mirror
- rashtrakuta-dynasty 772 gain cp=rulers of Kalinga and Kosala / mirror None None None: **missing**. free text, not listed
- rashtrakuta-dynasty 785 vassal_start cp=late-pallava-empire / mirror late-pallava-empire None None: **missing**. no Rashtrakuta event in the Pallava ledger (sa-02)
- rashtrakuta-dynasty 800 contest_end cp=gurjara-pratihara-dynasty / mirror gurjara-pratihara-dynasty 814 contest_end: **mismatch**. 14 years apart
- rashtrakuta-dynasty 805 vassal_end cp=late-pallava-empire / mirror late-pallava-empire None None: **missing**. sa-02
- rashtrakuta-dynasty 850 loss cp=rulers of Kalinga and Kosala / mirror None None None: **missing**. free text
- gurjara-pratihara-dynasty 860 gain cp=rashtrakuta-dynasty / mirror rashtrakuta-dynasty None None: **missing**. Rashtrakuta K11 drops Gujarat with no loss event
- rashtrakuta-dynasty 917 contest_end cp=gurjara-pratihara-dynasty / mirror gurjara-pratihara-dynasty 926 contest_end: **mismatch**. 9 years apart
- rashtrakuta-dynasty 982 dissolve cp=western-chalukya-empire / mirror western-ganga-dynasty 982 vassal_end: **mismatch**. the remnant lies in Gangavadi (WG land to 998), not in the Western Chalukya shape

Matched: the Pala-Rashtrakuta contests of 785, 790 and 800; Rashtrakuta-Chalukya 753 and 757; Rashtrakuta-Pratihara 785/786, 790, 800 starts, 806 Lata and 916. Exceptions: counterparts listed for new dossiers or owned by sa-03 parts not run yet (chandra, sena, chola, western-chalukya).

## Problems

- No dossier edits applied: every finding is a missing event, a region or keyframe correction, or a counterpart choice, none of the small kinds the reviewer may apply.
- western-ganga-dynasty.json exists although not in the author's Context list; it was used as a counterpart (its 780-982 Rashtrakuta events have no mirror here).
- gurjara-pratihara-dynasty uses kannauj-varman-dynasty as the counterpart for Chakrayudha (an Ayudha), while pala-empire uses 'Chakrayudha (Ayudha dynasty of Kannauj)': the orchestrator should pick one slug for the Ayudhas.
- late-pallava-empire (sa-02) has no event for Dhruva's 785 overlordship of Kanchi; route to sa-02.
- chandela-kingdom, chandra-dynasty, sena-dynasty, gahadavala-dynasty, chola-empire, eastern-ganga-kingdom, chaulukya-dynasty, tibetan-empire, western-chalukya-empire have no dossier yet: counterparts treated as 'group not run yet'.
- Gazetteer resolves region 'Vanga' to all of Bengal, so it cannot stand for east Bengal in the fixes.
