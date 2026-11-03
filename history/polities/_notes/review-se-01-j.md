# Review of batch se-01-j (2026-10-19)

Reviewer: adversarial review of rattanakosin-kingdom, nguyen-dynasty, burma, union-of-burma. Validator: 0 errors on all four; warnings are Dan Sai (gazetteer) and the declared split of the Cliopatria row Burma. Neighbour dossiers read: kingdom-of-luang-phrabang, kingdom-of-champasak, vientiane, konbaung-dynasty, cambodia, post-angkor-cambodia, tay-son-dynasty, thonburi-kingdom, champa, nguyen-lords (others in section 6 of the brief are not written yet).

## rattanakosin-kingdom: thin

Area: infobox 1119354 km2 (1805) against Cliopatria 430003 km2, ratio 0.38, acknowledged True. Factor 2.6 acknowledged in keyframe 1 (infobox counts tributaries drawn by Cliopatria as separate polities); 1893: 726,621 vs 659,741 (0.91).

Findings:
- `/ledger/26` (applied by reviewer): contest_start of the Franco-Siamese crisis dated June 1893 and its note said the page names no French campaign that took ground before 13 July. Evidence: Franco-Siamese War page: 'Lanessan sent three military columns into the disputed region to assert French control in April 1893' and the first was 'successful in evicting the Siamese commissioner at Khammuan by 25 May'; Grosgurin was killed on 5 June. Fix: Month 5 (first ground held), note rewritten with the April columns and 25 May; done by the reviewer, dossier re-validated (0 errors).
- `/ledger/9` (for the author/orchestrator): The 1793 loss of the Tenasserim Coast to konbaung-dynasty has no prior gain or occupation in the ledger, so the map would show Siam losing land it never held; the konbaung-dynasty dossier has no mirror. Evidence: Rattanakosin page: the Burmese governors of Tavoy and Mergui defected to Siam in 1792 and Siam temporarily occupied the coast; 'The Siamese were soundly defeated by the Burmese in the Battle of Tavoy in 1793 and ceded the Tenasserim Coast to Burma'. Fix: Add a 1792 occupation_start (Tavoy and Mergui, counterpart konbaung-dynasty, conf 2) and turn the 1793 loss into the occupation_end (or drop the event); add the war (Burmese-Siamese War 1792-1794) with that zone.
- `/wars` (for the author/orchestrator): The Siamese invasion of southern Vietnam of 1784-1785 is missing from wars and ledger; tay-son-dynasty carries contest_start rattanakosin-kingdom 1784 and contest_end rattanakosin-kingdom 1785-01 with no mirror here. Evidence: Rattanakosin page: 'In 1784, Siamese forces invaded Saigon to reinstate Nguyen Phuc Anh' but 'were defeated in the Battle of Rach Gam-Xoai Mut by the Tay Son'. Fix: Add the war and a contest_start 1784 / contest_end 1785-01 pair with counterpart tay-son-dynasty over the Mekong delta (Gia Dinh), citing the Rattanakosin page.
- `/ledger/12` (for the author/orchestrator): The Lao rebellion contest names only vientiane; kingdom-of-champasak carries contest_start rattanakosin-kingdom 1827-01, contest_end 1828 and a 1828 loss to Siam (conf 1) with no mirror here. Evidence: Lao rebellion page as quoted in the champasak dossier: 'the Lao armies of the kingdoms of Vientiane and Champasak moved south and west across the Khorat Plateau' in January 1827. Fix: Add champasak to the war's belligerents and a contest pair with counterpart kingdom-of-champasak (1827-01 to 1828), or agree with the champasak author that its 1828 loss is a vassal re-imposition.

Gaps for a gap-filler:
- `/ledger/0-3`: Vassal spans of 1782 over Vientiane, Luang Phrabang and Champasak are unmirrored; Luang Phrabang's dossier records Siamese occupations 1791-1792 and 1793-1794 that this ledger lacks. Try https://en.wikipedia.org/wiki/Kingdom_of_Luang_Phrabang
- `/ledger`: Siamese suzerainty over Cambodia from Ang Eng's installation in 1794 to the 1811-1812 turn to Hue is absent (the first Cambodian vassal_start is 1848). Try https://en.wikipedia.org/wiki/Post-Angkor_period
- `/keyframe_review/7`: Lampang, Lamphun, Nan and Phrae (140 cells) are drawn as direct Siamese land 1782-1899 although the Chiang Mai page has Lampang and Lamphun as Chet Ton princedoms and Nan and Phrae under their own dynasties until the 1894-1899 reforms. Try https://en.wikipedia.org/wiki/Nan_Kingdom
- `/keyframe_review/2`: Kengtung, Chiang Hung and Sipsong Panna tributary status (the page says the kingdom reached the Shan States and southern Yunnan in 1805-1812) is not recorded. Try https://en.wikipedia.org/wiki/Kengtung_State

