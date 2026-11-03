# Review: batch sa-01-x (Indus to the Mahajanapadas, additions)

Adversarial review filled by the orchestrator on 2026-10-18, run 2026-10-19. Nineteen new dossiers (no Cliopatria rows). The machine copy is history/notes/phase-b/reviews/sa-01-x.json.

## What was done

- Validator on all 19 with `--resolve`: 0 errors, 0 warnings.
- Every ledger event (51) and the one dated war was checked on its cited page (25 pages opened). No event is fabricated; no event is mis-dated except where the pages themselves conflict and the author says so.
- Every keyframe correction was resolved with history/tools/gazetteer.py: each area quoted in a note matches the resolution. None of the 19 pages gives an infobox area, so the area check is by extent only.
- Capitals checked against the resolved bboxes: all inside. Overlaps computed against neighbours: anga-kingdom/videha 15 cells (about 3,800 km2); shakya/koliya 1 cell; painted-grey-ware-culture/kuru-kingdom by design; none against indus-valley-civilization.
- Neighbour dossiers: macedonian-empire (eu-02) read; ptolemaic-kingdom not written yet (me-05, not run). Counterpart dossiers read: janapada-of-gandhara, -kuru, -pancala, -kasi, -anga, -vajji, -kosala, -surasena, -vatsa, indus-valley-civilization, mahajanapadas.

## Verdicts

### painted-grey-ware-culture: pass

- Thin at `/keyframe_review/1/correction`: Infobox 'Geographical range: North India, Eastern Pakistan': the Ghaggar-Hakra sites in Pakistan (Cholistan) are not in either keyframe; the page names no Pakistani site, so a gap-filler needs a site page. Page to try: https://en.wikipedia.org/wiki/Cholistan_Desert
- Thin at `/ledger/2`: Dissolve counterpart is the umbrella dossier 'mahajanapadas' (type umbrella, never territory); the land goes to the janapada successors listed in identity.successors. Harmless, but 'nobody' or the main successor would be cleaner. Page to try: https://en.wikipedia.org/wiki/Painted_Grey_Ware_culture
- Spot checks (3): /ledger/0 confirmed on Painted_Grey_Ware_culture; /ledger/1 confirmed on Painted_Grey_Ware_culture; /ledger/2 confirmed on Painted_Grey_Ware_culture
- Area: Infobox has no area; no Cliopatria row. Reviewer resolved every keyframe with history/tools/gazetteer.py: figures match the ones quoted in the keyframe notes. Resolved: {'K0': 73088, 'K1': 204849}.

### ochre-coloured-pottery-culture: pass

- Thin at `/ledger/1`: Confidence 1: -1900 is a bridging year for 'reached the Gangetic plain in the early 2nd millennium'. Page to try: https://en.wikipedia.org/wiki/Copper_Hoard_culture
- Thin at `/keyframe_review/0/correction`: The page says the culture extends 'from eastern Punjab to northeastern Rajasthan' with sites 'along the banks of Sahibi River' (Haryana); both keyframes subtract Haryana, Indian Punjab and Delhi to leave them to indus-valley-civilization (to -1300). Flagged by the author; a gap-filler should decide whether the Sahibi sites are OCP's. Page to try: https://en.wikipedia.org/wiki/Ochre_Coloured_Pottery_culture
- Spot checks (3): /ledger/0 confirmed on Ochre_Coloured_Pottery_culture; /ledger/1 confirmed on Ochre_Coloured_Pottery_culture; /ledger/2 confirmed on Ochre_Coloured_Pottery_culture
- Area: Infobox has no area; no Cliopatria row. Reviewer resolved every keyframe with history/tools/gazetteer.py: figures match the ones quoted in the keyframe notes. Zero overlap with every resolvable indus-valley-civilization keyframe. Resolved: {'K0': 36923, 'K1': 164891}.

### hindush: fix

