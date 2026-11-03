# Review: batch eu-12-k (Crown of Aragon, Taifa of Córdoba, Taifa of Tejada)

Reviewer: Phase B adversarial reviewer, 2026-10-25. The machine copy of this review is history/notes/phase-b/reviews/eu-12-k.json.

All three dossiers validate (`--resolve`: 0 errors, 0 warnings) before and after the reviewer's edits. Verdicts: crown-of-aragon **fail**, taifa-of-cordoba **fail**, taifa-of-tejada **fix** (fixed by the reviewer). Findings marked *applied* were edited in place by the reviewer and re-validated; every other finding is for the author.

## Summary of what fails

- crown-of-aragon: the shapes draw land that a neighbour dossier already draws, with no event that hands it over. Navarre 1429-1478 is drawn by both this dossier and kingdom-of-navarre; the dossier's own keyframe note admits Navarre was not the Crown's. The Greek duchies 1379-1389 are drawn by both this dossier and catalan-company, and the counterpart slug is the wrong state: duchy-of-athens, which ends in 1311. Cerdanya 1163-1208 is drawn by both this dossier and county-of-berga. Pallars Sobirà 1202-1486 is drawn by both this dossier and county-of-pallars-sobira. Spot checks were otherwise clean: 8 of 9 events confirmed on the page. The 1168 Sangüesa event was overstated, and the reviewer lowered it to confidence 1.
- taifa-of-cordoba: the Cliopatria row is mislabelled. The author flagged this honestly, but the dossier still draws Jaén 1241-1246 a second time over emirate-of-granada. It keeps a one-cell 1236 shape as 'ok' although its own note says the shape is wrong. It also holds Córdoba to 1151, while the Almoravid and Almohad dossiers have the city change hands in 1149. The orchestrator must decide what happens to the row.
- taifa-of-tejada: sound and sourced. The reviewer clipped the war span to the dossier's life. Two non-blocking choices remain for the author: whether the dossier starts in 1145 or 1146, and which predecessor to record.

## crown-of-aragon: fail

Area check: infobox 120000 km2 (1300), Cliopatria 122175 km2, ratio 0.98. Shape alive in 1300 is crown-of-aragon_1294 (1294-1304); the author's corrected shape (no Sicily, no Balearics) is about 94,000 km2, ratio 1.28 infobox/corrected; within a factor of two and stated in the keyframe note.

### Findings

1. `/ledger/2` (applied by reviewer). 1168 gain of 33 Taifa of Murcia cells is credited to the Treaty of Sanguesa, which the page describes only as a partition of land still to be conquered; the cells lie in Lower Aragon (bbox 0.77 W-0.58 E, 40.49-41.40 N), far from Murcia.
   - Evidence: Alfonso II page (opened 2026-10-25): the treaty was 'dividing the territory of the Taifa of Murcia between them'; no handover and no towns. gazetteer resolve of the event's region: 33 cells, 8,346 km2, bbox [-0.77, 40.49, 0.58, 41.4].
   - Fix: Confidence lowered 2 -> 1 and a reviewer sentence appended to the note saying the date and land rest on Cliopatria (page silent). A gap-filler may find the real Lower Aragon dates (Alcaniz, Caspe, Morella) on the Ramon Berenguer IV or Alfonso II pages.

2. `/ledger/33/region` (applied by reviewer). 1324 gain drew the whole island of Sardinia while keyframe crown-of-aragon_1326 holds only Cliopatria's 68 Sardinian cells and the page names only the Pisan lands and Sassari (Arborea was the ally).
   - Evidence: Kingdom of Sardinia page: 'occupied the Pisan territories of Cagliari and Gallura along with the city of Sassari'; Crown of Aragon page: 'In 1324, James II finally started to seize the Pisan territories in the former states of Cagliari and Gallura'.
   - Fix: Region replaced by {intersect: [Sardinia, Crown of Aragon 1326]} with the page's words in text; note appended. Validator: 0 errors, 0 warnings.

