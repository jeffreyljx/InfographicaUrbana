# eu-06-e notes (Migration kingdoms, part e)

Six dossiers written and validated (python3 -I tools/validate_dossier.py --resolve): kingdom-of-alamannia, thuringian-states, kingdom-of-thuringia, lombards, ostrogothic-kingdom, kingdom-of-the-gepids. All pages read 2026-10-19 through WebFetch. No unresolved gazetteer name after the repair pass (Bardowick dropped from lombards).

## Cross-cutting
- Two rows that are one state: Thuringian states (469-475) and Kingdom of Thuringia (476-533) are the Thuringii on the one page opened; Ostrogoths (455-499, eu-06-d) and Ostrogothic Kingdom (500-560) are one realm (Italy from 493). Lombards (480-586) and Kingdom of Italy (587-1946) share the Lombard kingdom to 774. Seams are Cliopatria's, written as dissolve events at confidence 1. Merge or relink in Phase C.
- Cliopatria Wikipedia fields: 'Thuringian states' is the 1871-1920 states page (opened, nothing on the 5th century); 'Basina of Thuringia' is a person page.
- Page budget exceeded only for ostrogothic-kingdom (six pages, two of them empty: Battle of Vouille, Provence). Failed URLs: Lantfrid,_Duke_of_Alemannia (replaced by /Lantfrid), Battle_of_Burgscheidungen.

## kingdom-of-alamannia (462-746, 5 of 5 pages)
- Cliopatria has no shape for 500-723 and ends in 731; added keyframes 496-723 and 732-745, end moved to 746 (Cannstatt).
- 462-490 shapes adjusted: Lorraine, Champagne and the Trier district removed (163 of 475 cells); the page says Strasbourg to Augsburg. Salian Franks (eu-07-a) also found the shape too wide.
- No capital on any page (Augsburg and Cannstatt only for counties): capitals empty.
- Status after 496 for other dossiers: southern half under Ostrogothic protection 496-536 (ostrogothic-kingdom carries vassal_start 500, vassal_end 536); nominal Frankish duchy from 536, broke away after 638 (Alamannia page), Frankish campaigns 709-746. kingdom-of-the-franks (eu-07) should carry a vassal tint 536-638 and from 709; no event here changes land in those years.
- Alsace: Alemanni page has it conquered in 406, Alamannia page says outside Alamannia in the early period; 462-495 shapes keep it, later keyframes do not.
- Salian Franks dossier takes the whole 499 shape at 496; this one gives the Franks the northern half only (Tolbiac page) and keeps the Lake Constance core.

## thuringian-states / kingdom-of-thuringia (469-475, 476-532, 3 pages shared)
- Thuringii page: kingdom 'conquered by the Franks in 531-532'; Cliopatria ends 533, dossier ends 532 and the 523 keyframe is cut to 523-532. The 523 break in Cliopatria is unexplained (identical shape).
- No capital, no ruler dates, no frontier, no Saxon partition on the pages (Battle of Burgscheidungen not found). Counterpart saxons not used.

## lombards (480-586, 5 of 5 pages)
- 480 shape (Scania) and 490 shape (migration trail) wrong: legend, undated. Repair pass: 480-487 is now the Middle Danube (Lombards page: 'previously settled in the Middle Danube in the 5th century, near what is now Austria, Slovenia and Hungary'; a 110 km circle round Szombathely, confidence 1), left in 488 for Rugiland; the Bardowick reading and its unresolved place name are dropped.
- Move from Rugiland to the Feld/Pannonia undated (Cliopatria 546, Audoin about 547); the Wacho page (reign c. 510-539) is silent on it. Counterpart ostrogothic-kingdom at confidence 1; the Audoin page says Justinian settled them in 'Roman Pannonia'.
- Friuli (568) is split from the 569 Po-valley gain; the Eastern Roman Empire dossier has one 569/9 loss including Friuli.
- Duchy of Tuscia stands apart from 577 in Cliopatria (split event, confidence 1). Spoleto and Benevento are Cliopatria rows from 577 outside the Lombard shape; the pages do not date them.
- Heruli war c. 494-511: dates only, outcome not on the page; Heruli have no dossier here.

## ostrogothic-kingdom (500-562, 6 pages for the state)
- Start 500 (Cliopatria) although the realm is Theodoric's from 5 March 493; the Ostrogoths dossier holds 493-499 and names this one as successor. End 562 (Verona and Brescia) against 553 (Teia) on the Ostrogothic Kingdom page.
- Shapes corrected: 500-503 (no Sirmium until 504, Dalmatia added), 510 and 534 (Sirmium and Dalmatia), 540-545 (Cliopatria's shape is Pannonia with no Italy; the Gothic War page keeps Pavia, Verona, Brescia, then Venetia and Liguria, then Totila's south), 546-554 (cut to 546-551 plus a 552-554 rump).
- Eastern Roman Empire mirrors in year and region: 535 Dec, 536 Jun, 536 Dec, 540 May, 543, 546 Dec, 547, 550, 552, 562. No ERE mirror for: the 536 Sirmium loss, the 541 Venetia and Liguria gain, the 546 Pannonia loss (counterpart lombards), the 541-552 contest.
- Provence 510: Cliopatria's 94 cells are Visigothic until 509 (counterpart visigothic-kingdom); the Ostrogothic Kingdom page says 'at the Burgundians' expense'. The 540 Frankish gain of Provence is a bridge: the Witiges page has the cession proposed under Theodahad and agreed by the Franks, with no year.
- Alpine cells lost in 536 (Raetia): no page names Raetia; counterpart kingdom-of-the-franks at confidence 1.
- The Alemannic protectorate (496-536) is recorded here from 500 only.
- Not on the pages: Ildibad and Eraric dates, Raetia and Noricum as Ostrogothic land, Campsa beyond its siege to spring 555, how Sirmium passed to Justinian.

