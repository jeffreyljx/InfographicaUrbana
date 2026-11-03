# Review: batch eu-14-i (Greenland), 2026-10-25

Reviewer: adversarial review, Phase B. One dossier: history/polities/greenland.json.

Verdict: **thin** (valid, honest, three small fixes applied by the reviewer; the largest border moves rest on Cliopatria's dates at confidence 1, within a spent nine-page budget).

## Mechanical
- `validate_dossier.py --resolve`: valid, 0 errors, 3 warnings (unknown places Qeqertarsuatsiaat, Aasiaat, Nanortalik); Maniitsoq and Saqqaq are also absent from the gazetteer (they sit in the same union region as Aasiaat). Re-validated after the reviewer's edits: valid, 0 errors.
- All 24 Cliopatria shapes of "Greenland" have a verdict; 4 new keyframes (1721, 1933, 1941, 1945) carry from, to and a correction. No known-bad row for Greenland in data/README.md.
- found 1721 = start, dissolve 1953 = end; capitals contiguous (1721-1727, 1728-1953); certainty covers 1721-1953; the 1931 contest_start sits in the Eastern Greenland war's zone and pairs with the 1933 contest_end.

## Fixes applied by the reviewer (applied: true)
1. `/ledger/24` (1917 gain): counterpart `united-states-of-america` changed to `nobody`, with a sentence added to the note. The Qaanaaq page says the US "abandoned its territorial claims in the area in 1917 in connection with the purchase of the Virgin Islands"; History of Greenland says it "agreed to relinquish all claims on Greenland". The US held no land, its dossier has no 1917 loss, and the same Thule coast is already gained in 1910 (`/ledger/23`).
2. `/wars/1/belligerents`: `denmark-norway` (ended 1814) replaced by `kingdom-of-denmark-1814-1940` for the 1931-1933 Eastern Greenland dispute.
3. `/wars/0/belligerents`: free text "the Dutch" replaced by the slug `dutch-republic` (History of Greenland: Severin "repulsed the Dutch at the Battle of Jacobshavn in a series of skirmishes in 1738 and 1739").

## Advisory (not blocking, not applied)
- The 1814 and 1940 `rename` events record a change of metropole and of government, not of name; the vassal_end/vassal_start pairs already carry both. They are harmless for colour, but the author may drop the 1940 one.

## Spot checks (7 pages opened)
- `/ledger/1` 1721 colonization: Greenland infobox "Danish-Norwegian resettlement and colonization: 1721". Confirmed.
- `/ledger/19` 14 Jan 1814: Greenland infobox "Unification with Denmark: 14 January 1814"; "Greenland was transferred from the Norwegian to the Danish crown". Confirmed. `/ledger/20`: History of Greenland "The colonies, including Greenland, remained in Danish possession". Confirmed.
- `/ledger/26` June 1931: Erik the Red's Land, Devold "raised the Norwegian flag at Myggbukta" in June 1931; proclamation 10 July 1931, Carlsberg Fjord to Bessel Fjord, 71°30' to 75°40'N. Confirmed.
- `/ledger/27`, `/ledger/28` April 1933: infobox "Territory awarded to Denmark: 5 April 1933". Confirmed (the Eastern Greenland Case reference list says 5 September 1933 but its link URL holds 1933.04.05; April stands).
- `/ledger/31` 9 April 1940: Greenland page "Greenland's connection to Denmark was severed on 9 April 1940". Confirmed.
- `/ledger/32` 9 April 1941: Greenland in World War II, Kauffmann "signed an executive agreement with Secretary of State Cordell Hull" on 9 April 1941 making Greenland "a protected state of the United States". Confirmed.
- `/ledger/36` 1953: Colonial Greenland "In 1953, Greenland's colonial status was ended". Confirmed.
- Colony foundation years (`/ledger/3,5-11,13-15,17`): Colonial Greenland list Christianshåb 1734 ... Julianehaab 1774, Nennortalik 1797. All confirmed.
- `/ledger/24` 1917: year confirmed (Qaanaaq); counterpart fixed (above). `/ledger/29` 1936: the Eastern Greenland Case page does not date 1936, as the note says (confidence 1 honest).

## Area
Greenland infobox 2,166,086 km2 (the island); Cliopatria greenland_1936 / _1940 2,219,796 km2; ratio 1.02, acknowledged in /keyframe_review/24. The colonial coastal shapes (10,964 to 170,640 km2, 1734-1935) are acknowledged against the island's area in /keyframe_review/1.

## Thin (for a gap-filler)
- `/ledger/29` 1936 gain of about 2.05 M km2 (the interior and the unsettled coasts; 93 percent of the dossier's maximum) rests on Cliopatria's date. The Danish claim to the whole island (Ihlen Declaration 1919, the 1921 Danish declaration, the US renunciation of 1916/1917, the 1933 judgment with its critical date of 10 July 1931) suggests 1921 or 1933. Pages to try: Treaty of the Danish West Indies; Legal Status of Eastern Greenland under another title; Royal Greenland.
- `/ledger/23` 1910 Thule gain (confidence 1) against the Qaanaaq page's "Denmark assumed control of the village in 1937". Page to try: Knud Rasmussen, Thule trading station.
- `/ledger/4` 1738, `/ledger/12` 1769, `/ledger/16` 1788, `/ledger/22` 1908: Cliopatria steps at confidence 1 (1908: possibly the Danmark expedition 1906-08).
- `/keyframe_review/21` 1924 (+9,300 km2 around Disko Island), `/keyframe_review/19` 1915 and `/keyframe_review/20` 1922 (east coast near 66N): no event. `/keyframe_review/4` 1744: +94 cells 62.0-65.5N, wider than the 1742 Frederikshåb radius.

## Cross-dossier matrix
- 1721 vassal_start denmark-norway: **missing** in denmark-norway (its ledger names Greenland only in the 1814 note "Excepted"). Route to the denmark-norway group.
- 1814 vassal_end denmark-norway: **missing** in denmark-norway.
- 1814 vassal_start kingdom-of-denmark-1814-1940: **missing** (its 1814 found note mentions Greenland; no vassal event). Route to that dossier's group.
- 1940 vassal_end kingdom-of-denmark-1814-1940: **missing**.
- 1941 vassal_start united-states-of-america: **matched** (US /ledger/100, April 1941).
- 1945 vassal_end united-states-of-america: **matched** (US /ledger/114, May 1945).
- 1945 vassal_start / 1953 vassal_end denmark; 1953 dissolve to denmark: exception, Cliopatria row Denmark (1945-2024) has no dossier yet (group not run).
- 1931 contest_start, 1933 contest_end, 1933 gain kingdom-of-norway: exception, kingdom-of-norway has no dossier yet (group not run). Its owner should end the Erik the Red's Land zone in 1933, not 1935.
- 1917 gain (now nobody): exception after fix.
- 20 other gains from nobody: no mirror needed.
- canada (context): neither dossier records an event against the other; contact only across Nares Strait. No mismatch.

## Gazetteer names needed
Maniitsoq, Aasiaat, Saqqaq, Qeqertarsuatsiaat, Nanortalik (places, Greenland west and south coasts).
