# Review of batch af-02-x (Carthage and the Maghreb, additions)

Reviewer run of 2026-10-19. 27 new dossiers (no Cliopatria rows; page budget 2-5 pages each). Validator with --resolve: 0 errors, 0 warnings on all 27 before and after the reviewer edits. Spot checks: 115 events opened with WebFetch, weighted to confidence 3 and to the largest moves; none was fabricated or mis-dated at confidence 3.

Verdicts: garamantes pass, exarchate-of-africa pass, kingdom-of-altava fix, kingdom-of-the-aures pass, midrarid-dynasty pass, awlad-muhammad-dynasty thin, banu-khurasan pass, zawiya-of-illigh pass, dila-iya-sultanate pass, bou-regreg-republic pass, portuguese-morocco thin, spanish-oran pass, mauro-roman-kingdom pass, maghrawa thin, banu-ifran thin, kingdom-of-kuku pass, kingdom-of-beni-abbas thin, hafsids-of-bejaia thin, spanish-bougie pass, masaesyli fix, spanish-tripoli pass, hospitaller-tripoli pass, spanish-tunis pass, spanish-presidios-of-morocco pass, banu-khazrun pass, banu-thabit fix, banu-makki pass.

Meaning: pass = could not break it; fix = small faults fixed in place by the reviewer (re-validated); thin = valid and honest, with non-blocking items (confidence-1 bridges, unexplained keyframe drops or in-batch mirrors) for a gap-filler. No dossier failed.

## Edits made by the reviewer

- kingdom-of-altava /wars/0: The war 'Garmul's war on the Eastern Romans' (570-578) lay outside the state's life (578-708) and duplicated mauro-roman-kingdom /wars/1. Evidence: Check 2 (wars inside the life); the same war, with its zone, is in mauro-roman-kingdom. Done: Removed the war here; a reviewer note was appended to notes. Re-validated: 0 errors, 0 warnings.
- maghrawa /ledger/4: No mirror for banu-ifran's January 993 seizure of Fez: the ledger had Ziri regain Fez from the Banu Ifran in 993 without first losing it. Evidence: Banu Ifran page: Yaddu ibn Ya'la 'took Fes by surprise in January 993 and held it for some months'; Ziri ibn Atiyya page: 'Ziri recaptured Fes in 993'. Done: Inserted a 993 loss of Fez (60 km) to banu-ifran, confidence 3, source Banu_Ifran (added to sources); the 987-997 keyframe is unchanged because both moves fall in 993. Later ledger indices shift by one. Re-validated: 0 errors, 0 warnings.
- banu-ifran /ledger/1: The January 993 gain of Fez (month 1) sorted after the undated loss of later in 993, so the ledger had the loss before the gain. Evidence: Banu Ifran page: 'took Fes by surprise in January 993 and held it for some months'; Ziri ibn Atiyya page: 'Ziri recaptured Fes in 993'. Done: Dropped the month from the gain (January kept in the note) and put the gain before the loss; now /ledger/1 gain, /ledger/2 loss. Re-validated: 0 errors, 0 warnings.
- masaesyli /identity/capitals/0: Siga was placed at Tlemcen (-1.32, 34.89), about 45 km from the site. Evidence: Siga page: coordinates 35.2663 N, 1.4499 W, 'in the lower valley of the Tafna'. Done: Set lon -1.45, lat 35.27 and appended the source to the capital note. Re-validated: 0 errors, 0 warnings.
- banu-thabit /ledger/0: The 1324 found event named counterpart 'nobody' although Tripoli was a Hafsid city. Evidence: Banu Thabit page: Thabit 'took power in the city toward 1324' after a rebellion expelled the Hafsid prince Ibn Abi 'Umran, appointed governor by Abu Yahya Abu Bakr II. Done: Counterpart set to hafsid-dynasty with a reviewer note. Re-validated: 0 errors, 0 warnings.

## Per dossier

### garamantes: pass

