# Review of batch se-02-c

Reviewer run of 2026-10-19. Dossiers: samudera-pasai-sultanate, majapahit, malaya, kingdom-of-singapura, sultanate-of-brunei, tondo. All six validate (0 errors) before and after the reviewer edits; the only warnings are counterpart slugs with no dossier yet (peureulak-sultanate, nan-sarunai).

Verdicts: samudera-pasai-sultanate **fail**, majapahit **fail**, malaya **thin**, kingdom-of-singapura **fix**, sultanate-of-brunei **fix**, tondo **pass**.

Meaning used here: `fix` = accepted with the reviewer-applied edits; items marked "applied: no" are non-blocking and the author should still do them. `fail` = at least one blocking item not applied; back to the author.

## samudera-pasai-sultanate: fail

Area: infobox has no area; Cliopatria max 8,675 km2.

Findings:

- `/keyframe_review/1/correction` (applied: no). The correction of shape samudera-pasai-sultanate_1272 (held 1272-1351) adds Peureulak (Langsa 70 km) from 1272, but /ledger/1 gains Peureulak only in 1292, so the keyframe draws Peureulak as Pasai 20 years before the union and contradicts the ledger (and the future peureulak-sultanate dossier, alive to 1292). Evidence: Peureulak_Sultanate page: infobox Disestablished 1292; "Perlak was united with the Samudera Pasai Kingdom under the reign of Sultan Samudera Pasai ... Muhammad Malik Al Zahir". The correction text itself says "plus Peureulak (East Aceh) from 1292", which a region cannot encode. Fix: Set samudera-pasai-sultanate_1272 to verdict ok (shape as drawn, no correction) and let /ledger/1 add Peureulak in 1292; or add a new keyframe samudera-pasai-sultanate_1292 (from 1292, to 1351) carrying the union and make _1272 ok.
- `/ledger/1/region` (applied: no). Peureulak is drawn as a 70 km circle round Langsa, which reaches Langkat in North Sumatra (Pangkalan Susu about 47 km) and takes in Aceh Tamiang, the Karang Baru kingdom that /wars/1 treats as a separate state Pasai attacked. The same circle is in every keyframe union, /ledger/6, /ledger/7, /identity/predecessors and /identity/successors. Evidence: Langsa 4.47 N 97.97 E; Peureulak town 4.81 N 97.89 E; the Aceh/North Sumatra boundary runs about 4.1-4.2 N, 98.2 E. Fix: Use {"intersect": [{"place": "Langsa", "km": 45}, {"admin1": "Aceh", "country": "Indonesia"}], "text": "Peureulak, now the East Aceh Regency"} everywhere the circle appears (or Peureulak itself once the gazetteer has it).
- `/ledger` (applied: no). No vassal events mirror majapahit /ledger/5 (vassal_start samudera-pasai-sultanate 1350) and /ledger/20 (vassal_end 1406); Pasai has only the 1350 contest pair. Evidence: majapahit.json /ledger/5 and /ledger/20; Pasai page: Majapahit "attacked and looted the place in the middle of the 14th century"; Regreg_War page: "one by one Majapahit's overseas possessions outside of Java have liberated themselves". Fix: Add vassal_start counterpart majapahit 1350 (confidence 2, Majapahit page) and vassal_end majapahit 1406 (confidence 1, Regreg War page), region {"cliopatria": "Samudera Pasai Sultanate", "year": 1363}; or agree with the Majapahit author to drop the tint.
- `/wars` (applied: no). The Pasai rulers table has Zainal Abidin I (1394-1400) "Attacked by Majapahit"; no war or contest records it. Evidence: Samudera_Pasai_Sultanate page, rulers table. Fix: Optional: add a war "Majapahit attack on Pasai (1390s)" with empty zones and say no land changed hands.

Gaps for a gap-filler:

- `/ledger/6`: The Aceh page gives no annexation year; 1524 rests on the Pasai page alone (Cliopatria grows Aceh in 1526). Try https://en.wikipedia.org/wiki/Ali_Mughayat_Syah

Spot checks:

