# me-06-b notes (Parthia and the Sasanians, part b)

Written 2026-10-19. States: kingdom-of-adiabene, kingdom-of-commagene, kingdom-of-gordyene, kingdom-of-osroene. All four validate (0 errors, 0 warnings, `--resolve` clean). Every page was read with WebFetch in this run.

## Pages and budget
- Commagene (2 of 1-2): Commagene; Antiochus IV of Commagene.
- Osroene (5 of 5): Osroene; Trajan's Parthian campaign; Roman-Parthian War of 161-166; Mesopotamia (Roman province); Roman-Parthian Wars.
- Adiabene (6, one over 5): Adiabene; Trajan's Parthian campaign; Roman-Parthian Wars; Mesopotamia (Roman province); Roman-Parthian War of 161-166; Peace of Nisibis (299) opened only to see whether it names Adiabene (it does not).
- Gordyene (5 of 5): Corduene; Adiabene; Peace of Nisibis (299); Jovian (emperor); Roman-Parthian Wars.
- Also opened, not cited in any dossier: Tigranes the Great, Parthian Empire, Parthian war of Caracalla, Peace of Nisibis (disambiguation).

## Pages that would not load
Roman-Parthian War of 195-197; Parthian campaigns of Septimius Severus; Peace of Nisibis (298); Peace of Nisibis (363) (three spellings); Julian's Persian campaign; Roman-Parthian_wars (lower-case w; the capital-W title loads). Severus' campaigns are therefore sourced from the Osroene, Adiabene and Roman-Parthian Wars pages only, and the 363 return of Corduene from the Jovian page.

