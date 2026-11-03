# Review af-03-a (Sahel empires, part a)

Reviewer, 2026-10-19. Validator: 0 errors on all five dossiers (warnings only for counterpart slugs without dossiers). Neighbour dossiers read: almoravid-dynasty (the only Context polity written so far). Machine copy: history/notes/phase-b/reviews/af-03-a.json.

| slug | verdict |
| --- | --- |
| ghana-empire | pass |
| sosso-empire | pass |
| takrur | pass |
| mali-empire | thin |
| empire-of-kanem | fail |

## ghana-empire: pass

Could not break it: all four events checked are on the page with their years; Awdaghust exclave 990-1053 matches the page; area gap acknowledged; Almoravid side has Awdaghust in its 1054 found event. Minor, non-blocking: war 'Sosso conquest of Ghana' 1200-1203 runs past the end year 1201 (natural for a hand-over war).

Area: infobox 650000 (1000) vs Cliopatria 204203, ratio 0.31. keyframe 0 note reads the infobox figure as the tribute sphere; resolved in favour of the shape

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Ghana_Empire: confirmed: 'In 990, presumably for commercial and economic reasons, the Ghana Empire conquered Awdaghust and installed its own governor.'
- `/ledger/2` https://en.wikipedia.org/wiki/Ghana_Empire: confirmed: 'Awdaghost, at the time a seat of the king, fell to the Almoravids in 1054.'
- `/ledger/3` https://en.wikipedia.org/wiki/Ghana_Empire: confirmed: 'By 1203, the Sosso had risen against their masters and conquered Ghana'; Sosso infobox 'Capture of Wagadu: c. 1200'; 1201 is an honest bridge at confidence 2
- `/ledger/0` https://en.wikipedia.org/wiki/Ghana_Empire: confirmed: king list 'Dyabe Cisse: circa 790s'; infobox 'Established: c. 300', not mapped and said so

## sosso-empire: pass

Could not break it: events match the page, the confidence-1 bridge is flagged, Ghana and Mali mirrors match within a year. Minor, non-blocking: war 'Sosso conquest of Ghana' 1200-1203 starts before the start year 1202.

Area: infobox None (None) vs Cliopatria 204203, ratio None. no area in the Sosso infobox (checked); the shape is cell for cell the Ghana shape, flagged and corrected by adding the Koulikoro seat

