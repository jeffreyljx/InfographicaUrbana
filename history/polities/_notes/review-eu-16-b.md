# Review of batch eu-16-b (Rus and Russia to 1721, part b)

Reviewer: adversarial review, 2026-11-01 (brief filled 2026-10-31). Dossiers: novgorod-republic, principality-of-chernigov, principality-of-kiev, principality-of-peremyshl, principality-of-pereyaslavl. All five validate with 0 errors and 0 warnings (also with --resolve), before and after the reviewer's edit.

Pages opened by the reviewer (WebFetch, 2026-11-01): Novgorod Republic, Swedish-Novgorodian Wars (twice), Battle of Shelon, Battle on the Ice, Alexander Nevsky, Kievan Rus', Principality of Chernigov, Principality of Murom, Mongol invasion of Kievan Rus', Principality of Kiev, Principality of Peremyshl, Principality of Terebovlia, Principality of Pereyaslavl. Every spot-checked event was on its page with its year; none was fabricated or mis-dated. Landskrona: the text says Novgorod destroyed it 'later that year', but the page's table gives the Neva campaign as 1300-1301, which supports the dossier's 1301.

Reading of the rules: the schema defines vassal_start/vassal_end with the vassal as counterpart on the suzerain's side, so a vassal relation is not expected in the vassal's own ledger (reviewer brief section 2.3 says otherwise; the schema governs). The vassal events of mongol-empire and principality-of-galicia-volhynia over Kiev, Chernigov, Pereyaslavl and Novgorod therefore need no mirror here.

## Verdicts

| slug | verdict | why |
| --- | --- | --- |
| novgorod-republic | thin | spot checks all confirmed; one slug fix applied; the northern growth (1126, 1314, 1468) and the losses to Moscow (1344, 1463) are confidence 1; the Swedish occupation of Orekhov (1348-1349) and the 1337-1339 fighting are missing, though the opened pages have them and kingdom-of-sweden carries them |
| principality-of-chernigov | pass | 1024, 1036, 1054, 1127 and 1239 confirmed; every shape change explained; the end in 1240 and the landless years 1036-1053 go to the orchestrator |
| principality-of-kiev | thin | 1054, 1132, 1149-1157 and November-December 1240 confirmed; the largest move (1188, half the land) is confidence 1 against the Turov page's 1162; the mirrors of Polotsk 1129-1132 are missing; Kiev's hold over Novgorod 1054-1136 is not recorded; one overlap among the rulers |
| principality-of-peremyshl | pass | 1084 and 1141 confirmed; the infobox's 1,124 km2 is acknowledged as wrong; found 1056 is honestly confidence 1 |
| principality-of-pereyaslavl | pass | 1054 and March 1239 confirmed; the page is silent from 1054 to 1239 (budget of 1-2 pages) |

## novgorod-republic

Applied by the reviewer (re-validated, read back):
- /ledger/5, /ledger/7, /wars/0/belligerents: the counterpart "Bishopric of Ösel–Wiek" (a name) is now the slug `bishopric-of-osel-wiek`. That dossier has been on disk since 2026-10-31 20:20. The note of /ledger/5 now says so.

