"use client";
import type { CustomLayerInterface, CustomRenderMethodInput, Map as MLMap } from "maplibre-gl";
import { hexToRgb, vassalTint, cultureTint, labelInk, type HistStates, type Geo, type Timeline } from "@/lib/history";

/*
 * CartaHistoria's cell layer: a MapLibre custom layer in WebGL2 that draws the 524,441 land cells in a year's colours.
 *
 * Two passes. The id pass (prerender, only when the camera moves) draws every cell as a small disc around its centre
 * into an offscreen integer texture, with the depth test keeping the nearest centre: each pixel ends up holding the id
 * of the cell it falls in (the cells are the Voronoi regions of their centres, which is what H3 hexagons are, to well
 * under a pixel). The colour pass (render) is one full-screen triangle: each pixel looks its cell up in a texture of
 * every cell's owner, status and second party, colours it from the state palette, adds the hatches and dots the plan
 * asks for, and draws a border wherever the pixel beside it belongs to another state. Moving the year therefore only
 * re-uploads that 4 MB state texture (one texSubImage2D), whatever the zoom; nothing is tessellated or rebuilt.
 *
 * The layer sits under the basemap's water, so lakes and coasts stay crisp, and uses MapLibre's own depth range for
 * its place in the style, so water drawn above it hides the discs' spill into the sea.
 */

const NONE = 0xffffffff;
const TEX_W = 1024;
/** disc radius at the equator, in Mercator units: 1.45 × the mean edge (= circumradius) of an H3 res-5 hexagon */
const DISC_R = 1.45 * 9.85 / 40075.017;

const ID_VS = `#version 300 es
precision highp float;
uniform mat4 u_matrix;
uniform float u_wrap;
uniform float u_r;
in vec2 a_centre;
out vec2 v_local;
flat out uint v_id;
const vec2 C[4] = vec2[4](vec2(-1.0, -1.0), vec2(1.0, -1.0), vec2(-1.0, 1.0), vec2(1.0, 1.0));
void main() {
  vec2 c = C[gl_VertexID];
  float sec = cosh(3.14159265 * (1.0 - 2.0 * a_centre.y));
  gl_Position = u_matrix * vec4(a_centre + c * (u_r * sec) + vec2(u_wrap, 0.0), 0.0, 1.0);
  v_local = c;
  v_id = uint(gl_InstanceID);
}`;
const ID_FS = `#version 300 es
precision highp float;
in vec2 v_local;
flat in uint v_id;
out uvec4 o_id;
void main() {
  float d = dot(v_local, v_local);
  if (d > 1.0) discard;
  gl_FragDepth = d;
  o_id = uvec4(v_id, 0u, 0u, 0u);
}`;

const FULL_VS = `#version 300 es
const vec2 P[3] = vec2[3](vec2(-1.0, -1.0), vec2(3.0, -1.0), vec2(-1.0, 3.0));
void main() { gl_Position = vec4(P[gl_VertexID], 0.0, 1.0); }`;