3. `/keyframe_review/39, /keyframe_review/40, /keyframe_review/41, /keyframe_review/42, /keyframe_review/43, /ledger/54, /ledger/61` (blocking). Navarre (38-40 cells, 9,610 km2, bbox 2.11 W-0.90 W, 41.91-43.26 N) is kept inside the Crown's corrected shapes for 1429-1478 although the keyframe note itself says it was John II's kingdom, not Alfonso V's, until 1458 and a separate crown in personal union afterwards.
   - Evidence: kingdom-of-navarre dossier (1134-1620) draws Navarre throughout with no event naming crown-of-aragon in 1429 or 1479 (its 1479 event is a rename to the Foix line); county-of-foix has no 1479 gain. The land is drawn twice for 50 years. gazetteer: intersect(Crown of Aragon 1429, Kingdom of Navarre 1428) = 38 cells.
   - Fix: Subtract {"cliopatria": "Kingdom of Navarre", "year": 1428} (or the 1429-minus-1422 Crown cells) from the corrections of crown-of-aragon_1429, _1450, _1453, _1459 and _1463; delete /ledger/54 (1429 gain) and /ledger/61 (1479 loss to county-of-foix) and keep the personal union as a sentence in notes.

4. `/keyframe_review/31, /keyframe_review/32, /ledger/44, /ledger/46, /ledger/47` (blocking). The Greek cells (Attica, Boeotia, Neopatras) are drawn as the Crown's own land 1379-1389 with counterpart 'duchy-of-athens', the Frankish duchy whose dossier ends in 1311; the Catalan duchies already have a dossier, catalan-company (eu-05, 1311-1390), which draws the same land as its own until 1388/1390.
   - Evidence: catalan-company ledger: 1377 rename ('the title of Duke of Athens and Neopatras was assumed by Peter IV of Aragon'; the land stays with the Company), 1379 loss of Thebes to the Navarrese Company, 1388 loss of Athens and 1390 loss of Neopatras to acciaioli-duchy-of-athens. duchy-of-athens dossier: 1205-1311. The author's counterparts_needing_dossiers asks for 'catalan-duchy-of-athens', which is not needed.
   - Fix: Remove the Greek cells from crown-of-aragon_1379 and _1385 (minus {"country": "Greece"}); replace /ledger/44 by a vassal_start with counterpart catalan-company (1379, or 1377 if the Duchy of Athens page dates it so) and /ledger/46-47 by vassal_end events (1388 Athens, 1390 Neopatras, counterpart catalan-company, Acciaioli named in the note); keyframe crown-of-aragon_1390 then equals 1385 and can be merged.

5. `/keyframe_review/0/correction, /keyframe_review/1, /keyframe_review/3 to /keyframe_review/7` (blocking). Cerdanya is drawn twice 1163-1208: the Crown's 1163 keyframe (Kingdom of Aragon + County of Barcelona 1163) already contains the 20 cells of Cliopatria's County of Berga 1169 shape, and keyframes 1169-1206 'restore' the Berga row's cells, while county-of-berga holds them continuously from 1162 to 1242. No Crown event records Cerdanya at all.
   - Evidence: gazetteer: intersect(Aragon 1163 + Barcelona 1163, County of Berga 1169) = 20 cells, 5,058 km2, bbox [1.25, 41.8, 2.79, 42.48]. county-of-barcelona /ledger/14: 1162 loss of Cerdanya to county-of-berga ('Pere (Peter) received Cerdanya'); county-of-berga /ledger/10 1162 gain, /ledger/11 1168 rename (Sancho I). Alfonso II page (opened): 'the counties of Cerdanya (1168) and Roussillon (inherited in 1172)'.
   - Fix: Subtract {"cliopatria": "County of Berga", "year": 1169} from crown-of-aragon_1163 (1163-1167) and add a 1168 event for Cerdanya with counterpart county-of-berga citing the Alfonso II page: a gain if the Crown holds it directly, or a vassal_start if Sancho's tenure 1168-1223 is read as an appanage (then the 1169-1206 corrections must not restore the cells). Route the matching 1168 event to county-of-berga's owner (eu-12).

6. `/ledger (missing, 1199)` (not blocking). The 1199 purchase of Berga by Peter II has no event in the Crown.
   - Evidence: county-of-berga /ledger/12: 1199 loss to crown-of-aragon, 'Berga was sold to king Peter II of Aragon in 1199' (c2).
   - Fix: Add a 1199 gain from county-of-berga, region a 20 km circle at 1.845 E, 42.101 N ('Berga and the Berguedà'), source the Berga page the neighbour cites; adjust the 1199-1208 shape accordingly once Cerdanya is reconciled.

7. `/ledger/7, /keyframe_review/6 onward` (blocking). The 12 Pallars Sobirà cells enter the Crown in 1202 (confidence 1, page silent) while county-of-pallars-sobira runs to 1487 and loses the county to the Crown only then; the land is drawn twice 1202-1486.
   - Evidence: county-of-pallars-sobira ledger: 1199 rename (Guillelma, then Comminges), 1487 loss to crown-of-aragon, c2: Hugh Roger III 'lost his County to the Crown in 1487'. gazetteer: Crown 1202 minus 1192 = 14 cells, 12 of them the Pallars Sobirà 1192 shape (3,035 km2, bbox 0.71-1.30 E, 42.31-42.73 N).
   - Fix: Subtract {"cliopatria": "County of Pallars Sobirà", "year": 1192} from the Crown corrections 1202-1486 (or tint it as a vassal with a vassal_start), replace /ledger/7 by a 1487 gain from county-of-pallars-sobira citing its page.