Gaps for a gap-filler:
- `/ledger/2`: Year of Soumaoro Kante's subjugation of the Manden chieftaincies (1227 is a confidence-1 bridge to Cliopatria's shape break); also the dates of the conquests of Diarra and Gajaaga (try https://en.wikipedia.org/wiki/Soumaoro_Kante)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Sosso_Empire: confirmed: infobox 'Capture of Wagadu: c. 1200'
- `/ledger/2` https://en.wikipedia.org/wiki/Sosso_Empire: confirmed undated: 'He conquered Diarra and Gajaaga and subdued the Mandinka chieftaincies to the south' (no year; confidence 1 is honest)
- `/ledger/3` https://en.wikipedia.org/wiki/Sosso_Empire: confirmed: 'At the Battle of Kirina (c. 1235)...'; 'the entire Kaniaga region was incorporated into Sundiata's Mali Empire'
- `/identity/capitals/0` https://en.wikipedia.org/wiki/Sosso_Empire: confirmed: 'The capital, a town of that name, still exists in Mali, near Boron in the Koulikoro Region' (Koulikoro proxy point lies inside the corrected shape)

## takrur: pass

Could not break it: the four Cliopatria shapes are one outline (1056 differs by 364 km2), so three events suffice within the 5-page budget; the 1285 hand-over matches Mali's 1285 gain. Minor, non-blocking: war 'War Jabi's holy war against Silla' 1035-1040 starts before the start year; identity.successors land cites the Takrur 1235 shape, the same outline as 1227.

Area: infobox None (None) vs Cliopatria 74105, ratio None. no area in the Takrur infobox (checked)

Gaps for a gap-filler:
- `/ledger/0`: A dated founding with territory (page: 'Established: 9th century'; War Jabi 'died around 1040-1041'); 1040 is Cliopatria's year at confidence 1 (try https://en.wikipedia.org/wiki/War_Jabi)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Takrur: confirmed: 'Around 1286, the Mali Empire conquered Takrur and put it under a military dictatorship ruled by farba (governors)'; infobox 'Conquered and vassalized by Mali Empire: c. 1285'
- `/keyframe_review/3` https://en.wikipedia.org/wiki/Takrur: confirmed: the extension of the 1227 shape to 1285 rests on the dated page; the Mali dossier removes Takrur until 1285 consistently
- `/ledger/0` https://en.wikipedia.org/wiki/Takrur: confirmed: 'In 1035 king War Jabi introduced Sharia law'; 'He died around 1040-1041'
- `/notes (no Ghana vassalage)` https://en.wikipedia.org/wiki/Takrur: confirmed: the page calls Takrur 'roughly parallel to the Ghana Empire' and a counter to it, not a vassal

## mali-empire: thin

Every dated event checked (seven) is on the page with its year, including both confidence-3 events; no fabrication. Keyframes and ledger agree (Takrur and the Niger bend taken out until their dated gains; 1436-1474 losses carried by new keyframes). Thin because the two largest border moves (1241 and 1475) and the 1415 growth rest on confidence-1 bridges or silence; within budget (8 pages for a 5-page budget).

Area: infobox 100000 (1250) vs Cliopatria 973312, ratio 9.73. Acknowledged in keyframes 0-1 and resolved for the shape against the infobox (1236-1240 cut to the Sosso lands, about 341,000 km2; full outline from 1241 at confidence 1). Other infobox years agree: 1350 1,300,000 vs 973,312 (0.75); 1380 1,100,000 (0.88); 1500 400,000 vs 346,027 (0.87). All quoted figures match the infobox.

Findings:
- `/identity/successors` (to do): No successor is named although the page says where the land went. Evidence: Mali Empire page: 'State divided among Emperor Mahmud Keita IV's sons: 1610'; the dossier's own dissolve note quotes 'Kangaba became the last refuge of the Keita royal family'. Fix: Add a successors entry for the Manden remnant (Kangaba, or 'nobody' for the sons' petty chiefdoms) with land {cliopatria: Mali Empire, year: 1609}. Non-blocking.
- `/ledger/7/counterpart` (to do): Counterpart 'songhai-empire' for Gao in 1300, while the author's own report proposes a separate kingdom-of-gao (1000-1463) for pre-imperial Gao. Evidence: Songhai Empire's Cliopatria row starts 1463 and the dossier's own note dates Songhai independence to the 1430s; a gain from songhai-empire in 1300 needs that dossier to exist in 1300. Fix: Pick one: keep songhai-empire only if the af-03 Songhai dossier starts by 1300 (Gao kingdom inside it), otherwise use kingdom-of-gao here and at /ledger/11. Non-blocking; routed in cross_checks.
- `/ledger/4/counterpart` (to do): vassal_start of 'jolof-empire' in 1241, but the author lists jolof-empire with years 1360-1549 in counterparts_needing_dossiers. Evidence: The dossier's own note: 'The Jolof Empire proper is founded only c. 1360 (Jolof page); the page's Jolof is the earlier Wolof kingdom.' Fix: Either the Jolof dossier starts by 1241 (as a Mali vassal until 1360) or this vassal is named 'Jolof (Wolof kingdom, no dossier)'; tell af-03-x which. Non-blocking.

Gaps for a gap-filler:
- `/ledger/2..5 and /keyframe_review/1`: Dates of Sundiata's and his generals' conquests (Diafunu, Kita, Senegambia, Jolof vassalage, Oualata, Audaghost): the biggest move in the dossier (about 341,000 km2 in 1236-1240 to about 809,000 km2 from 1241) rests on four confidence-1 bridges (try https://seshat-db.com/core/polity/ml_mali_emp/)
- `/ledger/14`: The 1475 loss (862,000 to 346,000 km2, the second-largest move) is a confidence-1 bridge; the Songhai side (Sunni Ali's campaigns, Djenne 1473) may date it (try https://en.wikipedia.org/wiki/Sunni_Ali)
- `/keyframe_review/3`: The 1415 growth (+141,000 km2) is unexplained by any page (marked unverified: page silent) (try https://seshat-db.com/core/polity/ml_mali_emp/)
- `/ledger/18`: End of the Wuli suzerainty is bridged to 1610 (confidence 1) (try https://en.wikipedia.org/wiki/Wuli)

Spot checks:
- `/ledger/8` https://en.wikipedia.org/wiki/Mali_Empire: confirmed: 'the scholarly city of Timbuktu, which he peaceably annexed in 1324'
- `/ledger/10` https://en.wikipedia.org/wiki/Mali_Empire: confirmed: 'In 1433-1434, the Empire lost control of Timbuktu to the Tuareg, led by Akil Ag-Amalwal.'
- `/ledger/12` https://en.wikipedia.org/wiki/Mali_Empire: confirmed: 'Three years later, Oualata also fell into their hands.'
- `/ledger/13` https://en.wikipedia.org/wiki/Mali_Empire: confirmed: 'The rising Songhai Empire conquered Mema, one of Mali's oldest possessions, in 1465.'
- `/ledger/15` https://en.wikipedia.org/wiki/Mali_Empire: confirmed: Askia Muhammad I 'defeated the Mali general Fati Quali Keita in 1502' and 'seized the province of Diafunu'
- `/ledger/17 and /ledger/19` https://en.wikipedia.org/wiki/Mali_Empire: confirmed: Wuli 'by 1576'; 'Around 1610, Mahmud Keita IV died'

## empire-of-kanem: fail

All eight dated events checked are on the pages (no fabrication; one confidence-3 region overstated, fixed). Fails on keyframe/ledger consistency: the Kanem shape is placed outside Kanem, the 1350-1380 drawing drops Kanem and Bornu with no event, Bornu shrinks from about 331,000 to 13,500 km2 between 1349 and 1381 with no event, and the 1482/1487 corrections subtract the wrong Kanem.

Area: infobox None (None) vs Cliopatria 339371, ratio None. No area anywhere on the Kanem-Bornu page (checked); the author says so.

Findings:
- `/keyframe_review/0` (to do): empire-of-kanem_1072 is kept 'ok' as 'the core round Njimi', but the Cliopatria shape lies wholly outside Kanem and does not contain the dossier's own capital point. Evidence: Kanem-Bornu page: 'with a core territory in the region of Kanem (northeast of Lake Chad)'; 'The empire's first capital was probably Njimi, east of Lake Chad'. Gazetteer: the 1072 shape (15.09-16.65 E, 11.30-12.64 N, 19,220 km2) intersects the 'Kanem' region (13.52-17.94 E, 13.05-16.76 N) in 0 cells; the Njimi point (15.31 E, 14.12 N) is 1.5 degrees north of the shape. The note's 'Cliopatria's shape is a seventh of it' is wrong: it is disjoint. Fix: Verdict adjust (or wrong) with correction {"region": "Kanem", "text": "a core territory in the region of Kanem (northeast of Lake Chad)"} for 1072-1249; same for the found event's region (/ledger/0).
- `/keyframe_review/1 and /keyframe_review/2` (to do): The zenith keyframe ends in 1349, after which the drawn empire falls back to the 20,000 km2 Cliopatria patch for 1350-1380, but the ledger loses only the Fezzan in 1350: Kanem and the Bornu region vanish with no event. Evidence: Dunama page: 'the empire would maintain its grip on these lands until the middle of the 14th century' refers to the Fezzan only; 'The region of Bornu was firmly under imperial control'; Kanem is lost only c. 1380 (/ledger/4). Cliopatria's empire-of-kanem_1072 shape spans 1072-1374 and resumes after the new 1250-1349 keyframe ends; ledger /ledger/3 removes only {region: Fezzan}. Fix: Add a new keyframe 1350-1380 = the 1250 correction minus the Fezzan (Kanem plus the Bornu land), and make keyframe 2 (1375 shape) adjust to the same; or extend keyframe 1 to 1380 with the Fezzan removed in the ledger as now.
- `/keyframe_review/3 and /keyframe_review/4` (to do): Bornu is drawn 1250-1349 as the gazetteer 'Bornu' region (about 331,000 km2, to 18 N) but from 1381 as Cliopatria's 13,538 km2 core west of the lake, with no ledger event for the difference. Evidence: Gazetteer 'Bornu' resolves to Borno + Yobe and beyond (9.8-16.66 E, 10.14-18.0 N); bornu-empire_1385 is 11.8-13.5 E, 12.8-13.9 N. The Kanem-Bornu page calls Bornu 'a former tributary territory established in the 13th century'; the Dunama page has Dunama reach 'as far south as Mafoni in modern day Borno State'. No event between 1250 and 1381 shrinks Bornu. Fix: Draw the 13th-century Bornu land as what the pages name (e.g. Borno State to Mafoni, or the 1385 core) in keyframe 1, or add the dated loss that shrinks it; keep the 1381 move consistent with what was held.
- `/keyframe_review/5/correction and /keyframe_review/6/correction` (to do): The 1482 and 1487 corrections take out the Cliopatria Kanem shape (south-east of the lake), not Kanem, so 1487-1499 still draws about 34,000 km2 of the Kanem region as Bornu while the ledger has Kanem in Bilala hands 1380-1500. Evidence: Gazetteer: intersect(Bornu Empire 1487, region Kanem) = 135 cells, about 34,142 km2 (13.52-16.13 E, 13.05-15.09 N); intersect(Bornu 1482, Kanem) = about 4,805 km2. /ledger/4 loses and /ledger/7 regains {region: Kanem}. Fix: Use {"minus": [{"cliopatria": "Bornu Empire", "year": 1482|1487}, {"region": "Kanem"}]} so the keyframes match the ledger.
- `/ledger/13/confidence` (applied by reviewer): Confidence 3 for a region (the whole Extreme-Nord province of Cameroon) that the page does not name. Evidence: al-Kanemi page: 'after defeating the Bagirmi in 1824' ... 'the occupation of the Kotoko kingdom city states of Kousseri, Ngulfai, and Logone'; the page names three towns, not the province. Fix: Lowered to 2 by the reviewer, with a note. The author may also narrow the region to those towns (Kousseri needs a gazetteer entry) and consider the Kotoko city states as counterpart instead of Bagirmi.
- `/ledger/11/region/text` (to do): The region text names districts (Hadejia, Katagum, Jamaare, Misau, Deya) that the event's own note says the page does not list. Evidence: al-Kanemi page: 'It does not state how much territory was lost'; only 'the Bornu Fulani began advancing further into Bornu territory'. Fix: Put the page's words in text, or mark the district list as the researcher's reading. Non-blocking.

Gaps for a gap-filler:
- `/ledger/0`: Founding c. 700 (Duguwa) and the Sayfawa change 'second half of the 11th century'; 1072 is a confidence-1 bridge (try https://seshat-db.com/core/polity/td_kanem/)
- `/ledger/2 and /ledger/3`: Years for Bornu's incorporation under Dunama and for the loss of the Fezzan (confidence 1) (try https://en.wikipedia.org/wiki/Fezzan)
- `/ledger/8 and /ledger/9`: Dates of Idris Alooma's Kanem expeditions and the Bilala treaty (contest 1570-1603 at confidence 1) (try https://en.wikipedia.org/wiki/Idris_Alooma)
- `/ledger/14`: Year the Fulani were driven out ('later in the 1820s', bridged to 1827) (try https://en.wikipedia.org/wiki/Fulani_War)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Kanem%E2%80%93Bornu_Empire: confirmed: 'In the mid-13th century, Kanem ruled the Fezzan as far as Waddan.'
- `/ledger/2 and /keyframe_review/1` https://en.wikipedia.org/wiki/Dunama_Dibbalemi: confirmed: 'The region of Bornu was firmly under imperial control'; Fezzan grip 'until the middle of the 14th century'; reign approximately 1221-1259
- `/ledger/4 and /ledger/7` https://en.wikipedia.org/wiki/Kanem%E2%80%93Bornu_Empire: confirmed: 'around the year 1380, the Bilala were able to oust the Sayfawa from power in Kanem'; 'reconquered by ... Idris III Katagarmabe in the early 1500s'
- `/ledger/10` https://en.wikipedia.org/wiki/Kanem%E2%80%93Bornu_Empire: confirmed: 'In 1808, under mai Ahmad Alimi, the Fulani captured and destroyed Ngazargamu.'
- `/ledger/13` https://en.wikipedia.org/wiki/Muhammad_al-Amin_al-Kanemi: year confirmed; region not named on the page (three Kotoko towns, not Extreme-Nord): confidence lowered to 2
- `/ledger/16 and /ledger/17` https://en.wikipedia.org/wiki/Rabih_az-Zubayr: confirmed: 'battle of Amja, in May 1893'; 'In February/March 1894, Rabih intercepted Kyari's army near Gashegar'; rule from 2 October 1893 (infobox)
- `/identity/capitals` https://en.wikipedia.org/wiki/Kanem%E2%80%93Bornu_Empire: confirmed: infobox 'Njimi (c. 700-1380); None (c. 1380-1472); Ngazargamu (c. 1472-1809); None (1809-1813); Kafela (1813-1846); Kukawa (1846-1893)': the two capital gaps are the page's

## Cross-dossier matrix

- ghana-empire 990 gain <- Awdaghust: exception; a city, no state; nothing to mirror
- ghana-empire 1054 loss <- almoravid-dynasty: matched (mirror almoravid-dynasty 1054 found); Almoravid found event of 1054 takes Sijilmasa and Awdaghust (region and year agree) but names no counterpart; af-02 may add ghana-empire there
- ghana-empire 1201 loss <- sosso-empire: matched (mirror sosso-empire 1202 gain); Cliopatria hand-over 1201/1202, one year apart by design
- sosso-empire 1227 gain <- Mandinka chieftaincies of the Manden: exception; no state named by the page
- sosso-empire 1235 loss <- mali-empire: matched (mirror mali-empire 1236 gain); Kirina c. 1235; Mali starts 1236
- takrur 1285 loss <- mali-empire: matched (mirror mali-empire 1285 gain); both c. 1285 from the Takrur page
- mali-empire 1241 gain <- Diafunu and Kita (local chiefdoms): exception; no state named
- mali-empire 1241 gain <- Senegambian chieftaincies: exception; no state named
- mali-empire 1241 gain <- Oualata and Audaghost (holders not named): exception; no holder named
- mali-empire 1241 vassal_start <- jolof-empire: exception; no jolof-empire dossier yet (af-03-x); author lists it 1360-1549, but this vassal relation needs it from 1241 or a different counterpart
- mali-empire 1360 vassal_end <- jolof-empire: exception; no dossier yet (af-03-x)
- mali-empire 1300 gain <- songhai-empire: exception; songhai-empire.json not written yet (af-03 Songhai part); it must begin by 1300 (Gao kingdom) or the counterpart becomes kingdom-of-gao as the author's own counterpart list proposes
- mali-empire 1324 gain <- Timbuktu (city): exception; city, no state named
- mali-empire 1433 loss <- Tuareg under Akil Ag-Amalwal: exception; listed as tuareg-of-timbuktu needing a dossier
- mali-empire 1436 loss <- Tuareg under Akil Ag-Amalwal: exception; listed as tuareg-of-timbuktu needing a dossier
- mali-empire 1435 loss <- songhai-empire: exception; songhai-empire.json not written yet (af-03 Songhai part); it should carry a gain from mali-empire in this year
- mali-empire 1465 loss <- songhai-empire: exception; songhai-empire.json not written yet (af-03 Songhai part); it should carry a gain from mali-empire in this year
- mali-empire 1475 loss <- songhai-empire: exception; songhai-empire.json not written yet (af-03 Songhai part); it should carry a gain from mali-empire in this year
- mali-empire 1502 loss <- songhai-empire: exception; songhai-empire.json not written yet (af-03 Songhai part); it should carry a gain from mali-empire in this year
- mali-empire 1537 loss <- kaabu: exception; kaabu listed as needing a dossier (af-03-x)
- mali-empire 1576 vassal_start <- Wuli: exception; no dossier; Wuli is in the author's notes but missing from the report's counterparts list (added here)
- mali-empire 1610 vassal_end <- Wuli: exception; as above
- empire-of-kanem 1250 gain <- Fezzan rulers: exception; no state named
- empire-of-kanem 1250 gain <- Sao / Bornu region: exception; no state named
- empire-of-kanem 1350 loss <- Fezzan rulers: exception; no state named
- empire-of-kanem 1380 loss <- Bilala: exception; bilala-kingdom listed as needing a dossier (af-03-x)
- empire-of-kanem 1500 gain <- Bilala: exception; as above
- empire-of-kanem 1809 loss <- sokoto-caliphate: exception; sokoto-caliphate.json not written yet (af-03 other part); it should carry a 1809 gain from empire-of-kanem (not bornu-empire)
- empire-of-kanem 1824 gain <- bagirmi-sultanate: exception; bagirmi-sultanate listed as needing a dossier (af-03-x); the page's land is the Kotoko city states
- empire-of-kanem 1894 loss <- state-of-rabih-az-zubayr: exception; listed as needing a dossier

## Batch-wide observations (non-blocking)

- Wars that straddle a hand-over run outside the life: ghana-empire and sosso-empire 'Sosso conquest of Ghana' 1200-1203, takrur 'War Jabi's holy war' 1035-1040, mali-empire 'Battle of Kirina' 1235-1236. Natural for hand-over wars; no change asked.
- Gazetteer lacks Njimi, Kukawa, Kafela, Kousseri, Waddan, Mema, Diafunu, Kaabu, Wuli, Kita, Sosso, Kirina, Kaniaga, Tumbere Jiinge; the authors used proxies.

## Problems

- No page failed to load for the reviewer (8 WebFetch reads: Ghana Empire, Takrur, Sosso Empire, Mali Empire, Kanem-Bornu Empire, Muhammad al-Amin al-Kanemi, Rabih az-Zubayr, Dunama Dibbalemi).
- bornu-empire is merged into empire-of-kanem (one Wikipedia article, one Wikidata id): the af-03 parts writing wadai-empire and sokoto-caliphate must name empire-of-kanem as counterpart, and no bornu-empire.json should be written.
- Only almoravid-dynasty of the four Context polities has a dossier; songhai-empire, sokoto-caliphate and wadai-empire are not written yet, so their mirrors are recorded as exceptions (group not run yet). songhai-empire must start by 1300 or Mali's 1300 counterpart changes to kingdom-of-gao.
- Reviewer edit applied: empire-of-kanem /ledger/13 confidence 3 -> 2 (re-validated: 0 errors; read back after the write).
