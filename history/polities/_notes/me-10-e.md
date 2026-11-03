# me-10-e: what could not be settled

Group me-10, part e. Five dossiers written (four owned, one new rebel state), 82 ledger events, 22 sources, all validate with 0 errors and 0 warnings under `--resolve`. (After the repair of 2026-10-25 muhammad-ali-dynasty has 27 events and 11 sources, so the batch totals are 92 events and 28 sources.) Pages were opened with WebFetch only; the fetch tool returns a summary, so only fragments the summary showed in quotation marks are quoted in the dossier notes and everything else is a close paraphrase. Where a page was silent the event is at confidence 1 with "page silent" in its note.

Page use: qajar-dynasty 9 of 9, persian-socialist-soviet-republic 1 (new state, minor), muhammad-ali-dynasty 5 of 5 (plus 6 pages opened in the repair of 2026-10-25), imamate-of-yemen 4 of 5, qatar-dynasty 3 of 5.

## qajar-dynasty (Cliopatria "Qajar Dynasty", 27 shapes, 1788..1923)

Cliopatria rows to correct
- 1895-1897 shape is a data error: it mixes Iran with a polygon in Indonesia (centroid in Borneo). Verdict wrong; use the 1894 shape.
- 1915-1921 shapes cut the occupied land (767 cells in 1915, 785 in 1916, 407 in 1917, 595 in 1918, 408 in 1920) out of Persia and give it to the Russian Empire, the British colonial empire and the Ottomans. Persia declared neutrality and stayed sovereign. All adjusted to the 1914 frontier, with occupation_start/end events carrying the foreign presence. The British counterpart string is british-colonial-empire (the Name Cliopatria uses); if the British rows are merged under british-empire the string must follow.
- 1788 adjust: the Qajar Iran page gives 'Establishment: 1789', so Cliopatria's first year is a year early; the shape itself fits the pages and is drawn for 1789-1790 only.
- New keyframe qajar-dynasty_1924 (1924..1925). Cliopatria ends the Qajar row in 1923 and starts the Pahlavi row in 1924; the pages end the Qajar state on 31 October 1925. The pahlavi-dynasty dossier (another agent) should start in 1925 or 1926.
- Qajar to Pahlavi is a dynasty change on the same land (rule 2 of the brief). The colour agent may want one colour for both.

Disagreements between pages
- Annexation of Kartli-Kakheti by Russia: December 1800 (Russo-Persian War 1804-1813 page) against 12 September 1801 (Qajar Iran page). Not resolved.
- Treaty of Turkmenchay: signed 2 February 1828 (war page) or 10 February 1828 (Qajar Iran page). Ledger uses February 1828 only.
- Agha Mohammad Khan page contradicts itself on Shusha: a settlement in 1795; he was killed "three days after he had taken the city" in 1797.
- Persian campaign (disambiguation page) was opened by mistake; Persian_campaign_(World_War_I) is the real article and was used.

Unsettled, with the reason
- Erivan, Karabakh and Ganja khanates 1796-1806: the pages show support, a settlement and submissions to Russia, not a status. Ledger gains at confidence 1 (counterpart string khanates-of-the-caucasus; the eu-19 row covers only to 1796). Shirvan, Sheki and Baku additions of 1797 are undated on every page opened. Page silent.
- First Herat campaigns of Mohammad Shah: undated on the Qajar Iran page.
- Treaty of Akhal (21 September 1881) and the 1884 transfer of Merv, Sarakhs and Ashgabat change no Cliopatria cell.
- Not opened (budget of 9): Seistan arbitration, Ottoman-Persian frontier treaties, Anglo-Russian Convention of 1907, Soviet-Persian treaty of 1921. Out of scope for the budget.
- When the British left Persia in 1920-21: page silent; two occupation_end events at confidence 1.
- The 1828 Russian occupation_end (Tabriz/Ardabil) and the April 1915 Ottoman occupation_end (Urmia) are at confidence 1 (page silent on the date). The 1796 and 1797 Caucasus gains are also confidence 1.

Counterparts needing dossiers
- Persian Socialist Soviet Republic: written here (persian-socialist-soviet-republic).
- Karabakh Khanate, Ganja Khanate, Erivan Khanate: named by string; no dossier exists in any group I could see (khanates-of-the-caucasus ends in 1796).

Gazetteer names the gazetteer lacks: Shusha, Anzali (Bandar-e Anzali, Enzeli), Mughan Plain, Talysh, Erivan Khanate, Quba. Khoi is spelled Khoy in places.jsonl and Bushire is Bushehr. Where they were needed they were drawn as lon/lat/km or described in text only.

