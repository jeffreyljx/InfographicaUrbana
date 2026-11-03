# Review of am-08-i (2026-10-19)

Reviewer: adversarial pass on republic-of-panama, maderistas, argentine-republic, republic-of-haiti, cuban-communists. Validator with --resolve: 0 errors, 0 warnings for all five. Pages opened (WebFetch, all loaded): Panama; Panama Canal Zone; Treaty of Ciudad Juarez; List of factions in the Mexican Revolution; Argentina; Falklands War; Haiti (twice); Dominican Republic-Haiti border; Cuban Revolution. Grid checks with tools/gazetteer.py. No reviewer fix applied: none of the findings is a one-field edit.

Verdicts: republic-of-panama thin; maderistas thin; argentine-republic fix; republic-of-haiti fix; cuban-communists pass.

## republic-of-panama: thin
- Confirmed on the pages: independence 3 November 1903 (infobox); Zone created 18 November 1903, turned over 4 May 1904, ceased to exist 1 October 1979, last parcels 31 December 1999; 553 sq mi (1,430 km2). Grid: Panama 2000 minus 1999 = 5 cells, inside the US shapes in 1950 and 1980, not in 1904. US mirrors at 1904-05 and 1979-10 match.
- Area: infobox 75,417 km2 against 83,580 km2 (ratio 1.11), acknowledged.
- Thin: republic-of-costa-rica records the Coto War (contest 1921-02 to 1921-03) and a 1921-03 gain from republic-of-panama, with no mirror here. The Panama page is silent on Coto (checked), so this is a budget gap. The Costa Rican region (Golfito 30 km) holds no cell of Cliopatria's Panama 1920 shape, so the gap-filler must decide between adjusting the 1905 keyframe to hold Coto for 1905-1920 with a 1921 loss, or recording only the war and contest. Page: Coto War.

## maderistas: thin
- Confirmed: siege of Ciudad Juarez (army approaching in April, besieged by the end of the month); treaty 21 May 1911; Diaz resigned 25 May; Madero elected October 1911; List of factions gives only '1910-11'.
- Fix (author, not blocking): the Treaty page does name a theatre: 'In the Guerrero district of Chihuahua, Pascual Orozco attacked federal troops'. Quote it in /keyframe_review/0 note and /ledger/0 (confidence stays 1, the year is not the page's).
- Fix (author, not blocking): /ledger/2 note says the page gives no end of the Ciudad Juarez fighting, but the page says 'After two days of fighting the city fell to the insurrectionists'. Rewrite the note and the war outcome; month 5 can stay.
- Thin: the zone's location and the 1910 months (page: Pascual Orozco); the dated capture of Ciudad Juarez (page: Battle of Ciudad Juarez (1911)). Grid: the zone is exactly Mexico 1910 minus Mexico 1911 (114 cells); the Ciudad Juarez contest zone is outside it (9 Mexican cells, 8 in the US).
- Accepted: the war begins in 1910 while the dossier starts in 1911 (the movement fought before Cliopatria draws a zone).

## argentine-republic: fix
- Confirmed: 1930 coup (row boundary, confidence 1); 2 April 1982 invasion, South Georgia 'the next day' (Argentina page: March); 14 June surrender. Area: infobox 2,780,085 km2 against 2,792,291 km2 (ratio 1.004).
- Fix (author, not blocking): /ledger/4 ends the occupation of South Georgia on 14 June, but the British retook it in April (Falklands War page, Operation Paraquet: after regrouping on 24 April 'the Argentine forces, a total of 190 men, surrendered without resistance to the Royal Marines'). Keep /ledger/4 for 'Falkland Is.' only and add an occupation_end 1982-04 on 'S. Geo. and the Is.' (confidence 2), counterpart british-colonial-empire.
- Thin: the 1936 swap. Grid-verified: the 3 gained cells are Bolivia's in 1930 and 1935 and Argentina's in 1936; the 3 lost cells are Argentina's to 1935 and Paraguay's in 1936 and 1938. Neither the bolivia nor the paraguay dossier has a mirror. If no page supports a transfer, a cleaner reading is to adjust argentine-republic_1936 (keep the 1930 outline) and drop both confidence-1 events.
- Falklands counterpart british-colonial-empire: eu-11 not run (exception). Its 1982 shape holds 44/47 Falklands and 9/10 South Georgia cells.

## republic-of-haiti: fix
- Confirmed: occupation 1915-1934, ended 'in 1934, under the Presidency of Stenio Vincent', infobox 15 August 1934; page silent on 1936. Border page: 1929; 27 February 1935; final treaty 9 March 1936; names no towns and no winner. Area: infobox 27,700 km2 (body 27,750) against 31,292 km2 (ratio 1.13). Grid: Republic of Haiti 1936 = Empire of Haiti 1915 (140 cells); Dominican Republic 1935 = 1937.
- Fix (author, not blocking): both keyframes leave out Tortuga ('The island of Tortuga is located off the coast of northern Haiti'), 1 land cell in no polity's shape. Set them to adjust with a union of the Cliopatria shape and {lon -72.8, lat 20.04, km 12} (or place 'Tortuga' once the gazetteer has it). The notes flagged Tortuga but kept 'ok'.
- Mismatch to route: dominican-republic /ledger/10 (1936-03 loss to republic-of-haiti) is land already on the Haitian side of both constant shapes; recommend the dominican-republic owner turn it into a certainty note. No gain is needed here.
- Mismatch to route: united-states-of-america (am-07) L93/L99 name republic-of-haiti for the 1915-1934 occupation; the counterpart is 'haiti' (haiti L26/L27 mirror them).

## cuban-communists: pass
- Tried and could not break: 1 January 1959 flight of Batista and 8 January arrival in Havana; El Jiguee 11-21 July 1958; Las Mercedes 29 July-8 August; Santa Clara columns and 31 December 1958; Granma landing 2 December; 'the mountains came under Castro's control'; Operation Verano undated on the page, as the note says. Grid: the zone is exactly Cuba 1957 minus Cuba 1958 (12 cells); Communist Cuba 1960 takes it back. Mirrors with republic-of-cuba match (1958 loss, 1959-01 gain). Display name change is justified on the pages; the Cliopatria name is kept.
- To route: republic-of-cuba_1958 (1958-1959) is still 'ok', keeping the zone out through 1959; it should be adjust (zone back from 1 January 1959) to agree with this dossier and with republic-of-cuba's own 1959 gain.
- Thin: the 1956-1957 start of the Sierra Maestra base (page: 26th of July Movement). Gazetteer: 'Sierra Maestra' region.

## Gazetteer names
- Sierra Maestra (region; cuban-communists). Tortuga / Ile de la Tortue (place, about 72.8 W 20.04 N; republic-of-haiti fix).

## Batch-wide
- unitary-state-of-brazil not written is right: brazilian-republic holds all four Q155 Names and reviews all three unitary-state shapes.
- Two states are split across Cliopatria rows with confidence-1 row-boundary events (argentine-confederation/argentine-republic; haiti/republic-of-haiti): contiguous and mirrored, flagged for the orchestrator.
