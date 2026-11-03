# Review of batch eu-13-g (2026-10-31): republic-of-genoa

Verdict: **fail** (one unapplied blocking finding: Chios). One fix applied by the reviewer. Machine copy: history/notes/phase-b/reviews/eu-13-g.json.

## What I tried and could not break
- Validator `--resolve`: 0 errors, 0 warnings, 283 regions (before and after my edit).
- Years: ledger sorted, found 1099, dissolve June 1797, wars and capitals inside the life; contests paired (1282-1284, 1729-1755, 1746-1748).
- Spot checks (pages opened by me): History of Corsica (1284, 1553 August, 1559, 1729, 1755, 1768), Republic of Genoa (1394-1409, 1458, 1461, 1464, 1463-1478 / 1488-1499, 1499-1528, Tabarka 1540-1742, 1580 name, September 1746, Aix-la-Chapelle, 14 June 1797, Chios and Samos 1275, Tana 1316), Gazaria (1266, 1308, 1313), Kingdom of Cyprus (infobox tributary 1372-1426), Chios (1329, 12 September 1346, April 1566). Every confidence-3 event checked is on its page with its year. No fabrication found.
- Not on the Gazaria page: 1305 Taman and 1375 Gothia (both confidence 1, so gaps). The Gazaria text gives 1474 for the Ottoman conquest (infobox 1471-1475); 1475 at confidence 2 is acceptable.
- Area: the Republic of Genoa infobox has no area; keyframe_review/0 says so. Cliopatria maximum 28,150 km2.
- Cliopatria row problems (pre-1099 shapes, Lesbos/Lemnos, Rhodes, Black Sea to 1525, Corsica to 1793, missing core 1402-1414, 1422-1439, 1540-1563, row ending 1795) are all flagged in keyframe corrections and notes.

## Applied by the reviewer
- /ledger/4 (1266 Caffa): counterpart golden-horde -> ulus-of-jochi. The golden-horde dossier starts in 1294; ulus-of-jochi (1225-1293) is the Jochid state of 1266. Note appended; re-validated clean.

## Blocking, back to the author
- **Chios is double-drawn.** /ledger/5, /13, /14, /40 and the corrections of keyframes 1272-1564 make Chios Genoa's own land 1275-1329 and 1346-1566. Two existing dossiers hold it: `lordship-of-chios` (state, 1304-1329; Chios page: 'the Genovese Benedetto I Zaccaria (1304)') and `maona-of-chios` (colony, 12 September 1346 to April 1566, drawn in Genoa's tint). The Byzantine dossier's 1329 gain is from the Zaccaria lordship, not Genoa. Fix: end Genoa's own Chios in 1304 (loss to lordship-of-chios) or justify keeping the 1275-1304 grant only; delete the 1329 loss; make 1346-09 a vassal_start and 1566-04 a vassal_end with counterpart maona-of-chios; take Chios out of the corrections for 1304-1329 and 1346-1566; add maona-of-chios to wars 3 and 9; remove the Maona and Gattilusio entries from counterparts_needing_dossiers (slugs `maona-of-chios` and `gattilusi` exist).

## Missing mirrors (author or gap-filler)
Neighbours carry events naming republic-of-genoa that this ledger lacks:
- Rhodes 1248-1250 (domain-of-rhodes occupation, nicaean-empire contest, confidence 3). Flagged by the author; the 1250 keyframe correction removes Rhodes, so add occupation_start 1248 / occupation_end 1250.
- Crete 1206-1217 (kingdom-of-candia; republic-of-venice 1207-1212): Pescatore's war. Not flagged.
- Trebizond: contest 1306-1314, Kerasus 1347-1349, Leonkastron 1349 (empire-of-trebizond). Partly flagged.
- Tripoli 1354-1355 (banu-thabit loss, banu-makki gain). Not flagged.
- Livorno: Genoa's 1407 purchase and the sale to Florence on 28 August 1421 (republic-of-florence, confidence 3). Not flagged.
- Gothia 1423 and Cembalo February 1433 to June 1434 (principality-of-theodoro, confidence 3). Not flagged.
- Monaco 1297-1419, nine events (principality-of-monaco). Flagged; sub-cell.
- Elba 1548 (republic-of-florence says bought 'from the Republic of Genoa'; probably Piombino's: one side is wrong). Not flagged.
- Capraia 1767-1768 (corsican-republic). Sub-cell.

## Confidence-1 gaps (thin)
1202 Bonifacio, 1305 Taman, 1352 Samos (the Republic page has Samos granted with Chios in 1275; lordship-of-chios has it 1325-1329), 1375 Gothia, 1421 Milan (try the Wars in Lombardy page, which the Milan dossier cites), 1422/1450 Aragon in Corsica (History of Corsica says only 'take-overs by Aragon between 1296 and 1434'), 1464 Famagusta. identity.rulers omitted (List of doges).

## Cross-dossier mismatches for other groups
- holy-roman-empire (eu-08): 1010 loss to Genoa vs Genoa's 1099 found / 1200 gain.
- duchy-of-milan (eu-13): 1441 loss vs Genoa 27 December 1435; no 1499 loss of Genoa.
- golden-horde / ulus-of-jochi (ia-02): no losses for Caffa 1266/1313, Tana 1316, Taman 1305, Gothia 1375; 1308 only a contest_end.
- byzantine-empire (eu-05): no 1275 loss; 1329 gain is from the Zaccaria lordship; no 1346 or 1352 loss.
- kingdom-of-cyprus: no vassal_start/end with Genoa 1372-1426.
- kingdom-of-france (eu-10): no occupations of Genoa 1394-1409, 1458-1461, 1499-1528; no 1768 gain from Genoa (its 1769 gain is from corsican-republic).
- ottoman-empire (me-10): no 1566 gain of Chios (maona-of-chios carries the loss).
- habsburg-monarchy (eu-09): no 1746-1748 contest.
- hafsid-dynasty, beylik-of-tunis: no Tabarka 1540 / 1742.
- kingdom-of-sardinia (eu-13): 1814 gain from republic-of-genoa, which ended in 1797; needs the restored Genoese republic of 1814-1815 or another counterpart.
