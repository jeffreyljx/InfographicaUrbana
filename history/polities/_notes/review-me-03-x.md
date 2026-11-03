# Review of batch me-03-x (Egypt additions: states Cliopatria lacks)

Reviewer me-03-x, 2026-10-19. Eleven dossiers, all new (no Cliopatria rows). Validator: 0 errors, 0 warnings before and after the reviewer's fixes (also with --resolve). Fifteen Wikipedia pages opened by the reviewer; none failed. No page gives an infobox area, so no area comparison was possible (confirmed on every state page).

Verdicts: pass 3 (twenty-fourth, twenty-eighth, khababash); fix 7, all fixed in place by the reviewer (twenty-fifth, twenty-seventh, revolt-of-inaros-ii, twenty-ninth, thirty-first, fourteenth, abydos-dynasty); fail 1 (high-priests-of-amun-at-thebes: missing vassal mirror of the Twenty-first Dynasty).

## twenty-fifth-dynasty-of-egypt: fix

- Finding at `/ledger/0/region; /keyframe_review/0/correction` (applied by reviewer; blocking): The founding region and the -754..-729 keyframe drew Thebes (Luxor 60 km) as Kushite, but the page says Kashta did not control Thebes, and me-03-b's Twenty-third Dynasty holds Thebes until 728. Evidence: Twenty-fifth Dynasty page: Kashta 'likely exercised some influence at Thebes (although he did not control it)'; 'A stela of his was found at Elephantine.' The note quoted only the first half of the sentence. Fix: Applied: region and correction reduced to Aswan (60 km), Elephantine, with text saying why Thebes is left out; reviewer notes appended to /ledger/0 and /keyframe_review/0.
- Finding at `/ledger/15/counterpart; /ledger/16/counterpart; /identity/successors/0/slug` (applied by reviewer; non-blocking): The 656 loss of Upper Egypt named twenty-sixth-dynasty-of-egypt, which begins only in 655; in 656 Psamtik I was still Assyria's vassal king (assyrian-egypt, 664-655). Evidence: assyrian-egypt /ledger/1 (-656 gain of Thebes, counterpart kingdom-of-kush); twenty-sixth-dynasty-of-egypt /ledger/0 (-655 found, counterpart assyrian-egypt); the review of me-03-c moved the 26th's start to 655 for this reason. Fix: Applied: counterpart and successor slug changed to assyrian-egypt, with a reviewer note.
- Finding at `/identity/capitals/0` (NOT applied; non-blocking): Napata (18.54N) is the capital for -754..-713 but lies outside every keyframe of this dossier, which draws only the Egyptian realm (Nubia stays with kingdom-of-kush). Evidence: Keyframes 0-1 are Aswan and Middle/Upper Egypt; check 9 wants capitals inside the state's shapes. Fix: Keep Napata only if the renderer accepts a seat outside the realm, and say so in the capital note; otherwise drop the capital before 712 (the Memphis entry from 712 stands).
- Finding at `/identity/rulers/0` (NOT applied; non-blocking): The ruler strip starts with Piye at -747 while the life starts at -754 (Kashta, founder per the infobox date, is missing). Evidence: Life -754..-656; rulers -747..-656. Fix: Add Kashta for -754..-747 citing the Twenty-fifth Dynasty page (or Kashta's page), or note why the strip starts at Piye.
- Gap at `/keyframe_review/0`: When Piye took Thebes before his year-20 campaign (the Piye page says he 'effectively controlled Upper Egypt by this time' and that his power 'only extended northward from Thebes up to the western desert oases and Herakleopolis'); the 728 gain is therefore late. A dated Thebes gain between 744 and 728 would close it. Page to try: https://en.wikipedia.org/wiki/Kashta
- Gap at `/keyframe_review/7`: Extent of Kushite hold between Thebes and Herakleopolis 663-656 (author's gap). Page to try: https://en.wikipedia.org/wiki/Tantamani
- Spot checks: `/ledger/0` year confirmed (infobox 'Established: 754 BC'); region contradicted by page (Kashta did not control Thebes): fixed; `/ledger/5` confirmed: 'Shebitku conquered the entire Nile Valley, including Upper and Lower Egypt, around 712 BC'; `/ledger/7` confirmed: Shebitku 'transferred the capital to Memphis'; `/ledger/9` confirmed: 'In 671, Esarhaddon took and sacked Memphis'; Necho I set up at Sais; `/ledger/10` confirmed: 'In 669 BC, Taharqa reoccupied Memphis, as well as the Delta'; `/ledger/13` confirmed: 663 defeat near Memphis and the sack of Thebes; `/ledger/15` confirmed: 'In 656 BC, Psamtik sent a large fleet southwards to Thebes'; infobox 'Disestablished: 656 BC'; `/ledger/2` confirmed at confidence 2: no BC year on the page (regnal year 20); 728 is derived and flagged
- Area: No infobox area on the Twenty-fifth Dynasty page (confirmed); no Cliopatria row; keyframes say so.

## twenty-fourth-dynasty-of-egypt: pass

- Spot checks: `/ledger/0` confirmed: infobox dates Tefnakht's conquests to 732 and his reign 732-725; capital Sais; `/ledger/2` confirmed: 'Tefnakht submits to Piye'; the stele page gives regnal years only, 728 is derived (confidence 2, flagged); `/ledger/5` confirmed: 'around 712 BC'; the 24th page's infobox dates Bakenranef's deposition to 720 and the note says so; `/identity/capitals/0` confirmed: capital 'Sais'; 'His authority was recognised in much of the Delta including Memphis'
- Area: No infobox area (confirmed). Tried: found/vassal/loss mirrors with me-03-b's 22nd and this batch's 25th (all match), years, the 712/720 conflict (flagged in notes).

## twenty-seventh-dynasty-of-egypt: fix

- Finding at `/ledger/2/region; /ledger/5/region; /keyframe_review/1/correction` (applied by reviewer; non-blocking): The 460 loss and 454 regain drew only the Sais radius while their text and the Inaros dossier include Mareia (Alexandria 60 km stand-in), so the Mareia coast was drawn by both dossiers in 460-454. Evidence: Inaros II page: 'He held a kingship over the Libyans from Mareia (above Pharos) and the part of the Nile Delta around Sais.' revolt-of-inaros-ii /ledger/0 region is Sais 80 km + Alexandria 60 km. Fix: Applied: Alexandria 60 km added to /ledger/2, /ledger/5 and the subtracted land of /keyframe_review/1.
- Finding at `/wars` (NOT applied; non-blocking): The rebellion at Xerxes' accession (486-484, 'possibly under Psamtik IV' on the 27th page) is not listed as a war. Evidence: Twenty-seventh Dynasty page: the rebellion on Xerxes' accession was 'possibly under Psamtik IV, although different sources dispute that detail'; the dossier records Psamtik IV only in a ruler note. Fix: Add a war entry (Egyptian revolt against Xerxes I, about 486-484, zones [] with a note that the page names no land).
- Gap at `/keyframe_review/0`: Satrapy borders (Libya/Cyrenaica attached or not) and Petubastis III's holding 522-520 (author's gaps). Page to try: https://en.wikipedia.org/wiki/Egypt_(satrapy)
- Spot checks: `/ledger/0` confirmed: 'defeated by Cambyses II at the Battle of Pelusium in the eastern Nile Delta in May of 525'; `/ledger/2` confirmed: 'In 460 BC, he revolted against the Persians'; Mareia and Sais (region widened, see fix); `/ledger/4` confirmed: 'finally defeated by a Persian army led by general Megabyzus in 454 BC'; `/ledger/6` confirmed: 'In 405 BC Amyrtaeus, with the help of Cretan mercenaries expelled the Persians from Memphis'; `/ledger/9` confirmed: infobox 'End of Satrapy: 404 BC'; Artaxerxes II recognised in parts to 401 is in the note
- Area: No infobox area or capital on the 27th page (confirmed). The 'sixth satrapy' line the author asked to recheck is on the page as written: 'Egypt was then joined with Cyprus and Phoenicia to form the sixth satrapy'.

## revolt-of-inaros-ii: fix

- Finding at `/ledger/3/region` (applied by reviewer; non-blocking): The 454 loss returned only the Sais radius to the 27th Dynasty while the found region was Sais + Alexandria (Mareia). Evidence: /ledger/0 region union Sais 80 km + Alexandria 60 km; Inaros II page (Mareia and the Delta around Sais). Fix: Applied: loss region set to the found region, with a reviewer note.
- Spot checks: `/ledger/0` confirmed: 460 BC revolt; Mareia and the Delta around Sais; `/ledger/1` confirmed: Persians kept 'the citadel of Memphis (called the White Castle)'; `/ledger/3` confirmed: captured and taken to Susa, 'crucified in 454 BC'
- Area: No area on the page (confirmed).

## twenty-eighth-dynasty-of-egypt: pass

- Gap at `/keyframe_review/0`: What Amyrtaeus actually held (whole valley drawn at confidence 2; the page says only that he 'consolidate[d] his rule over Egypt'); Elephantine papyri dating by Artaxerxes II to 401. Page to try: https://en.wikipedia.org/wiki/Amyrtaeus
- Spot checks: `/ledger/0` confirmed: 'lasted from 404 BC to 398 BC'; infobox capital Sais; `/ledger/1` confirmed: Nefaarud I defeated Amyrtaeus; infobox 'Deposition of Amyrtaeus: 398 BC'; `/ledger/2` confirmed: 'In 398 BC Amyrtaeus was overthrown and executed by Nefaarud I'
- Area: No area on the page (confirmed). The war bracket -399 is flagged as the researcher's.

## twenty-ninth-dynasty-of-egypt: fix

- Finding at `/ledger/1/counterpart` (applied by reviewer; non-blocking): The 380 dissolve named no counterpart although the land passed to the Thirtieth Dynasty. Evidence: Twenty-ninth Dynasty page: Nefaarud II 'Was deposed and likely killed by Nectanebo I'; thirtieth-dynasty-of-egypt /ledger/0 (-380 found, counterpart twenty-ninth-dynasty-of-egypt). Fix: Applied: counterpart thirtieth-dynasty-of-egypt added.
- Gap at `/wars/0`: Years of the Persian attempts on Hakor (the page gives none). Page to try: https://en.wikipedia.org/wiki/Hakor
- Spot checks: `/ledger/0` confirmed: 'Deposition of Amyrtaeus: 398 BC'; capital Mendes; `/ledger/1` confirmed: 'Deposition of Nefaarud II: 380 BC'; `/identity/rulers` confirmed: Nefaarud I 398-393, Psammuthes 393, Hakor 393-380, Nefaarud II 380
- Area: No area on the page (confirmed). Cliopatria's Thirtieth row starts -383 and overlaps this dossier to -380; flagged by the author for me-03-c.

## thirty-first-dynasty-of-egypt: fix

- Finding at `/wars/0/from` (applied by reviewer; non-blocking): The war 'Artaxerxes III's reconquest of Egypt' started at -351, eight years before this dossier's life (-343). Evidence: Check 2 (wars inside the life). Thirty-first Dynasty page: the c. 351 campaign failed (against the Thirtieth Dynasty); the infobox gives 'Conquests of Artaxerxes III: 343 BC'. Fix: Applied: from -343, with a note that the 351 campaign belongs to the Thirtieth Dynasty dossier.
- Gap at `/identity/capitals/0`: Seat of the Second Persian period (Memphis is the researcher's choice; the page names none). Page to try: https://en.wikipedia.org/wiki/Egypt_(satrapy)
- Spot checks: `/ledger/0` confirmed: 'Conquests of Artaxerxes III: 343 BC'; 'all of Egypt submitted to Artaxerxes'; `/ledger/2` confirmed: table Khababash 338-335, revolt 'in Upper Egypt'; Artaxerxes IV 'Only reigned in Lower Egypt'; `/ledger/3` confirmed: 'Upper Egypt returned to Persian control in 335 BC'; `/ledger/4` confirmed: 'In 332 BC, Mazaces handed over the country to Alexander the Great without a fight'
- Area: No area or capital on the page (confirmed).

## khababash: pass

- Gap at `/keyframe_review/0`: True extent: the Khababash page argues 'Khabash really did have control over all, or almost all, of Egypt' (Thebes contract, Buto decree, Saqqara Apis sarcophagus) against the 31st table's Upper Egypt; the author drew Upper Egypt and recorded the alternative. Page to try: https://en.wikipedia.org/wiki/Satrap_stele
- Spot checks: `/ledger/0` confirmed: 338-335, Upper Egypt; `/ledger/1` confirmed: 'Upper Egypt returned to Persian control in 335 BC'; `/identity/capitals/0` confirmed as honest: the page names no seat; Thebes flagged as the researcher's reading
- Area: No area on either page (confirmed).

## fourteenth-dynasty-of-egypt: fix

- Finding at `/wars/0/from` (applied by reviewer; non-blocking): The war started at -1655, a year no page gives (the note called it the researcher's bracket). Evidence: Fourteenth Dynasty page: 'until its demise under the Hyksos 15th Dynasty around 1650 BC'; no campaign dated. Fix: Applied: from -1650, with a reviewer note.
- Gap at `/identity/rulers`: Ruler strip (no regnal lengths on the page); start date 1700/1725/1805 disputed (author's gap). Page to try: https://en.wikipedia.org/wiki/Nehesy
- Spot checks: `/ledger/0` confirmed: '(c. 1700-1650 BC)', 'a provincial ruling family, located in the Nile Delta'; `/ledger/1` confirmed: 'demise under the Hyksos 15th Dynasty around 1650 BC'; `/keyframe_review/0` confirmed: territory 'roughly consisted of the Nile Delta'; capital 'Xois or Avaris'; infobox c. 1725 noted
- Area: No infobox area (confirmed); the 110 km Avaris radius (about 38,000 km2) is stated in the keyframe note.

## abydos-dynasty: fix

- Finding at `/ledger/1/counterpart` (applied by reviewer; non-blocking): The 1600 dissolve named no counterpart although its note cites the page saying the Hyksos ended the dynasty. Evidence: Second Intermediate Period page: 'The Abydos Dynasty ceased when the Hyksos expanded into Upper Egypt.' Fix: Applied: counterpart hyksos added (me-03-b's hyksos has no matching gain: see cross_checks).
- Gap at `/ledger/1`: Date and manner of the end (own page silent; the SIP page gives c. 1640-1620 and the Hyksos expansion); the Seventeenth Dynasty, named successor, starts only in 1582. Page to try: https://en.wikipedia.org/wiki/Senebkay
- Spot checks: `/ledger/0` confirmed: 'Established: c. 1650 BC'; 'ruling over parts of Middle and Upper Egypt'; southern limit Hu; `/ledger/1` confirmed: 'Disestablished: c. 1600 BC'; end per SIP page (Hyksos)
- Area: No area on the page (confirmed); 60 km Abydos radius stays north of Thebes and reaches Hu.

## high-priests-of-amun-at-thebes: fail

- Finding at `/ledger (missing events)` (NOT applied; blocking): No vassal_start/vassal_end mirrors me-03-b's Twenty-first Dynasty, which records this state as its vassal from -1077 to -943; the dossier's own notes acknowledge the relation but do not write it. Evidence: twenty-first-dynasty-of-egypt /ledger/1 (-1077 vassal_start, counterpart high-priests-of-amun-at-thebes) and /ledger/2 (-943 vassal_end); High Priest of Amun page: the priests were 'not officially pharaohs' and 'not regarded as a ruling dynasty with pharaonic prerogatives'. Fix: Add vassal_start at -1077 and vassal_end at -943, counterpart twenty-first-dynasty-of-egypt, region as /keyframe_review/0, confidence 2, source the High Priest of Amun page; or, if the priests are to be drawn independent, say so and ask me-03-b to drop its vassal pair.
- Finding at `/ledger/1/counterpart` (applied by reviewer; non-blocking): The -943 dissolve named no counterpart while me-03-b's Twenty-second Dynasty gains this land from it in -943. Evidence: twenty-second-dynasty-of-egypt /ledger/1 (-943 gain, counterpart high-priests-of-amun-at-thebes); page: Iuput, son of Shoshenq I, high priest 944-924. Fix: Applied: counterpart twenty-second-dynasty-of-egypt added.
- Gap at `/keyframe_review/0`: Northern limit of the priests' hold (El Hiba/Teudjoi or Herakleopolis); the page names only Upper Egypt. Page to try: https://en.wikipedia.org/wiki/Third_Intermediate_Period_of_Egypt
- Spot checks: `/ledger/0` confirmed: Herihor 'proclaimed as the first ruling High Priest of Amun in 1080 BC', year 19 of Ramesses XI; `/ledger/1` confirmed: 'effectively the rulers of Upper Egypt from 1080 to c. 943 BC'; Psusennes III 976-943; `/identity/rulers` confirmed with the overlap the author flagged (Pinedjem I 1070-1032 in the table, strip cut at 1055)
- Area: No area on the page (confirmed).

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| twenty-fifth-dynasty-of-egypt -728 gain (twenty-third-dynasty-of-egypt) | twenty-third-dynasty-of-egypt -728 loss | mismatch | 23rd loses Upper Egypt to kingdom-of-kush, not to this dossier: the 25th/Kush double coverage of Egypt 754-656 (author problem 2); orchestrator to decide which dossier owns the Egyptian realm. |
| twenty-fifth-dynasty-of-egypt -728 vassal_start (twenty-fourth-dynasty-of-egypt) | twenty-fourth-dynasty-of-egypt -728 vassal_start | matched |  |
| twenty-fifth-dynasty-of-egypt -712 gain (twenty-fourth-dynasty-of-egypt) | twenty-fourth-dynasty-of-egypt -712 loss | matched | kingdom-of-kush /ledger/3 also gains the Delta in -711 from the string "Twenty-fourth Dynasty of Egypt (Sais)": duplicate claim (af-01). |
| twenty-fifth-dynasty-of-egypt -712 vassal_end (twenty-fourth-dynasty-of-egypt) | twenty-fourth-dynasty-of-egypt -712 vassal_end | matched |  |
| twenty-fifth-dynasty-of-egypt -671 loss (neo-assyrian-empire) | neo-assyrian-empire -671 gain | mismatch | neo-assyrian-empire /ledger/31 names kingdom-of-kush as counterpart (same year, same land): 25th/Kush double coverage. |
| twenty-fifth-dynasty-of-egypt -669 gain (neo-assyrian-empire) | neo-assyrian-empire -669 loss | mismatch | neo-assyrian-empire /ledger/32 names kingdom-of-kush as counterpart (same year, same land): 25th/Kush double coverage. |
| twenty-fifth-dynasty-of-egypt -667 loss (neo-assyrian-empire) | neo-assyrian-empire -667 gain | mismatch | neo-assyrian-empire /ledger/35 names kingdom-of-kush as counterpart (same year, same land): 25th/Kush double coverage. |
| twenty-fifth-dynasty-of-egypt -664 gain (neo-assyrian-empire) | neo-assyrian-empire -664 loss | mismatch | neo-assyrian-empire /ledger/36 names kingdom-of-kush as counterpart (same year, same land): 25th/Kush double coverage. |
| twenty-fifth-dynasty-of-egypt -663 loss (neo-assyrian-empire) | neo-assyrian-empire -663 gain | mismatch | neo-assyrian-empire /ledger/38 names kingdom-of-kush as counterpart (same year, same land): 25th/Kush double coverage. |
| twenty-fifth-dynasty-of-egypt -656 loss (assyrian-egypt) | assyrian-egypt -656 gain | mismatch | Counterpart corrected by the reviewer from twenty-sixth-dynasty-of-egypt (starts 655); assyrian-egypt /ledger/1 names kingdom-of-kush: double coverage. |
| kingdom-of-kush -754 gain (twenty-second-dynasty-of-egypt) | twenty-fifth-dynasty-of-egypt -754 found | mismatch | Kush /ledger/1 "Kashta takes Thebes" is contradicted by the Twenty-fifth Dynasty page (Kashta "did not control" Thebes); the 25th now draws only Elephantine in 754. Route to af-01. |
| twenty-fourth-dynasty-of-egypt -732 found (twenty-second-dynasty-of-egypt) | twenty-second-dynasty-of-egypt -732 loss | matched |  |
| twenty-seventh-dynasty-of-egypt -525 found (twenty-sixth-dynasty-of-egypt) | twenty-sixth-dynasty-of-egypt -525 loss | exception | 26th names achaemenid-empire; explained modelling (Persian pharaohs drawn as occupied Egypt, author note 1). |
| twenty-seventh-dynasty-of-egypt -525 occupation_start (achaemenid-empire) | achaemenid-empire - none | exception | achaemenid-empire owned by me-05, not run yet. |
| twenty-seventh-dynasty-of-egypt -460 loss (revolt-of-inaros-ii) | revolt-of-inaros-ii -460 found | matched | Region aligned by the reviewer (Mareia added). |
| twenty-seventh-dynasty-of-egypt -454 gain (revolt-of-inaros-ii) | revolt-of-inaros-ii -454 loss | matched | Region aligned by the reviewer. |
| twenty-seventh-dynasty-of-egypt -404 loss (twenty-eighth-dynasty-of-egypt) | twenty-eighth-dynasty-of-egypt -404 found | matched |  |
| twenty-seventh-dynasty-of-egypt -404 occupation_end (achaemenid-empire) | achaemenid-empire - none | exception | me-05 not run yet. |
| twenty-eighth-dynasty-of-egypt -398 loss (twenty-ninth-dynasty-of-egypt) | twenty-ninth-dynasty-of-egypt -398 found | matched |  |
| twenty-ninth-dynasty-of-egypt -380 dissolve (thirtieth-dynasty-of-egypt) | thirtieth-dynasty-of-egypt -380 found | matched | Counterpart added by the reviewer. |
| thirty-first-dynasty-of-egypt -343 found (thirtieth-dynasty-of-egypt) | thirtieth-dynasty-of-egypt -343 loss | exception | 30th names achaemenid-empire; explained modelling. |
| thirty-first-dynasty-of-egypt -343 occupation_start (achaemenid-empire) | achaemenid-empire - none | exception | me-05 not run yet. |
| thirty-first-dynasty-of-egypt -338 loss (khababash) | khababash -338 found | matched |  |
| thirty-first-dynasty-of-egypt -335 gain (khababash) | khababash -335 loss | matched |  |
| thirty-first-dynasty-of-egypt -332 loss (macedonian-empire) | macedonian-empire -332 gain | mismatch | macedonian-empire /ledger/26 gains Egypt from achaemenid-empire; under the occupation model it should name thirty-first-dynasty-of-egypt (or the 31st should be read as the Achaemenid side). Same year and land. |
| thirty-first-dynasty-of-egypt -332 occupation_end (achaemenid-empire) | achaemenid-empire - none | exception | me-05 not run yet. |
| fourteenth-dynasty-of-egypt -1700 found (middle-kingdom-of-egypt) | middle-kingdom-of-egypt -1700 loss | matched |  |
| fourteenth-dynasty-of-egypt -1650 loss (hyksos) | hyksos -1650 found | matched | hyksos founds with this dossier as counterpart; fifteenth-dynasty-of-egypt also founds -1650 from it (two Hyksos dossiers, see problems). |
| abydos-dynasty -1650 found (middle-kingdom-of-egypt) | middle-kingdom-of-egypt - none | missing | middle-kingdom-of-egypt (me-03-a) loses Lower Egypt to hyksos, Thebes to the 16th and Lower Nubia to Kerma in 1650, but not Abydos/Thinis to this dossier. |
| abydos-dynasty -1600 dissolve (hyksos) | hyksos - none | missing | hyksos (me-03-b) has no gain of Abydos about 1600; the SIP page says the Hyksos expansion ended the Abydos Dynasty. Also seventeenth-dynasty-of-egypt names abydos-dynasty as predecessor but starts 1582. |
| high-priests-of-amun-at-thebes -1080 found (new-kingdom-of-egypt) | new-kingdom-of-egypt - none | missing | new-kingdom-of-egypt (me-03-b) keeps Upper Egypt to its -1077 dissolve, so both draw Thebes 1080-1077; NK should record the loss of the south to this dossier in 1080 (page: Herihor ruled Thebes while Ramesses XI ruled the north). |
| twenty-first-dynasty-of-egypt -1077 vassal_start (high-priests-of-amun-at-thebes) | high-priests-of-amun-at-thebes - none | missing | No mirror in this dossier: blocking fix 1. |
| twenty-first-dynasty-of-egypt -943 vassal_end (high-priests-of-amun-at-thebes) | high-priests-of-amun-at-thebes - none | missing | No mirror in this dossier: blocking fix 1. |
| twenty-second-dynasty-of-egypt -943 gain (high-priests-of-amun-at-thebes) | high-priests-of-amun-at-thebes -943 dissolve | matched | Counterpart added to the dissolve by the reviewer. |

## Problems for the orchestrator

- The five gazetteer_names_needed are improvement requests passed on from the author, not unresolved names: --resolve is clean before and after the fixes (Alexandria, Fayyum and Lower Egypt stand in today).
- Double coverage: twenty-fifth-dynasty-of-egypt and kingdom-of-kush (af-01) both draw Egypt 754-656 as solid territory, and every neighbour (twenty-third-dynasty-of-egypt, neo-assyrian-empire, assyrian-egypt) names kingdom-of-kush as counterpart. The orchestrator must decide which dossier owns the Egyptian realm and route counterpart renames accordingly; the author flagged it.
- Two Hyksos dossiers exist: hyksos.json and fifteenth-dynasty-of-egypt.json, both -1650..-1550 and both founded from fourteenth-dynasty-of-egypt (me-03-b). Not this batch's, but its 14th and Abydos counterparts point at hyksos.
- Persian periods (27th, 31st) are drawn as occupied Egypt with occupation events naming achaemenid-empire; me-05 has not run, so all Achaemenid mirrors are exceptions. macedonian-empire's 332 gain of Egypt names achaemenid-empire rather than thirty-first-dynasty-of-egypt.
- kingdom-of-kush /ledger/1 (754, 'Kashta takes Thebes') is contradicted by the Twenty-fifth Dynasty page ('although he did not control it'); af-01 should revisit.
- WebFetch returns summaries; quoted phrases above are as the fetch returned them. No page failed to load. The brief's notes path history/polities/_notes/review-me-03-x.md and the scratch /tmp/claude-0/work/me-03-x/ were used.
