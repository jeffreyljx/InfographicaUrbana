# Review of batch eu-05-x (Byzantium additions), 2026-10-19

Reviewer: adversarial review of 16 new-state dossiers (no Cliopatria rows). Validator: all 16 pass with 0 errors (also --resolve; warnings: Sutri, Rethymno unknown places; 'navarrese-company' has no dossier). Spot checks: 3-11 events per dossier on the cited Wikipedia pages, weighted to confidence 3 and the largest land moves; no event was found fabricated or mis-dated. Small fixes were applied in place by the reviewer and re-validated; the machine copy of this review is history/notes/phase-b/reviews/eu-05-x.json.

Verdicts: exarchate-of-ravenna **fix**, despotate-of-the-morea **fail**, kingdom-of-candia **fix**, hospitaller-rhodes **thin**, lordship-of-chios **thin**, maona-of-chios **thin**, gattilusi **fix**, catepanate-of-italy **fix**, acciaioli-duchy-of-athens **fix**, spania **fix**, venetian-modon-and-coron **fix**, lordship-of-argos-and-nauplia **pass**, marquisate-of-bodonitsa **pass**, lordship-of-salona **pass**, sclaviniae-of-greece **thin**, emirate-of-tarsus **fix**.

## exarchate-of-ravenna: fix
- APPLIED `/keyframe_review/0/to`: No keyframe covered 640 (the 584 shape ended 639 and the next began 641), so the Exarchate had no shape in 640. Evidence: Exarchate of Ravenna page: Liguria 'completely lost in 640 to the Lombards'; Rothari page: Genoa taken in 641. Ledger /ledger/1 (640) and /ledger/2 (641). Fix: Set 'to' 639 -> 640 and appended a reviewer note. Re-validated: 0 errors.
- THIN `/ledger/5, /ledger/6, /ledger/7`: Confidence-1 bridging events at 740: the recovery of the Pentapolis after Liutprand's 727 campaign, and the years Rome (the pope 'the real master') and Naples/Calabria ('overrun by' Benevento) left the Exarchate. (try https://en.wikipedia.org/wiki/Duchy_of_Rome)
- THIN `/keyframe_review/0 (584-640)`: Agilulf's conquests of 601-603 (Padua, Monselice, Cremona, Mantua) fall inside the 584 shape, which draws the whole 'Venetia' region until 641 and relies on the renderer to subtract Lombard land; no ledger event moves them. (try https://en.wikipedia.org/wiki/Agilulf)
- THIN `/ledger (727-740)`: Liutprand page: Ravenna 'at least temporarily under the Lombard king's control in 728' and occupied again in the mid-730s until Gregory III's allies 'expelled the Lombards from Ravenna'; Pope Zachary 'was ceded additional land around Ravenna and two-third of Cesena' (undated). Not in the ledger. (try https://en.wikipedia.org/wiki/Liutprand,_King_of_the_Lombards)
- Spot-checked and confirmed: /ledger/1, /ledger/8, /keyframe_review/2, /ledger/3, /ledger/4.
- Area: Infobox gives no area (read); KF0 note says so.

## despotate-of-the-morea: fail
- TO DO `/keyframe_review/0/correction`: The 1349-1417 shape is a 75 km circle round Sparti, which swallows land the dossier itself and its neighbours give to others: Venetian Coron (52 km from Sparti), Modon (70 km) and Navarino (68 km), the Lordship of Argos and Nauplia (Argos 67 km, Nauplia 63 km) and Achaean Messenia and Arcadia (Kalamata 29 km, Kyparissia 70 km). Evidence: Distances computed from the dossiers' own coordinates. The dossier's ledger gains Messenia only in 1418 (/ledger/7) and the Arcadia barony (Kyparissia) only in 1432 (/ledger/9), and loses Argos to Venice on 11 June 1394 (/ledger/2, confirmed on the Lordship of Argos and Nauplia page); venetian-modon-and-coron holds Modon and Coron from 1206 and lordship-of-argos-and-nauplia holds the Argolid to 1388. KF0's own text is only 'Mystras, Monemvasia and Grand Magne (Mani)'. Fix: Draw the nucleus the text names (for example Sparti 40 km + Monemvasia 20 km + the Mani), or keep the circle as {'minus': [Sparti 75 km, union(Kalamata 45 km, Kyparissia 25 km, Modon and Coron points, the Argolid (22.77, 37.6, 25 km))]}; say in the note that Karytaina (1320) is not drawn.
- TO DO `/keyframe_review/1/correction; /keyframe_review/2/correction; /keyframe_review/3/correction`: The 1418, 1430 and 1458 shapes subtract Modon and Coron but not Navarino (Venetian from 1417), and the 1418 and 1458 shapes do not subtract the Argolid, which the ledger gives to Venice in 1394 (/ledger/2) and KF2 itself carves out; the 1418 shape also still contains Kyparissia, gained only in 1432. Evidence: Koroni page: 'Navarino was taken over in 1417' (venetian-modon-and-coron /ledger/1); Lordship of Argos and Nauplia page: 'Argos, Kiveri and Thermisi remained in Theodore's hands until 11 June 1394, when he ceded them to Venice'. Fix: Add {lon 21.6958, lat 36.9125, km 12} (Navarino) to the minus of KF1-KF3, add the Argolid circle to the minus of KF1 and KF3, and add Kyparissia 25 km to the minus of KF1.
- TO DO `/ledger/7, /ledger/8, /ledger/9 (counterpart)`: The Morea's gains from principality-of-achaea are mirrored in the Achaea ledger as losses to 'byzantine-empire' (Achaea /ledger/38 1418, /ledger/45 1430, /ledger/47 1432), and byzantine-empire carries the same gains itself (/ledger/190, /ledger/194, /ledger/196). Evidence: principality-of-achaea.json and byzantine-empire.json ledgers read in this review. Fix: Not a defect of this dossier on its own: the orchestrator should decide whether the colony (despotate-of-the-morea) or the metropole (byzantine-empire) is the counterpart and have the other two dossiers follow; non-blocking.
- THIN `/keyframe_review/0`: The Byzantine Morea's extent 1349-1417 (Karytaina 1320, Skorta, Mani, Geraki), the Hexamilion/Corinth in 1415 and Patras 1429-30. (try https://en.wikipedia.org/wiki/Hexamilion_wall)
- Spot-checked and confirmed: /ledger/1, /ledger/2, /ledger/4, /ledger/8, /ledger/9, /ledger/10, /ledger/13.
- Area: Infobox gives no area (read).

## kingdom-of-candia: fix
- APPLIED `/ledger/7`: The 1648 loss of the rest of Crete was a confidence-1 bridging event on the Siege of Candia page, but the Cretan War page, already in sources, dates it. Evidence: Cretan War (1645-1669) page: 'The eastern half of the island was conquered in 1647, except for the fortress of Siteia'; 'By the beginning of 1648, all of Crete, except Candia and a few strongholds like the island of Gramvousa, was in Ottoman hands.' Fix: Source changed to the Cretan War page, confidence 1 -> 2, region text and note rewritten with the quotes; year kept at 1648 where the next shape starts. Re-validated: 0 errors.
- THIN `/wars/2`: The Kallergis revolt of 1282-1299 (and the 1217-1219 and 1363-1367 risings outside Candia) has no contest zone; the Kingdom of Candia page says only that it was 'the largest and most violent' and ended with the Peace of 28 April 1299. Also 'it took until 1212 for [the island] to be secured' (partial control 1205-1212 not drawn). (try https://en.wikipedia.org/wiki/Kallergis_family)
- Spot-checked and confirmed: /ledger/2, /ledger/4, /ledger/5, /ledger/6, /ledger/8, /ledger/9.
- Area: Infobox gives no area (read). Crete is about 8,300 km2.

## hospitaller-rhodes: thin
- THIN `/keyframe_review/0/correction (Dodecanese, from 1310)`: The Order's islands and their years: the page says only 'They also gained control of a number of neighbouring islands' and names Kastellorizo; the whole Dodecanese from 1310 is an upper bound and draws Kos, which lordship-of-chios gives to Martino Zaccaria in 1325-1329 (Martino Zaccaria page: Samos and Kos were already his in 1325). (try https://en.wikipedia.org/wiki/Kos)
- THIN `/ledger/3`: Bodrum's previous holder in 1402 (the page names none; counterpart beylik-of-menteshe is the author's reading). (try https://en.wikipedia.org/wiki/Bodrum_Castle)
- Spot-checked and confirmed: /ledger/0, /ledger/1, /ledger/2, /ledger/3, /ledger/6, /ledger/7, /ledger/5.
- Area: Infobox gives no area (read).

## lordship-of-chios: thin
- THIN `/ledger/1, /ledger/3`: Samos and Kos: the Martino Zaccaria page says Martino built his realm 'over the next few years' after 1314 and that the Zaccaria already held Chios, Samos and Kos at the 1325 grant; no year or previous holder for either, and nothing on how they were lost in 1329. Kos overlaps hospitaller-rhodes's Dodecanese region in 1325-1329. (try https://en.wikipedia.org/wiki/Samos)
- Spot-checked and confirmed: /ledger/0, /ledger/2, /ledger/4, /ledger/1.
- Area: No Wikipedia article (identity.wikipedia null); no area anywhere.

## maona-of-chios: thin
- THIN `/keyframe_review/0`: Phocaea: the infobox title is 'Maona of Chios and Phocaea' and the Maona's funds were raised to 're-conquer Chios and Phocaea' (1346), but the port is not drawn and no event takes it or loses it. (try https://en.wikipedia.org/wiki/Fo%C3%A7a)
- Spot-checked and confirmed: /ledger/0, /ledger/1, /ledger/2.
- Area: Infobox gives no area (read).

## gattilusi: fix
- APPLIED `/keyframe_review/4/to`: The last shape ended in 1461 although the lordship held Lesbos until September 1462 (the dissolve year). Evidence: Gattilusi page: 'An Ottoman fleet captured the island in September 1462'. Fix: Set 'to' 1461 -> 1462 with a reviewer note. Re-validated: 0 errors.
- THIN `/ledger/2 and /ledger/3`: Thasos (infobox only 'Lord of Thasos (1440s)'), Imbros and Samothrace have no year on any page; Old Phokaia (infobox 'c.1416-1426/8') is not drawn. (try https://en.wikipedia.org/wiki/Imbros)
- Spot-checked and confirmed: /ledger/1, /ledger/3, /ledger/4, /ledger/5, /ledger/6.
- Area: Infobox area not shown in the page text read; no area quoted by the author either.

## catepanate-of-italy: fix
- APPLIED `/keyframe_review/0/to`: No keyframe covered 1041-1042 (the 965 shape ended 1040 and the next began 1043). Evidence: Norman conquest of southern Italy page: the 1041 battles (16 March, 4 May, 3 September) and William's title of Count of Apulia at Melfi in September 1042; ledger /ledger/2 places the loss in September 1042. Fix: Set 'to' 1040 -> 1042 with a reviewer note. Re-validated: 0 errors.
- THIN `/keyframe_review/2 (1060-1071)`: Taranto, Otranto (besieged 1068), Matera and Calabria after Reggio (Squillace, Gerace): the pages give no fall dates, so the Salento-and-Bari shape is an upper bound. (try https://en.wikipedia.org/wiki/Otranto)
- THIN `/identity/start`: The themes of Longobardia and Calabria 876-965 are not carried (Theme_of_Longobardia gave 404). (try https://en.wikipedia.org/wiki/Longobardia)
- Spot-checked and confirmed: /ledger/0, /ledger/1, /ledger/2, /ledger/4, /ledger/5, /ledger/6, /ledger/7.
- Area: Infobox gives no area (read).

## acciaioli-duchy-of-athens: fix
- APPLIED `/keyframe_review/6/to`: No keyframe covered 1402 (the Boeotia-only shape ended 1401 and the next began 1403). Evidence: Antonio I Acciaioli page: Antonio 'captured the lower town of Athens in the first half of 1402' and forced the Acropolis 'to surrender in January or February 1403'; ledger /ledger/14 gains Attica in 1403. Fix: Set 'to' 1401 -> 1402 with a reviewer note. Re-validated: 0 errors.
- TO DO `/identity/capitals/1`: Athens is the capital for 1388-1458, but in 1395-1402 Athens was Venetian and the dossier's shape (KF6) is Boeotia only. Evidence: Antonio I Acciaioli page: the Senate acknowledged 'the annexation of Athens on 18 March 1395'; Nerio's will 'bequeathed two important castles in Boeotia, Livadeia and Thebes, to Antonio'. Fix: Split the capital: Athens 1388-1394, Thebes 1395-1402, Athens 1403-1458, and add capital_move events in 1395 and 1403. Non-blocking.
- TO DO `/identity/rulers/1, /identity/rulers/7`: The ruler strip gives 'Venetian podestas' for 1395-1402, although this dossier's state in those years is Antonio I's Boeotia; Francesco II ends in 1458 though he ruled Thebes to 1460, and 1454-1455 is uncovered. Evidence: Duchy of Athens page list (Antonio I 1394-1395, podestas 1395-1402 are Venetian Athens); Francesco II Acciaioli page: Mehmed 'allowed Franco to retain lordship of Thebes as his vassal' until 1460. Fix: Replace the podesta entry with Antonio I (1394-1435), run Francesco II to 1460 and close the 1454-1455 gap. Non-blocking.
- THIN `/ledger/3, /ledger/10`: Thebes 1385 (three accounts on the Nerio page) and how Corinth left the Acciaioli after 25 September 1394 (the page says only that Bartolomea 'claimed Corinth for herself'; house-of-tocco is the author's reading). (try https://en.wikipedia.org/wiki/Carlo_I_Tocco)
- Spot-checked and confirmed: /ledger/0, /ledger/2, /ledger/5, /ledger/6, /ledger/7, /ledger/8, /ledger/9, /ledger/11, /ledger/13, /ledger/16, /ledger/17.
- Area: Duchy of Athens infobox gives no area (read); its end year is 1458 and the dossier runs to 1460 with Thebes, which the Francesco II page supports.

## spania: fix
- APPLIED `/identity/capitals`: The capital Cartagena was given for 552-624, but Cartagena lies outside the 552-554 shape: the Byzantines landed there only in March 555. Evidence: Spania page: infobox capital 'Malaca (Málaga) or Carthago Spartaria (Cartagena)'; a force from Italy 'landed at Cartagena in early March 555'. Fix: Split into Málaga 552-554 (-4.42, 36.72, the author's own alternative) and Cartagena 555-624, with reviewer notes. Re-validated: 0 errors.
- THIN `/ledger/1 and /keyframe_review/2-3 (Algarve)`: The Algarve rests only on the Suintila page ('he seized what his predecessor had not at Algarve'); the Spania page does not mention it and says 'By the year 600 Spania had dwindled to little more than Málaga and Cartagena and the Balearics', which the 572-618 shape (with the whole Algarve) does not show. (try https://en.wikipedia.org/wiki/Sisebut)
- THIN `/ledger (555-589)`: Orospeda ('a region under Byzantine control' in 577, Spania page) and Baza ('was also Byzantine', 'Visigothic by 589') are neither drawn nor lost in the ledger; visigothic-kingdom gains Orospeda in 577. (try https://en.wikipedia.org/wiki/Liuvigild)
- THIN `/ledger/5, /ledger/6`: Cartagena's fall is undated (Spania page: Sisebut 'probably also razed Cartagena'); Málaga only 'before 619'. (try https://en.wikipedia.org/wiki/Cartagena,_Spain)
- Spot-checked and confirmed: /ledger/2, /ledger/3, /ledger/5, /ledger/7, /ledger/8.
- Area: Infobox gives no area (read).

## venetian-modon-and-coron: fix
- APPLIED `/keyframe_review/1/to`: The last shape ended in 1499 although the fortresses fell in August 1500 (the dissolve year). Evidence: Methoni page: 'After 28 days, on 9 August 1500, Methoni fell'; Koroni page: 'Koroni and Navarino surrendered (15 or 17 August 1500)'. Fix: Set 'to' 1499 -> 1500 with a reviewer note. Re-validated: 0 errors.
- THIN `/keyframe_review/0`: The territory behind the fortresses (the 'Messenian peninsula' the Koroni page says the fleet took) is drawn as two 15 km points; the 1686-1715 second period is not carried. (try https://en.wikipedia.org/wiki/Koroni)
- Spot-checked and confirmed: /ledger/0, /ledger/1, /ledger/2, /ledger/3.
- Area: No single article (identity.wikipedia null); no area anywhere.

## lordship-of-argos-and-nauplia: pass
- THIN `/identity/rulers`: Rulers start in 1311; the de la Roche holders of 1212-1311 (Otto, Guy I and their successors as dukes of Athens) are not listed. Optional. (try https://en.wikipedia.org/wiki/Otto_de_la_Roche)
- Spot-checked and confirmed: /ledger/0, /ledger/1, /ledger/2, /ledger/3, /ledger/4.
- Area: Infobox gives no area (read).

## marquisate-of-bodonitsa: pass
- Spot-checked and confirmed: /ledger/0, /ledger/1, /ledger/2.
- Area: No infobox in the page text read; no area.

## lordship-of-salona: pass
- Spot-checked and confirmed: /ledger/0, /ledger/1, /ledger/2, /ledger/3, /ledger/4.
- Area: Infobox gives no area (read); its 'Ottoman conquest: 1410' is the town's final fall, and /ledger/5 explains why the Frankish lordship ends in 1394.

## sclaviniae-of-greece: thin
- THIN `/keyframe_review/0/correction`: The Theme of the Peloponnese page puts the Slavs 'mostly in the western half of the peninsula', naming Elis, Messenia, Achaea and 'the Arcadian plateau'; Arcadia is not drawn, and Thessaly and Epirus (raided 586) are not settled either way. (try https://en.wikipedia.org/wiki/Theme_of_the_Peloponnese)
- THIN `/wars/1`: Constans II 'conquered Sklavinia in 657-658' with empty zones and no loss; Justinian II's 688-689 Slav campaign (byzantine-empire /ledger/26) has no event here. (try https://en.wikipedia.org/wiki/Justinian_II)
- THIN `/identity/end`: The Melingoi and Ezeritai of Taygetos, 'autonomous and tribute-paying', rebelled in 840/42 and 921/22 (Theme page): Slavic land survives 805. (try https://en.wikipedia.org/wiki/Melingoi)
- Spot-checked and confirmed: /ledger/0, /ledger/1, /ledger/2.
- Area: No area on either page.

## emirate-of-tarsus: fix
- APPLIED `/identity/capitals/0/note`: The capital note quoted an infobox ('Infobox: the page does not describe Tarsus as a capital') that the page does not have. Evidence: Emirate_of_Tarsus read twice: no infobox; its footnotes point to 'List of Abbasid governors of Tarsus'. Fix: Rewrote the note (no infobox, no capital named; Tarsus the governors' seat and the Thughur's 'most important town'). Re-validated: 0 errors.
- THIN `/ledger/1 and /keyframe_review/0`: The province's extent: the page names no town but Tarsus (governors 'often also exercised the governorship of the entire Syrian marches'); Adana and Mopsuestia were Muslim towns before 788, so 'gain from nobody' of all Cilicia is doubtful and the Abbasid dossier may draw the same land. (try https://en.wikipedia.org/wiki/Mopsuestia)
- THIN `/identity/wikipedia, /identity/type`: The URL Emirate_of_Tarsus serves the 'List of Abbasid governors of Tarsus' content (an inference from its footnotes); the governorate is typed 'state' although it was an Abbasid frontier province under Tulunid, Abbasid and Hamdanid overlords (colony of abbasid-caliphate may fit). (try https://en.wikipedia.org/wiki/Thughur)
- Spot-checked and confirmed: /ledger/0, /ledger/3.
- Area: No infobox, no area.

## Cross-dossier matrix (mismatches and missing mirrors)
- MISMATCH: despotate-of-the-morea 1418 gain cp=principality-of-achaea / principality-of-achaea 1418 loss: Achaea /ledger/38 names 'byzantine-empire', and byzantine-empire /ledger/190 carries the gain itself: one of colony or metropole must be the counterpart
- MISMATCH: despotate-of-the-morea 1430 gain cp=principality-of-achaea / principality-of-achaea 1430 loss: Achaea /ledger/42 (1429) and /ledger/45 (1430, Patras) name 'byzantine-empire'; byzantine-empire /ledger/193-194 duplicate
- MISMATCH: despotate-of-the-morea 1432 gain cp=principality-of-achaea / principality-of-achaea 1432 loss: Achaea /ledger/47 names 'byzantine-empire'; byzantine-empire /ledger/196 duplicate
- MISMATCH: kingdom-of-candia 1205 found cp=kingdom-of-thessalonica / byzantine-empire 1204 loss: byzantine-empire /ledger/149 gives Crete to 'republic-of-venice' in April 1204; Candia's found names kingdom-of-thessalonica (Boniface sold it). Note only
- MISMATCH: hospitaller-rhodes 1310 found cp=byzantine-empire / byzantine-empire 1314 loss: byzantine-empire /ledger/165 drops Rhodes in 1314 to 'domain-of-rhodes' (confidence 1, Cliopatria-driven); the Hospitaller page has the city surrender on 15 August 1310
- MISMATCH: hospitaller-rhodes 1402 loss cp=timurid-empire / timurid-empire 1402 occupation_start: timurid-empire has no event naming hospitaller-rhodes; Smyrna appears only inside its /ledger/14 note on the occupation of Ottoman land after Ankara. Timurid owner should add a gain from hospitaller-rhodes (December 1402)
- MISSING: lordship-of-chios 1304 found cp=byzantine-empire: byzantine-empire has no 1304 loss of Chios
- MISSING: lordship-of-chios 1325 gain cp=byzantine-empire: confidence 1 here; nothing in byzantine-empire
- MISSING: lordship-of-chios 1329 loss cp=byzantine-empire: Samos and Kos (confidence 1): no byzantine-empire event
- MISSING: maona-of-chios 1346 found cp=byzantine-empire: byzantine-empire has no 1346 loss of Chios
- MISSING: gattilusi 1355 found cp=byzantine-empire: byzantine-empire has no Lesbos event
- MISSING: gattilusi 1384 gain cp=byzantine-empire: Ainos: nothing in byzantine-empire
- MISSING: gattilusi 1440 gain cp=byzantine-empire: Thasos, confidence 1
- MISSING: gattilusi 1453 gain cp=byzantine-empire: Lemnos, Imbros, Samothrace: nothing in byzantine-empire
- MISSING: acciaioli-duchy-of-athens 1375 gain cp=catalan-company: Megara: catalan-company (1311-1390) has no loss
- MISMATCH: acciaioli-duchy-of-athens 1385 gain cp=catalan-company / catalan-company 1388 loss: the lower town of Athens in 1385; catalan-company loses Athens only in 1388 (/ledger/10)
- MISSING: acciaioli-duchy-of-athens 1394 loss cp=house-of-tocco: house-of-tocco (1357-1411) has no Corinth event; confidence 1 here
- MISSING: spania 552 gain cp=visigothic-kingdom: the Algarve (confidence 1): no visigothic-kingdom loss; eastern-roman-empire /ledger/49 gains Spania itself in 552
- MISMATCH: spania 555 gain cp=visigothic-kingdom / visigothic-kingdom 555 loss: visigothic-kingdom /ledger/19 names 'eastern-roman-empire' (colony vs metropole)
- MISMATCH: spania 572 loss cp=visigothic-kingdom / visigothic-kingdom 571 gain: visigothic-kingdom /ledger/21 (571) names 'eastern-roman-empire'; eastern-roman-empire /ledger/58 (572) duplicates
- MISMATCH: spania 619 loss cp=visigothic-kingdom / visigothic-kingdom 615 gain: visigothic-kingdom /ledger/31 has Malaga in 615 from 'eastern-roman-empire'; four years apart, both bridging
- MISMATCH: spania 624 loss cp=visigothic-kingdom / visigothic-kingdom 624 gain: visigothic-kingdom /ledger/32 names 'eastern-roman-empire'; eastern-roman-empire /ledger/87 duplicates
- MISMATCH: venetian-modon-and-coron 1206 found cp=principality-of-achaea / principality-of-achaea 1209 loss: Achaea /ledger/2 loses Modon and Coron at the Treaty of Sapienza (June 1209) to 'republic-of-venice'; the Koroni and Methoni pages have the capture in 1206 or 1207
- MISSING: venetian-modon-and-coron 1417 gain cp=principality-of-achaea: Navarino: no Achaea loss in 1416-1418
- MISSING: lordship-of-salona 1210 loss cp=despotate-of-epirus: despotate-of-epirus has no Salona event (its /ledger/1 1212 is Thessaly)
- MISSING: lordship-of-salona 1212 gain cp=despotate-of-epirus: as 1210
- MISSING: sclaviniae-of-greece 586 found cp=eastern-roman-empire: eastern-roman-empire has no Greek loss to the Slavs in 586 (its /ledger/63 582 is the Avar contest, /ledger/98 630 the Balkan interior to nobody)
- MISMATCH: sclaviniae-of-greece 783 loss cp=byzantine-empire / byzantine-empire 788 gain: byzantine-empire /ledger/38 gains inland Macedonia in 788 from 'nobody' (confidence 1, Cliopatria-driven)
- MISSING: sclaviniae-of-greece 805 loss cp=byzantine-empire: byzantine-empire has no 805 Peloponnese gain
- MISMATCH: emirate-of-tarsus 965 loss cp=byzantine-empire / byzantine-empire 962 gain: byzantine-empire /ledger/72 gains Cilicia in 962 from 'hamdanid-emirates' (confidence 1); the Tarsus page has Tarsus and 'the rest of Cilicia' taken in 965

Matched: despotate-of-the-morea 1388 gain = lordship-of-argos-and-nauplia 1388; despotate-of-the-morea 1404 loss = hospitaller-rhodes 1404; hospitaller-rhodes 1404 gain = despotate-of-the-morea 1404; lordship-of-chios 1329 loss = byzantine-empire 1329; acciaioli-duchy-of-athens 1372 found = principality-of-achaea 1371; acciaioli-duchy-of-athens 1388 gain = catalan-company 1388; acciaioli-duchy-of-athens 1390 gain = catalan-company 1390; lordship-of-argos-and-nauplia 1388 loss = despotate-of-the-morea 1388.

Exceptions (counterpart group not run, no dossier, or suzerain-side vassal events): see the JSON report.

## Problems for the orchestrator
- Every dossier is a new state with no Cliopatria row, so the area check compares nothing: no infobox read gives an area (all area_check values null, acknowledged in the keyframe notes).
- Colony-versus-metropole double counting across groups: despotate-of-the-morea, catepanate-of-italy, spania, kingdom-of-candia and exarchate-of-ravenna (type colony) carry the same gains and losses that byzantine-empire, eastern-roman-empire, principality-of-achaea and visigothic-kingdom record against the metropole slug, sometimes in other years (Morea 1418/1430/1432; Spania 555/572/624; Catepanate 1042/1060 against byzantine-empire 1046/1066; Tarsus 965 against byzantine-empire 962). The orchestrator should pick one convention and route the mirrors.
- Overlaps: lordship-of-chios Kos (1325-1329) inside hospitaller-rhodes's Dodecanese region (1310-); the Morea's 75 km Sparti circle over venetian-modon-and-coron and lordship-of-argos-and-nauplia (the Morea fail).
- Counterpart 'lombards' is used for 640-751 although Cliopatria's Lombards row ends in 586 and the author also asks for a separate lombard-kingdom-of-italy; 'papal-states' is used for 728 and 740 though its row starts in 755.
- Emirate_of_Tarsus serves the content of 'List of Abbasid governors of Tarsus' (no infobox, no H1 in the fetched text); identity.wikipedia was left as the author wrote it.
- Last keyframes of maona-of-chios (1565), spania (623) and sclaviniae-of-greece (804) end one year before the dissolve year; left as a convention (dissolution early in the year or undated), while gattilusi and venetian-modon-and-coron (dissolved August-September) were extended to the end year.
- Applied reviewer fixes (all re-validated, 0 errors, read back): exarchate-of-ravenna, catepanate-of-italy, acciaioli-duchy-of-athens (keyframe gaps), gattilusi, venetian-modon-and-coron (last keyframe to end year), kingdom-of-candia (/ledger/7 source and confidence), spania (capitals), emirate-of-tarsus (capital note). Backups of the pre-review files are in /tmp/claude-0/work/eu-05-x-review/bak/.
