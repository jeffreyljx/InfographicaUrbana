# af-02-x notes (Carthage and the Maghreb, additions batch)

Run of 2026-10-19. 27 new dossiers, none owning a Cliopatria row (cliopatria_names empty, every keyframe new, shape_id <slug>_<from>). All validate with 0 errors, 0 warnings and 0 resolve warnings. Every event, keyframe verdict and war cites a page opened with WebFetch in this run; where a page was silent the event is confidence 1 and says so. Confidence 3 only where the page gives both year and land.

## Method and conventions

- Types: dependencies are `colony` (exarchate-of-africa, portuguese-morocco, spanish-oran, spanish-bougie, spanish-tripoli, hospitaller-tripoli, spanish-tunis, spanish-presidios-of-morocco); dynasties are `dynasty`; everything else `state`. Dynasty changes inside a state are `rename` events. A vassal relation is recorded by the suzerain's dossier; where a page gave one for a state here it is in that dossier's notes only (Kuku's tribute to Algiers, the Kalaa's khalifa status, the Fatimid confirmation of the Khazrunids).
- Grid: H3 resolution 5 (about 253 km2 a cell). A circle under about 25 km around a coastal town can resolve to 0 cells, so every single-town presidio is a 25 km circle: it overstates the town and cannot show a tiny enclave.
- Where a sibling dossier already used a slug or a free-text counterpart name for one of these states, the same slug was adopted (zawiya-of-illigh, dila-iya-sultanate, bou-regreg-republic, mauro-roman-kingdom, maghrawa, banu-khurasan, banu-ifran, kingdom-of-kuku). hafsids-of-bejaia answers the Hafsid dossier's string 'Hafsid branch of Bejaia and Constantine' (it is in alt_names).
- Not duplicated: the Banu Ghaniya (Balearics 1126-1203 and the 1184-1188 occupation of Ifriqiya) are already events of almoravid-dynasty and almohad-caliphate, and the Banu Ghaniya page gives no land held after 1188 (raids only); no banu-ghaniya dossier was written.

## Mismatches with sibling dossiers (for the orchestrator)

