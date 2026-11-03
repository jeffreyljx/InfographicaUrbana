# Notes, group eu-03-b (Roman Republic, part b)

Owned state: roman-republic (1 dossier). The dossier was written on 2026-10-18 07:19 by an earlier, unsplit eu-03 run, 54 pages (the brief's budget for 50 shapes is 14, so it is not thin), and was KEPT UNCHANGED in this run after re-validation on 2026-10-19 (0 errors, 4 warnings, `--resolve` clean). The full per-state notes are in the dossier's own `notes` field; this file adds what the re-validation found.

## roman-republic

State and rows
- One state, one dossier, `cliopatria_names: ["Roman Republic"]`. 'Revolutionary Roman Republic' (1799, Q175881 shared by mistake in Wikidata) is the Jacobin republic of 1798-1799, a different state; its row belongs to the European 18th-century group. Do not merge.
- Corrections to Cliopatria's row: the Republic begins 509 BC (Cliopatria 500; the Roman Kingdom row's 500-481 shape belongs to it) and ends January 27 BC (Cliopatria 32). Cliopatria's Roman Empire row begins 31: the compiler must hand over at 27 BC, or the roman-empire dossier must start at 27.
- Biggest shape errors (34 adjust, 1 wrong, 16 ok): Numidia drawn Roman 212-198; the Regulus expedition drawn as territory 256-248; Sardinia and Corsica eight years late; Cisalpine Gaul kept two years after it rose for Hannibal; Macedon two years early and as direct rule in the merides years; an eastern Anatolian edge 164-145; Asia kept out 87-78; Armenia drawn Roman 66-64; Gaul added in one year (50) instead of 58-51; Syria kept lost to 37; Cyprus kept after 47.
- The '(Allegiance of Seleucid Empire to Roman Republic)' relation row (203-189) has no support on the pages opened (Magnesia 190, Apamea 188: indemnity and losses to Pergamon and Rhodes, not vassalage). The dossier has no vassal event for it.

Re-validation of 2026-10-19 (this run)
- `validate_dossier.py --resolve`: valid; 158 events, 54 sources, 51 keyframes, 784 regions, 0 unresolved names. The four warnings are vassal_start events with no vassal_end (Cappadocia, Galatia, Judea, Thracian kingdom): the relations last to 27 BC, which is the intended reading. Region names the earlier run said the gazetteer lacked (Samnium, Picenum, Sabina, Emilia, Isauria, Veii, Fregellae, Cales, Luceria and others) now resolve; 'Gallia Narbonensis' appears only in the notes text, not in a region.
- Spot-check against pages re-opened with WebFetch (Latin War, Macedonia (Roman province), Veii): the 338 BC suzerainty sentence, the 146/148 BC disagreement for the province of Macedonia and the 406-396 BC siege of Veii read as the ledger quotes them. Nothing was changed.
- Four sources are listed but not cited by any event, verdict or war (Roman Kingdom, Latin League, Volsci, Umbri); they back the predecessor relation and the notes. Harmless; a cleaner would drop them.
- Five confidence-3 events carry no quoted sentence (-241 contest_end, -222 contest_end, -171 contest_start, -148 vassal_end, -73 contest_start); their notes paraphrase the page. A reviewer who wants quotes should re-open First Punic War, Insubres, Third Macedonian War, Macedonia (Roman province) and Third Mithridatic War.

Counterparts that now have dossiers from other batches (the free-text counterpart strings in the ledger were written before they existed; the compiler should map them)
- 'Kingdom of Epirus (Pyrrhus)' -> kingdom-of-epirus (280-272 BC events).
- "Illyria (the three cantons of Gentius' kingdom)" (168 BC) -> illyrian-kingdom, whose dossier runs 256-168 BC.
- 'Gallic tribes (...)' (58-50 BC), 'Arverni and Allobroges' (121 BC) -> no dossier yet; see below.
- Dossiers that exist for the slugs used as counterparts: carthage, samnites, celtiberians, italian-city-states, insubres, etruscans, greek-city-states, boii, sertorian-hispania, picentes, syracuse, kingdom-of-numidia, lucanians, mamertines, adriatic-veneti, roman-kingdom, volsci, latin-league, aequi, sabines, senones, molossians, achaean-league, lusitanians, thracian-kingdom. Slugs still without a dossier on 2026-10-19 (Cliopatria rows owned by other groups, being written in parallel): kingdom-of-pontus, kingdom-of-armenia, cyrenaica, judea, ptolemaic-kingdom, antigonid-macedonia, galatia, parthian-empire, kingdom-of-pergamon, kingdom-of-cappadocia, kingdom-of-bithynia, seleucid-empire, roman-empire.

