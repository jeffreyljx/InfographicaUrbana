# Review of batch eu-03-b (roman-republic)

Reviewer run of 2026-10-19. Inputs: author report reports/eu-03-b.json, notes _notes/eu-03-b.md, dossier history/polities/roman-republic.json (158 events, 51 keyframes, 28 wars, 54 sources). Neighbour dossiers read: every Context polity of brief section 6 that has a file (greek-city-states, etruscans, mauretania, kingdom-of-numidia, thracian-kingdom, carthage, greek-colonies, roman-kingdom, mamertines, molossians, italian-city-states), plus every other dossier in history/polities/ that names roman-republic as a counterpart.

## Verdict: FAIL (back to the author)

Mechanical checks pass: validator 0 errors and 4 vassal_start-without-end warnings, all intended to last to 27; --resolve clean; all 50 Cliopatria shapes have verdicts; found at -509 and dissolve at -27; family rome exists; years in order.
All six spot checks (eight events) held on year and fact. The dossier fails on land, not on dates: six blocking findings remain, five for missing events and one for a wrong 146 BC region. Most of these are mirrors that counterpart dossiers written after 2026-10-18 now carry at confidence 2-3, and the kept-unchanged run did not integrate them.

## Fixes applied by the reviewer (validated afterwards)

- `/ledger/69/counterpart, /ledger/70/counterpart, /wars/5/belligerents, /wars/7/belligerents, /wars/11/belligerents`: Counterpart slug 'antigonid-macedonia' will never have a dossier: antigonid-dynasty.json lists both 'Antigonid Dynasty' and 'Antigonid Macedonia' in cliopatria_names. Evidence: history/polities/antigonid-dynasty.json identity.cliopatria_names; its life -306..-168 covers the 171-168 contest. Done: Replaced with 'antigonid-dynasty' (5 slug tokens, plus the notes text).
- `/ledger/72/counterpart, /ledger/75/counterpart, /ledger/76/counterpart`: Free-text counterpart 'Macedonian merides (four client republics)' now has a dossier, macedonian-republics. Evidence: macedonian-republics.json: vassal_start to roman-republic -168, vassal_end -148, dissolve -148 (mirrors RR -167 vassal_start and -148 gain and vassal_end). Done: Replaced with 'macedonian-republics'.
- `/ledger/80/confidence`: Confidence 3 on a region the page does not give for 146 BC. Evidence: https://en.wikipedia.org/wiki/Africa_(Roman_province): the 'present-day Tunisia, the northeast of Algeria, and the coast of western Libya' sentence is undated, and 'The remaining territory was left in the domain of the Berber Numidian king Massinissa.' Done: Lowered to 2 with a reviewer line in the note.
- `/ledger/149`: The note quoted a sentence that is not on the cited page, and the page does not date the Roman recovery of Syria. Evidence: https://en.wikipedia.org/wiki/Roman%E2%80%93Parthian_Wars has no 'held Syria for roughly two years' and no Gindarus. It says: 'After suffering a further defeat near the Syrian Gates, the Parthians withdrew from Syria' (undated) and 'They returned in 38 BC, but were decisively defeated by Ventidius and Pacorus was killed.' The year 38 is defensible, but the withdrawal may be 39. Done: Replaced the note with the page's sentences and lowered confidence 3 to 2.
- `/ledger/143/note`: The note says Antony reaffirmed Cleopatra's Cyprus 'in 40'. Evidence: https://en.wikipedia.org/wiki/Roman_Cyprus: 'Antony reaffirmed that Cleopatra was ruler of Cyprus at the Donations of Alexandria.' That was 34, not 40. Done: Changed to 'at the Donations of Alexandria (34)'.
- `/ledger/114/note`: The quoted sentence was a paraphrase, not the page text. Evidence: https://en.wikipedia.org/wiki/Bithynia_and_Pontus: 'In 74 BC, during the Third Mithridatic War, King Nicomedes IV of Bithynia died ... bequeathed his kingdom to Rome'; 'The Senate immediately voted to annex the kingdom as a province directly governed by the Republic.' Done: Replaced with the page's words. The event itself is confirmed.

