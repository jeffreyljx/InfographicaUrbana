/** InfographicaUrbana's mark (Jeffrey, 31 Oct 2026: the site renamed from ScraperMap, with new logos and icons): a
 *  bar chart that is also a skyline, three bars rising left to right on a baseline, the tallest a tower with a pointed
 *  top. The bars use the site's three ink colours: deep teal, dark blue and burnt sienna. The same drawing, on a pale
 *  tile, is the favicon (src/app/icon.svg) and the app icons (public/icons/, drawn by scripts/brand/make-icons.mjs). */
export function BrandMark({ size = 20 }: { size?: number }) {
  return (
    <svg className="mark" width={size} height={size} viewBox="8 8 48 48" aria-hidden="true" focusable="false">
      <rect x="11" y="33" width="11" height="19" fill="#164C48" />
      <rect x="26.5" y="23" width="11" height="29" fill="#1C3F7A" />
      <path d="M42 52V17l5.5-7 5.5 7v35z" fill="#7F2F16" />
      <rect x="8" y="51" width="48" height="3" rx="1.5" fill="#2B1D17" />
    </svg>
  );
}

/** The name as it is set in the top bar: "Infographica" in bold, "Urbana" in italic sienna, one word. */
export function BrandName() {
  return <span className="brand-name">Infographica<i>Urbana</i></span>;
}
