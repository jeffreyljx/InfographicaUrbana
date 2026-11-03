# eu-22-e notes (Europe 1945 to 2026, part e)

Six dossiers written, all validate with 0 errors; `--resolve` leaves no unknown region names. Pages opened 2026-10-31 with WebFetch. Detail per state is also in each dossier's `notes`.

## Cross-cutting
- Dates: all six states are the same countries as their communist-era or federal predecessors, under Cliopatria's regime-by-regime rows. The dossiers follow the pages' founding dates, which differ from Cliopatria's first year: Romania 28 Dec 1989 (row 1990), Germany 3 Oct 1990 (row 1991), Bulgaria 15 Nov 1990 (row 1991), Albania 29 Apr 1991 (row 1991), Bosnia 3 Mar 1992 (row 1992), Czech Republic 1 Jan 1993 (row 1992). New keyframes fill the gap years (romania_1989, federated-republic-of-germany_1990, republic-of-bulgaria_1990, bosnia-and-herzegovina_1994) and czech-republic_1992 is an `adjust` that moves the shape to 1993.
- Shared Wikidata ids (Romania Q203493, Bulgaria Q121932, Albania Q467864): kept as separate dossiers per Cliopatria row, the same choice the other eu-22 part made for Albania. Cell counts of predecessor and successor shapes are identical (Albania 96, Bulgaria 399, Romania 903), so the orchestrator may merge the colours (family balkans).
- Living states end in 2024 (the last Cliopatria year), as the Turkey dossier does; the schema says the current year.
- Living-state dossiers have no `dissolve` event; the validator does not warn.

## bosnia-and-herzegovina (5 of 5 pages)
- Cliopatria's 1992-1995 shape (13,439 km2, 26% of the infobox 51,209 km2) is read as the government-held land; the Dayton page's 13,955 km2 under Bosniak control is the same order. The rest is expressed as contest zones against `republika-srpska` (April 1992 to November 1995, gain on 14 December 1995) and `croatian-republic-of-herzeg-bosnia` (1993 to March 1994, gain March 1994). Neither has a dossier: they belong to eu-22-x ("the Yugoslav war fronts and the Dayton entities").
- Not settled: year-by-year front lines (Serbs about 70% in 1992, 49% at Dayton), the Autonomous Province of Western Bosnia (not on the Bosnian War page), the Brcko arbitration (only 'created in 2000'), Croatian and Yugoslav roles, the Herzeg-Bosnia territory beyond three cantons.
- Gazetteer: the Natural Earth entity names are spelled 'Repuplika Srpska' and 'Federacija Bosna i Hercegovina'; the dossier uses them as they are.

## czech-republic (2 of 2)
- The Sance (to Slovakia) and Sidonie (to the Czech Republic) awards of 1997 and the 1996 border treaty are on the Dissolution page without coordinates; left out of the ledger as sub-cell.
- Czechoslovakia's Cliopatria row ends 1991, so 1992 has no Czechoslovak shape; the czechoslovakia dossier (eu-21) should carry its last shape to 31 December 1992. Slovakia (Q33946 shared with Czechoslovakia) is another part's.

## federated-republic-of-germany (2 of 2)
- 1990 will show the FRG, the GDR and this dossier unless the renderer cuts at the month; the FRG and GDR dossiers should end October 1990.
- Capital: Bonn 1990-1993 is my reading (the page gives no capital for those years); Berlin from the Berlin/Bonn Act of 1994, relocation 'completed in 1999' (the reunification page says 2000).
- The Polish border treaty (signed 14 Nov 1990, in force 16 Jan 1992) and the Two Plus Four Treaty (in force 15 Mar 1991) are in `certainty` and the found note, not events.

## romania (2 of 2)
- The pages read are silent on Snake Island and the ICJ Black Sea delimitation (2009), the Ukraine treaty, the Moldovan and Serbian frontiers.

## republic-of-bulgaria (2 of 2)
- The pages read are silent on border treaties after 1990. The People's Republic page gives the renaming (15 Nov 1990) and the July 1991 constitution.

## republic-of-albania (3 of 5)
- The History of Albania page loaded only to 1941 (even with an offset), so the 1990 collapse and March 1991 elections are undated; the Albania infobox gives 29 April 1991.
- The 1997 rebellion: loss of the south to `nobody` in March 1997 (confidence 2), Berat regained 3 April (2), the rest bridged to August 1997 at confidence 1 (the page dates no restoration in the south).
