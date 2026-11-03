# Review of batch me-06-b

Reviewer run 2026-10-19. Validator: all four dossiers pass with 0 errors and 0 warnings, with `--resolve`. Verdicts: all four **fail**. The main reason is that none of the four ledgers records the vassal and client relations that define these frontier kingdoms (rule 4), although their own pages state them and parthian-empire and roman-empire already carry the other side. Commagene's kept Cliopatria shape is also misplaced, and its Cilician strip is drawn as the whole gazetteer Cilicia. The reviewer applied two small fixes (marked applied).

## kingdom-of-adiabene - fail

- `/ledger`: Blocking: the kingdom's whole-life vassal status is missing from the ledger; there is no vassal_start or vassal_end with parthian-empire, kingdom-of-armenia or sasanian-empire.
  - why: Adiabene page infobox: 'Vassal of the Parthian Empire (145 BC - 224 AD)' and 'Vassal of the Sasanian Empire (224-379)'. Text: 'conquered by the Parthian king Mithridates I ... between 145 and 141 BCE'; 'nominally vassal to the Armenian empire under Tigranes the Great'. parthian-empire /ledger/26 (vassal_start kingdom-of-adiabene, -95, confidence 3) and /ledger/32 (vassal_end, -87) have no mirror here. The author's own /ledger/0 note says 'it was a Parthian vassal from then' but records nothing.
  - fix: Insert, with the corrected core as region: vassal_start parthian-empire at -141 (confidence 2, Adiabene page; say parthian-empire has -95). At -87, vassal_end parthian-empire and vassal_start kingdom-of-armenia (confidence 2, mirroring parthian-empire /ledger/32). vassal_end kingdom-of-armenia and vassal_start parthian-empire when Armenian control ends (confidence 1, bridged to about -66). vassal_end parthian-empire at 116 with the Roman annexation and vassal_start parthian-empire at 117. vassal_end parthian-empire and vassal_start sasanian-empire at 224 (confidence 2, infobox; the text has Sasanian rule established by Shapur I, 240-270). vassal_end sasanian-empire at 379 next to the dissolve.
- `/keyframe_review/10`: Blocking: from 299 to 363 the corrected core overlaps the Roman gain of 299, and the ledger has no 299 loss or 363 return.
  - why: roman-empire /ledger/107 (299, gain from sasanian-empire, confidence 3) is a polygon for 'the area between the Tigris and the Greater Zab'. It resolves to 61 cells, 24 of which are inside this dossier's Arbil plus Nineveh 60 km core (98 cells), including 21 of the 44 Nineveh-circle cells. This dossier's own keyframe note quotes the Mesopotamia page: 'the territory in Adiabene conquered by Diocletian' was lost in 363.
  - fix: Add a loss at 299 to roman-empire of the land west of the Greater Zab, for example {"minus": [{"place": "Nineveh", "km": 60}, {"admin1": "Arbil", "country": "Iraq"}]} with text 'the territory in Adiabene conquered by Diocletian', at confidence 2 (Mesopotamia page). Add a 363 gain from roman-empire, or give that land to sasanian-empire with a note. Split keyframe 287 at 299 and 363. If you think the Roman polygon is wrong, say so in notes so that eu-04 can be routed.
- `/keyframe_review/2`: The Nisibis circle for 36-164 is double-booked with kingdom-of-osroene.
  - why: The {place: Nusaybin, km: 40} circle (19 cells) shares 9 cells with Cliopatria's Osroene shapes, which kingdom-of-osroene keeps 'ok' from -63 to 214.
  - fix: Keep Nisibis here (the page dates the grant to 36). The Osroene fix removes it on that side; no change is needed here once Osroene is fixed.
- `/ledger/6`: Nisibis in 165 is lost twice, by this dossier and by parthian-empire.
  - why: Roman-Parthian War of 161-166 page: 'The Parthians retreated to Nisibis, but this too was besieged and captured'; nothing on it about Adiabene. parthian-empire /ledger/59 also loses Nisibis to Rome in 165.
  - fix: Keep it at confidence 2, but note the conflict in the note so that the me-06-a and eu-04 owners can agree on one loser.
