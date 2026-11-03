# Review of batch se-02-h (Kutai Kartanegara, Jambi, Bali)

Written 2026-10-19 by the adversarial reviewer. The machine copy is history/notes/phase-b/reviews/se-02-h.json.

The validator gives 0 errors on all three dossiers. Its warnings are only unknown gazetteer places and the kutai-martadipura counterpart, which has no dossier yet. In this run a 'fix' verdict means the reviewer made the fixes; 'fail' means the dossier goes back to the author.

## kutai-kingdom: fail

- **/ledger/1/region (with /keyframe_review/0, /keyframe_review/1/correction and /keyframe_review/2-5)** (for the author): The 1635 gain of Martapura (30 km round Muara Kaman) falls mostly outside every keyframe drawn after it, and it does not explain how K0 grows into K1.
  - Evidence: Taking the author's own Muara Kaman coordinates (116.7 E, 0.2 S, from the report hint), the 30 km disc covers 11 cells, and 8 of them (about 2,020 km2) lie outside Cliopatria's 1648 outline, whose north edge is at 0.31 S. K1 (1635-1647) is that outline unchanged, and K2-K5 are 'ok' or change only the years. So the ledger has Kutai holding Martapura's centre from 1635 to 1844 while no keyframe draws it. Also, K0 (5 cells, about 1,260 km2, round Kutai Lama) becomes K1 (28 cells, about 7,080 km2), and no event covers 20 of the 23 added cells. Sultanate page: 'In 1635, the Kingdom of Kutai Kartanegara defeated the Kingdom of Kutai Martapura', which was 'centered in Muara Kaman'.
  - Fix: Make the keyframes and the ledger tell one story. Option (a): set K1-K5 to verdict adjust with correction {union: [Cliopatria shape, Muara Kaman 30 km]}, and make the 1635 gain region {union: [{minus: [{cliopatria: 'Kutai Kingdom', year: 1648}, Kutai Lama 20 km]}, Muara Kaman 30 km]}. Option (b): state in K1's correction text that Cliopatria's outline is the united realm, and make the gain region {minus: [{cliopatria: 'Kutai Kingdom', year: 1648}, Kutai Lama 20 km]}, dropping the disc that lies outside.
- **/ledger/0/note and /keyframe_review/0/note** (applied by reviewer): The quote 'founded in 1300 at Kutai Lama' was attributed to the Sultanate page as the founding of Kutai Kartanegara. On that page the phrase belongs to the Hindu Kingdom of Martapura, from which the sultanate originated, and the page body says 14th century.
  - Evidence: Sultanate page lead: the sultanate 'originated from the Hindu Kingdom of Martapura founded in 1300 at Kutai Lama'. Body: 'The Kingdom of Kutai Kartanegara was founded in the 14th century in the area of Kutai Lama'. Kutai page: 'established around the end of the 13th century', with the first ruler at 1300-1325. The year 1300 stays at confidence 2 on the Kutai page.
  - Fix: Reworded both notes to give what each page actually says. The year, the region and the confidence are unchanged. Re-validated: 0 errors.

Thin items, for a gap-filler:
- /keyframe_review/0: The extent of Kutai Kartanegara in 1300-1634 (a 20 km placeholder) and the extent of Martapura before 1635. Neither page gives either. Page to try: https://en.wikipedia.org/wiki/Kutai_Martadipura
- /identity/end and /identity/successors/0: Kutai's status after 1844 (the Kutai page says direct control; the Sultanate page says a vassal with internal autonomy under Sulaiman, 1845-1899, whose realm covered almost all of East Kalimantan). This is for a vassal tint in the dutch-east-indies dossier. Page to try: https://en.wikipedia.org/wiki/Kutai_Kartanegara_Regency
- /ledger: Relations with Banjar, Gowa/Makassar, the Bugis settlement at Samarinda and the VOC between 1648 and 1844. No event on the two pages opened. Page to try: https://en.wikipedia.org/wiki/Samarinda

