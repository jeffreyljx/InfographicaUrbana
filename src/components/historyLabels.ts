"use client";
import type { Map as MLMap } from "maplibre-gl";
import { labelInk, ST_CONSTITUENT, ST_VASSAL, type HistStates, type Timeline } from "@/lib/history";
import type { CellGrid } from "@/lib/historyGrid";

/*
 * State names on the map, as HTML over the canvas (in the site's serif, with no glyph server needed): each state's
 * name sits at its widest point (CellGrid.interiors), sized to its area on screen, larger states in spaced capitals,
 * cultures in italic, and a realm that holds member states (the Holy Roman Empire, the USSR) faintly across all of
 * them. Bigger states win where two names would overlap; a name with no room is left out until the map is zoomed in.
 */

interface Cand {
  id: number; x: number; y: number; r: number; cells: number;
  text: string; ink: string; kind: "state" | "culture" | "realm";
}
interface Placed { el: HTMLDivElement; key: string }

const OBSTACLES = [".h-dock", ".topbar", ".h-legend", ".panel", ".h-about"];
/** a cell's share of the Web Mercator square at the equator (252.9 km² over the equator's length squared) */
const CELL_M2 = 252.9 / (40075.017 * 40075.017);

export class HistoryLabels {
  private root: HTMLDivElement;
  private pool: HTMLDivElement[] = [];
  private cands: Cand[] = [];
  private raf = 0;
  sel = 0;

  constructor(private map: MLMap, private grid: CellGrid, private st: HistStates) {
    this.root = document.createElement("div");
    this.root.className = "h-labels";
    this.root.setAttribute("aria-hidden", "true");
    map.getCanvasContainer().appendChild(this.root);
    map.on("move", this.schedule);
    map.on("resize", this.schedule);
  }

  destroy() {
    this.map.off("move", this.schedule); this.map.off("resize", this.schedule);
    cancelAnimationFrame(this.raf);
    this.root.remove();
  }

  private schedule = () => {
    if (this.raf) return;
    this.raf = requestAnimationFrame(() => { this.raf = 0; this.layout(); });
  };

  /** Recompute where each state's name goes, for the timeline's year. */
  update(tl: Timeline, area: Uint32Array) {
    const { owner, status, other } = tl;
    const inter = this.grid.interiors(c => owner[c]);
    const cands: Cand[] = [];
    // realms with member states: their union, labelled faintly
    let members = false;
    for (let i = 0; i < status.length; i++) if (status[i] === ST_CONSTITUENT) { members = true; break; }
    const realmed = new Set<number>();
    if (members) {
      const realmArea = new Map<number, number>();
      for (let i = 0; i < status.length; i++) if (status[i] === ST_CONSTITUENT) realmArea.set(other[i], (realmArea.get(other[i]) ?? 0) + 1);
      const ri = this.grid.interiors(c => status[c] === ST_CONSTITUENT ? other[c] : realmArea.has(owner[c]) ? owner[c] : 0);
      for (const [id, [x, y, r]] of ri) {
        if (!realmArea.has(id)) continue;
        realmed.add(id);
        cands.push({ id, x, y, r, cells: (realmArea.get(id) ?? 0) + area[id], text: short(this.st.name[id - 1]), ink: labelInk(this.st.colour[id - 1]), kind: "realm" });
      }
    }
    for (const [id, [x, y, r]] of inter) {
      if (realmed.has(id) || id > this.st.count) continue;
      const k = id - 1;
      // a vassal is drawn in its suzerain's tint, so its name takes the suzerain's ink
      const c = this.grid.find(x, y);
      const sz = c >= 0 && status[c] === ST_VASSAL && other[c] ? other[c] : id;
      cands.push({ id, x, y, r, cells: area[id], text: short(this.st.name[k]), ink: labelInk(this.st.colour[sz - 1]), kind: this.st.type[k] === "c" ? "culture" : "state" });
    }
    cands.sort((a, b) => b.cells - a.cells);
    this.cands = cands;
    this.layout();
  }

