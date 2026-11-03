# Review of batch me-09-i (2026-10-25)

One dossier: `tahirid-sultanate` (Tahirid Sultanate of Yemen, 1454-1517; Cliopatria 1459-1515, 2 shapes, page budget 1-2). Verdict: **thin** (valid and honest; three small fixes applied by the reviewer; four gaps and one cross-dossier mismatch for a gap-filler and the orchestrator).

## Mechanical
- Validator `--resolve`: 0 errors, 1 warning (`/ledger/5/counterpart` `kathiri-sultanate` has no dossier; listed in the author's counterparts_needing_dossiers). Re-validated after the reviewer's edits: 0 errors, same warning.
- File name = slug; `cliopatria_names` matches polities.csv; both Cliopatria shapes (`_1459`, `_1512`) reviewed (adjust); new keyframes carry from/to/correction. Ledger in order; found 1454 = start; dissolve 1517 = end; contests paired. Capital Zabid (43.32 E, 14.20 N) is inside the corrected shape and the Cliopatria bbox. Family `caliphate` matches the Rasulid predecessor; type `dynasty` is allowed.

## Spot checks (https://en.wikipedia.org/wiki/Tahirid_Sultanate, opened twice by the reviewer)
- /ledger/1 1454 Aden (c3): confirmed, 'in 1454, the important port of Aden was swiftly taken by the brothers Amir and Ali bin Tahir'.
- /ledger/2 1457 Shihr (c3): confirmed, 'Shihr in Hadramawt was taken in 1457'.
- /ledger/6 1504 Sana'a (c3): confirmed, 'managed to take San'a again in 1504'.
- /ledger/9 1517 dissolve (c2): year confirmed (infobox 'Disestablished: 1517'; '15 May' has no year on the page but 'The Mamluk regime in Egypt was overrun by the Ottomans in the same year' puts it in 1517). Region was wrong (see fix 1).
- /ledger/3 1461 (c2): confirmed; the preceding sentence makes 'the latter' al-Mujahid Ali (see fix 2).
- Ruler list (1454-1460, 1460-1479, 1479-1489, 1489-1517; then to 1538) confirmed on the page.

## Fixes applied by the reviewer
1. /ledger/9/region: removed `{"admin1": "`Adan"}` from the dissolve region and said so in its text and note. The page: 'The entire Tahirid realm fell under the Mamluks with the exception of Aden which held out under the Tahirid governor Amir Murjan'. The region now agrees with the note, with /ledger/8 and with identity.successors[0].land.
2. /ledger/3/note: 'the latter' is al-Mujahid Ali ('The debacle probably inspired az-Zafir Amir to abdicate his royal prerogatives to another brother, al-Mujahid Ali. The latter was able to enter San'a temporarily in 1461'); the ambiguity remark replaced.
3. /identity/rulers/1-3: added the source URL (the page's ruler list), which only the first ruler carried.

## Gaps (thin; for a gap-filler)
- Aden remnant 1517-1538 (/identity/end, /ledger/9): the cited page names the Tahirid rulers of Aden to Amir bin Da'ud, says the Zabid Mamluks fought 'remaining Tahirid forces', and that Sulaiman Pasha hanged Amir bin Da'ud at Aden 'on 3 August 1538'. Suggested: end 1538-08; turn /ledger/9 into a 1517-05 `loss` of the realm without Aden; new keyframe `tahirid-sultanate_1518` = `{"place": "Aden", "km": 25}` 1518-1538; capital Aden from 1517; rulers to 1538; dissolve 1538-08 Aden to `ottoman-empire`. Until then Aden is ownerless on the map from 1517 (better than the Mamluk colour the page denies).
- /ledger/4 1466 contest_end (c1): no end to the Sana'a contest; who held Sana'a 1466-1504.
- /ledger/5 1499 Shihr loss (c1): year bridged from 'the end of the fifteenth century'.
- /ledger/7 1515 contest_start (c1): no landing date and no date for the fall of Zabid; Selman Reis's article (opened by the reviewer) gives only 'failed to take Yemen and Aden on 17 September 1516'.

## Cross-dossier
- **Mamluk mismatch (route to me-09-d / orchestrator).** mamluk-sultanate /ledger/40 gains Yemen in 1516 (c1) with region `{"cliopatria": "Tahirid Sultanate", "year": 1515}` (1,633 cells, Aden, Hadramawt, al-Mahrah and Najran included, though its own text says 'without Aden'); mamluk-sultanate ends 1517-01 (dissolve to ottoman-empire). This dossier hands the realm to mamluk-sultanate in 1517-05, four months after that state's end. The page: 'The Zabid Mamluks then offered prayers in the name of the Ottoman sultan'. Resolution needs one of: (a) a page dating the Mamluk capture of Zabid and the Tihama (likely 1516): Tahirid `loss` of the Tihama to mamluk-sultanate that year, and the highlands and Sana'a in 1517-05 to `ottoman-empire` (the Zabid Mamluks' overlord); or (b) the orchestrator accepts the four-month overlap and mamluk-sultanate passes its Yemen land to ottoman-empire in 1517-01. Either way mamluk-sultanate /ledger/40 should draw the corrected Tahirid realm (this dossier's /ledger/9 region), not the Cliopatria 1515 shape.
- **Rasulid land mismatch.** rasulid-dynasty /ledger/6 dissolves in 1454 handing `{"cliopatria": "Rasulid Dynasty", "year": 1453}` (377,950 km2) to tahirid-sultanate; this dossier takes about 105,000-113,000 km2 (455-489 cells). Sa'dah, al-Jawf, Ma'rib, Shabwah, the Hadramawt interior, al-Mahrah and Najran have no receiver. The Tahirid page supports the smaller realm ('they ruled in the first place in the Tihama lowland and the southern highlands'; the Zaydi imams 'were mostly able to resist Tahirid rule'); the Rasulid dossier's loose coast 'up to Dhofar' is a 13th-century statement. Route to the Rasulid author.
- **Lahij 1443.** rasulid-dynasty /ledger/4 loses Lahij to tahirid-sultanate in 1443, eleven years before this state begins; Lahij is ownerless 1443-1453 on the map. The author explained it (pre-state clan holding). Either the Rasulid dossier keeps Lahij to 1454 or records the Tahir clan as its subordinate there.
- adal-sultanate: neighbour across the Bab el-Mandeb in the seed only; no events either way.
- imamate-of-yemen (15th-16th-c. Zaydi imams) and kathiri-sultanate: no dossiers; listed by the author. Note the slug collision: polities.csv `imamate-of-yemen` is the 1814-1872 row; the Rasulid and Tahirid dossiers use it for the medieval imams.

## Area
Infobox has no area. Cliopatria 377,950 km2 (both shapes, identical to the Rasulid rows); corrected shape about 105,000 km2 (1454) and 113,000 km2 (1504-1517), ratio about 0.3, acknowledged and resolved in every keyframe note (adjust).

## Not faults, for the record
- The gazetteer's 'Tihama' includes Jizan (Saudi Arabia, 59 cells) and all of Hajjah governorate; the page says only 'the Tihama lowland'. Defensible at confidence 2 (Tihamat al-Yaman), but a gap-filler may narrow it to Al Hudaydah plus coastal Hajjah.
- /keyframe_review/3 starts in 1500 while the Shihr loss it reflects is dated 1499 (confidence 1, bridged); harmless.
- polities.csv 'wikipedia' for this row points to the Persian Tahirids ('Tahirid dynasty'); the author flagged it.
