# Review of batch me-05-b (2026-10-19)

Reviewer: adversarial review per history/briefs/reviewer-brief.md. All three dossiers validate (0 errors, 0 warnings with --resolve). Neighbour dossiers read: kingdom-of-kush, roman-republic, greek-city-states, cyrenaica, macedonian-empire, kingdom-of-lysimachus, antigonid-dynasty (and kingdom-of-numidia, carthage, greek-colonies, kingdom-of-bithynia, achaemenid-empire, nanda-empire, thracian-kingdom: no events with this batch). Not written yet (exception): seleucid-empire, ankhwennefer, nabataeans, antigonid-macedonia and the other Context slugs.

## ptolemaic-kingdom: fail

Area: The infobox gives no area (founded 305, ended 30 BC); the author says so. Cliopatria -247 shape (247-240) is 782,800 km2. The author's quoted shape areas match shapes.csv.

### Findings

- **/ledger/58/counterpart, /ledger/59/counterpart** (applied by reviewer): The 30 BC loss and dissolve named roman-empire, which has no dossier and in the roman-republic dossier's model begins only in 27 BC.  
  Why: roman-republic.json runs to -27 and its /ledger/214 records the August 30 BC gain of Egypt from ptolemaic-kingdom (Egypt (Roman province) page, c3).  
  Fix: Counterpart set to roman-republic in both events (applied; validator clean). The author may also set identity.successors[0].slug to roman-republic.
- **/keyframe_review/11, /ledger/17, /ledger/18**: The 281-280 shape's extra 95 k km2 north of the Aegean (bbox to 42.43 N) is recorded as a Ptolemaic gain from Lysimachus (281) and a loss to nobody (279), but it matches Ptolemy Keraunos's Macedon, which was never part of the Ptolemaic kingdom.  
  Why: Ptolemy Keraunos page: he 'was displaced in favour of his younger brother Ptolemy II', 'formally relinquished his claim to the Egyptian throne', was acclaimed at Lysimachia after Seleucus's murder (September 281) and 'seized the throne of Macedon'; killed by the Gauls in early 279. kingdom-of-lysimachus /ledger/23 (-281) gives Macedon, Thessaly and Thrace to 'Ptolemy Keraunos (Macedon and Thrace, 281-279)'. The Ptolemaic page's 'fresh conquests as far north as Thrace' is undated and does not support 95 k km2 of mainland.  
  Fix: Mark keyframe ptolemaic-kingdom_-281 'wrong' (or 'adjust') with correction {cliopatria: Ptolemaic Kingdom, year: -283} and a note naming Keraunos; delete /ledger/17 and /ledger/18 (or replace them with a small undated coastal holding if a page supports it).
