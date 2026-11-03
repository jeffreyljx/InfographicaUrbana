# Lost towers: notes for the ScraperMap "time capsule" slider

Compiled 12 October 2026. This is the companion to `lost-towers.json` in the same folder.

## In one paragraph

I found **15 buildings 150 m or taller that were finished, used, and later destroyed or taken down**. Ten are voluntary demolitions, three were destroyed on 11 September 2001, and two (Deutsche Bank Building, One Meridian Plaza) were dismantled after attack or fire damage. One of them, Tokyo's **Toshiba Building**, is still coming down (demolition started October 2025) and is **already in the site's dataset as a standing tower**, so that row needs to be retired. Three more 150 m+ towers were demolished without ever being finished; they are listed separately below and are not in the JSON. Several near-misses and doubtful cases are explained in the borderline section.

## The main list (what is in `lost-towers.json`)

| # | Building | City | Height (m) | Standing | How it ended |
|---|---|---|---|---|---|
| 1 | World Trade Center North Tower (1 WTC) | New York City | 417.0 | 1972-2001 | destroyed, 9/11 attacks |
| 2 | World Trade Center South Tower (2 WTC) | New York City | 415.1 | 1973-2001 | destroyed, 9/11 attacks |
| 3 | AXA Tower | Singapore | 234.7 | 1986-2022 (cleared 2023) | demolished |
| 4 | Union Carbide Building (270 Park Avenue) | New York City | 215.5 | 1960-2019 (cleared 2021) | demolished |
| 5 | Singer Building | New York City | 186.6 | 1908-1967 (cleared 1968) | demolished |
| 6 | 7 World Trade Center (1987) | New York City | 185.9 | 1987-2001 | destroyed, 9/11 attacks |
| 7 | CPF Building | Singapore | 171.0 | 1976-2017 (cleared 2018) | demolished |
| 8 | Toshiba Building (Hamamatsucho Building) | Tokyo | 167.0 | 1984-2025 (finishes about 2028) | demolished (in progress) |
| 9 | Fuji Xerox Towers | Singapore | 164.9 | 1987-2021 (cleared 2023) | demolished |
| 10 | Morrison Hotel | Chicago | 160.3 | 1925-1965 | demolished |
| 11 | World Trade Center Building | Tokyo | 158.0 | 1970-2021 (cleared 2023) | demolished |
| 12 | Deutsche Bank Building | New York City | 157.6 | 1974-2007 (cleared 2011) | dismantled after 9/11 damage |
| 13 | UIC Building | Singapore | 152.0 | 1974-2012 (cleared 2013) | demolished |
| 14 | One Meridian Plaza | Philadelphia | 150.0 | 1972-1998 (cleared 1999) | dismantled after 1991 fire |
| 15 | Menara Tun Razak | Kuala Lumpur | 150.0 | 1981-2014 | demolished (disputed, see below) |

All six cities already exist in the dataset under exactly these spellings: New York City, Singapore, Tokyo, Chicago, Philadelphia and Kuala Lumpur. Countries use the dataset's names: United States, Singapore, Japan and Malaysia.

### How to read the fields

- **completed** is the CTBUH completion year, which is how the dataset's `year` column works. A few towers were in use earlier; for example, the North Tower had its first tenants in December 1970. The notes give those dates.
- **gone** is the year the tower stopped standing as a building. For a demolition that took several years, I used **the year demolition began**, as the brief asked, and put the year it ended in `demolitionFinished`. For towers destroyed in a single event, `demolitionFinished` is `null`.
- Two towers stood empty and damaged for years before they came down. For those you may prefer an earlier "gone" year:
  - **Deutsche Bank Building:** damaged and closed in 2001, dismantled from 2007.
  - **One Meridian Plaza:** gutted by fire in 1991, dismantled from 1998.

  The JSON uses the year demolition began, and each tower's notes say so.
- **how** takes one of three values:
  - **destroyed:** brought down by an attack or disaster.
  - **demolished:** voluntarily torn down for redevelopment, whatever the method.
  - **dismantled:** taken apart piece by piece because damage had made it unusable.
