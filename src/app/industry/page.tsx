import type { Metadata } from "next";
import Shell from "@/components/Shell";
import IndustryBars, { type Bar } from "@/components/IndustryBars";
import { TradeTable, ExportTable, MfgTable, type TradeTableRow, type ExportTableRow, type MfgTableRow } from "@/components/IndustryTable";
import {
  TRADE, EXPORTS_ONLY, ALL_EXPORTS, JAPAN_PORTS, CONTAINER_PORTS, MFG, FX, REGION_NAME, region, money, moneyK, site, citySlug, tag, niceScale,
  type TradeRow, type ExportRow, type MfgRow,
} from "@/lib/industry";
import "@/components/industry.css";

export const metadata: Metadata = {
  title: { absolute: "IndustryMap · Industry and Exports" },   // its own mode, so not "· ScraperMap"
  description: "Which cities trade the most goods and which make the most: exports and imports by city, the busiest gateways and container ports, and manufacturing value added and output per factory worker, with every figure's source.",
};

const usd = (v: number) => `$${v.toLocaleString("en-US")}bn`;
const find = <T extends { place: string }>(rows: T[], place: string) => rows.find(r => r.place === place) as T;
const sentence = (...parts: (string | null | undefined | false)[]) => parts.filter(Boolean).join(". ").replace(/\.\./g, ".") + ".";

const href = (place: string) => { const s = citySlug(place); return s ? `/city/${s}/` : null; };
const how = (r: { unit: string; basis: string }) => [r.unit, r.basis].filter(Boolean).join(" · ");

const tradeBar = (r: TradeRow): Bar => ({
  label: r.place, href: href(r.place), tag: tag(r.caveat, r.year),
  segs: r.exports_usd_bn != null && r.imports_usd_bn != null
    ? [{ v: r.exports_usd_bn, cls: "c-ex" }, { v: r.imports_usd_bn, cls: "c-im" }]
    : [{ v: r.total_usd_bn ?? 0, cls: "c-tot" }],
  value: money(r.total_usd_bn),
  title: sentence(
    `${r.place}, ${r.country}, ${r.year}: ` + [r.exports_usd_bn != null && `exports ${money(r.exports_usd_bn)}`, r.imports_usd_bn != null && `imports ${money(r.imports_usd_bn)}`, `total ${money(r.total_usd_bn)}`].filter(Boolean).join(", "),
    r.unit, r.basis, r.note),
});
const exportBar = (r: ExportRow): Bar => ({
  label: r.place, href: href(r.place), tag: tag(r.caveat, r.year),
  segs: [{ v: r.exports_usd_bn, cls: "c-ex" }], value: money(r.exports_usd_bn),
  title: sentence(`${r.place}, ${r.country}, ${r.year}: exports ${money(r.exports_usd_bn)}`, r.unit, r.basis, r.note),
});
const isIndustrial = (r: MfgRow) => /^Industrial/.test(r.measure);
const mfgBar = (r: MfgRow): Bar => ({
  label: r.place, href: href(r.place), hollow: r.upper_bound,
  tag: [r.year, r.upper_bound ? "upper bound" : isIndustrial(r) ? "industrial" : ""].filter(Boolean).join(", "),
  segs: [{ v: r.va_usd_bn, cls: `c-${region(r.country)}` }], value: money(r.va_usd_bn),
  title: sentence(`${r.place}, ${r.country}, ${r.year}: ${r.measure.toLowerCase()} ${r.upper_bound ? "up to " : ""}${money(r.va_usd_bn)}`, r.unit, r.note),
});

