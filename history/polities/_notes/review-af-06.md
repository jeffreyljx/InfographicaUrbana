# Review of batch af-06 (Congo basin and Angola), 2026-10-19

Reviewer: adversarial review per history/briefs/reviewer-brief.md with the orchestrator's adjustments (page budgets, 4 spot checks per dossier, small verified fixes applied in place). Machine copy: history/notes/phase-b/reviews/af-06.json.

## Verdicts

| slug | verdict | applied fixes | open findings |
| --- | --- | --- | --- |
| kingdom-of-kongo | fix | 2 | 3 |
| kingdom-of-lunda | thin | 0 | 4 |
| kingdom-of-ndongo | fail | 0 | 3 |
| kingdom-of-matamba | fail | 0 | 3 |
| kingdom-of-kasanje | thin | 0 | 2 |
| kingdom-of-loango | thin | 0 | 1 |
| luba-empire | thin | 1 | 2 |
| kingdom-of-kazembe | fix | 1 | 1 |
| yeke-kingdom | fail | 0 | 2 |
| kuba-kingdom | thin | 0 | 2 |
| zanzibari-domain-of-tippu-tip | fix | 2 | 1 |
| congo-free-state | thin | 0 | 3 |
| portuguese-angola | fail | 0 | 5 |

Mechanical checks: the validator (--resolve) passed all 13 dossiers with 0 errors; the one warning (portuguese-angola /ledger/13, Matamba vassal_start without an end) is a finding below. Every region resolves. After the reviewer's edits, the four edited files validate with 0 errors and 0 warnings.

## The overlap problem (why four dossiers fail)

Shapes resolved with tools/gazetteer.py (H3 r5 cells, about 253 km2 each):

