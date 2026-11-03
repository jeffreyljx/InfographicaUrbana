# Review of batch me-10-c (Phase B, 2026-10-25)

Reviewer: adversarial review per history/briefs/reviewer-brief.md with the orchestrator's adjustments (spot-check budget 4/6, small verified fixes applied in place). Validator: all three dossiers 0 errors, 0 warnings under --resolve, before and after the reviewer's edits.

Neighbour dossiers read (ledgers grepped for counterpart events): khanate-of-bukhara, khanate-of-khiva, mughal-empire, durrani-empire, hotaki-dynasty, omani-slave-coast, dzungar-khanate, tibet; plus people-s-republic-of-zanzibar for the 1856 mirror. Not written yet (exception: group/part not run): qatar-dynasty, trucial-states, qajar-dynasty, kingdom-of-great-britain, kingdom-of-saudi-arabia, united-arab-emirates, ottoman-empire, republic-of-yemen, kuwait, house-of-khalifa, people-s-democratic-republic-of-yemen, khanates-of-the-caucasus, zand-dynasty, qasimids, kingdom-of-georgia, kingdom-of-kakheti, kingdom-of-imereti, principality-of-guria, russian-empire, safavid-dynasty, yarubid-dynasty, emirate-of-nejd, muhammad-ali-dynasty, imamate-of-yemen.

## afsharid-iran: thin

Area: infobox None km2, Cliopatria 3458881.5 km2, ratio None; Afsharid_Iran infobox has no area (re-checked); the dossier notes say so. Peak Cliopatria shape 1744.

### Fixes

- `/ledger/12` (applied by reviewer): Sindh gain (from mughal-empire) was dated 1741 at confidence 1 (Cliopatria's year) although the invasion page dates the annexation of the lands west of the Indus to May 1739. Evidence: Nader_Shah's_invasion_of_India: infobox 'Nader Shah annexes all lands west of the Indus river'; body 'left Delhi on 16 May 1739, but before they left, he ceded back all territories to the east of the Indus'. Afsharid_Iran lists Sindh among the captures of the campaign. mughal-empire /ledger/120 records the loss in May 1739. Fix: Moved to 1739-05 (now /ledger/12, was /ledger/14), confidence 2, source the invasion page, note rewritten; re-validated 0 errors 0 warnings.
- `/identity/rulers/1-3` (applied by reviewer): Adel Shah, Ebrahim Afshar and Shahrokh Shah had no source. Evidence: Afsharid_Iran infobox: '1747–1748: Adel Shah', '1748: Ebrahim Afshar', '1748–1796: Shahrokh Shah'. Fix: Added source https://en.wikipedia.org/wiki/Afsharid_Iran to the three rulers.
- `/ledger (1736-1737)` (for the author / gap-filler, non-blocking): No gain of Balkh from khanate-of-bukhara, although the Bukhara dossier records its loss to afsharid-iran. Evidence: khanate-of-bukhara /ledger/28: 1736 loss to afsharid-iran, c3, 'In 1736 it was conquered by Nader Shah.' Fix: Add a gain (1736 or 1737, counterpart khanate-of-bukhara, region Balkh) citing the page the Bukhara dossier used, or explain why Balkh is not Afsharid.
- `/ledger (1755, 1796)` (for the author / gap-filler, non-blocking): No vassal_start/vassal_end with durrani-empire for Shahrokh's Khorasan, although the Afsharid page says the state was 'subjugated to them' and durrani-empire holds the pair. Evidence: Afsharid_Iran: 'He also faced the Durrani invasions into Khorasan, eventually becoming subjugated to them in Ahmad Shah's second campaign.' durrani-empire /ledger/14 vassal_start 1755-05 (c3) and /ledger/35 vassal_end 1796 (c2), counterpart afsharid-iran. Fix: Add vassal_start 1755-05 and vassal_end 1796, counterpart durrani-empire, region Khorasan (the 1757 keyframe correction), source Shahrokh_Shah / Afsharid_Iran. The notes' view that only durrani-empire should hold it is against reviewer brief check 3 (both sides).
- `/identity/successors` (for the author / gap-filler, non-blocking): zand-dynasty is missing from successors although the 1748 loss gives it the western provinces and the infobox lists 'Zand Iran' (also 'Khanate of Kalat', 'Kingdom of Kartli-Kakheti'). Evidence: Afsharid_Iran infobox successor list as returned by WebFetch. Fix: Add zand-dynasty (land: the 1748 loss region) to successors; mention Kalat and Kartli-Kakheti in the note.
- `/ledger/5, /ledger/23` (for the author / gap-filler, non-blocking): Counterpart 'Arab rulers of Bahrain' is neither a slug nor in the report's counterparts_needing_dossiers (only in the notes). Evidence: Report counterparts_needing_dossiers lists six names, not this one. Fix: List it under counterparts_needing_dossiers (or use the Cliopatria 'Bahrain' row's slug if the group decides it covers 1736-1783).

