import type { TowerIndex, TowerRow } from "./types";

/**
 * Time capsule: the map as it stood in a chosen year. Only completed towers with a known completion year
 * take part; a tower shows from its completion year on. The dataset holds towers standing today, so the only
 * towers that disappear going forward are the lost ones (lib/lostTowers.ts), each gone from the year it came
 * down. The year range runs from the earliest completion year in the data to this year.
 */
export const COMPLETED = "Completed";

export function capsuleRange(idx: TowerIndex, extra: TowerRow[] = []): { first: number; last: number } {
  const done = idx.statuses.indexOf(COMPLETED);
  let first = Infinity, last = -Infinity;
  for (const r of idx.rows.concat(extra)) {
    if (r[7] !== done || r[8] === null) continue;
    if (r[8] < first) first = r[8];
    if (r[8] > last) last = r[8];
  }
  const now = new Date().getFullYear();
  return { first: Number.isFinite(first) ? first : now, last: Math.max(now, Number.isFinite(last) ? last : now) };
}

/**
 * Rows standing in `year`: `rows` must already be completed towers with a year (see the time capsule's base rows);
 * `gone` maps a lost tower's id to the year it came down.
 */
export function standingIn(rows: TowerRow[], year: number, gone?: Map<number, number>): TowerRow[] {
  return rows.filter(r => r[8]! <= year && !((gone?.get(r[0]) ?? Infinity) <= year));
}

/** Rows that came down in `year` (lost towers only). */
export function lostIn(rows: TowerRow[], year: number, gone: Map<number, number>): TowerRow[] {
  return rows.filter(r => gone.get(r[0]) === year);
}

/** Completions per year, first..last inclusive. */
export function perYear(rows: TowerRow[], first: number, last: number): number[] {
  const n = new Array<number>(last - first + 1).fill(0);
  for (const r of rows) { const y = r[8]!; if (y >= first && y <= last) n[y - first]++; }
  return n;
}
