# Review of batch eu-16-g (Vladimir-Suzdal, Tver, Ryazan), 2026-10-31

Reviewer: adversarial review per history/briefs/reviewer-brief.md. Machine copy: history/notes/phase-b/reviews/eu-16-g.json.

Mechanical: all three dossiers validate with --resolve, 0 errors, 0 warnings. Neighbour dossiers read (ledger grep): golden-horde, blue-horde, qasim-khanate, principality-of-smolensk, grand-duchy-of-lithuania, principality-of-rostov-suzdal, principality-of-ryazan. Not written yet: grand-principality-of-moscow, novgorod-republic, nizhny-novgorod, principality-of-beloozero (exceptions). Pages opened: Vladimir-Suzdal, Principality of Tver, Tver, Principality of Moscow, Ivan III of Russia, Principality of Ryazan, Ryazan, Pronsk (set index) and Pronsk, Pronsky District. None failed. No fix applied by the reviewer; no dossier edited.

## principality-of-vladimir-suzdal: fail (back to the author)

1. /ledger/5 (1389 merge, confidence 2): the region is the whole 1375 shape plus the Vladimir disc, so Rostov, Yaroslavl, Uglich, Bezhetsk and the Vologda country pass to Moscow in 1389. The Ivan III page dates them 'Principality of Yaroslavl in 1463, Rostov in 1474' and Uglich/Bezhetsk to Andrey Bolshoy until 'He died in prison in 1493, and Ivan seized his land'. The dossier's own /ledger/6 note and /identity/successors/0 say only the core went to Moscow. Fix: give the merge the successors' land (1375 shape minus 1395 shape, plus Vladimir 70 km), and account for the rest with a 1389 split/loss to the proposed Yaroslavl/Rostov/Uglich slugs (or nobody, with a note).
2. Missing vassal pair: the page says 'Vladimir became a vassal of the Mongol Empire ... with the Grand Prince appointed by the Great Khan' and golden-horde/ledger/2 has vassal_start 1294 for this slug. Add vassal_start 1294 and vassal_end 1389 (counterpart golden-horde).
3. Overlap with tver.json (same author): the 1294-1304 correction shares 28 cells (about 7,081 km2; Klin-Dmitrov edge and Uglich-Kalyazin edge) with the Tver correction, 7 cells (Uglich edge) in 1305-1389. The Tver page lists the 'Principality of Klin' as a Tver appanage, while /ledger/1 gives Klin to Vladimir-Suzdal until 1305. Reconcile and say so in the notes.
4. Non-blocking: the 'wrong' keyframes 1395-1486 repeat the Cliopatria shape as their correction; say the shape belongs to no year of this slug (or give an empty region) so it cannot be drawn after 1389.
Spot checks: 1389 end and 19 May 1389 (footnote) confirmed; 1305 and 1344 quotes on the Moscow page confirmed (years honestly Cliopatria's at confidence 1); Ivan III page dates for Yaroslavl/Rostov confirmed. Area: infobox gives none (confirmed). Thin: dates of Moscow's acquisitions (confidence 1), ruler list.

## tver: thin (gap-filler)

Everything checked holds: 1246 founding, infobox 28,450 km2 and 'from Kashin in the east to Zubtsov in the west', 1368 and 1370 invasions, the 1375 treaty ('elder brother', four-week siege), 12 September 1485. Area factor of four acknowledged in every keyframe note. Kashin and Zubtsov coordinates are right.
- Non-blocking finding: the corrected shape (three discs, about 32,118 km2) overlaps the neighbours' drawn land without a word: in 1294 Smolensk 42 cells (10,622 km2, Zubtsov-Rzhev), Novgorod 27 (6,828 km2, Torzhok), Vladimir-Suzdal 28 (7,081 km2); from 1344 Moscow 53 cells (13,404 km2), Smolensk/Lithuania 32. The page supports the Tver side for Zubtsov and eastern Smolensk Oblast; say so in /keyframe_review/1 note and reconcile the Vladimir-Suzdal overlap.
- Thin: no vassal pair with the Horde (Tver held its throne and the Vladimir patent by yarlyk; 'In 1375, Mamai again granted Mikhail II the yarlik'); golden-horde.json has none either. No ruler list. 1327 contest_end at confidence 1. Torzhok, Rzhev and 1470s treaties undated.
- The 1246 found event names principality-of-vladimir-suzdal, which starts in 1294 (consequence of the two-dossier split; see problems).

## ryazan: fail (back to the author)

1. The 'Pronsk' disc is at 40.85E 53.95N, near Sapozhok, about 80 km east of Pronsk, which the Pronsk, Pronsky District page puts at 54°07'N 39°37'E on the Pronya. A 40 km disc at the true site has 16 of 20 cells inside Cliopatria's 1453 Ryazan shape, so the keyframe note 'Pronsk lies outside it' is false; the author's disc meets the Ryazan shape in 0 cells and Cliopatria's Qasim Khanate in 14 cells (3,541 km2) and the Golden Horde in 5. The error runs through /ledger/1-3, /keyframe_review/1-4 and /identity/successors/0, and the gazetteer hint. Fix: redraw at 39.617E 54.117N and decide whether Pronsk is inside Ryazan's land before 1483 (a 'provincial' appanage: drop the union, keep or drop a small 1483 consolidation event) or subtract it from ryazan_1453 and keep the gain.
Spot checks: 1483 year, 1520/1521 end, dissolve on the Ryazan page and the ruler list confirmed. Area: infobox gives none (confirmed). Thin: tributary status to the Great Horde 1453-1480; golden-horde.json has a 1453 territorial loss to Ryazan instead.

## For the orchestrator

- Two-dossier split of the same states (Q83546, Q269109) against the author brief's one-dossier rule; both sides flagged it. 1241-1293 (Vladimir) and 1241-1452 (Ryazan) belong to no dossier.
- golden-horde (ia-02): vassal_end 1480 for Vladimir-Suzdal should be 1389 (or re-aimed to Moscow); the 1453 loss to Ryazan is a Cliopatria artefact; the Vladimir disc overlaps its shape by 34 cells 1294-1400.
- Uglich runs to 1493 on the Ivan III page, not 1491.
