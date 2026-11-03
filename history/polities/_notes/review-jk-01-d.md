# Review of batch jk-01-d (reviewer, 2026-10-18)

Dossier: history/polities/empire-of-japan.json (Empire of Japan 1868-1945 and Japan 1953-2024, merged). Verdict: **fail**, sent back for two blocking findings. The reviewer applied five small fixes in place; the dossier re-validates with 0 errors and the same 11 counterpart warnings.

## Summary
Validates (0 errors, 11 counterpart warnings). 19 events checked on 6 pages: 17 confirmed (3 of them confidence-3 events whose region is wider than the page, lowered to 2), 2 mis-dated at confidence 1-2 (both fixed by the reviewer). No fabricated event was found. Failed for two unapplied blocking findings: the Tsingtao/Kiautschou cells in the 1915-1932 shapes have no event, and the 1915 note denies what the shape and the page show (and the 1929 outline carries the cells into every correction to 1945); and the Ryukyu Domain vassalage (1872-1879) has no mirror for ryukyu-kingdom's ledger. The merge of 'Empire of Japan' and 'Japan' into one dossier is argued from the page and accepted.

## Area check
Infobox 1938: 1,984,000 km2 against the 1938 shape's 3,103,984 (ratio 1.56). Infobox 1942: 7,400,000 against the 1942 shape's 4,172,339 (0.56) and the 1943 shape's 7,043,849 (0.95). Japan page: 377,975 against japan_1973's 413,216 (1.09). The keyframe notes acknowledge all three, and the author's quoted figures match the pages.

