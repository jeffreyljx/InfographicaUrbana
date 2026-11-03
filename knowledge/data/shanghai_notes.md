# Shanghai tall-building tally notes (focus: Pudong New Area)

Date: 2026-09-05. Reference: CTBUH Skyscraper Center city page = 206 completed buildings >= 150 m, 76 >= 200 m.
Tooling: WebSearch/WebFetch only. Sources actually reached: skyscrapercenter.com building/complex pages, en.wikipedia, skyscraperatlas.com, 51cbd.com (Lujiazui ranking), biwuke.com (Chinese enthusiast "200 tallest" list, dated 2022-06-11), pudong.gov.cn PDF, xinhuanet, jingan.gov.cn.
Not reachable: zh.wikipedia (cache-only), baike.baidu (robots), motianguan.com (robots timeout), 51cbd.com/office/lujiazuipaiming (403), skyscraperpage diagrams (JS only), zhihu.

## 1. >= 200 m: all 70 input rows now assigned (file: shanghai_200m_by_district_v2.csv)

Resolutions of the 13 non-verified rows (all from skyscrapercenter.com unless noted):

| Row | Resolution | District |
|---|---|---|
| 66 Tower 1 / 2 (ids 742/743) | = Grand Gateway Towers 1 & 2, 1 Hongqiao Road, 261.8 m, 2005 | Xuhui |
| CITIC Ruibo Tower 1 / 2 (16909/16910) | Yincheng Road East, Lujiazui, 256 m / 238 m, 2017 | Pudong |
| Pacific New World Tower 1 (35857) | = CPIC Xintiandi Commercial Center T1, 111 Ji'an Road, 249.9 m, 2024 | Huangpu |
| AI W Tower (22205) | = MGM Shanghai West Bund, 315 Fenggu Road, 230.9 m, 2020 | Xuhui |
| CITIC Plaza (16911) | 859 Sichuan Road (North), 228 m, 2010 | Hongkou |
| Oasis Skyway Garden Hotel | = Pullman Shanghai Skyway (id 1165), 15 Dapu Road, Luwan (now Huangpu), 226 m, 2007 | Huangpu |
| No. 1 Shanghai (24128) | 156 Yangshupu Road, North Bund, 210.5 m, 2016 | Hongkou |
| Golden Landmark (1565) | = Merry Land Tower, Yincheng Road, Lujiazui, 206 m, 2008 | Pudong |
| BM Plaza Office Tower (8812) | 500 Hengfeng Road (ex-Zhabei), 203 m, 2009 | Jing'an |
| Dong Hai Plaza | SOHO Donghai Plaza, 299 Tongren Road; jingan.gov.cn planning notice | Jing'an |
| Shanghai SK Group Tower (22207) | 330 Jiming Road, Pudong New Area (Qiantan/Houtan), 275 m, 2019 — input said Xuhui, CORRECTED | Pudong |

### Per-district totals, >= 200 m (exact, from the 70-row list)

| District | Count | Notes |
|---|---|---|
| Pudong | **29** | 25 originally verified + Ruibo T1, Ruibo T2, Golden Landmark, SK Group Tower |
| Jing'an | 12 | incl. Dong Hai Plaza, BM Plaza |
| Huangpu | 9 | incl. CPIC Xintiandi T1, Pullman Skyway |
| Xuhui | 6 | incl. 66 Tower 1/2, AI W Tower (SK Tower moved out) |
| Putuo | 6 | |
| Hongkou | 5 | incl. CITIC Plaza, No. 1 Shanghai |
| Changning | 2 | |
| Yangpu | 1 | |
| **Total** | **70** | CTBUH says 76 completed >= 200 m — see gaps |

Pudong >= 200 m by sub-area: Lujiazui 21 (Shanghai Tower, SWFC, Jin Mao, One Lujiazui, IFC N+S, Bank of Shanghai HQ, IOSB, BOCOM, BoC Tower, Zhongrong Jasper, Riviera TwinStar 1+2, World Finance Tower, 21st Century Mansion, Taiping Financial, CMB Mansion, Sen Mao, Ruibo 1+2, Golden Landmark); Zhuyuan/Yanggao Rd 2 (SFEP Tower 1, DoubleTree/Shanghai Summit); Zhangjiang 2 (Science Gate 1+2); Qiantan 2 (Qiantan Center, SK Group Tower); Jinqiao 1 (King Tower); other 1 (Pudong Intl Information Port).

## 2. 150–199.9 m band (file: shanghai_150_200_band.csv)

### Pudong, by confidence

