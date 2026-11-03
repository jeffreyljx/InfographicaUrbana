# Review of batch se-04-x (Modern additions, South-east Asia)

Reviewer run 2026-10-25. 14 dossiers, all of them new states (no Cliopatria rows). Mechanical check: every dossier validates with `--resolve` (0 errors; the 4 warnings are the ones the author listed). Spot checks used WebFetch on the pages cited, weighted toward confidence-3 events and the events that move the most land. Page budget: 2-5 pages per state (orchestrator notes section 10).

Verdict key: `fix` = the reviewer applied every finding and re-validated; `fail` = at least one blocking finding left for the author; `thin` = valid, needs a gap-filler (non-blocking findings may be listed); `pass` = nothing to change.

| slug | verdict | blocking open | applied |
| --- | --- | --- | --- |
| provisional-revolutionary-government-of-the-republic-of-south-vietnam | fix | 0 | 1 |
| state-of-vietnam | fix | 0 | 1 |
| coalition-government-of-democratic-kampuchea | thin | 0 | 0 |
| revolutionary-government-of-the-republic-of-indonesia | fix | 0 | 1 |
| state-of-east-indonesia | fix | 0 | 1 |
| republic-of-south-maluku | fix | 0 | 1 |
| communist-party-of-burma | fix | 0 | 2 |
| wa-state | pass | 0 | 0 |
| mong-tai-army | fail | 1 | 0 |
| kuomintang-in-burma | fail | 2 | 0 |
| karen-national-union | fail | 1 | 0 |
| kachin-independence-organization | fail | 2 | 0 |
| arakan-army | thin | 0 | 0 |
| myanmar-national-democratic-alliance-army | thin | 0 | 0 |

## provisional-revolutionary-government-of-the-republic-of-south-vietnam: fix

