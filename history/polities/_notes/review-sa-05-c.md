# Review of batch sa-05-c (kingdom-of-bhutan), 2026-10-19

Reviewer: adversarial reviewer, Phase B. Dossier: history/polities/kingdom-of-bhutan.json (18 Cliopatria shapes, page budget 9, all 9 spent by the author). Neighbour dossiers present and read: tibet, khoshut-khanate, burma. Absent (groups not yet run or no dossier): qing-dynasty, british-empire, british-raj, republic-of-india, people-s-republic-of-china, mughal-empire, republic-of-china, nepal; sikkim, koch-bihar, ahom-kingdom (listed by the author under counterparts_needing_dossiers).

## Verdict: fix (applied by the reviewer)

## Mechanical checks
- validate_dossier.py --resolve: 0 errors; 34 warnings = 8 counterpart slugs without dossiers (sikkim x3, koch-bihar x4, ahom-kingdom x1) and 26 gazetteer unknowns (Kalimpong x10, Cooch Behar x7, Bengal Duars x5, Assam Duars x2, Dewangiri x2). All names real; listed for the gazetteer agent.
- File name = slug; cliopatria_names "Kingdom of Bhutan" matches polities.csv; all 18 shapes (1636..2024) have verdicts; two new keyframes (1616-1633, 1634-1635) carry from, to and correction.
- Ledger sorted; found at 1616 = start; no dissolve needed (extant 2024); contest pairs 1700/1706 (sikkim), 1772/1774 (british-empire), 1864/1865 (british-raj) each match a war with one zone; vassal 1765/1773 and occupation 1765/1774 paired.
- Family "india" is a colours.json family; capital Thimphu (89.639 E, 27.473 N) lies inside the shapes' bbox (88.80-92.16 E, 26.71-28.32 N) and inside the 1616 core (Paro + Thimphu).
- Areas quoted by the author match shapes.csv (41,700; 40,266; 40,754; 40,456; 71,218; 71,861 km2).

## Area check
Bhutan infobox: "Total: 38,395 km2" (no year; today). Cliopatria 2024 shape 40,721.7 km2, ratio 1.06. The 1939-1952 shapes (71.2-71.9 k km2, ratio 1.86) are acknowledged and cut back to modern Bhutan (verdict adjust); the pre-1865 Duars (a fifth of the country) are acknowledged and added by corrections 1788-1864. Nothing silent.

## Spot checks (WebFetch)
- /ledger/12 (1784 gain, Bengal Duars, c3): History of Bhutan "In 1784, the British turned over to Bhutanese control Bengal Duars territory, where boundaries were poorly defined." Confirmed.
- /ledger/14 (1841 loss, Assam Duars, c3): History of Bhutan "The British proceeded in 1841 to annex the formerly Bhutanese-controlled Assam Duars". Confirmed.
- /ledger/17 and /ledger/18 (1865-11 losses, c3): Duar War "Treaty of Sinchula, signed 11 November 1865"; "the whole of the tract known as the Eighteen Doars"; "the Hill territory on the left bank of the Teesta"; "the 83 km2 of territory of Dewangiri in southeastern Bhutan"; "Bhutan losing a fifth of its territory". Confirmed.
- /ledger/5 (1706 gain, Kalimpong, c3): Kalimpong "Kalimpong is said to have come under the control of Bhutan in the year 1706"; "encroachments had been in effect for about two decades". Confirmed.
- Incidentally confirmed on the same pages: /ledger/0 (1616 arrival), /ledger/1 (infobox "Unification: 1616-1634"; "In 1634 Ngawang Namgyal defeated Karma Tenkyong's army in the Battle of Five Lamas"), /ledger/3 ("In 1700, Bhutan again invaded Sikkim"), /ledger/6 ("By the mid-1760s, Thimphu considered Cooch Behar its dependency"), /ledger/10 ("peace agreement (25 April 1774) with Bhutan"; "pre-1730 boundaries"; "five horses"), /ledger/19 (infobox "Ascension of the Wangchuk dynasty: 17 December 1907").
- /ledger/7 (1765 occupation_start, c3): Cooch Behar State "Bhutan seized direct control of Behar territories including Jalpeswar, Mandas, Jalash", placed in the reign of Dhairjendra Narayan (1765-1770); the page gives no explicit year, and the region drawn (all of Cooch Behar) is wider than the three territories named. Confidence 3 overstated.

