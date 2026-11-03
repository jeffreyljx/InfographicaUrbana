# Review of batch me-03-c (Twenty-sixth and Thirtieth Dynasties of Egypt)

Reviewer, 2026-10-19 (brief filled 2026-10-18). Machine copy: history/notes/phase-b/reviews/me-03-c.json.

Validator (--resolve): both dossiers valid, no errors; one warning on thirtieth (/ledger/0 counterpart twenty-ninth-dynasty-of-egypt, no dossier yet: listed in counterparts_needing_dossiers, me-03-x). Pages opened: Twenty-sixth Dynasty of Egypt, Amasis II, Thirtieth Dynasty of Egypt, Second Achaemenid conquest of Egypt, Cyrenaica, Assyrian conquest of Egypt. Neighbour dossiers read: assyrian-egypt, kingdom-of-kush, neo-assyrian-empire, neo-babylonian-empire, greek-city-states (ledger grep). Not written yet: achaemenid-empire (me-05), phoenicia (me-04), carthage (af-02), twenty-ninth/twenty-seventh/thirty-first dynasties (me-03-x).

## twenty-sixth-dynasty-of-egypt: FAIL (back to the author)

Spot checks, all confirmed on the page with the year: /ledger/0 (Established 664 BC, capital Sais); /ledger/1 (quotes "recognized as sole king over all of Egypt", "Reunified Egypt and ended the Kushite control of Upper Egypt" are on the page; no year, as the note says); /ledger/2 (Amasis II: "to this he added Cyprus", no year, as the note says); /ledger/4 (Cambyses II "captured and later executed Psamtik III"; Amasis II page "battle of Pelusium in 525 BC"); /ledger/6 ("Disestablished: 525 BC", "Cambyses founded the First Egyptian Satrapy"). Nothing fabricated; confidences honest. Area: no infobox area on either page (acknowledged). Capital Sais 30.97N 30.77E is Sa el-Hagar, inside the -615 bbox. Rulers contiguous. Keyframes and ledger agree.

Blocking:
1. /identity/start, /keyframe_review/0, /ledger/0-1: Lower Egypt is drawn twice in 664-655. assyrian-egypt (passed in me-02) is Psamtik I's vassal kingdom 664-655, found -664 with Lower Egypt, gains Upper Egypt from Kush -656 (kingdom-of-kush /ledger/11 gives it to assyrian-egypt), dissolves -655 into this dossier; neo-assyrian-empire /ledger/37 and /41 have the vassal tie 664-655 with assyrian-egypt. This dossier's -664 found names assyrian-egypt as counterpart but assyrian-egypt has no loss in 664. Fix (recommended, matches three reviewed neighbours): start at -655. Delete /keyframe_review/0; replace /ledger/0 and /ledger/1 with one found at -655, counterpart assyrian-egypt, region {"cliopatria": "Twenty-sixth Dynasty of Egypt", "year": -615}, confidence 2, source https://en.wikipedia.org/wiki/Assyrian_conquest_of_Egypt ("Psamtik I threw off his ties to the Assyrians circa 655 BCE"; "by 656/655 BCE ... was able to declare outright independence from Assyria") added to sources; start, capital, Psamtik I's ruler entry and certainty from -655 (note: king from 664 as Assyrian vassal, see assyrian-egypt); drop the kingdom-of-kush predecessor entry. Alternative for the orchestrator: merge assyrian-egypt into this dossier (start -664 as vassal of neo-assyrian-empire, gain Upper Egypt from Kush -656, vassal_end -655), which needs edits in kingdom-of-kush and neo-assyrian-empire and retires assyrian-egypt.

Non-blocking:
2. /ledger/2: counterpart greek-city-states does not hold Cyprus in 555: greek-city-states /ledger/4 gives Cyprus to neo-assyrian-empire in -709 and never regains it; neo-assyrian-empire /ledger/26 gains it -709 and has no later Cyprus event. Use counterpart nobody (the Cypriot city-kingdoms) unless a page names a holder; keep phoenicia (/ledger/3) pending me-04.

