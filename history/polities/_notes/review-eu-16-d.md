# Review of batch eu-16-d (2026-10-31)

Validator (--resolve): 0 errors in all six; one warning (Halych /ledger/4 counterpart principality-of-zvenyhorod has no dossier, listed). Pages read with WebFetch: Principality of Halych, Béla III of Hungary, Roman the Great, Principality of Minsk, Principality of Drutsk, Principality of Vitebsk, Principality of Jersika, Principality of Koknese. None of the six infoboxes gives an area, so no area ratio could be taken; every author said so.

Verdicts: Halych fix (reviewer applied 1, 1 left for the author), Minsk pass, Drutsk pass, Vitebsk FAIL, Jersika pass, Koknese fix (applied).

## principality-of-halych: fix
- FIX /ledger/7/counterpart (applied by reviewer): The 1199 merge named principality-of-volhynia, but identity.successors, the Volhynia dossier (1199 merge into principality-of-galicia-volhynia) and the Galicia-Volhynia dossier (1199 found, predecessors volhynia and halych) all put the land in principality-of-galicia-volhynia. Evidence: Roman the Great page: 'In 1199, after the death of Prince Volodymyr Yaroslavych of Halych, Roman captured the Galician throne for the second time' ... 'creating the Principality of Galicia-Volhynia.' Fix: counterpart principality-of-galicia-volhynia (reviewer note appended to the event note).
- FIX /ledger/4/region (author to do): The 1145 Zvenyhorod gain is drawn as the whole L'viv oblast (about 21,800 km2), and the same land is already inside the 1141 found region and the 1141 keyframe (union of Peremyshl 1139 and Terebovlia 1139, text 'Przemyśl, Terebovlia and Zvenyhorod'), so Zvenyhorod is counted twice and is Halych's 1141-1144 although the page has it apart. Evidence: Principality of Halych page: Zvenyhorod 'was granted to his nephew Ivan Berladnyk'; 'In 1145, while Volodymyrko was absent, the citizens of Halych supported Ivan Berladnyk's attempt to seize the throne'; 'After Berladnyk's defeat outside Halych, the Principality of Zvenyhorod was incorporated into the Galician lands.' Fix: Make the 1145 region a disc round Zvenyhorod (lon/lat from a page; gazetteer lacks the place) instead of the oblast, and subtract the same disc from /keyframe_review/0/correction and /ledger/0/region for 1141-1144 (drop 'Zvenyhorod' from the found text); or, if the author keeps Zvenyhorod inside from 1141, turn the 1145 event into a note.
- THIN /identity/end: Galicia 1205-1238: the principality-of-galicia-volhynia dossier loses Galicia to principality-of-halych in 1205 and 1213 and regains it in 1211, but this dossier ends in 1199, so nobody draws Galicia in 1205-1211 and 1213-1230. Either this dossier gains a second span (Igorevichi 1206-1211, Volodyslav Kormylchych 1213-1214, the 1214 Hungarian-Polish partition, Hungarian rule to 1221, Mstislav the Bold) or the G-V dossier must name other counterparts; the orchestrator decides. Try: https://en.wikipedia.org/wiki/Principality_of_Halych
- THIN /ledger/4: Coordinates and extent of the Principality of Zvenyhorod (1085/1124-1145). Try: https://en.wikipedia.org/wiki/Principality_of_Zvenyhorod
- checked /ledger/0 on https://en.wikipedia.org/wiki/Principality_of_Halych: confirmed
- checked /ledger/4 on https://en.wikipedia.org/wiki/Principality_of_Halych: confirmed (1145 Berladnyk bid; incorporation undated, follows it)
- checked /ledger/5 on https://en.wikipedia.org/wiki/B%C3%A9la_III_of_Hungary: confirmed
- checked /ledger/7 on https://en.wikipedia.org/wiki/Roman_the_Great: confirmed (counterpart corrected)
- area: infobox none; Cliopatria 106341.6 km2. Infobox has no area or years (read); the author says so in K1.

