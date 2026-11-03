# af-08-j notes (Partition and independence, part j)

Run of 2026-10-24. Six owned states plus one successor state (People's Republic of Zanzibar and Pemba) written; all seven validate (python3 -I tools/validate_dossier.py, with --resolve: three warnings, all the unknown region name 'Kagera Salient'). Pages opened (12): Burundi, Rwanda, Uganda, Kenya, Sultanate of Zanzibar, Lesotho, Shifta War, Zanzibar Revolution, Uganda-Tanzania War (read twice), Second Congo War, Operation Boleas, Foreign relations of Lesotho (thin). One page failed: https://en.wikipedia.org/wiki/Conquered_Territory (url_not_found, retried once). Page extracts come through WebFetch's summariser, so quotes are the summariser's extracts of the page text.

## Cliopatria rows that are wrong, and what the dossiers do

- Sultanate of Zanzibar (1963-1966): the Sultanate lasted 10 December 1963 to 12 January 1964. The same islands were the People's Republic of Zanzibar and Pemba until the union with Tanganyika in April 1964 (the Zanzibar Revolution page gives 23 April and 26 April). Cliopatria adds Zanzibar to its Tanzania shape only in 1967 (882,278 to 886,467 km2). Verdict adjust; the Tanzania dossier (another part) should include Zanzibar from April 1964. The shape also reaches 8.0 S and 4,245 km2, larger than the archipelago the page describes (unexplained; the page gives no area).
- British East Africa (1961-1968, 2.68 M km2): its first shape still holds Kenya, Uganda and Basutoland/Lesotho (bounding box south edge 30.70 S = Lesotho's), overlapping their own shapes in 1963-1968. The british-east-africa dossier should drop them from their independence years (Uganda 9 Oct 1962, Kenya 12 Dec 1963, Lesotho 4 Oct 1966); these dossiers name it as predecessor.
- Republic of Burundi, Republic of Rwanda, Republic of Uganda start in 1963 and Lesotho in 1967, one year after independence (Burundi and Rwanda 1 July 1962, Uganda 9 October 1962, Lesotho 4 October 1966): new keyframes for the missing year, the shape unchanged. Burundi was a kingdom until 28 November 1966 and Uganda a dominion until the (disputed) republic date, so the 'Republic' labels are early; both are rename events, not new states.
- Lesotho 1973-1975: a 0.6 percent bigger shape that resolves to the same 118 cells; drawing noise, not land (verdict ok).
- Kenya (1963-2023): the shape's northern edge (5.36 N) lies beyond the Natural Earth outline (4.94 N) and its country join includes South Sudan, apparently the Ilemi Triangle; neither Kenya nor Shifta War page mentions it (verdict ok, unverified: page budget).

## Border moves outside the Cliopatria shapes (ledger events)

- Kenya Coastal Strip: the Sultan's 16 km strip (Sultanate of Zanzibar page) passes to Kenya on 12 December 1963; gain in the Kenya dossier, loss in the Zanzibar one. The region is proxied by the admin-1 Coast; the gazetteer needs 'Kenya Coastal Strip'.
- Shifta War 1963-1967: contest over the Northern Frontier District (Kenya admin-1 North-Eastern), counterpart federal-republic-of-somalia (it supported the rebels and claimed the district; not a declared belligerent). The Somalia dossier should mirror it.
- Kagera Salient 1978-79 and the Tanzanian stay in Uganda 1979 (Uganda dossier): Uganda holds the Salient from 30 October 1978 to early January 1979 (hatched, not a gain: the annexation was only declared); the Tanzanian offensive enters Uganda on 20-21 January 1979, Kampala falls on 11 April, and the Tanzanian occupation is recorded to June 1979 at confidence 1 because the page is silent on when the troops left. The Tanzania dossier should mirror both. Gazetteer needs 'Kagera Salient' (1,900 km2 strip between the border and the Kagera River).
- Second Congo War 1998-2003: Rwandan occupation of the Kivus (to 5 October 2002) and Ugandan occupation of Orientale and Equateur (to the Luanda Agreement, 6 September 2002); Rwanda-Uganda fights at Kisangani in August 1999 and May-June 2000. Zones are the researcher's reading of the page's towns (Bukavu, Uvira, Goma, Kisangani, Equateur): the page gives no boundary. Burundi's 'occupation of a portion of northeastern Congo' is one undated sentence and is not an event. The DR Congo / Zaire dossiers (another part) should mirror these; RCD-Goma and the MLC held land and may need rebel dossiers (listed in the report).
- Lesotho 1998-99: SANDF (with Botswana troops) deployed to Lesotho on 22 September 1998 and the last South African troops left in May 1999 ('seven months of occupation'). Zone is Maseru district, a reading. The South Africa dossier should mirror it.

## Not settled

- No ruler strips written for any of the seven (no page gives a list; budget). Lesotho's page contradicts itself on Moshoeshoe II's exile (1987 body, 1990 infobox).
- Uganda: the republic date (infobox 9 October 1963; body: 'until the 1966 crisis' and 'In 1967, a new constitution proclaimed Uganda a republic'). The Cliopatria name follows the infobox. Tanzanian withdrawal from Uganda is not on the page. Capital Kampala undated (Entebbe unmentioned).
- Burundi: the political capital moved to Gitega in 2019 (the page body gives no date; the year is that of a cited law of 4 February 2019). The page also contradicts itself on German East Africa (1885 body, 1890 infobox; not used).
- Rwanda: the republic was declared on 28 January 1961 under Belgian administration, before sovereignty on 1 July 1962; no event for it. The RPF-held north in 1990-94 is undated and not mapped.
- First Congo War (1996-97), in which Rwanda, Uganda and Burundi fought in Zaire, was not opened (budget): add to the three dossiers.
- Kenya's 2011 troop deployment in Somalia has a start (2011) but no end or territory on the page: no event. Migingo Island and the Ilemi Triangle not on the pages.
- Page budget: Uganda and Kenya used three pages (budget 1-2) because the Second Congo War page was shared with Rwanda and Burundi and the Zanzibar page gave the Coastal Strip; every other state is inside its budget.

## States and names that need attention elsewhere

- New dossier written here: people-s-republic-of-zanzibar-and-pemba (12 January to April 1964; no Cliopatria row; wikipedia and wikidata null). Its slug is not the slug people-s-republic-of-zanzibar, which is the earlier dossier of the Sultanate of 1856-1890 (Cliopatria 'People's Republic of Zanzibar' 1856-1889): the colour agent should not confuse them.
- Missing states: Rally for Congolese Democracy (RCD-Goma) and Movement for the Liberation of Congo (MLC), rebel-held land in the DR Congo 1998-2003 (Second Congo War page).
- Gazetteer names wanted: Kagera Salient; Kenya Coastal Strip. All other names resolve (Nord-Kivu, Sud-Kivu, Orientale, Equateur, North-Eastern, Coast, Maseru, Zanzibar, Kisangani, Mbarara, Kampala).
