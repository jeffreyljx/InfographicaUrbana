// Derives places.json (cities + districts with counts, ranks, tallest, bbox) from towers.json + details.json.
// Same rules as scripts/build_data.py so the two stay interchangeable.
import { readFileSync, writeFileSync } from "node:fs";

export function slugify(s) {
  const a = s.normalize("NFKD").replace(/[^\x00-\x7F]/g, "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/-+/g, "-").replace(/^-|-$/g, "");
  return a || "x";
}
const median = (xs) => { const a = [...xs].sort((p, q) => p - q); const m = a.length >> 1; return a.length % 2 ? a[m] : (a[m - 1] + a[m]) / 2; };
const r5 = (x) => Math.round(x * 1e5) / 1e5, r4 = (x) => Math.round(x * 1e4) / 1e4, r1 = (x) => Math.round(x * 10) / 10;
const sumH = (rows) => rows.reduce((s, r) => s + r[4], 0);

export function derivePlaces(idx, det) {
  const COMPLETED = idx.statuses.indexOf("Completed");
  const country = (id) => det.rows[String(id)][0];
  const agg = (rows) => {
    const comp = rows.filter(r => r[7] === COMPLETED);
    const pool = comp.length ? comp : rows;
    const tallest = pool.reduce((a, b) => (b[4] > a[4] ? b : a));
    const lats = rows.map(r => r[2]), lons = rows.map(r => r[3]);
    return {
      count: rows.length, completed: comp.length, supertall: rows.filter(r => r[4] >= 300).length,
      // Counts at the two higher thresholds: all statuses (count*) and completed only (completed*).
      count200: rows.filter(r => r[4] >= 200).length, completed200: comp.filter(r => r[4] >= 200).length,
      count300: rows.filter(r => r[4] >= 300).length, completed300: comp.filter(r => r[4] >= 300).length,
      // Aggregate skyline height: the heights of the completed towers added up, at each threshold (metres).
      skyline: r1(sumH(comp)), skyline200: r1(sumH(comp.filter(r => r[4] >= 200))), skyline300: r1(sumH(comp.filter(r => r[4] >= 300))),
      tallest_id: tallest[0], tallest_name: tallest[1], tallest_h: tallest[4],
      lat: r5(median(lats)), lon: r5(median(lons)),
      bbox: [r4(Math.min(...lons)), r4(Math.min(...lats)), r4(Math.max(...lons)), r4(Math.max(...lats))],
    };
  };
  const byCity = new Map(), byDist = new Map();
  for (const r of idx.rows) {
    (byCity.get(r[5]) ?? byCity.set(r[5], []).get(r[5])).push(r);
    (byDist.get(r[6]) ?? byDist.set(r[6], []).get(r[6])).push(r);
  }
  const cities = [...byCity.entries()].map(([ci, rows]) => ({
    ...agg(rows), name: idx.cities[ci], slug: slugify(idx.cities[ci]), country: country(rows[0][0]),
    districts: new Set(rows.map(r => r[6])).size,
    districts200: new Set(rows.filter(r => r[4] >= 200).map(r => r[6])).size,
    districts300: new Set(rows.filter(r => r[4] >= 300).map(r => r[6])).size,
  }));
  // Rank at each threshold by completed count, ties broken by name (the rule the site has always used
  // for the 150 m rank). Cities with no completed tower at the threshold get rank 0 (unranked).
  // CitiesTable.tsx sorts with the same rule so the on-page order always matches the rank column.
  const rankBy = (key, field) => {
    const sorted = [...cities].sort((a, b) => b[key] - a[key] || a.name.localeCompare(b.name));
    sorted.forEach((c, i) => { c[field] = c[key] > 0 ? i + 1 : 0; });
  };
  rankBy("completed", "rank"); rankBy("completed200", "rank200"); rankBy("completed300", "rank300");
  // ranked cities first by rank; unranked (pipeline-only) cities after them, by name
  cities.sort((a, b) => (a.rank === 0) - (b.rank === 0) || a.rank - b.rank || a.name.localeCompare(b.name));
  const districts = [...byDist.entries()].map(([di, rows]) => {
    const [ci, dname] = idx.districts[di];
    return { ...agg(rows), name: dname, city: idx.cities[ci], city_slug: slugify(idx.cities[ci]), slug: slugify(dname), country: country(rows[0][0]) };
  });
  districts.sort((a, b) => b.completed - a.completed || b.count - a.count || a.city.localeCompare(b.city) || a.name.localeCompare(b.name));
  districts.forEach((d, i) => { d.rank = i + 1; });
  const seen = new Set();
  for (const d of districts) { const k = d.city_slug + "/" + d.slug; if (seen.has(k)) throw new Error("duplicate district slug " + k); seen.add(k); }
  const totals = {
    towers: idx.rows.length, completed: idx.rows.filter(r => r[7] === COMPLETED).length,
    cities: idx.cities.length, districts: idx.districts.length,
    countries: new Set(idx.rows.map(r => country(r[0]))).size,
    supertall: idx.rows.filter(r => r[4] >= 300).length,
    with_photo: idx.rows.filter(r => r[13]).length,
  };
  return { cities, districts, totals };
}

if (process.argv[1] && process.argv[1].endsWith("derive.mjs")) {
  const idx = JSON.parse(readFileSync("public/data/towers.json")); const det = JSON.parse(readFileSync("public/data/details.json"));
  const places = derivePlaces(idx, det);
  for (const p of ["public/data/places.json", "src/data/places.json"]) writeFileSync(p, JSON.stringify(places));
  console.log(`places: ${places.cities.length} cities, ${places.districts.length} districts`);
}