## principality-of-minsk: pass
- THIN /ledger/3: Year Minsk absorbed Drutsk (page: 'second half of the 13th century'); 1260 is Cliopatria's year, confidence 1. Try: https://en.wikipedia.org/wiki/Drutsk
- THIN /keyframe_review/6: Extent 1250-1259 (bridged at confidence 1). Try: https://en.wikipedia.org/wiki/Mindaugas
- THIN /keyframe_review/11: Extent 1314-1326 and the 1326 Vasily treaty context (bridged at confidence 1). Try: https://en.wikipedia.org/wiki/Gediminas
- checked /ledger/1 on https://en.wikipedia.org/wiki/Principality_of_Minsk: confirmed ('In 1116, he started a war with Vladimir II Monomakh ... and sacked the town of Slutsk')
- checked /ledger/2 on https://en.wikipedia.org/wiki/Principality_of_Minsk: confirmed ('where he died in September 1119')
- checked /ledger/3 on https://en.wikipedia.org/wiki/Principality_of_Drutsk: confirmed undated ('in the second half of the 13th century'); confidence 1 is honest
- checked /ledger/4 on https://en.wikipedia.org/wiki/Principality_of_Minsk: confirmed ('then fell under de facto annexation in 1326'; infobox Disestablished 1326)
- area: infobox none; Cliopatria 98754.8 km2. No infobox area. Cliopatria doubles the shape in 1260 (51,830 -> 98,755 km2); the author measured it as Minsk + Drutsk + the whole Vitebsk/Polotsk core and removes the core (about 73,600 km2 left), consistent with the Polotsk dossier holding the core to 1307.

## principality-of-drutsk: pass
- THIN /ledger/3: Year of the takeover by Minsk (page: 'second half of the 13th century'); 1259 and the 1250-1259 keyframe are bridging at confidence 1. Try: https://en.wikipedia.org/wiki/Drutsk
- THIN /identity/capitals/0: Coordinates of Drutsk (placeholder is the shape centroid 54.14N 29.637E). Try: https://en.wikipedia.org/wiki/Drutsk
- checked /ledger/0 on https://en.wikipedia.org/wiki/Principality_of_Drutsk: confirmed ('established after the death of Vseslav ... in 1101')
- checked /ledger/1 on https://en.wikipedia.org/wiki/Principality_of_Drutsk: confirmed ('In 1116, the Principality of Drutsk was taken over by the Grand Principality of Kiev')
- checked /ledger/2 on https://en.wikipedia.org/wiki/Principality_of_Drutsk: confirmed as the princes' list year ('1140–1146: Rogvolod II of Polotzk'); conflict with 'by 1150s it was returned to Principality of Minsk' is flagged by the author
- checked /ledger/3 on https://en.wikipedia.org/wiki/Principality_of_Drutsk: confirmed undated; confidence 1 honest (infobox Disestablished 1565 is mentioned in the dossier)
- area: infobox none; Cliopatria 19977.6 km2. 

