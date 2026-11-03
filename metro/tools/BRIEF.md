# Worker brief: metro line facts and opening stages

You are one of several workers compiling the line-level facts of a world metro database for ScraperMap's metro history mode. Each worker covers one region. Your group's systems are in `<group>.systems.json` next to this file. Work only on those systems (plus any qualifying system in your region that the list misses: add it with a new `system_id` and say so in your report).

## Hard rules
- Do NOT call any `mcp__hearthbot__` tool. You never post to the user; your final message is a report to the session that started you.
- Do NOT write anywhere under `/mnt/project-files/`. Write only the two output files named below. Do not install packages.
- Copy figures exactly as the source gives them. Never estimate, never fill a value from memory. Unknown means empty string (or null for numbers).
- Every line and every stage carries the URL(s) it came from.

## Read first
`/mnt/project-files/metro/metro-definition.md` (v1.1) decides what counts. Read sections 2 to 5 and the section 9 rulings that touch your region. Key points:
- Only lines that pass all seven tests are metro lines. Monorails of every kind (straddle and suspended "skyrail"), trams, streetcars, light rail with street running or unbarriered level crossings, suburban/commuter rail (S-Bahn, RER, JR, Korail's own lines, CPTM, China Railway suburban lines, 市域铁路 presented as suburban railway), single-site people movers and circulators are OUT.
- China's metro-numbered express/airport lines that run under the metro's identity are IN, tagged `express: true`, with `national_mode` (e.g. 市域快轨) if CAMET classes them so.
- History counts: closed lines and closed sections are IN with their closing dates (New York's and Chicago's demolished elevated lines, Toronto Line 3, Boston's Els, the Liverpool Overhead Railway...). Steam/cable-hauled early lines count from first public service.
- A line runs as far as trains run under its metro identity; through-running onto another network's line stops at the boundary.
- Record excluded lines of your systems too (with `included: false` and the failing test), so the table is auditable. Never-built or under-construction lines: skip.

## Network
Command-line access to Wikipedia, Wikidata and OpenStreetMap is blocked. Use the **WebFetch** tool: one page per call. Ask it for compact pipe-separated output, for example: "Output every row of the table of lines as compact pipe-separated lines: Line|Termini|Opened|Last extension|Length km|Stations|Ridership (with unit and year)|Rolling stock|Cars per train. Copy values exactly; ? for missing; no commentary." For a long page, call again with the `offset` the result gives. Other-language Wikipedias (zh, ja, ko, ru, de, fr, es, pt...) and operator websites are allowed and often better (zh.wikipedia for Chinese opening timelines and 车型). Use WebSearch only to find a page.

## What to collect, in this order
1. **Lines, for every system in your group first** (one row per line, including excluded lines). Usually the system's English Wikipedia article has a lines table and a rolling-stock section; open each line's article when the system page lacks length, opening date, ridership or rolling stock for it.
2. **Opening stages**, after all lines are done: for each included line, every dated event that changed it (opening of the first section, each extension, each closure, reopening, infill station if dated, transfer of a section to another line). Line articles usually have an "Opening timeline"/"History" table. For lines with very long histories (London, Paris, New York, Chicago, Berlin, Moscow), capture every extension/closure you can find with dates; say in the report where it's incomplete.

## Output files (JSON Lines, UTF-8, one object per line)
Append with a small Python heredoc so quoting is safe, e.g.
```
python3 - <<'EOF'
import json
rows=[{...},{...}]
with open('OUT_PATH','a',encoding='utf8') as f:
    for r in rows: f.write(json.dumps(r, ensure_ascii=False)+'\n')
EOF
```
Append after each system so partial work survives.

### `<group>.lines.jsonl`
| key | meaning |
|---|---|
| line_id | `<system_id>:<ref-slug>`, e.g. `cn-beijing-subway:1`, `cn-beijing-subway:daxing-airport-express`, `gb-london-underground:central`, `us-new-york-city-subway:a`, `us-chicago-l:humboldt-park-branch`. Lowercase ascii, hyphens. Permanent: never reuse for a different line. |
| system_id | from your systems file |
| ref | number/letter as shown on the map ("1", "A", "M2", "U4"); "" if none |
| name_en | English name ("Line 1", "Central line", "Red Line") |
| name_local | name in local script ("1号线", "銀座線") or "" |
| colour_hex | official colour "#RRGGBB" if stated, else "" |
| termini | current (or final, if closed) termini "A – B"; branches "A – B / C" |
| included | true / false |
| ruling_test | "" if included; else the failing test, e.g. "T1" (monorail), "T3" (tram/light rail), "T7" (commuter rail) |
| ruling_note | short reason or caveat ("monorail", "check: 2 level crossings") |
| status | "open", "closed", or "partly_closed" |
| opened | first day of public service of the first section: "YYYY-MM-DD", or "YYYY-MM" / "YYYY" if that is all the source gives |
| latest_extension | date of the most recent extension or "" |
| closed | last day of service if the whole line closed, else "" |
| length_km | route length as stated (number) or null |
| stations | number of stations as stated (number) or null |
| annual_ridership_m | annual passengers in millions as stated (number) or null. If the source gives a daily average, put null here and fill ridership_daily_k |
| ridership_daily_k | average daily passengers in thousands as stated, or null |
| ridership_year | year (or fiscal year) of the ridership figure, e.g. "2024" |
| ridership_note | basis if stated: "journeys", "boardings", "entries+transfers", "line ridership incl. transfers" |
| rolling_stock | train models in service (and notable past ones), e.g. "CRRC Changchun DKZ16 (Type B, 6 cars); Bombardier MOVIA 456 (8 cars)". Free text, concise |
| car_type | the car class: China "Type A" / "Type B" / "Type As" / "Type D" / "Type L(B)" (linear motor); elsewhere a short class like "heavy rail, 3.2 m wide", "light metro", "rubber-tyred", "AGT (rubber-tyred)", "linear induction", "maglev", "Stock: 2009 Stock (deep tube)" |
| cars_per_train | e.g. "6", "4–8" |
| power_supply | e.g. "1500 V DC overhead", "750 V DC third rail" |
| gauge_mm | e.g. 1435, or null |
| automation | e.g. "GoA4 driverless", "GoA2", "" |
| technology | "steel_rail", "rubber_tyre", "agt", "maglev" or "linear_induction" |
| express | true if average station spacing > 3 km or an airport/express line of a metro, else false |
| national_mode | official national mode if relevant (China CAMET: 地铁/轻轨/市域快轨/磁浮; US NTD: heavy rail), else "" |
| operator | operating company |
| sources | list of URLs |
| notes | anything the map or a later pass should know (shared track, through-running, renumbering, predecessor tram) |

### `<group>.stages.jsonl`
| key | meaning |
|---|---|
| line_id | as above |
| event | "open" (first section), "extension", "closure", "reopening", "infill_station", "transfer" (section moved between lines), "renaming" |
| date | "YYYY-MM-DD" or "YYYY-MM" / "YYYY" |
| from_station | first station of the stretch (as named at the time; add today's name in brackets if different) |
| to_station | last station of the stretch ("" for a single station) |
| length_km | length of the stretch as stated, or null |
| stations_added | number of stations added (negative for closures), or null |
| note | e.g. "steam until 1905", "temporary", "branch" |
| source | URL |

## Final report (your last message, under 250 words)
Per system: lines included / excluded, stages captured, and gaps (fields missing, histories incomplete, rulings that need checking). List any system you added and any case where the definition's rules left the decision open.
