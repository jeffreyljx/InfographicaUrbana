# Review: batch me-10-i (2026-10-25)

Adversarial review of kingdom-of-saudi-arabia, lebanon, kingdom-of-iraq and second-syrian-republic. The machine copy is history/notes/phase-b/reviews/me-10-i.json. Neighbour dossiers found: north-yemen, sultanate-of-oman, united-states-of-america, british-africa and mujahideen, plus ottoman-empire for Iraq's predecessor. All other Context polities (state-of-israel, kingdom-of-jordan, syria, kuwait, iraqi-republic, kingdom-of-hejaz-and-nejd, french-mandate-for-syria-and-lebanon, kingdom-of-great-britain and the rest) are not written yet; their mirrors count as exceptions.

All four dossiers validate with 0 errors before and after the fixes. lebanon keeps 2 warnings, for occupations (Ghajar 2006, the invasion of October 2024) that end after 2024.

## Verdicts

- kingdom-of-saudi-arabia: **thin**. The reviewer applied three fixes. The largest move, the Rub' al Khali in 1936 (about 262,000 km2), is still at confidence 1.
- lebanon: **fix**. Two region fixes applied by the reviewer.
- kingdom-of-iraq: **fix**. Two fixes applied by the reviewer.
- second-syrian-republic: **fail**. Back to the author: the 1948-1949 events draw the wrong land, and the 1946-1948 keyframes are misread.

## kingdom-of-saudi-arabia (fixes applied)

1. /ledger/4 (and /ledger/3): the 1934 gain from north-yemen named Jizan, Asir and Najran. The Saudi-Yemeni war (1934) page says Asir 'in 1930 ... was incorporated into the Nejd and Hejaz Kingdom' and that 'Asir and Jizan were both part of the Idrisid Asir emirate during the 1920s'. Only Najran (captured 21 April 1934) changed hands, so the region is now Najran.
2. /ledger/8-9: the owner of Hamasa is Oman. The Buraimi dispute page calls it 'one of three Omani villages in the oasis'. The counterpart is now sultanate-of-oman (was trucial-states), and the Buraimi war's belligerent sultanate-of-muscat-and-oman (a row that ends in 1946) is now sultanate-of-oman.
3. /ledger/14: the counterpart is now nobody (was iraqi-republic). kingdom-of-iraq gives the neutral zone to nobody in 1922, and the zone page says no military or permanent buildings were allowed in it.

Thin (for a gap-filler):
- The 1936 Rub' al Khali claim needs an act and a year.
- Keyframes 12-13 keep 26 cells in Oman and 26 in Yemen that the treaties of 1990 and 2000 settled the other way. Make them adjust from 1990 (Oman side) and 2000 (Yemen side).
- The Battle of Khafji (Iraqi hold, 29 January to 1 February 1991) needs an occupation pair.
- The al-Wadiah war of 1969, the Treaty of Jeddah of 1974 (Khor al Udaid, Sabkha Matti) and the Qatar border agreements are missing.

Spot checks: the Taif date, the 7 July withdrawal, Buraimi (31 August 1952, 25 October 1955), Jordan (9 August 1965, 18 km of coast), the Kuwait zone (7 July 1965, 25 July 1966) and the Iraq zone (1981-1982) were all confirmed on the cited pages. Area: infobox 2,149,690 km2 against Cliopatria's 1,929,173 km2 (0.90); acknowledged.

## lebanon (fixes applied)

1. /ledger/1, /ledger/3 and /wars/0/zones/1: the 1948-1949 Israeli occupation was drawn as the South Lebanon and Nabatiyeh governorates, 'south of the Awali and the Litani'. No page says this. The armistice page names only the 13 villages Israel left. The region is now the border strip, two cells deep.
2. /ledger/18 and /wars/6: the invasion of 1 October 2024 was drawn as the same two governorates. The 2024 Israeli invasion of Lebanon page names border villages (Kafr Kila, Ayta ash Shab, Meiss Ej Jabal, a hill in Chamaa), a ceasefire on 27 November 2024 and a withdrawal deadline of 26 January 2025. The region is now the border strip, one cell deep, with that page as source (added to sources[]).