- **height** uses the CTBUH "height to architectural top" where CTBUH has the building, so it matches the dataset. There are two exceptions or disputes:
  - **7 WTC:** I used 185.9 m (610 ft), the figure in Wikipedia and the NIST investigation, because CTBUH's 173.7 m looks too low. Both are over 150 m.
  - **Tokyo World Trade Center:** sources give 152 m to the top floor, 158 m (CTBUH) and 162.6 m to the roof. I used CTBUH's 158 m.
- **floors** come from CTBUH. Where Wikipedia differs, the notes say so: CPF 45 vs 46, Fuji Xerox 40 vs 38, Menara Tun Razak 37 vs 35.
- **replacedBy** names a tower in the dataset that stands (or is being built) on the same plot. Two cases need care:
  - The **North Tower** is linked to One World Trade Center. They share the WTC site, but One WTC is about 100 m from the old footprint, which is now the memorial's North Pool.
  - The **South Tower** has no successor on its footprint (the South Pool), so `replacedBy` is `null`.

  Replacements not yet in the dataset:
  - **Fuji Xerox Towers:** Newport Plaza.
  - **Tokyo World Trade Center:** the new WTC Main/North Tower (235 m, due 2027).
  - **Toshiba Building:** BLUE FRONT SHIBAURA Tower N.
  - **Deutsche Bank Building:** 5 World Trade Center, which is planned but paused.
  - **Menara Tun Razak:** nothing confirmed.

### Coordinates: how they were obtained

Each tower's `coordSource` field says exactly where its point came from. The approaches, from most to least precise:

- **Official address points.** Singapore's government map service, OneMap, gave points for AXA, CPF and Fuji Xerox. The point is for the street address, and each new building sits on the same plot as the old one.
- **Wikipedia's own coordinates for the lost building:**
  - North and South Towers
  - Tokyo World Trade Center
  - UIC Building
  - Deutsche Bank Building, cross-checked against New York's city tax-lot data
- **CTBUH coordinates already in the dataset:**
  - Toshiba Building
  - One Meridian Plaza, using the Residences at the Ritz-Carlton, which was built on its site
- **Derived from building outlines.** For the Singer Building, 270 Park Avenue and the original 7 WTC, I took New York City's building-outline data and placed the old tower using documented setbacks and dimensions. The 270 Park point lands within about 9 m of Wikipedia's. The Singer point lands about 18 m from Wikipedia's. For 7 WTC, Wikipedia's point sits at the east end of a 100 m-long building, so I moved it to the middle. These points should be good to about 20 m.
- **Estimates with larger uncertainty (about 30 m):**
  - **Morrison Hotel:** placed from its Clark Street address and the US Census address-matching service.
  - **Menara Tun Razak:** the average of two web sources.

## Important: a tower already in the dataset

- **Toshiba Building (dataset id 2949, Tokyo, 167 m, "Completed 1984").** Shimizu began demolishing it on 1 October 2025 and plans to finish in late April 2028. Sources: Kensetsu News (2 Sep 2025), and a Japanese skyscraper blog with photos of the demolition dated May 2026. CTBUH still shows it as completed. The dataset row should be dropped or given an end year, otherwise the tower will appear twice.

None of the other 14 lost towers are in the dataset. I checked by name, by CTBUH id and by distance.

## Never completed, then demolished (kept out of the JSON)

| Building | City | Height | What happened |
|---|---|---|---|
| Mina Plaza Tower 1 (Meena Plaza) | Abu Dhabi, UAE | 168.6 m per CTBUH (Guinness measured 165.0 m); 46 floors | One of four towers begun around 2007. Construction stopped and they were never finished. All four were imploded on 27 Nov 2020, setting a Guinness record for the tallest building demolished with explosives. The other three towers were 127, 127 and 112 m. |
| Torre de la Escollera | Cartagena, Colombia | 206 m planned, topped out early 2007; 58 floors planned | A storm on 13 May 2007 twisted the unbraced steel frame. The tower was dismantled from July to November 2007 and was never finished or occupied. |
| Qilu Hotel Phase II (齐鲁宾馆二期) | Jinan, China | 157 m, 39 floors (CTBUH) | Built from 1992, stopped in 1996 when money ran out, and left an empty shell for more than 20 years (The Paper, 2020). Demolished in 2022, nearly finished by July 2022 (Dazhong Daily), for the Qianfoshan north plaza. CTBUH lists it as "completed 1997, demolished 2022", but Chinese reporting says it was never finished or used, so I left it out of the main list. |

