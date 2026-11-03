# Review of batch eu-04-b (Phase B)

Reviewed 2026-10-19 by the adversarial reviewer. Dossiers: gallic-empire, palmyrene-empire, western-roman-empire, kingdom-of-soissons, kingdom-of-odoacer, constantine-iii-usurper. Validator (--resolve): 0 errors in all six; 3 warnings in gallic-empire (unknown region Raetia).

| slug | verdict |
| --- | --- |
| gallic-empire | thin |
| palmyrene-empire | fix |
| western-roman-empire | fail |
| kingdom-of-soissons | pass |
| kingdom-of-odoacer | pass |
| constantine-iii-usurper | fail |

## gallic-empire: thin

Tried: 5 events on the Postumus and Gallic Empire pages (all confirmed with their years: 'By 261, Britannia, Narbonensis and Hispania also acknowledged him'; 'In the meantime, the Gallic Empire lost Hispania' under Marius; capitals Cologne 260-271 / Trier 271-274; Chalons 274), keyframe walk (260 new, 261+Hispania, 269 without, 270 minus Provence) consistent with the ledger, capitals inside the shape. Not broken; two border moves rest on confidence-1 events (minor state, within budget: thin by design). Mirrors for 261 Raetia, 269 Hispania and 270 Provence are missing on the roman-empire side (eu-04-a), not here.

Area: infobox None (None), Cliopatria 712514, ratio None. Gallic Empire page has no infobox area (confirmed); both Cliopatria shapes identical and run to 282, acknowledged in keyframe_review/3