Thin:
- admin1 Mount Lebanon (/ledger/8, /ledger/11) overstates the 1982-1983 hold, which was the Chouf, Aley and Baabda.
- The 1978 occupation south of the Litani, March to June, is drawn only as the strip.
- The Syrian offensive of October 1976 took 'all of central Lebanon' (Syrian occupation page), outside the North and Beqaa region used.
- The Malkiyya cells of 1946-1947 and the 2014 cell are unverified.

Spot checks: 1948 southern Lebanon, the armistice of 23 March 1949, the Syrian entry of 31 May 1976, the Syrian withdrawal of 30 April 2005 and October 2024 were all confirmed. The text of /ledger/2 runs together the ALA crossing of 15 May and the Lebanese army's action of 5-6 June; this is harmless. Area: infobox 10,452 km2 against Cliopatria's 9,684 km2 (0.93).

## kingdom-of-iraq (fixes applied)

1. The rename of 3 October 1932 is now an occupation_end with kingdom-of-great-britain, and an occupation_start of 23 August 1921 was added (confidence 2). The name never changed, and the group scope draws mandates as occupations. The ledger now has two occupation pairs: 1921-1932 and 1941-1947.
2. /wars/2 had empty zones although the Iraqi force held the Nablus-Jenin-Tulkarm triangle until March 1949. The zone is now a 30 km radius around Nablus.

Thin:
- The occupation of the Samaria triangle (late May 1948 to March 1949) needs a ledger pair (counterpart palestinians or kingdom-of-jordan).
- The 1937 frontier treaty with Iran.

Note: kingdom-of-great-britain is the slug every dossier uses for Britain (22 events). The brief splits it at 1801, so eu-11's new United Kingdom slug should replace it for 1921-1947 once named.

Spot checks: 23 August 1921, Lausanne on 4 February 1923, the Frontier Treaty of 1926 (no month on the page), Uqair on 2 December 1922, 2-31 May 1941 with 'British occupation of Iraq until 1947', and 14 July 1958 were all confirmed. The infobox has no area (confirmed).

## second-syrian-republic (fail, not applied)

1. /ledger/1-4 and /wars/0: the contest and occupation region is the Sea of Galilee plus the cells Cliopatria adds to Syria in 1949. Those five H3 cells are centred at 33.23N 35.83E, 33.10N 35.71E, 32.82N 35.66E, 32.95N 35.78E and 32.44N 36.37E (grid.py polity_cells 1949 minus 1948). That is the Golan and the Hauran, Syrian land under the mandate. The region misses Mishmar HaYarden (about 33.00N 35.60E, west of the Jordan), which the 1948 war page says Syria overran on 10 June 1948. Redraw it as the ground west of the international border, for example a 10 km radius around Mishmar HaYarden. Do not use country Israel or Galilee: the gazetteer puts the Golan inside both.
2. Keyframes 0-2: the occupation_end of July 1949 covers the same cells that keyframe 2 (ok) then draws as Syrian. The land was Syrian throughout, so the 1946 and 1947 shapes lack them. Make keyframes 0 and 1 adjust: {union [Second Syrian Republic 1946|1947, minus [SSR 1949, SSR 1948]]}. Rewrite the keyframe 2 note: the armistice's 66 km2 is below cell size.

Spot checks: 17 April 1946, 15 May 1948, 10 June 1948, 20 July 1949 and 1/22 February 1958 were all confirmed. Area: infobox 189,880 km2 against Cliopatria's 187,924 km2 (0.99).

## Cross-dossier routing

- north-yemen /ledger/8 (1934 loss): narrow it to Najran, because Asir and Jizan were Saudi from 1930.
- sultanate-of-oman /ledger/20, /ledger/23: add an occupation pair for Hamasa, 1952-08 to 1955-10, with kingdom-of-saudi-arabia; Oman now carries only a contest.
- iraqi-republic: its half of the neutral zone in 1982 is a gain from nobody.
- kingdom-of-jordan, kuwait, kingdom-of-hejaz-and-nejd, state-of-israel and syria (all me-10, not yet run): the author's notes list the reverse events each should carry.
