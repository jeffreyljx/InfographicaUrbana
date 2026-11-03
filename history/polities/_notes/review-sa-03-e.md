# Review of batch sa-03-e (2026-10-19)

Reviewer: Phase B adversarial reviewer. Dossiers: chola-empire, sind-habbari-dynasty, soomra-dynasty, chandra-dynasty. Validator: 0 errors on all four (warnings: unknown counterpart slugs listed by the author; the split Sind-Habbari row gives 'no verdict' warnings in each half). Pages opened: Rajaraja I, Rajendra Chola I, Kulottunga I, Chola Empire, Later Cholas, Pandya Empire, Habbari dynasty (twice), Soomra dynasty, Chandra dynasty. Areas below come from history/tools/gazetteer.py resolve.

Verdict 'fix' would mean fixed by the reviewer; 'thin' means valid with gaps for a gap-filler (unapplied fixes there are non-blocking); 'fail' means back to the author.

## chola-empire: fail

Area: Chola Empire infobox has no area (confirmed on the page); the author says so in KF1.

### Findings

1. `/keyframe_review/10, /keyframe_review/11, /keyframe_review/12` (for the author). The 970, 1000 and 1010 shapes (all 'ok') leave out northern Sri Lanka, which /ledger/11 gains in 993 (confidence 3) and keeps until 1070, so the keyframes contradict the ledger for 993-1017 across three shapes.
   - Evidence: Rajaraja I page: 'In 993, Rajaraja achieved the conquest of Anuradhapura ... resulting in the acquisition of the northern portion of Sri Lanka by the Chola empire.' Gazetteer: Chola 1000 shape intersect Anuradhapura 110 km = 0 cells; the region is 27,819 km2. Sri Lanka first appears in the 1018 shape. KF10's note says the gain is 'added by the ledger', but the brief accepts an untraced event only when it is small and inside one shape's span.
   - Fix: Make KF10 a years-only adjust valid 970-992; add a new keyframe chola-empire_993 (993-999) = {"union": [{"cliopatria": "Chola Empire", "year": 970}, {"place": "Anuradhapura", "km": 110}]}; set KF11 and KF12 to adjust with the same union on their own Cliopatria years.

2. `/keyframe_review/17/correction` (for the author). The correction removes Sri Lanka from the whole 1056 shape (1056-1093), but the note says '1056-1069 stand as drawn', and /ledger/27 (confidence 3) keeps the island Chola until 1070.
   - Evidence: A correction stands for the shape's whole span: it cannot say 'from 1070'. Kulottunga I page: 'In 1070, Vijayabahu attacked the Chola forces ... and defeated them'; Rajendra Chola I page: 'The Chola reign over Sri Lanka persisted until 1070.' The same pattern is in KF8 (Tondaimandalam removed from 947, lost 949), which is tolerable because 944-949 is a contest.
   - Fix: Make KF17 a years-only adjust valid 1056-1069 (shape unchanged) and add a new keyframe chola-empire_1070 (1070-1093) with {"minus": [{"cliopatria": "Chola Empire", "year": 1056}, {"country": "Sri Lanka"}]}, as was done for chola-empire_915.

3. `/keyframe_review/20` (for the author). The 1111 shape ('ok') already lacks Gangavadi in 1111, although /ledger/31 loses it in 1116, and it keeps Vengi until 1125, although /ledger/32 loses Vengi c. 1118; the note ('dated events inside these years are added by the ledger') misreads the shape.
   - Evidence: Gazetteer: Chola 1099 minus Chola 1111 = 92,056 km2 (bbox 74.68-78.12E, 11.64-14.92N), exactly the overlap of Chola 1099 with Cliopatria's Hoysala 1111 shape (92,056 km2). Chola 1111 intersect Rajahmundry 130 km = 34,142 km2 (Vengi still drawn). Hoysala page: Talakadu 1116; Chola Empire page: 'Around 1118, the Cholas lost control of Vengi to the Western Chalukya and Gangavadi ... to the Hoysala Empire'; Kulottunga I page: 'a brief occupation of the Vengi territories between 1118 and 1126'.
   - Fix: Split KF20: new keyframe 1111-1115 = {"union": [{"cliopatria": "Chola Empire", "year": 1111}, {"intersect": [{"cliopatria": "Chola Empire", "year": 1099}, {"cliopatria": "Hoysala Kingdom", "year": 1111}]}]}; 1116-1117 the 1111 shape as drawn; 1118-1125 {"minus": [{"cliopatria": "Chola Empire", "year": 1111}, <the Vengi union of /ledger/32>]}.

