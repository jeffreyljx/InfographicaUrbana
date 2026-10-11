"use client";
import { useMemo } from "react";
import { cityAt, countsAt, skylineAt, type CityAgg } from "@/lib/types";
import { SortTh, sortBy, useSort } from "@/components/SortTh";
import Rank from "@/components/Rank";
import GdpCell, { type GdpLite } from "@/components/GdpCell";
import { ThresholdSwitch, useThreshold } from "@/components/Threshold";

const KEYS = ["completed", "all", "c200", "c300", "skyline", "core", "gdp", "ppp", "tallest"] as const;
type Key = typeof KEYS[number];

const EVEREST = 8849;   // m
/** Aggregate skyline height in metres; the tooltip gives it in km (and in Everests once it passes one). */
function SkylineCell({ m }: { m: number }) {
  if (!m) return <td className="num muted">—</td>;
  const tip = `${(m / 1000).toFixed(1)} km of towers stacked end to end` + (m >= EVEREST ? `, ${(m / EVEREST).toFixed(1)} times the height of Mount Everest` : "");
  return <td className="num" title={tip}>{Math.round(m).toLocaleString("en-US")}{"\u00a0"}m</td>;
}

/** Cities table with a height-threshold switch (rank by completed towers of ≥150 / ≥200 / ≥300 m) and sortable columns. */
/** `gdp` is keyed by city slug: GDP within city limits (nominal US$ and PPP), null where no figure exists. */
/** `core` is keyed by city slug: the area of the city's skyline extent in km², for the cities that have one. */
export default function CitiesTable({ cities, gdp, core }: { cities: CityAgg[]; gdp: Record<string, GdpLite | null>; core: Record<string, number> }) {
  const [min, pick] = useThreshold();

  const sort = useSort<Key>(KEYS, "completed");
  // A 200 m+ / 300 m+ sort falls back to Completed when the threshold hides that column (it is the same count then).
  const key: Key = (sort.key === "c200" && min >= 200) || (sort.key === "c300" && min >= 300) ? "completed" : sort.key;
  const view = { ...sort, key, toggle: (k: Key) => sort.toggle(k, key) };

  const rows = useMemo(() => {
    const base = cities.map(c => ({ c, ...countsAt(c, min), ...cityAt(c, min) })).filter(r => r.count > 0);
    type Row = typeof base[number];
    // Default order = the precomputed rank (completed desc, then name) so it matches the # column;
    // the unranked pipeline-only cities at the end are ordered by how much they have coming. Also the tie-break for every other sort.
    const rank = (a: Row, b: Row) => b.completed - a.completed || (a.completed === 0 ? b.count - a.count : 0) || a.c.name.localeCompare(b.c.name);
    const value: Record<Key, (r: Row) => number | null> = {
      completed: r => r.completed, all: r => r.count, c200: r => r.c.completed200, c300: r => r.c.completed300, skyline: r => skylineAt(r.c, min), core: r => core[r.c.slug] ?? null,
      gdp: r => gdp[r.c.slug]?.usd ?? null, ppp: r => gdp[r.c.slug]?.ppp ?? null, tallest: r => r.c.tallest_h,
    };
    return sortBy(base, value[key], view.dir, rank);
  }, [cities, gdp, core, min, key, view.dir]);
  const ranked = rows.filter(r => r.completed > 0).length;
  const totalCompleted = rows.reduce((s, r) => s + r.completed, 0);

  return (
    <>
      <ThresholdSwitch min={min} pick={pick} label="Rank by completed towers of at least" />
      <p className="muted" style={{ marginTop: 10 }}>
        {min === 150
          ? `${ranked} cities, ${totalCompleted.toLocaleString()} completed towers of 150 m and taller.` + (rows.length > ranked ? ` ${rows.length - ranked} more have only buildings under construction or topped out; they are listed unranked at the end.` : "")
          : `${ranked} of ${cities.length} cities have a completed building of ${min} m or taller — ${totalCompleted.toLocaleString()} in all.` +
            (rows.length > ranked ? ` ${rows.length - ranked} more have one in the pipeline only; they are listed unranked at the end.` : "")}
      </p>
      <div className="tablewrap"><table>
        <thead><tr>
          <th className="num">#</th><th>City</th><th>Country</th>
          <SortTh k="completed" label="Completed" sort={view} num title={`Completed buildings of ${min} m and taller`} />
          <SortTh k="all" label="All" sort={view} num title={`All buildings of ${min} m and taller, including under construction and topped out`} />
          {min < 200 && <SortTh k="c200" label="200 m+" sort={view} num title="Completed buildings of 200 m and taller" />}
          {min < 300 && <SortTh k="c300" label="300 m+" sort={view} num title="Completed buildings of 300 m and taller" />}
          <SortTh k="skyline" label="Aggregate skyline height" sort={view} num className="wrap" title={`The heights of all completed buildings of ${min} m and taller, added up`} most="highest" least="lowest" />
          <SortTh k="core" label="Skyline size" sort={view} num title="Area of the city's skyline extent, the urban core outlined on the map" most="largest" least="smallest" />
          <SortTh k="gdp" label="GDP" sort={view} num title="GDP within city limits, nominal US$ (latest year; a small tag marks figures older than 2025)" most="largest" least="smallest" />
          <SortTh k="ppp" label="GDP (PPP)" sort={view} num title="GDP within city limits at purchasing-power parity, international $" most="largest" least="smallest" />
          <SortTh k="tallest" label="Tallest" sort={view} title="Tallest completed building" most="tallest" least="shortest" />
        </tr></thead>
        <tbody>{rows.map(({ c, completed, count, rank }) => (
          <tr key={c.slug}>
            <td className="num muted"><Rank rank={rank} /></td>
            <td><a className="place" href={`/city/${c.slug}/`}>{c.name}</a></td>
            <td><span className="place">{c.country}</span></td>
            <td className="num"><b>{completed}</b></td>
            <td className="num muted">{count}</td>
            {min < 200 && <td className="num">{c.completed200 || "—"}</td>}
            {min < 300 && <td className="num">{c.completed300 || "—"}</td>}
            <SkylineCell m={skylineAt(c, min)} />
            {c.slug in core ? <td className="num">{core[c.slug].toFixed(2)}{"\u00a0"}km²</td> : <td className="num muted">—</td>}
            <GdpCell g={gdp[c.slug]} kind="usd" />
            <GdpCell g={gdp[c.slug]} kind="ppp" />
            <td>{c.tallest_name} <span className="muted">{c.tallest_h}{"\u00a0"}m</span></td>
          </tr>))}
        </tbody></table></div>
      <p className="muted" style={{ marginTop: 18 }}>Completed, 200 m+ and 300 m+ count finished buildings; All adds those under construction or topped out. GDP is the economic output within the city's own limits (not its metro area) for 2025 or the latest year published — hover a figure for its year and source. Where nothing is published for the city itself, the figure is for the smallest official area that contains it — a county, a district or the metro area, never anything larger — and is marked †; hovering names the area and the city&apos;s share of its population, so these figures overstate the city itself. A dash means no figure exists at that scale. Nominal GDP is converted to US$ at that year's average exchange rate, GDP (PPP) at the IMF's purchasing-power-parity conversion rate. Aggregate skyline height adds up the heights of the city&apos;s completed buildings at the selected height, as if every tower were stacked end to end; hover a figure for it in kilometres. Skyline size is the area of the city&apos;s skyline extent, the urban core outlined on the map when Display skyline extent is on, measured from that outline on the WGS84 ellipsoid; it is given for the {Object.keys(core).length} cities that have one, and the others show a dash. Tallest is the tallest completed building in the city. Click a column&apos;s ▼ to sort by it, most first; click again for least first. The # column always shows the city&apos;s rank by completed towers.</p>
    </>
  );
}
