# Review of batch se-02-e (2026-10-19)

Reviewer: the adversarial reviewer (Phase B). Dossiers: sultanate-of-aceh, balinese-kingdom, blambangan-kingdom, maynila, sultanate-of-gowa, sultanate-of-bone. All six validate with `--resolve` and 0 errors. Aceh has 3 warnings, all for `pagaruyung-kingdom` (se-02-x). Neighbour dossiers read: portuguese-empire, samudera-pasai-sultanate, sultanate-of-kedah, sultanate-of-malacca, tondo, namayan, spanish-empire, sultanate-of-brunei, demak-sultanate, majapahit, early-balinese-kingdoms. The other context polities (mataram-sultanate, bali, dutch-republic, dutch-east-indies, sultanate-of-johor and the rest) are not written yet. Keyframe and ledger checks used the H3 r5 cells of the Cliopatria shapes (tools/grid.py).

## Verdicts

### sultanate-of-aceh: **fail**

Area: infobox None km2 (year None), Cliopatria 127447.1 km2, ratio None. The Aceh Sultanate infobox gives no area (checked); the author says so.

Findings:
- `/keyframe_review/9/correction, /keyframe_review/10/correction (against /ledger/11)` [BLOCKING, author to fix]: The 1613 gain of Aru (/ledger/11, a 90 km disc at 99.5 E 2.6 N) is drawn by no keyframe until Cliopatria's 1626 shape. The corrections for 1612-1623 and 1624-1625 contain none of its cells, so the map shows Aru 13 years after the ledger gains it, in a span marked adjust for other reasons. *Evidence:* Iskandar Muda page: 'In 1612 he conquered Deli, and in 1613 Aru and Johor.' Grid check (H3 r5): the Aru disc shares 0 cells with the Aceh 1612 shape and 44 with the 1626 shape. The dossier's own /keyframe_review/11 note says the 1626 step adds 'the Aru lands that the page dates to 1613, thirteen years earlier', but the correction does not move them. *Fix:* Add a new keyframe sultanate-of-aceh_1613 (from 1613, to 1623) equal to the /keyframe_review/9 correction united with the /ledger/11 Aru region. Unite the same Aru region into /keyframe_review/10 (1624-1625), and change the /keyframe_review/9 text to say it is valid for 1612 only. If the author keeps Cliopatria's 1626 date instead, move /ledger/11 to 1626 at confidence 1 and say why, though the page dates it 1613.
- `/ledger/21/counterpart (and /keyframe_review/12)` [author to fix]: The counterpart 'regional rulers' is neither a polity nor 'nobody'. The keyframe also drops the east coast and Nias in 1640, while this loss is dated 1641. *Evidence:* The Aceh Sultanate page names no successor for the east coast. It says only that after Iskandar Thani 'every corner shelters a separate king or governor'. *Fix:* Set the counterpart to 'nobody' and keep the quote in the note, or name the states if a page gives them (Deli, Siak, Johor). Align the year with the 1640 keyframe, or give that keyframe's correction a 1640-only note.

