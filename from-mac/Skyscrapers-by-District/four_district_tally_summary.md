# Futian, Nanshan, Tianhe, Pudong — building-level tally (session 1)

Threshold: completed/topped-out buildings, architectural height, CTBUH (Skyscraper Center) building set.
Companion files: `shenzhen_200m_by_district.csv` (140 rows), `shanghai_200m_by_district.csv` (70 rows), `guangzhou_150m_by_district.csv` (160 rows).

## 1. What is now exact: the ≥200 m split

| District | ≥200 m counted (building-level) | Coverage of CTBUH city total | Cross-check |
|---|---|---|---|
| **Nanshan** (Shenzhen) | **60** verified | Wikipedia table lists 140 of CTBUH's 200 | Skyscraper Atlas: 61 |
| **Futian** (Shenzhen) | **54** verified | same table | Skyscraper Atlas: 54 (exact match) |
| **Tianhe** (Guangzhou) | **21 verified + 5 probable = 26**, plus up to 15 unassigned candidates | Wikipedia lists 59 of CTBUH's 67 | none available |
| **Pudong** (Shanghai) | **25 verified**, plus up to 11 unassigned candidates | Wikipedia lists 70 of CTBUH's 74 | Skyscraper Atlas: "nearly a quarter" of the city's 150 m+ towers are in Lujiazui alone |

Other Shenzhen districts at ≥200 m (verified): Luohu 14 (Atlas: 14), Longgang 5, Bao'an 3, Longhua 2, Yantian 2. The 60 towers missing from the Wikipedia table relative to CTBUH's 200 are overwhelmingly outside the core three districts — Skyscraper Atlas's own database gives Shenzhen 219 at ≥200 m with Nanshan 61 + Futian 54 + Luohu 14 = 129, leaving ~90 in Bao'an, Longgang, Longhua, Guangming, Pingshan and Yantian.

Shanghai ≥200 m by district (verified / probable): Pudong 25, Jing'an 10+1, Huangpu 7, Putuo 6, Xuhui 3+1, Hongkou 3, Changning 2, Yangpu 1, unassigned 11.

Guangzhou ≥200 m by district (verified / probable): Tianhe 21+5, Haizhu 7+2, Yuexiu 3+1, Panyu 2+1, Huangpu 1, Baiyun 0+1, unassigned 15.

## 2. What remains bounded, not exact: the ≥150 m counts

| District | Verified minimum (≥150 m) | Best-supported range | Why not exact |
|---|---|---|---|
| Futian | 54 (the ≥200 m set) | ~100–130 | No public building-level list exists for Shenzhen's ~270 towers in the 150–200 m band |
| Nanshan | 60 (the ≥200 m set) | ~100–130 | same |
| Tianhe | 45 verified (+7 probable = 52) of 160 listed | ~75–100 | 67 of the 160 listed towers still unassigned; the list is also ~48 towers stale vs CTBUH's 208 |
| Pudong | 25 (the ≥200 m set) | ~65–85 | Shanghai's 150–200 m band (~130 towers) is not published anywhere fetchable; Lujiazui ≈ 50 per Skyscraper Atlas |

## 3. Ranking implications for the global list

- At ≥200 m the order is settled and not close: **Nanshan (60–61) > Futian (54) >> Tianhe (26–41) ≈ Pudong (25–36)**. Both Shenzhen districts have more 200 m+ towers than any district outside Manhattan (~95) and Dubai's Marina/Business Bay/Downtown communities.
- At ≥150 m the Futian-vs-Nanshan order is still unresolved: Futian's older CBD and Huaqiangbei have many 150–200 m offices, Nanshan's Houhai/Qianhai/High-Tech Park have many 150–200 m towers completed 2015–2025. Either could be #2 globally behind Manhattan.
- Tianhe and Pudong are almost certainly below both Shenzhen districts at every threshold, and roughly tied with each other; Hong Kong's Sai Kung (LOHAS Park) and Yau Tsim Mong remain the other candidates in the 70–130 band.

## 4. Method and sources

- Shenzhen: the CTBUH-sourced Wikipedia ≥200 m table carries a District column for all 140 rows; tallied row by row (file 1). Skyscraper Atlas's Shenzhen page independently reports Futian 54 / Nanshan 61 / Luohu 14 — two of three match exactly.
- Shanghai: the Wikipedia ≥200 m table did not render, but its 70 completed-building citations (each a Skyscraper Center record) were used as the enumeration; districts assigned from known locations (Lujiazui, Nanjing West Road, North Bund, etc.) and flagged verified/probable/unassigned (file 2).
- Guangzhou: the Wikipedia list is a full ≥150 m list (160 rows, last updated 2021) with no district column; districts assigned from known locations and flagged (file 3). 67 rows — mostly 1998–2010 residential towers such as Jade Pavilion, Coral Garden, King Peak Garden, The Riverside, Regal Harbour — are unassigned; most sit on the Haizhu riverfront (Binjiang East) or the Tianhe riverfront (Liede), so Tianhe's final figure likely rises well above 52.
- Blocked sources this session: the Skyscraper Center's full per-city building lists (member-only; only a top-10 shows), SKYDB district pages (member-only), zh.wikipedia district-tagged lists (not fetchable), gaoloumi.com city lists (blocks automated access).

## 5. What would close the gap (in priority order)

1. A Skyscraper Center (CVU) membership export, or SKYDB export, of all Shenzhen and Shanghai buildings 150–200 m with coordinates — this single dataset settles Futian vs Nanshan and gives Pudong exactly.
2. zh.wikipedia's 深圳摩天大楼列表 / 上海市摩天大楼列表 / 广州摩天大楼列表, read manually or via a mirror: they list 150 m+ (Shanghai: 170 m+) towers with a 区 (district) column.
3. Resolve the 67 unassigned Guangzhou rows and 11 unassigned Shanghai rows in the CSVs by address lookup (Baidu/Amap or the Skyscraper Center building pages); the CSVs are formatted so each verified row can simply have its flag flipped.
4. Refresh the Guangzhou list with the ~48 post-2021 completions missing from Wikipedia (Financial City, Pazhou West, Baiyun New Town, Nansha) before finalizing Tianhe.
