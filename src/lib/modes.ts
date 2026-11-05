import type { NavKey } from "@/components/Nav";

/** The site's name (Jeffrey, 31 Oct 2026: renamed from ScraperMap, which stays the name of the tower map's mode). */
export const SITE_NAME = "InfographicaUrbana";
export const SITE_URL = "https://infographicaurbana.vercel.app";

/** The site's modes, switched from the menu beside the name at the top left (Jeffrey, 18 Oct 2026): ScraperMap,
 *  the tower map with its rankings, skylines and method page in the top bar; TransitMap, the metro history map; and
 *  IndustryMap, the cities that trade and make the most, with its map and two pages of figures in the bar.
 *  CartaHistoria (Jeffrey, 1 Nov 2026) is the historical borders map at /history/: every state's borders year by year
 *  from 6000 BCE, with a page per state at /history/<slug>/. A mode listed before it opens takes `soon: true`. */
export type Mode = "scraper" | "transit" | "industry" | "history";
export interface ModeInfo {
  key: Mode; name: string; href: string; blurb: string;
  /** the mode's guide: a short page on what the map shows and how to use it (Jeffrey, 4 Nov 2026) */
  guide: string;
  /** listed in the menu, greyed out and not a link, with the blurb saying when it comes */
  soon?: boolean;
}

export const MODES: ModeInfo[] = [
  { key: "scraper", name: "ScraperMap", href: "/", guide: "/guide/", blurb: "Every skyscraper of 150 m+, with rankings and skylines" },
  { key: "transit", name: "TransitMap", href: "/metro/", guide: "/metro/guide/", blurb: "The world's metro lines, growing year by year" },
  { key: "industry", name: "IndustryMap", href: "/industry/", guide: "/industry/guide/", blurb: "Which cities trade and make the most" },
  { key: "history", name: "CartaHistoria", href: "/history/", guide: "/history/guide/", blurb: "Every state's borders, year by year, since 6000 BCE" },
];

export const modeOf = (active?: NavKey): ModeInfo =>
  MODES.find(m => m.key === (active?.startsWith("metro") ? "transit" : active?.startsWith("industry") ? "industry" : active?.startsWith("history") ? "history" : "scraper")) as ModeInfo;
export const modeByKey = (key: Mode): ModeInfo => MODES.find(m => m.key === key) as ModeInfo;
