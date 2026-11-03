# Review of batch se-01-g (2026-10-19)

Reviewer: adversarial review, Phase B. Dossiers: prome-kingdom (fix), first-toungoo-empire (fail), ai-viet (fix). Validator: 0 errors for all three before and after the reviewer's small fixes; 6 warnings on first-toungoo-empire (restored-hanthawaddy-kingdom not yet a dossier). Neighbour dossiers read: kingdom-of-mrauk-u, ayutthaya-kingdom, lan-xang, hanthawaddy-kingdom, shan-states, ava-kingdom, khmer-empire, le-dynasty, lan-na-kingdom, champa. Not yet written: ming-dynasty, nguyen-lords, tibet, trinh-lords, qing-dynasty, cambodia, lan-na, southern-ming, nguyen-dynasty, kingdom-of-luang-phrabang, tay-son-dynasty, konbaung-dynasty.

fix verdict = fixed by the reviewer (applied: true); first-toungoo-empire goes back to the author for the unapplied blocking findings.

## prome-kingdom: fix

What was tried: Validator clean; found/dissolve at start/end; ruler periods contiguous and match the infobox; capital (95.22 E, 18.82 N) inside the bbox; four events confirmed with dates; 1543-1546 years of the last Cliopatria shape correctly cut. The only open issue is the shan-states side (annexation 1533 vs tributary 1532), which is the other dossier's to change.

### Findings

- `/identity/rulers/1..3` (applied): Rulers Bayin Htwe, Narapati and Minkhaung carried no source URL.
  - Evidence: Prome Kingdom page: infobox periods '1482-1526', '1526-1532', '1532-1539', '1539-1542'; text 'Thado Minsaw died in 1526, and was succeeded by his son Bayin Htwe', 'Narapati too died soon after and was succeeded by Minkhaung of Prome'.
  - Fix: Add source https://en.wikipedia.org/wiki/Prome_Kingdom to each.
- `/wars/0/zones` (applied): The 1532 war had empty zones while /ledger/1-2 draw a contest over the whole kingdom in 1532.
  - Evidence: Prome Kingdom page: 'In 1532, the Confederation forces came down and attacked Prome.' Brief section 2.10: every contest_start corresponds to a war's zone.
  - Fix: Zone set to {cliopatria: Prome Kingdom 1502} (the contest region) and the note reworded.

### Thin (for a gap-filler)

- `/ledger (before /ledger/3)`: An earlier, undated Toungoo attack on Prome during the Toungoo-Hanthawaddy War ('When Toungoo troops attacked a heavily fortified Prome, Narapati asked for help from the Confederation in Ava'; the text says Toungoo 'again' laid siege in late 1541). Probably 1539-1540; no contest events drawn. Try https://en.wikipedia.org/wiki/Tabinshwehti
- `/ledger/0`: Year of Thado Minsaw's seizure: the page dates only Mingyi Swa's death (1482); confidence 2 is honest. Try https://en.wikipedia.org/wiki/Thado_Minsaw_of_Prome

### Spot checks

- `/ledger/1` https://en.wikipedia.org/wiki/Prome_Kingdom: confirmed ('In 1532, the Confederation forces came down and attacked Prome.')
- `/ledger/2` https://en.wikipedia.org/wiki/Prome_Kingdom: confirmed ('Prome itself became a tributary of the Confederation in 1532'; infobox 'Kingdom, vassal of Shan states (1532-1542)')
- `/ledger/3` https://en.wikipedia.org/wiki/Prome_Kingdom: confirmed ('In late 1541, Toungoo again laid siege to Prome.')
- `/ledger/4-5` https://en.wikipedia.org/wiki/Prome_Kingdom: confirmed ('On 19 May 1542 (5th waxing of Nayon 904 ME), Minkhaung surrendered.')

Area: infobox none; Cliopatria max 19580 km2. Infobox has no area or capital field; the three Cliopatria outlines differ by under 3 percent and the bbox (17.6-19.6 N, 94.8-96.6 E) fits 'territories up to Tharrawaddy and Myede'.

## first-toungoo-empire: fail

### Findings

