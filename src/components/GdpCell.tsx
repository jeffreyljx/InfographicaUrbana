/** Money for the GDP columns: $1.38T / $268B / $9.0B, with the data year as a small tag when it is not the latest. */
export interface GdpLite { usd: number | null; ppp: number | null; year: number; tip: string; area?: boolean }

export const LATEST_GDP_YEAR = 2025;

export function fmtMoney(v: number): string {
  const [d, s] = v >= 1e12 ? [1e12, "T"] : v >= 1e9 ? [1e9, "B"] : [1e6, "M"];
  const x = v / d;
  return "$" + (x >= 100 ? x.toFixed(0) : x >= 10 ? x.toFixed(1) : x.toFixed(2)) + s;
}

export default function GdpCell({ g, kind }: { g: GdpLite | null | undefined; kind: "usd" | "ppp" }) {
  const v = g?.[kind];
  if (!g || v == null) return <td className="num muted" title="No GDP figure for this area">–</td>;
  return (
    <td className="num gdp" title={g.tip}>
      {fmtMoney(v)}{g.area && <span className="gdp-area" aria-label=" (figure for a larger area that contains the city)">†</span>}
      {g.year !== LATEST_GDP_YEAR && <span className="gdp-yr">{"’" + String(g.year).slice(2)}</span>}
    </td>
  );
}
