# Review of batch sa-03-x (Phase B, India additions)

Reviewer, 2026-10-19. Authors' report: history/notes/phase-b/reports/sa-03-x.json; notes: history/polities/_notes/sa-03-x.md. Machine copy: history/notes/phase-b/reviews/sa-03-x.json.

Method: validator with --resolve on all 15 (no errors; three slug warnings in chera-perumal-kingdom for kolathunadu and venad); every keyframe resolved on the H3 grid and intersected with the shapes of every neighbour dossier alive in the same years; capitals tested against the keyframe of their first year; counterpart ledgers read for every territorial event; 30 pages opened with WebFetch for spot checks (every confidence-3 event in the batch was checked and confirmed).

Verdicts: eastern-chalukyas **thin**, hindu-shahis **fail**, kalachuris-of-tripuri **thin**, licchavi-kingdom **thin**, thakuri-dynasty **thin**, tomara-dynasty **thin**, guhilas-of-mewar **fail**, chera-perumal-kingdom **thin**, emirate-of-multan **pass**, bhauma-kara-dynasty **thin**, somavamshi-dynasty **fail**, karnat-dynasty-of-mithila **thin**, kalachuris-of-ratnapura **fail**, ayudha-dynasty **fail**, kalachuris-of-kalyani **thin**.

## eastern-chalukyas: thin

- [applied] `/ledger/2/region, /ledger/3/region, /ledger/4/region, /ledger/5/region, /wars/2/zones/0, /wars/3/zones/0, /identity/predecessors/0/land`: The Vengi contest zones and the predecessor land were drawn as {"region":"Andhra"}, 1,044 cells (about 264,000 km2, all of Andhra Pradesh plus a strip of Telangana), 3.5 times the state's own 300-cell shape, while each text says Vengi. Evidence: Rajaraja I page: 'Satyashraya retaliated by invading the Vengi country in 1006 A.D.'; Kulottunga I page: 'the Vengi kingdom was invaded by the Kalachuri king Yakshakarna'; the dossier's own Vengi spec is Rajahmundry 110 km + Vijayawada 100 km. Fix: Replaced by the dossier's Vengi spec {"union":[{"place":"Rajahmundry","km":110},{"place":"Vijayawada","km":100}]}, texts kept; revalidated.
- `/keyframe_review/0/note`: The 624-847 keyframe draws Vengi as an independent state from 624, while chalukya-dynasty /ledger/8 keeps Vengi in Badami hands until its 641 loss: 184 of 185 cells are drawn by both in 624-641. Evidence: Eastern Chalukyas page: Kubja Vishnuvardhana was made 'the governor of this newly acquired territory in 624 A.D.' and the viceroyalty became independent 'possibly after Pulakeshin died fighting the Pallavas in the Battle of Vatapi' (642). Fix: Say in the K0 note that 624-641/642 Vengi is a Badami viceroyalty, and route to chalukya-dynasty: replace its 641 loss with vassal_start 624 / vassal_end 642 counterpart eastern-chalukyas (or keep the loss and move it to 642).
- `/ledger (973-999)`: No event for Jata Choda Bhima's usurpation of Vengi (973-999), when 'the Vengi kingdom was under the rule of Jata Choda Bhima, a member of the Telugu Cholas branch'; the dossier draws the Eastern Chalukyas continuously. Evidence: Rajaraja I page (quoted); Eastern Chalukyas page king list: 'Jata Choda Bhima (973 - 999) (usurp.)'. Fix: Add rename 973 (Telugu Choda usurper) and rename 999/1001 (Saktivarman restored under Chola protection), confidence 2, citing the Rajaraja I page; or a note if the state is treated as interrupted.
- [thin] `/ledger/3`: End of Satyashraya's hold on Vengi (contest_end 1006 is a confidence-1 bridge). Try: https://en.wikipedia.org/wiki/Satyashraya
- [thin] `/ledger/5`: End of Yakshakarna's 1073 raid (confidence-1 bridge). Try: https://en.wikipedia.org/wiki/Yashahkarna
- [thin] `/ledger (1031-1045)`: The Vengi succession war of 1031-1035 (Vijayaditya VII drives out Rajaraja Narendra) that chola-empire /ledger/25-26 records as a contest with eastern-chalukyas. Try: https://en.wikipedia.org/wiki/Rajaraja_Narendra
- [thin] `/identity/capitals`: Capital-move years 847/1017 are placeholders (no capital_move events). Try: https://en.wikipedia.org/wiki/Vengi
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/6 (confidence 3) confirmed; /ledger/7 (infobox 1189, lead c. 1001) confirmed.
- Area: No infobox area on the page and no Cliopatria row (new state); nothing to compare. Dossier maximum about 75,900 km2.

## hindu-shahis: fail

