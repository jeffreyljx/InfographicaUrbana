import type { Tower, TowerDetail, TowerIndex, TowerRow } from "./types";
import { COMPLETED } from "./timeCapsule";
import data from "./lostTowers.json";

/**
 * Towers of 150 m+ that were completed and have since been demolished or destroyed (the original World Trade
 * Center and others). They are not in the CTBUH dataset of standing towers, so they appear only in the time
 * capsule, from their completion year until the year they came down. Sources: lostTowers.json (each entry
 * carries its own source link); scripts/skyline-years.mjs reads the same file.
 */
export interface LostTower {
  name: string;
  city: string;
  country: string;
  lat: number;
  lng: number;
  /** Where the coordinate comes from. */
  coordSource?: string;
  height: number;
  floors: number | null;
  completed: number;
  /** The first year it no longer stood (for a demolition over several years, the year it began). */
  gone: number;
  how: "destroyed" | "demolished" | "dismantled";
  /** One or two sentences on how it came down, shown after "Demolished in 2019." */
  cause: string;
  use: string;
  ctbuhUrl: string | null;
  sourceUrl: string;
  /** The tower in the dataset that replaced it on the site, if any, and its id. */
  replacedBy: string | null;
  replacedById: number | null;
}
export const LOST_TOWERS = data as LostTower[];
/** Their map ids: well clear of the dataset's ids (CTBUH ids, under 100,000). */
export const LOST_ID0 = 9_000_000;

export interface Lost {
  rows: TowerRow[];
  byId: Map<number, LostTower>;
  /** Map id -> the year it came down. */
  gone: Map<number, number>;
}

/**
 * The lost towers as index rows, so the filters, the map and the counts treat them like any other completed
 * tower. A tower takes its district from the nearest dataset tower in the same city; a city the dataset does
 * not hold gets index -1 (shown, but never matched by a city filter).
 */
export function lostRows(idx: TowerIndex): Lost {
  const done = idx.statuses.indexOf(COMPLETED);
  const building = Math.max(0, idx.precisions.indexOf("building"));
  const rows: TowerRow[] = [], byId = new Map<number, LostTower>(), gone = new Map<number, number>();
  LOST_TOWERS.forEach((t, i) => {
    const id = LOST_ID0 + i + 1, city = idx.cities.indexOf(t.city);
    let district = -1, best = Infinity;
    if (city >= 0) for (const r of idx.rows) {
      if (r[5] !== city) continue;
      const d = (r[2] - t.lat) ** 2 + ((r[3] - t.lng) * Math.cos(t.lat * Math.PI / 180)) ** 2;
      if (d < best) { best = d; district = r[6]; }
    }
    const fn = idx.functions.indexOf(t.use);
    rows.push([id, t.name, t.lat, t.lng, t.height, city, district, done, t.completed, t.floors ?? 0,
      fn >= 0 ? fn : Math.max(0, idx.functions.indexOf("Office")), building, 0, 0]);
    byId.set(id, t); gone.set(id, t.gone);
  });
  return { rows, byId, gone };
}

/** A lost tower resolved for the tower panel; `cityKnown` says whether the site has a page for its city. */
export function resolveLost(idx: TowerIndex, row: TowerRow, t: LostTower): Tower {
  const detail = {
    slug: "", country: t.country, sub_area: null, material: null, address: null, ctbuh_url: t.ctbuhUrl ?? "",
    rank_city: 0, rank_district: 0, rank_global: 0, height_confirmed: true, precision: "", coord_source: null,
    coord_note: t.coordSource ?? null, osm_way: null, photo: null,
  } satisfies TowerDetail;
  return {
    id: row[0], name: t.name, lat: t.lat, lon: t.lng, height: t.height,
    city: t.city, district: row[6] >= 0 ? idx.districts[row[6]][1] : "", status: COMPLETED, year: t.completed,
    floors: t.floors ?? 0, fn: t.use, precision: "building", sharesPoint: 0, hasPhoto: false, detail,
    lost: { completed: t.completed, gone: t.gone, how: t.how, cause: t.cause, source: t.sourceUrl, replacedBy: t.replacedBy, replacedById: t.replacedById, cityKnown: row[5] >= 0 },
  };
}
