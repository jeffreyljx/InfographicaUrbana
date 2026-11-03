# Review of batch eu-04-x

Adversarial review, 2026-10-19, of the 22 dossiers written by the eu-04-x research agent (Roman Empire additions: states Cliopatria lacks). Machine copy: history/notes/phase-b/reviews/eu-04-x.json.

Method: validator with --resolve on all 22 (0 errors; one warning, marcomanni /ledger/6 counterpart danubian-suebi has no dossier, which the author lists). Each ledger read in full; mirrors looked up in roman-empire, western-roman-empire, constantine-iii-usurper, palmyrene-empire and the batch's own dossiers; 33 Wikipedia pages opened for spot checks, weighted to confidence-3 events and to the events that move the most land. None of these states has a Cliopatria row or an infobox area, so the area checks are empty.

Policy used for verdicts: small fixes verified on a page (a year, a capital, a slug, a war's years, a region copy) were applied by the reviewer and tagged in the file; a missing land or client event that a page the author already opened states, or a mirror that disagrees with a written neighbour, is a blocking finding and sends the dossier back (fail); confidence-1 bridges and extents no opened page gives are thin.

## Summary

| dossier | verdict | main reason |
| --- | --- | --- |
| britannic-empire | pass | nothing broke |
| domain-of-magnus-maximus | pass | capital move to Trier undated (conf 1); a page dating Maximus's residence at Trier |
| alemanni | fail | The Alemannic conquest and settlement of Alsace in 406 is dated on a page the author opened but is not in the ledger, and the notes say the left-bank settlement |
| marcomanni | fail | The 20 event is typed 'gain' from quadi, but its mirror in the quadi dossier (/ledger/1) is a vassal_start with marcomanni as counterpart; both dossiers now dra |
| quadi | fail | The Quadi kingdom's Roman client status is on the pages the author opened but not in the ledger, so the map draws an independent kingdom. |
| kingdom-of-burebista | fix | fixed by reviewer: The war names the slug boii, whose dossier is the Cisalpine Boii of Italy (-396 to -191), not the Danubian Boii Burebista fought in 60/59 BC. |
| dacian-kingdom | fail | Domitian's Dacian War (85-89) starts two years before the state's life (87): the start is Decebalus's accession, a change of ruler, not the founding of the stat |
| bar-kokhba-state | fix | fixed by reviewer: The war ran to 136 while the state ends in 135 (wars must lie inside the life). |
| jewish-provisional-government | fix | fixed by reviewer: The war ran to 74 while the state ends in September 70. |
| marcellinus-dalmatia | fix | fixed by reviewer: The dissolve was dated 28 August 475 (Nepos's flight to Salona) although the author's own note says Dalmatia ceased to be separate when Nepos |
| eugenius-usurpation | pass | nothing broke |
| maximus-usurper | fail | Gerontius's 411 conquests in southern Gaul are missing although two neighbour dossiers record them as maximus-usurper's land. |
| jovinus-usurper | thin | extent: 'Gaul' within the 406 Western Roman shape is a maximum that overlaps the western-roman-empire dossier's own Gaul from 411 (its /ledger/12 and /ledger/14 |
| macrianus-and-quietus | fix | fixed by reviewer: The capital note said the pages name no seat before 261, but the Odaenathus page names Antioch as Macrianus's centre. |
| chatti | fail | Domitian's conquest of Chattan territory is on a page the author opened but no loss is recorded; the roman-empire dossier gains 'the Chatti country in Hesse and |
| cherusci | fail | The Cherusci's subjection to Rome from Drusus's campaigns to the Teutoburg Forest is on the dossier's own page but not in the ledger; the roman-empire dossier o |
| hermunduri | thin | Thuringia is added in 51 with no ledger event; the salt-river war of 57 (Werra or Saale, 'possibly') is the only lead and is not a ledger event |
| tarcondimotid-kingdom | fail | The kingdom's Roman client status is the page's own description but is not in the ledger. |
| brigantes | fail | The Brigantes' status as a Roman client kingdom under Cartimandua is on two opened pages but not in the ledger. |
| iceni | fail | The Iceni's client-kingdom status after 43 is quoted in the dossier's own war note but not in the ledger. |
| catuvellauni | thin | start is the first coinage at Verlamion, ca 20 BC (conf 1) |
| trinovantes | thin | first record before Caesar's invasions, not a founding (conf 1) |

Counts: pass 3, fix 5, thin 4, fail 10

## britannic-empire: pass

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Carausius: confirmed: 'declaring himself Emperor in Britain and northern Gaul', late 286 or early 287; infobox Reign 286-293
- `/ledger/1` https://en.wikipedia.org/wiki/Carausian_Revolt: confirmed: 'In 293, Constantius Chlorus ... isolated Carausius by retaking the territory he held in Gaul'
- `/ledger/2` https://en.wikipedia.org/wiki/Allectus: confirmed: 'Allectus assassinated Carausius and assumed command himself'; infobox Reign 293-296
- `/ledger/3` https://en.wikipedia.org/wiki/Allectus: confirmed: invasion 'in September 296'; Asclepiodotus 'landed near Southampton Water'
- `/ledger/5` https://en.wikipedia.org/wiki/Carausian_Revolt: confirmed: 'in 296, the Roman reconquest of Britain began'

Tried and could not break: page dates and places of every confidence-3 event, keyframe-to-ledger consistency, capital inside the shape, wars inside the life, mirrors in the counterpart dossiers.

## domain-of-magnus-maximus: pass

Thin (for a gap-filler):

- `/ledger/1`: capital move to Trier undated (conf 1); a page dating Maximus's residence at Trier Try https://en.wikipedia.org/wiki/Trier

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Magnus_Maximus: confirmed: 'In 383, he was proclaimed emperor in Britannia, and in Gaul the next year'
- `/ledger/2` https://en.wikipedia.org/wiki/Valentinian_II: confirmed: 383, 'established his headquarters in Gaul and Hispania' (the Magnus Maximus lead gives Hispania to Valentinian; conflict flagged by the author)
- `/ledger/3` https://en.wikipedia.org/wiki/Magnus_Maximus: confirmed: Gratian 'was killed at Lyon on 25 August 383'
- `/ledger/4` https://en.wikipedia.org/wiki/Magnus_Maximus: confirmed: 'launched a surprise invasion of Italy in 387'; Valentinian 'fled ... to Theodosius I'
- `/ledger/6` https://en.wikipedia.org/wiki/Magnus_Maximus: confirmed: 'Maximus surrendered in Aquileia ... was executed'; infobox died 28 August 388

Tried and could not break: page dates and places of every confidence-3 event, keyframe-to-ledger consistency, capital inside the shape, wars inside the life, mirrors in the counterpart dossiers.

## alemanni: fail

Findings:

- `/ledger (new event between /ledger/3 and /ledger/4); /keyframe_review; /notes` (for the author). The Alemannic conquest and settlement of Alsace in 406 is dated on a page the author opened but is not in the ledger, and the notes say the left-bank settlement is undated on the pages. Evidence: Alemanni page: 'In the great mixed invasion of 406, the Alemanni appear to have crossed the Rhine river a final time, conquering and then settling what is today Alsace'. Author's notes: 'The left-bank settlement ... and the Swiss plateau/Alsace are undated on the pages and are not drawn'. Fix: Add {year 406, type gain, counterpart western-roman-empire, region {region: Alsace, text: 'what is today Alsace'}, confidence 2, source https://en.wikipedia.org/wiki/Alemanni}; add keyframe alemanni_406 (406-461) = alemanni_300 shape plus Alsace; extend the 461 dissolve region; correct /notes; route a 406 loss of Alsace to the western-roman-empire dossier (its /ledger/50 gives the Rhine region to kingdom-of-alamannia only in 462, conf 1).

Thin (for a gap-filler):

- `/ledger/2`: year of Probus's recapture of the Agri Decumates (277 bridged from the 277-278 campaign; conf 1) Try https://en.wikipedia.org/wiki/Limes_Germanicus
- `/ledger/3`: year the Romans finally gave up the Agri Decumates (300 bridged between '290s or 300s' and 'about 310'; conf 1) Try https://en.wikipedia.org/wiki/Limes_Germanicus
- `/ledger/4`: the 461/462 cut is Cliopatria's row start, not an event (conf 1); consider merging with kingdom-of-alamannia Try https://en.wikipedia.org/wiki/Alamannia

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Alemanni: confirmed: 'first mentioned by Cassius Dio describing the campaign of Caracalla in 213'
- `/ledger/1` https://en.wikipedia.org/wiki/Alemanni: confirmed: 'the Alemanni captured the Agri Decumates in 260 AD'
- `/ledger/2` https://en.wikipedia.org/wiki/Agri_Decumates: confirmed (no year on page, conf 1 honest): 'Emperor Probus definitely recaptured the area'
- `/ledger/3` https://en.wikipedia.org/wiki/Agri_Decumates: confirmed: 'until the 290s or 300s, when the Roman military seems to have definitively abandoned the region'; 'By about 310 the Alemanni were becoming the dominant population'

## marcomanni: fail

Findings:

- `/ledger/2` (for the author). The 20 event is typed 'gain' from quadi, but its mirror in the quadi dossier (/ledger/1) is a vassal_start with marcomanni as counterpart; both dossiers now draw Moravia as their own land. Evidence: Marcomanni page: the displaced Marcomanni 'were moved by the Romans to an area near the Danube, between the Morava and "Cusus" rivers' and 'placed under the control of the Quadian king Vannius'. quadi /ledger/1: 20 vassal_start cp marcomanni; quadi keyframe quadi_20 includes Jihomoravsky. Fix: Change /ledger/2 to {year 20, type vassal_start, counterpart quadi, region Moravia, conf 2}; the exiles' land is a Quadian-tinted vassal, not a Marcomannic gain.
- `/ledger/3` (for the author). The 51 'gain' from Hermunduri should close the Quadian overlordship: quadi /ledger/2 has vassal_end cp marcomanni in 50 with no mirror here. Evidence: Marcomanni page: Vannius was 'deposed by Vibilius and the Hermunduri, working together with the Lugii from the north, in 50/51 AD'. quadi /ledger/2: 50 vassal_end cp marcomanni. Fix: Add {year 50, type vassal_end, counterpart quadi, region Moravia, conf 2} (same year as quadi /ledger/2); keep or drop the Bohemia gain from Hermunduri according to the thin item below.

Thin (for a gap-filler):

- `/ledger/1 and /ledger/3`: The page does not say the Hermunduri took Bohemia: only Maroboduus's and Catualda's followers were moved; the 19 loss and 51 gain of Bohemia (and hermunduri /ledger/1-2) are unsupported bridges at conf 1. Either find a page or keep Bohemia Marcomannic throughout. Try https://en.wikipedia.org/wiki/Catualda
- `/ledger/6`: 453 end bridged from the Suebian kingdom of Hunimund (conf 1); the page says the Marcomanni 'had held Pannonia Valeria' by then, not Bohemia Try https://en.wikipedia.org/wiki/Hunimund

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Marcomanni: confirmed: Maroboduus king, 'Boiohaemum', 'By 6 BC ... had established a powerful kingdom there'
- `/ledger/1` https://en.wikipedia.org/wiki/Marcomanni: partly: Catualda deposed Maroboduus in 19 and Vibilius deposed Catualda 'that same year'; the page 'does not say the Hermunduri took Bohemia' (conf 1 bridge)
- `/ledger/2` https://en.wikipedia.org/wiki/Marcomanni: confirmed (19 on page, 20 in dossier, conf 1): 'placed under the control of the Quadian king Vannius'
- `/ledger/4` https://en.wikipedia.org/wiki/Marcomannic_Wars: confirmed: Ballomar's coalition 'crossed the Danube, and defeated a Roman force of 20,000' in the campaign from autumn 169
- `/ledger/5` https://en.wikipedia.org/wiki/Marcomannic_Wars: confirmed: 'Commodus negotiated peace with the Marcomanni and Quadi'; infobox 'Status quo ante bellum'

## quadi: fail

Findings:

- `/ledger (new events)` (for the author). The Quadi kingdom's Roman client status is on the pages the author opened but not in the ledger, so the map draws an independent kingdom. Evidence: Quadi page: Vangio and Sido 'divided his realm between themselves as loyal Roman client kings' (50/51) and by 173 'they expelled their Roman-approved king Furtius'; Vannius page (cited at /ledger/0): Vannius ruled 20-50 as a client king of the Roman Empire. Fix: Add {year 20, type vassal_start, counterpart roman-empire, region = the quadi_20 shape, conf 2, source Vannius page} and a vassal_end at the break (173, 'expelled their Roman-approved king Furtius', conf 2, Quadi page); ask the roman-empire dossier for the mirror vassal_start/vassal_end with counterpart quadi.
- `/ledger/1, /ledger/2` (for the author). The vassal_start/vassal_end with marcomanni are not mirrored: marcomanni /ledger/2 is a 'gain' from quadi and the marcomanni ledger has no 50 vassal_end. Evidence: marcomanni /ledger/2: 20 gain cp quadi (Moravia); marcomanni /ledger/3: 51 gain cp Hermunduri. Fix: No change here if the marcomanni dossier is corrected as listed there; otherwise align both sides to 20 and 50.

Thin (for a gap-filler):

- `/ledger/6`: end of the Quadi homeland (409 is Jerome's letter; conf 1) Try https://en.wikipedia.org/wiki/Kingdom_of_the_Suebi
- `/keyframe_review/0`: 180 Roman garrisons 'of 20,000 men each permanently stationed in both countries' (Quadi page) are not drawn as an occupation; a page giving their years would place an occupation_start/end Try https://en.wikipedia.org/wiki/Marcomannic_Wars

Spot checks:

- `/ledger/1` https://en.wikipedia.org/wiki/Quadi: confirmed: exiles 'moved by the Romans to an area near the Danube, between the Morava and "Cusus" rivers, and a Quadian named Vannius was made king of them' (page dates Maroboduus's fall c. 18)
- `/ledger/2` https://en.wikipedia.org/wiki/Quadi: confirmed: Vannius deposed 'in 50/51 AD'
- `/ledger/4` https://en.wikipedia.org/wiki/Marcomannic_Wars: confirmed: 'By 173, the Romans began to turn on the Quadi, who had violated their treaty'
- `/ledger/5` https://en.wikipedia.org/wiki/Quadi: confirmed: by 180 'Roman garrisons of 20,000 men each permanently stationed in both countries'
- `/ledger/6` https://en.wikipedia.org/wiki/Quadi: confirmed (conf 1): last mention 'in another letter by Saint Jerome from 409'

## kingdom-of-burebista: fix

Findings:

- `/wars/0/belligerents` (applied by reviewer). The war names the slug boii, whose dossier is the Cisalpine Boii of Italy (-396 to -191), not the Danubian Boii Burebista fought in 60/59 BC. Evidence: Burebista page: 'In 60/59 BC he defeated and conquered the Boii'; history/polities/boii.json identity years -396..-191. Fix: Belligerent set to the name string 'Boii and Taurisci (Danubian Celts)', with a reviewer note.

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Dacia: confirmed: 'A Dacian kingdom that united the Dacians and the Getae was formed under the rule of Burebista in 82 BC' (the Burebista page gives 82 or 61-60 BC; conf 2 honest)
- `/ledger/1` https://en.wikipedia.org/wiki/Burebista: confirmed: 'Beginning around 55 BC Burebista annexed the Greek cities on the coast of the Black Sea', 'from Olbia to Apollonia'
- `/ledger/2` https://en.wikipedia.org/wiki/Burebista: confirmed: killed 'in either 45' or '44 BC'; 'After Burebista's death, the kingdom was divided into four parts'

## dacian-kingdom: fail

Findings:

- `/identity/start; /ledger/0; /wars/0` (for the author). Domitian's Dacian War (85-89) starts two years before the state's life (87): the start is Decebalus's accession, a change of ruler, not the founding of the state. Evidence: Decebalus page: infobox 'Predecessor: Duras'; 'In 85 AD the Dacian army began minor raids upon ... Moesia'; 'In 86 King Duras ordered a more vigorous attack south into Moesia'; 'Decebalus was crowned king after the ageing Duras abdicated'. Fix: Start the dossier no later than 85 under Duras (found at 85 or at Duras's accession, conf 2), make Decebalus's accession in 87 a rename, add Duras to rulers; or cut the war to 87-89 (worse, since the 85-86 raids are the war's start).
- `/ledger (new events 89 and 101)` (for the author). Decebalus's client status after Domitian's peace is on the Dacia page but not in the ledger. Evidence: Dacia page: 'Decebalus was given the status of "king client to Rome", receiving military instructors, craftsmen and money from Rome'; the peace follows 'the defeat of Domitian by the Marcomanni' (89). Fix: Add {year 89, type vassal_start, counterpart roman-empire, region Dacia, conf 2, source Dacia page} and {year 101, type vassal_end, counterpart roman-empire, conf 3} before the 101 contest_start; route the mirror to roman-empire.
- `/ledger/4 (and new events 102, 105)` (for the author). The 102 peace ceded territory and made Decebalus a client again; /ledger/4's note quotes 'He surrenders territory' but no loss is recorded. Evidence: Trajan's Dacian Wars page: 'The treaty forced him to surrender territory' and to 'accept Roman garrisons'; Decebalus page: 'the loss of some territories in the vicinity of the Danube and the dismantling of his fortresses' and 'He remained in power as a client king'. Fix: Add {year 102, type loss, counterpart roman-empire, region: the Danube-side lands (a reading such as Banat and Oltenia, text 'some territories in the vicinity of the Danube'), conf 2}, {year 102, vassal_start, roman-empire} and {year 105, vassal_end, roman-empire} before the 105 contest_start; add keyframe dacian-kingdom_102 without the ceded land; route the 102 gain to roman-empire.

Spot checks:

- `/ledger/3` https://en.wikipedia.org/wiki/Trajan%27s_Dacian_Wars: confirmed: 'Trajan's First Dacian War began in 101 CE'
- `/ledger/4` https://en.wikipedia.org/wiki/Trajan%27s_Dacian_Wars: confirmed: 'In 102 Decebalus chose to make peace'; 'The treaty forced him to surrender territory'
- `/ledger/5` https://en.wikipedia.org/wiki/Trajan%27s_Dacian_Wars: confirmed: 'In 105, Trajan launched the' second war, 'crossing on the great stone bridge at Drobeta'
- `/ledger/6` https://en.wikipedia.org/wiki/Trajan%27s_Dacian_Wars: confirmed: 'presumably during the summer of 106'; the city 'fell and was razed'; Decebalus 'committed suicide'
- `/ledger/7` https://en.wikipedia.org/wiki/Dacia: confirmed: infobox 'Disestablished: 106 AD'; 'the Roman province Dacia Traiana'
- `/ledger/1` https://en.wikipedia.org/wiki/Decebalus: confirmed: 'In 88 Julianus ... defeating them in a battle near Tapae'

## bar-kokhba-state: fix

Findings:

- `/wars/0/to` (applied by reviewer). The war ran to 136 while the state ends in 135 (wars must lie inside the life). Evidence: Bar Kokhba revolt page: 'the conflict persisted at least until January 136'; dossier end 135 (fall of Betar). Fix: War end set to 135; the 136 tail stays in the note.

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Bar_Kokhba_revolt: confirmed: 'likely erupted in the summer of 132 CE'; 'the Jewish rebels had established an independent state'; 'held all of Judea proper'
- `/ledger/1` https://en.wikipedia.org/wiki/Bar_Kokhba_revolt: confirmed: Betar 'came under siege in the summer of 135' and 'was captured and destroyed'

## jewish-provisional-government: fix

Findings:

- `/wars/0/to` (applied by reviewer). The war ran to 74 while the state ends in September 70. Evidence: First Jewish-Roman War page: Jerusalem 'fell in the summer of 70'; 'the fall of Masada in 73/74'; dossier end 70-9. Fix: War end set to 70; the holdouts to 73/74 are the roman-empire dossier's war.

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/First_Jewish%E2%80%93Roman_War: confirmed: 'After Gallus' defeat, a popular assembly convened at the Jerusalem Temple and established a provisional government'; districts listed
- `/ledger/1` https://en.wikipedia.org/wiki/First_Jewish%E2%80%93Roman_War: confirmed: base at Akko-Ptolemais 'In early summer of 67'; Yodfat 'fell in June or July'; Gamla 'in late October'
- `/ledger/2` https://en.wikipedia.org/wiki/First_Jewish%E2%80%93Roman_War: confirmed: 'In spring 68, Vespasian systematically subdued settlements en route to Jerusalem'
- `/ledger/3` https://en.wikipedia.org/wiki/Siege_of_Jerusalem_(70_CE): confirmed: infobox '13 April - 8 September 70 CE'; 'By early September, the conquest of Jerusalem was complete'

## marcellinus-dalmatia: fix

Findings:

- `/ledger/2; /identity/end; /keyframe_review/0/to; /identity/capitals/0/to; /identity/rulers/1/to; /certainty/0/to; /identity/successors/0` (applied by reviewer). The dissolve was dated 28 August 475 (Nepos's flight to Salona) although the author's own note says Dalmatia ceased to be separate when Nepos became western emperor on 24 June 474. Evidence: Julius Nepos page: 'On 24 June, having deposed Glycerius, Nepos was proclaimed the western Augustus in Rome'; infobox 'In Italy: 24 June 474 - 28 August 475'. Fix: End, dissolve, keyframe, capital, ruler and certainty spans moved to 474 (month 6); note and notes updated. The western-roman-empire dossier needs a 474 gain of Dalmatia (its keyframe adds Dalmatia only from 476).

Thin (for a gap-filler):

- `/ledger`: the page has Marcellinus 'briefly accepting the authority of the Emperors Majorian and Anthemius' (allegiance December 457; with Anthemius 467-468): optional vassal tints with western-roman-empire Try https://en.wikipedia.org/wiki/Majorian

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Marcellinus_(magister_militum): confirmed: 'first mention his name in 454 when he rebelled against Western Emperor Valentinian III'; 'powerful enough to seize control of Dalmatia for himself'
- `/ledger/1` https://en.wikipedia.org/wiki/Marcellinus_(magister_militum): confirmed: 'Marcellinus was murdered in Sicily that same year [468], possibly by Ricimer's order'; Nepos page: Nepos 'inherited this position'
- `/ledger/2` https://en.wikipedia.org/wiki/Julius_Nepos: mis-dated: the page puts Nepos's accession as western Augustus on 24 June 474; fixed to 474

## eugenius-usurpation: pass

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Eugenius: confirmed: 'elevated to augustus on 22 August 392 at Lyons, by Arbogast'; infobox 'Reign: 22 August 392 - 6 September 394'
- `/ledger/1` https://en.wikipedia.org/wiki/Eugenius: confirmed: 'into Italy in the spring of 393'
- `/ledger/2` https://en.wikipedia.org/wiki/Battle_of_the_Frigidus: confirmed: 'fought on 5 and 6 September 394', 'near the Julian Alps'
- `/ledger/3` https://en.wikipedia.org/wiki/Battle_of_the_Frigidus: confirmed: Eugenius 'was beheaded'; Arbogast 'committed suicide'
- `/ledger/4` https://en.wikipedia.org/wiki/Battle_of_the_Frigidus: confirmed: infobox 'Theodosius gains Western Empire'

Tried and could not break: page dates and places of every confidence-3 event, keyframe-to-ledger consistency, capital inside the shape, wars inside the life, mirrors in the counterpart dossiers.

## maximus-usurper: fail

Findings:

- `/ledger (new events in 411)` (for the author). Gerontius's 411 conquests in southern Gaul are missing although two neighbour dossiers record them as maximus-usurper's land. Evidence: Gerontius page: in 411 he 'successfully besieged and captured Constans in' Vienne and then 'besieged Constantine' at Arles. constantine-iii-usurper /ledger/7: 411 loss to maximus-usurper (Gaul); western-roman-empire /ledger/12: 411 gain from maximus-usurper (Gaul). Fix: Add {year 411, type gain, counterpart constantine-iii-usurper, region as constantine-iii-usurper /ledger/7, conf 2, source Gerontius page} and its loss to western-roman-empire later in 411 (Constantius's arrival), with a keyframe for the Gaulish holding; or agree with both neighbours that Gerontius's army did not count as Maximus's realm and have them change their counterparts.
- `/ledger/1/counterpart` (for the author). The 411 dissolve names nobody, while western-roman-empire /ledger/13 (411) and /ledger/17 (414) record gains of north-eastern Hispania from maximus-usurper. Evidence: Maximus of Hispania page: after Gerontius's death Maximus 'reportedly fled to sanctuary' 'amongst the barbarians in Hispania'; western-roman-empire /ledger/13: 411 gain cp maximus-usurper (conf 1). Fix: Name western-roman-empire as the dissolve counterpart for the part Honorius took (and say that the rest went to the Vandals, Alans and Suebi), or have the western-roman-empire dossier change its counterpart; the two must agree.

Thin (for a gap-filler):

- `/ledger/1`: the end of Maximus's realm is conf 1; the pages disagree (Maximus page: installed late summer 410, infobox reign 409-417) Try https://en.wikipedia.org/wiki/Constantine_III_(Western_Roman_emperor)
- `/keyframe_review/0`: the whole of Hispania is a maximum that overlaps the Vandal, Alan and Suebian lands of 409-411 Try https://en.wikipedia.org/wiki/Kingdom_of_the_Suebi

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Gerontius_(magister_militum): confirmed: 'In late spring 409, Gerontius rebelled against Constantine' and 'appointed Maximus as emperor'; 'He moved to Tarraco'
- `/ledger/1` https://en.wikipedia.org/wiki/Maximus_of_Hispania: confirmed as conf 1: Gerontius killed himself; Maximus 'fled to sanctuary' among the barbarians; the page does not date it to 411

## jovinus-usurper: thin

Thin (for a gap-filler):

- `/keyframe_review/0`: extent: 'Gaul' within the 406 Western Roman shape is a maximum that overlaps the western-roman-empire dossier's own Gaul from 411 (its /ledger/12 and /ledger/14) and the Visigoths from 412-413; a page placing Jovinus's rule (Rhineland, Mainz, the Burgundian left bank) would cut it Try https://en.wikipedia.org/wiki/Constantine_III_(Western_Roman_emperor)
- `/ledger/0`: the found counterpart is western-roman-empire, but much of Gaul in 411 was Constantine III's until his fall in September 411; the western-roman-empire dossier has no 411 loss or 413 gain for jovinus-usurper Try https://en.wikipedia.org/wiki/Gundahar

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Jovinus: confirmed: 'proclaimed emperor at Mainz in 411', backed by Gundahar and Goar; 'kept his position in Gaul for two years' (the note's 'held Gaul for about two years' is a paraphrase)
- `/ledger/1` https://en.wikipedia.org/wiki/Jovinus: confirmed: Ataulf 'allied his Visigoths with Honorius'; Jovinus 'besieged and captured in Valentia'; infobox 'Died: 413 Narbonne'

## macrianus-and-quietus: fix

Findings:

- `/identity/capitals; /ledger/1 (new capital_move)` (applied by reviewer). The capital note said the pages name no seat before 261, but the Odaenathus page names Antioch as Macrianus's centre. Evidence: Odaenathus page: Macrianus 'took Antioch on the Orontes as his center and organized the resistance against Shapur I'; 'In early 261, Fulvius Macrianus headed to Europe ... leaving Quietus and Balista in Emesa'. Fix: Capitals now Antioch 260-261 and Emesa 261-261, with a 261 capital_move (conf 2) at /ledger/1.

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Odaenathus: confirmed: 'declared his sons Quietus and Macrianus Minor as joint emperors in August 260'
- `/ledger/2` https://en.wikipedia.org/wiki/Odaenathus: confirmed: 'In the spring of 261, Fulvius Macrianus arrived in the Balkans but was defeated and killed'; 'The Emesans killed Quietus as Odaenathus approached the city'
- `/keyframe_review/0` https://en.wikipedia.org/wiki/Crisis_of_the_Third_Century: confirmed: 'They quickly took over most of the East (Egypt, Syria and Asia)'

## chatti: fail

Findings:

- `/ledger (new event in 83 or 85); /keyframe_review` (for the author). Domitian's conquest of Chattan territory is on a page the author opened but no loss is recorded; the roman-empire dossier gains 'the Chatti country in Hesse and the Taunus-Wetterau' in 83 while the chatti keyframes keep all of Hesse to 213. Evidence: Germanic Wars page (in this dossier's sources): '82-83, Campaign against the Chatti under Emperor Domitian, Roman armies conquer the territory of Chatti'. roman-empire /ledger/59: 83 gain, counterpart nobody, region Cliopatria 84 minus 83 within Germany. Author's notes: 'the Chatti page does not say'. Fix: Add {year 83 (or 85, the end of the fighting), type loss, counterpart roman-empire, region = the roman-empire /ledger/59 region intersected with Hesse, text 'Taunus and Wetterau', conf 2, source Germanic Wars page}; add a keyframe chatti_85 (or cut chatti_-11 at 83) without that land; ask the roman-empire dossier to name chatti.
- `/ledger (new events -11 and 9)` (for the author). The Roman occupation of Germania (12 BC-AD 9), which covers the Chatti land in the roman-empire dossier, has no mirror here. Evidence: Germanic Wars page: '12-9 BC ... Chatti, Mattiaci, Tencteri and Usipetes are overrun'; '9 ... Roman Empire is forced to strategically withdraw from Germania'. roman-empire /ledger/20 occupation_start -12 and /ledger/26 occupation_end 9, region 'Germania between the Rhine and the Elbe', counterpart nobody. Fix: Add {year -11, occupation_start, counterpart roman-empire, region Hesse, conf 2} and {year 9, occupation_end, counterpart roman-empire, conf 3}; ask the roman-empire dossier to name chatti (and cherusci) instead of nobody.
- `/wars/0/from` (applied by reviewer). Drusus's war began in -12, before the state's first year -11. Evidence: Chatti page: first record 11 or 10 BC; dossier start -11. Fix: War start set to -11, with a reviewer note.

Thin (for a gap-filler):

- `/ledger/0`: start is the first record (11 or 10 BC), conf 1 Try https://en.wikipedia.org/wiki/Chatti
- `/ledger/4`: end 213 is a bridge; 'may have eventually become part of the Franks' (conf 1) Try https://en.wikipedia.org/wiki/Franks

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Chatti: confirmed: 'The first clearly recorded event involving the Chatti was the Sugambri attack upon the Chatti in 11 or 10 BC'
- `/ledger/1` https://en.wikipedia.org/wiki/Chatti: confirmed: Domitian 'celebrated a triumph over them in late 83 or early 84'
- `/ledger/2` https://en.wikipedia.org/wiki/Chatti: confirmed: 'although fighting continued until 85'
- `/ledger/3` https://en.wikipedia.org/wiki/Cherusci: confirmed (conf 1): Chariomerus 'driven out of his kingdom by the neighbouring Chatti during the reign of the emperor Domitian'
- `/ledger/4` https://en.wikipedia.org/wiki/Chatti: confirmed (conf 1): the Chatti 'may have eventually become part of the Franks'

## cherusci: fail

Findings:

- `/ledger (new events -8 or -12, and 9)` (for the author). The Cherusci's subjection to Rome from Drusus's campaigns to the Teutoburg Forest is on the dossier's own page but not in the ledger; the roman-empire dossier occupies their land 12 BC-AD 9 with counterpart nobody. Evidence: Cherusci page: 'Roman writers thereafter treated the Cherusci as a dependent and ostensibly friendly people' (after 8 BC); 'A coalition led by the Cheruscan noble Arminius ambushed and destroyed three Roman legions' (9). Germanic Wars page: '12-9 BC ... Cherusci, Marsi and Sicambri subdued'; '9 ... Roman Empire is forced to strategically withdraw from Germania'. roman-empire /ledger/20 and /ledger/26. Fix: Add {year -8, type vassal_start (or occupation_start at -12 to mirror roman-empire /ledger/20), counterpart roman-empire, region = the cherusci_-58 shape, conf 2, source Cherusci page} and the matching _end in 9 (conf 3); add the Teutoburg Forest to the war zones; ask the roman-empire dossier to name cherusci.

Thin (for a gap-filler):

- `/ledger/0`: first record 58-52 BC, not a founding (conf 1) Try https://en.wikipedia.org/wiki/Cherusci
- `/ledger/3`: end 'during the reign of Domitian (81-96)' set at 96 (conf 1) Try https://en.wikipedia.org/wiki/Chariomerus

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Cherusci: confirmed: 'The Cherusci are first attested in' Caesar's Commentaries; the 'Bacenis Forest'
- `/ledger/1` https://en.wikipedia.org/wiki/Cherusci: confirmed: Germanicus 'led reprisal campaigns from 14 AD to 16 AD'
- `/ledger/2` https://en.wikipedia.org/wiki/Germanic_Wars: confirmed: '17, Cessation of military offensives east of the Rhine by Tiberius'
- `/ledger/3` https://en.wikipedia.org/wiki/Cherusci: confirmed (conf 1): 'After their defeat by the Chatti in the late first century AD, the Cherusci disappear from accounts'

## hermunduri: thin

Findings:

- `/ledger/0/counterpart; /identity/predecessors` (applied by reviewer). The found event named marcomanni as counterpart and predecessor for land the Marcomanni had already left; the marcomanni dossier never holds Franconia and has no mirror loss. Evidence: Marcomanni page: 'the Romans settled the Hermunduri where the Marcomanni had previously been living'; Hermunduri page: Ahenobarbus 'had taken under his protection the Hermunduri, who had left their homeland'. Fix: Counterpart set to nobody and the predecessor link removed, with reviewer notes.

Thin (for a gap-filler):

- `/keyframe_review/2`: Thuringia is added in 51 with no ledger event; the salt-river war of 57 (Werra or Saale, 'possibly') is the only lead and is not a ledger event Try https://en.wikipedia.org/wiki/Hermunduri
- `/ledger/1 and /ledger/2`: Bohemia held 19-51 is a bridge the page does not support (conf 1); mirrors marcomanni /ledger/1 and /ledger/3 Try https://en.wikipedia.org/wiki/Vibilius
- `/ledger/3`: end 180 is the last dated mention (conf 1) Try https://en.wikipedia.org/wiki/Thuringii

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Hermunduri: confirmed: Ahenobarbus 'had taken under his protection the Hermunduri, who had left their homeland' (about 3 BC)
- `/ledger/1` https://en.wikipedia.org/wiki/Hermunduri: confirmed as event (conf 1): 'the Hermundurian Vibilius led the overthrow of the Marcomannic king Catualda'; no land on the page
- `/ledger/2` https://en.wikipedia.org/wiki/Hermunduri: confirmed as event (conf 1): 'Around 50 AD, Vibilius deposed Vannius'
- `/ledger/3` https://en.wikipedia.org/wiki/Hermunduri: confirmed (conf 1): the Hermunduri 'within the alliance of the Marcomanni, the Sarmatians, and the Quadi' (180)

## tarcondimotid-kingdom: fail

Findings:

- `/ledger (new events)` (for the author). The kingdom's Roman client status is the page's own description but is not in the ledger. Evidence: Tarcondimotus I page: 'was a Roman client ruler of Upper Cilicia'; Pompey recognised local dynasts as 'client rulers subordinate to Rome'; 'formally recognized as king by Mark Antony c.38 BC'. Fix: Add {year -38, type vassal_start, counterpart roman-republic, conf 2}, the hand-over at -27 (vassal_end roman-republic / vassal_start roman-empire, as kingdom-of-cappadocia /ledger/15-16 does) and {year 17, vassal_end, roman-empire, conf 3} before the dissolve; ask the roman-empire dossier for the mirror (its -27 client list lacks this kingdom).
- `/identity/start; /ledger/0` (for the author). The state held land as a toparchy from Pompey's settlement; -38 is the royal title, a rename under the one-state rule. Evidence: Tarcondimotus I page: 'was confirmed as toparch by Pompey in or after 66 BC'; 'The core of Tarcondimotus' territory comprised the cities of Anazarbus and Castabala'. Fix: Start at about -64 (conf 2) with -38 as a rename; or keep -38 and say in /notes why the toparchy is excluded.

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Tarcondimotus_I: confirmed: 'formally recognized as king by Mark Antony c.38 BC'
- `/ledger/1` https://en.wikipedia.org/wiki/Tarcondimotus_I: confirmed: died at Actium in 31 BC; Octavian stripped Philopator of the royal title, 'though Philopator appears to have retained his position as toparch'
- `/ledger/2` https://en.wikipedia.org/wiki/Tarcondimotus_I: confirmed: 'In 20 BC, Augustus restored the royal title to Tarcondimotus II'
- `/ledger/3` https://en.wikipedia.org/wiki/Tarcondimotus_I: confirmed: 'continued to rule Upper Cilicia until AD 17, when the emperor Tiberius incorporated their territory into the Roman provincial system' (the note's wording is a paraphrase)

## brigantes: fail

Findings:

- `/ledger (new events 43 and 69)` (for the author). The Brigantes' status as a Roman client kingdom under Cartimandua is on two opened pages but not in the ledger. Evidence: Cartimandua page: reign 'c. AD 43 - c. 69'; the Romans 'sent some cohorts to defend their client queen'; 69: 'leaving Venutius in control of a kingdom at war with Rome'. Roman conquest of Britain page: 'the Roman client tribe of the Brigantes who occupied the Pennines'. Fix: Add {year 43, type vassal_start, counterpart roman-empire, region = the brigantes_43 shape, conf 2, source Cartimandua page} and {year 69, type vassal_end, counterpart roman-empire, conf 3}; route the mirror and the 74 gain (counterpart brigantes) to the roman-empire dossier.

Thin (for a gap-filler):

- `/ledger/3 and /ledger/4`: end of the war and annexation bridged to 74 (Cerialis's governorship; conf 1) Try https://en.wikipedia.org/wiki/Quintus_Petillius_Cerialis
- `/ledger/0`: the note quotes 'Her reign is usually dated from this year', which is not on the Cartimandua page (it gives 'c. AD 43'); reword the quote Try https://en.wikipedia.org/wiki/Cartimandua

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Cartimandua: confirmed year: 'reigned c. AD 43 - c. 69'; the quoted phrase 'usually dated from this year' is not on the page
- `/ledger/1` https://en.wikipedia.org/wiki/Cartimandua: confirmed: Venutius's 69 revolt, Cartimandua evacuated
- `/ledger/2` https://en.wikipedia.org/wiki/Roman_conquest_of_Britain: confirmed: 'in 71 Cerialis (governor AD 71-74) waged a successful war against the Brigantes'

## iceni: fail

Findings:

- `/ledger (new events 43 and 60)` (for the author). The Iceni's client-kingdom status after 43 is quoted in the dossier's own war note but not in the ledger. Evidence: Iceni page: 'At that point, the Iceni retained independence as a client kingdom' (43); 47: 'the Iceni were allowed to retain their independence'; at Prasutagus's death 'the procurator Catus Decianus seized his entire estate'. Fix: Add {year 43, type vassal_start, counterpart roman-empire, region = the iceni_-10 shape, conf 2, source Iceni page} and {year 60, type vassal_end, counterpart roman-empire, conf 2} before the contest_start; route the mirror to roman-empire.

Thin (for a gap-filler):

- `/ledger/0`: start is the first coinage, c. 10 BC (conf 1) Try https://en.wikipedia.org/wiki/Iceni
- `/ledger/3`: annexation after the revolt undated ('increasingly incorporated into the Roman province'; conf 1) Try https://en.wikipedia.org/wiki/Prasutagus

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Iceni: confirmed: 'The Iceni began producing coins around 10 BC'
- `/ledger/1` https://en.wikipedia.org/wiki/Roman_conquest_of_Britain: confirmed: Boudica's uprising 'in 60 or 61' (Iceni page: 'took place in AD 61')
- `/ledger/3` https://en.wikipedia.org/wiki/Iceni: confirmed (conf 1): 'the Iceni were increasingly incorporated into the Roman province'

## catuvellauni: thin

Findings:

- `/ledger/2/region; /identity/successors/0/land` (applied by reviewer). The 43 dissolve and the successor land were the 20 BC-AD 8 shape without Essex, though the last keyframe (9-43) includes Essex. Evidence: keyframe catuvellauni_9 correction = KF0 counties plus Essex; dissolve must hand over the whole last shape. Fix: Both set to the catuvellauni_9 keyframe region, with a reviewer note.

Thin (for a gap-filler):

- `/ledger/0`: start is the first coinage at Verlamion, ca 20 BC (conf 1) Try https://en.wikipedia.org/wiki/Tasciovanus
- `/ledger/1`: year and holder of the retaking of Camulodunum unsettled (Tasciovanus or Cunobelinus; conf 1) Try https://en.wikipedia.org/wiki/Cunobeline

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Catuvellauni: confirmed: 'Tasciovanus was the first king to mint coins at Verlamion, beginning ca 20 BC'
- `/ledger/1` https://en.wikipedia.org/wiki/Catuvellauni: confirmed (conf 1): 'Camulodunum was retaken, either by Tasciovanus or by his son Cunobelinus'; Cunobelinus 'succeeded him ca AD 9'
- `/ledger/2` https://en.wikipedia.org/wiki/Roman_conquest_of_Britain: confirmed: 'British resistance was led by Togodumnus and Caratacus, sons of the late king of the Catuvellauni'; Romans 'established their new capital at Camulodunum'

## trinovantes: thin

Thin (for a gap-filler):

- `/ledger/0`: first record before Caesar's invasions, not a founding (conf 1) Try https://en.wikipedia.org/wiki/Mandubracius
- `/ledger/2`: conquest by Tasciovanus or Cunobelinus undated on the page (conf 1) Try https://en.wikipedia.org/wiki/Cunobeline

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Trinovantes: confirmed: 'the Trinovantes were considered the most powerful tribe in Britain'
- `/ledger/1` https://en.wikipedia.org/wiki/Trinovantes: confirmed: Addedomarus 'took power c. 20-15 BC, and moved the tribe's capital to Camulodunum'
- `/ledger/2` https://en.wikipedia.org/wiki/Trinovantes: confirmed (conf 1): 'finally conquered by either Tasciovanus or his son Cunobelinus'; no year

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| britannic-empire 286 found (roman-empire) | roman-empire 286 loss | matched | roman-empire /ledger/102 names 'Britannic Empire (Carausius and Allectus)'; rename the counterpart to britannic-empire (eu-04-a). |
| britannic-empire 293 loss (roman-empire) | - | missing | roman-empire has no 293 gain of the Gallic coast (Carausian Revolt page: 'In 293, Constantius Chlorus ... retaking the territory he held in Gaul'); route to eu-04-a. |
| britannic-empire 296 dissolve (roman-empire) | roman-empire 296 gain | matched | roman-empire /ledger/104; rename the counterpart string. |
| domain-of-magnus-maximus 383 found (roman-empire) | roman-empire 383 loss | matched | roman-empire /ledger/122-123 'Magnus Maximus (usurper)'; rename to domain-of-magnus-maximus. |
| domain-of-magnus-maximus 383 gain (roman-empire) | roman-empire 383 loss | matched | Gaul and Hispania: roman-empire /ledger/122-123. |
| domain-of-magnus-maximus 387 gain (roman-empire) | roman-empire 387 loss | matched | Italy: roman-empire /ledger/124. |
| domain-of-magnus-maximus 388 dissolve (roman-empire) | roman-empire 388 gain | matched | roman-empire /ledger/126-127. |
| alemanni 260 gain (roman-empire) | roman-empire 260 loss | matched | roman-empire /ledger/93 names 'Alemanni'; rename to alemanni. |
| alemanni 277 loss (roman-empire) | roman-empire 277 gain | matched | roman-empire /ledger/100. |
| alemanni 300 gain (roman-empire) | roman-empire 300 loss | matched | roman-empire /ledger/109. |
| alemanni 406 gain (missing) (western-roman-empire) | - | missing | Alemanni page dates the conquest of Alsace to 406; neither alemanni nor western-roman-empire records it (WRE /ledger/50 gives the Rhine region to kingdom-of-alamannia in 462, conf 1). |
| alemanni 461 dissolve (kingdom-of-alamannia) | - | exception | kingdom-of-alamannia is owned by eu-06, which has not run. |
| marcomanni 19 loss (Hermunduri) | hermunduri 19 gain | matched | Both sides conf 1 and unsupported by the pages (see thin); the counterpart string should be the slug hermunduri. |
| marcomanni 20 gain (quadi) | quadi 20 vassal_start | mismatch | Type disagrees: quadi records the Marcomanni exiles as its vassal, marcomanni records a gain of Moravia. Fix on the marcomanni side (vassal_start cp quadi). |
| quadi 50 vassal_end (marcomanni) | - | missing | marcomanni has no 50 vassal_end (its 51 event is a gain from Hermunduri). |
| marcomanni 51 gain (Hermunduri) | hermunduri 51 loss | matched | conf 1 bridge on both sides; slug string 'Hermunduri' should be hermunduri. |
| marcomanni 453 dissolve (danubian-suebi) | - | exception | danubian-suebi has no dossier; listed in counterparts_needing_dossiers (eu-06-x). |
| quadi 20 vassal_start (missing) (roman-empire) | - | missing | Roman client status (Vannius; Vangio and Sido 'loyal Roman client kings') recorded on neither side. |
| kingdom-of-burebista -55 gain (West Pontic Greek cities (Olbia to Apollonia)) | - | exception | No dossier; listed in counterparts_needing_dossiers (eu-01). |
| dacian-kingdom 89 vassal_start (missing) (roman-empire) | - | missing | 'king client to Rome' (Dacia page) recorded on neither side. |
| dacian-kingdom 102 loss (missing) (roman-empire) | - | missing | 102 cession 'some territories in the vicinity of the Danube' recorded on neither side. |
| dacian-kingdom 106 dissolve (roman-empire) | roman-empire 106 gain | matched | roman-empire /ledger/66 names 'Dacians (Dacian kingdom)'; rename to dacian-kingdom. |
| bar-kokhba-state 132 found (roman-empire) | roman-empire 132 contest_start | mismatch | roman-empire has only a contest (/ledger/74) with 'Jewish rebels of Judaea'; it needs a 132 loss of Judea to bar-kokhba-state (eu-04-a). |
| bar-kokhba-state 135 dissolve (roman-empire) | roman-empire 135 contest_end | mismatch | roman-empire /ledger/75 contest_end only; needs a 135 gain from bar-kokhba-state. |
| jewish-provisional-government 66 found (roman-empire) | roman-empire 66 contest_start | mismatch | roman-empire /ledger/49 contest only; needs a 66 loss to jewish-provisional-government. |
| jewish-provisional-government 67 loss (roman-empire) | - | missing | roman-empire has no 67 gain of Galilee and Gaulanitis. |
| jewish-provisional-government 68 loss (roman-empire) | - | missing | roman-empire has no 68 gain of the Judean countryside. |
| jewish-provisional-government 70 dissolve (roman-empire) | roman-empire 70 contest_end | mismatch | roman-empire /ledger/53 contest_end only; needs a 70 gain. |
| marcellinus-dalmatia 454 found (western-roman-empire) | western-roman-empire 455 loss | mismatch | western-roman-empire /ledger/37 (455) gives Illyricum, Dalmatia included, to the ostrogoths (conf 1); it should lose Dalmatia to marcellinus-dalmatia in 454 (eu-04-b). |
| marcellinus-dalmatia 474 dissolve (western-roman-empire) | - | missing | Moved from 475 by the reviewer; western-roman-empire adds Dalmatia only in its 476 keyframe and needs a 474 gain from marcellinus-dalmatia. |
| eugenius-usurpation 392 found (roman-empire) | roman-empire 392 contest_start | mismatch | roman-empire /ledger/128 contest only with 'Eugenius (usurper)'; needs a 392 loss of Gaul. |
| eugenius-usurpation 393 gain (roman-empire) | - | missing | roman-empire has no 393 loss of Italy. |
| eugenius-usurpation 394 dissolve (roman-empire) | roman-empire 394 contest_end | mismatch | roman-empire /ledger/129 contest_end only; needs a 394 gain. |
| maximus-usurper 409 found (constantine-iii-usurper) | constantine-iii-usurper 409 loss | matched | constantine-iii-usurper /ledger/6. |
| maximus-usurper 411 gain (missing) (constantine-iii-usurper) | constantine-iii-usurper 411 loss | missing | constantine-iii-usurper /ledger/7 loses Gaul to maximus-usurper in 411 and western-roman-empire /ledger/12 gains Gaul from it; maximus-usurper never holds Gaul. |
| maximus-usurper 411 dissolve (nobody) | western-roman-empire 411 gain | mismatch | western-roman-empire /ledger/13 (411) and /ledger/17 (414) gain north-eastern Hispania from maximus-usurper; the dissolve names nobody. |
| jovinus-usurper 411 found (western-roman-empire) | - | missing | western-roman-empire has no 411 loss to jovinus-usurper (eu-04-b). |
| jovinus-usurper 413 dissolve (western-roman-empire) | - | missing | western-roman-empire has no 413 gain from jovinus-usurper. |
| macrianus-and-quietus 260 found (roman-empire) | - | missing | roman-empire has no 260 loss of the East to the usurpers (eu-04-a). |
| macrianus-and-quietus 261 dissolve (roman-empire) | palmyrene-empire 261 gain | mismatch | roman-empire has no 261 gain; palmyrene-empire /ledger/2 gains Syria etc. from roman-empire in 261 (conf 1). |
| chatti -11 occupation_start (missing) (roman-empire) | roman-empire -12 occupation_start | mismatch | roman-empire /ledger/20 occupies 'Germania between the Rhine and the Elbe' with counterpart nobody; chatti records nothing. |
| chatti 83 loss (missing) (roman-empire) | roman-empire 83 gain | mismatch | roman-empire /ledger/59 gains 'the Chatti country in Hesse and the Taunus-Wetterau' from nobody; chatti keeps all of Hesse. |
| chatti 96 gain (cherusci) | cherusci 96 dissolve | matched | conf 1 on both sides. |
| cherusci -12 occupation/vassal (missing) (roman-empire) | roman-empire -12 occupation_start | mismatch | roman-empire /ledger/20 and /ledger/26 (counterpart nobody); cherusci records no subjection or Teutoburg. |
| hermunduri -3 found (nobody) | - | exception | Reviewer changed the counterpart from marcomanni to nobody: the Marcomanni had left the land. |
| hermunduri 19 gain (marcomanni) | marcomanni 19 loss | matched | conf 1; see thin. |
| hermunduri 51 loss (marcomanni) | marcomanni 51 gain | matched | conf 1; see thin. |
| tarcondimotid-kingdom 17 dissolve (roman-empire) | - | missing | roman-empire has no AD 17 gain of Upper Cilicia (it has kingdom-of-cappadocia in 18). |
| tarcondimotid-kingdom -38 vassal_start (missing) (roman-republic) | - | missing | client status on the page; neither roman-republic nor roman-empire lists the kingdom. |
| brigantes 43 vassal_start (missing) (roman-empire) | - | missing | client kingdom 43-69 recorded on neither side. |
| brigantes 74 dissolve (roman-empire) | - | missing | roman-empire takes northern England from nobody (Agricola, 78-84) and has no Brigantes event. |
| iceni 43 vassal_start (missing) (roman-empire) | - | missing | client kingdom 43-60 recorded on neither side. |
| iceni 61 dissolve (roman-empire) | roman-empire 61 contest_end | mismatch | roman-empire /ledger/43 contest_end only ('Iceni and allied tribes'); needs a gain from iceni. |
| catuvellauni 9 gain (trinovantes) | trinovantes 9 dissolve | matched | conf 1 on both sides. |
| catuvellauni 43 dissolve (roman-empire) | roman-empire 43 gain | mismatch | roman-empire /ledger/35 gains south-east Britain from nobody; it should name catuvellauni. |

## Problems

- No page failed to load for the reviewer; 33 WebFetch calls, all Wikipedia. WebFetch returns a model summary, so quotes are the summary's.
- Neighbour dossiers: of the 40 Context polities in section 6 of the author's brief, 15 exist (eastern-roman-empire, galatia, greek-city-states, huns, indo-greeks, judea, kingdom-of-cappadocia, kingdom-of-kush, kingdom-of-pontus, kingdom-of-sophene, mauretania, nabataeans, nobatia, sabaeans, thracian-kingdom); none of them is a counterpart of this batch's ledgers. The real counterparts are roman-empire (eu-04-a), western-roman-empire (eu-04-b), constantine-iii-usurper and palmyrene-empire, which are not in the Context table and were read for the matrix; the other 25 Context polities are unwritten (groups not yet run).
- Most reciprocal events belong to roman-empire (eu-04-a) and western-roman-empire (eu-04-b): their counterparts are name strings ('Britannic Empire (Carausius and Allectus)', 'Jewish rebels of Judaea', 'Dacians (Dacian kingdom)', 'Alemanni', 'Eugenius (usurper)', 'Magnus Maximus (usurper)', 'Iceni and allied tribes') or nobody, and they lack gains/losses for bar-kokhba-state, jewish-provisional-government, eugenius-usurpation, macrianus-and-quietus, jovinus-usurper, marcellinus-dalmatia, tarcondimotid-kingdom, brigantes, iceni, catuvellauni (43) and chatti (83). Route to a gap-filler for those two dossiers.
- Reviewer edits applied in place and re-validated (0 errors, 0 warnings): marcellinus-dalmatia, macrianus-and-quietus, kingdom-of-burebista, bar-kokhba-state, jewish-provisional-government, chatti, hermunduri, catuvellauni; each edit is tagged '[Reviewer eu-04-x, 2026-10-19: ...]' in the event, war or capital note.
