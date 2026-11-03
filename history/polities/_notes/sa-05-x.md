# sa-05-x notes: additions batch for the Mughals and Marathas (South Asia, about 1526-1857)

Agent: Phase B research agent for sa-05-x. No Cliopatria row owned. 25 new dossiers written, all validate with 0 errors (`python3 -I history/tools/validate_dossier.py`, with --resolve). Totals: 160 ledger events, 94 source entries (76 distinct pages), every keyframe new (`adjust`), every dossier `cliopatria_names: []`. Where a page gave a number (area, year) the shape was sized to it with the gazetteer (factor-of-two rule; all ratios between 0.8 and 1.7, most 1.0). Shapes are circles, latitude bands, Natural Earth admin1 cuts or hand polygons because the pages give no boundaries; every one says so in its keyframe note and in `certainty` (soft).

## Dossiers written (slug: years; pages opened; main gap)

| slug | years | pages | main unsettled item |
|---|---|---|---|
| gwalior-state | 1731-1948 | 13 | detached portions not drawn; 1805 Gwalior vs Gohad; 1885 vs 1886 Jhansi exchange; repaired 2026-10-25 (Doab, neighbour overlaps), Delhi-Agra block, northern zilas and Chanderi treaty dates still page-silent |
| indore-state | 1732-07 to 1948-06 | 7 | Holkar dominion before 1818 and the Mandsaur treaty terms not on any page opened |
| baroda-state | 1721-1949-05 | 5 | Kadi, Navsari, Amreli, Okhamandal dates (bridged 1802, 1808 at confidence 1); infobox area 3,239 km2 (1911) cannot be right |
| kingdom-of-nagpur | 1739-1853 | 6 | Berar, Chhattisgarh, Chanda, Sambalpur dates; shapes about 175-185k km2 vs 217,560 km2 |
| rohilkhand-state | 1721-1774-10 | 5 | extent before 1772 undated; 1742 Kumaon parganas added from the Kumaon page |
| bharatpur-state | 1722-11 to 1948-03 | 6 | loss of the Jat districts after 1774 undated; no infobox area |
| jaipur-state | 1028-1949-04 | 4 | no area; Shekhawati, Bundi, Rampura gains undated; Mughal-era extent |
| kalhora-dynasty | 1701-1783 | 5 | no area; Shikarpur, Sibi, Kachhi conquests undated; Kutch now an occupation 1765-1770 (cutch-state lacks the mirror); Nader Shah in wars only (1739) |
| travancore | 1729-1949-07 | 2 | annexations dated by year spans only (bands are readings) |
| kolhapur-state | 1710-1949-03 | 4 | no territory before 1901; Warna boundary; Treaty of Warna page failed |
| janjira-state | 1489-1948 | 2 | 1489 vs fort page dates; 1670 Mughal-era transfer not on pages |
| kingdom-of-cochin | 1100-1949-07 | 4 | no dates for 1102 founding or 1753 cession on the Cochin page; capital move 1341 vs 1405 |
| bikaner-state | 1465-1947-08 | 4 | 1805 Bhatner conquest, 1542 Jodhpur occupation, 1949 merger not on pages |
| garhwal-kingdom | 823-1949-08 | 4 | 1757-1770 Dun; extent of the British half (Pauri) 1815 |
| alwar-state | 1775-1948-03 | 2 | no capital or ruler table; Pratap Singh Naruka pages unusable |
| bhopal-state | 1707-1949-06 | 3 | extent before 1901; 1724 Nizam cession of "much of his territory" has no land (no ledger event) |
| satara-state | 1818-1848 | 4 | 1848 vs 1849 end; the Chhatrapati kingdom before 1818 is inside maratha-empire |
| cutch-state | 1147-1948-06 | 3 | Lakhiarviro unplaced; pre-1549 extent; Rann excluded by polygon |
| jaisalmer-state | 1156-1949 | 3 | no area before 1931; 1762 recovery of the fort has no land |
| kumaon-kingdom | 700-1791 | 3 | Terai dates 1638/1665/1673 (two are confidence 1); no area |
| rewa-state | 1140-1948-03 | 4 | extent before 1901; Sohagpur and Amarkantak dates (confidence 1) |
| jhansi-state | 1728-1858-04 | 3 | 1853 lapse vs control only in November 1858 |
| kota-state | 1631-1948-04 | 3 | 1631 extent; Jhalawar districts (parganas not named) |
| bundi-state | 1241-1949-04 | 2 | no territorial change after 1631 on the page |
| jhalawar-state | 1838-1949 | 2 | no end date or Rajasthan merger on the page; 1899 remnant is a reading |

