# Review of batch eu-19-c (Caucasus, part c), 2026-10-31

Reviewer: adversarial review per history/briefs/reviewer-brief.md. Validator: 0 errors on all five dossiers before and after the reviewer's edits (warnings are counterpart slugs with no dossier yet and the unknown region 'Tao'). Neighbour ledgers read: byzantine-empire, eastern-roman-empire, umayyad-caliphate, abbasid-caliphate, sajid-dynasty, sallarid-dynasty, shaddadids, eldiguzids, great-seljuk-empire, timurid-empire, safavid-dynasty, jalayirid-sultanate, ilkhanate, khazaria, golden-horde, qara-qoyunlu, sasanian-empire. Not yet written: georgia, kingdom-of-georgia, kingdom-of-vaspurakan, kingdom-of-kakheti, kingdom-of-armenia, kingdom-of-kartli (eu-19 parts that have not run).

| slug | verdict |
| --- | --- |
| kingdom-of-lazica | thin |
| principality-of-iberia | pass |
| kingdom-of-the-iberians | thin |
| shirvan | thin |
| bagratid-armenia | fail |

## kingdom-of-lazica: thin

Area: Lazica infobox gives no area; Cliopatria 23424 km2.

Findings:

- `/identity` (for the author, not blocking). Same state as lazica (-63..545): same Wikipedia article (Lazica) and Wikidata Q136884; the 638 found event and the 546-637 gap are artefacts of Cliopatria's two rows. Evidence: Author's brief: one dossier under the earlier slug with both Names; the author could not because lazica belongs to another eu-19 part, and flagged it. Fix: Orchestrator: when lazica is written, merge this dossier into it (both Names in cliopatria_names, these 6 verdicts and 3 events), or keep it with a hand-over found event.

Gaps for a gap-filler:

- `/ledger/1`: 724 loss of the north-western strip to the Abasgians is Cliopatria's split only (confidence 1); no page dates it. Try https://en.wikipedia.org/wiki/Leon_I_of_Abkhazia
- `/ledger/0`: 638 found at confidence 1: the Lazica page is silent on 638; the dependency status 638-697 (incorporated as a Byzantine province, rulers styled Patricius) and Arab suzerainty from c. 696/697 are recorded in no suzerain dossier. Try https://en.wikipedia.org/wiki/Arab_conquest_of_Armenia
- `/identity/end`: Lazica infobox: Disestablished 697; the dossier runs to 777 on Cliopatria and 'Leon II exploited this dynastic union to acquire Lazica in the 770s' (Kingdom of Abkhazia). Acknowledged in the note; who held Lazica 697-777 needs a page. Try https://en.wikipedia.org/wiki/Kingdom_of_Abkhazia

Spot checks:

- `/ledger/2` https://en.wikipedia.org/wiki/Kingdom_of_Abkhazia: confirmed ('Leon II exploited this dynastic union to acquire Lazica in the 770s'; 'Towards circa 778')
- `/ledger/1` https://en.wikipedia.org/wiki/Kingdom_of_Abkhazia: confirmed silent on 724, as the confidence-1 note says
- `/ledger/0` https://en.wikipedia.org/wiki/Lazica: confirmed: page silent on 638; the 620s Heraclius and patricius sentences are on the page
- `/identity/capitals/0` https://en.wikipedia.org/wiki/Lazica: confirmed (Capital: Archaeopolis; inside the 638 shape bbox)

## principality-of-iberia: pass

Tried and could not break: years, capitals, dynastic renames, the 724/736 Tbilisi sequence and the 732 adjust all match the pages. Open points belong to neighbours: Cliopatria georgia_638 (638-646, 34,660 km2, same bbox as principality-of-iberia_682) is this principality's Kartli under the Georgia row, so the georgia split must give it here; umayyad-caliphate /ledger/39 claims a direct 705 gain of Iberia that the Arab-Khazar wars page contradicts; Kartli after the 813 dissolve is received by no dossier (author flagged; listed under kingdom-of-the-iberians thin).

