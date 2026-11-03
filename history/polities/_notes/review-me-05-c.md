# Review of batch me-05-c (2026-10-19)

Reviewer: adversarial review, Phase B. Dossiers: seleucid-empire, atropatene, revolt-of-molon, kingdom-of-achaeus. Validator before and after the reviewer's edits: 0 errors, 0 warnings for all four.
Neighbour dossiers read for cross-checks (context list, files present): ptolemaic-kingdom, greek-city-states, kingdom-of-bithynia, maurya-empire, greek-colonies, macedonian-empire, kingdom-of-lysimachus, kingdom-of-kush, roman-republic; also antigonid-dynasty and rhodes (counterparts named or implied in the ledger). Not yet written (exception): kingdom-of-armenia (eu-19), parthian-empire (me-06), kingdom-of-sophene, kingdom-of-cappadocia, kingdom-of-pontus, galatia, kingdom-of-pergamon, nabataeans, greco-bactrian-kingdom, judea (me-05 other parts), antigonid-macedonia.
Pages opened by the reviewer: Seleucid Empire, Mithridates I of Parthia, Syrian Wars, Antiochus III the Great, Atropatene (twice), Tigranes the Great, Molon, Achaeus (general).

## seleucid-empire: fail

Area: infobox 800000 km2 (-175), Cliopatria 1924785.8 km2, ratio 2.41. /keyframe_review/25 acknowledges the ratio and leaves it 'unverified: page budget'; other infobox years agree (301: 3.9M vs 2.98M; 240: 2.6M vs 2.27M; 100: 100k vs 91.7k).

