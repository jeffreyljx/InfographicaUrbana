// Deploy bootstrap: the source tree ships as bundle/src.tar.br.partNN (brotli tar, split to
// stay under the upload limit). Reassemble + extract it, then run the normal prebuild.
// Files under overlay/ (sent as plain files with a deployment) are then copied over the tree, last of all, so a
// small change can be deployed without rebuilding the bundle. Idempotent: safe to run on install and again on build.
import { readdirSync, readFileSync, writeFileSync, existsSync, rmSync, cpSync } from "node:fs";
import { brotliDecompressSync } from "node:zlib";
import { execSync } from "node:child_process";

// bundle/overlay.tar.br.partNN, bundle/delta.tar.br.partNN and bundle/delta2.tar.br.partNN, if present, are further
// brotli tars unpacked over the tree in that order (earlier fixes, then the latest changes), so a change can ship as a
// small upload without rebuilding the whole bundle.
function unpack(name, what) {
  const parts = readdirSync("bundle").filter(f => f.startsWith(`${name}.tar.br.part`)).sort();
  if (!parts.length) return;
  const tar = brotliDecompressSync(Buffer.concat(parts.map(f => readFileSync(`bundle/${f}`))));
  writeFileSync(`${name}.tar`, tar);
  execSync(`tar xf ${name}.tar`, { stdio: "inherit" });
  rmSync(`${name}.tar`);
  console.log(`bootstrap: unpacked ${what} (${tar.length} bytes) from ${parts.length} parts`);
}
if (existsSync("bundle")) {
  unpack("src", "source tree");
  unpack("overlay", "earlier fixes");
  unpack("delta", "changes since the bundle");
  unpack("delta2", "changes since the delta");
}
// plain overlay/ files go last, so a small change can ship on top of the tars above
if (existsSync("overlay")) {
  cpSync("overlay", ".", { recursive: true, force: true });
  console.log("bootstrap: applied overlay/");
}
execSync("node scripts/prebuild.mjs", { stdio: "inherit" });