const COLOR_FS = `#version 300 es
precision highp float;
precision highp int;
precision highp usampler2D;
uniform usampler2D u_ids;
uniform usampler2D u_state;
uniform sampler2D u_pal;
uniform int u_palRows;
uniform vec3 u_neutral;
uniform float u_dpr;
uniform float u_alpha;
uniform uint u_sel;
uniform uint u_hover;
out vec4 o;

const uint NONE = 0xffffffffu;
const uvec4 WATER = uvec4(65535u, 0u, 0u, 0u);
const vec3 INK = vec3(0.169, 0.114, 0.090);
const vec3 NEW = vec3(0.886, 0.337, 0.059);

uvec4 cellState(uint id) { return texelFetch(u_state, ivec2(int(id & 1023u), int(id >> 10u)), 0); }
uvec4 at(ivec2 p) { uint id = texelFetch(u_ids, p, 0).r; return id == NONE ? WATER : cellState(id); }
vec4 pal(uint i, int k) { int n = int(i); return texelFetch(u_pal, ivec2(n & 255, (n >> 8) + k * u_palRows), 0); }
uint realm(uvec4 s) { return (s.g & 7u) == 2u ? s.b : s.r; }

float toLin(float c) { return c <= 0.04045 ? c / 12.92 : pow((c + 0.055) / 1.055, 2.4); }
float toGam(float c) { return c <= 0.0031308 ? 12.92 * c : 1.055 * pow(c, 1.0 / 2.4) - 0.055; }
vec3 oklab(vec3 c) {
  vec3 r = vec3(toLin(c.r), toLin(c.g), toLin(c.b));
  vec3 lms = vec3(0.4122214708 * r.r + 0.5363325363 * r.g + 0.0514459929 * r.b,
                  0.2119034982 * r.r + 0.6806995451 * r.g + 0.1073969566 * r.b,
                  0.0883024619 * r.r + 0.2817188376 * r.g + 0.6299787005 * r.b);
  lms = pow(max(lms, vec3(0.0)), vec3(1.0 / 3.0));
  return vec3(0.2104542553 * lms.x + 0.7936177850 * lms.y - 0.0040720468 * lms.z,
              1.9779984951 * lms.x - 2.4285922050 * lms.y + 0.4505937099 * lms.z,
              0.0259040371 * lms.x + 0.7827717662 * lms.y - 0.8086757660 * lms.z);
}
vec3 srgb(vec3 L) {
  float l = L.x + 0.3963377774 * L.y + 0.2158037573 * L.z;
  float m = L.x - 0.1055613458 * L.y - 0.0638541728 * L.z;
  float s = L.x - 0.0894841775 * L.y - 1.2914855480 * L.z;
  l = l * l * l; m = m * m * m; s = s * s * s;
  vec3 r = vec3(4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
                -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
                -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s);
  r = clamp(r, 0.0, 1.0);
  return vec3(toGam(r.r), toGam(r.g), toGam(r.b));
}
/** coverage of a family of lines across the screen: spacing and width in css px, direction +1 (45°) or -1 (-45°) */
float hatch(vec2 p, float dir, float spacing, float width) {
  float u = (p.x + dir * p.y) * 0.70710678;
  float d = abs(fract(u / spacing + 0.5) - 0.5) * spacing;
  return clamp(width * 0.5 - d + 0.5, 0.0, 1.0);
}

void main() {
  ivec2 px = ivec2(gl_FragCoord.xy);
  uint id = texelFetch(u_ids, px, 0).r;
  if (id == NONE) discard;
  uvec4 s = cellState(id);
  uint owner = s.r, st = s.g & 7u, oth = s.b;
  vec2 css = gl_FragCoord.xy / u_dpr;

  vec3 fill;
  vec3 pc = vec3(0.0);
  float pa = 0.0;
  if (owner == 0u) {
    fill = u_neutral;
    if (st == 3u && oth != 0u) { pc = pal(oth, 0).rgb; pa = hatch(css, 1.0, 7.0, 2.5); }
  } else {
    vec4 full = pal(owner, 0);
    int type = int(full.a * 255.0 + 0.5);
    if (st == 1u) {
      fill = pal(oth != 0u ? oth : owner, 2).rgb;
    } else if (st == 3u) {
      fill = pal(owner, 1).rgb;
      pc = pal(oth, 0).rgb; pa = hatch(css, 1.0, 7.0, 2.5);
    } else if (st == 4u) {
      vec3 lab = mix(oklab(full.rgb), oklab(oth != 0u ? pal(oth, 0).rgb : full.rgb), 0.5);
      fill = srgb(lab);
      pc = srgb(lab - vec3(0.18, 0.0, 0.0)); pa = hatch(css, -1.0, 4.0, 1.0) * 0.8;
    } else {
      fill = pal(owner, 1).rgb;
      if (type == 1) {           // culture: a pastel with a dotted fill
        vec2 g = mod(css, 5.0) - 2.5;
        pc = full.rgb; pa = clamp(1.6 - length(g), 0.0, 1.0) * 0.85;
      } else if (type == 2) {    // rebel: hatched in its own colour
        pc = full.rgb; pa = hatch(css, 1.0, 5.0, 1.5);
      }
    }
  }
  vec3 col = mix(fill, pc, pa);
  if (owner != 0u && owner == u_hover) col = mix(col, vec3(1.0), 0.18);

  // borders: compare with the pixels beside this one
  uint r0 = realm(s);
  int ds = max(1, int(u_dpr + 0.5));             // a state's border: this many device px on each side
  int dt = int(u_dpr * 0.5 + 0.5);               // a member's or a status zone's: 0 means one px, on one side only
  float strong = 0.0, thin = 0.0, gainEdge = 0.0, selEdge = 0.0;
  bool gained = (s.g & 8u) != 0u;
  const ivec2 DIRS[4] = ivec2[4](ivec2(1, 0), ivec2(-1, 0), ivec2(0, 1), ivec2(0, -1));
  for (int k = 0; k < 4; k++) {
    for (int j = 1; j <= 2; j++) {
      if (j > ds) break;
      uvec4 n = at(px + DIRS[k] * j);
      if (n.r == 65535u) continue;
      if (realm(n) != r0) strong = 1.0;
      else if (n.r != owner || n.g != s.g || n.b != oth) {
        if (dt == 0 ? (j == 1 && (owner > n.r || (owner == n.r && (s.g > n.g || (s.g == n.g && oth > n.b))))) : j <= dt) thin = 1.0;
      }
      if (gained && ((n.g & 8u) == 0u || n.r != owner)) gainEdge = 1.0;
    }
  }
  if (u_sel != 0u && (owner == u_sel || r0 == u_sel)) {
    int dsel = max(2, int(2.0 * u_dpr + 0.5));
    for (int k = 0; k < 4; k++) {
      for (int j = 1; j <= 6; j++) {
        if (j > dsel) break;
        uvec4 n = at(px + DIRS[k] * j);
        if (n.r != u_sel && realm(n) != u_sel) selEdge = 1.0;
      }
    }
  }
  col = mix(col, INK, max(strong * 0.5, thin * 0.26));
  col = mix(col, NEW, gainEdge * 0.95);
  col = mix(col, INK, selEdge * 0.92);
  o = vec4(col * u_alpha, u_alpha);
}`;

