# China city goods trade, 2025: method notes and caveats

Companion to `china_trade.csv` in the same folder. All values are in RMB, in 亿元 (100 million yuan), exactly as published. Nothing has been converted to USD. Researched 2026-10-16.

## Coverage
- **2025 full-year figures for every city.** No 2024 fallback was needed.
- **32 prefecture- or provincial-level cities**, plus Kunshan and Yiwu (county-level, shown separately) and the national total.
- **Exports/imports split missing for two cities:**
  - Chengdu: only the total (8,502.3) was published on the pages I could fetch.
  - Zhuhai: the total is **derived**, not published (see below).
- **Kunshan:** imports were not published. Total minus exports gives 2,878.6 (derived).
- **Search budget ran out.** The shared web-search budget (200 per turn) was used up before I could check several cities that may fall in ranks 27–35: Changzhou, Shaoxing, Wenzhou, Jinan (+24.7% in 2025, level not captured), Taizhou (Zhejiang), Zhoushan, Weifang and Weihai. They are **not** in the CSV.
- **Ranks 1–26 are probably complete.** Huizhou's government says Huizhou ranked **25th** on the GACC 2025 city list. So the list has 24 cities above Huizhou. My compiled list has 25 cities above it, so no missing city should outrank Huizhou. At least one of my rows must be lower in GACC's own list, probably because bulletin and GACC figures differ slightly.

## Sources and method
Order of preference:
1. Municipal statistical bulletins (统计公报), which carry customs data.
2. Local customs releases, via city government sites or major media (Yicai, Xinhua and others).

When an official bulletin page blocked fetching, I used a verbatim repost. Those are the hongheiku.com bulletin repository, Sohu or fangchan.com reposts, and the bulletin PDFs hosted on hongheiku. I cross-checked them against media figures where I could. Every row lists its URL(s). I recorded only figures I saw on a fetched page.

Minor inconsistencies:
- **Hangzhou:** the bulletin says 9,072. The January customs release said 9,069.5. The CSV uses the bulletin figure.
- **Jinhua:** the bulletin text gives exports of 9,212.9, but its Table 3 prints 9,121.9. I used 9,212.9, which equals total minus imports.
- **Shenzhen and Shanghai:** published only to 0.01 万亿 (for example 4.55/2.74/1.81 万亿), so these rows are rounded.

## What is measured
- **Location of the trading firm, not the port.** City figures are customs statistics assigned to where the importer or exporter is registered: 收发货人所在地, formerly 经营单位所在地. They are not assigned to the port of clearance.
  - **Evidence I saw:** Beijing customs data is defined as "北京地区（含中央在京单位）", meaning the Beijing area including central units based in Beijing (sina.cn 2025-08-22; cs.com.cn 2024-01-18).
  - Commercial customs-data pages publish a separate city series called "商品收发货人所在地进出口" (huaon.com, Foshan). It is distinct from the "境内目的地/货源地" series (domestic destination or source of the goods).
  - Huaon's Foshan "收发货人所在地" figure for Jan–Nov 2025 is US$60.82bn, which is consistent with the Foshan bulletin's 4,813.6亿元 for the full year.
  - **Caveat:** I did not find an official GACC methodology note on a fetched page that states this definition outright.
- **Port figures are a different thing.** For example, Gongbei Customs reports a customs-district total covering Zhuhai and Zhongshan together. And 3,258 亿元 of goods crossed via the Hong Kong–Zhuhai–Macao Bridge port in 2025. Neither is a city figure.
- **Quanzhou** is absent from the GACC 2025 city list, according to NBD/STCN. Its figure comes from local customs and its bulletin.

## Beijing headquarters effect (important)
- **Beijing's figures include central SOEs headquartered there.** They cover "中央在京单位" (central units in Beijing). These include the HQ-registered trading arms of oil, gas and commodity SOEs (Sinopec/Unipec, PetroChina, CNOOC, Sinochem and others), which book large crude oil, gas and commodity imports.
- **2025: imports are about 80% of Beijing's trade.** Imports 25,642.9 vs exports 6,286.8.
- **2023 (latest product breakdown found):**
  - Beijing's top 5 imports were crude oil, unwrought gold, natural gas, agricultural products and cars. Together they were **72.6% of Beijing's imports** (cs.com.cn 2024-01-18; bjnews 2024-02-02).
  - State-owned enterprises handled 2.68万亿元, which is **73.5% of Beijing's total trade** (bjnews).
- **No 2025 energy-only share found.** For scale only: China's 2025 crude imports were worth 21,217亿元 (NBS), against Beijing's total imports of 25,642.9亿元. This is **not** a share; some crude is imported by firms registered elsewhere.
- **2025 regional figure:** crude oil plus mechanical and electrical products were 54.1% of Beijing-Tianjin-Hebei imports (stdaily 2026-02-26). The article gives no Beijing-only split.
- **Beijing's −11.5% (imports −14.6%) probably reflects lower commodity prices.** Nationally, crude import value fell 8.3% while volume rose 4.4% (NBS). This explanation is my inference; no source states it.
- **Suggestion for the lead:** report Beijing with a footnote, or show it on an exports-only basis. Beijing ranks about 3rd on total trade but far lower on exports, at 6,287 (below Hangzhou, Wuxi and Chongqing).

