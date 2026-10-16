/** Horizontal bar chart for the Industry and Exports page, drawn on the server: one row per place, a bar made of one or
 *  more segments with its value just past its end, a round scale with gridlines, and the full figures in each row's tooltip.
 *  A bar longer than the scale (Cork's output per worker) is cut with a break mark. */

export interface Bar {
  label: string;
  href?: string | null;
  tag?: string;                       // small line under the label: a caveat, or a year other than the chart's
  segs: { v: number; cls: string }[];
  value: string;
  title: string;                      // tooltip
  hollow?: boolean;                   // an upper bound, drawn as an outline
}

export default function IndustryBars({ rows, top, step, tick, label }: {
  rows: Bar[]; top: number; step: number; tick: (v: number) => string; label: string;
}) {
  const n = Math.round(top / step);
  return (
    <figure className="ibars" aria-label={label} style={{ "--n": n } as React.CSSProperties}>
      <ol>
        {rows.map((r, i) => {
          let used = 0;
          const off = r.segs.reduce((s, x) => s + x.v, 0) > top;
          return (
            <li key={i} title={r.title}>
              <span className="ib-lab">
                {r.href ? <a className="place" href={r.href}>{r.label}</a> : <span className="place">{r.label}</span>}
                {r.tag && <small>{r.tag}</small>}
              </span>
              <span className={"ib-track" + (off ? " off" : "")}>
                {r.segs.map((s, k) => {
                  const v = Math.max(0, Math.min(s.v, top - used));
                  used += v;
                  return <i key={k} className={s.cls + (r.hollow ? " hollow" : "")} style={{ width: `${(v / top) * 100}%` }} />;
                })}
                <span className="ib-val">{r.value}</span>
              </span>
            </li>
          );
        })}
        <li className="ib-axis" aria-hidden="true">
          <span />
          <span className="ib-ticks">
            {Array.from({ length: n + 1 }, (_, k) => <span key={k} style={{ left: `${(k / n) * 100}%` }}>{tick(k * step)}</span>)}
          </span>
          <span />
        </li>
      </ol>
    </figure>
  );
}
