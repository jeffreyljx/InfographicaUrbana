# Review of batch me-10-j (2026-10-25)

Reviewer: adversarial review, Phase B. Dossiers: state-of-israel, kingdom-of-jordan, palestinians, qatar-protectorate, republic-of-egypt, arab-federation. Neighbours read: kingdom-of-saudi-arabia, lebanon, iraqi-republic, united-arab-republic, second-syrian-republic, arab-socialist-ba-ath-party, kingdom-of-egypt, kingdom-of-iraq, gaza-hamas, all-palestine-government, kingdom-of-hejaz, qatar (syria, arab-republic-of-egypt, ba-athist-syria, kingdom-of-great-britain, state-of-qatar, sultanate-of-muscat-and-oman not written yet).

Validator (--resolve): 0 errors in all six, before and after the reviewer's edits; warnings only for the open 2024 events and british-mandate-for-palestine in state-of-israel and palestinians.

Spot checks: about 40 events checked on 17 pages; every confidence-3 event checked says what its note claims with the year. No fabricated or mis-dated event found. Reviewer edits are marked in the notes of the edited events with '[Reviewer me-10-j, 2026-10-25: ...]'.

## state-of-israel: thin

Area: infobox 22,072 km2 (2024), Cliopatria 28,263 km2, ratio 1.28, acknowledged True. Infobox '22,072 or 20,770 km2' excludes the West Bank; the corrections remove the occupied land (1987 note gives ratio 1.37 to 20,770).

Findings:
- `/ledger/7/region; /ledger/8/region` (applied by reviewer): The armistice-exchange regions were bare radii that straddled the 1949 line: the 25 km Hebron disc took 3 cells (about 759 km2) of Israel's own 1949 shape, the 15 km Wadi Ara disc 1 cell (about 253 km2) of the Jordanian-held West Bank. Evidence: 1949 Armistice Agreements page: 'Israel received control in the area known as Wadi Ara and the Little Triangle' 'in exchange for territory in the southern hills of Hebron'; gazetteer resolve: intersect(Al Khalil 25 km, State of Israel 1949) = 3 cells, intersect(35.05/32.45 15 km, West Bank) = 1 cell. Fix: Wadi Ara: intersect(radius, cliopatria State of Israel 1949); Hebron: intersect(Al Khalil 25 km, admin1 West Bank). Mirrored in kingdom-of-jordan /ledger/7-8.
- `/keyframe_review/8-12/correction (union item 2); /ledger/31/region` (applied by reviewer): The gazetteer 'Golan' polygon (10 cells, about 2,529 km2, east to 36.05 E) includes 4 cells (about 1,012 km2) east of Cliopatria's Israel line, so the corrected state drew the Syrian-held third of the Golan as Israeli from December 1981. Evidence: Golan Heights page: 'Civil administration of a third of the Golan Heights, including the capital Quneitra, was restored to Syria' (1974 disengagement); gazetteer resolve: minus(Golan, State of Israel 1987) = 4 cells. Fix: Golan item in corrections 8-12 and the 1981 gain region set to intersect(region Golan, cliopatria State of Israel 1987). The 1967 occupation_start and 1981 occupation_end keep the whole polygon (as the arab-socialist-ba-ath-party mirror does), so the hatch opens and closes on the same region.
- `/ledger/14, /ledger/17, /ledger/20, /wars/2/belligerents` (NOT applied): Counterpart 'arab-republic-of-egypt' for June 1967; Egypt was then the United Arab Republic (dossier written, me-10), whose ledger has occupation_start state-of-israel 1967-6 (Sinai) and dissolves into arab-republic-of-egypt in 1971-9. Evidence: united-arab-republic /ledger/7 and /ledger/8; the author's notes acknowledge the choice. Fix: 1967 contest events and the war's belligerent: united-arab-republic. Sinai: occupation_start united-arab-republic 1967-6, occupation_end united-arab-republic + occupation_start arab-republic-of-egypt 1971-9, occupation_end arab-republic-of-egypt 1982 (non-blocking).
- `/ledger/16, /ledger/19, /ledger/23, /wars/2/belligerents` (NOT applied): Counterpart 'syria' for June 1967; the Golan's owner in 1967-1972 is arab-socialist-ba-ath-party (written), whose /ledger/1 is occupation_start state-of-israel 1967-6. Evidence: arab-socialist-ba-ath-party /ledger/1 and /ledger/3 (dissolves into syria 1972). Fix: 1967 contest and Golan occupation_start: arab-socialist-ba-ath-party; occupation_end arab-socialist-ba-ath-party + occupation_start syria at 1972/1973; 1973 events stay 'syria' (non-blocking).
- `/ledger/21, /ledger/37, /ledger/39` (NOT applied): Counterpart 'palestinians' for Gaza 1967-2005 and the West Bank from 1988, but the palestinians dossier lives 1948-1950 only. Evidence: palestinians identity.end 1950-4; the author lists state-of-palestine and palestinian-national-authority as needed dossiers; united-arab-republic /ledger/4,6 also use 'palestinians' for Gaza 1959-1967. Fix: Re-point once the orchestrator picks the Palestinian owner slug (extend 'palestinians', or state-of-palestine / palestinian-national-authority); no change to dates or land (routing, non-blocking).
- `/keyframe_review/10/note, /keyframe_review/11/note` (NOT applied): The notes call the 2006 growth (+1,602 km2) and the 2014 drop (-1,730 km2) unexplained; the 2006-2013 shape's north bound is 33.52 N against 33.33 N, i.e. Cliopatria carries the 2006 Lebanon occupation (ledger /40-41) to 2013, and 2014 removes it. Evidence: shapes.csv bbox state-of-israel_1987 vs _2006 vs _2014. Fix: Rewrite the two notes to name the 2006 Lebanon War strip (the corrections already exclude it); note-only (non-blocking).