4. `/keyframe_review/21` (for the author). The 1126 shape ('ok', 1126-1138) lacks Vengi, but /ledger/33 regains it in 1133; the note itself says 'Cliopatria regains it in 1139' and leaves the verdict at ok.
   - Evidence: Kulottunga I page: 'By 1133 Vikrama Chola defeated Someshvara III in the Battle of Godavari.' Chola 1126 intersect Rajahmundry 130 km = 253 km2 (Vengi absent); about 66,000 km2 regained in Cliopatria only from 1139.
   - Fix: Make KF21 a years-only adjust valid 1126-1132 and add a new keyframe chola-empire_1133 (1133-1138) = {"cliopatria": "Chola Empire", "year": 1139} (or the 1126 shape plus the Vengi union of /ledger/33).

5. `/identity/capitals/1 and /keyframe_review/28` (for the author). Gangaikonda Cholapuram (79.449E, 11.206N), the capital to 1279, lies outside every Chola shape from 1241 (the 1241, 1250 and 1260 keyframes); the 1250 remnant (7,865 km2 at 79.0-80.25E, 13.66-14.88N) sits around Nellore, the very country /ledger/37 says the Pandyas marched to by 1250, yet KF28 is 'ok'.
   - Evidence: Gazetteer: Chola 1241 and Chola 1250 shapes intersect 15 km of the capital = 0 cells; Pandya Empire 1250 shape intersect = 3 cells. Later Cholas page: 'The Pandyans marched to Arcot; Tirumalai, Nellore, Visayawadai, Vengi, and Kalingam by 1250.' Pandya Empire page: 'the ancient Chola country was now overrun by the Pandyas'; no page says where Rajendra III ruled after 1246.
   - Fix: End the Gangaikonda Cholapuram capital at 1240 (seat page silent from 1241, say so in the note), and set KF28 and KF29 notes to say the remnant's location contradicts /ledger/37 and is unverified (verdict adjust with text, or a gap-filler page on Rajendra III).