Area: no infobox area; Cliopatria 34636 km2.

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Principality_of_Iberia: confirmed ('in 588, sent his protégé, Guaram I')
- `/ledger/2` https://en.wikipedia.org/wiki/Arab%E2%80%93Khazar_wars: confirmed ('In 724, al-Jarrah captured Tiflis and brought Caucasian Iberia ... under Muslim suzerainty')
- `/ledger/4` https://en.wikipedia.org/wiki/Emirate_of_Tbilisi: confirmed (735 in text, 'Established: 736' in infobox)
- `/ledger/6` https://en.wikipedia.org/wiki/Principality_of_Iberia: confirmed (Nersianids c. 748 - 779/80)
- `/ledger/3,/ledger/7` https://en.wikipedia.org/wiki/Principality_of_Iberia: confirmed (infobox: Uplistsikhe c. 736-813, Artanuji c. 813-888)

## kingdom-of-the-iberians: thin

Area: no infobox area; Cliopatria 24615 km2.

Findings:

- `/keyframe_review/0 and /ledger/0` (for the author, not blocking). The 813 keyframe and found region are Artvin only (Klarjeti, about 7,400 km2); the next keyframe (814) is Cliopatria's 24,352 km2 Tao-Klarjeti-Javakheti shape, and no ledger event explains the jump. Evidence: shapes.csv kingdom-of-the-iberians_814 24,351.7 km2; abbasid-caliphate /ledger/18 records an 814 loss to kingdom-of-the-iberians that has no mirror here; the Principality page has the Bagratids acting 'from their base in the region of Tao-Klarjeti'. Fix: Either make the 813 keyframe correction and the found region {cliopatria: Kingdom of the Iberians, year: 814}, or add an 814 gain from abbasid-caliphate (confidence 1) of the 814 shape minus Artvin.
- `/ledger/5` (for the author, not blocking). Phasiane, gained in /ledger/4 (c. 952), is never lost: the 1001 loss names Tao only. Evidence: byzantine-empire /ledger/83: 'In 1001, after the death of David of Tao, Basil inherited Tao, Phasiane and Speri'; David III of Tao page: the Upper Lands granted to David (Theodosiopolis, Phasiane) were for life. Fix: Region of the 1001 loss: {union: [{region: Tao}, {lon: 41.68, lat: 39.99, km: 30}]}, or a separate 1001 loss of Phasiane to byzantine-empire.

Gaps for a gap-filler:

- `/keyframe_review/5`: Kartli under Adarnase IV 888-904 ('Adarnase was dispossessed by Constantine III in 904', Kingdom page) and under Gurgen and Bagrat III 976-1008 are drawn by no dossier of this batch (author flagged; Cliopatria puts Kartli in its Georgia row). Try https://en.wikipedia.org/wiki/Adarnase_IV_of_Iberia
- `/ledger/0`: Who held Kartli (outside Tbilisi) 814-887 after principality-of-iberia's 813 dissolve, whose land this dossier does not receive. Try https://en.wikipedia.org/wiki/Bagrat_I_of_Iberia
- `/ledger/2`: 854 contest_end is bridging (confidence 1): the page says only 'for a brief time'. Try https://en.wikipedia.org/wiki/Bagrat_I_of_Iberia
- `/ledger (903)`: bagratid-armenia /ledger/5 annexes Klarjeti (Artvin) and Ardahan in 903; this dossier records no 903 loss. Resolve together with that dossier's fix. Try https://en.wikipedia.org/wiki/Smbat_I_of_Armenia

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Kingdom_of_the_Iberians: confirmed ('In 813, ... Ashot I ... established himself in his patrimonial Duchy of Klarjeti')
- `/ledger/1` https://en.wikipedia.org/wiki/Kingdom_of_the_Iberians: confirmed ('In 853, now supporting Bugha al-Kabir, Bagrat regained central Iberia, but only for a brief time')
- `/ledger/3` https://en.wikipedia.org/wiki/Kingdom_of_the_Iberians: confirmed (government 'Principality (c. 813-888); Feudal Monarchy (888-1008)')
- `/ledger/4` https://en.wikipedia.org/wiki/Kingdom_of_the_Iberians: confirmed ('He also received Phasiane from the Byzantine emperor in c. 952', Ashot II)
- `/ledger/5` https://en.wikipedia.org/wiki/David_III_of_Tao: confirmed ('murdered by his nobles early in 1000 or 1001'; Bagrat 'had to recognize the new borders')

## shirvan: thin

Area: Shirvanshah infobox garbled, no area; Shirvan page has no infobox. shirvan_825 (113,084 km2, 2.7 x the 866 shape) is already marked wrong.; Cliopatria 41531 km2.