- Fix at `/wars/0/from` (applied by the reviewer): The war 'Achaemenid conquest of the Indus Valley' ran -535..-518, starting 17 years before this dossier's life (-518..-325); hindush is not among its belligerents. Evidence: Reviewer brief check 2 (wars inside the life). Conquest page: 'Around 518 BCE, the Persian army pushed further into India ... annexing regions up to the Jhelum River'; the c. 535 Cyrus phase is Gandara's and is already in gandara /wars/0. Fix: from set to -518 and the note says why.
- Thin at `/ledger/3`: No page dates the end of Persian control in the Indus lands between Gaugamela (331) and Peithon's appointment (c. 325); the conquest page's infobox end '323 BCE' and 'under Achaemenid dominion at least until 338 BCE' are unexplained. Sambos and Musicanus (lower Indus) are undrawn. Page to try: https://en.wikipedia.org/wiki/Musicanus
- Spot checks (4): /ledger/0 confirmed on Sindhu-Sauv%C4%ABra; /ledger/1 confirmed on Achaemenid_conquest_of_the_Indus_Valley; /ledger/2 confirmed on Indian_campaign_of_Alexander_the_Great; /ledger/3 confirmed on Peithon_(son_of_Agenor)
- Area: Hindush infobox has no area (fields: Darius I 513-499 first, Darius III last, 'Persian conquest of the Indus Valley: c. 513 BCE', preceded by Sindhu-Sauvira, succeeded by Macedonian Empire). No Cliopatria row; the author's claim that the Cliopatria Achaemenid row covers 254 of Sindh's 562 cells in -500..-405 and none from -404 was reproduced by the reviewer. Resolved: {'K0': 234944, 'K1': 207884}.

### sindhu-sauvira: pass

- Thin at `/keyframe_review/0`: Nothing dated between c. 1000 and 518 BCE (thin by design under the 2-5 page budget); Sindhu and Sauvira are not separated. Page to try: https://en.wikipedia.org/wiki/Sauvira_Kingdom
- Spot checks (2): /ledger/0 confirmed on Sindhu-Sauv%C4%ABra; /ledger/1 confirmed on Sindhu-Sauv%C4%ABra
- Area: Infobox has no area; no Cliopatria row. Reviewer resolved every keyframe with history/tools/gazetteer.py: figures match the ones quoted in the keyframe notes. Resolved: {'K0': 207884}.

### gandara: fix

- Fix at `/wars/1/to` (applied by the reviewer): The Indian campaign war ran to -325 in this dossier, two years past the satrapy's end (-327), with gandara as a belligerent. Evidence: Reviewer brief check 2. Gandara page: 'In 327 BCE, Alexander the Great conquered Gandhara as well as the Indian satrapies of the Persian Empire'; the Assakenoi sieges (April 326) come after the dossier's dissolve. Fix: to set to -327 and the note says why.
- Thin at `/identity/successors`: Infobox 'Succeeded by: Kingdom of Taxiles, Peucelaotis, Kingdom of Abisares, Kingdom of Assacani' (c. 330-327) are not drawn; the author lists them under counterparts_needing_dossiers. Page to try: https://en.wikipedia.org/wiki/Taxiles
- Spot checks (2): /ledger/0 confirmed on Achaemenid_conquest_of_the_Indus_Valley; /ledger/1 confirmed on Gand%C4%81ra
- Area: Gandara infobox has no area. No Cliopatria row; the reviewer reproduced the author's count of the Cliopatria Achaemenid row covering 132 of the 193 Gandhara cells in -350. Resolved: {'K0': 59432}.

### videha: pass

- Thin at `/ledger/1`: Confidence 1: the dissolve year -601 is the hand-over convention; the page gives 'c. 7th century BCE' and 'around the 7th or 6th century BCE'. Page to try: https://en.wikipedia.org/wiki/Vajjika_League
- Spot checks (2): /ledger/0 confirmed on Videha; /ledger/1 confirmed on Videha
- Area: Infobox has no area; no Cliopatria row. Reviewer resolved every keyframe with history/tools/gazetteer.py: figures match the ones quoted in the keyframe notes. 15 cells (about 3,800 km2) north of the Ganga near Bhagalpur are also claimed by anga-kingdom: see that dossier. Resolved: {'K0': 60443}.

### kuru-kingdom: thin

