import type { Geo } from "./history";

/**
 * Two helpers over the cell centres, both on a 1024 × 1024 grid of Web Mercator buckets (about 39 km at the equator):
 * finding the cell under a point (the nearest centre, as the map draws it), and placing each state's label where it
 * is widest (the bucket farthest from its border, by a chamfer distance transform of the year's owners).
 */
export const B = 1024;
/** must match historyLayer's disc radius: a point farther than this from every centre is sea */
const DISC_R = 1.45 * 9.85 / 40075.017;
const ROW0 = 100, ROW1 = 760;   // the buckets that hold land (about 84°N to 62°S)

export class CellGrid {
  readonly bucket: Int32Array;     // per cell
  private start: Int32Array;       // CSR over buckets
  private cells: Int32Array;
  constructor(readonly geo: Geo) {
    const { N, x, y } = geo;
    this.bucket = new Int32Array(N);
    const count = new Int32Array(B * B + 1);
    for (let i = 0; i < N; i++) {
      const bx = Math.min(B - 1, Math.max(0, Math.floor(x[i] * B))), by = Math.min(B - 1, Math.max(0, Math.floor(y[i] * B)));
      const b = by * B + bx;
      this.bucket[i] = b; count[b + 1]++;
    }
    for (let b = 0; b < B * B; b++) count[b + 1] += count[b];
    this.start = count;
    this.cells = new Int32Array(N);
    const fill = count.slice(0, B * B);
    for (let i = 0; i < N; i++) this.cells[fill[this.bucket[i]]++] = i;
  }

  /** The cell at Mercator (mx, my), or -1 at sea. */
  find(mx: number, my: number): number {
    mx -= Math.floor(mx);
    const sec = Math.cosh(Math.PI * (1 - 2 * my));
    const lim = DISC_R * sec;
    const rad = Math.min(8, Math.ceil(lim * B));
    const bx = Math.floor(mx * B), by = Math.floor(my * B);
    let best = -1, bd = lim * lim;
    for (let j = by - rad; j <= by + rad; j++) {
      if (j < 0 || j >= B) continue;
      for (let i = bx - rad; i <= bx + rad; i++) {
        const ii = (i + B) % B, b = j * B + ii;
        for (let k = this.start[b]; k < this.start[b + 1]; k++) {
          const c = this.cells[k];
          let dx = this.geo.x[c] - mx;
          if (dx > 0.5) dx -= 1; else if (dx < -0.5) dx += 1;
          const dy = this.geo.y[c] - my, d = dx * dx + dy * dy;
          if (d < bd) { bd = d; best = c; }
        }
      }
    }
    return best;
  }

  private keyBuf = new Int32Array(B * B);
  private dist = new Float32Array(B * B);

  /**
   * For every key (owner, or realm), the bucket farthest from any other key: [key, mx, my, radius in Mercator units].
   * Keys of 0 (nobody) are skipped.
   */
  interiors(keyOf: (cell: number) => number): Map<number, [number, number, number]> {
    const key = this.keyBuf, dist = this.dist;
    key.fill(-1, ROW0 * B, ROW1 * B);
    for (let i = 0; i < this.geo.N; i++) {
      const b = this.bucket[i];
      if (b >= ROW0 * B && b < ROW1 * B) key[b] = keyOf(i);
    }
    const D = 1.4142;
    // forward pass: a neighbour of another key (or the sea) counts as distance 0
    for (let j = ROW0; j < ROW1; j++) {
      const up = j > ROW0;
      for (let i = 0; i < B; i++) {
        const p = j * B + i, k = key[p];
        if (k <= 0) { dist[p] = 0; continue; }
        let d = 1, q: number, v: number;
        if (up && i > 0) {
          d = 1e9;
          q = p - B; v = (key[q] === k ? dist[q] : 0) + 1; if (v < d) d = v;
          q = p - B - 1; v = (key[q] === k ? dist[q] : 0) + D; if (v < d) d = v;
          if (i < B - 1) { q = p - B + 1; v = (key[q] === k ? dist[q] : 0) + D; if (v < d) d = v; }
          q = p - 1; v = (key[q] === k ? dist[q] : 0) + 1; if (v < d) d = v;
        }
        dist[p] = d;
      }
    }
    // backward pass
    for (let j = ROW1 - 1; j >= ROW0; j--) {
      const down = j < ROW1 - 1;
      for (let i = B - 1; i >= 0; i--) {
        const p = j * B + i, k = key[p];
        if (k <= 0) continue;
        let d = dist[p], q: number, v: number;
        if (down && i < B - 1) {
          q = p + B; v = (key[q] === k ? dist[q] : 0) + 1; if (v < d) d = v;
          q = p + B + 1; v = (key[q] === k ? dist[q] : 0) + D; if (v < d) d = v;
          if (i > 0) { q = p + B - 1; v = (key[q] === k ? dist[q] : 0) + D; if (v < d) d = v; }
          q = p + 1; v = (key[q] === k ? dist[q] : 0) + 1; if (v < d) d = v;
        } else d = Math.min(d, 1);
        dist[p] = d;
      }
    }
    const out = new Map<number, [number, number, number]>();
    for (let p = ROW0 * B; p < ROW1 * B; p++) {
      const k = key[p];
      if (k <= 0) continue;
      const cur = out.get(k), d = dist[p];
      if (!cur || d > cur[2]) out.set(k, [((p % B) + 0.5) / B, (Math.floor(p / B) + 0.5) / B, d]);
    }
    for (const v of out.values()) v[2] /= B;
    return out;
  }
}

/* ---- Web Mercator */
export const lngToX = (lng: number) => (lng + 180) / 360;
export const latToY = (lat: number) => (1 - Math.log(Math.tan(Math.PI / 4 + (lat * Math.PI) / 360)) / Math.PI) / 2;
export const xToLng = (x: number) => x * 360 - 180;
export const yToLat = (y: number) => (Math.atan(Math.sinh(Math.PI * (1 - 2 * y))) * 180) / Math.PI;
