"use client";
import { useState, type PointerEvent } from "react";

/**
 * The line over a time dock's bar chart that says what its bars count (Jeffrey, 4 Nov 2026: "on each time capsule
 * toggle, indicate what the vertical bars mean"), with a reading on the right: the bar under the pointer, or else the
 * tallest bar, which gives the chart its scale. The tooltip says the rest. Used by ScraperMap's time capsule
 * (TimeCapsule.tsx), TransitMap's year dock (MetroYears.tsx) and CartaHistoria's (HistoryYears.tsx).
 */
export default function BarsKey({ what, read, title }: { what: React.ReactNode; read: React.ReactNode; title: string }) {
  return (
    <div className="cap-key" title={title}>
      <span className="cap-key-what"><i aria-hidden="true" />{what}</span>
      <span className="cap-key-read">{read}</span>
    </div>
  );
}

/**
 * Where the pointer is over the chart, as a fraction of its width from 0 to 1 (null when it is elsewhere). A mouse
 * reads a bar by hovering; a finger reads the bar it drags across, since that bar is also the year it picks.
 */
export function useChartHover(): [number | null, { onPointerMove: (e: PointerEvent<SVGSVGElement>) => void; onPointerLeave: () => void }] {
  const [at, setAt] = useState<number | null>(null);
  return [at, {
    onPointerMove: e => {
      const r = e.currentTarget.getBoundingClientRect();
      setAt(Math.min(1, Math.max(0, (e.clientX - r.left) / r.width)));
    },
    onPointerLeave: () => setAt(null),
  }];
}

/** The tallest bar: its index and value. */
export function peakOf(values: ArrayLike<number>): { i: number; v: number } {
  let i = 0;
  for (let k = 1; k < values.length; k++) if (values[k] > values[i]) i = k;
  return { i, v: values[i] ?? 0 };
}
