# Review of me-06-c (sasanian-empire), 2026-10-19

Verdict: **fail**, sent back to the author. The machine copy is history/notes/phase-b/reviews/me-06-c.json.

## Mechanical
The validator gives 0 errors and 4 warnings: persis x1 and hatra x3 are slugs with no dossier yet (me-06-x has not run). `--resolve` leaves nothing unresolved. The ledger is sorted. Capitals fall inside the shapes (Istakhr in the 215 bbox, Merv in the 641 bbox). Family `persia` is in colours.json. Certainty covers 215-651 and names the treaty frontiers.

## Area
The infobox gives 3,500,000 km2 for 550. The Cliopatria shape alive in 550 (546-554) is 3,189,275 km2, ratio 1.10. The author compares it in keyframe 555.

## Spot checks
I checked 23 events on 7 pages. All of them say what their notes claim, so nothing is fabricated. Three were mis-dated, and I fixed them in place (the file re-validates):
- /ledger/49: occupation_end moved from 506-11 to 504. The Roman-Persian Wars page has 'Finally in 504, the Romans gained control ... of Amida', which also matches eastern-roman-empire.
- /ledger/72: contest_start moved from 605 to 602. The war is 602-628, and /wars/23 starts in 602.
- /ledger/94 and /ledger/95: the January month is removed. Susa was besieged from January 641 and taken 'after a siege of a couple of months'. The keyframe 641 wording is changed to match.

## Blocking findings (not applied; the author should make them)
1. **Yemen 575-601 is missing from the keyframes.** The ledger gains Yemen in 575, and the main page has 598. Keyframes 567 and 592 are marked ok, and the corrections for 577 and 587 add only Dara and Martyropolis. Add a union with the Himyarite Kingdom 577 shape from the chosen year.
2. **The Turkic wars are missing.** Add the 588-589 war (Bahram Chobin) and the Turkic-Khazar invasion of 626-629. western-gokturks has a contest 588-589 and gains from this state in 627 (Derbent, Aghvania) and 629 (Armenia), but this dossier has no mirror for them, yet it regains Armenia from the Turks in 630. Split the 626 loss between eastern-roman-empire and western-gokturks. The notes call the 588-589 war the 'Third' Perso-Turkic War; it is the First.
3. **The 611-612 occupation of Caesarea in Cappadocia is missing.** It is in eastern-roman-empire /ledger/74-75 and on the 602-628 war page.
4. **260-263 disagrees with palmyrene-empire.** Here Roman Syria stays occupied until 263, with the end at confidence 1 and counterpart roman-empire. palmyrene-empire gains Syria from this state in 260 and Edessa, Carrhae and Nisibis in 262 (confidence 3). roman-empire has no occupation events in those years.
5. **Adiabene (224-379, absorbed 379) and Gordyene (240-299) have no vassal events here**, though their own dossiers carry them. Also, Corduene is ceded twice in 299: once in /ledger/28 here and once in gordyene /ledger/15.
6. **The 523 regain of Khorasan (confidence 1) is 10 years from white-huns' 513**, which comes from the Kavad I page. Open that page. If it says 513, move the gain to 513 and mark keyframe 510 adjust.
7. **The 387 eastern loss (/ledger/41) conflicts with the neighbours.** alchon-huns takes Kabulistan from this state about 380 and Zabulistan in 484, and gives it back about 560. kidarites takes the land in 390 from kushano-sasanian-kingdom. Split the event and add the Alchon events, or explain why they are left out.

## Mismatches to route (the other side may be wrong)
- 387: the loss to roman-empire here meets a vassal_start of kingdom-of-armenia on the roman-empire side, which has no gain from this state.
- 498: Chaganiyan is lost to white-huns here (confirmed on the page), and white-huns has no gain for it (ia-01).
- 619/621: Egypt is gained in two steps here (Alexandria 619, the rest by 621, from the main page), while eastern-roman-empire loses all of Egypt in 619.
- 617: eastern-roman-empire loses Lazica and western Iberia to this state (confidence 1), and there is no mirror here.
- eastern-kushans: the contest over Gandhara starts in 240 there and in 262 here.
- kidarites still has kushano-sasanian-kingdom alive in 360 and 390. This dossier absorbs the Indo-Sasanian land in 358.

## Thin (within budget, for a gap-filler)
- Confidence-1 events: 296, 306, 387, 484, 510, 523, 545, 626, 627, 634 and 643.
- Rulers are omitted: open the List of Sasanian monarchs.
- 13 keyframes are 'unverified: page budget'. That is allowed by design.
- The 283 shape adds 241,000 km2 that nothing explains.

## Report errors
- The author lists 'Chionites' (chionites) as needing a dossier, but xionites.json already exists.
