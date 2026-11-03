# Review of batch ia-03-b (shaybanids, khanate-of-bukhara, khanate-of-khiva)

Reviewer, 2026-10-19. The machine copy is history/notes/phase-b/reviews/ia-03-b.json. Validator: all three files pass with --resolve, before and after the reviewer's edits (khiva keeps one warning: khorezm-people-s-soviet-republic has no dossier yet). Under the orchestrator's adjustment I applied small, page-verified fixes in place; each edited note ends "(Reviewer ia-03-b, 2026-10-19: ...)".

Neighbour dossiers read: kazakh-khanate, timurid-empire, moghulistan, eastern-chagatai-khanate, nogai-horde, kapisa. Not yet written (exception): safavid-dynasty, afsharid-iran, qajar-dynasty, zand-dynasty (me-10); mughal-empire (sa-05); russian-empire, russian-republic (eu-17); qing-dynasty (ea-08); emirate-of-bukhara, khanate-of-kokand, durrani-empire, dzungar-khanate and the other ia-03 parts.

## shaybanids: FAIL (one missing event; two fixes applied)

- Applied, /ledger/12: Khwarazm was a 1511 loss to khanate-of-khiva at confidence 3. The Khanate of Khiva page says Shah Ismail and Shaybani "clashed in 1510 near Merv with Muhammad killed in the battle and Khorezm shortly occupied. The Shah's religion provoked resistance and in 1511 his garrison was expelled and power passed to Ilbars": the garrison was the Shah's. It is now a December 1510 loss to safavid-dynasty at confidence 2; the keyframe_review/4 note is reworded to match.
- Applied, /ledger/4: Tashkent was a 1502 gain from moghulistan at confidence 1. moghulistan's own ledger hands Tashkent to eastern-chagatai-khanate in 1492, and the Moghulistan page has Mahmud Khan, "the ruler of western Moghulistan in Tashkent", lose it in 1503 ("Tashkent was seized by the Uzbeks"). It is now 1503, counterpart eastern-chagatai-khanate, confidence 2, source Moghulistan (added to sources[]). wars/0, the predecessors/0 note and the notes field are updated to match.
- NOT applied (blocking): Babur's 1511 capture of Samarkand and Bukhara is missing. Babur page: "in 1511 ... he managed to take Samarkand for the third time; he also took Bukhara but lost both again to the Uzbeks in 1512." timurid-empire /ledger/48 has the 1511 gain from shaybanids with no mirror here, so in 1511 both dossiers draw the two cities. Add a 1511 loss to timurid-empire (union place Samarkand 150 km and Bukhara 150 km, as in the Timurid mirror), confidence 3, source Babur; mention it in keyframe_review/4; correct the dissolve note's "lost to Babur in 1512".
- Thin: found 1497 at confidence 1 (kazakh-khanate /ledger/5 gives these lands to shaybanids in 1496, while the found event names nobody); Fergana 1502 at confidence 1; the steppe handed to the Kazakhs (successors/3) is undated with no ledger loss, while kazakh-khanate /ledger/6 has a 1510 gain (confidence 1); the 1507 southern tongue is unsupported.
- Confirmed on the page: 1500 Samarkand, 1501 Bukhara, 1505 Urgench, 1506 Balkh, 1507 Herat, 1510 Balkh, 2 December 1510 Merv. Area: no infobox area.

## khanate-of-bukhara: FIX (applied by the reviewer)

- Applied, /ledger/28: the 1736 loss to afsharid-iran named {"country": "Afghanistan"}. It is now intersect[Afghanistan, the khanate's 1721 shape]: the same 94 cells south of the Amu Darya that the 1738-1752 corrections remove (Balkh page: "In 1736 it was conquered by Nader Shah").
- Fifteen events confirmed: 1516-17 and c.1521 (Kazakh Khanate); 1538 (Ubaydullah Khan); 1576, 1584, 1588 and 1593-94 (Abdullah Khan II); 1593 and 1600 Merv; 1598 (Kazakh Khanate); 1598, 1601, 1646, 1647 and 1736 Balkh; November 1762 Charjuy.
- Thin / to settle:
  - Tashkent is lost to kazakh-khanate in 1521 (/ledger/6) and regained in 1576 from a "Shaybanid appanage" (/ledger/11). Nothing returns it in between, and the Kazakh dossier never loses it before 1597, so 1576-1597 is drawn twice. Settle the holder for 1521-1576.
  - The Kazakh 1611-1613 contest over Tashkent has no mirror here.
  - The confidence-1 events at /ledger/16, /ledger/23, /ledger/30 and /ledger/32 have no page.
  - The ruler list has gaps: 1512-34, 1539-83 and 1753-58.
- The Nader Shah vassalage belongs in afsharid-iran (the schema puts vassal events in the overlord's ledger). Area: no infobox area.

## khanate-of-khiva: FIX (applied by the reviewer)

- Applied, /ledger/0: the found event's counterpart was shaybanids and its note said "the Shaybanid garrison". The page says the expelled garrison was Shah Ismail's. Counterpart is now safavid-dynasty; the predecessors/0 note is corrected.
- Applied, /ledger/14: the 1813 gain named the whole Qyzylorda province (741 cells). 422 of those cells (about 107,000 km2, to 68.1 E and 47.7 N) lie outside every Khiva shape and are never lost. The page says only "subdued the Kazakh tribes of the lower Syr Darya in 1812-1813". The region is now intersect[Qyzylorda, Khiva 1800], as the author did for the 1811 delta.
- Applied, /wars/2: the 1717 Bekovich expedition named russian-empire (from 1721). It now names tsardom-of-russia (1547-1720).
- Confirmed on the page: 1511 (year), 1740, 1811, 1812-13, 1823, c.1856, 11 March 1873, June 1873, October 1873 (the strip to Bukhara), and 2 February 1920.
- Thin:
  - Confidence 1 at /ledger/1, /ledger/5, /ledger/9-10, /ledger/11 and /ledger/17.
  - /ledger/11 (1791): kazakh-khanate /ledger/38 loses 725 of those cells to Khiva, so that part's counterpart should be kazakh-khanate.
  - 1822: the shape drops 49 lower-Syr-Darya cells with no event. kazakh-khanate /ledger/41 gains 47 cells from Khiva; add the mirror loss.
  - /ledger/20 and the new keyframe khanate-of-khiva_1873: intersect[Karakalpakstan, Khiva 1864] is only 32 delta cells on both banks (including Kungrad on the left bank), and Khorezm + Tashauz omit the left-bank delta, which by most accounts stayed Khivan. The pages opened do not settle the bank.
  - The ruler list has gaps: 1519-1763 and 1910-20.
- Area: infobox 67,521 km2 (1911). No Cliopatria row is alive in 1911; the 1864 shape reused for 1918-19 is 384,765 km2 (ratio 5.7). Acknowledged: the new 1873 keyframe is about 69,000 km2, and 1918-19 are marked wrong.

## Routed to other groups
- ia-02, timurid-empire:
  - Khwarazm should leave the Timurids in 1505 (Urgench), not in the 1507 loss.
  - The 1512 loss of Samarkand and Bukhara should name khanate-of-bukhara, not shaybanids.
  - There is no Balkh event for Babur's 1511-1512 rule.
- ia-03, kazakh-khanate:
  - Its 1496 loss to shaybanids is mirrored here by a found event from nobody.
  - Its 1510 gain from shaybanids (confidence 1) has no Shaybanid loss.
  - Tashkent is not lost between 1521 and 1597.
  - There is no 1812-1813 loss to Khiva.
  - The 1791 and 1822 counterparts differ from Khiva's.
