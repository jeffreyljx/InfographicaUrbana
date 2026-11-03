# Review of batch ia-03-c (2026-10-19)

Reviewer: adversarial review, Phase B. Dossiers: eastern-moghulistan, western-moghulistan, tumed, khoshut-khanate. All four validate with --resolve, 0 errors, before and after the reviewer's small fixes; warnings are the intended empty corrections (region resolves to no cells) and counterpart slugs without dossiers (khalkha, tsangpa-dynasty).

Orchestrator adjustments applied: spot checks weighted to confidence-3 and land-moving events (4 per dossier, 5-6 for khoshut-khanate); small verified fixes made in place and marked applied; thin judged against the 5-page budget.

## eastern-moghulistan: fix

Fixes:
- `/ledger/2/counterpart` (applied by reviewer): The 1678 loss of Turfan-Hami named turpan-khanate, whose dossier ends with its dissolve into this state in 1570, so the counterpart could never carry the mirror gain. Evidence: turpan-khanate.json: start 1487, end 1570, /ledger/6 1570 dissolve cp eastern-moghulistan. Dzungar conquest of Altishahr infobox: belligerents 'Dzungar Khanate Turfan Khanate Kumul Khanate: Yarkent Khanate'; Abdu'l Rashid II is 'son of Baba Khan of Turfan'. Turpan Khanate page: 'embassies sent from Turpan to Beijing in 1647 and 1657'. Fix: Counterpart set to 'Turfan Khanate (Chagatayid khans of Turpan after 1570; no dossier)' and the note extended; confidence stays 1. Re-validated, 0 errors 0 warnings.

Thin (for a gap-filler):
- `/ledger/2`: When and to whom Yarkand lost Turpan and Hami between 1570 and 1678 (a Turfan line under Baba Khan by the 1670s; Turpan embassies of 1647 and 1657); the event is a confidence-1 bridging year. Page to try: https://en.wikipedia.org/wiki/Yarkent_Khanate
- `/keyframe_review/1`: The eastern frontier 1514-1570 (Aksu and Kucha, Mansur Khan's court in 1503 per turpan-khanate) is not dated; the Tarim outline is carried unchanged. Page to try: https://en.wikipedia.org/wiki/Mansur_Khan

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Sultan_Said_Khan: confirmed: 'In May 1514' took Kashgar, dethroning Mirza Abu Bakr; Yarkand, Khotan, Aksu and Uch Turpan joined him; capital Yarkand
- `/ledger/1` https://en.wikipedia.org/wiki/Turpan_Khanate: confirmed: 'In 1570, the Turpan Khanate was invaded by an army led by Abduraim Sultan' ... 'Turpan came under the control of the Yarkand Khanate'; Hami a dependency of Turfan from 1513 is on the Moghulistan page
- `/ledger/3` https://en.wikipedia.org/wiki/Dzungar_conquest_of_Altishahr: confirmed: 'Later the following year Galdan led 120,000 Dzungar cavalry into the Tarim basin, advancing through Aksu'; footnote 'The year 1680 seems to have been accepted by most authorities'
- `/ledger/4` https://en.wikipedia.org/wiki/Dzungar_conquest_of_Altishahr: confirmed: infobox 1678-1680, 'Altishahr (Tarim Basin) annexed Dzungar Khanate'; Abdu'l Rashid II made Galdan's vassal

Area: No area in the Yarkent Khanate or Moghulistan infoboxes (both opened by the reviewer); the dossier says so. Yarkent infobox 1514-1705, the dossier's 1680 end is explained. (Cliopatria max 938660 km2).

## western-moghulistan: thin

Fixes:
- `/identity/capitals/0` (applied by reviewer): Almaliq (80.88 E, 44.2 N) was the capital 1519-1565, but it lies in the Zhetysu cells the dossier itself loses to the Kazakhs in 1521, outside every Western Moghulistan shape from 1521. Evidence: shapes.csv: western-moghulistan_1521..1632 bbox 73.38-80.22 E, 38.55-42.89 N; /ledger/1 1521 loss of Zhetysu to kazakh-khanate. Fix: Capital ended in 1520 with a note; no page names a seat for 1521-1565 (gaps in capitals are allowed).
- `/wars/0/from` (applied by reviewer): The Kyrgyz revolt war began in 1510, nine years before this state's start (1519); wars must lie inside the life. Evidence: Moghulistan page: 'by 1510-11, they had effectively driven out the Moghuls' (the predecessor's war); dossier start 1519. Fix: 'from' set to 1519 with a note that the revolt began under moghulistan.