Spot checks:
- `/ledger/6` https://en.wikipedia.org/wiki/Rattanakosin_Kingdom_(1782%E2%80%931932): confirmed: 'sent armies to sack Pattani in 1786, bringing Pattani into Siamese rule'
- `/ledger/10` https://en.wikipedia.org/wiki/Rattanakosin_Kingdom_(1782%E2%80%931932): confirmed: 1794, north-western Cambodia with Battambang and Siem Reap under direct Siamese rule
- `/ledger/9` https://en.wikipedia.org/wiki/Rattanakosin_Kingdom_(1782%E2%80%931932): confirmed for 1793; page also gives the 1792 occupation the ledger omits
- `/ledger/26` https://en.wikipedia.org/wiki/Franco-Siamese_War: mis-dated (conf 2): month 6 against April / 25 May on the page; fixed by reviewer
- `/ledger/27` https://en.wikipedia.org/wiki/Franco-Siamese_War: confirmed: treaty of 3 October 1893, east bank ceded
- `/ledger/32` https://en.wikipedia.org/wiki/Kingdom_of_Chiang_Mai: confirmed: Monthon Phayap December 1899, ending tributary relations
- `/ledger/38` https://en.wikipedia.org/wiki/Anglo-Siamese_Treaty_of_1909: confirmed: signed 10 March 1909, ratifications 9 July 1909 (infobox effective date); Kelantan, Tringganu, Kedah, Perlis named

## nguyen-dynasty: thin

Area: infobox None km2 (None) against Cliopatria 300553 km2, ratio None, acknowledged True. The Nguyen dynasty infobox has no area figure (confirmed); the author says so.

Findings:
- `/ledger/12` (applied by reviewer): The gain of the Cham remnant was dated 1834 at confidence 1 with no page, two years after the champa dossier's 1832 dissolve into nguyen-dynasty. Evidence: Champa page infobox: 'Panduranga annexed by Vietnam under Nguyen dynasty: November 1832'; text: Panduranga 'survived until August 1832' and was incorporated into Ninh Thuan and Binh Thuan. Fix: Re-dated to 1832-11, confidence 2, source the Champa page (added to sources[]), keyframe 8 note and notes updated; done by the reviewer (event moved from /ledger/15 to /ledger/12; later pointers in this report use the new order), re-validated (0 errors).
- `/keyframe_review/12` (for the author/orchestrator): Keyframe 1880 is 'ok' to 1884 while /ledger/31 removes Tonkin (about half the shape) in 1883: a large event with no trace in the keyframes. Evidence: Nguyen page: 'The Hue court was forced to sign the Harmand Convention in September 1883' (25 September); the note on keyframe 12 says the ledger carries both steps. Fix: Mark keyframe 12 adjust with a new keyframe 1883-1884 = minus(Nguyen 1880 shape, Tonkin), or model 1883 as a protectorate (vassal_start french-indochina over Tonkin) and keep the shape; add month 9 to /ledger/31 if the September date is kept.
- `/wars/0` (for the author/orchestrator): The war against the Tay Son has zones but the ledger has no contest_start/contest_end; tay-son-dynasty carries contest_start nguyen-dynasty 1793 and contest_end nguyen-dynasty 1802-07 with no mirror. Evidence: tay-son-dynasty ledger 25 and 33; rule 6 needs the contest events to blend the zone. Fix: Add contest_start 1793 (Thi Nai / Qui Nhon front) and contest_end 1802-07 with counterpart tay-son-dynasty.
- `/ledger/8` (for the author/orchestrator): The 1802-07 gain names only tay-son-dynasty, but part of its region is the Mekong delta that Cliopatria's 'Cambodia' row holds until 1802 and that the cambodia dossier dissolves into nguyen-dynasty in 1802 (conf 1). Evidence: cambodia dossier ledger 1; Nguyen keyframe 1 note: the 1791 shape (8,428 km2) is far smaller than the delta. Fix: Either widen the 1788-1801 keyframes to Gia Dinh (whole delta) or add a 1802 gain with counterpart cambodia for the delta cells; agree with the cambodia author.
- `/ledger/22` (for the author/orchestrator): Month 6 for the 1847 withdrawal is a reading: the page says 'mid-1847'. Evidence: Siamese-Vietnamese War (1841-1845) page: 'The Vietnamese withdrew their forces from Cambodia in mid-1847'. Fix: Say in the note that June stands for 'mid-1847' (minor).

