# Review of batch am-08-e (The republics from 1810, part e)

Reviewed 2026-10-19 by the adversarial reviewer. Dossiers: venezuela, centralist-mexico, peru-bolivian-confederation, riograndense-republic, guatemala, honduras. The machine copy is history/notes/phase-b/reviews/am-08-e.json.

## Mechanical checks

`validate_dossier.py --resolve`: all six valid, 0 errors. Warnings: venezuela Ankoko occupation without end (by design: still held); centralist-mexico five 'republic-of-yucatan' counterparts (listed for am-08-x); 'Soconusco' (centralist-mexico, guatemala) and 'Swan Islands' (honduras) unknown to the gazetteer.
Neighbour dossiers read (ledger lines only): federated-republic-of-mexico, empire-of-brazil, united-provinces-of-central-america, gran-colombia, republic-of-peru, bolivia, republic-of-chile, argentine-confederation, united-states-of-america; netherlands-antilles, republic-of-new-granada, republic-of-ecuador, paraguay, oriental-republic-of-uruguay and spanish-empire have no event with this batch. Not yet written (exception: group has not run): republic-of-el-salvador, british-colonial-empire, republic-of-nicaragua, republic-of-colombia, mexico, guyana, belize, mosquito-kingdom, los-altos, republic-of-the-rio-grande and the other am-08 rows.
Page budgets (5 for venezuela, centralist-mexico, guatemala, honduras; 2 for the confederation and Riograndense) were respected; thin items below are judged against them.

Spot checks: 18 distinct pages opened, 4-5 events per dossier among the confidence-3 and land-moving ones. No confidence-3 event was fabricated or mis-dated. One confidence-1 event is mis-dated (centralist-mexico /ledger/6), one region overstated (peru-bolivian-confederation Salta), and four notes or war texts misreported their page (fixed by the reviewer).

## venezuela: fix

Area: infobox 916445 km2 against Cliopatria 937211 km2 (ratio 1.02); acknowledged in the keyframe notes: yes.

Fixes:
- `/wars/3/outcome` (applied by the reviewer): The outcome dates Venezuela's denunciation of the 1899 award to '12 November 1962', which is not on the cited page. Evidence: Guayana_Esequiba: 'Venezuela denounced it before the first assembly of the United Nations in 1945'; 'Venezuela formally raised the issue again at an international level before the United Nations in 1962'. Fix: Reviewer rewrote it as: denounced before the UN in 1945 and 'formally raised the issue again' there in 1962.

Thin (for a gap-filler):
- `/ledger/3`: 1877 loss of 7 cells to British Guiana at confidence 1 (page silent; the Schomburgk Line dates are 1840 and October 1886). Probably rasterisation noise like the 1853 one-cell change: either find a dated 1877 event or drop it and say so in /keyframe_review/3. Page to try: https://en.wikipedia.org/wiki/Schomburgk_Line
- `/ledger/4`: 1877 gain of 4 cells from empire-of-brazil at confidence 1; the Brazil-Venezuela border page has only the 5 May 1859 treaty and the 1929 protocol, and empire-of-brazil has no mirror. Same choice: a dated event or drop as noise. Page to try: https://en.wikipedia.org/wiki/Brazil%E2%80%93Venezuela_border
- `/ledger/7`: The Ankoko occupation has no end (still held, per the page); the validator warning stays by design. Page to try: https://en.wikipedia.org/wiki/Ankoko_Island

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Venezuela: confirmed (infobox 'from Gran Colombia: 13 January 1830'; body 'proclamation of a newly independent Venezuela, on 22 September')
- `/ledger/1` https://en.wikipedia.org/wiki/Venezuela: confirmed (with /ledger/2 and /ledger/6: 'Estado de Venezuela (1830-1856), Republica de Venezuela (1856-1864) ... Estados Unidos de Venezuela (1864-1953), and again Republica de Venezuela (1953-1999)')
- `/ledger/5` https://en.wikipedia.org/wiki/Guayana_Esequiba: confirmed ('On 3 October 1899 the Tribunal ruled largely in favour of Britain'; 'Venezuela received Barima Point at the mouth of the Orinoco'; border 'at the Wenamu River')
- `/ledger/7` https://en.wikipedia.org/wiki/Ankoko_Island: confirmed ('began their occupation of Ankoko Island in October 1966'; 6 43 N 61 8 W; 'remains under Venezuelan administration')

## centralist-mexico: fix

