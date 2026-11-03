# Review ia-01-d (2026-10-18): western-gokturks, khazaria, old-great-bulgaria

Reviewer: adversarial review, Phase B. The machine copy is history/notes/phase-b/reviews/ia-01-d.json.

Mechanical: all three files validate with --resolve. The one warning is western-gokturks /ledger/20 (tokhara-yabghus, a listed new state). Neighbour dossiers present: eastern-gokturks and eastern-roman-empire, plus gokturk-khaganate as predecessor; the Tang is checked against _example-tang-dynasty.json. The other Context polities are not written yet. Overlaps were computed with tools/gazetteer.py on H3 r5 cells (about 250-275 km2 per cell).

## western-gokturks: fail

Blocking:

1. **/keyframe_review/11 and /12 corrections overlap Khazaria 647-657.** The corrections put back the 644 shape to 657. That shape holds 114 cells (about 31,000 km2; 96 in the Kazakh Steppe) which Cliopatria hands to the Khazars in 647: khazaria's 647 shape takes them out of Cliopatria's Western Göktürks 646 shape. Both dossiers draw them for 647-657, and neither has the handover. Fix: add `{"cliopatria": "Khazaria", "year": 647}` to the minus of both corrections. Then add a 647 loss, cp khazaria, region `intersect[{"cliopatria": "Western Göktürks", "year": 646}, {"cliopatria": "Khazaria", "year": 647}]`, at confidence 1 (Cliopatria's year). The khazaria dossier gets the mirror gain.
2. **Tokharistan (added from 625, /keyframe_review/3 to /12) overlaps other Cliopatria states, and nothing says so.** The added `intersect[Bactria, Afghanistan]` is 375 cells. Of these, 305 lie in Karkota Dynasty 626-655, 34 in Turk Shahis 561-643, 320 in Turk Shahis 644-665 and 19 in Rashidun 644. The addition itself is right: Tokhara Yabghus, 'In 625, Tong Yabgu invaded Tokharistan and forced the Hephthalite principalities to submit'. A Kashmir dynasty in Balkh and Samangan is probably a Cliopatria error. Fix: write this in the K3-K12 notes and in the dossier notes so that sa-03 removes those cells (or subtract them and name the Turk Shahis as counterpart), and list the routing.

Applied by the reviewer:

- /ledger/10 (627 vassal_start of the Onogur Bulgars): confidence 2 to 1. The note already says the start year is Cliopatria's, and the Tong Yabghu page gives no year.

Advisory (not blocking):

- /ledger/9, /12 (khazaria) and /ledger/10, /13 (old-great-bulgaria): these vassal pairs name states whose dossiers begin in 630 and 633, so no mirror can exist. Write string counterparts ('Khazar tribes (before the khaganate)', 'Onogur Bulgars (before Kubrat's state)'), or say in the notes why the slugs stay.
- /ledger/23: the dissolve region is Cliopatria's 656 shape (1.27 M km2), not the corrected K12 shape. Use the K12 correction.

Spot checks, all confirmed:

- /ledger/7: 625 Tokharistan, confidence 3 holds.
- /ledger/2 and /3: 588-589, Balkh, Talaqan, Badghis and Herat.
- /ledger/8: 'Early in 627 ... stormed Derbent and swarmed over Aghvania'.
- /ledger/18: Karasahr fell in 648; Kucha 19 January 649.
- /ledger/19: Su Dingfang beat Helu in 657.
- /ledger/11: Armenia is undated on the WTK page, so confidence 1 is honest.

Area: infobox 3,500,000 km2 (630) against the Cliopatria 630 shape of 3,854,580 km2, ratio 1.10; acknowledged in K7.

Thin, with pages to try:

- 587 Gaochang client status: Gaochang page.
- 602 Tarim vassalage: Kucha page.
- 627 Bulgar client status: Kubrat page.
- 629 Armenia: Third Perso-Turkic War page, which has April 630.
- 630 Derbent to the Khazars: Derbent page.
- Sogdia, Chach and Ferghana after 657: Protectorate General to Pacify the West page.
- The steppe west of the Irtysh after 657: Ashina Buzhen page.

Cross-dossier:

- gokturk-khaganate's 586 split matches the 587 found.
- khazaria's 630 Dagestan gain matches the 630 loss.
- The Tang example matches 640, 648 and 657. But its tang-dynasty_656 keyframe keeps Cliopatria's 656 shape 'as drawn' for 656-660, which holds 2,432 cells of the corrected Western Turk 656-657 shape. ea-04 should begin Dzungaria and Semirechye in 657.
- eastern-gokturks has no contest for 599-603: for ia-01-c, not required.

## khazaria: fail (one paired fix)

Blocking:

1. **/ledger/3 (647 gain, cp nobody).** 114 of the 532 cells lie in Cliopatria's Western Göktürks 646 shape, and the K3 note counts them. Those cells come from western-gokturks, so the counterpart cannot be nobody. Fix: split the event into a 647 gain cp western-gokturks of `intersect[{"cliopatria": "Khazaria", "year": 647}, {"cliopatria": "Western Göktürks", "year": 646}]` (confidence 1) and a 647 gain cp nobody of the remainder. This is the mirror of the western-gokturks fix 1. Nothing else blocks.

Spot checks, all confirmed:

- /ledger/2: Derbent 642.
- /ledger/4: 'c. 642 – c. 652', Balanjar 652; confidence 3 holds.
- /ledger/5: 668, with 'around 670' on the Khazars page.
- /ledger/7 and /9: 'c. 722 – c. 737', Balanjar stormed 21 August 722.
- /ledger/12: 'Sarkel fell in 965'.
- /ledger/13 and /11: the infobox 'Vassals of the Khazars (late 9th century-969)'.

Area: infobox 3,000,000 km2 (850 est.) against 749,503 km2, ratio 0.25; acknowledged in K17 as the tributary belt. Infobox 1,000,000 km2 (900) against 749,635 km2, ratio 0.75.

Other checks:

- The 668 gain matches old-great-bulgaria's 668 loss: 981 cells in common.
- The 682 gain from nobody is verified: none of its cells is in the OGB, Avar or Volga Bulgaria shapes.
- The new keyframes khazaria_668 and khazaria_965 have no overlap with neighbours alive then, apart from 26 Byzantine cells in the Crimea.

Thin, with pages to try:

- The 630, 647, 682 and 890 events are at confidence 1.
- No vassal events for the tributaries behind the 3.0 M km2 figure: Magyars, Severians, Radimichs, Vyatichi, Polans, Burtas. Page: Levedia.
- No dated loss of the Pontic steppe to the Pechenegs (889-896). Page: Etelköz.
- The 799 raid is missing from wars.
- Crimean Gothia and Cherson have no events.
- The Samandar placeholder point lies 15-30 km outside the 723 shape.

## old-great-bulgaria: fix (all applied by the reviewer)

Applied:

- /ledger/1 (656 gain from the Avars): confidence 2 to 1. The page says 'In the mid-7th century'; 656 is Cliopatria's year.
- /wars/0 (Kubrat's revolt): from 630 to 633, so the war lies inside the life.
- /wars/1 (Khazar conquest): to 670 to 668, the state's end. Khazaria keeps 668-670 in its own copy.
- /identity/capitals/0: moved from the Tmutarakan placeholder (36.72 E, 45.22 N), 15-30 km outside the 633 shape, to the Phanagoria page's coordinates (36.97 E, 45.28 N). That page says 'capital of Old Great Bulgaria between 632 and 665 under Kubrat'; it is now the capital's source and is added to sources[].

The file revalidates clean.

Spot checks:

- /ledger/0: confirmed, 'Between 630 and 635'.
- /ledger/1: the event is confirmed, but the year is not on the page.
- /ledger/2: confirmed, Asparukh in 668.
- /ledger/3: confirmed, 668.

Area: the infobox gives none.

Open, routed to eu-18: first-bulgarian-empire must take the 674-681 Dniester-Danube shape as a prelude keyframe, and found no later than 674, or that land is stateless.