For a gap-filler:
- `(missing) 1948-1949`: Israeli occupation of southern Lebanon, 1948 to 23 March 1949, on a page the author opened ('Israel then invaded and occupied southern Lebanon until the end of the war'); lebanon /ledger/1,3 has it. Try: https://en.wikipedia.org/wiki/1948_Arab%E2%80%93Israeli_War
- `(missing) 1978-1982`: Operation Litani (March 1978) and the border strip held to 1982; lebanon /ledger/6 has occupation_start state-of-israel 1978-3. Try: https://en.wikipedia.org/wiki/1978_South_Lebanon_conflict
- `(missing) 1994-10`: Israel's loss of Naharayim/Baqura and Tzofar/Al-Ghamr to Jordan (mirror of kingdom-of-jordan /ledger/21). Try: https://en.wikipedia.org/wiki/Israel%E2%80%93Jordan_peace_treaty
- `/ledger/33 and /keyframe_review/6`: Staged Sinai changes: Egyptian bridgeheads October 1973, Sinai I (1974) and Sinai II (1975) withdrawals, 1979-1982 stages; only 1982 is dated. Try: https://en.wikipedia.org/wiki/Sinai_Interim_Agreement
- `/ledger/0 and /keyframe_review/0`: 1948 growth beyond the May 1948 holdings (Operations Yoav and Hiram, October 1948); the 1948 shape is the end-of-year extent. Try: https://en.wikipedia.org/wiki/Operation_Yoav
- `/keyframe_review/2`: The 1953 step (-498 km2) has no event (unverified: page budget). Try: https://en.wikipedia.org/wiki/Green_Line_(Israel)
- `(missing) 2006-10`: Ghajar kept after 1 October 2006 (lebanon /ledger/17 occupation_start state-of-israel). Try: https://en.wikipedia.org/wiki/Ghajar

