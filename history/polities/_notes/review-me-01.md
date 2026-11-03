# Review: batch me-01 (Sumer to Ur III, Elam), 2026-10-18

Adversarial review of the fifteen me-01 dossiers. The machine copy is history/notes/phase-b/reviews/me-01.json. The validator (with --resolve) reports 0 errors in all fifteen; its warnings are gazetteer misses (Gu-edena, Adab, Isin, Larsa, Umma) and the expected 'shape has no verdict' in the split dossiers. Spot checks: 4 to 6 per dossier, weighted to the confidence-3 events and the events that move the most land. All seven confidence-3 events are on their pages with the year.

Verdict key: **fix** with every item marked [applied] = fixed by the reviewer. **fix** with [author] items = small additions that change no drawn land. **fail** = at least one [author] item that changes drawn land or leaves a land mirror missing.

## Verdicts

- `sumerian-city-states`: **fail**
- `elam`: **fail**
- `akkadian-empire`: **fail**
- `gutian-dynasty`: **fail**
- `third-dynasty-of-ur`: **fix**
- `uruk`: **fix**
- `isin`: **fail**
- `larsa`: **fail**
- `lagash`: **fail**
- `second-dynasty-of-lagash`: **pass**
- `ebla`: **fix**
- `mari`: **fix**
- `kish`: **fix**
- `first-dynasty-of-ur`: **fail**
- `umma`: **fail**

## sumerian-city-states: fail

- [author] `/ledger/7`: Eannatum's occupation of Susa and Mari's tribute (/ledger/7-10) are booked to the collective as well as to lagash (/ledger/4,5,8,9), so the same events are drawn twice, and elam /ledger/3-4 mirror the collective instead of Lagash. *Evidence:* Eannatum page: he 'demanded tribute as far as Mari' and subdued Elam 'destroying the city of Susa' as ruler of Lagash; lagash.json carries vassal_start mari and occupation_start elam at -2450. *Fix:* Delete /ledger/7-10 here; re-point elam /ledger/3 and /ledger/4 to counterpart lagash.
- [author] `/ledger`: The collective records none of the mirror events that eleven city-dossier events book against it: first-dynasty-of-ur gain of Sumer -2500 (/ledger/1), lagash loss of Sumer -2425 (/ledger/6), occupations of Ur -2400..-2340 and Kish -2350..-2340, umma's gain of Ur and Uruk -2350, and the -2340 dissolves of lagash, kish, first-dynasty-of-ur and umma into it. *Evidence:* Cross-check matrix: all eleven have no mirror within a year; here the hegemonies are capital_move events (-2500, -2450, -2425) and a rename (-2340). The author left the overlap rule to the orchestrator (notes, decision 3), which is not one of the brief's accepted exceptions. *Fix:* After the orchestrator's decision: either add the mirrors here (loss -2500 to first-dynasty-of-ur; gain -2425 from lagash; occupation_start/end over Ur -2400/-2340 and Kish -2350/-2340 with those counterparts; loss -2350 to umma; gains -2340 from the four dissolving cities) and drop the capital moves they duplicate, or demote this dossier and re-point the cities' counterparts.
- [author] `/keyframe_review/3`: The -2700 and -2500 shapes (K3 ok, K4 adjust minus Mari only) keep a tongue into Khuzestan to 48.9 E for -2700..-2301. That double-claims Susiana with elam's new keyframe elam_-2700 (Khuzestan + Ilam) and contradicts this ledger, which treats Susa as Elam's land, occupied only -2450..-2425. *Evidence:* shapes.csv: sumerian-city-states_-2700 and _-2500 bbox to 48.9476 E, modern_countries include Iran. The K3 note says the tongue 'rests only on Enmebaragesi's (c. 2750) and Eannatum's (c. 2450) Elamite victories'. *Fix:* K3 adjust {minus:[{cliopatria:'Sumerian City-States',year:-2700},{region:'Khuzestan'}]}; K4 minus Mari and Khuzestan.
- [author] `/identity/predecessors`: uruk-period.json (another group) names this dossier as its successor and books a loss -3400 with counterpart sumerian-city-states. Here there is no predecessor, and the found event has no counterpart. *Evidence:* uruk-period identity.successors[0] = sumerian-city-states, land {cliopatria: Sumerian City-States, year: -3400}; uruk-period /ledger/3 loss -3400. *Fix:* Add predecessor uruk-period (land {cliopatria:'Sumerian City-States',year:-3400}) and counterpart 'uruk-period' on /ledger/0.
- [author] `/notes`: The OVERLAP paragraph says kish, the First Dynasty of Ur and umma 'were not reached and their page evidence is cited here instead', but all three were written in this batch. *Evidence:* kish.json, first-dynasty-of-ur.json and umma.json exist and validate. *Fix:* Update the paragraph and point to those dossiers.
- [author] `/keyframe_review/6`: The correction for sumerian-city-states_-2100 (verdict wrong) names the 'Gutian Dynasty' -2100 shape, as if that shape were this state's for -2100..-2001, but the state ended in -2300. *Evidence:* The schema says 'wrong' gives 'the shape to use instead, or the years it belongs to'. Here the shape belongs to another dossier. *Fix:* Say in correction.text that the shape and years belong to third-dynasty-of-ur and lie outside this state's life.

