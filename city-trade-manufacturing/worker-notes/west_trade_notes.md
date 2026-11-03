# Goods trade by city/metro: Americas, Europe, Turkey (notes)

Companion to `west_trade.csv` (same folder). Research date: 2026-10-16. Values are in the currency and scale **as published**. Nothing is converted. Every number in the CSV was seen on a fetched page, and its URL is given. Sums I computed myself (Mexico annual totals, French and UK "total" columns) are labelled as such in the notes column.

## Method
- I used WebSearch to find official releases, then WebFetch to read single pages and PDFs. Command-line downloads (census.gov, gov.uk assets, ISTAT, Data México API) were refused by the egress proxy. WebFetch cannot read binary ODS/XLSX, so the HMRC and ISTAT spreadsheets could not be parsed.
- **The shared web-search budget ran out partway through the run.** After that I could only fetch URLs already seen or official URLs I knew. Spain, Netherlands, Belgium, Switzerland, Ireland, Canada CMAs, Italian provinces, Bremen and full-year Brazilian municipalities are therefore **NOT OBTAINED**. They appear as blank rows flagged "NOT OBTAINED" so the gaps are visible.
- Rows marked `DUPLICATE cross-check - do not sum` repeat a figure from a second source.

## Basis by country (the main comparability issue)
| Country | Geography | Year | Basis | Imports? |
|---|---|---|---|---|
| United States | MSA (30 largest) | 2025 | Census OM-ZIP series: exports go to the ZIP of the **US Principal Party in Interest (exporter of record)**, not the producer (ITA methodology page). Release dated 12 Mar 2026, USD million, NSA. | **No.** ITA confirms metro imports are not published because no ZIP is collected for importers. Port data are port-of-entry only. |
| Mexico | **State**, not city | 2025 = sum of four preliminary quarterly ETEF releases | INEGI assigns exports to the state of the **producing establishment** (linked to the RENEM register). Covers agriculture, mining (incl. crude oil) and manufacturing. Commerce/services and unlinked records are excluded. | No state imports. |
| Brazil | Municipality | 2025 (partial) | Comex Stat assigns trade to the **municipality of the exporting/importing firm's establishment**. Values are rounded, from secondary reports citing Fapespa/SECEX. | Import ranking for Jan–Aug 2025 only. |
| Canada | — | — | Statistics Canada publishes merchandise trade (customs basis) by **province only** (table 12-10-0175-01). No CMA series was found. | — |
| Germany | City-state (Land) | 2025 | Hamburg exports use **Spezialhandel** (goods produced or substantially processed in Hamburg). Imports use **Generalhandel** and include goods entering storage, so the port inflates them. | Yes |
| France | Region / département | Region: calendar 2025. Départements: 12 months Q3 2025–Q2 2026 | Douane data, exports FOB and imports CIF, excluding military goods. Allocated "in principle" to the **département of production (exports) or consumption (imports)**, but sometimes to the département of departure/arrival (e.g. oil). Val-d'Oise and Seine-et-Marne contain Roissy-CDG. | Yes |
| UK | ITL1 (London) | 2023 (ONS) | ONS subnational trade in goods: HMRC data allocated to local units via the IDBR. Precious metals go to "unknown", which matters for London. HMRC Regional Trade Statistics for 2025 exist but London's value is only in the ODS/interactive tables. | Yes (2023) |
| Italy | Province | 2025 | ISTAT assigns exports to the province where goods were **produced or processed** (Intrastat). Extra-EU exports are estimated from ASIA local units. Milan's value was not obtained. The release says Milan was among the five largest negative contributors in 2025. | — |
| Turkey | Province (il) | 2025 | **Two different bases.** (a) **TİM** assigns exports to the exporter's **legal headquarters (kanuni merkez)**: Istanbul gets 40% of the national total. (b) The **Ministry of Trade** uses the **activity province (faaliyet ili)**: Istanbul's share falls to 21% and Kocaeli, Tekirdağ and Mersin rise. A 2024 TÜİK provincial series (Istanbul 125.9 bn USD) is higher again. | Provincial imports not obtained |

