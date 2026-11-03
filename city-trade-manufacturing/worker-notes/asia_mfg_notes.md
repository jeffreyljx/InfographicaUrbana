# East Asia manufacturing cities: notes on method and data

Companion to `asia_mfg.csv` (89 rows). Research date: 2026-10-16.

## Method
- Every number in the CSV was read on a fetched page, and its URL is in `source_url`. Nothing was filled in from memory. A blank cell means the figure was not found or was not published.
- Measures are kept in separate columns:
  - `mfg_value_added` is manufacturing value added proper.
  - `industrial_value_added` is China's 工业增加值 (industrial VA, including mining and utilities).
  - `gross_output_or_shipments` holds a gross measure. `gross_output_measure` names which one (规上工业总产值, 规上工业销售产值, or Japan's 製造品出荷額等).
- Where a Chinese city does not publish an industrial VA amount, its **secondary-industry VA (第二产业增加值, which includes construction)** is given in `notes` as "FALLBACK 二产 VA". It is never put in a VA column.
- Each row has one reference year. The exception is Shanghai: its 2025 VA is paired with 2023 census employment, and `employment_measure` flags the mismatch.
- Limits on access:
  - The web-search budget for this run (shared across agents) ran out partway through. Korea and Taiwan were therefore **not retrieved** (see below).
  - Several official sites refuse automated fetching: sz.gov.cn, cq.gov.cn, gd.gov.cn, tjj.zj.gov.cn, kosis.kr, kostat.go.kr, data.gov.tw and sipa.gov.tw.
  - Command-line downloads through the proxy are blocked for all of these hosts.

## China (mostly 2025 bulletins)
- **Unit.** Most rows are prefecture-level cities, which include rural counties and county-level cities. Shanghai, Beijing, Tianjin and Chongqing are provincial-level municipalities covering their whole territory. Chongqing is about 82,000 km² and largely rural. Shenzhen and Dongguan have no counties.
- **Definitions.**
  - 工业增加值 / 全部工业增加值 covers mining, manufacturing and utilities (electricity, gas and water). It is not manufacturing VA.
  - 规上 means above designated size, i.e. annual main revenue of at least ¥20m.
  - No city in the sample published a **制造业增加值 amount** in its 2025 bulletin, only growth rates. Shenzhen, for example, reported manufacturing growth of +5.9%.
- **Industrial VA amounts found (2025, ¥100m):**

  | City | Industrial VA (¥100m) |
  |---|---|
  | Shenzhen | 13,232.34 |
  | Shanghai | 11,164.97 |
  | Chongqing | 9,049.94 |
  | Ningbo | 7,190 |
  | Beijing | 6,126.5 |
  | Tianjin | 5,718.65 |
  | Chengdu | 5,163.4 |
  | Hangzhou | 4,871 |

- **No industrial VA amount published (2025 bulletins).** Fallback secondary-industry VA, in ¥100m:

  | City | 二产 VA (¥100m) |
  |---|---|
  | Suzhou | 12,844.4 |
  | Wuxi | 7,870.47 |
  | Guangzhou | 7,710.27 |
  | Dongguan | 7,165.44 |
  | Wuhan | 6,589.72 |
  | Foshan | 6,520.37 |
  | Nantong | 5,902.6 |
  | Qingdao | 5,873.83 |
  | Nanjing | 5,873.07 |
  | Zhengzhou | 5,576.8 |
  | Changzhou | 5,154.4 |
  | Yulin | 5,124.88 |
  | Xi'an | 3,970.37 |
  | Quanzhou (2024) | 6,774.89 |

  Where both are published, industrial VA is 75–93% of 二产 VA: Shenzhen 91%, Ningbo 91%, Chongqing 77%, Beijing 85%, Tianjin 93%, Chengdu 75%, Hangzhou 87%. Do not use 二产 as a substitute for manufacturing VA without adjusting for this.
- **Gross output.**
  - Shanghai 规上工业总产值: 40,686.68
  - Suzhou 规上工业总产值: 48,966.4. This is the largest in China, but Suzhou publishes no VA amount.
  - Beijing and Hangzhou publish only 规上工业**销售**产值 (sales output): 27,787.0 and 20,573.
- **Employment.** City bulletins carry only "new urban jobs". The only usable industry employment found comes from the 2023 Fifth Economic Census:
  - **Shanghai, end-2023:** manufacturing legal-entity employees 2.083m; all industry 2.121m. The industrial-enterprise revenue figure in the same census is a 2023 number: ¥48,569.5 × 100m.
  - **Suzhou:** only secondary plus tertiary employees, 8.338m.
  - Census figures cover legal-entity units only and exclude individual businesses.
- **Mining-heavy cities (flag):**
  - Yulin: mining VA grew +9% against manufacturing +3.8%.
  - Ordos: not retrieved.
  - Tangshan (steel-heavy) and Yantai: not retrieved.
  - Hefei: the bulletin is only an embedded PDF and its text was not extracted.
- **Sources.** Many bulletins were read from **tjgb.hongheiku.com (红黑统计公报库)**. This is a third-party mirror that reproduces the official texts, used because the official sites blocked fetching. Shanghai and Suzhou were read on their official statistics-bureau sites. Shenzhen's figures come from a Beijing Daily (京报网) report of the bulletin.
- **Revisions.** Foshan's 2025 二产 VA (6,520) and Quanzhou's 2024 figure (6,775) are below the 2023 values reported in the press (7,514 and 7,164). This most likely reflects revisions after the economic census, so check this before comparing across years.

## Japan
- **Survey.** The source is 経済構造実態調査 (製造業事業所調査), which replaced the 工業統計 survey from 2022. The METI 2025 summary sets out its scope:
  - It covers **all establishments excluding individual proprietorships**. This is not "4+ employees", which applied to the old 工業統計 and to the 2021 Economic Census manufacturing tables.
  - 付加価値額 is replaced by 粗付加価値額 (gross VA) for establishments with 29 or fewer employees.
  - Employees are counted at 1 June of the survey year. Shipments and VA refer to the **previous calendar year**.
- **Municipal VA and employees for CY2022** (2023 survey) come from 大都市比較統計年表 R5:

  | City | VA (¥m) | Employees | VA per worker (¥m) |
  |---|---|---|---|
  | Tokyo 23 wards | 1,432,314 | 149,983 | 9.5 |
  | Nagoya | 1,184,479 | 97,702 | 12.1 |
  | Yokohama | 830,200 | 91,029 | 9.1 |
  | Shizuoka | 860,223 | 50,402 | 17.1 |
  | Hamamatsu | 789,044 | 72,296 | 10.9 |
  | Kawasaki | 611,334 | 50,062 | 12.2 |

  Osaka, Sakai, Kobe, Kyoto, Hiroshima and Kitakyushu have employees and shipments in the CSV but no VA, because their VA table was not in the PDF text. Their rows were matched to cities by table order, so treat that matching as approximate.
- **Shipments for CY2024** (2025 survey, released July 2026) are available for the national top-20 municipalities. Toyota is far ahead at ¥21.21tn, followed by Kurashiki 5.83, Ichihara 5.31, Sakai 4.80, Osaka 4.55, Yokohama 4.26, Kobe 4.20, Kawasaki 4.12, Oita 4.01, Yokkaichi 3.84 and Nagoya 3.44. Tahara is 2.72; Hamamatsu (2.3) and Kariya (2.0) are rounded figures. Municipal VA and employees for 2024 sit in e-Stat table 03008, which could not be read by fetch.
- **Toyota VA and employees.** The only firm figure is for **CY2019** (from 豊田市の工業, 4+ employees): VA ¥3.28tn, 112,478 employees, giving **¥29.2m per worker**. An Aichi PDF for CY2020 gives VA of about ¥2.76tn with about 114,600–114,900 employees. Two inconsistent versions appear on that page, so these are noted only.
- **Prefectures, CY2024 (METI 2025 summary):**

  | Prefecture | VA (¥bn) | Employees | VA per worker (¥m) |
  |---|---|---|---|
  | Aichi | 16,882.6 | 835,442 | 20.2 |
  | Osaka | 6,542.5 | 438,245 | 14.9 |
  | Tokyo | 3,479.2 | 258,621 | 13.5 |
  | Japan | 117,207 | 7.61m | 15.4 |

  Nagoya is a city inside Aichi; there is no Nagoya prefecture.

## South Korea: not retrieved
- The intended source is 광업·제조업조사 (Mining and Manufacturing Survey), which covers establishments with **10 or more employees** and publishes 부가가치, 출하액 and 종사자수 by 시군구 on KOSIS.
- KOSIS and kostat.go.kr both refused automated fetch, and the search budget ran out before an alternative was found. Possible alternatives are provincial statistics portals, city statistical yearbooks and the 국가데이터처 press-release PDFs.
- All 17 target cities are listed in the CSV with blank values.

## Taiwan: largely not retrieved
- The only figure is from the Wikipedia infobox: Hsinchu Science Park had **177,389 workers as of 2024-10**, citing data.gov.tw dataset 41272. It is unverified. The park is not a city: it spans Hsinchu City and Hsinchu County.
- County and city manufacturing VA or production value were not obtained. Likely sources are the DGBAS 2021 Industry, Commerce and Service Census (工業及服務業普查) county tables and the MOEA 工廠校正及營運調查.

## Singapore (city-state)
- **Manufacturing GVA at current prices in 2025: S$137,611.7m.** This is from SingStat table M015731 (SSIC 2020). Earlier years were S$124,455.3m in 2024, S$114,847.6m in 2023 and S$139,656.1m in 2022. GDP in 2025 was S$789,529.2m.
- **Manufacturing employment at December 2025: 498,200.** This is from MOM and comprises 237,500 residents and 260,700 non-residents.
- VA per worker is therefore about **S$276k**. MOM's employment count includes foreign workers, and the December 2025 data were revised for industry reclassification.

## VA per worker
Comparisons across countries need PPP or exchange-rate conversion, which is the lead's task.

| Place | Year | VA per worker | Basis |
|---|---|---|---|
| Toyota | 2019 | ¥29.2m | Highest found in Japan |
| Aichi | 2024 | ¥20.2m | |
| Shizuoka-shi | 2022 | ¥17.1m | |
| Japan average | 2024 | ¥15.4m | |
| Nagoya | 2022 | ¥12.1m | |
| Kawasaki | 2022 | ¥12.2m | |
| Hamamatsu | 2022 | ¥10.9m | |
| Tokyo 23 wards | 2022 | ¥9.5m | |
| Yokohama | 2022 | ¥9.1m | |
| Singapore | 2025 | S$276k | |
| Shanghai | 2025 VA / 2023 employment | ≈ ¥536k per manufacturing worker | Industrial VA divided by manufacturing employment: mixed years and a mixed measure. ≈ ¥526k per industrial worker. |

Shipments overstate process-industry cities compared with VA. In 2022 Kawasaki's VA was only about 15% of its shipments, against about 33% for Nagoya and 40% for the Tokyo wards. Kurashiki, Ichihara, Sakai and Yokkaichi rank high on shipments for the same reason.

## Key source URLs
- **Shanghai:** https://tjj.sh.gov.cn/tjgb/20260330/e0772941e8e041eaaad2df850b44ef98.html (bulletin) and https://tjj.sh.gov.cn/cmsres/42/4245ede056ad44d29f7c7410088be277/1fe46fa421193dfbc009dd59490aefdc.pdf (census, second industry).
- **Shenzhen:** https://news.bjd.com.cn/2026/05/26/11766177.shtml
- **Suzhou:** https://tjj.suzhou.gov.cn/sztjj/tjgb/202604/3dc4b574cabd4e86b36ec5d3280e927c.shtml
- **Other Chinese cities:** the tjgb.hongheiku.com pages listed per row in the CSV.
- **Japan:**
  - https://www.city.sapporo.jp/toukei/hikaku/documents/05r5.pdf (大都市比較統計年表 R5)
  - https://www.city.ota.gunma.jp/uploaded/attachment/42600.pdf (2024 shipment ranking)
  - https://www.meti.go.jp/statistics/tyo/kkj/pdf/seizo_gaikyo2025.pdf (METI summary)
  - Toyota open data on data.bodik.jp, as listed in the CSV.
- **Singapore:** https://tablebuilder.singstat.gov.sg/api/table/tabledata/M015731 and https://stats.mom.gov.sg/Pages/Employment-Summary-Table.aspx