6. `/keyframe_review/29 and /ledger (missing event)` (for the author). KF29 draws 1260-1279 'as a vassal of the Pandya Empire', but the ledger has no vassal_start for it (nor for the 1216 submission).
   - Evidence: Pandya Empire page: 'Jatavarman Sundara I subdued Rajendra II around 1258-1260 CE and made him pay tribute' (the page's 'Rajendra II' is Rajendra III, as the author notes) and, for 1216, 'The Chola king subsequently made a formal submission to Maravarman Sundara I and acknowledged his overlordship.'
   - Fix: Add vassal_start, counterpart pandya-empire, 1258 (confidence 2, Pandya Empire page), closed by the 1279 dissolve; consider a vassal_start/vassal_end pair 1216-1217 (Hoysala restoration in 1217 on the same page).

7. `/ledger/20` (applied by reviewer). The 1019 Pandya gain named {"region": "Tamil Nadu (region)"} (123,668 km2, the whole state including the Chola core at Thanjavur and Kanchi) and the counterpart pandya-dynasty, whose dossier ends in 915.
   - Evidence: Rajendra Chola I page (opened): 'In 1018 and 1019 CE, Rajendra invaded and conquered the Pandya and Chera Perumal kingdoms.' Gazetteer: Tamil Nadu (region) bbox 76.27-80.24E, 8.17-13.45N. pandya-dynasty ledger ends with dissolve 915; the author's own report flags pandya-kingdom-915-1216 as the counterpart needing a dossier.
   - Fix: Applied: region set to {"cliopatria": "Pandya Dynasty", "year": 900, "text": "the Pandya kingdom, Madurai and the south"} (as /ledger/6) and counterpart to pandya-kingdom-915-1216; the same slug replaces pandya-dynasty among the belligerents of /wars/7 and /wars/11. Re-validated: 0 errors.

8. `/ledger/22, /ledger/23` (for the author). The Srivijaya contest runs 1023-1024 here but 1025-1026 in the srivijaya dossier, and this dossier's own /wars/9 runs to 1025.
   - Evidence: Rajendra Chola I page gives both 'overseas war expedition commenced in 1023' / 'ended in 1024' and 'In 1025 CE, Rajendra's Chola forces crossed the Indian Ocean and invaded Srivijaya'; srivijaya /ledger/5-6 use the Srivijaya page infobox 'Date: 1025-1026'.
   - Fix: Date the contest over Kedah and Palembang 1025-1026 (keep 1023 as the start of the expedition in the war entry), or record in the note why 1023-1024 is preferred so the srivijaya author can align.

9. `/identity/rulers` (for the author). Gandaraditya (955-957) and Arinjaya (956-957) overlap, and only the first ruler entry carries a source.
   - Evidence: Rulers must be contiguous and cite a page (brief 2.9).
   - Fix: Make the reigns contiguous (e.g. Gandaraditya 955-956) and give each entry the Chola Empire page as source.

### Gaps for a gap-filler

- `/keyframe_review/7, /keyframe_review/10`: The far south (Tirunelveli, below 9.2N; 19,000 km2) leaves the Chola shape in 936 and 970 and returns in 960 and 1000 with no event either way. Page to try: https://en.wikipedia.org/wiki/Parantaka_II
- `/keyframe_review/15`: The 1034-1039 shape is 131,255 km2 smaller than 1018 (gazetteer: bbox 74.68-82.32E, 12.68-17.3N, the Rattapadi-Vengi belt) and is restored in 1040; no event. Page to try: https://en.wikipedia.org/wiki/Rajadhiraja_Chola
- `/ledger/19 (Kerala)`: Kerala, gained 1018, is never lost: the shape's west edge moves 74.6E to 75.2E (1111), 75.86E (1126), 77.32E (1216); of the 1177-1216 drop, 50,580 km2 lies outside the Pandya 1216 shape that /ledger/35 names, 26,049 km2 of it in Kerala. Page to try: https://en.wikipedia.org/wiki/Venad
- `/ledger/34`: Who took Vengi and the north in 1177 (confidence 1, kakatiya-dynasty guessed). Page to try: https://en.wikipedia.org/wiki/Velanati_Chodas
- `/ledger/36`: The 1241 contraction of the Kaveri country (confidence 1). Page to try: https://en.wikipedia.org/wiki/Rajaraja_III
- `/ledger/10, /ledger/16, /ledger/24, /ledger/26`: Confidence-1 bridges: Tondaimandalam recovery 967, Kalinga 1010, capital move 1025, Vengi 1045. Page to try: https://en.wikipedia.org/wiki/Eastern_Chalukyas
- `/ledger/18`: End of the Chola hold on the Maldives and Lakshadweep (no end, so they stay Chola to 1279). Page to try: https://en.wikipedia.org/wiki/History_of_the_Maldives
- `/keyframe_review/26`: The Hoysala hegemony over the Cholas 1220-1245 is left to the Hoysala dossier; a vassal relation belongs in both ledgers. Page to try: https://en.wikipedia.org/wiki/Hoysala_Empire
- `/keyframe_review/2`: The 886 growth (3,058 to 7,000 km2) has no event (unverified: page budget). Page to try: https://en.wikipedia.org/wiki/Aditya_I

### Spot checks

- `/ledger/1` on https://en.wikipedia.org/wiki/Chola_Empire: confirmed
- `/ledger/11` on https://en.wikipedia.org/wiki/Rajaraja_I: confirmed
- `/ledger/12` on https://en.wikipedia.org/wiki/Rajaraja_I: confirmed
- `/ledger/17` on https://en.wikipedia.org/wiki/Rajendra_Chola_I: confirmed
- `/ledger/18` on https://en.wikipedia.org/wiki/Rajendra_Chola_I: confirmed
- `/ledger/27` on https://en.wikipedia.org/wiki/Kulottunga_I: confirmed
- `/ledger/28` on https://en.wikipedia.org/wiki/Kulottunga_I: confirmed
- `/ledger/30` on https://en.wikipedia.org/wiki/Chola_Empire: confirmed
- `/ledger/33` on https://en.wikipedia.org/wiki/Kulottunga_I: confirmed
- `/ledger/37` on https://en.wikipedia.org/wiki/Later_Cholas: confirmed
- `/ledger/38` on https://en.wikipedia.org/wiki/Pandya_Empire: confirmed

## sind-habbari-dynasty: thin

Area: No area on the page (its 'greater in area than the modern Pakistani province of Sindh' refers to Umayyad Greater Sindh). The correction (Sind province, 142,130 km2) is 0.62 of Cliopatria's 860 shape; the 106,471 km2 removed is 50,833 in Pakistani Punjab (Uch, Bahawalpur), 29,842 in India (Thar) and 25,796 in Balochistan; acknowledged in KF0's note and supported by the page except for Khuzdar before c. 900.

### Findings

1. `/keyframe_review/0/correction` (for the author). The correction is the province of Sindh only, while its own text says Khuzdar is excluded only 'after the late 9th century', and the author's gap says the page gives no year for Khuzdar; the page does.
   - Evidence: Habbari dynasty page: the state 'controlled the region between the Arabian Sea and Aror, and Khuzdar in central Balochistan'; the Habbaris 'ruled over the area of Turan (modern Khuzdar), until the end of the 9th century', when Mughira bin Ahmad 'established his independence and moved his capital to Kijkanan (modern Kalat)'. Gazetteer: the Balochistan part of Cliopatria's 860 shape is 25,796 km2.
   - Fix: Add a new keyframe 861-899 = {"union": [{"admin1": "Sind", "country": "Pakistan"}, {"place": "Khuzdar", "km": 100, "text": "Turan (modern Khuzdar)"}]}, make KF0 valid from 900 (or keep KF0 and split), and add a loss of Turan c. 900 (bridge, confidence 2, counterpart nobody or a Turan entry) citing the Habbari page.

### Gaps for a gap-filler

- `/keyframe_review/0`: Year of the loss of Turan/Khuzdar (page: 'until the end of the 9th century') and whether the Aror region's subordinate Hindu raja counts as Habbari land (page: Habbaris ruled 'central and southern Sindh south of Aror'). Page to try: https://en.wikipedia.org/wiki/Khuzdar

### Spot checks

- `/ledger/0` on https://en.wikipedia.org/wiki/Habbari_dynasty: confirmed
- `/ledger/1` on https://en.wikipedia.org/wiki/Habbari_dynasty: confirmed
- `/ledger/2` on https://en.wikipedia.org/wiki/Soomra_dynasty: confirmed
- `/ledger/3` on https://en.wikipedia.org/wiki/Habbari_dynasty: confirmed
- `/ledger/4` on https://en.wikipedia.org/wiki/Habbari_dynasty: confirmed

## soomra-dynasty: thin

Area: No area on the page; the Sind correction (142,130 km2) is 0.62 of Cliopatria's 1028 shape, acknowledged in KF1.

### Findings

1. `/ledger (missing events)` (for the author). The Ghaznavid tributary status 1026-1030 and the Ghurid subjugation of 1182 are left out of the ledger 'because the types fit the other side'; a vassal relation is carried in the vassal's ledger too (vassal_start with the overlord as counterpart).
   - Evidence: Soomra dynasty infobox: 'Tributary of the Ghaznavids (1026-1030)'; Muhammad of Ghor page (author's source): Debal taken and the Soomras subjugated in 1182; reviewer brief 2.3: 'a vassal_start of X is a vassal_start in X's ledger with this state as counterpart'.
   - Fix: Add vassal_start 1026 / vassal_end 1030, counterpart ghaznavid-empire (Soomra page, confidence 3), and vassal_start 1182, counterpart ghurid-dynasty (Muhammad of Ghor page, confidence 2) with its end at the Ghurid collapse (1206 on the same page).

### Gaps for a gap-filler

- `/keyframe_review/7`: No page for 1202-1351: Soomra extent under Qabacha, Iltutmish ('Shimuddin Chamisar had submitted to Iltutmish ... allowed to continue as a vassal', undated) and the Tughluqs, and the 1344-1351 overlap with Cliopatria's Sind-Samma row. Page to try: https://en.wikipedia.org/wiki/Samma_dynasty
- `/identity/capitals/0`: Mansura is given as the seat for 1026-1351; the page lists 'Mansura (1026)' and Thari without dates and the Mansura page says the city never recovered. Page to try: https://en.wikipedia.org/wiki/Thari_(Badin)
- `/identity`: Whether the Habbari-Soomra change is a new state or a rename (the Soomra table lists Khafif 1010-1026, whom the Habbari page calls the last Habbari ruler): orchestrator's call; the split is documented in both files. Page to try: https://en.wikipedia.org/wiki/Soomra_dynasty

### Spot checks

- `/ledger/0` on https://en.wikipedia.org/wiki/Soomra_dynasty: confirmed
- `/ledger/1` on https://en.wikipedia.org/wiki/Soomra_dynasty: confirmed
- `/identity/capitals/0` on https://en.wikipedia.org/wiki/Soomra_dynasty: confirmed

## chandra-dynasty: fail

Area: Chandra dynasty infobox has no area (confirmed).

### Findings

1. `/keyframe_review/1, /keyframe_review/2, /ledger/3/region` (for the author). The 947 shape ('ok', 947-1045) and the 1046 shape (years only) leave out Bikrampur, the capital from 930, and the Srihatta-mandala, which /ledger/1 and /ledger/2 gain in 930 and never lose; the dissolve region's text names 'Bikrampur, Sylhet' but its spec (Cliopatria 1046) holds neither.
   - Evidence: Gazetteer: Chandra 947 shape intersect 10 km of Bikrampur (90.47E, 23.54N) = 0 cells; Dhaka 40 km minus the 947 shape = 4,299 km2; Sylhet (region) = 12,139 km2, all outside. Chandra dynasty page: 'the administrative centre of the Chandra kingdom was established in Bikrampur in Vanga'; 'the Srihatta-mandala (greater Sylhet and southern Assam plains)'. The capital sits 86 km outside the drawn state for 120 years.
   - Fix: Set KF1 and KF2 to adjust with {"union": [{"cliopatria": "Chandra Dynasty", "year": 947 (1046)}, {"place": "Dhaka", "km": 40}, {"region": "Sylhet (region)"}]} and use the same union (on 1046) as the dissolve region.

2. `/keyframe_review/0/correction` (for the author). The correction adds Bikrampur for the whole 900-946 span while its note and /ledger/1 date it from c. 930, and it omits the Samatata (Comilla) land the found event names.
   - Evidence: Gazetteer: the found region (Comilla 70 km plus Chattogram 70 km) extends 11,128 km2 beyond the Cliopatria 900 shape (west of 91.3E). A correction stands for the shape's whole span.
   - Fix: KF0 = {"union": [{"cliopatria": "Chandra Dynasty", "year": 900}, {"place": "Comilla", "km": 70}]} valid 900-929, plus a new keyframe chandra-dynasty_930 (930-946) adding Bikrampur and Sylhet as in the fix above.

### Gaps for a gap-filler

- `/identity/rulers`: No ruler list, though the page's table reads 'Traillokyachandra 900-930, Srichandra 930-975, Kalyanachandra 975-1000, Ladahachandra 1000-1020, Govindachandra 1020-1050'. Page to try: https://en.wikipedia.org/wiki/Chandra_dynasty
- `/wars`: Rajendra Chola's Ganges expedition, which the chola-empire dossier carries (/wars/8, 1019-1022, 'the rulers of Kalinga, Odisha and Bengal'), is absent here; the Chandra king of Vanga then was Govindachandra. Page to try: https://en.wikipedia.org/wiki/Rajendra_Chola_I
- `/ledger/1, /ledger/2`: Who held Vanga and Sylhet before c. 930 (confidence 1, counterparts guessed). Page to try: https://en.wikipedia.org/wiki/Samatata
- `/ledger/3`: The end: Pala annexation (Chandra page) vs the Varmans (Harikela page), 1050 vs Cliopatria 1055. Page to try: https://en.wikipedia.org/wiki/Varman_dynasty_(Bengal)

### Spot checks

- `/ledger/0` on https://en.wikipedia.org/wiki/Chandra_dynasty: confirmed
- `/ledger/1` on https://en.wikipedia.org/wiki/Chandra_dynasty: confirmed
- `/ledger/2` on https://en.wikipedia.org/wiki/Chandra_dynasty: confirmed
- `/ledger/3` on https://en.wikipedia.org/wiki/Chandra_dynasty: confirmed

## Cross-dossier matrix

| event | counterpart | mirror | status | note |
| --- | --- | --- | --- | --- |
| chola-empire 848 found | muttaraiyar | - | exception | no dossier; listed in counterparts_needing_dossiers |
| chola-empire 850 gain | muttaraiyar | - | exception | no dossier; listed |
| chola-empire 897 gain | late-pallava-empire | late-pallava-empire 897 dissolve | matched |  |
| chola-empire 897 gain | pandya-dynasty | pandya-dynasty 897 loss | matched | Kongu |
| chola-empire 910 occupation_start | pandya-dynasty | pandya-dynasty 910 occupation_start | matched | Madurai |
| chola-empire 915 occupation_end | pandya-dynasty | pandya-dynasty 915 occupation_end | matched |  |
| chola-empire 915 gain | pandya-dynasty | pandya-dynasty 915 dissolve | matched |  |
| chola-empire 944 contest_start | rashtrakuta-dynasty | rashtrakuta-dynasty 944 contest_start | matched |  |
| chola-empire 949 contest_end | rashtrakuta-dynasty | rashtrakuta-dynasty 949 contest_end | matched |  |
| chola-empire 949 loss | rashtrakuta-dynasty | rashtrakuta-dynasty 944 gain | mismatch | Tondaimandalam: Chola loses it at Takkolam 949, Rashtrakuta gains it 944 ('secured by 944'); both sides hold a 944-949 contest, so one of them should date the transfer to the other's year |
| chola-empire 967 gain | rashtrakuta-dynasty | rashtrakuta-dynasty 967 loss | matched | both confidence 1 bridges |
| chola-empire 993 gain | anuradhapura | anuradhapura 993 loss | matched |  |
| chola-empire 998 gain | western-ganga-dynasty | western-ganga-dynasty 998 loss | matched |  |
| chola-empire 1001 vassal_start | eastern-chalukyas | - | exception | no dossier; listed |
| chola-empire 1003 contest_start | western-chalukya-empire | - | exception | counterpart owned by a group that has not run yet (sa-03) |
| chola-empire 1005 gain | venad | - | exception | no dossier; listed |
| chola-empire 1010 gain | eastern-ganga-kingdom | - | exception | counterpart owned by a group that has not run yet (sa-03) |
| chola-empire 1017 gain | anuradhapura | anuradhapura 1017 dissolve | matched |  |
| chola-empire 1018 gain | chera-perumal-kingdom | - | exception | no dossier; listed |
| chola-empire 1019 gain | pandya-kingdom-915-1216 | - | exception | counterpart corrected by the reviewer from pandya-dynasty (ended 915); no dossier, listed |
| chola-empire 1023 contest_start | srivijaya | srivijaya 1025 contest_start | mismatch | two years apart; see chola fix /ledger/22 |
| chola-empire 1024 contest_end | srivijaya | srivijaya 1026 contest_end | mismatch | two years apart |
| chola-empire 1031 contest_start | eastern-chalukyas | - | exception | no dossier; listed |
| chola-empire 1070 loss | kingdom-of-polonnaruwa | - | exception | counterpart owned by a group that has not run yet (sa-03) |
| chola-empire 1075 gain | eastern-chalukyas | - | exception | no dossier; listed (with the 1075 vassal_end) |
| chola-empire 1116 loss | hoysala-kingdom | - | exception | counterpart owned by a group that has not run yet (sa-03); Cliopatria's Hoysala row takes Gangavadi from 1111 |
| chola-empire 1118 loss | western-chalukya-empire | - | exception | counterpart owned by a group that has not run yet |
| chola-empire 1133 gain | western-chalukya-empire | - | exception | counterpart owned by a group that has not run yet |
| chola-empire 1177 loss | kakatiya-dynasty | - | exception | counterpart owned by a group that has not run yet; confidence 1 |
| chola-empire 1216 loss | pandya-empire | - | exception | counterpart owned by a group that has not run yet (sa-04) |
| chola-empire 1241 loss | pandya-empire | - | exception | counterpart owned by a group that has not run yet |
| chola-empire 1250 loss | pandya-empire | - | exception | counterpart owned by a group that has not run yet |
| chola-empire 1279 dissolve | pandya-empire | - | exception | counterpart owned by a group that has not run yet |
| sind-habbari-dynasty 861 found | abbasid-caliphate | - | exception | counterpart owned by a group that has not run yet (me-08) |
| sind-habbari-dynasty 1025 contest_start | ghaznavid-empire | - | exception | counterpart owned by a group that has not run yet (me-08) |
| sind-habbari-dynasty 1026 dissolve | soomra-dynasty | soomra-dynasty 1026 found | matched |  |
| gurjara-pratihara-dynasty 860 gain | sind-habbari-dynasty | - | mismatch | Pratihara /ledger/21 gains a Sindh strip from the Habbaris in 860 (confidence 1, a Cliopatria overlap); the Habbari dossier starts 861 and holds all Sindh; the Pratihara dossier should drop it or the Habbari correction should exclude the strip |
| gurjara-pratihara-dynasty 936 loss | sind-habbari-dynasty | - | mismatch | Pratihara /ledger/26 returns the strip in 936; no Habbari gain |
| soomra-dynasty 1026 found | sind-habbari-dynasty | sind-habbari-dynasty 1026 dissolve | matched |  |
| soomra-dynasty 1026 vassal_start (missing) | ghaznavid-empire | - | missing | Soomra infobox 'Tributary of the Ghaznavids (1026-1030)'; neither ledger carries it (ghaznavid-empire, me-08, not run) |
| soomra-dynasty 1351 dissolve | sind-samma-dynasty | - | exception | sind-samma-dynasty has no dossier yet; Cliopatria's Samma row overlaps 1344-1351 |
| chandra-dynasty 900 found | harikela-kingdom | - | exception | no dossier; listed |
| chandra-dynasty 930 gain | pala-empire | pala-empire 947 loss | mismatch | east Bengal / Vanga: Chandra gains it c. 930 (confidence 1), Pala loses it to the Chandras in 947 (confidence 1); 17 years apart |
| pala-empire 981 gain | chandra-dynasty | - | mismatch | Pala /ledger/15 recovers 'eastern Bengal' from the Chandras in 981 (confidence 1); the Chandra dossier keeps Vanga to 1050 and the Chandra page lists Chandra kings to 1050, so the Pala counterpart is doubtful |
| chandra-dynasty 930 gain | kamarupa-kingdom | - | missing | kamarupa-kingdom dossier exists and has no loss of Sylhet; confidence 1 on the Chandra side |
| chandra-dynasty 1050 dissolve | pala-empire | - | missing | pala-empire has no 1050 gain of the Chandra land (it has a Varman east Bengal from 1072) |

## Problems

- No page failed to load. WebFetch extractions contradicted themselves on two pages (Rajendra Chola I: Srivijaya 1023-1024 and 1025; Pandya Empire: 'Rajendra II' for Rajendra III), as the author also noted.
- The Sind-Habbari row is split into sind-habbari-dynasty (861-1026) and the new soomra-dynasty (1026-1351); both list 'Sind-Habbari Dynasty', so each gets 'no verdict' warnings for the other's shapes. The split is documented; whether it is a new state or a rename is the orchestrator's call.
- Reviewer edit: chola-empire /ledger/20 region and counterpart and /wars/7, /wars/11 belligerents (pandya-dynasty to pandya-kingdom-915-1216); file re-validated (0 errors) and read back.
- Most Chola counterparts (hoysala-kingdom, western-chalukya-empire, kakatiya-dynasty, kingdom-of-polonnaruwa, eastern-ganga-kingdom, pandya-empire) belong to groups that have not run; their mirror events must be checked when they are written.
- counterparts_needing_dossiers years are the years these dossiers use the counterpart (from the author's report and the pala-empire dossier), not the counterparts' lives.
