import type { NavKey } from "@/components/Nav";

/** The site's name (Jeffrey, 31 Oct 2026: renamed from ScraperMap, which stays the name of the tower map's mode). */
export const SITE_NAME = "InfographicaUrbana";
export const SITE_URL = "https://infographicaurbana.vercel.app";

/** The site's three modes, switched from the menu beside the name at the top left (Jeffrey, 18 Oct 2026): ScraperMap,
 *  the tower map with its rankings, skylines and method page in the top bar; TransitMap, the metro history map; and
 *  IndustryMap, the cities that trade and make the most, with its map and two pages of figures in the bar. */
export type Mode = "scraper" | "transit" | "industry";
export interface ModeInfo { key: Mode; name: string; href: string; blurb: string }

export const MODES: ModeInfo[] = [
  { key: "scraper", name: "ScraperMap", href: "/", blurb: "Every skyscraper of 150 m+, with rankings and skylines" },
  { key: "transit", name: "TransitMap", href: "/metro/", blurb: "The world's metro lines, growing year by year" },
  { key: "industry", name: "IndustryMap", href: "/industry/", blurb: "Which cities trade and make the most" },
];

export const modeOf = (active?: NavKey): ModeInfo =>
  MODES.find(m => m.key === (active === "metro" ? "transit" : active?.startsWith("industry") ? "industry" : "scraper")) as ModeInfo;
