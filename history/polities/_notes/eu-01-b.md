# Notes: group eu-01-b (Bronze Age and Greece, part b)

Run of 2026-10-18 (second run of this batch). Owned state: greek-city-states only. The dossier
history/polities/greek-city-states.json already existed from an earlier run (06:58, 77 kB, 60 keyframes,
45 events, 11 wars, 34 sources) and passed `validate_dossier.py --json` with no errors, so per the
orchestrator's section-10 rule it was kept unchanged; this run opened no pages. Everything below is
read from that dossier's `notes`, its ledger counterparts and the `--resolve` warnings, plus checks
against data/polities.csv and the dossiers present on the mount today.

## greek-city-states (Cliopatria "Greek City-States", -800..83, 52 shapes)

- Split decision: the row was NOT split. The earlier run judged it an aggregate of hundreds of
  independent poleis and colonies (Iberia to the Crimea), not successive states, and kept one dossier
  of type `state` that carves out the poleis with rows of their own: Sparta (peloponnesian-league),
  the Bosporan Kingdom (cimmerian-bosporus), Athens' leagues (delian-league, second-athenian-league)
  and Thebes (sacred-band-of-thebes). No new slugs. `identity.capitals` is empty on purpose.
- Cliopatria corrections carried in keyframe_review (45 adjust, 6 wrong, 9 ok): Laconia and Messenia
  inside the aggregate -800..-551 and Laconia -337..-193; Kerch cities -480..-405; Boeotia -379..-367
  and the Second Athenian League members -377..-367; Ionia kept to -541 (Persian from 547) and to -384
  (Persian from 387); Attica and Boeotia missing -337..-324; a stray Kandahar cell -170..-145; the four
  Macedonian republics of 167-148 drawn as poleis -164..-145; Chersonesus kept to -88 (Pontic c. 110);
  Crete kept to -64 (Roman 67); Massalia kept to -43 (Roman 49).
- Row overlap to settle (orchestrator): Cliopatria's "Greek Colonies" row (greek-colonies, -271..-226,
  6 shapes, group eu-02) is the same aggregate under another Name. The kept dossier bridges -271..-226
  with a keyframe that uses that row's shape. Either eu-02 drops greek-colonies or this dossier drops
  the bridge keyframe; both drawn would double the colonies for 46 years.
- Dossier overlap to settle (reviewer): history/polities/syracuse.json now exists (Syracuse, -733 to
  -212/10, cliopatria_names []), written after the kept dossier. The kept ledger records the Sicilian
  foundations (Naxos, Syracuse 733, Gela 688, Akragas 580) as gains of greek-city-states from nobody and
  carries the Siege of Syracuse war; Sicilian cells need one owner per year.
- Counterpart strings that are names, not slugs: `Egypt (Saite kingdom), by grant` (Naukratis, -650).
  Cliopatria's matching rows are assyrian-egypt (-650..-616) and twenty-sixth-dynasty-of-egypt
  (-615..-501), both group me-02; the dossier was left unchanged (section 10), so the reviewer may
  retarget the counterpart.