Gaps for a gap-filler:
- `/keyframe_review/1`: Extent of Nguyen Anh's Gia Dinh 1788-1801 (shape of 8,428 km2 kept ok, unverified). Try https://en.wikipedia.org/wiki/Nguy%E1%BB%85n_lords
- `/ledger/2`: 1796 advance to Phu Yen (conf 1). Try https://en.wikipedia.org/wiki/Battle_of_Th%E1%BB%8B_N%E1%BA%A1i
- `/ledger/4`: 1800 loss of Qui Nhon (conf 1; Tay Son page says Nguyen Anh occupied the citadel in 1800). Try https://en.wikipedia.org/wiki/T%C3%A2y_S%C6%A1n_dynasty
- `/ledger/11`: End of the 1827 occupation of Savannakhet and Xam Neua (conf 1). Try https://en.wikipedia.org/wiki/Lao_rebellion_(1826%E2%80%931828)
- `/ledger/28`: contest_end of the Cochinchina campaign (conf 1). Try https://en.wikipedia.org/wiki/Cochinchina_campaign
- `/ledger/29`: End of Hue's suzerainty over Cambodia in 1863 (conf 1). Try https://en.wikipedia.org/wiki/French_protectorate_of_Cambodia

Spot checks:
- `/ledger/5` https://en.wikipedia.org/wiki/Nguyen_dynasty: confirmed: 'He seized the capital (Phu Xuan) on 3 May 1801'
- `/ledger/8` https://en.wikipedia.org/wiki/Nguyen_dynasty: confirmed: 'On 20 July 1802, Anh captured Hanoi'
- `/ledger/10` https://en.wikipedia.org/wiki/Nguyen_dynasty: confirmed: 'seized Xam Neua and Savannakhet in 1827'
- `/ledger/18` https://en.wikipedia.org/wiki/Siamese%E2%80%93Vietnamese_War_(1833%E2%80%931834): confirmed: Tran Tay province established November 1835
- `/ledger/22` https://en.wikipedia.org/wiki/Siamese%E2%80%93Vietnamese_War_(1841%E2%80%931845): confirmed for the year; month 6 reads 'mid-1847'
- `/ledger/26` https://en.wikipedia.org/wiki/Nguyen_dynasty: confirmed: June 1862 Treaty of Saigon, Gia Dinh, My Tho, Bien Hoa
- `/ledger/33` https://en.wikipedia.org/wiki/Nguyen_dynasty: confirmed: Treaty of Patenotre signed 6 June 1884
- `/ledger/12` https://en.wikipedia.org/wiki/Champa: re-dated: page gives November 1832, ledger had 1834 at conf 1; fixed by reviewer

## burma: thin

Area: infobox 794000 km2 (1824) against Cliopatria 797916 km2, ratio 1.0, acknowledged True. 

Findings:
- `/identity` (for the author/orchestrator): The dossier is the same state and dynasty as konbaung-dynasty (1752-1819, another se-01 part): Konbaung kings, Amarapura capital, no break in 1819-1820, so the map would give it a new colour and a found caption in 1820 (rule 2). Evidence: Konbaung dynasty page infobox: capitals Ava 1765-1783 and 1821-1842, Amarapura 1783-1821 and 1842-1857, Mandalay 1857-1885; monarchs Bodawpaya 1782-1819 to Thibaw 1878-1885. The author flagged it in the notes. Fix: Orchestrator: merge burma into konbaung-dynasty (earlier slug, cliopatria_names Konbaung Dynasty and Burma, end 1885-11) or replace the 1820 found with continuity so one colour runs 1752-1885.

Gaps for a gap-filler:
- `/ledger/11`: occupation_end of Rangoon dated 1826-02 at conf 1, but the page says Rangoon was among the areas 'occupied for several years' until the indemnity was paid. Try https://en.wikipedia.org/wiki/Treaty_of_Yandabo
- `/ledger/23`: Kachin vassal_end undated (conf 1). Try https://en.wikipedia.org/wiki/Kachin_Hills
- `/identity/rulers`: No ruler strip; the Konbaung page gives Mindon 1853-1878 and Thibaw 1878-1885 in the infobox and Tharrawaddy 1837, Pagan 1846 in the text. Try https://en.wikipedia.org/wiki/List_of_Burmese_monarchs
- `/wars/0`: Burmese operations in Cachar and Jaintia (1823-1824) that opened the First Anglo-Burmese War are not recorded. Try https://en.wikipedia.org/wiki/First_Anglo-Burmese_War

