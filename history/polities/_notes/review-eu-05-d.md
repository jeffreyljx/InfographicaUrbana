# Review of batch eu-05-d (Byzantium, part d)

Reviewer run of 2026-10-19. Dossiers: empire-of-trebizond, kingdom-of-thessalonica, latin-empire, negroponte, nicaean-empire, principality-of-achaea. Neighbour dossiers read: byzantine-empire, despotate-of-epirus, duchy-of-athens, domain-of-rhodes, mongol-empire, ilkhanate, golden-horde, timurid-empire (the other Context polities are not written yet).

All six validate with `--resolve` (0 errors, 0 warnings), before and after the reviewer edits. The reviewer applied small, page-verified edits in place (marked in each event note with `[Reviewer eu-05-d, 2026-10-19: ...]`); findings marked "not applied" are for the author. "Blocking" findings are why a dossier fails.

| dossier | verdict |
| --- | --- |
| empire-of-trebizond | fail |
| kingdom-of-thessalonica | thin |
| latin-empire | fix |
| negroponte | fix |
| nicaean-empire | fail |
| principality-of-achaea | fix |

## empire-of-trebizond: fail

Area: infobox None (None), Cliopatria 33147.3 km2, ratio None. The Empire of Trebizond page gives no area (checked); the 1333-1344 doubling (13,617 to 26,606 km2) is acknowledged in /keyframe_review/10 as an inland artefact.

Findings:

- `/ledger/7 and a missing 1214 loss` (not applied, BLOCKING). nicaean-empire /ledger/14 gains eastern Paphlagonia (polygon 32.6-34.8E) from Trebizond in late 1214, but this dossier has only the 1212 loss of 31-33.5E (confidence 1) and no 1214 loss. Evidence: Empire of Trebizond page: 'the territories west of Sinope were lost to Theodore I Laskaris by 1214'; nicaean-empire /ledger/13 (1212, Heraclea and Amastris, 31-32.6E) and /ledger/14 (1214, Kastamonu/Cide/Inebolu, 32.6-34.8E). Fix: Split the loss to match Nicaea: /ledger/7 1212 Heraclea Pontica and Amastris (polygon 31-32.6E, c1 or c2); add a 1214 loss of eastern Paphlagonia to nicaean-empire (32.6E to the west edge of the Sinope district, about 34.4E; c2, source Empire_of_Trebizond, 'lost to Theodore I Laskaris by 1214'); move /ledger/8 contest_end to 1214 to match nicaean-empire /ledger/15.
- `/keyframe_review/2/correction` (not applied, BLOCKING). The correction for the 1210 shape (in force 1210-1214, since the _1215 keyframe takes over from 1215) removes Sinope, which this ledger holds until 1 November 1214 (/ledger/9), and draws no Paphlagonia although /ledger/7 keeps it Trapezuntine until 1212. Evidence: Siege of Sinope page: 'the city surrendered on 1 November' 1214 and 'apart from a period of Trapezuntine recovery in 1254-1265, the city henceforth remained in Turkish hands'; the keyframe's own note: 'Right for 1210-1214 only if Sinope is kept'. Fix: Give the 1210 shape with Sinope for 1210-1214 (the minus-Sinope belongs only in the _1215 keyframe); either union the Paphlagonian polygon until the 1212 loss (a new keyframe empire-of-trebizond_1212 for 1212-1214) or move /ledger/7 to 1210 and say the shape is right.
- `/keyframe_review/3/correction` (not applied, non-blocking). The 60 km Sinope disc leaves the coast between the Sinope district and the Iris (Bafra, Samsun) Trapezuntine, against the keyframe's own text 'the frontier at the Thermodon/Iris'. Evidence: Keyframe text and note; Alexios I's 1204 gain (/ledger/0) includes Samsun. Fix: Extend the minus to the Iris mouth (about 36.6E) or say in the note why Samsun stays Trapezuntine.
- `/ledger/6` (not applied, non-blocking). Contest start 1208 against nicaean-empire /ledger/5 1206. Evidence: This dossier: Laskaris 'invested Heraclea Pontica' (1208); Nicaea: 'Theodore decided to capture Heraclea Pontica from David' (1206-07). Fix: Agree one year with nicaean-empire.
- `/ledger/24, /ledger/25, /ledger/30` (applied by the reviewer). Counterparts were sultanate-of-rum (1297, 1302) and ottoman-empire (1346) for Oinaion. Evidence: Oinaion page: 'Empire of Trebizond in 1204-1214, 1228-1230, 1243-1297 and 1302-1346' and 'Emirate of Hacıemiroğlu between 1297-1302 and 1346-1461'; the page never names the Ottomans. Fix: Counterpart set to 'Emirate of Hacıemiroğlu' (suggested slug haciemiroglu); note extended.
- `/ledger/36` (applied by the reviewer). Counterpart was ottoman-empire for the loss of Limnia (1384-86). Evidence: Limnia (Pontus) page: Limnia 'became a Turkoman possession', Tajeddin Çelebi Emir of Limnia in 1386; no Ottomans. Fix: Counterpart set to 'Emirate of Limnia'; note extended.
- `/ledger/9/note` (not applied, non-blocking). The quote 'back toward the Iris and Thermodon rivers' is not on the cited Siege of Sinope page. Evidence: Siege of Sinope page has the 1 November surrender and the 1254-1265 exception only. Fix: Cite the page the quote comes from (Alexios I of Trebizond?) or drop it; the event itself is confirmed.
- `/ledger/29, /ledger/34` (not applied, non-blocking). The civil-war contest names the state itself (empire-of-trebizond) as counterpart. Evidence: A contest needs another party to be drawn as a blend. Fix: Name the rival party as the page gives it, or drop the contest pair if no ground changed hands.