## Borderline cases

**Included, but close to the 150 m line:**

- **One Meridian Plaza:** 150.0 m exactly (CTBUH and Wikipedia agree).
- **Menara Tun Razak:** 150.0 m exactly (CTBUH and Wikipedia agree). Its *status* is also uncertain; see the doubts section.
- **UIC Building:** 152.0 m (CTBUH, Straits Times and Wikipedia agree).

**Left out:**

- **City Investing Building** (New York City, 1908-1968): 148.1 m (486 ft) per CTBUH, so just under 150 m. It wrapped around the Singer Building and was demolished with it for One Liberty Plaza. If you relax the cut-off, its location is roughly the middle of today's One Liberty Plaza block (about 40.7097, -74.0109).
- **Crowne Plaza Mutiara KL** (Kuala Lumpur, formerly the KL Hilton, 1973, 36 floors, closed 2 January 2013, demolished 2013). CTBUH says 150.3 m. Other sources disagree:
  - Wikipedia's Kuala Lumpur list gives 130 m and Wikipedia's demolished-buildings list gives 105 m.
  - CTBUH's own 2018 "Tallest Demolished Buildings" top ten did not include it, although a 150.3 m tower demolished in 2013 would have ranked sixth.
  - For a 36-storey hotel, 130 m is the more believable figure.

  I treated it as probably under 150 m. If you would rather follow CTBUH, the site is the former Crowne Plaza/Kompleks Antarabangsa plot on Jalan Sultan Ismail (Tradewinds Square site, about 3.1518, 101.7112). That point is only good to about 50 m because the plot also held a second building.