Spot checks:
- `/ledger/5` https://en.wikipedia.org/wiki/1948_Arab%E2%80%93Israeli_War: confirmed: 'On 10 March, Israeli forces secured the Southern Negev, reaching the southern tip of Palestine'; Uvda launched 5 March
- `/ledger/7, /ledger/8` https://en.wikipedia.org/wiki/1949_Armistice_Agreements: confirmed: Jordan agreement 3 April 1949; Wadi Ara and the Little Triangle 'in exchange for territory in the southern hills of Hebron'
- `/ledger/24` https://en.wikipedia.org/wiki/Israeli-occupied_territories: confirmed: 'On June 27, Israel extended its laws, jurisdiction, and administration to East Jerusalem'
- `/ledger/29, /ledger/31` https://en.wikipedia.org/wiki/Golan_Heights: confirmed: 'On 14 December 1981, Israel passed the Golan Heights Law'; Quneitra restored 'the year after the 1973 Yom Kippur War'
- `/ledger/33, /ledger/39, /ledger/41, /ledger/44` https://en.wikipedia.org/wiki/Israeli-occupied_territories: confirmed: Sinai 'Since 1982 ... not regarded as occupied'; Gaza 'completed on 12 September 2005'; Lebanon 'until the 1 October 2006'; 'In December 2024, Israel occupied the UN buffer zone', 235 km2
- `/ledger/20-22, /keyframe_review/5/note` https://en.wikipedia.org/wiki/Six-Day_War: confirmed: 5-10 June 1967; infobox 'Israel occupies a total of 70,000 km2 of territory' (the 'infobox' in the keyframe note is this page's)

## kingdom-of-jordan: fix

Area: infobox 89,342 km2 (2024), Cliopatria 90,193 km2, ratio 1.01, acknowledged True. 

Findings:
- `/identity/rulers/1-3` (applied by reviewer): Talal, Hussein and Abdullah II cited no page. Evidence: Jordan page: 'Abdullah was succeeded by his son Talal'; 'Hussein, who ascended to the throne in 1953 at age 17'; 'On 7 February 1999, Abdullah II ascended the throne'. Fix: source https://en.wikipedia.org/wiki/Jordan
- `/ledger/5` (applied by reviewer): 1949 rename had no month, confidence 2. Evidence: https://en.wikipedia.org/wiki/Jordanian_annexation_of_the_West_Bank: 'Transjordan became the Hashemite Kingdom of Jordan on 26 April 1949.' Fix: month 4, confidence 3, source the annexation page.
- `/ledger/1` (applied by reviewer): Note said the page does not name the recipient of Aqaba and Ma'an; it does, so confidence 2 understated. Evidence: https://en.wikipedia.org/wiki/Jordan%E2%80%93Saudi_Arabia_relations: 'In May 1925, Ibn Saud gave up the Aqaba and Ma'an districts of the Hejaz and it became part of British Emirate of Transjordan'. Fix: confidence 3; note corrected.
- `/ledger/7/region; /ledger/8/region` (applied by reviewer): Same straddling radii as state-of-israel /ledger/7-8. Evidence: See the state-of-israel finding (gazetteer resolve). Fix: Clipped with intersect (Israel 1949 shape; West Bank).
- `/ledger/0 (1921-1946)` (NOT applied): The Emirate was a British mandate territory; neither ledger carries the vassal relation. Evidence: Author's notes defer it to the British dossier (kingdom-of-great-britain, eu group, not yet written). Fix: When the UK dossier is written: vassal_start kingdom-of-jordan 1921-4 / vassal_end 1946-5 there; mirror here optional (non-blocking, exception).
- `/ledger/20` (NOT applied): 1988 loss names 'palestinians', whose dossier ends in 1950. Evidence: palestinians identity.end 1950-4. Fix: Re-point with state-of-israel /ledger/37 once the Palestinian owner slug is decided (routing, non-blocking).

