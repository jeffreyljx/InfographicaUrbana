# Review of batch sa-03-g (Phase B), 2026-10-19

Reviewer: adversarial review per history/briefs/reviewer-brief.md, with the orchestrator's adjustments: page budget, 4-6 spot checks per dossier, and small fixes applied by the reviewer. The machine copy is history/notes/phase-b/reviews/sa-03-g.json.

Validator (--resolve): all six dossiers are valid with 0 errors. The only warnings are counterpart slugs with no dossier (suryavamsha-dynasty, varman-dynasty-of-east-bengal, deva-dynasty).

## Verdicts

- **lohara-dynasty**: fail
- **eastern-ganga-kingdom**: fail
- **kingdom-of-polonnaruwa**: fix
- **sena-dynasty**: fail
- **gahadavala-dynasty**: fail
- **hoysala-kingdom**: fail

## lohara-dynasty (fail)

Area: The Lohara page has no area. Cliopatria's 1003 shape is 174,918 km2 and misses the Valley; the dossier's correction is 245 cells (about 62,000 km2), explained in each keyframe note. The only km2 figure on the pages is the Sultanate's 222,236 km2 for 1342, set against the dossier's 1294 correction of about 80,000 km2 (see fixes).

Findings:

- `/identity` [blocking]: The dossier is a dynasty-period duplicate of kashmir.json: same land (Kashmir Valley plus the Jammu hills), same years (1003-1320) and the same events (1015-1021 Lohkot sieges, 1056 loss, 1152 and 1210 gains, the 1320 raid), which kashmir.json already carries after its 1003 'rename' to the Lohara dynasty (kashmir /ledger/14).
  - Evidence: Research brief section 6: one dossier per state, a dynasty change is a rename event, and two Cliopatria rows for one state get one dossier under the earlier slug with both Names. The author's notes say the same ('draw ONE of kashmir / utpala-dynasty / lohara-dynasty for 1003-1320, or the Valley is painted twice').
  - Fix: Orchestrator decision needed, since kashmir.json belongs to another sa-03 part: add 'Lohara Dynasty' to kashmir.json cliopatria_names, move these 17 keyframe verdicts and the 1089/1101/1111 Lohara-principality events there, and retire lohara-dynasty.json.
- `/identity/end, /ledger/13` [blocking]: The dossier ends in 1320 with a dissolve to kashmiri-sultanate. kashmir.json treats 1320 as a rename (Rinchan), brings the Lohara line back in 1323 (kashmir /ledger/23) and dissolves only in 1339.
  - Evidence: Kashmir Sultanate infobox: 'Lohara Interruption: 1323–1339'. Lohara page: Rinchan 'claimed the throne for himself in 1320' and reigned until 1323.
  - Fix: Settled by the merge. If the dossier is kept, end it to match kashmir.json, or say why 1320 is the end.
- `/ledger (missing, c. 1235)` [blocking]: No vassal event for the Mongol dependency. The author lists it only as a mirror that mongol-empire should carry, and mongol-empire.json has no Kashmir event either.
  - Evidence: Kashmir Sultanate page: 'Unable to fend off the invasions this time, Kashmir became a Mongol dependency some time after 1235.'
  - Fix: Add vassal_start c. 1235 (counterpart mongol-empire, region Kashmir Valley, confidence 1, source Kashmir_Sultanate), with a vassal_end bridged to 1320 or later at confidence 1; carry it into kashmir.json on the merge.
- `/ledger/6, /ledger/7, /ledger/8` [not blocking, for the author]: The 1089 gain, 1101 split and 1111 merge name 'Lohara principality'. It has no dossier, is not in counterparts_needing_dossiers, and kashmir.json has none of the three events.
  - Evidence: Lohara page: Utkarsa's accession 'came the kingdom's reunification with Lohara'; 'again split at the time of Uccala's accession'; 'The downfall of Uccala came in December 1111'.
  - Fix: On the merge, move the three events into kashmir.json and either list the Lohara principality (Poonch) as a counterpart needing a dossier or record the events as internal (no counterpart).
- `/keyframe_review/16/note` [not blocking, for the author]: The note compares the Sultanate infobox (222,236 km2, 1342) only with Cliopatria's Kashmir row (201,709 km2). The dossier's own correction is 318 cells, about 80,000 km2, a ratio of 2.8.
  - Evidence: Kashmir Sultanate infobox: '1342: 222,236 km2'. The gazetteer resolves the 1294 correction to 318 cells.
  - Fix: Say in the note that the drawn shape is about a third of the 1342 infobox figure and why (the infobox belongs to the Sultanate and includes the northern hill states).

Thin (gap-filler):