Findings:

- `/ledger/8/note and /keyframe_review/20/note` (applied by the reviewer). The quote for 1405 was a paraphrase in quotation marks ('Ibrahim then declared independence and seized Ganja and Karabakh'). Evidence: Ibrahim I of Shirvan page: 'Ibrahim used the death of Timur as an opportunity to declare independence and seize Ganja and Karabakh.' Fix: Quote replaced with the page wording, marked [quote corrected to the page wording, reviewer eu-19-c, 2026-10-31]; validated 0 errors.
- `/keyframe_review/17` (for the author, not blocking). Derbent, added in shirvan_1201 and shirvan_1227, drops out in the new 1236 keyframe (the bare 1227 shape) with no loss event; later the Ibrahim I page has him recover 'the borders of his state as far as Derbent in north', with no gain event and no Derbent in the 1405/1415 keyframes (north edge 41.98N, Derbent 42.06N). Evidence: Rule 4: a change between keyframes needs a ledger event; Ibrahim I page sentence quoted. Fix: Add a loss of Derbent c. 1236-1239 (confidence 1, Mongols, page silent) or keep Derbent in the 1236 correction; add a gain of Derbent under Ibrahim I (confidence 2, 1405 or the reign) or say in the 1415 note why it is left out.
- `/keyframe_review/0/correction` (for the author, not blocking). Verdict wrong, but the correction is the 866 shape while its text says to draw nothing for 825-839. Evidence: The schema reads the correction as the shape as it should be; only the start of 861 keeps it from being drawn. Fix: Say in the note that the start year clips it, or use a correction that cannot be read as land for 825-839.

Gaps for a gap-filler:

- `/keyframe_review/2`: The 866-1084 shapes reach 45.8E toward Ganja, which shaddadids holds from 951 (Ganja annexed by the Seljuks 1075): a possible overlap no page resolves. Try https://en.wikipedia.org/wiki/Shaddadids
- `/keyframe_review/12`: Reading of the 1126 piece as the Georgian-annexed west inverts Cliopatria, whose kingdom-of-georgia_1126 (197,402 km2, east to 50.25E) also covers eastern Shirvan; the page supports 'annexed the western Shirvan' and 'left the eastern Shirvan to ... Manuchihr III as a Georgian protectorate'. Needs gazetteer cells and the kingdom-of-georgia dossier to agree (author flagged). Try https://en.wikipedia.org/wiki/David_IV_of_Georgia
- `/keyframe_review/17`: 1236-1343 carried at confidence 1; the Mongol conquest of Shirvan and Derbent is on no page opened. Try https://en.wikipedia.org/wiki/Derbent
- `/ledger/10`: 1501 contest_end bridging (confidence 1). Try https://en.wikipedia.org/wiki/Ismail_I
- `/ledger/5`: 1191 capital move bridging (confidence 1): the page ties it to Akhsitan I and Qizil Arslan's seizure of Shamakhi (eldiguzids /ledger/7 dates the invasion 1191). Try https://en.wikipedia.org/wiki/Akhsitan_I

Spot checks:

- `/ledger/0` https://en.wikipedia.org/wiki/Shirvanshah: confirmed (Haytham ibn Khalid, 861)
- `/ledger/1` https://en.wikipedia.org/wiki/Georgian%E2%80%93Seljuk_wars: confirmed ('In June 1123, a month after the Seljuk defeat, David IV invaded Shirvan')
- `/ledger/2` https://en.wikipedia.org/wiki/Georgian%E2%80%93Seljuk_wars: confirmed (September 1124; 'annexed the western Shirvan, handing its government over to Mtsignobartukhutsesi Simon')
- `/ledger/4` https://en.wikipedia.org/wiki/Georgian%E2%80%93Seljuk_wars: confirmed ('This probably happened in 1129 or 1130, when Demetrius restored the Shirvanshahs')
- `/ledger/6` https://en.wikipedia.org/wiki/Shirvanshah: confirmed ('At the start of the 13th century, the Shirvanshahs conquered Darband')
- `/ledger/7` https://en.wikipedia.org/wiki/Shirvanshah: confirmed (Hushang killed 1382; Ibrahim I starts the Darbandid line)
- `/ledger/8` https://en.wikipedia.org/wiki/Ibrahim_I_of_Shirvan: confirmed; quote corrected to the page wording
- `/ledger/11` https://en.wikipedia.org/wiki/Shirvanshah: confirmed ('This ended in 1538 when Shah Tahmasp I ... dismissed Shirvanshah Shahrukh')

