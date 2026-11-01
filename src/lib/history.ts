/**
 * CartaHistoria's data, read from public/history/ (packed by scripts/history/pack.py from the historical-borders
 * project): the state table, the cell centres, and one chunk per window (a century before 1600, a decade after),
 * loaded on demand as the year moves. A chunk holds every cell's owner, status and second party at the window's start
 * and the groups of cells that change in each of its years, so any year is its window's start plus the groups up to it.
 *
 * Cells are the project's 524,441 H3 resolution-5 land cells (about 253 km² each); a cell's id is its line in the
 * project's grid file. Owners are 1 + a row of states.json (0: nobody's land). Status: 0 direct, 1 vassal,
 * 2 constituent (a member drawn inside its parent: an Imperial Estate, a Soviet republic), 3 occupied, 4 contested;
 * the second party is the suzerain (vassal, constituent), the occupier, or the other claimant.
 */

export const FIRST_YEAR = -6000;
export const LAST_YEAR = 2026;
export const ST_DIRECT = 0, ST_VASSAL = 1, ST_CONSTITUENT = 2, ST_OCCUPIED = 3, ST_CONTESTED = 4;
export const STATUS_NAME = ["", "vassal", "constituent", "occupied", "contested"];

export interface HistIndex {
  built: string; N: number; Q: number; first: number; last: number; P: number; cellKm2: number;
  windows: { id: string; from: number; to: number; kb: number; src: string }[];
  /** cells whose owner or status changed, per year from `first` */
  changed: number[];
}
export interface HistStates {
  built: string; count: number; neutral: string; cellKm2: number;
  slug: string[]; name: string[]; type: string[]; start: (number | null)[]; end: (number | null)[];
  colour: string[]; fb: number[]; first: (number | null)[]; last: (number | null)[]; peak: number[]; peakYear: (number | null)[];
  capitals: [string, number, number, number, number][][]; alt: string[][]; wiki: string[];
}
export interface Caption { y: number; m?: number; s: number; t: string; x: string; u?: string }
export interface Chunk {
  id: string; from: number; to: number;
  owner: Uint16Array; status: Uint8Array; other: Uint16Array;
  gYear: Int32Array; gOwner: Uint16Array; gStatus: Uint8Array; gOther: Uint16Array;
  /** index of each group's first run (prefix sums of the run counts), length G + 1 */
  gRun0: Uint32Array;
  rStart: Uint32Array; rLen: Uint32Array;
  captions: Caption[];
}
export interface Geo {
  N: number;
  /** cell centres in Web Mercator, 0..1 */
  x: Float32Array; y: Float32Array;
}

export const TYPE_LABEL: Record<string, string> = { s: "State", d: "Dynasty", c: "Archaeological culture", k: "Colony", r: "Rebel state", u: "Association", n: "Named party" };

/* ---------------------------------------------------------------- loading */

async function gunzip(buf: ArrayBuffer): Promise<ArrayBuffer> {
  const b = new Uint8Array(buf);
  if (b[0] !== 0x1f || b[1] !== 0x8b) return buf;           // a host that already decoded it
  const ds = new DecompressionStream("gzip");
  return new Response(new Blob([buf]).stream().pipeThrough(ds)).arrayBuffer();
}
async function fetchBin(url: string): Promise<ArrayBuffer> {
  const r = await fetch(url);
  if (!r.ok) throw new Error(`${url}: ${r.status}`);
  return gunzip(await r.arrayBuffer());
}
async function fetchJson<T>(url: string): Promise<T> {
  const r = await fetch(url);
  if (!r.ok) throw new Error(`${url}: ${r.status}`);
  return r.json() as Promise<T>;
}

let indexP: Promise<HistIndex> | null = null;
let statesP: Promise<HistStates> | null = null;
let geoP: Promise<Geo> | null = null;
export const loadIndex = () => (indexP ??= fetchJson<HistIndex>("/history/index.json"));
export const loadStates = () => (statesP ??= fetchJson<HistStates>("/history/states.json"));

