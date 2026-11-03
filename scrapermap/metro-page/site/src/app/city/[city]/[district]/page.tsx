import type { Metadata } from "next";
import { notFound } from "next/navigation";
import Shell from "@/components/Shell";
import TowerTable from "@/components/TowerTable";
import { getPlaces, towersInDistrict } from "@/lib/data";

export const dynamicParams = false;
export function generateStaticParams() { return getPlaces().districts.map(d => ({ city: d.city_slug, district: d.slug })); }
export async function generateMetadata({ params }: { params: Promise<{ city: string; district: string }> }): Promise<Metadata> {
  const { city, district } = await params; const d = getPlaces().districts.find(x => x.city_slug === city && x.slug === district);
  return d ? { title: `${d.name}, ${d.city}`, description: `${d.completed} completed skyscrapers of 150 m+ in ${d.name}, ${d.city} — #${d.rank} district in the world.` } : {};
}

export default async function DistrictPage({ params }: { params: Promise<{ city: string; district: string }> }) {
  const { city, district } = await params;
  const d = getPlaces().districts.find(x => x.city_slug === city && x.slug === district);
  if (!d) notFound();
  const towers = towersInDistrict(d.city, d.name).sort((a, b) => b.height - a.height);
  return (
    <Shell active="districts">
      <div className="crumbs"><a href="/cities/">Cities</a> › <a className="place" href={`/city/${d.city_slug}/`}>{d.city}</a> › <span className="place">{d.name}</span></div>
      <h1>{d.name}</h1>
      <p className="lead">#{d.rank} district in the world with {d.completed} completed skyscrapers of 150 m and taller{d.count - d.completed ? `, ${d.count - d.completed} more in the pipeline` : ""}. Tallest: {d.tallest_name}, {d.tallest_h}{"\u00a0"}m.</p>
      <div className="heroactions"><a className="btn primary" href={`/?city=${encodeURIComponent(d.city)}&district=${encodeURIComponent(d.name)}`}>Open {d.name} on the map</a><a className="btn" href="/districts/">All districts</a></div>
      <h2>All {towers.length} towers</h2>
      <TowerTable towers={towers} showDistrict={false} />
    </Shell>
  );
}
