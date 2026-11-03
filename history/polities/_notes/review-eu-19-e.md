# Review of batch eu-19-e (Kartli, Imereti, Kakheti, Abkhazia, Guria, Mingrelia)

Reviewer: adversarial review, 2026-10-31. Validator: all six dossiers valid (0 errors); warnings only for the gazetteer names Samurzakano and Kobuleti. None of the six Wikipedia articles gives an area, so the area check is internal (Cliopatria shape against shape). Neighbour dossiers read: kingdom-of-georgia, kingdom-of-kartli-kakheti, ottoman-empire, safavid-dynasty, afsharid-iran, russian-empire, shirvan, qara-qoyunlu, timurid-empire, byzantine-empire. Not yet written (exceptions): principality-of-svaneti, samtskhe-saatabago, khanates-of-the-caucasus, elisu-sultanate.

## Verdicts

| slug | verdict | in one line |
| --- | --- | --- |
| kingdom-of-kartli | thin | successor slug fixed by reviewer; the 1578/1579 halving and 1705/1706 doubling of area are unexplained (thin within a 1-2 page budget) |
| kingdom-of-kakheti | fix | fixed by reviewer: successor slug, and a misquote that reversed Nader's 1744 grants |
| kingdom-of-imereti | thin | confidence of the 1774 Mingrelia vassalage lowered by reviewer; overlordship of Svaneti missing; two confidence-1 events |
| principality-of-abkhazia | thin | five of seven events at confidence 1; Sukhumi lost twice with no regain |
| principality-of-guria | fail | FAIL: the 13 December 1614 renunciation of Adjara is on the page and missing from the ledger (the note misquotes it); keyframes keep inland Adjara throughout |
| principality-of-mingrelia | thin | honest but thin; vassalage over Guria and Lower Svaneti missing |

## kingdom-of-kartli: thin

Area: No area on the page (checked). Cliopatria Kartli outlines 27,616 (1468), 14,860 (1612), 31,452 (1706); the internal factor of two is acknowledged in /keyframe_review/2-3 but not resolved.