Gaps for a gap-filler:
- `/ledger/2`: Year Raetia returned to Gallienus (261 loss at confidence 1, taken from Cliopatria; Postumus page names Raetia only among the provinces that recognised him at once) (try https://en.wikipedia.org/wiki/Raetia)
- `/ledger/4`: Year of Claudius's recovery of the Rhone valley (270 loss at confidence 1; Claudius Gothicus page gives no year inside 268-270; Placidianus took Grenoble) (try https://en.wikipedia.org/wiki/Placidianus)

Spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/3` confirmed; `/ledger/5` confirmed; `/ledger/6` confirmed

## palmyrene-empire: fix

Five confidence-3 events confirmed with their years (spring 262 Edessa/Carrhae; spring 270 Bosra/Arabia; October 270 Egypt; 271 Galatia/Ancyra; 273 revolt and razing). Cliopatria shapes correctly rejected. One small ledger/keyframe gap at 273.

Area: infobox None (None), Cliopatria 1043312, ratio 0.47. No infobox area (confirmed). Author's 271 shape about 0.49 M km2 against Cliopatria 1.04 M km2 (ratio 0.47), acknowledged in keyframe_review/6; all three Cliopatria shapes marked wrong for drawing 271 extent from 261.

Findings:
- `/ledger/13` (for the author): The 272 loss hands Palmyra itself (150 km) to Rome, leaving the state with no land, yet keyframe_review/8 draws Palmyra (50 km) in 273 and no 273 event gives it back. Evidence: Palmyrene Empire page: 'Aurelian besieged Palmyra in the summer of 272' and 'In 273, Palmyra rebelled under the leadership of a citizen named Septimius Apsaios'; the 273 keyframe has land the ledger never regains. Fix: Add a 273 gain of {place: Palmyra, km: 50} from roman-empire at confidence 3 (the Apsaios revolt, source Palmyrene Empire page), or drop Palmyra from the 272 loss so that the 273 dissolve carries it. Non-blocking.
- `/ledger/2` (for the author): The Roman East (Syria, Lebanon, Judaea) passes from roman-empire in 261 here and in 267 in roman-empire /ledger/95, which also gives Cilicia, Cappadocia and Galatia in 267; this dossier has Galatia in 271 and never Cilicia or Cappadocia. Evidence: Palmyrene Empire page: Galatia and Ancyra in the 271 narrative ('Afterward, in 271, Zabbai started the operations in Asia Minor'); neither Cilicia nor Cappadocia is named (checked). The 261 date is the author's bridge at confidence 1; the infobox has 'Established: 260 (as kingdom)/270 (as empire)'. Fix: Keep this dossier's years (they are the page's) but agree one year with eu-04-a for the Roman East; consider recording 260/261-270 as a client relation (Odaenathus 'minted coins only in Gallienus's name') so both dossiers can mirror it. Routed in cross_checks; non-blocking here.

Gaps for a gap-filler:
- `/ledger/2`: Year Odaenathus's rule over Syria, Phoenice and Palaestina began (261 at confidence 1; Odaenathus page lists the provinces without a year) (try https://en.wikipedia.org/wiki/Odaenathus)
- `/ledger/5`: End of the Persian contest (267 at confidence 1; Odaenathus page: second invasion 266, his death 267) (try https://en.wikipedia.org/wiki/Odaenathus)

Spot checks: `/ledger/3` confirmed; `/ledger/7` confirmed; `/ledger/8` confirmed; `/ledger/9` confirmed; `/ledger/14` confirmed

## western-roman-empire: fail

Every confidence-3 event checked is on its page with its year (413, 418, 435, 439, 442, 472, 475, 476). The dossier fails on land it does not account for: Hispania under Constantine III in 408 (its own page), the western and southern Hispania drop between the 462 and 469 shapes, and three neighbours' gains from it with no mirror here (huns 433 Pannonia, eastern-roman-empire 437 Sirmium, mauro-roman-kingdom 429).

Area: infobox 2000000 (395), Cliopatria 2132727, ratio 0.94. Infobox '2,000,000 km2' (395) confirmed; Cliopatria western-roman-empire_395 2,132,727 km2. Capitals in the infobox match the eight capital_move events.

Findings:
- `/keyframe_review/3/note` (for the author): The 407-408 keyframe keeps Hispania with Honorius ('Spain stays with Honorius until the 409 revolt'), but the dossier's own source has Hispania under Constantine III from 408. Evidence: Constantine III page: 'Early in 408, he [Constans] was sent with Gerontius into Hispania'; Constans 'established himself at Saragossa and rebuilt the civilian administration'; 'With Hispania back under Constantine's control', Constans returned to Arles. Fix: Split the 407 keyframe at 408 and remove Hispania from 408; add a 408 loss of {intersect: [Hispania, WRE 406 shape]} to constantine-iii-usurper (confidence 2, Constantine III page). Blocking.
- `/ledger/10` (for the author): The 409 loss of all Hispania to vandals is mis-attributed: Hispania was Constantine III's in 408 and passed to Gerontius's Maximus in 409; the barbarians only entered in autumn 409 and settled by lot in 411. Evidence: Constantine III page: 'In 409 Gerontius rebelled, proclaimed his client Maximus emperor'; 'in autumn 409 much of the barbarian force entered Hispania'. The note itself says the region is the reading. Fix: Remove this loss (the 408 loss to constantine-iii-usurper replaces it); Hispania 409-411 belongs to the maximus-usurper and vandals dossiers; keep /ledger/15 (414 regain) only for what Rome actually recovered, with its counterpart.
- `/ledger (no event, 433)` (for the author): No mirror for huns /ledger/8, a 433 gain from western-roman-empire of 'some parts of Pannonia' (Pannonia Prima); this dossier keeps Pannonia in every keyframe to 454. Evidence: huns.json /ledger/8: '433: Aetius cedes part of Pannonia. In 433 some parts of Pannonia were ceded to them by Flavius Aetius' (Rugila page). Author notes: 'no page opened dates it'. Fix: Add a 433 loss of {region: Pannonia} (Pannonia Prima) to huns at confidence 2, source https://en.wikipedia.org/wiki/Rugila, and cut it from the 435, 439, 441, 443, 451 and 452 keyframe corrections. Blocking (gain with no mirror).
- `/ledger (no event, 437)` (for the author): No mirror for eastern-roman-empire /ledger/6, a 437 gain from western-roman-empire of Sirmium and Pannonia Secunda (dowry of Licinia Eudoxia). Evidence: eastern-roman-empire.json /ledger/6: 'As part of the dowry of Licinia Eudoxia, Valentinian III recognized Eastern sovereignty over the prefecture'. Not mentioned anywhere in this dossier. Fix: Add a 437 loss of {place: Sirmium, km: 25} (Pannonia Secunda / western Illyricum as the ERE dossier has it) to eastern-roman-empire at confidence 2, or say in notes why not.
- `/ledger (no event, 429)` (for the author): No mirror for mauro-roman-kingdom /ledger/0, a 429 found from western-roman-empire in Mauretania Caesariensis around Altava; this dossier keeps Africa whole to 434 and gives Mauretania to the Vandals in 435. Evidence: mauro-roman-kingdom.json /ledger/0: infobox 'Military independence from the Western Roman Empire: 429' (Mauro-Roman Kingdom page). Fix: Add a 429 loss of {union: [Oranais, {place: Algiers, km: 150}]} to mauro-roman-kingdom (confidence 2) and take it out of the 435 Vandal loss, or record the disagreement in notes for the af group.
- `/keyframe_review/20` (for the author): Unexplained area: between the 462-468 shape (1.11 M km2, bbox west edge -9.23) and the 469b keyframe (Cliopatria 469 plus the 462 shape's Gaul and Tarraconensis; 469 bbox west edge -2.84) Lusitania, Gallaecia, Baetica and most of Carthaginiensis leave, and no ledger event between 462 and 472 removes them. Evidence: shapes.csv: western-roman-empire_462 1,106,379 km2 bbox -9.233..19.458; western-roman-empire_469 615,836 km2 bbox -2.837..19.458; ledger 462-472 has only Sicily, Burgundian, Visigothic (Gaul), Alamannic, Frankish and Tarraconensis losses. Author's notes list 'Spain 462-468' as unverified. Fix: Add the loss of western and southern Hispania to visigothic-kingdom (Euric's campaigns from 466) and/or kingdom-of-the-suebi at the year a page gives, or keep Hispania in the 469b correction until a dated loss. Blocking (unexplained keyframe change of several hundred thousand km2).
- `/keyframe_review/20/correction` (for the author): The 469-471 and 472-474 keyframes keep Arles and Provence Roman, and /ledger/52 moves Provence only in 476 at confidence 1, but the cited Visigothic page has Euric take Arles after the Battle of Arles in 471; the battle is absent from wars. Evidence: Visigothic Kingdom page: 'The Roman army was crushed at the nearby Battle of Arles (471)', 'resulting in Euric capturing Arles, securing much of southern Gaul'. Fix: Add the Battle of Arles (471) to the 'Euric's conquests' war zones; add a 471 contest_start (or loss) for {place: Arles, km: 80} with visigothic-kingdom, or explain in the note why 476 is kept for Provence.
- `/ledger/28-31` (applied by reviewer): Counterpart slug hunnic-empire does not have a dossier: huns.json carries both Cliopatria rows ('Huns', 'Hunnic Empire') under the earlier slug. Evidence: huns.json identity.cliopatria_names = ['Huns', 'Hunnic Empire']. Fix: Counterpart and war belligerents changed from hunnic-empire to huns (7 places); re-validated: 0 errors, 0 warnings.
- `/ledger/28-31` (for the author): Type mismatch with huns /ledger/13-16: Attila's 451 and 452 campaigns are occupation_start/occupation_end there and contest_start/contest_end here; the places also differ (huns: Metz, Reims, Troyes, Orleans; Friuli, Veneto, Lombardy). Evidence: huns.json /ledger/13-16; the brief requires an occupation of X's land to appear as an occupation in X's ledger. Fix: Agree one representation with eu-06: either occupation_start/occupation_end here with the huns places, or ask the huns author to switch to contest. Non-blocking.

Gaps for a gap-filler:
- `/ledger/3`: Northern Britain strip lost 402 (confidence 1) (try https://en.wikipedia.org/wiki/End_of_Roman_rule_in_Britain)
- `/ledger/7`: End of Alaric's first Italian campaign 407 (confidence 1) (try https://en.wikipedia.org/wiki/Alaric_I)
- `/ledger/15`: Roman recovery in Hispania 414-418 (confidence 1, from Cliopatria) (try https://en.wikipedia.org/wiki/Wallia)
- `/ledger/16`: Recovery of Septimania 415-417 (confidence 1) (try https://en.wikipedia.org/wiki/Ataulf)
- `/ledger/21`: Frankish advance into Brabant 439 (confidence 1) (try https://en.wikipedia.org/wiki/Chlodio)
- `/ledger/23`: Sicily to the Vandals 441 (confidence 1; Vandal page has only the 440 raid) (try https://en.wikipedia.org/wiki/Genseric)
- `/ledger/24`: What Rome got back under the 442 treaty (Mauretania Sitifensis/Caesariensis and western Numidia; Vandal Kingdom page names only the Vandal gains) (try https://en.wikipedia.org/wiki/Genseric)
- `/ledger/32`: Ostrogothic settlement in Pannonia after Nedao (455, confidence 1) (try https://en.wikipedia.org/wiki/Battle_of_Nedao)
- `/ledger/33`: Visigothic hold on Aquitaine/Spain 455 (confidence 1) (try https://en.wikipedia.org/wiki/Theodoric_II)
- `/ledger/37`: Sardinia to the Vandals (458, confidence 1; undated on the Vandal page) (try https://en.wikipedia.org/wiki/Genseric)
- `/ledger/42`: Sicily after Majorian's death (462, confidence 1) (try https://en.wikipedia.org/wiki/Marcellinus_(magister_militum))
- `/ledger/43`: Burgundian expansion down the Rhone (462 vs 'later 460s') (try https://en.wikipedia.org/wiki/Gundioc)
- `/ledger/44`: Narbonne/Septimania ceded 462 (confidence 1) (try https://en.wikipedia.org/wiki/Theodoric_II)
- `/ledger/45`: Alamannic advance 462 (confidence 1) (try https://en.wikipedia.org/wiki/Alemanni)
- `/ledger/46`: Frankish Belgica Secunda 462 (confidence 1) (try https://en.wikipedia.org/wiki/Childeric_I)
- `/ledger/52`: Year Provence (Arles, Marseille) passed to Euric (476 at confidence 1; see the 471 finding) (try https://en.wikipedia.org/wiki/Euric)

Spot checks: `/ledger/13` confirmed; `/ledger/17` confirmed; `/ledger/18` confirmed; `/ledger/22` confirmed; `/ledger/24` confirmed; `/ledger/47` confirmed; `/ledger/49` confirmed; `/ledger/54` confirmed; `/ledger/10` mis-dated

## kingdom-of-soissons: pass

Both events confirmed (Battle of Soissons 486; Syagrius executed 486 or 487; extent and duration disputed, 'name given by modern scholars'). The 476-479 shape's Dalmatian cells verified via shapes.csv and correctly moved to western-roman-empire_476. Capital Soissons inside the 480 shape bbox. Could not break it.

Area: infobox None (None), Cliopatria 125260, ratio None. No infobox on the page (confirmed). shapes.csv kingdom-of-soissons_476 modern countries France;Croatia;Bosnia and Herzegovina, bbox to 19.46 E and 42.24 N: the extra cells are Dalmatia, not Odoacer's Italy, as the author says (data/README.md suspicion corrected).

Gaps for a gap-filler:
- `/identity/start`: Start year: 476 follows Cliopatria; Aegidius held northern Gaul from about 457 and broke with Libius Severus in 461, the Syagrius infobox gives 'Domain of Soissons 464-486' (flagged by the author; a modelling choice, not a fault) (try https://en.wikipedia.org/wiki/Aegidius)

Spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed

## kingdom-of-odoacer: pass

All dated events confirmed on the Odoacer page (rex 23 August 476, Romulus abdicates 4 September; Sicily September or October 476 after Clover; Dalmatia annexed within two years of May 480; Rugians 487/488; Theodoric 489; Ravenna 5 March 493; Odoacer killed ten days later). Mirrors with western-roman-empire match (476 loss, 480 dissolve / 481 gain). Could not break it.

Area: infobox None (None), Cliopatria None, ratio None. New state, no Cliopatria row; Odoacer page infobox has no area (confirmed).

Gaps for a gap-filler:
- `/ledger/1`: Extent of the Alpine and Danubian remnant that passed with Italy in 476 (confidence 1, bridged from the 475 WRE shape) (try https://en.wikipedia.org/wiki/Noricum)
- `/keyframe_review/2`: Whether Rugiland should be Odoacer's in 488-493: the Odoacer page says after the 487/488 victory 'Onoulphus found it necessary to evacuate the remaining Romans and resettled them in Italy' (try https://en.wikipedia.org/wiki/Rugiland)

Spot checks: `/ledger/0` confirmed; `/ledger/2` confirmed; `/ledger/3` confirmed; `/ledger/4` confirmed; `/ledger/5` confirmed; `/ledger/6` confirmed; `/ledger/7` confirmed

## constantine-iii-usurper: fail

Dated events are all on the page (early 407 acclamation; Arles capital by May 408; Armorica expels his officials later in 409; beheaded August or September 411, head shown 18 September). Fails because the realm's extent is wrong: Hispania 408-409 is omitted against the page, and the 411 collapse to Arles has no ledger event.

Area: infobox None (None), Cliopatria None, ratio None. New rebel state, no Cliopatria row and no state infobox (the page is a biography).

Findings:
- `/keyframe_review/1/correction` (for the author): The 408 keyframe (Britain and Gaul) and the ledger leave out Hispania, which the dossier's main page puts under Constantine's control in 408; the 'Revolt of Constantine III' outcome even says he 'lost ... Hispania in 409' without ever gaining it. Evidence: Constantine III page: 'Early in 408, he [Constans] was sent with Gerontius into Hispania'; Constans 'established himself at Saragossa and rebuilt the civilian administration'; 'With Hispania back under Constantine's control'; 'In 409 Gerontius rebelled, proclaimed his client Maximus emperor'. Fix: Add a 408 gain of {intersect: [Hispania, WRE 406 shape]} from western-roman-empire (confidence 2) and a 409 loss of it to maximus-usurper (confidence 3, 'In 409 Gerontius rebelled'); put Hispania in the 408 correction; drop the notes' 'Hispania is not in the realm'. Blocking (the realm's largest province missing).
- `/keyframe_review/3` (for the author): Unexplained shrink: the 409-410 keyframe is Gaul without Armorica, the 411 keyframe is Arles (150 km) only, and no ledger event between them removes the rest of Gaul; the dissolve hands over only Arles while western-roman-empire /ledger/12 gains all Gaul except Armorica from this dossier in September 411. Evidence: Constantine III page: Gerontius 'besieged Constantine in Arles' after defeating Constans at Vienne 'probably early in 411'; Jovinus was proclaimed on the Rhine in 411 (author's notes). Fix: Add an early-411 loss (or contest_start) of Gaul minus Arles to maximus-usurper (Gerontius), confidence 2, and make this dossier's dissolve region and western-roman-empire /ledger/12 describe the same land (either both all of Gaul-minus-Armorica, or the WRE gain split between this dossier's Arles and the Gerontius/Jovinus counterparts). Blocking.

Spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/3` confirmed; `/ledger/4` confirmed; `/ledger/5` confirmed

## Cross-dossier problems

- gallic-empire /ledger/1 261 gain (roman-empire) -> mismatch vs roman-empire /ledger/94 260 loss: roman-empire /ledger/94 (260 loss) covers France, Benelux, Great Britain but not Hispania; GE gains Britain, Narbonensis and Hispania in 261 ('By 261, Britannia, Narbonensis and Hispania also acknowledged him', Postumus page). Hispania part unmatched; route to eu-04-a.
- gallic-empire /ledger/2 261 loss (roman-empire) -> missing: roman-empire (eu-04-a) has no 261 gain of Raetia; GE event is confidence 1 from Cliopatria
- gallic-empire /ledger/3 269 loss (roman-empire) -> missing: roman-empire has no 269 gain of Hispania from gallic-empire; its 260 loss also omits Hispania ('Hispania only briefly') and its shape keeps Spain 261-268 (overlap). Route to eu-04-a.
- gallic-empire /ledger/4 270 loss (roman-empire) -> missing: roman-empire has no 270 gain of the Rhone valley/Provence from gallic-empire. Route to eu-04-a.
- palmyrene-empire /ledger/0 260 found (roman-empire) -> mismatch: roman-empire dates the loss of the East to 267 (/ledger/95, Crisis of the Third Century page); this dossier 260/261 (Odaenathus page). Both sides must agree; route to eu-04-a and this author.
- palmyrene-empire /ledger/2 261 gain (roman-empire) -> mismatch vs roman-empire /ledger/95 267 loss: roman-empire /ledger/95 is 267, six years later, and adds Cilicia, Galatia and Cappadocia that the Palmyrene page does not name.
- palmyrene-empire /ledger/7 270 gain (roman-empire) -> mismatch vs roman-empire /ledger/97 271 loss: Arabia 270: roman-empire has no Arabia event (its 267 loss covers Levant/Judaea; 271 loss is Egypt only).
- palmyrene-empire /ledger/9 271 gain (roman-empire) -> mismatch vs roman-empire /ledger/97 271 loss: Galatia 271 here vs 267 in roman-empire /ledger/95.
- western-roman-empire /ledger/10 409 loss (vandals) -> mismatch: Hispania 409: counterpart should be maximus-usurper (no dossier) after a 408 loss to constantine-iii-usurper, which neither dossier records (Constantine III page).
- western-roman-empire /ledger/12 411 gain (constantine-iii-usurper) -> mismatch vs constantine-iii-usurper /ledger/5 411 dissolve: Land disagrees: WRE gains Gaul minus Armorica from constantine-iii-usurper in Sept 411; constantine-iii-usurper /ledger/5 dissolves with Arles (150 km) only and has no event for the rest of Gaul in 411.
- western-roman-empire /ledger/28 451 contest_start (huns) -> mismatch vs huns /ledger/13 451 occupation_start: type differs: huns records occupation, WRE contest; places differ. Slug fixed by reviewer (hunnic-empire -> huns).
- western-roman-empire /ledger/29 451 contest_end (huns) -> mismatch vs huns /ledger/14 451 occupation_end: type differs: huns records occupation, WRE contest; places differ. Slug fixed by reviewer (hunnic-empire -> huns).
- western-roman-empire /ledger/30 452 contest_start (huns) -> mismatch vs huns /ledger/15 452 occupation_start: type differs: huns records occupation, WRE contest; places differ. Slug fixed by reviewer (hunnic-empire -> huns).
- western-roman-empire /ledger/31 452 contest_end (huns) -> mismatch vs huns /ledger/16 452 occupation_end: type differs: huns records occupation, WRE contest; places differ. Slug fixed by reviewer (hunnic-empire -> huns).
- huns /ledger/8 433 gain (western-roman-empire) -> missing: WRE has no 433 loss of Pannonia (Pannonia Prima) and keeps Pannonia to 454; fix listed for WRE.
- eastern-roman-empire /ledger/6 437 gain (western-roman-empire) -> missing: WRE has no 437 loss of Sirmium / Pannonia Secunda; fix listed for WRE.
- mauro-roman-kingdom /ledger/0 429 found (western-roman-empire) -> missing: WRE has no 429 loss in Mauretania Caesariensis; it gives Mauretania to the Vandals in 435. Route to the af group and WRE author.
- roman-empire /ledger/95 267 loss (palmyrene-empire) -> mismatch vs palmyrene-empire /ledger/2 261 gain: six years apart; roman-empire adds Cilicia, Galatia (here 271) and Cappadocia (never here; not on the Palmyrene page).

Exceptions: counterparts owned by eu-06 (visigoths, vandals, vandal-kingdom, visigothic-kingdom, burgundian-kingdom, ostrogoths, rugiland, kingdom-of-alamannia), eu-07 (salian-franks, kingdom-of-the-franks) and me-06 (sasanian-empire) have no dossiers yet.

Gazetteer: Raetia (region; gallic-empire).