- `/keyframe_review/12,13,14,15,16,22,23,24,25,26,27/correction` (NOT applied, blocking): Vassal lands are drawn as direct territory in most keyframes, against the dossier's own rule (/keyframe_review/11: 'Lan Na (1558), Manipur (1560) and the Chinese Shan states (1563) are suzerainties, drawn as vassal tints by the vassal events, not as territory') and against /keyframe_review/21, which removes Lan Na for 1613-1618 because it is a tributary.
  - Evidence: 1564 (ok) keeps Lan Na 180 cells, Manipur 81 and Yunnan 279 (Chinese Shan states, 'at least nominal suzerainty', Bayinnaung page); 1572 and 1579 keep them plus Lan Xang (1,310 cells in 1579, about 375,000 km2) while removing Siam, also a vassal; 1588 and 1595 keep Lan Na and the Chinese Shan states; 1619-1726 (ok/adjust) keep Lan Na, which the Lan Na infobox has as 'Tributary of Burma (2nd): 1615-1628', 'Independent state: 1628-1631', 'Tributary of Burma (3rd): 1631-1727', so it is drawn Toungoo's even in 1628-1631 when /ledger/65-66 make it independent. The lan-xang dossier draws the same Lan Xang cells as its own in new keyframes lan-xang_1575 (1575-1578) and lan-xang_1579 (1579-1587): a double claim of about 375,000 km2.
  - Fix: Apply one rule throughout: subtract the vassal outlines (Lan Na Kingdom 1556 / Lan Na 1600, Lan Xang 1588, Manipur, the Yunnan cells) from the 1564, 1572, 1579, 1588, 1595, 1619, 1653, 1659, 1662, 1670 and 1683 corrections for the years of their vassal spans, as was done for Siam and for 1613; or, if vassal land is to stay inside the outline, add back Lan Na to 1613 and say why in notes. Either way Lan Xang must leave the 1572 (from 1575) and 1579 shapes.
- `/ledger/37` (NOT applied, blocking): The 6 December 1574 event is typed as a gain (annexation) of Vientiane and the middle Mekong at confidence 3, but the page has a vassal king installed, not annexation; the lan-xang dossier has no matching loss.
  - Evidence: Bayinnaung page: 'The Burmese king appointed a younger brother of Setthathirath, Maha Oupahat (Chao Tha Heua), king of Lan Xang'; Lan Xang was kept as a vassal kingdom (a vassal king had already been installed in 1565: 'They had installed a son-in-law of Setthathirath as vassal king'). lan-xang /ledger/15-16: occupation_start 1574-12, occupation_end 1575-4.
  - Fix: Replace with vassal_start lan-xang 1574-12 (or 1565-01, the first vassal king) and an occupation pair 1574-12/1575-04 for Vientiane; delete the confidence-1 /ledger/39 (1579 vassal_start); keep /ledger/45 vassal_end 1591; drop 'plus Vientiane from December 1574' from /keyframe_review/13.
- `/ledger/43` (NOT applied): May 1584 loss of the Northern Cities (confidence 1) removes land the dossier never gains or draws.
  - Evidence: No gain of Phitsanulok, Sukhothai, Kamphaeng Phet or Phichit appears in the ledger, and the 1572 and 1579 corrections subtract Cliopatria's Ayutthaya 1588 outline, which contains them. The ayutthaya-kingdom dossier books their loss in 1563 'as tributaries' and their return in May 1584.
  - Fix: Delete /ledger/43 (the 1584 vassal_end /ledger/42 already ends the relation), or add a 1563-1564 gain or vassal_start for the Northern Cities and draw them.
- `/ledger (1540-1541)` (NOT applied): No contest events for the Martaban siege that the hanthawaddy-kingdom dossier books (contest_start 1540-11, contest_end 1541-5).
  - Evidence: Hanthawaddy /ledger/15-16: 'In November 1540, a 13,000-strong Toungoo force attacked Martaban'; 'in May 1541, Smim Payu's second naval attack broke the harbor defenses'. War /wars/0 already has the zone.
  - Fix: Add contest_start hanthawaddy-kingdom 1540-11 and contest_end 1541-5 over Martaban (admin1 Mon, Kayin).
