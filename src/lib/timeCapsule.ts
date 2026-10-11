import type { TowerIndex, TowerRow } from "./types";

/**
 * Time capsule: the map as it stood in a chosen year. Only completed towers with a known completion year
 * take part (the dataset holds towers standing today, so none disappear going forward); a tower shows from
 * its completion year on. The year range runs from the earliest completion year in the data to this year.
 */
export const COMPLETED = "Completed";

export function capsuleRange(idx: TowerIndex): { first: number; last: number } {
  const done = idx.statuses.indexOf(COMPLETED);
  let first = Infinity, last = -Infinity;
  for (const r of idx.rows) {
    if (r[7] !== done || r[8] === null) continue;
    if (r[8] < first) first = r[8];
    if (r[8] > last) last = r[8];
  }
  const now = new Date().getFullYear();
  return { first: Number.isFinite(first) ? first : now, last: Math.max(now, Number.isFinite(last) ? last : now) };
}

/** Rows standing in `year`: `rows` must already be completed towers with a year (see the time capsule's base rows). */
export function standingIn(rows: TowerRow[], year: number): TowerRow[] {
  return rows.filter(r => r[8]! <= year);
}

/** Completions per year, first..last inclusive. */
export function perYear(rows: TowerRow[], first: number, last: number): number[] {
  const n = new Array<number>(last - first + 1).fill(0);
  for (const r of rows) { const y = r[8]!; if (y >= first && y <= last) n[y - first]++; }
  return n;
}