## Fixes
1. /ledger/7/confidence: 3 -> 2 (APPLIED by the reviewer; note extended with one sentence saying why; re-validated, 0 errors). Why: the page dates the seizure only by the reign 1765-1770 and names Jalpeswar, Mandas and Jalash, not the whole state the region spec draws.

## Thin (for a gap-filler; not faults within the 9-page budget)
- /ledger/13 (c. 1790 Assam Duars gain, confidence 1): Dooars gives only "last phase of 18th century". Try https://en.wikipedia.org/wiki/Ahom_kingdom or https://en.wikipedia.org/wiki/Moamoria_rebellion for the year the Darrang Duars passed to the Druk Desi.
- Missing small events: History of Bhutan says "Ladakh had earlier granted Bhutan several enclaves near Mount Kailash in western Tibet" "until 1959 when the Bhutanese enclaves were seized by the Chinese." The author's gap says the page gives no place; it names Mount Kailash. A 1959 loss (counterpart people-s-republic-of-china, place Mount Kailash, small km) and an earlier gain from Ladakh (year not on the page) can be added at confidence 2/1. Try https://en.wikipedia.org/wiki/Bhutan%E2%80%93China_border.
- /ledger/6 (1765 vassal_start): the same page says "In the early 18th century, Bhutan had successfully developed control over the principality of Cooch Behar" and "The raja of Cooch Behar had sought assistance from Bhutan against the Indian Mughals in 1730"; the 1774 return to "pre-1730 boundaries" implies holdings from about 1730. A gap-filler could test an earlier vassal_start (about 1730). Page: https://en.wikipedia.org/wiki/Koch_dynasty.
- /ledger/7 region: whole Cooch Behar is drawn hatched on top of the same region's vassal tint; the page names only Jalpeswar (Jalpesh, near Mainaguri, Jalpaiguri), Mandas and Jalash. Narrow the occupation region if a page places them.
- /ledger/1 (1634 gain of all Bhutan): History of Bhutan is silent on when central and eastern Bhutan (Trongsa, Bumthang, the east) came under the Zhabdrung's government; only the infobox range 1616-1634 supports 1634. Try https://en.wikipedia.org/wiki/Trongsa_Dzong for the eastern conquest.
- identity.rulers omitted: try https://en.wikipedia.org/wiki/King_of_Bhutan (Druk Gyalpo from 1907) and https://en.wikipedia.org/wiki/Druk_Desi.
- /keyframe_review/13-15: why Cliopatria's 1939-1952 Bhutan shapes carry the Arunachal strip is unexplained; the date matches the Tibet dossier's removal of the Tawang tract at Cliopatria 1939 (tibet /ledger/13), so it is likely the McMahon Line strip assigned to the wrong polity. The author's cut to modern Bhutan stands. Try https://en.wikipedia.org/wiki/McMahon_Line.
- /wars/4 zone: the British force "invaded Bhutan in 1772-73" (History of Bhutan), but the contest zone is Cooch Behar only; a gap-filler could add the Bhutanese foothill forts if a page names them.

## Cross-dossier matrix
All territorial counterparts are exceptions: nobody (1634); sikkim, koch-bihar, ahom-kingdom (no dossiers; listed in the author's counterparts_needing_dossiers); british-empire, british-raj, republic-of-india (group sa-06 has not run). Mirrors sa-06 must write: british-empire loss 1784 Bengal Duars and gain 1841 Assam Duars; british-raj gains 1865-11 (Bengal Duars, Kalimpong hill tract, Dewangiri); republic-of-india loss 1949-08 Dewangiri; british-raj vassal_start 1910 / vassal_end 1947 and republic-of-india vassal_start 1949 / vassal_end 2011 (counterpart kingdom-of-bhutan); the Arunachal strip cut from Bhutan 1939-1952 belongs in the British Raj / India keyframes.
Wars without land: khoshut-khanate's war "Khoshut expedition to Bhutan" (1644) names the belligerent as "Bhutan", not the slug "kingdom-of-bhutan", and dates it 1644 against History of Bhutan's 1643 (inside Bhutan's 1629-1647 war); the tibet dossier lists no war with Bhutan (invasions 1629-1647, 1714). Routing notes for ea-06, not faults of this dossier.

## Notes read
The author's notes flag the start-year choice, the Duars omission in Cliopatria, the 1939-1952 excess, the page disagreements (1905/1907, 1772-73/1774, 1866/1867) and the failed page. Unflagged: the 1765 occupation's year and region overstated at confidence 3 (fixed), and the Mount Kailash place on the 1959 enclaves (the gap's reason "no place" is wrong). data/README.md lists no known problem for Bhutan's rows.
