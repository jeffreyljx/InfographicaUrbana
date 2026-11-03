# Review of batch se-02-d (2026-10-19)

Reviewer: adversarial review, Phase B. Dossiers: Malacca, Palembang, Sulu, Demak, Cirebon, Cebu. All six validate with --resolve (0 errors; Cirebon keeps 3 warnings for successor slugs without dossiers). The reviewer applied three small fixes (marked applied); everything else is for the author.

## Verdicts

### sultanate-of-malacca: fail
- [BLOCKING] `/keyframe_review/3/correction`: The 1512-1528 keyframe keeps Cliopatria's whole 230,357 km2 shape (minus the town) as the exile court's 'claimed sphere', with no loss of the peninsula or Sumatran lands after the fall of Malacca. Evidence: The page the keyframe note cites, Capture of Malacca (1511), infobox Result: 'Destruction of the Malacca Sultanate; independence of Kampar, Pahang, and others'. The ledger loses only the town (/ledger/11) and ends the Siak vassalage (/ledger/12), so Pahang, Kampar, Indragiri, Jambi, Kelantan, Perak, Selangor and Negeri Sembilan stay Malaccan to 1528 against the page. Fix: Replace the 1512 correction with what the exiled sultan held (the Muar camp 1511-1512, Bintan and the nearby Riau islands 1513-1526, Kampar 1526-1528, with a page for each) and add 1511 loss events (counterpart nobody or the newly independent states, confidence 2-3 from the Capture infobox) for Pahang, Kampar and the other provinces; keep any province only with a page that says it stayed loyal.
- [BLOCKING] `/ledger (after /ledger/7, year 1470)`: No event for Pahang ceasing to be direct Malaccan land in 1470, when it became a separate sultanate and Malacca's vassal; Pahang stays direct land in the 1459 correction and the 1512 shape. Evidence: Pahang Sultanate page (opened by the author): Muhammad Shah 'was installed as sultan around 1470'; infobox 'Established: 1470' and 'Vassal state of the Malacca Empire (1470-1511)'. Fix: Add 1470 loss of {admin1: Pahang} (counterpart: the Pahang sultanate, e.g. 'old-pahang-sultanate', confidence 2) and vassal_start with the same counterpart in 1470, vassal_end in 1511 (Capture infobox: 'independence of ... Pahang'); take Pahang out of the 1512 correction.
- [to do] `/ledger/16/region`: The 1528 split to Johor hands on all of Kepulauan Riau, including Bintan, which /ledger/14 says Malacca lost in 1526 (confidence 3). Evidence: Capture of Malacca (1511): the Portuguese 'devastated Bintan in 1526, returning it to its previous ruler and vassalizing the kingdom'. Fix: Subtract {place: Tanjungpinang, km: 35} from the split region, or explain in the note how Bintan came back before 1528.
- [to do] `/ledger/5/region and /ledger/6`: Siak is drawn twice in 1477: inside the direct gain {place: Pekanbaru, km: 150} and as a vassal {place: Pekanbaru, km: 120}. Evidence: Malacca Sultanate page: Mansur Shah 'was also able to vassalise Siak' and 'later added Kampar and Siak to his realm'; one status has to be chosen for the same land. Fix: Either subtract the Siak circle from the /ledger/5 gain or drop the vassal pair /ledger/6 and /ledger/12.
- [to do] `/identity/predecessors`: kingdom-of-singapura names sultanate-of-malacca as its successor and as the counterpart of its 1398 dissolve, while Malacca has no predecessor. Evidence: kingdom-of-singapura ledger/4: 1398 dissolve, counterpart sultanate-of-malacca; Malacca's own notes say no land passed (Parameswara fled). Fix: Add kingdom-of-singapura as a predecessor with a note that no land passed, or ask the Singapura owner (se-02) to drop Malacca from its successors; one of the two must change.
- [to do] `/ledger`: No vassal-side event for Malacca's tributary relation with the Ming from 1405, which the notes mention and set aside. Evidence: Notes: 'Malacca paid tribute to the Ming from 1405 with a promise of protection (Malacca page)'; elsewhere in the project the vassal side records tributary relations (jk-01-b review, Chuzan). Fix: Optional: add vassal_start 1405 / vassal_end 1511 with counterpart ming-dynasty at confidence 2, or keep the note.
- [thin] `/ledger/1`: year and extent of the coast 'from Kuala Linggi to Kuala Kesang' (confidence 1, 1424) (try https://en.wikipedia.org/wiki/Megat_Iskandar_Shah)
- [thin] `/ledger/3`: date of the Dindings-to-Johor coast under Muzaffar Shah (confidence 1, 1459) (try https://en.wikipedia.org/wiki/Muzaffar_Shah_of_Malacca)
- [thin] `/ledger/4`: date of Perak, Singapore and Bintan coming under Malacca (confidence 1, 1477) (try https://en.wikipedia.org/wiki/Mansur_Shah_of_Malacca)
- [thin] `/ledger/5`: year Majapahit handed Indragiri, Jambi, Tungkal and Siantan to Malacca (confidence 1, 1477) (try https://en.wikipedia.org/wiki/Indragiri_Sultanate)
- [thin] `/ledger/6`: year Siak became Malacca's vassal (confidence 1) (try https://en.wikipedia.org/wiki/Siak_Sultanate)
- [thin] `/ledger/7`: year the Riau-Lingga islands came under Malacca (confidence 1, 1488) (try https://en.wikipedia.org/wiki/Alauddin_Riayat_Shah_of_Malacca)
- [thin] `/ledger/10`: extent of the 1511-1512 Muar camp and the contest zone (confidence 1) (try https://en.wikipedia.org/wiki/Portuguese_Malacca)
- [spot check] `/ledger/2` confirmed: 'proceeded to Pahang and conquered it in 1454' (https://en.wikipedia.org/wiki/Pahang_Sultanate)
- [spot check] `/ledger/8` confirmed: 'as late as 1506, when it conquered Kelantan' (https://en.wikipedia.org/wiki/Malacca_Sultanate)
- [spot check] `/ledger/14` confirmed: 'devastated Bintan in 1526, returning it to its previous ruler and vassalizing the kingdom' (https://en.wikipedia.org/wiki/Capture_of_Malacca_(1511))
- [spot check] `/ledger/5` confirmed: 'hand over control of Indragiri, Jambi, Tungkal and Siantan to Malacca', undated in Mansur Shah's reign; confidence 1 is honest (https://en.wikipedia.org/wiki/Malacca_Sultanate)
- [spot check] `/keyframe_review/3/note` not on page: the infobox says the opposite of a surviving 230,357 km2 sphere: 'independence of Kampar, Pahang, and others' (https://en.wikipedia.org/wiki/Capture_of_Malacca_(1511))
- [area] no infobox area on the article; Cliopatria max 230356.8 km2

### sultanate-of-palembang: fix
- [APPLIED] `/ledger/2/counterpart`: The late-17th-century gain of Bangka named 'nobody' as counterpart. Evidence: Bangka Island page: Bangka 'continued to pass to the Banten Sultanate' and was then 'inherited by the nearby Palembang Sultanate sometime in the late 17th century'. Fix: Counterpart set to sultanate-of-banten and the reason appended to the note (done by the reviewer; validates).
- [to do] `/ledger (1518 and 1546)`: No vassal-side events mirror demak-sultanate's vassal_start sultanate-of-palembang (1518) and vassal_end (1546). Evidence: Demak Sultanate page: Raden Patah 'gained overlordship of the ports of Jambi and Palembang'; Palembang Sultanate page: c. 1513 Tome Pires describes 'a patron who was appointed from Java ... the Sultanate of Demak', and the infobox reads 'Preceded by Demak Sultanate'. The project records the vassal side with the overlord as counterpart. Fix: Add vassal_start 1518 and vassal_end 1546, counterpart demak-sultanate, region {cliopatria: 'Sultanate of Palembang', year: 1512}, confidence 1, source the Demak page (add it to sources); mention the infobox's 'Preceded by Demak Sultanate' in notes.
- [thin] `/ledger/0`: any dated founding or extent of the pre-1659 Palembang principality (confidence 1, 1459 is Cliopatria's year) (try https://en.wikipedia.org/wiki/Palembang)
- [thin] `/ledger/2`: the year Bangka passed from Banten to Palembang (confidence 1, 'late 17th century') (try https://en.wikipedia.org/wiki/Bangka_Belitung_Islands)
- [spot check] `/ledger/1` confirmed: 'It was proclaimed in 1659 by Susuhunan Abdurrahman' (https://en.wikipedia.org/wiki/Palembang_Sultanate)
- [spot check] `/ledger/3` confirmed: 'His successor ceded Bangka to Britain in 1812' (https://en.wikipedia.org/wiki/Bangka_Island)
- [spot check] `/ledger/4` confirmed: Second Expedition 1821, 'Dutch rule would last from June 1821' (https://en.wikipedia.org/wiki/Palembang_Sultanate)
- [spot check] `/ledger/2` confirmed: 'sometime in the late 17th century'; counterpart corrected to Banten (https://en.wikipedia.org/wiki/Bangka_Island)
- [area] no infobox area on the article; Cliopatria max 77003.3 km2

### sultanate-of-sulu: fix
- [to do] `/keyframe_review/4/correction`: The 1673 correction adds all of Palawan province, which no earlier keyframe holds, and no ledger event gains it between the 1529 and 1673 keyframes; the whole admin1 also takes in the Calamianes and Cuyo, which Spain held earlier. Evidence: Sultanate of Sulu page: Sulu 'totally gave up its domain over Palawan to Spain in 1705' (so Sulu held it before) but the page gives no acquisition year; sultanate-of-brunei ledger/8 loses north Palawan to Spain in 1629. Fix: Add a confidence-1 gain of southern Palawan (counterpart sultanate-of-brunei, year 1673 or the year a page gives) and restrict the Palawan part of the correction and of /ledger/3 to the south of the island.
- [to do] `/ledger (1457-1578 and 1851)`: No vassal-side events for Sulu's two overlord relations in the infobox: Bruneian vassal 1457-1578 and Spanish protectorate from 1851. Evidence: Sulu infobox status: 'Bruneian vassal (1457-1578) Sovereign state (1578-1851) Spanish protectorate (1851-1899)'; sultanate-of-brunei carries vassal_start sultanate-of-sulu 1507 (c1) and vassal_end 1578 (c2). Fix: Add vassal_start/vassal_end with counterpart sultanate-of-brunei (1457, confidence 2; 1578, confidence 3) and vassal_start spanish-empire 1851 paired with a vassal_end at 1878-07; note Brunei's 1507 start.
- [thin] `/ledger/1`: when Tawi-Tawi and Basilan came under Sulu (confidence 1, 1529 is Cliopatria's year) (try https://en.wikipedia.org/wiki/Tawi-Tawi)
- [thin] `/keyframe_review/4`: when Sulu acquired southern Palawan (try https://en.wikipedia.org/wiki/History_of_Palawan)
- [thin] `/keyframe_review/7`: the two southern cells Cliopatria drops in 1830 (try https://en.wikipedia.org/wiki/Sultanate_of_Bulungan)
- [spot check] `/ledger/2` confirmed: 'granted the north-eastern part ... for helping the Sultan of Brunei ... against his enemies in 1704' (https://en.wikipedia.org/wiki/North_Borneo_dispute)
- [spot check] `/ledger/3` confirmed: 'gave up its domain over Palawan to Spain in 1705 and Basilan to Spain in 1762' (also confirms /ledger/4) (https://en.wikipedia.org/wiki/Sultanate_of_Sulu)
- [spot check] `/ledger/8` confirmed: 'signed by Sultan Jamal ul-Azam of Sulu on 22 January 1878' (https://en.wikipedia.org/wiki/North_Borneo_dispute)
- [spot check] `/ledger/5` confirmed: infobox 'Vassal of the Sultanate of Sulu (1789-1855)'; 'Sulu sacked both Berau and Tarakan in 1789' (https://en.wikipedia.org/wiki/Sultanate_of_Bulungan)
- [area] no infobox area on the article; Cliopatria max 68285.6 km2

### demak-sultanate: fix
- [to do] `/ledger (1475 and 1478)`: No vassal-side events mirror majapahit's vassal_start demak-sultanate 1475 and vassal_end 1478 (both confidence 3). Evidence: Demak infobox: vassal of Majapahit 1475-1478, independence 1478; majapahit ledger/29 and /30. Fix: Add vassal_start 1475 and vassal_end 1478, counterpart majapahit, region {cliopatria: 'Demak Sultanate', year: 1475}, confidence 3, source the Demak page.
- [to do] `/ledger (1482 and 1546)`: Demak's overlordship of Cirebon is recorded on neither side. Evidence: Sultanate of Cirebon infobox status: 'Puppet state of Demak (1479-1546)'. Fix: Add vassal_start 1482 (Cirebon's start) and vassal_end 1546, counterpart sultanate-of-cirebon, region {cliopatria: 'Sultanate of Cirebon', year: 1482}, confidence 2, source the Cirebon page (add to sources).
- [to do] `/ledger/6/counterpart`: The c. 1527 gain of Tuban names majapahit, whose dossier dissolves in 1518 with Demak as counterpart. Evidence: majapahit ledger/32: 1518 dissolve, counterpart demak-sultanate; Demak page calls Tuban only 'an old Majapahit port' conquered 'in about 1527'. Fix: Set the counterpart to nobody (an independent port by 1527) or to whichever ruler a page names; keep confidence 2.
- [to do] `/ledger/5`: sunda-kingdom records the 1527 loss of Sunda Kalapa to demak-sultanate (confidence 3), but Demak records only a contest 1527-1531 and no gain, so nobody holds the port after 1531. Evidence: sunda-kingdom ledger/10; Banten Sultanate page: Gunungjati and his son 'took control of both the port of Banten and Kelapa', and the VOC took Jayakarta 'from Banten in 1619'. Fix: Agree with the Sunda owner: either Demak gains Sunda Kalapa in 1527, or (better on the Banten page) Sunda's counterpart becomes sultanate-of-cirebon/sultanate-of-banten and Demak's notes say so.
- [thin] `/ledger/2`: dated extent of Demak's Central Java hinterland (confidence 1, bridged from the 1519 shape) (try https://en.wikipedia.org/wiki/Raden_Patah)
- [thin] `/ledger/3`: year of Demak's overlordship of Palembang (confidence 1) (try https://en.wikipedia.org/wiki/Palembang_Sultanate)
- [thin] `/ledger/4`: year of Demak's overlordship of Jambi (confidence 1) (try https://en.wikipedia.org/wiki/Jambi_Sultanate)
- [thin] `/ledger/8`: end of the Palembang overlordship (confidence 1, 1546 is Trenggana's death) (try https://en.wikipedia.org/wiki/Trenggana)
- [thin] `/ledger/9`: end of the Jambi overlordship (confidence 1) (try https://en.wikipedia.org/wiki/Trenggana)
- [spot check] `/ledger/1` confirmed: 'Between 1513 and 1518 Demak waged war against Patih Udara of Daha'; Daha defeated 1518 (https://en.wikipedia.org/wiki/Demak_Sultanate)
- [spot check] `/ledger/5` confirmed: 1527, Fatahillah sent to take Banten and Sunda Kelapa (https://en.wikipedia.org/wiki/Demak_Sultanate)
- [spot check] `/ledger/6` confirmed: Tuban 'conquered in about 1527' (https://en.wikipedia.org/wiki/Demak_Sultanate)
- [spot check] `/ledger/10` confirmed: 1568, Hadiwijaya 'moved all of Demak's regalia ... to Pajang' (https://en.wikipedia.org/wiki/Demak_Sultanate)
- [area] no infobox area on the article; Cliopatria max 45552.5 km2

### sultanate-of-cirebon: fix
- [APPLIED] `/wars/3/to`: The war 'Banten's hold on Cirebon and its loss' ran to 1680, past the state's end (1677). Evidence: Reviewer rule: wars inside the life; the Banten page gives the crowning of the princes in 1677 and only 'two years of war' after it, which belongs to the successor sultanates. Fix: Clipped to 1677 with a note (done by the reviewer; validates).
- [APPLIED] `/identity/rulers/0/from`: Sunan Gunungjati's reign began in 1479, before the dossier's start (April 1482). Evidence: Cirebon infobox: '1479-1568: Syarif Hidayatullah'; the dossier starts at the 2 April 1482 declaration (Sunda Kingdom page). Fix: Clipped to 1482 with the infobox year kept in the note (done by the reviewer; validates).
- [to do] `/ledger (1482-1546 and 1613-1677)`: No vassal-side events for the two overlord relations in Cirebon's own infobox. Evidence: Cirebon infobox status: 'Puppet state of Demak (1479-1546)' and 'Vassal of the Mataram Sultanate (1613-1705)'; 'Cirebon under the rule of Mataram Sultanate: 1613'. Fix: Add vassal_start 1482 / vassal_end 1546 with counterpart demak-sultanate (confidence 2) and vassal_start 1613 / vassal_end 1677 with counterpart mataram-sultanate (confidence 2); the notes' 1595 (Mataram page) can stay as the disagreement.
- [spot check] `/ledger/0` confirmed: 'On 2 April 1482, Sunan Gunungjati stated that Cirebon will no longer send tribute to Pajajaran' (https://en.wikipedia.org/wiki/Sunda_Kingdom)
- [spot check] `/ledger/1` confirmed: infobox 'De jure province of Cirebon Sultanate (1526-1552)', 'Syarif Hidayatullah conquered Banten: 1526' (https://en.wikipedia.org/wiki/Banten_Sultanate)
- [spot check] `/ledger/2` confirmed: 'Independence from Cirebon Sultanate: 1552' (https://en.wikipedia.org/wiki/Banten_Sultanate)
- [spot check] `/ledger/3` confirmed: 1677 'all three sons of Panembahan Girilaya inherited'; formal division into Kasepuhan and Kanoman 1679 (https://en.wikipedia.org/wiki/Sultanate_of_Cirebon)
- [area] no infobox area on the article; Cliopatria max 30571.9 km2

### rajahnate-of-cebu: pass
Tried and could not break: All three events opened and confirmed; start c. 1400 and end 27 April 1565 match the infobox and the Legazpi page; the island-wide region matches Sialo, Nahalin and Singhapala on the page; the 1564 keyframe is clipped to 1565 with an unchanged correction; the only disagreement is spanish-empire's counterpart (cross_checks).
- [spot check] `/ledger/0` confirmed: infobox 'c. 1400-1565' (https://en.wikipedia.org/wiki/Rajahnate_of_Cebu)
- [spot check] `/ledger/1` confirmed: 'On 27 April 1565, the expedition returned to Cebu and landed there'; 'Rajah Tupas challenged the Spaniards, but was overpowered' (https://en.wikipedia.org/wiki/Miguel_L%C3%B3pez_de_Legazpi)
- [spot check] `/ledger/2` confirmed: 'dissolved during the reign of Rajah Tupas ... in the battle of Cebu during 1565' (https://en.wikipedia.org/wiki/Rajahnate_of_Cebu)
- [area] no infobox area on the article; Cliopatria max 6669.4 km2

## Cross-dossier matrix

- sultanate-of-malacca 1454 gain (Pahang (Ligor's vassal)) / mirror: none / **exception**: listed in the author's counterparts_needing_dossiers (kingdom-of-pahang)
- sultanate-of-malacca 1477 gain (majapahit) / mirror: majapahit 1406 vassal_end / **mismatch**: Majapahit's ledger ends its Sumatran vassalage in 1406 and has no 1477 loss of Indragiri/Jambi/Tungkal/Siantan; the Malacca page dates the hand-over only to Mansur Shah's reign (1459-1477). Route to the majapahit owner (se-02).
- sultanate-of-malacca 1477 vassal_start (Siak) / mirror: none / **exception**: listed (siak-kingdom)
- sultanate-of-malacca 1506 gain (Kelantan (pre-1506 polity)) / mirror: none / **exception**: listed (kelantan-early-polity)
- sultanate-of-malacca 1511 loss (portuguese-empire) / mirror: portuguese-empire 1511 gain / **matched**: months disagree: Malacca 8 (15 August, Capture infobox), Portugal 7; Portugal's region is 50 km, Malacca's 15 km. Portugal (am-06) should use month 8.
- sultanate-of-malacca 1526 loss (portuguese-empire) / mirror: none / **missing**: portuguese-empire has no 1526 event for Bintan; the Capture page says Portugal vassalised Bintan in 1526 (a vassal_start on Portugal's side). Route to am-06.
- sultanate-of-malacca 1528 split (sultanate-of-johor) / mirror: none / **exception**: counterpart owned by se-02 part not yet run (no dossier)
- sultanate-of-malacca 1528 split (sultanate-of-perak) / mirror: none / **exception**: counterpart owned by se-02 part not yet run (no dossier)
- kingdom-of-singapura 1398 dissolve (sultanate-of-malacca) / mirror: sultanate-of-malacca None predecessor / **mismatch**: Singapura names Malacca as successor; Malacca lists no predecessor (its notes: no land passed).
- sultanate-of-palembang 1670 gain (sultanate-of-banten) / mirror: none / **exception**: counterpart changed from nobody by the reviewer (Bangka Island page); Banten (se-02) not yet written
- sultanate-of-palembang 1812 loss (british-colonial-empire) / mirror: none / **exception**: owned by eu-11, no dossier yet
- demak-sultanate 1518 vassal_start (sultanate-of-palembang) / mirror: none / **missing**: Palembang has no vassal-side event (fix listed on Palembang); same for the 1546 vassal_end
- demak-sultanate 1518 vassal_start (Jambi (before the sultanate)) / mirror: none / **exception**: listed (jambi-kingdom)
- majapahit 1475 vassal_start (demak-sultanate) / mirror: none / **missing**: Demak has no vassal-side vassal_start majapahit 1475 / vassal_end 1478 (fix listed on Demak)
- demak-sultanate 1518 gain (majapahit) / mirror: majapahit 1518 dissolve / **matched**: Majapahit dissolves in 1518 with demak-sultanate as counterpart (Daha); covers both 1518 gains
- demak-sultanate 1527 gain (majapahit) / mirror: majapahit 1518 dissolve / **mismatch**: Majapahit no longer exists in 1527 in its own dossier; Demak's Tuban counterpart should change
- sunda-kingdom 1527 loss (demak-sultanate) / mirror: demak-sultanate 1527 contest_start / **mismatch**: Sunda loses Sunda Kalapa to Demak (c3); Demak records only a contest 1527-1531 and no gain. Banten page gives the port to Gunungjati and his son (Cirebon/Banten). Route to the sunda-kingdom owner and the Demak author.
- sultanate-of-cirebon 1482 vassal_start (demak-sultanate) / mirror: none / **missing**: Cirebon infobox 'Puppet state of Demak (1479-1546)': neither Demak nor Cirebon records it (fixes listed on both)
- sultanate-of-cirebon 1482 found (sunda-kingdom) / mirror: sunda-kingdom 1482 loss / **matched**: both April 1482
- sultanate-of-cirebon 1526 vassal_start (sultanate-of-banten) / mirror: none / **exception**: Banten (se-02) not yet written; sunda-kingdom loses Banten to sultanate-of-banten in 1527 (c2), one year off Cirebon's 1526
- sultanate-of-cirebon 1613 vassal_start (mataram-sultanate) / mirror: none / **missing**: Cirebon infobox 'Vassal of the Mataram Sultanate (1613-1705)'; Cirebon has no vassal-side event; mataram-sultanate (se-02) not yet written
- sultanate-of-cirebon 1677 split (kasepuhan-sultanate / kanoman-sultanate / keprabonan-sultanate) / mirror: none / **exception**: listed in counterparts_needing_dossiers
- sunda-kingdom 1579 dissolve (sultanate-of-banten) / mirror: sultanate-of-cirebon None successor / **mismatch**: Sunda lists sultanate-of-cirebon among its successors, but Cirebon's 1579-1676 corrections remove Sunda's last 83 cells and gain nothing from Sunda; the Sunda owner should drop Cirebon or say what it got.
- sultanate-of-sulu 1704 gain (sultanate-of-brunei) / mirror: sultanate-of-brunei 1673 loss / **mismatch**: 31 years apart: North Borneo dispute page gives 1704 (confirmed); Brunei's 1673 loss (c2) follows Cliopatria. Route to the Brunei owner (se-02).
- sultanate-of-sulu 1705 loss (spanish-empire) / mirror: none / **missing**: spanish-empire has no 1705 gain of Palawan (am-06)
- sultanate-of-sulu 1762 loss (spanish-empire) / mirror: none / **missing**: spanish-empire has no gain of Basilan (1724, 1762 or 1845) (am-06)
- sultanate-of-sulu 1789 vassal_start (kingdom-of-bulungan) / mirror: none / **exception**: Bulungan owned by se-03, not yet written
- sultanate-of-sulu 1876 occupation_start (spanish-empire) / mirror: spanish-empire 1876 contest_start / **mismatch**: Sulu records an occupation of Jolo, Spain a contest over the Philippine part of the sultanate; one type should be agreed
- sultanate-of-sulu 1878 dissolve (spanish-empire) / mirror: spanish-empire 1878 vassal_start / **mismatch**: July 1878: Sulu ends the state and hands the land to Spain; Spain records Sulu as its vassal from the same month. Sulu infobox: Spanish protectorate 1851-1899. Agree on one.
- sultanate-of-sulu 1878 loss (British North Borneo Company (Overbeck and Dent)) / mirror: none / **exception**: listed (british-north-borneo-company, se-03)
- sultanate-of-brunei 1507 vassal_start (sultanate-of-sulu) / mirror: none / **missing**: Sulu has no vassal-side event (infobox: Bruneian vassal 1457-1578); also 50 years apart at the start
- rajahnate-of-cebu 1565 loss (spanish-empire) / mirror: spanish-empire 1565 gain / **mismatch**: same month (April 1565) but Spain's gain names counterpart 'nobody'; it should name rajahnate-of-cebu (am-06)

## Counterparts needing dossiers

- Pahang Sultanate (1470-1623), Malacca's vassal from 1470: `old-pahang-sultanate` [1470, 1623]
- Bintan kingdom (Portuguese vassal from 1526): `kingdom-of-bintan` [1526, 1528]

## Gazetteer names needed

- Bintan (place, sultanate-of-malacca)
- Dindings (region, sultanate-of-malacca)
- Kampar (region, sultanate-of-malacca)
- Siak (region, sultanate-of-malacca)
- Indragiri (region, sultanate-of-malacca)
- Buansa (place, sultanate-of-sulu)

## Problems

- No article in this batch has an infobox area, so every area_check is empty; the comparison could not be made.
- Reviewer applied three small fixes: sultanate-of-palembang /ledger/2 counterpart, sultanate-of-cirebon /wars/3/to and /identity/rulers/0/from; all re-validated (0 errors).
- Neighbour dossiers not yet written (counterpart groups not run): sultanate-of-johor, sultanate-of-banten, sultanate-of-perak, sultanate-of-aceh, dutch-republic, mataram-sultanate, sultanate-of-jambi, blambangan-kingdom, dutch-east-indies, sultanate-of-maguindanao, kingdom-of-pajana, kingdom-of-bulungan, british-colonial-empire and the other Context rows; read: spanish-empire, sultanate-of-brunei, sunda-kingdom, ayutthaya-kingdom, majapahit, portuguese-empire, sultanate-of-kedah, rattanakosin-kingdom, thonburi-kingdom, plus kingdom-of-singapura and tondo.
- WebFetch summarises pages; quotations above are as the fetch returned them.
