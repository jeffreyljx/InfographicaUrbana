# eu-06-f notes (Bavarians, Avar Khaganate, Duchy of Thuringia)

Written 2026-10-20. Every page named here was opened with WebFetch in this run. Three dossiers, all validate with 0 errors and 0 warnings (also with --resolve).

## Rows to reconcile with other groups

- **Carantania (eu-06) vs Bavarians.** Cliopatria's Bavarians 750-787 = the 661 Bavarian shape + the Carantania shape of 749 (checked cell by cell: 311 vs 312 cells). The pages (Duchy of Bavaria, Odilo, Carantania) make Carantania a vassal under Bavarian then Frankish overlordship ("about 743", "tributary to Franks: 745"), not Bavarian land. Verdicts for 750/775/783 are adjust (shape minus Carantania 749); the bavarians ledger has vassal_start 743 / vassal_end 788 with counterpart `carantania`. The carantania dossier should keep its shape through 788 or mark the vassal tint, not end it in 749.
- **Frankish suzerainty over Bavaria (eu-07).** Merovingian overlordship from c. 555, Charles Martel's "strict dependence", defeat on the Lech in 743 ("had to accept Frankish overlordship"), Pippin's ward Tassilo III from 748/749, the oath of 757, deposition at Ingelheim in 788: these are vassal_start/vassal_end events for the kingdom-of-the-franks dossier with counterpart `bavarians` (the schema gives vassal events to the suzerain). The Franks' 788 shape already contains Bavaria (487 of 488 cells).
- **Samo's Empire (eu-15) vs Avar Khaganate.** Cliopatria draws Samo from 623; the pages give Samo's arrival "c. 623-624", the Avar defeat of 626 (infobox "Defeated by Samo: 626") and the realm 631-658. The avar dossier keeps the 617 shape to 625 and takes the western Pannonian strip (205 cells) in 626. The two dossiers overlap in 623-625 until Samo's start is aligned. The same Samo shape takes 27 of the 30 cells Bavaria loses in 633 (a confidence-1 event in bavarians).
- **Kingdom of the Franks and Thuringia (eu-07).** Cliopatria's Frankish shape holds the Thuringian land in 534-566, 633-640 and from 724, but not in 567-632 nor in 720-723 (the duchy dossier ends 719). identity.successors in duchy-of-thuringia hands the land to the Franks at 719.
- **Old Great Bulgaria (ia-01), First Bulgarian Empire (eu-18).** Avar losses to them are dated 633, 656 and c. 680; the Cliopatria years 633/656/682 are within or near the pages' ranges (630-635, "mid-7th century", c. 680).
- **Kingdom of Thuringia row (476-533).** Its shape is identical to all four Duchy shapes (a cell template). 534-566 is blank in the Thuringian rows (inside the Franks' shape).

## Bavarians (540-788; 9 pages + the Samo page)

- Cliopatria begins in 540; the pages date the people "by about 520" (History of Bavaria), the duchy "c. 551/555" (Duchy of Bavaria), Garibald I from 555 (Garibald I page; the Agilolfings page says 548). The state starts in 540 (found, confidence 1) and a rename at 555 carries the first duke.
- Border changes explained only by Cliopatria shapes (confidence 1, pages silent): 546 and 555 (Alpine edge from the Ostrogothic shape), 633 loss and 661 regain (Samo's shape).
- Rulers: only the Agilolfings page's list; no duke is listed for 630-680 and Garibald I is 548 or 555.
- The Battle of Aguntum (c. 610) page would not load (https://en.wikipedia.org/wiki/Battle_of_Aguntum). Not verified for budget: Charles Martel's campaigns of 725/728, the Lombard border at Trentino/Bolzano, the Pustertal.
- One page over the nine: the Samo page, opened for the Avar dossier, is the source of the 633/661 events.

## Avar Khaganate (561-805; 8 pages)

- Corrections: 569/577 (Sirmium was Byzantine until c. 581/582, Cliopatria holds it from 569), 623 and 626 (Cliopatria drops 444 cells in 623 although the pages show Avar strength to 626; the 617 shape is kept and the Samo strip is taken in 626), 793 (Cliopatria's Frankish gain is dated 793, the pages 796), 804 (Transylvania to Bulgaria). New keyframes: 582, 796, 804.
- Open doubts: (1) the Avar shape keeps the Dniester-Dnieper steppe to 655 while the Old Great Bulgaria page puts Kubrat's state "between the Dniester and lower Volga" from 632; (2) the 28-cell Macedonian exclave of 682-740 may be Kuber's revolted Bulgars (First Bulgarian Empire page, undated); (3) the 741 gain (Slavonia) and the 800 gain (Danube-Tisza) are Cliopatria-only; (4) 627 losses to "nobody" stand for the Croats, Serbs and other Slavs, who have no Cliopatria row.
- Capitals: no page names the khagan's seat; both entries are shape centroids, flagged placeholders. The Avar Wars page mentions "the ring" without a place. Rulers omitted (only Baian and Theodorus are named).
- Not opened: the Seshat page (hu_avar_khaganate), the Avar March, the Siege of Constantinople (626).
- The Avar Wars page does not give 799, 803 or 805; those come from the Pannonian Avars and First Bulgarian Empire pages or are left out.
- https://en.wikipedia.org/wiki/Avar_campaigns_of_Charlemagne would not load (the article is "Avar Wars").

## Duchy of Thuringia (567-719; 4 pages + the Samo page)

- Status 531-641: Frankish supreme rule (Duchy page), Frankish dukes (Thuringi page), duchy established c. 631, Radulf's revolt 641/2 and royal title 642. Cliopatria's separate state for 567-632 is unsupported by the pages; kept (found event confidence 1) so the land is not blank. A gap-filler should decide whether 567-640 is a Frankish dependency.
- End: the Duchy page says autonomy ended "around 717-19" (Heden II 689-719); Cliopatria ends 723; the Hedan II page has Hedan rule to 741 from Würzburg. The dossier ends 719.
- Capitals: Erfurt (infobox only) to 703, Würzburg from 704 (Hedan II page); Radulf's seat was "a fortress on the Unstrut".
- Pages that would not load: https://en.wikipedia.org/wiki/Radulf_(duke_of_Thuringia) (the article is at Radulf,_King_of_Thuringia) and https://en.wikipedia.org/wiki/Kingdom_of_Thuringia.
- Not opened for budget: Sigebert III, Charles Martel, the Frankish conquest of 531 (Battle of the Unstrut River).

## Gazetteer

The specs use only names that resolve (--resolve gives 0 warnings). Names the gazetteer lacks and that a gap-filler will want: regions Pannonia, Carpathian Basin, Great Hungarian Plain (Avar heartland); places Freising, Ybbs, Augustae (Harlec), Karnburg; rivers Enns, Raba, Saale, Unstrut.