Spot checks:

- `/ledger/9` https://en.wikipedia.org/wiki/Siege_of_Sinope: confirmed. 1 November 1214; the Iris/Thermodon quote is not on this page
- `/ledger/18` https://en.wikipedia.org/wiki/Manuel_I_of_Trebizond: confirmed. 'On 24 June 1254, Manuel recaptured Sinope'
- `/ledger/19` https://en.wikipedia.org/wiki/Empire_of_Trebizond: confirmed. infobox 'Permanent loss of Sinope: 1265'
- `/ledger/37` https://en.wikipedia.org/wiki/Siege_of_Trebizond_(1461): confirmed. 15 August 1461
- `/ledger/30` https://en.wikipedia.org/wiki/Oinaion: confirmed. year confirmed; counterpart was wrong (Ottomans not on the page), fixed by the reviewer
- `/ledger/36` https://en.wikipedia.org/wiki/Limnia_(Pontus): confirmed. 1384-86 confirmed; counterpart was wrong (Turkoman, not Ottoman), fixed by the reviewer
- `/ledger/14, /ledger/15, /ledger/17, /ledger/24, /ledger/25` https://en.wikipedia.org/wiki/Oinaion: confirmed. 1228-1230, 1243, 1297-1302 on the page

Thin (for a gap-filler):