Thin (within the 1-2 page budget, by design): Cyprus year and holders (/ledger/2-3) and its fate in 525 (/ledger/5), try https://en.wikipedia.org/wiki/Ancient_history_of_Cyprus; Necho II's hold on the Levant 609-605 (Megiddo, Carchemish), try https://en.wikipedia.org/wiki/Necho_II and https://en.wikipedia.org/wiki/Battle_of_Carchemish (neo-babylonian-empire has a -605 Carchemish war with zone Levant naming this state, and gains the Levant from Assyria in 609: an Egyptian Levant 609-605 would conflict with that gain); Psamtik II's Nubian campaign (kingdom-of-kush dates it -593 from the Napata page, this dossier -592 from Amasis II), try https://en.wikipedia.org/wiki/Psamtik_II.

## thirtieth-dynasty-of-egypt: THIN

Spot checks, all confirmed: /ledger/0 ("Nectanebo I had gained control of all of Egypt by November of 380 BC"; "deposed and likely killed Nefaarud II"); /ledger/1 (343; "forced to withdraw from his defenses in the Nile Delta to Memphis"); /ledger/3 (343; the Second Achaemenid conquest page does give "340 or 339 BC" and "after a failed attempt in 351", so the c2 is honest); /ledger/5 ("Succeeded by: Thirty-first Dynasty of Egypt", "Flight of Nectanebo II: 343 BC"). Area: no infobox area (acknowledged). Capital Sebennytos 30.97N 31.24E is Samannud, inside the bbox. Rulers contiguous. Wars match the page; contest pair matches the war zone.

Libya (non-blocking here, flagged by the author as unverified: page budget, 16% of the shape, below a factor of two): the Cyrenaica page contradicts the shape: "In 525 BC, after conquering Egypt, the Achaemenid (Persian) army of Cambyses II seized the Pentapolis", a satrapy "for about the next two centuries", "The Persians were followed by Alexander the Great in 332 BC"; no Egyptian rule of the 4th century is mentioned, and greek-city-states /ledger/15 has Cyrenaica lost to achaemenid-empire in -525. Fix: corrections of /keyframe_review/0-2 = {"minus": [{"cliopatria": "Thirtieth Dynasty of Egypt", "year": Y}, {"country": "Libya"}]} with text, verdict adjust; delete /ledger/4; add https://en.wikipedia.org/wiki/Cyrenaica to sources. Route to me-05: achaemenid-empire should hold Cyrenaica (or say who did) 380-343.

Thin otherwise: the failed Persian invasion of 373 (Pharnabazus and Iphicrates), try https://en.wikipedia.org/wiki/Nectanebo_I; Teos' Syrian campaign, try https://en.wikipedia.org/wiki/Teos_of_Egypt; the 343 vs 340/339 date, try https://en.wikipedia.org/wiki/Nectanebo_II; the Twenty-ninth Dynasty predecessor dossier (me-03-x).

## Cross-dossier matrix

- 26th -664 found / assyrian-egypt: MISMATCH (assyrian-egypt -664 found holds the same Lower Egypt to -655; no loss in 664).
- 26th -655 gain / assyrian-egypt: matched (assyrian-egypt /ledger/2 dissolve -655, counterpart this state).
- 26th predecessor kingdom-of-kush (Upper Egypt): mismatch (kingdom-of-kush /ledger/11 -656 loss names assyrian-egypt).
- 26th -550 gain / greek-city-states (Cyprus): mismatch (greek-city-states lost Cyprus -709 to neo-assyrian-empire).
- 26th -550 gain / phoenicia: exception (me-04 not run).
- 26th -525 loss x2 and dissolve / achaemenid-empire: exception (me-05 not run).
- 30th -380 found / twenty-ninth-dynasty-of-egypt: exception (counterparts_needing_dossiers, me-03-x).
- 30th -343 contest pair, loss, dissolve / achaemenid-empire: exception (me-05 not run).
- 30th -343 loss of the Libyan coast / achaemenid-empire: exception on the counterpart, but the land conflicts with greek-city-states -525 and the Cyrenaica page (see above).
- Wars: kingdom-of-kush "Psamtik II's Nubian campaign" -593 vs 26th -592 (one year, both from pages); neo-babylonian-empire "Battle of Carchemish" -605 (zone Levant) has no counterpart war entry here (folded into the 612-567 conflict).

Gazetteer: Sebennytos (place, Samannud, 30.97N 31.24E).