function compile(gl: WebGL2RenderingContext, vs: string, fs: string): WebGLProgram {
  const sh = (type: number, src: string) => {
    const s = gl.createShader(type)!;
    gl.shaderSource(s, src); gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error("history shader: " + gl.getShaderInfoLog(s));
    return s;
  };
  const p = gl.createProgram()!;
  gl.attachShader(p, sh(gl.VERTEX_SHADER, vs)); gl.attachShader(p, sh(gl.FRAGMENT_SHADER, fs));
  gl.linkProgram(p);
  if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error("history program: " + gl.getProgramInfoLog(p));
  return p;
}

export interface LayerStats { lastUploadMs: number; lastIdPassMs: number; idPasses: number; uploads: number }

export class HistoryLayer implements CustomLayerInterface {
  id = "history-cells";
  type = "custom" as const;
  renderingMode = "2d" as const;
  stats: LayerStats = { lastUploadMs: 0, lastIdPassMs: 0, idPasses: 0, uploads: 0 };

  private map: MLMap | null = null;
  private gl: WebGL2RenderingContext | null = null;
  private idProg: WebGLProgram | null = null;
  private colProg: WebGLProgram | null = null;
  private vao: WebGLVertexArrayObject | null = null;
  private emptyVao: WebGLVertexArrayObject | null = null;
  private centres: WebGLBuffer | null = null;
  private fb: WebGLFramebuffer | null = null;
  private idTex: WebGLTexture | null = null;
  private depth: WebGLRenderbuffer | null = null;
  private stateTex: WebGLTexture | null = null;
  private palTex: WebGLTexture | null = null;
  private fbSize: [number, number] = [0, 0];
  private lastMatrix = new Float32Array(16);
  private idDirty = true;
  private uploaded = -1;
  private palDirty = false;
  private palRows = 1;
  private stateBuf: Uint16Array;
  private pal: Uint8Array | null = null;
  private uni: Record<string, WebGLUniformLocation | null> = {};
  private N: number;
  sel = 0;
  hover = 0;
  alpha = 1;
  neutral: [number, number, number] = [0.839, 0.816, 0.788];

  constructor(private geo: Geo, private tl: Timeline) {
    this.N = geo.N;
    this.stateBuf = new Uint16Array(TEX_W * Math.ceil(this.N / TEX_W) * 4);
  }

  /** The state palette: per state its colour (alpha: 1 culture, 2 rebel), its fill, its vassals' tint and its ink. */
  setStates(st: HistStates) {
    const n = st.count + 1;
    this.palRows = Math.ceil(n / 256);
    const pal = new Uint8Array(256 * this.palRows * 4 * 4);
    const put = (i: number, k: number, hex: string, a = 255) => {
      const [r, g, b] = hexToRgb(hex);
      const o = (((i >> 8) + k * this.palRows) * 256 + (i & 255)) * 4;
      pal[o] = Math.round(r * 255); pal[o + 1] = Math.round(g * 255); pal[o + 2] = Math.round(b * 255); pal[o + 3] = a;
    };
    for (let k = 0; k < st.count; k++) {
      const i = k + 1, hex = st.colour[k], t = st.type[k];
      const culture = t === "c", rebel = t === "r";
      put(i, 0, hex, culture ? 1 : rebel ? 2 : 0);
      put(i, 1, culture ? cultureTint(hex) : rebel ? vassalTint(hex) : hex);
      put(i, 2, vassalTint(hex));
      put(i, 3, labelInk(hex));
    }
    this.neutral = hexToRgb(st.neutral);
    this.pal = pal; this.palDirty = true;
    this.map?.triggerRepaint();
  }

