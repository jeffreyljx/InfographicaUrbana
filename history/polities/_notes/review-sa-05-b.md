# Review of batch sa-05-b

Reviewer pass, 2026-10-25. Six dossiers: nayaks-of-madurai, hussain-shahi-dynasty, nayaks-of-thanjavur, sur-empire, kingdom-of-mysore, gorkha-kingdom. The machine copy is history/notes/phase-b/reviews/sa-05-b.json.

Mechanical check: all six validate under `--resolve` (0 errors, 0 warnings). I opened 16 pages (Madurai Nayak dynasty, Chanda Sahib, Thirumalai Nayak, Ghiyasuddin Mahmud Shah, Thanjavur Nayak kingdom, Sur Empire, Karrani dynasty, Mughal conquest of Bengal, Sher Shah Suri, Kingdom of Mysore, Treaty of Seringapatam, Hyder Ali, Chikka Devaraja, Unification of Nepal, Prithvi Narayan Shah, Gorkha Kingdom) and spot-checked 44 entries (43 ledger events and one keyframe). None was fabricated. One was mis-dated: Mysore's Dharwad and Bellary gain.

How the verdicts are used here: fail means at least one blocking finding remains. fix means the dossier is accepted once the findings marked 'author' are made; findings marked 'applied' I made myself. Thin items are listed for a gap-filler.

Summary: nayaks-of-madurai fix; hussain-shahi-dynasty fail (duplicate of sultanate-of-bengal); nayaks-of-thanjavur fix; sur-empire fix; kingdom-of-mysore fail (the 1772 cession to the Marathas is missing); gorkha-kingdom fix.

## nayaks-of-madurai: fix

Area: infobox None (None), Cliopatria 48150 km2, ratio None. No area in the infobox (checked); the notes say so.

Findings:
- `/ledger (after /ledger/0; and before /ledger/7)` [author]: The Vijayanagara vassalage is not mirrored: vijayanagara-empire /ledger/37 (vassal_start 1529) and /ledger/43 (vassal_end 1565) name nayaks-of-madurai, but this ledger has no vassal_start or vassal_end with vijayanagara-empire. Evidence: Madurai Nayak page: Krishnadevaraya 'made Viswanatha governor of Madurai and other Tamil provinces in 1529'; the dossier's own predecessor note says it was founded 'as a viceroyalty under the Vijayanagara Empire' and that the vijayanagara dossier records the vassalage 1529-1565. Fix: Add vassal_start 1529 (counterpart vijayanagara-empire, region {cliopatria: Nayaks of Madurai, year 1529}, confidence 2, Madurai Nayak page) and vassal_end 1565 (confidence 1, bridge matching the vijayanagara dossier).
- `/ledger/5` [author]: The 1673 Coimbatore loss to kingdom-of-mysore has no mirror: kingdom-of-mysore /ledger/4 gains Coimbatore inside a 1673 gain whose counterpart is 'Various ...'. Evidence: Cross-dossier check within this batch. Fix: No change here; kingdom-of-mysore splits Coimbatore out as a gain with counterpart nayaks-of-madurai (see that dossier).

Thin (for a gap-filler):
- `/ledger/5`: Date of the Coimbatore loss to Mysore (confidence 1 bridge at 1673). Try: https://en.wikipedia.org/wiki/Coimbatore
- `/ledger/12`: When Travancore's tribute to Madurai stopped (confidence 1 bridge at 1736). Try: https://en.wikipedia.org/wiki/Marthanda_Varma
- `/identity/rulers`: Reign gap 1601-1609 (Muttu Krishnappa). Try: https://en.wikipedia.org/wiki/Muttu_Krishnappa_Nayak

Spot checks: /ledger/0 confirmed (Madurai_Nayak_dynasty); /ledger/1 confirmed (Madurai_Nayak_dynasty); /ledger/3 confirmed (Madurai_Nayak_dynasty); /ledger/11 confirmed (Chanda_Sahib); /ledger/13 confirmed (Madurai_Nayak_dynasty); /keyframe_review/2 confirmed (Thirumalai_Nayak)