Findings:
- `/identity/successors/0/slug; /ledger/11/counterpart` (applied by the reviewer). Successor and 1762 dissolve counterpart were kingdom-of-georgia, which ends in 1478. Evidence: Kartli infobox: 'Succeeded by: Kingdom of Kartli-Kakheti'; kingdom-of-georgia /ledger/57 dissolves in 1478; kingdom-of-kartli-kakheti (eu-19-d, written 23:27) /ledger/0 founds in 1762 with counterpart kingdom-of-kartli. Fix: Changed to kingdom-of-kartli-kakheti with a bracketed reviewer note; re-validated (0 errors, 0 warnings).
- `/wars/0/zones` (for the author). Zones empty although ground changed hands: Tiflis was taken in August 1578 (the dossier's own /ledger/5). Evidence: Brief rule 10: empty zones only where no ground changed hands, and said so. Fix: Add a zone {place: Tbilisi, km: 25} for 1578, or say in the war note why it is left empty.
- `/keyframe_review/2 to /keyframe_review/5` (for the author). Area halves at 1578/1579 (27,810 km2 Georgia-row shape to the 14,860 km2 Kartli 1612 shape carried back) and doubles at 1705/1706 (14,860 to 31,452 km2); no ledger event explains either move. Evidence: shapes.csv bboxes: Georgia-row shapes (Kartli) reach 40.48N and 45.99E (Lori, Borchalo, the Kazakh-Shamshadil marches); Kartli 1612/1702 stop at 41.13N and 44.82E. The author flags it but leaves it unresolved; within a 1-2 page budget this is thin by design. Fix: Gap-filler: find who held the southern marches 1578/1612-1705 (Ottoman Tiflis/Childir eyalets, Safavid direct rule) and add the loss and gain, or adjust the 1579-1611 keyframe to the 1552 shape.

Gaps for a gap-filler:
- `/keyframe_review/2-5`: Which lands left Kartli between 1578 and 1612 and came back by 1706 (the southern marches), with years. Try https://en.wikipedia.org/wiki/Treaty_of_Nasuh_Pasha
- `/ledger (1522)`: Shah Ismail's occupation of Tbilisi: Kartli page 'In 1522/24, Safavid Shah Ismail invaded Kartli occupying Tbilisi to suppress David X's revolt'; not ledgered and no end date. Try https://en.wikipedia.org/wiki/David_X_of_Kartli
- `/ledger (1612-1705)`: Rostom's Persian-installed rule (1632-1658) and any direct Safavid holdings in Kartli. Try https://en.wikipedia.org/wiki/Rostom_of_Kartli

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Kingdom_of_Kartli: confirmed: 'Established: 1478'; 'tripartite division of the Kingdom of Georgia in 1478'
- `/ledger/1` https://en.wikipedia.org/wiki/Kingdom_of_Kartli: confirmed: 'In 1481, Constantine managed to subordinate Samtskhe'
- `/ledger/3` https://en.wikipedia.org/wiki/Kingdom_of_Kartli: confirmed: 'In 1513, the Kingdom of Kartli managed a short conquest of neighbouring Kakheti' (note quote is a paraphrase)
- `/ledger/8` https://en.wikipedia.org/wiki/Kingdom_of_Kartli: confirmed: 'On 12 June an Ottoman army bloodlessly took Tbilisi from Konstantine'
- `/ledger/9` https://en.wikipedia.org/wiki/Kingdom_of_Kartli: confirmed: 'In 1736 Turkey, at war with both Austria and Russia, gave up Kartli and Kakheti'
- `/ledger/10` https://en.wikipedia.org/wiki/Kingdom_of_Kartli: confirmed: 'After Teimuraz II's death in 1762, Irakli II assumed control over Kartli'; infobox 'Union of Kartli and Kakheti: 1762'

## kingdom-of-kakheti: fix

Area: No area on the page (checked); one 23,396 km2 outline throughout.

Findings:
- `/identity/successors/0/slug; /ledger/12/counterpart` (applied by the reviewer). Successor and 1762 dissolve counterpart were kingdom-of-georgia, which ends in 1478. Evidence: Kakheti infobox successors: 'Kingdom of Kartli-Kakheti; Elisu Sultanate'; kingdom-of-kartli-kakheti /ledger/1 merges kingdom-of-kakheti in 1762. Fix: Changed to kingdom-of-kartli-kakheti with a reviewer note; re-validated.
- `/ledger/10/note; /keyframe_review/6/note` (applied by the reviewer). Notes quoted '1744: Nader granted Kakheti to Teimuraz II and Kartli to Erekle II' and said one king ruled both kingdoms; the page says the reverse. Evidence: Kakheti page: 'In 1744, as a reward for their loyalty, Nader granted the kingship of Kartli to Teimuraz II' (and Kakheti to his son Erekle II; ruler list ends 'Heraclius II (last)', 1744-1762). The event itself (end of the occupations in 1744: 'From 1724 to 1744, Kakheti was subjected to the successive Ottoman and Iranian occupations') is on the page, so it is a misquote, not a fabricated event. Fix: Both notes rewritten from the page with a reviewer tag; re-validated.

Gaps for a gap-filler:
- `/ledger/9`: 1736 Afsharid occupation is a bridging reading (confidence 1); afsharid-iran /ledger/0 has a 1736 gain of 'Caucasian Iberia' from the Ottomans instead. Try https://en.wikipedia.org/wiki/Teimuraz_II_of_Kakheti
- `/identity/successors`: Elisu Sultanate successor has no land or year; Hereti/Saingilo transfers undated. Try https://en.wikipedia.org/wiki/Elisu_Sultanate

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Kingdom_of_Kakheti: confirmed: 'Established: 1466'; 'tripartite division of the Kingdom of Georgia in 1466'
- `/ledger/5` https://en.wikipedia.org/wiki/Kingdom_of_Kakheti: confirmed: 'From 1677 to 1703, the Bagrationi dynasty lost control of the Kakhetian throne' (the note's '1677-1703: Direct Safavid rule.' is a paraphrase in quotes)
- `/ledger/6` https://en.wikipedia.org/wiki/Kingdom_of_Kakheti: confirmed: 'reestablishing themselves in 1703'
- `/ledger/10` https://en.wikipedia.org/wiki/Kingdom_of_Kakheti: confirmed year and event; note misquoted the 1744 grants (fixed)
- `/ledger/11` https://en.wikipedia.org/wiki/Kingdom_of_Kakheti: confirmed: 'When Teimuraz died on January 8, 1762, Erekle succeeded him'

## kingdom-of-imereti: thin

Area: No area on the page (checked); outline 11.1-11.5k km2 throughout.

Findings:
- `/ledger/7/confidence` (applied by the reviewer). 1774 vassal_start of Mingrelia at confidence 2 although the page gives no year. Evidence: Solomon I page: 'Solomon was able to force his autonomist vassals, princes of Mingrelia and Guria, into submission' (no year); research brief: 2 only when the year is the page's. Fix: Lowered to 1 with a reviewer note; re-validated.
- `/ledger (1721-1810)` (for the author). Imereti's overlordship of Svaneti is not ledgered; the author's notes hand it to the Svaneti dossier, but the schema puts vassal_start/vassal_end in the suzerain's ledger (as the author did for Guria, Mingrelia, Abkhazia). Evidence: Principality of Svaneti infobox: 'subject of Kingdom of Imereti: 1463-1833'; Cliopatria's Svaneti row starts 1721. Fix: Add vassal_start principality-of-svaneti 1721 (region {cliopatria: Principality of Svaneti, year: 1721}, confidence 2) and vassal_end 1810-2 (annexation).

Gaps for a gap-filler:
- `/ledger/2`: 1463 Imeretian overlordship of Mingrelia is a bridging reading (confidence 1). Try https://en.wikipedia.org/wiki/Levan_I_Dadiani
- `/ledger/10`: 1810 end of Abkhazia's link to Imereti is bridging (confidence 1). Try https://en.wikipedia.org/wiki/Principality_of_Abkhazia
- `/identity/rulers`: No ruler strip; Racha, Lechkhumi and the Ottoman forts (Poti, Bagdati) undated. Try https://en.wikipedia.org/wiki/Kingdom_of_Imereti

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Kingdom_of_Imereti: confirmed: 'Established: 1463'; 'established in 1463 by a member of the house of Bagrationi'
- `/ledger/5` https://en.wikipedia.org/wiki/Solomon_I_of_Imereti: confirmed: 'Ottomans took Kutaisi in 1765'
- `/ledger/6` https://en.wikipedia.org/wiki/Solomon_I_of_Imereti: confirmed: 'In 1767, Solomon managed to stage a comeback, and freed Imereti of the Turks again'
- `/ledger/7` https://en.wikipedia.org/wiki/Solomon_I_of_Imereti: no year on page: confidence lowered to 1
- `/ledger/9` https://en.wikipedia.org/wiki/Principality_of_Guria: confirmed: infobox 'Client state of Kingdom of Imereti (1460s-1810)'
- `/ledger/11` https://en.wikipedia.org/wiki/Kingdom_of_Imereti: confirmed: infobox 'Russian Annexation: 20 February 1810'

## principality-of-abkhazia: thin

Area: No area on the page (checked).

Findings:
- `/ledger/5` (for the author). Sukhumi is lost twice: to the Ottomans in 1572 (/ledger/1) and to Russia in 1810, with no event returning it to the princes in between. Evidence: Abkhazia page: 'On July 2, 1810, the Russian Marines stormed Suhum-Kale' and installed Sefer-Bey in place of Aslan-Bey, i.e. the princes held the fort by 1810. Fix: Add a gain of Sukhumi from the Ottomans (confidence 1 unless a page dates it; Kelesh Ahmed-Bey's reign c. 1780-1808) or re-describe /ledger/5 as the loss of the fort from the prince's domain to a Russian garrison.
- `/ledger/3/region; /ledger/4/region` (for the author). The circle 41.9E 42.44N, 25 km, lies inland and contains Zugdidi (41.87E 42.51N), the Mingrelian capital, while the notes call it 'a southern coastal strip'. Evidence: Cliopatria bboxes: Abkhazia 1700 and 1788 reach 42.37N and 42.53E (south of the Enguri), 1727 stops at 42.50N; Mingrelia's capital is in /identity/capitals of principality-of-mingrelia at 41.87E 42.51N. Fix: Make the region match the text (e.g. the coast between the Enguri and Anaklia) or say in a keyframe note that Cliopatria's 1700/1788 Abkhazia shape overlaps the Zugdidi plain.

Gaps for a gap-filler:
- `/ledger/1`: 1570s Ottoman seizure of Tskhumi: year is Cliopatria's (confidence 1). Try https://en.wikipedia.org/wiki/Sukhumi
- `/ledger/3`: 1727 loss (-1,540 km2) unexplained, Ottoman counterpart a reading. Try https://en.wikipedia.org/wiki/Anaklia
- `/ledger/4`: 1788 gain (+1,570 km2) unexplained. Try https://en.wikipedia.org/wiki/History_of_Abkhazia
- `/ledger/5`: Whether Sukhum-Kale left the princes' domain after 2 July 1810 (confidence 1). Try https://en.wikipedia.org/wiki/History_of_Abkhazia
- `/identity/rulers`: 1465-1580 rulers missing. Try https://en.wikipedia.org/wiki/Principality_of_Abkhazia

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Principality_of_Abkhazia: confirmed: 'Established: 1463'; 'Chikhori in 1463 ... thus the Principality of Abkhazia was founded'
- `/ledger/1` https://en.wikipedia.org/wiki/Principality_of_Abkhazia: confirmed decade: 'the Ottoman navy occupied the fort of Tskhumi' (note says 'seized'; confidence 1 is right)
- `/ledger/2` https://en.wikipedia.org/wiki/Samurzakano: confirmed: 'in 1705 three brothers of the Abkhazian ruling family, surnamed Chachba', 'from the Ghalidzga to the R. Enguri'; page silent on Mingrelia, as the note says
- `/ledger/5` https://en.wikipedia.org/wiki/Principality_of_Abkhazia: confirmed: 'On July 2, 1810, the Russian Marines stormed Suhum-Kale'
- `/ledger/6` https://en.wikipedia.org/wiki/Principality_of_Abkhazia: confirmed: 'in November 1864, Prince Michael was forced to renounce his rights'; infobox 'Disestablished: 1864'

## principality-of-guria: fail

Area: No area on the page (checked).

Findings:
- `/ledger (1614-12, after /ledger/2)` (for the author). Missing loss: on 13 December 1614 Guria renounced Adjara to the Ottomans; the /ledger/2 note quotes the sentence as 'renounced his claims and agreed to pay tribute', dropping 'to the region', and the author's notes read it as tribute only. Evidence: Guria page: Mamia II 'managed to reconquer Adjara in 1609, but was eventually forced to renounce, on December 13, 1614, any claims to the region and to pay an annual tribute to the Sublime Porte.' Fix: Add 1614-12 loss, counterpart ottoman-empire, region Adjara (inland Adjara if the author keeps Batumi-Chakvi to 1723 on the strength of 'By 1723, the Gurieli had lost Batumi and Chakvi'), confidence 3 for the year; correct the /ledger/2 note quote.
- `/keyframe_review/4, 6, 7 and 9-13` (for the author). Ledger and keyframes disagree on Adjara: the ledger moves all of {admin1: Ajaria} (about 2,900 km2) in 1547 and 1609, but the Cliopatria shapes change by only about 360 km2 at the western coast and keep a southern edge at 41.457N (the Turkish border, i.e. inland Adjara) in every shape 1468-1829. Evidence: shapes.csv: Guria 1547 4,300 km2 vs 1516 4,659 km2, bbox min lat 41.4571 in all eleven shapes; russian-empire /ledger/115 takes Ajaria from the Ottomans only in 1878; the page has Adjara Ottoman from the 1540s to 1609 and again from 1614. Fix: Adjust the 1547-1608 and 1615-1829 keyframes to minus (inland) Adjara with a correction and text, or show from the outline that Adjara lies outside; make /ledger/1 and /ledger/2 regions the same land the keyframes move.

Gaps for a gap-filler:
- `/ledger/1`: 1540s annexation year is Cliopatria's 1547 (confidence 1). Try https://en.wikipedia.org/wiki/Principality_of_Guria
- `/ledger/4`: Kobuleti detachment year within 1768-1774 (confidence 1). Try https://en.wikipedia.org/wiki/Russo-Turkish_War_(1768%E2%80%931774)
- `/keyframe_review/2`: 1507-1515 shape reaching into Turkey unexplained. Try https://en.wikipedia.org/wiki/Principality_of_Guria

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Principality_of_Guria: confirmed decade: 'in the 1540s, a naval blockade of Guria and annexed its southern provinces of Adjara'
- `/ledger/2` https://en.wikipedia.org/wiki/Principality_of_Guria: event confirmed ('managed to reconquer Adjara in 1609'); note misquotes the 1614 renunciation
- `/ledger/3` https://en.wikipedia.org/wiki/Principality_of_Guria: confirmed: 'By 1723, the Gurieli had lost Batumi and Chakvi to the Ottomans'
- `/ledger/4` https://en.wikipedia.org/wiki/Principality_of_Guria: confirmed (war only): 'Kobuleti and the surrounding area were detached from Guria'
- `/ledger/5` https://en.wikipedia.org/wiki/Principality_of_Guria: confirmed: 'On September 2, 1829, the Russian authorities deposed David'

## principality-of-mingrelia: thin

Area: No area on the page (checked).

Gaps for a gap-filler:
- `/ledger/1`: 1700 loss of Samurzakano: year is Cliopatria's and the source does not name Mingrelia (confidence 1). Try https://en.wikipedia.org/wiki/Samurzakano
- `/ledger/3`: 1727 coast loss (-660 km2) with an Ottoman counterpart as a reading (confidence 1). Try https://en.wikipedia.org/wiki/Poti
- `/ledger (vassal)`: Mingrelia's overlordship of Guria is not ledgered: Guria page 'which eventually succumbed to the vassalage of the neighboring principality of Mingrelia' (undated, after 1614). Try https://en.wikipedia.org/wiki/Principality_of_Guria
- `/ledger (gain)`: Lower Svaneti 'was gradually subjugated by the Dadiani princes of Mingrelia' (Svaneti page, undated). Try https://en.wikipedia.org/wiki/Principality_of_Svaneti
- `/keyframe_review/1`: Ottoman relationship and the 1463 vs 1557 independence left unreconciled; the article has no history section. Try https://en.wikipedia.org/wiki/Levan_I_Dadiani

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Principality_of_Mingrelia: confirmed: infobox 'Established: 1463'; 'established as an independent Principality in 1557'
- `/ledger/1` https://en.wikipedia.org/wiki/Samurzakano: confirmed 1705 division; page silent on Mingrelia, as the note says
- `/ledger/2` https://en.wikipedia.org/wiki/Principality_of_Svaneti: confirmed: 'emerged as the eventual winners by the 1720s'; 1721 not on page (Cliopatria's year, confidence 2 right)
- `/ledger/4` https://en.wikipedia.org/wiki/Principality_of_Mingrelia: confirmed: 'Annexation by Imperial Russia: January 4, 1867'

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| kingdom-of-kartli 1478 found (kingdom-of-georgia) | kingdom-of-georgia 1478 dissolve | matched | georgia /ledger/57 dissolves into kingdom-of-kartli. |
| kingdom-of-kartli 1481 vassal_start (samtskhe-saatabago) | - | exception | samtskhe-saatabago (eu-19) not written yet; same for the 1483 vassal_end. |
| kingdom-of-kartli 1513 gain (kingdom-of-kakheti) | kingdom-of-kakheti 1513 loss | matched |  |
| kingdom-of-kartli 1520 loss (kingdom-of-kakheti) | kingdom-of-kakheti 1520 gain | matched |  |
| kingdom-of-kartli 1578 occupation_start (ottoman-empire) | ottoman-empire 1578 gain | mismatch | ottoman-empire /ledger/89 records a direct 1578 gain of Georgia from safavid-dynasty (Tiflis eyalet), not an occupation of kingdom-of-kartli; route to me-10. |
| kingdom-of-kartli 1604 occupation_end (ottoman-empire) | ottoman-empire 1603 loss | mismatch | ottoman-empire /ledger/96 loses Tbilisi/Kartli/Kakheti to safavid-dynasty in 1603 (type differs; year within one). |
| kingdom-of-kartli 1723 occupation_start (ottoman-empire) | - | missing | No Ottoman event for Kartli 1723-1736 (Ottoman vassal per infobox); safavid-dynasty /ledger/63 ends its Kartli vassalage in 1724. |
| kingdom-of-kartli 1736 occupation_end (ottoman-empire) | afsharid-iran 1736 gain | mismatch | Ottoman side missing; afsharid-iran /ledger/0 has a 1736 gain of Caucasian Iberia from the Ottomans. |
| kingdom-of-kartli 1762 merge (kingdom-of-kakheti) | kingdom-of-kakheti 1762 merge | matched |  |
| kingdom-of-kartli 1762 dissolve (kingdom-of-kartli-kakheti) | kingdom-of-kartli-kakheti 1762 found | matched | After the reviewer's slug fix (was kingdom-of-georgia). |
| afsharid-iran 1744 vassal_start (kingdom-of-georgia) | kingdom-of-kartli 1744 (none) | mismatch | afsharid-iran /ledger/19 and /ledger/25 name kingdom-of-georgia for Teimuraz II's Kartli 1744-1747; should be kingdom-of-kartli (me-10). |
| safavid-dynasty 1510 vassal_start (kingdom-of-kartli) | kingdom-of-kartli 1555 (infobox) | mismatch | safavid-dynasty /ledger/7-8 and /ledger/63-64 keep Kartli and Kakheti vassals 1510-1724 without the Ottoman interval 1578-1612 the infoboxes give (Persia 1555-1578, 1612-1723; Ottoman 1578-1612, 1723-1736). Ottoman-empire has no vassal_start for either kingdom. |
| kingdom-of-kakheti 1466 found (kingdom-of-georgia) | kingdom-of-georgia 1463 split | mismatch | georgia /ledger/54 splits Kakheti off in 1463 ('does not date the Kakheti kingdom'); Kakheti infobox 'Established: 1466'. Georgia side (eu-19-d) should move to 1466 or hold Kakheti to 1465. |
| kingdom-of-kakheti 1677 loss (safavid-dynasty) | - | missing | safavid-dynasty has no 1677 gain of Kakheti or 1703 loss (me-10). |
| kingdom-of-kakheti 1703 gain (safavid-dynasty) | - | missing | As above. |
| kingdom-of-kakheti 1724 occupation_start (ottoman-empire) | - | missing | No Ottoman occupation of Kakheti 1724-1736 (me-10); safavid-dynasty /ledger/64 ends its Kakheti vassalage in 1724. |
| kingdom-of-kakheti 1736 occupation_start (afsharid-iran) | afsharid-iran 1736 gain | mismatch | afsharid-iran /ledger/0 records a 1736 gain of Caucasian Iberia from the Ottomans, not an occupation of Kakheti. |
| kingdom-of-kakheti 1744 occupation_end (afsharid-iran) | afsharid-iran 1744 vassal_start | matched | afsharid-iran /ledger/18 makes Kakheti a vassal in 1744 (to 1747). |
| kingdom-of-kakheti 1762 dissolve (kingdom-of-kartli-kakheti) | kingdom-of-kartli-kakheti 1762 merge | matched | After the reviewer's slug fix. |
| kingdom-of-imereti 1463 found (kingdom-of-georgia) | kingdom-of-georgia 1463 split | matched |  |
| kingdom-of-imereti 1463 vassal_start (principality-of-guria) | - | exception | Schema puts vassal events in the suzerain's ledger only; principality-of-guria acknowledges in /identity/predecessors note. Same for /ledger/9 (1810). |
| kingdom-of-imereti 1463 vassal_start (principality-of-mingrelia) | - | exception | As above; also /ledger/4 (1557), /ledger/7 (1774), /ledger/8 (1803). |
| kingdom-of-imereti 1490 vassal_start (principality-of-abkhazia) | - | exception | As above; principality-of-abkhazia /keyframe_review/1 acknowledges. Also /ledger/10 (1810). |
| kingdom-of-imereti 1765 occupation_start (ottoman-empire) | - | missing | No Ottoman occupation of Kutaisi 1765-1767 in ottoman-empire (me-10). |
| kingdom-of-imereti 1810 dissolve (russian-empire) | russian-empire 1810 gain | matched | russian-empire /ledger/53. |
| ottoman-empire 1555 gain (kingdom-of-imereti) | principality-of-guria 1547 loss | mismatch | ottoman-empire /ledger/80 takes Ajaria from kingdom-of-imereti in 1555; Imereti records only Ottoman vassalage from 29 May 1555, and Ajaria is Guria's loss of 1547 (1540s). Ottoman side should name principality-of-guria and the 1540s. |
| ottoman-empire 1612 loss (kingdom-of-imereti) | - | mismatch | ottoman-empire /ledger/101 (confidence 1) returns Georgian cells to Imereti in 1612; Imereti keeps its shape through 1579-1611 as an Ottoman vassal (new keyframe), so the Ottoman row should draw 1579-1611 as vassal tint, not direct. |
| russian-empire 1804 vassal_start (absent) (kingdom-of-imereti) | - | missing | russian-empire has no vassal_start for Imereti (25 April 1804), Mingrelia (1803), Guria (19 June 1810) or Abkhazia (2 July 1810) (eu-17). |
| principality-of-abkhazia 1463 found (kingdom-of-georgia) | - | missing | kingdom-of-georgia has no split/loss for Abkhazia, Guria or Mingrelia in 1463 (its 1463 keyframe holds only Kartli, so the land is not drawn twice) (eu-19-d). |
| principality-of-abkhazia 1572 loss (ottoman-empire) | - | missing | No Ottoman gain of Sukhumi/Tskhumi (me-10). |
| principality-of-abkhazia 1700 gain (principality-of-mingrelia) | principality-of-mingrelia 1700 loss | matched |  |
| principality-of-abkhazia 1727 loss (ottoman-empire) | ottoman-empire 1727 gain | mismatch | ottoman-empire /ledger/139 is a 1727 gain from safavid-dynasty (Iran, Azerbaijan, Armenia, 13 Georgian cells); nothing from Abkhazia, Mingrelia or Guria. Confidence 1 on both sides. |
| principality-of-abkhazia 1788 gain (ottoman-empire) | - | missing | No Ottoman loss in 1788. |
| principality-of-abkhazia 1810 loss (russian-empire) | - | missing | No Russian gain of Sukhum-Kale in 1810 (eu-17). |
| principality-of-abkhazia 1864 dissolve (russian-empire) | - | missing | No Russian gain of Abkhazia in 1864 (eu-17); Abkhazia's new keyframe 1830-1863 may overlap the Russian row. |
| principality-of-guria 1463 found (kingdom-of-georgia) | - | missing | See Abkhazia 1463. |
| principality-of-guria 1547 loss (ottoman-empire) | ottoman-empire 1555 gain | mismatch | See ottoman-empire 1555 above: 8 years and the counterpart differ. |
| principality-of-guria 1609 gain (ottoman-empire) | - | missing | No Ottoman loss of Adjara in 1609; and Guria itself lacks the 1614 loss. |
| principality-of-guria 1723 loss (ottoman-empire) | - | missing | No Ottoman gain of Batumi/Chakvi. |
| principality-of-guria 1772 loss (ottoman-empire) | - | missing | No Ottoman gain of Kobuleti. |
| principality-of-guria 1829 dissolve (russian-empire) | russian-empire 1829 gain | mismatch | russian-empire /ledger/73 takes Anapa, Poti etc. from the Ottomans in 1829, not Guria; and /ledger/63 already gains {country: Georgia} from qajar-dynasty in 1813, which swallows Guria, Mingrelia, Abkhazia (still principalities) and Ottoman Adjara. |
| principality-of-mingrelia 1463 found (kingdom-of-georgia) | - | missing | See Abkhazia 1463. |
| principality-of-mingrelia 1721 loss (principality-of-svaneti) | - | exception | principality-of-svaneti (eu-19) not written yet. |
| principality-of-mingrelia 1727 loss (ottoman-empire) | - | missing | No Ottoman gain of the Poti coast in 1727 (see ottoman-empire /ledger/139). |
| principality-of-mingrelia 1867 dissolve (russian-empire) | - | missing | No Russian gain of Mingrelia in 1867 (eu-17); Mingrelia's new keyframe 1811-1866 may overlap the Russian row. |

## Gazetteer names needed

- Samurzakano (region; principality-of-abkhazia, principality-of-mingrelia)
- Kobuleti (place; principality-of-guria)

## Counterparts needing dossiers

- Elisu Sultanate (elisu-sultanate, eu-19): Kakheti successor, no land or years on the page.

## Problems

- None of the six Wikipedia articles gives an area: area checks are internal only.
- Neighbour dossiers not yet written (exceptions): principality-of-svaneti, samtskhe-saatabago, khanates-of-the-caucasus, elisu-sultanate.
- Most unmatched mirrors are on the suzerains' side (ottoman-empire, safavid-dynasty written 2026-10-25 by me-10; russian-empire by eu-17; afsharid-iran me-10): the author's notes list the vassal dates for them.