export default function IndustryPage() {
  const hk = find(TRADE, "Hong Kong"), sg = find(TRADE, "Singapore"), sz = find(TRADE, "Shenzhen"), sh = find(TRADE, "Shanghai");
  const szMake = find(MFG, "Shenzhen");
  const perJob = MFG.filter(r => r.va_per_worker_usd_k != null).sort((a, b) => (b.va_per_worker_usd_k ?? 0) - (a.va_per_worker_usd_k ?? 0));
  const bestJob = perJob.find(r => r.country !== "Ireland") as MfgRow;
  const port = CONTAINER_PORTS[0];

  // charts
  const trade20 = TRADE.filter(r => r.total_usd_bn != null).slice(0, 20);
  const tradeScale = niceScale(trade20[0].total_usd_bn as number);
  const exp20 = ALL_EXPORTS.slice(0, 20);
  const expScale = niceScale(exp20[0].exports_usd_bn);
  const japan10 = JAPAN_PORTS.slice(0, 10);
  const japanScale = niceScale(japan10[0].total_usd_bn, 4);
  const teuScale = niceScale(port.teu_million, 4);
  const mfg30 = MFG.slice(0, 30);
  const mfgScale = niceScale(mfg30[0].va_usd_bn);
  const [first, second] = perJob.map(r => r.va_per_worker_usd_k as number);
  const jobScale = niceScale(first > second * 1.6 ? second * 1.1 : first, 7);

  const tradeRows: TradeTableRow[] = TRADE.map(r => ({
    place: r.place, slug: citySlug(r.place), country: r.country, year: r.year, ex: r.exports_usd_bn, im: r.imports_usd_bn, total: r.total_usd_bn,
    how: how(r), caveat: r.caveat, note: r.note, source: r.source,
  }));
  const exportRows: ExportTableRow[] = EXPORTS_ONLY.map(r => ({
    place: r.place, slug: citySlug(r.place), country: r.country, year: r.year, ex: r.exports_usd_bn, how: how(r), caveat: r.caveat, note: r.note, source: r.source,
  }));
  const mfgRows: MfgTableRow[] = MFG.map(r => ({
    place: r.place, slug: citySlug(r.place), country: r.country, year: r.year, va: r.va_usd_bn, jobs: r.employment, perJob: r.va_per_worker_usd_k,
    measure: r.measure, unit: r.unit, upper: r.upper_bound, note: r.note, source: r.source,
  }));

  return (
    <Shell active="industry">
      <h1>Industry and Exports</h1>
      <p className="lead">
        Which cities trade the most goods, and which make the most. <a className="place" href={href("Hong Kong") ?? undefined}>Hong Kong</a> moves
        the most goods of any city, {money(hk.total_usd_bn)} of exports and imports in 2025, nearly all of it re-exports, ahead
        of <a className="place" href={href("Singapore") ?? undefined}>Singapore</a> ({money(sg.total_usd_bn)}). Among cities that make what they ship,
        Shenzhen ({money(sz.total_usd_bn)}) and Shanghai ({money(sh.total_usd_bn)}) lead. Shenzhen also has the largest factory output,
        {" "}{money(szMake.va_usd_bn)} of industrial value added, while Silicon Valley makes the most per factory worker,
        {" "}{moneyK(bestJob.va_per_worker_usd_k)} a year, once Ireland&apos;s tax-booked pharmaceutical profits are set aside.
      </p>

      <div className="kpis ind-kpis">
        <div className="kpi"><b>{money(hk.total_usd_bn)}</b><span>Hong Kong · most goods trade</span></div>
        <div className="kpi"><b>{money(szMake.va_usd_bn)}</b><span>Shenzhen · most factory output</span></div>
        <div className="kpi"><b>{moneyK(bestJob.va_per_worker_usd_k)}</b><span>Silicon Valley · most output per factory job</span></div>
        <div className="kpi"><b>{port.teu_million.toFixed(1)}m</b><span>{port.port} · most containers handled</span></div>
      </div>

      <nav className="ind-toc" aria-label="On this page">
        <a href="#trade">Trade</a><a href="#exports">Exports</a><a href="#ports">Ports</a>
        <a href="#manufacturing">Manufacturing</a><a href="#per-worker">Per worker</a><a href="#method">How to read this</a>
      </nav>

      <section id="trade" className="ind-sec">
        <h2>Which cities trade the most goods</h2>
        <p>Exports plus imports of goods in 2025 or the latest year, counted where the trading firm is based, in US dollars at each year&apos;s average exchange rate. Services, and cargo only passing through, are left out. A small note under a name marks a figure counted differently or from another year; hover a bar for the full figures.</p>
        <div className="ib-legend" aria-hidden="true"><span><i className="c-ex" />Exports</span><span><i className="c-im" />Imports</span><span><i className="c-tot" />Total only, no split published</span></div>
        <IndustryBars label="Total goods trade, top 20 places" rows={trade20.map(tradeBar)} {...tradeScale} tick={v => v === 0 ? "0" : money(v)} />
        <p className="ind-note">Hong Kong and Singapore are re-export hubs, so much of their trade is goods bought and sold on by their traders. Beijing&apos;s imports are swollen by the state oil, gas and commodity firms registered there.</p>
        <details className="ind-more">
          <summary>All {TRADE.length} places with exports and imports, with sources</summary>
          <TradeTable rows={tradeRows} />
        </details>
      </section>

      <section id="exports" className="ind-sec">
        <h2>Exports alone</h2>
        <p>Adds the places that publish exports but not imports: US metro areas, Turkish provinces, a Mexican state and an Indian district. US metros count exports where the exporter of record is based.</p>
        <IndustryBars label="Goods exports, top 20 places" rows={exp20.map(exportBar)} {...expScale} tick={v => v === 0 ? "0" : usd(v)} />
        <details className="ind-more">
          <summary>The {EXPORTS_ONLY.length} places that publish exports only, with sources</summary>
          <ExportTable rows={exportRows} />
        </details>
      </section>

      <section id="ports" className="ind-sec">
        <h2>Gateways and ports</h2>
        <div className="ind-two">
          <div>
            <h3>Japan&apos;s busiest customs gateways, 2025</h3>
            <p className="ind-note">Japan publishes trade only by the port or airport where goods clear customs, so these are gateways rather than the cities where firms sit.</p>
            <div className="ib-legend" aria-hidden="true"><span><i className="c-ex" />Exports</span><span><i className="c-im" />Imports</span></div>
            <IndustryBars label="Japan's trade by customs port or airport, top 10" {...japanScale} tick={v => v === 0 ? "0" : usd(v)}
              rows={japan10.map(r => ({
                label: r.port, segs: [{ v: r.exports_usd_bn, cls: "c-ex" }, { v: r.imports_usd_bn, cls: "c-im" }], value: money(r.total_usd_bn),
                title: `${r.port}, ${r.year}: exports ${money(r.exports_usd_bn)}, imports ${money(r.imports_usd_bn)}, total ${money(r.total_usd_bn)}. Counted where goods clear customs.`,
              }))} />
            <p className="ind-src">Source: <a href={JAPAN_PORTS[0].source[0]} target="_blank" rel="noopener">Japan Customs, 2025 port rankings</a></p>
          </div>
          <div>
            <h3>Busiest container ports, 2025</h3>
            <p className="ind-note">Millions of twenty-foot containers (TEU) handled, including those moved from ship to ship. This counts cargo passing through, a different measure from the trade values above.</p>
            <IndustryBars label="Container throughput, million TEU" {...teuScale} tick={v => `${v}m`}
              rows={CONTAINER_PORTS.map(r => ({
                label: r.port, href: href(r.port), tag: r.note ? (r.note.startsWith("At least") ? "at least" : r.note.startsWith("Long Beach") ? "without Long Beach" : "") : "",
                segs: [{ v: r.teu_million, cls: "c-port" }], value: `${r.teu_million.toFixed(1)}m`,
                title: sentence(`${r.port}, ${r.country}, ${r.year}: ${r.teu_million.toFixed(2)} million TEU`, r.note),
              }))} />
            <p className="ind-src">Sources: {[...CONTAINER_PORTS.flatMap(r => r.source).reduce((m, u) => m.has(site(u)) ? m : m.set(site(u), u), new Map<string, string>())].map(([host, u], i) => <span key={host}>{i > 0 && ", "}<a href={u} target="_blank" rel="noopener">{host}</a></span>)}</p>
          </div>
        </div>
      </section>

      <section id="manufacturing" className="ind-sec">
        <h2>Which cities make the most</h2>
        <p>Manufacturing value added: what factories add on top of the materials and parts they buy, in US dollars. Chinese cities publish industrial value added, which also counts mines and power plants. Where a Chinese city publishes only secondary-industry value added, which adds construction, its bar is drawn hollow as an upper bound.</p>
        <div className="ib-legend" aria-hidden="true">
          {(["ea", "na", "eu"] as const).map(k => <span key={k}><i className={`c-${k}`} />{REGION_NAME[k]}</span>)}
          <span><i className="c-ea hollow" />Upper bound</span>
        </div>
        <IndustryBars label="Manufacturing value added, top 30 places" rows={mfg30.map(mfgBar)} {...mfgScale} tick={v => v === 0 ? "0" : usd(v)} />
        <p className="ind-note">US metros 2024, China and Singapore 2025, Europe 2023, Japan 2022 to 2024. Units differ: Chinese cities and the four municipalities include rural counties, and Aichi and Osaka are whole prefectures.</p>
        <details className="ind-more">
          <summary>All {MFG.length} places, with jobs and sources</summary>
          <MfgTable rows={mfgRows} />
        </details>
      </section>

      <section id="per-worker" className="ind-sec">
        <h2>Output per manufacturing worker</h2>
        <p>Manufacturing value added divided by manufacturing jobs in the same place, in US dollars a year. Refining, chips and medicines score highest because they need few workers per dollar of output. Cork and Dublin are inflated by multinational profits booked in Ireland, so Cork&apos;s bar runs off the scale. Chinese cities publish no manufacturing job counts, except Shanghai&apos;s census figure.</p>
        <IndustryBars label="Manufacturing value added per job" {...jobScale} tick={v => v === 0 ? "0" : moneyK(v)}
          rows={perJob.map(r => ({
            label: r.place, href: href(r.place),
            tag: [r.year, r.place === "Shanghai" ? "rough" : "", (r.va_per_worker_usd_k as number) > jobScale.top ? "off the scale" : ""].filter(Boolean).join(", "),
            segs: [{ v: r.va_per_worker_usd_k as number, cls: `c-${region(r.country)}` }],
            value: moneyK(r.va_per_worker_usd_k),
            title: sentence(`${r.place}, ${r.country}, ${r.year}: ${moneyK(r.va_per_worker_usd_k)} per job (${money(r.va_usd_bn)} from ${(r.employment ?? 0).toLocaleString("en-US")} jobs)`, r.unit, r.note),
          }))} />
      </section>

      <section id="method" className="ind-sec">
        <h2>How to read this</h2>
        <div className="ind-two">
          <div>
            <h3>What the numbers count</h3>
            <p><b>Trade</b> is the customs value of goods exported and imported. China, Korea, Vietnam, Brazil and the US count it where the trading firm or exporter of record is based, so a city that hosts head offices can look bigger than its factories. Beijing is the clearest case: state oil, gas and commodity firms registered there book most of its imports. Istanbul&apos;s figure uses legal head offices too.</p>
            <p><b>Port cargo</b> counts goods passing through, wherever they were made or bought, so it is kept apart from trade.</p>
            <p><b>Manufacturing value added</b> is output minus bought-in materials and parts. Per-worker figures divide it by jobs in the same place; US jobs leave out the self-employed, European ones include them.</p>
            <p><b>Places</b> are whatever each country publishes: Chinese prefecture-level cities and the four municipalities include large rural counties, Vietnam&apos;s figures follow the July 2025 province mergers, Malaysia&apos;s are states, and Paris and London are whole regions. A place name in blue opens that city&apos;s skyscrapers on ScraperMap.</p>
          </div>
          <div>
            <h3>What is missing</h3>
            <ul className="ind-list">
              <li><b>Korea and Taiwan factory output by city.</b> Hwaseong (Samsung&apos;s chip plants), Ulsan (Hyundai, refineries, shipyards) and Hsinchu (TSMC) would belong on the manufacturing chart, but their city tables could not be fetched.</li>
              <li><b>Several large Chinese cities</b> (Suzhou, Guangzhou, Dongguan, Wuxi, Foshan) publish no industrial value added amount, only growth rates, so their bars are upper bounds.</li>
              <li><b>US metro imports</b> are not published at all, and the BEA stopped publishing metro GDP from the 2024 data year, so US manufacturing figures are the Greater Houston Partnership&apos;s sums of BEA county data.</li>
              <li><b>Dubai</b> has not published a full 2025 split; its bar uses the 2023 non-oil total.</li>
              <li><b>Mexico, India and Brazil</b> publish few city figures; Ciudad Juárez appears through Chihuahua state.</li>
            </ul>
            <h3>Exchange rates used</h3>
            <p className="ind-note">Federal Reserve annual averages (G.5A), units of each currency per US dollar, for the year each figure covers. Figures were gathered on 16 October 2026 from national, provincial and city statistics offices, customs agencies and port authorities; every row&apos;s sources are linked in the tables above.</p>
            <div className="tablewrap"><table className="itable fx">
              <thead><tr><th>Currency</th><th className="num">Year</th><th className="num">Per US$</th></tr></thead>
              <tbody>{FX.map(r => (
                <tr key={r.code + r.year}><td>{r.currency} <span className="muted">{r.code}</span></td><td className="num">{r.year}</td><td className="num">{r.per_usd.toLocaleString("en-US", { maximumFractionDigits: 4 })}</td></tr>
              ))}</tbody>
            </table></div>
          </div>
        </div>
      </section>
    </Shell>
  );
}