## persian-socialist-soviet-republic (new slug, rebel state, no Cliopatria row)

- Written because the Qajar dossier's Gilan events name it as counterpart. One page opened (Persian_Socialist_Soviet_Republic). Territory is Gilan only on that page; drawn as admin1 Gilan, soft.
- The page is inconsistent on the month of foundation (infobox and body May 1920, intro June 1920); the dossier uses May 1920. Silent on the day of the Soviet-Persian treaty (infobox February 1921) and of Reza Khan's coup. Ends September 1921 on the page.
- Wikidata id not seen (the site was unreachable), so null.
- Its Soviet patron is republics-of-the-soviet-union (Cliopatria 1920-1921); no event in this dossier names it as a gain counterpart.

## muhammad-ali-dynasty (Cliopatria "Muhammad Ali dynasty", 8 shapes, 1805..1865)

Repaired 2026-10-25 after the reviewer's verdict "fail" (review-me-10-e.md); 27 ledger events (was 17), 12 keyframes (was 11), 11 sources (was 5), 0 errors and 0 warnings under `--resolve`. Pages re-opened: History of Egypt under the Muhammad Ali dynasty, Muhammad Ali of Egypt. New pages: Sultanate of Darfur, Sultanate of Sennar, Yemen Eyalet, Emirate of Nejd, Khedivate of Egypt, Turco-Egyptian Sudan (the repair went beyond the original budget of 5 on purpose: the findings are about dates and counterparts that only those pages give).

