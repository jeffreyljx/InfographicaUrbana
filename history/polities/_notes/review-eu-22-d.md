# Review of batch eu-22-d (2026-11-01)

Reviewer: adversarial review, Phase B. Dossiers: greek-junta, malta, portugal, third-hellenic-republic, turkish-republic-of-northern-cyprus, republic-of-lithuania. Machine copy: history/notes/phase-b/reviews/eu-22-d.json.

Mechanical: all six validate with `--resolve` (0 errors, 0 warnings), before and after the reviewer's edits. Cliopatria rows and shapes all reviewed; new keyframes carry from/to/correction. Capitals lie inside their shapes' bboxes. No confidence-1 events. Every event (15) was spot-checked on its cited page, all confirmed with the year and month; nothing fabricated.

## Verdicts

| slug | verdict | why |
| --- | --- | --- |
| greek-junta | fix (applied by reviewer) | war zones were empty though ground changed hands in Cyprus |
| malta | pass | all 3 events confirmed; UK side missing (eu-11) |
| portugal | fix (applied by reviewer) | "land area" was the infobox total; estado-novo overlap routed to orchestrator |
| third-hellenic-republic | pass | one event, confirmed; no Greek border moved 1974-2026 |
| turkish-republic-of-northern-cyprus | **fail** | missing mirror vassal_start of republic-of-turkey (1975-02) |
| republic-of-lithuania | pass | events confirmed; USSR contest/loss model differs (routed) |

## Findings

### greek-junta (fix, applied)
- `/wars/0/zones` was `[]` with the note "no Greek border moved". The brief allows empty zones only where no ground changed hands; the Turkish invasion page: 3% of the island by 22 July, "approximately 36%" after 14 August. Applied: zone `{country: Northern Cyprus}` (as in the TRNC, Cyprus and Turkey entries) and the note reworded.
- Spot checks: coup 21 April 1967, republic 1 June 1973 (referendum 29 July, counter-coup 25 November 1973), fall 24 July 1974 (Greek junta page), collapse 23 July (invasion page). Area 131,957 vs 123,711 (0.94), acknowledged.

### malta (pass)
- 21 September 1964, 13 December 1974, 31 March 1979 and "lands formerly controlled by the British were given to the Maltese government" all on the Malta page. Area 316 vs 474.7 (1.50), acknowledged (grid).
- Cross-check: united-kingdom.json (eu-11) puts Malta in its 1801 found region and never loses it. Route to eu-11: a 1964-09 loss of Malta to `malta` (and, if wanted, a 1979-03 caption loss of the base lands).

### portugal (fix, applied)
- `/sources/0/note`, `/keyframe_review/0/note`: "infobox land area 92,225 km2"; the infobox gives "Total: 92,225 km2" (water 1.2%). Applied: "total area".
- Advisory (orchestrator): estado-novo.json (another group) runs 1926-05 to 2024 with a 1974-04 rename and its own 1999-12 Macau loss; this dossier starts 1976-04 naming estado-novo as predecessor. 1976-2024 is claimed twice. Suggest ending estado-novo at 1976-04 with successor portugal and dropping its 1999 Macau loss (eu-22 splits regimes on Cliopatria rows: greek-junta / third-hellenic-republic).
- Advisory: Flores and Corvo (western Azores, about 31.1 W) are outside every Portugal shape (bbox stops at 28.85 W); the corrections leave them out (about 160 km2).
- PRC ledger/14 gains Macau 1999-12 from `portugal`: matched. Constitution 25 April 1976, Macau "Chinese territory under Portuguese supervision" 1976, handover midnight 20 December 1999, Joint Declaration 13 April 1987: confirmed.

### third-hellenic-republic (pass)
- Infobox "Established: 24 July 1974"; Metapolitefsi: Karamanlis sworn in "At 4 a.m. on 24 July 1974", Gizikis stayed "for legal continuity reasons". The page is silent on borders (Prespa undated, no Imia/Aegean), as the author says. 1992 -286 km2 read as grid: acceptable within a 1-2 page budget. Area 131,957 vs 121,731 (0.92).

### turkish-republic-of-northern-cyprus (fail)
- Blocking: republic-of-turkey.json (me-10, written 2026-10-25) has ledger/6 `1975-02 vassal_start`, counterpart `turkish-republic-of-northern-cyprus`. This dossier has no mirror, and its notes ask Turkey and the colour agent to decide a question that dossier had already decided. Rule 3 of the reviewer brief requires the mirror. Fix: add `{year 1975, month 2, type vassal_start, counterpart republic-of-turkey, region {cliopatria: Turkish Republic of Northern Cyprus, year 1976, text: ...}, source Turkish invasion of Cyprus page ("On 13 February 1975, Turkey declared the occupied areas of the Republic of Cyprus to be a 'Federated Turkish State'"), confidence 2}` with no end, and update the notes.
- Otherwise sound: August 1974 administration (infobox 1 October 1974, flagged), 13 February 1975 (infobox only on the Northern Cyprus page; the invasion page confirms), 15 November 1983, the war dates and 3% / 36-37% all confirmed. Area 3,355 vs 4,341 (1.29) acknowledged (buffer zone in the shape).
- Cyprus vs TRNC (occupation vs state) is an accepted de jure / de facto exception, flagged by the author.

### republic-of-lithuania (pass, with routing)
- All three events confirmed on the Act page (10:44 pm, 124 votes; 13 January 1991 LRT and TV Tower; 6 September 1991 State Council). Area 65,300 vs 65,178 (1.00).
- Advisory (orchestrator): union-of-soviet-socialist-republics (eu-17, written 2026-10-31) already has contest_start 1990-03 over the whole country (conf 3), contest_end 1991-09 and loss 1991-09 to republic-of-lithuania. This dossier contests only the Vilnius sites from 1991-01 and takes the land at 1990-03. The notes' request that the USSR "carry the matching loss 1990-03" misreads that dossier. Choose one model: either move ledger/1 here to 1990-03 with region `{country: Lithuania}`, or the USSR narrows its contest and moves its loss to 1990-03.
- Advisory: predecessor kingdom-of-lithuania (ended 1940-07) names only the Lithuanian SSR as successor; the 1990 continuity is legal, not territorial.
- Thin by design (1-2 pages): the 1992 -168 km2 Latvian-cell change and the border treaties; page to try: Latvia–Lithuania border.

## Cross-dossier matrix (summary)
- matched: kingdom-of-greece dissolve 1967-04 / greek-junta found; greek-junta dissolve 1974-07 / third-hellenic-republic found; portugal loss 1999-12 / PRC gain 1999-12; LSSR dissolve 1990-03 / Lithuania found; USSR contest_end 1991-09 / Lithuania contest_end 1991-09; the Cyprus war zones.
- missing: UK loss of Malta 1964 and 1979 (eu-11); TRNC vassal_start mirror of Turkey 1975-02 (eu-22-d, blocking).
- mismatch: portugal vs estado-novo overlap; Lithuania contest_start 1991-01 (Vilnius) vs USSR 1990-03 (Lithuania); USSR loss 1991-09 vs Lithuania found 1990-03.
- exception: TRNC found 1974-08 vs Cyprus occupation by Turkey (de jure vs de facto).

Gazetteer names needed: none. Counterparts needing dossiers: none.