- Thin /ledger/0: c1 found at -500: the page gives settlement by 1000 BC, first record 5th century BC and a footnote polity from the 6th century BCE, no founding year (try https://en.wikipedia.org/wiki/Fezzan)
- Spot checks: /ledger/0 confirmed (Garamantes: 5th century BC first record; c1 bridge honest); /ledger/1 confirmed (Garamantes: 'first emerged as a major regional power in the mid-2nd century AD'); /ledger/2 confirmed (Muslim_conquest_of_the_Maghreb: 'Around 666-667 ... campaigning in Sirte, Fezzan - taking ancient Germa'); /wars/2 confirmed (Garamantes: 'In 202 AD, Septimius Severus captured the capital city of Garama')
- Area / other: no infobox; the text gives roughly 180,000 km2; the 240 km Germa circle is about 181,000 km2

### exarchate-of-africa: pass

- Thin /ledger/8: c1: Corsica and the Balearics leave the exarchate in 698 by assumption; the page dates neither (try https://en.wikipedia.org/wiki/Byzantine_Sardinia)
- Spot checks: /ledger/0 confirmed (Exarchate_of_Africa: 'established by the Emperor Maurice in 591'); /ledger/1 confirmed (Exarchate_of_Africa: 'final conquest of the last Spanish strongholds in c. 624 by the Visigoths'); /ledger/2 confirmed (Exarchate_of_Africa: Gregory independent in 647, Sufetula the same year (cited page Gregory_the_Patrician not reopened)); /ledger/6 confirmed (Exarchate_of_Africa: 'In 698, ... Hasan ibn al-Nu'man ... crushed Carthage'); /ledger/9 confirmed (Muslim_conquest_of_the_Maghreb: lead: 'concluding in 709, when the Byzantine Empire lost its last remaining strongholds in the Maghreb')
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### kingdom-of-altava: fix

- Thin /ledger/1: c1: the 678 extension to Volubilis, Algiers and Numidia; the page gives only 'During the reign of Aksel, it extended from Volubilis in the west to the Aures', undated (try https://en.wikipedia.org/wiki/Kusaila)
- Thin /ledger/6: c1: the 690 collapse of the Volubilis-to-Aures realm to nobody; no page says who held the land 690-698 (try https://en.wikipedia.org/wiki/Kusaila)
- Spot checks: /ledger/2 confirmed (Kingdom_of_Altava: 'in 683 AD Uqba ibn Nafi was ambushed and killed in the Battle of Vescera'; Arabs forced to evacuate Kairouan); /ledger/3 confirmed (Uqba_ibn_Nafi: 'recaptured in 688' (the sentence is ambiguous between Kairouan and Barca; the conquest page has Mamma in 688/9, the Altava page in 690)); /ledger/5 confirmed (Kingdom_of_Altava: 'Caecilius met them in 690 AD ... at the Battle of Mamma'); /ledger/7 confirmed (Kingdom_of_Altava: infobox 'Annexed by Umayyad Caliphate: 708')
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### kingdom-of-the-aures: pass

- Spot checks: /ledger/1 confirmed (Kingdom_of_the_Aur%C3%A8s: 'a small interruption of Byzantine occupation from 539 to 544 AD'); /ledger/2 confirmed (Kingdom_of_the_Aur%C3%A8s: infobox 'Re-establishment of the kingdom after the Battle of Cillium: 544'); /ledger/3 confirmed (Dihya: Battle of Meskiana, 698); /ledger/5 confirmed (Dihya: 'ruled a sovereign Berber state from the Aures Mountains to the oasis of Ghadames (698-703)'); /ledger/6 confirmed (Kingdom_of_the_Aur%C3%A8s: 'killed in battle in 703 AD')
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### midrarid-dynasty: pass

- Thin /keyframe_review/0: One shape for 757-976; the Fatimid capture of Sijilmasa by Jawhar (958) and the 909-910 interruption are not on the two pages opened (within the 2-page budget) (try https://en.wikipedia.org/wiki/Jawhar_al-Siqilli)
- Spot checks: /ledger/0 confirmed (Midrarid_dynasty: 'Samgu led the establishment of the town of Sijilmasa in 757/8'); /ledger/1 confirmed (Sijilmasa: army 'arrived in the Tafilalt in the latter half of 909, and laid siege to the city'); /ledger/3 confirmed (Midrarid_dynasty: infobox 'Fatimid annexation: 976'; Maghrawa page 'In 976-7 ... conquered Sijilmasa from the Banu Midrar')
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### awlad-muhammad-dynasty: thin

- Thin /ledger/6: c1: the 1691 return after the 1690 occupation (page lists only the occupation years) (try https://en.wikipedia.org/wiki/Murzuk)
- Thin /ledger/8: c1: the 1717 return after the 1716 occupation (try https://en.wikipedia.org/wiki/Karamanli_dynasty)
- Thin /ledger/10: c1: the 1719 return after the 1718 occupation (try https://en.wikipedia.org/wiki/Karamanli_dynasty)
- Thin /ledger/3: The Fezzan page says the land was 'occupied fully from times to time like in 1679-1682, 1690, 1716, 1718 and 1811/1812'; the 1679-1719 pairs would be truer as occupation_start/occupation_end (hatched) than as loss/gain, and the 1716/1718 counterpart karamanli-dynasty is inferred (the page names no occupier) (try https://en.wikipedia.org/wiki/Fezzan)
- Spot checks: /ledger/1 confirmed (Fezzan: 'In 1574 Ottoman Tripolitania under Mahmut bey invaded and occupied Fezzan'); /ledger/2 confirmed (Awlad_Muhammad: 'overthrew the Ottoman Bey in 1639, and assumed control'); /ledger/3 confirmed (Fezzan: 1679-1682 occupation); /ledger/7 confirmed (Fezzan: 1716 occupation (occupier not named)); /ledger/11 confirmed (Fezzan: 1811/1812)
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### banu-khurasan: pass

- Spot checks: /ledger/0 confirmed (Banu_Khurasan: infobox c. 1058, ruler list from 1059); /ledger/1 confirmed (Banu_Khurasan: 1128: 'annexed to the Hammadid kingdom'); /ledger/2 confirmed (Banu_Khurasan: independence regained 1148); /ledger/3 confirmed (Banu_Khurasan: 'final end with the Almohad conquest in 1159')
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### zawiya-of-illigh: pass

- Thin /ledger/2: c1: the Draa valley gain is undated on the page (1631 borrowed from Sijilmasa and the Saadi dossier) (try https://en.wikipedia.org/wiki/Tazerwalt)
- Spot checks: /ledger/0 confirmed (Kingdom_of_Tazeroualt: infobox 'Established: 1613'); /ledger/3 confirmed (Kingdom_of_Tazeroualt: Sijilmasa seized 1631); /ledger/4 confirmed (Kingdom_of_Tazeroualt: 'until the Alawis expelled him in 1640'); /ledger/5 confirmed (Tazerwalt: 'in 1670 the Alaouites razed the capital of Tazerwalt at Iligh' (the Kingdom page says 1681; conflict acknowledged in notes))
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### dila-iya-sultanate: pass

- Thin /ledger/3: c1: the 'large parts of northern Morocco' (Tangier-Tetouan, Taza, Fes provinces) are undated beyond 'from 1637 onwards' (try https://en.wikipedia.org/wiki/Mohammed_al-Hajj_ibn_Abu_Bakr_al-Dila%27i)
- Spot checks: /ledger/1 confirmed (Zawiya_Dila%27iya: 'By 1641, they had conquered Meknes, Fez and the port of Sale'); /ledger/2 confirmed (Republic_of_Sal%C3%A9: infobox 'Under the suzerainty of the Zawiya Dila'iya (1641-1661)'); /ledger/4 confirmed (Zawiya_Dila%27iya: proclaimed sultan in Fez 1659); /ledger/6 confirmed (Zawiya_Dila%27iya: Fez lost 1662 after the putsch of Qaid Al-Doraidi); /ledger/7 confirmed (Republic_of_Sal%C3%A9: 'in June 1668, Sultan Moulay al-Rashid' vanquished the Dila'iya)
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### bou-regreg-republic: pass

- Spot checks: /ledger/0 confirmed (Republic_of_Sal%C3%A9: April 1627, 'the Hornacheros expelled the Sherif's governor'); /ledger/1 confirmed (Republic_of_Sal%C3%A9: June 1668, al-Rashid ended the independence)
- Area / other: dossier 15 km circle (about 700 km2) is the grid minimum; acknowledged in /keyframe_review/0. Non-blocking: identity.rulers has a gap 1641-1651 and ends 1661.

### portuguese-morocco: thin

- Open finding /ledger/2 (non-blocking): The 1471 gain of Asilah and Tangier names marinid-sultanate, whose own dossier ends in 1465 (and there loses Tangier to kingdom-of-portugal in 1465). Evidence: marinid-sultanate identity 1244..1465; wattasid-dynasty starts 1472; the event note says the pages do not name the holder; the Wattasid dynasty page (opened) is silent on 1471. Fix: Name the 1471 holder from a page (the Wattasid governor at Asilah, Muhammad al-Shaykh, or the Sharifian sultanate of Fez 1465-1471) or write the free-text holder; route the 1465/1471 Tangier conflict to the Marinid owner.
- Thin /ledger/2: who held Asilah and Tangier in 1471 (try https://en.wikipedia.org/wiki/Asilah)
- Spot checks: /ledger/7 confirmed (European_enclaves_in_North_Africa_before_1830: 'Mehdya was taken in 1515, though it was lost soon after in 1541'; Casablanca 1515-1755); /ledger/9 confirmed (Fall_of_Agadir: infobox 'March-September 1541'); /ledger/10 confirmed (Fall_of_Agadir: 'evacuated by the Portuguese in October 1541'); /ledger/12 confirmed (European_enclaves_in_North_Africa_before_1830: Asilah 1471-1550 and 1577-1589); /ledger/14 confirmed (European_enclaves_in_North_Africa_before_1830: Ceuta Portuguese 1415-1640, Spanish since 1640); /ledger/16 confirmed (European_enclaves_in_North_Africa_before_1830: Casablanca 1515-1755)
- Area / other: no Wikipedia article (wikipedia null); 25 km town circles, grid minimum, stated in notes

### spanish-oran: pass

- Spot checks: /ledger/0 confirmed (Spanish_conquest_of_Oran_(1509): 'In 1505, the Spanish captured the city of Mers-El-Kebir'); /ledger/1 confirmed (Spanish_conquest_of_Oran_(1509): infobox 'May 1509'); /ledger/3 confirmed (Siege_of_Oran_(1707%E2%80%931708): Oran fell January 1708); /ledger/5 confirmed (Siege_of_Oran_(1707%E2%80%931708): Mers el-Kebir fell April 1708); /ledger/6 confirmed (Spanish_conquest_of_Oran_(1732): entered Oran 1 July 1732); /ledger/9 confirmed (Spanish_Oran: 'In 1792 the Spanish troops retreated from the city')
- Area / other: no area on the page. Non-blocking: identity.capitals starts 1509 while the life starts 1505 (Mers el-Kebir 1505-1508 could be the first capital).

### mauro-roman-kingdom: pass

- Thin /keyframe_review/0: One shape 429-578 (Oranais plus a 150 km Algiers circle); the page says that under Mastigas it 'controlled virtually the entire ancient province of Mauretania Caesariensis, except for the old capital of Caesarea' (undated); thin by design within the 2-page budget (try https://en.wikipedia.org/wiki/Masuna)
- Spot checks: /ledger/0 confirmed (Mauro-Roman_Kingdom: infobox 'Military independence from the Western Roman Empire: 429'); /ledger/1 confirmed (Mauro-Roman_Kingdom: 'Garmul was defeated and killed in 578 AD' (infobox decline 599 acknowledged in notes))
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### maghrawa: thin

- Open finding /keyframe_review/4 (non-blocking): The 1001-1054 keyframe keeps Fez throughout, while banu-ifran (same batch) holds Fez 1033-1038; Fez is drawn by both dossiers for six years and the ledger has no 1033 loss or 1038 gain. Evidence: Banu Ifran page: Tamim retook Fes in May-June 1033 and 'the Maghrawa tribe retook Fes, forcing Tamim to flee to Sale' in 1038-1040; 1033 Fez massacre page dates the capture; banu-ifran /ledger/5 and /ledger/6. Fix: Add a 1033 loss of Fez (counterpart banu-ifran) and a 1038 gain (1038-1040 on the page), and split /keyframe_review/4 into 1001-1032, 1033-1037 (without Fez) and 1038-1054.
- Open finding /identity/alt_names (non-blocking): The alt name 'Banu Khazrun' is the name of another dossier in this batch (banu-khazrun, the Tripoli emirate). Evidence: banu-khazrun identity.name; name matching would collide. Fix: Write 'Banu Khazrun of Sijilmasa' or drop it.
- Thin /ledger/8: c1: Tiaret and Tlemcen taken from Idrisid remnants, undated on the page (after 998); counterpart idrisids ends in 974 in its own dossier (try https://en.wikipedia.org/wiki/Hammama_ibn_al-Mu%27izz)
- Thin /keyframe_review/4: Fez 1033-1038 (see fixes) and who held Fez 1039-1069 (Hammama, Futuh; Hammadid expulsion 1062) (try https://en.wikipedia.org/wiki/1033_Fez_massacre)
- Spot checks: /ledger/0 confirmed (Maghrawa_(tribe): '976-7 ... conquered Sijilmasa from the Banu Midrar'); /ledger/3 confirmed (Ziri_ibn_Atiyya: court at Fes 'after capturing it from the Idrisids' (987-988)); /ledger/5 confirmed (Ziri_ibn_Atiyya: 'Ziri recaptured Fes in 993'); /ledger/7 confirmed (Ziri_ibn_Atiyya: 'opened the gates to Abd al-Malik on October 13, 998'); /ledger/9 confirmed (Ziri_ibn_Atiyya: al-Mansur 'restored him to possession of all his father's former territories' (1001)); /ledger/10 confirmed (Sijilmasa: 'in 1055, Abdallah ibn Yasin' killed the Maghrawa leader)
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### banu-ifran: thin

- Thin /ledger/0: c1 found in 950 (navbox only; the text gives no 950 start) (try https://en.wikipedia.org/wiki/Ya%27la_ibn_Muhammad_al-Ifrani)
- Thin /ledger/4: c1: Sale as capital from 1030 (the page attaches citation needed) (try https://en.wikipedia.org/wiki/Temim_ibn_Ziri)
- Thin /keyframe_review/5: Tamesna (the Barghawata shape) is dropped in 1039 with no ledger event; K4 also runs to 1038 although the Fez loss is dated 1038. Add a loss of Tamesna (or keep it to the 1058/1066 end) and align K4/K5 with the loss year (try https://en.wikipedia.org/wiki/Barghawata)
- Spot checks: /ledger/1 confirmed (Banu_Ifran: January 993); /ledger/2 confirmed (Ziri_ibn_Atiyya: recaptured 993); /ledger/3 confirmed (Banu_Ifran: 1029: 'conquered Tamesna from the Barghawata'); /ledger/5 confirmed (Banu_Ifran: May or June 1033); /ledger/6 confirmed (Banu_Ifran: 1038-1040); /ledger/8 confirmed (Banu_Ifran: navbox 950-1066; Almoravids 'capturing Tlemcen' in 1066)
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### kingdom-of-kuku: pass

- Spot checks: /ledger/0 confirmed (Kingdom_of_Kuku: 'Established: c. 1515'; before 1518 'ruled over lands from the Djurdjura to Setif and Constantine'); /ledger/1 confirmed (Kingdom_of_Kuku: break with the Barbarossas 1518, domain reduced to Greater Kabylie (undated)); /ledger/2 confirmed (Ahmed_ou_el_Kadhi: took Algiers 1520); /ledger/3 confirmed (Kingdom_of_Kuku: 'from 1520 to 1525/1527' (Ahmed page: 1527)); /ledger/4 confirmed (Kingdom_of_Kuku: 'until 1632 or 1638')
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### kingdom-of-beni-abbas: thin

- Thin /ledger/1: c1: the page appears to date Ahmed Amokrane's southern campaign to 1559 ('He subjugated Tolga and Biskra, Laghouat and reached Touggourt'); confirm and raise to 2 with the Kingdom_of_Beni_Abbas source (try https://en.wikipedia.org/wiki/Kingdom_of_Beni_Abbas)
- Thin /keyframe_review/1: The oasis circles (Biskra, Touggourt, Laghouat) are kept for 1559-1848 and dropped at 1849 with no ledger event; the page says southern control 'dissipated' after Ahmed Amokrane's death (1596). Add a loss c. 1596 (or the year a page gives) and end the circles there (try https://en.wikipedia.org/wiki/Ahmed_Ait_Mokran)
- Spot checks: /ledger/0 confirmed (Kingdom_of_Beni_Abbas: 'founding to the withdrawal of the Hafsid Emir of Bejaia, Aberrahmane, in 1510'); /ledger/1 confirmed (Kingdom_of_Beni_Abbas: 1559 campaign (c1 is under-confident)); /ledger/2 confirmed (Kingdom_of_Beni_Abbas: 'In 1849, the tribes of the Hodna were similarly removed from his control'); /ledger/3 confirmed (Kingdom_of_Beni_Abbas: 'surrendered on 22 July 1871')
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### hafsids-of-bejaia: thin

- Thin /ledger/2: c1: loss of Tunis dated 1310; the page gives no year (Abu-l-Baqa was overthrown by al-Lihyani, usually 1311) (try https://en.wikipedia.org/wiki/Abu_Yahya_Zakariya_al-Lihyani)
- Thin /ledger/4: c1: the 1350 split (page: Marinid invasions after 1347, Ibrahim II ceding Bejaia to Abu Abdullah) (try https://en.wikipedia.org/wiki/Hafsid_dynasty)
- Thin /keyframe_review/3: No loss/gain for the Marinid hold of Bejaia (1353-1358): the state vanishes between K3 (to 1352) and K4 (from 1359) with no ledger event (try https://en.wikipedia.org/wiki/Abu_Inan_Faris)
- Thin /ledger/7: c1: the 1501 split; the page names Abu-l-Hasan's 1436 revolt as the start of the third independence and only 'early 16th century' for an independent emir (try https://en.wikipedia.org/wiki/Hafsids_of_B%C3%A9ja%C3%AFa)
- Spot checks: /ledger/0 confirmed (Hafsids_of_B%C3%A9ja%C3%AFa: infobox 'secession from Hafsid domain of Ifriqiya: 1285'); /ledger/1 confirmed (Hafsids_of_B%C3%A9ja%C3%AFa: Abu-l Baqa took Tunis after Abu Asida died in 1309); /ledger/3 confirmed (Hafsids_of_B%C3%A9ja%C3%AFa: 'in early 1318 Abu-Yahya Abu-Bakr made his entrance into the capital'); /ledger/5 confirmed (Hafsids_of_B%C3%A9ja%C3%AFa: 'In May 1366 Abu'l Abbas took Bejaia'); /ledger/6 confirmed (Hafsids_of_B%C3%A9ja%C3%AFa: reunited 'for the third time, in 1370'); /ledger/8 confirmed (Capture_of_B%C3%A9ja%C3%AFa_(1510): 1510, Sultan Abdelaziz)
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### spanish-bougie: pass

- Spot checks: /ledger/0 confirmed (Capture_of_B%C3%A9ja%C3%AFa_(1510): infobox 1510); /ledger/1 confirmed (Capture_of_B%C3%A9ja%C3%AFa_(1555): Peralta surrendered 'on September 27'; Kuku among the belligerents)
- Area / other: no area. Non-blocking: /wars/0 (1512) names kingdom-of-kuku, whose life starts 1515 (the Kuku page cites Rinn for a 1510 founding).

### masaesyli: fix

- Thin /ledger/0: c1 found at -344 (infobox ruler '344-310 BC: Aylimas (?)', 'Established: 4th century BC') (try https://en.wikipedia.org/wiki/Numidia)
- Thin /ledger/2: c1 capital move to Cirta in 206 BC; the Syphax page calls Cirta the capital only during the 203 pursuit (try https://en.wikipedia.org/wiki/Cirta)
- Spot checks: /ledger/0 confirmed (Masaesyli: 4th century BC (c1 honest)); /ledger/1 confirmed (Syphax: after Gala died in 206 BC Syphax was 'able to conquer considerable parts of the eastern Numidian kingdom'); /ledger/3 confirmed (Syphax: 'in the 203 BC Battle of the Great Plains'; the capital 'later fell as Masinissa claimed his kingdom')
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### spanish-tripoli: pass

- Spot checks: /ledger/0 confirmed (Spanish_Tripoli: infobox 'Spanish conquest: 25 July 1510'); /ledger/1 confirmed (Spanish_Tripoli: 'took control of the city on 25 July' 1530)
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### hospitaller-tripoli: pass

- Spot checks: /ledger/0 confirmed (Hospitaller_Tripoli: infobox 'Established: 25 July 1530'); /ledger/1 confirmed (Hospitaller_Tripoli: infobox 'Ottoman conquest: 15 August 1551' (text 14 August))
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### spanish-tunis: pass

- Spot checks: /ledger/1 confirmed (Conquest_of_Tunis_(1535): infobox 'June-August 1535'); /ledger/2 confirmed (Conquest_of_Tunis_(1535): 'restored as client ruler of Tunis and Spanish-Imperial tributary'); /ledger/7 confirmed (Conquest_of_Tunis_(1535): 'Tunis remained under Spanish control until its Ottoman recapture in 1569'); /ledger/9 confirmed (Conquest_of_Tunis_(1574): 're-conquered Tunis in October 1573'); /ledger/10 confirmed (Conquest_of_Tunis_(1574): last troops surrendered 13 September 1574); /ledger/5 confirmed (European_enclaves_in_North_Africa_before_1830: Bizerte 1535-1573, Sousse 1537-1574, Monastir 1550-1554, Mahdia 1550-1553)
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### spanish-presidios-of-morocco: pass

- Spot checks: /ledger/0 confirmed (Asilah: 'in 1589 the Saadians briefly regained control of Asilah ... but then lost it to the Spanish' (enclaves table c. 1604-1691, acknowledged)); /ledger/1 confirmed (Cession_of_Larache: 20 November 1610); /ledger/2 confirmed (Mehdya,_Morocco: August 1614); /ledger/3 confirmed (Mehdya,_Morocco: 1681); /ledger/4 confirmed (Siege_of_Larache_(1689): 11 November 1689); /ledger/5 confirmed (Asilah: 'In 1692, the town was taken by the Moroccans')
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### banu-khazrun: pass

- Thin /ledger/4: c1: the 1076 loss of the western conquests; the page gives no year for al-Muntasir's death (try https://en.wikipedia.org/wiki/Hammadid_dynasty)
- Spot checks: /ledger/0 confirmed (Banu_Khazrun: 'After 1001, Tripolitania broke away from Zirid control'); /ledger/2 confirmed (Banu_Khazrun: 'The Zirids finally ceded Tripoli to the Banu Khazrun in 1022'); /ledger/3 confirmed (Banu_Khazrun: around 1075 'occupied the towns of Ashir and al-Masila, along with the M'zab and Righ regions'; base at Waghlana near Biskra (Ashir not drawn: not in the gazetteer)); /ledger/6 confirmed (Banu_Khazrun: 'finally capture the city in 1146 or 1147')
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### banu-thabit: fix

- Spot checks: /ledger/0 confirmed (Banu_Thabit: 'toward 1324'); /ledger/1 confirmed (Banu_Thabit: Genoese conquest 1354-1355); /ledger/2 confirmed (Banu_Thabit: 'retake the city in 1369-1370'); /ledger/3 confirmed (Banu_Thabit: 'finally captured the city in 1401')
- Area / other: no Cliopatria row (new state) and no infobox area on the page

### banu-makki: pass

- Spot checks: /ledger/0 confirmed (Banu_Makki: 'ruled over Gabes from 1282 until 1394' (effective independence only in the second half of the 14th century)); /ledger/1 confirmed (Banu_Thabit: the Genoese 'agreed to give the city to the Banu Makki'); /ledger/2 confirmed (Banu_Makki: 'By the mid-1350s, they had extended their control to both Tripoli and Sfax'); /ledger/4 confirmed (Banu_Makki: direct Hafsid control under Abu al-Abbas Ahmad II (r. 1371-1394))
- Area / other: no area. Non-blocking: K1 (1355-1369) and banu-thabit K1 (from 1369) both hold Tripoli in 1369.

## Cross-dossier matrix (non-trivial rows)

Rows with counterpart nobody or a counterpart whose group has not run are omitted here (they are in the JSON report).

- mismatch: kingdom-of-the-aures 539 loss -> eastern-roman-empire; mirror eastern-roman-empire 540 gain. eastern-roman-empire (done, 395-632) has no Aures event in 539 or 544; its ledger should carry the 539 gain and 544 loss of Batna/Khenchela (Kingdom of the Aures page: Byzantine occupation 539-544).
- mismatch: kingdom-of-the-aures 544 gain -> eastern-roman-empire; mirror eastern-roman-empire 543 loss. see 539.
- mismatch: awlad-muhammad-dynasty 1716 loss -> karamanli-dynasty; mirror karamanli-dynasty 1713 gain. karamanli-dynasty starts 1711/1713 and has no Fezzan events 1716-1719; Fezzan page: occupied 1716 and 1718 (holder not named; Karamanli inferred). Route to the karamanli owner.
- missing: awlad-muhammad-dynasty 1717 gain -> karamanli-dynasty; mirror none. see 1716.
- missing: awlad-muhammad-dynasty 1718 loss -> karamanli-dynasty; mirror none. see 1716.
- missing: awlad-muhammad-dynasty 1719 gain -> karamanli-dynasty; mirror none. see 1716.
- mismatch: banu-khurasan 1128 loss -> hammadid-dynasty; mirror hammadid-dynasty 1128 gain. hammadid-dynasty has the 1128 gain but with the free-text counterpart "Banu Khurasan (Tunis)"; it should read banu-khurasan.
- mismatch: banu-khurasan 1148 gain -> hammadid-dynasty; mirror hammadid-dynasty 1148 loss. hammadid-dynasty 1148 loss names "Tunis (next holder not named on the page)"; should read banu-khurasan.
- matched: zawiya-of-illigh 1614 gain -> saadi-sultanate; mirror saadi-sultanate 1614 loss. 
- matched: zawiya-of-illigh 1631 gain -> saadi-sultanate; mirror saadi-sultanate 1631 loss. 
- matched: zawiya-of-illigh 1631 gain -> saadi-sultanate; mirror saadi-sultanate 1631 loss. 
- missing: zawiya-of-illigh 1640 loss -> morocco; mirror none. morocco (Alaouite) dossier has no 1640 gain of Sijilmasa from zawiya-of-illigh (Kingdom of Tazeroualt page: the Alawis expelled Abu Hassun in 1640).
- matched: dila-iya-sultanate 1641 gain -> saadi-sultanate; mirror saadi-sultanate 1641 loss. 
- exception: dila-iya-sultanate 1641 vassal_start -> bou-regreg-republic; mirror none. vassal relation recorded on the suzerain per the schema (counterpart = the vassal); a mirror vassal_start in bou-regreg-republic would invert the roles, so none is expected. Republic of Sale infobox: suzerainty of the Zawiya Dila'iya 1641-1661.
- matched: dila-iya-sultanate 1641 gain -> saadi-sultanate; mirror saadi-sultanate 1641 loss. 
- exception: dila-iya-sultanate 1661 vassal_end -> bou-regreg-republic; mirror none. as 1641.
- mismatch: portuguese-morocco 1458 gain -> marinid-sultanate; mirror marinid-sultanate 1458 loss. marinid-sultanate has the 1458 loss of Ksar es-Seghir but names kingdom-of-portugal; should name portuguese-morocco.
- missing: portuguese-morocco 1471 gain -> marinid-sultanate; mirror none. counterpart marinid-sultanate ends 1465 in its own dossier (and there loses Tangier to kingdom-of-portugal in 1465); wattasid-dynasty starts 1472. The 1471 holder of Asilah/Tangier is unresolved on the pages; the author must name it (Wattasids or the Sharifian sultanate of Fez 1465-1471, which has no dossier).
- mismatch: portuguese-morocco 1541 loss -> saadi-sultanate; mirror saadi-sultanate 1541 gain. saadi-sultanate has the 1541 gains but names portuguese-africa (Cliopatria row); should name portuguese-morocco.
- mismatch: portuguese-morocco 1541 loss -> saadi-sultanate; mirror saadi-sultanate 1541 gain. saadi-sultanate has the 1541 gains but names portuguese-africa (Cliopatria row); should name portuguese-morocco.
- mismatch: portuguese-morocco 1541 loss -> saadi-sultanate; mirror saadi-sultanate 1541 gain. saadi-sultanate has the 1541 gains but names portuguese-africa (Cliopatria row); should name portuguese-morocco.
- mismatch: portuguese-morocco 1550 loss -> saadi-sultanate; mirror saadi-sultanate 1550 gain. saadi-sultanate has 1549 gain from wattasid-dynasty and 1550 gain from portuguese-africa; the latter should name portuguese-morocco.
- missing: portuguese-morocco 1577 gain -> saadi-sultanate; mirror none. saadi-sultanate has no 1577 loss of Asilah to portuguese-morocco.
- matched: portuguese-morocco 1589 loss -> spanish-presidios-of-morocco; mirror spanish-presidios-of-morocco 1589 found. 
- missing: portuguese-morocco 1640 loss -> spanish-empire; mirror none. spanish-empire has no 1640 gain of Ceuta.
- mismatch: portuguese-morocco 1661 loss -> english-colonial-empire; mirror english-colonial-empire 1661 gain. english-colonial-empire (context neighbour) has the 1661 gain of Tangier but names portuguese-empire; should name portuguese-morocco.
- missing: portuguese-morocco 1755 loss -> morocco; mirror none. morocco has no 1755 gain of Casablanca (Anfa).
- mismatch: spanish-oran 1509 gain -> zayyanid-dynasty; mirror zayyanid-dynasty 1509 loss. zayyanid-dynasty has the 1509 loss of Oran but names crown-of-castile; should name spanish-oran.
- mismatch: spanish-oran 1708 loss -> regency-of-algiers; mirror regency-of-algiers 1708 gain. regency-of-algiers has the 1708 gain but names spanish-empire; should name spanish-oran.
- mismatch: spanish-oran 1708 loss -> regency-of-algiers; mirror regency-of-algiers 1708 gain. regency-of-algiers has the 1708 gain but names spanish-empire; should name spanish-oran.
- mismatch: spanish-oran 1732 gain -> regency-of-algiers; mirror regency-of-algiers 1732 loss. regency-of-algiers has the 1732 loss but names spanish-empire; should name spanish-oran.
- mismatch: maghrawa 979 loss -> zirid-dynasty; mirror zirid-dynasty 980 gain. zirid-dynasty has a 980 gain naming "western Maghreb rulers (not named on the page)"; should name maghrawa.
- mismatch: maghrawa 983 gain -> zirid-dynasty; mirror zirid-dynasty 985 loss. zirid-dynasty has a 985 loss to nobody; should be a 983 loss to maghrawa (Maghrawa page: driven out between 979 and 983).
- missing: maghrawa 987 gain -> idrisids; mirror none. idrisids dossier ends in 974 (Cliopatria row); the Ziri ibn Atiyya page says Fes was captured from the Idrisids in 987-988 (the 979-985 restoration of Hasan ibn Kannun). Route: the idrisids dossier lacks the 979-985 restoration.
- matched: maghrawa 993 loss -> banu-ifran; mirror banu-ifran 993 gain. 
- matched: maghrawa 993 gain -> banu-ifran; mirror banu-ifran 993 loss. 
- missing: maghrawa 999 gain -> idrisids; mirror none. as 987: idrisids dossier ends 974; the page has Ziri overthrow Idrisid remnants at Tiaret (undated, c1).
- mismatch: maghrawa 1055 loss -> almoravid-dynasty; mirror almoravid-dynasty 1054 found. almoravid-dynasty has no 1055 gain of Sijilmasa from maghrawa (its 1058 gain names Aghmat).
- matched: banu-ifran 993 gain -> maghrawa; mirror maghrawa 993 loss. 
- matched: banu-ifran 993 loss -> maghrawa; mirror maghrawa 993 gain. 
- missing: banu-ifran 1029 gain -> barghawata-conference; mirror none. barghawata-conference has no 1029 loss of Tamesna to banu-ifran (its Tamesna loss is to the Almoravids by 1060); author flagged.
- missing: banu-ifran 1033 gain -> maghrawa; mirror none. IN-BATCH: maghrawa keeps Fez throughout 1001-1054 and has no 1033 loss / 1038 gain; banu-ifran holds Fez 1033-1038 (Banu Ifran page; 1033 Fez massacre page). Both dossiers draw Fez 1033-1038.
- missing: banu-ifran 1038 loss -> maghrawa; mirror none. IN-BATCH: see 1033.
- exception: kingdom-of-kuku 1520 gain -> regency-of-algiers; mirror none. regency-of-algiers dossier starts 1706 (Cliopatria row); 1516-1705 lies in the Ottoman row; author flagged. Route to me-10/af-08.
- exception: kingdom-of-kuku 1525 loss -> regency-of-algiers; mirror none. as 1520.
- missing: hafsids-of-bejaia 1309 gain -> hafsid-dynasty; mirror none. hafsid-dynasty has no 1309 loss of Tunis to the Bejaia branch.
- missing: hafsids-of-bejaia 1310 loss -> hafsid-dynasty; mirror none. hafsid-dynasty has no matching event (and the year is a c1 bridge; 1311 is the usual date).
- mismatch: hafsids-of-bejaia 1318 merge -> hafsid-dynasty; mirror hafsid-dynasty 1318 merge. hafsid-dynasty 1318 merge names the free-text "Hafsid branch of Bejaia and Constantine"; should name hafsids-of-bejaia.
- missing: hafsids-of-bejaia 1350 split -> hafsid-dynasty; mirror none. hafsid-dynasty has no 1350 split.
- mismatch: hafsids-of-bejaia 1370 merge -> hafsid-dynasty; mirror hafsid-dynasty 1370 merge. hafsid-dynasty 1370 merge names "Hafsid branch of Tunis"; should name hafsids-of-bejaia.
- missing: hafsids-of-bejaia 1501 split -> hafsid-dynasty; mirror none. hafsid-dynasty has no 1501 split (c1 here; the page names a 1436 revolt instead).
- matched: hafsids-of-bejaia 1510 loss -> spanish-bougie; mirror spanish-bougie 1510 found. 
- matched: hafsids-of-bejaia 1510 loss -> kingdom-of-beni-abbas; mirror kingdom-of-beni-abbas 1510 found. 
- exception: spanish-bougie 1555 loss -> regency-of-algiers; mirror none. as kingdom-of-kuku 1520: regency-of-algiers has no dossier before 1706.
- matched: masaesyli -203 loss -> kingdom-of-numidia; mirror kingdom-of-numidia -202 found. 
- matched: spanish-tripoli 1530 loss -> hospitaller-tripoli; mirror hospitaller-tripoli 1530 found. 
- exception: spanish-tunis 1535 vassal_start -> hafsid-dynasty; mirror none. vassalage recorded on the suzerain (schema); hafsid-dynasty instead records the 1535 events under crown-of-castile/spanish-empire (author flagged); route.
- exception: spanish-tunis 1569 vassal_end -> hafsid-dynasty; mirror none. as 1535.
- mismatch: spanish-presidios-of-morocco 1610 gain -> saadi-sultanate; mirror saadi-sultanate 1610 loss. saadi-sultanate has the 1610 loss of Larache but names spanish-empire; should name spanish-presidios-of-morocco.
- mismatch: spanish-presidios-of-morocco 1614 gain -> saadi-sultanate; mirror saadi-sultanate 1614 loss. saadi-sultanate has the 1614 loss of La Mamora but names spanish-empire.
- mismatch: spanish-presidios-of-morocco 1681 loss -> morocco; mirror morocco 1684 gain. morocco has no 1681 gain of Mehdya (only 1684 Tangier from english-colonial-empire).
- missing: spanish-presidios-of-morocco 1689 loss -> morocco; mirror none. morocco has no 1689 gain of Larache.
- missing: spanish-presidios-of-morocco 1692 loss -> morocco; mirror none. morocco has no 1692 gain of Asilah.
- missing: banu-khazrun 1075 gain -> hammadid-dynasty; mirror none. hammadid-dynasty has no 1075 loss / 1076 gain (M'Sila, M'zab, Righ).
- missing: banu-khazrun 1076 loss -> hammadid-dynasty; mirror none. as 1075.
- mismatch: banu-khazrun 1146 loss -> kingdom-of-africa; mirror kingdom-of-africa 1146 found. kingdom-of-africa found event of 1146 names zirid-dynasty for Tripoli; should name banu-khazrun.
- matched: banu-thabit 1369 gain -> banu-makki; mirror banu-makki 1369 loss. 
- mismatch: banu-thabit 1401 loss -> hafsid-dynasty; mirror hafsid-dynasty 1401 gain. hafsid-dynasty 1401 gain of Tripoli names nobody; should name banu-thabit.
- matched: banu-makki 1369 loss -> banu-thabit; mirror banu-thabit 1369 gain. 
- missing: banu-makki 1394 loss -> hafsid-dynasty; mirror none. hafsid-dynasty has no 1394 gain of Gabes/Sfax from banu-makki.

## Gazetteer names needed

- Iligh (Illigh) (place, zawiya-of-illigh): Anti-Atlas, about 29.8 N 9.5 W; NOTE the author report hint (-6.0 E 30.4 N, 110 km) is the Draa-valley circle, not Iligh
- Draa valley (region, zawiya-of-illigh): drawn as a 110 km circle at -6.0, 30.4
- Sokna (Sukna) (place, awlad-muhammad-dynasty)
- Dila (Zawiya of Dila) (place, dila-iya-sultanate)
- Asilah (Arzila) (place, portuguese-morocco)
- Mehdya (La Mamora) (place, portuguese-morocco)
- Ksar es-Seghir (place, portuguese-morocco)
- Azemmour (place, portuguese-morocco)
- Tamesna (region, banu-ifran)
- Siga (place, masaesyli): 35.2663 N 1.4499 W (Siga page)
- Kuku (Koukou) (place, kingdom-of-kuku)
- Kalaa of Ait Abbas (place, kingdom-of-beni-abbas)
- Ashir (Achir) (place, banu-khazrun)
- Tolga (place, kingdom-of-beni-abbas)
- Waghlana (place, banu-khazrun)

## Counterparts needing dossiers

- Sharifian sultanate of Fez (sharifian-sultanate-of-fez, 1465..1471): possible 1471 counterpart of portuguese-morocco (Asilah, Tangier)
- Massylii kingdom of Gala (massylii, -213..-206)
- Tajura resistance (Aydin Reis) (tajura, 1526..1551)
- Oea (Tripoli) (oea, 69..69)
- Leptis Magna (leptis-magna, 69..69)
- Regency of Algiers before its Cliopatria row (1516-1705) (regency-of-algiers, 1516..1705): extension of the existing dossier, not a new slug: counterparts of kingdom-of-kuku 1520/1525, spanish-bougie 1555 and kingdom-of-beni-abbas wars point at years the dossier does not cover

## Problems

- Fetch failure: https://en.wikipedia.org/wiki/Siga_(ancient_city) returned 404; https://en.wikipedia.org/wiki/Siga was used.
- Verdict 'fix' here means fixed by the reviewer (5 small edits, all re-validated with 0 errors and 0 warnings: kingdom-of-altava, masaesyli, banu-thabit, plus applied fixes inside maghrawa and banu-ifran, which stay 'thin' for unapplied non-blocking items). No unapplied blocking finding; no fabricated or mis-dated confidence-3 event was found in 115 spot checks (every confidence-3 event of the batch except a few in portuguese-morocco and exarchate-of-africa).
- Schema vs reviewer brief: vassal_start/vassal_end are recorded on the suzerain with the vassal as counterpart, so dila-iya-sultanate 1641/1661 and spanish-tunis 1535/1569 have no mirror in the vassal by design (status exception).
- Most unmatched events are in sibling dossiers of af-02 a-f that use Cliopatria or free-text counterparts (portuguese-africa, spanish-empire, crown-of-castile, kingdom-of-portugal, Hafsid/Bejaia strings, regency-of-algiers before 1706); the author listed them in its notes; routed in cross_checks.
- maghrawa /ledger indices from 4 on are one higher than in the author report because of the inserted 993 loss.
