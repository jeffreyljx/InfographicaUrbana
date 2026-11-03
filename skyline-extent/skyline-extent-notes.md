# Skyline extent: every dense pocket of skyscrapers

Rule changed on 11 Oct 2026, in two rounds. Jeffrey first noticed that La Défense, London, Frankfurt and downtown Los Angeles had no extent while all of Moscow's historic centre was highlighted. Later that day he asked for central Kwai Chung, central Bao'an, Taipei's Xinyi and Ningbo's downtown, and said Chicago and Toronto (North York and the Yonge corridor) were drawn a little strictly. The first version (9 Oct, the one live on the site) drew hand-made cores for the 38 cities with more than 50 towers. This version uses one density rule everywhere, so any dense pocket gets an extent in any city. The polygons are in [skyline-extent.geojson](skyline-extent.geojson), with the same properties as before. The 9 Oct file is kept as [skyline-extent-2026-10-09.geojson](skyline-extent-2026-10-09.geojson). [density-rule-check.png](density-rule-check.png) shows the cities Jeffrey named against what is live.

## The rule

- **Towers.** Every tower of 150 m+ in the master list (`skyscrapers_150m_master_geocoded.csv`, 8,076 rows, all statuses, cities merged as on the site). The per-city CSVs were not touched.
- **Dense spot.** A tower is in a dense spot when at least four towers, itself included, stand within 800 m of it. Towers within 800 m of a tower in a dense spot join its group. This is DBSCAN with eps 800 m and min_samples 4 on great-circle distance.
- **Pocket.** A group of 5 or more towers is a pocket, and every pocket gets an extent wherever it is. A city gets one area per pocket. The first round used 10; 5 is what brings in Kwai Fong, Ningbo, most of Seoul and the neighbourhoods of Changsha IFS, Suzhou IFS and Wuhan CTF (see the threshold lever below).
- **Old downtowns.** No exceptions. A traditional centre is highlighted only if its own towers form a pocket. That is the one consistent answer: the highlight shows where the skyscrapers are, not where the historic centre is.
- **Outline.** It runs 300 m out from each pocket tower and closes gaps of up to about 1.9 km between towers (a 650 m closing). Rivers, harbours and the sea are cut out, and the shape is smoothed by 70 m. Parts smaller than 0.04 km² or holding no tower are dropped.
- **Waterfront fill.** Land up to about 600 m wide between the outline and the river, lake or sea it faces is taken in, because a skyline runs down to its waterfront: Chicago now reaches Grant Park and the lakefront, San Francisco the Embarcadero. Three kinds of land stay out:
  - piers and other land under about 300 m wide with water on both sides (Navy Pier);
  - landfill that juts out into the water and meets the outline only through a narrow neck (Chicago's water filtration plant north of Navy Pier);
  - spurs under about 300 m wide that would reach out from the outline toward a pond, a river bend or the tip of a dock (Kolkata, Montreal, Downtown Brooklyn).
- **Counts.** "In core" counts every tower inside the polygon, of any status, including a few outliers that sit inside the outline without being part of a pocket. "Completed" and "tallest" count completed towers only.

The result is 325 pockets in 128 cities, holding 5,907 of the 8,076 towers, and 710 km² of extent in all (the live version has 574 km² in 38 cities).

## Jeffrey's points of 11 Oct

1. **Central Kwai Chung.** Kwai Fong (Metroplaza and its neighbours) is a pocket of five towers, so it is in now. Under the first round's 10-tower rule it was too small.
2. **Central Bao'an.** Bao'an Centre (Xin'an, 22 towers) was already in after the first round, and Xixiang's Hongfa group (7) joins it now.
3. **Taipei.** Xinyi (10 towers, Taipei 101 included) was already in after the first round. The three towers around Taipei Main Station are too few to count.
4. **Ningbo.** Four pockets now: Eastern New Town around Ningbo Center (9), Sanjiangkou (5), Jiangbei's Old Bund (5) and the Southern Business District in Yinzhou (5).
5. **Chicago.** The same 136 towers, but the outline now runs down to the lakefront and takes in Grant Park (waterfront fill above). Navy Pier and the water plant stay out.
6. **Toronto.** Yonge and Eglinton (5 towers) is a pocket now. North York Centre has only two towers of 150 m+ (Hullmark Centre and 4800 Yonge, under construction) and St Clair has one (One Delisle), so neither can form a pocket; most of the Yonge corridor's towers are under 150 m and are not in the master list. Downtown still reaches Bloor and Yorkville.

## What changed from the live 9 Oct version

- **90 cities added.** They include London (Canary Wharf; the City and London Bridge; Nine Elms and Vauxhall), Paris (La Défense), Frankfurt (Bankenviertel), Los Angeles (Downtown and Century City), Taipei (Xinyi) and Ningbo. The table marks each one "new".
- **Moscow.** Moscow City and Savyolovsky (D1 and Graphite) instead of the Garden Ring. The Garden Ring holds two towers of 150 m+ (Kotelnicheskaya Embankment and Repin), so it was never dense. It was in only because the first version kept traditional downtowns.
- **Old downtowns.** Seoul's old centre (Jongno-gu and Jung-gu) holds three towers and drops out, as does Jamsil, where Lotte World Tower stands alone. Teheran-ro stays as two pockets (Gangnam station and Samseong), and Mokdong, Seongsu, Ilsan, Gwangmyeong and Konkuk University station join. South Mumbai's Nariman Point and Cuffe Parade hold one tower of 150 m+ and drop out, while Tardeo and Malabar Hill (7 towers) stay. Guangzhou's Yuexiu keeps Beijing Road and Haizhu Square, and Huanshi East Road (5 towers) stays too.
- **Lone supertalls.** Changsha IFS, Suzhou IFS and Wuhan CTF are now inside pockets. Lotte World Tower and Abeno Harukas still stand alone and stay out.
- **Hong Kong** gains its new towns and smaller groups: Tseung Kwan O, LOHAS Park, Tsuen Wan, Sha Tin and Tai Wai, Tung Chung, Tuen Mun, Tin Shui Wai, Yuen Long, Tsing Yi, Kai Tak, Quarry Bay and Kwai Fong among them.
- **Shenzhen** has 19 pockets, from Nanshan and Futian to Bao'an, Qianhai, Longhua and Pingshan. Most of Shennan Boulevard between Futian and Nanshan is too thin to join them.
- **Areas.** The outline hugs the towers, so some of the original 38 cities are smaller than live even when they hold more towers (Shenzhen 82.8 to 66.4 km², New York 28.7 to 17.5 km², Seoul 13.6 to 8.6 km², Moscow 19.4 to 2.8 km²). Cities with many small pockets grow (Hong Kong 21.8 to 43.0 km²). This changes the Skyline size column.

## The threshold lever

The pocket size of 5 is the one number that decides most of this. DBSCAN groups below 5 always have exactly 4 towers.

- **At 4** every dense spot would count: 89 more pockets and 12 more cities (Baltimore, Caracas, Huzhou, Milwaukee, Monterrey, Nashville, New Orleans, Phnom Penh, Portland, Urumqi, Vienna and Yantai). Tokyo's Shibuya and North Sydney would come in.
- **At 6** there would be 56 fewer pockets and 14 fewer cities (Auckland, Cleveland, Columbus, Fortaleza, Goiânia, Itapema, Kunming, Liuzhou, Madrid, New Alamein City, Perth, Rizhao, Shijiazhuang and Tampa), and Kwai Fong and three of Ningbo's four pockets would drop out again.
- **At 10** (the first round) there were 150 pockets in 75 cities.

Each city that newly qualifies needs its rivers and coastline fetched before it can be built (see [tools/README.md](tools/README.md)).

## Known quirks

- For the 90 added cities, and for Hong Kong and Shenzhen pockets outside their first-version bboxes, water is stored only within about 650 m of the pockets (`tools/water_new.json`). A later change that moves an outline further out needs a fresh water fetch for that city.
- Where two pockets sit less than about 1.9 km apart, the outline can join them into one shape, as with Tokyo's central business districts. The Midtown outline covers the southern 0.45 km² of Central Park, because towers line Central Park South.
- Low-rise blocks between two parts of one city's extent stay out, like Beacon Hill and the Public Garden between Downtown Boston and Back Bay. Only gaps that the outline fully encloses are filled.


## The 128 cities

Ordered by the number of towers in the city. "Live" gives the 9 Oct towers in core and area, or "new" for a city added on 11 Oct.

| # | City | Towers in core / city | Share | Area (km²) | Live | Pockets | Tallest completed in core |
|---|---|---|---|---|---|---|---|
| 1 | Hong Kong | 540 / 576 | 94% | 42.96 | 197 towers, 21.83 km² | 22 | International Commerce Centre (484 m) |
| 2 | Shenzhen | 467 / 536 | 87% | 66.37 | 374 towers, 82.81 km² | 19 | Ping An Finance Center (599 m) |
| 3 | New York City | 325 / 337 | 96% | 17.51 | 328 towers, 28.68 km² | 4 | One World Trade Center (541 m) |
| 4 | Dubai | 300 / 321 | 94% | 23.19 | 279 towers, 19.61 km² | 4 | Burj Khalifa (828 m) |
| 5 | Guangzhou | 168 / 233 | 72% | 21.24 | 144 towers, 25.77 km² | 9 | Guangzhou CTF Finance Centre (530 m) |
| 6 | Kuala Lumpur | 164 / 229 | 72% | 18.33 | 125 towers, 12.66 km² | 5 | Menara Merdeka Maybank (679 m) |
| 7 | Wuhan | 176 / 224 | 79% | 33.55 | 157 towers, 41.49 km² | 13 | Wuhan Greenland Center (476 m) |
| 8 | Shanghai | 162 / 210 | 77% | 25.36 | 155 towers, 28.17 km² | 7 | Shanghai Tower (632 m) |
| 9 | Tokyo | 163 / 190 | 86% | 26.33 | 146 towers, 20.2 km² | 4 | Mori JP Tower (327 m) |
| 10 | Chongqing | 97 / 152 | 64% | 10.62 | 88 towers, 13.98 km² | 5 | Raffles City Chongqing T3N (354 m) |
| 11 | Toronto | 141 / 148 | 95% | 11.86 | 110 towers, 7.45 km² | 5 | First Canadian Place (298 m) |
| 12 | Chengdu | 104 / 143 | 73% | 14.05 | 100 towers, 16.85 km² | 4 | Chengdu International Finance Square Tower 1 (247 m) |
| 13 | Chicago | 136 / 139 | 98% | 8.24 | 136 towers, 7.63 km² | 1 | Willis Tower (442 m) |
| 14 | Metro Manila | 124 / 139 | 89% | 16.53 | 113 towers, 11.37 km² | 5 | Park Central North Tower (276 m) |
| 15 | Bangkok | 100 / 136 | 74% | 18.72 | 104 towers, 24.04 km² | 3 | Magnolias Waterfront Residences Tower 1 (315 m) |
| 16 | Mumbai | 98 / 120 | 82% | 17.22 | 78 towers, 22.29 km² | 6 | Lokhandwala Minerva (301 m) |
| 17 | Jakarta | 101 / 118 | 86% | 13.07 | 83 towers, 12.21 km² | 3 | Autograph Tower (383 m) |
| 18 | Seoul | 80 / 117 | 68% | 8.59 | 45 towers, 13.55 km² | 10 | Parc1 Tower I (322 m) |
| 19 | Hangzhou | 85 / 110 | 77% | 8.46 | 78 towers, 7.96 km² | 3 | Greenland Hangzhou Century Center South Tower (304 m) |
| 20 | Singapore | 93 / 104 | 89% | 8.91 | 83 towers, 5.71 km² | 3 | Guoco Tower (284 m) |
| 21 | Miami | 96 / 103 | 93% | 7.57 | 82 towers, 5.33 km² | 3 | Panorama Tower (252 m) |
| 22 | Changsha | 77 / 99 | 78% | 13.97 | 60 towers, 13.82 km² | 9 | Changsha IFS Tower T1 (452 m) |
| 23 | Nanjing | 60 / 86 | 70% | 8.22 | 62 towers, 12.37 km² | 4 | Zifeng Tower (450 m) |
| 24 | Nanning | 61 / 82 | 74% | 6.23 | 53 towers, 6.99 km² | 6 | Guangxi China Resources Tower (403 m) |
| 25 | Melbourne | 79 / 81 | 98% | 4.99 | 79 towers, 4.61 km² | 1 | Australia 108 (317 m) |
| 26 | Busan | 56 / 77 | 73% | 6.16 | 51 towers, 5.98 km² | 5 | LCT The Sharp Landmark Tower (412 m) |
| 27 | Shenyang | 66 / 75 | 88% | 6.44 | 72 towers, 12.64 km² | 3 | Forum 66 Tower 1 (351 m) |
| 28 | Moscow | 28 / 73 | 38% | 2.77 | 25 towers, 19.35 km² | 2 | Federation Tower (374 m) |
| 29 | Beijing | 56 / 69 | 81% | 7.5 | 33 towers, 5.35 km² | 3 | CITIC Tower (528 m) |
| 30 | Tianjin | 55 / 69 | 80% | 9.12 | 47 towers, 10.04 km² | 4 | Tianjin Modern City Office Tower (338 m) |
| 31 | Panama City | 60 / 68 | 88% | 5.26 | 63 towers, 6.05 km² | 2 | JW Marriott Panama (284 m) |
| 32 | Sydney | 54 / 64 | 84% | 5.1 | 50 towers, 3.63 km² | 2 | One Barangaroo (271 m) |
| 33 | Suzhou | 33 / 60 | 55% | 4.93 | 19 towers, 2.97 km² | 4 | Suzhou IFS (450 m) |
| 34 | Zhuhai | 33 / 60 | 55% | 5.28 | 42 towers, 7.93 km² | 2 | Hengqin International Finance Center (338 m) |
| 35 | Istanbul | 22 / 59 | 37% | 3.23 | 38 towers, 9.55 km² | 2 | Central Bank of the Republic of Türkiye (354 m) |
| 36 | Doha | 43 / 56 | 77% | 4.15 | 43 towers, 3.94 km² | 1 | Kempinski Residences and Suites (253 m) |
| 37 | Dalian | 49 / 52 | 94% | 8.0 | 50 towers, 8.81 km² | 2 | Eton Place Dalian Tower 1 (383 m) |
| 38 | Osaka | 33 / 51 | 65% | 6.99 | 41 towers, 10.23 km² | 1 | The Kitahama (209 m) |
| 39 | Incheon | 42 / 50 | 84% | 4.05 | new | 3 | Northeast Asia Trade Tower (305 m) |
| 40 | London | 43 / 49 | 88% | 4.03 | new | 3 | The Shard (306 m) |
| 41 | Tel Aviv | 41 / 49 | 84% | 4.71 | new | 2 | Moshe Aviv Tower (244 m) |
| 42 | Jinan | 36 / 48 | 75% | 5.66 | new | 2 | Ping An Finance Center (360 m) |
| 43 | Abu Dhabi | 41 / 46 | 89% | 7.7 | new | 5 | Burj Mohammed Bin Rashid (381 m) |
| 44 | Xi’an | 17 / 46 | 37% | 1.9 | new | 2 | Glory・Xi’an International Financial Center (350 m) |
| 45 | Balneário Camboriú | 45 / 45 | 100% | 4.73 | new | 1 | Yachthouse by Pininfarina Tower 2 (294 m) |
| 46 | Xiamen | 21 / 45 | 47% | 3.65 | new | 3 | Xiamen Cross Strait Financial Centre (344 m) |
| 47 | Hefei | 15 / 45 | 33% | 3.39 | new | 2 | China Resources Center 2 (280 m) |
| 48 | Guiyang | 20 / 44 | 46% | 2.49 | new | 3 | Guiyang International Financial Center T1 (401 m) |
| 49 | Foshan | 17 / 44 | 39% | 3.08 | new | 2 | Foshan Entrepreneur Tower (250 m) |
| 50 | Houston | 31 / 40 | 78% | 2.01 | new | 1 | JPMorgan Chase Tower (305 m) |
| 51 | Nanchang | 12 / 40 | 30% | 1.98 | new | 2 | Jiangxi Nanchang Greenland Central Plaza, Parcel A (303 m) |
| 52 | Qingdao | 28 / 37 | 76% | 4.56 | new | 2 | Qingdao Hai Tian Center (369 m) |
| 53 | Kunming | 5 / 37 | 14% | 0.79 | new | 1 | China Overseas International Center (220 m) |
| 54 | Mexico City | 16 / 34 | 47% | 2.27 | new | 2 | Torre Reforma (246 m) |
| 55 | Los Angeles | 32 / 33 | 97% | 3.53 | new | 2 | Wilshire Grand Center (335 m) |
| 56 | Riyadh | 27 / 33 | 82% | 3.76 | new | 4 | PIF Tower (385 m) |
| 57 | Macau | 25 / 32 | 78% | 3.38 | new | 3 | Grand Lisboa (258 m) |
| 58 | Wuxi | 17 / 31 | 55% | 2.64 | new | 2 | Wuxi International Finance Square (339 m) |
| 59 | Vancouver | 19 / 28 | 68% | 3.64 | new | 3 | Two Gilmore Place (216 m) |
| 60 | Dongguan | 16 / 28 | 57% | 2.21 | new | 2 | Minying International Trade Center T2 (423 m) |
| 61 | San Francisco | 27 / 27 | 100% | 2.8 | new | 1 | Salesforce Tower (326 m) |
| 62 | Taipei | 10 / 27 | 37% | 1.3 | new | 1 | TAIPEI 101 (508 m) |
| 63 | Boston | 26 / 26 | 100% | 3.98 | new | 2 | 200 Clarendon (241 m) |
| 64 | Ningbo | 24 / 26 | 92% | 5.05 | new | 4 | Ningbo Center Tower 1 (409 m) |
| 65 | Delhi | 7 / 26 | 27% | 0.71 | new | 1 | Supertech Nova East (180 m) |
| 66 | Seattle | 23 / 25 | 92% | 2.05 | new | 1 | Columbia Center (284 m) |
| 67 | Paris | 21 / 25 | 84% | 2.41 | new | 1 | Tour First (231 m) |
| 68 | Jersey City | 24 / 24 | 100% | 2.62 | new | 2 | 99 Hudson Street (271 m) |
| 69 | Ho Chi Minh City | 21 / 24 | 88% | 2.58 | new | 2 | Vincom Landmark 81 (461 m) |
| 70 | Johor Bahru | 21 / 24 | 88% | 2.44 | new | 2 | The Astaka Tower A (279 m) |
| 71 | Liuzhou | 10 / 24 | 42% | 2.98 | new | 2 | China Resources Center Tower A (210 m) |
| 72 | Sharjah | 16 / 23 | 70% | 3.01 | new | 2 | Nestle Plaza (225 m) |
| 73 | Brisbane | 22 / 22 | 100% | 1.77 | new | 1 | Brisbane Skytower (270 m) |
| 74 | São Paulo | 9 / 22 | 41% | 0.39 | new | 1 | Begonias (158 m) |
| 75 | Hyderabad | 8 / 22 | 36% | 0.5 | new | 1 | My Home Nishada Tower 1 (154 m) |
| 76 | Frankfurt | 20 / 21 | 95% | 2.35 | new | 1 | Commerzbank Tower (259 m) |
| 77 | Kuwait City | 16 / 21 | 76% | 3.4 | new | 1 | Al Hamra Tower (413 m) |
| 78 | Dallas | 19 / 20 | 95% | 1.82 | new | 1 | Bank of America Plaza (281 m) |
| 79 | Atlanta | 13 / 20 | 65% | 2.28 | new | 2 | Truist Plaza (264 m) |
| 80 | Manama | 10 / 20 | 50% | 1.5 | new | 1 | Four Seasons Hotel (270 m) |
| 81 | Calgary | 19 / 19 | 100% | 2.45 | new | 1 | Brookfield Place Tower One (247 m) |
| 82 | Zhengzhou | 12 / 19 | 63% | 1.37 | new | 2 | Zhengzhou Greenland Central Plaza North Tower (284 m) |
| 83 | Philadelphia | 18 / 18 | 100% | 2.67 | new | 1 | Comcast Technology Center (339 m) |
| 84 | Austin | 18 / 18 | 100% | 1.74 | new | 1 | Waterline (310 m) |
| 85 | Montreal | 17 / 18 | 94% | 1.93 | new | 1 | 1 Square Phillips (232 m) |
| 86 | Gold Coast | 16 / 18 | 89% | 2.89 | new | 2 | Q1 Tower (322 m) |
| 87 | Las Vegas | 16 / 17 | 94% | 4.42 | new | 2 | Fontainebleau Las Vegas (224 m) |
| 88 | Haikou | 7 / 17 | 41% | 1.0 | new | 1 | Landmark Tower (260 m) |
| 89 | Pyongyang | 7 / 17 | 41% | 0.76 | new | 1 | Ryomyong Street Apartment Building (270 m) |
| 90 | Changchun | 7 / 16 | 44% | 0.68 | new | 1 | Changchun China Resources Center Tower 1 (283 m) |
| 91 | Cairo | 11 / 15 | 73% | 1.84 | new | 1 | Iconic Tower (394 m) |
| 92 | Colombo | 7 / 15 | 47% | 1.08 | new | 1 | Sapphire Residences (225 m) |
| 93 | Fuzhou | 7 / 15 | 47% | 0.91 | new | 1 | ICC Thang Long Global Center (300 m) |
| 94 | Bogotá | 10 / 14 | 71% | 1.6 | new | 1 | BD Bacatá Torre Sur (216 m) |
| 95 | Pattaya | 6 / 14 | 43% | 0.69 | new | 1 | North Point Tower 1 (226 m) |
| 96 | Shijiazhuang | 5 / 14 | 36% | 1.01 | new | 1 | Lerthai Center 2 (213 m) |
| 97 | Warsaw | 13 / 13 | 100% | 2.24 | new | 2 | Varso Tower (310 m) |
| 98 | Buenos Aires | 9 / 13 | 69% | 1.17 | new | 1 | Alvear Tower Puerto Madero (235 m) |
| 99 | Nagoya | 9 / 12 | 75% | 1.31 | new | 1 | Midland Square (247 m) |
| 100 | Minneapolis | 10 / 11 | 91% | 1.19 | new | 1 | IDS Center (241 m) |
| 101 | Manchester | 10 / 11 | 91% | 1.14 | new | 1 | Deansgate Square South Tower (200 m) |
| 102 | New Alamein City | 5 / 11 | 46% | 1.04 | new | 1 | none completed yet |
| 103 | Charlotte | 10 / 10 | 100% | 1.57 | new | 1 | Bank of America Corporate Center (266 m) |
| 104 | Pittsburgh | 9 / 10 | 90% | 1.39 | new | 1 | U.S. Steel Tower (256 m) |
| 105 | Kawasaki | 9 / 10 | 90% | 1.08 | new | 1 | Park City Musashi-Kosugi Mid Sky Tower (204 m) |
| 106 | Rotterdam | 9 / 10 | 90% | 1.28 | new | 1 | De Zalmhaven I (215 m) |
| 107 | Taichung | 8 / 10 | 80% | 1.6 | new | 1 | Taichung Commercial Bank Headquarters (225 m) |
| 108 | Daejeon | 8 / 10 | 80% | 0.49 | new | 1 | Kumgang Exllu Tower 102 (170 m) |
| 109 | Kolkata | 7 / 10 | 70% | 0.54 | new | 1 | Urbana Tower 2 (165 m) |
| 110 | Goiânia | 5 / 10 | 50% | 1.56 | new | 1 | Kingdom Park Residence (181 m) |
| 111 | Itapema | 5 / 10 | 50% | 0.83 | new | 1 | none completed yet |
| 112 | Mecca | 9 / 9 | 100% | 0.94 | new | 1 | Makkah Royal Clock Tower (601 m) |
| 113 | Detroit | 9 / 9 | 100% | 0.96 | new | 1 | Detroit Marriott at the Renaissance Center (222 m) |
| 114 | Yokohama | 6 / 9 | 67% | 1.21 | new | 1 | Landmark Tower (296 m) |
| 115 | Rizhao | 5 / 9 | 56% | 0.4 | new | 1 | Rizhao Sheraton Hotel Tower 2 (189 m) |
| 116 | Denver | 8 / 8 | 100% | 1.27 | new | 1 | Republic Plaza (218 m) |
| 117 | Pohang | 8 / 8 | 100% | 0.57 | new | 1 | Jangseong Doosan We've The Zenith Tower 1 (164 m) |
| 118 | Izmir | 6 / 8 | 75% | 1.4 | new | 1 | Mistral Office Tower (216 m) |
| 119 | Fortaleza | 5 / 8 | 62% | 1.25 | new | 1 | none completed yet |
| 120 | Astana | 6 / 6 | 100% | 1.17 | new | 1 | Abu Dhabi Plaza (311 m) |
| 121 | Cartagena | 6 / 6 | 100% | 1.16 | new | 1 | Hotel Estelar Bocagrande (202 m) |
| 122 | Laibin | 6 / 6 | 100% | 0.8 | new | 1 | Laibin Yuda Building (167 m) |
| 123 | Madrid | 5 / 6 | 83% | 0.57 | new | 1 | Torre de Cristal (249 m) |
| 124 | Cleveland | 5 / 5 | 100% | 1.0 | new | 1 | Key Tower (289 m) |
| 125 | Perth | 5 / 5 | 100% | 0.85 | new | 1 | Central Park Tower (253 m) |
| 126 | Tampa | 5 / 5 | 100% | 0.51 | new | 1 | Regions Building (176 m) |
| 127 | Auckland | 5 / 5 | 100% | 0.67 | new | 1 | The Pacifica (179 m) |
| 128 | Columbus | 5 / 5 | 100% | 0.79 | new | 1 | Rhodes State Office Tower (190 m) |

## Areas and popup text by city

The text after the area list is the rationale shown in the site popup.

### Hong Kong

Areas: Hong Kong Island north shore: Sheung Wan, Central, Admiralty, Wan Chai and Causeway Bay; Kowloon: Mong Kok, Tai Kok Tsui, Olympic and Sham Shui Po; Tseung Kwan O town centre and Tiu Keng Leng; Tsuen Wan; LOHAS Park; Tai Wai and Sha Tin; Kowloon East: Kwun Tong and Kowloon Bay; Tsim Sha Tsui, Jordan and West Kowloon; Tung Chung; Tseung Kwan O north (Po Lam); Tuen Mun town centre; Quarry Bay (Taikoo Place); To Kwa Wan and Hung Hom waterfront; Tsing Yi: Tierra Verde; Kai Tak; Tin Shui Wai (Vianni Cove); Yau Tong; Pok Fu Lam: Residence Bel-Air; Fo Tan; Yuen Long: Yoho Midtown; Diamond Hill (Galaxia); Kwai Chung: Kwai Fong (Metroplaza).

22 pockets here are dense enough to count: Hong Kong Island north shore: Sheung Wan, Central, Admiralty, Wan Chai and Causeway Bay (126 towers); Kowloon: Mong Kok, Tai Kok Tsui, Olympic and Sham Shui Po (74); Tseung Kwan O town centre and Tiu Keng Leng (69); Tsuen Wan (47); LOHAS Park (40); Tai Wai and Sha Tin (23); Kowloon East: Kwun Tong and Kowloon Bay (23); Tsim Sha Tsui, Jordan and West Kowloon (19); Tung Chung (17); Tseung Kwan O north, Po Lam (13); Tuen Mun town centre (10); Quarry Bay, Taikoo Place (9); To Kwa Wan and Hung Hom waterfront (9); Tsing Yi: Tierra Verde (9); Kai Tak (8); Tin Shui Wai, Vianni Cove (8); Yau Tong (7); Pok Fu Lam: Residence Bel-Air (6); Fo Tan (6); Yuen Long: Yoho Midtown (6); Diamond Hill, Galaxia (6); Kwai Chung: Kwai Fong, Metroplaza (5). The other 36 of the city's 576 towers stand in groups too small or too spread out to count. The new towns (Tseung Kwan O, Tsuen Wan, Sha Tin, Tung Chung, Tuen Mun, Tin Shui Wai and Yuen Long) count alongside the harbour because their towers are just as tightly packed.

### Shenzhen

Areas: Nanshan: Houhai, Hi-Tech Park and Shenzhen Bay; Futian CBD, Lianhua and Shatou; Luohu: Dongmen, Guiyuan, Sungang and Nanhu; Qianhai; Chegongmiao and Xiangmihu; Shekou and Prince Bay; Bao'an Centre (Xin'an); Shenzhen Bay Super Headquarters (Shahe); Xili; Longhua (Minzhi); Shuibei and Cuizhu; Huaqiangbei; Upperhills (Huafu); Taoyuan; Bao'an: Xixiang (Hongfa QCC); Meilin; Overseas Chinese Town (OCT One); Pingshan: Kengzi; Shekou west (Hengyu Bincheng).

Nineteen pockets here are dense enough to count: Nanshan: Houhai, Hi-Tech Park and Shenzhen Bay (88 towers); Futian CBD, Lianhua and Shatou (76); Luohu: Dongmen, Guiyuan, Sungang and Nanhu (59); Qianhai (38); Chegongmiao and Xiangmihu (23); Shekou and Prince Bay (22); Bao'an Centre, Xin'an (22); Shenzhen Bay Super Headquarters, Shahe (21); Xili (19); Longhua, Minzhi (19); Shuibei and Cuizhu (18); Huaqiangbei (12); Upperhills, Huafu (11); Taoyuan (11); Bao'an: Xixiang, Hongfa QCC (7); Meilin (6); Overseas Chinese Town, OCT One (5); Pingshan: Kengzi (5); Shekou west, Hengyu Bincheng (5). The other 69 of the city's 536 towers stand in groups too small or too spread out to count. Shekou, Bao'an, Xili and Longhua qualify on density too. Most of the band between Futian and Nanshan along Shennan Boulevard has too few towers to join them.

### New York City

Areas: Midtown Manhattan; Lower Manhattan; Downtown Brooklyn; Long Island City.

Four pockets here are dense enough to count: Midtown Manhattan (230 towers); Lower Manhattan (66); Downtown Brooklyn (16); Long Island City (12). The other 12 of the city's 337 towers stand in groups too small or too spread out to count. The Village, Chelsea south of the Midtown cluster and the Lower East Side have too few towers to join Midtown and Lower Manhattan into one area.

### Dubai

Areas: Downtown Dubai, Business Bay, DIFC and Sheikh Zayed Road; Dubai Marina, JBR and Jumeirah Lakes Towers; Barsha Heights (Tecom); Dubai Creek Harbour.

Four pockets here are dense enough to count: Downtown Dubai, Business Bay, DIFC and Sheikh Zayed Road (162 towers); Dubai Marina, JBR and Jumeirah Lakes Towers (121); Barsha Heights, Tecom (10); Dubai Creek Harbour (7). The other 21 of the city's 321 towers stand in groups too small or too spread out to count.

### Guangzhou

Areas: Tianhe CBD: Zhujiang New Town and Tianhe North; Pazhou; Panyu: Wanbo business district; Haizhu: Xingang and Chigang; International Financial City (Yuancun); Yuexiu: Beijing Road and Haizhu Square; Zengcheng: Yongning; Yuexiu: Huanshi East Road; Pazhou west (Canton Fair Complex).

Nine pockets here are dense enough to count: Tianhe CBD: Zhujiang New Town and Tianhe North (77 towers); Pazhou (22); Panyu: Wanbo business district (15); Haizhu: Xingang and Chigang (15); International Financial City, Yuancun (10); Yuexiu: Beijing Road and Haizhu Square (10); Zengcheng: Yongning (9); Yuexiu: Huanshi East Road (5); Pazhou west, Canton Fair Complex (5). The other 65 of the city's 233 towers stand in groups too small or too spread out to count. Panyu's Wanbo business district and the Haizhu riverside qualify on density too.

### Kuala Lumpur

Areas: KL city centre: KLCC, Bukit Bintang, Kampung Baru, Chow Kit and Merdeka 118; Bandar Tun Razak (Razak City); KL Sentral and Bangsar; Mont Kiara; Ampang (Ulu Kelang).

Five pockets here are dense enough to count: KL city centre: KLCC, Bukit Bintang, Kampung Baru, Chow Kit and Merdeka 118 (132 towers); Bandar Tun Razak, Razak City (12); KL Sentral and Bangsar (10); Mont Kiara (5); Ampang, Ulu Kelang (5). The other 65 of the city's 229 towers stand in groups too small or too spread out to count.

### Wuhan

Areas: Hankou centre: Wansong, Taibei Road and Liujiaoting; Wuchang: Shuiguohu and Zhongnan Road; Hankou riverside: Jianghan Road and Hualou Street; Hanyang riverside (Zhoutou); Wuchang riverside: Xujiapeng (Wuhan Greenland Center); Jiang'an riverside; Qiaokou: Hanzheng Street; Hanyang: Sixin; Wuchang: Liyuan (PTJ International Finance Center); Qingshan riverside; Hankou: Wuhan Tower; Jiang'an: Wuhan Tiandi; Jiang'an: Wuhan CTF Finance Center.

Thirteen pockets here are dense enough to count: Hankou centre: Wansong, Taibei Road and Liujiaoting (45 towers); Wuchang: Shuiguohu and Zhongnan Road (21); Hankou riverside: Jianghan Road and Hualou Street (15); Hanyang riverside, Zhoutou (15); Wuchang riverside: Xujiapeng, Wuhan Greenland Center (13); Jiang'an riverside (12); Qiaokou: Hanzheng Street (11); Hanyang: Sixin (9); Wuchang: Liyuan, PTJ International Finance Center (8); Qingshan riverside (7); Hankou: Wuhan Tower (6); Jiang'an: Wuhan Tiandi (6); Jiang'an: Wuhan CTF Finance Center (5). The other 48 of the city's 224 towers stand in groups too small or too spread out to count.

### Shanghai

Areas: Lujiazui and the Century Avenue corridor; Central Puxi: People's Square, Nanjing Road, Jing'an and Huaihai Road; North Bund; Xiaodongmen and the South Bund; Xuhui riverside (Longhua); Suhe Bay and Shanghai railway station; Xujiahui.

Seven pockets here are dense enough to count: Lujiazui and the Century Avenue corridor (79 towers); Central Puxi: People's Square, Nanjing Road, Jing'an and Huaihai Road (48); North Bund (9); Xiaodongmen and the South Bund (8); Xuhui riverside, Longhua (7); Suhe Bay and Shanghai railway station (6); Xujiahui (5). The other 48 of the city's 210 towers stand in groups too small or too spread out to count.

### Tokyo

Areas: Central Tokyo: Otemachi, Marunouchi, Toranomon, Akasaka, Roppongi, Shiodome and Hamamatsucho; Tsukishima, Kachidoki, Harumi and Toyosu; West Shinjuku; Ikebukuro (Sunshine 60).

Four pockets here are dense enough to count: Central Tokyo: Otemachi, Marunouchi, Toranomon, Akasaka, Roppongi, Shiodome and Hamamatsucho (103 towers); Tsukishima, Kachidoki, Harumi and Toyosu (30); West Shinjuku (25); Ikebukuro, Sunshine 60 (5). The other 27 of the city's 190 towers stand in groups too small or too spread out to count. The four towers at Shibuya station fall one short of the threshold.

### Chongqing

Areas: Yuzhong peninsula: Jiefangbei and Chaotianmen; Jiangbeizui CBD; Guanyinqiao; Nanping (Nan'an); Nan'an riverfront: Haitangxi.

Five pockets here are dense enough to count: Yuzhong peninsula: Jiefangbei and Chaotianmen (54 towers); Jiangbeizui CBD (19); Guanyinqiao (11); Nanping, Nan'an (8); Nan'an riverfront: Haitangxi (5). The other 55 of the city's 152 towers stand in groups too small or too spread out to count.

### Toronto

Areas: Downtown Toronto: Financial District, South Core, King West, St Lawrence and the Yonge Street corridor; Mississauga City Centre; Vaughan Metropolitan Centre; Humber Bay Shores; Yonge and Eglinton.

Five pockets here are dense enough to count: Downtown Toronto: Financial District, South Core, King West, St Lawrence and the Yonge Street corridor (110 towers); Mississauga City Centre (11); Vaughan Metropolitan Centre (8); Humber Bay Shores (7); Yonge and Eglinton (5). The other 7 of the city's 148 towers stand in groups too small or too spread out to count.

### Chengdu

Areas: Central Chengdu: Chunxi Road, Jinguanyi and Xiyuhe; Tianfu Avenue south (Global Center); Jincheng Financial City; Tianfu New Area (Tianfu Center).

Four pockets here are dense enough to count: Central Chengdu: Chunxi Road, Jinguanyi and Xiyuhe (46 towers); Tianfu Avenue south, Global Center (29); Jincheng Financial City (19); Tianfu New Area, Tianfu Center (10). The other 39 of the city's 143 towers stand in groups too small or too spread out to count.

### Chicago

Areas: The Loop, River North, Streeterville, West Loop Gate and the South Loop.

One pocket here is dense enough to count: The Loop, River North, Streeterville, West Loop Gate and the South Loop (136 towers). The other 3 of the city's 139 towers stand in groups too small or too spread out to count.

### Metro Manila

Areas: Makati CBD; Ortigas Center; Bonifacio Global City; Eastwood City (Quezon City); Greenhills (San Juan).

Five pockets here are dense enough to count: Makati CBD (60 towers); Ortigas Center (33); Bonifacio Global City (20); Eastwood City, Quezon City (6); Greenhills, San Juan (5). The other 15 of the city's 139 towers stand in groups too small or too spread out to count.

### Bangkok

Areas: Ratchaprasong, Ploenchit, Lumphini and lower Sukhumvit; Silom and Sathorn; Chao Phraya riverside: Iconsiam and Charoen Krung.

Three pockets here are dense enough to count: Ratchaprasong, Ploenchit, Lumphini and lower Sukhumvit (61 towers); Silom and Sathorn (28); Chao Phraya riverside: Iconsiam and Charoen Krung (11). The other 36 of the city's 136 towers stand in groups too small or too spread out to count.

### Mumbai

Areas: Lower Parel and Worli; Parel; Goregaon East; Tardeo and Malabar Hill; Wadala (New Cuffe Parade); Borivali East (Sky City).

Six pockets here are dense enough to count: Lower Parel and Worli (58 towers); Parel (11); Goregaon East (10); Tardeo and Malabar Hill (7); Wadala, New Cuffe Parade (7); Borivali East, Sky City (5). The other 22 of the city's 120 towers stand in groups too small or too spread out to count.

### Jakarta

Areas: Golden Triangle: Thamrin, Sudirman, SCBD and Kuningan; Podomoro City; Kebayoran Lama: Pakubuwono.

Three pockets here are dense enough to count: Golden Triangle: Thamrin, Sudirman, SCBD and Kuningan (83 towers); Podomoro City (13); Kebayoran Lama: Pakubuwono (5). The other 17 of the city's 118 towers stand in groups too small or too spread out to count.

### Seoul

Areas: Yeouido; Dogok; Mokdong; Samseong: COEX and Teheran-ro east; Seongsu (Seoul Forest); Ilsan: Tanhyeon; Gangnam station and Yeoksam (Teheran-ro west); Ilsan: Baekseok (Y-City); Gwangmyeong station; Konkuk University station (Star City).

Ten pockets here are dense enough to count: Yeouido (13 towers); Dogok (10); Mokdong (9); Samseong: COEX and Teheran-ro east (9); Seongsu, Seoul Forest (8); Ilsan: Tanhyeon (8); Gangnam station and Yeoksam, Teheran-ro west (6); Ilsan: Baekseok, Y-City (6); Gwangmyeong station (6); Konkuk University station, Star City (5). The other 37 of the city's 117 towers stand in groups too small or too spread out to count. Seoul's old centre (Jongno-gu and Jung-gu) holds only three towers of 150 m+, and Lotte World Tower at Jamsil stands alone, so neither counts.

### Hangzhou

Areas: Qianjiang Century City (Xiaoshan); Qianjiang New Town; Future Sci-Tech City (Yuhang).

Three pockets here are dense enough to count: Qianjiang Century City, Xiaoshan (44 towers); Qianjiang New Town (34); Future Sci-Tech City, Yuhang (7). The other 25 of the city's 110 towers stand in groups too small or too spread out to count.

### Singapore

Areas: Downtown Core: Raffles Place, Marina Bay, Tanjong Pagar and Shenton Way; Civic District, Marina Centre and Bugis; Orchard Boulevard and Newton.

Three pockets here are dense enough to count: Downtown Core: Raffles Place, Marina Bay, Tanjong Pagar and Shenton Way (69 towers); Civic District, Marina Centre and Bugis (15); Orchard Boulevard and Newton (9). The other 11 of the city's 104 towers stand in groups too small or too spread out to count.

### Miami

Areas: Downtown Miami and Brickell; Edgewater; Sunny Isles Beach.

Three pockets here are dense enough to count: Downtown Miami and Brickell (67 towers); Edgewater (15); Sunny Isles Beach (14). The other 7 of the city's 103 towers stand in groups too small or too spread out to count.

### Changsha

Areas: Kaifu: Furong Road north and Xiangya Road; Binjiang New City (Yuelu); Yuhua: Litou (Yunda Central Plaza); Meixi Lake (Yuelu); Furong: Houjiatang (Xinchu Qingtian Plaza); Tianxin riverside (Minmetals Plaza); Wuyi Square and Dingwangtai (Changsha IFS); Pozijie riverside; Xinhe Delta (Kaifu).

Nine pockets here are dense enough to count: Kaifu: Furong Road north and Xiangya Road (18 towers); Binjiang New City, Yuelu (12); Yuhua: Litou, Yunda Central Plaza (9); Meixi Lake, Yuelu (8); Furong: Houjiatang, Xinchu Qingtian Plaza (8); Tianxin riverside, Minmetals Plaza (7); Wuyi Square and Dingwangtai, Changsha IFS (5); Pozijie riverside (5); Xinhe Delta, Kaifu (5). The other 22 of the city's 99 towers stand in groups too small or too spread out to count.

### Nanjing

Areas: Hexi CBD; Xinjiekou and Gulou; Gulou: Zhongyangmen; Jiangdong (Suning Ruicheng).

Four pockets here are dense enough to count: Hexi CBD (25 towers); Xinjiekou and Gulou (24); Gulou: Zhongyangmen (6); Jiangdong, Suning Ruicheng (5). The other 26 of the city's 86 towers stand in groups too small or too spread out to count.

### Nanning

Areas: Wuxiang New Area (Liangqing); ASEAN Business District (Qingxiu); Qingxiu Wanda (Dongge Road); Wuxiang: Five Elephants (Liangqing); Zhongshan (Liyuan Skyline City); Vanke City (Qingxiu).

Six pockets here are dense enough to count: Wuxiang New Area, Liangqing (19 towers); ASEAN Business District, Qingxiu (16); Qingxiu Wanda, Dongge Road (9); Wuxiang: Five Elephants, Liangqing (7); Zhongshan, Liyuan Skyline City (5); Vanke City, Qingxiu (5). The other 21 of the city's 82 towers stand in groups too small or too spread out to count.

### Melbourne

Areas: CBD, Southbank and Docklands.

One pocket here is dense enough to count: CBD, Southbank and Docklands (79 towers). The other 2 of the city's 81 towers stand in groups too small or too spread out to count.

### Busan

Areas: Haeundae beachfront and Marine City; Centum City; Munhyeon (Busan International Finance Center) and Seomyeon; Haeundae Jung-dong (Hillside We've); Beomil-dong.

Five pockets here are dense enough to count: Haeundae beachfront and Marine City (20 towers); Centum City (16); Munhyeon, Busan International Finance Center and Seomyeon (9); Haeundae Jung-dong, Hillside We've (6); Beomil-dong (5). The other 21 of the city's 77 towers stand in groups too small or too spread out to count.

### Shenyang

Areas: Qingnian Avenue: Nanhu, Fengyutan and Wulihe; Shengjing Finance Plaza (Beishichang); Forum 66 (Qingnian Street).

Three pockets here are dense enough to count: Qingnian Avenue: Nanhu, Fengyutan and Wulihe (46 towers); Shengjing Finance Plaza, Beishichang (15); Forum 66, Qingnian Street (5). The other 9 of the city's 75 towers stand in groups too small or too spread out to count.

### Moscow

Areas: Moscow International Business Centre (Moscow City); Savyolovsky (D1 and Graphite).

Two pockets here are dense enough to count: Moscow International Business Centre, Moscow City (23 towers); Savyolovsky, D1 and Graphite (5). The other 45 of the city's 73 towers stand in groups too small or too spread out to count. The historic centre inside the Garden Ring holds only two towers of 150 m+ (Kotelnicheskaya Embankment and Repin), far below the threshold. Moscow's other towers are Stalinist high-rises and residential complexes spread across the city in groups of four or fewer.

### Beijing

Areas: Beijing CBD (Guomao); Lize Financial Business District; Wangjing.

Three pockets here are dense enough to count: Beijing CBD, Guomao (33 towers); Lize Financial Business District (12); Wangjing (11). The other 13 of the city's 69 towers stand in groups too small or too spread out to count. Lize and Wangjing qualify on density too; the old city inside the 2nd Ring is height-limited.

### Tianjin

Areas: Central Tianjin along the Hai River; Heping: Quanyechang and Nanjing Road; TEDA (Binhai); Yujiapu (Binhai).

Four pockets here are dense enough to count: Central Tianjin along the Hai River (35 towers); Heping: Quanyechang and Nanjing Road (9); TEDA, Binhai (6); Yujiapu, Binhai (5). The other 14 of the city's 69 towers stand in groups too small or too spread out to count.

### Panama City

Areas: Bella Vista, Obarrio, Marbella, Punta Paitilla and Punta Pacífica; Costa del Este.

Two pockets here are dense enough to count: Bella Vista, Obarrio, Marbella, Punta Paitilla and Punta Pacífica (45 towers); Costa del Este (15). The other 8 of the city's 68 towers stand in groups too small or too spread out to count.

### Sydney

Areas: Sydney CBD, Barangaroo and Haymarket; Parramatta.

Two pockets here are dense enough to count: Sydney CBD, Barangaroo and Haymarket (46 towers); Parramatta (8). The other 10 of the city's 64 towers stand in groups too small or too spread out to count. North Sydney holds four towers, one short of the threshold.

### Suzhou

Areas: Jinji Lake CBD (west bank); Wujiang: Taihu New Town; Jinji Lake CBD east bank (Suzhou IFS); Wujiang: Hengli Bay.

Four pockets here are dense enough to count: Jinji Lake CBD, west bank (13 towers); Wujiang: Taihu New Town (8); Jinji Lake CBD east bank, Suzhou IFS (6); Wujiang: Hengli Bay (6). The other 27 of the city's 60 towers stand in groups too small or too spread out to count.

### Zhuhai

Areas: Hengqin; Gongbei.

Two pockets here are dense enough to count: Hengqin (26 towers); Gongbei (7). The other 27 of the city's 60 towers stand in groups too small or too spread out to count. Zhuhai Tower stands alone and falls below the threshold.

### Istanbul

Areas: Istanbul Finance Center (Ataşehir); Levent and Esentepe.

Two pockets here are dense enough to count: Istanbul Finance Center, Ataşehir (11 towers); Levent and Esentepe (11). The other 37 of the city's 59 towers stand in groups too small or too spread out to count. Maslak, Seyrantepe (Skyland) and Fulya hold groups of four towers or fewer.

### Doha

Areas: West Bay.

One pocket here is dense enough to count: West Bay (43 towers). The other 13 of the city's 56 towers stand in groups too small or too spread out to count.

### Dalian

Areas: Central Dalian (Zhongshan District); Xinghai Bay business district.

Two pockets here are dense enough to count: Central Dalian, Zhongshan District (40 towers); Xinghai Bay business district (9). The other 3 of the city's 52 towers stand in groups too small or too spread out to count.

### Osaka

Areas: Umeda and Nakanoshima.

One pocket here is dense enough to count: Umeda and Nakanoshima (33 towers). The other 18 of the city's 51 towers stand in groups too small or too spread out to count. Abeno Harukas at Tennoji stands nearly alone and falls below the threshold.

### Incheon

Areas: Songdo International Business District; Songdo east; Cheongna.

Three pockets here are dense enough to count: Songdo International Business District (22 towers); Songdo east (12); Cheongna (8). The other 8 of the city's 50 towers stand in groups too small or too spread out to count.

### London

Areas: Canary Wharf; City of London and London Bridge; Nine Elms and Vauxhall.

Three pockets here are dense enough to count: Canary Wharf (21 towers); City of London and London Bridge (17); Nine Elms and Vauxhall (5). The other 6 of the city's 49 towers stand in groups too small or too spread out to count.

### Tel Aviv

Areas: Central Tel Aviv and Ramat Gan: Sarona, Azrieli and the Diamond Exchange; Bnei Brak business district.

Two pockets here are dense enough to count: Central Tel Aviv and Ramat Gan: Sarona, Azrieli and the Diamond Exchange (35 towers); Bnei Brak business district (6). The other 8 of the city's 49 towers stand in groups too small or too spread out to count.

### Jinan

Areas: Jinan CBD; Lixia: Shandong International Financial Center.

Two pockets here are dense enough to count: Jinan CBD (20 towers); Lixia: Shandong International Financial Center (16). The other 12 of the city's 48 towers stand in groups too small or too spread out to count.

### Abu Dhabi

Areas: Al Reem Island; Western Corniche: Etihad Towers and ADNOC Headquarters; Corniche and Markaziya (World Trade Center); Al Reem Island: Marina Square; Eastern Corniche (Capital Plaza).

Five pockets here are dense enough to count: Al Reem Island (10 towers); Western Corniche: Etihad Towers and ADNOC Headquarters (9); Corniche and Markaziya, World Trade Center (8); Al Reem Island: Marina Square (8); Eastern Corniche, Capital Plaza (6). The other 5 of the city's 46 towers stand in groups too small or too spread out to count.

### Xi’an

Areas: High-tech Zone (Zhangba); Yanta: Changyanbao (Xi'an Yanzhan).

Two pockets here are dense enough to count: High-tech Zone, Zhangba (11 towers); Yanta: Changyanbao, Xi'an Yanzhan (6). The other 29 of the city's 46 towers stand in groups too small or too spread out to count.

### Balneário Camboriú

Areas: Avenida Atlântica beachfront (Centro).

One pocket here is dense enough to count: Avenida Atlântica beachfront, Centro (45 towers).

### Xiamen

Areas: Lujiang waterfront (Cross Strait Financial Centre); Lianqian north (Strait Pearl Plaza); Lianqian south (C&D International).

Three pockets here are dense enough to count: Lujiang waterfront, Cross Strait Financial Centre (9 towers); Lianqian north, Strait Pearl Plaza (6); Lianqian south, C&D International (6). The other 24 of the city's 45 towers stand in groups too small or too spread out to count.

### Hefei

Areas: Swan Lake CBD; Baohe: Wannianbu.

Two pockets here are dense enough to count: Swan Lake CBD (10 towers); Baohe: Wannianbu (5). The other 30 of the city's 45 towers stand in groups too small or too spread out to count.

### Guiyang

Areas: Nanming centre (Hengfeng Guiyang Center); Guanshanhu (Guiyang International Financial Center); Yunyan east (Fangzhou Dong Mao Center).

Three pockets here are dense enough to count: Nanming centre, Hengfeng Guiyang Center (8 towers); Guanshanhu, Guiyang International Financial Center (7); Yunyan east, Fangzhou Dong Mao Center (5). The other 24 of the city's 44 towers stand in groups too small or too spread out to count.

### Foshan

Areas: Shunde: Lecong; Nanhai: Guicheng.

Two pockets here are dense enough to count: Shunde: Lecong (9 towers); Nanhai: Guicheng (8). The other 27 of the city's 44 towers stand in groups too small or too spread out to count.

### Houston

Areas: Downtown Houston.

One pocket here is dense enough to count: Downtown Houston (31 towers). The other 9 of the city's 40 towers stand in groups too small or too spread out to count.

### Nanchang

Areas: Honggutan: Greenland Central Plaza; Honggutan: Huaying Center and IFC.

Two pockets here are dense enough to count: Honggutan: Greenland Central Plaza (7 towers); Honggutan: Huaying Center and IFC (5). The other 28 of the city's 40 towers stand in groups too small or too spread out to count.

### Qingdao

Areas: Shinan: Hong Kong Middle Road and Fushan Bay; Laoshan: Jinjialing financial district.

Two pockets here are dense enough to count: Shinan: Hong Kong Middle Road and Fushan Bay (23 towers); Laoshan: Jinjialing financial district (5). The other 9 of the city's 37 towers stand in groups too small or too spread out to count.

### Kunming

Areas: Guandu (Longfor Times Financial Centre).

One pocket here is dense enough to count: Guandu, Longfor Times Financial Centre (5 towers). The other 32 of the city's 37 towers stand in groups too small or too spread out to count.

### Mexico City

Areas: Paseo de la Reforma; Santa Fe: Arcos Bosques.

Two pockets here are dense enough to count: Paseo de la Reforma (11 towers); Santa Fe: Arcos Bosques (5). The other 18 of the city's 34 towers stand in groups too small or too spread out to count.

### Los Angeles

Areas: Downtown Los Angeles; Century City.

Two pockets here are dense enough to count: Downtown Los Angeles (25 towers); Century City (7). One of the city's 33 towers stands apart from them.

### Riyadh

Areas: Olaya: Al Faisaliah; King Abdullah Financial District; Al Malqa (King Fahd Road north); Olaya: Kingdom Centre.

Four pockets here are dense enough to count: Olaya: Al Faisaliah (7 towers); King Abdullah Financial District (7); Al Malqa, King Fahd Road north (7); Olaya: Kingdom Centre (6). The other 6 of the city's 33 towers stand in groups too small or too spread out to count.

### Macau

Areas: Cotai; Macau Peninsula: Sé and NAPE (Grand Lisboa); Areia Preta (La Cité).

Three pockets here are dense enough to count: Cotai (11 towers); Macau Peninsula: Sé and NAPE, Grand Lisboa (9); Areia Preta, La Cité (5). The other 7 of the city's 32 towers stand in groups too small or too spread out to count.

### Wuxi

Areas: Wuxi centre: Chong'an Temple; Qingmingqiao (Wuxi IFS).

Two pockets here are dense enough to count: Wuxi centre: Chong'an Temple (9 towers); Qingmingqiao, Wuxi IFS (8). The other 14 of the city's 31 towers stand in groups too small or too spread out to count.

### Vancouver

Areas: Burnaby: Brentwood; Downtown Vancouver: West Georgia and the West End; Burnaby: Metrotown.

Three pockets here are dense enough to count: Burnaby: Brentwood (7 towers); Downtown Vancouver: West Georgia and the West End (6); Burnaby: Metrotown (6). The other 9 of the city's 28 towers stand in groups too small or too spread out to count.

### Dongguan

Areas: Nancheng: Dongguan CBD; Dongcheng centre.

Two pockets here are dense enough to count: Nancheng: Dongguan CBD (9 towers); Dongcheng centre (7). The other 12 of the city's 28 towers stand in groups too small or too spread out to count.

### San Francisco

Areas: Financial District, Rincon Hill and Transbay.

One pocket here is dense enough to count: Financial District, Rincon Hill and Transbay (27 towers).

### Taipei

Areas: Xinyi.

One pocket here is dense enough to count: Xinyi (10 towers). The other 17 of the city's 27 towers stand in groups too small or too spread out to count. The three towers around Taipei Main Station (Shin Kong Life Tower and the Taipei Twins) are too few to count.

### Boston

Areas: Downtown Boston: Financial District and Government Center; Back Bay (Prudential Center).

Two pockets here are dense enough to count: Downtown Boston: Financial District and Government Center (21 towers); Back Bay, Prudential Center (5).

### Ningbo

Areas: Eastern New Town (Ningbo Center); Sanjiangkou: Jiangxia and Tianyi Square; Jiangbei: Old Bund and Greenland Center; Southern Business District (Yinzhou).

Four pockets here are dense enough to count: Eastern New Town, Ningbo Center (9 towers); Sanjiangkou: Jiangxia and Tianyi Square (5); Jiangbei: Old Bund and Greenland Center (5); Southern Business District, Yinzhou (5). The other 2 of the city's 26 towers stand in groups too small or too spread out to count.

### Delhi

Areas: Noida Sector 94.

One pocket here is dense enough to count: Noida Sector 94 (7 towers). The other 19 of the city's 26 towers stand in groups too small or too spread out to count.

### Seattle

Areas: Downtown Seattle and Belltown.

One pocket here is dense enough to count: Downtown Seattle and Belltown (23 towers). The other 2 of the city's 25 towers stand in groups too small or too spread out to count.

### Paris

Areas: La Défense.

One pocket here is dense enough to count: La Défense (21 towers). The other 4 of the city's 25 towers stand in groups too small or too spread out to count. Central Paris has almost no towers of 150 m+; the 13th and 15th arrondissements hold one or two each.

### Jersey City

Areas: Downtown Jersey City waterfront; Journal Square.

Two pockets here are dense enough to count: Downtown Jersey City waterfront (17 towers); Journal Square (7).

### Ho Chi Minh City

Areas: Vinhomes Central Park (Landmark 81); Saigon centre: Bitexco and the riverfront.

Two pockets here are dense enough to count: Vinhomes Central Park, Landmark 81 (12 towers); Saigon centre: Bitexco and the riverfront (9). The other 3 of the city's 24 towers stand in groups too small or too spread out to count.

### Johor Bahru

Areas: Johor Bahru city centre; Danga Bay.

Two pockets here are dense enough to count: Johor Bahru city centre (11 towers); Danga Bay (10). The other 3 of the city's 24 towers stand in groups too small or too spread out to count.

### Liuzhou

Areas: Chengzhong (Sanbao International Plaza); Yufeng (China Resources Center).

Two pockets here are dense enough to count: Chengzhong, Sanbao International Plaza (5 towers); Yufeng, China Resources Center (5). The other 14 of the city's 24 towers stand in groups too small or too spread out to count.

### Sharjah

Areas: Al Majaz and Al Khan; Al Nahda.

Two pockets here are dense enough to count: Al Majaz and Al Khan (10 towers); Al Nahda (6). The other 7 of the city's 23 towers stand in groups too small or too spread out to count.

### Brisbane

Areas: Brisbane CBD.

One pocket here is dense enough to count: Brisbane CBD (22 towers).

### São Paulo

Areas: Cidade Jardim (Morumbi).

One pocket here is dense enough to count: Cidade Jardim, Morumbi (9 towers). The other 13 of the city's 22 towers stand in groups too small or too spread out to count.

### Hyderabad

Areas: Kokapet.

One pocket here is dense enough to count: Kokapet (8 towers). The other 14 of the city's 22 towers stand in groups too small or too spread out to count.

### Frankfurt

Areas: Bankenviertel: Innenstadt, Westend-Süd and Bahnhofsviertel.

One pocket here is dense enough to count: Bankenviertel: Innenstadt, Westend-Süd and Bahnhofsviertel (20 towers). One of the city's 21 towers stands apart from it.

### Kuwait City

Areas: Sharq and Mirqab.

One pocket here is dense enough to count: Sharq and Mirqab (16 towers). The other 5 of the city's 21 towers stand in groups too small or too spread out to count.

### Dallas

Areas: Downtown Dallas.

One pocket here is dense enough to count: Downtown Dallas (19 towers). One of the city's 20 towers stands apart from it.

### Atlanta

Areas: Midtown Atlanta; Downtown Atlanta.

Two pockets here are dense enough to count: Midtown Atlanta (7 towers); Downtown Atlanta (6). The other 7 of the city's 20 towers stand in groups too small or too spread out to count.

### Manama

Areas: Bahrain Financial Harbour and the Diplomatic Area.

One pocket here is dense enough to count: Bahrain Financial Harbour and the Diplomatic Area (10 towers). The other 10 of the city's 20 towers stand in groups too small or too spread out to count.

### Calgary

Areas: Downtown Calgary.

One pocket here is dense enough to count: Downtown Calgary (19 towers).

### Zhengzhou

Areas: Erqi: Minggong Road; Zhengdong New District CBD.

Two pockets here are dense enough to count: Erqi: Minggong Road (7 towers); Zhengdong New District CBD (5). The other 7 of the city's 19 towers stand in groups too small or too spread out to count.

### Philadelphia

Areas: Center City.

One pocket here is dense enough to count: Center City (18 towers).

### Austin

Areas: Downtown Austin.

One pocket here is dense enough to count: Downtown Austin (18 towers).

### Montreal

Areas: Downtown Montreal (Ville-Marie).

One pocket here is dense enough to count: Downtown Montreal, Ville-Marie (17 towers). One of the city's 18 towers stands apart from it.

### Gold Coast

Areas: Surfers Paradise; Broadbeach.

Two pockets here are dense enough to count: Surfers Paradise (11 towers); Broadbeach (5). The other 2 of the city's 18 towers stand in groups too small or too spread out to count.

### Las Vegas

Areas: The Strip north: Resorts World and Fontainebleau; The Strip centre: CityCenter and the Cosmopolitan.

Two pockets here are dense enough to count: The Strip north: Resorts World and Fontainebleau (8 towers); The Strip centre: CityCenter and the Cosmopolitan (8). One of the city's 17 towers stands apart from them.

### Haikou

Areas: Binhai Avenue (Longhua).

One pocket here is dense enough to count: Binhai Avenue, Longhua (7 towers). The other 10 of the city's 17 towers stand in groups too small or too spread out to count.

### Pyongyang

Areas: Ryomyong Street.

One pocket here is dense enough to count: Ryomyong Street (7 towers). The other 10 of the city's 17 towers stand in groups too small or too spread out to count.

### Changchun

Areas: Nanguan: China Resources Center.

One pocket here is dense enough to count: Nanguan: China Resources Center (7 towers). The other 9 of the city's 16 towers stand in groups too small or too spread out to count.

### Cairo

Areas: New Administrative Capital CBD.

One pocket here is dense enough to count: New Administrative Capital CBD (11 towers). The other 4 of the city's 15 towers stand in groups too small or too spread out to count.

### Colombo

Areas: Galle Face and Kompannaweediya.

One pocket here is dense enough to count: Galle Face and Kompannaweediya (7 towers). The other 8 of the city's 15 towers stand in groups too small or too spread out to count.

### Fuzhou

Areas: Taijiang riverside.

One pocket here is dense enough to count: Taijiang riverside (7 towers). The other 8 of the city's 15 towers stand in groups too small or too spread out to count.

### Bogotá

Areas: Centro Internacional.

One pocket here is dense enough to count: Centro Internacional (10 towers). The other 4 of the city's 14 towers stand in groups too small or too spread out to count.

### Pattaya

Areas: Wongamat (Na Kluea).

One pocket here is dense enough to count: Wongamat, Na Kluea (6 towers). The other 8 of the city's 14 towers stand in groups too small or too spread out to count.

### Shijiazhuang

Areas: Chang'an: Lerthai Center.

One pocket here is dense enough to count: Chang'an: Lerthai Center (5 towers). The other 9 of the city's 14 towers stand in groups too small or too spread out to count.

### Warsaw

Areas: City centre: Varso and the Palace of Culture; Wola: Rondo Daszyńskiego.

Two pockets here are dense enough to count: City centre: Varso and the Palace of Culture (8 towers); Wola: Rondo Daszyńskiego (5).

### Buenos Aires

Areas: Puerto Madero.

One pocket here is dense enough to count: Puerto Madero (9 towers). The other 4 of the city's 13 towers stand in groups too small or too spread out to count.

### Nagoya

Areas: Meieki (Nagoya Station).

One pocket here is dense enough to count: Meieki, Nagoya Station (9 towers). The other 3 of the city's 12 towers stand in groups too small or too spread out to count.

### Minneapolis

Areas: Downtown Minneapolis.

One pocket here is dense enough to count: Downtown Minneapolis (10 towers). One of the city's 11 towers stands apart from it.

### Manchester

Areas: Deansgate.

One pocket here is dense enough to count: Deansgate (10 towers). One of the city's 11 towers stands apart from it.

### New Alamein City

Areas: New Alamein Downtown.

One pocket here is dense enough to count: New Alamein Downtown (5 towers). The other 6 of the city's 11 towers stand in groups too small or too spread out to count.

### Charlotte

Areas: Uptown Charlotte.

One pocket here is dense enough to count: Uptown Charlotte (10 towers).

### Pittsburgh

Areas: Downtown Pittsburgh (Golden Triangle).

One pocket here is dense enough to count: Downtown Pittsburgh, Golden Triangle (9 towers). One of the city's 10 towers stands apart from it.

### Kawasaki

Areas: Musashi-Kosugi.

One pocket here is dense enough to count: Musashi-Kosugi (9 towers). One of the city's 10 towers stands apart from it.

### Rotterdam

Areas: Kop van Zuid (Wilhelminapier).

One pocket here is dense enough to count: Kop van Zuid, Wilhelminapier (9 towers). One of the city's 10 towers stands apart from it.

### Taichung

Areas: Xitun: 7th Redevelopment Zone.

One pocket here is dense enough to count: Xitun: 7th Redevelopment Zone (8 towers). The other 2 of the city's 10 towers stand in groups too small or too spread out to count.

### Daejeon

Areas: Seokbong-dong (Daedeok-gu).

One pocket here is dense enough to count: Seokbong-dong, Daedeok-gu (8 towers). The other 2 of the city's 10 towers stand in groups too small or too spread out to count.

### Kolkata

Areas: Anandapur (Urbana).

One pocket here is dense enough to count: Anandapur, Urbana (7 towers). The other 3 of the city's 10 towers stand in groups too small or too spread out to count.

### Goiânia

Areas: Nova Suíça.

One pocket here is dense enough to count: Nova Suíça (5 towers). The other 5 of the city's 10 towers stand in groups too small or too spread out to count.

### Itapema

Areas: Itapema beachfront.

One pocket here is dense enough to count: Itapema beachfront (5 towers). The other 5 of the city's 10 towers stand in groups too small or too spread out to count.

### Mecca

Areas: Abraj Al Bait (Ajyad).

One pocket here is dense enough to count: Abraj Al Bait, Ajyad (9 towers).

### Detroit

Areas: Downtown Detroit (Renaissance Center).

One pocket here is dense enough to count: Downtown Detroit, Renaissance Center (9 towers).

### Yokohama

Areas: Minato Mirai 21.

One pocket here is dense enough to count: Minato Mirai 21 (6 towers). The other 3 of the city's 9 towers stand in groups too small or too spread out to count.

### Rizhao

Areas: Shijiu (Donggang).

One pocket here is dense enough to count: Shijiu, Donggang (5 towers). The other 4 of the city's 9 towers stand in groups too small or too spread out to count.

### Denver

Areas: Downtown Denver.

One pocket here is dense enough to count: Downtown Denver (8 towers).

### Pohang

Areas: Jangseong-dong (Buk-gu).

One pocket here is dense enough to count: Jangseong-dong, Buk-gu (8 towers).

### Izmir

Areas: Bayraklı.

One pocket here is dense enough to count: Bayraklı (6 towers). The other 2 of the city's 8 towers stand in groups too small or too spread out to count.

### Fortaleza

Areas: Meireles beachfront.

One pocket here is dense enough to count: Meireles beachfront (5 towers). The other 3 of the city's 8 towers stand in groups too small or too spread out to count.

### Astana

Areas: Left Bank: Abu Dhabi Plaza (Esil).

One pocket here is dense enough to count: Left Bank: Abu Dhabi Plaza, Esil (6 towers).

### Cartagena

Areas: Bocagrande.

One pocket here is dense enough to count: Bocagrande (6 towers).

### Laibin

Areas: Laibin centre (Xingbin).

One pocket here is dense enough to count: Laibin centre, Xingbin (6 towers).

### Madrid

Areas: Cuatro Torres Business Area.

One pocket here is dense enough to count: Cuatro Torres Business Area (5 towers). One of the city's 6 towers stands apart from it.

### Cleveland

Areas: Downtown Cleveland (Public Square).

One pocket here is dense enough to count: Downtown Cleveland, Public Square (5 towers).

### Perth

Areas: Perth CBD.

One pocket here is dense enough to count: Perth CBD (5 towers).

### Tampa

Areas: Downtown Tampa.

One pocket here is dense enough to count: Downtown Tampa (5 towers).

### Auckland

Areas: Auckland city centre.

One pocket here is dense enough to count: Auckland city centre (5 towers).

### Columbus

Areas: Downtown Columbus.

One pocket here is dense enough to count: Downtown Columbus (5 towers).

## How to rebuild

Run `python3 build_density.py ../skyline-extent.geojson` from `tools/`. Pocket names and the extra popup sentences are in `tools/names.py`. The README there covers the water data and how to add a city.
