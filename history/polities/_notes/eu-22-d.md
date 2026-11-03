# eu-22-d notes (Europe 1945-2026, part d), written 2026-11-01

Six dossiers, all validating with `--resolve` (0 errors, 0 warnings): greek-junta, malta, portugal, third-hellenic-republic, turkish-republic-of-northern-cyprus, republic-of-lithuania. Eleven pages opened, all loaded: Greek junta, Third Hellenic Republic, Metapolitefsi, Turkish invasion of Cyprus, Northern Cyprus, Malta, State of Malta, Portugal, Handover of Macau, Lithuania, Act of the Re-Establishment of the State of Lithuania (the Turkish invasion page is cited by two dossiers, and each dossier lists two pages).

## Needs the orchestrator
- portugal vs estado-novo: polities/estado-novo.json (another group) is one Portuguese state 1926-2024 with the 1974 Third Republic as a rename and the 1999 Macau loss. `portugal` follows Cliopatria's split (row 1976..2024) and starts with the constitution of 25 April 1976, naming estado-novo as predecessor. Kept both, so 1976-2024 is claimed twice. Suggested: end estado-novo in 1975 with portugal as successor, or fold portugal into estado-novo.
- Cliopatria Portugal 1976-2023 shape still contains Macau (cell at 113.7 E, 22.2 N) until 2023; keyframe portugal_2000 (new) uses the 2024 shape. The western Azores (west of 28.8 W) appear in no Portugal shape (gazetteer Azores box 31.2 W to 25.2 W).
- Northern Cyprus: the republic-of-cyprus dossier (eu-22) draws the north as a Turkish occupation (counterpart republic-of-turkey, no occupation_end); turkish-republic-of-northern-cyprus draws it as a state from August 1974 and, since the review fix below, carries the 1975-02 vassal_start of republic-of-turkey that republic-of-turkey.json (me-10) ledger/6 already had. Open for the colour agent: between 1975-02 and 2026 the same ground is both occupation (Cyprus and Turkey ledgers, no occupation_end) and vassal (Turkey and TRNC ledgers); the Northern Cyprus page dates the first Turkish Cypriot administration to August 1974 in the text and 1 October 1974 in the infobox; August used.
- greek-junta ends July 1974 (Cliopatria row to 1975); third-hellenic-republic starts 24 July 1974 (Cliopatria row from 1976); each has a new or adjusted keyframe for the gap. Both claim 1974.
- lithuania: union-of-soviet-socialist-republics (eu-17) should carry the matching loss 1990-03 and contest zone (Vilnius broadcasting sites, Jan to Sept 1991); lithuanian-soviet-socialist-republic already dissolves 1990-03.
- malta: predecessor slug `united-kingdom`; no matching loss in the UK dossier for 1964 or 1979 was checked.

## Pages silent (nothing written from memory)
- Greek junta: Dodecanese and Aegean; no ruler list. Third Hellenic Republic: no Greek border event, Imia 1996, Aegean shelf, western Thrace, Prespa year, 8 December 1974 referendum date; 1992 shape change (-286 km2) unexplained.
- Malta: signing year of the defence agreement; maritime boundaries.
- Portugal: dates of African independences, Timor, Azores/Madeira autonomy, EEC day. Macau page gives no area.
- Lithuania: Latvia, Belarus, Kaliningrad border treaties; 1992 shape change (-168 km2, Latvian cells) unexplained.
- TRNC: Varosha, Pyla, first president, ceasefire day of 16 August 1974 (page gives the Security Council resolution on 16 August and the ceasefire of 22 July for phase one).

## Gazetteer names
All regions resolve (Northern Cyprus, Macao, Portugal, Greece, Malta, Lithuania, place Vilnius). No names needed.

## Area checks (Cliopatria km2 against infobox km2)
- Greek junta 1973 shape 123,711 km2 vs infobox 131,957 (0.94); TRNC 4,341 vs 3,355 (1.29); Malta 474.7 vs 316 (1.50); Portugal 96,985 vs 92,225 (1.05); Lithuania 65,346 vs 65,300 (1.00).

## Review fixes (2026-11-01, author returning after the reviewer's verdict)
- turkish-republic-of-northern-cyprus (verdict fail, one finding, applied): added ledger/2, 1975-02 vassal_start, counterpart republic-of-turkey, region {cliopatria: Turkish Republic of Northern Cyprus, year 1976, text: the page's own words}, source Turkish invasion of Cyprus, confidence 2, no vassal_end. Page reopened 2026-11-01: 'On 13 February 1975, Turkey declared the occupied areas of the Republic of Cyprus to be a "Federated Turkish State"' and 'Turkey is the only country that recognises it'. Rewrote the notes paragraph that left the question open. Re-validated with --resolve: 0 errors, 1 warning (the validator's own 'vassal_start has no vassal_end', which it says is fine when the relation lasts to the state's end, here 2026).
- Where I differ from the reviewer, by a little: (1) confidence 2 as asked, but the region text quotes the invasion page ('the occupied areas ... a "Federated Turkish State"') rather than the reviewer's 'Turkish Federated State', because the Northern Cyprus infobox uses the second wording and the invasion page the first; (2) the invasion page gives no day for the 1983 declaration (it says only 'In 1983, the Turkish Cypriot assembly declared the independence'), so 15 November 1983 stays on the Northern Cyprus page, as cited; (3) republic-of-turkey ledger/6 says the relation 'runs to 2024' (the Cliopatria row's end) while this dossier runs to 2026; neither side has a vassal_end, so no mismatch for the validator, but the orchestrator may want one end year.
- Not touched: greek-junta and portugal (verdict fix, already applied by the reviewer), malta, third-hellenic-republic, republic-of-lithuania (pass). Their routed advisories (estado-novo overlap, UK loss of Malta, USSR/Lithuania contest model) stay with the orchestrator and are in the lists above and in the review notes.
