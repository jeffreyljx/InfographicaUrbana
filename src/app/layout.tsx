import type { Metadata, Viewport } from "next";
import "./globals.css";
import { preload } from "react-dom";
import placesJson from "@/data/places.json";
const TOTALS = (placesJson as unknown as { totals: { towers: number; cities: number } }).totals;

export const metadata: Metadata = {
  metadataBase: new URL(process.env.NEXT_PUBLIC_SITE_URL ?? "https://scrapermap.vercel.app"),
  title: { default: "ScraperMap — every skyscraper ≥150 m, on the map", template: "%s · ScraperMap" },
  description: `${TOTALS.towers.toLocaleString("en-US")} skyscrapers of 150 m and taller across ${TOTALS.cities} cities, each pinned to its exact location and assigned to its district. Building data © CTBUH.`,
  openGraph: { siteName: "ScraperMap", type: "website" },
  twitter: { card: "summary_large_image" },
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
