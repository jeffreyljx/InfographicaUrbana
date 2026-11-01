import type { Metadata } from "next";
import { notFound } from "next/navigation";
import Nav from "@/components/Nav";
import "@/components/history.css";
import { historySlugs, historyState, historyStates, historyIndexBuilt } from "@/lib/historyServer";
import { fmtArea, fmtYear, yearsSpan, labelInk, undated, type HistStates } from "@/lib/history";
import type { StateFile } from "@/components/HistoryPanel";

export const dynamicParams = false;
export function generateStaticParams() {
  return historySlugs().map(slug => ({ slug }));
}

const TYPE: Record<string, string> = { state: "State", dynasty: "Dynasty", culture: "Archaeological culture", colony: "Colony", rebel: "Rebel state", umbrella: "Association" };
const EVENT: Record<string, string> = {
  found: "founded", gain: "gain", loss: "loss", contest_start: "war begins", contest_end: "war ends", vassal_start: "vassal", vassal_end: "vassal ends",
  occupation_start: "occupation", occupation_end: "occupation ends", capital_move: "capital", rename: "renamed", end: "end", collapse: "end",
};
const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const span = (f: StateFile) => yearsSpan(f.start?.year ?? null, f.end?.year ?? null);
const wikiTitle = (u?: string) => { if (!u) return ""; const m = /\/wiki\/([^#?]+)/.exec(u); try { return m ? decodeURIComponent(m[1]).replace(/_/g, " ") : new URL(u).hostname; } catch { return u; } };

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const f = historyState(slug);
  if (!f) return {};
  const t = TYPE[f.type] ?? "State";
  const description = `${f.name}: ${t.toLowerCase()}, ${span(f)}. Its borders year by year on CartaHistoria${f.peak ? `, at most ${fmtArea(f.peak)}${f.peakYear !== null ? ` in ${fmtYear(f.peakYear)}` : ""}` : ""}, with ${f.ledger.length} dated territorial events and their sources.`;
  return { title: `CartaHistoria · ${f.name}`, description, alternates: { canonical: `/history/${slug}/` } };
}

export default async function HistoryStatePage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const f = historyState(slug);
  if (!f) notFound();
  const st = historyStates();
  const { built, drafts } = historyIndexBuilt();
  const ink = labelInk(f.colour);
  const mapAt = (y: number) => `/history/?year=${y}&state=${encodeURIComponent(slug)}`;
  const firstMap = f.first ?? f.start?.year ?? 0;
  return (
    <>
      <Nav solid active="history-state" />
      <main className="page hpage">
        <p className="crumbs"><a href="/history/">CartaHistoria</a> › {TYPE[f.type] ?? "State"}</p>
        <div className="h-band" style={{ background: f.colour }} aria-hidden="true" />
        <h1 style={{ color: ink }}>{f.name}</h1>
        {f.native.length > 0 && <p className="h-native">{f.native.join(" · ")}</p>}
        {f.alt.length > 0 && <p className="h-alt">Also {f.alt.join(", ")}</p>}
        <p className="lead">
          {TYPE[f.type] ?? "State"}, {span(f)}.
          {f.first !== null ? <> On the map {yearsSpan(f.first, f.last)}{f.peak ? <>, largest in {fmtYear(f.peakYear ?? f.first)} at {fmtArea(f.peak)}</> : null}.</> : <> Not drawn on the map.</>}
          {f.fb ? <span className="muted"> Its colour is provisional.</span> : null}
        </p>
        <div className="heroactions">
          {f.first !== null && <a className="btn primary" href={mapAt(firstMap)}>On the map in {fmtYear(firstMap)}</a>}
          {f.peakYear !== null && f.peakYear !== f.first && <a className="btn" href={mapAt(f.peakYear)}>At its largest, {fmtYear(f.peakYear)}</a>}
          {f.wikipedia && <a className="btn" href={`https://en.wikipedia.org/wiki/${encodeURIComponent(f.wikipedia.replace(/ /g, "_"))}`} target="_blank" rel="noopener">Wikipedia ↗</a>}
        </div>

        {f.area.length > 1 && <><h2>Area over time</h2><AreaChart f={f} /></>}

        <div className="h-cols">
          {f.capitals.length > 0 && <section><h2>Capitals</h2><ul>{f.capitals.map((c, i) => <li key={i}><span className="place">{c.name}</span> <span className="muted">{yearsSpan(c.from, c.to)}</span></li>)}</ul></section>}
          {(f.predecessors.length > 0 || f.successors.length > 0) && (
            <section>
              {f.predecessors.length > 0 && <><h2>Before</h2><ul>{f.predecessors.map((p, i) => <li key={i}><Ref s={p} st={st} /></li>)}</ul></>}
              {f.successors.length > 0 && <><h2>After</h2><ul>{f.successors.map((p, i) => <li key={i}><Ref s={p} st={st} /></li>)}</ul></>}
            </section>
          )}
        </div>

        {f.rulers.length > 0 && (
          <>
            <h2>Rulers</h2>
            <div className="tablewrap"><table><thead><tr><th>Reign</th><th>Ruler</th></tr></thead>
              <tbody>{f.rulers.map((r, i) => <tr key={i}><td className="num" style={{ textAlign: "left", whiteSpace: "nowrap" }}>{yearsSpan(r.from, r.to)}</td><td>{r.name}{r.title ? <span className="muted"> · {r.title}</span> : null}</td></tr>)}</tbody>
            </table></div>
          </>
        )}

        <h2>Territorial events</h2>
        {f.ledger.length === 0 ? <p>No dated events in the record.</p> : (
          <div className="tablewrap"><table className="h-led"><thead><tr><th>Year</th><th>Event</th><th>Source</th></tr></thead>
            <tbody>{f.ledger.map((e, i) => (
              <tr key={i}>
                <td><a href={mapAt(e.y)}>{fmtYear(e.y)}</a>{e.m ? <span className="muted"> {MONTHS[e.m - 1]}</span> : null}</td>
                <td>{undated(e.x)}{e.t && EVENT[e.t] ? <span className="muted"> · {EVENT[e.t]}</span> : null}{e.cp ? <span className="muted"> · {e.cpn ? <a href={`/history/${e.cp}/`}>{e.cpn}</a> : e.cp}</span> : null}</td>
                <td className="src">{e.u ? <a href={e.u} target="_blank" rel="noopener">{wikiTitle(e.u)}</a> : ""}</td>
              </tr>
            ))}</tbody>
          </table></div>
        )}

        {f.wars.length > 0 && (
          <>
            <h2>Wars</h2>
            <div className="tablewrap"><table className="h-led"><thead><tr><th>Years</th><th>War</th><th>Outcome</th></tr></thead>
              <tbody>{f.wars.map((w, i) => <tr key={i}><td>{yearsSpan(w.from, w.to)}</td><td>{w.u ? <a href={w.u} target="_blank" rel="noopener">{w.name}</a> : w.name}</td><td>{w.outcome}</td></tr>)}</tbody>
            </table></div>
          </>
        )}

        {f.certainty.length > 0 && (
          <>
            <h2>How sure the borders are</h2>
            <ul className="h-note">{f.certainty.map((c, i) => <li key={i}><b>{yearsSpan(c.from, c.to)}: {c.level === "sharp" ? "sharp (treaty or survey)" : c.level === "soft" ? "soft (approximate frontier)" : c.level}.</b> {c.note}</li>)}</ul>
          </>
        )}

        <h2>Sources</h2>
        <ol className="h-sources">{f.sources.map((s, i) => <li key={i}><a href={s.url} target="_blank" rel="noopener">{s.title || s.url}</a></li>)}</ol>
      </main>
      <footer className="page foot">
        Borders from <a href="https://seshat-db.com/" target="_blank" rel="noopener">Cliopatria</a> (Seshat Global History Databank, CC BY 4.0), corrected and dated year by year from the Wikipedia pages listed above; one H3 resolution-5 cell is about 253 km².
        Data of {built}{drafts ? `, ${drafts} of 119 windows still drafts under review` : ""}. Basemap on the map by OpenFreeMap © OpenMapTiles, data from OpenStreetMap.
      </footer>
    </>
  );
}

function Ref({ s, st }: { s: StateFile["predecessors"][number]; st: HistStates }) {
  const k = s.slug ? st.slug.indexOf(s.slug) : -1;
  return (
    <>
      {k >= 0 ? <a href={`/history/${s.slug}/`}><i className="m-sw" style={{ background: st.colour[k] }} />{s.name}</a> : s.name}
      {s.year !== null && <span className="muted"> {fmtYear(s.year)}</span>}
      {s.text && <span className="muted"> · {s.text}</span>}
    </>
  );
}

/** Area held each year, as a step chart with a few year and area marks. */
function AreaChart({ f }: { f: StateFile }) {
  const a = f.area;
  const y0 = a[0][0], y1 = Math.max(a[a.length - 1][0], y0 + 1);
  const max = Math.max(1, ...a.map(p => p[1]));
  const W = 900, H = 200, L = 64, R = 12, T = 12, B = 24;
  const x = (y: number) => L + ((y - y0) / (y1 - y0)) * (W - L - R);
  const yv = (c: number) => T + (1 - c / max) * (H - T - B);
  let d = `M${x(y0)} ${yv(0)}`;
  let prev = 0;
  for (const [yy, c] of a) { d += `L${x(yy).toFixed(1)} ${yv(prev).toFixed(1)}L${x(yy).toFixed(1)} ${yv(c).toFixed(1)}`; prev = c; }
  d += `L${x(y1)} ${yv(prev).toFixed(1)}L${x(y1)} ${yv(0)}Z`;
  const ticks = niceYears(y0, y1);
  return (
    <svg className="h-chart" viewBox={`0 0 ${W} ${H}`} role="img" aria-label={`Area held by ${f.name}, ${fmtYear(y0)} to ${fmtYear(y1)}`}>
      <line x1={L} x2={W - R} y1={yv(0)} y2={yv(0)} stroke="#C8AB9E" />
      <path d={d} fill={f.colour} fillOpacity={0.6} stroke={labelInk(f.colour)} strokeWidth={1.2} />
      <text x={L - 6} y={yv(max) + 4} textAnchor="end">{fmtArea(max).replace(" km²", "")}</text>
      <text x={L - 6} y={yv(max) + 17} textAnchor="end">km²</text>
      {ticks.map(t => <text key={t} x={x(t)} y={H - 6} textAnchor="middle">{fmtYear(t)}</text>)}
    </svg>
  );
}
function niceYears(a: number, b: number): number[] {
  const span = b - a;
  const step = [1, 2, 5, 10, 20, 25, 50, 100, 200, 250, 500, 1000, 2000].find(s => span / s <= 8) ?? 1000;
  const out: number[] = [];
  for (let t = Math.ceil(a / step) * step; t <= b; t += step) out.push(t);
  return out;
}

