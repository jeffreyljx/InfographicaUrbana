# Review of gap batch g-sa-a (Bengal and Assam gaps), 2026-11-01

Reviewer: adversarial pass on the seven dossiers of g-sa-a. All seven validate with --resolve (0 errors, 0 warnings). Spot checks were made with WebFetch on the Wikipedia pages the dossiers cite; overlaps were measured by resolving the keyframe corrections with tools/gazetteer.py (cell counts; about 250 km2 a cell).

Verdicts: chutia-kingdom fail, kachari-kingdom fail, khalji-dynasty-of-bengal fail, balbani-sultanate-of-bengal thin, varman-dynasty-of-east-bengal pass, deva-dynasty fail, first-deva-dynasty fail.

## chutia-kingdom: fail

- **/keyframe_review/0/correction** (blocking): The 1228-1511 shape (an unclipped 170 km disc round Dibrugarh, 347 cells) contains the whole ahom-kingdom 1228 shape: the Chutia kingdom swallows the Ahom kingdom for 284 years.
  - Why: Gazetteer resolve: chutia K0 (347 cells) intersect ahom-kingdom /keyframe_review/0 (intersect Assam, Dibrugarh 90 km; 53 cells) = 53 cells, i.e. all of it; both are born in 1228, so the compile meets a found/keyframe conflict on every Ahom cell. Not flagged in the notes.
  - Fix: Subtract the Ahom land: minus(..., intersect(A1:Assam, P:Dibrugarh/90)) in /keyframe_review/0, /ledger/0 and /identity/predecessors/0/land, and coordinate with ahom-kingdom (see problems: its 1228 disc also contains Sadiya, so the Ahom core should be recentred on Charaideo/Sivasagar and the Chutia land drawn round Sadiya, Tinsukia, Dhemaji and Lakhimpur).
- **/keyframe_review/0/correction** (blocking): The shape runs past the limits the page gives and is about twice the size of the whole Ahom kingdom at its height; the factor is not acknowledged.
  - Why: Chutia kingdom page (Dutta): 'bound by the Himalayas on the north, river Burhi Dihing on the south, Patkai ranges on the east and Bharali river in the west'; core 'Lakhimpur, Dhemaji, Tinsukia, and parts of Dibrugarh'. The disc puts 45 cells in Myanmar (beyond the Patkai), 30 in Nagaland (south of the Burhi Dihing), 187 in Arunachal Pradesh and only 85 in Assam; 347 cells is about 87,000 km2, against the Ahom kingdom's infobox 41,958 km2 (1826).
  - Fix: Clip to the page's frame: intersect with union(A1:Assam, A1:Arunachal Pradesh) and minus Nagaland and anything south of the Burhi Dihing (a smaller disc centred on Sadiya once the gazetteer has it, e.g. {lon 95.65, lat 27.83, km 120} intersect those admin1s); give the drawn area in the keyframe note.
- **/keyframe_review/1/correction** (blocking): The capital Sadiya (identity capitals 1228-1523) lies outside the 1512-1522 shape, although the pages have the Chutias holding Sadiya until the 1523 fall.
  - Why: The subtracted Habung region intersect(Assam, Dibrugarh 110 km) contains Sadiya (82 km); gazetteer: the Sadiya cell is in ahom K1 and not in chutia K1. Suhungmung page: 'The Chutias fortified Sadiya, but they were soon defeated'; 'the newly acquired Sadiya region' after 1523-24. The author flagged it but left the shape wrong.
  - Fix: Subtract a Sadiya disc from the 1512 loss (/ledger/1/region) and from the subtrahend of /keyframe_review/1 (e.g. minus {lon 95.65, lat 27.83, km 40}), and route ahom-kingdom /ledger/2 and /keyframe_review/0-1 to keep Sadiya out of Ahom land before 1523.
