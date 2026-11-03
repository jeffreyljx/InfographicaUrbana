# Guangzhou 150 m+ buildings by district — refresh notes (2026-09-05)

Input: `guangzhou_150m_by_district.csv` (160 rows = en.wikipedia list as of ~2021).
Output: `guangzhou_150m_by_district_v2.csv` (167 rows: 160 original + 7 additions; every row has a `district`, `confidence`, `source`).

## 1. Per-district totals (v2 CSV, completed buildings, architectural height)

| District   | ≥150 m verified | ≥150 m probable | ≥150 m unverified | ≥150 m TOTAL | ≥200 m | of which added 2026 |
|------------|----:|----:|----:|----:|----:|----:|
| **Tianhe** | 70 | 5 | 0 | **75** | 30 | 0 |
| Haizhu     | 34 | 13 | 0 | 47 | 15 | 5 (1 ≥200 m) |
| Yuexiu     | 15 | 6 | 0 | 21 | 4 | 0 |
| Panyu      | 5 | 2 | 0 | 7 | 5 | 0 |
| Liwan      | 4 | 1 | 0 | 5 | 0 | 0 |
| Zengcheng  | 3 | 0 | 0 | 3 | 3 | 0 |
| Baiyun     | 2 | 0 | 0 | 2 | 0 | 0 |
| Nansha     | 2 | 0 | 0 | 2 | 1 | 2 (1 ≥200 m) |
| Huangpu    | 1 | 0 | 0 | 1 | 1 | 0 |
| Huadu / Conghua | 0 | 0 | 0 | 0 | 0 | 0 |
| UNASSIGNED | 0 | 0 | 4 | 4 | 2 | 0 |
| **Total**  | 136 | 27 | 4 | **167** | 61 | 7 |

**Tianhe ≥150 m: 75 (range 70–79).** Floor = 70 sourced-address rows; +5 probable (Yuehai Finance Center T1, GZ Electric Power Bldg, Yudean Plaza A, New World Times Center Ph2, R&F Yingtong); ceiling adds the 4 unresolved rows (Pearl River One 241 m, Deshun 200 m, Pol Tower V 180 m, Lifeng Center 169.7 m) if any turn out to be in Tianhe. Tianhe ≥200 m: 30 (29 verified + Yuehai probable).

Context: CTBUH (skyscrapercenter.com/city/guangzhou) currently lists Guangzhou #5 worldwide / #3 in Asia by number of 150 m+ completed buildings (~212 per the brief). This file has 167 rows, so ~45 completed 150 m+ buildings (mostly 2021–2025 completions and CTBUH-only entries) remain undocumented — see §4.

## 2. Key reassignments / corrections to the input

