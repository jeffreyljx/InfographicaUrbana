# Review of batch am-07-c (reviewer, 2026-10-19)

One dossier: united-states-of-america. Verdict: **fail** (three unapplied blocking findings; no event found fabricated or mis-dated).

Validator clean (0 errors, 5 counterpart-slug warnings, all for listed counterparts_needing_dossiers). 19 spot checks across S1, S2, S5 and S11, weighted to confidence-3 and large-land events: all dates confirmed, no fabrication found, page-silent claims honest except Midway and Wake. Fails on three unapplied blocking findings: the 1863 West Virginia gain double-counts land never lost; the 1818 Anglo-American Convention swap stated on an opened page is missing; the 1942-45 Philippines are a loss/gain against an existing empire-of-japan dossier that records an occupation, and Japan's occupations of Guam and the Aleutians have no US events. No reviewer fixes applied (none was a small verified edit).

## Findings (author to make; none applied by the reviewer)

1. `/ledger/55` (blocking)
   - What: The 1863-06 gain of West Virginia from confederate-states-of-america adds land the dossier never lost: /ledger/48 (1861-04) takes away only Virginia minus West Virginia.
   - Why: Territory page (S1), row 20 June 1863: 'The northwestern counties of Virginia, represented by the Restored Government of Virginia in Wheeling ... were admitted as the thirty-fifth state, West Virginia': an admission of loyal counties, not land taken from the Confederacy. The map would outline West Virginia as a new gain in 1863, and the CSA dossier would need a mirror loss of land it never held under this model.
   - Fix: Delete /ledger/55 and mention the admission in the /ledger/48 note (or in the 1863 keyframe note). If you would rather model Confederate claims, make /ledger/48 all of Virginia and date the regain of the north-western counties to the 1861 western Virginia campaign with a page that dates it; do not keep both readings.

2. `/ledger (new events between /ledger/28 and /ledger/29)` (blocking)
   - What: The 1818 Anglo-American Convention land swap is missing from the ledger, though a page the author opened states it and the keyframe 21 and certainty notes cite the 49th parallel line.
   - Why: Louisiana Purchase page (S5): the northern borders 'were adjusted by the Treaty of 1818 with the British'; 'the territory north of the 49th parallel (including the Milk River and Poplar River watersheds) was ceded to the UK' in exchange for 'parts of the Red River Basin south of 49th parallel'. Territory page (S1), row 30 January 1819: 'The Treaty of 1818 set 49° north as the border with the United Kingdom west of the Lake of the Woods'.
   - Fix: Add a gain (counterpart british-colonial-empire, region: the Red River of the North basin south of 49N, i.e. eastern North Dakota and north-western Minnesota west of the Lake of the Woods) and a loss (counterpart british-colonial-empire, region: the Milk River and Poplar River watersheds north of 49N in southern Alberta/Saskatchewan), dated 1818-10 (signed 20 October 1818) or 1819-01 (in force, S1), confidence 2, source S5; make sure the /ledger/20 'Louisiana' region and the 1815-1819 and 1820 corrections agree with the new line.

