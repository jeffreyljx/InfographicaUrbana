# Review of batch sa-06-d

Reviewer sa-06-d, 2026-10-25. Dossiers: british-ceylon, kashmir-and-jammu, british-raj, islamic-republic-of-pakistan. Validator (--resolve): 0 errors in all four; warnings only for counterparts without dossiers (hunza-and-nagar, chitral) after the reviewer's slug fixes. Neighbour dossiers read: dutch-ceylon, kingdom-of-kandy, british-empire, east-india-company, sikh-empire, mughal-empire, hyderabad-state, kingdom-of-sikkim, tibet, emirate-of-afghanistan, burma, british-burma, empire-of-japan, nepal, kingdom-of-bhutan, khanate-of-kalat, bahawalpur-state, sultanate-of-oman, danish-india, kingdom-of-manipur, gwalior-state, kingdom-of-thailand, chiangmai, kengtung, union-of-burma. Not yet written (exception): republic-of-india, people-s-republic-of-china, people-s-republic-of-bangladesh, talpur-dynasty, british-colonial-empire, the Soviet and Iranian rows.

Verdicts: british-ceylon pass; kashmir-and-jammu fail; british-raj fail; islamic-republic-of-pakistan thin. Fixes marked APPLIED were made in the dossier by the reviewer and re-validated; the others are for the author.

## british-ceylon: pass

Tried to break: years and months of found/gain/dissolve against both pages (all match); mirrors in dutch-ceylon (1796-02 dissolve to british-ceylon) and kingdom-of-kandy (1815-02 dissolve to british-ceylon) match within a month; certainty 1796-1814 + 1815-1948 is contiguous; the Ceylon/British Ceylon Wikidata split is argued in notes; the new keyframe has from, to and correction. Not a fault: the Uva Rebellion war (1817-1818) has a zone but no contest events (the brief only requires contest events to sit in a war zone); the notes say a sri-lanka dossier exists, which it does not yet (sa-06 parallel part, an allowed exception).

Area: infobox 65993 km2 (1946), Cliopatria 28908 km2, ratio 0.44. No Cliopatria British Ceylon shape is alive in 1946 (the row ends 1814); 28,908 km2 is the 1796-1814 coastal belt, against which the infobox's whole-island 65,993 km2 is 0.44, acknowledged in /keyframe_review/0. The new 1815-1947 keyframe (country Sri Lanka, about 65,600 km2) matches the infobox (ratio about 0.99).

Spot checks:
- `/ledger/0` (Kingdom_of_Kandy): confirmed: 'by the 15 of that month, Colombo had fallen and Dutch rule on the island had come to an end' (February 1796); confidence 2 fits the 14/15 February vs 5 March 1796 conflict the note records
- `/ledger/1` (British_Ceylon): confirmed: infobox 'Proclamation of the Crown colony: 25 March 1802'
- `/ledger/2` (Kingdom_of_Kandy): confirmed: 'On 31 January 1803, a British force led by General Hay Macdowall marched to Kandy and found it evacuated'
- `/ledger/5` (British_Ceylon): confirmed: 'In 1815 Kandy was captured in the Second Kandyan War, ending Sri Lankan independence'; infobox 'Signing of Kandyan Convention: 2 March 1815'
- `/ledger/7` (British_Ceylon): confirmed: infobox 'Independence: 4 February 1948'

## kashmir-and-jammu: fail

Area: infobox None km2 (None), Cliopatria 182006 km2, ratio None. The princely state page has no area in the infobox or the text (checked); the dossier says so. The 1947 shape is 182,006 km2; the 1846-1884 outlines (164,500-169,500 km2) carry 17,200 km2 of Himachal Pradesh, corrected.

