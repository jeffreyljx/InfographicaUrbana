# Review af-08-d (2026-10-19)

Reviewer for batch af-08-d: british-africa, belgian-congo. Machine copy: history/notes/phase-b/reviews/af-08-d.json.

Both dossiers pass the validator with --resolve: 0 errors. british-africa has two warnings, both for sultanate-of-egypt, which has no dossier and is listed under counterparts_needing_dossiers.

## british-africa: thin (I applied the small fixes)

What I tried: years in order; the vassal, contest and occupation pairs (all close); each keyframe step against the ledger, with the country composition of the Cliopatria shapes taken from the gazetteer; the area; 14 events on 8 pages; cross-checks against 23 dossiers. Every confidence-3 event I opened says what its note claims.

Applied by me, each verified on a page I opened, then re-validated (0 errors):
- **Somaliland trusteeship date.** /ledger/48 (was /ledger/51): the Italian Somaliland occupation_end was 1960 at confidence 1. It is now **1 April 1950** at confidence 3. Trust Territory of Somaliland: "The British continued to administer the area until 1 April 1950". The event was moved and the ledger re-sorted.
- **Libya start date and Fezzan.** /ledger/47: the Libya occupation_start was 1944 at confidence 1, drawn over the whole of Libya. It is now **February 1943** at confidence 2, because the infobox gives 13 May 1943. The region is now Libya minus Fezzan: "the French controlled Fezzan", per British Military Administration (Libya). Libya minus Fezzan resolves to 3,424 cells, against Cliopatria's 3,427.
- **Libya end region.** /ledger/49 (was /ledger/48): the Libya occupation_end now uses the same region.
- **Eritrea month.** /ledger/50 (was /ledger/49): the Eritrea end is now **15 September 1952** at confidence 3 (Federation of Ethiopia and Eritrea).
- **Ethiopia month.** /ledger/46: the Ethiopia end is now **31 January 1942** at confidence 2 (Ogaden War: "except Ogaden").
- **Sources.** Four were added: Trust_Territory_of_Somaliland, British_Military_Administration_(Libya), Federation_of_Ethiopia_and_Eritrea and Ogaden_War.

For the author (not applied):
1. **Ogaden and Haud.** /ledger/46 releases all of Ethiopia in January 1942, but the Ogaden and the Haud stayed British. The Ogaden War page: "the British gave the Haud and the Ogaden to Ethiopia" (1948); "The last remaining British controlled parts of the region were transferred to Ethiopia in 1955". The ethiopia dossier has the mirror events (/ledger/2, /ledger/4). Fix: carve the Ogaden and Haud out of the 1942 release, then add a 1948 occupation_end (and the 1955 remainder).
2. **Kigoma.** /ledger/36 records Kigoma in 1921-03 as a gain from belgian-congo, but belgian-congo has an occupation_end for it, not a loss. Fix: make it an occupation_start (counterpart german-africa) and gain all of Tanzania at the 1922-07 mandate.
3. **Nile valley 1896-1899.** mahdist-state loses Dongola (1896-09), Abu Hamed (1897-08) and Omdurman (1898-09) to british-africa, but this dossier gains nothing until 1899-06. Fix: add those gains, or move the Nile-valley gain to 1898-09.
4. **Darfur.** /ledger/33 needs month 11 and a contest pair over Darfur, matching sultanate-of-darfur /ledger/11-13 and the war already listed in the dossier.
5. **Notes.** Add a sentence saying that Nigeria, the Gold Coast, British Togoland, British Cameroons and Zanzibar lie outside this row (none of the shapes has cells there).

Thin, by design under the 14-page budget (15 pages cited):
- **South-eastern Libya block.** 1,837 cells are British from 1905 to 1929 with no event. It is probably the British/Egyptian sphere east of the 1899 Anglo-French line, ended by the 1925 Italo-Egyptian frontier and the Italian taking of Kufra in 1931. Then 280 cells remain to 1935, probably the Sarra Triangle (ceded 1934).
- **Confidence-1 events.** Five remain: the found event, Botswana 1890, Matabeleland 1894, Swaziland 1908 and the dissolve. The swaziland dossier has a British vassal_start in 1903.
- **Belgian zone in German East Africa.** The 1916 occupation gives Britain all of Tanzania except Kigoma, although the Belgians held Tabora from 19 September 1916 and "one-third of German East Africa" by 1917.
- **Parrot's Beak.** Liberia records it as a 1903 gain from british-africa and a 1911 loss to it (Liberia–Sierra Leone border page); this dossier has neither.

Area: the Scramble for Africa page gives "by 1921 ... 33.23% of Africa, or 3,897,920 mi2", which is about 10.10 M km2. The british-africa_1920 shape is 10.07 M km2, a ratio of 1.00. No factor-of-two problem.

## belgian-congo: pass

What I tried:
- validator, years in order, the occupation and contest pairs;
- the 1890-1898 shapes marked wrong, checked against congo-free-state, which has its own keyframes (1885 and 1895) and the mirror dissolve in 1908-11;
- the 1911 minus-Congo correction (the shape holds 163 Republic-of-the-Congo cells in 1911 and 31 in 1916);
- 8 of 14 events on 3 pages: all confirmed with their year and month;
- the capitals (Boma 1908-1923, Léopoldville 1923-1960, from the infobox);
- the area: about 2,344,000 km2 on the page against 2,358,485 km2 for the shape, a ratio of 1.01.

One declared judgement: Ruanda-Urundi counts as part of the colony from 1922, although the page says "These areas did not become part of the Belgian Congo". The notes defend this with the 1926 administrative merger and ask for a separate ruanda-urundi dossier.

Thin, optional: the Belgian occupation zone beyond Kigoma in 1916-1917 (Tabora); a frontier page for the 1911 Congo cells.

## Cross-dossier issues for the orchestrator

**Counterpart slugs.** free-orange-state, south-african-republic, swaziland, kingdom-of-buganda and imperial-british-east-africa-company name british-colonial-empire. ndebele-kingdom and lozi-kingdom (1899) name british-south-africa-company, which has no dossier. All of these refer to land british-africa claims, and the years agree. Pick one holder.

**Double ownership.** orange-river-colony and transvaal-colony (1902-1910), british-cape-colony, colony-of-natal, basutoland, british-bechuanaland and sierra-leone-colony-and-protectorate all overlap this row.

**Missing mirrors.**
- ethiopian-empire records a 1907 gain from british-africa (confidence 1); british-africa has no 1907 loss.
- mahdist-state records a 1895 loss to belgian-congo; it should be congo-free-state (route to af-01).

Not yet written, so not counted as faults: german-africa, italian-africa, south-africa, republic-of-sudan, federal-republic-of-somalia, british-east-africa, democratic-republic-of-the-congo, republic-of-rwanda and republic-of-burundi (all af-08 parts), plus khedivate-of-egypt and sultanate-of-egypt (me-10).
