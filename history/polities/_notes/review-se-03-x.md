# Review of batch se-03-x (Colonial, additions)

Reviewer: Phase B adversarial reviewer, 2026-10-24. Inputs: the 24 dossiers of the batch, the author report history/notes/phase-b/reports/se-03-x.json and notes history/polities/_notes/se-03-x.md, the neighbour dossiers that exist in history/polities/ (ayutthaya-kingdom, bali, empire-of-japan, khmer-empire, kingdom-of-thailand, nguyen-dynasty, portuguese-empire, rattanakosin-kingdom, republic-of-china, spanish-empire, sultanate-of-aceh/banten/bima/bone/brunei and others; the Cliopatria rows british-colonial-empire, british-empire, british-raj, dutch-republic, batavian-republic, german-empire, estado-novo, portuguese-colonies belong to groups that have not run, which is the brief's exception) and every other dossier a ledger names as counterpart.

Method: validator with --resolve on all 24 (0 errors; warnings: malayan-union unresolved twice, Kengtung unknown place three times, four Banda disc regions with no grid cell; all flagged by the author). Each dossier read as one line per event; 4-6 events per dossier spot-checked with WebFetch (weighted to confidence 3 and the largest land moves), infobox areas compared with the keyframes resolved on the res-5 grid (cells x 252.9 km2), every territorial event matched against the counterpart's ledger. None of these states has Cliopatria shapes, so the page budget is the brief's 2-5 pages for a new state; thin is judged against it.

Verdicts: 11 pass, 7 fix (all fixes applied by the reviewer and re-validated), 6 thin, 0 fail. No spot-checked event was fabricated; two months were not on the page (dutch-malacca 1795, diponegoro-s-rebels 1827) and were removed.

## Per dossier

### spanish-east-indies: thin

- Area: infobox 345155 (1877); keyframe on the grid 167926 km2; ratio 2.06. shape alive in 1877 is spanish-east-indies_1872; acknowledgement added by the reviewer; the 1878 shape is about 268,000 km2 (ratio 1.29)
- Spot checks: /ledger/16 confirmed (Spanish%E2%80%93Moro_conflict); /ledger/10 confirmed (Spanish%E2%80%93Moro_conflict); /ledger/4 confirmed (Spanish_East_Indies); /ledger/17 confirmed (Spanish_East_Indies); /ledger/25 confirmed (Spanish%E2%80%93Moro_conflict)
- Fix APPLIED at `/keyframe_review/9/note`: The 1877 infobox area (345,155 km2) is a factor of 2.06 above the shape alive in 1877 (spanish-east-indies_1872, about 167,900 km2 on the grid); the author compared it only with the 1878 shape. Evidence: Spanish East Indies infobox: "1877: 345,155 km2"; gazetteer resolve of keyframe 9 = 664 cells (about 167,900 km2). Fix: Note that the infobox figure is the de jure claim and the shape the de facto holding (done by the reviewer).
- Thin at `/keyframe_review/10`: The 1878 keyframe adds the Cordillera, interior Mindanao, southern Palawan and Sulu (about +100,000 km2) with no gain event; only the Sulu vassal_start of July 1878 sits at the boundary. The Cordillera note itself says it was outside control only "until the early 19th century". Page to try: https://en.wikipedia.org/wiki/Spanish_colonization_of_the_Philippines
- Thin at `/ledger/28`: No 1898 loss to first-philippine-republic (same batch, found June 1898 with this dossier as counterpart); the revolution is a contest with the free-text "Philippine Revolution" over Luzon only, so the Visayas are drawn twice June-December 1898. Page to try: https://en.wikipedia.org/wiki/First_Philippine_Republic
- Thin at `/ledger/0`: Confidence 1: Bohol, Leyte, Samar in 1565 (page silent). Page to try: https://en.wikipedia.org/wiki/Captaincy_General_of_the_Philippines
- Thin at `/ledger/5`: Confidence 1: Luzon without the Cordillera in 1571 (page silent). Page to try: https://en.wikipedia.org/wiki/Spanish_colonization_of_the_Philippines
- Thin at `/ledger/32`: The infobox has "Remaining islands ceded to the United States: 23 March 1901" (Sibutu and Cagayan de Sulu, 1900 Treaty of Washington); the dossier ends 12 February 1899. Page to try: https://en.wikipedia.org/wiki/Treaty_of_Washington_(1900)

### straits-settlements: fix

- Area: infobox 3227 (1901); keyframe on the grid 3288 km2; ratio 0.98. infobox table 1,246 sq mi (census of 1901) against straits-settlements_1886
- Spot checks: /ledger/3 confirmed (Straits_Settlements); /ledger/4 confirmed (Straits_Settlements); /ledger/6 confirmed (Straits_Settlements); /ledger/10 confirmed (Straits_Settlements); /ledger/7 confirmed (Straits_Settlements)
- Fix APPLIED at `/ledger/0/counterpart`: The 1826 found named british-colonial-empire while prince-of-wales-island (same batch) dissolves into this dossier in 1826. Evidence: History of Penang: "In 1826, the British East India Company amalgamated the territories of Penang, Singapore ... and Malacca ... into a single political entity, the Straits Settlements." Fix: counterpart prince-of-wales-island (done).
- Fix APPLIED at `/ledger/5/counterpart`: The 1907 Labuan gain named british-colonial-empire while colony-of-labuan (same batch) records the loss to this dossier. Evidence: Crown Colony of Labuan: incorporation "took effect from 1 January 1907". Fix: counterpart colony-of-labuan (done).

### british-burma: pass

- Area: infobox none; keyframe on the grid 580911 km2; ratio None. no infobox area on British rule in Burma; 1886 shape is Myanmar (about 581,000 km2 on the grid, 676,578 km2 real)
- Spot checks: /ledger/0 confirmed (British_rule_in_Burma); /ledger/9 confirmed (British_rule_in_Burma); /ledger/14 confirmed (Federated_Shan_States); /ledger/19 confirmed (British_rule_in_Burma)
- Thin at `/ledger/8`: Confidence 1: Kachin and Chin hills in 1886 (page silent). Page to try: https://en.wikipedia.org/wiki/Third_Anglo-Burmese_War
- Thin at `/ledger/15`: Confidence 1: Kengtung returned in 1945; the Federated Shan States page has "Thailand left the territory in 1945" and relinquished its claim in 1946 (could be confidence 2). Page to try: https://en.wikipedia.org/wiki/Federated_Shan_States

### british-north-borneo: fix

- Area: infobox none; keyframe on the grid 71318 km2; ratio None. neither page gives an area; Sabah is 73,904 km2
- Spot checks: /ledger/5 confirmed (British_North_Borneo); /ledger/7 confirmed (British_North_Borneo); /ledger/12 confirmed (British_North_Borneo); /ledger/17 confirmed (Crown_Colony_of_North_Borneo); /ledger/18 confirmed (Crown_Colony_of_North_Borneo)
- Fix APPLIED at `/ledger/9/counterpart`: The 1890 Labuan gain named british-colonial-empire while colony-of-labuan (same batch) records the 1890 loss to this dossier. Evidence: Crown Colony of Labuan: "From 1890, Labuan came to be administered by the North Borneo Chartered Company." Fix: counterpart colony-of-labuan (done).
- Fix APPLIED at `/ledger/11/counterpart`: The 1904 Labuan loss named british-colonial-empire while colony-of-labuan records the 1904 gain from this dossier. Evidence: Crown Colony of Labuan: Labuan "reverted to British government rule in 1904". Fix: counterpart colony-of-labuan (done).

### dutch-east-india-company: thin

- Area: infobox none; keyframe on the grid 90285 km2; ratio None. infobox gives "Area served" only; 1752 shape about 90,000 km2
- Spot checks: /ledger/1 confirmed (Dutch%E2%80%93Portuguese_War); /ledger/3 confirmed (Dutch_East_India_Company); /ledger/12 confirmed (Mataram_Sultanate); /ledger/17 confirmed (Mataram_Sultanate); /ledger/21 confirmed (Mataram_Sultanate); /ledger/23 confirmed (Mataram_Sultanate)
- Thin at `/keyframe_review/9`: The Moluccas (Ternate, Tidore, Bacan suzerainty), Kupang on Timor (1653), the west Sumatra coast (Padang, Painan Treaty 1663) are not drawn; the author lists them as page-silent gaps. Page to try: https://en.wikipedia.org/wiki/Dutch_Moluccas
- Thin at `/ledger`: No British seizures of 1795-1796 (Padang 1795, Ambon and Banda 1796) as occupation events; the 1752-1799 shape keeps them to 1799. Page to try: https://en.wikipedia.org/wiki/Dutch_East_India_Company
- Thin at `/ledger/28`: Confidence 1: the four vassal_end events of December 1799 (Gowa, Banten, Surakarta, Yogyakarta) are inferred from the dissolution. Page to try: https://en.wikipedia.org/wiki/Dutch_East_India_Company
- Thin at `/identity`: Dutch Ceylon (1640-1796), Dutch Malabar (1661-1795), Dutch Formosa (1624-1662) are VOC land with no dossier yet (listed by the author); the Dutch Formosa dossier should take the 1642 Keelung gain that spanish-east-indies loses to dutch-republic. Page to try: https://en.wikipedia.org/wiki/Dutch_Formosa

### portuguese-malacca: pass

- Area: infobox none; keyframe on the grid 506 km2; ratio None. no infobox area; the page describes the walled town and three suburbs only
- Spot checks: /ledger/0 confirmed (Portuguese_Malacca); /ledger/1 confirmed (Portuguese_Malacca); /ledger/2 confirmed (Portuguese_Malacca)
- Nothing found: years in order, events on the pages with their years, keyframes and ledger agree.

### dutch-malacca: fix

- Area: infobox none; keyframe on the grid 506 km2; ratio None. no infobox area
- Spot checks: /ledger/0 confirmed (Dutch_Malacca); /ledger/1 mis-dated (Dutch_Malacca); /ledger/2 confirmed (Dutch_Malacca); /ledger/4 confirmed (Dutch_Malacca)
- Fix APPLIED at `/ledger/1/month`: The British occupation is dated January 1795 at confidence 3, but January is the month of the Kew Letters; the page gives no month for the surrender. Evidence: Dutch Malacca: "In January 1795, Dutch stadtholder William V ... issued the Kew Letters." ... "Malacca was thus surrendered to British control" (no month). Fix: month removed, year kept (done).

### federated-malay-states: pass

- Area: infobox none; keyframe on the grid 60443 km2; ratio None. no infobox area (population only); the four states are about 71,600 km2
- Spot checks: /ledger/0 confirmed (Federated_Malay_States); /ledger/2 confirmed (Federated_Malay_States); /ledger/3 confirmed (Federated_Malay_States); /ledger/4 confirmed (Federated_Malay_States)
- Nothing found: years in order, events on the pages with their years, keyframes and ledger agree.

### portuguese-timor: thin

- Area: infobox 14874; keyframe on the grid 13657 km2; ratio 1.09. infobox 14,874 km2 (no year, the modern territory) against portuguese-timor_1859
- Spot checks: /ledger/1 confirmed (Portuguese_Timor); /ledger/3 confirmed (Treaty_of_Lisbon_(1859)); /ledger/7 confirmed (Portuguese_Timor); /ledger/9 confirmed (Portuguese_Timor); /ledger/2 not on page (Treaty_of_Lisbon_(1859))
- Fix APPLIED at `/ledger/2/region`: The 1769 loss named only Ambeno while the 1769 keyframe removes Ambeno and Liquica (Maubara) and the 1859 gain returns both. Evidence: portuguese-timor_1769 correction minus = Ambeno + Liquica; Treaty of Lisbon (1859): the Netherlands gave up "the kingdoms of Maubara and Ambeno". Fix: region widened to Ambeno and Liquica so ledger and keyframe agree (done).
- Thin at `/ledger/2`: Confidence 1 reading: Ambeno lost to the Dutch in 1769. The Treaty of Lisbon (1859) page says Ambeno already flew the Portuguese flag, and Lifau (capital to 1769) lies in Oecusse, so Ambeno probably stayed Portuguese; only Maubara looks Dutch before 1859. No year or page for either; the VOC dossier has no mirror gain. Page to try: https://en.wikipedia.org/wiki/Oecusse
- Thin at `/ledger/5`: Maucatar placed in Cova Lima by the researcher; the page names no district. Page to try: https://en.wikipedia.org/wiki/Portuguese_Timor

### sultanate-of-berau: pass

- Area: infobox none; keyframe on the grid 14921 km2; ratio None. no area on either page
- Spot checks: /ledger/0 confirmed (Kesultanan_Berau); /ledger/1 confirmed (Sultanate_of_Bulungan); /ledger/2 confirmed (Sultanate_of_Bulungan); /ledger/3 confirmed (Kesultanan_Gunung_Tabur)
- Thin at `/ledger/3`: The 1810 split names only sultanate-of-sambaliung; there is no 1810 loss to sultanate-of-gunung-tabur (same batch), whose found and gain name this dossier. Page to try: https://id.wikipedia.org/wiki/Kesultanan_Gunung_Tabur

### mangkunegaran: thin

- Area: infobox none; keyframe on the grid 3035 km2; ratio None. no infobox area
- Spot checks: /ledger/0 confirmed (Mangkunegaran); /ledger/1 confirmed (Mangkunegaran)
- Thin at `/ledger`: No vassal relation: the page says Raden Mas Said "signed a treaty with the Dutch East India Company (VOC) in 1757" and "swore allegiance to the rulers of Surakarta, Yogyakarta, and the Dutch East Indies Company"; vassal_start 1757 (VOC, then dutch-east-indies) is missing. No Japanese occupation 1942-1945 (page silent; pakualaman has it). Page to try: https://en.wikipedia.org/wiki/Mangkunegaran
- Thin at `/keyframe_review/0`: The page gives the modern extent (northern Surakarta, all of Karanganyar and Wonogiri, parts of Gunung Kidul) and "49% of the Surakarta core after 1830"; the three discs are a reading, no change of land 1757-1830 is recorded. Page to try: https://en.wikipedia.org/wiki/Mangkunegaran

### pakualaman: pass

- Area: infobox none; keyframe on the grid 1264 km2; ratio None. no infobox area
- Spot checks: /ledger/0 confirmed (Pakualaman); /ledger/1 confirmed (Pakualaman); /ledger/2 confirmed (Pakualaman); /ledger/3 confirmed (Pakualaman)
- Nothing found: years in order, events on the pages with their years, keyframes and ledger agree.

### diponegoro-s-rebels: fix

- Area: infobox none; keyframe on the grid 6070 km2; ratio None. rebel state, no infobox area
- Spot checks: /ledger/0 confirmed (Java_War); /ledger/2 mis-dated (Java_War); /ledger/3 confirmed (Java_War); /ledger/4 confirmed (Java_War)
- Fix APPLIED at `/ledger/2`: The 1827 loss was confidence 1 with month 7, but the page gives the year and the land (no month). Evidence: Java War: "By 1827, Dutch forces began employing ... Benteng-stelsel", "his territorial control began to shrink", rebels "confined to the west of Yogyakarta". Fix: confidence 2, month removed (done).

### padri-movement: fix

- Area: infobox none; keyframe on the grid 28072 km2; ratio None. rebel state, no infobox area
- Spot checks: /ledger/2 confirmed (Padri_War); /ledger/6 confirmed (Padri_War); /ledger/7 confirmed (Padri_War); /ledger/8 confirmed (Padri_War); /ledger/3 confirmed (Padri_War)
- Fix APPLIED at `/ledger/3/confidence`: The 1822 end of the Padri hold on Pagaruyung was confidence 1, but the page dates it. Evidence: Padri War: "On 4 March 1822" Dutch troops under Raaff "succeeded in pushing the Padri people out of Pagaruyung". Fix: confidence 2 (done).

### dutch-new-guinea: pass

- Area: infobox 421981; keyframe on the grid 346726 km2; ratio 1.22. infobox 421,981 km2 (no year)
- Spot checks: /ledger/0 confirmed (Dutch_New_Guinea); /ledger/1 confirmed (Operation_Trikora); /ledger/2 confirmed (Operation_Trikora); /ledger/4 confirmed (Dutch_New_Guinea)
- Thin at `/ledger/3`: The infobox has "Disestablished: 1 October 1962"; the dossier runs to 1 May 1963 to meet republic-of-indonesia and calls UNTEA a status caption, while the author also asks se-04 for a UNTEA dossier. Choose one: end on 1 October 1962 with a UNTEA dossier, or drop the UNTEA request. Page to try: https://en.wikipedia.org/wiki/Operation_Trikora

### colony-of-labuan: fix

- Area: infobox none; keyframe on the grid 253 km2; ratio None. no infobox area; one grid cell
- Spot checks: /ledger/0 confirmed (Crown_Colony_of_Labuan); /ledger/2 confirmed (Crown_Colony_of_Labuan); /ledger/3 confirmed (Crown_Colony_of_Labuan); /ledger/4 confirmed (Crown_Colony_of_Labuan)
- Fix APPLIED at `/keyframe_review/0`: The single keyframe drew Labuan 1846-1907 although the ledger loses it to british-north-borneo in 1890 and regains it in 1904, and british-north-borneo draws it 1890-1903. Evidence: Crown Colony of Labuan: "From 1890, Labuan came to be administered by the North Borneo Chartered Company"; "reverted to British government rule in 1904". Fix: keyframe 0 cut to 1846-1889 and keyframe colony-of-labuan_1904 added for 1904-1907 (done).

### karangasem-lombok: pass

- Area: infobox none; keyframe on the grid 4805 km2; ratio None. no infobox area; Lombok is about 4,700 km2
- Spot checks: /ledger/0 confirmed (Lombok); /ledger/1 confirmed (Lombok); /ledger/2 confirmed (Dutch_intervention_in_Lombok_and_Karangasem); /ledger/6 confirmed (Dutch_intervention_in_Lombok_and_Karangasem)
- Nothing found: years in order, events on the pages with their years, keyframes and ledger agree.

### first-philippine-republic: pass

- Area: infobox 298719 (1898); keyframe on the grid 179559 km2; ratio 1.66. infobox 298,719 km2 (1898) against first-philippine-republic_1898, which leaves out Manila and Mindanao as the infobox says ("except Manila and parts of Mindanao")
- Spot checks: /ledger/0 confirmed (First_Philippine_Republic); /ledger/3 confirmed (First_Philippine_Republic); /ledger/5 confirmed (First_Philippine_Republic); /ledger/6 confirmed (First_Philippine_Republic)
- Thin at `/ledger/4`: Confidence 1: the 1900 loss of everything but Nueva Vizcaya, Kalinga and Isabela; the page has the seat at Bayombong from November 1899, Lubuagan March-May 1900, Palanan from December 1900. Page to try: https://en.wikipedia.org/wiki/First_Philippine_Republic

### insular-government-of-the-philippine-islands: pass

- Area: infobox 297916 (1903); keyframe on the grid 266304 km2; ratio 1.12. infobox 297,916 km2 (1903)
- Spot checks: /ledger/0 confirmed (Insular_Government_of_the_Philippine_Islands); /ledger/6 confirmed (Commonwealth_of_the_Philippines); /ledger/8 confirmed (Commonwealth_of_the_Philippines); /ledger/11 confirmed (Commonwealth_of_the_Philippines)
- Nothing found: years in order, events on the pages with their years, keyframes and ledger agree.

### sultanate-of-gunung-tabur: thin

- Area: infobox none; keyframe on the grid 6070 km2; ratio None. no area on the page
- Spot checks: /ledger/0 confirmed (Kesultanan_Gunung_Tabur); /ledger/2 confirmed (Sultanate_of_Bulungan); /ledger/5 confirmed (Kesultanan_Gunung_Tabur); /ledger/4 not on page (Kesultanan_Gunung_Tabur)
- Thin at `/keyframe_review/0`: Disc only: the id page gives the land north of the Berau River and both banks of the Segah, bordering Bulungan to the north and Sambaliung to the west and south; no boundary or area. Page to try: https://id.wikipedia.org/wiki/Kesultanan_Gunung_Tabur
- Thin at `/ledger/2`: The 1834 Dutch contract is on the Bulungan page for Berau ("After the Dutch conquered Berau in 1834 ... 27 September"); Gunung Tabur is not named. Page to try: https://en.wikipedia.org/wiki/Sultanate_of_Bulungan
- Thin at `/ledger/4`: Confidence 1: vassal of Indonesia from December 1949 (the id infobox has 1951-1960, swapraja under Daerah Istimewa Berau). Page to try: https://id.wikipedia.org/wiki/Kesultanan_Gunung_Tabur

### british-bencoolen: thin

- Area: infobox none; keyframe on the grid 19220 km2; ratio None. the Bengkulu page gives the modern province only (20,181.53 km2), as the note says
- Spot checks: /ledger/0 confirmed (Bengkulu); /ledger/1 confirmed (Dutch_Malacca)
- Thin at `/keyframe_review/0`: The shape is the modern province (about 19,200 km2) from 1685, an upper bound the author flags; the page has a pepper centre and garrison in 1685, Fort Marlborough 1714, and "In 1785 the area was integrated into British Empire as Bencoolen". Page to try: https://en.wikipedia.org/wiki/Fort_Marlborough
- Thin at `/ledger`: No French occupation of 1760 and no events for Singapore 1819-1824 (Raffles was Lieutenant-Governor of Bencoolen 1818-1824); pages silent. Page to try: https://en.wikipedia.org/wiki/Fort_Marlborough

### prince-of-wales-island: fix

- Area: infobox none; keyframe on the grid 759 km2; ratio None. no infobox area; the 1800 strip was 189.3 km2, smaller than the modern Seberang Perai drawn (noted in the new keyframe)
- Spot checks: /ledger/0 confirmed (History_of_Penang); /ledger/1 confirmed (History_of_Penang); /ledger/2 confirmed (History_of_Penang); /ledger/3 confirmed (History_of_Penang)
- Fix APPLIED at `/keyframe_review/0`: The one keyframe drew the mainland strip (Seberang Perai) from 1786, but the ledger gains it in 1800 and it is two thirds of the shape. Evidence: History of Penang: in 1800 Leith "gained a 189.3 km2 strip of Seberang Perai from the new Sultan of Kedah". Fix: keyframe 0 cut to 1786-1799 with the island disc only, keyframe prince-of-wales-island_1800 added with the island and the strip for 1800-1826 (done).

### setul-mambang-segara: pass

- Area: infobox none; keyframe on the grid 2529 km2; ratio None. no infobox area
- Spot checks: /ledger/0 confirmed (Setul_Mambang_Segara); /ledger/1 confirmed (Setul_Mambang_Segara); /ledger/2 confirmed (Setul_Mambang_Segara); /ledger/5 confirmed (Setul_Mambang_Segara)
- Nothing found: years in order, events on the pages with their years, keyframes and ledger agree.

### kubang-pasu: pass

- Area: infobox none; keyframe on the grid 1264 km2; ratio None. no infobox area
- Spot checks: /ledger/0 confirmed (Kingdom_of_Kubang_Pasu_Darul_Qiyam); /ledger/3 confirmed (Kingdom_of_Kubang_Pasu_Darul_Qiyam); /ledger/1 not on page (Kingdom_of_Kubang_Pasu_Darul_Qiyam)
- Thin at `/ledger/1`: Confidence 1: Siamese clientage from 1839 (infobox "Client state of Siam", undated). Page to try: https://en.wikipedia.org/wiki/Kingdom_of_Kubang_Pasu_Darul_Qiyam

## Within-batch open items (for the author)

- spanish-east-indies / first-philippine-republic: the republic is founded in June 1898 from spanish-east-indies, which has no loss to it (contest with the free text "Philippine Revolution" over Luzon only). Add a 1898 loss to first-philippine-republic (Philippines without Manila and Mindanao, First Philippine Republic page) or a contest over the same land naming the slug.
- spanish-east-indies / insular-government-of-the-philippine-islands: the 1898-12 loss names united-states-of-america, the insular government is founded 1899-04 from spanish-east-indies. One of the two strings should change.
- first-philippine-republic: its 1899-1901 losses name united-states-of-america (am-07), whose ledger has only a contest with the republic; the in-batch colony dossier insular-government-of-the-philippine-islands draws the whole Philippines from April 1899 with a contest. Decide which dossier takes the republic's land and make the strings agree.
- sultanate-of-berau / sultanate-of-gunung-tabur: Gunung Tabur is founded and gains land from Berau in 1810; Berau dissolves naming only sultanate-of-sambaliung. Add a Berau 1810 loss to sultanate-of-gunung-tabur, or drop the duplicate gain.
- dutch-new-guinea: runs to May 1963 although the infobox disestablishes it on 1 October 1962, while the report asks se-04 for a UNTEA dossier; pick one. On the contest date: Operation Trikora has Indonesian forces holding Teminabuan on 21 May 1962 (and drops at Fakfak on 26 April); the dossier's May 1962 is the earlier, supported date; the Indonesian sibling's 24 June (Merauke) is within the year.
- portuguese-timor / dutch-east-india-company: the 1769 loss to the VOC has no VOC mirror and rests on a confidence-1 reading (see above).

## Cross-dossier matrix (summary; the full list is in the report JSON)

183 territorial events: 26 matched, 90 mismatch, 33 missing, 34 exceptions (nobody, groups not yet run, free-text counterparts, malayan-union).

- empire-of-japan: 22 (straits-settlements 1941 occupation_start; straits-settlements 1942 occupation_start; straits-settlements 1942 occupation_start; straits-settlements 1942 occupation_start; straits-settlements 1945 occupation_end; straits-settlements 1945 occupation_end; straits-settlements 1945 occupation_end; straits-settlements 1945 occupation_end ...)
- dutch-east-indies: 14 (portuguese-timor 1859 loss; portuguese-timor 1859 gain; portuguese-timor 1904 gain; portuguese-timor 1904 loss; diponegoro-s-rebels 1827 loss; diponegoro-s-rebels 1830 dissolve; padri-movement 1831 loss; padri-movement 1832 loss ...)
- sultanate-of-sulu: 9 (spanish-east-indies 1635 gain; spanish-east-indies 1663 loss; spanish-east-indies 1718 gain; spanish-east-indies 1724 gain; spanish-east-indies 1851 vassal_start; spanish-east-indies 1876 vassal_end; spanish-east-indies 1878 vassal_start; spanish-east-indies 1898 vassal_end ...)
- mataram-sultanate: 8 (dutch-east-india-company 1680 gain; dutch-east-india-company 1705 gain; dutch-east-india-company 1705 gain; dutch-east-india-company 1705 gain; dutch-east-india-company 1718 gain; dutch-east-india-company 1743 gain; dutch-east-india-company 1749 vassal_start; dutch-east-india-company 1755 vassal_end)
- sultanate-of-brunei: 7 (british-north-borneo 1877 found; british-north-borneo 1884 gain; british-north-borneo 1884 gain; british-north-borneo 1885 gain; british-north-borneo 1885 gain; british-north-borneo 1898 gain; colony-of-labuan 1846 found)
- sultanate-of-kedah: 7 (prince-of-wales-island 1786 found; prince-of-wales-island 1800 gain; setul-mambang-segara 1892 vassal_start; setul-mambang-segara 1909 vassal_end; kubang-pasu 1839 found; kubang-pasu 1859 merge; kubang-pasu 1859 dissolve)
- republic-of-indonesia: 5 (mangkunegaran 1945 dissolve; pakualaman 1945 dissolve; sultanate-of-gunung-tabur 1949 vassal_start; sultanate-of-gunung-tabur 1960 vassal_end; sultanate-of-gunung-tabur 1960 dissolve)
- rattanakosin-kingdom: 5 (setul-mambang-segara 1843 vassal_start; setul-mambang-segara 1916 vassal_end; setul-mambang-segara 1916 dissolve; kubang-pasu 1839 vassal_start; kubang-pasu 1859 vassal_end)
- united-states-of-america: 4 (spanish-east-indies 1898 loss; first-philippine-republic 1899 loss; first-philippine-republic 1900 loss; first-philippine-republic 1901 dissolve)
- sultanate-of-banten: 4 (dutch-east-india-company 1619 gain; dutch-east-india-company 1683 vassal_start; dutch-east-india-company 1752 gain; dutch-east-india-company 1799 vassal_end)
- sultanate-of-gowa: 4 (dutch-east-india-company 1667 gain; dutch-east-india-company 1667 gain; dutch-east-india-company 1667 vassal_start; dutch-east-india-company 1799 vassal_end)
- burma: 3 (british-burma 1826 found; british-burma 1853 gain; british-burma 1886 gain)
- republic-of-the-philippines: 3 (british-north-borneo 1947 loss; insular-government-of-the-philippine-islands 1946 loss; insular-government-of-the-philippine-islands 1946 dissolve)
- sultan-of-yogyakarta: 3 (dutch-east-india-company 1755 vassal_start; dutch-east-india-company 1799 vassal_end; diponegoro-s-rebels 1825 found)
- sultanate-of-perak: 2 (straits-settlements 1874 gain; straits-settlements 1935 loss)
- kingdom-of-thailand: 2 (british-burma 1943 loss; british-burma 1945 gain)
- portuguese-empire: 2 (dutch-east-india-company 1605 gain; portuguese-timor 1702 found)
- sultanate-of-cirebon: 2 (dutch-east-india-company 1680 vassal_start; dutch-east-india-company 1705 vassal_end)
- surakarta-sunanate: 2 (dutch-east-india-company 1755 vassal_start; dutch-east-india-company 1799 vassal_end)
- kingdom-of-bulungan: 2 (sultanate-of-berau 1731 vassal_start; sultanate-of-berau 1789 vassal_end)
- spanish-east-indies: 2 (first-philippine-republic 1898 found; insular-government-of-the-philippine-islands 1899 found)
- sultanate-of-berau: 2 (sultanate-of-gunung-tabur 1810 found; sultanate-of-gunung-tabur 1810 gain)
- rajahnate-of-cebu: 1 (spanish-east-indies 1565 found)
- maynila: 1 (spanish-east-indies 1571 gain)
- sultanate-of-maguindanao: 1 (spanish-east-indies 1849 gain)
- union-of-burma: 1 (british-burma 1948 dissolve)
- malaysia: 1 (british-north-borneo 1963 dissolve)
- sultanate-of-malacca: 1 (portuguese-malacca 1511 found)
- dutch-east-india-company: 1 (portuguese-timor 1769 loss)
- east-timor: 1 (portuguese-timor 1975 dissolve)
- pagaruyung-kingdom: 1 (padri-movement 1803 found)

Main routes: empire-of-japan (jk-01) records its occupations against british-colonial-empire, united-states-of-america and dutch-east-indies, not the colony dossiers (straits-settlements, federated-malay-states, british-north-borneo, british-burma, portuguese-timor, insular-government-of-the-philippine-islands, pakualaman); burma (se-01) names british-empire / british-raj for 1826, 1853, 1885; the se-02 sultanates (mataram-sultanate, sultanate-of-banten, sultanate-of-gowa, sultanate-of-cirebon) name dutch-republic where the VOC dossier now exists, and sultanate-of-sulu has none of the Spanish events; dutch-east-indies (se-03) names british-colonial-empire for the 1825 Bencoolen exchange and "rulers of Lombok (no dossier)" / bali for 1894; kingdom-of-thailand (se-04) names british-raj / british-colonial-empire for Kengtung (1942-05, 1943-10) where british-burma has August 1943 (Federated Shan States page: annexation formalised 1 August 1943); sultanate-of-kedah (se-02) treats Setul as its land (1808 loss, 1892 gain) and has no Kubang Pasu events; kingdom-of-bulungan writes "Berau Sultanate" instead of the slug sultanate-of-berau.

## Files changed by the reviewer

straits-settlements, british-north-borneo, dutch-malacca, padri-movement, diponegoro-s-rebels, portuguese-timor, colony-of-labuan, prince-of-wales-island, spanish-east-indies: each change is marked in the note it touches with "[Reviewer se-03-x, 2026-10-24: ...]"; all nine re-validate with --resolve (no new warnings).
