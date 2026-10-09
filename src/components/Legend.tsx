import { BAND_COLORS } from "@/lib/colors";
import { BAND_LABEL } from "@/lib/format";
export default function Legend({ skyline = false }: { skyline?: boolean }) {
  return (
    <div className="legend" aria-hidden>
      {BAND_LABEL.map((l, i) => (
        <span key={l}><i style={{ background: BAND_COLORS[i] }} />{l}</span>
      ))}
      <span><i className="hollow" />approximate</span>
      {skyline && <span><i className="sky" />skyline extent</span>}
    </div>
  );
}