- `/ledger/1` https://en.wikipedia.org/wiki/Peureulak_Sultanate: confirmed (union under Muhammad Malik Al Zahir; year only from infobox Disestablished 1292)
- `/ledger/4` https://en.wikipedia.org/wiki/Samudera_Pasai_Sultanate: confirmed: "The Portuguese occupied Pasai in 1521"
- `/ledger/5` https://en.wikipedia.org/wiki/Samudera_Pasai_Sultanate: confirmed: "The Portuguese garrison evacuated Pasai in 1524"
- `/ledger/6` https://en.wikipedia.org/wiki/Samudera_Pasai_Sultanate: confirmed: infobox "Conquered by the Aceh Sultanate: 1524"; Ali Mughayat Syah "annexed the territory"

## majapahit: fail

Area: infobox has no area; author cuts the 1.0 M km2 shapes to Java, Bali and west Lombok (direct rule) and tints the rest; Cliopatria max 1,001,530 km2.

Findings:

- `/ledger/19` (applied: no). The 1406 gain (confidence 3) of Blambangan and Lumajang from blambangan-kingdom has no earlier loss: keyframes majapahit_1363 and majapahit_1402 keep all of Jawa Timur, so the ledger gains land the dossier already holds and the eastern court never appears. Evidence: Regreg_War page: the eastern court's origins are 1376-1377 (Ming chronicles describe "two independent Javanese kingdoms"; Wijayarajasa "built a new eastern court in Pamotan"); the formal break came in 1403 when Wirabhumi sought Chinese help and the Chinese court recognised the province's independence; 1406 "the eastern court was finally reunited with the western court". Fix: Add a loss (or split) in 1403 (confidence 2, Regreg War page) of the eastern court's land to the eastern court (blambangan-kingdom, or a new slug such as kedhaton-wetan, listed under counterparts_needing_dossiers), optionally a 1376 note; keep the 1406 gain; mark keyframe majapahit_1402 note for it.
- `/ledger/17/region` (applied: no). The Regreg War regions (/ledger/17, /ledger/18, /ledger/19 and the Regreg War zone) are a 90 km circle round Jember, which reaches west Bali (Gilimanuk about 81 km). Evidence: Jember 8.17 S 113.70 E; Gilimanuk 8.17 S 114.44 E. Fix: {"intersect": [{"place": "Jember", "km": 90}, {"admin1": "Jawa Timur", "country": "Indonesia"}], "text": "Blambangan and Lumajang"} in all four places.
- `/ledger/6/counterpart` (applied: yes). vassal_start 1352 (and /ledger/21 vassal_end 1406) named the slug malaya, but the malaya dossier ends in 1351, so the counterpart was dead for the whole tributary span. Evidence: malaya.json identity end 1351 and /ledger/2 dissolve 1351; History_of_Malaysia: "In the 14th century, the Hindu Majapahit Empire came into possession of the peninsula". Fix: Counterpart set to "Malay Peninsula principalities (Pahang, Kelantan, Terengganu, Johor)", as the author did for Sumatra and Borneo; reviewer note appended to both notes.
- `/wars` (applied: no). The contest pair /ledger/27 and /ledger/30 (Kertabhumi at Trowulan, 1468-1478) has no war; the Demak-Majapahit war starts in 1478. Evidence: Majapahit page: "In 1468 Prince Kertabhumi rebelled against Singhawikramawardhana"; "The year 1478 was the year of Sudarma Wisuta war". Fix: Add war "Kertabhumi's rebellion and the Sudarma Wisuta war", 1468-1478, belligerents majapahit and the Kertabhumi string, zone {"place": "Mojokerto", "km": 60}.

Gaps for a gap-filler:

