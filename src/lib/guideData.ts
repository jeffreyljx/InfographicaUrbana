import "server-only";
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { getIndex, getPlaces } from "./data";
import { LOST_TOWERS } from "./lostTowers";
import { COMPLETED } from "./timeCapsule";
import { decode, type Raw } from "./metro";
import { FIRST_YEAR, LAST_YEAR, yearToPos, fmtYear } from "./history";

/**
 * The figures the modes' guides quote and chart, read from the same data the maps load, so the guides stay true when the
 * data changes. Each time-dock chart is computed the way its dock computes it (TimeCapsule, MetroYears, HistoryYears).
 */

export interface Series { first: number; last: number; values: number[]; peak: { year: number; v: number } }
const peakOf = (first: number, values: number[]) => {
  let i = 0;
  values.forEach((v, k) => { if (v > values[i]) i = k; });
  return { year: first + i, v: values[i] ?? 0 };
};

/** ScraperMap's time capsule with no filters on: completed towers with a known year (approximate pins are off by
 *  default), plus the lost towers, counted by completion year. */
export function scraperGuide() {
  const idx = getIndex(), { totals } = getPlaces();
  const done = idx.statuses.indexOf(COMPLETED), approx = idx.precisions.indexOf("approximate");
  const years = idx.rows.filter(r => r[7] === done && r[8] !== null && r[11] !== approx).map(r => r[8] as number)
    .concat(LOST_TOWERS.map(t => t.completed));
  const first = Math.min(...years), last = Math.max(new Date().getFullYear(), ...years);
  const values = new Array<number>(last - first + 1).fill(0);
  for (const y of years) values[y - first]++;
  const series: Series = { first, last, values, peak: peakOf(first, values) };
  return { totals, lost: LOST_TOWERS.length, counted: years.length, series };
}

/** TransitMap's year dock for the whole world: km of line opened each year, less closures. */
export function transitGuide() {
  const raw = JSON.parse(readFileSync(join(process.cwd(), "public/metro/metro.json"), "utf8")) as Raw;
  const d = decode(raw);
  const series: Series = { first: d.first, last: d.last, values: d.kmPerYear, peak: peakOf(d.first, d.kmPerYear) };
  const open = d.lines.filter(l => l.closeYear > d.last);
  return {
    systems: d.systems.length, cities: new Set(d.systems.map(s => s.city)).size, lines: d.lines.length,
    stations: d.stations.length, km: d.kmPerYear.reduce((a, b) => a + b, 0), openLines: open.length, series,
  };
}

/** CartaHistoria's year dock: land that changed owner or status, summed into the dock's 320 bars (each a stretch of
 *  years, wider before 1500 since the slider runs slower there). Cells are hexagons of `cellKm2` each. */
export const HISTORY_BINS = 320;
export function historyGuide() {
  const dir = join(process.cwd(), "public/history");
  const idx = JSON.parse(readFileSync(join(dir, "index.json"), "utf8")) as { changed: number[]; cellKm2: number; built: string };
  const st = JSON.parse(readFileSync(join(dir, "states.json"), "utf8")) as { slug: (string | null)[] };
  const binOf = (y: number) => Math.min(HISTORY_BINS - 1, Math.floor(yearToPos(y) * HISTORY_BINS));
  const cells = new Array<number>(HISTORY_BINS).fill(0), from = new Array<number>(HISTORY_BINS).fill(LAST_YEAR), to = new Array<number>(HISTORY_BINS).fill(FIRST_YEAR);
  for (let y = FIRST_YEAR; y <= LAST_YEAR; y++) { const b = binOf(y); from[b] = Math.min(from[b], y); to[b] = Math.max(to[b], y); }
  idx.changed.forEach((c, i) => { cells[binOf(FIRST_YEAR + i)] += c; });
  const years = (b: number) => from[b] === to[b] ? fmtYear(from[b], true)
    : to[b] < 0 ? `${-from[b]}–${-to[b]} BCE` : from[b] < 0 ? `${-from[b]} BCE–${to[b]} CE` : to[b] < 1000 ? `${from[b]}–${to[b]} CE` : `${from[b]}–${to[b]}`;
  const order = cells.map((c, b) => b).sort((a, b) => cells[b] - cells[a]);
  return {
    states: st.slug.filter(Boolean).length, cellKm2: idx.cellKm2, built: idx.built,
    bins: cells.map((c, b) => ({ x: b / HISTORY_BINS, w: 1 / HISTORY_BINS, v: c })),
    top: order.slice(0, 3).map(b => ({ years: years(b), cells: cells[b] })),
  };
}