/** geo.bin: "CHG1", N, Q, then dx and dy as delta-coded i32 split into byte planes. */
export const loadGeo = () => (geoP ??= fetchBin("/history/geo.bin").then(buf => {
  const dv = new DataView(buf);
  if (dv.getUint32(0, true) !== 0x31474843) throw new Error("geo.bin: bad magic");
  const N = dv.getUint32(4, true), Q = dv.getUint32(8, true);
  const bytes = new Uint8Array(buf, 12);
  const col = (k: number) => {
    const out = new Float32Array(N);
    const base = k * 4 * N;
    let acc = 0;
    for (let i = 0; i < N; i++) {
      const v = bytes[base + i] | (bytes[base + N + i] << 8) | (bytes[base + 2 * N + i] << 16) | (bytes[base + 3 * N + i] << 24);
      acc += v;
      out[i] = acc / Q;
    }
    return out;
  };
  return { N, x: col(0), y: col(1) };
}));

const chunks = new Map<string, Promise<Chunk>>();
export function loadChunk(id: string): Promise<Chunk> {
  let p = chunks.get(id);
  if (!p) {
    p = fetchBin(`/history/w/${id}.bin`).then(decodeChunk);
    p.catch(() => chunks.delete(id));
    chunks.set(id, p);
    // keep the memory bounded: a decoded window is about 2.6 MB
    if (chunks.size > 8) chunks.delete(chunks.keys().next().value!);
  }
  return p;
}

function decodeChunk(buf: ArrayBuffer): Chunk {
  const dv = new DataView(buf);
  if (dv.getUint32(0, true) !== 0x31574843) throw new Error("chunk: bad magic");
  const hl = dv.getUint32(4, true);
  const h = JSON.parse(new TextDecoder().decode(new Uint8Array(buf, 8, hl))) as {
    window: string; from: number; to: number; N: number; G: number; R: number; captions: Caption[];
    sections: Record<string, [number, number]>;
  };
  const base = 8 + hl;
  const sec = <T,>(name: string, C: { new (b: ArrayBuffer, o: number, n: number): T; BYTES_PER_ELEMENT: number }) => {
    const [o, n] = h.sections[name];
    // copy, so the chunk owns aligned memory whatever the header length was
    return new C(buf.slice(base + o, base + o + n), 0, n / C.BYTES_PER_ELEMENT);
  };
  const gRuns = sec("g_runs", Uint32Array);
  const gRun0 = new Uint32Array(h.G + 1);
  for (let g = 0; g < h.G; g++) gRun0[g + 1] = gRun0[g] + gRuns[g];
  const rStart = sec("r_start", Uint32Array);
  for (let i = 1; i < rStart.length; i++) rStart[i] += rStart[i - 1];   // delta-coded
  return {
    id: h.window, from: h.from, to: h.to,
    owner: sec("owner", Uint16Array), status: sec("status", Uint8Array), other: sec("other", Uint16Array),
    gYear: sec("g_year", Int32Array), gOwner: sec("g_owner", Uint16Array), gStatus: sec("g_status", Uint8Array), gOther: sec("g_other", Uint16Array),
    gRun0, rStart, rLen: sec("r_len", Uint32Array), captions: h.captions,
  };
}

export function windowFor(idx: HistIndex, year: number) {
  const w = idx.windows;
  let lo = 0, hi = w.length - 1;
  while (lo < hi) {
    const mid = (lo + hi + 1) >> 1;
    if (w[mid].from <= year) lo = mid; else hi = mid - 1;
  }
  return w[lo];
}

/* ---------------------------------------------------------------- the year's map */

/**
 * The map in one year: every cell's owner, status and second party after that year's changes, and which cells a
 * state gained that year (drawn with the bright first-year edge). Moving forward a year applies just that year's
 * groups; any other move restarts from the window's start.
 */
export class Timeline {
  owner: Uint16Array; status: Uint8Array; other: Uint16Array;
  /** 1 for a cell whose owner changed to a state in this year */
  gained: Uint8Array;
  year: number | null = null;
  chunk: Chunk | null = null;
  private gainedList: number[] = [];
  /** bumped on every change, so the layer and the labels know to refresh */
  version = 0;

