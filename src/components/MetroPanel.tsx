"use client";
import { useState } from "react";
import { neighbours, fmtKm, fmtInt, stationLabel, type MetroData, type MetroLine, type MetroStation, type MetroSystem, NEVER_YEAR } from "@/lib/metro";

export type MetroPick = { kind: "station"; i: number } | { kind: "line"; i: number } | { kind: "system"; i: number };

interface Props {
  data: MetroData;
  pick: MetroPick;
  year: number;
  onPick: (p: MetroPick) => void;
  onClose: () => void;
}

/** The infographic for a station, a line or a system, opened from the map, search or another panel. */
export default function MetroPanel({ data, pick, year, onPick, onClose }: Props) {
  const [copied, setCopied] = useState(false);
  const share = async () => {
    try { await navigator.clipboard.writeText(location.href); setCopied(true); setTimeout(() => setCopied(false), 1500); } catch { /* ignore */ }
  };
  const shareBtn = <button className="btn" onClick={share}>{copied ? "Link copied" : "Share"}</button>;
  return (
    <aside className="panel mpanel" aria-label="Metro details">
      <button className="x" onClick={onClose} aria-label="Close">×</button>
      {pick.kind === "station" && <StationView d={data} st={data.stations[pick.i]} year={year} onPick={onPick} share={shareBtn} />}
      {pick.kind === "line" && <LineView d={data} l={data.lines[pick.i]} year={year} onPick={onPick} share={shareBtn} />}
      {pick.kind === "system" && <SystemView d={data} s={data.systems[pick.i]} year={year} onPick={onPick} share={shareBtn} />}
    </aside>
  );
}

const LinePill = ({ l, onClick }: { l: MetroLine; onClick?: () => void }) => (
  <button className="m-pill" style={{ ["--lc" as string]: l.colour }} onClick={onClick} title={`Open ${l.name}`}>
    <i className="m-sw" />{l.name}
  </button>
);

function Where({ d, s, onPick }: { d: MetroData; s: MetroSystem; onPick: (p: MetroPick) => void }) {
  return (
    <p className="where">
      <button className="link m-sys" onClick={() => onPick({ kind: "system", i: s.i })}>{s.name}</button> · <span className="place">{s.city}</span>, <span className="place">{s.country}</span>
    </p>
  );
}

function StationView({ d, st, year, onPick, share }: { d: MetroData; st: MetroStation; year: number; onPick: (p: MetroPick) => void; share: React.ReactNode }) {
  const s = d.systems[st.sys];
  const lines = st.lines.map(([l, y]) => ({ l: d.lines[l], y }));
  const openNow = st.firstYear <= year && st.closeYear > year;
  const inter = st.interYear !== NEVER_YEAR;
  const wiki = st.wd ? `https://www.wikidata.org/wiki/Special:GoToLinkedPage/enwiki/${st.wd}` : null;
  return (
    <>
      <div className="m-head station" style={{ background: `linear-gradient(90deg, ${lines.map(({ l }, k) => `${l.colour} ${k * 100 / lines.length}% ${(k + 1) * 100 / lines.length}%`).join(", ")})` }}>
        <span className="m-kind">{inter ? "Interchange station" : "Station"}</span>
      </div>
      <div className="body">
        <h1>{stationLabel(st)}</h1>
        {st.en && st.name !== st.en && <p className="m-local" lang="">{st.name}</p>}
        <Where d={d} s={s} onPick={onPick} />
        {!openNow && (
          <p className="m-note">{st.firstYear > year ? `Not open yet in ${year}: the first line reaches it in ${st.firstYear}.` : `Closed by ${year}.`}</p>
        )}
        <dl className="facts">
          <div><dt>Opened</dt><dd>{st.firstYear}</dd></div>
          <div><dt>Lines</dt><dd>{lines.length}</dd></div>
          {inter && <div><dt>Interchange since</dt><dd>{st.interYear}</dd></div>}
          {st.closeYear !== NEVER_YEAR && <div><dt>Closed</dt><dd>{st.closeYear}</dd></div>}
        </dl>
        <h3 className="m-h">Lines at this station</h3>
        <ul className="m-lines">
          {lines.map(({ l, y }) => (
            <li key={l.i}>
              <div className="m-line-row">
                <LinePill l={l} onClick={() => onPick({ kind: "line", i: l.i })} />
                <span className="muted">{y > year ? `from ${y}` : `since ${y}`}{l.closeYear !== NEVER_YEAR ? `, closed ${l.closeYear}` : ""}</span>
              </div>
              {neighbours(l, st.i).map((n, k) => (
                <div key={k} className="m-next">
                  {n.prev !== null ? <button className="link" onClick={() => onPick({ kind: "station", i: n.prev! })}>← {stationLabel(d.stations[n.prev])}</button> : <span className="muted">terminus</span>}
                  <span className="m-dot" style={{ borderColor: l.colour }} />
                  {n.next !== null ? <button className="link" onClick={() => onPick({ kind: "station", i: n.next! })}>{stationLabel(d.stations[n.next])} →</button> : <span className="muted">terminus</span>}
                </div>
              ))}
            </li>
          ))}
        </ul>
        <div className="actions">
          {wiki && <a className="btn primary" href={wiki} target="_blank" rel="noopener">Wikipedia ↗</a>}
          <a className={"btn" + (wiki ? "" : " primary")} href={`https://www.openstreetmap.org/?mlat=${st.lat}&mlon=${st.lon}#map=18/${st.lat}/${st.lon}`} target="_blank" rel="noopener">OpenStreetMap ↗</a>
          {share}
        </div>
        <details className="loc">
          <summary>Where these facts come from</summary>
          <p>Position and name from OpenStreetMap (8 Oct 2026). The year each line reached the station comes from the opening stages Wikipedia lists for that line; where a stage could not be matched to the mapped stations, the station takes the year of the nearest dated stretch of its line.</p>
          <p className="muted">{st.lat.toFixed(5)}, {st.lon.toFixed(5)}{st.wd ? <> · <a href={`https://www.wikidata.org/wiki/${st.wd}`} target="_blank" rel="noopener">Wikidata {st.wd}</a></> : null}</p>
        </details>
      </div>
    </>
  );
}