### Thin (for a gap-filler)

- `/ledger/5, /ledger/23`: Dates of the Persian capture (1736-1738) and loss of Bahrain; Nader Shah page says Iran 'lost Bahrain to the House of Khalifa in 1783', so the 1747 loss may be wrong. Page to try: https://en.wikipedia.org/wiki/History_of_Bahrain
- `/ledger/29`: Who took the western provinces in 1747-1751 (Adel Shah, Ebrahim, Azad Khan, Karim Khan Zand); confidence-1 loss to zand-dynasty at 1748. Page to try: https://en.wikipedia.org/wiki/Adel_Shah
- `/ledger/24, /ledger/25`: End of Georgian vassalage (1747), confidence 1. Page to try: https://en.wikipedia.org/wiki/Erekle_II
- `/ledger/27, /ledger/28`: End of Khivan and Bukharan subjection in 1747, confidence 1; the khanate-of-khiva dossier quotes 'Oman and the Uzbek khanates of Bukhara and Khiva regained independence'. Page to try: https://en.wikipedia.org/wiki/Nader_Shah
- `/keyframe_review/2-3`: Balochistan/Kalat and Gulf-coast cells of the 1741 and 1744 shapes have no event. Page to try: https://en.wikipedia.org/wiki/Khanate_of_Kalat

### Spot checks

