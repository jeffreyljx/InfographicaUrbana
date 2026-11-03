# What counts as a metro: the ScraperMap definition

_Version 1.3 · 19 Oct 2026 (1.1, 12 Oct 05:30 UTC: monorails of every kind excluded on Jeffrey's ruling; China express-line ruling confirmed 05:25 UTC. 1.2, 12 Oct 21:00 UTC: section 9.5 adds the database pass's rulings; no test changed. 1.3, 19 Oct 2026 05:15 UTC: Ningbo Line 12 in as an exception to T5 on Jeffrey's ruling, in 9.5; no test changed) · thread "Defining a metro system" · Jeffrey's instructions and every design choice are logged in [metro.md](metro.md)_

This is the rule set the database thread applies, system by system and line by line, to decide what goes into the database behind ScraperMap's metro history mode. It covers three things: what counts as a metro line (sections 1 and 3), what the database records about it (section 2), and how the rules apply back through time (section 6). Section 9 rules on about 60 hard cases.

**How to use it.** Run the seven tests in the order in section 7. The first test a line fails decides the case, and the ruling names that test. When a case comes up that the rules leave open, add a ruling to section 9 and a line to metro.md. Don't change a test or threshold without Jeffrey's say.

---

## 1. The definition in one sentence

> A **metro line** (rapid transit line) is an urban public passenger line on rails or a rubber-tyred guideway (never a monorail beam), run with self-propelled trains of at least two cars on a right-of-way fully segregated from road, pedestrian and other rail traffic. It runs frequently all day, and it belongs to a metro network rather than to a suburban, commuter, regional or mainline railway. A **metro system** is a network of such lines under one public identity, and it qualifies when at least one of its lines does.

The sentence draws on the definitions already in use, tightened so that each clause becomes a test with a threshold:

| Source | What it says | What this definition takes from it |
|---|---|---|
| UITP, *Global Metro Figures* brief (May 2025, data at 31 Dec 2023) | Metros are "high capacity urban guided transport systems, mostly on rails, powered with electricity, running on an exclusive right-of-way, with trains composed of a minimum of two cars and with a total capacity of at least 100 passengers per train". Light-rail-vehicle, monorail and maglev systems count if they meet the rest. Suburban railways (Paris RER, Berlin S-Bahn, the KLIA express) and suspended systems are excluded. | Guided, exclusive right-of-way, two cars, 100 passengers (T1–T3) |
| Vuchic, *Urban Transit Systems and Technology* (2007) | Right-of-way category A has no level road or pedestrian crossings. Category B is reserved but has level crossings. Category C is street running. Rapid transit uses A; light rail is mostly B. | The segregation test (T3) |
| US National Transit Database | Heavy rail runs on "separate rights-of-way from which all other vehicular and foot traffic are excluded". Commuter rail is "local short distance travel … between a central city and adjacent suburbs", run with railroad practices. | Segregation, and the commuter-rail boundary (T7) |
| Wikipedia, *List of metro systems* (16 May 2026: 214 cities, 961 lines) | Follows UITP. "The name of the system is not a criterion." Excludes light rail, commuter rail, S-Bahn, funiculars, and people movers at airports, resorts and amusement parks. Excludes Barcelona's FGC lines L6–L8 because they share track with commuter trains. | The name never decides; shared track (T4); single-site people movers (T6) |
| UrbanRail.net (Robert Schwandl) | A metro is urban and electric, "totally independent from other traffic, rail or street traffic", with a "maximum interval approx. 10 minutes during normal daytime service". Fully segregated light rail and most automatic people movers count. | Frequency (T5) and technology neutrality |
| Metro Route Atlas | A 15-minute headway is the floor for "frequent". Lines running every 20–30 minutes off-peak are regional or commuter rail. | The 15-minute threshold in T5 |
| China's CJJ/T 114-2007 and CAMET statistics | Metro, light rail, monorail, AGT, maglev, suburban rapid rail (市域快轨) and tram are separate modes, with capacity bands (metro 25,000–70,000 passengers per hour per direction; light rail, monorail and AGT 10,000–30,000). | Recorded as each line's `national_mode`; it informs the rulings but does not decide them |
| **Jeffrey, 12 Oct 2026, 02:31 UTC** | "suburban/commuter rail does not count as metro/subway" | A hard exclusion (T7) |
| **Jeffrey, 12 Oct 2026, 05:27 UTC** | "Just to clarify, no streetcars or monorail or skyrail qualifies" | Hard exclusions (T1, and T3 for streetcars) |

---

## 2. What the database records

**System.** The lines shown together on one official network map under one public brand: *Tokyo Metro*, *Toei Subway*, *MTR*, *Seoul Subway*. Each line records its operator. A city can have several systems. When it's unclear whether operators form one system or several, follow the rows of Wikipedia's *List of metro systems*: Tokyo Metro and Toei are separate rows there, and Seoul's Lines 1–9 are one. A system qualifies when at least one of its lines qualifies. **Only qualifying lines go in the database**, so a system's tram or light-rail lines stay out. A line's system, operator and brand all carry date ranges (KCR's lines joined MTR on 2 Dec 2007).

