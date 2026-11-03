# oc-02-x notes: Australia, New Zealand and the colonial Pacific, additions batch

Twenty-five dossiers, all new states Cliopatria lacks (`cliopatria_names` []), every keyframe new, verdict `adjust`. All validate with 0 errors. Pages were opened with WebFetch on 2026-10-18 (first four: Colony of New South Wales, Territorial evolution of Australia, Colony of Victoria, Colony of Queensland, fetched across midnight UTC and recorded as 2026-10-18) and 2026-10-19 (all others). Living states end in 2024 (Cliopatria's last year; the schema says "the current year").

## Decisions the orchestrator should take

1. Legal jurisdiction or effective control. The six Australian colonies are drawn as the area the letters patent gave them (meridians 129, 132, 135, 138 and 141 E, 26 S, the Murray), so together they partition the continent by dated lines: 1788 east of 135 E; 129 E from 1825; Tasmania 1825; South Australia 1836; Western Australia 1829; Victoria 1851; Queensland 1859; Northern Territory to South Australia 1863. Cliopatria's British Colonial Empire row draws only settled land (7 cells of Australia in 1788, 675 in 1850, 19,472 in 1880). If the renderer wants effective control, the colony tints must shrink and the interior becomes nobody's land (rule 8); every dossier states which it is in `notes`. New Zealand follows the same rule (the whole of the islands from 21 May 1840) with only the Kingitanga lands cut out (Waikato 1858 to 1864 as a 50 km circle at Hamilton; King Country 1864 to 1883 as a 55 km circle at 175.1 E, 38.6 S minus the Hamilton circle), so that colony-of-new-zealand and maori-king-movement (oc-01) never claim the same cell.
2. Type and family. Colonies of the United Kingdom are `colony`, family britain (as new-zealand and commonwealth-of-australia); German New Guinea and German Samoa family germany; South Seas Mandate family japan; Trust Territory and the Northern Mariana Islands family americas; the independent and free-association island states are `state`, family pacific (as republic-of-fiji, palau). The Northern Mariana Islands are `colony` (a US dependency) like the trust territory.
3. Double drawing. new-zealand (oc-02-a) records the Cook Islands (from 1965) and Niue (from 1974) as clients with counterparts cook-islands and niue; those dossiers now exist and are the states named. The same land must not be drawn once as a client tint and once as a state.

## Cliopatria rows that overlap these dossiers

- British Colonial Empire (eu-11): draws settled Australia, New Zealand, Fiji (70 of 83 cells in 1980), the Solomons (78 cells in 1980), the Gilberts and British New Guinea. It should hand these cells to the colony dossiers on the dates in their ledgers and end Fiji in 1970, the Solomons in 1978.
- German Empire (german-empire, 1871 to 1919): already draws 810 cells of Papua New Guinea in 1890 to 1910; german-new-guinea should replace them. Marshall Islands 1885 to 1906 and Nauru 1888 to 1906 are the German Empire's own protectorate; no dossier of this batch holds them for those years.
- empire-of-japan (jk-01): its occupation and gain events should use counterparts german-new-guinea (1914, 1920), south-seas-mandate (1920 to 1945), british-solomon-islands-protectorate (1942 to 1945), gilbert-and-ellice-islands (Gilberts 1941 to 1943) and territory-of-nauru (Nauru, August 1942 to September 1945).
- United States row (am-07): draws Hawaii and Guam; American Samoa is 0 cells; it still contains Pohnpei and the other districts of the trust territory, which the trust-territory dossier hands over in 1986. It should list commonwealth-of-the-northern-mariana-islands as a dependency.
- French rows: none draws French Polynesia, Wallis and Futuna or New Caledonia (except the New Caledonia row 1856 to 1859). Facts gathered from the French Polynesia page for whoever writes it: protectorate over Tahiti and Tahuata 9 September 1842; Tahiti annexed as a colony in 1880 (kingdom-of-tahiti ends 1880-06 with counterpart french-third-republic); Leeward Islands annexed 1888 (Leewards War until 1897); Rimatara and Rurutu annexed 1889; name Etablissements francais de l'Oceanie from 1903; overseas territory 27 October 1946; renamed French Polynesia 1957; overseas collectivity 28 March 2003; 3,521.2 km2, 121 islands, capital Papeete. Not written here (French holdings, no sources registered).

## Fixes wanted in dossiers of other groups

- new-zealand (oc-02-a): Tokelau 'gain kingdom-of-great-britain 1925' has a guessed counterpart; the Gilbert and Ellice Islands page gives the Order in Council of 11 February 1926 (administration) and 1948 (sovereignty), so the counterpart is gilbert-and-ellice-islands.
- commonwealth-of-australia (oc-02-a): already names the six colonies (merge, 1901), british-new-guinea (1906) and german-new-guinea (1914, 1920). It has no Norfolk Island event (colony-of-norfolk-island ends 1914-07 into Australia) and none for Nauru, which was a mandate and trust territory administered by Australia, not Australian land (see territory-of-nauru).
- kingdom-of-fiji (oc-01): dissolve counterpart is british-colonial-empire; colony-of-fiji is the state that takes the land in 1874. kingdom-of-samoa (oc-01): dissolve counterpart german-empire; german-samoa takes the German part from 1900-03 (the US part, American Samoa, has no dossier).

## Per state

**colony-of-new-south-wales** (1788-02 to 1901-01; 6 pages). Eight keyframes, thirteen events. Not drawn: the Colony of North Australia (17 February 1846 to 28 December 1847, proclaimed 16 January 1849; paper colony under ten years); New Zealand inside the colony 1839 to 1841 (boundary redefinition arrived 15 June 1839; the NSW page gives 1 July 1841 for the separation, the Colony of New Zealand page 3 May 1841); Fort Dundas. Norfolk Island moves to Van Diemen's Land on 26 September 1844 on Territorial evolution, 29 September on the Norfolk Island page.

**colony-of-victoria** (1851-07 to 1901-01; 2 pages). Boundary is the modern Victoria polygon, which differs from the Murray by a few cells. The Eumerella wars begin in 1840 under the Port Phillip District and are outside this colony's life. Eureka is the one war.

**colony-of-queensland** (1859-12 to 1901-01; 3 pages). The pages disagree on creation: letters patent 6 June 1859, proclamation 10 December 1859 (dossier starts at the proclamation). The 1883 New Guinea annexation (repudiated) is not a gain: the protectorate is british-new-guinea. Torres Strait gains (1872, 1879) use a polygon that resolves to no cell.

**colony-of-south-australia** (1836-12 to 1901-01; 3 pages). The colony page is thin on territory; boundaries come from Territorial evolution. The 1840 Cape Jaffa killing is the only frontier-wars entry for the colony; no war entered. The 1911 transfer of the Northern Territory belongs to commonwealth-of-australia.

**colony-of-western-australia** (1829-06 to 1901-01; 4 pages). The Colony of Western Australia URL redirects to History of Western Australia. Founding 2 May 1829 (Territorial evolution) or 17 June 1829 (Swan River page); dossier starts 17 June. The 1832 renaming is a `rename`, not a new state. Convicts from 1850 and self-government in 1890 change no border.

**colony-of-tasmania** (1825-12 to 1901-01; 3 pages). Van Diemen's Land page disagrees with itself on self-government (1855 or 1856). Hobart (1804) and Launceston (1806) foundations are not on the pages. Furneaux group and Bass Strait islands are below the grid. Norfolk Island moves in and out (1844, 1856); colony-of-norfolk-island now exists.

**colony-of-new-zealand** (1840-05 to 1907-09; 9 pages, four over the budget: Cook Islands, Niue, Chatham Islands and Kermadec pages are one-fact pages). Eleven wars as contests over named districts; the Territorial_evolution_of_New_Zealand page does not exist (URL not found). Stewart Island and the subantarctic islands have no dated acquisition on any page; Tokelau is not dated on any page opened for this dossier. Confiscation under the Settlements Act 1863 (1.5 million hectares) is title, not sovereignty. The Kermadec Islands (letters patent of 18 January 1887) resolve to no cell.

**german-new-guinea** (1884-11 to 1920-12; 2 pages for the colony, 2 for Nauru). Same Papua/New Guinea province split as commonwealth-of-australia (Papua = Central, Gulf, Milne Bay, National Capital District, Northern, Western). The page gives no Anglo-German border on New Guinea or the Solomons line (a gap-filler should open Kaiser-Wilhelmsland, Bismarck Archipelago, German Solomon Islands); the 1884 shape leaves out the North Solomons, dated 1885. Nauru is held from 1906 (the page says the Marshall Islands protectorate 'also included Nauru'); Australian occupation of Nauru 1914 to 1920 and the loss to territory-of-nauru are entered from History of Nauru and Nauru.

**south-seas-mandate** (1920-12 to 1947-07; 4 pages). Seven grid cells. The bypassed garrisons (Truk, Yap, Pohnpei, Kosrae) are not dated on any page (one confidence-1 event). Not on the pages: 17 December 1920 for Japan, the 1922 mandate agreement, an area, the seat after 1932. Peleliu and Angaur resolve to no cell.

**trust-territory-of-the-pacific-islands** (1947-07 to 1994-10; 2 pages). The page is thin: no Security Council date of 2 April 1947, no 1962 date, no nuclear-testing detail. Whether the free-association states are drawn as a US tint is for am-07.

**british-new-guinea** (1884-10 to 1906-09; 2 pages). Dates differ: protectorate 21 October 1884 (Romilly) or 6 November 1884 (flag, and Territorial evolution). Not on the page: the 141 E boundary, area, Samarai, the Torres Strait line.

**colony-of-fiji** (1874-10 to 1970-10; 2 pages). The 1876 'Little War' and the Western Pacific High Commission are not on the page. Capital move 1877 (infobox) or 1882 (text).

**british-solomon-islands-protectorate** (1893-06 to 1978-07; 2 pages). The province split 1893 to 1899 is a reading of the page's island lists. Not on the pages: 6 October 1893, the Ontong Java and Sikaiana limits, the Anglo-German line, Japan's surrender; the occupation pair 1942 to 1945 is confidence 1. Only Guadalcanal is entered as a war.

**german-samoa** (1900-03 to 1920-12; 1 page). Tripartite Convention 2 December 1899 (this page) against 14 November 1899 (British Solomon Islands page).

**gilbert-and-ellice-islands** (1892-05 to 1979-07; 2 pages). Four to five cells at most. The Tuvalu page says the colony 'legally ceased to exist on 1 October 1975'; this dossier keeps the name for the Gilbert part to 12 July 1979 (Gilbert and Ellice Islands page). Japanese occupation ends in November 1943 at Tarawa on the battle page, 1945 in the infobox. The capital history is thin (Ocean Island 1908 to 1941 or 1942; no wartime seat; Tarawa from 1946). Ocean Island and the Line Islands polygons resolve to no cell.

**territory-of-nauru** (1920 to 1968-01; 2 pages). New. The pages disagree on the 1888 protectorate (Marshall Islands on Nauru, New Guinea on History of Nauru), the day of the Japanese landing (25 or 26 August 1942), the mandate year (terms 1920; conferral 1923; 'held control until 1920') and the mandatory (Australia with the United Kingdom and New Zealand as co-trustees). Start is confidence 2. Nauru has no Cliopatria row and no other owner.

**nauru** (1968-01 to 2024; 2 pages). Independence 31 January 1968 on both pages.

**samoa** (1962-01 to 2024; 1 page). The page gives three areas (2,831, 2,842, 2,934 km2). American Samoa has no dossier.

**tuvalu** (1975-10 to 2024; 1 page). Crown colony 1 October 1975, independent 1 October 1978. The page notes the US landing at Funafuti on 2 October 1942 and says nothing of a Japanese occupation of Tuvalu.

**kiribati** (1979-07 to 2024; 1 page). The US relinquished its claims to the Phoenix and Line Islands in the Treaty of Tarawa (September 1979, ratified 1983); the islands are already in the shape, so no gain is entered and the page gives no start year for the claim. Straddles 180 degrees (gazetteer handles the country).

**republic-of-the-marshall-islands** (1986-10 to 2024; 1 page). Starts at the Compact (21 October 1986) to match the trust-territory dossier; self-government is 1 May 1979 and Resolution 683 ended the trusteeship on 22 December 1990. The gazetteer's country shape is two cells near Majuro only, so the western atolls are not drawn.

**cook-islands** (1965-08 to 2024; 1 page) and **niue** (1974-10 to 2024; 1 page). Self-governance 4 August 1965 and 19 October 1974 (plebiscite 3 September 1974); both entered New Zealand's boundaries on 11 June 1901. The 11 June 1980 US maritime treaty relinquished American claims to Penrhyn, Pukapuka, Manihiki and Rakahanga (no gain entered). The Cook Islands shape is the Rarotonga cell only.

**commonwealth-of-the-northern-mariana-islands** (1986-11 to 2024; 1 page). The page gives 1 January and 9 January 1978 for the partly effective Covenant, and 3 or 4 November 1986 for full effect; November 1986 matches the trust-territory dossier. Guam is excluded.

**colony-of-norfolk-island** (1856-11 to 1914-07; 3 pages). Zero grid cells: the dossier is bookkeeping for the chain Tasmania, the colony, Australia. History of Norfolk Island says it was placed under the Commonwealth after 1901 without a date; Territorial evolution and the Norfolk Island page give 1 July 1914.

## Not written, and why

- Samoa 1920 to 1962 is New Zealand's (oc-02-a). American Samoa, Tokelau, Pitcairn, Wallis and Futuna, French Polynesia, New Caledonia after 1859: not covered (other groups or no sources opened).
- Page budget: micro-states have one page each (one to nine cells); history pages (History of Samoa, Kiribati, Tuvalu, the Marshall Islands) would add detail, not borders.
- Non-state belligerents are plain names in `wars` and counterparts (Maori hapu forces, Aboriginal nations, Ballarat miners); none is a state held for ten years, so no dossier is requested.

## Gazetteer names that resolve to no cell

Norfolk Island (country), the Torres Strait polygon, the Kermadec Islands, Peleliu and Angaur, the Ocean Island polygon, the northern Line Islands polygon. Macquarie Island resolves to one cell; Lord Howe Island is below the grid and not drawn. The country shapes Marshall Is. (2 cells), Cook Is., Niue, Nauru, Tuvalu (1 cell each) cannot show the whole state.
