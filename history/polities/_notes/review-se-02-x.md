# Review of batch se-02-x (Maritime Southeast Asia additions)

Reviewed 2026-10-19 by the Phase B adversarial reviewer. Inputs: author's report history/notes/phase-b/reports/se-02-x.json, notes history/polities/_notes/se-02-x.md, 20 dossiers, neighbour ledgers (ayutthaya-kingdom, portuguese-empire, spanish-empire, sukhothai-kingdom exist; dutch-republic and portuguese-colonies are not written yet) and the counterpart dossiers each ledger names. Machine copy: history/notes/phase-b/reviews/se-02-x.json.

## Summary

- Validator: 0 errors in all 20; 6 warnings, all 'Kutai Lama' (kutai-martadipura).
- Spot checks: 4-8 events per dossier on the cited pages (WebFetch). No fabricated or mis-dated confidence-3 event found. One confidence-3 year not on its page as claimed (negara-daha 1526, inferred from a reign table) and one confidence-3 counterpart not on the page (sultanate-of-tidore 1700 grantor): both lowered to 2 by the reviewer.
- One source URL wrong: https://en.wikipedia.org/wiki/Buayan now opens General Santos; the quoted facts are on Sultanate_of_Buayan. Replaced in the dossier.
- Two wars ran past the dossier's end (pagaruyung-kingdom Padri War, old-pahang-sultanate Acehnese invasion): trimmed to the life.
- No page gives an infobox area; no area comparison possible (no Cliopatria row).
- Vassal-mirror convention: the schema puts vassal events in the overlord's ledger; the reviewer brief asks for a mirror in the vassal's. Only sultanate-of-buayan carries its side. Listed in cross-checks, not counted against the dossiers.

Verdicts: melayu-kingdom pass, pagaruyung-kingdom fix, sultanate-of-ternate pass, sultanate-of-tidore thin, langkasuka thin, kedah-kingdom pass, old-pahang-sultanate fix, padri-movement pass, peureulak-sultanate pass, kingdom-of-aru thin, sumedang-larang thin, kutai-martadipura thin, nan-sarunai pass, negara-daha fix, luwu thin, wajo thin, siak-sultanate thin, kertabhumi-majapahit pass, sultanate-of-bacan pass, sultanate-of-buayan thin.

Reviewer edits applied (each re-validated, 0 errors 0 warnings, read back after writing): sultanate-of-buayan (URL, wikipedia title), negara-daha /ledger/4 confidence 3->2, sultanate-of-tidore /ledger/5 confidence 3->2 and note, pagaruyung-kingdom /wars/0 to 1833, old-pahang-sultanate /wars/2 to 1623.

## Per dossier

### melayu-kingdom: pass

Tried: 4 events confirmed on the page; keyframes follow the 692 merge and 1028 gain; 1028 vs srivijaya 1202 conflict is flagged by the author; Singhasari's 1290-1292 overlordship is carried by singhasari.json (vassal side not mirrored here, see cross_checks).

