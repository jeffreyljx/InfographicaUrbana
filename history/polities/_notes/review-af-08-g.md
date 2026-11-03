# Review of af-08-g (Partition and independence, part g)

Reviewer run of 2026-10-24. Eight dossiers: mali-federation, republic-of-cameroon, togo, british-east-africa, burkina-faso, central-african-republic, azawad, seleka. Validator with --resolve: 0 errors, 0 warnings for all eight. Pages opened by the reviewer (en.wikipedia.org): Mali Federation, Mali, Azawad, Agacher Strip War, Cameroon, British Cameroons, Bakassi, Togo, Decolonisation of Africa, East Africa Protectorate, Burkina Faso, Central African Republic, Central African Republic Civil War. No dossier was edited by the reviewer. Machine copy: history/notes/phase-b/reviews/af-08-g.json.

## Verdicts

| slug | verdict | why, in one line |
| --- | --- | --- |
| mali-federation | thin | Every spot check confirmed; the 1974 Agacher conflict and everything after February 2013 (Kidal; ISGS-held land 2022-2023 on the Mali page) are missing |
| republic-of-cameroon | pass | Every spot check confirmed; Bakassi adjust verified in the geometry; the Nigeria side lacks Bakassi (cross-check) |
| togo | pass | One event, confirmed; no border change on the page |
| british-east-africa | fail | The 1961 polygon also holds Zanzibar, Pemba, Mafia, Socotra and the Seychelles: wrong keyframe corrections for 1962-1967 and a spurious 1968 gain |
| burkina-faso | thin | Every spot check confirmed; the 1974 conflict is missing (the page dates it), and so is the insurgency's held territory |
| central-african-republic | fail | No event for the February 2021 government recapture, which the dossier's own note quotes; 62 percent of the country drawn rebel-held to 2024 |
| azawad | pass | Declaration, renunciation, capitals and areas confirmed |
| seleka | fail | The 2014-2025 keyframe and capital Bria to 2025 contradict the February 2021 recapture; the 13 Sep 2013 disbanding is not recorded |

## british-east-africa (fail)

What holds: all ten independence losses match the Decolonisation of Africa tables (Uganda 9 Oct 1962, Kenya 12 Dec 1963, Malawi 6 Jul 1964, Zambia 24 Oct 1964, Gambia 18 Feb 1965, Rhodesia UDI 11 Nov 1965, Botswana 30 Sep 1966, Lesotho 4 Oct 1966, Swaziland 6 Sep 1968, Seychelles 29 Jun 1976). Reading the row as the remainder of British Africa is sound, and the area mismatch with the East Africa Protectorate (696,400 km2, 1904, against 2,676,386) is acknowledged.

What breaks: the notes and /keyframe_review/0 say the 1961 polygon is "cell for cell" the nine territories. It is not. In the Cliopatria geometry (features cache), british-east-africa_1961 has 13 parts. Besides the mainland blocks and Gambia, Lesotho and Swaziland, it holds:
- Socotra: 5,563 km2 at 53.93 E 12.56 N
- Zanzibar (Unguja): 2,306 km2 at 39.27 E 6.18 S
- Pemba: 1,095 km2 at 39.64 E 5.28 S
- Mafia Island: 866 km2 at 39.67 E 7.85 S
- the Seychelles: 259 km2 at 55.35 E 4.66 S. The shapes.csv east edge of 55.4304 is the Seychelles shape's own east edge.

Consequences and fixes:
1. /keyframe_review/2-4: the minus-chains keep Zanzibar and Pemba after the Sultanate's independence on 10 December 1963 (Decolonisation table row "Sultanate of Zanzibar | 10 December 1963"). The sultanate-of-zanzibar dossier founds 1963-12 on {region: Zanzibar}, so that land is drawn twice to 1965. The chains also keep Mafia Island after Tanganyika's independence on 9 December 1961. Fix: subtract {region: Zanzibar} in the 1963, 1964 and 1965 keyframes and Mafia from 1962, and add a loss 1963-12 to sultanate-of-zanzibar (confidence 3, Decolonisation page).
2. /keyframe_review/5: the intersect with eSwatini silently drops the Seychelles, which were British to 1976, and Socotra. Fix: intersect with {any: [eSwatini, Seychelles]}. For Socotra, which belonged to the Aden Protectorate, either remove it from 1961 on as an artifact, saying so in text, or keep it to 1967 with a loss to the South Yemen successor.
3. /ledger/9: the 1968 gain of the Seychelles from british-colonial-empire did not happen. The islands are already in this shape, and british-colonial-empire's 1963-1968 shape does not contain them (0 km2 intersection). Delete it.
4. Rewrite the "cell for cell" claim in /keyframe_review/0/note and /notes.

Cross-dossier: Swaziland is drawn twice 1961-1968 (author flagged). The seychelles dossier founds 1976-06 from kingdom-of-great-britain, not from this slug.

## central-african-republic and seleka (fail)

