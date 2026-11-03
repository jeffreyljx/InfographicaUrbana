# Notes for group sa-02-c (Kushan Empire, Western Satraps, Eastern Kushans, Western Kushans)

Written 2026-10-19. Four dossiers, 39 ledger events, all validate (`python3 -I tools/validate_dossier.py`); only western-satraps has `--resolve` warnings (2, the sub-cell stub shapes). Pages opened: 16 distinct Wikipedia articles, none failed. Page use: kushan-empire 5/5, western-satraps 9/9, eastern-kushans 5/5, western-kushans 2/2.

## The Kushan rows (one state, three dossiers)
- Cliopatria's Kushan Empire (43-237), Eastern Kushans (238-346) and Western Kushans (238-259) share Q25979. The Kushan Empire page says the empire "split into western and eastern halves" after Vasudeva I's death in 225, the western half being "soon subjugated" by the Sasanians. Decision: three dossiers, empire 30-225, halves from 226. The empire's undivided Cliopatria row for 226-237 equals the union of the halves' 238 shapes (7,070 of 7,119 cells), so the two halves get a new keyframe each that holds the 238 outline back to 226. The colour agent should keep all three in one family (the western half is `persia` because the pages make it a Sasanian vassal kingdom).
- Western Kushans = early Kushano-Sasanian Kingdom. All 2,351 cells of the 238-259 shape lie inside Cliopatria's Indo-Sasanian Empire shape of 260 (me-06 owns it). The kidarites dossier uses the slug `kushano-sasanian-kingdom`, which has no dossier; it should resolve to `indo-sasanian-empire`. The Sasanian side should carry `vassal_start` with counterpart `western-kushans` (c. 230).
- The Kushan start is c. 30 (infobox), not 43; Cliopatria's 117-183 shapes carry a strip of the Tarim (Aksu, Kucha, Korla, Karashahr) taken from its Han shape that no page opened supports (only Kashgar, where "the Kushans installed Chenpan as king" in 114-120): corrected to Kashgar as a client kingdom (after the repair the whole strip, 893 cells, is removed from the direct shapes and Kashgar is drawn only by the vassal pair, 117-127).

## Per state: what is not settled
**kushan-empire**
- Capital for 30-90 and the early conquests' years are not on any page opened (Kujula: "after 45 CE", Vima Takto "c. 90-113"). Ledger events at 51, 91 (Punjab and Sindh remainder), 127 (vassal), 150 (vassal end), 161 are confidence 1 (Mathura 91 is confidence 2 after the repair, on the Northern Satraps page).
- Mathura: Cliopatria has it Kushan in 91; the Vima Kadphises page only says he "may have replaced" Sodasa there (113-127).
- Counterpart years disagree with the Indo-Parthian dossier (loss 50, 90) and Indo-Scythian dossier (51, 75, 100) written from other pages.
- Western Satraps as Kushan vassals (127-150 after the repair; was 127-225) is a confidence-1 bridge: the Western Satraps page says 'vassals of the Kushans, at least in the early period until Rudradaman I conquered the Yaudheyas', and the Rabatak inscription, the Chastana statue and the Rudradaman page's suzerains are all undated.
- Kanishka's undated Parthian war and the Han clashes (84, 86 or 90) moved no border.

