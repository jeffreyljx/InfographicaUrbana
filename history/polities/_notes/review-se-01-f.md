# Review of batch se-01-f (reviewer, 2026-10-19)

Dossiers: lan-xang, ava-kingdom, kingdom-of-mrauk-u, le-dynasty. Neighbour dossiers read (ledgers, by grep): shan-states, khmer-empire, ayutthaya-kingdom, champa, hanthawaddy-kingdom, lan-na-kingdom, sukhothai-kingdom, ngo-dynasty, plus sagaing-kingdom and kingdom-of-pinya. Not yet written (group not run, counted as exceptions): first-toungoo-empire, prome-kingdom, ai-viet, nguyen-lords, trinh-lords, konbaung-dynasty, lan-na, ming-dynasty, mughal-empire, qing-dynasty, southern-ming, yuan-dynasty, nawabs-of-bengal, british-empire, sultanate-of-bengal.

Mechanical: all four validate with --resolve (0 errors; le-dynasty keeps its Lam Sơn span warning). None of the four infoboxes gives an area, so no ratio exists; the authors say so. Page budgets (9/5/9/5) were respected; thin items are judged against them.

Verdicts: lan-xang **fail** (one blocking finding); ava-kingdom **thin**; kingdom-of-mrauk-u **thin** (one fix applied by the reviewer); le-dynasty **fix** (two fixes applied by the reviewer).

## lan-xang: fail

- **/ledger/13, /ledger/14, /ledger/15, /keyframe_review/12-14, identity.capitals[1]** (for the author): The Burmese suzerainty of 1574-1591 is encoded as losses of land: Vientiane and the middle Mekong (63 cells) are 'lost' to first-toungoo-empire in 1574-12 and the whole rest of Lan Xang in 1579-10, regained 1591, so the state has no land at all 1579-1590 and its capital Vientiane (identity.capitals 1560-1707) lies outside its own shape from December 1574.
  - Evidence: Bayinnaung page: on 6 December 1574 'The Burmese king appointed a younger brother of Setthathirath, Maha Oupahat (Chao Tha Heua), king of Lan Xang'; 'the vassal king's authority did not extend much beyond the capital'; after 1579 he 'installed Sen Soulintha ... as the successor'. Lan Xang page: 'A Burmese vassal, Chao Tha Heua, was left to administer Vientiane'; 'In 1580 Sen Soulintha returned as a Burmese vassal'; in 1591 Nokeo Koumane 'cast off any allegiance to the Toungoo Empire'. The dossier's own /ledger/14 note says 'drawn here as a tributary tint', contradicting its type 'loss'. Rule 4: vassals are a lighter tint, not a change of owner; research brief: a verdict that changes only the status (direct to vassal) keeps the shape.
  - Fix: Keep Lan Xang's full outline 1572-1590: /keyframe_review/12 correction stays the 1571 outline; /keyframe_review/13 (1575-1578) correction -> {cliopatria: Lan Xang, year: 1571} with text 'Lan Xang as a Burmese vassal'; add a new keyframe lan-xang_1579 (from 1579, to 1587, verdict adjust, correction the 1571 outline; note that Cliopatria's Toungoo shape of 1579-1587 annexes a vassal); /keyframe_review/14 correction years from 1588, not '1591-1594 only'. Delete the losses /ledger/13 and /ledger/14 and the gain /ledger/15 (keep their dates, 6 December 1574, 17 October 1579 and 1591, in the notes), or replace them with a vassal_start 1574-12 / vassal_end 1591 pair whose note says Lan Xang is the vassal; the tint itself belongs in first-toungoo-empire's ledger (vassal_start counterpart lan-xang 1574-12, vassal_end 1591).
- **/ledger/5** (applied by reviewer): contest_end 1484 at confidence 2 from the Lan Xang infobox; the Lê Thánh Tông page dates the withdrawal.
  - Evidence: Lê Thánh Tông page: 'By November 1484, Thanh Tong and his forces had withdrawn back to Dai Viet.'
  - Fix: month 11, confidence 3, source the Lê Thánh Tông page (already in sources[]), note quoting the sentence. Applied by the reviewer; validates.

