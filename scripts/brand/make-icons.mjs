// InfographicaUrbana's icons and link-preview image, drawn from the mark in src/components/Logo.tsx (a bar chart that
// is also a skyline) and rendered with Playwright's Chromium. Run after `npm install` (the preview image uses the
// self-hosted Libre Baskerville in public/fonts/):  node scripts/brand/make-icons.mjs
// Writes: src/app/favicon.ico (16, 32, 48 px), src/app/apple-icon.png (180 px, square: iOS rounds the corners itself),
// public/icons/icon-192.png and icon-512.png (rounded tile), public/icons/icon-maskable-512.png (full bleed, the mark
// inside the safe circle) and public/og.png (1200 x 630, shown when a link to the site is shared).
// src/app/icon.svg, the favicon for browsers that take SVG, is the same tile written by hand.
import { createRequire } from "node:module";
import { execSync } from "node:child_process";
import { mkdirSync, writeFileSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..", "..");
const require = createRequire(import.meta.url);
let playwright;
try { playwright = require("playwright"); }
catch { playwright = createRequire(join(execSync("npm root -g").toString().trim(), "x"))("playwright"); }

const TILE = "#F4ECE9", SAND = "#E6D6CF";
// the mark, in a 64 x 64 box: three bars on a baseline, the tallest a tower with a pointed top
const MARK = `<rect x="11" y="33" width="11" height="19" fill="#164C48"/><rect x="26.5" y="23" width="11" height="29" fill="#1C3F7A"/>`
  + `<path d="M42 52V17l5.5-7 5.5 7v35z" fill="#7F2F16"/><rect x="8" y="51" width="48" height="3" rx="1.5" fill="#2B1D17"/>`;
const svg = (body) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="100%" height="100%">${body}</svg>`;
const tile = svg(`<rect width="64" height="64" rx="14" fill="${TILE}"/>${MARK}`);
const square = svg(`<rect width="64" height="64" fill="${TILE}"/>${MARK}`);
const maskable = svg(`<rect width="64" height="64" fill="${TILE}"/><g transform="translate(32 32) scale(.78) translate(-32 -31)">${MARK}</g>`);

const fonts = pathToFileURL(join(root, "public/fonts/libre-baskerville/")).href;
const og = `<!doctype html><html><head><style>
@font-face{font-family:LB;font-weight:400;src:url(${fonts}libre-baskerville-latin-400-normal.woff2)}
@font-face{font-family:LB;font-weight:700;src:url(${fonts}libre-baskerville-latin-700-normal.woff2)}
@font-face{font-family:LB;font-weight:400;font-style:italic;src:url(${fonts}libre-baskerville-latin-400-italic.woff2)}
html,body{margin:0;width:1200px;height:630px;background:${SAND};color:#2B1D17;font-family:LB,Georgia,serif;font-variant-numeric:lining-nums}
.wrap{position:absolute;inset:0;padding:104px 84px 0}
.lock{display:flex;align-items:center;gap:30px}
.lock svg{width:128px;height:128px;flex:none}
.name{font-size:78px;font-weight:700;letter-spacing:-.5px;line-height:1}
.name i{font-weight:400;color:#7F2F16}
.tag{margin:34px 0 0 4px;font-size:34px;color:#4E3B33}
.modes{position:absolute;left:84px;right:84px;bottom:78px;display:grid;grid-template-columns:repeat(3,1fr);gap:34px}
.mode{border-top:5px solid;padding-top:16px}
.mode b{display:block;font-size:29px;margin-bottom:8px}
.mode span{font-size:21px;color:#4E3B33;line-height:1.35}
</style></head><body><div class="wrap">
<div class="lock"><svg viewBox="8 8 48 48">${MARK}</svg><div class="name">Infographica<i>Urbana</i></div></div>
<div class="tag">The world&rsquo;s cities in maps and figures</div>
</div><div class="modes">
<div class="mode" style="border-color:#7F2F16"><b>ScraperMap</b><span>Every skyscraper of 150&nbsp;m and taller</span></div>
<div class="mode" style="border-color:#164C48"><b>TransitMap</b><span>The world&rsquo;s metro lines, year by year</span></div>
<div class="mode" style="border-color:#1C3F7A"><b>IndustryMap</b><span>Which cities trade and make the most</span></div>
</div></body></html>`;

const browser = await playwright.chromium.launch();
async function shot(html, w, h, transparent) {
  const page = await browser.newPage({ viewport: { width: w, height: h } });
  const doc = html.startsWith("<!doctype") ? html : `<!doctype html><html><body style="margin:0;background:transparent">${html}</body></html>`;
  await page.setContent(doc, { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  const png = await page.screenshot({ omitBackground: transparent, clip: { x: 0, y: 0, width: w, height: h } });
  await page.close();
  return png;
}
const box = (s, n) => `<div style="width:${n}px;height:${n}px">${s}</div>`;

mkdirSync(join(root, "public/icons"), { recursive: true });
writeFileSync(join(root, "src/app/apple-icon.png"), await shot(box(square, 180), 180, 180, false));
writeFileSync(join(root, "public/icons/icon-192.png"), await shot(box(tile, 192), 192, 192, true));
writeFileSync(join(root, "public/icons/icon-512.png"), await shot(box(tile, 512), 512, 512, true));
writeFileSync(join(root, "public/icons/icon-maskable-512.png"), await shot(box(maskable, 512), 512, 512, false));
writeFileSync(join(root, "public/og.png"), await shot(og, 1200, 630, false));

// favicon.ico: 16, 32 and 48 px PNGs in one ICO container
const sizes = [16, 32, 48];
const pngs = [];
for (const n of sizes) pngs.push(await shot(box(tile, n), n, n, true));
const head = Buffer.alloc(6 + 16 * sizes.length);
head.writeUInt16LE(0, 0); head.writeUInt16LE(1, 2); head.writeUInt16LE(sizes.length, 4);
let offset = head.length;
sizes.forEach((n, i) => {
  const e = 6 + 16 * i;
  head.writeUInt8(n, e); head.writeUInt8(n, e + 1); head.writeUInt8(0, e + 2); head.writeUInt8(0, e + 3);
  head.writeUInt16LE(1, e + 4); head.writeUInt16LE(32, e + 6);
  head.writeUInt32LE(pngs[i].length, e + 8); head.writeUInt32LE(offset, e + 12);
  offset += pngs[i].length;
});
writeFileSync(join(root, "src/app/favicon.ico"), Buffer.concat([head, ...pngs]));
await browser.close();

// the hand-written SVG favicon must stay the same drawing
const iconSvg = readFileSync(join(root, "src/app/icon.svg"), "utf8");
if (!iconSvg.includes(MARK.slice(0, 60))) console.warn("src/app/icon.svg no longer matches the mark drawn here");
console.log("icons written");
