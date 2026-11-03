# Review of batch me-07 (Rashidun to Umayyad), 2026-10-19

Reviewer: adversarial review per history/briefs/reviewer-brief.md. Validator (--resolve): all eight dossiers 0 errors, 0 warnings. Spot checks: 3-8 events per dossier opened with WebFetch; every checked date was on its page except Rashidun /ledger/37 (mis-dated, c=2). Verdict "fix" would mean fixed by the reviewer; "fail" goes back to the author with the findings below.

| dossier | verdict |
| --- | --- |
| rashidun-caliphate | fail |
| dabuyid-dynasty | pass |
| umayyad-caliphate | fail |
| islamic-state-of-medina | thin |
| zubayrid-caliphate | fail |
| mukhtarid-state-of-kufa | fail |
| najdat-kharijite-emirate | pass |
| azariqa-kharijite-emirate | pass |

## rashidun-caliphate: fail

Sources hold: every spot-checked date is on its page. It fails on keyframe/ledger consistency in Iran, the Caucasus and Libya: the 644-660 corrections keep land the ledger loses (Armenia, Atropatene 646) or gains only later (Fars 648, Rey 651), keep Makran with no gain event, and Cyrenaica/Tripolitania are dated 647 against 642/643 on the Maghreb page. One small fix applied (predecessor land).

Area: infobox 6400000 km2 (655), Cliopatria 7090123 km2, ratio 0.9. acknowledged in the keyframe notes

Findings:
1. [APPLIED by reviewer] `/identity/predecessors/0/land`: Predecessor land was region Arabia, but the hand-over from Medina in 632 is the Hejaz (found event, keyframe 632 and Medina successor land all say Hejaz).
   - Evidence: Rashidun page: "The year 12 Hijri dawned on 18 March 633 with the Arabian peninsula united under the caliph in Medina" - Arabia is united only in 633; islamic-state-of-medina /identity/successors/0/land is region Hejaz.
   - Fix: Changed region Arabia -> Hejaz (text kept). Re-validated: 0 errors, 0 warnings.
2. [blocking] `/ledger/35 with /keyframe_review/6, /7, /8, /9`: Armenian Highlands and Atropatene are lost in 646 to kingdom-of-armenia, Armenia is never regained, yet the 647-660 corrections (Cliopatria 647 and 656 shapes, north to 43.1 N) keep the whole Caucasus; Atropatene's rebels are not the Armenian kingdom.
   - Evidence: Persia page: "The main rebellions were in the Persian provinces of Armenia and Azerbaijan in 646" and "The conquest of Iranian Azerbaijan started in 651". byzantine-empire /ledger/20 has Armenia passing from the Rashidun to Byzantium in 657 (c=2), with no Rashidun mirror. The Cliopatria Kingdom of Armenia row ends in 646.
   - Fix: Either (a) re-type 646 as contest_start (rebellion) with counterpart "Armenian and Azerbaijani rebels", contest_end 651 for Atropatene, and add a 657 loss of Armenia to byzantine-empire (mirror of byzantine /ledger/20); or (b) keep the 646 loss but subtract Armenian Highlands and Atropatene from the 647-650 correction, subtract Armenia from 651-660 and record its regain if any. Do not name kingdom-of-armenia for Atropatene.
3. [blocking] `/keyframe_review/5, /keyframe_review/6`: The 644-646 and 647-650 corrections keep Fars and Rey inside although the ledger gains Fars only in 648 (/ledger/39) and Rey in 651 (/ledger/43) from the Sasanians; sasanian-empire loses Media (Rey) in 642.
   - Evidence: Persia page: "In c. 643, Uthman ibn Abi al-As seized Bishapur, which signed a peace treaty"; "In 648 ... forced the governor of Estakhr ... to surrender"; Rey besieged in 651 and surrendered "after fierce resistance". sasanian-empire /ledger/114 loses Media in 642.
   - Fix: Make the corrections and the ledger agree: subtract Fars (admin1 Fars) until 648, or keep it and re-type /ledger/39 and /ledger/43 as reconquests after the revolts the page names ("Fars and Sistan in 649") - contest_start at the revolt, contest_end at the reconquest, counterpart the rebels - instead of gains from sasanian-empire.
4. [blocking] `/keyframe_review/5 ... /keyframe_review/10`: Makran (about a quarter of Pakistan, about 0.2 M km2) is kept in every correction from 644, but no ledger event gains it.
   - Evidence: The K5 note says "Makran and Pakistan (25%) are left in"; the Persia page has "Makran in 650" among the rebellions and "a simultaneous attack launched against Kerman and Makran" in 651, so it was taken before 650 and again in 651.
   - Fix: Add a gain of Makran (region Makran) with the year the Persia page supports (before the 650 revolt, c=1-2, or 651 c=2) and a contest for the 650 revolt; or subtract Makran from the 644-650 corrections and gain it in 651.
5. [blocking] `/ledger/37 with /keyframe_review/4, /5`: Cyrenaica and Tripolitania are dated 647 (c=2), but the Rashidun page gives no year for either (647 is Sufetula) and the Maghreb page dates Barqa to 642/643 and Tripoli to about 643; the 641-646 corrections leave Libya out.
   - Evidence: Maghreb page: Barqa taken "Soon after the fall of Alexandria in 642"; Tripoli "after around a month it also fell in around 643". Rashidun page: "In the ensuing battle in 647, the Exarchate was defeated" (Sufetula). byzantine-empire /ledger/13 loses Cyrenaica in 644 (643-644).
   - Fix: Split /ledger/37: gain Cyrenaica 643 and Tripolitania 643 (source the Maghreb page, add it to sources[], c=2); add Cyrenaica and Tripolitania to the 641 (from 643) and 644 corrections, or split 641 at 643. Mis-dated at confidence 2.
