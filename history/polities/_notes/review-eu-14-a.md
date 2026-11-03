# Review of batch eu-14-a (2026-10-25)

Reviewer: adversarial pass, Phase B. Dossiers: norse, scandinavian-minor-kingdoms. Both validate (`--resolve`, 0 errors, 0 warnings). No dossier was edited by the reviewer. Machine copy: history/notes/phase-b/reviews/eu-14-a.json.

## norse: thin (by design, page budget 5 for 6 shapes)

What I tried and could not break: ledger order and life (found 161, dissolve 499); every shape change has a gain event; new keyframe norse_200 carries from/to/correction; capital Gudme (10.68E 55.15N) lies inside the 161 bbox; family `nordic` exists; certainty covers 161-499; the norse->SMK handover agrees on both sides. Spot checks (4): /ledger/0 and /ledger/2 on Roman Iron Age (period 1-400 AD, page silent on 161/184/207; 'Norway's first royal seat was founded at Avaldsnes in c. 200 AD') confirmed; /ledger/5 and /ledger/6 on Danes (tribe) confirmed in substance. Area: Norse is a disambiguation page, no infobox; nothing to compare.

Non-blocking fixes:
- /identity/capitals/0: Gudme from 161, but the page dates the hall 'mid-3rd century'. Start at 250 or say the year is the shape's.
- /ledger/5/note: the Danes quote is a paraphrase; the page reads 'Some time around the middle of the First Millennium, both Jutland and Angeln became part of Danish kingdom or kingdoms. So was southern Schleswig'.

Thin (confidence 1, pages silent): /ledger/0, 1, 3, 4, 5, 6. Pages to try: Germanic Iron Age, Jutes, Geats, Svear, History of Gotland.

## scandinavian-minor-kingdoms: fail (one blocking finding)

Blocking:
- Missing 934 loss to kingdom-of-germany. kingdom-of-germany /ledger/11 gains Schleswig ({place: Hedeby, km: 40}) from this row in 934 at confidence 3; the Henry the Fowler page says he 'also conquered Schleswig in 934'. This row's 875 keyframe is 'ok' for 875-935 and holds Hedeby (54.49N) inside it (minlat 54.21). Add the 934 loss (source Henry_the_Fowler, add to sources), a new keyframe 934-935 = SMK@875 minus that region (adjust), and a war entry with the zone; say how the Danish 936 shape, which contains Schleswig, relates.

Non-blocking fixes:
- /ledger/4: the 804 Eider-strip gain names `nobody`, but kingdom-of-the-franks holds the strip in its Cliopatria shape to 813 and records a 814 loss of it to this row (/ledger/91). The 806 correction double-holds the strip 806-813. Name kingdom-of-the-franks or explain; eu-07 should adjust its 800-813 shapes or move its loss to 804.
- /wars/0: Gudfred war has empty zones and no obotrites belligerent, but the ledger gains land in 804 and obotrites carries contest_start 808 / contest_end 810 against this row (Reric, 808, on the Hedeby page). Add obotrites, the zone Obotrites@806 and the mirror contest pair.
- /ledger/8 note: the Harald Fairhair page puts Värmland in the 866 sentence ('In 866, Harald made the first of a series of conquests ... including Värmland in Sweden'), not 'undated'. Correct, and decide whether Värmland is contested/lost from 866.
- /identity/predecessors: angles names this row as successor of Angeln; add angles (Angeln, nobody's 479-499) or settle with eu-06.
- /identity/capitals/0: Old Uppsala to 1002, but Uppland leaves for kingdom-of-sweden in 980; end at 979 or note it as a label position.
- /ledger/15 and /wars/2: Svolder is '999 or 1000' on the Olof Skötkonung page.
- /identity/successors/2/land: the region is the 1000 remainder (53,937 km2) while the text describes all three Swedish handovers; use SMK@979 or a union.

Spot checks (5): /ledger/5 and /ledger/9 (Harald Fairhair: 866 conquests, 872 Hafrsfjord, Hålogaland undated), /ledger/12 (Gorm: 'reigning from c. 936', Jelling, 'only ruled Jutland'), /ledger/15 (Olof: Swedes and Geats, Västergötland bishopric, c. 995), /ledger/4 (Gudfred: Eider 'Denmark's southern boundary at the time' in 804): all confirmed. Area: Vendel Period has no infobox or area; nothing to compare.

Thin (confidence 1): /ledger/1 (523), /ledger/2-3 (793), /ledger/7 (Hålogaland 870), /ledger/8 (870 Swedish cells), /ledger/11 (875; 4 dropped cells have no loss), /ledger/13 (960), /ledger/14 (980), /ledger/15-16 (1000, 1002).

## Cross-dossier matrix (short)

- matched: norse 499 dissolve <-> SMK 500 found; SMK 866 loss <-> old-kingdom-of-norway 866 found; SMK 870 loss <-> OKN 870 gain (Hålogaland); SMK 872 loss <-> OKN 872 gain (Rogaland).
- missing: kingdom-of-germany 934 gain from SMK (c3) has no SMK loss; obotrites 808-810 contest against SMK has no SMK pair.
- mismatch: SMK 804 gain from nobody vs kingdom-of-the-franks 814 loss to SMK (10 years, counterpart); angles 479 dissolve to SMK, which begins in 500 and lists no angles predecessor; SMK contest 866-872 vs OKN with no contest events.
- exception (groups not yet run): SMK 936, 960 losses to kingdom-of-denmark; 980, 1000 losses and 1002 dissolve to kingdom-of-sweden. All norse gains and the SMK 523/793/870/875 changes are from nobody.

Routing: eu-06 (angles successor), eu-07 (Franks Eider strip 804-813), this group's author (934 Schleswig loss, obotrites contest, predecessor).
