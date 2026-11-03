# Review of batch sa-05-e (Nawabs of Bengal, Hyderabad State, Nawab of Awadh, Sikh Confederacy)

Reviewer, 2026-10-25. The validator (with --resolve) gave 0 errors for all four dossiers. Pages opened: Nawabs of Bengal, Maratha invasions of Bengal, Battle of Plassey, Bengal Subah, Northern Circars, Battle of Kharda, Asaf Jah II, Hyderabad State, Ceded Districts, Berar Province, Rohilla War, Ceded and Conquered Provinces, Shuja-ud-Daula, Nawab of Awadh, Wajid Ali Shah, Battle of Sirhind (1764), Bhangi Misl, Misl, Sikh Empire. Every event spot-checked said on its page what its note claims, with the year: nothing was fabricated or mis-dated at confidence 3.
Neighbour dossiers read: mughal-empire, maratha-empire, gorkha-kingdom, carnatic-sultanate, kingdom-of-mrauk-u, durrani-empire, nepal, sikh-empire, english-colonial-empire, plus rohilkhand-state and kingdom-of-nagpur (real counterparts). Not written yet (exception): french-india, british-empire, kingdom-of-mysore, dutch-republic, british-colonial-empire, danish-india, republic-of-india.

## nawabs-of-bengal: fix

Area: infobox 386470 (1781) against Cliopatria 381064, ratio 1.01. Nawabs of Bengal infobox gives no area; Bengal Subah infobox 'c. 1781: 386,470 km2' against nawabs-of-bengal_1757 (381,064 km2) and _1752 (384,515 km2); cited in sources[].

Findings:
- `/wars/2` (applied by the reviewer, not blocking): The war 'Battle of Buxar' (1764-1765) lay outside the life (1717 to June 1757); the validator warned. Evidence: Identity end 1757-06 (Plassey); the war's own entry dates it 22-23 October 1764 and the Treaty of Allahabad 1765, and nawab-of-awadh already carries it. Fix: Removed the war and recorded it in notes for nawab-of-awadh and british-empire; re-validated with 0 errors and 0 warnings.
- `/ledger/6` (applied by the reviewer, not blocking): The note said the page does not date the post-Plassey treaty, and the event had no month. Evidence: Battle of Plassey page: 'The treaty with Mir Jafar was signed on 4 June 1757'; the land grant ('all the land within the Maratha Ditch and 600 yards beyond it', 'the zamindari of all the land between Calcutta and the sea') took effect after the battle of 23 June 1757. Fix: Added month 6 and corrected the note; ledger order unchanged; re-validated.

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Nawabs_of_Bengal: confirmed: table row 'Annexation of Bihar (1733)' / 'Annexation of the Bihar Subah into the territory of the nawabs of Bengal'
- `/ledger/5` https://en.wikipedia.org/wiki/Nawabs_of_Bengal: confirmed: Orissa 'formally incorporated in the Maratha Empire in 1752' (the January 1747 cession sentence is on the page too and was rightly set aside)
- `/ledger/4` https://en.wikipedia.org/wiki/Maratha_invasions_of_Bengal: confirmed: treaty signed 'in May or June 1751', Subarnarekha limit, Mir Habib governor, 'de facto Maratha control over Orissa was established by 1751'
- `/ledger/7` https://en.wikipedia.org/wiki/Battle_of_Plassey: confirmed: 23 June 1757; infobox 'Bengal came under de facto control of the British East India Company'
- `/ledger/6` https://en.wikipedia.org/wiki/Battle_of_Plassey: confirmed (land grant); the treaty date 4 June 1757 is on the page, fixed

## hyderabad-state: thin

Area: infobox 214187 (1941) against Cliopatria 211298, ratio 1.01. Hyderabad State infobox '1941: 214,187 km2' against hyderabad-state_1947; quoted in keyframe_review/19.

