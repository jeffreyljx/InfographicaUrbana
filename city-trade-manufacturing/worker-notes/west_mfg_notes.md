# Manufacturing output and productivity: US, Europe and other non-East-Asian metros (notes)

File: `/tmp/claude-0/-home-claude/99c09ce4-a7f2-59e9-a667-27f63e15c2f7/scratchpad/research/west_mfg.csv` (98 rows).
Values are in **millions** of the currency named in each row. Employment is in **persons**, not thousands.

## How the data was collected

- **Access limits.** The proxy refused curl to ec.europa.eu, apps.bea.gov, bls.gov, census.gov, statcan and IBGE, so no raw files were downloaded. Every figure was read through WebFetch from an official API response or a published page. The URL for each row is in `source_url`. The WebSearch budget ran out partway through, which limited the US secondary sources (see below).
- **Eurostat.** The NUTS-3 tables `nama_10r_3gva` (GVA, NACE C, `CP_MEUR` / `CP_MNAC`) and `nama_10r_3empers` (employed persons `EMP`, NACE C, thousands) were read with the SDMX 2.1 REST API, using keys such as `A.CP_MEUR.C.DE111+DE112...`. That API returns geo codes next to the values. The candidate top-50 came from a JSON query for every NUTS-3 region in 2023. Every value in the CSV was then re-read by explicit geo code. That re-read caught one mapping error in the JSON listing: Kocaeli is TR421, not TR422. The metro rows come from `met_10r_3gva` (dimension `currency=MIO_EUR`) and `met_10r_3emp`, re-read the same way.
- **US.** BEA **discontinued GDP for metropolitan statistical areas (MSAs)** from the 2024 data year onward. The Feb 5 2026 release says: "BEA has discontinued publication of statistics for metropolitan statistical areas". BEA now publishes counties only and points users to its `bea_geo_aggregator` tool, which needs a BEA API key. The last official MSA vintage is 2023, which sits in the BEA data archive. Those official tables could not be reached: curl was blocked, the interactive tables are rendered in JavaScript, and the API needs a key. In their place:
  - **Manufacturing GDP for 2024** comes from the Greater Houston Partnership's *Economy at a Glance* (March 2026). It ranks the top 10 metros by manufacturing output in 2024, which GHP computed by summing BEA county GDP.
  - **Manufacturing employment** comes from the BLS Current Employment Statistics (CES) survey: annual-average "All Employees: Manufacturing" for each MSA, read from FRED (`SMU{state}{msa}3000000001A`).
- **Brazil.** IBGE SIDRA API, table 5938, variable 517 (gross value added of industry at current prices, in R$ thousand). The latest year filled in is 2021; 2022 and 2023 show "...".

## Definitions

| Column | Meaning |
|---|---|
| mfg_value_added | Gross value added at basic prices in manufacturing (NACE C / NAICS 31-33), current prices. For the US rows it is the GHP figure, which aggregates BEA county GDP (see caveats). |
| industrial_value_added | Brazil only: industry = mining + manufacturing + utilities + construction. |
| employment | Eurostat: employed persons, including self-employed, counted at place of work (domestic concept, national-accounts basis). US: CES wage-and-salary jobs, which leave out the self-employed. BEA's CAEMP25N series, which counts jobs including proprietors, would be about 3–8% higher. |

## Main results

**US, 2024, USD millions.** Manufacturing VA from GHP (aggregated BEA county data); employment from BLS CES.

| MSA | Mfg VA | Mfg jobs | VA per job |
|---|---|---|---|
| Houston | 126,900 | 239,100 | $531k |
| Los Angeles | 119,200 | 467,500 | $255k |
| Chicago | 100,900 | 405,500 | $249k |
| New York | 82,500 | 330,600 | $250k |
| San Jose | 74,200 | 126,400 | **$587k** |
| San Francisco–Oakland | 72,000 | 139,600 | $516k |
| Dallas–Fort Worth | 71,600 | 312,200 | $229k |
| Detroit | 50,600 | 249,400 | $203k |
| Boston | 48,700 | n/a | n/a |
| Atlanta | 42,000 | 180,400 | $233k |

**Europe, NUTS-3, 2023, EUR millions.** Largest by manufacturing GVA:

| Region | Mfg GVA |
|---|---|
| South-West Ireland (Cork & Kerry) | 90,680 |
| Istanbul | 47,652 (TRY 1.228 trillion) |
| Barcelona | 29,449 |
| Milano | 24,765 |
| München Stadt | 23,189 |
| Dublin | 21,718 |
| Västra Götaland | 20,210 |
| Stuttgart Stadt | 19,745 |
| Københavns omegn | 18,921 |
| Böblingen | 17,666 |
| Kocaeli | 17,380 |
| Eindhoven region | 17,357 |
| İzmir | 16,652 |
| Wolfsburg | 16,165 |
| Ankara | 16,083 |
| Hamburg | 16,072 |
| Torino | 15,984 |

**European aggregates built from NUTS-3, 2023:**

| Aggregate | Mfg GVA | Employed persons | GVA per person |
|---|---|---|---|
| Region Stuttgart (6 NUTS-3) | EUR 63,727m | 369,870 | EUR 172k |
| München Stadt + Landkreis | EUR 32,275m | 153,590 | EUR 210k |

**Eurostat metro regions, 2021** (official aggregates; later years are mostly empty):