## bagratid-armenia: fail

Area: Bagratid Armenia infobox gives no area; Cliopatria 99224 km2.

Findings:

- `/ledger/5` (BLOCKING, for the author). The 903 gain of Ardahan and Artvin (Klarjeti) double-claims the found region and core of kingdom-of-the-iberians (813-1008), which records no 903 loss; the gain has no end and no keyframe trace although it adds about 12,000 km2 to a 58,000-98,000 km2 shape. Evidence: Smbat I page: 'In 903, the Abkhazians began raiding Gugark and Iberia' and Smbat 'annexed several Abkhazian districts to his kingdom, including Klarjeti and Ardahan' (no year for the annexation); kingdom-of-the-iberians /ledger/0 region {admin1: Artvin}; the note acknowledges the overlap but does not resolve it. Fix: Resolve with kingdom-of-the-iberians: keep Ardahan (and Gugark) with an end (a loss by 914 at confidence 1, or whatever a page gives) and either drop Artvin or record it as a gain from kingdom-of-the-iberians with a mirror loss there; mark the 898/908/911 keyframe adjust if the land stays.
- `/ledger (1022)` (BLOCKING, for the author). Missing event: the 1022 loss of Dvin to the Shaddadids. Evidence: shaddadids /ledger/3 (confidence 3): '1022: Fadl I took Dvin from the Armenian Bagratids'. Also Smbat I page: 'In 901, ... Yusuf, who invaded Armenia and captured Dvin' (no event; mentioned only in the 892 note). Fix: Add 1022 loss {place: Artashat, km: 30, text: Dvin} to shaddadids (source Shaddadids page) and a 901 loss/recovery pair or a note saying why not; check the 1028 shape cut against it.
- `/ledger/8` (for the author, not blocking). 909 is recorded as a contest only, but the Sajid side has a 909 gain of Nakhchivan and Syunik from bagratid-armenia. Evidence: sajid-dynasty /ledger/2 (confidence 3): 'In 909 Yusuf took Nakhichevan and, together with Gagik, gained control of Siunikh'; this dossier regained Nakhchivan in 904 (/ledger/6) and never loses it. Fix: Add a 909 loss of Nakhchivan to sajid-dynasty (and Syunik's vassal_end if it applies) or explain in the note why the land stays Bagratid.
- `/keyframe_review/0 and /ledger/0` (for the author, not blocking). The 885 keyframe is an 80 km radius around Ani (about 20,000 km2); the 886 Cliopatria shape is 99,224 km2 (factor 5) with no ledger event between them. Evidence: shapes.csv bagratid-armenia_886; abbasid-caliphate /ledger/40 has an 886 loss to bagratid-armenia waiting for a mirror. Fix: Make the found region and the 885 correction the 886 shape, or add an 886 gain from abbasid-caliphate (confidence 1).
- `/ledger (c. 963)` (for the author, not blocking). Missing: the Kars (Vanand) kingdom under Mushegh I, a Bagratid sub-kingdom from c. 963. Evidence: Bagratid Armenia page: Ashot III 'had sent his brother Mushegh I to rule in Kars (Vanand) and had allowed him to use the title of king' (no year). Fix: Add a split or vassal_start kingdom-of-kars c. 963 (confidence 1-2) or say in the 947 keyframe note why it is left out.
- `/ledger/14/confidence` (applied by the reviewer). 988 vassal_start of Syunik at confidence 3 with no year on the page. Evidence: Kingdom of Syunik page: 'Abu-l-Haija Ravwadyan died in 988.' ends one paragraph; the next begins 'After the death of Abu al-Haij, Smbat I Sahakyan recognized the supreme authority of King Smbat II' with no year. Fix: Confidence lowered to 2 with a bracketed reviewer note; validated 0 errors.

Gaps for a gap-filler:

- `/ledger/16`: 1000 loss of the western strip to Byzantium is Cliopatria's redrawing (confidence 1); byzantine-empire has no matching event (its 1001 gain is from 'David III of Tao'). Try https://en.wikipedia.org/wiki/Basil_II
- `/ledger/17`: 1028 loss of the east and south (26 percent) attributed to Syunik at confidence 1; the 1020/1021 division between Hovhannes-Smbat and Ashot IV and the 1022 loss of Dvin are the likelier causes. Try https://en.wikipedia.org/wiki/Hovhannes-Smbat_III
- `/ledger/1`: 885 vassal_start of Syunik bridging (the Syunik page has 'in 885, Syunik became part of the administrative territory of the emirate'). Try https://en.wikipedia.org/wiki/Kingdom_of_Syunik
- `/ledger/15`: 989 gain of Vayots Dzor dated to Gagik I's accession (confidence 1). Try https://en.wikipedia.org/wiki/Gagik_I_of_Armenia
- `/ledger/19`: 1045 vassal_end of Syunik bridging (confidence 1). Try https://en.wikipedia.org/wiki/Kingdom_of_Syunik

Spot checks:

- `/ledger/3` https://en.wikipedia.org/wiki/Bagratid_Armenia: confirmed ('on April 21, 892, he recaptured the historic city of Dvin from the Arabs')
- `/ledger/4` https://en.wikipedia.org/wiki/Smbat_I_of_Armenia: confirmed ('In 902, King Smbat I granted Nakhchavan to his maternal cousin Ashot Artsruni')
- `/ledger/5` https://en.wikipedia.org/wiki/Smbat_I_of_Armenia: confirmed at confidence 2 (903 raids dated; annexation of Klarjeti and Ardahan undated)
- `/ledger/6` https://en.wikipedia.org/wiki/Smbat_I_of_Armenia: confirmed ('after Ashot's death in 904, the Armenian king took Nakhichevan away from Vaspurakan')
- `/ledger/7` https://en.wikipedia.org/wiki/Bagratid_Armenia: confirmed (Yusuf 'awarding Gagik a crown in 908')
- `/ledger/8` https://en.wikipedia.org/wiki/Smbat_I_of_Armenia: confirmed ('In 909, Yusuf gathered a large army and launched a campaign against Armenia')
- `/ledger/13` https://en.wikipedia.org/wiki/Kingdom_of_Syunik: confirmed (987, 'proclaimed a separate kingdom from the Bagratids')
- `/ledger/14` https://en.wikipedia.org/wiki/Kingdom_of_Syunik: year relative only ('After the death of Abu al-Haij', who died 988): confidence lowered to 2
- `/ledger/20` https://en.wikipedia.org/wiki/Bagratid_Armenia: confirmed ('surrendered Ani to the Byzantines in 1045')

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| kingdom-of-lazica 724 loss (kingdom-of-abkhazia) | kingdom-of-abkhazia   | exception | No dossier yet; listed in the author's counterparts_needing_dossiers (Cliopatria's Georgia row 724-1008). |
| kingdom-of-lazica 777 dissolve (kingdom-of-abkhazia) | kingdom-of-abkhazia   | exception | As above. |
| kingdom-of-lazica 638 found (lazica) | byzantine-empire   | missing | Lazica was a Byzantine dependency/province 638-c.697 and acknowledged Arab suzerainty c. 696/697 (Lazica page); byzantine-empire (eu-05) and umayyad-caliphate (me-07) record no vassal_start kingdom-of-lazica. eastern-roman-empire /ledger/88 opens a vassal_start lazica in 626 that byzantine-empire does not continue. |
| principality-of-iberia 724 contest_start (umayyad-caliphate) | umayyad-caliphate 705 gain | mismatch | umayyad-caliphate /ledger/39 has a direct 705 gain of Caucasian Iberia and Albania from principality-of-iberia; this dossier keeps Kartli to 813 with Tbilisi contested 724-736, and the Arab-Khazar wars page has Iberia only under 'Muslim suzerainty' from 724 and the western South Caucasus 'free from direct control' after 705. Route to me-07: turn the 705 gain into a vassal_start (Iberia) and add the 736 gain of Tbilisi. |
| principality-of-iberia 736 loss (umayyad-caliphate) | umayyad-caliphate   | missing | No 735/736 gain of Tbilisi in umayyad-caliphate (me-07). |
| principality-of-iberia 813 dissolve (kingdom-of-the-iberians) | kingdom-of-the-iberians 813 found | mismatch | Years match; land does not: the dissolve hands Kartli (minus Tbilisi) to kingdom-of-the-iberians, whose found region is Artvin only. Kartli 814-887 is drawn by no dossier (both sides flag it). |
| principality-of-iberia 588 found (sasanian-empire) | georgia 638  | mismatch | Cliopatria georgia_638 (638-646, 34,660 km2) has the same bbox as principality-of-iberia_682 and lies inside this dossier's new 588-681 keyframe: the georgia split (eu-19, not run) must assign that shape to principality-of-iberia. |
| kingdom-of-the-iberians 813 found (principality-of-iberia) | abbasid-caliphate 814 loss | mismatch | abbasid-caliphate /ledger/18 loses the 814 shape cells to kingdom-of-the-iberians; this dossier has no 814 gain (its 813 keyframe is Artvin only). See the fix on /keyframe_review/0. |
| kingdom-of-the-iberians 853 contest_start (emirate-of-tbilisi) | emirate-of-tbilisi   | exception | No dossier yet; listed (eu-19-x). |
| kingdom-of-the-iberians 952 gain (byzantine-empire) | byzantine-empire   | missing | byzantine-empire (eu-05) has no c. 952 loss of Phasiane to the Iberians. |
| kingdom-of-the-iberians 1001 loss (byzantine-empire) | byzantine-empire 1001 gain | matched | byzantine-empire /ledger/83 gains 'Tao, Phasiane and Speri' with counterpart string 'David III of Tao' (should be the slug kingdom-of-the-iberians); land differs by Phasiane (fix listed here). |
| kingdom-of-the-iberians 1008 dissolve (kingdom-of-georgia) | kingdom-of-georgia   | exception | kingdom-of-georgia is eu-19 and not written yet. |
| bagratid-armenia 885 found (abbasid-caliphate) | abbasid-caliphate 886 loss | matched | abbasid-caliphate /ledger/40 (886, confidence 1). Land: the Abbasid side loses the whole 886 shape while the found region is an 80 km radius (fix listed). |
| bagratid-armenia 892 gain (abbasid-caliphate) | abbasid-caliphate   | missing | No 892 loss of Dvin in abbasid-caliphate (me-08). |
| bagratid-armenia 902 loss (kingdom-of-vaspurakan) | kingdom-of-vaspurakan   | exception | kingdom-of-vaspurakan is eu-19 and not written yet (same for the 904 gain and 908 loss). |
| bagratid-armenia 903 gain (kingdom-of-abkhazia) | kingdom-of-the-iberians   | mismatch | Counterpart kingdom-of-abkhazia has no dossier (listed), but the land includes Artvin (Klarjeti), the found region of kingdom-of-the-iberians, which records no loss. Blocking fix on bagratid-armenia /ledger/5. |
| bagratid-armenia 909 contest_start (sajid-dynasty) | sajid-dynasty 909 gain | mismatch | sajid-dynasty /ledger/2 (confidence 3) gains Nakhchivan and Syunik from bagratid-armenia in 909; this dossier has a contest only (909-914). |
| shaddadids 1022 gain (bagratid-armenia) | bagratid-armenia   | missing | shaddadids /ledger/3 (confidence 3) takes Dvin from the Bagratids in 1022; no loss in bagratid-armenia (fix listed). |
| bagratid-armenia 1000 loss (byzantine-empire) | byzantine-empire 1001 gain | mismatch | byzantine-empire /ledger/83 gains Tao from 'David III of Tao', not from bagratid-armenia; this loss is Cliopatria's redrawing at confidence 1. |
| bagratid-armenia 1028 loss (kingdom-of-syunik) | kingdom-of-syunik   | exception | No dossier yet; listed (eu-19-x). Same for the 885/987/988/1045 Syunik vassal events and 989 gain, and the Tashir-Dzoraget vassal events (979, 1045). |
| bagratid-armenia 1045 dissolve (byzantine-empire) | byzantine-empire 1045 gain | matched | byzantine-empire /ledger/101. |
| shirvan 1123 contest_start (kingdom-of-georgia) | kingdom-of-georgia   | exception | kingdom-of-georgia is eu-19 and not written yet (also the 1124 loss and 1130 gain). Its author must draw eastern Shirvan 1124-1129/30 as a protectorate (vassal_start shirvan), not as the direct land Cliopatria's kingdom-of-georgia_1126 shape shows. |
| shirvan 1201 gain (Maliks of Darband) | maliks-of-darband   | exception | No dossier; listed by the author (eu-19-x). |
| shirvan 1405 gain (timurid-empire) | timurid-empire 1405 loss | mismatch | timurid-empire /ledger/19 loses Nakhchivan and Ganja to kingdom-of-georgia in 1405; this dossier has Ibrahim I seize Ganja and Karabakh (Ibrahim I page, confirmed). Route to the timurid-empire author: Ganja to shirvan, or both. |
| shirvan 1500 contest_start (safavid-dynasty) | safavid-dynasty 1501 vassal_start | mismatch | safavid-dynasty records a 1501 vassal_start shirvan but no December 1500 contest (Battle of Jabani). |
| shirvan 1538 dissolve (safavid-dynasty) | safavid-dynasty 1539 gain | matched | safavid-dynasty /ledger/18 (1539, confidence 1): within one year. |
| sajid-dynasty 909 vassal_start (shirvan) | shirvan   | exception | Vassal events belong to the suzerain's dossier (schema: counterpart is the vassal); likewise sallarid-dynasty 942-979, eldiguzids 1191-1195, jalayirid-sultanate 1364-1374 and safavid-dynasty 1501-1539. No Seljuk (1066/67 tribute), Mongol, Ilkhanid or Timurid (1386-1405) vassal_start shirvan exists yet in those suzerains' dossiers. |

