# Review of batch eu-01-x (reviewer, 2026-10-18)

Adversarial review of the 15 additions dossiers (states Cliopatria lacks). Validator: 0 errors in all 15; warnings are gazetteer names only. Spot checks were made with WebFetch on the pages the dossiers cite. Fixes marked APPLIED were made by the reviewer in place and re-validated.

## Verdicts

### athens: thin
- [APPLIED] `/ledger/3`: The Samos cleruchy gain was a bridged -350 at confidence 1, but a page in sources dates it to 365 BC. Evidence: Lamian War page: Athens 'had to surrender the island of Samos, colonised by Athenian clerurchs since 365 BC'. Fix: Year -365, source Lamian_War, confidence 2; keyframe 0 to -366, keyframe 1 shape_id athens_-365 from -365, note updated.
- [to do] `/ledger/2`: A 'merge' event that adds no land: region Attica is already the state's since -700, and the counterpart 'Attic local communities (demes)' is not a polity. Evidence: Classical Athens infobox '508 BC: Cleisthenes establishes Athenian democracy' is a constitutional change; the found event at -700 already draws Attica. Fix: Make it a rename (regime change, no region/counterpart) or drop it; keep the Attica page quote in notes.
- [to do] `/ledger/5`: dissolve -322 with macedonian-empire as counterpart and successor, while macedonian-empire records only a vassal_start of greek-city-states at -322 (garrison at Munychia, hegemony). Evidence: macedonian-empire /ledger/30: '-322 vassal_start greek-city-states: 18 September 322: the garrison enters Munychia'. A successor macedonian-empire implies annexation of Attica, the neighbour draws a client tint. Fix: Keep the end but name the successor relation consistently (successor land as Macedonian client, or orchestrator sets one convention for athens, corinth and thessalian-league).
- [to do] `/ledger/1`: Counterpart 'Megara' has no dossier and is not in counterparts_needing_dossiers. Evidence: Schema allows a source name, but the brief's exception needs the state listed. Fix: List Megara under counterparts_needing_dossiers (or route to eu-01 gap-fill).
- [thin] `/ledger/1`: Salamis taken from Megara: century only (6th c.), confidence 1; a dated war with Megara (Solon/Peisistratus) is needed. Try: https://en.wikipedia.org/wiki/Salamis_Island
- [thin] `/keyframe_review`: Cleruchies and overseas holdings never drawn: Chalcis (506), Lemnos and Imbros (Miltiades), Thracian Chersonese, Euboea after 446, Aegina (431), Oropos before 322, and their loss in 404. Try: https://en.wikipedia.org/wiki/Oropos
- [thin] `/ledger/4`: Oropos is lost in 322 but its holding is never dated (it is inside the gazetteer's Attica, so the shape works, but the gain/loss history is missing). Try: https://en.wikipedia.org/wiki/Oropos
- Spot checks: /ledger/3 mis-dated (page: 'colonised by Athenian clerurchs since 365 BC'; fixed); /ledger/4 confirmed; /ledger/5 confirmed (Munychia taken 18 September 322; 21,000 to 9,000 citizens); /ledger/1 confirmed (6th century only); /ledger/2 confirmed (infobox 508 BC)
- Area: No infobox area on Classical Athens or Attica; no Cliopatria row (new keyframes). Drawn Attica 3,288 km2 per the gazetteer.

### messene: thin
- [thin] `/ledger/2`: Nabis's withdrawal from Messene is bridged to -200 (confidence 1); the Philopoemen page puts Philopoemen's relief right after the 201 capture. Try: https://en.wikipedia.org/wiki/Nabis
- [thin] `/ledger/3`: Entry into the Achaean League and the end year -191 are bridged (Achaean League page: 'Messene ... joined by conquest', no date). Try: https://en.wikipedia.org/wiki/Diophanes_of_Megalopolis
- [thin] `/keyframe_review/0`: The polis's territory (all of Messenia?), Philip II's border grants of 338/337 and the Dentheliatis are undated; the whole region is a reading. Try: https://en.wikipedia.org/wiki/Messenia_(ancient_region)
- Spot checks: /ledger/0 confirmed (369, Epaminondas); /ledger/1 confirmed ('In 201 BC, Nabis invaded and captured Messene'); /ledger/2 confirmed as undated (Philopoemen intervened; no year), confidence 1 is honest; /ledger/3 confirmed as undated ('joined by conquest'), confidence 1 is honest
- Area: No infobox area; Messenia drawn as the region (modern regional unit 2,991 km2 per the author).

### kingdom-of-epirus: thin
- [to do] `/ledger/19`: Loss of Ambracia to the Aetolians bridged to -231, two years after the aetolian-league dossier's -233 gain; the page puts the seizure in the sentence right after Deidamia's murder 'In 233 BC'. Evidence: Epirus (ancient state): 'In 233 BC, the last surviving member of the Aeacid royal house, Deidamia, was murdered. Her death brought the Epirote royal family to an abrupt extinction and a federal republic was set up, [...] the Aetolians seized Ambracia'. aetolian-league /ledger/6 is -233 gain cp epirus. Fix: Move the loss to -233 (keyframe 7 to -234, keyframe 8 kingdom-of-epirus_-233 from -233) or have aetolian-league move to -231; one year for both.
- [to do] `/identity/capitals/1`: Capital Ambracia runs to -225 although Ambracia is lost at -231 (the capital lies outside the drawn shape for six years). Evidence: Infobox 'Ambracia (295-224 BC)' against the text 'the Aetolians seized Ambracia' after 233 and 'The new Epirote capital was therefore established at Phoenice'. Fix: End Ambracia at the year of the Aetolian seizure and start Phoenice then (text: after 233), noting the infobox's 224; move ledger/20 to match.
- [to do] `/keyframe_review/0/note`: The note says 'Cliopatria has no Epirus row before the Despotate of Epirus (1206)', but polities.csv has 'Molossians' (-170..-165, 1 shape, 4,708 km2, Wikipedia Molossians), which overlaps this dossier's last years; the overlap is not flagged. Evidence: polities.csv row molossians,-170,-165; roman-republic /ledger/73 '-167 gain cp molossians'. Fix: Say in notes how -170..-167 relates to the Molossians row (the Molossian secession to Perseus in 170?) and tell the orchestrator which dossier draws Molossia in -170..-165.
- [to do] `/ledger/5`: The -331 loss of all three Italian towns names only 'lucanians', though Terina was taken from the Bruttii and Sipontum from other Italic tribes (ledger/3, ledger/4). Evidence: Alexander I of Epirus page as quoted in ledger/2-4. Fix: Split the loss by counterpart (lucanians: Heraclea; Bruttii: Terina; Italic tribes: Sipontum), or say in the note that all three fall to the Lucanian-Bruttian coalition.
- [to do] `/identity/slug`: Neighbour dossiers call this state 'epirus' (antigonid-dynasty /ledger/13,18,19; kingdom-of-lysimachus /ledger/15-17; aetolian-league /ledger/6) or 'Kingdom of Epirus (Pyrrhus)' (roman-republic, syracuse, croton's neighbours): the mirrors exist but under another counterpart string. Evidence: xcheck of the neighbours' ledgers. Fix: Orchestrator: map counterpart 'epirus' and 'Kingdom of Epirus (Pyrrhus)' to kingdom-of-epirus (no change needed in this dossier).
- [thin] `/ledger/9`: How Pyrrhus came by Ambracia, Acarnania, Amphilochia and Parauaea (c. 294, from Alexander V) is not on the pages; the gain is confidence 1 with an unnamed counterpart. Try: https://en.wikipedia.org/wiki/Alexander_V_of_Macedon
- [thin] `/ledger/2`: Alexander I's Italian captures (Heraclea, Terina, Sipontum) and their loss in 331 are undated within 334-331 (confidence 1). Try: https://en.wikipedia.org/wiki/Battle_of_Pandosia
- [thin] `/ledger/16`: Loss of Macedon in 272 (Antigonus's recovery after Pyrrhus's death at Argos) and the end of the Tarentine dominion are bridged (confidence 1). Try: https://en.wikipedia.org/wiki/Antigonus_II_Gonatas
- [thin] `/ledger/6`: End of the Macedonian client relation at -331 is a bridge (confidence 1). Try: https://en.wikipedia.org/wiki/Alexander_I_of_Epirus
- [thin] `/keyframe_review/8`: Epirote League 231-167: no territorial event (Illyrian raids, Phoenice 230, First/Third Macedonian War splits, Molossian secession 170). Try: https://en.wikipedia.org/wiki/Epirote_League
- Spot checks: /ledger/7 confirmed (infobox 'Epirote tribes established united political entity: 330 BC'); /ledger/11 confirmed ('In 284 BC, he was driven out of Macedon by Lysimachus'); /ledger/13 confirmed ('In 277 BC, Pyrrhus captured the Carthaginian fortress in Eryx'); /ledger/21 confirmed ('Molossia fell to Rome in 167 BC'); /ledger/10 confirmed (288, co-ruled Macedon with Lysimachus); /ledger/19 undated on the page; follows the 233 murder (see fix)
- Area: Infobox has no area; no Cliopatria row for these years except Molossians (-170..-165, 4,708 km2), not compared by the author.

### sybaris: pass
- [thin] `/ledger/1`: The dominion over '4 tribes and 25 cities' is undated (bridged -550, confidence 1); the only dated expansion is Siris 'in the middle of the sixth century BC'. Try: https://en.wikipedia.org/wiki/Siris_(Magna_Graecia)
- Spot checks: /ledger/0 confirmed ('founded around 720 BC'); /ledger/2 confirmed ('destroyed in about 510 BC by its neighbour Kroton'); /ledger/3 confirmed; the page also says Sybaris 'was not completely destroyed' and became a dependent ally of Kroton, which the author flags in notes; /ledger/1 confirmed as undated ('ruled over 4 tribes and 25 cities')
- Area: Infobox 'Approximately 500 ha' is the city, not the territory; the 30 km disc is a reading and the keyframe note says so.

### croton: fail
- [BLOCKING] `/keyframe_review/2`: Between keyframe 1 (-510..-380, Crotene + Cosenza) and keyframe 2 (-379, Crotene only) the province of Cosenza (about 23 of 28 gazetteer cells, a fall of about 5x) disappears with no loss event: ledger/2 is an occupation of Crotene only. Evidence: Rule 4 of the reviewer brief; the K2 note itself says 'the confederation is not recorded on the page after 460'. Crotone page: the confederation is shown by 'coins minted between 480 and 460 BC'. Sybaris page (in sources): 'In 444/443 BC the Athenians and other new colonists then turned the city into a new foundation called Thurii'. Fix: Add a loss of the Sybarite land (Cosenza) at -444 to 'thurii' (already listed under counterparts_needing_dossiers), confidence 2, source Sybaris; end keyframe 1 at -445 and add keyframe croton_-444 (-444..-380, Crotene).
- [to do] `/ledger/5`: Syracusan occupation ends at -277 (confidence 1), twelve years after Agathocles's death (289), and the syracuse dossier has no Croton occupation at all. Evidence: syracuse /ledger/10: '289 BC: Agathocles dies'; Crotone page dates no end of the occupation and puts the Bruttii in the town 'with the exception of the citadel'. Fix: Bridge the end to -289 (Agathocles's death) or name the Bruttii as the occupier from then; keep confidence 1.
- [thin] `/ledger/5`: End of the Syracusan and Bruttian occupations is undated. Try: https://en.wikipedia.org/wiki/Bruttii
- [thin] `/keyframe_review/1`: The confederation's extent and end (Thurii 444, Italiote League) are not dated on the pages. Try: https://en.wikipedia.org/wiki/Italiote_League
- Spot checks: /ledger/2 confirmed ('captured Croton in 379 BC and held it for twelve years'); /ledger/4 confirmed ('In 295 BC, Croton fell to another Syracusan tyrant'); /ledger/6 confirmed ('What was left of its population submitted to Rome in 277 BC'); /ledger/1 confirmed (confederation of the 25 city-states, coins 480-460)
- Area: No territory area on the page (city 617 ha, comune 179.8 km2); province of Crotone 1,264 km2 is a reading, acknowledged.

### taras: thin
- [to do] `/ledger`: No vassal events for the Epirote dominion although kingdom-of-epirus (same batch) has vassal_start -280 and vassal_end -272 with counterpart taras, and roman-republic /ledger/23 takes Tarentum from the Epirote garrison in 272. Evidence: Pyrrhus of Epirus page: 'Only the city of Tarentum remained under the dominion of the Epirotes'. Fix: Add vassal_start -280 and vassal_end -272, counterpart kingdom-of-epirus, region Taranto disc, source Pyrrhus_of_Epirus (add to sources), confidence 2.
- [thin] `/ledger`: 434 years with two events: the 473 defeat by the Iapygians, Heraclea (433), the Italiote League hegemony and Alexander of Epirus's alliance (334) are missing. Try: https://en.wikipedia.org/wiki/Magna_Graecia
- Spot checks: /ledger/0 confirmed ('founded in 706 BC by Dorian Greek immigrants hailing from Sparta'); /ledger/1 confirmed ('surrendered to Rome after the death of Pyrrhus in Peloponnese in 272 BC')
- Area: Infobox 249.86 km2 is the modern comune; the 40 km disc (about 5,000 km2) is a reading of the chora and the keyframe note says so.

### chalcidian-league: fail
- [APPLIED] `/keyframe_review/1/to`: Keyframe 1 ended at -383, the year keyframe 2 starts (one-year overlap). Evidence: Every other boundary in the file is to = next from - 1. Fix: to: -384.
- [BLOCKING] `/keyframe_review/3`: Between keyframe 2 (-383..-379, Chalcidice + Kentriki Makedonia) and keyframe 3 (-378, Chalcidice) the whole of Central Macedonia west of the Chalcidice is dropped with no loss event: ledger/4 is a contest_end and ledger/5 a vassal_start of the Chalcidice only. Evidence: Rule 4; Olynthus page: Olynthus 'consented to dissolve the confederacy in 379'; Chalcidian League page: 'in 379 BCE the cities of the former League became autonomous and subject allies of Sparta'. Fix: Add a loss at -379 of the land outside the Chalcidice (counterpart greek-city-states for the freed cities, macedonian-empire for Pella), confidence 3, source Olynthus.
- [BLOCKING] `/keyframe_review/4`: Keyframe 4 (-375..-349) re-adds the Pella disc with no gain event and no page support. Evidence: Chalcidian League page: in 393/2 Amyntas 'temporarily transferred some territory to Olynthos' and it was returned when he regained power; the Olynthus page dates possession of Pella only 'by 382 BCE'. Nothing places Pella in the League after 375; 357/356 brought Potidaea (macedonian-empire /ledger/4), not Pella. Fix: Drop the Pella disc from keyframe 4 (Chalcidice only), or add a sourced gain; also add the return of the 393/2 land when Amyntas regained power (about -391, confidence 1).
- [to do] `/keyframe_review/2/correction`: Kentriki Makedonia already contains the Chalcidice and also Pieria and Imathia (Aigai), the Macedonian heartland: about 19,000 km2 for 'most of the Greek cities west of the Strymon'. Evidence: Olynthus page: 'by 382 BCE it had absorbed most of the Greek cities west of the Strymon, and had even got possession of Pella'. Fix: Narrow the correction to the Chalcidice, the Thermaic coast and a Pella disc, or lower the keyframe note to say the admin-1 overstates; keep confidence 1 on ledger/2.
- [thin] `/ledger/2`: The 383/382 expansion is a reading (confidence 1). Try: https://en.wikipedia.org/wiki/Olynthian_War
- Spot checks: /ledger/3 confirmed (Sparta's expedition 'in 382 BCE'); /ledger/4 confirmed (dissolution 'in 379'); /ledger/5 confirmed ('in 379 BCE ... subject allies of Sparta'); /ledger/6 confirmed ('Already in 375 BCE the Chalcidians threw off Spartan control'); /ledger/7 confirmed ('he besieged Olynthus in 348 BCE'); /ledger/1 confirmed but the page says the transfer was temporary and returned
- Area: No area on either page (Olynthus city 60 ha); Chalcidice is a reading, acknowledged.

### massalia: pass
- [thin] `/ledger`: The strip given up for the Via Domitia in 121 ('Massalia gave up a strip of land through its territory', History of Marseille) is not a ledger event; Tauroentium (early 3rd c.) is not drawn. Try: https://en.wikipedia.org/wiki/History_of_Marseille
- Spot checks: /ledger/0 confirmed ('Settled by Ionians from Phocaea c. 600 BC'); /ledger/5 confirmed ('Massalia's fleet was defeated and the city fell by September', 49); /ledger/2 confirmed ('Olbia (c. 325)'); /ledger/3 confirmed ('Antipolis and Nikaia (c. mid-3rd c.)'); /ledger/4 partly: History of Marseille says it 'lost its trading empire'; Massalia page 'lost most of its inland territory'; confidence 2 is fair
- Area: No area; city 'about fifty hectares'; the 25 km disc is a reading, acknowledged.

### kingdom-of-paeonia: fix
- [APPLIED] `/ledger/6`: End of the Celtic occupation was bridged to -279 (confidence 1); the page's infobox dates Leon's restoration c. 278. Evidence: Paeonia (kingdom) infobox: 'Leon reestablishes Paeonia after the Celtic invasion: c. 278 BC'. Fix: Year -278, confidence 2, note quotes the infobox (now matches keyframe 4 from -278).
- [to do] `/ledger/9`: dissolve -227 hands the whole kingdom to antigonid-dynasty, but the page says only the south fell in 227 and the rest in 217. Evidence: 'In 227 BC, Antigonus Doson conquered the southern part of Paeonia.' 'In 217 BC, Philip V of Macedon incorporated into his empire Dassaretia and Paeonia by capturing Bylazora and the rest.' Fix: Either extend the life to -217 (rump kingdom, end with the 217 incorporation) or keep -227 and lower the dissolve to confidence 1 with the 217 sentence in the note.
- [to do] `/identity/capitals/0`: Capitals stop at -231 while the life runs to -227 (Bylazora lost 230; the move to Stobi is undated). Evidence: 'The capital was Bylazora, later moved to Stobi.' Fix: Add Stobi -230..-227 with a note that the page gives no year, or extend Bylazora's note to say the capital is unknown for -230..-227.
- [to do] `/ledger/4`: occupation_end -280 with counterpart kingdom-of-lysimachus falls after that state's end (-281, Corupedium, February 281). Evidence: kingdom-of-lysimachus identity end -281, /ledger/20 dissolve -281. Fix: Bridge the end of Lysimachus's hold to -281 (confidence 1).
- [thin] `/ledger/0`: Start -479 is a bridge ('At some point after the Greco-Persian Wars, the Paeonian princedoms coalesced into a kingdom'); the first dated king is Agis (d. 359/358). Try: https://en.wikipedia.org/wiki/Agis_of_Paeonia
- [thin] `/ledger/4`: End of Lysimachus's control is bridged (confidence 1). Try: https://en.wikipedia.org/wiki/Lysimachus
- Spot checks: /ledger/1 confirmed (infobox 356; the page also has Philip's 358 campaign and oath, which macedonian-empire uses); /ledger/3 confirmed ('In 285/4 BC, Lysimachus took control of Paeonia'); /ledger/7 confirmed ('In 230 BC, the Dardani under Longarus captured Bylazora'); /ledger/8 confirmed ('In 227 BC, Antigonus Doson conquered the southern part of Paeonia'); /ledger/6 mis-dated (infobox c. 278; fixed)
- Area: No area; 'roughly corresponded to present-day North Macedonia' (25,713 km2) plus Blagoevgrad is a reading, acknowledged.

### kingdom-of-dardania: pass
- [thin] `/ledger/0`: Start -400 is a bridge for the infobox 'Founded: 4th century BC' (confidence 1); 372 years carry four events (Bato, Monunius, the Roman wars of the 1st century are not territorial on the pages). Try: https://en.wikipedia.org/wiki/Dardani
- Spot checks: /ledger/1 confirmed ('In 230, the Dardani under Longarus captured the strategic city of Bylazora'); /ledger/2 confirmed ('he managed to capture Bylazora from them in 217 BCE'); /ledger/3 confirmed ('officially annexed the kingdom in 28 BC'; the Dardani page has 39 or 29/28); /ledger/0 confirmed as a century only
- Area: No area on the pages; Kosovo plus Kumanovo and Skopje is a reading, acknowledged.

### kingdom-of-pylos: pass
- Spot checks: /ledger/0 confirmed ('The Mycenaean state of Pylos (1600-1200 BC) covered an area of 2,000 km2'); /ledger/1 confirmed ('destroyed by fire around 1180 BC')
- Area: Page area 2,000 km2 (body text, no infobox); drawn 25 km disc 1,963 km2; no Cliopatria shape.

### kingdom-of-mycenae: pass
- [thin] `/ledger/1`: Incorporation of Tiryns and Nauplion is undated (bridged -1350 from the population peak, confidence 1). Try: https://en.wikipedia.org/wiki/Tiryns
- Spot checks: /ledger/0 confirmed ('major power during LHI (c. 1550 - c. 1450 BC)'); /ledger/1 confirmed as undated ('Its territory would have also included adjacent centers, including Tiryns and Nauplion'); /ledger/2 confirmed ('destruction of Mycenae itself c. 1150 BC')
- Area: Page: 'two to three times the size of the other palatial states' (Pylos 2,000 km2, so 4,000-6,000); drawn 40 km disc 5,027 km2.

### thessalian-league: pass
- Spot checks: /ledger/0 confirmed ('By 374 BCE ... united ... by Jason of Pherae'); /ledger/1 confirmed (tyrants of Pherae defeated 'around 353 BCE', Philip archon for life; the League itself continues to 146, which the notes say)
- Area: No infobox or area; Thessalia admin-1 is a reading, acknowledged.

### corinth: pass
- [thin] `/keyframe_review/0`: One 22 km disc for 409 years: Perachora/Peraion, the Megarian border and the Corinthian War's ground (Lechaeum, the Long Walls) are not drawn; no page gives an area. Try: https://en.wikipedia.org/wiki/Corinthian_War
- Spot checks: /ledger/0 confirmed ('In 747 BC (a traditional date)'); /ledger/1 confirmed ('In 657 BC, polemarch Cypselus'); /ledger/2 confirmed ('581 BC: ... ending the tyranny'); /ledger/3 confirmed as the League of Corinth year 338; the garrison is on the Chaeronea page per the note
- Area: No area on the page (population 90,000 in 400 BC); disc is a reading, acknowledged.

### akragas: pass
- Spot checks: /ledger/0 confirmed ('around 582-580 BC by Greek colonists from Gela'); /ledger/2 confirmed (Heraclea Minoa 'around 500 BC'); /ledger/4 confirmed ('Around 483 BC, Theron invaded and conquered Himera'); /ledger/5 confirmed ('Himera continued subject to Theron until his death, in 472 BC'); /ledger/6 confirmed (captured and sacked by Carthaginian forces, 406)
- Area: Page: 'central portion of Sicily, an area of around 3,500 km2' after Himera; drawn province of Agrigento about 2,782 km2.

## Cross-dossier matrix

- sybaris -510 loss cp=croton -> croton -510 gain: matched. Cosenza province both sides.
- kingdom-of-paeonia -230 loss cp=kingdom-of-dardania -> kingdom-of-dardania -230 gain: matched. Veles admin-1 (Bylazora) both sides.
- kingdom-of-epirus -280 vassal_start cp=taras -> none: missing. taras has no vassal events (same batch); roman-republic /ledger/23 takes Tarentum from the Epirote garrison in 272.
- kingdom-of-epirus -272 vassal_end cp=taras -> none: missing. See above.
- athens -600 gain cp=Megara -> none: exception. No Megara dossier; not listed by the author (added below).
- athens -508 merge cp=Attic local communities (demes) -> none: exception. Not a polity; recommended as a rename.
- athens -365 gain cp=Samos (the Samians) -> none: exception. No Samos dossier; source name allowed.
- athens -322 loss cp=Samos (the Samians) -> none: exception. As above; Oropos in the same event goes to Boeotia (not named).
- athens -322 dissolve cp=macedonian-empire -> macedonian-empire -322 vassal_start: mismatch. Neighbour records a vassal_start of greek-city-states (client tint), this dossier hands Attica to macedonian-empire as successor.
- messene -369 found cp=peloponnesian-league -> peloponnesian-league -369 loss: mismatch. Year matches; peloponnesian-league /ledger/42 names greek-city-states, should now name messene.
- messene -201 occupation_start cp=peloponnesian-league -> none: missing. peloponnesian-league (eu-01-c) has no Nabis occupation of Messene in 201.
- messene -191 loss cp=achaean-league -> achaean-league -191 gain: mismatch. Year matches; achaean-league /ledger/25 names greek-city-states, should name messene.
- kingdom-of-epirus -343 vassal_start cp=macedonian-empire -> none: missing. macedonian-empire has no Epirote client relation (Alexander I installed by Philip II).
- kingdom-of-epirus -334 gain cp=lucanians -> none: missing. lucanians (-450..-272) has nothing in 334-331.
- kingdom-of-epirus -331 loss cp=lucanians -> none: missing. As above.
- kingdom-of-epirus -334 gain cp=Bruttii -> none: exception. No Bruttii dossier; not listed by the author (added below).
- kingdom-of-epirus -288 gain cp=antigonid-dynasty -> antigonid-dynasty -288 loss: matched. Neighbour's counterpart string is 'epirus'.
- kingdom-of-epirus -284 loss cp=kingdom-of-lysimachus -> kingdom-of-lysimachus -285 gain: matched. One year apart (Pyrrhus page 284, Lysimachus page 285); neighbour's counterpart 'epirus'.
- kingdom-of-epirus -277 gain cp=carthage -> none: exception. carthage (af-02) not written yet.
- kingdom-of-epirus -275 loss cp=carthage -> none: exception. As above.
- kingdom-of-epirus -274 gain cp=antigonid-dynasty -> antigonid-dynasty -274 loss: matched. Counterpart 'epirus'.
- kingdom-of-epirus -272 loss cp=antigonid-dynasty -> antigonid-dynasty -272 gain: matched. Counterpart 'epirus'.
- kingdom-of-epirus -231 loss cp=aetolian-league -> aetolian-league -233 gain: mismatch. Two years apart; the page sequence supports 233.
- kingdom-of-epirus -167 dissolve cp=roman-republic -> roman-republic -167 gain: matched. Neighbour names 'molossians' (a Cliopatria row -170..-165).
- croton -510 gain cp=sybaris -> sybaris -510 loss: matched. 
- croton -379 occupation_start cp=syracuse -> none: missing. syracuse has only Rhegium 386 and a generic 367 loss of the Italian holdings.
- croton -367 occupation_end cp=syracuse -> syracuse -367 loss: matched. Syracuse's 367 loss is generic (greek-city-states).
- croton -295 occupation_start cp=syracuse -> none: missing. syracuse has no Agathocles conquest of Croton.
- croton -277 occupation_end cp=syracuse -> syracuse -289 loss: mismatch. Agathocles dies 289; croton keeps the occupation to 277.
- croton -277 dissolve cp=roman-republic -> roman-republic -277 gain: matched. Neighbour's counterpart is 'Kingdom of Epirus (Pyrrhus)' ('Rufinus took Croton and Locri').
- taras -272 dissolve cp=roman-republic -> roman-republic -272 gain: matched. Neighbour's counterpart 'Kingdom of Epirus (Pyrrhus)'.
- chalcidian-league -393 gain cp=macedonian-empire -> none: missing. macedonian-empire has no 393/2 transfer to Olynthus.
- chalcidian-league -379 vassal_start cp=peloponnesian-league -> peloponnesian-league -379 vassal_start: matched. Neighbour's counterpart 'Olynthus (Chalcidian League)'.
- chalcidian-league -375 vassal_end cp=peloponnesian-league -> peloponnesian-league -371 vassal_end: mismatch. Four years apart; Chalcidian League page: 'Already in 375 BCE the Chalcidians threw off Spartan control'.
- chalcidian-league -348 dissolve cp=macedonian-empire -> macedonian-empire -348 gain: matched. Counterpart 'Chalcidian League'.
- massalia -49 loss cp=roman-republic -> roman-republic -49 gain: matched. Neighbour's counterpart greek-city-states.
- kingdom-of-paeonia -356 vassal_start cp=macedonian-empire -> macedonian-empire -358 vassal_start: mismatch. Two years apart; the Paeonia page has both 358 (campaign, oath) and 356 (infobox).
- kingdom-of-paeonia -285 occupation_start cp=kingdom-of-lysimachus -> none: missing. kingdom-of-lysimachus has no Paeonia event.
- kingdom-of-paeonia -280 occupation_end cp=kingdom-of-lysimachus -> kingdom-of-lysimachus -281 dissolve: mismatch. Ends after the counterpart's end.
- kingdom-of-paeonia -280 occupation_start cp=Celts under Brennus -> none: exception. No dossier for the Gallic invasion of 280-279.
- kingdom-of-paeonia -227 loss cp=antigonid-dynasty -> none: missing. antigonid-dynasty has no Paeonia gain in 227.
- kingdom-of-dardania -217 loss cp=antigonid-dynasty -> none: missing. antigonid-dynasty has no Bylazora gain in 217.
- kingdom-of-dardania -28 dissolve cp=roman-empire -> none: exception. roman-empire (-31..394) not written yet.
- kingdom-of-mycenae -1350 gain cp=Tiryns and Nauplion (adjacent centres) -> none: exception. Listed by the author (Mycenaean palace states).
- thessalian-league -353 dissolve cp=macedonian-empire -> macedonian-empire -352 vassal_start: matched. One year apart; neighbour draws Thessaly as a dependency.
- corinth -338 dissolve cp=macedonian-empire -> macedonian-empire -337 vassal_start: mismatch. Neighbour: League of Corinth hegemony over greek-city-states (client tint); this dossier names macedonian-empire as successor.
- akragas -483 gain cp=Himera -> none: exception. No Himera dossier; not listed by the author (added below).
- akragas -472 loss cp=Himera -> none: exception. As above.
- akragas -500 gain cp=Heraclea Minoa -> none: exception. Minor polis, no dossier.
- akragas -406 dissolve cp=carthage -> none: exception. carthage (af-02) not written yet.

## Gazetteer names needed

Samos (place, athens), Salamis (place, athens), Oropos (place, athens), Messenia (region, messene), Arta (place, kingdom-of-epirus), Policoro (place, kingdom-of-epirus), Lamezia Terme (place, kingdom-of-epirus), Manfredonia (place, kingdom-of-epirus), Erice (place, kingdom-of-epirus), Sibari (place, sybaris), Chalcidice (region, chalcidian-league), Agde (place, massalia), Hyères (place, massalia), Antibes (place, massalia), Pylos (place, kingdom-of-pylos), Agrigento (place, akragas)

## Counterparts needing dossiers

- Megara (megara, -600..-600): counterpart of athens /ledger/1 (Salamis); years are the event's only
- Bruttii (bruttii, -334..-277): counterpart of kingdom-of-epirus /ledger/3 and occupier of Croton (Crotone page)
- Himera (himera, -483..-409): counterpart of akragas /ledger/4-5; Himera page: destroyed by Carthage in 409
- Thurii (thurii, -444..-193): already listed by the author; needed for the croton fix

## Problems

- WebFetch answers through a summarising model; quotes above are its extracts, checked with narrow prompts. No page failed to load.
- Counterpart slug mismatch across groups: antigonid-dynasty, kingdom-of-lysimachus and aetolian-league use 'epirus', roman-republic uses 'Kingdom of Epirus (Pyrrhus)' and 'molossians', for the state this batch wrote as kingdom-of-epirus; the orchestrator should map them.
- Cliopatria row 'Molossians' (-170..-165) overlaps kingdom-of-epirus and is not owned by this batch; ownership needs settling.
- Five dossiers (sybaris, taras, kingdom-of-pylos, corinth, akragas) end their last keyframe at end-1 while massalia, chalcidian-league and kingdom-of-dardania add a one-year final keyframe; the validator accepts both, but the renderer should treat them alike.
- athens, corinth and thessalian-league end with a dissolve to macedonian-empire, which records only hegemony (vassal) relations for those years; one convention is needed.
- Applied fixes: athens /ledger/3 and /keyframe_review/0-1 (Samos 365), kingdom-of-paeonia /ledger/6 (278), chalcidian-league /keyframe_review/1/to (-384); all three re-validated with 0 errors and read back after writing.
