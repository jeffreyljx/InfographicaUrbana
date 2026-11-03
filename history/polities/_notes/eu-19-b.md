# eu-19-b notes (Caucasus, part b): caucasian-albania, caucasian-iberia, lazica, georgia, balasagan

Run of 2026-11-01. Five dossiers written, each validates with 0 errors (python3 -I tools/validate_dossier.py; --resolve resolves every region). 15 distinct English Wikipedia pages were opened with WebFetch on 2026-11-01; every event, verdict and war cites one of them. Three pages failed to load by their titles (below). No page was fetched for Seshat. All event dates come from a page or are confidence 1 with "page silent" in the note.

| slug | years | shapes reviewed | events | pages |
| --- | --- | --- | --- | --- |
| caucasian-albania | -63..510 | 9 Cliopatria + 1 new (260) | 7 | 2 |
| caucasian-iberia | -302..533 | 7 Cliopatria + 2 new (-302, 260) | 6 | 3 |
| lazica | -63..637 | 10 Cliopatria + georgia_567 + 2 new (546, 577) | 8 | 4 |
| georgia | 1918..2024 (two lives) | 5 Cliopatria + georgia_638 (wrong) + 3 new (1991, 1994, 2008) | 19 | 8 |
| balasagan | 638..645 | 2 | 2 | 2 |

## The Georgia row (567..2024) is split, no new slug
- georgia_567 (567-576) = Lazica's 534-545 outline: reviewed in `lazica` (cliopatria_names ["Lazica", "Georgia"]).
- georgia_638 (638-646) = the Caucasian Iberia outline (136 of 137 cells): verdict wrong in `georgia`, pointing at principality-of-iberia (its _588 keyframe covers 588-681). Nobody else reviewed it.
- georgia_724..980 = the Kingdom of Abkhazia: reviewed in kingdom-of-abkhazia (eu-19-x). Not touched.
- georgia_1918..2024 = modern Georgia: `georgia`. The validator's 11 "no verdict" warnings in lazica/georgia are the shapes left to the other dossiers.

## lazica
- One state with kingdom-of-lazica (Q136884, same Wikipedia article, infobox 131-697). Not merged because that dossier (eu-19-c, 638..777) belongs to another batch: lazica ends 637 with a bookkeeping dissolve, kingdom-of-lazica starts 638. The orchestrator may merge them under `lazica` and keep one colour.
- Gaps 546-566 (Lazic War) and 577-637 are bridged with the 545/576 outline at confidence 1; Persian holdings in the war are undated on the pages, so the contest zone is the whole kingdom.
- 62: Nero annexes Pontus "including Colchis" (Polemon II page); Cliopatria steps in 68. Keyframes lazica_-63 and lazica_68 keep the shapes but move the date to 62. roman-empire already records its 62 gain with counterpart kingdom-of-pontus; mine has counterpart roman-empire.
- Vassal relations (Lazica to Rome, Persia, Byzantium, Arabs) belong to the suzerains' ledgers (eastern-roman-empire has them 395-541, 551-617, 626-632).
- Lazic War: Petra siege years (550-551), Persian withdrawal and Gubazes II's murder year are not on the Lazic War page (the Lazica page gives 555).

## caucasian-albania
- Ends 510 (Vachagan III r. 485-510; Cliopatria 509; sasanian-empire gains it in 510). The page runs Albania on as a Sasanian province under Mihranid princes to 821-22; nothing draws 510-645 separately. A dossier "Mihranid principality of Arran (Aghvank)" 510-822 would be a gap-filler's job.
- Area: Cliopatria 50,113 km2 (to 386) against the page's "approximately 23,000 km2" (ratio 2.18, beyond a factor of two) and 74,782-75,001 km2 against "about 45,000 km2" (1.66). Kept; right-bank Karabakh cells removed before 387 and added after (the page's 387 gain is "all the right bank of the river Kura up to river Araxes, including Artsakh and Utik" while Cliopatria's 387 step goes toward the Caspian).
- 260-286 has no Cliopatria shape; a new keyframe carries the kingdom as a Sasanian vassal that "retained its monarchy". The vassal tint is the sasanian-empire dossier's (it has none for Albania before 510) and the Roman protectorate c. 297-300 is roman-empire's.
- Capital move (Qabala to Partaw) is 387 on one section of the page and "the 5th century" on another: confidence 1.

