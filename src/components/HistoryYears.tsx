"use client";
import { useEffect, useMemo, useRef, useState, type PointerEvent, type KeyboardEvent } from "react";
import CapsuleMin, { useCapsuleMin } from "./CapsuleMin";
import { fmtYear, posToYear, yearToPos, YEAR_TICKS, FIRST_YEAR, LAST_YEAR, fmtArea, undated, type Caption } from "@/lib/history";

const BAR_H = 40;
const BINS = 320;
const SPEEDS = [1, 3, 10];

interface Props {
  year: number;
  onYear: (y: number) => void;
  /** cells whose owner or status changed, per year from FIRST_YEAR */
  changed: number[];
  /** the year's captions, biggest state first, with the state's name and colour */
  captions: (Caption & { name: string; colour: string })[];
  /** states holding land in the year, and their land */
  statesAlive: number;
  cellsHeld: number;
  /** false while the year's window is still loading: Play waits for it */
  ready: boolean;
  onPickState: (owner: number) => void;
  panelOpen: boolean;
}

/**
 * CartaHistoria's year dock, the metro map's dock adapted: the year, a chart of how much land changed hands each year
 * over a slider that runs slower before 1500 (so the last five centuries are not a sliver of eight thousand years), and
 * Play, which steps from one year with a change to the next, lingering on years with more change and on captioned
 * events. The year's captions sit under the year. The bar button collapses it to a short bar.
 */
