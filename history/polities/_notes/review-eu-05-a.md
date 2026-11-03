# Review of batch eu-05-a (2026-10-19)

One dossier: `eastern-roman-empire` (395-632, 36 Cliopatria shapes, 94 events). Verdict: **fail**, a short return. The dossier is strong: it validates, all 36 shapes have verdicts, every keyframe transition is explained, the area check is right (infobox 2.35 M km2 for 457 against 1.98 M, ratio 0.84; 3.4 M for 565 against 2.60 M, ratio 0.77), and all 24 spot checks matched their pages. It goes back for three missing or misdrawn items listed below, which the reviewer could not add under the small-fix rule.

## Fixes the reviewer applied (re-validated, 0 errors)

- `/ledger/7..13 counterpart; /wars/4/belligerents`: Counterpart slug 'hunnic-empire' does not exist as a dossier: huns.json merges both Cliopatria rows (cliopatria_names ['Huns','Hunnic Empire'], 106-469) under the earlier slug per the Q45813 rule. Replaced 'hunnic-empire' with 'huns' in the 7 ledger counterparts and the war belligerents (cliopatria region specs naming 'Hunnic Empire' left as they are). Re-validated: 0 errors.
- `/ledger/15/counterpart; /ledger/18/counterpart`: Counterpart written as the name 'Kingdom of Odoacer' although history/polities/kingdom-of-odoacer.json now exists (reviewed pass in eu-04-b). Replaced with 'kingdom-of-odoacer'. Re-validated: 0 errors.
- `/identity/rulers/15/to`: Heraclius runs to 641, outside the dossier's life (end 632); rulers must lie inside the life. Set 'to' to 632 (note keeps the full reign dates). Re-validated: 0 errors.

## Findings for the author (not applied)

- `/ledger (missing, between /ledger/5 and /ledger/6)`: No mirror of the Hunnic occupation of 408-409 that huns.json records (/ledger/6 occupation_start 408, /ledger/7 occupation_end 409/3, conf 2/3).
  - Evidence: Uldin page: 'In the summer of 408 ... they entered the Balkans and Thrace.' 'The Huns captured Castra Martis in Dacia Ripensis.' Uldin 'was forced to re-cross the Danube by March 23, 409.'
  - Fix: Add occupation_start 408 (month 7 or none) and occupation_end 409/3, counterpart 'huns', region {'place': 'Castra Martis'} as a coordinate (Kula, Bulgaria, about 22.52 E 43.89 N, km 40) or the huns dossier's {'region': 'Moesia'} with text 'Castra Martis in Dacia Ripensis', source https://en.wikipedia.org/wiki/Uldin (add to sources), conf 3 for the end and 2 for the start; add a war entry 'Uldin's invasion of Thrace' 408-409.
- `/ledger/2/region; /ledger/5/region`: The Visigothic occupation is drawn over Thessaly, Central Greece, Attica, the Peloponnese and Epirus for all of 395-401, although the event's own region text ('... the Peloponnese (395-397), then Epirus (397-401)') and /keyframe_review/2 ('Greece returns but Epirus ...') say Greece was free from 397: the map hatches Greece for four years too many.
  - Evidence: Alaric I page: Stilicho 'pushed Alaric's forces north into Epirus'; in 397 Eutropius 'established Alaric as magister militum per Illyricum'.
  - Fix: Add an occupation_end 397, counterpart 'visigoths', region union Thessaly + Central Greece + Attica + Peloponnese (source Alaric_I, conf 2), and narrow /ledger/5 (401 occupation_end) to {'region': 'Epirus'}; keep /ledger/2's text.
- `/wars (missing); /ledger (missing contest pair 467-469)`: Dengizich's war on the Eastern Empire (467-469) is absent, though /ledger/13's note quotes 'In 469, Dengizich was defeated and killed in Thrace' and huns.json carries contest_start 467 / contest_end 469 with eastern-roman-empire over Moesia + Thrace.
  - Evidence: Huns page (in sources) as quoted in /ledger/13; huns.json /ledger/19-20 (source Dengizich).
  - Fix: Add a war 'Dengizich's war' 467-469, belligerents eastern-roman-empire and huns, zone Moesia + Thrace, and a contest_start 467 / contest_end 469 pair (counterpart 'huns'), or a war with empty zones and the reason if no ground changed hands.