Thin (for a gap-filler):
- `/ledger/0`: The 1519 founding is Cliopatria's year at confidence 1: no page dates a Moghul polity in the Zhetysu and Tian Shan after the Kyrgyz expulsion of 1510-11 (Said Khan's governors of Moghulistan in the 1520s would be the evidence). Page to try: https://en.wikipedia.org/wiki/Mirza_Muhammad_Haidar_Dughlat
- `/ledger/1`: The 1521 loss of Zhetysu to the Kazakhs is Cliopatria's year and land at confidence 1; a page dating Qasim's or Tahir's hold on Zhetysu is needed. Page to try: https://en.wikipedia.org/wiki/Kasym_Khan
- `/keyframe_review/0`: Keyframes 1519-1546 are verdict ok although the dossier's own page says the Kyrgyz had driven the Moghuls out by 1510-11 and Said's 1526-27 attempt failed; the 'soft Moghul claim' needs a page or a verdict wrong. Page to try: https://en.wikipedia.org/wiki/Moghulistan

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Moghulistan: confirmed as stated: the page names Mahmud Khan 'the ruler of western Moghulistan in Tashkent' and 'The rest of western Moghulistan (the area of modern Kyrgyzstan) were gradually lost to Kyrgyz tribes', and dates no 1519 founding (confidence 1 is honest)
- `/ledger/2` https://en.wikipedia.org/wiki/Moghulistan: confirmed: 'Abdurashid Khan (1533-1565)' ... 'also fought for control of (western) Moghulistan against the Kirghiz-Kazakhs of the Great Horde'
- `/ledger/3` https://en.wikipedia.org/wiki/Moghulistan: confirmed: reign to 1565 and 'thereafter the Moghuls were largely restricted to possession of the Tarim Basin'
- `/ledger/4` https://en.wikipedia.org/wiki/Moghulistan: confirmed (same sentence); confidence 2 is right, the year is the reign end

Area: The Moghulistan infobox has no area (reviewer opened it); acknowledged in notes. (Cliopatria max 285072 km2).

## tumed: thin

Fixes:
- `/sources/5/note` (applied by reviewer): The Tsangpa source note said 'a Tsangpa ruler was abducted by the Tumed Mongols in 1623'; the page says an abbot allied to the Tsangpa was. Evidence: Tsangpa page: 'The abbot of the important Drigung Monastery in Ü, allied to the Tsangpa, was abducted by the Tumed Mongols in 1623'. Fix: Note corrected to the page's sentence.

