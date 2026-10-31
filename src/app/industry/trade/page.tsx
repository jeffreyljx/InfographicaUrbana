import type { Metadata } from "next";
import Shell from "@/components/Shell";
import IndustryBars from "@/components/IndustryBars";
import { TradeTable, ExportTable, CountryTradeTable, type TradeTableRow, type ExportTableRow, type CountryTradeTableRow } from "@/components/IndustryTable";
import { usd, tickMoney, find, sentence, href, how, tradeBar, exportBar, countryTradeBar, countryMapHref, FxTable, IndustryLinks } from "@/components/industryParts";
import { TRADE, EXPORTS_ONLY, ALL_EXPORTS, JAPAN_PORTS, CONTAINER_PORTS, COUNTRY_TRADE, money, site, citySlug, niceScale } from "@/lib/industry";
import "@/components/industry.css";

export const metadata: Metadata = {
  title: "IndustryMap · Exports and imports",   // its own mode, named before the page
  description: "Which cities and countries trade the most goods: exports and imports by city and added up by country, the busiest customs gateways and container ports, with every figure's source.",
};

export default function TradePage() {
  const hk = find(TRADE, "Hong Kong"), sg = find(TRADE, "Singapore"), sz = find(TRADE, "Shenzhen"), sh = find(TRADE, "Shanghai");
  const houston = find(EXPORTS_ONLY, "Houston");
  const [cn, second] = COUNTRY_TRADE;
  const port = CONTAINER_PORTS[0];

  const trade20 = TRADE.filter(r => r.total_usd_bn != null).slice(0, 20);
  const tradeScale = niceScale(trade20[0].total_usd_bn as number);
  const exp20 = ALL_EXPORTS.slice(0, 20);
  const expScale = niceScale(exp20[0].exports_usd_bn);
  const countryScale = niceScale(cn.total ?? cn.ex);
  const japan10 = JAPAN_PORTS.slice(0, 10);
  const japanScale = niceScale(japan10[0].total_usd_bn, 4);
  const teuScale = niceScale(port.teu_million, 4);

  const tradeRows: TradeTableRow[] = TRADE.map(r => ({
    place: r.place, slug: citySlug(r.place), country: r.country, year: r.year, ex: r.exports_usd_bn, im: r.imports_usd_bn, total: r.total_usd_bn,
    how: how(r), caveat: r.caveat, note: r.note, source: r.source,
  }));
  const exportRows: ExportTableRow[] = EXPORTS_ONLY.map(r => ({
    place: r.place, slug: citySlug(r.place), country: r.country, year: r.year, ex: r.exports_usd_bn, how: how(r), caveat: r.caveat, note: r.note, source: r.source,
  }));
  const countryRows: CountryTradeTableRow[] = COUNTRY_TRADE.map(c => {
    const totalOnly = c.parts.filter(p => p.ex == null).map(p => p.place);
    return {
      country: c.country, mapHref: countryMapHref(c.country, "trade"), n: c.parts.length, years: c.years.join(", "),
      ex: c.ex || null, im: c.im || null, total: c.total, parts: c.parts.map(p => p.place).join(", "),
      note: [
        c.parts.some(p => p.place === "Hong Kong") && "Hong Kong counted with China",
        totalOnly.length > 0 && `${totalOnly.join(" and ")} publish${totalOnly.length === 1 ? "es" : ""} only a total, so the total is more than exports plus imports`,
        c.total == null && "Only exports published",
        c.parts.some(p => p.kind === "gateway") && "Counted at its busiest customs ports and airports",
      ].filter(Boolean).join(". "),
    };
  });
  const cnN = cn.parts.length, jp = COUNTRY_TRADE.find(c => c.country === "Japan");

  return (
    <Shell active="industry-trade">
      <h1>Exports and imports</h1>
      <p className="lead">
        Which cities trade the most goods. <a className="place" href={href("Hong Kong") ?? undefined}>Hong Kong</a> moves
        the most goods of any city, {money(hk.total_usd_bn)} of exports and imports in 2025, nearly all of it re-exports, ahead
        of <a className="place" href={href("Singapore") ?? undefined}>Singapore</a> ({money(sg.total_usd_bn)}). Among cities that make what they ship,
        Shenzhen ({money(sz.total_usd_bn)}) and Shanghai ({money(sh.total_usd_bn)}) lead. Added up by country, China&apos;s {cnN} places
        trade {money(cn.total)}, far ahead of {second.country === "Japan" ? <>Japan&apos;s {second.parts.length} busiest customs gateways</> : second.country} ({money(second.total ?? second.ex)}).
      </p>
      <IndustryLinks show="trade" />

      <div className="kpis ind-kpis">
        <div className="kpi"><b>{money(hk.total_usd_bn)}</b><span>Hong Kong · most goods trade</span></div>
        <div className="kpi"><b>{money(cn.total)}</b><span>China · its {cnN} places added up</span></div>
        <div className="kpi"><b>{money(houston.exports_usd_bn)}</b><span>Houston · most exports of a US metro</span></div>
        <div className="kpi"><b>{port.teu_million.toFixed(1)}m</b><span>{port.port} · most containers handled</span></div>
      </div>

      <nav className="ind-toc" aria-label="On this page">
        <a href="#trade">Cities</a><a href="#exports">Exports</a><a href="#countries">Countries</a><a href="#ports">Ports</a><a href="#method">How to read this</a>
      </nav>

      <section id="trade" className="ind-sec">
        <h2>Which cities trade the most goods</h2>
        <p>Exports plus imports of goods in 2025 or the latest year, counted where the trading firm is based, in US dollars at each year&apos;s average exchange rate. Services, and cargo only passing through, are left out. A small note under a name marks a figure counted differently or from another year; hover a bar for the full figures.</p>
        <div className="ib-legend" aria-hidden="true"><span><i className="c-ex" />Exports</span><span><i className="c-im" />Imports</span><span><i className="c-tot" />Total only, no split published</span></div>
        <IndustryBars label="Total goods trade, top 20 places" rows={trade20.map(tradeBar)} {...tradeScale} tick={tickMoney} />
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

      <section id="countries" className="ind-sec">
        <h2>Added up by country</h2>
        <p>Every place on this page added into the country it belongs to, Hong Kong into China. These are sums of the listed places, not national totals: China&apos;s bar adds up its {cnN} biggest trading places, and the United States&apos; adds up its {COUNTRY_TRADE.find(c => c.country === "United States")?.parts.length} biggest exporting metros, whose imports are not published, so it is drawn hollow at its exports. {jp && <>Japan is counted at its {jp.parts.length} busiest customs ports and airports.</>} A country&apos;s name opens it on the map.</p>
        <div className="ib-legend" aria-hidden="true"><span><i className="c-ex" />Exports</span><span><i className="c-im" />Imports</span><span><i className="c-tot" />Places with a total only</span><span><i className="c-ex hollow" />Exports only published</span></div>
        <IndustryBars label="Goods trade added up by country" rows={COUNTRY_TRADE.map(countryTradeBar)} {...countryScale} tick={tickMoney} />
        <details className="ind-more">
          <summary>All {COUNTRY_TRADE.length} countries, with the places in each</summary>
          <CountryTradeTable rows={countryRows} />
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

      <section id="method" className="ind-sec">
        <h2>How to read this</h2>
        <div className="ind-two">
          <div>
            <h3>What the numbers count</h3>
            <p><b>Trade</b> is the customs value of goods exported and imported. China, Korea, Vietnam, Brazil and the US count it where the trading firm or exporter of record is based, so a city that hosts head offices can look bigger than its factories. Beijing is the clearest case: state oil, gas and commodity firms registered there book most of its imports. Istanbul&apos;s figure uses legal head offices too.</p>
            <p><b>Port cargo</b> counts goods passing through, wherever they were made or bought, so it is kept apart from trade.</p>
            <p><b>Countries</b> add up the places on this page, so a country with many listed places ranks higher than one with few; Hong Kong is counted with China.</p>
            <p><b>Places</b> are whatever each country publishes: Chinese prefecture-level cities and the four municipalities include large rural counties, Vietnam&apos;s figures follow the July 2025 province mergers, Malaysia&apos;s are states, and Paris and London are whole regions. A place name in blue opens that city&apos;s skyscrapers on ScraperMap.</p>
          </div>
          <div>
            <h3>What is missing</h3>
            <ul className="ind-list">
              <li><b>US metro imports</b> are not published at all.</li>
              <li><b>Dubai</b> has not published a full 2025 split; its bar uses the 2023 non-oil total.</li>
              <li><b>Japan</b> publishes trade only by customs port or airport, not by city.</li>
              <li><b>Mexico, India and Brazil</b> publish few city figures; Ciudad Juárez appears through Chihuahua state.</li>
            </ul>
            <FxTable />
          </div>
        </div>
      </section>
    </Shell>
  );
}
