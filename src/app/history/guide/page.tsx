import type { Metadata } from "next";
import { GuidePage, GuideHead, Demo, Steps, Step, DockParts, placeParts, BarsFigure, TryList } from "@/components/Guide";
import { historyGuide } from "@/lib/guideData";
import { fmtArea, yearToPos, YEAR_TICKS } from "@/lib/history";
import media from "@/lib/guideMedia.json";

export const metadata: Metadata = {
  title: "CartaHistoria · Guide",
  description: "What CartaHistoria shows and how to use it: every state's borders year by year from 6000 BCE to 2026, with vassals, occupations and contested land, a page for every state, and a year dock that plays history forward.",
};

const FOOT = <>Borders from <a href="https://seshat-db.com/" target="_blank" rel="noopener">Cliopatria</a> (Seshat Global History Databank, CC BY 4.0), corrected and dated year by year from Wikipedia, listed on each state&apos;s page. Basemap by <a href="https://openfreemap.org" target="_blank" rel="noopener">OpenFreeMap</a> © OpenMapTiles, data from OpenStreetMap.</>;

/** CartaHistoria's guide (Jeffrey, 4 Nov 2026): what the map shows, how to use it, what the year dock's bars count. */
export default function HistoryGuide() {
  const g = historyGuide();
  const peak = g.bins.reduce((a, b) => b.v > a.v ? b : a);
  const ticks = YEAR_TICKS.map(t => ({ x: yearToPos(t), label: t < 0 ? `${-t} BCE` : String(t), wide: ![-6000, -1000, 0, 1500, 2000].includes(t) }));
  const area = (cells: number) => fmtArea(cells, g.cellKm2);
  const m = media.history;
  return (
    <GuidePage active="history-guide" foot={FOOT}>
      <GuideHead name="CartaHistoria" lead={<>Every state&apos;s borders, year by year, from 6000 BCE to 2026: {g.states.toLocaleString("en-US")} states, empires, dynasties and cultures on one map, with their vassals, occupations and contested land, and a page for every one.</>}>
        <a className="btn primary" href="/history/">Open the map</a>
        <a className="btn" href="/history/?year=1206&state=mongol-empire">Try the Mongol conquests</a>
      </GuideHead>

      <Demo name="history" w={m.demo.w} h={m.demo.h} label="The Mongol Empire spreading across Asia from 1206 to 1260">
        The year dock stepping from 1206 to 1260: the Mongol Empire spreads across Asia and splits into its khanates, land gained in a year is outlined in orange, and the year&apos;s events are listed in the dock.
      </Demo>

      <h2>What you can see</h2>
      <p>The world as it stood at the end of the chosen year. Each state keeps one colour for life, the familiar one where there is one (Rome red, France blue). A lighter tint of a state&apos;s colour is its vassal; member states, such as the Soviet republics, keep their own colour inside their realm&apos;s border; hatching in a state&apos;s colour is land it occupies; a blend of two colours is land they are fighting over; grey is nobody&apos;s land; dotted pastels are archaeological cultures rather than states. Land a state gains is outlined in orange in the year it gains it.</p>
      <p>Hover over the map for the name of the state below the pointer and its standing there. Click it for its card: its years on the map, its largest extent, its capital then, and the events around the chosen year. Each state also has a page of its own, with its rulers, wars, every dated change to its territory and the Wikipedia pages behind them.</p>
      <p>The map is drawn on a grid of hexagons of about {Math.round(g.cellKm2)} km² each, so a border is drawn to within about ten kilometres at best, and is rougher where the record is thin: each state&apos;s page says how sure its borders are.</p>

      <h2>How to use it</h2>
      <Steps>
        <Step title="Find a state.">Type a state, empire, dynasty or culture into the search box. The map flies to it, staying in the chosen year if the state held land then, or else going to its first year.</Step>
        <Step title="Move through time.">Drag the slider, or press Play. Play steps from one year with a change to the next, slowing on busy years and on years with events; the button beside it sets the speed, 1×, 3× or 10×. With the slider selected, the arrow keys move a year (ten with Shift), and Page Up and Page Down a century.</Step>
        <Step title="Open a state.">Click it on the map, or a state named in the dock&apos;s events, then follow its card to its page.</Step>
        <Step title="Read the method.">About, beside the search box, says how the borders were made and how fresh the data is.</Step>
      </Steps>

      <h2>The year dock</h2>
      <DockParts img="/guide/history-dock.png" w={m.dock.w} h={m.dock.h} alt="The year dock, set to 1300" parts={placeParts(m.dock.at, [
        ["play", <><b>Play</b> steps through the years with a change.</>],
        ["year", <><b>The year</b>: the borders at its end.</>],
        ["facts", <><b>The facts</b>: how many states hold land that year and how much land they hold between them.</>],
        ["caption", <><b>The year&apos;s events</b>, the biggest state&apos;s first; click a state&apos;s name to open it.</>],
        ["speed", <><b>Speed</b> for Play: 1×, 3× or 10×.</>],
        ["min", <><b>Collapse</b> folds the dock into a short bar; the map remembers it.</>],
        ["key", <><b>What the bars count</b>, on the left, and on the right the busiest stretch of years, or the one under the pointer and its land.</>],
        ["bars", <><b>The bars</b>: how much land changed hands in each stretch of years. Bars before the chosen year are filled, and an orange line marks it.</>],
        ["slider", <><b>The slider</b>, which runs slower before 1500, so the last five centuries aren&apos;t a sliver of eight thousand years.</>],
      ])} />

      <h3>What the bars count</h3>
      <BarsFigure label="Land that changed hands, 6000 BCE to 2026" bars={g.bins} top={peak.v} topLabel={area(peak.v)} ticks={ticks} sqrt
        peak={{ x: peak.x + peak.w / 2, label: g.top[0].years }}>
        Each bar is a stretch of years: about a century before 1000 BCE, 17 years from then to 1500, and 4 years since, as the slider gives more room to later centuries.
        Its height is the land whose owner or standing changed in those years: taken, made a vassal, occupied or fought over, counted again each time it changed. Heights are on a square-root scale, so the busiest stretches don&apos;t flatten the rest;
        the busiest are {g.top.map((t, i) => <span key={t.years}>{i ? (i === g.top.length - 1 ? " and " : ", ") : ""}{t.years} ({area(t.cells)})</span>)}.
        Quiet stretches are as often gaps in the record as years of peace.
      </BarsFigure>

      <h2>Try these</h2>
      <TryList items={[
        { href: "/history/?year=1206&state=mongol-empire", title: "The Mongol Empire, 1206", note: "Press Play to watch it spread across Asia and into Europe." },
        { href: "/history/?year=115&state=roman-empire", title: "Rome at its largest, 115", note: "The empire under Trajan, the largest it ever was." },
        { href: "/history/?year=-323&state=macedonian-empire", title: "Alexander's empire, 323 BCE", note: "The year he died, before his generals divided it." },
        { href: "/history/?year=1914", title: "1914", note: "The world's empires on the eve of the First World War." },
        { href: "/history/?year=1532&state=inca-empire", title: "The Inca Empire, 1532", note: "At its height, the year the Spanish arrived." },
        { href: "/history/roman-empire/", title: "A state's page", note: "The Roman Empire: rulers, wars, every change to its land, and the sources." },
      ]} />
    </GuidePage>
  );
}
