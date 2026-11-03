# Review of batch eu-01-b (reviewer, 2026-10-18)

Dossier: history/polities/greek-city-states.json (Greek City-States, -800..83, 52 Cliopatria shapes, 60 keyframes, 45 events). Verdict: **fail** (back to the author).

Mechanical: validator 0 errors; 45 --resolve warnings, all the gazetteer names listed below. All 52 Cliopatria shapes have a verdict; the 8 new keyframes carry from, to and a correction. Ledger sorted, found at -800, dissolve at 83, wars inside the life.

Spot checks (8 events on 6 pages, all confirmed): -547 Ionia (Ionia), -272 Tarentum (Pyrrhic War), -146 (Achaean War), -355 Chios/Rhodes/Cos/Byzantion (Social War 357-355), -688 Gela and -580 Akragas (Greek colonisation table), -88 Aristion and 1 March 86 (First Mithridatic War). No fabricated event found.

Why it fails: the dossier predates most of its neighbours and does not agree with them. Sicily is owned twice (syracuse.json), the Peloponnese is owned twice from 191 (achaean-league.json), confidence-3 gains from greek-city-states in macedonian-empire (-357, -356, -354), achaean-league (-251, -235), antigonid-dynasty (-294, -229) and peloponnesian-league (-383) have no mirror, and the League of Corinth / Diadochi years contradict macedonian-empire.json in type and, at -307, in direction.

Reviewer-applied fixes (re-validated, 0 errors): counterpart antigonid-macedonia -> antigonid-dynasty at /ledger/29, /ledger/32, /ledger/34 and /wars/6/belligerents; one sentence on the Polis infobox area added to notes.

## Findings

- **/ledger/29/counterpart, /ledger/32/counterpart, /ledger/34/counterpart, /wars/6/belligerents** (applied): Counterpart slug 'antigonid-macedonia' names a row that will never have a dossier: eu-02 wrote one dossier for both Antigonid rows under the earlier slug.
  - Evidence: history/polities/antigonid-dynasty.json identity.cliopatria_names = ['Antigonid Dynasty', 'Antigonid Macedonia'] (research rule: shared Wikidata Q237325, one dossier under the earlier slug).
  - Fix: counterpart 'antigonid-dynasty' (all four occurrences).
- **/notes** (applied): No infobox area comparison recorded.
  - Evidence: Polis infobox: 'max area of 60% of poleis: 100 km2', 'max area of 80% of poleis: 200 km2'; footnote 'Athens had 2,500 km2'; no aggregate area and no year.
  - Fix: Sentence added to notes saying the infobox gives only per-polis figures, so no ratio is possible.
- **/ledger/1, /ledger/31, /keyframe_review/2..41 (Sicilian cells)**: Sicily is owned twice: the aggregate keeps the Syracusan cells -700..-211 and loses 'Siracusa' to Rome in -212, while syracuse.json (found -733 from nobody) holds the same land and is the counterpart Rome names.
  - Evidence: syracuse.json: -733 found, -405 gain from greek-city-states (eastern Sicily), -386 gain from greek-city-states (Rhegium), -367 loss to greek-city-states (Adriatic colonies), -212 Oct loss/dissolve to roman-republic; roman-republic.json /ledger/55: -212 gain from syracuse. GCS keyframe 39 note: 'Syracuse's kingdom (9 Sicilian cells)' kept in the aggregate. The author flagged the overlap but did not resolve it.
  - Fix: Subtract syracuse.json's land from the keyframe corrections for the years it holds it (from -733; Hieron's kingdom -271..-212); add the mirrors: -405 loss (eastern Sicily) to syracuse, -386 loss (Rhegium) to syracuse, -367 gain (the Adriatic colonies) from syracuse; delete /ledger/31 or reduce it to the non-Syracusan cells.
- **/keyframe_review/45..49 and /ledger (missing events -251..-191)**: The Peloponnese is owned twice -191..-146: GCS keyframes subtract only Laconia, while achaean-league.json draws the whole Peloponnese from 191 and gains its members from greek-city-states; GCS has no loss to achaean-league at all.
  - Evidence: achaean-league.json /keyframe_review/10 correction union Peloponnese ('the whole Peloponnese from 191'); its ledger: -251 gain Sicyon from greek-city-states (c3), -243 Corinth, Megara, Troezen, Epidaurus (c2), -235 Megalopolis (c3), -234 Arcadia (c1), -191 Messene and Elis (c1). GCS -164 keyframe note: '71,000 km2 of it in Greece'; roman-republic.json /ledger/81 takes the Peloponnese in -146 from achaean-league while GCS /ledger/35 also loses it.
  - Fix: Add losses to achaean-league at -251, -243, -235, -234, -191; subtract the Achaean League's corrected shape from keyframes -251..-145; restrict /ledger/35 to the land the aggregate still held (Thessaly, central Greece outside the leagues, Euboea).