For a gap-filler:
- `/ledger/13, /ledger/14`: Month of the 1965 exchange: the Jordan-Saudi page has none; kingdom-of-saudi-arabia /ledger/11-12 dates the treaty 9 August 1965. Try: https://en.wikipedia.org/wiki/Jordan%E2%80%93Saudi_Arabia_border

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Jordan: confirmed: infobox 'Emirate: 11 April 1921'
- `/ledger/1` https://en.wikipedia.org/wiki/Jordan%E2%80%93Saudi_Arabia_relations: confirmed (better than claimed): 'In May 1925 ... it became part of British Emirate of Transjordan'
- `/ledger/5` https://en.wikipedia.org/wiki/Jordanian_annexation_of_the_West_Bank: confirmed and dated: 26 April 1949
- `/ledger/9, /ledger/10, /ledger/19, /ledger/20` https://en.wikipedia.org/wiki/Jordanian_annexation_of_the_West_Bank: confirmed: 'formally annexed on 24 April 1950'; 'On 31 July 1988, King Hussein announced the severance'
- `/ledger/13, /ledger/14` https://en.wikipedia.org/wiki/Jordan%E2%80%93Saudi_Arabia_relations: confirmed: 'In 1965, Saudi Arabia and Jordan agreed to trade land'; 6,000 km2 gained, 7,000 km2 ceded, 19 km of coast; no date
- `/ledger/11` https://en.wikipedia.org/wiki/Arab_Federation: confirmed: 'Officially formed on 14 February 1958'
- `/ledger/21` https://en.wikipedia.org/wiki/Israel%E2%80%93Jordan_peace_treaty: confirmed: 26 October 1994; 'Israel recognises Jordan's sovereignty over the Naharayim/Baqura area'

## palestinians: pass

Area: infobox 0 km2 (1948), Cliopatria 5,477 km2, ratio 0.0, acknowledged True. No page gives an area; the keyframe note compares with the gazetteer West Bank (4,805 km2).

For a gap-filler:
- `/ledger/0`: found event is confidence 1: no page describes a Palestinian government in the West Bank in 1948 (structural: the row is an owner of Jordanian-occupied land, as the notes say). Try: https://en.wikipedia.org/wiki/Jericho_Conference

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Palestinians: confirmed: 'the West Bank was ruled by Jordan, and the Gaza Strip by Egypt' after May 1948; no Palestinian polity described
- `/ledger/2-4` https://en.wikipedia.org/wiki/Jordanian_annexation_of_the_West_Bank: confirmed: 'formally annexed on 24 April 1950'
- `/ledger/0` https://en.wikipedia.org/wiki/Palestinians: not on page (confidence 1, said so in the note)

## qatar-protectorate: fix

Area: infobox 11,581 km2 (2024), Cliopatria 307,788 km2, ratio 26.58, acknowledged True. Both Cliopatria shapes reviewed 'wrong' and replaced by the State of Qatar 1973 shape.

Findings:
- `/identity/rulers/1-2` (applied by reviewer): Ali bin Abdullah and Ahmad bin Ali cited no page. Evidence: https://en.wikipedia.org/wiki/History_of_Qatar: Ali recognised as ruler in 1949, abdicated in 1960, 'he made his son, Ahmad bin Ali, ruler'. Fix: source https://en.wikipedia.org/wiki/History_of_Qatar
- `/ledger (1916-11 to 1971-9)` (NOT applied): No vassal_start/vassal_end with Britain in the protectorate's own ledger (all-palestine-government records its protector this way). Evidence: Q page: 'Qatar became a British protectorate on 3 November 1916'; the overlord dossier (kingdom-of-great-britain / its UK split) is not written. Fix: Overlord's dossier carries vassal_start qatar-protectorate 1916-11 / vassal_end 1971-9; mirror here once the UK slug is fixed (exception, non-blocking).

