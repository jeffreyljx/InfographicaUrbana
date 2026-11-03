# Review af-02-c (2026-10-19): Idrisids, Aghlabids, Hammadids, Almoravids, Zirids

Adversarial review of the five dossiers of af-02-c. All five validate (0 errors, 0 warnings, also with --resolve). Spot checks weighted to confidence-3 events and the largest land moves; no confidence-3 event was mis-dated or absent from its page. Pages were read through WebFetch (a model-made extraction).

Verdicts: idrisids **fix**, aghlabid-dynasty **fix**, hammadid-dynasty **fix**, almoravid-dynasty **fail**, zirid-dynasty **fix**. 'fix' here means the dossier is accepted once the findings marked not applied are made; the one reviewer-applied fix is marked applied.

## idrisids: fix

Area: infobox None (None) vs Cliopatria 194486 km2, ratio None. Infobox gives no area (Established 788, Disestablished 974); no comparison possible.

Findings:
- `/ledger/5` [for the author] The 828 'split' (counterpart 'Idrisid brother-principalities') removes the whole realm outside Fez/100 km, but keyframes /keyframe_review/1-2 keep the full 194,000 km2 outline to 921, /ledger/7 then loses the whole 911 shape, and the note says 'same dynasty, same colour'; the counterpart has no dossier and is not in counterparts_needing_dossiers. Evidence: Idrisid dynasty page: 'the kingdom was divided amongst seven of his brothers, whereby eight Idrisid statelets formed ... Muhammad himself came to rule Fes, with only nominal power over his brothers'. The statelets are Idrisid; a split hands land to a new state (schema), which contradicts the keyframes. Fix: Drop the split as a territorial event (keep the division in notes), or replace it with vassal_start 828 / vassal_end 921 with counterpart 'Idrisid brother-principalities' over the same region (lighter tint) and list that counterpart; do not leave a split whose land the keyframes still draw.
- `/keyframe_review/3` [for the author] The 926 shape is said to be valid 925-927 but carries no years, so 925 (the /ledger/9 regain) falls in no Idrisid shape and 922-924 relies on Cliopatria's gap. Evidence: Idrisid dynasty page: Hassan al-Hajam 'managed to wrest control of Fez from 925'; Cliopatria has no Idrisid shape 922-925. Fix: Say in the correction text that it applies 925-927 (as the dossier does elsewhere for re-timed shapes) or add a new keyframe idrisids_925 (from 925, to 927, correction the 926 shape).

Thin (for a gap-filler):
- `/ledger/2` Confidence-1 gain of 'the rest of the north' at 791 with no dated page; also no event 836-917 and no dates for the Sous, Tadla or Azrou. Try: https://en.wikipedia.org/wiki/Fez,_Morocco
- `/identity/capitals/2` Hajar an-Nasr has no coordinates on the page (rough point used). Try: https://en.wikipedia.org/wiki/Miknasa

Spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/5` confirmed; `/ledger/10` confirmed; `/ledger/12` confirmed

## aghlabid-dynasty: fix

Area: infobox None (None) vs Cliopatria 252479 km2, ratio None. Infobox gives no area ('Maximum extent of Aghlabid authority' map only).

Findings:
- `/ledger/14` [applied by reviewer] The 896 regain of the Jebel Nafusa rested on the Rustamid page at confidence 1 although a page dates it. Evidence: Battle of Manu page: '3 or 4 May 896', 'Aghlabid victory'; the defeat 'marked the end of Rustamid rule over' the mountains (it does not say the Aghlabids ruled them directly). Mirrors rustamid-dynasty /ledger/3 (896-05 loss). Fix: Source set to https://en.wikipedia.org/wiki/Battle_of_Manu (added to sources[]), month 5, confidence 2, note rewritten; re-validated (0 errors, 0 warnings).
- `/ledger/15` [for the author] Mila is lost in 902 and never regained or lost again, but the page has the Fatimid movement having to 'recapture Mila' before Setif in 904, so the Aghlabids held it again in between. Evidence: Aghlabids page: the Aghlabid recovery 'gave Abu Abdallah the opportunity to recapture Mila and then go on to capture Setif by October or November 904'. Fix: Add a gain of Mila (counterpart fatimid-caliphate, confidence 1-2, year from a page on al-Ahwal's campaign) and a 904 loss of Mila with Setif, or say in /ledger/15's note that the 902 loss was reversed until 904.

Thin (for a gap-filler):
- `/ledger/8` Bari as an Aghlabid client 847-871 at confidence 1; Taranto's end of Muslim rule; Reggio and Cosenza 901-902 retention. Try: https://en.wikipedia.org/wiki/Emirate_of_Bari
- `/ledger/15` Date of the Aghlabid recovery of Mila (902-903) before its 904 loss. Try: https://en.wikipedia.org/wiki/Abu_Abdallah_al-Shi%27i
- `/ledger/0` No vassal pair with abbasid-caliphate for the hereditary, tribute-paying emirate 800-909; me-08 may record it and this ledger must then mirror it. Try: https://en.wikipedia.org/wiki/Aghlabids

Spot checks: `/ledger/13` confirmed; `/ledger/10` confirmed; `/ledger/17` confirmed; `/ledger/6` confirmed; `/ledger/19` confirmed; `/ledger/22` confirmed; `/ledger/14` confirmed (year and month; confidence raised 1 to 2)

## hammadid-dynasty: fix

Area: infobox None (None) vs Cliopatria 165043 km2, ratio None. Infobox gives no area, only a map 'circa 1065'; the dossier keeps the 165,000 km2 outline to 1089 against Cliopatria's 32,800 km2 from 1066, supported by the page (peak under al-Nasir, southern territories given up in 1090).

Findings:
- `/ledger (between /7 and /8; and before /12)` [for the author] No occupation pair for Algiers, although almoravid-dynasty /ledger/10 (1082 occupation_start, counterpart hammadid-dynasty) and /ledger/22 (1104 occupation_end) record it, and the Hammadid /keyframe_review/6 note relies on that hatching. Evidence: Schema: 'occupation_start / occupation_end: ... the owner records the same event with the roles reversed.' The author's notes say the occupation is 'recorded as in the Almoravid dossier' but the Hammadid ledger has none. Fix: Add occupation_start 1082 and occupation_end 1104, counterpart almoravid-dynasty, region {place: Algiers, km: 50}, source the Almoravid dynasty page, confidence 2 and 1 as on the Almoravid side.
- `/ledger/6` [for the author] Laribus (El Kef) is gained from zirid-dynasty in 1066, but zirid-dynasty /ledger/9 already loses that land (inside its 1056-minus-1066 region: 19 cells round El Kef) to 'Banu Hilal and Banu Sulaym' in 1057. Evidence: Hammadid page: 'Sultan Al Nacer conquered the city of Laribus, near Kef, in 1066' with no previous holder; the counterpart is the author's inference from Cliopatria's Zirid 1056 shape. Fix: Make the two dossiers agree: either counterpart 'Banu Hilal and Banu Sulaym' here, or the Zirid dossier keeps El Kef to 1066 and loses it to hammadid-dynasty then.
- `/ledger/7 and /keyframe_review/6` [for the author] The 1082 loss of the Oran-Tlemcen part of the outline (about 18,700 km2, confidence 1) goes to almoravid-dynasty, but no Almoravid keyframe holds that land (its 1072/1085 shapes overlap the Hammadid outline by 5 cells), and almoravid-dynasty /ledger/11 gains 'Oran and Tenes' from unnamed rulers; Tenes (9 cells) stays inside this keyframe 1082-1089 although the Almoravids gain it in 1082. Evidence: Grid resolution: intersect(Hammadid 1056, Oranais) = 74 cells; intersect(Hammadid 1056, Tenes/40 km) = 9 cells, not in Oranais; no page opened names the Hammadids as losers of the Oranais. Fix: Either keep the Oranais part (drop /ledger/7, page silent) and lose Tenes to almoravid-dynasty in 1082 (mirrored in almoravid /ledger/11 with counterpart hammadid-dynasty), or keep /ledger/7 and have the Almoravid dossier draw that land from 1082; record the choice in both.
- `/ledger/4/note` [for the author] The note has Hammama submitting 'after an attack by Qa'id ibn Hammad'; the page as read has Hammama attacking Qa'id, withdrawing to Fez, asking for peace and submitting. Evidence: Hammadid dynasty page (1039 passage). Fix: Re-read the 1039 sentence and correct the quotation; the year and the submission stand.

Thin (for a gap-filler):
- `/ledger/5` End of Hammama's submission (1062 bridge, confidence 1). Try: https://en.wikipedia.org/wiki/Fez,_Morocco
- `/ledger/7` Who held the Oranais and Tenes in 1080-1083 (confidence 1). Try: https://en.wikipedia.org/wiki/Yusuf_ibn_Tashfin
- `/ledger/9` Hilalian steps year by year, Constantine, Biskra, Zab; the 1090 loss could rise to confidence 3 ('In 1090 the Hammadids moved their capital to Bejaia, giving up their southern territories to the Hilalians', Hammadid page) once a region is named. Try: https://en.wikipedia.org/wiki/Constantine,_Algeria

Spot checks: `/ledger/0` confirmed; `/ledger/3` confirmed; `/ledger/4` confirmed (year and submission; quotation inexact); `/ledger/9` confirmed; `/ledger/16` confirmed; `/ledger/17` confirmed

## almoravid-dynasty: fail

Area: infobox 1000000 (1120) vs Cliopatria 1923812 km2, ratio 0.52. Under a factor of two; acknowledged in /keyframe_review/12 (755,000 km2 of Mauritanian Sahara).

Findings:
- `/keyframe_review/18/correction` [for the author] BLOCKING. The new 1147-1155 keyframe draws the whole Spanish and Portuguese part of the 1139 shape (about 253,700 km2, 1,003 cells) as Almoravid for nine years, four beyond Cliopatria's own Iberian end (1151), and no ledger event removes Lisbon in 1147. Evidence: The cited Almoravid page: 'Lisbon was conquered by the Portuguese in 1147'; 'The Muridun staged a major revolt in southwestern Iberia in 1144'; the 1155 sentence ('the remaining Almoravids were forced to retreat to the Balearic Islands and later Ifriqiya') sits in a list of fragments resisting after Marrakesh fell and does not make the 1139 Iberian outline Almoravid to 1155. The Almohad page's 'Between 1146 and 1173, the Almohads gradually wrested control from the Almoravids over the Muslim principalities in Iberia' describes the second taifas, not Almoravid rule. /ledger/32 then loses only the Spanish part, so the Portuguese part (152 cells, 38,400 km2) is never lost. Fix: Rebuild 1144-1155 in Iberia from pages: a 1144 contest or loss in southwestern Iberia to the Muridun (counterpart already listed); a 1147 loss of Lisbon (and Santarem, from its page) to kingdom-of-portugal; the 1147-1148 losses to the Almohads and the second-taifa rulers; keep only the remnant a page names (the Banu Ghaniya page has Yahya dying 'in Granada' in late 1148 or early 1149) to 1155; make /ledger/32 lose whatever K18 keeps.
- `/keyframe_review/15 (step from /keyframe_review/14)` [for the author] The 1139 shape drops about 1,429,000 km2 (the Sahara and Mauritania, 755,000 km2 of it in Mauritania) from the 1126 shape and no ledger event explains it. Evidence: Shapes.csv 1126: 1,908,330 km2; 1139: 421,334 km2. The Almoravid page dates the break: after Abu Bakr died in November 1087 'the confederation of Berber tribes in the Sahara was divided between the descendants of Abu Bakr and his brother Yahya', the southern wing ruling from Azuggi; north and south were 'two distinct but co-dependent parts'. Fix: Add a loss (or split) of the Saharan land, counterpart 'southern Almoravids (Adrar)' or nobody, in 1087 (confidence 2, from that sentence) and drop it from the 1094-1138 keyframes, or keep it as tributary to 1138 and record a 1139 loss at confidence 1 with the reason.
- `/ledger/24 and /keyframe_review/9` [for the author] Lisbon is drawn Almoravid from 1094 (inside the 1094 shape) and gained again in 1111 with no loss in between. Evidence: The page: 'In 1111, Sir ibn Abu Bakr ... campaigned in the west, occupying Lisbon and Santarem'; the K9 note admits Lisbon (8 cells) is inside the 1094 shape. Fix: Either drop Lisbon from /ledger/24 (keep Santarem, naming its holder from a page) or take Lisbon out of the 1094-1110 keyframes and the 1094 Badajoz gain.
- `/ledger (after /33)` [for the author] No Balearic loss in 1185, although the Banu Ghaniya page has the Almohads retaking the islands while Ali ibn Ishaq was in Ifriqiya. Evidence: Banu Ghaniya page (rulers table): 'the Almohads retook the islands in 1185'. Fix: Add a 1185 loss (or occupation_start by almohad-caliphate) of the Balearic Islands and the regain under Abdallah ibn Ishaq with its year from the page, or explain in a note why it is not drawn.
- `/ledger/11` [for the author] Oran and Tenes are gained from unnamed rulers while hammadid-dynasty /ledger/7 loses the Oranais to this dossier in the same year; Tenes lies inside the Hammadid outline (9 cells) and no Almoravid keyframe draws it or the Oranais part of the Hammadid shape. Evidence: See the hammadid-dynasty finding at /ledger/7; the Yusuf ibn Tashfin page gives 'Algiers, Tenes, and Oran' 1082-83. Fix: Name hammadid-dynasty as counterpart for the land that comes from the Hammadid outline and draw it from 1082, or agree with the Hammadid author to drop /ledger/7 there.

Thin (for a gap-filler):
- `/ledger/22` End of the Algiers occupation (1104, confidence 1 bridge). Try: https://en.wikipedia.org/wiki/Algiers
- `/keyframe_review/18` Dated losses in al-Andalus 1144-1155 (Lisbon, Santarem, Almeria 1147; Seville and Cordoba to the Almohads; the second taifas). Try: https://en.wikipedia.org/wiki/Siege_of_Lisbon
- `/keyframe_review/15` Sijilmasa and the Saharan homeland after 1087/1139. Try: https://en.wikipedia.org/wiki/Abu_Bakr_ibn_Umar
- `/ledger/34` Banu Ghaniya in Ifriqiya after 1188 (Yahya ibn Ghaniya to 1237/38) is left to a banu-ghaniya dossier; the occupation region country:Tunisia is wider than the page's 'Bougie, Constantine and Algiers'. Try: https://en.wikipedia.org/wiki/Banu_Ghaniya

Spot checks: `/ledger/30` confirmed; `/ledger/27` confirmed; `/ledger/16` confirmed; `/ledger/13` confirmed; `/ledger/23` confirmed; `/ledger/25` confirmed; `/ledger/35` confirmed; `/ledger/32` confirmed as a sentence, but it does not support the 1147-1155 keyframe

## zirid-dynasty: fix

Area: infobox None (None) vs Cliopatria 113557 km2, ratio None. Infobox gives no area, only a map of the extent c. 980.

Findings:
- `/ledger (after /0)` [for the author] No vassal pair with fatimid-caliphate for the viceroyalty 972 to the break of 1048-49, although the author's own problem (the Fatimid 970-1055 shapes cover Ifriqiya) needs exactly that pair; the notes say the break 'has no event type'. Evidence: Zirid page: Buluggin 'was appointed viceroy of Ifriqiya', confirmed '2 October 972'; 'The Zirids renounced the Fatimids and recognized the Abbasid Caliphs in 1048-49' (also 'sometime between 1041 and 1051'). Reviewer brief check 3: a vassal_start of X is a vassal_start in X's ledger with the overlord as counterpart (practice in af-02-b for kingdom-of-numidia). Fix: Add vassal_start 972-10 and vassal_end 1048, counterpart fatimid-caliphate, region the 972 keyframe's correction, source the Zirid page, confidence 3 and 2; tell me-08 to record the same pair.
- `/ledger/9` [for the author] The 1057 loss of the interior to 'Banu Hilal and Banu Sulaym' includes El Kef (19 cells), which hammadid-dynasty /ledger/6 takes from zirid-dynasty in 1066. Evidence: Grid: intersect(Zirid 1056, El Kef/40 km) = 19 cells, intersect(Zirid 1066, El Kef/40 km) = 0. Fix: Agree with the Hammadid dossier on who held Laribus 1057-1066 (see the hammadid finding at /ledger/6).
- `/ledger/3` [for the author] Morocco in 985 is lost to 'nobody', but the land was not stateless and /ledger/2 gained it from 'western Maghreb rulers (not named on the page)'. Evidence: Zirid page: 'his successor decided to abandon Morocco in 985' (no heir named). Fix: Use the same counterpart string as /ledger/2 (or caliphate-of-cordoba if a page names the Umayyad clients).

Thin (for a gap-filler):
- `/ledger/13` End of the Tripolitania overlordship (1146 bridge, confidence 1) and who ruled Tripoli (Banu Khazrun) from about 1001. Try: https://en.wikipedia.org/wiki/Banu_Khazrun
- `/ledger/14` Gabes and the other coastal towns in 1148; who held Tunis in 1148. Try: https://en.wikipedia.org/wiki/Kingdom_of_Africa

Spot checks: `/ledger/0` confirmed; `/ledger/3` confirmed; `/ledger/7` confirmed; `/ledger/9` confirmed; `/ledger/16` confirmed (year; the 12 July day is from the Kingdom of Africa page, not opened)

## Cross-dossier matrix

- idrisids 789 gain (Banu Ifran (Abu Qurra)) -> no mirror: exception — listed in counterparts_needing_dossiers (banu-ifran)
- idrisids 791 gain (nobody) -> no mirror: exception — nobody; confidence 1
- idrisids 828 gain (nobody) -> no mirror: exception — nobody (the Sous)
- idrisids 828 split (Idrisid brother-principalities) -> no mirror: missing — no dossier, not listed; the keyframes keep the land as Idrisid; see idrisids /ledger/5 finding
- idrisids 921 loss (fatimid-caliphate) -> no mirror: exception — counterpart dossier not written yet (group has not run) (me-08); the holder was Musa ibn Abi l-Afiya / Miknasa, listed as miknasa
- idrisids 925 gain (fatimid-caliphate) -> no mirror: exception — counterpart dossier not written yet (group has not run) (me-08)
- idrisids 927 loss (fatimid-caliphate) -> no mirror: exception — counterpart dossier not written yet (group has not run) (me-08)
- idrisids 974 loss (caliphate-of-cordoba) -> no mirror: exception — counterpart dossier not written yet (group has not run) (eu-12)
- aghlabid-dynasty 812 loss (rustamid-dynasty) -> rustamid-dynasty 812 gain: matched — same region (Rustamid 778 shape within Tripolitania)
- aghlabid-dynasty 831 gain (byzantine-empire) -> no mirror: exception — counterpart dossier not written yet (group has not run) (eu-05); also 840 Taranto, 843 Messina, 859 Enna, 870 Malta, 878 Syracuse, 902 Taormina, same status
- aghlabid-dynasty 847 vassal_start (Emirate of Bari) -> no mirror: exception — listed (emirate-of-bari, eu-13); vassal_end 871 likewise
- aghlabid-dynasty 896 gain (rustamid-dynasty) -> rustamid-dynasty 896 loss: matched — both now cite the Battle of Manu (May 896); the Aghlabid event was raised to confidence 2 by this review
- aghlabid-dynasty 902 loss (fatimid-caliphate) -> no mirror: exception — counterpart dossier not written yet (group has not run) (me-08); pre-909 movement listed as kutama-fatimid-movement; also 904 Setif, 907 Baghaya
- hammadid-dynasty 1015 contest_start (zirid-dynasty) -> zirid-dynasty 1015 contest_start: matched — Hammadid found 1014 vs Zirid contest from 1015: one-year double claim, within tolerance
- hammadid-dynasty 1017 gain (zirid-dynasty) -> zirid-dynasty 1017 loss: matched — same region (Hammadid 1018 shape)
- hammadid-dynasty 1039 vassal_start (Hammama of Fez) -> no mirror: exception — named in the author notes but missing from counterparts_needing_dossiers; vassal_end 1062 at confidence 1
- hammadid-dynasty 1066 gain (zirid-dynasty) -> zirid-dynasty 1057 loss: mismatch — Zirid loses El Kef in 1057 to Banu Hilal and Banu Sulaym, not to the Hammadids in 1066
- hammadid-dynasty 1082 loss (almoravid-dynasty) -> almoravid-dynasty 1082 gain: mismatch — Almoravid gains Oran and Tenes from unnamed rulers; the 18,700 km2 Oranais part of the Hammadid outline is drawn by neither side 1082-1089; Tenes is in the Hammadid keyframe but gained by the Almoravids
- hammadid-dynasty 1090 loss (Banu Hilal and Banu Sulaym) -> no mirror: exception — tribal confederation, no dossier and not listed; treat as nobody-like (nomad land) or list it
- hammadid-dynasty 1103 contest_start (almoravid-dynasty) -> almoravid-dynasty 1103 contest_start: matched — Tlemcen 1103-1104 on both sides
- hammadid-dynasty 1128 gain (Banu Khurasan (Tunis)) -> no mirror: exception — listed (banu-khurasan); Zirid loses Tunis to the same counterpart in 1059
- hammadid-dynasty 1148 loss (Tunis (next holder not named on the page)) -> no mirror: exception — page silent; gap listed
- hammadid-dynasty 1152 loss (almohad-caliphate) -> no mirror: exception — counterpart dossier not written yet (group has not run) (af-02 almohad-caliphate not on disk); Algiers and Bejaia
- almoravid-dynasty 1060 gain (barghawata-conference) -> barghawata-conference 1060 loss: matched — contest 1058-1060 also matched; regions cite the Barghawata 1056 vs 1015 shape
- almoravid-dynasty 1081 gain (emirate-of-nekor) -> emirate-of-nekor 1081 loss: matched — Almoravid cites the Nekor 1027 shape, Nekor the 1018 shape
- almoravid-dynasty 1082 occupation_start (hammadid-dynasty) -> hammadid-dynasty None None: missing — Hammadid ledger has no occupation pair for Algiers (1082-1104)
- almoravid-dynasty 1082 gain (Oran and Tenes (rulers not named on the page)) -> hammadid-dynasty 1082 loss: mismatch — see hammadid 1082 row
- almoravid-dynasty 1058 gain (Aghmat (rulers not named on the page)) -> no mirror: exception — free-text counterpart, page silent; likewise Fez 1070, Tangier and Oujda 1079, Tlemcen 1080, Lisbon and Santarem 1111, Balearic Islands 1115
- almoravid-dynasty 1083 gain (taifa-of-ceuta) -> no mirror: exception — counterpart dossier not written yet (group has not run) (eu-12); also the taifas of Granada 1090, Seville 1091, Almeria 1091, Murcia 1092, Badajoz 1094, Valencia 1102, Zaragoza 1110 and the 1118 loss to kingdom-of-aragon
- almoravid-dynasty 1144 loss (almohad-caliphate) -> no mirror: exception — counterpart dossier not written yet (group has not run) (af-02 almohad-caliphate not on disk); also 1145, 1146, 1147, 1155 losses and the 1184-1188 occupation
- almoravid-dynasty 1147 loss (kingdom-of-portugal) -> no mirror: missing — no event: Lisbon 1147 is on the Almoravid page; see the blocking finding at /keyframe_review/18
- zirid-dynasty 972 vassal_start (fatimid-caliphate) -> no mirror: missing — no vassal pair 972-1048 in the Zirid ledger; me-08 not written; needed so the Fatimid 970-1055 shapes and the Zirid 972-1055 keyframes do not both claim Ifriqiya
- zirid-dynasty 978 vassal_start (Tripolitania) -> no mirror: exception — free-text vassal, not listed; vassal_end 1146 confidence 1
- zirid-dynasty 980 gain (western Maghreb rulers (not named on the page)) -> no mirror: exception — free text; the 985 loss goes to nobody instead of the same counterpart
- zirid-dynasty 1057 loss (Banu Hilal and Banu Sulaym) -> no mirror: exception — not listed; conflicts with hammadid 1066 gain of El Kef
- zirid-dynasty 1059 loss (Banu Khurasan (Tunis)) -> no mirror: exception — listed (banu-khurasan)
- zirid-dynasty 1135 loss (kingdom-of-sicily) -> no mirror: exception — counterpart dossier not written yet (group has not run) (Kingdom of Sicily, Cliopatria from 1139)
- zirid-dynasty 1148 loss (kingdom-of-africa) -> no mirror: exception — counterpart dossier not written yet (group has not run) (af-02 kingdom-of-africa not on disk)

## Counterparts needing dossiers (in addition to the author's list)

- Hammama of Fez (Zenata/Maghrawa rulers of Fez) (maghrawa-of-fez, 1039-1062)
- Idrisid brother-principalities (only if the 828 split is kept) (idrisid-principalities, 828-921)
- Southern Almoravids of the Adrar (Abu Bakr's descendants) (southern-almoravids, 1087-1200)
- Taifa of Majorca (Mubashir al-Dawla) (taifa-of-majorca, 1076-1115)

## Problems

- No page failed to load. WebFetch returns a model-made extraction, so quotations are approximate; years and months were checked.
- Spot checks: 31 events checked on 10 pages (Idrisid dynasty, Idris I, Aghlabids, Muslim conquest of Sicily, Battle of Manu, Hammadid dynasty, Almohad Caliphate, Almoravid dynasty, Banu Ghaniya, Zirid dynasty); no confidence-3 event was mis-dated or absent from its page.
- One fix applied by the reviewer: aghlabid-dynasty /ledger/14 (Battle of Manu source, month 5, confidence 2) and a new sources[] entry; the file re-validates with 0 errors and 0 warnings.
- Context dossiers on disk: rustamid-dynasty, barghawata-conference, emirate-of-nekor only; fatimid-caliphate, almohad-caliphate, kingdom-of-africa, byzantine-empire, caliphate-of-cordoba and the Iberian taifas are not written yet, so their mirrors are exceptions.
- None of the four infobox areas besides the Almoravid one gives a figure (Idrisid, Aghlabid, Hammadid, Zirid).
