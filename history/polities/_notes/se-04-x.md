# se-04-x: notes (Modern additions, South-east Asia from the 1930s)

Run date 2026-10-25. 14 dossiers written, all of them validate with `python3 -I history/tools/validate_dossier.py --resolve` (0 errors; 4 warnings, listed below). 114 ledger events, 62 source entries. Every state is a gap-filler that Cliopatria lacks, so every one is `new_state: true`. Per-state detail (quoted sentences, region readings, confidence reasons) is in each dossier's `notes` field; this file keeps only what a reviewer or a gap-filler must act on.

## How WebFetch limited the work

- WebFetch returns a summarising model's extraction, not the raw page. Every quotation in the dossiers is the extraction's wording, and the extraction sometimes cuts off. The Vietnam War page extract stopped before 1969, so the PRG's "Vietnam War" entry rests on two control statements only.
- No page opened gives a boundary for any insurgent zone (CPB, KNU, KIO, Wa, Mong Tai Army, KMT, PRG before 1975, CGDK). Regions are therefore named provinces, township circles clipped with `intersect` to the right admin1, or the siblings' own Thai-frontier strip. All are soft certainty and confidence 2; confidence 1 is used where the page is silent (see "Placements flagged confidence 1").
- Pages that failed to load or gave nothing usable: Spring_1975_offensive (replaced by Ho_Chi_Minh_campaign), Koto_Tinggi, Operation_17_August, Mong_Yawn. The unencoded KPNLF URL failed and the percent-encoded one worked.

## Per-state notes

| Slug | Span | Events | Open items |
| --- | --- | --- | --- |
| provisional-revolutionary-government-of-the-republic-of-south-vietnam | 1960-12 to 1976-07, rebel | 21 | No page maps NLF/PRG ground for 1961-71 or the 1973 land grab; the Bến Tre, Tây Ninh, Cam Lộ and Lộc Ninh circles are my readings. Capitals run Tây Ninh, Memot (Cambodia), Tây Ninh, Lộc Ninh, Cam Lộ, then Saigon. |
| coalition-government-of-democratic-kampuchea | 1979-01 to 1993, rebel | 8 | Reuses the Thai-frontier border_band strip of people-s-republic-of-kampuchea plus Krong Pailin. Renames 1982-06 (CGDK) and 1990 (NGC). Extent of the zone, Phnom Malai, Anlong Veng and Pailin after 1989 is page-silent. |
| revolutionary-government-of-the-republic-of-indonesia | 1958-02 to 1961-09, rebel | 12 | PRRI and Permesta in one dossier. Zone identical to the contest zone in republic-of-indonesia. Koto Tinggi page failed; the capital is a Bukittinggi stand-in for "Kotto Tingi". |
| communist-party-of-burma | 1948-04 to 1989-04, rebel | 11 | Boundary of the Northeast Command, Kokang, the Mong La NDAA and the Red Flag CPB in Arakan are page-silent. Successors named: wa-state, myanmar-national-democratic-alliance-army. Pegu Yoma capital is a Bago stand-in. CPB circles are clipped to Shan State (the unclipped circles took in Chinese cells). |
| wa-state | 1989-04 to 2024, rebel | 3 | Founded 17 April 1989 out of the CPB; the 1996 gain from the Mong Tai Army has no month; Hopang and Pan Lon transferred 15 January 2024. Southern Wa area placed at Mong Hsat at confidence 1: the page gives areas (about 27,000 or 30,000 km2 body and infobox, 13,000 south) and place names but no boundary. The 2010 Wa Self-Administered Division is a status note, not an event. |
| mong-tai-army | 1985 to 1996, rebel | 7 | Area, boundary and date of the Wa occupation of its border country are page-silent. Names shan-state-national-army, which has no dossier (warning). |
| karen-national-union | 1949-01 to 2024, rebel | 7 | KNU-held ground for any earlier year is page-silent (the page gives only a share of Karen State, dated July 2025); the seven districts and the post-1995 headquarters likewise. Open contest from March 2021 (warning). Capital is a Manerplaw stand-in for Papun. |
| kachin-independence-organization | 1961-02 to 2024, rebel | 5 | Special Region 1 and the 2024 Panwa and Chipwe positions are page-silent. Open contest from June 2011 (warning). Capital is a Laiza stand-in for Pajau. |
| state-of-east-indonesia | 1946-12 to 1950-08, state | 6 | The split is dated 1950-04 and sourced to the RMS page (25 April 1950); the SEI page says only "after the cabinet formed in May 1950". Both are quoted in the dossier. The 27 December 1949 joining of the federation has no event. |
| state-of-vietnam | 1949-06 to 1955-10, state | 6 | One state with republic-of-vietnam in the pages (Bao Dai's State of Vietnam became Diem's Republic on 26 October 1955). Written as a separate dossier; its dissolve event names republic-of-vietnam as counterpart. See the merge question below. |
| arakan-army | 2024-01 to 2024, rebel | 7 | Dates for Sittwe, Kyaukphyu, Ramree, Ann, Rathedaung and Ponnagyun are page-silent. Open contest from January 2024 (warning). Capital is a Laiza stand-in for the unnamed seat. |
| kuomintang-in-burma | 1949-12 to 1961-04, family china | 8 | Repaired 2026-10-25: the spread over the Shan states is 1952 (page: 'late 1952'); the extent is still my reading. Capital is a Tachileik stand-in for Kengtung. Family key is `china` because the army is Nationalist Chinese. |
| myanmar-national-democratic-alliance-army | 1989-03 to 2024, rebel | 6 | Founded 12 March 1989. Loses Kokang in August 2009 and holds no land until it retakes Laukkai on 5 January 2024 (the dossier says so and the 2015 contest closes then); Lashio taken in early August 2024. Headquarters before 2009, the month of the 1989 ceasefire and whether fighting 2015-2023 was continuous are page-silent. Pages disagree on dates (Laukkai 5 January 2024 against "December 2023"; Lashio "early August" against 3 August). |
| republic-of-south-maluku | 1950-04 to 1963-12, rebel | 7 | Proclaimed at Ambon 25 April 1950; Ambon falls 5 November 1950; government moves to Seram in December. The end is 2 December 1963 in the infobox but "until 1962" in the body text and 1954-1962 on the Seram page; I used the infobox date. When Buru was lost is page-silent. |

