# Station structures and exits on /metro

Written by the "Metro history map" thread, 16 Oct 2026; rewritten 18 Oct 2026 after the station fix. Jeffrey asked
(16 Oct 08:33 UTC) for every station to show, zoomed in, its structure in its line's colour and its exits, like
Baidu Maps does for Shenzhen's Houhai (`houhai-baidu-example.png`; our version is `houhai-scrapermap.png`). On
18 Oct 01:04 UTC he found the drawings inconsistent (Times Square, Châtelet, Houhai and Embankment fine; Chengdu's
interchanges, Gangxia North and Wimbledon not), and Chengdu South drawn as "two small disconnected square platforms"
although its exits show a much larger footprint. A workflow of diagnosis agents inspected 480 badly drawn stations,
four workers then built the 16 rule changes that came out of it, and a review of before-and-after plots checked
them; the rules below are the result (builder 6a83056b497e, rebuilt 18 Oct 2026 19:32 UTC; exit labels extended in
builder 2e7985369221, rebuilt 20:08 UTC and live since 19 Oct 2026).

## Where the data comes from

The OpenStreetMap planet of 15 Oct 2026, read by byte range from its public copy on Amazon S3, in two passes: the
first took platforms, station areas, passages and entrances near the page's stations; the second (18 Oct) took
buildings named like a station or below ground that the first pass skipped, with their multipolygons. Baidu's,
Amap's and Google's terms forbid copying their map data (and the container can't reach them), so nothing comes
from them. OpenStreetMap is open (ODbL), so the site credits it.

## What is drawn, from zoom 14

- **Box**: one per line at each station, in the line's colour, centred on where that line's own trains stop (its
  stop area's stop positions on its track, up to 400 m away when named after the station; proposed stops are
  ignored), not on the station's shared point. Where OpenStreetMap maps the line's platforms (tagged as platforms,
  listed by the line's own stop area or on its own track, at its level and mode) the box follows them, at most 340 m
  long and 50 m wide and never across the track; otherwise it is an approximate box along the track with a dashed
  edge, as long as the line's trains (two cars for a VAL, the system's usual count where a line has none), or as
  long as the station's own building where an elevated line runs through it, stretched outward to the line's own
  exits with the stop positions kept in its middle third, and laid back along the track only at a terminus whose
  stops are unmapped. Underground or elevated is read from the station's own platforms and buildings. Lines of
  different colours sharing one platform or track get one box in lengthwise stripes, only when the boxes share an
  axis.
- **Halls**: underground station and concourse areas, buildings named after the station (岗厦北站 for 岗厦北, also
  with Stasiun, Interchange, Complex, a trailing digit, or a whole-word prefix or suffix of 8+ letters), the
  station's own building above ground, found by its stop area or by geometry (it holds the station's node or stops,
  the track runs 40 m through it, or two exits stand on its outline), its own stop area's buildings and concourse
  outlines, and underground indoor areas with no level that lie on the track and touch two exits (Hidalgo). A hub
  larger than 120,000 m² (Futian), and an own or named hall longer than 250 m or twice the longest box, is clipped
  to 80 m around the metro's boxes plus 30 m strips to its exits (Gangxia North, Houhai, Shenzhen Airport); halls
  shared by lines are cut among the boxes. Mainline, tram and bus halls, buildings holding another operator's
  platforms or stops (Shimbashi's JR and Yurikamome buildings, Nagoya's JR station), halls listed by another stop
  area, malls, public squares, car parks, substations and anything under construction are kept out.
- **Estimated concourse**: where OpenStreetMap maps no hall touching an approximate box and three or more exits
  stand in its frame, a rectangle along the box, each side as wide as its exits less 10 m (12 to 45 m underground,
  12 to 30 m above), at most 30,000 m², cut among the lines at an interchange; lighter, with a dashed edge (areas
  with a 4th element 1, layer metro-st-area-approx). It never pulls in halls or passages, and a mapped hall
  replaces it as soon as one is drawn. Chengdu South gets three (about 46,000 m² together).
