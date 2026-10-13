// Deploy bootstrap: the source tree ships as bundle/src.tar.br.partNN (brotli tar, split to
// stay under the upload limit). Reassemble + extract it, then run the normal prebuild.
// Files under overlay/ (sent as plain files with a deployment) are then copied over the tree, so a small
// change can be deployed without rebuilding the bundle. Idempotent: safe to run on install and again on build.
import { readdirSync, readFileSync, writeFileSync, existsSync, rmSync, cpSync } from "node:fs";
import { brotliDecompressSync } from "node:zlib";
import { execSync } from "node:child_process";

if (existsSync("bundle")) {
  const parts = readdirSync("bundle").filter(f => /^src\.tar\.br\.part\d+$/.test(f)).sort();
  if (parts.length) {
    const tar = brotliDecompressSync(Buffer.concat(parts.map(f => readFileSync(`bundle/${f}`))));
    writeFileSync("src.tar", tar);
    execSync("tar xf src.tar", { stdio: "inherit" });
    rmSync("src.tar");
    console.log(`bootstrap: unpacked source tree (${tar.length} bytes) from ${parts.length} parts`);
  }
}
if (existsSync("overlay")) {
  cpSync("overlay", ".", { recursive: true, force: true });
  console.log("bootstrap: applied overlay/");
}
execSync("node scripts/prebuild.mjs", { stdio: "inherit" });