**western-satraps**
- Start c. 35 (infobox) not 43; end 409 (Chandragupta II page "between 397 and 409") not 415 (infobox) not 489: Cliopatria's two 55 km2 shapes of 476-489 are stubs next to the Maitrakas and are marked wrong. No shape exists for 410-475.
- Nahapana's chronology (24-70, 66-71, 119-124, or ending 78) leaves 43-126 unchecked; Rudradaman's reign (130-150) starts three years after Cliopatria's 127 jump; Nasik and Poona cut out of 127.
- The Junagadh list of 150 (Sindhu-Sauvira, Maru, Kukura) is 120 years earlier than Cliopatria's Satrap Sindh (270) and conflicts with the Kushan shape; an adjudicating page is missing.
- Nasik in the Satrap shape from 224 conflicts with the Abhira kingdom "around Nashik" (Satavahana page); Sanchi-Vidisha "re-established" 255-278 (Rudrasena II) versus held in the shape from 224; Eran possibly Gupta from Samudragupta's time versus held to 409.
- Events 154, 224, 260, 270, 306, 347 are Cliopatria's years with counterparts verified by geometry (453/453 cells into Vakataka, 1,339/1,339 from Eastern Kushans, 1,109/1,112 into Gupta, 230/235 into Yaudheya) but page-silent as to the year: confidence 1.
- No ruler strip (the page's list is partial and overlaps). Minnagara not located; Bharuch is a placeholder capital for 35-77.

**eastern-kushans**
- End 346 is Cliopatria's; the pages say "mid-4th century" (Samudragupta c. 335-375, Kipunada c. 335-350) and have the Kushans keeping their districts under Gupta suzerainty until the Kidarites (c. 390-410). The Gupta dossier should carry the vassal relation.
- 270: the page names only the Gangetic plain; Cliopatria also removes Rajasthan, Haryana and Sindh (1,339 cells to the Satraps).
- Gandhara: split between this shape (to 259) and the Indo-Sasanians (from 260) although the pages give it to the Sasanians by 225 or 240-270.

**western-kushans**
- Whether the western half was independent between 225 and c. 230 is page-silent; the Kushanshah governorship is dated 225, c. 230 and 233 on the same pages. The 259 end is Cliopatria's row change, not an event.

## Counterparts needing dossiers (not written here)
- Nagas of Padmavati (early 3rd century to mid-4th, Pawaya near Gwalior) and Nagas of Vindhyatabi: infobox successors of the Kushans; the Nagas page finds "no concrete evidence" that they defeated the Kushans. Group sa-02-x.
- Kingdom of Kashgar (Shule), client of the Kushans 114-120 onward.
- Abhira dynasty of Nashik (Satavahana successor, 3rd century).

## Region names the gazetteer lacks
None: every region and place name used (Bactria, Sogdia, Gandhara, Kabulistan, Tarim Basin, Kashgar, Nasik, Pune, Malwa, Konkan, Saurashtra, Rajputana, Sindh, Punjab, Gujarat (region), Haryana) resolved. Bharuch (Barygaza) and Minnagara appear only as capital names.

## Repair run (sa-02-c-fixed, 2026-10-19)

Answers the reviewer's findings (history/polities/_notes/review-sa-02-c.md). Pages re-opened: Kushan Empire, Western Satraps, Indo-Parthian Kingdom, Chastana, Kushano-Sasanian Kingdom, Northern Satraps, Shule Kingdom, Abhira dynasty, Huvishka (nine fetches; none failed). kushan-empire, western-satraps and western-kushans re-validated with --resolve (0 errors; warnings: western-satraps 3, western-kushans 1, kushan-empire 0). eastern-kushans untouched (verdict fix, done by the reviewer).

**kushan-empire (was fail)**
- Tarim (blocking): keyframes 117, 127, 154, 161, 165 now subtract the strip itself, {"minus": [Ky, {"minus": [K117, K91]}]}, 893 cells, instead of the Tarim Basin region (704 of the 893). The corrected 165 shape and Cliopatria's 184 differ by 4 cells, so 184 needs no event. Done as the reviewer proposed, except that Kashgar is not added back (next point).
- Kashgar drawn twice: removed from the corrections; the vassal pair draws it. The vassal end moved from 184 to 127 on the Shule Kingdom page ('In 127 AD, Shule began to pay tribute to the Eastern Han'; 'Chen Pan 127'); the page does not mention the Kushans, so the end is an inference (confidence 1). Disagreement with the earlier 184: that year was only Cliopatria's change of the strip, which no longer exists in the direct shape.
- Fergana: ledger/2 split. 168 cells from great-yuan (Cliopatria's reading; the Kushan Empire page re-read mentions neither Fergana nor Dayuan), 13 from nobody; great-yuan added to identity.predecessors. Request to ia-01: the great-yuan dissolve of 50 should name kushan-empire as counterpart (great-yuan /ledger/3 has none).
- Capital and Gandhara: took the first option and the second: keyframe 51 is now adjust, adding the 133 cells of Cliopatria's Indo-Parthian shape of 84 that lie in Gandhara, a 100 km circle round Taxila and Kabulistan (the Hou Hanshu's Jibin on the Kushan Empire page; Indo-Parthian Kingdom page: 'from the middle of the 1st century AD the Kushans ... began absorbing the northern Indian part'), with a 51 gain from indo-parthians. Reason: indo-parthians /ledger/2 and its keyframes 51 and 84 already take Gandhara, Taxila and the Kabul valley away from the Indo-Parthians in 50, so without this the land would be stateless 51-90. The 91 gain from indo-parthians is reduced to 1,683 cells, exactly the cells of indo-parthians /ledger/3. The capital is Kapisa (Begram) 30-90 (infobox: '1st Century BCE: Kapisa/Pushkalavati; from 1st century CE: Purushapura/Mathura'), Purushapura and Mathura from 91; the 127 capital_move is now a 91 one.
- Western Satraps vassal pair: 127-150, source the Western Satraps page, both dossiers carry the same years. The page: 'vassals of the Kushans, at least in the early period until Rudradaman I conquered the Yaudheyas'. The reviewer's c. 130 end was not taken: the page ties the end to the conquest of the Yaudheyas, not to the title, and dates neither; 130 would leave three years of vassalage. The Chastana page gives no date for any relation, so the Kshaharata and Chastana years (24-70, 78-130) remain undrawn.
- Mathura (91): Northern Satraps page, 'Mathura became part of the Kushan Empire from the reign of Vima Kadphises (90-100 CE)'; confidence 1 raised to 2. Keyframe 161's Champa remark now cites the Kushan Empire page (the reviewer had fixed only ledger/10).
- Thin, not resolved: the 161 loss (Huvishka page: reign 150-190, no loss or retreat described, no Champa or Chhattisgarh); the year of Kujula's conquest (Indo-Parthian Kingdom page: 'middle of the 1st century', no year for Gandhara or Taxila).

**western-satraps (was fail)**
- Vassal pair added (blocking): 127-150, counterpart kushan-empire, Western Satraps page, confidence 1.
- 35-42 overlap with indo-scythians: kept at 35 (page: 'Established: 35', 'c. 35: Abhiraka'). indo-scythians /ledger/13 and its keyframe 43 still put the land in the Indo-Scythian shape until 42, so it is drawn twice for eight years until sa-02-b moves its loss to 35. I cannot edit that dossier; reported.
- Ujjain: Bharuch (placeholder) to 126, Ujjain from 127. The page-based seat of Chastana (78-130, Ptolemy) is earlier than the first shape that contains Ujjain, Cliopatria's 127; I took the reviewer's first option rather than adjusting 91 and 106, because Cliopatria's Satavahana shapes -27 to 126 hold the land.
- 127 gain: dated 127 (was 130; Rudradaman's reign 130-150 stays in the note); confidence 2 to 1. Agrees with the 127 keyframe and satavahana-dynasty /ledger/5.
- 224 gain: split. Nasik (43 cells, 150 km) now names abhira-dynasty; the other 573 cells name satavahana-dynasty at confidence 1. The Abhira dynasty page says the Abhiras ruled Nasik from 203 'with the help and consent of the Western Satraps' and gives no Satrap conquest; satavahana-dynasty has no loss to the Satraps in 224 (its /ledger/9 dissolve gives the 215 shape to abhira-dynasty), so the mirror for the 573 cells is still missing. Disagreement: I did not drop Nasik, because the 224 keyframe keeps Cliopatria's shape and the cells need an owner.
- 124 loss (not done): Cliopatria's Satavahana shapes -27 to 126 (890,000 km2) hold 1,200 of the 1,203 cells the Satraps regain in 127, and satavahana-dynasty's keyframes 106 and 110 keep them whole through 126. Adding Nahapana's lands to the Satrap keyframes before 124 would therefore draw the land twice. The Western Satraps page puts Malwa, southern Gujarat, northern Konkan, Nasik and Poona in Nahapana's realm (24-70, 66-71 or 119-124) and dates the Satavahana conquest nowhere. The two dossiers must be fixed together: satavahana-dynasty subtracts the lands from keyframes 106 and 110 until 124 (or sets /ledger/4's counterpart to nobody), then this dossier adds a gain (106 or 119) and a 124 loss. My earlier keyframe-106 note that Cliopatria gave the lands to the Satavahanas 'from 124' was wrong (the shapes hold them from -27); corrected.
- Thin, not resolved: the years 154, 224, 260, 270, 306 and 347 remain Cliopatria's; the Abhira dynasty page (Established 203; 'From 203 to roughly 270 or 370, this dynasty formed a vast kingdom'; Abhiras 'gradually seized' Malwa 'from the Kshatrapas') bears on 224 and 270 but dates nothing for the Satraps; the Samudragupta, Yaudheya and Chastana pages were not re-opened for 347 and 306.

**western-kushans (was fail)**
- vassal_start at 230, counterpart sasanian-empire, Kushano-Sasanian Kingdom page, confidence 2, region the whole 247 shape; the rename stays. The page says the Sasanians captured Sogdia, Bactria and Gandhara 'following a series of wars in 225', 'extended their dominion into Bactria during the reign of Ardashir I around 230', and that the Kushanshahs are 'sometimes considered as forming a sub-kingdom inside the Sasanian Empire'; the Kushan Empire page has 'Persian vassals known as the Kushanshas'. No vassal_end, so the validator prints one warning that its own text calls fine for a relation lasting to the state's end. The mirror belongs in sasanian-empire (me-06). The 259 end remains Cliopatria's (the page runs the kingdom c. 230 to c. 365); the identity with indo-sasanian-empire is for me-06 and the orchestrator.

**For the orchestrator / other batches**
- sa-02-b (indo-scythians): move the loss to the Western Satraps from 43 to 35. (satavahana-dynasty): subtract Nahapana's lands from keyframes 106 and 110 until 124, or set /ledger/4's counterpart to nobody; add a 224 loss to western-satraps (573 cells) or a successor entry.
- ia-01 (great-yuan): name kushan-empire as counterpart of the 50 dissolve.
- me-06 (sasanian-empire, indo-sasanian-empire): vassal_start 230 with counterpart western-kushans; reconcile the two Cliopatria rows of Q1661685.
- Counterparts needing dossiers: abhira-dynasty (infobox: Established 203, supplanted by the Traikutakas 315 or 370; counterpart of the 224 Nasik gain and of satavahana-dynasty /ledger/8 and /ledger/9), kingdom-of-kashgar (Shule; Kushan client 117-127 here; ea-02). The Nagas of Padmavati and Vindhyatabi remain on the earlier list.

