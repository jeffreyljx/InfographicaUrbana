import type { Metadata } from "next";
import { GuidePage, GuideHead, Demo, Steps, Step, TryList } from "@/components/Guide";
import { industryMapData, money, mapKey } from "@/lib/industry";
import media from "@/lib/guideMedia.json";
import "@/components/industry.css";

export const metadata: Metadata = {
  title: "IndustryMap · Guide",
  description: "What IndustryMap shows and how to use it: the cities and countries that trade and make the most, each a circle to scale, with every figure's source.",
};

const FOOT = <>Figures from national and city statistics offices, customs agencies and port authorities, each named on its place&apos;s card and on the Exports and imports and Industrial output pages. Basemap by <a href="https://openfreemap.org" target="_blank" rel="noopener">OpenFreeMap</a> © OpenMapTiles, data from OpenStreetMap.</>;

/** IndustryMap's guide (Jeffrey, 4 Nov 2026): what the map shows and how to use it. It has no year dock: one year per figure. */
export default function IndustryGuide() {
  const d = industryMapData();
  const trade = [...d.trade].filter(r => r.total != null).sort((a, b) => (b.total ?? 0) - (a.total ?? 0));
  const output = [...d.output].sort((a, b) => b.va - a.va);
  const [t1, t2] = trade, o1 = output[0];
  const places = new Set([...d.trade, ...d.output].map(r => r.key)).size;
  const m = media.industry;
  return (
    <GuidePage active="industry-guide" foot={FOOT}>
      <GuideHead name="IndustryMap" lead={<>Which cities trade and make the most: goods exports and imports, and the value added by industry, for {places} places on one map, each a circle whose area is to scale with its figure, and every figure with its source.</>}>
        <a className="btn primary" href="/industry/">Open the map</a>
        <a className="btn" href="/industry/trade/">Exports and imports</a>
        <a className="btn" href="/industry/output/">Industrial output</a>
      </GuideHead>

      <Demo name="industry" w={m.demo.w} h={m.demo.h} label="Switching IndustryMap between trade and industrial output, cities and countries">
        Switching between trade and industrial output, and between cities and countries, then opening a city&apos;s card.
      </Demo>

      <h2>What you can see</h2>
      <p><b>Trade</b> shows each place&apos;s goods exports plus imports in US dollars, for 2025 or the latest year published, or either flow on its own. {t1.name} ({money(t1.total ?? 0)}) and {t2.name} ({money(t2.total ?? 0)}) lead, mostly on goods passing through them to somewhere else. Where only exports are published, as for the American metro areas, the circle is hollow; Japan counts trade at each customs port and airport, so its circles sit on those.</p>
      <p><b>Industrial output</b> shows the value that manufacturing (and, where the source counts them in, mining and utilities) adds in each city; {o1.name} leads with {money(o1.va)}. A hollow circle there is an upper bound that also counts construction.</p>
      <p><b>Cities</b> or <b>Countries</b>: a country&apos;s circle adds up its places on this map, with Hong Kong counted in China, so it is a sum of the listed cities rather than a national total. Cities report in different ways (a city proper, a metro area, a customs district), and each card says which.</p>

      <h2>How to use it</h2>
      <Steps>
        <Step title="Choose the figure.">Trade or Industrial output, in the first switch at the top.</Step>
        <Step title="Choose the places.">Cities, or Countries for the sums by country.</Step>
        <Step title="Choose the flow.">With Trade on, Exports + imports, Exports or Imports.</Step>
        <Step title="Read the circles.">The key at the bottom left gives three reference circles in dollars for the current zoom: a circle&apos;s area, not its width, is in proportion to its figure.</Step>
        <Step title="Open a place.">Click a circle for its card: the figures and their year, its rank on the map, how the source counts it, any caveat, and the sources, with links to the place&apos;s other figure where it has one, its skyscrapers and the full tables. A country&apos;s card lists its places.</Step>
        <Step title="See the tables.">Exports and imports and Industrial output, in the top bar, rank every place in charts and tables, with the busiest container ports and Japan&apos;s customs gateways.</Step>
      </Steps>
      <p>IndustryMap has no year dock: each figure is for one year, 2025 where it has been published, and a card shows when it is older.</p>

      <h2>Try these</h2>
      <TryList items={[
        { href: `/industry/?place=${mapKey(t1.name)}`, title: `${t1.name}'s trade`, note: "The largest figure on the map, and what is behind it." },
        { href: `/industry/?show=output&place=${mapKey(o1.name)}`, title: `${o1.name}'s industry`, note: "The most value added by industry of any city listed." },
        { href: "/industry/?by=country", title: "Countries", note: "Each country's listed cities, added up." },
        { href: "/industry/?flow=ex", title: "Exports only", note: "Adding the places that publish nothing else, such as Houston." },
        { href: "/industry/trade/", title: "Exports and imports", note: "Every place ranked, with ports and gateways." },
        { href: "/industry/output/", title: "Industrial output", note: "Value added and, where published, output per worker." },
      ]} />
    </GuidePage>
  );
}