export default function HistoryYears({ year, onYear, changed, captions, statesAlive, cellsHeld, ready, onPickState, panelOpen }: Props) {
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(0);
  const [min, setMin] = useCapsuleMin("infographica.history-dock");

  /** the years with any change, for Play to step through */
  const steps = useMemo(() => {
    const out: number[] = [];
    changed.forEach((v, i) => { if (v > 0) out.push(FIRST_YEAR + i); });
    return out;
  }, [changed]);
  const nextYear = (y: number) => {
    let lo = 0, hi = steps.length;
    while (lo < hi) { const m = (lo + hi) >> 1; if (steps[m] <= y) lo = m + 1; else hi = m; }
    return lo < steps.length ? steps[lo] : LAST_YEAR;
  };

  useEffect(() => {
    if (!playing || !ready) return;
    if (year >= LAST_YEAR) { setPlaying(false); return; }
    const c = changed[year - FIRST_YEAR] ?? 0;
    const delay = (90 + Math.min(420, 2.4 * Math.sqrt(c)) + (captions.length ? 380 : 0)) / SPEEDS[speed];
    const t = setTimeout(() => onYear(nextYear(year)), delay);
    return () => clearTimeout(t);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [playing, ready, year, captions.length, speed]);

  const play = () => {
    if (playing) { setPlaying(false); return; }
    if (year >= LAST_YEAR) onYear(FIRST_YEAR);
    setPlaying(true);
  };
  const pick = (y: number) => { setPlaying(false); onYear(Math.min(LAST_YEAR, Math.max(FIRST_YEAR, y))); };

  const dock = useRef<HTMLElement>(null);
  useEffect(() => {
    const el = dock.current, app = el?.parentElement;
    if (!el || !app || typeof ResizeObserver === "undefined") return;
    const ro = new ResizeObserver(() => app.style.setProperty("--capsule-h", `${el.offsetHeight}px`));
    ro.observe(el);
    return () => { ro.disconnect(); app.style.removeProperty("--capsule-h"); };
  }, []);

  // the chart: land changed per bin of the slider (square root, so the world wars don't flatten everything else)
  const bars = useMemo(() => {
    const v = new Float64Array(BINS);
    changed.forEach((c, i) => { if (c) v[Math.min(BINS - 1, Math.floor(yearToPos(FIRST_YEAR + i) * BINS))] += c; });
    const m = Math.max(1, ...Array.from(v, x => Math.sqrt(x)));
    let d = "";
    v.forEach((x, i) => {
      if (!x) return;
      const hgt = Math.max(1.5, (Math.sqrt(x) / m) * BAR_H);
      d += `M${i + 0.12} ${BAR_H}V${(BAR_H - hgt).toFixed(1)}h0.76V${BAR_H}z`;
    });
    return d;
  }, [changed]);
  const nowX = yearToPos(year) * BINS;

  const chart = useRef<SVGSVGElement>(null);
  const fromPointer = (e: PointerEvent<SVGSVGElement>) => {
    const r = chart.current!.getBoundingClientRect();
    pick(posToYear(Math.min(1, Math.max(0, (e.clientX - r.left) / r.width))));
  };
  const keys = (e: KeyboardEvent<HTMLInputElement>) => {
    const step = e.shiftKey ? 10 : 1;
    if (e.key === "ArrowLeft" || e.key === "ArrowDown") { e.preventDefault(); pick(year - step); }
    else if (e.key === "ArrowRight" || e.key === "ArrowUp") { e.preventDefault(); pick(year + step); }
    else if (e.key === "PageDown") { e.preventDefault(); pick(year - 100); }
    else if (e.key === "PageUp") { e.preventDefault(); pick(year + 100); }
  };
  const first = captions[0];
  const yearLabel = year < 0 ? <>{-year}<small> BCE</small></> : year < 1000 ? <>{year}<small> CE</small></> : <>{year}</>;

  return (
    <section ref={dock} className={"capsule metro-dock h-dock" + (panelOpen ? " with-panel" : "") + (min ? " min" : "")} aria-label="Borders by year">
      <div className="cap-head">
        <button className="cap-play" onClick={play} aria-label={playing ? "Pause" : year >= LAST_YEAR ? "Play from 6000 BCE" : "Play"} title={playing ? "Pause" : "Play through the years"}>
          <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">
            {playing ? <path d="M4 2.5h3v11H4zM9 2.5h3v11H9z" fill="currentColor" /> : <path d="M4.5 2.2v11.6L13.6 8z" fill="currentColor" />}
          </svg>
        </button>
        <div className="cap-year h-year" title="The borders at the end of this year">{yearLabel}</div>
        <div className="cap-facts">
          <div><b>{statesAlive.toLocaleString("en-US")} states</b> hold {fmtArea(cellsHeld)}{!ready && <span className="muted"> · loading…</span>}</div>
          {first && (
            <div className="cap-tallest h-cap">
              <button className="link" onClick={() => onPickState(first.s)} title={first.x}><i className="m-sw" style={{ background: first.colour }} />{first.name}</button>{" "}
              <span className="h-cap-text">{undated(first.x)}</span>
              {captions.length > 1 && <span className="muted"> · +{captions.length - 1} more</span>}
            </div>
          )}
        </div>
        {!min && (
          <button className="x cap-speed" onClick={() => setSpeed((speed + 1) % SPEEDS.length)} title="Play speed" aria-label={`Play speed ${SPEEDS[speed]}×`}>
            {SPEEDS[speed]}×
          </button>
        )}
        <CapsuleMin min={min} onToggle={() => setMin(!min)} what="year dock" />
      </div>
      {!min && captions.length > 1 && (
        <ul className="h-caps">
          {captions.slice(1, 3).map((c, i) => (
            <li key={i}><button className="link" onClick={() => onPickState(c.s)}><i className="m-sw" style={{ background: c.colour }} />{c.name}</button> <span className="h-cap-text">{undated(c.x)}</span></li>
          ))}
        </ul>
      )}
      {!min && <div className="cap-track">
        <svg ref={chart} className="cap-bars" viewBox={`0 0 ${BINS} ${BAR_H}`} preserveAspectRatio="none" height={BAR_H}
          onPointerDown={e => { e.currentTarget.setPointerCapture(e.pointerId); fromPointer(e); }}
          onPointerMove={e => { if (e.buttons === 1) fromPointer(e); }} aria-hidden="true">
          <defs><clipPath id="h-past"><rect x="0" y="0" width={nowX} height={BAR_H} /></clipPath></defs>
          <path d={bars} className="h-bars-future" />
          <path d={bars} className="h-bars-past" clipPath="url(#h-past)" />
          <rect x={nowX - 0.6} width={1.2} y={0} height={BAR_H} className="h-now" />
        </svg>
        <input type="range" min={0} max={10000} step={1} value={Math.round(yearToPos(year) * 10000)} onChange={e => pick(posToYear(Number(e.target.value) / 10000))}
          onKeyDown={keys} aria-label="Year" aria-valuetext={fmtYear(year)} />
        <div className="cap-ticks" aria-hidden="true">
          {YEAR_TICKS.map(t => <span key={t} style={{ left: `${yearToPos(t) * 100}%` }} className={t === FIRST_YEAR ? "first" : t === 1600 || t === 1700 || t === 1900 ? "minor" : undefined}>{t < 0 ? `${-t} BCE` : t}</span>)}
        </div>
      </div>}
    </section>
  );
}
