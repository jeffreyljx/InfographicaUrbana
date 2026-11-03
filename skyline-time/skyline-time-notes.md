# Skyline extents through time

Part of the time capsule. When the year slider is set, each city's "Display skyline extent" core shrinks back to the area around the towers that stood in that year. It is built on the slider's patch (no second slider) and uses the slider's rule for which towers stand.

Status: live on https://scrapermap.vercel.app since 11 Oct 2026 19:35 UTC (production `dpl_3PPzyGfHqTHkDDykHCW45A6uiTFn`, with the time capsule and the map-scale ruler). The preview was `dpl_5aZ6RYQw6cfhGHiMPYDTs4bwooNh`.

## Files

- `skyline-years.patch`: one commit (`git am`), applied on top of, in order, `skyline-extent/skyline-extent-site-changes.patch`, `scrapermap/patches/tower-icons.patch`, `scrapermap/patches/skyline-size.patch` and `scrapermap/patches/time-capsule.patch`. It adds:
  - `scripts/skyline-years.mjs`, which does the work.
  - A call from `scripts/prebuild.mjs`.
  - `jsts` 2.12.1 as a build-time devDependency (in `package.json` and `deploy/package.json`). It is not shipped to the browser.
  - The map side, in `src/components/skylineLayer.ts` and `MapApp.tsx`: the years file loads lazily, is filtered by the slider year, and the popup shows the year.
- The per-year file `public/skyline-extent-years.geojson` is **not committed**. It is made at build time, so a revised cores file (`public/skyline-extent.geojson` in the repo, copied from `skyline-extent/skyline-extent.geojson`) or new tower data is picked up on the next build without anyone re-running anything. The step stores a hash of its inputs in the output and skips itself when nothing changed, so the second prebuild on Vercel costs nothing. If one city fails, the build carries on and that city shows its drawn core for every year (with a warning in the build log).

## Rule

A tower stands in year Y if it is completed with a completion year of Y or earlier. This is the slider's rule. Completed towers with no year are left out, and the dataset has no demolitions. Only towers inside a city's core count.

1. Each standing tower claims the core within **R = 400 m** of it.
2. The rest of the core (parks, low-rise blocks, waterfront) is cut into **150 m** squares. A square joins once its **4 nearest towers** stand, along with any other tower within 300 m of the nearest one's distance. It also has to touch the extent already drawn, so gaps fill in from the edges of the built-up area and never appear as islands.
3. The result is closed by **300 m** (grown, then shrunk) so close towers read as one district. It is then clipped to the core, so an extent never goes past today's line.
4. **Cutoff: a city has no extent until 5 of its core's towers stand.**

So an extent only grows with time. From the year of the core's latest tower onwards it is exactly the drawn core. Run `SKYLINE_YEARS_REPORT=1 node scripts/skyline-years.mjs` for the table below.

Known behaviour:
- Cities whose core was drawn generously around a few late towers jump near the end, when those towers complete. Examples: Moscow (only 9 frames, shown from 2010), Shenzhen, Wuhan.
- Old low-rise downtowns inside a core (Moscow Garden Ring, South Mumbai, Seoul Jongno) fill only when nearby towers stand. That follows the rule, not the history of the district.

## Per city (live 9 Oct cores, 38 cities)

`towers` = completed towers with a year inside the core. `shown from` = the first year with 5 standing. The last column checks that the final frame matches the drawn core.

```
  city            towers  first  shown from  keyframes  computed/drawn core at the end
  Hong Kong          190   1973        1981         37  1.000
  Shenzhen           310   1985        1996         30  1.000
  New York City      319   1909        1915         75  1.000
  Dubai              244   1999        2001         26  1.000
  Guangzhou          137   1990        1996         29  1.000
  Kuala Lumpur       120   1983        1985         32  1.000
  Wuhan              138   1996        1997         22  1.000
  Shanghai           149   1988        1996         28  1.000
  Tokyo              137   1968        1976         37  1.000
  Chongqing           81   1998        2002         21  1.000
  Toronto             96   1967        1975         26  1.000
  Chengdu             90   1994        2007         15  1.000
  Chicago            135   1924        1929         50  1.000
  Metro Manila       109   1992        1997         26  1.000
  Bangkok             99   1987        1996         25  1.000
  Mumbai              71   1970        2010         16  1.000
  Jakarta             78   1996        2003         18  1.000
  Seoul               41   1985        1998         18  1.000
  Hangzhou            67   2003        2009         17  1.000
  Singapore           82   1975        1980         35  1.000
  Miami               68   1973        1997         17  1.000
  Changsha            54   1984        2014         12  1.000
  Nanjing             60   1998        2003         21  1.000
  Nanning             51   2008        2014         10  0.999
  Melbourne           77   1972        1978         23  1.000
  Busan               51   1997        2005         10  0.999
  Shenyang            65   2009        2011         10  1.000
  Moscow              24   1952        2010          9  1.000
  Beijing             30   1989        2006         12  1.000
  Tianjin             42   1997        1999         16  1.000
  Panama City         63   1996        2002         16  0.999
  Sydney              43   1967        1988         25  0.999
  Zhuhai              39   2014        2014          9  0.999
  Suzhou              18   2010        2015          8  0.999
  Istanbul            35   1993        2010         12  0.999
  Doha                43   2002        2009         13  1.000
  Dalian              48   1996        2000         14  1.000
  Osaka               38   1986        1992         21  1.000
```

## Revised cores (75 cities, not yet approved)

I ran the step against `skyline-extent/skyline-extent.geojson` as it stood at 07:45 on 11 Oct (sha1 b4ed9d4b…, DBSCAN 800 m / min 4). Result: 75 cities and 1,108 keyframes, with no failures. The new small clusters (London, Paris La Défense, Frankfurt, downtown LA, Boston) shrink sensibly. Nothing needs re-running when those cores land in the repo, because the build does it.

## Deploying

The preview used the production bundle and data parts by SHA, plus a new `bundle/delta.tar.br.part00–03` (sha1 d3977b3b…, 7153c77c…, d8b429d7…, 7c33831f…; 22000/22000/22000/10097 bytes). The delta holds every source file changed since the 3 Oct snapshot (all five patches above), so it needs no `overlay/` dir. The root `package.json` is sent inline with jsts. See `knowledge/claude/scrapermap-deploy-notes.md`.

Production was built the same way with `map-scale.patch` added last and a rebuilt delta (sha1 cd899146…, 03410031…, 4577a9f3…, 869d2cbb…; 22000/22000/22000/10263 bytes). Any later build carries what is live plus only what Jeffrey has approved, and checks production has not changed right before deploying.
