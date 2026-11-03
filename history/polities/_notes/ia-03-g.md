# Notes, batch ia-03-g (Central Asian khanates to the republics, part g)

Written 2026-10-19 by the Phase B research agent for ia-03-g. Six dossiers, all validate with 0 errors (`validate_dossier.py --resolve`): afghanistan, mujahideen, kazakhstan, kyrgyzstan, mongolia, republic-of-tajikistan. 22 pages were opened, none failed to load; one URL served the wrong article (see Afghanistan).

## Cross-cutting decisions

- Start years are the real founding dates, not Cliopatria's 1992: Kyrgyzstan 31 Aug 1991, Tajikistan 9 Sep 1991, Kazakhstan 16 Dec 1991, Mongolia 12 Feb 1992. Each of the first three has a new one-year keyframe for 1991 on the 1992 outline, so the USSR dossier (eu-17) and these overlap in 1991. Whoever applies the overlap rule should decide; if the project prefers Cliopatria's 1992 starts, drop the `_1991` keyframes and move the `found` events.
- End year 2024 (the last year of data) for every state alive today; no `dissolve` event.
- The four republics' shapes are each one outline (the area drifts by a few hundred km2 only, from the Aral Sea shoreline at the Kazakh-Uzbek frontier and vertex noise), so their dossiers carry few territorial events. Real treaties (China 1994-2002 / 2009 / 2011, Uzbekistan 2001-2003, Russia 2005-2006) moved strips below one grid cell and are recorded as low-confidence events with the strip named.

## afghanistan (6 pages: budget 5; the 6th served the wrong article)

- `https://en.wikipedia.org/wiki/Afghan_Interim_Government` returned the article on the 2001 Afghan Interim Administration, not the 1989 mujahideen government. Used only for 22 Dec 2001.
- Scope: this dossier starts on 30 April 1978 (the Democratic Republic; republic-of-afghanistan asked for that) and runs to 2024 as one state: Democratic Republic, Republic of Afghanistan (1987), Islamic State (1992), the Northern Alliance rump (1996-2001), Interim Administration, Transitional State, Islamic Republic (2004), Islamic Emirate (2021). The Wikidata id Q889 is shared with emirate-of-afghanistan, kingdom-of-afghanistan and republic-of-afghanistan; they were written as separate dossiers by other parts and are left separate.
- Cliopatria: no Afghanistan shape for 1987-1995 (the whole country is drawn as "Mujahideen"); handled as new keyframes afghanistan_1987 (nominal whole country, contested) and afghanistan_1992 (the Islamic State, claimed from the Mujahideen outline). The 1979 and 1983 shapes have holes at Kabul and the east and are corrected to the whole country. The 1996-1999 and 2000-2005 shapes are the Northern Alliance rump; they run to 2005, four years past the Taliban's fall, so afghanistan_2002 restores the whole country. The Taliban row (1996-2005) should be cut at December 2001 by the taliban dossier.
- Not settled: the 1998-1999 front beyond Balkh; Jan-Sep 1996 territory; faction fiefs 1992-1996 (the Islamic State page names no province); the Durand Line and Wakhan; Taliban-held lands 2002-2005; the 1987 rename date (confidence 1: the page dates the loya jirga but not the renaming). A gap-filler should open the Mazar-i-Sharif and Taloqan battle pages.

## mujahideen (5 pages)

- The Cliopatria "Mujahideen" row is two unrelated things. 1987-1995 is the Afghan resistance and, from April 1992, the state itself; 2014-2024 (68,889 km2) is an outline over northern and north-eastern Syria. Both Syrian shapes are marked wrong.
- The Syrian outline: gazetteer overlay shows Hasakah 94%, Aleppo 78%, Deir ez-Zor 61%, Idlib 48%, Dar'a 43%, Raqqa 35%, Hamah 3%, nothing in Homs, Latakia, Tartus, Damascus. The Mujahideen page does not mention territory in Syria and the Syrian civil war page never uses the word "mujahideen". I could not identify it and did not create a dossier. A Syria group (me-10) should decide: the Syrian opposition, the Islamic State, a Kurdish-led area, or a Cliopatria stand-in; then write a dossier for it or drop the row.
- Afghan part: written as type rebel from 25 Dec 1979 to 28 Apr 1992. mujahideen_1992 is wrong (the outline is afghanistan's, April 1992 onward). 1987 and 1990 shapes are adjusted to cut Kabul out (the government held it until 28 April 1992).
- Not settled: when and why the 1990 shape adds the northern provinces (Jawzjan, Kunduz, Balkh, Faryab, Baghlan); mujahideen territory 1979-1986 (no Cliopatria shape, no page with lines); the factions after 1992. The 1989-1992 war's own article was not opened.

## kazakhstan (5 pages)

- Cliopatria shapes 1992, 1996, 2006: the cell differences (6 and 4 cells) are on the Aral Sea shore at the Kazakh-Uzbek frontier; the Baikonur lease (20 cells, Natural Earth's "Baykonur Cosmodrome") is inside the shape. The lease is not an event (sovereignty stayed Kazakh); a renderer may tint those 20 cells as a client area.
- Confidence-1 events: the Zhalanashkol strip to China (year = the 2002 final protocol, page does not tie the strip to an agreement) and the Bagys gain from Uzbekistan (year = the 9 Sept 2002 treaty; the Kyzylorda land given in return is not located). No wars.

## kyrgyzstan (3 pages: budget 1-2; the Kyrgyz-Tajik border page was opened for Tajikistan)

- 2009 China agreement: Uzengi-Kuush ceded, part of Khan Tengri gained; no areas on the page. Names not in the gazetteer.
- 2021 and 2022 clashes with Tajikistan are contests matched in republic-of-tajikistan.
- Not opened: the Uzbek frontier and the enclaves (Sokh 325 km2 Uzbek, Barak Kyrgyz, Vorukh and Kayragach Tajik).

## mongolia (2 pages)

- One outline, one event (the 1992 re-founding on the Mongolian People's Republic's land). No rulers (the page names only Khurelsukh). Frontier treaties are not on either page.

## republic-of-tajikistan (4 pages of 5)

- Shapes 1992, 2000, 2006 are the identical 474 grid cells. The 2011 China cession (200 and 1,122 km2 for the 1999 and 2002 deals) is recorded as a loss in Gorno-Badakhshan (the page does not locate it; confidence 2).
- The civil war (5 May 1992 to 27 June 1997) is a contest with "United Tajik Opposition", a counterpart with no dossier; no page opened outlines the land it held. A rebel dossier would need a page on the zones.
- No rulers: the pages disagree (1992 or 1994) on Rahmon's start.

## For other groups

- republic-of-uzbekistan and turkmenistan (ia-03): the Bagys exchange (Kazakhstan gains) is the only event naming Uzbekistan here; a matching loss for the Kyzylorda semi-desert land has no location.
- union-of-soviet-socialist-republics (eu-17): successors should list kazakhstan, kyrgyzstan, republic-of-tajikistan with 1991 start dates.
- people-s-republic-of-china (ea-08): counterparts of the 2002 (Kazakhstan), 2009 (Kyrgyzstan) and 2011 (Tajikistan) border treaties.
- taliban (ia-03): cut Cliopatria's row at December 2001; the counterpart string in afghanistan is "taliban".
- islamic-republic-of-pakistan, russian-federation: nothing moved with Afghanistan, Kazakhstan, Tajikistan on the pages opened.
