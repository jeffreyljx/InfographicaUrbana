# Review of batch se-03-c (2026-10-19)

Reviewer: adversarial review, Phase B. Machine copy: history/notes/phase-b/reviews/se-03-c.json. Ledger indices below are after the reviewer's edits.

## Verdicts

- **french-indochina**: fix
- **kingdom-of-sarawak**: thin
- **pahang-sultanate**: pass
- **kedah-perlis-district**: thin
- **riau-lingga-sultanate**: fix
- **sultanate-of-sambaliung**: fix

## french-indochina (fix)

Area: infobox 737000 km2, Cliopatria 790410 km2, ratio 1.07. Infobox 737,000 km2 with no year; largest Cliopatria shape (1908) includes Réunion, French India, Tianjin, New Caledonia; author's /keyframe_review/12 quotes the same figures.

Findings:
- `/ledger/12` (APPLIED by reviewer): The c.1890 gain from nguyen-dynasty at confidence 1 ('page silent') is the Sipsong Chau Tai, incorporated into Tonkin on 7 April 1889; year, counterpart and confidence were wrong. Evidence: Sip Song Chau Tai page: it 'became an autonomous part of the French protectorate of Tonkin, and thereby of French Indochina, in 1889'; Pavie 'signed a treaty with Đèo Văn Trị, the White Tai lord of Muang Lay' on 7 April 1889; provinces Điện Biên, Lai Châu, Sơn La, western Lào Cai and Yên Bái (about 33-38,000 km2, against Cliopatria's 1890 step of 36,201 km2). kingdom-of-luang-phrabang /ledger/6 already records the loss in 1889/4. nguyen-dynasty ends in 1884. Fix: Set year 1889, month 4, counterpart kingdom-of-luang-phrabang, confidence 2, source https://en.wikipedia.org/wiki/Sip_Song_Chau_Tai (added to sources); note and region text rewritten; /keyframe_review/7/note appended.
- `/ledger/19` (APPLIED by reviewer): The 1904 gain of the west-bank lands (69 Laos cells) was confidence 1 'page silent', but the cited page names the lands. Evidence: French protectorate of Laos: 'In 1902, a treaty with Siam forced the kingdom to also surrender lands on the western side of the Mekong River. These lands now form the province of Sainyabuli and the western half of Champasak Province' and 'In 1904 ... Siam ceded Meluprey (Preah Vihear Province) and the Kingdom of Champasak to the French.' Fix: Confidence 1 to 2; note and region text quote the page (was /ledger/18).
- `/ledger/22` (APPLIED by reviewer): The 22 November 1904 annexation of Champasak named kingdom-of-champasak as counterpart, a dossier that ends in October 1893. Evidence: French protectorate of Laos: 'Siam ceded ... the Kingdom of Champasak to the French' (1904); kingdom-of-champasak dissolves 1893/10; rattanakosin-kingdom /ledger/34 holds the February 1904 loss of 'Mluprey, Champasak and Sainyabuli'. Fix: Counterpart changed to rattanakosin-kingdom; note says why (was /ledger/20).
- `/ledger/41` (APPLIED by reviewer): The French return to Laos was dated November 1946 at confidence 1 ('page silent'); the cited page dates it April 1946. Evidence: French protectorate of Laos infobox: 'French restoration: 24 April 1946'; body: the French were 'entering the capital of Vientiane towards the end of April 1946'. Fix: Month 4, confidence 3, note rewritten; event moved after the 1946/3 event (was /ledger/40).
- `/ledger/17 and /ledger/21` (APPLIED by reviewer): The French occupation of Chanthaburi (1893-1904) was missing although the dossier's own war outcome and /ledger/15 note mention it, and rattanakosin-kingdom records it (/ledger/25, /ledger/33). Evidence: Franco-Siamese War: 'The French demanded as guarantees the temporary occupation of Chantaburi'; French Indochina: 'In 1904, to get back Chantaburi, Siam had to give Trat and Koh Kong to French Indochina'. (The Franco-Siamese War page alternatively has the occupation of Chanthaburi and Trat 'up until 1907', noted.) Fix: Added occupation_start 1893/10 and occupation_end 1904/2, counterpart rattanakosin-kingdom, region admin1 Chanthaburi, confidence 2.
- `/ledger/4, /ledger/32, /ledger/39, /ledger/47 (kingdom-of-cambodia); /ledger/16, /ledger/34, /ledger/41, /ledger/46 (kingdom-of-laos); /ledger/8, /ledger/33 (nguyen-dynasty)` (NOT applied): Vassal events name counterparts whose dossiers do not cover the years (kingdom-of-cambodia and kingdom-of-laos start in 1953, nguyen-dynasty ends in 1884), while the report lists protectorate-of-cambodia, protectorate-of-laos and empire-of-annam as needed. Evidence: kingdom-of-cambodia found 1953/11, kingdom-of-laos found 1953/10, nguyen-dynasty end 1884; validator pairs vassal events by counterpart string so a rename of each pair is safe. Fix: Non-blocking, routing: once the orchestrator settles the protectorate-monarchy slugs, rename each pair's counterpart (1863-1953 Cambodia, 1893-1953 Laos, 1883-1945 Annam/Tonkin). Not applied because the slug choice is the orchestrator's.

Thin (for a gap-filler):
- `/ledger/25-36 and /keyframe_review/21-22`: Japanese zones 1940-1945 (Cliopatria's Hanoi block is the only extent) and the 9 March 1945 takeover of the rest of Indochina, which empire-of-japan /ledger/83 records and this dossier does not mirror (only vassal_end of the protectorates). Try: https://en.wikipedia.org/wiki/Japanese_coup_d%27%C3%A9tat_in_French_Indochina
- `/ledger/37-38`: The Chinese occupation of the north to the 16th parallel (September 1945 to 1946) is not modelled. Try: https://en.wikipedia.org/wiki/Chinese_occupation_of_northern_Indochina
- `/ledger/8`: The Patenôtre treaty of 6 June 1884 (nguyen-dynasty /ledger/32 has it as the loss of Annam); the Tonkin campaign page is silent on it. Try: https://en.wikipedia.org/wiki/Treaty_of_Hu%E1%BA%BF_(1884)
- `/wars`: The Tonkin campaign / Cần Vương resistance (1883-1896) is not a war entry although the pages give pacification to 1896. Try: https://en.wikipedia.org/wiki/C%E1%BA%A7n_V%C6%B0%C6%A1ng

Spot checks:
- `/ledger/0-3` (https://en.wikipedia.org/wiki/French_Cochinchina): confirmed (17 February 1859; siege lifted 1861; ceded 5 June 1862: Biên Hòa, Gia Định, Định Tường, Poulo Condore)
- `/ledger/5` (https://en.wikipedia.org/wiki/French_Cochinchina): confirmed (1867, de la Grandière, three provinces)
- `/ledger/7-10` (https://en.wikipedia.org/wiki/Tonkin_campaign): confirmed (Treaty of Huế 25 August 1883, Bình Thuận to Cochinchina, protectorate over Annam and Tonkin; Bac Le 23 June 1884; Tientsin 9 June 1885)
- `/ledger/11, /ledger/18, /ledger/20, /ledger/23, /ledger/31, /ledger/50` (https://en.wikipedia.org/wiki/French_Indochina): confirmed (17 October 1887; Guangzhouwan added 5 January 1900, returned 1945; Trat and Koh Kong 1904; Trat back 23 March 1907; 21 July 1954)
- `/ledger/4, /ledger/24, /ledger/27, /ledger/32, /ledger/39, /ledger/47` (https://en.wikipedia.org/wiki/French_protectorate_of_Cambodia): confirmed (11 August 1863; 23 March 1907 Battambang and Siem Reap; 1941 cession list; 9 March 1945; 16 October 1945; 9 November 1953)
- `/ledger/12 (was 1890)` (https://en.wikipedia.org/wiki/Sip_Song_Chau_Tai): mis-dated (confidence 1): the step is 7 April 1889; fixed
- `/ledger/16, /ledger/22, /ledger/28, /ledger/42, /ledger/46` (https://en.wikipedia.org/wiki/French_protectorate_of_Laos): confirmed (3 October 1893; Champasak annexed 22 November 1904; 1941 cession of Champassak and Xaignabouli; return in November; independence 22 October 1953)
- `/ledger/41 (was /ledger/40, November 1946)` (https://en.wikipedia.org/wiki/French_protectorate_of_Laos): mis-dated (confidence 1): 'French restoration: 24 April 1946'; fixed
- `/ledger/13-15` (https://en.wikipedia.org/wiki/Franco-Siamese_War): confirmed (columns April 1893, Khammuan by 25 May, treaty 3 October 1893, east bank ceded)

## kingdom-of-sarawak (thin)

Area: infobox None km2, Cliopatria 128406 km2, ratio None. Neither the Raj of Sarawak nor the History of Sarawak page gives an area (checked); author compared the 1946 shape with modern Sarawak in the gazetteer.

Thin (for a gap-filler):
- `/ledger/5`: The 1870 inland strip (95 cells, 111.1-114.7E, 1.4-4.3N, about 29,500 km2) is dated and assigned only from Cliopatria (confidence 1). It may be the Mukah-Oya coast ceded with Bintulu in 1861 or the Baram hinterland of 1882. Try: https://en.wikipedia.org/wiki/Mukah
- `/ledger/11 and /keyframe_review/7`: The interior (177 cells, about 43,000 km2, a third of Sarawak) is put in 1905 from 'nobody' at confidence 1. Much of it is probably the Baram basin, which the 1882 cession ('extended to 3 miles beyond the Baram River') covers but /ledger/6 draws as a 20 km circle at the mouth. Try: https://en.wikipedia.org/wiki/Baram_River
- `/ledger/10`: The cedant of Lawas in 1905 (british-north-borneo-company is an inference; the History of Sarawak page does not name it). Try: https://en.wikipedia.org/wiki/Lawas

Spot checks:
- `/ledger/0-1` (https://en.wikipedia.org/wiki/History_of_Sarawak): confirmed (24 September 1841 grant; 'Tanjung Datu, to the Samarahan river')
- `/ledger/2-3` (https://en.wikipedia.org/wiki/Raj_of_Sarawak): confirmed (1852 Saribas and Skrang; 1861 Rajang River basin)
- `/ledger/4, /ledger/6` (https://en.wikipedia.org/wiki/History_of_Sarawak): confirmed (1861 Bintulu; 1882 'extended to 3 miles beyond the Baram River (near Miri)')
- `/ledger/8` (https://en.wikipedia.org/wiki/Raj_of_Sarawak): confirmed ('Protected state: 14 June 1888')
- `/ledger/10` (https://en.wikipedia.org/wiki/History_of_Sarawak): confirmed for year and place ('The final expansion of Sarawak occurred in 1905 when Lawas was ceded'); the cedant is not on the page, as the note says (confidence 2)
- `/ledger/12-13, /ledger/15` (https://en.wikipedia.org/wiki/History_of_Sarawak): confirmed (Miri 16 December 1941, Kuching 24 December; surrender 10 September 1945; Crown colony 1 July 1946)

## pahang-sultanate (pass)

Area: infobox 36006 km2, Cliopatria 40730 km2, ratio 1.13. Infobox is modern Pahang; within a factor of two. Infobox year not given (modern state figure).

Tried: the 1853 and 1881 dates, the 1888 end, the area, the Johor overlap. The Johor dossier dates the separation 1861 from its own page; both pages say what they are cited for and both authors flagged it (cross_checks).

Spot checks:
- `/ledger/0-1` (https://en.wikipedia.org/wiki/Pahang): confirmed (1853, Tun Ali 'renounced his allegiance to the Sultan of Johor and became the independent ruler of Pahang')
- `/ledger/2` (https://en.wikipedia.org/wiki/Pahang): confirmed ('proclaimed Sultan of Pahang by his chiefs in 1881'; infobox 1882)
- `/ledger/3` (https://en.wikipedia.org/wiki/Pahang): confirmed ('In October 1888, Sultan Ahmad reluctantly accepted John Pickersgill Rodger as Pahang's first resident'; Clifford December 1887)
- `/wars/0` (https://en.wikipedia.org/wiki/Pahang): confirmed (civil war after 1857, ended 1863; Wan Ahmad backed by Terengganu and the Siamese; no land named)

## kedah-perlis-district (thin)

Area: infobox 819 km2, Cliopatria 2094 km2, ratio 2.56. Acknowledged in /keyframe_review/0 but unresolved; neither opened page mentions Langkawi except as a ferry destination. Thin by design within the 2-page budget. Infobox year not given (modern state figure).

Thin (for a gap-filler):
- `/keyframe_review/0 and /keyframe_review/1`: Area 2,094 km2 against the infobox's 819 km2 (ratio 2.56), acknowledged but not resolved: 3 of the 5 cells (Langkawi side and one cell east, possibly Kubang Pasu) have no owner on any opened page; sultanate-of-kedah /keyframe_review (1842) leaves them to this row. Langkawi was Kedah's; if a page confirms it, this shape should be corrected to admin1 Perlis and the Kedah dossier should take the cells. Try: https://en.wikipedia.org/wiki/Langkawi
- `/ledger/0-2`: The Perlis page gives both 1839 (separation, Raja Long Krok, rattanakosin-kingdom /ledger/18) and 1842 (principality, direct vassal of Bangkok); one year must be settled with rattanakosin-kingdom. Try: https://en.wikipedia.org/wiki/Kubang_Pasu

Spot checks:
- `/ledger/0-1` (https://en.wikipedia.org/wiki/Perlis): confirmed (after the 1842 restoration, 'Siam separated Perlis into a separate principality which was a direct vassal of Bangkok'; the page also has 'Perlis was separated' in 1839)
- `/ledger/2` (https://en.wikipedia.org/wiki/Perlis): confirmed at confidence 2 (infobox 'Vassal state of Siam governed by Raja Long Krok: 1839')
- `/ledger/3` (https://en.wikipedia.org/wiki/Perlis): confirmed (infobox 20 April 1843, text 20 May 1843)
- `/ledger/4-5` (https://en.wikipedia.org/wiki/Anglo-Siamese_Treaty_of_1909): confirmed (signed 10 March, effective 9 July 1909; Article 1 names Perlis)

## riau-lingga-sultanate (fix)

Area: infobox None km2, Cliopatria 103825 km2, ratio None. No infobox area (checked). The correction drops the Riau mainland the page does not list; resolved.

Findings:
- `/ledger/2 and /ledger/5` (APPLIED by reviewer): The Dutch protectorate was missing: the dossier recorded no vassal relation for a sultanate whose infobox status is 'Dutch protectorate', while its notes ask the Indies to draw it as a vassal. Evidence: Riau-Lingga Sultanate: infobox 'Status: Dutch protectorate'; the 1818 agreement made 'the Dutch ... the paramount leaders of the Johor-Riau Sultanate'; the sultan deposed in 1857 is called the Dutch 'vassal'; 'Abolished by the Dutch: 11 February 1911'. Fix: Added vassal_start 1824/6 (confidence 2) and vassal_end 1911/2 (confidence 3), counterpart dutch-east-indies, region as /ledger/1, vassal's side as in the batch's other dossiers.
- `/ledger/3` (NOT applied): The 1857 deposition of Mahmud IV is typed 'rename', but neither the name nor the dynasty changes; it is a ruler change already in /identity/rulers. Evidence: Schema: rename is a name change or a dynasty change within the same state; the page: 'The Dutch therefore deposed him on 7 October 1857'. Fix: Non-blocking: drop the event (the rulers strip carries it) or keep it with a note that it marks Cliopatria's row end. Not applied.

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Riau-Lingga_Sultanate): confirmed (infobox 'Anglo-Dutch Treaty of 1824: 2 June 1824')
- `/ledger/1` (https://en.wikipedia.org/wiki/Riau-Lingga_Sultanate): confirmed (Riau, Lingga and Tudjuh archipelagos; Igal, Gaung, Reteh and Mandah in Indragiri; Kateman enclave)
- `/ledger/3` (https://en.wikipedia.org/wiki/Riau-Lingga_Sultanate): confirmed (7 October 1857)
- `/ledger/4` (https://en.wikipedia.org/wiki/Riau-Lingga_Sultanate): confirmed by the infobox only (Daik royal 1824-1900, Tanjungpinang royal 1900-1911); no body sentence on a move
- `/ledger/6` (https://en.wikipedia.org/wiki/Riau-Lingga_Sultanate): confirmed (11 February 1911; direct rule 1913)

## sultanate-of-sambaliung (fix)

Area: infobox None km2, Cliopatria 13415 km2, ratio None. The id.wikipedia page gives no area (checked).

Findings:
- `/ledger/3` (APPLIED by reviewer): vassal_end dated 1960 with counterpart dutch-east-indies, whose dossier and sovereignty end in December 1949. Evidence: Dutch East Indies: 'Dutch–Indonesian Round Table Conference: 27 December 1949'; 'In December 1949 the Netherlands formally recognised Indonesian sovereignty'. dutch-east-indies identity end 1949/12. Fix: Year 1949, month 12, source https://en.wikipedia.org/wiki/Dutch_East_Indies (added to sources), confidence 2.
- `/ledger/4 and /ledger/5` (APPLIED by reviewer): With the Dutch tie ending in 1949 the sultanate would show as sovereign 1950-1960; the page has it as a swapraja to 1960. Evidence: id.wikipedia Kesultanan Sambaliung: 'hingga penghapusan swapraja pada tahun 1960'; republic-of-indonesia gains the Indies land 1949/12; pontianak-kadriyah-sultanate in the same group ends its Dutch tie 1949/12. Fix: Added vassal_start 1949/12 (confidence 2) and vassal_end 1960 (confidence 3), counterpart republic-of-indonesia, region as the other vassal events.
- `/ledger/2/note` (APPLIED by reviewer): The note quoted the Bulungan page as if the Sultan of Berau signed the agreement of 27 September 1834 and claimed a mirror in the Dutch East Indies dossier that does not exist. Evidence: Sultanate of Bulungan: the signatory is Bulungan's sultan ('Bulungan signed a treaty with the Dutch'); dutch-east-indies has only a 1849 gain at confidence 1 (/ledger/49). Fix: Note corrected; year and confidence 2 unchanged (the page does date the Dutch conquest of Berau to 1834).

Thin (for a gap-filler):
- `/ledger (1942-1945)`: No Japanese occupation 1942-1945 (pontianak-kadriyah-sultanate has one); the Sambaliung page is silent. Try: https://en.wikipedia.org/wiki/Japanese_occupation_of_the_Dutch_East_Indies
- `/keyframe_review/0-3`: Extent and the boundary with Gunung Tabur are on no opened page; the English Berau and Sambaliung articles failed to load for the author. Try: https://id.wikipedia.org/wiki/Kesultanan_Gunung_Tabur

Spot checks:
- `/ledger/0-1` (https://id.wikipedia.org/wiki/Kesultanan_Sambaliung): confirmed ('Berau dipecah menjadi dua ... sekitar tahun 1810-an'; capital at Tanjung 1810)
- `/ledger/2` (https://en.wikipedia.org/wiki/Sultanate_of_Bulungan): confirmed for the year ('After the Dutch conquered Berau in 1834'); the signatory in the quoted sentence is Bulungan's sultan (note fixed)
- `/ledger/3 (was 1960)` (https://en.wikipedia.org/wiki/Dutch_East_Indies): mis-dated (confidence 2): the Dutch tie cannot outlast 27 December 1949; fixed
- `/ledger/6` (https://id.wikipedia.org/wiki/Kesultanan_Sambaliung): confirmed (swapraja abolished 1960; sultan list 1810-1960)

## Cross-dossier mismatches and missing mirrors

- mismatch: french-indochina /ledger/7 1883 gain / nguyen-dynasty: nguyen-dynasty /ledger/31 (1883) is the loss of Tonkin, not of Bình Thuận; the Nguyễn ledger has no Bình Thuận cession (Tonkin campaign page: 'the cession of the southern province of Bình Thuận, which was annexed to Cochinchina'). Nguyễn side to add it.
- mismatch: french-indochina /ledger/8 1883 vassal_start / nguyen-dynasty: nguyen-dynasty ends 1884 and records Tonkin (1883, /ledger/31) and Annam (1884/6, /ledger/32) as LOSSES to french-indochina; french-indochina records a protectorate (vassal) from 25 August 1883 to 9 March 1945 with counterpart nguyen-dynasty, which is dead after 1884. The author lists empire-of-annam as needed for 1884-1945. Decide one model: nguyen-dynasty /ledger/31-32 should become vassal events (or end), and the FI counterpart should be empire-of-annam.
- mismatch: french-indochina /ledger/20 1904 gain / rattanakosin-kingdom: Trat and Koh Kong: rattanakosin-kingdom records Trat (with Dan Sai) as an occupation_start 1904/2 (/ledger/35), french-indochina as a gain (French Indochina page: 'Siam had to give Trat and Koh Kong to French Indochina'). Same year; type differs; Koh Kong absent from the Siamese side.
- mismatch: french-indochina /ledger/23 1907 loss / rattanakosin-kingdom: Trat 1907/3: rattanakosin-kingdom records occupation_end (/ledger/37), french-indochina a loss. Same date; type follows the 1904 disagreement.
- mismatch: french-indochina /ledger/30 1941 occupation_start / empire-of-japan: Japanese entry into southern Indochina 1941/7: empire-of-japan has no 1941 event; it records the occupation of the rest of Indochina from the coup of 1945/3 (/ledger/83). Japan side to add July 1941 (or FI to move to 1945/3).
- mismatch: french-indochina /ledger/36 1945 occupation_end / empire-of-japan: empire-of-japan /ledger/101 ends the 1945/3 occupation of the rest of Indochina; FI ends its own 1941/7 southern occupation. End dates agree (Aug/Sep 1945); starts differ, see /ledger/30.
- missing: french-indochina /ledger/40 1946 vassal_start / democratic-republic-of-vietnam: democratic-republic-of-vietnam has no vassal_start for the Ho-Sainteny arrangement of March 1946 (First Indochina War page).
- missing: french-indochina /ledger/43 1946 vassal_end / democratic-republic-of-vietnam: democratic-republic-of-vietnam has no vassal_end for December 1946.
- missing: kingdom-of-sarawak /ledger/6 1882 gain / sultanate-of-brunei: sultanate-of-brunei has no 1882 loss for Baram ('In 1882 Sarawak's territory was extended to 3 miles beyond the Baram River', History of Sarawak); its nearest loss to Sarawak is Trusan 1885 (/ledger/22).
- mismatch: kingdom-of-sarawak /ledger/12 1941 occupation_start / empire-of-japan: empire-of-japan records the occupation of 'Malaya, Singapore and British Borneo' as 1942/2 with counterpart british-colonial-empire (/ledger/61, region Malaysia+Singapore); Sarawak records 1941/12 (landing at Miri 16 December 1941). Japan side should name kingdom-of-sarawak and December 1941.
- mismatch: kingdom-of-sarawak /ledger/13 1945 occupation_end / empire-of-japan: empire-of-japan /ledger/106 ends the occupation 1945/9 with counterpart british-colonial-empire, not kingdom-of-sarawak.
- mismatch: pahang-sultanate /ledger/1 1853 gain / sultanate-of-johor: sultanate-of-johor /ledger/24 records the loss of Pahang in 1861 (treaty recognising separate states, Johor page); Pahang's page has Tun Ali renounce allegiance in 1853. Both pages say what they are cited for; both authors flagged it. Suggest Johor add a 1853 de facto loss (or a contest 1853-1861).
- missing: kedah-perlis-district /ledger/1 1842 gain / rattanakosin-kingdom: rattanakosin-kingdom has no 1842 loss of Perlis; it has Perlis as a vassal from 1839 (/ledger/18). Perlis page: 1839 separation and Raja Long Krok, and in 1842 'Siam separated Perlis into a separate principality which was a direct vassal of Bangkok'.
- mismatch: kedah-perlis-district /ledger/2 1842 vassal_start / rattanakosin-kingdom: rattanakosin-kingdom /ledger/18 starts the Perlis vassalage in 1839 (Perlis infobox 'Vassal state of Siam governed by Raja Long Krok: 1839'); Perlis dossier 1842 (its life starts with the 1842 principality). 3 years apart, both on the Perlis page; Perlis note flags it.
- mismatch: riau-lingga-sultanate /ledger/2 1824 vassal_start / dutch-east-indies: dutch-east-indies records no protectorate; it takes the land as a gain on 7 October 1857 (/ledger/53). Riau-Lingga page: 'Status: Dutch protectorate', abolished 11 February 1911. DEI should hold vassal_start 1824/6 - vassal_end 1911/2 and its gain in 1911/2.
- mismatch: riau-lingga-sultanate /ledger/5 1911 vassal_end / dutch-east-indies: as /ledger/2: DEI gain is 1857/10 (/ledger/53), the page has the abolition on 11 February 1911.
- mismatch: sultanate-of-sambaliung /ledger/2 1834 vassal_start / dutch-east-indies: dutch-east-indies has no vassal_start for Sambaliung; it has a gain in 1849 at confidence 1 (/ledger/49, Cliopatria's year, pages silent). Sambaliung (Bulungan page: Dutch conquest of Berau 1834) keeps a protectorate to 1949. DEI should add vassal_start 1834 and drop or explain the 1849 gain.
- mismatch: sultanate-of-sambaliung /ledger/3 1949 vassal_end / dutch-east-indies: as /ledger/2: DEI ends 1949/12 with no vassal_end for Sambaliung.
- missing: sultanate-of-sambaliung /ledger/4 1949 vassal_start / republic-of-indonesia: reviewer-added vassal event (swapraja 1949-1960); republic-of-indonesia has no mirror. Route to the republic-of-indonesia owner.
- missing: sultanate-of-sambaliung /ledger/5 1960 vassal_end / republic-of-indonesia: as /ledger/4.
- missing: nguyen-dynasty /ledger/32 1884 loss / french-indochina: Annam 1884/6 (Patenôtre): no french-indochina event in 1884; FI holds Annam as a protectorate from 1883/8 (/ledger/8). See the FI /ledger/8 row.
- mismatch: nguyen-dynasty /ledger/24 1858 contest_start / french-indochina: Đà Nẵng 1858/9 falls before french-indochina's life (found 1859/2); the counterpart should be France (second-french-empire) or the event left unpaired.
- missing: empire-of-japan /ledger/83 1945 occupation_start / french-indochina: The 9 March 1945 coup: french-indochina records vassal_end of the protectorates (/ledger/32-34) but no Japanese occupation of the rest of its land in 1945/3.
- mismatch: rattanakosin-kingdom /ledger/35 1904 occupation_start / french-indochina: Trat and Dan Sai: occupation on the Siamese side, gain of Trat and Koh Kong on the French side (/ledger/20); Dan Sai absent from french-indochina.
- mismatch: sultanate-of-brunei /ledger/16 1868 loss / kingdom-of-sarawak: Brunei confidence-1 1868 loss (Cliopatria's year) against Sarawak's 1861 Rajang gain (Raj of Sarawak page) covering the same Cliopatria step; Brunei should fold it into 1861.

Exceptions: counterparts without dossiers (sultanate-of-berau, british-north-borneo-company, state-of-vietnam; the protectorate monarchies protectorate-of-cambodia, protectorate-of-laos, empire-of-annam) and owners not run yet (qing-dynasty, republic-of-china: ea-08; british-colonial-empire: eu-11).

## Problems

- Validator: 0 errors in all six dossiers before and after the reviewer's edits; warnings only for counterparts without dossiers (state-of-vietnam, british-north-borneo-company, sultanate-of-berau). --resolve: no unresolved region names.
- Reviewer edits applied in place (re-validated, read back): french-indochina (/ledger/12, 17, 19, 21, 22, 41; /keyframe_review/7/note; one source added), riau-lingga-sultanate (/ledger/2, 5 added), sultanate-of-sambaliung (/ledger/2 note, 3; /ledger/4-5 added; one source added). Ledger indices in this report are after the edits.
- Neighbour dossiers to change (other groups): dutch-east-indies (Riau-Lingga 1857 gain should be a 1824-1911 protectorate; Sambaliung 1849 gain should be a 1834-1949 protectorate), nguyen-dynasty (Bình Thuận 1883 missing; Tonkin/Annam as losses vs FI's protectorate; 1858 contest before FI exists), empire-of-japan (Sarawak occupied 1941/12 under british-colonial-empire 1942/2; no July 1941 southern Indochina), sultanate-of-brunei (no 1882 Baram loss; 1868 c1 loss vs Sarawak 1861), rattanakosin-kingdom (no 1842 loss of Perlis; Trat as occupation vs FI gain), sultanate-of-johor (Pahang 1861 vs 1853; its 1612-1623 Pahang events name pahang-sultanate where old-pahang-sultanate is meant), democratic-republic-of-vietnam (no 1946 vassal pair), republic-of-indonesia (no mirror for the Sambaliung swapraja 1949-1960).
- Owners not run yet: qing-dynasty and republic-of-china (ea-08), british-colonial-empire (eu-11).
- No pages failed for the reviewer.
