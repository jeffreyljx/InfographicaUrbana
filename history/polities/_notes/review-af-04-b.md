# Review af-04-b (2026-10-19): republic-of-liberia

Reviewer: adversarial review, Phase B. One dossier. Verdict: **thin** (valid, honest, every keyframe change has a ledger event and every spot-checked event is on its page; but the event that moves the most land is confidence 1, two events are confidence 1, and the civil-war land and the early growth are not covered). No fixes applied; nothing blocking.

## What I tried
- Validator `--resolve`: 0 errors; 5 warnings, all expected: counterpart `republic-of-maryland` has no dossier (listed by the author), and "Parrot's Beak" not in the gazetteer (4 uses).
- Years: ledger sorted 1822..1980; `found` at 1822 (month 1, infobox 7 January 1822); no `dissolve` (alive 2024); certainty 1822-1884 / 1885-1910 / 1911-2024, contiguous; wars inside the life; capital Monrovia (-10.8, 6.31) inside every shape.
- Identity: type state, family `africa` (a key of colours.json), `cliopatria_names` = the one polities.csv row; all 6 Cliopatria shapes have a verdict; the 6 new keyframes carry from/to/correction. Rulers omitted (allowed; said so).
- Keyframe walk (geometry computed from features.pkl): 1848 to 1885 Cliopatria drops 4 pieces on the Guinea side (largest lon -10.5..-9.37, lat 7.95..8.58, next to Sierra Leone's north-east, which fits the Sierra Leone border page's "ceding a sizeable strip of territory to France ... shortened the Liberia-Sierra Leone boundary"); 1885 to 1895 drops the strip east of the Cavalla (lat 4.86..7.43); 1942 vs 1943 is a scatter of slivers on the Guinea and Ivory Coast lines (artefact, as the author says). The author's 1892 (Cavalla cells), 1903 (Beak in), 1907 (northern fringe out) and 1911 (Beak out) events explain each new keyframe; the 1857 Maryland gain explains 1848 -> 1857; the 1842 gain explains 1822 -> 1842.
- Area: infobox "43,000 sq mi (111,370 km2)", no year; Cliopatria 2024 shape 99,563 km2; ratio 0.89; acknowledged in keyframe notes. 1848 shape 101,997 km2 (0.92).
- Spot checks (5 pages, all opened): 1847 independence (c3), 1980 coup (c3), 1911 Parrot's Beak cession (c3), 1857 Maryland annexation, 1892 Cavalla treaty, 1907 treaty, 1903 extension, 1842 merger, 1838/1839 Commonwealth, 1822 settlement: every quote is on its page with its year. No fabricated or mis-dated event.
- Cross-checks: no counterpart dossier exists yet (british-africa, french-africa: af-08 not run; republic-of-maryland: listed as needing a dossier). The United States dossier (am-07-c) removes the Liberia cells from its 1822-1847 keyframes as not US land, which agrees with this dossier's `found` from nobody in 1822. No other dossier mentions republic-of-liberia.

## Thin: for a gap-filler
1. `/ledger/2` (1842 gain, confidence 1): the largest move in the dossier (about 95,000 km2, from the 40 km Monrovia core to Cliopatria's 1848 outline without Maryland County). The page gives only "By 1842, four out of the aforementioned five colonies were incorporated into Liberia"; which colonies, when, and how far inland is unknown, and the hinterland to 8.5 N is Cliopatria's later claim. The region also re-gains the 1822 core (harmless overlap). Try Mississippi-in-Africa and Kentucky in Africa.
2. `/keyframe_review/0` and `/ledger/1`: the 1822-1841 keyframe is a fixed 40 km radius for twenty years, but the History page says "The first colony on Cape Mesurado was extended along the coast as well as inland, sometimes by use of force" and "In 1838 the former four settlements came together to create the Commonwealth of Liberia"; the 1838/1839 merger is recorded only as a `rename`, not as a gain. Cliopatria (inside its US rows) draws growth 29 -> 93 -> 192 -> 284 -> 501 cells over 1822-1840. A dated gain for 1838/1839 (Bassa Cove and the other merged settlements) and for Sinoe (Mississippi-in-Africa) would replace the single 1842 jump.
3. `/ledger/6` (1903 gain of the Parrot's Beak, confidence 1): the Liberia-Sierra Leone border page says only that the Mano boundary "was then extended further northwards by mutual agreement in June 1903"; it does not say the Beak became Liberian then, or from whom. Try Kailahun District.
4. Missing 1911 gain: the same page says Liberia ceded the Beak "in exchange for territories east the Mano river"; no gain is drawn (no extent). Try Kailahun District, Mano River.
5. Missing pre-1911 loss on the Sierra Leone side: the Liberia page says British pressure "led to a loss of Liberia's claims to extensive territories" and "Both Sierra Leone and the Ivory Coast annexed territories" (late 19th century, undated); the author's notes say the Liberia page has nothing on borders, which overlooks this sentence. Cliopatria never draws the coast west of the Mano as Liberian, so no keyframe is affected; a claim-loss event (the Gallinas coast, recognised by the treaty of 11 November 1885) needs a page. Try Sierra Leone Colony and Protectorate.
6. `/wars/1`, `/wars/2`: zones are empty, but ground did change hands: the war's own outcome quotes "By September 1990, Doe's forces controlled only a small area". Contest events and a rebel dossier for the NPFL ("Greater Liberia", 1990-1997) are needed; LURD and MODEL held much of the country in 2002-2003. Try First Liberian Civil War and Second Liberian Civil War.
7. `/keyframe_review/5` and `/ledger/7`: the 1892-1907 northern strip is Cliopatria's own 1848-minus-1885 fringe; its location is plausible (see above) but its extent is unverified (confidence 2 is right).

## Observations, not faults
- `keyframe_review` lists the Cliopatria 1895 shape after the new 1893/1903/1907 keyframes (ordered by the years it is valid for, 1911-1941); the research brief asks for shape order. Harmless.
- The decision to start in 1822 (not 1848) is consistent with the US dossier's removal of the colony cells; the orchestrator should keep it.
- The 1842 counterpart is free text (the colonization societies' settlements), not a slug; no mirror is expected.

## Gazetteer names needed
- Parrot's Beak (region): the north-eastern salient of Kailahun District, Sierra Leone, between Liberia and Guinea (Koindu); ceded by Liberia to Sierra Leone in January 1911.

## Counterparts needing dossiers
- Republic of Maryland (republic-of-maryland), to 18 March 1857 (author's listing; its start is on no page opened).
- National Patriotic Front of Liberia / "Greater Liberia" (national-patriotic-front-of-liberia), 1989-1997: a rebel that held most of the country; needs a page for its extent before it is written.

## Problems
- None loading pages. The WebFetch extractor limits verbatim quotes to about 125 characters, so long sentences were checked in parts.
