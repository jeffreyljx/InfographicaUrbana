# Review: batch af-01-a (Nubia, Kush, Axum, Ethiopia, part a)

Reviewed 2026-10-18 by the Phase B adversarial reviewer. Machine copy: history/notes/phase-b/reviews/af-01-a.json. The validator passed all six dossiers (0 errors). Its only warnings were the counterpart slugs that have no dossier yet: banu-kanz, blemmyes, beja and kingdom-of-al-abwab, all listed by the author.

## The main finding, in four dossiers

Four corrections (makuria_1294, kingdom-of-kush_-800, alodia_602, zagwe-dynasty_947) put the shape the state reaches at the END of the keyframe's span into the region spec, while the text says 'as drawn until X; from X ...'. kingdom-of-axum_602 does the same harmlessly. The ledger event at X already carries the change, so the spec draws the change years early: Dongola lost in 1294 instead of 1365, Egypt Kushite from -800, the 10th-century Alodia from 602, Tigray Zagwe from 947 (overlapping Aksum). The fix is the same in each: the spec is the shape at the keyframe's first year (as tang-dynasty_757 and _768 in the worked example). The 'years or status only, shape unchanged, said in text' rule covers kingdom-of-axum_238 and _534 and kingdom-of-kush_-700, which are fine.

## Verdicts

### makuria: fail

Area: infobox None (None), Cliopatria 212626.7, ratio None. No infobox area on the page (checked); the dossier says so.

Findings:

- `/keyframe_review/9/correction`: makuria_1294 (1294-1406) is intersect(Makuria 1294, Lower Nubia), so the Dongola reach (150,981 km2 by the gazetteer) is dropped from 1294, 71 years before the 1365 loss that the ledger and the correction's own text date. Evidence: Correction text: 'as drawn until 1365; from 1365 only Lower Nubia'. /ledger/7 dates the loss 1365. Makuria page: 'Due to a civil war in 1365, the kingdom was reduced to a rump state that lost much of its southern territories, including Dongola.' Systemic: the correction spec is written as the shape at the END of the keyframe's span while its text says 'as drawn until X; from X ...'. The spec must be the shape at the keyframe's first year; the ledger event at X already carries the change (as tang-dynasty_757/768 do). The research brief's 'years or status only, shape unchanged, said in text' rule covers a shape whose years or status shift, not one that gains or loses land part-way. Fix: Set the spec to {"cliopatria": "Makuria", "year": 1294, "text": "as drawn; Dongola and the south are lost in 1365 (ledger)"} with verdict ok (or adjust if the vassal status text stays). /ledger/7 carries the 1365 change, and makuria_1407 already gives Lower Nubia only.
- `/ledger (missing, between /ledger/5 and /ledger/6)`: No vassal_start/vassal_end for the Mamluk client status that /keyframe_review/7 and /8 describe ('the whole kingdom in the vassal tint from 4 June 1276'); the vassal tint has no ledger event to draw it. Evidence: Makuria page: 'Mashkouda was installed on the Makurian throne on 4 June 1276'. Rule 4 asks for vassal_start/vassal_end events naming the land and the counterpart, and the cross-check needs the mirror on both sides (the Axum dossier records Himyar's vassalage itself). Fix: Add {"year": 1276, "month": 6, "type": "vassal_start", "counterpart": "mamluk-sultanate", "region": {"cliopatria": "Makuria", "year": 1276, "text": "..."}, "confidence": 3, "source": "https://en.wikipedia.org/wiki/Makuria"}, plus a paired vassal_end: the Baqt page has the treaty ending 'in the mid-fourteenth century', so 1365 at confidence 1 if nothing better is on a page.
- `/keyframe_review/7/correction/text and /wars/4/zones/0/text`: 'after defeating Makuria at Dongola on 20 January 1276' and 'Dongola, taken 20 January 1276': on the page 20 January 1276 is the day the Mamluk army was dispatched, not the day of the battle (non-blocking). Evidence: Makuria page (WebFetch): the date is given for the dispatch of the army; 'After conquering Gebel Adda and Meinarti it met the Nubian army at Dongola, defeating it decisively.' Fix: Write 'the Mamluk army sent out on 20 January 1276 defeated Makuria at Dongola' and 'Dongola, taken in 1276'.
- `/ledger/4/counterpart`: The 1173-1175 occupation names ayyubid-sultanate, whose Cliopatria row starts in 1177; Egypt in 1173 is the fatimid-caliphate row (911-1176). This is a routing note, non-blocking. Evidence: polities.csv in the author's brief: Ayyubid Sultanate 1177..1249, Fatimid Caliphate 911..1176. Fix: Keep ayyubid-sultanate (Turan-Shah was Saladin's brother) and say in the note that me-09 must start the Ayyubid dossier by 1171-1173 or take the reverse event under fatimid-caliphate.