**Line.** A route with its own identity on the official map: a name, number, letter or colour. Branches without their own identity belong to their parent line. Some cities name their services separately from their physical routes (New York's lettered and numbered services run over named trunk lines). There, the **service** is the line and the physical routes are segments. Every line gets a permanent id, and its names, numbers and colours carry date ranges.

**Segment.** The physical route between two adjacent stations. It is drawn once, along the track centreline, however many tracks or lines use it. An express service that skips stations runs over several segments in a row. Each segment has a geometry, an opening date and, if it closed, a closing date. Lines use segments over date ranges, so a reroute, split or extension changes which line uses a segment, not the segment itself.

**Station.** A place where trains of a qualifying line stop in regular service. Platforms of different lines count as **one station** when passengers can transfer inside the station or through a dedicated passage; UITP and Wikipedia count the same way. Each line that serves the station gets its own record with its own opening and closing dates. Stations where passengers must exit to the street to change are separate stations. Each station has:
- a point location (the centroid of its platforms) and its level (underground, elevated or at grade);
- its names in local script and English, with date ranges;
- an opening date, and a closing date if it closed.

Stations that were built but never opened stay out until they open. Closed stations stay in, with their closing date.

**Opening date.** The first day of regular public passenger service, whether fares were charged or not, to the day where known. Where only the month or year is known, a precision flag records that. Ceremonies, test running and staff-only running do not count. Chinese "trial operation" (试运营) carries the public and so counts as opening. **Closing date** is the last day of public service.

**City.** Each system is attributed to the urban agglomeration it serves, in UITP's sense: the contiguous built-up area, not the administrative city. It is matched to a ScraperMap city by ScraperMap's own rule: suburbs merge into their metro city, and principal cities such as Yokohama, Incheon and Jersey City stay separate. Each station also records the ScraperMap city it stands in, so a system that crosses into a neighbouring city (Guangzhou into Foshan, Shanghai into Kunshan) places every station correctly. A system in a city ScraperMap doesn't have gets a new city record. That will be common, because many metro cities (Glasgow, Lille, Budapest) have no 150 m tower.

**Scope.** Every system in the world that passes the tests is in scope. "Major" is for the map to decide later, by route length or ridership for instance. It is not a test for the database.

---

## 3. The seven tests

Each line is tested on its own, and it is a metro line only if it passes **all seven**. Section 6 explains how the tests apply over time.

### T1 · Guided public passenger line
The line runs on a continuous fixed guideway over its whole length: steel wheels on rails, rubber tyres on a guideway (rubber-tyred metros and AGT), or maglev. It carries the general public on a published timetable or headway.
- **Fails, on Jeffrey's ruling:** monorails of every kind, both straddle-beam and suspended ("skyrail"), and streetcars and trams. Examples: Chongqing Lines 2 and 3, Wuppertal's Schwebebahn, Wuhan's Optics Valley skyrail. Streetcars fail T3 as well.
- **Fails:** buses of every kind (BRT, guided busways, trolleybuses, China's rubber-tyred "ART" trams), aerial cableways, funiculars and inclined lifts, freight and mail railways, and private or staff-only lines.

### T2 · Self-propelled trains of real size
Trains carry their own motors. They have at least two cars, or one articulated vehicle of at least two sections, and room for at least 100 passengers.
- **Fails:** cable-hauled people movers (Perugia Minimetrò, Venice People Mover, Oakland Airport Connector) and small pods (Morgantown PRT).
- **History:** steam-hauled and cable-hauled urban railways pass T2 for their years before electrification (section 6).

### T3 · Segregated right-of-way (Vuchic category A)
Over its whole length the line has no street running, no public access to the track, and no road or pedestrian level crossing at which trains must stop or obey traffic signals.
- **Tolerance.** A line may keep **up to 10 level crossings** at which **trains have absolute priority**: full barriers or gates, with road and foot traffic always stopped for trains. Each crossing is counted on its segment.
  - The limit of 10 admits every line the standard lists treat as metro despite old crossings: Chicago's Brown Line has 6, its Yellow Line 8, and Oslo's Holmenkollen Line 6. It shuts out light rail, which has dozens.
  - A crossing without full barriers fails the line, however few there are.
- **Metro lines that gain a non-metro tail.** If a line opened and ran as a metro, and a later extension added a section that fails T3, the line stays in up to its last station on segregated track. The failing extension is left out. Example: Frankfurt's U4 since its 2008 extension to Enkheim.
- **Lines that never passed.** A line with failing sections from its first day fails as a whole, even if most of it is in tunnel (Toronto's Line 5, Málaga's Line 1).
- **Temporary diversions** of five years or less during construction do not remove a line. The diversion is recorded with its dates and tagged `temporary`. Example: Chicago's street-level Van Buren bypass, 1953–58.
- **Fails:** trams and streetcars, and light rail and Stadtbahn lines with level crossings or street running, even where they use central tunnels (premetro).

### T4 · Dedicated track through the core
The line's **core** runs on track reserved for metro trains: on a normal weekday at least **90 %** of the trains on it belong to qualifying lines.
- **The core** is the stretch between the line's first and last interchanges with other qualifying lines. A line with fewer than two such interchanges must have at least half its length dedicated instead.
- **Outside the core**, the line may share track with suburban, regional, intercity or freight trains. Those sections stay part of the line and are tagged `shared_track`.
- **Several pairs of tracks** (as on a four-track main line): judge the pair the line's all-stops trains use.
- **Passes:**
  - London's Bakerloo line. It shares 12.4 km (just over half its length) with London Overground beyond Queen's Park, but its core, Elephant & Castle–Paddington, is its own.
  - London's Metropolitan line (shared with Chiltern beyond Harrow) and District line (shared Gunnersbury–Richmond).
  - Hong Kong's East Rail line, where intercity trains were a small minority until they stopped in 2020.
- **Fails:**
  - Barcelona's FGC lines L6, L7 and L8. Their central trunks carry more commuter trains than metro trains: up to 32 an hour each way between Catalunya and Gràcia, plus freight on L8's trunk.
  - Seoul's Gyeongui–Jungang line, which shares its Jungang section with KTX-Eum, ITX, Mugunghwa and freight trains.

### T5 · Frequent, all-day service
In normal operation the line's busiest section has a weekday daytime off-peak headway of **15 minutes or better**, with service every day from morning to late evening.
- Branches of a qualifying line may run less often and stay part of it.
- A new line still in a reduced opening phase is judged on the service it was built and announced for.
- Sections with no daily all-day service (peak-only spurs, event-only branches, weekend shuttles) are recorded and tagged `limited_service`.
- **Fails:** lines run like commuter railways, every 20–30 minutes or with a few trips a day.

### T6 · Urban transit, not a single-site people mover
The line serves trips within a city and is not confined to one site.
- **Size.** A stand-alone line, or a system's whole network, needs **at least 3 stations and 2 km**. Short lines and shuttles inside a qualifying system pass on the system's strength: London's Waterloo & City line, New York's 42nd Street Shuttle.
- **Single-site (fails):** lines that serve only an airport (terminal, airside, car-park and rental-car shuttles), a campus, theme park, resort, hospital, exhibition ground or casino estate. This holds even inside a metro system, so Hong Kong's Disneyland Resort line fails.
- **Airport links (pass)** when they are lines of a metro system (Hong Kong's Airport Express, Beijing's airport lines, Delhi's Airport Express), or when they have at least **two intermediate stations** outside the airport that serve the city.
  - A shuttle from a rail station to the airport with one stop or none in between fails: Shanghai Maglev, Orlyval, AirTrain JFK, Changsha Maglev Express.
- **Circulators (fail):** a loop or shuttle whose stations all lie within **1.5 km** of the line's centroid. Examples: Detroit People Mover, Miami Metromover's loops.
- **Heritage and tourist lines (fail).**

### T7 · Part of a metro network, not suburban or mainline rail (Jeffrey's ruling)
The line does not belong to a suburban, commuter, regional or mainline railway network. It belongs to one if it runs under that network's identity. Examples: S-Bahn, S-tog, RER, Transilien, Cercanías and Rodalies, London Overground and the Elizabeth line, JR lines and Japanese private railways' own lines, Korail's own lines, CPTM, KRL Commuterline, Mumbai Suburban, Chennai MRTS, PRASA Metrorail, Metra, LIRR, and China Railway's suburban lines.
- **The name never decides.** "Metrorail" (South Africa), "Metro Trains" (Melbourne) and "Metrolink" (Los Angeles) are commuter railways and fail. Fully segregated lines called "LRT" in Manila and Kuala Lumpur pass.
- **Exception: railway-run sections of a metro line.** A section run by a mainline railway company, but presented as part of a metro line under the same number and run by its through trains, passes T7. It must still pass T3–T5. Examples: the Korail-run sections of Seoul Lines 1, 3 and 4.
  - The exception covers sections of metro lines, not whole lines of a railway network. Korail's own lines (Suin–Bundang, Gyeongui–Jungang and the rest) stay out even though they appear on Seoul's subway map. So do São Paulo's CPTM lines, even though they share the city's line-number series.
- **Stand-alone railways** that are neither metro-branded nor part of a wider suburban network count as metro if every section, not only the busiest, passes T5, and the line ends at the edge of the urban area rather than feeding a regional network. Example: Hong Kong's KCR East Rail after electrification.
- **Why identity and not only physical tests.** No physical test separates the most metro-like suburban railways from the most suburban metro lines.
  - Metro-like suburban rail: the Berlin S-Bahn has mostly dedicated track and most lines every 10 minutes; Copenhagen's S-tog serves every station at least every 10 minutes; Tokyo's Yamanote line runs every few minutes.
  - Suburban metro: Seoul Line 1 runs 218 km; Shanghai Line 16 averages nearly 5 km between stations.
  - UITP and Wikipedia draw the line by network identity, and so does this definition, with T3–T5 as a floor every line must still clear.

---

## 4. Classes and tags

Every qualifying line goes in the database. Tags let the map choose what to show; they never remove a line.

- **`technology`**:
  - `steel_rail`;
  - `rubber_tyre` (Paris, Montréal, Mexico City style);
  - `agt` (small rubber-tyred automated guideway: VAL, Japan's "new transit", Singapore's LRT);
  - `maglev` and `linear_induction`.
- **`class`**:
  - `metro` when the line's longest regular trains are 60 m or more and the technology is steel rail or rubber tyre;
  - `light_metro` for every other steel-rail, rubber-tyre or AGT line (shorter trains, AGT, light-rail vehicles on segregated track);
  - `maglev` by technology.
- **`express`**: an average distance between stations over 3 km (airport and suburban express lines of metro systems, such as Guangzhou's Line 18 or Shanghai's Line 16).
- **`national_mode`**: the line's mode in official national statistics (CAMET in China, the NTD in the US).
- **`automation`**: driver, semi-automatic or driverless, with dates.
- **Segment tags**: `shared_track`, `level_crossings` (a count), `limited_service`, `temporary`, and `traction` (steam, cable or electric, with dates).

---

## 5. Where a line ends

1. A line runs as far as its trains run **under the line's metro identity** on the official network map.
2. **Through-running ends at the boundary.** Where trains continue onto another network's line under that line's name, the other line is not in the database. Examples: Tokyo Metro trains running on onto Tokyu, Seibu, Tobu or JR lines.
3. **Lines built as extensions are included.** Another company's line belongs to the metro line it continues, tagged with its operator, if all three hold: it physically continues that line, it was built as its extension, and it is worked mostly by the metro line's own trains. It must also pass T1–T6 itself. Examples:
   - Kita-Osaka Kyuko beyond the Midosuji Line;
   - the Saitama Railway beyond the Namboku Line;
   - the Tōyō Rapid Railway beyond the Tōzai Line;
   - the Kintetsu Keihanna Line beyond the Chūō Line.
4. **An extension of a suburban line is not a metro line**, even underground. Yokohama's Minatomirai Line continues the Tokyu Toyoko Line, and Tokyo's Rinkai Line is worked mostly by trains running through from the JR Saikyō Line. Both fail T7.
5. Shared sections outside the core stay part of the line (T4).

---

## 6. Applying the rules through history

The animation shows each segment from the day it opened to the day it closed, so the tests apply across a line's whole life, not only today.

1. **A segment enters on the first day it carried public service as part of a qualifying line.** Any earlier life under another mode (tram, light rail, suburban railway) is recorded as `predecessor` with dates, but not drawn. Examples:
   - London's Central line east of Stratford enters in 1946–49, when Underground trains took over former main-line tracks.
   - Brussels' premetro tunnel enters on 20 Sep 1976, when it became metro.
   - Boston's Blue Line tunnel enters when rapid transit trains replaced streetcars in it.
2. **A predecessor that passed the tests is not a predecessor.** If the earlier service itself passed all seven tests, the metro history starts with it. Vienna's electric Stadtbahn of 4 Jun 1925 is the case (section 9).
3. **Physical and identity changes are dated.** T3, T4 and T7 are judged at each point in time. A line can be grade-separated, stop sharing track, or be absorbed into a metro network on a known date, and a section enters from the date it first passed all three.
4. **Train size and frequency are judged on normal operation.** T2 and T5 are judged on how the line runs today, or in its last full year for a closed line, because historical timetables are rarely available.
5. **Before electrification.** The first rapid transit lines were steam-hauled or cable-hauled, and they count from opening if they pass T1 and T3–T7. Examples: London's Metropolitan Railway from 10 Jan 1863, New York's elevated lines, Chicago's South Side Elevated from 6 Jun 1892, and Glasgow's cable-hauled subway from 14 Dec 1896. The `traction` tag records each change to electric.
6. **The evidence decides the start.** A line enters at the earliest date for which evidence shows it passed T1, T3, T4 and T7. Where that can't be shown for an early period, the line starts when it can. Athens Line 1, for example, starts with electrification on 16 Sep 1904 unless the 1869 steam railway can be shown to have passed T3.
7. **Closures.** A segment, station or line that closed keeps its last day of service, so lines demolished long ago appear in the animation and then disappear. Examples: New York's and Chicago's elevated lines, the Liverpool Overhead Railway, Toronto's Line 3. Suspensions of a year or more (war damage, rebuilding, Glasgow 1977–80) are recorded as gaps. Shorter closures are ignored.
8. **Reroutes, splits and renumbering** change which line uses a segment, never the segment's own dates.
9. **Infill stations** have their own opening date, later than their segment's.

---

## 7. Order of the tests, and evidence

Run the tests in this order. The first one a line fails decides the case, and the ruling cites it.

1. T1 guided public passenger line
2. T7 metro network, not suburban or mainline rail
3. T6 urban, not single-site
4. T3 segregation (with its tolerance and tail rules)
5. T4 dedicated core
6. T2 train size
7. T5 frequency

**Evidence, best first:**
1. the operator's own network map, timetables and history pages;
2. documents from governments and standards bodies;
3. UITP and national statistics (CAMET, the NTD);
4. Wikipedia and UrbanRail.net;
5. OpenStreetMap, for geometry and level crossings.

Every ruling and every opening date in the database carries its source.

**A note for the database thread.** From this project's cloud setup, command-line access to OpenStreetMap, the Overpass API, Wikipedia and Wikidata is refused by the network policy (checked 12 Oct 2026). Single pages can still be read through the web-fetch tool. Downloading line geometry in bulk will need those hosts allowed in a cloud environment, or a run on Jeffrey's Mac.

---

## 8. Excluded on purpose

| Excluded | Test | Examples |
|---|---|---|
| Suburban, commuter, regional and mainline rail | T7 | Berlin, Hamburg and Vienna S-Bahn; Copenhagen S-tog; Paris RER; London Overground and Elizabeth line; JR and Japanese private railways; Korail's own lines; CPTM; KRL; Mumbai Suburban; Kolkata Circular Railway; Chennai MRTS; PRASA Metrorail; Melbourne's Metro Trains; Marmaray; China Railway suburban lines (Beijing S2, Shanghai Jinshan Railway) |
| Monorails, straddle-beam and suspended ("skyrail"), on Jeffrey's ruling | T1 | Chongqing Lines 2 and 3; KL Monorail; São Paulo Lines 15 and 17; Bangkok Yellow and Pink; Daegu Line 3; Tokyo, Osaka, Chiba, Tama and other Japanese monorails; Mumbai Monorail; Las Vegas Monorail; Moscow Monorail; Wuppertal Schwebebahn; Wuhan's Optics Valley skyrail; the former Sydney Monorail |
| Trams, streetcars, light rail, Stadtbahn, premetro (Jeffrey confirmed streetcars on 12 Oct 2026) | T3 | Most Frankfurt U-Bahn lines; the Stuttgart, Cologne and Hanover Stadtbahns; Boston's Green Line and Mattapan line; Muni Metro; Brussels and Antwerp premetro; Toronto Lines 5 and 6; Seattle Link; Lausanne m1; Hong Kong Light Rail |
| Single-site people movers and circulators | T6 | Airport people movers (CDGVAL, AirTrain JFK); Orlyval; Disney Resort Line; Hong Kong's Disneyland Resort line; Detroit People Mover; Miami Metromover |
| Cable-hauled or pod systems | T2 | Perugia Minimetrò, Venice People Mover, Morgantown PRT |
| Funiculars, inclined lifts, cableways | T1 | Istanbul Tünel, Haifa Carmelit, Medellín Metrocable |
| Buses | T1 | BRT, guided busways, Nagoya Guideway Bus |

---

## 9. Rulings on hard cases

Status: **In** or **Out** is the ruling. **Check** marks a fact the database thread must confirm before the ruling is final; the default holds until then.

### 9.1 The first lines, and steam and cable traction
| Case | Ruling | Test | Notes |
|---|---|---|---|
| London: Metropolitan Railway | **In from 10 Jan 1863** | T2 (history) | Steam until electric trains from 1 Jan 1905; the Inner Circle was fully electric from 24 Sep 1905. Wikipedia dates London from 1890 (the electric City & South London, public from 18 Dec 1890). Here London starts in 1863. |
| New York: elevated railways | **In from first public service** | T2 (history) | The Ninth Avenue line ran trials by cable from 3 Jul 1868; public service from 14 Feb 1870 (**check**). Steam from 1871, electric 1902–03. The subway opened 27 Oct 1904. Demolished Els keep their closing dates (Sixth Ave 4 Dec 1938, Ninth Ave 11 Jun 1940, Second Ave 1940–42, Third Ave 1955 in Manhattan and 1973 in the Bronx, and the Brooklyn Els). |
| Chicago: South Side Elevated | **In from 6 Jun 1892** | T2 (history) | Steam until 1898. Closed branches keep their dates (Humboldt Park 1952, Garfield Park 1958, Normal Park 1954, Kenwood 1957, Stock Yards 1957, Westchester 1951). |
| Glasgow Subway | **In from 14 Dec 1896** | T2 (history) | Cable-hauled until 30 Nov 1935, then electric. The 1977–80 closure is recorded as a gap. |
| Liverpool Overhead Railway | **In, 6 Mar 1893 to 30 Dec 1956** | — | Electric from the start, and closed. Wikipedia lists no closed systems. |
| Budapest M1 | **In from 2 May 1896** | — | Electric. |
| Boston Main Line Elevated | **In from 10 Jun 1901** | — | The Tremont Street subway (1897) was a streetcar tunnel and is out, except for any tracks El trains used in 1901–08 (**check**). |
| Athens Line 1 | **In from 16 Sep 1904** | T3 (evidence) | The 1869 steam railway enters only if shown to pass T3. |
| Vienna: electric Stadtbahn | **In from 4 Jun 1925** | T2–T7 | The steam Stadtbahn (from 1898) was run by the state railways and fails T7. The city ran the electric Stadtbahn from 4 Jun 1925 (full network from 20 Oct 1925) on its own track bed, with trains of up to nine cars on an all-day clock-face timetable, so it passes; the U4 and U6 continue it. Trams of route 18G ran onto part of it from 20 Oct 1925, as a minority of trains. Wikipedia dates Vienna from 1978. |
| Istanbul Tünel | **Out** | T1 | A funicular. |

### 9.2 Level crossings and the light-rail boundary
| Case | Ruling | Test | Notes |
|---|---|---|---|
| Chicago 'L' crossings | **In** | T3 tolerance | Brown Line: 6 gated crossings (Spaulding, Kedzie, Albany, Sacramento, Francisco, Rockwell). Yellow Line: 8. Purple Line: at least 2, in Wilmette. Pink Line: at grade from Keeler to 54th Avenue (**check** that the count is 10 or fewer). |
| Oslo T-bane | **In from 1966** | T3 tolerance | The Holmenkollen Line has 6 crossings with full barriers. Earlier suburban tramway service is `predecessor`. |
| Rotterdam Metro | **In from 1968** | T3, T4 | Lines A and B have crossings where trains have priority (**check** that each line has 10 or fewer). Line E shares the Laan van NOI–Leidschendam section with RandstadRail trams (`shared_track`). The Hoekse Lijn has been metro since 2019, with at most a couple of freight trains a day, so it stays dedicated. |
| Tyne and Wear Metro | **Out by default** (**check**) | T3 | Five crossings without barriers fail any line they sit on. The Sunderland section is shared with Network Rail, but outside the core. UK statistics count the system as light rail and Wikipedia leaves it out. If all five crossings turn out to lie on later extensions, the tail rule keeps the original lines in. |
| Amsterdam line 51 | **In from 3 Mar 2019 only** | T3 | From 1990 to 2019 it ran on to Amstelveen as a "sneltram" through traffic-light crossings, from its first day, so it fails for those years. Its metro tracks are in anyway through lines 50, 53 and 54. |
| Frankfurt U-Bahn | **U4 in; the other lines out** | T3 | U4 was all tunnel from its opening (**check** the 1980 date). Its 2008 Enkheim extension is a tail and is left out. Wikipedia leaves out Frankfurt altogether. |
| Other German Stadtbahns | **Out by default** | T3 | Test any line that has been fully grade-separated since its opening (Essen U18 and Bochum U35 are worth checking). |
| Brussels | **In from 20 Sep 1976** | T3 | The premetro tunnel (1969) is `predecessor`. Tram routes still in premetro tunnels (T4, T7, T10) stay out until they are converted. |
| Guadalajara SITEUR | **Lines 1–3 in** | T3 tolerance | Line 1 has gated priority crossings (**check** 10 or fewer). Line 2 is all underground. Line 3 (2020) is tunnel and viaduct. Line 4 (Dec 2025): **check** for crossings. |
| Philadelphia | **Market–Frankford, Broad Street, PATCO and Norristown High Speed Line in** | — | The Norristown line is fully grade-separated, on third rail. |
| Cleveland | **Red Line in; Blue and Green out** | T3, T4 | The Red Line shares 4.2 km of grade-separated track with the light-rail lines. |
| Boston | **Red, Orange and Blue in; Green and Mattapan out** | T3 | — |
| Toronto | **Lines 1, 2 and 4 in; Line 3 in, 24 Mar 1985 to 24 Jul 2023; Lines 5 and 6 out** | T3 | Line 3 opened to invited guests on 22 Mar 1985 and to the public on 24 Mar (9.5). |
| Lausanne | **m2 in from 27 Oct 2008; m1 out** | T3 | m1 has 18 level crossings. |
| Spain | **Bilbao and Seville in. Málaga Line 1 out; Line 2 to test. Metrovalencia lines 1 and 2 out; 3, 5, 7 and 9 to test. Palma to test.** | T3, T4 | Bilbao's last crossings were removed in 2010–17. Málaga's Line 1 has had at-grade intersections since opening. Metrovalencia's Line 1 has 25 pedestrian crossings and Line 2 has 12. Palma's M2 shared all its track with the SFM railway in 2013–22. |
| Cairo Line 1, Mashhad Line 1 | **In by default** (**check**) | T3 | Wikipedia lists both, but its own pages contradict each other on at-grade running. |

### 9.3 The commuter-rail boundary
| Case | Ruling | Test | Notes |
|---|---|---|---|
| London Underground shared sections | **In** | T4 | Bakerloo: Queen's Park–Harrow & Wealdstone, 12.4 km, shared with Overground. District: Gunnersbury–Richmond, 3.8 km, shared with Overground. Metropolitan: Harrow-on-the-Hill–Amersham, 23.1 km, shared with Chiltern. All are tagged `shared_track`. East Putney–Wimbledon has belonged to London Underground since 1994 and is dedicated. |
| Elizabeth line, London Overground | **Out** | T7 | The Elizabeth line also fails T4, since most of its length is Network Rail main line. |
| Docklands Light Railway | **In** (`light_metro`) | — | — |
| Barcelona FGC L6, L7, L8 | **Out** | T4 | Matches Wikipedia. |
| Barcelona L12 | **In** (12 Sep 2016) | — | A dedicated 0.6 km shuttle, Sarrià–Reina Elisenda, that passes on the system's strength. It will stand alone on the map because L6 is out. |
| Barcelona TMB lines L1–L5, L9–L11 | **In** | — | — |
| Seoul Lines 1, 3, 4 (Korail-run sections) | **In** | T7 exception | Line 1 runs 218 km, of which Korail runs 210 km. Its Janghang section (Cheonan–Sinchang), shared with intercity trains, is outside the core and tagged. |
| Seoul: Korail's own lines (Suin–Bundang, Gyeongui–Jungang, Gyeongchun, Gyeonggang, Seohae), AREX, GTX-A | **Out** | T7 | Several also fail on their own: Gyeongui–Jungang shares track (T4) and runs every 20–30 min to outer stations, and Gyeonggang averages about 17 min (T5). Wikipedia's main Seoul count leaves these lines out too. |
| Seoul: Shinbundang, Ui LRT, Sillim, Incheon Lines 1–2, Uijeongbu, EverLine, Gimpo Goldline | **In**, each as its own system where Wikipedia gives it its own row | — | — |
| Hong Kong MTR | **In from 1979** (the Modified Initial System) | — | — |
| Hong Kong KCR East Rail | **In from electrification, 1982–83** (**check** the date of the first electric service) | T7 (stand-alone railway) | Diesel main line before that. Part of KCR until 2 Dec 2007, then MTR. Intercity trains (until Jan 2020) were a small minority and freight ended in 2009, so T4 is met. West Rail, Ma On Shan and Tuen Ma are in; the Airport Express is in (`express`). |
| Hong Kong Disneyland Resort line | **Out** | T6 (resort) | — |
| Tokyo Metro, Toei | **In** (Ginza line from 30 Dec 1927) | — | Through-running ends at the boundary. |
| Saitama Railway, Tōyō Rapid, Kita-Osaka Kyuko, Kintetsu Keihanna | **In, as parts of their metro lines** | §5.3 | — |
| Rinkai Line, Minatomirai Line | **Out** | T7, §5.4 | Wikipedia lists both. |
| Tsukuba Express, Keihan Nakanoshima Line, other private railways' underground sections | **Out** | T7 | — |
| Paris Métro | **In from 19 Jul 1900** | — | Line 14 has reached Orly since 24 Jun 2024. |
| Paris RER, Orlyval, CDGVAL | **Out** | T7, T6 | — |
| Delhi Airport Express | **In** (`express`) | — | — |
| Chennai MRTS | **Out until it becomes a Chennai Metro line**, then retest | T7 | Transfer to Chennai Metro was approved in 2025; Southern Railway still ran the trains in Aug 2026. |
| Mumbai Suburban, Kolkata Circular Railway | **Out** | T7 | — |
| São Paulo Metro (Lines 1–5) | **In** | — | Lines 15 and 17 are monorails and are out (9.4). |
| São Paulo CPTM, ViaMobilidade 8 and 9; Rio SuperVia | **Out** | T7 | — |
| Berlin, Hamburg, Vienna S-Bahn; Copenhagen S-tog | **Out** | T7 | — |
| United States | **In:** New York Subway, Staten Island Railway (its own system), PATH, PATCO, WMATA, CTA, MBTA (heavy rail), SEPTA, BART, MARTA, Miami Metrorail, LA Metro B and D, Baltimore Metro, Cleveland Red Line, Honolulu Skyline, San Juan Tren Urbano. **Out:** LIRR, Metra, Metrolink and other commuter railways. | T7 | The "in" list is the NTD's heavy-rail list. BART's eBART section is to test (T5). |
| China: metro-branded express lines | **In**, tagged `express`, with `national_mode` recorded (**Jeffrey confirmed, 12 Oct 2026 05:25 UTC**) | T7 | Guangzhou Lines 18 and 22, Beijing's Daxing Airport Express, Chengdu Line 18 and Shanghai Line 16 run under metro identity. CAMET classes several of them as suburban rapid rail (市域快轨). |
| China: China Railway suburban lines; Wenzhou S1 and S2 | **Out** | T7 | Beijing S2, the Shanghai Jinshan Railway and the Chengdu Chengguan line are run by China Railway. Wenzhou's lines are presented as suburban railway (市域铁路). |
| Melbourne Metro Trains, PRASA Metrorail, LA Metrolink | **Out** | T7 | The name doesn't decide. |
| Istanbul Marmaray | **Out** | T7 | — |
| KL KLIA Ekspres and KLIA Transit | **Out** | T7 | UITP names the KLIA express as excluded. |

### 9.4 AGT, maglev, monorails and people movers
| Case | Ruling | Test | Notes |
|---|---|---|---|
| Every monorail: Chongqing Lines 2 and 3, KL Monorail, São Paulo Lines 15 and 17, Bangkok Yellow and Pink, Daegu Line 3, the Tokyo, Osaka and other Japanese monorails, Mumbai, Las Vegas and Moscow monorails, Wuppertal Schwebebahn, Wuhan's Optics Valley skyrail | **Out** | T1 (Jeffrey's ruling, 12 Oct 2026 05:27 UTC) | Version 1.0 had these in. Wikipedia counts the first six, and UITP counts 15 monorail networks. |
| Yurikamome, Nippori-Toneri Liner, Kobe New Transit, Astram Line, New Shuttle, Kanazawa Seaside Line, Osaka's Nankō Port Town Line | **In** (`agt`) | — | — |
| Lille VAL (25 Apr 1983), Taipei Wenhu line (28 Mar 1996), Vancouver SkyTrain (11 Dec 1985) | **In** | — | — |
| Bangkok Gold Line | **In** (part of BTS) | T6 (system) | 1.8 km and 3 stations. Wikipedia counts it within BTS. |
| Singapore LRT | **Decided by the 1.5 km circulator test** | T6 | Likely in for Bukit Panjang and out for the Sengkang and Punggol loops; compute from station positions. |
| Beijing S1 (30 Dec 2017), Nagoya Linimo (6 Mar 2005) | **In** (`maglev`) | — | — |
| Shanghai Maglev, Changsha Maglev Express | **Out** | T6 airport rule | — |
| Miami Metromover, Detroit People Mover | **Out** | T6 circulator | — |
| Jacksonville Skyway | **Out** | T1, T2 | A monorail since 1997, with single 56-passenger vehicles. |
| Perugia Minimetrò, Morgantown PRT | **Out** | T2 | — |

### 9.5 Rulings made by the database pass (12 Oct 2026)
The thread "Metro systems database" applied the tests to every line and settled these cases. Each one applies the tests as written; none changes a test or threshold.

| Case | Ruling | Test | Notes |
|---|---|---|---|
| Mecca Metro (Al Mashaaer Al Mugaddassah line) | **Out** | T5 | Runs only in the Hajj season, not every day. |
| Palembang LRT | **Out** | T5 | A train every 17 minutes, 94 trips a day, last departure about 20:45. |
| Lagos Blue Line | **In from 4 Sep 2023** | T5 (reduced opening phase) | About one train every 23 minutes in Feb 2026, but built and announced for 5-minute headways (**check**). |
| Lagos Red Line | **Out** | T5 | Nine trips a day; commuter railway in character (T7 too). |
| Singapore LRT | **Bukit Panjang in from 6 Nov 1999; Sengkang and Punggol out** | T6 | Settles 9.4. Bukit Panjang: Choa Chu Kang lies 1.86 km from the centroid of its 13 stations. Sengkang and Punggol, judged loop by loop: every station lies within 1.16 km of its loop's centroid. |
| Bangkok Airport Rail Link; SRT Dark Red and Light Red lines | **Out** | T7 | State Railway of Thailand lines. |
| Shanghai Airport Link; Taizhou S1; Jinhua's Jinyi and Yidong lines | **Out** | T7 | Presented as suburban railway (市域铁路 or 市域轨道交通), like Wenzhou S1 and S2. |
| Xi'an Xihu line | **Out** (**check**) | T7 | Two stations over 26.3 km; believed to be run by China Railway. |
| BYD SkyShuttle: Shenzhen Pingshan, Jinan | **Out** | T1 (Pingshan), T2 (Jinan, **check**) | Small rubber-tyred vehicles on a narrow beam. |
| Wuhu Lines 1 and 2, Cairo's monorails, Moscow Line 13 | **Out** | T1 | Monorails, on Jeffrey's ruling. |
| Tyne and Wear Metro | **Out** | T3 | Settles 9.2. Green line: 4 open level crossings without barriers. Yellow line: 1, at Howdon, on the 1982 original network, so the tail rule can't save it. |
| London: the Metropolitan Railway's Brill branch | **Out** | T3 | A rural roadside tramway crossed by the highway at grade; also T5 and T6. |
| Munich U7 and U8 | **Out** | T5 | Peak-only and Saturday booster services over U1, U2 and U3 track. They add no track, so the map doesn't change. |
| Naples Line 2; EAV's Cumana, Circumflegrea and Circumvesuviana | **Out** | T7 | Trenitalia and EAV suburban railways. |
| Naples Line 11 (EAV, Piscinola–Aversa) | **Out** (**check**) | T7 | English Wikipedia calls it metro; EAV runs it with its suburban railways. |
| Guadalajara Line 4 | **Out** | T3 | 13 of its 15 road crossings are at grade. Settles 9.2. |
| SEPTA Media and Sharon Hill lines (D1, D2) | **Out** (**check**) | T3 | Light rail with level crossings. |
| Los Angeles C Line | **In** | — | Fully grade-separated light metro, so it passes every test. Section 9.3's US list named only the heavy-rail lines and missed it. **Check** the section shared with the K Line for crossings. |
| BART: eBART (Pittsburg/Bay Point–Antioch, 26 May 2018) | **In**, as part of the Yellow Line | T5 | Diesel multiple units, grade-separated, timed to the Yellow Line. Settles 9.3. |
| Oakland Airport Connector | **Out** | T2 | Cable-hauled. |
| Staten Island Railway | **In from 1 Jul 1971** (**check**) | T7 | The city bought it then. Before that it was a Baltimore & Ohio subsidiary carrying freight, recorded as `predecessor` from 1 Feb 1860 (electric from 30 May 1925). |
| Toronto Line 3 | **Opening date 24 Mar 1985** | — | 22 Mar 1985 was the opening for invited guests. |
| Fortaleza | **Sul line out** (**check**); **Oeste and Nordeste out** (**check**) | T5; T3 | Portuguese Wikipedia gives the Sul line a 17-minute headway. Oeste and Nordeste are diesel light rail mostly at grade. If the Sul line fails, the system is out. |
| Recife's VLT lines | **Out** | T5 | No Sunday service. |
| Porto Alegre Aeromóvel | **Out** | T6 | Airport shuttle with no intermediate station. |
| Medellín Metrocable, Caracas Metrocable and Cabletren, Santo Domingo Teleférico | **Out** | T1, T2 | Cableways and a cable-hauled people mover. |
| Hong Kong Express Rail Link; Meerut Namo Bharat | **Out** | T7 | High-speed and regional rapid rail. |
| Mashhad Line 1 | **In** | T3 | Settles 9.2: UrbanRail describes it as a completely segregated light rail system. |
| Tehran Line 5 (Tehran–Golshahr) | **In**, tagged `express` (**check** T3 and T4) | T2, T5, T7 | Runs under metro identity every 10 minutes; trains are locomotive-hauled, which still carry their own motors. Crossings and track sharing are undocumented. |
| Meerut Metro | **In** (**check** T4) | T4 | UrbanRail says it shares track with the Namo Bharat regional trains; Wikipedia says the tracks run alongside. |
| Yongin EverLine | **Out** | T2 | Overrides its 9.3 row. It runs single, non-articulated Bombardier ART 200 cars, so it fails "at least two cars, or one articulated vehicle". |
| Busan–Gimhae LRT | **In** (**check** T3, T5) | — | Two-car automated trains; the sources don't state grade separation or headways. |
| Kobe Hokushin Line | **In from 2 Apr 1988** | §5.3 | Runs as the continuation of the Seishin-Yamate Line; the private Hokushin Kyuko railway owned it until 2020. |
| Tōkadai New Transit (Peach Liner, closed 2006) | **Out** | T5 | About every 20 minutes in the daytime. |
| Free public trial service | **Counts as opening** | §2 | Section 2 counts the first day of regular public service whether fares were charged or not, so a month-long free public trial (Zhonghe–Xinlu, Taichung, Taoyuan, Busan–Gimhae) opens the line, like China's 试运营. Lines dated from an official ceremony (Wenhu, U Line) keep that date unless an earlier public trial is found. |
| Bilbao L3 | **Out** | T7 | Run by Euskotren over its own network, shared along the whole route with Euskotren trains. |
| Madrid Line 10's Suburbano de Carabanchel (4 Feb 1961) | **In from 1961** (**check**) | T7 (stand-alone railway) | A stand-alone line run with metro trains, not part of RENFE's suburban network. If it turns out to have run as a suburban railway, its start moves to the date it joined the metro. |
| Moscow Central Circle (Line 14) | **In** | T7, T4 | Runs as Line 14 under Moscow Metro identity with integrated fares; Russian Railways only operates it. About 23 freight movements a day, on a third track or at night, against trains every 4–8 minutes. |
| Moscow Central Diameters (D1–D4) | **Out** | T7 | Suburban railway lines. |
| Yerevan Metro | **In** (**check** T2) | T2 | Trains of 1 to 3 cars; in if most run with two or more. |
| China north: metro-run express lines | **In**, tagged `express`: Zhengzhou's Chengjiao line, Jinan's Jiyang line, Qingdao Lines 8, 11 and 13, Dalian Lines 3, 12 and 13; Zhengzhou's Zhengxu line and Tianjin's Jinjing line too (**check**) | T7 (China rule) | Zhengxu and Jinjing carry 市域铁路 in their formal names, which put Wenzhou S1 and Taizhou S1 out; they stay in only if they run under the metro's identity. |
| Changchun Line 3, Dalian Line 3 | **In** (**check** T3) | T3 | Changchun Line 3 has 4 level crossings with barriers not stated; 31 km of Dalian Line 3 runs at grade with no crossings mentioned. |
| Xi'an Xihu line | **Out** | T4 | Updates the row above: a commuter service on a freight branch line. |
| Ürümqi Airport line | **Out** | T6 | An airport-only shuttle until Line 2 opens. |
| Hong Kong East Rail | **In from 6 May 1982** (**check**) | T7 (stand-alone railway) | Settles 9.3's date: the first electric trains, Kowloon–Sha Tin; the source doesn't say whether they carried passengers that day. |
| China south and west: express lines | **In**, tagged `express`: Fuzhou's Binhai Express and Guiyang S1; Chengdu S3 too (**check**) | T7 (China rule) | Chengdu S3 is run by Chengdu Metro but its formal name calls it 市域铁路, as with Zhengxu and Jinjing above. |
| Chongqing's Jiangtiao and Bitong lines | **Out** | T7 | Branded as Chongqing suburban railway (市郊铁路). |
| Guangzhou APM (Zhujiang New Town) | **In** | T6 | Its end stations are about 3.9 km apart, so it isn't a circulator. |
| New York: Brooklyn lines that began as surface railways | **Brighton Line (B, Q) from 1908; Canarsie Line (L) from 28 Jul 1906** (**check**); **Franklin Avenue Line from 1906** | T3 (history) | Each started as a steam railway with grade crossings (1865–78); it enters when elevated trains ran on it with its crossings removed. The Canarsie Line kept one gated crossing, at East 105th Street, until about 1973. |
| Waterloo & City line | **In from 1 Apr 1994** (**check**) | T7 | Owned and run by the LSWR, the Southern Railway and British Rail from 8 Aug 1898 until it moved to London Underground; tagged `limited_service`, since it runs on weekdays only. |
| Metropolitan Railway's Aylesbury–Verney Junction section (1891–1936) | **In, as a branch** | T5 (branches) | Rural and infrequent, but a branch of a qualifying line may run less often. |
| Lyon line C | **In from 1978** | T1 | A rack railway converted to metro operation in 1978; exact day to find. |
| Tyne and Wear Metro | **Out** (confirmed) | T3 | Nexus lists five open crossings without barriers: Fawdon, Kingston Park and Bank Foot (1981), Howdon (1982) and Callerton Parkway (1991). |
| Rotterdam Lines A, B, C and E | **In** (**check** still open) | T3 | Crossings where trains have priority, but no count found yet. |
| Spain | **Málaga Line 2 in; Metrovalencia lines 3, 5, 7 and 9 out** (**check**); **Palma M1 and M2 out** | T3, T4; T5, T4 | Settles 9.2. Málaga Line 2 is all underground. Metrovalencia: Line 3 has at least 9 level crossings on its Rafelbunyol section, Line 7 runs over the Torrent line shared with Lines 1 and 2, and Lines 5 and 9 run mainly on Line 3's track. Palma: M1 runs every 20 minutes with no Sunday service; M2 shared all its track with the SFM railway. |
| Ningbo Line 12 (Xiaoyangjiang–Damuwan, opened 22 Sep 2026) | **In**, tagged `express` (**Jeffrey's ruling, 19 Oct 2026 05:10 UTC**) | T5, T7 (China rule) | A cross-sea suburban railway (市域（郊）铁路) run under Ningbo Rail Transit's line number and fares, like Shanghai Line 16 and Dalian Line 12. It fails T5 as written (every 15 minutes at weekday peaks and weekend daytime, 7.5 on Friday afternoons, 20 otherwise) and is let in as an exception; T5 itself is unchanged. |

---

## 10. Where this differs from UITP and Wikipedia

On purpose, this definition departs from the usual lists in four ways.
- **It goes back to the start.** It counts steam and cable railways and closed lines: London from 1863, New York's Els, the Liverpool Overhead Railway and Vienna's 1925 Stadtbahn. Wikipedia lists only open systems and is inconsistent about steam: it dates Chicago from 1892 steam and Glasgow from 1896 cable, but London only from 1890.
- **It tests each line, not whole systems.** That lets in single fully segregated lines of systems the lists leave out, such as Frankfurt's U4.
- **It excludes monorails of every kind, on Jeffrey's ruling.** That removes lines both lists count: Chongqing Lines 2 and 3, KL Monorail, São Paulo Lines 15 and 17, Bangkok's Yellow and Pink lines and Daegu Line 3 (Wikipedia), and UITP's 15 monorail networks. AGT, rubber-tyred and maglev lines that pass every test are in.
- **It applies the commuter-rail and single-site rules strictly.** That removes a few lines Wikipedia counts: Tokyo's Rinkai Line, Yokohama's Minatomirai Line and Hong Kong's Disneyland Resort line.

Every other ruling agrees with Wikipedia's *List of metro systems*.

---

## Sources
- UITP, Global Metro Figures statistics brief (May 2025): https://cms.uitp.org/wp/wp-content/uploads/2025/05/20250506_Global-Metro-Figures_Statistics-Brief_WEB-1.pdf
- Wikipedia, List of metro systems: https://en.wikipedia.org/wiki/List_of_metro_systems
- US NTD glossary: https://www.transit.dot.gov/ntd/national-transit-database-ntd-glossary ; BTS glossary: https://www.bts.gov/archive/publications/state_transportation_statistics/state_transportation_statistics_2013/index/appendix_d
- Vuchic's right-of-way categories, as summarised at https://en.everybodywiki.com/Semi-metro (Vuchic, *Urban Transit Systems and Technology*, Wiley 2007)
- UrbanRail.net, About: https://urbanrail.net/about.htm
- Metro Route Atlas, modes: https://metrorouteatlas.net/modes.html
- CAMET statistics (30 Sep 2025): https://infosharingp2-oss.camet.org.cn/resources/manual/2025/10/11/729132541857861.pdf ; CJJ/T 114-2007: https://oss.camet.org.cn/u/cms/www/202008/18113708ftg1.pdf
- Chicago 'L' crossings: https://www.chicago-l.org/operations/lines/ravenswood.html , https://www.chicago-l.org/operations/lines/yellow.html , https://www.chicago-l.org/operations/lines/douglas.html
- Oslo Holmenkollen Line: https://no.wikipedia.org/wiki/Holmenkollbanen
- Tyne and Wear Metro: https://en.wikipedia.org/wiki/Tyne_and_Wear_Metro
- London shared sections (chainages): https://www.davros.org/rail/culg/bakerloo.html , https://www.davros.org/rail/culg/district.html , https://www.davros.org/rail/culg/metropolitan.html
- Seoul Line 1: https://en.wikipedia.org/wiki/Seoul_Subway_Line_1 ; Gyeongui–Jungang track sharing: https://www.wikitree.co.kr/articles/1165083
- Hong Kong East Rail: https://en.wikipedia.org/wiki/East_Rail_line
- Vienna electric Stadtbahn: https://de.wikipedia.org/wiki/Wiener_Elektrische_Stadtbahn
- Barcelona L7 trunk: https://en.wikipedia.org/wiki/Barcelona_Metro_line_7
- Other line facts: the Wikipedia article for each line or system named in section 9.
