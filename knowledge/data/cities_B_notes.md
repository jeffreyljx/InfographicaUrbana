# Cities B: Jakarta, Osaka, Istanbul, Busan — completed buildings >= 150 m by sub-district

Method: en.wikipedia "List of tallest buildings in <city>" (all four list completed/topped-out buildings down to 150 m) was taken as the base list; sub-district assignment comes from the list's own location column (Osaka, Busan), from the sparse notes/rowspan structure plus per-building checks (Istanbul), or from address knowledge plus spot checks on skyscrapercenter.com / skydb.net / Wikipedia building pages (Jakarta). CTBUH city totals quoted in the brief: Jakarta 117/51, Osaka 46/5, Istanbul 57/12, Busan 77/25 (>=150 m / >=200 m). Snapshot date: 2026-09-05.

Files: jakarta_150m.csv, osaka_150m.csv, istanbul_150m.csv, busan_150m.csv (columns: name,height_m,floors,year,district_or_area,source_url,confidence).

---

## 1. Jakarta (5 administrative cities)

| Administrative city | >=150 m (Wikipedia-based) | >=200 m | Notes |
|---|---|---|---|
| South Jakarta (Jakarta Selatan) | 65 | 34 | SCBD, Kuningan, Mega Kuningan, Gatot Subroto, Setiabudi/east side of Sudirman, Kebayoran, Kemang |
| Central Jakarta (Jakarta Pusat) | 43 | 15 | Thamrin, west side of Sudirman (Karet Tengsin/Kebon Melati), Menteng, Kemayoran, Senayan-Gelora |
| West Jakarta (Jakarta Barat) | 18 | 3 | Central Park/Taman Anggrek (Tanjung Duren), Puri Indah/St Moritz, West Vista |
| North Jakarta (Jakarta Utara) | 6 | 4 | SeaView Condominium (Pantai Mutiara), Ancol Mansion |
| East Jakarta (Jakarta Timur) | 0 | 0 | none |
| Unverified | 1 | 0 | "Sky Tower" 167 m — could not identify the building |
| **Total in CSV** | **133** | **56** | CTBUH: 117 / 51 |

Gap vs CTBUH (+16 at 150 m, +5 at 200 m):
- Wikipedia pads the 150 m floor with 13 low-confidence Kemayoran entries (Dukuh Golf 1-4, Kemayoran Office 1-3, Royal Springhill 5-6, Springhill Terrace Lotus/Lavender/Magnolia/Marygold — all "150 m / 37 floors"), plus Aston II and ITC Kuningan at a flat 150 m. Most are almost certainly < 150 m by CTBUH measurement. Removing them brings the list to ~118, i.e. essentially the CTBUH total.
- Heights in Wikipedia are inflated for Menara Jakarta at Kemayoran: Azure Tower listed 288 m/77 fl but CTBUH says 200 m/55 fl (used 200); Equinox listed 254 m but its own Wikipedia page says 180 m (used 180). Neo SOHO, SOHO Capital, West Vista are entered as "200+" — treated as 200, so West Jakarta's 200 m count (3) is soft (range 0-3).
- SeaView Condominium J/K/L/M at 208 m (48 fl) look over-stated; CTBUH probably has them < 200 m, which would move 4 out of North Jakarta's 200 m column (range 0-4).
- CTBUH's Jakarta city page also shows Indonesia-1 (2 towers, Thamrin, Central) and Oasis Central Sudirman (2 towers) in its top-10, but their status is topped-out/under construction (2027-2028) — excluded.
- Boundary caveat: Senayan/GBK side (fX Residence, Fairmont) is administratively Gelora, Tanah Abang = Central Jakarta; the brief's rule "Senayan = South" would move 2 buildings (1 at 200 m+) to South. Sudirman was split by side: west side (Karet Tengsin/Kebon Melati) = Central, east side (Setiabudi/Karet Semanggi) = South.
- Duplicate row "Central Park Office Tower" on Wikipedia counted once.

Range for the top district: South Jakarta 63-67 at 150 m+ (33-35 at 200 m+); Central Jakarta 30-43 depending on how many of the 150-m Kemayoran fillers survive.

## 2. Osaka (city wards; Sakai and other prefecture cities excluded — the Wikipedia list is Osaka-city only)