Spot checks:

- `/ledger/4` (https://en.wikipedia.org/wiki/Makuria): confirmed ('Turan-Shah conquered Qasr Ibrim in January 1173')
- `/ledger/6` (https://en.wikipedia.org/wiki/Makuria): confirmed ('became Makuria's first Muslim king in 1316'; 'slain in late 1317')
- `/ledger/8` (https://en.wikipedia.org/wiki/Makuria): confirmed (king 'retreated to Gebel Adda'; infobox Gebel Adda after 1365)
- `/ledger/7` (https://en.wikipedia.org/wiki/Makuria): confirmed (1365 civil war, 'lost much of its southern territories, including Dongola')
- `/ledger/1` (https://en.wikipedia.org/wiki/Makuria): confirmed ('presumably during the 620s, [...] but before 642')
- `/ledger/2` (https://en.wikipedia.org/wiki/Makuria): confirmed ('between 962 and 964 they again attacked, this time pushing as far north as Akhmim')

Gaps for a gap-filler:

- `/ledger/0`: 347 founding at confidence 1 (the page: Makurian state 'by the 5th century') (try https://en.wikipedia.org/wiki/Old_Dongola)
- `/ledger/1`: The year of the Nobatia merger ('presumably during the 620s ... but before 642'); 641 is the latest year that fits (try https://en.wikipedia.org/wiki/Faras)
- `/ledger/9`: The 1414 hand-over to makuria-kingdom at confidence 1; the orchestrator has to decide whether to merge the rows (try https://en.wikipedia.org/wiki/Makuria)

### kingdom-of-kush: fail

Area: infobox None (None), Cliopatria 336379.0, ratio None. No infobox area (checked; infobox gives population 1,150,000 only).

Findings:

- `/keyframe_review/1/correction`: kingdom-of-kush_-800 (-800..-701) is union(Kush -800, Nile Valley (Egypt)), which draws all of Egypt (about 110,000 km2 beyond the shape) as Kushite from -800: 46 years before Upper Egypt (/ledger/1, -754) and 73 years before Lower Egypt (/ledger/2, -727). Evidence: The correction's own text: 'as drawn until c. -755; with Upper Egypt from c. -754 ... with Lower Egypt from -727'. Kush page: Piye 'seized control of Lower Egypt around 727 BC'. Systemic: the correction spec is written as the shape at the END of the keyframe's span while its text says 'as drawn until X; from X ...'. The spec must be the shape at the keyframe's first year; the ledger event at X already carries the change (as tang-dynasty_757/768 do). The research brief's 'years or status only, shape unchanged, said in text' rule covers a shape whose years or status shift, not one that gains or loses land part-way. Fix: Set the spec to {"cliopatria": "Kingdom of Kush", "year": -800, "text": "as drawn; Upper Egypt from c. -754, Lower Egypt from -727 and the Delta from -711 (ledger)"}. /ledger/1-3 carry Egypt, and keyframe_review/2's text already runs the Egypt shape from -727.
- `/ledger/14/note and /ledger/14/region/text`: The c. -200 gain quotes 'the territory, known in the Greco-Roman world as Dodekaschoinos, was taken back by the Kushite king'. On the page that sentence is about Yesebokheamani 'At the end of this 600-year period' (3rd century AD), not about c. 200 BC (mis-quoted, confidence 1). Evidence: Kush page: 'The northernmost part of Nubia was occupied from the 3rd century BC to the 3rd century AD ... At the end of this 600-year period, the territory, known in the Greco-Roman world as Dodekaschoinos, was taken back by the Kushite king Yesebokheamani.' The page does support a c. 200 BC recovery in other words: 'there was a serious revolt at the end of the reign of Ptolemy IV, around 204 BC' and 'Dynastic struggles led to the Ptolemies abandoning the area, and the Kushites reasserted their control ... with Qasr Ibrim occupied'. Fix: Quote the 204 BC revolt and the 'reasserted their control ... with Qasr Ibrim occupied' sentences instead, keep confidence 1, and drop 'with the Dodekaschoinos' from the region text unless a page puts Kush at Philae then. Move the Yesebokheamani sentence to /ledger/18 (c. 250) as its source words.
- `/keyframe_review/5/correction and /keyframe_review/6`: kush_-630 removes the Dodekaschoinos (4,046 km2 of the shape) from -630, though the page dates the Ptolemaic occupation only 'from the 3rd century BC'. kush_338 (verdict ok) then puts it back in Kush for 338-346 after the 297 loss to the Blemmyes (/ledger/19), with no event (small, non-blocking). Evidence: Gazetteer: intersect(Lower Nubia, Aswan 115 km) ∩ kingdom-of-kush_-630 = 4,046 km2. Kush page quoted above. Fix: Give kush_-630 the shape as drawn at -630 (the -274 loss removes Lower Nubia); mark kush_338 adjust with {"minus": [{"cliopatria": "Kingdom of Kush", "year": 338}, {"intersect": [{"region": "Lower Nubia"}, {"place": "Aswan", "km": 115}]}]}.
- `/ledger/11/counterpart`: The -656 loss names assyrian-egypt, whose Cliopatria row is -650..-616 (not alive in -656); Psamtik I's Twenty-sixth Dynasty row starts -615. This is a routing note for me-02/me-03, non-blocking. Evidence: Context table of the author's brief. Fix: Keep it, and say in the note which row me-02/me-03 should mirror.

Spot checks:

- `/ledger/5` (https://en.wikipedia.org/wiki/Assyrian_conquest_of_Egypt): confirmed ('In 671, Esarhaddon took and sacked Memphis')
- `/ledger/6` (https://en.wikipedia.org/wiki/Twenty-fifth_Dynasty_of_Egypt): confirmed ('In 669 BC, Taharqa reoccupied Memphis, as well as the Delta')
- `/ledger/9` (https://en.wikipedia.org/wiki/Assyrian_conquest_of_Egypt): confirmed (663 BCE, battle north of Memphis, 'effectively ended Nubian control over Egypt')
- `/ledger/11` (https://en.wikipedia.org/wiki/Assyrian_conquest_of_Egypt): confirmed ('until his 8th Year in 656 BCE, when Psamtik I's navy peacefully took control of Thebes')
- `/ledger/2` (https://en.wikipedia.org/wiki/Kingdom_of_Kush): confirmed ('seized control of Lower Egypt around 727 BC')
- `/ledger/13` (https://en.wikipedia.org/wiki/Kingdom_of_Kush): confirmed ('In 275 or 274 BC, Ptolemy II ... annexing to Egypt the area later known as Triakontaschoinos')
- `/ledger/14` (https://en.wikipedia.org/wiki/Kingdom_of_Kush): not on page as quoted (the quote is the 3rd-century-AD Yesebokheamani sentence; the c. 200 BC date is supported by the 204 BC revolt passage)

Gaps for a gap-filler:

- `/ledger/0`: -1000 emergence (page: 'around 1070 BC' independence, infobox c. 780 BC) (try https://en.wikipedia.org/wiki/Alara_of_Nubia)
- `/ledger/1`: Kashta's advance to Thebes, undated; the Twenty-fifth Dynasty page says he 'did not control it' (try https://en.wikipedia.org/wiki/Kashta)
- `/ledger/8`: The year of Tantamani's recapture of Memphis (try https://en.wikipedia.org/wiki/Tantamani)
- `/ledger/14`: The date of the Kushite recovery of Lower Nubia after the 204 BC revolt (try https://en.wikipedia.org/wiki/Arqamani)
- `/ledger/18`: The years of 3rd-century Kushite control at Philae (Yesebokheamani) (try https://en.wikipedia.org/wiki/Yesebokheamani)
- `/ledger/19`: Diocletian's 297 withdrawal: who took the Dodekaschoinos (try https://en.wikipedia.org/wiki/Dodekaschoinos)
- `/ledger/21`: The end of the Aksumite presence at Meroë (try https://en.wikipedia.org/wiki/Ezana_of_Axum)

### kingdom-of-axum: fix

Area: infobox 1250000 (350), Cliopatria 132994.0, ratio 9.4. Also 2,500,000 km2 for 525 against 97,004 km2 (25.8). Both acknowledged and resolved as an inflated infobox; ratios corrected by the reviewer.

Findings:

- `/ledger/8/confidence and /ledger/8/region/text` (applied by the reviewer): The 570 vassal_end quoted 'Aksumite rule in Yemen ended', which is not on the cited page, and had confidence 3 although the page has an Aksumite comeback and dates the end 'by 578'. Evidence: Aksumite–Persian wars page: no such phrase; 'Facing an Aksumite reconquest, the Sasanian Empire mounted a second invasion'; 're-conquered Yemen by 578, indefinitely ending Aksumite rule outside of Africa'; 570 is confirmed for Wahrez's expedition. Fix: Confidence lowered to 2. The region text now quotes 'The decisive Persian victory at Hadhramaut marked the beginning of the Aksumite retreat', 'the capture of Sanaʽa by Sasanian forces' and the 578 sentence; one sentence added to the note. Same misquote removed from /keyframe_review/3/correction/text.
- `/keyframe_review/2/note, /keyframe_review/3/note, /notes` (applied by the reviewer): The area checks compared the infobox with the wrong shapes: the shape alive in 350 is kingdom-of-axum_238 (132,994 km2) and in 525 kingdom-of-axum_353 (97,004 km2). Evidence: shapes.csv: _238 runs 238-352 and _353 runs 353-533. Fix: Ratios corrected to 9.4 (350) and 25.8 (525); the conclusion (infobox inflated, shapes kept) stands.
- `/keyframe_review/4/correction and /ledger/9/region`: kingdom-of-axum_602 removes northern Eritrea from 602 although the Beja loss is c. 700, and the /ledger/9 loss region (56,902 km2) lies almost wholly outside the drawn kingdom: only about 1,012 km2 of it is in the Cliopatria shape, which stops at 15.6 N. The effect on the map is negligible (non-blocking). Evidence: Gazetteer: union(Semenawi Keyih Bahri, Anseba, Gash Barka) ∩ kingdom-of-axum_602 = 1,012 km2. Fix: Optional: give _602 as drawn (verdict ok) and say in /ledger/9's note that the Cliopatria shape already excludes most of the Beja country.

Spot checks:

- `/ledger/8` (https://en.wikipedia.org/wiki/Aksumite%E2%80%93Persian_wars): mis-quoted; year confirmed (fixed: confidence 2, quote replaced)
- `/ledger/5` (https://en.wikipedia.org/wiki/Kingdom_of_Aksum): confirmed ('Aksum held on to Southern Arabia from 520 until 525 when Sumyafa Ashwa was deposed by Abraha')
- `/ledger/6` (https://en.wikipedia.org/wiki/Aksumite%E2%80%93Persian_wars): confirmed ('in 525, he was deposed by the Aksumite general Abraha')
- `/ledger/1` (https://en.wikipedia.org/wiki/Kingdom_of_Aksum): confirmed (Gedara c. 200-230, 'control of much of western Yemen')
- `/ledger/9` (https://en.wikipedia.org/wiki/Kingdom_of_Aksum): confirmed ('At the end of the seventh century, a strong Beja tribe known as the Zanafaj entered the Eritrean plateau')
- `/ledger/11` (https://en.wikipedia.org/wiki/Kingdom_of_Aksum): confirmed ('around 960, a queen known as Gudit ... conquered Aksum'; infobox 'Collapse: 960 AD')

Gaps for a gap-filler:

- `/ledger/0`: Founding c. -50 (page: '1st century'; 150 BCE-150 CE) (try https://en.wikipedia.org/wiki/Zoskales)
- `/ledger/1`: The start of the Arabian holding (Gedara c. 200-230) (try https://en.wikipedia.org/wiki/Gadarat)
- `/ledger/2`: The end of the 3rd-century Arabian holding. The page puts the break with Šaʿirum Yawtar (c. 210-230) and 'conflicts persisted throughout the 3rd century'; 275 is a guess (try https://en.wikipedia.org/wiki/Shammar_Yahri%27sh)
- `/ledger/4`: The end of the Meroë occupation (try https://en.wikipedia.org/wiki/Ezana_of_Axum)
- `/ledger/9`: Where the Beja gains of c. 700 lay (try https://en.wikipedia.org/wiki/Beja_people)
- `/ledger/10`: Kubar's site and the year of the move (try https://en.wikipedia.org/wiki/Kubar)

### nobatia: thin

Area: infobox None (None), Cliopatria 147534.1, ratio None. No infobox area (checked).

Spot checks:

- `/ledger/0` (https://en.wikipedia.org/wiki/Nobatia): confirmed (Diocletian 297; 'only became tangible around 400 AD')
- `/ledger/1` (https://en.wikipedia.org/wiki/Nobatia): confirmed (infobox '450 A.D: Silko'; 'driven the Blemmyes into the Eastern Desert', undated)
- `/ledger/2` (https://en.wikipedia.org/wiki/Nobatia): confirmed ('most likely occurred before the Muslim conquest in 652'; 'By 707')

Gaps for a gap-filler:

- `/ledger/0`: 347 founding (the page: kingdom 'only became tangible around 400 AD'), confidence 1 (try https://en.wikipedia.org/wiki/Faras)
- `/ledger/1`: The date and extent of Silko's war (infobox 450; inscription undated) and the 4th-5th-century split of Lower Nubia with the Blemmyes. The 347 shape already holds 4,046 km2 of the Dodekaschoinos this gain takes (small, inside one span) (try https://en.wikipedia.org/wiki/Silko)
- `/ledger/2`: The merger year ('before 652', 'By 707'; Makuria page 'before 642'), confidence 1 (try https://en.wikipedia.org/wiki/Faras_Cathedral)

### alodia: fail

Area: infobox None (None), Cliopatria 123780.4, ratio 7.6. No infobox area. The ratio is the author's corrected shape (941,294 km2) against Cliopatria's. The author acknowledges that the regions are 'wider than the page's words', but part of the extent contradicts the page (northern Kordofan).

Findings:

- `/keyframe_review/1/correction`: alodia_602 is union(Alodia 602, Nilotic Sudan, Kordofan, Beja country), 941,294 km2 by the gazetteer (7.6 times the 123,780 km2 shape), drawn from 602: 350 years before the c. 950 gain (/ledger/1) that is meant to carry it. Evidence: The correction's own text: 'as drawn until the 10th century; from c. 950 the extent Ibn Hawqal and al-Aswani describe'. Systemic: the correction spec is written as the shape at the END of the keyframe's span while its text says 'as drawn until X; from X ...'. The spec must be the shape at the keyframe's first year; the ledger event at X already carries the change (as tang-dynasty_757/768 do). The research brief's 'years or status only, shape unchanged, said in text' rule covers a shape whose years or status shift, not one that gains or loses land part-way. Fix: Set the spec to {"cliopatria": "Alodia", "year": 602, "text": "as drawn; the 10th-century extent from c. 950 and al-Abwab's split in 1276 are in the ledger"} with verdict ok or adjust.
- `/ledger/1/region`: The c. 950 gain names the whole of 'Kordofan' (360,130 km2, North and South Kordufan), which the page contradicts, and it overlaps the makuria 950 shape by 76,376 km2 with counterpart nobody, while the makuria dossier records no loss. Evidence: Alodia page: 'the Alodian-controlled Al-Ahdin, which has been identified with the Nuba Mountains', but 'Al-Jeblien, which was controlled by Makuria, probably corresponded with northern Kordofan'; the Eastern Desert is what the accounts 'suggest'. Gazetteer: the gain ∩ {cliopatria Makuria 950} = 76,376 km2, and al-Abwab's spec (River Nile minus Shendi 120 km) alone overlaps it by 50,580 km2. Fix: Replace {"region": "Kordofan"} with {"admin1": "South Kordufan", "country": "Sudan"} (Nuba Mountains, 134,796 km2), wrap the union in {"minus": [..., {"cliopatria": "Makuria", "year": 950}]}, and keep confidence 1. The same applies to /ledger/2's al-Abwab spec (clip it to outside Makuria).
- `/keyframe_review/2 (alodia_1502) and /ledger`: Unexplained area: the corrected kingdom (about 941,000 km2, less al-Abwab from 1276) returns to 123,780 km2 at the 1502 keyframe ('the shape unchanged') with no event between 1276 and 1504 that removes Kordofan, the Butana fringe or the Beja country (about 700,000 km2). Evidence: The page: decline 'From the 12th, and especially the 13th century'; Arabs 'had settled in the entire central Sudanese Nile valley' by the late 15th century. The keyframe text acknowledges the core-only extent, but no ledger loss carries it. Fix: Add loss events, at confidence 1 if undated (counterparts nobody, beja or abdallab), that bring the kingdom back to the Soba-Gezira core before 1502, or limit the c. 950 gain to what the ledger can take back.

Spot checks:

- `/ledger/1` (https://en.wikipedia.org/wiki/Alodia): not on page as drawn (the page gives Al-Ahdin/Nuba Mountains to Alodia and northern Kordofan to Makuria; the Eastern Desert is only 'suggested')
- `/ledger/2` (https://en.wikipedia.org/wiki/Alodia): confirmed ('By 1276 al-Abwab ... was recorded as an independent splinter kingdom')
- `/ledger/3` (https://en.wikipedia.org/wiki/Alodia): confirmed ('In 1504–1505 the Funj founded the Funj sultanate'; Tabaqat Dayfallah 1504–1505)
- `/ledger/0` (https://en.wikipedia.org/wiki/Alodia): confirmed (founded 'around 350 AD'; first mentioned 6th century)

Gaps for a gap-filler:

- `/ledger/0`: 347 founding ('around 350 AD'; first mention 569) (try https://en.wikipedia.org/wiki/Soba_(city))
- `/ledger/1`: The date of the expansion beyond the Gezira (described c. 950) and its limits (try https://en.wikipedia.org/wiki/Ibn_Hawqal)
- `/ledger/2`: al-Abwab's extent and end (try https://en.wikipedia.org/wiki/Al-Abwab)

### zagwe-dynasty: fail

Area: infobox None (None), Cliopatria 14454.3, ratio 23.0. No infobox area. The ratio is the author's corrected 1139 shape (331,805 km2) against Cliopatria's Lasta-only shape; the author acknowledges it and it rests on Buxton's description.

Findings:

- `/keyframe_review/0/correction`: zagwe-dynasty_947 is union(Zagwe 947, Tigray (region)), which gives the Zagwe Tigray and all of Eritrea from 947, while the gain is c. 960 (/ledger/1) and kingdom-of-axum holds the heartland to 960. 62,213 km2 is drawn in both states for 947-959. Evidence: The correction's own text: 'with the Aksumite heartland ... added from c. 960'. Gazetteer: Tigray (region) ∩ {cliopatria Kingdom of Axum 946} = 62,213 km2. kingdom-of-axum /keyframe_review/6 runs to 960. Systemic: the correction spec is written as the shape at the END of the keyframe's span while its text says 'as drawn until X; from X ...'. The spec must be the shape at the keyframe's first year; the ledger event at X already carries the change (as tang-dynasty_757/768 do). The research brief's 'years or status only, shape unchanged, said in text' rule covers a shape whose years or status shift, not one that gains or loses land part-way. Fix: Set the spec to {"cliopatria": "Zagwe dynasty", "year": 947, "text": "Lasta as drawn; the Aksumite heartland from c. 960 (ledger)"}; /ledger/1 carries Tigray.
- `/ledger/1/region and /ledger/1/note`: The 960 gain from kingdom-of-axum takes 'Tigray (region)' (171,719 km2: Tigray plus all of Eritrea), but Aksum hands over {cliopatria Kingdom of Axum 946} (96,102 km2) and had lost the northern Eritrean plateau to the Beja c. 700. The note's quote 'her line ruled for about 40 years' is not the cited page's wording (confidence 1). Evidence: kingdom-of-axum /ledger/11 region and /ledger/9. Zagwe page: 'According to one tradition, around 960, Queen Gudit destroyed the remnants of the Kingdom of Aksum' and 'For 40 years she ruled over what remained of the kingdom.' Fix: Use {"cliopatria": "Kingdom of Axum", "year": 946} (the land Aksum dissolves) for the 960 gain and quote the page's two sentences. The Buxton extent (Tigray (region) and Amhara) can stay from 1137 in keyframes 1-2 and /ledger/3.

Spot checks:

- `/ledger/1` (https://en.wikipedia.org/wiki/Zagwe_dynasty): confirmed in substance (around 960, Gudit; 40 years); mis-quoted ('For 40 years she ruled', not 'her line')
- `/ledger/2` (https://en.wikipedia.org/wiki/Zagwe_dynasty): confirmed (infobox 'Established: 1137'; 'the last of her dynasty was overthrown by Mara Takla Haymanot in 1137')
- `/ledger/3` (https://en.wikipedia.org/wiki/Zagwe_dynasty): confirmed (Buxton: 'probably embraced the highlands of modern Eritrea, Tigray, Wag and Bete Amhara and thence westwards towards Lake Tana'; undated)
- `/ledger/4` (https://en.wikipedia.org/wiki/Zagwe_dynasty): confirmed (killed the last Zagwe king 'at the Battle of Ansata', infobox 1270; month 8 is from the Yekuno Amlak page, not opened by the reviewer)

Gaps for a gap-filler:

- `/ledger/0`: 947 start (infobox 1137; 'other theories' c. 930), confidence 1 (try https://en.wikipedia.org/wiki/Mara_Takla_Haymanot)
- `/ledger/1`: Gudit's line 960-1137 is folded into this dossier; a gudit dossier would need a page giving it land (try https://en.wikipedia.org/wiki/Gudit)
- `/ledger/3`: The date the Zagwe took Wag, Bete Amhara and Begemder (Buxton undated) (try https://en.wikipedia.org/wiki/Lalibela_(king))

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| makuria 641 merge / nobatia | nobatia 641 dissolve | matched | nobatia ends 641 with counterpart makuria; both dossiers mark Cliopatria's 656 date wrong |
| nobatia 641 dissolve / makuria | makuria 641 merge | matched |  |
| makuria 962 occupation_start / abbasid-caliphate | - | exception | me-08 not run; Egypt was Ikhshidid (the author flags it) |
| makuria 1173 occupation_start / ayyubid-sultanate | - | exception | me-09 not run; Cliopatria's Ayyubid row starts 1177 and Egypt in 1173 is the fatimid-caliphate row (911-1176), so me-08/me-09 must agree who carries it |
| makuria 1276 vassal_start (missing) / mamluk-sultanate | - | missing | Neither side has it: makuria must add vassal_start 1276-06 and a vassal_end; me-09 (not run) mirrors |
| makuria 1365 loss / banu-kanz | - | exception | banu-kanz has no dossier; listed in counterparts_needing_dossiers (af-01-x) |
| makuria 1414 dissolve / makuria-kingdom | - | exception | makuria-kingdom belongs to another part of af-01 (running in parallel); the orchestrator should decide whether to merge the rows (same Wikidata Q829356) |
| kingdom-of-kush -1000 found / new-kingdom-of-egypt | - | exception | me-03 not run; Cliopatria's New Kingdom row overlaps Kush in Nubia to -801 |
| kingdom-of-kush -754 gain / twenty-second-dynasty-of-egypt | - | exception | me-03 not run |
| kingdom-of-kush -727 gain / twenty-second-dynasty-of-egypt | - | exception | me-03 not run |
| kingdom-of-kush -711 gain / Twenty-fourth Dynasty of Egypt (Sais) | - | exception | no Cliopatria row; listed in counterparts_needing_dossiers (me-03) |
| kingdom-of-kush -671 contest_start / neo-assyrian-empire | - | exception | me-02 not run |
| kingdom-of-kush -671 loss / neo-assyrian-empire | - | exception | me-02 not run |
| kingdom-of-kush -669 gain / neo-assyrian-empire | - | exception | me-02 not run |
| kingdom-of-kush -667 loss / neo-assyrian-empire | - | exception | me-02 not run |
| kingdom-of-kush -664 gain / neo-assyrian-empire | - | exception | me-02 not run |
| kingdom-of-kush -663 loss / neo-assyrian-empire | - | exception | me-02 not run |
| kingdom-of-kush -663 contest_end / neo-assyrian-empire | - | exception | me-02 not run |
| kingdom-of-kush -656 loss / assyrian-egypt | - | mismatch | me-02 not run, and the Assyrian Egypt row (-650..-616) is not alive in -656; route to me-02/me-03 (Psamtik I, Twenty-sixth Dynasty row from -615) |
| kingdom-of-kush -274 loss / ptolemaic-kingdom | - | exception | me-05 not run; the -200 gain is mis-quoted (see fixes) |
| kingdom-of-kush -200 gain / ptolemaic-kingdom | - | exception | me-05 not run; the -200 gain is mis-quoted (see fixes) |
| kingdom-of-kush -23 contest_start / roman-empire | - | exception | eu-04 not run |
| kingdom-of-kush -22 contest_end / roman-empire | - | exception | eu-04 not run |
| kingdom-of-kush -22 loss / roman-empire | - | exception | eu-04 not run |
| kingdom-of-kush 250 gain / roman-empire | - | exception | eu-04 not run |
| kingdom-of-kush 297 loss / blemmyes | nobatia 450 gain (from blemmyes) | exception | blemmyes has no dossier; listed (af-01-x). nobatia takes the same Dodekaschoinos from the Blemmyes c. 450, consistent |
| kingdom-of-kush 330 occupation_start / kingdom-of-axum | kingdom-of-axum 330 occupation_start | matched | same region (Meroe 100 km) |
| kingdom-of-kush 331 occupation_end / kingdom-of-axum | kingdom-of-axum 331 occupation_end | matched |  |
| kingdom-of-axum 200 occupation_start / himyarite-kingdom | - | exception | me-06 not run |
| kingdom-of-axum 275 occupation_end / himyarite-kingdom | - | exception | me-06 not run |
| kingdom-of-axum 520 gain / himyarite-kingdom | - | exception | me-06 not run |
| kingdom-of-axum 525 loss / himyarite-kingdom | - | exception | me-06 not run |
| kingdom-of-axum 525 vassal_start / himyarite-kingdom | - | exception | me-06 not run |
| kingdom-of-axum 570 vassal_end / himyarite-kingdom | - | exception | me-06 not run |
| kingdom-of-axum 700 loss / beja | - | exception | beja has no dossier; listed (af-01-x) |
| kingdom-of-axum 960 dissolve / zagwe-dynasty | zagwe-dynasty 960 gain | mismatch | Same year, different land: axum hands over {cliopatria Kingdom of Axum 946} (96,102 km2) and zagwe takes Tigray (region) (171,719 km2, all of Eritrea); zagwe's 947 keyframe also draws Tigray from 947 (62,213 km2 overlap 947-959) |
| nobatia 450 gain / blemmyes | - | exception | blemmyes has no dossier; listed (af-01-x) |
| alodia 950 gain / nobody | makuria 950 None | mismatch | The gain region overlaps the makuria 950 shape by 76,376 km2 (al-Abwab/River Nile and North Kordofan, which the Alodia page gives to Makuria), and makuria has no loss |
| alodia 1276 split / kingdom-of-al-abwab | - | exception | no dossier; listed (af-01-x) |
| alodia 1504 dissolve / funj-sultanate | - | exception | funj-sultanate belongs to another part of af-01 (not written yet); it should start 1504 |
| zagwe-dynasty 1137 gain / nobody | - | exception | land outside any Cliopatria row per the author; not verified against other rows |
| zagwe-dynasty 1270 dissolve / ethiopian-empire | - | exception | ethiopian-empire belongs to another part of af-01 (not written); it should start 1270 |

## Other notes

- Capitals: every dot is inside its shape's bbox except Old Dongola (30.74 E), 12 km west of makuria_347's bbox (30.86 E). Cliopatria's western edge is the problem there; no fix needed.
- Certainty spans cover every life without gaps. Wars carry zones, or say why they have none.
- The author's notes flag the Makuria/Makuria Kingdom merge, the changed end years, Gudit's line and the inflated Aksum infobox. Missed: Kordofan contradicts the Alodia page, the Alodia expansion overlaps Makuria, and no event takes the 10th-century Alodia back to its core before 1502.

## Problems

- One defect repeats in four dossiers (makuria_1294, kingdom-of-kush_-800, alodia_602, zagwe-dynasty_947; harmlessly also kingdom-of-axum_602): the correction spec is the shape at the end of the span and the text says 'as drawn until X'. One instruction to the author can fix all of them: the spec must be the shape at the keyframe's first year.
- makuria / makuria-kingdom (Wikidata Q829356) are one state on the page; the orchestrator must decide between merging them and handing over in 1414, and the makuria-kingdom 1507-1518 shapes (240,898 km2) need checking.
- End years moved against Cliopatria that other parts must follow: axum 960, zagwe 1270 (ethiopian-empire), alodia 1504 (funj-sultanate), nobatia 641.
- Pages the reviewer did not open (spot-check budget): Yekuno Amlak, Kaleb of Axum, Himyarite Kingdom, Banu Kanz, Baqt, Meroë, Napata, Ezana, Blemmyes, Soba. WebFetch caps quotes at 125 characters, so long passages were read in segments.
- Reviewer edits: kingdom-of-axum.json only (ledger/8 confidence and quote, keyframe_review/2-3 and notes area ratios); re-validated with 0 errors and read back after the write. No other dossier was edited.
