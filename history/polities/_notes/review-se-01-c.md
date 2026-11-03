# Review se-01-c (2026-10-18)

Adversarial review of khmer-empire, post-angkor-cambodia and pagan-kingdom. Validator: 0 errors on all three (khmer-empire's 13 and post-angkor-cambodia's 14 "no verdict" warnings are the two halves of the split Khmer row, by design; pagan-kingdom's 3 warnings are the listed new counterparts mon-city-states and arakan). Pages opened: Khmer Empire, Khmer–Cham wars, Jayavarman II, Sukhothai Kingdom, Lavo Kingdom, Post-Angkor period, Pagan Kingdom, First Mongol invasion of Burma. Neighbour ledgers read: champa, haripunjaya, land-chenla, water-chenla, chenla, lavo-kingdom, pyu-city-states (the others in the brief's context table are not written yet).

## khmer-empire: fix (5 fixes applied by the reviewer, 3 left for the author)

Every confidence-3 event spot-checked (802, 928, 944, 1132-1136, 1145-1149, 1177-1181, 1190-1191, 1203, 1220, 1353-1357, 1393-1394, 1431) and 1238 (conf 2) is on its page with the year. Area: infobox "1181–1218: 1,000,000 km2" against khmer-empire_1188 830,253 km2 (0.83) and _1206 953,197 km2 (0.95); acknowledged.

Applied (re-validated, 0 errors):
- /ledger/2: counterpart water-chenla -> srivijaya. water-chenla.json ends c. 790 under Java (successor srivijaya, then khmer-empire 802); Jayavarman II page: "Jayavarman first remained subordinate to Java for some time and thereafter declared independence".
- /ledger/3: capital_move 834 -> 835, to match the Hariharalaya span (835-888).
- /ledger/8 (946 vassal_start of Lavo): source -> Lavo Kingdom page (added to sources[]), confidence 1 -> 2. Infobox "Angkor vassal: 946–1052".
- /ledger/11 (1052 loss of Lavo): source -> Lavo Kingdom page, confidence 1 -> 2. Infobox "Reclaimed by Suphannabhum/ Haripuñjaya: 1052".
- /keyframe_review/10: "for 1220-1237" -> "for 1220-1226" (it overlapped khmer-empire_1227, "for 1227-1237").

For the author (not blocking):
- /keyframe_review/1 and /ledger/4: the 806 shape kept for 803-874 holds the ~45,800 km2 Cham strip (Kauthara, Panduranga and the highlands) that champa.json draws from 757 (/ledger/10; keyframe champa_757 = Chámpa 875 shape; capital Virapura near Phan Rang 757-875). So the strip is claimed twice for 72 years and the 875 loss has no mirror. The Khmer–Cham wars page calls Kauthara "the Cham principality" in 950 and has nothing on 875. Write khmer-empire_806 as minus [Khmer Empire 806, Chámpa 875] for 803-874 and delete /ledger/4.
- /keyframe_review/7 and /ledger/20: the 1188 shape reaches 21.2 N, but the Jayavarman VII page stops the northward reach "to Vientiane" (18.0 N). Clip the northern Lao provinces from 1188 onwards (and shrink the 1363 loss to lan-xang), or say why the edge is kept.
- /wars: pagan-kingdom /wars/1 "Khmer-Pagan clash on the Tenasserim coast" (1044-1077) names khmer-empire; add it with empty zones.

Thin: the 803 union, the 1006, 1181 and 1218 Lavo dates (the Lavo page will lift them), the 1188 gains and northern edge, the 1363 and 1375 losses, no rulers, Zhou Daguan's 1296 Siamese war.

## post-angkor-cambodia: thin (no edits)

Spot checks confirmed on the Post-Angkor period page: capitals (infobox "Chaktomuk (1431–1525); Longvek (1525–1594); Srey Sarchor (1594–1620); Oudong (1620–1863)"), 1594, 1658-59, "by the end of the 17th century", 1795, 1834-1847, 11 August 1863. No infobox area.

For the author (not blocking):
- /keyframe_review/1-6 and /ledger/6: the 1475-1691 corrections remove only Bình Thuận and keep ~130 cells of Cham highlands that no event gains (the 1375 shape is 240,474 km2, the 1475 shape 286,870 km2). The 1700 loss (minus 1691/1700) then gives those highlands to nguyen-lords, though the page talks only about the delta. Correct each to minus [Khmer Empire Y, minus [Chámpa 1429, Khmer Empire 1375]], so that the 1700 loss is the delta only.
- Vassal events missing: Ayutthaya 1594-1618 (Longvek sacked and royals taken hostage, 1594; "stopped sending tribute to Ayutthaya", 1618, quoted in /ledger/3); joint Siamese-Vietnamese suzerainty after 1847 (quoted in /ledger/9). Add vassal_start and vassal_end in this ledger; the suzerains mirror them.
- The 1863 end: standard 4 draws a protectorate as a tint. The dossier dissolves the kingdom although "the Cambodian monarchy was allowed to remain", and it asks french-indochina for a vassal_start naming a dissolved state. The orchestrator decides: continue as a protectorate to 1867 and hand over in 1868, or keep the end and withdraw the request.

Thin: the delta steps (1698 Gia Định, 1708 Hà Tiên, 1757); missing wars (Cambodian–Spanish War 1593-1597, the Siamese–Vietnamese wars of 1811-12, 1831-34 and 1841-45); highland extras and the 1702 and 1803 shapes unverified (page budget); no rulers.

## pagan-kingdom: thin (no edits)

Spot checks confirmed: 849 (infobox "23 December 849"), 1057 Thaton, 1283 (22 September; Kaungsin 9 December), 1284 (Tagaung 5 February; Zhengmian to 4 April 1303), 1287 (Wareru, 30 January; Arakan "stopped paying tribute"), 17 December 1297. No infobox area (population only); the author's comparison of the 1044 principality with the 960 shape (ratio 1.07) stands.

For the author (not blocking): add vassal_start 1297 (March) of the yuan-dynasty. Kyawswa "was recognized by the Yuan emperor Temür Khan as King of Pagan on 20 March 1297"; the dossier quotes this in /ledger/15 but does not draw it.

Thin: the 860 and 960 steps; the 1057 Shan Hills (the Pagan page credits the cis-Salween Shan Hills to Narapatisithu); the 1066 gains; the 1066 Arakan vassalage (the Pagan page: "most scholars credit control of Arakan to Alaungsithu", so 1118 may be better); the 1287 Shan and remainder losses; no rulers.

## Cross-dossier
- Matched: Land Chenla 802/803; Lavo 1006, 1052, 1181, 1218; Haripunjaya 1188; every Champa event 1145-1220; Pyu 849, 860, 960, 1044; Khmer 1431 / post-Angkor 1432 on the same shape.
- Mismatches: champa 757 vs khmer-empire 875 (the strip, above); lavo-kingdom has no vassal_start or vassal_end for khmer-empire 946/1006 (route to se-01-b); the Khmer-Pagan war is missing from khmer-empire.
- Routing: Pagan's 1283-1303 counterpart is yuan-dynasty, whose Cliopatria row starts in 1294 (mongol-empire, ea-05, covers 1206-1293). Whichever dossier holds Yunnan has to carry the Zhengmian gain (1284) and loss (1303). Pagan's successors (myinsaing-kingdom, hanthawaddy-kingdom, shan-states) start in 1294 in Cliopatria and should start in 1297, 1287 and 1287. Cliopatria's 'cambodia' row (1700-1802) is the delta: the orchestrator decides.
