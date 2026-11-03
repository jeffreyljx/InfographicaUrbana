# Review af-02-a (2026-10-19): phoenician-colonies, carthage, mauretania, mercenary-rebels

Adversarial review of Phase B batch af-02-a. Machine copy: history/notes/phase-b/reviews/af-02-a.json. Pointers to mauretania events after /ledger/11 are post-edit (one lower than the author's report).

## phoenician-colonies: thin

Thin by design (4 Cliopatria shapes, 5 of 5 pages): 4 of 5 events are confidence 1 but each is honest and the quoted sentences are on the pages. Validator: 0 errors, 1 warning (kition has no dossier; listed by the author). Every keyframe change has an event; Kition (Cyprus) is carried from -900 consistently.

Gaps (for a gap-filler):
- `/ledger/1`: Founding dates of the western colonies (Motya, Panormus, Solus, Malta, Tharros, Gadir); the -700 gain is confidence 1 on a general sentence (try https://en.wikipedia.org/wiki/Motya)
- `/ledger/2`: Dates for the Sardinian towns (Tharros, Bithia, Sulci, Nora, Caralis); History of Sardinia says only 'From the 8th century BC' (try https://en.wikipedia.org/wiki/Tharros)
- `/ledger/3`: A dated end of Tyrian/colonial status for Kition (confidence 1); Kition needs its own dossier (me-04) (try https://en.wikipedia.org/wiki/Ancient_history_of_Cyprus)
- `/ledger/4`: The -616 hand-over to Carthage rests on 'in the seventh century BC' (Phoenicia page); History of Sardinia puts Carthaginian control c. 510, the Cadiz page after Tyre's fall in 573. A gap-filler may extend the row into the 6th century or split it by colony (author flagged) (try https://en.wikipedia.org/wiki/Magonid_dynasty)

Spot checks: `/ledger/0` Phoenicia: confirmed; `/ledger/4` Phoenicia: confirmed; `/ledger/3` Kition: confirmed; `/ledger/2` History_of_Sardinia: confirmed

Area: Colonies in antiquity has no infobox; the dossier notes say no page gives an area

## carthage: fail

No fabricated or mis-dated event found in 13 spot checks (all confidence 3 checks confirmed). Fails on three missing events that the author's own cited pages (or a Context neighbour's dossier) support: the 311 gain of most of Sicily, the 213 regain of Agrigentum, and the 265-264 occupation of Messana. Many cross-dossier mismatches with roman-republic and greek-city-states are routed in cross_checks rather than charged to this dossier.

Findings:
- `/keyframe_review/11 and /ledger/12-14` (BLOCKING, for the author): Keyframe carthage_-307 keeps Cliopatria's near-whole-island Sicily (74 of 89 cells, +20,000 km2 on the -331 shape) as Carthaginian land, and /ledger/14 loses it in -306, but no event ever gains it: only a contest_start (-311) over the same zone. Evidence: Sicilian Wars page (cited): Hamilcar 'defeated Agathocles in the Battle of the Himera River in 311 BC', 'won control over the rest of Sicily' and the same year 'laid siege to Syracuse itself'; the 306 treaty left Agathocles 'the eastern half of the island' (both confirmed). Fix: Add a -311 gain, counterpart syracuse (and/or greek-city-states for the non-Syracusan cities), region {minus: [Carthage -307, Carthage -301]}, confidence 2, source Sicilian_Wars, quoting 'won control over the rest of Sicily'; ask syracuse (eu-03) for the mirror -311 loss. Or, if the land is meant as contested only, change keyframe 11 to the -331 shape and turn /ledger/14 into a note.
- `/ledger/35 and /keyframe_review/28-29` (BLOCKING, for the author): /ledger/35 loses Agrigentum to Rome in -210, but the ledger never regains it after losing it in -261 (/ledger/18), and the -212 and -210 corrections subtract all of country Italy, which also removes the Carthaginian-held Sicilian towns of 213-210. Evidence: Second Punic War page (cited): 'A large Carthaginian army led by Himilco was sent to relieve the city in 213 BC', 'several further Sicilian cities deserted the Romans', 'Carthage sent more reinforcements to Sicily in 211 BC', Agrigentum 'the main Carthaginian stronghold on the island' betrayed in 210 and 'The remaining Carthaginian-controlled towns then surrendered'. The /ledger/35 note itself says 'The page does not say when Carthage retook it'. Fix: Add a -213 gain from roman-republic, region {lon 13.59, lat 37.31, km 40} (Agrigentum; more towns if a page names them), confidence 2, source Second_Punic_War; change keyframe_review/28 and /29 corrections to subtract the Italian peninsula, not all of country Italy (e.g. minus [{country Italy} minus {region Sicily}] plus the Agrigentum circle kept), so the -212..-209 shapes keep Agrigentum until 210.
- `/ledger (between /15 and /17)` (BLOCKING, for the author): No occupation of Messana in 265-264, although the mamertines dossier records it with carthage as counterpart. Evidence: mamertines /ledger/2-3 (confidence 3, Mamertines page): 'When Hiero returned to besiege Messina in 265 BC, the Mamertines called on a Carthaginian fleet, which occupied the harbour of Messina'; the garrison left as the Romans crossed in 264. The mamertines dossier existed (2026-10-18) before carthage was written; mamertines is in the author's Context table. Fix: Add occupation_start -265 and occupation_end -264, counterpart mamertines, region {lon 15.56, lat 38.19, km 18, text: the harbour and citadel of Messana}, confidence 3, source https://en.wikipedia.org/wiki/Mamertines (add to sources).
- `/ledger/26` (applied by reviewer): The -239 loss to mercenary-rebels lacked Leptis Parva, which the rebels' keyframe and this dossier's -238 gain (/ledger/27) include. Evidence: Mercenary War page: Leptis Parva 'had risen against Carthage earlier in the war'. Fix: Added Leptis Parva {lon 10.87, lat 35.67, km 30} to the union and text, confidence 3 to 2, note extended (mirror of mercenary-rebels /ledger/2). Re-validated: 0 errors.

Gaps (for a gap-filler):
- `/ledger/2-4`: The -500, -480 and -450 gains (Libya, Algeria, Morocco, Sardinia; +190,000 km2) are confidence 1 on the Magonid page's reign-level sentences (try https://en.wikipedia.org/wiki/Hanno_the_Navigator)
- `/keyframe_review/17`: Corsica (+33 cells) appears in -264 with no gain event; the Ancient Carthage lead has Carthage holding Corsica by 300 BC and the etruscans dossier gives it to carthage in -384 (both unsourced for the year) (try https://en.wikipedia.org/wiki/Sardinia_and_Corsica)
- `/keyframe_review/26`: The -218 shape adds 399 Spanish cells north of 38.7 N (about 100,000 km2, the Meseta to the Ebro) explained only by the 30-km Saguntum gain; Hasdrubal's and Hannibal's campaigns of 228-220 (Olcades, Vaccaei, Carpetani) need a dated gain (try https://en.wikipedia.org/wiki/Hasdrubal_the_Fair)
- `/ledger/46`: The -197 loss of the Libyan coast and Algerian strips (about 94,000 km2, the largest single loss before 146) is confidence 1 at Cliopatria's year; the Second Punic War page says the treaty 'accepted in spring 201 BC' 'stripped Carthage of all of its overseas territories and some of its African ones', so -201 at confidence 2 may be better supported; Masinissa's later seizures (Emporia, the Great Plains) remain undated (try https://en.wikipedia.org/wiki/Masinissa)
- `/ledger/16`: Recovery of western Sicily after Pyrrhus (-275, confidence 1) (try https://en.wikipedia.org/wiki/Pyrrhic_War)
- `/ledger/1`: The -616 take-over of the Phoenician colonies (confidence 1; specific pages say c. 510 for Sardinia and after 573 for Gadir) (try https://en.wikipedia.org/wiki/Magonid_dynasty)
- `/ledger/42`: Hannibal's departure from Italy (-203, confidence 1; the page ties the recall to the 204 invasion) (try https://en.wikipedia.org/wiki/Hannibal)
- `/wars/9`: Sardinia 'lost with the mutiny of its garrisons' (c. 240) has no ledger event; the -237 loss to Rome follows a rebel interlude (try https://en.wikipedia.org/wiki/Mercenary_War)

Spot checks: `/ledger/5` Sicilian_Wars: confirmed (returned with the spoils in 409 BC); `/ledger/14` Sicilian_Wars: confirmed (306 treaty, Agathocles 'retained control of the eastern half of the island'); `/ledger/23` First_Punic_War: confirmed (Treaty of Lutatius 241, 'Carthage evacuated Sicily'); `/ledger/28` First_Punic_War: confirmed (237 BC passage; History of Sardinia says 238, flagged by the author); `/ledger/39` Second_Punic_War: confirmed (Ilipa 206, Gades defected in the same passage); `/ledger/48` Third_Punic_War: confirmed (Utica 'went over to Rome in 149 BC'); `/ledger/45` Ancient_Carthage: confirmed ('In effect, Carthage became a Roman client state'); `/ledger/35` Second_Punic_War: confirmed (Agrigentum betrayed in 210); `/ledger/31` Second_Punic_War: confirmed (Saguntum 219, eight months); `/ledger/37` Second_Punic_War: confirmed (Carthago Nova 209); `/ledger/18` First_Punic_War: confirmed (Akragas 261); `/ledger/21` First_Punic_War: confirmed (Panormus 254); `/ledger/22` First_Punic_War: confirmed (Thermae and Lipara 252; Selinous and Heraclea Minoa in the same passage)

Area: Ancient Carthage infobox gives no area (only population, 222 BC: 3.7-4.3 million); capital Carthage, c. 814 BC to 146 BC as in the dossier

## mauretania: fix

Solid, honest dossier; every keyframe change explained (new -105 keyframe for the Numidian west is well argued). One reviewer-applied fix. Open cross-dossier item, not changed: the vassal relation names roman-republic until -25 although that dossier ends in -27; the switch to roman-empire should follow eu-04's start year.

Findings:
- `/ledger/12 (pre-edit numbering)` (applied by reviewer): A -25 gain from roman-empire of 'the territory of Western Numidia' whose region (the -27 shape minus the -110 shape) repeats the land the dossier already gained from kingdom-of-numidia in -105 (/ledger/4, same subtrahend), with no loss in between. Evidence: Juba II page: Juba received Mauretania 'enlarged by territory of Western Numidia' (confirmed), but the dossier holds the Numidian west from 105 BC (Bocchus I page: 'By treaty, Bocchus and the Romans divided the kingdom of Numidia'; Mauretania page: Bocchus II extended the border 'to the Ampsaga River'), and the 33-25 Roman administration is drawn as vassalage, so nothing was lost; the event's own note says 'Cliopatria already holds the western land from -91'. It would also have required eu-04 to record a false Roman loss of Western Numidia. Fix: Removed the -25 gain; its quote moved into the -25 vassal_start note (now /ledger/11); the notes field's ROMAN EMPIRE COUNTERPARTS line updated. Re-validated: 0 errors, 0 warnings (17 events).

Gaps (for a gap-filler):
- `/ledger/2`: The -197 Moroccan coast from carthage (66 cells) is undated on every page opened (confidence 1); mirrored by carthage /ledger/47 (try https://en.wikipedia.org/wiki/Lixus_(ancient_city))
- `/ledger/3`: End of the vassalage to Masinissa: a bridge to his death in 148 (confidence 1) (try https://en.wikipedia.org/wiki/Masinissa)
- `/ledger/6`: Year of Caesar's grant of Masinissa II's land to Bocchus (page gives 49-45; the roman-republic dossier uses 46) (try https://en.wikipedia.org/wiki/Publius_Sittius)
- `/ledger/7`: Year of Arabio's recovery ('after Caesar's murder'); counterpart Arabio is a person with no polity dossier (try https://en.wikipedia.org/wiki/Arabio)
- `/identity/capitals/0`: Volubilis as capital -225..-50 is an assumption (no page names a capital before 49 BC) (try https://en.wikipedia.org/wiki/Volubilis)

Spot checks: `/ledger/4` Bocchus_I: confirmed (105 BCE betrayal; the division treaty is undated, confidence 2 is right); `/ledger/5` Bocchus_II: confirmed ('By 49 BC ... partitioned'; Bocchus II 'had Iol as capital'); `/ledger/9` Mauretania: confirmed (33 BC bequest; 'temporary Roman administration for eight years'); `/ledger/16 (pre-edit 17)` Mauretania: confirmed ('Sabalus surrendered in 44 AD'; annexed and divided 'Around 44 AD'; infobox Disestablished 44 AD); `/ledger/0` Mauretania: confirmed (Bagas fl. 225 BC); `/ledger/11` Juba_II: confirmed (25 BC, client kingdom, Caesaria); `/ledger/6` Bocchus_II: confirmed as a 49-45 span (confidence 1 is right)

Area: Mauretania infobox has no area (capitals Volubilis, Iol/Caesarea; 3rd century BC to 44 AD); the dossier notes say so

## mercenary-rebels: fix

Rebel state, type rebel, 2 new keyframes, every event matched in carthage. One reviewer-applied consistency fix (Leptis Parva).

Findings:
- `/ledger/2` (applied by reviewer): The -239 keyframe (keyframe_review/1) and the -238 loss include Leptis Parva, but no gain ever brought it to the rebels. Evidence: Mercenary War page: 'the wealthy city of Leptis Parva, which had risen against Carthage earlier in the war' (no year); the correction of mercenary-rebels_-239 is Tunis+Utica+Hippo+Leptis Parva while /ledger/2 gained only Utica and Hippo. Fix: Added {lon 10.87, lat 35.67, km 30} (Leptis Parva) to the /ledger/2 union and its text, lowered confidence 3 to 2 (Leptis's rising is undated), note extended; mirrored in carthage /ledger/26. Re-validated: 0 errors, 0 warnings.

Gaps (for a gap-filler):
- `/keyframe_review/1`: Extent of the Libyan revolt beyond the four named towns ('many cities and towns rose', '70,000 Africans ... flocked to join them'); also the Sardinian garrison mutiny of c. 240 that the carthage war entry mentions (try https://en.wikipedia.org/wiki/Battle_of_the_Bagradas_River_(240_BC))

Spot checks: `/ledger/2` Mercenary_War: confirmed (between March and September 239 BC); `/ledger/1` Mercenary_War: confirmed (march on Tunis, 241; the page leaves the march undated, confidence 2 is right); `/ledger/3` Mercenary_War: confirmed (Leptis Parva mid-to-late 238; surrender late 238 or very early 237); `/identity/capitals/0` Mercenary_War: confirmed ('all 20,000 troops marched to Tunis')

Area: no Cliopatria row and a war page without an area; shape is a stated minimum

## Cross-dossier matrix: rows that are not matched

- missing: carthage -409 gain / greek-city-states: greek-city-states (eu-01) has no Sicilian loss in 409 (Selinus, Himera); Carthage side confirmed on Sicilian Wars page. Route to eu-01.
- missing: carthage -406 contest_start / greek-city-states: greek-city-states has no Sicilian contest 406-405; route to eu-01.
- missing: carthage -405 contest_end / greek-city-states: as above; route to eu-01.
- missing: carthage -405 vassal_start / greek-city-states: 405 peace: Selinus, Thermae, Akragas, Gela and Camarina tributary to Carthage (Sicilian Wars page, confirmed); greek-city-states lacks the vassal_start. Route to eu-01.
- missing: carthage -398 contest_start / syracuse: syracuse records only gains; no contest 398-393. Route to eu-03 (syracuse owner).
- missing: carthage -396 vassal_end / greek-city-states: greek-city-states lacks the vassal_end; route to eu-01.
- missing: carthage -393 contest_end / syracuse: as above.
- missing: carthage -252 loss / roman-republic: roman-republic has no 252 gain (Selinous, Heraclea Minoa, Thermae, Lipara; First Punic War page, confirmed). Route to eu-03.
- missing: carthage -215 contest_end / roman-republic: roman-republic has no contest_end for Catalonia; it records a 218 gain from carthage there instead (see reverse row).
- missing: carthage -209 contest_start / roman-republic: roman-republic records the 209 gain of New Carthage but no contest pair; contest pairs need not mirror exactly.
- missing: carthage -206 contest_end / roman-republic: as above.
- missing: carthage -204 contest_start / roman-republic: roman-republic has no contest_start for the 204 invasion of Africa; its 218-201 Second Punic War contest covers it.
- missing: carthage -203 contest_end / roman-republic: roman-republic has no 203 contest_end for Italy; it records a 203 gain from carthage (see reverse row).
- missing: carthage -201 vassal_start / roman-republic: roman-republic has no vassal_start for Carthage in 201 (it has one for kingdom-of-numidia). Ancient Carthage page: 'In effect, Carthage became a Roman client state' (confirmed). Route to eu-03.
- missing: carthage -149 loss / roman-republic: roman-republic has no 149 gain of Utica (Third Punic War page: 'went over to Rome in 149 BC', confirmed); route to eu-03.
- missing: carthage -149 contest_start / roman-republic: roman-republic has no Third Punic War contest pair; only the 146 gain.
- missing: carthage -146 contest_end / roman-republic: as above.
- missing: carthage -146 vassal_end / roman-republic: roman-republic lacks the vassal_end (and the 201 start); route to eu-03.
- missing: mauretania -33 vassal_start / roman-republic: roman-republic has no vassal_start for mauretania (Mauretania page: bequeathed to Octavian 33 BC, 'temporary Roman administration for eight years', confirmed). Route to eu-03.
- mismatch: mauretania -25 vassal_end / roman-republic: mismatch of years: the roman-republic dossier ends in -27 (January) but this vassal_end naming roman-republic is -25, and the roman-empire vassal_start is -25; the overlord switch should fall at whichever year eu-04 starts roman-empire (Cliopatria -31, RR dossier -27). Not changed by the reviewer: depends on eu-04.
- mismatch: roman-republic -218 gain / carthage: RR /ledger/50 takes Catalonia (Emporion, Cissa, Tarraco) from carthage in 218; carthage has a contest -218..-215 over Gerona/Barcelona/Tarragona and no loss. Decide one model: either Carthage loses the land north of the Ebro in 218 or RR records a contest. Route to eu-03 and the carthage author.
- mismatch: roman-republic -216 loss / carthage: RR /ledger/53 gives Capua and the south to carthage in 216 and takes it back 211 (/56), 209 (/59, Tarentum) and 203 (/61); carthage keyframes -216..-208 remove all of Italy ('Hannibal held no territory of his own in Italy') and draw it as contest. The two dossiers disagree on whether Hannibal held land; the orchestrator should pick one model.
- missing: mamertines -265 occupation_start / carthage: mamertines /ledger/2-3: a Carthaginian fleet occupied the harbour of Messana in 265 and left in 264 (Mamertines page, confidence 3); carthage has no occupation_start/occupation_end with counterpart mamertines. Fix in carthage (blocking finding).
- mismatch: etruscans -384 loss / carthage: etruscans /ledger/17 gives Corsica to carthage in -384 (confidence 1, a Cliopatria-boundary guess); carthage keeps Cliopatria's -264 Corsica (keyframe 17, unverified) and records no gain at all. 120 years apart, both unsourced for the year; the Ancient Carthage lead has Carthage holding Corsica by 300 BC.
- missing: syracuse -289 loss / carthage: syracuse /ledger/10 (confidence 1) gives the interior and north coast to carthage at Agathocles' death; carthage has no gain at -289 and its -301 shape is unchanged to -278. Route to eu-03 (syracuse) and the carthage author; both sides are page-silent.
- mismatch: roman-republic -210 gain / carthage: matched in year, but neither dossier records Carthage regaining Agrigentum and other Sicilian towns in 213 (Second Punic War page: Himilco's army 'sent to relieve the city in 213 BC', 'several further Sicilian cities deserted the Romans', Agrigentum 'the main Carthaginian stronghold' in 210). carthage needs the -213 gain; roman-republic the -213 loss.

Exceptions (counterpart nobody, or no dossier yet): Arabio, Saguntum, kingdom-of-numidia, kition, nobody, roman-empire

## Problems

- Validator (--resolve): 0 errors in all four; one warning (phoenician-colonies: kition has no dossier). Re-validated after the reviewer edits: 0 errors, 0 warnings in carthage, mauretania and mercenary-rebels.
- Reviewer edits applied in place (re-read before writing, read back after): mercenary-rebels /ledger/2 and carthage /ledger/26 (Leptis Parva, confidence 3 to 2); mauretania: removed the -25 gain (pre-edit /ledger/12), so mauretania ledger pointers after /ledger/11 are one lower than in the author's report.
- Neighbour dossiers missing (exception, group not run yet): kingdom-of-numidia (af-02 other part), roman-empire (eu-04), achaemenid-empire, ptolemaic-kingdom, cyrenaica (me-05), phoenicia (me-04). Read: greek-city-states, roman-republic, etruscans, thirtieth-dynasty-of-egypt, neo-assyrian-empire, greek-colonies, mamertines, achaean-league, plus syracuse and kingdom-of-epirus (direct counterparts).
- Cross-dossier routing: greek-city-states (eu-01) lacks every Carthaginian event of 409-396 in Sicily; roman-republic (eu-03) lacks the 252 gain, the 201-146 Carthaginian clientage, the 149 Utica gain and the 33 BC Mauretanian vassalage, and models Hannibal's Italy and Catalonia as land changing hands where carthage models contest; etruscans and syracuse carry confidence-1 transfers to carthage (-384 Corsica, -289 interior Sicily) that carthage does not mirror.
- No page failed to load. Infobox areas: none of Ancient Carthage, Mauretania, Colonies in antiquity or Mercenary War gives one, so no factor-of-two test was possible.
- Author's report and notes mark all four dossiers as kept from an earlier run (2026-10-19 01:37-01:41); carthage cites 13 pages against a budget of 9, mauretania 6 against 5 (stated by the author).
