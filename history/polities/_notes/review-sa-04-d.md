# Review of batch sa-04-d (Deccan sultanates)

Reviewer, 2026-10-19. Machine copy: history/notes/phase-b/reviews/sa-04-d.json.

The validator gave 0 errors on all five dossiers. The only --resolve warnings are unknown places: Junnar, Janjira, Karwar, Gandikota. I opened 11 pages and confirmed events on them. I applied small fixes in place (marked APPLIED below) and re-validated. Findings marked OPEN are for the author.

## Verdicts

- ahmadnagar-sultanate: **fix**
- berar-sultanate: **fix**
- bidar-sultanate: **thin**
- bijapur-sultanate: **fail**
- golconda-sultanate: **fail**

## ahmadnagar-sultanate (fix)

Area: infobox None (year None), Cliopatria 152720.9, ratio None. No area on the Ahmadnagar page (checked). The author says so in the notes.

Findings:

- APPLIED `/ledger/5/region`: The 1561 return of Kaliyani was drawn as an 80 km circle around Bidar, which takes in the Barid Shahi capital and most of the Bidar heartland, not Kaliyani.
  - Evidence: Adil Shahi dynasty page: 'Hussain sued for peace in 1561, submitting to Rama Raya and returning Kaliyani to Ali Adil Shah'. The page names Kaliyani only, and the region's own text says 'Kaliyani (Basavakalyan), 55 km west of Bidar'.
  - Fix: region = {lon 76.95, lat 17.87, km 25, text unchanged} (Basavakalyan). The mirror bijapur-sultanate /ledger/11 got the same change.
- OPEN `/identity/capitals/4`: Aurangabad (Khirki) is the capital to 1636, but the dossier's own /ledger/13 gives the Daulatabad region (60 km, which contains Aurangabad 13 km away) to the Mughals in 1633.
  - Evidence: Ahmadnagar infobox: 'Aurangabad (1610–1636)'. Ahmadnagar page: 'Fath Khan surrendered to the Mughals in the siege of Daulatabad in 1633'. Shahaji page: Shahaji 'resided in Junnar while raising his army' and 'set up his capital at Shahabad' (undated). A capital outside the state's land is not plausible.
  - Fix: End Aurangabad in 1633. For 1633-1636 add the remnant's seat if a page gives one, or leave a note that the infobox years conflict with the 1633 loss. Also note that Junnar 1610 and Aurangabad from 1610 overlap in 1610.
- OPEN `/keyframe_review/8`: Verdict ok, but the note admits the 1600-1618 shape still contains Ahmadnagar fort and town, which the Mughals took on 18 August 1600; /ledger/11's region also leaves the fort out although its note says it fell.
  - Evidence: Chand Bibi page: 'Ahmednagar was captured by the Mughal forces of Daniyal and Mirza Yusuf Khan on 18 August 1600.' Malik Ambar page: he 'had captured Ahmednagar Fort and town from the Mughals' and later 'had to surrender the fort of Ahmadnagar' (both undated).
  - Fix: Mark the keyframe adjust: minus Ahmednagar (about 25 km) from August 1600 until a dated recapture. Put the town in /ledger/11's region. A gap-filler should find the years of Malik Ambar's recapture and of its loss (see thin).

Gaps (thin):

- `/ledger/2`: The c. 1540 loss of two Konkan coastal cells to the Portuguese is confidence 1. portuguese-empire /ledger/16 has the same coast (Mumbai 60 km: Salsette, Bombay, Chaul, Bassein) as a 1534 gain from the Gujarat Sultanate, so the holder and the year disagree. Page to try: https://en.wikipedia.org/wiki/Treaty_of_Bassein_(1534)
- `/ledger/3`: The Solapur-Naldurg strip, gained c. 1547 and lost c. 1552, is confidence 1. Its years come from Cliopatria. Page to try: https://en.wikipedia.org/wiki/Burhan_Nizam_Shah_I
- `/keyframe_review/8`: Years of Malik Ambar's recapture of Ahmadnagar fort and of its surrender back to the Mughals. Page to try: https://en.wikipedia.org/wiki/Ahmednagar_Fort
- `/ledger/15`: The line of the 1636 partition between the Mughals and Bijapur. The whole remnant goes to the Mughals at confidence 2, yet /identity/successors names Bijapur, and no event gives Bijapur its share. The Shahaji page says the Mughals got 'a major part of present-day Maharashtra, including Pune and Indapur', while Shahaji kept his Pune jagir in Bijapur service. Page to try: https://en.wikipedia.org/wiki/Muhammad_Adil_Shah

