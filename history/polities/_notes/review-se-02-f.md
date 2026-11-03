# Review se-02-f (2026-10-19)

Adversarial review of the six se-02-f dossiers. Validator: all pass, one warning (banjar: negara-daha has no dossier, listed). Machine copy: history/notes/phase-b/reviews/se-02-f.json.

Reviewer edits applied on the mount (validated, read back): johor /ledger/22 confidence 3->2; banten /ledger/13 confidence 3->2; perak /identity/rulers from the Sultan of Perak table.

## sultanate-of-johor: thin

Area: infobox 220000 (None), Cliopatria 208008, ratio 0.95.

Fixes:
- `/ledger/22` (applied by reviewer): 1824 loss to riau-lingga-sultanate at confidence 3 with a region (Riau admin1 = the Sumatran shore) the pages do not name for 1824. Evidence: Johor_Sultanate: 'the mainland part was administered by the British, and the insular part by the Dutch'; the infobox lists the Siak Sultanate among the successors. Rule 7 of the reviewer brief. Fix: Confidence lowered to 2 with a reviewer note (done). Author: narrow the 1824 region to Kepulauan Riau (c3) and date the Sumatran shore's separation separately (see thin).
- `/ledger (missing, 1613 and 1623)` (author): No mirror of the Aceh dossier's occupation of Johor in 1613 and its 1623 sack. Evidence: sultanate-of-aceh /ledger/12-13: 1613 occupation_start/occupation_end counterpart sultanate-of-johor ('taken in 1613 and later that year expelled the Acehnese garrison'); /ledger/19-20: 1623 contest_start/contest_end sultanate-of-johor. The Johor infobox has 'Conflicts with Aceh 1528-1629'. Fix: Add occupation_start/occupation_end 1613 (counterpart sultanate-of-aceh, region the Johor River around Batu Sawar) and contest_start/contest_end 1623, or say in notes why not; give the war 'Acehnese and Portuguese attacks on Johor' its zone.
- `/ledger/5, /ledger/6, /ledger/8, /identity/predecessors/1` (author): The 1470-1623 Pahang Sultanate is written as counterpart 'pahang-sultanate', the slug of Cliopatria's 1853-1889 row, while the report asks for a new dossier 'sultanate-of-pahang' for it. Evidence: Author's notes: 'pahang-sultanate (1853-1889) is a different era'; counterparts_needing_dossiers suggests sultanate-of-pahang [1470,1623]. The Aceh dossier writes 'Pahang Sultanate' for the same state. Fix: Orchestrator to decide one slug for the 1470-1623 state; then use it in these three events and the predecessor (keep pahang-sultanate for 1861).
- `/keyframe_review/1` (author): No event for the Malacca-hinterland cells that the Portuguese dossier gives to Johor in 1529. Evidence: portuguese-empire /ledger/15: 1529 loss counterpart sultanate-of-johor ('the Malacca patch shrinks from 82 to 21 cells', confidence 1, read off the shapes). Fix: Either add a 1529 gain from portuguese-empire (confidence 1, the cells around Melaka in Cliopatria's 1529 shape) or remove those cells from the 1528/1529 corrections and tell am-06.

Thin (for a gap-filler):
- `/keyframe_review/7, /keyframe_review/8`: The Sumatran shore (Riau admin1, Siak, Kampar, Bengkalis, Indragiri; about 87,000 km2) is drawn as Johor 1722-1823 with no page; Raja Kecil founded Siak after 1722 and the Johor infobox lists the Siak Sultanate as a successor. Date the loss and narrow KF 1727/1820b. Try: https://en.wikipedia.org/wiki/Siak_Sultanate
- `/ledger/25`: 1884 dissolve at confidence 1 (no page event; Johor continued under Abu Bakar and the 1885 treaty). Try: https://en.wikipedia.org/wiki/Abu_Bakar_of_Johor
- `/ledger/1`: 1528 gain of the Sumatran shore and Terengganu at confidence 1 (page gives them only 'at its height'). Try: https://en.wikipedia.org/wiki/Kampar_Kingdom
- `/keyframe_review/9`: 13 Kelantan cells kept in Johor 1824-1860 without a page. Try: https://en.wikipedia.org/wiki/Kelantan_Sultanate
- `/identity/rulers`: Rulers stop at 1830 (life to 1884) and only the first cites a page. Try: https://en.wikipedia.org/wiki/Sultan_of_Johor

Spot checks:
- `/ledger/8` https://en.wikipedia.org/wiki/Pahang_Sultanate: confirmed ('Pahang entered a nominal dynastic union with Johor in 1623')
- `/ledger/22` https://en.wikipedia.org/wiki/Johor_Sultanate: confirmed year; region over-reaches (insular part only), confidence lowered
- `/ledger/24` https://en.wikipedia.org/wiki/Johor_Sultanate: confirmed (1861 treaty, 'two independent states, Johor and Pahang')
- `/ledger/15` https://en.wikipedia.org/wiki/Johor_Sultanate: confirmed (assassinated in 1699 by Megat Sri Rama)
- `/ledger/13` https://en.wikipedia.org/wiki/Jambi_Sultanate: confirmed (May 1679 attack with 300 ships; Daeng Mangika fled 17 October 1679)
- `/ledger/10` https://en.wikipedia.org/wiki/Jambi_Sultanate: confirmed quote (1655 pro-Johorese rebellion); annexation by Johor is the author's reading, as the note says

## sultanate-of-banten: fix

Area: infobox None (None), Cliopatria 84855, ratio None.

Fixes:
- `/ledger/13` (applied by reviewer): 1752 loss at confidence 3 with Bengkulu and the whole Sumatera Selatan admin1 in the region; the pages name only Lampung and 'southern Sumatra'. Evidence: Banten_Sultanate: 'In 1752, the Dutch annexed territories on western Borneo and southern Sumatra formerly held by Banten.' Lampung page: Lampung annexed 1752. Neither names Bengkulu or Sumatera Selatan. Fix: Confidence lowered to 2 with a reviewer note (done).
- `/ledger/2/region, /ledger/13/region` (author): Regions are whole admin1s (Lampung + Sumatera Selatan + Bengkulu); Sumatera Selatan includes Palembang, the Palembang Sultanate's core, and Cliopatria's Banten shape only reaches about 3.6 S. Evidence: shapes.csv: sultanate-of-banten_1556 bbox north edge -3.6359; Palembang city is at about 3.0 S. Fix: Write the land as {intersect: [{cliopatria: 'Sultanate of Banten', year: 1556}, {union: [Lampung, Sumatera Selatan, Bengkulu]}]} (and the 1677 shape for 1752); then Lampung alone can go back to confidence 3. Find out who took Bengkulu (the English post at Bencoolen) before giving it to the Dutch in 1752.
- `/ledger/1` (author): 1552 'gain' from sultanate-of-cirebon of the Banten province that the 1526 found event already gives Banten; double-counted land, and it does not mirror Cirebon's ledger. Evidence: sultanate-of-cirebon /ledger/1-2 model 1526-1552 as vassal_start/vassal_end of sultanate-of-banten (confidence 3); Banten /ledger/0 already has the Banten admin1 from 1526. Fix: Drop the 1552 gain (or turn it into a note on the found event): Cirebon's vassal pair carries 1526-1552 in the lighter tint.
- `/ledger/3` (author): 1572 gain at confidence 1 'page gives no 1572', but the Banten page dates and bounds it. Evidence: Banten_Sultanate: 'When Hasanuddin died in 1570, the royal kingdom of Banten comprised all of Sunda, except for Cirebon and Sumedang Larang' and 'Banten ruled over the territory of the former Kingdom of Sunda west of the Citarum River.' Fix: Cite these sentences, raise to confidence 2 (by 1570), use the Citarum as the eastern limit in the region text.
- `/ledger/5` (author): No 1579 gain mirrors the Sunda dossier's 1579 loss to Banten. Evidence: sunda-kingdom /ledger/12-13: 1579 loss and dissolve, counterpart sultanate-of-banten. Sunda page: Banten 'took over most of the former Sunda Kingdom's territory'. The Banten dossier leaves Cliopatria's hand-over to Cirebon as drawn. Fix: Add a 1579 gain from sunda-kingdom (the Pakuan remnant west of the Citarum, confidence 2) with a keyframe adjust, or tell the Sunda author (se-02) why Cirebon should be the counterpart.
- `/ledger/8, /ledger/11` (author): vassal_start 1677 / vassal_end 1683 name sultanate-of-cirebon, which dissolves in 1677 into Kasepuhan, Kanoman and Keprabonan. Evidence: sultanate-of-cirebon /ledger/3-6: 1677 split into kasepuhan-sultanate, kanoman-sultanate, keprabonan-sultanate and dissolve. Fix: Name the successor sultanates (one pair each, or one pair with the region of all three) or say in the note that the counterpart is the partitioned Cirebon.
- `/ledger (missing)` (author): Bangka: the Palembang dossier takes Bangka from Banten (late 17th century) and Banten has no event for it. Evidence: sultanate-of-palembang /ledger/2: 1670 gain counterpart sultanate-of-banten; Bangka Island page (quoted by reviewer se-02-d): Bangka 'continued to pass to the Banten Sultanate' before Palembang inherited it. Fix: Add a gain and a loss of Bangka (confidence 1) or agree with se-02 that the counterpart is nobody.

Thin (for a gap-filler):
- `/ledger/2`: Year of the south Sumatra conquest inside 1550-1570 (confidence 1). Try: https://en.wikipedia.org/wiki/Lampung
- `/ledger/11, /ledger/14`: End of the Cirebon predominance and of Landak's dependency are bridged (confidence 1). Try: https://en.wikipedia.org/wiki/Landak_Kingdom
- `/identity/rulers`: Only the first ruler cites a page. Try: https://en.wikipedia.org/wiki/Banten_Sultanate

Spot checks:
- `/ledger/13` https://en.wikipedia.org/wiki/Banten_Sultanate: confirmed year (1752); region over-reaches, confidence lowered
- `/ledger/15` https://en.wikipedia.org/wiki/Banten_Sultanate: confirmed (22 November 1808, Daendels at Serang)
- `/ledger/12` https://en.wikipedia.org/wiki/Ageng_Tirtayasa: confirmed ('Ageng surrendered in March 1683')
- `/ledger/9` https://en.wikipedia.org/wiki/Ageng_Tirtayasa: confirmed ('Open war with the VOC began in 1680')
- `/ledger/7` https://en.wikipedia.org/wiki/Ageng_Tirtayasa: confirmed ('In 1661, Banten extended authority to Landak')
- `/ledger/10` https://en.wikipedia.org/wiki/Banten_Sultanate: confirmed land (Bogor, Priangan); year only via infobox 'Client state of VOC: 1683', confidence 2 is right

## sultanate-of-perak: fix

Area: infobox None (None), Cliopatria 23820, ratio 0.88. no infobox area; the modern state's 20,976 km2 (History_of_Perak) against Cliopatria 23,820

Fixes:
- `/identity/rulers` (applied by reviewer): Ruler years differ from the page and 18 of 19 rulers cited no page; 1577-1636 and 1871-1874 were missing although the page lists them. Evidence: Sultan_of_Perak table: Ahmad Tajuddin 1577-1584 ... Salehuddin 1630-1636, Muzaffar II 1636-1653, Mahmud Iskandar 1653-1720, Muzaffar III 1728-1752 (Upper Perak), Muhammad 1744-1750 (Lower Perak), Iskandar Zulkarnain 1752-1765, Alauddin Mansur 1773-1786, Ahmaddin 1786-1806, Ismail 1871-1874. The dossier had 1742, 1754, 1792 and a 'second reign' 1750-1754 the page does not give. Fix: Rulers rewritten from the page table with source Perak_Sultanate (done; validates).
- `/ledger/5` (author): The 1874 'loss' takes the same 25 km Dindings circle that /ledger/3 already lost in 1826: double loss. Evidence: Pangkor_Treaty_of_1874 quotes 'the Treaty under which the Pulo Dinding and the islands of Pangkor were ceded to Great Britain' and 'the Boundaries of the said Territory so ceded shall be rectified': 1874 rectifies an earlier cession. Fix: Make 1826 the cession of Pangkor and Pulo Dinding (islands) and 1874 the rectified mainland strip (Lumut/Manjung coast) as a separate region, or keep one loss and put the other in a note.
- `/ledger/1, /ledger/4` (author): The 1818-1826 contest names Reman, but the page says Kedah attacked Perak for Siam. Evidence: Sultan_of_Perak: Abdu'l-Malik 'forced to surrender to a large army sent by the Sultan of Kedah, on behalf of the Siamese King'; 'Removed from exercising executive powers by the Sultan of Kedah, after 18 November 1818'. Fix: Counterpart sultanate-of-kedah for the 1818 contest pair (and tell se-02 the Kedah dossier lacks it); keep Reman for the 1819 loss.
- `/identity/capitals/0` (author): Kuala Kangsar is given as the capital for 1528-1876 from a sentence about today ('The royal capital remains Kuala Kangsar'). Evidence: History_of_Perak gives only the present seat; the dossier's own note says the earlier seats are undated. Fix: Keep Kuala Kangsar only with a note that it is a stand-in, or replace by the river seats a page dates; lower nothing else.
- `/wars/0` (author): The Aceh dossier has Perak as its vassal 1620-1629; this dossier's war and notes say 1612-c.1653. Evidence: sultanate-of-aceh /ledger/18 (1620 vassal_start sultanate-of-perak) and /ledger/22 (1629 vassal_end); History_of_Perak: 'In 1620, the Acehnese sultanate invaded Perak and captured its sultan.' Fix: Agree the years with the se-02 Aceh author; cite the 1620 sentence in the war.

Thin (for a gap-filler):
- `/ledger/2, /ledger/4`: Reman's gain of Hulu Perak and the end of the contest are undated (confidence 1); the page has Reman working the Klian Intan mines and the recovery under the 1909 treaty. Try: https://en.wikipedia.org/wiki/Hulu_Perak_District
- `/ledger/6`: Deposition date: the ruler page gives 30 March 1877 against the 1876 end. Try: https://en.wikipedia.org/wiki/Abdullah_Muhammad_Shah_II_of_Perak

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Sultan_of_Perak: confirmed (18 November 1818)
- `/ledger/3` https://en.wikipedia.org/wiki/History_of_Perak: confirmed (Ligor 1826; 'The Sultan of Perak then ceded to the British Dindings and Pangkor')
- `/ledger/5` https://en.wikipedia.org/wiki/Pangkor_Treaty_of_1874: confirmed date (20 January 1874); the cession clause refers to an earlier treaty (see fixes)
- `/ledger/0` https://en.wikipedia.org/wiki/History_of_Perak: confirmed ('By 1528, a Muslim sultanate began to emerge in Perak')

## sultanate-of-maguindanao: fix

Area: infobox None (None), Cliopatria 106474, ratio None. no infobox area; Cliopatria 1521 shape marked wrong (Brunei overlay) and replaced by the valley (about 14,000-19,000 km2); the Brunei dossier also removes these cells

Fixes:
- `/keyframe_review/4, /ledger (missing 1864-1887)` (author): The 1862-1899 shape keeps the whole Cotabato valley except a 15 km Polloc circle, but the page the author opened has Spanish forts on the Rio Grande from 1864, a Spanish garrison at Cotabato itself (the sultan's capital) by 1884, Tumbao occupied 1 January 1887 and ten garrisoned stations after 1887; the war lists these zones but no ledger event carries them. Evidence: Spanish-Moro_conflict: 'The fort at Pagalungan was captured' (1864); 1884 report 'The fort at Cotabato...', 'the smaller forts of Libungan, Tumbao, Taviran, and Tamontaca'; 'On January 1, 1887, Tumbao was occupied'; '1.100 men were retained to garrison the ten forts or stations of Cotabato, Polloc, Libungan, Tumbao'. Fix: Add occupation_start events (counterpart spanish-empire) for the lower Rio Grande posts (1864 Pagalungan; 1887 Cotabato-Tumbao) and either subtract them from the 1862 keyframe or say why a garrison chain is not held land.
- `/ledger/10` (author): The Spanish Empire dossier has no 1862 gain at Polloc and draws Cotabato as Spanish from 1609. Evidence: spanish-empire /keyframe_review (spanish-empire_1609): '+423 cells: Mindanao 322 (... Cotabato ...): undated ... unverified: page budget'. Fix: Orchestrator: route to am-06 so that spanish-empire drops the Cotabato valley before 1862 and records the 1862 Polloc gain; this dossier's 1862 event stands.
- `/keyframe_review/2/correction` (author): The 1612 keyframe (1612-1848) includes the Sarangani islands, gained only in 1625. Evidence: /ledger/4 dates the gain 1625; the note itself says 'Applies 1625-1861'. A correction describes the shape at the keyframe's first year (review af-01-a). Fix: Write the 1612 correction as the valley only, and let the 1625 gain add Sarangani.

Thin (for a gap-filler):
- `/ledger/3, /ledger/6`: Buayan vassal pair at confidence 1 (page: 'a de facto subject state under Sultan Kudarat', undated, no region). Try: https://en.wikipedia.org/wiki/Sultanate_of_Buayan
- `/notes`: 'the Davao country was ceded to the Spaniards by the Sultan of Mindanao' (Spanish-Moro page, 1844-1849): outside the drawn valley, but the cession belongs in notes and in the Spanish dossier. Try: https://en.wikipedia.org/wiki/Spanish%E2%80%93Moro_conflict

Spot checks:
- `/ledger/4` https://en.wikipedia.org/wiki/Sultanate_of_Maguindanao: confirmed ('Since its capture in 1625, the people of the Sarangani islands were subjugated')
- `/ledger/10` https://en.wikipedia.org/wiki/Spanish%E2%80%93Moro_conflict: confirmed ('a small fleet forced the Sultan of Mindanao to hoist a Spanish flag at Polloc', 1862)
- `/ledger/11` https://en.wikipedia.org/wiki/Sultanate_of_Maguindanao: confirmed (infobox 'American occupation of Cotabato: December 1899')
- `/ledger/8` https://en.wikipedia.org/wiki/Sultanate_of_Maguindanao: confirmed (infobox 'Tamontaka (1711-1861)')

## sultanate-of-banjar: thin

Area: infobox None (None), Cliopatria 39178, ratio None.

Thin (for a gap-filler):
- `/ledger (1787-1826)`: Dutch protectorate and cessions: page 'Amir was arrested and exiled to Sri Lanka in 1787, and Banjar became a Dutch protectorate'; infobox 'Protectorate of the Dutch East Indies (1826-1860)'; Tahmidullah II 'handed over many areas to the VOC' (undated). The vassal tint belongs to the Dutch dossiers, the ceded land needs dated loss events here. Try: https://en.wikipedia.org/wiki/Banjarmasin
- `/ledger (1526-1548)`: Infobox 'Payment of tribute to of Demak Sultanate (1526-1548)': the Demak dossier has no vassal pair for Banjar. Try: https://en.wikipedia.org/wiki/Demak_Sultanate
- `/identity/capitals, /identity/rulers`: No capital 1806-1856 (infobox silent); rulers have gaps 1570-1595, 1645-1660, 1708-1734 and only the first cites a page. Try: https://en.wikipedia.org/wiki/Sultanate_of_Banjar

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Sultanate_of_Banjar: confirmed ('Raden Samudra converted to Islam on 24 September 1526')
- `/ledger/9` https://en.wikipedia.org/wiki/Banjarmasin_War: confirmed (29 April and 1 May 1859)
- `/ledger/11` https://en.wikipedia.org/wiki/Sultanate_of_Banjar: confirmed ('abolition of the sultanate in 1860')
- `/ledger/6` https://en.wikipedia.org/wiki/Sultanate_of_Banjar: confirmed (infobox 'Kayu Tangi (1680-1771)')

## kingdom-of-pajana: fix

Area: infobox None (None), Cliopatria 45552, ratio None.

Fixes:
- `/ledger/1, /keyframe_review/0-3` (author): The 30 km Demak vassal circle lies inside the direct shape (Cliopatria's 1572 shape cut to Jawa Tengah + Yogyakarta, which is Demak's own 1551 polygon), so Demak is drawn both as Pajang land and as a vassal. Evidence: kingdom-of-pajana_1572 note: the shape 'is cell for cell its Demak Sultanate 1551 shape'; Demak town is in Jawa Tengah. Demak_Sultanate: 'Pajang became the suzerain kingdom, while Demak became its vassal.' Fix: Subtract the Demak circle from the four keyframe corrections and the found region (or drop the vassal pair).
- `/identity/wikidata` (author): Keeps Q1074947, which the author's own notes call a mismatch (Cliopatria's 'Lontara script'). Evidence: Author's notes; polities.csv row kingdom-of-pajana: wikipedia 'Lontara script', wikidata Q1074947. Fix: Orchestrator: blank or replace the id when Wikidata is reachable; flag for the colour/state-page agents.

Thin (for a gap-filler):
- `/ledger/2`: vassal_end 1586 at confidence 1; Ario Pangiri (adipati of Demak) held Pajang 1583-1586 per the infobox dates. Try: https://en.wikipedia.org/wiki/Pajang_Sultanate

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Demak_Sultanate: confirmed ('In 1568, after Penangsang was killed, Hadiwijaya assumed the role of sovereign')
- `/ledger/1` https://en.wikipedia.org/wiki/Demak_Sultanate: confirmed ('Pajang became the suzerain kingdom, while Demak became its vassal')
- `/ledger/3` https://en.wikipedia.org/wiki/Pajang_Sultanate: confirmed ('Prince Banawa then submitted his crown to Sutawijaya and thus ended the Kingdom of Pajang in 1586')

## Cross-dossier matrix

- sultanate-of-johor 1528 found sultanate-of-malacca -> sultanate-of-malacca 1528 split: matched (Malacca /ledger/26 split sultanate-of-johor)
- sultanate-of-johor 1528 gain sultanate-of-malacca -> sultanate-of-malacca 1528 dissolve: matched (Malacca partitions in 1528; land passes with the split)
- sultanate-of-johor 1623 gain pahang-sultanate -> none: exception (1470-1623 Pahang has no dossier (listed as sultanate-of-pahang); slug choice open)
- sultanate-of-johor 1655 gain sultanate-of-jambi -> none: exception (sultanate-of-jambi not written yet (se-02); Jambi before 1670 listed)
- sultanate-of-johor 1722 loss sultanate-of-terengganu -> none: exception (se-03 has not run)
- sultanate-of-johor 1819 loss british-colonial-empire -> none: exception (eu-11 has not run)
- sultanate-of-johor 1824 loss riau-lingga-sultanate -> none: exception (se-03 has not run)
- sultanate-of-johor 1861 loss pahang-sultanate -> none: exception (se-03 has not run)
- sultanate-of-aceh 1613 occupation_start sultanate-of-johor -> none: missing (Johor ledger has no 1613 occupation (and no 1623 contest) mirror)
- portuguese-empire 1529 loss sultanate-of-johor -> none: missing (Johor ledger has no 1529 gain from Portugal (Malacca hinterland cells))
- sultanate-of-banten 1526 found sunda-kingdom -> sunda-kingdom 1527 loss: matched (within one year)
- sultanate-of-banten 1552 gain sultanate-of-cirebon -> sultanate-of-cirebon 1552 vassal_end: mismatch (Cirebon models 1526-1552 as vassalage; Banten already holds the land from 1526)
- sultanate-of-banten 1572 gain sunda-kingdom -> sunda-kingdom 1572 loss: matched (both at confidence 1, Cliopatria's year)
- sunda-kingdom 1579 loss sultanate-of-banten -> none: mismatch (Banten records no 1579 gain (leaves Cliopatria's hand-over to Cirebon))
- sultanate-of-banten 1619 loss dutch-republic -> none: exception (eu-09 has not run)
- sultanate-of-banten 1661 vassal_start Landak (kingdom in western Borneo) -> none: exception (no dossier; listed)
- sultanate-of-banten 1677 vassal_start sultanate-of-cirebon -> sultanate-of-cirebon 1677 dissolve: mismatch (Cirebon splits into kasepuhan/kanoman/keprabonan in 1677)
- sultanate-of-banten 1683 loss dutch-republic -> none: exception (eu-09 has not run; Banten as VOC client 1683-1808 should be a dutch-republic vassal_start)
- sultanate-of-banten 1752 loss dutch-republic -> none: exception (eu-09 has not run; Bengkulu likely English, not Dutch)
- sultanate-of-palembang 1670 gain sultanate-of-banten -> none: missing (Banten has no Bangka events)
- sultanate-of-banten 1808 dissolve dutch-east-indies -> none: exception (se-03 has not run)
- sultanate-of-perak 1528 found sultanate-of-malacca -> sultanate-of-malacca 1528 split: matched (Malacca /ledger/27)
- sultanate-of-perak 1819 loss Reman (Siamese tributary kingdom) -> none: exception (no dossier; listed as reman-kingdom)
- sultanate-of-perak 1826 loss british-colonial-empire -> none: exception (eu-11 has not run)
- sultanate-of-perak 1874 loss british-colonial-empire -> none: exception (eu-11 has not run; duplicate of 1826 region)
- sultanate-of-aceh 1620 vassal_start sultanate-of-perak -> none: mismatch (Perak has no events; its war and notes say 1612-c.1653, Aceh says 1620-1629)
- sultanate-of-maguindanao 1619 vassal_start Buayan (rival sultanate) -> none: exception (no dossier; listed)
- sultanate-of-maguindanao 1862 loss spanish-empire -> none: mismatch (spanish-empire has no 1862 gain and holds Cotabato from 1609 (KF spanish-empire_1609))
- sultanate-of-maguindanao 1899 dissolve united-states-of-america -> united-states-of-america 1898 gain: mismatch (USA takes the Philippines from spanish-empire (Treaty of Paris); nothing from Maguindanao)
- sultanate-of-banjar 1526 found negara-daha -> none: exception (no dossier; listed)
- sultanate-of-banjar 1860 dissolve dutch-east-indies -> none: exception (se-03 has not run)
- kingdom-of-pajana 1568 found demak-sultanate -> demak-sultanate 1568 dissolve: matched (Demak /ledger/10 names Pajang in its note)
- kingdom-of-pajana 1568 vassal_start demak-sultanate -> demak-sultanate 1568 dissolve: exception (Demak dossier ends 1568; the vassal is its rump under Pangiri, drawn only in Pajang's tint)
- kingdom-of-pajana 1586 dissolve mataram-sultanate -> none: exception (mataram-sultanate not written yet (se-02))

## Problems

- Spanish-Moro_conflict page is over 100,000 characters; WebFetch read the first 100,000 (the last 941 unread).
- Reviewer applied 3 edits (orchestrator allowance): sultanate-of-johor /ledger/22 confidence 3->2; sultanate-of-banten /ledger/13 confidence 3->2; sultanate-of-perak /identity/rulers rewritten from the Sultan of Perak table. All three re-validated and read back.
- Verdict 'fix' here means: no blocking finding; applied:true items done by the reviewer, applied:false items are non-blocking author fixes.
- Rulers in johor, banten, maguindanao and banjar cite a page only on the first entry; Perak's uncited list was wrong in 7 places, so the others were probably filled from memory too (not checked).