- `/ledger (1570)` (NOT applied): No occupation pair for the 1570 Burmese invasion of Lan Xang that the lan-xang dossier books (occupation_start 1570-2, occupation_end 1570-4); /wars/8 mentions it in its outcome.
  - Evidence: lan-xang /ledger/13-14: 'Bayinnaung personally led a two-pronged invasion'; 'The search for Setthathirath was called off in April 1570'.
  - Fix: Add occupation_start/occupation_end lan-xang 1570-02/1570-04 (Vientiane, 60 km).
- `/ledger/22,48` (NOT applied): The Lan Na vassalage is opened with counterpart lan-na-kingdom (1558-4) and closed with the same string in 1596, but the lan-na-kingdom dossier ends in November 1564 and hands the state to lan-na.
  - Evidence: lan-na-kingdom /ledger/11: dissolve 1564-11, successor lan-na; Lan Na infobox 'Tributary of Burma (1st): 1558-1596'.
  - Fix: Close lan-na-kingdom at 1564-11 (vassal_end) and open vassal_start lan-na 1564-11 to the 1596 vassal_end, or confirm with the lan-na owner that lan-na-kingdom runs to 1596.
- `/wars/6/zones` (NOT applied): War of 1558-1563 has empty zones and no note saying no ground changed hands.
  - Evidence: Bayinnaung page: Mekuti 'surrendered without a fight on 2 April 1558'; Manipur 'surrendered around February 1560'; Kengtung 'submitted prior to the invasion'; but 'a two-pronged invasion of the Taping valley in March/April 1563'.
  - Fix: Add the Taping valley zone for 1563, or a note that only submissions without fighting are booked.
- `/wars/12/zones` (NOT applied): Burmese-Siamese wars 1584-1593 have empty zones although ground changed hands (the Tenasserim coast) and Siam's independence came out of them; no contest events 1584-1593.
  - Evidence: First Toungoo page: 'five major punitive campaigns against Siam between 1584 and 1593'; ayutthaya-kingdom /ledger/38: Tenasserim and Tavoy besieged and taken in 1593.
  - Fix: Add contest events for the main campaigns (or for the 1593 Tenasserim front) and a zone.
- `/ledger/57/source` (applied): The July 1608 month came from the Prome Kingdom page but the source was the Anaukpetlun page, which gives the year only.
  - Evidence: Anaukpetlun page: 'In 1608, he took Prome' (no month); Prome Kingdom page: 're-annexed by King Anaukpetlun in July 1608'.
  - Fix: Source changed to https://en.wikipedia.org/wiki/Prome_Kingdom (already in sources[]).

### Thin (for a gap-filler)

- `/ledger/68,/ledger/72`: 1653 gain and 1738 loss of the northern Shan states and Kachin hills (about 400 cells, 110,000 km2 each way) rest on Cliopatria only, confidence 1, counterpart not a polity. Try https://en.wikipedia.org/wiki/Pindale_Min
- `/ledger/0`: Founding 1502 at confidence 1; the page has 'By 1502, Mingyi Nyo had already decided to break away' and formal independence on 16 October 1510. Try https://en.wikipedia.org/wiki/Mingyi_Nyo
- `/ledger/3`: Irrawaddy delta 1539 at confidence 1. Try https://en.wikipedia.org/wiki/Toungoo%E2%80%93Hanthawaddy_War
- `/ledger/39,/ledger/45`: Lan Xang vassalage 1579-1591 at confidence 1 (see the blocking finding on /ledger/37). Try https://en.wikipedia.org/wiki/Burmese%E2%80%93Lao_War_(1565%E2%80%931575)
- `/ledger/43,/ledger/47`: Northern Cities May 1584 and Mon provinces 1595 at confidence 1; the ayutthaya-kingdom dossier dates the Mon provinces 1594 from a war page. Try https://en.wikipedia.org/wiki/Burmese%E2%80%93Siamese_War_(1584%E2%80%931593)
- `/ledger/44`: Manipur's exit in 1588 at confidence 1. Try https://en.wikipedia.org/wiki/Nanda_Bayin
- `/keyframe_review/12-14`: About 110 Nagaland, Mizoram, Assam and Arunachal cells in the 1564-1587 shapes, 'unverified: page budget'. Try https://en.wikipedia.org/wiki/Bayinnaung
- `/identity/rulers`: No ruler strip although reign dates for Tabinshwehti, Bayinnaung, Nanda, Anaukpetlun and Mahadhammaraza Dipadi are on the pages read. Try https://en.wikipedia.org/wiki/List_of_Burmese_monarchs

