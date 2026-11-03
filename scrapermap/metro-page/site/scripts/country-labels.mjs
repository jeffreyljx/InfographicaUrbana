// Country display labels and groupings, applied once at build time (scripts/prebuild.mjs) to the served data.
//   labels: the dataset's own country name -> the name the site shows ("Taiwan" -> "Taiwan, China"). Rewritten in
//           details.json, places.json, and so on every tower, city, district page, panel and JSON-LD.
//   merge:  a displayed country -> the row it is counted under in the Countries table ("Taiwan, China" -> "China"),
//           the same way Hong Kong and Macau already count under China. Tower and city pages keep the label above.
// GDP is joined through the same config (src/lib/gdp.ts adds a merged country's GDP to its group's).
//
// TO UNDO: set scripts/country-labels.json to {"labels": {}, "merge": {}} and rebuild (npm run prebuild unpacks fresh
// data from data/data.br.part*). Drop just the "merge" entry to keep the label but give Taiwan its own Countries row again.
import { readFileSync, writeFileSync, existsSync } from "node:fs";

const CFG = JSON.parse(readFileSync(new URL("./country-labels.json", import.meta.url), "utf8"));
export const LABELS = CFG.labels ?? {};
export const MERGE = CFG.merge ?? {};
export const label = (c) => LABELS[c] ?? c;
export const group = (c) => MERGE[c] ?? c;
export const active = () => Object.keys(LABELS).length + Object.keys(MERGE).length > 0;

/** Rewrites the country strings in details.json (each row's first element) and places.json (cities + districts) in the given dirs,
 *  and recounts places.totals.countries after merging. Idempotent. Returns how many strings changed. */
export function applyCountryLabels(dirs = ["public/data", "src/data"]) {
  if (!active()) return 0;
  let n = 0;
  for (const dir of dirs) {
    const dp = `${dir}/details.json`, pp = `${dir}/places.json`;
    if (existsSync(dp)) {
      // Textual rewrite of each row's leading country string, so the file's row order and bytes are otherwise untouched
      // (JSON.parse/stringify would renumber the integer keys) and scripts/pack-data.mjs can reverse it exactly.
      let text = readFileSync(dp, "utf8");
      for (const [raw, shown] of Object.entries(LABELS)) {
        text = text.replace(new RegExp(`(":\\[)${JSON.stringify(raw)},`, "g"), (_, pre) => { n++; return `${pre}${JSON.stringify(shown)},`; });
      }
      writeFileSync(dp, text);
    }
    if (existsSync(pp)) {
      const pl = JSON.parse(readFileSync(pp, "utf8"));
      for (const p of [...pl.cities, ...pl.districts]) { const l = label(p.country); if (l !== p.country) { p.country = l; n++; } }
      // every city has a tower, so the countries counted in the Countries table are the groups of the cities' countries
      pl.totals.countries = new Set(pl.cities.map(c => group(c.country))).size;
      writeFileSync(pp, JSON.stringify(pl));
    }
  }
  return n;
}
