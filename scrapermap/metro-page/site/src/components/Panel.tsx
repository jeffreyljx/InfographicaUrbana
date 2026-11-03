"use client";
import { useState } from "react";
import type { Tower } from "@/lib/types";
import { fmtHeight, fmtFeet, PRECISION_LABEL, STATUS_SHORT, heightBand } from "@/lib/format";
import { BAND_COLORS } from "@/lib/colors";
import { slugify, towerSlug } from "@/lib/types";

export default function Panel({ tower: t, onClose }: { tower: Tower; onClose: () => void }) {
  const d = t.detail;
  const [copied, setCopied] = useState(false);
  const band = heightBand(t.height);
  const share = async () => {
    const url = d?.slug ? `${location.origin}/tower/${d.slug}/` : location.href;
    try { await navigator.clipboard.writeText(url); setCopied(true); setTimeout(() => setCopied(false), 1500); } catch { /* ignore */ }
  };
  const citySlug = slugify(t.city), distSlug = slugify(t.district);
  const lost = t.lost, how = lost ? lost.how[0].toUpperCase() + lost.how.slice(1) : "";
  const knownCity = !lost || lost.cityKnown;
  return (
    <aside className="panel" aria-label={t.name}>
      <button className="x" onClick={onClose} aria-label="Close">×</button>
      {d?.photo ? (
        <figure className="photo">
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src={d.photo.thumb} alt={t.name} loading="lazy" />
          <figcaption>
            {d.photo.complex ? <span title="Matched on the development's name; the photo may show other towers in the complex">Complex view · </span> : null}
            <a href={d.photo.page} target="_blank" rel="noopener">Wikimedia Commons</a>
            {d.photo.author ? <> · {d.photo.author}</> : null}
            {d.photo.license ? <> · {d.photo.license_url ? <a href={d.photo.license_url} target="_blank" rel="noopener">{d.photo.license}</a> : d.photo.license}</> : null}
          </figcaption>
        </figure>
      ) : (
        <div className="photo none" style={{ background: `linear-gradient(160deg, ${BAND_COLORS[band]}33, var(--bg-3))` }}>
          <span className="bigh">{fmtHeight(t.height)}</span>
        </div>
      )}
      <div className="body">
        <h1>{t.name}</h1>
        {lost && <p className="lost-note">{how} in {lost.gone}. {lost.cause}</p>}
        <p className="where">
          {knownCity && t.district ? <><a className="place" href={`/city/${citySlug}/${distSlug}/`}>{t.district}</a> · </> : null}
          {knownCity ? <a className="place" href={`/city/${citySlug}/`}>{t.city}</a> : <span className="place">{t.city}</span>}
          {d?.country ? <>, <span className="place">{d.country}</span></> : null}
        </p>

        <dl className="facts">
          <div><dt>Height</dt><dd>{fmtHeight(t.height)} <span className="muted">{fmtFeet(t.height)}</span>{d && d.height_confirmed === false ? <span className="muted"> · unconfirmed</span> : null}</dd></div>
          <div><dt>Floors</dt><dd>{t.floors || "—"}</dd></div>
          {lost
            ? <div><dt>Status</dt><dd>{how} <span className="muted" style={{ whiteSpace: "nowrap" }}>· stood {lost.completed}–{lost.gone}</span></dd></div>
            : <div><dt>Status</dt><dd>{STATUS_SHORT[t.status] ?? t.status}{t.year ? <span className="muted"> · {t.year}</span> : null}</dd></div>}
          <div><dt>Use</dt><dd>{t.fn || "—"}</dd></div>
          {d?.material && <div><dt>Structure</dt><dd>{d.material}</dd></div>}
          {d?.address && <div><dt>Address</dt><dd>{d.address}</dd></div>}
          {lost?.replacedBy && <div><dt>Replaced by</dt><dd>{lost.replacedById
            ? <a href={`/tower/${towerSlug(lost.replacedBy, lost.replacedById)}/`}>{lost.replacedBy}</a> : lost.replacedBy}</dd></div>}
        </dl>

        {d?.rank_global ? (
          <div className="ranks">
            <span><b>#{d.rank_global}</b> in the world</span>
            <span><b>#{d.rank_city}</b> in <span className="place">{t.city}</span></span>
            <span><b>#{d.rank_district}</b> in <span className="place">{t.district}</span></span>
          </div>
        ) : null}

        <div className="actions">
          {d?.ctbuh_url && <a className="btn primary" href={d.ctbuh_url} target="_blank" rel="noopener">View on CTBUH ↗</a>}
          {lost && <a className={"btn" + (d?.ctbuh_url ? "" : " primary")} href={lost.source} target="_blank" rel="noopener">{/wikipedia\.org/.test(lost.source) ? "Wikipedia" : "Source"} ↗</a>}
          <button className="btn" onClick={share}>{copied ? "Link copied" : "Share"}</button>
        </div>

        <details className="loc">
          <summary>How this pin was placed</summary>
          <p>{lost ? "Where the tower stood, from its source" : PRECISION_LABEL[t.precision] ?? t.precision}{d?.coord_note ? <> — {d.coord_note}</> : null}</p>
          {t.sharesPoint > 0 && <p className="muted">The source gives one point for this whole complex; {t.sharesPoint} other tower{t.sharesPoint > 1 ? "s" : ""} share it.</p>}
          <p className="muted">
            {t.lat.toFixed(5)}, {t.lon.toFixed(5)} ·{" "}
            <a href={`https://www.openstreetmap.org/?mlat=${t.lat}&mlon=${t.lon}#map=18/${t.lat}/${t.lon}`} target="_blank" rel="noopener">OpenStreetMap</a>
            {d?.osm_way ? <> · <a href={`https://www.openstreetmap.org/way/${d.osm_way}`} target="_blank" rel="noopener">footprint</a></> : null}
          </p>
        </details>
        <p className="credit">{lost ? "This tower is no longer standing, so it is not in the CTBUH list the map is built on; its facts come from the source linked above." : "Building data © CTBUH / The Skyscraper Center."}</p>
      </div>
    </aside>
  );
}