What I changed, per finding
1. Ottoman vassalage: added vassal_start 1805-5 (Egypt, counterpart ottoman-empire, History of Egypt page: 'when the Ottoman Sultan acknowledged his position'; 1841 'emphasizing his position as vassal') and vassal_end 1865 (bookkeeping for the dissolve; the relation passes to khedivate-of-egypt). I did not open a second vassal pair for the Syrian provinces, Crete and the Hejaz of 1833-1840 (ottoman-empire /ledger/181 and /ledger/185 have it): two open spans with one counterpart string cannot be told apart, and the pashalik grant stays written as gain 1833-5 and losses 1840-11 from ottoman-empire. Disagreement kept: ottoman-empire /ledger/220 (vassal_end 1914-11) names muhammad-ali-dynasty, a state that ends in 1865; khedivate-of-egypt is meant.
2. Kordofan: the former /ledger/4 is split into Sennar and the Gezira from funj-sultanate (June 1821; Sultanate of Sennar page: Badi VII submitted on 14 June 1821, confidence 2 because the page names Sennar, not the Gezira) and Kordofan from sultanate-of-darfur (19 August 1821, Sultanate of Darfur page, confidence 3; the Sennar page: the Fur Sultanate held Kordofan 'until the Egyptian invasion of 1821'). Both match the Darfur and Funj dossiers.
3. Greek war: /wars/2 now has zones (Peloponnese, Crete), `from` 1821, belligerent first-hellenic-republic (a Cliopatria row 1822-1940, group eu-18), an outcome that says no ground changed hands. Added occupation_start 1825-3 / occupation_end 1828-8 for the Morea (counterpart first-hellenic-republic; History page: Ibrahim 'in the following March ... landed in the Morea' after the autumn of 1824, so 1825 is read from the sentence, not written on the page; the convention to recall him followed Codrington's appearance 'early in August 1828', no signing day). Crete: occupation_start 1821 at confidence 1 (the page dates the appointment as governor, 'which he had occupied with a small Egyptian force', not the occupation) closed by occupation_end 1833-5 at Kutahya. The earlier note that no page dates Egyptian rule of Crete was wrong and is corrected. Disagreement kept: the counterpart for the Crete occupation is ottoman-empire (the island's sovereign, for whom the force held it), which is not a war enemy as for Syria 1832; no page names the Cretan insurgents as a state.
4. Tihama: gain 1833 from imamate-of-yemen (Yemen Eyalet page, 'new intervention by the Ottoman viceroy of Egypt in 1833 again wrested the coast from the ruler in Sana'a'; the page does not name Muhammad Ali or any town). The end: the Yemen Eyalet page is silent on any Egyptian withdrawal ('returned to the Tihama in 1849 after an absence of two centuries'); loss at 1840-11 (the Convention) at confidence 1, counterpart nobody. The 1834 and 1840 keyframes now add the Tihama.
5. Notes: the Hejaz and Najd sentence is corrected (ottoman-empire takes them in /ledger/163 and /ledger/169; emirate-of-diriyah gives them to muhammad-ali-dynasty in /ledger/18-23, /ledger/26 and /ledger/29). I disagree with nobody here, but the disagreement between those two dossiers stays open: this dossier records only a contest and draws the Hejaz from 1833, as Cliopatria does.
6. Area: no infobox on the History page (stated in the 1822 keyframe note); the Khedivate of Egypt infobox gives 5,000,000 km2 (inhabited areas only, no year) against 1,834,672 km2 for 1865, ratio 0.37, stated in the 1865 keyframe note and not used as a verdict.
7. Thin items: Najd moved from 1840 to a gain of 1838 at confidence 2 (Emirate of Nejd page: Faisal 'defeated and taken to Ottoman Egypt as a prisoner for the second time in 1838', Khalid bin Saud installed with Ottoman-Egyptian troops, undated), new keyframe muhammad-ali-dynasty_1839; Hasa stays a gain of 1840 at confidence 1 (the Nejd page does not mention Egyptian rule of Hasa); the loss of Najd and Hasa moved from 1842 to 1841 at confidence 1 (the page only says the Ottomans 'withdrew their military presence in the Arabian Peninsula' following the 1840 Convention of London; the reviewer's 1840-41 is not on any page). The 1865 dissolve stays at confidence 1: the Khedivate page says 8 June 1867 and is silent on 1866, the History page has a firman of 1866 on tribute and succession. The 1848 Sudan growth stays undated: the Turco-Egyptian Sudan page is silent on 1848 (Kassala and Taka 1840, Red Sea coast 1865).

Cliopatria rows to correct (unchanged)
- 1805-1810 shape (6 cells at Cairo) is wrong; replaced by the Egypt of the 1811 shape. The ottoman-empire dossier draws Egypt inside its own shape to 1810, so the two overlap and the renderer must choose the lighter tint.
- 1811, 1834, 1840 adjust; new keyframes 1820, 1821, 1839, 1841; 1822, 1842, 1848, 1865 ok.
- The dynasty ran to 1953 (History of Egypt page). The dossier ends in 1865 where Cliopatria's Khedivate of Egypt row begins in 1866; khedivate-of-egypt is another agent's dossier.

Disagreements and silences
- Convention of Kutahya: 5 May (Ottoman dossier's page), 14 May (History page), "May 1833" (Muhammad Ali page), and none on the war page whose infobox ends 8 April 1833. Ledger gives May 1833.
- Hejaz and Najd 1811-1833: three dossiers disagree (see point 5); the orchestrator should pick one holder.
- Overlap with turco-egyptian-sudan (another batch): that dossier is a state from July 1820 with muhammad-ali-dynasty as founding counterpart, and records Sennar (14-15 June 1821) and Kordofan the same way; this dossier keeps the Sudan inside the dynasty's shapes as Cliopatria does.
- Mamluk beys of Upper Egypt (extent and date driven out): on no page opened. They need a dossier.
- Ibrahim's conquest of Qatif and al-Hasa (Wahhabi War page, undated).
- Failed URL: https://en.wikipedia.org/wiki/Ottoman%E2%80%93Saudi_War (url_not_found). The article is Wahhabi_War.

## imamate-of-yemen (Cliopatria "Imamate of Yemen", 4 shapes, 1814..1872)

Cliopatria rows to correct
- The shapes contain the Tihama coast throughout. The pages say the coast was lost to the Wahhabis after 1803, regained temporarily in 1818, lost to Egypt in 1833 and taken by the Ottomans in 1849. Corrected keyframes (1814, 1815, 1870, 1871 adjust; new 1818 and 1833) remove it.
- Why the shape grows in 1815, and the extent held in the north (Sa'dah, Jizan and Najran are in the 1815 shape and on no page): page silent.

Same state or not
- The Qasimid state (Wikipedia: 1597-1849, "also known as the Imamate of Yemen") is the Zaydi imamate of Sana'a. Cliopatria has Qasimids 1636-1802 (Q5261548, dossier qasimids by another agent) and Imamate of Yemen 1814-1872 (Q1042069). Two dossiers, linked as predecessor and successor; the colour agent should give them one colour. The found event in 1814 is at confidence 1 (no page dates it) with qasimids as counterpart.
- The imamate did not end in 1872: al-Mutawakkil al-Muhsin (1855-1878), al-Hadi Sharaf ad-Din (1878-1890) and al-Mansur Muhammad (1890-1904) kept Upper Yemen under formal Ottoman recognition, and there was revolt again in 1904-05. A dossier for the highlands imamate 1873-1918 is missing (suggested slug imamate-of-upper-yemen; Cliopatria has no row between 1873 and 1918).
- The Ottoman dossier dates its Yemen gain 1873 (Cliopatria's year) against 1872 here.

Unsettled: who held the coast in 1840-1848 (pages silent; the Egyptian withdrawal is undated). No ruler strip: the Imams of Yemen page says "There is no uncontroversial list of imams of Yemen" and its list has overlapping reigns (al-Mansur Muhammad bin Abdallah 1853-1890 and al-Mutawakkil al-Muhsin 1855-1878). No infobox area on any page (the Yemen Vilayet figure of about 200,000 km2 is for a different entity).

## qatar-dynasty (Cliopatria "Qatar Dynasty", 5 shapes, 1820..1904)

Cliopatria rows to split
- The row is two things: the Qatar peninsula (48 gazetteer cells, 1820..1894) and a patch of 17-19 cells around Ras al-Khaimah and Fujairah that stays in the row to 1904 and is its only content from 1895. The patch is not Qatari on any page (the Al Qasimi page puts the Qawasim, whose seat was Ras Al Khaimah, there; it never mentions Qatar). Cliopatria also gives it to the Emirate of Nejd in 1853-1855. Corrected shapes drop it. Its owner (Qawasim of Ras al-Khaimah and Sharjah, or the Trucial States row, which covers only about 15 percent of the Ras al-Khaimah circle) is for the me-10 Trucial States dossier to settle.
- Verdicts: 1820, 1853, 1856 adjust; 1895 and 1900 wrong (no Qatar in them at all).
- The southern 20 cells of the peninsula that Cliopatria gives the Emirate of Nejd in 1853-1872 contradict the Emirate of Nejd page (peace of July 1851: the page says the Najd ruler 'agreed to stop interfering in Qatari affairs'). The Ottoman dossier also draws all of Qatar for the Ottomans from 1873.

Same state or not
- Wikidata Q846 is shared with Cliopatria's "Qatar" (1913-1915, dossier qatar) and "State of Qatar" (1973-2024, dossier state-of-qatar), both by other agents. The peninsula's polity is continuous in the pages (Al Thani since Mohammed bin Thani at Al Bidda in 1848, Ottoman province 1872-1913, British treaty 1916), so these are one state under three names. This dossier ends in January 1872 with the Ottoman province because the Ottoman dossier already owns the land from then; the Ottoman renunciation of 1913 restarts the sheikhdom (qatar).

Unsettled: the date and extent of Al Khalifa overlordship (claims, tribute to Najd, British recognition of Qatar as a dependent of Bahrain in 1861-62, Najd's dominion of June-July 1851; no boundary). Whether Qatar was a Bahraini vassal 1820-1868 (a vassal event belongs in the Bahrain dossier). Founding in 1820 is at confidence 1 (no page dates a founding). The Al Thani autonomy as Ottoman kaymakams and the Ottoman defeat at Al Wajbah in 1893 are on the History of Qatar page but fall outside the years of this dossier. Counterpart house-of-khalifa is a slug another agent will create (Cliopatria's bahrain row ends in 1845).

## Counterparts that need dossiers from another group

| name | suggested slug | years | group |
| --- | --- | --- | --- |
| Mamluk beys of Egypt | mamluk-beys-of-egypt | years not on any page opened | me-10-x |
| Imamate of Upper Yemen (Zaidi highlands) | imamate-of-upper-yemen | 1873-1918 | me-10-x |
| Qawasim, Emirate of Ras al-Khaimah and Sharjah | qawasim | years not on any page opened | me-10 Trucial States |
| Karabakh Khanate | karabakh-khanate | years not on any page opened | eu-19 |
| Ganja Khanate | ganja-khanate | years not on any page opened | eu-19 |
| Erivan Khanate | erivan-khanate | years not on any page opened | eu-19 |

## Region names the gazetteer lacks

Shusha, Anzali (Bandar-e Anzali), Mughan Plain, Talysh, Erivan Khanate, Quba (all qajar-dynasty; named in region text only); Suakin and Massawa (muhammad-ali-dynasty; named in note text only). Anzali also appears in persian-socialist-soviet-republic.

## Overlap with other dossiers to watch

- Egypt, Hejaz and Qatar are inside the ottoman-empire dossier's shapes while the Egyptian dossier also draws Egypt (to 1810), so overlap is intended and renderer-side.
- The Qajar occupation counterpart british-colonial-empire shares Wikidata Q8680 with british-empire; the string must match whichever slug sa-06 and eu-11 settle on.
