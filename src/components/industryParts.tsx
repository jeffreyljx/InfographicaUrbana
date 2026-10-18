import type { Bar } from "@/components/IndustryBars";
import {
  FX, money, citySlug, tag, region, mapKey,
  type TradeRow, type ExportRow, type MfgRow, type CountryTrade, type CountryMfg,
} from "@/lib/industry";

/** What the two IndustryMap pages of figures (Exports and imports, Industrial output) share: the bars' rows, the
 *  links from a name to its city or country, and the exchange-rate table. */

export const usd = (v: number) => `$${v.toLocaleString("en-US")}bn`;
/** A scale's tick: 0, $500bn, $1.5tn. */
export const tickMoney = (v: number) => v === 0 ? "0" : v >= 1000 ? `$${+(v / 1000).toFixed(2)}tn` : usd(v);
export const find = <T extends { place: string }>(rows: T[], place: string) => rows.find(r => r.place === place) as T;
export const sentence = (...parts: (string | null | undefined | false)[]) => parts.filter(Boolean).join(". ").replace(/\.\./g, ".") + ".";
export const href = (place: string) => { const s = citySlug(place); return s ? `/city/${s}/` : null; };
export const how = (r: { unit: string; basis: string }) => [r.unit, r.basis].filter(Boolean).join(" · ");
/** A country's circle on the IndustryMap map, its panel open. */
export const countryMapHref = (country: string, show: "trade" | "output") =>
  `/industry/?${show === "output" ? "show=output&" : ""}by=country&place=${mapKey(country)}`;
const places = (n: number, word = "place") => `${n} ${word}${n === 1 ? "" : "s"}`;
const span = (ys: string[]) => ys.length > 1 ? `${ys[0]}–${ys[ys.length - 1]}` : ys[0] !== "2025" ? ys[0] : "";

export const tradeBar = (r: TradeRow): Bar => ({
  label: r.place, href: href(r.place), tag: tag(r.caveat, r.year),
  segs: r.exports_usd_bn != null && r.imports_usd_bn != null
    ? [{ v: r.exports_usd_bn, cls: "c-ex" }, { v: r.imports_usd_bn, cls: "c-im" }]
    : [{ v: r.total_usd_bn ?? 0, cls: "c-tot" }],
  value: money(r.total_usd_bn),
  title: sentence(
    `${r.place}, ${r.country}, ${r.year}: ` + [r.exports_usd_bn != null && `exports ${money(r.exports_usd_bn)}`, r.imports_usd_bn != null && `imports ${money(r.imports_usd_bn)}`, `total ${money(r.total_usd_bn)}`].filter(Boolean).join(", "),
    r.unit, r.basis, r.note),
});
export const exportBar = (r: ExportRow): Bar => ({
  label: r.place, href: href(r.place), tag: tag(r.caveat, r.year),
  segs: [{ v: r.exports_usd_bn, cls: "c-ex" }], value: money(r.exports_usd_bn),
  title: sentence(`${r.place}, ${r.country}, ${r.year}: exports ${money(r.exports_usd_bn)}`, r.unit, r.basis, r.note),
});
const isIndustrial = (r: MfgRow) => /^Industrial/.test(r.measure);
export const mfgBar = (r: MfgRow): Bar => ({
  label: r.place, href: href(r.place), hollow: r.upper_bound,
  tag: [r.year, r.upper_bound ? "upper bound" : isIndustrial(r) ? "industrial" : ""].filter(Boolean).join(", "),
  segs: [{ v: r.va_usd_bn, cls: `c-${region(r.country)}` }], value: money(r.va_usd_bn),
  title: sentence(`${r.place}, ${r.country}, ${r.year}: ${r.measure.toLowerCase()} ${r.upper_bound ? "up to " : ""}${money(r.va_usd_bn)}`, r.unit, r.note),
});

/** A country's bar: exports and imports of the places that publish both, then the totals of those that publish only a
 *  total; a country whose places publish only exports is drawn hollow at its exports. */
export const countryTradeBar = (c: CountryTrade): Bar => {
  const gate = c.parts.some(p => p.kind === "gateway");
  return {
    label: c.country, href: countryMapHref(c.country, "trade"),
    tag: [places(c.parts.length, gate ? "gateway" : "place"), c.total == null ? "exports only" : "", span(c.years)].filter(Boolean).join(", "),
    hollow: c.total == null,
    segs: c.total == null ? [{ v: c.ex, cls: "c-ex" }]
      : [{ v: c.exSplit, cls: "c-ex" }, { v: c.imSplit, cls: "c-im" }, ...(c.totalOnly ? [{ v: c.totalOnly, cls: "c-tot" }] : [])],
    value: money(c.total ?? c.ex),
    title: sentence(
      `${c.country}, the sum of ${places(c.parts.length)} on this page: ` +
        [c.ex && `exports ${money(c.ex)}`, c.im && `imports ${money(c.im)}`, c.total != null && `exports plus imports ${money(c.total)}`].filter(Boolean).join(", "),
      c.parts.map(p => p.place).join(", ")),
  };
};
/** A country's bar of value added: the figures published, then its cities' upper bounds drawn hollow. */
export const countryMfgBar = (c: CountryMfg): Bar => {
  const n = c.parts.filter(p => !p.inside).length;
  return {
    label: c.country, href: countryMapHref(c.country, "output"),
    tag: [places(n), c.upper ? `${money(c.upper)} upper bounds` : "", span(c.years)].filter(Boolean).join(", "),
    segs: [{ v: c.va - c.upper, cls: `c-${region(c.country)}` }, ...(c.upper ? [{ v: c.upper, cls: `c-${region(c.country)}`, hollow: true }] : [])],
    value: money(c.va),
    title: sentence(`${c.country}, the sum of ${places(n)} on this page: manufacturing value added ${money(c.va)}`,
      c.upper > 0 && `${money(c.upper)} of it upper bounds`, c.parts.filter(p => !p.inside).map(p => p.place).join(", ")),
  };
};

export function FxTable() {
  return (
    <>
      <h3>Exchange rates used</h3>
      <p className="ind-note">Federal Reserve annual averages (G.5A), units of each currency per US dollar, for the year each figure covers. Figures were gathered on 16 October 2026 from national, provincial and city statistics offices, customs agencies and port authorities; every row&apos;s sources are linked in the tables above.</p>
      <div className="tablewrap"><table className="itable fx">
        <thead><tr><th>Currency</th><th className="num">Year</th><th className="num">Per US$</th></tr></thead>
        <tbody>{FX.map(r => (
          <tr key={r.code + r.year}><td>{r.currency} <span className="muted">{r.code}</span></td><td className="num">{r.year}</td><td className="num">{r.per_usd.toLocaleString("en-US", { maximumFractionDigits: 4 })}</td></tr>
        ))}</tbody>
      </table></div>
    </>
  );
}

/** The links between the map and the two pages of figures, under each page's opening. */
export function IndustryLinks({ show }: { show: "trade" | "output" }) {
  return (
    <div className="heroactions">
      <a className="btn primary" href={show === "output" ? "/industry/?show=output" : "/industry/"}>See them on the map</a>
      {show === "trade"
        ? <a className="btn" href="/industry/output/">Industrial output</a>
        : <a className="btn" href="/industry/trade/">Exports and imports</a>}
    </div>
  );
}