| shape A | shape B | cells of B inside A | years both alive |
| --- | --- | --- | --- |
| kingdom-of-ndongo_1518 (region Ndongo, 527) | kingdom-of-matamba_1530 (Malanje, 305) | 305 (all) | 1530-1671 |
| kingdom-of-ndongo_1518 | kingdom-of-kasanje_1620 (118) | 118 (all) | 1620-1671 |
| kingdom-of-matamba_1530 | kingdom-of-kasanje_1620 | 118 (all) | 1620-1744 (Matamba's own ledger loses it in 1683) |
| portuguese-angola_1671 (644) | kingdom-of-matamba_1530 | 305 (all) | 1671-1744 |
| portuguese-angola_1671 / _1885 | kingdom-of-kasanje_1620 | 118 (all) | 1671-1910 (PA's own ledger gains it in 1910) |
| kingdom-of-ndongo_1518 | portuguese-angola_1582 (225) | 108 | 1582-1671 (Ndongo's keyframe never drops its 1582/1602 losses) |
| yeke-kingdom_1867 (Katanga, 1,628) | luba-empire_1700 (909) | 909 (all, with the Luba capital) | 1867-1889 |
| yeke-kingdom_1867 | kingdom-of-lunda_1856 (1,014) | 443 | 1867-1887 |
| kingdom-of-lunda_1856 | luba-empire_1700 | 297 | 1856-1887 |
| Lunda /ledger/1 (Kasai 120 km, 1,383) | kuba-kingdom_1625 (346) | 236 | 1720-1884 |
| Kasanje /ledger/1 (Kwango 120 km, 1,042) | kingdom-of-kongo_1662 (429) | 85 | 1657- |
| kingdom-of-kongo_1885 (Mbanza Kongo 100 km, 118) | congo-free-state_1885 | 28 | 1885-1914 |

The root cause of the Angolan cluster is the gazetteer entry 'Ndongo' (= Luanda + Bengo + Cuanza Norte + Malanje), which the author used for Ndongo and for the Portuguese conquest of 1671 while using Malanje alone for Matamba and a Kwango band in Malanje for Kasanje; Matamba and Kasanje also share one capital point (the gazetteer's Malanje). In the Katanga cluster the Yeke shape is the whole Katanga province, which contains the gazetteer's 'Luba (region)' entirely.

## kingdom-of-kongo: fix

- **APPLIED** `/ledger/11`: The 1859 vassalage was typed 'rename' with no counterpart, so it did not mirror portuguese-angola's vassal_start of 1859 (a rename is a dynasty change).
  - Evidence: Kingdom of Kongo page: 'Portugal thus gained nominal authority over Kongo when Pedro gained control of it in 1859'; 'From 1862 to 1914, it functioned intermittently as a vassal state of the Kingdom of Portugal'. portuguese-angola /ledger/14 is vassal_start 1859 with counterpart kingdom-of-kongo.
  - Fix: Changed to vassal_start, counterpart portuguese-angola, region Mbanza Kongo 100 km (the same region as the mirror), confidence 2 kept; reviewer tag in the note.
- **APPLIED** `/ledger/14`: No vassal_end mirrored portuguese-angola's vassal_end of 1914.
  - Evidence: Kingdom of Kongo page: 'In 1914, following the Portuguese suppression of a Kongo revolt, Portugal abolished the titular monarchy.' portuguese-angola /ledger/19 is vassal_end 1914, counterpart kingdom-of-kongo.
  - Fix: Added vassal_end 1914 (counterpart portuguese-angola, Mbanza Kongo 100 km, confidence 3) before the dissolve; the file validates with 0 errors, 0 warnings.
- **OPEN** `/identity/predecessors`: Advisory (non-blocking): the predecessors 'mbata' and 'mpemba-kasi' are slugs with no dossier, no row in polities.csv and no entry in the author's counterparts_needing_dossiers.
  - Evidence: polities.csv has neither slug; the author's report lists only Soyo, the IAC, Chokwe, Viye, Kakongo/Ngoyo, Zanzibar and the Dutch WIC.
  - Fix: List both under counterparts_needing_dossiers (done in this review's report) or give them as names in the note.
- **OPEN** `/keyframe_review/6/correction`: Advisory (non-blocking): the 1885-1914 Mbanza Kongo disc (100 km) spills 28 cells (about 7,000 km2) into the Democratic Republic of the Congo, which is congo-free-state land from 1885 (its K0 and K1 contain those cells).
  - Evidence: Gazetteer resolve: kingdom-of-kongo_1885 118 cells, 28 of them inside congo-free-state_1885; the page puts the remaining kingdom in Portuguese Angola after Berlin.
  - Fix: Intersect the disc with {country: Angola} in /keyframe_review/6, /ledger/12 and /ledger/13 (the minus terms), /ledger/15 and the vassal events, consistently.
- **OPEN** `/ledger/15`: Advisory (routed to portuguese-angola): the 1914 dissolve names portuguese-angola, but that dossier has no 1914 gain of the São Salvador district and its 1885-1919 shape leaves it out, so the district belongs to nobody 1914-1919.
  - Evidence: portuguese-angola /ledger/19 is only a vassal_end; portuguese-angola_1885 (K3) does not contain the Mbanza Kongo disc (0 cells overlap).
  - Fix: portuguese-angola adds a 1914 gain (counterpart kingdom-of-kongo, Mbanza Kongo 100 km within Angola) and includes the district in its 1914-1919 shape.
- Thin (for a gap-filler):
  - `/keyframe_review/4`: Extent of the kingdom during the civil war (Nsundi and Mbata 'splitting off', undated and unlocated) and after 1709 ('fiefdoms recognising the King of Kongo but not truly under his control'); both keyframes are the 1662 shape at confidence 1, and the 1709 'gain' re-adds land the 1670 keyframe never removed. (try https://en.wikipedia.org/wiki/Pedro_IV_of_Kongo)
  - `/ledger/1`: Afonso I's conquests 'to the south and east' (1509-1540s) have no year or place (confidence 1). (try https://en.wikipedia.org/wiki/Afonso_I_of_Kongo)
  - `/ledger/12`: The 1885 division at Berlin is confidence 1 for both halves; the Kongo-Angola boundary line is not on the pages opened. (try https://en.wikipedia.org/wiki/Berlin_Conference)
- Spot checks: /ledger/0 confirmed (Kingdom_of_Kongo), /ledger/2 confirmed (Kingdom_of_Kongo), /ledger/3 confirmed (Kingdom_of_Kongo), /ledger/7 confirmed (Soyo), /ledger/8 confirmed (Kongo_Civil_War), /ledger/9 confirmed (Kongo_Civil_War), /ledger/11 confirmed (Kingdom_of_Kongo), /ledger/15 confirmed (Kingdom_of_Kongo).
- Area: page 129,400 km2 (1623), Cliopatria 131,582 km2, ratio 1.02, acknowledged True.

## kingdom-of-lunda: thin

- **OPEN** `/ledger/1/region`: Advisory (non-blocking): the 1720s gain is the whole Kasai river widened by 120 km: 1,383 cells (about 350,000 km2), more than the kingdom's 19th-century height, from the Angolan source to the Congo confluence, and 236 cells of it lie inside kuba-kingdom's shape (1625-1884).
  - Evidence: Kingdom of Lunda page: 'pushing the boundary of Lunda past the Kasai River to the west' (a crossing, not the river's length). Gazetteer resolve: Kasai 120 km 1,383 cells; overlap with kuba-kingdom_1625 236 cells.
  - Fix: Restrict the region to the crossing west of Musumba, e.g. intersect the Kasai band with the 309 km disc or with Lunda Norte/Lunda Sul, and give the land a trace in a keyframe (the 1709-1855 disc does not change).
- **OPEN** `/keyframe_review/2/correction`: Advisory (non-blocking, routed with yeke-kingdom): the 1856-1887 disc (309 km) overlaps luba-empire_1700 by 297 cells (about 75,000 km2, a third of the Luba shape) and yeke-kingdom_1867 by 443 cells, while /ledger/2 takes the ring from 'nobody'.
  - Evidence: Gazetteer resolve of the three shapes. The page gives the direction of growth: 'extending their kingdom through southwest Katanga into Angola and north-western Zambia'.
  - Fix: Shift the extra 150,000 km2 west and south (Lunda Norte, Lunda Sul, Moxico, north-western Zambia) rather than a disc, or subtract luba-empire's region; name the counterpart where land is taken.
- **OPEN** `/ledger/3`: Advisory (non-blocking): the dissolve names 'Chokwe invaders' as counterpart, while congo-free-state /ledger/1 gains the Lunda land in 1887 with counterpart kingdom-of-lunda; neither side records the other, and the Angolan half goes to nobody.
  - Evidence: Kingdom of Lunda page: 'At the start of the colonial era (1884), the Lunda heartland was divided' between Portuguese Angola, Leopold II's Congo Free State and British territory; the infobox ends the state in 1887.
  - Fix: Add 1887 losses to congo-free-state (DRC part) and portuguese-angola (Angolan part, then mirrored there), keeping the dissolve; or make the CFS gain counterpart match.
- **OPEN** `/wars/0`: Advisory (non-blocking): the Chokwe war 'from' 1801 is a placeholder; the page says only 'the 19th century' (the note says so).
  - Evidence: Kingdom of Lunda page; Chokwe people page 'By 1900'.
  - Fix: Keep as is or narrow when a page dates the Chokwe attacks.
- Thin (for a gap-filler):
  - `/ledger/2`: The doubling to 300,000 km2 has no year (1856 is Cliopatria's shape break, confidence 1). (try https://en.wikipedia.org/wiki/Mwata_Yamvo)
  - `/ledger/3`: No date for the Chokwe sack of Musumba or the end of the kingdom beyond the infobox's 1887. (try https://en.wikipedia.org/wiki/Chokwe_people)
  - `/keyframe_review/1`: Kazembe's split (c. 1740) and the Lunda tributaries are undated; the Lunda shapes are discs. (try https://en.wikipedia.org/wiki/Lunda_people)
- Spot checks: /ledger/0 confirmed (Kingdom_of_Lunda), /ledger/1 confirmed (Kingdom_of_Lunda), /ledger/2 not on page (Kingdom_of_Lunda), /ledger/3 confirmed (Kingdom_of_Lunda).
- Area: page 300,000 km2 (1856), Cliopatria 109,111 km2, ratio 0.36, acknowledged True.

## kingdom-of-ndongo: fail

- **OPEN** `/keyframe_review/0/correction`: BLOCKING: the shape swallows two sibling states. The gazetteer region 'Ndongo' is Luanda + Bengo + Cuanza Norte + Malanje provinces, so it contains all of kingdom-of-matamba's shape (Malanje, 305 cells, 1530-1744), all of kingdom-of-kasanje's (118 cells, from 1620) and both of their capital points (16.34 E, 9.54 S), for the whole of 1518-1671.
  - Evidence: Gazetteer regions.jsonl: Ndongo = union of admin1 Luanda, Bengo, Cuanza Norte, Malanje. Resolve: ndongo_1518 527 cells; overlap with matamba_1530 305 (100 percent), with kasanje_1620 118 (100 percent). Matamba page: Matamba lay 'in what is now the Baixa de Cassange region of Malanje Province' and paid tribute to Kongo in 1530; the author's own notes treat Matamba as a separate state until Nzinga's union of 1631.
  - Fix: Redraw Ndongo without Matamba and Kasanje: e.g. {minus: [{region: Ndongo}, <the Matamba shape>]} where the Matamba shape is narrowed to the Baixa de Cassange (eastern Malanje), keeping western Malanje (Pungo Andongo, the Kwanza islands) in Ndongo if a page supports it; apply the same region to /ledger/0, /ledger/6-8 and the successor land.
- **OPEN** `/keyframe_review/0/correction`: Part of the blocking redraw: the 1518-1671 shape also contains Luanda (Portuguese from 1575) and the Kwanza corridor lost in 1582 and 1602: 108 cells overlap portuguese-angola_1582.
  - Evidence: /ledger/1 and /ledger/2 are losses to portuguese-angola; the keyframe does not change. Ndongo page: Massangano 1582, Cambambe 1602; History of Angola: the colony founded 1575.
  - Fix: Subtract the Luanda disc from 1575 and the Kwanza discs from 1582/1602 (new keyframes 1575, 1582, 1602 or a correction that leaves them out).
- **OPEN** `/ledger/5`: The 1626 installation of a Portuguese client king is typed 'rename', so portuguese-angola's vassal_start of 1626 (and vassal_end of 1671) has no mirror here.
  - Evidence: Ndongo page: Fernão de Sousa installed Hari a Kiluanji (1626), later replaced by Filipe Hari a Ngola; portuguese-angola /ledger/6 vassal_start 1626 and /ledger/11 vassal_end 1671, counterpart kingdom-of-ndongo.
  - Fix: Add vassal_start 1626 (counterpart portuguese-angola, the client kingdom's land) and vassal_end 1671, or keep the rename and add the vassal_start beside it.
- Thin (for a gap-filler):
  - `/certainty/1`: Where the 1599 Ndongo-Portugal border ran. (try https://en.wikipedia.org/wiki/Kingdom_of_Ndongo)
  - `/ledger/0`: When Ndongo stopped being a Kongo vassal. (try https://en.wikipedia.org/wiki/Ngola_Kiluanji)
- Spot checks: /ledger/0 confirmed (Kingdom_of_Ndongo), /ledger/1 confirmed (Kingdom_of_Ndongo), /ledger/2 confirmed (Kingdom_of_Ndongo), /ledger/3 confirmed (Kingdom_of_Ndongo), /ledger/5 confirmed (Kingdom_of_Ndongo), /ledger/8 confirmed (Kingdom_of_Ndongo), /ledger/7 confirmed (Nzinga_of_Ndongo_and_Matamba).
- Area: the pages give none; nothing to compare (proxy shape, acknowledged in the keyframe note).

## kingdom-of-matamba: fail

- **OPEN** `/keyframe_review/0/correction`: BLOCKING: the 1530-1744 shape (all of Malanje Province) contains the whole of kingdom-of-kasanje's shape (118 cells, 39 percent of Matamba) through 1744, although this dossier's own /ledger/6 loses that band to Kasanje in September 1683 and Kasanje is founded there in 1620; the 1683 loss leaves no trace in the keyframes.
  - Evidence: Resolve: matamba_1530 305 cells, kasanje_1620 118 cells, overlap 118. Matamba page: the 1683 treaty, 'signed 7 September 1683', made Verónica 'acknowledge the independence of Kasanje'. Kasanje page: 'formed in 1620 ... on the upper Kwango River'.
  - Fix: Split the keyframe at 1683 (Malanje minus the Kasanje band from 1683), or subtract the band from 1620 if Kasanje was never Matamba's, and make /ledger/6 agree; give Matamba and Kasanje different capital points (both are the gazetteer's Malanje, 16.34 E 9.54 S).
- **OPEN** `/ledger/6`: No vassal_start mirrors portuguese-angola's vassal_start of 7 September 1683.
  - Evidence: Matamba page: Verónica 'accepted nominal vassalage' in the treaty 'signed 7 September 1683'; portuguese-angola /ledger/13 is vassal_start 1683-09, counterpart kingdom-of-matamba.
  - Fix: Add vassal_start 1683-09 (counterpart portuguese-angola, the Matamba shape, confidence 2), ending at the dissolve or at a vassal_end.
- **OPEN** `/ledger/7`: The 1744 dissolve to portuguese-angola has no mirror: portuguese-angola records no 1744 gain or vassal_end and its shapes do not reach Matamba until 1920 (apart from the Ndongo-region error), and the page does not end the kingdom in 1744.
  - Evidence: Matamba page: Ana II 'faced a Portuguese invasion in 1744' and 'signed a treaty of vassalage' which 'had little effect on the real sovereignty'; a king was 'crowned ... around 1810'; the state 'was integrated into Portuguese Angola in the late nineteenth century'. Only the lead's '(pre-1550-1744)' supports 1744.
  - Fix: Either extend the life to the integration (a gap-filler dates it) with 1744 as a renewed vassalage, or keep 1744 and have portuguese-angola gain the land in 1744 and close its vassal relation; the two dossiers must agree.
- Thin (for a gap-filler):
  - `/ledger/0`: Matamba's founding (only a 1530 documentary mention, confidence 1). (try https://en.wikipedia.org/wiki/Kingdom_of_Matamba)
  - `/ledger/7`: The year Matamba was integrated into Portuguese Angola. (try https://en.wikipedia.org/wiki/History_of_Angola)
- Spot checks: /ledger/0 confirmed (Kingdom_of_Matamba), /ledger/1 confirmed (Nzinga_of_Ndongo_and_Matamba), /ledger/2 confirmed (Kingdom_of_Matamba), /ledger/6 confirmed (Kingdom_of_Matamba), /ledger/7 confirmed (Kingdom_of_Matamba).
- Area: the pages give none; nothing to compare (proxy shape, acknowledged in the keyframe note).

## kingdom-of-kasanje: thin

- **OPEN** `/ledger/1/region`: Advisory (non-blocking): the 1657 Bembe gain is the whole Kwango river widened by 120 km: 1,042 cells (about 264,000 km2, nine times the state's own shape), from Angola to the Kasai confluence in the DRC, 85 cells of it inside kingdom-of-kongo's shape, with counterpart 'nobody'.
  - Evidence: Kasanje page: 'significant taking of areas in Bembe in 1657' (Bembe unlocated). Resolve: Kwango 120 km 1,042 cells; overlap with kingdom-of-kongo_1662 85 cells.
  - Fix: Keep the event at confidence 1 but give it a small region next to the state (e.g. the Kwango band within Malanje and Lunda Norte, or a disc), and a trace in a keyframe if it is drawn.
- **OPEN** `/identity/capitals/0`: Advisory (non-blocking): the capital point is the gazetteer's Malanje, the same point as kingdom-of-matamba's capital.
  - Evidence: Both dossiers use 16.34 E, 9.54 S; the Kasanje page names no capital ('located on the upper Kwango River').
  - Fix: Move the stand-in to the Kwango (Cassange in the Baixa de Cassange) once the gazetteer has it.
- Thin (for a gap-filler):
  - `/ledger/1`: Where Bembe lay. (try https://en.wikipedia.org/wiki/Imbangala)
  - `/identity/capitals/0`: The capital of Kasanje. (try https://en.wikipedia.org/wiki/Imbangala)
- Spot checks: /ledger/0 confirmed (Kingdom_of_Kasanje), /ledger/1 confirmed (Kingdom_of_Kasanje), /ledger/2 confirmed (Kingdom_of_Matamba), /ledger/3 confirmed (Kingdom_of_Kasanje).
- Area: the pages give none; nothing to compare (proxy shape, acknowledged in the keyframe note).

## kingdom-of-loango: thin

- **OPEN** `/ledger/1/region`: Advisory (non-blocking): the 1600 extent includes Cabinda, the land of the separate Vili states Kakongo and Ngoyo, which the page lists among Kongo's titles in 1535.
  - Evidence: Loango page: 'Loango influence extended from Cape St Catherine in the north to almost the mouth of the Congo River' (influence, 17th century) and c. 1600 the king gave 'command over four provinces' (Kaye, Boke, Selage, Kabango).
  - Fix: Keep confidence 1 and say in the text that Cabinda is influence, or leave Cabinda out until Kakongo/Ngoyo have dossiers.
- Thin (for a gap-filler):
  - `/ledger/1`: Loango's area and its 17th-century provinces. (try https://en.wikipedia.org/wiki/Vili_people)
  - `/ledger/2`: The treaty that ended Loango (c. 1883) and the fate of the Loango coast before French rule. (try https://en.wikipedia.org/wiki/French_Congo)
- Spot checks: /ledger/0 confirmed (Kingdom_of_Loango), /ledger/1 confirmed (Kingdom_of_Loango), /ledger/2 confirmed (Kingdom_of_Loango).
- Area: the pages give none; nothing to compare (proxy shape, acknowledged in the keyframe note).

## luba-empire: thin

- **APPLIED** `/ledger/2/confidence`: The 1889 dissolve to congo-free-state was confidence 3, but the page puts the hand-over 'later', not in 1889, and does not name the region.
  - Evidence: Luba Empire page: 'In 1889 it was split in two by a succession dispute, ending the unified state, and later joined the Congo Free State.'
  - Fix: Lowered to 2 with a reviewer tag in the note.
- **OPEN** `/ledger`: Advisory (non-blocking, routed with yeke-kingdom): no loss to Msiri is recorded, although the Luba people page says he 'raided and took over the southeastern Shaba region' (undated) and yeke-kingdom's 1870 gain covers the whole Luba shape.
  - Evidence: Luba people page; resolve: luba-empire_1700 909 cells, all inside yeke-kingdom_1867.
  - Fix: Add a loss to yeke-kingdom (confidence 1, south-eastern Katanga) once yeke-kingdom's shape is redrawn; the two must not both hold the Luba heartland 1867-1889.
- **OPEN** `/keyframe_review/1/note`: Advisory (non-blocking): the quote 'By 1870 the empire covered much of what is now the southeast...' is not on the Luba Empire page cited; the nearest sentence is on the Luba people page ('By then ... covered much of what is now the southeastern Democratic Republic of Congo', after Ilunga Kabale's death in 1870).
  - Evidence: Luba Empire and Luba people pages read on 2026-10-19.
  - Fix: Cite https://en.wikipedia.org/wiki/Luba_people for that sentence (it is already in sources).
- Thin (for a gap-filler):
  - `/ledger/0`: Founding year: 1585 (Early Congolese history) against 'Around 1500, possibly earlier' (Luba people) and '?' (Luba Empire infobox). (try https://en.wikipedia.org/wiki/Kalala_Ilunga)
  - `/keyframe_review/1`: Any boundary; the 1700 shape is the gazetteer's confidence-1 'Luba (region)'. (try https://en.wikipedia.org/wiki/Upemba_National_Park)
- Spot checks: /ledger/0 confirmed (Early_Congolese_history), /ledger/1 confirmed (Luba_Empire), /ledger/2 mis-dated (Luba_Empire).
- Area: the pages give none; nothing to compare (proxy shape, acknowledged in the keyframe note).

## kingdom-of-kazembe: fix

- **APPLIED** `/ledger/3`: The 1894 dissolve named congo-free-state and the whole Luapula valley at confidence 3, but the land Kazembe still held in 1894 (the 1867-1894 shape, on the Zambian side) went to Britain; the west bank had been Msiri's since 1867 (/ledger/2).
  - Evidence: Kingdom of Kazembe page: 'After Msiri's death, the Luapula valley was divided in 1894 between Britain' (the eastern shores to the BSAC's North-Eastern Rhodesia) and the Compagnie du Katanga (the western shores); the page presents it as a division, not the end of the kingship. The dossier's own successors give the eastern land to british-africa.
  - Fix: Counterpart changed to british-africa, region to the /keyframe_review/1 correction, confidence 3 to 2; reviewer tag in the note.
- **OPEN** `/end`: Advisory (non-blocking): the page's sovereign end could as well be 1899 (British officers burnt the capital, then indirect rule) as 1894.
  - Evidence: Kingdom of Kazembe page: in 1899 'British officers with Sikh and Nyasaland troops' burnt the capital; the chieftainship survived.
  - Fix: Keep 1894 or move the end to 1899 with 1894-1899 as a vassal relation; say which in notes.
- Thin (for a gap-filler):
  - `/keyframe_review/0`: The kingdom's extent ('west to the Lualaba', 'east to the Luba-Bemba country') is a Luapula band; no area on the page. (try https://en.wikipedia.org/wiki/Mwata_Kazembe)
- Spot checks: /ledger/0 confirmed (Kingdom_of_Kazembe), /ledger/1 confirmed (Kingdom_of_Kazembe), /ledger/2 confirmed (Msiri), /ledger/3 confirmed (Kingdom_of_Kazembe).
- Area: the pages give none; nothing to compare (proxy shape, acknowledged in the keyframe note).

## yeke-kingdom: fail

- **OPEN** `/keyframe_review/1/correction`: BLOCKING: the 1867-1891 shape (all of Katanga province, 1,628 cells) contains the whole of luba-empire's 1700-1889 shape (909 cells, about 230,000 km2) and the Luba capital Mwibele (26.4 E, 8.63 S), and 443 cells of kingdom-of-lunda's 1856-1887 shape, so three states hold the same land 1867-1887.
  - Evidence: Resolve: yeke_1867 1,628 cells; overlap with luba_1700 909 (100 percent), with lunda_1856 443. Gazetteer: 'Luba (region)' = Katanga intersected with 22.5-28.5 E, 5-10 S. Luba people page: Msiri 'raided and took over the southeastern Shaba region'; Yeke Kingdom page gives Bunkeya as capital and 'about half a million square kilometres' with no year and no place.
  - Fix: Redraw as south-eastern Katanga: e.g. {minus: [{admin1: Katanga}, {region: 'Luba (region)'}]} (or Haut-Katanga and Lualaba once the gazetteer has them), and note that the page's half-million km2 then counts tributaries; carry the same region in /ledger/2, /ledger/3 and congo-free-state /ledger/4 and its K0 minus term.
- **OPEN** `/ledger/2`: Part of the blocking redraw: the 1870 gain takes all Katanga from 'nobody' at confidence 1, though the land is Luba's (luba-empire 1700-1889) and partly Lunda's; the page gives no 1870 date.
  - Evidence: Yeke Kingdom page: 'The page gives no years for conquests' (no 1870); luba-empire and kingdom-of-lunda shapes as above.
  - Fix: Name luba-empire (and kingdom-of-lunda if kept) as counterparts for the parts taken, with mirrored losses there, and keep confidence 1.
- Thin (for a gap-filler):
  - `/ledger/2`: Dates and places of Msiri's conquests (Lunda, Luba, Kazembe tributaries). (try https://en.wikipedia.org/wiki/Garanganze)
  - `/keyframe_review/1`: Where the 'half a million square kilometres' lay. (try https://en.wikipedia.org/wiki/Bunkeya)
- Spot checks: /ledger/0 confirmed (Yeke_Kingdom), /ledger/1 confirmed (Msiri), /ledger/2 not on page (Yeke_Kingdom), /ledger/3 confirmed (Yeke_Kingdom).
- Area: page 500,000 km2 (1891), Cliopatria 0 km2, ratio 0.82, acknowledged True.

## kuba-kingdom: thin

- **OPEN** `/ledger/2/counterpart`: Advisory (non-blocking): the 1884 dissolve names congo-free-state, which did not exist until 1 July 1885 and has no gain from Kuba; the infobox successor is the International Association of the Congo.
  - Evidence: Kuba Kingdom page: 'Disestablished: 1884', successor International Association of the Congo, 'Europeans first reached the area in 1884'; Congo Free State page: 'Established: 1 July 1885'. Early Congolese history: the federation maintained itself 'even after King Leopold II ... established the Congo Free State in 1885'.
  - Fix: Use international-association-of-the-congo (listed as needing a dossier) as counterpart, or move the end to the Free State's occupation once a page dates it; the end year is disputed (author-flagged).
- **OPEN** `/ledger/1/region`: Advisory (non-blocking): the early-18th-century gain is the Kasai river widened by 80 km, 903 cells (about 228,000 km2), 2.6 times the kingdom's own shape, along the whole river.
  - Evidence: Kuba Kingdom page: under Kuete M'bogi Kuba 'extended its power further south along the Kasai River'. Resolve: 903 cells against kuba_1625 346.
  - Fix: Restrict to the stretch south of the kingdom (intersect with a disc around Nsheng or with Kasai-Occidental) and keep confidence 1.
- Thin (for a gap-filler):
  - `/identity/capitals/0`: Nsheng (Mushenge) coordinates (the Mushenge page failed for the author). (try https://en.wikipedia.org/wiki/Mushenge)
  - `/ledger/2`: The year the Kuba kingdom lost independence (infobox 1884 against the text). (try https://en.wikipedia.org/wiki/Kuba_people)
- Spot checks: /ledger/0 confirmed (Kuba_Kingdom), /ledger/1 confirmed (Kuba_Kingdom), /ledger/2 confirmed (Kuba_Kingdom).
- Area: page 100,000 km2 (1884), Cliopatria 0 km2, ratio 0.88, acknowledged True.

## zanzibari-domain-of-tippu-tip: fix

- **APPLIED** `/ledger/1`: The 24 February 1887 governorship was typed 'rename', so congo-free-state's vassal_start of February 1887 had no mirror.
  - Evidence: Tippu Tip page: Stanley 'proposed that Tippu Tip be made governor of the Stanley Falls District'; 'on February 24, 1887, Tippu Tip accepted.' congo-free-state /ledger/2 vassal_start 1887-02, counterpart this slug.
  - Fix: Changed to vassal_start, counterpart congo-free-state, region Maniema, confidence 3 kept; reviewer tag in the note.
- **APPLIED** `/ledger/2`: No vassal_end mirrored congo-free-state's vassal_end of March 1892.
  - Evidence: Congo Arab war page: 'In March and April 1892, Tippu Tip's son Sefu bin Hamid began attacking Congo Free State personnel in eastern Congo.' congo-free-state /ledger/5 vassal_end 1892-03.
  - Fix: Added vassal_end 1892-03 (counterpart congo-free-state, Maniema, confidence 2); the file validates with 0 errors, 0 warnings.
- **OPEN** `/keyframe_review/0`: Advisory (non-blocking): the keyframe and the capital end in 1893 while the life and the dissolve run to January 1894.
  - Evidence: Congo Arab war page: 'Within three days, the remaining forts ... surrendered' (9 January 1894); Kasongo fell 22 April 1893.
  - Fix: Run the keyframe to 1894 (the Kasongo and Nyangwe losses are already in the ledger) or end the life in 1893.
- Thin (for a gap-filler):
  - `/ledger/0`: The Sultan of Zanzibar's claim on the domain 1884-1887 ('for himself and for the Sultan of Zanzibar') is recorded in no dossier; the domain's extent beyond Maniema (Stanley Falls, Rumaliza's Ujiji) is undrawn. (try https://en.wikipedia.org/wiki/Rumaliza)
- Spot checks: /ledger/0 confirmed (Tippu_Tip), /ledger/1 confirmed (Tippu_Tip), /ledger/3 confirmed (Congo_Arab_war), /ledger/5 confirmed (Congo_Arab_war), /ledger/7 confirmed (Congo_Arab_war).
- Area: the pages give none; nothing to compare (proxy shape, acknowledged in the keyframe note).

## congo-free-state: thin

- **OPEN** `/keyframe_review/0`: Advisory (non-blocking): one keyframe covers 1885-1894 while the ledger adds the Lunda heartland (1887), the Luba empire (1889) and Katanga (1891): the 1890 anchor drawn from the keyframe would leave the Lunda and Luba lands to nobody (both states have ended by then).
  - Evidence: /ledger/1, /ledger/3 and /ledger/4 against congo-free-state_1885 (minus Katanga, Maniema, Lunda, Luba); kingdom-of-lunda ends 1887, luba-empire 1889.
  - Fix: Add keyframes at 1887, 1889 and 1891 (each minus one fewer term), or confirm that the compiler applies ledger gains between keyframes.
- **OPEN** `/ledger/1`: Advisory (non-blocking): the 1887 Lunda gain has no mirror; kingdom-of-lunda's dissolve names 'Chokwe invaders'.
  - Evidence: Kingdom of Lunda page (1884 division, infobox end 1887).
  - Fix: Settle with kingdom-of-lunda which counterpart takes the land in 1887.
- **OPEN** `/ledger/0`: Advisory (non-blocking): kingdom-of-kongo's 1885 loss to this state and kuba-kingdom's 1884 dissolve to it have no explicit gain here; the land is inside the founding shape (author's note: 'the Kuba and the Kongo lands are inside it').
  - Evidence: kingdom-of-kongo /ledger/13, kuba-kingdom /ledger/2; overlap of congo-free-state_1885 with kuba_1625 300 cells.
  - Fix: Accept as absorbed in the found event, or add gains dated 1885-07 for the matrix.
- Thin (for a gap-filler):
  - `/ledger/3`: When the Luba lands actually 'joined the Congo Free State' (the page says only 'later'; confidence 1). (try https://en.wikipedia.org/wiki/Luba_people)
  - `/ledger/9`: Lado Enclave extent and the date of effective occupation (Rejaf, 17 February 1897); Central Equatoria is a stand-in, confidence 1. (try https://en.wikipedia.org/wiki/Lado_Enclave)
  - `/certainty/1`: The 1885-1894 boundary treaties with France, Portugal, Britain and Germany. (try https://en.wikipedia.org/wiki/Berlin_Conference)
- Spot checks: /ledger/0 confirmed (Congo_Free_State), /ledger/3 mis-dated (Luba_Empire), /ledger/4 confirmed (Msiri), /ledger/9 confirmed (Congo_Free_State), /ledger/12 confirmed (Congo_Free_State).
- Area: page 2,345,409 km2 (1908), Cliopatria 0 km2, ratio 0.91, acknowledged True.

## portuguese-angola: fail

- **OPEN** `/keyframe_review/2/correction`: BLOCKING: the 1671-1884 and 1885-1919 shapes include the gazetteer region 'Ndongo', which contains Malanje Province: all of kingdom-of-matamba (305 cells, to 1744) and kingdom-of-kasanje (118 cells, to 1910) are drawn as the colony from 1671, contradicting this keyframe's own note ('Matamba ..., Kasanje and Kongo are separate states, not part of the colony, until their own events') and this dossier's /ledger/18 (Kasanje gained only in 1910).
  - Evidence: Gazetteer: Ndongo = Luanda + Bengo + Cuanza Norte + Malanje. Resolve: portuguese-angola_1671 644 cells, overlap with matamba 305 and kasanje 118; portuguese-angola_1885 overlap with kasanje 118. History of Angola: 'The Kingdom of Ndongo submitted to the Portuguese Crown in 1671' (Ndongo only).
  - Fix: Use the corrected Ndongo shape (without Matamba's and Kasanje's land) in /keyframe_review/2 and /3 and in /ledger/6, /ledger/11, /ledger/12.
- **OPEN** `/keyframe_review/3/correction`: Part of the blocking redraw: the 1885-1919 shape leaves out the land of its own 1885 gain from Kongo (/ledger/16: only 34 of 198 cells inside) and of the 1910 Kasanje gain (inside only through the Ndongo-region error), and there is no 1914 gain of the São Salvador district though kingdom-of-kongo dissolves to this state in 1914.
  - Evidence: Resolve of /ledger/16 against portuguese-angola_1885; kingdom-of-kongo /ledger/15 (dissolve 1914, counterpart portuguese-angola); Kongo page: 'The remaining territories of the kingdom were assimilated into the colony of Portuguese Angola'.
  - Fix: Add the 1885 Kongo land to the 1885 keyframe, a 1910 keyframe with Kasanje, and a 1914 gain (counterpart kingdom-of-kongo, Mbanza Kongo 100 km within Angola) with a keyframe from 1914.
- **OPEN** `/ledger/13`: The Matamba vassal_start (1683) has no end although kingdom-of-matamba dissolves to this state in 1744; no 1744 event here (validator warning).
  - Evidence: Matamba page: the 1744 invasion and a renewed treaty of vassalage; integration 'in the late nineteenth century'.
  - Fix: Agree with kingdom-of-matamba on its end: either a 1744 vassal_end plus gain, or a later integration year with vassal_end then.
- **OPEN** `/ledger/15`: Advisory (non-blocking): Cabinda (1885) is a 'gain' here but a vassal_start (protectorate) in portuguese-empire /ledger/81, and the Dutch years are an occupation by 'Dutch West India Company' here but a loss/gain with dutch-republic in portuguese-empire /ledger/28 and /33; the two Portuguese dossiers also both draw Luanda, Benguela and (from 1891) all of Angola up to 1910.
  - Evidence: portuguese-empire ledger; History of Angola: Cabinda 'ceded to Portugal on the legal basis of the Treaty of Simulambuko Protectorate'.
  - Fix: Route to the orchestrator (author-flagged overlap): pick one owner for Angola 1575-1910 and one counterpart spelling for the Dutch; make Cabinda a vassal_start or say why it is a gain.
- **OPEN** `/ledger/2`: Advisory (non-blocking): Benguela at 1601 is a placeholder ('17th century', confidence 1); the page gives no year.
  - Evidence: Portuguese Angola page: 'In the 17th century came the settlement of Benguela even farther to the south.'
  - Fix: Keep confidence 1; a gap-filler dates it (Benguela page).
- Thin (for a gap-filler):
  - `/ledger/2`: Benguela's founding year. (try https://en.wikipedia.org/wiki/Benguela)
  - `/ledger/20`: The 1885-1920 conquests (Dembos, Ovimbundu, Cuanhama, Lunda/Chokwe north-east); 1920 is a bridge from 'nobody' at confidence 1. (try https://en.wikipedia.org/wiki/Portuguese_colonial_campaigns_in_Angola)
- Spot checks: /ledger/0 confirmed (History_of_Angola), /ledger/9 confirmed (Nzinga_of_Ndongo_and_Matamba), /ledger/12 confirmed (History_of_Angola), /ledger/13 confirmed (Kingdom_of_Matamba), /ledger/17 confirmed (Portuguese_Angola), /ledger/21 confirmed (History_of_Angola), /ledger/22 confirmed (History_of_Angola), /ledger/2 not on page (Portuguese_Angola).
- Area: page 1,246,700 km2 (1975), Cliopatria 0 km2, ratio 1.0, acknowledged True.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| kingdom-of-kongo 1656 loss (Soyo) | none | exception | Soyo has no dossier; listed by the author as county-of-soyo. |
| kingdom-of-kongo 1859 vassal_start (portuguese-angola) | portuguese-angola 1859 vassal_start | matched | Kongo side was a 'rename'; changed to vassal_start by the reviewer. |
| kingdom-of-kongo 1885 loss (portuguese-angola) | portuguese-angola 1885 gain | mismatch | Years and counterparts agree, but portuguese-angola's 1885 keyframe holds only 34 of the 198 cells it gains. |
| kingdom-of-kongo 1885 loss (congo-free-state) | congo-free-state 1885 found | exception | No explicit gain; the land lies inside the Free State's founding shape. |
| kingdom-of-kongo 1914 vassal_end (portuguese-angola) | portuguese-angola 1914 vassal_end | matched | Kongo side added by the reviewer. |
| kingdom-of-kongo 1914 dissolve (portuguese-angola) | none | missing | portuguese-angola has no 1914 gain of the São Salvador district. |
| kingdom-of-lunda 1887 dissolve (Chokwe invaders) | congo-free-state 1887 gain | mismatch | CFS gains from kingdom-of-lunda; Lunda's dissolve names the Chokwe; the Angolan part goes to nobody. |
| kingdom-of-ndongo 1582 loss (portuguese-angola) | portuguese-angola 1582 gain | matched | Massangano. |
| kingdom-of-ndongo 1602 loss (portuguese-angola) | portuguese-angola 1602 gain | matched | Cambambe. |
| portuguese-angola 1626 vassal_start (kingdom-of-ndongo) | kingdom-of-ndongo 1626 rename | mismatch | Ndongo records the client kingship as a rename; no vassal_start/vassal_end there. |
| kingdom-of-ndongo 1671 dissolve (portuguese-angola) | portuguese-angola 1671 gain | matched | But both shapes carry Matamba's and Kasanje's land (Ndongo region includes Malanje). |
| kingdom-of-matamba 1683 loss (kingdom-of-kasanje) | kingdom-of-kasanje 1683 gain | matched | Treaty of 7 September 1683; Matamba's keyframe does not drop the band. |
| portuguese-angola 1683 vassal_start (kingdom-of-matamba) | none | missing | Matamba has no vassal_start. |
| kingdom-of-matamba 1744 dissolve (portuguese-angola) | none | missing | portuguese-angola has no 1744 gain or vassal_end; the page keeps Matamba alive as a vassal. |
| kingdom-of-kasanje 1910 dissolve (portuguese-angola) | portuguese-angola 1910 gain | matched | Page: 1910-1911. |
| kingdom-of-kasanje 1657 gain (nobody) | none | exception | Counterpart nobody, but the 120 km Kwango band covers 85 cells of kingdom-of-kongo. |
| kingdom-of-loango 1883 dissolve (french-africa) | none | exception | french-africa (Cliopatria row) has no dossier yet; its group has not run. |
| luba-empire 1889 dissolve (congo-free-state) | congo-free-state 1889 gain | matched | Both at 1889; the page says the Luba 'later joined' the Free State. |
| yeke-kingdom 1870 gain (nobody) | none | mismatch | The land is luba-empire's (1700-1889) and partly kingdom-of-lunda's; neither records a loss. |
| kingdom-of-kazembe 1867 loss (yeke-kingdom) | yeke-kingdom 1867 gain | matched | Same region (the west bank). |
| kingdom-of-kazembe 1894 dissolve (british-africa) | none | exception | Counterpart changed from congo-free-state by the reviewer; british-africa has no dossier yet (group not run). |
| yeke-kingdom 1891 dissolve (congo-free-state) | congo-free-state 1891 gain | matched | December 1891. |
| kuba-kingdom 1884 dissolve (congo-free-state) | congo-free-state 1885 found | exception | No explicit gain; Kuba land is inside the Free State's 1885 shape; the infobox successor is the IAC (no dossier). |
| congo-free-state 1887 vassal_start (zanzibari-domain-of-tippu-tip) | zanzibari-domain-of-tippu-tip 1887 vassal_start | matched | Tippu Tip side was a 'rename'; changed by the reviewer. |
| congo-free-state 1892 vassal_end (zanzibari-domain-of-tippu-tip) | zanzibari-domain-of-tippu-tip 1892 vassal_end | matched | Tippu Tip side added by the reviewer. |
| zanzibari-domain-of-tippu-tip 1893 loss (congo-free-state) | congo-free-state 1893 gain | matched | Nyangwe, 4 March 1893. |
| zanzibari-domain-of-tippu-tip 1893 loss (congo-free-state) | congo-free-state 1893 gain | matched | Kasongo, 22 April 1893. |
| zanzibari-domain-of-tippu-tip 1894 dissolve (congo-free-state) | congo-free-state 1894 gain | matched | January 1894. |
| congo-free-state 1894 gain (british-colonial-empire) | none | exception | Lado Enclave lease; british-colonial-empire has no dossier yet. |
| congo-free-state 1908 dissolve (belgian-congo) | none | exception | belgian-congo (af-08) not written; author asks af-08 to start it in 1908. |
| portuguese-angola 1641 occupation_start (Dutch West India Company) | portuguese-empire 1641 loss | mismatch | portuguese-empire records a loss of Luanda and Benguela to dutch-republic; PA an occupation of Luanda by the WIC (no dossier). |
| portuguese-angola 1648 occupation_end (Dutch West India Company) | portuguese-empire 1648 gain | mismatch | As above; August 1648 on both sides. |
| portuguese-angola 1885 gain (nobody) | portuguese-empire 1885 vassal_start | mismatch | Cabinda: a gain here, a protectorate (vassal_start) in portuguese-empire. |
| portuguese-angola 1890 gain (Viye (Ovimbundu kingdom)) | none | exception | Viye has no dossier; listed by the author. |
| portuguese-angola 1975 dissolve (people-s-republic-of-angola) | none | exception | Successor dossier not written yet. |

## Gazetteer names that would help

Baixa de Cassange (region, kingdom-of-matamba), Mbata (region, kingdom-of-kongo), Nsundi (region, kingdom-of-kongo), Bembe (region, kingdom-of-kasanje), Lado Enclave (region, congo-free-state), Haut-Katanga (region, yeke-kingdom), Musumba (place, kingdom-of-lunda), Bunkeya (place, yeke-kingdom), Mwibele (place, luba-empire), Mushenge (place, kuba-kingdom), Kabasa (place, kingdom-of-ndongo), Cassange (place, kingdom-of-kasanje), Vivi (place, congo-free-state), Nyangwe (place, zanzibari-domain-of-tippu-tip), Massangano (place, portuguese-angola), Cambambe (place, portuguese-angola), Pungo Andongo (place, kingdom-of-ndongo).

## Counterparts needing dossiers

Mbata (predecessor of Kongo) (mbata, 1300-1390), Mpemba Kasi (predecessor of Kongo) (mpemba-kasi, 1300-1390), Soyo (county-of-soyo, 1641-1887), International Association of the Congo (international-association-of-the-congo, 1879-1885), Chokwe (chokwe, 1850-1910), Viye (Bié) (viye, 1750-1890), Sultanate of Zanzibar (sultanate-of-zanzibar, 1856-1890).

## Problems

- Reviewer applied small verified fixes in four dossiers (kingdom-of-kongo, zanzibari-domain-of-tippu-tip, luba-empire, kingdom-of-kazembe); all validate with 0 errors, 0 warnings, and each edit carries a '[Reviewer af-06, 2026-10-19: ...]' tag.
- Root cause of three of the four fails: the gazetteer region 'Ndongo' (aliases 'Ndongo and Matamba', 'Angola (kingdom core)') includes Malanje Province, so kingdom-of-ndongo and portuguese-angola swallow kingdom-of-matamba and kingdom-of-kasanje; the gazetteer agent may want to split it (Ndongo without Malanje; a 'Baixa de Cassange' entry).
- yeke-kingdom (all Katanga), luba-empire ('Luba (region)' = Katanga intersected with a box) and kingdom-of-lunda (309 km disc) overlap by 75,000-230,000 km2 in 1856-1887; they need a joint redraw.
- portuguese-angola and portuguese-empire (am-06) both draw Angola 1575-1910 (author-flagged); the orchestrator must pick one owner.
- No page failed to load for the reviewer; the 'Kongolese Civil War' and 'Njinga' URLs that failed for the author were not needed.
