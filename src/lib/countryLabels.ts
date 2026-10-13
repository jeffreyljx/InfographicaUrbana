import CFG from "../../scripts/country-labels.json";

/** Country display labels and Countries-table groupings; see scripts/country-labels.mjs (which rewrites the data) and its undo note. */
const cfg = CFG as { labels?: Record<string, string>; merge?: Record<string, string> };
const labels = cfg.labels ?? {}, merge = cfg.merge ?? {};

/** The dataset's own name behind a displayed one ("Taiwan, China" → "Taiwan"). */
export function rawCountry(shown: string): string {
  return Object.keys(labels).find(raw => labels[raw] === shown) ?? shown;
}
/** The Countries-table row a displayed country is counted under ("Taiwan, China" → "China"; others map to themselves). */
export function countryGroup(shown: string): string { return merge[shown] ?? shown; }
/** Dataset names of the countries counted under `group` besides its own ("China" → ["Taiwan"]). */
export function mergedMembers(group: string): string[] {
  return Object.keys(merge).filter(m => merge[m] === group).map(rawCountry);
}