Spot checks:

- `/ledger/0` (Ahmadnagar_Sultanate): confirmed: 'On 28 May 1490, Ahmad declared independence'
- `/ledger/6` (Ahmadnagar_Sultanate): confirmed: 'Murtaza Shah annexed Berar in 1574'
- `/ledger/9` (Chand_Bibi): confirmed: 'On 23 February 1596, she decided to make peace by ceding Berar to Murad'. The siege began November 1595 (/ledger/7).
- `/ledger/11` (Chand_Bibi): confirmed (date): 18 August 1600. The land is the author's reading at confidence 2, but the region leaves out the fort the note says fell.
- `/ledger/13` (Ahmadnagar_Sultanate): confirmed: 'Fath Khan surrendered to the Mughals in the siege of Daulatabad in 1633'
- `/ledger/14` (Shahaji): confirmed: 'In October 1636, Shahaji surrendered Mahuli and Junnar to the Mughals'
- `/ledger/5` (Adil_Shahi_dynasty): confirmed (1561, Kaliyani). The region was wrong and has been fixed.

## berar-sultanate (fix)

Area: infobox 29340 (year None), Cliopatria 80056.2, ratio 2.73. The infobox gives 29,340 km2 with no year. The author acknowledges the gap in /keyframe_review/0-1 and in notes, and keeps the shape as the Bahmani taraf of Berar with Mahur. That is accepted: the page has no boundary, and the British province of Berar alone was about 46,000 km2.

Findings:

- APPLIED `/identity/rulers/3/to`: Burhan Imad Shah ran to 1574 and overlapped Tufail Khan (1568-1574), so the rulers were not contiguous.
  - Evidence: Berar page rulers table: Burhan Imad Shah '1562 – 1574 (de facto 1562 – 1568)'; 'Tufail Khan (usurper): 1568 – 1574'.
  - Fix: to = 1568. His note already records the de jure years.

Spot checks:

- `/ledger/0` (Berar_Sultanate): confirmed: Fathullah Imad-ul-Mulk 'proclaimed his independence amidst the civil unrest in the Bahmani Sultanate', 1490 (rulers table 1490-1504)
- `/ledger/1` (Berar_Sultanate): confirmed: 'annex Berar into his own dominions of the Ahmadnagar Sultanate in 1574'; infobox 'Conquered by the Ahmednagar Sultanate: 1574'
- `/ledger/2` (Berar_Sultanate): confirmed (same sentence)
- `/identity/capitals/0` (Berar_Sultanate): confirmed: 'had its capital at Ellichpur'

## bidar-sultanate (thin)

Area: infobox None (year None), Cliopatria 63693.2, ratio None. No area on the page (checked).

Findings:

- APPLIED `/identity/rulers/0/from`: Qasim Barid I started in 1489, before the state's start (1492). Rulers must fall inside the life.
  - Evidence: Bidar page: 'The sultanate was founded in 1492 by' Qasim Barid I; infobox 'Established 1492'.
  - Fix: from = 1492. His note keeps the table's 1489.

Gaps (thin):

- `/ledger/1`: The 1518-1519 loss of the eastern (Telangana) lands to Golconda is confidence 1 and moves 58 percent of the state's area. No page says which Bahmani province went to whom. The Bidar page says only that 'the sultanate's initial territory corresponded to that of one of the five provinces of the Bahmani Sultanate', which argues against Telangana being in Bidar's 1492 shape at all. Page to try: https://en.wikipedia.org/wiki/Qasim_Barid_I
- `/ledger/2`: The 1521 southern gain (21 cells) is confidence 1, and its counterpart is given only as vijayanagara-empire, though 6 of the cells come from Bijapur's 1520 shape and Bijapur has no matching loss. Page to try: https://en.wikipedia.org/wiki/Amir_Barid_I

Spot checks:

- `/ledger/0` (Bidar_Sultanate): confirmed: founded 1492 by Qasim Barid I; infobox 1492-1619
- `/ledger/3` (Bidar_Sultanate): confirmed: 'When the last Bahmani ruler Kalimullah fled to Bidar in 1527', Amir Barid 'became practically independent'
- `/ledger/4` (Bidar_Sultanate): confirmed: 1542, Ali Barid Shah I 'the first to assume the royal title of Shah'
- `/ledger/5` (Bidar_Sultanate): confirmed: 1619, 'Bidar was annexed to Bijapur sultanate'

