# Review of batch sa-05-f (nepal, sikh-empire), 2026-10-20

Reviewer: adversarial review, Phase B. Validator (--resolve): 0 errors in both; warnings are the unwritten counterpart slugs (kingdom-of-sikkim, kumaon-kingdom, garhwal-kingdom, kangra-state, all listed by the author) and the unknown region Ngari. Neighbour dossiers read (ledgers only): kathmandu, tibet, mughal-empire, durrani-empire, emirate-of-afghanistan, kingdom-of-bhutan, durrani-dynasty. Not yet written (counted as groups that have not run): qing-dynasty, british-empire, british-raj, republic-of-india, people-s-republic-of-china, people-s-republic-of-bangladesh, talpur-dynasty, islamic-republic-of-pakistan, nawab-of-awadh, gorkha-kingdom, sikh-confederacy, british-colonial-empire, kashmir-and-jammu.

Pages opened by the reviewer: Unification of Nepal, Anglo-Nepalese War, Kingdom of Sikkim, Nepal, Kumaon Kingdom, Sikh Empire (twice), First Anglo-Sikh War, Treaty of Amritsar (1846), Dera Ghazi Khan, Ranjit Singh. Every quoted event checked was on its page with its year; no fabricated or mis-dated event found.

## nepal: FAIL (two keyframe findings for the author; one fix applied by the reviewer)

Spot checks (all confirmed): /ledger/0, 1, 2, 4 (Bhaktapur 'on 14 April 1769' is on the Unification page), 5 (Kaski 1771 is the page's table row; confidence 2 is apt), 6, 8, 11, 12 (table rows 1774, 1786, 1789, 1790), 7 (Sikkim infobox 'Nepalese Invasion: 1776'), 13 (Kumaon 1791), 20 (war declared 1 November 1814; month 10 rests on Nalapani from 31 October, said in the note), 21 (Almora 27 April 1815), 22 (15 May 1815), 25 (Mechi-Teesta in the infobox), 27 (1846, Kot massacre), 28 (1860 western Terai; the Nepal page says 'as a friendly gesture', the note's '1857 rebellion' reason is not on that page), 29 (28 May 2008).

Area: Nepal infobox 147,181 km2 (modern) against Cliopatria nepal_2024 148,575 km2, ratio 1.01, acknowledged.

Blocking findings (not applied):

1. /keyframe_review/2 (nepal_1788, verdict ok). Cliopatria's 1788 shape already holds Jumla (admin1 Karnali, 82 cells) and Doti (Seti 50 + Mahakali 24 cells), about 39,500 km2, which the ledger gains only in 1789 (/ledger/11) and 1790 (/ledger/12) from the Unification table ('1789 Jumla is annexed', '1790 Doti, Kumaun ...'). None of these cells is in the 1775 shape. The note on /keyframe_review/3 says so ('Doti and Jumla ... are already inside the 1788 shape') and the notes field says the far west is 'added by the ledger', but the verdict is ok, so the map shows them Nepalese one to two years early and the two gains do nothing. Fix: verdict adjust, correction {"minus": [{"cliopatria": "Nepal", "year": 1788}, {"union": [{"admin1": "Karnali", "country": "Nepal"}, {"admin1": "Seti", "country": "Nepal"}, {"admin1": "Mahakali", "country": "Nepal"}, {"admin1": "Sikkim", "country": "India"}]}], "text": "Cliopatria's 1788 shape without Jumla (annexed 1789), Doti (1790) and occupied Sikkim"}.
2. Sikkim's status changes from keyframe to keyframe. Sikkim (24 of its 27 cells, about 6,000 km2) is direct territory in nepal_1788 (ok), nepal_1791 (ok), nepal_1792 (its correction is 'the 1791 Nepal shape (Nepal with Kumaon, Sikkim and the Teesta strip)') and nepal_1814 (ok), but is left out in 1775-1787 and 1794-1813 ('Sikkim is occupied, not annexed'), while /ledger/7 and /ledger/26 hatch it as an occupation for the whole of 1776-1816 (the note of /ledger/7 says itself 'Cliopatria draws Sikkim inside Nepal only in 1788-1793 and in 1814'). Between nepal_1792 and nepal_1794, and between nepal_1812 and nepal_1814, Sikkim leaves and then re-enters the direct shape with no ledger event. Fix: take {"admin1": "Sikkim", "country": "India"} out of the 1788, 1791, 1792 and 1814 shapes (1791 and 1814 become adjust), so that Sikkim is the hatched occupation throughout. Or, if Sikkim was annexed in some years, add dated gain and loss events with a page (the Kingdom of Sikkim infobox has 'Nepalese domination (1776-1792)', then 'Nepalo-Bhutanese presence (1792-1816)').