Confirmed: independence on 13 Aug 1960; the Central African Empire from 4 Dec 1976 to Sep 1979; the towns N'Délé, Sam Ouandja and Ouadda taken on 10 Dec 2012; "By the end of 2014, the country was de facto partitioned"; ex-Séléka factions held "about 60%" (undated); the Republic of Logone on 14 Dec 2015 (intended capital Bambari); the UPC and 3R disarmament agreements of 11 Jul 2025.

What breaks: the CAR Civil War page says the government "captured a number of strategic towns throughout February 2021", naming:
- Bria (Haute-Kotto), which is seleka's own capital in the dossier
- Kaga-Bandoro (Nana-Grébizi)
- the Bakouma sub-prefecture and Nzacko (Mbomou)
- Bossembele, Bouar, Beloko and Bossangoa

After a Wagner offensive in March 2022, "the rebels were being pushed back". Four groups (MLCJ, RPRC, UFR, UFR-R) announced their dissolution on 4 Dec 2022. The CAR /ledger/5 note quotes the 2021 sentence and still draws all eight prefectures rebel-held to 2024. That is about 380,000 km2 drawn wrongly for four years, against a page the author read. The "towns, not areas" reason does not hold: the same dossier turns three towns into two prefectures for 2012.

Fixes:
- CAR: add a gain 2021-2 from seleka covering at least Haute-Kotto, Nana-Grébizi and Mbomou (confidence 2). Optionally add a contest over the rest.
- seleka: end seleka_2014 at 2020, add seleka_2021 without those prefectures, and add the mirror loss 2021-2. End the capital Bria in 2021.
- seleka: record the formal disbanding ("On 13 September 2013, Djotodia formally disbanded Séléka") as a rename to the ex-Séléka factions, or state it in notes. Check that 3R, which the page names among the six CPC groups of 19 Dec 2020, is not counted as a Séléka faction.
- Non-blocking, CAR /wars/0: the CAR page says that in November 2006 the rebels "had taken control of towns in the country's northern regions". "No territory" is too strong.

## mali-federation (thin)

Confirmed on the pages:
- independence 20 Jun 1960
- Senegal's secession 20 Aug 1960
- the rename on 22 Sep 1960
- the Agacher ICJ division on 22 Dec 1986 ("Mali received the more-densely populated western portion")
- the Azawad declaration on 6 Apr 2012
- the partial recapture a month after 11 Jan 2013

Area: 1,246,690 against 1,240,192 km2.

Gaps:
- The 1974 conflict is dated on the Agacher page ("In 1974, a brief armed conflict broke out"), not undated as the notes say. Add a contest 1974-1975.
- The Mali page says ISGS was "occupying large swaths of territory in southeastern Mali" in 2022-2023 and "By mid-2023 ... had doubled the amount of territory it controlled". Add a contest over the Ménaka region.
- Nothing covers Kidal outside government control from 2013 to 2023 (try the Mali War page).
- The capital move to Bamako is confidence 1.

## burkina-faso (thin)

Confirmed: independence 5 Aug 1960; the rename (4 Aug 1984 in the lead, 2 Aug in the history section); the war of 25-30 Dec 1985; the 1986 division. Area: 274,142 against 274,223 km2.

Gaps:
- The 1974 conflict (same as Mali).
- The jihadist insurgency: the page gives only percentages ("about 60% of the country under government control", 2022; "around 50% ... in the hands of Islamists", 2023). A contest needs a page that names regions.
- Oudalan stands in for the Agacher Strip at confidence 2. The page names Dionouga, Sebba, Kounia and Douna. The gazetteer name is requested.

## republic-of-cameroon, togo, azawad (pass)

Cameroon: every event confirmed. The geometry shows the 1961-2023 shape contains Bakassi and every Nigeria shape excludes it, so the Bakassi adjust is right. But the Nigeria dossier (af-08) must hold Bakassi from 1961 to 2005/2007 and lose it in 2006 and 2008, or the peninsula is blank.

Togo: the one event is confirmed.

Azawad:
- confirmed: 6 Apr 2012 to 14 Feb 2013; Timbuktu proclaimed and Gao provisional as capitals
- the three regions sum to 819,928 km2 against the page's 60 percent, as the author says
- the Islamist takeover of June-July 2012 is flagged

## Cross-dossier routing

- federal-republic-of-nigeria: no Bakassi in the shapes or the ledger. Needs losses 2006-08 and 2008-08 to republic-of-cameroon, and Bakassi held from 1961.
- sultanate-of-zanzibar against british-east-africa: Zanzibar is drawn twice from 1963-12 to 1965 (fix on the BEA side).
- swaziland against british-east-africa: Eswatini is drawn twice 1961-1968.
- seychelles: its found event names kingdom-of-great-britain; the land comes from british-east-africa.
- french-fifth-republic (eu-22): must lose Burkina Faso and the CAR in 1960.
- republic-of-senegal (af-08): must found 1960-08.
- british-gold-coast (af-08): carries the 1961 Southern Cameroons loss.
- malawi, zambia, the Gambia, rhodesia, botswana, lesotho (af-08): must found at their independence dates (1964-1966).