- `/wars (missing)`: Garmul's war against the Eastern Romans in Africa (570-578), listed in mauro-roman-kingdom.json's wars, has no entry; the dossier's Moorish wars end in 548.
  - Evidence: history/polities/mauro-roman-kingdom.json wars: 'Garmul's war on the Eastern Romans' 570-578.
  - Fix: Add the war (Praetorian prefecture of Africa page or the Mauro-Roman Kingdom page), with empty zones and the reason if no ground changed hands; not blocking on its own.

## Minor points (no action required)

- `/ledger/51`: the contest starts in 571 (Armenian revolt, 'began in 571') while the war entry starts in 572; either is defensible.
- `/ledger/0` (395 Lazica vassal_start, no month) sorts before `/ledger/3` (the 395/1 found event); putting `found` first reads better.
- `/ledger/83` (626 gain of Colchis and Iberia, conf 2) rests on 'campaigned in the Caucasus, winning a series of victories', which names neither region; conf 1 would be more honest unless a page names Lazica.

## Spot checks

- `/ledger/7` (Attila): confirmed: 'The Hunnish army sacked Margus and Viminacium, and then took Singidunum (Belgrade) and Sirmium' (441).
- `/ledger/30` (Gothic_War_(535%E2%80%93554)): confirmed: 'In March 536, Mundus overran Dalmatia and captured ... Salona'; 'by late June, the whole of Dalmatia was in Byzantine hands'.
- `/ledger/33` (Gothic_War_(535%E2%80%93554)): confirmed: 'In May 540, Belisarius and his army entered Ravenna'.
- `/ledger/47` (Gothic_War_(535%E2%80%93554)): confirmed: 'not until 562 that their last strongholds, the cities of Verona and Brixia, were subjugated'.
- `/ledger/36` (Gothic_War_(535%E2%80%93554)): confirmed: Naples surrendered on terms in 543.
- `/ledger/53` (Byzantine%E2%80%93Sasanian_War_of_572%E2%80%93591): confirmed: Dara captured 'after a four-month siege', 573.
- `/ledger/60` (Byzantine%E2%80%93Sasanian_War_of_572%E2%80%93591): confirmed: Martyropolis 'fell to the Persians through the treachery of an officer named Sittas', 589.
- `/ledger/61` (Byzantine%E2%80%93Sasanian_War_of_572%E2%80%93591): confirmed: Khosrow II 'returned Dara and Martyropolis'; 'gives the Byzantine Empire most of Persian Armenia and western half of Iberia' (591).
- `/ledger/51` (Byzantine%E2%80%93Sasanian_War_of_572%E2%80%93591): confirmed: Armenian rebellion 'began in 571'; direct hostilities early 572 (war entry says 572; acceptable).
- `/ledger/56` (Avar%E2%80%93Byzantine_wars): confirmed: Sirmium 'fell in c. 581, or possibly 582'.
- `/ledger/58` (Avar%E2%80%93Byzantine_wars): confirmed: 'The Avars took the cities of Augustae, Singidunum, and Viminacium in 583'.
- `/ledger/59` (Avar%E2%80%93Byzantine_wars): conf 1 event supported indirectly: 'In 588, they abandoned the siege of Singidunum after only seven days', so the city was Roman by 588; no recapture date.
- `/ledger/84` (Avar%E2%80%93Byzantine_wars): confirmed: assault from 29 June 626, land assaults of 6-7 August repelled.
- `/ledger/66` (Roman%E2%80%93Persian_Wars): confirmed: 'Dara fell after a nine-month siege' (604).
- `/ledger/68` (Roman%E2%80%93Persian_Wars): confirmed: 'in 611 they overran Syria and entered Anatolia, occupying Caesarea'.
- `/ledger/69` (Roman%E2%80%93Persian_Wars): confirmed: 'Having expelled the Persians from Anatolia in 612'.
- `/ledger/21` (Roman%E2%80%93Persian_Wars): confirmed: 'Finally in 504, the Romans gained control through the renewed investment of Amida'; the Anastasian War page gives no year.
- `/ledger/80` (Roman%E2%80%93Persian_Wars): undated there ('Over the following decade the Persians were able to conquer Palestine, Egypt, Rhodes ...'); the 622/623 date rests on the 602-628 war page, not opened; conf 2 acceptable.
- `/ledger/79` (Sasanian_conquest_of_Egypt): confirmed: 'Alexandria was then betrayed to the Persians by a certain Peter in June 619'; 'by 621, the province was securely in Persian hands'.
- `/ledger/90` (Sasanian_conquest_of_Egypt): confirmed: 'in the summer of 629 the Persian troops began leaving Egypt'.
- `/ledger/81` (Spania): confirmed: 'by 624 the entire province of Spania was in Visigothic hands save the Balearic Islands'.
- `/ledger/52` (Spania): confirmed: Medina Sidonia and Cordoba retaken by Leovigild in 572.
- `/ledger/75` (Spania): confirmed at conf 2: Sisebut's expeditions 'in 614 and 615', Malaga conquered 'before 619'.
- `/ledger/5` (Alaric_I): confirmed: in 399 'they nominally transferred Alaric's province to the West'; invasion of Italy late 401 (Halsall) or spring 402 (Kulikowski).

