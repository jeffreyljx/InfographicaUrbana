# Review of batch ia-01-b (Xiongnu to the Türks, part b), 2026-10-18

This is the adversarial review of the six dossiers xianbei, wusun, kidarites, xionites, southern-xiongnu and great-yuan. The machine copy is history/notes/phase-b/reviews/ia-01-b.json.

How it was checked: the validator with --resolve gave 0 errors (one warning: kidarites /ledger/1, the new slug kushano-sasanian-kingdom). Every ledger region and every correction was resolved on the gazetteer grid and compared, cell by cell, with the Cliopatria shapes and with the neighbour dossiers xiongnu and yuezhi. Sixteen pages were opened for the spot checks. Small page-verified fixes were applied in place, tagged '(reviewer ia-01-b, 2026-10-18)', and re-validated.

| slug | verdict | in short |
| --- | --- | --- |
| xianbei | fail | Fails. From 91 to 235 it draws about 206 k km2 of the Southern Xiongnu's land as Xianbei, and the 205 split / 233 merge carry the whole state while the keyframes keep it. Two small fixes were applied (the area acknowledgement on K9, the war start 218). |
| wusun | thin | Thin. The 91 drop and the 3rd-4th centuries are unexplained (5 of 9 pages used). The capital was moved out of the lake. Successors still need adding. |
| kidarites | fail | Fails. 156 k km2 of southern land is drawn from 387 with no gain, and about 198 k km2 vanishes in 466 with no loss. The ruler, capital and notes were fixed by the reviewer. |
| xionites | thin | Thin by design. Four of five events are at confidence 1; all spot checks hold. |
| southern-xiongnu | fix | Fixed by the reviewer: two confidence-3 events lowered to 2 and the overlap note added. The overlap itself is settled on the xianbei side. |
| great-yuan | fix | Fixed by the reviewer: one misattributed quote. Ferghana is double-claimed with yuezhi -126..-111 (to fix on the yuezhi side). |

## xianbei (fail)