## kingdom-of-the-gepids (454-567, 4 of 5 pages)
- Cliopatria starts 510 and ends 566; dossier runs 454 (Nedao) to 567 (pages). New keyframes 454-472, 473-503, 504-509, 536-538, 539-545; the 510 shape is cut to 510-535 without Sirmium (expelled 504) and without the south Danube bank (Gepid only after 537, recognised 539).
- Mismatch with huns (eu-06-a): its 454 loss hands the Gepids all of Dacia (986 cells, about 249,000 km2); this dossier draws the Cliopatria heartland (495 cells). 483 cells (chiefly Muntenia and Oltenia) are in no one's hands here; to decide.
- Sirmium: Ostrogothic from 504; Gepid 'since 536' after being taken from Justinian (Cunimund page, 537 on Thurisind). Eastern Roman Empire (eu-05) has no Sirmium event before 567.
- 555 drop of the Danube bank is Cliopatria's and unverified (page silent). Capital Sirmium 473-504 and 536-567 only; no page names a seat for 454-472 or 505-535.

## Repair pass, 2026-10-20 (reviewer eu-06-e: lombards, ostrogothic-kingdom, kingdom-of-the-gepids failed on keyframes)
Pages re-opened with WebFetch: Cunimund, Gothic War (535-554), Ostrogothic Kingdom, Lombards. New pages: Teia, Theudebert I, Ildibad, Sirmium, Wacho, Odoacer, Heruli, Duchy of Tuscia, Singidunum, Ardaric. All three dossiers validate with 0 errors and 0 warnings (--resolve).
- Applied by the reviewer and kept: lombards rulers/3 and wars/4 clipped to 586; ostrogothic-kingdom rulers/0 from 500.
- Sirmium (blocking, lombards and kingdom-of-the-gepids): S = intersect(Lombards 555, Gepids 546) = 11 cells, Syrmia with Sirmium, 2,782 km2. Lombards keyframes 555, 561 and 567 now minus S (verdict adjust, source Cunimund); Gepid keyframes 555 and 561 and the dissolve region now plus S. Cunimund page: Sirmium Gepid 'since 536', handed to the Byzantines before his death in 567, no year. Eastern Roman Empire (eu-05) gains Sirmium at 567 with 25 km, the Gepid ledger loses it with 40 km.
- ostrogothic-kingdom 546-562 (blocking): 546-551 is Cliopatria's 546 shape plus Pavia, Verona and Brescia; 552-554 the 555 rump plus the same three; 555-562 the 555 rump plus Verona and Brescia in full. New ledger events: 546 loss to kingdom-of-the-franks (Venetia and Liguria in part) and 555 loss of Pavia to the Eastern Roman Empire (confidence 1, no page dates it). Ildibad and Eraric added to the ruler strip.
- Disagreement with the reviewer (Venetia and Liguria in 546-551): the Theudebert I page says that during Totila's resurgence the Franks 'captured the Cottian Alps, parts of the Liguria region, and the greater part of Venetia' (Theudebert died end 547 or early 548). Adding the whole Veneto and Liguria to 546-551, as the reviewer suggested, would contradict it; Cliopatria's 546 shape already holds 34 of the Veneto's 71 cells and none of Liguria's 24, so the keyframe keeps Cliopatria's share and the ledger records the loss at 546 (confidence 1, year bridged). kingdom-of-the-franks (eu-07) should carry the matching gain; the Eastern Roman Empire (eu-05) holds the Po valley from its 540 gain in Cliopatria's data and has no event for 541 or 552.
- Pages disagree: Mons Lactarius is October 553 (Gothic War page) and October 552 (Teia page). The Ostrogothic dossier keeps the 552 loss of the peninsula, which both fit.
- Thin findings answered: lombards 488 Rugiland gain raised to confidence 2 (Heruli page: Lombards occupy the Rugian country in 488; Odoacer page: 'settled by the Lombards by 493'); Wacho, Heruli and Duchy of Tuscia pages added to the notes of events 546, the Heruli war and the 577 split (Tuscia 'Established: 576' on its infobox against Cliopatria's 577). Ostrogothic: the Sirmium page is silent on how Justinian got Sirmium before 536; the Theudebert I page has Vitiges ceding Provence and part of Raetia, undated; Wacho silent. Gepids: Singidunum page gives no Byzantine return before 596 ('the Byzantines recaptured it in 596'), Ardaric page names no seat, so the 555 Danube-bank loss stays Cliopatria's at confidence 1 and capitals for 454-472 and 505-535 stay empty.
- Still open: kingdom-of-odoacer (eu-04) has no 488-493 loss of Rugiland to the Lombards; eastern-roman-empire (eu-05) has no Sirmium event for 536 (its 567 gain uses 25 km), no 541/552 Venetia and Liguria events and takes Pavia in 540; kingdom-of-the-franks (eu-07) has no matching gains; the huns/Gepids 454 mismatch (483 Dacian cells) is unchanged; Heruli still has no dossier.
