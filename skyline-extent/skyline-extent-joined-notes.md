# Skyline extents with almost-touching skylines joined

**Status:** live since 12 Oct 2026 19:07 UTC in production dpl_5UwoR4xYrrysTeC8DFpu3XpSypYW, together with the Skylines comparison page (Jeffrey's Go live 18:53 UTC); the site serves `skyline-extent-joined.geojson` (md5 811f2e119a43eb23747d472d4300a9bf) as `public/skyline-extent.geojson` via `scrapermap/patches/skyline-joined.patch`. `skyline-extent.geojson` (md5 cf6700ea05a3654f87ddc7893527a36d) is the unjoined density-rule file it replaced, live 12 Oct 05:44:57 to 19:07 UTC.

## What Jeffrey asked

> "Also, for skylines that are ALMOST connected but are severed, just connect them for ease of calculations/display (e.g. the Shekou vs Nanshan Tech Park vs QIanhai seperation, the Tianhe-Pazhou separation, or the Shenzhen Bay-Xiangmihu separation)" (12 Oct 2026, 16:52 UTC)

## The rule

Two outline pieces of the same city are joined when you can get from one to the other in steps of at most **1.9 km** between towers of 150 m+ (any status, in a pocket or not) and outline edges, with no step crossing more than **600 m of water**.

- **Why 1.9 km.** It is the smallest round number that covers all three of Jeffrey's examples. Shekou to Nanshan is 0.4 km and Nanshan to Qianhai is 1.24 km. Shenzhen Bay to Xiangmihu has no shorter route than one whose longest step is 1.8 km, from Jindi Century at OCT to the Antosan Headquarters towers. Just above 1.9 km come joins that read as separate places: Nanjing's Hexi CBD and Jiangdong at 1.91 km, Pok Fu Lam over the hill to Hong Kong Island's north shore at 1.94 km, Moscow City and Savyolovsky at 1.99 km, and Yeouido and Mokdong at 2.06 km.
- **Why 600 m of water.** Rivers this narrow join the skylines on their two banks:
  - the Pearl River between Tianhe and Pazhou (0.36 km);
  - the Huangpu at Lujiazui (0.36 km);
  - the Jialing at Jiangbeizui (0.34 km);
  - the Chao Phraya at Iconsiam;
  - the East River between Midtown and Long Island City (0.52 km).

  Wider water keeps skylines apart:
  - Victoria Harbour between Wan Chai and Hung Hom (0.94 km);
  - the Han at Samseong (0.77 km);
  - the Yangtze at Chongqing's Nan'an (0.64 to 0.76 km);
  - Sharjah's Khalid Lagoon (0.70 km).
- **The bridge.** The links used are the minimum spanning tree's, which gives every pair of pieces the route with the shortest longest step. Each link becomes a band: the hull of the outline within 300 m of each end of the step, or 300 m around a tower. A band over land is cut back from water. A band whose step crosses a river covers that stretch of the river. Corners where a band meets an outline are rounded by 300 m without spilling into water. Stray towers on a route are taken in with 300 m around them, so they count as inside.
- **Pieces of one pocket that water cut apart** (Dubai's canal and marina, the canals at Tokyo's Tsukishima, Melbourne's Yarra, the Moskva at Moscow City, London, Manama, Rotterdam) are joined across it by the same rule.
- **Kept as before:** the pockets (5+ towers, DBSCAN 800 m / 4), their names (`areas`, one per pocket, largest first, as the Skylines page expects), the property set, and 91 of the 128 cities, which come out exactly as in `skyline-extent.geojson`. The popup rationale of a joined city gains one sentence. An example: "Skylines that almost touch are joined (towers up to 1.9 km apart, rivers up to 600 m wide), so the 19 pockets here make three skylines."
- **Shenzhen's note** changed, because its old one said the band between Futian and Nanshan had too few towers to join them. It now reads: "Nanshan and Futian join through Jindi Century at Overseas Chinese Town and the Antosan Headquarters towers on the way to Xiangmihu."

## Totals

- Skylines, counted as the Skylines page counts them: 263 before, 209 after.
- Area: 710.1 km² before, 758.1 km² after.
- Towers of 150 m+ inside: 5,911 before, 5,953 after, because stray towers on the bridges are now inside.

Jeffrey's three examples:

- **Shenzhen.** Shekou, Nanshan, Shenzhen Bay Super Headquarters, Qianhai, Bao'an, Xili, OCT and all of Futian, Luohu and Meilin are now one skyline. Longhua and Taoyuan make a second, and Pingshan stands alone. That is 11 skylines down to 3, and 66.4 km² up to 73.8 km².
- **Guangzhou.** Tianhe, Pazhou, Pazhou west, International Financial City, Haizhu Xingang and Yuexiu are now one skyline. Panyu and Zengcheng stand alone.

## The lever

`STEP` at the top of `tools/build_joined.py`. At 1.25 km, 29 cities change instead of 37. Shekou, Qianhai and Tianhe-Pazhou still join, but Shenzhen Bay and Xiangmihu stay apart, as do Tokyo's West Shinjuku, Kuala Lumpur's Mont Kiara and Metro Manila's Eastwood. `WATER` sets the widest river a step may cross.

## Cities that change

Pieces are the outline's separate shapes. Skylines counts pieces that share a pocket as one, as the Skylines page does.

| City | Pieces | Skylines | Area km² | Towers inside |
|---|---|---|---|---|
| Hong Kong | 13 → 9 | 13 → 9 | 42.96 → 45.00 | 540 → 541 |
| Shenzhen | 12 → 3 | 11 → 3 | 66.37 → 73.81 | 467 → 469 |
| New York City | 4 → 3 | 4 → 3 | 17.51 → 18.29 | 325 → 325 |
| Dubai | 6 → 3 | 3 → 3 | 23.19 → 23.47 | 300 → 300 |
| Guangzhou | 8 → 3 | 8 → 3 | 21.24 → 25.09 | 168 → 177 |
| Kuala Lumpur | 5 → 1 | 5 → 1 | 18.33 → 23.88 | 164 → 175 |
| Wuhan | 7 → 4 | 7 → 4 | 33.55 → 35.59 | 176 → 177 |
| Shanghai | 4 → 2 | 3 → 2 | 25.36 → 27.40 | 162 → 163 |
| Tokyo | 5 → 2 | 3 → 2 | 26.33 → 27.68 | 163 → 163 |
| Chongqing | 5 → 2 | 5 → 2 | 10.62 → 12.29 | 97 → 98 |
| Toronto | 5 → 4 | 5 → 4 | 11.86 → 13.74 | 141 → 142 |
| Chengdu | 4 → 3 | 4 → 3 | 14.05 → 14.88 | 104 → 104 |
| Metro Manila | 2 → 1 | 2 → 1 | 16.53 → 17.59 | 124 → 124 |
| Bangkok | 2 → 1 | 1 → 1 | 18.72 → 18.84 | 100 → 100 |
| Jakarta | 3 → 2 | 3 → 2 | 13.07 → 13.92 | 101 → 101 |
| Seoul | 10 → 7 | 10 → 7 | 8.59 → 10.77 | 80 → 80 |
| Changsha | 6 → 4 | 6 → 4 | 13.97 → 14.97 | 77 → 77 |
| Nanning | 5 → 4 | 5 → 4 | 6.23 → 7.14 | 61 → 61 |
| Melbourne | 2 → 1 | 1 → 1 | 4.99 → 5.03 | 79 → 79 |
| Busan | 3 → 2 | 3 → 2 | 6.16 → 7.11 | 56 → 59 |
| Moscow | 3 → 2 | 2 → 2 | 2.77 → 2.86 | 28 → 28 |
| Tianjin | 5 → 2 | 3 → 2 | 9.12 → 9.43 | 55 → 55 |
| London | 4 → 3 | 3 → 3 | 4.03 → 4.18 | 43 → 43 |
| Tel Aviv | 2 → 1 | 2 → 1 | 4.71 → 5.44 | 41 → 41 |
| Jinan | 2 → 1 | 2 → 1 | 5.66 → 5.93 | 36 → 36 |
| Abu Dhabi | 4 → 1 | 3 → 1 | 7.70 → 10.42 | 41 → 43 |
| Xiamen | 3 → 2 | 3 → 2 | 3.65 → 4.48 | 21 → 22 |
| Macau | 3 → 2 | 3 → 2 | 3.38 → 4.99 | 25 → 29 |
| Wuxi | 2 → 1 | 2 → 1 | 2.64 → 3.81 | 17 → 19 |
| Dongguan | 2 → 1 | 2 → 1 | 2.21 → 2.32 | 16 → 16 |
| Ningbo | 5 → 3 | 3 → 3 | 5.05 → 5.18 | 24 → 24 |
| Jersey City | 2 → 1 | 2 → 1 | 2.62 → 3.47 | 24 → 24 |
| Sharjah | 2 → 1 | 2 → 1 | 3.01 → 3.55 | 16 → 16 |
| Atlanta | 2 → 1 | 2 → 1 | 2.28 → 2.98 | 13 → 15 |
| Manama | 3 → 1 | 1 → 1 | 1.50 → 1.68 | 10 → 10 |
| Gold Coast | 2 → 1 | 2 → 1 | 2.89 → 3.50 | 16 → 17 |
| Rotterdam | 2 → 1 | 1 → 1 | 1.28 → 1.44 | 9 → 9 |

Check images: `joined-check.png` (Jeffrey's examples plus Hong Kong, Shanghai, Tokyo, Kuala Lumpur and New York) and `joined-cities.png` (all 37 cities). Both show joined in gold over the live extents in dashed blue.

## Rebuild and use

- **Build.** From `tools/`, run `python3 build_joined.py ../skyline-extent-joined.geojson`. It imports `build_density.py` unchanged, so the same folder also rebuilds the live file. It needs pandas, shapely 2, scikit-learn and scipy. `lib.geo.load()` leaves a `geo_cache.pkl` next to `geo_all.json`; delete it afterwards.
- **Site.** Copy the file to `public/skyline-extent.geojson`. The Skyline size column, the popups, the time capsule's `scripts/skyline-years.mjs` and the /skylines page all read that file at build time, and none needs a code change. The Skylines page already shows pockets that share an outline as one skyline under all their names.
