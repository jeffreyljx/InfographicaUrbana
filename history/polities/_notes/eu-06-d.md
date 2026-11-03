# Notes: group eu-06-d (Migration kingdoms, part d)

Written 2026-10-19 by the Phase B research agent for eu-06-d. Dossiers: visigothic-kingdom, vandal-kingdom, ostrogoths, rugiland (the four owned states) and two rebel states added for the Visigothic civil wars, revolt-of-athanagild and revolt-of-hermenegild. All six validate with 0 errors and 0 warnings, and every region resolves through the gazetteer (`--resolve`). 23 distinct pages opened (32 source entries across the six dossiers, since pages are shared); two page URLs failed. WebFetch returns an extraction of each page, so the quotation marks in the notes carry that extraction's wording; the reviewer should treat them as close paraphrases of the page.

## What changed against Cliopatria (other dossiers must follow)

- Visigothic Kingdom: starts 418 (Honorius's grant, infobox 'Established: 418'), not 426; ends 721 (Ardo dies, Septimania occupied), not 723. Cliopatria's 718-723 shape draws Septimania plus Galicia, Asturias and Cantabria as Visigothic; the dossier keeps Septimania only and gives the north-west coast to the Kingdom of Asturias (Cliopatria row 724; Pelagius's revolt is 718 on the Visigothic page, Covadonga 722 on the Umayyad page). The Asturias and Umayyad dossiers should show the north-west coast and Septimania accordingly.
- Vandal Kingdom: starts 435 (treaty and capital Hippo Regius), not 439; ends 534 (March), not 533. Cliopatria draws all of Sicily from 441 to 489; the pages give a failed siege of Palermo (440), occupation 468-476 and the Lilybaeum toehold to 491. Balearics, Sardinia, Corsica and Malta are 455 (Cliopatria 439, 458, 469). The 455 shape's patch round Rome (19 cells) is a sack of about a fortnight. Mauretania is lost after 477 and the Frexenses and Laguatan take land in 510 and the 510s, which Cliopatria keeps inside to 533.
- Ostrogoths: Cliopatria's 455-489 Pannonian shape is only right to 473; the pages have the Goths on East Roman land (Moesia 474, Epirus 479, Dacia Ripensis and Moesia Inferior 483) until autumn 488, so the 476 and 480 shapes are marked wrong. The 490 shape (Italy plus the old Pannonian land) is cut to the north of Italy for 490-492 and replaced for 493-499 by Odoacer's realm (Italy with Sicily but not Sardinia, and Dalmatia; see the revision below). The Goths in Moesia and Epirus are Eastern Roman federates (vassal_start 474 and 479, vassal_end 488), not conquerors of imperial land.
- Rugiland: ends 487 (Odoacer's victory), not 489; starts 454, not 455.

## Needs a decision

- Ostrogoths (455-499, Q103122) and the Ostrogothic Kingdom (500-560, Q583038) are one people and one realm on every page opened (kingdom in Italy founded 493). The Ostrogoths dossier ends 499 to match Cliopatria's rows, holds Italy for 493-499 (keyframe ostrogoths_493) and carries a `rename` at 493 and a bridging `dissolve` at 499. The Ostrogothic Kingdom dossier is not written yet: it should start at 500 from Cliopatria's row; if its author starts it in 493, the two overlap in 493-499 and the orchestrator should trim the Ostrogoths dossier to 492 (moving the rename and the three 493 gains to the kingdom) or merge the two. The kingdom-of-odoacer dossier already names 'ostrogoths' as the counterpart of its 493 dissolve.
- The Ostrogothic Kingdom dossier should record a vassal tint over the Visigothic Kingdom 511-526 (Theodoric the Great page: 'In 511, the Visigothic Kingdom was brought under Theodoric's direct control'); here it is a `rename` event.
- Provence 508-510: the Ostrogothic Kingdom page has Theodoric's generals campaigning in Gaul from 508 'at the expense of the Burgundians' (and says nothing of the Visigoths); the Euric page has Provence Visigothic since 475 (Nepos 'renounced Provence in 475'); the Visigothic Kingdom page says only 'the Rhone and the Loire' for 476. The 475 gain and the 510 loss to the Ostrogoths are both recorded, the second at confidence 1.

## Unsettled, by state

Visigothic Kingdom
- Pages that failed: https://en.wikipedia.org/wiki/List_of_Visigothic_kings and https://en.wikipedia.org/wiki/List_of_Visigoth_kings (not found). The ruler list is the Visigothic Kingdom article's own table, which gives two sets of years for several reigns (noted per ruler); rebels (Iudila, Froia, Suniefred) are left out.
- Ten pages opened against a budget of nine; the Vascones page gave no Visigothic dates.
- No page opened dates: the Cliopatria northern gains of 592-612 (Cantabria, Asturias, Burgos; confidence-1 events at 602 and 612), the loss of the Rioja-Navarre-Aragon belt in 661 (confidence 1), +19 coastal cells in 567, +12 cells in 592. The 523-554 shapes are unchanged in substance (Amalaric's defeat in 531 and Theudis's reign are not on the pages opened).
- Septimania's seat under Ardo (714-721) is not named on any page; no capital is invented after 711.
- Infobox areas: 500,000 km2 for 484 (Cliopatria 480 shape 689,151: ratio 1.38) and 600,000 km2 for 580 (577 shape 438,274: ratio 0.73); both inside the factor of two.
- Byzantine Spania has no dossier (province of the Eastern Roman Empire, 552-624).

Vandal Kingdom
- The Vandal Kingdom page gives no area. Months: Carthage 19 October 439 (Gaiseric page); Ad Decimum 13 September 533; the Carthage entry of 15 September rests on the Vandalic War page's wording; Tricamarum 'mid-December' (Vandalic War page) against 15 December (Vandal Kingdom page); surrender March 534.
- The pages date the Balearics, Sardinia, Corsica and Malta only collectively (455) and give no date for the end of Vandal rule there but the 533-534 war.
- Aures (484) lie inland of the coastal Cliopatria shape, so that loss changes no cell.
- Frexenses (Kingdom of the Dorsale, 510), Laguatan (King Cabaon, 510s), Godas's Sardinia and Pudentius's Tripolitania (533) have no dossier.
- The Odoacer page has the Vandals invading Sicily in 490; the Gaiseric page has the Lilybaeum toehold ceded to Theodoric in 491; the Vandal Kingdom page has Gunthamund losing 'large parts of Sicily' to the Ostrogoths. Settled for the Ostrogoths dossier in the revision below: Lilybaeum is a 491 gain (Gaiseric page), the rest of Sicily a confidence-1 gain at 493.

Ostrogoths
- Dates that differ: Nedao 454 (Nedao, Ostrogoths pages) against 453 (Rugiland page); Theodemir's death 474 (Ostrogoths) against 475 (Theodemir page); the treaty with Odoacer 2 February (Theodoric the Great) against 25 February (Odoacer).
- Not on any page: the date of the Pannonian settlement, who held Pannonia 474-504, Valamir's and Videmir's reigns. Theoderic Strabo's Goths (473-481) have no dossier.
- Six pages opened against a budget of five (Nedao shared with Rugiland). No infobox area on any page (the Ostrogoths, Theodoric the Great and Ostrogothic Kingdom pages re-checked on 2026-10-19).

Rugiland
- No capital on the page. The start is soft (453 rebellion, 454 reign list and Nedao, 467 kingdom in the infobox). The Lombard settlement of the land is undated; Moravia and Severinus are not on the page.

## Region names the gazetteer lacks (all resolve through other forms)
Pannonia (used as text only), Zeugitana (Carthage 200 km disc), Aures Mountains (Batna + Khenchela), Thugga/Dougga (a 60 km disc by coordinate), Lilybaeum (Marsala), Orospeda (Murcia admin1), Waldviertel and Weinviertel (Cliopatria shape).

## Revision 2026-10-19 (ostrogoths, after the adversarial review)

Review verdict for ostrogoths was fail on one blocking finding and two missing mirrors; all three are applied, the dossier validates with 0 errors and 0 warnings under `--resolve`, and the area comparison is now acknowledged in the ostrogoths_493 keyframe.

What changed:
- Keyframes. The old ostrogoths_490 correction (the 490 shape inside Italy, 120,380 km2, southern edge 43.76 N, years 490-499) left out Rome, the south and Sicily, a factor of 2.05 under the 246,830 km2 that Cliopatria's Ostrogothic Kingdom 500 shape holds inside Italy. It is now three keyframes: ostrogoths_490 (northern Italy but for Ravenna, 119,116 km2, year 490), ostrogoths_491 (the same plus a 40 km disc at Lilybaeum, 491-492) and ostrogoths_493 (Italy less Sardinia, with Sicily, plus Dalmatia, 293,870 km2, 493-499; the Italian part is 1.07 times the successor's). Ravenna is taken out of the 490-492 shape because Odoacer held it under siege until 5 March 493, which the ledger already said.
- Ledger. Added: 491 gain of Lilybaeum from vandal-kingdom (Gaiseric page footnote, mirrors vandal-kingdom /ledger/11, confidence 2); 493 gains of Sicily (but Lilybaeum) and of Dalmatia from kingdom-of-odoacer (confidence 1: no page dates their passing; the Ostrogoths page names Italy, Sicily, Dalmatia and the lands north of Italy in the Ostrogothic power around 500). Changed: the 493 gain of Ravenna alone is now Ravenna and the rest of Italy south of the 490 line (121,139 km2, confidence 3: 'master of Italy', Theodoric the Great and Odoacer pages); the 490 gain's text now says what it resolves to (northern Italy, not 'Italy but for Ravenna'); the 499 dissolve carries the 493-499 shape. The 474 and 479 gains and the 488 loss against eastern-roman-empire became vassal_start (474 Moesia, 479 Epirus) and two vassal_end (488), counterpart eastern-roman-empire, because the Ostrogoths page has the Goths on Eastern Roman land as a 'federate kingdom' and the Empire's dossier has no loss. identity.predecessors now lists kingdom-of-odoacer. Two sources added (Gaiseric, Vandal Kingdom), eight pages in all against a budget of five.

What I disagree with, or could not settle:
- The reviewer asked to keep the north-Italian shape for 490-492. I kept it, but the Odoacer page says Theodoric 'seized most of Italy by 490'; it names only Milan, Pavia and Ticinum and not Rome or the south, so I left the south in the contested zone (contest 489-493) rather than draw it Gothic. Whoever reads the page differently can widen ostrogoths_490.
- The reviewer allowed 'a new keyframe 493-499 with Dalmatia if a page dates it'. No page dates it. I included Dalmatia and Sicily at confidence 1 because Odoacer's dossier (/ledger/3, /ledger/2) holds both to his death and the Ostrogoths page has them Gothic around 500; the alternative is to leave them to the Ostrogothic Kingdom dossier. Raetia, Noricum and the Rugians' land are not drawn: no page dates them, and the Odoacer page has the Lombards settling the Rugians' land by 493.
- Vassalage dates. I dated vassal_start to 474 (the entry into Eastern Roman territory, 'in 473/474', Ostrogoths page); the same page puts the federate kingdom's recognition 'about 476', and eastern-roman-empire has 483 (Theodoric the Great page, magister militum praesentalis) as its vassal_start with a 488 vassal_end. The ERE author should move its 483 back to 476 or 474 or say why not. The Epirus pair is held coarsely to 488 (no page dates the Goths' departure from Epirus).
- eastern-roman-empire's 493 vassal_start names ostrogothic-kingdom while Italy is the Ostrogoths dossier's to 499; its tint from 493 rests on the Ostrogothic Kingdom page's 'recognized by the new Emperor Anastasius in 497', so no vassalage is recorded here after 488. The ERE author and the Ostrogothic Kingdom author should settle that pair.
- western-roman-empire (eu-04) has a 455 loss of Pannonia to the Ostrogoths (confidence 1) while ostrogoths and huns hold it as Hunnic land to 454; one holder must go (not touched here; the other batch owns it).

Counterparts needing a dossier from another group: ostrogothic-kingdom (500-560, eu-06; see above for where it should start), and Theoderic Strabo's Goths (473-481, no row in Cliopatria).
