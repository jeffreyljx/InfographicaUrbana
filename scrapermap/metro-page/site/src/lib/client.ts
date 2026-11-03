"use client";
import { decodeDetail, type TowerIndex, type TowerRow, type TowerDetail, type DetailsFile, type Tower } from "./types";
import { computeRanks, type Ranks } from "./ranks";

/** Resolve an index row into a Tower on the client (detail may be absent until details.json loads). */
export function resolveRow(idx: TowerIndex, row: TowerRow, det?: TowerDetail): Tower {
  const [id, name, lat, lon, height, city, district, status, year, floors, fn, precision, sharesPoint, hasPhoto] = row;
  return {
    id, name, lat, lon, height,
    city: idx.cities[city], district: idx.districts[district][1], status: idx.statuses[status],
    year, floors, fn: idx.functions[fn], precision: idx.precisions[precision], sharesPoint, hasPhoto: !!hasPhoto,
    detail: det ?? ({} as TowerDetail),
  };
}

let indexPromise: Promise<TowerIndex> | null = null;
let ranks: Ranks | null = null;
export function loadIndex(): Promise<TowerIndex> {
  if (!indexPromise) indexPromise = fetch("/data/towers.json").then(r => r.json()).then((idx: TowerIndex) => { ranks = computeRanks(idx); return idx; });
  return indexPromise;
}
let detailsPromise: Promise<DetailsFile> | null = null;
export function loadDetails(): Promise<DetailsFile> {
  if (!detailsPromise) detailsPromise = fetch("/data/details.json").then(r => r.json());
  return detailsPromise;
}
export function detailFor(df: DetailsFile | null, id: number, name: string): TowerDetail | undefined {
  if (!df || !ranks) return undefined;
  return decodeDetail(id, name, df.rows[String(id)], { global: ranks.global.get(id) ?? 0, city: ranks.city.get(id) ?? 0, district: ranks.district.get(id) ?? 0 });
}

export function norm(s: string): string {
  return s.normalize("NFKD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
}
