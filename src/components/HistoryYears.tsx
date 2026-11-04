"use client";
import { useEffect, useMemo, useRef, useState, type PointerEvent, type KeyboardEvent } from "react";
import CapsuleMin, { useCapsuleMin } from "./CapsuleMin";
import BarsKey, { useChartHover, peakOf } from "./BarsKey";
import { fmtYear, posToYear, yearToPos, YEAR_TICKS, FIRST_YEAR, LAST_YEAR, fmtArea, undated, type Caption } from "@/lib/history";

const BAR_H = 40;
const BINS = 320;
const SPEEDS = [1, 3, 10];
/** the first tick sits flush left; minor ticks are fainter; on a phone only 6000 BCE, 0, 1500, 1800 and 2000 are labelled */
/** the chart's bar (one of BINS along the slider) that holds a year */
const binOf = (y: number) => Math.min(BINS - 1, Math.floor(yearToPos(y) * BINS));
/** a bar's years: "1912–1915", "450–467 CE", "2104–2001 BCE", "21 BCE–3 CE" */
const yearsOf = (a: number, b: number) => a === b ? fmtYear(a, true) : b < 0 ? `${-a}–${-b} BCE` : a < 0 ? `${-a} BCE–${b} CE` : b < 1000 ? `${a}–${b} CE` : `${a}–${b}`;
const tickClass = (t: number) => [t === FIRST_YEAR && "first", (t === 1600 || t === 1700 || t === 1900) && "minor", ![FIRST_YEAR, 0, 1500, 1800, 2000].includes(t) && "wide"].filter(Boolean).join(" ") || undefined;

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
 * (a line over it says so, with the bar under the pointer) over a slider that runs slower before 1500 (so the last five centuries are not a sliver of eight thousand years), and
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

  // the chart: land changed per bin of the slider (square root, so the world wars don't flatten everything else), and
  // each bin's first and last year for the key
  const { bars, binCells, binFrom, binTo } = useMemo(() => {
    const v = new Float64Array(BINS), from = new Int32Array(BINS).fill(LAST_YEAR), to = new Int32Array(BINS).fill(FIRST_YEAR);
    for (let y = FIRST_YEAR; y <= LAST_YEAR; y++) { const b = binOf(y); from[b] = Math.min(from[b], y); to[b] = Math.max(to[b], y); }
    changed.forEach((c, i) => { if (c) v[binOf(FIRST_YEAR + i)] += c; });
    const m = Math.max(1, ...Array.from(v, x => Math.sqrt(x)));
    let d = "";
    v.forEach((x, i) => {
      if (!x) return;
      const hgt = Math.max(1.5, (Math.sqrt(x) / m) * BAR_H);
      d += `M${i + 0.12} ${BAR_H}V${(BAR_H - hgt).toFixed(1)}h0.76V${BAR_H}z`;
    });
    return { bars: d, binCells: v, binFrom: from, binTo: to };
  }, [changed]);
  const [at, hoverProps] = useChartHover();
  const peak = peakOf(binCells);
  const hb = at === null ? null : Math.min(BINS - 1, Math.floor(at * BINS));
  const area = (cells: number) => fmtArea(cells).replace(" million", "m");   // "51.3m km²": the key's line is short
  const read = hb !== null
    ? <><b>{yearsOf(binFrom[hb], binTo[hb])}</b>: {binCells[hb] ? area(binCells[hb]) : "no change"}</>
    : peak.v > 0 ? <>Peak: {area(peak.v)} in {yearsOf(binFrom[peak.i], binTo[peak.i])}</> : null;
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
        <BarsKey what="Land that changed hands" read={read}
          title="Each bar is a stretch of years (about a century before 1000 BCE, 17 years from then to 1500, and 4 years since, as the slider runs faster there): how much land changed owner or status (became a vassal, was occupied or fought over) in it. Heights are on a square-root scale, so the world wars don't flatten the rest. Bars up to the chosen year are filled, and an orange line marks it." />
        <svg ref={chart} className="cap-bars" viewBox={`0 0 ${BINS} ${BAR_H}`} preserveAspectRatio="none" height={BAR_H}
          onPointerDown={e => { e.currentTarget.setPointerCapture(e.pointerId); fromPointer(e); }}
          onPointerMove={e => { hoverProps.onPointerMove(e); if (e.buttons === 1) fromPointer(e); }} onPointerLeave={hoverProps.onPointerLeave} aria-hidden="true">
          <defs><clipPath id="h-past"><rect x="0" y="0" width={nowX} height={BAR_H} /></clipPath></defs>
          <path d={bars} className="h-bars-future" />
          <path d={bars} className="h-bars-past" clipPath="url(#h-past)" />
          <rect x={nowX - 0.6} width={1.2} y={0} height={BAR_H} className="h-now" />
        </svg>
        <input type="range" min={0} max={10000} step={1} value={Math.round(yearToPos(year) * 10000)} onChange={e => pick(posToYear(Number(e.target.value) / 10000))}
          onKeyDown={keys} aria-label="Year" aria-valuetext={fmtYear(year)} />
        <div className="cap-ticks" aria-hidden="true">
          {YEAR_TICKS.map(t => <span key={t} style={{ left: `${yearToPos(t) * 100}%` }} className={tickClass(t)}>{t < 0 ? `${-t} BCE` : t}</span>)}
        </div>
      </div>}
    </section>
  );
}
