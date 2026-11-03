# Review: batch eu-07-b (kingdom-of-the-franks)

Reviewed 2026-10-25 by the Phase B adversarial reviewer. Machine copy: history/notes/phase-b/reviews/eu-07-b.json.

## Verdict: fix (fixed by the reviewer)

Validator: 0 errors, 0 warnings before and after the reviewer's edits (`--resolve`, 388 regions). 63 keyframes (4 wrong, 36 adjust, 23 ok), 100 events, 24 wars, 14 sources. Page budget for 50 shapes: 14 pages, all spent.

### Applied by the reviewer (verified on the page)

- /ledger/8, Provence: 537 -> 536 (confidence 3). Chlothar I page: "In 536 Vitiges, the new king offered Provence and Rhaetia in exchange for military help, which the Franks agreed to." The page's only 537 is the outbreak of the Roman-Ostrogothic conflict; the keyframe note had put "537:" inside the quotation. Keyframe kingdom-of-the-franks_537 is now kingdom-of-the-franks_536 (536-539), keyframe 534 is valid 534-535, keyframe 540 note and the notes field updated. Now matches ostrogothic-kingdom's 536 loss.
- /ledger/45, War of Aquitaine opening: 763 -> 760 (confidence 3). Pepin the Short page: "In 760, after conquering the Roussillon from the defeated Muslims and denouncing Waiofar's actions, ...". /wars/13 from 760; notes 763-768 -> 760-768. Now matches the aquitaine dossier.

### Not applied (non-blocking; routed)

1. Q146246. merovingian-empire.json (Merovingian Empire 710-717, Carolingian Empire 718-723: one 32,241 km2 Provence outline) draws Provence as a separate state, and this dossier draws it too (keyframes 705 and 718): a double cover 710-723, and that file's found 710 and dissolve 723 have no mirror here. The brief's rule puts both Names here. This is the orchestrator's decision: add both Names to cliopatria_names with keyframes merovingian-empire_710 and carolingian-empire_718 as wrong (duplicate), and retire merovingian-empire.json in the same step.
2. Alamannia. /ledger/38 gains it in 732 (confidence 1); kingdom-of-alamannia keeps it to 746 (Cannstatt, confidence 3): double cover 732-746. Your keyframe 741 quotes the 741 division ("to Carloman he gave Austrasia, Alemannia, and Thuringia"), so the likely outcome is a Frankish vassalage 732-746 in the alamannia dossier, with /ledger/38 raised to confidence 2.
3. Thuringia. /ledger/33 regains it in 724 (confidence 1); duchy-of-thuringia dissolves into this state in 719 (confidence 2). Nobody draws Thuringia 719-723. Move to 719 and union it into keyframe 718, or the duchy owner extends.
4. Frisia. /ledger/28 loss 718 (confidence 1) vs magna-frisia gain 714 (confidence 2); /ledger/26 gain 692 vs magna-frisia loss 689; /ledger/73 gain 788 vs frisia loss and dissolve 785 (confidence 3).
5. Events neighbours give that have no mirror here: aquitaine contest 735-736 (confidence 2); breton-kingdoms occupation 819-822 (confidence 2; /wars/20 dates the campaign 818 with no zone); carantania vassal_start 788 and vassal_end plus dissolve 828 (confidence 3); frankish-burgundy gain 595 (declined here for want of a page) and loss 610 (confidence 3); obotrites loss 814 (confidence 3).
6. /ledger/2: the 511 capital_move changes no capital (Paris stays 509-799). Drop it or fold it into the capital note.

### Thin (for a gap-filler)

- 37 events at confidence 1 (list in the author's notes). Spanish March, March of Pannonia, Odo the Great/Hunald, Lantfrid/Theudebald, Tassilo and Radulf pages were not opened.
- /ledger/7: the 534 Alpine-cells gain could be 536 at confidence 2 ("Provence and Rhaetia", Chlothar I page).
- Ruler strip gaps: 511-558, 561-613, 639-687, 714-718. Aachen as capital from 800 is a bridge (confidence 1).

### Spot checks (8 events, 4 pages)

| where | page | result |
| --- | --- | --- |
| /ledger/3 Thuringia 532 | Francia | confirmed |
| /ledger/15 Basques 602 | Francia | confirmed |
| /ledger/8 Provence | Chlothar I | mis-dated 537, page 536: fixed |
| /ledger/9 Saxon tribute 555 | Chlothar I | confirmed |
| /ledger/45 Aquitaine war | Pepin the Short | mis-dated 763, page 760: fixed (759 Narbonne confirmed) |
| /ledger/53 Lombards 774 | Charlemagne | confirmed |
| /ledger/69 Benevento 786 | Charlemagne | confirmed |
| /ledger/72 Bavaria 788 | Charlemagne | confirmed |

Two of the confidence-3 events checked were mis-dated. The author often puts a year inside a quotation ("'537: When the Ostrogoths...'"), which makes the year look like the page's own. Re-check the other confidence-3 years against the sentence each one quotes.

### Area

Francia infobox: "814 (peak): 1,200,000 km2". Cliopatria's 814-824 shape is 1,301,581 km2, a ratio of 0.92. The author acknowledged this in keyframes 806 and 814.

### What held

- The keyframe walk is thorough. Every shape change is given its own Cliopatria intersections: Neustria put back 724-731, Aquitaine cut 732-749, the Avar land out 793-795, and the 840 shape cut at Verdun.
- Found 509 and dissolve 843 (month 8) are in place, and the capitals run without a gap.
- The family france exists.
- The Saxon swings (775, 778, 779, 782, 785, 793, 794) match the saxons dossier year by year.
- The Verdun splits match west-franks, middle-franks and east-franks.

## Cross-dossier matrix (summary)

Matched: salian-franks 509; kingdom-of-thuringia 532; burgundian-kingdom 532-534; ostrogothic-kingdom 536 (after the fix); frankish-burgundy 561, 599/600, 612, 613, 639, 660/661; aquitaine 629, 632, 731-732, 760-768 (after the fix); duchy-of-thuringia 633, 641; magna-frisia 719, 734; kingdom-of-neustria 717-724; saxons 772-794; bavarians 788; avar-khaganate 791, 796, 800; frisians 793, 799/800; the three Verdun successors 843.

Mismatched or missing on the other side:
- ripuarian-franks 509 names salian-franks as its counterpart.
- saxons: the vassalage 555-556 is a contest there, and 738 is missing.
- eastern-roman-empire has no 561 gain.
- duchy-of-thuringia: no vassal_start 567, and it ends in 719 where this dossier has 724.
- kingdom-of-alamannia: nothing for 724 or 730-732, and it ends in 746.
- umayyad-caliphate: nothing for 739. The 755 gain falls after that dossier's 750 end.
- magna-frisia: 689/714 against 692/718 here, and nothing for 772.
- aquitaine: books a gain in 781 where this dossier has a vassal_start, and has no 843 vassal_end.
- frisia: 783 names magna-frisia, and the end is 785 against 788 here.
- obotrites: books the 804 gain from saxons.

Before 509, burgundian-kingdom, kingdom-of-soissons, visigothic-kingdom and western-roman-empire name kingdom-of-the-franks, which does not exist yet. They should name salian-franks.

Exceptions: counterparts owned by groups that have not run: eu-12, eu-13, eu-10, eu-14, eu-15, eu-18, and frisia-kingdom (eu-06).
