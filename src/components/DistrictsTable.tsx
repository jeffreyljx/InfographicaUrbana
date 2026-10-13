"use client";
import { useMemo } from "react";
import { SortTh, sortBy, useSort } from "@/components/SortTh";
import Rank from "@/components/Rank";

/** District league table (on /districts/ and each city page), sortable by completed, pipeline, 300 m+ and tallest building. */
export interface DistrictRow {
  rank: number; name: string; slug: string; city: string; city_slug: string;
  completed: number; pipeline: number; supertall: number; tallest_name: string; tallest_h: number;
}

const KEYS = ["completed", "pipeline", "supertall", "tallest"] as const;
type Key = typeof KEYS[number];

export default function DistrictsTable({ rows, showCity = true, rankLabel = "#" }: { rows: DistrictRow[]; showCity?: boolean; rankLabel?: string }) {
  const sort = useSort<Key>(KEYS, "completed");
  const sorted = useMemo(() => {
    const value: Record<Key, (r: DistrictRow) => number> = {
      completed: r => r.completed, pipeline: r => r.pipeline, supertall: r => r.supertall, tallest: r => r.tallest_h,
    };
    // ties keep the league-table order (the # column)
    return sortBy(rows, value[sort.key], sort.dir, (a, b) => a.rank - b.rank || a.name.localeCompare(b.name));
  }, [rows, sort.key, sort.dir]);

  return (
    <div className="tablewrap"><table>
      <thead><tr>
        <th className="num">{rankLabel}</th><th>District</th>{showCity && <th>City</th>}
        <SortTh k="completed" label="Completed" sort={sort} num title="Completed buildings of 150 m and taller" />
        <SortTh k="pipeline" label="Pipeline" sort={sort} num title="Under construction or topped out" />
        <SortTh k="supertall" label="300 m+" sort={sort} num title="Buildings of 300 m and taller" />
        <SortTh k="tallest" label="Tallest" sort={sort} title="Tallest completed building in the district" most="tallest" least="shortest" />
      </tr></thead>
      <tbody>{sorted.map(d => (
        <tr key={d.city_slug + "/" + d.slug}>
          <td className="num muted"><Rank rank={d.rank} /></td>
          <td><a className="place" href={`/city/${d.city_slug}/${d.slug}/`}>{d.name}</a></td>
          {showCity && <td><a className="place" href={`/city/${d.city_slug}/`}>{d.city}</a></td>}
          <td className="num"><b>{d.completed}</b></td>
          <td className="num muted">{d.pipeline || "—"}</td>
          <td className="num">{d.supertall || "—"}</td>
          <td>{d.tallest_name} <span className="muted">{d.tallest_h}{"\u00a0"}m</span></td>
        </tr>))}
      </tbody></table></div>
  );
}
