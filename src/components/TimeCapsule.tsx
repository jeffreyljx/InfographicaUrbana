"use client";
import { useEffect, useRef, useState, type PointerEvent } from "react";
import { fmtHeight } from "@/lib/format";
import CapsuleMin, { useCapsuleMin } from "./CapsuleMin";
import BarsKey, { useChartHover, peakOf } from "./BarsKey";

/** Play speed: how long a year stays up before the next one, longer when more towers were completed in it. */
const delayFor = (added: number) => added === 0 ? 70 : added < 100 ? 160 : 240;
const BAR_H = 40;

interface Props {
  first: number;
  last: number;
  year: number;
  onYear: (y: number) => void;
  onClose: () => void;
  /** Completions per year, first..last, for the towers the other filters let through. */
  perYear: number[];
  /** Towers standing in `year`. */
  shown: number;
  /** Names of the towers that came down in `year`. */
  lost: string[];
  tallest: { id: number; name: string; height: number; city: string } | null;
  onPick: (id: number) => void;
  /** The tower panel is open on the right: keep clear of it. */
  panelOpen: boolean;
  /** The city (or "district, city") the filters narrow the map to, named in the bars' key. */
  scope?: string | null;
}

/**
 * The time capsule's dock: the chosen year, a bar chart of completions per year with a slider under it
 * (the bars up to the chosen year are filled, and a line over them says what they count), and Play, which walks forward one year at a time. The bar button at its
 * top right collapses it to a short bar (Play, the year and the count), which stays collapsed until opened again.
 */
export default function TimeCapsule({ first, last, year, onYear, onClose, perYear, shown, lost, tallest, onPick, panelOpen, scope }: Props) {
  const [playing, setPlaying] = useState(false);
  const [min, setMin] = useCapsuleMin();
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
    if (year >= last) onYear(first);
    setPlaying(true);
  };
  const pick = (y: number) => { setPlaying(false); onYear(Math.min(last, Math.max(first, y))); };

  // the dock's height, as --capsule-h on the map app, so the map's corner controls can sit above it on a phone
  const dock = useRef<HTMLElement>(null);
  useEffect(() => {
    const el = dock.current, app = el?.parentElement;
    if (!el || !app || typeof ResizeObserver === "undefined") return;
    const ro = new ResizeObserver(() => app.style.setProperty("--capsule-h", `${el.offsetHeight}px`));
    ro.observe(el);
    return () => { ro.disconnect(); app.style.removeProperty("--capsule-h"); };
  }, []);

  // the chart: bar i is centred where the slider's thumb stands for year first + i; click or drag on it to choose a year
  const chart = useRef<SVGSVGElement>(null);
  const fromPointer = (e: PointerEvent<SVGSVGElement>) => {
    const r = chart.current!.getBoundingClientRect();
    pick(first + Math.round(((e.clientX - r.left) / r.width) * span));
  };

  const ticks: number[] = [];
  for (let y = Math.ceil(first / 20) * 20; y <= last; y += 20) ticks.push(y);
  const pct = (y: number) => `${((y - first) / span) * 100}%`;

  // the bars' key: the bar under the pointer, else the year with the most completions
  const [at, hoverProps] = useChartHover();
  const peak = peakOf(perYear);
  const towers = (n: number) => `${n.toLocaleString("en-US")} ${n === 1 ? "tower" : "towers"}`;
  const hy = at === null ? null : first + Math.round(at * span);
  const read = hy !== null ? <><b>{hy}</b>: {towers(perYear[hy - first] ?? 0)}</> : peak.v > 0 ? <>Peak: {towers(peak.v)} in {first + peak.i}</> : null;

  return (
    <section ref={dock} className={"capsule" + (panelOpen ? " with-panel" : "") + (min ? " min" : "")} aria-label="Time capsule">
      <div className="cap-head">
        <button className="cap-play" onClick={play} aria-label={playing ? "Pause" : year >= last ? "Play from " + first : "Play"} title={playing ? "Pause" : "Play through the years"}>
          <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">
            {playing ? <path d="M4 2.5h3v11H4zM9 2.5h3v11H9z" fill="currentColor" /> : <path d="M4.5 2.2v11.6L13.6 8z" fill="currentColor" />}
          </svg>
        </button>
        <div className="cap-year" title="Each tower is shown from the year it was completed until the year it came down, if it has">{year}</div>
        <div className="cap-facts">
          <div>
            <b>{shown.toLocaleString("en-US")}</b> {shown === 1 ? "tower" : "towers"} standing in {year}
            {added > 0 && <span className="cap-new"> · {added.toLocaleString("en-US")} new</span>}
            {lost.length > 0 && <span className="cap-lost" title={lost.join(", ")}> · {lost.length} lost</span>}
          </div>
          {tallest && !min && (
            <div className="cap-tallest">Tallest: <button className="link" onClick={() => onPick(tallest.id)}>{tallest.name}</button>, {fmtHeight(tallest.height)}, <span className="place">{tallest.city}</span></div>
          )}
        </div>
        <CapsuleMin min={min} onToggle={() => setMin(!min)} what="time capsule" />
        <button className="x" onClick={onClose} aria-label="Close the time capsule">×</button>
      </div>
      {!min && <div className="cap-track">
        <BarsKey what={<>Towers completed each year{scope && <> in <span className="place">{scope}</span></>}</>} read={read}
          title="Each bar is one year: how many of the towers on the map (150 m or taller, after any filters) were completed that year, including the lost ones since demolished. Bars up to the chosen year are filled, and the chosen year's is orange." />
        <svg ref={chart} className="cap-bars" viewBox={`0 0 ${span} ${BAR_H}`} preserveAspectRatio="none" height={BAR_H}
          onPointerDown={e => { e.currentTarget.setPointerCapture(e.pointerId); fromPointer(e); }}
          onPointerMove={e => { hoverProps.onPointerMove(e); if (e.buttons === 1) fromPointer(e); }} onPointerLeave={hoverProps.onPointerLeave} aria-hidden="true">
          {perYear.map((c, i) => c > 0 && (
            <rect key={i} x={i - 0.38} width={0.76} y={BAR_H - Math.max(1.5, (c / max) * BAR_H)} height={Math.max(1.5, (c / max) * BAR_H)}
              className={first + i === year ? "now" : first + i < year ? "past" : "future"} />
          ))}
        </svg>
        <input type="range" min={first} max={last} step={1} value={year} onChange={e => pick(Number(e.target.value))}
          aria-label="Year" aria-valuetext={`${year}: ${shown.toLocaleString("en-US")} towers`} />
        <div className="cap-ticks" aria-hidden="true">
          {ticks.map(t => <span key={t} style={{ left: pct(t) }}>{t}</span>)}
        </div>
      </div>}
    </section>
  );
}
