# Review of batch eu-06-e (Migration kingdoms, part e)

Reviewer, 2026-10-19 (adversarial pass, Phase B). Validator: 0 errors on all six; 2 warnings (lombards: place Bardowick unknown to the gazetteer). Pages read through WebFetch: Gepids, Cunimund, Gothic War (535-554), Ostrogothic Kingdom, Theodoric the Great, Alboin, Kingdom of the Lombards, Lombards, Alamannia, Alemanni, Battle of Tolbiac, Blood court at Cannstatt, Thuringii. No infobox on these pages gives an area, so no area ratio could be computed; every dossier says so.

Verdicts: kingdom-of-alamannia **pass**, thuringian-states **thin**, kingdom-of-thuringia **pass**, lombards **fail**, ostrogothic-kingdom **fail**, kingdom-of-the-gepids **fail**.

Every confidence-3 event opened was on its page with its year; nothing fabricated was found. The three fails are keyframe faults: the shapes contradict the dossiers' own ledgers and capitals (Sirmium 555-567 in lombards and kingdom-of-the-gepids; Pavia, Verona and Brescia 546-562 in ostrogothic-kingdom). They are shape corrections, which the reviewer may not apply, so they go back to the author with the exact correction to write.

## kingdom-of-alamannia: pass

What was tried: All four events opened and confirmed; keyframe walk 462-499 (Lorraine/Champagne/Trier cut), 496 loss, 496-723 and 732-745 new keyframes consistent; Alamannia infobox status 'Ostrogothic Kingdom (496-539)' differs from the 536 vassal_end by three years (the Alemanni page gives 536; acceptable).

