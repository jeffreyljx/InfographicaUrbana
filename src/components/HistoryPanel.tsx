"use client";
import { useEffect, useState } from "react";
import { fmtArea, fmtYear, yearsSpan, capitalIn, TYPE_LABEL, labelInk, undated, type HistStates } from "@/lib/history";

export interface StateFile {
  slug: string; name: string; native: string[]; alt: string[]; type: string; family: string;
  start: { year: number; month?: number } | null; end: { year: number; month?: number } | null;
  wikipedia: string | null; wikidata: string | null; colour: string; fb: number;
  first: number | null; last: number | null; peak: number; peakYear: number | null;
  predecessors: { slug: string; name: string; year: number | null; text: string }[];
  successors: { slug: string; name: string; year: number | null; text: string }[];
  capitals: { name: string; lon: number; lat: number; from: number; to: number }[];
  rulers: { name: string; from: number; to: number; title?: string }[];
  area: [number, number][];
  ledger: { y: number; m?: number; t: string; x: string; cp?: string; cpn?: string; u?: string; c?: number }[];
  wars: { name: string; from: number; to: number; outcome: string; u?: string }[];
  certainty: { from: number; to: number; level: string; note: string }[];
  sources: { url: string; title: string }[];
}

const files = new Map<string, Promise<StateFile>>();
export function loadStateFile(slug: string): Promise<StateFile> {
  let p = files.get(slug);
  if (!p) {
    p = fetch(`/history/state/${slug}.json`).then(r => { if (!r.ok) throw new Error(String(r.status)); return r.json(); });
    p.catch(() => files.delete(slug));
    files.set(slug, p);
  }
  return p;
}

export interface PanelNow { cells: number; status: string; party: number }

interface Props {
  st: HistStates;
  owner: number;
  year: number;
  now: PanelNow;
  onYear: (y: number) => void;
  onPick: (owner: number) => void;
  onClose: () => void;
}