- `/ledger/1`: year of David Komnenos' Paphlagonian conquests (bridged to 1204) (try https://en.wikipedia.org/wiki/David_Komnenos)
- `/ledger/16`: 1230 loss of Adjara/Imereti to Georgia (c1) (try https://en.wikipedia.org/wiki/Andronikos_I_of_Trebizond)
- `/ledger/20, /ledger/22`: 1282-83 Georgian occupation extent (c1) (try https://en.wikipedia.org/wiki/John_II_of_Trebizond)
- `/ledger/23`: Chalybia loss year (midpoint 1285, c1) (try https://en.wikipedia.org/wiki/John_II_of_Trebizond)
- `/ledger/35`: 1355 loss, no town named (c1) (try https://en.wikipedia.org/wiki/Alexios_III_of_Trebizond)
- `/ledger/2, /ledger/28`: Perateia tributary 1204-1333 (c1) (try https://en.wikipedia.org/wiki/Perateia)

## kingdom-of-thessalonica: thin

Area: infobox None (None), Cliopatria 33016.9 km2, ratio None. Kingdom of Thessalonica infobox has no area (checked).

Findings:

- `/ledger (Serres 1205-1221)` (not applied, non-blocking). Serres is in this kingdom's shapes 1206-1220 and lost to Epirus in late 1221, but latin-empire /ledger/6 loses a 40 km Seres disc to Bulgaria in April 1205 and never regains it. Evidence: latin-empire /ledger/11 note: 'Serres passed to the Kingdom of Thessalonica's sphere'; no event moves it. Fix: With latin-empire, settle who held Serres 1205-1221: either latin-empire drops the Seres disc from /ledger/6, or this dossier adds the 1205 loss to second-bulgarian-empire and the recovery.

Spot checks:

- `/ledger/11` https://en.wikipedia.org/wiki/Medieval_Thessaly: confirmed. 'In 1212 ... Larissa and much of central Thessaly came under Epirote rule'
- `/ledger/13` https://en.wikipedia.org/wiki/Theodore_Komnenos_Doukas: confirmed. 'the surrender of the great Platamon Castle in 1218'
- `/ledger/14` https://en.wikipedia.org/wiki/Theodore_Komnenos_Doukas: confirmed. 'the surrender of Serres in late 1221'
- `/ledger/15` https://en.wikipedia.org/wiki/Medieval_Thessaly: confirmed. 'by c. 1222/3 completed the recovery of the entire region except for Halmyros'
- `/ledger/17` https://en.wikipedia.org/wiki/Theodore_Komnenos_Doukas: confirmed. 'surrendered the city to Theodore sometime in December 1224'
- `/ledger/6-9` https://en.wikipedia.org/wiki/Kingdom_of_Thessalonica: confirmed. Henry's expedition 'in 1208-09' 'ended the feudal dependency' of Athens, Bodonitsa, Salona and Negroponte

Thin (for a gap-filler):

- `/keyframe_review/3`: date of the loss of the 12 western-Macedonian cells (Pieria, Elimeia) that leave between the 1210 and 1216 shapes (try https://en.wikipedia.org/wiki/Kingdom_of_Thessalonica)
- `/keyframe_review/5`: date of the Pieria and Pelion-coast loss between the 1216 and 1220 shapes, beyond Platamon (1218) (try https://en.wikipedia.org/wiki/Medieval_Thessaly)
- `/ledger (1205)`: Kaloyan's capture of Serres in 1205 and its recovery (try https://en.wikipedia.org/wiki/Kaloyan_of_Bulgaria)
- `/keyframe_review/7`: whether the eastern lobe to 25.5E (Kavala) was royal or imperial land (try https://en.wikipedia.org/wiki/Demetrius_of_Montferrat)

## latin-empire: fix

Area: infobox 206000 (1209), Cliopatria 59891.5 km2, ratio 0.29. Infobox: 179,000 (1204), 206,000 (1209), 47,000 (1228), 14,000 (1260). The 1209 figure counts the vassal states (keyframe 2 note, against the 1210 shape 89,156); 1228 against the 1227 shape 55,305 is 1.18; 1260 against the 1250 shape 2,997 is 0.21, and the dossier's corrected 1236-1261 shape (45 km disc plus Tzurulum) is about 6,000-9,000 km2, called 'generous' for the infobox in keyframe 6.

Findings:

- `/ledger/1` (applied by the reviewer). Confidence 3 with a month (October) and an 'agreement of 16 May 1204' that the cited page does not contain. Evidence: Kingdom of Thessalonica page: 'Kingdom established: 1204' and 'established as a vassal of the Latin Empire'; no month, no 16 May; the Latin Empire page has the partition of 1 October 1204. Fix: Confidence 3 to 2; note rewritten with the page's words, October marked as a reading of the 1 October 1204 partition.
- `/ledger/24/note` (applied by the reviewer). The quote 'Robert was forced to cede all his Asian possessions to Nicaea, except for Nicomedia' and the islands clause are not on the Battle of Poimanenon page. Evidence: Page: 'the Latins abandoned all their Asian possessions except for the eastern shore of the Bosporus' and kept 'the city of Nicomedia with the surrounding region'; no islands. Fix: Note rewritten with the page's words; the event (1225, c3) is confirmed.
- `/ledger/28/note` (applied by the reviewer). Event had no note. Evidence: Latin Empire page: 'Epirote armies then conquered Thrace in 1225-26, appearing before Constantinople itself.' Fix: Note added with that quote.
- `/identity/family` (applied by the reviewer). Family 'latin' is not a key of colours.json families. Evidence: colours.json families: africa ... france ... italy ... rome ...; duchy-of-athens (passed in eu-05-c) uses france. Fix: Set to 'france' (Flemish-French crusader empire).
- `/ledger (Thebes 1209-1211)` (not applied, non-blocking). No Thebes event: duchy-of-athens /ledger/1 gains Thebes from latin-empire c.1211 with no mirror here. Evidence: Otto de la Roche page (via duchy-of-athens /ledger/1): Henry took Thebes from Albertino of Canossa on 8 May 1209; 'it is unclear whether Henry then gave Thebes to Othon in 1209 or ... before 1211'. Fix: Add a 1211 loss of Thebes (25 km) to duchy-of-athens, c2, source Otto_de_la_Roche (with the 1209 gain if the empire is to hold it 1209-1211), or agree with duchy-of-athens on another counterpart. Non-blocking: Thebes is in the duchy's shape from 1206.
- `/ledger/6/region` (not applied, non-blocking). The 1205 loss to Bulgaria includes a 40 km Seres disc that kingdom-of-thessalonica holds until 1221. Evidence: See the kingdom-of-thessalonica finding; /ledger/11 note says Serres passed to the kingdom's sphere. Fix: Drop the Seres disc or have both dossiers carry the 1205 loss and the recovery.
- `/ledger/14` (not applied, non-blocking). Ravennika homage of Othon de la Roche (May 1209, c2) is disputed. Evidence: eu-05-c review: the Otto de la Roche page says Othon 'never recognised Henry as his direct overlord' (Longnon). Fix: Name the disagreement in the note (not re-opened by this reviewer).
- `/identity/rulers` (not applied, non-blocking). Gap 1219-1221 between Yolanda (to 1219) and Robert (from 1221). Evidence: Rulers should be contiguous inside the life. Fix: Add the regency (Conon of Béthune, then Giovanni Colonna) or note the interregnum.
- `/keyframe_review/8/correction` (not applied, non-blocking). For a shape after the end of the state the correction is a 5 km Istanbul disc with the text 'nothing ... delete this keyframe', which a renderer could draw. Evidence: The empire ends 25 July 1261; the shape runs 1272-1278. Fix: Keep verdict wrong and give the years it belongs to (none: outside the life) in text; avoid a drawable region.

Spot checks:

- `/ledger/1` https://en.wikipedia.org/wiki/Kingdom_of_Thessalonica: mis-dated. year and vassalage on the page; the month and the 16 May agreement are not; lowered to c2 by the reviewer
- `/ledger/24` https://en.wikipedia.org/wiki/Battle_of_Poimanenon: confirmed. 1225 peace; quote paraphrased, fixed
- `/ledger/28` https://en.wikipedia.org/wiki/Latin_Empire: confirmed. 'Epirote armies then conquered Thrace in 1225-26'
- `/ledger/32` https://en.wikipedia.org/wiki/Siege_of_Constantinople_(1235): confirmed. 'In the spring of 1235 ... took over Gallipoli', Thrace 'up to the mouth of the Marica', 'the fortress of Tzurulum'
- `/ledger/33` https://en.wikipedia.org/wiki/Latin_Empire: confirmed. 'In 1235, finally, the last Latin possessions fell to Nicaea.'
- `/ledger/38` https://en.wikipedia.org/wiki/Latin_Empire: confirmed. 'By 1247, the Nicaeans had effectively surrounded the main holdings' (c1)

Thin (for a gap-filler):

- `/ledger/7, /ledger/20`: Trebizond (David Komnenos) vassalage 1206-1212 (c1) (try https://en.wikipedia.org/wiki/David_Komnenos)
- `/ledger/12, /ledger/30, /ledger/31`: Alexius Slav's Melnik lordship 1209-1230 and the 1230 loss (c1) (try https://en.wikipedia.org/wiki/Alexius_Slav)
- `/ledger/38`: Tzurulum 1247 (c1; the 1235 siege page has Latin knights retaking Tzurulum c.1239) (try https://en.wikipedia.org/wiki/Siege_of_Constantinople_(1235))

## negroponte: fix

Area: infobox 3660 (None), Cliopatria 2178.3 km2, ratio 0.6. Infobox area has no year; keyframe 1 notes the missing Karystos end.

Findings:

- `/ledger/4 and /wars/2/from` (applied by the reviewer). Licario contest start 1276 (c1) taken from another dossier; the cited page has 1278. Evidence: Triarchy of Negroponte page: its table lists the Nicaean occupation as '1278-1285/96' with Licario as vice-governor; prose 'after 1280' and 'By 1296'. Fix: Year 1276 to 1278, confidence 1 to 2, note rewritten; war 2 from 1278.
- `/ledger/4-5` (not applied, non-blocking). The Licario years are drawn as a contest; the page's table calls them an occupation. Evidence: Triarchy page table: 'Nicaean occupation 1278-1285/96'. Fix: Consider occupation_start/occupation_end by byzantine-empire (the owner records it with roles reversed), once byzantine-empire carries the event.

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Triarchy_of_Negroponte: confirmed. infobox 'Principality established: 1204'
- `/ledger/1` https://en.wikipedia.org/wiki/Triarchy_of_Negroponte: confirmed. 'After his death in mid-1205 however, the island was ceded to three' barons
- `/ledger/6` https://en.wikipedia.org/wiki/Triarchy_of_Negroponte: confirmed. 'In 1317 however, Karystos fell to the Catalan Company'; 1319 treaty
- `/ledger/7` https://en.wikipedia.org/wiki/Triarchy_of_Negroponte: confirmed. 'which the Venetians acquired in 1365'
- `/ledger/8` https://en.wikipedia.org/wiki/Triarchy_of_Negroponte: confirmed. triarchs 'died in 1383 and 1390 respectively'; colony 1390-1470
- `/ledger/9` https://en.wikipedia.org/wiki/Triarchy_of_Negroponte: confirmed. 'With the fall of the city on 12 July' (1470)
- `/ledger/4` https://en.wikipedia.org/wiki/Triarchy_of_Negroponte: mis-dated. 1276 not on the page; table has 1278; fixed (c1 event)

Thin (for a gap-filler):

- `/ledger/2`: date of William's capture of Chalkis (1256-58; page: 'William then captured Chalkis', retaken by Venice early 1258) (try https://en.wikipedia.org/wiki/War_of_the_Euboeote_Succession)
- `/ledger/8`: which triarchy passed to Venice in 1383 (try https://en.wikipedia.org/wiki/Triarchy_of_Negroponte)
- `/keyframe_review/2`: 1216 six-sestieri settlement not drawn (try https://en.wikipedia.org/wiki/Ravano_dalle_Carceri)

## nicaean-empire: fail

Area: infobox None (None), Cliopatria 235926.9 km2, ratio None. Empire of Nicaea infobox has no area (checked).

Findings:

- `/keyframe_review/2/correction and /ledger/14/region` (not applied, BLOCKING). The correction of the 1210 shape is in force 1210-1224 but describes 1214-1224 (its text: 'for 1214-1224'): it draws David Komnenos' Paphlagonian coast as Nicaean from 1210, two to four years before /ledger/13 (1212) and /ledger/14 (1214); and /ledger/14's polygon (32.6-34.8E) reaches beyond every keyframe's Paphlagonian polygon (31-33.5E) and into the Sinope district, Seljuk from 1 November 1214. Evidence: Keyframe 2 note: 'The 1210-1214 years also want the Latin Mysian lobe removed and Paphlagonia excluded'; Siege of Sinope page (1 November 1214); empire-of-trebizond /ledger/7 (1212, 31-33.5E) and /keyframe_review/2. Fix: Add a keyframe nicaean-empire_1214 (1214-1224) with the present correction, and give _1210 (1210-1213) the 1210 shape without the Paphlagonian polygon (with 31-32.6E from 1212 if wanted); make /ledger/14's polygon and the 1214/1225/1235 keyframe polygons agree (east edge at the Sinope district, about 34.4E); do it together with the empire-of-trebizond Paphlagonia fix.
- `/ledger/25` (applied by the reviewer). Rhodes vassalage at confidence 2 on a surmise. Evidence: Leo Gabalas page: 'It has been surmised that at some point Leo acknowledged the suzerainty of the Empire of Nicaea'; the expedition 'in 1232/3'. Fix: Confidence 2 to 1; note extended.
- `/ledger/19` (applied by the reviewer). Aegean islands named and dated 1224-25 at confidence 2; the cited page names none and gives no year. Evidence: Latin Empire page: 'Nicaea turned also to the Aegean, capturing the islands awarded to the empire.' Fix: Confidence 2 to 1; note extended.
- `/ledger/34/note` (applied by the reviewer). The note quoted 'attacked Bulgaria and recovered most of Thrace and Macedonia' after Koloman I's death; the Vatatzes page has no such sentence and names no towns. Evidence: Vatatzes page: John III imposed suzerainty over Thessalonica in 1242 'and later to annex this city, as well as much of Bulgarian Thrace in 1246'. Fix: Note rewritten with the page's words; the Macedonian towns of the polygon are listed under thin.
- `/ledger/22/note` (applied by the reviewer). Adrianople lost to Epirus in 1227 here, 1225 in despotate-of-epirus /ledger/11. Evidence: Vatatzes page: 'drove the Nicaean garrison out of Adrianople and annexed much of Thrace in 1227'; Theodore Komnenos Doukas page: the capture then 'In the same summer of 1225, Theodore led his army to the environs of Constantinople'. Fix: Disagreement named in the note (reviewer); the year is left to the author and the Epirus dossier.
- `/ledger/5` (not applied, non-blocking). Contest start 1206 against empire-of-trebizond /ledger/6 1208. Evidence: See the empire-of-trebizond finding. Fix: Agree one year.
- `/wars (Pelagonia)` (not applied, non-blocking). principality-of-achaea /ledger/15-16 carries a 1259 Pelagonia contest with Nicaea; this dossier has none. Evidence: Battle of Pelagonia: Achaea fought in the Epirote coalition. Fix: Add the pair (zone at Pelagonia) or agree with achaea to drop it, since no Achaean land was contested.

Spot checks:

- `/ledger/18` https://en.wikipedia.org/wiki/Battle_of_Poimanenon: confirmed. 1225 peace, Asia except Nicomedia and the Bosporus shore
- `/ledger/20` https://en.wikipedia.org/wiki/Empire_of_Thessalonica: confirmed. 'the Nicaeans seized Adrianople from the Latins in 1225'
- `/ledger/22` https://en.wikipedia.org/wiki/John_III_Doukas_Vatatzes: confirmed. 1227 on the page; Theodore page and Epirus page say 1225
- `/ledger/25` https://en.wikipedia.org/wiki/Leo_Gabalas: not on page. suzerainty only surmised, undated; lowered to c1
- `/ledger/19` https://en.wikipedia.org/wiki/Latin_Empire: not on page. no islands or year named; lowered to c1
- `/ledger/33` https://en.wikipedia.org/wiki/Empire_of_Thessalonica: confirmed. 'Thessalonica was incorporated into the Nicaean state' (1246)
- `/ledger/34` https://en.wikipedia.org/wiki/John_III_Doukas_Vatatzes: confirmed. 1246 and Bulgarian Thrace on the page; the quoted sentence was not; note fixed

Thin (for a gap-filler):

- `/ledger/34`: page naming the Macedonian towns taken from Bulgaria in 1246 (Serres, Melnik, Skopje, Veles, Prosek, Pelagonia) (try https://en.wikipedia.org/wiki/Second_Bulgarian_Empire)
- `/ledger/30`: 1237 loss to Bulgaria (c1; the 1235 siege page reports no Bulgarian gain, only Latin knights taking Tzurulum c.1239) (try https://en.wikipedia.org/wiki/Ivan_Asen_II)
- `/ledger/19`: which islands Nicaea took and when (c1) (try https://en.wikipedia.org/wiki/Battle_of_Poimanenon)
- `/ledger/25`: Rhodes suzerainty 1233 (c1) (try https://en.wikipedia.org/wiki/Leo_Gabalas)

## principality-of-achaea: fix

Area: infobox None (None), Cliopatria 19839.7 km2, ratio None. Principality of Achaea infobox has no area (checked); capitals Andravida 1205-1249, Mystras 1249-1261 on the page.

Findings:

- `/identity/family` (applied by the reviewer). Family 'latin' is not a key of colours.json families. Evidence: colours.json families; duchy-of-athens uses france. Fix: Set to 'france' (Champenois Villehardouin).
- `/ledger/6 and /ledger/33` (applied by the reviewer). Argolid vassalage paired under counterpart duchy-of-athens, which ends in 1311, though the vassal_end is 1388. Evidence: Lordship of Argos and Nauplia page: granted 'as a fief to Otto de la Roche ... by Geoffrey I of Villehardouin'; it 'remained in the possession of the de la Roche and the Brienne dukes of Athens' after 1311, passed to Guy of Enghien in 1356, sold to Venice 'on 12 December' 1388. Fix: Counterpart of both set to 'Lordship of Argos and Nauplia' (pairing kept); notes extended.
- `/ledger/31` (applied by the reviewer). 1371 Corinth loss named duchy-of-athens (ends 1311). Evidence: Nerio I Acciaioli page: Angelo 'soon mortgaged it to Nerio, who established himself in the town'; Philip of Taranto 'confirmed Angelo's hereditary right to Corinth in 1371'; November 1372 'lord of the town of Corinth'. Fix: Counterpart set to 'Nerio I Acciaioli'; note extended.
- `/ledger/41` (applied by the reviewer). Capital move to Chalandritsa in 1418 at confidence 2; the cited page does not name Chalandritsa as his seat then. Evidence: Centurione II Zaccaria page: he fled Glarentza by sea in spring 1418; Chalandritsa appears only in the 1429 siege. Fix: Confidence 2 to 1; note extended.
- `/ledger/12` (not applied, non-blocking). Contest start 1256 against duchy-of-athens /ledger/2 1258. Evidence: War of the Euboeote Succession page (this dossier) against the duchy's 1258 invasion; both cite pages. Fix: Agree one year with duchy-of-athens.
- `/ledger/30/note` (not applied, non-blocking). The clause on Akova falling 'along with the castles of Karytaina' is not on the Barony of Karytaina page. Evidence: Page: 'In 1320, Karytaina and the eastern half of the ancient barony fell into the hands of the Byzantines under Andronikos Asen.' Fix: Cite the page that names Akova or drop the clause; the event is confirmed.
- `/ledger/15-16` (not applied, non-blocking). Pelagonia contest with nicaean-empire has no mirror and its zone is outside Achaea. Evidence: nicaean-empire has no contest with principality-of-achaea. Fix: Drop the pair (no Achaean land contested) or have nicaean-empire add it.

Spot checks:

- `/ledger/2` https://en.wikipedia.org/wiki/Treaty_of_Sapienza: confirmed. 'concluded in June 1209'; 'Venice kept only the two forts of Modon and Coron'
- `/ledger/18` https://en.wikipedia.org/wiki/Mystras: confirmed. 'the cession of Monemvasia, Grand Magne, and Mystras'; 'The handover was effected in 1262'
- `/ledger/30` https://en.wikipedia.org/wiki/Barony_of_Karytaina: confirmed. 1320; Akova clause not on the page
- `/ledger/33` https://en.wikipedia.org/wiki/Lordship_of_Argos_and_Nauplia: confirmed. sold to Venice 12 December 1388
- `/ledger/35, /ledger/36` https://en.wikipedia.org/wiki/Centurione_II_Zaccaria: confirmed. Glarentza 1408 to the Toccos, retaken 1414
- `/ledger/42, /ledger/47` https://en.wikipedia.org/wiki/Centurione_II_Zaccaria: confirmed. Chalandritsa besieged 1429, barony of Arcadia kept; died 1432, domains to the despotate

Thin (for a gap-filler):

- `/keyframe_review/11-12`: Theodore I Palaiologos' gains of the 1390s (1385 to 1395 shape: 14,143 to 13,724 km2) undated (try https://en.wikipedia.org/wiki/Theodore_I_Palaiologos)
- `/ledger/25`: 1278 vassal_end of Negroponte (c1, bookkeeping) (try https://en.wikipedia.org/wiki/Triarchy_of_Negroponte)
- `/keyframe_review/8`: Skorta revolts of the 1290s (try https://en.wikipedia.org/wiki/Skorta)

## Cross-dossier matrix: rows that need action

- empire-of-trebizond /ledger/6 1208 contest_start (counterpart nicaean-empire) -> mismatch against nicaean-empire /ledger/5 1206 contest_start. Contest start 1208 (Laskaris invests Heraclea) against nicaean-empire /ledger/5 1206 (Theodore decides to take Heraclea, 1206-07); agree a year (non-blocking).
- empire-of-trebizond /ledger/8 1212 contest_end (counterpart nicaean-empire) -> mismatch against nicaean-empire /ledger/15 1214 contest_end. Contest end 1212 (c1) against nicaean-empire /ledger/15 1214; the Empire of Trebizond page: 'the territories west of Sinope were lost to Theodore I Laskaris by 1214'. Move to 1214 (part of the Paphlagonia fix).
- kingdom-of-thessalonica /ledger/10 1212 contest_start (counterpart despotate-of-epirus) -> missing. despotate-of-epirus (eu-05-c, failed) carries no contest events with this state; route the mirror to it.
- kingdom-of-thessalonica /ledger/12 1218 contest_start (counterpart despotate-of-epirus) -> missing. despotate-of-epirus (eu-05-c, failed) carries no contest events with this state; route the mirror to it.
- kingdom-of-thessalonica /ledger/16 1222 contest_end (counterpart despotate-of-epirus) -> missing. despotate-of-epirus (eu-05-c, failed) carries no contest events with this state; route the mirror to it.
- kingdom-of-thessalonica /ledger/18 1224 contest_end (counterpart despotate-of-epirus) -> missing. despotate-of-epirus (eu-05-c, failed) carries no contest events with this state; route the mirror to it.
- latin-empire /ledger/27 1225 contest_start (counterpart despotate-of-epirus) -> missing. despotate-of-epirus (eu-05-c, failed) carries no contest events with this state; route the mirror to it.
- latin-empire /ledger/29 1228 contest_end (counterpart despotate-of-epirus) -> missing. despotate-of-epirus (eu-05-c, failed) carries no contest events with this state; route the mirror to it.
- negroponte /ledger/4 1278 contest_start (counterpart byzantine-empire) -> missing. byzantine-empire (eu-05-b, failed) carries no contest events with this state; route the mirror to it.
- negroponte /ledger/5 1296 contest_end (counterpart byzantine-empire) -> missing. byzantine-empire (eu-05-b, failed) carries no contest events with this state; route the mirror to it.
- nicaean-empire /ledger/5 1206 contest_start (counterpart empire-of-trebizond) -> mismatch against empire-of-trebizond /ledger/6 1208 contest_start. See empire-of-trebizond /ledger/6 (1208).
- nicaean-empire /ledger/14 1214 gain (counterpart empire-of-trebizond) -> mismatch against empire-of-trebizond /ledger/7 1212 loss. Late-1214 gain of eastern Paphlagonia (32.6-34.8E) from Trebizond: Trebizond has only the 1212 loss of 31-33.5E (its /ledger/7, c1) and no 1214 loss; the polygon also overlaps the Sinope district (Rum from 1 November 1214). Blocking for empire-of-trebizond: add the 1214 loss; nicaean-empire should clip the polygon at the Sinope district.
- nicaean-empire /ledger/15 1214 contest_end (counterpart empire-of-trebizond) -> mismatch against empire-of-trebizond /ledger/8 1212 contest_end. See empire-of-trebizond /ledger/8 (1212).
- nicaean-empire /ledger/22 1227 loss (counterpart despotate-of-epirus) -> mismatch against despotate-of-epirus /ledger/11 1225 gain. Adrianople: despotate-of-epirus /ledger/11 has 1225 (Despotate of Epirus page; the Theodore Komnenos Doukas page also has summer 1225); this dossier has 1227 from the Vatatzes page. Both cite pages; the note now names the disagreement (reviewer). Non-blocking.
- nicaean-empire /ledger/23 1232 contest_start (counterpart domain-of-rhodes) -> missing. domain-of-rhodes (eu-05-c) has no contest with Nicaea; route the mirror to it (non-blocking).
- nicaean-empire /ledger/24 1233 contest_end (counterpart domain-of-rhodes) -> missing. domain-of-rhodes (eu-05-c) has no contest with Nicaea; route the mirror to it (non-blocking).
- nicaean-empire /ledger/40 1251 contest_start (counterpart despotate-of-epirus) -> missing. despotate-of-epirus (eu-05-c, failed) carries no contest events with this state; route the mirror to it.
- nicaean-empire /ledger/42 1252 contest_end (counterpart despotate-of-epirus) -> missing. despotate-of-epirus (eu-05-c, failed) carries no contest events with this state; route the mirror to it.
- nicaean-empire /ledger/49 1257 contest_start (counterpart despotate-of-epirus) -> missing. despotate-of-epirus (eu-05-c, failed) carries no contest events with this state; route the mirror to it.
- nicaean-empire /ledger/55 1260 contest_end (counterpart despotate-of-epirus) -> missing. despotate-of-epirus (eu-05-c, failed) carries no contest events with this state; route the mirror to it.
- principality-of-achaea /ledger/12 1256 contest_start (counterpart duchy-of-athens) -> mismatch against duchy-of-athens /ledger/2 1258 contest_start. 1256 (Guy joins the Lombard-Venetian camp, War of the Euboeote Succession page) against duchy-of-athens /ledger/2 1258 (the invasion). Both cite pages; agree one year (non-blocking).
- principality-of-achaea /ledger/15 1259 contest_start (counterpart nicaean-empire) -> missing. Pelagonia 1259: nicaean-empire has no contest with principality-of-achaea (its Pelagonia war names only Epirus). The zone is in Macedonia, not Achaean land; either nicaean-empire adds the pair or this pair is dropped (no ground of Achaea changed hands).
- principality-of-achaea /ledger/16 1259 contest_end (counterpart nicaean-empire) -> missing. See /ledger/15.
- principality-of-achaea /ledger/21 1263 contest_start (counterpart byzantine-empire) -> missing. byzantine-empire (eu-05-b, failed) carries no contest events with this state; route the mirror to it.
- principality-of-achaea /ledger/23 1264 contest_end (counterpart byzantine-empire) -> missing. byzantine-empire (eu-05-b, failed) carries no contest events with this state; route the mirror to it.
- principality-of-achaea /ledger/37 1417 contest_start (counterpart byzantine-empire) -> missing. byzantine-empire (eu-05-b, failed) carries no contest events with this state; route the mirror to it.
- principality-of-achaea /ledger/40 1418 contest_end (counterpart byzantine-empire) -> missing. byzantine-empire (eu-05-b, failed) carries no contest events with this state; route the mirror to it.
- principality-of-achaea /ledger/44 1429 contest_start (counterpart byzantine-empire) -> missing. byzantine-empire (eu-05-b, failed) carries no contest events with this state; route the mirror to it.
- principality-of-achaea /ledger/46 1430 contest_end (counterpart byzantine-empire) -> missing. byzantine-empire (eu-05-b, failed) carries no contest events with this state; route the mirror to it.
- duchy-of-athens /ledger/1 1211 gain (counterpart latin-empire) -> missing. Thebes c.1211 (Otto de la Roche page: 'unclear whether Henry then gave Thebes to Othon in 1209 or ... before 1211'). latin-empire has no Thebes event at all (gain from Albertino of Canossa on 8 May 1209, loss to Othon by 1211). Non-blocking: Thebes is inside the duchy's Cliopatria shape from 1206, so the map is unaffected; route to latin-empire (add the loss) or to duchy-of-athens (counterpart kingdom-of-thessalonica/Albertino).
- mongol-empire  1243 vassal_start (counterpart empire-of-trebizond) -> missing. Empire of Trebizond infobox: 'Submission to the Mongol Empire: 1243', 'Vassal of the Mongol Empire (1243–1335)'. Neither mongol-empire nor ilkhanate (ia-02, written) carries the vassal_start/vassal_end; route to ia-02.
- timurid-empire  1402 vassal_start (counterpart empire-of-trebizond) -> missing. Trebizond keyframe 1402 note: vassal of Timur after Ankara (1402); timurid-empire (ia-02, written) has no vassal event for Trebizond; route to ia-02 (page to cite: Alexios IV / Manuel III of Trebizond).
- latin-empire /ledger/6 1205 loss (counterpart second-bulgarian-empire) -> mismatch against kingdom-of-thessalonica /ledger/14 1221 loss. Serres: latin-empire loses a 40 km Seres disc to Bulgaria in April 1205 and never regains it (its /ledger/11 note: 'Serres passed to the Kingdom of Thessalonica's sphere'), while kingdom-of-thessalonica holds Serres in its 1206-1220 shapes and loses it to Epirus in late 1221 with no 1205 loss or later recovery. One of the two must change (non-blocking).

Matched: 49 rows; exceptions (no dossier yet, nobody, vassal relations recorded by the suzerain): 79 rows; full list in history/notes/phase-b/reviews/eu-05-d.json.

## Problems

- No page failed to load for the reviewer.
- Shapes have no geometry in history/data (bbox and area only), so the Paphlagonian overlap between empire-of-trebizond and nicaean-empire was judged from region specs and bboxes, not drawn.
- Reviewer applied 19 small edits in five dossiers (counterparts, confidences, notes, family, one year); all five re-validate with --resolve, 0 errors, 0 warnings; each edit is marked in the event note with '[Reviewer eu-05-d, 2026-10-19: ...]'.
- Contest mirrors missing on the despotate-of-epirus (eu-05-c) and byzantine-empire (eu-05-b) side: route there.
- Trebizond vassalage to the Mongols (1243-1335, infobox) and to Timur (1402) is missing from mongol-empire/ilkhanate and timurid-empire (ia-02).
- kingdom-of-thessalonica opened 7 pages against a budget of 5 (not a fault).
