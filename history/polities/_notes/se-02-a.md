# se-02-a notes (Maritime: Tarumanagara, Galuh, Srivijaya, Sunda, Mataram, Early Balinese)

Written 2026-10-19. Six dossiers, all validate (python3 -I history/tools/validate_dossier.py, with --resolve: no unresolved region names). 20 distinct Wikipedia pages opened; page budgets respected per state (Srivijaya 5 of 5, Sunda 9 of 9, Galuh 5 of 5, Tarumanagara 5 of 5, Early Balinese 5 of 5, Mataram 5 cited against a budget of 1-2 because three of them were opened for the neighbours' dossiers). The pages were read through WebFetch's summariser, so quotes are the summariser's rendering of the page, not a byte copy.

## Cliopatria rows split or merged

- Sunda Kingdom (674-1578, 13 shapes): NOT split. The 26,774 km2 / 62,041 km2 alternation is Sunda alone versus Sunda plus Galuh (26,774 + 35,841 = 62,615); the Galuh Kingdom has its own row. Rows 724-731 (62,498) and 732-740 (121,225) put Galuh and Sanjaya's Mataram (59,610) inside Sunda: corrected to Sunda alone, with Galuh and Mataram carrying those years in their dossiers. 825-895, 896-1027 and 1028-1293 rest on no dated page ('unverified: page budget').
- Galuh Kingdom (674-1481): one state; Cliopatria's gaps (724-740, 825-895, 1028-1474) are the Sunda row absorbing it. The Galuh page puts the absorption in the 10th century and ends its king list at 799: either the union is much earlier than 1028 or the separate Galuh of 896-1027 is spurious.
- Srivijaya (674-1293): NOT split. Read as one Palembang-based state; its end is open (see below).
- Early Balinese Kingdoms: the only Cliopatria row of the pre-Majapahit Bali; shares Wikipedia 'Bali Kingdom' and Q12491027 with 'Balinese Kingdom' (1519-1686, se-02-e) and 'Bali' (1687-1907). I did NOT merge them: Bali sits under Majapahit 1343-1478 (infobox) and Cliopatria has no shape for it. If the colour agent wants one Bali colour, give the three the same family/hue; Majapahit's dossier should carry Bali as vassal or province 1343-1478 (I record the loss at 1343 with counterpart majapahit).

## Dates that differ from Cliopatria (all in the dossiers)

- Tarumanagara: 358 (infobox) to 669 (infobox 'Invasion by Sriwijaya: 669'); Cliopatria 367-673. The page's text also dates the attack c. 686 (Kota Kapur), which contradicts 669.
- Galuh: 612 (Tarumanagara page; Galuh table) with sovereignty from 669/670; to 1482 (infobox 'Unification of Sunda and Galuh: 1482').
- Sunda: 670 (Galuh page: 'In 670, Tarumanagara was divided into the Sunda Kingdom (west) and the Galuh Kingdom (east)') to 1579 (Pakuan razed); the Sunda page's own infobox says 'established 932' (earliest inscription naming the kingdom).
- Mataram: 717 (Sanjaya c. 717) to 1016 (infobox); Airlangga page gives 1006 for the destruction of Dharmawangsa's capital, the Mataram page 1016-1017 (Pucangan). Cliopatria 741-1009.
- Srivijaya: 671 (infobox c. 671) to 1293 (Cliopatria's year, kept).
- Early Balinese: 914 (Belanjong pillar) to 1343; Cliopatria 922-1343.

## Open questions for the reviewer

1. Srivijaya's end. The Srivijaya page: 'The kingdom may have disintegrated after 1025'; last epigraphic use of the name a Chola inscription of 1030-1031; Jambi leads the Sanfoqi missions from the 11th century and goes independent in the early 13th; the Melayu page has Mahesa Anabrang taking Palembang and Jambi in 1288 and Majapahit crushing a Palembang revival in 1377. 1293 is Cliopatria's year and has no page behind it (event at confidence 1). Cliopatria's 456,772 km2 shape for 1202 is 0.38 of the infobox's 1,200,000 km2 for 1200 (the infobox follows the maximum maritime extent).
2. Srivijaya and the Isthmus of Kra. The sibling dossier tambralinga.json (se-01-x, from the Tambralinga page, which I did not open) has Srivijaya occupying Tambralinga 775-969 and Tambralinga independent 970-1277. Cliopatria's Srivijaya shape holds 9.9N until 1138, and my srivijaya events 'loss, 1139' (one for Kedah, counterpart sultanate-of-kedah, one for the strip north of it, counterpart tambralinga) are at confidence 1; on the grid the 1138 shape holds 38 cells of Cliopatria's 1139 Sultanate of Kedah and 43 of Surat Thani, and the 1139 shape holds neither. The two dossiers disagree by about 170 years; the Tambralinga page is the better evidence for the date, and a reviewer may move the Srivijaya loss to c. 969-970 and the gain to c. 775 (718 is Cliopatria's).
3. Coastal Banten and Jakarta. The Tarumanagara page says they 'came under Srivijayan control after the invasion'; Cliopatria keeps them in Sunda's shape (674-723, and in later shapes), and its Srivijaya shape holds no Banten, Jakarta or West Java cell. Unresolved; no dated page.
4. Bali before 1343 and under the Javan kingdoms: Bali 'probably' a Mataram (c. 990-1016) and Kahuripan vassal (Airlangga page; unresolved on the Bali page); a Kediri colony c. 1225 (Chu-fan-chi, Kediri page); integrated into Singhasari 1284 (Singhasari and Bali pages), sovereign again by 1342 (Majapahit page). The Mataram dossier carries Bali as vassal 990-1016 at confidence 1; Kahuripan, Kediri and Singhasari dossiers (other groups) should carry the rest.
5. The Sunda/Banten sequence: Banten page (Hasanuddin's Banten 'comprised all of Sunda' at his death in 1570) against the Sunda page (Pakuan razed 1579); I kept Pakuan inside Sunda to 1578 and put the loss of the west at 1572 (Cliopatria's year, 'the Banten conquest began in the 1570s'). Cliopatria also keeps Jakarta (Sunda Kalapa, taken by Demak in 1527) in Sunda's shape to 1571; corrected.
6. Cirebon's independence: 1482 (body, chronogram 2 April 1482; Banten page) against 1479 (infobox).

## Pages that would not load

- https://en.wikipedia.org/wiki/Singhasari_Empire (URL_NOT_FOUND) -> recovered at https://en.wikipedia.org/wiki/Singhasari.
- https://en.wikipedia.org/wiki/Sumedang_Larang (URL_NOT_FOUND) -> recovered at https://en.wikipedia.org/wiki/Sumedang_Larang_Kingdom.
- Nothing was filled from memory. Where a page was silent the event is at confidence 1 and says 'page silent' (Srivijaya 718, 1139; Sunda 825, 896, 1028; Galuh 825, 896, 1028, 1200; Tarumanagara 534; Mataram 898, 990 and 1016 Bali; Early Balinese 1293).

## Counterparts that need a dossier (not written; other groups)

- melayu-kingdom (Jambi / Dharmasraya, c. 671-1347; Melayu Kingdom page), named in the Srivijaya ledger (686 gain, 692 merge, 1202 loss) and the Mataram wars. Cliopatria's 'Malaya' (1294-1351) is the Malay Peninsula, not Dharmasraya.
- Kedah (Kadaram) before 1139 (Srivijaya ledger 685 gain); Langkasuka (718 gain); kantoli (infobox predecessor of Srivijaya); sumedang-larang (Sunda's successor, 1578/1585-1620); the Sailendra dynasty of Central Java (c. 775-852; Borobudur 825, Balaputra defeated 852), which is not a Cliopatria row and was not opened.
- Majapahit, Kahuripan, Kediri, Singhasari, Banten, Cirebon, Demak, Chola Empire and Tambralinga already have rows or dossiers; Majapahit should carry Bali (1343), Sunda (vassal? Bubat 1357 only 'possibly') and the Palembang revival (1377).

## Gazetteer names wanted (all real; none is used in a region, only in text and capitals)

Rivers Citarum, Cimanuk, Pemali (Brebes), Cipamali, Cisarayu (Serayu); places Kawali, Karangkamulyan, Pakuan (Bogor), Sundapura, Bedulu, Tamwlang/Watugaluh, Wwatan, Kedukan Bukit, Sunda Kalapa (alias of Jakarta); region Priangan/Parahyangan (West Java highlands; Sumedang country).

## Per-state remarks

- tarumanagara: no ruler strip (the reign lists come from the Wangsakerta manuscripts, which the page calls likely fraudulent). Galuh is read as Tarumanagara's dependency 612-669 (a vassal pair in the ledger), because Cliopatria adds the Galuh country to the Tarumanagara shape in 612, the year the page has Galuh founded.
- galuh-kingdom: the later Galuh at Panaekan (16th century, conquered by Mataram 1595) is not this state and has no dossier.
- srivijaya: capital kept at Palembang throughout (the move to Jambi has no year on the page); no ruler strip.
- sunda-kingdom: ruler table taken from the Sunda page (partial before 1340; Dharmasiksa 1175-1297 is a 122-year entry that probably merges reigns).
- mataram-kingdom: 741 shape (Central and East Java, 59,610 km2) cut to Central Java until Balitung's accession in 898 on the page's description; capitals' coordinates approximate.
- early-balinese-kingdoms: Cliopatria gaps 1010-1045 and 1236-1284 bridged with new keyframes; the 1285 shape is cut to 1293-1332.

## Checks run on Cliopatria's grid (tools/gazetteer.py, H3 res-5 cells)

- Tarumanagara 612-673 (136 + 89 cells) is exactly Cliopatria's Galuh 674 shape plus its Sunda 674 shape; Sunda 732-740 contains the whole Mataram 741 shape (233 cells) and Sunda 724 is Sunda plus Galuh.
- Srivijaya 1293 (1,500 cells) passes to Cliopatria's Majapahit 1294 (1,094 cells) and Malaya 1294 (403): the successors in the dossier.
- Kahuripan 1028-1045 and Majapahit from 1344 hold the whole of Bali (22 cells); Kediri 1046 and Singhasari 1227/1285 hold none, so 1236-1284 has no owner in Cliopatria.
- Every region in the six dossiers resolves to a non-empty cell set.
