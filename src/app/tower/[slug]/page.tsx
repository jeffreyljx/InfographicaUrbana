import type { Metadata } from "next";
import { notFound } from "next/navigation";
import MapApp from "@/components/MapApp";
import { allTowers, towerBySlug, getPlaces } from "@/lib/data";
import { fmtHeight } from "@/lib/format";

export const dynamicParams = false;
export function generateStaticParams() {
  return allTowers().map(t => ({ slug: t.detail.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const t = towerBySlug(slug);
  if (!t) return {};
  const title = `${t.name}, ${t.city}`;
  const description = `${t.name} — ${fmtHeight(t.height)}, ${t.floors} floors, ${t.status.toLowerCase()}${t.year ? ` ${t.year}` : ""}. ${t.district}, ${t.city}. #${t.detail.rank_global} tallest of ${getPlaces().totals.towers.toLocaleString("en-US")} skyscrapers on ScraperMap.`;
  return {
    title, description,
    openGraph: { title, description, images: t.detail.photo ? [t.detail.photo.thumb] : undefined },
    alternates: { canonical: `/tower/${slug}/` },
  };
}

export default async function TowerPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const t = towerBySlug(slug);
  if (!t) notFound();
  const ld = {
    "@context": "https://schema.org", "@type": "Place", name: t.name,
    geo: { "@type": "GeoCoordinates", latitude: t.lat, longitude: t.lon },
    address: { "@type": "PostalAddress", streetAddress: t.detail.address ?? undefined, addressLocality: t.city, addressCountry: t.detail.country },
    additionalProperty: [{ "@type": "PropertyValue", name: "height", value: t.height, unitCode: "MTR" }, { "@type": "PropertyValue", name: "floors", value: t.floors }],
    sameAs: t.detail.ctbuh_url,
  };
  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(ld) }} />
      <MapApp initialTower={t} />
    </>
  );
}