  /** Call when the timeline has moved: the state texture is re-uploaded on the next frame. */
  refresh() { this.map?.triggerRepaint(); }

  onAdd(map: MLMap, gl: WebGL2RenderingContext) {
    this.map = map; this.gl = gl;
    this.idProg = compile(gl, ID_VS, ID_FS);
    this.colProg = compile(gl, FULL_VS, COLOR_FS);
    for (const n of ["u_matrix", "u_wrap", "u_r"]) this.uni["id." + n] = gl.getUniformLocation(this.idProg, n);
    for (const n of ["u_ids", "u_state", "u_pal", "u_palRows", "u_neutral", "u_dpr", "u_alpha", "u_sel", "u_hover"]) this.uni[n] = gl.getUniformLocation(this.colProg, n);

    const xy = new Float32Array(this.N * 2);
    for (let i = 0; i < this.N; i++) { xy[2 * i] = this.geo.x[i]; xy[2 * i + 1] = this.geo.y[i]; }
    this.vao = gl.createVertexArray();
    gl.bindVertexArray(this.vao);
    this.centres = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, this.centres);
    gl.bufferData(gl.ARRAY_BUFFER, xy, gl.STATIC_DRAW);
    const loc = gl.getAttribLocation(this.idProg, "a_centre");
    gl.enableVertexAttribArray(loc);
    gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
    gl.vertexAttribDivisor(loc, 1);
    gl.bindVertexArray(null);
    gl.bindBuffer(gl.ARRAY_BUFFER, null);
    this.emptyVao = gl.createVertexArray();

