# Review of batch eu-15-a (Samo, Great Moravia, Principality of Nitra, Magyars, Duchy of Bohemia, Nitra)

Reviewer, 2026-10-25. All six dossiers validate with `--resolve` (0 errors, 0 warnings) before and after the reviewer's edits. Pages opened with WebFetch: Samo's Empire, Sorbs, Carantania, Great Moravia (3 reads), Nitra, Battle of Pressburg, Wilhelminer War, Bořivoj I, Rastislav, Svatopluk I, Duchy of Bohemia (2 reads), Mieszko I, Etelköz, Pechenegs, Hungarians, Principality of Nitra. Geometry checked with `tools/gazetteer.py resolve` on Cliopatria shapes. No infobox of the six articles gives an area, so no area comparison was possible for any state.

Verdicts: samo-s-empire thin; great-moravia FAIL; principality-of-nitra fix (applied); magyars FAIL; duchy-of-bohemia thin (one fix applied); nitra fix (applied).

No confidence-3 event was found fabricated or mis-dated: GM 833 (Nitra page "In 833"), GM/DoB June 895, DoB 955 Moravia ("fought in the 955 Battle of Lechfeld and after the defeat of the Magyars received the lands of Moravia"), Magyars 895 Etelköz ("around 895"), PoN 833 all confirmed.

## Edits made by the reviewer (re-validated)

- principality-of-nitra /ledger/1: source changed from the Great Moravia page to the Nitra page ("In 833, Pribina was ousted by the Moravian prince Mojmír I"); the misquote 'Around 833, he expelled Pribina' (not on the Great Moravia page, which has "early 830s", Mojmír expelled 'one Pribina', Ratpot "from around 833") replaced in all notes.
- great-moravia /ledger/7 and /ledger/8 (890 vassal_end, gain): source changed from the Bořivoj page (gives only c. 889, no 890) to the Svatopluk I page ("during the winter of 890"). The same 833 misquote and the misquote "later ruled as an appanage by the heir" (page: "was ruled autonomously by the heir of the dynasty as an appanage") corrected throughout.
- duchy-of-bohemia /ledger/1 (890 loss): source changed to the Svatopluk I page for the same reason.
- nitra: the appanage misquote corrected in the identity, ledger and keyframe notes.

## great-moravia: FAIL (back to the author)

1. BLOCKING. /ledger/10 (896 loss to `nobody`, 183,100 km2) contains 53,109 km2 (19.1-23.4E, 47.5-49.5N: eastern Slovakia and the upper Tisza) that magyars /ledger/3 gains in 895, also from `nobody`. The same land is lost to nobody by one dossier and gained from nobody by the other, a year apart, and both are in this batch. Fix: split /ledger/10: `{"intersect": [<current region>, {"cliopatria": "Magyars", "year": 896}]}` lost to `magyars` (895 or 896, the same year as the magyars gain), the rest to `nobody`; mirror in magyars.
2. BLOCKING. Nitra 898: /ledger/11 is only a `vassal_start` naming `nitra`, but Nitra is direct land from the 833 gain and no event removes it; the 898 keyframe drops it and the `nitra` dossier is founded in 898 with counterpart great-moravia. Fix: add `{"year": 898, "type": "split", "counterpart": "nitra", "region": {"cliopatria": "Nitra", "year": 898}, "confidence": 1}` before the vassal_start (as the Bohemian 890 vassal_end + gain does in the other direction).
3. /ledger/13 (900 loss, 8,852 km2, counterpart principality-of-hungary, c1): the whole region lies inside Cliopatria's East Franks 900 shape (35 of 35 cells) and on the west/south edge, as the author's note suspects. Fix: counterpart `east-franks` (east-franks has no gain from great-moravia in 900: route to eu-07), or say why Hungary.
4. /ledger/17 (907 dissolve, counterpart principality-of-hungary, region = the Czech remnant of Moravia, about 20,000 km2): Cliopatria's Principality of Hungary shapes hold none of it in 900, 911, 920, 930 or 950 (0-2 cells), and duchy-of-bohemia /ledger/4 gains Moravia in 955 from `nobody`. The Battle of Pressburg page gives only "Hungarian suzerainty over the rest of Moravia". Fix: counterpart `nobody` for the remnant (the Hungary dossier may record a vassal_start of Moravia), keeping principality-of-hungary for the 902 eastern loss.
5. Keyframes /keyframe_review/4-9 and /ledger/3, 7, 8, 9 use `{"region": "Bohemia"}` (58,926 km2). It is larger than Cliopatria's Bohemia (45,600 km2) and overlaps the Moravian shapes: the 860-889 corrections remove 7,334 km2 (15.4-16.7E, 49.1-50.2N) that Great Moravia held in 814-859, and 14,415 km2 of the 860 shape inside "Bohemia" is held by neither dossier in 870-889 (the Duchy's 870 keyframe is the Cliopatria 896 shape). Fix: use `{"cliopatria": "Duchy of Bohemia", "year": 896}` in place of the region in the corrections and in the 872/890/895 events (and in duchy-of-bohemia /ledger/1-2).
6. Minor: the Wilhelminer War entry ends 884 but /ledger/6 contest_end is 885 (page: "An actual agreement was not reached between the Moravians and Arnulf until late 885"); set the war's `to` to 885. /ledger/2 (850, c2): the Rastislav page dates the eastern gain only "in the first eight years of his reign" (846-854); say so in the note.
7. Thin: /ledger/4 (875, c1, 132,267 km2: Vistula, Silesia, Lusatia), /ledger/10 (c1), /ledger/11 (c1), /ledger/13 (c1).

