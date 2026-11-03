# Review of batch sa-06-c (2026-10-25)

Reviewer: adversarial review, Phase B. Dossiers: british-empire, danish-india, indian-rebels-of-1857. The validator (`--resolve --json`) reports no errors and no warnings for any of the three. The reviewer edited no dossier. The machine copy of this review is history/notes/phase-b/reviews/sa-06-c.json.

Verdicts: **british-empire: fail** (goes back to the author). **danish-india: pass**. **indian-rebels-of-1857: thin** (needs a gap-filler and the fixes below).

## british-empire (fail)

Spot checks (Company_rule_in_India, Second_Anglo-Maratha_War, First_Anglo-Burmese_War, Indian_Rebellion_of_1857): /ledger/22 (1801), /27 (Surji-Anjangaon, 30 December 1803), /26, /23, /25, /29, /48 (Yandabo, 24 February 1826), /88, /89, /91, /32, /38, /53, /54 and /58 all say what the page says. The trouble is that three confidence-3 dates come from the Company page's timeline and are contradicted by the pages for those states:

- /ledger/11 Jaipur vassal 1794. Jaipur_State has a treaty in 1803 that was dissolved soon after, and the subsidiary alliance in 1818. Move it to 1818, or fold it into the 1817 Rajputana event.
- /ledger/44 Baroda vassal 1819. The Baroda_State infobox has 'Protectorate of the East India Company (1805-1858)'. Change the year to 1805.
- /ledger/14 Andamans gained in 1796. Andaman_Islands has the settlement founded in 1789 and closed in May 1796. No keyframe draws the islands from 1796 to 1856. Replace it with a 1789 gain and a 1796/5 loss.

Blocking findings:

1. **Ceylon is drawn twice.** The corrections for keyframes 13-40 (1796-1858) keep Sri Lanka. british-ceylon is founded 1796/2 from dutch-ceylon, and dutch-ceylon dissolves to british-ceylon, so /ledger/15 (gain from dutch-ceylon) has no mirror. The author's report says the verdicts correct Sri Lanka; they do not. Add a minus of Sri Lanka to each correction. Then either drop /ledger/15, or follow it with a loss to british-ceylon in 1798/1802.
2. **Counterparts that do not exist at the date of the event.**
   - /ledger/2-3: the 1765 vassal_end and gain name nawabs-of-bengal, which ends in June 1757 with a dissolve to british-empire.
   - /ledger/50: the 1828 loss names ahom-kingdom, which dissolved into british-empire in 1826. That loss is Cliopatria noise and is undone by the confidence-1 gain at /ledger/55.
3. **The author's own danish-india events are not mirrored**: the occupations of 1763, 1801-1802 and 1808-1815, and the 1845 sales of Tranquebar and Serampore (1845/10).
4. **The rebel war is not mirrored place by place.**
   - The rebels gain Lucknow in 1857/11, but this ledger never loses it.
   - Lucknow (/89) and Jhansi (/90) are regained in 1858 without having been lost.
   - Gwalior was Scindia's. After the 1858/6 recapture it must go back to gwalior-state, which records a 1858 gain from british-empire.
5. **About 25 neighbour events against british-empire have no mirror here.** Several of them explain the confidence-1 'unspecified (page silent)' steps:

   | Neighbour | Events | Note |
   | --- | --- | --- |
   | hyderabad-state | 1768/3 Northern Circars, 1788 Guntur, 1800 Ceded Districts, 1804 gain | fits /ledger/5 and /ledger/21 |
   | carnatic-sultanate | 1801/7 | fits /ledger/24 |
   | thanjavur-maratha-kingdom | 1799 | |
   | kingdom-of-mysore | 1769/3 Karur | |
   | maratha-empire | 1776/3 Salsette, 1803/9 Delhi | |
   | indore-state | 1805/12, 1818/1 | |
   | kingdom-of-nagpur | 1806 | |
   | gwalior-state | 1805, 1818, 1844, 1858 | 1844 fits /ledger/69 |
   | french-india | Chandernagore and Pondicherry occupations, 1757-1816 | |
   | kingdom-of-bhutan | 1784, 1841 | |
   | qajar-dynasty | Kharg and Bushehr occupation, 1856/12-1857/10 | |
   | english-colonial-empire | Bombay 1762, Masulipatnam 1778, Madras 1779 | the 1757 shape already holds a Bombay cell |
   | burma | Rangoon occupation, 1824/5-1826/2 | |
   | sikh-empire | Faridkot and Ambala 1809/4; Kashmir and Hazara 1846/3 | Kashmir: add a gain here and a same-month loss to kashmir-and-jammu |

