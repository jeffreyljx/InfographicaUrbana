# Review of batch ia-01-x (Xiongnu to the Türks: additions)

Reviewer: Phase B adversarial reviewer, 2026-10-19. Inputs: the 15 dossiers, the author's report (history/notes/phase-b/reports/ia-01-x.json) and notes (history/polities/_notes/ia-01-x.md), and the counterpart dossiers that exist (khazaria, kidarites, white-huns, western-gokturks, eastern-gokturks, turgesh, uyghur-khaganate, yenisei-kyrgyz, oghuz-turks, kimek-kipchak-confederation, cuman-kipchak-confederation, rouran-khaganate, scythia, huns, xionites, xiongnu, zhizhi-xiongnu, great-yuan, kushan-empire, kara-khitans, yan). Of the section-6 Context polities only cimmerian-bosporus, dai, eastern-roman-empire, goguryeo, gojoseon, greek-city-states, greek-colonies, han, indo-parthians, indo-scythians and kushan-empire have files; the rest belong to groups that have not run.

Method: validator with --resolve (0 errors, 0 warnings on all 15); a ledger digest per dossier; 29 Wikipedia pages opened with WebFetch for spot checks (4 or more events per dossier, all confidence-3 events of the larger dossiers); grid overlaps of every keyframe against the neighbours alive in its years (history/tools/gazetteer.py resolve, H3 r5 cells of about 252.9 km2). No infobox among the 15 gives an area, so the area check records the drawn area only.

No spot-checked event was fabricated; one confidence-2 note (tokhara-yabghus 718) quoted a list the page does not give and was corrected. The failures are all cross-dossier: land or relations a neighbour's dossier records against these slugs and that the author neither mirrored nor flagged.

## Verdicts

| slug | verdict | why |
| --- | --- | --- |
| pechenegs | fix | fixed by the reviewer (dissolve region); routing items for khazaria, oghuz-turks, kimek |
| second-turkic-khaganate | pass | every checked event confirmed; three confidence-1 bridges listed as thin |
| alchon-huns | fix | all eight checked events confirmed; Turk Shahi overlap note added by the reviewer |
| sarmatians | fail | starts 200 BCE while scythia records six events against it from 339 to 224 BCE; 113 counterpart wrong |
| naiman | pass | all checked events confirmed |
| kingdom-of-gaochang | fail | no mirror for the Rouran vassalage 460-481 (rouran dossier, confidence 3); Gaoche rule unrecorded |
| kangju | fail | Transoxiana keyframe double-draws great-yuan (-36..50) and kushan-empire (51..225), unflagged |
| alania | thin | events confirmed; one shape for 360 years and the 1222 war missing |
| xueyantuo | fail | no mirror for eastern-gokturks' 642 loss; notes deny a date a cited page gives |
| donghu | fail | no mirror for yan's -300 gain; Liaoxi double-drawn with Yan -291..-223 |
| kerait | fail | 300 km radius double-draws 42 percent of the Merkit shape |
| tokhara-yabghus | fix | 718 vassal region and quote corrected by the reviewer; Turk Shahi overlap note added |
| kingdom-of-kucha | thin | two events in 800 years; the opened page dates 60 BCE and 383 CE events the notes say it lacks |
| merkit | thin | one page; war end clamped by the reviewer |
| yueban | thin | one page; confidence-1 start |

## pechenegs: fix

Findings:
- `/ledger/9/region` (applied by the reviewer): The 1091 dissolve region still included the Budjak, which ledger 7 and keyframe pechenegs_1078 give to the Cumans from 1078. Evidence: Keyframe pechenegs_1078 correction is the same union minus {region: Budjak}; Cumans page (ledger 7): 'The Cumans first entered the Bugeac (Bessarabia) at some point around 1068-1078'. Fix: Region replaced by the pechenegs_1078 correction (union minus Budjak); note marked [Reviewer ia-01-x].

