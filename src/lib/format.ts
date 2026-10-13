export function slugify(s: string): string {
  return s.normalize("NFKD").replace(/[\u0300-\u036f]/g, "")
    .toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/-+/g, "-").replace(/^-|-$/g, "") || "x";
}

export function fmtHeight(m: number): string {
  return `${Number.isInteger(m) ? m : m.toFixed(1)}\u00a0m`; // no-break space: keep the unit with its number
}
export function fmtFeet(m: number): string {
  return `${Math.round(m * 3.28084).toLocaleString()}\u00a0ft`;
}

export const STATUS_SHORT: Record<string, string> = {
  "Completed": "Completed",
  "Architecturally topped out": "Topped out",
  "Structurally topped out": "Topped out (structure)",
  "Under construction": "Under construction",
};

export const PRECISION_LABEL: Record<string, string> = {
  "building-verified": "Building footprint, verified against OpenStreetMap",
  "building": "Building point from the CTBUH database",
  "building-geocoded": "Geocoded to the named building",
  "complex": "Centre of the multi-tower complex",
  "approximate": "Approximate — street or area level only",
};

export function heightBand(h: number): 0 | 1 | 2 | 3 {
  if (h >= 400) return 3;
  if (h >= 300) return 2;
  if (h >= 200) return 1;
  return 0;
}
export const BAND_LABEL = ["150–199 m", "200–299 m", "300–399 m", "400 m +"];