- `/ledger/1`: Confidence 1, Cliopatria year 1294; kediri-kingdom dissolves in 1293 (within a year, kept so it agrees with keyframe majapahit_1293). Try https://en.wikipedia.org/wiki/Raden_Wijaya
- `/ledger/6`: Malay Peninsula tribute start 1352 is Cliopatria's year (Nagarakretagama is 1365). Try https://en.wikipedia.org/wiki/Nagarakretagama
- `/ledger/7`: Sumatra tribute start 1352 and who held south Sumatra 1294-1351 (Melayu/Dharmasraya, Adityawarman). Try https://en.wikipedia.org/wiki/Dharmasraya
- `/ledger/9`: Southern Borneo tribute 1362 (Negara Dipa). Try https://en.wikipedia.org/wiki/Negara_Dipa
- `/ledger/20`: Confidence 1 vassal_ends at 1406 (also /ledger/21, /ledger/25): no per-region dates. Try https://en.wikipedia.org/wiki/Regreg_War
- `/identity/rulers`: Gap 1429-1474 (Suhita, Kertawijaya, Rajasawardhana, Girishawardhana, Singhawikramawardhana). Try https://en.wikipedia.org/wiki/Suhita

Spot checks:

- `/ledger/4` https://en.wikipedia.org/wiki/Gajah_Mada: confirmed: "Soon he conquered the surrounding territory of Bedahulu (Bali) and Lombok (1343)"
- `/ledger/15` https://en.wikipedia.org/wiki/Majapahit: confirmed: "finally sacked and destroyed the Kingdom in 1398"
- `/ledger/19` https://en.wikipedia.org/wiki/Regreg_War: confirmed 1404-1406 and reunion in 1406, but the page also dates the eastern court from 1376-1377 and its independence to 1403 (missing loss, see fixes)
- `/ledger/28` https://en.wikipedia.org/wiki/Demak_Sultanate: confirmed: infobox "Vassal state of Majapahit (1475-1478)"
- `/ledger/31` https://en.wikipedia.org/wiki/Demak_Sultanate: confirmed: "Demak managed to consolidate its power by defeating Daha in 1518" (Majapahit infobox says 1527; author flagged)
- `/ledger/13` https://en.wikipedia.org/wiki/Majapahit: confirmed: 1377 punitive naval attack on Palembang

## malaya: thin

Area: "Malaya" is a disambiguation page; no infobox; Cliopatria max 143,936 km2.

Findings:

- `/wars/0` (applied: no). A "war" with no zones records Sukhothai's and Majapahit's claims, not fighting; the Sukhothai overlordship the page states is not in the ledger. Evidence: History_of_Malaysia: "By the late 13th century, the Siamese kings of Sukhothai had brought most of Malaya under their rule." sukhothai-kingdom.json has no event naming malaya. Fix: Replace the pseudo-war with vassal_start counterpart sukhothai-kingdom c. 1294 (confidence 2, region {"cliopatria": "Malaya", "year": 1294}) and a vassal_end at 1351 (confidence 1); the sukhothai-kingdom author adds the mirror.

Gaps for a gap-filler:

- `/ledger/0`: Confidence 1: no page dates a state called Malaya; the row is an aggregate of principalities. Try https://en.wikipedia.org/wiki/Pahang_Kingdom
- `/ledger/2`: Confidence 1: the 1351 end is Cliopatria's; Majapahit's possession is undated ("14th century"). Try https://en.wikipedia.org/wiki/Langkasuka
- `/identity`: The aggregate should be split into Pahang, Kelantan, Terengganu, Langkasuka/Patani, Johor (author agrees); Federation of Malaya (Q1479726) is a different state, correctly not merged. Try https://en.wikipedia.org/wiki/Kelantan_Sultanate

Spot checks:

- `/ledger/1` https://en.wikipedia.org/wiki/Kingdom_of_Singapura: confirmed: infobox "Founding of Temasek by Sang Nila Utama: 1299"
- `/ledger/0` https://en.wikipedia.org/wiki/History_of_Malaysia: confirmed quote (undated "late 13th century"; Srivijaya's last ruler "overthrown in 1288")
- `/ledger/2` https://en.wikipedia.org/wiki/History_of_Malaysia: confirmed quote, undated "14th century"

## kingdom-of-singapura: fix

Area: infobox has no area; Cliopatria max 691 km2.

Findings:

- `/ledger/0/counterpart` (applied: yes). The found event took the island from melayu-kingdom (no dossier, validator warning), while malaya.json /ledger/1 loses Singapore island to kingdom-of-singapura in 1299, so the pair did not match. Evidence: Kingdom_of_Singapura page: founder "a fleeing Palembang prince named Sang Nila Utama" (not called Melayu); infobox founding 1299; malaya /ledger/1. Fix: Counterpart set to malaya; reviewer note appended. predecessors still name melayu-kingdom for the dynasty, which is acceptable.

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Kingdom_of_Singapura: confirmed 1299
- `/ledger/1` https://en.wikipedia.org/wiki/Kingdom_of_Singapura: confirmed: "In 1398, Majapahit dispatched a fleet of 300 jong"
- `/ledger/2` https://en.wikipedia.org/wiki/Kingdom_of_Singapura: confirmed: "sacked by Majapahit in 1398 according to the Malay Annals" (Portuguese sources: Siam)
- `/ledger/4` https://en.wikipedia.org/wiki/Kingdom_of_Singapura: confirmed: infobox "Majapahit invasion and escape of Parameswara ...: 1396/1398"

## sultanate-of-brunei: fix

Area: Bruneian Empire infobox (1300s-1888) has no area; author removes Mindanao and Manila from the 1497-1581 shapes; Cliopatria max 230,860 km2.

Findings:

- `/ledger/24/region` (applied: yes). The 1890 Limbang loss was a 40 km circle round 4.75 N 115.0 E, which holds Bandar Seri Begawan (about 17 km) and most of Temburong, so the loss took the capital that keyframe sultanate-of-brunei_1890 keeps. Evidence: Limbang page: Limbang "sits on the Limbang River between the two halves of Brunei", the Temburong crossing about 15 km east, the Brunei-Muara crossing about 43 km west. Fix: Region set to {"intersect": [{"minus": [{"cliopatria": "Sultanate of Brunei", "year": 1885}, {"cliopatria": "Sultanate of Brunei", "year": 1987}]}, {"admin1": "Sarawak", "country": "Malaysia"}], "text": "Limbang"}; same for the Limbang annexation war zone (/wars/3/zones/0). Validated.
- `/ledger/22/region` (applied: yes). The 1885 Trusan loss was a 35 km circle round 4.8 N 115.35 E, which reaches Bangar in Temburong (about 33 km). Evidence: Bangar 4.71 N 115.07 E; Limbang page: "Brunei later agreed to cede Trusan in 1885". Fix: Region set to {"intersect": [{"minus": [{"cliopatria": "Sultanate of Brunei", "year": 1870}, {"cliopatria": "Sultanate of Brunei", "year": 1885}]}, {"admin1": "Sarawak", "country": "Malaysia"}], "text": "the Trusan district, by Lawas"}. Validated.
- `/ledger` (applied: no). No vassal events mirror majapahit /ledger/11 (vassal_start sultanate-of-brunei 1365, confidence 3) and /ledger/24 (vassal_end 1406). Evidence: Bruneian_Empire page: the Nagarakretagama, "written by Prapanca in 1365", "mentioned Barune as the vassal state of Majapahit". Fix: Add vassal_start counterpart majapahit 1365 (confidence 3, Bruneian Empire page) and vassal_end majapahit 1406 (confidence 2, Regreg War page), region {"cliopatria": "Sultanate of Brunei", "year": 1363}.
- `/keyframe_review/11/correction` (applied: no). Labuan is removed from 1842, but /ledger/13 cedes it in 1846 (same in _1859, _1868, _1870 only from 1846 is right). Evidence: History_of_Brunei: "Sultan Omar Ali Saifuddin II ceded Labuan to the British under the Treaty of Labuan" (1846). Labuan is about 92 km2, below a cell, so the effect is small. Fix: Make sultanate-of-brunei_1842 ok (as drawn) and let /ledger/13 remove Labuan in 1846.
- `/ledger/19` (applied: no). The North Borneo cessions after November 1884 (Kawang River February 1885, Mantanani Islands April 1885, minor Padas lands March 1898) are not in the ledger; the 1877-1884 Sabah events name british-colonial-empire while the author lists british-north-borneo as the counterpart needing a dossier. Evidence: North_Borneo page list of cessions. Fix: Add the 1885 cessions (confidence 3) and pick one counterpart for the Sabah events (british-north-borneo once it exists).