Spot checks:
- `/ledger/5` https://en.wikipedia.org/wiki/First_Anglo-Burmese_War: confirmed: British force entered Rangoon harbour on 11 May 1824
- `/ledger/6` https://en.wikipedia.org/wiki/First_Anglo-Burmese_War: confirmed: Burmese expelled from Assam in the summer of 1825
- `/ledger/9` https://en.wikipedia.org/wiki/First_Anglo-Burmese_War: confirmed: Mrauk-U defeated 1 April 1825
- `/ledger/10` https://en.wikipedia.org/wiki/First_Anglo-Burmese_War: confirmed: Yandabo 24 February 1826, Arakan and Tenasserim ceded
- `/ledger/16` https://en.wikipedia.org/wiki/Second_Anglo-Burmese_War: confirmed: 'The proclamation of annexation was issued on 20 January 1853'
- `/ledger/21` https://en.wikipedia.org/wiki/Third_Anglo-Burmese_War: confirmed: 7-29 November 1885, Mandalay fallen 28 November
- `/identity/capitals` https://en.wikipedia.org/wiki/Konbaung_dynasty: confirmed: Amarapura to 1821, Ava 1821-1842, Amarapura 1842-1857, Mandalay 1857-1885
- `/ledger/18` https://en.wikipedia.org/wiki/Konbaung_dynasty: confirmed: 'Mindon avoided annexation in 1875 by ceding the Karenni States'

## union-of-burma: thin

Area: infobox 676579 km2 (2024) against Cliopatria 675942 km2, ratio 1.0, acknowledged True. 

Findings:
- `/identity/cliopatria_names` (for the author/orchestrator): The dossier claims the Union of Myanmar row, which the se-04 group owns (1-2 pages); two dossiers would cover 1990-2024 unless se-04 is told. Evidence: Author's report problems[0]; polities.csv union-of-myanmar shares Q836 with burma. Fix: Orchestrator: assign union-of-myanmar to this dossier and tell se-04 not to write it.

