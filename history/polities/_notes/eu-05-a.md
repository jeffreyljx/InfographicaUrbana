# eu-05-a — research notes (written 2026-10-18)

One owned state: **eastern-roman-empire** (Cliopatria "Eastern Roman Empire", 395..632, 36 shapes). Dossier: `history/polities/eastern-roman-empire.json` (after the review fixes of 2026-10-19: 100 events, 36 keyframe verdicts: 17 ok / 19 adjust / 0 wrong, 23 wars, 49 sources; validates with 0 errors; `--resolve` resolves all 396 regions with no unknown names). The two remaining validator warnings (vassal_start for `lazica` 626 and `ghassanids` 629 without a vassal_end) are intended: both relations run to the state's end in 632 and continue under `byzantine-empire`.

## Eastern Roman Empire (eastern-roman-empire, 395-632)

### Cliopatria rows to split or merge
- **One state, three rows.** "Roman Empire" (-31..394), "Eastern Roman Empire" (395..632) and "Byzantine Empire" (633..1474) are one continuous polity; Wikidata Q12544 is shared by the first two and Seshat's 632/633 cut (tr_east_roman_emp → tr_byzantine_emp_1) matches no political event. The dossier covers 395-632 only because the brief assigns the other rows to other agents; its `end` is a hand-over (`dissolve` → `byzantine-empire`, confidence 1). Rule 2 (one colour for life): the colour agent should give `eastern-roman-empire` and `byzantine-empire` the same colour, and arguably `roman-empire` too. The sibling owner of `byzantine-empire` should set its `found` 633 as a hand-over from `eastern-roman-empire`, not a new state.
- **"Georgia" 567-576** (neighbour row in the seed) is Lazica/Egrisi, the Eastern Roman client kingdom, not a Georgian state; **"Lazica" 395-545** ends while Persia held eastern Lazica (Petra 541-551). The dossier keeps Lazica as a vassal tint (395-541, 551-617, 626-632) over the Colchis region; whoever owns the Caucasus rows should merge Cliopatria's Lazica and Georgia 567-576 into one `lazica` dossier.
- **Ostrogothic allegiance 500-554** (seed relation: ERE suzerain of ostrogothic-kingdom) is wrong at both ends: Theodoric ruled Italy under imperial mandate from 493 and the Gothic War began in 535. Dossier: vassal_start 493/3, vassal_end 535.
- **"Kingdom of Soissons" 476-479** shape (bbox to 19.46 E, 42.24 N) seems to include Odoacer's northern Italy. The Western Europe group should check that row; Odoacer's Italy (476-493) has no Cliopatria row at all.
- **"Hunnic Empire" 46 km² residues 633-673** (data/README.md) are outside this range; nothing to do here.
- **Sirmium** (Pannonia Secunda) is never drawn Eastern although it was transferred to the East in 437 and Roman 567-582; the dossier adds it in the 439-440 and 567-582 corrections.

### Shape corrections made (keyframe_review)
Hunnic raid 395-398 and Alaric's Goths in Greece (395-397) and Epirus (397-401) drawn as foreign territory (396, 397, 402 shapes → occupations, not borders); Epirus "nobody's" 402-406; the 447 Moesian strip removed from the 443 shape (Danube cities lost 441, strip ceded 447, restored 449-451); northern Syria given to Persia 540-545 after a raid (restored); Verona and Brescia Roman from 540 though Gothic to 562; a Sophene-to-Tigris strip given to Persia 577-586 while Dara (573-591) and Martyropolis (589-591) never removed; 602-611 shape keeps Mesopotamia lost 604-610; 612-616 keeps Syria and Palestine lost 613-614; Egypt kept to 622 though lost 619-621; 104 Naissus-Serdica interior cells returned 623-629 without a source; Armenia/Mesopotamia drawn imperial 626-628 during Heraclius's campaigns (treated as contested); northern Syria returned 627-628, a year or two before Shahrbaraz's evacuation (629). Noise not treated as events: Malta cell missing 441-442; one to three cells flicker in 452, 459, 469, 490, 523, 587.