| Metro | Mfg GVA |
|---|---|
| Cork | 83,928 |
| Stuttgart | 47,875 |
| Paris | 37,221 |
| Dublin | 36,446 |
| München | 31,814 |
| Milano | 28,641 |
| Barcelona | 27,765 |

**Highest VA per worker, in EUR:**

| Region | GVA per worker | Driver |
|---|---|---|
| South-West Ireland | about EUR 1.71m | Multinational profits booked in Ireland |
| Københavns omegn | about EUR 510k | Novo Nordisk |
| Dublin | about EUR 402k | Multinationals |
| Ireland West / Mid-West | about EUR 334k | Multinationals |
| Ingolstadt | about EUR 318k | Audi |
| Stuttgart Stadt | about EUR 255k | |
| Turnhout | about EUR 242k | Janssen pharma |

By contrast, Milano is about EUR 110k and Barcelona about EUR 86k.

**Lake Charles, Beaumont, Corvallis and Hillsboro were not verified.** I could not reach county- or MSA-level BEA data for these small metros, so their very high per-worker values remain unconfirmed.

## Caveats

1. **Irish figures.** These are dominated by foreign multinationals' pharma, medtech and IT-hardware production and by profits booked in Ireland, including contract manufacturing and intellectual-property income. GVA swings sharply: South-West was 110.7bn in 2022 and 90.7bn in 2023, and Dublin fell from 34.2bn to 21.7bn. Read them as accounting value added, not physical output. The Copenhagen suburbs (Novo Nordisk) and Turnhout (Janssen) have a similar but smaller pharma effect.
2. **US GHP numbers.**
   - GHP says its metro GDP is "real GDP in '24 dollars", so for 2024 it is roughly equal to current dollars. Chain-weighting means sums of real components will not exactly equal nominal totals.
   - The manufacturing figures are GHP's own aggregation of BEA county data, not an official BEA MSA estimate.
   - The metro-to-value pairing was read from chart text. The internal checks hold: Houston is first, ahead of Los Angeles since 2022, and "more than double Detroit". Still, verify the pairing if precision matters.
   - BEA suppresses some county-by-industry cells. GHP notes that wholesale trade and information were withheld for Houston.
3. **How BEA allocates metro and county GDP.** It is allocated by establishment location using earnings (compensation plus proprietors' income) and gross operating surplus. Headquarters-heavy or IP-heavy metros, and refinery or chip-fab metros, can therefore show very high VA per worker.
4. **Employment definitions differ by source.**
   - US CES counts jobs on payrolls and excludes the self-employed. Its MSA definitions follow the 2023 OMB delineations; FRED titles still use some older names, such as Houston-The Woodlands-Sugar Land and San Francisco-Oakland-Hayward.
   - Boston: CES switched from New England city areas (NECTAs) to MSAs. The Boston-Cambridge-Nashua NECTA series stops at 2023 (184.0k), so no 2024 MSA employment was entered.
   - Eurostat counts persons employed, including the self-employed.
5. **Eurostat flags and gaps.**
   - German and Spanish 2023 values are provisional (p). Germany, Italy, Spain and Austria have no NUTS-3 data for 2024 yet. Ireland, Denmark, Sweden, Finland, Turkey, France, Belgium and Czechia do have 2024.
   - Turkey has GVA but no NUTS-3 employment by industry in Eurostat, so Turkish employment is blank.
   - Switzerland (including Basel) and Norway have no NUTS-3 GVA by industry in Eurostat. The UK is no longer in Eurostat.
   - NUTS-3 units are administrative units, not functional metros. A city Kreis such as Wolfsburg or Ingolstadt captures a plant whose workers commute in from surrounding districts.
6. **Brazil.** "Indústria" includes mining (Parauapebas is the Carajás iron-ore mine), utilities and construction. The latest municipal year is 2021.
7. **Not collected** because no verifiable page was reachable without search: Mexico (INEGI Censos Económicos 2024), India, Israel, Russia/Moscow, Canada (StatCan table 36-10-0468-01 showed no industry dimension), the Swiss cantons (BFS), the UK (ONS ITL3 tables) and official BEA 2023 MSA values.

## Sources

- **Eurostat API:**
  - `https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/nama_10r_3gva/...`
  - `.../nama_10r_3empers/...`
  - `.../met_10r_3gva/...`
  - `.../met_10r_3emp/...`
  - JSON: `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10r_3gva?format=JSON&nace_r2=C&unit=CP_MEUR&time=2023&geoLevel=nuts3`
- **BEA:**
  - https://www.bea.gov/data/gdp/gdp-county-metro-and-other-areas
  - https://www.bea.gov/sites/default/files/2026-02/lagdppi0226.pdf
  - https://github.com/us-bea/bea_geo_aggregator (README)
- **Greater Houston Partnership:**
  - https://wpb.houston.org/app/uploads/2026/03/Glance-March-2026-Final.pdf
  - https://houston.org/houston-data/economy-at-a-glance-march-2026/
- **FRED / BLS CES:** `https://fred.stlouisfed.org/data/SMU<state><msa>3000000001A`, plus `HOUS448MFGN` and `SMU25716503000000001A`.
- **IBGE:** https://apisidra.ibge.gov.br/values/t/5938/n6/3550308,1302603,1505536,3304557,3106705,3518800/v/517/p/2021,2022