Page budget: the brief allows 2-5 pages per new state; all 25 are inside it (the thinnest have 2). Where the pages are silent on territory the dossier says so; the reviewer should treat low page counts as budget-limited, not as skipped.

## Pages that failed (url_not_found, retried or tried the other title)

Battle_of_Maharajpur; Holkar_dynasty; Treaty_of_Mandsaur; Treaty_of_Mandeswar; Damajirao_Gaekwad; Maratha_conquest_of_Gujarat; Rohilkhand_Kingdom; Treaty_of_Warna; Hanumangarh_Fort; Dost_Mohammad_Khan_(Bhopal); Dost_Mohammad_Khan_(Nawab_of_Bhopal); Ali_Mohammad_Khan_Rohilla (the spelling Ali_Mohammed_Khan_Rohilla loads and is cited in rohilkhand-state); Baghela_dynasty; (repair 2026-10-25) Noor_Muhammad_Kalhoro and Nader_Shah%27s_invasion_of_the_Mughal_Empire (url_not_found; Noor_Mohammad_Kalhoro and Nader_Shah%27s_invasion_of_India load).
Loaded but unusable: Conquest_of_Sindh (the Arab conquest, not the British one); Pratap_Singh_Naruka and Pratap_Singh_Prabhakar (20th-century ruler text, accession date 7 April 1949 that matches Jaipur and not Alwar; not cited); Qudsia_Begum (a Delhi regent, not Bhopal; not cited). Kutch_State is the post-1948 state; Cutch_State is the princely state.

## Disagreements between pages (all recorded in the dossier notes)

- Gwalior State vs Gohad State on 1805; Gwalior State 1885 vs Jhansi State 1886 for the return of Jhansi city; area 68,291 vs 64,856 km2.
- Indore: founding 29 July 1732 / 1733 / 1730; accession 1 January 1948 / 1950 / 1947 / 16 June 1948; Bundi at Rajghat.
- Baroda: area 3,239 km2 (1911) on the state page.
- Nagpur: 1739 (infobox) vs 1743 (text). Doctrine of lapse page: Nagpur 1854 in the text and 1853 in its table (kingdom-of-nagpur ends 1853).
- Garhwal: 823 vs Kanak Pal 688-699; Sugauli 21 April 1815 (Garhwal page) vs drafted 2 December 1815 and signed 4 March 1816 (Sugauli page); Gorkhas out in 1814 (Garhwal page) vs 1815 (Sugauli page).
- Kumaon: Established 600 vs "Around 700"; Gorkha invasion 1791 (page) vs 1790; cession 1816 (page) vs 1815.
- Cochin: capital to Cochin 1341 vs 1405. Janjira: 1489 vs early 1100 and 1567. Kolhapur: 1707 / 1709 / 1710.
- Satara: annexation 1848 (text, Doctrine of lapse) vs 1849 (page introduction, infobox); Pratap Singh deposed 1838 vs 1839; coronation 9 April 1818 vs reign from 3 June 1818.
- Bhopal: infobox predecessor Maratha Empire vs text (Mughal 1707-1737); Sikandar and Shah Jahan Begum reign years.
- Kutch: merger 1 June 1948 vs 4 May 1948. Jaisalmer: treaty 11 vs 12 December 1818; end 1947 vs 1949 vs "Greater Rajasthan in 1950". Rewa: capital 1617 vs 1618; merger year absent.
- Jhansi: annexed 1853 vs British control November 1858 vs fort fell 5 April 1858.

## Cliopatria and other-group observations for the orchestrator

