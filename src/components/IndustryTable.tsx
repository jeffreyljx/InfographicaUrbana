"use client";
import { useMemo, useState } from "react";
import { SortTh, sortBy, type SortDir, type SortState } from "@/components/SortTh";
import { money, moneyK, site } from "@/lib/industryFormat";

/** The Industry and Exports page's full tables, with every row's sources. Numeric columns sort most-first, then
 *  least-first, like the site's other tables; the sort stays on the page (there are several tables, so not in the URL). */

export interface TradeTableRow { place: string; slug: string | null; country: string; year: string; ex: number | null; im: number | null; total: number | null; how: string; caveat: string; note: string; source: string[] }
export interface ExportTableRow { place: string; slug: string | null; country: string; year: string; ex: number; how: string; caveat: string; note: string; source: string[] }
export interface MfgTableRow { place: string; slug: string | null; country: string; year: string; va: number; jobs: number | null; perJob: number | null; measure: string; unit: string; upper: boolean; note: string; source: string[] }

function useLocalSort<K extends string>(initial: K): SortState<K> {
  const [key, setKey] = useState<K>(initial);
  const [dir, setDir] = useState<SortDir>("desc");
  return { key, dir, toggle: (k: K) => { setDir(k === key && dir === "desc" ? "asc" : "desc"); setKey(k); } };
}

const Place = ({ r }: { r: { place: string; slug: string | null } }) =>
  r.slug ? <a className="place" href={`/city/${r.slug}/`} title={`Skyscrapers in ${r.place} on ScraperMap`}>{r.place}</a> : <span className="place">{r.place}</span>;

const Sources = ({ urls }: { urls: string[] }) => (
  <>{urls.map((u, i) => <span key={i}>{i > 0 && ", "}<a href={encodeURI(u)} target="_blank" rel="noopener">{site(u)}</a></span>)}</>
);

const Note = ({ caveat, note }: { caveat?: string; note: string }) => (
  <>{caveat && <span className="pill">{caveat}</span>}{caveat && note && " "}{note}</>
);

const n1 = (v: number | null) => v == null ? "–" : v.toLocaleString("en-US", { minimumFractionDigits: 1, maximumFractionDigits: 1 });
const rankOf = <T,>(rows: T[], v: (r: T) => number | null) => new Map([...rows].sort((a, b) => (v(b) ?? -1) - (v(a) ?? -1)).map((r, i) => [r, i + 1]));

export function TradeTable({ rows }: { rows: TradeTableRow[] }) {
  const sort = useLocalSort<"total" | "ex" | "im">("total");
  const rank = useMemo(() => rankOf(rows, r => r.total), [rows]);
  const shown = useMemo(() => sortBy(rows, r => r[sort.key], sort.dir, (a, b) => (rank.get(a) ?? 0) - (rank.get(b) ?? 0)), [rows, sort.key, sort.dir, rank]);
  return (
    <div className="tablewrap"><table className="itable">
      <thead><tr>
        <th className="num">#</th><th>Place</th><th>Country</th><th className="num">Year</th>
        <SortTh k="ex" label="Exports $bn" sort={sort} num />
        <SortTh k="im" label="Imports $bn" sort={sort} num />
        <SortTh k="total" label="Total $bn" sort={sort} num />
        <th>How counted</th><th>Note</th><th>Sources</th>
      </tr></thead>
      <tbody>{shown.map(r => (
        <tr key={r.place}>
          <td className="num muted">{rank.get(r)}</td><td><Place r={r} /></td><td>{r.country}</td><td className="num">{r.year}</td>
          <td className="num">{n1(r.ex)}</td><td className="num">{n1(r.im)}</td><td className="num"><b>{n1(r.total)}</b></td>
          <td className="how">{r.how}</td><td className="note"><Note caveat={r.caveat} note={r.note} /></td><td className="src"><Sources urls={r.source} /></td>
        </tr>
      ))}</tbody>
    </table></div>
  );
}

export function ExportTable({ rows }: { rows: ExportTableRow[] }) {
  return (
    <div className="tablewrap"><table className="itable">
      <thead><tr>
        <th className="num">#</th><th>Place</th><th>Country</th><th className="num">Year</th><th className="num">Exports $bn</th>
        <th>How counted</th><th>Note</th><th>Sources</th>
      </tr></thead>
      <tbody>{rows.map((r, i) => (
        <tr key={r.place}>
          <td className="num muted">{i + 1}</td><td><Place r={r} /></td><td>{r.country}</td><td className="num">{r.year}</td>
          <td className="num"><b>{n1(r.ex)}</b></td>
          <td className="how">{r.how}</td><td className="note"><Note caveat={r.caveat} note={r.note} /></td><td className="src"><Sources urls={r.source} /></td>
        </tr>
      ))}</tbody>
    </table></div>
  );
}

export function MfgTable({ rows }: { rows: MfgTableRow[] }) {
  const sort = useLocalSort<"va" | "jobs" | "perJob">("va");
  const rank = useMemo(() => rankOf(rows, r => r.va), [rows]);
  const shown = useMemo(() => sortBy(rows, r => r[sort.key], sort.dir, (a, b) => (rank.get(a) ?? 0) - (rank.get(b) ?? 0)), [rows, sort.key, sort.dir, rank]);
  return (
    <div className="tablewrap"><table className="itable">
      <thead><tr>
        <th className="num">#</th><th>Place</th><th>Country</th><th className="num">Year</th>
        <SortTh k="va" label="Value added" sort={sort} num title="Manufacturing value added, US$" />
        <SortTh k="jobs" label="Jobs" sort={sort} num title="Manufacturing jobs" />
        <SortTh k="perJob" label="Per job" sort={sort} num title="Value added per manufacturing job, US$" />
        <th>Measure</th><th>Note</th><th>Sources</th>
      </tr></thead>
      <tbody>{shown.map(r => (
        <tr key={r.place}>
          <td className="num muted">{rank.get(r)}</td><td><Place r={r} /></td><td>{r.country}</td><td className="num">{r.year}</td>
          <td className="num">{r.upper && <span className="ub" title="Upper bound: secondary-industry value added, which includes construction">up to </span>}<b>{money(r.va)}</b></td>
          <td className="num">{r.jobs == null ? "–" : r.jobs.toLocaleString("en-US")}</td>
          <td className="num">{r.perJob == null ? "–" : moneyK(r.perJob)}</td>
          <td className="how">{r.measure}. {r.unit}</td><td className="note">{r.note}</td><td className="src"><Sources urls={r.source} /></td>
        </tr>
      ))}</tbody>
    </table></div>
  );
}