## Findings for the author (not applied)

- `/ledger/80/region`: BLOCKING. The 146 BC gain uses the gazetteer region 'Africa Proconsularis'. That region is Tunisia plus Tripolitania plus Algeria's Constantine, Annaba, Skikda and Guelma provinces, so it gives Rome Cirta and Tripolitania in 146.
  - Evidence: Africa page: the rest 'was left in the domain of ... Massinissa'. kingdom-of-numidia holds Lepcis and Tripolitania from 158 (its /ledger/2) and eastern Numidia until 46; RR's own /ledger/144 gains eastern Numidia only in 46. Region is gazetteer regions.jsonl 'Africa Proconsularis'.
  - Fix: Replace the region with Carthage's last territory east of the fossa regia (Thabraca to Thaenae): northern and central-eastern Tunisia, as admin1 units or Cliopatria's Carthage -149 shape. Text: 'the Carthaginian territory annexed as the province of Africa, capital Utica'.
- `/keyframe_review/50/correction and /ledger after 156`: BLOCKING. The last correction runs the -36 shape 'to January 27 BC' without Cyprus and Cilicia Aspera. The ledger has no event for 31-27 beyond Thrace. The /ledger/156 note says 'Egypt (30) is the Empire's', yet the dossier itself ends in 27.
  - Evidence: https://en.wikipedia.org/wiki/Roman_Cyprus: after Actium Octavian 'gained control of Egypt and Cyprus', 'Cyprus returns to Roman rule' (31 BC). Egypt was annexed in August 30, inside this dossier's life. Cliopatria's ptolemaic-kingdom_-30 shape runs to -28 and roman-empire_-27 is the first shape with Egypt.
  - Fix: Pick one. (a) Add a new keyframe roman-republic_-31 (from -31 to -27) whose correction is the -36 shape plus Cyprus and Cilicia Aspera from 31/30 and Egypt from August 30, with matching ledger events (-31 or -30 gain ptolemaic-kingdom for Cyprus and Cilicia Aspera; -30 gain ptolemaic-kingdom for Egypt). (b) End the Roman land at -31 and hand over to roman-empire, saying so in successors.
- `/ledger (new, -33)`: BLOCKING (missing event). The 33 BC Mauretanian bequest has no RR event.
  - Evidence: https://en.wikipedia.org/wiki/Mauretania: 'Upon his own death in 33 BC, Bocchus II bequeathed his entire kingdom to Octavian', 'placed Mauretania under temporary Roman administration for eight years'. mauretania.json /ledger/9 has vassal_start roman-republic -33 at confidence 3.
  - Fix: Add vassal_start mauretania -33 (region: Cliopatria Mauretania shape, text from the page; source Mauretania page). It lasts to the end in -27.
- `/ledger (new, -76 and -33)`: BLOCKING (missing events). The Dalmatian coast and Illyricum are listed as 'page silent', but a page exists and a counterpart dossier carries both events.
  - Evidence: dalmatae.json /ledger/5 (-76 loss of Salona to RR, C3) and /ledger/8 (-33 dissolve to RR, C3, 'Dalmatia, now Roman Illyricum'), both from https://en.wikipedia.org/wiki/Dalmatae: the Roman-Dalmatae wars 'lasted until 33 BC when Octavian' installed Roman hegemony.
  - Fix: Add gain dalmatae -76 (Salona) and gain dalmatae -33 (Dalmatia), sourced to the Dalmatae page, and check the Cliopatria -36 shape for that coast in the keyframe note.
