# Review of batch se-01-h (2026-10-19)

Dossiers: trinh-lords, nguyen-lords, lan-na, cambodia, kingdom-of-champasak. Neighbours read: ai-viet, champa, le-dynasty, post-angkor-cambodia, khmer-empire, lan-xang, lan-na-kingdom, first-toungoo-empire, ayutthaya-kingdom (the other context polities have no file yet). All five validate with `--resolve` (cambodia: 3 warnings for its empty corrections, by design). No infobox of the five gives an area, so the area checks are n/a. Machine copy: history/notes/phase-b/reviews/se-01-h.json.

| slug | verdict | why |
| --- | --- | --- |
| trinh-lords | fix (fixed by reviewer) | 8 events checked on 4 pages, all confirmed; keyframe walk clean; ruler span fixed |
| nguyen-lords | fail | 174 cells lost in 1775 with no event; the 1700 'Cambodia' union takes Panduranga (Bình Thuận) from champa |
| lan-na | thin | 1664 withdrawal re-dated by reviewer; no territorial event in 210 years |
| cambodia | fail | null row with losses of land it never holds; duplicates post-angkor-cambodia's 1700 loss |
| kingdom-of-champasak | thin | 5 events confirmed; ruler span fixed; 1828 loss is confidence 1; 1893-1904 right bank not drawn |

## nguyen-lords (fail)

1. **/keyframe_review/11, /ledger/22-27: 174 cells lost with no event.** The 1773 keyframe has 580 cells and the 1775 one 295. Take away /ledger/24 (Quảng Nam, Quảng Ngãi) and /ledger/27 (Thuận Hóa) and 174 cells (~40,000 km2) are still unexplained: Phú Yên 19, Khánh Hòa 14, Kon Tum 35, Gia Lai 55, Đắk Lắk 42. Fix: add a 1774 or 1775 loss of these lands to tay-son-dynasty (Tây Sơn dynasty page), or widen /ledger/24 to cover them.
2. **/ledger/16 and /keyframe_review/5-11: the union with the 'Cambodia' row takes Panduranga.** The Cliopatria 'Cambodia' row has all 27 cells of Bình Thuận, plus Lâm Đồng 33, Đắk Nông 20, Bình Phước 24 and Tây Ninh 13, as well as the delta. Bình Thuận is Panduranga, which:
   - this dossier's own /ledger/14 makes a client from 1695;
   - champa draws as Cham land from 1695 to 1832 (a 28-cell overlap with champa /keyframe_review/25);
   - the Panduranga page also keeps Cham: the revolts of 1693-96 forced the lord to abolish the Bình Thuận county, and the capital stayed at Phan Rí Cửa until 1832.

   Fix: write the union as `{"minus": [{"cliopatria": "Cambodia", "year": 1757}, {"admin1": "Bình Thuận", "country": "Vietnam"}]}`. Name the uplands in the text, or take them out (the Post-Angkor sentence names only the Mekong Delta).
3. /keyframe_review/0 note: 133 of the 296 cells in the 1572 shape (Kon Tum, Gia Lai, Đắk Lắk) are the Central Highlands, about 45% of its area. The note does not mention them. Either acknowledge them or adjust the keyframe.
4. /identity/rulers/0: Nguyễn Hoàng starts in 1558, before the dossier starts in 1572. Change it to 1572 and keep 1558 in the note.
5. The 1739-1749 contest and the 1755 gain name post-angkor-cambodia as counterpart. Their mirrors are in cambodia.json, not in post-angkor-cambodia. Settle this after the cambodia decision.
6. Cross-dossier: champa loses Phú Yên to nguyen-lords in 1611, but this dossier holds Phú Yên from 1572 and has no gain in 1611. The two overlap on 19 cells from 1572 to 1610. The Panduranga page supports the Nguyễn side ('in an attempt to retake land from the Nguyen lord, Champa mounted an attack in Phu Yen'), so this goes to champa's owner.
7. Thin, for a gap-filler: the dated Nam tiến steps (1698 Gia Định, 1708 Hà Tiên and Mạc Cửu, 1732, 1756-1757). There are also four confidence-1 events, and ayutthaya's 1715-1717 contest has no mirror here.

Spot checks, all confirmed:
- /ledger/2, /5, /6, /12 and /14 on the Panduranga page;
- /ledger/7 on the Trịnh–Nguyễn War page;
- /ledger/16 on the Post-Angkor page (the wording is there but no year);
- /ledger/19, /21, /29, /30 and /32 and the capitals on the Nguyễn lords page.

## trinh-lords (fix, applied by reviewer)