## Headline figures
- **US 2025 (USD mn):** Houston 177,336; New York 161,437; Corpus Christi 68,914; Los Angeles 62,566; Chicago 56,424; Dallas 53,557; Miami 52,119; El Paso 49,059; Cincinnati 45,935; New Orleans 44,373; Seattle 42,096; Detroit 34,621; Boston 30,541; Beaumont 29,192; San Jose 28,560; San Francisco 27,853; Portland 27,704; Lake Charles 25,166. New York rose 62% from 2024 (99,414). The cause was not verified, so treat this figure with care.
- **Laredo port of entry 2025:** about 354 bn USD total trade (imports plus exports). This is port-of-entry basis, not trader location.
- **Mexico 2025 (USD mn, state):** Chihuahua 109,628; Coahuila 67,484; Nuevo León 58,672; Baja California 56,475; Jalisco 52,728; Tamaulipas 36,803; Ciudad de México 3,764, which is low because establishments are counted where they produce. Ciudad Juárez municipal "~67,833 USD mn" is an unsourced estimate (Expansión) and marked unverified.
- **Brazil 2025 (USD bn, rounded):** Canaã dos Carajás 6.6; Parauapebas 5.3; São José dos Campos 4.1; Barcarena 3.4; Marabá 3.2. Imports Jan–Aug 2025: Manaus ~10.93 bn, Itajaí ~10.78, São Paulo ~6.65, Petrópolis ~6.47, Rio ~5.24. The articles print "R$", but Comex Stat publishes US$, so the currency is ambiguous.
- **Île-de-France 2025:** exports 146.68 bn EUR, imports 184.42 bn EUR. **Paris (75)**, 12 months to Q2 2026: exports 24.2 bn EUR, imports 36.7 bn EUR.
- **Hamburg 2025:** exports 56.76 bn EUR, imports 76.60 bn EUR. Bavaria (context only): exports 226.95 bn EUR.
- **London 2023 (ONS):** goods exports 41.8 bn GBP, imports 89.8 bn GBP. England 2025 (HMRC): exports 262.2 bn GBP, imports 446.1 bn GBP.
- **Turkey 2025 exports (USD thousand):**

  | Province | TİM (legal HQ) | Ministry of Trade (activity province) |
  |---|---|---|
  | Istanbul | 95,197,035 | 57,758,289 |
  | Kocaeli | 22,928,716 | 35,086,932 |
  | Bursa | 17,862,024 | 19,985,826 |
  | Ankara | 17,485,657 | 13,084,738 |
  | İzmir | 13,597,550 | 23,614,855 |
  | Gaziantep | 10,145,026 | 9,526,798 |

## Caveats
1. None of these series measure production in a city. The US uses the exporter of record, Turkey (TİM) uses headquarters, and Brazil uses the firm's establishment. All three over-weight headquarters cities. Mexico and Italy use the production location. France uses production/consumption with port and airport exceptions.
2. Hamburg's imports and the Val-d'Oise/Seine-et-Marne figures reflect gateway effects from the port and from CDG airport.
3. The Mexican annual totals are my sums of preliminary quarterly figures. They may differ slightly from INEGI's revised annual series.
4. US metro imports do not exist as an official series. Do not pair metro exports with port-district imports.

## Sources (main)
- Census metro exports Q4 2025: https://www.census.gov/foreign-trade/statistics/state/metroq42025.pdf
- ITA methodology: https://www.trade.gov/metropolitan-export-series-methodology
- Greater Houston Partnership Glance May 2026: https://wpb.houston.org/app/uploads/2026/05/Glance-May-2026-Final.pdf
- INEGI ETEF bulletins: etef2025_06, etef2025_09, etef2025_12 (https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/exporta_ef/) and https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/exporta_ef/etef2026_03.pdf
- Statistikamt Nord Hamburg 2025: https://www.statistik-nord.de/fileadmin/Dokumente/SI26_43.pdf
- Bayern: https://www.statistik.bayern.de/mam/produkte/veroffentlichungen/statistische_berichte/g3000c_202512.pdf
- Douane regional data: https://lekiosque.finances.gouv.fr/site_fr/regions/comparaison_region.asp?serie=I0000 and https://lekiosque.finances.gouv.fr/site_fr/regions/data_region.asp?lreg=0300
- ONS 2023: https://www.ons.gov.uk/businessindustryandtrade/internationaltrade/bulletins/internationaltradeinuknationsregionsandcities/2023/pdf
- HMRC RTS Q4 2025: https://www.uktradeinfo.com/trade-data/regional/2025/uk-regional-trade-in-goods-statistics-fourth-quarter-2025/
- ISTAT regional exports Q4 2025: https://www.istat.it/wp-content/uploads/2026/03/Esportazioni-regioni_122025.pdf
- Turkey: ADASO Dec 2025 report (TİM and Ministry tables): https://adaso.org.tr/Content/Files/raporlarFiles/2026/1/42f3ad85-9a74-47f3-880f-10a6467191e4_2025 YILI ARALIK İHRACAT RAPORU_ADASO.pdf ; ASO 2025 report: https://aso.org.tr/uploads/attachments/ASO%202025%20YILI%20%C4%B0HRACAT%20DE%C4%9EERLEND%C4%B0RME%20RAPORU.pdf ; TİM İhracat 2025 Raporu: https://tim.org.tr/files/downloads/Strateji_Raporlari/Ihracat2025Raporu.pdf
- Brazil: O Liberal/Fapespa: https://www.oliberal.com/economia/balanca-comercial-do-para-fecha-2025-com-saldo-de-us-21-5-bilhoes-1.1122978 ; Guia Marítimo: https://www.guiamaritimo.com.br/noticias/comercio-exterior/manaus-passa-a-liderar-o-ranking-dos-municipios-que-mais-importam-no-brasil-em-2025 ; SJC: https://www.sjc.sp.gov.br/noticias/2026/janeiro/26/sao-jose-exporta-para-120-paises-e-diversifica-mercados-em-2025/