- `/ledger/1`: confirmed: infobox 'Established: 22 January 1736' (https://en.wikipedia.org/wiki/Afsharid_Iran)
- `/ledger/3`: confirmed: 'In 1738, Nader Shah conquered Kandahar, the last outpost of the Hotak dynasty' (https://en.wikipedia.org/wiki/Afsharid_Iran)
- `/ledger/7`: confirmed: Ghazni 11 June, Kabul citadel capitulated 19 June 1738 (https://en.wikipedia.org/wiki/Nader_Shah%27s_invasion_of_India)
- `/ledger/16`: confirmed: 'In 1743, he conquered Oman and its main capital Muscat.' (https://en.wikipedia.org/wiki/Afsharid_Iran)
- `/ledger/9, /ledger/10`: confirmed: entered Delhi 20 March 1739, left 16 May 1739 (https://en.wikipedia.org/wiki/Nader_Shah%27s_invasion_of_India)
- `/ledger/0`: confirmed: 'the resultant 1736 Treaty of Constantinople forced the Ottomans to confirm Iranian suzerainty' (https://en.wikipedia.org/wiki/Afsharid_Iran)
- `/ledger/12 (was /ledger/14)`: mis-dated (confidence 1): annexation west of the Indus is May 1739, not 1741; fixed by reviewer (https://en.wikipedia.org/wiki/Nader_Shah%27s_invasion_of_India)

## emirate-of-diriyah: thin

Area: infobox None km2, Cliopatria 2281665.6 km2, ratio None; Emirate_of_Diriyah has no infobox area (re-checked); keyframe notes 0 and 17 say so. Peak Cliopatria shape 1811.

### Fixes

- `/ledger/11` (applied by reviewer): Bahrain vassal_start dated 1802 at confidence 2, but the page's only 1802 is Muscat's capture of Bahrain; the Saudi recapture is undated. Evidence: Abdulaziz_bin_Muhammad_Al_Saud: 'In 1802 Bahrain was invaded and captured by the ruler of Muscat.' ... 'Abdulaziz bin Muhammad recaptured it in addition to Qatar and appointed there a governor, Abdullah bin Ufaysan'. No year for the recapture. Fix: Confidence lowered to 1 and the note extended; re-validated 0 errors 0 warnings.
- `/ledger/29/region` (for the author / gap-filler, non-blocking): The dissolve region is the raw Cliopatria 1815 shape, which still holds Al-Qassim (lost in 1817, /ledger/26) and the Buraimi oasis. Evidence: /keyframe_review/21 correction removes Al Quassim; Wahhabi_War: 'By 1817, the armies had overrun Rass, Buraida and Unayza.' shapes.csv emirate-of-diriyah_1815 bbox east to 56.50 E (Buraimi). Fix: Use the corrected shape: {minus:[{cliopatria:'Emirate of Diriyah',year:1815},{admin1:'Al Quassim',country:'Saudi Arabia'}]}; decide who takes Buraimi in 1818 so that sultanate-of-oman /ledger/8 can mirror it.

### Thin (for a gap-filler)

- `/keyframe_review/1-9`: Growth from 5,598 km2 (1744) to 274,468 km2 (1788): Kharj, Sudair, Washm, Qasim; only Riyadh 1773 is in the ledger (keyframes noted 'unverified: page budget', not a fault). Page to try: https://en.wikipedia.org/wiki/Muhammad_bin_Saud_Al_Muqrin
- `/ledger/6, /ledger/9, /ledger/13, /ledger/14`: Dates and holders of Asir, Najran and the Tihama to Hodeida (1794-1803), four confidence-1 gains at Cliopatria's years. Page to try: https://en.wikipedia.org/wiki/Najran
- `/keyframe_review/10`: Qatar is inside the shapes from 1791 with no gain event (Bani Khalid land). Page to try: https://en.wikipedia.org/wiki/History_of_Qatar
- `/keyframe_review/17-18`: North reach to 32-33 N (Jawf, Wadi Sirhan) and east reach to 58.4 E in 1811 have no event. Page to try: https://en.wikipedia.org/wiki/Dumat_al-Jandal
- `/ledger/12`: Mecca was retaken by Sharif Ghalib after the 1803 entry and finally submitted in 1806 (Saud page and History of Saudi Arabia: 'Mecca in 1806'); the ledger keeps Mecca continuously from 1803. Page to try: https://en.wikipedia.org/wiki/Ghalib_bin_Musa%27ad
- `/ledger/27`: End of Saudi control of Bahrain (bridged to 1818 at confidence 1). Page to try: https://en.wikipedia.org/wiki/History_of_Bahrain_(1783%E2%80%931971)

### Spot checks

- `/ledger/2`: confirmed: 'only in 1773 Riyadh was captured by Abdulaziz' (https://en.wikipedia.org/wiki/Abdulaziz_bin_Muhammad_Al_Saud)
- `/ledger/7`: confirmed: 'the capture of Qatif in 1794 and Hasa in 1795' (also /ledger/5) (https://en.wikipedia.org/wiki/Abdulaziz_bin_Muhammad_Al_Saud)
- `/ledger/10`: confirmed: 'In 1802 Hejaz, namely Taif and Khurma, was captured' (https://en.wikipedia.org/wiki/Abdulaziz_bin_Muhammad_Al_Saud)
- `/ledger/15`: confirmed: 'the capture of Medina in April 1804' (https://en.wikipedia.org/wiki/Saud_bin_Abdulaziz_bin_Muhammad)
- `/ledger/16`: confirmed: 1805 'a part of Oman'; 'The same year he also annexed the Buraimi Oasis.' (https://en.wikipedia.org/wiki/Saud_bin_Abdulaziz_bin_Muhammad)
- `/ledger/26`: confirmed: 'By 1817, the armies had overrun Rass, Buraida and Unayza.' (https://en.wikipedia.org/wiki/Wahhabi_War)
- `/ledger/12, /ledger/18, /ledger/21`: confirmed: Mecca entered 1803; Yanbu landing 1811; Mecca captured January 1813 (https://en.wikipedia.org/wiki/Wahhabi_War)
- `/ledger/11`: not on page (year): recapture undated; confidence lowered to 1 by reviewer (https://en.wikipedia.org/wiki/Abdulaziz_bin_Muhammad_Al_Saud)

## sultanate-of-oman: thin

Area: infobox 315331 km2, Cliopatria 314076.1 km2, ratio 1.004; Infobox gives no year (modern Oman); compared with the 2024 shape. The 1744-1898 empire shapes cannot be compared; the author says so.

### Fixes

- `/ledger/3/note` (applied by reviewer): The note did not record that the Oman page has the Persians expelled before the November 1744 election, against 1747 on the Ahmad bin Said page. Evidence: Oman: occupations 'on two occasions between 1737 and 1744'; 'After the Omanis expelled the Persians' precedes the election of 20 November 1744. Fix: Disagreement appended to the note; confidence 2 kept; re-validated.
- `/ledger/12` (for the author / gap-filler, non-blocking): The 1856 split hands the Omani Slave Coast land to people-s-republic-of-zanzibar, but this dossier already split that land off in 1814 (/ledger/7), and the Zanzibar dossier takes it from omani-slave-coast. Evidence: people-s-republic-of-zanzibar /ledger/0: 1856-10 found, counterpart omani-slave-coast; omani-slave-coast /ledger/8: 1856-10 dissolve to people-s-republic-of-zanzibar with the same region. Fix: Drop the split (the 1856 rename /ledger/13 already records the division) or make it non-territorial; keep the Oman page quote in the rename note.
- `/ledger/8` (for the author / gap-filler, non-blocking): Buraimi is gained in 1820 from emirate-of-diriyah, which ended in September 1818 and records no loss of the oasis. Evidence: emirate-of-diriyah /identity/end 1818-09 and /ledger/29 dissolve (to muhammad-ali-dynasty); Wahhabi_War: surrender on 11 September 1818. Muscat_and_Oman (the cited page) has no Buraimi sentence. Fix: Counterpart nobody (or whoever the Diriyah dissolve gives Buraimi to) and keep confidence 1; coordinate with the Diriyah /ledger/29 fix.
- `/keyframe_review/11, /keyframe_review/12` (for the author / gap-filler, non-blocking): The 1856 and 1870 corrections leave Dhofar out, while the ledger holds Dhofar from 1830 (/ledger/10) to its loss to Fadhl bin Alawi in 1876 (/ledger/14): keyframes and ledger disagree for 1856-1875 (176k to 79k km2 with no loss event). Evidence: Dhofar page: Dhofar 'remained loyal to the sultans of Muscat'; Fadhl 'had established himself as the de facto ruler of Dhofar' in 1876. Fix: Either add admin1 Zufar to both corrections (as /keyframe_review/14 does for 1898) or add a confidence-1 loss in 1856 with a counterpart.
- `/keyframe_review/4-8, /ledger/9` (for the author / gap-filler, non-blocking): The corrections drop Sharjah from 1800 and all Trucial land by 1815, but the ledger loses the Trucial coast only in 1820. Evidence: Keyframe notes 4 and 8; Muscat_and_Oman: 'In the early 1820s, the Sultanate lost most of its territories in the Persian Gulf, which became the Trucial States'. Fix: Add the Trucial coast (Sharjah, Fujairah radii) back to the 1800-1815 corrections until 1820, or date the loss earlier at confidence 1.
- `/keyframe_review/23/note, /notes` (for the author / gap-filler, non-blocking): Unflagged Cliopatria problem: 'Cliopatria has no Omani shape for 1947-1972' is wrong; the 'Qatar Protectorate' row (1947-1955) is the Muscat and Oman outline mislabelled. Evidence: shapes.csv qatar-protectorate_1947 and _1953: area 307,787.5 km2, bbox 52.1253,16.679,59.9039,26.3865, modern_countries Oman: identical to sultanate-of-muscat-and-oman_1936/_1946. Fix: Say so in the 1947 keyframe note and in notes; tell the qatar-protectorate author (me-10).
- `/notes` (for the author / gap-filler, non-blocking): Unflagged known problem from the brief's context table: Kingdom of Great Britain's 1969-2023 Cliopatria shapes also contain Oman (1,440 cells). Evidence: Brief section 6, kingdom-of-great-britain known problems; data/README.md 'Kingdom of Great Britain -> Oman'. Fix: Note the overlap and that Oman is sovereign from 1970/71 (end of de facto protection).
- `/ledger (1891, 1970)` (for the author / gap-filler, non-blocking): No vassal_start/vassal_end for British protection, which the cited page states. Evidence: Muscat_and_Oman infobox: 'De facto British protected state (1891–1970)'. Reviewer brief check 3 wants the relation in both ledgers. Fix: Add vassal_start 1891 and vassal_end 1970 with the British counterpart; note eu-11 will split the United Kingdom from 1801 under a new slug, so the 1854/1891/1967/1970 counterparts should use that slug rather than kingdom-of-great-britain.

### Thin (for a gap-filler)

- `/ledger/4`: Who held Gwadar before 1783 (the Khan of Kalat's grant), counterpart given as nobody. Page to try: https://en.wikipedia.org/wiki/Gwadar
- `/ledger/10`: Date and manner of Dhofar's inclusion (1830 is Cliopatria's year, confidence 1). Page to try: https://en.wikipedia.org/wiki/Salalah
- `/ledger/8`: Return of Buraimi after 1818 (confidence 1, page silent). Page to try: https://en.wikipedia.org/wiki/Al-Buraimi
- `/ledger/7`: The 1814 split of the East African coast is Cliopatria's year (confidence 1). Page to try: https://en.wikipedia.org/wiki/Said_bin_Sultan
- `/keyframe_review/8-11`: Four Iranian-coast cells 1811-1869 (Bandar Abbas lease, 1794-1868) have no gain or loss. Page to try: https://en.wikipedia.org/wiki/Bandar_Abbas
- `/ledger (1802)`: Muscat's capture of Bahrain in 1802 (on the Abdulaziz page) is not in the ledger. Page to try: https://en.wikipedia.org/wiki/Abdulaziz_bin_Muhammad_Al_Saud
- `/keyframe_review/2`: The Trucial-coast piece added in 1757 has no gain event. Page to try: https://en.wikipedia.org/wiki/Trucial_States

### Spot checks

- `/ledger/1`: confirmed: 'Ahmad bin Said became the elected Imam of Oman on 20 November 1744' (https://en.wikipedia.org/wiki/Oman)
- `/ledger/11`: confirmed: 'In 1854, a deed of cession of the Omani Kuria Muria islands to Britain was signed' (https://en.wikipedia.org/wiki/Oman)
- `/ledger/24`: confirmed: 'On 8 September 1958, Pakistan purchased the Gwadar enclave from Oman for US$3 million.' (https://en.wikipedia.org/wiki/Oman)
- `/ledger/14, /ledger/15`: confirmed: Fadhl de facto ruler 1876, 'expelled by local sheikhs in January 1879' (https://en.wikipedia.org/wiki/Dhofar)
- `/ledger/16`: confirmed: 'In 1913, Imam Salim ibn Rashid al-Kharusi instigated an anti-Muscat rebellion'; Seeb 25 September 1920 and 1959 end also confirmed (https://en.wikipedia.org/wiki/Imamate_of_Oman)
- `/ledger/28`: confirmed: 'the sultanate did gain some territory in 1967, when Britain returned the Khuriya Muriya Islands' (https://en.wikipedia.org/wiki/Muscat_and_Oman)
- `/ledger/12, /ledger/27, /ledger/29, /ledger/30`: confirmed: 1856 two sultanates; Dhofar War began 1963; 'Sultanate of Oman: 9 August 1970'; campaign declared over December 1975 (Dhofar page) (https://en.wikipedia.org/wiki/Oman)

## Cross-dossier matrix

- afsharid-iran 1736 gain ottoman-empire: **exception**. ottoman-empire (me-10): counterpart dossier not written yet (group has not run / part not reached)
- afsharid-iran 1738 gain hotaki-dynasty <-> hotaki-dynasty 1738 loss: **matched**. hotaki 1738-03 loss of Kandahar
- afsharid-iran 1738 gain Arab rulers of Bahrain: **exception**. no dossier; not in author's counterparts list; added to counterparts_needing_dossiers
- afsharid-iran 1738 gain mughal-empire <-> mughal-empire 1738 loss: **matched**. Ghazni and Kabul, June 1738
- afsharid-iran 1738 gain mughal-empire <-> mughal-empire 1739 loss: **matched**. Peshawar Nov 1738 vs mughal loss of the lands west of the Indus May 1739 (within a year)
- afsharid-iran 1739 occupation_start mughal-empire <-> mughal-empire 1739 occupation_start: **matched**. Delhi 20 March-16 May 1739; occupation_end also matched
- afsharid-iran 1739 gain mughal-empire <-> mughal-empire 1739 loss: **matched**. Sindh; was 1741 (2-year mismatch), moved to 1739-05 by the reviewer
- afsharid-iran 1740 vassal_start khanate-of-bukhara <-> khanate-of-bukhara: none: **missing**. Bukhara ledger has no 1740 vassal_start (ia-03); vassal_end 1747 likewise missing
- khanate-of-bukhara 1736 loss afsharid-iran <-> afsharid-iran: none: **missing**. Balkh: no gain in afsharid-iran (fix listed for me-10-c)
- afsharid-iran 1740 vassal_start khanate-of-khiva <-> khanate-of-khiva 1740 occupation_start: **mismatch**. type disagrees: vassal (afsharid) vs occupation (khiva); same for the 1747 end
- afsharid-iran 1743 gain yarubid-dynasty: **exception**. yarubid-dynasty (me-10): counterpart dossier not written yet (group has not run / part not reached)
- afsharid-iran 1744 vassal_start kingdom-of-kakheti: **exception**. eu-19: counterpart dossier not written yet (group has not run / part not reached); also kingdom-of-georgia 1744 and both vassal_end 1747
- afsharid-iran 1747 loss sultanate-of-oman <-> sultanate-of-oman 1747 gain: **matched**. Muscat
- afsharid-iran 1747 split durrani-empire <-> durrani-empire 1747 found: **matched**. durrani found 1747-07 from afsharid-iran
- afsharid-iran 1748 loss zand-dynasty: **exception**. zand-dynasty (me-10): counterpart dossier not written yet (group has not run / part not reached)
- afsharid-iran 1750 loss durrani-empire <-> durrani-empire 1750 gain: **matched**. Herat
- durrani-empire 1755 vassal_start afsharid-iran <-> afsharid-iran: none: **missing**. afsharid-iran has no vassal_start/vassal_end with durrani-empire (fix listed); durrani vassal_end 1796 likewise
- afsharid-iran 1796 dissolve qajar-dynasty: **exception**. qajar-dynasty (me-10): counterpart dossier not written yet (group has not run / part not reached)
- emirate-of-diriyah 1773 gain Dahham ibn Dawwas (ruler of Riyadh): **exception**. listed in counterparts_needing_dossiers (emirate-of-riyadh, me-10-x)
- emirate-of-diriyah 1794 gain Bani Khalid Emirate: **exception**. listed (bani-khalid-emirate, me-10-x); also 1795
- emirate-of-diriyah 1794 gain nobody: **exception**. Asir; also 1799 and 1803 gains from nobody
- emirate-of-diriyah 1802 gain ottoman-empire: **exception**. ottoman-empire (me-10): counterpart dossier not written yet (group has not run / part not reached); also Mecca 1803, Medina 1804. Author lists sharifate-of-mecca as needing a dossier but uses ottoman-empire as counterpart: pick one
- emirate-of-diriyah 1802 vassal_start house-of-khalifa: **exception**. house-of-khalifa (me-10): counterpart dossier not written yet (group has not run / part not reached); vassal_end 1818 likewise
- emirate-of-diriyah 1803 gain qasimids: **exception**. qasimids (me-10): counterpart dossier not written yet (group has not run / part not reached)
- emirate-of-diriyah 1805 gain sultanate-of-oman <-> sultanate-of-oman 1805 loss: **matched**. Buraimi
- emirate-of-diriyah 1811 loss muhammad-ali-dynasty: **exception**. muhammad-ali-dynasty (me-10): counterpart dossier not written yet (group has not run / part not reached); also losses 1812-1817 and the 1818 dissolve
- sultanate-of-oman 1820 gain emirate-of-diriyah <-> emirate-of-diriyah: none: **mismatch**. Diriyah ended 1818-09 and records no loss of Buraimi; its dissolve region still holds the oasis
- sultanate-of-oman 1744 found yarubid-dynasty: **exception**. yarubid-dynasty (me-10): counterpart dossier not written yet (group has not run / part not reached)
- sultanate-of-oman 1783 gain nobody: **exception**. Gwadar; Khanate of Kalat probably the right counterpart (thin)
- sultanate-of-oman 1814 split omani-slave-coast <-> omani-slave-coast 1814 found: **matched**. both confidence 1 at Cliopatria's year
- sultanate-of-oman 1820 loss trucial-states: **exception**. trucial-states (me-10): counterpart dossier not written yet (group has not run / part not reached)
- sultanate-of-oman 1854 loss kingdom-of-great-britain: **exception**. eu-11: counterpart dossier not written yet (group has not run / part not reached); after eu-11's split the counterpart should be the United Kingdom slug; 1967 gain likewise
- sultanate-of-oman 1856 split people-s-republic-of-zanzibar <-> people-s-republic-of-zanzibar 1856 found: **mismatch**. Zanzibar's found counterpart is omani-slave-coast (which dissolves 1856-10 with the same region): Oman's split is a duplicate
- sultanate-of-oman 1876 loss Fadhl bin Alawi: **exception**. no dossier (minor); 1879 gain likewise
- sultanate-of-oman 1913 loss imamate-of-oman: **exception**. imamate-of-oman (me-10): counterpart dossier not written yet (group has not run / part not reached); also vassal 1920-1954 and gain 1959
- sultanate-of-oman 1958 loss islamic-republic-of-pakistan: **exception**. no dossier yet (not a context polity of this batch)

## Problems and routing

- MERGE conflict: sultanate-of-oman lists both 'Sultanate of Oman' and 'Sultanate of Muscat and Oman' in cliopatria_names and reviews both rows (defensible: one Al Bu Said state), but the orchestrator assigned sultanate-of-muscat-and-oman to another me-10 part (not written yet); colours.json gives them different colours. The orchestrator must drop one.
- Cliopatria 'Qatar Protectorate' (1947-1955) is the Omani outline mislabelled (identical area and bbox to Muscat and Oman 1936/1946, modern_countries Oman): route to the qatar-protectorate author (me-10).
- afsharid-iran ledger indices shifted by the reviewer's fix: the Sindh gain is now /ledger/12 (was /ledger/14); the 1740 Bukhara and Khiva vassal_start events are now /ledger/13 and /ledger/14. All other pointers in this report use the current files.
- Mirror issues for ia-03: khanate-of-bukhara lacks the 1740-1747 vassal pair; khanate-of-khiva records 1740-1747 as occupation, afsharid-iran as vassalage.
- All three verdicts are thin with only non-blocking unapplied fixes: no fabricated or mis-dated confidence-3 event was found in the 32 events checked; the remaining work is mirror events, keyframe-ledger consistency and pages for confidence-1 gaps.
- WebFetch answers are paraphrased by a small model; quotes are as it returned them.

## Gazetteer names needed

- Diriyah (place, emirate-of-diriyah)
- Khurma (place, emirate-of-diriyah)
- Kuria Muria Islands (Hallaniyat) (place, sultanate-of-oman)

## Counterparts needing dossiers

- Bani Khalid Emirate (bani-khalid-emirate, 1669-1795)
- Emirate of Riyadh (Dahham ibn Dawwas) (emirate-of-riyadh, 1747-1773)
- Sharifate of Mecca (sharifate-of-mecca, 1802-1813)
- Dhofar Liberation Front / PFLOAG (rebel) (pfloag, 1963-1975)
- Avar Khanate (Dagestani tribes and khanates) (avar-khanate, 1741-1745)
- Emirate of Abu Dhabi (Buraimi) (emirate-of-abu-dhabi, 1952-1955)
- Arab rulers of Bahrain (before the Al Khalifa) (bahrain, 1736-1783)
- Fadhl bin Alawi's Dhofar (fadhl-bin-alawi-dhofar, 1876-1879)
- Khanate of Kalat (khanate-of-kalat, 1666-1955)
