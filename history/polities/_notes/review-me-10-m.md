# Review of batch me-10-m (2026-10-25)

Reviewer: adversarial review, Phase B. Machine copy: history/notes/phase-b/reviews/me-10-m.json.

Validator (--resolve): all four valid, no errors; warnings are unknown counterpart slugs (no dossiers yet), unpaired ongoing contests (Yemen houthis 2014, STC 2018; Gaza Israel 2023) and the gazetteer lacking Hawija and Sinjar.

## islamic-republic-of-iran: fail

Area: infobox 1648195 km2 vs Cliopatria 1624652 km2, ratio 0.986, acknowledged True.

Findings:
- `/ledger/7/region (and /ledger/8/region, /wars/1/zones/0, /wars/2/zones/0)` (for the author): BLOCKING. The al-Faw occupation (confidence 3) is drawn as the whole Iraqi bank of the Shatt al-Arab within 30 km, which hatches Basra city, Abu al-Khasib and the river up to Qurna as Iranian-held 1986-1988. Evidence: First Battle of al-Faw: 'The Iranian strike force overran the tip of the peninsula, in 24 hours' and 'Iranian troops succeeded in reaching the Khor Abdullah waterway opposite Kuwait'; Second Battle of al-Faw: Iranian forces 'killed or cleared from the al-Faw Peninsula'. No page has Iran holding Basra or the Shatt's west bank north of the peninsula; the Shatt runs past Basra (30.5 N), the bridgehead was at the tip (about 29.95-30.2 N). Fix: Region {"intersect": [{"lon": 48.47, "lat": 29.98, "km": 25}, {"country": "Iraq"}], "text": "the tip of the al-Faw peninsula, from the Shatt al-Arab to the Khor Abdullah opposite Kuwait"} (or {"place": "Al-Faw", "km": 25} intersected with Iraq, listing Al-Faw for the gazetteer) in both ledger events and both war zones.
- `/ledger/6/region (and /ledger/10/region)` (for the author): BLOCKING. The Majnoon occupation is a 90 km circle round Basra: it hatches Basra city, Khorramshahr and Abadan (Iranian land, i.e. Iran 'occupying' itself) and northern Kuwait, and its text adds 'the Basra-Baghdad highway beyond it', which Iran did not hold. Evidence: Iran-Iraq War page: 'By 27 February, they had captured the island' (Operation Kheibar); the dossier's own note says the Iraqi counterattack pushed them back from the outskirts of Qurna. Majnoon lies about 31.0-31.1 N, 47.5-47.6 E, some 60 km north of Basra. Fix: Region {"intersect": [{"lon": 47.55, "lat": 31.05, "km": 25}, {"country": "Iraq"}], "text": "Majnoon Island in the Hawizeh Marshes"}; drop the highway from text.
- `/ledger (missing) and /keyframe_review/2/correction` (for the author): BLOCKING. No ledger event for Iran's capture and hold of Haj Omran in Iraqi Kurdistan (23 July 1983 to the August 1988 ceasefire), although the 1987 correction says the Iraqi-Kurdistan cells 'are Iranian-held Iraqi land, drawn as occupation by the ledger' and /keyframe_review/1/note itself cites Haj Omran; the dossier notes then say no page covers the Kurdish-front gains of 1983. Evidence: Iran-Iraq War page (in sources): 'With Kurdish support, the Iranians attacked on 23 July 1983, capturing the Iraqi town of Haj Omran and maintaining it against an Iraqi poison gas counteroffensive'. Neighbour iraqi-republic.json /ledger/7 (1983-7 contest_start, Haj Omran) and /ledger/9 (1988-8 contest_end) have no mirror here. Fix: Add occupation_start 1983-7, counterpart iraqi-republic, region {"intersect": [{"lon": 45.05, "lat": 36.65, "km": 20}, {"country": "Iraq"}], "text": "the Iraqi town of Haj Omran"} (or a region covering the 36.0-36.2 N, 45.1-45.4 E cells if a page supports them), source the war page, confidence 3; and occupation_end 1988-8 (confidence 2, ceasefire, 'Status quo ante bellum'). Correct the notes sentence that says no opened page covers the 1983 Kurdish front.
- `/ledger/6, /ledger/10 vs iraqi-republic /ledger/8, /ledger/10` (for the author): Non-blocking, cross-dossier. Majnoon is an occupation_start/occupation_end here but a contest_start/contest_end in iraqi-republic.json; the schema says the owner records an occupation 'with the roles reversed'. Evidence: dossier.schema.json event types: 'occupation_start / occupation_end: this state occupies region belonging to counterpart ... the owner records the same event with the roles reversed.' Fix: Orchestrator: route to me-10-k so iraqi-republic records occupation_start 1984-2 / occupation_end 1988 with counterpart islamic-republic-of-iran for Majnoon (and for al-Faw 1986-2 / 1988-4, which it lacks entirely).

