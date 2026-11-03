# Notes, group se-01-h (Phase B, run of 2026-10-19)

Five dossiers: trinh-lords, nguyen-lords, lan-na, cambodia, kingdom-of-champasak. All validate with `--resolve` (cambodia has 3 warnings: its three corrections are intentionally empty regions). 19 distinct pages opened; the dossiers' own `notes` hold the detail. Read this first.

## Decisions the orchestrator should confirm

1. **lan-na is the same state as lan-na-kingdom** (shared Q1059707 and the Lan Na article). The brief asks for one dossier under the earlier slug; lan-na-kingdom.json belongs to another batch and was not edited, so lan-na.json continues it (1565 to 15 January 1775, same 180 cells, same colour, new keyframes for 1565-1599, 1619-1733, 1762-1775 where Cliopatria has no shape). To merge: add "Lan Na" to lan-na-kingdom's cliopatria_names, move this file's keyframes and ledger in, drop the 1564 dissolve there.
2. **cambodia is a null row (revised in the fix pass below: found and dissolve only, no territorial events).** Cliopatria's 'Cambodia' (1700-1802, Q424, 'Cambodia Middle Period') is the Mekong delta that its Khmer Empire row loses in 1700 (287 of 295 cells) and touches no Nguyễn cell. 'Cambodia Middle Period' is the Post-Angkor period article, i.e. post-angkor-cambodia. Following the Post-Angkor page ('by the end of the 17th century ... full Vietnamese administrative control') and that dossier's own 1700 loss, the delta is drawn by nguyen-lords from 1700 (the 17 western cells from 1755), and all three cambodia shapes are `wrong` with empty corrections. Alternative: keep the delta Cambodian to 1757 (then change nguyen-lords' 1700 gain and its 'union with Cambodia' corrections and mark cambodia ok), or merge the Name into post-angkor-cambodia. kingdom-of-cambodia (1956-2024, also Q424) is a different, modern state and was not merged.
3. **Years that differ from Cliopatria:** Trịnh Đông Kinh 1592 (shape from 1595); Trịnh Thuận Hóa 1775-1786 and Nhạc's land as a Trịnh client 1775-1778 (Cliopatria: whole middle country 1775-1777, none after); Champasak 1713 (Cliopatria 1709) to October 1893 (Cliopatria 1894); Nguyễn lords end 1777 (Cliopatria 1775).

## Per state

- **trinh-lords** (7 of 9 pages): Trịnh page has no area. Thuận Hóa held to 1786 is confidence 2 (Hoàng Ngũ Phúc page: viceroy, successor Bùi Thế Đạt; Quang Trung page: Huệ marches on Phú Xuân in 1786); the Trịnh lords page's 'withdrew ... leaving the south to the Tây Sơn' is the contrary statement. No months for 1786 (the brief's June/July 1786 are on none of the pages). Gianh River frontier is 9 cells south of Cliopatria's line, undated, left. 1694 Laos war and Lao tribute undated, no land. Seven cells of the 1677 outline fall in China, read as artefacts.
- **nguyen-lords** (6 of 5 pages; Nam tiến was thin): Phú Yên: the Panduranga page implies Nguyễn held it before 1611 (champa's ledger has the loss at 1611, unmirrored); Khánh Hòa 1611 annexation contradicts the page's own 1653 loss, drawn as a contest 1611-1653. Not on any page: 1698 Gia Định, 1708 Hà Tiên, 1757 Tầm Phong Long, 1674-1699 Cambodian events. ayutthaya-kingdom's 1715-1717 contest with nguyen-lords is unmirrored (no page). Panduranga's client status (1695) is closed in 1777 only because the dossier ends; it runs to 1832.
- **lan-na** (3 of 5): no page gives Lan Na's extent for 1558-1775, so no gain or loss is dated. Vassal records belong to the suzerains (first-toungoo-empire and ayutthaya-kingdom have theirs; konbaung-dynasty 1757/1763 and thonburi-kingdom 1775 are still to be written). Ong Kham (Luang Prabang) offered the throne 1727, ruled to 1769 (his page) against the infobox's last ruler Po Mayu-nguan 1768-1775.
- **cambodia** (2 of 2): see decision 2.
- **kingdom-of-champasak** (5 of 5; the first page, 'Champasak', is a disambiguation): 1828 loss of the land around Champasak town is Cliopatria's, page silent (confidence 1). 1709-1712 land has no state. Cliopatria has no French Indochina outline over the Left Bank in 1894 (starts 1895): french-indochina should start the Left Bank in October 1893. Rulers list ends 1899 (past the dossier's end). Undated: Stung Treng, Kontum, Pleiku. Soi Sisamut and Phraya Supho (named in the brief) are on none of the pages.