- **Guangdong Business Center 375.5 m (2025): Baiyun → Haizhu (Pazhou West).** SkyDB coordinates 23.1033 N, 113.3377 E (https://www.skydb.net/building/574538451/guangdong-business-center/); 快办公 article: "项目雄踞海珠区琶洲大道南侧 … 376米 … 地上61层" (https://gz.kbgok.com/news/13352).
- Huijin Center 1 = CTBUH "Shimao Canton Financial Center", 320.6 m, 650 Huangpu Road, Tianhe District (Financial City) — https://www.skyscrapercenter.com/building/shimao-canton-financial-center/23582. Huijin Center 2 (220 m) is in the same complex (https://www.skyscrapercenter.com/complex/2341). Both → Tianhe verified.
- Junchao Plaza 320 m (2025) → Tianhe: address Huangpu Middle Avenue (https://www.skyscrapercenter.com/building/junchao-plaza/31177).
- Star River Center → Haizhu (Pazhou West 星河湾中心); CTBUH gives 259.5 m (vs 280 m on Wikipedia) — https://www.skyscrapercenter.com/building/star-river-center/35384.
- Cadre City Plaza West/East = Kaidar International TOD Centre, Zengcheng (Xintang) — https://www.skyscrapercenter.com/building/cadre-city-plaza-west-tower/24427.
- New World Canton Center C2 = "New World Zengcheng Mixed-Use Development C2" → Zengcheng — https://www.skyscrapercenter.com/building/new-world-zengcheng-mixed-use-development-c2-tower/33591.
- Grand City Main Tower 266 m → Panyu (Hanxi East Avenue) — https://www.skyscrapercenter.com/building/grand-city-main-tower/39125.
- Guangzhou International Commercial Center → Tianhe (Tianhe Rd North & Linhe Middle Rd; CTBUH height 229.6 m) — https://www.skyscrapercenter.com/building/guangzhou-international-commercial-center/38789.
- Dapeng International Plaza = 正佳环市中心, Huanshi Road East, Yuexiu (213 m roof / 269.4 m spire) — https://en.wikipedia.org/wiki/Dapeng_International_Plaza.
- The Riverside 1–4 → **Liwan** (Huangsha Avenue), not Haizhu — https://www.skyscrapercenter.com/guangzhou/the-riverside-1/13578.
- Jade Pavilion 4–9 = Haizhu Peninsula Garden (海珠半岛花园) → Haizhu — https://www.skyscrapercenter.com/complex/421.
- Regal Harbour 1–3 (555 Binjiang Rd East), Post Chateau A/B (中信君庭, Binjiang Rd East), Fortune Way (199 Tongfu West Rd), Vertical City (保华广场, 362 Jiangnan Ave), Bravo Park Place (Xingang East Rd) → Haizhu (CTBUH pages, see CSV).
- Victory Garden B/C ("Caesar's Palace" = 凯旋会, 明月一路 11–23号), Top View 1/2 (Jinsui Rd), The Cosmos 1/2 (誉峰, 711 Jinsui Rd), King Peak Garden B/C/D/E (Xingguo Rd), CC Tower (1 Huaxia Rd), R&F Yingxin (28 Huaxia Rd), Jiayu Bldg (421 Zhujiang East Rd), Banghua Global Plaza (1 Jinsui Rd), Kingold Century (Jinsui Rd), R&F IBC Ph2 (Xiancun Rd), Guangzhou International Trade Center (1 Linhe Rd West), Center Plaza (161 Linhe Rd West), Renfeng Tower (490 Tianhe Rd), Bercy Plaza I/II (Tiyu Rd West) → Tianhe (CTBUH / SkyscraperPage pages, see CSV).
- Pearl River International Bldg (Yuehua Rd), RenFun (Dongfeng Middle Rd), Riverside Hotel (298 Yanjiang Rd Central), Shun Tak Business Centre (246 Zhongshan 4 Rd), JLB Tower (健力宝大厦, 410 Dongfeng Rd Central), Dongzhao Bldg (东照大厦, Dongfeng Rd Central) → Yuexiu.
- China Southern Airlines Tower → Baiyun (68 Qixin Rd, Baiyun New Town) — https://www.skyscrapercenter.com/building/china-southern-airlines-tower/35621.
- CCCC South Headquarters = Window of Guangzhou Zone A (广州之窗) → Haizhu, marked probable (CTBUH address only "Zhenxing Street").

## 3. Additions (post-2020 completions ≥150 m not in the 2021 list) — 7 rows, note = "added 2026 refresh"

| Building | Height | Year | District | Confidence | Source |
|---|---|---|---|---|---|
| Huanju Tower / JOYY HQ 欢聚大厦 | 222 m | 2023 (topped out; year approx.) | Haizhu (Pazhou W) | verified | haizhu.gov.cn post_9843394; kbgok.com/news/12759 |
| Nansha Yuexiu IFC Tower A 南沙越秀国际金融中心A塔 | 220 m | 2023 (in use Oct 2023) | Nansha (Mingzhu Bay) | verified | gzns.gov.cn post_9256190 ("总高220米，共设置43层") |
| Window of Guangzhou Zone B | 196 m | 2022 | Haizhu | probable | skyscrapercenter.com/complex/1317 |
| Oppein International Plaza 欧派国际广场 | 180 m | ~2020 | Haizhu (Pazhou W) | probable | kbgok.com/news/12759 |
| Vipshop HQ South Tower 唯品会总部 | 173 m | ~2021 | Haizhu (Pazhou W) | probable | haizhu.gov.cn post_9843394 ("南塔173米") |
| 37 Interactive Global HQ 三七互娱 | 172 m | 2024 | Haizhu (Pazhou W) | verified | news.qq.com/rain/a/20241212A08A9J00 |
| Nansha Yuexiu IFC Tower B | 150 m | 2023 | Nansha | verified | gzns.gov.cn post_9256190 ("总高150米，共设置31层") |

Checked and NOT added: Guangjian Financial Center 广建金融中心 333 m (No. 8 Zhongshan Ave East, **Huangpu**) is *under construction*, expected 2027 (https://www.skyscrapercenter.com/building/guangjian-financial-center/41161) even though it appears in the Skyscraper Center city top-10. Marubi HQ 138 m and Window of Guangzhou Zone C 146 m are below 150 m.

## 4. Quantitative statements found (quoted)

- en.wikipedia "List of tallest buildings in Guangzhou" (fetched 2026-09-05): completed table has **156 rows**, columns Rank / Name / Height / Floors / Year / Notes — **no District column**. Lead text is inconsistent: "204 buildings" in one place, "208" (as of 2025) taller than 150 m in another. https://en.wikipedia.org/wiki/List_of_tallest_buildings_in_Guangzhou
- skyscrapercenter.com/city/guangzhou: Guangzhou "ranks #5 globally and #3 in Asia by number of 150m+ completed buildings" (no numeric count exposed on the page). Top-10 there: CTF 530, IFC 438.6, CITIC 390.2, Guangdong Business Center 375.5, Pinnacle 350.3, Guangjian FC 333 (UC), Knowledge Tower 330, Shimao Canton FC 320.6, Junchao Plaza 320, Intl Cultural Center 320.
- SkyscraperPage Guangzhou: "2,752 total buildings … 2,387 highrise buildings" (all heights; list not fetchable). https://skyscraperpage.com/cities/?cityID=25
- Guangzhou International Financial City (Tianhe), 21jingji 2025-01-13: "25座甲级写字楼在建、交付 … 18 towers in the starting zone, 11 already in use, 15 towers in the financial square (金融方城) area"; 广州国际金融交易广场 main structure topped out Dec 2024. No heights given. https://www.21jingji.com/article/20250113/herald/3eb18b5cae37cef9687a90dea41e10fd.html
- Tianhe govt page on Financial City names 绿地中心, 保利金融大都汇, 汇金金融中心 as in use (no heights). https://www.thnet.gov.cn/zjth/tzth/zlpt/content/post_7804263.html
- Pazhou West (Haizhu), Tencent News 2024-12-12: "at least 21 major towers are operational" in western Pazhou, six more HQs expected by 2025. https://news.qq.com/rain/a/20241212A08A9J00
- Haizhu govt 2024: Guangzhou International Cultural Center "320米 … 地上54层", topped out; 广东省港航集团总部 topped out 31 May 2024 (height not given). https://www.haizhu.gov.cn/hzdt/ztlm/tzhz/yshj/yshl/content/post_9843394.html
- No source found giving an explicit per-district count of 150 m+ buildings for Tianhe or other districts; the table above is the only such tally.

## 5. Remaining gaps

1. **4 unresolved rows** (no CTBUH/SkyDB/SkyscraperPage page found; search budget exhausted): Pearl River One Office Tower 241 m (2022), Deshun Building 200 m (2018), Pol Tower V 180 m (2011), Lifeng Center 169.7 m (2016). Two of these are ≥200 m and could shift Tianhe/Haizhu ≥200 m counts.
2. **Probable-only identities**: Coral Garden 1–4 and Le Palais (assumed Haizhu Binjiang East cluster, no page found); CCB Tower 1996, Crowne Plaza Harbourview 2008 (assumed Yuexiu); New China Mansion (Liwan, known location, no page); Yuehai Finance Center T1 283.9 m (assumed Tianhe — unresolved which project this is); Country Garden Center T1 (Panyu Wanbo, skyscrapercity thread returned 402).
3. **Gap to CTBUH's ~212**: ~45 completed 150 m+ buildings are still missing from this file. Most likely clusters: Guangzhou International Financial City starting zone (Tianhe; 11 towers in use incl. 绿地中心, 保利金融大都汇, 中国人寿 tower — heights not obtained), Pazhou West remaining HQs (Haizhu: 广东省港航总部, TCL, 东升, 广州国际航运大厦, 赫基, 树根, 小米 etc. — heights not obtained, several may be <150 m), Baiyun New Town / 广州设计之都 (Baiyun; gz.gov.cn page blocked by robots), Wanbo/Hanxi (Panyu; chinadaily page timed out), Huangpu Science City, Nansha Mingzhu Bay (only Yuexiu IFC captured), plus 2020–2025 residential towers ≥150 m that CTBUH counts but Wikipedia omits.
4. Height discrepancies to reconcile: Star River Center 280 vs 259.5 (CTBUH); GZ ICC 219.5 vs 229.6; New World Times Center Ph2 249 vs 213.1 (SkyDB); Shun Tak 150.6 vs 165.8; Pearl River Intl Bldg year 2007 vs 2010.
5. Tools not usable this session: zh.wikipedia (has a district-tagged 广州市摩天大楼列表), zhihu (2020 "250米以上摩天大楼盘点"), sohu/baidu-baike (robots), Skyscraper Center explore-data. zh.wikipedia's list would be the fastest way to close gap #3 if it becomes fetchable.
