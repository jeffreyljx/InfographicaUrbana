# Review of batch eu-16-c (Rus principalities, part c), 2026-10-31

Reviewer: adversarial reviewer, Phase B. Inputs: the six dossiers, the author's report and notes, the neighbour dossiers that exist (rus, mongol-empire, grand-duchy-of-lithuania, golden-horde, livonian-brothers-of-the-sword, principality-of-galicia-volhynia, halych-volhynia-occupation, principality-of-turov-and-pinsk and the rest in section 6 of the author's brief). Not written yet (group has not run): kievan-rus, principality-of-kiev, principality-of-chernigov, novgorod-republic, principality-of-minsk, principality-of-drutsk, principality-of-vitebsk, principality-of-jersika, principality-of-peremyshl, principality-of-halych, grand-principality-of-moscow, principality-of-vladimir-suzdal, ryazan, tver, kingdom-of-poland.

Mechanical: the validator with --resolve gives 0 errors for all six; one warning (principality-of-volhynia /ledger/2 counterpart principality-of-lutsk has no dossier; listed by the author under counterparts_needing_dossiers).

Spot checks: 27 events opened on 11 pages (Principality of Smolensk, Yuri Dolgorukiy, Vladimir-Suzdal, Mongol invasion of Kievan Rus', Principality of Vitebsk, Principality of Polotsk, Principality of Ryazan, Principality of Volhynia, Roman the Great, Principality of Terebovlia). No fabricated event found; one mis-dated event (Ryazan contest_end) fixed by the reviewer.

## Verdicts

| slug | verdict | why |
| --- | --- | --- |
| principality-of-polotsky | fail | the 1101 division drops about 67,000 km2 with no event (Jersika and Koknese not split off, Minsk drawn as a 60 km disc); Kiev's 1129 annexation and the 1195 return of Vitebsk are not land events |
| principality-of-smolensk | thin | all c3 events confirmed; the three largest moves (1294 +34,700, 1359 band, 1375 north) are confidence-1 bridges; one contest without a war |
| principality-of-rostov-suzdal | thin | all c3 events confirmed; the 1126 growth (+75,700 km2, the largest move) is a confidence-1 bridge; dissolve 1240 against the page (orchestrator decision) |
| principality-of-ryazan | fix (reviewer) | contest_end moved 1240 -> 1238 on the pages; dissolve 1240 against the page (orchestrator decision) |
| principality-of-volhynia | fix (reviewer) | found 1054 raised to confidence 2 (page's list of princes: Igor Yaroslavich 1054-1057) |
| principality-of-terebovlia | thin | within its 1-2 page budget; the 1094 growth is a bridge, though the page names its land |

## principality-of-polotsky: fail

1. /ledger/4-6 and /keyframe_review/3 (blocking, missing events, unexplained area). The 1085 shape (133,005 km2, held to 1100) gives way in 1101 to Polotsk proper (the 1202 core minus a 60 km Vitebsk disc, about 23,000 km2). The splits name Vitebsk (60 km disc, about 11,300), Minsk (60 km disc, about 11,300) and Drutsk (Cliopatria Drutsk 1111, 19,978). About 67,000 km2 (Latgale, Koknese, the Minsk land beyond 60 km, the Vilnius side) leaves with no event. Evidence: the Principality of Polotsk page lists Jersika and Koknese among the fiefs that split off from Polotsk after Vseslav's death, and says the principalities of Jersika and Koknese 'had previously been under the control of Polotsk' (crusader conquest 1209). Cliopatria 1111: Minsk 52,681 + Drutsk 19,978 + Vitebsk 34,385 + Jersika 23,422 + Koknese 2,162 = 132,628 km2, the 1085 Polotsk shape almost exactly. Fix: add `split` 1101 counterpart principality-of-jersika (region {"cliopatria": "Principality of Jersika", "year": 1111}) and `split` 1101 counterpart principality-of-koknese ({"cliopatria": "Principality of Koknese", "year": 1111}), source Principality of Polotsk, confidence 2; change /ledger/5's region to {"cliopatria": "Principality of Minsk", "year": 1111} (as /ledger/6 does for Drutsk).
2. /ledger/7-8 (blocking, missing events, note contradicts page). The Principality of Vitebsk page: in 1129 Mstislav 'captured the three remaining sons of Vseslav' and 'annexed Polotsk and its vassals including Vitebsk'; in 1132 the residents 'invited Vasilko to claim the Principality of Polotsk'. Polotsk infobox: 'Vassal of Kievan Rus' (978-1001, 1127-1132)'. /ledger/7's note says 'The page gives no ground taken'. Fix: end the contest in 1129 and add `loss` 1129 and `gain` 1132 with counterpart principality-of-kiev (region: the dossier's 1101 Polotsk-proper shape), source Principality of Vitebsk, confidence 2. Or, if you read the infobox's vassalage as stronger evidence, keep the contest, correct the note, and list a 1127-1132 vassalage for the principality-of-kiev owner. Either way the note must quote 'annexed'.
3. /keyframe_review/4 and the ledger at 1195 (blocking, missing event). The 1195 keyframe adds the Vitebsk disc back, but the only event in 1195 is a contest_end with Smolensk, which moves no land. The Vitebsk page: the princes who 'in 1195 marched against the prince of Smolensk', after which 'Vitebsk again fell under the rule of Polotsk'. Fix: add `gain` 1195 counterpart principality-of-vitebsk (the 1101 split's counterpart), region {"place": "Vitsyebsk", "km": 60}, source Principality of Vitebsk, confidence 2.
4. Confirmed: /ledger/4 (1101 division, Vitebsk to Sviatoslav), /ledger/7 (1127), /ledger/8 (1132), /ledger/9 (1165-1167 Smolensk), /ledger/13 (1307: 'It officially became part of Lithuania in 1307').
5. Area: infobox 100,000-120,000 km2 (greatest extent, no year) against Cliopatria 103,984 (1056) and 133,005 (1085). Acknowledged in /keyframe_review/1-2.
6. Thin: /ledger/3 (1085 gain, confidence 1). Pages to try: Principality of Jersika, Latgalians.

## principality-of-smolensk: thin

- Confirmed on the Principality of Smolensk page: /ledger/1 (1125 'It became an independent principality in 1125'), /ledger/6 (1239 'briefly captured by the Lithuanians in 1239', expelled 'the following year'), /ledger/10 (1356), /ledger/14 (1395), /ledger/15 (1401 revolt and recall of Yury), /ledger/16 (1404 'incorporated into the Grand Duchy of Lithuania in 1404').
- Area: the infobox gives none. Acknowledged in /keyframe_review/1.
- Fix (non-blocking, author): /wars has no war for the 1239-1240 contest with grand-duchy-of-lithuania (/ledger/6-7). Add a war 'Lithuanian capture of Smolensk' 1239-1240 (smolensk, grand-duchy-of-lithuania, principality-of-rostov-suzdal for Yaroslav Vsevolodovich), zone {"place": "Smolensk", "km": 60}, source Principality of Smolensk. The 'Vytautas's conquest of Smolensk' war (1395-1404) has empty zones though land changed hands. Its note should say the transfers are the ledger's loss and gain events of 1395, 1401 and 1404.
- Thin, the largest moves at confidence 1: /ledger/8 1294 gain from nobody (+34,700 km2, Gomel and Rzhev; in 1293 that land sat in the Mongol Empire shape; Gomel was Chernigov land); /ledger/12 1359 loss of the south-west band (year inferred from Algirdas's 1359 campaign, region Cliopatria's 1363); /ledger/13 1375 loss of the north (Velikiye Luki, Toropets); /ledger/9 1304 Mozhaysk (check 1303 or 1304 on the Mozhaysk page). Pages to try: Rzhev, Principality of Bryansk, Mstislavl, Toropets, Mozhaysk.

## principality-of-rostov-suzdal: thin

- Confirmed: /ledger/2 (1125, Vladimir-Suzdal page 'moved his capital from Rostov to Suzdal in 1125'), /ledger/4-6 and /ledger/8 (Yuri page '(in September 1149 - April 1151, again in March 1155 - May 1157)', 'In 1155, Yuri regained Kiev once again', death 15 May 1157), /ledger/7 (infobox Suzdal 1125-1157, Vladimir 1157-1389), /ledger/11-12 (siege of Vladimir 4 February 1238, Sit River 4 March).
- Area: no infobox area. Acknowledged.
- Orchestrator decision (non-blocking): /ledger/13 dissolve 1240, confidence 1. The Vladimir-Suzdal page has the state established 1125 and disestablished 1389, Alexander Nevsky (1252-1263) 'the last prince to reign directly in Vladimir', and 'by 1389, the two thrones were permanently united'. The author ends the dossier at Cliopatria's row end and does not merge with principality-of-vladimir-suzdal (eu-16-g, the same Wikidata Q83546), against the brief's instruction for same-state rows, and says so. If merged: replace the dissolve with continuity under Mongol vassalage (mongol-empire /ledger/32 already has the suzerain side) and add a 1241-1293 keyframe as Smolensk did.
- Note (non-blocking): /ledger/10 vassal_end 1212 (Murom page) disagrees with the Ryazan page, which lists Roman II (1212-1217) as 'held captive in Vladimir, but released as their vasal'. Quote both in the note.
- Thin: /ledger/3 1126 gain, +75,700 km2 (Kostroma, Galich, Unzha, Sukhona), confidence 1, the largest move in the dossier. Pages to try: Kostroma, Galich (Kostroma Oblast), Vologda. /keyframe_review/5 (+5,200 km2 on the Volga above Nizhny Novgorod in 1227); page to try: Nizhny Novgorod. /ledger/0 found 1054, confidence 1.

## principality-of-ryazan: fix (applied by the reviewer)

- Applied: /ledger/3 contest_end 1240 (confidence 1, 'no page opened dates the end') -> 1238, confidence 2. Mongol invasion page: Ryazan fell after three days, 'the Tartars took the town on December 21' [1237]; 'Having burnt down Kolomna and Moscow, the horde laid siege to Vladimir on 4 February 1238'. Ryazan page: in 1238 Ryazan forces joined the Vladimir-Suzdal army against Batu near Kolomna. This matches the dossier's own war (1237-1238) and mongol-empire /ledger/27 (contest_end December 1237). Re-validated: 0 errors.
- Confirmed: /ledger/1 (1129 'fully split off from the Principality of Chernigov by 1129 as Murom-Ryazan'), /ledger/2 ('In December 1237, the duchy became the first...').
- Orchestrator decision (non-blocking): /ledger/4 dissolve 1240, confidence 1. The Ryazan page lists rulers through the period (Ingvar II 1237-1252, Oleg the Red 1252-1258, Roman III 1258-1270, Fyodor I 1270-1294, Yaroslav III 1294-1299, Konstantin 1299-1301) and the merger with Muscovy in 1521. Same question as Rostov-Suzdal: merge with ryazan (eu-16-g, Q269109).
- Thin: /ledger/0 found 1094, confidence 1 (Cliopatria's year; the pages give 1127 and 1129). Page to try: Yaroslav Sviatoslavich.

## principality-of-volhynia: fix (applied by the reviewer)

- Applied: /ledger/0 found 1054, confidence 1 -> 2. The Volhynia page's list of princes has 'Igor Yaroslavich (1054-1057)', then Rostislav of Tmutarakan (1057-1064). The note now quotes it. Re-validated: 0 errors, the one known warning.
- Confirmed: /ledger/1 (1069-1118 Izyaslavichi), /ledger/2 (Lutsk 1154-1228 separated, 'Principality of Volodymyr' 1154-1199), /ledger/3-4 (Roman page 'Roman captured Halych, but was soon expelled by Hungarian king Bela III', 1188), /ledger/5 (1199 union).
- Thin (by budget, 1-2 pages): the page names Brest, Lutsk, Dorogobuzh, Belz, Kremenets, Busk and Shumsk. Kremenets (50.10N), Busk (49.97N) and Shumsk (50.12N) lie south of the shape's southern edge (50.25N, shapes.csv bbox). A gap-filler should find in which years they were Volhynian. Pages to try: Kremenets, Belz. The 1154 Lutsk split (a 40 km disc) has no keyframe trace; it is small and inside one shape's span, so it is accepted.

## principality-of-terebovlia: thin (by budget)

- Confirmed: /ledger/0 (1084 'established as an appanage around the year 1084 and given to Vasylko Rostyslavych'), /ledger/2 (1124 death of Vasylko), /ledger/3 (1141 'by 1141 Terebovlia principality had become a part of the Principality of Galicia').
- /ledger/1 (1094 gain, confidence 1). The note says the pages say nothing of this land, but the Terebovlia page has 'Its territories included parts of southeastern Galicia, Bukovina, and western Podolia', which supports the extent of the 1094 shape (Chernivtsi and Kamianets-Podilskyi inside) though not the year. Quote it in the note; the year stays Cliopatria's.
- Non-blocking: /ledger/2 is a `rename` for a son succeeding his father; rename is for a change of name or dynasty. The same page sentence, 'After Vasylko Rostyslavych died in 1124, Halych principality seceded', implies a split that the ledger does not encode (thin). The predecessor `rus` follows the infobox ('Preceded by Kievan Rus''), but the rus dossier dissolves in 1054, 30 years before the found event that names it.

## Cross-dossier matrix: mismatches and routes

- grand-duchy-of-lithuania (eu-15, written) lacks mirrors for Smolensk's 1239-1240 contest, the 1356-1359 contest, the 1359 loss, the 1395 loss and the 1401 gain. Its /ledger/23 (1375 gain, counterpart 'unknown (page silent)') should name principality-of-smolensk. Its /ledger/2 and /ledger/5 (1250 gain and 1260 loss of Polotsk, confidence 1, Cliopatria bridges) disagree with the Polotsk dossier, which keeps Polotsk as a Lithuanian vassal from 1240 ('in 1240 Polotsk became a vassal of the Grand Duchy of Lithuania') to the 1307 annexation (matched at GDL /ledger/9). Route to eu-15: vassal_start 1240 and vassal_end 1307, counterpart principality-of-polotsky, in place of the 1250/1260 pair. The 1404 Smolensk gain is matched.
- livonian-brothers-of-the-sword (eu-14, written, ends 1237) has no vassalage of Polotsk; the Polotsk infobox gives 'Vassal of Livonian Brothers of the Sword (1227-1240)'. Route to eu-14.
- golden-horde (ia-02, written) has no tributary relation for Smolensk after 1294; the Smolensk city page says it 'paid tribute to the Golden Horde'. Route to ia-02.
- mongol-empire: Ryazan's contest (now 1237.12-1238) and Rostov-Suzdal's contest (1238.2-1238.3) are matched; its vassal_start of Ryazan (1237.12), Rostov-Suzdal (1238.3) and Smolensk (1241) is suzerain-side.
- rus: its 1054 dissolve lists Polotsk, Rostov-Suzdal, Smolensk and Volhynia as successors. Matched.
- principality-of-galicia-volhynia: its 1199 found lists Volhynia as predecessor. Matched with Volhynia's 1199 merge.
- Exceptions (counterpart group not run): principality-of-kiev (Polotsk 1067-1071 and 1127-1132, Rostov-Suzdal occupations of Kiev), principality-of-vitebsk, principality-of-minsk, principality-of-drutsk (1101 splits), principality-of-halych (Volhynia 1188, Terebovlia 1141), grand-principality-of-moscow (Smolensk 1304), principality-of-chernigov (Ryazan's predecessor). principality-of-lutsk and principality-of-murom need dossiers (eu-16-x).

## Problems for the orchestrator

- Same-state pairs not merged (rostov-suzdal with vladimir-suzdal, principality-of-ryazan with ryazan). Both earlier dossiers dissolve in 1240 against their pages; decide the merge before eu-16-g runs.
- Polotsk and Vitebsk claim the same land for 1111-1187 (Cliopatria's Vitebsk row is the whole Polotsk core); the colour agent and the principality-of-vitebsk author must choose.
- WebFetch returns a model summary. The 1168 end of Smolensk's first Vitebsk episode rests on the page's princes' list, which the summary did not reproduce (the text says 1165-1167).
