# Asia (ex-mainland China) and Middle East: city goods trade, notes

Companion to `asia_trade.csv` (56 rows). Research date: 16 Oct 2026. All values are in the currency and unit scale as published. Nothing has been converted. A value marked "derived" is my arithmetic on published figures. A value marked "UNVERIFIED" was not seen on a fetched page.

## Method
- I used WebSearch and then WebFetch on official releases where they could be read (SingStat, HK C&SD/TID, Macao GCS, Japan MOF Customs, DOSM, Abu Dhabi Media Office). Where the official tables would not load (KITA K-stat, Korea Customs, Taiwan customs, the HK C&SD PDF annex, Vietnam customs), I used news reports that cite those agencies.
- Goods only (customs or merchandise trade). Services are excluded throughout.
- Year: 2025 calendar year wherever published. India uses fiscal years (Apr–Mar); FY2025-26 is now the latest, and FY2024-25 is shown where found. Dubai has a 2023 fallback.
- The web-search budget ran out near the end. Gaps listed below could be closed with more searching.

## Basis by country (important for comparison)
| Country | Basis | Comparability |
|---|---|---|
| Singapore, Hong Kong, Macau | Whole-economy merchandise trade, including re-exports | Clean city figures. HK and SG exports are dominated by re-exports: HK 5,174.2 of 5,240.3 HK$bn; SG 454.8 of 739.4 S$bn |
| Dubai / Abu Dhabi | Emirate-wide **non-oil** foreign trade: imports + non-oil exports + re-exports. Oil is excluded | Emirate, not city. For Dubai 2025 I found only "external trade surpassed Dhs3 trillion" (in DIEZ's June 2026 release), with no split |
| Japan | **Port or airport of customs clearance** (MOF 全国港別貿易額表, 2025 final 確々報) | NOT firm location. Narita mostly reflects air-cargo semiconductors and pharma for all of Japan. Nagoya reflects Toyota/Aichi autos. Tokyo Port is import-heavy for the metro area |
| South Korea | KITA "지자체 수출입" or regional customs-office releases | Exports are assigned from the export declaration. A Herald (Jan 2026) case shows that the declared **manufacturing place** is used, and where it is missing ("미상") the exporter's **head-office address** is used, so HQ cities are inflated. Customs-office figures (Ulsan, Gumi, Changwon, Pyeongtaek) cover the office's jurisdiction. KITA and customs totals differ (e.g., Ulsan: customs 855.7 vs a KITA headline of ~868 억$) |
| Taiwan | No city or customs-district 2025 values could be read. Science-park administration data used instead | Hsinchu Science Park trade covers park firms and spans Hsinchu City and County (plus satellite parks). The Southern Science Park figure is the value of goods leaving the bonded zone (an export proxy) |
| Vietnam | Customs Dept trade by province, 2025 | Uses the **post-1 July 2025 merged 34-province boundaries**. I inferred this because the full-year values are reported under merged names (Phú Thọ, Ninh Bình, Tây Ninh). HCMC includes former Bình Dương and Bà Rịa–Vũng Tàu; Bắc Ninh includes Bắc Giang; Hải Phòng includes Hải Dương; Đồng Nai includes Bình Phước; Thái Nguyên includes Bắc Kạn. Province attribution is by enterprise location |
| Malaysia | DOSM External Trade Statistics by State 2025 | The DOSM release publishes only **shares**. The RM values here are derived as share × national total, ±~RM0.8bn. The Penang Chief Minister's own figures (exports 573, imports 382, total 955 RM bn) differ from the DOSM-derived values (612 / 355 / 967) |
| India | DGFT/DGCI&S district-of-origin exports | **Exports only.** District imports are not published. Values come from news reports citing DGFT, FIEO and the Commerce Ministry |

## Headline figures (2025 unless noted)
- **Hong Kong**: exports HK$5,240.3bn, imports ~HK$5,686.9bn (derived), total ~HK$10.93tn.
- **Singapore**: total S$1,397.7bn; exports S$739.4bn (domestic 284.7, re-exports 454.8, NODX 182.0); imports S$658.3bn.
- **Japan, top clearance points (億円)**: Narita 413,169 (X 200,970 / M 212,199); Tokyo Port 253,352; Nagoya 240,887 (largest seaport exporter, 163,734); Yokohama 154,136; Kobe 124,143; Kansai Airport 123,490; Osaka 113,527; Hakata 65,244; Chiba 60,533; Mikawa 48,355. Ranks 11–15 are also in the CSV.
- **Dubai**: >AED3tn external trade (2025, floor, no split); AED2tn non-oil (2023). DIEZ free zones AED491bn (2025).
- **Abu Dhabi**: AED415.4bn non-oil trade (imports 170.4, non-oil exports 175.4, re-exports 70.0).
- **Vietnam (USD bn)**: HCMC 192.5 (X 92.68 / M 99.8); Bắc Ninh ~181 (X 93.27 / M 87.8); Hải Phòng 87.2; Phú Thọ 74.6; Hà Nội >69. Exports also given for Đồng Nai 35.0, Thái Nguyên 30.1, Ninh Bình 26.3, Tây Ninh 17.9.
- **Korea (억 USD)**: Ulsan X 855.7 / M 637.7; Asan X 694.9 / M 34.6 (No.1 basic-level local government); Incheon X 601 / M 593; Gumi X 284.6 / M 136.4; Changwon X 226.4 / M 63.3; Pyeongtaek Customs area X 715 / M 756.
- **Malaysia (RM bn, derived)**: Penang X 612 / M 355; Johor X 318 / M 324; Selangor X 273 / M 383; KL X 59 / M 129.
- **India**: Jamnagar FY26 ₹3.22 lakh crore (US$36.6bn) and FY25 ₹3.63 lakh crore; Kancheepuram FY26 US$26.4bn; Ahmedabad FY26 ₹1.05 lakh crore (US$11.9bn). Pune, Mumbai Suburban, Bengaluru Urban, Gautam Buddha Nagar, Surat and Mumbai FY26 values (US$10–16bn) are UNVERIFIED and come from a social-media list.
- **Macau**: total MOP138.71bn (exports 13.92, imports 124.79).
- **Taiwan**: Hsinchu Science Park NT$3.97tn trade (X 1.83tn / M 2.14tn).

## Gaps and caveats
- **Korea**: I did not find 2025 figures for Seoul, Busan, Hwaseong, Icheon, Pyeongtaek City, Cheonan, Yeosu, Gwangyang, Seosan or Pohang. The KITA K-stat "지자체 수출입" tables are dynamic and robots-blocked. Seoul imports would be very large because of head-office registration. Hwaseong and Icheon (SK hynix) are likely in Korea's top tier but are unverified. The Pyeongtaek row is a customs-office jurisdiction, not a city.
- **Dubai**: no official 2025 split into imports, exports and re-exports was found. Dubai Customs/DSC usually announce these figures, but no 2024 or 2025 emirate release surfaced. The UAE national 2025 non-oil trade was ~AED3.8tn (non-oil exports 813.8bn, re-exports 830.2bn, imports >2.1tn) (trade.gov.ae). That is national, so it is not in the CSV.
- **Hong Kong imports**: derived as exports plus the HK$446.6bn deficit. The C&SD annex PDF could not be read.
- **Japan**: port figures should not be read as city output. Nagoya Port, for example, handles exports for all of Aichi (Toyota), and Narita handles high-value air cargo for the whole country.
- **Taiwan**: Keelung, Taipei, Taichung and Kaohsiung customs-district 2025 values were not readable.
- **Thailand, Indonesia, Philippines, Saudi Arabia, Iran**: skipped, as planned, because no cheap city-level data turned up.
- **India**: FY2024-25 district values were found only for Jamnagar and Ahmedabad.

## Sources (one per row in the CSV)
- SingStat: https://www.singstat.gov.sg/find-data/explore-data-themes/trade-investment/merchandise-trade/latest-news-data ; EnterpriseSG review: https://www.enterprisesg.gov.sg/-/media/esg/files/media-centre/media-releases/2026/february/mr00626_review-of-2025-trade-performance.pdf
- HK: https://www.info.gov.hk/gia/general/202601/27/P2026012700489.htm ; https://www.tid.gov.hk/en/our_work/statistics/tradestat/rxdes.html ; https://www.tid.gov.hk/en/our_work/statistics/tradestat/excom.html ; https://news.rthk.hk/rthk/en/component/k2/1841583-20260127.htm
- Macau: https://www.gcs.gov.mo/news/detail/en/N26AdU58hW
- Dubai: https://www.gulftoday.ae/business/2026/06/07/dubai-records-highest-non-oil-trade-performance-in-2025-reaching-dhs491-billion-up-46 ; https://www.thenationalnews.com/business/2024/02/06/dubais-non-oil-foreign-trade-hits-540bn-a-year-before-schedule/
- Abu Dhabi: https://www.mediaoffice.abudhabi/en/economy/abu-dhabi-non-oil-foreign-trade-records-36-percent-growth-in-2025/
- UAE (context only): https://www.trade.gov.ae/web/guest/w/mohammed-bin-rashid-uae-s-non-oil-foreign-trade-surpasses-aed3.8-trillion-for-first-time
- Japan: https://www.customs.go.jp/kobe/boueki/zenkokujuni/banzukehyo2025.pdf ; https://www.customs.go.jp/tokyo/etu/tokuR07soku.pdf
- Korea: kukinews kuk202602030086 (Asan), iusm.co.kr 1058738 (Ulsan), news.ifm.kr 463179 (Incheon), kyongbuk.co.kr 4062241 (Gumi), kukinews kuk202602110347 (Changwon), newspim 20260114000769 (Pyeongtaek Customs), kukinews kuk202601150171 (Gyeongnam), heraldk.com 2026012717375012007 (regional basis)
- Taiwan: https://wantrich.chinatimes.com/news/20260311900707-420101 ; https://n.yam.com/Article/20260519719887
- Vietnam: https://baodautu.vn/dia-phuong-xuat-khau-dan-dau-ca-nuoc-dong-gop-tren-93-ty-usd-d486043.html ; https://thuehaiquan.tapchikinhtetaichinh.vn/tp-ho-chi-minh-dan-dau-ca-nuoc-ve-xuat-nhap-khau-138781.html
- Malaysia: https://www.dosm.gov.my/portal-main/release-content/malaysia-external-trade-statistics-by-state-2026 ; https://storage.dosm.gov.my/trade/trade_2025-12_headline_en.pdf ; https://www.nst.com.my/amp/news/regional/2026/05/1439207/penang-trade-hits-rm955bil-exports-surge-2025
- India: https://indiashippingnews.com/trending-news/ahmedabad-enters-%e2%82%b91-lakh-crore-export-club-ranks-5th-nationwide/ ; https://www.dtnext.in/news/tamilnadu/tn-records-highest-export-growth-in-the-country-in-fy26-kancheepuram-ranked-second-among-districts ; https://deshgujarat.com/2025/08/06/gujarat-retains-no-1-exporter-spot-jamnagar-drives-over-one-third-of-states-shipments/ ; https://www.vibesofindia.com/ahmedabad-top-5-exporting-district-india-fy26-record-exports/ ; (unverified) https://x.com/UpdatesChennai/status/2073995247626113114
