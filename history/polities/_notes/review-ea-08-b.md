# Review of batch ea-08-b (qing-dynasty)

Reviewer, 2026-10-25. Verdict: **thin**. No blocking finding remains: the validator passes (0 errors, 1 warning: bogd-khanate has no dossier), all six confidence-3 spot checks were confirmed on their pages, and the infobox areas are within a factor of two and acknowledged in keyframe notes. The reviewer applied four small fixes (below, applied). What remains is for a gap-filler or the author: missing events that leave three keyframe changes unexplained (Gansu 1864, Guangzhou 1648, Guilin 1652), missing mirror events for neighbours that now exist (Liaodong 1895, Weihaiwei 1898), and counterpart disagreements with ia-03 dossiers (Khalkha, Khoshut, Kumul).

## What was tried and held
- Validator with --resolve: valid; the region names resolve (stand-ins listed under gazetteer names).
- Years: ledger sorted, found 1644-06 and dissolve 1912-02 at start and end; capitals and certainty cover the life. Rulers: Kangxi to 1722 and Yongzheng from 1723 leave a one-year gap; the page gives 'r. 1723-1735', so it was left; 1850 Daoguang/Xianfeng is a flagged bridge.
- Areas (Qing dynasty infobox, read on the page): 1700 8.8 M vs 8.89 M (1.01); 1790 14.7 M vs 11.33 M (0.77); 1860 13.4 M vs 10.50 M (0.78); 1908 11.35 M vs 11.10 M (0.98). The author's figures match.
- Keyframes: the 1645-1652, 1673-1682, 1757-1759, 1856, 1865, 1881 and 1900-1904 corrections agree with the ledger. The 1794 Tibet keyframe follows the worked example's pattern (shape as drawn, part as vassal tint).
- Known problems: the author flagged Cliopatria's 1673-82 'Southern Ming' rows (Three Feudatories), the Tibet overlap and the Later Jin hand-over.