- `/keyframe_review/5/correction (and /keyframe_review/3, /keyframe_review/4)`: The 1002-1013 shape leaves out the Salt Range, so the capital Nandana (32.7 N, 72.9 E; identity.capitals, 1002-1014) lies outside it: 0 of the 12 cells within 30 km of Nandana are drawn. The shape is Gandhara-in-Punjab (37 cells, Attock/Rawalpindi), Islamabad and a 150 km Lahore disc, with a gap between them. Evidence: Hindu Shahis infobox: 'Nandana (1002–1014)'; K5 note itself: 'what is left is Gandhara east of the Indus ... and the Lahore country, with the capital at Nandana'. Fix: Add the Salt Range and Jhelum country (e.g. {"lon":72.9,"lat":32.7,"km":70} or a Salt Range gazetteer entry) to K3-K5 and to the 1014 loss region (/ledger/10), so the capital is inside the state.
- `/keyframe_review/1/correction, /keyframe_review/2/correction`: The 878-990 shapes are Gandhara + Kabulistan + Laghman only (300 cells); the Punjab, which both pages give to the Shahis before 999, is not drawn and no keyframe note says why. Evidence: Hindu Shahis lead: 'ruled Kabulistan, Gandhara and Punjab between 822 CE and 1026 CE'; Jayapala page: 'He ruled over the area which stretched from Lamghan in the west, to Kashmir in the east and from Sirhind to Multan.' Fix: Either add the Punjab east of the Indus (Salt Range, Jhelum, Chenab doab) to K1-K4 with a note on its extent, or state in the notes why it is left out; keep Multan out (it is emirate-of-multan's to 1010).
- [applied] `/wars/2/belligerents`: Free-text belligerent 'Multan (Daud)' where the dossier emirate-of-multan exists (same batch). Evidence: Anandapala page: Mahmud went to war and took Multan; emirate-of-multan /ledger/2 is the same 1006 campaign. Fix: Set to 'emirate-of-multan'.
- [applied] `/wars/4/belligerents`: 'lohara-principality' is not a slug of any dossier, and the war's own outcome names 'Sangramaraja of the Lohara dynasty'; lohara-dynasty (Kashmir, 1003-1339) exists. Evidence: Outcome text of the war; history/polities/lohara-dynasty.json identity. Fix: Set to 'lohara-dynasty'; drop lohara-principality from counterparts_needing_dossiers.
- [thin] `/ledger/6`: Battle of Peshawar day: 27 November (infobox/battle page) vs 27 September (Jayapala page: 'Jayapala met with Mahmud at Peshawar on 27 September 1001'); month 11 kept. Try: https://en.wikipedia.org/wiki/Battle_of_Peshawar_(1001)
- [thin] `/identity/rulers`: No ruler list with reign years. Try: https://en.wikipedia.org/wiki/Anandapala
- Spot checks: /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3-4 confirmed; /ledger/5 confirmed; /ledger/6 confirmed (year; day differs between pages, as the author notes); /ledger/7, /ledger/11, /ledger/12 confirmed.
- Area: No infobox area on the page and no Cliopatria row (new state); nothing to compare. Dossier maximum about 102,200 km2.

## kalachuris-of-tripuri: thin

- [applied] `/ledger/7/region, /ledger/8/region`: The 1073 Vengi raid zone was {"region":"Andhra"} (1,044 cells, about 264,000 km2) for a text that says 'the Vengi Chalukya kingdom'. Evidence: Yashahkarna page: 'Yashahkarna's raid on the Vengi Chalukya kingdom in 1073 CE'. Fix: Replaced by the Vengi spec (Rajahmundry 110 km + Vijayawada 100 km), the same as eastern-chalukyas; revalidated.
- [applied] `/wars/1/belligerents`: 'chalukya-dynasty' (the Badami Chalukyas, 543-757) named in a 1015-1041 war whose own note says the enemy is the page's 'Chalukyas of Kalyani'. Evidence: War note: 'Western Chalukya of Kalyani is the page's "Chalukyas of Kalyani"'. Fix: Set to 'western-chalukya-empire'.
- `/identity/start, /ledger/0`: The notes say the page gives no founding year, but its infobox lists '675–700: Vamaraja-deva (first)' and the text has Vama-raja 'established himself at Kalanjara in the late 7th century, and finally moved to Tripuri'; the dossier starts in 850 without saying why 675-849 is left out. Evidence: Kalachuris of Tripuri page, infobox and early history section. Fix: Either start the state c. 675 at Kalanjara/Tripuri (as a Pratihara subordinate, with the move to Tripuri) or keep 850 and explain in notes and /ledger/0 that the pre-Kokalla line is not drawn as a state.
- `/keyframe_review/0/correction`: K0 (850-1032) still draws Kalinjar and northern Baghelkhand, which chandela-kingdom /ledger/5 takes 'sometime before 954' from the Kalachuris; with chandela-kingdom's shapes 155 of Tripuri's 302 cells are drawn twice in 960-1032 (141-156 cells through 1151). Evidence: chandela-kingdom /ledger/5 quote: 'Sometime before 954, the Chandela dynasty under Yashovarman had captured Kalinjar from the Kalachuris'; the author's notes acknowledge the Kalinjar loss is not in this ledger. Fix: Add a loss of Kalinjar to chandela-kingdom by 954 (confidence 2, citing the Chandela page the neighbour cites) and trim K0 from 954; reconcile the Baghelkhand overlap with the chandela-kingdom author (route).
- [thin] `/ledger (1056-1074)`: Lata: paramara-dynasty /ledger/6 loses it to the Kalachuris in 1056 and chaulukya-dynasty /ledger/8 takes it from them 'By 1074' (confidence 3); no gain or loss here. Try: https://en.wikipedia.org/wiki/Karna_(Chaulukya_dynasty)
- [thin] `/ledger (c. 1035)`: Gangeya's gains 'at the expense of the Chandelas' (chandela-kingdom /ledger/7, 1035). Try: https://en.wikipedia.org/wiki/Vidyadhara_(Chandela_dynasty)
- [thin] `/ledger/3, /ledger/4, /ledger/10, /ledger/11, /ledger/12, /ledger/13, /ledger/8`: Seven confidence-1 bridges (Prayaga 1033, Devavarman 1050, Gahadavala 1085, Ratnapura 1123, Madanavarman 1152, end 1212, Vengi withdrawal). Try: https://en.wikipedia.org/wiki/Madanavarman
- Spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/4 confirmed; /ledger/5-6 confirmed ('around 1073' is the author's reading of 'By the end of his reign'); /ledger/7 confirmed; /ledger/9 confirmed; /ledger/10 confirmed (no year on the page; confidence 1 is honest); /ledger/13 confirmed.
- Area: No infobox area (the infobox map is 'Territory ... during the reign of Lakshmikarna, circa 1050 CE'); no Cliopatria row. Dossier maximum about 95,900 km2.

## licchavi-kingdom: thin

- [thin] `/keyframe_review/0/correction`: The text quotes settlement 'west toward Tistung Deurali, and northwest toward present-day Gorkha', but the 35 km Kathmandu disc (16 cells) does not reach Gorkha (about 75 km); either widen it or say the extension is settlement, not rule. Try: https://en.wikipedia.org/wiki/Licchavi_(kingdom)
- [thin] `/wars/0`: Tibetan role in Narendradeva's restoration (no page opened says it); the kingdom is a minor state, thin by design within its budget. Try: https://en.wikipedia.org/wiki/Narendradeva
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed ('when the Lichhavi rule came to an end').
- Area: No infobox area on the page and no Cliopatria row (new state); nothing to compare. Dossier maximum about 4,000 km2.

## thakuri-dynasty: thin

- [thin] `/sources`: One page only; the dynasty's existence 'is disputed by some historians'. Minor state, thin by design. Try: https://en.wikipedia.org/wiki/History_of_Nepal
- [thin] `/wars`: Nanyadeva's attack on Nuwakot (page: 'Nanyadeva, King of the Karnats of Mithila, attacked Nuwakot'), undated. Try: https://en.wikipedia.org/wiki/Nanyadeva
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed.
- Area: No infobox area on the page and no Cliopatria row (new state); nothing to compare. Dossier maximum about 4,000 km2.

## tomara-dynasty: thin

- `/ledger/0/counterpart, /keyframe_review/0/note`: The 736 found takes Haryana and Delhi from 'nobody', but kannauj-varman-dynasty's 732 and 768 shapes (Cliopatria 'ok') hold 162 of the 171 cells until 771; neither side has an event. Evidence: Overlap computed on the H3 grid; kannauj-varman-dynasty /ledger/4 (771) drops its periphery to 'unrecorded'. Fix: Name the overlap in the K0 note and route: kannauj-varman-dynasty /ledger/4 can name tomara-dynasty for the Haryana part, or the Tomara found counterpart becomes kannauj-varman-dynasty.
- `/ledger (736-c. 950)`: The infobox status 'Vassal state of the Gurjara-Pratihara dynasty (8th–10th century)' is not modelled anywhere; gurjara-pratihara-dynasty has no vassal event for the Tomaras. Evidence: Tomara dynasty infobox; 'As the Pratihara power declined, the Tomaras established a sovereign principality around Delhi by the 10th century.' Fix: Route to gurjara-pratihara-dynasty: vassal_start tomara-dynasty (from 736 or when its shape reaches Haryana) and vassal_end c. 950, citing the Tomara page; note it in /ledger/0.
- [thin] `/ledger/1`: The 1041 'gain' of Hansi and Thanesar is of land K0 already draws as Tomara; the earlier Ghaznavid capture (Hansi 1037) is not on the pages, so the ledger has a gain without a prior loss. Try: https://en.wikipedia.org/wiki/Mas%27ud_I_of_Ghazni
- [thin] `/ledger/4`: Chahamana vassalage 1152-1192 belongs in chauhan-dynasty (vassal_start counterpart tomara-dynasty). Try: https://en.wikipedia.org/wiki/Vigraharaja_IV
- Spot checks: /ledger/0 confirmed (footnote 736); /ledger/1 confirmed (no year on the page; confidence 1 honest); /ledger/3 (confidence 3) confirmed; /ledger/4 confirmed.
- Area: No infobox area on the page and no Cliopatria row (new state); nothing to compare. Dossier maximum about 43,200 km2.

## guhilas-of-mewar: fail

- `/ledger (later 10th century), /keyframe_review/1`: Missing loss: the author's main page says that after Munja's victory 'the Paramaras gained control of the eastern part of Mewar, including Chittorgarh'; K1 (728-1150) still draws all of Mewar with Chittor, and 99 of its 132 cells are also in paramara-dynasty's 980-1150 shapes. Evidence: Guhila dynasty page (section on Munja; he 'plundered their capital Ahar'); the notes list only 'Munja's sack of Ahar' as undated and miss the loss of eastern Mewar. Fix: Add loss c. 975 (bridge, Munja r. c. 972-990; confidence 1-2) of eastern Mewar with Chittorgarh to paramara-dynasty, split K1 at that year, and draw western Mewar (Nagda/Ahar) only until Chittor's return.
- `/ledger/2`: The 1151 loss of Chittor to chaulukya-dynasty is of land the page says was Paramara by then, and chaulukya-dynasty has no event naming the Guhilas. Evidence: Guhila page: 'By 1151, Chittor was under the control of the Chaulukya king Kumarapala.' (no Guhila loss stated). Fix: Once the c. 975 loss is in, drop this loss (the 1151 change is Paramara to Chaulukya) or reword it; keep the 1213 bridge regain.
- `/identity/capitals/1`: Chitrakuta (Chittor) is the capital from 1151, the year the ledger gives Chittor to the Chaulukyas (K2 1151-1212 excludes it): the capital lies outside the state for 1151-1212. The page names no move to Chittor ('Towards the end of the 10th century, Ahar became the second capital'). Evidence: Capital check on the grid: Chittorgarh at 1151 is OUTSIDE guhilas-of-mewar_1151; Guhila page. Fix: Keep Nagda/Ahar to 1212 and start Chittor in 1213 (or later), with the note that the page gives no year.
- `/ledger (728-c. 950)`: The Pratihara feudatory status is unmodelled; gurjara-pratihara-dynasty's 750 and 860 shapes cover all 132 cells of K1. Evidence: Guhila page: 'The Guhila kings initially ruled as feudatories of the Pratiharas during the 8th and the 9th century.' Fix: Route to gurjara-pratihara-dynasty: vassal_start/vassal_end guhilas-of-mewar for the 8th-9th centuries; say so in K1's note.
- [thin] `/ledger/3`: Date and taker of Chittor's return before 1213 (confidence-1 bridge). Try: https://en.wikipedia.org/wiki/Chittorgarh
- Spot checks: /ledger/0 confirmed (infobox 566); /ledger/1 confirmed; /ledger/2 confirmed (quote), but see fixes; /ledger/4 (confidence 3) confirmed; /ledger/5 confirmed.
- Area: No infobox area on the page and no Cliopatria row (new state); nothing to compare. Dossier maximum about 33,400 km2.

## chera-perumal-kingdom: thin

- `/notes, /keyframe_review/1/note`: The notes say the Chola overlordship 'is recorded in the chola-empire dossier (vassal_start counterpart chera-perumal-kingdom)'; it is not: chola-empire /ledger/15 gains southern Kerala (Kollam) in 1005 from 'venad' and /ledger/19 gains the whole Chera Perumal kingdom in 1018, and all 158 cells of K1 are in chola-empire's 1000-1124 shapes. Evidence: chola-empire ledger; Chera page: 'The Chera state in Kerala was subjugated during the reign of the Chola emperor Rajaraja I', Kerala 'for a time was held as an appanage by junior members of the Chola dynasty', and Kulottunga I's 1077-1081 campaign restored the Chera country 'to Chola authority' (Rama Varma Kulashekhara page). Fix: Reconcile with the chola-empire author: either the Cholas hold Kerala as a vassal (their 1005/1018 gains become vassal_start counterpart chera-perumal-kingdom, with an end) and this dossier says so, or this dossier records the appanage as a loss/occupation with a recovery. Correct the notes sentence either way.
- `/wars/0/zones`: Empty zones for the Chola subjugation of 1001-1014, though the page says the state was subjugated and held as an appanage (ground changed hands). Evidence: Chera Perumals of Makkotai page (quoted above). Fix: Give the zone (at least Kollam/Kandalur, the south) or the whole kingdom, per the reconciliation above.
- `/ledger/1, /ledger/5, /keyframe_review/1/correction`: Kolathunadu is drawn twice: as a vassal (vassal_start 1001 / vassal_end 1124, Kannur 90 km in Kerala) and as direct land inside K1 (Kerala up to the Chandragiri), while /ledger/2 subtracts it from the 1001 gain. Evidence: K1 correction is the union of Kerala (region) and Nagercoil, which contains the Kannur disc. Fix: Either subtract the Kolathunadu spec from K1 or drop the vassal pair and add it to the 1001 gain.
- [thin] `/ledger/1, /ledger/2`: Dates for the northern and southern extension and Kolathunadu's submission (11th century, bridged to 1001). Try: https://en.wikipedia.org/wiki/Kolathunadu
- [thin] `/identity/rulers`: No ruler list. Try: https://en.wikipedia.org/wiki/Chera_Perumals_of_Makkotai
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/3 confirmed; /ledger/4 confirmed (page: 'around c. 1102 AD', the note's 'by 1102' is a paraphrase); /ledger/6 confirmed (1126 Cholapuram inscription, Vira Kerala).
- Area: No infobox area on the page and no Cliopatria row (new state); nothing to compare. Dossier maximum about 40,000 km2.

## emirate-of-multan: pass

- Spot checks: /ledger/0 confirmed; /ledger/1 (confidence 3) confirmed; /ledger/2 (confidence 3) confirmed; /ledger/3-5 (confidence 3) confirmed.
- Area: No infobox area; the page's extent ('located in southern Punjab, bordered the Hindu Shahi kingdom in northern Punjab' and the Habbari emirate to the south) fits the 120 km Multan disc, which touches neither hindu-shahis nor sind-habbari-dynasty on the grid. Dossier maximum about 42,200 km2.

## bhauma-kara-dynasty: thin

- [thin] `/keyframe_review/1/correction`: The page says the kingdom 'included a major part of Odisha, as well as the Midnapore district of West Bengal'; Midnapore (about 260 km from Bhubaneswar) is outside the 170 km disc. Try: https://en.wikipedia.org/wiki/Bhauma-Kara_dynasty
- [thin] `/identity/successors`: The lead says the dynasty 'was supplanted by the Bhanjas and the Somavamshis in the 10th century'; the Bhanjas are not named. Try: https://en.wikipedia.org/wiki/Bhanja_dynasty
- [thin] `/ledger/1, /ledger/6, /ledger/7`: Three confidence-1 bridges (756 extension, 950 loss and end); one page only. Minor state, thin by design. Try: https://en.wikipedia.org/wiki/Somavamshi_dynasty
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2-5 confirmed; /ledger/7 confirmed (infobox last ruler 940-950).
- Area: No infobox area on the page and no Cliopatria row (new state); nothing to compare. Dossier maximum about 51,600 km2.

## somavamshi-dynasty: fail

- `/keyframe_review/0/correction, /ledger/0`: K0 (882-1020) includes Cuttack 70 km, 69 cells that bhauma-kara-dynasty (same batch) draws to 950; the 882 found names bhauma-kara-dynasty but bhauma-kara has no loss in 882, and its 950 loss to somavamshi-dynasty has no gain here. Evidence: Grid overlap 69/173 cells in 882-950; Somavamshi page: 'it is not known how exactly this happened'; Bhauma-Kara page lists rulers to 940-950. Fix: Pick one: draw K0 without the Bhauma-Kara land (Kosala only) and add a gain from bhauma-kara-dynasty in 950 matching its /ledger/6; or move bhauma-kara's loss of the Cuttack area to 882.
- `/keyframe_review/1/correction`: K1 (1021-1113) is all of Odisha (568 cells) including Kalinga (85 cells round Berhampur), drawn from an inscription title; 117 of eastern-ganga-kingdom's 162 cells are drawn by both in 1078-1113. The page's statement of control is only 'Kosala and Utkala'. Evidence: Somavamshi page: 'He re-established the Somavamshi control over Kosala and Utkala'; 'One of his inscriptions describes him as the lord of Kalinga, Kosala, and Utkala.' (Gazetteer note: 'Kalinga' and 'Utkala' both resolve to all of Odisha.) Fix: Draw Kosala and Utkala (western and northern/coastal Odisha) without southern Odisha, and say the Kalinga title is not drawn.
- [applied] `/ledger/1/counterpart`: Counterpart 'nobody' for land the page says 'had been lost to rival chiefs'. Evidence: Somavamshi page (quoted). Fix: Set to 'rival chiefs (unnamed on the page)'; revalidated.
- [thin] `/ledger (c. 1000-1050)`: Loss of 'some western parts' to the Kalachuris of Ratnapura (kalachuris-of-ratnapura /ledger/0 conquers Dakshina Kosala from the Somavamshis c. 1000). Try: https://en.wikipedia.org/wiki/Kalachuris_of_Ratnapura
- [thin] `/ledger/4`: eastern-ganga-kingdom /ledger/3 takes Utkala in 1118 ('Somavamshi dynasty', free text) against 'By 1114' here. Try: https://en.wikipedia.org/wiki/Anantavarman_Chodaganga
- [thin] `/identity/capitals`: The 1101 move to Jajpur is a placeholder (no capital_move event). Try: https://en.wikipedia.org/wiki/Jajpur
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 (confidence 3) confirmed; /ledger/4 confirmed.
- Area: No infobox area on the page and no Cliopatria row (new state); nothing to compare. Dossier maximum about 143,600 km2.

## karnat-dynasty-of-mithila: thin

- `/keyframe_review/0/correction`: The Muzaffarpur 100 km disc crosses the Ganges: 21 of 142 cells lie south of the river around Patna (Magadha), outside Tirhut/Mithila. Evidence: Grid check (cells below 25.62 N between 84.6 and 86.1 E); the correction text says 'Tirhut or Mithila in Bihar'. Fix: Subtract the land south of the Ganges (e.g. minus a Magadha/Patna spec) from K0 and the event regions.
- [thin] `/ledger/0`: pala-empire /ledger/21 loses Mithila to the Karnats in 1085 (confidence 1) and its 1097-1150 shapes still hold 66 of these 142 cells; the Karnat side (inscription of 10 July 1097) is the better date: route to pala-empire. Try: https://en.wikipedia.org/wiki/Ramapala
- [thin] `/ledger/2`: Karnat rulers held parts of Mithila into the 15th century (page); not drawn. Try: https://en.wikipedia.org/wiki/Oiniwar_dynasty
- Spot checks: /ledger/0 (confidence 3) confirmed; /ledger/1 confirmed; /ledger/2 (confidence 3) confirmed.
- Area: No infobox area on the page and no Cliopatria row (new state); nothing to compare. Dossier maximum about 35,900 km2.

## kalachuris-of-ratnapura: fail

- `/identity/end, /ledger/2, /keyframe_review/1`: The state is ended in 1225 (dissolve to 'nobody', confidence 1), but the author's own page says it lasted to 1758, so Chhattisgarh is left empty for 533 years. Evidence: Kalachuris of Ratnapura page: 'The kingdom survived until 1758, when its last ruler Mohan Singh died and the state was annexed by its suzerain'; 'In 1740, the general of the Maratha Nagpur Kingdom, Bhaskar Pant invaded the kingdom'; infobox 'Bimbaji Bhonsle becomes governor of Chhattisgarh: 1758'. Fix: Extend the life to 1758: keyframe(s) to 1758 (a bridge with a note that 1225-1740 is undocumented), the 1740 Maratha invasion (contest or vassal_start in the Maratha dossier), dissolve 1758 to maratha-empire (or a Nagpur Bhonsle dossier).
- `/ledger/1/region, /keyframe_review/1/correction`: The 1114 gain draws all of Chhattisgarh outside the Bilaspur disc, including Bastar; the page says Jajalla-deva I invaded the Chindaka Naga territory and took its king prisoner, and annexed southern Kosala 'which were under Telugu Choda governorship', not that he annexed the Naga country. 133 cells of K1 are also in kakatiya-dynasty's 1188-1225 shape. Evidence: Kalachuris of Ratnapura page: 'In 1114 CE, Jajalla-deva I invaded the Chindaka Naga territory to the south' ... 'defeated the Chindaka Naga king Somesvara and took him prisoner'. Fix: Draw southern Kosala without Bastar (or say in the note why Bastar is included), and split the counterpart: 'Telugu Choda governors' for the gain, the Chindaka Nagas only as a war.
- [thin] `/identity/predecessors`: somavamshi-dynasty has no loss for the c. 1000 conquest of Dakshina Kosala (route to that dossier). Try: https://en.wikipedia.org/wiki/Somavamshi_dynasty
- Spot checks: /ledger/0 confirmed; /ledger/1 (confidence 3) confirmed (year and southern Kosala; extent overdrawn); /ledger/2 not on page: the page has the kingdom survive to 1758.
- Area: No infobox area on the page and no Cliopatria row (new state); nothing to compare. Dossier maximum about 130,700 km2.

## ayudha-dynasty: fail

- `/ (whole dossier)`: Duplicate state: kannauj-varman-dynasty (sa-03-c, reviewed thin) already carries the Ayudhas as a rename of the Kingdom of Kannauj in 770 (/ledger/3, confidence 3), the 816 loss and dissolve to gurjara-pratihara-dynasty (/ledger/7-8), and 'Ayudha dynasty' in its alt_names; all 279 cells of ayudha-dynasty_770 lie inside kannauj-varman-dynasty_772, so Kannauj is drawn twice in 770-816. Evidence: Research brief rule 2 (a dynasty that replaces a dynasty on the same land is a rename); Ayudha page: 'The dynasty was established when Vajrayudha deposed the Varmans and started ruling over Kannauj.' gurjara-pratihara-dynasty /ledger/16 and pala-empire /ledger/4 already treat Kannauj 770-816 as one state. Fix: Withdraw history/polities/ayudha-dynasty.json and its new_slug; move anything new (the Chakrayudha page as a source, the c. 791 Pala installation) into kannauj-varman-dynasty, and ask the pala-empire author to set /ledger/4 and /ledger/8 counterpart 'Chakrayudha (Ayudha dynasty of Kannauj)' to kannauj-varman-dynasty.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed (no year on the page; infobox c. 816); /ledger/2 confirmed.
- Area: No infobox area on the page and no Cliopatria row (new state); nothing to compare. Dossier maximum about 70,600 km2.

## kalachuris-of-kalyani: thin

- `/keyframe_review/1/correction and the 1162-1184 event regions`: The 150 km Bidar disc puts 150 cells (about 38,000 km2) in Telangana and 21 in Andhra Pradesh, beyond the page's 'parts of present-day northern Karnataka and Maharashtra'; 94-150 of those cells are also kakatiya-dynasty's in 1163-1184. Evidence: Kalachuris of Kalyani lead; grid intersection with admin-1 Telangana / Andhra Pradesh; the K1 note calls the radii 'the researcher's reading' but does not mention Telangana. Fix: Intersect K1 and the event regions with Karnataka and Maharashtra (or cite a page for the Telangana districts).
- `/ledger/0, /keyframe_review/0`: 1156-1161 is drawn as an independent state, but Bijjala 'ruled initially as a vassal of Chalukya' and 'proclaimed independence in 1162'; western-chalukya-empire models 1157-1183 as a Kalachuri occupation of Kalyani (/ledger/28, /ledger/30), not a vassal or a loss. Evidence: Bijjala II page; Kalachuris of Kalyani ruler list; western-chalukya-empire ledger. Fix: Route: western-chalukya-empire to carry vassal_start/vassal_end kalachuris-of-kalyani 1156-1162 and a loss in 1162 / gain c. 1183-1184 instead of the occupation pair; this dossier to say in K0's note that 1156-1161 is a Chalukya feudatory.
- [thin] `/ledger/3, /ledger/4, /ledger/5`: Date and manner of the fall (1184 is the ruler list's last year; the infobox and lead give 1181; western-chalukya-empire has 1183). Try: https://en.wikipedia.org/wiki/Someshvara_IV
- Spot checks: /ledger/0 confirmed (infobox 1156-1181); /ledger/1 confirmed; /ledger/2 confirmed; /ledger/5 confirmed (ruler list to 1184).
- Area: No infobox area on the page and no Cliopatria row (new state); nothing to compare. Dossier maximum about 152,800 km2.

## Cross-dossier matrix (mismatches and missing mirrors)

- eastern-chalukyas 624 found chalukya-dynasty: **mismatch**. chalukya-dynasty /ledger/8 keeps Vengi to a 641 loss; 184 cells drawn twice 624-641. Page: independence possibly after Pulakeshin II died (642). Route: Badami vassal_start 624/vassal_end 642 counterpart eastern-chalukyas, or move its loss to 642.
- eastern-chalukyas 1006 contest_start western-chalukya-empire: **missing**. western-chalukya-empire has no 1006 Vengi event (route to that dossier: contest_start/contest_end eastern-chalukyas 1006).
- eastern-chalukyas 1006 contest_end western-chalukya-empire: **missing**. as above
- eastern-chalukyas 1077 loss chola-empire: **mismatch**. chola-empire /ledger/30 gains Vengi in 1075 (and ends its protectorate /ledger/29 in 1075); Kulottunga I page: 'After the death of Vijayaditya in 1077, Kulottunga brought the Vengi province directly under his control'. Route to chola-empire: move to 1077.
- eastern-chalukyas 1077 dissolve chola-empire: **mismatch**. as above (1075 vs 1077).
- kalachuris-of-tripuri 850 found gurjara-pratihara-dynasty: **missing**. gurjara-pratihara-dynasty has no vassal event for the Kalachuris (page: 'the Kalachuris were subordinate to the Pratihara emperor Bhoja'); route to that dossier.
- kalachuris-of-tripuri 1033 gain pala-empire: **missing**. pala-empire has no 1033 loss of Varanasi to the Kalachuris (route to pala-empire).
- kalachuris-of-tripuri 1033 gain unknown (page silent on who held Prayaga): **missing**. free-text counterpart
- kalachuris-of-tripuri 1055 contest_start paramara-dynasty: **mismatch**. paramara-dynasty /ledger/6 loses Lata to the Kalachuris in 1056 (a loss, not a contest), and chaulukya-dynasty /ledger/8 takes Lata from them by 1074; this dossier has neither the Lata gain nor the loss.
- kalachuris-of-tripuri 1073 contest_end paramara-dynasty: **mismatch**. see 1055.
- kalachuris-of-tripuri 1085 loss gahadavala-dynasty: **mismatch**. gahadavala-dynasty /ledger/0 (1085 found) and /ledger/1 (1090 gain of Kosala) name 'Kalachuri of Tripuri' as free text; same events, route: set the counterpart to kalachuris-of-tripuri.
- kalachuris-of-tripuri 1212 dissolve chandela-kingdom: **mismatch**. chandela-kingdom /ledger/13 gains northern Baghelkhand from the Kalachuris in 1202 (Cliopatria year, confidence 1); 10 years apart; the page gives no year.
- tomara-dynasty 736 found nobody: **mismatch**. counterpart nobody, but kannauj-varman-dynasty's 732/768 shapes hold 162 of 171 cells until 771 with no event; the Tomara infobox also calls it a Pratihara vassal (8th-10th century), which gurjara-pratihara-dynasty does not carry.
- guhilas-of-mewar 1151 loss chaulukya-dynasty: **mismatch**. chaulukya-dynasty has no event naming the Guhilas; the Guhila page has Chittor pass to the Paramaras after Munja (later 10th century) and be Chaulukya by 1151, so the Guhila loss belongs c. 975 to paramara-dynasty, which also has no event naming guhilas-of-mewar.
- guhilas-of-mewar 1213 gain unknown (page silent on who held Chittor): **missing**. free-text counterpart (unknown holder); bridge.
- chera-perumal-kingdom 1001 gain unknown (page silent on who held it): **missing**. free text (unknown holder); bridge.
- chera-perumal-kingdom 1097 contest_start chola-empire: **missing**. chola-empire has no 1097 Kollam contest; the nearest Chola events naming this state are /ledger/19 (1018 gain of the whole kingdom) and /ledger/15 (1005 gain of southern Kerala, counterpart venad): see reverse rows.
- chera-perumal-kingdom 1102 contest_end chola-empire: **missing**. no Chola 1097-1102 contest (route to chola-empire).
- bhauma-kara-dynasty 790 contest_start rashtrakuta-dynasty: **mismatch**. rashtrakuta-dynasty /ledger/4 gains Kalinga from bhauma-kara-dynasty in 772 and /ledger/25 loses it in 850 (both confidence 1, Cliopatria years); this dossier has a 790-829 contest. Route to rashtrakuta-dynasty: replace the gain/loss with the page's 790-829 contest.
- bhauma-kara-dynasty 790 contest_start pala-empire: **mismatch**. pala-empire /ledger/9-10 holds Utkala as a vassal 825-860 (confidence 1); this dossier ends the Pala invasions in 829. Route to pala-empire to align the end with 829 or cite a page.
- bhauma-kara-dynasty 829 contest_end rashtrakuta-dynasty: **mismatch**. see 790.
- bhauma-kara-dynasty 829 contest_end pala-empire: **mismatch**. see 790 (pala-empire vassal 825-860).
- bhauma-kara-dynasty 950 loss somavamshi-dynasty: **mismatch**. somavamshi-dynasty /ledger/0 takes the Cuttack area in 882 (found, counterpart bhauma-kara-dynasty) and has no 950 gain: 69 cells drawn twice 882-950 (fix on the Somavamshi side).
- bhauma-kara-dynasty 950 dissolve somavamshi-dynasty: **mismatch**. see 950 loss.
- somavamshi-dynasty 882 found bhauma-kara-dynasty: **mismatch**. bhauma-kara-dynasty /ledger/6 loses the land in 950, not 882.
- somavamshi-dynasty 1021 contest_start chola-empire: **missing**. chola-empire has no 1021 Yayatinagara raid (route).
- somavamshi-dynasty 1021 contest_end chola-empire: **missing**. as above.
- somavamshi-dynasty 1114 loss eastern-ganga-kingdom: **mismatch**. eastern-ganga-kingdom /ledger/3 gains Utkala from 'Somavamshi dynasty' (free text) in 1118; route: counterpart to somavamshi-dynasty and reconcile 1114 (Somavamshi page 'By 1114') with 1118.
- somavamshi-dynasty 1114 dissolve eastern-ganga-kingdom: **mismatch**. as above.
- karnat-dynasty-of-mithila 1097 found pala-empire: **mismatch**. pala-empire /ledger/21 loses Mithila to the Karnats in 1085 (confidence 1); the Simraungadh inscription dates Nanyadeva's taking of the land to 10 July 1097. Route to pala-empire: move to 1097.
- kalachuris-of-ratnapura 1000 found somavamshi-dynasty: **missing**. somavamshi-dynasty has no loss for Dakshina Kosala c. 1000 (Somavamshi page: Ratnapura 'conquered some western parts of the Somavamshis').
- kalachuris-of-ratnapura 1114 gain Telugu Chola governors (Chindaka Nagas): **missing**. free text (Telugu Choda governors / Chindaka Nagas); no dossiers.
- kalachuris-of-ratnapura 1225 dissolve nobody: **mismatch**. page has the kingdom survive to 1758 (see fixes).
- ayudha-dynasty 770 found kannauj-varman-dynasty: **mismatch**. duplicate of kannauj-varman-dynasty /ledger/3 (rename 770).
- ayudha-dynasty 816 loss gurjara-pratihara-dynasty: **mismatch**. gurjara-pratihara-dynasty /ledger/16 gains Kannauj from kannauj-varman-dynasty in 816: the same event under the other slug (duplicate state).
- ayudha-dynasty 816 dissolve gurjara-pratihara-dynasty: **mismatch**. as above; kannauj-varman-dynasty /ledger/8 is the dissolve.
- kalachuris-of-kalyani 1156 found western-chalukya-empire: **mismatch**. western-chalukya-empire /ledger/28 records a Kalachuri occupation of Kalyani from 1157 (confidence 3); the pages make 1156-1161 a Chalukya feudatory (independence 1162).
- kalachuris-of-kalyani 1162 gain western-chalukya-empire: **mismatch**. western-chalukya-empire has no 1162 loss; it has occupation 1157-1183.
- kalachuris-of-kalyani 1181 contest_start western-chalukya-empire: **missing**. western-chalukya-empire has no 1181-1184 contest.
- kalachuris-of-kalyani 1184 contest_end western-chalukya-empire: **missing**. as above.
- kalachuris-of-kalyani 1184 loss western-chalukya-empire: **mismatch**. western-chalukya-empire /ledger/30 ends the occupation in 1183 (a year apart, different type).
- kalachuris-of-kalyani 1184 dissolve western-chalukya-empire: **mismatch**. as above.
- chandela-kingdom 954 gain kalachuris-of-tripuri: **missing**. No 954 loss of Kalinjar in kalachuris-of-tripuri; its K0 still draws Kalinjar to 1032 (155 cells drawn twice 960-1032).
- chandela-kingdom 1035 loss kalachuris-of-tripuri: **missing**. No Gangeya gain at Chandela expense in kalachuris-of-tripuri.
- chandela-kingdom 1070 gain kalachuris-of-tripuri: **mismatch**. kalachuris-of-tripuri /ledger/9 ends Chandela vassalage in 1075 (no land loss).
- paramara-dynasty 1056 loss kalachuris-of-tripuri: **missing**. No Lata gain in kalachuris-of-tripuri (it has a Malwa contest 1055-1073).
- chaulukya-dynasty 1074 gain kalachuris-of-tripuri: **missing**. No Lata loss in kalachuris-of-tripuri; the Chaulukya event is confidence 3.
- chola-empire 1005 gain venad: **mismatch**. Southern Kerala (Kollam) in 1005 belongs to chera-perumal-kingdom, which has no loss; venad is independent only from c. 1124-1126. Route: counterpart chera-perumal-kingdom, and reconcile with the Chera dossier (vassal or loss).
- chola-empire 1018 gain chera-perumal-kingdom: **mismatch**. chera-perumal-kingdom draws all Kerala as its own 1001-1124 and says the Chola relation is overlordship; the Chera page has subjugation and a temporary appanage. 158 cells drawn twice 1018-1124.
- chola-empire 1031 contest_start eastern-chalukyas: **missing**. The 1031-1045 Vengi succession war is not in eastern-chalukyas.
- pala-empire 791 vassal_start Chakrayudha (Ayudha dynasty of Kannauj): **mismatch**. Free-text counterpart for the Kannauj state, which is kannauj-varman-dynasty; ayudha-dynasty is a duplicate to withdraw.
- gurjara-pratihara-dynasty 750 (shape) guhilas-of-mewar: **missing**. Pratihara 750-960 shapes hold all 132 cells of Guhila K1 with no vassal event; the Guhila page calls them Pratihara feudatories in the 8th-9th centuries (route: vassal_start/vassal_end guhilas-of-mewar).
- paramara-dynasty 980 (shape) guhilas-of-mewar: **missing**. Paramara 980-1150 shapes hold 99 of Guhila K1's 132 cells (eastern Mewar with Chittor, per the Guhila page); neither ledger has the c. 975 transfer.
- kakatiya-dynasty 1163 (shape) kalachuris-of-kalyani: **mismatch**. 94-150 cells of western Telangana drawn by both 1163-1184; the Kalyani page names only Karnataka and Maharashtra (fix on the Kalyani side).
- kakatiya-dynasty 1188 (shape) kalachuris-of-ratnapura: **mismatch**. 133 cells of southern Chhattisgarh (Bastar side) drawn by both 1188-1225.
- eastern-ganga-kingdom 1078 (shape) somavamshi-dynasty: **mismatch**. 117 of eastern-ganga-kingdom's 162 cells (southern Odisha) are inside Somavamshi K1 1078-1113 (fix on the Somavamshi side).

## Problems and routing

- Verdicts: 1 pass, 9 thin, 5 fail (hindu-shahis, guhilas-of-mewar, somavamshi-dynasty, kalachuris-of-ratnapura, ayudha-dynasty).
- ayudha-dynasty duplicates kannauj-varman-dynasty (sa-03-c), which already carries the Ayudhas as a 770 rename to 816; the orchestrator should withdraw ayudha-dynasty.json and its new_slug rather than send it back for edits.
- Reviewer-applied fixes (all revalidated, read back): eastern-chalukyas and kalachuris-of-tripuri Vengi zones ({region: Andhra} replaced by the Vengi spec, 9 places); kalachuris-of-tripuri /wars/1 chalukya-dynasty -> western-chalukya-empire; hindu-shahis /wars/2 'Multan (Daud)' -> emirate-of-multan and /wars/4 lohara-principality -> lohara-dynasty; somavamshi-dynasty /ledger/1 counterpart nobody -> rival chiefs.
- The author's counterparts_needing_dossiers lists lohara-principality, but lohara-dynasty (Kashmir 1003-1339) exists; drop it.
- Gazetteer: 'Kalinga' and 'Utkala' both resolve to all of Odisha (568 cells), the same as {region: Odisha}; they need separate entries (southern Odisha with coastal north Andhra; northern coastal Odisha).
- Neighbour dossiers to route (all already failed or thin in earlier reviews): chola-empire (1075 vs 1077 Vengi; 1005 counterpart venad; 1018 Chera gain), chalukya-dynasty (641 Vengi), pala-empire (1085 Mithila -> 1097; Chakrayudha free text; 1033 Varanasi loss missing), rashtrakuta-dynasty (772/850 Bhauma-Kara), gurjara-pratihara-dynasty (vassal Tomaras, Guhilas, Kalachuris), paramara-dynasty (c. 975 Chittor), gahadavala-dynasty and eastern-ganga-kingdom (free-text counterparts), western-chalukya-empire (Kalyani occupation pair vs feudatory/independence), chandela-kingdom (Baghelkhand overlap with Tripuri).
- Groups not yet run, treated as exceptions: ghaznavid-empire, saffarid-dynasty, abbasid-caliphate (me-08); khalji-dynasty, tughlaq-dynasty, mamluk-dynasty (sa-04); kathmandu (later group).
- No page failed to load. No infobox in the batch gives an area, and no state has a Cliopatria row, so the area checks are empty by construction; overlaps were measured on the H3 grid against neighbour dossiers instead.

## Gazetteer names wanted

Vengi (eastern-chalukyas), Salt Range (hindu-shahis), Nandana (hindu-shahis), Udabhandapura (Hund) (hindu-shahis), Baghelkhand (Dahala) (kalachuris-of-tripuri), Tripuri (Tewar) (kalachuris-of-tripuri), Kalinjar (Kalanjara) (kalachuris-of-tripuri), Rewa (kalachuris-of-tripuri), Kathmandu Valley (licchavi-kingdom), Gorkha (licchavi-kingdom), Nuwakot (thakuri-dynasty), Hansi (tomara-dynasty), Thanesar (tomara-dynasty), Nagda (guhilas-of-mewar), Ahar (guhilas-of-mewar), Kodungallur (Mahodayapuram) (chera-perumal-kingdom), Kolathunadu (chera-perumal-kingdom), Venad (chera-perumal-kingdom), Chandragiri river (chera-perumal-kingdom), Toshala (bhauma-kara-dynasty), Jajpur (bhauma-kara-dynasty), Utkala (northern Odisha; now resolves to all of Odisha) (somavamshi-dynasty), Kalinga (southern Odisha and coastal Andhra; now resolves to all of Odisha) (somavamshi-dynasty), Dakshina Kosala (kalachuris-of-ratnapura), Binka (Yayatinagara) (somavamshi-dynasty), Tirhut / Mithila (karnat-dynasty-of-mithila), Simraungadh (karnat-dynasty-of-mithila), Darbhanga (karnat-dynasty-of-mithila), Ratanpur (kalachuris-of-ratnapura), Bastar (kalachuris-of-ratnapura), Basavakalyan (Kalyani) (kalachuris-of-kalyani), Mangalvedha (kalachuris-of-kalyani).