- **/ledger (missing events -357, -356, -354, -348)**: Philip II's conquests of Greek cities are absent: Macedon records three confidence-3 gains from greek-city-states with no mirror, and the Chalcidice is never lost.
  - Evidence: macedonian-empire.json /ledger/3 -357 gain from greek-city-states (Amphipolis, Pydna), /ledger/4 -356 (Crenides/Kavala), /ledger/5 -354 (Methone), all c3; /ledger/7 -348 gain Chalcidian League (Polygyros 50 km). GCS keyframe -350 is 'ok' at 144,364 km2 with no event between -355 and -338 other than /ledger/21.
  - Fix: Add losses to macedonian-empire at -357 (Amphipolis, Pydna), -356 (Crenides), -354 (Methone) and -348 (Olynthus and the Chalcidice, or counterpart chalcidian-league if eu-01-x writes it), citing the pages Macedon cites.
- **/ledger/22, /ledger/25, /ledger/26, /ledger/27, /ledger/28, /keyframe_review/22..28**: The League of Corinth and the Diadochi years disagree with macedonian-empire.json in type and, at -307, in direction.
  - Evidence: macedonian-empire.json: -337 vassal_start greek-city-states (Central Greece, Attica, Peloponnese), -323 vassal_end, -322 vassal_start, -307 vassal_end; GCS records -338 loss, -323 gain, -322 loss and -307 LOSS (Thessaly and the Peloponnese), plus a -319 gain Macedon does not mirror. GCS keyframe 22 itself says the members 'should be drawn as Macedonian tint rather than colour', and /ledger/28 cites a page that says Demetrius 'freed the city' (a release, not a loss).
  - Fix: Agree one model with eu-02: record vassal_start/vassal_end of macedonian-empire (-338/-337, -323, -322, -307 Attica) and keep the mainland in the keyframes as vassal land, or have eu-02 change its events to gain/loss; rewrite /ledger/28 so it does not contradict its own page, and pair /ledger/27 with a Macedon event.
- **/ledger/30**: The Italiot cities in 272 are a loss here but a vassal_start in roman-republic.json, and Rome's -90 vassal_end of greek-city-states has no mirror.
  - Evidence: Pyrrhic War page: 'the remaining cities quickly seeking terms'; 'the Romans taking allies from Tarentum in the form of Locri, Croton, and Rhegium'. roman-republic.json /ledger/24 -272 vassal_start greek-city-states (Taranto, Reggio, Napoli), /ledger/99 -90 vassal_end greek-city-states.
  - Fix: Change /ledger/30 to vassal_start (counterpart roman-republic, region Taranto, Reggio, Napoli) and add the -90 vassal_end plus the loss of those cities at the Social War enfranchisement, matching the Rome dossier.
- **/ledger/15**: Ionia is lost twice (-547 to Persia, -478 to the Delian League) with no regain between, and the -480 keyframe already excludes the Aegean and Ionian cities.
  - Evidence: /ledger/11 -547 loss Ionia (confirmed: 'conquest of all the Ionian cities in 547 BC'); no event for Mycale (479); /keyframe_review/13 text: 'the Aegean and Ionian cities are absent'. delian-league.json /ledger/1 records -478 vassal_start with counterpart 'Delian League allies', not greek-city-states.
  - Fix: Either add a -479 gain of Ionia from achaemenid-empire (Mycale) or drop Ionia from /ledger/15; agree with delian-league on vassal_start (counterpart greek-city-states) versus loss for 478 and 404.
- **/ledger/19, /ledger/23, /keyframe_review/19**: Attica leaves the aggregate in the keyframe at -377 but not in the ledger, then is gained back from the Second Athenian League at -338.
  - Evidence: /keyframe_review/19 subtracts the whole Second Athenian League -366 shape; /ledger/19 region is that shape minus Attica; /ledger/23 gains Attica from second-athenian-league in -338.
  - Fix: Include Attica in /ledger/19 (Athens leaves with its league), or keep Attica in keyframe 19 and drop /ledger/23.
