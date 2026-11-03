# Review ea-06-b (Yuan, part b): tibet

Reviewer, 2026-10-19. One dossier: `history/polities/tibet.json` (49 Cliopatria shapes, budget 14 pages, spot-check budget 6). Validator (`--resolve`): 0 errors, 3 warnings (counterpart `kingdom-of-ladakh` has no dossier; listed by the author). Verdict: **fail** (four unapplied blocking findings: two shape corrections contradict the dossier's own text and the 1642 gain has the wrong land and counterpart). One small fix applied by the reviewer (/ledger/12 confidence 2 to 1; re-validated, 0 errors).

## Mechanical checks
- Ledger sorted; found 1354 = start, dissolve 1951-05 = end; capitals contiguous (Nedong 1354-1564, Shigatse 1565-1641, Lhasa 1642-1951), coordinates inside the shapes; certainty covers 1354-1951 without gaps.
- Rulers: 1354-1432 (confirmed on the Phagmodrupa page, reigns exact) and 1565-1642; gap 1432-1565 and nothing after 1642 (author flagged; thin).
- 49 Cliopatria shapes all have verdicts; 4 new keyframes carry from/to/correction.
- /ledger/35 (1914 contest_start, Tawang) has no war entry, contrary to rule 10 (every contest_start in a war's zone).

## Spot checks (all on the pages cited)
- /ledger/20 (1727, Kham east of the Dri to Sichuan, c3): confirmed, Tibet under Qing rule ("annexed to Sichuan in 1726-1727 through a treaty"). Also confirmed there: /ledger/19 (Qinghai 1724), /ledger/30 (Lhasa 1910), /ledger/28 ("either 1905 or 1908").
- /ledger/36 (1918 Chamdo and western Kham, c3): confirmed, Tibet (1912-1951) ("In 1918, Lhasa regained control of Chamdo and western Kham." "A truce set the border at the Yangtze River."). Also /ledger/31 (Three Point Agreement, infobox 12 August 1912) and /ledger/44 ("In 1951 Ü-Tsang and the western Kham area of Chamdo were annexed by the newly formed People's Republic of China") confirmed.
- /ledger/43 (Chamdo, October 1950, c3): confirmed, Annexation of Tibet by the PRC (Jinsha crossed 6 or 7 October; Chamdo taken by 19 October; Qamdo Liberation Committee).
- /ledger/0 (found 1354, c3): confirmed, Phagmodrupa dynasty (infobox Established 1354, Capital Nêdong; "superseded Sakya in the period 1354-1358"; "wielded power over Central Tibet").
- /ledger/15-18 (Dzungar 1717-1720): confirmed, Dzungar conquest of Tibet (25 August, 8 October, 2 December 1717; occupation "lasting from 1717 to 1720"; military government; the page does not define the occupation's extent).
- /ledger/40 and /ledger/35 (Tawang 1944, 1914, c3): confirmed, Tawang district. /ledger/12 (1681): the page dates only the monastery's founding, not Tawang coming under Tibet ("The Monyul kingdom was later absorbed into the control of neighbouring Bhutan and Tibet") - confidence lowered to 1 (applied).
- /ledger/5 (1612): the year is the sentence's own ("In 1612 and 1613, the Tsangpa ruler subjugated a number of local regimes in West Tibet: the Ngari Gyelpo, Lhopa and Changpa"), so the note's caveat about a heading can go; the region (Ngari around Tsaparang) is not on the page (see F3).
No fabricated or mis-dated event found.

## Area
Tibet (1912-1951) infobox: 1,221,600 km2, no year given. Cliopatria tibet_1912 = 910,375 km2 (ratio 1.34); tibet_1928 = 1,217,316 km2 (1.00), the shape the author's corrections use for 1918-1950. Acknowledged in /keyframe_review/38. Not a factor of two.

## Findings (blocking; for the author)

**F1. /keyframe_review/0-13/correction ("Central Tibet").** The gazetteer's "Central Tibet" is admin1 Xizang (the whole TAR): 4,342 cells, 1,098,092 km2, bbox 78.47-99.03 E. It holds 699 cells (about 176,800 km2) of the gazetteer's Kham (Chamdo) and 173 cells (about 43,800 km2) of the /ledger/14 Guge circle. The dossier's own text excludes both before 1642/1684: /certainty/0 "Kham and Amdo are outside the state until 1642"; /ledger/7 the Beri king held Kham in 1640-41; /ledger/14 "annexed Gu-ge to Tibet" in 1684. Fix: for 1354-1641 use `{"minus":[{"region":"Central Tibet"},{"region":"Kham"},{"lon":79.8,"lat":31.5,"km":150}]}` (or a proper U-Tsang spec), carry the Guge exclusion through /keyframe_review/14-19 (1642-1683) so /ledger/14 shows, and let the 1642 Kham gain (F2) bring Chamdo in.

**F2. /ledger/7 (1642 gain, counterpart Beri).** Its region (Tibet 1642 minus Central Tibet) resolves to 1,839 cells (465,083 km2), of which 1,278 cells (323,206 km2) lie in the gazetteer's Qinghai region: most of the "Kham" gain is Amdo/Kokonor. The page quoted in /ledger/8 (Khoshut Khanate) says "the Khoshut realm encompassed Kokonor and the Qaidam Basin while Tibet was a protectorate", and Gushi had "crushed the king of Beri" in the winter of 1640-41 (khoshut-khanate /ledger/3 books Kham as its own gain from Beri in 1641). So Beri is not the counterpart in 1642, and keyframes 14-25 (1642-1723) paint the Khoshut home realm as Tibet; khoshut-khanate paints Qinghai (from 1637) and Kham (from 1641) to 1717, so both dossiers hold about 465,000 km2 at once. Fix: restrict the 1642 gain to Kham (intersect with region Kham), counterpart khoshut-khanate (the 1642 grant of temporal power), and ask for the mirror in khoshut-khanate; cut Kokonor/Qaidam (the 921 northern cells, 89.9-100.4 E, 32.3-36.9 N) out of keyframes 14-25 and re-check /ledger/19 (if Kokonor was Khoshut, the 1724 Qinghai cut is a Khoshut loss, not Tibet's). If the orchestrator instead adopts the author's protectorate model (Tibet holds the plateau under a Khoshut suzerain), khoshut-khanate must turn its 1641/1642 gains into vassal events. Orchestrator decision needed either way (the author flagged the Central Tibet half of this, not the Kokonor half).

**F3. /ledger/5 (1612 gain, circle 80.0 E 31.3 N 250 km, "around Tsaparang").** (a) Its 368 cells inside Central Tibet are already in the keyframes from 1354 (F1), so the gain draws nothing. (b) The circle contains the whole /ledger/14 Guge circle, which is gained again in 1684 with no loss in between. (c) Ngari/Tsaparang is not the page's reading: the Tsangpa page names no Guge, calls Mangyul Gungthang (conquered 1619, not ledgered) "the West Tibetan kingdom", and says Karma Tenkyong "was threatened by Ladakh in the west"; /ledger/14 has Guge annexed only in 1684. Fix: re-region to western Tsang (Lato; the Ngari Gyelpo = Ngari Mangyul/Gungthang reading is the author's to confirm), add the 1619 Gungthang conquest, keep Guge out until 1684; if Guge was held by Ladakh before 1684, book the war's land accordingly (page to try below).

**F4. /ledger/32-37 with /keyframe_review/38-40 (western Kham 1912-1918).** tibet_1794 (= Tibet 1775) holds the 879 cells of Kham ∩ Tibet 1929; tibet_1912 (verdict ok) holds none of them. The ledger explains that drop only with an occupation_end (qing) and occupation_start (republic-of-china), which do not change the owner's shape, and in 1918 books both an occupation_end and a gain of the same land from republic-of-china (a gain with no earlier loss). Fix, one of: (a) occupation: adjust keyframes 38-40 to union `{"intersect":[{"region":"Kham"},{"cliopatria":"Tibet","year":1929}]}` and delete /ledger/36; (b) loss: make /ledger/33 a 1912 loss to republic-of-china and delete /ledger/37. Note the page also says "After the 1911 Revolution however, Chinese forces lost ground control beyond the city of Kangding".

## Minor
- /ledger/12: confidence 2 to 1 (applied).
- /ledger/35: add a wars[] entry (Simla Convention / McMahon Line dispute, 1914-1947, zone Tawang, no fighting) or say why none.
- /ledger/6 (c1): the Tsangpa page has "In 1641, the leader of the Khoshut Mongols of the Kokonor region, Güshi Khan, set out from his home area" - cite it and raise to 2.

## Thin (gap-filler)
- Rulers 1432-1565 (Rinpungpa period) and 1642-1951 (Dalai Lamas, regents).
- Who held Kham and Amdo 1354-1641 (author's gap).
- Tsangpa expansion: Tsangpa page names "spectacular successes in the east" (Dagpo, Phanyul, Neu) and Gungthang 1619; the state's reach 1565-1620 (Tsang only?) is drawn as all of Xizang.
- 1865: Tibet under Qing rule says the Dri River boundary "was used until 1865"; what changed (Nyarong) is not ledgered.
- /ledger/41-42 (1947, c1): what became of the Tawang claim after the Raj.
- 1930-32 Tibetan advance east of the Yangtze (Dege, Garze) not drawn; net zero by 1933.

## Cross-dossier
Neighbour dossiers that exist: khoshut-khanate, dzungar-khanate (checked; mismatches below), chagatai-khanate, durrani-empire, east-turkestan, eastern-moghulistan, first-toungoo-empire, konbaung-dynasty, moghulistan, mongol-khanate, shan-states, tumed (no events with tibet). Not yet written (groups not run, or ea-06-a in parallel): yuan-dynasty, qing-dynasty, nepal, british-raj, republic-of-china, people-s-republic-of-china, ming-dynasty and the rest.
- khoshut-khanate 1641 gain Kham from Beri vs tibet 1642 gain (Kham + Kokonor) from Beri: mismatch (F2).
- khoshut-khanate 1642-03 gain Central Tibet from tsangpa-dynasty (= tibet) vs tibet 1642 rename (no loss): mismatch, flagged by the author.
- khoshut-khanate 1717-12 loss Central Tibet to dzungar-khanate; dzungar-khanate 1717-12 gain from khoshut-khanate; tibet 1717-12 occupation_start by dzungar-khanate: mismatch of type (gain vs occupation) and owner; years agree.
- dzungar-khanate 1720 loss Central Tibet to qing-dynasty vs tibet 1720 occupation_end: mismatch of type; years agree.

## Gazetteer
"Central Tibet" carries alt names U-Tsang, Ü-Tsang, Tibet Autonomous Region and Xizang and resolves to the whole TAR (Chamdo and Ngari included). Every dossier that uses it for historical U-Tsang (tibet, khoshut-khanate, dzungar-khanate) inherits about 220,000 km2 of Chamdo and Ngari. A separate U-Tsang region is needed.