## Pages that failed or were empty

- https://en.wikipedia.org/wiki/Nguyễn_Huệ: URL_NOT_FOUND on the first try; Quang Trung (the article's title) opened instead.
- https://en.wikipedia.org/wiki/Champasak: disambiguation page, no content.
- https://en.wikipedia.org/wiki/Nam_tiến: opened, no dated Nguyễn expansion.

## Counterparts without a dossier at the time of the run

tay-son-dynasty, nguyen-dynasty, thonburi-kingdom, chiangmai, konbaung-dynasty, rattanakosin-kingdom, vientiane (all se-01, other parts), french-indochina (se-03).

## Gazetteer

No unknown names: every region resolves (Natural Earth spellings 'Ha Tinh', 'Quàng Nam', 'Thừa Thiên - Huế' used as listed).

## Fix pass (2026-10-19), after review-se-01-h

Pages opened in the fix pass: Nguyễn Nhạc, Nguyễn Hữu Cảnh, Mạc Cửu, Cochinchina and Barom Ramadhipati (the Ang Em page) are new; Tây Sơn dynasty, Nguyễn lords and Panduranga (Champa) were read again. Failed: https://en.wikipedia.org/wiki/Siamese–Vietnamese_War_(1717) (URL_NOT_FOUND; the Barom Ramadhipati page was used for 1714-1717 instead). Both files validate with `--resolve` (nguyen-lords 0 warnings; cambodia 3 warnings, its empty corrections).

### nguyen-lords: all five findings applied
1. **174 cells with no event.** The Tây Sơn dynasty page the reviewer named is silent on Phú Yên, Khánh Hòa and the highlands (it dates only Quy Nhơn 1773 and Gia Định 1776). The Nguyễn Nhạc page has 'the country from Quảng Ngãi to Bình Thuận was occupied by Tây Sơn rebels' after Lord Thuần fled to Gia Định (no year; the sequence is 1775). /ledger 1775 (loss to tay-son-dynasty, confidence 2) is therefore widened from Quảng Nam and Quảng Ngãi to Quảng Nam, Quảng Ngãi, Phú Yên, Khánh Hòa and Đà Nẵng, and its source is the Nguyễn Nhạc page. The Central Highlands (Kon Tum, Gia Lai, Đắk Lắk, with one cell each of Lâm Đồng and Đắk Nông) are not given to the Tây Sơn: no page puts them under the Nguyễn at all (see 3), so they leave the shape in every keyframe. A walk of the 12 keyframes against the gain and loss events now leaves only coast and edge cells (at most 7 per step, none of them named by a province).
2. **Panduranga inside the 'Cambodia' union.** The 1700 gain and every union now use the Cambodia row minus Ninh Thuận, Bình Thuận, Lâm Đồng, Đắk Nông, Bình Phước and Đắk Lắk: 163 of the row's 271 cells (the delta and the Đồng Nai, Bình Dương and Tây Ninh lowlands). Panduranga stays the 1695 client tint (/ledger 1692-1695), no longer double-drawn as Nguyễn land and no longer overlapping champa. I took the Lâm Đồng, Đắk Nông and Bình Phước uplands out as well (77 cells, the reviewer's second option): the Post-Angkor sentence names only the Mekong Delta. Tây Ninh (13 cells) stays as Cliopatria's reading; no page dates it.
3. **Highlands in the 1572 note.** Acknowledged and dropped (not just noted): 133 of 296 cells (about 45%). Keyframes 1572 to 1775 are now `adjust` with the highlands subtracted. The Nguyễn lords and Cochinchina pages are silent on the highlands. If the orchestrator would rather keep Cliopatria's outline, remove the `minus` of the five-province union in each keyframe and the 1775 loss then needs the 133 cells added to its region.
4. **Nguyễn Hoàng** starts in 1572; 1558 is in the note.
5. **Counterpart mismatch (1739-1749, 1755).** I kept post-angkor-cambodia as the counterpart and removed the mirrors from cambodia, which holds no land: the mirrors belong in post-angkor-cambodia (another batch). Reported under counterparts_needing_dossiers.

