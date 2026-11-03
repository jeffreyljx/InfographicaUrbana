# Review of batch eu-22-g (reviewer, 2026-11-01; brief filled 2026-10-31)

Dossiers: russian-federation, russian-occupied-territories, serbia-montenegro, slovakia, ukraine, british-overseas-territories. The validator (--resolve) gives 0 errors for all six and no unresolved region. Warnings: open occupation_start/contest_start events run to the end of the data (5 in russian-federation, 3 in ukraine), which is acceptable.

Pages I opened: First Chechen War, Second Chechen War, Russo-Ukrainian war, Russian annexation of Donetsk/Kherson/Luhansk/Zaporizhzhia oblasts, Russian-occupied territories, Annexation of Crimea, Serbia and Montenegro, Dissolution of Czechoslovakia, Ukraine, Russia, British Overseas Territories, Slovakia. Every date I spot-checked is on its page. I found no fabricated event.

Verdicts: russian-federation **fail**, ukraine **fail**, russian-occupied-territories **fail**, serbia-montenegro **pass**, slovakia **pass**, british-overseas-territories **fix** (one finding that does not block, not applied).

## russian-federation (fail)
- /keyframe_review/7: the 2024 correction is the 2013 outline, yet /ledger/14-15 make the LPR and DPR lands solid Russian gains in 2022-9, and nothing removes them later. As written, the 2024 frame draws the Donbas only as Ukraine's solid. The orchestrator must choose one treatment: either retype /ledger/14-15 as occupation_start (counterpart ukraine), the same as Crimea, or add those regions to the K7 correction.
- /ledger/13: a loss of the whole of Kharkiv Oblast (about 34,100 km2, including Kharkiv city) in 2022-9, but Russia never held the oblast in the ledger. The page says 'recaptured the majority of Kharkiv Oblast in September'. Fix: add a 2022-2 occupation_start for the occupied east of the oblast and make /ledger/13 its occupation_end.
- Missing events: the occupation north of Kyiv, February to early April 2022 (war page: 'After the Russian withdrawal from areas north of Kyiv').
- /ledger/16: the Kherson event of November 2022 ends an occupation (/ledger/12), so it should be typed occupation_end, not loss.
- /ledger/17 (and ukraine /ledger/14): the Kursk zone is the whole oblast (about 31,100 km2) for 'up to 350 square kilometres'. Narrow it to a circle around Sudzha.
- /ledger/10: does not match georgia. Georgia records the Gori/Zugdidi buffer-zone occupation (2008-8 to 2008-10), which Russia lacks, while Russia records Abkhazia and South Ossetia, which Georgia counts as republic land. W3 has empty zones because the war page was not opened (page budget).
- /keyframe_review/5 note: the infobox 17,098,246 km2 is '(within internationally recognised borders)', so it excludes Crimea; the note says it includes it. This one does not block.
- Chechnya: the correction that Cliopatria has the years inverted holds against both war pages. Cross-check: chechen-republic (eu-19) has no 1995 loss to mirror /ledger/3.
- Area: 17,098,246 against 16,948,097 (ratio 0.99), acknowledged.

## ukraine (fail)
- /keyframe_review/2: the 2024 correction is the whole 1992 outline, but the Donbas leaves the ledger as plain losses (/ledger/4, 5, 6, 10, 12) and is never regained. Same decision as for Russia.
- /ledger/11: a gain of the whole of Kharkiv Oblast that Ukraine never lost. Reviewer applied: confidence 3 lowered to 2 (the page says 'the majority'). Still open: restructure as occupation_start in 2022-2 and occupation_end in 2022-9 over the occupied east.
- Missing events: the occupation north of Kyiv, February to April 2022. The /ledger/10 note's 'with no territorial change' contradicts the page.
- /ledger/12: the 2022-9 loss to russian-federation has no mirror, and it double-counts the 2014 DPR area. The DPR's 2022-6 gain and the LPR's 2022-6 and 2022-7 gains from ukraine have no loss here. Replace it with losses to the DPR and LPR, and add the 2022 contest_start and contest_end with both republics.
- /ledger/10: Mariupol is lost to russian-federation, which has no matching gain; the DPR /ledger/7 holds Mariupol.
- /ledger/13: Kherson in November 2022 should be occupation_end.
- /ledger/4 does not match the DPR found region: the DPR includes Kramatorsk and Mariupol in April 2014 and loses them to Ukraine in June and July 2014, and Ukraine has no gains for them.
- Area: 603,628 against 590,177 (1992-2023, ratio 0.98) and 568,320 (Cliopatria 2024, Crimea removed). Acknowledged and corrected.

## russian-occupied-territories (fail)
- K3 and K4 keep all of Kherson Oblast in 2023 and 2024, although Ukraine retook Kherson on 11 November 2022 and Russia withdrew to the east bank. No ledger event covers it. Add the 2022-11 event and cut the right bank out of the 2023 and 2024 corrections.
- K3 adds the 2022 Donbas extent, but no ledger event gains it.
- The dossier is typed umbrella, and its gains have no mirrors. The author explained this. The orchestrator should decide whether to keep it as an umbrella or fold it into russian-federation.
- Spot checks: Transnistria since 1992, Abkhazia and South Ossetia since 2008 (decrees of 26 August 2008), Donbas parts and Crimea since 2014, the south since 2022. All confirmed.

## serbia-montenegro (pass)
I tried: 27 April 1992, 4 February 2003, June 1999 Kosovo, 21 May / 3 June / 5 June 2006, the rulers (contiguous, as on the page), and the Republika Srpska and Krajina cells in 1992-1995 (corrected; their dossiers exist and draw them). Area 102,173 against 101,815 (ratio 1.00); the 1992-1995 shape at ratio 1.45 is acknowledged. Mirrors: SFRY lists it as successor, and montenegro gains in 2006-6. kosovo and republic-of-serbia are not written yet. Prevlaka is below a grid cell.

## slovakia (pass)
1 January 1993, the 1997 Sidonie and U Sabotů exchange, the capital and the area 49,035 against 49,241 all check out. Cross-check: czech-republic (eu-22-e) lacks the 1997 mirror events; route this to its owner.

## british-overseas-territories (fix, not applied)
- british-colonial-empire dissolves in 1999 and names this dossier as successor. This dossier starts in 2002 with predecessor united-kingdom, and the Cliopatria 2000 shape is said to hold from 2002, so no dossier draws South Georgia and Bermuda in 2000-2001. Close the gap: start in 2000 with predecessor british-colonial-empire, or have the eu-11 owner end british-colonial-empire in 2002.
- Area 18,015 (text, without the British Antarctic Territory) against 20,560 (ratio 1.14); the correction resolves to 19 cells (about 4,800 km2) for South Georgia and Bermuda.

## Cross-dossier
The report lists 37 checks. The main open items are the Donbas 2014 and 2022 mirrors between ukraine, the DPR and the LPR; the 2008 occupation between Russia and Georgia; the 1995 Chechnya loss; the 1997 Czech-Slovak exchange; and the BOT hand-over.