## bijapur-sultanate (fail)

Area: infobox None (year None), Cliopatria 396482.8, ratio None. No area on the Adil Shahi page (checked). The internal factor of 8.5 between the 1662 (338k) and 1670 (39.6k) Cliopatria shapes is acknowledged and corrected, but the correction over-retains the Carnatic (see fixes).

Findings:

- OPEN `/ledger (1636)`: There is no vassal_start for Bijapur's 1636 submission to the Mughals. The author files it only as an event the Mughal dossier should carry.
  - Evidence: Adil Shahi dynasty page (in sources): 'In 1636, Bijapur signed a treaty agreeing to pay tribute to the Mughal emperor and acknowledge Mughal authority.' A vassal_start must appear in both ledgers.
  - Fix: Add {year 1636, type vassal_start, counterpart mughal-empire, region the 1619 shape, confidence 3, source Adil Shahi page}. End it with a vassal_end (the 1657 war, or Jai Singh's campaign of 1665-66, if a page dates it), or let the 1686 dissolve close it, and say which.
- OPEN `/keyframe_review/15/correction`: The 1677-1686 corrections keep the whole Carnatic of the 1662 shape (Bangalore, Kolar, Hoskote, Sira, the Tamil country beyond the Vellore and Gingee circles) for Bijapur until 1686. The two pages the author cites say otherwise, and nothing in the ledger loses Bangalore, which was gained in 1638.
  - Evidence: Shivaji page: Shivaji defeated Venkoji's army on 26 November 1677 and 'seized most of his possessions on the Mysore plateau' (Venkoji held Shahaji's Bijapur jagir of Bangalore, Kolar, Hoskote and Sira: Shahaji page). Adil Shahi page: Shivaji 'undid almost all the southern Bijapuri conquests over the following years.' The keyframe note says the post-1677 holdings are 'not described by any page opened'; they are, in outline.
  - Fix: Add a loss of the Bangalore-Kolar-Hoskote plateau (Bengaluru about 80 km), either to maratha-empire in November 1677 or to thanjavur-maratha-kingdom in 1676 if Venkoji's jagir is taken as leaving Bijapur when he made himself king at Thanjavur. Subtract it in the 1677 and 1683 corrections. Then restate what Bijapur held 1677-1686 (the Raichur Doab, Adoni, Bankapur and Dharwar side, Belgaum, Gulbarga) from a page, not as the 1662 shape minus four circles.
- OPEN `/ledger/31/region`: The 1686 loss and dissolve (/ledger/32) use Cliopatria's 1686 shape (39,924 km2), but the dossier's own correction for 1683-1686 is the 1662 shape minus the 1675-1677 losses, roughly 300,000 km2. Most of the corrected land therefore has no closing event and never passes to the Mughals.
  - Evidence: /keyframe_review/16 correction: 'the 1662 shape minus the lands Shivaji took in 1675 and 1677'; /ledger/31 region: {cliopatria Bijapur Sultanate 1686}.
  - Fix: Once the 1677-1686 correction is settled, use the corrected 1683 shape as the region of /ledger/31 and /ledger/32.
- OPEN `/keyframe_review/7`: Keyframes 7 (1619-1639) and 8 (1640-1652) are marked ok, but the ledger adds land outside them: Bangalore (December 1638, 50 km), Vellore (1641, 60 km) and Gingee (1648, 80 km), about 39,000 km2. The 1653 note itself says these cells 'match Shahaji's conquests of 1638-1648, not 1653'. Keyframe 8 also holds the Nellore coast, which Golconda took in April 1642.
  - Evidence: Shahaji page: 'In December 1638, the Bijapur forces seized Bangalore'; 1641 Vellore. Mir Jumla II page: 'In April 1642 ... Reaching Nellore plains unopposed he captured eight forts'. The reviewer rule says an event with no trace in the keyframes is fine only if it is small or the keyframe is marked adjust.
  - Fix: Mark keyframes 7 and 8 adjust. Add the Bangalore-Kolar-Hoskote-Sira jagir from December 1638 (new keyframes at 1638/1641/1648, or a correction that names the dates), and subtract the Nellore coast from 1642 so that Bijapur and Golconda do not overlap.