- **Comcentre** (Singapore, 1979-81, demolished about 2023-24): 140 m to the roof and 145 m with its spire (Wikipedia; 33 storeys per Singapore's heritage site, Roots). A Straits Times chart gave 165 m, which looks like an error.
- **Old St Paul's Cathedral** (London): CTBUH lists it as a demolished "building" at 150.3 m (completion 1240, demolished 1666). The height was its medieval spire, estimated at 149-160 m, which fell after a lightning strike in 1561; the cathedral burned in 1666. It is pre-modern and the height is uncertain, so I left it out.
- **Trylon** (New York World's Fair, 1939-1940, 185.9 m): CTBUH files it as a demolished "building" but its function is "statue". It was a hollow steel spire with no floors, so it is not a building.

**Near misses for context (all under 150 m, all demolished):**

- Mizuho Bank Uchisaiwaicho HQ, Tokyo: 143 m (2023)
- Ritz-Carlton Hong Kong: 142 m (2009)
- Grand Prince Hotel Akasaka, Tokyo: 140-141 m (2013)
- Hennessy Centre, Hong Kong: 140 m (2008)
- Funkhaus, Cologne: 138 m (2019)
- Shaw Tower, Singapore: 134-138 m (2020)

## Doubts and open questions

1. **Menara Tun Razak** is the least certain entry. CTBUH, both on its building page and in its 2018 study where it ranked seventh, and Wikipedia say it was demolished in 2014. Against that:
   - In 2010 and 2012, owner Tradewinds announced it would *refurbish* the tower and add a second one.
   - Malaysia's workplace-safety department described the January 2014 fire as happening during renovation.
   - A SkyscraperCity thread is titled "Menara Tun Razak 2 & refurbished Menara Tun Razak 1 (50 fl & 26 fl)".

   It may have been taken down, or cut down to 26 floors, but I could not confirm which. Checking satellite or street imagery of Jalan Raja Laut would settle it. I could not find exact demolition dates either.
2. **Toshiba Building** is still partly standing. If the slider should show it until it is physically gone, use 2028 (the planned finish) instead of 2025.
3. **Height disagreements, none of which affect inclusion:**
   - Tokyo World Trade Center: 152, 158 or 162.6 m
   - 7 WTC: 173.7 or 185.9 m
   - Deutsche Bank Building: 157.6 or 163 m
4. **Completion-year disagreements:**
   - UIC Building: 1973 or 1974
   - Menara Tun Razak: 1981 or 1983
   - CPF Building: finished demolition 2017 or 2018
   - Singer Building: site cleared 1968 or early 1969
5. **Morrison Hotel's exact position** on its block is estimated (within about 30 m), because I found no plan showing where the 1925 tower stood.

## Coming up: demolitions to watch (still standing, still in the dataset)

- **Renaissance Center 300 and 400 Towers, Detroit** (dataset ids 3690 and 3691, 155 m each). GM and Bedrock plan to demolish them; demolition "could begin by summer 2027" (GM Authority, July 2026).
- **Plaza Tower, New Orleans** (dataset id 3219, 161.9 m). Empty since 2002; a judge cleared the way for demolition in January 2025, but it was still standing in August 2026.

## How I searched

**Starting points:**

- Wikipedia's "List of tallest voluntarily demolished buildings".
- Reporting on CTBUH's 2018 study "Tallest Demolished Buildings", via Building Design + Construction, Construction Junkie and The Urban Developer.
- The Guinness record for the tallest building demolished with explosives.
- The Straits Times' November 2024 feature on Singapore's skyscraper demolitions.

**The key step** was CTBUH's own database. Its "Explore Data" page, filtered to status *Demolished* and height 150 m and over, returned 17 entries:

- 13 of the 15 towers in the table above. The other two, Toshiba and Tokyo WTC, are missing because CTBUH still shows both as "Completed".
- Qilu Hotel, Crowne Plaza Mutiara, Old St Paul's and Trylon, which are discussed above.

I then checked each candidate individually on its CTBUH page and on Wikipedia, and looked for towers CTBUH has not yet updated. That is how the Tokyo WTC and the Toshiba Building turned up. Checking the older pre-1990 towers in the dataset for Tokyo, Singapore, Hong Kong, Osaka and Kuala Lumpur found no other demolitions; Singapore's Hong Leong Building is being refurbished, not demolished.

**Regions searched with nothing found at 150 m or over** (beyond the cases above):

- **Mainland China:** Chinese-language searches. The tallest completed building demolished there seems to be Xi'an's 118 m Jinhua Building; Changsha's China Telecom tower burned in 2022 but was not demolished.
- **Hong Kong:** the tallest demolished is the Ritz-Carlton at 142 m.
- **Japan** beyond the two Tokyo entries.
- **Malaysia** beyond the two Kuala Lumpur cases.
- **The Gulf and Saudi Arabia,** including the Mecca hotel clearances.
- **Russia and Europe:** the tallest demolished in Europe is Cologne's 138 m Funkhaus.
- **Latin America:** the only 150 m+ case is the unfinished Torre de la Escollera.
- **Australia:** the tallest demolished is 128 m.
- **Africa and India:** the Noida twin towers were 103 m and unfinished.

No other building of 150 m or more was destroyed by war, fire or earthquake. Fire-damaged towers such as Changsha's China Telecom tower, Dubai's Torch, Caracas's Parque Central and Beijing's TVCC were all repaired.

**Sources I could open:**

- Wikipedia (English and Japanese).
- skyscrapercenter.com building, complex and explore-data pages.
- SkyscraperPage building pages.
- Singapore OneMap.
- New York City's GeoSearch geocoder and its open-data building-footprint and tax-lot records.
- The US Census geocoder.
- Guinness World Records.
- News sites: Straits Times via Truescope, Kensetsu News, the Dazhong Daily (dzwww), The Paper (thepaper.cn), The Star, Philly YIMBY, Chicago YIMBY, GM Authority and Mingtiandi.
- Nomura Real Estate press releases.
- Structurae.

**Sources I could not open:**

- OpenStreetMap's Nominatim and Overpass services, blocked by their robots rules.
- skyscrapercenter.com's map pages (robots rules).
- Direct command-line downloads from skyscrapercenter.com and OneMap, refused by the proxy. The same pages worked through the web-fetch tool.
- Several Chinese news pages (gmw.cn, 163.com, lmjx.net).
- SkyscraperCity forum threads.
- The Malaysian Reserve and Berita Harian.
- The Malay Wikipedia article on Menara Tun Razak (not found).

Where a page would not open I relied on search-result snippets and other sources, as noted above.
