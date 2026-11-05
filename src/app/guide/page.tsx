import type { Metadata } from "next";
import { GuidePage, GuideHead, Demo, Steps, Step, DockParts, placeParts, BarsFigure, TryList } from "@/components/Guide";
import { scraperGuide } from "@/lib/guideData";
import media from "@/lib/guideMedia.json";

export const metadata: Metadata = {
  title: "ScraperMap · Guide",
  description: "What ScraperMap shows and how to use it: every skyscraper of 150 m or taller on one map, with search, filters, skyline extents, metro footprints and a time capsule that goes back to 1889.",
};

const fmt = (n: number) => n.toLocaleString("en-US");

/** ScraperMap's guide (Jeffrey, 4 Nov 2026): what the map shows, how to use it, what the time capsule's bars count. */
export default function ScraperGuide() {
  const { totals, lost, counted, series } = scraperGuide();
  const { first, last, values, peak } = series;
  const span = last - first;
  const x = (y: number) => (y - first) / span;
  const ticks = [];
  for (let y = Math.ceil(first / 20) * 20; y <= last; y += 20) ticks.push({ x: x(y), label: String(y), wide: y % 40 !== 0 });
  const m = media.scraper;
  return (
    <GuidePage active="guide">
      <GuideHead name="ScraperMap" lead={<>Every skyscraper of 150 metres or taller in {totals.cities} cities, {fmt(totals.towers)} towers in all, each pinned where it stands and counted by the district it stands in.</>}>
        <a className="btn primary" href="/">Open the map</a>
        <a className="btn" href="/?year=1931&city=New%20York%20City">Try the time capsule</a>
      </GuideHead>

      <Demo name="scraper" w={m.demo.w} h={m.demo.h} label="The time capsule playing over Downtown Dubai from 2000 to 2026">
        The time capsule playing over Downtown Dubai from 2000 to 2026: each tower appears in the year it was completed, ringed in orange that year, and the Burj Khalifa stands up in 2010. The bars at the foot count the towers completed each year around the world.
      </Demo>

      <h2>What you can see</h2>
      <p>Each dot is a tower, coloured by its height: 150 to 199 m, 200 to 299 m, 300 to 399 m, and 400 m or more (the key is at the bottom left). Zoomed out, towers close together gather into numbered circles; zoom in and they split into single pins, and the world&apos;s ten tallest stand up as small drawings at one shared scale. Completed towers show by default, and the filters add those topped out or under construction.</p>
      <p>Click a tower for its card: height, floors, year, use, a photograph where a freely licensed one exists, and where it ranks in the world, its city and its district. The pages in the top bar rank every country, city and district by their towers, and Skylines sets the leading cities&apos; skylines side by side at one scale.</p>
      <p>Three switches change what the map draws. <b>Skyline extent</b> outlines each city&apos;s dense core, wherever five or more towers stand close together. <b>Metro footprint</b> shades the built-up land around each city, from ESA&apos;s WorldCover satellite map. The eye button hides the towers, so the shapes can be read on their own, and <b>Satellite</b> swaps the map for imagery.</p>

      <h2>How to use it</h2>
      <Steps>
        <Step title="Find a place.">Type a tower, city or district into the search box, or drag and zoom the map. Opening a city or district draws its boundary.</Step>
        <Step title="Open a tower.">Click its pin, or a numbered circle to zoom into it. Where several towers share one point, a list lets you pick.</Step>
        <Step title="Narrow it down.">Filters chooses the status, a minimum height, the years completed, the use (homes, offices, hotels or mixed), and one city or district.</Step>
        <Step title="Change the view.">Turn on Skyline extent or Metro footprint, hide the towers, or switch to satellite.</Step>
        <Step title="Go back in time.">The Time capsule button at the foot of the map opens the dock below. Drag the slider, or press Play to watch the skylines rise from {first}. Skyline extents shrink back to the towers built by then.</Step>
      </Steps>

      <h2>The time capsule</h2>
      <DockParts img="/guide/scraper-dock.png" w={m.dock.w} h={m.dock.h} alt="The time capsule dock, set to 2000" parts={placeParts(m.dock.at, [
        ["play", <><b>Play</b> walks forward a year at a time, lingering on busy years.</>],
        ["year", <><b>The year</b> on the map. A tower shows from its completion year; the {lost} lost towers, such as the original World Trade Center, stand until the year they came down.</>],
        ["facts", <><b>The facts</b>: towers standing that year, how many are new and any lost, and the tallest standing, which opens with a click.</>],
        ["key", <><b>What the bars count</b>, on the left, and on the right the busiest year, or the year under the pointer and its count.</>],
        ["bars", <><b>The bars</b>: one per year, as tall as the number of towers completed that year. Bars up to the chosen year are filled, and its own is orange. Click or drag along them to choose a year.</>],
        ["slider", <><b>The slider</b> chooses any year from {first} to {last}.</>],
        ["min", <><b>Collapse</b> folds the dock into a short bar, so dragging the map can&apos;t move the year.</>],
        ["close", <><b>Close</b> puts the map back to today.</>],
      ])} />

      <h3>What the bars count</h3>
      <BarsFigure label={`Towers completed each year, ${first} to ${last}`} bars={values.map((v, i) => ({ x: (i - 0.5) / span, w: 1 / span, v }))}
        top={peak.v} topLabel={fmt(peak.v)} ticks={ticks} peak={{ x: x(peak.year), label: `${peak.year}: ${fmt(peak.v)}` }}>
        Towers of 150 m or more completed each year, from {first} to {last}: {fmt(counted)} with a known completion year, the lost towers included. {peak.year} was the busiest year, with {fmt(peak.v)}.
        With a filter on, such as one city, the dock&apos;s bars count only the towers that pass it, and the line above them names the city.
      </BarsFigure>

      <h2>Try these</h2>
      <TryList items={[
        { href: "/?year=1931&city=New%20York%20City", title: "New York in 1931", note: "The year the Empire State Building was finished, and the bars for New York alone." },
        { href: "/?year=2000&city=Dubai", title: "Dubai in 2000", note: "Press Play to watch Sheikh Zayed Road, the Marina and Downtown fill in." },
        { href: "/?city=Shenzhen&skyline=1", title: "Shenzhen's skyline extents", note: "The dense cores of the city with the most towers after Hong Kong." },
        { href: "/?footprint=1&skyline=0", title: "Metro footprints", note: "The built-up land around every city on the map." },
        { href: "/?id=3", title: "Burj Khalifa", note: "The tallest of all, 828 m, with its card open." },
        { href: "/skylines/", title: "Skylines side by side", note: "The leading cities' skylines at one scale." },
      ]} />

      <p className="g-more">Where the data comes from, how each pin was placed and checked, and what is missing: <a href="/method/">Method &amp; sources</a>.</p>
    </GuidePage>
  );
}