| Ward | >=150 m | >=200 m | Notes |
|---|---|---|---|
| Kita-ku | 29 | 0 | Umeda (Grand Front, Grand Green, Umeda Twin Towers, Sky Building, JP Tower), Nakanoshima (Festival Towers, KEPCO, Parkhouse), Dojima, Temma/Tenroku |
| Chuo-ku | 10 | 1 | The Kitahama 209; OBP (Twin 21 x2, Castle Tower, Crystal Tower), Honmachi/Yodoyabashi residential |
| Nishi-ku | 4 | 0 | Hibikino Machi Sanctus, Ciella Horie, Metropolis, D'Grafort Higobashi |
| Minato-ku | 3 | 2 | ORC 200 / Osaka Bay Tower 200, X-Tower Osaka Bay 200 (CTBUH 201), ORC 200 Prio 167 |
| Fukushima-ku | 3 | 0 | City Tower Nishi-Umeda, The Tower Osaka, Osaka Fukushima Tower |
| Abeno-ku | 2 | 1 | Abeno Harukas 300; City Tower Grand Tennoji |
| Suminoe-ku | 1 | 1 | Cosmo Tower (Osaka Prefectural Sakishima Bldg / former WTC) 256 |
| Naniwa-ku | 1 | 0 | The Namba Tower |
| **Total** | **53** | **5** | CTBUH: 46 / 5 |