## hussain-shahi-dynasty: fail

Area: infobox None (None), Cliopatria 260980 km2, ratio None. No area on either page.

Findings:
- `/identity` [author, BLOCKING]: The dossier is a second dossier for the Sultanate of Bengal: the same state, land and events as sultanate-of-bengal (sa-04-c), so Bengal is drawn twice in 1534-1538. Evidence: Hussain Shahi page: the dynasty ruled the Sultanate of Bengal from 1494 to 1538; sultanate-of-bengal runs to 6 April 1538 and its /ledger/47-50 hold the same 1534 contest, 1537 Teliagarhi loss and 1538 contest_end and dissolve; research brief section 6: two Cliopatria rows for one state get one dossier under the earlier slug. The author flagged this. Fix: Withdraw hussain-shahi-dynasty.json from rendering (orchestrator decision; not the author's alone): sultanate-of-bengal (sa-04-c) adds 'Hussain Shahi Dynasty' to cliopatria_names and a keyframe_review entry for hussain-shahi-dynasty_1534 (covered by its own Bengal outline to April 1538; 1538-1539 belong to sur-empire's new 1538 keyframe).
- `/ledger/1` [author]: The counterpart sur-empire does not exist yet in 1534 or 1537 (sur-empire starts April 1538), so the 1534 contest_start and 1537 loss have no mirror; sultanate-of-bengal /ledger/47-48 repeat the same pairing. Evidence: sur-empire identity start {year: 1538, month: 4}; sur-empire /ledger/0 founds from sultanate-of-bengal in April 1538. Fix: Resolved with the merge: the Bengal dossier names Sher Khan's Bihar (or moves sur-empire's start) for 1534-1537.

Spot checks: /ledger/1 confirmed (Ghiyasuddin_Mahmud_Shah); /ledger/2 confirmed (Ghiyasuddin_Mahmud_Shah); /ledger/3 confirmed (Ghiyasuddin_Mahmud_Shah); /ledger/4 confirmed (Ghiyasuddin_Mahmud_Shah)

## nayaks-of-thanjavur: fix

Area: infobox None (None), Cliopatria 14694 km2, ratio None. No area in the infobox (map caption only).

Findings:
- `/ledger (after /ledger/0)` [author]: The Vijayanagara vassalage is not mirrored: vijayanagara-empire /ledger/39 (vassal_start 1534) and /ledger/44 (vassal_end 1565) name nayaks-of-thanjavur; this ledger has neither. Evidence: Thanjavur Nayak page: in 1532 Achyuta Deva Raya 'granted regional governor Sevappa Nayaka permission to establish a hereditary feudatory kingdom'. Fix: Add vassal_start 1532 (counterpart vijayanagara-empire, region {cliopatria: Nayaks of Thanjavur, year 1534}, confidence 3, Thanjavur Nayak page) and vassal_end 1565 (confidence 1 bridge). The vijayanagara dossier should move its vassal_start from 1534 to 1532.

Thin (for a gap-filler):
- `/keyframe_review/2`: No event 1572-1672 (Vallamprakara undated, end of Vijayanagara suzerainty, Bijapur pressure in the 1650s): thin by budget (1-2 pages). Try: https://en.wikipedia.org/wiki/Vijaya_Raghava_Nayak

Spot checks: /ledger/0 confirmed (Thanjavur_Nayak_kingdom); /ledger/1 confirmed (Thanjavur_Nayak_kingdom); /ledger/2 confirmed (Thanjavur_Nayak_kingdom); /ledger/3 confirmed (Thanjavur_Nayak_kingdom)

## sur-empire: fix

Area: infobox None (None), Cliopatria 1254263 km2, ratio None. Sur Empire and Sher Shah Suri pages give no area (checked).