Gaps (thin):
- `/ledger/0`: found 462 is confidence 1: the year is Cliopatria's row start; the Alemanni page only says the kingdom 'between Strasbourg and Augsburg lasted until 496' (try https://en.wikipedia.org/wiki/Gibuld)
- `/wars/2`: Frankish campaigns 709-746 have no zones; the outcome should say in words that no ground changed hands before 746 (the Lantfrid page limits Willehari to the Ortenau) (try https://en.wikipedia.org/wiki/Lantfrid)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Alemanni: confirmed: 'The kingdom of Alamannia between Strasbourg and Augsburg lasted until 496' (no founding year, confidence 1 honest)
- `/ledger/1` https://en.wikipedia.org/wiki/Battle_of_Tolbiac: confirmed: traditionally 496 (revised 506); 'the northern half of the Alammanian lands went to the Franks'; 'the southern half sought protection under Theoderic'
- `/ledger/2` https://en.wikipedia.org/wiki/Alemanni: confirmed: 'again subjugated by the Franks under Theudebert I in 536'; Alamannia page 'Thereafter, Alamannia was a nominal dukedom within Francia'
- `/ledger/3` https://en.wikipedia.org/wiki/Blood_court_at_Cannstatt: confirmed: 746, Carloman's invitation, 'ended the independence of the duchy of Alamannia, after which it was ruled by Frankish dukes'

Area: Alamannia infobox has no area (read 2026-10-19); keyframe notes say so. Quoted shape areas match shapes.csv (the 60,973 km2 for the 724 shape is the gazetteer cell count, 57,419 polygon).

## thuringian-states: thin

What was tried: One shape, one page; no border move to explain. Thin by design within the 1-2 page budget.

Gaps (thin):
- `/ledger/0`: found 469 is confidence 1 (Cliopatria row start); the Thuringii page gives only 'late fifth century' and Jordanes 'about 470' (try https://en.wikipedia.org/wiki/Bisinus)
- `/ledger/1`: dissolve 475 is a Cliopatria seam, not an event: the Thuringii page shows one kingdom 469-532; the orchestrator should decide whether to merge kingdom-of-thuringia into this dossier (the earlier slug), as the research brief's one-dossier-per-state rule suggests (try https://en.wikipedia.org/wiki/Thuringii)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Thuringii: confirmed as quoted: 'The Thuringi established an empire in the late fifth century'; Jordanes 'immediately north of the Alemanni and Suevi in about 470'
- `/ledger/1` https://en.wikipedia.org/wiki/Thuringii: confirmed: the page shows no break at 475/476

Area: No area on the Thuringii page; the Cliopatria Wikipedia field 'Thuringian states' is the 1871-1920 article. Acknowledged in the keyframe note.

## kingdom-of-thuringia: pass

What was tried: Contest 531-532 paired with the war zone; the 523 Cliopatria break carries an identical shape and is honestly called unexplained; end 532 against Cliopatria 533 is the page's year.

Gaps (thin):
- `/ledger/0`: found 476 is a confidence-1 Cliopatria seam (same kingdom as thuringian-states) (try https://en.wikipedia.org/wiki/Thuringii)
- `/ledger/1`: the 531-532 battles (Unstrut, Burgscheidungen) and any Saxon share of the conquest are not on the Thuringii page; the page says only that 'Towards the end of this century, parts of Thuringia came under Saxon rule' (try https://en.wikipedia.org/wiki/Herminafried)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Thuringii: confirmed: 'conquered by the Franks in 531-532'; 'defeated Herminafrid in two battles and took control of the Unstrut region'
- `/ledger/3` https://en.wikipedia.org/wiki/Thuringii: confirmed (531-532)
- `/ledger/4` https://en.wikipedia.org/wiki/Thuringii: confirmed; the page names no capital (only the later Frankish dukes' seat at Wurzburg)

Area: No area on the Thuringii page; acknowledged.

## lombards: fail

What was tried: Keyframe walk 480-586: every area change has an event except the 546->555 Syrmia cells (finding above). Capitals inside the 568 and 569-586 shapes.

Findings:
- `/identity/rulers/3/to` (applied by reviewer). Authari's reign ran to 590, past the dossier's end (586). Evidence: Rulers must lie inside the life (reviewer brief 2.2); Kingdom of the Lombards page: Autari crowned 584. Fix: to 586, note says the reign continues to 590 in the successor dossier.
- `/wars/4/to` (applied by reviewer). Frankish invasions of Lombard Italy ran to 590, past the dossier's end (586). Evidence: Wars must lie inside the life (reviewer brief 2.2). Fix: to 586, note says the later attacks belong to the successor dossier.
- `/keyframe_review/6, /keyframe_review/7, /keyframe_review/8/correction` (BLOCKING, for the author). lombards_555 and lombards_561 (verdict ok) and the 567 correction keep the 11 cells Cliopatria moves from the Gepids to the Lombards in 555: Syrmia with Sirmium itself (19.2-20.1 E, 44.8-45.2 N, 2,782 km2), with no ledger event; the K6 note calls them 'unexplained ... Kept'. Evidence: Cunimund page: 'The Gepids had held the important city of Sirmium ... since 536, after taking it from the Byzantine emperor Justinian I', and the Gepid king 'handed Sirmium over to the Byzantines' (died 567). This batch's kingdom-of-the-gepids has Sirmium as capital 536-567 and /ledger/10 hands it to eastern-roman-empire in 567 (ERE /ledger/55 gains it). Gazetteer: Sirmium within 15 km is 2 cells, Gepid in the 546 shape, Lombard in the 555, 561 and 567 shapes. As drawn, Sirmium is Lombard 555-568 and double-claimed with the ERE in 567-568. Fix: K6 and K7: verdict adjust, correction {'minus':[{'cliopatria':'Lombards','year':555 (561)}, S]} with text 'Pannonia without Syrmia and Sirmium, Gepid until 567 (Cunimund page)'; K8 correction {'minus':[{'cliopatria':'Lombards','year':567}, S]}, where S = {"intersect":[{"cliopatria":"Lombards","year":555},{"cliopatria":"Kingdom of the Gepids","year":546}]} (the 11 cells); the K6 note no longer says 'Kept'. Pair with the kingdom-of-the-gepids fix that gives S back to the Gepids 555-567.

Gaps (thin):
- `/ledger/0, /keyframe_review/0`: 480-487 location at Bardowick (confidence 1): the Lombards page puts Bardengau/Bardowick at 'the first known homeland' (1st century) and says 'They had previously settled in the Middle Danube in the 5th century' and 'reappear ... near the Danube river in the late 5th century'; a 480 reading needs a page (try https://en.wikipedia.org/wiki/Lombards)
- `/ledger/1`: 488 Rugiland gain is confidence 1 and its counterpart kingdom-of-odoacer keeps Rugiland in its 488-493 keyframe with no loss to the Lombards (see cross_checks) (try https://en.wikipedia.org/wiki/Odoacer)
- `/ledger/2, /ledger/3`: the move from Rugiland to the Feld and Pannonia (both confidence 1, Cliopatria's 546): the Alboin page has 'the Lombards under Wacho migrated towards the east into Pannonia, taking advantage of the difficulties facing the Ostrogothic Kingdom' (after 526), earlier than 546 (try https://en.wikipedia.org/wiki/Wacho)
- `/wars/0`: the Heruli war's land outcome: the Lombards page has 'Rodulf died in the ensuing battle, and this Heruli kingdom came to an end' (493-511) but no land; the Feld settlement is undated (try https://en.wikipedia.org/wiki/Heruli)
- `/ledger/11, /ledger/12`: 577 Tuscia split and 586 dissolve are Cliopatria seams at confidence 1 (try https://en.wikipedia.org/wiki/Duchy_of_Tuscia)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Lombards: confirmed: 'When Odoacer defeated the Rugian kingdom which lay north of the Danube in Lower Austria in 488'
- `/ledger/6` https://en.wikipedia.org/wiki/Alboin: confirmed: 'In 567 the allies made their final move against Cunimund'
- `/ledger/7` https://en.wikipedia.org/wiki/Kingdom_of_the_Lombards: confirmed: 'Gisulf, who became the first Duke of Friuli in 568'
- `/ledger/8` https://en.wikipedia.org/wiki/Alboin: confirmed: migration 'started on Easter Monday, 2 April 568'; 'the Avars were to take possession of Pannonia'
- `/ledger/9` https://en.wikipedia.org/wiki/Alboin: confirmed: reached 'Mediolanum (Milan) on 3 September 569'
- `/ledger/10` https://en.wikipedia.org/wiki/Kingdom_of_the_Lombards: confirmed: infobox 'Cividale del Friuli (568-572) Pavia (572-774)'; the quoted siege sentence is on the Lombards page

Area: No area on the Lombards or Kingdom of the Lombards pages; acknowledged in notes.

## ostrogothic-kingdom: fail

What was tried: All confidence-3 events opened: every one is on the page with its year; the failure is the 546-562 keyframes, not the ledger.

Findings:
- `/identity/rulers/0/from` (applied by reviewer). Theodoric's reign started at 493, before the dossier's start (500). Evidence: Rulers must lie inside the life (reviewer brief 2.2); the ostrogoths dossier holds 493-499. Theodoric page infobox: 'Reign: 15 March 493 - 30 August 526'. Fix: from 500, note keeps 493.
- `/keyframe_review/8/correction` (BLOCKING, for the author). The 546-551 keyframe is Cliopatria's 546 shape unchanged, which drops the Gothic north that keyframes 5-7 hold (Pavia, Verona, Brescia, Venetia, Liguria: 76 cells, about 19,200 km2) with no ledger event, and leaves the capital outside the state. Evidence: Gazetteer: the Pavia admin1 has 0 cells in the 546 shape, Verona 1 cell; identity.capitals has Pavia 540-553 (infobox 'Pavia (540-553)'); Gothic War page: 'Pavia (which became the new capital of the Ostrogothic Kingdom) and Verona remained unconquered', 'It was not until 562 that their last strongholds, the cities of Verona and Brixia, were subjugated'; the page has no Frankish occupation of Venetia. /ledger/24 then removes Verona and Brescia in 562 from cells the keyframes do not hold. Fix: Correction {'union':[{'cliopatria':'Ostrogothic Kingdom','year':546},{'admin1':'Pavia','country':'Italy'},{'admin1':'Verona','country':'Italy'},{'admin1':'Brescia','country':'Italy'},{'admin1':'Veneto','country':'Italy'},{'admin1':'Liguria','country':'Italy'}]}, text 'Totila's Italy with the Gothic north (Pavia, Verona, Brixia, Venetia, Liguria)'; if any of Venetia or Liguria is not Gothic in 546-551, a dated loss event with its page instead.
- `/keyframe_review/9/correction, /keyframe_review/10, /keyframe_review/11/correction` (BLOCKING, for the author). The 552-554, 555-560 (ok) and 561-562 keyframes use the Cliopatria 555 rump, which holds none of Pavia and 4 of Verona's 12 cells, while the K9 text says 'Verona, Brescia, Pavia and the Alpine edge' and /ledger/24 loses Verona and Brescia only in 562. Evidence: Gazetteer: Ostrogothic Kingdom 555 bbox starts at 45.50 N (Pavia is 45.19 N); intersect with admin1 Verona = 4 of 12 cells. Capital Pavia to 553 (infobox). Fix: K9: {'union':[{'cliopatria':'Ostrogothic Kingdom','year':555},{'admin1':'Pavia','country':'Italy'},{'admin1':'Verona','country':'Italy'},{'admin1':'Brescia','country':'Italy'}]}; K10 verdict adjust and K11 correction: the 555 rump union Verona and Brescia (and Pavia until a dated loss; the Gothic War page does not date Pavia's fall, so a confidence-1 loss at 553 or keep it to 562 and say so).

Gaps (thin):
- `/ledger/0`: found 500 is a Cliopatria seam (realm from 493, held by the ostrogoths dossier) (try https://en.wikipedia.org/wiki/Ostrogoths)
- `/ledger/1`: the Alemannic protectorate is dated 500 (confidence 1); Battle of Tolbiac/Alemanni pages give 496 and the Alamannia infobox 'Ostrogothic Kingdom (496-539)' (try https://en.wikipedia.org/wiki/Alamannia)
- `/ledger/8`: how Sirmium passed to Justinian before the Gepids took it in 536 (confidence 1) (try https://en.wikipedia.org/wiki/Sirmium)
- `/ledger/9, /ledger/12`: Raetia lost to the Franks 536 and Provence ceded 540 are confidence-1 bridges (try https://en.wikipedia.org/wiki/Theudebert_I)
- `/ledger/18`: Pannonia lost to the Lombards 546 (confidence 1; the Alboin page puts the Lombard move under Wacho, after 526) (try https://en.wikipedia.org/wiki/Wacho)
- `/identity/rulers`: Ildibad (540-541) and Eraric (541) are missing from the ruler strip; the Gothic War page names Ildibad re-establishing 'Gothic control over Venetia and Liguria' (try https://en.wikipedia.org/wiki/Ildibad)

Spot checks:
- `/ledger/2` https://en.wikipedia.org/wiki/Ostrogothic_Kingdom: confirmed: 'In 504-505, Theodoric's forces launched a campaign to recover Pannonia and the strategically important town of Sirmium'
- `/ledger/4` https://en.wikipedia.org/wiki/Theodoric_the_Great: confirmed: 'In 511, the Visigothic Kingdom was brought under Theodoric's direct control'
- `/ledger/6` https://en.wikipedia.org/wiki/Gothic_War_(535%E2%80%93554): confirmed: Sicily 'quickly captured, with ... Palermo, overcome by late December' (535); the note's quote is paraphrased
- `/ledger/10` https://en.wikipedia.org/wiki/Gothic_War_(535%E2%80%93554): confirmed: 'by late June, the whole of Dalmatia was in Byzantine hands'
- `/ledger/13` https://en.wikipedia.org/wiki/Gothic_War_(535%E2%80%93554): confirmed: 'In May 540, Belisarius and his army entered Ravenna'; Ticinum and Verona 'remained in Gothic hands'
- `/ledger/15` https://en.wikipedia.org/wiki/Gothic_War_(535%E2%80%93554): confirmed: Ildibad 're-established Gothic control over Venetia and Liguria'
- `/ledger/17` https://en.wikipedia.org/wiki/Gothic_War_(535%E2%80%93554): confirmed: Naples surrendered 'on terms in 543'; the note's quote is paraphrased
- `/ledger/19` https://en.wikipedia.org/wiki/Gothic_War_(535%E2%80%93554): confirmed: 'Totila finally entered Rome on 17 December 546'
- `/ledger/20` https://en.wikipedia.org/wiki/Gothic_War_(535%E2%80%93554): confirmed: 'reoccupied Rome four months later in the spring of 547'
- `/ledger/24` https://en.wikipedia.org/wiki/Gothic_War_(535%E2%80%93554): confirmed: 'It was not until 562 that their last strongholds, the cities of Verona and Brixia, were subjugated'
- `/ledger/14` https://en.wikipedia.org/wiki/Ostrogothic_Kingdom: confirmed: infobox 'Ravenna (493-540); Pavia (540-553)'

Area: No area on the Ostrogothic Kingdom, Theodoric or Gothic War pages; acknowledged in notes.

## kingdom-of-the-gepids: fail

What was tried: Extension to 454-567 is page-backed (infobox 454 and 567); the 510 shape's Danube bank held back to 539 matches 'after 537' and the 539 recognition; Sirmium 473/504/536/567 chain matches ostrogothic-kingdom and the ERE 567 gain.

Findings:
- `/keyframe_review/7, /keyframe_review/8/correction` (BLOCKING, for the author). kingdom-of-the-gepids_555 (verdict ok) and the 561-567 keyframe drop Syrmia with Sirmium (11 cells, 2,782 km2) besides the Danube bank, so the capital Sirmium (536-567) lies outside the state for 555-567 and /ledger/10 hands the Byzantines in 567 a city the keyframes no longer hold; the K7 note explains only the 74-cell Danube bank. Evidence: Cunimund page: 'The Gepids had held the important city of Sirmium ... since 536', the Gepid king 'handed Sirmium over to the Byzantines' (died 567). Gazetteer: Sirmium within 15 km = 2 cells, in the Gepid 546 shape, absent from the 555 and 561 shapes; minus(Gepids 546, Gepids 555 + Danube bank) = 11 cells at 19.2-20.1 E, 44.8-45.2 N, the same cells that enter lombards_555. Fix: K7: verdict adjust, correction {'union':[{'cliopatria':'Kingdom of the Gepids','year':555}, S]} with text 'the Gepid lands with Syrmia and Sirmium, the capital until 567 (Cunimund page)'; K8 correction {'union':[{'cliopatria':'Kingdom of the Gepids','year':561}, S]}, where S = {"intersect":[{"cliopatria":"Lombards","year":555},{"cliopatria":"Kingdom of the Gepids","year":546}]}. Pair with the lombards fix.

Gaps (thin):
- `/ledger/5`: 555 loss of the Danube bank is Cliopatria's (confidence 1); no page dates the Byzantine recovery of Singidunum (try https://en.wikipedia.org/wiki/Singidunum)
- `/identity/capitals`: no seat for 454-472 and 505-535 (try https://en.wikipedia.org/wiki/Ardaric)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Gepids: confirmed: infobox 'Ardaric established an independent Gepid kingdom following the Hunnic defeat at the Battle of Nedao: 454'; 'a large part of the former Roman province of Dacia, north of the Danube'
- `/ledger/1` https://en.wikipedia.org/wiki/Gepids: confirmed: 'After the Ostrogoths left Pannonia in 473, the Gepids captured Sirmium'
- `/ledger/2` https://en.wikipedia.org/wiki/Gepids: confirmed: 504; 'Comes Pitzia expelled the Gepid troops from Sirmium without much resistance'
- `/ledger/3` https://en.wikipedia.org/wiki/Cunimund: confirmed: 'since 536, after taking it from the Byzantine emperor Justinian I'
- `/ledger/4` https://en.wikipedia.org/wiki/Gepids: confirmed: 'height of their power after 537, settling in the rich area around Singidunum'; 'In 539 ... the Gepids and Heruls plundered Moesia'; 'recognize new zones of Gepid occupation'
- `/ledger/11` https://en.wikipedia.org/wiki/Gepids: confirmed: 'The Gepids were finally overrun by the Avars in the 567 Lombard-Gepid war'; infobox 567

Area: No area in the Gepids infobox; acknowledged. The 454 found draws 495 cells against the huns dossier's 986 (see cross_checks); the Gepids page's 'a large part of ... Dacia, north of the Danube' supports the smaller reading.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| kingdom-of-alamannia 462 found (alemanni) | alemanni 461 dissolve | matched | alemanni passes its land to the kingdom. |
| western-roman-empire 462 loss (kingdom-of-alamannia) | kingdom-of-alamannia 462 found | mismatch | WRE /ledger/50 also hands 'the Rhine region, Alsace and Swabia' to Alamannia while alemanni /ledger/5 hands the same land; Alamannia's found names alemanni only. eu-04 should decide which of its two dossiers held Alsace and Swabia in 461. |
| kingdom-of-alamannia 496 loss (salian-franks) | salian-franks 496 gain | mismatch | Year agrees; land does not: salian-franks takes the whole 499 shape, Alamannia only the northern half (Tolbiac page: 'the northern half of the Alammanian lands went to the Franks'). Route to eu-07-a: narrow the Salian gain to Alamannia's /ledger/1 region. |
| ripuarian-franks 496 contest_start (kingdom-of-alamannia) | - | exception | Contest zone in Ripuarian land (Zulpich); Alamannia's Tolbiac war zone covers its own northern half. Not a territorial transfer. |
| ostrogothic-kingdom 500 vassal_start (kingdom-of-alamannia) | kingdom-of-alamannia | exception | Schema: vassal events live in the overlord's ledger only; Alamannia's notes describe the protectorate. Paired vassal_end 536. |
| kingdom-of-alamannia 746 dissolve (kingdom-of-the-franks) | - | exception | kingdom-of-the-franks (eu-07) not written yet. |
| thuringian-states 475 dissolve (kingdom-of-thuringia) | kingdom-of-thuringia 476 found | matched | Cliopatria seam; one kingdom. |
| kingdom-of-thuringia 532 loss (kingdom-of-the-franks) | - | exception | kingdom-of-the-franks (eu-07) not written yet. |
| lombards 488 gain (kingdom-of-odoacer) | kingdom-of-odoacer | missing | kingdom-of-odoacer (eu-04) gains Rugiland in 488 and keeps it in its 488-493 keyframe with no loss to the Lombards; its own note says the Lombards settled the province by 493. Route to eu-04: add a loss of Rugiland to lombards (488, or 493 with the Lombards gain moved to match). |
| lombards 546 gain (ostrogothic-kingdom) | ostrogothic-kingdom 546 loss | matched | Both confidence 1. |
| lombards 546 loss (nobody) | - | exception | Rugiland left to nobody. |
| lombards 555 keyframe (kingdom-of-the-gepids) | kingdom-of-the-gepids | mismatch | Syrmia with Sirmium (11 cells) is Lombard in lombards_555/561/567 and outside the Gepid shape 555-567, while the Gepid ledger and capital keep it to 567 and the ERE gains it in 567. Fix on both sides (verdict findings). |
| lombards 567 gain (kingdom-of-the-gepids) | kingdom-of-the-gepids 567 loss | matched | Same region (110 cells). |
| lombards 568 gain (eastern-roman-empire) | eastern-roman-empire 569 loss | matched | ERE has one 569/9 loss including Friuli; Lombards split Friuli to 568. Within one year. |
| lombards 568 loss (avar-khaganate) | - | exception | avar-khaganate (eu-06, another part) not written yet. |
| lombards 569 gain (eastern-roman-empire) | eastern-roman-empire 569 loss | matched | Month 9 on both sides. |
| lombards 577 split (duchy-of-tuscia) | - | exception | duchy-of-tuscia (eu-13) not written yet. |
| lombards 586 dissolve (kingdom-of-italy) | - | exception | Kingdom of Italy row (eu-13) not written; split suggested as kingdom-of-the-lombards (author's counterparts_needing_dossiers). |
| ostrogothic-kingdom 500 found (ostrogoths) | ostrogoths 499 dissolve | matched | Cliopatria seam. |
| eastern-roman-empire 493 vassal_start (ostrogothic-kingdom) | ostrogothic-kingdom 500 found | mismatch | ERE /ledger/25 makes ostrogothic-kingdom its vassal from March 493, but that dossier starts in 500 (493-499 is ostrogoths). Route to eu-05: name ostrogoths for 493-499 or start the tint at 500. vassal_end 535 is fine. |
| ostrogothic-kingdom 504 gain (kingdom-of-the-gepids) | kingdom-of-the-gepids 504 loss | matched | Sirmium. |
| ostrogothic-kingdom 510 gain (visigothic-kingdom) | visigothic-kingdom 510 loss | matched | Provence; the Ostrogothic Kingdom page says 'at the expense of the Burgundians' (noted by the author). |
| ostrogothic-kingdom 511 vassal_start (visigothic-kingdom) | - | exception | Overlord's ledger only (schema); paired vassal_end 526. |
| ostrogothic-kingdom 535 loss (eastern-roman-empire) | eastern-roman-empire 535 gain | matched | Sicily, month 12 both. |
| ostrogothic-kingdom 536 loss (eastern-roman-empire) | - | missing | Sirmium (confidence 1): ERE has no Sirmium event between 504 and 567, neither this gain nor the 536 loss to the Gepids. Route to eu-05. |
| kingdom-of-the-gepids 536 gain (eastern-roman-empire) | - | missing | Sirmium taken from Justinian (Cunimund page); no ERE loss. Route to eu-05. |
| ostrogothic-kingdom 536 loss (kingdom-of-the-franks) | - | exception | Raetia; kingdom-of-the-franks not written yet. |
| ostrogothic-kingdom 536 loss (eastern-roman-empire) | eastern-roman-empire 536 gain | matched | Dalmatia June; southern Italy December. |
| ostrogothic-kingdom 540 loss (kingdom-of-the-franks) | - | exception | Provence; kingdom-of-the-franks not written yet. |
| ostrogothic-kingdom 540 loss (eastern-roman-empire) | eastern-roman-empire 540 gain | mismatch | May 540 both; land differs on Pavia: ERE /ledger/39 subtracts only Verona and Brescia, so it takes Pavia, which the Gothic War page says 'remained unconquered' and became the Gothic capital. Route to eu-05: subtract admin1 Pavia too. |
| ostrogothic-kingdom 541 gain (eastern-roman-empire) | - | missing | Venetia and Liguria regained by Ildibad (Gothic War page); ERE has no 541 loss. Route to eu-05. |
| ostrogothic-kingdom 543 gain (eastern-roman-empire) | eastern-roman-empire 543 loss | matched | Naples. |
| ostrogothic-kingdom 546 loss (lombards) | lombards 546 gain | matched | Pannonia. |
| ostrogothic-kingdom 546 gain (eastern-roman-empire) | eastern-roman-empire 546 loss | matched | Month 12 both. |
| ostrogothic-kingdom 547 loss (eastern-roman-empire) | eastern-roman-empire 547 gain | matched | Rome. |
| ostrogothic-kingdom 550 gain (eastern-roman-empire) | eastern-roman-empire 550 loss | matched | Rome. |
| ostrogothic-kingdom 552 loss (eastern-roman-empire) | eastern-roman-empire 552 gain | matched | Peninsula south of the Po. |
| ostrogothic-kingdom 562 loss (eastern-roman-empire) | eastern-roman-empire 562 gain | matched | Verona and Brescia. |
| huns 454 loss (kingdom-of-the-gepids) | kingdom-of-the-gepids 454 found | mismatch | huns /ledger/21 and /ledger/23 hand the Gepids all Dacia plus the Tisza country (986 cells, about 249,000 km2); the Gepid found draws 495 cells. 483 cells (Muntenia, Oltenia) are in no one's hands. The Gepids page ('a large part of the former Roman province of Dacia, north of the Danube') supports the smaller reading; route to eu-06-a to narrow the huns losses or name another holder. |
| kingdom-of-the-gepids 473 gain (nobody) | ostrogoths 474 loss | exception | Both sides 'nobody' (Ostrogoths leave Pannonia 473/474); within one year. |
| eastern-roman-empire 510 loss (kingdom-of-the-gepids) | kingdom-of-the-gepids 539 gain | mismatch | South Danube bank: ERE /ledger/28 at 510 (confidence 1, Cliopatria) against the Gepid 539 gain (confidence 2, Gepids page 'after 537' and 'In 539 ... recognize new zones of Gepid occupation'). Route to eu-05: move the loss to 539. |
| kingdom-of-the-gepids 555 loss (eastern-roman-empire) | eastern-roman-empire 555 gain | matched | Both confidence 1. |
| kingdom-of-the-gepids 567 loss (lombards) | lombards 567 gain | matched |  |
| kingdom-of-the-gepids 567 loss (avar-khaganate) | - | exception | avar-khaganate not written yet. |
| kingdom-of-the-gepids 567 loss (eastern-roman-empire) | eastern-roman-empire 567 gain | matched | Sirmium (but see the Syrmia keyframe mismatch). |

## Problems and routes

- Reviewer applied three small fixes (lombards rulers/3 and wars/4 clipped to 586, ostrogothic-kingdom rulers/0 from 500); both files re-validated with 0 errors. The authors of the failed dossiers should re-read them before revising.
- thuringian-states and kingdom-of-thuringia are one kingdom on the one page (Thuringii); the research brief's one-dossier-per-state rule points to a merge under thuringian-states. Orchestrator's decision; neither dossier is faulted for it.
- Routes to other groups: eu-05 eastern-roman-empire (Sirmium 536 gain and loss missing; 541 Venetia/Liguria loss missing; 540 gain should exclude Pavia; 510 Danube-bank loss should be 539; 493 vassal names ostrogothic-kingdom, which starts 500); eu-04 kingdom-of-odoacer (no 488-493 loss of Rugiland to lombards) and western-roman-empire/alemanni (Alsace and Swabia handed to Alamannia twice in 461-462); eu-07-a salian-franks (496 gain should be Alamannia's northern half only); eu-06-a huns (454 losses to the Gepids, 986 cells against 495).
- Gazetteer: place 'Pavia' is not in the gazetteer (admin1 Pavia is); not used as a place by these dossiers.
- No page failed to load for the reviewer.
