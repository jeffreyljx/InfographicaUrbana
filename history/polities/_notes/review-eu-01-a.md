# Review: batch eu-01-a (Bronze Age and Greece, part a), 2026-10-18

Reviewer: adversarial reviewer, Phase B. Dossiers: minoan-civilization, mycenaean-greece, greek-dark-ages. Neighbour dossiers: hittites (me-04) not yet written, so every Hittite counterpart is the exception "a counterpart owned by a group that has not run yet". greek-city-states (another part of eu-01) was read for the -800 handover only.

Mechanical: validate_dossier.py --resolve, all three valid, 0 errors, 0 warnings (before and after the reviewer's edits). Geometry checked with tools/gazetteer.py resolve (cell diffs between consecutive keyframes and across the handovers).

Pages opened: Minoan civilization, Knossos, Mycenaean Greece (twice), Ahhiyawa, Late Bronze Age collapse, Greek Dark Ages.

## minoan-civilization: pass

- Spot checks, both confirmed: /ledger/0 (Knossos: "The first palace was built around 1900 BC"); /ledger/1 (Minoan page: "with a Mycenaean elite clearly ruling Knossos from around 1450 BC"; Knossos: "After about 1450 BC, Knossos became an important Mycenaean administrative centre").
- Keyframes: -1900 (new, = Cliopatria -1600, 16 cells), -1600, -1500 all 16 cells; no unexplained change. Capital Knossos 25.16 E 35.30 N inside the bbox. Type 'state' justified (schema: culture = before 3400 BCE). Family hellenistic is a colours.json family.
- Area: no infobox area (infobox gives only dates c. 3100 - c. 1100 BC and range). Cliopatria 5,499 km2 against Crete's real ~8,300 km2 (ratio 0.66), within a factor of two and noted.
- Handover to mycenaean-greece at -1450 matched both ways.

## mycenaean-greece: fail (one blocking finding, not applied)

Blocking, not applied:
1. Lesbos is removed from the -1240, -1220 and -1200 shapes (/keyframe_review/5..7/correction, minus Mitilini 40 km) and drawn as contested (/ledger/7, /ledger/9); /wars/0/outcome says "Wilusa and Lesbos stayed outside Mycenaean possession". The Mycenaean Greece page, the very sentence the note quotes, continues: Piyama-Radu "later invaded the island of Lesbos, which then passed into Ahhiyawan control" (reign of Hattusili III, c. 1267-1237 BC). The correction contradicts its source. Fix: keep Lesbos in the -1240..-1200 shapes (minus only the Troad), split /ledger/7 into a contest_start for the Troad (Wilusa, "may have extended to the region of Wilusa") and a gain of Lesbos (place Mitilini 40 km or a Lesbos polygon, c. -1240, confidence 2, counterpart the Seha River Land / hittites or nobody, quoting "which then passed into Ahhiyawan control"); /ledger/9 then ends only the Troad contest; correct the war outcome and the K5-K7 texts; /ledger/11 loses Lesbos at -1150.

Not blocking, not applied (author):
2. /ledger/11 (-1150 loss) region is the -1240 additions (38 cells), but 15 of those cells are still inside the -1150 shape (Thessaly-Epirus fringe, Ionian islands) and 3 dropped cells are outside it. Use {"union": [{"minus": [{"minus": [{"cliopatria": "Mycenaean Greece", "year": -1200}, {"cliopatria": "Mycenaean Greece", "year": -1150}]}, {"region": "Troad"}]}, {"place": "Miletus", "km": 20}]} (Lesbos included per finding 1).
3. /keyframe_review/8/note says "the 34 cells of the -1240 additions ... are dropped"; 34 cells drop, but 12 of them are the Troad and Lesbos, and about 12 of the -1240 additions stay. Reword.

Applied by the reviewer (re-validated, 0 errors):
4. /keyframe_review/2/correction: {"region": "Crete"} (27 cells) replaced by {"cliopatria": "Minoan civilization", "year": -1500} (16 cells). The full-island Crete made Crete grow from 16 to 27 cells at -1450 (Minoan -1500 shape before) and shrink back to 16 at -1400 (Cliopatria -1400 has exactly the Minoan 16 cells) with no event.
5. /keyframe_review/2/note and /keyframe_review/3/correction/text: the quote 'Mycenaean Greece's main base in Asia Minor' is not on the page; replaced by the page's 'the most important base for Mycenaean activity in Asia Minor'.
6. /ledger/5/note and /ledger/8/note: quotes replaced by the page's words ("an anti-Hittite rebellion headed by Arzawa, a Hittite vassal state, received support from Ahhiyawa"; "In c. 1220 BC, the king of Ahhiyawa is again reported to have been involved in an anti-Hittite uprising in western Anatolia"). Years were right.

Spot checks (all on the page with the year): /ledger/2 Crete c. 1450 (conf 3) confirmed; /ledger/3 Miletus c. 1450 confirmed; /ledger/5 c. 1315 confirmed; /ledger/7 Wilusa confirmed, Lesbos misread (finding 1); /ledger/8 c. 1220 confirmed; /ledger/10 Mycenae c. 1190, Tiryns largest post-palatial centre confirmed; war 1 destruction dates (Mycenae 1250/1190, Tiryns 1200, Pylos c. 1180, Thebes, "Up to 90%") confirmed on Late Bronze Age collapse.

Thin (within the 5-page budget, by design): /ledger/1 (-1500), /ledger/4 (-1400 Rhodes), /ledger/6 (-1240 Macedonia and the west), /ledger/11 (-1150) are confidence 1 at Cliopatria's dates; the Hittite takeover of Milawata (Milawata letter), Mursili II's campaign and the Sausgamuwa treaty are missing (the Ahhiyawa page as fetched has none of them, nor Piyama-Radu, whose text is on the Mycenaean page).

Area: no infobox area (range only). Shapes 45,664-71,057 km2; nothing to compare.

## greek-dark-ages: fix (fixed by the reviewer; thin items remain by design)

Applied by the reviewer (re-validated, 0 errors):
1. /ledger/3 (dissolve -800) region was {"cliopatria": "Greek Dark Ages", "year": -900} although its text says "and the Anatolian coast" and the -1000/-900 keyframes add Ionia; Ionia (71 cells) vanished at -800 with no event. Now {"union": [{"cliopatria": "Greek Dark Ages", "year": -900}, {"region": "Ionia"}]}.
2. /keyframe_review/0/note said the -1100 shape is "Cliopatria's Mycenaean -1150 shape plus six cells"; it also lacks 40 cells of that shape (about 10,000 km2: Aetolian, Evrytanian and Phthiotid interior and western Thessaly, 21.1-22.5 E, 38.6-39.6 N, four Cycladic cells and Kythera). The note now says so.
3. /ledger/1/note: the page dates the Anatolian movement "perhaps as early as 1000 BC", not "c. 1000 BC"; quote corrected (confidence 2 kept).

Thin: the 40-cell drop at the -1100 handover is unexplained (a gap-filler may keep the Mycenaean -1150 extent instead: correction union of GDA -1100 and Mycenaean -1150); /ledger/2 Cyprus (confidence 1) is against the page ("did not colonize the island"); kept, since greek-city-states also draws Cyprus at -800; the Halicarnassus cells of -1100 unverified.

Spot checks: /ledger/0 (c. 1180-800, infobox) confirmed; /ledger/1 confirmed ("perhaps as early as 1000 BC"); /ledger/2 page says the opposite of the shape, as the note admits; /ledger/3 (c. 800 BC, Olympics 776) confirmed.

Area: no infobox area.

## Cross-dossier

- Crete -1450: minoan dissolve <-> mycenaean gain, matched.
- -1100: mycenaean dissolve <-> GDA found, years matched; land mismatch of 40 cells (above).
- -800: GDA dissolve (now with Ionia) <-> greek-city-states found: years matched; greek-city-states' -800 and -750 shapes have no Anatolia (Cliopatria adds Turkey at -700), so Ionia drops for a century. Route to the greek-city-states author (eu-01, other part): add Ionia to the -800 and -750 corrections, or the GDA Ionia correction should be reconsidered together.
- Hittites (me-04, not run): must carry contest events for the Miletus coast -1315..-1220 and the Troad -1240..-1220, and (finding 1) a loss of Lesbos/Seha River Land c. -1240 if the author records it so.