Area: infobox 4350000 km2 against Cliopatria 2144956 km2 (ratio 0.49); acknowledged in the keyframe notes: yes.

Fixes:
- `/ledger/6` (for the author): The return of Coahuila, Nuevo Leon and Tamaulipas from the Republic of the Rio Grande is dated 1842 (confidence 1, 'page silent') though the rebellion ended on 6 November 1840. Evidence: Republic_of_the_Rio_Grande: 'The rebellion lasted from January 17 to November 6, 1840'; Canales 'surrendered at Camargo' on 6 November 1840. The federated-republic-of-mexico dossier (/ledger/11) and this dossier's own note quote the same dates. Fix: Move the gain to 1840-11 with source https://en.wikipedia.org/wiki/Republic_of_the_Rio_Grande (add it to sources), confidence 2; add a new keyframe for 1840-11..1841 (or split /keyframe_review/2) whose correction is union(the current 1840 correction, Coahuila, Nuevo Leon, Tamaulipas); note that Cliopatria's Rio Grande row runs a year too long.
- `/keyframe_review/1` (for the author): The Centralist corrections keep Cliopatria's cells in Alta California, Arizona and New Mexico while the federated-republic-of-mexico dossier adds {'region': 'Alta California'} to its own 1836-1845 shapes: the two dossiers draw the same land. Evidence: gazetteer.py resolve intersect: Centralist Mexico 1836 holds 105 cells of California (about 26,600 km2), 280 of Arizona, 30 of New Mexico; the 1842 shape holds 76 of California, 278 of Arizona, 129 of New Mexico and 20 of Texas. federated-republic-of-mexico /keyframe_review/3-5 corrections are union(Federated shape, Alta California). Fix: In /keyframe_review/0-4 corrections subtract {'region':'Alta California'} (and the New Mexico province and Texas cells the Federated row holds), or agree with the Federated author which row holds the north; say which in the notes.
- `/wars/3/zones` (for the author): The Mexican-American War lists zones (Alta California, Texas) but this ledger has no contest or occupation event for them; the federated-republic-of-mexico and united-states-of-america dossiers carry the 1846 contests with federated-republic-of-mexico as counterpart. /wars/0/zones (Texas, for the Texas Revolution) has the same problem: the 1836 shape holds no Texas cells. Evidence: Validator rule: contest events need a war zone; here the war zones have no events. Centralist_Republic_of_Mexico: 'American forces were seizing Alta California' before 22 August 1846. Fix: Either empty both wars' zones with a note that the Federated row carries those fronts, or add contest_start 1846-04/06 and contest_end 1846-08 with united-states-of-america over the land this shape holds (the Nueces cells of Tamaulipas, the California cells).

Thin (for a gap-filler):
- `/ledger/5`: 1842 gain of Chihuahua, Durango and southern New Mexico from federated-republic-of-mexico at confidence 1: a Cliopatria drawing transfer between two rows of one country (the author says so). Resolves only with the orchestrator's decision on the two rows. Page to try: https://en.wikipedia.org/wiki/Centralist_Republic_of_Mexico

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Centralist_Republic_of_Mexico: confirmed ('a unitary political regime established in Mexico on 23 October 1835')
- `/ledger/9` https://en.wikipedia.org/wiki/Centralist_Republic_of_Mexico: confirmed ('on 22 August 1846 restored the Constitution of 1824, putting an end to Centralist Republic')
- `/ledger/2` https://en.wikipedia.org/wiki/Republic_of_Yucat%C3%A1n: confirmed ('On June 6, 1840, the city of Campeche surrendered to the Yucatecan Federalists'); /ledger/7 (August 1842, Carmen Island) and /ledger/8 (5 December 1843, 'the Republic retained its sovereignty') also confirmed
- `/ledger/4` https://en.wikipedia.org/wiki/Soconusco: confirmed ('which Soconusco did in 1842', no month; Guatemala 'declaring it part of the Quetzaltenango District in 1840')
- `/ledger/6` https://en.wikipedia.org/wiki/Republic_of_the_Rio_Grande: mis-dated (page: rebellion 'from January 17 to November 6, 1840'; ledger 1842, confidence 1)

## peru-bolivian-confederation: fix

Area: infobox none km2 against Cliopatria 3195637 km2 (ratio n/a); acknowledged in the keyframe notes: yes.

