# City-limits GDP — research rules (read fully before starting)

We run ScraperMap, a ranking of cities by skyscrapers. We are adding a GDP column to the Cities table. The user's
instruction, verbatim: "a 2025 (or most recent) GDP (calculated strictly within city limits) figure ... Use '-' for
cities for which there is no data, but try your best to find data for within city-limits (not broader metro area) GDP
figures for all these cities."

You research GDP for the cities in your input file and write one result per city. Currency conversion (nominal US$ and
PPP) is done later by us — you only report the figure in the currency the source uses.

## What counts as "within city limits"

The territory of the city's own municipality / city government (the city proper). Examples that ARE city limits:
- a mainland-Chinese prefecture-level or sub-provincial city as a whole (地级市/副省级市 市域, including its counties and
  county-level cities) and the four municipalities (Beijing, Shanghai, Tianjin, Chongqing) as a whole;
- Hong Kong SAR, Macau SAR, Singapore, Monaco;
- Korean special / metropolitan cities (Seoul 서울특별시, Busan 부산광역시 …) and ordinary si (창원시, 천안시 …);
- Tokyo Metropolis (東京都) for "Tokyo"; other Japanese cities as the municipality (大阪市, 横浜市 …);
- city-counties and consolidated city-counties in the US (San Francisco County, Philadelphia County, Denver, Baltimore
  city, St. Louis city, Orleans Parish, Virginia Beach city, Nashville-Davidson, Louisville/Jefferson County Metro …);
  New York City = sum of its five counties (New York, Kings, Queens, Bronx, Richmond);
- federal cities / capital districts / city-states / city-provinces (Moscow, St Petersburg, Kyiv, Berlin, Vienna,
  Ciudad de México, CABA, Bogotá D.C., Tashkent city, Almaty city, Astana city, Baku city, Belgrade city, Sofia-city,
  Kuala Lumpur FT, DKI Jakarta, Bangkok, Metro Manila/NCR (our "Metro Manila" entity IS the NCR), Ho Chi Minh City,
  Hanoi, Nairobi County, Delhi NCT …);
- Turkish metropolitan provinces (since 2012 the metropolitan municipality covers the whole province);
- Greater London for "London" (our London entity is Greater London);
- a municipality (município, municipio, commune, Gemeinde, kota, cantón …) when an official municipal GDP exists.

NOT city limits: metropolitan areas (US MSA, Canadian CMA, EU functional urban areas, "Greater X" metro estimates, metro
regions, city regions), provinces/states/regions/counties that are clearly larger than the city, and partial sums of
some districts. Do NOT use a metro figure "because it is the best available" — write null instead.

Special cases:
- `merged_suburbs`: our dataset folds these suburbs into the city for counting towers. EXCLUDE them. Report the core
  city only (e.g. City of Vancouver without Burnaby/Surrey; Paris = Ville de Paris/département 75 without Courbevoie).
- `osm_unit`: the OpenStreetMap boundary we draw for the city — a hint only. If it is larger than the city (a province,
  emirate, division), still report the city's own limits if a figure exists; you may use the larger unit only if it is
  effectively the city (see "coterminous" below).
- Administrative changes in 2025 (e.g. Vietnamese province/city mergers of July 2025): report the figure for the unit
  as it existed in the reported year and say so in notes.

Set `coterminous`:
- "exact" — the statistical unit is the city's legal territory (or legally coterminous with it);
- "near"  — the unit differs only marginally (e.g. a county that also contains a few small towns making up only a few
  per cent of its population, or a city-province with some rural fringe); explain in notes;
- if the only unit available is materially larger or smaller than the city: value = null.

## What figure

- GDP at current prices (nominal), most recent year. Prefer calendar 2025 if an official (even preliminary) figure is
  out; otherwise the latest year published. Never real/chained/constant-price GDP, never per capita, never growth rates.
- If the official measure for that geography is GVA / gross value added / GRDP / GSDP / GDDP / GRP / GCP / PIB / PDRB
  ADHB / 地区生产总值 / 市内総生産 / 지역내총생산, use it and name it in `measure`.
- `value` in FULL local-currency units as a number (e.g. 36,800 亿元 → 3.68e12; 1.2 兆円 → 1.2e12; 50조원 → 5e13;
  R$ 1.000 table units → multiply by 1,000; ₹ lakh crore → 1e12, crore → 1e7). Re-check the unit before writing.
- `currency` ISO code (CNY, HKD, MOP, JPY, KRW, TWD, USD, CAD, BRL, MXN, COP, ARS, EUR, GBP, CHF, RUB, PLN, TRY, …). If
  the only official figure is in US$, report it in USD.
- `year`: the calendar year. For fiscal years give `period` (e.g. "FY2023 (Apr 2023–Mar 2024)") and set `year` to the
  calendar year that contains most of it (Apr–Mar → the start year; Jul–Jun → the end year).
- Sanity-check every value against population (GDP per capita should be plausible for that country/city).

## Sources

Acceptable: national or sub-national statistical offices, central banks, the city government's official statistics /
yearbook / statistical communiqué (统计公报) / economic report, and reputable reporting that quotes those official
figures (give the most primary URL you can). A figure the city itself publishes from a commissioned model (e.g.
Australian councils' GRP from NIEIR/.id, South African metros' GVA in their IDP) is acceptable — set
`source_type` = "city-published estimate". Do not use your own estimates, population-prorated figures, or random blogs.

## Tools

Use WebSearch (mode "standard"; "extended" only when standard results are thin) and WebFetch. The shell in this
environment has NO internet access (curl fails) — do not try it. Be efficient: look for sources that cover many of
your cities at once (national tables of municipal/county/city GDP, articles listing all cities of a province, Wikipedia
lists sourced to official statistics), then fill gaps one by one. Search in the local language where it helps.

## Output

Write a JSON array to the output path you are given — one object per input city, in input order, ALL cities included:

```json
{"city": "Shenzhen", "country": "China", "value": 3.85e12, "currency": "CNY", "year": 2025, "period": "calendar",
 "measure": "GDP (地区生产总值)", "area": "Shenzhen (sub-provincial city, whole 市域)", "coterminous": "exact",
 "source": "Shenzhen Statistics Bureau, 2025 statistical communiqué", "url": "https://...",
 "source_type": "official", "confidence": "high", "notes": "preliminary"}
```

For cities without data: `{"city": ..., "country": ..., "value": null, "reason": "only metro (MSA) GDP is published"}`
(keep the other keys if useful).

`confidence`: high (official figure read from an official source or a faithful quote of it), medium (secondary source
quoting official stats, or unit/period needed interpretation), low (avoid — prefer null).

Write the file early and update it as you go (so partial work survives). When finished, reply with a SHORT summary
(under 250 words): how many cities have a value, which are null and why in a phrase, and anything we should double-check.
