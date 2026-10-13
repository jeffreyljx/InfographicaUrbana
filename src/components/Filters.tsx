"use client";
import { useMemo } from "react";
import type { TowerIndex, TowerRow } from "@/lib/types";
import places from "@/data/places.json";
import type { Places } from "@/lib/types";

const PLACES = places as unknown as Places;

export interface FilterState {
  statuses: Set<number>;        // indices into idx.statuses
  minHeight: number;
  yearFrom: number | null;
  yearTo: number | null;
  fnGroup: "all" | "residential" | "office" | "hotel" | "mixed";
  showApproximate: boolean;
  city: string | null;
  district: string | null;
}

export const DEFAULT_FILTERS: FilterState = {
  statuses: new Set([0]),
  minHeight: 150,
  yearFrom: null,
  yearTo: null,
  fnGroup: "all",
  showApproximate: false,
  city: null,
  district: null,
};

function fnGroupOf(fn: string): FilterState["fnGroup"] {
  const parts = fn.split("/").map(s => s.trim().toLowerCase()).filter(Boolean);
  if (parts.length > 1) return "mixed";
  const p = parts[0] ?? "";
  if (p.includes("residential") || p.includes("apartment")) return "residential";
  if (p.includes("office")) return "office";
  if (p.includes("hotel")) return "hotel";
  return "mixed";
}

export function applyFilters(idx: TowerIndex, f: FilterState): TowerRow[] {
  const ci = f.city ? idx.cities.indexOf(f.city) : -1;
  const di = f.district && ci >= 0 ? idx.districts.findIndex(d => d[0] === ci && d[1] === f.district) : -1;
  const fnGroups = idx.functions.map(fnGroupOf);
  const approxIdx = idx.precisions.indexOf("approximate");
  return idx.rows.filter(r => {
    if (!f.statuses.has(r[7])) return false;
    if (r[4] < f.minHeight) return false;
    if (f.yearFrom !== null && (r[8] === null || r[8] < f.yearFrom)) return false;
    if (f.yearTo !== null && (r[8] === null || r[8] > f.yearTo)) return false;
    if (f.fnGroup !== "all" && fnGroups[r[10]] !== f.fnGroup) return false;
    if (!f.showApproximate && r[11] === approxIdx) return false;
    if (ci >= 0 && r[5] !== ci) return false;
    if (di >= 0 && r[6] !== di) return false;
    return true;
  });
}

interface Props {
  idx: TowerIndex;
  state: FilterState;
  onChange: (s: FilterState) => void;
  onClose: () => void;
  shown: number;
  onFlyTo: (bbox: [number, number, number, number]) => void;
}

export default function Filters({ idx, state, onChange, onClose, shown, onFlyTo }: Props) {
  const set = (patch: Partial<FilterState>) => onChange({ ...state, ...patch });
  const toggleStatus = (i: number) => {
    const s = new Set(state.statuses); if (s.has(i)) s.delete(i); else s.add(i);
    if (s.size === 0) s.add(0);
    set({ statuses: s });
  };
  const districts = useMemo(() => state.city ? PLACES.districts.filter(d => d.city === state.city) : [], [state.city]);
  const cityAgg = state.city ? PLACES.cities.find(c => c.name === state.city) : null;

  return (
    <aside className="filters" role="dialog" aria-label="Filters">
      <div className="filters-head">
        <strong>Filters</strong>
        <span className="muted">{shown.toLocaleString()} of {idx.rows.length.toLocaleString()} towers</span>
        <button className="x" onClick={onClose} aria-label="Close filters">×</button>
      </div>

      <label className="lbl">Status</label>
      <div className="chips">
        {idx.statuses.map((s, i) => (
          <button key={s} className={"chip" + (state.statuses.has(i) ? " on" : "")} onClick={() => toggleStatus(i)}>{s}</button>
        ))}
      </div>

      <label className="lbl">Minimum height <span className="muted">{state.minHeight} m</span></label>
      <input type="range" min={150} max={500} step={10} value={state.minHeight} onChange={e => set({ minHeight: Number(e.target.value) })} />

      <label className="lbl">Completed between</label>
      <div className="row">
        <input type="number" placeholder="from" min={1900} max={2035} value={state.yearFrom ?? ""} onChange={e => set({ yearFrom: e.target.value ? Number(e.target.value) : null })} />
        <input type="number" placeholder="to" min={1900} max={2035} value={state.yearTo ?? ""} onChange={e => set({ yearTo: e.target.value ? Number(e.target.value) : null })} />
      </div>

      <label className="lbl">Use</label>
      <div className="chips">
        {(["all", "residential", "office", "hotel", "mixed"] as const).map(g => (
          <button key={g} className={"chip" + (state.fnGroup === g ? " on" : "")} onClick={() => set({ fnGroup: g })}>{g[0].toUpperCase() + g.slice(1)}</button>
        ))}
      </div>

      <label className="lbl">City</label>
      <select value={state.city ?? ""} onChange={e => { const c = e.target.value || null; set({ city: c, district: null }); const agg = PLACES.cities.find(x => x.name === c); if (agg) onFlyTo(agg.bbox); }}>
        <option value="">All {PLACES.cities.length} cities</option>
        {PLACES.cities.map(c => <option key={c.name} value={c.name}>{c.name} ({c.completed})</option>)}
      </select>
      {state.city && (
        <>
          <label className="lbl">District in {state.city}</label>
          <select value={state.district ?? ""} onChange={e => { const d = e.target.value || null; set({ district: d }); const agg = districts.find(x => x.name === d); if (agg) onFlyTo(agg.bbox); else if (cityAgg) onFlyTo(cityAgg.bbox); }}>
            <option value="">All {districts.length} districts</option>
            {districts.map(d => <option key={d.name} value={d.name}>{d.name} ({d.completed})</option>)}
          </select>
        </>
      )}

      <label className="check">
        <input type="checkbox" checked={state.showApproximate} onChange={e => set({ showApproximate: e.target.checked })} />
        Show approximately-located towers <span className="muted">(78, street level only)</span>
      </label>

      <button className="link" onClick={() => onChange({ ...DEFAULT_FILTERS })}>Reset</button>
    </aside>
  );
}
