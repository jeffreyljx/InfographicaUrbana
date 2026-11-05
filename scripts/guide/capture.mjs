// Records the modes' guide media from a local build (Jeffrey, 4 Nov 2026): a short demo clip per mode and a picture of
// each year dock with the positions of its parts, used by the guide pages (src/app/**/guide/page.tsx).
//
//   npm run build && python3 -m http.server 3456 --directory out &
//   node scripts/guide/capture.mjs http://localhost:3456 [scraper|transit|industry|history ...]
//
// Writes public/guide/<mode>.mp4 (H.264, needs ffmpeg), <mode>.jpg (its first frame, the poster), <mode>-dock.png, and
// the clip sizes and dock part positions into src/lib/guideMedia.json. Basemap tiles come from tiles.openfreemap.org.
import { createRequire } from "node:module";
import { execFileSync } from "node:child_process";
import { mkdtempSync, readFileSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

const BASE = process.argv[2] ?? "http://localhost:3456";
const ONLY = process.argv.slice(3);
const ROOT = new URL("../../", import.meta.url).pathname;
const OUT = join(ROOT, "public/guide");
const MEDIA = join(ROOT, "src/lib/guideMedia.json");
const VIEW = { width: 1280, height: 720 };   // the clip's frame, at 1.5x, encoded at 1440 wide
const CLIP_W = 1440;

// Playwright as installed on the machine (a plain require finds it through NODE_PATH, an ES import would not)
const { chromium } = createRequire(import.meta.url)("playwright");
const media = JSON.parse(readFileSync(MEDIA, "utf8"));
const browser = await chromium.launch();

async function open(url, wait = 6000) {
  const ctx = await browser.newContext({ viewport: VIEW, deviceScaleFactor: 1.5 });
  // a first visit would show the note pointing to the guide; the clips leave it out
  await ctx.addInitScript(() => { try { for (const m of ["scraper", "transit", "industry", "history"]) localStorage.setItem(`infographica.guide-seen.${m}`, "1"); } catch { /* */ } });
  const page = await ctx.newPage();
  await page.goto(BASE + url, { waitUntil: "load" });
  await page.waitForTimeout(wait);
  return page;
}

/** frames → mp4: each frame shown for its own time (seconds); the first frame is also saved as the poster */
function encode(name, frames, dir) {
  const list = frames.map(f => `file '${f.file}'\nduration ${f.t}`).join("\n") + `\nfile '${frames.at(-1).file}'\n`;
  writeFileSync(join(dir, "list.txt"), list);
  execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", join(dir, "list.txt"),
    "-vf", `scale=${CLIP_W}:-2:flags=lanczos,fps=12,format=yuv420p`, "-c:v", "libx264", "-preset", "slow", "-crf", "27",
    "-movflags", "+faststart", "-an", join(OUT, `${name}.mp4`)]);
  execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-i", frames[0].file, "-vf", `scale=${CLIP_W}:-2:flags=lanczos`, "-q:v", "4", join(OUT, `${name}.jpg`)]);
  media[name].demo = { w: CLIP_W, h: Math.round(CLIP_W * VIEW.height / VIEW.width) };
}

/** a ring where the next click lands, so the clip shows what was pressed */
async function tap(page, locator) {
  const r = await locator.boundingBox();
  if (!r) return;
  await page.evaluate(r => {
    const d = document.createElement("div");
    d.className = "demo-tap";
    Object.assign(d.style, { position: "fixed", left: `${r.x + r.width / 2 - 22}px`, top: `${r.y + r.height / 2 - 22}px`, width: "44px", height: "44px",
      borderRadius: "50%", border: "3px solid #E2560F", background: "rgba(226,86,15,.18)", zIndex: 99999, pointerEvents: "none" });
    document.body.appendChild(d);
  }, r);
}
const untap = page => page.evaluate(() => document.querySelectorAll(".demo-tap").forEach(e => e.remove()));

/** park the pointer on the dock's year, where it raises no hover label on the map or reading on the bars */
async function restPointer(page) {
  const b = await page.locator(".capsule .cap-year").boundingBox();
  if (b) await page.mouse.move(b.x + b.width / 2, b.y + b.height / 2);
}

/** step the dock's slider one year at a time with the arrow key, a frame per year */
async function stepYears(page, n, dir, frames, { settle = 450, t = 0.22, hold = 2.4 } = {}) {
  const slider = page.locator(".capsule input[type=range]");
  await slider.focus();
  for (let i = 0; i <= n; i++) {
    if (i) { await page.keyboard.press("ArrowRight"); await page.waitForTimeout(settle); }
    // the focus ring on the slider is not part of the picture
    await page.evaluate(() => (document.activeElement)?.blur?.());
    const file = join(dir, `f${String(frames.length).padStart(4, "0")}.png`);
    await page.screenshot({ path: file });
    frames.push({ file, t: i === n ? hold : t });
    await slider.focus();
  }
}