Thin (for a gap-filler):
- `/ledger/1`: -3200/-3000/-2700 area growth: gains from nobody at confidence 1 (settlement, no page gives a frontier) (try https://en.wikipedia.org/wiki/Jemdet_Nasr_period)
- `/ledger/9`: end of Lagash's hegemony -2425 (confidence 1) (try https://en.wikipedia.org/wiki/Enannatum_I)
- `/ledger/11`: Uruk hegemony from -2425 (confidence 1) (try https://en.wikipedia.org/wiki/Lugal-kinishe-dudu)

Spot checks: `/ledger/13` Akkadian_Empire: confirmed; `/ledger/7` Eannatum: confirmed; `/ledger/8` Eannatum: confirmed; `/ledger/12` Lugal-zage-si: confirmed

Area: History of Sumer has no infobox area (only a partial fragment: 'Southern Irak and neighboring regions'). The dossier says no infobox area exists.

## elam: fail

- [applied] `/ledger/6`: The note's quote was not on the page, and the year -2110 is not the page's. *Evidence:* Kutik-Inshushinak page: 'He conquered numerous cities in central Mesopotamia, including Eshnunna and Akkad, and probably Akshak' (undated). 'Early in his reign' refers to Ur-Nammu's reconquest, and the page links these conquests to the Gutians' weakness before Utu-hengal's revolt. *Fix:* Lowered confidence 2 to 1 and corrected the quote in the note.
- [author] `/ledger/6`: A large gain (Akkad + Diyala) from 'nobody' leaves no trace in the keyframes (K2 elam_-2200 is ok). By the page, it falls before the Gutian fall (c. 2119), when gutian-dynasty held Akkad (its K2 -2154..-2119 = Akkad + the plain). *Evidence:* Same page as above. gutian-dynasty /keyframe_review/2 includes {region: Akkad} to -2119. *Fix:* Re-date to c. -2125 (bridged, confidence 1) with counterpart gutian-dynasty (gutian-dynasty to add the loss), and mark /keyframe_review/2 adjust with Akkad + Diyala for the years held, or drop the event.
- [author] `/keyframe_review/4`: No event explains Fars (Anshan) dropping out of the map for -2000..-1801 and returning at -1800: elam_-2100 is Fars only, elam_-2000 ends at 50.48 E, elam_-1800 reaches 52.24 E again. The K4 correction removes only Iraq. *Evidence:* shapes.csv bboxes: _-2100 50.06-52.24 E; _-2000 44.30-50.48 E; _-1800 44.30-52.24 E. The ledger has no Persis event between -2240 and -539. *Fix:* K4 correction {union:[{minus:[{cliopatria:'Elam',year:-2000},{country:'Iraq'}]},{region:'Persis'}]} (the Shimashki and Sukkalmah kings held Anshan), or record the loss and regain with a page.
- [author] `/ledger`: Akkad's vassalage is not mirrored here: akkadian-empire /ledger/4 vassal_start (-2290) and /ledger/10 vassal_end (-2210), both with counterpart elam, have no pair in this ledger. The K1 note acknowledges it but leaves it to the Akkad ledger. *Evidence:* Sargon page: 'the governors, viceroys, and kings of Susa, Waraḫše, and neighboring districts became vassals of Akkad'. Awan page: 'the low-lying, westerly parts of Elam became a vassal of Akkad, centred at Susa'. *Fix:* Add vassal_start -2290 and vassal_end -2210, counterpart akkadian-empire, region Khuzestan, confidence 1.
- [author] `/ledger/5`: Persis is gained in -2240 from 'nobody', but akkadian-empire's -2250..-2201 keyframe (adjust minus Oman only) still draws Fars and Kerman to 56.5 E. *Evidence:* shapes.csv akkadian-empire_-2250 bbox 32.49-56.54 E. Awan page: Kutik-Inshushinak 'liberated Awan and Elam' as the empire broke down 'around 2240 BC'. *Fix:* Keep 'nobody' only if akkadian-empire removes the plateau from its K2 (see that dossier). Otherwise use counterpart akkadian-empire.
- [author] `/ledger/3`: Occupation of Susa by Eannatum names sumerian-city-states; lagash /ledger/5 and /ledger/9 hold the same occupation. *Evidence:* See sumerian-city-states /ledger/7. *Fix:* Counterpart lagash for /ledger/3 and /ledger/4.
- [author] `/keyframe_review/16`: K16 (-650..-631) and K17 (-615..-601) are ok, yet /ledger/27 takes Khuzestan, almost the whole -650 shape, from Elam for -640..-612. The keyframes and the ledger disagree about what is drawn. *Evidence:* Elam page: 'Humban-Haltash III, was captured in 640 BC by Ashurbanipal, who annexed and destroyed the country'. The /ledger/27 note says 'The highland remnant east of Susiana continues'. *Fix:* Mark K16 adjust (years -650..-641) and add a new keyframe elam_-640 (-640..-613) for the highland remnant, or record the Assyrian hold as an occupation.
- [author] `/identity/capitals/0`: Susa is the capital for all of -3200..-539, including -2094..-2015 (Susa was Ur III's: /ledger/9-10) and -640..-612 (Assyrian: /ledger/27-28). *Evidence:* Shulgi page as quoted in K3: 'The Ur III dynasty had held control over Susa since the demise of Puzur-Inshushinak'. *Fix:* Split the capitals: Anshan (Tall-e Malyan) for -2094..-2016 and the highland seat for -640..-613, or say in the note that no seat is drawn for those years.
- [author] `/identity/predecessors`: uruk-period.json books a loss -3200 with counterpart elam and names elam as a successor; elam has no predecessor and its found event has no counterpart. *Evidence:* uruk-period /ledger/4; identity.successors[1]. *Fix:* Add predecessor uruk-period and counterpart on /ledger/0.

Thin (for a gap-filler):
- `/keyframe_review/11`: -1100..-701: shapes go 81,970 -> 19,288 -> 46,092 -> 59,564 -> 46,072 km2 with no event (dark age; pages silent, 9/9 budget spent) (try https://en.wikipedia.org/wiki/List_of_rulers_of_Elam)
- `/ledger/1`: Proto-Elamite to Old Elamite extent -2700 (confidence 1; Proto-Elamite page failed) (try https://en.wikipedia.org/wiki/Proto-Elamite)
- `/ledger/8`: Ur-Nammu's reconquest of Akkad and Susa -2100/-2094 (confidence 1) (try https://en.wikipedia.org/wiki/Ur-Nammu)
- `/ledger/10`: Susa regained -2015 (confidence 1) (try https://en.wikipedia.org/wiki/Ibbi-Sin)
- `/ledger/22`: loss of Babylonia -1153 (confidence 1) (try https://en.wikipedia.org/wiki/Second_Dynasty_of_Isin)
- `/ledger/28`: Susiana regained -612 under Median suzerainty (confidence 1) (try https://en.wikipedia.org/wiki/Medes)

Spot checks: `/ledger/11` Shimashki_dynasty: confirmed; `/ledger/21` Shutruk-Nakhunte: confirmed; `/ledger/25` Elam: confirmed; `/ledger/6` Kutik-Inshushinak: mis-dated (the note's quote 'conquered early in Ur-Nammu's reign' is not on the page and the year -2110 is not the page's; confidence 2 lowered to 1 (applied), re-dating and counterpart left to the author); `/ledger/5` Awan_dynasty: confirmed; `/ledger/27` Elam: confirmed

Area: The Elam infobox has no area ('Dates: 3200–539 BC', 'Geographical range: Iran and Iraq'). The dossier's sources note says 'no area'. Largest Cliopatria shape: 215,100 km2 (-1150, marked wrong).

## akkadian-empire: fail

- [author] `/keyframe_review/2`: No ledger event explains the -2250 peak's spread east to 56.5 E (Fars, Kerman) and south to 24.5 N. The correction removes only Oman, and the only gain between -2300 and -2250 is /ledger/9 (NW Syria). *Evidence:* shapes.csv: _-2300 bbox ends at 49.10 E; _-2250 runs 32.49-56.54 E, 24.52-37.90 N. Akkad page: Manishtushu 'claimed to have subjugated the land of Magan'; W2 'Manishtushu's campaigns' has empty zones; the note keeps Marhashi 'soft'. *Fix:* Remove the plateau east of Khuzestan from the K2 correction, or add dated gains with a page (Manishtushu's Anshan/Sherihum campaign, Naram-Sin). Then reconcile elam /ledger/5 (Persis -2240).
- [author] `/keyframe_review/1`: K1 (ok) and K2 draw Khuzestan as direct territory, while /ledger/4 makes it a vassal from -2290 ('Lighter tint (rule 4), not direct territory as Cliopatria draws it'). That double-claims Susiana with elam's keyframe elam_-2700. *Evidence:* /ledger/4 note; elam /keyframe_review/1 = Khuzestan + Ilam -2700..-2201. K3 already removes Khuzestan. *Fix:* K1 adjust {minus:[{cliopatria:'Akkadian Empire',year:-2300},{region:'Khuzestan'}]} (a new keyframe -2300..-2291 if Susa was direct before the vassalage), and K2 likewise minus Khuzestan.
- [author] `/ledger`: Nothing mirrors gutian-dynasty /ledger/0 (found -2220 at Adab, counterpart akkadian-empire): Akkad has no loss of Adab, and its -2250..-2201 keyframe still covers Adab, an overlap the author flagged but did not resolve. *Evidence:* Gutian page: 'By the end of the Akkadian period, the Sumerian city of Adab was occupied by the Gutians, who made it their capital'; infobox 'Established: c. 2220 BC'. *Fix:* Add loss -2220 {place:'Adab',km:40} counterpart gutian-dynasty, confidence 1.
- [author] `/ledger/11`: The land disagrees with gutian-dynasty /ledger/1: Akkad loses 'Sumer minus Lagash' (Uruk included), but the Gutians gain Sumer minus Lagash and Uruk. Uruk then belongs to no dossier for -2189..-2154. *Evidence:* Region specs of the two events; uruk /ledger/0 founds Uruk only in -2154. *Fix:* Align the two: Akkad keeps Uruk (loss region minus Uruk too; uruk /ledger/0 counterpart then akkadian-empire), or the Gutian gain includes Uruk.

Thin (for a gap-filler):
- `/ledger/4`: Elamite vassalage years -2290/-2210 bridged (confidence 1) (try https://en.wikipedia.org/wiki/Rimush)
- `/ledger/5`: Kaku of Ur revolt and Great Revolt lengths (confidence 1) (try https://en.wikipedia.org/wiki/Naram-Sin_of_Akkad)
- `/ledger/9`: Naram-Sin's conquest of Ebla/Armanum -2250 (confidence 1) (try https://en.wikipedia.org/wiki/Naram-Sin_of_Akkad)

Spot checks: `/ledger/1` Akkadian_Empire: confirmed; `/ledger/3` Mari,_Syria: confirmed; `/ledger/4` Sargon_of_Akkad: confirmed; `/ledger/11` Akkadian_Empire: confirmed

Area: No infobox area (infobox c. 2334 - c. 2154 BC). The dossier says 'No infobox area to compare'.

## gutian-dynasty: fail

- [author] `/ledger/4`: The dissolve hands {region: Akkad} to uruk. Its own text says 'Akkad and Kish to no state until Kutik-Inshushinak's Elam', and uruk /ledger/1 gains only Sumer minus Lagash and Uruk. *Evidence:* Region of /ledger/4 vs its text and uruk /ledger/1. The Utu-hengal page does not mention Akkad. *Fix:* Make the dissolve region the Sumer part only. Give Akkad to elam (a loss before -2119, if elam re-dates its /ledger/6 as the Kutik-Inshushinak page implies) or to nobody.
- [author] `/ledger/0`: The found event names akkadian-empire as counterpart, but Akkad records no loss of Adab (see akkadian-empire). *Evidence:* Cross-check matrix: no akkadian-empire event at -2220. *Fix:* Keep, once akkadian-empire adds the loss; otherwise use counterpart nobody and note the overlap.
- [author] `/ledger/1`: Gains Sumer minus Lagash and Uruk, while Akkad's mirror loses Sumer minus Lagash only (Uruk unassigned -2189..-2154). *Evidence:* See akkadian-empire /ledger/11. *Fix:* Align with akkadian-empire.

Thin (for a gap-filler):
- `/ledger/1`: the Gutian frontier -2189 bridged (confidence 1) (try https://en.wikipedia.org/wiki/Erridupizir)

Spot checks: `/ledger/0` Gutian_rule_in_Mesopotamia: confirmed; `/ledger/1` Gutian_rule_in_Mesopotamia: confirmed; `/ledger/2` Gutian_rule_in_Mesopotamia: confirmed; `/ledger/4` Gutian_rule_in_Mesopotamia: confirmed

Area: No infobox area. Cliopatria's only shape (-2100, 131,488 km2) is marked wrong: it is Ur III's realm.

## third-dynasty-of-ur: fix

- [author] `/ledger/4`: The Zagros vassal region (Arbil + Sulaymaniyah + Diyala) includes Diyala, which this state holds directly from /ledger/2 (-2100) until it loses it to Eshnunna in /ledger/8. The same land is drawn as both direct territory and vassal. *Evidence:* /ledger/2 region {Akkad, Diyala}; /ledger/8 loss Diyala -2020. *Fix:* Drop Diyala from /ledger/4 and /ledger/7 (Simurrum/Karhar on the upper Diyala can be named as a place instead).
- [author] `/ledger/4`: The Zagros vassals (Simurrum, Lullubum, Urbilum, Karhar) have no dossier. They are named in the author's notes but missing from the report's counterparts_needing_dossiers. *Evidence:* Author notes: 'Eshnunna, Der, Simurrum, Lullubum, Urbilum, Karhar need dossiers'. *Fix:* Added to this review's counterparts_needing_dossiers; no change to the dossier itself.

Thin (for a gap-filler):
- `/ledger/5`: Larsa as Ur III vassal -2025..-2004 (confidence 1; no page calls Naplanum a vassal, and larsa has no mirror) (try https://en.wikipedia.org/wiki/Naplanum)
- `/ledger/11`: Ibbi-Sin's loss of Sumer to Isin -2008 (confidence 1; isin has no mirror gain) (try https://en.wikipedia.org/wiki/Ibbi-Sin)

Spot checks: `/ledger/13` Third_Dynasty_of_Ur: confirmed; `/ledger/10` Third_Dynasty_of_Ur: confirmed; `/ledger/9` Isin: confirmed; `/ledger/6` Lagash: confirmed; `/ledger/3` Kutik-Inshushinak: confirmed

Area: No infobox area (c. 2112 - c. 2004 BC; seat Ur). The reused 'Gutian Dynasty' shape is 131,488 km2.

## uruk: fix

- [applied] `/keyframe_review/1/note`: The note quoted Kutik-Inshushinak's conquests as made 'early in Ur-Nammu's reign'; on the page that phrase belongs to Ur-Nammu's reconquest. *Evidence:* Kutik-Inshushinak page: Ur-Nammu 'early in his reign, reconquered the northern territories that had been occupied by Puzur-Inshushinak'. *Fix:* Rewrote the clause: 'took 'Eshnunna and Akkad, and probably Akshak' (undated on his page; Ur-Nammu reconquered them 'early in his reign')'.

Spot checks: `/ledger/0` Uruk: confirmed; `/ledger/1` Utu-hengal: confirmed; `/ledger/2` Utu-hengal: confirmed

Area: No state infobox: Uruk is a site page and Utu-hengal a ruler page. No Cliopatria shape.

## isin: fail

- [author] `/ledger`: Isin has no mirror for third-dynasty-of-ur /ledger/11 (loss -2008 of 'Sumer minus Ur' to isin), so nothing explains its growth from K0 (Isin + Nippur) to K1 (the -2000 shape minus Larsa, Ur, Lagash and Uruk: all of central and northern Babylonia). *Evidence:* Cross-check matrix; shapes.csv sumerian-city-states_-2000 53,983 km2, bbox 44.16-48.10 E, 30.31-33.33 N. Ishbi-Erra page: a 27th year-name claims suzerainty over Sumer and Akkad. *Fix:* Add gain -2008 (or the year the author can source), counterpart third-dynasty-of-ur, with a region matching K1.
- [author] `/keyframe_review/1`: K1 (-2000..-1801) excludes Ur, though /ledger/1 gives Isin Ur from -1983 to -1906 (/ledger/2). It also excludes Lagash, though /ledger/2 loses Lagash. *Evidence:* Ishbi-Erra page: 'Some years later, Ishbi-Erra ousted the Elamite garrison from Ur'. Larsa page: Lagash is 'a city Ishbi-Erra recaptured'. *Fix:* Split K1 with new keyframes at -1983 (Isin with Ur) and -1906 (without), and decide Lagash: either Isin gains it (add the event) or /ledger/2 loses Ur only.
- [author] `/ledger/2`: The region includes Lagash province, but the Isin page makes Gungunum already 'the royally appointed governor of Larsa and Lagash province' when he seized Ur, so Lagash did not pass from Isin to Larsa in -1906. *Evidence:* Isin page, as quoted in the note itself. *Fix:* Region {place:'Ur',km:70} only; record Lagash where it changed hands (larsa /ledger/1 likewise).

Thin (for a gap-filler):
- `/keyframe_review/1`: K1 keeps northern Babylonia (Kish, Babylon, Sippar inside the shape to 33.33 N) to -1801, while Babylon's First Dynasty rises c. 1894 and Kish is 'a buffer state' c. 2020-1900 (kish note); no event (try https://en.wikipedia.org/wiki/Sumu-abum)
- `/ledger/2`: Gungunum's capture of Ur undated (-1906, confidence 1) (try https://en.wikipedia.org/wiki/Gungunum)
- `/ledger/3`: loss of Nippur 'at some point' (-1865, confidence 1) (try https://en.wikipedia.org/wiki/Lipit-Ishtar)

Spot checks: `/ledger/0` Isin: confirmed; `/ledger/1` Ishbi-Erra: confirmed; `/ledger/2` Isin: confirmed; `/ledger/7` Rim-Sin_I: confirmed

Area: Site page; no state area (site 'about 150 hectares'). Reuses the Sumerian City-States -2000 shape with corrections.

## larsa: fail

- [author] `/ledger`: No mirror for third-dynasty-of-ur /ledger/5 and /ledger/12 (vassal_start -2025 / vassal_end -2004, counterpart larsa). Larsa's found event names Ur III but records no vassalage. *Evidence:* Cross-check matrix. Larsa page: 'The page does not call Naplanum a vassal' (author K0 note); the page has only 'After the Third Dynasty of Ur collapsed c. 2004 BC'. *Fix:* Add vassal_start -2025 and vassal_end -2004, counterpart third-dynasty-of-ur, confidence 1, or have Ur III drop the pair.
- [author] `/keyframe_review/1`: The correction draws Larsa + Ur + Lagash for all of -2000..-1801, but the ledger gives Ur to elam (-2004..-1983) and isin (-1983..-1906) and gains it only in -1906 (/ledger/1). The note itself says 'until then Larsa is the city alone'. Ur is double-claimed with elam and isin. *Evidence:* K1 note; elam /ledger/11-12; isin /ledger/1-2. *Fix:* New keyframe larsa_-2000 (-2000..-1907) = Larsa plus Lagash province (if the author follows the Isin page on Gungunum), and K1 from -1906.
- [author] `/ledger/1`: Gains Lagash from isin in -1906, but per the Isin page Gungunum already governed 'Larsa and Lagash province', and isin's keyframes never include Lagash. *Evidence:* Isin page; isin /keyframe_review/1 minus Lagash. *Fix:* Region Ur only. Give Lagash to Larsa earlier (from nobody c. -2024, mirroring third-dynasty-of-ur /ledger/6) or from isin with a gain in isin.

Thin (for a gap-filler):
- `/ledger/0`: Larsa 'was later under Isin's control' (Larsa page) before Gungunum: no vassal events (try https://en.wikipedia.org/wiki/Gungunum)
- `/ledger/2`: Nippur -1865 (confidence 1) (try https://en.wikipedia.org/wiki/Nur-Adad)
- `/identity/capitals/0`: Mashkan-shapir as second capital not placed (try https://en.wikipedia.org/wiki/Mashkan-shapir)

Spot checks: `/ledger/0` Larsa: confirmed; `/ledger/3` Rim-Sin_I: confirmed; `/ledger/4` Rim-Sin_I: confirmed; `/ledger/10` Rim-Sin_I: confirmed

Area: Site page; no state area (remains 'about 200 hectares'). Reuses the Sumerian City-States -2000/-1800 shapes.

## lagash: fail

- [applied] `/ledger/2/counterpart`: The gain of Sumer in -2450 named the collective, while first-dynasty-of-ur /ledger/2 books the same loss of Sumer to lagash. *Evidence:* Eannatum page: 'conquered all of Sumer, including Ur...'. First Dynasty of Ur page: Eannatum 'came to dominate the whole region'. *Fix:* Counterpart changed to first-dynasty-of-ur and the note updated; the pair now matches.
- [applied] `/ledger/10/confidence`: The contest_end in -2400 was confidence 2, but neither page dates an end; the Umma page only says the conflict was 'reported c. 2400 BC by Entemena'. *Evidence:* Umma page; Lagash page gives no end date. *Fix:* Lowered to 1, with the reason in the note.
- [author] `/ledger`: Nothing here mirrors kish /ledger/2-3 (occupation of Kish by lagash -2450..-2400). *Evidence:* Eannatum: 'He defeated Kish, Akshak, and Mari' and claimed 'King of Kish'. Kish page: Kug-Bau (c. 2400) 'gained independence from En-anna-tum I of Lagash'. *Fix:* Add occupation_start -2450 and occupation_end -2400, {place:'Kish',km:40}, counterpart kish.
- [author] `/keyframe_review/1`: K1 (union Sumer + Susa 60 km) draws Susa as direct territory, though /ledger/5 and the note make it a hatched occupation. It also draws Ur and Umma, which first-dynasty-of-ur (K2, Ur 40 km from -2450) and umma (K0) keep for the same years: double claims inside the batch. *Evidence:* K1 note 'Susa hatched (ledger)'; first-dynasty-of-ur /keyframe_review/2; umma /keyframe_review/0; lagash /ledger/3 makes Umma a vassal, not territory. *Fix:* Correction {minus:[{region:'Sumer'},{place:'Umma',km:30},{place:'Ur',km:40}]} without Susa, or have Ur and Umma record the occupation and vassalage that justify drawing them.
- [author] `/ledger/0`: /ledger/0 (found), /ledger/6 (loss of Sumer -2425) and /ledger/11 (dissolve -2340) name sumerian-city-states, which records no mirror. *Evidence:* Cross-check matrix. *Fix:* Settled by the collective's fix: keep the counterparts if the collective adds the mirrors, re-point them if it is demoted.

Thin (for a gap-filler):
- `/ledger/6`: end of the hegemony -2425 (confidence 1); the Kish page has Kish under Enannatum I to c. 2400 (try https://en.wikipedia.org/wiki/Enannatum_I)
- `/ledger/7`: Umma and Mari vassalage ends -2425 (confidence 1) (try https://en.wikipedia.org/wiki/Entemena)

Spot checks: `/ledger/0` Lagash: confirmed; `/ledger/1` Lagash: confirmed; `/ledger/2` Eannatum: confirmed; `/ledger/5` Eannatum: confirmed; `/ledger/10` Umma: confirmed (the quoted 'reported c. 2400 BC by Entemena' is on the page; the end year is bridged, so confidence was lowered to 1 (applied))

Area: Site/city page; no state area. No Cliopatria shape.

## second-dynasty-of-lagash: pass

- No fixes.

Spot checks: `/ledger/0` Lagash: confirmed; `/ledger/1` Lagash: confirmed

Area: No state area; no Cliopatria shape. Tried and could not break: both events are on the Lagash page with the years given (Ur-Baba r. c. 2164 - c. 2144; Nam-mahani r. c. 2113 - c. 2110, 'He slew Nam-ha-ni'); mirrors match in akkadian-empire /ledger/12 and third-dynasty-of-ur /ledger/1; Gutian and Uruk regions exclude Lagash 50 km for these years; Puzur-Mama's earlier, 'tenuous' independence is flagged in the notes.

## ebla: fix

- [author] `/ledger`: Ebla does not mirror mari /ledger/4-5: vassal_start -2360 and vassal_end -2340, counterpart ebla (Ebla tributary to Mari). *Evidence:* Ebla page: 'Ebla later paid tribute to Mari under Igrish-Halam'; 'Ebla recovered under King Irkab-Damu in about 2340 BC'. *Fix:* Add vassal_start -2360 (confidence 1) and vassal_end -2340 (confidence 2), counterpart mari, region {place:'Ebla',km:60}.

Thin (for a gap-filler):
- `/ledger/2`: height of the kingdom undated (-2400 bridged, confidence 1) (try https://en.wikipedia.org/wiki/Irkab-Damu)
- `/ledger/4`: destroyer of palace G disputed (confidence 1) (try https://en.wikipedia.org/wiki/Ebla_tablets)

Spot checks: `/ledger/0` Ebla: confirmed; `/ledger/1` Ebla: confirmed; `/ledger/2` Ebla: confirmed; `/ledger/4` Ebla: confirmed

Area: No infobox area for the kingdom; the extent is 'roughly half the size of modern Syria' (undated), rendered as six western governorates.

## mari: fix

- [author] `/ledger`: Mari does not mirror lagash /ledger/4 and /ledger/8 (vassal_start -2450 / vassal_end -2425, counterpart mari), nor the collective's duplicates (sumerian-city-states /ledger/8, /ledger/10). *Evidence:* Eannatum page: he 'demanded tribute as far as Mari'. *Fix:* Add vassal_start -2450 and vassal_end -2425, counterpart lagash, region {place:'Mari',km:100}.

Thin (for a gap-filler):
- `/keyframe_review/1`: the second kingdom's Euphrates strip is the dossier's reading (no border on the page) (try https://en.wikipedia.org/wiki/Iblul-Il)

Spot checks: `/ledger/1` Mari,_Syria: confirmed; `/ledger/2` Mari,_Syria: confirmed; `/ledger/4` Ebla: confirmed; `/ledger/7` Mari,_Syria: confirmed

Area: The site infobox gives 60 ha for the city; no state area. No Cliopatria shape.

## kish: fix

- [applied] `/ledger/1/region/text`: The text quoted 'a large territorial state' as if from the cited Kish page, which has only a cited paper title on the question. *Evidence:* Early Dynastic Period page: 'Kish was possibly the center of a large territorial state'. *Fix:* Text now reads 'northern Babylonia; the Early Dynastic page: 'Kish was possibly the center of a large territorial state''. The source stays the Kish page for Enmebaragesi's c. 2750.

Thin (for a gap-filler):
- `/keyframe_review/1`: territory of the Kish state bridged to the gazetteer's Akkad (confidence 1) (try https://en.wikipedia.org/wiki/Mesilim)

Spot checks: `/ledger/1` Kish_(Sumer): confirmed; `/ledger/2` Eannatum: confirmed; `/ledger/3` Kish_(Sumer): confirmed; `/ledger/4` Early_Dynastic_Period_(Mesopotamia): confirmed; `/ledger/6` Lugal-zage-si: confirmed

Area: No state area; no Cliopatria shape. The K1 'Akkad' region overlaps the collective's -2700/-2500 shapes: listed under sumerian-city-states.

## first-dynasty-of-ur: fail

- [author] `/keyframe_review/1`: K1 (-2500..-2451) draws all Sumer as Ur's territory, though its note says 'A union led, not land annexed'. For the same years lagash K0 (Lagash 40 km, to -2451) and umma K0 (Umma, from -2500) keep their cities: double claims inside the batch. *Evidence:* First Dynasty of Ur page: the dynasty 'apparently led a union of south Mesopotamian polities'. lagash /keyframe_review/0; umma /keyframe_review/0. *Fix:* Draw K1 as Ur (plus whatever a page says Mesannepada annexed) and record the union as vassal_start/vassal_end of the member dossiers, as lagash does for Umma and Mari; or K1 = Sumer minus Lagash 40 km minus Umma 30 km.
- [author] `/ledger/1`: /ledger/1 (gain -2500), /ledger/3-4 (occupation by the collective -2400..-2340) and /ledger/5 (dissolve -2340) name sumerian-city-states, which records no mirror. *Evidence:* Cross-check matrix. *Fix:* Settled by the collective's fix (see sumerian-city-states).

Thin (for a gap-filler):
- `/ledger/4`: end of the Uruk hold on Ur -2340 (confidence 1) (try https://en.wikipedia.org/wiki/Lugal-kinishe-dudu)

Spot checks: `/ledger/0` First_Dynasty_of_Ur: confirmed; `/ledger/1` First_Dynasty_of_Ur: confirmed; `/ledger/2` Eannatum: confirmed; `/ledger/3` Uruk: confirmed

Area: No infobox area (founded c. 2600, dissolved c. 2340); no Cliopatria shape.

## umma: fail

- [applied] `/ledger/2/confidence`: The contest_end in -2400 was confidence 2, but the Umma page gives no end, only that the conflict was 'reported c. 2400 BC by Entemena'. *Evidence:* Umma page. *Fix:* Lowered to 1, with the reason in the note.
- [author] `/ledger/3`: /ledger/3 gains Ur and Uruk in -2350, but the only keyframe (K0, -2500..-2340) draws Umma alone, and its note says Lugal-zage-si's conquests 'are the collective's rename, not Umma's territory'. The ledger and the keyframe contradict each other. *Evidence:* Umma page: 'the city reached its zenith c. 2350 BC, under the rule of Lugal-Zage-Si who also controlled Ur and Uruk'. *Fix:* Either add keyframe umma_-2350 (-2350..-2340) = Umma + Ur 40 km + Uruk 40 km (the holders of Ur and Uruk then record the loss), or drop /ledger/3 and the Ur/Uruk parts of /ledger/4's region.
- [author] `/ledger`: Umma does not mirror lagash /ledger/3 and /ledger/7 (vassal_start -2450 / vassal_end -2425, counterpart umma). *Evidence:* Eannatum page: he 'made Umma a tributary that paid grain into the temple treasury'. *Fix:* Add vassal_start -2450 (confidence 2) and vassal_end -2425 (confidence 1), counterpart lagash, region {place:'Umma',km:30}.

Thin (for a gap-filler):
- `/ledger/0`: founding -2500 bridged to Mesilim (confidence 1) (try https://en.wikipedia.org/wiki/Mesilim)

Spot checks: `/ledger/0` Early_Dynastic_Period_(Mesopotamia): confirmed; `/ledger/1` Lagash: confirmed; `/ledger/3` Umma: confirmed; `/ledger/4` Lugal-zage-si: confirmed; `/ledger/2` Umma: confirmed (the quoted 'reported c. 2400 BC by Entemena' is on the page; the end year is bridged, so confidence was lowered to 1 (applied))

Area: No state area; no Cliopatria shape.

## Cross-dossier matrix (not matched)

Matched pairs are in the JSON report. Below are the missing ones, the disagreements, and the exceptions.

- matched: sumerian-city-states -2450 occupation_start (counterpart elam) -> elam -2450 occupation_start. duplicate of lagash /ledger/5; to be deleted with elam re-pointed
- missing: sumerian-city-states -2450 vassal_start (counterpart mari) -> -. Lagash's tribute from Mari, duplicated in the collective; mari records neither
- matched: sumerian-city-states -2425 occupation_end (counterpart elam) -> elam -2425 occupation_end. duplicate of lagash /ledger/9
- missing: sumerian-city-states -2425 vassal_end (counterpart mari) -> -. as above
- matched: elam -2450 occupation_start (counterpart sumerian-city-states) -> sumerian-city-states -2450 occupation_start. matched, but the occupier was Lagash: lagash /ledger/5 books the same event; re-point to lagash
- matched: elam -2425 occupation_end (counterpart sumerian-city-states) -> sumerian-city-states -2425 occupation_end. as above
- exception: elam -1767 occupation_start (counterpart Eshnunna) -> -. listed in the author's counterparts_needing_dossiers (eshnunna, me-02)
- exception: elam -1760 occupation_end (counterpart Eshnunna) -> -. listed in the author's counterparts_needing_dossiers (eshnunna, me-02)
- exception: elam -1320 occupation_start (counterpart babylonia) -> -. babylonia belongs to me-02, which has not run
- exception: elam -1319 occupation_end (counterpart babylonia) -> -. babylonia belongs to me-02, which has not run
- exception: elam -1158 gain (counterpart babylonia) -> -. babylonia belongs to me-02, which has not run
- exception: elam -1153 loss (counterpart babylonia) -> -. babylonia belongs to me-02, which has not run
- exception: elam -653 occupation_start (counterpart neo-assyrian-empire) -> -. neo-assyrian-empire belongs to me-02, which has not run
- exception: elam -640 occupation_end (counterpart neo-assyrian-empire) -> -. neo-assyrian-empire belongs to me-02, which has not run
- exception: elam -640 loss (counterpart neo-assyrian-empire) -> -. neo-assyrian-empire belongs to me-02, which has not run
- exception: elam -612 gain (counterpart neo-assyrian-empire) -> -. neo-assyrian-empire belongs to me-02, which has not run
- exception: elam -539 dissolve (counterpart achaemenid-empire) -> -. achaemenid-empire has no dossier yet; another group (Iran) that has not run owns it
- missing: akkadian-empire -2290 vassal_start (counterpart elam) -> -. elam has no vassal_start for Akkad
- exception: akkadian-empire -2279 contest_start (counterpart Kaku of Ur (Sumerian revolt)) -> -. rebel coalition in a contest; no dossier needed
- exception: akkadian-empire -2278 contest_end (counterpart Kaku of Ur (Sumerian revolt)) -> -. rebel coalition in a contest; no dossier needed
- exception: akkadian-empire -2254 contest_start (counterpart Iphur-Kish (Great Revolt coalition)) -> -. rebel coalition in a contest; no dossier needed
- exception: akkadian-empire -2253 contest_end (counterpart Iphur-Kish (Great Revolt coalition)) -> -. rebel coalition in a contest; no dossier needed
- exception: akkadian-empire -2250 gain (counterpart Ebla (second kingdom)) -> -. listed in the author's counterparts_needing_dossiers
- missing: akkadian-empire -2210 vassal_end (counterpart elam) -> -. elam has no vassal_end for Akkad
- missing: gutian-dynasty -2220 found (counterpart akkadian-empire) -> akkadian-empire -2189 loss. akkadian-empire has no loss of Adab at -2220; nearest Akkad events are -2189 and -2154; nearest same-type event is more than a year away
- exception: third-dynasty-of-ur -2049 vassal_start (counterpart Zagros highland polities (Simurrum, Lullubum, Urbilum, Karhar)) -> -. named in the author's notes but missing from the report's list; added to counterparts_needing_dossiers by this review
- missing: third-dynasty-of-ur -2025 vassal_start (counterpart larsa) -> -. larsa has no vassal_start (its found names Ur III)
- exception: third-dynasty-of-ur -2020 vassal_end (counterpart Zagros highland polities (Simurrum, Lullubum, Urbilum, Karhar)) -> -. named in the author's notes but missing from the report's list; added to counterparts_needing_dossiers by this review
- exception: third-dynasty-of-ur -2020 loss (counterpart Eshnunna) -> -. listed in the author's counterparts_needing_dossiers (eshnunna, me-02)
- missing: third-dynasty-of-ur -2008 loss (counterpart isin) -> isin -2018 found. isin has no gain at -2008 (only its found at -2018); nearest same-type event is more than a year away
- missing: third-dynasty-of-ur -2004 vassal_end (counterpart larsa) -> -. larsa has no vassal_end
- missing: larsa -2025 found (counterpart third-dynasty-of-ur) -> -. found with counterpart Ur III, but Ur III records a vassal_start, not a split; acceptable once larsa adds the vassal pair
- exception: larsa -1801 gain (counterpart Uruk (Sin-kashid dynasty)) -> -. listed in the author's counterparts_needing_dossiers
- exception: larsa -1764 contest_start (counterpart babylonia) -> -. babylonia belongs to me-02, which has not run
- exception: larsa -1763 contest_end (counterpart babylonia) -> -. babylonia belongs to me-02, which has not run
- exception: larsa -1763 dissolve (counterpart babylonia) -> -. babylonia belongs to me-02, which has not run
- missing: lagash -2520 found (counterpart sumerian-city-states) -> -. collective records nothing
- matched: lagash -2450 gain (counterpart first-dynasty-of-ur) -> first-dynasty-of-ur -2450 loss. matched after the reviewer re-pointed the counterpart from sumerian-city-states
- missing: lagash -2450 vassal_start (counterpart umma) -> -. umma has no vassal_start
- missing: lagash -2450 vassal_start (counterpart mari) -> -. mari has no vassal_start
- missing: lagash -2450 occupation_start (counterpart elam) -> -. elam's mirror names sumerian-city-states
- missing: lagash -2425 loss (counterpart sumerian-city-states) -> -. collective records no gain from lagash
- missing: lagash -2425 vassal_end (counterpart umma) -> -. umma has no vassal_end
- missing: lagash -2425 vassal_end (counterpart mari) -> -. mari has no vassal_end
- missing: lagash -2425 occupation_end (counterpart elam) -> -. elam's mirror names sumerian-city-states
- missing: lagash -2340 dissolve (counterpart sumerian-city-states) -> -. collective records no gain from lagash
- missing: mari -2360 vassal_start (counterpart ebla) -> -. ebla has no vassal_start
- missing: mari -2340 vassal_end (counterpart ebla) -> -. ebla has no vassal_end
- missing: kish -2450 occupation_start (counterpart lagash) -> -. lagash has no occupation of Kish
- missing: kish -2400 occupation_end (counterpart lagash) -> -. lagash has no occupation_end
- missing: kish -2350 occupation_start (counterpart sumerian-city-states) -> -. the collective records no mirror (see sumerian-city-states /ledger)
- missing: kish -2340 occupation_end (counterpart sumerian-city-states) -> -. the collective records no mirror (see sumerian-city-states /ledger)
- missing: kish -2340 dissolve (counterpart sumerian-city-states) -> -. the collective records no mirror (see sumerian-city-states /ledger)
- missing: first-dynasty-of-ur -2500 gain (counterpart sumerian-city-states) -> -. the collective records no mirror (see sumerian-city-states /ledger)
- matched: first-dynasty-of-ur -2450 loss (counterpart lagash) -> lagash -2450 gain. matched after the reviewer's fix to lagash /ledger/2
- missing: first-dynasty-of-ur -2400 occupation_start (counterpart sumerian-city-states) -> -. the collective records no mirror (see sumerian-city-states /ledger)
- missing: first-dynasty-of-ur -2340 occupation_end (counterpart sumerian-city-states) -> -. the collective records no mirror (see sumerian-city-states /ledger)
- missing: first-dynasty-of-ur -2340 dissolve (counterpart sumerian-city-states) -> -. the collective records no mirror (see sumerian-city-states /ledger)
- missing: umma -2350 gain (counterpart sumerian-city-states) -> -. the collective records no mirror (see sumerian-city-states /ledger)
- missing: umma -2340 dissolve (counterpart sumerian-city-states) -> -. the collective records no mirror (see sumerian-city-states /ledger)
- mismatch: gutian-dynasty -2119 dissolve (counterpart uruk) -> uruk -2119 gain. land: the Gutian dissolve region includes Akkad, uruk's gain excludes Akkad, and the Gutian text says Akkad went to no state
- mismatch: akkadian-empire -2189 loss (counterpart gutian-dynasty) -> gutian-dynasty -2189 gain. land: Akkad's loss includes Uruk, the Gutian gain excludes it, so Uruk is unassigned -2189..-2154
- mismatch: isin -1906 loss (counterpart larsa) -> larsa -1906 gain. land: both include Lagash province, which the Isin page makes Gungunum's ('governor of Larsa and Lagash province') before -1906 and which isin's keyframes never hold
- mismatch: uruk-period -3400 loss (counterpart sumerian-city-states) -> sumerian-city-states -3400 found. sumerian-city-states' found has no counterpart and no predecessor; add uruk-period
- mismatch: uruk-period -3200 loss (counterpart elam) -> elam -3200 found. elam's found has no counterpart and no predecessor; add uruk-period
- mismatch: elam -2240 gain (counterpart nobody) -> -. Persis gained from nobody while akkadian-empire's -2250..-2201 keyframe still draws Fars and Kerman
- mismatch: elam -2110 gain (counterpart nobody) -> -. the Kutik-Inshushinak page puts the conquest of Akkad before the Gutian fall (c. 2119), when gutian-dynasty held Akkad; gutian-dynasty has no loss to elam

## Counterparts needing dossiers

- Eshnunna (`eshnunna`, -2020..-1762)
- Uruk (Sin-kashid dynasty) (`sin-kashid-dynasty-of-uruk`, -1865..-1801)
- Mari (Shakkanakku dynasty) (`shakkanakku-dynasty-of-mari`, -2266..-1830)
- Mari (Lim dynasty) (`lim-dynasty-of-mari`, -1830..-1761)
- Ebla (second kingdom) (`second-kingdom-of-ebla`, -2300..-2000)
- Ebla (third kingdom) (`third-kingdom-of-ebla`, -2000..-1600)
- Marhashi (`marhashi`, -2300..-2000)
- Magan (`magan`, -2300..-2200)
- Simurrum (`simurrum`, -2100..-2000)
- Lullubi (Lullubum) (`lullubi`, -2300..-2000)
- Urbilum (`urbilum`, -2100..-2000)
- Karhar (`karhar`, -2100..-2000)

## Gazetteer names needed

- Gu-edena (region): lagash, umma, sumerian-city-states
- Adab (place): gutian-dynasty
- Isin (place): isin, larsa, third-dynasty-of-ur
- Larsa (place): larsa, isin, third-dynasty-of-ur
- Umma (place): umma, lagash

## Problems and notes for the orchestrator

- Verdicts: 'fix' with every finding applied:true means the reviewer fixed it (uruk, kish). 'fix' with applied:false items (third-dynasty-of-ur, ebla, mari) means small non-blocking additions the author still has to make: vassal mirrors and a region trim that do not change drawn territory. 'fail' means at least one unapplied finding that changes drawn land or leaves a land mirror missing.
- Reviewer edits applied in place, re-validated (0 errors) and read back: elam /ledger/6 (confidence 2->1, note quote corrected); uruk /keyframe_review/1/note; kish /ledger/1/region/text; lagash /ledger/2 (counterpart -> first-dynasty-of-ur, note) and /ledger/10 (confidence 2->1); umma /ledger/2 (confidence 2->1). Pre-edit copies are in /tmp/claude-0/work/review-me-01/backup/.
- Not one section-6 context polity (babylonia, assyria, neo-assyrian-empire, median-kingdom) has a file in history/polities/ yet, so their mirrors are recorded as exceptions (group not run). uruk-period.json (another group) was cross-checked because it books losses to sumerian-city-states and elam.
- The Early Dynastic overlap (author's notes, decision 3) needs an orchestrator ruling before sumerian-city-states, lagash, first-dynasty-of-ur, umma and kish can be reconciled: 11 city-dossier events name the collective as counterpart with no mirror, and the hegemony keyframes of first-dynasty-of-ur and lagash double-claim cities that their own dossiers keep.
- Not one infobox in the batch gives an area in km2 (Elam, Akkadian Empire, Gutian rule in Mesopotamia, Third Dynasty of Ur, History of Sumer; the rest are city or site pages), so the area checks are recorded with infobox_km2 null.
- No confidence-3 event failed: all seven confidence-3 events in the batch were checked (elam /ledger/11, /21, /25; third-dynasty-of-ur /ledger/13; uruk /ledger/2; lagash /ledger/1; umma /ledger/1) are on their pages with the year. 25 distinct Wikipedia pages opened, none failed.