Fixes:
- `/ledger/4/region` (applied by the reviewer): The 1838 Bolivian occupation was drawn as the whole of Jujuy and Salta provinces (about 210,000 km2); neither page names Salta. Evidence: Peru-Bolivian_Confederation: Bolivia was 'occupying and incorporating certain disputed territories in northern Argentina in 1838' (no places); War_of_the_Confederation: Argentina lost 'some territories north of Jujuy'. Fix: Reviewer narrowed the region to {'admin1':'Jujuy','country':'Argentina'} here, in /ledger/7/region and in /wars/0/zones/2, kept confidence 2 (1 for /ledger/7) and the source text, and noted the change in the /ledger/4 note.

Thin (for a gap-filler):
- `/ledger/7`: The return of the occupied Argentine land is dated 1839 at confidence 1; the War page says only that the territories 'are returned' under the Bolivia-Argentina peace. The occupied places themselves (the Puna of Jujuy?) are also unnamed. Page to try: https://es.wikipedia.org/wiki/Guerra_contra_la_Confederaci%C3%B3n_Per%C3%BA-Boliviana

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Peru%E2%80%93Bolivian_Confederation: confirmed ('by decree given in Lima on 28 October 1836'; capital Tacna)
- `/ledger/2` https://en.wikipedia.org/wiki/War_of_the_Confederation: confirmed ('The Chilean army landed at Islay in southern Peru in October, 1837, occupying the city of Arequipa')
- `/ledger/5` https://en.wikipedia.org/wiki/War_of_the_Confederation: confirmed with /ledger/6 ('occupied Lima at the end of October, 1838 but abandoned it on November 3')
- `/ledger/9` https://en.wikipedia.org/wiki/Peru%E2%80%93Bolivian_Confederation: confirmed ('Dissolution declared: 25 August 1839'; Velasco 'later declared the confederation dissolved on 26 October 1839'); /ledger/8 Yungay 20 January 1839 confirmed on the War page
- `/ledger/4` https://en.wikipedia.org/wiki/Peru%E2%80%93Bolivian_Confederation: year confirmed (1838), region overstated: Salta on no page (fixed)

## riograndense-republic: fix

Area: infobox none km2 against Cliopatria 287825 km2 (ratio n/a); acknowledged in the keyframe notes: yes.

Fixes:
- `/identity/successors/0/land` (applied by the reviewer): The land handed to the empire was the raw Cliopatria 1842 shape, which includes the Uruguayan and Argentine border slivers the keyframe corrections remove. Evidence: /keyframe_review/0-1 and /ledger/5 use minus(Rio Grande do Sul, Porto Alegre 25 km); Riograndense_Republic: the republic 'was reincorporated into the Brazilian Empire'. Fix: Reviewer set the successor land to the same minus(Rio Grande do Sul, Porto Alegre 25 km) region, keeping its text.

Thin (for a gap-filler):
- `/identity/capitals`: Capital spans (Piratini 1836-1842, Alegrete 1843-1845) are bridges; the page lists five capitals without years. Page to try: https://en.wikipedia.org/wiki/Piratini

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Riograndense_Republic: confirmed ('It was proclaimed on 11 September 1836 by general Antonio de Sousa Neto')
- `/ledger/2` https://en.wikipedia.org/wiki/Riograndense_Republic: confirmed ('Laguna was taken ... on 22 July 1839'; Juliana Republic proclaimed 29 July)
- `/ledger/3` https://en.wikipedia.org/wiki/Riograndense_Republic: confirmed ('The retaking of Laguna on 1 November 1839 put an end to the Juliana Republic')
- `/ledger/4` https://en.wikipedia.org/wiki/Riograndense_Republic: confirmed ('on 1 March 1845, peace was signed: the Ponche Verde Treaty'); /keyframe_review/0 Porto Alegre confirmed on Ragamuffin_War ('recaptured by the empire in June 1836, and the rebels never managed to retake it')

## guatemala: thin

Area: infobox 108889 km2 against Cliopatria 109084 km2 (ratio 1.0); acknowledged in the keyframe notes: yes.

Fixes:
- `/wars/2/outcome` (applied by the reviewer): The 1863 war's outcome said the page records 'only' the open war, but the cited page also has Carrera besieging and occupying San Salvador. Evidence: History_of_Guatemala: the rivalry 'escalated into open war in 1863' and Carrera 'besieged and occupied San Salvador' (no date given). Fix: Reviewer rewrote the outcome to quote the occupation and flagged the missing ledger event in the war note.