- **/ledger** (non-blocking): The Chutia occupation of 1520-1522 (up to Namdang and Mungkhrang) is in a note only.
  - Why: Suhungmung page: 'The Chutias again attacked the Ahoms in 1520 and occupied the areas up to Namdang and Mungkhrang'; 'In 1522, the Ahoms fought back, re-occupied their lost territories'.
  - Fix: Optional: occupation_start 1520 / occupation_end 1522 against ahom-kingdom on a small region round Namdang (confidence 2), or say in the note why it is not drawn.
- Thin:
  - /ledger/0: Founding year (bridge 1228, confidence 1); kamarupa-kingdom hands this land over in 1140. (try https://en.wikipedia.org/wiki/Chutia_kingdom)
  - /ledger/1: Where Habung (Panbari) lay, so the 1512 loss can be drawn without Sadiya. (try https://en.wikipedia.org/wiki/Lakhimpur_district)
- Spot checks:
  - /ledger/1, https://en.wikipedia.org/wiki/Suhungmung: confirmed: 'He annexed Habung, a Chutia dependency in 1512'
  - /ledger/2, https://en.wikipedia.org/wiki/Suhungmung: confirmed: Dhirnarayan 'attacked the Ahoms at Dikhoumukh the next year' (1513)
  - /ledger/4, https://en.wikipedia.org/wiki/Suhungmung: confirmed: 'later in 1523-24, the rest of the Chutia Kingdom'
  - /ledger/5, https://en.wikipedia.org/wiki/Chutia_kingdom: confirmed: infobox 'Disestablished 1523-24'; 'The Chutiya power lasted until 1523'
- Area: No infobox area and no Cliopatria row. Drawn 347 cells (about 87,000 km2) against the page's four districts plus Arunachal foothills, and against the Ahom kingdom's 41,958 km2 (1826 infobox): about 2x the Ahom maximum, unacknowledged.

## kachari-kingdom: fail

- **/keyframe_review/1/correction** (blocking): The 1526-1557 shapes (/keyframe_review/1 and /2) exclude the capital Dimapur (identity capitals, 1228-1536), contrary to the keyframe note 'the Dimapur disc stays Kachari'.
  - Why: The gazetteer files the Dimapur cell (93.73E 25.91N) under Assam and it lies 104 km from Jorhat, so intersect(A1:Assam, P:Jorhat/110), subtracted in K1/K2 and lost in /ledger/2, takes it. Ahom kingdom page: the Ahoms 'twice occupied the Kachari capital at Dimapur' and the author's own note quotes 'did not result in the permanent annexation of Dimapur'.
  - Fix: Carve Dimapur out of the Marangi region in /ledger/1-/ledger/4 and in the subtrahends of /keyframe_review/1-2 (e.g. minus(intersect(A1:Assam, P:Jorhat/110), {lon 93.73, lat 25.91, km 30})); route ahom-kingdom /ledger/6-7 and its 1526-1638 keyframes to do the same.
- **/keyframe_review/3** (non-blocking): The 1558 keyframe adds 14 cells (the North Cachar hills round Maibang outside the Dimapur disc) with only a capital_move in the ledger.
  - Why: Rule 4: K2 58 cells to K3 72 cells; /ledger/5 is a capital_move with no region. Kachari page: 'In either 1558 or 1559 a son of Detsung, Madanakumara, assumed the throne'.
  - Fix: Add a 1558 gain, counterpart nobody, region intersect(A1:Assam, {lon 93.02, lat 25.17, km 45}), source Kachari_Kingdom, confidence 2; or, if the hills were Kachari all along, put them in /keyframe_review/0 and say so.
- **/wars/2** (non-blocking): The Koch subjugation (1562-1564) is a war only; neither this dossier nor koch-bihar records the feudatory status the dossier's own note describes.
  - Why: Kachari page: 'After subjugating the Ahoms in 1564, the Koch commander Chilarai advanced on Marangi'; footnote: 'The Khaspur state originated with Chilarai's invasion in 1562 AD'. koch-bihar has no event naming this slug.
  - Fix: Add vassal_start 1564 counterpart koch-bihar over the Maibang hills (confidence 2) and a vassal_end at a bridge year (confidence 1), or state in the note why no vassalage is drawn.
- Thin:
  - /ledger/0: Founding year (bridge 1228, confidence 1); kamarupa-kingdom hands Assam over in 1140. (try https://en.wikipedia.org/wiki/Dimasa_people)
  - /keyframe_review/5: Dates of the Burmese occupation of Cachar (1819-1826) and Govinda Chandra's restoration. (try https://en.wikipedia.org/wiki/Burmese_invasions_of_Assam)
- Spot checks:
  - /ledger/7, https://en.wikipedia.org/wiki/Kachari_Kingdom: confirmed: 'The independent rule of the Khaspur's Koch rulers ended in 1745 when it merged with the Kachari kingdom'
  - /ledger/9, https://en.wikipedia.org/wiki/Kachari_Kingdom: confirmed: 'the plains in 1832' (body also has 1833 for Govinda Chandra's domain, noted by the author)
  - /ledger/10, https://en.wikipedia.org/wiki/Kachari_Kingdom: confirmed: 'the hills in 1834'
  - /ledger/6, https://en.wikipedia.org/wiki/Kachari_Kingdom: confirmed: 'By the reign of Birdarpan Narayan (reign around 1644), the Dimasa rule had withdrawn completely from the Dhansiri valley'
  - /ledger/2, https://en.wikipedia.org/wiki/Ahom_kingdom: confirmed: Marangi 'acquired from the Kachari kingdom in 1526'
  - /ledger/4, https://en.wikipedia.org/wiki/Ahom_kingdom: confirmed: 'In 1536, after the series of contacts with the Kachari kingdom, the Ahom rule extended up to the Kolong River in Nagaon'
- Area: No infobox area, no Cliopatria row; 131 cells in 1228 falling to 19 by 1644; the keyframe notes say the page gives no area.

## khalji-dynasty-of-bengal: fail

- **/ledger** (blocking): No vassal_start/vassal_end mirrors mamluk-dynasty /ledger/9 (1225 vassal_start, confidence 3) and /ledger/11 (1227 vassal_end), both listed under 'Cited by' in section 6 of the author's brief.
  - Why: Rule 3. Iltutmish page: 'Iltutmish's forces captured Bihar in the 1210s, and invaded Bengal in 1225'; Ghiyasuddin chose to submit, 'paying tribute and accepting Iltutmish's overlordship', and later 'Ghiyasuddin re-asserted his independence and occupied Bihar'. The dossier's own /ledger/3 note quotes the tribute but writes no event.
  - Fix: Add vassal_start 1225, counterpart mamluk-dynasty, region union(A1:West Bengal, A1:Rajshahi, A1:Rangpur), source Iltutmish, confidence 3; add vassal_end 1227 to match mamluk-dynasty /ledger/11 (or an earlier bridge for the re-assertion, confidence 1, saying in the note that the Mamluk dossier has 1227).
- **/ledger/0** (non-blocking): The 1204 found takes the Lakhnauti disc while sena-dynasty still holds it (sena /ledger/9: 1204 loss to ghurid-dynasty) and ghurid-dynasty gains it in 1205 (/ledger/34) before handing it over in 1206 (/ledger/38): a conflict in 1204 and a double claim in 1205.
  - Why: Neighbour ledgers as cited; sena-dynasty is not a predecessor or the counterpart of the found, so the compile counts the 1204 claim as a conflict.
  - Fix: Either begin the state in 1206 (found counterpart ghurid-dynasty, region = ghurid /ledger/38, with 1204-1205 in the identity notes), or keep 1204 and route ghurid-dynasty /ledger/34 to exclude {lon 88.14, lat 24.87, km 60}; say which in the note.
- Spot checks:
  - /ledger/1, https://en.wikipedia.org/wiki/Khalji_dynasty_of_Bengal: confirmed: 'pledged allegiance to Sultan Muhammad of Ghor until his death in 1206'
  - /ledger/2, https://en.wikipedia.org/wiki/Iltutmish: confirmed as a decade: 'captured Bihar in the 1210s'; 1215 is the mamluk-dynasty bridge
  - /ledger/3, https://en.wikipedia.org/wiki/Iltutmish: confirmed: 'Nasiruddin captured his capital Lakhnauti, and defeated and executed him'; Khalji page: 'In 1227, Iwaz was killed'
  - /ledger/4, https://en.wikipedia.org/wiki/Iltutmish: confirmed: 'the coinage in the Bengal region was issued in the name of Iltutmish'
- Area: No infobox area (page header 1204-1231); 804 cells 1206-1214 equal ghurid-dynasty's 1206 handover exactly.

## balbani-sultanate-of-bengal: thin

- **/keyframe_review/0/correction** (non-blocking): The 1287-1300 shape (Mamluk 1285 intersect Bengal) holds 54 cells of the Dhaka division, Bikrampur, Sonargaon and Dhaka among them, which deva-dynasty holds to 1294 and which /ledger/2 says came to the kingdom only in 1301.
  - Why: Gazetteer: balbani K0 intersect deva-dynasty K0 = 54 cells; inherited from mamluk-dynasty /ledger/35 as the author's brief required, so not blocking here.
  - Fix: Resolve together with the deva-dynasty rework: either subtract A1:Dhaka from K0 and /ledger/0 (and route mamluk-dynasty /ledger/35), or keep the Mamluk handover and drop the Dhaka part of the Deva land; say which in the K0 note.
- **/ledger/2/counterpart** (non-blocking): Counterpart deva-dynasty dissolved in 1294, so the 1301 gain has no mirror, and deva-dynasty's identity.successors hands the Dhaka division to this state at the end of 1294 in the compile, so '1295-1300 nobody's land by design' (notes) does not hold.
  - Why: Compiler rules: a counterpart counts only while its dossier is alive; dissolve hands the remaining cells to identity.successors.
  - Fix: Counterpart nobody with the Devas in the note, or align with whatever end year deva-dynasty gets.
- Thin:
  - /ledger/1: Year of the Satgaon conquest and of Matuk's defeat (bridged to 1301, confidence 1). (try https://en.wikipedia.org/wiki/Satgaon)
  - /ledger/2: Year Sonargaon came under Lakhnauti (bridged to 1301, confidence 1). (try https://en.wikipedia.org/wiki/Sonargaon)
  - /ledger/3: Dates of the Bihar contest with the Delhi Khaljis (1301-1320 bridges); khalji-dynasty records no mirror. (try https://en.wikipedia.org/wiki/Alauddin_Khalji)
  - /ledger/5: End of the Bihar contest (1320 bridge). (try https://en.wikipedia.org/wiki/Shamsuddin_Firoz_Shah)
  - /keyframe_review/0: Kaikaus's reign 1291-1301 and the dynasty's link to Firoz Shah. (try https://en.wikipedia.org/wiki/Rukunuddin_Kaikaus)
- Spot checks:
  - /ledger/0, https://en.wikipedia.org/wiki/Bughra_Khan: confirmed: 'After the death of Ghiyasuddin in 1287, Bughra Khan declared independence of Bengal'
  - /ledger/4, https://en.wikipedia.org/wiki/Shamsuddin_Firoz_Shah: confirmed: 'According to an inscription Firuz Shah conquered Sylhet in 1303 CE'
  - /ledger/6, https://en.wikipedia.org/wiki/Ghiyath_al-Din_Tughluq: confirmed: 'In 1324, Tughluq turned his attention towards Bengal, then in the midst of a civil war'
  - /ledger/8, https://en.wikipedia.org/wiki/Ghiyath_al-Din_Tughluq: confirmed: 'placed Nasiruddin on the throne of West Bengal as a vassal state, and East Bengal was annexed'
- Area: No article of its own; 539-642 cells, the mamluk-dynasty 1285 handover plus dated additions.

## varman-dynasty-of-east-bengal: pass

- Thin:
  - /ledger: Ramapala's suzerainty over the Varmans and their independence under Madanapala (vassal_start/vassal_end with pala-empire; undated on the page). (try https://en.wikipedia.org/wiki/Pala_Empire)
- Spot checks:
  - /ledger/0, https://en.wikipedia.org/wiki/Varman_dynasty_(Bengal): confirmed: 'Jatavarman's rise to power sometime in between 1050 and 1075 AD'; Pala page: 'The Varmans occupied eastern Bengal during his reign' (Vigrahapala III)
  - /ledger/1, https://en.wikipedia.org/wiki/Vijaya_Sena: confirmed: 'Vijaya Sena ousted the Varmans from southeastern Bengal in the middle of the 12th century AD'
  - /ledger/2, https://en.wikipedia.org/wiki/Varman_dynasty_(Bengal): confirmed: defeated 'by Vijaysena of Sena dynasty and rule of Varmans over southeast Bengal came to an end'; infobox 1150
  - /identity/capitals/0, https://en.wikipedia.org/wiki/Varman_dynasty_(Bengal): confirmed: infobox 'Bikrampur; Champapuri'
- Area: Infobox area is words only (Vanga, Anga, Pundravardhana); acknowledged in the keyframe note. Tried and could not break: 0 cells overlap with pala-empire, sena-dynasty or kamarupa-kingdom keyframes 1072-1151; capital inside; land equals pala-empire /ledger/18 exactly.

## deva-dynasty: fail

- **/keyframe_review/0/correction** (blocking): The Dhaka division and the capital Bikrampur are drawn from 1230, but the page brings Bikrampur into the kingdom only under Dasharathadeva (the ruler allied with Balban in 1281).
  - Why: Deva dynasty page: Damodaradeva (reigned 1231-1243) 'was the most powerful ruler'; his kingdom reached 'the present-day Comilla- Noakhali- Chittagong region'; 'Ariraja-Danuja-Madhava Dasharathadeva extended his kingdom up to Bikrampur', which became his capital.
  - Fix: Draw 1230 onwards as A1:Chittagong (Comilla-Noakhali-Chittagong); add a gain of Bikrampur (e.g. {place Dhaka, km 40}, counterpart nobody or mamluk-dynasty) at a bridge year before 1281, confidence 1; start capitals/0 at that year and say the earlier seat is unknown; adjust /ledger/0, /ledger/1, /identity/predecessors/0/land and /identity/successors/0/land to match.
- **/keyframe_review/0/correction** (blocking): 54 of the 206 cells (western Dhaka division, Bikrampur, Sonargaon and Dhaka among them) are also held by mamluk-dynasty from 1236 (its 1236-1285 Cliopatria shapes) and by balbani-sultanate-of-bengal from 1287; the double claim is not flagged.
  - Why: Gazetteer: deva K0 intersect Mamluk Dynasty 1236/1250/1260/1285 shapes = 54 cells; intersect balbani K0 = 54. In the compile the Mamluk keyframe snap of 1236 takes them, capital included.
  - Fix: After the first fix, say in the note which side holds western Dhaka 1236-1294 and route mamluk-dynasty (/keyframe_review/8-11) and balbani K0 to subtract the Deva Bikrampur land from the year it is gained.
- Thin:
  - /ledger/0: Founding (infobox '12th century', Purushottamadeva); 1230 is a bridge at confidence 1. (try https://en.banglapedia.org/index.php/Deva_Dynasty)
  - /ledger/1: End of the dynasty (1294 last record, confidence 1) and where the eastern remnant went. (try https://en.banglapedia.org/index.php/Deva_Dynasty)
- Spot checks:
  - /ledger/0, https://en.wikipedia.org/wiki/Deva_dynasty: confirmed as a bridge: 'Damodaradeva (reigned 1231-1243)'; copperplates 1234, 1236, 1243; infobox 'Established: 12th century'
  - /ledger/1, https://en.wikipedia.org/wiki/Deva_dynasty: confirmed: 'moved to the eastern side of the kingdom in 1294'; 'This is the last recorded history of this dynasty'
  - /keyframe_review/0, https://en.wikipedia.org/wiki/Deva_dynasty: not on page for 1230: Bikrampur came under Dasharathadeva; Damodaradeva's land is Comilla-Noakhali-Chittagong
  - /wars/0, https://en.wikipedia.org/wiki/Deva_dynasty: confirmed: Danuj Rai 'made an alliance with Ghiyas-ud-Din Balban in 1281'
- Area: No infobox area; 206 cells.

## first-deva-dynasty: fail

- **/keyframe_review/0/correction** (blocking): The 716-899 shape is Cliopatria's whole Khadga 704 outline (294 cells, 32 of them in West Bengal), and pala-empire holds 253 of those cells from 750 and 289-290 from 806, so in the compile the Devas keep only the West Bengal fringe after 750 and almost nothing after 806: not Samatata and not their capital Devaparvata. Not flagged.
  - Why: Gazetteer: Khadga 704 intersect Pala Empire 750 = 253 of 294 cells, intersect Pala 806/850/899 = 289-290; Comilla 70 km disc is wholly inside Pala 750. Pala Empire page: Gopala (750-770) 'consolidating his power over the whole of Bengal including Gaur, Varendra and Banga'. Khadga infobox: 'Succeeded by: Deva Dynasty; Pala Empire'. Samatata page: the Devas ruled from Devaparvata near Comilla.
  - Fix: Draw the Devas at Samatata only (e.g. {place Comilla, km 70}, the land chandra-dynasty takes in 900) and resolve the Pala claim: either end the dossier at 750 (loss to pala-empire, confidence 1) or have pala-empire subtract Samatata from its 750-899 shapes; give the rest of the Khadga land to pala-empire or nobody at 716; say which in the note.
- **/identity/successors/0** (non-blocking): chandra-dynasty founds its kingdom in 900 on the same Comilla land from 'harikela-kingdom' (no dossier) and lists harikela-kingdom as predecessor, not this state.
  - Why: chandra-dynasty /ledger/0: 900 found, counterpart harikela-kingdom, region union(Comilla 70 km 'Samatata', Chattogram 70 km).
  - Fix: Route to chandra-dynasty to name first-deva-dynasty for the Samatata part (or explain the Harikela line), so the 900 handover is one story.
- Thin:
  - /ledger/0: Any date for the Devas' rise (716 is the Khadga end, confidence 1). (try https://en.banglapedia.org/index.php/Deva_Dynasty)
  - /ledger/1: Any date for the Devas' end (900 is the Chandra start, confidence 1). (try https://en.wikipedia.org/wiki/Mainamati)
- Spot checks:
  - /ledger/0, https://en.wikipedia.org/wiki/Khadga_dynasty: confirmed as a bridge: 'Disestablished: 716 CE'; 'succeeded by the 8th-9th century Buddhist Deva dynasty' (the infobox also names the Pala Empire as successor, which the dossier omits)
  - /ledger/1, https://en.wikipedia.org/wiki/Samatata: confirmed undated: 'They were succeeded by the Chandras'; timeline '8th century-9th century: First Deva dynasty'
  - /identity/capitals/0, https://en.wikipedia.org/wiki/Samatata: confirmed: Devaparvata 'identified with Kotbari area in Mainamati near Comilla City'
  - /identity, https://en.wikipedia.org/wiki/Deva_dynasty: confirmed split: 'This Hindu Vaishnava Deva dynasty is different from the earlier Buddhist Deva dynasty'
- Area: No page gives an area; the drawn shape is the Khadga 704 shape (90,427 km2 in shapes.csv) though the pages place the Devas only in Samatata; 86-99 percent of it is Pala land from 750.

## Cross-dossier matrix

- chutia-kingdom 1512 loss (counterpart ahom-kingdom) -> ahom-kingdom 1512 gain: **mismatch**. Same year and region, but the shared region (Assam x Dibrugarh 110 km) contains Sadiya, the Chutia capital to 1523; ahom-kingdom's 1228 disc (Dibrugarh 90 km) contains it too and lies wholly inside chutia K0. Route to both.
- chutia-kingdom 1513 contest_start (counterpart ahom-kingdom) -> ahom-kingdom 1513 contest_start: **matched**. ahom /ledger/3; contest_end 1523 /ledger/4.
- chutia-kingdom 1523 loss (counterpart ahom-kingdom) -> ahom-kingdom 1523 gain: **matched**. ahom /ledger/5, same region.
- kachari-kingdom 1526 loss (counterpart ahom-kingdom) -> ahom-kingdom 1526 contest_start: **mismatch**. ahom-kingdom has only a contest_start in 1526 (/ledger/6) and draws the land by keyframe; it records no 1526 gain. The Jorhat 110 km region on both sides contains the Dimapur cell (never annexed).
- kachari-kingdom 1536 loss (counterpart ahom-kingdom) -> ahom-kingdom 1536 gain: **matched**. ahom /ledger/8 (Nagaon 70 km); contest_end /ledger/7.
- kachari-kingdom 1745 gain (counterpart Khaspur (Koch rulers; no dossier)) -> no mirror: **exception**. Listed under counterparts_needing_dossiers (khaspur-state). But koch-bihar /ledger/1 gains the Barak valley in 1562 and never loses it; route koch-bihar to lose it to khaspur-state (or to kachari-kingdom in 1745).
- kachari-kingdom 1832 loss (counterpart east-india-company) -> east-india-company 1832 gain: **mismatch**. Year and region agree (/ledger/68) but its counterpart is the text 'Dimasa Kachari kingdom of Cachar (no dossier)': re-point to kachari-kingdom.
- kachari-kingdom 1834 loss (counterpart east-india-company) -> east-india-company 1834 gain: **mismatch**. Year and region agree (/ledger/72); re-point its counterpart text to kachari-kingdom.
- khalji-dynasty-of-bengal 1204 found (counterpart ghurid-dynasty) -> sena-dynasty 1204 loss: **mismatch**. sena-dynasty loses Bengal to ghurid-dynasty in 1204 (/ledger/9) and ghurid gains it in 1205 (/ledger/34); the Khalji 1204 claim on Lakhnauti conflicts with both.
- khalji-dynasty-of-bengal 1206 gain (counterpart ghurid-dynasty) -> ghurid-dynasty 1206 loss: **matched**. ghurid /ledger/38, identical region.
- khalji-dynasty-of-bengal 1215 loss (counterpart mamluk-dynasty) -> mamluk-dynasty 1215 gain: **matched**. mamluk /ledger/4 (Bihar).
- mamluk-dynasty 1225 vassal_start (counterpart khalji-dynasty-of-bengal) -> no mirror: **missing**. mamluk /ledger/9 (confidence 3) and vassal_end /ledger/11 (1227) have no mirror in khalji-dynasty-of-bengal.
- khalji-dynasty-of-bengal 1227 loss (counterpart mamluk-dynasty) -> mamluk-dynasty 1227 gain: **matched**. mamluk /ledger/12.
- balbani-sultanate-of-bengal 1287 found (counterpart mamluk-dynasty) -> mamluk-dynasty 1287 loss: **mismatch**. Year and region agree (/ledger/35) but its counterpart is the text "Bughra Khan's Bengal (Balbani rulers of Lakhnauti)": re-point to balbani-sultanate-of-bengal.
- balbani-sultanate-of-bengal 1301 gain (counterpart deva-dynasty) -> no mirror: **mismatch**. deva-dynasty dissolved in 1294 and its identity.successors already hands the Dhaka division to balbani then; 54 of those cells are in balbani K0 from 1287.
- balbani-sultanate-of-bengal 1301 gain (counterpart local rulers of Satgaon and the Sundarbans) -> no mirror: **exception**. No dossier; listed under counterparts_needing_dossiers.
- balbani-sultanate-of-bengal 1301 contest_start (counterpart khalji-dynasty) -> no mirror: **missing**. khalji-dynasty records no Bihar contest with Bengal (1301-1320); its shapes keep part of Bihar.
- balbani-sultanate-of-bengal 1303 gain (counterpart rulers of Sylhet) -> no mirror: **exception**. No dossier; listed under counterparts_needing_dossiers.
- balbani-sultanate-of-bengal 1325 loss (counterpart tughlaq-dynasty) -> tughlaq-dynasty 1325 gain: **matched**. tughlaq /ledger/6; contest 1324-1325 /ledger/4-5.
- varman-dynasty-of-east-bengal 1072 found (counterpart pala-empire) -> pala-empire 1072 loss: **matched**. pala /ledger/18, identical region.
- varman-dynasty-of-east-bengal 1152 loss (counterpart sena-dynasty) -> sena-dynasty 1152 gain: **mismatch**. Year agrees (/ledger/3); sena gains 366 cells, the Varmans hold 175 (flagged by the author); about 190 cells of the Sena gain have no Varman source.
- deva-dynasty 1230 found (counterpart sena-dynasty) -> sena-dynasty 1230 dissolve: **mismatch**. sena /ledger/11 hands 366 cells to deva-dynasty; the Deva takes 206 (Dhaka, Chittagong), and the page puts Bikrampur (Dhaka) in the kingdom only later.
- first-deva-dynasty 716 found (counterpart khadga-dynasty) -> khadga-dynasty 716 dissolve: **mismatch**. khadga /ledger/3 and identity.successors name deva-dynasty (the 13th-century state); re-point to first-deva-dynasty.
- first-deva-dynasty 900 dissolve (counterpart chandra-dynasty) -> chandra-dynasty 900 found: **mismatch**. chandra /ledger/0 founds from harikela-kingdom (no dossier) on the same Comilla land.

## Problems and routing

- deva-dynasty split accepted: the Deva dynasty page says the 13th-century Vaishnava Devas are 'different from the earlier Buddhist Deva dynasty'; khadga-dynasty identity.successors and /ledger/3 counterpart should be re-pointed from deva-dynasty to first-deva-dynasty (owner of khadga-dynasty).
- ahom-kingdom (not in this batch): its 1228 disc (Assam x Dibrugarh 90 km) and 1512 Habung disc contain Sadiya, the Chutia capital to 1523; its 1526 Jorhat 110 km disc contains the Dimapur cell (the Kachari capital, never annexed per the Ahom page). The chutia-kingdom and kachari-kingdom fixes need the Ahom regions changed too.
- mamluk-dynasty /ledger/35 (1287 loss) counterpart text should become balbani-sultanate-of-bengal; its 1236-1285 Cliopatria keyframes hold 54 cells of the Deva land (Bikrampur, Sonargaon, Dhaka).
- east-india-company /ledger/68 and /ledger/72 counterpart text should become kachari-kingdom.
- koch-bihar /ledger/1 (1562 Barak valley gain) is never undone; the Kachari 1745 gain and a future khaspur-state need it to lose the valley.
- chandra-dynasty names harikela-kingdom (no dossier) as the 900 source of Samatata, where first-deva-dynasty ends; one story is needed.
- WebFetch returns small-model summaries; the quotes above are as returned. No page failed to load.

## Gazetteer names needed

Sadiya (place, chutia-kingdom), Habung (place, chutia-kingdom), Dimapur (place, kachari-kingdom), Maibang (place, kachari-kingdom), Khaspur (place, kachari-kingdom), Lakhnauti (place, khalji-dynasty-of-bengal), Satgaon (place, balbani-sultanate-of-bengal), Sonargaon (place, balbani-sultanate-of-bengal), Bikrampur (place, deva-dynasty), Devaparvata (place, first-deva-dynasty), Samatata (region, first-deva-dynasty), Vanga (region, varman-dynasty-of-east-bengal).