- **/keyframe_review/1, /ledger (missing -724)**: Messenia leaves the aggregate in 724 by the keyframe's own note, but the correction keeps it to -701 and no event records it.
  - Evidence: /keyframe_review/1 note: 'Messenia stays in the aggregate until the First Messenian War ends in 724'; peloponnesian-league.json /ledger/1: -724 gain Messenia from greek-city-states (c2).
  - Fix: Add -724 loss of Messenia to peloponnesian-league and a new keyframe -724..-701 = GCS -750 minus Laconia and Messenia.
- **/ledger/20, /keyframe_review/20**: Messenia is gained in -369 but the -366 keyframe ('ok') draws it, with Arcadia and Thessaly, in the Sacred Band of Thebes row; the -377 to -366 area fall of about 15,000 km2 has no event and no event returns the land at -350.
  - Evidence: /keyframe_review/20 note: 'Messene (369) is inside the Theban shape, as Thebes' ally'; keyframe 19 = 178,577 minus Thebans and SAL shapes, keyframe 20 = 123,887 km2.
  - Fix: Either adjust keyframe 20 to keep Messenia and Arcadia in the aggregate with Theban tint (vassal_start of sacred-band-of-thebes) or add losses to sacred-band-of-thebes at -366 and gains at -350.
- **/ledger/24**: Boeotia is gained at -335 from sacred-band-of-thebes while keyframes 22-25 already add it from -337, and the row alive in -350..-338 is 'Thebans'.
  - Evidence: /keyframe_review/22 correction unions Thebans -350 from -337; sacred-band-of-thebes row is -366..-351, thebans -350..-338 (section 6 of the brief).
  - Fix: Date the event to match the keyframe (or start the Boeotia union at -335) and name counterpart 'thebans'.
- **/ledger/39, /keyframe_review/53**: Athens is lost to Rome in -86 at confidence 1, but the page says the opposite and Rome's dossier has no matching gain.
  - Evidence: First Mithridatic War page: 'The city was not included in the penalties imposed on the Asian cities'; Sulla let Athens keep Delos. roman-republic.json /ledger/81 excludes Athens from its 146 gain and has only a -86 contest_end with Pontus.
  - Fix: Either keep Attica in the aggregate after 1 March 86 (adjust keyframes -87..-42 to union Attica) and delete /ledger/39, or hand Athens to the proposed 'athens' dossier with a dated event.
- **/ledger (missing mirrors, confidence 2-3)**: Further neighbour events name greek-city-states with no mirror here.
  - Evidence: antigonid-dynasty.json -301 loss Attica to GCS (c2), -294 gain Attica from GCS (c3), -287 loss Attica to GCS (c1), -261 vassal_start GCS Attica (c2), -229 vassal_end (c3); peloponnesian-league.json -383 occupation_start of Thebes (c3), -379 occupation_end (c3), -338 loss to GCS (c1), -229 gain Tegea area from GCS (c2); aetolian-league.json -301 Delphi, -280 Lamia (c2), -245 (c1); athenian-coalition.json -323 two gains from GCS (c2); cimmerian-bosporus.json -360 Theodosia (c2); delian-league.json -412 loss of Chios and Mytilene to GCS (c2), -416 Melos (counterpart written as 'Melos (independent polis)'); kingdom-of-lysimachus.json -302 Heraclea Pontica (c2); etruscans.json -540 Corsica (Alalia, c2).
  - Fix: Add each mirror event (or agree with the other group that its event is wrong); wars Chremonidean War, Battle of Alalia and the Cleomenean War follow.
- **/wars**: Wars behind ledger events are missing and one zone list is empty without a note; one war is dated from memory.
  - Evidence: /ledger/21 rests on the Social War (357-355 BC) page but no such war; /ledger/12 (300 Champions, 546), /ledger/22 (Chaeronea, 338), the Mycale campaign (479), the Chremonidean War (antigonid-dynasty -261) and Alalia (etruscans -540) are absent; /wars/1 Peloponnesian War has zones [] although Chios/Mytilene changed sides (delian-league -412) and the league dissolved; /wars/0 note: '499-494 are the handbooks' years'.
  - Fix: Add the wars with zones; give the Peloponnesian War its Aegean/Ionian zone or a note; take the Ionian Revolt years from the Ionian Revolt page.

