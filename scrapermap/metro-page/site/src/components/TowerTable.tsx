import type { Tower } from "@/lib/types";
import { fmtHeight, STATUS_SHORT } from "@/lib/format";
export default function TowerTable({ towers, showCity = false, showDistrict = true }: { towers: Tower[]; showCity?: boolean; showDistrict?: boolean }) {
  return (
    <div className="tablewrap">
      <table>
        <thead><tr>
          <th className="num">#</th><th>Tower</th>{showCity && <th>City</th>}{showDistrict && <th>District</th>}
          <th className="num">Height</th><th className="num">Floors</th><th className="num">Year</th><th>Status</th>
        </tr></thead>
        <tbody>
          {towers.map((t, i) => (
            <tr key={t.id}>
              <td className="num muted">{i + 1}</td>
              <td><a href={`/tower/${t.detail.slug}/`}>{t.name}</a></td>
              {showCity && <td><span className="place">{t.city}</span></td>}
              {showDistrict && <td><span className="place">{t.district}</span></td>}
              <td className="num">{fmtHeight(t.height)}</td>
              <td className="num">{t.floors || "—"}</td>
              <td className="num">{t.year ?? "—"}</td>
              <td><span className="pill">{STATUS_SHORT[t.status] ?? t.status}</span></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
