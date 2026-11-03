# Review of batch eu-18-f (2026-10-31)

Reviewer: adversarial review, Phase B. Machine copy: history/notes/phase-b/reviews/eu-18-f.json.
Mechanical check: validate_dossier.py --resolve gave 0 errors and 0 warnings for all four dossiers, both before and after the reviewer's fixes.
Neighbours read: republic-of-venice, ottoman-empire, kingdom-of-hungary, serbian-empire, principality-of-wallachia, principality-of-bulgaria, despotate-of-epirus, russian-empire, habsburg-monarchy, house-of-habsburg, albania, principality-of-valona, banate-of-bosnia. Not written yet (skipped as "group not run"): austria-hungary, montenegro, first-french-empire, serbian-despots, kingdom-of-serbia, yugoslavia and others.
principality-of-valona-and-kanina: no dossier, on purpose. principality-of-valona.json lists both Names and reviews both 1395/1415 shapes (checked).

## kingdom-of-bosnia: fix (applied by the reviewer)
- /ledger/3 and /ledger/4: Zadar removed from the 1390 gain and 1391 loss. The Tvrtko I page says Zadar was "the only Dalmatian city that had evaded his rule".
- /ledger/10: year 1449 changed to 1448, to match keyframe kingdom-of-bosnia_1448 and the duchy's found event (Duchy page infobox "Established: 1448").
- Spot checks confirmed: 1385 Kotor, July 1387 Klis, May 1390 surrender (date), 25 May 1463 fall (Stephen Tomasevic page). No area in the infobox.
- Thin, within budget: the 1391 confidence-1 bridging loss (try Stephen_Dabiša); the unexplained Cliopatria cell changes of 1395, 1415 (-1,417 km2, eastern edge, probably Srebrenica/Podrinje) and 1422; the Banate of Jajce placeholder.
- Routed: kingdom-of-hungary.json (eu-15) has no mirror for the 1385, 1387 and 1390 gains or the 1391 loss.

## republic-of-ragusa: fix (applied by the reviewer)
- /keyframe_review/5 and /6 (1772, 1807): verdict changed from ok to adjust. Their notes said the Pelješac and Mljet addition still applies, but with "ok" the map would have dropped Ston, Pelješac and Mljet for 1772-1808. They now carry the same union correction as 1385-1771.
- New /ledger/8 and /ledger/11: occupation_start 1806-5 and occupation_end 1808-1, counterpart first-french-empire, confidence 3. Page: infobox "Invasion by France: 26 May 1806"; "General Lauriston took possession of the City and Republic of Ragusa, on the 27th of May"; Marmont's 1808 abolition. The schema has the owner record an occupation with the roles reversed.
- Notes cited "S6" (the Duchy of Saint Sava page) and "S11" (no such source) for quotes that are on S1, Republic_of_Ragusa. Relabelled in /ledger/9 and keyframes 1429 and 1807. The top-level notes field still cites S11 and S9: cosmetic.
- Spot checks confirmed: 1399 Primorje, 24 June 1419 and 31 December 1426 Konavle, 1451 and 1454 Herceg Stjepan's war, 27 May - 1 October 1806 siege, 31 January 1808 annexation. No area on the page.
- Thin: the 1699 Neum/Sutorina cession is on the page ("ceded two patches of its coast") and is not a ledger event (sub-cell); no acquisition date for Mljet.
- Routed: Hungarian suzerainty 1358-1458 and Ottoman tribute from 1458 are missing from the suzerains' dossiers. republic-of-venice uses counterpart republic-of-ragusa in 1030 and 1205, before this dossier starts.

## duchy-of-saint-sava: pass
- What I tried: every confidence-3 event against the Duchy and Stjepan Vukcic pages: 1451 attack, 1454 peace, 1463 cession "north of Blagaj", 1465 east, autumn 1481 siege of Novi, 1482 end (infobox; the Bosnia page's December 1481 is noted). All confirmed. Founding in 1448 agrees with the Bosnia dossier (after the reviewer's 1449->1448 fix there). Moving Cliopatria's Herzegovina rump (1463-1481) from the kingdom to the duchy is argued from the pages and consistent across the two dossiers.
- Thin, within budget: the 1463 and 1465 sub-shapes are placeholders. From 1467 the duchy is drawn as Novi only, but the page has "by 1467, much of the Duchy was occupied" and "gradually reduced to the region of Novi" only after the 1470 treaty.
- Routed: ottoman-empire.json /ledger/55 (1482 gain) names kingdom-of-bosnia but should name duchy-of-saint-sava. The duchy's 1463, 1465 and 1467 losses have no Ottoman mirror.

## serbs: fail (back to the author)
Applied by the reviewer:
- /identity/rulers: added Mihailo Obrenović III 1839-1842 (Principality page) to close the 1839-1842 gap.
- /ledger/15/note: the 48,300 -> 87,780 km2 quote is on the Treaty of Bucharest page, not the Kingdom page. Attribution corrected.
Not applied (blocking):
1. No occupation events for 1915-1918. Kingdom page: "In 1915 Serbia was occupied by foreign troops after a combined invasion by Austro-Hungarian, German, and Bulgarian troops". principality-of-bulgaria.json records occupation_start 1915-10 and occupation_end 1918-9 with counterpart serbs. Add pairs for principality-of-bulgaria and austria-hungary (and german-empire if a page gives it a zone), with liberation dates from a page (Serbian_campaign_(World_War_I), Military_Governorate_of_Serbia).
2. Vojvodina's union in November 1918 is missing. Kingdom page lead: "At the end of World War I in 1918 it united with Vojvodina and the Kingdom of Montenegro". Add a 1918-11 gain (Syrmia; Banat, Bačka and Baranja) and include it in the 1918 keyframe and the dissolve region.
3. /ledger/13: the 1913 "loss" of northern Albania to albania (confidence 1) is land Serbia only occupied, already closed by /ledger/14's occupation_end. albania.json has no gain. Delete it, or split the occupation_end if a page dates the withdrawal.
4. /wars: the Serbo-Bulgarian War of 14-28 November 1885 is missing (Kingdom page; Bulgaria's dossier has the contest pair). The WWI entry covers 1915 only; check its years on the page.
- Spot checks confirmed: 8 January 1807 Belgrade capital, October 1813 collapse, 1878 gains (Niš, Pirot, Leskovac, Vranje; independence), 6 March 1882 kingdom, 1913 annexations, 10 August 1913 Bucharest, 28 November 1918 Montenegro.
- Area: Principality infobox 24,440 km2 (1815) vs Cliopatria 41,371 (ratio 1.69, acknowledged and corrected); 37,511 (1834) ratio 1.10; 1913: 87,780 vs 88,969.
- Note: the Bucharest page credits the whole 48,300 -> 87,780 increase to the August 1913 settlement. Dating the main gain to the Treaty of London (May 1913, confidence 2) is a defensible choice, not a fault.
- Splitting into three dossiers is not needed: one state, with rename events.
- Cross-dossier: the Cliopatria row "serbia" (1918, eu-21-a) is this state's Macedonia in 1918. albania.json uses counterpart "serbia" for November 1918. The Ottoman mirrors for 1833, 1878 and 1913 are missing. The 1912-1913 events are an occupation on this side and a contest on the Ottoman side. The 1913 gain from principality-of-bulgaria has no loss there.