- **between /ledger/34 and /ledger/35 (c. 204)**: No loss of Lower Nubia to Kush during the Great Theban Revolt: the ledger gains Lower Nubia in 275 and again in 155 with no loss in between.  
  Why: Great Theban Revolt page (the author's own source): 'the Kingdom of Kush of Meroe took advantage of the situation to invade Egypt and Lower Nubia from the south' and 'take control of all Ptolemaic territories south of Aswan, including the island of Philae'. kingdom-of-kush /ledger/14 records a -204 gain of Lower Nubia from ptolemaic-kingdom (Kingdom of Kush page, c2).  
  Fix: Add {year: -204, type: loss, counterpart: kingdom-of-kush, region: {region: Lower Nubia}, confidence 2, source Great_Theban_Revolt}; the 205 Thebaid keyframe correction should also drop Lower Nubia.
- **/keyframe_review/31/correction and the ledger 58-47 BC**: Cyprus is kept Ptolemaic 'unchanged, from 105 to 35' although Rome annexed it in 58 and Caesar restored it in 47; neither event is in the ledger.  
  Why: roman-republic /ledger/173 (-58 gain Cyprus from ptolemaic-kingdom, Roman Cyprus page, c3: 'Cato the Younger was sent to annex the island') and /ledger/183 (-47 loss Cyprus to ptolemaic-kingdom, c3: 'Julius Caesar ... returned control of Cyprus to the Ptolemaic Kingdom'). The Ptolemaic Kingdom page also says Rome 'annexed both Libya and Cyprus' (undated). The author's notes flag it as not on any page opened; the page is https://en.wikipedia.org/wiki/Roman_Cyprus.  
  Fix: Add -58 loss Cyprus (roman-republic) and -47 gain Cyprus (roman-republic), both c3 from Roman_Cyprus; add a new keyframe ptolemaic-kingdom_-58 (from -58 to -48) = {minus: [{cliopatria: Ptolemaic Kingdom, year: -110}, {region: Cyprus (island)}]} and narrow the 110 correction text accordingly.
- **/keyframe_review/6/correction and the ledger 308-300**: The 307 keyframe adds Cyrenaica for 307-302 and the ledger has no loss of Cyrenaica after 313, yet the pages have it in revolt until about 300.  
  Why: Ptolemy I Soter page: 'Cyrenaica, after a series of rebellions, was finally subjugated in about 300 and placed under his stepson Magas'; Magas of Cyrene page: 'Around 300 BC, Ptolemy dispatched Magas ... to reconquer Cyrene'. cyrenaica /ledger/4 (-305 gain from ptolemaic-kingdom) and /ledger/7 (-300 loss to ptolemaic-kingdom) have no mirror here.  
  Fix: Add a loss of Cyrenaica (counterpart cyrenaica, year agreed with the cyrenaica dossier: 305, c1-2) and a gain c. 300 (c2, Magas page 'Around 300 BC ... to reconquer Cyrene'); drop Cyrenaica from the 307 correction (keep the Cliopatria shape minus Cyprus) and start Cyrenaica in the 301 correction from 300.
- **/ledger/0 (and a missing vassal_end)**: The founding is drawn as full rule from 323 with no vassal relation, while the macedonian-empire dossier holds Ptolemy's Egypt as its vassal 323-321 and records a 321 loss of Egypt and Libya to this kingdom.  
  Why: macedonian-empire /ledger/43 (-323 vassal_start ptolemaic-kingdom, c3), /ledger/46 (-321 vassal_end), /ledger/49 (-321 loss of 'Egypt and Libya'). The Ptolemaic page itself: 'Ptolemy ruled Egypt from 323 BC, nominally in the name of the joint kings Philip III and Alexander IV'.  
  Fix: Add {year: -323, type: vassal_start, counterpart: macedonian-empire, region: the found region, c3, Ptolemaic_Kingdom} and a vassal_end in 321 (Triparadisus, matching macedonian-empire) or another year agreed with group eu-02; say in notes which.
- **/ledger/4, /ledger/7, /ledger/8**: Counterpart antigonid-dynasty for 315-311, but that dossier begins in 306; until its 306 split the macedonian-empire dossier holds Antigonus's Syria.  
  Why: antigonid-dynasty identity.start -306; macedonian-empire /ledger/63 (-306 split antigonid-dynasty: 'Greece, Asia Minor, Syria, Phoenicia and northern Mesopotamia'). The author's counterparts_needing_dossiers proposes antigonus-monophthalmus for 306-301 only.  
  Fix: Use macedonian-empire as counterpart for 315-311 (and ask eu-02 for the 315 gain of Syria), or extend the proposed antigonus-monophthalmus dossier back to 315 and list it so.
- **between /ledger/35 and /ledger/36 (201)**: No loss for Philip V's 201 seizure of Ptolemaic Samos, Miletus and Carian footholds.  
  Why: antigonid-dynasty /ledger/52 (-201 gain from ptolemaic-kingdom: 'Miletus, Samos and footholds in Caria', Philip V of Macedon page, c2).  
  Fix: Add a -201 loss (counterpart antigonid-dynasty, c2, citing the Philip V page) or explain in notes why the land was not Ptolemaic.
- **/ledger/57**: The Donations gain is dated 34 only and omits Cilicia Aspera, though the page records an earlier donation at Antioch in 36 and the roman-republic dossier gives Cilicia Aspera to Cleopatra in 36 and takes it back in 30.  
  Why: Donations of Alexandria page: 'a similar donation ceremony had taken place two years earlier at Antioch in 36 BC'. roman-republic /ledger/200 (-36 loss Cilicia Aspera to ptolemaic-kingdom, c3, Cilicia (Roman province) page: 'Marc Antony gave Cyprus and Cilicia Aspera to Cleopatra VII') and /ledger/213 (-30 gain Cilicia Aspera, c1). /ledger/211 (-31 gain Cyprus, c3) also has no Ptolemaic loss in 31.  
  Fix: Add a -36 gain of Cilicia Aspera (roman-republic, c3, Cilicia_(Roman_province)) and losses of Cyprus (-31) and Cilicia Aspera (-30) to roman-republic, or fold them into the -30 dissolve region and say so; the 34 keyframe should include Cilicia Aspera.
- **/ledger/2**: Cyprus 318 is a confidence-1 bridge 'neither page dates', but the Ptolemy I page dates a protectorate over Cyprus to 318.  
  Why: Ptolemy I Soter page: 'His first occupation of Syria was in 318' and 'he established at the same time a protectorate over the petty kings of Cyprus'.  
  Fix: Make it type vassal_start (counterpart nobody, region Cyprus (island)), confidence 2, quoting that sentence; the full gain can stay with the Salamis-era rule if a page supports it.

### Gaps for a gap-filler

- /ledger/1: Year of the Cyrenaica conquest (322 bridge, c1) (try https://en.wikipedia.org/wiki/Ophellas)
- /ledger/12: End of the Corinth/Sicyon garrison (302 bridge, c1); Demetrius took Corinth in 304-303 per macedonian-empire /ledger/65 (try https://en.wikipedia.org/wiki/Demetrius_I_of_Macedon)
- /ledger/19: Lower Nubia 275 (c1); the Kush page gives '275 or 274 BC' (try https://en.wikipedia.org/wiki/Kingdom_of_Kush)
- /ledger/27: Cyrenaica's return c. 247 (c1) (try https://en.wikipedia.org/wiki/Berenice_II)
- /ledger/50: Lower Nubia 155 (c1); the Ptolemaic page says 'Throughout the 160s and 150s BC, Ptolemy VI also reasserted Ptolemaic control over the northern part of Nubia' (Dodecaschoenus): c2 possible (try https://en.wikipedia.org/wiki/Dodecaschoenus)
- /wars/4 (Third Syrian War): The loss of the Cyclades at Andros is in the war note but has no ledger event or year (try https://en.wikipedia.org/wiki/Battle_of_Andros)
- /identity/rulers: No rulers list (try https://en.wikipedia.org/wiki/Ptolemaic_dynasty)

### Spot checks

- /ledger/3, https://en.wikipedia.org/wiki/Ptolemy_I_Soter: confirmed
- /ledger/4, https://en.wikipedia.org/wiki/Ptolemy_I_Soter: confirmed
- /ledger/9, https://en.wikipedia.org/wiki/Ptolemy_I_Soter: confirmed
- /ledger/10, https://en.wikipedia.org/wiki/Ptolemaic_Kingdom: confirmed
- /ledger/16, https://en.wikipedia.org/wiki/Ptolemaic_Kingdom: confirmed
- /ledger/32, https://en.wikipedia.org/wiki/Syrian_Wars: confirmed
- /ledger/34, https://en.wikipedia.org/wiki/Great_Theban_Revolt: confirmed
- /ledger/37, https://en.wikipedia.org/wiki/Syrian_Wars: confirmed
- /ledger/44, https://en.wikipedia.org/wiki/Great_Theban_Revolt: confirmed
- /ledger/48, https://en.wikipedia.org/wiki/Ptolemy_VIII_Physcon: confirmed
- /ledger/53, https://en.wikipedia.org/wiki/Ptolemy_VIII_Physcon: confirmed
- /ledger/57, https://en.wikipedia.org/wiki/Donations_of_Alexandria: confirmed (but the page also has a donation at Antioch in 36 BC)
- /ledger/17, https://en.wikipedia.org/wiki/Ptolemaic_Kingdom: not on page (undated Thrace conquests only; the land is Keraunos's Macedon, Ptolemy_Keraunos page)
- /ledger/2, https://en.wikipedia.org/wiki/Ptolemy_I_Soter: mis-dated as undated: the page dates a protectorate over Cyprus to 318

## laomedon: fail

Area: No infobox on the Laomedon of Mytilene page.

### Findings

- **/ledger (missing vassal_start -323 and vassal_end -318)**: The satrapy is drawn as an independent state; the macedonian-empire dossier holds it as a vassal 323-319 and those events have no mirror here.  
  Why: macedonian-empire /ledger/41 (-323 vassal_start laomedon, Partition of Babylon, c3) and /ledger/50 (-319 vassal_end laomedon, c1). Laomedon of Mytilene page: 'obtaining in the division of the provinces, after the king's death in 323 BC, the important government of Syria'; 'This he was still allowed to retain on the second partition at Triparadisus in 321 BC'. Cliopatria's seed lists the row as a member of the (Macedonian Empire) umbrella 323-319.  
  Fix: Add {year: -323, type: vassal_start, counterpart: macedonian-empire, region: the found region, c2, Laomedon_of_Mytilene} and {year: -318, type: vassal_end, counterpart: macedonian-empire, c2, Ptolemy_I_Soter}; ask eu-02 to move its vassal_end to 318 or keep 319 (within one year).

### Spot checks

- /ledger/0, https://en.wikipedia.org/wiki/Laomedon_of_Mytilene: confirmed
- /ledger/1, https://en.wikipedia.org/wiki/Ptolemy_I_Soter: confirmed (318; the Laomedon page gives no year for Nicanor's invasion)
- /ledger/2, https://en.wikipedia.org/wiki/Ptolemy_I_Soter: confirmed
- /identity/capitals, https://en.wikipedia.org/wiki/Laomedon_of_Mytilene: confirmed: the page names no seat

## perdiccas: fail

Area: The Perdiccas page infobox is a person's; no area.

### Findings

- **/keyframe_review/0** (applied by reviewer): Verdict 'ok' on a shape that runs to 319 while the dossier ends in 320.  
  Why: Perdiccas page: 'killed him in 320 BC', 'probably in the summer of 320 BC'; research brief: a verdict that changes only the years gives the shape unchanged and says so in text.  
  Fix: Verdict set to adjust with correction {cliopatria: Perdiccas, year: -323, text: unchanged, ending 320} (applied; validator clean).
- **/ledger (missing vassal_start -323 and vassal_end -320)**: The regency's Babylonia is drawn as an independent state; the macedonian-empire dossier holds it as a vassal 323-321 and those events have no mirror here.  
  Why: macedonian-empire /ledger/42 (-323 vassal_start perdiccas, c2) and /ledger/47 (-321 vassal_end perdiccas: 'Babylonia, reassigned ... to Seleucus', Partition of Triparadisus page, c3). Seed: member of the (Macedonian Empire) umbrella 323-319.  
  Fix: Add vassal_start -323 (counterpart macedonian-empire, c2, Partition_of_Babylon) and vassal_end -320 (c3, Perdiccas page), or agree with eu-02 that the regency row is the empire's own seat and have eu-02 drop its two events; record the choice in notes.
- **/identity/successors/0 and /ledger/1/counterpart**: Successor seleucid-empire (from Cliopatria's bbox only) and a dissolve with no counterpart, while the macedonian-empire dossier hands Babylonia to Seleucus as its own satrap in 321 (vassal_start seleucid-empire, /ledger/48) and the Seleucid row starts only in 318.  
  Why: macedonian-empire /ledger/47-48 (Partition of Triparadisus page). The author's notes say no page dates the hand-over.  
  Fix: Name macedonian-empire (Seleucus as satrap) as the successor of the land and as the dissolve counterpart, or keep seleucid-empire and say the land is the empire's vassal 320-312.

### Spot checks

- /ledger/0, https://en.wikipedia.org/wiki/Perdiccas: confirmed (regency 323 BC - 320 BC in the infobox; Partition of Babylon not opened)
- /ledger/1, https://en.wikipedia.org/wiki/Perdiccas: confirmed (320 BC throughout the page)
- /identity/capitals/0, https://en.wikipedia.org/wiki/Perdiccas: confirmed ('had chosen to centre the empire at Babylon'); 44.42 E 32.54 N inside the shape bbox

## Cross-dossier matrix

- ptolemaic-kingdom -323 found (macedonian-empire) -> macedonian-empire -323 vassal_start: mismatch - macedonian-empire holds Ptolemy as vassal 323-321 (/ledger/43, 46) and loses Egypt and Libya to him in 321 (/ledger/49); the Ptolemaic ledger has no vassal events and no 321 event.
- ptolemaic-kingdom -322 gain (cyrenaica) -> cyrenaica -322 loss: matched
- ptolemaic-kingdom -318 gain (nobody) -> none: exception - Cyprus; counterpart nobody (should be a vassal_start, see fixes).
- ptolemaic-kingdom -318 gain (laomedon) -> laomedon -318 loss: matched
- ptolemaic-kingdom -315 loss (antigonid-dynasty) -> none: mismatch - antigonid-dynasty starts in -306; macedonian-empire holds Antigonus's Syria until its 306 split and has no 315 gain.
- ptolemaic-kingdom -308 occupation_start (greek-city-states) -> none: missing - greek-city-states (eu-01) has no 308 occupation of Corinth/Sicyon/Megara.
- ptolemaic-kingdom -306 loss (antigonid-dynasty) -> antigonid-dynasty -306 gain: matched
- ptolemaic-kingdom -302 occupation_end (greek-city-states) -> macedonian-empire -304 loss: mismatch - greek-city-states has no mirror; macedonian-empire /ledger/65 has Demetrius taking Corinth from the macedonian-empire in 304-303 while this dossier has Ptolemy holding it to 302.
- ptolemaic-kingdom -301 gain (antigonid-dynasty) -> antigonid-dynasty -301 loss: matched
- ptolemaic-kingdom -295 gain (antigonid-dynasty) -> antigonid-dynasty -294 loss: matched - one year apart
- ptolemaic-kingdom -281 gain (kingdom-of-lysimachus) -> kingdom-of-lysimachus -281 loss: mismatch - Lysimachus's dossier gives Macedon, Thessaly and Thrace to Ptolemy Keraunos, not to the Ptolemaic kingdom; the Ptolemaic events should go.
- ptolemaic-kingdom -279 loss (nobody) -> none: exception - to be removed with the 281 gain.
- ptolemaic-kingdom -275 gain (kingdom-of-kush) -> kingdom-of-kush -274 loss: matched - one year apart
- ptolemaic-kingdom -274 loss (cyrenaica) -> cyrenaica -276 gain: mismatch - two years apart; Magas page infobox: king 276-250, coronation 'disputed' (283-280 or 276/274). Owners to agree one year.
- ptolemaic-kingdom -271 gain (seleucid-empire) -> none: exception - seleucid-empire not written yet (me-05, other part).
- ptolemaic-kingdom -253 loss (seleucid-empire) -> none: exception - seleucid-empire not written yet.
- ptolemaic-kingdom -247 gain (cyrenaica) -> cyrenaica -246 loss: matched - one year apart
- ptolemaic-kingdom -241 gain (seleucid-empire) -> none: exception - seleucid-empire not written yet.
- ptolemaic-kingdom -219 loss (seleucid-empire) -> none: exception - seleucid-empire not written yet.
- ptolemaic-kingdom -205 loss (ankhwennefer) -> none: exception - ankhwennefer not written yet (me-05); covers Horwennefer 205-199 too.
- ptolemaic-kingdom -199 gain (ankhwennefer) -> none: exception - ankhwennefer not written yet.
- ptolemaic-kingdom -198 loss (seleucid-empire) -> none: exception - two events (Coele-Syria; Caria and Cilicia); seleucid-empire not written yet.
- ptolemaic-kingdom -197 loss (ankhwennefer) -> none: exception - ankhwennefer not written yet.
- ptolemaic-kingdom -191 gain (ankhwennefer) -> none: exception - ankhwennefer not written yet.
- ptolemaic-kingdom -186 gain (ankhwennefer) -> none: exception - ankhwennefer not written yet; its Cliopatria row runs to 171, the page ends the revolt 27 August 186.
- ptolemaic-kingdom -170 occupation_start (seleucid-empire) -> none: exception - seleucid-empire not written yet (occupation_end 168 likewise).
- ptolemaic-kingdom -163 loss (cyrenaica) -> none: missing - cyrenaica dossier has no 163-145 interval (author flagged it and also proposes cyrene-under-ptolemy-viii); owners must pick one counterpart.
- ptolemaic-kingdom -155 gain (kingdom-of-kush) -> none: missing - kingdom-of-kush (af-01) has no 160s-150s loss of Lower Nubia.
- ptolemaic-kingdom -145 gain (cyrenaica) -> none: missing - as for 163.
- ptolemaic-kingdom -105 loss (cyrenaica) -> cyrenaica -105 gain: matched
- ptolemaic-kingdom -34 gain (roman-republic) -> roman-republic -36 loss: mismatch - two years and different land: Rome gives Cilicia Aspera in 36; this dossier takes Cyrenaica and central Syria in 34, which Rome's ledger never loses.
- ptolemaic-kingdom -30 loss (roman-republic) -> roman-republic -30 gain: matched - after the reviewer's slug fix (was roman-empire).
- kingdom-of-kush -204 gain (ptolemaic-kingdom) -> none: missing - no Ptolemaic loss of Lower Nubia c. 204 (Great Theban Revolt page supports it).
- antigonid-dynasty -201 gain (ptolemaic-kingdom) -> none: missing - no Ptolemaic loss of Samos, Miletus and Carian footholds in 201.
- roman-republic -58 gain (ptolemaic-kingdom) -> none: missing - Cyprus annexed; no Ptolemaic loss.
- roman-republic -47 loss (ptolemaic-kingdom) -> none: missing - Cyprus restored; no Ptolemaic gain.
- roman-republic -31 gain (ptolemaic-kingdom) -> ptolemaic-kingdom -30 dissolve: mismatch - Cyprus after Actium; the Ptolemaic dossier ends everything in 30 (one year apart, but no loss event).
- roman-republic -30 gain (ptolemaic-kingdom) -> none: missing - Cilicia Aspera (c1); never gained in the Ptolemaic ledger.
- macedonian-empire -321 loss (ptolemaic-kingdom) -> none: missing - Egypt and Libya; the Ptolemaic dossier holds them from 323/322.
- cyrenaica -305 gain (ptolemaic-kingdom) -> none: missing - Cyrenaica's revolt; no Ptolemaic loss.
- cyrenaica -300 loss (ptolemaic-kingdom) -> none: missing - Magas's reconquest; no Ptolemaic gain.
- laomedon -318 loss (ptolemaic-kingdom) -> ptolemaic-kingdom -318 gain: matched
- macedonian-empire -323 vassal_start (laomedon) -> none: missing - no vassal_start in laomedon (vassal_end -319 likewise).
- macedonian-empire -323 vassal_start (perdiccas) -> none: missing - no vassal_start in perdiccas (vassal_end -321 likewise).

## Counterparts needing dossiers

- Antigonid kingdom of Antigonus Monophthalmus in Asia (antigonus-monophthalmus, -306 to -301): from the author; if it is to carry the 315-311 Syria events it must start in 315
- Thebaid of Horwennefer (Haronnophris) (horwennefer, -205 to -199): from the author; or fold into ankhwennefer
- Kingdom of Cyrene under Ptolemy VIII (cyrene-under-ptolemy-viii, -163 to -145): from the author; the ledger uses counterpart cyrenaica instead
- Cleopatra II's Alexandria (cleopatra-ii-alexandria, -132 to -127): from the author; contest events only, minor
- Ptolemy Keraunos's kingdom of Macedon and Thrace (ptolemy-keraunos, -281 to -279): string counterpart in kingdom-of-lysimachus /ledger/23; probably the land Cliopatria labels Ptolemaic in 281-280

## Problems

- No page failed to load. The Ptolemaic Kingdom, Laomedon and Perdiccas pages have no area in their infoboxes, so no area ratio could be computed.
- Cross-group mismatches to route: macedonian-empire (eu-02) models Ptolemy, Laomedon and Perdiccas as its vassals 323-321/319, the batch dossiers do not; kingdom-of-lysimachus (eu-02) gives the 281 land to Ptolemy Keraunos; roman-republic (eu-03) carries Cyprus 58/47/31 and Cilicia Aspera 36/30; kingdom-of-kush (af-01) carries Lower Nubia 274/204 but not 155; greek-city-states (eu-01) lacks the Corinth occupation 308-302; cyrenaica (me-05) lacks 163-145 and disagrees on 276/274 and 305-300.
- Reviewer applied two small fixes: ptolemaic-kingdom /ledger/58-59 counterpart roman-empire -> roman-republic; perdiccas /keyframe_review/0 verdict ok -> adjust (ends 320). Both files re-validated clean and read back.
