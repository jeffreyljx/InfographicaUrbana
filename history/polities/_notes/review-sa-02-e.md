# Review of batch sa-02-e (2026-10-19)

Dossiers: kalabhra-dynasty, kamarupa-kingdom, maitraka-dynasty.
Neighbour dossiers read (Context list, existing): gupta-empire, vakataka-kingdom, white-huns, western-satraps. Also read because they name this batch's states: late-pallava-empire, alchon-huns, early-cholas, early-pandyas, early-cheras. Not written yet (exception: group not run yet): pala-empire, tibetans, tibetan-empire, chalukya-dynasty, harsha-s-empire, sena-dynasty, maukhari-dynasty, khadga-dynasty, pandya-dynasty, gauda-kingdom, umayyad-caliphate, gurjara-pratihara-dynasty.

Validator (--resolve): 0 errors in all three, before and after the reviewer's edits. Warnings: kamarupa /ledger/3 `davaka`, /identity/successors/2 place `Sadiya`; maitraka /ledger/7 and /9 `nandipuri-gurjaras` (all listed by the author).

Pages opened by the reviewer: Kamarupa (three reads), Pala dynasty (Kamarupa), Pala Empire, Maitraka dynasty, Caliphate campaigns in India, Kalabhra dynasty, Pandya dynasty. Every spot-checked event says what its note claims; no fabricated or mis-dated event. None of the three pages has an infobox area (checked).

Verdicts: kalabhra-dynasty fix (fixed by the reviewer); kamarupa-kingdom fail; maitraka-dynasty fail.

## kalabhra-dynasty: fix (reviewer applied)

Applied by the reviewer (re-validated):
- /keyframe_review/0 and new /keyframe_review/1. The 353 keyframe was `ok` for 353-591, but /ledger/1 gives 81 of its 520 cells to the Late Pallavas in 575 and late-pallava-empire /keyframe_review/6 draws those cells from 575: 81 cells double-drawn for 17 years. Now: keyframe 0 `adjust` (353 shape, 353-574 only); new keyframe `kalabhra-dynasty_575` (575-591) = Kalabhra 353 minus (Late Pallava 602 minus 555), 439 cells. Kalabhra page: "Simhavishnu consolidated his kingdom from south of the Krishna river and up to the Kaveri river by c. 575 CE."

Not applied, non-blocking:
- Start 353 vs predecessors: early-cholas /ledger/2, early-pandyas /ledger/1, early-cheras /ledger/2 dissolve into kalabhra-dynasty in 305, so the Tamil country is drawn by nobody 305-352. The page's infobox gives "Established: 3rd century CE". Suggest starting in 305 (found at confidence 1, keyframe 305-352 = the 353 shape), or say in notes which side moves.

Thin (by design, 2 of 2 pages): /ledger/0 (353, Cliopatria), /ledger/2 (592, Cliopatria; Kadungon c. 560-590), /ledger/3 (601, Cliopatria). Pages to try: Simhavishnu, Kadungon, Achyuta Vikranta.

Spot checks: /ledger/0, /1, /3 on Kalabhra dynasty; /2 on Pandya dynasty: all confirmed as the notes say.

## kamarupa-kingdom: fail

Blocking, not applied:
1. /ledger (missing vassal_start / vassal_end, counterpart pala-empire). The Pala Empire page the author opened says the king of Pragjyotisha "submitted without giving a fight" and "accepted the suzerainty of Devapala" (c. 810-850), and "Narayanapala lost control of Assam and Orissa" (854-908 Majumdar). The dossier keeps this only as /wars/4 with empty zones and routes the relation to pala-empire. Rule 3 needs it in both ledgers (sa-02-d failed vakataka and yaudheya for the same). Add vassal_start c. 810 and vassal_end c. 855-860, confidence 1-2, source Pala_Empire.

Applied by the reviewer (re-validated):
- /ledger/16, /ledger/17: the 960 gain named `tibetan-empire`, whose row ended in 849. 75 of the 190 cells lie in the Tibetans 959 shape (none in its 960 shape), so /ledger/16 is now those 75 cells from `tibetans`, and /ledger/17 (nobody) subtracts the Tibetans 959 shape instead (460 cells).
- /ledger/13 note: the quote "was elected as king by the ruling chieftains" after Tyagasimha is on the Kamarupa page, not the cited Pala dynasty (Kamarupa) page (which has only "Established: 900 CE" and "the first ruler ... was elected"). The note now says so; the year and confidence 3 stand.