/** the dock, with a margin, and where its parts are in the picture (fractions of its width and height) */
async function dock(page, name, parts) {
  const M = 16;
  const box = await page.locator(".capsule").boundingBox();
  const clip = { x: box.x - M, y: box.y - M, width: box.width + 2 * M, height: box.height + 2 * M };
  await page.screenshot({ path: join(OUT, `${name}-dock.png`), clip });
  const at = await page.evaluate(({ parts, clip }) => {
    const out = {};
    for (const [k, sel, where] of parts) {
      const el = document.querySelector(sel);
      if (!el) continue;
      const r = el.getBoundingClientRect();
      const [x, y] = where === "left" ? [r.left - 8, r.top + r.height / 2] : where === "right" ? [r.right + 8, r.top + r.height / 2]
        : where === "corner" ? [r.left - 7, r.top - 7] : [r.left + r.width / 2, r.top - 4];
      out[k] = [+((x - clip.x) / clip.width).toFixed(4), +((y - clip.y) / clip.height).toFixed(4)];
    }
    return out;
  }, { parts, clip });
  media[name].dock = { w: Math.round(clip.width), h: Math.round(clip.height), at };
}

const TRACK = [
  ["key", ".capsule .cap-key", "left"],
  ["bars", ".capsule .cap-bars", "right"],
  ["slider", ".capsule .cap-track input[type=range]", "left"],
];

const jobs = {
  async scraper(dir) {
    // Downtown Dubai from 2000: open on the Burj Khalifa's pin, close its card, step back a little, and play
    const page = await open("/?id=3&year=2000", 9000);
    await page.locator(".panel .x").click();
    await page.waitForTimeout(800);
    await page.locator(".maplibregl-ctrl-zoom-out").click();
    await page.waitForTimeout(2500);
    await restPointer(page);
    const frames = [];
    await stepYears(page, 2026 - 2000, dir, frames, { settle: 600, t: 0.32 });
    encode("scraper", frames, dir);
    await page.close();
    // the dock on its own, for the parts: the whole world in 2000
    const p2 = await open("/?year=2000", 8000);
    await restPointer(p2);
    await dock(p2, "scraper", [["play", ".capsule .cap-play", "corner"], ["year", ".capsule .cap-year", "corner"], ["facts", ".capsule .cap-facts", "corner"],
      ["min", ".capsule .cap-min", "corner"], ["close", ".capsule .cap-min + .x", "corner"], ...TRACK]);
  },
  async transit(dir) {
    // Shanghai from 1995, its card open, so the dock counts Shanghai alone
    const page = await open("/metro/?system=cn-shanghai-metro&year=1995", 9000);
    await restPointer(page);
    const frames = [];
    await stepYears(page, 2026 - 1995, dir, frames, { settle: 600, t: 0.28 });
    encode("transit", frames, dir);
    await page.close();
    const p2 = await open("/metro/?year=2000", 8000);
    await restPointer(p2);
    await dock(p2, "transit", [["play", ".capsule .cap-play", "corner"], ["year", ".capsule .cap-year", "corner"], ["facts", ".capsule .cap-facts", "corner"],
      ["min", ".capsule .cap-min", "corner"], ...TRACK]);
  },
  async history(dir) {
    // the Mongol conquests, 1206 to 1260, the map left free of the card
    const page = await open("/history/?year=1206&state=mongol-empire", 10000);
    await page.locator(".panel .x").click().catch(() => {});
    await page.waitForTimeout(1500);
    // out to the whole of Asia and eastern Europe, where the empire will spread
    for (let i = 0; i < 2; i++) { await page.locator(".maplibregl-ctrl-zoom-out").click(); await page.waitForTimeout(900); }
    await page.mouse.move(560, 300); await page.mouse.down(); await page.mouse.move(800, 250, { steps: 12 }); await page.mouse.up();
    await page.waitForTimeout(2500);
    await restPointer(page);
    const frames = [];
    await stepYears(page, 1260 - 1206, dir, frames, { settle: 700, t: 0.2 });
    encode("history", frames, dir);
    await page.close();
    const p2 = await open("/history/?year=1300", 10000);
    await restPointer(p2);
    await dock(p2, "history", [["play", ".capsule .cap-play", "corner"], ["year", ".capsule .cap-year", "corner"], ["facts", ".capsule .cap-facts", "corner"],
      ["caption", ".capsule .h-caps", "left"], ["speed", ".capsule .cap-speed", "corner"], ["min", ".capsule .cap-min", "corner"], ...TRACK]);
  },
  async industry(dir) {
    // the switches, one press at a time, then a city's card
    const page = await open("/industry/", 8000);
    const frames = [];
    const shot = async t => { const file = join(dir, `f${String(frames.length).padStart(4, "0")}.png`); await page.screenshot({ path: file }); frames.push({ file, t }); };
    const press = async label => {
      const b = page.locator(".ind-controls .seg button", { hasText: new RegExp(`^${label}$`) }).first();
      await tap(page, b); await shot(0.9);
      await untap(page); await b.click(); await page.waitForTimeout(1200); await shot(2.2);
    };
    await shot(2.2);
    await press("Industrial output");
    await press("Countries");
    await press("Cities");
    await press("Trade");
    await page.goto(BASE + "/industry/?place=hong-kong", { waitUntil: "load" });
    await page.waitForTimeout(6000);
    await shot(3.5);
    encode("industry", frames, dir);
  },
};

for (const [name, job] of Object.entries(jobs)) {
  if (ONLY.length && !ONLY.includes(name)) continue;
  const dir = mkdtempSync(join(tmpdir(), `guide-${name}-`));
  console.log(name);
  await job(dir);
  rmSync(dir, { recursive: true, force: true });
}
writeFileSync(MEDIA, JSON.stringify(media, null, 2) + "\n");
await browser.close();
