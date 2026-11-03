# Review of batch eu-06-f (bavarians, avar-khaganate, duchy-of-thuringia)

Reviewer, 2026-10-20. Machine copy: history/notes/phase-b/reviews/eu-06-f.json. All three dossiers validate with 0 errors and 0 warnings (--resolve), before and after the reviewer's edits. Verdicts: **fix** for all three. No fabricated or mis-dated confidence-3 event was found: 23 events and fields were checked against 11 pages, and every quote is on its page.

## Edits applied by the reviewer (re-validated)

- avar-khaganate /ledger/2: the 568 gain from the Lombards now leaves out Sirmium (`minus` place Sirmium 30 km). This matches the dossier's own 569/577 corrections and the ERE's 567 gain.
- avar-khaganate /ledger/10, /ledger/13, /ledger/15: confidence 2 -> 1. The page gives no year for these events (627 Balkan collapse, 'mid-7th century' Bulgar expansion, the Slav return after 658/665), and the notes already say 'the year is Cliopatria's'.
- avar-khaganate /wars/7/to: 796 -> 803 (Avar Wars infobox 'Date: 788 to 803').
- bavarians rulers 1-8: added the source https://en.wikipedia.org/wiki/Agilolfings (the dates match the page).
- duchy-of-thuringia rulers 1-3: added the source https://en.wikipedia.org/wiki/Duchy_of_Thuringia (they match the ducal list).

## Open fixes for the authors (non-blocking)

### bavarians
1. **/identity/predecessors is empty**, yet all 310 cells of bavarians_540 lie in Cliopatria's Ostrogothic Kingdom shape of 539. Neither dossier records this 76,734 km2 hand-over. Add ostrogothic-kingdom as predecessor (land = intersect Ostrogothic 539 / Bavarians 540) and find a page that dates the Gothic loss of Raetia and Noricum. eu-06-e should add the matching 540 loss.
2. **/ledger/1 (546 gain from lombards)**: the lombards dossier records 546 as a loss to nobody (Rugiland), and only 2 of the 5 cells were Lombard. Set the counterpart to nobody, or drop the event as Cliopatria noise.
3. **/ledger/3 (555 gain from ostrogothic-kingdom)**: no matching loss in ostrogothic-kingdom, whose 555 loss is Pavia to the ERE. Route this to the eu-06-e rework.

### avar-khaganate
4. **/ledger/4**: the ERE records Singidunum and Viminacium lost to the Avars in 583 (c3) and regained in 588. This dossier records only a contest. Add a 583 gain and a 588 loss using ERE's region, or agree with eu-05 to drop both sides.
5. **/ledger/8-9**: Thrace in 626 is a contest here but an Avar occupation in the ERE. Make the two dossiers use the same event type.
6. **/ledger/5**: this contest ends in 602, while the ERE contest runs without a break from 582 to August 626. Reconcile the two.
7. **/ledger/10**: 99 of the 103 cells are the Naissus-Serdica interior, which the ERE corrects out of 623-625 ('no page returns them'). The ERE has no gain from the Avars. Use counterpart nobody, or add a matching ERE gain.
8. **/keyframe_review/17**: the 682 shape adds a 28-cell exclave in Macedonia with no ledger event, and it disappears in 741 with none either (Kuber's Bulgars?). Either mark 682 and 741 adjust and correct the exclave out, or add c1 events.

### duchy-of-thuringia
9. **/identity/predecessors**: kingdom-of-thuringia hands its land to the Franks in 532, and 173 of the duchy's 174 cells were Frankish in 566. Add kingdom-of-the-franks as predecessor.

## Thin (gap-filler)

- bavarians: found 540 and the 546/555/633/661 edge moves are confidence 1. The 788 end of the Carantanian overlordship is a bridging judgement. Missing: Tassilo I's Slav wars and Aguntum (c. 610), the Adige-valley border, and Charles Martel's 725/728 campaigns. All of this is within the 9-page budget, so it is thin by design.
- avar-khaganate: the 656 loss of the Dniester-Dnieper steppe to nobody (about 413,000 km2, c1) is the largest land move. Whether the Avars held that steppe at all in 568-655 is doubtful (the Old Great Bulgaria page has Great Bulgaria 'between the Dniester and lower Volga'). Other gaps: the 741 Slavonia gain, the 800 regain, placeholder capitals, and no rulers.
- duchy-of-thuringia: Cliopatria's 567-630 own-state span is unsupported, since the duchy was set up 'about 631' under Frankish supreme rule. The 633-640 years leave the duchy without land while Radulf rules. The end comes c. 719, but the Hedan II page has his rule running to 741. Saxon rule over parts of Thuringia is not drawn.

## Cross-dossier (see the JSON matrix)

These pairs match: Gepids 567, Lombards 568, ERE 561/582/583-contest/615, OGB 633/656. Exceptions: counterparts not written yet (kingdom-of-the-franks, samo-s-empire, carantania, first-bulgarian-empire), or nobody. Mismatches: ERE 583/588, 602, 626 occupation, 627; Lombards 546; Ostrogoths 540 and 555.

## Area

None of the three state articles (Duchy of Bavaria, Pannonian Avars, Duchy of Thuringia) has an infobox area. The areas the authors quote match shapes.csv.