Thin (for a gap-filler):
- `/keyframe_review/0`: The 1547-1581 shapes keep about 2 M km2 of Dzungaria, the Tian Shan and southern Siberia as Tumed with no page (marked unverified); the Tumed page has the Tumeds recapture Karakorum 'from the hands of the Oirats' in 1552, which puts the Oirats west of Karakorum. A page on Altan's western wars is needed to keep or cut the west. Page to try: https://en.wikipedia.org/wiki/Northern_Yuan_dynasty
- `/ledger/2`: The 1552 gain of Inner Mongolia and the Ordos is Cliopatria's year and land at confidence 1 (Altan led the whole Right Wing from 1542, so the year may be 1542-1547). Page to try: https://en.wikipedia.org/wiki/Northern_Yuan_dynasty
- `/ledger/3`: The 1582 loss of 7,369 cells to khalkha and /ledger/4 the loss of the rest to nobody rest on Altan's death date only (confidence 1). Page to try: https://en.wikipedia.org/wiki/Northern_Yuan_dynasty
- `/wars/2`: The war has a Hohhot zone but the ledger has no contest or occupation for Ligdan's Chahar hold on Hohhot c. 1627-1632: Ligdan page, 'Princes ruling the Sunid, Uzemchin, and Abaga moved northwest and allied with the Three Right Wing Tumens against Ligden' (1627), 'In 1631 Ligden ... successfully attacked the Khorchin and the Tümed', 'They destroyed 4,000 Chahar militias in Hohhot'; Hohhot page: razing of 1631. Page to try: https://en.wikipedia.org/wiki/Ligdan_Khan
- `/ledger`: Altan's Kokonor expeditions 1559-1578 (Qinghai is in the kept 1547-1581 shape without an event). Page to try: https://en.wikipedia.org/wiki/Sonam_Gyatso,_3rd_Dalai_Lama

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Altan_Khan_of_the_Tumed: confirmed: 'After Gün Bilig's death in 1542, Altan became the de facto leader of the whole of the Right Wing'; in 1547 'Altan forced Bodi Alagh's successor Darayisung Küdeng Khan to flee eastward'
- `/ledger/1` https://en.wikipedia.org/wiki/Altan_Khan_of_the_Tumed: confirmed: 'In 1552 Altan Khan gained control of the remains of Karakorum, the old Mongol capital' (no holder named); Tumed page: 'recaptured Karakorum from the hands of the Oirats', so counterpart khalkha is Cliopatria's accounting, as the note says
- `/ledger/3` https://en.wikipedia.org/wiki/Altan_Khan_of_the_Tumed: confirmed for the date: 'Altan Khan died on 13 January 1582'; no land on the page (confidence 1 is honest)
- `/ledger/5` https://en.wikipedia.org/wiki/Inner_Mongolia: confirmed: 'The Manchus gained far-reaching control of the Inner Mongolian tribes in 1635, when Ligden Khan's son surrendered'; the Tumed page has the submission 'in the early 17th century' (confidence 2 is right)

Area: No infobox on the Tumed or Altan Khan pages (reviewer opened both). The dossier cuts the realm from 2.6 M km2 to a 200 km Hohhot disc in 1582 at confidence 1; acknowledged in keyframe notes. (Cliopatria max 2616320 km2).

## khoshut-khanate: fix

Fixes:
- `/ledger/8/month` (applied by reviewer): The Dzungar contest_start was dated October 1717 (arrival at Lhasa) and the note said the first Dzungar ground was not dated, but the page dates the entry into Tibet in August. Evidence: Dzungar conquest of Tibet: 'On August 25th of 1717, the Dzungars passed through the Largin pass' and 'in the Summer of 1717, after the Dzungar arrival on Tibet'. Fix: Month changed from 10 to 8 and the note rewritten with both sentences; confidence stays 2; order unchanged.
- `/wars/0/from` (applied by reviewer): The Qinghai war began in 1636, before the state's start (1637); wars must lie inside the life. Evidence: Güshi Khan page: 'Güshi marched into Qinghai with 10,000 Oirat troops in 1636'; dossier start 1637 (first land held). Fix: 'from' set to 1637 with a note keeping the 1636 march.