Findings:
- `/ledger/7/counterpart` (applied by the reviewer, not blocking): The 1804 Berar gain named maratha-empire as counterpart, but the page has the Company transfer the land to the Nizam. Evidence: Berar Province page: the Bhonsla raja was forced 'to cede his territories south of Gawilgarh and Narnala Fort and east of the Wardha River' and by the 1804 partition treaty between the Nizam and the British 'these ceded territories in Berar were transferred in perpetual sovereignty to the Nizam'; kingdom-of-nagpur /ledger/8 records the loss of 'southern Berar' to british-empire in December 1803. Fix: Counterpart changed to british-empire with a note; re-validated (0 errors, the known occupation warning only).
- `/wars, /ledger (1760)` (for the author, not blocking): The Battle of Udgir (1760) and the cession after it are missing, though two pages the author opened carry it and maratha-empire records a 1760 gain from hyderabad-state. Evidence: Asaf Jah II page: the Nizam was defeated 'again at the Battle of Udgir in 1760'; Berar Province page: certain districts were 'ceded to the Maratha Peshwa in 1760 and 1795'; maratha-empire /ledger/31 (3 January 1760, c2, Battle of Udgir page): 'territory worth 60 lakhs, including the cities of Ahmadnagar, Daultabad, Burhanpur and Bijapur'. Daulatabad lies inside the Aurangabad disc that every keyframe 1724-1794 adds. Fix: Add the war 'Battle of Udgir' (1760, hyderabad-state v maratha-empire) and a 1760 loss to maratha-empire for the land the Battle of Udgir page names that the Nizam's drawn shape holds (at least Daulatabad); say in a note how Daulatabad came back before the 1795 Kharda cession, or take it out of the 1760-1794 keyframes.
- `/ledger (1759)` (for the author, not blocking): The British capture of Masulipatnam in 1759 is missing although it is on the Northern Circars page the author used. Evidence: Northern Circars page: 'In 1759, through the conquest of the fortress of Masulipatnam, the maritime provinces from the river Gundlakamma to the Chilka Lake were transferred from the French to the British. But the British left them under the administration of the Nizam, except Masulipatnam, a valuable port, which was retained by the British.' english-colonial-empire /ledger/59 has a 1763 gain of Masulipatnam from hyderabad-state at c1. Fix: Add a 1759 loss of Masulipatnam (a small disc) to british-empire at c3 from the Northern Circars page, and exclude it from the 1759-1768 keyframes; ask the english-colonial-empire owner to move its c1 1763 gain to 1759.

Gaps for a gap-filler:
- `/ledger/4, /keyframe_review/9-12`: The 1792 gain from Mysore leaves no trace in the keyframes: Cliopatria holds the Krishna-Penner land (Bellary, Cuddapah, Kurnool, Anantapur) from 1727, but the Treaty of Seringapatam page has Tipu hand it to the Nizam in 1792. The years Mysore (Hyder Ali) took Bellary, Gooty and Cuddapah are needed to take the land out of the keyframes for those years (unverified: page budget). Try https://en.wikipedia.org/wiki/Hyder_Ali
- `/ledger/8`: Confidence-1 bridge: the year the Daulatabad-Aurangabad-Solapur country and the rest of Marathwada came back to the Nizam after Kharda (1795). Try https://en.wikipedia.org/wiki/Nana_Fadnavis
- `/ledger/9`: The occupation of Berar (1853) has no end: the British left India in August 1947 and Berar stayed in India's Central Provinces and Berar; close it (1947, british-empire) and decide how 1947-1948 is drawn. Try https://en.wikipedia.org/wiki/Central_Provinces_and_Berar
- `/ledger (1753)`: Salabat Jang's grant of Kondavid and then 'the other circars' to the French (undated on the Northern Circars page; about 1753) and their status to 1759; french-india (sa-06) has no dossier yet. Try https://en.wikipedia.org/wiki/Charles_Joseph_Patissier,_Marquis_de_Bussy-Castelnau
- `/ledger`: The Nizam's overlordship of the Carnatic Sultanate ('under the legal purview of the Nizam of Hyderabad', left unsettled by both dossiers): a vassal_start/vassal_end pair if a page dates it. Try https://en.wikipedia.org/wiki/Carnatic_Sultanate