Findings:
- [BLOCKING] `/ledger (missing events)`: The princely state has no vassal relation to Britain at all, although three dossiers record it as their vassal and the dossier's own pages state it. Evidence: Treaty of Amritsar page, Article 10: 'Maharajah Gulab Singh acknowledges the supremacy of the British Government'; Jammu and Kashmir (princely state) page: 'in a subsidiary alliance with the British East India Company from 1846 to 1858' and British paramountcy 'from 1858 until British withdrawal and the partition of British India in 1947', infobox 'End of British Crown Suzerainty: 15 August 1947'. Mirrors with no counterpart here: british-empire /ledger/68 (1846 vassal_start kashmir-and-jammu) and /ledger/103 (1858-11 vassal_end); east-india-company /ledger/66 and /ledger/98 (same); british-raj /ledger/3 (1858-11 vassal_start kashmir-and-jammu) and /ledger/25 (1947-08 vassal_end), both in this same batch. Fix: Add vassal_start british-empire 1846-03 (Treaty of Amritsar, Art. 10, confidence 3), vassal_end british-empire 1858-11, vassal_start british-raj 1858-11 and vassal_end british-raj 1947-08 (princely state page), region {cliopatria: Kashmir and Jammu, year 1846 or 1947} as in the found event and the Raj's events. If the orchestrator rules east-india-company rather than british-empire as the 1846-1858 overlord, use that slug.
- [to do] `/end and /ledger/9 (with islamic-republic-of-pakistan /ledger/3, /ledger/4, /ledger/6)`: The state ends with a dissolve in October 1947, but the pakistan dossier gains Gilgit (1947-11), Azad Kashmir (1947-11) and Baltistan (1948-08) from kashmir-and-jammu after that end, and this ledger has no mirror loss. Evidence: Indo-Pakistani war of 1947-1948 page: accession 'on 26 October 1947'; 'By 1 November, Gilgit-Baltistan had been annexed from the Dogra dynasty'; Mirpur 'captured ... on 25 November 1947'; Skardu surrendered 'On 14 August' 1948. Gains from a state that no longer exists cannot be mirrored. Fix: Settle one model with the pakistan dossier: either keep the end at 1947-10 and have pakistan name republic-of-india (the state having acceded) as counterpart of its 1947-11 and 1948-08 gains, or extend this state to the ceasefire of 1 January 1949 with loss events to islamic-republic-of-pakistan in 1947-11 (Gilgit; Azad Kashmir) and 1948-08 (Baltistan) before the dissolve.
- [APPLIED] `/ledger/7 (was /ledger/6)`: occupation_start by british-raj of Gilgit dated 1889 at confidence 3 is mis-dated: in 1889 the page has only a Political Agent; the land passed under the 1935 lease. Evidence: Gilgit Agency page: Gilgit and Astore tehsils 'comprised the Gilgit wazarat of Jammu and Kashmir with its own governor' under dual rule; infobox 'Gilgit Wazarat leased: 26 March 1935'; 'The part of Gilgit wazarat lying to the west of Indus was leased by British in 1935.' Fix: Applied by the reviewer: year 1889 -> 1935, month 3, region text 'the Gilgit Leased Area', event moved after the 1891 event to keep the ledger sorted; the mirror in british-raj moved the same way. Validates.
- [APPLIED] `/ledger/10`: vassal_end of hunza-and-nagar dated 1947-11, after the state's own end (1947-10). Evidence: identity.end and the dissolve are 1947-10; the Gilgit-Baltistan page has Hunza accede to Pakistan on 3 November and Nagar on 18 November 1947. Fix: Applied by the reviewer: month 11 -> 10 with a note. Validates.
- [APPLIED] `/wars/2`: The Indo-Pakistani War of 1947-1948 ran to 1949, outside the state's life (end 1947). Evidence: Brief check 2: wars inside the life; war page: accession 26 October 1947, ceasefire 1 January 1949. Fix: Applied by the reviewer: to 1949 -> 1947 with a note that the war continues in the india and pakistan dossiers.

Thin (for a gap-filler):
- `/ledger/4`: Year of the loss of Gilgit to Gohar Aman (confidence 1, dated from the Cliopatria outline); the Gilgit-Baltistan page summary gives 'Gohar Aman of Yasin conquered Gilgit in 1842' and no year for the second conquest. Try https://en.wikipedia.org/wiki/Gohar_Aman
- `/keyframe_review/7`: The 1891-1946 keyframe adds 25,800 km2 in Gilgit-Baltistan against 1884; Hunza and Nagar are explained (1891 vassal_start) but Yasin, Punial, Kuh-Ghizar and Ishkoman have no event (the Dogra conquest of Yasin in the 1860s). Try https://en.wikipedia.org/wiki/Yasin_Valley
- `/keyframe_review/1, /keyframe_review/2, /keyframe_review/4`: 1848, 1849 and 1859 cell changes unverified: page budget (allowed). Try https://en.wikipedia.org/wiki/Gulab_Singh

