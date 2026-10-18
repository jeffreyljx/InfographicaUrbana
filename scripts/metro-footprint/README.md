# Metro footprints

`public/metro-footprint.json` is the "Metro footprint" layer: the built-up land around every city on the map, one
multipolygon per metropolitan area, from the ESA WorldCover 2021 land cover map (10 m, class 50 = built-up: buildings,
roads, airports, ports and other paved ground; class 80 = permanent water). Attribution: © ESA WorldCover project 2021,
contains modified Copernicus Sentinel data (2021) processed by the ESA WorldCover consortium, CC BY 4.0.

## The rule (fpbuild.py)

1. The map is read straight from the public S3 copy of WorldCover (3° tiles, windowed reads; no download) and summed
   into cells of 1/2400° (about 46 m, 5×5 pixels). A cell is built-up when at least 5 of its 25 pixels are.
2. An opening of 100 m drops strips narrower than about 200 m (highways, rail lines between fields); a closing of
   350 m bridges gaps up to 700 m (a park, a river, a rail yard between two built-up areas); holes under 0.5 km²
   are filled, so larger parks, fields, reservoirs and airfields' grass stay out.
3. The contiguous pieces that remain are matched with the towers of 150 m+ (the master CSV). A city claims a piece
   that holds at least 3 of its towers, or a tenth of them (so a city with one or two towers claims with one). The
   city's footprint is the pieces it claims; cities that claim the same piece share one feature (Tokyo with Kawasaki,
   Yokohama, Chiba and Saitama; the Pearl River Delta cities; Hong Kong stays separate from Shenzhen, New York from
   Jersey City and Newark). Tower-less pieces of 1 km² and more within 1,500 m of a claimed piece are attached to it
   (across water too). Water cells (at least half water) are cut last.
4. The box around a job's towers starts 20 km wide and grows 25 km per side while a kept piece reaches its edge
   (up to 300 km; a feature cut off by that limit carries `clipped: true`).
5. A city whose towers stand on no sizeable piece (a construction site in 2021, a tower by the shore or in a park)
   claims the nearest piece of 1 km²+ within 3 km of one of its towers. Cairo's towers are all in the New
   Administrative Capital, bare ground in 2021 and 45 km from the city, so it claims the piece under an anchor point
   in central Cairo instead (`ANCHORS` in fpbuild.py).

## Building it

```
export TOWERS_CSV=data_master.csv          # the master tower CSV build_data.py reads
cd scripts/metro-footprint
python3 jobs.py                            # groups cities whose tower boxes (padded 20 km) overlap: jobs.json
python3 runall.py                          # ~1 hour with 3 workers: out/<city>.geojson, .png (check image), .log
python3 merge.py ../../public/metro-footprint.json
```

`merge.py` fills water holes under 0.25 km² (ponds and canals; the basemap draws them over the fill anyway), drops
pieces under 0.25 km², smooths the outline to 80 m and rounds coordinates to 4 decimals, then gives any ground two
jobs both attached to the nearer of the two. Needs numpy, pandas, scipy, shapely, rasterio (GDAL with curl).

Feature properties: `name` (the top three cities), `cities` [{city, towers (inside the footprint), towers_in_city}],
`area_km2`, `pieces`, `clipped`. `src/components/footprintLayer.ts` draws the file.