## magyars: FAIL (back to the author)

1. BLOCKING. /ledger/3 (895 gain from `nobody`, 121,392 km2) includes the 53,109 km2 of Great Moravia's 892-895 shape described above. Fix: split off `{"intersect": [<current region>, {"cliopatria": "Great Moravia", "year": 892}]}` as a gain from `great-moravia`, same year as the great-moravia loss.
2. Thin (within the 5-page budget): /keyframe_review/4 (884: -14,000 km2 with no event); seven confidence-1 events (/ledger/0, 4-9). The author's gaps say the Kabar revolt is undated: the Hungarians page has "Around 830, a rebellion broke out in the Khazar khaganate" (no land, so no event needed).
3. Matched: the 892 and 895 losses to the Pechenegs are mirrored in pechenegs /ledger/2-3 (the pechenegs dossier now exists; drop it from counterparts_needing_dossiers).

## samo-s-empire: thin

Spot checks confirmed: 623 (c. 623-624, revolt of 623-24), 631 Sorbs (Sorbs page: "after Samo's decisive victory against Frankish King Dagobert I in 631"), 658 Carantania ("In 658 Samo died and his Tribal Union disintegrated"), 658 Avars ("at least to southernmost modern Slovakia").

1. /ledger/1 (631 gain from the Sorbs): the region (633 minus 627 shape, 23,520 km2, bbox 12.1-14.6E, 46.5-51.7N) includes 6,828 km2 at 46.5-48.4N (Upper Austria and Salzburg), which is not Lusatia; bavarians /ledger/4 records it as a 633 loss to samo-s-empire (c1). Fix: limit the Sorbian gain to the northern part and add a gain from `bavarians` (c1) for the southern strip, or explain it in the 633 verdict.
2. /ledger/3 (658 loss to the Avars, region = all of the shape in Slovakia, 32,877 km2, including Nitra, which the page calls the union's centre): the page says only "at least to southernmost modern Slovakia", and the avar-khaganate mirror (/ledger/15, 661, c1) takes back 5,058 km2 of Samo's shape in Burgenland and western Hungary, none in Slovakia. Fix: narrow the region to southern Slovakia or to the Avar 661 shape, rest to `nobody`.
3. /ledger/2 (658 loss to carantania): carantania is founded in 661 (Cliopatria year) in its own dossier, so the land has no holder 658-660. Samo's side follows its page; route to eu-06 (carantania could start 658).
4. Thin: /ledger/4 (c1, loss to nobody); bavarians /ledger/5 (661) gains 2,529 km2 of it from samo-s-empire.

## principality-of-nitra: fix (applied)

Confirmed: infobox "Independent state (825-833)", "Established: c. 825", capital Nitra (inside the shape bbox), ruler Pribina 825-833; 833 on the Nitra page. Mirror of great-moravia 833 gain. Source and quote corrected (above).

## duchy-of-bohemia: thin

Confirmed: 870 ("formed around 870 by Czechs as part of the Great Moravian realm"), June 895 (Great Moravia page), 955 Moravia (c3, Duchy page names Lechfeld 955), 990 Silesia (Mieszko page: war of 990, annexation "possibly ... around 985"), 1002 enfeoffment of Vladivoj. Source of /ledger/1 corrected.

1. /ledger/1-2 use `{"region": "Bohemia"}` (58,926 km2) against keyframes of 45,600 km2; the region overlaps Great Moravia's 896 shape. Use the Cliopatria Duchy of Bohemia 896 shape (see great-moravia item 5).
2. /ledger/4 (955 Moravia from `nobody`) disagrees with great-moravia's dissolve to principality-of-hungary; resolved on the great-moravia side (item 4), no change here unless the author prefers the other reading.
3. /ledger/7 (1002 dissolve to holy-roman-empire): the page has "Raised to Kingdom: 1198" and the duchy continued; holy-roman-empire has no event receiving Bohemia in 1002, and margraviate-of-meissen /ledger/8 records a 1076 loss to `duchy-of-bohemia`, a counterpart this dossier says no longer exists. The author flagged the 1003-1201 gap; the orchestrator should route it (extend this dossier to 1198/1201 with new keyframes, or hand over to kingdom-of-bohemia as a rename).
4. Thin: /ledger/3 (947 Silesian slice, c1), /ledger/5 (960 Kraków, c1); rulers missing for 889-935 and 999-1002 (Spytihněv I, Vratislaus I, Wenceslaus, Boleslaus III).
5. Overlord-side vassal events agree with the pages: east-franks 895 (fealty to Arnulf), kingdom-of-germany 929 and 950. kingdom-of-germany draws a 936-950 contest zone over Bohemia; this dossier's war has empty zones ("no land changed hands"); minor.

## nitra: fix (applied)

Confirmed: infobox "Vassal of the Great Moravia (833-906/907)", "Principality of Hungary (906/907-1000/1001)"; the 898 start is Cliopatria's (c1, page silent). The great-moravia side owes the 898 split (great-moravia item 2). Quote corrected.

## Cross-dossier mismatches to route

- avar-khaganate (eu-06): /ledger/7 loss to samo in 626 against Samo's found in 623; /ledger/15 gain from samo in 661 (c1) against Samo's 658 loss, and on different land.
- bavarians (eu-06): /ledger/4 (633 loss to samo) and /ledger/5 (661 gain from samo) have no mirror in samo-s-empire.
- carantania (eu-06): found 661 against Samo's 658 loss to carantania.
- kingdom-of-the-franks (eu-07): /ledger/90 (814 loss to great-moravia, c1) against great-moravia's found in 822 from nobody (page: "The earliest certain reference to Moravians ... is dated to 822").
- east-franks (eu-07): no gain for great-moravia /ledger/13 if its counterpart becomes east-franks.
- holy-roman-empire (eu-08): no event receiving Bohemia in 1002; margraviate-of-meissen: 1076 counterpart duchy-of-bohemia after its end.
- Not yet written (exceptions): principality-of-hungary, kingdom-of-poland (eu-15 other parts), first-bulgarian-empire (eu-18); "Sorbs under Dervan" has no dossier.

## Gazetteer names needed

Lusatia, Etelköz, Pannonia (regions) and Mikulčice (place): none resolves; all are used in text only.