For a gap-filler:
- `(missing) 1936-1939`: Hawar Islands passing to Bahrain: the History of Qatar page (opened) says 'Bahrain claimed rule over a group of islands between the two countries in 1936' and Britain accepted the claim; small loss not in the ledger. Try: https://en.wikipedia.org/wiki/Hawar_Islands

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Qatar: confirmed: 'Qatar became a British protectorate on 3 November 1916'
- `/ledger/1` https://en.wikipedia.org/wiki/History_of_Qatar: confirmed: 'declared its independence on 1 September 1971 and became an independent state on 3 September'
- `/keyframe_review/1-2` https://en.wikipedia.org/wiki/Qatar: confirmed wrong: infobox 11,581 km2 against Cliopatria's 307,788 km2 Oman outline

## republic-of-egypt: fix

Area: infobox 1,010,408 km2 (2024), Cliopatria 1,011,422 km2, ratio 1.0, acknowledged True. 

Findings:
- `/identity/rulers/1` (applied by reviewer): Nasser cited no page. Evidence: https://en.wikipedia.org/wiki/Egypt: 'In June 1956, Nasser assumed the presidency'; 'The presidency remained vacant until Nasser was formally elected in 1956' (so the 1954-1956 gap is the page's). Fix: source https://en.wikipedia.org/wiki/Egypt
- `/ledger/9, /ledger/10, /identity/end` (applied by reviewer): The 1958 merge and dissolve had no month (the UAR dossier's found is 1958-2). Evidence: https://en.wikipedia.org/wiki/United_Arab_Republic: 'The United Arab Republic was established on 1 February 1958'; infobox 22 February 1958. Fix: month 2, source the UAR page (added to sources[]), identity.end month 2.
- `/keyframe_review/0/note; /ledger/5 region` (NOT applied): Gaza is drawn as Egypt's own land, while the all-palestine-government dossier holds it as Egypt's vassal 1948-1959 (vassal_start kingdom-of-egypt 1948-9, no vassal_end); republic-of-egypt neither inherits nor ends that vassalage, and the 1956 Israeli occupation names Egypt as Gaza's owner. Evidence: all-palestine-government /ledger/1-2; kingdom-of-egypt /ledger/3; this dossier has no vassal event. Fix: Agree one model with me-10-h: either vassal_start all-palestine-government 1953-6 (inherited, conf 1) and vassal_end 1958-2 here, and the 1956 occupation of Gaza recorded against all-palestine-government; or the APG dossier drops the vassalage (non-blocking, routing).

For a gap-filler:
- `/ledger/7`: Completion of the Anglo-French withdrawal from Port Said (confidence 1, month 11 bridged); the Suez Crisis page has no date ('agreed to withdraw from Egypt within a week'). Try: https://en.wikipedia.org/wiki/United_Nations_Emergency_Force
- `/ledger/1`: Canal Zone occupation start inherited (confidence 1). Try: https://en.wikipedia.org/wiki/Anglo-Egyptian_Treaty_of_1936

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Egypt: confirmed: 'On 18 June 1953, the Republic of Egypt was officially declared'
- `/ledger/2` https://en.wikipedia.org/wiki/Egypt: confirmed: 'British forces completed their withdrawal from the Suez Canal Zone on 13 June 1956'
- `/ledger/5, /ledger/8` https://en.wikipedia.org/wiki/Suez_Crisis: confirmed: 'Israel invaded on 29 October'; infobox 'Israeli occupation of the Sinai Peninsula and the Gaza Strip until March 1957'
- `/ledger/7` https://en.wikipedia.org/wiki/Suez_Crisis: not on page (confidence 1, said so)
- `/ledger/9` https://en.wikipedia.org/wiki/Egypt: confirmed year only ('In 1958'); month taken from the UAR page

## arab-federation: fix

Area: infobox 533,314 km2 (1958), Cliopatria 537,952 km2, ratio 1.01, acknowledged True. 

Findings:
- `/identity/rulers/1` (applied by reviewer): Hussein cited no page. Evidence: https://en.wikipedia.org/wiki/Arab_Federation: infobox 'King of Jordan: Hussein'. Fix: source https://en.wikipedia.org/wiki/Arab_Federation

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Arab_Federation: confirmed: 'Officially formed on 14 February 1958'
- `/ledger/3` https://en.wikipedia.org/wiki/Arab_Federation: confirmed: 14 July 1958 'both the Hashemite regime fell and with it the short-lived Arab Federation'
- `/ledger/5` https://en.wikipedia.org/wiki/Arab_Federation: confirmed: 'the new Iraqi government officially dissolved the Federation on 2 August 1958'
- `/keyframe_review/0` https://en.wikipedia.org/wiki/Arab_Federation: confirmed: infobox 533,314 km2, capital Baghdad

## Cross-dossier matrix (non-matched rows)

- exception: state-of-israel 1949 gain nobody <-> -  . Southern Negev, Operation Uvda, counterpart nobody
- mismatch: state-of-israel 1967 occupation_start arab-republic-of-egypt <-> united-arab-republic 1967 occupation_start. Sinai: the UAR dossier records it with state-of-israel; Israel names arab-republic-of-egypt (dossier not written, starts 1971)
- mismatch: state-of-israel 1967 contest_start arab-republic-of-egypt <-> united-arab-republic  . no contest events in the UAR dossier for 1967; owner string anachronistic
- mismatch: state-of-israel 1967 occupation_start syria <-> arab-socialist-ba-ath-party 1967 occupation_start. Golan: ASBP /ledger/1 names state-of-israel; Israel names syria (me-10 part not run)
- mismatch: state-of-israel 1967 occupation_start palestinians <-> united-arab-republic 1967 occupation_end. Gaza: UAR ends its own occupation of palestinians land 1967-6; the palestinians dossier ends 1950
- exception: state-of-israel 1973 contest_start arab-republic-of-egypt <-> -  . arab-republic-of-egypt owned by a me-10 part that has not run
- exception: state-of-israel 1973 contest_start syria <-> -  . syria owned by a me-10 part that has not run
- exception: state-of-israel 1974 loss syria <-> -  . Quneitra; syria not written
- exception: state-of-israel 1981 gain syria <-> -  . Golan annexation; syria not written
- exception: state-of-israel 1982 occupation_end arab-republic-of-egypt <-> -  . Sinai; arab-republic-of-egypt not written
- mismatch: state-of-israel 1985 occupation_start lebanon <-> lebanon 1978 occupation_start. security belt: lebanon dates its border-band occupation from March 1978 (to 2000); Israel from 1985
- missing: lebanon 1948 occupation_start state-of-israel <-> state-of-israel  . 1948 to 23 March 1949 occupation of south Lebanon has no Israeli event (on the 1948 War page the author read)
- missing: lebanon 1978 occupation_start state-of-israel <-> state-of-israel  . Operation Litani, March 1978
- missing: lebanon 2006 occupation_start state-of-israel <-> state-of-israel  . Ghajar from October 2006
- mismatch: state-of-israel 1988 occupation_start palestinians <-> palestinians  . palestinians dossier ends 1950; owner slug for post-1988 West Bank undecided
- mismatch: state-of-israel 2005 occupation_end palestinians <-> palestinians  . Gaza 2005; palestinians dossier ends 1950
- exception: state-of-israel 2024 occupation_start syria <-> -  . UN buffer zone; syria not written
- mismatch: kingdom-of-jordan 1988 loss palestinians <-> palestinians  . palestinians dossier ends 1950
- missing: kingdom-of-jordan 1994 gain state-of-israel <-> state-of-israel  . Naharayim/Tzofar: no loss in state-of-israel (author flagged)
- exception: palestinians 1948 found british-mandate-for-palestine <-> -  . listed in counterparts_needing_dossiers
- exception: qatar-protectorate 1971 dissolve state-of-qatar <-> -  . state-of-qatar owned by a me-10 part that has not run
- exception: republic-of-egypt 1953 occupation_start kingdom-of-great-britain <-> -  . kingdom-of-great-britain (eu group) not written
- exception: republic-of-egypt 1956 occupation_start kingdom-of-great-britain <-> -  . Port Said; France has no slug yet (french-fourth-republic listed)
- mismatch: all-palestine-government 1948 vassal_start kingdom-of-egypt <-> republic-of-egypt  . vassalage of Gaza not carried through 1953-1958 by republic-of-egypt nor ended by kingdom-of-egypt
- missing: arab-federation 1958 merge kingdom-of-iraq <-> kingdom-of-iraq  . kingdom-of-iraq has no merge on 14 February 1958 (only dissolve to iraqi-republic 1958-7); route to its group
- mismatch: arab-federation 1958 loss iraqi-republic <-> iraqi-republic 1958 found. iraqi-republic /ledger/0 names kingdom-of-iraq as counterpart, though it lists arab-federation as predecessor

Matched: 33 of 59 rows (full list in history/notes/phase-b/reviews/me-10-j.json).

## Problems for the orchestrator

- Owner slug for Palestinian land after 1950 is undecided: 'palestinians' (dossier 1948-1950) is used as counterpart by state-of-israel (Gaza 1967-2005, West Bank from 1988), kingdom-of-jordan (1988) and united-arab-republic (Gaza 1959-1967). The orchestrator should either extend 'palestinians' or create state-of-palestine / palestinian-national-authority and re-point all four dossiers together.
- Cliopatria 'Qatar Protectorate' 1947-1955 (307,787.5 km2) has exactly the area of sultanate-of-muscat-and-oman_1936 and _1946: it is Muscat and Oman continued under a wrong label. Route the outline to the Oman owner (sultanate-of-muscat-and-oman, me-10 part not yet run) for 1947-1955; Cliopatria has no Oman shape 1956-1972.
- Gazetteer 'Golan' polygon reaches 36.05 E and covers the Syrian-held third (10 cells, about 2,529 km2; 6 inside Cliopatria's Israel). The reviewer clipped state-of-israel's sovereign Golan (keyframes 8-12, 1981 gain) to the Cliopatria line; the 1967 occupation in state-of-israel and arab-socialist-ba-ath-party still uses the whole polygon. A gazetteer entry for the Israeli-held Golan would let both sides name it.
- Arab Federation chain: kingdom-of-iraq (written) has no merge into arab-federation on 14 February 1958, and iraqi-republic /ledger/0 names kingdom-of-iraq where arab-federation gives Iraq to the iraqi-republic; route to the owners of those two dossiers.
- Gaza 1948-1959: all-palestine-government (me-10-h) has vassal_start kingdom-of-egypt 1948-9 with no vassal_end, republic-of-egypt carries no vassal event and treats Gaza as its own land; one model should be agreed across kingdom-of-egypt, republic-of-egypt, all-palestine-government and united-arab-republic.
- Brief conflict noted: reviewer-brief section 5 says reviewers do not edit dossiers; the orchestrator's adjustment for this run allowed small verified fixes, which were applied (rulers' sources, three months, two confidence levels, four armistice regions, the Golan clip) and re-validated with 0 errors.
- No page failed to load. The Suez Crisis page (85,730 characters) gives no date for the Anglo-French withdrawal.

## Gazetteer names needed

- Eilat (place; state-of-israel)
- Wadi Ara (region; state-of-israel; kingdom-of-jordan)
- Little Triangle (region; state-of-israel; kingdom-of-jordan)
- Naharayim (Baqura) (place; kingdom-of-jordan)
- Tzofar (Al Ghamr) (place; kingdom-of-jordan)
- South Lebanon Security Belt (region; state-of-israel)
- Southern Negev (region; state-of-israel)
- Golan Heights, Israeli-held (west of the 1974 disengagement line) (region; state-of-israel; arab-socialist-ba-ath-party)
