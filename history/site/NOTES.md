# CartaHistoria site build: notes

Branch `claude/project-thread-yvewot` of jeffreyljx/SkyscraperMaps (not merged, no PR).

## Packing the data

    python3 -I scripts/history/pack.py /mnt/project-files/history          # writes public/history/
    python3 -I scripts/history/pack.py /mnt/project-files/history --check  # replay and report only
    npm run build                                                           # then commit public/history

- Reads `land_r5.txt` (grid), `colours.json`, `polities/*.json`, `compiled/<window>.json` (or `compiled/_draft/<window>.json` where no final exists; `--drafts` forces drafts) and the anchors.
- Replays each window from its start anchor and checks it ends on its end anchor (`seams` in index.json; all clean on 1 Nov).
- States without a colour in `colours.json` get one from a hash of the slug (OKLCH wheel), flagged `fb` and shown as "provisional colour" (1,484 on 1 Nov).
- Captions: `keyframe` notes and captions that are compilers' workings (cells, rows, Cliopatria, infobox, dossier, page...) are left out of the dock; parentheses citing pages are stripped. 34,360 of 43,244 captions kept. Final windows with clean captions make this filter mostly a no-op.

## Output (1 Nov 2026, drafts)

public/history 24.1 MB: geo.bin 1.27 MB (cell centres), w/ 5.9 MB in 119 chunks (largest 235 KB), states.json 0.89 MB, state/ 16.0 MB (2,995 files), index.json 30 KB. First view loads geo + states + one chunk, about 2.4 MB.

## Rendering

Custom MapLibre WebGL2 layer (src/components/historyLayer.ts): an ID pass, only when the camera moves, draws each cell as a disc round its centre with depth = distance (so the nearest centre wins: a Voronoi that matches the H3 hexes) into an R32UI texture; the colour pass reads each pixel's cell, looks up owner/status/other in a 4 MB per-year texture and paints fill, vassal tint, hatches, culture dots, borders, gains. A year step = apply the deltas (about 1.4 ms) + one texture upload (about 3 ms). The water layer sits above the cells.

## Known gaps

- The basemap (tiles.openfreemap.org) is blocked from the build container, so the screenshots show the fallback: sea background, land = the cells (nobody's land grey), coasts scalloped by the hexes.
- GPU frame time not measured (software GL only here).