## Kingdom of Adiabene
- All eight Cliopatria shapes are verdict wrong: they lie on the Tigris west of Mosul between Nisibis and Cizre (box 41.18-42.76E, 36.35-37.51N) and contain neither Arbela (the capital, 44.0E) nor Nineveh. Corrected to Arbil governorate plus a 60 km circle round Nineveh, plus a 40 km circle round Nisibis for 36-164 (Artabanus II's grant of 36). The rendering agent should not use the Cliopatria outline.
- Dates: founded c. 164 BC (coinage), Parthian from 145-141 BC (Mithridates I) on this page; the parthian-empire dossier (me-06-a) has the submission about 95 BC (Mithridates II) and Tigranes retaking it 88-85 BC. Ends c. 379 (province), not 370.
- Bridges at confidence 1 or without a page: 260-286 (no Cliopatria shape, page silent); the end of the Gordyene dependency in 116; Diocletian's 'territory in Adiabene' (Mesopotamia page, lost 363) has no land named, so nothing is drawn.
- Matching entries other dossiers lack: parthian-empire has no loss of Nisibis in 36 and no 116 loss of Adiabene; roman-empire has no Assyria events for Adiabene (116/117) and no 165 gain of Nisibis.

## Kingdom of Commagene
- Ends in 72, not 77; annexed to Syria once already in 17 and restored in 38 (the Cliopatria gap 23-42 roughly fits). roman-empire (eu-04) keeps it a client from 27 BC to 72 without the 17 loss and the 38 gain, and the matching Cilicia Trachea gain/loss of 38 and 72.
- Undated on both pages: Caligula's deposition of Antiochus IV (between 38 and 41), his gain of 'parts of Armenia' in 61, Armenian suzerainty under Mithridates Callinicus, and when Zeugma was Commagenian.
- Gazetteer name needed: Cilicia Trachea (coastal 'wild' Cilicia); the Cilician strip is drawn with {"region": "Cilicia"} which is the plain.

## Kingdom of Gordyene
- The Corduene page is thin (no infobox, no capital, some undated or garbled sentences). Cliopatria shapes kept (ok). The dossier ends in 299, not 259: the Peace of Nisibis cedes Corduene to Rome, the Jovian page has it a Roman province until 363, and the 260-298 stretch is a bridge (gordyene_260, confidence 1: who ruled Gordyene then is on no page).
- No capital named; identity.capitals is empty.
- Gazetteer name needed: Gordyene (Corduene), the Bohtan country on the left bank of the Tigris.

## Kingdom of Osroene
- Cliopatria 50 k km2 against a gazetteer 'Osroene' of 18.5 k km2; no infobox area; the page says only 'perhaps roughly coterminous' with the Roman province. Shapes kept (ok), unverified on area.
- Disagreements: independence 132 BC (infobox) or 136 BC (text); absorbed by Trajan in 114 (Osroene page), 115 (Trajan page), 116 (Quietus); Severus 195 leaves Abgar VIII his kingdom (Osroene page) or makes Osroene a full province (Mesopotamia page); end 213 or 214.
- New keyframes for the Cliopatria gaps 118-126 (restoration after Trajan) and 161-164 (the Parthian-installed Wa'el, drawn as a contest with roman-empire).
- Not drawn: Tigranes' overlordship (a map caption), the rump of 238-244 (debated), Severus' possible annexation of 'some of its territory'. Anthemusia (Batnae), a semi-autonomous principality annexed by Rome in 115, could be a small dossier.

## For the reviewer
Counterparts in my ledgers are slugs: seleucid-empire (founding), roman-empire, parthian-empire. parthian-empire (me-06-a) carves Adiabene out of its outline in -63 with {cliopatria: Kingdom of Adiabene} (a loss event), which relies on the misplaced shape; its vassal tint for Adiabene uses the gazetteer's Assyria region, which is closer to the corrected land. The Adiabene correction here (Arbil + Nineveh) should be preferred for that loss.

## Fix pass (2026-10-19), after the review (verdict fail for all four)
All four dossiers re-validated with `--resolve`: 0 errors, 0 warnings. Pages were re-opened with WebFetch for every date, region or source I changed; what I could not confirm is marked. Details sit in each dossier's `notes` and in the changed events ("[fix me-06-b ...]").

### Pages opened in this pass
Adiabene; Tigranes the Great; Shapur I; Corduene; Mesopotamia (Roman province); Commagene; Antiochus IV of Commagene; Cilicia; Samsat; Roman-Parthian War of 58-63; Zeugma (Commagene); Third Mithridatic War; Parthian Empire; Mithridates II of Parthia; Roman-Parthian Wars; Roman-Persian Wars; Trajan's Parthian campaign; Osroene; Gordian III; Septimius Severus. Not cited in a dossier: Parthian Empire (it has nothing on Mithridates II and the three kingdoms; the Mithridates II page has it) and the Peace of Nisibis disambiguation.

### Kingdom of Adiabene
- Vassal chain added: Parthian from -141 (Adiabene page; parthian-empire has -95, left to me-06-a), Armenian -87 to -66 (Tigranes page; the end is a confidence-1 bridge because the page never says when Armenian control of Adiabene ended), Parthian again from -66, interrupted by Trajan 116-117, Sasanian from 224 (infobox) to 379.
- 299 loss and 363 gain of the Tigris-to-Greater-Zab part, keyframe 287 split at 299 and 363. I drew it as the intersection of the core with eu-04's polygon (roman-empire /ledger/107, 24 of the core's 98 cells) instead of the reviewer's 'Nineveh 60 km minus Arbil' (40 cells): the minus form has 19 cells outside the Roman polygon and leaves 3 overlapping cells. Disagreement is about method only. The polygon is eu-04's, unverified on a page: the Mesopotamia page gives no year and no land for Diocletian's Adiabene, the Peace of Nisibis (299) page does not name Adiabene. eu-04 should check the polygon; if it changes, this region follows.
- Nisibis 165: noted that parthian-empire /ledger/59 loses the same city; the 161-166 page names no Adiabene. The three owners (me-06-a, eu-04, me-06-b) need one loser.
- For me-06-a: parthian-empire /ledger/40 (-63 loss of Adiabene from the misplaced shape) contradicts a Parthian vassal Adiabene -66..116; parthian-empire /ledger/26 has -95, the Adiabene page -145/-141.
- Thin items checked: Shapur I (silent on 260-286; names 'Ardashir, governor of Adiabene'), Corduene (silent on any Adiabene dependency), Tigranes (88-85 BC retaking, 66 BC annexation of conquests, no end date for Adiabene).

### Kingdom of Commagene
- The Cliopatria outline is wrong in every keyframe (_-63, _43, _68 now verdict wrong). Region everywhere: Adiyaman province + 15 km circle at Samosata (the Samosata cell is in Sanliurfa in the grid) + the part of Gaziantep north of 37.1N (the page: 'Adiyaman and northern Antep'): 38 cells, 9.6 k km2, near Cliopatria's 9.6 k km2, 0 cells shared with Cappadocia's -64 shape. For me-05: Cappadocia /ledger/13 (-63 loss of 17 cells to Commagene) rests on the misplaced shape. For eu-03: Roman Republic's -63 shape holds 24 of the 38 corrected cells.
- Cilician strip is now a polygon (Coracesium to the Lamos, south of 37.0N, 62 cells). The Cilicia page confirms Rugged Cilicia is the western part from Coracesium but gives no Lamos boundary and does not say which part Antiochus IV got, so the polygon is the reviewer's reading, confidence 2; it is generous (62 cells against the kingdom's 38). Gazetteer: 'Cilicia Trachea' still wanted.
- Roman client chain: roman-republic -64 (Pompey's ally; the page also says he 'kept Commagene independent from the Romans', so 'client' is a reading), roman-empire -27 to 16, 38 to 39, 41 to 71 (to 72). Deposition by Caligula bridged to 40 (confidence 1); restoration 41 (confidence 3, both pages date it). My earlier note that the pages give no date for the restoration was wrong. Keyframes _38 (38-39) and _41 (41-42). Samosata coordinates now 37.58N 38.48E (Samsat page).
- For eu-04: roman-empire keeps the client tint unbroken from -27 to 72, though the kingdom was a province 17-38 (and the deposition of about 40).
- Thin items: the 58-63 war page names no recipient or district for 'outlying western parts of Armenia' (the 61 gain stays undrawn); the Zeugma page has nothing on Commagene; the Tigranes page has nothing on Commagene.

### Kingdom of Gordyene
- Vassal and occupation chain added (Cliopatria shape as region): Parthian from 95 BC (Mithridates II page: 'by 95 BC ... had acknowledged his authority'), Armenian -87 to -69 (Tigranes page), Roman occupation -69 to -65 (Corduene page: Lucullus 'took over the region of Corduene'), Roman protection -65 to -27 (Corduene page, undated sentences, confidence 1), Adiabenian dependency -1 to 116 (mirror of the Adiabene events), Sasanian from 240 (a confidence-1 bridge) to the 299 cession. Contest moved from -66 to -67 (Tigranes page) to agree with parthian-empire /ledger/35; the note now says the dispute was between Tigranes and Phraates III.
- The Corduene page contradicts itself ('Lucullus took over the region' against 'Tigran retained Gordyene and Nisibis, which Pompeius withheld from the Parthians'); the Roman protection span is a reading. The Third Mithridatic War, Roman-Persian Wars and Trajan's Parthian campaign pages are silent on Gordyene for 65 BC, 260-298 and 114-126, so those bridges stay.
- Still no capital: the Corduene page names Sareisa, Satalca and Pinaca (Bezabde) as cities and no capital. Gazetteer: a region 'Gordyene (Corduene)' is still wanted.

### Kingdom of Osroene
- Vassal chain added: Parthian -95 to -66 (Mithridates II page and the Roman-Parthian Wars page; mirrors parthian-empire /ledger/28 and /37), Roman 114-115 (Osroene page 'semiautonomous vassal state'), Roman from 118 with a Parthian-nominee interruption 163-165 (king list 'Installed by the Parthians') and a Roman restart in 165, to 214. The contest of 163-165 stays beside the Parthian vassal. The Armenian tributary status under Tigranes (infobox caption, no year) is not drawn: it would overlap the Parthian span and the Tigranes page has no sentence on Osroene.
- Nisibis removed from all shapes and keyframes (verdicts now adjust, confidence 2, 171-174 cells). Disagreement with the page, not the reviewer: the Osroene page says the eastern boundary 'may have extended to Nisibis'; I followed the reviewer because the Adiabene page dates the grant of Nisibis to 36, the 161-166 page has Rome take it in 165 and the Mesopotamia page has it the capital of Mesopotamia in 198. After the cut the shapes are still about 48 k km2 against the gazetteer's 18.5 k km2; the Osroene and Mesopotamia pages give no area, so the area stays unresolved.
- Misquote in the 118 keyframe note corrected. Septimius Severus page: annexed 'the Kingdom of Osroene' (194 on its sequence), Abgar IX 'essentially only the ruler of Edessa' (197): a third reading beside the Osroene and Mesopotamia pages; no land named, nothing cut. Gordian III page: nothing on Osroene, the 238-244 rump stays undrawn.

### Routing
- eu-04 (roman-empire): the 299 polygon vs Adiabene (24 cells); 363 return; Commagene tint -27..72 vs the 17-38 province and the 40 deposition; no Osroene events for 114-115, 118, 163-165; Nisibis loser in 165.
- me-06-a (parthian-empire): Adiabene -95 vs -141 and the -63 loss; Nisibis 36 and 165.
- me-05: Cappadocia /ledger/13 and the Commagene shape. eu-03: Roman Republic -63 shape holds Commagene land; no Commagene (-64) and Corduene (-69, -65) events. eu-19 (kingdom-of-armenia): Adiabene and Gordyene as Armenian vassals -87 to -66/-69; Osroene tributary not drawn.