Gaps for a gap-filler:

- `/ledger/1`: Confidence 1 gains 1492 and 1502 (/ledger/2) under Bolkiah: only "the coastal areas of northwest Borneo", undated. Try https://en.wikipedia.org/wiki/Bolkiah
- `/ledger/3`: Sulu as Brunei vassal 1507 (confidence 1). Try https://en.wikipedia.org/wiki/Sultanate_of_Sulu
- `/ledger/8`: Palawan to Spain 1629 and 1842 (/ledger/12), confidence 1; Palawan under Brunei 1507-1841 unverified. Try https://en.wikipedia.org/wiki/History_of_Palawan
- `/ledger/7`: Sambas 1619 (confidence 1). Try https://en.wikipedia.org/wiki/Sambas_Sultanate
- `/ledger/16`: Sarawak cells 1868 and 1870 (/ledger/17), Bintulu, Mukah, Baram dates (confidence 1). Try https://en.wikipedia.org/wiki/Charles_Brooke,_Rajah_of_Sarawak
- `/wars`: The 1962 Brunei revolt (not on the pages opened) and the 1941-1945 Borneo campaigns. Try https://en.wikipedia.org/wiki/Brunei_revolt
- `/identity/rulers`: No ruler strip. Try https://en.wikipedia.org/wiki/List_of_sultans_of_Brunei

Spot checks:

- `/ledger/11` https://en.wikipedia.org/wiki/Raj_of_Sarawak: confirmed: "Hashim granted Sarawak to Brooke on 24 September 1841"
- `/ledger/15` https://en.wikipedia.org/wiki/Raj_of_Sarawak: confirmed: "In 1861, he acquired the Rajang River basin"
- `/ledger/20` https://en.wikipedia.org/wiki/North_Borneo: confirmed: Putatan River May 1884, Padas district November 1884
- `/ledger/24` https://en.wikipedia.org/wiki/Limbang: confirmed: "On 17 March 1890, Rajah Charles Brooke annexed Limbang"
- `/ledger/5` https://en.wikipedia.org/wiki/History_of_Brunei: confirmed: April 1578, Spanish back in Manila 26 June 1578
- `/ledger/14` https://en.wikipedia.org/wiki/Raj_of_Sarawak: confirmed 1852 Saribas and Skrang

## tondo: pass

Area: infobox has no area; author cuts to a 40 km circle round Manila (page: north of the Pasig; Bulacan influence "not territorial control"); Cliopatria max 4,953 km2.

Gaps for a gap-filler:

- `/ledger/1`: Confidence 1: the Pasig-mouth cell to Maynila c. 1497 is Cliopatria's year (Maynila page: founded "about 1500"). Try https://en.wikipedia.org/wiki/Rajah_Sulayman
- `/ledger/3`: Confidence 1 end of the Tondo-Maynila conflict. Try https://en.wikipedia.org/wiki/Lakandula
- `/identity/rulers`: No ruler strip (Lakandula, Gat Lontok). Try https://en.wikipedia.org/wiki/Lakandula

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Tondo_(historical_polity): confirmed: infobox "First historical mention, in the Laguna Copperplate Inscription ...: before 900"
- `/ledger/2` https://en.wikipedia.org/wiki/Tondo_(historical_polity): confirmed: "Territorial conflict with Maynila ...: c. 1520"
- `/ledger/5` https://en.wikipedia.org/wiki/Tondo_(historical_polity): confirmed: "June 3, 1571, marked the last resistance"
- `/ledger/6` https://en.wikipedia.org/wiki/Tondo_(historical_polity): confirmed: "only started to capitulate to Spanish rule in 1571" (infobox end 1589, author flagged)

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| samudera-pasai-sultanate 1292 gain / peureulak-sultanate |  | exception | no dossier; listed by the author under counterparts_needing_dossiers (se-02) |
| samudera-pasai-sultanate 1521 occupation_start / portuguese-empire | portuguese-empire 1521 gain | mismatch | portuguese-empire has a 1521 gain (confidence 1) from sultanate-of-aceh of the north-Sumatran coast and no 1524 loss; the Pasai page says the Portuguese occupied Pasai 1521 and evacuated 1524. Route to the portuguese-empire author: counterpart samudera-pasai-sultanate, occupation 1521-1524. |
| samudera-pasai-sultanate 1524 occupation_end / portuguese-empire | portuguese-empire 1521 gain | mismatch | portuguese-empire has a 1521 gain (confidence 1) from sultanate-of-aceh of the north-Sumatran coast and no 1524 loss; the Pasai page says the Portuguese occupied Pasai 1521 and evacuated 1524. Route to the portuguese-empire author: counterpart samudera-pasai-sultanate, occupation 1521-1524. |
| samudera-pasai-sultanate 1524 loss / sultanate-of-aceh |  | exception | owned by se-02 (another part), not written yet |
| majapahit 1294 gain / kediri-kingdom | kediri-kingdom 1293 dissolve | matched | kediri-kingdom dissolves 1293 to majapahit; majapahit gain 1294 (confidence 1) is within a year and agrees with keyframe majapahit_1293 (stronghold only) |
| majapahit 1343 gain / early-balinese-kingdoms | early-balinese-kingdoms 1343 loss | matched | early-balinese-kingdoms loss + dissolve 1343 to majapahit; Lombok part has no counterpart (none named on the page) |
| majapahit 1350 vassal_start / samudera-pasai-sultanate |  | mismatch | within this batch: samudera-pasai-sultanate has only a 1350 contest_start/contest_end with majapahit, no vassal_start/vassal_end. Fix on the Pasai side (see its findings). |
| majapahit 1352 vassal_start / Malay Peninsula principalities (Pahang, Kelantan, Terengganu, Johor) |  | exception | descriptive counterpart (no slug): the principalities named are tinted, not drawn as states; Kalimantan ones listed as needing dossiers (negara-dipa, nan-sarunai) |
| majapahit 1352 vassal_start / Sumatran principalities (Jambi-Melayu, Palembang, Minangkabau) |  | exception | descriptive counterpart (no slug): the principalities named are tinted, not drawn as states; Kalimantan ones listed as needing dossiers (negara-dipa, nan-sarunai) |
| majapahit 1362 vassal_start / Kalimantan principalities (Negara Dipa, Tanjungpura, Kutai) |  | exception | descriptive counterpart (no slug): the principalities named are tinted, not drawn as states; Kalimantan ones listed as needing dossiers (negara-dipa, nan-sarunai) |
| majapahit 1365 vassal_start / sultanate-of-brunei |  | mismatch | within this batch: sultanate-of-brunei has no vassal event with majapahit. Fix on the Brunei side (see its findings). |
| majapahit 1365 vassal_start / Eastern tributaries (Nusa Tenggara, Maluku) |  | exception | descriptive counterpart (no slug): the principalities named are tinted, not drawn as states; Kalimantan ones listed as needing dossiers (negara-dipa, nan-sarunai) |
| majapahit 1406 gain / blambangan-kingdom |  | exception | owned by se-02 (another part), not written yet; the 1295/1376-1406 Eastern court is listed by the author as needing a dossier |
| majapahit 1406 vassal_end / samudera-pasai-sultanate |  | mismatch | within this batch: samudera-pasai-sultanate has only a 1350 contest_start/contest_end with majapahit, no vassal_start/vassal_end. Fix on the Pasai side (see its findings). |
| majapahit 1406 vassal_end / Malay Peninsula principalities (Pahang, Kelantan, Terengganu, Johor) |  | exception | descriptive counterpart (no slug): the principalities named are tinted, not drawn as states; Kalimantan ones listed as needing dossiers (negara-dipa, nan-sarunai) |
| majapahit 1406 vassal_end / Sumatran principalities (Jambi-Melayu, Palembang, Minangkabau) |  | exception | descriptive counterpart (no slug): the principalities named are tinted, not drawn as states; Kalimantan ones listed as needing dossiers (negara-dipa, nan-sarunai) |
| majapahit 1406 vassal_end / Kalimantan principalities (Negara Dipa, Tanjungpura, Kutai) |  | exception | descriptive counterpart (no slug): the principalities named are tinted, not drawn as states; Kalimantan ones listed as needing dossiers (negara-dipa, nan-sarunai) |
| majapahit 1406 vassal_end / sultanate-of-brunei |  | mismatch | within this batch: sultanate-of-brunei has no vassal event with majapahit. Fix on the Brunei side (see its findings). |
| majapahit 1406 vassal_end / Eastern tributaries (Nusa Tenggara, Maluku) |  | exception | descriptive counterpart (no slug): the principalities named are tinted, not drawn as states; Kalimantan ones listed as needing dossiers (negara-dipa, nan-sarunai) |
| majapahit 1475 vassal_start / demak-sultanate |  | exception | owned by se-02 (another part), not written yet |
| majapahit 1478 vassal_end / demak-sultanate |  | exception | owned by se-02 (another part), not written yet |
| malaya 1299 loss / kingdom-of-singapura | kingdom-of-singapura 1299 found | matched | matched after the reviewer set kingdom-of-singapura /ledger/0 counterpart from melayu-kingdom to malaya |
| kingdom-of-singapura 1398 loss / nobody |  | exception | counterpart nobody |
| sultanate-of-brunei 1492 gain / nobody |  | exception | counterpart nobody |
| sultanate-of-brunei 1502 gain / nobody |  | exception | counterpart nobody |
| sultanate-of-brunei 1507 vassal_start / sultanate-of-sulu |  | exception | owned by se-02 (another part), not written yet |
| sultanate-of-brunei 1578 vassal_end / sultanate-of-sulu |  | exception | owned by se-02 (another part), not written yet |
| sultanate-of-brunei 1578 occupation_start / spanish-empire |  | missing | spanish-empire ledger has no event naming sultanate-of-brunei (no 1578 occupation of Brunei Town, no Palawan gains 1629/1842). Route to am-06. |
| sultanate-of-brunei 1578 occupation_end / spanish-empire |  | missing | spanish-empire ledger has no event naming sultanate-of-brunei (no 1578 occupation of Brunei Town, no Palawan gains 1629/1842). Route to am-06. |
| sultanate-of-brunei 1619 loss / sultanate-of-sambas |  | exception | owned by se-02 (another part), not written yet |
| sultanate-of-brunei 1629 loss / spanish-empire |  | missing | spanish-empire ledger has no event naming sultanate-of-brunei (no 1578 occupation of Brunei Town, no Palawan gains 1629/1842). Route to am-06. |
| sultanate-of-brunei 1673 loss / sultanate-of-sulu |  | exception | owned by se-02 (another part), not written yet |
| sultanate-of-brunei 1841 loss / kingdom-of-sarawak |  | exception | owned by se-03, not run yet |
| sultanate-of-brunei 1842 loss / spanish-empire |  | missing | spanish-empire ledger has no event naming sultanate-of-brunei (no 1578 occupation of Brunei Town, no Palawan gains 1629/1842). Route to am-06. |
| sultanate-of-brunei 1846 loss / british-colonial-empire |  | exception | owned by eu-11, not run yet (the 1877-1884 Sabah events are really the North Borneo company: british-north-borneo, listed as needing a dossier, se-03) |
| sultanate-of-brunei 1852 loss / kingdom-of-sarawak |  | exception | owned by se-03, not run yet |
| sultanate-of-brunei 1861 loss / kingdom-of-sarawak |  | exception | owned by se-03, not run yet |
| sultanate-of-brunei 1868 loss / kingdom-of-sarawak |  | exception | owned by se-03, not run yet |
| sultanate-of-brunei 1870 loss / kingdom-of-sarawak |  | exception | owned by se-03, not run yet |
| sultanate-of-brunei 1877 occupation_start / british-colonial-empire |  | exception | owned by eu-11, not run yet (the 1877-1884 Sabah events are really the North Borneo company: british-north-borneo, listed as needing a dossier, se-03) |
| sultanate-of-brunei 1884 loss / british-colonial-empire |  | exception | owned by eu-11, not run yet (the 1877-1884 Sabah events are really the North Borneo company: british-north-borneo, listed as needing a dossier, se-03) |
| sultanate-of-brunei 1884 loss / british-colonial-empire |  | exception | owned by eu-11, not run yet (the 1877-1884 Sabah events are really the North Borneo company: british-north-borneo, listed as needing a dossier, se-03) |
| sultanate-of-brunei 1884 occupation_end / british-colonial-empire |  | exception | owned by eu-11, not run yet (the 1877-1884 Sabah events are really the North Borneo company: british-north-borneo, listed as needing a dossier, se-03) |
| sultanate-of-brunei 1885 loss / kingdom-of-sarawak |  | exception | owned by se-03, not run yet |
| sultanate-of-brunei 1890 loss / kingdom-of-sarawak |  | exception | owned by se-03, not run yet |
| sultanate-of-brunei 1941 occupation_start / empire-of-japan | empire-of-japan 1942 occupation_start | mismatch | empire-of-japan occupies {Malaysia, Singapore} from 1942-02 with counterpart british-colonial-empire; Brunei (country) is not in its region and Borneo was taken from December 1941. Route to the empire-of-japan author. |
| sultanate-of-brunei 1945 occupation_end / empire-of-japan | empire-of-japan 1942 occupation_start | mismatch | empire-of-japan occupies {Malaysia, Singapore} from 1942-02 with counterpart british-colonial-empire; Brunei (country) is not in its region and Borneo was taken from December 1941. Route to the empire-of-japan author. |
| tondo 1497 loss / maynila |  | exception | owned by se-02 (another part), not written yet |
| srivijaya 1293 dissolve / majapahit | majapahit 1294 keyframe | mismatch | srivijaya names majapahit successor of its Sumatran land (1293); majapahit_1294 is cut to Java (page: direct rule did not extend beyond east Java and Bali) and gains no Sumatra, so Sumatra 1294-1351 is nobody. Route to the srivijaya author (se-02): successor for Sumatra should be melayu-kingdom (Dharmasraya), listed as needing a dossier. |
| tondo 1571 dissolve / spanish-empire | spanish-empire 1571 gain | mismatch | spanish-empire 1571 gain names namayan only (Manila 120 km, which covers Tondo); it should name tondo (and maynila) too, or carry one gain per polity. Route to am-06. |
| malaya 1351 dissolve / majapahit | majapahit 1352 vassal_start | exception | majapahit takes no land from malaya; it tints the peninsula as a tributary 1352-1406 (counterpart renamed by the reviewer from the dead slug malaya to the principalities). The peninsula is nobody from 1352 until the Malacca and Kedah rows. |