- Applied: /identity/rulers/0 Trịnh Tùng `from` 1570 → 1572 (inside the life; the note keeps the page's 1570).
- Confirmed:
  - /ledger/1, /4 and /9 on the Mạc dynasty page;
  - /ledger/7, /8, /10 and /12 on the Trịnh–Nguyễn War page (15 November 1774; February 1775);
  - /ledger/5 and /16 on the Trịnh lords page.
- /ledger/13 (Thuận Hóa held to 1786, confidence 2) is supported by the Trịnh lords page: in summer 1786 Nhạc 'wanted to reclaim the land of the Nguyễn lords taken by the Trịnh in 1775'.
- Keyframe walk: every change between shapes is explained.
- Thin: the Tây Sơn occupation of Thăng Long in 1786 is not drawn, and the Gianh frontier is undated.

## lan-na (thin)

- Applied: /ledger/3 occupation_end 1663 → 1664. On the Burmese–Siamese War (1662–1664) page, 'Later that year, the Siamese relinquished control of Lan Na' comes after the May 1664 retreat and carries no year of its own. ayutthaya-kingdom still has 1663, which is within a year.
- Confirmed on the Lan Na page: /ledger/0 (November 1564), /1 (January 1579), /4 (1727) and /5 (15 January 1775). /ledger/2 (February 1663) is confirmed on the war page.
- Thin:
  - no territorial event at all from 1565 to 1775;
  - the infobox's 'Independent city-states: 1727-1763' is drawn as one Lan Na;
  - 2 of the 5 budget pages were not used.
- Orchestrator: lan-na and lan-na-kingdom are one state in two dossiers.

## cambodia (fail)

1. /ledger/1: the dossier holds no land (all three corrections are empty), yet it loses 271 cells to nguyen-lords in 1700. That is the same loss that post-angkor-cambodia /ledger/6 already records, so the land is counted twice.
2. /ledger/4: a 1755 loss of 17 cells the dossier never holds. This is the mirror of nguyen-lords /ledger/21, which names post-angkor-cambodia as counterpart.
3. /wars/0 runs 1658-1755, which starts outside the dossier's life (1700-1802).
4. The notes describe the row as 'the delta and the Đồng Nai and Tây Ninh lowlands'. It also covers all of Bình Thuận and the Lâm Đồng, Đắk Nông and Bình Phước uplands.

Fix, after the orchestrator decides: either keep a null row with only the found and dissolve events, or move the Name 'Cambodia' and its three verdicts into post-angkor-cambodia together with the 1739-1749 contest and the 1755 loss. Option (3) in the author's notes stays open: the western delta Cambodian until 1732-1757.

Confirmed: /ledger/1 (Post-Angkor wording) and /2 and /4 (Nguyễn lords page).

## kingdom-of-champasak (thin)

- Applied: /identity/rulers/11 Kham Souk `to` 1899 → 1893 (the note keeps 1863-1899).
- Confirmed: /ledger/0 (1713), /1 (1778) and /6 (Left Bank in 1893) on the Kingdom of Champasak page; /ledger/2 (1779) and /3 (January 1827) on the Lao rebellion page.
- Thin:
  - /ledger/5: the 1828 loss of 18 west-bank cells is confidence 1. The page says only that Champasak 'was reduced to vassalage'.
  - The infobox has 'Vassal of Siam (1778–1904)', but the dossier ends in October 1893, so the right bank around Bassac from 1893 to 1904 is not drawn.

## Cross-dossier matrix (summary)

Matched:
- Trịnh with ai-viet: 1572 occupation, 1592, 1677.
- Trịnh with Nguyễn: 1653, 1656, 1775.
- Nguyễn with champa: 1653, 1692-1694.
- Nguyễn with post-angkor-cambodia: 1700.
- lan-na with ayutthaya: 1663-1664.

Missing:
- champa's 1611 loss of Phú Yên;
- nguyen's 1691 gain (post-angkor-cambodia has no loss);
- ayutthaya's 1715 contest.

Mismatch:
- nguyen's 1755 gain and the 1739 contest: the counterpart slug differs from the dossier that holds the mirror;
- cambodia's 1700 loss duplicates post-angkor-cambodia's;
- the 1700 'Cambodia' land includes champa's Bình Thuận;
- ai-viet's 1559-1572 contests name trinh-lords before 1572 (le-dynasty should be the counterpart).

Exceptions (counterpart not written yet): tay-son-dynasty, thonburi-kingdom, rattanakosin-kingdom, vientiane, french-indochina. Suzerain-only vassal records are also treated as exceptions (first-toungoo-empire and ayutthaya for lan-na; nguyen for Panduranga).