States still needing a dossier (not Cliopatria rows; none was written here because the brief leaves them to the additions batch eu-03-x)
- Arverni, Helvetii, Belgae, Allobroges and the other Gallic tribes of Caesar's war (events 121, 58-50 BC).
- Messapii and Sallentini (event c. 266 BC, confidence 1).
- The Marsi, Marrucini, Paeligni, Frentani and Vestini, treated in the ledger as one allied group (304-91 BC).
- The Bruttii (named in the dossier's notes, no ledger event).
- Aristonicus' revolt as Eumenes III (133-129 BC; a rebel state on the Pergamene land).
- The Cilician pirates (103, 74, 67 BC), marginal.
- The Pompeian faction of 49-45 BC is not a state; the ledger uses it only as the counterpart of the civil-war contest. Smaller counterparts (Fidenae, the Ausones of Cales, the Greek cities and towns of the Illyrian coast, the Macedonian merides) are not worth dossiers.

Gaps (all confidence 1 or page silent, from the dossier): Sallentini/Brundisium c. 266; the part of Cilicia made a province in 103; Galatia's client date (63); the Veneti's amicitia (238); the Balearic conquest of 123 (no page opened); the Ligurian wars 238-155 (no page); the dates of Rome's Sicilian towns 261-241; Pompey's eastern clients (Commagene, Osroene, the Nabataeans, Deiotarus; the Third Mithridatic War page does not cover the settlement); the Dalmatian coast north of Lissus (Octavian 35-33).

Disagreements between pages (the dossier gives both): Sardinia ceded 238 or 237; New Carthage 209 or 210; the two Spanish provinces 197 or 198; province of Macedonia 148 (text) or 146 (infobox); Crete conquered 66, joint province 67; Sertorius murdered 72 or 73; Antonius' Cilician command 103 (Cilicia page) or 102 (usual); Hiero II died 215 or 216; the Social War 91-87 against Cliopatria's Italian City-States row ending 88; the Hispania conquest page summary covered only its first 100,000 characters.

Pages that failed: none in this run. No gazetteer names are needed.
No ruler strip: the annual consuls are not a ruler list in the sense of rule 10.

## Second round, 2026-10-19 (eu-03-b-fix, after the reviewer's FAIL)

Dossiers touched: roman-republic.json (216 events, 53 keyframes, 38 wars, 82 sources; 0 errors, 5 warnings, all vassal_start with no vassal_end that last to 27 BC; `--resolve` clean) and one new rebel dossier, sextus-pompeius.json (10 events, 3 keyframes, 1 war, 2 sources; 0 errors, 0 warnings). Every changed event was checked on a page opened again that day.

Applied (15 of the reviewer's 17 open findings, plus 4 thin items)
- Africa 146: region is now Cliopatria's Carthage shape of 149 (northern and central-eastern Tunisia, about 46,000 km2), not 'Africa Proconsularis'; Utica (149), the 201 client state (vassal_start 201, vassal_end 146), Selinous/Heraclea Minoa/Thermae/Lipara (252) and Agrigentum (213 loss) added as the Carthage mirrors. The Africa page names neither Thabraca nor Thaenae; the Third Punic War page has no boundary.
- 31-27 BC: keyframes roman-republic_-31 (Cyprus back, 'Cyprus returns to Roman rule') and roman-republic_-30 (plus Egypt, 'seized by Octavian as his personal possession', August 30; plus Cilicia Aspera at confidence 1); events gain ptolemaic-kingdom for Cyprus (31), Egypt (Aug 30), Cilicia Aspera (30); the dissolve event and successors now include them. The -36 keyframe is cut to 36-31 in its text.
- New events: vassal_start mauretania 33; Dalmatae contests and gains 76 (Salona) and 33 (Dalmatia); loss cimmerian-bosporus 48 and gain 47 (Pontus); Greek and Illyrian events 214-146 (Illyrian protectorate lost 212 and restored 205, garrisons of Corinth, Chalcis and Demetrias 197/196-194, Aetolian contest 191-189 and client state 189-146, Thessalian koinon 196-146, Leucas 168); Umbria (gain 299 Narnia, vassal_start c. 260, vassal_end 90); loss insubres 218 split from the Boii's; Locri 277; loss sertorian-hispania 80 (Lusitania); Balearic Islands 122; Ligurian contest 238-155; Liberators' contest 43-42; Sextus Pompeius' contests and losses 42-36.
- Counterparts re-pointed: kingdom-of-epirus (contest and 280 loss), croton (277), taras (272), massalia (49).
- Wars added: First and Second Macedonian, Roman-Seleucid (Aetolian phase), Dalmatian, Cimbrian (empty zones), Second Mithridatic (empty zones), Liberators', Sicilian (Sextus Pompey), Caesar-Pharnaces, Ligurian; Third Punic War and War of Actium zones corrected.
- Keyframe 480 gets a 10 km disc at Rome (the shape's east edge is 12.4517 E, the capital 12.48 E).
- Thin items filled: Messapii and Brundisium 267, Salento 266 (Messapians page); Cilicia 102 (Marcus Antonius Orator page: 'in 102 Antonius was elected praetor with proconsular powers for the Roman province of Cilicia'); Balearics 122 (page: command 123, 'continued into 122', 'By 121 BC ... conquered'); Ligurian wars.

Where I disagree with the reviewer (with the page)
- /ledger/143: two fresh reads of https://en.wikipedia.org/wiki/Roman_Cyprus return 'in 40 BC, Antony reaffirmed that Cleopatra was ruler of Cyprus at the Donations of Alexandria'. The reviewer's quote omitted 'in 40 BC'. The Donations of Alexandria page says 'autumn 34 BC'. The note now gives both; the page has an internal date error.
- /ledger/33 (gain syracuse 263): not added. Hiero II page: 'he was to rule over the south-east of Sicily and the eastern coast as far as Tauromenium', nothing about cession; First Punic War page: 'it became a Roman ally, paid an indemnity of 100 talents of silver'; Sicilia page: Syracuse 'an independent ally of Rome until its defeat in 212 BC', Tauromenium under Syracuse 'until 212 BC'. syracuse.json /ledger/16 is an inference; its author should make it a vassal_start.
- Samnites, Lucanians, Etruscans, Picentes, Insubres as socii (modelling conflict): kept. The Social War page and Cliopatria's Italian City-States row treat them as allied until 91-89. Their dossiers dissolve at conquest with no vassal pairs; one side must change (RR's reading is the one that matches the pages).
- Pact of Misenum: the Sextus Pompey page says 'Sicily and Sardinia' only; Corsica and the Peloponnese are not on it. Corsica is included with Sardinia because they were one province (confidence 2). 'Sicilian revolt' on Wikipedia is a disambiguation list; the war is cited to the Sextus Pompey and Menas pages.
- Cilicia Aspera 31-27 is confidence 1: the Cilicia page gives 36 (to Cleopatra) and 25 (to Archelaus), nothing between.

Pages that failed or were not articles: https://en.wikipedia.org/wiki/Menodorus (use Menas_(admiral)), https://en.wikipedia.org/wiki/Sicilian_Revolt (not found), https://en.wikipedia.org/wiki/Sicilian_revolt (disambiguation list), https://en.wikipedia.org/wiki/Roman%E2%80%93Seleucid_War (not found; the article is Roman%E2%80%93Seleucid_war).

Still silent after the page tries (gap-fillers): Veneti amicitia 238 (Cenomani page says nothing); the end of the Mamertine alliance 257 (Messina page: 'At the end of the First Punic War it was a free city allied with Rome'); the recovery of Syria (Ventidius page undated); Galatia as client (Deiotarus: king 'sometime between 60 BC and 65 BC'); Commagene, Osroene and the Nabataeans (Pompey page does not mention them); Sicilian towns 261-241 (Sicilia page: west Roman 241, Syracuse 212).

Asked of other batches: greek-city-states drops its 49 (Massilia) and 146 (Epirus, Thessaly) losses; kingdom-of-epirus and molossians are one state in two dossiers (RR's 167 gain names molossians); boii books its 218 loss as a loss (RR has loss boii); antigonid-dynasty books Corinth, Chalcis, Demetrias as a 196 loss, RR has occupations (Corinth under achaean-league); samnites, lucanians, etruscans, picentes, insubres, adriatic-veneti, mamertines, kingdom-of-numidia add the vassal pairs RR carries; carthage 201 is a vassal_start both ways now.
Counterparts without dossiers that RR now uses: ligures, messapii (with the Sallentini), locri, the Illyrian protectorate towns (Parthini, Atintani, Dimale), ptolemaic-kingdom, kingdom-of-pergamon, seleucid-empire (me-05). New slug: sextus-pompeius (rebel).