- Cliopatria's Byzantine Empire row loses Africa at 698/709 while exarchate-of-africa runs from the 590s to 698/709; the sibling Byzantine dossier should carry the matching loss to the Umayyad Caliphate.
- Cliopatria's 'Portuguese Africa' row (1507-1581) overlaps portuguese-morocco (1415-1769); the Portuguese Morocco dossier is the page-based account, and its Asilah 1589 loss now names spanish-presidios-of-morocco.
- Saadi dossier: its Asilah (1589), Larache (1610) and La Mamora (1614) losses name the counterpart spanish-empire; they should read spanish-presidios-of-morocco. Morocco dossier: no events for Mehdya 1681, Larache 1689 or Asilah 1692 (the gains of the Alaouite sultan Moulay Ismail).
- Fez: the Dila'iya page has Fez lost in 1662 (putsch of Qaid Al-Doraidi) while the Alaouite and Morocco dossiers have al-Rashid take it in 1666; Salé was a vassal of the Zawiya from 1641 on the Republic of Salé page but held directly on others; the Dila'iya, Bou Regreg and Morocco dossiers should agree on the counterpart for 1661-1666.
- Hafsid dossier: Spain's takings of Bejaia (1509 there; 1510 on the Capture page and the Beni Abbas page), Tripoli (1510) and the 1535-1569 and 1573-1574 occupations of Tunis use the counterparts crown-of-castile and spanish-empire; the states that held them are spanish-bougie, spanish-tripoli, hospitaller-tripoli (1530-1551, not in the Hafsid dossier), spanish-tunis. Its 1401 annexation of Tripoli (counterpart 'nobody') is banu-thabit; Gabes before 1394 is banu-makki. Its 1277 split / 1318 and 1370 merges name 'Hafsid branch of Bejaia and Constantine' (hafsids-of-bejaia, whose own start is the infobox's 1285). Its Constantine attached to Algiers in the 1530s conflicts with kingdom-of-kuku (Constantine a Belkadi land before 1518) and hafsids-of-bejaia (a separate prince, Abu Bakr, in 1510).
- Regency of Algiers: the Cliopatria row and the sibling dossier start in 1706; the 1516-1705 life is inside the Ottoman Empire row. Counterparts named regency-of-algiers for 1520-1559 (kingdom-of-kuku, kingdom-of-beni-abbas, spanish-bougie, hafsid-dynasty) therefore have no dossier for those years.
- Kingdom of Africa dossier: its found event of 1146 names zirid-dynasty for Tripoli; the holder was banu-khazrun (1001-1146). The Zirid dossier's vassal_end for Tripolitania in 1146 (confidence 1) is the relation banu-khazrun's page dates to 1051-1052 (accepted the Zirid ruler's authority).
- Barghawata dossier: no loss of Tamesna in 1029; banu-ifran gains Tamesna from the Barghawata in 1029 (Temim ibn Ziri page), the Barghawata dossier has the Almoravids conquer it 'by 1060'. Idrisids dossier: its Tlemcen events of 789 and the Banu Ifran of Abu Qurra (765) are not matched by banu-ifran, which starts in 950 (page: navbox 950-1066).
- Maghrawa and banu-ifran agree on Fez 993 and 1033/1038; the Maghrawa page's Fez story 1001-1069 is not settled on any page (see the maghrawa notes). Hammadid dossier: no event for the c. 1075 gain of banu-khazrun; Zirid dossier: the Zirid ceding of Tripoli in 1022 is not recorded.

## Pages that failed

- https://en.wikipedia.org/wiki/Awlad_Muhammad_dynasty (404; the page was found by search as Awlad_Muhammad), https://en.wikipedia.org/wiki/Sultanate_of_Fezzan (404), https://en.wikipedia.org/wiki/Senussi_order (404; a search led to Senusi and Muhammad_al-Mahdi_as-Senussi, which were opened but gave no territory a dossier could draw).

## States not written and why

- banu-ghaniya (revival 1184-1238): covered by occupation events in almoravid-dynasty and almohad-caliphate; the page gives no land after 1188.
- miknasa (917-931, Fez): the Miknasa page names no Fez, no ruler and no date between 917 and the 11th century.
- senussi-order: a Sufi order with zawiyas from Cyrenaica to Chad; the pages give Jaghbub (1855/1856), Kufra (1894/1895) and the Emirate of Cyrenaica (25 October 1920) but no territory.
- beylik-of-constantine (1830-1837), beylik-of-titteri, emirate-of-tlemcen (742), sharifian-sultanate-of-fez (1465-1471): each under ten years.
- marinid-kingdom-of-marrakesh (1374-1387), awlad-mandil (Maghrawa of the Chelif, c. 1160-1372; page gives governors and years, no frontier), the Spanish posts of Melilla (since 1497), the Peñon de Velez de la Gomera (1508-1522, since 1564), Alhucemas, Ceuta (since 1640), Cazaza (1505-1533), Santa Cruz de la Mar Pequeña (1510-1644), Annaba (1535-1540), Honaine (1531-1535), Djerba (1521-1524, 1559-1560) and Dakhla: not reached (no pages opened); the enclaves-table years are in the notes of spanish-presidios-of-morocco and spanish-tunis.
- The Hilalian invasion 'year by year': the Banu Hilal page gives no year for Haydaran, Kairouan or Setif; the Zirid dossier holds the 1052-1057 events.
- English Tangier (1661-1684) is already an event pair of english-colonial-empire (Cliopatria draws it from 1662); not duplicated.

## Gazetteer names needed

- Sokna (Fezzan oasis, awlad-muhammad-dynasty): drawn as a lon/lat circle (15.9 E, 29.05 N, 100 km).
- Dila (Dila'iya, Middle Atlas highlands around Ait Ishaq, dila-iya-sultanate): circle at -5.6, 32.9, 70 km.
- Illigh / Tazerwalt (zawiya-of-illigh): circle at -6.0, 30.4, 110 km.
- Asilah (Arzila), Mehdya (La Mamora), Ksar es-Seghir, Azemmour (portuguese-morocco, spanish-presidios-of-morocco): 25 km circles at -6.03/35.47, -6.68/34.26, -5.56/35.85, -8.34/33.28.
- Tamesna, Siga, Cirta (as a place), Ashir, Kuku (Koukou), the Kalaa of Beni Abbas, Ifgan, Tolga: entered as notes or approximate capitals only.

## Per-state notes (the notes field of each dossier)

### Garamantes (garamantes, -500 to 666)

3 events (1 low confidence), 2 keyframes, 4 wars, 4 pages. Pages: Garamantes; Fezzan; Muslim_conquest_of_the_Maghreb; Uqba_ibn_Nafi.

Cliopatria has no Garamantes row (polities.csv). Start year is a bracket: the page puts the earliest written record in the 5th century BC (Herodotus), a footnote asserts a powerful polity from the 6th century BCE, and the lead says the kingdom 'first emerged as a major regional power in the mid-2nd century AD'. The page has no infobox in the fetched text and names only one king (Masyphios, undated). The end year is the Arab conquest of the Fezzan (663 or 666/7 depending on the page); the Garamantes page speaks of a 'late 7th century AD' end of the civilisation. The Garamantian hold on Ghat and the Wadi al-Ajal after 666 is not on the pages. Gazetteer: Germa, Fezzan and Ghat resolve; the radii are mine. Roman events are entered in wars only because no page gives a held front. A gap-filler could open 'Cornelius Balbus', 'Roman Libya' or 'Septimius Severus' for the garrisons (Bu Njem) the Garamantes page does not mention.

### Exarchate of Africa (exarchate-of-africa, 591 to 709)

10 events (1 low confidence), 3 keyframes, 3 wars, 5 pages. Pages: Exarchate_of_Africa; Battle_of_Carthage_(698); Gregory_the_Patrician; Muslim_conquest_of_the_Maghreb; Uqba_ibn_Nafi.

Cliopatria has no exarchate row; Africa sits inside the Eastern Roman Empire (534-632) and Byzantine Empire (633-) rows, whose bboxes reach 6 W and (from 656) Libya, and whose Cliopatria years for losing Africa do not match the pages (the byzantine-empire dossier author, eu-05, should drop Africa at 698, Ceuta at 709). Type 'colony' is chosen because the exarchate was ruled from Constantinople and was never a separate state, although Gregory's revolt 646-647 shows it acting as one. Pages disagree: the Exarchate page detaches Tripolitania to Egypt while the Gregory page gives western Libya; Gregory's revolt is 646 (Gregory page) or 647 (Exarchate table); Vescera is 682 (Exarchate) or 683 (Uqba); Hasan's entry to Carthage 695/6 (conquest page) or 697-698 (Battle page); Gregory is exarch 629-647 in the table but first attested July 645. The Corsica and Balearics hand-over in 698 is page-silent (confidence 1). Kusaila (Altava) and the Kahina (Aurès) are the Berber states that sat beside the exarchate; their lands are not subtracted here. Gazetteer: Ifriqiya, Sardinia, Corsica, Balearic Islands, Ceuta, Murcia and Almería resolve; 'Sbeitla' is not entered as a place.

### Kingdom of Altava (kingdom-of-altava, 578 to 708)

8 events (2 low confidence), 5 keyframes, 4 wars, 4 pages. Pages: Kingdom_of_Altava; Mauro-Roman_Kingdom; Uqba_ibn_Nafi; Muslim_conquest_of_the_Maghreb.

Cliopatria has no Altava, Aures or Mauro-Roman row. This dossier starts at the 578 collapse of the Mauro-Roman Kingdom, which needs a dossier of its own (429 independence per the infobox, Masuna's inscription at Altava dated 508, Garmul to 578; the page says the Kingdom of Ouarsenis and the Kingdom of Hodna were its regional successors, which no page here dates). Rulers: the infobox gives Sekerdid 668-678 and Caecilius (Kusaila, Aksel) 678-688, the table 680-690, the text his death in 690; no ruler strip is entered because the pages conflict and the first 90 years are unlisted. Kusaila's capital is Altava on this page, 'Tlemcen or more probably Tubna' on the Muslim conquest page. Kairouan: the Altava page says only that Kusaila forced the Arabs out of Kairouan in 683; the Uqba page has the recapture in 688. The Volubilis-to-Aures extent has no date on the page. The Exarchate of Africa (separate dossier) and the Aures kingdom are the neighbours. Gazetteer: Oranais, Volubilis, Algiers, Qairouan, Numidia and the Batna and Khenchela provinces resolve; 'Altava' is not a place name in the gazetteer (needed: Altava, Ouled Mimoun, Algeria, c. 34.88 N 1.05 W).

### Kingdom of the Aurès (kingdom-of-the-aures, 484 to 703)

7 events (0 low confidence), 3 keyframes, 4 wars, 4 pages. Pages: Kingdom_of_the_Aur%C3%A8s; Dihya; Mauro-Roman_Kingdom; Battle_of_Carthage_(698).

Cliopatria has no Aures row. Start 484 is the infobox's 'Revolt against Huneric'; the infobox gives 429 for the separation from the Western Roman Empire. 539-543 is a break (Byzantine rule) entered as a loss and a gain, with no keyframe for those years. Conflicts between pages: Dihya reigns c. 668-703 on the Aures page and 698-703 on the Dihya page (the ledger uses 698); the Dihya page says most Berbers joined her 'in the 680s, after Kusaila was killed' while Altava and the Aures page date Kusaila's death to 690; Iabdas ends 539 or 548; the Dihya page puts her death at Bir al-Kahina or Tabarka. The extent of the state between 544 and 698 is not on any page and the 690-697 interval is not covered (the Altava dossier gives Kusaila's lost land to nobody). Whether the Kahina held Kairouan after Hasan fled Ifriqiya is not stated and not entered. Gazetteer names needed: 'Aures' (the Aurès massif, Batna and Khenchela provinces, c. 35.3 N 6.5 E), 'Arris' and 'Khenchela' as places. The 'mauro-roman-kingdom' counterpart used by kingdom-of-altava needs its own dossier.

### Midrarid dynasty (midrarid-dynasty, 757 to 976)

4 events (0 low confidence), 1 keyframes, 2 wars, 2 pages. Pages: Midrarid_dynasty; Sijilmasa.

Cliopatria has no Midrarid row. The Midrarid page names only the Tafilalt as territory; any wider Midrarid hold on the Draa or the Sous is not on the pages opened. Start 757 is the founding of Sijilmasa; the page says the city 'asserted its independence' from the Abbasids 'as early as 771' (Sijilmasa page) and lists the dynasty's status as nominal Abbasid vassal 757-906 and Fatimid vassal 906-976: those vassal relations are the Abbasid and Fatimid dossiers' to record (me-08), and no event is entered here. End 976 is the infobox's 'Fatimid annexation', which sits uneasily with the Maghrawa takeover in the lede; no page gives a month or a named conqueror. The Maghrawa (Zenata of Fez and Sijilmasa, 909-1269 per the infobox) need a dossier: slug 'maghrawa'. The ruler list of 19 is the page's, with the slashed years reduced to the first year. Gazetteer: Tafilalt resolves; Sijilmasa is a place there.

### Awlad Muhammad dynasty (awlad-muhammad-dynasty, 1550 to 1811)

12 events (3 low confidence), 1 keyframes, 3 wars, 3 pages. Pages: Awlad_Muhammad; Fezzan; Murzuk.

Cliopatria has no Fezzan row. Start 1550 is the Awlad Muhammad page's 'from 1550 to 1812'; the Murzuk page puts the founder's rise 'early in the 16th century' and the Awlad page also says 'from the late 15th century'. The sibling Karamanli dossier records the Fezzan as a vassal 1807-1811 under the string 'Fezzan (Awlad Muhammad dynasty)'; the ottoman-empire and ottoman-tripolitania dossiers should carry the Ottoman suzerainty from 1574 (Fezzan page: 'vassalised from 1574') with this dossier's slug as counterpart. The 1574-1639 gap is the page-literal reading of 'invaded and occupied' and 'overthrew the Ottoman Bey in 1639'; the same pages call the Fezzan an autonomous tributary, so a reviewer may prefer a vassal reading (no event is entered for it). The occupations of 1690, 1716, 1718 name only a year; the Fezzan page does not name the occupier, and the Ottoman and Karamanli counterparts are the researcher's reading. The Awlad Muhammad page names no sultan except Bulalah Muhammad (1574) and Muhammad bin Juhaym (1639), so no ruler strip is entered. Gazetteer: Fezzan and Marzuq resolve; Sokna (Al Jufrah district, c. 29.05 N 15.9 E) is not a gazetteer place, so a 100 km circle by coordinates stands in for 'Sokna in the north' - listed as needed.

### Banu Khurasan (banu-khurasan, 1059 to 1159)

4 events (0 low confidence), 2 keyframes, 4 wars, 2 pages. Pages: Banu_Khurasan; Abd_al-Mu%27min.

Cliopatria has no Banu Khurasan row. The principality was a city state under Zirid and Hammadid suzerainty, often recognised on paper (al-Nasir to 1067, Tamim, the Zirids again 1116-7, the Hammadids 1120-1): those overlord relations are not drawn as vassal events here, because the overlord dossiers carry them if at all. The Kingdom of Africa dossier of this group records a vassal_start in 1148 with this state as counterpart ('Banu Khurasan (Tunis)'); the Banu Khurasan page does not mention Roger II's tribute or a 1148 Norman capture of Mahdia, saying only that 'some historians suggest that Roger II of Sicily granted the Banu Khurasan authority to govern', and the Abd al-Mu'min page does not mention Tunis's holder; a reviewer should check that vassal event against the Kingdom of Africa page. Start 1059 is the ruler list and the Zirid dossier's year (infobox c. 1058). Gazetteer: Tunis resolves.

### Zawiya of Illigh (zawiya-of-illigh, 1613 to 1670)

6 events (1 low confidence), 4 keyframes, 3 wars, 2 pages. Pages: Kingdom_of_Tazeroualt; Tazerwalt.

Cliopatria has no Illigh row. The sibling Saadi dossier (af-02-e) uses the slug zawiya-of-illigh for its 1614 (Sous) and 1631 (Draa) losses, which this dossier mirrors with the same region specs. Pages conflict: start 1613 (Kingdom page infobox) vs 1603 (Tazerwalt page: 'After Sultan Ahmad al-Mansur died in 1603, his grandson Sidi Ali Bou Dmia declared himself amir'); end 1681 (Kingdom page, with al-Rashid, who per the Alawi dossier reigned 1664-1672) vs 1670 (Tazerwalt page); the Kingdom page has Sijilmasa held 1631-1640 and the Tazerwalt page has the Alaouites take it in the late 1650s; the Tazerwalt page says the amirate 'by the mid-17th century' controlled Touat and Taghaza (not drawn). The House of Iligh regained 'significant political and military strength' and 'controlled much of the Souss region' in the 18th-19th centuries (Tazerwalt page; Hashim ibn Ali d. 1825, Husayn d. 1886, subdued by Hassan I in 1882 per the Kingdom page): that second life has no dates on the pages and is not entered; a gap-filler could extend this dossier. The Ali Abu Hassun article (Wattasid regent d. 1554) is a different person and was not used. Gazetteer: Sous, Tiznit and Sijilmasa resolve; Iligh is not a place there (needed: Iligh, Anti-Atlas, c. 29.8 N 9.5 W).

### Dila'iya Sultanate (dila-iya-sultanate, 1637 to 1668)

8 events (1 low confidence), 4 keyframes, 4 wars, 3 pages. Pages: Zawiya_Dila%27iya; Alawi_dynasty; Republic_of_Sal%C3%A9.

Cliopatria has no Dila'iya row. The sibling Saadi dossier (af-02-e) records 'dila-iya-sultanate' as counterpart for the 1641 loss of Fez, Meknes and Salé (one event) and of the northern union (another); this dossier uses the same region specs, but draws Salé as a vassal of the Dila'iya (1641-1661, from the Republic of Salé page), whereas the Dila page says Salé was 'taken': the reviewer can fold the Salé circle back into the gain. The Alawi dossier (morocco) records Fez in June 1666 and the Dila capital in June 1668 against 'dila-iya-sultanate'; this dossier has Fez lost to a putsch in 1662 and an autonomous Fez regime surrendering in 1666, so that gain should read 'nobody' or the Fez regime. The Alawi page also dates a Dala'iyya invasion of 1646 (undated outcome). No page opened gives the Dila'ites a presence outside northern and central Morocco, and the Saadi dossier's north union (including Casablanca and Chaouia) is only partly supported ('large parts of northern Morocco'; Tétouan; the Taza corridor; Ksar el-Kebir): it is the researcher's reading shared with the sibling. The rename event marks the 1659 proclamation as Sultan of Morocco at Fez ('ruling dynasty of Morocco 1659-1663'). Gazetteer: all names resolve. After 1668: in 1677 a grandson of Mohammed al-Hajj, Ahmad ibn Abdullah, returned with support from the Turkish regime in Algeria and rallied the Idrassen and other Sanhaja, three government expeditions were defeated before Ismail ibn Sharif overcame the highland forces, and he 'remained in the region until 1680, when he disappeared mysteriously' (Dila page); no land is held, so it is not a war entry. Gaps: no page gives an area, Mohammed al-Hajj's death, or a Dila'ite list of governors.

### Bou Regreg Republic (bou-regreg-republic, 1627 to 1668)

2 events (0 low confidence), 1 keyframes, 4 wars, 3 pages. Pages: Republic_of_Sal%C3%A9; Alawi_dynasty; Zawiya_Dila%27iya.

Cliopatria has no Bou Regreg row. The Saadi dossier (af-02-e) lists this state as a successor on the admin1 'Rabat - Salé - Zemmour - Zaer' and has no 1627 loss; the Alawi (morocco) dossier lists it as a predecessor and records the Dila'iya, not the republic, as holder of Salé in 1641, so the Saadi shape still contains Salé until 1641 while this dossier founds the republic in 1627: the integrator can resolve the overlap by giving the cells to the republic from 1627. The Dila'iya dossier of this batch records the vassal relation 1641-1661 with this state as counterpart. The page does not describe a Dutch alliance (only Jan Janszoon as Grand Admiral from 1624 and a Dutch consul from 1643) and does not mention Moulay Ismail or 1666. The 1609 Morisco influx, the 1614 first governor Brahim Vargas and Janszoon's 1624 admiralty precede the state and are not entered. No governor is listed for 1642-1650. Gazetteer: Rabat resolves.

### Portuguese Morocco (portuguese-morocco, 1415 to 1769)

18 events (0 low confidence), 15 keyframes, 7 wars, 4 pages. Pages: European_enclaves_in_North_Africa_before_1830; Moroccan%E2%80%93Portuguese_conflicts; Portuguese_conquest_of_Ceuta; Fall_of_Agadir.

Cliopatria has no 'Portuguese Morocco' row; the Cliopatria row 'Portuguese Africa' (1507-1581, max 35,685 km2, af-08) is a different bounding of the same coast and its years overlap this dossier's keyframes 1507-1581: the integrator should choose one of the two for those years. Wikipedia has no article of this exact title among the pages opened (null). The enclaves list and the conflicts page disagree on: Mazagan (seized 1486 vs founded 1514-17), Ksar es-Seghir's end (1549 vs 1550), Mogador (1506-1525 vs 1506-1510) and Aguz (1506-1525 vs 1520-25); Mogador and Aguz are short-lived and not entered. The first conquests (Ksar es-Seghir 1458, Arzila and Tangier 1471) name no holder on the pages opened; the Marinid dossier records them as losses, so 'marinid-sultanate' is the counterpart at confidence 2, and the later gains (Safi, Agadir, Azemmour, Mazagan, Casablanca, Mehdya) are entered against 'nobody'. Ceuta: 1640 (enclaves) vs 1668 (Ceuta page). The Spanish capture of Asilah in 1589 is the Saadi dossier's reading. Gazetteer names needed: Asilah, Ksar es-Seghir, Azemmour, Mehdya and Essaouira as places (coordinates stand in).

### Spanish Oran (spanish-oran, 1505 to 1792)

10 events (0 low confidence), 4 keyframes, 4 wars, 5 pages. Pages: Spanish_Oran; Spanish_conquest_of_Oran_(1509); Siege_of_Oran_(1707%E2%80%931708); Spanish_conquest_of_Oran_(1732); European_enclaves_in_North_Africa_before_1830.

Cliopatria has no Spanish Oran row (the Spanish Empire row's shape does not distinguish it). Start 1505 (Mers-el-Kebir) rather than the infobox's 1509 (Oran) because the two fortress-cities were held, lost and retaken together; the infobox lists 1509, 1708, 1732 and 1792 as its dates. Months: 18 May 1509 (storming), 20 January 1708 (Oran), 4 April 1708 (Mers el-Kebir), 1 and 2 July 1732 (Oran, Mers el-Kebir). The 1792 withdrawal has no month on the pages opened (the sibling Regency dossier has the 1791 agreements and the evacuation). The enclaves list gives 1791 for Oran's end and 1792 for Mers el-Kebir; the Spanish Oran page gives 1792. The sibling dossiers record the same events against 'crown-of-castile' (zayyanid losses 1505, 1509) and 'spanish-empire' (regency-of-algiers 1708, 1732, 1790-1792); this dossier's slug spanish-oran is the colony-level counterpart, and the integrator may map the Spanish Empire strings onto it. Other Spanish presidios (Bougie 1510-1555, Tripoli 1510-1530, the Algiers peñon 1510-1529, Melilla 1497-, Peñon de Velez, Alhucemas, Larache 1610-1689, La Mamora 1614-1681, Asilah, Santa Cruz de la Mar Pequena, Honaine, Annaba, Bizerte, La Goulette, Tunis, Sousse, Monastir, Mahdia, Djerba) are on the enclaves list and not in this dossier.

### Mauro-Roman Kingdom (mauro-roman-kingdom, 429 to 578)

2 events (0 low confidence), 1 keyframes, 2 wars, 2 pages. Pages: Mauro-Roman_Kingdom; Kingdom_of_Altava.

Cliopatria has no Mauro-Roman row. Pages disagree on the end: the Mauro-Roman page's infobox gives the decline at 599 and its text 'until roughly 589-599', the Altava page gives the collapse as 578 and Garmul's reign c. 570-579; 578 (Garmul's death) is used and the 579-599 remnant is the Altava dossier. The Mauro-Roman page gives no founding date; 429 is the infobox's military independence, and the Aures page gives the same 429 for its own separation, so the two states' beginnings are not distinguished on the pages. The infobox rulers (Mephanias? c. 477, Masuna c. 508, Mastigas c. 541, Stotzas 541-545, John 545-546, Garmul c. 570-579) mix Moorish kings with Byzantine officers and are not entered as a ruler strip. The Vandal wars of Gunthamund and Thrasamund (and Cabaon's victory over a Vandal army) are undated on the page and are not entered as a war. The Kingdoms of Ouarsenis and Hodna (regional successors) and the Aures kingdom (separate dossier kingdom-of-the-aures) are neighbours; the Mauretania Caesariensis extent is the researcher's reading and overlaps the Vandal Kingdom row of Cliopatria west of 3 E only at the margin. Gazetteer: Oranais and Algiers resolve; Altava is not a gazetteer place.

### Maghrawa (maghrawa, 976 to 1070)

11 events (1 low confidence), 6 keyframes, 3 wars, 3 pages. Pages: Maghrawa_(tribe); Ziri_ibn_Atiyya; Sijilmasa.

Cliopatria has no Maghrawa row. The pages opened do not give a founding of the 'state': the Maghrawa were the largest branch of the Zenata, and the dossier starts with Khazrun ibn Fulful's 976-7 conquest of Sijilmasa. The Maghrawa page has no infobox; 1070 is the Almoravid capture of Fez ('1069 or some time later in the 1070s'). The text calls Tamim 'the last Maghrawa ruler of Fez' while also giving the Banu Ifran leader Abu al-Kamal Tamim the capture of Fez in 1032-3 and the Hammadid Buluggin ibn Muhammad the expulsion of Futuh from Fez in 1062: the Fez timeline between 1001 and 1069 is not reconstructible from these pages (the sibling Hammadid dossier has the Hammama of Fez as a vassal 1039-1062) and the 1001-1054 keyframe keeps Fez throughout. Ziri's 'master of the Maghreb' (991) and 'amir of the Maghreb' (987) do not name territory. The Umayyad appointment of 987 and the Fatimid protection of Tlemcen after 998 are vassal-type relations recorded by the Caliphate of Cordoba and Fatimid dossiers if at all. Banu Ifran, Hammama and Idrisid remnants need their own dossiers (banu-ifran suggested). Gazetteer: Fez, Oujda, Tiaret, Tlimcen and Tafilalt resolve.

### Banu Ifran (banu-ifran, 950 to 1066)

9 events (2 low confidence), 6 keyframes, 4 wars, 5 pages. Pages: Banu_Ifran; Temim_ibn_Ziri; 1033_Fez_massacre; Zirid_conquest_of_the_western_Maghreb; Ziri_ibn_Atiyya.

Cliopatria has no Banu Ifran row. The Banu Ifran page has no infobox; the navbox gives 950-1066 and the text an Abu Qurra emirate at Tlemcen from 765 (the sibling Idrisid report names Abu Qurra's Tlemcen in 789), with the 8th-century revolt against the Umayyads and Abbasids and the c.547-550 clash with John Troglita as undated background; the dossier starts in 950 because nothing connects the 765 emirate to the 10th-century dynasty on the pages opened. The page says Ya'la ibn Mohammed was killed by Jawhar 'in battle in 954' (a footnote cites Ibn Khaldun for 958) and that the Fatimids destroyed Ifgan; none is placed or dated closely enough for a ledger event. Pages disagree on the Maghrawa recapture of Fez (1037-1038, 1039, 1038-1040). The Ifranid founding of the Taifa of Ronda (1039; Abu Nur lord of Ronda and Seville 1023-1039 per the page) is al-Andalus and is left to the Iberia group. The Barghawata dossier has no 1029 loss; its Tamesna loss is to the Almoravids by 1060, so the two dossiers conflict on who held Tamesna after 1029. The Maghrawa dossier has the matching 993 and 1033/1038 Fez events; the Idrisid dossier's Tlemcen events from 789 are not matched here.

### Kingdom of Kuku (kingdom-of-kuku, 1515 to 1638)

5 events (0 low confidence), 4 keyframes, 1 wars, 2 pages. Pages: Kingdom_of_Kuku; Ahmed_ou_el_Kadhi.

Cliopatria has no Kuku row. The Hafsid dossier already holds the 1520 and 1525 Algiers events under the counterpart regency-of-algiers; the Regency dossier itself starts in 1706, so the counterpart slug has no dossier for 1520-1525 (the Regency page dates the state from 1516). The Kuku page says the kingdom was 'an absolutely independent feudatory' that paid an unspecified tribute to the Algiers pashalik (no date), that Hassan Pasha married the king's daughter for an alliance (no year), and that Koukou troops served in the Algerian campaigns of 1541, 1562, 1565, 1569, 1576 and 1578 and the sieges of the Qala (1559); the tribute is the Regency's to record. Its mention that Cherchell and Annaba gave allegiance in 1520-1527 has no exact year and is not drawn. The Hafsid dossier has Constantine pass to Algiers in the 1530s, the Kuku page has it a Belkadi land before 1518; the two are not reconciled. Ahmed ou el Kadhi's reign is 1510-1527 on his page and 1515-1527 on the kingdom's infobox. The Ait Abbas kingdom (kingdom-of-beni-abbas) was its rival: its Ahmed Amokrane is said to have occupied Algiers in 1598. The 1618 Aourir move of Si Ahmed Atounsi and the 1696 succession of Si Ali (a date after the stated end of the dynasty, which the page does not explain) are not drawn.

### Kingdom of Beni Abbas (kingdom-of-beni-abbas, 1510 to 1871)

4 events (1 low confidence), 3 keyframes, 4 wars, 2 pages. Pages: Kingdom_of_Beni_Abbas; Ahmed_Ait_Mokran.

Cliopatria has no Kalaa row. The page's infobox lists rulers Abdelaziz Ou Abbas 1510-1559 and Boumezrag 1871-1872 and says the principality reached 'from the valley of the Soummam to the Sahara'; no area is given. Status towards Algiers, from the page: submission to the Barbarossas in 1516, khalifa of the Medjana from 1542, 'independence' recognised by Khizr Pasha in 1590 for 30,000 douros and again after the Guidjel victory in 1638, tribute and the ouadia under Bouzid (1680-1735), vassals of the Bey of Constantine in the late 18th century (no year); after the French took Constantine in 1837 Ahmed Mokrani became khalifa of the Medjana on 30 September 1838. These are suzerainty events for the Regency, Constantine and French dossiers, and none is drawn here; the Regency dossier starts in 1706, so the early wars use its slug without a dossier for the years. The Mokrani dynasty's end is 1871 here (surrender of the Kalaa) against 1872 in the infobox. The Kuku kingdom (kingdom-of-kuku) fought on Algiers' side in 1559. Béjaïa, held by Spain 1510 (1509 on the Hafsid dossier) to 1555, is not in the kingdom's circle.

### Hafsids of Béjaïa (hafsids-of-bejaia, 1285 to 1510)

11 events (3 low confidence), 6 keyframes, 3 wars, 3 pages. Pages: Hafsids_of_B%C3%A9ja%C3%AFa; Capture_of_B%C3%A9ja%C3%AFa_(1510); Capture_of_B%C3%A9ja%C3%AFa_(1555).

Cliopatria has no row for this branch: the Hafsid Dynasty row (1236-1571) carries the Constantinois to 1555 (see the Hafsid dossier's notes). The sibling Hafsid dossier already holds this branch under the name 'Hafsid branch of Bejaia and Constantine' with a split in 1277, a merge in 1318 and a merge in 1370 (the last dated 1370 on both pages); the 1285 here is the infobox's, the 1277 the death of al-Mustansir. Gaps without a shape are deliberate: 1318-1349 and 1370-1500 the branch is inside the unified Hafsid state; 1351-1358 is the Marinid hold (the Hafsid dossier); the page gives no date for the cession to Abu Abdullah (1350 here is a bridge). The conflict of Béjaïa's fall: the HB infobox says 9 November 1510, the Capture page 25 May 1510 on Arab sources and 1509 on a door inscription; the Beni Abbas page gives 1510 and the Hafsid dossier 1509. The 1436-1452 revolt of Abu-l-Hasan (spring 1436 to 1439, capture of Béjaïa on 9 November 1439, three weeks of 1446, siege and betrayal in 1452) is the Hafsid dossier's war and is not drawn here. Constantine: the Capture page has a separate prince there in 1510, and the Hafsid dossier has it attached to Algiers in the 1530s. The page's Zayyanid and Marinid wars (Uthman's Zayyanids against Abu Zakariya; Abu Yaqub Yusuf's seizure of Algiers) have no year and are not drawn. The Kingdom of Kuku and the Kingdom of Beni Abbas dossiers (kingdom-of-kuku, kingdom-of-beni-abbas) cover the successors.

### Spanish Bougie (spanish-bougie, 1510 to 1555)

3 events (0 low confidence), 1 keyframes, 2 wars, 4 pages. Pages: Capture_of_B%C3%A9ja%C3%AFa_(1510); Capture_of_B%C3%A9ja%C3%AFa_(1555); Ahmed_ou_el_Kadhi; Kingdom_of_Kuku.

Cliopatria has no Bougie row (its Kingdom of Spain row starts in 1516 and the Hafsid row carries the Constantinois to 1555; see the Hafsid dossier notes). Dates: Pedro Navarro reached Béjaïa on 5 January 1510 and the city fell in late May 1510 on the Arab sources, while a Casbah door inscription reads 1509 (the Hafsid dossier has 1509); the Hafsids of Béjaïa infobox gives 9 November 1510. The Hafsid emir's flight: Emir Abderrahmane withdrew to the Kalaa of Beni Abbes and set up a principality (the kingdom-of-beni-abbas dossier), and Abdelaziz's brother Abu Bakr, prince of Constantine, killed him in battle at Takerkat (no year). The 1555 page's Spanish strength differs by source: about 100 men in the presidio, or 500 to 1,000 men across the three forts (Féraud), or 1,000 men and a few dozen horses (Braudel). Other Spanish enclaves taken in the same years (the Peñón of Algiers, Tripoli in 1510, Melilla, the Peñón de Vélez) are not on the pages opened here.

### Masaesyli (masaesyli, -344 to -203)

5 events (2 low confidence), 2 keyframes, 2 wars, 2 pages. Pages: Masaesyli; Syphax.

Cliopatria has no Masaesyli row (its Kingdom of Numidia row starts in 197 BC). The page has no rulers' reign years beyond '344-310 BC: Aylimas (?)' and '? -175 BC: Archobarzane'; Syphax's own reign is 'c. 225 - c. 203 BC' on his page (infobox) and the only date on the Masaesyli page is the 220 BC map caption; the dossier starts in 344 BC only to have a number (page silent, confidence 1). The end is the Masaesyli page's 'c. 203-202 BC' for Masinissa's unification; the infobox 'Annexed by Numidia: 175 BC' and the Syphax page's 'died in Tibur in 203 or 202 BC' are the other dates. The Syphax page says he was born at Siga c. 250 BC, allied with Rome in 213 BC, and concluded a treaty with Scipio only at Siga in 206 BC; the 'Massylii' kingdom of Gala has no dossier here (the Cliopatria row for Numidia begins in 197 BC). Cape Tritonis, Strabo's eastern limit as the page quotes him, is not in the gazetteer and is not placed.

### Spanish Tripoli (spanish-tripoli, 1510 to 1530)

3 events (0 low confidence), 1 keyframes, 1 wars, 2 pages. Pages: Spanish_Tripoli; Hospitaller_Tripoli.

Cliopatria has no Tripoli row for 1510-1551: the Hafsid Dynasty row carries Tripolitania to 1551 (Hafsid dossier, note 2), which is the overlap to correct. The Hafsid dossier writes the 1510 loss with the counterpart crown-of-castile; this dossier is the state the Spanish held it through. The Hafsid dossier cites the Siege of Tripoli page for 'under Spanish rule since its capture in 1510'; this one rests on the Spanish Tripoli and Hospitaller Tripoli pages.

### Hospitaller Tripoli (hospitaller-tripoli, 1530 to 1551)

3 events (0 low confidence), 1 keyframes, 1 wars, 1 pages. Pages: Hospitaller_Tripoli; Siege_of_Tripoli_(1551).

Cliopatria has no Hospitaller row: the Hafsid Dynasty row carries Tripolitania to 1551 (Hafsid dossier, note 2). Skirmishes with Tajura (under Aydin Reis, who built the el-Cadi tower about a mile outside the walls, destroyed by Georg Schilling von Cannstatt, no year) are on the page, with March-June 1539 as the only year implied; no war is entered for them. The page also has Dragut capture the galley La Catarinetta carrying 7,000 scudi (no date), the 1559-1560 Battle of Djerba and Dragut as beylerbey of Tripoli in 1556; none touches the Order's land.

### Spanish Tunis (spanish-tunis, 1535 to 1574)

12 events (0 low confidence), 6 keyframes, 2 wars, 3 pages. Pages: Conquest_of_Tunis_(1535); Conquest_of_Tunis_(1574); European_enclaves_in_North_Africa_before_1830.

Cliopatria has no Spanish Tunis row. The Hafsid dossier holds the Hafsid side: the vassalage and the occupation of Tunis 1535-1569 and 1573-1574 under the counterpart spanish-empire and the Ottoman events under ottoman-empire; this dossier uses ottoman-empire for the Spanish gains and losses. Page conflicts: the Conquest of Tunis (1574) page gives the fall of La Goleta as 24 August; the Conquest of Tunis (1535) page names no capture date for La Goulette (14 July is the date set for the assault) and does not say Spain held Bizerte. The enclaves table gives Bizerte, Sousse, Monastir and Mahdia years with no text; those four are confidence 2 and the grid cannot show a presidio smaller than 25 km. Not entered: Annaba (1535-1540), Honaine (1531-1535) and Djerba (1521-1524, 1559-1560), which are Algerian or island holdings of the same table. The 1569-1573 interval is Ottoman at Tunis and the table keeps La Goulette Spanish throughout; the 1574 page says the presidio was 'defended by 7,000 men'. The Tunis page does not use the word 'protectorate' for the Hafsid relationship (the enclaves table does).

### Spanish presidios of Morocco (spanish-presidios-of-morocco, 1589 to 1692)

7 events (0 low confidence), 5 keyframes, 3 wars, 5 pages. Pages: Asilah; Cession_of_Larache; Siege_of_Larache_(1689); Mehdya,_Morocco; European_enclaves_in_North_Africa_before_1830.

Cliopatria has no row for these posts. The Saadi dossier carries the Spanish gains (Asilah 1589, Larache 1610, La Mamora 1614) under the counterpart spanish-empire; this dossier is the state that held them, and those events should read spanish-presidios-of-morocco. The Portuguese Morocco dossier's 1589 loss of Asilah has the same counterpart. Dates in conflict: Asilah to Spain 1589 (Asilah page, the Saadi and Portuguese dossiers) or c. 1604 (enclaves table); Asilah lost 1692 (Asilah page) or 1691 (table; the siege page has a prisoner exchange in September 1691); Larache taken 11 November 1689 or 1 November (siege page); Mehdya 'Portuguese 1515' on the Mehdya page (São João da Mamora) and the English-Dutch pirate battle of about 1610. Not entered, for page budget: Melilla (since 1497), the Peñón de Vélez de la Gomera (1508-1522, since 1564), Alhucemas (table 'since 1559', text 1673), Ceuta (since 1640), Cazaza (1505-1533), Santa Cruz de la Mar Pequena (1510-1644) and Dakhla (1502) of the same enclaves table; Cliopatria's Kingdom of Spain row may carry the Mediterranean ones.

### Banu Khazrun (banu-khazrun, 1001 to 1146)

7 events (1 low confidence), 3 keyframes, 3 wars, 2 pages. Pages: Banu_Khazrun; Norman_expedition_to_Tripoli_(1143).

Cliopatria has no Khazrunid row (Tripolitania is inside its Hafsid row from 1236 and nothing before). Internal conflicts on the page: the Zirids retake Tripoli after 1009 'for a time' while the ruler list has Warru 1009/1010-1014/1015 and Khalifa from c. 1015; the same list ends al-Muntasir in 1049 while the Hammadid conquest is 'around 1075'; the text has Khazrun ibn Sa'id leave for Egypt around 1014-5 while the list puts Khazrun ibn Khalifa in 1037/1038. The Zirid dossier holds a vassal_end for Tripolitania in 1146 at confidence 1; the Hilalian invasion year of 1051-1052 on this page is the Zirid dossier's contest of 1052-1057. Ashir is not in the gazetteer and is not placed. The Fatimid confirmation of 1026-7 would be a vassal event for the Fatimid dossier; none is entered here. The Hammadid dossier has no event for the c. 1075 gain.

### Banu Thabit (banu-thabit, 1324 to 1401)

5 events (0 low confidence), 2 keyframes, 3 wars, 2 pages. Pages: Banu_Thabit; Banu_Makki.

Cliopatria has no Banu Thabit row; its Hafsid Dynasty row carries Tripolitania from 1236. The Hafsid dossier records Abu Faris's 1401 annexation of Tripoli with the counterpart 'nobody' because no page named the holder; this dossier supplies it. The Banu Makki page says their domain 'extended from Gabès to Tripoli' at its height 'sometime the early 14th century', which conflicts with this page's rule of Tripoli from c. 1324 and is left to the Banu Makki dossier's notes. Regnal years on the page are given as year pairs (1326-1327 for Muhammad's command, 1348 for his murder, 1354-1355 and 1369-1370, 1389-1390, 1397-1398); the first of each pair is used. The page has no infobox, so no area or dates were compared.

### Banu Makki (banu-makki, 1282 to 1394)

6 events (0 low confidence), 3 keyframes, 2 wars, 2 pages. Pages: Banu_Makki; Banu_Thabit.

Cliopatria has no Banu Makki row; its Hafsid Dynasty row carries Gabès and Tripolitania throughout. The Banu Makki page has no infobox and names no ruler except the Hafsid Ahmad II; its early-14th-century height 'from Gabès to Tripoli' (and the Jabal Nafusa) conflicts with the Banu Thabit page (Tripoli under the Banu Thabit from c. 1324) and is not drawn. The Hafsid dossier has no 1394 event for Gabès and records Tripoli's 1401 annexation under the counterpart 'nobody'. The page's 'an effectively independent state in the second half of the 14th century' has no year.