Thin (for a gap-filler):
- /ledger/2, /ledger/3: the 1363 gains from khmer-empire and ngo-dynasty are confidence 1 (Cliopatria's year); the Lan Xang page puts the Khorat Plateau march after 1357 and Xam Neua undated (try https://en.wikipedia.org/wiki/Fa_Ngum)
- /keyframe_review/1-11: Muang Phuan (Xiang Khouang), inside the Lan Xang outline, was annexed by Đại Việt: the Lê Thánh Tông page says 'the Vietnamese had annexed the land back in 1448' and 'Thánh Tông made that territory a prefecture of Đại Việt in 1471'; no loss or vassal event in either dossier (try https://en.wikipedia.org/wiki/Muang_Phuan)
- /identity/rulers: no ruler list (try https://en.wikipedia.org/wiki/List_of_monarchs_of_Laos)

Spot checks:
- /ledger/0: confirmed ('In 1353 Fa Ngum was crowned'; infobox 'Founded by Fa Ngum: 1353') [https://en.wikipedia.org/wiki/Lan_Xang]
- /ledger/4: confirmed ('In fall 1479, Thánh Tông led an army of 180,000 men'; 'Luang Phabang was captured') [https://en.wikipedia.org/wiki/L%C3%AA_Th%C3%A1nh_T%C3%B4ng]
- /ledger/9: confirmed ('easily captured Vientiane on 2 January 1565'; 'left Vientiane on 1 August 1565') [https://en.wikipedia.org/wiki/Bayinnaung]
- /ledger/13: date confirmed (6 December 1574); type contradicted: the page has a vassal king appointed, not annexation [https://en.wikipedia.org/wiki/Bayinnaung]
- /ledger/14: date confirmed (17 October 1579); type contradicted: no annexation on the page, Lan Xang stays under a vassal king [https://en.wikipedia.org/wiki/Bayinnaung]
- /ledger/17: confirmed ('In 1707 Lan Xang was divided'; infobox 'Kingdom partitioned: 1707') [https://en.wikipedia.org/wiki/Lan_Xang]

Area: The Lan Xang infobox gives no area (checked); the author says so in /keyframe_review/1. Cliopatria max/at-start 375,643 km2.

## ava-kingdom: thin


Thin (for a gap-filler):
- /keyframe_review/0-4: the Toungoo district sits inside Ava's outline 1365-1501 with no gain or vassal event, while kingdom-of-pinya /ledger/5 loses it to 'Toungoo' in 1358; the author flags it ('Nothing opened dates Toungoo's return to Ava's fold'). A page dating Toungoo's submission to Ava (or a vassal tint for it) is needed (try https://en.wikipedia.org/wiki/Swa_Saw_Ke)
- /ledger/3 - /ledger/8: the Forty Years' War page has a second truce ('A second truce ran from 1403 to 1408' in the page summary); the contest 1401-1424 is drawn without a break in this dossier and in hanthawaddy-kingdom. Add contest_end 1403 / contest_start 1408 in both, or say why not (try https://en.wikipedia.org/wiki/Forty_Years%27_War)
- /notes: Ava's 1404 conquests of Kale and Mohnyin and its Shan tributaries are undated and not drawn (try https://en.wikipedia.org/wiki/Minkhaung_I)

Spot checks:
- /ledger/0: confirmed (infobox 'Kingdom of Ava founded: 26 February 1365'; text 1364, noted) [https://en.wikipedia.org/wiki/Kingdom_of_Ava]
- /ledger/1: confirmed ('began c. December 1385') [https://en.wikipedia.org/wiki/Forty_Years%27_War]
- /ledger/4: confirmed ('Ava troops overran Launggyet on 29 November 1406') [https://en.wikipedia.org/wiki/Min_Saw_Mon]
- /ledger/5: confirmed ('In 1408, Peguan forces dislodged Avan troops from Arakan') [https://en.wikipedia.org/wiki/Forty_Years%27_War]
- /ledger/7: confirmed ('Minye Kyawswa was killed in battle in March 1415') [https://en.wikipedia.org/wiki/Forty_Years%27_War]
- /ledger/11: confirmed (infobox 'Start of Shan period: 14 March 1527') [https://en.wikipedia.org/wiki/Kingdom_of_Ava]

Area: No area in the Kingdom of Ava infobox (checked). The 1527 end (Wikipedia runs Ava to 22 January 1555 under Shan-appointed kings) is a documented choice matching shan-states /ledger/7 and /ledger/11; not a fault. Cliopatria max/at-start 193,597 km2.

## kingdom-of-mrauk-u: thin

- **/ledger/17** (applied by reviewer): The 1605 Sandwip gain cites the Min Razagyi page, which has no such passage, and names Gonçalves Tibau as the counterpart although he seized Sandwip only in 1609.
  - Evidence: Min Razagyi page: no mention of 1602, 1605, 'three years' or Sandwip before the 1609 passage ('returned with 400 Portuguese and seized Sandwip'). Kingdom of Mrauk U page: 'Razagyi would take three years (1602–1605) to retake Sandwip from the Portuguese.'
  - Fix: source -> https://en.wikipedia.org/wiki/Kingdom_of_Mrauk_U (already in sources[]); counterpart -> 'Portuguese (Sandwip)'; note says which page. Applied by the reviewer; validates.

Thin (for a gap-filler):
- /keyframe_review/10: Cliopatria's 1564 shape drops 88 cells (Chin Hills and the Magwe edge; 100,283 -> 76,559 km2) with no ledger event; marked ok 'unverified' within the 9-page budget (try https://en.wikipedia.org/wiki/Min_Sekkya)
- /wars/4: Tripura tributary to Arakan from January 1575 ('agreed to pay tribute'); Mrauk U, as suzerain, should carry vassal_start counterpart twipra-kingdom with an end year; no page gave the end (try https://en.wikipedia.org/wiki/Amar_Manikya)
- /ledger/18: Sandwip lost to Tibau in 1609 has no later event; Arakan's recapture (Min Khamaung's reign) and Dilawar's hold before November 1665 are undated (try https://en.wikipedia.org/wiki/Sandwip)
- /keyframe_review/13-16: 1670-1784: no dated event on any page opened (the infobox has 'Vassal of Konbaung dynasty: 1784') (try https://en.wikipedia.org/wiki/Konbaung_conquest_of_Arakan)

Spot checks:
- /ledger/0: confirmed ('proclaimed king at Launggyet on 18 April 1429') [https://en.wikipedia.org/wiki/Min_Saw_Mon]
- /ledger/2: confirmed ('annexed Sandoway and Ramu in 1437') [https://en.wikipedia.org/wiki/Kingdom_of_Mrauk_U]
- /ledger/13: confirmed (Syriam seized 'in March 1599'; Nanda surrendered in December) [https://en.wikipedia.org/wiki/Min_Razagyi]
- /ledger/17: not on page; found on https://en.wikipedia.org/wiki/Kingdom_of_Mrauk_U ('three years (1602–1605)'); source corrected [https://en.wikipedia.org/wiki/Min_Razagyi]
- /ledger/18: confirmed (Tibao seized Sandwip in 1609) [https://en.wikipedia.org/wiki/Min_Razagyi]
- /ledger/19: confirmed year ('In 1666, it lost control of Chittagong'; infobox 'Loss of Chittagong: 1666'); the 27 January day is from the Mughal conquest page, not reopened [https://en.wikipedia.org/wiki/Kingdom_of_Mrauk_U]
- /ledger/20: confirmed (infobox 'End of kingdom: 2 January 1785') [https://en.wikipedia.org/wiki/Kingdom_of_Mrauk_U]

Area: No area in the Kingdom of Mrauk U infobox (checked). Cliopatria max/at-start 102,177 km2.

## le-dynasty: fix

- **/ledger/4, /ledger/5 (new), /wars/2/zones** (applied by reviewer): The 1479-1484 war with Lan Xang has a contest pair in lan-xang (/ledger/4-5) but none here, and the war's zones were empty although Luang Phabang was taken.
  - Evidence: Lê Thánh Tông page: 'In fall 1479, Thánh Tông led an army of 180,000 men marched westward, attacked Muang Phuan, Lan Xang and Nan'; 'Luang Phabang was captured'; 'By November 1484, Thanh Tong and his forces had withdrawn back to Dai Viet.'
  - Fix: Added contest_start 1479 and contest_end 1484-11 (counterpart lan-xang, region admin1 Louangphrabang, Laos, confidence 3, source the Lê Thánh Tông page) and the same region as the war's zone. Applied by the reviewer; validates (the only warning is the existing Lam Sơn span one).
- **/ledger/6 (was /ledger/4)** (applied by reviewer): The 1527 loss to the Mạc used Cliopatria's uncorrected Lê 1526 shape, which includes Phú Yên and Khánh Hòa that this dossier's /keyframe_review/3 keeps Cham to 1611.
  - Evidence: Champa-Đại Việt War (1471) page: annexed 'Northern Champa (now Quảng Nam, Quảng Ngãi and north of Phú Yên)', border 'moved from Hải Vân Pass to Cù Mông Pass from 1471 till 1611'.
  - Fix: region replaced by the /keyframe_review/3 correction (Lê 1475 minus Phú Yên and Khánh Hòa). Applied by the reviewer; validates.

Thin (for a gap-filler):
- /ledger/8, /ledger/9: split and dissolve of 1571 are confidence 1 (Cliopatria's row change); the Lê dynasty runs to 1789 and the author explains the cut (try https://en.wikipedia.org/wiki/Nguy%E1%BB%85n_Ho%C3%A0ng)
- /notes: Muang Phuan, annexed 1448 and a prefecture from 1471 (Lê Thánh Tông page), is not drawn here or in lan-xang (try https://en.wikipedia.org/wiki/Muang_Phuan)
- /ledger/3: the war page's infobox has the Cham remnant (Panduranga) a vassal of Đại Việt after 1471; no vassal_start (try https://en.wikipedia.org/wiki/Panduranga_(Champa))
- /identity/rulers: no ruler list (try https://en.wikipedia.org/wiki/Emperor_of_Vietnam)

Spot checks:
- /ledger/0: confirmed (infobox 'Coronation of Lê Lợi: 29 April 1428') [https://en.wikipedia.org/wiki/L%C3%AA_dynasty]
- /ledger/1: confirmed ('On November 28, 1470, a 100,000-strong Vietnamese naval expedition ... set out') [https://en.wikipedia.org/wiki/Champa%E2%80%93%C4%90%E1%BA%A1i_Vi%E1%BB%87t_War_(1471)]
- /ledger/3: confirmed ('On March 22, the city fell'; northern Champa annexed; Hải Vân to Cù Mông 1471-1611) [https://en.wikipedia.org/wiki/Champa%E2%80%93%C4%90%E1%BA%A1i_Vi%E1%BB%87t_War_(1471)]
- /ledger/6: confirmed (infobox 'Mạc Đăng Dung usurped the throne: 15 June 1527') [https://en.wikipedia.org/wiki/L%C3%AA_dynasty]
- /ledger/7: confirmed ('over the next three years all the provinces south of the Red River were captured'; 'In 1533 ... crowned at the recaptured Tây Đô castle'); confidence 2 is right, the page does not date the start [https://en.wikipedia.org/wiki/M%E1%BA%A1c_dynasty]

Area: The Lê dynasty infobox has population only (1490: 7,700,000), no area (checked). It also lists Xam Neua (1531-1540) as capital-in-exile, not in identity.capitals; harmless while the state holds no land 1527-1532. Cliopatria max/at-start 190,463 km2.

## Cross-dossier matrix

- lan-xang 1353 gain (lan-na-kingdom) -> lan-na-kingdom 1353 loss: **matched**. 
- lan-xang 1363 gain (khmer-empire) -> khmer-empire 1363 loss: **matched**. both confidence 1, Cliopatria's year
- lan-xang 1363 gain (ngo-dynasty) -> ngo-dynasty 1363 loss: **matched**. both confidence 1
- lan-xang 1479 contest_start (le-dynasty) -> le-dynasty 1479 contest_start: **matched**. mirror added by the reviewer (le-dynasty /ledger/4-5), with the 1484-11 contest_end
- lan-xang 1546 vassal_start (lan-na-kingdom) -> lan-na-kingdom 1546 rename: **mismatch**. Setthathirath's personal union 1546-1551: lan-xang tints Lan Na as its dependant, lan-na-kingdom records only a dynasty rename (1546, 1551). Same years; the two dossiers should agree on whether Lan Na is tinted
- lan-xang 1565 occupation_start (first-toungoo-empire) -> none: **exception**. first-toungoo-empire (se-01) not written yet; also 1565-08 end, 1570-02/1570-04 pair
- lan-xang 1574 loss (first-toungoo-empire) -> none: **exception**. Toungoo not written. These (and 1579 loss, 1591 gain) must become Toungoo's vassal_start counterpart lan-xang 1574-12 / vassal_end 1591 (lan-xang fail finding)
- lan-xang 1707 split (kingdom-of-luang-phrabang) -> none: **exception**. kingdom-of-luang-phrabang, vientiane, kingdom-of-champasak (se-01) not written yet
- ava-kingdom 1365 found (sagaing-kingdom) -> sagaing-kingdom 1365 dissolve: **matched**. kingdom-of-pinya dissolves to sagaing-kingdom 1364-09, consistent
- ava-kingdom 1365 found (Toungoo district) -> kingdom-of-pinya 1358 loss: **mismatch**. Pinya loses Toungoo in 1358; Ava's outline holds it from 1365 with no gain or vassal event (author flagged)
- ava-kingdom 1385 contest_start (hanthawaddy-kingdom) -> hanthawaddy-kingdom 1385 contest_start: **matched**. also 1391 end, 1401 start, 1424 end matched
- ava-kingdom 1406 occupation_start (Launggyet (Arakan)) -> none: **exception**. no dossier; launggyet-kingdom in counterparts_needing_dossiers; end 1408 matches the Forty Years' War page
- ava-kingdom 1415 occupation_start (hanthawaddy-kingdom) -> hanthawaddy-kingdom 1415 occupation_start: **matched**. end 1415-03 matched
- ava-kingdom 1482 loss (prome-kingdom) -> none: **exception**. prome-kingdom (se-01) not written yet
- ava-kingdom 1502 loss (first-toungoo-empire) -> none: **exception**. Toungoo not written; Ava infobox dates Toungoo's secession 16 October 1510 (dossier 1502 at confidence 2, explained)
- ava-kingdom 1527 loss (shan-states) -> shan-states 1527 gain: **matched**. both March 1527
- kingdom-of-mrauk-u 1437 gain (Sandoway (Thandwe)) -> none: **exception**. no dossier; listed as sandoway
- kingdom-of-mrauk-u 1459 gain (sultanate-of-bengal) -> none: **exception**. sultanate-of-bengal (sa-04) not written; also 1437 Ramu gain, 1516 loss, 1532-10 gain, 1532-12/1533-04 Dhaka occupation, and the Bengal protectorate 1429-1437 the author leaves to that dossier
- kingdom-of-mrauk-u 1546 occupation_start (first-toungoo-empire) -> none: **exception**. Toungoo not written; also 1580-09/1581-11 Thandwe and Arakan's occupations of Syriam (1599-03..1603-03) and Pegu (1599-12..1600-03); Cliopatria's Toungoo 1547 shape holds 158 Arakan cells marked wrong here
- kingdom-of-mrauk-u 1605 gain (Portuguese (Sandwip)) -> none: **exception**. no dossier; 1609 loss to Tibau likewise
- kingdom-of-mrauk-u 1666 loss (mughal-empire) -> none: **exception**. mughal-empire (sa-05) not written; Cliopatria's Mughal row should take Chittagong in 1666, not 1670
- kingdom-of-mrauk-u 1785 loss (konbaung-dynasty) -> none: **exception**. konbaung-dynasty (se-01) not written; Cliopatria's Konbaung row takes Arakan only in 1788
- le-dynasty 1428 found (ming-dynasty) -> none: **exception**. ming-dynasty (ea-07) not written; it should carry the Lam Sơn contest 1418-1427 and the 1428 loss
- le-dynasty 1471 gain (champa) -> champa 1471 loss: **matched**. contest 1470-11 / 1471-03 matched; same regions
- le-dynasty 1527 loss (ai-viet) -> none: **exception**. ai-viet (se-01) not written; also the 1533 gain
- le-dynasty 1571 split (nguyen-lords) -> none: **exception**. nguyen-lords and trinh-lords (se-01) not written

## Problems

- WebFetch returns a model summary, not page text; quotes are the summary's quotations.
- kingdom-of-mrauk-u.json changed checksum between my write and the read-back with no new mtime; its content matched my edit exactly (one ledger entry changed), so nothing was re-applied.
- lan-xang fails on one finding (vassalage drawn as annexation); the same choice affects first-toungoo-empire, which should carry vassal_start counterpart lan-xang 1574-12 / vassal_end 1591 when written.
- ava-kingdom ends 1527 (Wikipedia 1555) by a documented choice that matches shan-states; accepted, not a fault.
