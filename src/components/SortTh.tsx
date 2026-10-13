"use client";
import { useCallback, useEffect, useState } from "react";

/** Sortable table headers shared by the Countries, Cities and Districts tables.
 *  Each sortable column carries a small downward triangle: first click sorts that column most-first (▼),
 *  a second click flips it to least-first (▲). The default view (completed, most first) keeps the URL clean;
 *  any other view is mirrored into ?sort=&order= so it can be linked, alongside other params such as ?min=. */

export type SortDir = "desc" | "asc";
export interface SortState<K extends string> { key: K; dir: SortDir; toggle: (k: K, shown?: K) => void }

export function useSort<K extends string>(keys: readonly K[], initial: K): SortState<K> {
  const [key, setKey] = useState<K>(initial);
  const [dir, setDir] = useState<SortDir>("desc");

  useEffect(() => {
    const q = new URLSearchParams(location.search);
    const k = q.get("sort") as K | null;
    if (k && keys.includes(k)) setKey(k);
    if (q.get("order") === "asc") setDir("asc");
  }, [keys]);

  // `shown` is the column the table is actually sorted by, when it differs from the stored key (a hidden column's fallback).
  const toggle = useCallback((k: K, shown?: K) => {
    const d: SortDir = k === (shown ?? key) && dir === "desc" ? "asc" : "desc";
    setKey(k);
    setDir(d);
    const u = new URL(location.href);
    if (k === initial && d === "desc") { u.searchParams.delete("sort"); u.searchParams.delete("order"); }
    else { u.searchParams.set("sort", k); u.searchParams.set("order", d); }
    history.replaceState(null, "", u.toString());
  }, [key, dir, initial]);

  return { key, dir, toggle };
}

/** Compare two rows by a numeric value in the chosen direction; ties fall back to `tie` (the default ranking order).
 *  Rows without a value (null, e.g. no GDP figure) go to the end in either direction. */
export function sortBy<T>(rows: T[], value: (r: T) => number | null, dir: SortDir, tie: (a: T, b: T) => number): T[] {
  const m = dir === "desc" ? -1 : 1;
  return [...rows].sort((a, b) => {
    const va = value(a), vb = value(b);
    if (va == null || vb == null) return va == null && vb == null ? tie(a, b) : va == null ? 1 : -1;
    return (va - vb) * m || tie(a, b);
  });
}

export function SortTh<K extends string>({ k, label, sort, num = false, title, most = "most", least = "fewest", className }: {
  k: K; label: string; sort: SortState<K>; num?: boolean; title?: string; most?: string; least?: string; className?: string;
}) {
  const active = sort.key === k;
  const next = active && sort.dir === "desc" ? least : most;
  return (
    <th className={[num ? "num" : "", className ?? ""].join(" ").trim() || undefined} aria-sort={active ? (sort.dir === "desc" ? "descending" : "ascending") : "none"}>
      <button type="button" className={"sort" + (active ? " on" : "") + (active && sort.dir === "asc" ? " asc" : "")}
        onClick={() => sort.toggle(k)} aria-label={`Sort by ${label}, ${next} first`} title={(title ? title + " — " : "") + `sort ${next} first`}>
        {label}
        <svg className="tri" width="9" height="6" viewBox="0 0 10 6" aria-hidden="true"><path d="M0 0h10L5 6z" /></svg>
      </button>
    </th>
  );
}