### Spot checks

- `/ledger/19` https://en.wikipedia.org/wiki/Bayinnaung: confirmed ('By March 1557, Bayinnaung in one stroke controlled most of the cis-Salween Shan states'; Mohnyin 6 March, Mogaung 11 March 1557)
- `/ledger/22` https://en.wikipedia.org/wiki/Bayinnaung: confirmed ('Mekuti surrendered without a fight on 2 April 1558')
- `/ledger/37` https://en.wikipedia.org/wiki/Bayinnaung: not on page as typed: date 6 December 1574 confirmed but the page has a vassal king appointed, not an annexation (blocking finding)
- `/ledger/46` https://en.wikipedia.org/wiki/First_Toungoo_Empire: confirmed ('Siam seized the entire Tenasserim coast in 1595')
- `/ledger/59` https://en.wikipedia.org/wiki/Anaukpetlun: confirmed ('took the port of Syriam in 1613'; no month)
- `/ledger/73-77` https://en.wikipedia.org/wiki/Restored_Hanthawaddy_Kingdom: confirmed (governor at Pegu 'assassinated on 29 November 1740'; 'By 1745 ... up to Prome and Toungoo'; invasion 'November 1751'; Ava sacked 'in March 1752', day not given on this page)

Area: infobox none; Cliopatria max 1477943 km2. First Toungoo Empire infobox has no area (capitals 'Toungoo (1510-1539) Pegu (1539-1599)', independence '16 October 1510', fall '19 December 1599'); Bayinnaung page only 'the largest empire in Burmese history'. The author's removal of Siam (1,132 cells) from 1572/1579 is sound; the remaining vassal cells are the blocking finding.

## ai-viet: fix

### Findings

- `/identity/rulers/1..7` (applied): Seven of eight rulers carried no source URL.
  - Evidence: Mạc dynasty page monarch list: 'Mạc Thái Tông (Mạc Đăng Doanh) (1529-40)', 'Mạc Hiến Tông (Mạc Phúc Hải) (1540-46)', 'Mạc Tuyên Tông (Mạc Phúc Nguyên) (1546-61)', 'Mạc Mậu Hợp (1562-92)', 'Mạc Toàn (1592-93)'; Mạc Kính Cung 'ruled for more than thirty years (1593-1625)'; infobox '1638-1677: Mạc Kính Vũ (last)'.
  - Fix: Add source https://en.wikipedia.org/wiki/M%E1%BA%A1c_dynasty to each.
- `/ledger/4,/ledger/5,/ledger/6` (NOT applied): The 1559-1561 and 1570-1572 campaigns name trinh-lords as counterpart while the le-dynasty dossier (1428-1571, successors trinh-lords and nguyen-lords) is alive and carries no contest with ai-viet; Cliopatria's Trịnh lords row starts in 1572.
  - Evidence: Lê-Mạc War page: 'Trịnh Kiểm, the military regent of the Lê dynasty' ordered the September 1559 offensive; 'In October 1572, Mạc forces retreated back to the north.' le-dynasty ledger has only 1527 loss and 1533 gain with ai-viet.
  - Fix: Orchestrator to decide with the trinh-lords owner: if trinh-lords starts in 1572, use le-dynasty for /ledger/4-5 and either split /ledger/6-8 at 1571/1572 or name le-dynasty; if it starts in 1545 (Trịnh Kiểm), keep. Either way le-dynasty needs the mirror contests.

### Thin (for a gap-filler)

