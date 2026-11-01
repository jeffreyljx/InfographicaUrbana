import type { NavKey } from "@/components/Nav";

/** The site's name (Jeffrey, 31 Oct 2026: renamed from ScraperMap, which stays the name of the tower map's mode). */
export const SITE_NAME = "InfographicaUrbana";
export const SITE_URL = "https://infographicaurbana.vercel.app";

/** The site's modes, switched from the menu beside the name at the top left (Jeffrey, 18 Oct 2026): ScraperMap,
 *  the tower map with its rankings, skylines and method page in the top bar; TransitMap, the metro history map; and
 *  IndustryMap, the cities that trade and make the most, with its map and two pages of figures in the bar.
 *  CartaHistoria, the historical borders map at /history/, is listed but can't be opened yet (Jeffrey, 1 Nov 2026:
 *  "Under construction...coming this week"); when it ships, drop `soon` and give modeOf its NavKey. */
export type Mode = "scraper" | "transit" | "industry" | "history";
export interface ModeInfo {
  key: Mode; name: string; href: string; blurb: string;
  /** listed in the menu, greyed out and not a link, with the blurb saying when it comes */
  soon?: boolean;
}

export const MODES: ModeInfo[] = [
  { key: "scraper", name: "ScraperMap", href: "/", blurb: "Every skyscraper of 150 m+, with rankings and skylines" },
  { key: "transit", name: "TransitMap", href: "/metro/", blurb: "The world's metro lines, growing year by year" },
  { key: "industry", name: "IndustryMap", href: "/industry/", blurb: "Which cities trade and make the most" },
  { key: "history", name: "CartaHistoria", href: "/history/", blurb: "Under construction...coming this week", soon: true },
];

export const modeOf = (active?: NavKey): ModeInfo =>
  MODES.find(m => m.key === (active === "metro" ? "transit" : active?.startsWith("industry") ? "industry" : "scraper")) as ModeInfo;