  layout() {
    const map = this.map;
    const cv = map.getCanvas();
    const w = cv.clientWidth, h = cv.clientHeight;
    const W = 512 * 2 ** map.getZoom();
    const c = map.getCenter();
    const cx = (c.lng + 180) / 360;
    const cy = (1 - Math.log(Math.tan(Math.PI / 4 + (c.lat * Math.PI) / 360)) / Math.PI) / 2;
    const boxes: [number, number, number, number][] = [];
    // the controls floating over the map are obstacles too
    const at = map.getContainer().getBoundingClientRect();
    for (const sel of OBSTACLES) {
      const el = map.getContainer().parentElement?.querySelector(sel);
      if (!el) continue;
      const r = el.getBoundingClientRect();
      if (r.width && r.height) boxes.push([r.left - at.left, r.top - at.top, r.right - at.left, r.bottom - at.top]);
    }
    let used = 0;
    const hit = (b: [number, number, number, number]) => boxes.some(o => b[0] < o[2] && b[2] > o[0] && b[1] < o[3] && b[3] > o[1]);
    // the picked state first, then states by size, then realms where their members' names leave room
    const order = [...this.cands.filter(k => k.id === this.sel), ...this.cands.filter(k => k.id !== this.sel && k.kind !== "realm"), ...this.cands.filter(k => k.id !== this.sel && k.kind === "realm")];
    for (const k of order) {
      let dx = k.x - cx; dx -= Math.round(dx);
      const sx = w / 2 + dx * W, sy = h / 2 + (k.y - cy) * W;
      if (sx < -200 || sx > w + 200 || sy < -60 || sy > h + 60) continue;
      const sec = Math.cosh(Math.PI * (1 - 2 * k.y));
      const areaPx = k.cells * CELL_M2 * sec * sec * W * W;
      const rPx = k.r * W;
      if (areaPx < 120 && k.id !== this.sel) continue;
      const n = Math.max(3, k.text.length);
      const span = Math.max(2.6 * rPx, 1.5 * Math.sqrt(areaPx));
      let fs: number, caps = false, lines = 1;
      if (k.kind === "realm") {
        fs = Math.min(30, span / (0.95 * n));
        caps = true;
        if (fs < 11) continue;
      } else {
        fs = Math.min(26, span / (0.56 * n), 1.5 * rPx + 4);
        if (fs >= 14) { caps = true; fs = Math.min(fs, span / (0.78 * n)); fs = Math.max(fs, 13.5); }
        if (fs < 9.5 && k.text.includes(" ")) {
          const longest = Math.max(...wrap(k.text).map(s => s.length));
          const f2 = Math.min(13, span / (0.56 * longest), rPx * 0.9 + 3);
          if (f2 > fs) { fs = f2; lines = 2; }
        }
        if (fs < 9.5) { if (k.id !== this.sel) continue; fs = 11; }
      }
      const cw = caps ? (k.kind === "realm" ? 0.95 : 0.78) : 0.56;
      const longest = lines === 2 ? Math.max(...wrap(k.text).map(s => s.length)) : n;
      const bw = fs * cw * longest + 6, bh = fs * 1.25 * lines + 2;
      const box: [number, number, number, number] = [sx - bw / 2, sy - bh / 2, sx + bw / 2, sy + bh / 2];
      // a name the screen's edge would cut is left out (the state is mostly off screen)
      if (box[0] < 2 || box[2] > w - 2 || box[1] < 56 || box[3] > h - 2) continue;
      if (hit(box)) continue;
      boxes.push(box);
      const el = this.pool[used] ?? this.make();
      used++;
      const cls = "h-label" + (k.kind === "realm" ? " realm" : k.kind === "culture" ? " culture" : "") + (caps ? " caps" : "") + (k.id === this.sel ? " sel" : "");
      const text = lines === 2 ? wrap(k.text).join("\n") : k.text;
      if (el.className !== cls) el.className = cls;
      if (el.textContent !== text) el.textContent = text;
      el.style.transform = `translate(${sx.toFixed(1)}px, ${sy.toFixed(1)}px) translate(-50%, -50%)`;
      el.style.fontSize = `${fs.toFixed(1)}px`;
      el.style.color = k.ink;
      el.style.display = "";
    }
    for (let i = used; i < this.pool.length; i++) this.pool[i].style.display = "none";
  }

  private make() {
    const el = document.createElement("div");
    el.className = "h-label";
    this.root.appendChild(el);
    this.pool.push(el);
    return el;
  }
}

/** A name as the map shows it: without a trailing parenthesis ("Holy Roman Empire (1260-1806)"). */
const short = (s: string) => s.replace(/\s*\([^)]*\)\s*$/, "") || s;

/** Two lines for a long name, broken at the space nearest its middle. */
function wrap(s: string): string[] {
  const mid = s.length / 2;
  let best = -1;
  for (let i = 0; i < s.length; i++) if (s[i] === " " && (best < 0 || Math.abs(i - mid) < Math.abs(best - mid))) best = i;
  return best < 0 ? [s] : [s.slice(0, best), s.slice(best + 1)];
}

export type { Placed };
