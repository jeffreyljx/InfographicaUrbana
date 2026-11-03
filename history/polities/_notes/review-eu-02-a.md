# Review of batch eu-02-a (Hellenistic world, part a)

Reviewer run of 2026-10-18 (filled brief date). Machine copy: history/notes/phase-b/reviews/eu-02-a.json. Validator: no errors in any of the seven dossiers, before or after the reviewer's small fixes.

## Verdicts

- **macedonian-empire**: fail
- **athenian-coalition**: fix
- **kingdom-of-lysimachus**: fail
- **polyperchon**: fix
- **antigonid-dynasty**: fail
- **aetolian-league**: fail
- **chremonidean-alliance**: fix

Rule applied: a finding the reviewer applied (applied: true) is fixed in the dossier; any unapplied wrong correction, unexplained change or missing mirror of a confirmed event makes the dossier fail and go back to its author.

## macedonian-empire: fail

Area: infobox 5200000 (-323), Cliopatria 4700858 km2, ratio 0.9. acknowledged in the keyframe note

Findings:

- `/keyframe_review/15/correction` [to do] The 307-302 correction keeps the Iranian plateau, Afghanistan and the Punjab in Macedon's colour. Evidence: shapes.csv macedonian-empire_-307 is 1,526,818 km2 with bbox to 75.52 E; the seed gives centroid 49.42 E 35.79 N and modern countries Turkey, Pakistan, Afghanistan. The correction subtracts only Anatolia, Levant, Mesopotamia and Cyprus, while its own text says 'Cassander's Macedon, Thessaly and his Greek garrisons' and /ledger/40 gives the upper satrapies to Seleucus in 309. The note's 'Macedon plus Antigonus's Asia' misreads the shape. Fix: Use {"intersect": [{"cliopatria": "Macedonian Empire", "year": -307}, {"cliopatria": "Macedonian Empire", "year": -301}]} (the Balkan part), or add Iran, Afghanistan, Pakistan, Turkmenistan, Uzbekistan and Tajikistan to the minus. Then correct the note.
- `/ledger (after /ledger/40)` [to do] There is no loss of the Indus satrapies, yet keyframes 13-15 keep Pakistan in the shape until 302. Evidence: The /ledger/40 note itself says 'The Punjab had already passed to Chandra[gupta]'. The 315-308 and 307-302 shapes reach 75.5 E. Fix: Add a loss of Gandhara and the Punjab to maurya-empire: c. 317 (Eudemus leaves India) or 305-303 (the cession; Seleucus I Nicator page), confidence 2. Subtract the region in the 318 and 315 corrections from that year.
- `/ledger/31 and /keyframe_review/13/correction` [to do] Egypt leaves the empire with no ledger event. /ledger/31 is a vassal_end with no loss, and keyframe 13 removes Nile Valley and Cyrenaica from 318. Evidence: Check 4: a correction must be backed by ledger events. The 312 Seleucid case already does this with a vassal_end plus loss pair. Fix: Add a 321 loss to ptolemaic-kingdom, region union(Nile Valley (Egypt), Cyrenaica), source Partition_of_Triparadisus, confidence 2.
- `/ledger (393-379)` [to do] The Chalcidian League's hold on Macedonian land, Pella included, is missing. Evidence: chalcidian-league /ledger/1 is a 393 gain from macedonian-empire (Thessaloniki 25 km), /ledger/3 a 385 gain (Pella 30 km) and /ledger/8 a 379 loss. The Macedonia page says the Macedonians 'forced Olynthos to surrender and dissolve their Chalcidian League in 379 BC' after Olynthos nearly overthrew Amyntas III. Keyframe 5 (404-367) carries no event. Fix: Add a loss to chalcidian-league in 393 (Thessaloniki 25 km) and in 385 (Pella 30 km), and a gain in 379, confidence 2, sources Chalcidian_League and Olynthus.
- `/ledger (343-331)` [to do] The Epirote client kingship is missing. Evidence: kingdom-of-epirus /ledger/1 (vassal_start 343) and /ledger/6 (vassal_end 331) name macedonian-empire. The Macedonia page says Philip 'deposed Arybbas in Epirus in favour of his brother-in-law Alexander I'. Fix: Add vassal_start -343 and vassal_end -331 with kingdom-of-epirus, region Ioannina 45 km, confidence 2, source Alexander_I_of_Epirus.
- `/ledger/8-10` [to do] The Thracian sequence disagrees with odrysian-kingdom. Evidence: Here: vassal_start 347, vassal_end and gain 342. There: vassal_start 352 and loss 347 (odrysian /ledger/5-6); loss and vassal_start 340 (/ledger/9-10); vassal_end and gain back for Seuthes III in 325 (/ledger/11-12). The 340 and 325 events have no mirror here. Fix: Add vassal_start -340 (the interior under a strategos) and vassal_end plus loss -325 (Seuthes III's revolt) with odrysian-kingdom. Agree 352 or 347 for the first submission with eu-01.
- `/ledger (512-479)` [to do] Macedon's Persian vassalage is missing from this ledger. Evidence: The infobox says 'Vassal of Persia: 512/511-493 BC', and the notes of keyframes 1-2 rely on the Achaemenid dossier for it. A vassal relation belongs in both ledgers. Fix: Add vassal_start -512 and vassal_end -479 (or -493) with achaemenid-empire, region Macedonian Empire -550, source Macedonia_(ancient_kingdom), confidence 2.
- `/wars` [to do] Agis III's war (331) is missing. Evidence: peloponnesian-league /ledger/51-52 carries a 331 contest with macedonian-empire at Megalopolis (Sparta page). Fix: Add the war (-331..-331, zone Megalopolis 15 km) and the contest_start/contest_end pair.
- `/ledger/6` [to do] Thessaly is modelled as a vassal 'Thessalian League', while thessalian-league.json dissolves in 353 with macedonian-empire as successor, so the vassal has no living dossier. Evidence: thessalian-league /ledger/1: -353 dissolve into macedonian-empire. Cliopatria's 350 shape already reaches 38.87 N, which takes in Thessaly. Fix: Retype as a gain from thessalian-league (Thessaly, -352, confidence 2) so the land has an owner, or ask eu-01 to extend thessalian-league as a vassal to 196. The Antigonid dossier already holds Thessaly as territory.
- `/ledger/2, /ledger/37, /keyframe_review/14-16` [to do] Paeonia: the year disagrees (358 here, 356 in kingdom-of-paeonia). After the 315 vassal_end, the 315-292 shapes still take in the Vardar valley that kingdom-of-paeonia draws as independent (all of North Macedonia plus Blagoevgrad). Evidence: kingdom-of-paeonia keyframes -315 to -279 draw the whole of North Macedonia; macedonian-empire_-315 and _-301 reach 42.69 N. Both dossiers use the whole country, which also holds Upper Macedonian Lyncestis and Pelagonia. Fix: Subtract the Paeonian region from the 315 and 301 corrections, or narrow it (e.g. the Vardar valley north of Demir Kapija) in both dossiers. Agree one year with the Paeonia owner.
- `/keyframe_review/13/correction and polyperchon /ledger/3` [to do] The Polyperchon side does not match. Keyframe 13 subtracts Cliopatria's Polyperchon row (Upper Macedonia and Epirus), while polyperchon.json redraws that row as a rebel hatch over Ancient Macedon and Thessaly. Polyperchon's 316 loss to macedonian-empire has no gain here. Evidence: Both dossiers are in this batch. The 315 keyframe puts Upper Macedonia back with no event. Fix: Drop the Polyperchon subtraction from keyframe 13 (the hatch lies over the Macedonian colour), and add a gain from polyperchon in -316 (Ancient Macedon and Thessaly, Cassander page, confidence 3), or make polyperchon's 316 event a plain end.
- `/ledger (338)` [to do] aetolian-league /ledger/1, the 338 gain of Naupactus from macedonian-empire, has no mirror loss here. Evidence: The Aetolian League page says the league received 'Naupactus from Philip II of Macedon in 338 BC'. Philip had taken it from the Achaeans. Fix: Add a 338 gain of Naupactus (lon 21.83, lat 38.39, km 20) from greek-city-states and a 338 loss to aetolian-league, confidence 2.
- `/ledger/13/confidence` [applied] Confidence 3 with regions the page does not name. Evidence: Wars of Alexander the Great names the Granicus (May 334), Sardis, Halicarnassus, Caria (given to Ada) and the road to Phrygia. 'Neither [Lycia nor Pamphylia] appears anywhere on the page', and the Troad, Mysia and Ionia are not named either. Fix: Confidence 3 to 2, with a reviewer note.

Spot checks:

- `/ledger/13` Wars_of_Alexander_the_Great: confirmed for May 334, Sardis and Halicarnassus; Lycia, Pamphylia, Troad, Mysia and Ionia are not on the page, so confidence was lowered to 2
- `/ledger/15` Wars_of_Alexander_the_Great: confirmed (Tyre, January-July 332)
- `/ledger/17` Wars_of_Alexander_the_Great: confirmed (Gaugamela 1 October 331; 'advanced to Babylon and Susa')
- `/ledger/20` Wars_of_Alexander_the_Great: confirmed (Cyropolis and the Jaxartes 329; Sogdian Rock 327)
- `/ledger/22` Wars_of_Alexander_the_Great: confirmed (Hydaspes May 326, Punjab, Hyphasis mutiny, the Malli at Multan)

Thin (for a gap-filler):

- `/ledger/0` Foundation c. 675 at confidence 1 (try https://en.wikipedia.org/wiki/Argead_dynasty)
- `/ledger/19` 330 march through Hyrcania, Aria, Drangiana and Arachosia at confidence 1 (try https://en.wikipedia.org/wiki/Alexander_the_Great)
- `/ledger/34` 319 end of Laomedon's Syria at confidence 1 (try https://en.wikipedia.org/wiki/Laomedon_of_Mytilene)
- `/keyframe_review/1-4` 550-405: area 18,962 -> 28,540 -> 23,355 -> 29,436 km2 and the move west to 20.77 E, with no events (Bisaltia, Crestonia, Upper Macedonia) (try https://en.wikipedia.org/wiki/Alexander_I_of_Macedon)
- `/keyframe_review/16` 301-292 shape reaching 34.3 E (Cilicia, Pleistarchus?) is unconfirmed (try https://en.wikipedia.org/wiki/Pleistarchus)

## athenian-coalition: fix

Area: infobox None (None), Cliopatria 23257 km2, ratio None. war article, no area; the keyframe note gives the 23 k km2 shape and its four-year overrun

Findings:

- `/ledger/5/counterpart and /ledger/6/counterpart` [applied] The 322 losses named macedonian-empire, which records no gain. Macedon instead takes the Greeks back as vassals of the greek-city-states row. Evidence: greek-city-states /ledger/47 is a September 322 gain from athenian-coalition, and its note asks for this change. macedonian-empire /ledger/30 is a vassal_start of greek-city-states in September 322. Fix: Counterpart changed to greek-city-states on both events, with a reviewer note.
- `/keyframe_review/0/correction, /ledger/0/region, /ledger/7/region, /identity/predecessors/0/land, /identity/successors/1/land` [applied] The admin-1 unit Dytiki Ellada (all of Western Greece) drew Achaea and Acarnania as coalition members at confidence 3. Evidence: Lamian War page: the members include 'the Aetolian League', but 'Acarnania backed Macedonia (except Alyzeia)', and Peloponnesian Achaea is not among the listed members. Fix: Each Dytiki Ellada was replaced by {"cliopatria": "Aetolian League", "year": -284} (Aetolia proper, the same shape aetolian-league uses for 367-302). Elis stays in through the Pirgos radius of /ledger/3. A reviewer sentence was added to notes.

Spot checks:

- `/ledger/0` Lamian_War: confirmed ('probably in the beginning of September' 323)
- `/ledger/2` Lamian_War: confirmed (Phokis treaty 27 October)
- `/ledger/3` Lamian_War: confirmed (Sicyon 23 December; Argos, Acte, Phlius, Elis, Messenia)
- `/ledger/4` Lamian_War: confirmed (Crannon 6 August 322)
- `/ledger/6` Lamian_War: confirmed (Munychia 18 September 322; navy, garrison, possessions outside Attica)

## kingdom-of-lysimachus: fail

Area: infobox None (None), Cliopatria 488990 km2, ratio None. the Lysimachus page is a biography with no area; the keyframe notes quote the Cliopatria areas

Findings:

- `/keyframe_review/4/correction` [to do] The 291-285 correction adds Central Macedonia for the whole span, but Lysimachus took it only in 288/287 (/ledger/14). It also keeps the Cliopatria 291 shape's southern reach, which the note says to trim. Evidence: The keyframe's own text reads 'the 301 shape to 288; from 288/287 add the eastern half of Macedon'. Between 291 and 289 Central Macedonia is Demetrius's (antigonid-dynasty_-291, 127,922 km2 to 24.26 E), so it is drawn twice. The Lysimachus page has 'In 287 BC, Lysimachus and Pyrrhus in turn invaded Macedonia', and the infobox has 'Macedon 288-281'. Fix: Set keyframe 4 to 291-289 with keyframe 3's union (Kingdom of Lysimachus -315 plus Mysia, Troad, Lydia, Ionia, Phrygia and Zonguldak 90 km). Add a new keyframe kingdom-of-lysimachus_-288 (-288..-286) with that union plus Kentriki Makedonia.
- `/keyframe_review/5/correction and /keyframe_review/6` [to do] The 285-282 corrections use the Cliopatria 283 shape unchanged, south to 36.2 N (Lycia, Pamphylia, southern Caria). Keyframe 3's note calls that coast Ptolemaic and trims it; keyframe 6 is even marked ok. Evidence: shapes.csv kingdom-of-lysimachus_-283: bbox 19.33-35.59 E, 36.22-45.56 N. The page gives 'Lydia, Ionia, Phrygia and the north coast of Asia Minor'. Fix: Use {"minus": [{"cliopatria": "Kingdom of Lysimachus", "year": -283}, {"union": [{"region": "Lycia"}, {"region": "Pamphylia"}]}]} (plus southern Caria if confirmed) for keyframes 5 and 6, and set keyframe 6 to adjust.
- `/ledger/17` [to do] Thessaly in 288-285 has three different owners across the dossiers. Evidence: Here it is a 285 gain from kingdom-of-epirus (Western Macedonia and Thessaly). antigonid-dynasty /ledger/14 loses Thessaly to Lysimachus in 288 (confidence 1, no mirror here). kingdom-of-epirus /ledger/10-11 hold Western Macedonia only. The Lysimachus page does not mention Thessaly. Fix: Choose one owner with the Pyrrhus of Epirus page and align all three dossiers. Either add Thessaly to /ledger/14 and drop it from /ledger/17, or have antigonid /ledger/14 and kingdom-of-epirus /ledger/10 name Pyrrhus.
- `/ledger/0, /ledger/5, /ledger/6` [to do] The Seuthes III relation disagrees with odrysian-kingdom. Evidence: Here: contest 323-310 and vassal from 310 (confidence 1). odrysian-kingdom /ledger/13-18: contest 322-321, vassal from 321, contest 313-312. The Seuthes III page dates only the 322 draw ('They fought each other to a draw'), the 313 revolt and 'finally subdued Callatis in 310 BC'. The acknowledgement of Lysimachus is undated ('Ultimately, Seuthes appears to have acknowledged'). Fix: Agree one model with eu-01. Suggested: contest 322 only, contest 313-310, vassal from 310 at confidence 1. Non-blocking on its own.

Spot checks:

- `/ledger/13` Lysimachus: confirmed ('Lysimachus's share was Lydia, Ionia, Phrygia and the north coast of Asia Minor', 301)
- `/ledger/7` Lysimachus: confirmed (Lysimachia founded 309)
- `/ledger/9` Lysimachus: confirmed ('In 306/305 BC ... assumed the royal title')
- `/ledger/19` Lysimachus: confirmed (Corupedium 281; infobox February 281)
- `/ledger/4` Seuthes_III: confirmed ('finally subdued Callatis in 310 BC')

Thin (for a gap-filler):

- `/ledger/6` Seuthes III's acknowledgement of Lysimachus, undated on the page (confidence 1) (try https://en.wikipedia.org/wiki/Odrysian_kingdom)
- `/ledger/21` End of the Paeonian occupation in 281 (confidence 1) (try https://en.wikipedia.org/wiki/Ptolemy_Keraunos)

## polyperchon: fix

Area: infobox None (None), Cliopatria 69900 km2, ratio None. biography, no area; the Epirus part of the row was trimmed and said so

Findings:

- `/ledger/4/note` [applied] The quote was cut short and hid that the son was Cassander's appointee. Evidence: Polyperchon page: 'By 314 BC, his son Alexander had been appointed strategos (military governor) of the Peloponnese by Cassander'. The note quoted only up to 'strategos'. Fix: Quote completed, with a reviewer tag.
- `/ledger/3 and /ledger/7` [to do] Both losses (316 to macedonian-empire, 303 to antigonid-dynasty) lack mirrors on the other side. Evidence: macedonian-empire has only contest_end 316. antigonid-dynasty has no event naming polyperchon. Fix: Nothing to change in this dossier. The mirrors are listed under macedonian-empire and antigonid-dynasty.

Spot checks:

- `/ledger/0` Polyperchon: confirmed ('In 319 BC, shortly before his death, the aging Antipater appointed Polyperchon as regent')
- `/ledger/1` Polyperchon: confirmed ('major setback at Megalopolis in 317 BC')
- `/ledger/2` Polyperchon: confirmed (Olympias 'captured and murdered' in 316)
- `/ledger/7` Polyperchon: confirmed ('In 303 BC, Demetrius Poliorcetes launched a campaign in Greece')

Thin (for a gap-filler):

- `/ledger/4 and /keyframe_review/1` Peloponnese 315-303 at confidence 1. By 314 Alexander held it for Cassander, and Cratesipolis 'surrendered her fortresses' (Corinth, Sicyon) in 308, to Ptolemy on the usual account. Which cities were Polyperchon's in which years? (try https://en.wikipedia.org/wiki/Cratesipolis)

## antigonid-dynasty: fail

Area: infobox None (None), Cliopatria 137606 km2, ratio None. Antigonid dynasty infobox has no area (checked); the author says so

Findings:

- `/ledger (211, 210, 208)` [to do] The mirrors of three confirmed Aetolian events are missing. Evidence: aetolian-league /ledger/12: 211 gain of Oeniadae and Nasos. /ledger/13: 210 gain of Anticyra. /ledger/14: 208 loss of Epicnemidian and Opuntian Locris. First Macedonian War page: Laevinus 'handed the Acarnanian town of Oeniadae and the island of Nasos to Aetolia' (211); 'Aetolia took possession of the town' (Anticyra, 210); Philip 'captured Thronium ... Tithronium and Drymaea' and 'took Opus' (208). Fix: Add a loss to aetolian-league in -211 (lon 21.25, lat 38.45, km 25) and in -210 (lon 22.63, lat 38.38, km 20), and a gain in -208 (the /ledger/14 region), with the same confidences.
- `/ledger (303)` [to do] polyperchon /ledger/7, the 303 loss of the Peloponnese to antigonid-dynasty, has no gain here. Evidence: Polyperchon page: 'In 303 BC, Demetrius Poliorcetes launched a campaign in Greece' and reversed his gains. Only the 304 gain from macedonian-empire is here. Fix: Add a gain from polyperchon in -303, region minus(Peloponnese, Sparta 60 km), confidence 2.
- `/ledger (275)` [to do] achaean-league /ledger/1, the 275 expulsion of the Macedonian garrison of Aegium (confidence 3), has no loss here. Evidence: Aigio page via the achaean-league dossier: 'Around the year 275 BC, the people expelled the Macedonian garrison'. Fix: Add a loss to achaean-league in -275 (lon 22.081, lat 38.251, km 15), confidence 2.
- `/ledger (217)` [to do] kingdom-of-dardania /ledger/2, Philip V taking Bylazora in 217 (confidence 3), has no gain here. Evidence: Dardani page via the dardania dossier: 'managed to capture Bylazora from them in 217 BCE'. Fix: Add a gain from kingdom-of-dardania in -217, region admin1 Veles (North Macedonia, Natural Earth country 'Macedonia'), confidence 2.
- `/ledger (227)` [to do] kingdom-of-paeonia /ledger/8-9 (227, confidence 3) has no gain here. Evidence: Paeonia (kingdom) page: 'In 227 BC, Antigonus Doson conquered southern Paeonia'. Fix: Add a gain from kingdom-of-paeonia in -227, region union(admin1 Gevgelija, Strumitsa), confidence 2.
- `/ledger (198-197)` [to do] Argos is missing: Philip held it in 198 and handed it to Nabis. Evidence: Second Macedonian War page (opened by the author and cited): Philip was 'handing the city of Argos over to Nabis of Sparta' (winter 198/197). peloponnesian-league /ledger/57 gains Argos from antigonid-dynasty. Fix: Add a gain of the Argolid from achaean-league in -198 (Argos left the league for Philip) and a loss to peloponnesian-league in -197, confidence 2.
- `/ledger/34` [to do] The 219 gain from aetolian-league is Triphylia (Pirgos 40 km), but aetolian-league /ledger/8 loses Oeniadae and Elaeus in 219: same year, different land, and the Oeniadae gain has no mirror here. Evidence: Social War page: Philip 'conquered several cities, including Elaeus and Oeniadae' (219) and 'fought the Aetolians in Triphylia'. The infobox has 'Triphylia and Phthiotis to Macedon'. aetolian-league never draws Triphylia, and its note calls it Elean. A Pirgos 40 km circle is centred north of the Alpheus, in Elis proper. Fix: Add a 219 gain of Oeniadae and Elaeus (lon 21.25, lat 38.45, km 25) from aetolian-league. Recentre Triphylia south of the Alpheus (e.g. Zacharo 25 km) and either name greek-city-states (Elis) as counterpart or have aetolian-league record an Aetolian-held Triphylia.
- `/ledger/49` [to do] The 191 gain from aetolian-league (Demetrias, Larissa, Ioannina 45 km) has no mirror, and most of the land was not Aetolian. Evidence: aetolian-league has no 192 seizure of Demetrias and no 191 loss. Larissa belonged to the Roman-protected Thessalian League, and the Ioannina circle stands for Athamania, a separate kingdom (the note says so). Fix: Split by owner: aetolian-league for Demetrias (with a 192 gain and 191 loss added there), 'Thessalian League' for Larissa, Athamania for the Ioannina radius.
- `/keyframe_review/0/correction` [to do] The 306-302 keyframe draws Boeotia and Corinth from 306, but /ledger/2 gains them only in 304. Evidence: Demetrius I page, quoted in /ledger/2: 'In 304-303 he seized cities including Corinth'. In 306-305 they are Cassander's (macedonian-empire /ledger/47 loses them in 304). Fix: End keyframe 0 at -305 without Boeotia and Corinth, and add a new keyframe antigonid-dynasty_-304 (-304..-302) with them.
- `/keyframe_review/1 and /ledger/11` [to do] Boeotia is drawn as Antigonid in 301-295 (keyframe 1), then gained again in 291 from the 'Boeotian League' with no loss in between. Cyprus leaves between keyframe 1 and keyframe 2 (294) with no event. Evidence: Check 4: every change between keyframes needs an event. The author's gaps list Cyprus 294 as 'not on pages opened'. Fix: Drop Boeotia from keyframe 1 or add its loss after Ipsus. Add a 294 loss of Cyprus to ptolemaic-kingdom (Ptolemy I Soter page) or record it as a confidence 1 gap.
- `/ledger/13` [to do] The 288 loss to kingdom-of-epirus includes all of North Macedonia, where kingdom-of-epirus /ledger/10 gains Western Macedonia only. Evidence: kingdom-of-paeonia draws North Macedonia plus Blagoevgrad as independent in 315-286, so Paeonia is drawn twice. Fix: Drop {"country": "North Macedonia"}, or replace it with a Pelagonia/Lyncestis radius (e.g. Bitola 40 km).
- `/ledger/12/region` [applied] The 288 loss to Lysimachus included Western Macedonia, which /ledger/13 gives to Pyrrhus in the same year. Evidence: kingdom-of-lysimachus /ledger/14 gains Kentriki Makedonia. kingdom-of-epirus /ledger/10 gains Dytiki Makedonia. Ancient Macedon is the union of both. Fix: Region Ancient Macedon replaced by admin1 Kentriki Makedonia, with a reviewer note (Anatoliki Makedonia kai Thraki stays; Lysimachus's side should add it).
- `/wars/0/from` [applied] The Fourth War of the Diadochi started in -307, before the state's start in -306. Evidence: Check 2: wars must fall inside the life. The earlier part belongs to macedonian-empire's 'Wars of the Diadochi'. Fix: from -307 changed to -306.

Spot checks:

- `/ledger/16` Antigonus_II_Gonatas: confirmed for Lysimachia in 277. Control came later: 'By the end of 276 BC Antigonus had gained control of most of Macedon'; consider 276 or confidence 2
- `/ledger/18` Antigonus_II_Gonatas: confirmed ('Pyrrhus now took control of upper Macedonia and Thessaly, while Antigonus held on to the coastal towns'); the year 274 is derived from 'the next year' after 275
- `/ledger/24` Antigonus_II_Gonatas: confirmed ('regained control of Corinth in the winter of 245/44 BC')
- `/ledger/25` Antigonus_II_Gonatas: confirmed ('In 243 BC ... he seized the Acrocorinth')
- `/ledger/34` Social_War_(220%E2%80%93217_BC): confirmed (infobox 'Triphylia and Phthiotis to Macedon'); the land disagrees with aetolian-league, see the fix
- `/ledger/45` Second_Macedonian_War: confirmed ('Philip was forced to abandon Orestis and all possessions in Thessaly')
- `/ledger/38-39` First_Macedonian_War: confirmed (Lissus; Dassaretis, Atintani, Parthini and Dimale, 213-212)

Thin (for a gap-filler):

- `/ledger/14` Thessaly 288 (confidence 1) (try https://en.wikipedia.org/wiki/Pyrrhus_of_Epirus)
- `/ledger/15` Athens revolts 287, undated on the page (confidence 1) (try https://en.wikipedia.org/wiki/Demetrius_I_of_Macedon)
- `/ledger/23` Alexander of Corinth's revolt c. 253 (confidence 1) (try https://en.wikipedia.org/wiki/Alexander_of_Corinth)
- `/ledger/50` 185/184 surrender of the Thessalian and Athamanian towns (confidence 1) (try https://en.wikipedia.org/wiki/Philip_V_of_Macedon)
- `/keyframe_review/1` 301-295 holdings (Cyprus, Corinth, Boeotia) at confidence 1 (try https://en.wikipedia.org/wiki/Demetrius_I_of_Macedon)
- `/keyframe_review/12` The 256-248 shape reaches 19.2 E and is 22,762 km2 larger than 264-257, with no event (try https://en.wikipedia.org/wiki/Alexander_II_of_Epirus)
- `/keyframe_review/24` The 197-171 shape reaches 29.6 E (Aenus, Maronea), not on the pages opened (try https://en.wikipedia.org/wiki/Aenus)

## aetolian-league: fail

Area: infobox None (None), Cliopatria 11781 km2, ratio None. no infobox area (checked); the corrections roughly double the Cliopatria shape by adding the cantons, sourced to the peak-membership sentence

Findings:

- `/keyframe_review/15/correction` [to do] The 188-146 correction keeps all the central Greek cantons (Central Greece minus Boeotia and Euboea) as Aetolian. Its own text says 'Aetolia proper and Naupactus as a Roman client', and no ledger event removes the cantons. Evidence: The Aetolian League page names no 189 territorial clause; it says only that Aetolia 'was reduced to a Roman client state'. The correction contradicts its text. Fix: Make the correction {"union": [{"cliopatria": "Aetolian League", "year": -284}, {"lon": 21.83, "lat": 38.39, "km": 20}]} and add a 189 loss of the cantons (confidence 1, or 2 with the Aetolian War or Marcus Fulvius Nobilior page). Alternatively keep the cantons, but then fix the text and source them.
- `/keyframe_review/10-14/correction` [to do] From 210 the corrections add back the whole of 'Central Greece minus Boeotia and Euboea', although /ledger/10 loses Achaia Phthiotis in 217 (its polygon lies partly inside Central Greece) and /ledger/14 loses Epicnemidian and Opuntian Locris in 208. No event regains them. Evidence: Check 4: the corrections must agree with the ledger. The 208 loss is confirmed on the First Macedonian War page. Fix: Subtract the /ledger/10 and /ledger/14 regions from the 210-189 corrections (minus [..., union(those two intersects)]), or add sourced regain events (e.g. 196, if a page gives Phocis and Locris back).
- `/ledger (192-191)` [to do] The Aetolian seizure of Demetrias (192) and its loss (191) are missing. antigonid-dynasty /ledger/49 claims a 191 gain from aetolian-league. Evidence: Both dossiers are in this batch. The Aetolian League page dates the war with Rome from 'September 192 BC'. Fix: Add a 192 gain of Demetrias (Volos 25 km) and a 191 loss to antigonid-dynasty, or agree with antigonid that its 191 event names other owners.
- `/ledger/6` [to do] Ambracia: 233 here, 231 in kingdom-of-epirus /ledger/19 (confidence 1, bridged). Evidence: This dossier quotes 'the Aetolians seized Ambracia around 233 BC' from the Epirus (ancient state) page. Fix: Keep 233. The Epirus owner should move its loss to -233. Routed, non-blocking.
- `/wars` [to do] The Social War contest with achaean-league is missing (achaean-league /ledger/16 and /ledger/18). Evidence: The Social War page has the war 'Macedonian and Achaean victory' against the Aetolians. Fix: Add achaean-league to the Social War belligerents and a contest pair with it (Pirgos and Tripoli zones). Non-blocking.

Spot checks:

- `/ledger/1` Aetolian_League: confirmed ('Naupactus from Philip II of Macedon in 338 BC')
- `/ledger/2` Aetolian_League: confirmed ('Around 301 BC, the Aetolians took control of Parnassus')
- `/ledger/3` Aetolian_League: confirmed ('in 280 BC, they took control of Heraclea in Trachis')
- `/ledger/12` First_Macedonian_War: confirmed (Oeniadae and Nasos handed to Aetolia, 211)
- `/ledger/13` First_Macedonian_War: confirmed (Anticyra, 210)
- `/ledger/21` Aetolian_League: confirmed ('reduced to a Roman client state'; infobox 188)

Thin (for a gap-filler):

- `/ledger/0` Foundation and extent in 367 (confidence 1) (try https://en.wikipedia.org/wiki/Aetolia)
- `/ledger/5` Accession of Phocis, Locris, Doris, Malis, Dolopia, Achaia Phthiotis, Ainis and Oetaea as one confidence 1 step in 245 (try https://en.wikipedia.org/wiki/Phocis)
- `/keyframe_review/15` Roman client years 188-146 at confidence 1; the 189 clauses (Amphilochia, Cephallenia, Oeniadae, Acarnania) (try https://en.wikipedia.org/wiki/Marcus_Fulvius_Nobilior_(consul_189_BC))

## chremonidean-alliance: fix

Area: infobox None (None), Cliopatria 10805 km2, ratio None. war article, no area

Findings:

- `/ledger/2 (deleted)` [applied] The 265 'loss' of a 40 km Corinth radius to antigonid-dynasty: the alliance never held Corinth, and the circle reaches western Attica. Evidence: The found region is Attica plus Sparta 60 km. Chremonidean War page: 'in 265 BC Antigonus won a decisive and crushing victory outside Corinth' is a battle, not a transfer. antigonid-dynasty has no mirror. Fix: Event deleted. The 267-261 contest pair already covers Areus's defeat. A reviewer note was put on the 261 loss.
- `/ledger/3/counterpart (was /ledger/4)` [applied] The 261 loss of Attica named antigonid-dynasty, which takes Athens as a vassal of greek-city-states, not as territory. Evidence: antigonid-dynasty /ledger/22 and greek-city-states /ledger/59: 261 vassal_start over Attica. The page says Athens 'lost her last pre-Hellenistic vestiges of political independence'. Fix: Counterpart changed to greek-city-states.

Spot checks:

- `/ledger/0` Chremonidean_War: confirmed ('267-261 BC'; 'possibly as early as the autumn of 268 BC')
- `/ledger/1` Chremonidean_War: confirmed (Athens, Sparta and Ptolemaic Egypt against Macedon)
- `/ledger/2` Chremonidean_War: confirmed ('starved into surrender in either 262 BC or 261 BC')
- `/ledger/3` Chremonidean_War: confirmed ('lost her last pre-Hellenistic vestiges of political independence')

Thin (for a gap-filler):

- `/identity` Members beyond Athens, Sparta and Ptolemy (the decree of Chremonides); the page names only those three (try https://en.wikipedia.org/wiki/Chremonides)

## Cross-dossier matrix (unmatched and mismatched only; all rows in the JSON)

- macedonian-empire -358 vassal_start / kingdom-of-paeonia -> mismatch: 2 years apart: 358 (Philip II page) against 356 (Paeonia page); the author flagged it (mirror: kingdom-of-paeonia -356 vassal_start)
- macedonian-empire -352 vassal_start / Thessalian League -> mismatch: thessalian-league dissolves into macedonian-empire in 353, but Macedon makes the dead league a vassal; turn it into a gain or extend the league (mirror: thessalian-league -353 dissolve)
- macedonian-empire -347 vassal_start / odrysian-kingdom -> mismatch: odrysian has vassal_start 352 and loss 347; Macedon has vassal_start 347 and no gain in 347 (mirror: odrysian-kingdom -352 vassal_start)
- odrysian-kingdom -340 loss / macedonian-empire -> missing: odrysian /ledger/9-10 (340 loss and vassal_start of the interior) have no mirror in macedonian-empire
- odrysian-kingdom -325 gain / macedonian-empire -> missing: odrysian /ledger/11-12 (Seuthes III revolts c. 325) have no mirror in macedonian-empire
- polyperchon -316 loss / macedonian-empire -> missing: both dossiers are in this batch: macedonian-empire needs a 316 gain from polyperchon (Ancient Macedon, Thessaly)
- chalcidian-league -393 gain / macedonian-empire -> missing: chalcidian-league /ledger/1, /ledger/2, /ledger/3, /ledger/8 (393, 391, 385, 379) have no mirror in macedonian-empire
- kingdom-of-epirus -343 vassal_start / macedonian-empire -> missing: Epirote client kingship 343-331 (and vassal_end 331) is not in macedonian-empire
- aetolian-league -338 gain / macedonian-empire -> missing: Naupactus: macedonian-empire has no 338 event; both are in this batch
- peloponnesian-league -331 contest_start / macedonian-empire -> missing: Agis III war; macedonian-empire has neither the contest nor the war
- athens -322 dissolve / macedonian-empire -> mismatch: athens dissolves into macedonian-empire, while Macedon and greek-city-states model Athens as a GCS vassal; route to the athens owner (mirror: greek-city-states -322 vassal_start)
- corinth -338 dissolve / macedonian-empire -> mismatch: corinth dissolves into macedonian-empire, which records only the League of Corinth hegemony; route to the corinth owner (mirror: greek-city-states -337 vassal_start)
- greek-city-states -318 gain / macedonian-empire -> missing: greek-city-states /ledger/48 (confidence 1) has no mirror; the decree of Polyperchon is not territorial in this batch
- kingdom-of-lysimachus -310 vassal_start / odrysian-kingdom -> mismatch: 11 years apart; the Seuthes III page gives no year for the acknowledgement (mirror: odrysian-kingdom -321 vassal_start)
- odrysian-kingdom -313 contest_start / kingdom-of-lysimachus -> mismatch: odrysian contest 313-312 against Lysimachus; Lysimachus has 313-310 against the name Callatis and the west Pontic cities
- antigonid-dynasty -288 loss / kingdom-of-lysimachus -> missing: antigonid /ledger/14 loses Thessaly to Lysimachus (confidence 1); Lysimachus takes Thessaly from Epirus in 285 instead
- kingdom-of-lysimachus -285 gain / kingdom-of-epirus -> mismatch: year matches within 1; land differs: Lysimachus takes Western Macedonia and Thessaly, Epirus loses Western Macedonia only (mirror: kingdom-of-epirus -284 loss)
- kingdom-of-lysimachus -288 contest_start / kingdom-of-epirus -> missing: kingdom-of-epirus has no contest 288-285 with Lysimachus
- polyperchon -303 loss / antigonid-dynasty -> missing: both are in this batch: antigonid-dynasty needs a 303 gain from polyperchon
- antigonid-dynasty -288 loss / kingdom-of-epirus -> mismatch: year matches; land differs: antigonid adds all of North Macedonia, which kingdom-of-paeonia draws as independent (mirror: kingdom-of-epirus -288 gain)
- antigonid-dynasty -274 loss / kingdom-of-epirus -> mismatch: land: antigonid gives upper Macedonia and Thessaly as the page says; Epirus takes Ancient Macedon including the coast that Antigonus kept (mirror: kingdom-of-epirus -274 gain)
- chremonidean-alliance -261 loss / greek-city-states -> missing: after the reviewer fix; greek-city-states predates the split and has no 267 loss or 261 gain naming chremonidean-alliance; route to eu-01
- achaean-league -275 gain / antigonid-dynasty -> missing: Aegium expels its Macedonian garrison (confidence 3); no loss in antigonid-dynasty
- achaean-league -197 gain / antigonid-dynasty -> mismatch: achaean takes Corinth from antigonid in 197; antigonid gives Corinth to roman-republic in 196, and the Second Macedonian War page has Roman garrisons in Corinth until 194; route to eu-02-b (mirror: antigonid-dynasty -196 loss)
- peloponnesian-league -197 gain / antigonid-dynasty -> missing: Argos to Nabis; the Second Macedonian War page confirms it; antigonid needs a 198 gain and 197 loss
- antigonid-dynasty -219 gain / aetolian-league -> mismatch: year matches; land differs: antigonid takes Triphylia, aetolian loses Oeniadae and Elaeus (mirror: aetolian-league -219 loss)
- aetolian-league -211 gain / antigonid-dynasty -> missing: Oeniadae and Nasos (confidence 3); both are in this batch
- aetolian-league -210 gain / antigonid-dynasty -> missing: Anticyra (confidence 3)
- aetolian-league -208 loss / antigonid-dynasty -> missing: Locris and Opus (confidence 2)
- aetolian-league -211 contest_start / antigonid-dynasty -> missing: First and Second Macedonian War contests 211-206 and 199-197 with Aetolia are absent from antigonid, which has them against roman-republic only
- antigonid-dynasty -214 contest_start / roman-republic -> missing: roman-republic has no event naming antigonid-dynasty for 214-168; its /ledger/69-70 name the slug antigonid-macedonia, which will not exist (rename to antigonid-dynasty)
- antigonid-dynasty -196 loss / nobody -> mismatch: greek-city-states /ledger/67 (Freedom of the Greeks, confidence 3) gains from antigonid; antigonid names the Thessalian League, roman-republic and nobody (mirror: greek-city-states -196 gain)
- antigonid-dynasty -191 gain / aetolian-league -> missing: aetolian-league has no 192 gain or 191 loss of Demetrias; Larissa and Athamania are not Aetolian
- kingdom-of-dardania -217 loss / antigonid-dynasty -> missing: Bylazora (confidence 3); no gain in antigonid
- kingdom-of-paeonia -227 loss / antigonid-dynasty -> missing: southern Paeonia and the end of the kingdom (confidence 3); no gain in antigonid
- greek-city-states -167 gain / antigonid-dynasty -> mismatch: greek-city-states gains from antigonid-dynasty in 167, after its end in June 168; route to eu-01
- aetolian-league -233 gain / kingdom-of-epirus -> mismatch: 2 years apart; the Epirus page gives about 233, and the epirus dossier bridged 231 at confidence 1 (mirror: kingdom-of-epirus -231 loss)
- achaean-league -220 contest_start / aetolian-league -> missing: Social War contest with achaean-league is not in aetolian-league
- aetolian-league -192 contest_start / roman-republic -> missing: roman-republic has no event naming aetolian-league (contest 192-189, loss of Ambracia and vassal_start 189)

## Other problems

- No dossier in the batch has a validator error. The warnings left are the intended split warnings (athenian-coalition and chremonidean-alliance), the unpaired Thessalian, Odrysian and Roman vassal relations, and 'Aetolia' unknown to the gazetteer.
- Reviewer fixes applied in place and re-validated (no errors): macedonian-empire /ledger/13 confidence; athenian-coalition /ledger/5-6 counterparts and the five Dytiki Ellada regions; chremonidean-alliance (the 265 event deleted, the 261 counterpart changed); antigonid-dynasty /ledger/12 region and /wars/0 from; polyperchon /ledger/4 quote. Backups are in /tmp/claude-0/work/review-eu-02-a/bak/.
- Identity question for the orchestrator (not scored as a fault): master-plan rule 2 ('a dynasty that replaces a dynasty on the same land without a break stays in the state's dossier as a rename event') would make Demetrius's seizure of Macedon in 294 a rename inside one Macedon dossier. The author kept macedonian-empire (to 294) and antigonid-dynasty (306-168, with Antigonus's Asian kingdom 306-301) as two colours and flagged this in notes. Decide before the colour pass.
- antigonid-dynasty carries both Cliopatria rows, 'Antigonid Dynasty' and 'Antigonid Macedonia'. Group eu-02-b must not write antigonid-macedonia, and roman-republic /ledger/69-70 must rename its counterpart to antigonid-dynasty.
- Wikidata ids not verifiable here (wikidata.org unreachable; the Wikipedia pages fetched carry no Q-id): athenian-coalition Q33745 is the Cliopatria row's Peloponnesian War id and is wrong for the Lamian War league; chremonidean-alliance Q1073686 is unverified.
- kingdom-of-paeonia (another group) draws the whole of North Macedonia plus Blagoevgrad for 479-227. That also covers Upper Macedonian Lyncestis and Pelagonia and overlaps the Macedonian, Lysimachid and Antigonid shapes; the Paeonia owner and this batch's authors should agree a narrower region.
- Cross-group routing: greek-city-states (eu-01) needs the chremonidean split pair, its 348 double loss of the Chalcidice and its 167 gain from a dossier that ended in 168 fixed; odrysian-kingdom (eu-01) needs to agree the Seuthes III years; kingdom-of-epirus needs 233 for Ambracia, the 288-285 contest and the 274 land; achaean-league (eu-02-b) needs to agree Corinth 197/196; roman-republic needs mirrors for the Macedonian wars and the Aetolian war.
