import type { Metadata } from "next";
import { GuidePage, GuideHead, Demo, Steps, Step, DockParts, placeParts, BarsFigure, TryList } from "@/components/Guide";
import { transitGuide } from "@/lib/guideData";
import { fmtKm } from "@/lib/metro";
import media from "@/lib/guideMedia.json";

export const metadata: Metadata = {
  title: "TransitMap · Guide",
  description: "What TransitMap shows and how to use it: the world's metro lines on one map, each stretch drawn from the year it opened, with a card for every station, line and city and a year dock that plays them growing from 1863.",
};

const fmt = (n: number) => n.toLocaleString("en-US");
const FOOT = <>Metro lines and stations © <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors (ODbL); opening dates, lengths and riders from Wikipedia. Basemap by <a href="https://openfreemap.org" target="_blank" rel="noopener">OpenFreeMap</a> © OpenMapTiles, data from OpenStreetMap; satellite imagery © Esri, Maxar, Earthstar Geographics and the GIS User Community.</>;

/** TransitMap's guide (Jeffrey, 4 Nov 2026): what the map shows, how to use it, what the year dock's bars count. */
export default function TransitGuide() {
  const g = transitGuide();
  const { first, last, values, peak } = g.series;
  const span = last - first;
  const x = (y: number) => (y - first) / span;
  const ticks = [];
  for (let y = Math.ceil(first / 20) * 20; y <= last; y += 20) ticks.push({ x: x(y), label: String(y), wide: y % 40 !== 0 });
  const m = media.transit;
  return (
    <GuidePage active="metro-guide" foot={FOOT}>
      <GuideHead name="TransitMap" lead={<>How the world&apos;s metros grew, from London&apos;s first underground line in {first} to today: {g.systems} systems in {g.cities} cities, {fmt(g.lines)} lines and {fmt(g.stations)} stations, each stretch of line drawn from the year it opened.</>}>
        <a className="btn primary" href="/metro/">Open the map</a>
        <a className="btn" href="/metro/?system=cn-shanghai-metro&year=1995">Try Shanghai from 1995</a>
      </GuideHead>

      <Demo name="transit" w={m.demo.w} h={m.demo.h} label="Shanghai's metro growing year by year">
        Shanghai&apos;s metro growing year by year: each year&apos;s new track shows in orange, and the bars count the kilometres opened.
      </Demo>

      <h2>What you can see</h2>
      <p>Zoomed out, each city&apos;s metro is a dot sized by its length in the chosen year. Zoom in, or search, and the lines appear in their own colours, with a dot for every station and a ring for every interchange; track that opened in the chosen year is drawn in orange, and track two lines share is striped in both their colours.</p>
      <p>Zoom right in on a station and it opens up: a box for each line&apos;s platforms in the line&apos;s colour (dashed where its outline is approximate), the station&apos;s halls, and its exits as lettered badges, all from OpenStreetMap.</p>
      <p>Only metros count, by one definition throughout: trains on their own tracks, running often, within a city. Suburban and commuter rail, monorails and trams are left out. Click a station, a line or a city for its card: when it opened, how it grew stage by stage, its stations, length, riders and trains.</p>

      <h2>How to use it</h2>
      <Steps>
        <Step title="Find a city, line or station.">Type it into the search box, or drag and zoom the map; a click on a city&apos;s dot zooms into it.</Step>
        <Step title="Open a card.">Click a line or a station. From a station&apos;s card you can step to its lines, and from a line&apos;s to its stations and its city.</Step>
        <Step title="Move through time.">The year dock at the foot is always open. Drag the slider, or press Play to watch the lines grow from {first}; with a city picked, Play starts from its first line and the dock counts that city alone.</Step>
        <Step title="Look inside a station.">Zoom in close on a station to see its platforms, halls and exits.</Step>
        <Step title="Switch to satellite.">The Satellite button swaps the map for imagery, and the choice is shared with the other maps.</Step>
      </Steps>

      <h2>The year dock</h2>
      <DockParts img="/guide/transit-dock.png" w={m.dock.w} h={m.dock.h} alt="The year dock, set to 2000" parts={placeParts(m.dock.at, [
        ["play", <><b>Play</b> walks forward a year at a time, lingering on years with more new line.</>],
        ["year", <><b>The year</b> on the map: every stretch of line open by then.</>],
        ["facts", <><b>The facts</b>: kilometres of metro open by that year and in how many cities, how many are new, and the longest line opened that year, which opens with a click.</>],
        ["key", <><b>What the bars count</b>, on the left, and on the right the busiest year, or the year under the pointer and its kilometres.</>],
        ["bars", <><b>The bars</b>: one per year, as tall as the kilometres of metro opened that year. Bars up to the chosen year are filled, and its own is orange. Click or drag along them to choose a year.</>],
        ["slider", <><b>The slider</b> chooses any year from {first} to {last}.</>],
        ["min", <><b>Collapse</b> folds the dock into a short bar, so dragging the map can&apos;t move the year; the map remembers it.</>],
      ])} />

      <h3>What the bars count</h3>
      <BarsFigure label={`Kilometres of metro opened each year, ${first} to ${last}`} bars={values.map((v, i) => ({ x: (i - 0.5) / span, w: 1 / span, v }))}
        top={peak.v} topLabel={`${fmtKm(peak.v)} km`} ticks={ticks} peak={{ x: x(peak.year), label: `${peak.year}: ${fmtKm(peak.v)} km` }}>
        Kilometres of metro line opened each year worldwide, less any that closed, from {first} to {last}; {peak.year} opened the most, {fmtKm(peak.v)} km.
        Lengths follow each line&apos;s published length, shared among its stretches by when they opened. With a city picked, the dock&apos;s bars count that city alone, and the line above them names it.
      </BarsFigure>

      <h2>Try these</h2>
      <TryList items={[
        { href: "/metro/?system=gb-london-underground&year=1900", title: "London in 1900", note: "The first underground railways, before the tube network spread." },
        { href: "/metro/?system=fr-paris-metro&year=1900", title: "Paris in 1900", note: "Line 1 opens for the World's Fair; press Play to see the rest follow." },
        { href: "/metro/?system=us-new-york-city-subway&year=1904", title: "New York in 1904", note: "The first subway opens beside the elevated lines already running." },
        { href: "/metro/?system=cn-shanghai-metro&year=1995", title: "Shanghai from 1995", note: "From one line to over 800 km in thirty years: press Play." },
        { href: "/metro/?station=hk-mtr~central", title: "Inside Central, Hong Kong", note: "A station close up, with its platforms, halls and lettered exits." },
        { href: "/metro/?line=in-chennai-metro:4", title: "This autumn's newest line", note: "Chennai's Yellow Line, opened in October 2026." },
      ]} />
    </GuidePage>
  );
}
