# Review of batch eu-21-e (2026-11-01, adversarial reviewer)

Dossier: history/polities/yugoslav-partisans.json (1 Cliopatria shape, page budget 1-2 pages). Verdict: **fix** (two small fixes applied by the reviewer; the dossier re-validates with 0 errors and 0 warnings under --resolve). The remaining findings are non-blocking gaps for a gap-filler and cross-dossier mismatches routed to the neighbours' groups.

## Mechanical
- validate_dossier.py --resolve: valid, 0 errors, 0 warnings, 33 regions resolve (before and after the reviewer's edits).
- Slug = file name; cliopatria_names ["Yugoslav Partisans"] matches polities.csv; the one shape yugoslav-partisans_1944 (33,803 km2) has a verdict (adjust, with a correction that is the whole extent).
- Ledger sorted; found 1941-06 = start, dissolve 1945-03 = end; contest_start 1944-12 before contest_end 1945. Capitals Foca 1942, Drvar 1943-44, Belgrade 1945 contiguous from 1942 (none in 1941); coordinates checked (Drvar 44.37N 16.38E and Foca lie inside the 1944 shape bbox 15.16-20.45E, 42.17-45.37N).
- type rebel (a resistance that held land) and family balkans (a colours.json family) accepted.

## Spot checks (WebFetch)
- /ledger/9 (conf 3, Belgrade 20 Oct 1944): confirmed, Yugoslav Partisans page: 'On 20 October, the Red Army and the Partisans liberated Belgrade in a joint operation known as the Belgrade Offensive'.
- /ledger/10, /ledger/11 (Serbia, Vardar Macedonia, winter 1944): confirmed, same page: 'At the onset of winter, the Partisans effectively controlled the entire eastern half of Yugoslavia' (Serbia, Vardar Macedonia, Montenegro, the Dalmatian coast).
- /ledger/12 (Dalmatia): confirmed, WWII in Yugoslavia page: 'as well as most of the Dalmatian coast'.
- /ledger/4 (Bihac, 4 Nov 1942): confirmed: 'took Bihac and neighbouring towns on 4 November 1942' ... 'the so-called Bihac Republic'.
- /ledger/7 (Risan and Podgorica, Oct-Dec 1944): confirmed: 'liberated Risan and Podgorica between October and December', in the 1944 context.
- /ledger/1 (Uzice republic, gain): MIS-DATED at confidence 2. The author dated it November 1941 (the committee founding). Republic of Uzice page: infobox 'Fall of Uzice: 24 September 1941', 'Battle of Kadinjaca: 29 November 1941', 'Conquered: 1 December 1941'; first sentence 'existed in the autumn of 1941'. APPLIED: month 11 -> 9, source -> https://en.wikipedia.org/wiki/Republic_of_U%C5%BEice (added to sources[]), note extended.
- /ledger/5 (1943 loss of western Bosnia, confidence 1): the page is not silent: 'Axis forces pushed Partisan troops to retreat from western Bosnia to northern Herzegovina', 'from January to April, 1943'. APPLIED: confidence 1 -> 2 (year and land are the page's, Una-Sana is the researcher's reading), note extended.

## Area
Yugoslav Partisans infobox has no area (confirmed). Cliopatria 1944: 33,803 km2; the page's end-1944 extent (eastern half of Yugoslavia plus most of the Dalmatian coast) is about 125,000 km2, ratio 0.27. Acknowledged in /keyframe_review/0/note and resolved by the adjust correction (shape + Republic of Serbia + North Macedonia + Montenegro + Dalmatia, about 146,000 km2; the reviewer's rough sum of the units gives about 150,000). Accepted.