## Spot checks
- /ledger/42: confirmed (https://en.wikipedia.org/wiki/Qing_dynasty)
- /ledger/24: confirmed (https://en.wikipedia.org/wiki/Revolt_of_the_Three_Feudatories)
- /ledger/27: confirmed (https://en.wikipedia.org/wiki/Treaty_of_Nerchinsk)
- /ledger/54: confirmed (https://en.wikipedia.org/wiki/Amur_Annexation)
- /ledger/35: confirmed (https://en.wikipedia.org/wiki/Tibet_under_Qing_rule)
- /ledger/59: confirmed (https://en.wikipedia.org/wiki/Dungan_Revolt_(1862%E2%80%931877))
- /ledger/41: confirmed (1757 is on the page; disagrees with the Kumul Khanate page's 1696) (https://en.wikipedia.org/wiki/Qing_dynasty)
- /ledger/46: confirmed (https://en.wikipedia.org/wiki/Qing_dynasty)
- /ledger/17: confirmed (the page's 1674 sentence is garbled but names Geng Jingzhong in Fujian) (https://en.wikipedia.org/wiki/Revolt_of_the_Three_Feudatories)
- /ledger/71: mis-dated (1877 for August 1876, confidence 1); fixed by reviewer (https://en.wikipedia.org/wiki/Qing_reconquest_of_Xinjiang)

## Findings
- **/ledger/71** (applied by reviewer): The recovery of Urumqi and Dzungaria was dated 1877 at confidence 1 (the year of the shape) with a free-text counterpart. Evidence: Qing reconquest of Xinjiang page: 'In August 1876, the Qing appeared at Urumchi'; footnote 'on 18 August, Urumchi fell without resistance'; 'On 6 November it surrendered' (Manas). The dungan-revolt dossier has the Dungan state losing Urumqi in 1876-08. Fix: Year 1876, month 8, confidence 2, counterpart dungan-revolt, source https://en.wikipedia.org/wiki/Qing_reconquest_of_Xinjiang (added to sources).
- **/ledger/58, /ledger/59, /ledger/62, /ledger/65, /ledger/67, /ledger/68, /ledger/70** (applied by reviewer): Dungan Revolt events named free-text counterparts ('Hui rebels of Shaanxi/Gansu', 'Dungan rebels of Urumqi') although a dossier dungan-revolt now exists. Evidence: history/polities/dungan-revolt.json (rebel, 1862-1876) carries the mirror events: 1863-10 gain Ningxia, 1864-10 gain Urumqi, 1869 loss, 1871-01 loss, 1872 losses, 1873-10 loss, all with counterpart qing-dynasty. Fix: Counterpart dungan-revolt on all seven (the contest pair 58/65 changed together).
- **/ledger/41, /ledger/87** (applied by reviewer): Kumul vassal pair named the free-text counterpart 'Kumul Khanate' although kumul-khanate.json exists. Evidence: kumul-khanate dossier: vassal_start qing-dynasty 1696, vassal_end qing-dynasty 1912. Fix: Counterpart kumul-khanate on both.
- **/ledger/77, /ledger/78, /ledger/80, /ledger/88, /ledger/89, /ledger/91** (applied by reviewer): The 1898 leases named the metropoles (german-empire, russian-empire, french-indochina) as occupiers although the leased-territory dossiers exist; /ledger/89 kept the Russian lease of Liaodong until 1912. Evidence: Kwantung Leased Territory page: 'In March 1898 Russia formally leased the region'; 'Under the Portsmouth Treaty (1905) resulting from the Russo-Japanese War, Japan replaced Russia as leaseholder.' kiautschou-bay-leased-territory (found 1898-03), kwantung-leased-territory (found 1898-03, rename 1905-09) and guangzhouwan (found 1898-05) all name qing-dynasty as predecessor. Fix: Counterparts kiautschou-bay-leased-territory, kwantung-leased-territory, guangzhouwan; /ledger/89 note rewritten (the lease outlives the dynasty; Japan lessee from 1905, carried by the Kwantung dossier), source https://en.wikipedia.org/wiki/Kwantung_Leased_Territory (added).
- **/ledger/29, /ledger/30** (not applied): vassal_start/vassal_end khalkha-khanates 1691-1696 names a state whose dossier ended in 1688. Evidence: khalkha-khanates.json: 1688 dissolve, counterpart dzungar-khanate; no vassal events; its successor note says the Khalkha leaders 'returned to Outer Mongolia as Qing vassals' after Galdan fell. The Qing ledger itself has Outer Mongolia contested with the Dzungars 1690-1696 and gained from dzungar-khanate in 1696. Fix: Either drop the 1691-1696 vassal pair (the land is Dzungar-held and contested in this ledger) or ask ia-03 to extend khalkha-khanates to 1691 with the Dolon Nor vassal_start; keep both ledgers saying the same thing.
- **/ledger/34** (not applied): The 1724 gain of Qinghai names khoshut-khanate, whose dossier dissolves in December 1717. Evidence: khoshut-khanate.json /ledger/11: 'Disestablished: 1717' and 'The Khoshuts of Qinghai under Lobzang Danjin are outside the pages opened'. The Tibet under Qing rule page says only 'The Qing made the region of Amdo into the province of Qinghai in 1724' and names no holder. Fix: Use a free-text counterpart such as 'Khoshut Mongols of Qinghai (Lobzang Danjin)' and say in the note that the holder is the researcher's reading, or find a page that names the 1723-24 rising.
- **/ledger/41** (not applied): Kumul becomes a Qing vassal in 1757 here and in 1696 in the kumul-khanate dossier, 61 years apart. Evidence: The Qing dynasty page does say 'incorporated into the Qing dynasty as a vassal after helping Qing defeat the Zunghars in 1757' (confirmed); the kumul-khanate dossier cites the Kumul Khanate infobox 'Banner of the Qing dynasty (1696-1912)'. Two pages disagree; not a fabrication. Fix: Move the vassal_start to 1696 citing https://en.wikipedia.org/wiki/Kumul_Khanate, or keep 1757 and say in the note that the Kumul page dates the submission to 1696.
- **/keyframe_review/58 (qing-dynasty_1864), /ledger/68, /ledger/70** (not applied): Gansu -69 percent in the 1864 shape has no loss event: the ledger loses only Ningxia (1863) and Xinjiang, yet regains Xining (1872) and the Hexi Corridor (1873) it never lost. Evidence: The ledger's own note at /ledger/59 cites the Dungan Revolt page on Ma Zhan'ao (Hezhou), Ma Guiyuan (Xining) and Ma Wenlu (Suzhou) from 1862; dungan-revolt.json has 1862 gains of Jinjibao, Hezhou, Xining and Suzhou, 1863-01 Guyuan, 1863-08 Pingliang, 1864-02 Weiyuan, all from qing-dynasty. Fix: Add 1862-1864 loss events of Hezhou/Linxia, Xining, the Hexi Corridor (Suzhou), Guyuan and Pingliang to dungan-revolt, source the Dungan Revolt page.
- **/keyframe_review/3 to /keyframe_review/5, /ledger/10, /ledger/11, /ledger/12** (not applied): Guangzhou is in the 1647 keyframe and gone from the 1648 one with no loss event; the 1649 keyframe holds all Guangdong although /ledger/11 has Guangzhou fall only in November 1650; /ledger/12 loses Guilin in 1652 although no keyframe or gain ever gave Guilin to the Qing. Evidence: Keyframe corrections 3 (includes Guangzhou radius 150) and 4 (does not); /ledger/11 note: 'the city had been lost since the January 1647 capture; the page does not say when'; keyframe 5 note: 'Guangxi stays out'. Fix: Add the 1648 loss of Guangdong and Jiangxi (Li Chengdong's and Jin Shenghuan's defections) to southern-ming, at confidence 1 if the Southern Ming page is silent; hold Guangzhou out of the 1649 keyframe until 1650-11; add the Qing capture of Guilin (1650) or drop the 1652 loss.
- **/ledger (1895)** (not applied): The Liaodong cession of April 1895 and its return in November 1895 are missing. Evidence: empire-of-japan.json /ledger/19 (1895-04 gain qing-dynasty, Liaodong tip, 19 cells) and /ledger/20 (1895-11 loss qing-dynasty, Triple Intervention); the First Sino-Japanese War page the author opened names Liaodong. Fix: Add 1895-04 loss and 1895-11 gain of the Liaodong tip with counterpart empire-of-japan.
- **/ledger (1898)** (not applied): The British lease of Weihaiwei (1898) is missing although a weihaiwei dossier exists. Evidence: weihaiwei.json: found 1898-07, predecessor qing-dynasty, 'ruled by the British from 1 July 1898 to 1930 under a lease agreement'. The Qing dynasty page does not name Weihaiwei (confirmed), so the author could not source it. Fix: Add occupation_start weihaiwei 1898-07 and occupation_end weihaiwei 1912-02 (place Weihai), source https://en.wikipedia.org/wiki/Weihaiwei.
- **/ledger/66, /ledger/73** (not applied): Russia's 1871 occupation of Ili is drawn as an occupation of Qing land although the ledger lost the Ili Valley to ili-sultanate in 1866 and records no regain; the 1876 Dzungaria gain region also overlaps the Russian-held Ili Valley. Evidence: /ledger/64 (1866-03 loss ili-sultanate, Yining radius 150), /ledger/66 (1871 occupation_start russian-empire, same region), /ledger/71 region 'Dzungaria'. Fix: Either model 1881 as a gain from russian-empire (Treaty of Saint Petersburg) and drop the occupation pair, or keep the pair and say why; draw the 1876 gain as Dzungaria minus the Ili Valley.
- **/ledger/15 to /ledger/23** (not applied): The Three Feudatories' revolt (1673-1681) is booked against southern-ming, a state that ended in 1662. Evidence: Revolt of the Three Feudatories page: Wu Sangui, Geng Jingzhong and Shang Zhixin; 'Wu ... proclaimed himself emperor of the Great Zhou Dynasty'. The author flagged that Cliopatria's 'Southern Ming' rows of 1673-82 are this revolt (problems[0]). Fix: Keep southern-ming only if ea-07's southern-ming dossier takes Cliopatria's 1673-1682 rows as the revolt; otherwise a rebel dossier (suggested slug wu-zhou) becomes the counterpart. Orchestrator to decide with ea-07.

## Thin: for a gap-filler
- /ledger/1: Joseon tributary relation restated at 1644 at confidence 1; the joseon dossier has no vassal events at all (try https://en.wikipedia.org/wiki/Qing_invasion_of_Joseon)
- /ledger/9: Date of the Qing hold on Sichuan (confidence 1, year from the 1648 shape) (try https://en.wikipedia.org/wiki/Zhang_Xianzhong)
- /ledger/13: Dates for Guizhou and Guangxi 1658-59 (confidence 1) (try https://en.wikipedia.org/wiki/Li_Dingguo)
- /ledger/16: Year of Wu Sangui's hold on Hunan and Sichuan (confidence 1) (try https://en.wikipedia.org/wiki/Wu_Sangui)
- /ledger/22: Recovery dates of Fujian and Guangdong (Geng Jingzhong's and Shang Zhixin's surrenders; confidence 1, bridged to 1680) (try https://en.wikipedia.org/wiki/Geng_Jingzhong)
- /ledger/45, /ledger/74: Nguyen tributary relation 1803-1885 (start at confidence 1); the nguyen-dynasty dossier has no vassal events with the Qing (try https://en.wikipedia.org/wiki/Gia_Long)
- /ledger/52: Kowloon cession 1860 (confidence 1, page silent) (try https://en.wikipedia.org/wiki/Convention_of_Peking)
- /ledger/66: Russian occupation of Ili 1871 (confidence 1) (try https://en.wikipedia.org/wiki/Treaty_of_Saint_Petersburg_(1881))
- /ledger/82: End of the Russian occupation of Manchuria 1905 (confidence 1) (try https://en.wikipedia.org/wiki/Treaty_of_Portsmouth)
- /ledger/84: Outer Mongolia's declaration of December 1911 (confidence 1) (try https://en.wikipedia.org/wiki/Mongolian_Revolution_of_1911)
- /keyframe_review/50 (qing-dynasty_1848): -714 cells on the north-western steppe (43-50 N, 74-87 E) unexplained; the Tarbagatai cession of 1864 is the likely treaty (try https://en.wikipedia.org/wiki/Treaty_of_Tarbagatai)
- /keyframe_review/45 (qing-dynasty_1822): -611 cells on the western edge unexplained (Kokand frontier?) (try https://en.wikipedia.org/wiki/Khanate_of_Kokand)
- /ledger (1663-1680): Tungning's coastal holdings: kingdom-of-tungning has 1663-11 loss, 1674 and 1675 gains, 1677-03/04 losses, 1677-08 gain, 1680-04 loss, all with qing-dynasty; no mirror here (try https://en.wikipedia.org/wiki/Kingdom_of_Tungning)
- /ledger (1856, 1860): Taiping loss of Wuchang 1856-12 and the Panthay gain of 1860 (both neighbour events with qing-dynasty) have no mirror (try https://en.wikipedia.org/wiki/Taiping_Rebellion)
- /ledger (1905): Zhao Erfeng's Kham campaign: tibet.json has 1905 occupation_start qing-dynasty; the Tibet under Qing rule page says 'Zhao was sent in either 1905 or 1908' (try https://en.wikipedia.org/wiki/Zhao_Erfeng)
- /wars: Sino-Burmese War 1765-69 (konbaung-dynasty has a contest with qing-dynasty) and the 1788-89 campaign in Vietnam (tay-son-dynasty has a contest with qing-dynasty) are not in wars (try https://en.wikipedia.org/wiki/Sino-Burmese_War)
- /ledger (1887): Macau's cession to Portugal 1887 (portuguese-colonies not written yet) (try https://en.wikipedia.org/wiki/Sino-Portuguese_Treaty_of_Peking)

## Cross-dossier matrix

| Qing event | counterpart | mirror | status | note |
| --- | --- | --- | --- | --- |
| 1644 vassal_start | joseon | joseon 1637 contest_end | missing | joseon has only the 1637 contest_end ('becomes a Qing tributary'); no vassal_start/vassal_end with later-jin-dynasty or qing-dynasty; jk-02 to add 1637 and 1895 |
| 1644 gain | Shun regime of Li Zicheng | - | exception | no dossier; listed in counterparts_needing_dossiers |
| 1645 gain | southern-ming | - | exception | 1645-1659 gains (ledger 4-8, 10, 11, 13, 14) and the 1652 loss: southern-ming (ea-07) not written yet |
| 1648 gain | Zhang Xianzhong's Xi regime and Ming loyalists in Sichuan | - | exception | no dossier; listed |
| 1673 loss | southern-ming | - | exception | 1673-1681 Three Feudatories events (ledger 15-23): southern-ming not written; counterpart naming to settle with ea-07 |
| 1683 gain | kingdom-of-tungning | kingdom-of-tungning 1683 loss | matched | tungning 1683-07 loss and 1683-09 dissolve to qing-dynasty; but tungning's 1663-1680 coastal events with qing-dynasty have no mirror here |
| 1689 gain | tsardom-of-russia | - | exception | tsardom-of-russia owned by eu-16, not run |
| 1691 vassal_start | khalkha-khanates | khalkha-khanates 1688 dissolve | mismatch | khalkha dossier ends 1688 (dissolve to dzungar-khanate) and has no vassal events; Qing pair 1691-1696 |
| 1696 gain | dzungar-khanate | dzungar-khanate 1696 loss | matched | dzungar 1696 and 1696-06 losses |
| 1720 vassal_start | tibet | tibet 1720 occupation_end | missing | tibet has no vassal_start/vassal_end with qing-dynasty (1720 occupation_end dzungar only; 1912-08 occupation_end qing); dzungar-khanate has a 1720 loss to qing-dynasty (Tibet) that this ledger draws as the Tibet protectorate, not a gain |
| 1724 gain | khoshut-khanate | khoshut-khanate 1717 dissolve | mismatch | khoshut dossier dissolves 1717-12; the Qinghai Khoshuts are outside it |
| 1726 gain | tibet | tibet 1727 loss | matched | eastern Kham to Sichuan |
| 1757 gain | dzungar-khanate | dzungar-khanate 1757 loss | matched | also dissolve 1757 |
| 1757 vassal_start | kumul-khanate | kumul-khanate 1696 vassal_start | mismatch | 61 years apart; Qing dynasty page 1757 vs Kumul Khanate infobox 1696; counterpart slug fixed by reviewer |
| 1759 gain | Khojas of Altishahr (Tarim Basin) | - | exception | no dossier; listed |
| 1803 vassal_start | nguyen-dynasty | - | missing | nguyen-dynasty has no vassal events with qing-dynasty (1803-1885); se-01 |
| 1842 loss | british-colonial-empire | - | exception | eu-11 not run (also 1860 Kowloon and the 1898 New Territories) |
| 1853 loss | taiping-heavenly-kingdom | taiping-heavenly-kingdom 1853 gain | matched | also 1852-12 and 1853-02 gains; Taiping's 1856-12 loss (Wuchang) has no mirror here |
| 1856 loss | panthay-rebellion | panthay-rebellion 1856 found | matched | panthay's 1860 gain from qing-dynasty has no mirror here |
| 1858 gain | taiping-heavenly-kingdom | taiping-heavenly-kingdom 1858 loss | matched | 1858-05 and 1858-09 |
| 1860 loss | taiping-heavenly-kingdom | taiping-heavenly-kingdom 1860 gain | matched |  |
| 1860 loss | russian-empire | - | exception | eu-17 not run (also the 1871-1881 Ili and 1900-1905 Manchuria occupations) |
| 1861 gain | taiping-heavenly-kingdom | taiping-heavenly-kingdom 1861 loss | matched | Anqing; 1861-12 Zhejiang loss and 1862-05 Ningbo gain also matched |
| 1863 loss | dungan-revolt | dungan-revolt 1863 gain | matched | Ningxia 1863-10; dungan's 1862-1864 gains in Gansu (Jinjibao, Hezhou, Xining, Suzhou, Guyuan, Pingliang, Weiyuan) have no mirror here |
| 1864 loss | yettishar | yettishar 1864 found | matched | yettishar found 1864-11 from qing-dynasty; the 1865 Kashgar loss falls under it |
| 1864 gain | taiping-heavenly-kingdom | taiping-heavenly-kingdom 1864 dissolve | matched |  |
| 1864 loss | dungan-revolt | dungan-revolt 1864 gain | matched | Urumqi 1864-10 |
| 1866 loss | ili-sultanate | ili-sultanate 1866 gain | matched | 1866-01 and 1866-03 |
| 1869 contest_end | dungan-revolt | dungan-revolt 1869 loss | mismatch | Qing has a contest over Guanzhong, dungan has gains/loss in Shaanxi; types differ, land agrees |
| 1871 gain | dungan-revolt | dungan-revolt 1871 loss | matched | Jinjibao/Ningxia |
| 1872 gain | dungan-revolt | dungan-revolt 1872 loss | matched | Xining |
| 1873 gain | panthay-rebellion | panthay-rebellion 1872 dissolve | matched |  |
| 1873 gain | dungan-revolt | dungan-revolt 1873 loss | matched | Suzhou/Hexi |
| 1876 gain | dungan-revolt | dungan-revolt 1876 loss | matched | after the reviewer's fix (was 1877, free-text counterpart) |
| 1877 gain | yettishar | yettishar 1877 dissolve | matched |  |
| 1895 vassal_end | joseon | - | missing | see 1644 |
| 1895 loss | empire-of-japan | empire-of-japan 1895 gain | matched | Taiwan and Penghu; Japan's 1895-04 Liaodong gain and 1895-11 Liaodong loss have no mirror here |
| 1898 occupation_start | kiautschou-bay-leased-territory | kiautschou-bay-leased-territory 1898 found | mismatch | type differs (occupation here, found there); counterpart re-pointed by reviewer from german-empire |
| 1898 occupation_start | kwantung-leased-territory | kwantung-leased-territory 1898 found | mismatch | type differs; re-pointed from russian-empire, which wrongly kept the lease to 1912 |
| 1898 occupation_start | guangzhouwan | guangzhouwan 1898 found | mismatch | type differs; re-pointed from french-indochina; french-indochina also has 1900-01 gain from qing-dynasty (Guangzhouwan), which conflicts with the guangzhouwan dossier |
| 1898 occupation_start | british-colonial-empire | - | exception | New Territories; eu-11 not run |
| 1898 occupation_start | weihaiwei | weihaiwei 1898 found | missing | weihaiwei found 1898-07 with predecessor qing-dynasty; no Qing event |
| 1910 occupation_start | tibet | tibet 1910 occupation_start | matched | tibet also has 1905 occupation_start qing-dynasty (Kham) with no mirror here |
| 1911 split | bogd-khanate | - | exception | no dossier (validator warning); listed |
| 1912 occupation_end | tibet | tibet 1912 occupation_end | matched | tibet 1912-08 |
| 1912 vassal_end | tibet | - | missing | see 1720 |
| 1912 vassal_end | kumul-khanate | kumul-khanate 1912 vassal_end | matched |  |
| 1912 dissolve | republic-of-china | republic-of-china 1912 gain | matched | ROC found 1912-01, gain 1912-02 |

## Problems
- Spot checks ran past the budget of 6 because several events shared a page; all six formal confidence-3 checks confirmed.
- The author's counterparts kumul-khanate, dungan-revolt (both Dungan entries) and the four leased territories now exist as dossiers (written after the author's run); five of them were re-pointed by the reviewer, Weihaiwei is still missing from the Qing ledger.
- Neighbour dossiers not yet written (exceptions): southern-ming (ea-07), tsardom-of-russia (eu-16), russian-empire (eu-17), british-colonial-empire (eu-11), german-empire (eu-20), portuguese-colonies (sa-06), british-raj, british-empire, talpur-dynasty, kashmir-and-jammu.
- Mirror gaps on other groups' dossiers: joseon (jk-02) and nguyen-dynasty (se-01) lack the Qing tributary relation; tibet (ea-06) lacks vassal_start/vassal_end 1720/1912; french-indochina (se-03) 1900 Guangzhouwan gain conflicts with the guangzhouwan dossier; khalkha-khanates and khoshut-khanate (ia-03) end before the Qing events that name them.

## Counterparts still needing dossiers
- Shun regime of Li Zicheng (shun-dynasty, 1644-1645)
- Zhang Xianzhong's Xi regime (xi-dynasty, 1644-1647)
- Khojas of Altishahr (khojas-of-altishahr, 1680-1759)
- Bogd Khanate (bogd-khanate, 1911-1924)
- British Hong Kong (colony-of-hong-kong, 1842-1997)
- Wu Sangui's Zhou and the Three Feudatories (only if ea-07 does not own Cliopatria's 1673-82 'Southern Ming' rows) (wu-zhou, 1673-1681)

## Gazetteer names
- Ili Valley, Jiuquan, Jiaozhou Bay, Lüshun, New Territories, Kowloon peninsula, Guangzhouwan, Weihaiwei (stand-ins in use; see the author's notes for hints).
