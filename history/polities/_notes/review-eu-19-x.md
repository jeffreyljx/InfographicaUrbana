# Review of batch eu-19-x (Caucasus additions)

Reviewer: Phase B adversarial reviewer, 2026-10-31 (run 2026-11-01). Machine copy: history/notes/phase-b/reviews/eu-19-x.json.

Mechanical: all 13 dossiers validate (0 errors); warnings only on kingdom-of-abkhazia (war 735-736 outside the life, principality-of-abasgia unknown slug, seven Georgia shapes owned by eu-19-b without a verdict, expected) and kingdom-of-kakheti-hereti (kingdom-of-hereti unknown slug). No unresolved region names. No fabricated or mis-dated confidence-3 event was found in 55 spot checks; every page opened says what the note claims, with the year.

Verdict rule used: pass = could not break; fix = only reviewer-applied fixes; thin = valid and honest but events, mirrors or shapes are missing (gap-filler list); fail = blocking finding left for the author. Findings marked applied were made by the reviewer in the dossier, re-validated and read back.

## emirate-of-tbilisi: thin

Area: infobox None (None), shape None, ratio None, acknowledged True.

Findings:
- `/ledger/1/region` (for the author): The 853 contest is over Kartli (central Iberia) but no keyframe ever gives the emirate Kartli: the only shape is Tbilisi + 30 km for 736-1122. Evidence: Kingdom of the Iberians page: 'In 853, now supporting Bugha al-Kabir, Bagrat regained central Iberia', i.e. central Iberia was the Arabs' before 853; the Emirate page: the emirate ruled 'parts of today's eastern Georgia'. Fix: Either add a keyframe for the emirate's Kartli holding before 853 (with a page that dates it) or narrow the contest region to the Tbilisi circle and say so in the note.

Thin (for a gap-filler):
- `/keyframe_review/0`: One 30 km circle stands for 386 years; nothing dates the emirate's wider holdings in Kartli before 853 or its shrinking to the city. Try: https://en.wikipedia.org/wiki/Arab_rule_in_Georgia
- `/ledger/2`: contest_end 854 is a confidence-1 bridge ('for a brief time'). Try: https://en.wikipedia.org/wiki/Bagrat_I_of_Iberia
- `/ledger`: No vassal events for caliphal (Umayyad/Abbasid) or Seljuk (from 1068) overlordship, nor the Tashir-Dzoraget suzerainty the Tashir page mentions; the 1032 capture of Emir Jafar and the two-year siege are undated. Try: https://en.wikipedia.org/wiki/Bagrat_IV_of_Georgia

Spot checks: /ledger/0 confirmed (infobox 'Established: 736'; text 735 for Marwan II); /ledger/1 confirmed; /ledger/3 confirmed (emirs table: 'Fadlun of Ganja 1068-1080 ... appointed by Alp Arslan'); /ledger/4 confirmed ('took the city in February', 1122; capital moved from Kutaisi)

## kingdom-of-abkhazia: thin

Area: infobox None (None), shape 86640, ratio None, acknowledged True.