- OPEN `/keyframe_review/2`: Verdict ok, though the note quotes the page calling Raichur 'the Bijapuri fort of Raichur' in 1520 while the 1512-1520 shape leaves the Doab out. /ledger/5 then loses a Raichur that the keyframe never held.
  - Evidence: Adil Shahi page: Krishnadevaraya 'laid siege to the Bijapuri fort of Raichur in 1520'.
  - Fix: Mark it adjust and add Raichur and Mudgal (Raichur 60 km) for 1512-1520, so the 1520 loss removes something.
- APPLIED `/ledger/26/region`: The April 1675 loss of Ponda was drawn as all of admin1 Goa, which includes the Portuguese Old Conquests that Bijapur had not held since 1510.
  - Evidence: Shivaji page: 'capturing the Bijapuri forts of Ponda (April 1675), Karwar (mid-year), and Kolhapur (July)'.
  - Fix: region = {lon 74.01, lat 15.40, km 15, text unchanged}, with the same change to the Ponda term inside /keyframe_review/14, /15 and /16.
- APPLIED `/ledger/11/region`: The 1561 gain of Kaliyani was drawn as an 80 km circle around Bidar, which paints the Barid Shahi capital as Bijapur's from 1561.
  - Evidence: Adil Shahi page: 'returning Kaliyani to Ali Adil Shah' (1561).
  - Fix: region = {lon 76.95, lat 17.87, km 25} (Basavakalyan), mirroring ahmadnagar-sultanate /ledger/5.
- APPLIED `/ledger/18/confidence`: Gingee (1648) was at confidence 3, but its region is an 80 km circle around Puducherry, a place the page does not name.
  - Evidence: Mir Jumla II page: 'in 1648, Gingee fell to the Adil Shahis'. The year and the fort are the page's; the drawn region is the researcher's.
  - Fix: confidence = 2 (or a {lon 79.42, lat 12.25, km 50} Gingee circle, kept at 3).
- OPEN `/ledger/16/counterpart`: Bangalore is taken from vijayanagara-empire, but the page names Kempe Gowda III's territories.
  - Evidence: Shahaji page: Shahaji received Bangalore 'after Bijapur's invasion of Kempe Gowda III's territories'.
  - Fix: counterpart 'Kempe Gowda III (Yelahanka Nayakas)', listed under counterparts_needing_dossiers, or keep vijayanagara-empire with a note that the Gowdas were its vassals.
- OPEN `/keyframe_review/6`: The 1572 keyframe's correction text says the shape 'holds from 1575' and the note says '1572-1574 is the 1552 shape', but no keyframe for 1572-1574 was added, so nothing in the keyframes encodes it.
  - Evidence: Adil Shahi page: the Carnatic campaign 'lasted until 1575'. Compare the 1657 and 1675 keyframes, which were added for the same kind of shift.
  - Fix: Add a bijapur-sultanate_1572 keyframe for 1572-1574 (the 1552 correction), or date the gain within the campaign and say so.

Gaps (thin):

- `/ledger/8`: The 1547 gain of Kanara cells from Vijayanagara and the 1547/1552 Solapur exchange with Ahmadnagar are confidence 1. Page to try: https://en.wikipedia.org/wiki/Ibrahim_Adil_Shah_I
- `/ledger (1636)`: Bijapur's share of the 1636 partition of Ahmadnagar. The page says only that it 'was partitioned between the two states'. ahmadnagar-sultanate /identity/successors names Bijapur, but no event gives Bijapur the share. Page to try: https://en.wikipedia.org/wiki/Muhammad_Adil_Shah
- `/ledger (1563)`: The 1563 cession of Yadgir and Bagalkote, noted by the author but not entered. Page to try: https://en.wikipedia.org/wiki/Ali_Adil_Shah_I
- `/ledger/6`: The 1530 recapture of Raichur and Mudgal is the author's reading of 'the following year, after the death of Krishnadevaraya' (the page's previous date is 1520). It is fine at confidence 2 but should be confirmed. Page to try: https://en.wikipedia.org/wiki/Ismail_Adil_Shah

Spot checks:

- `/ledger/4` (Adil_Shahi_dynasty): confirmed: the Portuguese 'again conquered it in November of that year' (1510)
- `/ledger/14` (Adil_Shahi_dynasty): confirmed: 'In 1618, the sultan lost the fortress of Janjira to the independent Habshi state of western India.'
- `/ledger/16` (Shahaji): confirmed: 'In December 1638, the Bijapur forces seized Bangalore, which was given as a jagir to Shahaji'
- `/ledger/18` (Mir_Jumla_II): confirmed (year, fort): 'in 1648, Gingee fell to the Adil Shahis'. The region is a proxy, so confidence is lowered to 2.
- `/ledger/20` (Adil_Shahi_dynasty): confirmed: 'invaded by Mughal forces in 1657 under viceroy Aurangzeb, who captured Bidar and other forts'
- `/ledger/23` (Shivaji): confirmed: Panhala 'handed over ... on 22 September 1660'
- `/ledger/26` (Shivaji): confirmed (Ponda, April 1675). The region was too large and has been fixed.
- `/ledger/28` (Shivaji): confirmed: 1677 'Shivaji seized the forts of Vellore and Gingee'. The page does not call them Bijapuri, so confidence 2 is right.
- `/ledger/7` (Adil_Shahi_dynasty): confirmed: 'In 1534, Vijayanagara invaded the sultanate and seize the Raichur Doab'

## golconda-sultanate (fail)

Area: infobox None (year None), Cliopatria 203522.5, ratio None. No area on the Qutb Shahi page (checked). The Mir Jumla II page gives 'nearly 40,000 square kilometers' for Mir Jumla's Karnatak domain in 1652, which is consistent with the Carnatic additions in size.

Findings:

- OPEN `/ledger (1636)`: There is no vassal_start for Golconda's 1636 acceptance of Mughal suzerainty and tribute. The dossier's own war note on the 1656 siege quotes the sentence.
  - Evidence: Qutb Shahi dynasty page: 'In 1636, Mughal emperor Shah Jahan forced the Qutb Shahis to recognize Mughal suzerainty' and 'pay periodic tributes'. /wars/3/note quotes it.
  - Fix: Add {year 1636, type vassal_start, counterpart mughal-empire, region the 1612 shape, confidence 3, source Qutb Shahi page}. It ends with the 1687 dissolve, or with a vassal_end if a page dates one.
- OPEN `/keyframe_review/5/correction`: The 1640-1658 correction adds Nellore (100 km) and Gandikota (60 km) from 1640, and keeps the 123 Carnatic-interior cells that Cliopatria adds in 1640. The ledger gains these lands in April 1642, 1646 and 1650, and the note itself says the page dates them from 1642. The keyframe and the ledger disagree by two to ten years.
  - Evidence: Mir Jumla II page: 'In April 1642 Mir Jumla advanced with an army into Karnatak'; 1646 Chandragiri and Udayagiri; 'In 1650, Mir Jumla conquered the nearly inaccessible Gandikota fort'.
  - Fix: Split the span. Keep 1640-1641 without the Carnatic additions (the 1612 shape, or the 1640 shape minus the interior cells). Add new keyframes at 1642, 1646 and 1650 (or let the ledger gains carry those lands and drop the Nellore and Gandikota terms from the 1640 correction).
- APPLIED `/identity/rulers/0/from`: Sultan Quli started in 1512, before the state's start (December 1518).
  - Evidence: Quli Qutb Shah page infobox: 'Reign: 7 December 1518 – 2 September 1543' (the Qutb Shahi table prints 1512).
  - Fix: from = 1518, with a note.
- APPLIED `/ledger/6/confidence`: The 1646 gain was at confidence 3 with a 150 km circle around Nellore (about 70,000 km2). The page names only the Kingdom of Chandragiri, three forts and Udayagiri.
  - Evidence: Mir Jumla II page: 'In 1646, Mir Jumla decided to invade the Kingdom of Chandragiri'; three forts fell, then Udayagiri. The region is the researcher's reading.
  - Fix: confidence = 2.
- OPEN `/ledger/5/counterpart`: The same Aravidu remnant is named 'vijayanagara-empire' in 1642 and 'Kingdom of Chandragiri' in 1646.
  - Evidence: Mir Jumla II page calls it the Kingdom of Chandragiri.
  - Fix: Use one counterpart for both. If it is 'Kingdom of Chandragiri', it is already listed under counterparts_needing_dossiers.

Gaps (thin):