## Thin (confidence-1 events for a gap-filler)

- `/ledger/4`: Date of the Hunnic withdrawal after the 395 raid (401 here, 396 in huns.json; both conf 1); the two dossiers must agree. Try https://en.wikipedia.org/wiki/Eutropius_(consul_399)
- `/ledger/13`: Year and agent of the Crimean (Cherson/Bosporus) gain of 469; huns.json hands Dobruja, not the Crimea, to the empire at 469. Try https://en.wikipedia.org/wiki/Bosporan_Kingdom
- `/ledger/22`: Gepid seizure of the Danube bank in 510 (Cliopatria's year only). Try https://en.wikipedia.org/wiki/Gepids
- `/ledger/45`: Return of the Gepid bank in 555. Try https://en.wikipedia.org/wiki/Sirmium
- `/ledger/46`: Avar cells at the Danube delta in 561 (pages give 558 or 568). Try https://en.wikipedia.org/wiki/Pannonian_Avars
- `/ledger/59`: Recapture of Singidunum: the Avar-Byzantine wars page shows it Roman by 588 (seven-day siege abandoned); could rise to conf 2 with that quote. Try https://en.wikipedia.org/wiki/Avar%E2%80%93Byzantine_wars
- `/ledger/63`: Inland contraction of Spania in 592 (Cliopatria's year). Try https://en.wikipedia.org/wiki/Spania
- `/ledger/71`: Interruption of the Ghassanid client relation 613. Try https://en.wikipedia.org/wiki/Ghassanids
- `/ledger/77`: Lazica's passage to Persia in 617 (Cliopatria's year); /ledger/83 regains it in 626 on a general Caucasus-campaign quote that names neither Colchis nor Iberia. Try https://en.wikipedia.org/wiki/Lazica
- `/ledger/78`: As /ledger/77: the Persian hold on Colchis and western Iberia 617-626. Try https://en.wikipedia.org/wiki/Byzantine%E2%80%93Sasanian_War_of_602%E2%80%93628
- `/ledger/88`: Date Rhodes returned (628 here). Try https://en.wikipedia.org/wiki/Rhodes
- `/ledger/91`: Resumption of the Ghassanid client relation 629. Try https://en.wikipedia.org/wiki/Ghassanids
- `/ledger/93`: 632 dissolve is a periodisation hand-over to byzantine-empire (by design; nothing to find). Try https://en.wikipedia.org/wiki/Byzantine_Empire

## Cross-dossier matrix (non-exception rows)

- eastern-roman-empire 395 occupation_start -> huns: **matched** (mirror huns 395 occupation_start). huns /ledger/4
- eastern-roman-empire 395 found -> roman-empire: **matched** (mirror roman-empire 395 split). roman-empire /ledger/131 split eastern-roman-empire 395/1
- eastern-roman-empire 401 occupation_end -> huns: **mismatch** (mirror huns 396 occupation_end). 5 years apart, both conf 1: ERE follows Cliopatria's 402 shape, huns ends in 396; a gap-filler should date the withdrawal and both adopt it
- huns 408 occupation_start -> eastern-roman-empire: **missing**. ERE lacks the 408-409 Uldin occupation (fix listed for ERE)
- huns 409 occupation_end -> eastern-roman-empire: **missing**. as above
- eastern-roman-empire 437 gain -> western-roman-empire: **matched** (mirror western-roman-empire 437 loss). WRE /ledger/25 (added after the eu-04-b review)
- eastern-roman-empire 441 loss -> huns: **mismatch** (mirror huns 441 contest_start). huns records only a contest 441-443; the Attila page says the Huns 'took Singidunum (Belgrade) and Sirmium': huns should add the 441 gain
- eastern-roman-empire 441 contest_start -> huns: **mismatch** (mirror huns 441 contest_start). years differ: ERE contest 441-449, huns 441-443 and 447-448
- eastern-roman-empire 447 loss -> huns: **mismatch** (mirror huns 447 contest_start). huns records a contest 447-448 but no gain of the strip south of the Danube
- eastern-roman-empire 449 contest_end -> huns: **mismatch** (mirror huns 448 contest_end). ERE closes in 449, huns in 448 (pages disagree 447/448/449)
- eastern-roman-empire 451 gain -> huns: **missing**. huns has no 451 loss of the Danube strip and cities to the empire
- eastern-roman-empire 455 gain -> huns: **missing**. huns has no 455 loss to the empire (its 455 loss is Pannonia to ostrogoths)
- huns 467 contest_start -> eastern-roman-empire: **missing**. ERE has no Dengizich war or contest 467-469 (fix listed for ERE)
- eastern-roman-empire 469 gain -> huns: **mismatch** (mirror huns 469 dissolve). huns dissolves to nobody in 469 and names Dobruja (Ernak's Huns) as the land passing to the empire; ERE gains the Crimea (conf 1): land disagrees
- eastern-roman-empire 476 vassal_start -> kingdom-of-odoacer: **missing**. kingdom-of-odoacer.json has no vassal_start toward eastern-roman-empire (route to its owner, eu-04)
- eastern-roman-empire 493 vassal_end -> kingdom-of-odoacer: **missing**. kingdom-of-odoacer.json ends 493/3 by dissolve to 'ostrogoths' with no vassal_end; acceptable once its vassal_start is added

67 further events are exceptions: counterpart `nobody`, the Mauri name, or a counterpart whose group has not run yet (lazica eu-19; visigothic-kingdom, visigoths, ostrogoths, ostrogothic-kingdom, kingdom-of-the-gepids, vandal-kingdom, avar-khaganate, lombards eu-06; sasanian-empire, ghassanids me-06; duchy-of-benevento, duchy-of-spoleto, kingdom-of-italy eu-13; byzantine-empire eu-05 sibling).

## Other notes

- The author's suggested slug `mauro-roman-kingdom` for the 534-548 Moorish counterpart is now taken by the western (Altava) kingdom, which records no contest with the empire in 534-548; the Byzacena/Aures Moors need their own name or slug (suggested `kingdom-of-the-aures`).
- Pages read by the reviewer: Byzantine Empire, Gothic War (535-554), Byzantine-Sasanian War of 572-591, Avar-Byzantine wars, Roman-Persian Wars, Sasanian conquest of Egypt, Spania, Attila, Anastasian War, Alaric I, Uldin. None failed to load.