## Area check

Polis infobox gives only per-polis areas (60% of poleis at most 100 km2, 80% at most 200 km2; Athens 2,500 km2), no aggregate and no year; Cliopatria shapes run 602 to 206,488 km2. The dossier was silent; the reviewer added a sentence to notes (applied fix).

## Thin (confidence-1 events and unexplained shapes, for a gap-filler)

- /ledger/3: Cyprus leaving the aggregate (-700, c1): the date of the Cypriot kings' submission to Assyria (try https://en.wikipedia.org/wiki/Ancient_history_of_Cyprus)
- /ledger/6: Naukratis grant (-650, c1); counterpart is a name, not a slug (assyrian-egypt in 650 by Cliopatria) (try https://en.wikipedia.org/wiki/Naukratis)
- /ledger/7, /ledger/13: Cyrene's foundation year and its submission to Persia (Cambyses, c. 525) instead of -630 and -500 (try https://en.wikipedia.org/wiki/Cyrene,_Libya)
- /ledger/27, /ledger/28: which land Polyperchon's decree (319) and Cassander/Demetrius (307) moved (try https://en.wikipedia.org/wiki/Second_War_of_the_Diadochi)
- /ledger/29, /keyframe_review/30..35: Thessaly's leaving in -277 and the Diadochi-year shape changes -291..-277 (try https://en.wikipedia.org/wiki/Antigonus_II_Gonatas)
- /ledger/33, /keyframe_review/47: the +60,000 km2 of Anatolian coast in -188: Apamea gave Lycia and Caria to Rhodes and the interior to Pergamon; the Black Sea coast was never Seleucid (try https://en.wikipedia.org/wiki/Treaty_of_Apamea)
- /ledger/34, /keyframe_review/49: the +100,000 km2 after Pydna (-164 shape) outside the Macedonian republics (try https://en.wikipedia.org/wiki/Third_Macedonian_War)
- /ledger/41: the Anatolian coast removed in -63 (Pompey's settlement) (try https://en.wikipedia.org/wiki/Third_Mithridatic_War)
- /ledger/43, /ledger/44: Olbia (78) and Thasos (83) end dates (try https://en.wikipedia.org/wiki/Pontic_Olbia)
- /keyframe_review/12: -500 shape change (-21,000 km2) unexplained (try https://en.wikipedia.org/wiki/Greek_colonisation)

## Cross-dossier matrix (unmatched or disagreeing only)

- greek-city-states -734 gain / nobody -> syracuse -733 found: mismatch; both dossiers claim Syracusan land from 733/734
- greek-city-states -478 loss / delian-league -> delian-league -478 vassal_start: mismatch; DL: vassal_start with counterpart "Delian League allies"; GCS: loss; Ionia already lost in -547
- greek-city-states -404 gain / delian-league -> delian-league -404 vassal_end: mismatch; type differs; DL counterpart "Delian League allies"
- greek-city-states -338 loss / macedonian-empire -> macedonian-empire -337 vassal_start: mismatch; loss vs vassal_start
- greek-city-states -323 gain / macedonian-empire -> macedonian-empire -323 vassal_end: mismatch; gain vs vassal_end
- greek-city-states -322 loss / macedonian-empire -> macedonian-empire -322 vassal_start: mismatch; loss vs vassal_start
- greek-city-states -319 gain / macedonian-empire -> no mirror: missing; macedonian-empire has no -319 event with GCS
- greek-city-states -307 loss / macedonian-empire -> macedonian-empire -307 vassal_end: mismatch; opposite directions
- greek-city-states -277 loss / antigonid-dynasty -> antigonid-dynasty -277 gain: mismatch; AD gains Ancient Macedon from Sosthenes, not Thessaly from GCS
- greek-city-states -272 loss / roman-republic -> roman-republic -272 vassal_start: mismatch; loss vs vassal_start
- greek-city-states -212 loss / roman-republic -> roman-republic -212 gain: mismatch; RR gains Syracuse from syracuse, not GCS
- greek-city-states -196 gain / antigonid-dynasty -> antigonid-dynasty -196 loss: mismatch; AD gives Thessaly to "Thessalian League", Corinth/Chalcis/Demetrias to roman-republic, rest to nobody
- greek-city-states -167 gain / antigonid-dynasty -> antigonid-dynasty -168 dissolve: mismatch; AD land passes to roman-republic in -168
- greek-city-states -146 loss / roman-republic -> roman-republic -146 gain: mismatch; RR gains the Peloponnese etc. from achaean-league, not GCS
- greek-city-states -86 loss / roman-republic -> no mirror: missing; RR has no -86 gain of Attica; page says Athens was not penalised
- greek-city-states -63 loss / roman-republic -> no mirror: missing; RR -64/-63 gains name seleucid-empire, kingdom-of-armenia, pontus, not GCS
- peloponnesian-league -724 gain / greek-city-states -> no mirror: missing; no GCS loss of Messenia
- etruscans -540 gain / greek-city-states -> no mirror: missing; Corsica (Alalia)
- delian-league -416 gain / Melos (independent polis) -> no mirror: missing; counterpart should be greek-city-states; no GCS loss
- delian-league -412 loss / greek-city-states -> no mirror: missing; Chios, Mytilene; no GCS gain
- syracuse -405 gain / greek-city-states -> no mirror: missing; eastern Sicily
- syracuse -386 gain / greek-city-states -> no mirror: missing; Rhegium
- peloponnesian-league -383 occupation_start / greek-city-states -> no mirror: missing; Cadmea of Thebes (c3)
- syracuse -367 loss / greek-city-states -> no mirror: missing; Adriatic colonies
- cimmerian-bosporus -360 gain / greek-city-states -> no mirror: missing; Theodosia
- macedonian-empire -357 gain / greek-city-states -> no mirror: missing; Amphipolis, Pydna (c3)
- macedonian-empire -356 gain / greek-city-states -> no mirror: missing; Crenides (c3)
- macedonian-empire -354 gain / greek-city-states -> no mirror: missing; Methone (c3)
- peloponnesian-league -338 loss / greek-city-states -> no mirror: missing; border districts (c1)
- athenian-coalition -323 gain / greek-city-states -> no mirror: missing; two gains (central Greece; Peloponnesian cities)
- kingdom-of-lysimachus -302 gain / greek-city-states -> no mirror: missing; Heraclea Pontica
- aetolian-league -301 gain / greek-city-states -> no mirror: missing; Delphi
- antigonid-dynasty -301 loss / greek-city-states -> no mirror: missing; Attica
- antigonid-dynasty -294 gain / greek-city-states -> no mirror: missing; Attica (c3)
- antigonid-dynasty -287 loss / greek-city-states -> no mirror: missing; Attica
- aetolian-league -280 gain / greek-city-states -> no mirror: missing; Lamia
- antigonid-dynasty -261 vassal_start / greek-city-states -> no mirror: missing; Attica (Chremonidean War)
- achaean-league -251 gain / greek-city-states -> no mirror: missing; Sicyon (c3)
- aetolian-league -245 gain / greek-city-states -> no mirror: missing; central Greece (c1)
- achaean-league -243 gain / greek-city-states -> no mirror: missing; Corinth, Megara, Troezen, Epidaurus
- achaean-league -235 gain / greek-city-states -> no mirror: missing; Megalopolis (c3)
- achaean-league -234 gain / greek-city-states -> no mirror: missing; Arcadia (c1)
- antigonid-dynasty -229 vassal_end / greek-city-states -> no mirror: missing; Attica (c3)
- peloponnesian-league -229 gain / greek-city-states -> no mirror: missing; Tegea area
- achaean-league -191 gain / greek-city-states -> no mirror: missing; Messene and Elis
- roman-republic -90 vassal_end / greek-city-states -> no mirror: missing; Italiot cities

Matched: -800 greek-dark-ages, -546 and -369 peloponnesian-league, -480 cimmerian-bosporus, -67 and -49 roman-republic. Exceptions (counterpart not written yet): achaemenid-empire, neo-assyrian-empire, seleucid-empire, kingdom-of-pontus, roman-empire, sacred-band-of-thebes, second-athenian-league, Saite Egypt (name, not slug).

## Gazetteer names needed

Regions: Laconia, Messenia, Thyreatis, Magna Graecia, Chalcidice. Places: Gela, Agrigento.

## Still for the orchestrator

- greek-colonies (eu-02) row versus the -271..-226 bridge keyframe.
- Counterparts needing dossiers: the author's list, plus thessalian-league (named by antigonid-dynasty and macedonian-empire).