- I own no row. `talpur-dynasty` is a Cliopatria row (1820-1894) owned by a sibling part; I drafted a dossier before finding that and did NOT publish it (the draft was in my scratch directory only, so the sibling part must write it; the kalhora-dynasty dossier cites the same Talpur dynasty page).
- Members of the Maratha confederacy (gwalior, indore, baroda, nagpur, kolhapur, satara before 1818, bhopal 1737-1818, jhansi) lie inside the maratha-empire shape until 1818. The rendering agents must decide whether members are sub-units or tints.
- The gorkha-kingdom Cliopatria row ends in 1787 while the conquests of Kumaon (1791) and Garhwal (1804) are carried by the nepal dossier; garhwal-kingdom and kumaon-kingdom therefore use `nepal` as counterpart, not gorkha-kingdom.
- Existing Cliopatria slugs used as counterparts: mughal-empire, maratha-empire, british-empire, british-raj, republic-of-india, nawab-of-awadh, hyderabad-state, nepal, tibet, delhi-sultanate, kingdom-of-mysore (as a note), kingdom-of-marwar, nawabs-of-bengal (note).

## Counterparts and states that still need a dossier

From other groups or later passes: matsya-union (1948-03 to 1949-05; Alwar, Bharatpur, Dholpur, Karauli), vindhya-pradesh (1948-1956), madhya-bharat, travancore-cochin, rampur-state, gohad-state, gond-kingdom-of-deogarh, venad, rajasthan-union (1948; Kota's end), kutch-state (Part C 1948-1956), bhopal-state (Part C 1949-1956).
Candidate additions of this region and era with a Wikipedia article and no dossier: Orchha, Datia, Panna, Tonk, Karauli, Dholpur, Sawantwadi, Sirohi, Dhar, Dewas, Junagadh, Nawanagar, Bhavnagar, Pethapur, Jaitpur, Sambalpur, Chanda Gond, Kangra, Patiala and the Sikh states (check the Punjab groups first).

## Vassal and suzerainty records the suzerain dossiers should carry

(The suzerain records `vassal_start`/`vassal_end` with the vassal as counterpart.)
- mughal-empire: jaipur-state (1562-1710), bikaner-state (from Kalyan Mal, 1542-1571), bundi-state (title of Rao Raja 1569), bhopal-state (1707-1737).
- hyderabad-state: bhopal-state from 1723. kingdom-of-mysore: kingdom-of-cochin 1766-1790. maratha-empire: jaipur-state (chauth from 1732), bhopal-state 1737-1818, bundi-state (tribute demanded to 1817), baroda-state 1752-1802.
- british-empire / british-raj: gwalior-state 5 November 1817; indore-state 6 January 1818; baroda-state 15 March 1802; kingdom-of-nagpur 1818-1853; jaipur-state 1818; bikaner-state 9 March 1818; bundi-state 10 February 1818; jaisalmer-state 11/12 December 1818; kota-state 1817; jhalawar-state 1838; bhopal-state February-March 1818; cutch-state 1819; rewa-state 5 October 1812; alwar-state 1803; jhansi-state 1804 (treaty 18 November 1817) to 1853; satara-state 1818-1848; kolhapur-state after 1818 (and the 1812 treaty, undated on the pages); tehri garhwal (garhwal-kingdom) 1815-1816; travancore 1795; kingdom-of-cochin confirmed 6 May 1809; janjira-state 1870; bharatpur-state 1805 or 1826.
- portuguese-empire: kingdom-of-cochin protectorate 1503-1663 (Dutch alliance 1663-1795). durrani-empire: kalhora-dynasty 1748-1750.

## Gazetteer names needed (used as coordinates or polygon cuts instead)

Sheopur, Isagarh, Bhilsa, Narwar, Shajapur, Mandsaur, Amjhera, Chanderi, Broach, Hisar, Khargone, Mehidpur, Rampura, Bhanpura, Maheshwar, Bundi, Kota, Jhalawar, Rewa, Bandhavgarh, Sohagpur, Amarkantak, Kadi, Songadh, Amreli, Okhamandal, Kodinar, Pethapur, Dholpur, Mainpuri, Hathras, Murud, Janjira, Gowalkot, Anjanvel, Shrivardhan, Jafarabad, Chittur, Mahodayapuram, Thrissur (Trichur), Garhwal, Tehri, Uttarkashi, Chandpur Garhi, Kumaon, Champawat, Almora, Baijnath, Kashipur, Rudrapur, Doti, Anjar, Lakhiarviro, Khudabad, Islamnagar, Berasia. The gazetteer region "Kutch" includes the Great Rann (62,000 km2, three times the 1901 state area), so cutch-state uses a polygon cut to India instead.

## Notes on method

- Events without a land on the page are not ledger events (a loss needs a region): Bhopal's March 1724 cession to the Nizam and Jaisalmer's 1762 recovery of the fort are in the wars and notes only.
- Confidence 1 events are marked "page silent" and sit mostly in baroda, bharatpur, gwalior, jaipur (the Jat share of 1775), kumaon (Terai 1638, 1673; founding), rewa (Sohagpur and Amarkantak 1800, 1858), cochin and janjira.
- Dossiers that exist for pairs and chains should be read together: jaipur/alwar, kota/bundi/jhalawar, kumaon/rohilkhand/garhwal/nepal, gwalior/jhansi/kolhapur/satara.

## Repair of 2026-10-25 (review verdict fail: gwalior-state, kalhora-dynasty)

Files changed: history/polities/gwalior-state.json and history/polities/kalhora-dynasty.json only; both validate with 0 errors (--resolve: gwalior 2 warnings, the unwritten gohad-state and madhya-bharat; kalhora 0). No other dossier was touched (cutch-state, indore-state, bharatpur-state, bhopal-state, nawab-of-awadh and kingdom-of-marwar carry verdicts pass, thin or belong to other batches).

### gwalior-state

- Doab (KF 1788 and 1790, ledger 1788 gain and 1803 loss, the 1803 war zone): the gazetteer's whole Doab (536 cells, 135,554 km2) lay on the Nawab of Awadh's lower Doab. It is now the Doab less Cliopatria's Awadh 1796 shape and cut at about 26.6 N: about 49,800 km2, 197 cells. KF 1788 fell from 726 cells (about 183,600 km2) to 330 (83,457 km2); KF 1790 from 769 (about 194,500 km2) to 368 (93,067 km2); both now share 0 cells with the Cliopatria Awadh shapes of 1788, 1790, 1796 and 1800.
- Neighbour overlaps cut out: Bharatpur 60 km (29 cells) from the Agra and Mathura side, Indore State's Holkar districts (29 cells from 1767, 14 cells against indore-state's 1732-1766 circle) from the Malwa circles in every keyframe, Bhopal State's polygon (17 cells) from the Isagarh and Bhilsa circles, the Jaipur 90 km circle from the Ajmer circle (5 cells), the Jhansi 36 km circle from the Bundelkhand circle of the 1803 loss. The first Malwa keyframe is split at 1767 (gwalior-state_1731 for 1731-1766, gwalior-state_1767 for 1767-1782). The Ujjain city cell (the capital until 1810) lies inside Indore's 52 km circle and is kept in Gwalior: one shared cell with indore-state remains. Rescan against every polities/*.json keyframe: at most 2 shared cells with kota-state and jhansi-state at the edges of the Narwar and Sheopur circles (from the first drawing, not flagged by the reviewer).
- Areas after repair: 1731-1766 about 17,956 km2; 1767-1782 about 14,162; 1788-1789 about 83,457; 1790-1802 about 93,067; 1818-1843 about 60,949; 1844-1857 about 56,902; 1858-1948 about 59,179 km2 (ratio 0.87 to the 68,291 km2 infobox, 0.91 to the 64,856 km2 body text). The Malwa part (about 14,200 km2) is below the page's 20,774 km2 because the Malwa and Indore circles cannot both keep the page figures.
- Thin items tried, with the page (all opened again with WebFetch): Ajmer (ledger 1790) is now confidence 2 on the Battle of Merta page ("the rich province of Ajmer" given to the Scindias after the battle of 10 September 1790; the handover is undated) and its counterpart is kingdom-of-marwar instead of the unnamed Rajput kingdoms. Still confidence 1 because the pages are silent: the Delhi-Agra, upper Doab and Haryana block (Daulat Rao Scindia: only the 1803 cession "between the Yamuna and the Ganges" and "South Haryana"); Isagarh, Bhilsa, Narwar and Sheopur (Treaty of Gwalior: only the Asirgarh fort; Narwar: no transfer to the Scindias; Sheopur: the Gaurs ruled until they "succumbed to the Scindias", undated); the Chanderi treaty (Gwalior campaign: no treaty; Jayajirao Scindia: lands "including Chanderi District" worth 1.8 million ceded for a contingent force, no date, other lands ceded for war expenses). The Jayajirao Scindia page puts the Gwalior-fort-for-Jhansi exchange in 1886, as the Jhansi State page does; only the Gwalior State page says 1885 (events kept at 1885, noted).
- Where I differ from the reviewer: (1) the subtraction uses the Awadh 1796 shape, not the 1790 shape, because every nawab-of-awadh keyframe for 1788-1800 contains the 1796 shape (the 1790 shape leaves 79 cells of Rohilkhand-side Doab that Awadh holds from October 1774, nawab-of-awadh ledger 5); (2) the cut at 26.6 N is mine: the gazetteer region Doab spills 86 cells south of the Yamuna (Jhansi, Banda, Hamirpur, 25.3 to 26.6 N), which is Bundelkhand, not Doab; (3) the Indore cut is applied to all Malwa shapes from 1731, not only KF7 to KF9, because the same circles overlap from 1732 on.

### kalhora-dynasty

- Kutch: the "northern half of Kutch district" is no longer in the 1736-1783 shape (36 cells, about 9,100 km2 of cutch-state's mainland, no event in either dossier). The Kalhora page dates it to no year ("The northern half of Kutch district was also under the Kalhora Dynasty"). The Cutch State page, opened again, dates the only evidence: Ghulam Shah Kalhoro attacked Cutch in 1763-64 (battle near Jara) and in 1765, Rao Godji II "had to make a truce with him after losing several territories", and after the 1770 marriage the Mian returned "the towns of Busta Bandar and Lakhpat" and other conquered territories (the handover has no year of its own). The Kalhora ledger now carries occupation_start 1765 (confidence 1, bridged to the second attack) and occupation_end 1770 (confidence 2) with counterpart cutch-state over the northern Kutch mainland (north of 23.4 N, inside cutch-state's polygon) and a 25 km circle at Lakhpat (about 11,100 km2), and a war entry for the attacks.
- Where I differ from the reviewer: it asked for a loss/gain pair in both dossiers if a page shows Kalhora rule on the mainland. The page shows a conquest handed back by a ruler whose state went on, so I used an occupation (hatched), and did not edit cutch-state (verdict pass; the repair brief leaves pass dossiers untouched). cutch-state needs occupation_start 1765 and occupation_end 1770 with counterpart kalhora-dynasty; its wars already list the Kalhora attacks of 1763-65.
- Thin items tried: Noor_Mohammad_Kalhoro (the Muhammad spelling returns url_not_found) lists the conquests of Sindh (Thatta from the Mughal governor, the Bakhar and Sehwan sarkars, Shikarpur from the Daudpotras, Sibi and Kachhi, Shahbandar, an invasion of Kutch) without any year, and dates the title Nawab Khuda-Yar Khan to 1737 "after taking Thatta" against 1736 on the Kalhora page; the all-Sindh gain therefore stays at 1736, confidence 1. Nader Shah's 1739 invasion is added to the wars ("Mian fled to Umerkot for shelter but was captured by the King of Iran"); the Nader Shah's invasion of India page names no Sindh cession (it annexes "all lands west of the Indus" in 1738-1739 and returns the east on 16 May 1739), so there is no ledger event. Ghulam Shah's reign (1758-1772, Kalhora table) covers the Kutch attacks. New 4-cell edge overlap with jaisalmer-state (the Jaisalmer circle against the Sindh border, present since the first pass).

### Follow-ups for other dossiers and the gazetteer

- cutch-state: add the Kalhora occupation 1765-1770 (above). kingdom-of-marwar: add a 1790 loss of Ajmer to gwalior-state (Battle of Merta page). indore-state: trim the Indore circle so that Ujjain city is outside it. kota-state and jhansi-state: 2-cell overlaps with the Narwar, Sheopur and Gwalior circles. talpur-dynasty (a sa-05 Cliopatria row) must start in 1783; gohad-state and madhya-bharat are still unwritten.
- Gazetteer names needed: Lakhpat (place, about 23.82 N 68.78 E), Busta Bandar (place, a Kutch port named on the Cutch State page, location not found), Upper Doab (region: the Ganges-Jamuna Doab north of about 26.6 N; the gazetteer's Doab spills across the Yamuna into Bundelkhand).