Gaps for a gap-filler:
- `/wars/0`: Kuomintang army holding remote northern Burma after 1949 (an occupation by a foreign force) is not recorded; the war has empty zones. Try https://en.wikipedia.org/wiki/Kuomintang_in_Burma
- `/wars/0`: Rebel-held land (Karen 1949, Communist Party of Burma north-east 1968-1989, the post-2021 civil war) is not recorded as rebel or contest zones (rule 5). Try https://en.wikipedia.org/wiki/Myanmar_civil_war_(2021%E2%80%93present)
- `/certainty/0`: Border treaties (China 1960, India, Thailand) are not dated in certainty notes. Try https://en.wikipedia.org/wiki/China%E2%80%93Myanmar_border

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Union_of_Burma: confirmed: established 4 January 1948
- `/ledger/1` https://en.wikipedia.org/wiki/Union_of_Burma: confirmed: coup of 2 March 1962; Union of Burma the official name 1948-1962
- `/ledger/2` https://en.wikipedia.org/wiki/Myanmar: confirmed: 1974 constitution of the Socialist Republic of the Union of Burma
- `/ledger/3` https://en.wikipedia.org/wiki/Myanmar: confirmed: official English name changed on 18 June 1989
- `/ledger/4` https://en.wikipedia.org/wiki/Myanmar: confirmed: capital moved from Yangon in November 2005

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| rattanakosin-kingdom 1782 found thonburi-kingdom | thonburi-kingdom 1782 dissolve | matched | both April 1782 |
| rattanakosin-kingdom 1782 vassal_start vientiane | vientiane   | missing | vientiane dossier has no vassal span under Siam (only the 1778-1779 contest with thonburi-kingdom) |
| rattanakosin-kingdom 1782 vassal_start kingdom-of-luang-phrabang | kingdom-of-luang-phrabang   | missing | LP dossier has no vassal span; it has Siamese occupations 1791-1792 and 1793-1794 that rattanakosin lacks |
| rattanakosin-kingdom 1782 vassal_start kingdom-of-champasak | kingdom-of-champasak   | missing | champasak dossier has no vassal span under Siam |
| rattanakosin-kingdom 1782 vassal_start chiangmai | -   | exception | chiangmai not written yet (se-01 part) |
| rattanakosin-kingdom 1786 gain Pattani | -   | exception | listed in counterparts_needing_dossiers |
| rattanakosin-kingdom 1786 vassal_start kelantan | -   | exception | kelantan owned by se-03, not run |
| rattanakosin-kingdom 1786 vassal_start Terengganu | -   | exception | listed in counterparts_needing_dossiers |
| rattanakosin-kingdom 1793 loss konbaung-dynasty | konbaung-dynasty   | mismatch | no 1792 gain/occupation in rattanakosin and no 1793 event in konbaung-dynasty; see fix /ledger/9 |
| rattanakosin-kingdom 1794 gain post-angkor-cambodia | post-angkor-cambodia 1795 loss | matched | one year apart: Rattanakosin page 1794, Post-Angkor page 1795 |
| rattanakosin-kingdom 1821 gain sultanate-of-kedah | -   | exception | sultanate-of-kedah owned by se-02, not written |
| rattanakosin-kingdom 1827 contest_start vientiane | vientiane 1826 contest_start | matched | 1827-01 vs 1826-12 |
| rattanakosin-kingdom 1828 gain vientiane | vientiane 1828 dissolve | matched | vientiane dissolves into rattanakosin-kingdom |
| rattanakosin-kingdom 1833 contest_start nguyen-dynasty | nguyen-dynasty 1833 contest_start | matched | both 1833-11; ends both 1834-04 |
| rattanakosin-kingdom 1839 vassal_start kedah-perlis-district | -   | exception | se-03 not run |
| rattanakosin-kingdom 1841 contest_start nguyen-dynasty | nguyen-dynasty 1841 contest_start | matched | ends both 1847-01 |
| rattanakosin-kingdom 1842 loss sultanate-of-kedah | -   | exception | se-02 not written |
| rattanakosin-kingdom 1848 vassal_start post-angkor-cambodia | post-angkor-cambodia   | missing | post-angkor-cambodia has only occupation_end nguyen-dynasty 1847; no joint-suzerainty vassal events |
| rattanakosin-kingdom 1867 vassal_end post-angkor-cambodia | post-angkor-cambodia 1863 dissolve | mismatch | counterpart dissolves 1863-08 (French protectorate); Siam keeps its claim to 1867-07 |
| rattanakosin-kingdom 1893 loss french-indochina | -   | exception | french-indochina owned by se-03, not run (also 1893 occupation/contest, 1904, 1907) |
| rattanakosin-kingdom 1893 vassal_end kingdom-of-luang-phrabang | kingdom-of-luang-phrabang 1893 dissolve | missing | LP dissolves 1893-10 but carries no vassal span to end |
| rattanakosin-kingdom 1893 vassal_end kingdom-of-champasak | kingdom-of-champasak 1893 dissolve | missing | champasak has no vassal span; it has a 1828 loss to rattanakosin (conf 1) unmirrored here |
| rattanakosin-kingdom 1899 gain chiangmai | -   | exception | chiangmai not written yet |
| rattanakosin-kingdom 1909 vassal_end sultanate-of-kedah | -   | exception | kedah se-02, perlis and kelantan se-03, terengganu listed |
| tay-son-dynasty 1784 contest_start rattanakosin-kingdom | rattanakosin-kingdom   | missing | Siamese invasion of 1784-1785 absent from rattanakosin; see fix /wars |
| kingdom-of-champasak 1827 contest_start rattanakosin-kingdom | rattanakosin-kingdom   | missing | rattanakosin contests the Lao rebellion with vientiane only |
| kingdom-of-champasak 1828 loss rattanakosin-kingdom | rattanakosin-kingdom   | missing | no 1828 gain from champasak in rattanakosin (conf 1 on the champasak side) |
| kingdom-of-luang-phrabang 1791 occupation_start rattanakosin-kingdom | rattanakosin-kingdom   | missing | also 1792 end, 1793 start, 1794-06 end |
| nguyen-dynasty 1788 found tay-son-dynasty | tay-son-dynasty 1788 loss | matched | both 1788-09 |
| nguyen-dynasty 1794 gain tay-son-dynasty | tay-son-dynasty 1794 loss | matched | also 1796, 1799 gain, 1800 loss/gain, 1801-05 matched |
| nguyen-dynasty 1802 gain tay-son-dynasty | tay-son-dynasty 1802 dissolve | matched | 1802-07 both sides |
| cambodia 1802 dissolve nguyen-dynasty | nguyen-dynasty 1802 gain | mismatch | nguyen 1802 gain names tay-son-dynasty for the delta cells the cambodia row hands over |
| nguyen-dynasty 1803 vassal_start post-angkor-cambodia | post-angkor-cambodia   | missing | no vassal events in post-angkor-cambodia |
| nguyen-dynasty 1827 occupation_start vientiane | vientiane   | missing | vientiane has no Vietnamese occupation; rattanakosin gains the whole Vientiane shape in 1828 (conflict flagged by the author) |
| nguyen-dynasty 1832 gain champa | champa 1832 dissolve | matched | after reviewer fix (was 1834) |
| nguyen-dynasty 1833 loss Le Van Khoi's rebels | -   | exception | listed in counterparts_needing_dossiers |
| nguyen-dynasty 1835 gain post-angkor-cambodia | post-angkor-cambodia 1834 occupation_start | mismatch | annexation (gain) here vs occupation there; nguyen also has vassal_end 1834 |
| nguyen-dynasty 1847 loss post-angkor-cambodia | post-angkor-cambodia 1847 occupation_end | mismatch | type differs; nguyen vassal_start 1847-06 has no mirror |
| nguyen-dynasty 1863 vassal_end post-angkor-cambodia | post-angkor-cambodia 1863 dissolve | matched | conf 1 here |
| nguyen-dynasty 1862 loss french-indochina | -   | exception | se-03 not run (also 1858-1859 contest/occupation, 1867, 1883, 1884) |
| tay-son-dynasty 1778 loss nguyen-dynasty | nguyen-dynasty   | mismatch | nguyen-dynasty starts 1788 and nguyen-lords ends 1777: tay-son 1778 loss, 1782 gain, 1783 contest_start, 1785 contest_end name a counterpart not alive |
| tay-son-dynasty 1793 contest_start nguyen-dynasty | nguyen-dynasty   | missing | no contest events in nguyen; see fix /wars/0 |
| burma 1820 found konbaung-dynasty | konbaung-dynasty 1819 dissolve | matched | same state; see identity fix |
| burma 1820 vassal_start Shan principalities (Saopha states) | -   | exception | listed; the shan-states dossier covers 1287-1563 only |
| burma 1824 occupation_start british-empire | -   | exception | british-empire owned by sa-06, not written (also 1825, 1826, 1852-1853) |
| burma 1875 loss Karenni States | -   | exception | listed |
| burma 1885 loss british-raj | -   | exception | british-raj owned by sa-06, not written |
| union-of-burma 1948 found british-raj | -   | exception | british-raj not written |