Findings:
- `/ledger/3/counterpart` (applied by reviewer): The 904 Kartli gain had counterpart 'nobody' with the claim that the page is silent on who held Kartli. Evidence: Kingdom of the Iberians page (already in this dossier's sources): 'in 904 Adarnase was dispossessed by Constantine III'. Fix: Counterpart kingdom-of-the-iberians; note extended. Done by the reviewer; validator passes.
- `/keyframe_review/0` (for the author): georgia_724 (724-777) has verdict ok although the note says the years belong to the predecessor Principality of Abasgia; as written the renderer draws this kingdom 54 years before its 778 start. Evidence: Dossier life 778-1008; shapes.csv georgia_724 724-777; K0 note: 'The years 724-777 belong to the predecessor Principality of Abasgia'. Fix: Verdict wrong with a correction naming the years it belongs to (principality-of-abasgia, 724-777), or leave the shape to that dossier and to eu-19-b's Georgia split; move war /wars/0 (735-736, outside the life, validator warning) to principality-of-abasgia when it is written.
- `/keyframe_review/5` (for the author): georgia_888 (888-910) is corrected to the 886 outline without Kartli for all of 888-910, while /ledger/3 gains Kartli in 904 and the new keyframe /keyframe_review/10 (904-979) draws it: the two overlap for 904-910 and disagree. Evidence: Constantine III page: 'In 904 he had finally annexed a significant portion of Kartli'. Fix: State in the georgia_888 correction/note that it applies to 888-903 only and that kingdom-of-abkhazia_904 governs from 904.

Thin (for a gap-filler):
- `/ledger`: bagratid-armenia /ledger/5 (903 gain of Abkhazian districts, Klarjeti and Ardahan, counterpart kingdom-of-abkhazia) and /ledger/11 (c. 911 loss back to kingdom-of-abkhazia) have no mirror here. Try: https://en.wikipedia.org/wiki/Smbat_I_of_Armenia
- `/keyframe_review/3`: georgia_875 (+19 percent) and georgia_886 stand unverified (page budget); George I's eastward expansion is undated. Try: https://en.wikipedia.org/wiki/George_I_of_Abkhazia
- `/ledger/5`: Kakheti vassal_start 935 and vassal_end 960 are confidence 1 (Principality of Kakheti page: Padla II assisted George II in 925; Ujarma handed over 959; Kakheti 'ultimately still managed to reclaim its lands'). Try: https://en.wikipedia.org/wiki/George_II_of_Abkhazia
- `/ledger/7`: Tao-Klarjeti vassal_end c. 973 is a confidence-1 bridge ('almost sixty years'). Try: https://en.wikipedia.org/wiki/Tao-Klarjeti

Spot checks: /ledger/2 confirmed (infobox 'Anacopia (778-786) Kutaisi (786-1008)'); /ledger/3 confirmed ('In 904 he had finally annexed a significant portion of Kartli'); counterpart corrected from the Kingdom of the Iberians page; /ledger/8 confirmed ('In 978, the Bagratid prince Bagrat ... occupied the Abkhazian throne'); /ledger/9 confirmed (infobox 'Unification of the Georgian Kingdom: 1008'); /ledger/0 confirmed ('Towards circa 778, Leon II won his full independence')

## kingdom-of-kakheti-hereti: thin

Area: infobox None (None), shape None, ratio None, acknowledged True.

Findings:
- `/ledger` (for the author): The dossier records no Abkhazian overlordship although its own war /wars/1 'Abkhazian overlordship over Kakheti' (925-960, zone Kakheti) and kingdom-of-abkhazia /ledger/5-6 (vassal_start 935, vassal_end 960, counterpart this slug) say it existed: the two dossiers of the same batch disagree. Evidence: kingdom-of-abkhazia /ledger/5 and /ledger/6; this dossier /wars/1. Fix: Add vassal_start 935 and vassal_end 960 with counterpart kingdom-of-abkhazia (confidence 1, same pages), or drop the Abkhazia events; the two must agree.
- `/notes` (for the author): The notes say the pages support Kakheti only for Bagrat III's 1010 conquest; the Principality of Kakheti page says 'In 1010, Bagrat again invaded Kakheti-Hereti and captivated Kvirike III' and its infobox puts the union of Kakheti-Hereti in 1010, while the Kingdom page has 'Incorporation of Hereti: 1010s' and Kvirike III taking Hereti on becoming king in 1014. Evidence: Principality_of_Kakheti and Kingdom_of_Kakheti-Hereti pages, read 2026-10-31. Fix: Say in the notes that the two pages disagree on Hereti in 1010 (kingdom-of-georgia /ledger/1 follows the Principality page); keep the 1014 Hereti gain at confidence 2.

Thin (for a gap-filler):
- `/ledger`: Seljuk submission: Aghsartan I's submission to Alp Arslan in 1068 (war /wars/5, 1068-1084) has no vassal_start/vassal_end with great-seljuk-empire. Try: https://en.wikipedia.org/wiki/Aghsartan_I_of_Kakheti
- `/ledger`: The Kiurikid (Tashir-Dzoraget) branch on the Kakheti throne from 1039 (Tashir page: a branch ruled there 1029-1105) is not recorded as a rename. Try: https://en.wikipedia.org/wiki/Gagik_of_Kakheti
- `/keyframe_review/0`: No shape for Grigol's hold on Shida Kartli to the Ksani or for Hereti strongholds (Ortchobi) taken in 905. Try: https://en.wikipedia.org/wiki/Grigol_of_Kakheti

Spot checks: /ledger/0 confirmed ('Grigol separated from the Principality of Iberia after the death of Juansher in 787'; 'Kakhet-Kukhet-Gardabani'); /ledger/1 confirmed ('In 1010, Bagrat again invaded Kakheti-Hereti and captivated Kvirike III'), but see the Hereti note; /ledger/2 confirmed ('Following Bagrat's death in 1014' Kvirike III 'was able to recover the crown'); /ledger/5 confirmed ('In 1104, Aghsartan was arrested by his vassals, the princes Areshiani of Hereti'; David IV page agrees)

## kingdom-of-syunik: thin

Area: infobox 5500 (1100), shape 4050, ratio 0.74, acknowledged True.

Thin (for a gap-filler):
- `/ledger`: The vassal relation to the Bagratids is not mirrored: bagratid-armenia /ledger/1 (885 vassal_start), /16 (987 vassal_end), /17 (988 vassal_start), /23 (1045 vassal_end) all name kingdom-of-syunik; the Syunik page says the kingdom 'was a vassal of the medieval Bagratids'. Try: https://en.wikipedia.org/wiki/Kingdom_of_Syunik
- `/keyframe_review/1`: The single 989-1170 shape ignores the page's dated losses: 'In 1103, the Seleucids captured and destroyed Capan', 'In 1152, the Turks succeeded in conquering the fortress of Slorou ... in 1157, the fortress of Mali fell', 'Between 1166 and 1169, they captured Grkam, Geghi, and Kakavaberd'. These are on the page the author opened. Try: https://en.wikipedia.org/wiki/Kingdom_of_Syunik
- `/identity/capitals/0`: Capital Kapan 987-1170, but the page has Kapan destroyed in 1103 and King Hasan in Baghk in 1170: a capital_move is missing. Try: https://en.wikipedia.org/wiki/Baghaberd
- `/ledger/1`: 989 loss of Vayots Dzor is dated only to Gagik I's reign (989-1020), confidence 1. Try: https://en.wikipedia.org/wiki/Gagik_I_of_Armenia

Spot checks: /ledger/0 confirmed (infobox 'Established: 987'; 'proclaimed a separate kingdom from the Bagratids'); /ledger/1 confirmed ('King Gagik I (989-1020) took some regions (Jahuk and part of the Pot), including Vayots Dzor, from his vassal'); /ledger/2 confirmed ('In 1170, they besieged Baghdad, the last stronghold'; 'the other fortresses were forced to submit to the Yeltkuz atabek'); the page is garbled

## kingdom-of-tashir-dzoraget: thin

Area: infobox None (None), shape None, ratio None, acknowledged True.

Thin (for a gap-filler):
- `/ledger`: Vassalage to the Bagratids is not mirrored: bagratid-armenia /ledger/15 (979 vassal_start) and /22 (1045 vassal_end) name this slug; the Tashir page says it was formed 'as a vassal kingdom of the Bagratid Kingdom of Armenia' and that after 1045 Kiurike II 'became an independent ruler'. Try: https://en.wikipedia.org/wiki/Kingdom_of_Tashir-Dzoraget
- `/ledger`: 'Kiurke II became a vassal of the Seljuk Empire' and David I Anhoghin's conquests from Tbilisi and Ganja are undated; a page on Kiurike II or David Anhoghin may date them. Try: https://en.wikipedia.org/wiki/Lori_Berd

Spot checks: /ledger/0 confirmed ('In 979 King Smbat II of Armenia granted the province of Tashir to his brother Kiurike with the title of king'); /ledger/1 confirmed ('moved the capital from Matsnaberd to Lori in 1064'; infobox Lori 1065-1118); /ledger/2 confirmed ('Still in 1118, the Armenian towns of Lori and Agarak were captured by David IV'); /ledger/3 confirmed ('ruled until 1118 when Tashir-Dzoraget was annexed to the Kingdom of Georgia')

## kingdom-of-kars: thin

Area: infobox None (None), shape None, ratio None, acknowledged True.

Thin (for a gap-filler):
- `/ledger`: Vassalage to the Bagratids is not mirrored: bagratid-armenia /ledger/14 (963 vassal_start) and /24 (1045 vassal_end) name kingdom-of-kars. Try: https://en.wikipedia.org/wiki/Kingdom_of_Kars
- `/ledger`: The 1064 homage to the Seljuks is on the page ('In 1064 ... paid homage to the victorious Turks so that they would not lay siege to his city') but is only a war entry; a vassal_start 1064 with great-seljuk-empire is missing. Try: https://en.wikipedia.org/wiki/Kingdom_of_Kars

Spot checks: /ledger/0 confirmed ('formed in the year 963 by the son of Abas I of Armenia, Mushegh Bagratuni'); /ledger/1 confirmed ('In 1065 Gagik-Abas ceded his kingdom to the Byzantine Empire'; infobox span 963-1064); /ledger/2 confirmed

## republic-of-artsakh: thin

Area: infobox 11458 (1995), shape 4050, ratio 0.35, acknowledged True.

Findings:
- `/ledger/5/confidence` (applied by reviewer): Confidence 3 on a region (Shusha + the whole Khojavend district) the page does not name beyond Shusha. Evidence: Second Nagorno-Karabakh War page names Shusha ('On 8 November 2020, Azerbaijani forces seized Shusha') and '72% of the disputed territory'; it does not say who held Martuni/Khojavend after the ceasefire. Fix: Lowered to 2 with a note. Done by the reviewer; validator passes.
- `/ledger` (for the author): republic-of-armenia /ledger/9-10 (1994 vassal_start) and /15, /20 (2020 and 2023 vassal_end) name this slug as Armenia's client; this dossier has no vassal events. Evidence: Republic of Artsakh page: 'Artsakh was heavily dependent on Armenia'; Armenia 'became the main financial and military supporter'. Fix: Add vassal_start 1994 and vassal_end 2023 (counterpart republic-of-armenia, confidence 2), or ask eu-19 to drop the Armenia events; the two must agree.
- `/ledger/2` (for the author): Event types disagree with republic-of-azerbaijan: this ledger has gain 1994 / loss 2020 / loss 2023, Azerbaijan has occupation_start 1994 / occupation_end 2020 / occupation_end 2023 with counterpart republic-of-artsakh; its contest events name republic-of-armenia, not this slug. Evidence: republic-of-azerbaijan /ledger/1, /8, /9, /10, /11, /15, /16, /20. Fix: Orchestrator to settle one convention for de facto states (the Abkhazia and South Ossetia dossiers use gain/contest too); then align both ledgers.

Thin (for a gap-filler):
- `/keyframe_review/0`: 1991-1994 control line not drawn (Shahumyan, Getashen, the Mardakert losses of June 1992, Shusha 9 May 1992); only the contest zone covers it. Try: https://en.wikipedia.org/wiki/Operation_Goranboy
- `/keyframe_review/2`: The Tərtər rayon used for the 2020-2023 rump includes Tartar town, Azerbaijani-held throughout, and the pages opened do not say whether the Martuni area (inside the Xocavənd rayon drawn as lost in 2020) stayed in the rump; a page on the November 2020 ceasefire line would settle the outline. Try: https://en.wikipedia.org/wiki/2020_Nagorno-Karabakh_ceasefire_agreement

Spot checks: /ledger/0 confirmed (infobox 'Proclamation 2 September 1991'; text '6 January 1992'); /ledger/3 confirmed ('a ceasefire that would go into effect at 12:01 AM on 12 May'); /ledger/5 confirmed for Shusha 8 November 2020; region broader than the page (confidence lowered); /ledger/6 confirmed ('from 10 November 2020, 00:00 Moscow time'); /ledger/7 confirmed ('On 19 September, Azerbaijan launched a military offensive'); /ledger/8 confirmed (decree of 28 September: institutions dissolved by 1 January 2024)

## principality-of-armenia: thin

Area: infobox None (None), shape 73677, ratio None, acknowledged True.

Findings:
- `/identity/capitals/0` (for the author): Capital Dvin for 638-884, but /ledger/3 has the Qaysid emirs taking Dvin c. 780 and the ostikan moving to Bardha'a. Evidence: Arminiya page: 'Around 780, Dvin was taken by the Qaysid emirs, causing the ostikan to move his seat to Bardha'a in Arran.' Fix: End the Dvin capital at 780 (or say in its note that the presiding princes had no fixed seat after 780).
- `/ledger/3/counterpart` (for the author): Counterpart 'Qaysid emirs' is a label, not a slug. Evidence: Author's report suggests qaysid-emirs; Wikipedia's article is 'Qaysites'. Fix: Use one slug (e.g. qaysites) here and in counterparts_needing_dossiers.

Thin (for a gap-filler):
- `/ledger`: The Arab overlordship the page dates is not ledgered: 'Rshtuni voluntarily agreed to submit to Muslim overlordship' (653) and the return to Byzantium in 657; rashidun-caliphate /ledger/41, /60, /61, /66 (646 contest, 653 vassal_start, 657 vassal_end, counterpart 'Armenian princes (Theodore Rshtuni)') and byzantine-empire 657 need mirrors here. Try: https://en.wikipedia.org/wiki/Principality_of_Armenia
- `/ledger/1`: 644 loss of the north-west is confidence 1 (Cliopatria step; the page has 645/646 for the conquest). Try: https://en.wikipedia.org/wiki/Muslim_conquest_of_Armenia
- `/keyframe_review/2`: 647-884 reuses the 644 outline for 238 years; no page gives a frontier (Arminiya page: four regions). Try: https://en.wikipedia.org/wiki/Muslim_conquest_of_Armenia

Spot checks: /ledger/0 confirmed (lands on Arminiya; 'Theodore Rshtuni, 638-645'); /ledger/2 confirmed (705: 'grouped into one vast province called al-Arminiya'); /ledger/3 confirmed ('Around 780, Dvin was taken by the Qaysid emirs'); /ledger/4 confirmed (884 'King of the Armenians'; recognised 885 and 886)

## emirate-of-derbent: thin

Area: infobox None (None), shape None, ratio None, acknowledged True.

Findings:
- `/ledger/1/month` (applied by reviewer): The 1075 loss carried month 8, which the page does not give; the rulers table has Maymun II b. Mansur II reigning '20 August 1075 - December 1075', so the annexation cannot be in August. Evidence: Emirate of Derbent page: 'The Hashimid dynasty fell from power in 1075 when Fariburz I annexed Derbent'; rulers table. Fix: Month removed, note extended. Done by the reviewer; validator passes.

Thin (for a gap-filler):
- `/ledger/2`: The restoration is a confidence-1 bridge at 1130; the page says 'soon another dynasty emerged following Saljuq intervention' (the Aghlabids, Aghlab b. Ali appointed by Savtegin), i.e. well before 1130, so 1076-1129 drawn as Shirvan's may be wrong. Try: https://en.wikipedia.org/wiki/Shirvanshah
- `/ledger`: The 1173 Shirvan-Georgian defeat of Emir Bek-Bars (war /wars/2) and the infobox's alternative end 'c. 1173' are not resolved in the ledger. Try: https://en.wikipedia.org/wiki/Akhsitan_I

Spot checks: /ledger/0 confirmed ('formed in 869 by Hashim b. Suraqa'; infobox c. 869); /ledger/1 year confirmed; month 8 not on page (fixed); /ledger/2 bridge: the page has 'around 1130-1150, the emirate was ruled by another dynasty'; /ledger/3 confirmed ('absorbed into Shirvanshah state after 1225'; Rashid c. 1222-c. 1225)

## kingdom-of-artsakh: thin

Area: infobox None (None), shape None, ratio None, acknowledged True.

Findings:
- `/ledger/2` (for the author): The 1261 gain of Dizak (Xocavənd rayon) adds land the only keyframe (Karabakh, 1000-1603) already draws from 1000: the event has no trace in the keyframes. Evidence: Keyframe kingdom-of-artsakh_1000 region Karabakh; ledger /2 region admin1 Xocavənd; Kingdom of Artsakh infobox 'Acquisition of Dizak and Gardman: 1261'. Fix: Split the keyframe at 1261 (Karabakh minus Dizak before) or drop the gain and say Dizak is drawn throughout.

Thin (for a gap-filler):
- `/ledger/2`: 1261 Dizak and Gardman acquisition is confidence 1 with counterpart nobody (infobox only). Try: https://en.wikipedia.org/wiki/Dizak
- `/ledger`: No overlord events: vassal of the Bagratid kingdom around 1000 (page), the Zakarid/Georgian and Mongol/Ilkhanid overlordship; the 1182 subdivision is undated detail. Try: https://en.wikipedia.org/wiki/Hasan-Jalal_Dawla
- `/keyframe_review/0`: One Karabakh shape for 603 years; Gardman and the Syunik/Ayrarat cantons the page names are not drawn. Try: https://en.wikipedia.org/wiki/Kingdom_of_Artsakh

Spot checks: /ledger/0 confirmed (infobox 'Established: 1000'); /ledger/1 confirmed ('began ruling much of Khachen and Artsakh in 1214'); /ledger/3 confirmed ('Assassination of Hasan Jalal, last king of Artsakh: 1261'; 'by the Ilkhanid ruler Arghun'); /ledger/4 confirmed ('In 1603 the Persians established a protectorate over the Khamsa')

## circassia: thin

Area: infobox 82000 (None), shape 70050, ratio 0.85, acknowledged True.

Findings:
- `/ledger/5` (for the author): occupation_end 1864 for Kabarda means the occupation ended, but the note says 'Kabarda stays Russian' and the 1864 loss /ledger/6 excludes Kabarda, so Kabarda is never lost in this ledger. Evidence: Note of /ledger/5; region of /ledger/6 = polygon minus (Mozdok + Kabardin-Balkar). Fix: Keep occupation_end 1864 and add Kabarda to the 1864 loss region (polygon minus Mozdok only), or replace the occupation pair with a 1822 loss if a page says annexed.

Thin (for a gap-filler):
- `/keyframe_review/2`: 1822-1863 is one shape although the Russo-Circassian War page (in sources) dates land moves: 'The Russians besieged Anapa in 1828' and the fort surrendered; the Treaty of Adrianople (14 September 1829) gave Circassia to Russia on paper; the Abzakh region annexed and the Abadzekhs submitting on 20 November 1859; Russian control of the coast after 1830. Try: https://en.wikipedia.org/wiki/Russo-Circassian_War
- `/identity/capitals/0`: Bighuqal (Anapa) is capital from 1839 while the Russian siege of Anapa in 1828 ended in surrender; say whose Anapa was in 1839-1859 or name the seat differently. Try: https://en.wikipedia.org/wiki/Anapa
- `/ledger/0`: Found c. 1250 is confidence 1 ('c. 13th century'); Inal's union 1427-1453 is on the page. Try: https://en.wikipedia.org/wiki/Circassia

Spot checks: /ledger/1 confirmed (Mozdok entered 17 July 1763; 'between July 1763 and June 1864'); /ledger/2 confirmed ('placed under Russian military rule in 1822'); /ledger/3 confirmed ('In 1839, the Circassians declared Bighuqal ... as their new capital'); /ledger/4 confirmed (parliament at Sochi 'on June 13, 1860'); /ledger/6 confirmed ('May 21, 1864, was officially the end of the war')

## republic-of-abkhazia: thin

Area: infobox 8664.59 (2024), shape 8346, ratio 0.96, acknowledged True.

Findings:
- `/ledger/0/counterpart` (applied by reviewer): The July 1992 found event and the predecessor named georgian-soviet-socialist-republic, a dossier that ends in April 1991 (successor georgia). Evidence: georgian-soviet-socialist-republic identity end 1991-04, last event 'Independence declared: 9 April 1991', successors ['georgia']; Abkhazia infobox 'Declaration of independence: 23 July 1992'. Fix: Counterpart and /identity/predecessors/0/slug set to georgia, notes extended. Done by the reviewer; validator passes.
- `/keyframe_review/0` (for the author): The 1992-2008 keyframe draws all of Abkhazia except Upper Kodori from July 1992, yet /ledger/2 gains that land in September 1993; the war page has Georgian forces holding most of Abkhazia from August 1992 to September 1993. Evidence: War in Abkhazia page: 'By late August 1992, Georgian forces held most of Abkhazia'; Abkhaz held Gudauta, recaptured Gagra 2 October 1992, Tkvarcheli pocket; 'Sukhumi fell on 27 September'. Fix: Add a 1992-1993 keyframe (Gudauta and Gagra districts plus Tkvarcheli, from October 1992) and start the full shape in 1993.

Thin (for a gap-filler):
- `/ledger/3`: The 1994 ceasefire is on the Abkhazia page without a day; the 14 May 1994 Moscow Agreement is not on the pages opened (confidence 2). Try: https://en.wikipedia.org/wiki/Georgian%E2%80%93Abkhazian_conflict
- `/keyframe_review/0`: Upper Kodori is a 25 km circle (no gazetteer region). Try: https://en.wikipedia.org/wiki/Kodori_Gorge

Spot checks: /ledger/0 confirmed (infobox 'Declaration of independence: 23 July 1992'); /ledger/1 confirmed ('On August 14, the National Guard of Georgia entered Abkhazia'); /ledger/2 confirmed ('Sukhumi fell on 27 September'; upper Kodori 'remained in Georgian hands'); /ledger/3 confirmed as '1994 ceasefire agreement' without a date (confidence 2 fits); /ledger/4 confirmed (Upper Kodori under Georgian control 'until 2008'; Abkhaz moved to expel Georgian forces, August 2008)

## republic-of-south-ossetia: pass

Area: infobox 3885 (2024), shape 4046, ratio 1.04, acknowledged True.

Spot checks: /ledger/0 confirmed ('proclaiming the South Ossetian Soviet Democratic Republic within the Soviet Union on 20 September 1990'); /ledger/1 confirmed ('Georgian troops entered Tskhinvali on 5 January 1991'); /ledger/2 confirmed ('On 24 June 1992, Shevardnadze and the South Ossetian government signed the Sochi ceasefire agreement'); /ledger/3 confirmed (Akhalgori Georgian-held after 1992; in August 2008 'gained full de facto control of the territory of the former South Ossetian Autonomous Oblast')

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| emirate-of-tbilisi 736 found (principality-of-iberia) | principality-of-iberia 736 loss | mismatch | Iberia's 736 loss names umayyad-caliphate; the land (Tbilisi + 30 km) is this emirate's. Acceptable if the orchestrator treats the caliph as the taker; otherwise principality-of-iberia should name emirate-of-tbilisi. |
| emirate-of-tbilisi 853 contest_start (kingdom-of-the-iberians) | kingdom-of-the-iberians 853 contest_start | matched |  |
| emirate-of-tbilisi 854 contest_end (kingdom-of-the-iberians) | kingdom-of-the-iberians 854 contest_end | matched |  |
| emirate-of-tbilisi 1122 loss (kingdom-of-georgia) | kingdom-of-georgia 1122 gain | mismatch | kingdom-of-georgia /ledger/12 names great-seljuk-empire; Emirate of Tbilisi and David IV pages: the city was the emirate's. Route to eu-19-d. |
| kingdom-of-abkhazia 778 found (principality-of-abasgia) | - | exception | principality-of-abasgia has no dossier; listed in the author's counterparts_needing_dossiers. |
| kingdom-of-abkhazia 778 gain (kingdom-of-lazica) | kingdom-of-lazica 777 dissolve | matched | Lazica dissolves 777 with counterpart kingdom-of-abkhazia. |
| kingdom-of-abkhazia 904 gain (kingdom-of-the-iberians) | kingdom-of-the-iberians   | missing | Counterpart corrected by the reviewer from 'nobody' (Kingdom of the Iberians page: 'in 904 Adarnase was dispossessed by Constantine III'); kingdom-of-the-iberians has no 904 loss of Kartli. |
| kingdom-of-abkhazia 914 vassal_start (kingdom-of-the-iberians) | kingdom-of-the-iberians   | missing | kingdom-of-the-iberians records no Abkhazian overlordship over Tao-Klarjeti (914-c.973). |
| kingdom-of-abkhazia 973 vassal_end (kingdom-of-the-iberians) | kingdom-of-the-iberians   | missing | As above. |
| kingdom-of-abkhazia 935 vassal_start (kingdom-of-kakheti-hereti) | kingdom-of-kakheti-hereti   | missing | Same batch: kakheti-hereti has the war 'Abkhazian overlordship over Kakheti' 925-960 but no vassal events. |
| kingdom-of-abkhazia 960 vassal_end (kingdom-of-kakheti-hereti) | kingdom-of-kakheti-hereti   | missing | As above. |
| kingdom-of-abkhazia 1008 dissolve (kingdom-of-georgia) | kingdom-of-georgia 1008 found | mismatch | kingdom-of-georgia found names kingdom-of-the-iberians only; both kingdoms merged in 1008. |
| bagratid-armenia 903 gain (kingdom-of-abkhazia) | kingdom-of-abkhazia   | missing | Ardahan/Klarjeti districts taken from Abkhazia in 903 (Smbat I); no loss in kingdom-of-abkhazia. |
| bagratid-armenia 911 loss (kingdom-of-abkhazia) | kingdom-of-abkhazia   | missing | Confidence-1 lapse of the Ardahan annexation; no gain in kingdom-of-abkhazia. |
| kingdom-of-kakheti-hereti 787 found (principality-of-iberia) | principality-of-iberia   | missing | principality-of-iberia (588-813) has no 787 loss of Kakheti. |
| kingdom-of-kakheti-hereti 1010 loss (kingdom-of-georgia) | kingdom-of-georgia 1010 gain | mismatch | Same year; land differs: Georgia gains Kakheti + Hereti (Zaqatala-Sheki), this dossier loses Kakheti only. Pages disagree (Principality of Kakheti: Bagrat 'invaded Kakheti-Hereti' in 1010; Kingdom page: Hereti incorporated 1010s/1014). |
| kingdom-of-kakheti-hereti 1014 gain (kingdom-of-georgia) | kingdom-of-georgia 1014 loss | mismatch | Same year; Georgia loses Kakheti + Hereti, this dossier gains Kakheti from Georgia and Hereti from kingdom-of-hereti. |
| kingdom-of-kakheti-hereti 1014 gain (kingdom-of-hereti) | - | exception | kingdom-of-hereti has no dossier; listed by the author. |
| kingdom-of-kakheti-hereti 1104 loss (kingdom-of-georgia) | kingdom-of-georgia 1104 gain | matched |  |
| kingdom-of-syunik 987 found (bagratid-armenia) | bagratid-armenia 987 vassal_end | matched | Bagratid also has 885 and 988 vassal_start and 1045 vassal_end with kingdom-of-syunik, none mirrored in Syunik (see thin). |
| bagratid-armenia 988 vassal_start (kingdom-of-syunik) | kingdom-of-syunik   | missing | Syunik has no vassal events (also 885 vassal_start, 1045 vassal_end). |
| kingdom-of-syunik 989 loss (bagratid-armenia) | bagratid-armenia 989 gain | matched | Vayots Dzor, both confidence 1. |
| kingdom-of-syunik 1170 dissolve (eldiguzids) | eldiguzids   | missing | eldiguzids (me-09) has no Syunik gain in 1170. |
| bagratid-armenia 979 vassal_start (kingdom-of-tashir-dzoraget) | kingdom-of-tashir-dzoraget 979 found | mismatch | Tashir has found but no vassal_start; also bagratid 1045 vassal_end unmirrored. |
| kingdom-of-tashir-dzoraget 1118 loss (kingdom-of-georgia) | kingdom-of-georgia 1118 gain | matched |  |
| bagratid-armenia 963 vassal_start (kingdom-of-kars) | kingdom-of-kars 963 found | mismatch | Kars has found but no vassal_start; bagratid 1045 vassal_end unmirrored. |
| kingdom-of-kars 1065 loss (byzantine-empire) | byzantine-empire 1064 gain | mismatch | Within a year, but byzantine-empire /ledger/105 names 'Kingdom of Kars (Gagik-Abas)' instead of the slug kingdom-of-kars; Kingdom of Kars page: 'In 1065 Gagik-Abas ceded his kingdom'. Route to eu-05. |
| republic-of-artsakh 1991 found (azerbaijan-soviet-socialist-republic) | azerbaijan-soviet-socialist-republic 1991 dissolve | exception | The SSR dissolves in 1991; no loss recorded, acceptable for a breakaway declaration. |
| republic-of-artsakh 1992 contest_start (republic-of-azerbaijan) | republic-of-azerbaijan 1992 contest_start | mismatch | Azerbaijan's contest names republic-of-armenia, not republic-of-artsakh. |
| republic-of-artsakh 1994 gain (republic-of-azerbaijan) | republic-of-azerbaijan 1994 occupation_start | mismatch | Type differs: gain here, occupation_start (counterpart republic-of-artsakh) in Azerbaijan. Needs one convention for de facto states. |
| republic-of-artsakh 2020 loss (republic-of-azerbaijan) | republic-of-azerbaijan 2020 occupation_end | mismatch | Same land (Şuşa + Xocavənd), type differs. |
| republic-of-artsakh 2023 loss (republic-of-azerbaijan) | republic-of-azerbaijan 2023 occupation_end | mismatch | Same land, type differs. |
| republic-of-armenia 1994 vassal_start (republic-of-artsakh) | republic-of-artsakh   | missing | Armenia /ledger/9-10 (1994 vassal_start) and /15, /20 (vassal_end 2020, 2023) have no mirror in Artsakh. |
| principality-of-armenia 638 found (byzantine-empire) | byzantine-empire 638 loss | mismatch | Byzantine 637-638 losses name rashidun-caliphate; the principality's Byzantine origin is not recorded there. Low priority. |
| principality-of-armenia 644 loss (rashidun-caliphate) | rashidun-caliphate 644 gain | mismatch | Rashidun 644 gain of the South Caucasus names sasanian-empire. |
| rashidun-caliphate 653 vassal_start (Armenian princes (Theodore Rshtuni)) | principality-of-armenia   | missing | Rashidun /ledger/41, /60, /61, /66 (646 contest, 653 vassal_start, 657 vassal_end) use a label; should name principality-of-armenia, which lacks the mirrors (Arminiya page: Rshtuni submitted in 653). |
| principality-of-armenia 780 loss (Qaysid emirs) | - | exception | No dossier for the Qaysites; listed by the author (suggested slug qaysid-emirs). |
| principality-of-armenia 884 dissolve (bagratid-armenia) | bagratid-armenia 885 found | mismatch | Bagratid found 885 names abbasid-caliphate; within a year. |
| emirate-of-derbent 869 found (abbasid-caliphate) | abbasid-caliphate   | missing | abbasid-caliphate has no Derbent loss c. 869. |
| emirate-of-derbent 1075 loss (shirvan) | shirvan   | missing | shirvan (eu-19-c) has no 1075 gain of Derbent (Emirate of Derbent page: 'Fariburz I annexed Derbent' in 1075). |
| emirate-of-derbent 1130 gain (shirvan) | shirvan   | missing | Confidence-1 bridge; shirvan has no loss. |
| emirate-of-derbent 1225 dissolve (shirvan) | shirvan 1201 gain | mismatch | shirvan /ledger/6 c. 1201 gain from 'Maliks of Darband': counterpart should be emirate-of-derbent; years 1201 vs 'after 1225'. |
| kingdom-of-artsakh 1000 found (bagratid-armenia) | bagratid-armenia   | missing | Bagratid ledger has no Artsakh/Khachen vassal or loss. |
| kingdom-of-artsakh 1261 gain (nobody) | - | exception | Infobox only; counterpart unknown (confidence 1). |
| kingdom-of-artsakh 1603 dissolve (safavid-dynasty) | safavid-dynasty   | missing | Safavid ledger has no Khamsa protectorate 1603; successor melikdoms-of-karabakh has no dossier. |
| circassia 1250 found (nobody) | - | exception |  |
| circassia 1763 loss (russian-empire) | russian-empire   | missing | russian-empire has no 1763 Mozdok gain. |
| circassia 1822 occupation_start (russian-empire) | russian-empire   | missing | russian-empire has no Kabarda event. |
| circassia 1864 loss (russian-empire) | russian-empire 1864 gain | mismatch | russian-empire /ledger/96 names 'Circassians'; should name circassia. Route to eu-11/eu-22 owner of russian-empire. |
| republic-of-abkhazia 1992 found (georgia) | - | exception | Counterpart corrected by the reviewer from georgian-soviet-socialist-republic (ended April 1991). georgia (modern Georgia) is eu-19-b, not run yet. |
| republic-of-abkhazia 1993 gain (georgia) | - | exception | eu-19-b not run; also 1992 contest_start, 1994 contest_end, 2008 gain. |
| republic-of-south-ossetia 1990 found (georgian-soviet-socialist-republic) | georgian-soviet-socialist-republic 1990 rename | exception | The SSR (renamed Republic of Georgia November 1990, ends April 1991) records no loss; acceptable for a declaration. |
| republic-of-south-ossetia 1991 contest_start (georgia) | - | exception | eu-19-b not run. Note: in January 1991 the land was still the georgian-soviet-socialist-republic dossier's (ends April 1991); the pair 1991-1992 straddles the hand-over. |
| republic-of-south-ossetia 2008 gain (georgia) | - | exception | eu-19-b not run. |

## Problems and routing

- No page failed to load. The Wikipedia title Principality_of_Armenia lands on Arminiya (as the author said).
- Reviewer applied four small fixes (abkhazia 904 counterpart, republic-of-abkhazia 1992 counterpart and predecessor, derbent 1075 month, artsakh 2020 confidence); all four files re-validate and were read back.
- Most thin findings are missing mirror events against dossiers already written by eu-19-a (bagratid-armenia: vassal events for Syunik, Tashir-Dzoraget, Kars, and the 903/911 Ardahan events for Abkhazia), me-08/me-09 (rashidun, eldiguzids), eu-19-c (shirvan/Derbent), eu-19-d (kingdom-of-georgia 1010/1014 Hereti and 1122 Tbilisi counterparts) and the Armenia/Azerbaijan dossiers (Artsakh client and occupation conventions).
- Orchestrator decision needed: one convention for de facto states (Artsakh, Abkhazia, South Ossetia): gain/loss with contest, or occupation in the parent state's ledger; republic-of-azerbaijan uses occupation, this batch uses gain/loss.
- georgia (modern Georgia, eu-19-b) is the counterpart of all Abkhazia/South Ossetia events and is not written yet; eu-19-b must also not review georgia_724-georgia_980 again (kingdom-of-abkhazia holds them) and should take georgia_724 for principality-of-abasgia or mark it.

Gazetteer names wished for: South Ossetia, Akhalgori, Upper Kodori Gorge, Hereti, Kukheti, Gardabani, Dvin, Kabarda, Dizak, Gardman.