## caucasian-iberia
- Start -302 from the page (Pharnavaz I, c. 302 BC) with a new Kartli keyframe -302..-64; end 533 (Cliopatria) although the Kingdom of Iberia page abolishes the monarchy in 580. The sasanian-empire dossier gains Iberia in 534; principality-of-iberia starts 588. 534-587 is drawn Persian.
- Contests recorded: Vakhtang I's rising 482-502 and the 523-532 revolt/Iberian War, both with counterpart sasanian-empire. sasanian-empire has the vassal 260-524 as vassal_start/end on caucasian-iberia.
- Tbilisi as capital is undated on the page (Vakhtang I, 447-502): from 447, confidence-low note.
- Pages that failed: Peace_of_Nisibis_(298), Partition_of_Armenia_(387). The Peace of Nisibis (299) article loaded and gives the Iberian clause.

## balasagan
- Cliopatria's 638-646 outline is the Albania 509 outline (9 cells differ). The page says Balasagan is the Dasht i-Balasakan = Mughan plain and "Nothing is known about the Kingdom of Balasagan": both shapes are trimmed to a 90 km disk on the Mughan (about 11,000 km2). The state ends c. 645 (Arab conquest, Salman ibn Rabi'a), Cliopatria 646. No capital on the page. The orchestrator may drop the dossier and treat the land as Sasanian then Rashidun (sasanian-empire dossier has the Albanian lowlands from 510).

## georgia
- One dossier for 1918-1921 and 1991-2024 (the Georgian SSR dossier names slug georgia as predecessor and successor). The 1921-1991 interruption is a ledger loss (March 1921) and gain (April 1991) with counterpart georgian-soviet-socialist-republic. Could equally be two dossiers; see the dossier note.
- Keyframes follow the republic-of-abkhazia and republic-of-south-ossetia dossiers: Tskhinvali disk (28 km) cut out from 1991, Abkhazia minus the Upper Kodori disk (25 km at 41.9E 43.05N) from September 1993, Kodori and Akhalgori (20 km at 44.49E 42.12N) from August 2008. Contest end for Abkhazia is 27 September 1993 here and 1994 there. The South Ossetian war has no start date on the Georgian-Ossetian conflict page (sibling has 5 January 1991).
- Not drawn (page gives no date or Cliopatria omits them): Artvin and Ardahan "regained" from the Ottomans; Zaqatala; Sochi 1918-19; the Volunteer Army; the 2004 Adjara crisis; the Treaty of Moscow (7 May 1920). georgian-soviet-socialist-republic has a confidence-1 gain of the Artvin Okrug from georgia that has no mirror here.
- Infobox area: 69,700 km2 (Georgia page; 67,900 km2 in the Geography section) against Cliopatria 68,876; the DRG infobox gives 75,110 km2 (1918) and 107,600 km2 (1919) against 70,484 and 72,873: inside a factor of two.
- Failed page: South_Ossetia_War_(1991-1992); the Georgian-Ossetian conflict article was used. Not opened (budget 9, used 8): Treaty of Kars, Transcaucasian Democratic Federative Republic, Zaqatala and Sochi disputes.
- Counterpart slugs without a dossier: transcaucasian-democratic-federative-republic (1918), "United Kingdom (British occupation force)" (a name), "zviadists" (a belligerent label). armenia (Cliopatria 1918-1919) is eu-19's.

## Gazetteer names needed
- Mughan plain (region, 48.6E 39.55N; Dasht i-Balasakan) for balasagan.
- Gori, Zugdidi, Senaki (places, Georgia) for georgia's 2008 occupation; lon/lat disks used.
- Utik (region, the Armenian province on the right bank of the Kura, Barda) is not in the gazetteer; Karabakh was used.

## Pages that failed
- https://en.wikipedia.org/wiki/Partition_of_Armenia_(387)
- https://en.wikipedia.org/wiki/Peace_of_Nisibis_(298)
- https://en.wikipedia.org/wiki/South_Ossetia_War_(1991%E2%80%931992)