Gaps for a gap-filler:
- `/ledger/5, /ledger/6, /ledger/7`: The interior steps of 1526, 1540 and 1572 (about 15,000 km2 each) are gains from 'nobody' at confidence 1, with no place or year on any page. (try https://en.wikipedia.org/wiki/Alauddin_al-Kahar)
- `/keyframe_review/9 (1612 shape) and its successors to 1639`: Besides Deli and Nias, the 1612 step adds 59 cells (about 15,000 km2) that no event explains: the Mentawai islands (1.0-3.1 S, 98.5-100.3 E), Simeulue (2.4-2.9 N, 95.7-96.4 E), the Batu islands and Langkat. No page opened names Simeulue or the Mentawai as Acehnese. Either cut them, or add a gain with a page, or mark them 'unverified: page budget'. (try https://en.wikipedia.org/wiki/Simeulue)
- `/ledger/8, /ledger/9`: The 1609 west coast and the Pagaruyung vassalage are at confidence 1 ('early 17th century', no year). (try https://en.wikipedia.org/wiki/Alauddin_Riayat_Syah_Sayyid_al-Mukammal)
- `/ledger/21`: The 1641 loss of the east coast, Nias and the islands is at confidence 1 (the page is silent). (try https://en.wikipedia.org/wiki/Taj_ul-Alam)
- `/ledger/15, /ledger/17`: The ends of the Pahang and Kedah contests are at confidence 1 and are only bridged. The Johor sack of 1623 ('He again sacked Johor in 1623', Iskandar Muda page) is not recorded. (try https://en.wikipedia.org/wiki/Iskandar_Muda)
- `/ledger`: The infobox's 'Protectorate of the Ottoman Empire (1569-1903)' is left out on purpose (the notes call it nominal). The relation could be added as a vassal pair with ottoman-empire if the Ottoman dossier wants it. (try https://en.wikipedia.org/wiki/Ottoman_expedition_to_Aceh)

Spot checks:
- `/ledger/22` https://en.wikipedia.org/wiki/Pagaruyung_Kingdom: confirmed ('When the VOC succeeded in expelling the Sultanate of Aceh from the coast of West Sumatra in 1666'; the 1665 revolt against the Aceh governors)
- `/ledger/11` https://en.wikipedia.org/wiki/Iskandar_Muda: confirmed ('In 1612 he conquered Deli, and in 1613 Aru and Johor')
- `/ledger/14` https://en.wikipedia.org/wiki/Iskandar_Muda: confirmed ('In 1617 he conquered Pahang and carried its sultan Ahmed Syah to Aceh')
- `/ledger/32` https://en.wikipedia.org/wiki/Aceh_Sultanate: confirmed (infobox: dissolution by the Dutch 1904; the body has the sultan surrendering in 1903)
- `/ledger/25` https://en.wikipedia.org/wiki/Aceh_Sultanate: confirmed (the palace was captured on 31 January 1874 and the sultan left the capital in early 1874)
- `/keyframe_review/8 (Inderapura cut)` https://en.wikipedia.org/wiki/Iskandar_Muda: confirmed (Aceh was never able to 'expand the empire to the rich pepper-producing Inderapura Kingdom')

### balinese-kingdom: **fix**

Area: infobox None km2 (year None), Cliopatria 7719.0 km2, ratio None. There is no km2 figure on the page (checked); the infobox gives the extent 'Blambangan (Banyuwangi) to the western part of Sumbawa'. The 1519 shape is roughly Bali island.

Findings:
- `/ledger/6/counterpart (with /keyframe_review/3)` [author to fix]: The 1683 loss of western Lombok names 'bali' as the counterpart. That polity's life (Cliopatria row and planned dossier) starts in 1687, four years later, so no mirror can exist. The dossier's own /keyframe_review/3 note also says that the Lombok page does not support Cliopatria's 1683 loss. *Evidence:* polities.csv: bali 1687..1907. Lombok page as quoted in the dossier: the Balinese held western Lombok from the early 17th century and 'the whole island by 1750'. *Fix:* Either set the counterpart to 'nobody', with a note that Gelgel broke up and Karangasem held Lombok outside the crown, or keep western Lombok in the 1683-1686 keyframe and pass it to 'bali' with the 1686 dissolve.

Gaps for a gap-filler:
- `/ledger/1, /ledger/2`: The suzerainty over Blambangan, Lombok and western Sumbawa is dated 1519 (Cliopatria's year) at confidence 1. The page gives only Dalem Baturenggong's 'mid-16th century' apogee (infobox reign c. 1460-1550). (try https://en.wikipedia.org/wiki/History_of_Bali)
- `/ledger/6`: The 1683 loss is at confidence 1 and taken from Cliopatria. No page dates it. (try https://en.wikipedia.org/wiki/Karangasem_Regency)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Bali_Kingdom: confirmed (infobox: 'Vassal state of the Majapahit Empire (1343-1478)', 'Gelgel Kingdom (1478-1661)')
- `/ledger/5` https://en.wikipedia.org/wiki/Bali_Kingdom: confirmed ('In 1639 Mataram launched an invasion to Blambangan'; Gelgel supported Blambangan)
- `/ledger/7` https://en.wikipedia.org/wiki/Bali_Kingdom: confirmed ('In 1686 a new royal seat was established in Klungkung, four kilometres north of Gelgel')
- `/ledger/1` https://en.wikipedia.org/wiki/Bali_Kingdom: confirmed as undated: the apogee sentence is on the page, without a year; 1519 is Cliopatria's, as the note says
- `/ledger/4` https://en.wikipedia.org/wiki/Sultanate_of_Gowa: confirmed ('In 1618 Makassar undertook the first of several attacks on the island of Sumbawa')

### blambangan-kingdom: **fix**

Area: infobox None km2 (year None), Cliopatria 27731.8 km2, ratio None. The page gives no area (checked); the author notes this.

Findings:
- `/ledger/9/counterpart and /identity/successors/0/slug` [APPLIED by reviewer]: The 1768 loss and the successor named 'dutch-east-indies', whose life starts in 1800. In 1768 the land went to the VOC, which this batch calls dutch-republic (Aceh /ledger/22, Gowa /ledger/9). *Evidence:* polities.csv: dutch-east-indies 1800..1949, dutch-republic 1582..1795. The dossier's own successor note says 'The Dutch East India Company held it until 1799'. *Fix:* Change both to 'dutch-republic'. Done; the dossier still validates with 0 errors and 0 warnings.
- `/ledger (vassal events)` [author to fix]: Blambangan carries no vassal events. balinese-kingdom /ledger/1 (vassal_start 1519) and /ledger/5 (vassal_end 1639) name blambangan-kingdom and have no mirror here. The infobox line 'Blambangan became the vassal of Mataram Sultanate aftermath of the war: 1635-1639' is recorded only as a contest. The notes leave all vassalage to the suzerains' dossiers, but the rule is that both ledgers carry it. *Evidence:* Blambangan Kingdom infobox, as read in this review; reviewer brief 2.3: 'a vassal_start of X is a vassal_start in X's ledger with this state as counterpart'. *Fix:* Add vassal_start 1519 and vassal_end 1639 with counterpart balinese-kingdom (confidence 1 and 2, Bali Kingdom page). Add vassal_start 1639 with counterpart mataram-sultanate (confidence 2, infobox) and vassal_end 1659 (Mataram Sultanate page, already in sources). If the Mataram page's 'rejoined Bali' in 1697 is drawn, add vassal_start 1697 with counterpart bali, ended at 1768.
- `/notes (and /identity/start)` [author to fix]: The majapahit dossier names blambangan-kingdom as the Eastern court: /ledger/17 (1403 loss), the 1404-1406 contest pair and /ledger/20 (1406 gain). Blambangan starts in 1478, so these events have no mirror, and the notes do not mention them. *Evidence:* Blambangan Kingdom page: the Eastern court, 'which would become the Blambangan Kingdom', was led by Bhre Wirabhumi in the Regreg war (1404-1406). *Fix:* Say in the notes whether the Eastern court of 1376/1403-1406 is this state. If it is, add a phase. If it is not, the orchestrator should ask the Majapahit author to name a different counterpart.

Gaps for a gap-filler:
- `/ledger/2`: The 1519 gain from majapahit (the eastern salient with Pasuruan and Pajarakan) is at confidence 1. Tome Pires (c. 1515) already has Blambangan as 'the most powerful Javanese kingdom east of Surabaya'. (try https://en.wikipedia.org/wiki/Blambangan_Kingdom)
- `/identity/capitals`: The capitals leave gaps for 1501-1527, 1600-1665 and 1762-1768. Kedawung and Lateng are undated. (try https://en.wikipedia.org/wiki/Banyuwangi_Regency)
- `/ledger/9`: The VOC conquest of 1767-1772 and the end year (1768 against 1777) are not settled. (try https://en.wikipedia.org/wiki/Puputan_Bayu)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Blambangan_Kingdom: confirmed (infobox: 'Dissolution of Majapahit led to an independent Blambangan: 1478')
- `/ledger/1` https://en.wikipedia.org/wiki/Blambangan_Kingdom: confirmed (capitals 'Semboro (1478-1489); Lamajang (1489-1501)')
- `/ledger/5` https://en.wikipedia.org/wiki/Blambangan_Kingdom: confirmed (infobox: 'Blambangan lost Pasuruan and Pajarakan because it was taken by Demak: 1545-1546'; the claim is in the infobox only)
- `/ledger/7` https://en.wikipedia.org/wiki/Blambangan_Kingdom: confirmed ('The conquest of Blambangan by the forces of Sultan Agung of Mataram took place in 1639')
- `/ledger/9` https://en.wikipedia.org/wiki/Blambangan_Kingdom: confirmed (infobox: 'Absorbed into the territory of Dutch East Indies: 1768/1777')

### maynila: **pass**

What I tried: I tried the start (c. 1500), the end (24 June 1571), the cut of the Ryukyu cells (a correction intersected with the Philippines), and the mirrors in tondo and spanish-empire. Both mismatches are on the other dossiers' side.

Area: infobox None km2 (year None), Cliopatria 3359.4 km2, ratio None. There is no infobox area. The Cliopatria shapes are 85-90 percent Okinawa cells; the adjust and wrong verdicts handle this.

Gaps for a gap-filler:
- `/ledger/1, /ledger/2`: The Tondo contest is at confidence 1 (infobox 'c. before 1521'), and the page gives no Maynila-Tondo border. (try https://en.wikipedia.org/wiki/Rajah_Sulayman)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Maynila_(historical_polity): confirmed (infobox: 'Establishment of Maynila and conversion to Islam: c. 1500'; Scott: 'probably founded as a Bornean trading colony about 1500')
- `/ledger/1` https://en.wikipedia.org/wiki/Maynila_(historical_polity): confirmed (infobox: 'territorial conflicts with Tondo: c. before 1521'; Ache sailing to confront his cousin in 1521)
- `/ledger/3` https://en.wikipedia.org/wiki/Maynila_(historical_polity): confirmed (Goiti 'attacked Maynila in May of that year', 1570)
- `/ledger/5` https://en.wikipedia.org/wiki/Maynila_(historical_polity): confirmed ('declared as the new Spanish city of Manila on June 24, 1571', 'effectively ending Maynila's history as an independent polity')

### sultanate-of-gowa: **fail**

Area: infobox None km2 (year None), Cliopatria 2613.0 km2, ratio None. The page gives no area (checked).

Findings:
- `/identity/end, /ledger/11, /ledger/12, /keyframe_review/2, /identity/successors/0` [BLOCKING, author to fix]: The dossier ends Gowa in June 1669 and gives its whole core to the VOC (/ledger/11 loss, successor dutch-republic). None of the pages cited say this. Gowa was reduced to a VOC vassal and lived on until 1911, so the map would show 2,600 km2 of Gowa as Dutch for 242 years. The /ledger/11 note ('Gowa's core passes to the VOC') is not what the cited Makassar War page says. *Evidence:* Sultanate of Gowa page: 'In 1911 the sultanate lost its independence and became a Dutch East Indies regency'; it dissolved after 1945 (the infobox says 1957). Treaty of Bongaya page: 'Gowa was reduced to a vassal of the VOC'. Makassar War page: Palakka and the VOC divided power, with Palakka 'dominating internal affairs and the VOC dominating external affairs'; Speelman built Fort Rotterdam on Somba Opu's site. One dossier per state: a state reduced to vassalage continues with vassal events (research brief section 6). *Fix:* Move the end to 1911 (loss of independence) and note the page's 1945 and 1957. Add vassal_start 1667-11 with counterpart dutch-republic (Treaty of Bongaya page). Close it with vassal_end 1795 and reopen with dutch-east-indies from 1800, or bridge as the author judges. Keep /ledger/9 (Jum Pandan). Replace /ledger/11 with a loss to dutch-republic in June 1669 of the Somba Opu-Makassar coast only (the Fort Rotterdam area, e.g. the Makassar 8-20 km disc). Add a keyframe for 1669-1911 equal to the 1662 outline minus that disc. End with a loss to dutch-east-indies and a dissolve in 1911, and make that the successor.
- `/ledger/4, /ledger/8` [author to fix]: The vassal pair over Bone (1611-1667) has no mirror in sultanate-of-bone, which records only contests; the same author wrote both dossiers. *Evidence:* Sultanate of Bone /ledger/1-6: contest pairs only. The Makassar War page: after the 1644 rising, Bone was defeated at Passempe (a footnote dates it April-May 1646) and a Gowa regent was installed. *Fix:* Make the two agree. Either Bone adds a vassal pair with counterpart sultanate-of-gowa, or Gowa's vassal_start moves to 1646 (Passempe) if 1611 was only a forced conversion.

Gaps for a gap-filler:
- `/ledger/0, /ledger/1`: The 1320 start and the 1512 merge with Tallo are at confidence 1: the page says 'Not much is known'. (try https://en.wikipedia.org/wiki/Tallo_Kingdom)
- `/ledger`: Gowa's dependencies (Sumbawa after 1618, Selayar, Buton, eastern Lombok, Minahasa) have no tribute or conquest years. (try https://en.wikipedia.org/wiki/Sultanate_of_Bima)

Spot checks:
- `/ledger/2` https://en.wikipedia.org/wiki/Sultanate_of_Gowa: confirmed (capitals Tamalate 1320-1548, Somba Opu 1548-1670)
- `/ledger/5` https://en.wikipedia.org/wiki/Sultanate_of_Gowa: confirmed ('In 1618 Makassar undertook the first of several attacks on the island of Sumbawa')
- `/ledger/9` https://en.wikipedia.org/wiki/Treaty_of_Bongaya: confirmed (18 November 1667; 'Jum Pandan ... was ceded to the Dutch'; 'Gowa was reduced to a vassal of the VOC')
- `/ledger/10` https://en.wikipedia.org/wiki/Sultanate_of_Gowa: confirmed (Somba Opu broken on June 12, 1669; the Makassar War page has an assault from 14 June and an infobox end of 24 June)
- `/ledger/11` https://en.wikipedia.org/wiki/Makassar_War: not on page: the page has Speelman building Fort Rotterdam and the VOC taking external affairs, not Gowa's core passing to the VOC; the Gowa page has independence lost in 1911

### sultanate-of-bone: **fix**

Area: infobox 2600 km2 (year None), Cliopatria 2155.1 km2, ratio 0.83. The body text gives 'an area of 2,600 square kilometres' without a year. The corrected shape (with the Watampone disc) is about 3,000 km2.

Findings:
- `/ledger/1 to /ledger/6 (1611-1667) and /ledger/4/note` [author to fix]: No vassal or occupation event mirrors Gowa's vassal pair (sultanate-of-gowa /ledger/4, /ledger/8). The /ledger/4 note says 'The page gives no outcome' for the 1644 rising, but the cited Makassar War page gives one: Bone was defeated at Passempe and a Gowa regent was installed. *Evidence:* Makassar War page: 'In 1644, Bone rose up against Gowa'; the Battle of Passempe saw Bone defeated and a regent installed; a footnote dates the battle April-May 1646. Bone page: La Maqdaremmeng was restored in 1667. *Fix:* Add vassal_start with counterpart sultanate-of-gowa (1611 to match Gowa, or 1646 for Passempe, with Gowa changed to match) and vassal_end 1667. Raise /ledger/4 to confidence 2, quote the Passempe sentence, and consider 1646 as its year.

Gaps for a gap-filler:
- `/wars/2`: The wars of 1824 and 1859 have no territorial result. The 1860 reduction to Dutch vassalage ('the Dutch tried to reduce Bone from an equal to a vassal') is undated. (try https://en.wikipedia.org/wiki/Bone_Regency)
- `/ledger/0, /ledger/4, /ledger/6`: These three events are at confidence 1: the 1350 start (the body says early 15th century), the 1645 end of the contest and the 1660 end of the contest. (try https://en.wikipedia.org/wiki/Arung_Palakka)

Spot checks:
- `/ledger/3` https://en.wikipedia.org/wiki/Makassar_War: confirmed ('In 1644, Bone rose up against Gowa'; footnote: Passempe was really April-May 1646)
- `/ledger/5` https://en.wikipedia.org/wiki/Makassar_War: confirmed ('In 1660 Arung Palakka ... led a Bugis revolt against Gowa')
- `/ledger/7` https://en.wikipedia.org/wiki/Bone_Sultanate: confirmed (after Makassar fell in 1669, Bone was 'by treaty and in practice the overlord of South Sulawesi' until 1814)
- `/ledger/11` https://en.wikipedia.org/wiki/Bone_Sultanate: confirmed (after the 1905 defeat Bone 'lost its independence to the Dutch')

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| sultanate-of-aceh 1522 gain (Sultanate of Pedir) |  | exception | No dossier yet; listed in counterparts_needing_dossiers (sultanate-of-pedir, se-02-x). |
| sultanate-of-aceh 1524 gain (samudera-pasai-sultanate) | samudera-pasai-sultanate 1524 loss | matched | Pasai /ledger/8 loss and /ledger/9 dissolve to sultanate-of-aceh in 1524. |
| sultanate-of-aceh 1523 contest_start (portuguese-empire) | portuguese-empire 1529 loss | mismatch | portuguese-empire /ledger/11 gains the Pasai coast in 1521 from 'sultanate-of-aceh' (it should be samudera-pasai-sultanate) and loses it in 1529 (/ledger/14, confidence 1). The Pasai page has the garrison evacuated in 1524. Route to the portuguese-empire author (am-06): loss in 1524, gain counterpart samudera-pasai-sultanate. |
| sultanate-of-aceh 1526 gain (nobody) |  | exception | The counterpart is nobody. |
| sultanate-of-aceh 1540 gain (nobody) |  | exception | The counterpart is nobody. |
| sultanate-of-aceh 1572 gain (nobody) |  | exception | The counterpart is nobody. |
| sultanate-of-aceh 1624 gain (nobody) |  | exception | The counterpart is nobody. |
| sultanate-of-aceh 1609 gain (pagaruyung-kingdom) |  | exception | Also covers the vassal_start of 1609 and the vassal_end of 1666. se-02-x has not run; the author lists it. |
| sultanate-of-aceh 1612 gain (Deli) |  | exception | Listed in counterparts_needing_dossiers. |
| sultanate-of-aceh 1613 gain (Aru) |  | exception | Listed (kingdom-of-aru). The keyframes do not draw this gain until 1626; see the fixes. |
| sultanate-of-aceh 1613 occupation_start (sultanate-of-johor) |  | exception | The sultanate-of-johor dossier is not written yet (another se-02 part). |
| sultanate-of-aceh 1617 contest_start (Pahang Sultanate) |  | exception | Listed (sultanate-of-pahang). |
| sultanate-of-aceh 1619 contest_start (sultanate-of-kedah) |  | missing | The sultanate-of-kedah dossier exists and has no Acehnese event. Its author could add the 1619/1620 (or 1629) conquest as an occupation or contest. This is not territorial on Aceh's side. |
| sultanate-of-aceh 1620 vassal_start (sultanate-of-perak) |  | exception | The sultanate-of-perak dossier is not written yet (another se-02 part). |
| sultanate-of-aceh 1641 loss (regional rulers) |  | exception | Not a polity; the fixes recommend 'nobody'. |
| sultanate-of-aceh 1666 loss (dutch-republic) |  | exception | dutch-republic is owned by eu-09, not run yet. It should carry a 1666 gain of the west coast of Sumatra. |
| sultanate-of-aceh 1904 loss (dutch-east-indies) |  | exception | dutch-east-indies is owned by se-03, not run yet. Its Cliopatria shape adds Aceh only in 1914. |
| balinese-kingdom 1478 found (majapahit) | majapahit 1518 dissolve | mismatch | Majapahit keeps Bali in its shape to 1518 (majapahit_1516 ok) and records no loss of Bali. The Bali Kingdom infobox has the Majapahit vassalage end in 1478. Recommend that the Majapahit dossier (se-02-c, already failed) lose Bali to balinese-kingdom in 1478. |
| balinese-kingdom 1519 vassal_start (blambangan-kingdom) |  | missing | blambangan-kingdom (same batch) has no vassal_start or vassal_end with balinese-kingdom (1519-1639). This is a fix on the Blambangan side. |
| balinese-kingdom 1519 vassal_start (Lombok and West Sumbawa) |  | exception | Not a polity; Sasak and Sumbawa principalities. Also covers the 1609 gain and the 1618 vassal_end. |
| balinese-kingdom 1683 loss (bali) |  | mismatch | bali (se-02, not written) begins in 1687, four years after the loss. See the fixes. |
| blambangan-kingdom 1478 found (majapahit) | majapahit 1518 dissolve | mismatch | Majapahit keeps East Java to 1518 and records no loss of the eastern salient in 1478. The Blambangan infobox gives independence in 1478. Recommend that Majapahit lose the eastern salient to blambangan-kingdom in 1478 and keep Daha's core to 1518. |
| blambangan-kingdom 1519 gain (majapahit) |  | mismatch | Majapahit dissolved in 1518 to demak-sultanate and records no loss to Blambangan. With the 1478 fix above this gain becomes part of the 1478 split (confidence 1). |
| majapahit 1403 loss (blambangan-kingdom) |  | mismatch | Also covers the 1404-1406 contest and the 1406 gain. Blambangan starts in 1478 and has no Eastern-court phase. The Blambangan page says the Eastern court 'would become the Blambangan Kingdom'. Route to both authors. |
| blambangan-kingdom 1546 loss (demak-sultanate) |  | missing | demak-sultanate (exists, end 1568) has no gain of Pasuruan or Pajarakan in 1545-1546, only Trenggana killed at Pasuruan. Route to the Demak author (se-02-d). |
| blambangan-kingdom 1635 contest_start (mataram-sultanate) |  | exception | mataram-sultanate is not written yet (another se-02 part). It should carry vassal_start 1639 and vassal_end 1659 over Blambangan, and so should Blambangan (see the fixes). |
| blambangan-kingdom 1768 loss (dutch-republic) |  | exception | Counterpart corrected by the reviewer from dutch-east-indies (life from 1800). dutch-republic (eu-09) is not run yet. |
| maynila 1500 found (nobody) | tondo 1497 loss | mismatch | tondo /ledger/1 loses the Pasig mouth to maynila in c. 1497 (confidence 1), three years before Maynila exists, quoting Scott's 'about 1500'. Route to the Tondo author: move it to 1500. The Maynila page does not say the land was Tondo's, so 'nobody' stands here. |
| maynila 1520 contest_start (tondo) | tondo 1520 contest_start | matched | Ended in 1521 on both sides. |
| maynila 1571 loss (spanish-empire) | spanish-empire 1571 gain | mismatch | spanish-empire /ledger/22 gains Manila in 1571 with counterpart 'namayan', though its note says 'the Spaniards captured Maynila'. Route to the Spanish Empire author: the counterpart should be maynila, with a separate gain from namayan if wanted. |
| sultanate-of-gowa 1512 merge (Tallo) |  | exception | Listed (kingdom-of-tallo). |
| sultanate-of-gowa 1611 vassal_start (sultanate-of-bone) | sultanate-of-bone 1611 contest_start | mismatch | Also covers the 1667 vassal_end. Bone records only contests (1611, 1644-1645, 1660). Both dossiers are in this batch; see the fixes on both. |
| sultanate-of-gowa 1618 contest_start (Sumbawa) |  | exception | Listed (sultanate-of-sumbawa). |
| sultanate-of-gowa 1667 loss (dutch-republic) |  | exception | Also covers the 1669 loss. eu-09 has not run. The 1669 loss of the whole core is wrong; see the Gowa fixes. |
| sultanate-of-bone 1669 vassal_start (South Sulawesi principalities) |  | exception | Not a polity; Wajo, Soppeng and Luwu are listed. |
| sultanate-of-bone 1905 loss (dutch-east-indies) |  | exception | se-03 has not run. |

## Problems and decisions for the orchestrator

- No page failed to load. WebFetch returns a model's summary of each page, so the quotes above are as the summary gave them.
- Overlap to decide: majapahit (se-02-c) keeps Bali and the eastern salient of Java to 1518, while balinese-kingdom and blambangan-kingdom start in 1478 from their own infoboxes. Both pages give 1478, so the reviewer recommends cutting Majapahit (losses to both in 1478, Daha's core kept to 1518). Neither of this batch's dossiers needs to change for it.
- Reviewer edit: blambangan-kingdom /ledger/9/counterpart and /identity/successors/0/slug changed from dutch-east-indies to dutch-republic. The file was re-validated (0 errors) and read back after 10 s.
- Wrong verdicts for years after a state's end (maynila_1572 and maynila_1595; sultanate-of-aceh_1946 to _1958) carry a correction region (a Manila disc, admin1 Aceh) whose text says 'not the state'. The compiler must clip corrections to identity start/end, or these would draw Maynila after 1571 and Aceh after 1904.
- The Gowa vassal sultanate (1669-1911) also changes how Bone's 1669-1814 overlordship tint should treat Gowa's land: that land is a VOC vassal, not Bone's. The Bone tint's region (South Sulawesi minus Bone and the Makassar disc) includes it. The Gowa rewrite should settle this.

Gazetteer names needed: Sigli, Nias, Inderapura, Deli, Aru (Haru), Pagar Ayer, Indrapuri, Keumala, Samalanga, Sumbawa, Somba Opu, Lombok, Gelgel, Pajarakan, Panarukan, Lumajang, Muncar.