**Verified (CTBUH page/complex page or Wikipedia infobox) — 19:**
World Plaza 199.9 (1997); BEA Finance Tower 198 (2009); SFEP Tower 2 / CFFEX 195 (2020); Shimao Riviera Garden 7 & 8 (192, 2006/2003); Lujiazui Century Tower 1 190 (2014); Huaneng Union Tower 188 (1997); Bao'an Tower 188 (1997); Aurora Plaza 185 (2003); Mirae Asset Tower 180 (2008); Shimao Riviera Garden 1 (173), 2, 3, 5 (169 each), 6 (161); Century Link Tower A & B 168 (2016); Tomson Riviera Garden 1 153 (2005); SFEP Tower 3 / CSDC 152 (2020).

**Verified by news, completed Jan 2026 (likely not yet in CTBUH's "completed" count) — 2:**
BOC Financial Center Lingang twin towers, 195 m each (Xinhua 2026-01-26: "两栋高195米的双子塔楼 … 顺利竣工").

**Probable (Chinese lists 51cbd / biwuke, consistent heights, well-known buildings) — 19:**
Tomson Riviera Garden 2 & 3 (153; CTBUH pages exist, ids 3763/20790); China Insurance Building 196; Taikang Insurance Tower 194; Minsheng Bank Tower 191; FTZ Plaza (Waigaoqiao) 186; SPD Bank/ex-HNA Tower 185; Sheraton Waigaoqiao 181; Citigroup Tower 180; Pudong Shangri-La Grand Tower 180 (CTBUH id 2320 exists, fetch 403); Sino Life Tower 180; Hua Xia Bank Tower 180; Kerry Parkside 179; PetroChina Tower 171; Hui Ya Tower 169; CCB Tower (Lujiazui, 43 fl) 168; Century Financial Tower 168; New Jinqiao Plaza 167; China Resources Times Square 155.

**Possible (conflicting or single-source heights) — 6:**
Tomson Riviera Garden 4 (153); Xinmei Union Square T1 & T2 (180 per biwuke vs 156 per 51cbd); New Shanghai International Tower (168 vs 132); SPD Tower 浦发大厦 (150.0 borderline); Shanghai Futures Building (~158, unverified).

### Pudong >= 150 m totals

| Measure | Value |
|---|---|
| Verified minimum (>=200 list 29 + 19 verified band) | **48** |
| + Lingang BOC twin towers (completed 2026) | 50 |
| Best estimate (29 + 19 + 2 + 19 probable + ~3 of 6 possible) | **~72** |
| Range | **60 – 82** |

Upper end allows for: (a) Pudong buildings that Chinese lists put at >= 200 m but which are absent from the 70-row input (平安金融大厦 210, 中国电信信息大楼 201, 建设银行 219, 农业银行 219, 浦东四季酒店 210 — some may be the same as rows already present under other names, e.g. Four Seasons Pudong / Riviera TwinStar; DoubleTree = 东锦江); (b) unlisted 150-165 m residential/hotel towers in Beicai, Sanlin, Huamu, Jinqiao, Zhangjiang, which the 2022 biwuke list does not cover well below ~165 m.

Cross-check: Lujiazui alone (>=200 m: 21; band verified+probable: ~30) ≈ 50, matching Skyscraper Atlas "nearly one quarter" of 205 (≈ 51). Pudong ≈ 72 of 206 = 35%.

### Other districts, 150–199.9 m (harvested, mostly 'probable' from biwuke 2022 list; incomplete below ~165 m)
Huangpu ~19 (Bund Center 199, Huaihai Intl 193, Xinyuan twin 191 x2, Golden Bell Plaza 188, 88 Dagu Rd 183, Ciro's 181, Bund Finance Center x2 180, Zhongyi 177, Liu Chong Hing 174, Lansheng 173, Guangming 170, CapitaLand Luwan 168, Jin Jiang Tower 153, Haitong 150, World Trade Tower 150…); Jing'an ~5 (Century Commercial Plaza 196, CITIC Pacific Plaza 193, Zhabei Plaza 180, Shanghai Centre 165…); Xuhui ~6 (Shanghai Bay x2 185, IAPM/ICC x2 168/157, Jiahua 162, Shiye 150); Hongkou 3 (W Hotel 180, Pujiang Intl Financial 180, SIIC Center 180); Putuo ~3 (Great Wall 180, China Construction Bldg 168, Global Harbor x2 if counted at 195); Changning 1 (Raffles City Changning 188); Yangpu 1 (Hopson Intl 180); Minhang 1 (CapitaMall Xinzhuang 170); Jiading 1 (Poly Hyatt 196); Fengxian 1 (China Enterprise United 180).
These sum to only ~40 of the ~130 non-200 buildings CTBUH counts (206-76); the remaining ~50-60 (mostly 150-165 m and residential) are not enumerated by any source reached.

## 3. Quantitative per-area statements found (quoted)

- skyscraperatlas.com/city/shanghai/: "As of 2026, Shanghai has 205 skyscrapers (buildings taller than 150 meters)"; "Nearly one quarter of Shanghai's skyscrapers are located here" (Lujiazui); "The number of completed skyscrapers rose from just 2 in 1994...to 135 in 2015...reaching 205 skyscrapers by 2025"; "Among these towers are 9 supertalls (buildings over 300 meters), 3 of which exceed 400 meters".
- skyscrapercenter.com/city/shanghai: Shanghai "#7 Tallest City in the World" (by 150 m+ completed); top-10 list includes Shanghai ITC Tower 2 (369.7 m) and Greenland Bund Centre Tower 1 (300 m) as completed.
- skyscraperatlas.com/city/shanghai/tallest-buildings/: Shanghai ITC Tower 2 370 m, 2025, completed, "the new tallest building in Puxi"; Greenland Bund Center Tower 1 299.9 m, 2025, completed.
- CTBUH per-building "Shanghai rank" (completed only, useful as a height-rank ladder): 66 Tower 1/2 261.8 m = #22; CITIC Ruibo T1 256 m = #26; CPIC Xintiandi T1 249.9 m = #30; Ruibo T2 238 m = #37; AI W Tower 230.9 m = #41; CITIC Plaza 228 m = #45; Pullman Skyway 226 m = #47; No. 1 Shanghai 210.5 m = #59; Golden Landmark 206 m = #66; BM Plaza 203 m = #71; SFEP Tower 2 195 m = #88; Huaneng Union Tower 188 m = #98. (Implies ~76 completed at >= 200 m, ~88 at >= 195 m, ~98 at >= 188 m; so ~108 completed buildings lie between 150 and 188 m.)
- pudong.gov.cn Lujiazui PDF (2022): "截至 2016 年底，陆家嘴金融城有 8 层以上商办楼宇 240 多幢，已建成地上办公面积 1300 多万平方米"; "在建商办楼宇 26 项" — no height-band counts.
- xinminweekly.com.cn/content/11571.html: Shanghai "100米以上的也超过了1000幢"; "高层建筑已经超过了3万幢" — no 150 m count.
- xinhuanet 2026-01-26: Lingang 中银金融中心 "两栋高195米的双子塔楼", 282,500 m2, "顺利竣工".
- biwuke.com/gaoloumi/zixuninfo/61.html (2022-06-11): claims to list Shanghai's 200 tallest (built + planned) — used as the main Chinese enumeration source.
- en.wikipedia List of tallest buildings in Shanghai: main table cutoff 200 m only; "twelve skyscrapers that are under construction … at least 200 m"; no 150 m section.

## 4. Gaps / caveats

1. Input >= 200 m list has 70 rows vs CTBUH 76. Likely missing: Shanghai ITC Tower 2 (370, Xuhui, 2025), Greenland Bund Centre Tower 1 (300, Huangpu, 2025) and possibly Tower 2; Pudong candidates per Chinese lists: Ping An Finance Tower (210), China Telecom Information Tower (201), CCB/ABC Lujiazui towers (219), Four Seasons Pudong (210). Some may already be present under other names. Pudong's exact 29 could therefore be 29–33.
2. Height discrepancies between CTBUH and Chinese real-estate lists are common (Bank of Shanghai HQ 252 vs 230; Taiping 208 vs 216/218; Global Harbor 195 roof vs antenna 248; DoubleTree/东锦江 174 vs >200). Band membership of Global Harbor towers (Putuo) and DoubleTree Pudong should be re-checked against CTBUH.
3. Skyscraper Center pages for the ~19 'probable' Pudong towers were not individually fetched (search engine rarely surfaces them); heights are from 51cbd/biwuke.
4. No source reached enumerates completed 150–165 m buildings city-wide; the 2022 biwuke list is thin below 165 m and stops at ~181 entries.
5. Qiantan: only Qiantan Center (280) and SK Group Tower (275) confirmed >= 150 m; New Bund WTC Phase III towers are 82 m, Qiantan Enterprise World towers ~99 m — Qiantan contributes little to the 150 m band. Zhangjiang: only the Science Gate twins. Lingang: BOC Financial Center twins (195, 2026). Waigaoqiao: FTZ Plaza 186, Sheraton 181 (probable). Jinqiao: King Tower 212, New Jinqiao Plaza 167. Beicai/Sanlin: nothing >= 150 m identified.
