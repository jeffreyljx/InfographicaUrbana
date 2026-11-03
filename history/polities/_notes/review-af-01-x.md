# Review of batch af-01-x (Nubia, Kush, Axum, Ethiopia: additions)

Adversarial review, dated 2026-10-18 by the orchestrator. Inputs: the 25 dossiers, the author's report and notes (history/polities/_notes/af-01-x.md), and the sibling and neighbour dossiers that exist (ethiopian-empire, ethiopia, funj-sultanate, mahdist-state, adal-sultanate, makuria, makuria-kingdom, ifat-sultanate, nobatia, kingdom-of-axum, alodia, zagwe-dynasty, kingdom-of-kush, middle-kingdom-of-egypt, seventeenth-dynasty-of-egypt, new-kingdom-of-egypt, assyrian-egypt, eastern-roman-empire, macedonian-empire, neo-assyrian-empire). The other Context polities of the author's brief have no dossier yet (groups me-09, me-10, af-08 and others not run): their mirrors are counted as exceptions.

Mechanical checks: all 25 validate with 0 errors (`--resolve` warnings only for the unknown region names Damot, Kaffa, Gimirra, Hadiya and the place Wadelai, all flagged by the author). Spot checks: the main source page of every dossier (and the second page where events rest on it) was opened with WebFetch; up to 7 events per dossier, all events where a dossier has fewer than 4, weighted to confidence 3 and to the largest moves. Not opened: Kamose, Thutmose I, Mahdist War, Mahdist State, Medri Bahri and Yeha, whose events were either confirmed on another page or rest on the sibling dossiers' quotes. No fabricated event was found; one confidence-2 event was mis-dated (dervish-state, fixed).

## Verdicts

| dossier | verdict | blocking | applied | open |
| --- | --- | --- | --- | --- |
| kingdom-of-kerma | fix | 0 | 0 | 2 |
| turco-egyptian-sudan | fix | 0 | 0 | 5 |
| equatoria-province | fail | 1 | 0 | 2 |
| ajuran-sultanate | fix | 0 | 0 | 2 |
| geledi-sultanate | fix | 0 | 1 | 2 |
| dervish-state | fix | 0 | 1 | 1 |
| kingdom-of-d-mt | fix | 0 | 1 | 0 |
| blemmyes | fix | 0 | 0 | 1 |
| emirate-of-harar | fix | 0 | 0 | 2 |
| kingdom-of-damot | thin | 0 | 0 | 0 |
| sultanate-of-shewa | fix | 0 | 0 | 1 |
| imamate-of-aussa | pass | 0 | 0 | 0 |
| sultanate-of-aussa | fix | 0 | 0 | 1 |
| kingdom-of-kaffa | fix | 0 | 0 | 2 |
| banu-kanz | fail | 1 | 0 | 3 |
| shaigiya | fix | 0 | 0 | 1 |
| abdallab | fix | 0 | 0 | 1 |
| kingdom-of-taqali | fail | 2 | 0 | 3 |
| kingdom-of-fazughli | fix | 0 | 0 | 1 |
| eritrean-people-s-liberation-front | fix | 0 | 1 | 0 |
| habesh-eyalet | fail | 1 | 0 | 3 |
| hiraab-imamate | fix | 0 | 0 | 2 |
| hadiya-sultanate | fail | 2 | 0 | 2 |
| sultanate-of-mogadishu | fix | 0 | 0 | 1 |
| kingdom-of-jimma | fix | 0 | 0 | 1 |

## kingdom-of-kerma: fix

- **/ledger/1** (fix). The c. 1750 BC gain of Lower Nubia from middle-kingdom-of-egypt is a page-silent placeholder a century earlier than the mirror: middle-kingdom-of-egypt /ledger/14 loses Lower Nubia to "Kerma (Kush, Upper Nubia)" c. 1650 BC.  
  Evidence: Kerma culture page gives no year ("later extended its reach northward into Lower Nubia and the border of Egypt"); middle-kingdom-of-egypt /ledger/14 cites the Second Intermediate Period page (13th Dynasty withdrew from the southern forts, Kush reoccupied them) at -1650, the Middle Kingdom end.  
  Fix: Move the gain to -1650 (KF0 to -1651, KF1 from -1650) citing the Second Intermediate Period page, or say in the note why -1750 is kept; middle-kingdom-of-egypt should rename its counterpart to kingdom-of-kerma.
- **/ledger** (fix). No loss of Lower Nubia c. 1540 BC, although new-kingdom-of-egypt /ledger/3 gains Lower Nubia (Wawat, Buhen) from kingdom-of-kerma under Ahmose I; KF1 keeps Lower Nubia to -1504, so the two dossiers draw it twice for 36 years.  
  Evidence: new-kingdom-of-egypt /ledger/3 (Ahmose I page: "Ahmose restored Egyptian rule over Nubia, which was controlled from a new administrative center established at Buhen"); this dossier's /ledger/3 note already has Kamose campaigning at Buhen.  
  Fix: Add a loss c. -1540 (counterpart new-kingdom-of-egypt, region Lower Nubia, c1-2, Ahmose I page) and end KF1 at -1541 with a -1540 keyframe of the Kerma core only; or argue the overlap away in both dossiers.