Findings:
- `/identity/rulers` [author]: The ruler strip has gaps: nothing for 1556-1564 (the Muhammad Shahi sultans, whom the Sur page dates 1553-1563) or 1576-1593 (Qutlu Khan and Nasir Khan in Orissa), so it is not contiguous. Evidence: Sur Empire page: 'the Muhammad Shahi dynasty, which ruled Bengal from 1553 to 1563'; Mughal conquest of Bengal page: 'Qutlu Khan died and his son Nasir Khan became the ruler of Odisha'. Fix: Add the Muhammad Shahi rulers and the Orissa Afghan chiefs with the years a page gives, or end the strip and say why in notes.
- `/identity` [author]: Structural: 1557-1593 sits inside sur-empire through two renames, yet the Sur page ends the empire in 1556 and the Karrani page calls 1564-1576 'the restored Bengal Sultanate', a different state. Bengal broke away under Muhammad Shah in 1553 while the Delhi Sur line ran to 1556-1557. Evidence: Sur Empire page lead: the empire lasted 'between 1538/1540 and 1556'; Karrani page: 'ruled the restored Bengal Sultanate between 1564 and 1576'. Fix: Orchestrator decision (the author asked for it): split at 1556/1557 into an Afghan (Muhammad Shahi and Karrani) sultanate of Bengal, 1553/1557-1593, with mughal-empire's 1574-1595 counterparts renamed, or keep it as is and record why in notes.
- `/ledger (1575)` [author]: mughal-empire /ledger/40 has a vassal_start in 1575 (Treaty of Katak, Orissa) naming sur-empire. This ledger has no 1575 event: no Bengal cession and no vassalage. Evidence: Karrani page: the Battle of Tukaroi (3 March 1575) led to the Treaty of Katak, in which Daud 'ceded the whole of Bengal and Bihar, retaining only Orissa'. Fix: Either add vassal_start 1575 (counterpart mughal-empire, Orissa, confidence 2) with a vassal_end when Daud broke the treaty (1575/1576), and the Mughal side ends its vassalage then instead of 1595; or record in notes why the treaty is not drawn.

Thin (for a gap-filler):
- `/ledger/7`: Date and extent of Haibat Khan's subjugation of upper Sindh (confidence 1 at 1544). Try: https://en.wikipedia.org/wiki/Haibat_Khan_Niazi
- `/ledger/10`: Date of the Malwa loss to Baz Bahadur (confidence 1 at 1555; taken from the malwa-sultanate dossier). Try: https://en.wikipedia.org/wiki/Baz_Bahadur

Spot checks: /ledger/1 confirmed (Sur_Empire); /ledger/4 confirmed (Sur_Empire); /ledger/5 confirmed (Sur_Empire); /ledger/6 confirmed (Sher_Shah_Suri); /ledger/8 confirmed (Sher_Shah_Suri); /ledger/21 confirmed (Karrani_dynasty); /ledger/24 confirmed (Karrani_dynasty); /ledger/25 confirmed (Mughal_conquest_of_Bengal); /ledger/28 confirmed (Mughal_conquest_of_Bengal)

## kingdom-of-mysore: fail

Area: infobox 205000 (1779), Cliopatria 91042 km2, ratio 0.44. Resolved by new keyframes 1763, 1766 and 1779; the 1779 correction resolves to 837 cells, about 211,700 km2.

