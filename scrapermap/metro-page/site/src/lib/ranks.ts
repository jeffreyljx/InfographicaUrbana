import type { TowerIndex } from "./types";

export interface Ranks { global: Map<number, number>; city: Map<number, number>; district: Map<number, number> }

/** Height ranks with ties sharing the lower rank (pandas rank(method="min")), over all statuses. */
export function computeRanks(idx: TowerIndex): Ranks {
  const rankWithin = (key: (r: TowerIndex["rows"][number]) => number | string) => {
    const groups = new Map<number | string, TowerIndex["rows"]>();
    for (const r of idx.rows) { const k = key(r); (groups.get(k) ?? groups.set(k, []).get(k)!).push(r); }
    const out = new Map<number, number>();
    for (const rows of groups.values()) {
      const sorted = [...rows].sort((a, b) => b[4] - a[4]);
      let rank = 0;
      sorted.forEach((r, i) => { if (i === 0 || r[4] !== sorted[i - 1][4]) rank = i + 1; out.set(r[0], rank); });
    }
    return out;
  };
  return { global: rankWithin(() => 0), city: rankWithin(r => r[5]), district: rankWithin(r => r[6]) };
}
