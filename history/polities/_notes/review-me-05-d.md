# Review of batch me-05-d

Reviewer, 2026-10-19. Dossiers: kingdom-of-pontus, galatia, kingdom-of-pergamon, paphlagonia, kingdom-of-sophene, revolt-of-aristonicus. Validator: 0 errors (one gazetteer warning, Acilisene). Neighbour ledgers read: kingdom-of-bithynia, seleucid-empire, greek-city-states, roman-republic, greek-colonies, rhodes, ptolemaic-kingdom, cimmerian-bosporus.

Verdicts: kingdom-of-pontus **fail**, galatia **fix**, kingdom-of-pergamon **fix**, paphlagonia **fail**, kingdom-of-sophene **thin**, revolt-of-aristonicus **pass**.

## kingdom-of-pontus: fail

- `/ledger/11` (for the author): The partition of Paphlagonia with Nicomedes III is dated -116 (c2) on a quoted line ('c. 116 BC: Mithridates and Nicomedes III of Bithynia invaded and divided Paphlagonia') that is not on the Kingdom of Pontus page; the page the author also opened dates it 108. Evidence: Kingdom of Pontus page (read 2026-10-19): no timeline at all; the partition sentence 'Mithridates and Nicomedes of Bithynia both invaded Paphlagonia and divided it amongst themselves' is undated, and the only '116' is 'In 116 the king of Cappadocia, Ariarathes VI, was murdered'. Mithridates VI of Pontus page: he 'contrived to partition [Paphlagonia] and [Galatia] with King Nicomedes III' and 'It was probably on the occasion of the Paphlagonian invasion of 108 BC that Mithridates adopted the Bithynian era'. 23 k km2 drawn Pontic 8 years early. Fix: Move /ledger/11 and /ledger/12 to -108 (after the -110 events, keeping the ledger sorted), cite Mithridates_VI_of_Pontus, drop the invented quote; extend /keyframe_review/8 (core, -120..-117) to -120..-111 and replace /keyframe_review/9 (-116..-111, core+Paphlagonia) so Paphlagonia is not Pontic before -108; /keyframe_review/10 (Cliopatria -110 shape, which already contains Paphlagonia) needs a new keyframe -110..-109 that subtracts the Paphlagonia -127 shape. Do the same in paphlagonia.json (end -108); galatia.json /ledger/5 was moved to -108 by the reviewer.
- `/ledger/9` (applied by reviewer): The -129 gain of Phrygia named roman-republic as counterpart while the Kingdom of Pergamon dossier records the same transfer as its loss to kingdom-of-pontus. Evidence: Aristonicus of Pergamon page: Aquillius 'dividing the Pergamene kingdom among Rome, Pontus, and Cappadocia'; kingdom-of-pergamon /ledger/15 -129 loss kingdom-of-pontus; the Roman Republic dossier has no Phrygia loss in -129. Fix: counterpart set to kingdom-of-pergamon (note extended).
- `/keyframe_review/11/correction` (for the author): The -105..-92 correction adds the whole region 'Crimea' as direct Pontic land, while /ledger/15 makes the Bosporan kingdom (circle 36.5 E 45.3 N, 90 km, the Kerch peninsula) a vassal; the Kerch peninsula is drawn both direct and vassal, and /ledger/41 then gives 'Crimea' to the Bosporus in -63. Evidence: Natural Earth 'Crimea' covers Kerch; the ledger note says only the Tauric Chersonesus was taken directly. Fix: Use {"minus": [{"region": "Crimea"}, {"lon": 36.5, "lat": 45.3, "km": 90}]} (the Chersonesus side) in /keyframe_review/11 and the same land in /ledger/14 and /ledger/41.
- `/ledger/21` (for the author): Pontus records Bithynia as a gain (-89) and loss (-85); the Kingdom of Bithynia dossier records a Pontic occupation_start at -88 (c3) and occupation_end at -85, quoting the same sentence, and another occupation in -90. Evidence: First Mithridatic War page: 'captured Bythinia without opposition' with no separate year; Kingdom of Pontus page: at Dardanus Mithridates had to 'return Bithynia and Cappadocia to their former kings'. kingdom-of-bithynia /ledger/8-11. Fix: Agree with the me-05 Bithynia author: preferably record occupation_start/occupation_end kingdom-of-bithynia (-89 or -88 / -85) in place of the gain/loss, hatched in the -87 keyframe; same question for Cappadocia (/ledger/20, /ledger/27).
- `/ledger/23` (for the author): Athens/Attica 88-86 is a contest with roman-republic here, but greek-city-states records a Pontic occupation of Athens (occupation_start kingdom-of-pontus -88, occupation_end -86, c3); Pontus has no occupation event to mirror it. Evidence: greek-city-states /ledger/74-75. Fix: Add occupation_start/occupation_end greek-city-states (Athens and Attica, -88/-86) citing First_Mithridatic_War, keeping the contest with Rome.
- `/ledger/39` (for the author): Galatia's -63 gain of 'part of eastern Pontus' (galatia /ledger/8, border band) has no matching Pontus loss; /ledger/39 gives Galatia only Lesser Armenia. Evidence: Deiotarus page: he 'increased his territory to include part of eastern Pontus'. Fix: Make /ledger/39 region a union of Lesser Armenia and the border band galatia/kingdom-of-pontus -63, or add a second c1 loss.
- `/ledger/16-20, /ledger/13, /ledger/36` (for the author): Several notes quote dated 'timeline' lines ('97: Cappadocian revolt crushed...', '91/90 BC: Tigranes invaded...', 'c. 115-106 BC: Inherited Lesser Armenia...', '63 BC: Western half of Pontus...') as page text; the Kingdom of Pontus page has no timeline. Evidence: The page's narrative carries the same facts (Senate decree after the 97 rebellion; Colchis and Lesser Armenia c. 115-106; western half annexed, infobox 63 BC), so the events stand, but the quotes are WebFetch summaries. Fix: Mark these as paraphrases, not quotations.
- thin `/ledger/10`: When Rome took Phrygia back: Pontus says -120 (c1, bridging); the Roman Republic dossier says -116; the Mithridates V page says he kept it until his death c. 120 and is silent after; the Mithridates VI page is silent. Try https://en.wikipedia.org/wiki/Phrygia
- thin `/ledger/14, /ledger/15`: Dates of the Chersonesus and Bosporan protection (Pontus -105 c1; greek-city-states -110 c2; cimmerian-bosporus -107 c2). Try https://en.wikipedia.org/wiki/Diophantus_(general)
- thin `/ledger/13, /ledger/47`: Dates of the Colchis conquests by Mithridates VI (c. 115-106) and Polemon I (undated). Try https://en.wikipedia.org/wiki/Colchis
- thin `/ledger/41, /ledger/42`: What became of the Tauric Chersonesus in 63 and the seat of the client kingdom after 63. Try https://en.wikipedia.org/wiki/Bosporan_Kingdom
- thin `/ledger/12, /ledger/20, /ledger/29`: Part of Galatia taken in the partition, the 90 reinvasion of Cappadocia, the 72 end of the Bithynian fighting (all c1). Try https://en.wikipedia.org/wiki/Third_Mithridatic_War
- Spot checks: `/ledger/21` confirmed (Bithynia 'captured ... without opposition'; the page gives no separate year, 89 rests on the war's chronology before 'early 88'); `/ledger/36` confirmed (infobox 63 BC; 'Most of the western half of Pontus and the Greek cities of the coast, including Sinope, were annexed by Rome directly'); `/ledger/46` confirmed ('in 31 BC, when the agreement was finalised, Antony gave Polemon Lesser Armenia as a reward'); `/ledger/48` confirmed ('In 62, Nero induced Polemon II to abdicate ... Pontus, including Colchis, became a Roman province'); `/ledger/11` mis-dated (partition undated on the page; the quoted 'c. 116 BC' line is not there; Mithridates VI page: 108 BC)
- Area: Kingdom of Pontus page has no area figure (confirmed); the author says so.

## galatia: fix

- `/ledger/12` (applied by reviewer): Amyntas' kingdom was dated -37 with counterpart nobody; the page dates his Galatian kingdom 36-25 BC and the Roman Republic dossier records the matching loss in -36. Evidence: Amyntas of Galatia page: 'King of Galatia and of several adjacent countries between 36 and 25 BC'; roman-republic /ledger/201 -36 loss galatia (eastern Phrygia, Lycaonia, Isauria, Pisidia). Fix: year -36, counterpart roman-republic; /keyframe_review/7 now -47..-37; /keyframe_review/8 renamed galatia_-36, from -36.
- `/ledger/5` (applied by reviewer): The 'part of Galatia' taken by Mithridates VI was dated -116 from an undated sentence; the Mithridates VI page dates the Paphlagonian-Galatian partition 108. Evidence: Mithridates VI of Pontus page: 'contrived to partition [Paphlagonia] and [Galatia] with King Nicomedes III' and 'the Paphlagonian invasion of 108 BC'. Fix: year moved to -108 (note extended); the Pontus dossier's /ledger/12 must follow.
- thin `/ledger/7, /ledger/8`: Where Deiotarus' 'part of eastern Pontus' lay and when the Senate granted Lesser Armenia (page: c. 65-60). Try https://en.wikipedia.org/wiki/Pompey's_eastern_settlement
- thin `/ledger/11`: Which dominions Caesar took from Deiotarus in 47 and who received them (Lesser Armenia to Ariobarzanes III of Cappadocia?); the counterpart roman-republic has no matching gain. Try https://en.wikipedia.org/wiki/Ariobarzanes_III_of_Cappadocia
- thin `/ledger/6`: Tetrarchies to kingdom: date of Deiotarus' kingship (c1). Try https://en.wikipedia.org/wiki/Galatia_(Roman_province)
- thin `/wars/0/zones`: The Battle of the Elephants war has no zone although its outcome is the settlement of northern Phrygia. Try https://en.wikipedia.org/wiki/Battle_of_the_Elephants
- Spot checks: `/ledger/1` confirmed ('fought in 189 BC'; Lampsacus terms 'stay confined within their own lands', undated); `/ledger/11` confirmed ('deprived of part of his dominions in 47 BC'; land unnamed, c1 is honest); `/ledger/12` mis-dated (36, not 37) - fixed by reviewer; `/ledger/13` confirmed ('After his death in 25 BC, Galatia was incorporated by Augustus into the Roman Empire')
- Area: Galatia page has no area (infobox 280-64 BC only).

## kingdom-of-pergamon: fix

- `/ledger/7` (applied by reviewer): A -217 loss of the whole 31 k km2 extension was given confidence 3, but the page names no land lost in 217. Evidence: Attalus I page: 'Achaeus returned from victory in Selge in 217 BC and resumed hostilities with Attalus'; nothing on Attalus losing territory. The Kingdom of Pergamon page has him regain 'control over his territories' only after Achaeus' death, so a loss between 218 and 213 is a bridging reading. Fix: confidence lowered to 1 (note extended).
- thin `/ledger/0-1`: Seleucid overlordship of Philetaerus and Eumenes I (281-261) and the Galatian tribute until Attalus I refused (c. 238-235). Try https://en.wikipedia.org/wiki/Philetaerus
- thin `/ledger/6-8`: Which cities Attalus took in 218 and held after 213 (Aeolis, Teos, Colophon?); the counterpart for 220-213 is the usurper Achaeus, not the Seleucid throne. Try https://en.wikipedia.org/wiki/Achaeus_(general)
- thin `/keyframe_review/5`: Lycaonia (124 cells) and Pisidia in the -188 shape: Livy's Apamea list gives Eumenes Lycaonia; the pages opened do not. Try https://en.wikipedia.org/wiki/Eumenes_II
- Spot checks: `/ledger/7` not on page as a loss (Achaeus 'resumed hostilities' in 217) - confidence lowered to 1 by reviewer; `/ledger/8` confirmed (Antiochus put Achaeus to death the year after 214; 'Attalus regained control over his territories'); `/ledger/12` confirmed ('gave Mysia, Lydia, Phrygia, and Pamphylia to the kingdom of Pergamon'); `/ledger/17` confirmed (infobox: incorporated into the province of Asia 129 BC)
- Area: Figure is in the body text ('143,000 square kilometres' for the expanded kingdom, no year); the author ties it to c. 227 and compares both the -225 shape (0.27, acknowledged) and the -188 shape (1.23).

## paphlagonia: fail

- `/identity/end, /ledger/3, /keyframe_review/2, /certainty/0` (for the author): The state ends -116 on a partition date that no opened page gives: the Kingdom of Pontus page leaves the partition undated and the Mithridates VI page dates it 108. Evidence: See kingdom-of-pontus /ledger/11: Kingdom of Pontus page 'Mithridates and Nicomedes of Bithynia both invaded Paphlagonia and divided it amongst themselves' (no year; its only '116' is Ariarathes VI's murder); Mithridates VI page 'the Paphlagonian invasion of 108 BC'. Fix: End -108; dissolve at -108 citing Mithridates_VI_of_Pontus; /keyframe_review/2 -126..-108; certainty to -108; wars[1] from -108.
- `/identity/successors/0/note` (applied by reviewer): The note said the Kingdom of Pontus dossier marks the whole shape as contested; it records an outright gain. Evidence: kingdom-of-pontus /ledger/11 is a gain of the whole Paphlagonia -127 shape, with no contest events. Fix: Note rewritten to say so and to flag the Bithynia share.
- thin `/identity/capitals`: Capital, founding and princes (Pylaemenes, Morzius) - page silent; native Paphlagonia after the Senate order of 97 and under Pompey. Try https://en.wikipedia.org/wiki/Pylaemenes
- Spot checks: `/ledger/1` confirmed (attack 'in the spring of 181 BC'); `/ledger/2` confirmed (peace with 'cession of all his conquests in Galatia and Paphlagonia, with the exception of Sinope', 179); `/ledger/3` mis-dated (partition undated on the page; Mithridates VI page gives 108); `/ledger/0` confirmed as undated (Pylaimenes princes, no founding year; c1 honest)
- Area: Region page, no area.

## kingdom-of-sophene: thin

- `/identity/capitals/0/to, /identity/capitals/1/to` (applied by reviewer): Both capitals ended -96 while the state ends -95. Evidence: identity.end -95 (infobox 'Conquered by Tigranes the Great: 95 BC'); other dossiers end the last capital at the end year. Fix: to set to -95.
- thin `/keyframe_review/7-10`: Who held the -63..113 cells: the page has Pompey install Tigranes the Younger and then cede 'the kingdom' to Ariobarzanes I of Cappadocia after 66 BCE, and 'Around 54 CE, the Romans installed Sohaemus of Emesa as King of Sophene'. The 54 CE client kingdom is a state the page attests; the dossier neither covers it nor lists it as a needed counterpart, and the page opened for it (Sohaemus of Armenia) is the wrong Sohaemus. Try https://en.wikipedia.org/wiki/Sohaemus_of_Emesa
- thin `/ledger/2`: Dates of Zariadres' gains (Acilisene, Akisene); gazetteer lacks both names. Try https://en.wikipedia.org/wiki/Zariadres
- thin `/identity/predecessors`: The found counterpart is kingdom-of-armenia but the author's report asks for an orontid-armenia dossier; pick one slug. Try https://en.wikipedia.org/wiki/Orontid_dynasty
- Spot checks: `/ledger/0` confirmed ('Most likely, Sophene emerged as a distinct kingdom' in the mid-3rd century BCE; year is Cliopatria's, c1 honest); `/ledger/1` confirmed (after Antiochus III's defeat in 190 Zariadres 'took the royal title'); `/ledger/2` confirmed (Acilisene and Akisene named, undated; c1 honest); `/ledger/3` confirmed (infobox 95 BC; Tigranes 'deposed Arsakes, the king of Sophene')
- Area: No area on the page.

## revolt-of-aristonicus: pass

Tried: type (rebel, held cities 133-129), dates, cities, counterpart chain (Pergamon contest -133..-129, Roman Republic -129 gain of Asia). Could not break it. Samos was probably not Pergamene in 133; the predecessor text 'the cities were Pergamene' is loose but harmless.

- Spot checks: `/ledger/0` confirmed (claimed the throne after Attalus III's death in 133; revolt start undated, c2 honest; Leucae, Samos, Myndus, Colophon, Thyatira, Apollonis all named); `/ledger/1` confirmed ('quelled by the Roman Republic in 129 BC')
- Area: No Cliopatria row; circles round named cities.

## Cross-dossier matrix

- kingdom-of-pontus -281 found nobody <-> seleucid-empire -279 loss: **mismatch**. Seleucid /ledger/14 loses Pontus to it in -279 (c1); Pontus is founded from nobody in -281 (Kingdom page: founded 281). Route to the seleucid-empire author (me-05).
- kingdom-of-pontus -279 gain greek-city-states <-> None None None: **missing**. Amastris (Kingdom page: captured 279). greek-city-states (eu-01) has no loss.
- kingdom-of-pontus -183 gain greek-city-states <-> None None None: **missing**. Sinope 183 (Paphlagonia page; Kingdom page 182). greek-city-states has no loss.
- kingdom-of-pontus -182 gain greek-city-states <-> None None None: **missing**. Coast east and west of Sinope (shape delta). greek-city-states has no loss.
- kingdom-of-pontus -129 gain kingdom-of-pergamon <-> kingdom-of-pergamon -129 loss: **matched**. Counterpart corrected by the reviewer from roman-republic.
- kingdom-of-pontus -120 loss roman-republic <-> roman-republic -116 gain: **mismatch**. Phrygia back to Rome: Pontus -120 (c1), Roman Republic /ledger/123 -116 (c2). Neither page opened dates it.
- kingdom-of-pontus -116 gain paphlagonia <-> paphlagonia -116 dissolve: **matched**. Both mis-dated: the partition is 108 (Mithridates VI page). Both go back to the author.
- kingdom-of-pontus -116 gain galatia <-> galatia -108 loss: **mismatch**. Galatia moved to -108 by the reviewer; Pontus /ledger/12 must follow.
- kingdom-of-pontus -105 gain greek-city-states <-> greek-city-states -110 loss: **mismatch**. Chersonesus: Pontus -105 (c1) vs greek-city-states /ledger/71 -110 (c2).
- kingdom-of-pontus -105 vassal_start cimmerian-bosporus <-> cimmerian-bosporus -107 vassal_start: **mismatch**. Bosporus records it at -107 (c2) in the vassal's own ledger with counterpart kingdom-of-pontus, against the schema (overlord records). Route to the cimmerian-bosporus author.
- kingdom-of-pontus -101 vassal_start kingdom-of-cappadocia <-> None None None: **exception**. kingdom-of-cappadocia not written yet (me-05 part running in parallel).
- kingdom-of-pontus -90 gain kingdom-of-cappadocia <-> None None None: **exception**. kingdom-of-cappadocia not written yet.
- kingdom-of-pontus -89 gain kingdom-of-bithynia <-> kingdom-of-bithynia -88 occupation_start: **mismatch**. Type differs (gain vs occupation by Pontus) and year (-89 vs -88); Bithynia also has a -90 Pontic occupation Pontus lacks.
- kingdom-of-pontus -88 gain roman-republic <-> roman-republic -88 loss: **matched**. Roman Asia and Phrygia.
- kingdom-of-pontus -88 contest_start roman-republic <-> greek-city-states -88 occupation_start: **mismatch**. greek-city-states records a Pontic occupation of Athens -88..-86; Pontus has only a contest with Rome.
- kingdom-of-pontus -85 loss roman-republic <-> roman-republic -85 gain: **matched**. Dardanus.
- kingdom-of-pontus -85 loss kingdom-of-bithynia <-> kingdom-of-bithynia -85 occupation_end: **mismatch**. Same type disagreement as -89.
- kingdom-of-pontus -85 loss kingdom-of-cappadocia <-> None None None: **exception**. kingdom-of-cappadocia not written yet.
- kingdom-of-pontus -72 occupation_start roman-republic <-> roman-republic -72 occupation_start: **matched**. Lucullus; both end -67.
- kingdom-of-pontus -66 occupation_start roman-republic <-> None None None: **missing**. Roman Republic has no occupation of Pontus 66-63 (it has a -65 gain instead). Route to eu-03.
- kingdom-of-pontus -63 loss roman-republic <-> roman-republic -65 gain: **mismatch**. Western Pontus and Paphlagonia: Pontus -63 (Kingdom infobox 63) vs Roman Republic /ledger/167 -65 (c2).
- kingdom-of-pontus -63 loss roman-republic <-> None None None: **missing**. Colchis to Rome (c2): no Roman Republic event (a client kingdom: vassal_start in the Roman ledger).
- kingdom-of-pontus -63 loss galatia <-> galatia -63 gain: **matched**. Lesser Armenia; Galatia's second -63 gain (eastern Pontus band) has no Pontus loss.
- kingdom-of-pontus -63 loss cimmerian-bosporus <-> None None None: **missing**. Crimea (c1): cimmerian-bosporus has no gain.
- kingdom-of-pontus -31 gain roman-republic <-> None None None: **missing**. Lesser Armenia to Polemon I (Polemon I page, 31 BC): Roman Republic has no loss (nor the -47 gain from Galatia).
- galatia -279 found seleucid-empire <-> seleucid-empire -279 loss: **matched**. Seleucid /ledger/11.
- galatia -63 gain kingdom-of-pontus <-> kingdom-of-pontus -63 loss: **mismatch**. Lesser Armenia matched; the eastern-Pontus border band has no Pontus loss.
- galatia -47 loss roman-republic <-> None None None: **missing**. Roman Republic has no -47 gain; the recipient is unknown on the page (probably Cappadocia).
- galatia -36 gain roman-republic <-> roman-republic -36 loss: **matched**. After reviewer fix (was -37, nobody).
- kingdom-of-pergamon -282 found kingdom-of-lysimachus <-> kingdom-of-lysimachus None none: **exception**. Lysimachus' kingdom ends -281; found events need no mirror.
- kingdom-of-pergamon -261 gain seleucid-empire <-> seleucid-empire -279 loss: **mismatch**. Pergamon page: Eumenes I beat Antiochus I near Sardis in 261; Seleucid /ledger/13 has the loss at -279 (c1). Seleucid side should move to -261.
- kingdom-of-pergamon -227 gain seleucid-empire <-> seleucid-empire -225 loss: **mismatch**. Two years apart (Attalus I page: Sardis spring 228).
- kingdom-of-pergamon -223 loss seleucid-empire <-> None None None: **missing**. Achaeus' recovery 223-221: no Seleucid gain.
- kingdom-of-pergamon -218 gain seleucid-empire <-> None None None: **missing**. Land then held by the usurper Achaeus (king 220-213), not the Seleucid throne.
- kingdom-of-pergamon -213 gain seleucid-empire <-> None None None: **missing**. No Seleucid loss.
- kingdom-of-pergamon -210 gain greek-city-states <-> None None None: **missing**. Aegina: greek-city-states has no loss (the Aetolians held it in 210).
- kingdom-of-pergamon -188 gain seleucid-empire <-> seleucid-empire -188 loss: **matched**. Apamea.
- kingdom-of-pergamon -129 loss kingdom-of-cappadocia <-> None None None: **exception**. kingdom-of-cappadocia not written yet.
- kingdom-of-pergamon -129 dissolve roman-republic <-> roman-republic -129 gain: **matched**. Province of Asia.
- paphlagonia -116 dissolve kingdom-of-pontus <-> kingdom-of-bithynia -127 occupation_start: **mismatch**. Bithynia occupies coastal Paphlagonia -127..-94 (c1); Paphlagonia has no occupation event and ends at the (mis-dated) partition.
- kingdom-of-sophene -256 found kingdom-of-armenia <-> None None None: **exception**. kingdom-of-armenia (eu-19) not written yet.
- kingdom-of-sophene -95 dissolve kingdom-of-armenia <-> None None None: **exception**. kingdom-of-armenia not written yet; Cliopatria's Armenia holds the cells only from -80.
- revolt-of-aristonicus -129 dissolve roman-republic <-> roman-republic -129 gain: **matched**. Covered by the Roman Republic's gain of the province of Asia.

## Problems

- WebFetch returns a model's answer, not the page text; the 'c. 116' partition line the author quoted was confirmed absent by a second targeted fetch of the Kingdom of Pontus page (it has no timeline).
- Reviewer edits applied and re-validated (0 errors): kingdom-of-pontus /ledger/9 counterpart; galatia /ledger/5 year, /ledger/12 year+counterpart, /keyframe_review/7-8 years and shape_id; kingdom-of-pergamon /ledger/7 confidence; paphlagonia /identity/successors/0/note; kingdom-of-sophene capital end years. Read back after ~10 s: all present.
- Schema vs reviewer brief: the schema puts vassal_start/vassal_end in the overlord's ledger only (counterpart = the vassal); the brief's mirror rule for vassals was not applied. cimmerian-bosporus records its Pontic vassalage in its own ledger, against the schema.
- Routing: roman-republic (eu-03) needs -66..-63 occupation of Pontus, -63 Colchis, -47 Lesser Armenia, -31 Lesser Armenia, and its -65/-116 dates reconciled; seleucid-empire (me-05) -261 Pergamon, -223..-213 Achaeus; greek-city-states (eu-01) Amastris 279, Sinope 183, Aegina 210; kingdom-of-bithynia (me-05) the 89-85 occupation type and the Paphlagonia partition (108).