- Thin: /ledger/1: year Kerma took the Egyptian forts of Lower Nubia (try https://en.wikipedia.org/wiki/Second_Intermediate_Period_of_Egypt)
- Thin: /ledger/3: how the Kamose war ended (c1) (try https://en.wikipedia.org/wiki/Kamose)
- Spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/4 confirmed; /ledger/1 not on page (year; acknowledged at c1)
- Area: infobox none. No infobox area on the Kerma culture page (only the town, about 25 ha); the keyframe notes say so.

## turco-egyptian-sudan: fix

- **/keyframe_review/0..6/correction** (fix). The colony is drawn with "Lower Nubia" and "Nubia", which the gazetteer resolves to include Egypt's Aswan governorate (Nubia = Northern + River Nile (Sudan) + Aswan (Egypt)); Aswan was Egypt proper, not the Sudan colony, for 1820-1885.  
  Evidence: Gazetteer regions.jsonl: Nubia spec union(Northern, River Nile, Aswan); Lower Nubia = Aswan + the Sudan strip to 22.2 N. The dossier's own successor text puts the colony's northern end at Wadi Halfa.  
  Fix: Replace "Nubia"/"Lower Nubia" with the Sudanese admin-1 Northern and River Nile (plus the Halfa reach) in KF0-KF6 and /ledger/0, so Aswan stays in the metropole.
- **/keyframe_review/1/correction** (fix). KF1 (1821-1839) starts from Cliopatria's Funj Sultanate 1820 shape, which reaches 37.24 E (Taka and the Kassala lowlands), so Kassala is drawn from 1821 although /ledger/8 adds it in 1840.  
  Evidence: shapes.csv funj-sultanate_1820 bbox 27.28-37.24 E, 10.89-18.03 N, 626,983 km2; Turkiyah page: "In 1840, the regions of Kassala and Taka were added to the Egyptian domains"; funj-sultanate /ledger/14: Taka independent after 1791.  
  Fix: Use minus(Funj Sultanate 1820, Kassala admin-1 of Sudan) in KF1 (and leave KF2 as the union with Kassala).
- **/ledger/10** (fix). The 1865 gain of the Red Sea coast names ottoman-empire, while this batch's habesh-eyalet holds that coast as the Ottoman province and loses it in 1866 to khedivate-of-egypt (habesh-eyalet /ledger/5): the batch disagrees with itself on counterpart and year.  
  Evidence: Turkiyah page: "In 1865 the Ottoman Empire ceded the Red Sea coast and its ports to Egypt"; Habesh Eyalet page: "formally incorporated into the Egyptian vice-kingdom as a separate entity" (1866).  
  Fix: Name habesh-eyalet as counterpart here and turco-egyptian-sudan in habesh-eyalet /ledger/5, with one agreed year (and the other page's year in the note).
- **/ledger** (fix). abdallab dissolves into turco-egyptian-sudan in 1821 (abdallab /ledger/3), but no gain names abdallab here: the Butana is only inside "Funj Sultanate 1820" at /ledger/5.  
  Evidence: Abdallab page: "In 1821 Sheikh Nasir submitted to Egyptian rule without resistance".  
  Fix: Add a 1821 gain (counterpart abdallab, admin-1 River Nile and Khartoum of Sudan, Abdallab page) or name abdallab in the /ledger/5 note.
- **/keyframe_review/7** (fix). KF7 (1885-1885) draws Equatoria, Wadi Halfa and the Red Sea coast after the January 1885 dissolve; equatoria-province's keyframe also starts in 1885, so Equatoria is drawn twice in that year.  
  Evidence: /ledger/21 dissolve 1885-01; equatoria-province /keyframe_review/0 from 1885; successors give Wadi Halfa and Suakin to khedivate-of-egypt.  
  Fix: End the colony's keyframes at 1884 (KF6) or give KF7 only the land not handed to equatoria-province and the khedivate, with a note.
- Thin: /ledger/2: year of the Battle of Bara (Kordofan), c1 (try https://en.wikipedia.org/wiki/Kordofan)
- Thin: /ledger/17: dates of the Berber, Dongola and Bahr el Ghazal losses, c1 (try https://en.wikipedia.org/wiki/Mahdist_War)
- Thin: /ledger/18: Equatoria split date, c1 (try https://en.wikipedia.org/wiki/Equatoria)
- Spot checks: /ledger/1 confirmed; /ledger/5 confirmed; /ledger/8 confirmed; /ledger/9 confirmed; /ledger/10 confirmed; /ledger/12 confirmed
- Area: infobox none. No infobox area on Turkiyah; keyframe notes compare with Cliopatria Muhammad Ali (1.64 M km2 1822-1833) and Khedivate (3.0 M km2 1877-1884) shapes.

## equatoria-province: fail

- **/keyframe_review/0/correction** (BLOCKING). The only keyframe uses {"region": "Equatoria"}, which the gazetteer resolves to the whole of South Sudan ({"country": "S. Sudan"}, about 0.64 M km2, Bahr el Ghazal and Upper Nile included), plus a 120 km disc at Wadelai: about 0.66-0.69 M km2 against the Equatoria page's 195,848 km2, a factor of about 3.4, for a province whose governor had withdrawn south to Wadelai.  
  Evidence: Equatoria page infobox: "195,847.67 km2"; the province "contained most of northern parts of present-day Uganda, including Lake Albert and West Nile". Emin Pasha page: "In 1885, Emin and most of his forces withdrew further south, to Wadelai near Lake Albert." gazetteer regions.jsonl: Equatoria = {"country": "S. Sudan"} (alt name Southern Sudan). The KF0 note calls 0.6 M km2 "the South Sudan Equatoria region" and an upper bound, but does not resolve it.  
  Fix: Draw union(admin-1 Central Equatoria, Eastern Equatoria, Western Equatoria of S. Sudan; the Wadelai 120 km disc) in /keyframe_review/0, /identity/predecessors/0/land, /ledger/0-2 and /wars/0/zones, or give a page for the larger extent.
- **/ledger/1** (fix). Confidence 1 and the note "The page does not say the Mahdists took the land" are wrong: the cited page says they did.  
  Evidence: Equatoria page: after Emin reached the coast "the Mahdists were firmly in control of Equatoria".  
  Fix: Raise to confidence 2 and quote that sentence in the note.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed (confidence understated); /ledger/2 confirmed; turco-egyptian-sudan /ledger/11 confirmed
- Area: infobox 195848, ratio 3.4. Infobox area is the modern Equatoria region; the drawn shape is about 0.66 M km2 (all South Sudan plus the Wadelai disc). No Cliopatria row.

## ajuran-sultanate: fix

- **/keyframe_review/2/correction** (fix). KF2 (1500-1694) includes admin-1 Banaadir (Mogadishu), where sultanate-of-mogadishu is drawn as a sovereign 50 km disc to 1590: a double claim with no relation recorded.  
  Evidence: Sultanate of Mogadishu page: the sultanate "came under the Ajuran Sultanate control"; infobox successor Ajuran Sultanate. sultanate-of-mogadishu /ledger/1 dissolves 1590 with counterpart ajuran-sultanate; no mirror here.  
  Fix: Record Mogadishu as an Ajuran vassal (vassal_start/vassal_end, counterpart sultanate-of-mogadishu, c1) and add the 1590 gain (counterpart sultanate-of-mogadishu, Mogadishu 50 km) to mirror its dissolve; or take Banaadir out of KF2 before 1590.
- **/ledger/5** (fix). The 1695 dissolve and identity.successors name only geledi-sultanate, but the Hiraab Imamate was founded at Mogadishu by rebelling against and expelling the Ajuran; no loss names hiraab-imamate and KF2 (to 1694) overlaps hiraab-imamate KF0 (1690-1699) on Banaadir and Shabeellaha Dhexe.  
  Evidence: Ajuran page: the Abgaal imam "then established the Hiraab Imamate taking residence in Mogadishu"; "By the early 1700s there was effectively no trace of Ajuran left in Banaadir". Hiraab page: "founded by Imam Omar who successfully rebelled against and defeated the Ajuran Sultanate".  
  Fix: Add a loss c. 1690 (counterpart hiraab-imamate; Banaadir and Shabeellaha Dhexe) ending KF2 there for that land, and add hiraab-imamate to identity.successors (Banaadir, Galguduud, Mudug).
- Thin: /ledger/0: founding year (13th century placeholder, c1) (try https://en.wikipedia.org/wiki/Ajuran_Sultanate)
- Thin: /ledger/2: date of the Hobyo-Kismayo-Qelafo extent (c1) (try https://en.wikipedia.org/wiki/Ajuran%E2%80%93Portuguese_wars)
- Thin: /ledger/3: dates of the Gaal Madow wars (c1) (try https://en.wikipedia.org/wiki/Ajuran_Sultanate)
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed (extent undated, as noted); /ledger/5 confirmed
- Area: infobox none. No infobox area on the Ajuran page.

## geledi-sultanate: fix

- **/ledger/1/confidence** (fix, applied by reviewer). Confidence 3 for the Gedo region, which the page does not name (it names Bardera).  
  Evidence: Geledi page: "eliminated regional threats with the Conquest of Bardera in 1843".  
  Fix: Lowered to 2 with a reviewer note.
- **/keyframe_review/0/correction and /keyframe_review/1/correction** (fix). Both keyframes include admin-1 Banaadir (Mogadishu city) for 1695-1911, which hiraab-imamate (capital Mogadishu) holds 1690-1889: the two dossiers draw Mogadishu twice.  
  Evidence: Hiraab page: "Trade between the Hiraab of Mogadishu and the Geledi Sultanate"; Geledi page: the chief "behind Brava, Marka and Mogdisho" (the hinterland, not the city).  
  Fix: Drop Banaadir from both Geledi keyframes and /ledger/0, /ledger/2 (keep Shabeellaha Hoose), or record the overlap as a contest in both dossiers.
- **/ledger/1/counterpart** (fix). Counterpart "Bardera" is neither a slug nor listed in counterparts_needing_dossiers.  
  Evidence: The page does not say who held Bardera.  
  Fix: Use the name the page gives (the Bardera jama'a or jihad) and list it in the report, or use "nobody" with a note.
- Thin: /ledger/2: Italian protectorate years before the 1911 incorporation (1889-1910), a vassal relation for italian-africa (try https://en.wikipedia.org/wiki/Italian_Somaliland)
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed
- Area: infobox none. No infobox area on the Geledi page.

## dervish-state: fix

- **/ledger/4 (was /ledger/5), /keyframe_review/1/to, /keyframe_review/2** (fix, applied by reviewer). The gain of the British Somaliland interior was dated 1913 ("the withdrawal year is not on the page"), but the dossier's own campaign page dates the British evacuation of the interior to March-April 1910.  
  Evidence: Somaliland campaign page: "the British government ordered the evacuation of the internal regions of Somaliland" "between March and April 1910"; Dervish state page: the British "retreated to the few remaining coastal regions", leaving "the interior regions in the hands of the Dervishes".  
  Fix: Applied: gain moved to 1910-04 (source Somaliland campaign), KF1 ends 1909, KF2 renamed dervish-state_1910 and starts 1910, the 1913 contest_end now dated 1913-08 at Dul Madoba with a corrected note, and the notes field corrected. Validated, 0 errors.
- **/keyframe_review/2/correction** (fix). The interior is drawn as Somaliland minus a 100 km disc at Berbera only, but the British kept "the few remaining coastal regions" (Zeila and Bulhar as well).  
  Evidence: Dervish state page, as above.  
  Fix: Subtract the other coastal towns too (Zeila, Bulhar) or say in the note that only Berbera is excluded.
- Thin: /ledger/6: how the Italian-protected Nugaal valley ended in 1920 (c1); the Illig protected status as an italian-africa vassal relation (try https://en.wikipedia.org/wiki/Treaty_of_Illig)
- Spot checks: /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 mis-dated (1913 for 1910; fixed); /ledger/7 confirmed
- Area: infobox none. No infobox area on the Dervish state page.

## kingdom-of-d-mt: fix

- **/ledger/1/counterpart** (fix, applied by reviewer). The dissolve named kingdom-of-axum, which the Axum dossier founds only in -50 (from nobody); the page puts a Proto-Aksumite polity in between.  
  Evidence: Dʿmt page: "a Proto-Aksumite polity had emerged in northern Tégray by the 4th century BC"; kingdom-of-axum /ledger/0 found -50, counterpart nobody.  
  Fix: Applied: counterpart set to "Proto-Aksumite polity" (no dossier yet; author suggested slug proto-aksumite-kingdoms), with a reviewer note. Validated, 0 errors, 0 warnings.
- Thin: /ledger/0: founding date (8th century BC placeholder, c1) (try https://en.wikipedia.org/wiki/Yeha)
- Thin: /ledger/1: end date (4th century BC placeholder, c1) (try https://en.wikipedia.org/wiki/D%CA%BFmt)
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed
- Area: infobox none. No infobox area; the note says the drawn Tigray and Eritrean highlands are wider than the page's "northern Tigray".

## blemmyes: fix

- **/keyframe_review/0/correction** (fix). The shape is the whole of "Lower Nubia" (which includes all of Aswan governorate) plus Egypt's Red Sea governorate: it takes in Philae and Aswan, the Roman frontier, and the whole Nobatian core that nobatia holds from 347 with no loss c. 380.  
  Evidence: Blemmyes page: in 298 "Rome moved its border north to Philae"; "Kalabsha would serve as the capital of the Blemmyes"; Silko page: Nobatia "defeated the Blemmyes to the North". nobatia /ledger/1 gains Philae-Kalabsha (Aswan 115 km) from blemmyes in 450; nobatia has no event c. 380.  
  Fix: Limit the Blemmyan Nile reach to the northern Dodekaschoinos (Kalabsha/Talmis, south of Philae) plus the Eastern Desert, and set /ledger/0 counterpart to nobatia (with a mirror loss in nobatia) or say why the land was nobody's.
- Thin: /ledger/0: year of the Blemmyan occupation of Lower Nubia (late 4th century, c1) (try https://en.wikipedia.org/wiki/Nobatia)
- Thin: /ledger/1: date of Silko's war (c1) (try https://en.wikipedia.org/wiki/Kalabsha)
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed (undated, c1); /ledger/2 confirmed (bridge)
- Area: infobox none. No infobox on the Blemmyes page.

## emirate-of-harar: fix

- **/ledger/1/region** (fix). The 1700 loss to the Oromo takes the whole emirate (its region equals /keyframe_review/0: Harar region plus the 150 km disc), yet KF0 runs unchanged to 1874 and the state goes on: ledger and keyframe disagree over the entire territory.  
  Evidence: Emirate of Harar page: "They completely overran the region between Harar and Shewa"; "Oromo and Somali clans paid tax to the Emirate into the 18th century, even as they gradually annexed Harari land".  
  Fix: Make the loss the outer belt (e.g. minus(Harar 150 km, Harar 40 km)) and split KF0 at 1700, the reduced core running to 1874.
- **/ledger/3/counterpart** (fix). The 1884 regain names british-colonial-empire while the 1875 loss went to khedivate-of-egypt; neither me-10 nor the British dossier has a 1882 transfer of Harar yet.  
  Evidence: Page: the British "occupied [the Khedivate's] territories in 1882 including Harar"; "the British withdrew from Harar in 1884".  
  Fix: Keep, but list in the report that khedivate-of-egypt (loss 1882 to british-colonial-empire) and british-colonial-empire (gain 1882, loss 1884) must mirror; or name khedivate-of-egypt for 1884 with the British role in the note.
- Thin: /ledger/1: dated stages of the Oromo annexation of Harari land (c1) (try https://en.wikipedia.org/wiki/Harar)
- Spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed
- Area: infobox none. No infobox area; extent "between the rivers Awash and Shebelle" (League of Nations) quoted in the KF0 note.

## kingdom-of-damot: thin

- No fixes.
- Thin: /ledger/0: founding (page: "Possibly formed in the 10th century"; 950 placeholder, c1) (try https://en.wikipedia.org/wiki/Kingdom_of_Damot)
- Thin: /ledger/1: year Damot made Shewa tributary (13th century, c1); sultanate-of-shewa lacks the mirror (try https://en.wikipedia.org/wiki/Sultanate_of_Showa)
- Thin: /ledger/4: the infobox has Damot "ultimately overrun during the Oromo expansion": if Damot survived 1316/7 as an Ethiopian tributary, a vassal relation to the 16th century is missing (try https://en.wikipedia.org/wiki/Amda_Seyon_I)
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed (13th century, no year); /ledger/3 confirmed
- Area: infobox none. No infobox area on the Damot page.

## sultanate-of-shewa: fix

- **/ledger** (fix). No vassal_start/vassal_end mirrors kingdom-of-damot /ledger/1-2 (Shewa tributary to Damot 1250-1285).  
  Evidence: Sultanate of Showa page: "Damot was a powerful state by the 13th century that forced the Sultanate of Shewa to pay tributes".  
  Fix: Add vassal_start 1250 and vassal_end 1285 (counterpart kingdom-of-damot, c1, region as in Damot's events).
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed
- Area: infobox none. No infobox area. The page places Walale "in northern Hararghe in Harla country", which supports the Harar (region) drawing at confidence 2.

## imamate-of-aussa: pass

- No fixes.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed
- Area: infobox 76868. The infobox area belongs to the later Sultanate; the Imamate adds the Harar region to 1646. Tried: predecessor and successor years (adal-sultanate dissolves 1577, emirate-of-harar found 1647 and sultanate-of-aussa 1734 agree), capital coordinate (Asaita 41.43 E 11.57 N) inside the shape, all three dates on the page.

## sultanate-of-aussa: fix

- **/ledger** (fix). Two changes of status that the cited page states are missing: the 1889 Italian protectorate and the Ethiopian tributary status after the Battle of Arraddo (January 1896) to 1936; the Afar land is drawn sovereign throughout, and ethiopian-empire has no Aussa event either.  
  Evidence: Sultanate of Aussa page: "On 6 December 1889, Aussa signed a treaty with the Italians, agreeing to become a protectorate of Italy"; Welde Giyorgis Aboye "defeated Sultan Muhammad Hanfare at the battle of Arraddó in January 1896"; "After this, Aussa became a tributary of the Ethiopian Empire".  
  Fix: Add vassal_start 1896-01 and vassal_end 1936-04 (counterpart ethiopian-empire, c3 years, region Afar), and the 1889 protectorate (counterpart italian-africa) with its end, or explain in notes why the paper protectorate is not drawn; ethiopian-empire (af-01-b) must add the mirror.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed
- Area: infobox 76868, ratio 1.32. Drawn as the Afar admin-1 of Ethiopia, 101,413 km2 on the grid (author's figure); within a factor of two and acknowledged in the KF0 note.

## kingdom-of-kaffa: fix

- **/ledger/3/region** (fix). The 1775 gain repeats the Gimirra region already gained at /ledger/1 (1675), while its note quotes an extension "as far as the Omo to the southeast"; no keyframe changes at 1775.  
  Evidence: Kingdom of Kaffa page: Shagi Sherocho (1775-1795) "extended the boundaries of his kingdom as far as the Omo to the southeast".  
  Fix: Give the 1775 gain the land between Kaffa and the Omo (a coordinate disc on the Omo bend, or the admin unit the gazetteer has), and start a keyframe at 1775 with it.
- **/ledger/2/region** (fix). The 1700 loss takes a 100 km disc round Jimma, north of the Gojeb, which /keyframe_review/0 never drew (Kaffa is drawn bounded by the Gojeb from 1390).  
  Evidence: Page: "all territories north of the Gojeb River were lost to the Oromos"; KF0 note: "It was bounded to the north by the Gojeb River".  
  Fix: Either draw the pre-1700 kingdom across the Gojeb in a 1390-1699 keyframe, or turn the loss into a note.
- Thin: /ledger/1: year of each Gimira annexation (c1) (try https://en.wikipedia.org/wiki/Kaffa_Province)
- Thin: /ledger/2: date of the Mecha Oromo invasion (c1) (try https://en.wikipedia.org/wiki/Oromo_migrations)
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed (18th century, region outside shape); /ledger/4 confirmed
- Area: infobox none. No infobox area on the Kaffa page; the Ras Gobana tribute (ethiopian-empire 1881) is not on this page.

## banu-kanz: fail

- **/keyframe_review/1/correction and /identity/capitals/0** (BLOCKING). KF1 (1175-1365) keeps Aswan's countryside and the Eastern Desert, and the capital stays at Aswan to 1365, but the page says the Banu Kanz lost Aswan in 1174 and moved south; no event removes Aswan.  
  Evidence: Banu Kanz page: "The Ayyubid army proceeded to confront the Banu Kanz, who were defeated after major clashes in Aswan"; "The expulsion of the Banu Kanz from the frontier zone around Aswan caused the area's neglect"; "With the loss of their capital, the Banu Kanz migrated south to occupy Maris".  
  Fix: Add a 1174 loss (counterpart ayyubid-sultanate, Aswan governorate, c3) and redraw KF1 as Maris (Lower Nubia south of Aswan) with the Eastern Desert reach the page gives for the 14th century ("the region between the Red Sea ports of Aydhab and Suakin"); end the Aswan capital in 1174 and add the Maris seat.
- **/ledger** (fix). No gain of Dongola before the December 1365 surrender, although the page has it and makuria /ledger/8 loses Dongola to banu-kanz in 1365; the dossier's notes say the sentence was not on the page, but it is.  
  Evidence: Banu Kanz page: "The Mamluks sent an expedition against the Banu Kanz and Banu Ikrima after Dongola was captured by the tribesmen and its king killed"; the Banu Kanz and Banu Ikrima "were in control of the region between the Red Sea ports of Aydhab and Suakin".  
  Fix: Add a 1365 gain (counterpart makuria, Dongola reach, c2) before the December loss, and correct the notes.
- **/ledger/1** (fix). The 1175 gain of Maris names makuria, but makuria has no loss in 1175 (only the occupation_end of the Ayyubid hold on Qasr Ibrim), so the gain has no mirror and no explanation.  
  Evidence: makuria /ledger/5: 1175 occupation_end, counterpart ayyubid-sultanate; Banu Kanz page: the move into Maris is undated.  
  Fix: Agree a year and counterpart with makuria (af-01-a) or explain in the note why Makuria does not record the loss.
- Thin: /ledger/1: year of the move into Maris (c1) (try https://en.wikipedia.org/wiki/Makuria)
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed (undated); /ledger/2 confirmed; /keyframe_review/1 not on page (page has Aswan lost in 1174)
- Area: infobox none. No infobox area (infobox has only "Historic seat: Aswan", founded 943, dissolution 1365).

## shaigiya: fix

- **/keyframe_review/0/correction** (fix). The shape is a 170 km disc on Dongola (30.48 E 19.17 N), but the page puts Dar Shaigiya from Korti to the Fourth Cataract with its capital at Merowe; the disc covers the Dongola reach that funj-sultanate keeps to 1782 and misses the Fourth Cataract.  
  Evidence: Shaiqiya page: Dar Shaigiya "stretches along the banks of the Nile River from Korti to the now flooded 4th Nile cataract"; "Their tribal capital is Merowe"; the page reports no capture of Dongola. funj-sultanate /ledger/11: Dongola "finally fell to the Shaykiyya in around 1782".  
  Fix: Re-centre on Merowe (31.82 E 18.48 N, about 120 km) for 1690-1781, and add a 1782 gain of Dongola (counterpart funj-sultanate, citing the Funj page) with a 1782 keyframe, or drop Dongola.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed
- Area: infobox none. No area on the Shaiqiya page.

## abdallab: fix

- **/ledger** (fix). No vassal_start 1504 / vassal_end 1821 (counterpart funj-sultanate) mirrors funj-sultanate /ledger/2 and /ledger/16, so the Butana is drawn sovereign for 317 years; the author's notes say the Funj vassal years "agree with this dossier", but this ledger has no vassal event.  
  Evidence: Abdallab page: "they were defeated by the Funj Sultanate in 1504 and thereafter ruled over the Butana as vassals".  
  Fix: Add vassal_start 1504 and vassal_end 1821 (counterpart funj-sultanate, c2, region as KF0).
- Thin: /ledger/0: year of the revolt against Alodia (late 15th century, c1); alodia has no matching loss (try https://en.wikipedia.org/wiki/Alodia)
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed
- Area: infobox none. No area on the Abdallab page.

## kingdom-of-taqali: fail

- **/keyframe_review/0** (BLOCKING). The single keyframe runs 1750-1969 unchanged although /ledger/1 loses the whole kingdom to the Mahdists in 1884 and /ledger/2 regains it in 1898: the Mahdist interregnum is drawn as Taqali.  
  Evidence: Kingdom of Taqali page: "In July 1884 the ruler of Taqali, Makk Adam, was captured by the Mahdists"; "The state was then conquered by the forces of the self-proclaimed Mahdi".  
  Fix: End KF0 at 1883 and start a new keyframe in 1898.
- **/ledger (1898-1969)** (BLOCKING). After 1898 the kingdom is drawn as a sovereign state for 71 years, but the page makes it a British client inside Anglo-Egyptian Sudan (and before 1884 "officially incorporated into Egyptian Sudan" for a nominal tax); no vassal relation is recorded and the same land is British Africa and then the Republic of Sudan.  
  Evidence: Page: "restored as a British client state"; the Makk "was restored to power but remained closely controlled by the British"; the Taqali "would pay a nominal tax and be officially incorporated into Egyptian Sudan".  
  Fix: Record vassal_start 1898 (counterpart british-africa) to 1956 and republic-of-sudan 1956-1969, or end the sovereign state in 1898 and keep the Makkdom in notes; add the undated Egyptian tribute as a c1 vassal relation of turco-egyptian-sudan.
- **/ledger/2/counterpart** (fix). The 1898 regain names mahdist-state, which has no loss to Taqali; the restoration was by the British.  
  Evidence: Page, as above; mahdist-state ledger has no Taqali event.  
  Fix: Name british-africa (the restorer) or nobody, with the Mahdist end in the note.
- Thin: /ledger/1: date of the Mahdist conquest itself (c1) (try https://en.wikipedia.org/wiki/Mahdist_State)
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed (rulers list 1898; text says 1889); /ledger/3 confirmed
- Area: infobox none. No infobox area on the Taqali page.

## kingdom-of-fazughli: fix

- **/ledger** (fix). The 1615 conquest by Susenyos, which the page reports as ending Fazughli's independence (Spaulding), is only in the notes as "a claim".  
  Evidence: Kingdom of Fazughli page: a 1615 conquest by the Ethiopian emperor Susenyos, "which Spaulding says ended Fazughli's independence".  
  Fix: Add a 1615 event (vassal relation with ethiopian-empire, or contest) at c1-2 citing the page, or say in the notes why it is not drawn.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed
- Area: infobox none. No infobox area; the map caption is a "tentative estimation".

## eritrean-people-s-liberation-front: fix

- **/keyframe_review/3/correction, /keyframe_review/4/correction, /ledger/3/region** (fix, applied by reviewer). Afabet was placed at 38.0 E 16.0 N, about 75 km west-south-west of the town.  
  Evidence: Afabet page: "16°11′N 38°41′E / 16.183°N 38.683°E".  
  Fix: Applied: the three Afabet discs moved to 38.68 E 16.18 N, with a reviewer note on /ledger/3. Validated, 0 errors.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/3 confirmed; /ledger/4 confirmed; /ledger/5 confirmed
- Area: infobox none. Rebel front: no infobox area. The ELF (1961-1981) is inside this dossier, flagged by the author.

## habesh-eyalet: fail

- **/keyframe_review/1/correction** (BLOCKING). KF1 (1866-1872) draws the African Red Sea coast (Red Sea state and Massawa), exactly the land /ledger/5 gives to khedivate-of-egypt in 1866; the KF1 note says the opposite ("the African part passed to the Egyptian vice-kingdom; the Hejaz stayed with the Jeddah walilik"), and turco-egyptian-sudan draws the same coast from 1865.  
  Evidence: Habesh Eyalet page: Habesh was "formally incorporated into the Egyptian vice-kingdom as a separate entity" (1866); "the walilik was brought back the following year" (1872); turco-egyptian-sudan /keyframe_review/4-6 include the Red Sea coast and Massawa from 1865.  
  Fix: Make KF1 the coastal Hejaz (Jeddah) only, or end the dossier in 1866 (dissolve, successors khedivate/turco-egyptian-sudan for the coast and ottoman-empire for the Hejaz).
- **/ledger/1-4** (fix). The 1813 loss and 1827 regain of the whole eyalet, and the 1846 loss and 1849 regain of the coast, leave KF0 (1557-1865) unchanged.  
  Evidence: Page: "he received the administration of Habesh in 1813"; "it reverted to Ottoman rule in 1827"; "Massawa and Sawakin were given to him again in 1846, until his death in 1849".  
  Fix: Split KF0 at 1813, 1827, 1846 and 1849, or record Muhammad Ali's administration as a change of governor in notes (he ruled as an Ottoman governor) and drop the loss/gain pairs.
- **/ledger/5** (fix). The 1866 loss names khedivate-of-egypt while turco-egyptian-sudan /ledger/10 gains the coast in 1865 from ottoman-empire.  
  Evidence: As above.  
  Fix: Agree counterpart (turco-egyptian-sudan) and year with that dossier.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/3 confirmed; /ledger/5 confirmed; /ledger/6 confirmed
- Area: infobox 503000 (1856), ratio 1.09. Drawn Hejaz (Makkah, Madinah, Tabuk admin-1) plus the Red Sea coast, about 547,000 km2 (author's grid figure); the page says only "coastal Hejaz".

## hiraab-imamate: fix

- **/ledger/1/counterpart** (fix). The 1700 gain names ajuran-sultanate, which dissolves in 1695, and neither this founding (1690) nor this gain has a mirror in ajuran-sultanate.  
  Evidence: Hiraab page: the Habar Gidir and Duduble "drove the Ajuuraan out of Galgaduud and Mudug provinces" (undated); "By 1700, the Hiraab and other clans occupied a large territory"; ajuran-sultanate /ledger/5 dissolves 1695 to geledi-sultanate only.  
  Fix: Date the expulsion of the Ajuran from Galguduud and Mudug at or before 1695 (with the mirror loss in ajuran-sultanate), or keep 1700 with counterpart nobody and the Ajuran in the note.
- **/keyframe_review/0 and /keyframe_review/1** (fix). Banaadir (Mogadishu) is drawn in both this dossier and geledi-sultanate for 1695-1889; the KF1 note acknowledges the overlap but does not resolve it.  
  Evidence: Hiraab page: "the Hiraab of Mogadishu and the Geledi Sultanate" traded as separate states.  
  Fix: Resolve with geledi-sultanate: Mogadishu (Banaadir) to the Hiraab, the hinterland to the Geledi.
- Thin: /ledger/0: founding year (late 17th century placeholder, c1) (try https://en.wikipedia.org/wiki/Hiraab_Imamate)
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed
- Area: infobox none. No area on the Hiraab page.

## hadiya-sultanate: fail

- **/keyframe_review/0** (BLOCKING). Hadiya is drawn as one sovereign state 1250-1893, but the page has it brought under Amda Seyon's control, an autonomous Abyssinian province from the 14th century, and independent again only in the 1600s; ethiopian-empire /ledger/3 gains Hadiya in 1316 and no event here answers it, so the land is drawn twice for about 300 years. The notes say the Ethiopian dossier records a vassal relation, but it records an annexation.  
  Evidence: Hadiya Sultanate page: Amda Seyon "proceeded to Hadiya and brought it under his control"; Hadiya "became an autonomous province of Abyssinia in the fourteenth century"; "Hadiya regained its independence" (1600s); "Hadiya was historically a vassal state of the Adal federation".  
  Fix: Add the 1316 event (loss or vassal_start, counterpart ethiopian-empire, c2) and the 17th-century regain (c1), split KF0 accordingly; agree the form with ethiopian-empire (af-01-b).
- **/ledger/1, /ledger/2, /ledger/3** (BLOCKING). Each event removes the whole "Hadiya" region (1590, 1889, 1893) while KF0 is unchanged and the state continues; the page names only "some parts" (1590), Qabeena (1889) and the Halaba (1893). /ledger/2 and /ledger/3 are confidence 3 for a region the page does not name.  
  Evidence: Page: "In the late sixteenth century, some parts of the Hadiya region was overrun by the Oromo expansion"; "Hassan was however defeated in 1889 at the battle of Jabdu Meda"; the Halaba "continued to resist until 1893".  
  Fix: Give each event the part the page names (Qabeena, Halaba as coordinates if the gazetteer lacks them), add keyframes for the steps, and lower /ledger/2 and /ledger/3 to confidence 2.
- Thin: /ledger/0: founding year (13th century placeholder, c1) (try https://en.wikipedia.org/wiki/Hadiya_people)
- Thin: /ledger/1: date and extent of the Oromo overrun (c1) (try https://en.wikipedia.org/wiki/Oromo_migrations)
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed (only "some parts"); /ledger/2 confirmed (year; region broader than the page); /ledger/3 confirmed (year; region broader than the page)
- Area: infobox none. No infobox; al-Umari's "eight days' journey by nine" (about 160 by 180 km, Pankhurst) quoted in KF0; region Hadiya not in the gazetteer.

## sultanate-of-mogadishu: fix

- **/ledger** (fix). The city is drawn sovereign to 1590 inside ajuran-sultanate's Banaadir (1500-1694) with no relation recorded.  
  Evidence: Sultanate of Mogadishu page: it "came under the Ajuran Sultanate control and experienced another Golden Age"; infobox successor Ajuran Sultanate.  
  Fix: Add vassal_start (counterpart ajuran-sultanate, c1, year as the page allows) and vassal_end 1590, mirrored in ajuran-sultanate.
- Thin: /ledger/0: founding (infobox 10th century, text mid-13th century or 1330; 1250 placeholder, c1) (try https://en.wikipedia.org/wiki/Mogadishu)
- Thin: /ledger/1: end of the Fakhr al-Din dynasty (late 16th century, c1) (try https://en.wikipedia.org/wiki/Mogadishu)
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed
- Area: infobox none. No infobox area.

## kingdom-of-jimma: fix

- **/ledger** (fix). No vassal relation, although the infobox gives "Vassal to Kingdom of Shewa: 1884" and "Vassal to Ethiopian Empire: 1889", and ethiopian-empire /ledger/30 makes the Gibe states tributary from 1881; the kingdom is drawn sovereign to 1932.  
  Evidence: Kingdom of Jimma page infobox, as quoted; Abba Jifar II "submitted to Menelik II, and agreed to pay tribute to the negus".  
  Fix: Add vassal_start 1884 and vassal_end 1932-05 (counterpart ethiopian-empire, c3, Jimma 80 km), with the 1889 step in the note; ethiopian-empire should move its Jimma date to 1884 or say why 1881, and add the 1932 gain.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed
- Area: infobox none. No infobox area on the Jimma page.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| kingdom-of-kerma -1750 gain (middle-kingdom-of-egypt) | middle-kingdom-of-egypt -1650 loss | mismatch | 100 years apart; the mirror names "Kerma (Kush, Upper Nubia)", not the slug. Kerma's year is a c1 placeholder; move it to -1650. |
| new-kingdom-of-egypt -1540 gain (kingdom-of-kerma) | - | missing | Kerma has no loss c. -1540 (Ahmose, Lower Nubia); Kerma KF1 keeps Lower Nubia to -1504. |
| kingdom-of-kerma -1504 loss (new-kingdom-of-egypt) | new-kingdom-of-egypt -1504 gain | matched |  |
| turco-egyptian-sudan 1820 gain (shaigiya) | shaigiya 1820 loss | matched |  |
| turco-egyptian-sudan 1821 gain (funj-sultanate) | funj-sultanate 1821 loss | mismatch | funj-sultanate /ledger/20 (June 1821) names muhammad-ali-dynasty; should name turco-egyptian-sudan (af-01-b). |
| turco-egyptian-sudan 1821 gain (sultanate-of-darfur) | - | exception | Kordofan; sultanate-of-darfur has no dossier yet (counterpart owned by a group that has not run yet). |
| turco-egyptian-sudan 1865 gain (ottoman-empire) | habesh-eyalet 1866 loss | mismatch | Same coast: the batch's habesh-eyalet loses it in 1866 to khedivate-of-egypt; agree counterpart (habesh-eyalet / turco-egyptian-sudan) and year. |
| turco-egyptian-sudan 1874 gain (sultanate-of-darfur) | - | exception | counterpart owned by a group that has not run yet (no sultanate-of-darfur dossier). |
| turco-egyptian-sudan 1882 loss (mahdist-state) | mahdist-state 1882 gain | mismatch | mahdist-state /ledger/1 names khedivate-of-egypt; should name turco-egyptian-sudan (af-01-c). |
| turco-egyptian-sudan 1883 loss (mahdist-state) | mahdist-state 1883 gain | mismatch | mahdist-state /ledger/2 names khedivate-of-egypt. |
| turco-egyptian-sudan 1885 loss (mahdist-state) | mahdist-state 1885 gain | mismatch | Kassala/Sennar, the rest and Khartoum: mahdist-state /ledger/3, /6, /7 name khedivate-of-egypt. |
| turco-egyptian-sudan 1885 split (equatoria-province) | equatoria-province 1885 found | matched |  |
| abdallab 1821 dissolve (turco-egyptian-sudan) | - | missing | turco-egyptian-sudan has no gain naming abdallab (the land is inside the Funj 1820 shape at /ledger/5). |
| equatoria-province 1889 loss (mahdist-state) | mahdist-state 1889 gain | mismatch | mahdist-state /ledger/10 names "Equatoria Province"; should be equatoria-province (af-01-c). |
| ajuran-sultanate 1695 dissolve (geledi-sultanate) | geledi-sultanate 1695 found | matched |  |
| hiraab-imamate 1690 found (ajuran-sultanate) | - | missing | ajuran-sultanate has no loss to hiraab-imamate; its dissolve names only geledi-sultanate. |
| hiraab-imamate 1700 gain (ajuran-sultanate) | - | mismatch | ajuran-sultanate dissolved in 1695; no loss in its ledger. |
| sultanate-of-mogadishu 1590 dissolve (ajuran-sultanate) | - | missing | ajuran-sultanate has no gain from or vassal relation with sultanate-of-mogadishu. |
| geledi-sultanate 1843 gain (Bardera) | - | exception | No dossier; not listed by the author; page does not say who held Bardera. |
| geledi-sultanate 1911 dissolve (italian-africa) | - | exception | counterpart owned by a group that has not run yet (af-08). |
| hiraab-imamate 1889 dissolve (italian-africa) | - | exception | counterpart owned by a group that has not run yet (af-08); italian-africa's first year is 1890 in polities.csv. |
| dervish-state 1905 gain (italian-africa) | - | exception | counterpart owned by a group that has not run yet (af-08). |
| dervish-state 1910 gain (british-africa) | - | exception | counterpart owned by a group that has not run yet (af-08); year corrected from 1913 by the reviewer. |
| dervish-state 1920 loss (italian-africa) | - | exception | counterpart owned by a group that has not run yet (af-08). |
| dervish-state 1920 loss (british-africa) | - | exception | counterpart owned by a group that has not run yet (af-08). |
| kingdom-of-d-mt -400 dissolve (Proto-Aksumite polity) | - | exception | Listed by the author under counterparts_needing_dossiers (proto-aksumite-kingdoms); counterpart corrected from kingdom-of-axum (founded -50). |
| blemmyes 380 found (nobody) | nobatia   | mismatch | nobatia holds Lower Nubia from 347 with no loss c. 380; the Blemmyan shape covers it. |
| blemmyes 450 loss (nobatia) | nobatia 450 gain | matched |  |
| imamate-of-aussa 1577 found (adal-sultanate) | adal-sultanate 1577 dissolve | matched |  |
| imamate-of-aussa 1647 loss (emirate-of-harar) | emirate-of-harar 1647 found | matched |  |
| emirate-of-harar 1875 loss (khedivate-of-egypt) | - | exception | counterpart owned by a group that has not run yet (me-10). |
| emirate-of-harar 1884 gain (british-colonial-empire) | - | exception | counterpart owned by a group that has not run yet; khedivate-of-egypt (me-10) also needs the 1882 transfer. |
| emirate-of-harar 1887 loss (ethiopian-empire) | ethiopian-empire 1887 gain | matched | 6 January (ethiopian-empire) against 9 January 1887 (Battle of Chelenqo page, confirmed): ethiopian-empire should take the 9th. |
| kingdom-of-damot 1250 vassal_start (sultanate-of-shewa) | - | missing | sultanate-of-shewa has no vassal_start/vassal_end with kingdom-of-damot (same batch). |
| kingdom-of-damot 1316 loss (ethiopian-empire) | ethiopian-empire 1316 gain | matched |  |
| sultanate-of-shewa 1285 loss (ifat-sultanate) | ifat-sultanate 1285 gain | matched |  |
| ethiopian-empire 1316 gain (hadiya-sultanate) | - | missing | hadiya-sultanate has no 1316 event (page: brought under Amda Seyon's control, autonomous province). |
| hadiya-sultanate 1889 loss (ethiopian-empire) | ethiopian-empire 1889 gain | mismatch | ethiopian-empire's 1889 gain names nobody (author flagged); should name hadiya-sultanate. |
| hadiya-sultanate 1893 loss (ethiopian-empire) | - | missing | ethiopian-empire has no 1893 Halaba gain. |
| ethiopian-empire 1881 vassal_start (kingdom-of-kaffa) | - | missing | kingdom-of-kaffa has no vassal_start; the Kaffa page does not mention the 1881 tribute. |
| kingdom-of-kaffa 1897 loss (ethiopian-empire) | ethiopian-empire 1900 gain | mismatch | Kaffa page: captured 11 September 1897, "Annexed by Ethiopian Empire: 1897"; ethiopian-empire (af-01-b) should move its c1 1900 gain and vassal_end to 1897. |
| ethiopian-empire 1881 vassal_start (Gibe Oromo states (Jimma, Limmu, Gera, Guma)) | kingdom-of-jimma   | mismatch | Jimma page infobox: vassal to Shewa 1884, to Ethiopia 1889; kingdom-of-jimma has no vassal events; ethiopian-empire uses a group string, not the slug. |
| kingdom-of-jimma 1932 loss (ethiopian-empire) | - | missing | ethiopian-empire has no 1932 gain of Jimma (af-01-b). |
| sultanate-of-aussa 1896 vassal_start (missing) (ethiopian-empire) | - | missing | Page: tributary of Ethiopia after Arraddo (January 1896); neither dossier records it. |
| sultanate-of-aussa 1936 loss (italian-africa) | - | exception | counterpart owned by a group that has not run yet (af-08). |
| funj-sultanate 1504 vassal_start (abdallab) | - | missing | abdallab has no vassal_start/vassal_end; page confirms vassals from 1504. |
| abdallab 1490 found (alodia) | - | missing | alodia has no loss c. 1490 (dissolves 1504 to funj-sultanate); alodia failed review af-01-a. |
| kingdom-of-fazughli 1500 found (alodia) | - | missing | alodia has no loss c. 1500. |
| kingdom-of-fazughli 1685 loss (funj-sultanate) | funj-sultanate 1665 gain | mismatch | Fazughli page (confirmed): 1685, no 1665; funj-sultanate (af-01-b) should move its gain to 1685. |
| funj-sultanate 1665 vassal_start (kingdom-of-taqali) | kingdom-of-taqali 1750 found | mismatch | Taqali infobox 1750 (tradition early 16th century); Sennar "appeased by annual payments": funj should start its Taqali relation no earlier than the Taqali dossier, or Taqali should start earlier. |
| kingdom-of-taqali 1884 loss (mahdist-state) | - | missing | mahdist-state has no Taqali gain (af-01-c). |
| kingdom-of-taqali 1898 gain (mahdist-state) | - | mismatch | mahdist-state has no loss to Taqali; the restorer was British (british-africa, af-08). |
| kingdom-of-taqali 1969 dissolve (republic-of-sudan) | - | exception | counterpart owned by a group that has not run yet (af-08). |
| shaigiya 1690 found (funj-sultanate) | - | missing | funj-sultanate has no 1690 loss of Dar Shaigiya; it has Dongola falling to the Shaigiya c. 1782 (/ledger/11), which shaigiya does not mirror. |
| funj-sultanate 1782 loss (Shaigiya (Shaykiyya)) | shaigiya   | missing | shaigiya has no 1782 gain of Dongola; funj should use the slug shaigiya. |
| shaigiya 1820 loss (turco-egyptian-sudan) | turco-egyptian-sudan 1820 gain | matched |  |
| banu-kanz 1175 gain (makuria) | - | missing | makuria has only an occupation_end (Ayyubid, Qasr Ibrim) in 1175. |
| makuria 1365 loss (banu-kanz) | - | missing | banu-kanz has no 1365 gain of Dongola although its page has it. |
| banu-kanz 1365 loss (mamluk-sultanate) | - | exception | counterpart owned by a group that has not run yet (me-09). |
| banu-kanz 1174 loss (missing) (ayyubid-sultanate) | - | missing | Page: Banu Kanz lost Aswan in 1174; no event in either dossier (ayyubid-sultanate is me-09, not run). |
| habesh-eyalet 1557 found (ottoman-empire) | - | exception | counterpart owned by a group that has not run yet (me-10). |
| habesh-eyalet 1813 loss (muhammad-ali-dynasty) | - | exception | counterpart owned by a group that has not run yet (me-10); 1827 regain, 1846 loss and 1849 regain likewise. |
| habesh-eyalet 1866 loss (khedivate-of-egypt) | turco-egyptian-sudan 1865 gain | mismatch | See the turco-egyptian-sudan 1865 entry. |
| ethiopia 1961 contest_start (Eritrean independence fighters) | eritrean-people-s-liberation-front 1961 found | mismatch | ethiopia (af-01-c) uses a free string; it should name eritrean-people-s-liberation-front and record the 1977 loss, 1978 regain and 1988, 1990 and 1991 losses. |
| eritrean-people-s-liberation-front 1977 gain (ethiopia) | - | missing | ethiopia has only contest events with the fronts (1961-1991) and the 1991 loss to state-of-eritrea. |
| eritrean-people-s-liberation-front 1991 dissolve (state-of-eritrea) | - | exception | counterpart owned by a group that has not run yet (af-08). |

## Gazetteer and other problems

- No page failed. One page outside the dossiers' sources was opened (Afabet) to verify a coordinate.
- The reviewer brief says reviewers do not edit dossiers; the orchestrator allowed small verified fixes, and four dossiers were edited in place and re-validated (dervish-state, geledi-sultanate, kingdom-of-d-mt, eritrean-people-s-liberation-front); each edit carries a "[Reviewer af-01-x, 2026-10-18: ...]" note. Read back after 45 s: unchanged.
- Gazetteer: the region "Equatoria" resolves to all of South Sudan ({"country": "S. Sudan"}, alt name Southern Sudan), three times the Equatoria page's 195,848 km2; it should be the three Equatoria admin-1 (Central, Eastern, Western) or be renamed Southern Sudan. "Nubia" and "Lower Nubia" include Egypt's Aswan governorate, which is wrong for the 19th-century Sudan colony.
- Three statements in the author's notes are contradicted by the pages: Abdallab "Funj vassal years agree with this dossier" (no vassal events in the dossier); Banu Kanz "the Dongola sentence was not on the page" (it is); Dervish "the year the British withdrew is not on the pages" (March-April 1910 on the Somaliland campaign page).
- Many mismatches are on the sibling side (af-01-a/b/c): mahdist-state names khedivate-of-egypt for the colony's losses and "Equatoria Province" for equatoria-province; funj-sultanate dates Fazughli 1665 (page 1685) and names muhammad-ali-dynasty for Sennar 1821; ethiopian-empire dates Kaffa 1900 (page 1897), lacks Jimma 1932, Hadiya 1893 and the Aussa tributary; ethiopia uses "Eritrean independence fighters". See cross_checks.
- This review is dated 2026-10-18 by the orchestrator; the author's notes are dated 2026-10-19.

Gazetteer names needed: Afabet (place, eritrean-people-s-liberation-front), Merowe (place, shaigiya (suggested re-centre)), Maris (region, banu-kanz (suggested KF1)), Qabeena (region, hadiya-sultanate (suggested 1889 loss)), Halaba (region, hadiya-sultanate (suggested 1893 loss)), Dodekaschoinos (region, blemmyes (suggested shape)), Damot (region, kingdom-of-damot), Kaffa (region, kingdom-of-kaffa), Gimirra (region, kingdom-of-kaffa), Hadiya (region, hadiya-sultanate), Wadelai (place, equatoria-province).