- Unexplained shape changes (events at confidence 1, pages give the politics but not the land):
  -500 (-21,000 km2), -318 (+28,000), -307 (-73,000), -291/-284/-283/-281/-279/-277 (Diadochi years),
  -188 (+60,000 in Anatolia after Apamea), -164 (+100,000 after Pydna), -87 (Athens removed),
  -63 (Anatolian coast removed). Also confidence 1: Cyprus leaving the aggregate -700 (no page dates
  the Cypriot kings' submission to Assyria), Naukratis -650, Cyrene -630 (page gives no year).
- Disagreements between pages (recorded in the ledger notes): Megara to Sparta 448 vs revolt 447 vs
  Thirty Years' Peace 446/445; Selinus 650 or 627; Sybaris 721/720 or 709-707; Cadmea seized 383 or 382;
  Sparta into the Achaean League 192 (text) or 188 (infobox).
- Pages that would not load: none recorded by the earlier run; none opened in this run.

## States needing a dossier from another group or a gap-filler (counterparts of greek-city-states)

Massalia (c. -600..-49); Cyrene before the Cyrenaica row (-631..-331, Battiad kingdom, Persian vassal
from c. 525; cyrenaica is me-05); the Cypriot kingdoms (to the Ptolemaic annexation); Messene
(-369..-146); the Arcadian League (-370..-362); the Chalcidian League / Olynthus (to -348); Rhodes before
the rhodes row (-408..-189; rhodes -188..-165 is eu-02); the Lycian League (-168..43); the four Macedonian
republics (-167..-148); Athens as a free city after -86. Syracuse is no longer on this list
(syracuse.json exists). delian-league.json and athenian-coalition.json exist.

## Gazetteer names used but absent (45 --resolve warnings, all of them these names)

Regions: Laconia (31 keyframe corrections + ledger), Messenia, Thyreatis, Magna Graecia, Chalcidice.
Places: Gela, Agrigento. Coordinates were used for Naukratis, Heraclea Pontica and Cos because no place
entry exists; Kandahar resolves.

## Second pass after review (2026-10-18, verdict fail; findings 3-15 applied here, 1-2 applied by the reviewer)

Dossier rewritten from the kept first-run file: ledger 45 -> 81 events, keyframes 60 -> 85 (the Cliopatria
shapes are cut into corrected pieces where a neighbour holds part of the land), wars 11 -> 18, sources
34 -> 55. `validate_dossier.py --resolve`: 0 errors, 65 warnings, all of them names the gazetteer lacks
(Laconia 56, Messenia 2, Magna Graecia 2, Thyreatis 2, Chalcidice, Gela, Agrigento). The statements
above about "kept unchanged, no pages opened" and about syracuse.json are superseded by this section.
Pages opened for the repairs are listed in `sources[]`; five were opened a second time to check the
quotes (Battle of the 300 Champions, Pyrrhic War, Peace of Antalcidas, League of Corinth, Lysimachus).

What changed, per finding:
- 3 Sicily: Syracuse and its chora are subtracted from -700 (the Cliopatria shape first holds the cell
  then), eastern Sicily from -405, Hieron's south-east -289..-213; losses to syracuse at -405 and -386
  (Rhegium), gain from syracuse at -367 (Adriatic colonies), as syracuse.json writes them; the -212
  Siracusa loss (/ledger/31) is deleted, Rome's gain is syracuse's. The Siege of Syracuse war now names syracuse.
- 4 Peloponnese: losses to achaean-league -251, -243, -235, -234, -191; the Peloponnese is subtracted
  -191..-145; the -146 loss (/ledger/35) is cut to the 126 cells the aggregate still holds (Thessaly, central
  Greece, Euboea, Epirus).
- 5 Philip II: losses to macedonian-empire -357 (Amphipolis, Pydna), -356 (Crenides), -354 (Methone), -348
  (Olynthus and the Chalcidice); the cities are kept in the shape until their year. No chalcidian-league dossier exists, so the counterpart is macedonian-empire.
- 6 League of Corinth: vassal_start -337 / vassal_end -323 (June) / vassal_start -322 (September) /
  vassal_end -307 of macedonian-empire, as that dossier writes them; /ledger/28 is the -307 release
  ('freed the city from the power of Cassander and Ptolemy'), no longer a loss. The -319 Polyperchon gain is
  dated -318 (where Cliopatria's shape grows), confidence 1, with a -316 loss to polyperchon.
- 7 Italiots: vassal_start roman-republic -272 (Taranto, Reggio, Napoli), vassal_end and loss at -90 (October).
- 8 Ionia: -479 gain from achaemenid-empire (Mycale; the page: Greeks 'could only free the Aegean islands'),
  -478 loss to delian-league, -525 Cyrene and -387 Ionia/Cyprus losses to achaemenid-empire.
- 9, 11, 12 Attica, the Theban cells, Boeotia: Attica leaves with the Second Athenian League at -377; -366
  loss and -350 gain with sacred-band-of-thebes; Boeotia returns at -337 from thebans (matches the keyframes).
- 10 Messenia: -724 loss to peloponnesian-league, keyframe -724..-701 without Laconia and Messenia.
- 13 Athens: the -86 loss is deleted (First Mithridatic War page: Athens 'was not included in the penalties
  imposed on the Asian cities'); Attica stays in the shape from -87. A free-city dossier 'athens' is needed.
- 14 Mirrors added for every neighbour event naming greek-city-states (antigonid-dynasty, peloponnesian-league,
  aetolian-league, athenian-coalition, cimmerian-bosporus, delian-league, kingdom-of-lysimachus, etruscans,
  neo-assyrian-empire, assyrian-egypt, mamertines, polyperchon). A scripted check finds no neighbour event
  without a mirror here except greek-dark-ages' -800 dissolve (the predecessor link).
- 15 Wars added: Alalia (540-535), 300 Champions (546), Mycale (479), Social War (357-355), Chaeronea (338),
  Chremonidean War (267-261), Cleomenean War (229-222). Ionian Revolt now 499-493 (page: 'from 499 BC to 493 BC').
  The Peloponnesian War has an Aegean/Ionian zone. Deleted events: /29 (-277 Thessaly: the Gonatas page has
  Thessaly only in 274), /31, /33 (-188 Seleucid gain: Apamea page frees no Greek city), /39.

Disagreements kept (a page or a neighbour contradicts the reviewer's fix or the neighbour's own page):
- delian-league writes vassal_start/vassal_end for 478 and 404 with the counterpart 'Delian League allies';
  this row keeps loss/gain against delian-league because the members' land leaves the aggregate. The choice is a modelling one. The ledger of delian-league also
  writes -416 Melos with the counterpart 'Melos (independent polis)', not a slug.
- macedonian-empire has no event for Polyperchon's 318 gain; the Polyperchon page ('retained control over
  several strongholds, including Corinth and Sicyon') gives no year for the decree of freedom.
- antigonid-dynasty writes -196 as Thessalian League / roman-republic / nobody and its end in -168 as a
  dissolve to roman-republic; this row keeps -196 and -167 as gains from antigonid-dynasty (Third Macedonian
  War page: four client republics, 'the Macedonians and Illyrians should be free').
- athenian-coalition records its members lost to macedonian-empire in -322; this row returns them to the
  aggregate first (-323 losses, -322 gain) and then makes them vassals (Lamian War page: Crannon 322).
- roman-republic /ledger/81 takes Boeotia and Euboea from achaean-league in -146; achaean-league's own -146
  loss is the Peloponnese only, and this row holds Boeotia and Euboea until -146. Attica stays: 'Autonomy was
  granted to some cities, including Athens and Sparta'.
- Pages that do not say what the neighbours cite them for: Cyrene, Libya (no Cambyses; Cyrenaica has 525),
  Peloponnesian War (no Lesbos or Chios), Roman expansion in Italy (no 272; Pyrrhic War has it),
  Social War 91-87 (no Greek city), Second Athenian League (the league ends 355, not 338), Cleomenean War
  (the Arcadian cities had already allied themselves with the Aetolian League), League of Corinth
  (the 'latter half of 337' sentence is on the Chaeronea page).

Still unexplained Cliopatria shape changes (events at confidence 1, pages silent): -366 (Thrace, Macedonia
and Cyprus cells), -318 (+28,000 km2), -307 (-73,000), -210 (Peloponnese, Iberia), -110 (Massalia's territory
in France), -63 (Anatolian coast; Pompey's page does not discuss free-city status), and Attica is drawn twice
with Rome's Cliopatria shapes from about -60. The Cliopatria 'Greek Colonies' bridge keyframe -271..-226 is unchanged.

Counterparts without a dossier on the mount today: sacred-band-of-thebes, thebans, second-athenian-league
(other eu-01 batches), achaemenid-empire and kingdom-of-pontus (me-05), roman-empire (eu-04). Needing an owner:
athens, massalia, cyrene, messene, rhodes (before -188), the Chalcidian League, the Cypriot kingdoms, the
Arcadian League, the Lycian League, the four Macedonian republics (-167..-148).
