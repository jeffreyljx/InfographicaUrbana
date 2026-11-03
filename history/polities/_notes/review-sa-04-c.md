# Review: batch sa-04-c (Bengal, Vijayanagara, Bahmani, Jaunpur, Sayyid, Lodi)

Reviewer brief filled 2026-10-19; review run 2026-10-20. All six dossiers pass the validator (with --resolve, 0 errors). Spot checks: 4 to 9 events per dossier, opened with WebFetch on the pages cited. No confidence-3 event was found fabricated or mis-dated. Every dossier still fails, on keyframe/ledger inconsistencies, on mismatches with batch-mates and neighbours that the author must settle, or on events missing from pages the author opened. The machine copy is history/notes/phase-b/reviews/sa-04-c.json.

Reviewer-applied fixes (re-validated): vijayanagara-empire /ledger/0 counterpart kampili-kingdom to tughlaq-dynasty; jaunpur-sultanate /wars/1 start year 1461 to 1458 (Kapilendra Deva page).

## sultanate-of-bengal: fail

Area: infobox None (None) against Cliopatria 361167 km2, ratio None. The Bengal_Sultanate infobox gives no area

Findings:
- `/ledger/14`: The 1420 gain of 'Bihar (region)' from jaunpur-sultanate leaves no trace in the keyframes, and jaunpur-sultanate has no matching loss or war. Evidence: Bengal_Sultanate: 'The war began in 1415 and ended in 1420.' 'Parts of the Jaunpur Sultanate were annexed by Bengal' (no place named). /keyframe_review/3 (1395-1481) keeps the whole Bihar block out until 1482. jaunpur-sultanate ledger has no 1415-1420 event against Bengal. Fix: Either name a smaller region and add it to the 1395 keyframe from 1420 (split it into 1395-1419 and 1420-1481), or lower to confidence 1 with a small region the shape already holds. Make jaunpur-sultanate carry the 1420 loss and the 1415-1420 contest with the same region.
- `/ledger/23`: The counterpart of the 1482 gain is jaunpur-sultanate, which dissolved in 1479 in its own dossier, so no mirror can exist. Evidence: jaunpur-sultanate /ledger/7 dissolve 1479. Bahlul_Lodi: 'In 1479, Sultan Bahlul Khan Lodi defeated and annexed the Jaunpur Sultanate.' lodi-dynasty has no 1482 loss. Fix: Name lodi-dynasty as the counterpart (lodi-dynasty adds the 1482 loss of the Bihar block), or name the Sharqi rump if jaunpur-sultanate is extended to 1494 (see that dossier's findings).
- `/ledger/10`: The 1395 loss of the Bihar block to Jaunpur disagrees with jaunpur-sultanate /ledger/1, which takes South Bihar from tughlaq-dynasty in the same year. Evidence: Jaunpur_Sultanate: Malik Sarwar 'was also able to bring under his control Kara, Awadh, Dalmau, Bahraich and South Bihar' (no year, no previous holder). Both events are confidence 1. Fix: Agree on one holder with jaunpur-sultanate. Either Jaunpur's 1395 gain names sultanate-of-bengal for the Bihar block, or Bengal's 1352 correction removes the block as Delhi's and this loss is dropped.
- `/ledger (1522-1523)`: A gain is missing. Nasrat Shah's annexation up to the Tons river is on a page the author opened, yet the notes and gaps say no page carries it. Evidence: Nasiruddin_Nasrat_Shah: Nasrat 'annexed the lands up to Tons river soon after 1522', after allying with the Lohani rebels as Lodi authority in Bihar collapsed. Fix: Add a gain c. 1523 (confidence 2), counterpart lodi-dynasty, with a region for Bihar west to the Tons. Add it to the 1519 keyframe correction, and lodi-dynasty adds the loss.
- `/ledger`: No mirrors for neighbour events on Bengal land: kingdom-of-mrauk-u /ledger/3 (1437 gain of Ramu, C2), /ledger/6-8 (1532 gain C3; 1532-1533 occupation of Dhaka, C3); gajapati-kingdom /ledger/1 (1447 gain, C3, of Bengal land west of the Ganga round Medinipur). Evidence: The author's notes name the 1532-33 Arakanese invasion as 'recorded in the kingdom-of-mrauk-u dossier' but do not mirror it. The Bengal_Sultanate page has none of these, so they rest on the neighbours' pages. Fix: Add the matching loss and occupation_start/occupation_end events, citing the neighbours' pages, or say in notes why each is rejected so the neighbour can be corrected.
- `/keyframe_review/5`: The 1497 keyframe keeps the Bihar land west of Barh, which the confidence-3 treaty at /ledger/28 gives to Lodi. The ledger and the keyframe disagree. Evidence: Alauddin_Hussain_Shah: 'the country west of Barh went to Sikandar Lodi' while 'the country east of Barh remained under Husain Shah'; the 1501-02 Hussainabad mosque shows 'firm control of Husain Shah in trans-Gandak area'. The note acknowledges the conflict but leaves the shape uncorrected. Fix: Add a 1496 loss to lodi-dynasty of the land west of Barh and cut it from the 1497 correction. Or keep the shape and rewrite /ledger/28 and /certainty/1 so they no longer call Barh a fixed line.

Thin (for a gap-filler):
- `/ledger/1`: 1346 Nepal raid held as an occupation at confidence 1 though the page dates it; a 3-day sack may not be an occupation at all (try https://en.wikipedia.org/wiki/Shamsuddin_Ilyas_Shah)
- `/ledger/3`: Tirhut 1350: previous holder and extent (southern half, Hajipur) (try https://en.wikipedia.org/wiki/Hajipur)
- `/ledger/22`: vassal_end for Tripura (left open to 1538) (try https://en.wikipedia.org/wiki/Twipra_Kingdom)
- `/ledger/34`: vassal_end for Orissa (left open to 1538) (try https://en.wikipedia.org/wiki/Prataparudra_Deva)
- `/keyframe_review/3`: Bihar block 1395-1482: who held it and when it returned (try https://en.wikipedia.org/wiki/Ibrahim_Shah_Sharqi)

Spot checks: /ledger/4 confirmed; /ledger/5 confirmed; /ledger/21 confirmed; /ledger/29 confirmed; /ledger/34 confirmed; /ledger/38 confirmed; /ledger/13 confirmed; /ledger/16 confirmed; /ledger/22 confirmed

## vijayanagara-empire: fail

Area: infobox 880000 (1500) against Cliopatria 528466 km2, ratio 0.6. 

Findings:
- `/ledger/0` (applied by reviewer): The found event named kampili-kingdom (ended 1327) as its counterpart. tughlaq-dynasty /ledger/15 carries the 1336 loss of this land. Evidence: Vijayanagara_Empire: Kampili 'collapsed after a defeat by the armies of Delhi Sultanate' c. 1327-28, so the land was Delhi's until 1336. Fix: Counterpart set to tughlaq-dynasty and a reviewer note added. Re-validated: 0 errors, 0 warnings.
- `/keyframe_review/6`: The 1492, 1502 and 1507 corrections remove the Raichur doab, but no ledger event loses it after the 1374 gain (/ledger/4). The map therefore holds the doab 1374-1491 and drops it in 1492 with no explanation. Evidence: The contests of 1368-1407 and 1417-1443 end with no outcome. Krishnadevaraya: 'the conquest of the Raichur Doab in 1512'. bahmani-sultanate has no 1374 loss and no later gain of the doab. Fix: Add a loss of the doab to bahmani-sultanate, at the year a page gives (or a confidence-1 bridge, for example 1443), and have Bahmani mirror both the 1374 loss and that gain. Otherwise keep the doab in the 1492-1507 corrections.
- `/keyframe_review/18`: The area falls from 338,405 km2 (the 1564 shape, to 1571) to a 150 km placeholder round Penukonda in 1572, with no loss event. bijapur-sultanate /ledger/12 (1565 gain from vijayanagara-empire, C2) and /ledger/13 (1575 gain, C2) have no mirror here. Evidence: Battle_of_Talikota and Vijayanagara_Empire name no annexed land (checked). The neighbour dossier dates the doab's transfer to 1565. Fix: Add the 1565 loss of the Raichur doab to bijapur-sultanate, citing the Bijapur dossier's page, and 1575. Add confidence-1 losses or vassal_end events for the nayaka lands (Keladi, Mysore, Gingee) that the page lists as becoming independent, so the 1572 drop is explained.
- `/ledger/30`: Both golconda-sultanate /ledger/2 and bidar-sultanate /ledger/2 have 1521 gains (C1) from vijayanagara-empire. This ledger gives the only 1521 loss to gajapati-kingdom, and gajapati-kingdom has no 1521 gain. Evidence: Cliopatria's 1519 to 1521 step drops 107k km2. Krishnadevaraya: 'Krishnadevaraya returned all the lands that the Vijayanagara Empire had captured north of the Krishna River' (no year). Fix: Agree with the golconda-sultanate, bidar-sultanate and gajapati-kingdom dossiers who took which part of the 1521 drop, and add the matching losses here or drop the neighbours' gains.
- `/ledger/11`: The 1436 gain of Kondavidu reads an overlordship as an annexation, and reddi-kingdom /ledger/3 dates the loss to 1424 at confidence 3: a 12-year mismatch. Evidence: Vijayanagara_Empire: 'By 1436 the rebellious chiefs of Kondavidu and the Velama rulers were successfully dealt with and had to accept Vijayanagara overlordship.' Fix: Reconcile with reddi-kingdom. Use a 1424 gain if that dossier's page dates the annexation, or a vassal_start in 1436 (with a vassal_end) if the page means overlordship.
- `/ledger/22`: The 1485 gain (C1) of coastal Andhra, Chittoor, the Arcots, Kolar, Kanchipuram and Tiruchirappalli from gajapati-kingdom misreads the page. Saluva Narasimha held these lands; he did not regain them in 1485. gajapati-kingdom's 1472 loss and 1476 gain against Vijayanagara have no mirror here. Evidence: Vijayanagara_Empire: as governor under Virupaksha Raya II, Saluva 'reduced territorial losses by holding almost all of coastal Andhra Pradesh south of the Krishna river, Chittoor, the two Arcots and Kolar'. Yet /keyframe_review/4-5 remove Kanchipuram as Gajapati-held for 1450-1484. Fix: Revisit the 1450 and 1475 Tamil-town removals and this gain together with gajapati-kingdom /ledger/6-7, and keep only what a page dates.
- `/ledger`: No mirrors for neighbour events: bijapur-sultanate /ledger/6 (1530 gain of Raichur and Mudgal), /ledger/7 (1534 loss), /ledger/8 (1547 gain); english-colonial-empire /ledger/24 (1639 gain of Madras, C3); bijapur-sultanate /ledger/18 (1641 gain of Vellore) against this dossier's 1646 dissolve at Vellore. Evidence: The notes acknowledge only that the Raichur back-and-forth is not modelled. Fix: Add the mirror events, citing the neighbours' pages, or explain in notes why they are rejected.

Thin (for a gap-filler):
- `/keyframe_review/18`: Aravidu extent 1572-1646 (placeholder radii at confidence 1) (try https://en.wikipedia.org/wiki/Aravidu_dynasty)
- `/ledger/31`: Dates of nayaka autonomy (Madurai 1529, Thanjavur 1534 are Cliopatria's steps at confidence 1) (try https://en.wikipedia.org/wiki/Madurai_Nayak_dynasty)
- `/ledger/12`: Jaffna vassalage (decade only; Cliopatria relation 1385-1501) (try https://en.wikipedia.org/wiki/Jaffna_kingdom)
- `/keyframe_review/2`: +141k km2 in 1352 with no dated event (try https://en.wikipedia.org/wiki/Harihara_I)
- `/keyframe_review/14`: 1547 west-coast loss (-3.8k km2) undated; bijapur-sultanate has a 1547 gain (try https://en.wikipedia.org/wiki/Sadasiva_Raya)

Spot checks: /ledger/7 confirmed; /ledger/28 confirmed; /ledger/26 confirmed; /ledger/14 confirmed (year from the Mallikarjuna context, 1446); /ledger/4 confirmed; /ledger/11 confirmed year; the page says overlordship, not annexation; /ledger/20 confirmed; /ledger/22 not on page as claimed (held under Virupaksha II, not regained in 1485; confidence 1)

## bahmani-sultanate: fail

Area: infobox None (None) against Cliopatria 470822 km2, ratio None. The Bahmani_Sultanate infobox gives no area. The author compared the 1352 shape with the 1358 extent on the Alauddin Bahman Shah page

Findings:
- `/keyframe_review/2`: The 1352 correction cuts the realm to the 1358 box for 1352-1374. The next keyframe (1375, verdict ok) restores the full Cliopatria shape, about 210k km2 more (the Konkan west of 75 E and Telangana east of 79.3 E, Warangal included), and no ledger event gains that land. Evidence: Gazetteer resolve: the corrected 1352 shape is 927 cells, about 234,438 km2; the 1375 shape is 1,755 cells, about 443,840 km2; the 1375 shape minus the box is about 211,930 km2. The 1375 shape holds Warangal (12 cells in a 30 km radius), yet the 1352 note says the Warangal country was 'taken 1424-25', and the ledger has only the 1424-1425 contest. Fix: Either carry the box (with dated additions) into the 1375 and 1450 keyframes, or add gain events for the land the 1375 shape adds: Golconda in 1361 (musunuri-nayaks /ledger/3 has that loss), Mohammed Shah I's subjugation of Warangal, and the Konkan.
- `/keyframe_review/3`: The 1450 keyframe (verdict ok) drops the Hyderabad/Telangana block from 1450, but /ledger/11 dates the loss of Telangana to 1458. That loss names the whole 'Telangana (region)', while the 1450 and 1475 shapes still hold Warangal and no event regains it. Evidence: Kapilendra_Deva: battle at Devarakonda in 1458, after which 'the Telangana region became a feudal state of the Gajapati empire with the Velama chiefs as the vassal rulers'. Fix: Set 1450 to adjust and keep the block to 1458. Narrow /ledger/11 to the land the shapes actually drop, or add the regain. Have gajapati-kingdom mirror it (it has no 1458 gain).
- `/ledger (1469)`: A gain on a page the author opened is missing: the Konkan in 1469. /keyframe_review/4 credits the +30k km2 on the west coast to Goa in 1472 only. Evidence: Mahmud_Gawan: 'in 1469, conquering the city of Kanjeeveram and the entire Konkan'. Fix: Add a 1469 gain of the Konkan (confidence 2 or 3; the page names no counterpart, so the local chiefs or nobody), and add the land to the 1450 keyframe's successor from 1469.
- `/ledger`: No mirror for vijayanagara-empire /ledger/4, the 1374 gain (C2) of the Raichur doab from bahmani-sultanate. Both dossiers are in this batch. Evidence: Vijayanagara_Empire: 'By 1374 ... had gained control over Goa in the west and the Tungabhadra-Krishna River doab in the north.' Fix: Add the 1374 loss of the doab, and the later regain the Vijayanagara correction implies (see the vijayanagara-empire finding at /keyframe_review/6).
- `/ledger`: No mirrors for neighbour events: gujarat-sultanate /ledger/5-7 (1429-1431 contest and the 1431 gain of Thane and Mahim); khandesh-sultanate /ledger/3-4 (1435 gain of Berar, C3; 1437 loss); recherla-nayaks /ledger/1 (1435 dissolve into Bahmani of Telangana, Warangal and Rachakonda); musunuri-nayaks /ledger/3 (1361 loss of Golconda); gajapati-kingdom /ledger/5 (1472 loss of Rajahmundry and Kondavidu to Bahmani). Evidence: The notes list the Gujarat and Khandesh wars as recorded in those dossiers but do not mirror them. Fix: Add the mirror events, citing the neighbours' pages, or say in notes why each is rejected.

Thin (for a gap-filler):
- `/identity/rulers`: No ruler list (the sultan table did not come through) (try https://en.wikipedia.org/wiki/List_of_Bahmani_sultans)
- `/keyframe_review/2`: Extents 1359-1449 (unverified: page budget) (try https://en.wikipedia.org/wiki/Mohammed_Shah_I)
- `/ledger/1`: Kaulas position approximate (try https://en.wikipedia.org/wiki/Kaulas)

Spot checks: /ledger/0 confirmed (3 August 1347); /ledger/7 confirmed; /ledger/15 confirmed (February 1472); /ledger/16 confirmed; /ledger/11 confirmed (1458; a Gajapati feudal state, not said to be Bahmani land); /ledger/8 confirmed (1429; Ahmad Shah page 1432, noted)

## jaunpur-sultanate: fail

Area: infobox None (None) against Cliopatria 159344 km2, ratio None. The Jaunpur_Sultanate infobox gives no area

Findings:
- `/wars/1` (applied by reviewer): The Gajapati war was dated 1461. The page the note cites puts Husain Sharqi's invasion of Orissa in 1458. Evidence: Kapilendra_Deva: the Jaunpur Sultanate 'twice invaded Orissa', the second time 'in 1458 by Husain Shah', which is linked to the Gajapati withdrawal from the 1461 Berar campaign. Fix: Start year set to 1458 (end stays 1461) and the outcome and note rewritten. Re-validated: 0 errors, 0 warnings.
- `/ledger`: The Bengal-Jaunpur war of 1415-1420 and its loss of land are missing; sultanate-of-bengal /ledger/13-15 in this batch carries them. Evidence: Bengal_Sultanate: 'The war began in 1415 and ended in 1420.' 'Parts of the Jaunpur Sultanate were annexed by Bengal'. Jaunpur_Sultanate: Ibrahim Shah's 'attempt to conquer Bengal also failed'. Fix: Add contest_start 1415 and contest_end 1420 against sultanate-of-bengal, a 1420 loss with the region agreed with Bengal, and the war.
- `/ledger/1`: The 1395 gain of South Bihar from tughlaq-dynasty disagrees with sultanate-of-bengal /ledger/10, which loses the Bihar block to Jaunpur in 1395. Evidence: Jaunpur_Sultanate names no previous holder of South Bihar. Both events are confidence 1. Fix: Agree with the Bengal dossier on one holder, and split the counterpart if the Bihar block was Bengal's.
- `/identity/end`: The end in 1479 conflicts with two batch-mates. lodi-dynasty /ledger/4 (1497, Bihar 'from the Sharqis') and sultanate-of-bengal /ledger/23 (1482) name jaunpur-sultanate as counterpart after its dissolve. Evidence: Jaunpur_Sultanate infobox: 'Disestablished: 1494'; 'In 1494, Sultan Hussain Shah Sharqi was defeated' at Benares; 'Sharqi inscriptions in Bihar continued until 1505'. Lodi_dynasty: Sikandar's 'conquest and annexation of Bihar from the Sharqis'. Fix: Decide in one place. Either extend the dossier to 1494 with a rump keyframe in Bihar (and move /ledger/7), or keep 1479 and have lodi-dynasty and sultanate-of-bengal name another counterpart. Record the choice in notes.
- `/ledger/3`: No mirror in lodi-dynasty for the 1457 loss of Shamsabad. Both dossiers are in this batch. Evidence: Jaunpur_Sultanate: Muhammad Shah 'made peace with Bahlul Lodi and recognised his right over Shamsabad' (1457). Fix: lodi-dynasty adds a 1457 gain of Shamsabad, counterpart jaunpur-sultanate, confidence 2.

Thin (for a gap-filler):
- `/keyframe_review/1`: Extent changes 1395-1479 (one shape for 85 years); the Bihar frontier with Bengal (try https://en.wikipedia.org/wiki/Ibrahim_Shah_Sharqi)

Spot checks: /ledger/0 confirmed (1394); /ledger/3 confirmed (1457); /ledger/8 confirmed (March 1479, seven parganas); /ledger/7 confirmed (1479); /ledger/1 confirmed undated (confidence 1 right); /wars/1 mis-dated (1458, not 1461); fixed

## sayyid-dynasty: fail

Area: infobox None (None) against Cliopatria 88975 km2, ratio None. The Sayyid_dynasty infobox gives no area

Findings:
- `/ledger`: The dynasty's own vassalage to the Timurids is missing. The notes keep it out on the view that vassal events are only for the state's own vassals, but rule 3 has the vassal's ledger carry a vassal_start with the suzerain as counterpart. Evidence: Khizr_Khan: he took no royal title out of 'fear of invasion by Amir Timur', 'continued to pay him tribute', and in 1417 'obtained permission from Shah Rukh to have his own name also suffixed to that of Shah Rukh'. Fix: Add vassal_start 1414 (counterpart timurid-empire, confidence 2, Khizr Khan page) and a vassal_end at the year a page gives for Mubarak Shah dropping the allegiance (or a confidence-1 bridge). Ask timurid-empire to mirror.
- `/ledger/2`: The 1414 gain of Multan from timurid-empire has no mirror. Multan was the founder's own base, not land gained in 1414. Evidence: Sayyid_dynasty: in 1398 Timur appointed Khizr Khan 'deputy of Multan in Punjab' with charge of Lahore, Dipalpur, Multan and upper Sindh. Khizr_Khan: 'Abdur Rahman received the fiefs of Multan and Fatehpur' (undated). timurid-empire has no 1414 loss. Fix: Fold Multan (and Lahore and Dipalpur, if kept) into the found event and the 1414 keyframe correction, or keep the gain with a counterpart whose dossier mirrors it.
- `/ledger/5`: The 1443 loss of Multan to langah-sultanate is two years off langah-sultanate /ledger/0 (found 1445, C3). Evidence: Sayyid_dynasty: 'Multan became independent under the Langahs during his rule' (Muhammad Shah, 1434-1443). Fix: Align the year with langah-sultanate (1445), or note why the Sayyid page's reign bound is preferred.

Thin (for a gap-filler):
- `/keyframe_review/1`: Extent of the Sayyid realm (Doab, Mewat, Etawah, Lahore, Dipalpur) - page silent (try https://en.wikipedia.org/wiki/Mubarak_Shah_(Sayyid_dynasty))
- `/wars`: Sayyid-Jaunpur wars 1400s-1440s (try https://en.wikipedia.org/wiki/Ibrahim_Shah_Sharqi)

Spot checks: /ledger/1 confirmed (28 May 1414); /ledger/3 confirmed (July 1416, 'annexed both the regions'); /ledger/4 confirmed (1418); /ledger/6 confirmed (19 April 1451 in text, 20 April in infobox); /ledger/2 no year on page (grant undated)

## lodi-dynasty: fail

Area: infobox None (None) against Cliopatria 441658 km2, ratio None. The Lodi_dynasty infobox gives no area

Findings:
- `/ledger/4`: The 1497 gain of Bihar names jaunpur-sultanate as counterpart, a state that dissolved in 1479, and the year is Cliopatria's step, not a page's. Evidence: Lodi_dynasty: Sikandar's 'conquest and annexation of Bihar from the Sharqis' (undated). Jaunpur_Sultanate: 'In 1494, Sultan Hussain Shah Sharqi was defeated'. Fix: Date it 1494 (confidence 2, Jaunpur page) and adjust the 1487 keyframe from 1494. Use a counterpart that matches the end jaunpur-sultanate settles on.
- `/wars`: The 1496 Bengal campaign and the Barh treaty are missing (sultanate-of-bengal /ledger/27-28, confidence 3, in this batch), and /certainty/0 calls the treaty undated. Evidence: Alauddin_Hussain_Shah: 'an expedition against Bengal in 1496 by Sultan Sikandar Lodi'; 'the country west of Barh went to Sikandar Lodi'. Fix: Add the war, contest_start and contest_end 1496 against sultanate-of-bengal, and any gain west of Barh. Cite the Barh line in certainty.
- `/ledger`: No mirror for jaunpur-sultanate /ledger/3, the 1457 loss of Shamsabad. Evidence: Jaunpur_Sultanate: Muhammad Shah 'recognised his right over Shamsabad'. Fix: Add a 1457 gain of Shamsabad, counterpart jaunpur-sultanate, confidence 2.
- `/ledger`: The losses to Bengal are missing: the Bihar block in 1482 (if sultanate-of-bengal /ledger/23 takes lodi-dynasty as counterpart) and Nasrat Shah's annexation up to the Tons river soon after 1522. Evidence: Nasiruddin_Nasrat_Shah: 'annexed the lands up to Tons river soon after 1522'. Fix: Add the losses to sultanate-of-bengal, agreed with the Bengal dossier, and remove the land from the 1519-1526 corrections.

Thin (for a gap-filler):
- `/ledger/13`: Bahar Khan Lohani's independence in Bihar: year and extent (page undated) (try https://en.wikipedia.org/wiki/Bahar_Khan_Lohani)
- `/ledger/7`: Capital move to Agra: year (page: 'Sometime later' after 1504) (try https://en.wikipedia.org/wiki/Agra)
- `/keyframe_review/5`: Eastern territory 1519-1526 (Awadh, Jaunpur, Bihar) kept on the pages' silence (try https://en.wikipedia.org/wiki/Ibrahim_Lodi)

Spot checks: /ledger/2 confirmed (1479); /ledger/6 confirmed (1501); /ledger/8 confirmed (December 1508); /ledger/11 confirmed (1518); /ledger/14 confirmed (1524; Panipat page lists Jhelum, Sialkot, Kalanaur, Dipalpur); /ledger/15 confirmed (21 April 1526)

## Cross-dossier matrix (missing and mismatched only)

- sultanate-of-bengal 1346 occupation_start kathmandu -> missing: kathmandu (sa-04-a) has no 1346 occupation by Bengal
- sultanate-of-bengal 1350 gain tughlaq-dynasty -> missing: Tirhut; tughlaq-dynasty has no 1350 loss (confidence 1 both ways)
- sultanate-of-bengal 1353 occupation_start tughlaq-dynasty -> missing: tughlaq-dynasty has no occupation of Pandua 1353-1355 (C3 here)
- tughlaq-dynasty 1339 loss sultanate-of-bengal -> mismatch: sultanate-of-bengal 1342 found; Tughlaq loses Bengal to sultanate-of-bengal in 1339; Bengal starts 1342 and names lakhnauti-sultanate
- sultanate-of-bengal 1395 loss jaunpur-sultanate -> mismatch: jaunpur-sultanate 1395 gain; Jaunpur gains South Bihar from tughlaq-dynasty, not from Bengal
- sultanate-of-bengal 1420 gain jaunpur-sultanate -> missing: Same batch: jaunpur-sultanate has no 1415-1420 war or 1420 loss
- sultanate-of-bengal 1430 vassal_start kingdom-of-mrauk-u -> missing: mrauk-u has no vassal_start 1430
- kingdom-of-mrauk-u 1437 gain sultanate-of-bengal -> missing: Ramu; Bengal has no 1437 loss
- sultanate-of-bengal 1482 gain jaunpur-sultanate -> mismatch: Counterpart dissolved 1479; should be lodi-dynasty (no 1482 loss there) or a Sharqi rump
- gajapati-kingdom 1447 gain sultanate-of-bengal -> missing: Medinipur, C3 in gajapati; Bengal has no loss
- sultanate-of-bengal 1496 contest_start lodi-dynasty -> missing: Same batch: lodi-dynasty has no 1496 Bengal campaign
- sultanate-of-bengal 1515 vassal_start gajapati-kingdom -> missing: gajapati-kingdom has no vassal_start to Bengal
- sultanate-of-bengal 1523 gain lodi-dynasty -> missing: Nasrat Shah to the Tons river soon after 1522 (Nasrat page); neither dossier has it
- kingdom-of-mrauk-u 1532 occupation_start sultanate-of-bengal -> missing: Dhaka 1532-1533 (C3 in mrauk-u); Bengal has none
- vijayanagara-empire 1374 gain bahmani-sultanate -> missing: Same batch: Raichur doab; bahmani has no 1374 loss
- reddi-kingdom 1424 loss vijayanagara-empire -> mismatch: vijayanagara-empire 1436 gain; 12 years apart; Vijayanagara page says overlordship by 1436
- vijayanagara-empire 1440 vassal_start jaffna-kingdom -> missing: jaffna-kingdom (sa-04-b) has no vassal_start
- vijayanagara-empire 1446 loss gajapati-kingdom -> missing: Tamil towns; gajapati-kingdom has no 1446 gain
- gajapati-kingdom 1472 loss vijayanagara-empire -> missing: Udayagiri, C1; Vijayanagara has no 1472 gain
- gajapati-kingdom 1476 gain vijayanagara-empire -> missing: C1; Vijayanagara has no 1476 loss
- vijayanagara-empire 1485 gain gajapati-kingdom -> missing: C1 bridge; page says Saluva held, not regained
- vijayanagara-empire 1521 loss gajapati-kingdom -> missing: gajapati has no 1521 gain
- golconda-sultanate 1521 gain vijayanagara-empire -> mismatch: vijayanagara-empire 1521 loss; Vijayanagara gives its 1521 loss to gajapati, not golconda
- bidar-sultanate 1521 gain vijayanagara-empire -> mismatch: vijayanagara-empire 1521 loss; Vijayanagara gives its 1521 loss to gajapati, not bidar
- bijapur-sultanate 1530 gain vijayanagara-empire -> missing: Raichur and Mudgal; not modelled here
- bijapur-sultanate 1534 loss vijayanagara-empire -> missing: not modelled here
- bijapur-sultanate 1547 gain vijayanagara-empire -> missing: C1; the 1547 keyframe drops 3.8k km2 unexplained
- bijapur-sultanate 1565 gain vijayanagara-empire -> missing: Post-Talikota; Vijayanagara records only the Hampi occupation
- bijapur-sultanate 1575 gain vijayanagara-empire -> missing: 
- english-colonial-empire 1639 gain vijayanagara-empire -> missing: Madras grant, C3; outside the Vellore placeholder
- bijapur-sultanate 1641 gain vijayanagara-empire -> mismatch: vijayanagara-empire 1646 dissolve; Vellore 1641 in bijapur against the 1646 end at Vellore here
- vijayanagara-empire 1646 dissolve bijapur-sultanate -> mismatch: bijapur-sultanate 1648 gain; 2 years apart (Gingee 1648)
- bahmani-sultanate 1350 gain musunuri-nayaks -> missing: Kaulas; musunuri has a 1361 loss of Golconda instead, which Bahmani lacks
- musunuri-nayaks 1361 loss bahmani-sultanate -> missing: Golconda
- gujarat-sultanate 1431 gain bahmani-sultanate -> missing: Thane and Mahim after the 1429-1431 contest
- khandesh-sultanate 1435 gain bahmani-sultanate -> missing: Berar, C3
- recherla-nayaks 1435 dissolve bahmani-sultanate -> missing: Telangana, Warangal and Rachakonda into Bahmani
- bahmani-sultanate 1458 loss gajapati-kingdom -> missing: gajapati-kingdom has no 1458 gain or vassal for Telangana
- gajapati-kingdom 1472 loss bahmani-sultanate -> missing: Rajahmundry and Kondavidu, C1
- jaunpur-sultanate 1457 loss lodi-dynasty -> missing: Same batch: Shamsabad; lodi-dynasty has no 1457 gain
- lodi-dynasty 1497 gain jaunpur-sultanate -> mismatch: jaunpur-sultanate 1479 dissolve; Counterpart dissolved 1479; Bihar from the Sharqis 1494 per Jaunpur page
- sayyid-dynasty 1414 gain timurid-empire -> missing: Multan; timurid has no 1414 loss; Multan was Khizr Khan's own charge
- sayyid-dynasty 1414 vassal_start timurid-empire (missing) -> missing: Neither dossier records the Sayyid allegiance to the Timurids
- sayyid-dynasty 1443 loss langah-sultanate -> mismatch: langah-sultanate 1445 found; 2 years apart

## Problems

- No page failed to load. The Bengal_Sultanate, Bahmani_Sultanate, Jaunpur_Sultanate, Sayyid_dynasty and Lodi_dynasty infoboxes give no area, so only Vijayanagara has an area ratio.
- Two small fixes applied and re-validated: vijayanagara-empire /ledger/0 counterpart (kampili-kingdom to tughlaq-dynasty) and jaunpur-sultanate /wars/1 start year (1461 to 1458). All six dossiers still fail on findings left to the author.
- The author's report and notes say no page opened carries Nasrat Shah's annexation up to the Tons river. The Nasiruddin_Nasrat_Shah page, which the author opened, has it ('soon after 1522').
- Batch-internal mismatches (Bengal-Jaunpur 1395/1420/1482, Bengal-Lodi 1496/1523, Jaunpur-Lodi 1457/1497, Vijayanagara-Bahmani 1374 and the doab regain) need one author pass across the batch.
- Neighbour conflicts to route: timurid-empire /ledger/53 and mughal-empire /ledger/1 both gain the Lodi realm in 1526. mughal-empire /ledger/2 (1527), bijapur-sultanate /ledger/1 (1504) and golconda-sultanate /ledger/1 (1518) take land from states that ended before those years.
- Neighbour dossiers not yet written (not faults): nayaks-of-madurai, nayaks-of-thanjavur (sa-05), portuguese-colonies (sa-06).