Spot checks:
- `/ledger/2` (Treaty_of_Amritsar_(1846)): confirmed: 'in early 1847, Gulab Singh ceded Hazara back to the Lahore Darbār', 'in exchange for territory near Jammu'
- `/ledger/3` (Treaty_of_Amritsar_(1846)): confirmed at confidence 2: exchange 'for territory near Jammu'; 'Kashmir retained Bhadrawah, Lakhanpur, and Chandgraon'
- `/ledger/5` (Gilgit-Baltistan): confirmed: 'It was not until his death in 1860 that Dogras finally managed to subdue Gilgit.'
- `/ledger/7 (was /ledger/6)` (Gilgit_Agency): mis-dated: the page gives a Political Agent in 1889 but Kashmir's own governor and dual rule until the lease of 26 March 1935; fixed to 1935-03 by the reviewer
- `/ledger/8` (Gilgit_Agency): confirmed: lease terminated '30 July 1947' (infobox), 1 July in the text, as the note says
- `/ledger/9` (Jammu_and_Kashmir_(princely_state)): confirmed: 'On 26 October 1947, Hari Singh acceded' (infobox 27 October 1947)

## british-raj: fail

Area: infobox 4993650 km2 (None), Cliopatria 4902308 km2, ratio 0.98. Infobox area has no year; compared with the 1946 shape as the author did. The corrected 1946 Raj (minus Burma about 677,000, Ceylon about 66,000 and Kashmir 182,000, plus the 33,400 km2 frontier tract) is about 4.0 M km2, ratio about 0.80: within a factor of two either way.