- `/ledger/5, /ledger/9, /ledger/10`: Confidence-1 events that only mirror Cliopatria's Kashmir-row steps (1056, 1152, 1210). The page is silent on all three. (try https://en.wikipedia.org/wiki/Rajatarangini)
- `/ledger/6`: The boundary of the Lohara principality, given only as a 50 km disc at Poonch. (try https://en.wikipedia.org/wiki/Poonch_district)

Spot checks:

- `/ledger/2`: confirmed (https://en.wikipedia.org/wiki/Siege_of_Lohkot_(1015)): Mahmud 'made the difficult decision to abandon the siege and retreat towards Ghazni'; infobox 'Summer – Winter 1015', result 'Inconclusive'
- `/ledger/4`: confirmed (https://en.wikipedia.org/wiki/Siege_of_Lohkot_(1015)): 'led a second military campaign in 1021 AD'; 'Mahmud gave up on further plans of expansion into Kashmir'
- `/ledger/11`: confirmed (https://en.wikipedia.org/wiki/Kashmir_Sultanate): 'In 1320, a Mongol commander, Zulju, with an army of Qara'unas, entered Kashmir'
- `/ledger/6`: confirmed (https://en.wikipedia.org/wiki/Lohara_dynasty): reunification with Lohara at Utkarsa's accession; year from Kalasa's death in 1089 (page context)
- `/ledger/7`: confirmed (https://en.wikipedia.org/wiki/Lohara_dynasty): 'again split at the time of Uccala's accession', Lohara ceded to Sussala
- `/ledger/8`: confirmed (https://en.wikipedia.org/wiki/Lohara_dynasty): 'The downfall of Uccala came in December 1111'

## eastern-ganga-kingdom (fail)

Area: The infobox has no area (Established 493, Disestablished 1947). Cliopatria's 1056 shape is 163,985 km2.

Findings:

- `/keyframe_review/0/correction` [blocking]: Applies 1078-1151 with 556 cells, 411 of them Odisha cells outside the founding core (Brahmapur, 110 km), that is Utkala. The ledger gains Utkala only in 1118 (/ledger/4), so the keyframe draws it 40 years before the ledger does.
  - Evidence: Anantavarman_Chodaganga_Deva: the Sindurapura grant 'in the saka year 1040 (1118 A.D)' says he 'had sovereignty over entire of the whole Utkala'; the conquest is 'with the decline of the Somavamshis' (undated). Eastern_Ganga_dynasty: 'captured Utkala (Northern Odisha) from the Somavamshi Kings' (no year).
  - Fix: Split the keyframe: 1078-1117 Kalinga proper (the found region plus the Andhra and southern Odisha districts, minus Visakhapatnam) and 1118-1151 the 1056 outline minus Visakhapatnam. Or date the Utkala gain to the start at confidence 1 and say so; the keyframe and ledger must agree.
- `/ledger/4/region` [blocking]: The 1118 gain is all of {admin1: Odisha} (568 cells), which includes the Kalinga core held since 1078. The page names Utkala, 'Northern Odisha'.
  - Evidence: Eastern_Ganga_dynasty: 'captured Utkala (Northern Odisha)'.
  - Fix: Region: northern and central Odisha, e.g. {minus: [{admin1: Odisha}, <the found region>]}, with text 'Utkala (Northern Odisha)'.
- `/ledger/6` [blocking]: The 1152 gain of Sambalpur from the Kalachuris of Ratnapura contradicts its page. The note quotes 'fought with the Kalachuris of Ratnapura for the possession of the Sambalpur' and leaves out that he failed.
  - Evidence: Eastern_Ganga_dynasty (fetched twice): Kamarnava VII fought the Kalachuris of Ratnapura for the Sambalpur-Bolangir tract 'but was unsuccessful'.
  - Fix: Delete the gain, or turn it into a contest_start/contest_end pair with no transfer. Mark /keyframe_review/1 adjust, minus the Sambalpur cells that Cliopatria adds in 1152 (about 27 cells), or keep them as Kalachuri land with a note.
- `/ledger/1` [blocking]: The 1078 Visakhapatnam loss is never reversed. Keyframes 0 and 1 keep the district out until Cliopatria's 1260 shape, which the ledger credits to 'nobody'. The note leaves out the page's recovery clause.
  - Evidence: Eastern_Ganga_dynasty: he 'lost to them a part of his kingdom comprising the Visakhapatnam district, though he later recovered his lost territories'. Chodaganga page: the empire 'extended to river Godavari in the south'.
  - Fix: Add a gain of the Visakhapatnam district from chola-empire (c. 1118-1126, confidence 1) and put the district back into the keyframe corrections from that year.
- `/ledger/2` [not blocking, for the author]: The gain of Vengi north of the Godavari is bridged to 1100. The page ties it to Chola weakness at the end of Kulottunga I's reign. The chola-empire and western-chalukya-empire dossiers give Vengi to the Western Chalukyas for 1118-1133.
  - Evidence: Anantavarman_Chodaganga_Deva: 'Chodaganga saw this as an advantage and conquered the part of Vengi lying north to river Godavari' (context: Kulottunga's death). Kulottunga_Chola_I: 'the northern half of the Vengi kingdom seems to have slipped from his hands' late in the reign (reign 1070-1122). chola-empire /ledger/32 and western-chalukya-empire /ledger/24: Vengi to the Western Chalukyas c. 1118.
  - Fix: Date the gain c. 1118-1122 (confidence 1). Reconcile with the Western Chalukya Vengi of 1118-1133: either the Ganga land stops at a line north of the Chalukya-held part, or name the counterpart western-chalukya-empire.
- `/ledger/3` [not blocking, for the author]: The Chola conquest of Kalinga proper is dated c. 1115, the year the page attests Chola rule, not the year of the conquest.
  - Evidence: Kulottunga_Chola_I: the first war 'before 1096'; the second 'sometime before the 33rd year of the king's reign' (c. 1102); Chola rule over 'some parts of Kalinga (proper) including the capital Kalinganagara' is attested 'in his 45th regnal year (c. 1115 CE)'.
  - Fix: Date the loss c. 1102 (second Kalinga war) at confidence 1-2 and keep 1115 in the note as the attestation.
- `/ledger/9` [blocking]: The 1244 gain of Rarh from mamluk-dynasty has no end. Keyframes 1260-1344 (verdict ok) have no West Bengal cells, so the land drops out at 1260 with no loss event. The page calls the land occupied.
  - Evidence: Narasingha_Deva_I: 'Rarh and Gauda remained occupied by the Odia forces'; 'In 1247 CE ... Ikhtiyar-ud-Din Yuzbak was appointed as the governor of Bengal'.
  - Fix: Make it an occupation_start (1244) with an occupation_end or loss by 1247-1260 (confidence 1), or carry Rarh in the 1260 keyframe correction.
- `/ledger (missing, 1358)` [blocking]: The Tughlaq tribute is missing. The notes say the invasion has 'no territorial result', but the page has the king pay tribute.
  - Evidence: Eastern_Ganga_dynasty: 'Firuz Shah Tughlaq, invaded Odisha between 1353 and 1358, and levied tribute on the Ganga king.'
  - Fix: Add vassal_start 1358 (counterpart tughlaq-dynasty, region Odisha, confidence 2) and a vassal_end (confidence 1, bridged).
- `/ledger/1, /ledger/3, /ledger/5` [not blocking, for the author]: No Ganga-Chola event has a mirror in chola-empire.json. Its only Ganga event is a c. 1010 gain from 'eastern-ganga-kingdom', 68 years before this dossier starts.
  - Evidence: chola-empire /ledger/16 (1010 gain, counterpart eastern-ganga-kingdom). No Chola events in 1078-1126 name the Gangas.
  - Fix: Route to the chola-empire author (see cross_checks). The 1010 counterpart should be the earlier Ganga kingdom of Kalinganagara, which has no dossier.

Thin (gap-filler):

- `/ledger/7, /ledger/11`: Confidence-1 Cliopatria-step events (the 1152 loss of 104 cells, the 1260 gain of 238 cells), page silent. (try https://en.wikipedia.org/wiki/Narasingha_Deva_I)
- `/wars/1`: The Kalachuri of Ratnapura frontier 1120-1225 has no dated border. (try https://en.wikipedia.org/wiki/Kalachuris_of_Ratnapura)

Spot checks:

- `/ledger/14`: confirmed (https://en.wikipedia.org/wiki/Eastern_Ganga_dynasty): 'founded the Suryavamsha dynasty in 1434–35'
- `/ledger/1`: confirmed (https://en.wikipedia.org/wiki/Eastern_Ganga_dynasty): the loss is on the page, but so is 'though he later recovered his lost territories', which the dossier omits
- `/ledger/6`: not on page (https://en.wikipedia.org/wiki/Eastern_Ganga_dynasty): the page says the Sambalpur war was unsuccessful (confidence 1)
- `/ledger/4`: confirmed (https://en.wikipedia.org/wiki/Anantavarman_Chodaganga_Deva): the 1118 grant is confirmed; the region is too wide
- `/ledger/2`: mis-dated (https://en.wikipedia.org/wiki/Anantavarman_Chodaganga_Deva): tied on the page to Chola weakness at Kulottunga's death (1118 there, c. 1122 on the Kulottunga page), not to 1100 (confidence 1)
- `/ledger/3`: mis-dated (https://en.wikipedia.org/wiki/Kulottunga_Chola_I): c. 1115 is when Chola rule is attested; the conquest is the second Kalinga war, before the 33rd regnal year (confidence 2)
- `/ledger/12`: confirmed (https://en.wikipedia.org/wiki/Eastern_Ganga_dynasty): 'invaded Odisha between 1353 and 1358', and the page adds 'levied tribute on the Ganga king'
- `/ledger/9`: confirmed (https://en.wikipedia.org/wiki/Narasingha_Deva_I): 'In 1244 CE, the victorious Odia forces again seized two provinces of Varendra and Rarh'

## kingdom-of-polonnaruwa (fix)

Area: The infobox has no area. Cliopatria's 1072 shape (73,514 km2) is the whole island plus 4 rim cells.

Findings:

- `/ledger/3/counterpart, /ledger/4/counterpart` [applied by the reviewer]: The Rameswaram occupation (1167-1182) named chola-empire, but the land was in the Pandya country and Cliopatria's Chola shape has none of these cells in 1167-1182. chola-empire.json has no mirror.
  - Evidence: Parakramabahu_I: 'In 1167 the Pandyan king Parakrama appealed to his namesake in Sri Lanka for assistance'; Lankapura 'landed in the vicinity of Ramanathapuram' and 'captured the city of Rameswaram'. Kingdom_of_Polonnaruwa: 'Rameshwaram was under Sinhalese and Vira Pandyan Alliance rule till 1182'. Gazetteer: the 45 km disc has 0 cells in the Chola shapes of 1167, 1175 and 1182.
  - Fix: Applied: counterpart set to "Pandya kingdom of Madurai (Kulasekhara's side in the Pandyan civil war)" on both events, with a reviewer note. The dossier re-validated with 0 errors and 0 warnings under --resolve.

Thin (gap-filler):

- `/ledger/1, /keyframe_review/2, /keyframe_review/4`: Rajarata's boundary for 1111-1152 and 1197-1236, drawn with Cliopatria's 1250 northern outline as a stand-in (confidence 1). (try https://en.wikipedia.org/wiki/Vikramabahu_I)
- `/keyframe_review/0`: Vijayabahu I's Rohana enclave of 1055-1069 is not drawn (infobox start 1055). (try https://en.wikipedia.org/wiki/Vijayabahu_I)
- `/ledger/8`: Magha as 'a tribute-paying subordinate of the Chola Empire' (1215) carries no vassal event; check whether any page supports the tribute. (try https://en.wikipedia.org/wiki/Kalinga_Magha)
- `/ledger/5`: The 1196 loss goes to 'nobody'; the page names rival claimants but no holder of the south. (try https://en.wikipedia.org/wiki/Nissanka_Malla)

Spot checks:

- `/ledger/0`: confirmed (https://en.wikipedia.org/wiki/Kingdom_of_Polonnaruwa): 'By 1070, when Sinhalese sovereignty was restored under Vijayabāhu I'
- `/ledger/1`: confirmed (https://en.wikipedia.org/wiki/Parakramabahu_I): 'By the reign of Vikramabāhu I (1111–1132), the island was divided into three kingdoms'
- `/ledger/2`: confirmed (https://en.wikipedia.org/wiki/Parakramabahu_I): 'he secured power over the entire island around 1153'
- `/ledger/4`: confirmed (https://en.wikipedia.org/wiki/Kingdom_of_Polonnaruwa): 'Rameshwaram was under Sinhalese and Vira Pandyan Alliance rule till 1182'
- `/ledger/6`: confirmed (https://en.wikipedia.org/wiki/Kingdom_of_Polonnaruwa): 'In 1212, the capital was seized by Parakrama Pandyan'
- `/ledger/9`: confirmed (https://en.wikipedia.org/wiki/Kingdom_of_Polonnaruwa): 'expelled from Polonnaruwa in 1236, with an invasion from the south'

## sena-dynasty (fail)

Area: The infobox has no area. Cliopatria draws all of Bengal (257,438 km2) from 1072. The dossier's Rarh-only correction (147 cells, about 37,000 km2) is explained in the keyframe notes.

Findings:

- `/ledger/5, /keyframe_review/8` [blocking]: The 1169 gain of the Pala 1168 shape (307 cells, Bihar) is not in the 1169-1203 keyframe, whose correction is West Bengal plus Bangladesh (804 cells, 0 of the 307), so the keyframe contradicts the ledger. The counterpart pala-empire also dissolved in 1161 (pala-empire /ledger/26, dissolve to sena-dynasty).
  - Evidence: Sena_dynasty: 'The Palas were ousted in totality, and their entire territory annexed sometime after 1165.' Lakshmana_Sena: 'his empire, at its peak, possessed the territories of Gauda, Kamrupa, Kalinga, Magadha, and Kashi.'
  - Fix: Either add the Magadha land to the 1169 correction or drop the gain. Agree the year with the Pala author (Pala dissolve 1161 against this gain in 1169), or name the Gaya Palas as counterpart if after 1161.
- `/ledger/0, /ledger (missing vassal events)` [blocking]: Rarh is drawn as direct Sena land from 1070, though the Senas were Pala sāmantas until 1095. Meanwhile pala-empire.json keeps 'Radha' in its keyframes to 1158-1161, so both dossiers paint Rarh directly for 1070-1161.
  - Evidence: Sena_dynasty: 'The Senas entered into the service of Palas as sāmantas in Rāḍha, probably under Samantasena'; Hemanta Sena 'usurped power and styled himself king in 1095 AD'. pala-empire /keyframe_review (1111-1152 notes): 'Add Radha and Varendra'.
  - Fix: Add vassal_start 1070 and vassal_end 1095 (counterpart pala-empire, region Rarh, confidence 2). Settle with the Pala author that Rarh leaves the Pala keyframes in 1095 (cross-check mismatch).
- `/ledger/1, /keyframe_review/5` [not blocking, for the author]: The 1150 gain of south-eastern Bengal falls in the 1147 shape's span (1147-1151), whose correction is Rarh only. The 1152 keyframe adds the land.
  - Evidence: Vijaya_Sena: 'ousted the Varmans from southeastern Bengal in the middle of the 12th century AD' (no year).
  - Fix: Date the gain 1152 to match the 1152 keyframe (still confidence 2), or extend the 1152 correction back to 1150.
- `/ledger/3/region` [not blocking, for the author]: The 1159 'Gaur and the Bengal Delta' gain covers all of West Bengal and Bangladesh. That includes Rarh (Sena since 1070), south-eastern Bengal (1150) and Rajshahi (gained the same year in /ledger/2). The north-Bengal conquest is Vijaya Sena's, after 1152-53.
  - Evidence: Vijaya_Sena: 'Vijaya Sena established his own supremacy in North and North Western Bengal by ousting the Palas sometime after 1152–53 AD'; 'compelled the king of Gauda to flee'.
  - Fix: Region: Bengal minus the land already Sena and minus Rajshahi. Consider dating it within Vijaya Sena's reign (1153-1159, confidence 1).
- `/identity/capitals` [not blocking, for the author]: No capital covers 1070-1095; the first entry starts in 1096.
  - Evidence: Research brief rule 10: capitals with years for every state.
  - Fix: Add a 1070-1095 entry (a seat in Rarh, or Vikramapura from 1070 with a note that the page names none).

Thin (gap-filler):

- `/keyframe_review/8`: Lakshmana Sena's claimed Kamarupa, Kalinga and Kashi holdings are not drawn (no dates on the page). (try https://en.wikipedia.org/wiki/Lakshmana_Sena)
- `/ledger/3, /ledger/5, /ledger/7`: Confidence-1 events: the date Gaur passed, the Bihar annexation, the seat after 1204. (try https://en.wikipedia.org/wiki/Ballala_Sena)

Spot checks:

- `/ledger/0`: confirmed (https://en.wikipedia.org/wiki/Sena_dynasty): infobox 'Established: 1070'; sāmantas in Rāḍha
- `/ledger/1`: confirmed (https://en.wikipedia.org/wiki/Vijaya_Sena): 'ousted the Varmans from southeastern Bengal in the middle of the 12th century AD'
- `/ledger/3`: confirmed (https://en.wikipedia.org/wiki/Sena_dynasty): 'Ballala Sena conquered Gaur from the Pala, became the ruler of the Bengal Delta, and made Nadia the capital as well' (undated, confidence 1 honest)
- `/ledger/5`: confirmed (https://en.wikipedia.org/wiki/Sena_dynasty): 'sometime after 1165'
- `/ledger/6`: confirmed (https://en.wikipedia.org/wiki/Lakshmana_Sena): 'When Bakhtiyar captured Nadia, Lakshmana Sena withdrew to southeastern Bengal'; the Sena page has 1203–1204
- `/ledger/8`: confirmed (https://en.wikipedia.org/wiki/Sena_dynasty): 'Probably they ruled till at least 1230 AD'

## gahadavala-dynasty (fail)

Area: The infobox has no area. Cliopatria's 1085 shape is 216,799 km2.

Findings:

- `/ledger/8, /keyframe_review/1, /keyframe_review/2` [blocking]: The page says Govindachandra lost his Bihar territory by the end of his reign. The ledger's c. 1155 loss covers only the 8 cells Cliopatria drops in 1152, and the 1152 keyframe (verdict ok) keeps 105 Bihar cells to 1194.
  - Evidence: Govindachandra_(Gahadavala_dynasty): 'in the east, Govindachandra controlled a part of the present-day Bihar'; 'the Pala inscriptions in this area indicate that he lost this territory by the end of his reign'.
  - Fix: Loss region: the Bihar part of the Cliopatria shape ({intersect: [{cliopatria: Gahadavala Dynasty, year: 1152}, {admin1: Bihar, country: India}]}), c. 1155, confidence 1-2. Mark /keyframe_review/1 and /2 adjust, minus Bihar.
- `/keyframe_review/0` [blocking]: The 1085 shape (verdict ok, 860 cells) already holds land the ledger gains later: Kashi and Ayodhya (1090), Kannauj (1093) and the Yamuna-Sone land (1120). 557 of its cells have no event at all (Bihar 111, Nepal 74, Uttarakhand 44 among them), and the page puts the Bihar holding in Govindachandra's reign (1114-1155).
  - Evidence: Gazetteer: the found region plus the 1090, 1093 and 1120 gains is 349 cells against 860. Gahadavala_dynasty: 'The 1090 CE Chandrawati inscription of Chandradeva states that he protected the sacred places of Kashi'; 'According to Chandrawati inscriptions from 1093 CE and 1100 CE, the Gahadavalas occupied Kanyakubja'.
  - Fix: Mark it adjust: either a 1085-1092 core (the found region plus the 1090 inscription lands), with the gains carrying the growth to Cliopatria's outline, or recast the 1090 and 1093 events as attestations rather than gains. Remove Bihar before c. 1114, or say why it is kept.
- `/ledger/2/counterpart` [not blocking, for the author]: The 1093 Kannauj gain names gurjara-pratihara-dynasty, whose dossier ends in 1036 with a dissolve to gahadavala-dynasty (gurjara-pratihara-dynasty /ledger/38). That is 57 years before this gain and 49 before this dossier starts.
  - Evidence: Gahadavala_dynasty: 'the Gahadavalas occupied Kanyakubja' after the Gurjara-Pratihara descendants of Devapala were destroyed (1093 and 1100 inscriptions).
  - Fix: Counterpart 'nobody', or the Kannauj rulers of 1036-1093 (the Rashtrakutas of Kannauj under Gopala, which the Govindachandra page mentions). Route the 1036 dissolve successor to the Gurjara-Pratihara author.
- `/ledger/0, /ledger/1` [not blocking, for the author]: The founding region (Varanasi, 110 km) and the 1090 gain (Varanasi, 90 km, from the Kalachuris of Tripuri) are the same land.
  - Evidence: Gahadavala_dynasty: 'Chandradeva likely took Varanasi from the Kalachuris'.
  - Fix: Make the founding the Varanasi land taken from the Kalachuris (counterpart Kalachuri of Tripuri), and limit the 1090 event to Ayodhya/Kosala.
- `/wars/3/to` [applied by the reviewer]: The 'Sena-Gahadavala conflicts' ran to 1206, after the dossier's end in 1194 (wars must fall inside the life).
  - Evidence: identity.end 1194.
  - Fix: Applied: 'to' set to 1194, with a reviewer note; the sena-dynasty dossier keeps 1155-1206. Re-validated: 0 errors.
- `/sources` [applied by the reviewer]: sources[] listed https://en.wikipedia.org/wiki/Govindachandra, a disambiguation page with no content, cited by no event (the author's own problems list says it was opened by mistake).
  - Evidence: Reviewer brief, check 6: a source must be a page with content.
  - Fix: Applied: the entry was removed from sources[]. Re-validated: 0 errors.

Thin (gap-filler):

- `/keyframe_review/0`: The Himalayan rim (Nepal 74 cells, Uttarakhand 44 cells) has no page support (flagged by the author). (try https://en.wikipedia.org/wiki/Gahadavala_dynasty)
- `/ledger/0`: The 1085 founding year is a confidence-1 bridge to Cliopatria (the page: 'sometime before 1089'; infobox 1072). (try https://en.wikipedia.org/wiki/Chandradeva_(Gahadavala_dynasty))
- `/wars/3`: The Sena-Gahadavala conflicts have no land. (try https://en.wikipedia.org/wiki/Vijayachandra)

Spot checks:

- `/ledger/3`: confirmed (https://en.wikipedia.org/wiki/Gahadavala_dynasty): 'the Gahadavalas lost Kanyakubja to Ghaznavids somewhere between 1104 CE and 1105 CE' (confidence 3)
- `/ledger/9`: confirmed (https://en.wikipedia.org/wiki/Gahadavala_dynasty): 'He was defeated and killed at the Battle of Chandawar in 1194' (confidence 3)
- `/ledger/1`: confirmed (https://en.wikipedia.org/wiki/Gahadavala_dynasty): 1090 Chandrawati inscription, 'protected the sacred places of Kashi'
- `/ledger/2`: confirmed (https://en.wikipedia.org/wiki/Gahadavala_dynasty): 1093 and 1100 inscriptions: Kanyakubja occupied
- `/ledger/4`: confirmed (https://en.wikipedia.org/wiki/Govindachandra_(Gahadavala_dynasty)): 'restore the Gahadavala power in Kanyakubja and its surrounding area by 1109 CE'
- `/ledger/8`: confirmed (https://en.wikipedia.org/wiki/Govindachandra_(Gahadavala_dynasty)): the loss is on the page, but it covers 'this territory' (his Bihar holding), not an 8-cell edge

## hoysala-kingdom (fail)

Area: The infobox has no area (only a 'greatest extent' map caption). Cliopatria's 1111 shape is 111,360 km2.

Findings:

- `/keyframe_review/2, /keyframe_review/3, /keyframe_review/4` [blocking]: Three keyframes marked ok (1126, 1188, 1241) contradict the ledger. The northern gains of 1120, 1140 and 1190, the 1192 gain (618 cells, 226 outside the 1188 shape) and the Tamil gains of 1225 and 1236 are in no keyframe. After the 1212 loss the ledger still holds 191 cells (about 48,000 km2) outside the 1241 shape: 73 between the Cliopatria shape and the Tungabhadra plus 118 Tamil cells. They vanish at the 1241 keyframe with no loss event.
  - Evidence: Gazetteer: the 1188 shape plus /ledger/9, /12 and /18-19, minus /13, gives 626 cells against 439 in the 1241 shape. The pages support the land: Vishnuvardhana ('re-captured Hanagal, Uchchangi and Bankapura by c.1140'), Veera_Ballala_II ('By c. 1192 ... emperor over the entire modern Karnataka region'), Hoysala_Empire ('Kannanur Kuppam near Srirangam a provincial capital').
  - Fix: Mark these keyframes adjust with union corrections: 1126 plus Banavasi and Humacha; 1188 plus the marches to the Tungabhadra, with 1192-1211 as its own new keyframe to the Krishna; 1241 plus Kannanur and Magadai Mandalam. Carry the same land in the 1250-1285 corrections, which now restore only 'the 1241 outline'.
- `/ledger (missing, c. 1122 and 1126)` [blocking]: No vassal events for the Hoysala subordination to the Western Chalukyas. western-chalukya-empire /ledger/25-26 records vassal_start 1122 and vassal_end 1126 with hoysala-kingdom.
  - Evidence: Vishnuvardhana: 'Vishnuvardhana thus had to accept, for the time being, subordination to the Chalukya throne' (c. 1122). Hoysala_Empire: 'Initially, the Hoysalas served as feudatories of the Western Chalukyas of Kalyana.'
  - Fix: Add vassal_start 1122 (counterpart western-chalukya-empire, the Hoysala realm, confidence 2) and vassal_end 1126 (confidence 1, as in the Chalukya dossier).
- `/ledger (missing, 1311 and c. 1318)` [blocking]: No vassal events for the tribute to Delhi. The note on /ledger/26 leaves the relation to the khalji-dynasty dossier, but the vassal's own ledger must carry it too.
  - Evidence: Veera_Ballala_III: he had to 'pay a handsome tribute, and send his son Veera Virupaksha to Delhi as an act of submission'; after 1318 he 'refused to pay tribute and withdrew from his earlier pact to support the Delhi Sultanate as a vassal'.
  - Fix: Add vassal_start 1311 (month 2 or later, counterpart khalji-dynasty, confidence 2) and vassal_end c. 1318 (confidence 2).
- `/ledger/9/counterpart, /ledger/12/counterpart` [blocking]: The 1190 and 1192 gains name western-chalukya-empire, which dissolves in 1187 (its /ledger/32). The 1190 note says the page's numeral 'does not match'; the page says Someshvara VI.
  - Evidence: Veera_Ballala_II: 'expeditions to Banavasi against the exiled Chalukya King Someshvara VI and defeated him by c. 1190'; 'In c. 1191 ... gained the upper hand over Yadava Bhillama V in the critical battles of Soratur and Lakkundi'.
  - Fix: 1190: counterpart = the exiled Chalukya rump (no dossier: list it, or 'nobody'), and correct the note to Someshvara VI. 1192: counterpart yadava-dynasty (and Kalachuri of Kalyani for the Kalachuri marches).
- `/ledger/6-8` [not blocking, for the author]: The c. 1179 Kalachuri seizure of Hangal is missing; the ledger records only a truce.
  - Evidence: Veera_Ballala_II: 'an attempt by him to invade Belvola-300 in c. 1179 led to his defeat by Kalachuri commander Sankama who seized Hangal'.
  - Fix: Add a loss of Hangal c. 1179 (counterpart Kalachuri of Kalyani, confidence 2), and show Hangal regained by the c. 1190-1192 gains.
- `/wars/5, /ledger/23` [not blocking, for the author]: The Hoysala-Pandya war of 1262-1263 has a zone but no contest or loss events. The 1295 merge 'recaptured territory in the Tamil country', which implies an earlier loss the ledger lacks.
  - Evidence: Vira_Someshwara (cited in /wars/5): he 'was killed in a war with' Sadayavarman Sundara Pandyan I. Hoysala_Empire: 'Veera Ballala III recaptured territory in the Tamil country'.
  - Fix: Add contest_start and contest_end 1262-1263 at Kannanur and the loss of the Tamil holdings to pandya-empire (bridged, confidence 1), or explain in the note why none is drawn.
- `/ledger/22, /ledger/23` [not blocking, for the author]: The 1254 split and 1295 merge name 'Hoysala southern branch', which the note itself treats as the same state and colour. It has no dossier and is not listed.
  - Evidence: /ledger/22 note: 'Both are Hoysala kings, so the colour stays the same'.
  - Fix: Drop the split and merge (two kings of one state), or list the southern branch in counterparts_needing_dossiers.

Thin (gap-filler):

- `/ledger/6`: Hangal c. 1178: the earlier holder is not named (confidence 1). (try https://en.wikipedia.org/wiki/Veera_Ballala_II)
- `/identity/rulers`: No ruler strip, though the dynasty's kings and reigns are given on the main page and the ruler pages. (try https://en.wikipedia.org/wiki/Hoysala_Empire)
- `/keyframe_review/5-7`: The 1254 border between the branches (Cliopatria's 1250-1325 shapes may show the split). (try https://en.wikipedia.org/wiki/Vira_Narasimha_III)

Spot checks:

- `/ledger/25`: confirmed (https://en.wikipedia.org/wiki/Veera_Ballala_III): 'Halebidu was attacked and plundered on 26 February 1311' (confidence 3)
- `/ledger/12`: confirmed (https://en.wikipedia.org/wiki/Veera_Ballala_II): 'By c. 1192, Ballala II had crowned himself the emperor over the entire modern Karnataka region'
- `/ledger/13`: confirmed (https://en.wikipedia.org/wiki/Veera_Ballala_II): 'After c. 1212, he lost all these territories north of the Tungabhadra River to Yadava king Singhana II'
- `/ledger/9`: confirmed (https://en.wikipedia.org/wiki/Veera_Ballala_II): the event is confirmed; the defeated king is Someshvara VI, an exile, so the counterpart is wrong
- `/ledger/1`: confirmed (https://en.wikipedia.org/wiki/Hoysala_Empire): 'Vishnuvardhana achieved a victory over the Cholas at Talakadu in 1116'
- `/ledger/18`: confirmed (https://en.wikipedia.org/wiki/Hoysala_Empire): 'extended their foothold in modern-day Tamil Nadu around 1225'
- `/ledger/3`: confirmed (https://en.wikipedia.org/wiki/Vishnuvardhana): Banavasi and Humacha c.1117-1120
- `/ledger/5`: confirmed (https://en.wikipedia.org/wiki/Vishnuvardhana): 're-captured Hanagal, Uchchangi and Bankapura by c.1140'
- `/ledger/16`: confirmed (https://en.wikipedia.org/wiki/Hoysala_Empire): 'From 1220 to 1245 the dynasty's hegemony increased southwards'
- `/ledger/31`: confirmed (https://en.wikipedia.org/wiki/Hoysala_Empire): 'killed at the battle of Madurai in 1343'; territories 'merged with the areas administered by Harihara I'

## Cross-dossier matrix

- lohara-dynasty 1003 found (utpala-dynasty) -> utpala-dynasty 1003 dissolve: **matched**. Kashmir also records a 1003 rename to the Lohara dynasty; the land is drawn twice.
- lohara-dynasty 1056 loss (nobody) -> kashmir 1056 loss: **exception**. Counterpart nobody; kashmir.json carries the same event.
- lohara-dynasty 1089 gain (Lohara principality) -> -  : **missing**. No dossier, not listed; kashmir.json lacks the event.
- lohara-dynasty 1101 split (Lohara principality (Sussala)) -> -  : **missing**. As for 1089.
- lohara-dynasty 1111 merge (Lohara principality (Sussala)) -> -  : **missing**. As for 1089.
- lohara-dynasty 1152 gain (nobody) -> kara-khitans 1152 loss: **mismatch**. kara-khitans /ledger/12 gives 218 Pamir cells to lohara-dynasty; the Lohara 1152 correction removes the Pamirs, and its 1152 gain is the Jammu/Himachal hills. The Kara-Khitan loss should go to nobody (ia-01).
- lohara-dynasty 1210 gain (nobody) -> kashmir 1210 gain: **exception**. Counterpart nobody.
- lohara-dynasty 1235 vassal_start (missing) (mongol-empire) -> mongol-empire  : **missing**. Neither side records the Mongol dependency 'some time after 1235' (Kashmir Sultanate page).
- lohara-dynasty 1320 dissolve (kashmiri-sultanate) -> kashmir 1320 rename: **mismatch**. kashmir.json continues the state to 1339 (Lohara line back 1323-1339).
- eastern-ganga-kingdom 1078 loss (chola-empire) -> chola-empire  : **missing**. No Chola gain of Visakhapatnam (sa-03 Chola author).
- eastern-ganga-kingdom 1100 gain (chola-empire) -> chola-empire 1118 loss: **mismatch**. Chola /ledger/32 loses Vengi c. 1118 to western-chalukya-empire (WCE /ledger/24 holds it 1118-1133), not to the Gangas; the Ganga gain should be c. 1118-1122 and reconciled.
- eastern-ganga-kingdom 1115 loss (chola-empire) -> chola-empire  : **missing**. No Chola gain of Kalinga proper (conquest c. 1102 per Kulottunga page).
- eastern-ganga-kingdom 1118 gain (Somavamshi dynasty) -> -  : **exception**. Listed in the author's counterparts_needing_dossiers.
- eastern-ganga-kingdom 1126 gain (chola-empire) -> chola-empire  : **missing**. No Chola loss of Kalinga proper.
- eastern-ganga-kingdom 1152 gain (Kalachuri of Ratnapura) -> -  : **exception**. Counterpart listed, but the page says the Ganga attempt was unsuccessful (see fixes).
- eastern-ganga-kingdom 1152 loss (nobody) -> -  : **exception**. Counterpart nobody.
- eastern-ganga-kingdom 1244 gain (mamluk-dynasty) -> mamluk-dynasty  : **exception**. mamluk-dynasty is sa-04, not run yet.
- eastern-ganga-kingdom 1260 gain (nobody) -> -  : **exception**. Counterpart nobody.
- chola-empire 1010 gain (eastern-ganga-kingdom) -> eastern-ganga-kingdom  : **mismatch**. The eastern-ganga-kingdom dossier starts in 1078; the 1010 counterpart is the earlier Ganga kingdom of Kalinganagara (no dossier).
- kingdom-of-polonnaruwa 1070 found (chola-empire) -> chola-empire 1070 loss: **matched**. chola /ledger/27, confidence 3.
- kingdom-of-polonnaruwa 1111 loss (Dakkhinadesa and Ruhuna) -> -  : **missing**. No dossier; added to counterparts_needing_dossiers by the reviewer.
- kingdom-of-polonnaruwa 1153 gain (Dakkhinadesa and Ruhuna) -> -  : **missing**. As for 1111.
- kingdom-of-polonnaruwa 1167 occupation_start (Pandya kingdom of Madurai (Kulasekhara's side in the Pandyan civil war)) -> -  : **exception**. Reviewer changed the counterpart from chola-empire (applied); no Pandya dossier for 915-1216, listed.
- kingdom-of-polonnaruwa 1182 occupation_end (Pandya kingdom of Madurai (Kulasekhara's side in the Pandyan civil war)) -> -  : **exception**. As for 1167.
- kingdom-of-polonnaruwa 1196 loss (nobody) -> -  : **exception**. Counterpart nobody.
- sena-dynasty 1070 found (Rarh) (pala-empire) -> pala-empire 1161 dissolve: **mismatch**. pala-empire keeps Radha in its keyframes to 1158-1161; the Sena dossier holds Rarh directly from 1070. The Senas were Pala samantas to 1095: both sides need a vassal_start 1070 and vassal_end 1095, and the Pala keyframes should drop Rarh from 1095.
- sena-dynasty 1150 gain (varman-dynasty-of-east-bengal) -> -  : **exception**. Listed (placeholder slug).
- sena-dynasty 1159 gain (pala-empire) -> pala-empire 1159 loss: **matched**. Rajshahi ('a part of Varendra'), pala /ledger/25.
- sena-dynasty 1159 gain (pala-empire) -> pala-empire 1161 dissolve: **mismatch**. Gaur/Bengal Delta gained 1159; the Pala dossier hands its remnant (incl. Radha and Rangpur) over at its 1161 dissolve; 2 years apart.
- sena-dynasty 1169 gain (pala-empire) -> pala-empire 1161 dissolve: **mismatch**. Bihar (Pala 1168 shape) gained 8 years after the Pala dossier's end; also absent from the Sena 1169 keyframe.
- sena-dynasty 1204 loss (ghurid-dynasty) -> ghurid-dynasty  : **exception**. ghurid-dynasty is sa-04, not run yet.
- kamarupa-kingdom 1072 loss (sena-dynasty) -> sena-dynasty  : **mismatch**. kamarupa /ledger/25 gives 32 cells (90.8-92.4 E, 25.3-26.0 N) to the Sena in 1072; the Sena 1072 keyframe is corrected to Rarh, so the Kamarupa counterpart should be nobody or another holder (sa-02).
- gahadavala-dynasty 1090 gain (Kalachuri of Tripuri) -> -  : **exception**. Listed.
- gahadavala-dynasty 1093 gain (gurjara-pratihara-dynasty) -> gurjara-pratihara-dynasty 1036 dissolve: **mismatch**. GP dissolves in 1036 with successor gahadavala-dynasty, which starts in 1085; the 1093 holder of Kannauj is not the Pratihara state.
- gahadavala-dynasty 1104 loss (ghaznavid-empire) -> ghaznavid-empire  : **exception**. ghaznavid-empire is me-08, not run yet.
- gahadavala-dynasty 1109 gain (ghaznavid-empire) -> ghaznavid-empire  : **exception**. As for 1104.
- gahadavala-dynasty 1120 gain (Kalachuri of Tripuri) -> -  : **exception**. Listed.
- gahadavala-dynasty 1155 loss (pala-empire) -> pala-empire  : **missing**. pala-empire has no gain from the Gahadavalas (its 1147 note: Madanapala took Munger from the Gahadavalas, undated).
- chandela-kingdom 1085 loss (gahadavala-dynasty) -> gahadavala-dynasty  : **mismatch**. chandela /ledger/9 (confidence 1, 28 cells) has no Gahadavala gain; flagged by the author; the Chandela author should drop or re-route it.
- hoysala-kingdom 1116 gain (chola-empire) -> chola-empire 1116 loss: **matched**. chola /ledger/31.
- hoysala-kingdom 1120 gain (western-chalukya-empire) -> western-chalukya-empire  : **missing**. WCE has no loss of Banavasi/Humacha.
- western-chalukya-empire 1122 vassal_start (hoysala-kingdom) -> hoysala-kingdom  : **missing**. Hoysala ledger lacks the vassal_start (see fixes).
- western-chalukya-empire 1126 vassal_end (hoysala-kingdom) -> hoysala-kingdom  : **missing**. As for 1122.
- hoysala-kingdom 1140 gain (western-chalukya-empire) -> western-chalukya-empire  : **missing**. WCE has no loss of Hanagal/Uchchangi/Bankapura.
- hoysala-kingdom 1178 gain (Hangal (holder not named on the page)) -> -  : **exception**. Holder unnamed.
- hoysala-kingdom 1190 gain (western-chalukya-empire) -> western-chalukya-empire 1187 dissolve: **mismatch**. WCE ends 1187; the page's counterpart is the exiled Someshvara VI.
- hoysala-kingdom 1192 gain (western-chalukya-empire) -> western-chalukya-empire 1187 dissolve: **mismatch**. WCE ends 1187; the land came from the Yadavas/Kalachuris.
- hoysala-kingdom 1212 loss (yadava-dynasty) -> yadava-dynasty  : **exception**. yadava-dynasty belongs to another sa-03 part, not written yet.
- hoysala-kingdom 1220 vassal_start (chola-empire) -> chola-empire  : **missing**. Chola has no vassal_start under the Hoysalas (only the 1217 end of Pandya overlordship).
- hoysala-kingdom 1220 vassal_start (pandya-empire) -> pandya-empire  : **exception**. sa-04, not run yet.
- hoysala-kingdom 1225 gain (chola-empire) -> chola-empire  : **missing**. No Chola loss of Kannanur Kuppam.
- hoysala-kingdom 1236 gain (chola-empire) -> chola-empire  : **missing**. No Chola loss of Magadai Mandalam.
- hoysala-kingdom 1245 vassal_end (chola-empire) -> chola-empire  : **missing**. As for 1220.
- hoysala-kingdom 1245 vassal_end (pandya-empire) -> pandya-empire  : **exception**. sa-04.
- hoysala-kingdom 1254 split (Hoysala southern branch (Ramanatha, Kannanur)) -> -  : **exception**. Internal division; see fixes.
- hoysala-kingdom 1295 merge (Hoysala southern branch (Ramanatha, Kannanur)) -> -  : **exception**. As for 1254.
- hoysala-kingdom 1311 vassal_start (missing) (khalji-dynasty) -> khalji-dynasty  : **missing**. Neither side yet; khalji-dynasty is sa-04.

## Counterparts needing dossiers (added by the reviewer)

- Dakkhinadesa (Malaya Rata) and Ruhuna kingdoms (`dakkhinadesa`, 1111-1153): counterpart of kingdom-of-polonnaruwa /ledger/1-2; Ruhuna may want its own slug (ruhuna)
- Pandya kingdom of Madurai (12th century) (`pandya-kingdom-of-madurai`, 1167-1182): counterpart of kingdom-of-polonnaruwa /ledger/3-4; no Pandya dossier covers 915-1216
- Eastern Gangas of Kalinganagara (before 1078) (`eastern-gangas-of-kalinganagara`, 493-1077): counterpart of chola-empire /ledger/16 (c. 1010)
- Rashtrakutas of Kannauj (Gopala) (`rashtrakutas-of-kannauj`, 1036-1093): holder of Kannauj before gahadavala-dynasty /ledger/2; only if a page supports it, else counterpart nobody
- Lohara principality (Poonch) (`lohara-principality`, 1028-1111): counterpart of lohara-dynasty /ledger/6-8; only if Lohara is not folded into kashmir.json

## Problems

- lohara-dynasty duplicates kashmir.json (another sa-03 part) for 1003-1320, and utpala-dynasty does the same for 855-1003. The orchestrator must decide to fold the Lohara and Utpala rows into kashmir.json (one state, dynasty renames), or the Valley is painted twice. The lohara author cannot fix this alone.
- Applied reviewer edits (re-validated, 0 errors): kingdom-of-polonnaruwa /ledger/3-4 counterpart; gahadavala-dynasty /wars/3 'to' 1206 -> 1194 and the Govindachandra disambiguation entry removed from sources[].
- Mirror work for neighbour authors: chola-empire (EG 1078/1115/1126, Hoysala 1220-1245 vassal and 1225/1236 losses, c. 1010 counterpart); western-chalukya-empire (Hoysala 1120/1140 losses; Someshvara IV/VI's Banavasi rump after 1187); pala-empire (Rarh 1070-1161 overlap, Sena vassal 1070-1095, the 1155 Gahadavala loss, the 1161 dissolve vs Sena 1169); kamarupa-kingdom /ledger/25 and chandela-kingdom /ledger/9 (losses to states that do not gain); kara-khitans /ledger/12 (Pamirs to lohara); gurjara-pratihara-dynasty /ledger/38 (1036 dissolve to a state that starts in 1085).
- No infobox of the six main pages gives an area, so every area_check is against Cliopatria only.
- WebFetch returns extracts and paraphrases: the quotes in this report are as returned. 'Unsuccessful' (Sambalpur) and 'though he later recovered his lost territories' (Visakhapatnam) were paraphrased rather than quoted verbatim by the fetch tool; the first was confirmed in two separate fetches.
- No confidence-3 event failed a spot check (Lohkot 1015/1021, Zulju 1320, Suryavamsha 1434, Kannauj 1104, Chandawar 1194, Halebidu 1311 all confirmed). The EG author twice cut a page sentence before its contrary clause (/ledger/1 and /ledger/6); a re-run of that dossier should re-read its pages.
