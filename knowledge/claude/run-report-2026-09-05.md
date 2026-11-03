# Skyscraper district tally — scheduled run report, 2026-09-05

## Bottom line

The scheduled run could **not** execute the plan as written. From the cloud sandbox, the Skyscraper Center's filter/compare tool, Wikidata SPARQL, Chinese Wikipedia and every query-string URL are unreachable (details below). Priorities 1 and 2 (Futian / Nanshan / Tianhe / Pudong and the Hong Kong threshold checks) therefore made no progress. What did work: English-Wikipedia tables that already carry a district column. That produced complete first-pass district tallies for **Seoul, Bangkok and Metro Manila**, the raw Guangzhou ≥150 m list (160 rows, district not yet assigned), and the citywide figures needed for Priority 4.

## What is blocked from a scheduled run (and how to unblock)

| Source | Result from this run | Notes |
|---|---|---|
| skyscrapercenter.com `/compare-data` (POST) and `/buildings?status=…&location=…` | Blocked | Fetch tool only allows URLs that appeared verbatim in a web-search result; any other query string is stripped, so the filter tool falls back to "100 Tallest in the World". The one working URL is the indexed `?status=construction&location=city-shenzhen` page (100 tallest UC in Shenzhen). Even where it works, the list is capped at 100 and the `year=` parameter is a snapshot year, not completion year, so it cannot beat the cap for ≥150 m. |
| skyscrapercenter.com city / building pages | Fetchable once surfaced by search | Building pages carry a street address but **no district field** — district would still need geocoding. Shenzhen city page shows no 150 m+ count ("CVU Member access required" for the full DB). |
| skyscraperpage.com `/cities/?cityID=24` | Only the indexed first page | Says 3,085 Shenzhen entries, 100 per page, 31 pages; the `offset=` pagination URLs are not fetchable. |
| query.wikidata.org SPARQL | Blocked (proxy 403) | Would have been the cleanest route: P2048 height ≥150 plus P131 located-in district. |
| zh.wikipedia.org | Blocked ("cache-only domain") | 深圳摩天大楼列表 etc. unavailable. |
| en.wikipedia.org | Works | Only after a WebSearch surfaces the exact URL. |
| Shell network (curl/python) | Blocked for all of the above | Organization egress policy. |

**Recommendation:** run Priorities 1–2 interactively (where you can approve fetches), or re-create this scheduled task from the Claude desktop app with your computer attached so a script can call the Skyscraper Center compare-data endpoint and Wikidata directly from your machine. The cloud sandbox alone cannot do the enumeration.

## Priority 4 — citywide totals as of the current Wikipedia intros (all cite CTBUH)

| City | Wikipedia count ≥150 m | CTBUH-recognised | Gap | Table in Wikipedia |
|---|---|---|---|---|
| Hong Kong | **567** (2025, "according to CTBUH") | 567 | The 569-vs-669 gap: Wikipedia has now converged on the CTBUH number (567). 669 is the Guinness/other-source figure. Recommend 567 as the spine. | Only down to 180 m (166 ranked rows), no district column |
| Shenzhen | 469 (2025) | — | Article also carries an older "over 443 completed" sentence | Only down to 200 m (141 rows); has a "tallest per district" mini-table (7 districts) |
| Guangzhou | 204 (2025) | — | Table has 160 rows ≥150 m, so ~44 towers are in the CTBUH count but not tabulated | Down to 150 m, no district column |
| Shanghai | 193 (2025) | — | — | Only down to 200 m, no district column |
| Seoul | 126 (March 2024 sentence) | 82 (per the same sentence; you had noted 86) | Table extraction gives 127 rows | Down to 150 m, **has district (gu) column** |
| Metro Manila | 215 (Nov 2025) | ~129 (your CVU component-city sum) | Table holds only 162 rows | Down to 150 m, **has city column** |
| Bangkok | 204 (Dec 2025) | 129 | Table extraction gives 202 rows | Down to 150 m, **has district (khet) column** |

