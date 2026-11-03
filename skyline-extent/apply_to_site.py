"""Put the 11 Oct 2026 skyline extents (density rule, pockets of 5+ towers) into a ScraperMap checkout.

Usage: python3 apply_to_site.py /path/to/scrapermap-repo [/path/to/skyline-extent.geojson]

Run it on a tree that already has the live patches (skyline-extent-site-changes, tower-icons,
skyline-size; time-capsule, skyline-years or map-scale on top is fine). It copies the new GeoJSON to
public/skyline-extent.geojson and replaces the texts that still describe the old rule
("the 38 cities with more than 50 towers"). Each replacement is reported; nothing else is touched.
The Cities table texts may already be generic (skyline-size.patch's second commit); either wording is
handled, and a missing optional text is reported but not an error.
Commit the result and save it as a patch next to the others in scrapermap/patches/.
"""
import os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
# (file, old texts (first one found is replaced), new text, required)
EDITS = [
    ("src/components/MapApp.tsx",
     ["skyline extent: the urban core of each city with more than 50 towers (remembered per browser"],
     "skyline extent: every dense pocket of 5+ towers, in any city (remembered per browser", True),
    ("src/components/MapApp.tsx",
     ['"Display skyline extent: the urban core of each city with more than 50 towers"'],
     '"Display skyline extent: wherever 5 or more towers stand close together"', True),
    ("src/components/MapApp.tsx",
     ["Skyline extents are drawn for the 38 cities with more than 50 towers. Zoom in on one to see its core."],
     "Skyline extents are drawn wherever 5 or more towers stand close together. Zoom in on a city to see them.", True),
    ("src/components/skylineLayer.ts",
     ['"Display skyline extent": the urban core of each city with more than 50 towers, drawn as a gold'],
     '"Display skyline extent": every pocket of 5+ towers standing close together, drawn as a gold', True),
    ("src/components/CitiesTable.tsx",
     ["Area of the city's skyline extent, the urban core drawn on the map for the cities with more than 50 towers\"",
      "Area of the city's skyline extent, the urban core outlined on the map\""],
     "Area of the city's skyline extent, drawn on the map wherever 5 or more towers stand close together\"", False),
    ("src/components/CitiesTable.tsx",
     ["skyline extent, the urban core drawn on the map for the 38 cities with more than 50 towers, measured",
      "skyline extent, the urban core outlined on the map when Display skyline extent is on, measured"],
     "skyline extent, drawn on the map wherever 5 or more towers stand close together, measured", False),
]

def main(repo, gj):
    ok = True
    for rel, olds, new, required in EDITS:
        p = os.path.join(repo, rel)
        s = open(p, encoding="utf-8").read()
        if new in s:
            print(f"already done  {rel}: {new[:60]}")
            continue
        old = next((o for o in olds if o in s), None)
        if old is None:
            print(f"{'NOT FOUND    ' if required else 'not present  '} {rel}: {olds[0][:60]}")
            ok = ok and not required
            continue
        n = s.count(old)
        open(p, "w", encoding="utf-8").write(s.replace(old, new))
        print(f"replaced x{n}  {rel}: {old[:60]}")
    dst = os.path.join(repo, "public", "skyline-extent.geojson")
    shutil.copyfile(gj, dst)
    print(f"copied {gj} -> {dst} ({os.path.getsize(dst)} bytes)")
    if not ok:
        sys.exit("some texts were not found; check the tree has the live patches")

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "skyline-extent.geojson"))
