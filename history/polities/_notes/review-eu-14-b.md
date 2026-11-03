# Review of batch eu-14-b (viking-settlements)

Reviewer, 2026-10-25. Verdict: **fail** (one blocking finding, fix 1; the rest are fixes). Two small fixes applied by the reviewer (slug kievan-rus -> rus; /ledger/29 confidence and note), dossier re-validated: 0 errors, 0 warnings.

Pages re-read: Danelaw, Kingdom of Dublin, Alan II Duke of Brittany, Viking expansion, Vikings, Scandinavian Scotland. Every confidence-3 event checked (11, 16, 22, 23, 27, 37, 41, 42, 43, 45, 52, 53, 67) is on its page with its year. No fabrication found.

## Findings

1. `/ledger/61 and /keyframe_review (viking-settlements_990, _1000, _1003, _1018, _1028, _1040 corrections)` (open): The Hebrides, Skye, Argyll and the Isle of Man (27 cells) are given to old-kingdom-of-norway in 990 on a computed Cliopatria overlap, so the corrections drop them from 990 on; no dossier holds them 990-1079/1085.
   - Why: Scandinavian Scotland (the event's own source, re-read 2026-10-25): Hebrides under Scandinavian rulers from 'at least the late tenth century', 'Magnus Barelegs re-established direct Norwegian overlordship there by 1098', 'Godred Crovan became the ruler of Dublin and Mann from 1079'. old-kingdom-of-norway's keyframe _990 cuts the same isles ('None of the nine pages opened puts these islands under Norway before 1098 ... Before 1098 Cliopatria's Viking set[tlements row holds them]') and has no 990 gain; kingdom-of-the-isles /ledger/1 is '1085 gain viking-settlements' (Hebrides) with no mirror here. The land is orphaned for about 90 years. Blocking.
   - Fix: Delete /ledger/61. Keep the 27 cells in the corrections of _990, 1000, 1003, 1018, 1028 and _1040 (and a new keyframe if needed) until they go: add '1079 loss kingdom-of-the-isles' for the Isle of Man (Scandinavian Scotland: 'Godred Crovan became the ruler of Dublin and Mann from 1079', confidence 2) and '1085 loss kingdom-of-the-isles' for the Hebrides, Skye and Argyll (confidence 1, the Isles dossier's year, Cliopatria's shape). Rewrite the keyframe notes that cite the Norway overlap.

2. `/ledger/43, /ledger/49, /keyframe_review (viking-settlements_911 correction)` (open): Rouen and the lower Seine are held by this dossier 911-921 and by duchy-of-normandy from 911: a double claim.
   - Why: Viking expansion (opened): 'In 911 Rollo entered vassalage to Charles the Simple through the Treaty of Saint-Clair-sur-Epte.' duchy-of-normandy /ledger/0 is '911 found west-franks' (c3) and west-franks /ledger/23 is '911 loss duchy-of-normandy' (c3); duchy-of-normandy has no 922 gain from viking-settlements, so /ledger/49 has no mirror.
   - Fix: Either drop /ledger/43 and /ledger/49 and correct keyframe viking-settlements_911 (911-921) to the Cliopatria shape without the 36 Normandy cells, noting that the duchy-of-normandy dossier carries Rollo's land from 911; or, if the authors of both dossiers agree that the Viking row should hold it to 921, get duchy-of-normandy and west-franks changed. The first is consistent with the page (vassalage, the start of the county of Rouen).

3. `/ledger/46, /ledger/47, /ledger/52, /ledger/53, /ledger/54` (open): The Brittany episode is turned from an occupation into a gain in 922 on Cliopatria alone, and the 936-939 events name duchy-of-brittany as counterpart although that dossier starts in 939.
   - Why: Alan II, Duke of Brittany (opened): 'He expelled the Vikings/Norsemen from Brittany after an occupation that lasted from 907 to about 939'; 'In 938, Alan was elected Brittonum dux'. kingdom-of-brittany lives to 939 and has '919 occupation_start viking-settlements' and '937 occupation_end viking-settlements' (both c3); duchy-of-brittany /ledger/0 is '939 found kingdom-of-brittany'. A 937 loss to a polity founded in 939 has no possible mirror.
   - Fix: Delete /ledger/46 and /ledger/47 (the 922 conversion); keep /ledger/42 as the occupation of kingdom-of-brittany running to 937 (occupation_end, counterpart kingdom-of-brittany, for Brittany except the Loire estuary) and 939 (occupation_end for the Loire estuary, counterpart kingdom-of-brittany or duchy-of-brittany per the 1 August 939 Trans-la-Foret victory); set /ledger/52's counterpart to kingdom-of-brittany. Correct keyframes 922, 926, 936, _938, _940 to drop the Brittany cells from the Viking territory: research-brief rule 4 draws occupied land hatched from the occupation events, so the occupation carries them. The 907 against 919 start (kingdom-of-brittany's page) stays a flagged disagreement.

4. `/ledger/51` (open): The Cotentin passes to duchy-of-normandy in 936 here, in 933 from kingdom-of-brittany in both neighbours.
   - Why: duchy-of-normandy /ledger/2: '933: William Longsword is granted the Cotentin and the Avranchin' (c3, counterpart kingdom-of-brittany); kingdom-of-brittany /ledger/7: '933 loss duchy-of-normandy' (c3). This event is confidence 1, page silent.
   - Fix: If the Brittany cells are no longer Viking territory (previous finding), delete /ledger/51 and drop the Cotentin with them; otherwise move it to 933 with counterpart duchy-of-normandy.

5. `/ledger/8, /keyframe_review/5 (viking-settlements_840)` (open): The note says the source page dates no settlement in the Inner Hebrides; the page dates their conquest to 847.
   - Why: Scandinavian Scotland: 'The Frankish Annales Bertiniani may record the conquest of the Inner Hebrides by Vikings in 847.' dal-riata /ledger/6 is '847 loss viking-settlements' (c2). Mis-dated at confidence 1: a fix, not a fail.
   - Fix: Year 847, confidence 2, quote the sentence; mark keyframe 840 adjust (the 840 shape without the Inner Hebrides and Argyll cells for 840-846) or add a new keyframe _847.

6. `/ledger/29` (applied): The note said the Danelaw page was silent on Wessex before Edington; the page's timeline has '875 - The Danes settled in Dorset' and Wareham in 876.
   - Why: Danelaw timeline: '875 - The Danes settled in Dorset, well inside Alfred's Kingdom of Wessex, but Alfred quickly made peace with them.' '876 - The Danes broke the peace when they captured the fortress of Wareham, followed by a similar capture of Exeter in 877.'
   - Fix: Reviewer applied: confidence 1 -> 2, note quotes the two timeline entries. Year 875 kept (the page's Dorset settlement).

7. `/ledger/30` (open): Exeter is taken in 876 here; the Danelaw page has 877.
   - Why: Danelaw timeline: '... followed by a similar capture of Exeter in 877.' Confidence 1, one year off.
   - Fix: Year 877, confidence 2, quote the sentence; keyframe 876 (876-877) becomes adjust (Exeter cells only in 877).

8. `/identity/successors/1/slug and /ledger/36/counterpart` (applied): Counterpart slug kievan-rus names a Cliopatria row whose dossier is rus (one dossier for the rows Rus' and Kievan Rus').
   - Why: history/polities/rus.json identity: slug rus, cliopatria_names ["Rus'", "Kievan Rus'"], 880-1054; there is no kievan-rus.json and the shared-Wikidata rule puts both rows under the earlier slug.
   - Fix: Reviewer applied: kievan-rus -> rus in both places; re-validated with --resolve (0 errors, 0 warnings).

9. `/ledger/65, /keyframe_review/37 (viking-settlements_1040)` (open): The Faroes pass to Norway in 1040 (computed overlap, confidence 1); the Norway dossier has them from 1035 on a page.
   - Why: old-kingdom-of-norway /ledger/14: '1035 gain viking-settlements', History of the Faroe Islands page: 'The Faroes became a part of the Kingdom of Norway in 1035' (c3).
   - Fix: Move /ledger/65 to 1035, cite History of the Faroe Islands (add to sources), confidence 2; start keyframe _1040 in 1035 (rename _1035) and limit the 1028 correction to 1028-1034.

10. `/ledger/40, /ledger/44` (open): The Kent occupation runs 892-911 on Cliopatria's shape; the Wessex dossier ends the fighting in 896.
   - Why: kingdom-of-wessex /ledger/27 '892 contest_start viking-settlements' and /ledger/28 '896 contest_end viking-settlements: the Viking army disperses ... in 896 (or 897)'. This dossier's events are confidence 1, page silent.
   - Fix: Open the Wessex dossier's page (or Alfred the Great) and end the Kent occupation in 896 unless a page keeps a Danish foothold in Kent to 910; mark keyframe 892 adjust for 897-910.

## Thin (for a gap-filler)

- `/ledger/0, /ledger/1, /ledger/4, /ledger/6, /ledger/20`: Ladoga, Rostov, Beloozero, the Mecklenburg coast (possibly Obotrite land), Rugen and the Peene mouth: no dated sentence; all confidence 1. Try https://en.wikipedia.org/wiki/Staraya_Ladoga
- `/ledger/2, /ledger/3`: Shetland and the Faroes from 800: no dated sentence. Try https://en.wikipedia.org/wiki/History_of_the_Faroe_Islands
- `/ledger/7, /ledger/9, /ledger/10`: Caithness, Isle of Man and the Western Isles from 840: Scandinavian Scotland gives Man 877 or by 900. Try https://en.wikipedia.org/wiki/Kingdom_of_the_Isles
- `/ledger/13, /ledger/14, /ledger/15, /ledger/17, /ledger/18, /ledger/59`: Bayonne, the Garonne mouth, Limerick, Waterford, Truso: no page; Viking expansion founds the Irish towns after 914, against Cliopatria's 850/860. Try https://en.wikipedia.org/wiki/Norse%E2%80%93Gaels
- `/ledger/21`: Lincolnshire cluster 866. Try https://en.wikipedia.org/wiki/Great_Heathen_Army
- `/ledger/31, /ledger/32, /ledger/33, /ledger/35`: Chippenham 878-880 and the end of the Wessex footholds. Try https://en.wikipedia.org/wiki/Alfred_the_Great
- `/ledger/38, /ledger/39`: Seine-Oise cluster 886-891. Try https://en.wikipedia.org/wiki/Siege_of_Paris_(885%E2%80%93886)
- `/ledger/56, /ledger/57, /ledger/58, /ledger/62`: Mecklenburg 947, the Oder mouth and Wolin/Jomsborg 947-1000: Vikings gives Jomsborg 'between the 960s and 1043'. Try https://en.wikipedia.org/wiki/Jomsborg
- `/ledger/64`: End of L'Anse aux Meadows (1022, one-year keyframe). Try https://en.wikipedia.org/wiki/L%27Anse_aux_Meadows
- `/ledger/66, /ledger/68`: Greenland to Norse Greenland 1072 (computed) and the fall of Waterford, Wexford, Cork, Limerick in 1171 (the Angevin dossier has Henry II take Wexford and Waterford in 1171; Cork and Limerick undated). Try https://en.wikipedia.org/wiki/Norse_Greenland

## Spot checks

- `/ledger/22` https://en.wikipedia.org/wiki/Danelaw: confirmed
- `/ledger/23` https://en.wikipedia.org/wiki/Danelaw: confirmed
- `/ledger/34` https://en.wikipedia.org/wiki/Danelaw: confirmed
- `/ledger/41` https://en.wikipedia.org/wiki/Kingdom_of_Dublin: confirmed
- `/ledger/45` https://en.wikipedia.org/wiki/Kingdom_of_Dublin: confirmed
- `/ledger/67` https://en.wikipedia.org/wiki/Kingdom_of_Dublin: confirmed
- `/ledger/42` https://en.wikipedia.org/wiki/Alan_II,_Duke_of_Brittany: confirmed
- `/ledger/53` https://en.wikipedia.org/wiki/Alan_II,_Duke_of_Brittany: confirmed
- `/ledger/11` https://en.wikipedia.org/wiki/Viking_expansion: confirmed
- `/ledger/37` https://en.wikipedia.org/wiki/Viking_expansion: confirmed
- `/ledger/43` https://en.wikipedia.org/wiki/Viking_expansion: confirmed
- `/ledger/27` https://en.wikipedia.org/wiki/Scandinavian_Scotland: confirmed
- `/ledger/36` https://en.wikipedia.org/wiki/Vikings: confirmed
- `/ledger/8` https://en.wikipedia.org/wiki/Scandinavian_Scotland: mis-dated
- `/ledger/29` https://en.wikipedia.org/wiki/Danelaw: confirmed
- `/ledger/30` https://en.wikipedia.org/wiki/Danelaw: mis-dated
- `/ledger/61` https://en.wikipedia.org/wiki/Scandinavian_Scotland: not on page

## Area

Vikings has no infobox area; Cliopatria max 134,483 km2 (876). Acknowledged by the author.

## Cross-dossier matrix

- viking-settlements 840 gain dal-riata -> dal-riata 847 loss: **mismatch**. Dal Riata 847 (c2, page); this dossier 840 (c1). See fix /ledger/8.
- viking-settlements 850 gain middle-franks -> middle-franks None None: **missing**. Frisia c. 850 (c3, page); middle-franks (843-855) has no Frisia loss: route to eu-07.
- viking-settlements 850 gain west-franks -> west-franks None None: **missing**. Garonne mouth (c2); no mirror in west-franks.
- viking-settlements 850 gain west-franks -> west-franks None None: **missing**. Bayonne (c1); no mirror.
- viking-settlements 860 loss west-franks -> west-franks None None: **missing**. Garonne and Bayonne return (c1); no mirror.
- viking-settlements 866 gain kingdom-of-mercia -> kingdom-of-mercia None None: **exception**. No dossier yet; eu-11 has not written it.
- viking-settlements 867 gain kingdom-of-northumbria -> kingdom-of-northumbria None None: **exception**. No dossier yet (eu-11).
- viking-settlements 869 gain kingdom-of-east-anglia -> kingdom-of-east-anglia 869 dissolve: **matched**. East Anglia /ledger/7 dissolve viking-settlements 869.
- viking-settlements 874 gain kingdom-of-mercia -> kingdom-of-mercia None None: **exception**. No dossier yet (eu-11).
- viking-settlements 875 loss old-kingdom-of-norway -> old-kingdom-of-norway 875 gain: **matched**. Northern Isles, both c3.
- viking-settlements 875 loss old-kingdom-of-norway -> old-kingdom-of-norway 875 gain: **matched**. Caithness and Sutherland.
- viking-settlements 875 occupation_start kingdom-of-wessex -> kingdom-of-wessex 876 contest_start: **mismatch**. Type differs (occupation here, contest in Wessex); Danelaw page has Dorset 875 and Wareham 876.
- viking-settlements 876 occupation_start kingdom-of-wessex -> kingdom-of-wessex 876 contest_start: **mismatch**. Exeter: page says 877; Wessex records a contest, not an occupation.
- viking-settlements 878 occupation_end kingdom-of-wessex -> kingdom-of-wessex 878 contest_end: **mismatch**. Year matches; type differs.
- viking-settlements 878 occupation_start kingdom-of-wessex -> kingdom-of-wessex None None: **missing**. Chippenham 878-880: no occupation in Wessex.
- viking-settlements 878 loss danelaw -> danelaw None None: **exception**. No dossier yet (eu-11).
- viking-settlements 880 occupation_end kingdom-of-wessex -> kingdom-of-wessex None None: **missing**. No mirror.
- viking-settlements 882 loss rus -> rus 880 found: **mismatch**. Slug fixed from kievan-rus. rus /ledger/0 founds the state c. 880 from nobody with Oleg at Novgorod, while this dossier holds Novgorod to 881; rus has no gain from viking-settlements. Route to eu-16.
- viking-settlements 885 loss west-franks -> west-franks None None: **missing**. Frisia; page names Gerolf of Holland, Cliopatria the West Franks from 886; west-franks has no Frisia gain.
- viking-settlements 886 occupation_start west-franks -> west-franks None None: **missing**. Seine-Oise cluster.
- viking-settlements 892 occupation_end west-franks -> west-franks None None: **missing**. Seine-Oise cluster.
- viking-settlements 892 occupation_start kingdom-of-wessex -> kingdom-of-wessex 892 contest_start: **mismatch**. Kent: type differs.
- viking-settlements 911 occupation_end kingdom-of-wessex -> kingdom-of-wessex 896 contest_end: **mismatch**. Wessex ends the fighting in 896; this dossier keeps Kent to 910.
- viking-settlements 902 loss native Irish (Leinster) -> kingdom-of-leinster None None: **exception**. Listed in the author's counterparts_needing_dossiers.
- viking-settlements 907 occupation_start kingdom-of-brittany -> kingdom-of-brittany 919 occupation_start: **mismatch**. 907 (Alan II page) against 919 (Kingdom of Brittany's page, c3): both pages; flagged by the author.
- viking-settlements 911 gain west-franks -> west-franks 911 loss: **mismatch**. west-franks gives Rouen to duchy-of-normandy (found 911), not to viking-settlements: double claim 911-921.
- viking-settlements 917 gain native Irish (Leinster) -> kingdom-of-leinster None None: **exception**. As 902.
- viking-settlements 922 occupation_end kingdom-of-brittany -> kingdom-of-brittany 937 occupation_end: **mismatch**. Kingdom of Brittany keeps the occupation to 937.
- viking-settlements 922 gain kingdom-of-brittany -> kingdom-of-brittany None None: **missing**. No 922 loss in kingdom-of-brittany (it lives to 939).
- viking-settlements 922 loss duchy-of-normandy -> duchy-of-normandy 911 found: **mismatch**. Normandy founded from west-franks in 911; no gain from viking-settlements.
- viking-settlements 930 loss icelandic-commonwealth -> icelandic-commonwealth 930 found: **matched**. Year agrees; the commonwealth's found names counterpart nobody.
- viking-settlements 936 loss duchy-of-normandy -> duchy-of-normandy 933 gain: **mismatch**. Cotentin: Normandy gains it from kingdom-of-brittany in 933 (c3).
- viking-settlements 937 loss duchy-of-brittany -> kingdom-of-brittany 937 occupation_end: **mismatch**. duchy-of-brittany starts 939; kingdom-of-brittany ends the occupation in 937.
- viking-settlements 939 loss duchy-of-brittany -> duchy-of-brittany 939 found: **mismatch**. duchy-of-brittany founds from kingdom-of-brittany, not viking-settlements.
- viking-settlements 947 loss kingdom-of-germany -> kingdom-of-germany 947 gain: **mismatch**. Germany's 947 events are a vassal_start of the Obotrites and a gain from nobody; neither names viking-settlements.
- viking-settlements 980 loss kingdom-of-poland -> kingdom-of-poland None None: **exception**. No dossier yet (eu-15).
- viking-settlements 990 loss old-kingdom-of-norway -> old-kingdom-of-norway None None: **mismatch**. Norway explicitly cuts the isles 990-1098; blocking (fix 1).
- viking-settlements 1000 loss kingdom-of-poland -> kingdom-of-poland None None: **exception**. No dossier yet (eu-15).
- viking-settlements 1040 loss old-kingdom-of-norway -> old-kingdom-of-norway 1035 gain: **mismatch**. Faroes: Norway 1035 (c3, page).
- viking-settlements 1072 loss norse-greenland -> norse-greenland None None: **exception**. No dossier yet (eu-14, a parallel part).
- viking-settlements 1171 loss angevin-empire -> angevin-empire 1171 gain: **mismatch**. Year agrees; Angevin's counterpart is 'Kingdom of Leinster' (Dublin, Wexford, Waterford).
- viking-settlements 1171 dissolve angevin-empire -> angevin-empire 1171 gain: **mismatch**. Angevin takes Wexford and Waterford in 1171, not Cork or Limerick.
- kingdom-of-the-isles 1085 gain viking-settlements -> viking-settlements None None: **missing**. Hebrides from viking-settlements; no mirror here (fix 1). Also kingdom-of-the-isles 1079 found (Man) and 1094-1095 Dublin overlap this dossier's Dublin.
- kingdom-of-east-anglia 865 occupation_start viking-settlements -> viking-settlements None None: **missing**. Great Heathen Army in East Anglia 865-866 (East Anglia /ledger/5-6); no occupation event here.