- `/ledger/5` (applied): Confidence 3 rested on a year that the page does not give, and the note misquoted the page.
  - why: Roman-Parthian Wars page: Hadrian 'willingly returned to the status quo ante, surrendering the territories of Armenia, Mesopotamia, and Adiabene back to their previous rulers and client-kings'. The page gives no year.
  - fix: Applied by the reviewer: confidence lowered to 2 and the quote corrected (117 is the year of Trajan's death).

Thin:
- `/keyframe_review/9`: 260-286 is bridged and the page is silent on it (try https://en.wikipedia.org/wiki/Shapur_I)
- `/ledger/4`: the end of the Gordyene dependency, bridged to 116 at confidence 1 (try https://en.wikipedia.org/wiki/Corduene)
- `/ledger`: how long Tigranes held Adiabene (for the Armenian vassal span) (try https://en.wikipedia.org/wiki/Tigranes_the_Great)

Spot checks:
- `/ledger/2` https://en.wikipedia.org/wiki/Adiabene: confirmed: 'Nisibis was not part of Adiabene before 36, when Artabanus presented the city to Izates'
- `/ledger/3` https://en.wikipedia.org/wiki/Adiabene: confirmed: 'made a part of the Roman province of Assyria after the invasion by Trajan in 116'
- `/ledger/5` https://en.wikipedia.org/wiki/Roman%E2%80%93Parthian_Wars: mis-dated: the page gives no year and the quote was a paraphrase; lowered to confidence 2 (applied)
- `/ledger/7` https://en.wikipedia.org/wiki/Adiabene: confirmed: 'in c. 379 transformed into a province (shahr)'
- `/ledger/1` https://en.wikipedia.org/wiki/Adiabene: confirmed: 'starting at least with the rule of Monobazos I (late 1st-century BCE), Gordyene became an Adiabenian dependency'

Area: The page has no infobox area. Cliopatria's 13.8 k km2 is misplaced (verdict wrong, confirmed: 1 of its 54 cells lies in the corrected core). The corrected core is 98 cells, about 24.8 k km2, 1.8 times Cliopatria.

## kingdom-of-commagene - fail

- `/keyframe_review/1`: Blocking: the Cliopatria shape, kept as 'shape unchanged' in all five keyframes, is in the wrong place, and the capital lies outside it.
  - why: Of the shape's 36-37 cells, only 9 are in Adiyaman province. 8 are in Malatya and 12 in Elazig, which is on the left bank of the Euphrates in Sophene's country. Samosata (38.48E, about 37.55N) lies south of the shape's bounding box (37.71-38.87N), and a cell at Samosata is not in the shape. 17 of the shape's cells are also in kingdom-of-cappadocia's -64 shape: Cappadocia /ledger/13 hands them to Commagene in -63, and carrying the -63 shape back to -163 (/keyframe_review/0) double-books them for a century. Commagene page: 'Commagene extended from the right bank of the Euphrates to the Taurus and Amanus Mountains', capital Samosata. The dossier's own text says 'roughly Adiyaman and northern Antep'.
  - fix: Make the verdict 'wrong' for commagene_-63, _43 and _68, and correct /keyframe_review/0 and /2 to match. Use the correction {"admin1": "Adiyaman", "country": "Turkey"} (26 cells, about 6.6 k km2), plus a polygon for the northern Gaziantep strip if you want it, with text 'from the right bank of the Euphrates to the Taurus and Amanus, with Samosata'. Use the same region in /ledger/0, /ledger/1, /ledger/2, /ledger/4 and /ledger/6. Then tell me-05 that Cappadocia's -63 loss to Commagene rests on the misplaced shape.
- `/ledger/3`: Blocking: the Cilician strip is drawn as the whole gazetteer Cilicia, mostly the wrong land.
  - why: The gazetteer's 'Cilicia' is Adana + Mersin + Osmaniye. It resolves to 120 cells (about 30 k km2), three times the kingdom, and is mostly the plain round Tarsus and Adana, which was Roman provincial land. Antiochus IV page: 'a part of Cilicia bordering on the seacoast'. Commagene page: 'the wild areas of Cilicia'. The same spec is used in /ledger/5 and /keyframe_review/2, /3 and /4.
  - fix: Until the gazetteer has 'Cilicia Trachea', use a polygon for the coastal Taurus from Coracesium (Alanya, about 32.0E) to the Lamos river (about 34.2E) between the coast and about 37.0N, at confidence 2, text 'a part of Cilicia bordering on the seacoast (Cilicia Trachea)'. Use the same polygon in /ledger/5 and in the three keyframe corrections.
- `/ledger`: The Roman client status is not recorded, and roman-empire's client tint has no mirror.
  - why: Commagene page: 'Antiochus IV was the only client king of Commagene under the Roman Empire'. Antiochus I was Pompey's ally in 64 BC. roman-empire /ledger/4 (vassal_start kingdom-of-commagene, -27, confidence 2) and /ledger/54 (vassal_end, 72, confidence 3) have no mirror here. Also on the page: 'Mithridates Callinicus is thought have accepted Armenian suzerainty during the reign of Tigranes II' (undated).
  - fix: Add vassal_start roman-republic at -64 (Pompey; confidence 2), or vassal_start roman-empire at -27 to mirror eu-04. Add vassal_end at 17 with the annexation, vassal_start roman-empire at 38 (or 41), and vassal_end roman-empire at 72 before the loss. Note that roman-empire keeps the tint unbroken from -27 to 72 although the kingdom was a province from 17 to 38; route that to eu-04.
- `/keyframe_review/2`: A dated deposition and restoration are missing; the kingdom is held without a break from 38 to 42.
  - why: Antiochus IV page: 'he was subsequently deposed by Caligula' and 'Antiochus did not regain his kingdom till the accession of Roman Emperor Claudius in 41'. Commagene page: 'Deposed by Caligula and restored again upon Claudius' accession in 41 AD'. The author's notes say the pages give no date, but the restoration is dated 41 on both pages.
  - fix: Add a loss to roman-empire at 40 (confidence 1, bridged between 38 and 41) and a gain from roman-empire at 41 (confidence 3). End keyframe commagene_38 at 39 and add a 41-42 keyframe.
- `/identity/capitals/0`: Samosata's coordinates are slightly south (37.53N; Samsat is at about 37.58N), and the capital falls outside the drawn shape.
  - why: The shape bounding box from shapes.csv starts at 37.706N. Fix 1 above covers the shape side.
  - fix: Use lat 37.58, lon 38.48 (not verified on a page, so the reviewer did not apply it).

Thin:
- `/ledger`: 61: 'in the year 61 he obtained parts of Armenia' (Antiochus IV page); no land is named (try https://en.wikipedia.org/wiki/Roman%E2%80%93Parthian_War_of_58%E2%80%9363)
- `/ledger`: the undated Armenian suzerainty under Mithridates Callinicus and Tigranes (try https://en.wikipedia.org/wiki/Tigranes_the_Great)
- `/ledger`: Zeugma, which Pompey assigned to Commagene; undated, and outside the shape (try https://en.wikipedia.org/wiki/Zeugma,_Commagene)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Commagene: confirmed: 'In 17 when Antiochus III of Commagene died, Emperor Tiberius annexed Commagene to the province of Syria'
- `/ledger/2` https://en.wikipedia.org/wiki/Commagene: confirmed: 'In 38 AD, Caligula reinstated Antiochus III's son Antiochus IV'
- `/ledger/3` https://en.wikipedia.org/wiki/Antiochus_IV_of_Commagene: confirmed (year): 'enlarged Antiochus' territory with a part of Cilicia bordering on the seacoast'; the region drawn is wrong (fix 2)
- `/ledger/4` https://en.wikipedia.org/wiki/Commagene: confirmed: infobox 'Disestablished 72 AD'; Vespasian 'deposed the dynasty and definitively re-annexed the territory'

Area: No infobox area. The Cliopatria shape is about the right size but misplaced (fix 1). Adiyaman province is 26 cells, about 6.6 k km2.

## kingdom-of-gordyene - fail

- `/ledger`: Blocking: there are no vassal events at all, though two dossiers already in history/polities name Gordyene as a vassal, and so does the page.
  - why: The same batch's kingdom-of-adiabene /ledger/1 (vassal_start kingdom-of-gordyene, -1) and /ledger/4 (vassal_end, 116) have no mirror here. Neither do parthian-empire /ledger/27 (vassal_start kingdom-of-gordyene, -95, confidence 3) and /ledger/33 (vassal_end, -87). Corduene page: 'From 189 to 90 BCE, it enjoyed a period of independence'; Tigranes 'extended his power by the annexation of Sophene and the Submission of Gordyene under its prince'; 'a small vassal state between Armenia and Parthian Empire'; Pompey 'gave protection to the newly acquired territory of Gordyene'; 'acknowledged the sovereignty of Rome'.
  - fix: Add these vassal pairs, with the Cliopatria shape as region: vassal_start/vassal_end parthian-empire, -95 and -87 (mirror). vassal_start kingdom-of-armenia at -87 (confidence 2), ending at -69 when Lucullus 'took over the region of Corduene' (Corduene page, 69 BC). vassal_start roman-republic after Pompey's settlement, -65 (confidence 1-2). vassal_start/vassal_end kingdom-of-adiabene, -1 and 116 (mirror). For 224/240-298, a vassal_start sasanian-empire (confidence 1) so that the 299 cession has a giver.
- `/ledger/1`: The contest's counterpart and year disagree with parthian-empire, and the 69 BC Roman takeover is missing.
  - why: Roman-Parthian Wars page: Pompey 'offered arbitration between Tigranes and the Parthian king over Corduene', a dispute between Armenia and Parthia. parthian-empire /ledger/35 opens it at -67 with kingdom-of-armenia. Corduene page: in 69 BC Lucullus 'took over the region of Corduene'.
  - fix: Add occupation_start roman-republic at -69 (confidence 2, Corduene page), with an occupation_end. Say in the contest's note that the dispute was between Tigranes and Phraates III, or move it to -67 to match parthian-empire.

Thin:
- `/ledger/2`: the end of the 66/65 BC dispute, bridged to -65 at confidence 1 (try https://en.wikipedia.org/wiki/Third_Mithridatic_War)
- `/keyframe_review/9`: 260-298: who ruled Corduene before the Peace of Nisibis (try https://en.wikipedia.org/wiki/Roman%E2%80%93Persian_Wars)
- `/keyframe_review/2`: 114-126: the Trajanic interval is bridged; Manisarus is undated (try https://en.wikipedia.org/wiki/Trajan%27s_Parthian_campaign)
- `/identity/capitals`: no capital; the page names Pinaca (Bezabde) as 'the strong fort' and Sareisa and Satalca as cities (try https://en.wikipedia.org/wiki/Corduene)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Corduene: confirmed: 'emerged from the declining Seleucid Empire'; 'From 189 to 90 BCE, it enjoyed a period of independence'
- `/ledger/1` https://en.wikipedia.org/wiki/Roman%E2%80%93Parthian_Wars: confirmed: arbitration 'over Corduene', with the year coming from 'invaded Armenia in 66/65 BC'
- `/ledger/3` https://en.wikipedia.org/wiki/Peace_of_Nisibis_(299): confirmed: spring 299; Corduene is in both lists of five satrapies
- `/ledger/4` https://en.wikipedia.org/wiki/Corduene: confirmed as reading: 'conquered again by Diocletian in the 3rd century'; peace dated 296 on this page; confidence 2 is fair

Area: No infobox on the Corduene page.

## kingdom-of-osroene - fail

- `/ledger`: Blocking: there are no vassal events; the dossier draws a client kingdom as independent for its whole life.
  - why: Osroene page: 'absorbed into the Roman Empire in 114 as a semiautonomous vassal state'; in 123 'Osroene was established as a client kingdom of the Empire'; infobox map caption: 'a tributary kingdom of the Armenian Empire under Tigranes the Great'; Wa'el 'Installed by the Parthians' 163-165. Trajan page: Abgar VII 'submitted to Trajan publicly, as a Roman protectorate'. parthian-empire /ledger/28 (vassal_start kingdom-of-osroene, -95, confidence 3) and /ledger/37 (vassal_end, -66) have no mirror here.
  - fix: Add, with the shape as region: vassal_start/vassal_end parthian-empire, -95 and -66 (mirror). vassal_start roman-empire at 114 (confidence 2, Osroene page), with vassal_end at the 115/116 annexation. vassal_start roman-empire at 118 or 123 (confidence 3, 'established as a client kingdom of the Empire'), with vassal_end at 214 before the loss. For 163-165, vassal_start/vassal_end parthian-empire (confidence 3, the Parthian nominee), beside or instead of the contest. Add the Armenian tributary status under Tigranes as a confidence 1 pair if you keep it.
- `/keyframe_review/1`: The Cliopatria shapes, all verdict 'ok', take in Nisibis, which no page gives to Osroene; this double-books land with kingdom-of-adiabene.
  - why: The shapes contain 9 of the 19 cells of the Nusaybin 40 km circle. kingdom-of-adiabene holds that circle from 36 to 164 (Adiabene page: 'Artabanus presented the city to Izates'). The 161-166 war page has the Parthians retreat to Nisibis in 165. The Mesopotamia page makes Nisibis the Roman provincial capital in 198.
  - fix: Mark the shapes _-63 to _207 and the new _118 and _161 keyframes 'adjust' with {"minus": [{"cliopatria": "Kingdom of Osroene", "year": y}, {"place": "Nusaybin", "km": 40}]}, text 'without Nisibis', at confidence 2. This also answers part of the 50 k km2 question in /keyframe_review/1.
- `/ledger/2` (applied): The ledger note misquoted the Roman-Parthian Wars page.
  - why: The page reads 'surrendering the territories of Armenia, Mesopotamia, and Adiabene back to their previous rulers and client-kings', with no year.
  - fix: Applied by the reviewer: quote corrected in the /ledger/2 note (confidence was already 2). The same misquote remains in the /keyframe_review/7 note; the author can correct it.

Thin:
- `/keyframe_review/1`: the area: Cliopatria 50.3 k km2 against the gazetteer Osroene of 73 cells (about 18.5 k km2, factor 2.7); no infobox area; noted but not resolved (try https://en.wikipedia.org/wiki/Mesopotamia_(Roman_province))
- `/keyframe_review/11`: 195: Severus 'possibly annexed some of its territory'; no land is named (try https://en.wikipedia.org/wiki/Septimius_Severus)
- `/ledger/7`: the 238-244 rump under Gordian III is left undrawn (try https://en.wikipedia.org/wiki/Gordian_III)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Trajan%27s_Parthian_campaign: confirmed: 'In 115, the Roman emperor overran northern Mesopotamia and annexed it to Rome as well'; the Osroene page has 114 (vassal) and 116 (end of independence), as the note says
- `/ledger/4` https://en.wikipedia.org/wiki/Roman%E2%80%93Parthian_War_of_161%E2%80%93166: confirmed: 'In 163 ... the Parthians intervened in Osroene', nominee 'until 165'
- `/ledger/5` https://en.wikipedia.org/wiki/Roman%E2%80%93Parthian_War_of_161%E2%80%93166: confirmed: 'Edessa was re-occupied, Mannus re-installed'
- `/ledger/6` https://en.wikipedia.org/wiki/Osroene: confirmed: 'remaining territory incorporated into the Roman province of Osroene'; 213 in the text and 214 for the province, a disagreement the note acknowledges
- `/ledger/3` https://en.wikipedia.org/wiki/Osroene: confirmed: in 123 'Osroene was established as a client kingdom of the Empire'

Area: No infobox area. The factor of 2.7 against the gazetteer region is noted in /keyframe_review/1 but left unverified.

## Cross-dossier matrix

- kingdom-of-adiabene -1 vassal_start (counterpart kingdom-of-gordyene): missing. Same batch: kingdom-of-gordyene has no vassal events.
- kingdom-of-adiabene 36 gain (counterpart parthian-empire): missing. parthian-empire (me-06-a) has no 36 loss of Nisibis; the author flagged it. Route to me-06-a.
- kingdom-of-adiabene 116 loss (counterpart roman-empire): mismatch. roman-empire occupies Parthian land from 115 (counterpart parthian-empire) and has no gain from kingdom-of-adiabene. Route to eu-04.
- kingdom-of-adiabene 116 vassal_end (counterpart kingdom-of-gordyene): missing. Same batch: kingdom-of-gordyene has no vassal events.
- kingdom-of-adiabene 117 gain (counterpart roman-empire): mismatch. roman-empire's 117 events have counterparts parthian-empire and kingdom-of-armenia, none kingdom-of-adiabene. Route to eu-04.
- kingdom-of-adiabene 165 loss (counterpart roman-empire): mismatch. Nisibis is lost to Rome in 165 by both kingdom-of-adiabene and parthian-empire (/ledger/59); roman-empire has only a contest_end with parthian-empire. One loser must be chosen.
- kingdom-of-adiabene 379 dissolve (counterpart sasanian-empire): exception. sasanian-empire is owned by another part of me-06 running in parallel; not written yet.
- parthian-empire -95 vassal_start (counterpart kingdom-of-adiabene): missing. Adiabene has no vassal events; its page has Parthian vassalage from 145 BC (author to add, fix 1).
- parthian-empire -87 vassal_end (counterpart kingdom-of-adiabene): missing. As above.
- parthian-empire -63 loss (counterpart kingdom-of-adiabene): mismatch. parthian-empire carves out Cliopatria's misplaced Adiabene shape at -63 (confidence 1); Adiabene has no -63 gain (founded -164; the shape is verdict 'wrong'). Route to me-06-a to drop the loss or use the corrected core.
- roman-empire 299 gain (counterpart sasanian-empire): mismatch. The Tigris-Greater Zab polygon takes 24 cells of Adiabene's corrected core, which Adiabene keeps to 379 with no 299 loss (Adiabene fix 2).
- kingdom-of-commagene 17 loss (counterpart roman-empire): missing. roman-empire (eu-04) has no 17 gain of Commagene and keeps it a client from -27 to 72; the author flagged it.
- kingdom-of-commagene 38 gain (counterpart roman-empire): missing. roman-empire has no 38 loss of Commagene; flagged.
- kingdom-of-commagene 38 gain (counterpart roman-empire): missing. Cilician strip: roman-empire has no 38 loss of Cilicia to Commagene.
- kingdom-of-commagene 72 loss (counterpart roman-empire): matched. roman-empire /ledger/55.
- kingdom-of-commagene 72 loss (counterpart roman-empire): mismatch. roman-empire /ledger/56 gains the Cilician strip from 'Cilicia Trachea (client kingdom)', not kingdom-of-commagene; both use the gazetteer Cilicia (the wrong land).
- roman-empire -27 vassal_start (counterpart kingdom-of-commagene): missing. Commagene has no vassal events (fix 3).
- roman-empire 72 vassal_end (counterpart kingdom-of-commagene): missing. As above.
- kingdom-of-cappadocia -63 loss (counterpart kingdom-of-commagene): mismatch. Cappadocia /ledger/13 (confidence 1) gives Commagene 21 cells, 17 of them inside Commagene's -63 shape, which Commagene carries back to -163: the cells are double-booked from -163 to -64. Both rest on the misplaced Cliopatria shape (Commagene fix 1). Route to me-05.
- parthian-empire -95 vassal_start (counterpart kingdom-of-gordyene): missing. Gordyene has no vassal events (fix 1).
- parthian-empire -87 vassal_end (counterpart kingdom-of-gordyene): missing. As above.
- kingdom-of-gordyene -66 contest_start (counterpart parthian-empire): mismatch. parthian-empire's contest over Gordyene has counterpart kingdom-of-armenia at -67.
- kingdom-of-gordyene 299 loss (counterpart roman-empire): mismatch. roman-empire /ledger/107 gains from sasanian-empire a polygon containing 0 of Gordyene's 54 cells; no roman-empire event takes Corduene. Route to eu-04.
- kingdom-of-osroene 115 loss (counterpart roman-empire): mismatch. roman-empire /ledger/69 gains northern Mesopotamia (Jazira) from parthian-empire, not from kingdom-of-osroene.
- kingdom-of-osroene 118 gain (counterpart roman-empire): missing. roman-empire has no 117/118 loss to kingdom-of-osroene (its 117 loss of northern Mesopotamia goes to parthian-empire).
- kingdom-of-osroene 163 contest_start (counterpart roman-empire): mismatch. roman-empire's 161-165 contest is with parthian-empire; the Osroene page has a Parthian nominee, which is a vassal relation (Osroene fix 1).
- kingdom-of-osroene 214 loss (counterpart roman-empire): matched. roman-empire /ledger/87 (confidence 1 there, 3 here).
- parthian-empire -95 vassal_start (counterpart kingdom-of-osroene): missing. Osroene has no vassal events (fix 1).
- parthian-empire -66 vassal_end (counterpart kingdom-of-osroene): missing. As above.
- kingdom-of-adiabene 36 gain (counterpart parthian-empire): mismatch. Nisibis (Nusaybin 40 km, 9 of 19 cells) is inside Osroene's 'ok' Cliopatria shapes from 36 to 164 (Osroene fix 2).
- kingdom-of-gordyene -189 found (counterpart seleucid-empire): exception. seleucid-empire has no event for the foundings of Gordyene (-189), Adiabene (-164), Commagene (-163) or Osroene (-132); the found events need no mirror, but the predecessor land is not given up there. Noted for the seleucid owner.

## Problems

- Reviewer edits applied: kingdom-of-adiabene /ledger/5 (confidence 3 to 2, quote) and kingdom-of-osroene /ledger/2 (quote); both re-validated with 0 errors and 0 warnings.
- kingdom-of-armenia (eu-19) and sasanian-empire (me-06, parallel part) are not written yet; their sides of the cross-checks could not be read.
- All four dossiers leave out the client and vassal relations that define them (rule 4). The same pattern is likely in the author's other batches.
- Overlaps were measured by resolving region specs with history/tools/gazetteer.py on the r5 grid (about 253 km2 per cell).
