# Notes for batch me-10-k (Ottomans and the modern Middle East, part k)

Written by the Phase B agent on 2026-10-25. Five dossiers were written for the six owned states, from 18 pages opened with WebFetch in this run (4 further guessed titles failed). All five validate (python3 -I history/tools/validate_dossier.py). Read this first, then the `notes` field of each dossier.

## Rows merged, split or left for other batches

- **ba-athist-syria has no dossier of its own.** Its Cliopatria Name "Ba'athist Syria" (1963-1966) and "Republic of Syria" (1961-1962) share Wikidata Q858 and the same 52-cell shape, so `republic-of-syria` carries both Names (`cliopatria_names`) and reviews both shapes, as the brief says for shared ids. The slug `ba-athist-syria` should be treated as an alias of `republic-of-syria` by the colour and compile steps.
- **The Syrian state is one state across five Cliopatria rows**: Second Syrian Republic (me-10-i, 1946-1957), UAR (Syria part, 1958-1961), Republic of Syria + Ba'athist Syria (1961-1966, this batch), Arab Socialist Ba'ath Party (1967-1972, this batch, kept as its own dossier because it has its own Wikidata id Q16243030), Syria (me-10-l, 1973-2024, whose Wikidata Q41137 is Assyria's and wrong). The 1963 coup page's infobox says the coup was the "Fall of the Second Syrian Republic", so 1961-1963 is the restored Second Republic, not a new state. colours.json already gives republic-of-syria, ba-athist-syria and arab-socialist-ba-ath-party one hex; the other two Syrian rows have different hexes.
- **iraqi-republic and republic-of-iraq (me-10-m) are one state** (Q796). I did not take the later row's two shapes (they belong to another batch), so iraqi-republic ends at the row boundary 2005 with a confidence-1 dissolve; Cliopatria has no Iraq row for 2006-2013, so `republic-of-iraq` must start in 2005/2006 or the gap-filler must join the two. Colour: one hue for both.
- **state-of-kuwait and kuwait (me-10-d) are one state** (Q817), with Cliopatria rows missing for 1873-1960 and 1990. The earlier slug is `kuwait`; I kept `state-of-kuwait` separate because the brief owns it. colours.json gives them different hues; they should share one. State-of-kuwait ends in February 1991 and the `kuwait` row's 1991 shape governs the whole of 1991.
- **united-arab-republic** ends in September 1971 (rename to Arab Republic of Egypt, 2 or 11 September per the page), but Cliopatria's UAR row runs to 1972 and its Arab Republic of Egypt row starts in 1973. **1972 has no row**; arab-republic-of-egypt must start in September 1971, or the 1972 shape of the UAR must be kept by the gap-filler.

## Cliopatria rows that are wrong

- UAR 1960-1966 keeps Syria inside the shape after the coup of 28 September 1961 (verdict adjust for 1960, new keyframe 1962-1966 for Egypt alone, less the Gaza Strip). The Syrian rows of the same years overlap it.
- Iraqi Republic starts in 1960 and its Arab Federation row (me-10-j) covers Iraq and Jordan in 1958-1959: new keyframe 1958-1959 for Iraq alone from 14 July 1958.
- The Iraqi 1960-1989 shapes lack Iraq's share of the Saudi-Iraqi neutral zone (22 cells at about 29.1-29.5 N, 44.2-46.4 E, which Cliopatria adds only in 1991); the pages date the division to 1982 (agreement 26 December 1981, divided between 28 January and 30 July 1982; an administrative division in 1975). The Saudi dossier already enters the other half in 1982 with counterpart nobody; the Iraqi gain uses the same.
- The Iraqi 1983 and 1987 cuts (four cells east of Basra; three Kurdish-border and two marsh cells) are only partly explained by the pages (Haj Omran 23 July 1983, Dawn 4 September 1983, Majnoon Island February 1984; "no permanent border changes" at the cease-fire of 20 August 1988). The 1987 shape is limited to 1987-1988 and a 1989 keyframe returns the pre-war line.
- Kuwait 1961-1972 lacks Kuwait's half of the Saudi-Kuwaiti neutral zone (13 cells), partitioned from 25 July 1966 (agreement 7 July 1965; demarcation formal 18 December 1969; ratified 18 January 1970), not 1973.
- Iraq 1990 is the 1991 shape plus exactly the 62 Kuwait cells; Kuwait is drawn as occupied land (hatched), not Iraqi, and the Iraqi keyframe cuts it out.
- Iraq 1991-2005 is a full Iraq; the Kurdistan Region (Erbil, Sulaymaniyah, Duhok) was de facto outside Baghdad's control from 1992 to the constitution of 15 October 2005: new keyframe 1992-1999, adjust for 2000-2005, a loss (May 1992) and a gain (October 2005) with the counterpart `kurdistan-region`.

## Pages that would not load

- https://en.wikipedia.org/wiki/Saudi%E2%80%93Kuwaiti_neutral_zone, https://en.wikipedia.org/wiki/Divided_Zone, https://en.wikipedia.org/wiki/Kuwait%E2%80%93Saudi_Arabia_neutral_zone and https://en.wikipedia.org/wiki/Iraq%E2%80%93Saudi_Arabia_neutral_zone returned url_not_found (guessed titles). They were replaced by the Kuwait-Saudi Arabia and Iraq-Saudi Arabia border pages and then by the titles the Saudi dossier uses (Saudi_Arabian-Kuwaiti_neutral_zone, Saudi_Arabian-Iraqi_neutral_zone), which loaded.

## Gaps left (page budget or page silent)

- Iraq: the 2003-2004 occupation under the Coalition Provisional Authority (rule 4 hatch); the Iran-Iraq War's al-Faw (1986), Halabja (1988) and Basra front, which the war page does not cover; the land moved by the 1993 UN Iraq-Kuwait demarcation ("minor adjustments", no land named); the 1991 Shi'ite uprising in the south; the heads of state.
- UAR: Egypt's role in Yemen after 1961 and the Egypt-Libya border (no page opened); Egyptian control of Gaza before 1959; the `occupation_end` of the Sinai occupation (belongs to arab-republic-of-egypt; the UAR page gives 1978 for partial sovereignty).
- Syria: the border incidents and "War over Water" of the early 1960s (undated on the Golan page); the 1966 coup page; the September 1970 Syrian intervention in Jordan.
- Kuwait: the heads of state (Abdullah III and Sabah III are undated on the Kuwait page); Bubiyan and Warbah (only a 1932 mention on the Iraq-Kuwait border page).

## Associations, not territory (umbrella dossiers wanted)

- United Arab States (Egypt, Syria, Mutawakkilite Kingdom of Yemen), 1958-1961, a "loose confederation" per the UAR page.
- Federation of Arab Republics (Egypt, Libya, Syria), referendums 1 September 1971, established 1 January 1972, ended 19 November 1977; three capitals, no territory of its own.

## Counterparts that need a dossier

- `kurdistan-region` (Kurdistan Regional Government, de facto state 1992-2005, federal region after): counterpart of two Iraqi events.
- `kingdom-of-great-britain` is used as the counterpart for the United Kingdom in Kuwait's founding (the seed's neighbour slug); the eu-11 group is creating `united-kingdom` for the years after 1800.

## Gazetteer names the resolver lacks

Region: Halaib Triangle (20,580 km2, disputed between Egypt and Sudan; the 1899 line on the 22nd parallel against the 1902 administrative boundary). Places: Mehran (taken by Iraq in September 1980 'on the central front', Iran), Haj Omran (an Iraqi town Iran took on 23 July 1983 with Kurdish support), Majnoon Island (Iraq, in the marshes Iran held from February 1984).