Spot checks:
- /ledger/0 (https://en.wikipedia.org/wiki/Kutai): confirmed: 1300 (first ruler 1300-1325, 'end of the 13th century', Tepian Batu or Kutai Lama). The Sultanate-page quote was mis-attributed; reworded.
- /ledger/1 (https://en.wikipedia.org/wiki/Kutai_Kartanegara_Sultanate): confirmed: 'In 1635, the Kingdom of Kutai Kartanegara defeated the Kingdom of Kutai Martapura', centred in Muara Kaman
- /ledger/3 (https://en.wikipedia.org/wiki/Kutai): confirmed: 'In 1732 ... moved its capital from Old Kutai to Jembayan'; the Sultanate page agrees
- /ledger/4 (https://en.wikipedia.org/wiki/Kutai): confirmed: 'in 1782 from Pemarangan to Tepian Pandan'; the Sultanate page has 1782 to Tenggarong
- /ledger/5 (https://en.wikipedia.org/wiki/Kutai): confirmed: 1844, after Murray's repulse, 'the Dutch defeated the sultan Aji Muhammad Salehudin' and 'took direct control of Kutai'

Area: infobox None, Cliopatria 6765.8, ratio None. Neither page has an area figure (checked: the Kutai page has no infobox, and the Sultanate infobox has none). A Sultanate-page caption puts 'almost the entire present-day East Kalimantan Province' under Kutai only from Sulaiman's reign (1845-1899), after this dossier ends. K2 says so.

## sultanate-of-jambi: fail

- **/ledger/5/region** (for the author): The c. 1681 gain (confidence 1) adds the whole Batang Indragiri valley plus the Tungkal disc to Jambi. That land is not in any keyframe and is never lost again, so it would add about 80 percent to the state's area.
  - Evidence: Gazetteer: {river: Batang Indragiri, km: 20} gives 69 cells (about 17,450 km2), none inside the 1670 shape (101 cells, about 25,540 km2). The Tungkal 60 km disc adds 11 more cells (about 2,780 km2) outside the shape. Johor-Jambi wars page: Jambi 'recaptured Kuala Tungkal and Indragiri' after 1679, with no year and no former holder named, and the infobox gives territorial changes as 'status quo ante bellum'. The Jambi page describes the domain as the Batanghari, part of the Tembesi, and Tungkal, never Indragiri.
  - Fix: Limit the gain to the land lost in 1655 (the /ledger/2 region, ideally intersected with the 1670 shape) and keep confidence 1. In the note, say that the recapture of Indragiri is not drawn, because the page does not say Jambi held Indragiri and gives status quo ante bellum.
- **/ledger/3/region, /ledger/4/region and /wars/0/zones/0** (for the author): The contest zone includes a 20 km buffer along the whole Batang Indragiri, from the Minangkabau highlands to the sea (about 17,450 km2). The page names only fighting at the Jambi river mouth, Tungkal and Indragiri.
  - Evidence: Johor-Jambi wars page: May 1667, a Johorese fleet at the mouth of the Jambi River; August 1670, Jambian raids on Indragiri and Tungkal; May 1679, an attack on Jambi. Nothing up the Indragiri valley.
  - Fix: Replace the river buffer with the lower Indragiri (a disc round the Indragiri mouth, e.g. at Rengat or Tembilahan) or drop it. Tell the Johor owner, since sultanate-of-johor /ledger/11 and /ledger/13 use the same spec.
- **/keyframe_review/0 and /keyframe_review/1** (for the author): K0 (1460-1669, correction = the 1670 shape) and K1 (1670-1821, ok) both keep Tungkal, while /ledger/2 loses it to Johor in 1655 and /ledger/5 recovers it c. 1681. The notes acknowledge this but the keyframes do not draw it.
  - Evidence: The Tungkal disc covers 18 of the 1670 shape's 101 cells (about 4,550 km2, 18 percent). Reviewer rule 4: an adjust keyframe must agree with the ledger, and an event without a trace in the keyframes must be small.
  - Fix: Split K0 at 1655: add a new keyframe sultanate-of-jambi_1655 for 1655-1669 with {minus: [{cliopatria: 'Sultanate of Jambi', year: 1670}, Tungkal disc]}. Mark K1 adjust and add a new keyframe for 1670-1680 without Tungkal (or a K1 correction text saying so).
- **/ledger (no 1858 event) and /wars/1/zones** (for the author): The 1858 division of Jambi is missing. The ledger records the identical 1688 split but not this one. Also, war W1 has the whole 1900 shape as its zone but no contest_start/contest_end in the ledger.
  - Evidence: Jambi Sultanate page: in 1858 a Dutch expedition deposed Taha, who fled upstream to Upper Jambi while his uncle Ahmad Nazaruddin ruled; 'This split Jambi into Upper and Lower areas'. Research-brief rule 6 draws contested land from contest events naming the zone.
  - Fix: Add a split in 1858 (counterpart 'Upper Jambi (Sultan Taha)', confidence 2) ended by the 1904 dissolve or a merge. Or add contest_start 1858 and contest_end 1904 with dutch-east-indies over the W1 zone. Otherwise empty W1's zones and say why.

Thin items, for a gap-filler:
- /ledger/4 and /ledger/5: A year for the end of the Johor war and for the recapture of Tungkal. The war page gives none: its infobox puts the Tungkal recapture in the 1673 war and a fourth war in 1680-1681, and the Johor dossier uses 17 October 1679. Page to try: https://en.wikipedia.org/wiki/Johor_Sultanate
- /keyframe_review/0: The extent before 1670 (the 1460-1669 keyframe reuses the 1670 shape), and Majapahit's hold over Jambi until the early 16th century. Page to try: https://en.wikipedia.org/wiki/Melayu_Kingdom
- /keyframe_review/2 and /keyframe_review/3: Events behind the 1822 (-0.8 percent) and 1895 (-1.1 percent) shape steps. Both are small and acknowledged. Page to try: https://en.wikipedia.org/wiki/Kerinci_Regency

Spot checks:
- /ledger/1 (https://en.wikipedia.org/wiki/Jambi_Sultanate): confirmed: 'At around 1615, Jambi became a sultanate'; infobox Kingdom 1460-1615, Sultanate 1615-1904
- /ledger/2 (https://en.wikipedia.org/wiki/Johor%E2%80%93Jambi_wars): confirmed: a pro-Johor rebellion forced Jambi out of Tungkal in 1655 (the Jambi page agrees)
- /ledger/3 (https://en.wikipedia.org/wiki/Johor%E2%80%93Jambi_wars): confirmed: May 1667, a Johorese fleet at the mouth of the Jambi River
- /ledger/5 (https://en.wikipedia.org/wiki/Johor%E2%80%93Jambi_wars): not on page for year and land: the recapture of Kuala Tungkal and Indragiri is undated (honestly confidence 1), the page never says Jambi held Indragiri, and the infobox says status quo ante bellum
- /ledger/6 (https://en.wikipedia.org/wiki/Jambi_Sultanate): confirmed: 1688, the VOC deposed Ingalaga; Lower Jambi (Tanah Pilih, Kiai Gede) and Upper Jambi (Pringgabaya, under Pagaruyung's influence)
- /ledger/7 (https://en.wikipedia.org/wiki/Jambi_Sultanate): confirmed: 1708 arrangement, Kiai Gede gave up authority to Pringgabaya
- /ledger/9 (https://en.wikipedia.org/wiki/Jambi_Sultanate): confirmed: annexed into the Palembang Residency in 1903; Taha's killing in 1904 ended the sultanate; infobox disestablished 1904

Area: infobox None, Cliopatria 27696.8, ratio None. The Jambi Sultanate infobox has no area, only an 1852 population of about 60,000 (checked). K1 says so.

## bali: fix

- **/wars/2** (applied by reviewer): The war behind the 1894 loss of Karangasem (/ledger/4), the Dutch defeat of the Balinese ruler of Lombok, was missing from wars[].
  - Evidence: History of Bali page, 1894: the Dutch defeated the Balinese ruler of Lombok, 'adding both Lombok and Karangasem to their possessions'. Reviewer rule 10: each war in the sources appears, with zones where ground changed hands.
  - Fix: Added wars entry 'Dutch intervention in Lombok and Karangasem (1894)', 1894-1894, belligerents dutch-east-indies and bali, with zone Amlapura 25 km (the same spec as /ledger/4). Re-validated: 0 errors.

Thin items, for a gap-filler:
- /ledger (no vassal events): Balinese (Buleleng, later Mengwi) suzerainty over Blambangan from 1697 until the VOC in 1768. The blambangan-kingdom dossier (wars/3, notes) says 'rejoined Bali in 1697' (Mataram page) and asks this dossier to carry it. The History of Bali page has no 1697 event (checked). Page to try: https://en.wikipedia.org/wiki/Blambangan_Kingdom
- /keyframe_review/3: When Tabanan (1906), Gianyar, Bangli and Mengwi lost independence. Both pages opened are silent, so they stay in until 1908. Page to try: https://en.wikipedia.org/wiki/Dutch_intervention_in_Bali_(1906)
- /notes (Lombok): The start of Balinese (Karangasem) rule on western Lombok, and who holds Lombok 1683-1894. The balinese-kingdom dossier /ledger/6 gives Lombok to 'bali' in 1683, but this dossier begins in 1687 and draws no Lombok. Page to try: https://en.wikipedia.org/wiki/Dutch_intervention_in_Lombok_and_Karangasem
- /wars: The 1868 fifth Dutch expedition against Ida Mahe Rai's rebellion, which is on the History of Bali page. It was fought in Dutch-held Buleleng and moved no Balinese land, so it is optional. Page to try: https://en.wikipedia.org/wiki/History_of_Bali

Spot checks:
- /ledger/0 (https://en.wikipedia.org/wiki/History_of_Bali): confirmed: Gelgel broke up after 1651; new seat at Klungkung in 1686; nine kingdoms named as in the note
- /ledger/1 (https://en.wikipedia.org/wiki/History_of_Bali): confirmed: three expeditions between 1846 and 1849
- /ledger/3 (https://en.wikipedia.org/wiki/History_of_Bali): confirmed: 1849, Bangli helped; the Dutch took control of Buleleng and Jembrana
- /ledger/4 (https://en.wikipedia.org/wiki/History_of_Bali): confirmed: 1894, 'adding both Lombok and Karangasem to their possessions'
- /ledger/5 (https://en.wikipedia.org/wiki/History_of_Bali): confirmed: 1906, assaults at Sanur, elimination of the Badung royal house, about 1,000 dead
- /ledger/6 (https://en.wikipedia.org/wiki/History_of_Bali): confirmed: 1908, assault on Klungkung, 'the total rule of the Dutch over Bali'

Area: infobox 5582.83, Cliopatria 7719.0, ratio 0.72. The Bali infobox gives 5,582.83 km2 for the modern province (no year); the body gives 5,590.15 km2 including offshore islands. Against the 1687 shape the ratio is 0.72, within a factor of two, and K0 states it (as 1.38).

## Cross-dossier matrix

- kutai-kingdom 1635 gain (counterpart kutai-martadipura) -> mirror: none. **exception**: No dossier yet; listed in the author's counterparts_needing_dossiers (se-02-x additions).
- kutai-kingdom 1844 loss (counterpart dutch-east-indies) -> mirror: none. **exception**: dutch-east-indies is owned by se-03, which has not run yet. It should also carry the post-1844 vassal tint for Kutai.
- majapahit 1362 vassal_start (counterpart Kalimantan principalities (Negara Dipa, Tanjungpura, Kutai)) -> mirror: kutai-kingdom None None. **exception**: The schema records vassalage on the suzerain's side only. The Kutai dossier (from 1300) is silent on Majapahit's 1362-1406 tributary claim; for information only.
- sultanate-of-jambi 1655 loss (counterpart sultanate-of-johor) -> mirror: sultanate-of-johor 1655 gain. **matched**: Tungkal; same 60 km disc on both sides.
- sultanate-of-jambi 1667 contest_start (counterpart sultanate-of-johor) -> mirror: sultanate-of-johor 1667 contest_start. **matched**: May 1667 on both sides. Both zones include the whole Batang Indragiri buffer, which both sides should shrink.
- sultanate-of-jambi 1681 contest_end (counterpart sultanate-of-johor) -> mirror: sultanate-of-johor 1679 contest_end. **mismatch**: Jambi has 1681 (confidence 1, the war-page infobox's fourth war 1680-1681); Johor has 17 Oct 1679 (confidence 3, 'Daeng Mangika fled to Palembang'). The WebFetch extract of the Johor-Jambi wars page does not show that date. Reconcile on the Johor side.
- sultanate-of-jambi 1681 gain (counterpart sultanate-of-johor) -> mirror: none. **missing**: Johor has no loss of Tungkal after 1655. Jambi's gain region is also too wide (Indragiri). Once Jambi limits it to Tungkal, Johor needs a c. 1681 loss of Tungkal, or both should say the recapture is undated.
- sultanate-of-jambi 1688 split (counterpart Upper Jambi (Pangeran Pringgabaya)) -> mirror: none. **exception**: An internal division with no dossier. Reunited by the 1708 merge.
- sultanate-of-jambi 1904 loss (counterpart dutch-east-indies) -> mirror: none. **exception**: se-03 has not run. The 1833/1858-1904 protectorate also belongs in the dutch-east-indies dossier.
- sultanate-of-jambi 1642 vassal (recorded in notes; belongs to the suzerain) (counterpart mataram-sultanate) -> mirror: mataram-sultanate None vassal_start missing. **missing**: Jambi page: Pangeran Ratu accepted Mataram's overlordship in 1642 and Jambi broke away in 1663/64. mataram-sultanate has no Jambi vassal events, only a mention in its 1622 Sukadana note. Route to the Mataram owner. The Jambi notes flag it.
- bali 1687 found (counterpart balinese-kingdom) -> mirror: balinese-kingdom 1686 dissolve. **matched**: balinese-kingdom ends in 1686 and lists bali as its successor.
- balinese-kingdom 1683 loss (counterpart bali) -> mirror: none. **mismatch**: Gelgel gives Lombok to 'bali' in 1683 (confidence 1), but bali begins in 1687 and no bali keyframe holds Lombok. Either the Gelgel event's counterpart becomes karangasem-lombok (a new dossier, as the bali author proposes), or bali gains western Lombok. Route to se-02-x and the Gelgel owner.
- blambangan-kingdom 1697 war wars/3 and notes (Balinese suzerainty) (counterpart bali) -> mirror: bali None vassal_start missing. **missing**: blambangan-kingdom wars/3 and notes: Buleleng's 1697 expedition, 'rejoined Bali in 1697' (Mataram page). They ask the bali dossier to carry Balinese suzerainty until 1768. bali has no vassal_start. The History of Bali page is silent, so this is recorded as a thin item for a gap-filler.
- bali 1849 loss (counterpart dutch-east-indies) -> mirror: none. **exception**: se-03 has not run. The same holds for the 1846/1849 contest and the 1894, 1906 and 1908 losses.

## Gazetteer names needed

- Kutai Lama (place, kutai-kingdom)
- Muara Kaman (place, kutai-kingdom)
- Amlapura (place, bali)
- Kuala Tungkal (place, sultanate-of-jambi)

## Problems

- Reviewer edits applied, each re-validated with 0 errors: kutai-kingdom /ledger/0/note and /keyframe_review/0/note reworded; bali /wars/2 added (the 1894 Lombok-Karangasem war).
- The Muara Kaman Wikipedia page gives no coordinates, so the Kutai overlap test uses the author's own approximate Muara Kaman coordinates (116.7 E, 0.2 S).
- The Johor dossier's contest_end of 17 October 1679 (confidence 3) does not appear in the WebFetch extract of the Johor-Jambi wars page. Whoever reviews Johor should recheck it.
- Of the context polities, only sultanate-of-palembang, sultanate-of-johor and blambangan-kingdom have dossiers. dutch-east-indies, dutch-republic, riau-lingga-sultanate, batavian-republic, qajar-dynasty and british-colonial-empire belong to groups that have not run yet. balinese-kingdom, mataram-sultanate and majapahit were read as well, because the ledgers name them.