Not applied, non-blocking:
- /ledger/9 (656 loss, nobody): 33 of 163 cells lie in the Tibetan Empire 656 shape; split off a loss to tibetan-empire for them.
- /ledger/0 (350 found, gupta-empire): the 150 km Guwahati core overlaps the Gupta 347 shape by 87 cells while gupta-empire /ledger/9 releases them only in 353. The Kamarupa side is page-sourced ("Established: 350"; "began as a subordinate but sovereign ally of the Gupta Empire around present-day Guwahati in the 4th century"): routed to gupta-empire to move its loss to 350. Optionally record the "subordinate ally" relation as a vassal pair here.
- /ledger/6 (637 gain from gauda-kingdom): Cliopatria's Gauda row is 602-611; the sa-03 Gauda dossier must run to 636/637, or the counterpart changes.

Thin (by design, 9 of 9 pages; 12 shapes "unverified: page budget"): the confidence-1 jumps at 656, 751, 960, 1056 and 1072. Pages to try: Salasthambha, Yashovarman, Ratna Pala, Dharma Pala (Kamarupa), Vijaya Sena, History of Assam.

Spot checks (all confirmed): /ledger/0, /3, /4, /7, /15, /18 on Kamarupa; /13, /23, /24 on Pala dynasty (Kamarupa); Devapala, Narayanapala, Ramapala and Vaidyadeva on Pala Empire. Kept as one state across Varman, Mlechchha and Pala dynasties (renames 655, 900): accepted.

## maitraka-dynasty: fail

Blocking, not applied:
1. /ledger (missing vassal_start / vassal_end, counterpart harsha-s-empire). Maitraka dynasty page: "They came under the rule of Harsa of Vardhana dynasty in the mid-seventh century", keeping local autonomy and regaining independence after Harsha's death; Dhruvasena II "married the daughter of Harsavardhana" (640-643 on the Vallabhi list). Routed only to harsha-s-empire. Add vassal_start c. 640 (confidence 1-2) and vassal_end 647 (Harsha's death).

Not applied, non-blocking:
- /ledger/4 (616 Ujjain from nobody): all 134 cells of the Ujjain circle lie in Cliopatria's Harsha's Empire shapes of 615-640 (0 in 655). Say so in the note; harsha-s-empire (sa-03) should not draw Ujjain directly while the Maitrakas hold it (the Virdi grant of 616 is confirmed).
- /ledger/2 (555 gain from vakataka-kingdom): the vakataka-kingdom dossier ends in 510 (dissolve to kalachuris-of-mahishmati and others). Name the 554 holder per the dossiers (kalachuris-of-mahishmati, or nobody).
- /ledger/6 (724 loss of Ujjain to gurjara-pratihara-dynasty, confidence 1): the Caliphate page dates Nagabhata's victory over the "Valacha Mlecchas" to around 725 but gives "no authentic information about where precisely he encountered them" and says Junayd did not take Ujjain; Cliopatria's Gurjara-Pratihara row starts in 732. Either move to 732 or make sure the G-P dossier starts by 724.
- /keyframe_review/0: the note says the full 476 shape holds from 475, but /ledger/0 founds on Saurashtra alone in 475; say 476-533.

Thin: north Gujarat only from Dharasena III (626-640), not subtracted; the Alchon hold on Gujarat 500-515 (alchon-huns /ledger/9 and /12 cover 609 of the 617 Maitraka 476 cells but name gupta-empire: routed to ia-01); the end of the Nandipuri relation; the Arab-invasion end. Pages to try: Sanjeli inscription, Nagabhata I, Gurjaras of Lata, Dharasena III.

Spot checks (all confirmed): /ledger/0, /4, /10 on Maitraka dynasty; /5, /7, /8 on Caliphate campaigns in India; /6 quotes confirmed, transfer inferred as the note says. The 656-731 correction (Gujarat core plus Ujjain instead of Cliopatria's Rajasthan and Madhya Pradesh) is consistent with every page read.

## Cross-dossier matrix (summary; the JSON report has every row)

- Matched: kalabhra 575 loss / late-pallava 575 gain; kamarupa 353 gain / gupta 353 loss; maitraka 475 found and 476 gain / gupta 476 loss.
- Mismatch: kalabhra 353 start / early-cholas, early-pandyas, early-cheras 305 dissolve; kamarupa 350 found / gupta 353 loss; kamarupa 656 loss nobody / tibetan-empire 656 shape (33 cells); maitraka 555 gain / vakataka ends 510; maitraka 616 gain nobody / Harsha's Empire shape; alchon-huns 500-515 Gujarat named gupta-empire / maitraka holds it.
- Missing on both sides: kamarupa-pala-empire vassal (c. 810-855); maitraka-harsha-s-empire vassal (c. 640-647).
- Exceptions (counterpart not written yet or no dossier listed): pandya-dynasty, davaka, gauda-kingdom, tibetans, pala-empire, sena-dynasty, umayyad-caliphate, gurjara-pratihara-dynasty, nandipuri-gurjaras.