Applied by the reviewer:

3. /wars/0/from: 1744 changed to 1768. The war ('Unification of Nepal') began before the dossier's life (start 1768-09). The war's own note gives the 1744-1767 campaigns to gorkha-kingdom, and the Unification page has the Kingdom of Nepal announced 'On 25 September 1768'. A sentence saying so was added to the note. Re-validated: 0 errors.

Not blocking (for the author when the dossier comes back):

4. /keyframe_review/14 (nepal_1815): the correction removes the western Terai from 1815, and Cliopatria's 1815 shape lacks the Mechi-Teesta strip, yet both losses are dated March 1816 (/ledger/24, /ledger/25), and the text says 'in 1815 the British held the west but the Terai was still Nepal's'. The two pieces are off by under a year. Either keep both in the 1815 shape and let the 1816 losses remove them, or say why not.
5. /keyframe_review/0 (nepal_1768) takes in the whole Bagmati zone, Bhaktapur included, from September 1768, while /ledger/4 gains Bhaktapur on 14 April 1769. The area is small and the time is seven months, so this is noted only. /ledger/4's region (a 25 km radius round Kathmandu) is also a caption, since that land is already inside the 1768 shape.
6. /ledger/28 note: the reason '1857 rebellion' is not on the Nepal page ('as a friendly gesture'). Attribute it to the page that says it, or drop it.

Thin, within the 9-page budget (for a gap-filler):
- 1775 to 1788: about 65,000 km2 enters with no dated event: Dhawalagiri 8,100, Rapti 10,400, Lumbini 9,100, the Terai now in Uttar Pradesh 8,850, and a Tibetan fringe of about 15 cells. This is the Chaubisi and Palpa annexations, which the author flagged.
- /ledger/17 (1806 hill states to the Sutlej, confidence 1) and /ledger/18 (1807 start of the Kangra siege, confidence 1).
- The Nepal-Tibet war of 1855-56: an occupation of Kuti and Kerung, returned by the Treaty of Thapathali. Not in the ledger.
- The Terai lands returned in December 1816, which the Anglo-Nepalese War page has without names.

## sikh-empire: THIN (one fix applied by the reviewer; gaps for a gap-filler)

