# Review af-03-b (Sahel empires, part b)

Reviewed 2026-10-19 by the adversarial reviewer. Inputs read: the author's brief, the author's report (notes/phase-b/reports/af-03-b.json) and the author's notes (_notes/af-03-b.md). Neighbour ledgers read: empire-of-kanem (which holds the Bornu Empire row), funj-sultanate, mali-empire, mahdist-state and saadi-sultanate. The other Context polities have no dossier yet.

Mechanical check: all six dossiers validate with `--resolve` (0 errors, 0 unresolved names). The only warnings are counterpart slugs with no dossier yet: dendi-kingdom, pashalik-of-timbuktu, tukulor-empire, tunjur-kingdom, bagirmi-sultanate. All are listed for af-03-x.

Spot checks: 41 events opened on 11 pages, weighted towards confidence-3 events and the largest moves. All confirmed except wadai-empire /ledger/3, whose note misreads the page (confidence 1). No fabricated or mis-dated confidence-3 event was found.

Verdicts: songhai-empire thin; sokoto-caliphate thin (two small fixes applied by the reviewer); bamana-empire thin; massina-empire pass; wadai-empire thin; sultanate-of-darfur thin. "Thin" here means valid, with dated pages behind every confidence-3 event, and a list of unapplied, non-blocking fixes and gaps for a gap-filler. No dossier fails.

## songhai-empire: thin