Spot checks:
- `/ledger/2` https://en.wikipedia.org/wiki/Northern_Circars: confirmed: 'signed on 1 March 1768', the Nizam 'acknowledged the validity of Shah Alam's grant'
- `/ledger/3` https://en.wikipedia.org/wiki/Northern_Circars: confirmed: Basalat Jang 'died in 1782, but it was not till 1788 that Guntur came under British administration'
- `/ledger/5` https://en.wikipedia.org/wiki/Battle_of_Kharda: confirmed: 11 March 1795; 'cede territory of Daulatabad, Aurangabad, and Solapur'; negotiations 'concluded in April 1795'; the page does not mention a later restoration
- `/ledger/6` https://en.wikipedia.org/wiki/Ceded_Districts: confirmed: ceded by Nizam Ali Khan in 1800 (no month); subsidiary alliance 1796; districts Anantapur, Kadapa, much of Kurnool, Bellary, Pavagada
- `/ledger/7` https://en.wikipedia.org/wiki/Berar_Province: confirmed year and land (1804 partition treaty); counterpart corrected
- `/ledger/10` https://en.wikipedia.org/wiki/Hyderabad_State: confirmed: Operation Polo 13-17 September 1948; infobox 'Annexation 18 September 1948'

## nawab-of-awadh: thin

Area: infobox None (None) against Cliopatria 115930, ratio None. No area on the Nawab of Awadh infobox or page; the author's area reasoning (47,000 km2 rump) is flagged in keyframe_review/16.