## Gazetteer names needed

- Tao (region), used in kingdom-of-the-iberians
- Klarjeti (region), used in kingdom-of-the-iberians
- Phasiane (place), used in kingdom-of-the-iberians
- Dvin (place), used in bagratid-armenia

## Problems

- An earlier, cut-short review run of eu-19-c had already edited kingdom-of-the-iberians and shirvan on 2026-10-25 (notes marked '[quote corrected to the page wording, reviewer eu-19-c]') without saving a report; I kept those edits after re-checking the Georgian-Seljuk wars, Shirvanshah, Kingdom of the Iberians and David III of Tao quotes myself.
- Network-mount stale read: my second edit of shirvan.json read the file at its pre-edit length and wrote it back 161 bytes short (invalid JSON for a few minutes). I restored the lost tail of the notes string from the author's scratch copy /tmp/claude-0/work/research-eu-19-c/shirvan.json (byte-exact, 161 bytes), validated (0 errors) and read it back after 10 s (30,169 bytes). Agents editing a file twice in quick succession on the mount should re-check its length.
- Verdict usage: 'fix'-type findings with applied:false and blocking:false are author follow-ups that do not on their own fail the dossier; bagratid-armenia fails on two blocking findings (903 double-claim of Klarjeti with kingdom-of-the-iberians; missing 1022 Dvin loss mirrored at confidence 3 by shaddadids).
- kingdom-of-lazica duplicates lazica (Wikidata Q136884, same article): the author could not merge because lazica belongs to another eu-19 part; the orchestrator should merge them when lazica is written.
- Neighbour dossiers not yet written (eu-19 parts that have not run, counted as exceptions): georgia, kingdom-of-georgia, kingdom-of-vaspurakan, kingdom-of-kakheti, kingdom-of-armenia, kingdom-of-kartli; also kingdom-of-abkhazia, emirate-of-tbilisi, kingdom-of-syunik, kingdom-of-tashir-dzoraget (author's counterparts_needing_dossiers).
- Routing for the georgia split: Cliopatria georgia_567 (567-576) is Lazica and georgia_638 (638-646, 34,660 km2) is the Principality of Iberia's Kartli (same bbox as principality-of-iberia_682).
- None of the five Wikipedia articles (Lazica, Principality of Iberia, Kingdom of the Iberians, Shirvanshah/Shirvan, Bagratid Armenia) gives an infobox area; area checks are recorded as not possible.
- Pages that loaded: Lazica, Kingdom of Abkhazia, Principality of Iberia, Arab-Khazar wars, Emirate of Tbilisi, Kingdom of the Iberians, David III of Tao, Bagratid Armenia, Smbat I of Armenia, Kingdom of Syunik, Shirvanshah, Shirvan, Ibrahim I of Shirvan, Georgian-Seljuk wars. None failed.