- Area: infobox 1400000 (1528), Cliopatria 629260, ratio 0.45. Discussed in keyframe_review/5: Aïr and Taghaza are added, the rest is read as tributary influence, and 800,000 km2 (1550) is within range.
- **Fix (not applied)** `/keyframe_review/1/correction and /ledger/2`: Mema is gained in 1464 (ledger/2), but the keyframe that covers 1464-1467 leaves Mema out, so the map shows the land in neither Songhai nor Mali from 1465 to 1467. Evidence: ledger/2 region is the difference of Mali's 1463 and 1468 shapes. keyframe_review/1 is the Cliopatria 1463 shape plus Dendi only, and its own note says Mema 'enters the Cliopatria shape only at 1468'. mali-empire ledger/13 loses Mema in 1465 ('conquered Mema ... in 1465', Mali page). Fix: Either add ledger/2's region to keyframe_review/1's correction union (and set ledger/2 to 1465 to match mali-empire), or move ledger/2 to 1468 at confidence 1. Not blocking.
- **Fix (not applied)** `/ledger (Taghaza) and /keyframe_review/6/correction`: Songhai draws Taghaza to 1590, but the saadi-sultanate dossier occupies it in 1556-1557 and takes it in 1586. Songhai has no mirror for either event, so both states draw Taghaza from 1586 to 1590. Evidence: saadi-sultanate ledger/12-13 (occupation_start 1556 / occupation_end 1557, counterpart songhai-empire) and ledger/15 (gain 1586, counterpart songhai-empire), citing the Taghaza and Pashalik pages. The author's notes say the Songhai pages do not date these events. Fix: Add occupation_start 1556 and occupation_end 1557 (counterpart saadi-sultanate, the Taghaza disc), and a loss in 1586 (counterpart saadi-sultanate). Source: https://en.wikipedia.org/wiki/Taghaza. Then drop Taghaza from keyframe_review/6 from 1586 on, or split that keyframe. Not blocking: a gap-filler can do it.
- Thin `/ledger/9`: The Askia gain of Taghaza is undated (confidence 1), and so are the Saadi occupations of 1556-57 and 1586 (see fixes). Page to try: https://en.wikipedia.org/wiki/Taghaza
- Thin `/ledger/10 and /keyframe_review/6`: The 1564 western strip to the Senegal coast (+36,000 km2) is a confidence-1 bridge. Page to try: https://en.wikipedia.org/wiki/Askia_Daoud
- Thin `/ledger/1`: There is no date for Dendi joining the empire. The year is a confidence-1 bridge at Sunni Ali's accession. Page to try: https://en.wikipedia.org/wiki/Dendi_Kingdom
- Thin `/ledger/5`: The 1475 Sahel gain from Mali, the largest move (+378,000 km2), is a confidence-1 bridge. Page to try: https://en.wikipedia.org/wiki/Sunni_Ali
- Thin `/keyframe_review/5`: The Hausaland conquests of about 1512-1514 (Katsina, Zaria, Kano) and the 1516 Kebbi revolt are not mapped. The infobox gives 1,400,000 km2 against Cliopatria's 629,260 km2. The author acknowledges the gap and reasons it through. Page to try: https://en.wikipedia.org/wiki/Hausa_Kingdoms
- Spot check `/ledger/3` (https://en.wikipedia.org/wiki/Songhai_Empire): confirmed: 'He annexed Timbuktu in 1468 after the leaders of the town asked him to help overthrow the Tuaregs'
- Spot check `/ledger/6` (https://en.wikipedia.org/wiki/Askia_Mohammad_I): confirmed: 'Ture defeated Baru at the Battle of Anfao in April 1493'
- Spot check `/ledger/7` (https://en.wikipedia.org/wiki/Askia_Mohammad_I): confirmed: 'In 1501 he ... sacked and captured Diafunu'
- Spot check `/ledger/8` (https://en.wikipedia.org/wiki/Askia_Mohammad_I): confirmed: '1515 saw another campaign against Agadez, reinforcing the Songhai position there'
- Spot check `/ledger/11` (https://en.wikipedia.org/wiki/Battle_of_Tondibi): confirmed: 'On 13 March 1591, the armies met at ... Tondibi'

## sokoto-caliphate: thin

- Area: infobox 488500 (1900), Cliopatria 792270, ratio 1.62. Within a factor of two. keyframe_review/4 quotes the infobox figure.
- **Fix (applied by reviewer)** `/identity/capitals/1/to`: The capital Sokoto ended in 1902, so the state's last months (to 13 March 1903) had no capital. Evidence: Sokoto page: 'On 13 March 1903, at the grand market square of Sokoto, the last Vizier of the Caliphate officially conceded to British Rule'. The infobox gives Sokoto 1851-1902. Fix: Set to 1903 and add a review note. The file re-validates with 0 errors.
- **Fix (applied by reviewer)** `/ledger/19/confidence`: The dissolve event had confidence 3 although it gives the whole 1900 outline to british-africa, while the page divides the land between three powers. Evidence: Sokoto page: 'It was dissolved when the British, French, and Germans conquered the area in 1903'. The dossier's own successors list french-africa for the Niger part. Fix: Lowered to 2 with a review note. The file re-validates with 0 errors.
- **Fix (not applied)** `/ledger/19/region and /keyframe_review/10-11`: The French and German parts of the 1895-1903 outline go to british-africa in 1903. These are Liptako and Dori in Burkina Faso, the Niger strip, and eastern Adamawa in Cameroon. Evidence: Shapes 1895 and 1900 reach -0.26 E and 15.2 N and into Cameroon. The page says the British, French and Germans conquered the area. The author's notes list the French and German takeovers as 'not on any page opened'. Fix: Restrict the dissolve region to the Nigerian intersect. Add dated losses to french-africa (the Niger and Burkina parts) and german-africa (Adamawa east of the 1901 line), or bridge them at confidence 1 with nobody until af-08 runs. Not blocking.
- Thin `/ledger/11`: Zamfara, Zazzau, Bauchi, Gombe and Adamawa enter in one confidence-1 bridge in 1809. This is the largest move (about 350,000 km2). Page to try: https://en.wikipedia.org/wiki/Adamawa_Emirate
- Thin `/ledger/14`: The 1834 western step to Dori, Gurma and Liptako (+162,000 km2) is a confidence-1 bridge. Page to try: https://en.wikipedia.org/wiki/Liptako
- Thin `/ledger/15 and /ledger/16`: The years Oyo-Ile was burned and abandoned are confidence-1 bridges. The Ilorin page gives 1838 for the end of expansion, while the loss is dated 1840. Page to try: https://en.wikipedia.org/wiki/Oyo_Empire
- Thin `/keyframe_review/5`: The 1820 step (+16,000 km2 on the south-western edge) has no ledger event. It is small, but no page explains it. Page to try: https://en.wikipedia.org/wiki/Gwandu_Emirate
- Thin `/keyframe_review/10-11`: Dates of the French and German conquests of the caliphate's fringes, 1895-1903. Page to try: https://en.wikipedia.org/wiki/Voulet%E2%80%93Chanoine_Mission
- Spot check `/ledger/0` (https://en.wikipedia.org/wiki/Sokoto_Caliphate): confirmed: infobox 'Founded: 21 February 1804'
- Spot check `/ledger/6` (https://en.wikipedia.org/wiki/Sokoto_Caliphate): confirmed: 'tried to conquer Borno ... in 1808. They burnt the capital, Ngazargamu'
- Spot check `/ledger/9` (https://en.wikipedia.org/wiki/Fulani_War): confirmed: 'transformed the semi-permanent camp of Sokoto into a city in 1809'
- Spot check `/ledger/18` (https://en.wikipedia.org/wiki/Sokoto_Caliphate): confirmed: 'On 13 March 1903 ... the last Vizier ... conceded to British Rule'
- Spot check `/ledger/2 and /ledger/7` (https://en.wikipedia.org/wiki/Fulani_War): confirmed: Kebbi 'In 1805'; 'In 1808, the jihadists assaulted Gobir, killing Yunfa in the battle of Alkalawa'
- Spot check `/ledger/3-5` (https://en.wikipedia.org/wiki/Sokoto_Caliphate): confirmed: Katsina, Daura and Kano 'in 1807'; Nupe 'fell to the Sokoto forces c. 1808'

## bamana-empire: thin

- Area: infobox None (None), Cliopatria 104716, ratio None. The infobox gives no area (checked).
- **Fix (not applied)** `/ledger/2 and /ledger/9`: The 1751 vassalage of 'the Mansa of the rump-state Mali Empire' names mali-empire, whose dossier ends in 1610. Its region is Cliopatria's 1609 Mali shape (128,538 km2 in Guinea and Mali), so a 110-year vassal overlay is drawn over a state that no longer exists. Evidence: Bamana page: 'In 1751 he also conquered Niani, making the Mansa of the rump-state Mali Empire a vassal.' mali-empire.json ends in 1610 with dissolve: 'No single Keita ever ruled Manden after Mahmud Keita IV's death'. The author's notes flag the conflict. Fix: Use a counterpart for the Manden remnant (for example 'kingdom-of-kangaba', listed for a dossier) and a small region at Niani or Kangaba (a 60-100 km disc), not the 1609 Mali shape. Keep ledger/9 at confidence 1 or end it with a source. Not blocking.
- **Fix (not applied)** `/ledger/7/region`: The 1818 loss gives the whole 1803 outline outside Ségou (the Niger bend, Timbuktu, Hombori-Seno) to massina-empire. massina-empire gains only Mopti and Djenné in 1818, and the rest only in 1826, from other counterparts. Evidence: massina-empire ledger/0 (found 1818, region Mopti admin1 plus Djenné) and ledger/1-2 (1826, Timbuktu from the Tuareg, the rest from 'Dogon, Fulbe and Tuareg lands'). Massina page: 'in 1826/7 conquered Timbuktu'. As written, 1818-1825 draws that land in neither state. Fix: Split ledger/7: give massina-empire the Mopti/Djenné region of massina ledger/0, and give the rest of the 1803 outline outside Ségou to nobody (or to the Tuareg of Timbuktu for the Timbuktu disc). Alternatively, massina-empire could gain all of it from bamana-empire in 1818. Not blocking.
- Thin `/ledger/1, /ledger/3, /ledger/5`: The Timbuktu hold years of 1748, 1752 and 1769 are confidence-1 bridges to Cliopatria steps. Page to try: https://seshat-db.com/core/polity/ml_bamana_k/
- Thin `/ledger/6`: The 1803 expansion (+70,000 km2: Massina, the Dogon country, the Niger bend) is a confidence-1 bridge. Page to try: https://en.wikipedia.org/wiki/Mansong_Diarra
- Thin `/keyframe_review/7`: The extent of the Ségou state from 1818 to 1861 is a 100 km disc, and no page gives an extent. Page to try: https://en.wikipedia.org/wiki/Ségou
- Thin `/identity/rulers`: There is no rulers strip, although the Bamana page has a ruler list. Page to try: https://en.wikipedia.org/wiki/Bamana_Empire
- Spot check `/ledger/0` (https://en.wikipedia.org/wiki/Bamana_Empire): confirmed: 1712, Mamari Kulubali chosen to lead the ton; infobox 1712-1861
- Spot check `/ledger/2` (https://en.wikipedia.org/wiki/Bamana_Empire): confirmed on the page ('In 1751 he also conquered Niani, making the Mansa of the rump-state Mali Empire a vassal'); the counterpart and region are wrong (see fixes)
- Spot check `/ledger/4` (https://en.wikipedia.org/wiki/Bamana_Empire): confirmed: 'In 1766, ... Ngolo Diarra seized the throne'
- Spot check `/ledger/7` (https://en.wikipedia.org/wiki/Bamana_Empire): confirmed: 'At the Battle of Noukouma in 1818, Bambara forces ... were defeated'; the land assigned is the issue
- Spot check `/ledger/8, /ledger/10-11` (https://en.wikipedia.org/wiki/Bamana_Empire): confirmed: 'Tall took Nyamina without a fight on May 25, 1860'; 'Ségou itself fell on March 10, 1861'

## massina-empire: pass

- Area: infobox None (None), Cliopatria 104716, ratio None. The infobox gives no area (checked). The Cliopatria 1822 outline is the Bamana 1803 outline; the Ségou cut is acknowledged.
- Thin `/ledger/2`: The outline beyond the Djenné-Mopti heartland and Timbuktu (Fakala-Kunari, Hayre-Seno, Nabbe-Dude) enters by a confidence-1 bridge in 1826. This is thin by design within the 1-2 page budget. Page to try: https://en.wikipedia.org/wiki/Seku_Amadu
- Thin `/identity/capitals/0/from`: Hamdullahi is the capital from 1818, but the Massina page says 'In 1820 Ahmadu established a new capital at Hamdullahi'. The seat for 1818-1819 (Noukouma or Sebera?) is not given. The note acknowledges this. Page to try: https://en.wikipedia.org/wiki/Hamdullahi
- Spot check `/ledger/0` (https://en.wikipedia.org/wiki/Massina_Empire): confirmed: 'founded by Seku Amadu in 1818'; 'taking Djenné in 1818'
- Spot check `/ledger/1` (https://en.wikipedia.org/wiki/Massina_Empire): confirmed: 'in 1826/7 conquered Timbuktu'
- Spot check `/ledger/3-4` (https://en.wikipedia.org/wiki/Massina_Empire): confirmed: Tuareg 'drove off the Massina garrison in 1840'; starved into submission 'by 1846'
- Spot check `/ledger/6-7` (https://en.wikipedia.org/wiki/Massina_Empire): confirmed: 1862, 'he entered Hamdullahi on 16 May, levelling it'

## wadai-empire: thin

- Area: infobox None (None), Cliopatria 279943, ratio None. The infobox gives no area (checked).
- **Fix (not applied)** `/ledger/3`: The note says that after the 1805 campaign 'no occupation or tribute is described afterwards (page silent)', but the page says Bagirmi became a tributary and that Sharif later enforced it. The relation is entered as a one-year contest instead of a vassalage. Evidence: Wadai Empire page: 'In 1805 Wadai conquered Bagirmi, killed its ruler, and captured and sold 20,000 people into slavery. Bagirmi was reduced to a tributary.' Also: Sharif sacked Kukawa 'in 1846 and enforc[ed] Bagirmi's tributary status'. The event is at confidence 1, so this does not count as a fail. Fix: Replace ledger/3 (contest_end) with a vassal_start in 1805, counterpart bagirmi-sultanate, region Baguirmi, confidence 2, quoting the sentence. Add a vassal_end, bridged at confidence 1 to the French protectorate over Bagirmi (1897; page to try https://en.wikipedia.org/wiki/Kingdom_of_Baguirmi). Keep the contest_end in 1805.
- **Fix (not applied)** `/ledger (Darfur suzerainty)`: Wadai carries no mirror of the sultanate-of-darfur vassal events: Wadai tributary to Darfur in the 17th century, and Darfur installing Sharif for tribute in 1838. Evidence: sultanate-of-darfur ledger/2-3 (vassal_start 1636 / vassal_end 1700, counterpart wadai-empire) and ledger/7-8 (1838/1839). Wadai page: 'Throughout the 17th century, Wadai was a tributary of the Darfur'; 'Darfur took advantage of a disputed political succession in 1838 to put its own candidate' in return for tribute; 'Sharif quickly regained Wadai's independence'. Wadai's own wars[0] outcome already says this. Fix: Add vassal_start 1636 (confidence 1) and vassal_end 1700 (confidence 2), and vassal_start 1838 (confidence 3) and vassal_end 1839 (confidence 1), all with counterpart sultanate-of-darfur, a region matching the keyframe of those years, and source https://en.wikipedia.org/wiki/Wadai_Empire.
- Thin `/ledger/1`: Sabun's southward expansion (Dar Sila, Dar Runga) and the later control of Dar al Kuti are one confidence-1 bridge in 1804 for about 190,000 km2. Three of the five budgeted pages are unused. Page to try: https://en.wikipedia.org/wiki/Dar_al_Kuti
- Thin `/identity/capitals/1/from`: The year Sharif moved the capital to Abéché is bridged to 1838. Page to try: https://en.wikipedia.org/wiki/Abéché
- Spot check `/ledger/0` (https://en.wikipedia.org/wiki/Wadai_Empire): confirmed: 1635, the Maba rallied to Abd al-Karim and overthrew the Tunjur king Daud
- Spot check `/ledger/2` (https://en.wikipedia.org/wiki/Wadai_Empire): confirmed: 'In 1805 Wadai conquered Bagirmi, killed its ruler'
- Spot check `/ledger/3` (https://en.wikipedia.org/wiki/Wadai_Empire): not on page: the note's 'no ... tribute is described afterwards (page silent)' is contradicted by 'Bagirmi was reduced to a tributary.'
- Spot check `/ledger/4` (https://en.wikipedia.org/wiki/Wadai_War): confirmed: 'heavy defeats on Wadaian forces at Dokotchi on 29 May 1908'
- Spot check `/ledger/5` (https://en.wikipedia.org/wiki/Wadai_War): confirmed: 'occupy Abéché on 2 or 12 June 1909'
- Spot check `/ledger/6, /ledger/8` (https://en.wikipedia.org/wiki/Wadai_War): confirmed: 'forcing Dud Murra to surrender in October 1911'; 'Wadai was completely occupied by the French in 1912'

## sultanate-of-darfur: thin

- Area: infobox None (None), Cliopatria 296630, ratio None. The infobox gives no area (checked).
- **Fix (not applied)** `/ledger/2/region and /ledger/3/region`: The 1636-1700 vassalage of Wadai is drawn over Cliopatria's full 280,000 km2 Wadai outline, while the wadai-empire dossier holds only the Maba heartland until 1804. Evidence: wadai-empire keyframe_review/0 (1635-1803) is the intersect of the Cliopatria 1636 Wadai shape with the Wadai region. The rest of the outline enters only with wadai ledger/1 (1804). Fix: Set the region of ledger/2 and ledger/3 to {"intersect": [{"cliopatria": "Wadai Empire", "year": 1636}, {"region": "Wadai"}]}. Not blocking.
- Thin `/ledger/1`: Daali's state before 1609 and the 1609 outline (+about 250,000 km2) are a confidence-1 bridge, and Sulayman Solong's dates are unsettled. Page to try: https://en.wikipedia.org/wiki/Sulayman_Solong
- Thin `/keyframe_review/7`: The extent of Ali Dinar's restored sultanate (1898-1916) reuses the 1873 outline. The Dar Masalit and Dar Tama borderlands disputed with Wadai and France are not dated. Page to try: https://en.wikipedia.org/wiki/Anglo-Egyptian_Darfur_Expedition
- Thin `/ledger/8`: The end of the 1838 suzerainty over Wadai is bridged to 1839. Page to try: https://en.wikipedia.org/wiki/Wadai_Empire
- Spot check `/ledger/4` (https://en.wikipedia.org/wiki/Sultanate_of_Darfur): confirmed: 'Around 1785 the Funj withdrew from Kordofan ... and the elderly Tayrab launched an invasion'
- Spot check `/ledger/5` (https://en.wikipedia.org/wiki/Sultanate_of_Darfur): confirmed: Abd al-Rahman 'established a new capital at al-Fashir' in 1792
- Spot check `/ledger/6` (https://en.wikipedia.org/wiki/Sultanate_of_Darfur): confirmed: 'routed by the Egyptians near Bara on 19 August 1821'
- Spot check `/ledger/7` (https://en.wikipedia.org/wiki/Wadai_Empire): confirmed: 'Darfur took advantage of a disputed political succession in 1838 to put its own candidate'
- Spot check `/ledger/9` (https://en.wikipedia.org/wiki/Sultanate_of_Darfur): confirmed: 'slain in the Battle of al-Manawashi in the autumn of 1874'
- Spot check `/ledger/10, /ledger/13` (https://en.wikipedia.org/wiki/Ali_Dinar): confirmed: infobox 'Reign: September 1898 – 6 November 1916' (the lead's 1891 ascension is noted by the author)

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| songhai-empire 1435 found (mali-empire) | mali-empire 1435 loss | matched | Gao leaves Mali c. 1430s; both sides use 1435. |
| songhai-empire 1464 gain (mali-empire) | mali-empire 1465 loss | matched | Mema, within one year (Songhai 1464, Mali 1465). See the Songhai keyframe fix: the land is drawn by neither state from 1465 to 1467. |
| songhai-empire 1475 gain (mali-empire) | mali-empire 1475 loss | matched | Both confidence 1 and bridged to the Cliopatria step. |
| songhai-empire 1501 gain (mali-empire) | mali-empire 1502 loss | matched | Diafunu, within one year (Askia page 1501, Mali page 1502). Mali's 1475 shape also lacks Diafunu (author's note), so a gap-filler should keep it in Mali until 1501. |
| mali-empire 1300 gain (songhai-empire) | -   | mismatch | songhai-empire starts in 1435, so it cannot lose Gao in 1300. The mali-empire counterpart should be a kingdom-of-gao or nobody (already raised in review af-03-a). |
| songhai-empire 1468 gain (Tuareg of Timbuktu) | -   | exception | No dossier yet. Listed in the author's counterparts_needing_dossiers (tuareg-of-timbuktu). |
| songhai-empire 1515 gain (Sultanate of Agadez) | -   | exception | No dossier yet. Listed (sultanate-of-agadez, af-03-x). |
| saadi-sultanate 1556 occupation_start (songhai-empire) | songhai-empire   | missing | Taghaza: the Saadi occupation of 1556-57 has no mirror in songhai-empire. |
| saadi-sultanate 1586 gain (songhai-empire) | songhai-empire   | missing | Taghaza: no 1586 loss in songhai-empire, whose keyframe_review/6 keeps Taghaza to 1590. |
| songhai-empire 1591 contest_start (saadi-sultanate) | saadi-sultanate 1591 contest_start | matched | Tondibi, 13 March 1591. |
| songhai-empire 1591 loss (saadi-sultanate) | saadi-sultanate 1591 gain | matched | Gao and Timbuktu. Saadi dates Timbuktu to 30 May 1591. |
| songhai-empire 1592 loss (saadi-sultanate) | saadi-sultanate 1592 gain | matched | Djenné. Songhai has it at confidence 1, Saadi at confidence 3. |
| songhai-empire 1599 dissolve (dendi-kingdom) | -   | exception | No dossier yet. Listed (dendi-kingdom, af-03-x). |
| sokoto-caliphate 1808 contest_start (empire-of-kanem) | empire-of-kanem 1808 contest_start | matched | Ngazargamu burnt in 1808 (both confidence 3). |
| sokoto-caliphate 1809 gain (empire-of-kanem) | empire-of-kanem 1809 loss | matched | Same region: the difference of the Bornu 1808 and 1809 shapes. |
| sokoto-caliphate 1827 contest_end (empire-of-kanem) | empire-of-kanem 1827 contest_end | matched | Both bridged to 1827 at confidence 1. |
| sokoto-caliphate 1824 gain (oyo-empire) | -   | exception | oyo-empire is owned by af-04, which has not run yet. It should carry the loss of Ilorin in 1824. |
| sokoto-caliphate 1836 gain (oyo-empire) | -   | exception | af-04 has not run. Oyo-Ile, confidence 1. |
| sokoto-caliphate 1805 gain (Kingdom of Kebbi) | -   | exception | Listed (kingdom-of-kebbi). The Katsina, Kano, Nupe and Gobir gains of 1807-1808 are listed in the same way. |
| sokoto-caliphate 1903 dissolve (british-africa) | -   | exception | british-africa is owned by af-08, which has not run. The French and German parts should go to french-africa and german-africa (see fixes). |
| bamana-empire 1751 vassal_start (mali-empire) | mali-empire   | mismatch | mali-empire ends in 1610, so the vassal has no dossier in 1751. The counterpart should be the Manden or Kangaba remnant. |
| bamana-empire 1818 loss (massina-empire) | massina-empire 1818 found | mismatch | The years agree. The land does not: Bamana gives away the whole 1803 outline outside Ségou, but Massina takes only Mopti and Djenné in 1818 and the rest in 1826 from other counterparts. |
| bamana-empire 1748 gain (pashalik-of-timbuktu) | -   | exception | No dossier yet. Listed (pashalik-of-timbuktu); the same applies to the 1752 loss and the 1769 gain. |
| bamana-empire 1861 dissolve (tukulor-empire) | -   | exception | No dossier yet. Listed (tukulor-empire, af-03-x); the same applies to the 1860 contest. |
| massina-empire 1826 gain (Tuareg of Timbuktu) | -   | exception | Listed (tuareg-of-timbuktu). |
| massina-empire 1862 dissolve (tukulor-empire) | -   | exception | Listed (tukulor-empire). |
| wadai-empire 1635 found (tunjur-kingdom) | -   | exception | Listed (tunjur-kingdom, af-03-x). |
| wadai-empire 1805 contest_start (bagirmi-sultanate) | -   | exception | Listed (bagirmi-sultanate). Should become a vassal_start (see fixes). |
| wadai-empire 1912 dissolve (french-africa) | -   | exception | french-africa is owned by af-08, which has not run. The same applies to the 1908-1912 contest and occupation. |
| sultanate-of-darfur 1636 vassal_start (wadai-empire) | wadai-empire   | missing | Wadai has no vassal_start with sultanate-of-darfur as counterpart (same batch; see the wadai fix). |
| sultanate-of-darfur 1838 vassal_start (wadai-empire) | wadai-empire   | missing | Wadai has no mirror for the 1838 installation of Sharif. |
| sultanate-of-darfur 1785 gain (funj-sultanate) | funj-sultanate 1785 loss | matched | Kordofan c. 1785. |
| sultanate-of-darfur 1821 loss (muhammad-ali-dynasty) | -   | exception | muhammad-ali-dynasty is owned by me-10, which has not run. The loss is Kordofan, 19 August 1821. |
| sultanate-of-darfur 1874 loss (khedivate-of-egypt) | -   | exception | khedivate-of-egypt is owned by me-10, which has not run. |
| sultanate-of-darfur 1898 gain (mahdist-state) | mahdist-state   | missing | mahdist-state (af-01) has no 1898 loss of Darfur to sultanate-of-darfur; its only 1898 loss is Omdurman to british-africa. Route to af-01. Also, Darfur's page dates the Mahdist conquest to 1885, the mahdist-state dossier to 1883. |
| sultanate-of-darfur 1916 dissolve (british-africa) | -   | exception | british-africa is owned by af-08, which has not run. |
| sultanate-of-darfur 1550 found (tunjur-kingdom) | -   | exception | Listed (tunjur-kingdom). |

## Routing

- af-01 (mahdist-state): add the 1898 loss of Darfur to sultanate-of-darfur, and settle 1883 (dossier) against 1885 (Darfur page) for the Mahdist conquest.
- af-02 (saadi-sultanate): nothing to change. Songhai must mirror Taghaza 1556-57 and 1586.
- af-03-a (mali-empire): the 1300 gain of Gao names songhai-empire, which starts in 1435. Diafunu should stay in Mali's shape until 1501/1502.
- af-03-x: dossiers for dendi-kingdom, tukulor-empire, pashalik-of-timbuktu, tuareg-of-timbuktu, tunjur-kingdom, bagirmi-sultanate, the Hausa states, Kebbi/Argungu, Nupe, Agadez, Kaarta, and a Manden/Kangaba remnant (the vassal of Ségou in 1751).
- af-04 (oyo-empire): losses of Ilorin (1824) and of the Oyo-Ile core (1836, confidence 1) to sokoto-caliphate.
- af-08: french-africa gains Wadai (1909-1912) and the Niger and Burkina fringes of Sokoto; german-africa gains eastern Adamawa; british-africa gains Sokoto (1903) and Darfur (1916).