## principality-of-vitebsk: fail
- FIX /keyframe_review/0/correction, /keyframe_review/1, /keyframe_review/2, /keyframe_review/3/correction (author to do): Every keyframe draws Cliopatria's whole 'Principality of Vitebsk' shape (34,385 km2), which the author's own K1 note says 'also holds Polotsk'; Polotsk proper is drawn at the same time by the principality-of-polotsky dossier (K3, 1101-1194: the 1202 core minus a 60 km disc round Vitsyebsk), so about 27,900 km2 including the town of Polotsk is drawn twice for 94 years. The K1 verdict 'adjust' corrects only the years. Evidence: Vitebsk page: 'Sviatoslav Vseslavich inherited the lands surrounding Vitebsk'; Polotsk itself stayed with Davyd (Polotsk dossier K3 note, Vseslav page). Shapes.csv: principality-of-vitebsk_1111 and principality-of-polotsky_1202 are both 34,385.1 km2 with the same bbox 27.29-30.97E 54.95-57.08N; the Minsk dossier measures the Vitebsk shape as the whole Polotsk-Vitebsk core (164 of 164 cells). No infobox area to settle the size, so the double drawing is the deciding fact. Fix: Set K1 (and K2) to verdict 'wrong' (or adjust) with correction = the Vitebsk fief only, matching the Polotsk dossier: {"place": "Vitsyebsk", "km": 60, "text": "the lands surrounding Vitebsk"} (or the Cliopatria Vitebsk shape minus the Polotsk K3 region); use the same region in K0 and K3 and in /ledger/0-8 (found, 1129 loss, 1132 gain, 1165 loss, 1168 gain, 1186-1195 contest, 1195 merge, dissolve) and in identity.predecessors/successors land; say in the note that Cliopatria's row is the Polotsk-Vitebsk core.
- FIX /identity/rulers (author to do): Rulers overlap: Vseslav Vasilkovich 1132-1164 with Roman Vyacheslavich 1162-1165, and Briachislav Vasilkovich 1178-1181 with Vseslav Vasilkovich 1180-1186. Evidence: Brief section 2.9: rulers are contiguous. Fix: Make the spans contiguous (e.g. Vseslav to 1162, Briachislav to 1180) or say in a note that the page's list overlaps.
- THIN /identity/end: Vitebsk 1195-1320 under its own princes as a Polotsk then Lithuanian dependency (page: 'nominally inherited into the Grand Duchy of Lithuania in 1320', infobox 1508); the Lithuanian dossier's 1318 gain names principality-of-vitebsk as counterpart. Try: https://en.wikipedia.org/wiki/Principality_of_Vitebsk
- checked /ledger/1 on https://en.wikipedia.org/wiki/Principality_of_Vitebsk: confirmed ('During the new campaigning in 1129 ... annexed Polotsk and its vassals including Vitebsk')
- checked /ledger/3 on https://en.wikipedia.org/wiki/Principality_of_Vitebsk: confirmed ('In 1165–1167 ... the principality of Vitebsk was shortly acquired by the princes of Smolensk')
- checked /ledger/6 on https://en.wikipedia.org/wiki/Principality_of_Vitebsk: confirmed ('who in 1195 marched against the prince of Smolensk')
- checked /ledger/7 on https://en.wikipedia.org/wiki/Principality_of_Vitebsk: confirmed ('Vitebsk again fell under the rule of Polotsk'); region wrong (see fixes)
- area: infobox none; Cliopatria 34385.1 km2. No infobox area. The drawn shape is the whole Polotsk-Vitebsk core, about 5x the 60 km Vitebsk disc (about 6,500 km2) the Polotsk dossier leaves for Vitebsk; noted by the author but not resolved.

## principality-of-jersika: pass
- THIN /ledger/0: Founding year: 1111 is Cliopatria's (confidence 1); page offers 1041 (saga), infobox 1041/1190, first mention 1203; the Polotsk dossier splits Jersika off in 1101. Try: https://en.wikipedia.org/wiki/Visvaldis
- THIN /keyframe_review/3: Extent of Visvaldis's fief 1216-1239 after the 1211 division and 1214 sack (bridged at confidence 1). Try: https://en.wikipedia.org/wiki/Visvaldis
- THIN /identity/capitals/0: Coordinates of the Jersika hill fort (placeholder is the shape centroid 56.562N 26.563E). Try: https://en.wikipedia.org/wiki/Jersika_Castle
- checked /ledger/0 on https://en.wikipedia.org/wiki/Principality_of_Jersika: not on page (1111 absent) but confidence 1 and the note says so: a gap, not a fabrication
- checked /ledger/1 on https://en.wikipedia.org/wiki/Principality_of_Jersika: confirmed ('In 1209, Visvaldis ... was defeated by the bishop Albert of Riga and the Livonian Brothers of the Sword'; 'He lost the lands of Autīne and Cesvaine')
- checked /ledger/2 on https://en.wikipedia.org/wiki/Principality_of_Jersika: confirmed ('After the death of Visvaldis in 1239, his fief passed to the Livonian Order')
- area: infobox none; Cliopatria 23422.4 km2. 

## principality-of-koknese: fix
- FIX /ledger/1/confidence, /ledger/2/confidence (applied by reviewer): The 1209 loss and dissolve were at confidence 3, but the page gives no firm year. Evidence: Koknese page: 'By 1209 Koknese had been taken over by the Brothers of the Sword'; infobox 'Disestablished: 1208'. Fix: confidence 2 on both (reviewer note appended).
- THIN /keyframe_review/1: The 1205 grant of half the land to Albert of Riga 'in return for protection' has no event (page gives no extent); likely a vassal_start in the archbishopric-of-riga ledger or a loss of an unnamed half. Try: https://en.wikipedia.org/wiki/Vetseke
- THIN /ledger/0: Status of the Koknese land 1101-1179: the Polotsk dossier splits Koknese off in 1101, this dossier founds it c. 1180, so the land is drawn by nobody for 79 years. Try: https://en.wikipedia.org/wiki/Koknese_Castle
- checked /ledger/0 on https://en.wikipedia.org/wiki/Principality_of_Koknese: confirmed (infobox 'Established: c. 1180', '1180–1206: Vetseke')
- checked /ledger/1 on https://en.wikipedia.org/wiki/Principality_of_Koknese: confirmed as 'By 1209' (infobox 1208); confidence lowered to 2
- checked /identity/capitals/0 on https://en.wikipedia.org/wiki/Principality_of_Koknese: confirmed ('Koknese Castle 56°42′00″N 25°28′00″E'); the shape's bbox (max 56.66N) misses it, the 15 km disc correction is justified
- area: infobox none; Cliopatria 2287.8 km2. 

