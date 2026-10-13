# City GDP — second pass (read fully before starting)

We run ScraperMap, a ranking of cities by skyscrapers, with a GDP column on its Cities table. A first research pass
found no GDP for the cities in your input file. The site owner says many of them, especially large ones, must have
published figures somewhere, and asked for a DEEP search, always using the LATEST year available (today is
October 2026; 2025 figures are often out, otherwise 2024, etc. — always check for the newest release).

For EVERY city in your input file, find two things:

## 1. `strict` — GDP within the city's own limits
The territory of the city's own municipality / city government (city proper). Examples: a municipality, commune,
district that IS the city (e.g. Distrito Nacional for Santo Domingo, Montevideo department, CABA, Cairo governorate,
eThekwini metro for Durban, Dubai-style emirate only if effectively the city), a Korean si, a Japanese shi, a Malaysian
city council area, an Australian council LGA (City of Melbourne, City of Brisbane, City of Perth), a Canadian city
(City of Toronto). Acceptable sources: national/regional statistics offices, central banks, the city government itself
(statistical yearbook, economic report, budget/IDP documents), a city's economic-development agency, or reputable
reporting that quotes them. Figures the city itself publishes from a commissioned model (economy.id / NIEIR / REMPLAN
for Australian councils, Conference Board / city economic bulletin for Canadian cities, IDP GVA for South African
metros) are fine — mark `source_type: "city-published estimate"`. Do NOT invent or pro-rate figures yourself.
`merged_suburbs` in the input are suburbs the site folds into the city for counting towers: EXCLUDE them (core city
only). `coterminous`: "exact" or "near" (differs only marginally; explain). If nothing qualifies, `strict: null`.

## 2. `container` — the smallest official unit with published GDP that contains the city
Needed even when `strict` exists only if `strict` is not "exact" — otherwise optional. This is the fallback the owner
may choose to show (clearly labelled) when no city-limits figure exists: the smallest administrative/statistical unit
with an official GDP/GVA/GRDP figure that contains all (or nearly all) of the city — e.g. a county, district,
governorate, emirate, province/state, region, prefecture, NUTS3 region, Census Metropolitan Area is NOT allowed (metro
areas are never containers; we want administrative units). Report the unit's population and the city's own population
(same or nearby year, cite them) so we can say "the city is N% of this area's population". If the city spans several
units, give the unit holding most of the city and say so in notes. If the only containing unit is the whole country,
`container: null` (the country figure is already on the site).

## Figures
- Nominal / current-price GDP (or GVA, GRDP, GDDP, PIB, PDRB ADHB, 地区生产总值, 市内総生産, 지역내총생산, etc. — name it in
  `measure`). Never real/chained/constant prices, never per capita, never growth rates.
- `value` in FULL local-currency units as a plain number (e.g. 1.2 trillion → 1.2e12; ₹ crore → ×1e7; ₹ lakh crore → ×1e12;
  table "in thousands" → ×1000). Re-check units. If the only official figure is in US$, report it in USD.
- `currency` ISO code. `year` calendar year; for fiscal years give `period` (e.g. "FY2024-25 (Apr–Mar)") and set `year` to
  the calendar year containing most of it (Apr–Mar → start year; Jul–Jun → end year).
- Sanity-check against population (per-capita must be plausible).

## Tools
WebSearch (mode "standard"; "extended" only when standard is thin — budget roughly 30–40 searches total) and WebFetch.
Search in local languages. The local shell has NO internet. If you need to download a file WebFetch can't read
(xlsx, csv, zip, large PDF), a Vercel Sandbox with full internet exists: load the tools with ToolSearch
("select:mcp__Vercel__run_session_command,mcp__Vercel__get_session_command_logs") and run commands in session
`sbx_DZK2ALRIFx8lHfeGeqyqsvyiWss8` (requestBody {"command":"bash","args":["-c","..."],"wait":true,"timeout":120000}),
then read output with get_session_command_logs (output is capped ~2.5 KB per read — print only what you need; python3,
curl, pip are available; work under /tmp/<your-batch-name>/).

## Output
Write a JSON array to the output path you are given — one object per input city, in input order, ALL cities:

```json
{"city": "Chicago", "country": "United States",
 "strict": null,
 "container": {"value": 5.46e11, "currency": "USD", "year": 2024, "period": "calendar", "measure": "GDP",
   "area": "Cook County, Illinois", "unit_population": 5087000, "city_population": 2721000, "pop_year": 2024,
   "source": "BEA, GDP by county 2024", "url": "https://...", "notes": "Chicago is ~53% of Cook County's population"},
 "reason": "no official GDP is published for the City of Chicago itself"}
```
`strict` objects use: value, currency, year, period, measure, area, coterminous, source, url, source_type
("official" | "city-published estimate"), confidence ("high" | "medium"), notes.

Write the file early and update it as you go. When finished, reply with a SHORT summary (under 200 words): which cities
got a strict figure, which only a container, which nothing, and anything to double-check.