## Problems for the orchestrator

- burma (1820-1885) and konbaung-dynasty (1752-1819) are one state under one dynasty: two dossiers break rule 2 (new colour in 1820); orchestrator to merge under konbaung-dynasty or carry one colour.
- union-of-burma takes the Union of Myanmar row owned by se-04; se-04 must not write union-of-myanmar.
- nguyen-dynasty starts 1788 and nguyen-lords ends 1777, but tay-son-dynasty records Nguyen Anh's Gia Dinh 1778-1785 against nguyen-dynasty; the Nguyen lords infobox gives 'Dates 1558-1777 and 1780-1802'. Orchestrator to decide which dossier carries 1778-1785.
- Neighbour dossiers of other se-01 parts lack the Siamese and Vietnamese vassal spans: vientiane, kingdom-of-luang-phrabang, kingdom-of-champasak (no vassal of Siam), post-angkor-cambodia (models 1834-1847 as occupation where nguyen-dynasty has annexation, no vassal events, dissolves 1863 while Siam's claim runs to 1867).
- Author's counterparts list named 'kedah-sultanate' (it is the Cliopatria row sultanate-of-kedah, se-02) and 'panduranga' (covered by the champa dossier, which ends 1832 into nguyen-dynasty); both dropped here.
- Validator 'no verdict' warnings on burma (2) and union-of-burma (8) are the declared split of the Cliopatria row Burma, not omissions.
- Reviewer edited two dossiers in place (rattanakosin-kingdom /ledger/26 month; nguyen-dynasty Cham gain re-dated to 1832-11 with the Champa page added to sources); both re-validated with 0 errors and read back.
- All pages opened loaded; no tool failures.