### Changes beyond the findings (thin items, pages now open)
- **1698 Saigon.** The Nguyễn Hữu Cảnh page: 'In 1698, Canh was sent by Nguyễn Phúc Chu to the south. He founded Gia Dinh garrison there' and 'founded the city of Saigon in 1698'. The confidence-1 gain of 1691 (a two-cell change in Cliopatria) is now 1698, confidence 2; keyframes 1659 and 1691 are re-dated 1659-1697 and 1698-1699.
- **1715-1717.** Mirror of ayutthaya-kingdom's contest added (contest_start 1715 at confidence 2; contest_end 1717 at confidence 1, the page does not date the end), and the zero-zone 1714 war is now 'Siamese-Nguyễn struggle for Cambodia (1714-1717)' with zone Cambodia.
- **Panduranga's vassal_end** moved from 1777 (confidence 1, 'dossier ends') to 1775 (confidence 2) on the Nguyễn Nhạc sentence above. The Panduranga page is silent on the 1770s.
- **Hà Tiên.** The Mạc Cửu page contradicts a whole-delta 1700 gain: 'Hà Tiên was a part of Cambodia until the year 1714' (a footnote: he offered Hà Tiên to the Nguyễn that year), tribute and Nguyễn titles in 1708, a Cambodian invasion in 1715, a Siamese expedition in 1771. The 17 western cells stay out of the shape until 1755 (as before), so the gain is not changed; Hà Tiên as a Nguyễn dependency has no vassal events here because 1708/1714 is a title and a footnote, and its tie lasts past 1755. It needs a dossier (see report). Not drawn: 1732 Mỹ Tho and Vĩnh Long and 1756-1757 Tầm Phong Long (Mạc Cửu, Cochinchina, Nguyễn Hữu Cảnh and Nguyễn lords are all silent).
- The four confidence-1 events: 1699 and 1749 contest ends and 1717 (new) stay at 1; Cochinchina is silent on all of them. The 1691 gain and the 1777 vassal end were re-dated and are no longer confidence 1.

### cambodia: null row, as the reviewer's first option
- Removed: the 1700 loss to nguyen-lords (duplicate of post-angkor-cambodia /ledger/6), the 1739 and 1749 contest events, the 1755 loss and the 1658-1755 war (it started before 1700). Kept: found 1700 and dissolve 1802 (the validator requires both), three `wrong` verdicts with empty corrections, `wars` empty. Successors now list champa for Bình Thuận and Ninh Thuận, nguyen-lords for the 163 delta cells and nguyen-dynasty as before.
- Notes and keyframe note now describe the whole row: delta and lowlands 179 cells, Panduranga 28, uplands 80 (Lâm Đồng 33, Đắk Nông 20, Bình Phước 24, Đắk Lắk 3).
- Disagreement with the review: none on the dossier. The thin question (Cambodian western delta until 1732-1757) cannot be settled from the Mạc Cửu page, which is about Hà Tiên only; row kept `wrong`. A merge of the Name into post-angkor-cambodia stays the orchestrator's option, in which case this file is dropped.

### Still open for other batches
- post-angkor-cambodia: no mirror for nguyen-lords' 1739-1749 contest and 1755 gain (Gulf of Siam coast, Kiên Giang and Cà Mau); its 1700 loss takes the whole 295-cell land including Bình Thuận, the uplands and the Hà Tiên strip that the Mạc Cửu page has Cambodian to 1714; its 1699 contest end is one year before the Cliopatria change and the Nguyễn Hữu Cảnh page has the war in Cambodia itself in 1700 (Kampot, Phnom Penh).
- champa: its 1611 loss of Phú Yên is unmirrored here and the Panduranga page puts Phú Yên under the Nguyễn before 1611 (19 cells overlap, 1572-1610); the Nguyễn Nhạc page has Bình Thuận occupied by the Tây Sơn about 1775.
- tay-son-dynasty: should carry the 1773 gain of Bình Định, the 1775 gain of Quảng Nam to Khánh Hòa and the 1776-1777 Gia Định gain.
- New state Cliopatria lacks: Hà Tiên (Mạc clan principality, about 1708 to 1771 or 1832); no dossier yet.