Spot checks (all confirmed): /ledger/1 ('In 1800, the Jammu region was annexed by Ranjit Singh'; the Ranjit Singh page has the 1800 cession), 4 (Kasur 1807), 7 (Attock 1813, Ranjit Singh page), 8 (Multan 1818), 9 (Kashmir 1819, Shopian), 10 (Dera Ghazi Khan 1819), 11 (Mankera 1821), 12 (Peshawar tributary 1823), 15 (Peshawar annexed 1834), 18 (Baltistan 1839-40), 21 and 22 (war 11 December 1845 to 9 March 1846), 23 and 24 (Treaty of Lahore terms), 27 (Hazara ceded back 'in early 1847'; the treaty was 'executed on 16 March 1846'), 30 (proclamation 29 March 1849), and identity.rulers (the page's table of Maharajas, dates exact).

Area: infobox '1839: 520,000 km2' against Cliopatria sikh-empire_1836 (1836-1839) 349,342 km2, ratio 0.67; the corrected direct land is about 265,000 km2 (ratio 0.51, just under a factor of two). Both are acknowledged in the /keyframe_review/10 note, which says the infobox figure probably counts claims. Accepted.

Applied by the reviewer:
1. /identity/rulers/1 to /identity/rulers/6 had no source. Added https://en.wikipedia.org/wiki/Sikh_Empire, whose table of Maharajas gives exactly the dates in the notes. Re-validated: 0 errors.

Thin (the priority items first; both are on pages the author already opened):
- Missing event: 'In the same year [1807] he also annexed the Sial-ruled Jhang' (Ranjit Singh page). Jhang enters Cliopatria only in 1820 (18 of the 31 cells of a 50 km radius round Jhang; none in the 1807 or 1811 shapes). Add a 1807 gain (counterpart: the Sial nawabs of Jhang) and add Jhang to the 1807 and 1811 corrections.
- Missing event: the Treaty of Bhyroval. The First Anglo-Sikh War page (a source) has Jind Kaur 'replaced by a British resident in Lahore' with a Council of Regency, which 'effectively gave the East India Company control of the government'. /ledger/28's own note quotes the Resident's 'full authority'. Add vassal_start 1846 month 12 with counterpart british-empire over the whole Lahore state, and vassal_end 1849 month 3. The author asked only the british-empire dossier to carry it.
- 1811 to 1820: about 92,000 km2 enters with no dated event beyond Attock (25 km), the Kashmir Valley region (14,000 km2) and the Kangra radius. That is about 47,000 km2 in Pakistani Punjab (Pothohar and Rawalpindi, Jhelum, Gujrat, Khushab, Jhang), 24,000 km2 of Kashmir outside the Valley region (Poonch, Rajouri, Bhimber, Muzaffarabad) and 16,000 km2 of Himachal hill states. The /keyframe_review/5 note names 'the Rawalpindi, Attock and Peshawar lands', but only Attock has an event.
- /ledger/2 (the 1800 core of 50,300 km2, confidence 1), /ledger/5 (Kangra 1809, confidence 1), /ledger/13 (Hazara 1830, confidence 1), the 1842 step near Gilgit (/keyframe_review/12), and Kohat, Bannu and the Derajat before 1836.
- The 1847 exchange: Gulab Singh got 'the talukas of Kathua and Suchetgarh, along with part of Minawar' for Hazara (Treaty of Amritsar (1846) page). This is a small 1847 loss to kashmir-and-jammu, not in the ledger.
- /ledger/6 (1809 loss of Ambala and Faridkot) has no earlier gain; the note calls it a caption. The 1806-1808 cis-Sutlej campaigns are missing.

## Cross-dossier matrix (short)

- nepal and tibet, 1788, 1789, 1791 and 1792-10 occupations: all four matched.
- nepal 1768 gain of kathmandu against the kathmandu dossier's 1768-09 dissolve and contest_end: the year matches, but kathmandu names gorkha-kingdom as its counterpart. This follows from where the gorkha-kingdom/nepal split falls (25 September 1768). The kathmandu owner and the gorkha-kingdom author should settle it: name nepal if the Kingdom of Nepal is held to begin on 25 September 1768.
- sikh-empire 1819 gain of Kashmir and durrani-empire 1819-07 loss: matched.
- sikh-empire 1813 gain of Attock from durrani-empire: no 1813 loss in durrani-empire (ia-03).
- sikh-empire 1818 gain of Multan (counterpart 'Multan (Nawab Muzaffar Khan)') against durrani-empire 1818 loss to sikh-empire: same year and land, counterparts named differently.
- sikh-empire 1823 vassal_start over Peshawar against durrani-empire 1823-03 loss to sikh-empire: the type differs (loss against tributary). The Sikh side matches its page ('Peshawar became tributary in 1823').
- sikh-empire 1834 gain of Peshawar against emirate-of-afghanistan's contest_start with sikh-empire 1834 to 1837-04 (Jamrud): the Sikh ledger has no contest for 1834-1837.
- sikh-empire 1841 occupation of Ngari: the tibet dossier (ea-06) has no 1841 event.
- durrani-empire lists sikh-empire as a successor; sikh-empire does not list durrani-empire as a predecessor (it lists sikh-confederacy and sukerchakia-misl).
- Every british-empire, british-raj, kashmir-and-jammu, sikh-confederacy and gorkha-kingdom event is an exception: those groups have not run yet. The free-text counterparts the author listed are exceptions too. Not listed by the author: Kaski and the Chaubisi states (1771), the Kirant chiefdoms (1774), the Bheri (Baise) principalities (1786), the hill states between Garhwal and the Sutlej (1806), and the Sial nawabs of Jhang (1807, the missing event above).