Thin (for a gap-filler):
- `/ledger`: No vassal_start for the Qing nominal suzerainty of 1654 ('Güshi Khan accepted the nominal suzerainty of the Qing dynasty in 1654', Khoshut page, verified); the author leaves it to qing-dynasty. Convention question (as raised in review ia-03-a): whether the vassal's ledger mirrors it. Page to try: https://en.wikipedia.org/wiki/Khoshut_Khanate
- `/ledger/11`: Kham and Qinghai are dissolved with Central Tibet in December 1717, but the Qinghai Khoshuts (Lobzang Danjin) held on to the 1723-24 rising; the pages tried did not load. Page to try: https://en.wikipedia.org/wiki/Qinghai
- `/identity`: No ruler strip: the Khoshut page's table has Lhazang 1697-1717 against '1703' in its text; Dayan Khan's reign undated. Page to try: https://en.wikipedia.org/wiki/Lha-bzang_Khan

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/G%C3%BCshi_Khan: confirmed: 'The campaign was prepared in 1639 ... In June of that year, Güshi moved against Beri and subjugated most of Donyo Dorje's subjects'
- `/ledger/3` https://en.wikipedia.org/wiki/Khoshut_Khanate: confirmed: 'In the winter of 1640-1641, Güshi crushed the king of Beri, Donyo Dorje'; Güshi page 'Having subdued Kham entirely by 1641'
- `/ledger/6` https://en.wikipedia.org/wiki/Tsangpa: confirmed: 'The Tsangpa stronghold, Shigatse, was captured after a long and bloody siege in March 1642'; 'dominated large parts of Tibet from 1565 to 1642'
- `/ledger/7` https://en.wikipedia.org/wiki/Khoshut_Khanate: confirmed: 'On 13 April 1642, the 5th Dalai Lama proclaimed Güshi the khan of Tibet'
- `/ledger/10` https://en.wikipedia.org/wiki/Dzungar_conquest_of_Tibet: confirmed: 'on November 30th of 1717, Lhasa was attacked'; 'Later on December 2nd of 1717, Potala Palace was attacked, subsequently leading to the death of Lha-bzang Khan and the collapse of the Khoshut Khanate'
- `/ledger/8` https://en.wikipedia.org/wiki/Dzungar_conquest_of_Tibet: mis-dated (month): entry 25 August 1717, not October; fixed

Area: No area or capital in the Khoshut Khanate infobox (reviewer opened it: established 1642, disestablished 1717, predecessor Tsangpa, successor Dzungar Khanate); all nine Cliopatria shapes are marked wrong and corrected to Ü-Tsang, Kham and Qinghai. (Cliopatria max 291729 km2).

## Cross-dossier matrix