### Pages that would not load
- https://en.wikipedia.org/wiki/Roman%E2%80%93Sasanian_War_of_440 (not found)
- https://en.wikipedia.org/wiki/Roman%E2%80%93Sasanian_War_(440) (not found)
The 440 Persian raid rests on the Roman–Persian Wars page (war entry only, no border change).

### Disagreements between pages
- Anatolius's treaty: 443 (Attila page, Bury) vs 447 (Theodosius II page, Kelly); the strip treaty autumn 447 or 448 (Battle of the Utus page); war's end 449 (Huns page). Dossier: Danube cities lost 441, strip 447 (conf 2), contest closed 449.
- Dara's fall 604 (Roman–Persian Wars) vs 605 (602-628 war page). Dossier: 604.
- Antioch's fall 611 (Roman–Persian Wars, "the Persians overran Syria") vs 613 (Battle of Antioch). Dossier: Syria lost 613, Caesarea occupation 611-612.
- Alexandria's fall June 619 (Sasanian conquest of Egypt) vs "about a year" of resistance (602-628 war page). Dossier: 619/6.
- True Cross restored 629 or 630 (Heraclius vs 602-628 pages); Egypt/Levant evacuated "summer of 629" (Egypt page) — Cliopatria's 629 shape agrees.
- Duchy of Benevento founded 571, 577 or c. 590; Spoleto 571 or after 576 (Lombard and duchy pages). Dossier follows Cliopatria's 577 shape with conf 2.
- Avars at the Danube 558 (Sclaveni page) vs 568 (Avar–Byzantine wars page); Cliopatria's 561 delta cells have no dated source (conf 1).
- Lazica page internally inconsistent on the first Christian king (Gubazes I vs Tzath I); not used.