Findings:
- [BLOCKING] `/ledger (missing events, 1893 and 1895)`: The Durand Line agreement is not in the ledger, although the Durand Line page is one of the dossier's sources and the emirate-of-afghanistan dossier records two gains from british-raj on it at confidence 3; the omission is not flagged in the notes. Evidence: emirate-of-afghanistan /ledger/18 (1893-11 gain from british-raj: 'Asmar in Kunar Valley as far as Chanak was ceded to Afghanistan', Nuristan and 'parts of Chitral' granted to Afghanistan) and /ledger/19 (1895 gain from british-raj: 'Nasrat and Bashgal, along with other areas, were ceded to Afghanistan'), both citing the Durand Line page. The Raj's certainty notes date the line 12 November 1893, and /keyframe_review/7 (1895) adds 16,400 km2 in Khyber Pakhtunkhwa that only the Chitral vassalage is said to explain. Fix: Add loss events to emirate-of-afghanistan 1893-11 and 1895 with the Afghan dossier's regions and the Durand Line page as source; add the British side of the 1893 settlement (Waziristan, Bajaur, Mohmand, Chagai brought inside the British line) as gain events if the page names them, and say in the 1895 verdict which part of the 16,400 km2 is Durand land and which is Chitral.
- [BLOCKING] `/ledger/15 and /keyframe_review/9-19 corrections`: The 1914 gain from tibet takes all of Arunachal Pradesh, Tawang included, and the 1939-1946 corrections re-add the 33,400 km2 Cliopatria drops, against the page the event cites. Evidence: McMahon Line page: 'The district remained in Tibetan hands until 1951'; Lightfoot's 1938 visit was brief and Tibet 'regained its authority'; the page places Tawang 'under British jurisdiction' on paper only and does not describe a cession. The tibet dossier has /ledger/35 1914-07 contest_start british-raj (Tawang tract) and /ledger/39 1944 occupation_start by british-raj of the tract south of the Sela Pass only. The Raj's own note: 'Treaty gain on paper, administered land only later.' Fix: Take the Tawang tract north of the Sela Pass (about 27.6 N 91.9 E) out of the 1914 gain and out of every Raj correction 1914-1946, or turn the 1914 event into a contest_start with tibet as the tibet dossier has it and add a 1944 occupation_start of the tract south of the Sela Pass; keep the tribal belt the British actually entered. Align type and month with tibet /ledger/35.
- [to do] `/ledger (missing event, 1865) and /wars/1/zones`: No gain of the Bengal Duars from Bhutan in 1865, and the Anglo-Bhutan War has empty zones although ground changed hands (flagged by the author as page silent). Evidence: kingdom-of-bhutan /ledger/17 1865-11 loss to british-raj ('the whole of the tract known as the Eighteen Duars' and 'the Hill territory on the left bank of the Teesta', Duar War page, confidence 3) and /ledger/18 (Dewangiri). Brief check 10: empty zones only where no ground changed hands. Fix: Add a 1865-11 gain from kingdom-of-bhutan (Bengal Duars and the Kalimpong hills, Duar War page) and the same region as the war's zone, with contest events 1864-1865.
- [to do] `/ledger (missing event, 1860)`: No loss of the western Terai (Naya Muluk) to Nepal in 1860. Evidence: nepal /ledger/31 1860 gain from british-raj, confidence 2, Nepal page: 'In 1860 some parts of the western Terai region were gifted to Nepal by the British'. Fix: Add a 1860 loss to nepal with nepal's region and the Nepal page.
- [to do] `/ledger (missing events, 1903-1908 and 1944)`: The British expedition to Tibet and the occupation of the Chumbi Valley are absent, as is the 1944 occupation of the tract south of the Sela Pass. Evidence: tibet /ledger/25-26 (1903-12 to 1904-09 contest with british-raj, Chumbi Valley and the Gyantse road, confidence 3), /ledger/27 and /ledger/29 (1904-09 to 1908-02 occupation of the Chumbi Valley by british-raj), /ledger/39 (1944 occupation_start by british-raj). Fix: Add the war (British expedition to Tibet, 1903-1904) with its zone, occupation_start/occupation_end of the Chumbi Valley 1904-09 / 1908-02, and the 1944 occupation (see the McMahon finding).
- [to do] `/ledger (missing events, Baluchistan and Kalat)`: No event for British Baluchistan or the Khanate of Kalat, though the Raj page lists 'Baluchistan established as a Chief Commissionership' under Lytton (1876-1880) and the Raj outline holds the whole of Baluchistan. Evidence: khanate-of-kalat /ledger/13 1877 loss to british-raj ('Quetta and Pishin, which became British Baluchistan', confidence 1; its note quotes the Baluchistan Agency page, 'following the 1876 treaty'). The kalat dossier was rewritten at 06:50 today and no longer carries a 1876-1947 vassal_start/vassal_end with british-raj. Fix: Add a 1877 gain from khanate-of-kalat (Quetta and Pishin), and a vassal_start khanate-of-kalat (the 1876 treaty) with vassal_end 1947-08 once the kalat dossier settles; source the Baluchistan Agency page.
- [to do] `/ledger (missing events, 1891)`: The Anglo-Manipur War and the British occupation of the Imphal valley in 1891 are absent. Evidence: kingdom-of-manipur /ledger/7-10: 1891-03 contest_start, 1891-04 occupation_start, 1891-04 contest_end, 1891-09 occupation_end, all british-raj, confidence 3. Fix: Add the mirror events and the war, or a vassal tint for Manipur if the orchestrator wants the princely states drawn.
- [APPLIED] `/ledger/16 (was /ledger/11)`: occupation_start of Gilgit dated 1889 at confidence 3 is mis-dated: in 1889 the page has only a permanent Political Agent; the British took the land under the 1935 lease. Evidence: Gilgit Agency page: Gilgit and Astore 'comprised the Gilgit wazarat of Jammu and Kashmir with its own governor' (dual rule); infobox 'Gilgit Wazarat leased: 26 March 1935'. Fix: Applied by the reviewer: 1889 -> 1935-03, region text 'the Gilgit Leased Area', event re-sorted after 1914; the kashmir-and-jammu mirror moved the same way. Validates.
- [APPLIED] `/ledger/5`: The 1869 Nicobar gain names counterpart nobody, but Denmark sold the islands to Britain and danish-india records the loss. Evidence: Nicobar Islands page: Denmark's presence 'ended formally on 16 October 1868' when it sold its rights to the United Kingdom, which made the islands part of British India in 1869; danish-india /ledger/16 1868-10 loss to british-raj, /ledger/17 1869 dissolve. Fix: Applied by the reviewer: counterpart -> danish-india, source -> Nicobar Islands page (added to sources[]). Validates.
- [APPLIED] `/ledger/18 and /ledger/21`: Japanese occupation of the Andaman and Nicobar Islands dated 1943-1945 at confidence 1 from the Cliopatria outline; empire-of-japan has 1942-03 to 1945-08. Evidence: Japanese occupation of the Andaman and Nicobar Islands page: 'Port Blair was occupied on the 23 March 1942'; the islands were surrendered on 15 August 1945. Fix: Applied by the reviewer: start 1943 -> 1942-03, end month 8, both confidence 3, source that page (added to sources[]). Validates.
- [APPLIED] `/wars/0`: Indian Rebellion of 1857 starts in 1857, before the Raj's start (1858-08). Evidence: Brief check 2: wars inside the life. Fix: Applied by the reviewer: from 1857 -> 1858 with a note that the 1857 phase belongs to british-empire.