## Findings (blocking first)
### /keyframe_review/10/note, /keyframe_review/11-18, /keyframe_review/19-27/correction, /ledger (missing), /wars/3/zones [BLOCKING]
- What: The 1915 shape adds 4 cells at Tsingtao (120.35-120.56 E, 36.13-36.25 N; the Kiautschou leased territory) beside the 3 Micronesian cells, and the ledger has no event for them. The 1915 note says 'Nothing in the shape corresponds to the surrender ... (the page does not say where)', which is untrue for both the shape and the page. The cells stay in every shape to 1929 (and 8 cells from 1938), so the 1924-1931 keyframes and the 1929 outline used as the correction for 1932-1945 keep Tsingtao as direct Japanese land after its return to China in 1922.
- Why: Gazetteer: minus(Empire of Japan 1915, Empire of Japan 1911) = 7 cells, 4 of them at Qingdao. A Qingdao probe gives 4 cells in the 1915, 1917, 1920, 1922, 1924, 1926-1929 and 1932 shapes. Empire of Japan page (the author's own source): 'Japanese and allied British Empire forces soon moved to occupy Tsingtao fortress, the German East Asia Squadron base, German-leased territories in China's Shandong Province as well as the Marianas, Caroline, and Marshall Islands in the Pacific'; 'The German colonial troops surrendered on November 7, 1914, and Japan gained the German holdings.'
- Fix: Add occupation_start german-empire 1914-11 at Tsingtao/Kiautschou ({'place':'Qingdao','km':30}, confidence 3, Empire page) and the end in 1922 with the return to republic-of-china (open the Kiautschou Bay Leased Territory or Shandong Problem page for the year and month). Mark keyframes 1924-1931 adjust with a correction minus Qingdao, and use minus Qingdao in the 1932-1945 corrections; the 1938 reoccupation is part of the China occupation events. Add Tsingtao to the zones of /wars/3 and correct the 1915 note.

### /ledger (missing, between /ledger/7 and /ledger/8) [BLOCKING]
- What: No mirror for ryukyu-kingdom's vassal_start 1872-10 and vassal_end 1879-3, both with counterpart empire-of-japan (the Ryukyu Domain, 1872-1879).
- Why: ryukyu-kingdom /ledger/17 vassal_start 1872-10 empire-of-japan (c3: infobox 'Domain of the Empire of Japan (1872–1879)', 'Reorganized into Ryukyu Domain: 16 October 1872') and /ledger/18 vassal_end 1879-3. This dossier's 1870 keyframe correction removes Okinawa and leaves the 1872-1879 domain to the ryukyu dossier, so the vassal relation is drawn from neither side.
- Fix: Add vassal_start ryukyu-kingdom 1872-10 and vassal_end ryukyu-kingdom 1879-3, with the region of /ledger/8 (minus Okinawa minus the Amami circle) and the ryukyu-kingdom page as source; give /ledger/8 month 3 to match ryukyu-kingdom /ledger/19.

### /ledger/73 [fix]
- What: Guam and Wake end together at 1945-9 (confidence 2), but the US retook Guam in 1944: the dossier's own 1944 keyframe note says 'Guam goes', and the Pacific War page puts the 'invasions of the Mariana and Palau Islands' between June 1944 and June 1945.
- Why: Pacific War page: 'invasions of the Mariana and Palau Islands, Iwo Jima, and Okinawa between June 1944 and June 1945'; /keyframe_review/26 note: 'Guam goes'.
- Fix: Split the event: occupation_end united-states-of-america for Guam in 1944-8 (Battle of Guam (1944) page), and Wake alone in 1945-9.

### /ledger/21 [fix]
- What: The 1920 occupation of northern Sakhalin names the Soviet Union as counterpart, but that state exists only from December 1922 (Cliopatria row 1922..1991).
- Why: The note itself says 'The owner was the Russian Soviet state, then the Soviet Union'; union-of-soviet-socialist-republics starts 1922 in polities.csv.
- Fix: Use far-eastern-republic (already in counterparts_needing_dossiers) or russian-republic, as in /ledger/18, for the 1920 start. Keep the 1925 end against the Soviet Union and say in the note that the owner changed.

### /ledger/18, /ledger/22 [fix]
- What: The Primorye occupation runs 1918-8 to 1922-10 against russian-republic, whose Cliopatria row is 1917..1919, so the end falls three years after the counterpart's life.
- Why: polities.csv russian-republic 1917..1919; the brief's Context list has provisional-priamurye-government (1922..1923) and the author lists far-eastern-republic (1920-1922).
- Fix: Either end the occupation against the state that held Vladivostok in 1922 (provisional-priamurye-government or far-eastern-republic, as the Siberian intervention page reads), or say in the note that russian-republic stands for every Russian owner and route the mirror to eu-17.

### /ledger/30, /ledger/32, /ledger/33, /ledger/34 [fix]
- What: The China occupations are drawn as whole provinces (all of Hebei in July 1937, all of Zhejiang in December 1937, all of Shanxi in March 1938, all of Henan in June 1938), although the pages date only the cities. Western Henan fell only in the 1944 Ichi-Go offensive, which /ledger/47 does not cover.
- Why: Second Sino-Japanese War page: 'On 6 June, they captured Kaifeng, the capital of Henan'; 'In 1944, Japan launched Operation Ichi-Go, the invasion of Henan and Changsha'.
- Fix: Intersect each province with the Cliopatria shape of the year after (for example intersect(admin1 Henan, Empire of Japan 1939)), and add the rest of Henan to the 1944 Ichi-Go event with the Ichi-Go page.

### /keyframe_review/6, /keyframe_review/7, /keyframe_review/8-18 [fix]
- What: The Tianjin cells (1 in 1898, 8 from 1900, 7 in 1929; about 2,000 km2) are kept as Japanese territory, and through the 1929 outline they sit in every correction to 1945. The dossier's own notes say 'concessions are not territory under rule 4 and are not recorded'.
- Why: A probe over 116.5-118 E and 38.5-40 N gives 1 cell in 1898, 8 in 1900-1926 and 7 in 1929. The real Japanese concession at Tianjin covered about 1 km2.
- Fix: Mark the 1898-1931 keyframes adjust with a correction minus the Tianjin cells (polygon 116.5-118 E, 38.5-40 N), and do the same in the 1932-1945 corrections, or explain in the note why they stay.

### /ledger/2, /ledger/4, /ledger/5 [fix]
- What: The Boshin War opponent is republic-of-ezo from January 1868 for all of northern Honshu and Hokkaido, and the whole remainder is gained in May 1869. By the reviewer's reading (to be confirmed on the Boshin War page), the Republic of Ezo was proclaimed only in the winter of 1868-1869 and held Hokkaido alone; northern Honshu was the Northern Alliance's and fell in 1868.
- Why: The Empire page (as quoted) dates only the end at Hakodate, May 1869; the war page was not opened (page budget). Confidence 1 and 2.
- Fix: Open the Boshin War page. Split the contest and gain into northern Honshu (1868, against the Ouetsu Reppan Domei or the shogunate's loyalists) and Hokkaido (republic-of-ezo, from its proclamation to 1869-5).

### /identity/rulers/1, /identity/rulers/2 [APPLIED by reviewer]
- What: Taisho and Showa had no source.
- Why: Empire of Japan infobox: '1868–1912: Meiji • 1912–1926: Taishō • 1926–1947: Shōwa'.
- Fix: source set to https://en.wikipedia.org/wiki/Empire_of_Japan

### /identity/rulers/3, /identity/rulers/4 [APPLIED by reviewer]
- What: Akihito and Naruhito had no source.
- Why: Japan page: 'On May 1, 2019, after the historic abdication of Emperor Akihito, his son Naruhito became Emperor, beginning the Reiwa era.'
- Fix: source set to https://en.wikipedia.org/wiki/Japan

### /ledger/17, /wars/3/outcome [APPLIED by reviewer]
- What: The occupation of German Micronesia was dated 1915 (Cliopatria's year), confidence 1, with 'page silent on the landings'; the page names the islands and dates the war to 1914.
- Why: Empire page: 'soon moved to occupy Tsingtao fortress, ... as well as the Marianas, Caroline, and Marshall Islands in the Pacific'; 'The German colonial troops surrendered on November 7, 1914, and Japan gained the German holdings.'
- Fix: year 1914, confidence 2, reviewer note appended; war outcome 'held from 1914'.

### /ledger/30, /ledger/34, /ledger/35 [APPLIED by reviewer]
- What: Confidence 3 for regions the page does not name: the whole of Hebei (the page names Beiping and Tianjin), the whole of Henan (Kaifeng only) and Anhui (only in a flood context).
- Why: Second Sino-Japanese War page: 'The Japanese captured the city on July 29'; 'The Taku Forts at Tianjin fell on 30 July'; 'On 6 June, they captured Kaifeng, the capital of Henan'; 'the floods in Henan and Anhui destroyed much of the tracks and bridges'.
- Fix: confidence lowered to 2, reviewer notes appended.

### /ledger/37 [APPLIED by reviewer]
- What: The occupation of northern French Indochina was dated 1941 (Cliopatria's year). The 102 cells are Tonkin (20.5-22.3 N), the zone entered first, and the page gives the occupation as 1940-41.
- Why: Empire page: 'the occupation of French Indochina in the years of 1940–41'; the note's own quote: 'After Japanese advancements into French Indochina in 1940'.
- Fix: year 1940, confidence 2 kept, reviewer note appended.

## Thin (for a gap-filler)
- /ledger/2, /ledger/4, /ledger/5: Boshin War fronts by year and the right opponents (Northern Alliance in 1868, Ezo 1869). Try https://en.wikipedia.org/wiki/Boshin_War
- /ledger/31: End of East Hebei at confidence 1 (July 1937); the reviewer's reading is that it was merged into the Provisional Government in 1938, to be confirmed on the page. Try https://en.wikipedia.org/wiki/East_Hebei_Autonomous_Council
- /ledger/36: Guangdong (Canton fell in October 1938) and Hainan (1939) at confidence 1, one year for both. Try https://en.wikipedia.org/wiki/Canton_Operation
- /ledger/44: Portuguese Timor occupation, confidence 1. Try https://en.wikipedia.org/wiki/Battle_of_Timor
- /ledger/48: March 1945 coup in Indochina, confidence 1, no month. Try https://en.wikipedia.org/wiki/Japanese_coup_d%27%C3%A9tat_in_French_Indochina
- /ledger/61: End of Mengjiang, confidence 1. Try https://en.wikipedia.org/wiki/Mengjiang
- /keyframe_review/25 (20 Indian cells): Andaman and Nicobar occupation 1942-1945 against british-raj: the cells are in the 1943 shape with no ledger event. Try https://en.wikipedia.org/wiki/Japanese_occupation_of_the_Andaman_and_Nicobar_Islands
- /ledger (missing): Aleutians (Attu, Kiska, 1942-1943, united-states-of-america), the Gilbert Islands and Nauru (1942-1943/1945). Try https://en.wikipedia.org/wiki/Aleutian_Islands_campaign
- /ledger/54, /ledger/73: US recapture of the Marshalls, Marianas and Palau in 1944 (an owner-first occupation of mandate land before the 1945 loss). Try https://en.wikipedia.org/wiki/Mariana_and_Palau_Islands_campaign
- /ledger (missing): Bonin (Ogasawara) annexation, 1876. Try https://en.wikipedia.org/wiki/Bonin_Islands
- /ledger/18: Siberian intervention beyond Primorye (Amur and Transbaikal, 1918-1920). Try https://en.wikipedia.org/wiki/Siberian_intervention
- /ledger/63-80: Pacific War and China occupation ends before September 1945 (Burma by May 1945, the Philippines 1944-1945, Guadalcanal 1943); the Wang Jingwei, Provisional and Reformed client governments. Try https://en.wikipedia.org/wiki/Wang_Jingwei_regime

## Spot checks
- /ledger/6: confirmed (https://en.wikipedia.org/wiki/Treaty_of_Saint_Petersburg_(1875)). 'The treaty itself went into effect in 1877'; 'signed on 7 May 1875, and its ratifications exchanged at Tokyo on 22 August 1875'
- /ledger/7: confirmed (https://en.wikipedia.org/wiki/Treaty_of_Saint_Petersburg_(1875)). same page, Kurils for Sakhalin, 1877 in force
- /ledger/12: confirmed (https://en.wikipedia.org/wiki/Empire_of_Japan). 'The Korean Empire was then occupied and declared a Japanese protectorate following the Japan–Korea Treaty of 1905.'
- /ledger/17: mis-dated (https://en.wikipedia.org/wiki/Empire_of_Japan). 1915 should be 1914 (the page names the islands and the November 1914 surrender); fixed by the reviewer
- /ledger/26, /ledger/27, /ledger/58: confirmed (https://en.wikipedia.org/wiki/Manchukuo). 'Established: 1 March 1932'; 'Rehe annexed: 4 March 1933'; 'Dissolution: 20 August 1945'
- /ledger/30: confirmed (https://en.wikipedia.org/wiki/Second_Sino-Japanese_War). dates confirmed (29 and 30 July 1937); the region (whole Hebei) is wider than the page, so confidence lowered to 2
- /ledger/34: confirmed (https://en.wikipedia.org/wiki/Second_Sino-Japanese_War). 'On 6 June, they captured Kaifeng, the capital of Henan'; the whole province is not on the page (confidence lowered to 2)
- /ledger/35: confirmed (https://en.wikipedia.org/wiki/Second_Sino-Japanese_War). 'the Nationalists were forced to abandon Wuhan by October'; Anhui is not dated (confidence lowered to 2)
- /ledger/37: mis-dated (https://en.wikipedia.org/wiki/Empire_of_Japan). 'the occupation of French Indochina in the years of 1940–41'; the Tonkin cells are the 1940 zone; fixed to 1940
- /ledger/38: confirmed (https://en.wikipedia.org/wiki/Pacific_War). 'fell to Japanese forces on 25 December 1941'
- /ledger/41: confirmed (https://en.wikipedia.org/wiki/Pacific_War). 'the capture of Rabaul on 23 January 1942'
- /ledger/42: confirmed (https://en.wikipedia.org/wiki/Pacific_War). 'In January, Japan invaded British Burma, the Dutch East Indies, New Guinea, and the Solomon Islands.'
- /ledger/54: confirmed (https://en.wikipedia.org/wiki/Allied_occupation_of_Japan). map caption: 'occupied by the United States 1945–1947' (the 1944 battles are not recorded; see thin)
- /ledger/82: confirmed (https://en.wikipedia.org/wiki/Allied_occupation_of_Japan). 'until the Treaty of San Francisco took effect on April 28, 1952'
- /ledger/83, /ledger/84, /ledger/85: confirmed (https://en.wikipedia.org/wiki/Allied_occupation_of_Japan). 'the Amami Islands (until 1953)'; 'Iwo Jima was returned to Japan in 1968'; 'most of Okinawa was returned in 1972'

## Cross-dossier matrix (only the entries that are not exceptions)
- empire-of-japan 1868 found tokugawa-shogunate -> matched: tokugawa-shogunate /ledger/12 loss 1868-1 to empire-of-japan and /ledger/15 dissolve 1868-1 with successor empire-of-japan.
- empire-of-japan 1879 gain ryukyu-kingdom -> matched: ryukyu-kingdom /ledger/19 dissolve 1879-3 to empire-of-japan (and /ledger/18 vassal_end 1879-3); this side has no month.
- empire-of-japan 1942 occupation_start commonwealth-of-australia -> mismatch: Years agree (Australia 1942-1 / 1945-8 against 1942-1 / 1945-9) but the type does not: Australia records a contest (its /ledger/13-16, with a separate Papua contest 1942-7 to 1943-1), this dossier an occupation of the whole intersect of PNG with the 1943 shape from 1942-1. One rule for both sides is needed; the Papua beachhead (Buna/Gona, July 1942 to January 1943) is not separate here.
- empire-of-japan 1945 occupation_end commonwealth-of-australia -> mismatch: Years agree (Australia 1942-1 / 1945-8 against 1942-1 / 1945-9) but the type does not: Australia records a contest (its /ledger/13-16, with a separate Papua contest 1942-7 to 1943-1), this dossier an occupation of the whole intersect of PNG with the 1943 shape from 1942-1. One rule for both sides is needed; the Papua beachhead (Buna/Gona, July 1942 to January 1943) is not separate here.
- ryukyu-kingdom 1872 vassal_start empire-of-japan -> missing: ryukyu-kingdom has vassal_start 1872-10 and vassal_end 1879-3 with counterpart empire-of-japan ('Domain of the Empire of Japan (1872–1879)', 'Reorganized into Ryukyu Domain: 16 October 1872'); empire-of-japan has neither, although its own 1870 keyframe note defers the 1872-1879 domain to the ryukyu dossier.
- tokugawa-shogunate 1868 contest_end russian-empire -> matched: the Sakhalin contest passes from the shogunate to empire-of-japan /ledger/1 in 1868-1 (hand-over, not a mirror pair).
- Every other territorial event (76) is an exception: its counterpart has no dossier yet and is either in the author's counterparts_needing_dossiers or owned by a group that has not run (eu-17, ea-08, jk-02, eu-20, se-03, eu-11, am-07, eu-21, se-01 e-f).

## What I tried and could not break
- The merge of the two Cliopatria rows into one dossier, argued from the Empire page ('became simply the modern state of Japan'; 'Reconstituted: May 3, 1947').
- The 1877 Sakhalin-Kuril exchange (the page says 'The treaty itself went into effect in 1877'), the 1905 and 1910 Korea events, and the Manchukuo dates.
- The post-1945 returns: Amami 1953, the Nanpo Islands and Iwo Jima 1968, Okinawa 1972, and the end of the occupation on 28 April 1952.
- The 1932-1945 policy of using the 1929 shape for direct land, with vassal and occupation events on top, and the new keyframes for 1896, 1946-1952 and 1972.
- The rulers (contiguous 1868-2024) and the capitals (Tokyo inside the shapes).
