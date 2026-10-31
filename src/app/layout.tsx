import type { Metadata, Viewport } from "next";
import "./globals.css";
import { preload } from "react-dom";
import placesJson from "@/data/places.json";
import { SITE_NAME, SITE_URL } from "@/lib/modes";
const TOTALS = (placesJson as unknown as { totals: { towers: number; cities: number } }).totals;

export const metadata: Metadata = {
  metadataBase: new URL(process.env.NEXT_PUBLIC_SITE_URL ?? SITE_URL),
  // the site is InfographicaUrbana; the home page is its first mode, ScraperMap (src/lib/modes.ts)
  title: { default: `${SITE_NAME} · ScraperMap, every skyscraper ≥150 m on the map`, template: `%s · ${SITE_NAME}` },
  applicationName: SITE_NAME,
  description: `${TOTALS.towers.toLocaleString("en-US")} skyscrapers of 150 m and taller across ${TOTALS.cities} cities, each pinned to its exact location and assigned to its district. Building data © CTBUH.`,
  appleWebApp: { title: SITE_NAME },
  openGraph: { siteName: SITE_NAME, type: "website", images: [{ url: "/og.png", width: 1200, height: 630, alt: SITE_NAME }] },
  twitter: { card: "summary_large_image", images: ["/og.png"] },
};
export const viewport: Viewport = { themeColor: "#E6D6CF", width: "device-width", initialScale: 1 };

export default function RootLayout({ children }: { children: React.ReactNode }) {
  // the regular and bold Latin subsets cover almost every page's first paint
  for (const w of [400, 700]) preload(`/fonts/libre-baskerville/libre-baskerville-latin-${w}-normal.woff2`, { as: "font", type: "font/woff2", crossOrigin: "anonymous" });
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
