// 1. Reassemble + unpack the dataset (data/data.br.part*) into public/data and src/data.
// 2. Copy MapLibre's worker files into /public so the map can start its worker from a fixed URL.
// 3. Copy the site font (Libre Baskerville, from @fontsource) into /public/fonts; globals.css declares the @font-faces.
// 4. Work out each city's skyline extent year by year for the time capsule (scripts/skyline-years.mjs).
import { copyFileSync, mkdirSync, readdirSync, readFileSync, writeFileSync, existsSync } from "node:fs";
import { brotliDecompressSync } from "node:zlib";
import { derivePlaces } from "./derive.mjs";
import { applyCountryLabels, active, LABELS, MERGE } from "./country-labels.mjs";
import { buildSkylineYears } from "./skyline-years.mjs";

const parts = existsSync("data") ? readdirSync("data").filter(f => /^data\.br\.part\d+$/.test(f)).sort() : [];
if (parts.length) {
  const raw = brotliDecompressSync(Buffer.concat(parts.map(f => readFileSync(`data/${f}`))));
  const hlen = raw.readUInt32BE(0);
  const header = JSON.parse(raw.subarray(4, 4 + hlen).toString());
  mkdirSync("public/data", { recursive: true }); mkdirSync("src/data", { recursive: true });
  let off = 4 + hlen;
  for (const [name, len] of header) {
    const body = raw.subarray(off, off + len); off += len;
    writeFileSync(`public/data/${name}`, body); writeFileSync(`src/data/${name}`, body);
  }
  console.log(`data: unpacked ${header.map(h => h[0]).join(", ")} from ${parts.length} parts`);
  const idx = JSON.parse(readFileSync("public/data/towers.json")); const det = JSON.parse(readFileSync("public/data/details.json"));
  const places = JSON.stringify(derivePlaces(idx, det));
  writeFileSync("public/data/places.json", places); writeFileSync("src/data/places.json", places);
  console.log("data: derived places.json");
} else {
  console.log("data: no packed parts found, using existing JSON");
}
// Country display labels and Countries-table merges (Taiwan -> "Taiwan, China", counted under China); see scripts/country-labels.mjs. Applied after derivePlaces so the
// derivation and scripts/build_data.py keep working on the dataset's own names.
if (active()) console.log(`data: relabelled ${applyCountryLabels()} country strings (${[...Object.entries(LABELS).map(([a, b]) => `${a} -> ${b}`), ...Object.entries(MERGE).map(([a, b]) => `${a} counted under ${b}`)].join("; ")})`);

mkdirSync("public/maplibre", { recursive: true });
for (const f of ["maplibre-gl-worker.mjs", "maplibre-gl-shared.mjs"]) copyFileSync(`node_modules/maplibre-gl/dist/${f}`, `public/maplibre/${f}`);
console.log("maplibre worker copied");

// weights 400-700 upright + 400 italic, Latin and Latin Extended; keep in step with the @font-face list in globals.css
const FONT = "node_modules/@fontsource/libre-baskerville", FONT_OUT = "public/fonts/libre-baskerville";
mkdirSync(FONT_OUT, { recursive: true });
const faces = [400, 500, 600, 700].map(w => `${w}-normal`).concat("400-italic");
for (const sub of ["latin", "latin-ext"]) for (const f of faces) copyFileSync(`${FONT}/files/libre-baskerville-${sub}-${f}.woff2`, `${FONT_OUT}/libre-baskerville-${sub}-${f}.woff2`);
copyFileSync(`${FONT}/LICENSE`, `${FONT_OUT}/OFL.txt`);
console.log(`font copied (${faces.length * 2} files)`);

buildSkylineYears();