Findings:
- `/ledger (1772) and /keyframe_review/6` [author, BLOCKING]: Missing border move: the 1772 Maratha peace, in which Hyder ceded the north-east of the kingdom, is not in the ledger. The notes say the 1772 peace 'give[s] no territorial terms', which the cited page contradicts. Evidence: Hyder Ali page (a source of this dossier): the Marathas invaded in November 1770, took much of north-eastern Mysore and then Bangalore; in the 1772 peace Hyder agreed to 3.6 million rupees in tribute arrears and 1.4 million a year and ceded territory 'all the way to Bangalore'. Fix: Add a loss in 1772 to maratha-empire (the north-east up to Bangalore, from the page's words, confidence 2), the recovery (c. 1774-1777, confidence 1-2; the 1777 event names only Coorg and Malabar) and consider vassal_start 1772 for the annual tribute; split keyframe 6 at 1772.
- `/ledger/10 and /keyframe_review/6` [author]: Mis-dated land: Dharwad and Bellary (Hubballi 70 km and Ballari 80 km, about 35,000 km2) are gained in 1766 and drawn from 1766, but the page gives no year and the Hyder Ali page places the capture of Dharwad in the 1776-1779 conflicts. Evidence: Kingdom of Mysore page: he 'extended the Mysore kingdom up to Dharwad and Bellary in the north' (no year). Hyder Ali page: he extended his domain to the Krishna River after a lengthy siege of Dharwad in 1776-1779. Fix: Move the gain to 1778 (confidence 1-2), drop the two circles from keyframe 6 (1766-1778) and let keyframe 7 (1779) carry them. Reviewer lowered /ledger/10 from confidence 2 to 1 (applied); the date and keyframe remain.
- `/ledger/10` [applied]: Confidence 2 for a year the page does not give. Evidence: Kingdom of Mysore page: no year for Dharwad and Bellary. Fix: Confidence 2 -> 1 (applied by reviewer; dossier re-validated).
- `/ledger/15` [author]: The region given to the Marathas in 1792 (Hubballi 70 km plus Ballari 80 km, bbox down to 14.51 N) takes in Ballari and the country south of the Tungabhadra, but the treaty gives the Peshwa land only 'up to the Tungabhadra River'. It was also at confidence 3 for places the page does not name. Evidence: Treaty of Seringapatam page: 'The Peshwa acquired territory up to the Tungabhadra River'; Bellary and Dharwad are not named. Ballari (15.14 N) lies south of the river. Fix: Limit the region to the land north and west of the Tungabhadra (the Hubballi-Dharwad country), keep Ballari with Mysore until 1799 and give its 1799 fate from a page. Reviewer lowered confidence from 3 to 2 (applied); the region fix remains.
- `/ledger/15` [applied]: Confidence 3 with regions the page does not name. Evidence: Treaty of Seringapatam page names only the Tungabhadra. Fix: Confidence 3 -> 2 (applied by reviewer; dossier re-validated).
- `/ledger/0 and /keyframe_review/0` [author]: 1399-1571: Mysore is drawn as its own state inside Vijayanagara with no vassalage on either side. The vijayanagara-empire ledger loses the Mysore country only in 1572 (/ledger/49) and has no event in 1399. Evidence: Wadiyar page (cited in /ledger/0): Yaduraya was 'made prefect of Mysore' under Harihara II of Vijayanagara in 1399; the notes say the Wodeyars paid tribute to Chandragiri until 1612-13. Fix: Add vassal_start 1399 (counterpart vijayanagara-empire) and vassal_end 1572 (or 1612-13 if a page dates it); vijayanagara-empire mirrors them.
- `/ledger/4` [author]: The 1673 gain counterpart 'Various (... Coimbatore)' hides the Coimbatore part, which nayaks-of-madurai /ledger/5 loses to kingdom-of-mysore in 1673. Evidence: Cross-dossier check within this batch. Fix: Split out a gain of Coimbatore (place Coimbatore 50 km, confidence 1, 1673) with counterpart nayaks-of-madurai; leave the rest as 'Various'.
- `/ledger (1700)` [author]: The 1700 subordination to the Mughals is on a page opened but not in the ledger. Evidence: Chikka Devaraja page: the 1700 embassy to Aurangzeb brought 'a formal subordination to Mughal authority and a requirement to pay annual tribute'. Fix: Add vassal_start 1700 (counterpart mughal-empire, confidence 2) with an end the pages support, or say in notes why it is not drawn.

Thin (for a gap-filler):
- `/ledger/1`: Independence on the core (confidence 1 at 1572). Try: https://en.wikipedia.org/wiki/Timmaraja_Wodeyar_II
- `/ledger/4`: Dates and former holders of Chikka Devaraja's conquests (confidence 1 at 1673). Try: https://en.wikipedia.org/wiki/Chikka_Devaraja
- `/ledger/13`: When Dindigul, the Baramahal, Cuddapah, Kurnool and Anantapur were taken (confidence 1 at 1779). Try: https://en.wikipedia.org/wiki/Second_Anglo-Mysore_War
- `/identity/rulers`: No ruler strip. Try: https://en.wikipedia.org/wiki/Wadiyar_dynasty

Spot checks: /ledger/5 confirmed (Chikka_Devaraja); /ledger/6 confirmed (Chikka_Devaraja); /ledger/8 confirmed (Hyder_Ali); /ledger/9 confirmed (Hyder_Ali); /ledger/10 mis-dated (Kingdom_of_Mysore); /ledger/11 confirmed (Hyder_Ali); /ledger/12 confirmed (Kingdom_of_Mysore); /ledger/15 confirmed (Treaty_of_Seringapatam); /ledger/16 confirmed (Treaty_of_Seringapatam); /ledger/17 confirmed (Treaty_of_Seringapatam); /ledger/22 confirmed (Kingdom_of_Mysore); /ledger/25 confirmed (Kingdom_of_Mysore)

## gorkha-kingdom: fix

Area: infobox None (None), Cliopatria 148032 km2, ratio None. No area on the page; all Cliopatria shapes (modern Nepal) marked wrong and replaced by the hill core.

Findings:
- `/ledger/11` [author]: The dissolve region (all of Bagmati and Narayani plus Gorkha) hands nepal more than Gorkha held on 25 September 1768. Lalitpur fell in October 1768 and Bhaktapur in November 1769, and the last keyframe (1762-1768) is only circles. nepal /ledger/2 founds on the same union. Evidence: Prithvi Narayan Shah page, campaign table: Conquest of Lalitpur 'October 1768', Conquest of Bhaktapur 'November 1769'. Fix: Make the dissolve region the keyframe 7 correction plus Kathmandu 12 km; the nepal dossier's found should match (route to sa-05-f).
- `/ledger/3` [author]: The contest_start (1757, the valley) disagrees with kathmandu /ledger/4 (contest_start 26 September 1744, Nuwakot) by 13 years and on the zone. Evidence: Unification of Nepal page: Nuwakot taken 26 September 1744; 'In 1757, The Gorkhalis set up a base on Naikap to mount their assault on Kirtipur'. Fix: Agree one reading with kathmandu (sa-04): either kathmandu starts its contest in 1757 and keeps Nuwakot 1744 as a plain loss (as here), or this ledger adds a 1744 contest pair over Nuwakot.
- `/notes` [author]: The notes say no page dates any growth before 1744, but the Gorkha Kingdom page has expansion from the 1730s. Evidence: Gorkha Kingdom page: 'From the 1730s, the Gorkha Kingdom began expanding under King Nara Bhupal Shah' (no places). Fix: Say so in notes (no region can be drawn from it).

Spot checks: /ledger/0 confirmed (Gorkha_Kingdom); /ledger/1 confirmed (Unification_of_Nepal); /ledger/2 confirmed (Unification_of_Nepal); /ledger/4 confirmed (Unification_of_Nepal); /ledger/5 confirmed (Unification_of_Nepal); /ledger/6 confirmed (Unification_of_Nepal); /ledger/7 confirmed (Prithvi_Narayan_Shah); /ledger/8 confirmed (Prithvi_Narayan_Shah); /ledger/11 confirmed (Unification_of_Nepal)

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| nayaks-of-madurai 1529 found (vijayanagara-empire) | vijayanagara-empire 1529 vassal_start | mismatch | vijayanagara records vassal_start 1529 and vassal_end 1565 for Madurai; Madurai records neither (fix listed in nayaks-of-madurai). |
| nayaks-of-madurai 1635 vassal_start (Travancore (Venad)) | -   | exception | travancore.json (sa-05-x) starts 1729; Venad before 1729 has no dossier (listed by the author). |
| nayaks-of-madurai 1673 occupation_start (nayaks-of-thanjavur) | nayaks-of-thanjavur 1673 occupation_start | matched |  |
| nayaks-of-madurai 1673 loss (kingdom-of-mysore) | kingdom-of-mysore 1673 gain | mismatch | Mysore /ledger/4 gains Coimbatore in 1673 but names counterpart "Various ..."; fix listed in kingdom-of-mysore. |
| nayaks-of-madurai 1675 occupation_end (nayaks-of-thanjavur) | nayaks-of-thanjavur 1675 occupation_end | matched |  |
| nayaks-of-madurai 1734 contest_start (carnatic-sultanate) | carnatic-sultanate 1734 contest_start | matched |  |
| nayaks-of-madurai 1736 contest_end (carnatic-sultanate) | carnatic-sultanate 1736 contest_end | matched |  |
| nayaks-of-madurai 1736 loss (carnatic-sultanate) | carnatic-sultanate 1736 gain | matched |  |
| nayaks-of-madurai 1736 vassal_end (Travancore (Venad)) | -   | exception | as 1635. |
| nayaks-of-madurai 1736 dissolve (carnatic-sultanate) | carnatic-sultanate 1736 gain | matched |  |
| hussain-shahi-dynasty 1534 found (sultanate-of-bengal) | sultanate-of-bengal   | mismatch | Same state as sultanate-of-bengal (which runs to April 1538 over the same land): duplicate dossier, merge recommended. |
| hussain-shahi-dynasty 1534 contest_start (sur-empire) | sur-empire   | mismatch | sur-empire starts April 1538; sultanate-of-bengal /ledger/47 makes the same 1534 pairing. Resolved by the merge (and a sur-empire start or counterpart decision for 1534-1537). |
| hussain-shahi-dynasty 1537 loss (sur-empire) | sur-empire   | mismatch | As above; sultanate-of-bengal /ledger/48 has the same 1537 loss to sur-empire, which has no 1537 gain (it founds with Bihar and Bengal in April 1538). |
| hussain-shahi-dynasty 1538 dissolve (sur-empire) | sur-empire 1538 found | matched | sur-empire /ledger/0 founds from sultanate-of-bengal (not from hussain-shahi-dynasty) on 6 April 1538. |
| nayaks-of-thanjavur 1532 found (vijayanagara-empire) | vijayanagara-empire 1534 vassal_start | mismatch | Two years apart, and Thanjavur records no vassal_start or vassal_end (vijayanagara has 1534 and 1565). Thanjavur page: feudatory kingdom 1532. |
| nayaks-of-thanjavur 1673 occupation_start (nayaks-of-madurai) | nayaks-of-madurai 1673 occupation_start | matched |  |
| nayaks-of-thanjavur 1675 occupation_end (nayaks-of-madurai) | nayaks-of-madurai 1675 occupation_end | matched |  |
| nayaks-of-thanjavur 1675 loss (thanjavur-maratha-kingdom) | thanjavur-maratha-kingdom 1676 found | matched | Venkoji takes Thanjavur in 1675 and assumes sovereignty in early 1676. |
| sur-empire 1538 found (sultanate-of-bengal) | sultanate-of-bengal 1538 dissolve | matched | 6 April 1538 on both sides. |
| sur-empire 1538 contest_start (mughal-empire) | mughal-empire 1539 contest_start | matched | Sur September 1538 (Humayun at Gauda), Mughal June 1539 (Chausa): nine months apart. |
| sur-empire 1540 gain (mughal-empire) | mughal-empire 1540 loss | matched | Hindustan, 17 May 1540. |
| sur-empire 1540 gain (mughal-empire) | mughal-empire 1540 loss | matched | Punjab: Sur November 1540 (Lahore), Mughal July 1540. |
| sur-empire 1541 gain (Multan (holder not named on the page)) | -   | exception | Listed by the author. langah-sultanate ends 1528 and its note says Multan merged into the Mughal Empire in 1530 and Sher Shah took it in 1541, so the counterpart may be mughal-empire. |
| sur-empire 1542 gain (malwa-sultanate) | malwa-sultanate 1542 loss | matched |  |
| sur-empire 1544 gain (Upper Sindh (rulers not named on the page)) | -   | exception | Listed by the author. |
| sur-empire 1544 occupation_start (kingdom-of-marwar) | kingdom-of-marwar 1544 occupation_start | matched |  |
| sur-empire 1545 occupation_end (kingdom-of-marwar) | kingdom-of-marwar 1545 occupation_end | matched |  |
| sur-empire 1555 loss (malwa-sultanate) | malwa-sultanate 1555 gain | matched |  |
| sur-empire 1555 loss (mughal-empire) | mughal-empire 1555 gain | matched | Punjab and Delhi; Sur February-June 1555, Mughal July 1555. |
| sur-empire 1556 gain (mughal-empire) | mughal-empire   | missing | Hemu takes Delhi and Agra on 7 October 1556 (Second Panipat page); mughal-empire has no October 1556 loss, only the November 1556 regain. Route to the mughal-empire author (sa-05). |
| sur-empire 1556 loss (mughal-empire) | mughal-empire 1556 gain | matched | 5 November 1556. |
| sur-empire 1568 gain (Orissa (holder not named on the page)) | -   | exception | Listed by the author. |
| sur-empire 1574 loss (mughal-empire) | mughal-empire 1574 gain | matched | Patna; Sur also loses Tanda (40 km) in September 1574, which the Mughal 1574 gain (Patna 120 km) does not cover: small land mismatch. |
| sur-empire 1576 loss (mughal-empire) | mughal-empire 1576 gain | matched | Bengal at Rajmahal. |
| mughal-empire 1575 vassal_start (sur-empire) | sur-empire   | missing | Treaty of Katak (Karrani page: Daud ceded Bengal and Bihar, retaining only Orissa). Neither side agrees: Mughal vassalage 1575-1595 against Sur independence to 1593. Fix listed in sur-empire. |
| sur-empire 1592 contest_start (mughal-empire) | mughal-empire   | missing | Man Singh campaign, April 1590 to 1593 (Mughal conquest of Bengal page); mughal-empire has no contest. |
| sur-empire 1593 loss (mughal-empire) | mughal-empire 1595 gain | mismatch | Two years apart. Mughal conquest of Bengal page: Man Singh conquered Odisha the year after April 1592 and returned to Bihar in 1593; the Mughal 1595 (confidence 1, Cliopatria) should move to 1593, with its vassal_end. |
| kingdom-of-mysore 1399 found (vijayanagara-empire) | vijayanagara-empire   | missing | No vassalage 1399-1572 on either side; fix listed in kingdom-of-mysore. |
| kingdom-of-mysore 1572 gain (vijayanagara-empire) | vijayanagara-empire 1572 loss | matched | Land differs: vijayanagara gives the whole 1572 shape including Srirangapatna, which Mysore takes only in 1610. |
| kingdom-of-mysore 1610 gain (vijayanagara-empire) | vijayanagara-empire   | missing | vijayanagara-empire (life to 1646) has no 1610 loss of Srirangapatna. Route to sa-04. |
| kingdom-of-mysore 1673 gain (Various (... Coimbatore)) | nayaks-of-madurai 1673 loss | mismatch | The Coimbatore part should name nayaks-of-madurai. |
| kingdom-of-mysore 1687 gain (mughal-empire) | mughal-empire   | missing | Bangalore; the Chikka Devaraja page has the Mughals sealing the sale in 1687. mughal-empire has no event. Route to sa-05. |
| kingdom-of-mysore 1763 gain (Nayakas of Keladi) | -   | exception | No dossier; listed by the author. |
| kingdom-of-mysore 1766 gain (Zamorin of Kozhikode) | -   | exception | No dossier; listed by the author. |
| kingdom-of-mysore 1769 gain (british-empire) | -   | exception | british-empire (sa-06) not written yet. The Hyder Ali page does not say who held Karur before. |
| kingdom-of-mysore 1777 gain (maratha-empire) | maratha-empire   | missing | maratha-empire has no Mysore event in 1770-1792, though the Hyder Ali page has the Maratha conquest of north-eastern Mysore in 1770-1772. |
| kingdom-of-mysore 1792 loss (maratha-empire) | maratha-empire   | missing | Treaty of Seringapatam: the Peshwa acquired territory up to the Tungabhadra. maratha-empire has no 1792 gain. Route to sa-05. |
| kingdom-of-mysore 1792 loss (hyderabad-state) | hyderabad-state 1792 gain | matched |  |
| kingdom-of-mysore 1792 loss (british-empire) | -   | exception | british-empire (sa-06) not written yet. |
| kingdom-of-mysore 1792 loss (Coorg (Kodagu) under its rajah) | -   | exception | No dossier; listed by the author. |
| kingdom-of-mysore 1799 loss (british-empire) | -   | exception | british-empire (sa-06) not written yet. |
| kingdom-of-mysore 1947 dissolve (republic-of-india) | -   | exception | republic-of-india not written yet. |
| gorkha-kingdom 1559 found (Mansingh Khadka Magar (Gorkhakot)) | -   | exception | A local chief; no dossier needed. |
| gorkha-kingdom 1744 gain (kathmandu) | kathmandu 1744 loss | matched | Nuwakot, 26 September 1744. |
| gorkha-kingdom 1754 gain (Dolakha and the hill principalities) | -   | exception | Listed by the author (sa-05-f). |
| gorkha-kingdom 1757 contest_start (kathmandu) | kathmandu 1744 contest_start | mismatch | 13 years apart and different zones (valley against Nuwakot). |
| gorkha-kingdom 1759 gain (kathmandu) | kathmandu   | missing | Shivapuri; kathmandu has no 1759 loss. Route to sa-04. |
| gorkha-kingdom 1762 gain (Makwanpur (Sen dynasty)) | -   | exception | Listed by the author. |
| gorkha-kingdom 1763 gain (Nepal Valley city-states (Lalitpur and Bhaktapur)) | -   | exception | Listed by the author. |
| gorkha-kingdom 1768 gain (kathmandu) | kathmandu 1768 dissolve | matched | 25 September 1768. |
| gorkha-kingdom 1768 dissolve (nepal) | nepal 1768 found | matched | Same date; land overreaches on both sides (all of Bagmati and Narayani). Fix listed in gorkha-kingdom. |

## Problems

- hussain-shahi-dynasty duplicates sultanate-of-bengal (sa-04-c): the merge needs the orchestrator and the sa-04-c owner, not this author alone.
- sur-empire 1557-1593 (Muhammad Shahi and Karrani Bengal, Orissa Afghans) needs an orchestrator decision: keep as renames or split at 1556/1557.
- kingdom-of-mysore runs to 1947 past Cliopatria's 1799; british-empire and republic-of-india dossiers do not exist yet, so the 1769-1799 and 1947 pairings are unchecked.
- Missing mirrors in other groups' dossiers: mughal-empire (October 1556 Hemu loss, 1590-1593 Orissa contest, 1687 Bangalore, Orissa 1595 to 1593), maratha-empire (Mysore 1770-1772, 1777, 1792), vijayanagara-empire (Mysore vassalage 1399-1572, Srirangapatna 1610, Thanjavur vassal_start 1534 to 1532), kathmandu (contest start 1744 against 1757, Shivapuri 1759), nepal (found region).
- Reviewer edits: kingdom-of-mysore /ledger/10 confidence 2 to 1 and /ledger/15 confidence 3 to 2, re-validated (0 errors, 0 warnings). No other dossier was edited.
- No page failed to load. No infobox area exists for five of the six states (checked on each article); only kingdom-of-mysore has one (205,000 km2 for 1779).