- Gap /ledger/3: 1286 move to Dharmasraya is confidence 1; the Melayu page links bhumi Malayu with Dharmasraya in the 1286 Padang Roco inscription and gives 'Minanga Dharmasraya Pagaruyung' as capitals, enough for confidence 2 (try https://en.wikipedia.org/wiki/Padang_Roco_Inscription)
- Spot checks: /ledger/0 confirmed on Melayu_Kingdom; /ledger/1 confirmed on Melayu_Kingdom (infobox 'Annexed by Srivijaya: 692'); /ledger/2 confirmed on Melayu_Kingdom (infobox 'Independence restored: 1028'; Srivijaya page: Sanfoqi mission of 1028 'would refer to Malayu-Jambi'); /ledger/4 confirmed on Melayu_Kingdom ('In the year 1347 ... delegated Adityawarman as the ruler of Melayu')

### pagaruyung-kingdom: fix

- Finding /wars/0/to (applied by reviewer): Padri War ran past the dossier's end (1803-1837 against an end of May 1833). Evidence: Section 2 rule: wars inside the life; the kingdom's part ends with the arrest of 2 May 1833 (Pagaruyung_Kingdom page). Fix: to set to 1833; the war's later years stay in padri-movement.json.
- Gap /ledger/1: c.1609 loss of the west coast to Aceh is confidence 1 (page: 'early 17th century'); sultanate-of-aceh.json uses the same year at confidence 1 (try https://en.wikipedia.org/wiki/Aceh_Sultanate)
- Spot checks: /ledger/0 confirmed on Pagaruyung_Kingdom; /ledger/3 confirmed on Pagaruyung_Kingdom ('expelling the Sultanate of Aceh from the coast of West Sumatra in 1666'); /ledger/5 confirmed on Padri_War; /ledger/6 confirmed on Padri_War ('On 4 March 1822 ... pushing the Padri people out of Pagaruyung'); /ledger/8 confirmed on Pagaruyung_Kingdom ('On 2 May 1833 Sultan Tunggul Alam Bagagar was arrested')

### sultanate-of-ternate: pass

Tried: 6 confidence-3 events confirmed; keyframes match the 1450 gain and 1656 loss. The 1801 occupier conflict with Tidore is listed under sultanate-of-tidore and in cross_checks.

- Gap /ledger/1: c.1450 gain of Sula and Seram is confidence 1 ('in the 1400s', Ternate page); the Sultanate of Ternate page does not date it (try https://en.wikipedia.org/wiki/Sula_Islands)
- Gap /ledger: infobox 'Vassalisation by Dutch: 1683' ('Ternate had lost its equal position with the Dutch and became a vassal') has no ledger event; the schema puts it in the overlord's dossier (dutch-republic, not written yet) (try https://en.wikipedia.org/wiki/Sultanate_of_Ternate)
- Spot checks: /ledger/2 confirmed on Sultanate_of_Ternate; /ledger/5 confirmed on Sultanate_of_Ternate; /ledger/7 confirmed on Sultanate_of_Ternate; /ledger/9 confirmed on Sultanate_of_Ternate ('The Spaniards abandoned Maluku in 1663.'); /ledger/12 confirmed on Sultanate_of_Ternate; /ledger/14 confirmed on Sultanate_of_Ternate

### sultanate-of-tidore: thin

- Finding /ledger/5/confidence (applied by reviewer): 1700 gain of East Seram at confidence 3 names the VOC (dutch-republic) as grantor, which no page says. Evidence: Sultanate_of_Tidore: 'which had been granted Tidore in 1700' (no grantor); Nuku_of_Tidore: East Seram in 1700 not on page. Fix: confidence 3 -> 2 and the note says the grantor is the researcher's reading.
- Finding /ledger/10 (NOT applied, author to do): Tidore records itself occupying Ternate 1801.6-1802 while sultanate-of-ternate.json records the British (british-empire) as occupier for the same months; one cell cannot carry two occupiers. Evidence: Sultanate_of_Tidore: 'In 1801 Ternate was captured by the British and Tidorese after a long siege'; Nuku_of_Tidore: 'Dutch defenders finally surrendered in June 1801'. sultanate-of-ternate /ledger/10-11 occupation_start/end cp british-empire 1801/1802. Fix: Pick one occupier and mirror it: either drop /ledger/10-11 here and describe Tidore's part in /wars/1 (the British held the fort), or add an occupation pair cp sultanate-of-tidore to Ternate and drop its British pair.
- Gap /ledger/3: 1606 Spanish arrival on Tidore is confidence 1 (no page dates it) (try https://en.wikipedia.org/wiki/Spanish_East_Indies)
- Gap /ledger/13: end of Nuku's occupation of Bacan (1806) is a bridge, confidence 1; Bacan page silent (try https://en.wikipedia.org/wiki/Nuku_of_Tidore)
- Gap /ledger/14: end of the Dutch hold on Tidore (1811) read from the reign table, confidence 1 (try https://en.wikipedia.org/wiki/Sultanate_of_Tidore)
- Gap /ledger/15: Papuan coast tint 'by 1849' is an upper bound, confidence 1 (try https://en.wikipedia.org/wiki/Western_New_Guinea)
- Gap /ledger: 1780 treaty: 'Tidore was turned from an ally to a vassal and thus lost its independence' (Tidore page; Nuku page has the same) is not in the ledger; schema puts it in dutch-republic (not written) (try https://en.wikipedia.org/wiki/Sultanate_of_Tidore)
- Spot checks: /ledger/1 confirmed on Sultanate_of_Tidore; /ledger/4 confirmed on Sultanate_of_Tidore ('decided to withdraw from Tidore in 1662. This was effectuated in 1663-1666.'); /ledger/5 confirmed on Sultanate_of_Tidore (year and land confirmed; grantor not on page (fixed: confidence 2)); /ledger/6 confirmed on Sultanate_of_Tidore; /ledger/7 confirmed on Nuku_of_Tidore; /ledger/9 confirmed on Nuku_of_Tidore; /ledger/10 confirmed on Nuku_of_Tidore; /ledger/12 confirmed on Nuku_of_Tidore

### langkasuka: thin

Tried: One page used against a budget of 2-5; every event is confidence 1.

- Gap /ledger/0: founding 150 is the mid-point of 'Established: 2nd century', confidence 1 (try https://en.wikipedia.org/wiki/Langkasuka)
- Gap /ledger/1: 718 loss to Srivijaya: Langkasuka page 'By the 8th century', Srivijaya page 'During the 7th century, Langkasuka ... became part of Srivijaya'; no year (try https://en.wikipedia.org/wiki/Srivijaya)
- Gap /ledger/2: 1225 regain from tambralinga: the page only has the Zhu fan zhi of 1225 describing Ling-ya-si-jia and 'In the 12th century, Langkasuka was a tributary to Srivijaya'; no page links the land to Tambralinga, and tambralinga.json has no matching loss (try https://en.wikipedia.org/wiki/Tambralinga)
- Gap /ledger/3: 1400 end (Pasai Annals c.1370; 'survived up to the 1470s' per other historians), confidence 1 (try https://en.wikipedia.org/wiki/Pattani_Kingdom)
- Spot checks: /ledger/0 confirmed on Langkasuka; /ledger/1 confirmed on Langkasuka (century only, honest at confidence 1); /ledger/2 confirmed on Langkasuka (1225 Zhu fan zhi confirmed; Tambralinga counterpart not on page (confidence 1)); /ledger/3 confirmed on Langkasuka

### kedah-kingdom: pass

Tried: 5 events checked on Kedah_Sultanate and Srivijaya; the 1026-1135 conflict sits in srivijaya.json and sultanate-of-kedah.json (cross_checks).

- Gap /ledger/0: 330 is the infobox label 'Old Kedah (330-1136)' (Kedah_Sultanate); could be confidence 2 (try https://en.wikipedia.org/wiki/Kedah_Sultanate)
- Gap /ledger/3: 1026 independence is a reading of 'Kedah fell outside the influence of Sanfoqi during the 11th century' (Srivijaya page), confidence 1; conflicts with srivijaya.json's 1139 loss to sultanate-of-kedah (author flagged) (try https://en.wikipedia.org/wiki/Chola_invasion_of_Srivijaya)
- Spot checks: /ledger/0 confirmed on Kedah_Sultanate; /ledger/1 confirmed on Kedah_Sultanate ('In 634 CE, a new kingdom was formed in Kedah'); /ledger/2 confirmed on Srivijaya (infobox 'Conquest of Kedah: c. 682-685'); /ledger/3 confirmed on Srivijaya (11th century, honest at confidence 1); /ledger/4 confirmed on Kedah_Sultanate (1136 and the page's 'unlikely' both quoted honestly)

### old-pahang-sultanate: fix

Tried: Malacca's vassalage 1470-1511 (infobox) is carried by sultanate-of-malacca.json /ledger/6 and /ledger/14; not mirrored here (cross_checks).

- Finding /wars/2/to (applied by reviewer): 'Acehnese invasion of Pahang' ran to 1641, past the dossier's end in 1623. Evidence: Section 2 rule: wars inside the life; the dossier ends with the 1623 union with Johor (Pahang_Sultanate infobox 'Union with Johor: 1623'). Fix: to set to 1623; the 1629-1635 resistance and Aceh's 1641 abandonment of its claim belong to sultanate-of-johor/sultanate-of-aceh.
- Gap /ledger/4: 1617 contest_end is a same-year bridge (confidence 1); the page has Pahang ousting the Acehnese 1629-1635 and Aceh abandoning its claim in 1641, i.e. an Acehnese hold 1617-1623 inside this life (try https://en.wikipedia.org/wiki/Pahang_Sultanate)
- Spot checks: /ledger/0 confirmed on Pahang_Sultanate; /ledger/1 confirmed on Pahang_Sultanate ('In September 1612, the Johor army overran the suburbs of Pekan'); /ledger/2 confirmed on Pahang_Sultanate; /ledger/3 confirmed on Pahang_Sultanate; /ledger/5 confirmed on Pahang_Sultanate

### padri-movement: pass

Tried: type rebel correct; all dated events confirmed; pairs with pagaruyung-kingdom match; the government side (Pagaruyung) carries the 1803-1833 contest as the rule for rebels asks.

- Spot checks: /ledger/1 confirmed on Padri_War; /ledger/2 confirmed on Padri_War ('in April 1821, Dutch troops attacked Simawang and Sulit Air'); /ledger/3 confirmed on Padri_War; /ledger/5 confirmed on Padri_War; /ledger/6 confirmed on Padri_War ('on 16 August 1837, Fort Bonjol was completely conquered')

### peureulak-sultanate: pass

- Gap /ledger/2: 988 end of Perlak Pesisir (merge) is confidence 1; who held the coast is not on the page (try https://en.wikipedia.org/wiki/Peureulak_Sultanate)
- Spot checks: /ledger/0 confirmed on Peureulak_Sultanate ('1 Muharram 225 H (840 AD)'); /ledger/1 confirmed on Peureulak_Sultanate; /ledger/3 confirmed on Peureulak_Sultanate; /ledger/4 confirmed on Peureulak_Sultanate; /ledger/5 confirmed on Peureulak_Sultanate

### kingdom-of-aru: thin

- Gap /ledger/1: 1539 loss of Kota Rentang is 'probably' on the page (confidence 1); sultanate-of-aceh.json has no matching gain (try https://en.wikipedia.org/wiki/Alauddin_al-Qahhar)
- Gap /ledger/2: capital move dated only 'early 16th century' (try https://en.wikipedia.org/wiki/Aru_Kingdom)
- Gap /ledger/4: 1564 contest closed the same year (bridge) (try https://en.wikipedia.org/wiki/Ottoman_expedition_to_Aceh)
- Gap /wars/1: 1339 Majapahit expedition 'did manage to gain control of Haru and Pane' (Aru page) has no vassal event here or in majapahit.json; the Majapahit page is silent (try https://en.wikipedia.org/wiki/Nagarakretagama)
- Spot checks: /ledger/0 confirmed on Aru_Kingdom (infobox 'Established 1225'); /ledger/1 confirmed on Aru_Kingdom ('probably took place in 1539'); /ledger/3 confirmed on Aru_Kingdom; /ledger/5 confirmed on Aru_Kingdom ('In 1613 ... Iskandar Muda of Aceh, strike a final blow')

### sumedang-larang: thin

- Gap /identity/start: The page's infobox has 'Sumedang Larang became an independent state preceded the fall of Sunda Kingdom: 1529' and the text 'founded in 721 AD by Prabu Tajimalela'; Geusan Ulun was crowned in 1578. The dossier starts at the 1585 separation from Cirebon and neither the notes nor the dossier discuss 1529 or 721 (unflagged). Decide whether the state's life starts earlier as a Sunda/Cirebon vassal, or say why not. (try https://en.wikipedia.org/wiki/Sunda_Kingdom)
- Gap /ledger/1: mataram-sultanate.json has no 1620 gain; its first Sumedang event is a 1631 vassal_start of 'Sumedang and Ukur (Priangan)' (try https://en.wikipedia.org/wiki/Mataram_Sultanate)
- Spot checks: /ledger/0 confirmed on Sumedang_Larang_Kingdom ('in 1585 declared itself a sovereign state and separated from Cirebon'); /ledger/1 confirmed on Sumedang_Larang_Kingdom (infobox 'joined the Mataram Sultanate: 1620')

### kutai-martadipura: thin

- Gap /keyframe_review/0: One disc for 399-1635 with no event in 1,236 years; one page used (budget 2-5). Majapahit's 1362-1406 tributary string 'Kalimantan principalities (Negara Dipa, Tanjungpura, Kutai)' is not mirrored (try https://en.wikipedia.org/wiki/Kutai)
- Gap /ledger/0/region: 'Kutai Lama' is not in the gazetteer (6 resolve warnings) (try https://en.wikipedia.org/wiki/Kutai_Kartanegara_Sultanate)
- Spot checks: /ledger/0 confirmed on Kutai_Martapura_Kingdom ('(399-1635)'; script dated 'to the last half the 4th century'); /ledger/1 confirmed on Kutai_Martapura_Kingdom ('Aji Pangeran Sinum Panji Mendapa, who ruled 1635-1650, was able to conquer')

### nan-sarunai: pass

- Gap /ledger/1: Majapahit page dates the final battle to December 1362 ('the second battle happened in December 1362'); a month could be added; majapahit.json's contest 1355-1362 has no mirror here and no gain on its side (try https://en.wikipedia.org/wiki/Majapahit)
- Spot checks: /ledger/0 confirmed on Nan_Sarunai (infobox 'Established: 1309'); /ledger/1 confirmed on Nan_Sarunai ('the kingdom fell in 1362 CE'; infobox 1389 / vassal 1354-1389 conflict flagged by the author)

### negara-daha: fix

- Finding /ledger/4/confidence (applied by reviewer): 1526 loss to sultanate-of-banjar at confidence 3, but the Negara Daha page gives no end year. Evidence: Negara_Daha: 'Maharaja Tumenggung, 1520-1526'; 'End of Daha in 1526: not on page' (the year comes from the last reign and the banjar dossier). Fix: confidence 3 -> 2, with the reason in the note.
- Gap /ledger/3: 1478 spread over Kalimantan Selatan and Kotawaringin is confidence 1 (territories listed without dates) (try https://en.wikipedia.org/wiki/Banjar_Sultanate)
- Spot checks: /ledger/1 confirmed on Negara_Daha; /ledger/2 confirmed on Negara_Daha (capital moved to Muara Hulak, port Muara Bahan); /ledger/3 confirmed on Negara_Daha (territory list confirmed, undated); /ledger/4 confirmed on Negara_Daha (note is honest that the page gives no end date; the year is the end of the last reign (1520-1526); confidence lowered 3 -> 2)

### luwu: thin

- Gap /ledger/3: 1905 end is confidence 1, but South_Sulawesi_expeditions_of_1905 says 'The chief targets of the expeditions were the most powerful south Sulawesi kingdoms of Bone, Luwu and Wajo'; add that page to sources and raise to 2 (try https://en.wikipedia.org/wiki/South_Sulawesi_expeditions_of_1905)
- Gap /identity/rulers: ruler strip omitted though the page lists rulers (Dewaraja c.1495-1520, Andi Kambo 1901-1935 ...) (try https://en.wikipedia.org/wiki/Kingdom_of_Luwu)
- Gap /ledger: Wajo page calls Luwu 'Wajoq's probable overlord' (undated); Luwu's 16th-century eclipse by the southern kingdoms is undated (try https://en.wikipedia.org/wiki/Sultanate_of_Bone)
- Spot checks: /ledger/0 confirmed on Kingdom_of_Luwu; /ledger/1 confirmed on Kingdom_of_Luwu ('On 4 or 5 February 1605'); /ledger/2 confirmed on Kingdom_of_Luwu ('Around 1620, Malangke was abandoned'); /ledger/3 confirmed on South_Sulawesi_expeditions_of_1905 (Luwu named as a 1905 target; no Luwu date)

### wajo: thin

- Gap /ledger: The page the author opened dates the fall of the capital: 'the walled capital city of Tosora fell to the Bone-led forces in December 1670'; the notes and report wrongly call the 1670 fall undated. Add an occupation or contest pair with sultanate-of-bone (1670.12), and mirror it in sultanate-of-bone.json (try https://en.wikipedia.org/wiki/Wajo_Kingdom)
- Gap /ledger: 18th-century peak: 'briefly became the hegemon of South Sulawesi' under La Maddukelleng, arung matoa 1736-1754 (dated, no land named) (try https://en.wikipedia.org/wiki/La_Maddukelleng)
- Gap /ledger/3: 1905 end is confidence 1; South_Sulawesi_expeditions_of_1905 names Wajo among the chief targets (raise to 2 with that source) (try https://en.wikipedia.org/wiki/South_Sulawesi_expeditions_of_1905)
- Gap /ledger/2: 1610 contest closed the same year (bridge); sultanate-of-gowa.json has no Wajo event (try https://en.wikipedia.org/wiki/Sultanate_of_Gowa)
- Spot checks: /ledger/0 confirmed on Wajo_Kingdom; /ledger/1 confirmed on Wajo_Kingdom ('forcing Soppeng to embrace Islam in 1609, Wajoq in 1610'); /ledger/3 confirmed on Wajo_Kingdom ('early 20th century', no year (honest at confidence 1))

### siak-sultanate: thin

- Gap /keyframe_review/0: The page gives a peak extent, 'the entire northeast coast of Sumatra to the sultanate of Deli', and the 19th-century Dutch treaties that 'reduced their area of state influence to the Siak River' (undated); the single 90 km disc for 1722-1946 explains neither (try https://en.wikipedia.org/wiki/Deli_Sultanate)
- Gap /ledger/0: sultanate-of-johor.json has no 1722 loss to Siak and keeps mainland Riau to 1824 (author flagged) (try https://en.wikipedia.org/wiki/Raja_Kecil)
- Spot checks: /ledger/0 confirmed on Siak_Sultanate ('founded by Sultan Abdul Jalil Rahmat Shah in 1722'); /ledger/1 confirmed on Siak_Sultanate ('ceded his kingdom to the Republic of Indonesia in 1946')

### kertabhumi-majapahit: pass

Tried: type rebel correct; the government side (majapahit.json) carries the 1468-1478 contest; only its counterpart string differs (cross_checks).

- Spot checks: /ledger/0 confirmed on Majapahit ('In 1468 Prince Kertabhumi rebelled against Singhawikramawardhana'); /ledger/1 confirmed on Majapahit ('1478 ... Sudarma Wisuta war ... breached Trowulan defences')

### sultanate-of-bacan: pass

- Gap /ledger/5: end of Nuku's occupation (1806) is a bridge, confidence 1; page: 'The war nevertheless led to widespread destruction on the Bacan Islands' (try https://en.wikipedia.org/wiki/Nuku_of_Tidore)
- Gap /ledger/2: 1609 contest closed the same year (bridge); infobox 'Vassalisation by Dutch: 1609' belongs to dutch-republic (not written) (try https://en.wikipedia.org/wiki/Sultanate_of_Bacan)
- Spot checks: /ledger/0 confirmed on Sultanate_of_Bacan; /ledger/1 confirmed on Sultanate_of_Bacan; /ledger/3 confirmed on Sultanate_of_Bacan ('sold the Obi Islands to the VOC for 800 Reals'); /ledger/4 confirmed on Sultanate_of_Bacan

### sultanate-of-buayan: thin

- Finding /sources/0/url and every source field; /identity/wikipedia (applied by reviewer): The cited page https://en.wikipedia.org/wiki/Buayan now opens 'General Santos' and says none of what the notes quote; the quoted text is on Sultanate_of_Buayan. Evidence: WebFetch of /wiki/Buayan: title 'General Santos', 'Datu Mamu ... Malala: not on page'; /wiki/Sultanate_of_Buayan: 'Established by Datu Mamu: c.1350', '10 March 1887', 'Battle of the Malala River on 22 October 1905'. Fix: URL replaced by https://en.wikipedia.org/wiki/Sultanate_of_Buayan (12 places), title and identity.wikipedia set to 'Sultanate of Buayan'; validator 0 errors 0 warnings.
- Finding /identity/capitals (NOT applied, author to do): Capitals end in 1860 although the life runs to 1905. Evidence: Infobox: 'Buayan (1350-c.1860) Bacat (c.1860-1872; 1875-1899) Kudarangan (1872-1875) Tinungkup (1899-1905)'; rule: capitals contiguous over the life. Fix: Add Bacat, Kudarangan and Tinungkup with approximate coordinates (Cotabato valley) or say why not.
- Gap /ledger/1: 1619-1671 vassalage under Maguindanao is confidence 1 (page: 'faced a decline', 'heavily influenced') (try https://en.wikipedia.org/wiki/Muhammad_Kudarat)
- Gap /ledger/4: 1898 end of Spanish vassalage is page-silent, confidence 1 (try https://en.wikipedia.org/wiki/Datu_Uto)
- Spot checks: /ledger/0 confirmed on Sultanate_of_Buayan (confirmed on Sultanate_of_Buayan; not on the cited /wiki/Buayan); /ledger/1 confirmed on Sultanate_of_Buayan; /ledger/3 confirmed on Sultanate_of_Buayan ('signed on 10 March 1887'; 'Buayan officially became a vassal of Spain'); /ledger/5 confirmed on Sultanate_of_Buayan ('Battle of the Malala River on 22 October 1905')

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| melayu-kingdom 692 merge cp srivijaya | srivijaya 692 merge | matched |  |
| melayu-kingdom 1028 gain cp srivijaya | srivijaya 1202 loss | mismatch | 174 years apart; the Srivijaya page supports both ('after 1025 the term Sanfoqi referred to the Malayu Dharmasraya kingdom'; 'Jambi became independent from Sanfoqi's influence in the early 13th century'). Author flagged. Route to srivijaya's owner (se-02 Cliopatria part). |
| singhasari 1290 vassal_start cp melayu-kingdom | - | mismatch | singhasari.json /ledger/4 (and vassal_end 1292) has Melayu as vassal; melayu-kingdom carries no vassal-side event. Schema puts vassal events in the overlord's ledger, the reviewer brief expects both sides: orchestrator to settle the convention (sultanate-of-buayan carries its side, the rest of this batch does not). |
| melayu-kingdom 1347 dissolve cp pagaruyung-kingdom | pagaruyung-kingdom 1347 found | matched |  |
| pagaruyung-kingdom 1609 loss cp sultanate-of-aceh | sultanate-of-aceh 1609 gain | matched | both confidence 1 |
| sultanate-of-aceh 1609 vassal_start cp pagaruyung-kingdom | - | mismatch | Aceh /ledger/9 and /ledger/25 (vassal 1609-1666) not mirrored in pagaruyung-kingdom, which has a contest 1665-1666 instead; same convention question as singhasari/melayu. |
| pagaruyung-kingdom 1815 occupation_start cp padri-movement | padri-movement 1815 occupation_start | matched |  |
| pagaruyung-kingdom 1822 occupation_end cp padri-movement | padri-movement 1822 occupation_end | matched | both March 1822 |
| pagaruyung-kingdom 1833 loss cp dutch-east-indies | - | exception | dutch-east-indies.json not written yet |
| majapahit 1352 vassal_start cp Sumatran principalities (Jambi-Melayu, Palembang, Minangkabau) | - | mismatch | majapahit.json uses one string for Melayu/Minangkabau; pagaruyung-kingdom (1347-1833) has no vassal-side event for 1352-1406. Route to majapahit's owner (se-02) to use the slug pagaruyung-kingdom. |
| sultanate-of-ternate 1522 occupation_start cp portuguese-empire | portuguese-empire | missing | portuguese-empire.json (am-06, written) has no Ternate fort 1522-1575; only a 1529 Zaragoza gain of the Moluccas |
| sultanate-of-ternate 1606 occupation_start cp spanish-empire | spanish-empire | missing | spanish-empire.json (am-06) has no Ternate/Tidore occupation 1606-1663/1666 |
| sultanate-of-ternate 1656 loss cp dutch-republic | - | exception | dutch-republic (eu-09) not written yet |
| sultanate-of-ternate 1801 occupation_start cp british-empire | sultanate-of-tidore 1801 occupation_start | mismatch | Ternate names the British as occupier; Tidore /ledger/10-11 names itself occupier of Ternate (cp sultanate-of-ternate) for June 1801-1802. One occupier per cell: author to choose (finding under sultanate-of-tidore). |
| sultanate-of-ternate 1810 occupation_start cp british-empire | - | exception | british-empire.json not written yet |
| sultanate-of-ternate 1914 loss cp dutch-east-indies | - | exception | not written yet |
| sultanate-of-tidore 1578 occupation_start cp portuguese-empire | portuguese-empire | missing | no Tidore fort 1578-1605 in portuguese-empire.json |
| sultanate-of-tidore 1606 occupation_start cp spanish-empire | spanish-empire | missing | no Tidore event in spanish-empire.json |
| sultanate-of-tidore 1700 gain cp dutch-republic | - | exception | dutch-republic not written; grantor not on page (confidence lowered) |
| sultanate-of-tidore 1768 loss cp dutch-republic | - | exception | dutch-republic not written |
| sultanate-of-tidore 1780 contest_start cp Nuku's rebel Tidore | - | exception | listed in the author's counterparts_needing_dossiers (nuku-rebellion) |
| sultanate-of-tidore 1797 occupation_start cp sultanate-of-bacan | sultanate-of-bacan 1797 occupation_start | matched | ends 1806 on both sides (both confidence 1) |
| sultanate-of-tidore 1806 occupation_start cp dutch-east-indies | - | exception | not written |
| langkasuka 718 loss cp srivijaya | srivijaya 718 gain | matched | both confidence 1 (Cliopatria's year) |
| langkasuka 1225 gain cp tambralinga | tambralinga | missing | tambralinga.json (150-1277) has no loss of the Pattani basin; srivijaya.json gives 'the peninsula north of Kedah' to tambralinga in 1139 |
| langkasuka 1400 dissolve cp patani-kingdom | patani-kingdom 1400 found | matched |  |
| kedah-kingdom 685 loss cp srivijaya | srivijaya 685 gain | matched | srivijaya.json uses the string 'Kedah (Kadaram), pre-1139' instead of the slug kedah-kingdom |
| kedah-kingdom 1026 gain cp srivijaya | srivijaya 1139 loss | mismatch | srivijaya.json loses Kedah to sultanate-of-kedah in 1139 (confidence 1, Cliopatria's year); kedah-kingdom regains it in 1026 (confidence 1). Author flagged. |
| kedah-kingdom 1136 dissolve cp sultanate-of-kedah | sultanate-of-kedah 1136 found | mismatch | sultanate-of-kedah /ledger/0 founds with counterpart srivijaya, not kedah-kingdom (its predecessor list names kedah-kingdom) |
| old-pahang-sultanate 1470 found cp sultanate-of-malacca | sultanate-of-malacca 1470 loss | matched | Malacca also has vassal_start 1470 / vassal_end 1511 cp old-pahang-sultanate (infobox 'Vassal state of the Malacca Empire (1470-1511)'), not mirrored on the Pahang side (convention question) |
| old-pahang-sultanate 1612 contest_start cp sultanate-of-johor | sultanate-of-johor 1612 contest_start | mismatch | years agree; Johor uses counterpart 'pahang-sultanate' (the 1853-1889 state's slug) instead of old-pahang-sultanate |
| old-pahang-sultanate 1617 contest_start cp sultanate-of-aceh | sultanate-of-aceh 1617 contest_start | mismatch | years agree; Aceh uses the string 'Pahang Sultanate' |
| old-pahang-sultanate 1623 loss cp sultanate-of-johor | sultanate-of-johor 1623 gain | mismatch | years agree; counterpart string 'pahang-sultanate' in Johor |
| padri-movement 1821 contest_start cp dutch-east-indies | - | exception | not written |
| peureulak-sultanate 988 contest_start cp srivijaya | srivijaya | missing | srivijaya.json has no Perlak contest 988-1006 (Peureulak page: 'continued the struggle against Sriwijaya until 1006') |
| peureulak-sultanate 1292 loss cp samudera-pasai-sultanate | samudera-pasai-sultanate 1292 gain | matched |  |
| kingdom-of-aru 1539 loss cp sultanate-of-aceh | sultanate-of-aceh 1539 gain | mismatch | Aceh's 1539 gain is the Batak country with counterpart nobody; no loss of Kota Rentang from Aru |
| kingdom-of-aru 1564 contest_start cp sultanate-of-aceh | sultanate-of-aceh | missing | no 1564 Aru contest in sultanate-of-aceh.json |
| kingdom-of-aru 1613 loss cp sultanate-of-aceh | sultanate-of-aceh 1613 gain | mismatch | years agree; Aceh uses the string 'Aru' (and 'Deli' for 1612, 1669) instead of the slug kingdom-of-aru |
| kingdom-of-aru 1339 vassal_start cp majapahit | majapahit | missing | Aru page: 1339 'the Javanese expedition did manage to gain control of Haru and Pane'; neither dossier carries a vassal event (Aru has only /wars/1) |
| sumedang-larang 1585 found cp sultanate-of-cirebon | sultanate-of-cirebon | missing | sultanate-of-cirebon.json has no 1585 loss of Sumedang |
| sumedang-larang 1620 loss cp mataram-sultanate | mataram-sultanate 1631 vassal_start | mismatch | Mataram's first Sumedang event is a 1631 vassal_start of 'Sumedang and Ukur (Priangan)'; no 1620 gain |
| kutai-martadipura 1635 loss cp kutai-kingdom | kutai-kingdom 1635 gain | matched |  |
| nan-sarunai 1362 loss cp majapahit | majapahit 1362 contest_end | mismatch | majapahit.json has the 1355-1362 contest (cp nan-sarunai) but no gain; nan-sarunai has no contest pair mirroring it. Author flagged. |
| negara-daha 1380 found cp majapahit | majapahit 1362 vassal_start | mismatch | majapahit.json /ledger/9 tributary 'Kalimantan principalities (Negara Dipa, Tanjungpura, Kutai)' starts 1362, before Negara Dipa's 1380 founding, and uses a string |
| negara-daha 1526 loss cp sultanate-of-banjar | sultanate-of-banjar 1526 found | matched |  |
| luwu 1905 loss cp dutch-east-indies | - | exception | not written |
| wajo 1610 contest_start cp sultanate-of-gowa | sultanate-of-gowa | missing | Gowa has Bone 1611 but no Wajo 1610 (author flagged) |
| wajo 1670 occupation_start cp sultanate-of-bone | - | missing | Wajo_Kingdom: 'Tosora fell to the Bone-led forces in December 1670'; in neither dossier |
| siak-sultanate 1722 found cp sultanate-of-johor | sultanate-of-johor | missing | Johor /ledger/20 1722 is a loss to sultanate-of-terengganu; no loss to Siak, mainland Riau kept to 1824 (author flagged). sultanate-of-malacca's 'Siak' (1477-1511) is a different, earlier polity |
| siak-sultanate 1946 loss cp republic-of-indonesia | - | exception | republic-of-indonesia.json not written yet |
| kertabhumi-majapahit 1468 found cp majapahit | majapahit 1468 contest_start | mismatch | years agree; majapahit.json uses the string 'Kertabhumi (rebel Majapahit at Trowulan)', not the slug kertabhumi-majapahit |
| kertabhumi-majapahit 1478 loss cp majapahit | majapahit 1478 contest_end | mismatch | as above (string only) |
| sultanate-of-bacan 1609 contest_start cp dutch-republic | - | exception | dutch-republic not written; co-invader Ternate (Mudafar Syah I) has no 1609 Bacan event in sultanate-of-ternate.json (minor) |
| sultanate-of-bacan 1682 loss cp dutch-republic | - | exception | not written |
| sultanate-of-buayan 1619 vassal_start cp sultanate-of-maguindanao | sultanate-of-maguindanao 1619 vassal_start | matched | 1619-1671 on both sides, both confidence 1; Maguindanao uses the string 'Buayan (rival sultanate)' instead of the slug |
| sultanate-of-buayan 1887 vassal_start cp spanish-empire | spanish-empire | missing | no Buayan event in spanish-empire.json |
| sultanate-of-buayan 1905 loss cp united-states-of-america | united-states-of-america | missing | no Buayan/Mindanao event 1898-1914 in united-states-of-america.json |

## Gazetteer names needed

- Kutai Lama (place, Indonesia; kutai-martadipura). The author's report lists 30 more names that would turn coordinate discs into named places; none of them is an unresolved name in the dossiers.

## Counterparts needing dossiers

- Nuku's rebel Tidore (nuku-rebellion, [1780, 1797])
- Kiliman (kiliman, [None, 1350])
- Soppeng (soppeng, [None, None])
- Sultanate of Jailolo (sultanate-of-jailolo, [None, None])

## Problems

- https://en.wikipedia.org/wiki/Buayan now opens General Santos; the sultanate article is Sultanate_of_Buayan (fixed in the dossier).
- Vassal-mirror convention: the schema puts vassal_start/vassal_end in the overlord's ledger with the vassal as counterpart, while the reviewer brief expects a mirror in the vassal's ledger too; only sultanate-of-buayan carries its own side. Listed as mismatches in cross_checks (Singhasari-Melayu, Aceh-Pagaruyung, Malacca-Pahang, Majapahit strings) without counting against the dossiers; the orchestrator should settle it.
- Counterpart strings in other groups' dossiers do not use this batch's slugs: majapahit ('Kertabhumi (rebel Majapahit at Trowulan)', 'Sumatran principalities ...', 'Kalimantan principalities ...'), sultanate-of-aceh ('Aru', 'Deli', 'Pahang Sultanate'), sultanate-of-johor ('pahang-sultanate'), srivijaya ('Kedah (Kadaram), pre-1139'), sultanate-of-maguindanao ('Buayan (rival sultanate)').
- dutch-republic, dutch-east-indies, british-empire, portuguese-colonies and republic-of-indonesia dossiers do not exist yet; their events here are exceptions.
- No page opened for this batch gives an infobox area; area_check is null for all 20 dossiers (no Cliopatria row to compare).