const EVENT: Record<string, string> = { open: "Opened", extension: "Extended", closure: "Closed", reopening: "Reopened", infill_station: "New station", transfer: "Transferred", renaming: "Renamed" };

function LineView({ d, l, year, onPick, share }: { d: MetroData; l: MetroLine; year: number; onPick: (p: MetroPick) => void; share: React.ReactNode }) {
  const s = d.systems[l.sys];
  const route = l.routes[0] ?? [];
  const yearAt = (st: number) => d.stations[st].lines.find(([x]) => x === l.i)?.[1] ?? l.openYear;
  const riders = l.riders != null ? `${fmtKm(l.riders)} million a year` : l.ridersDaily != null ? `${fmtInt(l.ridersDaily)} thousand a day` : null;
  const facts: [string, React.ReactNode][] = ([
    ["Opened", l.opened],
    ["Latest extension", l.ext],
    ["Closed", l.closed],
    ["Length", l.km != null ? `${fmtKm(l.km)} km` : l.kmOsm != null ? `${fmtKm(l.kmOsm)} km mapped` : ""],
    ["Stations", l.stations != null ? String(l.stations) : l.stationsOsm != null ? `${l.stationsOsm} mapped` : ""],
    ["Riders", riders ? `${riders}${l.ridersYear ? ` (${l.ridersYear})` : ""}` : ""],
    ["Termini", l.termini],
    ["Rolling stock", l.stock],
    ["Car type", l.carType],
    ["Cars per train", l.cars],
    ["Power", l.power],
    ["Gauge", l.gauge ? `${l.gauge} mm` : ""],
    ["Automation", l.automation],
    ["Operator", l.operator],
  ] as [string, string][]).filter(([, v]) => v);
  return (
    <>
      <div className="m-head" style={{ background: l.colour }}>
        <span className="m-kind">{l.express ? "Express metro line" : "Metro line"}</span>
      </div>
      <div className="body">
        <h1>{l.name}</h1>
        {l.local && <p className="m-local">{l.local}</p>}
        <Where d={d} s={s} onPick={onPick} />
        {l.openYear > year && <p className="m-note">Not open yet in {year}: it opens in {l.openYear}.</p>}
        {l.closeYear <= year && <p className="m-note">Closed in {l.closeYear}.</p>}
        <dl className="facts m-facts">
          {facts.map(([k, v]) => <div key={k} className={String(v).length > 26 ? "wide" : undefined}><dt>{k}</dt><dd>{v}</dd></div>)}
        </dl>
        {l.stages.length > 0 && (<>
          <h3 className="m-h">How it grew</h3>
          <ol className="m-stages">
            {l.stages.map((g, k) => (
              <li key={k} className={Number(g.date.slice(0, 4)) > year ? "later" : undefined}>
                <span className="m-date">{g.date}</span>
                <span>{EVENT[g.event] ?? g.event}{g.from ? `: ${g.from}` : ""}{g.to ? ` – ${g.to}` : ""}{g.km ? ` (${fmtKm(g.km)} km)` : ""}</span>
              </li>
            ))}
          </ol>
        </>)}
        {route.length > 1 && (<>
          <h3 className="m-h">Stations{l.routes.length > 1 ? <span className="muted"> (longest of {l.routes.length} mapped routes)</span> : null}</h3>
          <ol className="m-strip" style={{ ["--lc" as string]: l.colour }}>
            {route.map(st => {
              const y = yearAt(st), x = d.stations[st];
              return (
                <li key={st} className={y > year ? "later" : undefined}>
                  <span className={"m-bub" + (x.lines.length > 1 ? " inter" : "")} />
                  <button className="link" onClick={() => onPick({ kind: "station", i: st })}>{stationLabel(x)}</button>
                  <span className="m-yr">{y}</span>
                </li>
              );
            })}
          </ol>
        </>)}
        <div className="actions">{share}</div>
        {l.sources.length > 0 && (
          <details className="loc">
            <summary>Sources</summary>
            {l.sources.map(u => <p key={u}><a href={u} target="_blank" rel="noopener">{decodeURIComponent(u.replace(/^https?:\/\/(www\.)?/, "")).slice(0, 80)}</a></p>)}
            <p className="muted">Track and stations from OpenStreetMap (8 Oct 2026). Line id {l.id}.</p>
          </details>
        )}
      </div>
    </>
  );
}

