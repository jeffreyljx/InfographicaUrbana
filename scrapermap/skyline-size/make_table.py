"""Rebuild skyline-sizes.md/.csv from the current skyline-extent.geojson.

Area = geodesic polygon area on the WGS84 ellipsoid (Karney, via pyproj), holes subtracted.
The site computes the same figures at build time (src/lib/geoArea.ts), so the two agree.
Usage: python3 -I make_table.py [path/to/skyline-extent.geojson] [path/to/places.json]
Needs: pip install pyproj
"""
import json, os, sys
from pyproj import Geod

here = os.path.dirname(os.path.abspath(__file__))
src = sys.argv[1] if len(sys.argv) > 1 else "/mnt/project-files/skyline-extent/skyline-extent.geojson"
places = sys.argv[2] if len(sys.argv) > 2 else None
g = Geod(ellps="WGS84")
fc = json.load(open(src))

def ring(r):
    return abs(g.polygon_area_perimeter([p[0] for p in r], [p[1] for p in r])[0])

country = {}
if places:
    country = {c["name"]: c["country"] for c in json.load(open(places))["cities"]}
rows = []
for f in fc["features"]:
    gm = f["geometry"]
    polys = gm["coordinates"] if gm["type"] == "MultiPolygon" else [gm["coordinates"]]
    km2 = sum(ring(p[0]) - sum(ring(h) for h in p[1:]) for p in polys) / 1e6
    city = f["properties"]["city"]
    rows.append((city, country.get(city, f["properties"].get("country", "")), km2))
rows.sort(key=lambda r: -r[2])

md = [f"# Skyline size of the {len(rows)} skyline-extent cities", "",
      "Area of each city's skyline extent (the urban-core outline drawn on ScraperMap), measured from the outline "
      "polygons on the WGS84 ellipsoid (geodesic polygon area, holes such as water bodies subtracted). "
      f"Source polygons: `{src}`.", "",
      "| # | City | Country | Skyline size (km²) |", "|---:|---|---|---:|"]
csv = ["rank,city,country,skyline_size_km2"]
for i, (city, ctry, a) in enumerate(rows, 1):
    md.append(f"| {i} | {city} | {ctry} | {a:.2f} |")
    csv.append(f'{i},"{city}","{ctry}",{a:.2f}')
open(os.path.join(here, "skyline-sizes.md"), "w").write("\n".join(md) + "\n")
open(os.path.join(here, "skyline-sizes.csv"), "w").write("\n".join(csv) + "\n")
print(f"{len(rows)} cities written")
