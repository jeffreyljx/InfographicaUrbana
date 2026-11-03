# Review of batch af-07-a (Southern Africa, part a)

Reviewer, 2026-10-19. Dossiers: dutch-cape-colony, republic-of-graaff-reinet, british-cape-colony, merina-kingdom, zululand. Machine copy: history/notes/phase-b/reviews/af-07-a.json.

Mechanical: `validate_dossier.py --resolve` passes all five (0 errors). Warnings: british-cape-colony 29 (27 gazetteer names, 2 'basutoland' counterpart slugs), merina-kingdom 2 (betsimisaraka-kingdom slug; northern Tanala vassal_start with no end), zululand 2 (mtetwa-paramountcy, ndwandwe-kingdom slugs). Ledgers sorted, inside the lives, found/dissolve at start/end, capitals contiguous, certainty covers each life, every event source is in sources[].

Neighbour dossiers: only new-france, republic-of-liberia and united-states-of-america exist among the Context polities and none names a state of this batch. natalia-republic, south-african-republic, free-orange-state, swaziland, nieuwe-republiek (af-07-b) and french-africa (af-08) are not written yet: their mirrors are exceptions, listed below as owed.

Verdicts: dutch-cape-colony thin; republic-of-graaff-reinet fix (applied by the reviewer); british-cape-colony thin (one fix applied by the reviewer); merina-kingdom thin; zululand thin. No fabricated or mis-dated event found: all 44 spot-checked events say on the page what the note claims.

## Reviewer edits (applied, re-validated)
- republic-of-graaff-reinet /ledger/0 and /ledger/1: confidence 3 -> 2. The page gives no boundaries ('in and around the city of Graaff-Reinet'); the Eastern Cape extent is the researcher's reading (research brief: 2 when the region is your reading). The Dutch and British mirrors were already at 2.
- british-cape-colony /ledger/2 (1803 loss to the Batavian Republic): region was Cliopatria's 1802 British Cape shape, which holds the Sierra Leone cells; now `{"cliopatria": "Napoleonic Batavia Republic", "year": 1803}`, the same land as the Dutch mirror gain (/ledger/12).

## dutch-cape-colony (thin)
- Merge with napoleonic-batavia-republic accepted (shared Q4807130; the Dutch_Cape_Colony infobox runs 1652-1806, 'Cape Colony to Dutch rule: 1 March 1803').
- Spot checks confirmed: 1795 (infobox 'First British occupation: 7 August 1795'), 1 March 1803, January 1806 (Blaauwberg), Delagoa Bay April 1721 and December 1730, 1660 cession, 1672 purchase, 1745 and 1786 magistracies.
- Area: infobox 145,000 km2 (no year) against the 1788-1795 shape 278,665 km2, ratio 1.92, discussed in /keyframe_review/7.
- Fix (not applied): /wars/1 and /wars/2 (Muizenberg, Blaauwberg) have empty zones with no note, though the Cape changed hands.
- Thin: 1734 (+30,000 km2) and 1769 (+100,000 km2) steps are confidence-1 bridges; the 1652 circle to the 1653-1720 shape jump has no event (Stellenbosch 1679, Drakenstein 1687 undated); the Khoikhoi-Dutch Wars are missing from wars; the Republic of Swellendam (1795) is not split off. Within the 5-page budget, so thin by design.

## republic-of-graaff-reinet (fix, done)
- 1795 proclamation and August 1796 end confirmed on Republic_of_Graaff-Reinet. No area or boundary on the page, as the dossier says. Confidence lowered (above).

## british-cape-colony (thin)
- Spot checks confirmed (17): Basutoland 3 November 1871 and 2 February 1884; Griqualand West and East 'In 1877' (confidence 2 is right); Walvis Bay 1878; British Bechuanaland 1895; Union 31 May 1910; Orange River Sovereignty 3 February 1848, renounced 30 January 1854, Bloemfontein 23 February 1854; Transvaal annexation 12 April 1877; Pretoria Convention 3 August 1881 ('under British suzerainty'); Queen Adelaide 10 May 1835 and December 1836; British Kaffraria 17 December 1847, 7 March 1860, 17 April 1866; Orange River proclamation 17 December 1847 (History page); Xesibeland end of 1886; Pondoland 1894.
- Area: infobox 331,907 km2 (1822) against Cliopatria's 1822 shape 573,477 km2, ratio 1.73, acknowledged and corrected to the 1820 Cape (about 302,000 km2) until 1847. The History page's 'about 194,000 square kilometres' for 1814 is also discussed. The removal of the Sierra Leone, Gambia, Gorée, Socotra and Transvaal cells holds up.
- Fixes (not applied): /wars/0 and /wars/2 empty zones with no note; /ledger/15 and /ledger/20: Griqualand West is gained in 1871 and merged again in 1880 with the same region (its separate Crown-colony years are drawn as Cape land), while British Kaffraria's Crown-colony years 1860-1866 are cut out. Treat the two the same way, or say why not.
- Thin: the Transkei enters all at once in 1894 (Fingoland and Idutywa 1879, Griqualand East incorporation 1879, Port St Johns 1884, Gcalekaland and Thembuland 1885 missing); the pre-1847 northern line (1798, Colesberg 1824-1825); the Second Boer War (1899-1902: the northern Cape invasions, the sieges of Kimberley and Mafeking) is missing although the dossier now runs to 1910; the Basotho Gun War (1880-1881) is missing; the Natal administration from 1844 (infobox) is not entered; the 1812 contest_end is at confidence 1; the Graaff-Reinet rebellions of 1799-1803. The author spent 11 pages against a budget of 9.
- For the orchestrator: the 1885-1910 extension against british-africa (author flagged; see problems).

