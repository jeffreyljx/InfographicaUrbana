/** Rank number for the leaderboard tables (# column), with a gold / silver / bronze crown to its left for ranks 1–3.
 *  The crown follows the number shown, so tied ranks share a crown and re-ranking (e.g. the 200 m / 300 m switch) moves it. */
const MEDALS: Record<number, { cls: string; label: string }> = {
  1: { cls: "gold", label: "Gold crown: 1st" },
  2: { cls: "silver", label: "Silver crown: 2nd" },
  3: { cls: "bronze", label: "Bronze crown: 3rd" },
};

export function Crown({ rank }: { rank: number }) {
  const m = MEDALS[rank];
  if (!m) return null;
  return (
    <svg className={`crown ${m.cls}`} width="17" height="13" viewBox="0 0 26 20" role="img" aria-label={m.label}>
      <title>{m.label}</title>
      <path className="crown-body" d="M3.2 15.2 2.2 6.4l5.9 4.3L13 3.4l4.9 7.3 5.9-4.3-1 8.8z" />
      <rect className="crown-body" x="3.2" y="16.2" width="19.6" height="2.6" rx="1" />
      <circle className="crown-gem" cx="2.2" cy="5.2" r="1.8" />
      <circle className="crown-gem" cx="13" cy="2.2" r="1.8" />
      <circle className="crown-gem" cx="23.8" cy="5.2" r="1.8" />
    </svg>
  );
}

/** Contents of a # cell: optional crown, then the rank (or a dash for unranked rows). */
export default function Rank({ rank }: { rank: number }) {
  return (
    <span className={"rank" + (MEDALS[rank] ? " top" : "")}>
      <Crown rank={rank} />
      {rank || "—"}
    </span>
  );
}