  constructor(readonly N: number) {
    this.owner = new Uint16Array(N); this.status = new Uint8Array(N); this.other = new Uint16Array(N); this.gained = new Uint8Array(N);
  }

  /** Bring the map to `year` using `chunk` (the window that holds it). */
  apply(chunk: Chunk, year: number) {
    let from: number;
    if (this.chunk === chunk && this.year !== null && year >= this.year) {
      if (year === this.year) return;
      from = this.year + 1;
    } else {
      this.owner.set(chunk.owner); this.status.set(chunk.status); this.other.set(chunk.other);
      from = chunk.from;
    }
    for (const c of this.gainedList) this.gained[c] = 0;
    this.gainedList = [];
    const { gYear, gOwner, gStatus, gOther, gRun0, rStart, rLen } = chunk;
    // groups are in year order
    let g = lowerBound(gYear, from);
    for (; g < gYear.length && gYear[g] <= year; g++) {
      const o = gOwner[g], s = gStatus[g], t = gOther[g], mark = gYear[g] === year;
      for (let r = gRun0[g]; r < gRun0[g + 1]; r++) {
        const a = rStart[r], b = a + rLen[r];
        if (mark && o) for (let c = a; c < b; c++) if (this.owner[c] !== o) { this.gained[c] = 1; this.gainedList.push(c); }
        this.owner.fill(o, a, b); this.status.fill(s, a, b); this.other.fill(t, a, b);
      }
    }
    this.chunk = chunk; this.year = year; this.version++;
  }
}

function lowerBound(a: Int32Array, v: number) {
  let lo = 0, hi = a.length;
  while (lo < hi) { const m = (lo + hi) >> 1; if (a[m] < v) lo = m + 1; else hi = m; }
  return lo;
}

/** Cells per owner (index = owner id). */
export function areas(t: Timeline, P: number): Uint32Array {
  const a = new Uint32Array(P + 1);
  const o = t.owner;
  for (let i = 0; i < o.length; i++) a[o[i]]++;
  return a;
}

/* ---------------------------------------------------------------- years on the dock */

/** "44 BCE", "800", "0" (the data's year 0 is kept as it is). */
export function fmtYear(y: number, ce = false): string {
  if (y < 0) return `${-y} BCE`;
  return ce && y > 0 && y < 1000 ? `${y} CE` : String(y);
}

/**
 * The dock's slider is slower before 1500, so the modern era is not a sliver: 6000 to 1000 BCE takes 15% of its
 * length, 1000 BCE to 1500 CE 45%, and 1500 to 2026 the last 40% (a year there is about 13 times as wide as one
 * before 1000 BCE... and 6 times one in antiquity and the Middle Ages).
 */
const STOPS: [number, number][] = [[FIRST_YEAR, 0], [-1000, 0.15], [1500, 0.6], [LAST_YEAR, 1]];
export function yearToPos(y: number): number {
  for (let i = 1; i < STOPS.length; i++) {
    const [y0, p0] = STOPS[i - 1], [y1, p1] = STOPS[i];
    if (y <= y1) return p0 + (p1 - p0) * (Math.max(y, y0) - y0) / (y1 - y0);
  }
  return 1;
}
export function posToYear(p: number): number {
  for (let i = 1; i < STOPS.length; i++) {
    const [y0, p0] = STOPS[i - 1], [y1, p1] = STOPS[i];
    if (p <= p1) return Math.round(y0 + (y1 - y0) * (Math.max(p, p0) - p0) / (p1 - p0));
  }
  return LAST_YEAR;
}
export const YEAR_TICKS = [-6000, -1000, 0, 500, 1000, 1500, 1600, 1700, 1800, 1900, 2000];
/** a caption without its leading date ("618: ", "Dec 618: ", "1905-1906: "), which the dock already shows */
export const undated = (s: string) => s.replace(/^[^:]{0,24}\d[^:]{0,14}:\s+/, "");

/* ---------------------------------------------------------------- colour: OKLab (Björn Ottosson) */

