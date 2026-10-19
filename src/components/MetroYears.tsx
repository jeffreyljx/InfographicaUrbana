"use client";
import { useEffect, useRef, useState, type PointerEvent } from "react";
import { fmtKm } from "@/lib/metro";
import CapsuleMin, { useCapsuleMin } from "./CapsuleMin";

/** Play speed: a year with more new line stays up longer. */
const delayFor = (km: number) => km <= 0 ? 70 : km < 50 ? 150 : km < 200 ? 220 : 300;
const BAR_H = 40;

interface Props {
  first: number;
  last: number;
  year: number;
  onYear: (y: number) => void;
  /** km of line opened per year, first..last (net of closures) */
  perYear: number[];
  /** km of line open in `year`, and in how many cities */
  kmOpen: number;
  systemsOpen: number;
  /** the longest stretch opened in `year` */
  newest: { line: number; name: string; city: string; colour: string } | null;
  onPickLine: (line: number) => void;
  /** a system is picked: the facts are its own */
  scope: string | null;
  /** where Play starts over from once it has reached the last year (the picked system's first year) */
  playFrom?: number;
  panelOpen: boolean;
}

/**
 * The metro map's year dock, like the tower map's time capsule: the chosen year, a bar chart of the km of metro opened
 * each year with a slider under it (bars up to the chosen year filled), and Play, which walks forward a year at a time.
 * The bar button at its top right collapses it to a short bar (Play, the year and the km), remembered in this browser.
 */
export default function MetroYears({ first, last, year, onYear, perYear, kmOpen, systemsOpen, newest, onPickLine, scope, playFrom, panelOpen }: Props) {
  const [playing, setPlaying] = useState(false);
  const [min, setMin] = useCapsuleMin("scrapermap.metro-dock");
  const span = Math.max(1, last - first);
  const max = Math.max(1, ...perYear);
  const added = perYear[year - first] ?? 0;

  useEffect(() => {
    if (!playing) return;
    if (year >= last) { setPlaying(false); return; }
    const t = setTimeout(() => onYear(year + 1), delayFor(perYear[year - first] ?? 0));
    return () => clearTimeout(t);
  }, [playing, year, last, first, perYear, onYear]);

  const play = () => {
    if (playing) { setPlaying(false); return; }
    if (year >= last) onYear(Math.max(first, Math.min(last - 1, playFrom ?? first)));
    setPlaying(true);
  };
  const pick = (y: number) => { setPlaying(false); onYear(Math.min(last, Math.max(first, y))); };

  const dock = useRef<HTMLElement>(null);
  useEffect(() => {
    const el = dock.current, app = el?.parentElement;
    if (!el || !app || typeof ResizeObserver === "undefined") return;
    const ro = new ResizeObserver(() => app.style.setProperty("--capsule-h", `${el.offsetHeight}px`));
    ro.observe(el);
    return () => { ro.disconnect(); app.style.removeProperty("--capsule-h"); };
  }, []);

  const chart = useRef<SVGSVGElement>(null);
  const fromPointer = (e: PointerEvent<SVGSVGElement>) => {
    const r = chart.current!.getBoundingClientRect();
    pick(first + Math.round(((e.clientX - r.left) / r.width) * span));
  };
  const ticks: number[] = [];
  for (let y = Math.ceil(first / 20) * 20; y <= last; y += 20) ticks.push(y);
  const pct = (y: number) => `${((y - first) / span) * 100}%`;
  const where = scope ?? (systemsOpen === 1 ? "1 city" : `${systemsOpen.toLocaleString("en-US")} cities`);

  return (
    <section ref={dock} className={"capsule metro-dock" + (panelOpen ? " with-panel" : "") + (min ? " min" : "")} aria-label="Metro networks by year">
      <div className="cap-head">
        <button className="cap-play" onClick={play} aria-label={playing ? "Pause" : year >= last ? "Play from " + (playFrom ?? first) : "Play"} title={playing ? "Pause" : "Play through the years"}>
          <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">
            {playing ? <path d="M4 2.5h3v11H4zM9 2.5h3v11H9z" fill="currentColor" /> : <path d="M4.5 2.2v11.6L13.6 8z" fill="currentColor" />}
          </svg>
        </button>
        <div className="cap-year" title="The metro lines open in this year, each stretch drawn from the year it opened">{year}</div>
        <div className="cap-facts">
          <div><b>{fmtKm(kmOpen)} km</b> of metro {kmOpen > 0 ? <>in {scope ? <span className="place">{where}</span> : where}</> : null} by {year}{added > 0.05 && <span className="cap-new"> · {fmtKm(added)} km new</span>}</div>
          {newest && !min && (
            <div className="cap-tallest">Opened: <button className="link" onClick={() => onPickLine(newest.line)}><i className="m-sw" style={{ background: newest.colour }} />{newest.name}</button>, <span className="place">{newest.city}</span></div>
          )}
        </div>
        <CapsuleMin min={min} onToggle={() => setMin(!min)} what="year dock" />
      </div>
      {!min && <div className="cap-track">
        <svg ref={chart} className="cap-bars" viewBox={`0 0 ${span} ${BAR_H}`} preserveAspectRatio="none" height={BAR_H}
          onPointerDown={e => { e.currentTarget.setPointerCapture(e.pointerId); fromPointer(e); }}
          onPointerMove={e => { if (e.buttons === 1) fromPointer(e); }} aria-hidden="true">
          {perYear.map((c, i) => c > 0.05 && (
            <rect key={i} x={i - 0.38} width={0.76} y={BAR_H - Math.max(1.5, (c / max) * BAR_H)} height={Math.max(1.5, (c / max) * BAR_H)}
              className={first + i === year ? "now" : first + i < year ? "past" : "future"} />
          ))}
        </svg>
        <input type="range" min={first} max={last} step={1} value={year} onChange={e => pick(Number(e.target.value))}
          aria-label="Year" aria-valuetext={`${year}: ${fmtKm(kmOpen)} km of metro`} />
        <div className="cap-ticks" aria-hidden="true">
          {ticks.map(t => <span key={t} style={{ left: pct(t) }}>{t}</span>)}
        </div>
      </div>}
    </section>
  );
}