## Unit definitions (what a "city" is)
- **Provincial-level municipalities (直辖市): Shanghai, Beijing, Tianjin, Chongqing.** These include rural districts. Chongqing in particular covers about 82,000 km² with many rural counties.
- **Sub-provincial cities (副省级):** Shenzhen, Guangzhou, Ningbo, Xiamen, Qingdao, Hangzhou, Chengdu, Nanjing, Wuhan, Xi'an, Dalian and Shenyang. These are prefecture-level units that include outlying districts or counties. Shenzhen has no counties.
- **Prefecture-level cities (地级市), incl. counties or county-level cities:** Suzhou, Jinhua, Wuxi, Zhengzhou, Yantai, Jiaxing, Foshan, Hefei, Nantong, Huizhou, Zhuhai, Changsha, Fuzhou and Quanzhou.
  - Suzhou contains Kunshan, Changshu, Zhangjiagang and Taicang.
  - Jinhua contains Yiwu.
- **Dongguan and Zhongshan:** prefecture-level cities with no county tier; towns report directly to the city.
- **Kunshan (in Suzhou) and Yiwu (in Jinhua):** county-level cities (县级市).
  - **They are already included in their parent city. Do not add them.**
  - Yiwu is about 80% of Jinhua's trade.
  - Kunshan is about 29% of Suzhou's trade. 60% of Kunshan's trade is processing trade.

## 2025 national and provincial context
- **China (NBS communiqué / GACC):** total 454,685, exports 269,890, imports 184,795. That is +3.8% / +6.1% / +0.5%. GACC's 14 Jan 2026 release gave 45.47 / 26.99 / 18.48 万亿元.
- **Guangdong:** 9.49万亿 (+4.4%). Exports 6.03万亿, imports 3.46万亿. The 9 Greater Bay Area mainland cities together: 9.15万亿, which is 20.1% of China's total.
- **Zhejiang:** 5.55万亿 (+5.4%). Exports 4.19万亿 (first year above 4万亿), imports 1.36万亿.
- **Jiangsu:** about 6万亿 (Nanjing Customs, via Yicai).
- **Anhui:** 10,135.6 (+17.3%).
- **Sichuan:** 10,318.1. Exports 6,086.5, imports 4,231.6. Chengdu is more than 82% of Sichuan's total.
- **Concentration:** Shenzhen and Shanghai are each about 10% of China's total. The top 4 cities together (Shenzhen, Shanghai, Beijing, Suzhou) are about 33%.

## 2025 growth notes
- **Rank changes:**
  - Shenzhen stayed No. 1 (4.55万亿, +1.4%), but its exports fell 2.5%. Shanghai was close behind at 4.51万亿 (+5.6%).
  - Dongguan rose back into the top 5 (+13.8%).
  - Jinhua entered the 1万亿 club (+19.5%), driven by Yiwu (+25.1%, mostly market-procurement exports).
- **Fast growers:**

  | City | Growth |
  |---|---|
  | Yiwu | +25.1% |
  | Xi'an | +21.1% |
  | Hefei | +20.2% |
  | Jinhua | +19.5% |
  | Zhengzhou | +16.8% |
  | Dongguan | +13.8% |
  | Yantai | +13.7% |
  | Wuhan | +12.7% |
  | Nantong | +12.3% |
  | Chongqing | +12.0% |
  | Guangzhou | +10.4% |

  Jinan was +24.7% (level not captured) and Wuhu +32.4% (NBD).
- **Decliners:**

  | City | Change |
  |---|---|
  | Fuzhou | −24.0% (exports −32%) |
  | Quanzhou | −12.9% |
  | Beijing | −11.5% |
  | Shenyang | −7.6% |
  | Foshan | −3.7% |
  | Nanjing | −1.4% |
  | Dalian | −0.3% |

- **Surprise:** Foshan, at 4,813.6, is much smaller than its manufacturing reputation suggests. Yantai, at 5,379.3, is level with Nanjing.

## Key sources
- **National:**
  - NBS 2025 communiqué: https://www.stats.gov.cn/sj/zxfbhjd/202602/t20260228_1962662.html
  - GACC release via Yicai: https://www.yicai.com/news/103003349.html
- **Rankings and context:**
  - Yicai top-10: https://www.yicai.com/news/103019783.html
  - NBD/STCN 50-city analysis: https://www.stcn.com/article/detail/3611143.html
  - 36Kr: https://www.36kr.com/p/3650250401243268
  - Huizhou rank 25: https://news.qq.com/rain/a/20260302A05FPI00?app=news&id=20260302A05FPI00&path=a&redirect_pc=1
- **Beijing definitions and HQ effect:**
  - https://m.jiemian.com/article/14159781.html
  - https://finance.sina.cn/2025-08-22/detail-infmutkt4025418.d.html?vt=4
  - https://www.cs.com.cn/xwzx/hg/202401/t20240118_6385914.html
  - https://m.bjnews.com.cn/detail/170683887719782.html
  - https://www.stdaily.com/web/gdxw/2026-02/26/content_477022.html
- **Measurement series label:** https://www.huaon.com/channel/tradedata/1136647.html
- **Provincial:**
  - Guangdong: https://paper.cnstock.com/html/2026-01/20/content_2172046.htm
  - Zhejiang: https://tidenews.com.cn/news.html?id=3350670
  - Anhui: https://www.cnr.cn/ah/gstjah/20260118/t20260118_527497190.shtml
  - Greater Bay Area: https://www.peoplecen.com/html/2026/difang_0120/25293.html
- **City-level:** see the `source_url` column of `china_trade.csv`.