Decision recorded: use CTBUH/CVU as the spine citywide (your recommendation). Note that for Seoul, Manila and Bangkok the Wikipedia tables include many residential towers CTBUH has not entered, so district tallies from Wikipedia will run 30–60 % above a CTBUH-only tally. Both numbers are kept below; publish the CTBUH one and footnote the Wikipedia one.

## First-pass district tallies (English Wikipedia tables, ≥150 m, completed)

### Seoul (127 rows extracted; intro says 126)
Gangnam 19 · Yeongdeungpo 17 · Yongsan 16 · Seongdong 12 · Dongdaemun 9 · Songpa 8 · Yangcheon 8 · Gwangjin 6 · Gangdong 6 · Guro 5 · Jungnang 5 · Seocho 4 · Mapo 3 · Jongno 3 · Seongbuk 2 · Jung 2 · Dobong 1 · Dongjak 1

### Bangkok (202 rows extracted; intro says 204 — up to 2 rows may be missing)
Pathum Wan 30 · Watthana 25 · Khlong Toei 24 · Bang Rak 19 · Ratchathewi 17 · Sathon 16 · Huai Khwang 15 · Khlong San 11 · Chatuchak 11 · Phra Khanong 7 · Yan Nawa 5 · Bang Kho Laem 5 · Din Daeng 5 · Phaya Thai 4 · Bang Na 3 · Thonburi 2 · Bang Sue 2 · Rat Burana 1

### Metro Manila (162 rows extracted = table size; intro's 215 figure not reflected in the table)
Makati 66 · Taguig 24 · Mandaluyong 21 · Pasig 20 · Manila 15 · Quezon City 8 · San Juan 6 · Pasay 2

Caveat on one row: the table lists "Park Central South Tower" twice (248 m/2022 and 189 m/2025); the second is almost certainly Park Central **North** Tower and was recorded as such — verify.

### Guangzhou (160 rows extracted, ≥150 m; district NOT assigned)
Raw list saved as `guangzhou_150m_wikipedia.csv`. Tianhe assignment still needs a per-building check; the only district hints in the table are notes such as "first supertall outside Tianhe District" (Poly Pazhou C2, Haizhu). Because the CTBUH count is 204 and the table 160, Tianhe's exact number cannot come from Wikipedia alone.

## Where this ranks against the ~90–120 band

None of the districts tallied this run reaches the #2–#5 band: the top non-Chinese-mainland districts found are Makati (66, Wikipedia basis), Pathum Wan (30) and Gangnam (19). That is consistent with the working hypothesis that ranks #2–#5 are decided among Futian, Nanshan, Tianhe and Pudong, with Hong Kong's Sai Kung / Yau Tsim Mong the only other candidates — all of which still need the blocked CTBUH enumeration.

## Files written to the project
- `data/seoul_150m_wikipedia.csv` (127 rows, with district)
- `data/bangkok_150m_wikipedia.csv` (202 rows, with district)
- `data/metro_manila_150m_wikipedia.csv` (162 rows, with city)
- `data/guangzhou_150m_wikipedia.csv` (160 rows, no district yet)

## Not done this run
- Futian / Nanshan / Tianhe / Pudong enumeration (blocked — see above)
- LOHAS Park / Union Square 150 m checks (Hong Kong Wikipedia table stops at 180 m; CTBUH blocked)
- Toronto, Moscow, Sydney, Singapore, Jakarta, Osaka, Istanbul, Busan (not started — same blocker for anything below Wikipedia's per-city cutoff; Toronto/Moscow/Sydney Wikipedia tables should be checked for district columns next run)

Sources: Wikipedia list pages for Shenzhen, Shanghai, Guangzhou, Hong Kong, Seoul, Metro Manila and Bangkok (all fetched 2026-09-05); skyscrapercenter.com city/buildings pages for Shenzhen; skyscraperpage.com Shenzhen city page.