Gaps for a gap-filler:
- `/ledger/10`: date Iraq retook Majnoon (confidence 1, set at the ceasefire); the pages opened stop before it (try https://en.wikipedia.org/wiki/Operation_Tawakalna_ala_Allah)
- `/keyframe_review/2`: Karbala-5 (January 1987) east of Basra and the 1987 Iraqi-Kurdistan cells (36.0-36.2 N) (try https://en.wikipedia.org/wiki/Operation_Karbala-5)
- `/ledger/0, /ledger/5`: towns held by the KDPI/Komala in 1979-1982 (contest confidence 2, no ground named) (try https://en.wikipedia.org/wiki/1979_Kurdish_rebellion_in_Iran)
- `/ledger (missing)`: Iraq's 1988 incursions into Iran (Dehloran, Mehran) named in /wars/2 outcome but not in the ledger (try https://en.wikipedia.org/wiki/Operation_Forty_Stars)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Iran: confirmed (referendum 31 March 1979, 99.31%; infobox 'Islamic Republic established: 1 April 1979')
- `/ledger/2` https://en.wikipedia.org/wiki/Iran: confirmed ('On 22 September 1980, the Iraqi army invaded Iran at Khuzestan')
- `/ledger/4` https://en.wikipedia.org/wiki/Iran%E2%80%93Iraq_War: confirmed (drive on Khorramshahr 23 May 1982, city fell in under 48 hours, 19,000 surrendered, 'recaptured all their territory by June 1982')
- `/ledger/6` https://en.wikipedia.org/wiki/Iran%E2%80%93Iraq_War: confirmed ('By 27 February, they had captured the island'); region overdrawn, see fixes
- `/ledger/7` https://en.wikipedia.org/wiki/First_Battle_of_al-Faw: confirmed (Dawn 8 on 9 February 1986, tip overrun in 24 hours, town held out until 14 February, Khor Abdullah reached); region overdrawn, see fixes
- `/ledger/8` https://en.wikipedia.org/wiki/Second_Battle_of_al-Faw: confirmed (17-18 April 1988, Faw town 35 hours in, all Iranian forces killed or cleared within 48 hours)

## republic-of-yemen: thin

Area: infobox 455503 km2 vs Cliopatria 463074 km2, ratio 1.017, acknowledged True.

Gaps for a gap-filler:
- `/wars/0 (zones empty) and /ledger (missing)`: the 1994 civil war: the southern secession (Democratic Republic of Yemen, May-July 1994) held all of former South Yemen and was reconquered; ground changed hands, so empty zones and no contest are a gap, not a no-change war (try https://en.wikipedia.org/wiki/1994_civil_war_in_Yemen)
- `/ledger/3`: Houthi-held extent by year: the contest draws the present-day zone (all former North Yemen except Marib) from September 2014; the 2015 advance to Aden and its reversal, Hodeidah 2018, Marib 2020-2021 are absent (try https://en.wikipedia.org/wiki/Houthi_takeover_in_Yemen)
- `/ledger (missing)`: the Eritrean occupation of the Hanish Islands (1995-1998) and the 1998 award to Yemen; state-of-eritrea.json has no event either (try https://en.wikipedia.org/wiki/Hanish_Islands_conflict)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Yemen: confirmed ('the countries were merged on 22 May 1990, with Saleh as president')
- `/ledger/3` https://en.wikipedia.org/wiki/Yemeni_civil_war_(2014%E2%80%93present): confirmed (infobox '16 September 2014 - present'; Houthis seized Sanaa in September 2014; present snapshot 'all of former North Yemen except for eastern Marib Governorate')
- `/ledger/4` https://en.wikipedia.org/wiki/Yemen: confirmed (Hadi fled to Aden on 21 February 2015; the page puts the 'temporary capital' declaration 'the following month', i.e. March 2015; month 2 = the seat's move, acceptable)
- `/ledger/5` https://en.wikipedia.org/wiki/Yemen: confirmed ('In February 2018, Aden was seized by the UAE-backed separatist Southern Transitional Council')

## gaza-hamas: pass

Area: infobox 365 km2 vs Cliopatria 154.8 km2, ratio 0.424, acknowledged True.

Gaps for a gap-filler:
- `/ledger/1`: the zones Israel held in 2023-2024 (Netzarim Corridor, Philadelphi Corridor, Rafah May 2024); only a whole-Strip contest is recorded (try https://en.wikipedia.org/wiki/Netzarim_Corridor)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Governance_of_the_Gaza_Strip: confirmed (Hamas governance 'began 11 June 2007'; Abbas dissolved the unity government 14 June; 'full takeover of the Gaza Strip by Hamas on 15 June 2007')
- `/ledger/1` https://en.wikipedia.org/wiki/Governance_of_the_Gaza_Strip: confirmed ('the Israeli invasion of the Gaza Strip in early November 2023'; 6 January 2024 statement on northern Gaza)
- `/keyframe_review/1` https://en.wikipedia.org/wiki/Gaza_Strip: confirmed (infobox 'Total: 365 km2'; 'By 14 June, Hamas fully controlled the Gaza Strip'; 2005 withdrawal has no day on the page)

## republic-of-iraq: fix

Area: infobox 438317 km2 vs Cliopatria 438702 km2, ratio 1.001, acknowledged True.

Findings:
- `/ledger/13/note` (applied by reviewer): The note put in quotation marks a sentence the page does not contain ('Following this, the Iraqi armed forces captured Kirkuk and Sinjar.') and said the page does not say from whom. Evidence: War in Iraq (2013-2017): 'Following the defeat of the Peshmerga and the capture of Kirkuk and Sinjar by the Iraqi armed forces...', which names the Peshmerga and supports the kurdistan-region counterpart. Fix: Quote the page's words; counterpart kurdistan-region stands; confidence left at 2 (no separate date for Sinjar).
- `/ledger/14/confidence` (applied by reviewer): Confidence 3 on a region (all of Al-Anbar governorate) the page does not name; it names only Al-Qa'im and Rawah. Evidence: War in Iraq (2013-2017): 'Iraq captured ISIL's last two strongholds of Al-Qa'im and Rawah on 17 November.' (date confirmed). Fix: Confidence 3 -> 2 and a sentence in the note saying the governorate is a reading.
- `/ledger/3/region` (for the author): Non-blocking. Kirkuk's 2014 loss to the Kurdistan Region takes the whole At-Ta'mim governorate in the same month as /ledger/5 gives the Hawija pocket (inside At-Ta'mim) to islamic-state, so the two losses overlap. Evidence: Both events 2014-6; Hawija lies in Kirkuk governorate (the author's own gazetteer hint); /ledger/11 then regains Hawija from islamic-state, /ledger/12 the whole governorate from kurdistan-region. Fix: Region {"minus": [{"admin1": "At-Ta'mim", "country": "Iraq"}, {"place": "Hawija", "km": 40}], "text": "..."} for /ledger/3 and /ledger/12 (both confidence-1/3 events keep their sources).
- `/identity` (for the author): Non-blocking, for the orchestrator. One state in two dossiers (iraqi-republic 1958-2005, republic-of-iraq 2005-2024) against the brief's rule 'one dossier under the earlier slug'; both files agree (iraqi-republic /ledger/15 dissolve 2005-10 counterpart republic-of-iraq; this /ledger/0 found 2005-10), and the author flagged it. Evidence: Iraq page: 'Since January 1992, the official name of the state is "Republic of Iraq"'; author's report problems[0]; research brief section 6 rule on shared Wikidata ids (Q796). Fix: Orchestrator decides: either fold this ledger into iraqi-republic.json (adding 'Republic of Iraq' to its cliopatria_names) or keep the join and give both one colour.

Gaps for a gap-filler:
- `/ledger/3`: Kirkuk's passage to Peshmerga control in June 2014 (confidence 1, page silent) (try https://en.wikipedia.org/wiki/Northern_Iraq_offensive_(June_2014))
- `/ledger/5`: ISIL's capture of Hawija in 2014 (confidence 1, placed from its 2017 recapture) (try https://en.wikipedia.org/wiki/Northern_Iraq_offensive_(June_2014))
- `/ledger/13`: Sinjar: fell to ISIL in August 2014 (not June with Nineveh) and was retaken by Kurdish forces in November 2015; neither date is on the pages opened (try https://en.wikipedia.org/wiki/November_2015_Sinjar_offensive)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Iraq: confirmed (infobox 'Current constitution: 15 October 2005'; referendum October 2005 with 78%)
- `/ledger/2` https://en.wikipedia.org/wiki/War_in_Iraq_(2013%E2%80%932017): confirmed ('seized at least 70% of Al Anbar Governorate by June 2014')
- `/ledger/7` https://en.wikipedia.org/wiki/War_in_Iraq_(2013%E2%80%932017): confirmed ('On December 28, Iraq declared Ramadi liberated')
- `/ledger/8` https://en.wikipedia.org/wiki/War_in_Iraq_(2013%E2%80%932017): confirmed ('Third Battle of Fallujah ending in June 2016')
- `/ledger/9` https://en.wikipedia.org/wiki/War_in_Iraq_(2013%E2%80%932017): confirmed ('On 10 July, Iraqi Army forces captured Mosul')
- `/ledger/12` https://en.wikipedia.org/wiki/War_in_Iraq_(2013%E2%80%932017): confirmed (offensive 'on 15 October against Kurdistan Region to recapture the disputed city of Kirkuk')
- `/ledger/13` https://en.wikipedia.org/wiki/War_in_Iraq_(2013%E2%80%932017): confirmed in substance; quotation corrected
- `/ledger/14` https://en.wikipedia.org/wiki/War_in_Iraq_(2013%E2%80%932017): confirmed (17 November; region not named, confidence lowered)

## Cross-dossier matrix

- islamic-republic-of-iran 1979 found / pahlavi-dynasty -> none: **exception**. pahlavi-dynasty (me-10, another part) has no dossier yet
- islamic-republic-of-iran 1979 contest_start / iranian-kurdish-insurgents -> none: **exception**. no dossier; in counterparts_needing_dossiers
- islamic-republic-of-iran 1980 contest_start / iraqi-republic -> iraqi-republic 1980 contest_start: **matched**. iraqi-republic /ledger/4, 22 September 1980 (both Iran events: Khuzestan and Shatt al-Arab)
- islamic-republic-of-iran 1982 contest_end / iraqi-republic -> iraqi-republic 1982 contest_end: **matched**. iraqi-republic /ledger/6, June 1982
- islamic-republic-of-iran 1982 contest_end / iranian-kurdish-insurgents -> none: **exception**. no dossier
- islamic-republic-of-iran 1984 occupation_start / iraqi-republic -> iraqi-republic 1984 contest_start: **mismatch**. Majnoon: occupation here, contest in iraqi-republic /ledger/8; schema wants occupation on both sides (roles reversed)
- islamic-republic-of-iran 1986 occupation_start / iraqi-republic -> none: **missing**. al-Faw (9-14 February 1986): no event in iraqi-republic.json
- islamic-republic-of-iran 1988 occupation_end / iraqi-republic -> none: **missing**. al-Faw retaken 17-18 April 1988: no event in iraqi-republic.json
- islamic-republic-of-iran 1988 contest_end / iraqi-republic -> iraqi-republic 1988 contest_end: **mismatch**. Iran closes a Shatt al-Arab contest open 1980-1988; iraqi-republic closed its 1980 contest in June 1982 (/ledger/6) and its 1988-8 contest_ends (/ledger/9, /ledger/10) are Haj Omran and Majnoon
- islamic-republic-of-iran 1988 occupation_end / iraqi-republic -> iraqi-republic 1988 contest_end: **mismatch**. Majnoon end: occupation_end here (confidence 1) vs contest_end iraqi-republic /ledger/10
- iraqi-republic 1983 contest_start / islamic-republic-of-iran -> none: **missing**. Haj Omran 23 July 1983 (iraqi-republic /ledger/7, confidence 3): no mirror in islamic-republic-of-iran; fix listed
- iraqi-republic 1988 contest_end / islamic-republic-of-iran -> none: **missing**. Haj Omran returned at the August 1988 ceasefire (iraqi-republic /ledger/9): no mirror in islamic-republic-of-iran
- republic-of-yemen 1990 merge / north-yemen -> north-yemen 1990 dissolve: **matched**. north-yemen /ledger/20 dissolve 1990-5 counterpart republic-of-yemen (and /ledger/19 merge with the PDRY); successor/predecessor agree
- republic-of-yemen 1990 merge / people-s-democratic-republic-of-yemen -> none: **exception**. PDRY (me-10, another part) has no dossier yet
- republic-of-yemen 2014 contest_start / houthis -> none: **exception**. no dossier; in counterparts_needing_dossiers (me-10-x)
- republic-of-yemen 2018 contest_start / southern-transitional-council -> none: **exception**. no dossier; in counterparts_needing_dossiers (me-10-x)
- gaza-hamas 2007 found / palestinian-national-authority -> none: **exception**. no dossier; in counterparts_needing_dossiers
- gaza-hamas 2023 contest_start / state-of-israel -> none: **exception**. state-of-israel (me-10, another part) has no dossier yet
- republic-of-iraq 2005 found / iraqi-republic -> iraqi-republic 2005 dissolve: **matched**. iraqi-republic /ledger/15 dissolve 2005-10 counterpart republic-of-iraq
- republic-of-iraq 2014 loss / islamic-state -> none: **exception**. three losses 2014 and seven gains 2015-2017 plus the contest pair; islamic-state has no dossier (me-10-x); the mujahideen dossier (ia-03) ends in 1992 and does not cover Cliopatria's 2014-2024 Mujahideen shapes
- republic-of-iraq 2014 loss / kurdistan-region -> none: **exception**. Kirkuk June 2014 (confidence 1); kurdistan-region has no dossier; iraqi-republic uses the same slug (1992 loss, 2005 gain), consistent
- republic-of-iraq 2017 gain / kurdistan-region -> none: **exception**. Kirkuk and Sinjar October 2017; no dossier yet

## Problems

- Iran-Iraq War page: WebFetch text did not cover Majnoon's 1988 recapture or Karbala-5 for me either (same truncation the author reported).
- republic-of-iraq duplicates the state of iraqi-republic (me-10-k) by design of the author; needs an orchestrator decision (fold or keep the join).
- Neighbour dossiers present and read (ledgers grepped): iraqi-republic, north-yemen, kingdom-of-saudi-arabia, sultanate-of-oman, state-of-kuwait, turkmenistan, afghanistan, mujahideen, islamic-republic-of-pakistan, taliban, republic-of-djibouti, state-of-eritrea, united-states-of-america, ethiopia; not yet written: republic-of-turkey, kuwait, french-fifth-republic, kingdom-of-great-britain, republic-of-armenia, republic-of-azerbaijan, union-of-soviet-socialist-republics, arab-republic-of-egypt, state-of-israel, kingdom-of-jordan, syria (their groups have not run).
- Reviewer applied two small fixes to republic-of-iraq.json (/ledger/13 note quotation, /ledger/14 confidence 3->2); the file re-validates.