Gaps for a gap-filler:
- `/ledger/1`: Who held the Don-Dnieper steppe 889-969 (confidence-1 contest bridge with khazaria, whose shape keeps it to 969; 50 percent of keyframe pechenegs_895 lies inside Khazaria 900) (try https://en.wikipedia.org/wiki/De_Administrando_Imperio)
- `/keyframe_review/2`: Crimea: the Pecheneg page says they 'controlled much of the steppes of southeast Europe and the Crimean Peninsula' in the 9th-10th centuries; not drawn (flagged by the author) (try https://en.wikipedia.org/wiki/Pechenegs)
- `/ledger/5`: Counterpart of the 1043 loss: the oghuz-turks dossier (Oghuz Yabgu State, Syr Darya) never holds the Pontic steppe and has no 1043 gain; the Oghuz of the Pontic steppe are the Torks (no dossier). The kimek-kipchak dossier claims the same steppe from 'pechenegs' in 1056. (try https://en.wikipedia.org/wiki/Torks)
- `/ledger/6`: The 1048 crossing of the Danube by Kegen and Tyrach and the settlement in Paristrion (the 1072 start is the researcher's round number) (try https://en.wikipedia.org/wiki/Paristrion)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Pechenegs: confirmed: 'Driven further west by the Khazars and Cumans by 889'; infobox 889-1091
- `/ledger/2` https://en.wikipedia.org/wiki/Pechenegs: confirmed: 'drove the Magyars west of the Dnieper River by 892'
- `/ledger/3` https://en.wikipedia.org/wiki/Etelk%C3%B6z: confirmed: 'A new Pecheneg invasion compelled the Magyars to leave Etelkoz ... around 895'; Simeon I
- `/ledger/5` https://en.wikipedia.org/wiki/Khazars: confirmed: 'By 1043, Kimeks and Qipchaqs, thrusting westwards, pressured the Oguz, who in turn pushed the Pechenegs west'
- `/ledger/8` https://en.wikipedia.org/wiki/Battle_of_Levounion: confirmed: 'On 29 April 1091, an invading force of Pechenegs was crushed'
- `/ledger/9` https://en.wikipedia.org/wiki/Pechenegs: confirmed: 'annihilated as an independent force in 1091'; survivors in imperial service (Levounion page)

Area: No infobox area on the page (checked); no Cliopatria row. Largest drawn keyframe pechenegs_895 is about 435,500 km2 on the grid (H3 r5 cells x 252.9).

## second-turkic-khaganate: pass

Gaps for a gap-filler:
- `/ledger/2`: 692 plateau gain is confidence 1 (no conquest dated between 685 and 692) (try https://en.wikipedia.org/wiki/Ilterish_Qaghan)
- `/ledger/10`: Khitan vassal_end is a 745 bridge (confidence 1); the Khitans likely returned to Tang allegiance after Qapaghan's death (716); not on the Qapaghan page (try https://en.wikipedia.org/wiki/Khitan_people)
- `/ledger/11`: Yenisei Kyrgyz vassal_end is a 745 bridge (confidence 1); the yenisei-kyrgyz dossier has no mirror for 709 or 745 (try https://en.wikipedia.org/wiki/Yenisei_Kyrgyz)
- `/ledger`: Bilge Qaghan's reign (716-734): the Tiele/Uyghur revolts of 715-716 and the wars with the Tang, Khitan and Basmyls are not in the ledger or wars (try https://en.wikipedia.org/wiki/Bilge_Qaghan)

Spot checks:
- `/ledger/5` https://en.wikipedia.org/wiki/Battle_of_Bolchu: confirmed: 'The Battle of Bolchu was fought in 711', Dzungaria, Saqal and Zhenu executed
- `/ledger/6` https://en.wikipedia.org/wiki/Battle_of_Bolchu: confirmed: 'all western Turkestan came under the Second Turkic Khaganate'; Qapaghan 'overlord of both Tashkent and Ferghana' (Qapaghan page)
- `/ledger/3` https://en.wikipedia.org/wiki/Second_Turkic_Khaganate: confirmed: 'In 696-697 Qapaghan subjugated the Khitans'
- `/ledger/4` https://en.wikipedia.org/wiki/Second_Turkic_Khaganate: confirmed: 'In 709-710 ... inflicted a crushing defeat on the Yenisei Kyrgyz'
- `/ledger/8` https://en.wikipedia.org/wiki/Qapaghan_Qaghan: confirmed: killed 'on 22 July 716'; the Second Turkic page body says 715 (flagged by the author)
- `/ledger/9` https://en.wikipedia.org/wiki/Second_Turkic_Khaganate: confirmed: 'In 744 Kutlug seized Otuken and beheaded the last Gokturk qaghan, Ozmish Qaghan'
- `/ledger/2` https://en.wikipedia.org/wiki/Second_Turkic_Khaganate: confirmed in substance: 'He died in 692 and was succeeded by his brother, Qapaghan Qaghan' (the note's quote is a paraphrase)

Area: No infobox area on the page (checked); no Cliopatria row. Largest drawn keyframe second-turkic-khaganate_692 is about 2,871,000 km2 on the grid (H3 r5 cells x 252.9).

## alchon-huns: fix

Findings:
- `/notes` (applied by the reviewer): Unflagged double-draw with Cliopatria's Turk Shahis row 561-670 over Kabulistan, Bamyan and Zabulistan. Evidence: shapes.csv turk-shahis_561 (561-643, bbox 64.8-71.7 E, 32.7-36.0 N), _644, _666; on the grid 42 percent of keyframe alchon-huns_560 lies inside Turk Shahis 600 and 100 percent of alchon-huns_630 inside Turk Shahis 650; the notes named the Turk Shahis only as the c. 665 successor. Fix: Sentence appended to notes (marked [Reviewer ia-01-x]); the turk-shahis owner should start its Kabul land c. 665.

Gaps for a gap-filler:
- `/ledger/3`: 430 Hindu Kush routes drawn as Bamyan (confidence 1) (try https://en.wikipedia.org/wiki/Khingila)
- `/ledger/12`: 515 loss of Gujarat, Rajputana and the Kausambi march (confidence-1 bridge) (try https://en.wikipedia.org/wiki/Mihirakula)
- `/ledger/18`: 560 loss of Zabulistan to the Sasanians ('may have', confidence 1) (try https://en.wikipedia.org/wiki/Nezak_Huns)
- `/ledger/19`: The Alchon and Tokhara Yabghus pages say Khuttal and Kapisa-Gandhara were 'taken over as vassals by the Western Turks' in 625: a vassal_start under western-gokturks fits the page better than an outright loss of Gandhara, which no dossier then holds (western-gokturks' 625 gain is Tokharistan only) (try https://en.wikipedia.org/wiki/Tokhara_Yabghus)
- `/ledger/20`: 630 end of the Kashmir line (confidence 1) (try https://en.wikipedia.org/wiki/Karkota_dynasty)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Alchon_Huns: confirmed: 'occupied Bactria circa 370 CE, chasing the Kidarites in the direction of India'; infobox 370-670
- `/ledger/5` https://en.wikipedia.org/wiki/Alchon_Huns: confirmed: 'Between 460 and 470 CE, the Alchons took over Gandhara and the Punjab'
- `/ledger/6` https://en.wikipedia.org/wiki/Alchon_Huns: confirmed: 'defeat in 467 CE against the Sasanian Empire of Peroz I, with Hephthalite and Alchon aid under Mehama'
- `/ledger/8` https://en.wikipedia.org/wiki/Alchon_Huns: confirmed: 'First Hunnic War (496-515)', 'maximum territorial extent', 'Gujarat and Madhya Pradesh'
- `/ledger/11` https://en.wikipedia.org/wiki/Toramana: confirmed: 'Prakashadharma of Malwa defeated him in 515 CE'; Risthal inscription; vassal after 515
- `/ledger/9` https://en.wikipedia.org/wiki/Toramana: confirmed: Sanjeli inscription 'conquest and control over Malwa and Gujarat'; Kausambi sacked 497-500
- `/ledger/16` https://en.wikipedia.org/wiki/Alchon_Huns: confirmed: 'ended the Second Hunnic War in c. 534, after an occupation which lasted nearly 15 years'
- `/ledger/17` https://en.wikipedia.org/wiki/Alchon_Huns: confirmed: 'loss of Alchon possessions in the Punjab and north India by 542'
- `/ledger/19` https://en.wikipedia.org/wiki/Alchon_Huns: confirmed (paraphrased): Khuttal and Kapisa-Gandhara 'in 625 CE ... were taken over by the expanding Western Turks'

Area: No infobox area on the page (checked); no Cliopatria row. Largest drawn keyframe alchon-huns_500 is about 1,131,000 km2 on the grid (H3 r5 cells x 252.9).

## sarmatians: fail

Findings:
- `/identity/start` (for the author): The dossier starts in -200, so six scythia events that name 'sarmatians' as counterpart (-339 contest_start; -313 contest_end, loss and contest_start; -224 contest_end and dissolve) have no mirror, and the -200 gain from scythia disagrees with scythia's -224 dissolve by 24 years; the notes mention only the unwritten Sauromatians, not these events. Evidence: Sarmatians page: in the 3rd century BC the most important Sarmatian centres were 'around the lower Don, Kalmykia, the Kuban area, and the Central Caucasus', and after the Scythian defeats of 339 and 313 BC they 'began crossing the Don river and invaded Scythia'; scythia.json ledger 12-17 (ia-01-a) carry these years with counterpart 'sarmatians'. Fix: Start at -313 with the trans-Don core (Rostov east of the Don, Kalmykia, Lower Volga, North Caucasus and the Kuban) as the found region, mirroring scythia ledger 14; add contest_start -313 and contest_end -224 with counterpart scythia on scythia's zone; move the Pontic-steppe gain from -200 to -224 to mirror scythia's dissolve ('By 200 BC' allows it); add keyframes sarmatians_-313 and sarmatians_-224. If the author holds that the pre-200 people are the Sauromatians, say so in notes and list scythia's six events for ia-01-a to re-point.
- `/ledger/4/counterpart` (for the author): The 113 gain of the Tisza-Transylvania steppe names roman-empire, which never held it. Evidence: Iazyges page: Trajan 'did not incorporate the steppe between the Tisza river and the Transylvanian mountains into the province of Dacia'; the Iazyges took 'absolute control of the territory from the Dacians'. Fix: Counterpart 'Dacians' (as in ledger 3) or nobody; keep the year.

Gaps for a gap-filler:
- `/ledger/6`: 260 loss to Gothia rests on Cliopatria's Gothia 260 shape (confidence 1) (try https://en.wikipedia.org/wiki/Goths)
- `/ledger/7`: The huns dossier gains the Don Alans in 370 (counterpart string 'Alans of the Don (Pontic Alans)'); this dossier dissolves in 375 to huns: the two disagree by five years (try https://en.wikipedia.org/wiki/Alans)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Sarmatians: confirmed: 'By 200 BC, the Sarmatians replaced the Scythians as the dominant people of the steppes'
- `/ledger/2` https://en.wikipedia.org/wiki/Sarmatians: confirmed: 'At their greatest reported extent, around 100 BC, these tribes could be found from the Danube and eastward to the Volga'
- `/ledger/3` https://en.wikipedia.org/wiki/Iazyges: confirmed: 'In c. 44 BC, they moved into modern-day Hungary and Serbia ... between the Danube and Tisza rivers'
- `/ledger/4` https://en.wikipedia.org/wiki/Iazyges: year confirmed (annexation of Dacia dated 113 on the page); counterpart not supported (see fixes)
- `/ledger/5` https://en.wikipedia.org/wiki/Sarmatians: confirmed: the Goths 'conquered the Pontic Steppe around 200'; 'In the 3rd century AD, the Germanic Goths broke the Sarmatian dominance'
- `/ledger/7` https://en.wikipedia.org/wiki/Sarmatians: confirmed: 'In 375, the Huns conquered most of the Alans living to the east of the Don river'

Area: No infobox area on the page (checked); no Cliopatria row. Largest drawn keyframe sarmatians_113 is about 895,000 km2 on the grid (H3 r5 cells x 252.9).

## naiman: pass

Gaps for a gap-filler:
- `/ledger/0`: The Kara-Khitan vassal period before 1175 is undated, and the kara-khitans dossier has no Naiman vassal_start or vassal_end to mirror the 1175 found (flagged by the author) (try https://en.wikipedia.org/wiki/Qara_Khitai)
- `/wars/1`: 'Pursuit of Kuchlug' runs 1204-1218, after the dossier's end; harmless (no zones) but it belongs to the kara-khitans dossier (try https://en.wikipedia.org/wiki/Kuchlug)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Naimans: confirmed: 'were subservient to them until 1175'
- `/ledger/1` https://en.wikipedia.org/wiki/Naimans: confirmed: 'In 1199, Temujin (Genghis Khan) together with an ally Ong khan launched a campaign against the Naimans'
- `/ledger/2` https://en.wikipedia.org/wiki/Tayang_Khan: confirmed: 'The armies first met on 17 May 1204 in the Khangai Mountains'; crossed the Orkhon the next day
- `/ledger/3` https://en.wikipedia.org/wiki/Tayang_Khan: confirmed: Tayang 'killed whilst attempting to escape'; reign c. 1198-1204 (the Naimans page says 1203; flagged)

Area: No infobox area on the page (checked); no Cliopatria row. Largest drawn keyframe naiman_1175 is about 908,000 km2 on the grid (H3 r5 cells x 252.9).

## kingdom-of-gaochang: fail

Findings:
- `/ledger (after /ledger/0)` (for the author): The rouran-khaganate dossier's 460 vassal_start (confidence 3) and 481 vassal_end name kingdom-of-gaochang, and this ledger has neither; the oasis is drawn as independent while 92 percent of it lies inside Cliopatria's Rouran shape of 470. Evidence: Gaochang page (this dossier's own source): the Northern Liang remnants ruled 'until 460 when they were conquered by the Rouran Khaganate', and the Rouran 'appointed a Han Chinese named Kan Bozhou to rule as King of Gaochang in 460'; rouran-khaganate.json ledger 1-2. The notes say the suzerains are 'named in notes only', which the reciprocity rule does not allow. Fix: Add vassal_start 460 and vassal_end 481 with counterpart rouran-khaganate, region {place: Gaochang, km: 120}, sources the Gaochang and Gaoche pages; remove the 'not drawn' sentence from notes.
- `/ledger/1` (for the author): The Gaoche overlordship is recorded only as a rename although the page says Gaochang 'thus passed under Gaoche rule'. Evidence: Gaochang page: the Gaoche king Afuzhiluo 'killed King Kan Shougui'; 'Gaochang thus passed under Gaoche rule' (Kan Shougui '478-488? or 478-491?'). Fix: Add vassal_start c. 488 with counterpart 'Gaoche (Fufuluo)' (confidence 2) and its end from the Gaoche page (the Fufuluo statelet's fall), plus the Western Turkic alliance before 640 if the Hou Junji page dates it.

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Gaochang: confirmed: Northern Liang remnants 'conquered by the Rouran Khaganate' in 460; Kan Bozhou appointed 460
- `/ledger/2` https://en.wikipedia.org/wiki/Gaochang: confirmed: reign table 'Ma Ru | 496-501'
- `/ledger/3` https://en.wikipedia.org/wiki/Gaochang: confirmed: 'Qu Jia | 501-525'; Qu rule to 640
- `/ledger/4` https://en.wikipedia.org/wiki/Protectorate_General_to_Pacify_the_West: confirmed: 'On 19 September 640 Hou Junji of Tang conquered Gaochang and set up Xi Prefecture'

Area: No infobox area on the page (checked); no Cliopatria row. Largest drawn keyframe kingdom-of-gaochang_460 is about 41,000 km2 on the grid (H3 r5 cells x 252.9).

## kangju: fail

Findings:
- `/ledger/3 and /keyframe_review/2` (for the author): The -36 gain of Sogdia and Ferghana (counterpart nobody, confidence 1) and keyframe kangju_-36 (Transoxiana, -36..270) double-draw two neighbours' land without a word in notes: Dayuan (great-yuan dossier, alive to 50) lies wholly inside the keyframe, and 28 percent of the keyframe (about 213,000 km2) lies inside the Kushan shapes from 51. Evidence: Grid overlap: Cliopatria 'Great Yuan' -50 (172 cells) is 100 percent inside kangju_-36; 'Kushan Empire' 51 overlaps 844 of its 3035 cells. great-yuan.json dissolves in 50 naming kangju as successor for Fergana but has no event with kangju; kushan-empire.json ledger 2 gains Fergana and Sogdia in 51 (counterpart nobody, confidence 1). Kangju page: 'By this time it had gained control of Dayuan and Sogdiana' (undated, Hanshu period). Fix: Make the Dayuan relation a vassal_start of great-yuan (or a gain from great-yuan at 50 mirroring its dissolve) instead of a gain from nobody, keeping Ferghana out of the direct shape until then; from 51 either subtract the Kushan shape (new keyframe kangju_51) or keep the land and ask sa-02 to drop kushan ledger 2; say which in notes.
- `/ledger/1/note` (applied by the reviewer): The note dated Zhizhi's settling among the Kangju to 44 BCE as if the page said so. Evidence: Zhizhi Chanyu page: 'In 44 BCE he was reported to be on the north slope of the Tian Shan'; the westward move began 'in 49 BCE'; the Kangju alliance and fortress are undated. Fix: Note amended to say the year is a reading (marked [Reviewer ia-01-x]); confidence 2 kept since the land is on the page.
- `/ledger/4/counterpart` (for the author): The 270 dissolve names xionites, whose dossier starts in 353. Evidence: Kangju page: 'Around 270 CE they were subdued by the Xionites'; xionites.json identity 353..401. Fix: Keep the page's counterpart but say in notes that the xionites dossier begins in 353, and list it for ia-01 so the xionites owner can decide whether to start earlier; otherwise counterpart nobody.

Gaps for a gap-filler:
- `/ledger/0`: Tributary ties to the Yuezhi and the Xiongnu ('acknowledges sovereignty to the Yuezhi people in the South and the Xiongnu in the East') are not drawn (try https://en.wikipedia.org/wiki/Kangju)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Kangju: confirmed: Zhang Qian 'visited the area c. 128 BCE'
- `/ledger/1` https://en.wikipedia.org/wiki/Zhizhi_Chanyu: year not on page: 44 BCE is the Tian Shan report; the arrival in Kangju is undated (note amended)
- `/ledger/2` https://en.wikipedia.org/wiki/Zhizhi_Chanyu: confirmed: Chen Tang and Gan Yanshou, 40,000 men, 'Upon reaching Kangju (around modern Taraz)'; Zhizhi killed 36 BCE
- `/ledger/3` https://en.wikipedia.org/wiki/Kangju: confirmed (undated): 'had gained control of Dayuan and Sogdiana'; five lesser kings
- `/ledger/4` https://en.wikipedia.org/wiki/Kangju: confirmed: 'Around 270 CE they were subdued by the Xionites'

Area: No infobox area on the page (checked); no Cliopatria row. Largest drawn keyframe kangju_-36 is about 767,500 km2 on the grid (H3 r5 cells x 252.9).

## alania: thin

Gaps for a gap-filler:
- `/wars`: The first Mongol war of 1222 (the page: the Mongols 'met the Alans for the first time in 1222') is not in wars; nor the 1033 Shirvan raid with the Rus (try https://en.wikipedia.org/wiki/Alania)
- `/keyframe_review/0`: One shape for 880-1239 (360 years): the 1060s Alanian-Georgian alliance and any change of the Laba-Argun extent are undated; 96 percent of the shape lies inside Cliopatria's Khazaria to 969 and the khazaria dossier has no 880 loss (flagged by the author) (try https://en.wikipedia.org/wiki/Alans)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Alania: confirmed: 'In the late 9th century, Alania became independent from the Khazars'
- `/ledger/1` https://en.wikipedia.org/wiki/Alania: confirmed: 'the siege of Maghas, which began in November or December 1239'
- `/ledger/2` https://en.wikipedia.org/wiki/Maghas: confirmed: 'ended in the 2nd lunar month of 1240 (i.e. 6-24 February)'
- `/ledger/3` https://en.wikipedia.org/wiki/Alania: confirmed: infobox 'Fall of Maghas ... 1240'

Area: No infobox area on the page (checked); no Cliopatria row. Largest drawn keyframe alania_880 is about 54,000 km2 on the grid (H3 r5 cells x 252.9).

## xueyantuo: fail

Findings:
- `/ledger (between /ledger/1 and /ledger/2) and /notes` (for the author): The eastern-gokturks dossier (reviewed) loses Hetao minus Ordos to xueyantuo in 642 and this ledger has no mirror gain; the notes say 'The pages do not support a 642 Yellow River campaign', but a page this dossier cites says it. Evidence: Eastern Turkic Khaganate page (in this dossier's sources): 'In 642 the Xueyantuo drove them south of the river.'; eastern-gokturks.json ledger 12 (642 loss, region minus [Hetao, Ordos], counterpart xueyantuo). Fix: Add a 642 gain from eastern-gokturks with region {minus: [{region: Hetao}, {region: Ordos}]} (confidence 2, source the Eastern Turkic Khaganate page); split keyframe xueyantuo_630 into 630..641 and xueyantuo_642 (642..646, the 630 shape plus Hetao minus Ordos); correct the notes sentence.

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Xueyantuo: confirmed: 'In 629 the Xueyantuo Yinan-erkin declared himself' khagan; infobox 628
- `/ledger/1` https://en.wikipedia.org/wiki/Xueyantuo: confirmed: 'On March 27, 630, the Xueyantuo allied with the Tang to defeat the Eastern Turkic Khaganate in the Yin Mountains'; ETK page: 'Xueyantuo occupied the territory of the former Turkic Khaganate'
- `/ledger/2` https://en.wikipedia.org/wiki/Xueyantuo: confirmed: 'On August 1, 646, the Xueyantuo were defeated by the Uyghurs (Huihe) and the Tang'
- `/notes` https://en.wikipedia.org/wiki/Eastern_Turkic_Khaganate: not on page as claimed: the page does give 642 ('In 642 the Xueyantuo drove them south of the river')

Area: No infobox area on the page (checked); no Cliopatria row. Largest drawn keyframe xueyantuo_630 is about 1,112,000 km2 on the grid (H3 r5 cells x 252.9).

## donghu: fail

Findings:
- `/keyframe_review/0, /ledger/0 and /ledger/1` (for the author): The yan dossier gains 'the lands of the Donghu' in -300 (Cliopatria's Yan growth of -291 outside Liaodong) and this dossier neither loses them nor leaves them out: Liaoxi is drawn by both states -291..-223 (139 grid cells, about 35,000 km2, 16 percent of the Donghu shape), and the notes say Yan is 'a counterpart for the 300 BCE war, not a ledger event'. Evidence: yan.json ledger 6 (-300 gain, counterpart 'Donghu', region Yan -291 minus Yan -292 minus Liaodong); Donghu people page: 'In 300 BCE Qin Kai, a general taken hostage from the state of Yan ... defeated the Donghu'; Liaoxi in the gazetteer is Liaoning minus Liaodong, which the Yan -291 shape enters. Fix: Subtract {cliopatria: Yan, year: -291} from the found, keyframe and dissolve regions (the Donghu land after Qin Kai's campaign), or add a -300 loss to yan of that land; set W0 zones to it; correct the notes sentence.

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Donghu_people: confirmed: 'In 300 BCE Qin Kai ... defeated the Donghu'; they lived in northern Hebei, southeastern Inner Mongolia and western Liaoning
- `/ledger/1` https://en.wikipedia.org/wiki/Modu_Chanyu: confirmed: 'By 208 BCE, the Donghu had been defeated and their remnants split into the Xianbei and Wuhuan tribes' (the Donghu lead says 150 BCE; flagged)

Area: No infobox area on the page (checked); no Cliopatria row. Largest drawn keyframe donghu_-300 is about 220,000 km2 on the grid (H3 r5 cells x 252.9).

## kerait: fail

Findings:
- `/keyframe_review/0 (and /ledger/0, /ledger/1, /identity/successors/0/land)` (for the author): The 300 km radius around Ulaanbaatar double-draws the Merkit land of the same years (1050-1200): 283 grid cells (about 72,000 km2) of the Kerait shape lie inside the merkit keyframe (Selenge and Bulgan provinces), 42 percent of the Merkit shape, with no word in either dossier. Evidence: Keraites page names only 'the upper Onon and Kherlen rivers and the Tuul river'; Merkit page: 'The Merkits lived in the basins of the Selenga and lower Orkhon River'; grid overlap of kerait_1000 and merkit_1050. Fix: Subtract {union: [{admin1: Selenge, country: Mongolia}, {admin1: Bulgan, country: Mongolia}]} from the Kerait region in the keyframe, both ledger events and the successor land, or redraw it from the three rivers; note the boundary with the Merkits.

Gaps for a gap-filler:
- `/ledger`: Liao and Qara Khitai vassalage undated (infobox 'Subject to'); the capital Orta Balagasun named on the page is not recorded; Toghrul's 1196/1198 restorations (try https://en.wikipedia.org/wiki/Toghrul)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Keraites: confirmed: 'absorbed into the Church of the East around 1000 by Metropolitan Abdisho'; infobox 11th century
- `/ledger/1` https://en.wikipedia.org/wiki/Keraites: confirmed: 'In 1203, Temujin defeated the Keraites'

Area: No infobox area on the page (checked); no Cliopatria row. Largest drawn keyframe kerait_1000 is about 306,000 km2 on the grid (H3 r5 cells x 252.9).

## tokhara-yabghus: fix

Findings:
- `/ledger/5 and /ledger/6 (region, counterpart, note)` (applied by the reviewer): The 718 vassal tint drew Kapisa and Gandhara and quoted 'Chinese sources from 718 list Khuttal, Chaghaniyan, Kapisa-Gandhara', which the page does not say: Kapisa-Gandhara belongs to the 625 list, and the 718 account names Kabul and Zabul. Evidence: Tokhara Yabghus page: the 718 account 'shows that the Yabghu of Tokharistan ruled a vast area circa 718 CE', 'formed of the territories north and south of the Hindu Kush, including the areas of Kabul and Zabul'; its list names 'the king of [Zabul]', 'the king of [Kabul]', 'Khuttal', 'Chaghanian'. Fix: Region now Khatlon + Surkhandarya + Kabulistan + Zabulistan, counterpart 'Khuttal, Chaghaniyan, Kabul and Zabul' on both events, ledger 5 note rewritten with the page's words (marked [Reviewer ia-01-x]).
- `/notes` (applied by the reviewer): Unflagged overlap of keyframe tokhara-yabghus_657 with Cliopatria's Turk Shahis shapes of 644-717. Evidence: shapes.csv turk-shahis_644/_666/_674/_692 reach 38.4 N; on the grid 85 percent of tokhara-yabghus_657 lies inside Turk Shahis 680; the notes named only the 718 tint. Fix: Sentence appended to notes (marked [Reviewer ia-01-x]).

Gaps for a gap-filler:
- `/ledger/6`: 758 vassal_end is the dossier-end bridge (confidence 1) (try https://en.wikipedia.org/wiki/Tokharistan)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Tokhara_Yabghus: confirmed: 'In 625, Tong Yabgu invaded Tokharistan and forced the Hephthalite principalities to submit'; capital Kunduz
- `/ledger/1` https://en.wikipedia.org/wiki/Tokhara_Yabghus: confirmed: 'In 652-653 CE, the Arabs under Abdallah ibn Amir conquered the whole of Tokharistan'
- `/ledger/4` https://en.wikipedia.org/wiki/Tokhara_Yabghus: confirmed: 'In 710, Qutaiba ibn Muslim was able to re-establish Muslim control over Tokharistan'
- `/ledger/5` https://en.wikipedia.org/wiki/Tokhara_Yabghus: not on page as written: the 718 list names Kabul and Zabul, not Kapisa-Gandhara (fixed)
- `/ledger/7` https://en.wikipedia.org/wiki/Tokhara_Yabghus: confirmed: remnants 'surviving in the area of Badakhshan until 758 CE'; Wu-na-to's visit 758

Area: No infobox area on the page (checked); no Cliopatria row. Largest drawn keyframe tokhara-yabghus_657 is about 95,000 km2 on the grid (H3 r5 cells x 252.9).

## kingdom-of-kucha: thin

Gaps for a gap-filler:
- `/ledger`: Dated events on the page the author opened are missing (the notes say 'the page dates no early event'): Xiongnu control in the 2nd century BCE; 'In 60 BCE, the Han court established the Protectorate of the Western Regions' (vassal_start, han-dynasty); 'conquered Kucha in 383 CE' (Lu Guang of Former Qin); Tibetan domination in the late 7th century; Bai Huan to 789. 84 percent of the Kucha shape lies inside Cliopatria's Han shape of 100, so the Han tie matters for the tint. (try https://en.wikipedia.org/wiki/Kucha)
- `/ledger/0`: Founding is confidence 1 ('2nd century BCE') (try https://en.wikipedia.org/wiki/Protectorate_of_the_Western_Regions)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Kucha: confirmed: infobox 'Established: 2nd century BCE'; controlled 'by the steppe federation of Xiongnu'
- `/ledger/1` https://en.wikipedia.org/wiki/Protectorate_General_to_Pacify_the_West: confirmed: 'In 648, the Tang conquered Kucha'

Area: No infobox area on the page (checked); no Cliopatria row. Largest drawn keyframe kingdom-of-kucha_-150 is about 60,000 km2 on the grid (H3 r5 cells x 252.9).

## merkit: thin

Findings:
- `/wars/0/to` (applied by the reviewer): The war ran to 1218, past the dossier's end (1200), with zones. Evidence: Merkit page: 'they were defeated in 1200 by Genghis Khan' (infobox 'Disestablished: 1200'); the remnants were 'crushed' in 1215-1218. Fix: 'to' set to 1200; the later fighting kept in the outcome; note marked [Reviewer ia-01-x].

Gaps for a gap-filler:
- `/ledger`: One page opened (under the 2-page minimum): the c. 1181 Borte raid, the five wars of 1191-1207, Toqto'a's alliance with Tayang in 1204 and his death in 1208 are not events; the found is confidence 1 ('11th century'); the shape is double-drawn with kerait (see the kerait finding) (try https://en.wikipedia.org/wiki/Toqto%27a_Beki)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Merkit: confirmed: infobox 'Established: 11th century' (confidence 1 bridge)
- `/ledger/1` https://en.wikipedia.org/wiki/Merkit: confirmed: 'After a struggle of over 20 years, they were defeated in 1200 by Genghis Khan'

Area: No infobox area on the page (checked); no Cliopatria row. Largest drawn keyframe merkit_1050 is about 171,000 km2 on the grid (H3 r5 cells x 252.9).

## yueban: thin

Gaps for a gap-filler:
- `/ledger/0`: Start is the infobox 160 (confidence 1); the page gives 'Xiongnu migrations (93 CE - circa 380 CE)'; one page opened (try https://en.wikipedia.org/wiki/Northern_Xiongnu)
- `/ledger/1`: The Tiele attack ('the Yueban were attacked by the Tiele, who had split from the Rouran in 487') and the 448 embassy to the Northern Wei against the Rouran are not events (try https://en.wikipedia.org/wiki/Gaoche)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Yueban: confirmed: infobox 'Established: 160'; Xianbei campaigns 'Between 155 and 166'
- `/ledger/1` https://en.wikipedia.org/wiki/Yueban: confirmed: 'The Yueban principality ceased to existed during the 480s and split into four tribes'; infobox 490

Area: No infobox area on the page (checked); no Cliopatria row. Largest drawn keyframe yueban_160 is about 330,500 km2 on the grid (H3 r5 cells x 252.9).

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| pechenegs 889 found (khazaria) | - | missing | khazaria (ia-01-d) has no loss to pechenegs; it keeps the Don-Dnieper steppe in its shape to 969 and lists pechenegs as successor. Flagged by the author (confidence-1 contest bridge). Route to ia-01-d. |
| pechenegs 889 contest_start (khazaria) | - | missing | No contest events in khazaria; 50 percent of pechenegs_895 lies inside Khazaria 900. Flagged by the author. |
| pechenegs 969 contest_end (khazaria) | - | missing | As above. |
| pechenegs 892 gain (magyars) | - | exception | No magyars dossier (Cliopatria row 840-910; listed by the author). Cliopatria Magyars 895 still overlaps pechenegs_895 by 36 percent. |
| pechenegs 895 gain (magyars) | - | exception | As above. |
| pechenegs 1043 loss (oghuz-turks) | - | missing | oghuz-turks (ia-01-e) has no 1043 gain and never holds the Pontic steppe (its land is the Syr Darya and Aral steppes); the Oghuz who pushed the Pechenegs are the Torks of the Pontic steppe, who have no dossier. Route to ia-01-e / a Torks dossier. |
| kimek-kipchak-confederation 1056 gain (pechenegs) | - | mismatch | kimek ledger 4 takes the Pontic steppe east of the Don from pechenegs in 1056; the pechenegs dossier lost that steppe in 1043 to the Oghuz. Route to the kimek owner: counterpart should be the Torks/Oghuz. |
| kimek-kipchak-confederation 896 gain (pechenegs) | - | mismatch | kimek ledger 1 takes the Ural-Turgay steppe from pechenegs in 896 (confidence 1); the pechenegs dossier starts in 889 already west of the Don and never holds that land. Route to the kimek owner: counterpart nobody, or the pechenegs owner extends the shape east before 889. |
| pechenegs 1078 loss (cuman-kipchak-confederation) | cuman-kipchak-confederation 1078 gain | matched | Budjak, both sides confidence 2. |
| pechenegs 1072 contest_start (byzantine-empire) | - | exception | byzantine-empire (eu-05) not written yet; also contest_end and dissolve 1091. |
| second-turkic-khaganate 682 found (tang-dynasty) | - | exception | tang-dynasty (ea-04) not written yet. |
| second-turkic-khaganate 685 gain (Toquz Oghuz) | - | exception | No dossier; listed by the author. |
| second-turkic-khaganate 697 vassal_start (Khitans) | - | exception | No dossier; listed by the author (vassal_end 745 is a confidence-1 bridge). |
| second-turkic-khaganate 709 vassal_start (yenisei-kyrgyz) | - | missing | yenisei-kyrgyz has no vassal_start with second-turkic-khaganate in 708-710 (nor the 745 vassal_end). Route to the yenisei-kyrgyz owner (ia-01). |
| second-turkic-khaganate 711 contest_start (turgesh) | turgesh 711 contest_start | matched | Dzungaria. |
| second-turkic-khaganate 716 contest_end (turgesh) | turgesh 715 contest_end | matched | Within a year; the Qapaghan page says 22 July 716, the Second Turkic page body 715 (flagged by both authors). |
| second-turkic-khaganate 711 vassal_start (Chach and Ferghana (western Turkestan)) | - | exception | No dossier; listed by the author. |
| second-turkic-khaganate 744 loss (uyghur-khaganate) | uyghur-khaganate 744 found | matched | And the 745 dissolve matches uyghur-khaganate 745 gain. |
| second-turkic-khaganate 692 gain (nobody) | - | exception | Plateau drawn from Cliopatria Turgesh 692; turgesh 705-749 shapes still contain all of this keyframe (100 percent overlap) until the turgesh correction is applied (flagged by both authors). |
| oghuz-turks 750 found (second-turkic-khaganate) | - | mismatch | second-turkic-khaganate ends in 745; oghuz-turks ledger 0 names it as the 750 counterpart. Route to ia-01-e (counterpart nobody or uyghur-khaganate/karluks). |
| alchon-huns 370 found (kidarites) | - | missing | kidarites (ia-01-c) has no event with alchon-huns (it names alchon-huns only as successor of the Gandhara remnant); also missing: 370 contest_start, 430 gain, 460 gain of Gandhara and the Punjab, 467 contest_end. Route to ia-01-c. |
| alchon-huns 450 loss (white-huns) | white-huns 450 found | mismatch | white-huns found has counterpart None; it should name alchon-huns for Bactria (or kidarites, as its predecessors say). |
| white-huns 490 gain (alchon-huns) | - | missing | white-huns ledger 7 (confidence 1) takes the Indian lands from alchon-huns in 490; alchon-huns keeps them 460-541 and the Alchon page calls the Alchon a separate entity. Flagged by the author; route to ia-01-c to drop the Indian lands from white-huns 490-533 (62 percent of alchon-huns_500 lies inside White Huns 500). |
| alchon-huns 625 loss (western-gokturks) | - | missing | western-gokturks ledger 7 gains Tokharistan in 625 from the Hephthalite principalities, not Gandhara; the pages say Khuttal and Kapisa-Gandhara became Western Turk vassals. Route both: a vassal_start under western-gokturks would match the pages. |
| alchon-huns 670 dissolve (turk-shahis) | - | exception | No turk-shahis dossier yet; Cliopatria Turk Shahis 561-670 double-draws Kabulistan (now flagged in alchon notes). |
| alchon-huns 496 contest_start (gupta-empire) | - | exception | gupta-empire (sa-02) not written; also 500 gain, 515 loss and contest_end, 520-534 occupation. white-huns carries the same 496-534 contest with gupta (double). |
| alchon-huns 380 gain (sasanian-empire) | - | exception | sasanian-empire not written; also 484 gain and 560 loss. |
| sarmatians -200 gain (scythia) | scythia -224 dissolve | mismatch | 24 years apart; scythia also has -339 contest_start, -313 contest_end, loss and contest_start, and -224 contest_end naming sarmatians, none mirrored (sarmatians starts -200). Blocking for sarmatians. |
| sarmatians 375 dissolve (huns) | huns 370 gain | mismatch | huns ledger 1 gains the Don Alans in 370 with counterpart string 'Alans of the Don (Pontic Alans)'; the Sarmatians page says 375. Route to the huns owner (slug sarmatians, year). |
| sarmatians 113 gain (roman-empire) | - | mismatch | roman-empire not written, and the Iazyges page says Rome never incorporated the Tisza steppe; counterpart should be Dacians. |
| sarmatians 207 loss (gothia) | - | exception | gothia has no dossier (Cliopatria row); also 260. |
| naiman 1175 found (kara-khitans) | - | missing | kara-khitans (ia-01-g) has no Naiman vassal_start/vassal_end. Flagged by the author. |
| naiman 1204 dissolve (mongol-empire) | - | exception | mongol-empire not written; Cliopatria starts it in 1206 (also kerait 1203, merkit 1200). |
| rouran-khaganate 460 vassal_start (kingdom-of-gaochang) | - | missing | No mirror in kingdom-of-gaochang (blocking there); rouran ledger 2 vassal_end 481 likewise. |
| kingdom-of-gaochang 460 found (northern-liang) | - | exception | northern-liang (ea-03) not written. |
| kangju -44 loss (zhizhi-xiongnu) | zhizhi-xiongnu -44 gain | matched | zhizhi-xiongnu uses the string 'Kangju'; should now be the slug kangju (route to ia-01-a). |
| kangju -36 gain (zhizhi-xiongnu) | zhizhi-xiongnu -36 dissolve | matched | As above ('Kangju' string). |
| kangju 270 dissolve (xionites) | - | mismatch | xionites dossier is 353..401; the Kangju page says 270. |
| great-yuan 50 dissolve (None) | - | mismatch | great-yuan names kangju as successor for Fergana but kangju already draws Fergana from -36 (gain from nobody); no event pairs them. |
| kushan-empire 51 gain (nobody) | - | mismatch | kushan ledger 2 (confidence 1) gains Fergana and Sogdia, 28 percent of kangju_-36 (alive to 270), with no kangju loss. Route to sa-02 and kangju. |
| alania 880 found (khazaria) | - | missing | khazaria has no 880 loss; it keeps the North Caucasus to 969 (96 percent of alania_880 inside Khazaria 900). Flagged by the author. |
| xueyantuo 630 gain (eastern-gokturks) | eastern-gokturks 630 loss | matched | Also the 629 found. |
| eastern-gokturks 642 loss (xueyantuo) | - | missing | No 642 gain in xueyantuo; blocking there. |
| xueyantuo 646 dissolve (tang-dynasty) | - | exception | tang-dynasty not written; 99 percent of xueyantuo_630 lies inside Cliopatria Tang 640 (flagged by the author). |
| donghu -208 dissolve (xiongnu) | xiongnu -208 gain | matched | xiongnu uses the string 'Donghu'; should now be the slug donghu (route to ia-01-a). |
| yan -300 gain (Donghu) | - | missing | yan ledger 6 takes Yan's -291 growth from 'Donghu'; donghu has no loss and still draws Liaoxi; blocking for donghu; yan should use the slug. |
| tokhara-yabghus 657 gain (western-gokturks) | western-gokturks 657 loss | matched |  |
| tokhara-yabghus 625 found (Hephthalite principalities of Tokharistan) | - | exception | No dossier; western-gokturks 625 gain names the same string. |
| tokhara-yabghus 710 loss (umayyad-caliphate) | - | exception | Not written; also 652-653 rashidun contest and 758 tang dissolve. |
| kingdom-of-kucha 648 dissolve (tang-dynasty) | - | exception | Not written; 84 percent of the Kucha shape inside Cliopatria Han 100 with no Han vassal event (thin). |
| kerait 1203 dissolve (mongol-empire) | - | exception | Not written. |
| merkit 1200 dissolve (mongol-empire) | - | exception | Not written; kerait_1000 overlaps 42 percent of merkit_1050 (blocking for kerait). |

## Other

- Gazetteer: Kausambi (place, alchon-huns) is the only unresolved name; the author drew it as a coordinate radius.
- Counterparts needing dossiers: Torks (Oghuz of the Pontic steppe) (torks); Toquz Oghuz (toquz-oghuz); Khitans (pre-Liao) (khitans); Gaoche (Fufuluo) (gaoche); Nezak Huns (nezak-huns); Aulikara dynasty of Malwa (aulikara-dynasty); Dacians (dacians); Sauromatians (sauromatians); Scythian kingdom of Crimea (scythian-kingdom-of-crimea); Kangar union (kangar-union); Chach and Ferghana (western Turkestan) (chach-and-ferghana); Hephthalite principalities of Tokharistan (hephthalite-principalities); Magyars (magyars); Wuhuan (wuhuan); Basmyls (basmyls).
- Validator: 0 errors, 0 warnings on all 15 with --resolve; re-run after the reviewer's edits on pechenegs, tokhara-yabghus, alchon-huns, kangju and merkit: 0 errors, 0 warnings.
- No page failed to load; no infobox of the 15 gives an area, so no area ratio is possible; drawn areas are given from the grid instead.
- Six dossiers fail on cross-dossier conflicts the author did not mirror or flag: sarmatians (scythia -339..-224), kingdom-of-gaochang (rouran 460/481 vassalage), kangju (great-yuan and kushan-empire double-draw), xueyantuo (eastern-gokturks 642), donghu (yan -300), kerait (merkit overlap).
- Mismatches routed to other groups: khazaria (pechenegs, alania), oghuz-turks and kimek-kipchak-confederation (pechenegs 1043/1056, 896; oghuz 750 found names a khaganate that ended in 745), yenisei-kyrgyz (709/745), kidarites and white-huns and western-gokturks (alchon-huns), huns (375 vs 370), kara-khitans (naiman 1175), xionites (kangju 270, xionites start 353), great-yuan and kushan-empire (kangju), zhizhi-xiongnu, xiongnu and yan (plain-name strings 'Kangju' and 'Donghu' should become slugs).
- Cliopatria's Turk Shahis row (shapes from 561) double-draws alchon-huns 561-670 and tokhara-yabghus 657-709; no turk-shahis dossier exists yet; the reviewer flagged it in both dossiers' notes.
- Reviewer edits applied in place (re-read before and read back after): pechenegs /ledger/9/region; tokhara-yabghus /ledger/5-6 region, counterpart and note, /notes; alchon-huns /notes; kangju /ledger/1/note; merkit /wars/0/to. The rewritten files keep the 1-space indent and now end with a newline.