Thin (for a gap-filler):
- `/ledger/19, /ledger/20`: 1944 Japanese offensive into Manipur at confidence 1 ('a reading'; the Raj page is silent). Try https://en.wikipedia.org/wiki/Battle_of_Imphal
- `/keyframe_review/10-14`: 1917, 1918, 1927, 1932 and 1938 north-east and Burma-China frontier tweaks unverified: page budget (allowed). Try https://en.wikipedia.org/wiki/North-East_Frontier_Tract
- `/ledger (Aden, Straits Settlements)`: Aden (Raj 1858-1937, on the Raj page) and the Straits Settlements (to 1867) are not written; Cliopatria does not draw them in the Raj row. Try https://en.wikipedia.org/wiki/Aden_Province
- `/identity/rulers`: No viceroy strip (the Raj page's table stops at 1884). Try https://en.wikipedia.org/wiki/List_of_governors-general_of_India

Spot checks:
- `/ledger/4` (Kingdom_of_Sikkim): confirmed: 'Under the 1861 Treaty of Tumlong, Sikkim became a British protectorate'
- `/ledger/5` (British_Raj): confirmed year: 'Nicobar Islands annexed and incorporated into India 1869' (viceroy table); counterpart corrected from the Nicobar Islands page
- `/ledger/6` (Treaty_of_Gandamak): confirmed: 'signed on 26 May 1879'; 'Jurisdiction over the Korram and Pishin valleys, the Sibi district, and the Khyber pass were transferred to the British'
- `/ledger/8` (British_rule_in_Burma): confirmed: 'British troops entered Mandalay on 28 November 1885'; province of British India 1 January 1886
- `/ledger/10` (Kingdom_of_Sikkim): confirmed: 'In 1888 the British sent a military expedition to expel Tibetan forces from Sikkim'
- `/ledger/14` (British_Raj): confirmed: capital to be moved from Calcutta to Delhi (1911 Durbar); infobox 'New Delhi (1911/1931-1947)'
- `/ledger/15` (McMahon_Line): confirmed date (maps and notes exchanged 24-25 March 1914), but the region overreaches: 'The district remained in Tibetan hands until 1951' (blocking finding)
- `/ledger/16 (was /ledger/11)` (Gilgit_Agency): mis-dated (1889 Political Agent, not occupation; lease 26 March 1935); fixed by the reviewer
- `/ledger/17` (British_rule_in_Burma): confirmed: 'The British separated Burma Province from British India on 1 April 1937'
- `/ledger/18` (British_Raj): not on page, as the author said (confidence 1); re-dated from the Japanese occupation page by the reviewer

## islamic-republic-of-pakistan: thin

Area: infobox 881913 km2 (2024), Cliopatria 875923 km2, ratio 0.99. Infobox total (current) against the 2006-2024 shapes; quoted correctly in /keyframe_review/4 and /keyframe_review/10.

Findings:
- [APPLIED] `/identity/predecessors/1/slug, /ledger/5/counterpart`: Counterpart slug 'kalat' does not exist; the Khanate of Kalat's dossier is khanate-of-kalat. Evidence: history/polities/khanate-of-kalat.json (name 'Khanate of Kalat', 1666-1955); validator warning on /ledger/5; Princely state page: Kalat 'remained independent until it was acceded on 27 March 1948'. Fix: Applied by the reviewer: kalat -> khanate-of-kalat (both places). Validates with 0 warnings.
- [APPLIED] `/ledger/1/counterpart`: Counterpart slug 'bahawalpur' does not exist; the state's dossier is bahawalpur-state. Evidence: history/polities/bahawalpur-state.json (name 'Bahawalpur State'); Princely state page: 'Bahawalpur from the Punjab Agency joined Pakistan on 5 October 1947'. Fix: Applied by the reviewer: bahawalpur -> bahawalpur-state. Validates.
- [to do] `/ledger (missing event, 1958) and /keyframe_review/0-1`: No 1958 gain of Gwadar from Oman, and the Omani enclave stays inside the 1947 and 1948-1957 land (flagged by the author). Evidence: sultanate-of-oman /ledger/24 1958-09 loss to islamic-republic-of-pakistan ('the Gwadar enclave', confidence 3). The Pakistan page does not mention it (checked). Fix: Add a 1958-09 gain from sultanate-of-oman, region {place: Gwadar, km: 20} (in the gazetteer), sourced to the Gwadar page, and subtract the same region in the 1947 correction (the 1948-1962 shape can keep it as a small in-span event, or be marked adjust).
- [to do] `/ledger/3, /ledger/4, /ledger/6`: Gains from kashmir-and-jammu dated 1947-11 and 1948-08, after that state's own end (1947-10); no mirror loss exists. Evidence: kashmir-and-jammu identity.end 1947-10 and /ledger/9 dissolve; war page: accession to India 26 October 1947. Fix: Settle with kashmir-and-jammu (see its finding): either name republic-of-india as counterpart or have kashmir-and-jammu extended to 1949-01 with loss events.
- [to do] `/ledger/0 region and /ledger/1`: Bahawalpur is counted twice: the found region (Cliopatria 1947 minus Kalat) already holds it, then /ledger/1 gains it again in October 1947; the neighbour dossiers now model Bahawalpur and Kalat as states that last to the One Unit merger (dissolve into Pakistan 1955-10) with no 1947-1948 event, while this ledger has gains in 1947-10 and 1948-03 and nothing in 1955. Evidence: bahawalpur-state /ledger/2 and khanate-of-kalat /ledger/15: 1955-10 dissolve into islamic-republic-of-pakistan (both files rewritten at 06:50 today, during this review). Fix: Subtract Bahawalpur from the found region as Kalat is subtracted; after the orchestrator settles the model, either keep the accession gains (and the neighbours add 1947/1948 losses) or turn them into vassal_start with 1955-10 gains.

Thin (for a gap-filler):
- `/ledger (1947-11)`: Accession of Hunza (3 November 1947) and Nagar (18 November 1947) to Pakistan (Gilgit-Baltistan page); hunza-and-nagar has no dossier yet. Try https://en.wikipedia.org/wiki/Gilgit-Baltistan
- `/ledger (1947-09 to 1947-11)`: Junagadh's accession to Pakistan and its annexation by India (Princely state page names it, no dates). Try https://en.wikipedia.org/wiki/Annexation_of_Junagadh
- `/ledger (1968-1969)`: Rann of Kutch dispute after the 1965 war (a tribunal award to Pakistan is to be checked on the page); /wars/1 says no border moved. Try https://en.wikipedia.org/wiki/Rann_of_Kutch
- `/ledger (1947-1948)`: Accession dates of Khairpur, Swat, Dir, Chitral, Amb, Las Bela, Makran and Kharan (flagged). Try https://en.wikipedia.org/wiki/Princely_states_of_Pakistan

Spot checks:
- `/ledger/1` (Princely_state): confirmed: 'Bahawalpur from the Punjab Agency joined Pakistan on 5 October 1947'
- `/ledger/3` (Indo-Pakistani_war_of_1947%E2%80%931948): confirmed: 'By 1 November, Gilgit-Baltistan had been annexed from the Dogra dynasty'
- `/ledger/5` (Princely_state): confirmed: 'The state remained independent until it was acceded on 27 March 1948'
- `/ledger/6` (Indo-Pakistani_war_of_1947%E2%80%931948): confirmed at confidence 2: 'On 14 August, Thapa had to surrender Skardu' (1948 from context)
- `/ledger/8` (Pakistan): confirmed: infobox 'Republic: 23 March 1956'
- `/ledger/10` (Sino-Pakistan_Agreement): confirmed: signed 2 March 1963; 'ceding its claim over 1,050 sq mi (2,730 km2) in Shaksgam'

## Cross-dossier matrix

- matched: british-ceylon 1796 found dutch-ceylon <-> dutch-ceylon 1796 dissolve. both 1796-02
- matched: british-ceylon 1815 gain kingdom-of-kandy <-> kingdom-of-kandy 1815 dissolve. kandy dissolves 1815-02 to british-ceylon; gain 1815-03
- missing: kashmir-and-jammu 1846 gain british-empire <-> british-empire None None. Hazara gained 1846 from british-empire; british-empire has no 1846 loss of Hazara (only the vassal_start of Kashmir, /ledger/68)
- matched: kashmir-and-jammu 1847 loss sikh-empire <-> sikh-empire 1847 gain. Hazara, sikh-empire /ledger/27
- missing: kashmir-and-jammu 1847 gain sikh-empire <-> sikh-empire None None. territory near Jammu given in exchange for Hazara; sikh-empire has no 1847 loss
- exception: kashmir-and-jammu 1853 loss Yasin (Gohar Aman) <-> yasin None None. no dossier; in the author's counterparts_needing_dossiers
- exception: kashmir-and-jammu 1860 gain Yasin (Gohar Aman) <-> yasin None None. no dossier; in the author's counterparts_needing_dossiers
- missing: british-empire 1846 vassal_start kashmir-and-jammu <-> kashmir-and-jammu None None. kashmir-and-jammu has no vassal_start british-empire (blocking finding); east-india-company /ledger/66 records the same relation: british-empire and east-india-company overlap
- missing: british-empire 1858 vassal_end kashmir-and-jammu <-> kashmir-and-jammu None None. same; east-india-company /ledger/98 too
- missing: british-raj 1858 vassal_start kashmir-and-jammu <-> kashmir-and-jammu None None. kashmir-and-jammu has no vassal_start british-raj (same batch)
- missing: british-raj 1947 vassal_end kashmir-and-jammu <-> kashmir-and-jammu None None. same
- matched: british-raj 1935 occupation_start kashmir-and-jammu <-> kashmir-and-jammu 1935 occupation_start. both moved from 1889 to 1935-03 by the reviewer
- matched: british-raj 1947 occupation_end kashmir-and-jammu <-> kashmir-and-jammu 1947 occupation_end. 1947-07
- exception: kashmir-and-jammu 1891 vassal_start hunza-and-nagar <-> hunza-and-nagar None None. no dossier (sa-06-x); british-raj also takes Hunza-Nagar as vassal in 1891: two overlords
- mismatch: islamic-republic-of-pakistan 1947 gain kashmir-and-jammu <-> kashmir-and-jammu None None. pakistan /ledger/3 and /ledger/4 (1947-11) and /ledger/6 (1948-08) gain from a state that ends 1947-10; kashmir has a dissolve with pakistan as successor, no loss
- matched: british-raj 1858 found british-empire <-> british-empire 1858 dissolve. Raj starts 1858-08, british-empire dissolves 1858-11 (within a year); east-india-company /ledger/100 also dissolves 1858-11 to british-raj: duplicate predecessor, for the orchestrator
- matched: mughal-empire 1858 dissolve british-raj <-> british-raj 1858 found. Raj lists mughal-empire as predecessor
- missing: british-raj 1858 vassal_start hyderabad-state <-> hyderabad-state None None. hyderabad-state has no event with british-raj (its last British event is the 1853 Berar occupation by british-empire); also /ledger/24 vassal_end 1947-08
- matched: british-raj 1861 vassal_start kingdom-of-sikkim <-> kingdom-of-sikkim 1861 vassal_start. sikkim 1861-03; vassal_end 1947 matched too
- mismatch: kingdom-of-sikkim 1861 loss british-raj <-> british-raj None None. sikkim /ledger/8 gives the Darjeeling hills to british-raj in 1861, but the Kingdom of Sikkim page has 'Darjeeling given to British India: 1835' (before the Raj): sikkim's side should be fixed (year and british-empire)
- matched: british-raj 1869 gain danish-india <-> danish-india 1868 loss. after the reviewer's counterpart fix (was nobody); danish-india 1868-10
- matched: british-raj 1879 gain emirate-of-afghanistan <-> emirate-of-afghanistan 1879 loss. 1879-05
- missing: emirate-of-afghanistan 1893 gain british-raj <-> british-raj None None. Durand Line: Asmar etc.; Raj has no 1893 loss (blocking finding)
- missing: emirate-of-afghanistan 1895 gain british-raj <-> british-raj None None. Nasrat and Bashgal; Raj has no 1895 loss
- matched: british-raj 1885 gain burma <-> burma 1885 loss. 1885-11; but british-burma /ledger/9 also gains Upper Burma from burma in 1886-01: Burma overlap flagged by the author
- mismatch: british-raj 1937 loss british-burma <-> british-burma 1937 rename. british-burma has only a 1937 rename, no gain from british-raj; depends on the Burma overlap decision
- missing: kingdom-of-bhutan 1865 loss british-raj <-> british-raj None None. Bengal Duars and Kalimpong hills (1865-11, c3) and Dewangiri; Raj has no gain
- missing: nepal 1860 gain british-raj <-> british-raj None None. Naya Muluk; Raj has no 1860 loss
- missing: tibet 1904 occupation_start british-raj <-> british-raj None None. Chumbi Valley 1904-09 to 1908-02 (tibet /ledger/27, /ledger/29); also the 1903-1904 contest
- mismatch: british-raj 1914 gain tibet <-> tibet 1914 contest_start. Raj gain of all Arunachal Pradesh 1914-03 vs tibet contest_start 1914-07 and british-raj occupation south of the Sela Pass from 1944 (tibet /ledger/39), which the Raj lacks
- missing: khanate-of-kalat 1877 loss british-raj <-> british-raj None None. Quetta and Pishin (c1); kalat rewritten at 06:50 and no longer carries the 1876-1947 vassalage
- missing: kingdom-of-manipur 1891 occupation_start british-raj <-> british-raj None None. Imphal valley 1891-04 to 1891-09 (c3); Raj has neither the occupation nor the war
- missing: gwalior-state 1861 gain british-raj <-> british-raj None None. gwalior /ledger/20-22: 1861 gain of Jhansi, 1885 gain of Gwalior fort and Morar, 1885 loss of Jhansi; internal exchanges the Raj does not record
- matched: british-raj 1942 occupation_start empire-of-japan <-> empire-of-japan 1942 occupation_start. after the reviewer's fix (was 1943, c1); end 1945-08 matched
- mismatch: kingdom-of-thailand 1942 gain british-raj <-> british-burma 1943 loss. Thailand takes the Shan States from british-raj, but Burma had left the Raj in 1937; british-burma /ledger/14-15 has the 1943 loss and 1945 gain: thailand's counterpart should be british-burma
- missing: chiangmai 1892 loss british-raj <-> british-raj None None. Trans-Salween Karenni towns; Burma was in British India in 1892, so british-raj or british-burma depending on the Burma overlap decision
- missing: kengtung 1895 dissolve british-raj <-> british-raj None None. same Burma overlap dependency
- mismatch: union-of-burma 1948 found british-raj <-> british-burma 1948 dissolve. union-of-burma names british-raj (ended 1947-08); british-burma /ledger/19 dissolves into union-of-burma: union-of-burma's counterpart should be british-burma
- matched: british-raj 1947 loss islamic-republic-of-pakistan <-> islamic-republic-of-pakistan 1947 found. 1947-08
- exception: british-raj 1947 loss republic-of-india <-> republic-of-india None None. republic-of-india not written yet (sa-06 parallel part)
- exception: british-raj 1895 vassal_start chitral <-> chitral None None. no dossier; in counterparts_needing_dossiers
- exception: british-raj 1858 vassal_start Princely states of India (paramountcy) <-> princely-states-of-india None None. generic union, no dossier; bahawalpur-state (rewritten 06:50) and kingdom-of-manipur no longer carry their 1858-1947 vassalage either
- mismatch: islamic-republic-of-pakistan 1947 gain bahawalpur-state <-> bahawalpur-state 1955 dissolve. after the reviewer's slug fix; bahawalpur-state (rewritten 06:50) has no 1947 event and dissolves into Pakistan 1955-10
- mismatch: islamic-republic-of-pakistan 1948 gain khanate-of-kalat <-> khanate-of-kalat 1955 dissolve. after the reviewer's slug fix; khanate-of-kalat (rewritten 06:50) has no 1948 event and dissolves into Pakistan 1955-10
- missing: sultanate-of-oman 1958 loss islamic-republic-of-pakistan <-> islamic-republic-of-pakistan None None. Gwadar 1958-09 (c3); pakistan has no gain
- exception: islamic-republic-of-pakistan 1963 loss people-s-republic-of-china <-> people-s-republic-of-china None None. PRC not written yet (ea-08)
- exception: islamic-republic-of-pakistan 1971 loss people-s-republic-of-bangladesh <-> people-s-republic-of-bangladesh None None. not written yet (sa-06 parallel part)

## Problems

- khanate-of-kalat, bahawalpur-state and kingdom-of-manipur were rewritten at 06:50 today while this review ran: their 1858/1876-1947 vassal events with british-raj and their 1947/1948 events with pakistan are gone; the cross-checks reflect the files as of 06:55.
- british-empire and east-india-company both cover Company India to 1858-11, both record Kashmir as vassal 1846-1858 and both dissolve into british-raj: duplicate land for the orchestrator (the Raj names british-empire).
- Burma overlap (flagged by the author): british-raj and british-burma both draw Upper Burma 1886-1937; dependent mirrors in chiangmai (1892), kengtung (1895), kingdom-of-thailand (1942/1945, should name british-burma) and union-of-burma (1948 found names british-raj, should be british-burma).
- kashmir-and-jammu end (1947-10) vs pakistan's 1947-11 and 1948-08 gains from it: needs one model across both dossiers (and republic-of-india when written).
- The author's notes say a sri-lanka dossier exists; it does not yet (sa-06 parallel part).
- WebFetch returns a model summary of each page; the quotes above are the summaries' quotations. The British Raj infobox area has no year. The Jammu and Kashmir (princely state) page has no area.
- The gazetteer resolves 'Kalat' to Qalat, Afghanistan (alt_names): the author rightly used coordinates; a Balochistan Kalat entry is needed.

## Gazetteer names needed

- Hunza (place, british-raj)
- Nagar (Gilgit-Baltistan) (place, kashmir-and-jammu)
- Chitral (place, british-raj)
- Kalat (Balochistan) (place, islamic-republic-of-pakistan)
- Hazara (region, kashmir-and-jammu)
- Kurram (region, british-raj)
- Tawang (place, british-raj)
- Kalimpong (place, british-raj)

## Counterparts needing dossiers

- Hunza and Nagar (princely states): hunza-and-nagar [1891, 1974]
- Chitral (princely state): chitral [1895, 1969]
- Yasin (Gohar Aman): yasin [1842, 1860]
- Princely states of India (generic paramountcy union): princely-states-of-india [1858, 1947]
- Aden Province (Raj dependency): colony-of-aden [1858, 1937]
