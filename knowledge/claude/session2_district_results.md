# District tally — session 2 results (2026-09-05, scheduled run)

Scope of this run: the four scheduled priorities — (1) Futian / Nanshan / Tianhe / Pudong at ≥150 m, (2) Hong Kong Sai Kung and Yau Tsim Mong plus the 569-vs-669 gap, (3) the un-finished cities, (4) the Wikipedia-vs-CTBUH discrepancies. Basis throughout: completed buildings, architectural height, CTBUH/CVU Skyscraper Center as the authority where a page could be fetched. Companion files are listed in §7.

## 1. Headline: what changed in the #2–#5 global picture

| District | Previous status | Now | Basis |
|---|---|---|---|
| **Nanshan** (Shenzhen) | ~100–130 | **~125–155 (central ≈140)** — estimate, not enumerated | 200 m+ anchor 60–61 exact; 150–199 m band still not enumerable from any reachable source |
| **Futian** (Shenzhen) | ~100–130 | **~115–140 (central ≈125)** — estimate | 200 m+ anchor 54 exact; 3 band towers verified on CTBUH |
| **Sai Kung** (Hong Kong) | 70–130 | **110 towers ≥150 m verified building-by-building (101 CTBUH rows); conservative 95 towers / 86 rows if the fifteen 151–154 m towers are excluded** | CTBUH complex pages for every TKO / LOHAS Park estate |
| **Old Toronto** | not done | **102 (≥200 m: 31)** | Wikipedia list (CTBUH-sourced) filtered to completed; CTBUH city total 109 |
| **Tianhe** (Guangzhou) | 75–100 | **75 on the 2021-era list (range 70–79), ≥200 m: 30**; a realistic 2026 figure is ~85–95 once Financial City / Pazhou-era completions are added | All 160 list rows now district-assigned (82 with a source) |
| **Singapore Downtown Core** | not done | **77 (73 excluding six rows at exactly 150 m); ≥200 m: 35** | Wikipedia list (CTBUH-sourced) |
| **Pudong** (Shanghai) | 65–85 | **~72 (range 60–82); ≥200 m exact = 29 of 70 listed (29–33 vs CTBUH's 76 citywide)** | All 13 unassigned rows resolved via CTBUH pages; 40 band towers documented, 19 verified |
| **South Jakarta** | not done | **65 (63–67); ≥200 m: 34** | Wikipedia list, filler rows removed |
| **Yau Tsim Mong** (Hong Kong) | 70–130 | **39 towers verified (23–30 CTBUH rows); realistic ~50–60** once six Olympic-station estates (Harbour Green, Long Beach, Island Harbourview, Central Park, Park Avenue, Hampton Place) are height-checked | CTBUH complex pages + Wikipedia; The Waterfront (142 m) and Imperial Cullinan (140 m) fall below the line |

Tentative order behind Manhattan, on a per-tower basis: **Nanshan (est.) > Futian (est.) > Sai Kung 110 ≈ Old Toronto 102 > Tianhe 75–95 > Downtown Core 77 ≈ Pudong ~72 > South Jakarta 65 > Yau Tsim Mong 39–60.** Two things could still reorder the top: (a) Futian's legacy 150–199 m office stock could overturn Nanshan's 7-tower lead at 200 m+ (the Shenzhen agent puts Nanshan ahead at only ~60–65 % confidence); (b) Sai Kung would drop to 95 (and below Old Toronto) if the project decides to exclude at-threshold 151–154 m towers, and to 101 on a CTBUH-row basis. Tianhe and Pudong are now confirmed below both Shenzhen districts and below Sai Kung at every threshold.

**Decision still needed before publishing:** count CTBUH *rows* or physical *towers*? CTBUH merges podium-linked towers into one row (Sai Kung: 110 towers vs 101 rows; YTM: 39 vs 23–30; The Arch = 4 towers / 1 row; Ocean Shores = 10 towers / 4 rows). Every Hong Kong district — and Seoul/Bangkok/Jakarta residential complexes — moves by 5–15 % depending on the choice. The existing Shenzhen/Guangzhou/Shanghai CSVs count towers.

## 2. Priority 1 — the four core districts

### Shenzhen (Futian vs Nanshan) — still not enumerable
- Anchors: Skyscraper Atlas (end-2025) — city 501 at 150 m+, 219 at 200 m+; Futian 54 / Nanshan 61 / Luohu 14 at 200 m+. CTBUH cities page (fetched today) — Shenzhen 471 / 200 / 22. en.wikipedia lead — 469 / 200.
- The 150–199 m band therefore holds 271–282 buildings citywide (1.3× the 200 m+ count). Applying a district-adjusted ratio of 1.0–1.3 gives Futian ~115–140 and Nanshan ~125–155.
- Direction of the recent pipeline: of ~50 band towers in Wikipedia's 150 m+ under-construction table, ~12 are clearly Nanshan (Qianhai/Houhai/Shenzhen Bay) vs ~2 clearly Futian; residential ≥180 m planning tally 9 Nanshan vs 7 Futian. Everything points the same way, so **Nanshan is the favoured #2, but this is "probably, not established."**
- Why it is not settled: the Skyscraper Center's full list is member-only and its explore-data tool needs a POST (the compare-data/submit GET redirects to the default top-100), SkyscraperPage city lists do not render, and the only complete 150 m+ list with a 区 column — zh.wikipedia 深圳摩天大楼列表 — is unreachable in this sandbox in every form tried (direct, mobile, wikiwand, wikizero, translate proxy, mirrors). A curl/Overpass/Wikidata route is proxy-blocked. **Any machine with ordinary internet can settle this in minutes with a pivot on that zh.wikipedia table** (or by walking Skyscraper Center building pages by numeric id, each of which shows a street address).

### Guangzhou (Tianhe) — list fully district-assigned
- Per-district (≥150 m verified/probable/total; ≥200 m): Tianhe 70/5/**75** (30); Haizhu 34/13/47 (15); Yuexiu 15/6/21 (4); Panyu 5/2/7 (5); Liwan 4/1/5 (0); Zengcheng 3 (3); Baiyun 2; Nansha 2 (1); Huangpu 1 (1); unassigned 4 (Pearl River One 241 m, Deshun 200 m, Pol Tower V, Lifeng Center).
- Corrections to the session-1 file: Guangdong Business Center (375.5 m, 2025) is in **Pazhou West, Haizhu — not Baiyun**; Huijin Center 1 = CTBUH "Shimao Canton Financial Center" (Tianhe); Junchao Plaza is Tianhe; The Riverside 1–4 are **Liwan**, not Haizhu; Cadre City Plaza = Kaidar TOD, Zengcheng.
- Seven post-2020 completions added (JOYY/Huanju Tower 222 m, Nansha Yuexiu IFC A/B, Window of Guangzhou B 196 m, Oppein 180 m, Vipshop HQ 173 m, 37 Interactive HQ 172 m). The list (167 rows) is still ~45 short of CTBUH's 212; the gap sits in Financial City (Tianhe: "18 towers in the starting zone, 11 in use"), Pazhou West ("at least 21 towers operational"), Baiyun New Town, Wanbo and Nansha — hence the ~85–95 realistic Tianhe figure.

### Shanghai (Pudong)
- All 13 previously unassigned ≥200 m rows resolved from CTBUH pages by numeric id: CITIC Ruibo T1/T2, Golden Landmark → Pudong (Lujiazui); **Shanghai SK Group Tower (275 m) → Pudong (Qiantan), not Xuhui**; 66 Tower 1/2 = Grand Gateway → Xuhui; AI W = MGM West Bund → Xuhui; Pacific New World = CPIC Xintiandi → Huangpu; Oasis Skyway = Pullman Skyway → Huangpu; CITIC Plaza, No. 1 Shanghai → Hongkou; BM Plaza, Dong Hai Plaza → Jing'an.
- ≥200 m by district (70 listed; CTBUH says 76): **Pudong 29**, Jing'an 12, Huangpu 9, Xuhui 6, Putuo 6, Hongkou 5, Changning 2, Yangpu 1. Missing ~6 include ITC Tower 2 and Greenland Bund Centre T1, so Pudong is 29–33.
- 150–199 m band: 19 Pudong towers verified on CTBUH/Wikipedia (World Plaza 199.9, BEA 198, CFFEX 195, Shimao Riviera Garden ×7, Lujiazui Century T1 190, Huaneng 188, Bao'an 188, Aurora 185, Mirae 180, Century Link A/B, Tomson Riviera 1, CSDC), +2 Lingang BOC twins (195 m, Jan 2026), +19 probable from Chinese lists, +6 possible → **Pudong ≥150 m ≈ 72 (60–82)**. Lujiazui alone ≈ 50, matching Skyscraper Atlas's "nearly one quarter" of 205.
- Remaining gap: CTBUH's Shanghai rank ladder (#71 at 203 m, #88 at 195 m, #98 at 188 m) implies ~108 completed buildings between 150 and 188 m that no reachable source enumerates.

## 3. Priority 2 — Hong Kong

### Sai Kung District (all Tseung Kwan O / Tiu Keng Leng / Hang Hau)
LOHAS Park Phases 1–11 = **43 towers, all 177–229 m** (every tower clears 150 m; Villa Garda I–III completed 2025). Other TKO estates ≥150 m: Metro Town + Le Point 9 (188–205), Ocean Shores 15 (171–174), Park Central 12 (162–168), TKO Plaza 8 (168), Residence Oasis 6 (165–168), Area 56 hotels 2 (163), Metro City I 6 (154), East Point City 7 (151), Nan Fung Plaza 1–2 (151). **Total 110 towers / 101 CTBUH rows.** Checked and excluded: The Wings (133 m est.), Nan Fung Plaza 3/5/6 (137–141), Monterey, Alto, Savannah, Papillons, Bauhinia Garden. Not counted: LOHAS Phase 12 (completion unverified), Phase 13 (U/C), Metro City II/III (unverified, plausibly 140–160 m).

### Yau Tsim Mong
Union Square = 15 towers / 10 rows (ICC 484; Cullinan I/II 270; The Arch ×4 231; Harbourside 251; Sorrento ×5 206–256). W Hotel/HarbourView Place is inside Cullinan II — not a third tower. **The Waterfront ×6 (142.46 m) and Imperial Cullinan ×5 (140 m) are below 150 m and drop out.** Plus Victoria Dockside 272.5, Masterpiece 261, Langham Place Office 255, Hermitage ×6 (214–234), Victoria Towers ×3 (213), Shining Heights 213, One SilverSea ×8 (182), Florient Rise ×3 (152–174) → **39 towers verified**. Cullinan West is Sham Shui Po; Harbourfront Landmark is Kowloon City; Mong Kok East Station (312 m) is U/C to 2030.

### 569 vs 669
- 569 = CTBUH/CVU completed-only count (Wikipedia "cities with the most skyscrapers", Feb 2026; Skyscraper Atlas mirrors it; the HK list lead's 567 is an early-2025 snapshot of the same count).
- 669 = Guinness World Records "City with the most buildings 150 m or taller" (30 Jan 2025, credited to CTBUH), which also gives Shenzhen 626, New York 434, Dubai 424 — each 100–160 *above* the later completed-only figures. Since a completed count can only grow, the Guinness numbers cannot be an older completed count; the pattern matches a Skyscraper Center query run with **all statuses** (completed + U/C + topped-out + proposed/on-hold/never-completed). A transcription slip is the only alternative. (The separate Guinness "most skyscrapers" record is 2,580 at ≥100 m, 2019 — different threshold.)
- Consequence: 669 does **not** shift any district upward. What *does* shift Hong Kong districts upward relative to a Wikipedia-table tally (which only covers ≥179 m, 166 rows) is the 150–179 m residential stock — Sai Kung (40+ rows alone), Kwai Tsing/Tsuen Wan, Sham Shui Po, Eastern, Tuen Mun (Sun Tuen Mun Centre ×10 at exactly 150 m), Kowloon City — which must be pulled from CTBUH complex pages.

## 4. Priority 3 — the un-finished cities (completed, ≥150 m / ≥200 m)

| City (CTBUH total) | Target area | ≥150 m | ≥200 m | Notes |
|---|---|---|---|---|
| Toronto (109/32) | **Old Toronto** | **102** | **31** | Etobicoke (Humber Bay) 8/1, North York 1. Wikipedia 117 rows → 111 completed (SkyTower, One Bloor West, One Delisle, 400 King W, Kipling, Alias not complete); 111 vs 109 because CTBUH still lists CIBC Square II as U/C. 200 m+ matches CTBUH exactly. |
| Moscow (70/27) | **Presnensky** (Moscow-City + Shelepikha/Headliner + Kudrinskaya) | **28** | **18** | Ramenki 16, Khoroshevo-Mnevniki 8. Strict-completed citywide 104 vs CTBUH 70 — tower-by-tower residential complexes CTBUH does not track; 19 rows dated 2027 excluded, 14 dated 2026 flagged. |
| Sydney (47/15) | **Sydney CBD** (City of Sydney incl. Barangaroo, Haymarket) | **38** | **15** | North Sydney 5, Chatswood 2, St Leonards 1, Rhodes 1. Sydney-excluding-Parramatta = exactly CTBUH's 47/15. |
| Sydney | **Parramatta CBD** | **8** (7 if The Lennox's CTBUH 148.6 m is used) | **2** | CTBUH files Parramatta as a separate city; 8 Phillip St (218 m) still topped-out only. |
| Singapore (102/35) | **Downtown Core** | **77** (73 excl. six at exactly 150 m) | **35** | Queenstown 16 (Dawson HDB), Bukit Merah 11, Outram 8 (Pinnacle@Duxton), Orchard 6, Newton 4, Kallang 2, River Valley 2. List 126 vs CTBUH 102 = HDB blocks + threshold rows. DUO, mTower, TwentyOne Anguilla assignments flagged medium/low. |
| Jakarta (117/51) | **South Jakarta** | **65** (63–67) | **34** | Central 43/15, West 18/3, North 6/4, East 0. Wikipedia 133 → ~118 after removing 13 Kemayoran "150 m / 37 fl" filler rows; Azure/Equinox heights corrected to CTBUH. |
| Osaka (46/5) | **Kita-ku** (Umeda + Nakanoshima) | **29** (24–29) | 0 | Chuo-ku 10/1, Nishi-ku 4, Minato-ku 3/2, Fukushima 3, Abeno 2/1, Suminoe 1/1. 200 m+ matches CTBUH; Sakai excluded. |
| Istanbul (57/12) | **Şişli** | **21** (15–21) | 1 | Ataşehir 14/4 (leads at 200 m+), Sarıyer 10/3, Beşiktaş 7, Kartal 5, Üsküdar 4/1, Kağıthane 3/2, Esenyurt 4. Over-count vs CTBUH from per-tower complexes and five 2026/U-C rows; Four Winds ×4 district unverified. |
| Busan (77/25) | **Haeundae-gu** | **43** (43–48) | **11** (11–16) | Nam-gu 7/5, Dong-gu 7/2, Busanjin 6/1. Wikipedia lists *fewer* (72/20) than CTBUH; CTBUH has WBC The Palace at 265 m (Wikipedia 186). |

## 5. Priority 4 — database discrepancies and the chosen spine

| City | Wikipedia figure | CTBUH/CVU (fetched 2026-09-05) | Cause |
|---|---|---|---|
| Seoul | 126 (city list lead: "of which only 82 are recognized by the CTBUH"); 127 rows across 18 gu | **86 / 21 / 2** | Crowd-compiled list counts every tower of apartment complexes (Tower Palace, Lotte Castle, Trimage, Raemian, Hyperion) at 150–165 m that developers never submitted to CTBUH |
| Metro Manila | 215 (lead; ranked table only 162 rows) | **no CVU row**; CVU city rows Makati 59 + Taguig 19 + Mandaluyong 18 + Pasig 14 + Quezon City 10 + Manila 9 = **129** (+San Juan 2; Pasay/Parañaque/Muntinlupa ≤2 each) | Height column is literally "Height (Emporis)"; 215 includes ~53 buildings with floor-count-estimated heights excluded from the article's own table; "Metro Manila" is not a CVU city |
| Bangkok | 204 (lead: "of which 129 are listed on the CTBUH database"); 203 rows across 18 khet | **129 / 36 / 3** | Condo towers (Park Origin, Ashton, Noble, Ideo, Rhythm, The Line, Skyrise) at 150–165 m not in CTBUH |
| Hong Kong | 569 (cities list) / 567 (HK list lead) / 669 (Guinness) | **569 / 102 / 6** | See §3 — 669 is an all-statuses query, not a completed count |
| Busan | ~70–72 (under-maintained list) | **77 / 25 / 4** | Wikipedia incomplete; runs the other way |

The Wikipedia ranking page itself now says its data "derives from the Skyscraper Center database", that "the CVU's figures may undercount ... and are unreliable for many non-Western cities", and footnote [a] on Manila/Bangkok/Tokyo/Mumbai/Moscow reads "This figure is from the corresponding linked article. It includes topped-out buildings that are not fully completed." CTBUH's own FAQ: it "receives most of its information directly from companies involved in the projects" and "it is unlikely all tall buildings are represented."

**Adopted authority (recommendation applied to the write-up):** CVU cities page, Completed status, architectural height ≥150 m, dated at fetch (2026-09-05), as the citywide spine for every city; Metro Manila built from CVU city rows (129 + San Juan 2); Wikipedia district-column lists used only for district *shares* of the CVU total, never mixed into it; the Wikipedia ranking table not cited. State the known under-coverage explicitly: Seoul ≈ −32 %, Bangkok ≈ −37 %, Metro Manila ≈ −20 %, Moscow ≈ −33 % (residential complexes). Full CVU counts for 52 cities are in `ctbuh_city_counts.csv` (e.g. Hong Kong 569/102/6, Shenzhen 471/200/22, NYC 324/102/18, Dubai 273/132/33, Guangzhou 212/69/14, Wuhan 209/76/8, Shanghai 206/76/9, Kuala Lumpur 201/74/7, Tokyo 178/40/1, Chongqing 156/64/6, Chicago 137/38/7, Bangkok 129, Jakarta 117/51, Mumbai 113/51, Toronto 109/32, Singapore 102/35, Seoul 86/21, Nanjing 82/39, Melbourne 79/30, Busan 77/25, Moscow 70/27, Panama City 68/25, Miami 68/9, Makati 59/21, Istanbul 57/12, Doha 57/30, Incheon 50/8, Sydney 47/15, Osaka 46/5, Abu Dhabi 45/23).

## 6. What still blocks an exact answer, and the cheapest fix for each
1. **Futian vs Nanshan** — one pivot on zh.wikipedia's 深圳摩天大楼列表 (150 m+, 区 column) from any unrestricted machine; or a CVU member export. This is the single item that decides global #2 vs #3.
2. **Pudong 150–188 m** (~108 towers citywide in that band) — same zh.wikipedia route (上海市摩天大楼列表, 170 m+ with 区), or CVU export.
3. **Tianhe post-2021 completions** — walk Skyscraper Center building pages for Financial City / Pazhou West / Baiyun New Town; ~45 buildings.
4. **Yau Tsim Mong** — fetch six CTBUH complex pages (Harbour Green, The Long Beach, Island Harbourview, Central Park, Park Avenue, Hampton Place); plus Metro City II/III for Sai Kung.
5. **Rows vs towers** — a project-level decision, then re-state Hong Kong (and Seoul/Bangkok/Jakarta/Moscow) on the chosen basis.

Tooling note for the next run: this session exhausted its 200-call WebSearch budget across the seven research agents; WebFetch kept working. zh.wikipedia, wikidata, Overpass, web.archive.org, gaoloumi, zhihu and the Skyscraper Center explore-data tool are unreachable from this sandbox; Skyscraper Center *building* (`/building/<slug>/<id>`) and *complex* (`/complex/<id>`) pages are reachable and give address + height + status, which is how Hong Kong and the Shanghai unassigned rows were resolved.

## 7. Files written to the project this run
- `data/shenzhen_150_200_band.csv`, `data/shenzhen_notes.md` — 36 band towers (3 CTBUH-verified), quotes, estimate reasoning.
- `data/guangzhou_150m_by_district_v2.csv` (167 rows, all assigned, source column), `data/guangzhou_notes.md`.
- `data/shanghai_200m_by_district_v2.csv` (70 rows, all assigned), `data/shanghai_150_200_band.csv` (~80 rows), `data/shanghai_notes.md`.
- `data/hongkong_saikung_ytm.csv` (166 rows incl. exclusions), `data/hongkong_notes.md`.
- `data/toronto_150m.csv`, `data/moscow_150m.csv`, `data/sydney_150m.csv`, `data/singapore_150m.csv`, `data/cities_A_notes.md`.
- `data/jakarta_150m.csv`, `data/osaka_150m.csv`, `data/istanbul_150m.csv`, `data/busan_150m.csv`, `data/cities_B_notes.md`.
- `data/seoul_150m.csv` (127 rows, gu), `data/manila_150m.csv` (162 rows, city), `data/bangkok_150m.csv` (203 rows, khet), `data/ctbuh_city_counts.csv` (52 cities), `data/discrepancies_notes.md`.
Session-1 files (`four_district_tally_summary.md`, the three original CSVs) are unchanged; the v2 CSVs supersede the Guangzhou and Shanghai originals.