- `/ledger (new, -48 and -47)`: BLOCKING (missing events). Pharnaces II took Roman Pontus in 48 and lost it at Zela in 47; RR has no event.
  - Evidence: cimmerian-bosporus.json /ledger/13 (-48 gain of Colchis, Lesser Armenia and Pontus from RR, C2) and /ledger/14 (-47 loss to RR, C3), from https://en.wikipedia.org/wiki/Pharnaces_II_of_Pontus.
  - Fix: Add occupation_start (or loss) -48 and occupation_end (or gain) -47 against cimmerian-bosporus for Pontus (the Pontic half of Bithynia et Pontus), and add the war (Caesar's war with Pharnaces, Zela 47) to wars[].
- `/ledger (new, 212-146 BC, Greece) and /wars`: BLOCKING (missing events and wars). Rome's Greek and Illyrian protectorates between the Illyrian Wars and 146 have no events, and wars[] has no First Macedonian War (214-205), Second Macedonian War (200-197) or Roman-Seleucid/Aetolian War (192-188).
  - Evidence: aetolian-league.json /ledger/25: vassal_start roman-republic -189, C3 ('Aetolia was reduced to a Roman client state', Roman-Seleucid war page), plus /ledger/24 Ambracia 189. thessalian-league-roman-era.json: vassal_start -196, dissolve -146. antigonid-dynasty.json: -212 gain of the Atintani, Parthini and Dimale, and -205 loss at the Peace of Phoenice (C3). achaean-league.json: occupation of Acrocorinth 197-194. acarnanian-league.json: -168 Leucas (C3).
  - Fix: Add the three wars with zones. Add vassal_start aetolian-league -189 and vassal_start thessalian-league-roman-era -196 (vassal_end/gain 146). Add the 212 loss and 205 recovery of the Illyrian protectorate (vassal_end/vassal_start of the free-text Illyrian towns), the 197-194 garrisons, and Leucas 168, each with its page, or explain any you reject.
- `/ledger (new, Umbria) and /ledger/97`: BLOCKING (missing event). Umbria never enters the ledger, yet /ledger/97 enfranchises it in 90 as allied land, and the notes list umbri as a counterpart.
  - Evidence: umbri.json: -299 loss of Nequinum/Narnia to RR (C3) and -260 loss and dissolve to RR (C2, Umbri page: conquest of Umbria 'completed ... by approximately 260 BC'). Cliopatria's -301 and -291 shapes include Umbria with no RR event explaining it.
  - Fix: Add gain umbri -299 (Narnia) and vassal_start umbri (c. 266-260, allied Umbria, tint) against the umbri dossier. /ledger/97 then reads as its vassal_end.
- `/ledger/51`: The loss of all Cisalpine Gaul in November 218 names only boii. The insubres dossier records a 218 gain of Lombardy from RR at confidence 3, which RR does not mirror.
  - Evidence: insubres.json /ledger/4: -218 (11) gain roman-republic, C3. boii.json has contest_start, not gain, in 218.
  - Fix: Split it: loss boii (Emilia) and loss insubres (Lombardy), November 218. Ask the boii author to add the matching gain.
- `/ledger/21, /ledger/23 (and /ledger/19, 20, 25)`: The 277 and 272 gains name the free-text 'Kingdom of Epirus (Pyrrhus)'. The land belonged to Croton, Locri and Tarentum, which now have dossiers that dissolve to RR. kingdom-of-epirus has no RR events at all.
  - Evidence: croton.json /ledger/9 (-277 dissolve to RR, C3); taras.json /ledger/1 (-272 dissolve to RR, C3); kingdom-of-epirus.json has vassal_start taras -280.
  - Fix: Set /ledger/21's counterpart to croton (Locri as a second event if wanted) and /ledger/23's to taras, and use slug kingdom-of-epirus for the contest and the 280 loss. Ask the kingdom-of-epirus author for mirrors.
- `/ledger/142/counterpart`: Massilia's annexation (49) names greek-city-states, but massalia.json now exists and dissolves to RR. greek-city-states also books a 49 loss, so the land is counted twice.
  - Evidence: massalia.json /ledger/5 (-49 dissolve to RR, C3); greek-city-states.json /ledger/78 (-49 loss, C3).
  - Fix: Set the counterpart to massalia and ask greek-city-states to drop its 49 loss.
- `/ledger/112`: Sertorius' state is founded in Lusitania (Roman since 139) in 80, but RR has only a contest_start in 80; its first loss is in 77.
  - Evidence: sertorian-hispania.json /ledger/0: found -80 from roman-republic, C3.
  - Fix: Add loss sertorian-hispania -80 (Lusitania), or change the counterpart's found to nobody and say why.
- `/ledger/38-41, /ledger/53, /ledger/80`: Carthage mismatches: carthage.json has -252 loss of Selinous, Heraclea Minoa and Thermae (C3), -213 gain of Agrigentum from RR (C2), -201 vassal_start to RR (C2) and -149 loss of Utica (C3). RR mirrors none of them.
  - Evidence: carthage.json ledger 26, 41, 52, 55.
  - Fix: Add gain carthage -252, loss carthage -213 (Agrigentum; regained in RR's -210 gain) and gain carthage -149 (Utica). Then either add vassal_start carthage -201 (vassal_end at the 146 gain) or ask af-02 to drop Carthage's 201 vassal_start.
- `/ledger/33`: syracuse.json records a 263 loss to RR of 'the interior and north coast beyond Tauromenium' (C2). RR has only the vassal_start for Hiero's kingdom and no gain of that land.
  - Evidence: syracuse.json /ledger/16.
  - Fix: Add gain syracuse -263 for the land outside Hiero's kingdom, or ask the syracuse author to change it to vassal_start.
- `/ledger/81`: Greece in 146: RR's only gain names achaean-league. greek-city-states.json loses Thessaly, central Greece, Euboea and Epirus to RR in 146 (C3), and thessalian-league-roman-era dissolves to RR in 146.
  - Evidence: greek-city-states.json /ledger/70; thessalian-league-roman-era.json /ledger/5.
  - Fix: Say which of this land joined Macedonia in 148 and which in 146. Add gain events against the right counterparts, or ask those authors to align.
- `/wars`: The late-Republic civil wars after 45 are missing: the Liberators' civil war (43-42; Brutus and Cassius held Macedonia, Asia and Syria) and Sextus Pompeius' Sicilian revolt (42-36; the Pact of Misenum in 39 left him Sicily, Sardinia, Corsica and the Peloponnese). The Cimbrian War (113-101) and Second Mithridatic War (83-81) are also absent.
  - Evidence: By the dossier's own standard (Sertorius modelled as a rebel holding Roman land 80-72), Sextus' six-year hold on the islands is a contest. Check 10: every war in the sources appears, with empty zones only where said so.
  - Fix: Add the wars. Add contest_start/contest_end for Sicily, Sardinia and Corsica 42(40)-36 against a Sextus Pompeius counterpart (page: https://en.wikipedia.org/wiki/Sicilian_revolt). Give the Cimbrian and Second Mithridatic wars empty zones and a note.
- `/keyframe_review/2/correction`: Cliopatria's -480 shape has a bbox east edge of 12.4517 E, west of Rome itself (capital at 12.48 E, 41.89 N), so the shape does not contain the capital.
  - Evidence: shapes.csv roman-republic_-480 bbox 11.972,41.7816,12.4517,42.1712; identity.capitals[0] lon 12.48.
  - Fix: Add a union with {"place":"Roma","km":10} to the correction and a line in the note.
- `/ledger/13, 16, 22, 27, 30, 64, 94, 95, 98, 103`: Modelling conflict with the Italic dossiers. RR keeps the Samnites (290-91), Lucanians (272-91), Etruscans (264-90), Picentes (299-268) and Insubres (197-89) as allies (vassal tint). Those dossiers instead dissolve at conquest (samnites 290, lucanians 272, etruscans 264, insubres 197) and have no vassal pairs.
  - Evidence: Cross-check matrix; each counterpart's dissolve event.
  - Fix: Not a fault of RR's reading, which is defensible (socii). The eu-03 authors should agree one model: either the counterpart dossiers run to 91/89 as vassals, or RR turns these vassal_starts into gains.

## Spot checks

- `/ledger/80` (https://en.wikipedia.org/wiki/Africa_(Roman_province)): confirmed: province 146, capital Utica. Region overstated (extent sentence undated; the rest left to Massinissa); confidence lowered to 2, region fix pending
- `/ledger/88` (https://en.wikipedia.org/wiki/Gallia_Narbonensis): confirmed: 'The area became a Roman province in 121 BC'; Bituitus at the Isère in the 125-121 war; Narbo 118; bounds as quoted
- `/ledger/114` (https://en.wikipedia.org/wiki/Bithynia_and_Pontus): confirmed: 74 BC bequest and annexation; the quote was a paraphrase, now corrected
- `/ledger/129` (https://en.wikipedia.org/wiki/Roman_Syria): confirmed: 'Syria was annexed to the Roman Republic in 64 BC'; Antiochus XIII executed, Philip II deposed, Scaurus governor
- `/ledger/134 and /ledger/143` (https://en.wikipedia.org/wiki/Roman_Cyprus): confirmed: lex Clodia 58, Cato, added to Cilicia, Ptolemy's suicide; Caesar returned Cyprus to the Ptolemies (47). The 'reaffirmed in 40' detail was wrong (Donations of Alexandria) and is fixed. The page also has Cyprus Roman again from 31, which the dossier omits (see the keyframe 50 finding)
- `/ledger/147 and /ledger/149` (https://en.wikipedia.org/wiki/Roman%E2%80%93Parthian_Wars): 147 confirmed (40 BC, 'swiftly overran Syria', the coast except Tyre). 149: 38 BC is on the page as Pacorus' defeat, but the Roman recovery is undated and the quoted 'held Syria for roughly two years' is not on the page; note replaced and confidence lowered to 2

## Area
- Infobox 'Area: 326 BC: 10,000 km2; 50 BC: 1,950,000 km2'. Cliopatria -326 is 10,064.6 km2 (ratio 1.01) and -50 is 2,216,249 km2 (ratio 1.14). No factor of two, so no acknowledgement is needed. The dossier quotes no infobox area.

## Thin (gap-filler list)

- `/ledger/28`: Messapii, Sallentini and Brundisium c. 266: no page dates it (confidence 1). Try https://en.wikipedia.org/wiki/Messapians
- `/ledger/35`: End of the Mamertine alliance in 257 is Cliopatria's year (confidence 1); when did Messana pass into Roman Sicily?. Try https://en.wikipedia.org/wiki/Messina
- `/ledger/42`: Veneti amicitia 238 (confidence 1). Try https://en.wikipedia.org/wiki/Cenomani
- `/ledger/90`: The part of Cilicia made a province in 103/102 (confidence 1). Try https://en.wikipedia.org/wiki/Marcus_Antonius_Orator
- `/ledger/133`: Galatia as a client in 63 (confidence 1); I confirmed the Bithynia and Pontus page says nothing about Galatia or Deiotarus in 63. Try https://en.wikipedia.org/wiki/Deiotarus
- `/ledger (none)`: Balearic conquest of 123 BC: no event at all, though Cliopatria's -126/-110 shapes probably include the islands. Try https://en.wikipedia.org/wiki/Quintus_Caecilius_Metellus_Balearicus
- `/ledger (none)`: Ligurian wars 238-155 (Liguria and the Apuan Alps): no event. Try https://en.wikipedia.org/wiki/Ligures
- `/ledger (none)`: Pompey's eastern settlement 64-62: Commagene, Osroene, the Nabataeans, Ituraea and Deiotarus as clients. Try https://en.wikipedia.org/wiki/Pompey
- `/ledger/34-39`: Dates of the Sicilian towns between 261 and 241 beyond Agrigentum, Panormus and Lilybaeum. Try https://en.wikipedia.org/wiki/Sicilia_(Roman_province)
- `/ledger/149`: Year Syria was recovered from the Parthians (39 at the Amanus Pass, or 38 at Gindarus). Try https://en.wikipedia.org/wiki/Publius_Ventidius_Bassus

## Cross-dossier matrix (mismatches and missing mirrors only; the full list is in reviews/eu-03-b.json)

- missing: roman-republic -299 vassal_start -> picentes; mirror none. picentes dossier has no vassal_start in 299 (its first Roman event is the 269 contest_start); add it there or drop the RR vassal_start
- mismatch: roman-republic -290 vassal_start -> samnites; mirror samnites -291 loss. modelling conflict: samnites dossier dissolves in 290 (and has a 291 Venusia loss), RR keeps Samnium as allied (vassal) 290-91; one side must change
- mismatch: roman-republic -272 vassal_start -> lucanians; mirror lucanians -272 loss. modelling conflict: lucanians dossier records loss + dissolve in 272, RR records vassal_start 272 (vassal_end 91)
- mismatch: roman-republic -268 vassal_end -> picentes; mirror picentes -269 contest_start. picentes dossier has loss + dissolve 268 (matched by RR gain 268) but no vassal_start/vassal_end; RR's vassal pair 299-268 has no mirror
- mismatch: roman-republic -264 vassal_start -> etruscans; mirror etruscans -265 contest_start. modelling conflict: etruscans dossier dissolves in 264 ('allies of Rome from 264 (tint)' in its text) without a vassal_start; RR vassal_start 264, vassal_end 90
- missing: roman-republic -264 vassal_start -> mamertines; mirror none. mamertines dossier has no vassal_start; it only dissolves to RR in 257 (C1)
- mismatch: roman-republic -263 vassal_start -> syracuse; mirror syracuse -263 loss. syracuse dossier records a 263 loss to RR of 'the interior and north coast beyond Tauromenium' and no vassal_start; RR records only the vassal_start for Hiero's retained kingdom and no gain of the land beyond
- mismatch: roman-republic -257 vassal_end -> mamertines; mirror mamertines -257 dissolve. mamertines dossier dissolves to RR in 257 (C1); RR has vassal_end and no gain of Messana; both C1
- missing: roman-republic -238 vassal_start -> adriatic-veneti; mirror none. adriatic-veneti dossier has no vassal_start in 238 (its Roman events are the 181 Aquileia loss and the 89 dissolve); RR event C1
- mismatch: roman-republic -225 vassal_start -> boii; mirror boii -225 contest_start. boii dossier has contest_start 225, not vassal_start
- mismatch: roman-republic -218 gain -> carthage; mirror carthage -218 contest_start. carthage dossier has contest_start 218 and a C1 gain from nobody of Catalonia in 218, no loss to RR of the Emporion-Ebro coast
- mismatch: roman-republic -218 loss -> boii; mirror boii -218 contest_start. RR names only boii for the whole of Cisalpine Gaul; the insubres dossier records a 218 Nov gain of Lombardy from RR (C3) that has no RR mirror, and boii records contest_start, not gain
- mismatch: roman-republic -218 vassal_end -> boii; mirror boii -218 contest_start. boii dossier has no vassal pair
- mismatch: roman-republic -216 loss -> carthage; mirror carthage -215 contest_end. carthage dossier records gain of Agrigentum from RR in 213, nothing for Capua/Samnium 216
- mismatch: roman-republic -215 vassal_end -> syracuse; mirror syracuse -214 contest_start. syracuse dossier has a 215 rename and 214 contest_start; no vassal_end
- mismatch: roman-republic -203 gain -> carthage; mirror carthage -204 contest_start. carthage dossier has no 203 loss of southern Italy (it ends the Italian theatre with contest_end 203)
- missing: roman-republic -201 vassal_start -> kingdom-of-numidia; mirror none. kingdom-of-numidia dossier (found 202) has no vassal_start to RR; RR vassal 201-46
- mismatch: roman-republic -197 vassal_start -> insubres; mirror insubres -197 contest_end. modelling conflict: insubres dossier dissolves in 197, RR vassal_start 197 (vassal_end 89)
- missing: roman-republic -91 vassal_end -> samnites; mirror none. samnites dossier ended in 290; no vassal pair there
- missing: roman-republic -91 vassal_end -> lucanians; mirror none. lucanians dossier ended in 272; no vassal pair there
- missing: roman-republic -90 vassal_end -> etruscans; mirror none. etruscans dossier ended in 264; no vassal pair there
- missing: roman-republic -89 vassal_end -> insubres; mirror none. insubres dossier ended in 197; no vassal pair there
- mismatch: roman-republic -89 vassal_end -> adriatic-veneti; mirror adriatic-veneti -89 dissolve. adriatic-veneti dossier dissolves to RR in 89 (matches the RR 89 gain from nobody of Transpadane Gaul in substance); no vassal pair there
- mismatch: roman-republic -46 vassal_end -> kingdom-of-numidia; mirror kingdom-of-numidia -46 loss. kingdom-of-numidia has loss + dissolve 46 (matched by RR gain) but no vassal pair
- missing: roman-republic -31 vassal_start -> thracian-kingdom; mirror none. thracian-kingdom dossier has only a dynastic rename in 31, no vassal_start to RR
- missing: mauretania -33 vassal_start -> roman-republic; mirror none. Mauretania page: 'Upon his own death in 33 BC, Bocchus II bequeathed his entire kingdom to Octavian'; RR has no vassal_start mauretania (C3 on the counterpart side)
- missing: dalmatae -76 loss -> roman-republic; mirror none. Salona passes to Rome (C3, Dalmatae page); no RR gain
- missing: dalmatae -33 dissolve -> roman-republic; mirror none. Octavian ends Dalmatian independence, Roman Illyricum (C3); RR lists the Dalmatian coast only as a gap
- missing: cimmerian-bosporus -48 gain -> roman-republic; mirror none. Pharnaces II seizes Colchis, Lesser Armenia and Pontus from Rome in 48; RR has no loss
- missing: cimmerian-bosporus -47 loss -> roman-republic; mirror none. Zela (47, C3): Rome recovers Pontus; RR has no gain
- missing: aetolian-league -189 loss -> roman-republic; mirror none. Ambracia taken by Fulvius Nobilior 189 (C3); RR has no gain
- missing: aetolian-league -189 vassal_start -> roman-republic; mirror none. 'Aetolia was reduced to a Roman client state' (Roman-Seleucid war page, C3); RR has no vassal_start
- missing: thessalian-league-roman-era -196 vassal_start -> roman-republic; mirror none. Thessaly under Roman protection from 196 (C2); RR has no vassal_start
- missing: thessalian-league-roman-era -146 dissolve -> roman-republic; mirror none. Thessaly into the province of Macedonia; RR has no gain
- missing: achaean-league -197 occupation_start -> roman-republic; mirror none. Roman garrison in Acrocorinth 197-194 (C2); RR has none
- missing: antigonid-dynasty -212 gain -> roman-republic; mirror none. Philip V takes the Atintani, Parthini and Dimale from Roman protection (C2); RR has no loss or vassal_end
- missing: antigonid-dynasty -205 loss -> roman-republic; mirror none. Peace of Phoenice (C3): Parthini, Dimallum etc. to Rome; RR has no gain or vassal_start
- missing: antigonid-dynasty -196 loss -> roman-republic; mirror none. Demetrias, Chalcis and Corinth garrisoned by Rome to 194 (C2); RR has no occupation
- mismatch: antigonid-dynasty -168 dissolve -> roman-republic; mirror none. RR has contest_end 168 (now counterpart antigonid-dynasty) and vassal_start macedonian-republics 167; no RR event takes the Antigonid land in 168 except via the merides
- missing: acarnanian-league -168 loss -> roman-republic; mirror none. Leucas to Rome 168 (C3); RR has no gain
- mismatch: kingdom-of-epirus -167 dissolve -> roman-republic; mirror none. RR's 167 gain names molossians; the Epirote state dissolving to RR in 167 (C3) has no RR mirror
- mismatch: croton -277 dissolve -> roman-republic; mirror none. RR's 277 gain of Croton and Locri names the free-text 'Kingdom of Epirus (Pyrrhus)'; croton.json dissolves to RR (C3)
- mismatch: taras -272 dissolve -> roman-republic; mirror none. RR's 272 gain of Tarentum names 'Kingdom of Epirus (Pyrrhus)'; taras.json dissolves to RR (C3); kingdom-of-epirus has no RR events at all
- missing: umbri -299 loss -> roman-republic; mirror none. Nequinum/Narnia to Rome 299 (C3); RR has no Umbrian event
- missing: umbri -260 loss -> roman-republic; mirror none. conquest of Umbria completed c. 260 (C2); RR has no Umbrian event
- missing: volsci -304 loss -> roman-republic; mirror none. the Volscian country (Antium, Pomptine plain, Privernum, Liris) lost by 304 (C2); RR has only the 377 gain
- missing: samnites -338 loss -> roman-republic; mirror none. Campanian plain of Capua, Pompeii, Cumae (C2); RR's 338 gain names latin-league
- missing: samnites -291 loss -> roman-republic; mirror none. Venusia 291 (C2); RR's 290 events are vassal_start + contest_end
- missing: etruscans -383 loss -> roman-republic; mirror none. Sutrium and Nepet (C2); RR has no gain
- missing: etruscans -300 loss -> roman-republic; mirror none. Pyrgi (C2); RR has no gain
- missing: etruscans -273 loss -> roman-republic; mirror none. Caere and its coast (C2); RR has no gain
- mismatch: greek-city-states -146 loss -> roman-republic; mirror none. mainland Greece outside the Peloponnese (Thessaly, central Greece, Euboea, Epirus) to RR (C3); RR's only 146 Greek gain names achaean-league
- missing: greek-city-states -63 loss -> roman-republic; mirror none. Greek cities of the Anatolian coast (C1); RR none
- mismatch: massalia -49 dissolve -> roman-republic; mirror none. RR's 49 Sept gain of Massilia names greek-city-states (which also records a 49 loss); massalia.json now exists and dissolves to RR (C3): one of the two counterpart dossiers double-counts
- missing: sertorian-hispania -80 found -> roman-republic; mirror none. Sertorius' state founded in Lusitania (Roman since 139) in 80; RR has only contest_start 80 and the first loss in 77
- missing: syracuse -263 loss -> roman-republic; mirror none. see RR /ledger/33
- missing: carthage -252 loss -> roman-republic; mirror none. Selinous, Heraclea Minoa and Thermae 252 (C3); RR has gains 254 and 241 only
- missing: carthage -213 gain -> roman-republic; mirror none. Agrigentum retaken by Carthage 213 (C2); RR has no loss
- missing: carthage -201 vassal_start -> roman-republic; mirror none. Carthage's territory under the 201 treaty (C2); RR has no vassal_start carthage
- missing: carthage -149 loss -> roman-republic; mirror none. Utica (C3); RR includes Utica only in the 146 gain
- mismatch: illyrian-kingdom -229 loss -> roman-republic; mirror none. Corcyra to Rome 229 (C3); RR models the Greek coast as a 228 vassal_start of free-text 'Greek cities of the Illyrian coast'
- mismatch: illyrian-kingdom -168 dissolve -> roman-republic; mirror none. illyrian-kingdom loses its last lands and dissolves to RR (C3); RR has vassal_start of free-text 'Illyria (the three cantons of Gentius' kingdom)'
- missing: rhodes -39 dissolve -> roman-republic; mirror none. C1 on the counterpart side; RR none; low priority

## Problems

- No page failed to load. WebFetch summaries paraphrase, so a quote the summarizer could not find (the Parthian 'roughly two years') may in principle sit in an unread part of the page; two targeted re-reads found it absent.
- Many cross-check mismatches come from counterpart dossiers written after roman-republic (2026-10-18 07:19): kingdom-of-epirus, croton, taras, massalia, macedonian-republics, dalmatae, umbri, thessalian-league-roman-era, cimmerian-bosporus, aetolian-league. The eu-03-b author kept the dossier unchanged and did not integrate them.
- Counterparts whose groups have not run yet (no dossier on 2026-10-19): kingdom-of-pontus, kingdom-of-armenia, cyrenaica, judea, ptolemaic-kingdom, galatia, parthian-empire, kingdom-of-pergamon, kingdom-of-cappadocia, kingdom-of-bithynia, seleucid-empire, roman-empire; Context polities kingdom-of-commagene, kingdom-of-osroene, nabataeans and kingdom-of-armenia also have no dossier yet. Their events are recorded as exceptions.
- Reviewer edits to history/polities/roman-republic.json (validated after each, 0 errors, 4 vassal_start-without-end warnings unchanged): counterpart slugs antigonid-macedonia -> antigonid-dynasty and the merides -> macedonian-republics; /ledger/80 and /ledger/149 confidence 3 -> 2; note text of /ledger/114, /ledger/143 and /ledger/149 corrected to the pages' words.
