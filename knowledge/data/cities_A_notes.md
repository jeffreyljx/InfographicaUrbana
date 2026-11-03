# Cities A: Toronto, Moscow, Sydney, Singapore — completed buildings >= 150 m by sub-district

Compiled 2026-09-05. Primary source: en.wikipedia "List of tallest buildings in <city>" (all four tables use a 150 m cutoff); status of borderline/2026-dated rows checked against skyscrapercenter.com (CTBUH) building/complex pages and local news. Heights are architectural heights as given by Wikipedia (CTBUH value noted where it differs). "Completed" = completed as of Sept 2026; rows with status `topped_out` / `under_construction` / `not_complete` are kept in the CSVs but excluded from the totals below.

CSV columns: `name,height_m,floors,year,district_or_area,source_url,confidence,status,notes` (spec columns plus `status` and `notes`).

---

## 1. Toronto — `toronto_150m.csv` (117 rows; 111 completed)

| Area | >= 150 m | >= 200 m |
|---|---|---|
| **Old Toronto** (pre-1998 city: downtown, waterfront, Yorkville, Church-Wellesley, Yonge-Eglinton midtown, Yonge-St Clair) | **102** | **31** |
| Etobicoke (Humber Bay Shores x7, Six Points/Pinnacle Etobicoke x1) | 8 | 1 (Eau du Soleil Sky Tower) |
| North York (Hullmark Centre I, North York Centre) | 1 | 0 |
| Scarborough / York / East York | 0 | 0 |
| **City of Toronto total** | **111** | **32** |