    this.stateTex = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, this.stateTex);
    gl.texStorage2D(gl.TEXTURE_2D, 1, gl.RGBA16UI, TEX_W, this.stateBuf.length / 4 / TEX_W);
    this.nearest(gl);
    this.palTex = gl.createTexture();
    this.fb = gl.createFramebuffer();
    gl.bindTexture(gl.TEXTURE_2D, null);
  }

  onRemove(_map: MLMap, gl: WebGL2RenderingContext) {
    gl.deleteProgram(this.idProg); gl.deleteProgram(this.colProg);
    gl.deleteVertexArray(this.vao); gl.deleteVertexArray(this.emptyVao); gl.deleteBuffer(this.centres);
    gl.deleteTexture(this.idTex); gl.deleteTexture(this.stateTex); gl.deleteTexture(this.palTex);
    gl.deleteRenderbuffer(this.depth); gl.deleteFramebuffer(this.fb);
    this.map = null; this.gl = null;
  }

  private nearest(gl: WebGL2RenderingContext) {
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
  }

  private ensureTarget(gl: WebGL2RenderingContext) {
    const w = gl.drawingBufferWidth, h = gl.drawingBufferHeight;
    if (this.fbSize[0] === w && this.fbSize[1] === h && this.idTex) return;
    if (this.idTex) gl.deleteTexture(this.idTex);
    if (this.depth) gl.deleteRenderbuffer(this.depth);
    this.idTex = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, this.idTex);
    gl.texStorage2D(gl.TEXTURE_2D, 1, gl.R32UI, w, h);
    this.nearest(gl);
    this.depth = gl.createRenderbuffer();
    gl.bindRenderbuffer(gl.RENDERBUFFER, this.depth);
    gl.renderbufferStorage(gl.RENDERBUFFER, gl.DEPTH_COMPONENT24, w, h);
    gl.bindRenderbuffer(gl.RENDERBUFFER, null);
    gl.bindFramebuffer(gl.FRAMEBUFFER, this.fb);
    gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, this.idTex, 0);
    gl.framebufferRenderbuffer(gl.FRAMEBUFFER, gl.DEPTH_ATTACHMENT, gl.RENDERBUFFER, this.depth);
    this.fbSize = [w, h];
    this.idDirty = true;
  }

  private upload(gl: WebGL2RenderingContext) {
    gl.pixelStorei(gl.UNPACK_ALIGNMENT, 4);
    gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, false);
    gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, false);
    if (this.palDirty && this.pal) {
      gl.bindTexture(gl.TEXTURE_2D, this.palTex);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA8, 256, this.palRows * 4, 0, gl.RGBA, gl.UNSIGNED_BYTE, this.pal);
      this.nearest(gl);
      this.palDirty = false;
    }
    if (this.uploaded !== this.tl.version) {
      const t0 = performance.now();
      const b = this.stateBuf, { owner, status, other, gained } = this.tl;
      for (let i = 0, o = 0; i < this.N; i++, o += 4) {
        b[o] = owner[i]; b[o + 1] = status[i] | (gained[i] << 3); b[o + 2] = other[i];
      }
      gl.bindTexture(gl.TEXTURE_2D, this.stateTex);
      gl.texSubImage2D(gl.TEXTURE_2D, 0, 0, 0, TEX_W, b.length / 4 / TEX_W, gl.RGBA_INTEGER, gl.UNSIGNED_SHORT, b);
      this.uploaded = this.tl.version;
      this.stats.lastUploadMs = performance.now() - t0;
      this.stats.uploads++;
    }
    gl.bindTexture(gl.TEXTURE_2D, null);
  }

  prerender(gl: WebGL2RenderingContext, args: CustomRenderMethodInput) {
    if (!this.map || !this.pal) return;
    const prevFb = gl.getParameter(gl.FRAMEBUFFER_BINDING) as WebGLFramebuffer | null;
    this.upload(gl);
    this.ensureTarget(gl);
    const m = Float32Array.from(args.defaultProjectionData.mainMatrix as unknown as ArrayLike<number>);
    let same = !this.idDirty;
    if (same) for (let i = 0; i < 16; i++) if (m[i] !== this.lastMatrix[i]) { same = false; break; }
    if (!same) {
      const t0 = performance.now();
      this.lastMatrix.set(m);
      gl.bindFramebuffer(gl.FRAMEBUFFER, this.fb);
      gl.viewport(0, 0, this.fbSize[0], this.fbSize[1]);
      gl.disable(gl.BLEND); gl.disable(gl.STENCIL_TEST); gl.disable(gl.SCISSOR_TEST); gl.disable(gl.CULL_FACE);
      gl.enable(gl.DEPTH_TEST); gl.depthFunc(gl.LESS); gl.depthMask(true); gl.depthRange(0, 1);
      gl.colorMask(true, true, true, true);
      gl.clearBufferuiv(gl.COLOR, 0, new Uint32Array([NONE, 0, 0, 0]));
      gl.clearBufferfv(gl.DEPTH, 0, new Float32Array([1]));
      gl.useProgram(this.idProg);
      gl.uniformMatrix4fv(this.uni["id.u_matrix"], false, m);
      gl.uniform1f(this.uni["id.u_r"], DISC_R);
      gl.bindVertexArray(this.vao);
      const b = this.map.getBounds();
      const w0 = Math.floor((b.getWest() + 180) / 360), w1 = Math.floor((b.getEast() + 180) / 360);
      for (let w = Math.max(w0, -3); w <= Math.min(w1, 3); w++) {
        gl.uniform1f(this.uni["id.u_wrap"], w);
        gl.drawArraysInstanced(gl.TRIANGLE_STRIP, 0, 4, this.N);
      }
      gl.bindVertexArray(null);
      gl.bindFramebuffer(gl.FRAMEBUFFER, prevFb);
      this.idDirty = false;
      this.stats.lastIdPassMs = performance.now() - t0;
      this.stats.idPasses++;
    }
  }

  render(gl: WebGL2RenderingContext) {
    if (!this.map || !this.pal || !this.idTex) return;
    gl.useProgram(this.colProg);
    gl.bindVertexArray(this.emptyVao);
    gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, this.idTex);
    gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, this.stateTex);
    gl.activeTexture(gl.TEXTURE2); gl.bindTexture(gl.TEXTURE_2D, this.palTex);
    gl.uniform1i(this.uni.u_ids, 0); gl.uniform1i(this.uni.u_state, 1); gl.uniform1i(this.uni.u_pal, 2);
    gl.uniform1i(this.uni.u_palRows, this.palRows);
    gl.uniform3f(this.uni.u_neutral, ...this.neutral);
    gl.uniform1f(this.uni.u_dpr, this.fbSize[0] / Math.max(1, this.map.getCanvas().clientWidth));
    gl.uniform1f(this.uni.u_alpha, this.alpha);
    gl.uniform1ui(this.uni.u_sel, this.sel);
    gl.uniform1ui(this.uni.u_hover, this.hover);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
    gl.bindVertexArray(null);
    for (const u of [gl.TEXTURE2, gl.TEXTURE1, gl.TEXTURE0]) { gl.activeTexture(u); gl.bindTexture(gl.TEXTURE_2D, null); }
  }
}

export { DISC_R };
