// Packs public/data/*.json into a brotli container split into data/data.br.partNN (≤18 KB each),
// so the dataset ships inside the repo in small pieces and needs nothing but Node to unpack.
import { readFileSync, writeFileSync, mkdirSync, readdirSync, unlinkSync } from "node:fs";
import { brotliCompressSync, constants } from "node:zlib";
import { LABELS } from "./country-labels.mjs";
const FILES = ["towers.json", "details.json"];
mkdirSync("data", { recursive: true });
for (const f of readdirSync("data")) if (/^data\.(br|tgz)/.test(f)) unlinkSync(`data/${f}`);
// public/data may already carry the display labels from prebuild (scripts/country-labels.json): pack the dataset's own names.
const raw0 = (f) => { let t = readFileSync(`public/data/${f}`, "utf8"); for (const [a, b] of Object.entries(LABELS)) t = t.replaceAll(JSON.stringify(b), JSON.stringify(a)); return Buffer.from(t); };
const parts = FILES.map(f => ({ name: f, buf: raw0(f) }));
const header = Buffer.from(JSON.stringify(parts.map(p => [p.name, p.buf.length])));
const hlen = Buffer.alloc(4); hlen.writeUInt32BE(header.length);
const raw = Buffer.concat([hlen, header, ...parts.map(p => p.buf)]);
const br = brotliCompressSync(raw, { params: { [constants.BROTLI_PARAM_QUALITY]: 11, [constants.BROTLI_PARAM_SIZE_HINT]: raw.length } });
const SIZE = 18 * 1024; let n = 0;
for (let off = 0; off < br.length; off += SIZE, n++) writeFileSync(`data/data.br.part${String(n).padStart(2, "0")}`, br.subarray(off, off + SIZE));
console.log(`packed ${raw.length} → ${br.length} bytes into ${n} parts`);
