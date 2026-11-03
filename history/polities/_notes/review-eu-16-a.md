# Review of batch eu-16-a (2026-10-25)

Reviewer: adversarial pass, Phase B. Machine copy: history/notes/phase-b/reviews/eu-16-a.json.
All three dossiers validate with `--resolve`: 0 errors. The only warnings are the ten intended empty corrections of halych-volhynia-occupation. Neighbour dossiers read: khazaria, magyars, pechenegs, byzantine-empire, cuman-kipchak-confederation, kimek-kipchak-confederation, mongol-empire, old-great-bulgaria, golden-horde, duchy-of-sandomierz, duchy-of-silesia, empire-of-trebizond. The other Context polities (the eu-16 principalities, kingdom-of-poland, first-bulgarian-empire, kingdom-of-hungary and others) are not written yet; their groups have not run.

| slug | verdict | why |
| --- | --- | --- |
| rus | fix | Fixed by the reviewer: the 965 Sarkel gain (c3 to 2, radius 150 to 25 km), the 990 Tmutarakan gain (c1 to 2 on a page that dates it), Oleg's reign clipped to the dossier's start. 17 events checked on 4 pages, all confirmed. |
| volga-bulgaria | fail | Two missing events on pages the author opened: the Khazar vassalage (late 9th century to 969, mirror of khazaria.json) and the 1232 Mongol occupation of the south. Keyframe 3's note says the opposite of the page. |
| halych-volhynia-occupation | pass | The row is not Galicia-Volhynia. All four pages I opened bear out the author's reading. The type `umbrella` is for the orchestrator to settle. |

## rus (fix, applied by the reviewer)

Applied (re-validated, 0 errors, 0 warnings):
1. `/ledger/7` (965 gain of Sarkel from khazaria). The Sviatoslav I page has 'Sviatoslav destroyed the Khazar city of Sarkel around 965' and 'The exact chronology of his Khazar campaign is uncertain and disputed', so confidence 3 was too high; it is now 2. The region was a 150 km disc around Sarkel (70,600 km2). No Rus' keyframe touches it: its intersection with the 990 shape is 0 cells. 52,900 km2 of it lies in the pechenegs dossier's Rostov, Luhansk and Donetsk (889-1043), and no event ever loses it. The page names only 'a Rus' settlement called Belaya Vyezha', so the radius is now 25 km (the fortress). That is small, like Tartu (1030), and the ledger carries it.
2. `/ledger/15` (990 gain of Tmutarakan). The Vladimir the Great page lists, among his children, Mstislav of Chernigov, 'Prince of Tmutarakan' (990-1036). That dates Rus' rule there from 990, so the source now points to that page and confidence goes from 1 to 2. The Tmutarakan page's quotes stay in the note.
3. `/identity/rulers/0`. Oleg's 'from' was 879, before the dossier's start of 880. It is now clipped to 880, and the note says why.