Thin (for a gap-filler):
- `/ledger`: Missing occupation_start/occupation_end of San Salvador by Guatemala in 1863 (counterpart republic-of-el-salvador, region {'place':'San Salvador','km':30}); the History of Guatemala page gives the year but no month, so a dated page is needed. Page to try: https://en.wikipedia.org/wiki/Gerardo_Barrios
- `/certainty/0`: The 1882 Mexican treaty, the 1933 Honduran arbitration and the Salvadoran frontier are on no page opened (no shape change in Cliopatria, so only certainty notes depend on them). Page to try: https://en.wikipedia.org/wiki/Guatemala%E2%80%93Mexico_border

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Guatemala: confirmed ('Declared from the Federal Republic of Central America: 17 April 1839')
- `/ledger/1` https://en.wikipedia.org/wiki/Los_Altos_(state): confirmed (infobox 'Forcible reincorporation into Guatemala: January 1840'; body 2 April 1840, as the note says)
- `/ledger/3` https://en.wikipedia.org/wiki/Guatemala: confirmed ('On 21 March 1847, Guatemala declared itself an independent republic and Carrera became its first president')
- `/ledger/5` https://en.wikipedia.org/wiki/Los_Altos_(state): confirmed ('The existence of Los Altos lasted until 8 May 1849'); /ledger/4 26 August 1848 also confirmed; Los Altos had eight departments 'as well as the Soconusco region'
- `/ledger/2` https://en.wikipedia.org/wiki/Soconusco: confirmed (1842, no month)

## honduras: thin

Area: infobox 112492 km2 against Cliopatria 114698 km2 (ratio 1.02); acknowledged in the keyframe notes: yes.

Fixes:
- `/ledger/2/note` (applied by the reviewer): The note quotes 'By 1859 Britain ceded the northern part of the Mosquito Coast to Honduras', a sentence the page does not have (the year is in the sentence before). Evidence: Mosquito_Coast: 'By 1859 British opinion was no longer supportive of their nation's presence in the Mosquito Coast.' 'The British government returned the Bay Islands and ceded the northern part of the Mosquito Coast to Honduras'. Fix: Reviewer replaced the quote with the two verbatim sentences; year and confidence 2 unchanged.
- `/ledger/4/note` (applied by the reviewer): The note puts in quotation marks words on neither page ('cuts the cape in half', 'was disputed from 1869'). Evidence: Mosquito_Coast: 'Attempts to decide the sovereignty over the northern bank of the Wanks/Coco River' were made from 1869 until the ICJ ruled for Honduras; Cape_Gracias_a_Dios has only the 1906 award and the 1960 confirmation. Fix: Reviewer rewrote the sentence with the verbatim phrase; year 1869 and confidence 2 unchanged.
- `/wars/1/note` (applied by the reviewer): The Football War note said the page gives no ceasefire date, but it does, and the Salvadoran withdrawal too. Evidence: Honduras: 'on 14 July 1969, the Salvadoran army invaded Honduras'; an OAS 'cease-fire which took effect on 20 July'; 'a withdrawal of Salvadoran troops in early August'. Fix: Reviewer rewrote the note with the dates and flagged the missing occupation as a gap.