- **/ledger/12** (applied by reviewer): Confidence 3 on Đắk Lắk province, but the page names only the city. Evidence: Ho_Chi_Minh_campaign: 'capturing the city of Buôn Ma Thuột on 18 March'; no sentence names Darlac province. Fix: Confidence lowered to 2, with a reviewer note appended.
- thin, /keyframe_review/0: NLF ground for 1960-1971 is the researcher reading Tây Ninh + Bến Tre (about 5,600 km2 drawn) against "a third of the population" in NLF areas; no extent for the 1973 land grab (try https://en.wikipedia.org/wiki/War_of_the_flags)
- spot checks: /ledger/3 confirmed; /ledger/6 confirmed; /ledger/8 confirmed; /ledger/9 confirmed; /ledger/11 confirmed; /ledger/12 confirmed (date); region not named, confidence lowered; /ledger/15 confirmed; /ledger/16 confirmed; /ledger/19 confirmed
- area: infobox 173809 (1975), drawn 180020, ratio 1.04, acknowledged True. 1975 keyframe is the Cliopatria Republic of Vietnam 1966 outline (shapes.csv 180,020; grid about 150,000).

## state-of-vietnam: fix

- **/ledger/2 and /ledger/4 (new)** (applied by reviewer): french-indochina records vassal_start state-of-vietnam 1949-06 and vassal_end 1954-06 (its /ledger/45 and /ledger/48); this dossier had no mirror events. Evidence: State_of_Vietnam: state formation 14 June 1949, 'an associated state within the French Union' 1949-1954; the Matignon Treaty of 4 June 1954 'was seen as granting Vietnam independence from France'. Fix: Added vassal_start (1949-06) and vassal_end (1954-06), counterpart french-indochina, confidence 3, source State_of_Vietnam. Ledger indices after /ledger/1 shift by one, and after /ledger/3 by two.
- thin, /keyframe_review/2: The French Union evacuation of Hanoi (October 1954) and Haiphong (May 1955), and the sect armies, are page-silent (try https://en.wikipedia.org/wiki/Operation_Passage_to_Freedom)
- spot checks: /ledger/0 confirmed; /ledger/3 confirmed; /ledger/5 confirmed; /ledger/7 confirmed
- area: infobox None (None), drawn 180020, ratio None, acknowledged True. No infobox area on the State of Vietnam page. The 1954-55 keyframe uses the Republic of Vietnam 1956 outline.

## coalition-government-of-democratic-kampuchea: thin

- **/identity/capitals/0** (non-blocking, for the author or a gap-filler): The capital dot is Phnom Penh, outside every shape of this state. Evidence: Coalition_Government_of_Democratic_Kampuchea names no seat for the coalition. The only place it gives is Phnom Penh, as the seat of the rival PRK, so the dot falls inside PRK land. Fix: Use a stand-in inside the Thai-frontier strip, and Pailin from 1989-10, flagged as a stand-in. Or name the KR headquarters if a page gives one.
- **/ledger/7 and /identity/successors** (non-blocking, for the author or a gap-filler): The 1993 dissolve passes Pailin to kingdom-of-cambodia. Evidence: Pailin_province: Pailin stayed 'under their [Khmer Rouge] control long after they were defeated in 1979' and became a province 'after the surrender of the Ieng Sary faction of the Khmer Rouge in 1996'. Fix: For Pailin, make the counterpart provisional-government-of-national-union-and-national-salvation-of-cambodia (already in the author report counterparts_needing_dossiers) and add the Pailin_province page to sources. Keep kingdom-of-cambodia for the strip.
- thin, /ledger/6: Confidence-1 loss of the frontier strip in 1991-10, a bridging judgment (try https://en.wikipedia.org/wiki/Khmer_Rouge)
- thin, /keyframe_review/0: No page gives the extent of the zone (Phnom Malai, Anlong Veng, the KPNLF camps) (try https://en.wikipedia.org/wiki/Anlong_Veng)
- spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed; /ledger/7 confirmed (year); land counterpart wrong, see fixes
- area: infobox None (None), drawn None, ratio None, acknowledged True. No infobox area. The drawn strip is about 15,700 km2 on the grid.

## revolutionary-government-of-the-republic-of-indonesia: fix

- **/keyframe_review/0/note** (applied by reviewer): South Sumatra is drawn as PRRI land (Sumatera Selatan, about 90,000 km2), and the doubt about it was not flagged. Evidence: Revolutionary_Government_of_the_Republic_of_Indonesia: the page lists the South Sumatra Region but also names Barlian's Garuda Council among the unwilling parties, and the infobox puts only 'Central Sumatra province' under PRRI control in February 1958. Fix: Doubt acknowledged in the keyframe note. A gap-filler should decide whether to drop Sumatera Selatan (see thin).
- thin, /ledger/2: No event for the government recapture of Pekanbaru and Riau in March 1958 (Operation Tegas), which comes before Padang; Riau is drawn as PRRI land until 1960-07 (try https://en.wikipedia.org/wiki/Pekanbaru)
- thin, /keyframe_review/0: South Sumatra: did Barlian hold it for the PRRI? Also Permesta battle areas in Gorontalo, Central Sulawesi and North Maluku (named on the Permesta page) are not drawn (try https://en.wikipedia.org/wiki/Permesta)
- spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/4 confirmed; /ledger/6 confirmed; /ledger/7 confirmed; /ledger/8 confirmed; /ledger/9 confirmed; /ledger/11 confirmed
- area: infobox None (None), drawn None, ratio None, acknowledged True. No infobox area on either page. The 1958 keyframe is about 261,000 km2 on the grid.

## state-of-east-indonesia: fix

- **/ledger/4** (applied by reviewer): Confidence 3 on the whole of Maluku province, but the page names three islands. Evidence: Republic_of_South_Maluku: 'claimed the islands of Ambon, Buru, and Seram'. Fix: Confidence lowered to 2, with a reviewer note appended.
- spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/4 confirmed (date); region broader than page, confidence lowered; /ledger/5 confirmed
- area: infobox 349088 (1946), drawn 308538, ratio 0.88, acknowledged True. cliopatria_km2 is the grid area of the new keyframe (no Cliopatria row).

## republic-of-south-maluku: fix

- **/ledger/0 and /ledger/1** (applied by reviewer): Confidence 3 on the whole of Maluku province (Kei, Aru and Tanimbar included), but the page names three islands. Evidence: Republic_of_South_Maluku: 'claimed the islands of Ambon, Buru, and Seram'. Fix: Confidence lowered to 2 on both, with reviewer notes appended.
- thin, /ledger/3: Confidence-1 loss of Buru and the rest of the claim by 1950-12 (page-silent) (try https://en.wikipedia.org/wiki/Buru)
- thin, /keyframe_review/0: The region should be Ambon + Buru + Seram, not Maluku province (about 37,000 km2 drawn), once the gazetteer has Buru and Seram (try https://en.wikipedia.org/wiki/Republic_of_South_Maluku)
- spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/4 confirmed; /ledger/5 confirmed (infobox 2 December 1963; the body says Soumokil was captured 2 December 1962; the author flagged this)
- area: infobox None (None), drawn None, ratio None, acknowledged True. No infobox area.

## communist-party-of-burma: fix

- **/ledger/7 (was /ledger/8)** (applied by reviewer): The Kokang split to the MNDAA was dated 1989-04; the page and the MNDAA dossier (found 1989-03) give March. Evidence: Communist_Party_of_Burma: 'The defections thereby began on 12 March 1989 among the Kokang'. Fix: Month set to 3 and the event moved ahead of the Wa split (1989-04).
- **/ledger/10** (applied by reviewer): The dissolve passed the Kokang circle to wa-state as well as the Wa circle. Evidence: The split of 1989-03 had already given the Kokang circle to myanmar-national-democratic-alliance-army. Fix: Dissolve region cut to the Wa circle.
- thin, /keyframe_review/0: 1948-1967 is drawn as Bago Region only. The page names Pyinmana and the Irrawaddy Delta as party grounds, and 15,000 fighters in 1949 (try https://en.wikipedia.org/wiki/Internal_conflict_in_Myanmar)
- thin, /ledger/6: Confidence-1 capital move to Panghsang in 1975 (try https://en.wikipedia.org/wiki/Pangkham)
- spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/4 confirmed; /ledger/7 mis-dated (month); fixed; /ledger/8 confirmed; /ledger/10 confirmed (16 April 1989)
- area: infobox None (None), drawn None, ratio None, acknowledged True. No area on the page ('thousands of square miles'). Drawn on the grid: 31,000 / 54,000 / 24,000 km2.

## wa-state: pass

- thin, /ledger/1: Confidence-1 gain of the southern region dated 1996. The page gives two accounts: granted by the junta in 1989, and taken by force in the 1990s (try https://en.wikipedia.org/wiki/United_Wa_State_Army)
- spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/1 not on page (undated; honest confidence 1); /keyframe_review/1 confirmed (13,000 km2 southern region)
- area: infobox 30000 (2024), drawn 29842, ratio 0.99, acknowledged True. cliopatria_km2 is the grid area of the 1996-2023 keyframe; 2024 is about 33,100.

## mong-tai-army: fail

- **/ledger/3** (BLOCKING, for the author): The 1995 split to the Shan State National Army takes the Ho Mong headquarters circle. But the MTA keeps that same circle in the 1996 keyframe and dissolves it to union-of-burma, and the page puts the breakaway elsewhere. Evidence: Mong_Tai_Army: '8,000 fighters under the command of Colonel Yod Kan and Dae Wain retreated into the village of Hsipaw', where they renamed themselves the SSNA. Hsipaw is in northern Shan, not at Ho Mong. Fix: Give the split the SSNA's ground at Hsipaw: a circle cut to Shan State, with Hsipaw added to the gazetteer. Add that land to the 1985-1995 keyframe only if a page puts MTA ground there; otherwise give the split a region that the keyframes hold. Keep confidence 3 for the date and use 2 for the land.
- thin, /ledger/4: Confidence-1 loss of the Thai-border country to the Wa in 1996 (undated on the page) (try https://en.wikipedia.org/wiki/Khun_Sa)
- spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/3 confirmed (date); region contradicted by the page; /ledger/6 confirmed (infobox active 1985-1996)
- area: infobox None (None), drawn None, ratio None, acknowledged True. No infobox area.

## kuomintang-in-burma: fail

- **/ledger/3 and /ledger/4** (BLOCKING, for the author): The spread over the eastern Shan country is dated 1951, and the note says the page gives no date. The page dates it after late 1952. Evidence: Kuomintang_in_Burma: after the failed re-entry into China in August 1952 the KMT 'stopped concentrating their forces near the China border in late 1952' and spread across the Shan states; 'Eventually it gained control over the Shan territories between the Salween River on the west...'. Fix: Date the gain and the contest_start 1952 (or 1953). Start keyframe 1 then, and add a keyframe from 1950 for the Mong Hsat base circle of /ledger/2: keyframe 0 now shows only Tachileik.
- **/keyframe_review/2, /ledger/6, /ledger/7** (BLOCKING, for the author): Keyframe 2 (1961) shrinks to a Tachileik circle with no event, and the 1961-04 loss and dissolve then take keyframe 1's whole union, which keyframe 2 no longer holds. Evidence: Kuomintang_in_Burma: the joint Burmese-PLA operations of '1960-1961' 'broke the back' of the irregulars, then the evacuation of 31 March to 17 April 1961. Fix: Either drop keyframe 2 and end on the keyframe 1 shape, or add an early-1961 loss of the Mong Hsat circle (the 1960-61 operations) and give the 1961-04 loss and dissolve the Tachileik circle.
- **/identity/capitals/2** (non-blocking, for the author or a gap-filler): The 1961 capital is Chiang Rai, in Thailand, outside every shape. Evidence: Kuomintang_in_Burma infobox lists Chiang Rai (1961). Fix: Sourced; keep it, or end the capitals at Mong Hsat and say so in the note.
- thin, /keyframe_review/1: The 1953-54 evacuation (7 November 1953 to 7 May 1954; Li Mi dissolved the force on 30 May 1954) has no event and no change in extent (try https://en.wikipedia.org/wiki/Kuomintang_in_Burma)
- spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 mis-dated (page: late 1952); /ledger/5 confirmed; /ledger/6 confirmed
- area: infobox None (None), drawn None, ratio None, acknowledged True. No infobox area.

## karen-national-union: fail

- **/keyframe_review/2 and /ledger** (BLOCKING, for the author): Keyframe 2 (2021-2024) subtracts the 40 km Manerplaw/Hpapun circle through 2024. Its own note says the KNLA claimed Hpapun on 28 March 2024, and the KNU retook Manerplaw on 17 December 2024. Neither gain is in the ledger. Evidence: Hpapun: the KNLA 'claimed to have seized the town on 28 March 2024'. Manerplaw: 'The KNU and KNLA recaptured it on 17 December 2024'. Both pages are in sources[]. Fix: Add 2024-03 gain from union-of-burma (Hpapun, confidence 2: a claim) and 2024-12 gain (Manerplaw, confidence 3), and a 2024 keyframe of the whole of Kayin.
- **/identity/capitals/0** (non-blocking, for the author or a gap-filler): The Taungoo capital (1949-1952) lies in Bago Region, outside keyframe 0 (Kayin State). Evidence: Kawthoolei: 'the KNU set up a provisional government in Taungoo' (May 1949); the span to 1952 is a bridging guess. Fix: Add the Taungoo area to a 1949 keyframe, or end the Taungoo span when the page allows and say so.
- **/ledger/3** (non-blocking, for the author or a gap-filler): Confidence 1 on the 1975 move to Manerplaw. Evidence: Manerplaw: the camp 'was established in 1975'. Fix: Raise to 2.
- thin, /keyframe_review/0: 1949-1994 is the whole of Kayin State. The 1949 holds outside it (Insein, Taungoo) and the shrinking after the 1970s are page-silent (try https://en.wikipedia.org/wiki/Kawthoolei)
- spot checks: /ledger/4 confirmed; /ledger/5 confirmed; /ledger/6 confirmed; /keyframe_review/2/note confirmed; contradicts the keyframe shape; /ledger/3 confirmed (established 1975)
- area: infobox None (None), drawn None, ratio None, acknowledged True. No infobox area. The KNU page gives 'approximately 61% of Karen State' (15 July 2025); about 22,500 km2 is drawn.

## kachin-independence-organization: fail

- **/keyframe_review/0/correction and /ledger/0,1,2,4 regions** (BLOCKING, for the author): The whole of Kachin State (about 81,700 km2 on the grid) is drawn as KIO land for 1961-2024. The page excludes the towns and the railway, and the dossier quotes the sentence without its first clause. Evidence: Kachin_Independence_Organization: 'Aside from its major towns and railway corridor, KIO/A-controlled areas in Kachin State remained virtually independent ... from the mid-1960s through 1994'. Fix: Use Kachin minus circles at Myitkyina, Bhamo and Putao and the Myitkyina-Mogaung-Mohnyin railway corridor (place circles; Bhamo, Putao and Mohnyin need gazetteer entries). Quote the full sentence.
- **/ledger** (BLOCKING, for the author): No 2024 gains, though the keyframe note quotes them. Evidence: Kachin_Independence_Organization: 'In 2024, it took control of the towns of Panwa and Chipwe'. Fix: After the region fix, add a 2024 gain from union-of-burma (Panwa, Chipwe; confidence 2, no month) and a 2024 keyframe.
- thin, /ledger/2: What the 1994 ceasefire left the KIO (Special Region 1), and its extent in 2011-2024 (try https://en.wikipedia.org/wiki/Kachin_Independence_Army)
- spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed (month; 9 June is from the KIA page)
- area: infobox None (None), drawn 81686, ratio None, acknowledged False. No infobox area. The drawn whole state is contradicted by the page; see fixes.

## arakan-army: thin

- **/identity/capitals/0** (non-blocking, for the author or a gap-filler): The capital dot is Laiza in Kachin State, about 700 km from any 2024 AA land. The note says it only 'keeps the capital list non-empty'. Evidence: Arakan_Army infobox: headquarters 'Laiza, Kachin State (former); Rakhine State (current)'. Fix: Put a flagged stand-in inside the 2024 shape, for example Mrauk U, the first district taken.
- thin, /keyframe_review/0: Before 2024: the page says the AA 'reached a ceasefire in late 2020 after eroding the central government's control in northern Rakhine', so rural northern Rakhine may have been AA-held 2020-2023. Ann (Western Command, December 2024), Pauktaw (retaken January 2024) and the undated townships are not drawn (try https://en.wikipedia.org/wiki/Ann_Township)
- spot checks: /ledger/0 confirmed; /ledger/2 confirmed (the page puts Mrauk U on 9 February; the note says 10); /ledger/3 confirmed; /ledger/4 confirmed; /ledger/5 confirmed; /ledger/6 confirmed
- area: infobox None (None), drawn 17703, ratio None, acknowledged True. No infobox area. The drawn 2024 shape (grid) understates; the author says so.

## myanmar-national-democratic-alliance-army: thin

- **/keyframe_review/0** (non-blocking, for the author or a gap-filler): The drawn Kokang is about 1,000 km2 (4 grid cells once the circle is cut to Shan), against the 1,895 km2 the note quotes. The author compared the uncut circle (1,963 km2). Evidence: Grid resolve of the keyframe 0 correction: 4 cells, about 1,011 km2. Ratio 0.53. Fix: Widen the Laukkai circle to about 35 km, or cut it to the Kokang zone, and redo the comparison.
- thin, /ledger: The MNDAA page says 'Chinshwehaw had come fully under control of the MNDAA' on 28 October 2023, which contradicts 'holds no land until 5 January 2024'. Hsenwi and Kunlong (Operation 1027, late 2023) are missing too: add a 2023-10 gain and a 2023 keyframe (try https://en.wikipedia.org/wiki/Operation_1027)
- spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed
- area: infobox None (None), drawn 1011, ratio 0.53, acknowledged False. Against the 1,895 km2 Kokang figure the author quotes; no infobox area.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| provisional-revolutionary-government-of-the-republic-of-south-vietnam 1969 loss (republic-of-vietnam) | republic-of-vietnam None None | missing | RVN (se-04-b) records only contest_start 1961 and contest_end 1975-04 with the PRG; no gain of Bến Tre. |
| provisional-revolutionary-government-of-the-republic-of-south-vietnam 1972 gain (republic-of-vietnam) | republic-of-vietnam 1973 occupation_start | mismatch | Lộc Ninh (1972-04) and Quảng Trị/Cam Lộ (1972-05, 1972-09): the RVN and DRV dossiers model the same ground as a DRV occupation from 1973-01 (republic-of-vietnam /ledger/5, democratic-republic-of-vietnam /ledger/11), and the PRG as a PRG gain. One model should win. |
| provisional-revolutionary-government-of-the-republic-of-south-vietnam 1975 gain (republic-of-vietnam) | democratic-republic-of-vietnam 1975 gain | mismatch | Double claim: the PRG gains all of South Vietnam in 1975-04 (its /ledger/11-16), and democratic-republic-of-vietnam /ledger/12 also gains it from RVN in 1975-04; RVN has no loss to the PRG. The PRG page infobox calls the PRG a 'Satellite state of the DRV' for 1975-1976. Suggested fix: the DRV records vassal_start of the PRG in 1975-04 in place of the gain, and the PRG records vassal_start of the DRV, ending at the 1976-07 merge. |
| provisional-revolutionary-government-of-the-republic-of-south-vietnam 1976 merge (democratic-republic-of-vietnam) | democratic-republic-of-vietnam 1976 dissolve | mismatch | The DRV dissolves to the SRV in 1976-07 with no merge naming the PRG. |
| state-of-vietnam 1949 vassal_start (french-indochina) | french-indochina 1949 vassal_start | matched | Added by the reviewer to mirror french-indochina /ledger/45. |
| state-of-vietnam 1950 gain (french-indochina) | french-indochina None None | missing | The Domain of the Crown (1950-04): french-indochina has no loss to the State of Vietnam. Acceptable under the vassal model (FI stays overlord); no action needed if the orchestrator accepts the vassal pair. |
| state-of-vietnam 1954 vassal_end (french-indochina) | french-indochina 1954 vassal_end | matched | Added by the reviewer to mirror french-indochina /ledger/48. |
| state-of-vietnam 1954 loss (democratic-republic-of-vietnam) | democratic-republic-of-vietnam 1954 gain | mismatch | DRV /ledger/5 names french-indochina as the 1954-07 counterpart; this dossier names the DRV. By June 1954 the State of Vietnam was independent, so DRV should name state-of-vietnam (or both). |
| state-of-vietnam 1955 dissolve (republic-of-vietnam) | republic-of-vietnam 1955 found | matched | republic-of-vietnam starts 1955-10; the pages call them one state (author flagged). |
| coalition-government-of-democratic-kampuchea 1979 found (people-s-republic-of-kampuchea) | people-s-republic-of-kampuchea 1979 contest_start | mismatch | PRK uses the counterpart string khmer-rouge for the 1979-1991 frontier contest, but the khmer-rouge dossier ends 1979-01. PRK should name coalition-government-of-democratic-kampuchea (author flagged). |
| coalition-government-of-democratic-kampuchea 1989 gain (people-s-republic-of-kampuchea) | people-s-republic-of-kampuchea 1989 loss | mismatch | PRK /ledger/5 records the 1989-10 Pailin loss with counterpart khmer-rouge; it should be coalition-government-of-democratic-kampuchea. |
| coalition-government-of-democratic-kampuchea 1991 loss (people-s-republic-of-kampuchea) | people-s-republic-of-kampuchea 1991 contest_end | missing | PRK has only a contest_end in 1991-10, no gain. The CGDK loss is confidence 1. |
| revolutionary-government-of-the-republic-of-indonesia 1958 loss (republic-of-indonesia) | republic-of-indonesia None None | missing | The six PRRI losses (Padang 1958-04, Bukittinggi 1958-05, Manado 1958-06, Tomohon 1958-08, Kotamobagu 1959-09, Sumatra 1960-07) have no gains in republic-of-indonesia, which has only contest_start 1958-02 and contest_end 1961-09. There is also no RI loss at the 1958-02 founding. |
| state-of-east-indonesia 1946 found (dutch-east-indies) | dutch-east-indies None None | missing | dutch-east-indies (se-03) has no split, loss or vassal_start for the State of East Indonesia (1946-12); the page calls it a Dutch puppet state. |
| state-of-east-indonesia 1950 split (republic-of-south-maluku) | republic-of-south-maluku 1950 found | matched | RMS founds 1950-04 from state-of-east-indonesia. |
| state-of-east-indonesia 1950 dissolve (republic-of-indonesia) | republic-of-indonesia 1950 rename | missing | republic-of-indonesia /ledger/17 (1950-08) is a rename, with no gain or merge of East Indonesia. |
| republic-of-south-maluku 1950 loss (republic-of-indonesia) | republic-of-indonesia None None | missing | Ambon (1950-11) and the rest of the claim (1950-12): no RI gain, and no RI contest with the RMS. |
| communist-party-of-burma 1968 gain (union-of-burma) | union-of-burma None None | missing | union-of-burma (1948-2024, se-01) has no insurgency event at all: no contest, loss or gain with any batch slug. |
| communist-party-of-burma 1975 loss (union-of-burma) | union-of-burma None None | missing | See above. |
| communist-party-of-burma 1989 split (myanmar-national-democratic-alliance-army) | myanmar-national-democratic-alliance-army 1989 found | matched | Month aligned to 1989-03 by the reviewer. |
| communist-party-of-burma 1989 split (wa-state) | wa-state 1989 found | matched | 1989-04. |
| wa-state 1996 gain (mong-tai-army) | mong-tai-army 1996 loss | matched | Both confidence 1. |
| wa-state 2024 gain (union-of-burma) | union-of-burma None None | missing | Hopang and Pan Lon (15 January 2024): no loss in union-of-burma. |
| mong-tai-army 1995 split (shan-state-national-army) | None None None | exception | No dossier; listed in the author counterparts_needing_dossiers. The split region itself is wrong (see the MTA fixes). |
| karen-national-union 1995 loss (union-of-burma) | union-of-burma None None | missing | Manerplaw 1995-01: no gain in union-of-burma. |
| arakan-army 2024 gain (union-of-burma) | union-of-burma None None | missing | Five 2024 gains (Mrauk-U district, Buthidaung, Thandwe, Maungdaw, Taungup): no losses in union-of-burma. |
| kuomintang-in-burma 1950 gain (union-of-burma) | union-of-burma None None | missing | The KMT 1950-07 loss and gain, 1951 gain and 1961-04 loss: none in union-of-burma. |
| myanmar-national-democratic-alliance-army 2009 loss (union-of-burma) | union-of-burma None None | missing | Kokang 2009-08, Laukkai 2024-01 and Lashio 2024-08: none in union-of-burma. |

## Gazetteer names needed

Hsipaw (mong-tai-army), Bhamo (kachin-independence-organization), Putao (kachin-independence-organization), Mohnyin (kachin-independence-organization), Panwa (kachin-independence-organization), Chipwe (kachin-independence-organization), Chinshwehaw (myanmar-national-democratic-alliance-army), Buru (island) (republic-of-south-maluku), Seram (island) (republic-of-south-maluku)

## Counterparts needing dossiers

- Shan State National Army: `shan-state-national-army` [1995, 2024]
- Provisional Government of National Union and National Salvation of Cambodia (Khmer Rouge holdout, held Pailin to 1996): `provisional-government-of-national-union-and-national-salvation-of-cambodia` [1994, 1998]

## Problems and notes

- Reviewer-applied fixes (re-validated, 0 errors): provisional-revolutionary-government-of-the-republic-of-south-vietnam /ledger/12 confidence; state-of-vietnam vassal_start/vassal_end added (ledger indices shift); communist-party-of-burma Kokang split month and order, dissolve region; republic-of-south-maluku /ledger/0-1 confidence; state-of-east-indonesia /ledger/4 confidence; revolutionary-government-of-the-republic-of-indonesia keyframe 0 note. Backups in /tmp/claude-0/work/review-se-04-x/backup/.
- Verdict policy for this run: fail = an unapplied blocking finding (region contradicted by the page, keyframe and ledger in conflict, missing land events documented on pages the author opened, mis-dating that needs keyframe changes). Findings marked blocking:false (capitals outside the shape, a counterpart pending a dossier that does not exist yet, area comparison) do not fail a dossier on their own.
- union-of-burma (se-01) records no insurgency events, so every Burma rebel gain and loss in this batch lacks a mirror. The orchestrator should route these to the union-of-burma owner, or accept the rebel dossiers as the only record.
- PRG/DRV/RVN 1972-1976 model conflict (PRG gains against DRV occupation and gain): needs an orchestrator decision; see cross_checks.
- Neighbour dossiers in section 6 that exist (burma, dutch-east-indies, empire-of-japan, french-indochina, papua-new-guinea, sultanate-of-aceh, sultanate-of-brunei, united-states-of-america): only french-indochina and dutch-east-indies touch this batch. british-colonial-empire, british-raj, estado-novo, people-s-republic-of-bangladesh, people-s-republic-of-china and republic-of-india are not written yet (exception). Counterparts outside section 6 that were also read: union-of-burma, republic-of-vietnam, democratic-republic-of-vietnam, socialist-republic-of-vietnam, people-s-republic-of-kampuchea, khmer-rouge, kingdom-of-cambodia, republic-of-indonesia.
- MNDAA Lashio (2024-08) was not re-checked: the MNDAA page does not report the capture, and the note cites the Lashio and civil-war pages.