Confirmed on the pages (Kievan Rus', Sviatoslav I of Kiev, Vladimir the Great, Yaroslav the Wise):
- ledger 1 and 2: 'captured Smolensk and later Kiev in 882'.
- ledger 4: 'In 883, he conquered the Drevlians'.
- ledger 5: 'By 885 he had subjugated the Poliane, Severiane, Vyatichi, and Radimichs'.
- ledger 8: 'In 969, he moved his seat to Pereyaslavets on the Danube'.
- ledger 9: the treaty of 971, 'agreed to abandon the Balkans'.
- ledger 10, 11, 12 and 13: 981 Cherven 'from the Duchy of Poland'; 983 Yatvingians; 984 Radimichs; 988 Chersonesus.
- ledger 17 and 20: 1024, and the Chernigov left bank 'ceded to Mstislav until his death in 1036'.
- ledger 18 and 19: 1030 Tartu and 1031 Cherven.
- ledger 21: death on 20 February 1054. The page also lists the sons' principalities.
- ledger 16 (1018, confidence 1) is honest: the Yaroslav page says nothing of the Cherven towns in 1018.

Area: the infobox gives 1,330,000 km2 for 1000. Cliopatria's kievan-rus_990 is 1,170,311 km2, a ratio of 0.88, and keyframe 11 acknowledges it.

End at 1054: this is a defensible decision and it is documented. One inconsistency is left for the orchestrator. Keyframe 15 limits the 1040 shape to 1040-1054, while the notes say 'the renderer should hold it through 1055'. The principalities start in 1056 in Cliopatria, so 1055 has no owner unless the eu-16 principality dossiers start in 1054.

Thin (for a gap-filler; within the 11-page budget, 10 pages used):
- ledger 6: the 896 and 900 southward growth (confidence 1). Keyframes 896, 900 and 922 are unverified.
- ledger 14: the return of Chersonesus in 989 (confidence 1).
- ledger 16: what Poland took in 1018 (confidence 1). The Bolesław I the Brave page should date the Cherven towns.
- The war of Sviatoslav's sons (972-980) is absent.

Cross-dossier:
- magyars /ledger/1 (884 loss to kievan-rus, confidence 1) has no mirror here. Its region is 58 cells, 48 of them in Zhytomyr and Rivne, which is the Drevlian land of this dossier's 883 gain. The Kievan Rus' page backs the rus side ('In 883, he conquered the Drevlians'). The magyars owner (eu-15) should take the Drevlian land out of the Magyars' 882 shape, or name the Drevlians, rather than this dossier adding a Magyar gain.
- byzantine-empire has no occupation of Chersonesus in 988-989 to mirror ledger 13 and 14. It also has a 1016 gain of a Sevastopol disc (80 km) from 'Crimea (defenders not named)', but Chersonesus is at Sevastopol and was Byzantine before. Both are for eu-05.
- khazaria /ledger/13 (965 loss, a 150 km disc) now disagrees with this dossier's 25 km on the land. The rest of the disc stays Khazar until the 969 dissolve, and is Pecheneg in that dossier anyway.
- Several dossiers name the counterpart `kievan-rus`, which is this dossier (`rus`): khazaria, magyars, and the author says the principality agents will too. Alias it.

## volga-bulgaria (fail)

1. `/ledger` (no event, late 9th century and 969): the Khazar vassalage is missing. The infobox has 'Vassals of the Khazars (late 9th century-969)'. khazaria.json /ledger/12 has a vassal_start of volga-bulgaria in 890 (confidence 1) and /ledger/14 a vassal_end in 969 (confidence 2). The author's note ('Khazar suzerainty to 969 is in khazaria.json') is not a mirror. Fix: add a vassal_start (890, confidence 1, or 'late 9th century' as the page puts it) and a vassal_end (969, confidence 2). Use counterpart khazaria, region {"cliopatria": "Volga Bulgaria", "year": 682} and source the Volga Bulgaria page.
2. `/ledger` (no event, 1232) and `/keyframe_review/3/note`: the Mongol invasion of Volga Bulgaria page, which the author opened, has 'In 1232 the Mongol cavalry subjugated the southeastern part of the Bashkiria and occupied southern portions of Volga Bulgaria'. Keyframe 3's note says 'the raids of 1229-1232 changed no border on the pages'. Fix: add an occupation_start in 1232 at confidence 2, counterpart mongol-empire, with a region for the south of the shape (the part of the 1227 shape south of the Kama, for example), and end it in the 1236-1241 contest or the 1241 dissolve. Correct keyframe 3's note.
3. Cross-dossier (not this dossier's fault): mongol-empire /ledger/25 has a gain of Volga Bulgaria in 1236 (confidence 2). This dossier has a contest from 1236 to 1241 and the dissolve in 1241. The Volga Bulgaria page ('In 1236, the Mongols returned and in five years had subjugated the whole country'; infobox 'Conquered by the Mongols: 1240s') backs this side. ia-02 should make 1236 a contest_start and move the gain to 1241.

Confirmed on the pages:
- ledger 1: the 1236 contest_start, both quotes.
- ledger 2: 1241 by the 'five years' arithmetic, honestly at confidence 2.
- ledger 3: 'Volga Bulgaria became a part of the Ulus Jochi, later known as the Golden Horde'; infobox 'Bulgar territories added to Mongol Empire'.
- Capitals: Bolghar 'Sometime in the late 9th century'; the move to Bilär is undated, as the notes say.

Area: the infobox has no area. Cliopatria's 682 shape is 44,239 km2, and keyframe 1 acknowledges the missing figure.

Thin:
- ledger 0: found in 674 (confidence 1; the infobox says 'late 9th century').
- A fuller extent than the Tatarstan core (the page has 'Commanding the Volga River in its middle course').
- The Rus' campaigns of 1088, 1164, 1172 and 1183.

## halych-volhynia-occupation (pass)

What I tried and could not break:
- On the Kingdom of Galicia-Volhynia page: 'The Principality of Galicia was formed in the years 1124-1144'; 'Galicia and Volhynia merged around 1198 or 1199'; Roman's campaigns 'in 1201-2 and 1203-4'; 'briefly controlled the Brodnici on the Black Sea' (with [citation needed] and no year); Halych and Volodymyr 'devastated by the Mongols' in 1240. The page holds no steppe land and gives no area.
- On the Principality of Halych page: 'the consolidation of Galician influence in the lower reaches of the Dniester, Prut, and Danube rivers' (undated); the unified principality of 1141; the 1084 division. There is nothing on Bârlad or the Black Sea.
- On the Cumania page: 'stretching from present-day Kazakhstan, southern Russia, Ukraine, to southern Moldavia'; White Cumania 'may have denoted eastern Wallachia', Black Cumania 'may have denoted Moldavia'; disestablished 1241.

So the 'wrong' verdict on all ten shapes stands.

For the orchestrator:
- The type is `umbrella`, but reviewer-brief 2.9 says an umbrella is never a dossier of its own. This is a leaf row the orchestrator assigned, and it carries no territory. Either keep it as a record of a mis-attributed row (no colour) or drop the slug; the sa-01-d review raised the same point for mahajanapadas.
- mongol-empire /ledger/48-50 (Dec 1240 contest_start, contest_end and vassal_start of halych-volhynia-occupation) duplicate its events for principality-of-galicia-volhynia (/ledger/45-47) and would tint the steppe as a Mongol vassal. That land is Cuman until 1241 in cuman-kipchak-confederation and mongol-empire /ledger/52. ia-02 should drop 48-50.
- The Wallachia and Moldavia part of the row (22.5-29 E, 1066-1205) is claimed by no dossier once the row is dropped. ia-01 should extend cuman-kipchak-confederation (the Cumania page's White and Black Cumania).
- The 1240 dissolve names the row's 1236 shape and mongol-empire. It transfers nothing while every keyframe is empty. If the compiler reads dissolve regions literally, it would hand the steppe to the Mongols one year before the Cuman dossier does.

## Problems
- No page failed to load. WebFetch was used 11 times on 8 pages. The Vladimir the Great page and the Mongol invasion of Volga Bulgaria page were each fetched twice, the second time for a targeted quote.