## Other

- Reviewer edits applied and re-validated (0 errors): majapahit /ledger/6 and /ledger/21 counterpart; kingdom-of-singapura /ledger/0 counterpart; sultanate-of-brunei /ledger/22 and /ledger/24 regions and /wars/3 zone.
- Verdict fix here means: reviewer-applied fixes plus non-blocking items the author should still do (applied false); fail means at least one unapplied blocking finding (samudera-pasai-sultanate keyframe 1272 vs the 1292 Peureulak gain; majapahit missing eastern-court loss before the 1406 gain).
- No infobox in the batch gives an area, so no area ratio could be computed.
- WebFetch returns a model summary of each page; History_of_Brunei summary says the 1962 revolt is not in the body text.
- Cross-group mismatches to route: portuguese-empire (1521 Pasai), empire-of-japan (Brunei 1941-1945), spanish-empire am-06 (Brunei 1578, Palawan 1629/1842, Tondo 1571), srivijaya (Sumatra successor 1293).

Gazetteer names needed: Lombok, Blambangan, Lumajang, Daha, Pamotan, Peureulak (Perlak), Pasai, Limbang, Lawas / Trusan, Kota Batu, Lusong (Lusung).

Counterparts needing dossiers: Eastern court of Majapahit (Kedhaton Wetan, Bhre Wirabhumi) (kedhaton-wetan, 1376-1406); Melayu Kingdom (Dharmasraya) (melayu-kingdom, 1293-1347); Peureulak Sultanate (peureulak-sultanate, 840-1292); British North Borneo (Chartered Company) (british-north-borneo, 1877-1946).
