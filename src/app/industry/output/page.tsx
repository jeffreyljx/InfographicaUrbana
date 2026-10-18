import type { Metadata } from "next";
import Shell from "@/components/Shell";
import IndustryBars from "@/components/IndustryBars";
import { MfgTable, CountryMfgTable, type MfgTableRow, type CountryMfgTableRow } from "@/components/IndustryTable";
import { usd, tickMoney, find, sentence, href, mfgBar, countryMfgBar, countryMapHref, FxTable, IndustryLinks } from "@/components/industryParts";
import { MFG, COUNTRY_MFG, REGION_NAME, region, money, moneyK, citySlug, niceScale, type MfgRow } from "@/lib/industry";
import "@/components/industry.css";

export const metadata: Metadata = {
  title: { absolute: "IndustryMap · Industrial output" },   // its own mode, so not "· ScraperMap"
  description: "Which cities and countries make the most: manufacturing value added by city and added up by country, and output per factory worker, with every figure's source.",
};

export default function OutputPage() {
  const sz = find(MFG, "Shenzhen"), su = find(MFG, "Suzhou"), sh = find(MFG, "Shanghai");
  const perJob = MFG.filter(r => r.va_per_worker_usd_k != null).sort((a, b) => (b.va_per_worker_usd_k ?? 0) - (a.va_per_worker_usd_k ?? 0));
  const bestJob = perJob.find(r => r.country !== "Ireland") as MfgRow;
  const [cn, us] = COUNTRY_MFG;
  const counted = (c: typeof cn) => c.parts.filter(p => !p.inside).length;

  const mfg30 = MFG.slice(0, 30);
  const mfgScale = niceScale(mfg30[0].va_usd_bn);
  const countryScale = niceScale(cn.va);
  const [first, second] = perJob.map(r => r.va_per_worker_usd_k as number);
  const jobScale = niceScale(first > second * 1.6 ? second * 1.1 : first, 7);

  const mfgRows: MfgTableRow[] = MFG.map(r => ({
    place: r.place, slug: citySlug(r.place), country: r.country, year: r.year, va: r.va_usd_bn, jobs: r.employment, perJob: r.va_per_worker_usd_k,
    measure: r.measure, unit: r.unit, upper: r.upper_bound, note: r.note, source: r.source,
  }));
  const countryRows: CountryMfgTableRow[] = COUNTRY_MFG.map(c => ({
    country: c.country, mapHref: countryMapHref(c.country, "output"), n: counted(c), years: c.years.join(", "),
    va: c.va, upper: c.upper, jobs: c.jobs, perJob: c.perJob, jobPlaces: c.jobPlaces,
    parts: c.parts.filter(p => !p.inside).map(p => p.place).join(", "),
    note: [
      ...c.parts.filter(p => p.inside).map(p => `${p.place} left out, as it is inside ${p.inside}`),
      c.country === "Ireland" && "Inflated by multinational profits booked in Ireland",
      c.country === "China" && "Only Shanghai publishes manufacturing jobs",
    ].filter(Boolean).join(". "),
  }));

  return (
    <Shell active="industry-output">
      <h1>Industrial output</h1>
      <p className="lead">
        Which cities make the most. <a className="place" href={href("Shenzhen") ?? undefined}>Shenzhen</a> has the largest factory output,
        {" "}{money(sz.va_usd_bn)} of industrial value added in 2025, ahead of Suzhou (up to {money(su.va_usd_bn)}) and Shanghai ({money(sh.va_usd_bn)}).
        Silicon Valley makes the most per factory worker, {moneyK(bestJob.va_per_worker_usd_k)} a year, once Ireland&apos;s tax-booked
        pharmaceutical profits are set aside. Added up by country, China&apos;s {counted(cn)} places make {money(cn.va)} and the
        {" "}{us.country === "United States" ? <>United States&apos; {counted(us)} metros</> : us.country} {money(us.va)}.
      </p>
      <IndustryLinks show="output" />

      <div className="kpis ind-kpis">
        <div className="kpi"><b>{money(sz.va_usd_bn)}</b><span>Shenzhen · most factory output</span></div>
        <div className="kpi"><b>{money(cn.va)}</b><span>China · its {counted(cn)} places added up</span></div>
        <div className="kpi"><b>{money(us.va)}</b><span>{us.country} · its {counted(us)} places added up</span></div>
        <div className="kpi"><b>{moneyK(bestJob.va_per_worker_usd_k)}</b><span>Silicon Valley · most output per factory job</span></div>
      </div>

      <nav className="ind-toc" aria-label="On this page">
        <a href="#manufacturing">Cities</a><a href="#countries">Countries</a><a href="#per-worker">Per worker</a><a href="#method">How to read this</a>
      </nav>

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

      <section id="countries" className="ind-sec">
        <h2>Added up by country</h2>
        <p>Every place on this page added into the country it belongs to. These are sums of the listed places, not national totals: China&apos;s bar is its {counted(cn)} biggest factory cities, {money(cn.upper)} of them upper bounds drawn hollow. Nagoya city is left out of Japan&apos;s sum because Aichi prefecture already counts it. A country&apos;s name opens it on the map.</p>
        <div className="ib-legend" aria-hidden="true">
          {(["ea", "na", "eu"] as const).map(k => <span key={k}><i className={`c-${k}`} />{REGION_NAME[k]}</span>)}
          <span><i className="c-ea hollow" />Upper bounds</span>
        </div>
        <IndustryBars label="Manufacturing value added, added up by country" rows={COUNTRY_MFG.map(countryMfgBar)} {...countryScale} tick={tickMoney} />
        <details className="ind-more">
          <summary>All {COUNTRY_MFG.length} countries, with jobs and the places in each</summary>
          <CountryMfgTable rows={countryRows} />
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
            <p><b>Manufacturing value added</b> is output minus bought-in materials and parts. Per-worker figures divide it by jobs in the same place; US jobs leave out the self-employed, European ones include them.</p>
            <p><b>Countries</b> add up the places on this page, so a country with many listed places ranks higher than one with few, and a place inside another listed place is counted once.</p>
            <p><b>Places</b> are whatever each country publishes: Chinese prefecture-level cities and the four municipalities include large rural counties, US figures are metro areas, European ones NUTS-3 regions, and Aichi and Osaka whole prefectures. A place name in blue opens that city&apos;s skyscrapers on ScraperMap.</p>
          </div>
          <div>
            <h3>What is missing</h3>
            <ul className="ind-list">
              <li><b>Korea and Taiwan factory output by city.</b> Hwaseong (Samsung&apos;s chip plants), Ulsan (Hyundai, refineries, shipyards) and Hsinchu (TSMC) would belong on the manufacturing chart, but their city tables could not be fetched.</li>
              <li><b>Several large Chinese cities</b> (Suzhou, Guangzhou, Dongguan, Wuxi, Foshan) publish no industrial value added amount, only growth rates, so their bars are upper bounds.</li>
              <li><b>US metro GDP</b> stopped being published by the BEA from the 2024 data year, so US manufacturing figures are the Greater Houston Partnership&apos;s sums of BEA county data.</li>
              <li><b>Mexico, India and Brazil</b> publish few city figures.</li>
            </ul>
            <FxTable />
          </div>
        </div>
      </section>
    </Shell>
  );
}