- **Passages**: underground footways, steps and corridors, given to the nearest box; a passage several stations
  claim (Namba Walk, Tenjin's underground street, Sapporo's Chi-ka-ho) is split among them at the nearest station.
  Above ground, only footways inside the station's own halls or building, within 20 m of its exits, or crossing
  its own boxes (West Ham's footbridge); never service lanes, named street arcades, or walkways inside a mainline
  station's platforms or building (Charing Cross's Arches, Victoria's mainline concourse) other than the stairs
  down to the metro. Where an exit is reached by no mapped passage, a dashed passage joins it (one trunk along the
  track per box end with short cross links, else a straight line), nearest first, at most 12 or 1,500 m a station;
  two parts of one station with nothing between them (up to 200 m) are joined the same way.
- **Exits**: entrance nodes (railway=subway_entrance and similar, plus the stop areas' entrance members) with the
  exit's letter or number where OpenStreetMap has one (refs, names such as 出口A, Exit 3, 3番出口, 天神駅5番出入り口,
  北口, Gate No. 4, H: BTM Layout, 东1（北）as 东1北, compass names in Tehran, Mashhad, Santiago and São Paulo;
  since 19 Oct also full-width letters and digits read as plain ones (Ａ３ is A3), 2番口, A區出入口, 3번 출입구, Pintu B,
  Entrance A, a code with a bracketed note (B（楼梯）, not F（錯誤）), 八乙女駅北2, 花隈駅西口 as W, the description:*
  keys, and as a last resort the exit's Wikimedia Commons category, which stays out of the convention rule below;
  a leading zero in a name's code is dropped, as refs number them). Not
  labels: a single lowercase letter, an initial, a line or mode sign of the station's own lines (U, S, L3, (7)), a
  keyword inside a word. Where ref and name disagree, the name's code wins only when two or more of the station's
  exits follow it. One label on two exits more than 100 m apart stays on the station's own or nearer one (Euljiro's
  mall doors are drawn unlabelled); unlabelled nodes under 15 m apart are one exit (Santa Anita's nine gates).
  On the map (since 19 Oct) every exit is a rounded blue square (#1F63D0, white halo) with its label in white where it
  has one; about 3,400 exits in East and Southeast Asia have no code in OpenStreetMap and stay plain squares.
  Emergency, service, closed and exit-only doors, lifts and the doors of mainline stations are not exits; an
  unlabelled entrance nearer to another stop area's station (FGC Gràcia at Fontana, Millennium Station at
  Washington/Wabash) or beyond 200 m with another station nearer is dropped. A stop area that belongs to a railway,
  tram or bus is kept out; a metro stop area named like the station within 300 m, or a same-named one in its stop
  area group, is its own, and its exits are kept up to 1 km (Futian's 12A and 12B). Duplicate page stations are
  drawn once (MARTA's SEC District).

## Files

- `coverage_cities.csv`: per system: stations, stations with exits, exits (lettered), boxes and the share from
  mapped platforms, stations with halls, stations with an estimated concourse, estimated passages.
- `coverage_stations.csv`: the same per station.
- The site's data is `public/metro/structures/<system_id>.json` on main of github.com/jeffreyljx/SkyscraperMaps
  (format v2: boxes [station, line, approximate, ring], areas [station, line, ring, estimated], paths [station, line,
  coords, estimated], exits [station, x, y, label, name]; coordinates in millionths of a degree; `builder` names the
  builder's hash, and `_build.json` lists it with the extracts and systems). The builder is
  `scripts/metro/build_structures.py` (DEBUG_STATION=i prints one station's hall candidates; its hall claims are
  logged per system for review; DEBUG_HALLS=i,j prints several stations' hall and box decisions); the planet extraction scripts and their README are in `scripts/metro/osm/`.

## Coverage (16,175 stations, rebuilt 18 Oct 2026 19:32 UTC)

- Exits at 12,357 stations (76%): 46,876 exits, 30,638 of them lettered or numbered (16 Oct: 50,886 and 29,223;
  the drop is duplicate nodes and gate grids merged, and mainline, exit-only and other stop areas' doors removed).
- 18,791 boxes, 8,735 (46%) drawn from mapped platforms, the rest approximate (16 Oct: 18,809 and 43%). The 03:59
  build had 8,840; the difference is untagged footway rings and concourse outlines no longer taken as platforms
  (Luoyang, Times Square's mezzanine) and frames wider than 50 m (Istanbul's M4 and M7, Izmir).
- Halls at 7,403 stations (16 Oct: 4,225); an estimated concourse at 2,329 more (Seoul 242, Chengdu 124, Shanghai
  111, Paris 85, Busan 81). Estimated passages at 6,223 stations.
- Best: exits at every station in Seoul, New York, Paris, Barcelona, Chicago, Tehran, Busan, Santiago, Tokyo, Hong
  Kong, Munich, Saint Petersburg, Toronto, Montreal, Bucharest, Brussels, Prague, Lisbon, Warsaw, Helsinki and others.
- Weakest, where OpenStreetMap has few exits mapped: Nagpur 0%, Hyderabad, Monterrey and Belo Horizonte 5%,
  Medellín 7%, Ahmedabad 9%.

## Known limits

- Where OpenStreetMap has no platforms, halls or exits, the drawing is still a guess along the track: most of
  Chengdu, Changchun, Suzhou, Guiyang and Wuhan, and many Korean stations with long concourses.
- Platforms shared by two lines at a cross-platform interchange go to one line (St Petersburg's Tekhnologicheskiy
  institut); an exit listed by two of one station's single-line stop areas stretches only one line's box.
- Concourses mapped as walkways (Bucharest) and sunken plazas mapped as pedestrian multipolygons (Rotterdam) are
  not yet drawn. The estimated concourse is a guess from the exits: at big interchanges it is large (Namba
  58,000 m², Hommachi 46,000), one far exit widens a whole side, and Voronoi cuts show where lines cross.
- Rule (e) blanks real labels where one stop area holds several numbering schemes (Nagoya's underground malls,
  Porta Susa's three stairs per exit); those exits are drawn, just unlabelled.
