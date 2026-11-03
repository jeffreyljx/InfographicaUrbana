# Review of batch eu-05-e (Byzantium, part e)

Reviewed 2026-10-19 by the adversarial reviewer. Validator (--resolve): all six valid, 0 errors, 0 warnings before review. Spot checks: 4-6 events per dossier, weighted to confidence 3 and the largest land moves; every page opened said what the note claims (no fabricated events). No infobox in the batch gives an area.

| slug | verdict |
| --- | --- |
| catalan-company | fix |
| thessaly | fail |
| empire-of-thessalonica | pass |
| commune-of-the-zealots | pass |
| duchy-of-the-archipelago | fail |
| principality-of-theodoro | fail |

## catalan-company: fix

- **APPLIED by reviewer** `/ledger/10/counterpart, /ledger/12/counterpart, /ledger/13/counterpart, /identity/successors/0/slug, /wars/4/belligerents/0`: The 1388 and 1390 losses, the dissolve and the successor named 'duchy-of-athens', but the duchy-of-athens dossier ends in March 1311 (successor catalan-company), so the counterpart did not exist in 1388-1390.
  - Evidence: duchy-of-athens identity.end = 1311-03 and its notes: 'Either way Cliopatria lacks the Acciaioli Duchy of Athens (1388-1458)'. The author's own report lists acciaioli-duchy-of-athens under counterparts_needing_dossiers. Duchy of Neopatras page: 'Athens fell to Acciaioli in 1388'; 'in 1390 he captured Neopatras as well'.
  - Fix: Counterpart, successor slug and belligerent changed to 'acciaioli-duchy-of-athens' (5 lines). Re-validated: valid, 0 errors, 3 warnings, all 'looks like a slug but no polity or dossier has it' for that slug, which is expected until the Acciaioli dossier is written.
- Thin (for a gap-filler):
  - `/ledger/6/region`: Which Catalan places in Thessaly were lost to the Serbs in 1348. The region ('Thessaly' minus Neopatras) is the modern Thessalia unit, which hardly overlaps the Catalan shapes (south of 38.93 N), so the loss removes almost nothing and no keyframe shows it. The Neopatras page names Domokos, Gardiki and Pharsalus as taken 'apparently briefly' by 1325. Try https://en.wikipedia.org/wiki/Duchy_of_Neopatras
  - `/ledger/9`: Confidence-1 capital move to Athens in 1379: no page gives the Company's seat. Try https://en.wikipedia.org/wiki/Navarrese_Company
  - `/keyframe_review/7, /keyframe_review/8`: The end of the County of Salona (kept to 1390), and who took the land lost in 1379-1380 besides Thebes. Neopatras page: 'In 1378-79, the Aragonese lost most of their possessions in Boeotia to the Navarrese Company'. Try https://en.wikipedia.org/wiki/County_of_Salona