## Placements flagged confidence 1

The Wa South circle at Mong Hsat, the Tachileik and Pegu capital stand-ins, the 1996 loss of the Mong Tai Army's Thai-border country to the Wa, the 1950 loss of the Taungoo area by the KNU (page silent) and the Cambodia and Burma Thai-border losses. The KMT's spread is now 1952 at confidence 2 (the page dates it; the extent is my reading). Everything else with a region is confidence 2 at most. Confidence 3 is used only where a page gave both year and land.

## Capital stand-ins (placeholder coordinates)

kuomintang-in-burma (Tachileik for Kengtung), communist-party-of-burma (Bago for the Pegu Yoma), karen-national-union (Manerplaw for Papun), revolutionary-government-of-the-republic-of-indonesia (Bukittinggi for Kotto Tingi), kachin-independence-organization (Laiza for Pajau), arakan-army (Laiza for the unnamed seat). Each is flagged in the capital event's note.

## Validator warnings (4)

- mong-tai-army: counterpart `shan-state-national-army` looks like a slug but no polity or dossier has it.
- karen-national-union, kachin-independence-organization, arakan-army: a `contest_start` against `union-of-burma` with no later `contest_end`. These are wars still running at the end of the data, so the open contest is the honest record.

## Counterpart mismatches for the gap-fillers

- people-s-republic-of-kampuchea uses `khmer-rouge` for the Thai-border zone; coalition-government-of-democratic-kampuchea mirrors it under `people-s-republic-of-kampuchea`. One side should be changed.
- union-of-burma, republic-of-indonesia, dutch-east-indies, republic-of-vietnam and french-indochina have no mirror events for the gains and losses recorded here (PRG 1972-75, KMT, KNU, KIO, CPB, Wa, MNDAA, AA, the PRRI losses, State of East Indonesia). The contest slugs are mirrored so the validator pairs them, but the counterparts' own ledgers were not edited (not in the brief).