### States that need a dossier from another group
- ~~Kingdom of Odoacer~~ now exists as `kingdom-of-odoacer.json` (eu-04-b); the counterpart is the slug since the review. That dossier still lacks the matching vassal_start 476/9 / vassal_end toward `eastern-roman-empire` (route to eu-04).
- **Moorish kingdoms of Africa (Mauri; Altava, the Aures)** 534-548 contest — Africa group, if wanted; Cliopatria has no polity. Counterpart written as "Mauri (Moorish tribes)"; `kingdom-of-the-aures` (539 loss to the empire, 544 gain) and `kingdom-of-altava` now exist, but the 534-548 contest is a whole-interior contest, so the name is kept; the Aures 539/544 land changes are covered by the contest here, not mirrored as events.
- **Sclaveni / sclaviniae** of the Balkan interior (617-632 and after): stateless; this dossier gives their land to `nobody` from 630 (Cliopatria's 630 shape). No dossier suggested, but the Balkan owners after 632 should keep that convention.
- `lazica` (395-632 as one client kingdom, see above) and `ghassanids` (Cliopatria 510-633; vassal from 473 per the Ghassanids page) need their owners to adopt the vassal dates used here: Lazica 395-541, 551-617, 626-632; Ghassanids 473-613, 629-632.

### Region names the gazetteer lacks (given as coordinates in the dossier)
- Rhodes (place) — 28.0 E 36.2 N, km 40.
- Dara (place) — 37.18 E 37.18 N (Oğuz near Mardin), km 25.
- Martyropolis / Silvan (place) — 41.0 E 38.14 N, km 20.
- Viminacium (place) — 21.2 E 44.74 N (Kostolac), km 25.
Natural Earth admin-1 "Verona" and "Brescia" (Italian provinces) were used for the Gothic north 540-562.

### Low-confidence events (confidence 1) and what a gap-filler could open
401 Hunnic withdrawal (Huns page dates the raid, not the departure); 469 Crimea/Bosporus gain (Cliopatria's 469 shape; Chersonesus page undated); 510 loss and 555 gain of the Gepid Danube bank (Gepids page undated at those years); 561 Avar delta cells; 588 Singidunum regained; 592 Spain contraction (Spania page: Leovigild 570s, Sisebut 614-615); 613 Ghassanid vassal_end and 629 vassal_start (phylarchate suspended 584, Persian Syria 613, return inferred); 617 Lazica vassal_end and Colchis/Iberia loss; 628 Rhodes occupation_end (Rhodes 617-629 in Cliopatria; no page opened dates the Persian seizure); 632 dissolve (hand-over).
Pages worth opening: "Siege of Amida (502–503)", "Sack of Antioch (540)", "Siege of Constantinople (626)", "Byzantine–Lombard wars", "Mauro-Roman Kingdom", "Siege of Thessalonica (586)", "Bosporan Kingdom" (Justinian c. 528), "Theodosius I" (the 395 partition), "Siege of Tiflis (627–628)", "Rhodes" (Persian occupation 622/623-628).

### Infobox area check
2.35 M km² (457) vs Cliopatria 1.98 M (ratio 0.84); 3.4 M km² (565) vs 2.60 M (0.77); Justinian dynasty page "around 2.7 million km²" at greatest extent → 0.96. No shape flagged for area.

## Review fixes of 2026-10-19 (author's return to the dossier)

The adversarial review failed the dossier for four missing items. All four are done; the reviewer's own three fixes (huns, kingdom-of-odoacer, Heraclius 'to' 632) were kept. Re-validated: 0 errors, 2 intended warnings (lazica and ghassanids vassal_start 626/629 run to 632). Pages opened again with WebFetch: Uldin, Alaric I, Dengizich, Mauro-Roman Kingdom, Eutropius (consul 399), Bosporan Kingdom, Chersonesus, Crimean Goths, Gepids, Sirmium, Pannonian Avars, Avar-Byzantine wars, Spania, Ghassanids, Lazica, Rhodes, Byzantine-Sasanian War of 602-628 (eight of them new to the sources list: Uldin, Eutropius, Dengizich, Bosporan Kingdom, Crimean Goths, Mauro-Roman Kingdom, Pannonian Avars, Rhodes). The page budget (14) was spent in the first run; these pages are the fixes' own evidence.

### Applied
- **Uldin 408-409**: occupation_start 408 (conf 2, 'In the summer of 408 ... they entered the Balkans and Thrace'; 'The Huns captured Castra Martis in Dacia Ripensis') and occupation_end 409/3 (conf 3, 'forced to re-cross the Danube by March 23, 409'), counterpart `huns`, region Moesia with the page's text (the same region as huns.json /ledger/6-7); war "Uldin's invasion of Thrace". Only Castra Martis is named as taken; the hatching of all Moesia follows the huns dossier.
- **Greece 395-397, Epirus 397-401**: the 395 occupation_start is narrowed to Thessaly, Central Greece, Attica and the Peloponnese; new occupation_end 397 for that land; new occupation_start 397 for Epirus; the 401 occupation_end narrowed to Epirus (Alaric I page: Stilicho 'pushed Alaric's forces north into Epirus'; 397 magister militum per Illyricum; 399 transfer; invasion of Italy late 401 or spring 402). Keyframe 397 correction text updated. This is a small departure from the reviewer's wording (which kept Epirus in the 395 start and would leave an unpaired end): two pairs instead of one start with two ends.
- **Dengizich 467-469**: contest_start 467 (conf 2) and contest_end 469 (conf 3), counterpart `huns`, zone Moesia + Thrace as in huns.json /ledger/19-20; war "Dengizich's war on the Danube". The Dengizich page ('In 467, Dengizich crossed the frozen Danube'; 'the war dragged on for two years'; killed by Anagastes 'general in Thrace'; infobox died 469) reports no land ceded either way.
- **Garmul's war 570-578**: war entry with empty zones. Mauro-Roman Kingdom page: Theodore and Theoctistus killed 570, Amabilis 571, 'he failed to take any significant town'; campaign 577-78; killed 578; whether the Altava area or coast was incorporated into the empire is 'unclear'. No border change in Cliopatria in those years.

### Thin items worked
- **Hunnic withdrawal (was 401, conf 1)**: now 398, conf 2, source Eutropius (consul 399): 'Eutropius' ascension to power was assisted by his defeat of a Hun invasion in 398'. huns.json /ledger/5 still says 396 (conf 1): it should adopt 398. War "Hunnic invasion of 395" now ends 398.
- **469 Crimea (conf 1)**: still unsupported. Bosporan Kingdom page: Gothic Bosporan realm 'regaining its independence after the empire's collapse in the 450s and 460s', imperial control only after the 527 revolt (Justinian); Chersonesus: 'Byzantine possession during the Early Middle Ages' (no year); Crimean Goths: nothing; Dengizich: no Crimea. The counterpart is now `nobody` (was `huns`) so that it agrees with huns.json, which dissolves the Huns to nobody in 469 and hands the empire Dobruja, not the Crimea. Cliopatria's 75 cells are kept (keyframe 469 ok, unverified). A gap-filler with a page on the Byzantine Crimea (Cherson, Alusta, Gurzuf, Doros) could date it.
- **Gepid bank 510 / 555 (conf 1)**: Gepids page: kingdom 'north of the Danube', 'settling in the rich area around Singidunum' after 537, Moesia plundered 539; silent on 510 and 555. Sirmium page: silent on 555 ('After 567, Sirmium was returned to the East Roman Empire'). Kept as Cliopatria's; the 510 date looks about three decades early.
- **Avar delta 561**: Pannonian Avars: 557 embassy; 'By 562 the Avars controlled the lower Danube basin' -> conf 2, source switched to that page (Sclaveni page in the note).
- **Singidunum 588**: Avar-Byzantine wars: taken 583; 'In 588, they abandoned the siege of Singidunum after only seven days, in exchange for a meagre ransom' -> conf 2 as an upper bound; the page describes no recapture; Viminacium Roman by 599.
- **Spania 592**: still conf 1. The page has no sentence dated 592; the quotation in the ledger note and keyframe 592 was wrong ('By 600 the province reached no further north than the Sierra Nevada' is not on the page; it says 'By the year 600 Spania had dwindled to little more than Malaga and Cartagena and the Balearics' and 'extended no further north than the Sierra Nevada'); corrected. The same page says Reccared's Byzantines 'probably even regained or gained ground' (586-601).
- **Ghassanid client relation 613 / 629 (conf 1)**: Ghassanids page is silent on both; Phocas's accession (602) 'came with an immediate restoration in relations' and the Ghassanids 'played an essential role' on the Byzantine side in the war of 602-628. The 613 break rests on Persian rule of Syria and Cliopatria's gap (617-628) only; the page, read plainly, does not show an interruption. Left at conf 1; the Ghassanid owner (me-06) should decide.
- **Lazica 617 / Colchis-Iberia 617-626**: Lazica page and the 602-628 war page give no year for a Persian hold of Lazica, Colchis or Iberia; Lazica page: 'In the 620s, the Laz, together with the Abasgians, participated in Emperor Heraclius' campaigns'. The 626 gain of Colchis and Iberia (named neither by the Heraclius quote nor by a dated sentence) is lowered from 2 to 1.
- **Rhodes**: Rhodes page and the 602-628 page both give 'In 622/3 ... captured by the Sasanian navy' (ledger 623, conf 2 kept because the year is split); the return (628) is on neither page: conf 1.
- **Nothing to find**: 632 dissolve (hand-over to byzantine-empire).

### Disagreements
- huns.json vs this dossier on the Hunnic raid's end: 396 (huns, conf 1) vs 398 (here, Eutropius page); on Anatolius's treaty and the 447-449 contest years (pages disagree: 443/447/448/449); on the 469 land (Dobruja there, nothing supported here).
- Reviewer's Singidunum suggestion (conf 2) taken, but the page still gives no recapture date: the conf 2 is for 'Roman by 588'.

### Counterparts needing other groups' work
- `huns` (eu-06): ledger/5 end 396 -> 398; add the 441 gain of Singidunum and Sirmium and the 447 strip, the 451 and 455 returns (see the review's cross-dossier matrix).
- `kingdom-of-odoacer` (eu-04): add vassal_start 476/9 and vassal_end 493/3 toward `eastern-roman-empire`.
- `mauro-roman-kingdom` (Altava/Mauro-Roman group): has Garmul's war with the empire; no contest event, none needed (no ground changed hands).
- No new dossier is requested.