- eastern-moghulistan 1514 found cp=moghulistan -> moghulistan 1514 loss: matched. Tarim Basin both sides.
- eastern-moghulistan 1570 gain cp=turpan-khanate -> turpan-khanate 1570 dissolve: matched. turpan-khanate dissolves into eastern-moghulistan.
- eastern-moghulistan 1678 loss cp=Turfan Khanate (no dossier) -> no mirror: exception. Was turpan-khanate, whose life ends 1570 (mismatch); reviewer changed the counterpart to a named non-dossier Turfan Khanate. Route to ia-03 (turpan-khanate owner) if the project wants the Turfan line 1570s-1680 drawn.
- eastern-moghulistan 1680 loss cp=dzungar-khanate -> no mirror: exception. dzungar-khanate not written yet (another ia-03 part); it should gain the Tarim Basin in 1680 (contest 1680) and may carry the nominal Yarkent khans 1680-1705 as vassals.
- western-moghulistan 1519 found cp=moghulistan -> moghulistan 1518 dissolve: matched. Within one year; both confidence 1.
- western-moghulistan 1521 loss cp=kazakh-khanate -> kazakh-khanate 1521 gain: matched. Same Cliopatria delta (475/474 cells), both confidence 1.
- western-moghulistan 1533 contest_start cp=kazakh-khanate -> kazakh-khanate 1533 contest_start: matched. Semirechye both sides; contest_end 1565 also matched.
- western-moghulistan 1565 dissolve cp=None -> no mirror: exception. Successor kyrgyz-khanate has no dossier; listed for ia-03-x.
- tumed 1547 found cp=mongol-khanate -> mongol-khanate 1547 loss: matched. Same intersect region both sides.
- tumed 1552 gain cp=khalkha -> no mirror: exception. Two gains (Karakorum c2, Inner Mongolia c1); khalkha has no dossier, listed for ia-03-x; the Tumed page says Karakorum was taken from the Oirats (no state row in 1552).
- tumed 1582 loss cp=khalkha -> no mirror: exception. khalkha has no dossier; the parallel 1582 loss to nobody needs no mirror.
- tumed 1635 loss cp=later-jin-dynasty -> no mirror: exception. later-jin-dynasty (ea-08) not written yet; mongol-khanate loses the Chahar lands to the same counterpart in Feb 1635, consistent. ea-08 should add the Tumed alliance/submission 1632-1635 and the Ming (ea-07) the 1570-71 tributary relation.
- khoshut-khanate 1637 found cp=Choghtu Khong Tayiji -> no mirror: exception. No dossier; listed by the author.
- khoshut-khanate 1641 gain cp=Beri (Donyo Dorje) -> no mirror: exception. No dossier (minor, ea-06); contest 1639-1641 likewise.
- khoshut-khanate 1642 gain cp=tsangpa-dynasty -> no mirror: exception. tsangpa-dynasty has no dossier (ea-06 not run); contest 1641-1642 likewise. Cliopatria's Tibet row overlaps the Khoshut land 1642-1717; ea-06 must settle it.
- khoshut-khanate 1717 loss cp=dzungar-khanate -> no mirror: exception. dzungar-khanate not written yet; it should gain Central Tibet in Dec 1717 (contest from Aug 1717 after the reviewer's fix) and lose it in 1720.
- khoshut-khanate 1654 vassal_start cp=qing-dynasty -> no mirror: missing. Neither side records the 1654 nominal Qing suzerainty; qing-dynasty (ea-08) not written yet. Convention question for the orchestrator.

## Counterparts needing dossiers

- Khalkha khanates (Cliopatria 'Golden Horde' rows 1547-1691) (khalkha, 1547-1691)
- Tsangpa dynasty (tsangpa-dynasty, 1565-1642)
- Kyrgyz khanate / Kyrgyz tribes of the Tian Shan (kyrgyz-khanate, 1514-1685)
- Kingdom of Beri (Donyo Dorje, Kham) (kingdom-of-beri, 1639-1641)
- Choghtu Khong Tayiji's Kokonor Mongols (choghtu-khong-tayiji, 1635-1637)
- Dughlat emirate of Kashgar (Mirza Abu Bakr) (dughlat-emirate, 1465-1514)
- Turfan Khanate after 1570 (Baba Khan's line; or extend turpan-khanate) (turfan-khanate, 1570-1680)

## Problems and routing

- No page failed for the reviewer (opened 2026-10-19: Sultan Said Khan, Turpan Khanate, Dzungar conquest of Altishahr, Yarkent Khanate, Moghulistan, Altan Khan of the Tumed, Tumed, Inner Mongolia, Ligdan Khan, Khoshut Khanate, Tsangpa, Dzungar conquest of Tibet, Güshi Khan).
- Reviewer applied fixes in place (orchestrator adjustment): eastern-moghulistan /ledger/2 counterpart; western-moghulistan /identity/capitals/0 to, /wars/0 from; tumed /sources/5 note; khoshut-khanate /ledger/8 month and note, /wars/0 from. All four re-validate with --resolve, 0 errors, warnings unchanged (empty corrections and counterpart slugs without dossiers).
- Neighbour dossiers present and cross-checked: kazakh-khanate, mongol-khanate, moghulistan, turpan-khanate, eastern-chagatai-khanate (golden-horde, khanate-of-bukhara, crimean-khanate, astrakhan-khanate exist but hold no event with these states). Not written yet (groups not run): tibet, ming-dynasty, qing-dynasty, later-jin-dynasty, dzungar-khanate, oirat-confederation, kalmyk-khanate, southern-ming, ottoman-empire, mughal-empire, tsardom-of-russia, don-cossacks, kashmiri-sultanate.
- small-horde was not written by the author: nogai-horde (ia-02-d) holds the Small Horde row; consistent with review ia-03-a (counterpart small-horde will not exist).
- Route to ea-06: Cliopatria's Tibet row overlaps the Khoshut Khanate land 1642-1717; tsangpa-dynasty and Beri need dossiers. Route to ea-08: qing-dynasty vassal_start khoshut-khanate 1654 and later-jin-dynasty Tumed 1632-1635. Route to ia-03 (dzungar-khanate): Tarim gain 1680, Central Tibet Dec 1717 (contest from Aug 1717).
- Western Moghulistan and Tumed are thin by design within their 5-page budgets: verdict thin, not fail.