- Thin at `/identity/capitals/0`: The page says 'The first capital was at Asandivat, identified with modern Assandh in Haryana' and lists Hastinapura and Indraprastha as later seats; the dossier has Hastinapura for the whole life -1200..-601 (its note mentions Asandivat). A dated capital sequence is needed. Page to try: https://en.wikipedia.org/wiki/Hastinapur
- Thin at `/ledger`: 'By the 6th century BCE, the dynasty had split into the Kuru and Vatsa kingdoms' has no split event (Vatsa's Kausambi lies outside the Kuru shape, so no area is unexplained, but the relation is missing). Also 'declined in importance during the late Vedic period (c. 900 - c. 500 BCE)' without a shape change. Page to try: https://en.wikipedia.org/wiki/Vatsa
- Thin at `/ledger/1`: Confidence 1 dissolve at the -601 convention year. Page to try: https://en.wikipedia.org/wiki/Mahajanapadas
- Spot checks (3): /ledger/0 confirmed on Kuru_Kingdom; /ledger/1 confirmed on Mahajanapadas; /wars/0 confirmed on Kuru_Kingdom
- Area: Infobox has no area; no Cliopatria row. Reviewer resolved every keyframe with history/tools/gazetteer.py: figures match the ones quoted in the keyframe notes. Overlaps painted-grey-ware-culture by 37,429 km2 (-1200..-1001) and 49,316 km2 (-1000..-601) by design ('the state wins'), flagged by the author. Resolved: {'K0': 52350}.

### panchala-kingdom: pass

- Thin at `/ledger/1`: Confidence 1 dissolve at -601; the page dates the switch to a republic 'around 500 BCE'. The 'later' division into northern (Ahichchhatra) and southern (Kampilya) Panchala is undated, so both capitals run concurrently for the whole life. Page to try: https://en.wikipedia.org/wiki/Ahichchhatra
- Spot checks (2): /ledger/0 confirmed on Panchala_kingdom; /ledger/1 confirmed on Panchala_kingdom
- Area: Infobox has no area; no Cliopatria row. Reviewer resolved every keyframe with history/tools/gazetteer.py: figures match the ones quoted in the keyframe notes. Resolved: {'K0': 45522}.

### ahar-banas-culture: pass

- Thin at `/ledger/1`: Confidence 1: the hand-over of the Madhya Pradesh sites (Jawad, Mandsaur, Kayatha, Dangwada) to the Malwa culture in -1600 rests on the two pages' date ranges. Page to try: https://en.wikipedia.org/wiki/Gilund
- Spot checks (3): /ledger/0 confirmed on Ahar%E2%80%93Banas_culture; /ledger/1 confirmed on Malwa_culture; /ledger/2 confirmed on Ahar%E2%80%93Banas_culture
- Area: Infobox has no area; no Cliopatria row. Reviewer resolved every keyframe with history/tools/gazetteer.py: figures match the ones quoted in the keyframe notes. Zero overlap with every resolvable indus-valley-civilization keyframe. Resolved: {'K0': 72329, 'K1': 51844}.

### malwa-culture: pass

- Thin at `/keyframe_review/0/correction`: The whole Malwa region (154,500 km2) is drawn from eight named sites (Daimabad, Inamgaon, Kayatha, Nagda, Vidisha, Eran, Mandsaur, Navdatoli); the author flags that a smaller shape may be better. L1 (-1600 gain) is confidence 1. Page to try: https://en.wikipedia.org/wiki/Daimabad
- Spot checks (4): /ledger/0 confirmed on Malwa_culture; /ledger/1 confirmed on Malwa_culture; /ledger/2 confirmed on Jorwe_culture; /ledger/3 confirmed on Malwa_culture
- Area: Infobox has no area; no Cliopatria row. Reviewer resolved every keyframe with history/tools/gazetteer.py: figures match the ones quoted in the keyframe notes. Resolved: {'K0': 178042, 'K1': 154522}.

### jorwe-culture: thin

- Thin at `/keyframe_review/1`: 'Most Jorwe culture sites were abandoned around 1000 BCE, possibly due to famine or drought' is a page-stated contraction with no event: K1 keeps 290,835 km2 (Maharashtra plus the whole Malwa region) to -700. A gap-filler should find where the c. 700 survivors were (e.g. Inamgaon's late Jorwe) and add a -1000 loss to nobody. Page to try: https://en.wikipedia.org/wiki/Inamgaon
- Thin at `/ledger/2`: 'also reached north into the Malwa region of Madhya Pradesh' names only Navdatoli; the -1300 gain of the whole Malwa region (154,500 km2) is a generous reading at confidence 2. Page to try: https://en.wikipedia.org/wiki/Navdatoli
- Spot checks (4): /ledger/0 confirmed on Jorwe_culture; /ledger/1 confirmed on Jorwe_culture; /ledger/2 confirmed on Jorwe_culture; /ledger/3 confirmed on Jorwe_culture
- Area: Infobox has no area; no Cliopatria row. Reviewer resolved every keyframe with history/tools/gazetteer.py: figures match the ones quoted in the keyframe notes. Resolved: {'K0': 136313, 'K1': 290835}.

### gandhara-grave-culture: pass

- Thin at `/keyframe_review/0/correction`: The spread from the Swat core to Dir, Kunar, Chitral and Peshawar is undated, so the whole 73,000 km2 is drawn from -1200 (flagged by the author). Page to try: https://en.wikipedia.org/wiki/Timergara
- Spot checks (2): /ledger/0 confirmed on Gandhara_grave_culture; /ledger/1 confirmed on Gandhara_grave_culture
- Area: Infobox has no area; no Cliopatria row. Reviewer resolved every keyframe with history/tools/gazetteer.py: figures match the ones quoted in the keyframe notes. Resolved: {'K0': 73088}.

### southern-neolithic-ashmound-tradition: pass

- Thin at `/keyframe_review/0/correction`: Of the six discs, Raichur and Kurnool are not named on the page (it names Ballari, Kalaburagi, the Tungabhadra, Krishna and Hagari valleys and the sites Utnur, Budihal, Kupgal, Hallur, Sanganakallu, Palavoy); the K0 note's 'named districts' overstates it. They sit in the named Tungabhadra-Krishna valleys, so the shape stands at confidence 2. Page to try: https://en.wikipedia.org/wiki/Sanganakallu
- Spot checks (2): /ledger/0 confirmed on Neolithic_ashmounds; /ledger/1 confirmed on Neolithic_ashmounds
- Area: The Neolithic ashmounds page has no infobox. No Cliopatria row. Resolved area matches the author's figure. Resolved: {'K0': 113805}.

### kingdom-of-tambapanni: fix

- Fix at `/ledger/0/confidence` (applied by the reviewer): Confidence 3 on a region the cited page does not name. Evidence: Tambapanni page: the landing was 'an area near modern-day Mannar, which is believed to be the district of Chilaw'; Puttalam is not on it (only the Upatissa Nuwara page has 'Tambapanni, which was in present-day Puttalam'). The 543 date is the chronicle tradition ('traditionally starts in 543 BC'). Fix: Confidence 2, with a reviewer sentence in the note.
- Fix at `/ledger/0/note` (applied by the reviewer): The quotation was not verbatim. Evidence: The page reads 'Sinhalese history and the historical period of Sri Lanka traditionally starts in 543 BC with the arrival of Prince Vijaya'. Fix: Quotation replaced with the page's words.
- Fix at `/ledger/2/confidence` (applied by the reviewer): Confidence 3 on the same unnamed Puttalam disc. Evidence: Infobox 'Kingdom moved to Anuradhapura: 437 BC' confirms the year, but the region is the same placeholder disc the page does not name. Fix: Confidence 2, with a reviewer sentence in the note.
- Fix at `/identity/rulers` (applied by the reviewer): The ruler list stopped at Abhaya (-474..-454), leaving the last 17 years without a ruler. Evidence: Infobox monarchs: '543-505 BC: Vijaya', '505-504 BC: Upatissa', '504-474 BC: Panduvasdeva', '474-454 BC: Abhaya', '454-437 BC: Tissa'. Fix: Added {name: Tissa, from: -454, to: -437} citing the Tambapanni page.
- Thin at `/wars`: Infobox 'Nineteen Years' War: 458-439 BC' (the succession war that ends with the move to Anuradhapura in 437) is not in wars[]; a gap-filler should add it with empty zones if no land changed hands. Page to try: https://en.wikipedia.org/wiki/Pandukabhaya_of_Anuradhapura
- Thin at `/identity/capitals`: Infobox capitals 'Tambapanni, Upatissagama, Vijithapura': Vijithapura is missing; the -505 capital move is confidence 1 (undated on both pages). Page to try: https://en.wikipedia.org/wiki/Anuradhapura_Kingdom
- Thin at `/keyframe_review/0/correction`: Extent on neither page; the 50 km Puttalam disc is a placeholder (author flagged). Page to try: https://en.wikipedia.org/wiki/Anuradhapura_Kingdom
- Spot checks (3): /ledger/0 confirmed on Kingdom_of_Tambapanni; /ledger/1 confirmed on Kingdom_of_Upatissa_Nuwara; /ledger/2 confirmed on Kingdom_of_Tambapanni
- Area: Infobox has no area; no Cliopatria row. Reviewer resolved every keyframe with history/tools/gazetteer.py: figures match the ones quoted in the keyframe notes. Resolved: {'K0': 4299}.

### shakya: thin

- Thin at `/ledger/0`: Confidence 1: the page gives only 'c. 7th century BCE' for the start. Page to try: https://en.wikipedia.org/wiki/Kapilavastu
- Thin at `/ledger/1`: Confidence 1: 'Conquered by Vidudabha of Kosala: c. 5th century BCE', 'Shortly after the Buddha's death'; -460 is bridging. The vassalage to Kosala ('Status: Vassal state of Kosala'; 'By that time [6th century BCE], the Shakya republic had become a vassal state') belongs in janapada-of-kosala as vassal_start/vassal_end for shakya and is not there yet. Page to try: https://en.wikipedia.org/wiki/Vidudabha
- Spot checks (2): /ledger/0 confirmed on Shakya; /ledger/1 confirmed on Shakya
- Area: Infobox has no area; no Cliopatria row. Reviewer resolved every keyframe with history/tools/gazetteer.py: figures match the ones quoted in the keyframe notes. One cell (253 km2) shared with koliya along the Rohini; negligible. Resolved: {'K0': 4046}.

### koliya: thin

- Thin at `/ledger/0`: Confidence 1: 'c. 7th century BCE' only. Page to try: https://en.wikipedia.org/wiki/Ramagrama
- Thin at `/ledger/1`: Confidence 1: 'Conquered by Vidudabha of Kosala: c. 5th century BCE'; -460 is bridging. Capital conflict Ramagama (infobox) / Devadaha (body) flagged by the author. Page to try: https://en.wikipedia.org/wiki/Vidudabha
- Spot checks (2): /ledger/0 confirmed on Koliya; /ledger/1 confirmed on Koliya
- Area: Infobox has no area; no Cliopatria row. Reviewer resolved every keyframe with history/tools/gazetteer.py: figures match the ones quoted in the keyframe notes. Resolved: {'K0': 3541}.

### kingdom-of-porus: fix

- Fix at `/ledger/1/note` (applied by the reviewer): The note said 'Porus annexes the land of Glausae' and quoted 'Annexing the territories of Glausae', dropping the page's subject: the annexation was Alexander's, the land went to Porus. Evidence: Porus page: his territory 'was not only restored, but also expanded, with Alexander's forces annexing the territories of Glausaes, who ruled to the northeast of Porus' kingdom'. Fix: Note rewritten with the page's words; the gain itself (land to Porus, -326, confidence 2) stands.
- Thin at `/ledger/0`: Confidence 1 found at -326 ('Reign: before 326'); the kingdom before Alexander is undated. Page to try: https://en.wikipedia.org/wiki/Puru_(Vedic_tribe)
- Thin at `/ledger/1`: Counterpart 'Glausae' is a free-text people with no dossier and is not in the author's counterparts_needing_dossiers (added in this report). Page to try: https://en.wikipedia.org/wiki/Partition_of_Triparadisus
- Spot checks (5): /ledger/0 confirmed on Porus; /ledger/1 confirmed on Porus; /ledger/2 confirmed on Battle_of_the_Hydaspes; /ledger/3 confirmed on Peithon_(son_of_Agenor); /ledger/4 confirmed on Porus
- Area: Porus page has no area. No Cliopatria row. K1's note quotes both the band (about 105,000 km2 added) and the total (156,000 km2); the reviewer's resolution gives 156,292. Resolved: {'K0': 50833, 'K1': 156292}.

### kashi-kingdom: pass

- Thin at `/ledger`: The page says earlier Kosalan kings 'Vanka and Dabbasena reportedly gained suzerainty over Kasi' before Kamsa's final conquest; undated, so no vassal events. The shape is the Varanasi core (15,000 km2) while the page gives the Syandika river (north) and the Son (south and east) as bounds. Page to try: https://en.wikipedia.org/wiki/Kosala
- Spot checks (2): /ledger/0 confirmed on Kashi_Kingdom; /ledger/1 confirmed on Kashi_Kingdom
- Area: Infobox has no area; no Cliopatria row. Reviewer resolved every keyframe with history/tools/gazetteer.py: figures match the ones quoted in the keyframe notes. Resolved: {'K0': 15174}.

### anga-kingdom: thin

- Fix at `/keyframe_review/0/correction` (not applied, for the author): The Bhagalpur 60 km disc crosses the Ganga and overlaps videha by 15 cells (about 3,800 km2, 86.58-87.47E, 25.31-25.72N) for the whole -800..-601. Evidence: Videha page: Videha is bounded by 'the Ganga river in the south'; Anga page: 'Anga proper was located between the Champa river to the west and the Rajmahal hills to the east'. Gazetteer: resolve(anga K0) intersect resolve(videha K0) = 15 cells, all from the Bhagalpur disc (the Cliopatria Anga part overlaps 0). The same 15-cell overlap exists between janapada-of-anga (sa-01-a) and janapada-of-vajji (sa-01-c), whose shapes these two copy. Fix: Not blocking. Subtract the Videha polygon (or the land north of the Ganga) from the Bhagalpur disc here and in janapada-of-anga together, so the -601/-600 hand-over stays continuous.
- Thin at `/ledger/1`: Confidence 1 dissolve at the -601 convention year (the page dates nothing before the 6th century). Page to try: https://en.wikipedia.org/wiki/Anga
- Thin at `/ledger`: 'During the Iron Age, Anga expanded to include Vanga within its borders' and 'its territories did extend to the sea in the south, or included Magadha in the west': undated expansions, not drawn (flagged by the author). Page to try: https://en.wikipedia.org/wiki/Vanga_Kingdom
- Spot checks (2): /ledger/0 confirmed on Anga; /ledger/1 confirmed on Anga
- Area: Infobox has no area; no Cliopatria row. Reviewer resolved every keyframe with history/tools/gazetteer.py: figures match the ones quoted in the keyframe notes. Resolved: {'K0': 14921}.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| hindush -518 found (sindhu-sauvira) | sindhu-sauvira -518 dissolve | matched | Same land (Sindh + Multan 150 km), same year. |
| hindush -518 gain (janapada-of-gandhara) | janapada-of-gandhara -518 dissolve | mismatch | Year and land agree (Taxila); the janapada's dissolve names achaemenid-empire, not hindush. Route to sa-01-a: counterpart should be hindush. Also hindush /identity/predecessors/1 uses Taxila 60 km against 100 km in the ledger (cosmetic). |
| hindush -326 loss (macedonian-empire) | macedonian-empire -326 gain | mismatch | macedonian-empire /ledger/35 (-326, confidence 3) gains from 'Porus and the Indian kingdoms of the Punjab' (free text); it has no gain from hindush for Taxila. Route to eu-02. |
| hindush -325 dissolve (macedonian-empire) | none | missing | macedonian-empire has no gain of the lower Indus (Sindh, Peithon's satrapy) from hindush in -326..-325. Route to eu-02. |
| gandara -535 found (janapada-of-gandhara) | janapada-of-gandhara -535 loss | mismatch | Year and land agree (Gandhara west of the Indus); the janapada names achaemenid-empire. Flagged by the author. Route to sa-01-a. The Achaemenid dossier (me-05, not run) should carry gandara and hindush as vassal_start/vassal_end. |
| gandara -327 dissolve (macedonian-empire) | macedonian-empire -326 gain | mismatch | macedonian-empire /ledger/34 (-326) gains the Assakenoi and Aspasioi land with counterpart 'nobody', not gandara; nothing for the Peshawar valley in -327. Route to eu-02. |
| sindhu-sauvira -518 dissolve (hindush) | hindush -518 found | matched | Same land and year. |
| kingdom-of-porus -326 gain (Glausae) | none | exception | Glausae have no dossier; added to counterparts_needing_dossiers. |
| kingdom-of-porus -326 gain (nobody) | none | exception | Lands to the Hyphasis, counterpart nobody; the Hydaspes page has Macedon annexing them and leaving Porus in charge, so eu-02 may prefer macedonian-empire as the grantor. |
| kingdom-of-porus -326 vassal_start (expected in suzerain) (macedonian-empire) | none | missing | Porus 'reinstated ... as his satrap' (Porus page); per the schema the suzerain carries vassal_start/vassal_end with counterpart kingdom-of-porus. macedonian-empire has neither. Flagged by the author. Route to eu-02. |
| kingdom-of-porus -321 gain (macedonian-empire) | none | missing | Triparadisus: 'Those on the river Indus, with the city Patala ... were assigned to Porus' (Peithon page). macedonian-empire has no -321 loss to kingdom-of-porus. Route to eu-02. |
| kingdom-of-porus -317 dissolve (macedonian-empire) | macedonian-empire -317 loss | mismatch | macedonian-empire /ledger/52 (-317) loses Gandhara and the Punjab to maurya-empire; it records no gain of Porus's land from kingdom-of-porus (Eudemus). Route to eu-02. |
| painted-grey-ware-culture -600 dissolve (mahajanapadas) | mahajanapadas -600 found | exception | Counterpart is an umbrella dossier (not territory); the land goes to the successors janapada-of-kuru/-pancala/-surasena/-vatsa, none of which lists painted-grey-ware-culture as predecessor. |
| ochre-coloured-pottery-culture -1500 dissolve (painted-grey-ware-culture) | painted-grey-ware-culture -1200 found | mismatch | 300-year gap (-1499..-1201) between the infobox dates; flagged by the author (Uesugi's alternative dates would close it). |
| ahar-banas-culture -1600 loss (malwa-culture) | malwa-culture -1600 gain | matched | Same intersect region, both confidence 1. |
| malwa-culture -1400 loss (jorwe-culture) | jorwe-culture -1400 gain | matched | Ahmednagar 60 + Pune 60 discs. |
| malwa-culture -1300 dissolve (jorwe-culture) | jorwe-culture -1300 gain | matched | Region Malwa. |
| videha -601 dissolve (janapada-of-vajji) | janapada-of-vajji -600 found | matched | Same polygon; janapada-of-vajji lists videha as predecessor. |
| kuru-kingdom -601 dissolve (janapada-of-kuru) | janapada-of-kuru -600 found | mismatch | janapada-of-kuru (sa-01-b) has predecessors [] (flagged by the author). Same state: see problems on one dossier per state. |
| panchala-kingdom -601 dissolve (janapada-of-pancala) | janapada-of-pancala -600 found | mismatch | janapada-of-pancala (sa-01-c) has predecessors [] (flagged). |
| kashi-kingdom -601 dissolve (janapada-of-kasi) | janapada-of-kasi -600 found | mismatch | janapada-of-kasi (sa-01-b, -600..-600) has predecessors []; both dossiers narrate the same Kamsa conquest (kashi-kingdom -601, janapada-of-kasi -600 dissolve to janapada-of-kosala). |
| anga-kingdom -601 dissolve (janapada-of-anga) | janapada-of-anga -600 found | mismatch | janapada-of-anga (sa-01-a) has predecessors [] (flagged). Both Anga dossiers overlap the Videha/Vajji polygon by 15 cells. |
| shakya -460 dissolve (janapada-of-kosala) | none | missing | janapada-of-kosala (sa-01-b, -600..-451) has no gain from shakya and no vassal_start/vassal_end for shakya ('Vassal state of Kosala'). Flagged by the author. Route to sa-01-b. |
| koliya -460 dissolve (janapada-of-kosala) | none | missing | No gain from koliya in janapada-of-kosala. Route to sa-01-b. |
| kingdom-of-tambapanni -437 dissolve (anuradhapura) | none | exception | anuradhapura is owned by sa-02, which has not run; its Cliopatria row starts in -291, so -437..-292 is uncovered (flagged by the author). |
| gandhara-grave-culture -800 dissolve (nobody) | none | exception | Successor janapada-of-gandhara starts -600 (200-year gap) and does not list it as predecessor. |

## Problems and routing

- No page failed to load for the reviewer. Every one of the 51 ledger events and the one war with a date claim was checked against its cited page (25 pages opened): none fabricated, none mis-dated beyond the author's own flagged conflicts.
- One state, two dossiers: kuru-kingdom/janapada-of-kuru, panchala-kingdom/janapada-of-pancala, kashi-kingdom/janapada-of-kasi and anga-kingdom/janapada-of-anga are the same state split at -601/-600 because the janapada rows belong to other parts. Each pair is one state (its page is one article), so master-plan rule 2 suggests one dossier: extend the janapada dossiers back to these starts, or at least add the predecessor links (the author lists them). janapada-of-kasi is a one-year dossier (-600..-600) that repeats kashi-kingdom's Kamsa conquest.
- Type culture is used for seven post-3400 BCE cultures (painted-grey-ware, ochre-coloured-pottery, ahar-banas, malwa, jorwe, gandhara-grave, southern-neolithic-ashmound), against the schema text 'culture: an archaeological culture before 3400 BCE'; the author follows sa-01-a's Indus precedent. The orchestrator should rule.
- Culture/state overlap by design: painted-grey-ware-culture overlaps kuru-kingdom by 37,000-49,000 km2 and also panchala-kingdom over -1200..-601; the renderer rule 'the state wins' that the author relies on is not written anywhere the reviewer could find.
- eu-02 (macedonian-empire) lacks the mirrors for hindush, gandara and kingdom-of-porus (gains -327..-325, vassal_start/vassal_end for Porus -326..-317, loss of the Indus lands to Porus -321) and uses free text 'Porus and the Indian kingdoms of the Punjab' as a counterpart. sa-01-a (janapada-of-gandhara) should name gandara (-535) and hindush (-518) as counterparts. sa-01-b (janapada-of-kosala) should carry shakya/koliya gains (-460) and the shakya vassalage. me-05 (achaemenid-empire, not run) should carry vassal relations for the colonies hindush and gandara.
- Same 15-cell (about 3,800 km2) overlap between janapada-of-anga (sa-01-a) and janapada-of-vajji (sa-01-c) as between anga-kingdom and videha; fix them together.
- Reviewer edits (all re-validated with 0 errors and 0 warnings and read back 30 s later): kingdom-of-tambapanni /ledger/0 and /ledger/2 confidence 3 to 2, /ledger/0 quotation, /identity/rulers Tissa added; kingdom-of-porus /ledger/1 note; hindush /wars/0 from -535 to -518; gandara /wars/1 to -325 to -327.

## Gazetteer names

- Puttalam (place, kingdom-of-tambapanni): gazetteer spells it 'Puttalan'; add the alias
- Assandh (Asandivat) (place, kuru-kingdom): first Kuru capital on the page, 29.52N 76.60E
- Mehrgarh (place, indus-valley-civilization): neighbour dossier (sa-01-a): its keyframes -3300, -3000, -2700 and -2500 do not resolve ('unknown place Mehrgarh')