Not applied (for the author or a gap-filler):
- Missing occupation, 1348-1349. The Novgorod Republic page: "Magnus IV of Sweden captured the key fortress of Orekhov" in August 1348. The Swedish-Novgorodian Wars page: the army went "to Oreshek and set it ablaze", "Novgorod soon regained control" (table 1348-1351). kingdom-of-sweden /ledger/14-15 has occupation_start 1348-08 and occupation_end 1349-02 against novgorod-republic. Add occupation_start 1348 month 8 (counterpart kingdom-of-sweden, region the Orekhov fortress at the Neva source: {"place": "Shlisselburg", "km": 15}, text 'the key fortress of Orekhov', confidence 3, source Novgorod_Republic) and occupation_end 1349 (confidence 2; February comes from the Sweden dossier's page, not opened here).
- Missing contest, 1337-1339. The Swedish-Novgorodian Wars page: "In 1337, Karelians rebelled, and Magnus Eriksson's troops briefly occupied Korela Fortress"; "In 1338, Novgorod besieged Viborg, but an armistice was soon agreed." kingdom-of-sweden /ledger/12-13 has contest_start 1337 and contest_end 1339. Add contest_start 1337 and contest_end 1338 or 1339 against kingdom-of-sweden, zone Korela (Priozersk) and the Karelian Isthmus, confidence 2, with a war zone.
- /ledger/3 (1236 loss) and /ledger/10 (1294 gain) against karelians, both confidence 1. The cited Alexander Nevsky page says "the Karelians had been allies and tributaries of Novgorod since the mid-12th century". The karelians dossier has no matching 1236 gain or 1294 loss, and it draws different land (the Karelian Isthmus and South Karelia, not the Ladoga-Onega strip). Two fixes would work: mark novgorod-republic_1236 adjust and keep the strip (correction {"cliopatria": "Novgorod Republic", "year": 1220}, dropping /ledger/3 and /ledger/10); or name the counterpart nobody. Agree it with the karelians owner.

Thin (confidence 1, each with a page to try):
- /ledger/15, 1314 gain from nobody: +3,668 cells, about 930,000 km2, the largest move in the dossier, with no page. Try Zavolochye again (as 'Zavolochie'), Great Perm, Yugra, and the Pechora River history. The Novgorod page has a Pechora expedition in 1032 and Yugra trade by 1096, which could also date /ledger/1.
- /ledger/1, 1126 gain from nobody (+163,000 km2); /ledger/22, 1468 gain from nobody (Kola, +138,000 km2; try Kola Peninsula, history).
- /ledger/18, 1344 and /ledger/21, 1463 losses to Moscow (try Vologda, history; Grand Principality of Moscow). The Novgorod page has Moscow seizing northern land gradually after 1456, without dates.
- /ledger/8, 1285 split of Pskov: the Novgorod page says "Pskov won its formal independence in August 1348", "confirmed by the Treaty of Bolotovo". Either keep 1285 together with pskov-republic or move both to 1348.
- 1259: the Alexander Nevsky page says "In 1259, he led an army to the city of Novgorod and forced it to pay tribute ... to the Golden Horde". This belongs on the suzerain's side; mongol-empire carries a vassal_start at 1241 (confidence 1, from the overlap of the Cliopatria shapes) and should move it to 1259.

Area: the infobox has no area; the dossier says so. The largest Cliopatria shape is 1,599,366 km2 (1468).

## principality-of-chernigov

Confirmed on the pages: 1024 (Mstislav from Tmutarakan, the Dnieper boundary); 1036 ("Chernigov was incorporated into the realm of Kiev"); 1054 (Kievan Rus': "Principality of Chernigov and Tmutarakan, for Sviatoslav II"); 1127 (Murom: "In 1127, it became a separate principality"); 1239 (Mongol invasion: "In the winter of 1239, he sacked Chernigov and Pereyaslavl"). The keyframes are consistent: Murom-Ryazan is drawn for 1054-1126 and lost in 1127.

Thin: /ledger/6, dissolve in 1240 at confidence 1. The page runs the state to 1402: "vassal of the Golden Horde (1245-1362)", then Lithuania (1362-1402). Tmutarakan (Chernigov's from 1054, "eventually overtaken", undated) is not drawn; try the Tmutarakan page, or the separate tmutarakan dossier the author suggests.

For the orchestrator: the state lives 1024-1240 but has no land in 1036-1053, so its capitals are not contiguous. This mirrors rus 1024/1036 and is flagged. The end in 1240 conflicts with grand-duchy-of-lithuania's 1357 gain from principality-of-chernigov and with principality-of-galicia-volhynia's gains of 1238 and 1245.

## principality-of-kiev

Confirmed: 1054 found; 1132 rename ("Following the death of Mstislav I of Kiev in 1132, the semi-autonomous states were de facto independent"); Yuri Dolgorukiy 1149-1151 and 1155-1157 (from the page's list); November 1240 (approach) and December 1240 (storm).

Not applied:
- Missing mirrors of Polotsk. principality-of-polotsky /ledger/11 has a 1129 loss to Kiev and /ledger/12 a 1132 gain from Kiev (Principality of Vitebsk page: Mstislav "annexed Polotsk and its vassals including Vitebsk"), plus contests in 1067-1071 and 1127-1129. Kiev has none of them. Add gain 1129 / loss 1132 (counterpart principality-of-polotsky, source Principality_of_Vitebsk) and the contests, or agree with the polotsky owner that the counterpart is the grand prince and not this principality.
- Kiev's hold over Novgorod, 1054-1136, is not recorded. The Kievan Rus' page has "Principality of Kiev and Novgorod, for the eldest son Iziaslav I" (1054) and "In 1136, Novgorod revolted against Kiev, and became independent". Add vassal_start 1054 month 2 and vassal_end 1136 with counterpart novgorod-republic (region {"cliopatria": "Novgorod Republic", "year": 1056}, confidence 2), so that Novgorod is drawn in the tint until 1136.
- identity.rulers: 'Rurik Rostislavich 1180-1181' lies inside 'Sviatoslav Vsevolodovich 1177-1194' (co-rule). Drop it or move it into the note so the strip is contiguous.

Thin: /ledger/6, the 1188 loss to principality-of-turov-and-pinsk at confidence 1. It moves 69,000 km2 (147,400 to 78,100). The Turov page gives 1162 for "full independence from Kievan Rus'"; settle it with the turov-and-pinsk owner. The end in 1240 conflicts with grand-duchy-of-lithuania's 1321 gain from principality-of-kiev; the page runs the principality to 1471.

Area: no infobox area (moot). The largest Cliopatria shape is 147,669 km2.

## principality-of-peremyshl

Confirmed: 1141 merge ("In 1141, it was united with the Principality of Terebovlia and Principality of Zvenyhorod", forming "the enlarged Principality of Halych"); 1084 split ("established as an appanage around the year 1084 and given to Vasylko Rostyslavych", Terebovlia page); the 1097 siege. The found event of 1056 is honest at confidence 1: the page says "Established: 11th century", and the earliest known prince is Ryurik Rostislavich in 1087. Area: the infobox gives 1,124 km2 (no year) against 62,424 km2 (ratio 0.018). The dossier acknowledges this and keeps the shape; agreed.

Cross: principality-of-terebovlia's found event (1084) names rus as its counterpart, but rus ended in 1054; it should be principality-of-peremyshl. The rus dossier's successors omit Peremyshl.

## principality-of-pereyaslavl

Confirmed: 1054 (Vsevolod; the Kievan Rus' and Pereyaslavl pages); March 1239 ("Pereyaslavl was conquered and devastated by the Mongols in March 1239"). The infobox gives "Disestablished: 1239/1323" and no area. Thin by design: nothing is dated 1054-1239; dissolve 1240 at confidence 1.

## Cross-dossier matrix (unmatched and mismatched only; the full list is in the JSON report)

- Missing on Novgorod's side: kingdom-of-sweden 1337-1339 contest and 1348-1349 occupation.
- Missing on the counterpart's side: kingdom-of-sweden (eu-14), the 1300-1301 Landskrona occupation; teutonic-order (eu-14), the September 1240 to 1241 Pskov occupation (the page names bishop Hermann of Dorpat; bishopric-of-dorpat exists and is another candidate); bishopric-of-osel-wiek, the 1240-1241 Votia occupation; karelians, the 1236 gain and 1294 loss.
- Mismatch: karelians contest 1278-1323 against Novgorod's contest of 1314 only; principality-of-ryazan found 1094 (counterpart chernigov) against Chernigov's 1127 loss (the Murom page gives 1127); principality-of-terebovlia found 1084 (counterpart rus) against Peremyshl's 1084 split; grand-duchy-of-lithuania gains of 1321 (Kiev) and 1357 (Chernigov) after both end in 1240; principality-of-galicia-volhynia gains of 1238 and 1245 from Chernigov, which never drew Galicia; mongol-empire's 1241 vassal_start for Novgorod against the page's 1259; principality-of-polotsky 1067-1132 against Kiev (above).
- Exceptions: grand-principality-of-moscow (eu-16-f has not run): 1344, 1397, 1398, 1463, the 1471 contest and the 1478 merge; it should also carry a vassal_start for novgorod-republic in 1471 (Korostyn: "recognize itself as a patrimony of the grand prince").