## merina-kingdom (thin)
- Spot checks confirmed (11): 1540; Mahajanga 'By 1824'; Toamasina 1817; treaty of 23 October 1817; Vohemar and Diego Suarez 1824; Farafangana and Fort Dauphin 1825; Antesaka and Tanala 1827; Tamatave 17 December 1885 (Antsiranana ceded); Toamasina 12 December 1894; Antananarivo 1 October 1895; protection 1896.
- Area: no infobox area. Radama_I: 'Radama united two thirds of the island' (about 391,000 km2) against the 1825 shape 374,728 km2, ratio 0.96.
- Fixes (not applied): /keyframe_review/7 and /8 keep the Antsiranana tip in 1820-1823 while /ledger/13 gains it in 1824 (Radama_I: 'In 1824 further expeditions established posts at Vohemar, Diego Suarez, and Mahajanga'); add a 30 km Antsiranana circle as a minus term to both corrections. /ledger/16: the northern Tanala vassal_start has no end. Free-text counterparts (rival Merina principalities, Sihanaka and Bezanozano, northern coastal chiefdoms, Antanosy, Antesaka, northern Tanala) are neither nobody nor listed. /ledger/20: the 1896 protectorate is a rename; french-africa owes a vassal_start merina-kingdom 1896.
- Thin: 1814 to 1820 (+60,000 km2, north and east) and 1820 to 1822 (+71,000 km2, east and south-east) are explained only by the 40 km Toamasina gain; 1834 (+22,000 km2) and 1840 (+29,500 km2) have no events at all (the Merina page's 'Between 1828 and 1840 ... 200,000 enslaved by Merina forces' could anchor confidence-1 bridges); four confidence-1 events (1796, 1803, 1811, 1814); rulers 1630-1787 and 1861-1883; the extent of Imerina before 1792. Within the 5-page budget.

## zululand (thin)
- Spot checks confirmed (6): Shaka's accession 1816; Mhlatuze 1820; Dingane's cession of the land south of the Tugela (treaty the day after 3 February 1838); invasion 11 January 1879; Ulundi 4 July 1879; protectorate and annexation 1887.
- Area: infobox 207,000 km2 (1822) against 25,596 km2, ratio 0.12, acknowledged and resolved (the shape is kept; the text's 'Pongola to the Tugela' is about 26,000 km2).
- Fixes (not applied): /ledger/1, the 1820 gain from ndwandwe-kingdom, uses the whole Zulu shape as its region, the land /keyframe_review/0 already draws for 1816-1819 (give it the Ndwandwe country north of the White Mfolozi and a smaller 1816-1819 keyframe). /ledger/8: the 1887 protectorate and annexation is a rename ('Protectorate of the United Kingdom 1887-1897'), so 1887-1897 is drawn as independent; british-colonial-empire owes a vassal_start zululand, or the orchestrator ends the kingdom in 1887. /wars/2 has empty zones with no note.
- Thin: 1879-1884 (the thirteen kinglets, the 1883 reserve, the 1884 grant of 'about half of Zululand') with the full shape kept to 1884; the capital moves at confidence 1; the extent in 1816-1819; Mpande's Buffalo-Tugela cession, the Utrecht district and the Disputed Territory. Within the 5-page budget.

## Mirrors owed by other batches
- free-orange-state: gain of the Orange River Sovereignty land in February 1854 (Cliopatria starts 1856).
- south-african-republic: British occupation April 1877 to August 1881, then suzerainty to 1884.
- natalia-republic: gain south of the Tugela 1838 (Cliopatria starts 1840); gain of Zululand 1897.
- nieuwe-republiek: gain round Vryheid August 1884 (its Cliopatria shape lies east of Vryheid).
- french-africa: Antsiranana December 1885; contest 1894-1895; vassal_start merina-kingdom 1896; Madagascar from 1897.
- british-colonial-empire: contest in Zululand January-July 1879; vassal_start zululand 1887-1897.
- af-07-x: xhosa-chiefdoms, british-kaffraria, griqualand-west, griqualand-east, basutoland, mpondo-kingdom, british-bechuanaland, republic-of-swellendam, betsimisaraka-kingdom, menabe-kingdom, boina-kingdom, betsileo-kingdoms, mtetwa-paramountcy, ndwandwe-kingdom, swazi-kingdom; union-of-south-africa (1910).

## Gazetteer names needed
Transkei, British Kaffraria, Griqualand East, Xesibeland, Pondoland, British Bechuanaland (all regions, used in british-cape-colony).