const host = (u: string) => { try { return new URL(u).hostname.replace(/^www\.|^en\./, ""); } catch { return u; } };
const pageTitle = (u: string) => { try { const m = /\/wiki\/([^#?]+)/.exec(u); return m ? decodeURIComponent(m[1]).replace(/_/g, " ") : host(u); } catch { return u; } };

/** The panel for a state, opened from the map, a caption or search: its years, type, capital, size in the year, and the
 *  ledger events nearest the year with their sources; the full record is on its page. */
export default function HistoryPanel({ st, owner, year, now, onYear, onPick, onClose }: Props) {
  const k = owner - 1;
  const slug = st.slug[k];
  const [f, setF] = useState<StateFile | null>(null);
  const [failed, setFailed] = useState(false);
  useEffect(() => {
    let live = true;
    setF(null); setFailed(false);
    if (slug) loadStateFile(slug).then(x => { if (live) setF(x); }).catch(() => { if (live) setFailed(true); });
    return () => { live = false; };
  }, [slug]);

  const colour = st.colour[k];
  const cap = capitalIn(st.capitals[k], year);
  const type = TYPE_LABEL[st.type[k]] ?? "State";
  const alive = now.cells > 0;
  const party = now.party ? st.name[now.party - 1] : null;
  const statusLine = !alive ? null
    : now.status === "vassal" ? <>a vassal of <button className="link" onClick={() => onPick(now.party)}>{party}</button></>
    : now.status === "constituent" ? <>a member of <button className="link" onClick={() => onPick(now.party)}>{party}</button></>
    : now.status === "occupied" ? <>partly occupied by <button className="link" onClick={() => onPick(now.party)}>{party}</button></>
    : now.status === "contested" ? <>contested with <button className="link" onClick={() => onPick(now.party)}>{party}</button></>
    : null;

  // the ledger events nearest the year: up to two before it (or in it) and two after
  let events: StateFile["ledger"] = [];
  if (f) {
    const i = f.ledger.findIndex(e => e.y > year);
    const cut = i < 0 ? f.ledger.length : i;
    events = [...f.ledger.slice(Math.max(0, cut - 3), cut), ...f.ledger.slice(cut, cut + 2)];
  }
  const span = st.first[k] !== null ? yearsSpan(st.first[k], st.last[k]) : "";
  const dossierSpan = yearsSpan(st.start[k], st.end[k]);

  return (
    <aside className="panel mpanel hpanel" aria-label="State details">
      <button className="x" onClick={onClose} aria-label="Close">×</button>
      <div className="m-head" style={{ background: colour }}>
        <span className="m-kind">{type}{st.fb[k] ? " · provisional colour" : ""}</span>
      </div>
      <div className="body">
        <h1 style={{ color: labelInk(colour) }}>{st.name[k]}</h1>
        {f && f.native.length > 0 && <p className="m-local">{f.native.slice(0, 3).join(" · ")}</p>}
        <p className="where">{dossierSpan || span}{st.capitals[k].length > 0 && cap ? <> · capital <span className="place">{cap[0]}</span></> : null}</p>
        <p className="m-note">
          {alive ? <>In {fmtYear(year, true)}: {fmtArea(now.cells, st.cellKm2)}{statusLine ? <>, {statusLine}</> : null}.</>
            : st.first[k] === null ? <>Not drawn on the map.</>
            : year < (st.first[k] ?? 0) ? <>Not on the map yet in {fmtYear(year, true)}: it first holds land in {fmtYear(st.first[k]!, true)}. <button className="link" onClick={() => onYear(st.first[k]!)}>Go to {fmtYear(st.first[k]!)}</button></>
            : <>Gone from the map by {fmtYear(year, true)}: it last holds land in {fmtYear(st.last[k]!, true)}. <button className="link" onClick={() => onYear(st.last[k]!)}>Go to {fmtYear(st.last[k]!)}</button></>}
        </p>
        <dl className="facts">
          {span && <div><dt>On the map</dt><dd>{span}</dd></div>}
          {st.peak[k] > 0 && <div><dt>Largest</dt><dd>{fmtArea(st.peak[k], st.cellKm2)}{st.peakYear[k] !== null ? <span className="muted"> in {fmtYear(st.peakYear[k]!)}</span> : null}</dd></div>}
        </dl>
        {f && f.area.length > 1 && <AreaSpark f={f} year={year} colour={colour} onYear={onYear} />}
        {slug && <h2 className="m-h">Events around {fmtYear(year, true)}</h2>}
        {!f && slug && !failed && <p className="muted">Loading the record…</p>}
        {failed && <p className="muted">The record could not be loaded.</p>}
        {f && events.length === 0 && <p className="muted">No dated events in the record.</p>}
        {events.length > 0 && (
          <ol className="h-ledger">
            {events.map((e, i) => (
              <li key={i} className={e.y > year ? "later" : undefined}>
                <button className="link h-ly" onClick={() => onYear(e.y)}>{fmtYear(e.y)}</button>
                <span>{undated(e.x)}{e.u && <> <a className="h-src" href={e.u} target="_blank" rel="noopener" title={e.u}>{pageTitle(e.u)} ↗</a></>}</span>
              </li>
            ))}
          </ol>
        )}
        <div className="actions">
          {slug && <a className="btn primary" href={`/history/${slug}/`}>The state&apos;s page</a>}
          {f?.wikipedia && <a className="btn" href={`https://en.wikipedia.org/wiki/${encodeURIComponent(f.wikipedia.replace(/ /g, "_"))}`} target="_blank" rel="noopener">Wikipedia ↗</a>}
        </div>
        {f && (f.predecessors.length > 0 || f.successors.length > 0) && (
          <p className="h-links">
            {f.predecessors.length > 0 && <>After {f.predecessors.slice(0, 3).map((p, i) => <span key={i}>{i ? ", " : ""}{p.slug ? <a href={`/history/${p.slug}/`}>{p.name}</a> : p.name}</span>)}. </>}
            {f.successors.length > 0 && <>Followed by {f.successors.slice(0, 3).map((p, i) => <span key={i}>{i ? ", " : ""}{p.slug ? <a href={`/history/${p.slug}/`}>{p.name}</a> : p.name}</span>)}.</>}
          </p>
        )}
        {!slug && <p className="muted">Named in the record of another state; it has no record of its own yet.</p>}
      </div>
    </aside>
  );
}

/** Area over time, a small step chart; a click moves the map to that year. */
function AreaSpark({ f, year, colour, onYear }: { f: StateFile; year: number; colour: string; onYear: (y: number) => void }) {
  const a = f.area;
  const y0 = a[0][0], y1 = Math.max(a[a.length - 1][0], y0 + 1);
  const max = Math.max(1, ...a.map(p => p[1]));
  const W = 360, Hh = 54;
  const x = (y: number) => ((y - y0) / (y1 - y0)) * W;
  let d = `M0 ${Hh}`;
  for (let i = 0; i < a.length; i++) {
    const yy = Hh - (a[i][1] / max) * (Hh - 4);
    d += `L${x(a[i][0]).toFixed(1)} ${i ? (Hh - (a[i - 1][1] / max) * (Hh - 4)).toFixed(1) : Hh}L${x(a[i][0]).toFixed(1)} ${yy.toFixed(1)}`;
  }
  d += `L${W} ${(Hh - (a[a.length - 1][1] / max) * (Hh - 4)).toFixed(1)}L${W} ${Hh}Z`;
  const inRange = year >= y0 && year <= y1;
  return (
    <figure className="h-spark">
      <svg viewBox={`0 0 ${W} ${Hh}`} preserveAspectRatio="none" onClick={e => {
        const r = e.currentTarget.getBoundingClientRect();
        onYear(Math.round(y0 + ((e.clientX - r.left) / r.width) * (y1 - y0)));
      }}>
        <path d={d} fill={colour} fillOpacity={0.55} stroke={labelInk(colour)} strokeWidth={1} vectorEffect="non-scaling-stroke" />
        {inRange && <line x1={x(year)} x2={x(year)} y1={0} y2={Hh} stroke="#2B1D17" strokeWidth={1.5} vectorEffect="non-scaling-stroke" />}
      </svg>
      <figcaption><span>{fmtYear(y0)}</span><span>Area held, by year</span><span>{fmtYear(y1)}</span></figcaption>
    </figure>
  );
}