8. `/ledger/48, /ledger/49, /ledger/50` (not blocking). Empúries is gained 1395, lost 1402 and regained 1415 at confidence 1, while county-of-ampuria dates the escheat to 1410 (c2) and calls the county royal from 1402.
   - Evidence: county-of-ampuria /ledger/9 1402 rename (infobox 'Annexed into the Principality of Catalonia: 1402'); /ledger/10-11 1410 loss and dissolve to crown-of-aragon ('Empúries escheated to the crown between 1410 and 1436').
   - Fix: Replace the three events by one gain in 1410 (or 1402) from county-of-ampuria matching the neighbour, and drop the 4 Empúries cells from the Crown corrections before that year.

9. `/ledger/20/counterpart` (not blocking). The 1244 gain names taifa-of-denia, whose dossier ends in 1227 (loss and dissolve).
   - Evidence: taifa-of-denia ledger: 1227 loss and dissolve; almohad-caliphate /ledger/44: 1228 'Zayyan ibn Mardanish ... took control' of Valencia.
   - Fix: Name the holder in 1244 (taifa-of-valencia for Zayyan's realm, as /ledger/19) or nobody, with a note; or ask the Denia owner to extend its dossier if a page supports it.

10. `/ledger/11` (not blocking). Menorca 1232 is a gain at confidence 3; the page says 'acquired', and the Kingdom of Majorca page says its sovereignty was surrendered while Muslim rule continued; the conquest of Menorca (Alfonso III) is not in the ledger.
   - Evidence: James I page: 'Menorca (1232) and Ibiza (1235) were later acquired during the reconquest' (confirmed). Kingdom of Majorca page footnote: Menorca 'was still under the rule of Muslims until 1231 when its sovereignty was surrendered to James I'.
   - Fix: Consider a vassal_start (counterpart nobody, a tributary Muslim ruler) instead of a gain and look for the conquest of Menorca on the Alfonso III page; the kingdom-of-majorca dossier's 1305 Menorca gain (c1) also needs the same answer.

11. `/ledger/1/counterpart (neighbour side)` (not blocking). The Crown merges county-of-barcelona in 1162, but county-of-barcelona /ledger/15 names kingdom-of-aragon as the merge partner.
   - Evidence: county-of-barcelona ledger 1162: merge kingdom-of-aragon (c3), dissolve.
   - Fix: No change here; route to the county-of-barcelona owner (eu-12) to name crown-of-aragon as counterpart and successor.

### Thin (for a gap-filler)

- `/ledger/5, /ledger/8, /ledger/14, /ledger/16`: Southern frontier steps 1188, 1206, 1236, 1241 (Castello, Tortosa, Valencia districts) are Cliopatria-only, counterpart almohad-caliphate with no mirror in the Almohad dossier. Try https://en.wikipedia.org/wiki/Kingdom_of_Valencia

- `/ledger/21`: 1260 Alicante cells (5 from the Almohad row, 1 from Castile); the Almohads held nothing there in 1260; holder and date unknown. Try https://en.wikipedia.org/wiki/Treaty_of_Almizra

- `/ledger/6`: Pallars Jussa 1192 is confidence 1 here but the neighbour dates it 27 May 1192 at confidence 3 from its page. Try https://en.wikipedia.org/wiki/Pallars_Juss%C3%A0

- `/ledger/13`: Urgell cells 1236, page silent. Try https://en.wikipedia.org/wiki/County_of_Urgell

- `/ledger/25, /ledger/31, /ledger/32`: Murcia/Alicante frontier 1285-1305 (Torrellas 1304, Elche 1305) is confidence 1; crown-of-castile has a 1304 loss that pairs with /ledger/31 but nothing for /ledger/25 or /ledger/32. Try https://en.wikipedia.org/wiki/Treaty_of_Torrellas

- `/ledger/45`: Sicily from 1385 is Cliopatria-only; the Crown page has 'Sicily was dissociated in the hands of Martin I from 1395 to 1409', so the union date is open. Try https://en.wikipedia.org/wiki/Martin_I_of_Sicily

- `/ledger/53, /ledger/58`: Corsica 1422-1449 rests on 'much of Corsica by the 1420s'; the Kingdom of Sardinia page says Corsica 'had never been conquered'. Try https://en.wikipedia.org/wiki/History_of_Corsica

- `/ledger/67`: 1515 dissolve into kingdom-of-spain is Cliopatria-only (Ferdinand II died in January 1516). Try https://en.wikipedia.org/wiki/Ferdinand_II_of_Aragon

- `/keyframe_review (missing 1166-1173)`: Provence under Alfonso II 1166-1173 (page text) is not drawn and county-of-provence has no matching period. Try https://en.wikipedia.org/wiki/County_of_Provence

- `/identity/rulers`: Ruler strip omitted (page budget). Try https://en.wikipedia.org/wiki/List_of_Aragonese_monarchs

### Spot checks

- `/ledger/11`: confirmed (https://en.wikipedia.org/wiki/James_I_of_Aragon)

- `/ledger/15`: confirmed (https://en.wikipedia.org/wiki/James_I_of_Aragon)

- `/ledger/2`: not on page (https://en.wikipedia.org/wiki/Alfonso_II_of_Aragon)

- `/ledger/27`: confirmed (https://en.wikipedia.org/wiki/Kingdom_of_Majorca)

- `/ledger/57`: confirmed (https://en.wikipedia.org/wiki/Alfonso_V_of_Aragon)

- `/ledger/60`: confirmed (https://en.wikipedia.org/wiki/Treaty_of_Barcelona_(1493))

- `/ledger/62`: confirmed (https://en.wikipedia.org/wiki/Treaty_of_Barcelona_(1493))

- `/ledger/52`: confirmed (https://en.wikipedia.org/wiki/Kingdom_of_Sardinia)

- `/ledger/33`: confirmed (https://en.wikipedia.org/wiki/Crown_of_Aragon)

## taifa-of-cordoba: fail

Area check: infobox None km2 (None), Cliopatria 15320 km2, ratio None. The article (1031-1091 republic) gives no area; stated in keyframe taifa-of-cordoba_1147.

### Findings

1. `/wars/0/from` (applied by reviewer). War 'Almohad conquest of al-Andalus' started in 1146, before the dossier's start (1147).
   - Evidence: Brief section 2.2: wars inside the life.
   - Fix: Set from 1147 with a reviewer note (the wider war ran 1146-1173).

2. `/keyframe_review/2, /keyframe_review/3, /ledger/3 to /ledger/7, /identity/capitals/1, /wars/2` (blocking). The 1241-1249 shape (9 cells containing Jaen) is Ibn al-Ahmar's Jaen, already drawn by emirate-of-granada; this dossier draws it a second time 1241-1246 and its 1246 loss has no mirror, since crown-of-castile takes Jaen from emirate-of-granada.
   - Evidence: Emirate of Granada page (opened): 'Jaén, Guadix, and Baeza accepted his authority quickly in 1232'; 'agreed to surrender Jaén and to become Ferdinand's vassal' (March 1246). emirate-of-granada /ledger/1 (1232 gain of Jaen) and /ledger/7 (1246 loss to crown-of-castile); crown-of-castile /ledger/5 (1246 gain of Jaen from emirate-of-granada). The author's own note says the land 'probably belongs under the Emirate of Granada'.
   - Fix: Mark taifa-of-cordoba_1241 'wrong' (correction: the land is emirate-of-granada's, nothing drawn here), delete keyframe taifa-of-cordoba_1246, ledger 3-7, the Jaen capital and the third war, and end the dossier with its first shape (see the next finding). The orchestrator should relabel Cliopatria's 1241 shape to the Emirate of Granada.

3. `/keyframe_review/1/verdict, /ledger/2` (blocking). Keyframe taifa-of-cordoba_1236 is marked 'ok' while its note says the one cell does not contain Cordoba, lies inside the Almohad shape and that 'No page names a state on this land'; the 1236 gain from almohad-caliphate has no mirror.
   - Evidence: Cordoba page: 'Ferdinand III entered the city on 29 June 1236'; almohad-caliphate has no 1236 event naming taifa-of-cordoba; crown-of-castile /ledger/1 gains Cordoba itself in 1236 from taifa-of-cordoba, which this dossier does not hold.
   - Fix: Set the verdict to 'wrong' with an empty-land correction note, delete /ledger/2, and route crown-of-castile /ledger/1 to its owner (eu-12) to name the 1236 holder of Cordoba.

4. `/ledger/1, /identity/end, /keyframe_review/0` (blocking). Cordoba city is drawn twice 1147-1149 and held here to 1151, though the neighbours date its fall to the Almohads, from the Almoravids, to 1149 on a page.
   - Evidence: almohad-caliphate /ledger/11: 1149 gain of Cordoba from almoravid-dynasty, 'They took control of Cordoba in 1149' (Abd al-Mu'min page); almoravid-dynasty /ledger/45: 1149 loss of Cordoba to the Almohads; neither has a 1147 event naming taifa-of-cordoba. Taifa page (opened): Cordoba is listed only for 1031-1091; 'Jaén: 1145–1159 (to Murcia); 1168 (to Almohads)'.
   - Fix: Either (a) a gap-filler finds a page for an independent Cordoba ruler in 1145-1149 (Ibn Hamdin, Spanish 'Taifa de Córdoba'), the dossier ends with a 1149 loss and dissolve to almohad-caliphate, and almoravid-dynasty adds the 1147 loss; or (b) the 1147 shape is marked wrong (Almoravid and Jaen-taifa land) and the dossier is withdrawn. With the findings above this leaves at most 1147-1149.

### Thin (for a gap-filler)

- `/ledger/0, /ledger/1`: Any page naming a Cordoba taifa or ruler in 1145-1151 (Ibn Hamdin did not load in English). Try https://es.wikipedia.org/wiki/Taifa_de_C%C3%B3rdoba

### Spot checks

- `/ledger/0`: confirmed (https://en.wikipedia.org/wiki/Taifa)

- `/ledger/4`: confirmed (https://en.wikipedia.org/wiki/Emirate_of_Granada)

- `/ledger/5`: confirmed (https://en.wikipedia.org/wiki/Emirate_of_Granada)

- `/ledger/6`: confirmed (https://en.wikipedia.org/wiki/Emirate_of_Granada)

## taifa-of-tejada: fix

Area check: infobox None km2 (None), Cliopatria 2252 km2, ratio None. No area on the page; the circle keeps Cliopatria's area.

### Findings

1. `/wars/0/to` (applied by reviewer). War 'Almohad conquest of al-Andalus' ran to 1173, past the dossier's end (1150).
   - Evidence: Brief section 2.2: wars inside the life.
   - Fix: Set to 1150 with a reviewer note (the wider war ran 1146-1173).

2. `/identity/rulers/0/from` (not blocking). The first ruler starts in 1145, a year before the dossier's start (1146).
   - Evidence: Taifa of Tejada page (opened): ruler list 'Abu al-Walid Mohammed ibn al-Mundir: 1145-1146', infobox 'Established: 1146'; the Taifa page gives 'Tejada: 1145–1150 (to Almohads)'.
   - Fix: Choose one: start the dossier in 1145 (two pages support it) or clip the ruler to 1146 and keep 1145 in the note.

3. `/ledger/0/counterpart` (not blocking). The found event names almoravid-dynasty, but the infobox says 'Preceded by: Taifa of Silves' and the first ruler (1145-1146) is Ibn al-Mundhir; neither almoravid-dynasty nor taifa-of-silves has a matching 1146 event.
   - Evidence: Taifa of Tejada page (opened): infobox 'Preceded by: Taifa of Silves'; almoravid-dynasty 1145 gives Huelva province to taifa-of-niebla; taifa-of-silves has no Tejada event.
   - Fix: Keep almoravid-dynasty or switch to taifa-of-silves, say why in the note, and route the mirror to the chosen owner (af-02 or eu-12).

### Spot checks

- `/ledger/0`: confirmed (https://en.wikipedia.org/wiki/Taifa_of_Tejada)

- `/ledger/1`: confirmed (https://en.wikipedia.org/wiki/Taifa_of_Tejada)

- `/ledger/2`: confirmed (https://en.wikipedia.org/wiki/Taifa_of_Tejada)

- `/keyframe_review/1`: confirmed (https://en.wikipedia.org/wiki/Taifa_of_Tejada)

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |

| taifa-of-tejada 1146 found (almoravid-dynasty) | almoravid-dynasty - - | missing | No Almoravid loss to Tejada; Almoravid gives Huelva province to taifa-of-niebla in 1145. Route to af-02 (or switch counterpart to taifa-of-silves). |

| taifa-of-tejada 1150 loss (almohad-caliphate) | almohad-caliphate 1152 gain | mismatch | Almohad dates it 1152 at c1 (Cliopatria bridging); the Tejada page gives 1150. Route to af-02 to move to 1150. |

| taifa-of-cordoba 1147 found (almoravid-dynasty) | almoravid-dynasty - - | missing | Almoravid holds Cordoba to 1149 (loss to Almohads); no event naming taifa-of-cordoba. |

| taifa-of-cordoba 1152 loss (almohad-caliphate) | almohad-caliphate 1152 gain | matched | Both c1; but almohad-caliphate already gains Cordoba city from almoravid-dynasty in 1149. |

| taifa-of-cordoba 1236 gain (almohad-caliphate) | almohad-caliphate - - | missing | No Almohad event; Cliopatria artefact (one cell). |

| taifa-of-cordoba 1241 gain (taifa-of-almeria) | taifa-of-almeria - - | exception | No dossier yet (eu-12, listed by the author). |

| taifa-of-cordoba 1246 loss (crown-of-castile) | crown-of-castile 1246 gain | mismatch | Castile gains Jaen from emirate-of-granada, not from taifa-of-cordoba; Jaen is drawn by both Cordoba and Granada 1241-1246. |

| taifa-of-cordoba 1249 dissolve (crown-of-castile) | crown-of-castile - - | missing | No Castile event in 1249. |

| crown-of-castile 1236 gain (taifa-of-cordoba) | taifa-of-cordoba - - | mismatch | Castile takes Cordoba city from taifa-of-cordoba, which holds no land at Cordoba in 1236. Route to Castile owner (eu-12). |

| crown-of-aragon 1162 merge (county-of-barcelona) | county-of-barcelona 1162 merge | mismatch | Barcelona names kingdom-of-aragon as merge partner, not crown-of-aragon. |

| crown-of-aragon 1168 gain (taifa-of-murcia) | taifa-of-murcia 1169 loss | matched | Both Cliopatria-based (Crown now c1, Murcia c1). |

| crown-of-aragon 1171 gain (taifa-of-murcia) | taifa-of-murcia - - | missing | Teruel: Murcia has no 1171 (or 1177) loss to the Crown. |

| crown-of-aragon 1172 gain (county-of-rosellon) | county-of-rosellon - - | exception | No dossier yet (eu-12, listed). |

| crown-of-aragon 1188 gain (almohad-caliphate) | almohad-caliphate - - | missing | c1; route to af-02 or rename counterpart. |

| crown-of-aragon 1192 gain (county-of-pallars-jussa) | county-of-pallars-jussa 1192 loss | matched | Neighbour has 27 May 1192 at c3; Crown is c1. |

| crown-of-aragon 1202 gain (county-of-pallars-sobira) | county-of-pallars-sobira 1487 loss | mismatch | Neighbour keeps the county to 1487; land drawn twice 1202-1486. |

| crown-of-aragon 1206 gain (almohad-caliphate) | almohad-caliphate - - | missing | c1. |

| crown-of-aragon 1209 vassal_start (county-of-berga) | county-of-berga 1209 gain | mismatch | Berga records a gain of Roussillon, not a vassal_start; Berga also holds Cerdanya 1162-1242 which the Crown draws as its own 1163-1208. |

| county-of-berga 1199 loss (crown-of-aragon) | crown-of-aragon - - | missing | Berga sold to Peter II in 1199; no Crown event. |

| county-of-barcelona 1162 loss (county-of-berga) | county-of-berga 1162 gain | matched | But the Crown 1163 keyframe still contains these 20 Cerdanya cells (double drawing 1163-1208). |

| crown-of-aragon 1229 gain (almohad-caliphate) | almohad-caliphate 1230 loss | matched | Almohad 1230 loss is the whole Balearic Islands. |

| crown-of-aragon 1232 gain (almohad-caliphate) | almohad-caliphate 1230 loss | mismatch | Almohad gives all Balearics in 1230; Crown has Menorca 1232. Route to af-02. |

| crown-of-aragon 1235 gain (almohad-caliphate) | almohad-caliphate 1230 loss | mismatch | Ibiza: Almohad 1230 vs Crown 1235. |

| crown-of-aragon 1236 gain (county-of-urgell) | county-of-urgell - - | exception | No dossier yet (eu-12, listed). |

| crown-of-aragon 1236 gain (almohad-caliphate) | almohad-caliphate - - | missing | c1. |

| crown-of-aragon 1238 gain (taifa-of-valencia) | taifa-of-valencia - - | exception | No dossier yet (eu-12, listed). |

| crown-of-aragon 1241 gain (almohad-caliphate) | almohad-caliphate - - | missing | c1. |

| crown-of-aragon 1242 gain (county-of-berga) | county-of-berga 1242 loss | matched |  |

| crown-of-aragon 1242 vassal_end (county-of-berga) | county-of-berga 1242 loss | mismatch | Berga has no vassal pair. |

| crown-of-aragon 1244 gain (taifa-of-valencia) | taifa-of-valencia - - | exception | No dossier yet (eu-12, listed). |

| crown-of-aragon 1244 gain (taifa-of-denia) | taifa-of-denia 1227 dissolve | mismatch | Denia dossier ends in 1227. |

| crown-of-aragon 1260 gain (almohad-caliphate) | almohad-caliphate - - | missing | c1; the Almohads held nothing in Alicante in 1260. |

| crown-of-aragon 1276 split (kingdom-of-majorca) | kingdom-of-majorca 1276 found | matched |  |

| crown-of-aragon 1279 vassal_start (kingdom-of-majorca) | kingdom-of-majorca - - | missing | Majorca has no vassal_start. Route to eu-12 (Majorca owner). |

| crown-of-aragon 1282 gain (house-of-anjou-sicily) | house-of-anjou-sicily - - | exception | eu-18 has not run. |

| crown-of-aragon 1285 gain (crown-of-castile) | crown-of-castile - - | missing | c1. |

| crown-of-aragon 1285 split (kingdom-of-sicily) | kingdom-of-sicily - - | exception | eu-13 has not run. |

| crown-of-aragon 1286 occupation_start (kingdom-of-majorca) | kingdom-of-majorca 1286 loss | mismatch | Same year, different type: Majorca records an outright loss of Mallorca only. |

| crown-of-aragon 1291 merge (kingdom-of-sicily) | kingdom-of-sicily - - | exception | eu-13 has not run. |

| crown-of-aragon 1295 occupation_end (kingdom-of-majorca) | kingdom-of-majorca 1295 gain | mismatch | Same year, type differs (gain vs occupation_end). |

| kingdom-of-majorca 1305 gain (crown-of-aragon) | crown-of-aragon - - | missing | Menorca c1 in Majorca; the Crown drew no Menorca 1295-1305. |

| crown-of-aragon 1295 loss (papal-states) | papal-states - - | exception | eu-13 has not run. |

| crown-of-aragon 1305 gain (crown-of-castile) | crown-of-castile 1304 loss | matched | Torrellas/Elche. |

| crown-of-aragon 1305 loss (crown-of-castile) | crown-of-castile - - | missing | c1. |

| crown-of-aragon 1324 gain (republic-of-pisa) | republic-of-pisa - - | exception | eu-13 has not run. |

| crown-of-aragon 1343 vassal_end (kingdom-of-majorca) | kingdom-of-majorca - - | missing | Majorca has no vassal_end. |

| crown-of-aragon 1344 gain (kingdom-of-majorca) | kingdom-of-majorca 1343 loss | matched | Majorca 1343 Balearics, 1344 Roussillon/Cerdanya. |

| crown-of-aragon 1353 contest_start (giudicato-of-arborea) | giudicato-of-arborea - - | exception | eu-13 has not run. |

| crown-of-aragon 1357 contest_start (crown-of-castile) | crown-of-castile 1357 contest_start | matched |  |

| crown-of-aragon 1363 contest_start (crown-of-castile) | crown-of-castile 1363 contest_start | matched |  |

| crown-of-aragon 1375 contest_end (crown-of-castile) | crown-of-castile 1369 contest_end | mismatch | Six years apart. |

| crown-of-aragon 1368 loss (giudicato-of-arborea) | giudicato-of-arborea - - | exception | eu-13 has not run. |

| crown-of-aragon 1379 gain (duchy-of-athens) | catalan-company 1377 rename | mismatch | Wrong counterpart slug (duchy-of-athens ends 1311); catalan-company draws the land as its own to 1388/1390. |

| crown-of-aragon 1385 gain (kingdom-of-sicily) | kingdom-of-sicily - - | exception | eu-13 has not run. |

| crown-of-aragon 1388 loss (duchy-of-athens) | catalan-company 1388 loss | mismatch | Athens falls to acciaioli-duchy-of-athens from catalan-company, not from the Crown. |

| crown-of-aragon 1390 loss (duchy-of-athens) | catalan-company 1390 loss | mismatch | Neopatras, as above. |

| crown-of-aragon 1395 gain (county-of-ampuria) | county-of-ampuria 1410 loss | mismatch | Neighbour dates the escheat 1410. |

| crown-of-aragon 1402 loss (county-of-ampuria) | county-of-ampuria 1402 rename | mismatch |  |

| crown-of-aragon 1415 gain (county-of-ampuria) | county-of-ampuria 1410 loss | mismatch |  |

| crown-of-aragon 1420 gain (giudicato-of-arborea) | giudicato-of-arborea - - | exception | eu-13 has not run. |

| crown-of-aragon 1422 gain (republic-of-genoa) | republic-of-genoa - - | exception | eu-13 has not run. |

| crown-of-aragon 1429 gain (kingdom-of-navarre) | kingdom-of-navarre - - | mismatch | Navarre dossier keeps the kingdom 1134-1620; land drawn twice 1429-1478. |

| crown-of-aragon 1442 gain (kingdom-of-naples) | kingdom-of-naples - - | exception | eu-13 has not run. |

| crown-of-aragon 1450 loss (republic-of-genoa) | republic-of-genoa - - | exception | eu-13 has not run. |

| crown-of-aragon 1458 split (kingdom-of-naples) | kingdom-of-naples - - | exception | eu-13 has not run. |

| crown-of-aragon 1462 loss (kingdom-of-france) | kingdom-of-france - - | missing | France has no 1462 gain of Roussillon/Cerdagne. Route to eu-10. |

| crown-of-aragon 1479 loss (county-of-foix) | county-of-foix - - | missing | Moot once Navarre is removed from the Crown. |

| crown-of-aragon 1493 gain (kingdom-of-france) | kingdom-of-france 1497 loss | mismatch | France c1 (Cliopatria) 1497; the Treaty of Barcelona page gives 19 January 1493. Route to eu-10. |

| crown-of-aragon 1500 gain (kingdom-of-naples) | kingdom-of-naples - - | exception | eu-13 has not run. |

| crown-of-aragon 1503 gain (kingdom-of-france) | kingdom-of-france 1503 loss | matched |  |

| crown-of-aragon 1515 dissolve (kingdom-of-spain) | kingdom-of-spain 1516 merge | matched |  |

## Routing

- eu-12 (other parts): county-of-berga (1168 Cerdanya, 1209 vassal pair), county-of-barcelona (1162 merge counterpart), kingdom-of-majorca (1279 vassal_start, 1343 vassal_end, 1286 type, 1305 Menorca), taifa-of-murcia (1171 Teruel), crown-of-castile (1236 holder of Córdoba, 1305 gain, War of the Two Peters end 1369 vs 1375), taifa-of-denia (ends 1227), kingdom-of-navarre (no change needed once the Crown drops Navarre), kingdom-of-aragon (must end 1162).

- af-02: almohad-caliphate (Tejada 1150 not 1152; Balearics split 1229/1232/1235; no mirrors for the Crown's 1188-1260 c1 gains), almoravid-dynasty (Tejada and Córdoba founding events).

- eu-10: kingdom-of-france (1462 gain of Roussillon and Cerdagne; return 1493, not 1497).

- eu-05: catalan-company and the Crown must agree on 1377/1379-1390 (vassal pair).

## Problems

- No page failed to load for the reviewer; 11 WebFetch calls (James I, Alfonso II, Kingdom of Majorca, Alfonso V, Treaty of Barcelona (1493), Kingdom of Sardinia, Crown of Aragon x2, Emirate of Granada, Taifa of Tejada, Taifa).

- The author's counterparts_needing_dossiers is stale: catalan-company (eu-05) already holds the Catalan duchies, crown-of-castile, taifa-of-murcia and kingdom-of-majorca exist; the rest (kingdom-of-sicily, house-of-anjou-sicily, republic-of-pisa, giudicato-of-arborea, republic-of-genoa, kingdom-of-naples, papal-states: eu-13/eu-18; taifa-of-valencia, taifa-of-almeria, county-of-urgell, county-of-rosellon, kingdom-of-aragon: eu-12) are owned by groups that have not written them, so none is listed as needing a new dossier.

- Orchestrator decision needed for Cliopatria row 'Taifa of Córdoba': the 1236 cell and the 1241-1249 Jaén shape are not a Córdoba taifa (the 1241 shape is Ibn al-Ahmar's Jaén, drawn by emirate-of-granada); the 1147-1151 shape conflicts with the Almoravid/Almohad dossiers, which put Córdoba under the Almoravids until the Almohad capture of 1149.

- Moving the Cliopatria Taifa of Tejada shape to Huelva leaves its 8 eastern Algarve cells (8.17-7.45 W, 37.00-37.45 N) with no holder in 1147-1151 unless taifa-of-silves or almoravid-dynasty covers them; check when the Algarve dossiers are reviewed.

- kingdom-of-aragon has no dossier yet; it must end in 1162 (the Crown draws its land from 1163), as the author says.