function SystemView({ d, s, year, onPick, share }: { d: MetroData; s: MetroSystem; year: number; onPick: (p: MetroPick) => void; share: React.ReactNode }) {
  const lines = d.lines.filter(l => l.sys === s.i).sort((a, b) => a.openYear - b.openYear || a.name.localeCompare(b.name, "en", { numeric: true }));
  const openLines = lines.filter(l => l.openYear <= year && l.closeYear > year).length;
  return (
    <>
      <div className="m-head" style={{ background: `linear-gradient(90deg, ${lines.slice(0, 12).map((l, k, a) => `${l.colour} ${k * 100 / a.length}% ${(k + 1) * 100 / a.length}%`).join(", ")})` }}>
        <span className="m-kind">Metro system</span>
      </div>
      <div className="body">
        <h1>{s.name}</h1>
        <p className="where"><span className="place">{s.city}</span>, <span className="place">{s.country}</span></p>
        <dl className="facts">
          <div><dt>First line</dt><dd>{s.firstOpened || s.first}</dd></div>
          <div><dt>Lines</dt><dd>{lines.length}{openLines !== lines.length ? <span className="muted"> · {openLines} open in {year}</span> : null}</dd></div>
          {s.km != null && <div><dt>Length</dt><dd>{fmtKm(s.km)} km</dd></div>}
          {s.stations != null && <div><dt>Stations</dt><dd>{s.stations}</dd></div>}
          {s.riders != null && <div><dt>Riders</dt><dd>{fmtKm(s.riders)} million a year{s.ridersYear ? <span className="muted"> ({s.ridersYear})</span> : null}</dd></div>}
        </dl>
        <h3 className="m-h">Lines</h3>
        <ul className="m-syslines">
          {lines.map(l => (
            <li key={l.i} className={l.openYear > year || l.closeYear <= year ? "later" : undefined}>
              <LinePill l={l} onClick={() => onPick({ kind: "line", i: l.i })} />
              <span className="muted">{l.openYear !== NEVER_YEAR ? l.openYear : ""}{l.closeYear !== NEVER_YEAR ? `–${l.closeYear}` : ""}{l.km != null ? ` · ${fmtKm(l.km)} km` : ""}</span>
            </li>
          ))}
        </ul>
        <div className="actions">{share}</div>
        <p className="credit">Lines that pass the project&apos;s metro definition only; suburban and commuter rail, trams and monorails are left out.</p>
      </div>
    </>
  );
}