export type RGB = [number, number, number];
const lin = (c: number) => c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4;
const gam = (c: number) => c <= 0.0031308 ? 12.92 * c : 1.055 * c ** (1 / 2.4) - 0.055;
export function hexToRgb(h: string): RGB {
  const n = parseInt(h.slice(1, 7), 16);
  return [(n >> 16 & 255) / 255, (n >> 8 & 255) / 255, (n & 255) / 255];
}
export function rgbToHex([r, g, b]: RGB): string {
  return "#" + [r, g, b].map(v => Math.round(Math.min(1, Math.max(0, v)) * 255).toString(16).padStart(2, "0")).join("");
}
export function rgbToOklab([r, g, b]: RGB): RGB {
  const R = lin(r), G = lin(g), B = lin(b);
  const l = Math.cbrt(0.4122214708 * R + 0.5363325363 * G + 0.0514459929 * B);
  const m = Math.cbrt(0.2119034982 * R + 0.6806995451 * G + 0.1073969566 * B);
  const s = Math.cbrt(0.0883024619 * R + 0.2817188376 * G + 0.6299787005 * B);
  return [0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s, 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s, 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s];
}
export function oklabToRgb([L, a, b]: RGB): RGB {
  const l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3;
  const m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3;
  const s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3;
  return [gam(4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s), gam(-1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s), gam(-0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)];
}
/** OKLCH adjustment (colours.json rules): chroma × cf, lightness + dl (clamped to [lmin, lmax]), then into sRGB. */
export function tint(hex: string, cf: number, dl: number, lmax = 0.94, lmin = 0): string {
  const [L, a, b] = rgbToOklab(hexToRgb(hex));
  const L2 = Math.max(lmin, Math.min(lmax, L + dl));
  let k = cf;
  for (let i = 0; i < 20; i++) {
    const rgb = oklabToRgb([L2, a * k, b * k]);
    if (rgb.every(v => v >= -0.001 && v <= 1.001)) return rgbToHex(rgb);
    k *= 0.9;
  }
  return rgbToHex(oklabToRgb([L2, 0, 0]));
}
/** The plan's tints: a vassal (chroma ×0.55, L +0.12), a culture (×0.4, +0.15), a label (L −0.30, not below 0.22). */
export const vassalTint = (hex: string) => tint(hex, 0.55, 0.12);
export const cultureTint = (hex: string) => tint(hex, 0.4, 0.15);
export const labelInk = (hex: string) => tint(hex, 0.9, -0.3, 1, 0.22);
export function blend(a: string, b: string): string {
  const A = rgbToOklab(hexToRgb(a)), B = rgbToOklab(hexToRgb(b));
  return rgbToHex(oklabToRgb([(A[0] + B[0]) / 2, (A[1] + B[1]) / 2, (A[2] + B[2]) / 2]));
}

/* ---------------------------------------------------------------- numbers */

export const fmtInt = (n: number) => Math.round(n).toLocaleString("en-US");
export function fmtArea(cells: number, km2PerCell = 252.9): string {
  const km = cells * km2PerCell;
  if (km >= 1e6) return `${(km / 1e6).toFixed(km >= 1e7 ? 1 : 2)} million km²`;
  if (km >= 1e4) return `${fmtInt(Math.round(km / 1000) * 1000)} km²`;
  return `${fmtInt(Math.round(km / 100) * 100)} km²`;
}
/** A state's capital in a year: the dossier's span that holds it (else the nearest one). */
export function capitalIn(caps: [string, number, number, number, number][], year: number) {
  if (!caps.length) return null;
  let best = caps[0], bd = Infinity;
  for (const c of caps) {
    if (c[3] <= year && year <= c[4]) return c;
    const d = Math.min(Math.abs(year - c[3]), Math.abs(year - c[4]));
    if (d < bd) { bd = d; best = c; }
  }
  return best;
}
export const yearsSpan = (a: number | null, b: number | null) =>
  a === null ? "" : b === null || b === a ? fmtYear(a) : a < 0 && b < 0 ? `${-a}–${-b} BCE` : a < 0 ? `${-a} BCE – ${b} CE` : `${a}–${b}`;
