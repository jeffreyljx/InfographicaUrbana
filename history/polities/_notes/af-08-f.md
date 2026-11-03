# Notes for batch af-08-f (Partition and independence, part f)

Written 2026-10-20. Six owned dossiers (republic-of-tunisia, ghana, democratic-republic-of-the-congo, federal-republic-of-somalia, guinea, madagascar) and three rebel dossiers the DRC needs (state-of-katanga, south-kasai, free-republic-of-the-congo). All nine validate with 0 errors; `--resolve` leaves no unknown region names. WebFetch returns a model's summary of the page, so a few dates (Tunisia's republic 25 July 1957, Ghana's republic 1 July 1960) are the summary's reading of the infobox and are said so in the notes of the events.

## Decisions the integrator needs

- ZAIRE ROW. Cliopatria draws one state as 'Democratic Republic of the Congo' 1960-1972 and 1996-2024 and as 'Zaire' 1973-1995 (same Seshat id cg_congo_democratic_rep). The DRC dossier covers 1960-2024 with the 1973-1995 years as a new keyframe pointing at the Zaire shape and rename events in 1971 and 1997. 'Zaire' is NOT in its cliopatria_names. If another af-08 part writes a 'zaire' dossier, keep one of the two.
- WIKIDATA COLLISIONS. Q974 (DRC and republic-of-the-congo) and Q983 (guinea and equatorial-guinea) are Cliopatria errors: the pages show different states. No merges; each state keeps its own dossier. Both dossiers keep the id Cliopatria gives.
- OVERLAPS TO RESOLVE in other groups' rows: british-gold-coast (1943-1959 and a 1960 shape, a 1.19 M km2 composite across Nigeria, Ghana, Cameroon) still covers Ghana after 6 March 1957; the French Fifth Republic row (1958-) holds Guinea in 1958-1959 (independent 2 October 1958) and perhaps Madagascar until 26 June 1960; french-africa carries Tunisia until 1956; the Somalia shape contains Somaliland through 2024.
- Matching events other dossiers should carry: loss of Tunisia (20 March 1956, counterpart republic-of-tunisia) in french-africa; loss of Guinea (2 October 1958) and Madagascar (26 June 1960) in french-fifth-republic; Bizerte (15 October 1963) in french-fifth-republic; loss of British Togoland to Ghana (6 March 1957); loss of Italian and British Somaliland (July 1960) in italian-africa and british-africa; belgian-congo already records the 1960 split.
- REBEL DOSSIERS WRITTEN HERE (type rebel, cliopatria_names []): state-of-katanga (11 July 1960 - January 1963), south-kasai (9 August 1960 - 5 October 1962), free-republic-of-the-congo (12 December 1960 - 16 January 1962). The DRC ledger carries the matching losses and gains, so they must stay together. If af-08-x also writes Katanga, keep one file and keep the DRC counterpart slug.

## republic-of-tunisia (6 shapes; 5 pages incl. one empty)

Six shapes 1956-2024 all within 0.1 percent of 151,479 km2 (infobox 163,610, ratio 0.93): grid noise, all verdict ok. Events: independence 20 March 1956, republic 1957 (rename), Bizerte crisis 19 July 1961 - 15 October 1963 (contest and gain, France). 'History of Tunisia' returned text that ends in the Aghlabid period, so nothing is cited from it. Algeria border: French decrees of 1888-89 and 1901, southern sections 1911-23, confirmed by an agreement of 6 January 1960; Libya border: treaty of 19 May 1910; ICJ 1982 sea decision. No ruler strip (the page does not date Marzouki or Essebsi). Sakiet 1958 and Gafsa 1980 were not on the pages opened. The French protectorate of Tunisia has no dossier (needed).

## ghana (4 shapes; 3 pages)

Row starts 1958 but independence was 6 March 1957: new keyframe 1957. British Togoland joined at independence (plebiscite 9 May 1956, 58 percent; union with effect from midnight 6 March 1957; the Gold Coast page's infobox has 11 December 1956 for the incorporation). Republic 1 July 1960. Area 240,673 against 239,567 km2 in the text (the page also has 240,000 and 238,540). No war or border change after 1957 on any page, so wars is empty. British Togoland needs a dossier.

## democratic-republic-of-the-congo (6 shapes + new 1973-1995 keyframe; 5 pages for the state, 1 more for the rebels)

Keyframes are the de jure country (2.31 M km2 against 2.35 M infobox, ratio 0.98); secessions are ledger loss/gain events (rule 5). Dated: independence 30 June 1960; Katanga 11 July 1960 - 17 January 1963; South Kasai 8/9 August 1960 - 5 October 1962; Stanleyville government December 1960 - January 1962; Simba rebellion July - November 1964 (contest only; towns, not extents); Zaire 1971; First Congo War 24 October 1996 - 16 May 1997; renaming May 1997; Second Congo War 2 August 1998 - 18 July 2003. Weak spots: the Sankuru gain (undated, confidence 1); the Simba and Second Congo War zones (the pages give towns and 'the eastern provinces', no map); the MLC's north (not named, not drawn). Not covered at all: the Shaba invasions of the 1970s, the Kwilu rebellion's zone, the Ituri conflict, the M23 occupation of Goma in 2012 (page: year only) and the 2025 M23 conquests (after 2024). Counterparts still needing dossiers: the People's Republic of the Congo (Simba rebels, 1964), AFDL (1996-1997), RCD and MLC (1998-2003).

## federal-republic-of-somalia (2 shapes; 2 pages)

Shape is the union of the two Somalilands (646,088 km2 against 637,657, ratio 1.01) and contains Somaliland to 2024; the 1991 loss event is the correction. Ogaden War as a contest July 1977 - March 1978 with ethiopia. The rename to the Somali Democratic Republic is undated on the page (confidence 1, year 1969 is the coup's). Not on the pages: Ethiopia's 2006 invasion extent and end; the Northern Frontier District transfer date. Somaliland and British Somaliland need dossiers; Puntland (1998) and Jubaland are member states inside Somalia and are not losses.

## guinea (2 shapes + new 1958-1959 keyframe; 2 pages)

Row starts 1960; independence 2 October 1958. Area 245,676 against 245,857 km2. Operation Green Sea (21-22 November 1970) held no ground. No border change or dispute after 1958 on the page. Ruler strip written from the page's narrative (Beavogui, Konate and Conde's start are year-level readings).

## madagascar (2 shapes; 1 page)

Whole island both shapes, 616,267 against 592,796 km2 (ratio 1.04). Start follows Cliopatria and sovereignty (26 June 1960); the autonomous Malagasy Republic of 14 October 1958 is a note. The Scattered Islands dispute is not on the page. No war. Only one page opened (budget 1-2); a second would be 'Scattered Islands in the Indian Ocean' for the claims.

## Gazetteer

No unknown names after `--resolve`. Places used with radii: Bizerte, Mbuji-Mayi, Kisangani, Isiro, Lisala, Kindu, Kalemie, Bukavu, Lodja, Manono, Lubumbashi; admin1: Katanga, Orientale, Nord-Kivu, Sud-Kivu, Maniema, Volta (Ghana); countries Somaliland and Somalia; region Ogaden. The modern names for the colonial towns of the Simba page (Port-Empain, Paulis, Albertville) are the researcher's identification.