- Spot checks:
  - `/ledger/0` (https://en.wikipedia.org/wiki/Battle_of_Halmyros): confirmed: 'fought on 15 March 1311'; 'All of Attica and Boeotia passed peacefully into the hands of the Catalans'; Thebes 'the capital of the Duchy'
  - `/ledger/3` (https://en.wikipedia.org/wiki/Duchy_of_Neopatras): confirmed: 'the Catalans took Neopatras in 1319'
  - `/ledger/6` (https://en.wikipedia.org/wiki/Duchy_of_Neopatras): confirmed: lost 'when the region was conquered by the Serbs of Stefan Dushan in 1348'
  - `/ledger/8` (https://en.wikipedia.org/wiki/Duchy_of_Athens): confirmed: 'In 1379 the Navarrese Company ... conquered Thebes' and part of the Duchy of Neopatras; Neopatras page: 'By 1380, the Catalans were left only with the two capitals of Athens and Neopatras, as well as the County of Salona'
  - `/ledger/10, /ledger/12` (https://en.wikipedia.org/wiki/Duchy_of_Neopatras): confirmed: 'Athens fell to Acciaioli in 1388'; 'in 1390 he captured Neopatras as well'
  - `/ledger/1, /identity/end` (https://en.wikipedia.org/wiki/Catalan_Company): confirmed: 'In 1312, they accepted the overlordship of the Aragonese crown of Sicily'; duchies held 'until 1388-1390'; infobox 'Active: 1302-1390'
- Area: No infobox area on Catalan Company, Duchy of Neopatras or Duchy of Athens (checked); author says so in notes.

## thessaly: fail

- **TO FIX (author)** `/ledger/5 and a missing 1332 loss to despotate-of-epirus`: The 1332 loss gives all of Thessaly to byzantine-empire at confidence 3, but the pages and the despotate-of-epirus dossier give western Thessaly to John II Orsini of Epirus from 1332 to his death about 1335/6; this dossier has no loss to Epirus.
  - Evidence: Thessaly page: 'In 1332, most of Thessaly was taken by the Byzantines' (most, not all). Stephen Gabrielopoulos page: the Byzantines 'established direct control over the northern and eastern part of the region'; his heirs' quarrels led to 'an invasion by the Epirote ruler John II Orsini'; 'With Orsini's death three years later, all of Thessaly came under Byzantine control.' Medieval Thessaly: per Ferjancic 'the western part remained under Epirote rule until Orsini's death three years later'. despotate-of-epirus /ledger/40: 1332 gain, counterpart thessaly, region minus[Thessaly, Larissa 50 km]; /ledger/41: 1336 loss of 'the Epirote part of Thessaly' to byzantine-empire. The dossier's own dissolve note says 'with the western part claimed by John II Orsini of Epirus'.
  - Fix: Split /ledger/5: (a) 1332 loss, counterpart byzantine-empire, region the north and east (e.g. intersect of Thessaly with a Larissa 50 km disc, the complement of Epirus /ledger/40), confidence 2, text 'most of Thessaly'; (b) add 1332 loss, counterpart despotate-of-epirus, region {minus:[{region:Thessaly},{place:Larissa,km:50}]} to match Epirus /ledger/40, confidence 2, source Stephen_Gabrielopoulos or Medieval_Thessaly. Add despotate-of-epirus (western Thessaly) to identity.successors. The byzantine-empire dossier's 1333 gain of all 'Thessaly' (/ledger/172) needs the same split (route to its owner).
- Thin (for a gap-filler):
  - `/keyframe_review/2, /keyframe_review/3`: The 1318-1332 division (Gabrielopoulos at Trikala, the Maliasenoi around Volos, Byzantine north) is drawn as one state; flagged by the author. Try https://en.wikipedia.org/wiki/John_II_Doukas
  - `/wars/1`: How long Naupaktos (1295) was held. Try https://en.wikipedia.org/wiki/Nikephoros_I_Komnenos_Doukas
- Spot checks:
  - `/ledger/0` (https://en.wikipedia.org/wiki/Medieval_Thessaly): confirmed: dominions 'divided between Nikephoros ... and Michael's illegitimate son John Doukas'; reign 1267/8-1289; capital Neopatras
  - `/ledger/1` (https://en.wikipedia.org/wiki/Thessaly): confirmed: 'In 1318, with the death of John II, Thessalian independence came to an end'
  - `/ledger/2` (https://en.wikipedia.org/wiki/Thessaly): confirmed: 'the Almogavars occupied Siderokastron and southern Thessaly (1319)'
  - `/ledger/5` (https://en.wikipedia.org/wiki/Thessaly): year confirmed ('In 1332, most of Thessaly was taken by the Byzantines'), but the region overstates: 'most', and the Stephen Gabrielopoulos and Medieval Thessaly pages leave the west to Epirus (see fixes)
- Area: Thessaly infobox is the modern region; Medieval Thessaly has no infobox area. Acknowledged in /keyframe_review/1.

## empire-of-thessalonica: pass

- Thin (for a gap-filler):
  - `/keyframe_review/0`: Whether Thessaly was Manuel's in 1230-1237: the Empire page says yes ('the dynasty's lands in Thessaly and Epirus'), the Manuel page names only Thessalonica and its environs. The author flagged it. Try https://en.wikipedia.org/wiki/Theodore_Komnenos_Doukas
- Spot checks:
  - `/ledger/1` (https://en.wikipedia.org/wiki/Empire_of_Thessalonica): confirmed: 'Manuel's rule lasted until 1237, when he was deposed in a coup by Theodore', who crowned his son John
  - `/ledger/2` (https://en.wikipedia.org/wiki/Manuel_Komnenos_Doukas): confirmed: 'Manuel returned to Greece in 1239 with the support of Nicaea' and 'captured several fortresses, including Larissa and Pharsalos, from Theodore's son John Komnenos Doukas'; after his death c. 1241 'the area passed into the hands of ... Michael II'
  - `/ledger/3` (https://en.wikipedia.org/wiki/Empire_of_Thessalonica): confirmed: John renounced the imperial title and recognised Nicaean authority; infobox 'Vassal ... of the Empire of Nicaea (1242-46)'
  - `/ledger/5` (https://en.wikipedia.org/wiki/Empire_of_Thessalonica): confirmed: 'Thessalonica was incorporated into the Nicaean state'; infobox 'Fall of Thessalonica to Nicaea: 1246'
  - `/ledger/0 region` (https://en.wikipedia.org/wiki/Empire_of_Thessalonica): confirmed: 'He still controlled the environs of Thessalonica as well as the dynasty's lands in Thessaly and Epirus' (1230)
- Area: No infobox area on Empire of Thessalonica (checked). What I tried and could not break: years 1230-1246 against Epirus /ledger/14 (1230 split) and Nicaea /ledger/31-33 (1242 vassal, 1246 gain); keyframes 1236 -> 1239 (minus Thessaly) -> 1241 agree with /ledger/2; rulers contiguous; capital inside the 1241 bbox.

## commune-of-the-zealots: pass

- Spot checks:
  - `/ledger/0` (https://en.wikipedia.org/wiki/Byzantine_civil_war_of_1341%E2%80%931347): confirmed: after 2 March 1342 the armies 'arrived too late'; Synadenos and the aristocrats 'had fled after an uprising led by ... the Zealots'; Zealots page: 'from 1342 until 1350'
  - `/ledger/1` (https://en.wikipedia.org/wiki/Zealots_of_Thessalonica): confirmed: 'At the end of 1349, the people of the city finally rose in revolt'; 'in 1350, Kantakouzenos ... made a triumphal entry into the city'
  - `/ledger/2` (https://en.wikipedia.org/wiki/Byzantine_civil_war_of_1341%E2%80%931347): confirmed for 1350 ('to recover Thessalonica from the Zealots'); the note's 'only Macedonian city still Byzantine after 1345' is a paraphrase of 'leaving only Thessalonica in Byzantine hands' (after 1350), harmless
- Area: Neither page has an area; the 25 km disc (1,963 km2) matches Cliopatria's 1,760 km2. What I tried and could not break: dates 1342/1350 on both pages; type rebel per schema; identity.wikipedia/wikidata keep Cliopatria's values as the schema asks.

## duchy-of-the-archipelago: fail

- **TO FIX (author)** `/keyframe_review/1/correction, /keyframe_review/4/correction, /ledger/1/region, /ledger/3/region, /ledger/6/region, /wars/0 and /wars/2 zones, /identity/successors/0`: The corrections and events say 'all the Cyclades except Mykonos, Tinos (the Ghisi) and Andros (Dandolo)' but the spec subtracts only a 22 km disc at Andros, so Tinos and Mykonos are drawn inside the duchy 1210-1276 and 1310-1579.
  - Evidence: Duchy page: 'It included all the Cyclades (except Mykonos and Tinos)'. Gazetteer 'Cyclades' = Notio Aigaio intersect box 24.2-26.3 E, 36.3-37.9 N, which contains Tinos (25.16 E 37.54-37.66 N) and Mykonos (25.33 E 37.45 N); the Andros disc (24.9 E 37.83 N, 22 km) stops short of Tinos (24 km to its northern tip, 40 km to Tinos town) and is 57 km from Mykonos. The spec contradicts its own text.
  - Fix: In every spec that reads {minus:[{region:Cyclades},{lon:24.9,lat:37.83,km:22}]} add to the minus a Tinos disc (lon 25.16, lat 37.59, km 14) and a Mykonos disc (lon 25.36, lat 37.45, km 10), or the gazetteer names once added; the nested minus specs of /ledger/2, /ledger/3, /keyframe_review/2 and /wars/0 inherit it.
- Thin (for a gap-filler):
  - `/ledger/2`: Confidence-1 Licario loss dated 1277: the Licario page dates Skopelos 1277 (a Ghisi island, not the duchy's), then 'Kythera and Antikythera', 'later Kea, Astypalaia, and Santorini', and Sifnos and Serifos, all before c. 1280; the duchy page gives no year ('late 13th century'). A year in 1278-1280 is likelier for the duchy's islands. Try https://en.wikipedia.org/wiki/Marco_II_Sanudo
  - `/keyframe_review/4`: 1310-1579 rests on one page; island-by-island changes (Venetian and Ottoman takeovers before 1579) unverified within the 1-2 page budget. Try https://en.wikipedia.org/wiki/Duchy_of_the_Archipelago
- Spot checks:
  - `/ledger/0` (https://en.wikipedia.org/wiki/Duchy_of_the_Archipelago): confirmed: 'created in 1207 by the Venetian nobleman' Marco Sanudo, who 'largely captured the island'
  - `/ledger/1` (https://en.wikipedia.org/wiki/Duchy_of_the_Archipelago): confirmed for year and text ('With the entire island occupied in 1210' ... 'Melos and the rest of the islands of the Cyclades'); region spec wrong (see fixes)
  - `/ledger/3` (https://en.wikipedia.org/wiki/Duchy_of_the_Archipelago): confirmed: 'They relinquished control of their gains in 1310'
  - `/ledger/6` (https://en.wikipedia.org/wiki/Duchy_of_the_Archipelago): confirmed: 'annexed by the Ottomans in 1579'; infobox 'Expropriated by Murad III: 1579'
  - `/ledger/2` (https://en.wikipedia.org/wiki/Licario): page dates the island campaign 1277-c.1280, names no duchy island in 1277 (confidence 1 is honest; see thin)
- Area: No infobox area on the duchy page. Cliopatria's 1210 and 1305 shapes are the wrong islands (author marked 1305 'wrong' and corrected 1210), so no area comparison is meaningful.

## principality-of-theodoro: fail

- **TO FIX (author)** `/keyframe_review/2/correction, /keyframe_review/3/correction, /ledger/1/region, and a missing 1433 gain`: The 1423-1475 keyframe and the 1423 gain draw Cembalo (Balaklava) as Theodoro's for the whole span, while the ledger loses Cembalo to Genoa in June 1434 (/ledger/4) and the page has it Genoese before the February 1433 rising; there is no gain of Cembalo for the 1434 loss to undo.
  - Evidence: Principality of Theodoro page: 'Alexios supported a Greek rebellion in Cembalo in February 1433'; 'A Genoese force reconquered Cembalo in June 1434'; 'While Alexios lost Cembalo it seems that he retained the rest of his conquests'; 'Cembalo revolted once more in 1439'. The Sevastopol place (33.465 E, 44.60 N, gazetteer) with km 20 contains Balaklava (33.60 E, 44.50 N, 15 km away) and most of the /ledger/4 Cembalo disc (33.6, 44.5, 15 km).
  - Fix: Subtract the Cembalo disc (lon 33.6, lat 44.5, km 15) from /ledger/1/region and from the 1423 keyframe correction; add a February 1433 gain of Cembalo from republic-of-genoa (confidence 2: the page says Alexios supported the rebellion and Genoa 'reconquered' it) so that /ledger/4 undoes it; either split the 1423 keyframe at 1433/1434 or note that the Cembalo episode falls inside its span and is small. /keyframe_review/3 copies the same correction and needs the same change.
- Thin (for a gap-filler):
  - `/ledger/0`: Founding year (confidence 1, Cliopatria's 1333; page: 'first mentioned in the early 14th century'). Try https://en.wikipedia.org/wiki/Mangup
  - `/ledger/1`: Confidence-1 coastal gain dated 1423: the page's 1423 sentence is a repelled attack ('the Genoese had to spend a large sum of money to repel him'); the note says so. Date and extent of the coastal strip. Try https://en.wikipedia.org/wiki/Alexios_I_of_Theodoro
  - `/keyframe_review/1`: Cliopatria's 1375 halving (1,331 to 653.5 km2) is unexplained; within budget, flagged by the author. Try https://en.wikipedia.org/wiki/Gothia
- Spot checks:
  - `/ledger/1` (https://en.wikipedia.org/wiki/Principality_of_Theodoro): page has 'In 1423 prince Alexios attacked and the Genoese had to spend a large sum of money to repel him' and 'From the first half of the 15th century it also included parts of the coastline'; no capture date (confidence 1 honest)
  - `/ledger/2` (https://en.wikipedia.org/wiki/Principality_of_Theodoro): confirmed: 'Alexios supported a Greek rebellion in Cembalo in February 1433'
  - `/ledger/4` (https://en.wikipedia.org/wiki/Principality_of_Theodoro): confirmed: 'A Genoese force reconquered Cembalo in June 1434'
  - `/ledger/6` (https://en.wikipedia.org/wiki/Principality_of_Theodoro): confirmed: 'At the end of December 1475, Mangup surrendered to the Ottomans'
- Area: No infobox area on the Theodoro page (checked).

## Cross-dossier matrix

- catalan-company 1311 found <- duchy-of-athens: mirror duchy-of-athens 1311 dissolve; **matched**. duchy-of-athens /ledger/6 dissolve, counterpart catalan-company, 15 March 1311.
- catalan-company 1319 gain <- thessaly: mirror thessaly 1319 loss; **matched**. Neopatras disc on both sides.
- catalan-company 1325 gain <- thessaly: mirror thessaly 1325 loss; **matched**. Same region spec (Catalan 1326 minus 1314) on both sides.
- catalan-company 1348 loss <- serbian-empire: mirror -; **exception**. serbian-empire (eu-18) not written yet; note Cliopatria's Serbian Empire row starts only in 1352.
- catalan-company 1379 loss <- Navarrese Company: mirror -; **exception**. Listed in counterparts_needing_dossiers (navarrese-company).
- catalan-company 1388 loss <- acciaioli-duchy-of-athens: mirror -; **exception**. Was 'duchy-of-athens' (dead since 1311); reviewer changed it to the author's suggested new slug. Needs a dossier.
- catalan-company 1390 loss <- acciaioli-duchy-of-athens: mirror -; **exception**. As above (Neopatras 1390).
- thessaly 1268 found <- despotate-of-epirus: mirror despotate-of-epirus 1268 split; **matched**. despotate-of-epirus /ledger/29.
- thessaly 1332 loss <- byzantine-empire: mirror byzantine-empire 1333 gain; **matched**. Years within one; but both sides give all of Thessaly to Byzantium, while Epirus /ledger/40 takes western Thessaly in 1332 (next row).
- despotate-of-epirus 1332 gain <- thessaly: mirror thessaly (none); **missing**. Thessaly has no 1332 loss to Epirus; pages (Stephen Gabrielopoulos, Medieval Thessaly) support Epirus. Fix in thessaly (and the byzantine-empire 1333 gain should exclude the west until 1336).
- empire-of-thessalonica 1230 found <- despotate-of-epirus: mirror despotate-of-epirus 1230 split; **matched**. despotate-of-epirus /ledger/14.
- empire-of-thessalonica 1239 loss <- Manuel Komnenos Doukas (Thessaly): mirror -; **exception**. Listed in counterparts_needing_dossiers (thessaly-under-manuel-komnenos-doukas).
- despotate-of-epirus 1241 gain <- empire-of-thessalonica: mirror empire-of-thessalonica 1239 loss; **mismatch**. Epirus /ledger/18 takes Thessaly from empire-of-thessalonica in 1241, but Thessalonica lost it to Manuel in 1239 (Manuel page: after his death 'the area passed into the hands of ... Michael II'). Epirus should name Manuel's lordship as counterpart. Route to the despotate-of-epirus owner.
- despotate-of-epirus 1236 gain <- empire-of-thessalonica: mirror empire-of-thessalonica (none); **mismatch**. Epirus /ledger/17 (Corfu, confidence 1) has no mirror: no empire-of-thessalonica shape or event covers Corfu (shapes start at 21.36 E). Epirus side should change counterpart or region. Route to the despotate-of-epirus owner.
- empire-of-thessalonica 1246 loss <- nicaean-empire: mirror nicaean-empire 1246 gain; **matched**. nicaean-empire /ledger/33; Nicaea also carries vassal_start 1242 / vassal_end 1246 (overlord side, consistent with /ledger/3 here).
- commune-of-the-zealots 1342 found <- byzantine-empire: mirror byzantine-empire (none); **missing**. byzantine-empire has no 1342 loss of Thessalonica; flagged by the author. Route to the byzantine-empire owner (eu-05).
- commune-of-the-zealots 1350 loss <- byzantine-empire: mirror byzantine-empire (none); **missing**. byzantine-empire has no 1350 gain of Thessalonica. Route to the byzantine-empire owner.
- duchy-of-the-archipelago 1207 found <- byzantine-empire: mirror byzantine-empire 1204 loss; **mismatch**. byzantine-empire /ledger/149 gives Venice 'many ports and islands' in 1204 and holds nothing in the Aegean 1205-1261; the duchy takes the Cyclades from byzantine-empire in 1207/1210. One side must change (republic-of-venice or nobody as counterpart here, or the Byzantine 1204 loss should exclude the Cyclades).
- duchy-of-the-archipelago 1210 gain <- byzantine-empire: mirror byzantine-empire (none); **mismatch**. As for 1207.
- duchy-of-the-archipelago 1277 loss <- byzantine-empire: mirror byzantine-empire (none); **missing**. byzantine-empire has no Licario gains (1276-1280) in the Cyclades. Route to the byzantine-empire owner.
- duchy-of-the-archipelago 1310 gain <- byzantine-empire: mirror byzantine-empire (none); **missing**. byzantine-empire has no 1310 loss of the Cyclades. Route to the byzantine-empire owner.
- duchy-of-the-archipelago 1579 dissolve <- ottoman-empire: mirror -; **exception**. No ottoman-empire dossier yet.
- latin-empire 1210 vassal_start <- duchy-of-the-archipelago: mirror -; **exception**. Overlord side only (schema: vassal events are the overlord's); latin-empire /ledger/16 and /ledger/39, principality-of-achaea /ledger/8 and /ledger/24 agree with the duchy's notes (1248, 1278).
- principality-of-theodoro 1423 gain <- republic-of-genoa: mirror -; **exception**. republic-of-genoa (eu-13) not written yet; confidence 1.
- principality-of-theodoro 1434 loss <- republic-of-genoa: mirror -; **exception**. eu-13 not run; the matching 1433 gain is missing in this dossier (see fixes).
- principality-of-theodoro 1475 loss <- ottoman-empire: mirror -; **exception**. No ottoman-empire dossier yet.

## Problems and routing

- No page failed to load for the reviewer. No infobox in the batch gives an area, so every area_check is null with the author's acknowledgement.
- catalan-company was edited by the reviewer (5 slug lines, duchy-of-athens -> acciaioli-duchy-of-athens for 1388-1390); it now validates with 3 expected 'no dossier has this slug' warnings until the Acciaioli dossier exists.
- Mirrors missing in byzantine-empire (eu-05, another part): 1342 loss / 1350 gain of Thessalonica (Zealots), Licario's Cycladic gains 1277 and their 1310 loss, the western-Thessaly split of 1332-1336; its 1204 loss of 'many ports and islands' to Venice conflicts with the Archipelago's 1207/1210 counterpart.
- despotate-of-epirus (eu-05) needs counterpart changes: /ledger/18 (1241 Thessaly, should be Manuel's lordship) and /ledger/17 (1236 Corfu, empire-of-thessalonica never held it in any shape).
- Years for county-of-salona are the span the catalan-company dossier draws it; Andros and Tinos-Mykonos years are not on the pages opened.