- `/ledger/2`: Location and size of the 1540/1541 cession to the Ming: only 'ceded half of Quảng Ninh province to China' (Lê-Mạc War) is on a page; drawn as 45 km around Móng Cái at confidence 2. Try https://en.wikipedia.org/wiki/M%E1%BA%A1c_%C4%90%C4%83ng_Dung
- `/wars/2,/identity/rulers`: The 1627 Lê attack on Cao Bằng and Mạc Kính Khoan's surrender (page names him without years); ruler gap 1625-1638. Try https://en.wikipedia.org/wiki/M%E1%BA%A1c_K%C3%ADnh_Khoan

### Spot checks

- `/ledger/1` https://en.wikipedia.org/wiki/L%C3%AA%E2%80%93M%E1%BA%A1c_War: confirmed (1533, Nguyễn Kim; 'Lê army regained the provinces of Thanh Hóa and Nghệ An')
- `/ledger/3` https://en.wikipedia.org/wiki/L%C3%AA%E2%80%93M%E1%BA%A1c_War: confirmed ('In 1554, Trịnh Kiểm ... dispatched 25,000 men to the south and easily regained two provinces, Thuận Hóa and Quảng Nam from the Mạc')
- `/ledger/12-13` https://en.wikipedia.org/wiki/L%C3%AA%E2%80%93M%E1%BA%A1c_War: confirmed (14 and 25 November 1592; 'In April 1593, the southern emperor Lê Thế Tông was welcomed back to Đông Kinh')
- `/ledger/14` https://en.wikipedia.org/wiki/L%C3%AA%E2%80%93M%E1%BA%A1c_War: confirmed ('completedly defeated by Trịnh clan in 1677'; Mạc page infobox 'Loss of Cao Bằng: 1677')