## Non-blocking findings (not applied; for the author or a gap-filler)
1. /ledger/1 region: the Republic of Uzice page bounds the republic by 'the river Drina on the west, the river Zapadna Morava in the east' and gives 15,000 or 20,000 km2; Zlatiborski alone is about 6,000 km2. Suggested region: union of the admin-1 units Zlatiborski, Moravicki, Kolubarski, Macvanski (Republic of Serbia), text from the page; the same for /ledger/2 and the 1941 war zone.
2. Kosovo: albania /ledger/20 records a 1944 loss of Kosovo with counterpart yugoslav-partisans (confidence 1); this dossier has no mirror gain, and its 1944 correction (Natural Earth 'Republic of Serbia' excludes Kosovo) leaves a hole at Kosovo. Add a 1944 gain of {"country": "Kosovo"} from albania (or decide with eu-18 that the counterpart is nazi-germany) and add Kosovo to the correction union, from a page that dates it (try 'Kosovo Operation (1944)').
3. 1942 free territory: page B (opened) says the Partisans 'established a new headquarters at Foca' after the Second Enemy Offensive (Jan-early Feb 1942) and 'By June the Partisans had lost practically all their free territory in eastern Bosnia, Montenegro and Herzegovina'; the Third Enemy Offensive was launched 15 April 1942 'between Sarajevo and the Drina'. The ledger records the Foca capital but neither the gain nor the June 1942 loss of that land, so the 1942 capital sits in land the ledger never gives the Partisans. Add a 1942 gain and a 1942-06 loss (confidence 2, regions Montenegro plus the Bosnian-Podrinje / eastern Bosnia units as captions).
4. Wars on page B missing from wars[]: Second Enemy Offensive (Jan-Feb 1942), Third Enemy Offensive (from 15 April 1942), Fifth Enemy Offensive / Sutjeska (May-June 1943, 'southeastern Bosnia and northern Montenegro').
5. Capitals: no seat in 1941 (Uzice, Sept-Nov 1941, is the republic's capital on the Republic of Uzice page); Jajce (late 1943), Drvar (to the Rosselsprung raid of late May 1944), Vis (summer 1944) and Belgrade from late October 1944 are page-silent on the two pages the author opened. Pages to try: Second session of AVNOJ, Operation Rosselsprung, Vis.
6. Italian armistice of September 1943: page B says only that two Italian divisions joined the Montenegrin Partisans; the land the Partisans took in Dalmatia, Lika, the islands and Slovenia is not on the pages opened.
7. /ledger/8 (1944 NDH interior, confidence 1) and /ledger/14 (Syrmian Front end, confidence 1) remain bridges; the Syrmian Front broke in April 1945, after this dossier's March 1945 end (the author says so).

## Cross-dossier matrix
| event (yugoslav-partisans) | counterpart | mirror | status |
| --- | --- | --- | --- |
| 1941-09 gain Zlatiborski (Uzice) | nazi-germany | none; nazi-germany /ledger/26 holds Serbia as occupation_start yugoslavia 1941-04 | exception: stand-in for serbia-under-german-occupation (listed, eu-21-x not run) |
| 1941-11 loss Zlatiborski | nazi-germany | none | exception (same) |
| 1942-11 gain Una-Sana (Bihac) | independent-state-of-croatia | dossier not written | exception: eu-21 part not run |
| 1943 loss Una-Sana | independent-state-of-croatia | dossier not written | exception |
| 1944 gain Montenegro | nazi-germany | none: nazi-germany has no 1943-44 occupation of Montenegro | exception for this dossier (montenegro-under-axis-occupation listed); route to eu-21-c / eu-21-x |
| 1944 gain NDH interior (bridge) | independent-state-of-croatia | not written | exception |
| 1944-10 gain Belgrade | nazi-germany | nazi-germany /ledger/67 1945-01 occupation_end Serbia, counterpart yugoslavia | mismatch: counterpart and type (occupation_end vs loss), dates within one year |
| 1944-12 gain Serbia | nazi-germany | same /ledger/67 | mismatch (same) |
| 1944-12 gain North Macedonia | principality-of-bulgaria | principality-of-bulgaria /ledger/38 1944 occupation_end, counterpart yugoslavia (confidence 1) | mismatch: Bulgaria treats Vardar Macedonia as occupation, page B says 'Bulgaria formally annexed these territories on 14 May 1941'; route to eu-18 |
| 1944-12 gain Dalmatia | independent-state-of-croatia | not written | exception |
| 1944-12 contest_start Syrmia | nazi-germany | none | contest, no mirror required; noted |
| (albania /ledger/20) 1944 loss Kosovo to yugoslav-partisans | albania | no gain in this dossier | missing: gap-filler for yugoslav-partisans |
| 1945-03 dissolve -> successor yugoslavia | yugoslavia | dossier not written | exception |

## Notes read
The author's notes flag every gap above except the 1941 mis-dating, the Uzice extent on the Republic of Uzice page, the Foca-land inconsistency and the missing wars. No data/README.md known-bad row concerns this state.