## Cross-dossier matrix
- principality-of-halych 1141 merge -> principality-of-peremyshl: exception (mirror principality-of-peremyshl None None). Peremyshl dossier not written yet (another eu-16 part); it should end in 1141 with a merge into Halych, as Terebovlia does, or 1141-1146 is drawn twice.
- principality-of-halych 1141 merge -> principality-of-terebovlia: matched (mirror principality-of-terebovlia 1141 merge). 
- principality-of-halych 1145 gain -> principality-of-zvenyhorod: exception (mirror principality-of-zvenyhorod None None). No dossier; listed under counterparts_needing_dossiers.
- principality-of-halych 1188 occupation_start -> kingdom-of-hungary: matched (mirror kingdom-of-hungary 1188 occupation_start). 
- principality-of-halych 1189 occupation_end -> kingdom-of-hungary: matched (mirror kingdom-of-hungary 1190 occupation_end). One year apart; Béla III page dates Vladimir's return '1189-1190'.
- principality-of-halych 1199 merge -> principality-of-galicia-volhynia: matched (mirror principality-of-galicia-volhynia 1199 found). After the reviewer's counterpart fix (was principality-of-volhynia); G-V predecessors list Halych.
- principality-of-galicia-volhynia 1205 loss -> principality-of-halych: mismatch (mirror principality-of-halych None None). G-V loses Galicia to principality-of-halych in 1205 and 1213 and regains it in 1211, but the Halych dossier ends in 1199: Galicia has no holder in 1205-1211 and 1213-1230. Route to the orchestrator: extend Halych or re-target the G-V counterparts.
- principality-of-minsk 1116 contest_start -> kievan-rus: exception (mirror kievan-rus None None). kievan-rus dossier not written yet (eu-16).
- principality-of-minsk 1260 gain -> principality-of-drutsk: matched (mirror principality-of-drutsk 1259 merge). 
- principality-of-minsk 1326 loss -> grand-duchy-of-lithuania: mismatch (mirror grand-duchy-of-lithuania 1314 gain). Lithuania has gain and vassal_end of Minsk in 1314 (confidence 1, Cliopatria's year); the Minsk page gives 'de facto annexation in 1326' (infobox 1326). Route to eu-15: move to 1326.
- grand-duchy-of-lithuania 1250 vassal_start -> principality-of-minsk: mismatch (mirror principality-of-minsk None None). Lithuania dates the Minsk vassalage 1250 at confidence 1; the Minsk page: 'nominally annexed by the Grand Duchy of Lithuania in 1242', 'In 1242, Minsk was annexed by the Grand Duchy of Lithuania'. Route to eu-15: 1242.
- principality-of-polotsky 1101 split -> principality-of-minsk: matched (mirror principality-of-minsk 1101 found). 
- principality-of-drutsk 1116 loss -> kievan-rus: exception (mirror kievan-rus None None). kievan-rus not written yet (eu-16).
- principality-of-drutsk 1140 gain -> kievan-rus: exception (mirror kievan-rus None None). kievan-rus not written yet (eu-16).
- principality-of-polotsky 1101 split -> principality-of-drutsk: matched (mirror principality-of-drutsk 1101 found). 
- principality-of-vitebsk 1129 loss -> kievan-rus: exception (mirror kievan-rus None None). kievan-rus not written yet; note the Polotsk dossier gives the same 1129 annexation to principality-of-kiev: eu-16 must pick one counterpart for Mstislav's Kiev.
- principality-of-vitebsk 1132 gain -> kievan-rus: exception (mirror kievan-rus None None). As above (Polotsk: principality-of-kiev).
- principality-of-vitebsk 1165 loss -> principality-of-smolensk: mismatch (mirror principality-of-smolensk 1165 contest_start). Smolensk records a contest with principality-of-polotsky, not a gain from Vitebsk; Vitebsk page: 'the principality of Vitebsk was shortly acquired by the princes of Smolensk'. Smolensk should carry gain 1165 / loss 1168 with counterpart principality-of-vitebsk.
- principality-of-vitebsk 1168 gain -> principality-of-smolensk: mismatch (mirror principality-of-smolensk 1168 contest_end). As above.
- principality-of-vitebsk 1186 contest_start -> principality-of-smolensk: mismatch (mirror principality-of-smolensk 1186 contest_start). Years agree (1186-1195) but Smolensk names principality-of-polotsky as counterpart; the land is Vitebsk's until 1195.
- principality-of-vitebsk 1195 merge -> principality-of-polotsky: mismatch (mirror principality-of-polotsky 1195 gain). Year agrees; land does not: Vitebsk merges its whole 34,385 km2 shape, Polotsk gains a 60 km disc round Vitsyebsk (see the Vitebsk fail).
- principality-of-polotsky 1101 split -> principality-of-vitebsk: mismatch (mirror principality-of-vitebsk 1101 found). Year agrees; Polotsk splits off a 60 km Vitsyebsk disc, Vitebsk founds on the whole Polotsk-Vitebsk core.
- grand-duchy-of-lithuania 1318 gain -> principality-of-vitebsk: mismatch (mirror principality-of-vitebsk None None). The Vitebsk dossier ends in 1195 (land to Polotsk, which Lithuania annexes in 1307); nobody holds Vitebsk in 1318 to lose it. Route to eu-15 and the Vitebsk gap-filler (vassal span 1195-1320).
- principality-of-jersika 1209 loss -> archbishopric-of-riga: missing (mirror archbishopric-of-riga None None). Riga dossier has no Jersika event: needs the 1209 gain (Autīne, Cesvaine) and a vassal_start of the Jersika fief 1209-1239; also the 1205 Koknese protection.
- livonian-brothers-of-the-sword 1210 gain -> principality-of-jersika: mismatch (mirror principality-of-jersika 1209 loss). Jersika gives the 1209 loss to archbishopric-of-riga; the page has Albert and the Brothers together in 1209 and the conquered part divided between them in 1211. Split the land: Riga 1209, the Brothers' share 1211, both sides naming each other.
- principality-of-jersika 1239 loss -> teutonic-order: missing (mirror teutonic-order None None). Teutonic Order dossier (eu-14) has no 1239 gain of the Jersika fief ('passed to the Livonian Order').
- principality-of-polotsky 1101 split -> principality-of-jersika: mismatch (mirror principality-of-jersika 1111 found). Ten years apart; Jersika's 1111 is Cliopatria's (confidence 1), Polotsk's 1101 is the division year; the land is undrawn 1101-1110. One side must move.
- principality-of-koknese 1209 loss -> livonian-brothers-of-the-sword: mismatch (mirror livonian-brothers-of-the-sword 1210 gain). The Brothers' 1210 gain names principality-of-jersika though its note covers Koknese; add a gain with counterpart principality-of-koknese in 1209.
- principality-of-polotsky 1101 split -> principality-of-koknese: mismatch (mirror principality-of-koknese 1180 found). 79 years apart (Koknese page: 'Established: c. 1180'); the Koknese land is undrawn 1101-1179. Polotsk should keep it to 1180 or split in 1180.

## Problems
- Reviewer applied two small fixes (Halych /ledger/7 counterpart; Koknese /ledger/1-2 confidence) and re-validated both: 0 errors.
- No page failed. No per-shape grid is on the mount, so the claim that Cliopatria's Vitebsk shape contains Polotsk rests on shapes.csv (identical area and bbox to principality-of-polotsky_1202) and on the Vitebsk, Minsk and Polotsk dossiers' own measurements.
- Galicia 1205-1230 has no holder: principality-of-galicia-volhynia loses it to principality-of-halych, which ends in 1199; needs an orchestrator decision.
- eu-16 uses both kievan-rus (Drutsk, Vitebsk, Minsk) and principality-of-kiev (Polotsk) for Mstislav's 1129 annexation and Monomakh's wars; neither dossier exists yet.