Other fixes:

- /ledger/6 Benares: change 1773 to 1775. nawab-of-awadh and Cliopatria both have 1775; the Company page does not date the cession.
- /ledger/81 Berar: this ledger has a gain in 1854; hyderabad-state has an occupation in 1853. Agree on one year and one type.
- /ledger/69 cites the Anglo-Maratha Wars disambiguation page. The unused Umayyad 'Conquest_of_Sindh' entry should be removed from sources.
- Wars:
  - /wars/11 names durrani-empire (its row ends in 1827); use emirate-of-afghanistan or durrani-dynasty. Add zones, because the ledger occupies Kalat; follow khanate-of-kalat's dates, 1839/11-1841, not 1840-1842.
  - /wars/2 and /wars/3 have empty zones although land changed hands (Karur, Salsette).
- **Duplicate state.** east-india-company.json (sa-06-x) is the same Company, and bahawalpur-state, kingdom-of-coorg and khanate-of-kalat mirror that file. The orchestrator must keep one.

What held up:

- Every Cliopatria shape is reviewed, and the Canadian cells are removed throughout.
- The 1857-58 rebel cut is restored with a reason.
- Baluchistan is removed after 1842, as khanate-of-kalat agrees.
- The area is acknowledged: infobox 1,940,000 km2 (1858) against 3,627,885 km2, a ratio of 1.87, the difference being protected states that the ledger tints.
- Treating Bengal as a client from 1757 to 1765 with the shape unchanged follows the brief's rule for a status-only verdict.

Thin, at confidence 1 within the 14-page budget:

- 1769 (Northern Circars)
- 1780 and 1783 (noise)
- 1794 (southern Odisha)
- 1800 and 1803 (Ceded Districts, Thanjavur, the Carnatic)
- 1814 and 1824
- 1834 and 1836 (Jaintia)
- 1840-1842 (Kalat)
- 1846 (the Gwalior campaign of 1843-44)

## danish-india (pass)

What I tried:

- **Spot checks.** Danish_India confirms 20 November 1620, 'The British occupy Serampore for the year' (1763), the 1801-1802 and 1808-1815 occupations, the transfer of 20 September 1815, '11 October 1845 Frederiksnagore sold', the Crown takeover of 1777, and the annexation of 1869. Nicobar_Islands confirms 16 October 1868.
- **Flagged disagreements.** The author flags the page's unreconciled Serampore sale of 1839 and the 19 or 20 November date for the treaty.
- **Keyframes and life.** The new keyframes carry from, to and a correction. The occupation pairs are closed. The Nicobar circle (93.3 E, 8.0 N, 190 km) stays clear of Little Andaman and Sumatra.
- **Area.** The infobox gives no area.

Unmirrored events against this dossier sit elsewhere, so they do not count against it:

- british-empire mirrors none of the occupations or sales (same author).
- nawabs-of-bengal has no 1755 loss of Serampore.
- british-raj gains the Nicobars in 1869 from 'nobody' instead of from danish-india.

## indian-rebels-of-1857 (thin)

The dossier is built from one page (Indian_Rebellion_of_1857). These dates are confirmed: Delhi 11 May 1857, Kanpur in June, Lucknow 21 March 1858, Gwalior 1 June 1858, and the Jhansi siege in March 1858.

Fixes:

- /ledger/9: the 1858 Gwalior gain names british-empire, but Gwalior was gwalior-state's.
- Jhansi and Bundelkhand appear in the 1858 keyframe and are lost in 1858/3, but are never gained. jhansi-state holds Jhansi until its dissolve in 1858/4, and the capture was in April.
- The 1857 keyframe draws all of Awadh, but the ledger's only Awadh event is the Lucknow gain of 1857/11. Add an Awadh gain in mid-1857 (the Residency siege began on 30 June) and a mirror in british-empire, or draw only the places the ledger gains.
- Delhi: mughal-empire holds Delhi until 1857/9, so three dossiers draw it three ways. Reconcile with sa-05.

Gap-filler pages:

- Siege_of_Lucknow
- Siege_of_Jhansi
- Siege_of_Cawnpore
- Begum_Hazrat_Mahal: the Awadh resistance ran into late 1858, and the page has hostilities formally ending on 8 July 1859, so the 1858/6 end is early.

## Counterparts needing dossiers

- cis-sutlej-states (1809-1858)
- sambalpur-state (to 1849)
- sultanate-of-lahej (Aden, 1839)
- the Rajputana states, or name the individual sa-04 states as counterparts

bahawalpur-state and kingdom-of-coorg now exist. talpur-dynasty (sa-05) has not been written yet.