Thin (for a gap-filler):
- `/ledger/1`: 1846 loss of the eastern Mosquitia to the Mosquito Kingdom at confidence 1 (Cliopatria's date; the page has the British protectorate of 1844). Page to try: https://en.wikipedia.org/wiki/Mosquito_Kingdom
- `/ledger`: Missing occupation_start 1969-07 / occupation_end 1969-08 by republic-of-el-salvador: dates on the Honduras page, the occupied towns not. Page to try: https://en.wikipedia.org/wiki/Football_War
- `/ledger`: Missing 1907 Nicaraguan-backed invasion: History of Honduras: 'Supported by elements of the Nicaraguan army, the exiles invaded Honduras in February 1907' (ground and dates needed). Page to try: https://en.wikipedia.org/wiki/Battle_of_Namasig%C3%BCe
- `/keyframe_review/7`: The 1992 ICJ judgment on the Salvadoran frontier (the bolsones) is on no page opened; Cliopatria's 1979-1991 and 1992 shapes differ by 56 km2. Page to try: https://en.wikipedia.org/wiki/El_Salvador%E2%80%93Honduras_relations

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Honduras: confirmed (infobox 'Declared, as Honduras, from the Federal Republic of Central America: 5 November 1838')
- `/ledger/5` https://en.wikipedia.org/wiki/Honduras: confirmed ('Comayagua was the capital of Honduras until 1880, when the capital moved to Tegucigalpa')
- `/ledger/8` https://en.wikipedia.org/wiki/History_of_Honduras: confirmed ('On November 22, 1971, the United States handed over the Swan Islands to Honduras'; sovereignty from 1 September 1972); the 1906 war is also on the page ('resisted an invasion from Guatemala in 1906')
- `/ledger/2` https://en.wikipedia.org/wiki/Mosquito_Coast: confirmed, quote not verbatim (fixed): 1859 is in the preceding sentence
- `/ledger/6` https://en.wikipedia.org/wiki/Mosquito_Coast: confirmed ('In 1960 the northern part was granted to Honduras by the International Court of Justice'); /ledger/7 confirmed on Honduras ('transferred from Nicaragua to Honduras')

## Observations that need no change

- venezuela and republic-of-venezuela kept as two states (1810-1814 against 1830 on): agreed; gran-colombia dates the separation 1830-05, this dossier 1830-09, both on the pages.
- honduras: the 1869-1960 contest and the 1960 gain cover land that Cliopatria already draws Honduran from 1860; the Honduras page says the northern Mosquito Coast was 'transferred from Nicaragua to Honduras' in 1960, so the blend is the honest drawing; no keyframe change asked.
- guatemala: the 1848-1849 loss and regain of Los Altos fall inside the 1842-1912 shape and are named in its note; the renderer applies them from the ledger.
- peru-bolivian-confederation: the two pages disagree on Argentina's declaration of war (19 May 1837 on the Confederation page, 9 May on the War page), as the author noted.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| venezuela 1830 found (gran-colombia) | gran-colombia 1830 loss | matched | gran-colombia has 1830-05 (Valencia congress), this dossier 1830-09; same year. |
| venezuela 1877 loss (british-colonial-empire) | british-colonial-empire - - | exception | british-colonial-empire (eu-11) not written yet; confidence 1, possibly noise. |
| venezuela 1877 gain (empire-of-brazil) | empire-of-brazil - - | missing | empire-of-brazil has no venezuela event; this side is confidence 1 page silent: drop as noise rather than add a mirror. |
| venezuela 1899 gain (british-colonial-empire) | british-colonial-empire - - | exception | group eu-11 has not run. |
| venezuela 1966 occupation_start (guyana) | guyana - - | exception | guyana (am-08) not written yet. |
| centralist-mexico 1835 found (federated-republic-of-mexico) | federated-republic-of-mexico 1835 split | matched | Both 1835-10. |
| centralist-mexico 1840 loss (republic-of-yucatan) | republic-of-yucatan - - | exception | Listed in counterparts_needing_dossiers (am-08-x); also the 1840 and 1842-1843 contests. |
| centralist-mexico 1842 gain (guatemala) | guatemala 1842 loss | matched | Soconusco, both 1842 without month. |
| centralist-mexico 1842 gain (federated-republic-of-mexico) | federated-republic-of-mexico 1842 loss | matched | Both confidence 1 drawing transfers between two rows of one Mexico (orchestrator decision). |
| centralist-mexico 1842 gain (republic-of-the-rio-grande) | republic-of-the-rio-grande - - | exception | Dossier not written (am-08); but the page ends the republic on 1840-11-06 and federated-republic-of-mexico has the loss to it in 1840-01: this gain should be 1840-11. |
| centralist-mexico 1846 dissolve (federated-republic-of-mexico) | federated-republic-of-mexico 1846 gain | matched | Both 1846-08. |
| peru-bolivian-confederation 1836 found (republic-of-peru) | republic-of-peru 1836 loss | matched | Both 1836-10. |
| peru-bolivian-confederation 1836 gain (bolivia) | bolivia 1836 loss | matched | Both 1836-10. |
| peru-bolivian-confederation 1837 occupation_start (republic-of-chile) | republic-of-chile - - | missing | republic-of-chile has no events 1835-1841; it should carry occupation_start 1837-10 / occupation_end 1837-11 of Arequipa. |
| peru-bolivian-confederation 1838 occupation_start (republic-of-chile) | republic-of-chile - - | missing | Lima, end of October to 3 November 1838: missing in republic-of-chile. |
| peru-bolivian-confederation 1838 occupation_start (argentine-confederation) | argentine-confederation - - | missing | argentine-confederation has no 1837-1839 event for the War of the Confederation; it should carry the Bolivian occupation of northern Jujuy (1838-1839) with peru-bolivian-confederation as counterpart. |
| peru-bolivian-confederation 1839 loss (republic-of-peru) | republic-of-peru 1839 gain | matched | Both 1839-01. |
| peru-bolivian-confederation 1839 loss (bolivia) | bolivia 1839 gain | matched | Both 1839-10. |
| riograndense-republic 1836 found (empire-of-brazil) | empire-of-brazil 1836 loss | matched | Both 1836-09. |
| riograndense-republic 1836 contest_start (empire-of-brazil) | empire-of-brazil 1835 contest_start | matched | Empire's contest starts 1835-09 with the rising, before the republic existed; acceptable. |
| riograndense-republic 1839 contest_start (empire-of-brazil) | empire-of-brazil 1839 contest_start | mismatch | Land differs: Laguna 40 km here (page: 'Laguna was taken ... on 22 July 1839'), all of Santa Catarina in empire-of-brazil /ledger/15-16 (confidence 2, no month). empire-of-brazil should narrow to Laguna and add months 7 and 11. |
| riograndense-republic 1845 dissolve (empire-of-brazil) | empire-of-brazil 1845 gain | matched | Both 1845-03, with the contest_end. |
| guatemala 1839 found (united-provinces-of-central-america) | united-provinces-of-central-america 1839 dissolve | matched | Both 1839-04. |
| guatemala 1840 gain (los-altos) | los-altos - - | exception | los-altos (am-08) not written yet; it should end in 1840-01 (not 1841) and carry the 1848-08..1849-05 second state. |
| guatemala 1842 loss (centralist-mexico) | centralist-mexico 1842 gain | matched | Soconusco. |
| guatemala 1848 loss (los-altos) | los-altos - - | exception | Not written yet; also the 1849-05 gain. |
| honduras 1838 found (united-provinces-of-central-america) | united-provinces-of-central-america 1838 loss | matched | Federation 1838-10, Honduras 1838-11 (page infobox 5 November). |
| honduras 1846 loss (mosquito-kingdom) | mosquito-kingdom - - | exception | mosquito-kingdom (am-08) not written yet; also the 1859 gain. |
| honduras 1859 gain (british-colonial-empire) | british-colonial-empire - - | exception | Bay Islands; eu-11 has not run. |
| honduras 1960 gain (republic-of-nicaragua) | republic-of-nicaragua - - | exception | republic-of-nicaragua (am-08) not written yet; also the 1869-1960 contest. |
| honduras 1971 gain (united-states-of-america) | united-states-of-america - - | missing | united-states-of-america has no 1971 Swan Islands loss (Treaty of the Swan Islands, 22 November 1971). |

## Problems for the orchestrator

- Orchestrator decision still open (also review-am-08-c item 5): Cliopatria's Centralist Mexico and Federated Republic of Mexico rows draw one country as two simultaneous states in 1836-1846; the centralist-mexico and federated-republic-of-mexico dossiers keep the split, with confidence-1 'drawing transfer' gains in 1842 and overlapping Alta California land. Either merge (centralist-mexico becomes rename events 1835-10 and 1846-08 in federated-republic-of-mexico and its shapes are reviewed there) or keep the split and give both one colour and disjoint corrections.
- republic-of-the-rio-grande (not yet written) should end on 6 November 1840 (Republic_of_the_Rio_Grande page), not 1841 as Cliopatria draws; centralist-mexico /ledger/6 must move with it.
- los-altos (not yet written) should end its first life in January 1840 and carry the second state of 26 August 1848 - 8 May 1849, matching guatemala.
- Mirrors to route to written dossiers: republic-of-chile (Arequipa 1837, Lima 1838 occupations), argentine-confederation (Bolivian occupation of northern Jujuy 1838-1839), united-states-of-america (Swan Islands loss 1971-11), empire-of-brazil (Laguna rather than all of Santa Catarina in 1839).
- Reviewer edits applied and re-validated (0 errors): venezuela /wars/3/outcome; peru-bolivian-confederation /ledger/4, /ledger/7, /wars/0/zones/2 (Salta removed); riograndense-republic /identity/successors/0/land; guatemala /wars/2; honduras /ledger/2, /ledger/4, /wars/1 notes.
- WebFetch: 18 distinct pages opened, all loaded.

## Gazetteer names needed

- Soconusco (region): centralist-mexico, guatemala. Swan Islands (region): honduras.
