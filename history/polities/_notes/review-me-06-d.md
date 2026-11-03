# Review of batch me-06-d (indo-sasanian-empire, lakhmid-kingdom, ghassanids)

Reviewer, 2026-10-19. Machine copy: history/notes/phase-b/reviews/me-06-d.json.

Mechanical: all three validate with --resolve, 0 errors, 0 warnings (before and after the reviewer's edits). File names, Cliopatria rows (4, 8 and 6 shapes) and verdicts, families (persia, near-east), year order, found/dissolve years, capitals (Balkh and al-Hira inside their shapes; Jabiyah outside, acknowledged) checked. No infobox gives an area (confirmed on each page), so there is no area ratio; the notes say so.

Spot checks (WebFetch): 6 + 5 + 6 events, including both confidence-3 events (Lakhmid 602 loss and dissolve). Nothing fabricated: every quoted phrase checked was on its page. One event cited a page that does not date it (Ghassanid 636 contest_end, fixed).

## Verdicts: all three FAIL, on one blocking gap

None of the three ledgers holds a vassal event, though all three are client states and the overlords' dossiers already record the relation. Same finding as me-06-b's fails for Adiabene, Gordyene and Osroene.

- indo-sasanian-empire: Kushan Empire page, "replaced them with Persian vassals known as the Kushanshas", "from around AD 240". The mirrors are sasanian-empire /ledger/23 (vassal_start 260) and /ledger/39 (vassal_end 358). Add vassal_start 260 (counterpart sasanian-empire, region the 260 shape, confidence 2) and vassal_end 360 with the dissolve over the north. Then ask me-06-c to end its tint in 360 over the north, or both dossiers use 358.
- lakhmid-kingdom: Lakhmid page, infobox "Status: Dependency of the Sasanian Empire"; text "The Lakhmids functioned as a client state of the Sasanian Empire". The mirrors are sasanian-empire /ledger/31 (270) and /ledger/84 (602). Add vassal_start 270 and vassal_end 602.
- ghassanids: Ghassanids page, infobox "Status: Vassal of the Eastern Roman Empire"; text "They became clients of the Roman Empire". The mirrors are eastern-roman-empire /ledger/20 (473), /ledger/77 (vassal_end 613) and /ledger/97 (vassal_start 629), and byzantine-empire /ledger/1 (vassal_end 633). Add vassal_start 510 (ERE), a vassal_end with the 617 loss (agree 613 or 617 with eu-05), vassal_start 629 (ERE), the hand-over in 632/633 to byzantine-empire, and vassal_end 636 with the loss.

## Fixed by the reviewer (re-validated, 0 errors 0 warnings)

- indo-sasanian-empire /wars/0: from 241 to 260 (life starts 260); /wars/3: to 370 to 360 (life ends 360). Each has a note.
- lakhmid-kingdom /wars/3: to 611 to 602 (Dhi Qar falls after the end), with a note.
- ghassanids /ledger/7: the source was Muslim_conquest_of_the_Levant, whose text gives no year for the Yarmuk. It is now Battle_of_the_Yarmuk (infobox "15–20 August 636"), added to sources[], and the note is corrected. The /ledger/8 note now names that page for the year.

## Other fixes for the author (not blocking)

- lakhmid-kingdom /ledger/0: the found region (Kufa, 150 km) is 156 Sasanian cells and only 114 Lakhmid cells. Intersect it with {cliopatria: Lakhmid Kingdom, year: 270}.
- ghassanids /ledger/1 note: eastern-roman-empire does not record the 54 cells as a ledger loss. They appear only in its /keyframe_review/14 note.
- ghassanids /keyframe_review/2 note: the page says the confederation was restored "After two or three years", not "a few years later" (undated).
- ghassanids /ledger/2 note: delete "withdrawing to Anatolia (undated)". The page's withdrawal is Jabala's, in 639.
- ghassanids /identity/rulers: gaps 583-587 and 591-632. Close them or say why not.
- ghassanids capital: Jabiyah (Golan) lies outside every keyframe. This is acknowledged; an adjust keyframe adding the Golan/Hauran seat would be better, but it is optional.

## Thin (confidence 1; gap-filler)

- indo-sasanian-empire /ledger/0 and /ledger/1: dated only to Cliopatria's 260.
- indo-sasanian-empire: the c. 325 "southern part" under Shapur II is not located.
- lakhmid-kingdom /ledger/0: found 270, dated only to Cliopatria's year.
- lakhmid-kingdom: undated claims (Imru' al-Qays I, Najd before 521).
- ghassanids /ledger/0-5: 510, 617 and 629 are all Cliopatria's years. The whole state vanishes for 617-628 on Cliopatria's word.
- ghassanids: the 582-c.585 break-up is not drawn.

## Cross-dossier, to route

- sasanian-empire (me-06-c):
  - The 990 Lakhmid cells of 629-633 are in no dossier. Add them to the 629-633 keyframes, with a loss to rashidun-caliphate in May 633.
  - 617: add a gain from ghassanids. /ledger/93 shares 0 cells with the Ghassanid loss.
  - 629: /ledger/102 loses the 550 Ghassanid cells to eastern-roman-empire. They should go to ghassanids.
  - No contest 350-358 with indo-sasanian-empire.
  - Vassal_end 358, against this dossier's 360.
- kidarites: /ledger/1 and the predecessors use the slug kushano-sasanian-kingdom; it should be indo-sasanian-empire. /ledger/4 (390) names the same slug for land that is Sasanian from 358.
- eastern-roman-empire / byzantine-empire (eu-05):
  - No 510 ledger loss to ghassanids.
  - Vassal_end 613, against the 617 loss here.
  - byzantine-empire's vassal_end 633 should be 636, with a vassal_start at the 633 hand-over.
- himyarite-kingdom: optional mirror of the 521 Najd contest.
- rashidun-caliphate (me-07, not run): the 634-636 contest and the 636 loss of the Ghassanid country.