Findings:
- [APPLIED by reviewer] `/ledger/31 (was /ledger/29)`: vassal_start atropatene dated 223; the quoted sentence 'In 223 BCE, Antiochus III attacked Atropatene' is not on the page. Evidence: Atropatene page: 'In 223 BCE, Antiochus III came to power in the Seleucid Empire...' (accession), then 'Antiochus attacked Atropatene, resulting in a victory' with no year; infobox map caption 'Atropatene as a vassal of Seleucids in 221 BC'; Antiochus III page puts 'The submission of Lesser Media' after the 221 collapse of Molon's revolt. Fix: Year -221, moved after the -221 gain from revolt-of-molon; note rewritten; notes and sources[14] note updated.
- [APPLIED by reviewer] `/ledger/29, /ledger/30, /ledger/63, /ledger/72`: Regions use the gazetteer's 'Media', which includes 273 cells of Atropatene, independent in 222-221 and a Parthian vassal later; the gains of 221 (Molon), 160 (Timarchus) and 130 (Antiochus VII) drew Atropatene as Seleucid land. Evidence: Antiochus III page: 'Lesser Media, which had asserted its independence under Artabazanes'; Mithridates I page lists 'Media and Atropatene' separately; the dossier's own -164 correction subtracts Atropatene. Cells: Media 674, Media and Atropatene -223 overlap 273. Fix: Each positive Media node wrapped as {minus: [Media, Atropatene -223 (221-222 events) or -170 (160, 130)]}; resolved: 0 Atropatene cells left.
- [TO DO by author] `/ledger (new event after /ledger/49)`: BLOCKING: no loss to rhodes at Apamea, although rhodes.json carries 'gain -188 from seleucid-empire' (c3) for Caria and Lycia south of the Maeander. Evidence: rhodes.json gain region (Rhodes -188 minus the island) is 81 cells, 54 of them inside Seleucid -197 minus -188 and covered by no Seleucid 188 loss (overlap with /ledger/48, /ledger/49, /ledger/50 is 0). Antiochus III page: Apamea land went to 'Rhodes or the Attalid ruler Eumenes II'; Roman-Seleucid war page (the dossier's source) names Rhodes for Lycia and Caria. Fix: Add {year -188, type loss, counterpart 'rhodes', region {intersect: [{minus: [Seleucid -197, Seleucid -188]}, {minus: [{cliopatria: 'Rhodes', year: -188}, {region: 'Rhodes'}]}]}, source Roman-Seleucid war page, confidence 2 or 3}.
- [TO DO by author] `/ledger/49`: Note says 'Rhodes receives Lycia and Caria' but the region is the Greek City-States -188 cells (184), none of which are Rhodes' gain; greek-city-states has no mirror gain. Evidence: Cell overlap with rhodes.json -188 gain region: 0. greek-city-states ledger: no event at -192..-186. Fix: Rewrite the note as the Greek cities freed or handed to Rome's allies at Apamea (or drop the event if the Cliopatria Greek City-States cells are not freed cities) and list the missing greek-city-states gain for eu-01.
- [TO DO by author] `/wars/12 (Roman-Seleucid war)`: The war has a zone (Asia Minor west of the Taurus) but no contest_start/contest_end in the ledger, so no fighting zone is drawn for 190-188 (Magnesia). Evidence: Atropatene page: 'in 190 B.C. ... the battle of Magnesia'; schema: the zone is drawn from contest events. Fix: Add contest_start -190 and contest_end -188, counterpart roman-republic, region = the war's zone.
- [TO DO by author] `/ledger/1, /ledger/2, /ledger/71, /ledger/74`: Contest zones 'Media' include Atropatene (273 cells), drawing fighting over a state that was not a belligerent. Evidence: Same overlap as the applied region fix. Fix: Clip Media with minus Atropatene as in /ledger/30.
- [TO DO by author] `/ledger/79`: The quote 'at the invitation of one of the factions in the interminable civil wars, he invaded Syria' is not on the cited Tigranes page (year and land are). Evidence: Tigranes the Great page: 'the Syrians decided to choose Tigranes as the protector of their kingdom and offered him the crown of Syria' (83 BC); 'He then conquered Phoenicia and Cilicia, effectively putting an end to the last remnants of the Seleucid Empire'. Fix: Quote the Tigranes page's own words, or cite the page the phrase comes from.
- [TO DO by author] `/ledger/45 note and notes`: Says the Syrian Wars page puts Panium in 200; that page gives no year for Panium. Evidence: Syrian Wars page: 'he delivered a crushing blow to the Ptolemies at the Battle of Panium' (no year); Antiochus III page: 'in 198 BC Antiochus defeated Scopas at the Battle of Panium'. Fix: Correct the disagreement note.
- [TO DO by author] `/identity/capitals/2`: Antioch is the capital to -64, but Tigranes held it 83-69 ('Magadates was appointed as his governor in Antioch'). Evidence: Tigranes the Great page. Fix: Split the span or note the 83-69 gap.

Thin (for a gap-filler):
- `/keyframe_review/25`: Area 1,924,786 km2 for 188-171 vs infobox 800,000 km2 for 175 BC (ratio 2.41), marked 'unverified: page budget'. The outline keeps Aria (198 of 203 cells) although the Mithridates I page has him conquer 'Aria, Margiana and western Bactria from the Greco-Bactrians sometime in 163-155 BC'; Persis (620 cells) and Carmania (691) are unbounded by any page. Page to try: https://en.wikipedia.org/wiki/Frataraka
- `/keyframe_review/28`: Susiana (247 cells) is in the -164 shape and not in the -144 shape; no ledger event takes it (Elymais not mapped). Page to try: https://en.wikipedia.org/wiki/Elymais
- `/ledger/9`: 294 Cilicia from Pleistarchus, confidence 1. Page to try: https://en.wikipedia.org/wiki/Pleistarchus
- `/ledger/11-14`: 279 losses to Galatia, Bithynia, Pergamon, Pontus, confidence 1 (Cliopatria's year). Page to try: https://en.wikipedia.org/wiki/Antiochus_I_Soter
- `/ledger/26, /ledger/50`: 239 and 188 Cappadocia, confidence 1. Page to try: https://en.wikipedia.org/wiki/Ariarathes_III_of_Cappadocia
- `/ledger/28`: 225 Attalid gains, confidence 1 (War of the Brothers page failed). Page to try: https://en.wikipedia.org/wiki/Attalus_I
- `/ledger/51`: 188 end of Armenian vassalage, confidence 1. Page to try: https://en.wikipedia.org/wiki/Artaxias_I
- `/ledger/61`: 164 east (Persis, Carmania, Aria) to Parthia, confidence 1. Page to try: https://en.wikipedia.org/wiki/Frataraka
- `/ledger/62`: 161 start of Timarchus's revolt, confidence 1. Page to try: https://en.wikipedia.org/wiki/Timarchus
- `/ledger/75, /ledger/76`: 129 Judea vassal_end and 126 Hasmonean gains, confidence 1. Page to try: https://en.wikipedia.org/wiki/John_Hyrcanus
- `/ledger/77`: 110 Euphrates land to Parthia (487 cells), confidence 1. Page to try: https://en.wikipedia.org/wiki/Mithridates_II_of_Parthia
- `/ledger/78`: 91 Judea gains, confidence 1. Page to try: https://en.wikipedia.org/wiki/Alexander_Jannaeus
- `/ledger/81`: 66 Nabataean gain, confidence 1 (Aretas III held Damascus in the 80s-70s). Page to try: https://en.wikipedia.org/wiki/Aretas_III
- `/keyframe_review/29-31`: Losses of Cilicia, Phoenicia and Coele-Syria in the dynastic wars 129-83 are not mapped (author's gap). Page to try: https://en.wikipedia.org/wiki/Seleucid_Dynastic_Wars
- `/identity/rulers`: Ruler strip omitted (page budget). Page to try: https://en.wikipedia.org/wiki/Seleucid_dynasty

Spot checks:
- `/ledger/8` (https://en.wikipedia.org/wiki/Seleucid_Empire): confirmed (Ipsus 301; 'Seleucus took control over eastern Anatolia and northern Syria')
- `/ledger/17` (https://en.wikipedia.org/wiki/Syrian_Wars): confirmed ('Ptolemy reconquered these territories by 271 BC ... Caria and into most of Cilicia')
- `/ledger/46` (https://en.wikipedia.org/wiki/Syrian_Wars): confirmed ('completed the subjugation of Coele-Syria in 198 BC'; treaty 195)
- `/ledger/54` (https://en.wikipedia.org/wiki/Syrian_Wars): confirmed (Pelusium November 170; withdrew late 169; evacuation of Egypt and Cyprus 168)
- `/ledger/64` (https://en.wikipedia.org/wiki/Mithridates_I_of_Parthia): confirmed ('conquering Media and Atropatene in 148/7 BC')
- `/ledger/67` (https://en.wikipedia.org/wiki/Mithridates_I_of_Parthia): confirmed ('In 141 BC, he conquered Babylonia')
- `/ledger/65` (https://en.wikipedia.org/wiki/Seleucid_Empire): confirmed ('By 143 BC ... fully established their independence')
- `/ledger/73` (https://en.wikipedia.org/wiki/Seleucid_Empire): confirmed (killed at Ecbatana 129)
- `/ledger/79` (https://en.wikipedia.org/wiki/Tigranes_the_Great): confirmed (83, Phoenicia and Cilicia); quoted phrase not on this page
- `/ledger/31 (was 29)` (https://en.wikipedia.org/wiki/Atropatene): mis-dated (223 is Antiochus III's accession; infobox map 221) - fixed
- `/ledger/41` (https://en.wikipedia.org/wiki/Antiochus_III_the_Great): confirmed (siege of Xerxes of Sophene 212; the page names Sophene, not Armenia: confidence 2 is right)
- `/ledger/48` (https://en.wikipedia.org/wiki/Antiochus_III_the_Great): confirmed (Apamea 188, 'all the country north and west of the Taurus Mountains')

## atropatene: fix

Area: infobox 0 km2 (0), Cliopatria 147253.2 km2, ratio 0.0. No area on the Atropatene page (checked); the author says so.

Findings:
- [APPLIED by reviewer] `/ledger/1, /ledger/2, /wars/0, /keyframe_review/4`: Antiochus III's attack and Artabazanes' submission dated 223 on a misquote ('In 223 BCE, Antiochus III attacked Atropatene'). Evidence: Atropatene page: 'In 223 BCE, Antiochus III came to power in the Seleucid Empire...'; the attack sentence has no year; infobox map 'Atropatene as a vassal of Seleucids in 221 BC'; Antiochus III page puts the submission after 221. Fix: Years -221 in both contest events and the war; notes and keyframe note updated.

Thin (for a gap-filler):
- `/ledger (88-85 BC)`: Tigranes of Armenia 'retook Adiabene, Gordyene, and Media Atropatene' between 88 and 85 BC; no event (vassal tint belongs to kingdom-of-armenia, eu-19, but any land loss belongs here). Page to try: https://en.wikipedia.org/wiki/Tigranes_the_Great
- `/ledger (189-160 BC)`: Artaxias I's Armenian conquests on the Atropatene border (Caspiane, Phaunitis) are not checked. Page to try: https://en.wikipedia.org/wiki/Artaxias_I
- `/ledger (36-20 BC)`: Atropatene's alliance with Antony, Artavasdes I and Ariobarzanes II (in Rome c. 30-20 BC) and any land given or taken; the page gives no border move. Page to try: https://en.wikipedia.org/wiki/Artavasdes_I_of_Media_Atropatene
- `/keyframe_review/0`: 323-308 overlap with macedonian-empire's shapes (579 of 582 cells) with no loss or vassal tint on the Macedonian side; independence date undated on both pages. Page to try: https://en.wikipedia.org/wiki/Atropates

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Atropatene): confirmed (infobox 'Established: c. 323 BC')
- `/ledger/1` (https://en.wikipedia.org/wiki/Atropatene): mis-dated (223 for 221) - fixed
- `/ledger/3` (https://en.wikipedia.org/wiki/Mithridates_I_of_Parthia): confirmed ('Media and Atropatene in 148/7 BC')
- `/ledger/5` (https://en.wikipedia.org/wiki/Atropatene): confirmed (Atropatid table ends with Artavasdes II r. 4-6; Arsacids from Artabanus)
- `/ledger/6` (https://en.wikipedia.org/wiki/Atropatene): confirmed ('In 226, Atropatene submitted with little resistance to Ardashir I')

## revolt-of-molon: thin

Area: infobox 0 km2 (0), Cliopatria 0 km2, ratio 0.0. No Cliopatria row and no infobox area.

Findings:
- [APPLIED by reviewer] `/ledger/0-2, /keyframe_review/0/correction, /identity/predecessors/0/land, /identity/successors/0/land, /wars/0/zones`: 'Media' drew the rebel domain over independent Atropatene (273 cells). Evidence: Antiochus III page: 'Lesser Media, which had asserted its independence under Artabazanes'; its submission followed the revolt. Fix: Every Media node wrapped as {minus: [Media, Atropatene -223]}; the domain resolves to 1,021 cells, all inside the Seleucid -223 shape; note added to notes.

Thin (for a gap-filler):
- `/ledger/1, /ledger/2, /identity/end`: The Molon page says he 'made himself master of the city of Seleucia on the Tigris together with the whole of Babylonia and Mesopotamia' and died in 220 BC (Antiochus crossed the Tigris in 220; infobox death '220 BC Mesopotamia'), against the Antiochus III page's 'collapsed' in 221. Add the Babylonian/Mesopotamian gain from seleucid-empire (with the Seleucid mirror loss) and decide the end year (220 per the dedicated page), noting the disagreement. Page to try: https://en.wikipedia.org/wiki/Molon

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Antiochus_III_the_Great): confirmed (Media and Persis revolted, 222)
- `/ledger/1` (https://en.wikipedia.org/wiki/Antiochus_III_the_Great): confirmed on the cited page (collapsed 221); the Molon page gives 220
- `/ledger/0 (region)` (https://en.wikipedia.org/wiki/Molon): confirmed for Media (revolt 222); page adds Babylonia and Mesopotamia

## kingdom-of-achaeus: thin

Area: infobox 0 km2 (0), Cliopatria 0 km2, ratio 0.0. No Cliopatria row and no infobox area.

Thin (for a gap-filler):
- `/keyframe_review/0/correction, /ledger/0, /identity/predecessors/0/land`: Extent: the Achaeus page gives him 'the command of all Asia Minor on the western side of Mount Taurus' and 'the whole of Asia on the western side of the Taurus'; the region is only Lydia, Phrygia, Ionia and Caria (161 of the 694 Seleucid cells west of the Taurus: Lycaonia 130, Pisidia 56, Mysia 46, Pamphylia 39 left out). Widen to Seleucid -218 minus Seleucid -188 (less Cilicia if Antiochus held it) and mirror it in seleucid-empire /ledger/32, /ledger/37, /ledger/38. Page to try: https://en.wikipedia.org/wiki/Achaeus_(general)
- `/ledger/3-5`: Page disagreement not noted: the Achaeus page has the citadel fall in 214 ('After sustaining a siege of two years'; infobox death 214 BC at Sardes) against 213 (Antiochus III page, under Laodice); and he declared himself king 'in Phrygia'. Page to try: https://en.wikipedia.org/wiki/Achaeus_(general)

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Antiochus_III_the_Great): confirmed (title of king in Asia Minor, 220 section; Achaeus page: 'proclaimed himself king in 220 BC')
- `/ledger/1` (https://en.wikipedia.org/wiki/Antiochus_III_the_Great): confirmed (216 march into western Anatolia)
- `/ledger/2` (https://en.wikipedia.org/wiki/Antiochus_III_the_Great): confirmed ('by 214 BC driven him from the field into Sardis')
- `/ledger/4` (https://en.wikipedia.org/wiki/Antiochus_III_the_Great): confirmed on the cited page ('held out until 213 BC'); Achaeus page says 214

## Why seleucid-empire fails

One blocking finding remains unapplied: the Treaty of Apamea's land for Rhodes. rhodes.json (written before this batch) records 'gain -188 from seleucid-empire' at confidence 3; the Seleucid ledger has no loss to rhodes, and its /ledger/49 note speaks of Rhodes while its land is 184 cells of the Greek City-States row that do not touch Rhodes' 81 cells. Add the loss to rhodes and correct /ledger/49. Everything else in the dossier held up: 12 events checked on 6 pages, 11 confirmed and one mis-dated at confidence 2 (fixed). The other TO DO items are small.

## Cross-dossier matrix (non-exception rows)

- seleucid-empire /ledger/3 -309 gain macedonian-empire -> matched (macedonian-empire /ledger/58 -309 loss)
- seleucid-empire /ledger/7 -303 loss maurya-empire -> matched (maurya-empire /ledger/7 -302 gain): one year apart
- seleucid-empire /ledger/8 -301 gain antigonid-dynasty -> matched (antigonid-dynasty /ledger/7 -301 loss)
- seleucid-empire /ledger/10 -281 gain kingdom-of-lysimachus -> matched (kingdom-of-lysimachus /ledger/22 -281 loss)
- seleucid-empire /ledger/12 -279 loss kingdom-of-bithynia -> matched (kingdom-of-bithynia /ledger/2 -279 gain)
- seleucid-empire /ledger/17 -271 loss ptolemaic-kingdom -> matched (ptolemaic-kingdom /ledger/29 -271 gain)
- seleucid-empire /ledger/20 -253 gain ptolemaic-kingdom -> matched (ptolemaic-kingdom /ledger/32 -253 loss)
- seleucid-empire /ledger/24 -241 loss ptolemaic-kingdom -> matched (ptolemaic-kingdom /ledger/37 -241 gain)
- seleucid-empire /ledger/29 -222 loss revolt-of-molon -> matched (revolt-of-molon /ledger/0 -222 found): found event of the rebel state mirrors the loss
- seleucid-empire /ledger/30 -221 gain revolt-of-molon -> matched (revolt-of-molon /ledger/1 -221 loss)
- seleucid-empire /ledger/32 -220 loss kingdom-of-achaeus -> matched (kingdom-of-achaeus /ledger/0 -220 found): found event of the rebel state mirrors the loss
- seleucid-empire /ledger/34 -219 gain ptolemaic-kingdom -> matched (ptolemaic-kingdom /ledger/39 -219 loss)
- seleucid-empire /ledger/36 -217 loss ptolemaic-kingdom -> missing: ptolemaic-kingdom has only contest_end -217 (Raphia); it needs gain -217 from seleucid-empire for the Phoenician/Coele-Syrian land Antiochus took in 219 (it carries the 219 loss). Route to the ptolemaic-kingdom author (me-05).
- seleucid-empire /ledger/38 -214 gain kingdom-of-achaeus -> matched (kingdom-of-achaeus /ledger/2 -214 loss)
- seleucid-empire /ledger/40 -213 gain kingdom-of-achaeus -> matched (kingdom-of-achaeus /ledger/4 -213 loss)
- seleucid-empire /ledger/46 -198 gain ptolemaic-kingdom -> matched (ptolemaic-kingdom /ledger/46 -198 loss)
- seleucid-empire /ledger/49 -188 loss greek-city-states -> missing: greek-city-states (eu-01) has no gain at -188. Also the event note describes Rhodes receiving Lycia and Caria, but its land (Greek City-States -188 cells, 184) does not overlap rhodes.json's -188 gain region (81 cells): see the rhodes row.
- seleucid-empire /ledger/54 -170 occupation_start ptolemaic-kingdom -> matched (ptolemaic-kingdom /ledger/55 -170 occupation_start)
- seleucid-empire /ledger/56 -168 occupation_start ptolemaic-kingdom -> missing: ptolemaic-kingdom has no occupation_start for Cyprus in 168 ("a Seleucid fleet seized Ptolemaic Cyprus", Syrian Wars page). Route to me-05 ptolemaic-kingdom.
- seleucid-empire /ledger/57 -168 occupation_end ptolemaic-kingdom -> matched (ptolemaic-kingdom /ledger/56 -168 occupation_end)
- seleucid-empire /ledger/58 -168 occupation_end ptolemaic-kingdom -> missing: Cyprus occupation_end: ptolemaic-kingdom /ledger/56 is the Egypt occupation_end; no Cyprus pair.
- seleucid-empire /ledger/82 -64 loss roman-republic -> matched (roman-republic /ledger/168 -64 gain)
- revolt-of-molon /ledger/1 -221 loss seleucid-empire -> matched (seleucid-empire /ledger/30 -221 gain)
- kingdom-of-achaeus /ledger/2 -214 loss seleucid-empire -> matched (seleucid-empire /ledger/38 -214 gain)
- kingdom-of-achaeus /ledger/4 -213 loss seleucid-empire -> matched (seleucid-empire /ledger/40 -213 gain)
- rhodes /ledger (gain -188, c3) -188 gain seleucid-empire -> mismatch: rhodes.json (written 2026-10-19 01:18, before this batch) gains Caria and Lycia south of the Maeander from seleucid-empire (81 cells, 54 inside Seleucid -197 minus -188). seleucid-empire has no loss to rhodes; its /ledger/49 loss to greek-city-states covers 184 other cells. Fix in seleucid-empire.
- atropatene /ledger/0 -323 found macedonian-empire -> mismatch: Not a matrix type, but predecessor land disagrees: macedonian-empire (eu-02) draws its -323..-307 shapes over 579 of the 582 Atropatene cells and has no loss (or vassal tint) to atropatene; one of the two must give way for 323-308. Route to eu-02.

Exceptions: 35 events whose counterpart has no dossier yet (listed above as not yet written, or in counterparts_needing_dossiers), plus the vassal events, which by the schema only the overlord records.

## Problems

- The reviewer brief's rule 3 (a vassal_start mirrored in the vassal's ledger with the overlord as counterpart) conflicts with the schema (the overlord records vassal events, counterpart = the vassal); vassal events were treated as exceptions.
- https://en.wikipedia.org/wiki/Molon_(general) does not exist; the article is at https://en.wikipedia.org/wiki/Molon.
- Pages the author could not load were not retried: Seleucid-Parthian wars, War of the Brothers (Seleucid).
- Reviewer edits applied in place (validated, 0 errors, 0 warnings): seleucid-empire (Atropatene vassal year, Media clipped in 4 events, notes), atropatene (221 for 223), revolt-of-molon (Media clipped). The ledger indices of seleucid-empire events 29-31 changed (old 29 -> 31, old 30 -> 29, old 31 -> 30).
- Cross-batch routing: ptolemaic-kingdom (me-05) lacks gain -217 and the 168 Cyprus occupation; greek-city-states (eu-01) lacks gain -188; macedonian-empire (eu-02) overlaps Atropatene 323-307 without a loss.