Gap: 200 m+ matches CTBUH exactly (5: Harukas, Cosmo Tower, Kitahama, X-Tower, ORC 200). The +7 at 150 m is borderline heights: Wikipedia carries several 150-157 m entries (Yodobashi Umeda Tower, Osaka Station North Gate, Yodoyabashi Station One, Meiji-Yasuda Umeda, Geo Tower Tenroku, D'Grafort, Fine Tower Toyosaki, Metropolis Tower) that CTBUH may list below 150 m or not at all; and two 2024-25 completions (Grand Green North Residence, Yodoyabashi Station One) may post-date the CTBUH count. Kita-ku range: 24-29 (still far ahead of Chuo-ku 8-10).

## 3. Istanbul (districts / ilçe)

| District | >=150 m | >=200 m | Notes |
|---|---|---|---|
| Şişli | 21 | 1 | Mecidiyeköy (Torun Center x3, Quasar x2, Trump, Nurol Tower, Torun Tower), Bomonti (Anthill x2, Sinpaş Queen, Divan, Rotana), Esentepe/Levent west side of Büyükdere Cad. (Istanbul Tower 205 - the only 200 m+ - Levent 199, Kristalkule, River Plaza, Istanbloom), Fulya (Selenium Twins x2), Şişli Plaza |
| Ataşehir | 14 | 4 | Istanbul Finance Center (CBRT 354, Ziraat x2, Halkbank x2, Vakıfbank), Metropol x3, Palladium, Allianz, Varyap, Andromeda, Modern Arya |
| Sarıyer | 10 | 3 | Maslak/Ayazağa (Spine, 42 Maslak x2, Maslak 1453 x3), Skyland x3 (Huzur mah.), Etro/Rams Beyond (2026, flagged) |
| Beşiktaş | 7 | 0 | Levent east side (İşbank Tower, Akbank/Sabancı), Zincirlikuyu (Çiftçi x2), Etiler (Mandarin Oriental x3, 2026, flagged) |
| Kartal | 5 | 0 | Maya Anatolium, Manzara Adalar, Moment x2, Istmarina |
| Üsküdar | 4 | 1 | Emaar Square x2 (Address 245), Akasya x2 |
| Esenyurt | 4 | 0 | Gümüş Panorama, Sembol, Aris Grand, Sheraton Residence |
| Kağıthane | 3 | 2 | Istanbul Sapphire 261 (4. Levent, west side), Nurol Life 220 (Seyrantepe), Sarphan Finans Park |
| Esenler | 2 | 0 | Tekstilkent Koza Plaza x2 |
| Ümraniye | 1 | 0 | Exen Plaza |
| Küçükçekmece | 1 | 0 | Terrace Tema B (Halkalı) |
| Başakşehir | 1 | 0 | Bulvar İstanbul |
| Beylikdüzü | 1 | 0 | Terrace Lotus |
| Unverified | 4 | 0 | Four Winds Residence x4 (156 m) — district not confirmed (Asian side) |
| Bağcılar, Bakırköy, Zeytinburnu, Maltepe, Kadıköy | 0 | 0 | none at 150 m+ on the list |
| **Total** | **78** | **11** | CTBUH: 57 / 12 |

Gap (+21 at 150 m, -1 at 200 m):
- Wikipedia counts each tower of a complex (Torun Center x3, Maslak 1453 x3, Four Winds x4, Anthill x2, Selenium x2, Çiftçi x2, Koza x2, Metropol B/C, Mandarin Oriental x3, 42 Maslak x2); CTBUH often has only the tallest or lists siblings below 150 m. Several 150-156 m entries (Torun/Deniz Tower, Moment, Bulvar, Sheraton Esenyurt, Istmarina, Metropol B/C, Terrace Lotus, Sembol) are borderline.
- 5 rows are 2026 or under-construction (Etro Residences/Rams Beyond, Mandarin Oriental Etiler x3, plus Terrace Lotus 2025) — CTBUH likely does not count them yet.
- 200 m+: CTBUH has Vakıfbank HQ Tower 1 at 221.3 m (Wikipedia 194 m) — adding it gives 12 = CTBUH. CTBUH also has Metropol at 280 m and Tower 205 at 220 m (heights differ, counts don't).
- Levent split: buildings on the west side of Büyükdere Cad. (Kanyon/Levent 199/Tower 205/Kristalkule) are Şişli (Esentepe); east side (İş Kuleleri, Sabancı) is Beşiktaş; 4. Levent/Sapphire is Kağıthane. Assignments for Tower 205, Levent 199, Kristalkule are medium confidence — if all three were Beşiktaş, Şişli would still lead (18 vs 10).
- Range for the top district: Şişli 15-21 at 150 m+ (1 at 200 m+); Ataşehir 11-14 at 150 m+ (4-5 at 200 m+, the most 200 m+ towers of any district).

## 4. Busan (gu)

| Gu | >=150 m | >=200 m | Notes |
|---|---|---|---|
| Haeundae-gu | 43 | 11 | LCT x3, Zenith x3, I'Park x3, WBC Palace x2, Centum City (Centum Star x3, Leadersmark, Centum Park x12, Sky Biz), AID Sea Colony x7, Kyungdong Jade x3, Marine City Xi, Park Hyatt, etc. |
| Nam-gu | 7 | 5 | BIFC 289, The W x4 (246, Yongho-dong), BI City x2 (Munhyeon) |
| Dong-gu | 7 | 2 | Hyupsung Marina G7 x2 (200), Majestower Beomil x3, Ocean Bridge x2 |
| Busanjin-gu | 6 | 1 | Seomyeon Central Star A-E (A 207), Lotte Hotel Busan |
| Buk-gu | 4 | 0 | Royal Duke Vista 48 x4 (Hwamyeong) |
| Seo-gu | 3 | 1 | Hillstate Ijin Bay City A (247), B, C |
| Dongnae-gu | 2 | 0 | SK Hub Sky x2 |
| Suyeong-gu, Saha-gu, Yeonje-gu etc. | 0 | 0 | none on list |
| **Total** | **72** | **20** | CTBUH: 77 / 25 |

Gap (-5 at 150 m, -5 at 200 m): Wikipedia lists FEWER than CTBUH. CTBUH's Busan top-10 has WBC The Palace 1 at 265 m (Wikipedia 186 m) — likely both WBC Palace towers are 200 m+ in CTBUH (+2). Other candidates for the missing 200 m+ towers: CTBUH heights for Centum Star A/C, Daewoo Aratrium (198) or Hyupsung G7 rounding; missing 150 m+ entries are probably recent (2023-2026) completions in Haeundae (e.g. Elcity/Centum area residential towers) or Nam-gu/Dong-gu (North Port redevelopment). Since Haeundae holds 60% of the list, the 5 missing towers most plausibly fall there. Haeundae-gu range: 43-48 at 150 m+, 11-16 at 200 m+. Note the CSV uses CTBUH's 2019 completion for LCT (Wikipedia shows 2010, which is wrong).

## Cross-cutting caveats
- Heights are architectural per Wikipedia unless a CTBUH figure was substituted (Azure Tower, Equinox Tower). Where Wikipedia and CTBUH disagree it is noted in the district field or here.
- Confidence column: high = district certain from source or unambiguous address; medium = assigned from address knowledge / boundary-side reasoning; low = building identity or height/status doubtful.
- The Skyscraper Center city pages only show a top-10 and their "completed" filter is not reliable through the fetch tool (U/C towers appeared), so CTBUH totals were taken from the brief rather than re-derived.