## state-of-vietnam versus republic-of-vietnam

These are one continuous state in the pages. If a gap-filler merges them under one colour, the merge point is 26 October 1955. Not merged here because republic-of-vietnam belongs to se-04-b.

## Not written, and why

No dossier for the following, because the pages opened give no territory: National Unity Government of Myanmar and the People's Defence Force (only shares of the country, "40-50%" and "under 40%", no map), Karenni National Progressive Party (headquarters and ceasefires only), National Democratic Alliance Army / Mong La (headquarters only), New Mon State Party, Shan State Army and Shan State National Army, Ta'ang National Liberation Army, the Khmer Rouge Provisional Government of 1994-1999, the other Dutch-sponsored federal states (East Sumatra, Pasundan, East Java, South Sumatra) and the Autonomous Republic of Cochinchina. They are all listed in the report's `counterparts_needing_dossiers` or `gaps`.

## Gazetteer names needed

26 names, with hints, are in the report's `gazetteer_names_needed`. The ones that matter most: Cam Lộ, Lộc Ninh, Memot, Tomohon, Kotamobagu, Pangkham, Hopang, Mong Hsat, Homein, Kengtung, Tachileik, Manerplaw, Hpapun, Laiza, Pajau, Laukkai, Lashio, Buthidaung, Maungdaw, Thandwe, Taungup, Paletwa, Seram. Until the gazetteer has them the dossiers use coordinate circles clipped to the right admin1, which resolve now.

## Repair pass 2026-10-25 (reviewer verdict fail on four dossiers)

Backups of the four originals are in /tmp/claude-0/work/fix-se-04-x/backup/. All four validate with `--resolve` (0 errors); the only warnings are the open contests that are still running (KNU, KIO) and the missing shan-state-national-army dossier. Details and quotations are in each dossier's `notes`.

### mong-tai-army
- Changed: the 1995-07 split to the Shan State National Army and the SSNA successor land now sit at Hsipaw (40 km circle at 22.617 N, 97.283 E cut to Shan State, from the Hsipaw page), confidence 2, instead of the Ho Mong circle the MTA keeps to 1996. Page (Mong Tai Army): '8,000 fighters under the command of Colonel Yod Kan and Dae Wain retreated into the village of Hsipaw'.
- Changed: the Khun Sa page (opened this pass) gives 'Khun Sa surrendered to the Burmese government on January 5, 1996, gave up control of his army', so contest_end and dissolve carry month 1 and cite that page. It is silent on when the Wa took the Thai-border country, so ledger/4 stays confidence 1; it also says the 1985 alliance gave Khun Sa 'a 150-mile Thai-Burma border area' from Ho Mong to Mae Sai, which the two keyframe circles span (noted in keyframe 0).
- Disagreement with the reviewer's second option: no page puts MTA ground at Hsipaw, so I did not add it to a keyframe and did not move the split onto a region the keyframes hold. The split records the SSNA's base, not drawn MTA land; the Mong Tai Army page names no MTA land passing to the SSNA.