- Mississauga / Vaughan / Pickering are not in the Wikipedia Toronto table (they're in a separate GTA table), so none are included.
- Excluded as not completed (6): SkyTower at Pinnacle One Yonge (CTBUH: structurally topped out), One Bloor West (topped out, 2028), One Delisle (2027), 400 King West (CTBUH: structurally topped out), Kipling Station Condos (topped off Sept 2026), Alias (under construction). This matches the page's own statement "111 completed skyscrapers taller than 150 m as of 2026, 32 over 200 m".
- Gap vs CTBUH (109 / 32): +2 at 150 m+. Most likely CTBUH still files CIBC Square II (opened 4 June 2026; CTBUH page still "Under Construction") and one 2025/26 condo (Burke, The Charles at Church or similar) as not complete. 200 m+ matches exactly.
- Yonge-Eglinton buildings (E Condos South, 2221 Yonge, Quantum 2, E2 at E Place) are counted as Old Toronto: the former City of Toronto extended north past Eglinton to roughly Lawrence/Blythwood.
- Possible omission: Manulife Centre (55 Bloor W, 51 fl, 1974) is not in the Wikipedia 150 m table; some databases list it near 155-157 m. Not counted.
- Old Toronto at 200 m+ (31): all the downtown/Yorkville towers from First Canadian Place down to YC Condominiums, minus SkyTower and One Bloor West (not complete) and minus Eau du Soleil (Etobicoke).

## 2. Moscow — `moscow_150m.csv` (137 rows; 104 completed strictly, 118 incl. rows dated 2026)

| Area | >= 150 m | >= 200 m |
|---|---|---|
| **Presnensky District** (Moscow-City/MIBC 23 + Headliner x4, Presnya City x3, Kudrinskaya Square Bldg, iCity Time) | **28** | **18** |
| Rest of Moscow (completed, year <= 2025) | 76 | 7 |
| Rest of Moscow, additionally rows Wikipedia dates 2026 (status unverified) | +14 | +3 |
| **City total** | **104 (118 incl. 2026 rows)** | **25 (28)** |

- Presnensky 200 m+ (18): Federation East & West, OKO South & North, Neva Towers 1 & 2, Mercury, Eurasia, City of Capitals Moscow & St Petersburg, Capital Towers River/City/Park, Moscow Towers (= CTBUH "Grand Tower", 283 m), Naberezhnaya Tower C, iCity Space Tower, Evolution, Imperia. Presnensky 150-200 m (10): IQ-quarter Tower 2, Headliner Towers 1/4/6/8, Presnya City 1/2/3, Kudrinskaya Square Building (1954), iCity Time Tower (150 m, borderline).
- Other 200 m+ completed outside Presnensky: National Space Center (Filyovsky Park), Triumph Palace, MSU main building, House on Mosfilmovskaya 1, Hotel Ukraina, MOD Towers 3 & 7 (200 m). With 2026 rows: Five Towers (274, Donskoy), Level Yuzhnoportovaya 1 (224.4), Obrucheva 30 Tower 1 (200).
- Gap vs CTBUH (70 / 27): Wikipedia's table (137 rows, "as of June 2026") includes dozens of recent residential complexes counted tower-by-tower (City Bay, Sky Garden, Hide, Nebo, Will Towers, Sobytye, Sydney City, Wellton, Savyolovskiy City, Avenue 77, etc.) that CTBUH either does not have in its database, lists below 150 m, or has not yet marked completed; it also carries rows dated 2026-2027 in the "completed" table with no status column (19 rows dated 2027 excluded; 14 dated 2026 flagged `listed_2026`). CTBUH's 27 at 200 m+ vs my 25-28 is consistent. The Presnensky 200 m+ count (18) is robust; the 150 m+ figure (28) depends on whether CTBUH counts the Headliner/Presnya City towers and the borderline iCity Time Tower.
- Naberezhnaya Towers A/B, Northern Tower, IQ-quarter Towers 1/3 and Afimall are all below 150 m and correctly absent. The MIBC article mentions a second Imperia tower (171 m, 2019) which is NOT in the tallest-buildings list; not counted (low confidence it exists at that height).

## 3. Sydney — `sydney_150m.csv` (63 rows; 55 completed)

| Area | >= 150 m | >= 200 m |
|---|---|---|
| **Sydney CBD / City of Sydney LGA** (CBD 30 + Barangaroo 6 + Haymarket 1 + Darling Harbour 0 completed) | **38** | **15** |
| North Sydney | 5 | 0 |
| Chatswood | 2 | 0 |
| St Leonards | 1 | 0 |
| Rhodes | 1 | 0 |
| Macquarie Park (Trilogy A/C topped out only) | 0 | 0 |
| Greater Sydney excl. Parramatta | 47 | 15 |
| **Parramatta CBD** (incl. Paramount on Parkes, Harris Park) | **8** (7 by CTBUH heights) | **2** |
| **Total** | **55** | **17** |

- KEY FINDING: CTBUH files Parramatta as a separate "city" (skyscrapercenter.com/city/parramatta). The CTBUH Sydney total of 47 / 15 therefore EXCLUDES Parramatta, and my Sydney-excluding-Parramatta count is exactly 47 / 15. North Sydney, Chatswood, St Leonards and Rhodes are inside CTBUH "Sydney" (no separate North Sydney page).
- Parramatta 150 m+: 6 & 8 Parramatta Square (225/223.3), 180 George St North (213), 180 George St South (189), Altitude West/Tower A (177), 4 Parramatta Square (158), Paramount on Parkes (158; CTBUH 157.4, completed), HOME Parramatta = CTBUH "116 Macquarie Street" (156.4), The Lennox (Wikipedia 152 m but CTBUH 148.6 m — counted here, flagged). 8 Phillip Street (218 m) is architecturally topped out per CTBUH (completion 2026) — excluded; it will make Parramatta 9 / 3 when done.
- Excluded as not complete (8): 55 Pitt Street, One Circular Quay, Atlassian Central, Chifley South, Harbourside Residences (all CBD, topped out), 8 Phillip Street, Trilogy Towers A & C.
- Victoria Cross Tower (North Sydney) is "topped out" in the list but its own article says completed 2025; counted.
- Borderline heights flagged (Wikipedia vs CTBUH may differ): The Cove 158, Sydney Central 152, 85 Castlereagh 151, Lumiere 151, Hordern Towers 156, Meriton Tower 170.

## 4. Singapore — `singapore_150m.csv` (126 rows, all completed)

| URA planning area | >= 150 m | >= 200 m |
|---|---|---|
| **Downtown Core** (Raffles Place, Shenton Way/Cecil/Robinson, Tanjong Pagar, Anson, Marina Bay/Bayfront, Marina Centre/Suntec, City Hall/Beach Rd, Bugis) | **77** | **35** |
| Queenstown (Dawson HDB x12, Commonwealth Towers x2, Margaret Ville, Mapletree Business City II) | 16 | 0 |
| Bukit Merah (Reflections at Keppel Bay x3, Avenue South x2, Echelon x2, Ascentia Sky, Artra, Spottiswoode Suites, mTower) | 11 | 0 |
| Outram (Pinnacle@Duxton x7, State Courts Towers) | 8 | 0 |
| Orchard (Orchard Residences, Boulevard Vue, Skyline@Orchard Blvd, Scotts Square, Hilton Orchard T2, TwentyOne Anguilla Park) | 6 | 1 |
| Newton (Nouvel 18 x2, Scotts Tower, Sculptura Ardmore) | 4 | 0 |
| Kallang (The Concourse, Concourse Skyline) | 2 | 0 |
| River Valley (New Futura x2) | 2 | 0 |
| Marina South, Novena, Toa Payoh, Rochor, Museum, Tanglin | 0 | 0 |
| **Total** | **126** | **36** |

- Gap vs CTBUH (102 / 35): 200 m+ matches within 1 (CTBUH measures Republic Plaza 276.3, CapitaSpring 276, OUB Centre 277.8 etc. — OUE Downtown 1 at 201 m or one of the 207 m MBS towers may be treated differently). The 150 m+ gap (+24) is almost entirely public housing and borderline rows: SkyOasis/SkyResidence/SkyParc @ Dawson (12 HDB blocks, 151-158 m) and possibly the 7 Pinnacle@Duxton blocks (Wikipedia 160-163 m; the Pinnacle article gives roof height 156 m) are unlikely to all be in CTBUH; plus six rows at exactly 150 m (Gateway East/West, Lippo Centre, OUE Downtown 2, Concourse Skyline, Sculptura Ardmore). Removing the Dawson blocks and the 150 m rows gives 108, close to 102.
- Downtown Core count without the borderline 150 m rows: 73.
- Location assignment notes (Wikipedia table has no location column; assigned from known addresses):
  - DUO Tower/Residences (Ophir-Rochor site) assigned Downtown Core (Bugis subzone) — medium confidence; sits on the Downtown Core/Rochor/Kallang boundary.
  - Pinnacle@Duxton and State Courts appear in the Outram planning-area article's photo montage — Outram. (Task hint said Outram — confirmed at medium confidence.)
  - The Concourse is named in the Kallang planning-area article — Kallang; Concourse Skyline next door also Kallang.
  - mTower (PSA Building, 460 Alexandra Rd) — Bukit Merah, low confidence (Bukit Merah/Queenstown boundary near Labrador Park).
  - Ardmore Park / Anderson Rd towers (Sculptura Ardmore, Nouvel 18) — Newton's Orange Grove subzone; Scotts Tower (38 Scotts Rd) — Newton; Scotts Square (6 Scotts Rd) — Orchard, medium.
  - TwentyOne Anguilla Park — Orchard (Boulevard subzone), low confidence; could be Tanglin.
- Not in the Wikipedia table (so not counted): SkyVille@Dawson / SkyTerrace@Dawson (47 fl, probably <150 m), 8 Shenton Way redevelopment (under construction, 299.7 m), One Bernam, Marina View Residences (UC).

---

## Headline

| Target area | >= 150 m | >= 200 m |
|---|---|---|
| Old Toronto | 102 | 31 |
| Presnensky District (Moscow) | 28 | 18 |
| Sydney CBD (City of Sydney LGA) | 38 | 15 |
| Parramatta CBD | 8 (7 by CTBUH heights) | 2 |
| Singapore Downtown Core | 77 | 35 |
| Singapore other planning areas | Queenstown 16, Bukit Merah 11, Outram 8, Orchard 6 (1 at 200+), Newton 4, Kallang 2, River Valley 2 | |

## Tooling notes
- en.wikipedia.org fetches are cache-served; en.m.wikipedia.org and several article pages (DUO, The Concourse) were not fetchable. skyscrapercenter.com building/complex pages work (one 403: One Delisle). WebSearch budget was exhausted near the end of the run, so the last few Singapore boundary checks were done via the planning-area Wikipedia articles instead of individual building pages.