Findings:
- /ledger/3 [for the author]: The 91 gain, and every Xianbei keyframe from 91 to 235, draw about 206 k km2 of the Southern Xiongnu's land as Xianbei, while southern-xiongnu.json (same batch) holds that land 48-216 with no event moving it. Evidence: Gazetteer cells: minus(Mongolian Plateau, Xianbei 84) intersect Cliopatria 'Southern Xiongnu' 91 (216 k km2, 103.5-114.8 E, 38.7-42.4 N) = 206 k; the K3-K5 correction (Xianbei 84 + Mongolian Plateau) = 206 k; the 154/161/165 shapes kept ok in K6-K8 = 213 k; the 224 strip used in K9-K11 = 203 k. southern-xiongnu K1-K4 keep the shape 51-215. Fix: Subtract {"cliopatria":"Southern Xiongnu","year":91} from /ledger/3/region and the corrections of /keyframe_review/3-5; mark /keyframe_review/6-8 adjust with the same subtraction; subtract it from /keyframe_review/9-11 until 216 (a later keyframe may add it back with a gain dated 216). If the author instead holds that the Southern Xiongnu sat only inside the commanderies, shrink southern-xiongnu to match. One dossier, not both.
- /ledger/8 [for the author]: The 205 split and the 233 merge (/ledger/9) carry the whole remaining state (the 224 strip, 774 k km2) as their region, so the ledger has the Xianbei lose all their land in 205, but /keyframe_review/9-10 keep the same 774 k km2 Xianbei through 207-233. Kuitou's divided domain is also not Kebineng's land, and the matching war has empty zones without saying why. Evidence: /ledger/8/region = /ledger/9/region = the K9-K11 correction {cliopatria Xianbei 224}. Xianbei page: 'Following his death in 205, Kuitou's territory was divided between his brothers, Budugen and Fuluohan'; 'In 218, Kebineng allied with the Wuhuan of Dai and killed Fuluohan'; 'Kebineng killed Budugen soon afterwards'; Kebineng 'rose to power west of Dai Commandery'. Kebineng page: he 'resided near the Great Wall around the areas of Dai and Shanggu commanderies'. Fix: Give the split only Kuitou's share: a part of the strip, at confidence 1 if no page names it. Keep Kebineng's Dai-Shanggu land with the state. Mirror it with a merge of Fuluohan's share in 218 and Budugen's by 233. Or drop the split/merge pair, explain it in notes, and either give /wars/2 a zone or say that no ground changed hands.
- /ledger/4 [for the author]: The 154 gain of Dzungaria names 'nobody', but xiongnu.json dissolves in 151 with xianbei as a successor; the two sides differ by three years and by counterpart. Evidence: xiongnu /ledger/40: 151 dissolve, successors [xianbei, yueban]; its region (Hami ring, 89 k km2) overlaps only 43 k of this 449 k gain. Battle of Ikh Bayan page footnote: the Dzungarian remnant is 'mentioned in annals until 151'. Fix: Either date the gain to 151-152 with counterpart xiongnu (keeping confidence 1 and noting that Cliopatria's shape starts in 154), or say in the note why the land was nobody's from 151 to 154.
- /keyframe_review/9/note [applied by reviewer]: The infobox area for 200 (4.5 M km2) against the 0.77 M km2 this correction draws (ratio 0.17) was acknowledged only on the 60-83 and 161 keyframes, not on the keyframe alive in 200. Evidence: Xianbei infobox: '200: 4,500,000 km2'; the correction of xianbei_197 resolves to about 774 k km2. Fix: Added a sentence to the note: the infobox figure is set aside because the page's text has the Xianbei 'already split into many different groups' by the Jian'an era (reviewer ia-01-b, 2026-10-18).
- /wars/2/from [applied by reviewer]: Kebineng's wars of consolidation started in 224 in the dossier, but the page dates the first blow to 218. Evidence: Xianbei page: 'In 218, Kebineng allied with the Wuhuan of Dai and killed Fuluohan'. Fix: from 224 -> 218, with the quote added to the war note (reviewer ia-01-b, 2026-10-18).

Gaps for a gap-filler:
- /ledger/6: the year of Tanshihuai's expansion to 5.22 M km2 (161 is Cliopatria's year; the page is undated), and who held the north and the east (try https://en.wikipedia.org/wiki/Dingling)
- /ledger/4: who took Dzungaria after 151 (confidence 1, bridged from Cliopatria) (try https://en.wikipedia.org/wiki/Yueban)
- /keyframe_review/1: the extent in 60-83 (unverified; the page is silent) (try https://en.wikipedia.org/wiki/Wuhuan)

Spot checks:
- /ledger/0, Xianbei: confirmed: 'In 49, the governor Ji Tong convinced the Xianbei chieftain Pianhe to turn on the Xiongnu'
- /ledger/3, Xianbei: confirmed: 'In 91, the Northern Xiongnu were defeated by the Han dynasty and the Xianbei began occupying the Mongolian Plateau'
- /ledger/7, Xianbei: confirmed: 'By the Jian'an era (196-220), the Xianbei had already split into many different groups'
- /ledger/8, Xianbei: confirmed (year and actors): 'Following his death in 205, Kuitou's territory was divided between his brothers, Budugen and Fuluohan.'; the region is the fault above
- /ledger/9, Tanshihuai: confirmed: 'by 233, they were both killed by a rival chieftain, Kebineng'; the Xianbei page dates Fuluohan's death to 218
- /ledger/10, Kebineng: confirmed: assassinated by Han Long, sent by Wang Xiong, in 235; 'a period of relative peace ... for several decades'
- /keyframe_review/4, Battle_of_Ikh_Bayan: confirmed: 'The rest of the Xiongnu left in Dzungaria, specifically near Lake Barkol'; footnote 'until 151'

Area: The ratio is against Cliopatria's xianbei_197. The dossier's own correction draws 0.77 M km2 for 200 (ratio 0.17). That is acknowledged on K1 and K7, and the reviewer added it to K9.

## wusun (thin)

Findings:
- /identity/capitals/0/lat [applied by reviewer]: Chigu was placed at 77.5 E, 42.4 N, a point inside Lake Issyk-Kul on the grid, although the note says 'a point on the southern shore'. Evidence: The gazetteer's lake Issyk-Kul (bbox 76.42-78.04 E, 42.21-42.68 N) contains the cell at 77.5, 42.4; the cell at 77.5, 42.15 is outside the lake and inside wusun_443. Fix: lat 42.4 -> 42.15, with a note (reviewer ia-01-b, 2026-10-18).
- /identity/successors [for the author]: The 450 dissolve has no successors, so the last Wusun land passes to no one. Evidence: Wusun page: 'In the 5th century AD the Wusun were pressured by the Rouran'; 'It is possible that they became subsumed into the later Hephthalites'. Cliopatria's White Huns 451 shape covers all of the last Wusun shape (33 of 33 k km2 on the grid). Fix: Add a successor: white-huns, with land {cliopatria: Wusun, year: 443} and a note that the page only says 'possible'. Or name rouran-khaganate if a page supports it.

Gaps for a gap-filler:
- /ledger/2: the fall from 194 k to 40 k km2 in 91: no page dates it or names the taker (confidence 1, counterpart nobody); the Yueban page's 'Established: 160' does not match 91 (try https://en.wikipedia.org/wiki/Ban_Chao)
- /keyframe_review/14: the 3rd and 4th centuries (165-386), page silent (try https://en.wikipedia.org/wiki/Zhetysu)
- /ledger/3: the end: the last mention is in 436, while 450 is Cliopatria's year (confidence 1) (try https://en.wikipedia.org/wiki/Rouran_Khaganate)
- /notes: the author used 5 of the 9 pages the budget allows; the Greater and Lesser Kunmi division is undated (try https://en.wikipedia.org/wiki/Protectorate_of_the_Western_Regions)

Spot checks:
- /ledger/0, Wusun: confirmed: 'In 133-132 BC, the Wusun drove the Yuezhi out of the Ili Valley and settled the area' (confidence 3 holds: the page names the Ili Valley and Chigu by Issyk Kul)
- /ledger/1, Wusun: confirmed by the same sentence; the original home 'between the Qilian Mountains and Dunhuang (Gansu)' also confirmed
- /ledger/2, Wusun: confirmed as noted: 'During the 2nd century AD the Wusun continued their decline in political importance'; the page gives no year (confidence 1 is honest)
- /ledger/3, Wusun: confirmed as noted: Rouran pressure, 'may have migrated to the Pamir Mountains', 'last mentioned ... in 436 AD', 'subsumed into the later Hephthalites'

Area: The Wusun page has no infobox area. The author says so on K2.

## kidarites (fail)

Findings:
- /keyframe_review/1 [for the author]: kidarites_387 is marked ok, but the 387 shape adds 194 k km2 in the south over the 358 shape and no event in 387 gains it. The only southern gain is /ledger/3 (Gandhara, 37 k km2), dated 390, so 156 k km2 (Kabul and the Hindu Kush side) is never gained and Gandhara is drawn three years before its gain. Evidence: Gazetteer cells: Kidarites 387 minus Kidarites 358 = 194 k km2 (64.9-73.6 E, 31.9-38.6 N); minus the /ledger/3 region it is 156 k. The K1 note itself says 'the shape already includes Gandhara in 387'. Kidarites page: 'circa 390-410 CE, the Kidarites invaded northwestern India'. Fix: Either mark K1 adjust for 387-389 with the southern addition removed (intersect the 387 shape with the 358 shape), or add a 387 gain of the southern addition with its counterpart and a page, and align /ledger/3 with the keyframe that first draws Gandhara.
- /keyframe_review/6 [for the author]: In 466 the state falls from the 402 shape (822 k km2 on the grid) to Gandhara (49 k), but the 466 losses (/ledger/7, north, 410 k; /ledger/8, Bactria, 212 k) leave about 198 k km2 with no loss event: Kabulistan, the Zabul side, the Hindu Kush, and the land south of the gazetteer's Bactria. Evidence: Gazetteer cells: Kidarites 402 minus the /ledger/7 region minus Bactria minus Gandhara = 198 k km2 (64.8-73.6 E, 31.9-39.3 N). Kidarites page: 'Although the Kidarites still controlled some places such as Gandhara and Punjab'. Fix: Add the missing 466-467 loss (to white-huns, sasanian-empire or alchon-huns, at the confidence a page supports), or widen /keyframe_review/6 and /ledger/9 to the land the Kidarites kept.
- /identity/rulers/0/from [applied by reviewer]: Kidara's reign began in 350, before the state's start in 360. Evidence: Rule 2: rulers inside the life. The Kidarites page table gives 'c.350-390'; the dossier's start is 360. Fix: 350 -> 360, with a note (reviewer ia-01-b, 2026-10-18).
- /identity/capitals/0/to [applied by reviewer]: Balkh stayed the capital to 467, but Bactria is lost in 466 (/ledger/8) and the 466-467 keyframe is Gandhara only. Evidence: Kidarites page: Peroz 'finally vanquished Kidarites in 466, and brought Bactria briefly under Sasanian control'. Fix: 467 -> 465, with a note (reviewer ia-01-b, 2026-10-18).
- /notes [applied by reviewer]: The infobox 'Established: 320 CE' (and 'fl. 320: Kidara') was not acknowledged against the start of 360. Evidence: Kidarites infobox; the text has 'In 360-370 CE, a Kidarite kingdom was established'. Fix: Added one sentence to notes (reviewer ia-01-b, 2026-10-18).

Gaps for a gap-filler:
- /ledger/2: the year the north passed to the Xionites (387 is Cliopatria's; the Xionites page has only 'At the end of the 4th century AD, the Kidarites were pushed into Gandhara') (try https://en.wikipedia.org/wiki/Shapur_III)
- /ledger/4: how the Xionite land returned in 402 (confidence 1, bridged) (try https://en.wikipedia.org/wiki/Bahram_V)
- /ledger/5: where the 450 defeat fell (try https://en.wikipedia.org/wiki/Yazdegerd_II)

Spot checks:
- /ledger/0, Kidarites: confirmed: 'In 360-370 CE, a Kidarite kingdom was established'; Bactria 'by 360'
- /ledger/1, Kushano-Sasanian_Kingdom: confirmed: 'This administration continued until 360-370'; 'lost much of their domains to the invading Kidarites'
- /ledger/3, Kidarites: confirmed: 'circa 390-410 CE, the Kidarites invaded northwestern India'
- /ledger/5, Hephthalites: confirmed: 'were militarily important from 450 CE, when they defeated the Kidarites'
- /ledger/7, Hephthalites: confirmed: 'Around 466 they probably took Transoxianan lands from the Kidarites with Persian help'
- /ledger/8, Peroz_I: confirmed (confidence 3 holds): 'finally vanquished the Kidarites in 466, and brought Tokharistan briefly under Sasanian control'; the Kidarites page says 'Bactria'
- /ledger/9, Hephthalites: confirmed: 'by 467, Peroz I, with Hephthalite aid, reportedly managed to capture Balaam'; 'The weakened Kidarites had to take refuge in the area of Gandhara'

Area: The Kidarites infobox has no area figure, only a map captioned c. 400.

## xionites (thin)


Gaps for a gap-filler:
- /ledger/1: the three 387 events (/ledger/1-3) rest on Cliopatria's 387 shape alone (confidence 1; the page gives no year) (try https://en.wikipedia.org/wiki/Shapur_II)
- /ledger/4: the end in 401 is Cliopatria's; the page has the Xionites 'until the mid-5th century AD' and Chionites at Chach into the 6th (try https://en.wikipedia.org/wiki/Alchon_Huns)
- /keyframe_review/0: the 353-386 extent rests only on the word 'Transoxiana' (thin by design within the 1-2 page budget, 2 of 2 used) (try https://en.wikipedia.org/wiki/Shapur_II)

Spot checks:
- /ledger/0, Grumbates: confirmed: 'Between 353 AD and 358 CE ... the Xionites under Grumbates attacked in the eastern frontiers'. Caveat: the page's 'an ancient nomadic tribe of Transoxiana' follows 'probably of the Kidarites tribe' and may describe the Kidarites; the Xionites page lead ('Transoxiana and Bactria') supports the region anyway
- /ledger/4, Xionites: confirmed as noted: 401 is not on the page (confidence 1 is honest); 'until the mid-5th century AD'
- /ledger/1, Xionites: not on page as a dated event; the note says so (confidence 1); 'At the end of the 4th century AD, the Kidarites were pushed into Gandhara' confirmed
- /identity/capitals/0, Xionites: confirmed: 'Some Chionites are known to have ruled in Chach (modern Tashkent)'

Area: The Xionites page has no infobox.

## southern-xiongnu (fix)

Findings:
- /ledger/0/confidence [applied by reviewer]: The 48 found event was at confidence 3, but its region is the Cliopatria 51 shape and the page names no boundary. Evidence: Xiongnu page: 'a confederation of eight Xiongnu tribes in Bi's power base in the south'; the event's own note: 'The page names the base, not a boundary.' Fix: 3 -> 2, with a note (reviewer ia-01-b, 2026-10-18).
- /ledger/1/confidence [applied by reviewer]: The 216 dissolve was at confidence 3, but its region is the 91 shape carried forward and the page names no land. Evidence: Xiongnu page: 'In 216, he detained Huchuquan in the city of Ye and reorganized the last vestiges of the Southern Xiongnu into the Five Divisions'; the event's note: 'The shape is the researcher's reading'. Fix: 3 -> 2, with a note (reviewer ia-01-b, 2026-10-18).
- /keyframe_review/4/note [applied by reviewer]: The 106-215 keyframe (the 91 shape carried forward) did not say that Cliopatria's Xianbei shapes of 106-196, and the xianbei dossier's keyframes from 91, cover almost all of it. Evidence: Gazetteer cells: 203-213 k of this shape's 216 k km2 overlap Xianbei 106/154/161/165/224 and the xianbei K3-K5 correction. Fix: Added an overlap sentence (reviewer ia-01-b, 2026-10-18). The land is to be settled on the xianbei side (see xianbei /ledger/3) or here, but in one dossier only.

Gaps for a gap-filler:
- /keyframe_review/4: the extent in 106-215: the page names only Meiji in Xihe and 'eight frontier commanderies' (thin by design: 2 of 2 pages) (try https://en.wikipedia.org/wiki/Five_Barbarians)

Spot checks:
- /ledger/0, Xiongnu: confirmed (year and actors): 48 AD, 'eight Xiongnu tribes in Bi's power base in the south ... 40,000 to 50,000 men, seceded from Punu's kingdom'
- /ledger/1, Xiongnu: confirmed (year): 'In 216, he detained Huchuquan in the city of Ye and reorganized the last vestiges of the Southern Xiongnu into the Five Divisions'
- /identity/capitals/0, Xiongnu: confirmed: 'ordered to establish his court in Meiji County, Xihe Commandery'; 111.2 E, 39.85 N lies inside the shape's bbox
- /keyframe_review/4, Xiongnu: confirmed: 'against the Wuhuan in Hebei in 188'; Huchuquan 'in 195'

Area: The Xiongnu infobox gives no area figure, and it would describe the whole Xiongnu anyway.

## great-yuan (fix)

Findings:
- /keyframe_review/0/note [applied by reviewer]: The note quoted 'in the southwestern part of the Ferghana valley' as describing Dayuan, but the page says this of Alexandria Eschate. Evidence: Dayuan page: Alexandria Eschate lies 'in the southwestern part of the Ferghana valley'; Dayuan is 'generally accepted as relating to the Ferghana Valley'. Fix: Replaced it with the page's 'generally accepted as relating to the Ferghana Valley' (reviewer ia-01-b, 2026-10-18).

Gaps for a gap-filler:
- /ledger/3: the end in 50 and everything after 100 BC (confidence 1; the Kangju page's control of Dayuan is undated) (try https://en.wikipedia.org/wiki/Fergana_Valley)

Spot checks:
- /ledger/0, Dayuan: confirmed: 'When the Chinese explorer Zhang Qian described Dayuan around 128 BCE'; capital 'Guishan (Khujand)'
- /ledger/1, War_of_the_Heavenly_Horses: confirmed: 'In the autumn of 102 BC, Li set out with an army of 60,000'; forty-day siege
- /ledger/2, War_of_the_Heavenly_Horses: confirmed in substance: Wugua killed, 3,000 horses taken, Meicai enthroned; infobox '104-101 BC', 'Dayuan becomes a puppet-state of Han'; the page gives no year for the peace (101 is an inference, confidence 2 is fair)
- /ledger/3, Kangju: confirmed as noted: 'By this time it had gained control of Dayuan and Sogdiana' (undated); 'In 101 BCE, the Kangju allied themselves with the Dayuan'

Area: The Dayuan page has no infobox area.

## Cross-dossier matrix

- xianbei 91 gain (xiongnu) / xiongnu 91 loss: mismatch. The years agree but the land does not. The xianbei gain (minus(Mongolian Plateau, Xianbei 84), 1,929 k km2) and the xiongnu loss (Xiongnu 84 minus Xiongnu 91, 712 k km2) share only 151 k km2. The xiongnu dossier's own 91 correction cuts it to a 125 k Dzungarian remnant, so its loss region should be the central plateau. 526 k of the xianbei gain lies outside Xiongnu 84, including 206 k of Southern Xiongnu land. Route to ia-01-a (xiongnu /ledger/35) and to the xianbei author.
- xianbei 87 contest_start (xiongnu) / xiongnu 87 contest_start: matched. Same region and years (87-91) on both sides.
- xianbei 154 gain (nobody) / xiongnu 151 dissolve: mismatch. xiongnu dissolves in 151 with xianbei as a successor; xianbei gains Dzungaria from nobody in 154. The land overlaps by only 43 of 449 k km2.
- xianbei 91 gain (xiongnu) / southern-xiongnu 48 found: mismatch. Both dossiers in this batch claim about 206 k km2 (the Ordos-Hetao frontier) from 91 to 216; there is no loss in southern-xiongnu.
- xianbei 205 split (Budugen and Fuluohan (Xianbei groups)) / no dossier: exception. Not a state with a dossier. Its region is still faulty (see the xianbei fixes).
- wusun -132 gain (yuezhi) / yuezhi -132 loss: matched. yuezhi /ledger/6 loses Semirechye to wusun at confidence 3.
- xiongnu -132 vassal_start (wusun) / wusun -132 found: exception. The vassalage is recorded on the suzerain's side (xiongnu /ledger/9 and /ledger/16, -132 to -115); the wusun notes acknowledge it.
- wusun 91 loss (nobody) / no dossier: exception. Counterpart nobody, confidence 1.
- kidarites 360 gain (kushano-sasanian-kingdom) / kushano-sasanian-kingdom 0 : exception. No dossier yet; listed in counterparts_needing_dossiers (sa-02).
- kidarites 387 loss (xionites) / xionites 387 gain: matched. The same 145 k km2 on both sides.
- kidarites 390 gain (Kushan remnants in Gandhara) / no dossier: exception. Not a state with a dossier.
- kidarites 402 gain (xionites) / xionites 401 dissolve: matched. xionites dissolves in 401 with kidarites (and white-huns) as successors on the same 410 k km2.
- kidarites 466 loss (white-huns) / white-huns 0 : exception. white-huns belongs to another part of ia-01 that has not written it yet; the 450-466 contest is the same.
- kidarites 466 loss (sasanian-empire) / sasanian-empire 0 : exception. me-06 has not run yet.
- southern-xiongnu 48 found (-) / xiongnu 48 split: matched. xiongnu /ledger/27 splits off southern-xiongnu on the Southern Xiongnu 51 shape.
- southern-xiongnu 216 dissolve (cao-cao) / cao-cao 0 : exception. ea-03 has not run yet.
- great-yuan -102 contest_start (han-dynasty) / han-dynasty 0 : exception. ea-02 has not run yet. han-dynasty should also carry vassal_start for great-yuan (-101), wusun (-51) and southern-xiongnu (50).
- great-yuan -128 found (-) / yuezhi -126 keyframe: mismatch. yuezhi /keyframe_review/6 (-126..-111) keeps the whole Ferghana basin (42 k km2 of overlap) while great-yuan holds it from -128; the author flagged it. Route to ia-01-a: remove Ferghana from yuezhi -126..-111.
- great-yuan 50 dissolve (kushan-empire) / kushan-empire 0 : exception. sa-02 has not run yet; kangju has no dossier and is listed.

## Problems

- Brief conflict: the reviewer brief says not to edit dossiers, but the orchestrator's adjustment allows small page-verified fixes. Ten were applied in place and each re-validated: xianbei 2, wusun 1, kidarites 3, southern-xiongnu 3, great-yuan 1. Every edit is tagged '(reviewer ia-01-b, 2026-10-18)'.
- Every page opened loaded: Xianbei, Tanshihuai, Kebineng, Battle of Ikh Bayan, Wusun, Yueban, Kidarites, Peroz I, Hephthalites, Kushano-Sasanian Kingdom, Xionites, Grumbates, Xiongnu, Dayuan, War of the Heavenly Horses, Kangju.
- Of the neighbour dossiers, only xiongnu and yuezhi exist (ia-01-a). han-dynasty, protectorate-of-the-western-regions, goguryeo, kushan-empire, sasanian-empire, white-huns, gupta-empire, cao-wei, rouran-khaganate, western-jin, cao-cao and xin-dynasty are not written yet, so their counterparts count as exceptions.
- Two fixes for ia-01-a came out of the cross-checks: xiongnu /ledger/35 (the 91 loss region shares only 151 k km2 with the xianbei gain) and yuezhi /keyframe_review/6 (Ferghana -126..-111).
- The wake note asked for a thread reply; none was sent, because the computed task forbids mcp__hearthbot__ tools.