### kuomintang-in-burma
- Changed: the spread over the eastern Shan states is dated 1952 (Kuomintang_in_Burma: 'The KMT stopped concentrating their forces near the China border in late 1952' after the failed August 1952 re-entry), confidence 2; the gain region subtracts the Mong Hsat circle already held.
- Changed: keyframes are 1949 (Tachileik), 1950-1951 (Mong Hsat circle) and 1952-1961 (the Shan territory); the 1961 Tachileik-only keyframe is dropped because the page names no place taken in the 1960-61 operations ('broke the back' only), so the 1961 loss and dissolve take the shape the keyframe holds.
- Changed: capitals end at Mong Hsat (1950-1961); the infobox's Chiang Rai (1961) is in Thailand outside every shape and is no longer drawn.
- Disagreement: the reviewer asked for contest_start in 1952 (or 1953). I put it at 1950-07 with the Mong Hsat circle: the same page has the Burmese army taking Tachilek 'within weeks' of June 1950 and making 'several attempts over the next two years' to oust the KMT from Mong Hsat, which is fighting that holds ground, and the war entry already begins in 1950. The zone widens to the whole KMT country with the 1952 gain.
- Thin item left: the 1953-54 evacuation (7 November 1953 to May 1954; Li Mi's 30 May 1954 dissolution announcement) changed no border and no event type fits; it is in the 1952-1961 keyframe note.

### karen-national-union
- Changed: 2024-03 gain of Hpapun (confidence 2, 'claimed to have seized the town on 28 March 2024') and 2024-12 gain of Manerplaw (confidence 3, recaptured 17 December 2024), a 2024 keyframe of the whole of Kayin, and the 2021 keyframe now ends 2023. The Hpapun circle is at the Hpapun Township page's coordinates (18.0 N, 97.567 E; the town's own are on no page), 35 km from Manerplaw; the Manerplaw gain subtracts it.
- Changed: the Taungoo capital ends in 1949, the year the page dates ('capital in Taungoo in May 1949'); the 1949 keyframe adds a 30 km Taungoo circle with a 1949-05 gain and a 1950 loss at confidence 1 (page silent on how long Taungoo was held); Papun starts in 1950 as a bridging span. The 1975 move to Manerplaw is confidence 2.
- Not done: Insein (the page says only that the KNU lost at the Battle of Insein) and any shrinking of KNU ground from the 1970s to 1995 are page-silent, so keyframe 1950-1994 stays the whole of Kayin.

### kachin-independence-organization
- Changed: the zone is Kachin State minus circles at Myitkyina, Bhamo, Putao, Mogaung, Mohnyin (and the midpoint of the railway line) and the Chipwi-Panwa area, 70,812 km2 on the grid against 81,687 for the whole state; the full sentence is quoted ('Aside from its major towns and railway corridor, KIO/A-controlled areas in Kachin State remained virtually independent ... from the mid-1960s through 1994').
- Changed: 2024-09 gain of Chipwi and Panwa (KIO page: year only; Chipwi page: 30 September 2024 for Chipwi; confidence 2) and a 2024 keyframe. The Chipwi circle is carved out of the 1961-2023 zone so the gain is new land; for 1961-1994 the pages are silent on it.
- Disagreement: the reviewer suggested place circles. Bhamo, Putao, Mohnyin, Mogaung and Chipwi are not in the gazetteer, so they are coordinate circles from the coordinates printed on their pages (Bhamo 24.26667 N 97.23333 E; Putao 27.32583 N 97.4225 E; Mohnyin 24.78333 N 96.36667 E; Mogaung 25.30139 N 96.94167 E; Chipwi 25.88417 N 98.13194 E) so that the subtraction takes effect now. An unresolved name in a `minus` would draw the whole state.
- Panwa has no page of its own that loads ('Pangwa,_Myanmar', 'Panwa', 'Pangwa_Township' do not exist; 'Pangwa' is a Tanzanian mountain), so it is placed only by the Chipwi circle. Thin item left: what the 1994 ceasefire left the KIO (Special Region 1 and the jade mines are undated on the KIA page) and the 2011-2024 extent are page-silent.

### Gazetteer names needed after the repair
Hsipaw (22.617 N, 97.283 E), Bhamo (24.267 N, 97.233 E), Putao (27.326 N, 97.423 E), Mohnyin (24.783 N, 96.367 E), Mogaung (25.301 N, 96.942 E), Chipwi (25.884 N, 98.132 E); Panwa and Hpapun town have no coordinates on any page opened.

### Counterparts needing dossiers
shan-state-national-army (1995-2024), unchanged from the first report. The union-of-burma gains and losses of all four dossiers still have no mirror in the union-of-burma ledger.