6. [blocking] `(missing, between /ledger/39 and /ledger/40)`: No event for the Byzantine reoccupation of Alexandria in 645-646.
   - Evidence: Muslim conquest of Egypt page: "Constans sent a large fleet of 300 ships to retake Egypt towards the end of 645" and Manuel "easily overpowered small Arab garrison at Alexandria"; infobox 645-646. byzantine-empire /ledger/14 (gain 645, c=3) and /ledger/15 (loss 646) have no mirror here.
   - Fix: Add loss 645 and gain 646 of place Alexandria 60 km, counterpart byzantine-empire, source the Egypt page (or an occupation_start/occupation_end pair).
7. [to do, not blocking] `/ledger/48`: The 656 loss of Syria to Mu'awiya names only the Levant, but the 656 keyframe drops Cyprus ("went with Syria") and the Umayyad 656 keyframe includes it.
   - Evidence: /keyframe_review/8 note; umayyad-caliphate /keyframe_review/0 note "Syria (Levant 81%, Cyprus)".
   - Fix: Add region Cyprus (island) to the /ledger/48 region union.

Gaps for a gap-filler:
- `/ledger/7`: date of Hira and the first Iraqi towns (634 bridging, c=1) (try https://en.wikipedia.org/wiki/Battle_of_Hira)
- `/ledger/9, /ledger/10`: fate and date of the Ghassanid country (636 bridging, c=1) (try https://en.wikipedia.org/wiki/Jabalah_ibn_al-Aiham)
- `/ledger/23`: date Hormuzan broke the treaty (640, c=1) (try https://en.wikipedia.org/wiki/Hormuzan)
- `/ledger/32`: date of Isfahan (643, c=1) (try https://en.wikipedia.org/wiki/Isfahan)
- `/ledger/38`: date of the withdrawal from Ifriqiya after Sufetula (648, c=1) (try https://en.wikipedia.org/wiki/Battle_of_Sufetula)

Spot checks:
- `/ledger/43` W:Muslim_conquest_of_Persia: confirmed: Rey besieged in 651 and "surrendered after fierce resistance"
- `/ledger/41` W:Muslim_conquest_of_Persia: confirmed: "In 651 the conquest of Khurasan was assigned to Ahnaf ibn Qais"
- `/ledger/33` W:Muslim_conquest_of_Persia: confirmed: "Suhail marched from Basra in 643" and Kerman "was subdued"
- `/ledger/35` W:Muslim_conquest_of_Persia: confirmed (year): "main rebellions were in the Persian provinces of Armenia and Azerbaijan in 646"; counterpart wrong for Azerbaijan
- `/ledger/39` W:Muslim_conquest_of_Persia: confirmed: "In 648 ... forced the governor of Estakhr, Mahak, to surrender"
- `/ledger/42` W:Muslim_conquest_of_Persia: partly confirmed: page dates "The first real invasion" of Sistan to 650; the 651 Zaranj tribute was not quoted back
- `/ledger/37` W:Rashidun_Caliphate: mis-dated (c=2): no year for Cyrenaica or Tripoli on the Rashidun page; Maghreb page gives 642/643 and around 643
- `/identity/capitals` W:Rashidun_Caliphate: confirmed: "Medina (632-656); Kufa (656-661)"

## dabuyid-dynasty: pass

Could not break it: the four checked events (642 founding, 716 invasion, 759-760 conquest, 760 end) are on their pages with the years given; capitals sit inside the shape; the six Cliopatria shapes are reviewed and the 757-760 extension is sourced. Only gaps a gap-filler could close.

Area: infobox None km2 (None), Cliopatria 64825 km2, ratio None. no area in the infobox

Gaps for a gap-filler:
- `/ledger/2`: year Farrukhan moved the capital to Sari (712 bridging, c=1) (try https://en.wikipedia.org/wiki/Sari,_Iran)
- `/wars/0`: the 716/717 treaty: Farrukhan page says Yazid agreed "to withdraw in return for tribute" - a tributary pair with umayyad-caliphate may be warranted; and Abu Muslim's submission c. 750 (try https://en.wikipedia.org/wiki/Farrukhan_the_Great)
- `/notes`: Tang embassy of 746 recognising Khurshid as a vassal prince (Khurshid page) - a vassal pair for tang-dynasty if ea-04 wants it (try https://en.wikipedia.org/wiki/Khurshid_of_Tabaristan)

Spot checks:
- `/ledger/0` W:Dabuyid_dynasty: confirmed: "from around 642 to the Abbasid conquest in 760"; table Gil Gavbara 642-660
- `/ledger/3` W:Farrukhan_the_Great: confirmed: "In 716, the Arab governor of Iraq and Khurasan, Yazid ibn al-Muhallab invaded Tabaristan"
- `/ledger/6` W:Khurshid_of_Tabaristan: confirmed: "the Abbasids conquered his country in 759-760"
- `/ledger/8` W:Dabuyid_dynasty: confirmed: header "Dabuyid dynasty (642-760)"
- `/identity/capitals/0` W:Dabuyid_dynasty: confirmed: infobox "Capital: Fuman (660-760)"; Sari from the Farrukhan page, undated

## umayyad-caliphate: fail

Dates hold on every page opened (685 Egypt, 690 Cyrenaica, 705 Balkh, 721 Sindh, 728 Bukhara, 743 Transoxiana, 743 Gujarat). It fails on the Second Fitna: the 684-691 keyframe (Levant and Egypt) drops Iran, the Jazira, Arminiya, eastern Arabia, Libya and Kairouan with no loss events (the 683 loss names only Hejaz, Iraq, Egypt, Yemen) and the 692 keyframe restores them with gains only for Iraq, Khorasan and the Hejaz; Cyrenaica is lost in 690 and never regained; Gujarat is lost in 743 without ever being gained.

Area: infobox 15000000 km2 (720), Cliopatria 9839115 km2, ratio 0.66. acknowledged in the keyframe notes

Findings:
1. [blocking] `/keyframe_review/6 with /ledger/13, /ledger/19, /ledger/20`: The 684-691 correction (Levant + Egypt) removes Khuzestan, Jibal, Isfahan, Rey, Sistan, Azerbaijan, Arminiya, the Jazira, Bahrain, Oman and Nejd, but no ledger event loses them: /ledger/13 (683/11) names only Hejaz, Mesopotamia, Egypt and Yemen; zubayrid /ledger/1 gains Fars and Kerman from the Umayyads in 683 with no mirror here; najdat /ledger/0-1 found and gain Nejd, Bahrain and Oman from the Umayyads in 685 with no mirror here. The 692 keyframe (Cliopatria 692) restores all of them with gains only for Iraq (691), Khorasan (691, c=1), Hejaz (692), Armenia (692) and the Najdat lands (693).
   - Evidence: Abd Allah ibn al-Zubayr page: "Most of the Islamic provinces offered their allegiance, including Egypt, Kufa, Yemen and the Qaysi tribes of northern Syria"; Second Fitna page: "most provinces recognized Ibn al-Zubayr as caliph"; Mukhtar page: Iraq "and its dependencies including Arminiya, Adharbayjan, Jibal and parts of the Jazira". Area: 674 shape 7.0 M km2 against roughly 1.3 M km2 for Levant + Egypt.
   - Fix: Widen /ledger/13 to the provinces that recognised Ibn al-Zubayr (add Fars, Kerman, Khuzestan, Jibal/Media, Isfahan, Sistan, Azerbaijan; Arminiya and the eastern Jazira if the author accepts the Mukhtar page), add a 685 loss of Nejd, Bahrain and Oman to najdat-kharijite-emirate, and widen /ledger/20 (691/10 gain from zubayrid) to Iraq with the same dependencies. Coordinate with the Zubayrid dossier (it must hold what this loses).
2. [blocking] `/keyframe_review/6 with /ledger/16, /ledger/18`: The 684-691 correction omits Cyrenaica and Tripolitania, which the ledger keeps Umayyad until the Byzantine landing of 690, and Kairouan, regained from Kusaila in 688.
   - Evidence: Maghreb page: "a Byzantine fleet landing in Cyrenaica in 690" and "Barqa had fallen out of Muslim control" (so it was Muslim before 690); "in 688/9 ... Zuhayr ibn Qays to defeat Kusaila and retake Qayrawan".
   - Fix: Add Tripolitania and Cyrenaica to the 684-689 correction (Cyrenaica out from 690) and Kairouan from 688; split the keyframe at 688 and 690 or note the ledger carries them.
3. [blocking] `/ledger/18 with /keyframe_review/7 ... /14`: Cyrenaica is lost to the Byzantines in 690 and never regained in the ledger, yet every keyframe from 692 contains it.
   - Evidence: Maghreb page (confirmed): 690 landing; the Umayyad ledger has no later Cyrenaica event; byzantine-empire has no gain of Cyrenaica either.
   - Fix: Add the regain (Hassan ibn al-Nu'man's advance through Barqa in the 690s; find the year on the Maghreb or Hassan ibn al-Nu'man page) or subtract Cyrenaica from the 692 correction until a dated regain.
4. [blocking] `/ledger/68 with /ledger/56`: The 743 loss of Gujarat and Rajasthan removes land the ledger never gained (723 is only a contest_start).
   - Evidence: India page: "Al-Junayd have conquered all of Gujarat, a large part of Rajasthan, and some parts of Madhya Pradesh"; "Junayd ... (723-726) recaptured Sindh, conquered Gujarat and parts of Rajasthan"; "The Arabs lost their conquests in Rajasthan and Gujarat by 743".
   - Fix: Add a gain c. 724-725 of Gujarat (and Rajputana as far as the page supports), c=2, counterpart the local kings (maitraka-dynasty / gurjara-pratihara-dynasty or "Hindu kings"), or turn /ledger/68 into a contest_end only.
5. [to do, not blocking] `/ledger/14`: 684/8 records a gain of northern Syria from the Zubayrids, but neither the Umayyad 683 loss nor the Zubayrid ledger has that land changing hands (zubayrid /ledger/2 and /6 are a contest).
   - Evidence: Second Fitna page on Marj Rahit names a clash, not a transfer; zubayrid /ledger/6 is contest_end 684/8.
   - Fix: Make /ledger/14 a contest_end with zubayrid-caliphate (it already has the matching contest in the Zubayrid file), or add the land to both 683 events.
6. [to do, not blocking] `/keyframe_review/6`: Egypt is drawn Umayyad from 684, while the Zubayrid 683-684 keyframe also holds it and the ledger moves it in 685.
   - Evidence: Abd Allah ibn al-Zubayr page: "in March 685, Ibn al-Zubayr lost ... Egypt to Marwan"; Umayyad page: "In 685, Marwan and Ibn Bahdal expelled the Zubayrid governor of Egypt".
   - Fix: Start Egypt in 685 (split the keyframe 684 / 685-691).
7. [to do, not blocking] `/ledger/30`: 705 gains the Armenian Highlands again (already gained from Byzantium in 692, /ledger/21, with no loss between), and names principality-of-iberia as counterpart for Armenia and Albania.
   - Evidence: Umayyad page: "By 705, Armenia was annexed by the caliphate".
   - Fix: Limit the 705 gain to Caucasian Iberia (and Albania if sourced), or add the intervening loss of Armenia (the 703 revolt) with its source.
8. [to do, not blocking] `/keyframe_review/3`: Marked ok, but the 666 shape (west edge 18.8 E) does not contain the Fezzan gained in 666 (/ledger/9, Germa 12.9 E).
   - Evidence: shapes.csv bbox of umayyad-caliphate_666; garamantes /ledger/2 dissolves to the Umayyads in 666.
   - Fix: Mark adjust and add the Fezzan (or treat 666 as a tribute raid and re-type the event).
9. [to do, not blocking] `(missing mirrors in the Maghreb)`: Neighbour dossiers name the Umayyads in events with no mirror here: kingdom-of-altava 708 dissolve (Oranais), emirate-of-nekor vassal 710-750, kingdom-of-the-aures 698 gain (the Kahina's victory) and 703 end (here 701), exarchate-of-africa 709 Ceuta, barghawata-conference 744 found (here Morocco is lost to nobody in 740).
   - Evidence: rev-check of history/polities/*.json, 2026-10-19.
   - Fix: Add a 708 gain of Oranais from kingdom-of-altava, a vassal pair with emirate-of-nekor (710-750), a 698 loss of Numidia and southern Tunisia to kingdom-of-the-aures before /ledger/28, and Ceuta 709 if a page dates it; leave the 701/703 and 740/744 disagreements in notes if pages differ.
10. [to do, not blocking] `/ledger/23`: The 693 gain from the Najdat omits Ta'if, which the Najdat dossier holds 689-693.
   - Evidence: najdat /keyframe_review/2 and /ledger/5.
   - Fix: Add place Ta'if 60 km to the region union.

Gaps for a gap-filler:
- `/ledger/12`: year Kusaila entered Kairouan (683, c=1) (try https://en.wikipedia.org/wiki/Kusaila)
- `/ledger/17`: year of the Cyprus condominium (688, c=1) (try https://en.wikipedia.org/wiki/Cyprus_in_the_Middle_Ages)
- `/ledger/19`: when Khorasan returned to Umayyad control after Ibn Khazim (691, c=1) (try https://en.wikipedia.org/wiki/Abd_Allah_ibn_Khazim_al-Sulami)
- `/ledger/23`: 693 is on the Najdat page ("defeated by the caliphate in 693, at the battle of Mushahhar"); cite it and raise to c=2 (try https://en.wikipedia.org/wiki/Najdat)
- `/ledger/71`: date of the Fihrid break-away in Ifriqiya (745, c=1) (try https://en.wikipedia.org/wiki/Abd_al-Rahman_ibn_Habib_al-Fihri)
- `/ledger/73`: dates of Rey and Nahavand in the Abbasid advance (748, c=1) (try https://en.wikipedia.org/wiki/Qahtaba_ibn_Shabib_al-Ta%27i)
- `/ledger/78`: status of al-Andalus 750-756 (c=1) (try https://en.wikipedia.org/wiki/Yusuf_ibn_Abd_al-Rahman_al-Fihri)
- `/ledger/77`: when Sindh passed to the Abbasids (750, c=1) (try https://en.wikipedia.org/wiki/Umayyad_campaigns_in_India)

Spot checks:
- `/ledger/15` W:Umayyad_Caliphate: confirmed: "In 685, Marwan and Ibn Bahdal expelled the Zubayrid governor of Egypt"
- `/ledger/18` W:Muslim_conquest_of_the_Maghreb: confirmed: "a Byzantine fleet landing in Cyrenaica in 690"; "Barqa had fallen out of Muslim control"
- `/ledger/29` W:Muslim_conquest_of_Transoxiana: confirmed: "Qutayba began his tenure by recovering Balkh in spring 705"
- `/ledger/54` W:Umayyad_campaigns_in_India: confirmed: timeline row 721 "Hullishah surrenders"; text has Junayd appointed in 723
- `/ledger/57` W:Muslim_conquest_of_Transoxiana: confirmed: Suluk "in 728 took Bukhara"
- `/ledger/66` W:Muslim_conquest_of_Transoxiana: confirmed: "Nasr recovered most of Transoxiana by 743"
- `/ledger/68` W:Umayyad_campaigns_in_India: confirmed: "The Arabs lost their conquests in Rajasthan and Gujarat by 743" (but no gain recorded)
- `/ledger/21` W:Umayyad_Caliphate: confirmed (year): "defeating the Byzantines at the Battle of Sebastopolis in 692"

## islamic-state-of-medina: thin

Valid and honest; its four checked dates (622 Hijra, Mecca December 629 - January 630, end of the Quraysh war, 8 June 632) are on the pages. Thin by design (no Cliopatria shape, 3 pages): the 630 keyframe jumps from Medina and Mecca to the whole Hejaz with only the Mecca event behind it, and Muhammad's authority beyond the Hejaz by 632 is not traced.

Area: infobox None km2 (None), Cliopatria None km2, ratio None. no area on the page and no Cliopatria row

Gaps for a gap-filler:
- `/keyframe_review/1`: Khaybar (628) and other Hejaz oases before 630; the 622-629 keyframe is Medina 60 km only (try https://en.wikipedia.org/wiki/Battle_of_Khaybar)
- `/keyframe_review/1`: Ta'if and Hunayn (630), Thaqif's submission (try https://en.wikipedia.org/wiki/Siege_of_Ta%27if)
- `/keyframe_review/1`: Tabuk (630) and the northern Hejaz chiefs who submitted (try https://en.wikipedia.org/wiki/Expedition_of_Tabuk)
- `/keyframe_review/1`: Year of Delegations (631): Yemen, Bahrain, Oman submissions, the extent at 632 (try https://en.wikipedia.org/wiki/Year_of_Delegations)

Spot checks:
- `/ledger/0` W:Muhammad_in_Medina: confirmed: "the Hijrah in 622"
- `/ledger/2` W:Conquest_of_Mecca: confirmed: infobox "December 629 - January 630"; "10 or 11 January 630"
- `/ledger/3` W:Conquest_of_Mecca: confirmed: "formally marked the end of the conflict between his followers and the Quraysh"
- `/ledger/4` W:Muhammad_in_Medina: confirmed: "He died on Monday, June 8, 632"

## zubayrid-caliphate: fail

Dates hold (Egypt March 685, Yemen 688, Ta'if 689, Maskin October 691, Mecca October/November 692). It fails on the mirror for Mukhtar: mukhtarid /ledger/0 takes Media and Azerbaijan from the Zubayrids in 685, but this dossier never holds or loses them, and its keyframes keep Iraq without the dependencies the pages give it ("most provinces"), leaving central Iran with nobody 683-691 next to the Umayyad 684-691 keyframe.

Area: infobox None km2 (None), Cliopatria None km2, ratio None. no area on the page and no Cliopatria row

Findings:
1. [blocking] `/keyframe_review/0 ... /5 with /ledger/9, /ledger/10, /ledger/14`: No loss of Media and Azerbaijan to Mukhtar in 685 (mirror of mukhtarid /ledger/0) and no regain in 687; the corrections hold Iraq (Mesopotamia) without the provinces governed from Kufa and Basra, although the Umayyad dossier drops them in 684.
   - Evidence: Abd Allah ibn al-Zubayr page: "Most of the Islamic provinces offered their allegiance, including Egypt, Kufa, Yemen..."; Mukhtar page: Mukhtar "controlled most of Iraq and its dependencies including Arminiya, Adharbayjan, Jibal and parts of the Jazira" after taking Kufa from the Zubayrid governor.
   - Fix: Add Iraq's dependencies (at least Jibal/Media and Azerbaijan; Khuzestan, Isfahan, Sistan if accepted) to the 683-684 correction; add a 685/10 loss of Media and Azerbaijan to mukhtarid-state-of-kufa, a 687/4 gain back (with mukhtarid widening its loss), and widen the 691/10 loss to the Umayyads accordingly. Keep it consistent with umayyad /ledger/13 and /ledger/20.
2. [to do, not blocking] `/ledger/17, /ledger/18`: The 692/10 loss and dissolve hand the whole Hejaz to the Umayyads, but the 691-692 correction excludes Ta'if (Najdat since 689).
   - Evidence: /keyframe_review/5 correction minus Ta'if; najdat /keyframe_review/2.
   - Fix: Use minus(region Hejaz, place Ta'if 60 km) for /ledger/17, /ledger/18 and /identity/successors/0/land.

Gaps for a gap-filler:
- `/ledger/0, /ledger/1, /ledger/2`: dates of Yemen, Fars/Kerman and the Qays of northern Syria joining (683, c=1) (try https://en.wikipedia.org/wiki/Abd_Allah_ibn_al-Zubayr)
- `/ledger/5, /ledger/13`: when Abd Allah ibn Khazim recognised Ibn al-Zubayr and how Khorasan ended (684-691, c=1) (try https://en.wikipedia.org/wiki/Abd_Allah_ibn_Khazim_al-Sulami)

Spot checks:
- `/ledger/8` W:Abd_Allah_ibn_al-Zubayr: confirmed: "in March 685, Ibn al-Zubayr lost the economically important province of Egypt to Marwan"
- `/ledger/11` W:Second_Fitna: confirmed: "captured Yemen and Hadhramawt in 688"
- `/ledger/12` W:Abd_Allah_ibn_al-Zubayr: confirmed: "in 689, they occupied Ta'if, Mecca's southern neighbour"
- `/ledger/14` W:Second_Fitna: confirmed: "defeated and killed at the Battle of Maskin in October 691"
- `/ledger/17` W:Abd_Allah_ibn_al-Zubayr: confirmed: infobox death "October/November 692"; Second Fitna "besieged Mecca in March 692"

## mukhtarid-state-of-kufa: fail

Dates hold (Kufa October 685, Khazir early August 686, Mukhtar killed 3 April 687). It fails because the land it holds is not handed on: the 685-687 keyframe includes Media and Azerbaijan, but the 687 loss, the dissolve and the successor land are Iraq without Basra only, and the 685 gain of Media and Azerbaijan has no mirror in the Zubayrid dossier.

Area: infobox None km2 (None), Cliopatria None km2, ratio None. no area on the page and no Cliopatria row

Findings:
1. [blocking] `/ledger/6, /ledger/8, /identity/successors/0/land`: The 687 loss, dissolve and successor land cover only Iraq without Basra, while /keyframe_review/0 holds Media and Iranian Azerbaijan to 687: that land passes to nobody.
   - Evidence: Research brief, table row 7 (Collapse and partition): "At the end the land passes to the successors with a caption". Mukhtar page: Mus'ab besieged the palace "for four months"; Mukhtar killed "On 3 April 687".
   - Fix: Give /ledger/6, /ledger/8 and the successor land the full keyframe region (the union in /keyframe_review/0/correction), with the matching Zubayrid gain; or drop Media and Azerbaijan from the keyframe and /ledger/0 if the dependencies are judged too vague to draw.
2. [blocking] `/ledger/0`: Gain of Media and Azerbaijan from zubayrid-caliphate with no mirror in the Zubayrid ledger.
   - Evidence: zubayrid ledger has no event for Media or Azerbaijan; Mukhtar page: "Iraq and its dependencies including Arminiya, Adharbayjan, Jibal" (undated).
   - Fix: Resolve together with the Zubayrid finding (Zubayrid adds the loss), or change the counterpart if the author decides the Zubayrids never governed them.

Gaps for a gap-filler:
- `/ledger/0`: when Mukhtar's authority reached the Jibal and Azerbaijan (685, c=1) (try https://en.wikipedia.org/wiki/Mukhtar_al-Thaqafi)

Spot checks:
- `/ledger/1` W:Mukhtar_al-Thaqafi: confirmed: "Mukhtar captured Kufa in October 685"
- `/ledger/4` W:Mukhtar_al-Thaqafi: confirmed: "The armies met at the banks of Khazir River in early August 686"
- `/ledger/6` W:Mukhtar_al-Thaqafi: confirmed: "On 3 April 687, Mukhtar came out of the palace ... and was killed fighting"
- `/ledger/0` W:Mukhtar_al-Thaqafi: confirmed (undated): "controlled most of Iraq and its dependencies including Arminiya, Adharbayjan, Jibal and parts of the Jazira"

## najdat-kharijite-emirate: pass

Could not break it: the founding (685), Yemen (688), Ta'if (689), Abu Fudayk's accession (691) and the defeat at Mushahhar (693) are on the pages; page disagreements (682 revolt, 687 Yemen, the holy villages) are in the notes. The missing mirror of its 685 founding is the Umayyad dossier's fault, listed there.

Area: infobox None km2 (None), Cliopatria None km2, ratio None. no area on the page and no Cliopatria row

Gaps for a gap-filler:
- `/ledger/1`: date of Bahrain and Oman (685, c=1) (try https://en.wikipedia.org/wiki/Najda_ibn_Amir_al-Hanafi)

Spot checks:
- `/ledger/0` W:Second_Fitna: confirmed: "Najda had established an independent state in Najd and Yamamah in 685"
- `/ledger/2` W:Second_Fitna: confirmed: "captured Yemen and Hadhramawt in 688" (the Najdat page has 687; disagreement in the author notes)
- `/ledger/3` W:Second_Fitna: confirmed: "occupied Ta'if in 689"
- `/ledger/5` W:Najdat: confirmed: "eventually defeated by the caliphate in 693, at the battle of Mushahhar"
- `/identity/rulers/1` W:Najdat: confirmed: "Abu Fudayk, murdered Najda himself in 691 and took his place"

## azariqa-kharijite-emirate: pass

Could not break it: Fars and Kerman taken from the Zubayrids in 685 and held until 698 are on the Second Fitna page, the end 698-699 on the Azariqa page; the 685/686 disagreement is in the notes. Rulers are empty although the page names leaders with partial dates (gap only).

Area: infobox None km2 (None), Cliopatria None km2, ratio None. no area on the page and no Cliopatria row

Gaps for a gap-filler:
- `/identity/rulers`: leaders with partial dates: Nafi ibn al-Azraq (killed early 685), Ubayd Allah ibn Mahuz (killed May 686 at Sillabra), Zubayr ibn Mahuz, Qatari ibn al-Fuja'a (to 698/699) (try https://en.wikipedia.org/wiki/Qatari_ibn_al-Fuja%27a)

Spot checks:
- `/ledger/0` W:Second_Fitna: confirmed: "had captured Fars and Kirman from the Zubayrids in 685"
- `/ledger/1` W:Second_Fitna: confirmed: "holding parts of Fars and Kirman until being defeated by ... al-Muhallab ibn Abi Sufra in 698"
- `/ledger/2` W:Azariqa: confirmed: "were subsequently destroyed in 698-699"

## Cross-dossier matrix (not matched only)

| event | mirror | status | note |
| --- | --- | --- | --- |
| rashidun-caliphate 633 gain Ridda rebels (apostate tribes) | - | exception | not a state; no dossier wanted |
| rashidun-caliphate 638 vassal_start Hormuzan (Ahvaz) | - | exception | a local ruler, no dossier |
| rashidun-caliphate 640 gain byzantine-empire | byzantine-empire 638 loss | mismatch | Jazira: Rashidun 640 vs Byzantine 638 (Upper Mesopotamia with Armenia) - two years apart, both c=2; Levant page has Raqqa 639-640. |
| rashidun-caliphate 640 vassal_end Hormuzan (Ahvaz) | - | exception | local ruler |
| rashidun-caliphate 643 gain sasanian-empire | - | missing | Kerman (Carmania) 643: no Sasanian loss of Kerman (sasanian-empire, group me-06) |
| rashidun-caliphate 644 gain sasanian-empire | - | missing | Transcaucasia 644: no Sasanian loss of the South Caucasus (me-06) |
| rashidun-caliphate 646 loss kingdom-of-armenia | - | exception | kingdom-of-armenia (eu-19) not written yet; but the Atropatene half of this loss is to Azerbaijani rebels, not the Armenian kingdom, and Armenia is never regained in the Rashidun ledger (see byzantine-empire 657 below) |
| rashidun-caliphate 647 gain byzantine-empire | byzantine-empire 644 loss | mismatch | Cyrenaica: Rashidun 647 (c=2, no year on its page) vs Byzantine 644 (643-644); Maghreb page: Barqa soon after 642, Tripoli around 643. Tripolitania half matches Byzantine 647. |
| rashidun-caliphate 649 gain byzantine-empire | byzantine-empire 653 loss | mismatch | Cyprus: Rashidun 649 (Levant page; Rashidun page 650) vs Byzantine 653 (Arab-Byzantine wars page). Page disagreement acknowledged on both sides; align or keep with notes. |
| rashidun-caliphate 651 gain sasanian-empire | sasanian-empire 651 dissolve | mismatch | Sistan: the Sasanian 651 loss/dissolve covers Khorasan only; neither side places Sistan |
| rashidun-caliphate 651 gain sasanian-empire | sasanian-empire 642 loss | mismatch | Rey: Sasanian loses Media in 642; Rashidun gains Rey from the Sasanians in 651 (page: siege of 651 after rebellion). Rashidun should make 651 a reconquest, not a Sasanian gain. |
| rashidun-caliphate 651 gain sasanian-empire | - | mismatch | Atropatene 651: lost by Rashidun in 646 to rebels, retaken 651; not a Sasanian loss in either dossier. Counterpart should be the rebels/nobody. |
| byzantine-empire 644 loss rashidun-caliphate | - | mismatch | byzantine-empire /ledger/13 Cyrenaica 644 vs Rashidun 647 (see above) |
| byzantine-empire 645 gain rashidun-caliphate | - | missing | byzantine-empire /ledger/14 Alexandria retaken 645 (c=3) and /ledger/15 lost 646: no mirror in Rashidun; the Muslim conquest of Egypt page (a Rashidun source) has it (infobox 645-646). |
| byzantine-empire 657 gain rashidun-caliphate | - | missing | byzantine-empire /ledger/20 Armenia returns to Byzantium 657: no Rashidun loss of Armenia (Rashidun has Armenia lost to kingdom-of-armenia in 646). |
| dabuyid-dynasty 642 found sasanian-empire | - | exception | founding by a Sasanian cadet; predecessor sasanian-empire. Sasanian ledger has no loss of Gilan/Tabaristan in 642 (me-06 may add one). |
| dabuyid-dynasty 760 loss abbasid-caliphate | - | exception | abbasid-caliphate is group me-08, not run yet |
| umayyad-caliphate 670 gain exarchate-of-africa | - | missing | exarchate-of-africa has no loss of Kairouan/the interior in 669-671 (group af-*) |
| umayyad-caliphate 674 vassal_start Bukhara | - | exception | Bukhara listed in counterparts_needing_dossiers (central Asia group) |
| umayyad-caliphate 683 loss zubayrid-caliphate | zubayrid-caliphate 683 gain | mismatch | Land: Zubayrid gains Hejaz, Iraq, Egypt, Yemen AND Fars and Kerman (zubayrid /ledger/1) in 683; the Umayyad loss lacks Fars and Kerman and any of the rest of Iran, Arminiya, the Jazira and eastern Arabia that the Umayyad 684 keyframe drops. |
| umayyad-caliphate 684 gain zubayrid-caliphate | zubayrid-caliphate 684 contest_end | mismatch | Northern Syria: Umayyad records a gain from the Zubayrids, but the Zubayrid side (and the Umayyad 683 loss) has only a contest there; make it a contest_end, or add the land to both 683 events. |
| najdat-kharijite-emirate 685 found umayyad-caliphate | - | missing | Najdat founded in Najd/Yamama (685) and gains Bahrain and Oman from the Umayyads (najdat /ledger/0-1); the Umayyad ledger has no loss of eastern Arabia (its 684 keyframe drops it silently). |
| umayyad-caliphate 690 loss byzantine-empire | - | missing | Cyrenaica 690 (c=3, confirmed on the Maghreb page): byzantine-empire has no gain of Cyrenaica (eu-05); the Umayyad ledger also never regains it although its 692 keyframe holds it |
| umayyad-caliphate 691 gain zubayrid-caliphate | zubayrid-caliphate 691 vassal_end | mismatch | Khorasan (c=1): the Zubayrids held it only as a vassal pair (Abd Allah ibn Khazim); acceptable as recorded but the gain is from Ibn Khazim, not the Zubayrid state |
| kingdom-of-the-aures 698 gain umayyad-caliphate | - | missing | Kahina defeats Hassan and takes Numidia and southern Tunisia (aures /ledger/5, c=2): no Umayyad loss |
| umayyad-caliphate 701 gain kingdom-of-the-aures | kingdom-of-the-aures 703 dissolve | mismatch | Kahina's defeat: Umayyad 701 (Maghreb page "around 701") vs Aures dissolve 703; two years apart |
| umayyad-caliphate 705 gain tokhara-yabghus | - | missing | Balkh / Lower Tokharistan spring 705 (c=3, confirmed): tokhara-yabghus has only the 710 loss |
| umayyad-caliphate 705 gain principality-of-iberia | - | exception | principality-of-iberia (eu-19) not written yet; note the Armenian Highlands are already gained in 692 (double gain) |
| umayyad-caliphate 708 gain nobody | - | exception | Berber tribes; but kingdom-of-altava /ledger/7 dissolves to the Umayyads in 708 (Oranais) and emirate-of-nekor /ledger/1 is an Umayyad vassal from 710: neither has a mirror in the Umayyad ledger |
| kingdom-of-altava 708 dissolve umayyad-caliphate | - | missing | Oranais to the Umayyads 708: no Umayyad event names Altava (Umayyad 708 gain is Morocco from nobody) |
| emirate-of-nekor 710 vassal_start umayyad-caliphate | - | missing | Nekor a client of the Umayyads 710-750: no vassal pair in the Umayyad ledger |
| exarchate-of-africa 709 dissolve umayyad-caliphate | - | missing | Ceuta 709: Umayyad ledger silent (author lists Ceuta as not reached) |
| umayyad-caliphate 709 vassal_end Bukhara | - | exception | central Asia group |
| umayyad-caliphate 709 gain Bukhara | - | exception | central Asia group |
| umayyad-caliphate 712 gain Samarkand (Sogdian ikhshid) | - | exception | central Asia group |
| umayyad-caliphate 712 gain Khwarazm (Khwarazmshah) | - | exception | central Asia group |
| umayyad-caliphate 713 gain Dahir's kingdom of Sindh | - | exception | brahman-dynasty-of-sindh, south Asia group |
| umayyad-caliphate 713 gain khazaria | - | missing | Derbent recovered 713/14 (c=2): khazaria (ia-01) has no loss of Derbent |
| umayyad-caliphate 715 loss Hindu kings of Sindh | - | exception | south Asia group |
| umayyad-caliphate 721 gain Hindu kings of Sindh | - | exception | south Asia group |
| umayyad-caliphate 740 loss nobody | - | exception | Berber revolt; barghawata-conference /ledger/0 is founded from umayyad-caliphate in 744 (Tamesna) - counterpart disagreement |
| umayyad-caliphate 743 gain turgesh | turgesh 743 contest_end | mismatch | Transoxiana recovered by Nasr (c=3, confirmed) but turgesh records only a contest_end in 743 (the Turgesh khaganate had collapsed after 738) |
| umayyad-caliphate 743 loss gurjara-pratihara-dynasty | gurjara-pratihara-dynasty 743 contest_end | mismatch | Gujarat and Rajasthan: the Umayyad loses land it never gained (723 is only a contest_start); gurjara records contest_end only |
| umayyad-caliphate 748 loss abbasid-caliphate | - | exception | me-08 not run |
| umayyad-caliphate 749 loss abbasid-caliphate | - | exception | me-08 not run |
| umayyad-caliphate 750 loss abbasid-caliphate | - | exception | me-08 not run (Sindh, Levant, Egypt) |
| umayyad-caliphate 750 loss Fihrid governors of al-Andalus | - | exception | fihrid-al-andalus listed in counterparts_needing_dossiers (eu-12) |
| byzantine-empire 672 loss umayyad-caliphate | - | missing | Cyzicus 672-678 (byzantine /ledger/23-24): Umayyad silent (author: siege of Constantinople not on the pages opened) |
| byzantine-empire 718 loss umayyad-caliphate | - | missing | Balearics and Ceuta 718 (byzantine c=1, page silent): no Umayyad event; Ceuta is 709 in the exarchate dossier |
| turk-shahis 684 occupation_start umayyad-caliphate | - | missing | Kabul valley 684-685 (turk-shahis /ledger/5-6): Umayyad silent, and in 684 Sistan/Khorasan are outside the Umayyad 684-691 keyframe |
| zubayrid-caliphate 684 vassal_start Abd Allah ibn Khazim | - | exception | khorasan-under-ibn-khazim in counterparts_needing_dossiers (low priority) |
| mukhtarid-state-of-kufa 685 gain zubayrid-caliphate | - | missing | Media and Azerbaijan (mukhtarid /ledger/0, c=1): the Zubayrid dossier never holds or loses them; and the Mukhtarid dissolve hands only Iraq-without-Basra on in 687 |
| zubayrid-caliphate 691 vassal_end Abd Allah ibn Khazim | - | exception |  |
| islamic-state-of-medina 630 gain Quraysh of Mecca | - | exception | a city, no dossier wanted |

48 further events matched their mirror within a year (see the JSON copy at history/notes/phase-b/reviews/me-07.json).

## Other notes

- No page failed to load. Not opened for this review (budget): Arab-Byzantine wars, Arab-Khazar wars, First Fitna, Umayyad conquest of Hispania, Abbasid Revolution, Muslim conquest of the Levant, Tabaristan, Gil Gavbara, Muhammad.
- Reviewer edit: history/polities/rashidun-caliphate.json /identity/predecessors/0/land region Arabia -> Hejaz; re-validated (0 errors, 0 warnings) and read back.
- The Second Fitna geography is one problem across three dossiers (umayyad /keyframe_review/6 and /ledger/13, zubayrid keyframes, mukhtarid dissolve): the author should fix them together so that Iran outside Fars, Kerman and Khorasan has a holder 683-691.
- Neighbour dossiers with events naming this batch and no mirror (their owners may prefer to change their side): byzantine-empire 644 Cyrenaica, 645-646 Alexandria, 653 Cyprus, 657 Armenia, 672-678 Cyzicus, 690 (no Cyrenaica gain), 718 Balearics; sasanian-empire (no Kerman 643, Transcaucasia 644, Sistan 651 losses; Media lost 642 vs Rey gained 651); exarchate-of-africa 670 Kairouan; khazaria 713 Derbent; tokhara-yabghus 705 Balkh; turgesh 743; kingdom-of-altava 708; kingdom-of-the-aures 698/703; emirate-of-nekor 710-750; turk-shahis 684-685 Kabul; barghawata-conference 744.
- Dossiers whose group has not run (counterpart exceptions): kingdom-of-armenia, principality-of-iberia, kingdom-of-lazica, balasagan (eu-19); abbasid-caliphate (me-08); aquitaine, kingdom-of-the-franks (eu-07); kingdom-of-asturias (eu-12); emirate-of-cordoba (no dossier yet).
- Author notes say the Dabuyid 755 keyframe was adjusted to exclude Gurgan; the dossier keeps the 755 shape unchanged (harmless, notes inaccurate).

Gazetteer names wanted (from the author, still open): Yamama (region, najdat-kharijite-emirate), Jibal (region, mukhtarid-state-of-kufa), Azerbaijan (historical, Atropatene) (region, mukhtarid-state-of-kufa), Siffin (place, rashidun-caliphate), Ascalon (place, rashidun-caliphate).