Area: infobox none; Cliopatria max 190572 km2. Mạc dynasty infobox has no area (capitals 'Đông Kinh (1527-1592) Cao Bằng (1592-1677)'). Shapes 1683-1830 correctly marked wrong as Panduranga, which the champa dossier carries (champa_1653, champa_1695).

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| prome-kingdom 1482 found ava-kingdom | ava-kingdom 1482 loss | matched | predecessor land |
| prome-kingdom 1532 contest_end shan-states | shan-states 1533 gain | mismatch | shan-states books annexation of Prome in 1533 (and loss to first-toungoo-empire 1542, c1); Prome page: 'tributary of the Confederation in 1532', infobox 'vassal of Shan states (1532-1542)'. shan-states should switch to vassal_start/vassal_end prome-kingdom 1532-1542 and drop the 1542 loss. Flagged by the author. |
| prome-kingdom 1542 loss first-toungoo-empire | first-toungoo-empire 1542 gain | matched | 19 May 1542 |
| first-toungoo-empire 1502 found ava-kingdom | ava-kingdom 1502 loss | matched |  |
| first-toungoo-empire 1538 gain hanthawaddy-kingdom | hanthawaddy-kingdom 1538 loss | matched | Pegu |
| first-toungoo-empire 1539 gain hanthawaddy-kingdom | hanthawaddy-kingdom 1539 loss | matched | delta |
| hanthawaddy-kingdom 1540 contest_start first-toungoo-empire | - | missing | Martaban siege 1540-11 to 1541-5 has no contest pair in first-toungoo-empire |
| first-toungoo-empire 1541 gain hanthawaddy-kingdom | hanthawaddy-kingdom 1541 loss | matched | Martaban, May 1541 |
| first-toungoo-empire 1544 gain shan-states | shan-states 1545 loss | matched | Pagan; 1544 vs 'by 1545', within a year |
| first-toungoo-empire 1546 contest_start kingdom-of-mrauk-u | kingdom-of-mrauk-u 1546 occupation_start | mismatch | FTE books a contest 1546-10 to 1547-01, mrauk-u an occupation of Thandwe 1546-10 to 1547-03; agree on one type |
| first-toungoo-empire 1547 contest_start ayutthaya-kingdom | - | missing | Burmese-Siamese War 1547-1549 has no events in ayutthaya-kingdom |
| first-toungoo-empire 1555 gain shan-states | shan-states 1555 loss | matched | Ava, 22 January 1555 |
| first-toungoo-empire 1557 contest_start shan-states | shan-states 1556 contest_start | matched | within a year; contest_end 1557-3 both |
| first-toungoo-empire 1557 gain shan-states | shan-states 1563 dissolve | exception | shan-states books no loss for the 1557 conquests, only its 1563 dissolve with first-toungoo-empire as successor |
| first-toungoo-empire 1558 vassal_start lan-na-kingdom | - | missing | lan-na-kingdom has no vassal events and ends 1564-11; FTE's vassal_end lan-na-kingdom 1596 outlives it (lan-na not written yet) |
| first-toungoo-empire 1560 vassal_start Manipur Kingdom | - | exception | in counterparts_needing_dossiers |
| first-toungoo-empire 1562 vassal_start Kengtung | - | exception | in counterparts_needing_dossiers |
| first-toungoo-empire 1563 vassal_start Chinese Shan states | - | exception | in counterparts_needing_dossiers |
| first-toungoo-empire 1564 contest_end ayutthaya-kingdom | ayutthaya-kingdom 1563 loss | mismatch | ayutthaya books the Northern Cities lost to FTE in 1563 'as tributaries'; FTE books no gain or vassal_start for them but loses them in 1584 (/ledger/43) |
| first-toungoo-empire 1564 gain ayutthaya-kingdom | ayutthaya-kingdom 1564 loss | matched | western strip, February 1564 |
| first-toungoo-empire 1565 occupation_start lan-xang | lan-xang 1565 occupation_start | matched | 2 January to 1 August 1565 |
| lan-xang 1570 occupation_start first-toungoo-empire | - | missing | February-April 1570 occupation absent from first-toungoo-empire |
| first-toungoo-empire 1568 contest_start ayutthaya-kingdom | ayutthaya-kingdom 1568 contest_start | matched | to 2 August 1569 |
| first-toungoo-empire 1574 gain lan-xang | lan-xang 1574 occupation_start | mismatch | FTE annexes Vientiane; lan-xang has an occupation 1574-12/1575-4 and draws all of Lan Xang as its own (vassal) in lan-xang_1575 and lan-xang_1579; Bayinnaung page has a vassal king appointed. Blocking for FTE. |
| first-toungoo-empire 1579 vassal_start lan-xang | - | mismatch | FTE confidence 1; its 1579 keyframe still draws the 1,310 Lan Xang cells as territory while lan-xang_1579 draws them as Lan Xang's: double claim 1579-1587 |
| first-toungoo-empire 1580 occupation_start kingdom-of-mrauk-u | kingdom-of-mrauk-u 1580 occupation_start | matched | Sandoway: November 1580 (Bayinnaung page) vs 9 September 1580 (mrauk-u) |
| first-toungoo-empire 1584 loss ayutthaya-kingdom | ayutthaya-kingdom 1584 gain | matched | date matches; FTE never drew the land (see fix on /ledger/43) |
| first-toungoo-empire 1595 loss ayutthaya-kingdom | ayutthaya-kingdom 1593 gain | mismatch | Tenasserim coast: 1595 (First Toungoo page, confirmed) vs 1593 (ayutthaya, war page); two years apart, both sourced; flagged by the author |
| first-toungoo-empire 1595 loss ayutthaya-kingdom | ayutthaya-kingdom 1594 gain | matched | Mon provinces; FTE at confidence 1 |
| ayutthaya-kingdom 1595 contest_start first-toungoo-empire | first-toungoo-empire 1600 contest_start | mismatch | ayutthaya's contest runs 1595-01 to 1600-05 (Naresuan's march on Pegu); FTE's only 1600 |
| first-toungoo-empire 1597 loss Shan states and other former vassals | - | missing | composite counterpart with no dossier and not in counterparts_needing_dossiers |
| first-toungoo-empire 1599 loss Lower Burma lords: Toungoo, Prome, Syriam and Arakan | kingdom-of-mrauk-u 1599 occupation_start | mismatch | mrauk-u books occupations of Syriam (1599-03) and Pegu (1599-12, ended 1600-03; Syriam lost 1603-03); FTE books an outright loss to a composite counterpart |
| first-toungoo-empire 1608 gain Prome principality | - | exception | in counterparts_needing_dossiers |
| first-toungoo-empire 1610 gain Natshinnaung's Toungoo | - | exception | listed with the Prome principality in counterparts_needing_dossiers; string differs |
| first-toungoo-empire 1613 gain Portuguese Syriam | - | exception | in counterparts_needing_dossiers |
| first-toungoo-empire 1613 gain ayutthaya-kingdom | ayutthaya-kingdom 1613 loss | matched | Tavoy 1613; but ayutthaya books the Mon provinces lost only in 1618 (c1) where FTE has them in 1613 (First Toungoo page) |
| first-toungoo-empire 1613 contest_start ayutthaya-kingdom | - | missing | 1613-1618 contest has no pair in ayutthaya-kingdom |
| first-toungoo-empire 1614 vassal_start lan-na | ayutthaya-kingdom 1618 vassal_end | mismatch | lan-na not written (se-01 part not run); ayutthaya holds Lan Na as its vassal 1600-1618, overlapping FTE's 1614 start (Lan Na infobox: Ayutthaya 1596-1615, Burma 1615-1628) |
| first-toungoo-empire 1653 gain northern Shan states and Kachin hills | - | missing | no polity; confidence 1 |
| first-toungoo-empire 1663 contest_start ayutthaya-kingdom | ayutthaya-kingdom 1663 contest_start | matched | to May 1664 |
| first-toungoo-empire 1738 loss northern Shan states and Kachin hills | - | missing | no polity; confidence 1 |
| first-toungoo-empire 1740 loss restored-hanthawaddy-kingdom | - | exception | in counterparts_needing_dossiers (also 1745, 1751-1752) |
| ai-viet 1527 found le-dynasty | le-dynasty 1527 loss | matched | 15 June 1527 |
| ai-viet 1533 loss le-dynasty | le-dynasty 1533 gain | mismatch | dates match; land differs: le-dynasty takes the far south (Quảng Bình to Bình Định) in 1533, ai-viet keeps it to 1554 per the Lê-Mạc War page |
| ai-viet 1540 loss ming-dynasty | - | exception | ming-dynasty owned by ea-07, not run yet |
| ai-viet 1554 loss le-dynasty | - | missing | le-dynasty has no 1554 gain; the page ('regained two provinces, Thuận Hóa and Quảng Nam from the Mạc' in 1554) supports ai-viet, so le-dynasty should change |
| ai-viet 1559 contest_start trinh-lords | - | mismatch | trinh-lords not written; le-dynasty alive to 1571 with no contest; see fix on /ledger/4-6 |
| ai-viet 1570 contest_start trinh-lords | - | mismatch | as above (to 1572-10) |
| ai-viet 1572 occupation_start trinh-lords | - | exception | trinh-lords (se-01) not written yet |
| ai-viet 1592 loss trinh-lords | - | exception | trinh-lords not written yet (also contest 1592-2/1593-4) |
| ai-viet 1677 loss trinh-lords | - | exception | trinh-lords not written yet |

## Problems

- WebFetch returns model summaries, not raw pages; quotes are the summariser's.
- No infobox of the three states gives an area, so no area ratio could be computed.
- Neighbour dossiers not yet written (no cross-check possible): ming-dynasty, nguyen-lords, tibet, trinh-lords, qing-dynasty, cambodia, lan-na, southern-ming, nguyen-dynasty, kingdom-of-luang-phrabang, tay-son-dynasty, konbaung-dynasty.
- Routed to other owners: shan-states (Prome 1532-1542 as vassal, not annexation); le-dynasty (far south to 1554; mirror contests 1559-1572); lan-xang (pending FTE rework of 1574-1591); ayutthaya-kingdom (no 1547-1549 events, 1593 vs 1595 Tenasserim, 1618 vs 1613 Mon provinces, no 1613-1618 contest); kingdom-of-mrauk-u (1546-47 and 1599-1603 event types); lan-na-kingdom (no vassal_start 1558).
- Reviewer applied small fixes in place (prome-kingdom rulers' sources and war-0 zone; first-toungoo-empire /ledger/57 source; ai-viet rulers' sources); all three re-validated with 0 errors.