Findings:
- `/ledger/1, /ledger/6, /ledger/7, /keyframe_review/1-9` (for the author, not blocking): The Benares country is modelled twice: a vassal_start in 1737 makes it Awadh's vassal (lighter tint), while every keyframe 1737-1774 keeps it as direct Awadh land (verdicts ok), and in 1775 it gets both a vassal_end and a loss. Evidence: Schema: vassal_start means the region 'becomes this state's vassal ... drawn in the lighter tint'; the keyframes nawab-of-awadh_1727 to _1772 include the area that the 1775 shape loses (28,072 km2). Benares State page: the rulers 'were originally Zamindars for the Awadh province'. Fix: Pick one reading: either keep Benares as direct land (drop the vassal_start/vassal_end pair; keep the 1775 loss) or as a vassal (take minus [Awadh 1772, Awadh 1775] out of the keyframes from 1737 and replace the 1775 loss by the vassal_end alone, the Company's suzerainty going in british-empire).
- `/ledger/2, /ledger/8` (for the author, not blocking): The Kora-Allahabad districts are lost to british-empire in 1765 but regained from mughal-empire in 1775, without a transfer between the two in either dossier. Evidence: Shuja-ud-Daula page: the treaty 'said that Kora and Allahabad district would go to Company'; Shah Alam II page: he 'later also handed over the districts of Allahabad and Kora to the Nawab of Awadh'. The two pages name different holders. Fix: Open the Treaty of Allahabad page to settle who held the districts 1765-1773 and the year they returned to Awadh; make the 1765 and the later counterpart agree, and raise /ledger/8 above confidence 1 if the year is found.

Gaps for a gap-filler:
- `/ledger/8`: Confidence 1: the year Kora, Allahabad and the Doab came back to Awadh (Cliopatria's 1775; historically the Treaty of Benares, 1773), and from whom. Try https://en.wikipedia.org/wiki/Treaty_of_Allahabad
- `/keyframe_review/12`: Cliopatria removes 4,299 km2 of the northern Tarai (80.75-82.24 E) in 1788 with no ledger event on either side (nepal and gorkha-kingdom have no gain from nawab-of-awadh): either find the transfer or restore the strip to Awadh. Try https://en.wikipedia.org/wiki/Asaf-ud-Daula
- `/keyframe_review/16`: The 1801-1856 rump is drawn at about 47,000 km2 by cells; the note says the historical rump is larger, but no page gives its area. Try https://en.wikipedia.org/wiki/Saadat_Ali_Khan_II
- `/ledger/1`: The Benares country before 1737 (Cliopatria draws it in Awadh from 1727): unverified, page budget. Try https://en.wikipedia.org/wiki/Benares_State

Spot checks:
- `/ledger/5` https://en.wikipedia.org/wiki/Rohilla_War: confirmed: Miranpur Katra 23 April 1774; 'Rohilkhand fell to Awadh, and was plundered and occupied'; Lal Dang 7 October 1774
- `/ledger/10` https://en.wikipedia.org/wiki/Ceded_and_Conquered_Provinces: confirmed: 1801 cession by Saadat Ali of the Gorakhpur and Rohilkhand divisions, Allahabad, Fatehpur, Cawnpore, Etawah, Mainpuri, Etah (the page also lists 'the southern part of Mirzapur' and 'the terai parganas of Kumaun')
- `/ledger/2` https://en.wikipedia.org/wiki/Shuja-ud-Daula: confirmed as quoted: 16 August 1765, 'Kora and Allahabad district would go to Company'
- `/ledger/12` https://en.wikipedia.org/wiki/Wajid_Ali_Shah: confirmed: 'annexed by the EIC on 11 February 1856' (7 February only in the bottom table)
- `/ledger/11` https://en.wikipedia.org/wiki/Nawab_of_Awadh: confirmed: 'Oudh State eventually declared itself independent from the rule of the Mughal in 1818'

## sikh-confederacy: thin

Area: infobox None (None) against Cliopatria 63122, ratio None. No area on the Misl page or infobox.

Findings:
- `/keyframe_review/8, /keyframe_review/9, /keyframe_review/10` (applied by the reviewer, not blocking): Shapes after the 1799 end were marked adjust (1800) and ok (1803, 1806), which says they are right for the Sikh Confederacy in years the dossier says it no longer existed. Evidence: Identity end 1799 (Misl infobox '1748-1799'); schema: 'wrong: the shape should not be used for these years; correction gives ... the years it belongs to'; the author's own notes call them remnant misls. Fix: Verdicts set to wrong, with corrections giving the unchanged shape and the owner (Bhangi misl at Amritsar 1800-1802; an unidentified remnant round Kasur 1803-1806); re-validated with 0 errors and 0 warnings.
- `/keyframe_review/0` (for the author, not blocking): The 1748-1761 core includes the Kasur disc from 1748, but the ledger gains Kasur only in 1761. Evidence: Bhangi Misl page: 'In 1761, the Bhangi chief Hari Singh captured Kasur and nearby areas of Ferozepore'; ledger /ledger/0 founds the state on Amritsar alone. Fix: Make keyframe 0 Amritsar only (1748-1760) and add a 1761 keyframe with Amritsar plus Kasur.

Gaps for a gap-filler:
- `/keyframe_review/0 to /keyframe_review/1`: Between the 1748-1761 core (two discs, about 8,000 km2) and Cliopatria's 1762 shape (63,071 km2 less Lahore) about 52,000 km2 appear with no gain or contest event, in the year of the Vadda Ghalughara; durrani-empire has a contest 1762-1767 and a 1772 loss to sikh-confederacy. Thin by page budget (5 pages). Try https://en.wikipedia.org/wiki/Jassa_Singh_Ahluwalia
- `/ledger`: The Misl page says 'The Bhangis conquered Multan and held it until 1780', and 'Jassa Singh Ahluwalia conquered Fatehabad in 1753' (inside the Amritsar disc). Multan is neither in the shapes nor in the ledger: the conquest year and the 1780 loss to the Durrani are missing. Try https://en.wikipedia.org/wiki/Multan
- `/keyframe_review/6`: 1772-1798 detail of the city-patch shape (27 years without an event); unverified: page budget. Try https://en.wikipedia.org/wiki/Sukerchakia_Misl
- `/ledger/2, /ledger/5`: Lahore's holder before 1765 (Durrani is the researcher's inference) and the Kasur holder before 1761. Try https://en.wikipedia.org/wiki/Kasur

Spot checks:
- `/ledger/3` https://en.wikipedia.org/wiki/Battle_of_Sirhind_(1764): confirmed: 14 January 1764; Sirhind 'handed over the land to Maharaja Ala Singh of Patiala State'; 'established their rule between the rivers Satluj and Yamuna'
- `/ledger/1` https://en.wikipedia.org/wiki/Bhangi_Misl: confirmed: 'In 1761, the Bhangi chief Hari Singh captured Kasur and nearby areas of Ferozepore'
- `/ledger/5` https://en.wikipedia.org/wiki/Bhangi_Misl: confirmed: 16 April 1765, Gujjar Singh, Lehna Singh Kahlon and Sobha Singh take Lahore
- `/ledger/6` https://en.wikipedia.org/wiki/Sikh_Empire: confirmed: 'In 1799, Ranjit Singh of the Sukerchakia Misl captured Lahore from the Sikh triumvirate' (infobox 7 July 1799)
- `/ledger/7` https://en.wikipedia.org/wiki/Misl: confirmed: infobox 1748-1799, 'Ranjit Singh unites the Sikh Confederacy into the Sikh Empire'

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| nawabs-of-bengal 1717 found (mughal-empire) | mughal-empire 1717 loss | mismatch | Mughal /ledger/110 gives 'Bengal, Bihar and Orissa' in 1717; Bengal founds on Bengal and Orissa and takes Bihar in 1733 (Nawabs page table). Mughal should drop Bihar from 1717 and add a 1733 loss. |
| nawabs-of-bengal 1733 gain (mughal-empire) | none | mismatch | No 1733 Bihar loss in mughal-empire (see 1717 row). |
| nawabs-of-bengal 1742 contest_start (maratha-empire) | maratha-empire 1742 contest_start | matched | maratha /ledger/26 (April 1742). kingdom-of-nagpur /ledger/1 also records it against nawabs-of-bengal. |
| nawabs-of-bengal 1751 contest_end (maratha-empire) | maratha-empire 1751 contest_end | matched | maratha /ledger/27; kingdom-of-nagpur /ledger/2 (June 1751) too. |
| nawabs-of-bengal 1752 loss (maratha-empire) | maratha-empire 1752 gain | matched | maratha /ledger/28. Double claim: kingdom-of-nagpur /ledger/3 gains the same Orissa from nawabs-of-bengal in June 1751; the orchestrator must pick one holder (the pages say the Nagpur Bhonsles) and Bengal's counterpart follows. |
| nawabs-of-bengal 1757 loss (british-empire) | none | exception | british-empire (sa-06) not written yet. |
| hyderabad-state 1724 found (mughal-empire) | mughal-empire 1724 loss | matched | mughal /ledger/113. |
| maratha-empire 1739 gain (hyderabad-state) | none | mismatch | maratha /ledger/23 (Khargone and Handia, Baji Rao I page, c3) has no loss in hyderabad-state; the land lies north of every Hyderabad shape (max 20.2 N). Either the counterpart is mughal-empire or Hyderabad must add the land. |
| maratha-empire 1760 gain (hyderabad-state) | none | missing | maratha /ledger/31 (Udgir: Ahmadnagar, Daulatabad, Burhanpur, Bijapur); hyderabad-state has no 1760 loss (finding on hyderabad-state). |
| english-colonial-empire 1763 gain (hyderabad-state) | none | mismatch | english-colonial-empire /ledger/59 (Masulipatnam, c1); the Northern Circars page dates the capture to 1759; hyderabad-state has no loss (finding). |
| hyderabad-state 1768 loss (british-empire) | none | exception | british-empire not written yet. |
| hyderabad-state 1788 loss (british-empire) | none | exception | british-empire not written yet. |
| hyderabad-state 1792 gain (kingdom-of-mysore) | none | exception | kingdom-of-mysore (sa-05) has no dossier yet. |
| hyderabad-state 1795 loss (maratha-empire) | none | missing | maratha-empire has no 1795 gain of Daulatabad, Aurangabad and Solapur from hyderabad-state (Battle of Kharda page). |
| hyderabad-state 1800 loss (british-empire) | none | exception | british-empire not written yet. |
| hyderabad-state 1804 gain (british-empire) | kingdom-of-nagpur 1803 loss | exception | Counterpart corrected to british-empire (not written yet); the chain is kingdom-of-nagpur /ledger/8 (December 1803, 'southern Berar' to british-empire) then the 1804 partition treaty. |
| hyderabad-state 1805 gain (maratha-empire) | none | missing | c1 bridge; maratha-empire has no loss to hyderabad-state 1795-1805 and draws Aurangabad to 1804. |
| hyderabad-state 1853 occupation_start (british-empire) | none | exception | british-empire not written yet. |
| nawab-of-awadh 1722 found (mughal-empire) | mughal-empire 1722 loss | matched | mughal /ledger/112. |
| nawab-of-awadh 1737 vassal_start (benares-state) | none | exception | benares-state has no dossier; listed in counterparts_needing_dossiers. |
| nawab-of-awadh 1765 loss (british-empire) | none | exception | british-empire not written yet; the holder (Company or Shah Alam II) is disputed between the pages. |
| nawab-of-awadh 1774 contest_start (rohilkhand-state) | rohilkhand-state 1774 contest_start | matched | rohilkhand /ledger/4. |
| nawab-of-awadh 1774 gain (rohilkhand-state) | rohilkhand-state 1774 loss | matched | rohilkhand /ledger/5 (April 1774) against Awadh October 1774, within a year; contest_end and dissolve also match (/ledger/7, /ledger/8). |
| nawab-of-awadh 1775 vassal_end (benares-state) | none | exception | benares-state has no dossier. |
| nawab-of-awadh 1775 loss (british-empire) | none | exception | british-empire not written yet. |
| nawab-of-awadh 1775 gain (mughal-empire) | none | missing | c1; mughal-empire has no 1772-1775 loss of Kora/Allahabad/Doab to nawab-of-awadh. |
| nawab-of-awadh 1801 loss (british-empire) | none | exception | british-empire not written yet. |
| nawab-of-awadh 1856 loss (british-empire) | none | exception | british-empire not written yet. |
| sikh-confederacy 1761 gain (Kasur (holder not named on the page)) | none | exception | Free-text counterpart; the page names no holder. |
| sikh-confederacy 1761 contest_start (durrani-empire) | durrani-empire 1762 contest_start | matched | durrani /ledger/19, one year apart. |
| sikh-confederacy 1764 gain (durrani-empire) | durrani-empire 1772 loss | mismatch | durrani /ledger/27 gives 'the Indian Punjab and Sirhind lands' in 1772; Sirhind fell on 14 January 1764 (Battle of Sirhind page). durrani-empire should add a 1764 loss of Sirhind. |
| sikh-confederacy 1765 gain (durrani-empire) | none | mismatch | No 1765 Lahore loss in durrani-empire (its 1772 loss is the nearest). |
| sikh-confederacy 1765 contest_end (durrani-empire) | durrani-empire 1767 contest_end | mismatch | durrani /ledger/22 ends the contest in 1767, two years later. |
| sikh-confederacy 1799 loss (sikh-empire) | sikh-empire 1799 found | matched | sikh-empire /ledger/0 (July 1799, Lahore, counterpart sikh-confederacy). |
| sikh-empire 1800 gain (sikh-confederacy) | none | mismatch | sikh-empire /ledger/2 (c1) and /ledger/3 (1802, Amritsar, c3) take land from sikh-confederacy after its 1799 dissolve; the counterpart should be bhangi-misl (Amritsar) or the remnant misls, or the 1800 core should pass at the 1799 dissolve. |

## Problems for the orchestrator

- No page failed to load for the reviewer.
- The Bhonsle state has a dossier as kingdom-of-nagpur; the author's report suggests 'nagpur-kingdom' and maratha-empire's successors say 'nagpur-state': one slug is needed. kingdom-of-nagpur and maratha-empire both gain Orissa from nawabs-of-bengal (1751 and 1752): the orchestrator should give the event to one of them.
- sikh-empire (sa-05-f) gains from sikh-confederacy in 1800 and 1802, after this dossier's 1799 end: route to the sikh-empire owner.
- Cliopatria's 1788 transfer of an Awadh Tarai strip (4,299 km2) to its Nepal row has no event in any dossier; nepal, gorkha-kingdom and nawab-of-awadh are all silent.
- Author's report counts are stale after the reviewer fixes: sikh-confederacy keyframe_verdicts are now ok 0, adjust 8, wrong 3; nawabs-of-bengal has 2 wars.
- Reviewer edits applied in place: nawabs-of-bengal (wars/2 removed; ledger/6 month 6), sikh-confederacy (keyframe_review/8-10 verdict wrong), hyderabad-state (ledger/7 counterpart british-empire); each re-validated with 0 errors and read back.

## Counterparts needing dossiers

- Bhangi Misl (bhangi-misl, 1748-1810)
- Sukerchakia Misl (sukerchakia-misl, 1748-1799)
- Patiala State (Phulkian) (patiala-state, 1763-1799)
- Benares State (benares-state, 1737-1775)
- Rampur State (rampur-state, 1774-1799)
- Awadh rebel government of 1857-58 (awadh-rebel-government, 1857-1858)
- Remnant principality round Kasur (Cliopatria 'Sikh Confederacy' 1803-1806 shapes), unidentified (slug to be decided, 1803-1806)