3. `/ledger/87` (blocking)
   - What: The Japanese conquest of the Philippines is a loss (1942, confidence 1) and its recovery a gain (/ledger/88, 1945), while the existing empire-of-japan dossier records an occupation (occupation_start 1942-05 /ledger/65, occupation_end 1945-09 /ledger/110); Japan's occupations of Guam (1941-12..1944-08, its /ledger/56 and /ledger/72) and of Attu and Kiska (1942-06..1943-05 and 1943-07, its /ledger/66-69) have no US events at all.
   - Why: Brief rule 3: an occupation of X's land is an occupation in X's ledger; the schema: for occupation_start 'the owner records the same event with the roles reversed'. Timeline page (S2) speaks only of '1944-1946: Temporary reoccupation of the Philippines', i.e. the US was the sovereign throughout.
   - Fix: Replace /ledger/87 and /ledger/88 with occupation_start (1942-05) and occupation_end (1945) against empire-of-japan for the Philippines, keep the islands as US land in the 1942-1944 corrections (hatched, not removed), and add occupation pairs against empire-of-japan for Guam (1941-12..1944-08) and for Attu and Kiska (1942-06..1943-05/07), each citing a page that dates them (e.g. https://en.wikipedia.org/wiki/Aleutian_Islands_campaign, https://en.wikipedia.org/wiki/Battle_of_Guam_(1941), https://en.wikipedia.org/wiki/Philippines_campaign_(1941%E2%80%931942)).

4. `/wars`
   - What: No World War II entry, although the ledger carries its events (1941 protections of Greenland and Iceland, the 1942-45 Philippines events, the 1945 occupations of Germany, Austria, Japan and Korea); World War I (Rhineland occupation, which Cliopatria draws 1919-23) and the Korean War are also absent.
   - Why: Reviewer brief check 10: each war in the sources appears; the Timeline page (S2) is a source and lists both world wars.
   - Fix: Add a 'World War II' war (1941-12..1945-09, belligerents united-states-of-america and empire-of-japan/nazi-germany) with zones for the Philippines, Guam and Attu/Kiska once the occupation events exist; add World War I (1917-04..1918-11) with empty zones and a note that no US land changed hands (the Rhineland occupation is a gap).

5. `/ledger/30/region`
   - What: The 1842 Webster-Ashburton gain uses the whole of Maine (admin1 Maine), though the land at issue was only the disputed north; the rest of Maine was US land from 1783 (it lies inside the found region and the 1783 treaty).
   - Why: Territory page (S1), row 13 October 1842: the treaty 'defined the border with the United Kingdom east of the Rocky Mountains', resolving disputes over 'the northern borders of Maine and New Hampshire and the northeastern border of Wisconsin Territory' and affirming the US claim to Sugar Island.
   - Fix: Restrict the region to the disputed northern Maine (Aroostook and the upper Saint John valley, roughly Maine north of 46N; the author's own gazetteer request 'Eastern Maine'), add the Indian Stream/New Hampshire strip if wanted, keep confidence 2, and check that the pre-1842 corrections leave that strip out.

6. `/ledger/53/region`
   - What: The February 1862 Union gain is all of Tennessee (admin1 Tennessee) while the note and text say 'central Tennessee: Fort Henry, Fort Donelson, Nashville'; Memphis fell in June 1862 and East Tennessee (Knoxville, Chattanooga) only in late 1863, and Cliopatria itself draws Tennessee 43% in 1862 and 83% in 1863.
   - Why: The event's own text, and the 1862/1863 keyframe notes quoting Cliopatria's Tennessee shares.
   - Fix: Limit the 1862-02 region to Middle Tennessee (Nashville, the Cumberland and Tennessee river forts), and add later gains for West Tennessee (Memphis, 1862-06) and East Tennessee (Knoxville 1863-09, Chattanooga 1863-11) citing the American Civil War page or a campaign page.

7. `/ledger (new events) and the report's gazetteer list`
   - What: Midway and Wake are said to be undated on every page opened ('no page opened dates it'), but the Territory page dates both.
   - Why: Territory page (S1): row 28 August 1867 'Midway Atoll was claimed.'; row 17 January 1899 'Wake Island was claimed.'
   - Fix: Add two gains, counterpart nobody, confidence 3, source S1: Midway Atoll 1867-08 and Wake Island 1899-01 (tiny, but Wake is the land empire-of-japan occupies 1941-12..1945-09); correct the notes.

8. `/ledger/64`
   - What: The 1898-07 occupation of Cuba (and its end, /ledger/74) names republic-of-cuba, a Cliopatria row that starts in 1905 (the event's own note says so); in July 1898 Cuba was Spanish, and spanish-empire records a 1898-12 loss of Cuba to the US (/ledger/122) that has no mirror here.
   - Why: Spanish-American War page (S11): Cuba 'having been occupied since July 17, 1898 ... under the jurisdiction of the U.S. military government'; spanish-empire.json /ledger/122.
   - Fix: Make the 1898-07 occupation_start against spanish-empire, end it at the Treaty of Paris (1898-12), and start a second occupation pair for 1899-01..1902-05 against whatever slug am-08 gives Cuba before 1905 (or 'Cuba'); tell am-06 that the Cuba cession is an end of occupation on the US side, not a gain.

9. `/ledger/45`
   - What: Losses to confederate-states-of-america are dated 1860-12 (South Carolina) and 1861-01 (/ledger/46: Mississippi, Florida, Alabama, Georgia, Louisiana), before the Confederacy was formed in February 1861 (the author's notes give 4 or 8 February 1861; the Cliopatria row starts in 1861).
   - Why: Author's notes ('Confederacy formed 4 February 1861 (Civil War page) or 8 February 1861 (Territory page)'); polities.csv confederate-states-of-america first_year 1861.
   - Fix: Keep the secession dates but say in both notes that the seceded states stood alone until 1861-02, and flag to am-07 part d that the CSA dossier must begin at 1860-12 (or carry these states in its found region) so the losses have a mirror.

10. `/ledger/92`
   - What: The 1945 occupation of South Korea (and its 1949 end, /ledger/97) names republic-of-korea, founded only in 1948-08; empire-of-japan records the 1945 transfer as a loss of South Korea to the US (/ledger/77) and republic-of-korea records the US as its predecessor at its 1948-08 founding. Likewise /ledger/89 and /ledger/96 name federal-republic-of-germany (row 1950-1990) for the 1945 occupation.
   - Why: republic-of-korea.json /ledger/0 and identity.predecessors; empire-of-japan.json /ledger/77; polities.csv first_year of federal-republic-of-germany 1950. Timeline page (S2): '1945-1949: Post-World War II occupation of South Korea'.
   - Fix: Name the 1945 owner in the occupation_start (empire-of-japan for Korea; nazi-germany or the slug eu-22 gives occupied Germany), say in the note that the occupation ended at the founding of the Republic (1948-08) with troops out in 1949, and route the type disagreement (loss vs occupation) to jk-01.

11. `/wars/0/from`
   - What: The American Revolutionary War starts in 1775, before identity.start (1776-07).
   - Why: Reviewer brief check 2: wars inside the life.
   - Fix: Either set from to 1776 with a note that fighting began in April 1775, or keep 1775 and say in the war note why it precedes the state's founding; no ledger change needed.

## Thin (for a gap-filler)

- `/ledger/8`: End of the Georgia contest, year only at confidence 1 (Savannah evacuated 11 July 1782). Page to try: https://en.wikipedia.org/wiki/Capture_of_Savannah
- `/ledger/38`: End of the Veracruz and Mexico City occupations (/ledger/39), 1848 at confidence 1 (June-August 1848). Page to try: https://en.wikipedia.org/wiki/Treaty_of_Guadalupe_Hidalgo
- `/ledger/59`: Trans-Mississippi surrender, 1865 at confidence 1 (Kirby Smith, 2 June 1865). Page to try: https://en.wikipedia.org/wiki/Conclusion_of_the_American_Civil_War
- `/ledger/71`: Start of the Philippine-American War, 1899 at confidence 1 (S11 confirmed silent; 4 February 1899 elsewhere). Page to try: https://en.wikipedia.org/wiki/Philippine%E2%80%93American_War
- `/ledger/87`: Japanese conquest of the Philippines, 1942 at confidence 1 (Bataan April, Corregidor 6 May 1942); see the occupation fix. Page to try: https://en.wikipedia.org/wiki/Philippines_campaign_(1941%E2%80%931942)
- `/ledger/93`: End of the Greenland protection, 1946 at confidence 1 (the year is Cliopatria's). Page to try: https://en.wikipedia.org/wiki/Greenland_in_World_War_II
- `/ledger/94`: End of the Iceland protection, 1946 at confidence 1 (Keflavik Agreement 1946, troops out 1947). Page to try: https://en.wikipedia.org/wiki/Allied_occupation_of_Iceland
- `/ledger/100`: Canal Zone return, 1979 without month (1 October 1979) and the 1999 final transfer. Page to try: https://en.wikipedia.org/wiki/Panama_Canal_Zone
- `/identity/capitals/0`: Philadelphia 1776-99 is unsourced; the Congress sat in several cities and New York was the capital 1785-1790. Page to try: https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States
- `/identity/rulers`: No ruler strip (presidents). Page to try: https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States
- `/ledger (Trust Territory)`: Trust Territory of the Pacific Islands and Northern Marianas 1945/47-1986/94: mirrors empire-of-japan /ledger/79 (1945 loss of Micronesia to the US) and micronesia /ledger/0 (1986-11 found from the US). Page to try: https://en.wikipedia.org/wiki/Trust_Territory_of_the_Pacific_Islands
- `/ledger (Ryukyus)`: US occupation of Okinawa 1945-1972, Amami 1945-1953, Bonin and Volcano Islands 1945-1968: mirrors empire-of-japan /ledger/80-82 and /ledger/113-115; the 1947-66 correction removes all of Japan. Page to try: https://en.wikipedia.org/wiki/United_States_Civil_Administration_of_the_Ryukyu_Islands
- `/keyframe_review/60`: Rhineland occupation 1918-1923 (Cliopatria draws 28 cells in Germany 1919-23; removed with no occupation event). Page to try: https://en.wikipedia.org/wiki/Occupation_of_the_Rhineland
- `/ledger (1779, 1783-95, 1817-19)`: Mirrors for haudenosaunee's 1779 Sullivan Expedition contest and spanish-florida's 1783-1795 (31N-32.5N strip) and 1817-1819 (First Seminole War) contests. Page to try: https://en.wikipedia.org/wiki/Sullivan_Expedition ; https://en.wikipedia.org/wiki/Pinckney%27s_Treaty ; https://en.wikipedia.org/wiki/Seminole_Wars

## Spot checks

- `/ledger/43` confirmed: row May 30, 1848: Guadalupe Hidalgo 'ceded a large region from Mexico' (https://en.wikipedia.org/wiki/Territorial_evolution_of_the_United_States)
- `/ledger/61` confirmed: row October 18, 1867: 'Alaska was purchased from the Russian Empire and designated the Department of Alaska.' (https://en.wikipedia.org/wiki/Territorial_evolution_of_the_United_States)
- `/ledger/73` confirmed: row April 19, 1901: Aguinaldo, captured 23 March 1901, 'took an oath of allegiance ... ending the First Philippine Republic' (https://en.wikipedia.org/wiki/Territorial_evolution_of_the_United_States)
- `/ledger/19` confirmed: 'France turned over New Orleans ... on December 20, 1803' (https://en.wikipedia.org/wiki/Louisiana_Purchase)
- `/ledger/20` confirmed: 'On March 9 and 10, 1804 ... Three Flags Day ... St. Louis'; 828,000 sq mi (2,140,000 km2) (https://en.wikipedia.org/wiki/Louisiana_Purchase)
- `/ledger/97` confirmed: '1945-1949: Post-World War II occupation of South Korea' (https://en.wikipedia.org/wiki/Timeline_of_United_States_military_operations)
- `/ledger/85` confirmed: '1941: Iceland was taken under the protection of the United States' (no month) (https://en.wikipedia.org/wiki/Timeline_of_United_States_military_operations)
- `/ledger/86` confirmed: 'Greenland was taken under protection of the United States in April' (https://en.wikipedia.org/wiki/Timeline_of_United_States_military_operations)
- `/ledger/18` confirmed: row April 25, 1796: 'The northern half of West Florida was ceded by Spain' (https://en.wikipedia.org/wiki/Territorial_evolution_of_the_United_States)
- `/ledger/30` confirmed: row October 13, 1842 confirmed; region overstated (see fixes) (https://en.wikipedia.org/wiki/Territorial_evolution_of_the_United_States)
- `/ledger/55` confirmed: row June 20, 1863 confirmed; the event double-counts (see fixes) (https://en.wikipedia.org/wiki/Territorial_evolution_of_the_United_States)
- `/ledger/77` confirmed: row May 19, 1904: 'The Panama Canal Zone was granted by Panama' (https://en.wikipedia.org/wiki/Territorial_evolution_of_the_United_States)
- `/ledger/76` confirmed: row December 10, 1903: Guantanamo Bay leased (https://en.wikipedia.org/wiki/Territorial_evolution_of_the_United_States)
- `/ledger/82` confirmed: row March 31, 1917: Danish West Indies purchased (https://en.wikipedia.org/wiki/Territorial_evolution_of_the_United_States)
- `/ledger/75` confirmed: row October 20, 1903: Alaska boundary dispute resolved 'generally in favor of the United States claim' (https://en.wikipedia.org/wiki/Territorial_evolution_of_the_United_States)
- `/ledger/80` confirmed: Haiti 'From July 28, 1915, to August 15, 1934'; Dominican Republic 'From May 1916 to September 1924' (/ledger/81, /ledger/83) (https://en.wikipedia.org/wiki/Timeline_of_United_States_military_operations)
- `/ledger/78` confirmed: Cuba 'From September 1906 to January 23, 1909' (/ledger/79) (https://en.wikipedia.org/wiki/Timeline_of_United_States_military_operations)
- `/ledger/64` confirmed: 'Having been occupied since July 17, 1898' (https://en.wikipedia.org/wiki/Spanish%E2%80%93American_War)
- `/ledger/71` confirmed: page gives no date for the outbreak of the Philippine-American War: the confidence 1 'page silent' is honest (https://en.wikipedia.org/wiki/Spanish%E2%80%93American_War)

## Area

Infobox 9833520 km2 (undated, taken as 2024) against Cliopatria 2024 9436681 km2: ratio 0.96, acknowledged. Infobox area is undated (taken as current, 2024 shape). Pre-1889 shapes draw settled land only (1860: 4.30 M km2 against a treaty extent near 8 M km2, about x1.9); acknowledged in every keyframe note and corrected by adjust verdicts. 1941-45 shapes (12.0-12.19 M km2) include Greenland and occupied lands; acknowledged and removed.

## Cross-dossier matrix (non-exception rows)

- united-states-of-america 1784 gain haudenosaunee (/ledger/13) -> matched: haudenosaunee 1784 loss /ledger/32 Fort Stanwix; this side has no month (haudenosaunee gives 22 October 1784).
- united-states-of-america 1796 gain spanish-florida (/ledger/18) -> mismatch: no mirror spanish-florida has no 1795-96 loss to the US (only /ledger/12 1795 contest_end of the 31-32.5N strip); spanish-empire /ledger/69 records the same land as a 1795 loss to the US. Same land under two counterparts and two years (treaty 1795 vs cession row 25 April 1796); am-06 should pick one owner and the US counterpart should follow.
- united-states-of-america 1803 gain french-louisiana (/ledger/19) -> matched: french-louisiana 1803 loss /ledger/4 
- united-states-of-america 1804 gain french-louisiana (/ledger/20) -> matched: french-louisiana 1804 loss /ledger/6 
- united-states-of-america 1810 gain spanish-florida (/ledger/21) -> matched: spanish-florida 1810 loss /ledger/13 spanish-florida loses a wider region (West Florida west of the Pearl/Perdido) than the Baton Rouge district here; land differs (author flagged).
- united-states-of-america 1812 gain spanish-florida (/ledger/22) -> matched: spanish-florida 1812 loss /ledger/14 
- united-states-of-america 1821 gain spanish-florida (/ledger/29) -> matched: spanish-florida 1821 dissolve /ledger/17 spanish-empire /ledger/94 also records a 1821-07 loss of Florida to the US: double-counted on the Spanish side (am-06).
- united-states-of-america 1898 occupation_start spanish-empire (/ledger/62) -> missing: no mirror spanish-empire records no 1898 occupation of Guam, Puerto Rico or Manila by the US, only the 1898-12 cession (/ledger/121); am-06 to add the occupation pairs.
- united-states-of-america 1898 occupation_start spanish-empire (/ledger/63) -> missing: no mirror spanish-empire records no 1898 occupation of Guam, Puerto Rico or Manila by the US, only the 1898-12 cession (/ledger/121); am-06 to add the occupation pairs.
- united-states-of-america 1898 occupation_start spanish-empire (/ledger/65) -> missing: no mirror spanish-empire records no 1898 occupation of Guam, Puerto Rico or Manila by the US, only the 1898-12 cession (/ledger/121); am-06 to add the occupation pairs.
- united-states-of-america 1898 gain republic-of-hawai-i (/ledger/66) -> matched: republic-of-hawai-i 1898 dissolve /ledger/1 
- united-states-of-america 1898 occupation_end spanish-empire (/ledger/67) -> missing: no mirror spanish-empire records no 1898 occupation of Guam, Puerto Rico or Manila by the US, only the 1898-12 cession (/ledger/121); am-06 to add the occupation pairs.
- united-states-of-america 1898 occupation_end spanish-empire (/ledger/68) -> missing: no mirror spanish-empire records no 1898 occupation of Guam, Puerto Rico or Manila by the US, only the 1898-12 cession (/ledger/121); am-06 to add the occupation pairs.
- united-states-of-america 1898 occupation_end spanish-empire (/ledger/69) -> missing: no mirror spanish-empire records no 1898 occupation of Guam, Puerto Rico or Manila by the US, only the 1898-12 cession (/ledger/121); am-06 to add the occupation pairs.
- united-states-of-america 1898 gain spanish-empire (/ledger/70) -> matched: spanish-empire 1898 loss /ledger/121 
- united-states-of-america 1900 gain kingdom-of-samoa (/ledger/72) -> mismatch: kingdom-of-samoa 1900 dissolve /ledger/3 kingdom-of-samoa dissolves into german-empire with a region that includes American Samoa, while its own identity.successors gives American Samoa to the US; the Samoa dossier (oc group) should split the dissolve land: American Samoa to united-states-of-america.
- united-states-of-america 1942 loss empire-of-japan (/ledger/87) -> mismatch: empire-of-japan 1942 occupation_start /ledger/65 US records a loss (c1, no month), empire-of-japan an occupation from 1942-05 (c3). The US side should become occupation_start/occupation_end with empire-of-japan (see fixes).
- united-states-of-america 1945 gain empire-of-japan (/ledger/88) -> mismatch: empire-of-japan 1945 occupation_end /ledger/110 US records a gain from Japan; empire-of-japan records the end of its occupation of the Philippines in 1945-09.
- united-states-of-america 1945 occupation_start empire-of-japan (/ledger/91) -> matched: empire-of-japan 1945 occupation_start /ledger/89 US side has no month; empire-of-japan gives 1945-09 for the main islands.
- united-states-of-america 1945 occupation_start republic-of-korea (/ledger/92) -> mismatch: empire-of-japan 1945 loss /ledger/77 republic-of-korea (founded 1948-08) cannot be the owner in 1945; empire-of-japan records the 1945 loss of South Korea to the US as a loss (territory), not an occupation. One of the two should change; occupation of land Japan lost is the US reading (Timeline page).
- united-states-of-america 1949 occupation_end republic-of-korea (/ledger/97) -> mismatch: republic-of-korea 1948 found /ledger/0 republic-of-korea is founded 1948-08 with the US as predecessor; the US occupation ends 1949 (Timeline span 1945-1949). One year apart and different types; acceptable within a year but the ROK side has no occupation_end.
- united-states-of-america 1952 occupation_end empire-of-japan (/ledger/98) -> matched: empire-of-japan 1952 occupation_end /ledger/112 US side has no month (28 April 1952 on the Japan side).
- haudenosaunee 1779 contest_start united-states-of-america (/ledger/30) -> missing: no mirror Sullivan Expedition 1779-06..1779-10: no US contest event.
- spanish-florida 1783 contest_start united-states-of-america (/ledger/11) -> missing: no mirror The 31N-32.5N strip disputed 1783-1795: no US contest pair (US /ledger/10 leaves the strip out and gains it in 1796).
- spanish-florida 1817 contest_start united-states-of-america (/ledger/15) -> missing: no mirror First Seminole War contest 1817..1819-02: no US event (author flagged; none of the 14 pages covers it).
- spanish-empire 1795 loss united-states-of-america (/ledger/69) -> mismatch: no mirror US pairs this land with spanish-florida in 1796-04 (/ledger/18).
- spanish-empire 1898 loss united-states-of-america (/ledger/122) -> mismatch: no mirror Cuba: the US carries an occupation (1898-07..1902-05) against republic-of-cuba, a row that starts in 1905; no US gain. Spain should record the end of a US occupation or a loss to Cuba, and the US occupation_start counterpart should be spanish-empire.
- empire-of-japan 1941 occupation_start united-states-of-america (/ledger/56) -> missing: no mirror Guam occupied 1941-12..1944-08: no US occupation pair.
- empire-of-japan 1941 occupation_start united-states-of-america (/ledger/57) -> missing: no mirror Wake occupied 1941-12..1945-09: the US dossier draws no Wake at all (Wake claimed 17 January 1899 on the Territory page).
- empire-of-japan 1942 occupation_start united-states-of-america (/ledger/66) -> missing: no mirror Attu and Kiska occupied 1942-06..1943-05/07: no US occupation pairs.
- empire-of-japan 1945 loss united-states-of-america (/ledger/79) -> missing: no mirror Japanese Micronesia (South Seas Mandate) passes to the US in 1945: the US carries no Trust Territory (author gap).
- empire-of-japan 1945 occupation_start united-states-of-america (/ledger/80) -> missing: no mirror Okinawa/Ryukyus 1945..1972, Amami 1945..1953 (/ledger/81), Bonin and Volcano Islands 1945..1968 (/ledger/82): no US events (author gap).
- micronesia 1986 found united-states-of-america (/ledger/0) -> missing: no mirror Micronesia founded from US-administered land; the US carries no Trust Territory events (author gap).

54 further events are exceptions: their counterparts (british-colonial-empire, kingdom-of-great-britain, vermont-republic, confederate-states-of-america, republic-of-texas, federated-republic-of-mexico, russian-empire, republic-of-cuba, republic-of-panama, denmark-norway, greenland, kingdom-of-iceland, republic-of-haiti, dominican-republic, federal-republic-of-germany, second-republic-of-austria, iraqi-republic, republic-of-the-philippines) belong to groups that have not run yet (eu-11, am-07 part d, am-08, eu-17, eu-14, eu-21, eu-22, me-10, se-04), or are in counterparts_needing_dossiers (thirteen-colonies, northwestern-confederacy, first-philippine-republic).

## Problems

- No page failed to load. Neighbour dossiers read: spanish-empire, republic-of-korea, democratic-people-s-republic-of-korea, micronesia (Context list); also the existing counterpart dossiers spanish-florida, french-louisiana, haudenosaunee, republic-of-hawai-i, kingdom-of-samoa, empire-of-japan. The other 35 Context polities have no dossier yet (owner groups have not run).
- Counterpart-side faults found while cross-checking (not in this batch): spanish-empire double-counts Florida 1821 and the 1795 strip with spanish-florida and records no 1898 occupations of Guam, Puerto Rico and Manila; kingdom-of-samoa dissolves American Samoa into german-empire although its successors give it to the US.
- The orchestrator's adjustments redefine 'fix' as fixed by the reviewer; findings the author must make are applied: false and this dossier is therefore 'fail', though no event was found fabricated or mis-dated.