- `/ledger/2`: The 1521 gain of 193 cells from Vijayanagara is confidence 1. The Quli page names forts taken at 'Warangal, Kondapalli, Eluru, and Rajamundry' while Krishnadevaraya fought Odisha (undated), which can at least name the land. Page to try: https://en.wikipedia.org/wiki/Quli_Qutb_Shah
- `/ledger/3`: The 1572 eastern gain (37 cells) and the 1612 north-eastern coast gain (/ledger/4, 191 cells) are confidence 1 from 'nobody'. This is former Gajapati country (Rajahmundry, Chicacole), and the Gajapatis are to be added by sa-04-x. Page to try: https://en.wikipedia.org/wiki/Gajapati_Kingdom
- `/ledger/8`: The 1659 northern loss to the Mughals is confidence 1. The 1656 peace terms are not on the Siege of Golconda page. Page to try: https://en.wikipedia.org/wiki/Abdullah_Qutb_Shah
- `/identity/capitals/0`: The year the court moved from Golconda to Hyderabad (begun 1591). Page to try: https://en.wikipedia.org/wiki/Hyderabad

Spot checks:

- `/ledger/1` (Quli_Qutb_Shah): confirmed: 'Reign: 7 December 1518 – 2 September 1543'
- `/ledger/5` (Mir_Jumla_II): confirmed: 'In April 1642 ... Reaching Nellore plains unopposed he captured eight forts'
- `/ledger/6` (Mir_Jumla_II): confirmed (1646, Chandragiri, Udayagiri; submission by April 1647). The region is broader than the page, so confidence is lowered to 2.
- `/ledger/7` (Mir_Jumla_II): confirmed: 'In 1650, Mir Jumla conquered the nearly inaccessible Gandikota fort from Timma Nayadu'
- `/ledger/9` (Siege_of_Golconda): confirmed: siege 28 January - 22 September 1687; the betrayal by Sarandaz Khan on 21 September; the Mughal Empire annexes Golconda

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| berar-sultanate 1574 loss (ahmadnagar-sultanate) | ahmadnagar-sultanate 1574 gain | matched | Berar annexed 1574; the same region (Berar 1573 shape). |
| ahmadnagar-sultanate 1547 gain (bijapur-sultanate) | bijapur-sultanate 1547 loss | matched | Solapur-Naldurg strip, confidence 1 on both sides. |
| ahmadnagar-sultanate 1552 loss (bijapur-sultanate) | bijapur-sultanate 1552 gain | matched | Same strip reverts, confidence 1. |
| ahmadnagar-sultanate 1561 loss (bijapur-sultanate) | bijapur-sultanate 1561 gain | matched | Kaliyani. Both regions were fixed to a Basavakalyan circle; the cells lie inside Bidar's 1552-1578 shape (an overlap Cliopatria draws). |
| bidar-sultanate 1518 loss (golconda-sultanate) | golconda-sultanate 1518 gain | matched | Telangana strip, confidence 1 on both sides. |
| bidar-sultanate 1619 loss (bijapur-sultanate) | bijapur-sultanate 1619 gain | matched | Annexation of Bidar. |
| bijapur-sultanate 1510 loss (portuguese-empire) | portuguese-empire 1510 gain | matched | Goa, November 1510. The Portuguese region is admin1 Goa; Bijapur's is the 1511-minus-1512 cells. |
| ahmadnagar-sultanate 1540 loss (portuguese-empire) | portuguese-empire 1534 gain | mismatch | portuguese-empire /ledger/16 gains the same north Konkan coast (Mumbai 60 km, with Chaul and Bassein) in 1534 from the Gujarat Sultanate. There is no 1540 gain from Ahmadnagar. The Ahmadnagar event is confidence 1. |
| bidar-sultanate 1521 gain (vijayanagara-empire) | - | exception | vijayanagara-empire (sa-04, another part) is not written yet. 6 of the 21 cells come from Bijapur's 1520 shape, and Bijapur has no 1521 loss to Bidar. |
| golconda-sultanate 1642 gain (vijayanagara-empire) | bijapur-sultanate 1640 keyframe | mismatch | Bijapur's 1640-1652 keyframe (verdict ok) holds the Nellore cells that Golconda takes in April 1642. The two dossiers overlap at Nellore until the Mughal conquests. |
| bijapur-sultanate 1504 gain (bahmani-sultanate) | - | exception | bahmani-sultanate is owned by another part of sa-04 and not written yet. After 1571 the counterpart is the Aravidu remnant (Kingdom of Chandragiri); the 1638 Bangalore defender was Kempe Gowda III (Shahaji page). |
| bijapur-sultanate 1520 loss (vijayanagara-empire) | - | exception | vijayanagara-empire is owned by another part of sa-04 and not written yet. After 1571 the counterpart is the Aravidu remnant (Kingdom of Chandragiri); the 1638 Bangalore defender was Kempe Gowda III (Shahaji page). |
| bijapur-sultanate 1530 gain (vijayanagara-empire) | - | exception | vijayanagara-empire is owned by another part of sa-04 and not written yet. After 1571 the counterpart is the Aravidu remnant (Kingdom of Chandragiri); the 1638 Bangalore defender was Kempe Gowda III (Shahaji page). |
| bijapur-sultanate 1534 loss (vijayanagara-empire) | - | exception | vijayanagara-empire is owned by another part of sa-04 and not written yet. After 1571 the counterpart is the Aravidu remnant (Kingdom of Chandragiri); the 1638 Bangalore defender was Kempe Gowda III (Shahaji page). |
| bijapur-sultanate 1547 gain (vijayanagara-empire) | - | exception | vijayanagara-empire is owned by another part of sa-04 and not written yet. After 1571 the counterpart is the Aravidu remnant (Kingdom of Chandragiri); the 1638 Bangalore defender was Kempe Gowda III (Shahaji page). |
| bijapur-sultanate 1565 gain (vijayanagara-empire) | - | exception | vijayanagara-empire is owned by another part of sa-04 and not written yet. After 1571 the counterpart is the Aravidu remnant (Kingdom of Chandragiri); the 1638 Bangalore defender was Kempe Gowda III (Shahaji page). |
| bijapur-sultanate 1575 gain (vijayanagara-empire) | - | exception | vijayanagara-empire is owned by another part of sa-04 and not written yet. After 1571 the counterpart is the Aravidu remnant (Kingdom of Chandragiri); the 1638 Bangalore defender was Kempe Gowda III (Shahaji page). |
| bijapur-sultanate 1638 gain (vijayanagara-empire) | - | exception | vijayanagara-empire is owned by another part of sa-04 and not written yet. After 1571 the counterpart is the Aravidu remnant (Kingdom of Chandragiri); the 1638 Bangalore defender was Kempe Gowda III (Shahaji page). |
| bijapur-sultanate 1641 gain (vijayanagara-empire) | - | exception | vijayanagara-empire is owned by another part of sa-04 and not written yet. After 1571 the counterpart is the Aravidu remnant (Kingdom of Chandragiri); the 1638 Bangalore defender was Kempe Gowda III (Shahaji page). |
| bijapur-sultanate 1648 gain (vijayanagara-empire) | - | exception | vijayanagara-empire is owned by another part of sa-04 and not written yet. After 1571 the counterpart is the Aravidu remnant (Kingdom of Chandragiri); the 1638 Bangalore defender was Kempe Gowda III (Shahaji page). |
| golconda-sultanate 1521 gain (vijayanagara-empire) | - | exception | vijayanagara-empire is owned by another part of sa-04 and not written yet. After 1571 the counterpart is the Aravidu remnant (Kingdom of Chandragiri); the 1638 Bangalore defender was Kempe Gowda III (Shahaji page). |
| golconda-sultanate 1642 gain (vijayanagara-empire) | - | exception | vijayanagara-empire is owned by another part of sa-04 and not written yet. After 1571 the counterpart is the Aravidu remnant (Kingdom of Chandragiri); the 1638 Bangalore defender was Kempe Gowda III (Shahaji page). |
| ahmadnagar-sultanate 1596 loss (mughal-empire) | - | exception | mughal-empire is owned by sa-05, which has not run. |
| ahmadnagar-sultanate 1600 loss (mughal-empire) | - | exception | mughal-empire is owned by sa-05, which has not run. |
| ahmadnagar-sultanate 1633 loss (mughal-empire) | - | exception | mughal-empire is owned by sa-05, which has not run. |
| ahmadnagar-sultanate 1636 loss (mughal-empire) | - | exception | mughal-empire is owned by sa-05, which has not run. |
| bijapur-sultanate 1657 loss (mughal-empire) | - | exception | mughal-empire is owned by sa-05, which has not run. |
| bijapur-sultanate 1686 loss (mughal-empire) | - | exception | mughal-empire is owned by sa-05, which has not run. |
| golconda-sultanate 1659 loss (mughal-empire) | - | exception | mughal-empire is owned by sa-05, which has not run. |
| golconda-sultanate 1687 loss (mughal-empire) | - | exception | mughal-empire is owned by sa-05, which has not run. |
| bijapur-sultanate 1636 vassal_start (missing) (mughal-empire) | - | missing | Neither side carries the 1636 tribute and acknowledgement of Mughal authority (Adil Shahi page). Bijapur must add it; sa-05 should mirror it. |
| golconda-sultanate 1636 vassal_start (missing) (mughal-empire) | - | missing | Neither side carries the 1636 Mughal suzerainty (Qutb Shahi page). Golconda must add it; sa-05 should mirror it. |
| ahmadnagar-sultanate 1636 successor (land) (bijapur-sultanate) | - | missing | Ahmadnagar's successors name Bijapur's share of the 1636 partition, but no gain appears in Bijapur and no loss to Bijapur in Ahmadnagar. The author flagged it as a gap. |
| bijapur-sultanate 1656 loss (maratha-empire) | - | exception | maratha-empire (sa-05) is not written, and its Cliopatria row starts in 1677. The author lists Shivaji's pre-1677 kingdom under counterparts_needing_dossiers. |
| bijapur-sultanate 1659 loss (maratha-empire) | - | exception | maratha-empire (sa-05) is not written, and its Cliopatria row starts in 1677. The author lists Shivaji's pre-1677 kingdom under counterparts_needing_dossiers. |
| bijapur-sultanate 1660 gain (maratha-empire) | - | exception | maratha-empire (sa-05) is not written, and its Cliopatria row starts in 1677. The author lists Shivaji's pre-1677 kingdom under counterparts_needing_dossiers. |
| bijapur-sultanate 1673 loss (maratha-empire) | - | exception | maratha-empire (sa-05) is not written, and its Cliopatria row starts in 1677. The author lists Shivaji's pre-1677 kingdom under counterparts_needing_dossiers. |
| bijapur-sultanate 1675 loss (maratha-empire) | - | exception | maratha-empire (sa-05) is not written, and its Cliopatria row starts in 1677. The author lists Shivaji's pre-1677 kingdom under counterparts_needing_dossiers. |
| bijapur-sultanate 1677 loss (maratha-empire) | - | exception | maratha-empire (sa-05) is not written, and its Cliopatria row starts in 1677. The author lists Shivaji's pre-1677 kingdom under counterparts_needing_dossiers. |
| bijapur-sultanate 1618 loss (Janjira (Habshi state)) | - | exception | Listed by the author under counterparts_needing_dossiers (janjira-state). |
| golconda-sultanate 1646 gain (Kingdom of Chandragiri) | - | exception | Listed by the author (aravidu-vijayanagara). |
| golconda-sultanate 1650 gain (Timma Nayadu (Gandikota)) | - | exception | Listed by the author. |
| golconda-sultanate 1572 gain (nobody) | - | exception | Former Gajapati coast. The counterpart should probably be the Gajapati kingdom (to be added by sa-04-x). |
| golconda-sultanate 1612 gain (nobody) | - | exception | As for 1572. |

## Problems

- No page failed. WebFetch returns summaries made by a small model; quotes in this review are its extracts.
- Reviewer edits applied in place and re-validated with 0 errors: ahmadnagar /ledger/5/region; bijapur /ledger/11/region, /ledger/26/region, /keyframe_review/14-16 (the Ponda term), /ledger/18/confidence; golconda /identity/rulers/0/from, /ledger/6/confidence; berar /identity/rulers/3/to; bidar /identity/rulers/0/from.
- Only three Context dossiers exist (portuguese-empire, spanish-empire, english-colonial-empire). mughal-empire, vijayanagara-empire, maratha-empire, nayaks-of-thanjavur, kingdom-of-mysore, dutch-republic and portuguese-colonies are not written yet (their groups have not run), and neither is bahmani-sultanate (sa-04, another part).
- Cliopatria's Bijapur shape of 1640-1669 and Golconda's Mir Jumla gains overlap at Nellore; Bijapur's 1561 Kaliyani lies inside Bidar's shape. The orchestrator should route the Nellore overlap with the Bijapur fail.
