# Metro footprints (built-up land around each city)

Jeffrey's ask (18 Oct 2026, in the "Display skyline extent" thread): "determine the extent of metropolitan settlement
... another showable/displayable highlight covering each city/metropolitan area's built-up settlement area. e.g. parks,
natural reserves, farms, unexcavated land, rivers should not be considered built-up land, but roads, offices,
residential towers, malls, airports, ports should be considered part of the metropolitan footprint."

## What is here

- `metro-footprint.json`: the file the site serves as `public/metro-footprint.json` (10.3 MB, 2.4 MB compressed).
  320 features, one per metropolitan area, covering 347 of the 348 cities (Ashgabat's one tower, the broadcasting
  centre, stands on a mountainside 8 km from the city's built-up land, so it has none). 174,515 km² in all.
  Properties: `name` (top three cities), `cities` [{city, towers (inside the footprint), towers_in_city}],
  `area_km2`, `pieces`, `clipped` (none is).
- `table.md`: every city with its footprint area, towers inside, and the feature it shares.
- `tools/`: the build (fp.py reads ESA WorldCover tiles, fpbuild.py builds one job, jobs.py groups cities into jobs,
  runall.py runs them all, merge.py joins the outputs). The same scripts are in the site repo under
  scripts/metro-footprint/ with a README that explains the rule in full.
- `check-images/`: the check renders for a few cities (built cells grey, footprint mauve, water blue, towers red).

## Source and rule, in short

ESA WorldCover 2021 (10 m land cover; class 50 "built-up" is buildings, roads, airports, ports and other paved
ground, which matches the ask; parks, farms, bare ground and water are other classes). It is read straight from the
public S3 copy. Cells of about 46 m count as built when a fifth of their pixels are; strips narrower than about 200 m
(highways between fields) are dropped, gaps up to 700 m are bridged, holes under 0.5 km² are filled (larger parks,
fields and airfields' grass stay out); water is cut last. A city claims a contiguous piece that holds at least 3 of
its towers of 150 m+ (or a tenth of them); cities sharing a piece share one feature (Tokyo with Kawasaki, Yokohama,
Chiba, Saitama; nine Pearl River Delta cities, Hong Kong separate; Shanghai with Suzhou, Wuxi, Changzhou; Dubai with
Sharjah and Ajman; Seoul with Incheon; Miami with Fort Lauderdale; Osaka with Kobe; Dallas with Fort Worth, and so
on; 13 shared features). Tower-less pieces of 1 km²+ within 1.5 km of a claimed piece are attached. A city whose
towers stand on no built-up piece (New Alamein City's towers were construction sites in 2021; Bonn's, Chennai's and
a few others' stand by water or in a park) claims the nearest piece within 3 km. Cairo's towers are all in the New
Administrative Capital, bare ground in 2021 and 45 km east of the city, so Cairo claims the piece under an anchor
point in central Cairo instead (ANCHORS in fpbuild.py). The merge fills
water holes under 0.25 km² and smooths outlines to 80 m to keep the file small.

Things to know: the map is a 2021 snapshot, so land built since (Cairo's New Administrative Capital, New Alamein)
is thin or missing. Conurbations are drawn as one shared feature rather than split per city.

## Site

Branch `metro-footprint` in jeffreyljx/SkyscraperMaps: a "Metro footprint" button in the ScraperMap top bar
(icon only below 1600 px; a checkbox in the Filters panel on phones), mauve fill under the basemap's roads and labels,
legend entry, a popup with the area, towers and cities, ESA WorldCover credit in the map attribution, the Method page
and the footer. `?footprint=1` turns it on; the choice is remembered in localStorage (`scrapermap.footprint`).
