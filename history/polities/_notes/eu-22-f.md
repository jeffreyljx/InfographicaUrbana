# eu-22-f notes (Phase B, Europe 1945-2026, part f)

Six dossiers written and validated (0 errors, 0 warnings, `--resolve` clean): republic-of-croatia (3 pages, one over the 1-2 budget, because the 1995 and 1998 border moves needed the Krajina page), former-yugoslav-republic-of-macedonia, republic-of-belarus, republic-of-estonia, republic-of-moldova, republic-of-slovenia (2 pages each). Every page was opened with WebFetch on 2026-11-01. WebFetch returns a small model's extract of the page, so quotes in `note` are the extract's quotes; a few extracts were ambiguous and are flagged below.

Common pattern: Cliopatria starts all six in 1992 while the pages date the births to 1991 (Croatia 25 June, Slovenia 25 June, Macedonia 8 September referendum, Moldova 27 August, Belarus 25 August, Estonia 20 August restoration). Each dossier therefore carries a new 1991 keyframe that repeats the 1992 outline, and a `found` event in 1991. None of the six has a ruler strip (no list opened).

## republic-of-croatia
- Cliopatria's two shapes are not nested. The 1992 shape (44,390 km2) contains about 5,800 km2 of Bosnia and Herzegovina (23 gazetteer cells, read as Herzeg-Bosnia, dossier croatian-republic-of-herzeg-bosnia) and most of Sibensko-Kninska county including Knin, the Krajina's capital; the verdict is `adjust` (minus Bosnia, minus a 35 km radius at Knin). The 1996 shape already includes Eastern Slavonia, which came back only in January 1998 (UNTAES from 15 January 1996): `adjust` for 1996-1997, plus a new keyframe republic-of-croatia_1998 (the unchanged 1996 outline) for 1998-2023.
- Krajina, Eastern Slavonia, Western Slavonia, Konavle are built from the difference of the two Cliopatria shapes, admin-1 intersections and lon/lat radii (Natural Earth has no Knin, Glina, Pakrac, Konavle). Gazetteer names wanted: Krajina (region), Konavle (region), Knin (place), Western Slavonia (region; Pakrac, Okucani), Baranja (region).
- Day-level dates of Operation Flash and Storm are not on the pages opened as quotable sentences (the Krajina page's extract gave "3 May" and "8 August", the republic-of-serbian-krajina dossier has 1-4 May and 4-7 August from another page); only the months (May, August 1995) are recorded here, so the two dossiers agree to the month.
- Page silent: the date the JNA occupation of Konavle began (recorded at confidence 1, 1991), the Prevlaka dispute after the 1992 UN takeover (the pages say only that the peninsula "was demilitarized and turned over to the UNPROFOR"), the Piran Bay border with Slovenia, the Neum/Sutorina sections with Bosnia and Herzegovina.
- The Krajina page gives the RSK at 17,028 km2 at its greatest extent, the War page 13,913 km2 in early 1992 (the 12,200 km2 gap in the 1992 shape is consistent with the smaller figure).

## republic-of-estonia
- Rows: Cliopatria `Estonia` (1919-1939, slug estonia) and `Republic of Estonia` (1992-2024) share Q191 and the identical polygon (48,568.9 km2). They are kept as two dossiers: the Estonian SSR intervenes (1940-1991) and the existing estonia dossier ends in August 1940; the legal-continuity doctrine ("continuity ... preserved through the government-in-exile") is in the predecessor note, with estonia listed as a predecessor.
- The shared polygon equals modern Estonia in the gazetteer (227 of 228 cells), so Cliopatria's 1919-1939 Estonia lacks Pechory (Petseri) and the Narva east bank (Ivangorod), which Estonia held between 1920 and 1944. The owner of the estonia dossier should check this; names wanted in the gazetteer: Pechory/Petseri County (region), Ivangorod (place).
- Estonia's claim to the Treaty of Tartu line is a diplomatic position; the border treaties of 2005 and 2014 were unratified "as of May 2021" (Border page). No contest event is recorded for it. The last Russian army units left in 1994 (day not on the page); not drawn as an occupation.
- Page silent: the Soviet-Estonian declaration of 30 March 1990 (the union dossier uses it), treaty dates of 2005 and 2014.

## republic-of-moldova
- Cliopatria's shape is the right bank without Transnistria and Bender (consistent with the 21 July 1992 ceasefire line); no correction. The Transnistria War page does not say who holds all of Bender (PMR forces "retook parts of Bender, including the center").
- Cliopatria's `Russian-occupied territories` row (1992-2024, 7,000 km2, bbox 28.3-44.5 E, countries Moldova, Georgia, Ukraine) abuts Moldova; the transnistria and russian-occupied-territories dossiers must settle whether the left bank is a state, occupied land, or both.
- Page silent: date of the Moldova-Ukraine land exchange (Giurgiulesti on the Danube against a road stretch; tiny), the 1994 autonomy of Gagauzia and the date of the Gagauz Republic's 1990 declaration (a possible `gagauz-republic` dossier), the UN admission date (the extract was truncated). The Moldova page ties the name change to 27 August 1991, the moldavian-soviet-socialist-republic dossier dates the rename to 23 May 1991.

## republic-of-belarus
- Cliopatria shape equals the republican border; no correction. The Belarus page gives 25 August 1991 for independence and for the change of name, the byelorussian-soviet-socialist-republic dossier 19 September 1991 for the rename.
- The Union State of Russia and Belarus (treaties 2 April 1996 and 1997, 8 December 1999, in force 26 January 2000) is an association: it needs an `umbrella` dossier that no Cliopatria row supplies (suggested slug union-state). The two pages' extracts disagree on the month of the 2022 staging of the invasion from Belarus (April on one, February on the other); no event dated.

## republic-of-slovenia
- Cliopatria shape equals the republican border (76 of 76 cells); no correction. Page silent: Piran Bay and the land dispute with Croatia, the Treaty of Osimo with Italy. The Ten-Day War extract's statement about who took the border crossings on 27 June was ambiguous and is not quoted. The withdrawal of the Yugoslav army: the Slovenia page says "the end of the month" after the 7 July entry, the Ten-Day War page "completed by 26 October"; the latter is used.

## former-yugoslav-republic-of-macedonia
- Two Cliopatria shapes of 25,267 and 25,125 km2 (the infobox gives 25,436); the 142 km2 step in 2000 has no page behind it (`ok`, flagged). The Kosovo page dates a border dispute born of the 2001 insurgency to a land exchange agreement in October 2009 but names no land, so no ledger event can be placed. The 2001 insurgency is listed in `wars` with no zone. Page silent: the exact day of the declaration of independence (the page gives the referendum of 8 September 1991) and of the constitution.
- Display name is North Macedonia; the slug and Cliopatria Name keep "Former Yugoslav Republic of Macedonia", and the ledger carries the two renames (UN admission 8 April 1993 under the provisional name; February 2019 after the Prespa agreement).

## For the gap-fillers
Counterparts without a dossier: union-state (umbrella, Belarus-Russia), gagauz-republic (Moldova, 1990). Existing counterparts used: socialist-federal-republic-of-yugoslavia, republic-of-serbian-krajina, transnistria, serbia-montenegro, union-of-soviet-socialist-republics, estonian-soviet-socialist-republic, byelorussian-soviet-socialist-republic, moldavian-soviet-socialist-republic, estonia.
