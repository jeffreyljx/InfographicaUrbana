import Shell from "./Shell";
import GuideVideo from "./GuideVideo";
import type { NavKey } from "./Nav";
import "./guide.css";

/**
 * The pieces of a mode's guide (Jeffrey, 4 Nov 2026: for each mode "a brief home or landing page that explains in a few
 * brief paragraphs, and/or demos of how to use the map, what each map allows you to see and play with"). The pages are
 * /guide/ (ScraperMap), /metro/guide/, /industry/guide/ and /history/guide/; the clips and dock pictures in
 * public/guide/ are recorded from the maps by scripts/guide/capture.mjs.
 */

export function GuidePage({ active, foot, children }: { active: NavKey; foot?: React.ReactNode; children: React.ReactNode }) {
  return <Shell active={active} foot={foot}><article className="guide">{children}</article></Shell>;
}

export function GuideHead({ name, lead, children }: { name: string; lead: React.ReactNode; children: React.ReactNode }) {
  return (
    <header className="g-head">
      <p className="g-kicker">Guide</p>
      <h1>{name}</h1>
      <p className="lead">{lead}</p>
      <div className="heroactions">{children}</div>
    </header>
  );
}

/** The demo clip, public/guide/<name>.mp4 with its first frame as the poster. */
export function Demo({ name, w, h, label, children }: { name: string; w: number; h: number; label: string; children: React.ReactNode }) {
  return (
    <figure className="g-demo">
      <GuideVideo src={`/guide/${name}.mp4`} poster={`/guide/${name}.jpg`} w={w} h={h} label={label} />
      <figcaption>{children}</figcaption>
    </figure>
  );
}

export function Steps({ children }: { children: React.ReactNode }) {
  return <ol className="g-steps">{children}</ol>;
}
export function Step({ title, children }: { title: string; children: React.ReactNode }) {
  return <li><b>{title}</b> {children}</li>;
}

/** A picture of the year dock with numbered pins on its parts (positions measured when it was recorded), and the key. */
export interface Part { x: number; y: number; text: React.ReactNode }
/** The parts in the order given, placed where the recording measured them (src/lib/guideMedia.json); a part it didn't find is left out. */
export function placeParts(at: Record<string, number[]>, list: [string, React.ReactNode][]): Part[] {
  return list.flatMap(([k, text]) => at[k] ? [{ x: at[k][0], y: at[k][1], text }] : []);
}
export function DockParts({ img, w, h, alt, parts }: { img: string; w: number; h: number; alt: string; parts: Part[] }) {
  return (
    <figure className="g-dock">
      <div className="g-dock-pic">
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img src={img} width={w} height={h} alt={alt} loading="lazy" />
        {parts.map((p, i) => <span key={i} className="g-pin" style={{ left: `${p.x * 100}%`, top: `${p.y * 100}%` }} aria-hidden="true">{i + 1}</span>)}
      </div>
      <ol className="g-parts">{parts.map((p, i) => <li key={i}>{p.text}</li>)}</ol>
    </figure>
  );
}

/**
 * The dock's bars drawn large, from the same data, with a scale: each bar at x (0 to 1 across the slider) and w wide;
 * heights in proportion to the value, or to its square root where the dock uses one.
 */
export interface Bar { x: number; w: number; v: number }
export function BarsFigure({ bars, top, topLabel, ticks, peak, sqrt = false, label, children }: {
  bars: Bar[]; top: number; topLabel: string; ticks: { x: number; label: string; wide?: boolean }[];
  peak?: { x: number; label: string }; sqrt?: boolean; label: string; children: React.ReactNode;
}) {
  const H = 100, W = 1000;
  const hOf = (v: number) => v <= 0 ? 0 : Math.max(0.8, (sqrt ? Math.sqrt(v / top) : v / top) * H);
  const pk = peak ? Math.min(0.9, Math.max(0.1, peak.x)) : 0;
  return (
    <figure className="g-bars" aria-label={label}>
      <div className="g-bars-plot">
        <span className="g-bars-y g-top">{topLabel}</span>
        <span className="g-bars-y g-zero">0</span>
        <svg viewBox={`0 0 ${W} ${H}`} preserveAspectRatio="none" aria-hidden="true">
          <line x1="0" x2={W} y1="0.5" y2="0.5" className="g-grid" />
          {bars.map((b, i) => {
            const h = hOf(b.v);
            if (!h) return null;
            const w = Math.max(1.2, b.w * W * 0.76);
            return <rect key={i} x={(b.x + b.w / 2) * W - w / 2} width={w} y={H - h} height={h} />;
          })}
        </svg>
        {peak && <span className="g-peak" style={{ left: `${pk * 100}%` }}>{peak.label}</span>}
      </div>
      <div className="g-ticks" aria-hidden="true">{ticks.map(t => <span key={t.label} className={t.wide ? "wide" : undefined} style={{ left: `${t.x * 100}%` }}>{t.label}</span>)}</div>
      <figcaption>{children}</figcaption>
    </figure>
  );
}

/** Links that open the map on a particular view. */
export function TryList({ items }: { items: { href: string; title: string; note: string }[] }) {
  return (
    <ul className="g-try">
      {items.map(it => <li key={it.href}><a href={it.href}><b>{it.title}</b><span>{it.note}</span></a></li>)}
    </ul>
  );
}
