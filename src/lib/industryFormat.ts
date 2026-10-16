/** Number formats for the Industry and Exports page, kept apart from its data so the client tables load no JSON. */

/** US$ billions as $672bn, $4.5bn or $1.40tn. */
export function money(v: number | null): string {
  if (v == null) return "";
  if (v >= 1000) return `$${(v / 1000).toFixed(2)}tn`;
  return `$${v < 10 ? v.toFixed(1) : Math.round(v).toLocaleString("en-US")}bn`;
}
export const moneyK = (v: number | null) => v == null ? "" : `$${Math.round(v).toLocaleString("en-US")}k`;
/** A source link's label: its site, without www. */
export function site(url: string): string {
  try { return new URL(encodeURI(url)).hostname.replace(/^www\./, ""); } catch { return "source"; }
}
