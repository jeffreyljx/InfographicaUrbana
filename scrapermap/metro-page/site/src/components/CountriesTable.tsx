"use client";
import { useMemo } from "react";
import type { Threshold } from "@/lib/types";
import { SortTh, sortBy, useSort } from "@/components/SortTh";
import Rank from "@/components/Rank";
import GdpCell, { type GdpLite } from "@/components/GdpCell";
import { ThresholdSwitch, useThreshold } from "@/components/Threshold";

/** One country, with counts at each height threshold (built on the server from the city aggregates). */
export interface CountryRow {
  name: string;
  completed: number; count: number; completed200: number; count200: number; completed300: number; count300: number;
  cities: number; cities200: number; cities300: number;       // cities with any building at that height (all statuses)
  districts: number; districts200: number; districts300: number;
  top: { 150: TopCity | null; 200: TopCity | null; 300: TopCity | null };   // city with the most completed at that height
  tallest_name: string; tallest_h: number; tallest_city: string; tallest_slug: string;
  gdp: GdpLite | null;                                        // national GDP, nominal US$ and PPP
}
export interface TopCity { name: string; slug: string; completed: number }

const KEYS = ["completed", "all", "c200", "c300", "cities", "gdp", "ppp", "tallest"] as const;
type Key = typeof KEYS[number];

const at = (r: CountryRow, m: Threshold) => m === 300
  ? { completed: r.completed300, count: r.count300, cities: r.cities300, districts: r.districts300 }
  : m === 200 ? { completed: r.completed200, count: r.count200, cities: r.cities200, districts: r.districts200 }
  : { completed: r.completed, count: r.count, cities: r.cities, districts: r.districts };

export default function CountriesTable({ countries }: { countries: CountryRow[] }) {
  const [min, pick] = useThreshold();
  const sort = useSort<Key>(KEYS, "completed");
  const key: Key = (sort.key === "c200" && min >= 200) || (sort.key === "c300" && min >= 300) ? "completed" : sort.key;
  const view = { ...sort, key, toggle: (k: Key) => sort.toggle(k, key) };

  const { rows, ranked } = useMemo(() => {
    const base = countries.map(c => ({ c, ...at(c, min) })).filter(r => r.count > 0);
    type Row = typeof base[number];
    // league order: completed desc, then name; countries with only pipeline buildings at this height come last, unranked
    const league = (a: Row, b: Row) => b.completed - a.completed || (a.completed === 0 ? b.count - a.count : 0) || a.c.name.localeCompare(b.c.name);
    const ordered = [...base].sort(league);
    const rank = new Map<string, number>();
    ordered.forEach((r, i) => { if (r.completed > 0) rank.set(r.c.name, i + 1); });
    const value: Record<Key, (r: Row) => number | null> = {
      completed: r => r.completed, all: r => r.count, c200: r => r.c.completed200, c300: r => r.c.completed300,
      cities: r => r.cities, gdp: r => r.c.gdp?.usd ?? null, ppp: r => r.c.gdp?.ppp ?? null, tallest: r => r.c.tallest_h,
    };
    return { rows: sortBy(base, value[key], view.dir, league).map(r => ({ ...r, rank: rank.get(r.c.name) ?? 0 })), ranked: rank.size };
  }, [countries, min, key, view.dir]);
  const totalCompleted = rows.reduce((s, r) => s + r.completed, 0);

  return (
    <>
      <ThresholdSwitch min={min} pick={pick} label="Rank by completed towers of at least" />
      <p className="muted" style={{ marginTop: 10 }}>
        {min === 150
          ? `${ranked} countries and territories, ${totalCompleted.toLocaleString()} completed towers of 150 m and taller.` + (rows.length > ranked ? ` ${rows.length - ranked} more have only buildings under construction or topped out; they are listed unranked at the end.` : "")
          : `${ranked} of ${countries.length} have a completed building of ${min} m or taller — ${totalCompleted.toLocaleString()} in all.` +
            (rows.length > ranked ? ` ${rows.length - ranked} more have one in the pipeline only; they are listed unranked at the end.` : "")}
      </p>
      <div className="tablewrap"><table>
        <thead><tr>
          <th className="num">#</th><th>Country</th>
          <SortTh k="completed" label="Completed" sort={view} num title={`Completed buildings of ${min} m and taller`} />
          <SortTh k="all" label="All" sort={view} num title={`All buildings of ${min} m and taller, including under construction and topped out`} />
          {min < 200 && <SortTh k="c200" label="200 m+" sort={view} num title="Completed buildings of 200 m and taller" />}
          {min < 300 && <SortTh k="c300" label="300 m+" sort={view} num title="Completed buildings of 300 m and taller" />}
          <SortTh k="cities" label="Cities" sort={view} num title={`Cities with a building of ${min} m and taller`} />
          <SortTh k="gdp" label="GDP" sort={view} num title="National GDP, nominal US$ (2025)" most="largest" least="smallest" />
          <SortTh k="ppp" label="GDP (PPP)" sort={view} num title="National GDP at purchasing-power parity, international $ (2025)" most="largest" least="smallest" />
          <th title={`City with the most completed buildings of ${min} m and taller`}>Leading city</th>
          <SortTh k="tallest" label="Tallest" sort={view} title="Tallest completed building" most="tallest" least="shortest" />
        </tr></thead>
        <tbody>{rows.map(({ c, completed, count, cities, rank }) => {
          const top = c.top[min];
          return (
            <tr key={c.name}>
              <td className="num muted"><Rank rank={rank} /></td>
              <td><span className="place">{c.name}</span></td>
              <td className="num"><b>{completed}</b></td>
              <td className="num muted">{count}</td>
              {min < 200 && <td className="num">{c.completed200 || "—"}</td>}
              {min < 300 && <td className="num">{c.completed300 || "—"}</td>}
              <td className="num muted">{cities}</td>
              <GdpCell g={c.gdp} kind="usd" />
              <GdpCell g={c.gdp} kind="ppp" />
              <td>{top ? <><a className="place" href={`/city/${top.slug}/`}>{top.name}</a> <span className="muted">{top.completed}</span></> : <span className="muted">—</span>}</td>
              <td>{c.tallest_name} <span className="muted">{c.tallest_h}{"\u00a0"}m · <a className="place" href={`/city/${c.tallest_slug}/`}>{c.tallest_city}</a></span></td>
            </tr>);
        })}
        </tbody></table></div>
      <p className="muted" style={{ marginTop: 18 }}>Completed, 200 m+ and 300 m+ count finished buildings; All adds those under construction or topped out. Cities counts the places with a building at the selected height. GDP is the country's 2025 GDP from the IMF World Economic Outlook, in nominal US$ and at purchasing-power parity (hover for the source); China includes Hong Kong, Macau and Taiwan, as its tower counts do. Leading city is the one with the most completed buildings at that height. Tallest is the tallest completed building in the country. Click a column&apos;s ▼ to sort by it, most first; click again for least first. The # column always shows the country&apos;s rank by completed towers.</p>
    </>
  );
}
