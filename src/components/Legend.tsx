import { BAND_COLORS } from "@/lib/colors";
import { BAND_LABEL } from "@/lib/format";
export default function Legend({ skyline = false, capsuleYear = null, lostThisYear = false }: {
  skyline?: boolean; capsuleYear?: number | null;
  /** Time capsule: a tower came down in the chosen year (a ghost ring marks where it stood). */
  lostThisYear?: boolean;
}) {
  return (
    <div className="legend" aria-hidden>
      {BAND_LABEL.map((l, i) => (
        <span key={l}><i style={{ background: BAND_COLORS[i] }} />{l}</span>
      ))}
      <span><i className="hollow" />approximate</span>
      {skyline && <span><i className="sky" />skyline extent</span>}
      {capsuleYear !== null && <span><i className="new" />completed in {capsuleYear}</span>}
      {capsuleYear !== null && lostThisYear && <span><i className="ghost" />came down in {capsuleYear}</span>}
    </div>
  );
}
