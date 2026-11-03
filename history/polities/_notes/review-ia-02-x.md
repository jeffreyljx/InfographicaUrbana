# Review of batch ia-02-x (Mongols and successor khanates, additions)

Reviewer run of 2026-10-19. Ten new dossiers, none with Cliopatria rows; all validate with 0 errors (one known resolve warning, nizari-ismaili-state, in ulus-of-hulegu). Spot checks: 4-6 events per dossier, weighted to confidence 3 and the largest land moves, each opened with WebFetch. No event was found fabricated; one confidence-3 date was not on its page (ogedeid-ulus 1277, lowered), one confidence-3 vassal start was mis-dated (ulus-of-jochi 1252, should be 1243).

Blocking rule used: a finding blocks when it leaves land drawn by the wrong state or by none (an unexplained keyframe change, a missing gain/loss/vassal/occupation, a missing mirror inside this batch), or when a confidence-3 event is mis-dated. Non-blocking findings (ruler gaps, quotes, a missing contest pair with no land change) are listed with applied: false.

| dossier | verdict |
| --- | --- |
| ogedeid-ulus | fix |
| ulus-of-chagatai | fail |
| ariq-boke | fix |
| ulus-of-jochi | fail |
| ulus-of-hulegu | thin |
| amirate-of-qazaghan | thin |
| uzbek-khanate-of-abul-khayr | thin |
| turpan-khanate | pass |
| kara-del | fail |
| sufi-dynasty-of-khwarazm | fail |

## ogedeid-ulus: fix

Findings:

- `/ledger/3` (applied by the reviewer): 1277 gain of Almaliq at confidence 3, but neither cited page dates the capture. Evidence: Kaidu-Kublai war page: 'Kublai's son Nomukhan and generals occupied Almaliq in 1266-1276' then 'However, Kaidu captured Almaliq' (no year); Kaidu page: 'was also able to recover control over Almaliq in the east' (no year). Fix: Confidence 2 (done; note annotated).
- `/ledger/2, /ledger/3, /ledger/4, /ledger/5, /ledger/6, /ledger/7` (applied by the reviewer): Counterpart yuan-dynasty for events of 1275-1289; the yuan-dynasty row starts in 1294. Evidence: polities.csv yuan-dynasty 1294..1374; the mongol-empire dossier carries Kublai's state to 1293 (/ledger/80 rename 18 Dec 1271, /ledger/93 dissolve 1293 to yuan-dynasty). Fix: Counterpart mongol-empire (done; dossier notes annotated).
- `/wars/0/belligerents, /wars/1/belligerents` (applied by the reviewer): Only post-1294 slugs (chagatai-khanate, yuan-dynasty, ilkhanate) for wars that start in 1268 and 1288. Evidence: Same row years as above; ulus-of-chagatai, mongol-empire and ulus-of-hulegu are the polities alive before 1294. Fix: Added ulus-of-chagatai and mongol-empire to /wars/0, ulus-of-hulegu to /wars/1 (done).
- `/ledger/8, /ledger/9` (for the author): The Altai/western Mongolia contest 1289-1301 crosses the 1293/1294 change of counterpart; L8 still names yuan-dynasty in 1289 so that the pair validates. Evidence: yuan-dynasty row starts 1294; mongol-empire ends 1293. Fix: Split it: contest_start mongol-empire 1289, contest_end mongol-empire 1293 (c1, bookkeeping), contest_start yuan-dynasty 1294 (c1), contest_end yuan-dynasty 1301 (as now).
- `/ledger/10` (for the author): vassal_end of 1306 names ulus-of-chagatai, which ends in 1293; the client relation is not drawn 1294-1306 and has no mirror anywhere. Evidence: ulus-of-chagatai /identity/end 1293; chagatai-khanate (from 1294) has no vassal event with ogedeid-ulus; Kaidu page: Kaidu 'died shortly afterwards, late in 1301', 'Chapar fell out with Duwa by 1306'. Fix: vassal_end ulus-of-chagatai 1293 (c1, bookkeeping) + vassal_start chagatai-khanate 1294 + vassal_end chagatai-khanate (1301 at Kaidu's death or 1306 as now, say which); ask the chagatai-khanate author for the mirror.
- `/identity/start` (for the author): Founded 1271, but ulus-of-chagatai gives Semirechye and Bukhara to ogedeid-ulus in 1267 (/ledger/4 there): the land belongs to no ulus in 1267-1270. Evidence: Kaidu page: investiture at Talas 'August/September 1271'; the Baraq-Kaidu meeting 'around 1267' (Wassaf) or 'spring of 1269' (Rashid al-Din). Chagatai Khanate page: 'In 1267, Baraq accepted peace with Kaidu, and relinquished the territory east of Transoxania'. Fix: Decide with ulus-of-chagatai: either start this dossier at the 1267/1269 settlement (found event with the Kaidu page's alternative dates) or move the ulus-of-chagatai loss to 1271. Recorded as blocking on ulus-of-chagatai.

Gaps for a gap-filler:

- `/keyframe_review/2`: The Tarim Basin and Uighuria split between Kaidu and Duwa after the Yuan withdrawal (author flagged). Try https://en.wikipedia.org/wiki/Duwa

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Kaidu: confirmed ('invested as ruler of the previously dispersed Ulus of Ögedei at a kurultai at Talas in August/September 1271')
- `/ledger/3` https://en.wikipedia.org/wiki/Kaidu–Kublai_war: year not on page (capture of Almaliq undated); confidence lowered to 2
- `/ledger/6` https://en.wikipedia.org/wiki/Kaidu: confirmed ('capturing the old capital Karakorum in 1289'; 'When Kublai himself advanced on Kaidu, however, Kaidu retreated')
- `/ledger/11` https://en.wikipedia.org/wiki/Chagatai_Khanate: confirmed ('forcing him to surrender his territory to Duwa in 1306')
- `/ledger/5` https://en.wikipedia.org/wiki/Kaidu: confirmed at c2 (Beshbaliq 1286 on the Kaidu page, Yuan withdrawal 'From 1288/89' on the war page; note says so)

Area: infobox none, Cliopatria none; No Cliopatria row and no infobox area (the article used is the family page House of Ögedei).

## ulus-of-chagatai: fail

Findings:

- `/ledger/3, /ledger/7, /ledger/8` (applied by the reviewer): Counterpart yuan-dynasty for 1266 and 1289 events; the yuan-dynasty row starts in 1294. Evidence: polities.csv yuan-dynasty 1294..1374; mongol-empire dossier /ledger/80 (rename 1271) and /ledger/93 (dissolve 1293). Fix: Counterpart mongol-empire (done).
- `/ledger/5, /ledger/6` (applied by the reviewer): Counterpart ilkhanate for Baraq's 1270 invasion; the ilkhanate row starts in 1294. Evidence: polities.csv ilkhanate 1294..1343; ulus-of-hulegu (this batch) covers 1256-1293. Fix: Counterpart ulus-of-hulegu (done). The mirror contest is missing in ulus-of-hulegu (see there).
- `/wars/0../wars/4 belligerents` (applied by the reviewer): Belligerents yuan-dynasty, golden-horde and ilkhanate in wars of 1260-1293. Evidence: Those rows start in 1294. Fix: Replaced with mongol-empire, ulus-of-jochi, ulus-of-hulegu (done).
- `/ledger (1260-1262)` (for the author): No vassal_start 1260 / vassal_end 1262 with counterpart ariq-boke, the mirror of ariq-boke /ledger/2 and /ledger/4. Evidence: Alghu page: 'In 1260 Alghu was appointed as head of the ulus of the Chagatai Khanate by the Great Khan claimant Ariq Böke'; 'In 1262 he rebelled against Ariq Boke'. Fix: Add vassal_start 1260 (c2) and vassal_end 1262 (c3), counterpart ariq-boke, region as in ariq-boke /ledger/2, source the Alghu page.
- `/ledger (1271-1293)` (for the author): No vassal_start 1271 with counterpart ogedeid-ulus, the mirror of ogedeid-ulus /ledger/1 (Kaidu sets up the Chagatai khans), and no end at 1293. Evidence: ogedeid-ulus /ledger/1 cites the Kaidu page ('Kaidu also appointed Negübei as khan of Chagatai') and the Duwa page (1282). Fix: Add vassal_start 1271 counterpart ogedeid-ulus (c2) and vassal_end 1293 (c1, bookkeeping hand-over to chagatai-khanate).
- `/ledger (1263-1267), /keyframe_review/0` (for the author): ulus-of-jochi /ledger/8 (1263 loss of Otrar and Khwarazm to ulus-of-chagatai) and /ledger/10 (1267 regain) have no mirror here, and no keyframe here contains Otrar or Khwarazm, so the land is drawn by neither ulus in 1263-1266. Evidence: Golden Horde page: 'Alghu declared war on Berke, seizing Otrar and Khorazm' (undated); Alghu page: territories 'formerly under the control of the Blue Horde' after 1261, 'a new battle near Otrar'. Fix: Add gain 1263 (c1) from ulus-of-jochi and loss 1267 (c1) to ulus-of-jochi, region union(place Otrar 200 km, place Gurganj 400 km), and a keyframe 1263-1266 that includes them; or drop the pair from ulus-of-jochi. Both dossiers must agree.
- `/ledger/4` (for the author): 1267 loss to ogedeid-ulus, which exists only from 1271: Semirechye and Bukhara belong to no ulus 1267-1270. Evidence: ogedeid-ulus /identity/start 1271 (Kaidu page: Talas investiture 'August/September 1271'); Kaidu page dates the Baraq-Kaidu meeting 'around 1267' or 'spring of 1269'. Fix: Either keep Semirechye and Bukhara in this dossier until 1271 (loss in 1271, note the 1267 peace) or have ogedeid-ulus start at the 1267/1269 settlement; the two dossiers must agree within a year.
- `/identity/capitals/0` (for the author): Almaliq is the capital 1227-1293 but lies outside /keyframe_review/1 and /keyframe_review/2 from 1267 (Semirechye and Almaliq went to Kaidu; ogedeid-ulus gains Almaliq in 1277). Evidence: Keyframe corrections 1267-1293 are Transoxiana minus Bukhara (plus the Tarim from 1289). Fix: End Almaliq in 1266; name a Transoxiana or Tarim seat for 1267-1293 if a page gives one, else none.

Gaps for a gap-filler:

- `/ledger/9`: 1293 dissolve at c1 (bookkeeping hand-over to chagatai-khanate). Try https://en.wikipedia.org/wiki/Duwa
- `/keyframe_review/0`: Alghu's gains of Samarkand and Bukhara (undated) are not events (author flagged). Try https://en.wikipedia.org/wiki/Alghu

Spot checks:

- `/ledger/4` https://en.wikipedia.org/wiki/Chagatai_Khanate: confirmed ('In 1267, Baraq accepted peace with Kaidu, and relinquished the territory east of Transoxania')
- `/ledger/6` https://en.wikipedia.org/wiki/Chagatai_Khanate: confirmed ('defeated Baraq near Herat on 22 July 1270')
- `/ledger/1` https://en.wikipedia.org/wiki/Toluid_Civil_War: confirmed at c2 (Alghu 'lost his headquarters at Almalikh to Ariq Böke', undated; the Chagatai page places it after Alghu's 1263 flight)
- `/ledger/8` https://en.wikipedia.org/wiki/Kaidu: confirmed at c2 (Beshbaliq 1286, Tarim evacuated 'over the following years'; war page 'From 1288/89')

Area: infobox 3400000 (1310), Cliopatria none; No Cliopatria row; the author's gazetteer area 1.77 M km2 against the infobox 3.4 M km2 ('1310 or 1350 est.') is acknowledged in /keyframe_review/0/note. Successor row chagatai-khanate_1294 is 2,460,790 km2.

## ariq-boke: fix

Findings:

- `/wars/0/belligerents` (applied by the reviewer): golden-horde and ilkhanate in a 1260-1264 war; both rows start in 1294. Evidence: polities.csv; ulus-of-jochi and ulus-of-hulegu (this batch) cover those years. Fix: Replaced with ulus-of-jochi and ulus-of-hulegu (done).
- `/keyframe_review/1/note` (for the author): Says no page names the land Ariq held 1261-1264; the Toluid page does. Evidence: Toluid Civil War page: 'Ariq Böke retreated from Karakorum to a tributary of the Yenisei'; 'The only supply line still open to Ariq Böke was the Yenisei River valley in the northwest.' Fix: Quote these in the note and correction text (keyframe can stay; certainty can rise).
- `/ledger/3/note` (for the author): Quotes 'By 1261, most of Mongolia was now under the control of Kublai'; the page has no 'By 1261'. Evidence: Toluid page: 'In 1261, Kublai and Ariq Böke engaged in battle at Shimultai...' then 'Meanwhile, most of Mongolia was now under the control of Kublai.' Fix: Quote the page as written; the year stays (c2).

Spot checks:

- `/ledger/2` https://en.wikipedia.org/wiki/Alghu: confirmed ('In 1260 Alghu was appointed as head of the ulus of the Chagatai Khanate by the Great Khan claimant Ariq Böke')
- `/ledger/4` https://en.wikipedia.org/wiki/Alghu: confirmed ('In 1262 he rebelled against Ariq Boke')
- `/ledger/7` https://en.wikipedia.org/wiki/Ariq_Böke: confirmed (infobox reign '11 August 1259 – 21 August 1264'; 'Ariq Böke finally submitted to Kublai in 1264')
- `/ledger/3` https://en.wikipedia.org/wiki/Toluid_Civil_War: confirmed at c2 (Shimultai 1261; quote paraphrased, see fixes)

Area: infobox none, Cliopatria none; Rebel claimant; no infobox area, no Cliopatria row.

## ulus-of-jochi: fail

Findings:

- `/keyframe_review/2/correction` (for the author): Khwarezm (and the Urals) enter the shape in 1241 with no ledger event; /keyframe_review/0 and /keyframe_review/1 do not contain Khwarezm. Evidence: Ledger L0-L7 gain only Volga Bulgaria, the North Caucasus and the Pontic steppe; the Golden Horde page mentions Khorazm only when 'Alghu smashed the Golden Horde's lands in Khorazm' (undated) and does not say when it became Jochid. Fix: Add a dated gain of northern Khwarazm (Urgench) with a page (e.g. the Jochi page or the Siege of Gurganj page for 1221/1225), or put it in the 1225 found region; otherwise drop Khwarezm from /keyframe_review/2-3 and the 1263/1267 pair.
- `/ledger/6` (for the author): vassal_start of Rostov-Suzdal dated 1252 at confidence 3: the page's 1252 sentence is a later act, not the start of the vassalage. Evidence: Batu Khan page: 'Alexander was installed as the grand prince of Vladimir by Batu in 1252' and, earlier, 'Yaroslav was well received by Batu, who confirmed him as suzerain over the other Rus' princes'; Golden Horde page: 'All the senior princes of Rus', including Yaroslav II of Vladimir' 'acknowledged Batu's supremacy'; Yaroslav II page: 'In 1243, he was summoned by Batu Khan to his capital Sarai.' Fix: Year 1243, confidence 2, cite https://en.wikipedia.org/wiki/Yaroslav_II_of_Vladimir (add to sources). Note that the counterpart row principality-of-rostov-suzdal ends in 1240 and golden-horde uses principality-of-vladimir-suzdal from 1294: agree the slug with eu-16.
- `/identity/rulers` (for the author): Not contiguous: gaps 1225-1227, 1255-1257 and 1280-1291. Evidence: Golden Horde page: Jochi 'c. 1225 (first)'; 'After Batu died in 1256, his son Sartaq Khan was appointed', 'The infant Ulaghchi succeeded him'; 'Mengu-Timur was succeeded in 1281 by his brother Töde Möngke'; Talabuga 'succeeded him'; 'replaced with Toqta in 1291'. Fix: Add Jochi (1225-1227), Sartaq and Ulaghchi (1255/56-1257), Töde Möngke (1280/81-1287) and Talabuga (1287-1291), citing the Golden Horde page.
- `/keyframe_review/2/note` (for the author): Quotes Cliopatria's Golden Horde 1294 shape as 4.5 M km2. Evidence: shapes.csv golden-horde_1294 area_km2 4,933,986.5. Fix: Write 4.93 M km2.

Gaps for a gap-filler:

- `/ledger/8, /ledger/10`: Otrar and Khwarazm 1263-1267 at c1 (bridging years); must also be mirrored in ulus-of-chagatai. Try https://en.wikipedia.org/wiki/Mengu-Timur
- `/ledger/11`: Bulgaria's vassalage to Nogai dated by Ivaylo's death (1280), the vassalage itself undated. Try https://en.wikipedia.org/wiki/Second_Bulgarian_Empire
- `/ledger/12, /ledger/13, /ledger/14, /ledger/15`: 1293 hand-overs at c1 (bookkeeping, acceptable). Try https://en.wikipedia.org/wiki/Golden_Horde

Spot checks:

- `/ledger/1` https://en.wikipedia.org/wiki/Batu_Khan: confirmed ('crossed the Volga and invaded Volga Bulgaria in 1236')
- `/ledger/3` https://en.wikipedia.org/wiki/Cumania: confirmed ('the final blow came in 1241, when the Cuman confederacy ceased to exist as a political entity')
- `/ledger/5` https://en.wikipedia.org/wiki/Golden_Horde: confirmed ('Daniel personally visited Batu in 1245 and pledged allegiance to him')
- `/ledger/6` https://en.wikipedia.org/wiki/Batu_Khan: mis-dated (1252 is on the page, but as Alexander's installation; the pages put the princes' acknowledgment of Batu earlier, 1243 on the Yaroslav II page)

Area: infobox 6000000 (1310), Cliopatria 4933987; Cliopatria golden-horde_1294 (used as /keyframe_review/4); the author quotes it as 4.5 M km2.

## ulus-of-hulegu: thin

Findings:

- `/ledger (1270), /wars` (for the author): Baraq's 1270 invasion of Khorasan is missing: no contest pair and no war, although ulus-of-chagatai /ledger/5-6 record it with this dossier as counterpart. Evidence: Ilkhanate page: 'In 1270, Abaqa defeated an invasion by Ghiyas-ud-din Baraq of the Chagatai Khanate.' Chagatai Khanate page: 'defeated Baraq near Herat on 22 July 1270'. Fix: Add contest_start 1270 (region Khorasan) and contest_end 1270-07 (Herat 200 km), counterpart ulus-of-chagatai, and the war.
- `/keyframe_review/2/note` (for the author): Quotes Cliopatria's Ilkhanate 1294 shape as 3.77 M km2. Evidence: shapes.csv ilkhanate_1294 area_km2 3,941,078.1. Fix: Write 3.94 M km2 (ratio to the infobox 3.75 M km2 is 1.05).
- `/ledger/12` (for the author): Aleppo's recapture given month 10 at confidence 3; the page says only 'within a month' of 3 September. Evidence: Battle of Ain Jalut page: 'the Mamluks captured Damascus five days later after Ain Jalut, followed by Aleppo within a month'. Fix: Drop the month or keep it with a note that September is possible.

Gaps for a gap-filler:

- `/ledger/2`: Georgia's vassalage to Hulegu (c1); the mongol-empire dossier has it from 1243. Try https://en.wikipedia.org/wiki/David_VII_of_Georgia
- `/ledger/3`: Cilicia's submission (c1; Hethum I, 1247/1254). Try https://en.wikipedia.org/wiki/Armenian_Kingdom_of_Cilicia
- `/ledger/4`: Trebizond's vassalage (c1); Ilkhanate page: Rum and Trebizond 'became vassals of the Mongols' after Köse Dağ; the empire-of-trebizond dossier has no Mongol vassal events. Try https://en.wikipedia.org/wiki/Empire_of_Trebizond
- `/ledger/15../ledger/18`: 1293 vassal_end hand-overs at c1 (bookkeeping). Try https://en.wikipedia.org/wiki/Ilkhanate

Spot checks:

- `/ledger/5` https://en.wikipedia.org/wiki/Sultanate_of_Rum: confirmed ('In October 1256, Bayju defeated Kaykaus II near Aksaray and all of Anatolia became officially subject to Möngke Khan')
- `/ledger/8` https://en.wikipedia.org/wiki/Hulagu_Khan: confirmed ('On 10 February Baghdad surrendered. The Mongols swept into the city on 13 February.')
- `/ledger/10` https://en.wikipedia.org/wiki/Hulagu_Khan: confirmed ('seized Damascus on 1 March 1260')
- `/ledger/11` https://en.wikipedia.org/wiki/Battle_of_Ain_Jalut: confirmed ('on 3 September 1260'; 'the Mamluks captured Damascus five days later')
- `/ledger/1` https://en.wikipedia.org/wiki/Hulagu_Khan: confirmed ('in early 1256')

Area: infobox 3750000 (1310), Cliopatria 3941078; Cliopatria ilkhanate_1294 (basis of /keyframe_review/2); author quotes 3.77 M km2.

## amirate-of-qazaghan: thin

Findings:

- `/keyframe_review/0/to` (applied by the reviewer): No keyframe covered 1360 (KF0 ended 1359, KF1 starts 1361), so the state vanished in the year of the Moghul invasion although the ledger loses Transoxiana only in 1361. Evidence: Ledger /ledger/3 contest_start 1360, /ledger/5 loss 1361. Fix: to 1360 (done; note annotated).
- `/identity/rulers` (for the author): Gap 1360-1363 while /keyframe_review/1 keeps the state alive at Balkh in 1361-1362. Evidence: Chagatai page: Tughlugh 'defeated Amir Husayn in Afghanistan'; Timur page: Husayn and Timur 'became rivals and antagonists'. Fix: Extend Amir Husayn back to 1360/1361 or say the state lapsed and drop KF1.
- `/identity/capitals/0` (for the author): Qarshi 1346-1370 lies outside /keyframe_review/1 (Balkh only) in 1361-1362. Evidence: KF1 correction admin1 Balkh. Fix: End Qarshi in 1360 and resume in 1363, or no capital in 1361-1362.

Gaps for a gap-filler:

- `/keyframe_review/1, /keyframe_review/2`: Balkh enters in 1361 with no gain event; no page opened says when Husayn held Balkh. Try https://en.wikipedia.org/wiki/Qazaghan
- `/ledger/2`: End of Herat's tribute (c1, 1358). Try https://en.wikipedia.org/wiki/Kart_dynasty
- `/keyframe_review/0`: Fergana, Badakhshan, Balkh and Khorasan under Qazaghan (author flagged). Try https://en.wikipedia.org/wiki/Qazaghan

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Chagatai_Khanate: confirmed ('In 1346 a tribal chief, Amir Qazaghan, killed Qazan and set up Danishmendji as puppet khan')
- `/ledger/1` https://en.wikipedia.org/wiki/Chagatai_Khanate: confirmed ('Qazaghan made Herat a tributary in 1351')
- `/ledger/3` https://en.wikipedia.org/wiki/Chagatai_Khanate: confirmed ('In 1360, Tughlugh invaded Transoxania and conquered it')
- `/ledger/6` https://en.wikipedia.org/wiki/Chagatai_Khanate: confirmed ('Following Tughlugh's death in 1363, Timur and Amir Husayn took over Transoxiana')
- `/ledger/7` https://en.wikipedia.org/wiki/Timur: confirmed ('Coronation: 9 April 1370, Balkh')

Area: infobox none, Cliopatria none; No infobox area and no Cliopatria row (author says so in /keyframe_review/0/note).

## uzbek-khanate-of-abul-khayr: thin

Gaps for a gap-filler:

- `/ledger/3`: The steppe gain (the largest land move, about 1.9 M km2) is c1 at a bridging year 1440; the page gives only '1420s-1450s'. Try https://en.wikipedia.org/wiki/Shaybanids
- `/ledger/6`: Kerei and Janibek's secession (c1, undated) and the 1457 Oirat defeat (not in the ledger). Try https://en.wikipedia.org/wiki/Janibek_Khan

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Abu%27l-Khayr_Khan: confirmed ('Coronation: 1428'; 'After being released in 1428, Abu'l-Khayr began consolidating...' 'around Tyumen and the Tura River')
- `/ledger/2` https://en.wikipedia.org/wiki/Abu%27l-Khayr_Khan: confirmed ('In 1430–1431 ... occupying the regional capital Urganj'; 'retreated in the summer of 1431')
- `/ledger/4` https://en.wikipedia.org/wiki/Abu%27l-Khayr_Khan: confirmed ('Starting in 1446 Abu'l-Khayr and his forces invaded the Syr Darya region'; 'The town of Sighnaq became Abu'l-Khayr's new capital')
- `/ledger/7` https://en.wikipedia.org/wiki/Abu%27l-Khayr_Khan: confirmed ('died in 1468 (though some sources say 1469 or 1470)')

Area: infobox none, Cliopatria none; Infobox has no area (checked); no own Cliopatria row, the land sits in the khanate-of-sibir row (author flagged).

## turpan-khanate: pass

Gaps for a gap-filler:

- `/ledger/5`: End of the Ming-Turpan fighting over Hami (c1 1528) and who held Hami afterwards. Try https://en.wikipedia.org/wiki/Ming–Turpan_conflict

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Turpan_Khanate: confirmed ('It was founded by Ahmad Alaq in 1487 based in Turpan')
- `/ledger/2` https://en.wikipedia.org/wiki/Turpan_Khanate: confirmed ('Mansur conquered the kingdom and brought the region under his control in 1513')
- `/ledger/4` https://en.wikipedia.org/wiki/Mansur_Khan_(Moghul_Khan): confirmed ('In 1517, 1524, and 1528 battles broke out')
- `/ledger/6` https://en.wikipedia.org/wiki/Turpan_Khanate: confirmed ('in 1570, the Turpan Khanate was invaded by an army led by Abduraim Sultan' and 'Turpan came under the control of the Yarkand Khanate')

Area: infobox none, Cliopatria none; Infobox has no area (checked). Overlaps Cliopatria moghulistan_1492 (1.08 M km2, bbox reaches 92.7 E) and possibly eastern-chagatai-khanate (1492-1511), see problems.

## kara-del: fail

Findings:

- `/ledger/2` (for the author): 1404 is recorded only as the end of the Ming occupation, but the page and the event's own note describe the start of a Ming protectorate (the Hami Guard), which has no vassal_start; Kara Del is drawn independent 1404-1513. Evidence: Kara Del page: 'In 1404, Gunashiri's successor Engke Temiir accepted the establishment of a Ming guard'; 'From 1406, it was governed by Ming under the Hami Guard'. Mansur page (1513): the prince 'switched his allegiance from the Chinese Ming Emperor to Mansur Khan'. The author's own report asks for 'a vassal/protectorate counterpart of ming-dynasty from 1404'. Fix: Keep occupation_end 1404 and add vassal_start 1404 counterpart ming-dynasty (Hami 120 km, c3, Kara Del page) and vassal_end 1513 counterpart ming-dynasty (c3, Mansur page); interrupt it 1446 if the occupation stays.
- `/ledger (1430s-1455)` (for the author): Oirat suzerainty missing; the four-oirats dossier has vassal_start 'Kara Del (Hami)' 1445 (/ledger/3, c2) and vassal_end 1455 (/ledger/6, c1) with no mirror here. Evidence: Kara Del page: 'During the 1430s, Kara Del submitted to the Oirats'; infobox 'Conquered by Esen of the Northern Yuan' (undated). Fix: Add vassal_start counterpart four-oirats (1445 to match, c1, note the page's '1430s') and vassal_end 1455 (c1), or agree another year with the four-oirats dossier.
- `/identity/rulers` (for the author): Only Gunashiri 1389-1404; the page names his successor Engke Temür in 1404. Evidence: Kara Del page, as above. Fix: Add Engke Temür from 1404 (end year if a page gives it) or say the list is partial.

Gaps for a gap-filler:

- `/ledger/4`: End of the 1446 Ming occupation (c1, same-year bridge). Try https://en.wikipedia.org/wiki/Kara_Del

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Kara_Del: confirmed ('in 1389 the Buddhist Chagataid prince Gunashiri broke away from the Northern Yuan dynasty'; 'established himself in Qamil (Hami) by 1390')
- `/ledger/1` https://en.wikipedia.org/wiki/Kara_Del: confirmed at c2 ('The next year, the Ming dynasty occupied his territory and forced him to submit')
- `/ledger/3` https://en.wikipedia.org/wiki/Kara_Del: confirmed ('In 1446, disturbances broke out in Hami'; Ren Li 'occupied the city and deported 1,230 people')
- `/ledger/5` https://en.wikipedia.org/wiki/Kara_Del: confirmed ('Hami was conquered by Mansur Khan, the ruler of Moghulistan in 1513')
- `/ledger/2` https://en.wikipedia.org/wiki/Kara_Del: page says 1404 began a Ming guard (protectorate): wrong event type, see fixes

Area: infobox none, Cliopatria none; No infobox area; a 120 km circle at Hami, acknowledged in /keyframe_review/0.

## sufi-dynasty-of-khwarazm: fail

Findings:

- `/ledger (1372), /keyframe_review/0` (for the author): The 1372 peace in which Timur received Kath and Khiva is missing; the single keyframe keeps all of Khwarezm Sufi until 1388. Evidence: Sufi dynasty page: 'Husain Sufi's refusal to return southern Khwarezm caused Timur to go to war against him in 1372'; Yusuf Sufi 'concluded a peace with Timur in which Timur received Kath and Khiva'. Fix: Add loss 1372 (or 1373) counterpart timurid-empire, region Kath and Khiva (place Khiva ~60 km; Kath is not in the gazetteer: lon/lat 60.98, 41.54 or Beruniy), c3, and split the keyframe at 1373 with a correction for northern Khwarezm (Urgench) only.
- `/ledger/3` (for the author): A 'rename' with no new name stands in for a change of suzerain; the golden-horde dossier has vassal_start 'Sufi dynasty of Khwarazm' 1383 (/ledger/15, c3) and vassal_end 1388 (/ledger/17), with no mirror here. Evidence: Tokhtamysh page (1383): Tokhtamysh 'restored the Golden Horde's authority over the semi-autonomous Ṣūfī Dynasty in Khwarazm'. Fix: Replace with vassal_start 1383 counterpart golden-horde (region Khwarezm, c3, Tokhtamysh page) and add vassal_end 1388 counterpart golden-horde.
- `/ledger/2` (for the author): 1379 contest_end records no outcome, although the cited page calls it a subjugation and the Sufi infobox ends the dynasty in 1379. Evidence: Timur page: 'the subjugation of Khwarazm and Urgench in the Siege of Urgench (1379)'; Sufi page infobox 'Dissolution: 1379'; Sufi page: 'a general massacre followed and the city was burned'. Fix: Add vassal_start 1379 counterpart timurid-empire (c2) ending 1383 when Tokhtamysh restored Horde authority, or explain in the note why the land is drawn independent 1379-1383.
- `/identity/rulers` (for the author): Sulayman 1379-1388; the page's list has Balankhi (1380), Maing (1380), Sulayman (1380-1388). Evidence: Sufi dynasty page ruler list. Fix: Follow the page's list or note the difference.

Spot checks:

- `/ledger/1` https://en.wikipedia.org/wiki/Sufi_dynasty: confirmed (1372 war, Husain 'died during the siege'); the same passage records the cession of Kath and Khiva, missing from the ledger
- `/ledger/2` https://en.wikipedia.org/wiki/Timur: confirmed ('the subjugation of Khwarazm and Urgench in the Siege of Urgench (1379)'); outcome not recorded
- `/ledger/4` https://en.wikipedia.org/wiki/Sufi_dynasty: confirmed ('Suleiman Sufi allied with the khan of the Golden Horde, Tokhtamysh, and in 1387 revolted')
- `/ledger/5` https://en.wikipedia.org/wiki/Tokhtamysh: confirmed (Timur 'overthrew the Ṣūfī Dynasty of Khwarazm for its collusion with Tokhtamysh and razed to the ground its capital', 1388)

Area: infobox none, Cliopatria none; No infobox area; no Cliopatria row.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| ogedeid-ulus 1271 vassal_start ulus-of-chagatai | - | missing | ulus-of-chagatai (this batch) has no vassal_start 1271 with ogedeid-ulus; fix listed there. |
| ogedeid-ulus 1277 gain mongol-empire | - | missing | Almaliq; counterpart corrected from yuan-dynasty by the reviewer. mongol-empire (ia-02-a) has no 1277 loss of Almaliq (nor the 1266 occupation). |
| ogedeid-ulus 1289 gain mongol-empire | - | missing | Beshbalik and Turfan-Hami; mongol-empire has no 1286-1289 loss of Uighuria. |
| ogedeid-ulus 1289 occupation_start mongol-empire | - | missing | Karakorum 1289 (Kaidu page); mongol-empire has no occupation event. |
| ogedeid-ulus 1306 vassal_end ulus-of-chagatai | - | mismatch | Counterpart ended in 1293; chagatai-khanate has no vassal event with ogedeid-ulus. |
| ogedeid-ulus 1306 loss chagatai-khanate | chagatai-khanate 1306 merge | matched | Land disagrees: chagatai-khanate /ledger/1 merges Dzungaria; ogedeid-ulus hands over Semirechye, Almaliq, Bukhara, Beshbalik and Turfan-Hami. |
| ulus-of-chagatai 1263 occupation_start ariq-boke | ariq-boke 1263 occupation_start | matched | Almaliq; end 1264 matched too. |
| ulus-of-chagatai 1267 loss ogedeid-ulus | ogedeid-ulus 1271 found | mismatch | 4 years apart: Semirechye and Bukhara belong to no ulus 1267-1270 (blocking fix on ulus-of-chagatai). |
| ulus-of-chagatai 1289 gain mongol-empire | - | missing | Tarim Basin; counterpart corrected from yuan-dynasty; mongol-empire has no Tarim loss (contest 1266-1289 also absent there). |
| ulus-of-chagatai 1270 contest_start ulus-of-hulegu | - | missing | Baraq's invasion; counterpart corrected from ilkhanate; ulus-of-hulegu lacks the pair (fix listed there). |
| ariq-boke 1260 vassal_start ulus-of-chagatai | - | missing | Alghu appointed by Ariq; end 1262 also missing; blocking fix on ulus-of-chagatai. |
| ariq-boke 1261 loss mongol-empire | - | missing | mongol-empire records only contest_start/contest_end 1260/1264 with the string 'Ariq Böke' (L73, L77); no gain of Karakorum/Mongolia in 1260-61 and the string should become the slug ariq-boke. |
| ariq-boke 1260 contest_start mongol-empire | mongol-empire 1260 contest_start | matched | mongol-empire uses the string 'Ariq Böke' as counterpart; end 1264 matched. |
| ulus-of-jochi 1236 gain volga-bulgaria | mongol-empire 1236 gain | exception | No volga-bulgaria dossier yet; mongol-empire /ledger/25 gains the same land the same year (double gain, overlap flagged by the author). |
| ulus-of-jochi 1240 gain alania | alania 1240 dissolve | mismatch | alania dissolves to mongol-empire (counterpart), which also gains it (/ledger/41): same land gained twice; overlap flagged by the author, orchestrator to decide. |
| ulus-of-jochi 1241 gain cuman-kipchak-confederation | cuman-kipchak-confederation 1241 dissolve | mismatch | cuman-kipchak-confederation dissolves to mongol-empire, which also gains it (/ledger/52): same overlap. |
| ulus-of-jochi 1245 vassal_start principality-of-galicia-volhynia | - | exception | No dossier (eu-16 not run); mongol-empire has vassal_start 1240. The row ends 1240 in polities.csv; golden-horde continues with galicia-volhynia from 1294. |
| ulus-of-jochi 1252 vassal_start principality-of-rostov-suzdal | - | exception | No dossier (eu-16 not run); mis-dated (should be 1243); mongol-empire has 1238; row ends 1240, golden-horde continues with principality-of-vladimir-suzdal from 1294. |
| ulus-of-jochi 1263 loss ulus-of-chagatai | - | missing | Otrar and Khwarazm; no gain in ulus-of-chagatai (blocking fix there). |
| ulus-of-jochi 1267 gain ulus-of-chagatai | - | missing | Otrar and Khwarazm back; no loss in ulus-of-chagatai. |
| ulus-of-jochi 1280 vassal_start second-bulgarian-empire | - | exception | No dossier yet (eu group not run). |
| ulus-of-jochi 1293 dissolve golden-horde | golden-horde 1294 found | mismatch | golden-horde found names mongol-empire as counterpart and predecessor; it should name ulus-of-jochi. Vassal hand-overs 1293/1294 match (golden-horde L1-L3). |
| ulus-of-hulegu 1256 gain nizari-ismaili-state | - | exception | Listed in counterparts_needing_dossiers; mongol-empire /ledger/64 also gains it (1257, string 'Nizari Ismaili state'). |
| ulus-of-hulegu 1256 vassal_start kingdom-of-georgia | - | exception | No dossier (eu-19 not run); mongol-empire has vassal_start 1243. |
| ulus-of-hulegu 1256 vassal_start armenian-kingdom-of-cilicia | - | exception | No dossier (me-09 not run). |
| ulus-of-hulegu 1256 vassal_start empire-of-trebizond | - | missing | empire-of-trebizond dossier exists and has no Mongol/Ilkhanid vassal events (eu-05). |
| ulus-of-hulegu 1256 vassal_start sultanate-of-rum | - | exception | No dossier (me-09 not run); mongol-empire has vassal_start 1243 and a 1250 gain in Anatolia. |
| ulus-of-hulegu 1258 gain abbasid-caliphate | mongol-empire 1258 gain | exception | No abbasid-caliphate dossier (me-08 not run); mongol-empire /ledger/65 gains the same land (overlap flagged). |
| ulus-of-hulegu 1260 occupation_start ayyubid-sultanate | mongol-empire 1260 occupation_start | exception | ayyubid-sultanate listed in counterparts_needing_dossiers (row ends 1249 in polities.csv); mongol-empire /ledger/75-76 duplicates Aleppo and Damascus. |
| ulus-of-hulegu 1262 contest_start ulus-of-jochi | ulus-of-jochi 1262 contest_start | matched | Berke-Hulagu war; ends 1265 matched. |
| ulus-of-hulegu 1293 dissolve ilkhanate | ilkhanate 1294 found | mismatch | ilkhanate found names mongol-empire; it should name ulus-of-hulegu. |
| amirate-of-qazaghan 1346 found chagatai-khanate | chagatai-khanate 1346 split | matched |  |
| amirate-of-qazaghan 1351 vassal_start kartids | - | exception | No kartids dossier (me-09 not run). |
| amirate-of-qazaghan 1361 loss chagatai-khanate | chagatai-khanate 1361 gain | matched | Contest 1360-1361 matched too. |
| amirate-of-qazaghan 1363 gain chagatai-khanate | chagatai-khanate 1363 loss | matched |  |
| amirate-of-qazaghan 1370 dissolve timurid-empire | timurid-empire 1370 found | mismatch | timurid-empire predecessors list only chagatai-khanate; add amirate-of-qazaghan. |
| uzbek-khanate-of-abul-khayr 1428 found golden-horde | - | missing | golden-horde has no 1428 split for the eastern wing. |
| uzbek-khanate-of-abul-khayr 1430 occupation_start timurid-empire | - | missing | Urganj 1430-1431; timurid-empire has no occupation event. |
| uzbek-khanate-of-abul-khayr 1446 gain timurid-empire | - | missing | Syr Darya and Sighnaq; timurid-empire has no loss. |
| uzbek-khanate-of-abul-khayr 1468 loss kazakh-khanate | - | exception | No kazakh-khanate dossier (ia-03 not run). |
| turpan-khanate 1487 found moghulistan | - | missing | moghulistan has no 1487 split (its /ledger/3 is a 1492 loss to eastern-chagatai-khanate). |
| turpan-khanate 1513 gain kara-del | kara-del 1513 loss | matched |  |
| turpan-khanate 1570 dissolve eastern-moghulistan | - | exception | No eastern-moghulistan dossier yet. |
| kara-del 1389 found northern-yuan | - | missing | northern-yuan (starts 1368/9) has no 1389 split or loss at Hami. |
| kara-del 1391 occupation_start ming-dynasty | - | exception | No ming-dynasty dossier (ea group not run); also 1404 and 1446. |
| four-oirats 1445 vassal_start Kara Del (Hami) | - | missing | kara-del has no Oirat vassal events (blocking fix there); four-oirats should use the slug kara-del. |
| golden-horde 1383 vassal_start Sufi dynasty of Khwarazm | sufi-dynasty-of-khwarazm 1383 rename | mismatch | Sufi side has a placeholder rename; needs vassal_start/vassal_end golden-horde 1383/1388 (blocking fix there); golden-horde should use the slug. |
| sufi-dynasty-of-khwarazm 1388 dissolve timurid-empire | timurid-empire 1402 gain | mismatch | timurid-empire /ledger/11 gains Khwarazm in 1402 (c1); the pages give 1388 (Tokhtamysh page) and 1379/1372 (Timur, Sufi pages). |
| sufi-dynasty-of-khwarazm 1361 found golden-horde | - | missing | golden-horde has no 1361 loss of Khwarazm. |

## Problems for the orchestrator

- Reviewer edits applied and re-validated (0 errors, 0 warnings): ogedeid-ulus /ledger/3 confidence 3->2, counterparts of /ledger/2-7 yuan-dynasty->mongol-empire, /wars/0-1 belligerents; ulus-of-chagatai counterparts of /ledger/3,7,8 yuan-dynasty->mongol-empire and /ledger/5,6 ilkhanate->ulus-of-hulegu, /wars/0-4 belligerents; ariq-boke /wars/0 belligerents; amirate-of-qazaghan /keyframe_review/0/to 1359->1360. Each edited dossier's notes carry a '[Reviewer ia-02-x, 2026-10-19]' line.
- Verdict 'fix' (ogedeid-ulus, ariq-boke) means the blocking findings were applied by the reviewer; their remaining applied:false findings are non-blocking and should ride with the next repair of ulus-of-chagatai. Verdict 'thin' dossiers (ulus-of-hulegu, amirate-of-qazaghan, uzbek-khanate-of-abul-khayr) also carry applied:false non-blocking findings.
- The author's report asks yuan-dynasty for mirrored events of 1260-1289 (Almaliq, Beshbalik, Tarim, Ariq Böke): before 1294 those belong in mongol-empire (ia-02-a), which carries Kublai's state to 1293; only the 1294-1306 events go to yuan-dynasty.
- Overlap not settled: mongol-empire (ia-02-a) records as its own the gains that ulus-of-jochi (Volga Bulgaria 1236, Alania 1240, Cumania 1241, Rus' vassals) and ulus-of-hulegu (Nizari 1256/57, Baghdad 1258, Aleppo and Damascus 1260) also record, so the same land is gained twice in the same year; alania and cuman-kipchak-confederation dissolve to mongol-empire. The orchestrator must decide which dossier owns these events (the author flagged it).
- Successor dossiers golden-horde, ilkhanate and chagatai-khanate start in 1294 with counterpart and predecessor mongol-empire; they should name ulus-of-jochi, ulus-of-hulegu and ulus-of-chagatai. timurid-empire should name amirate-of-qazaghan as predecessor and move its Khwarazm gain from 1402 (c1) to 1388 (or 1372 for Kath and Khiva).
- Strings instead of slugs in other groups' dossiers: mongol-empire 'Ariq Böke' (now ariq-boke), golden-horde 'Sufi dynasty of Khwarazm' (now sufi-dynasty-of-khwarazm), four-oirats 'Kara Del (Hami)' (now kara-del), timurid-empire 'Khwarazm (Urgench, Sufi dynasty)'.
- turpan-khanate (1487-1570) may duplicate Cliopatria's eastern-chagatai-khanate row (1492-1511, Wikipedia title Moghulistan, bbox 71-81 E): if that row is Ahmad Alaq's eastern khanate, the two should be one state; the author's notes mention only the moghulistan and eastern-moghulistan rows.
- Counterpart rows that end before the events naming them: principality-of-rostov-suzdal and principality-of-galicia-volhynia (rows end 1240) used by ulus-of-jochi to 1293; ayyubid-sultanate (row ends 1249) used for 1260. eu-16 and me-09 should agree the slugs.
- All pages opened with WebFetch loaded; WebFetch answers through a summarising model, so quoted sentences are as it returned them.
