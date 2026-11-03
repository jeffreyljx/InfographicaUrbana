# Review of batch am-08-c (Phase B, reviewer, 2026-10-19)

Dossiers: first-mexican-empire (fix), gran-colombia (fix), united-provinces-of-central-america (fix), republic-of-peru (FAIL), federated-republic-of-mexico (fix; one fix applied by the reviewer).
Machine copy: history/notes/phase-b/reviews/am-08-c.json.

## Mechanical checks
`validate_dossier.py --resolve`: all five valid, 0 errors, 0 warnings. Neighbour dossiers read (ledger grep only): spanish-empire, republic-of-chile, united-states-of-america, republic-of-texas, california-republic, new-granada (plus empire-of-brazil, paraguay, rio-de-la-plata, netherlands-antilles, confederate-states-of-america, republic-of-venezuela, guayaquil-junta: no events with this batch). Not yet written (exception "group has not run"): bolivia, republic-of-ecuador, republic-of-colombia, republic-of-new-granada, venezuela, centralist-mexico, peru-bolivian-confederation, guatemala, honduras, republic-of-nicaragua, republic-of-costa-rica, republic-of-el-salvador, republic-of-the-rio-grande, republic-of-baja-california, second-mexican-empire, mexican-monarchists, second-french-empire, mexico.

Spot checks (12 pages opened): every confidence-3 event checked was on its page with the stated year. One region overstated (Baja California, lowered to 2 by the reviewer). One keyframe correction contradicted by a page (Peru 1821-1824).

## Applied by the reviewer
- federated-republic-of-mexico /ledger/29 (1853-11 loss of Baja California to Walker): confidence 3 -> 2, note extended. Republic of Baja California page: Walker had neither "full control of the peninsula nor the support of the population" (La Paz, then Ensenada). Re-validated: 0 errors. The author may still redraw it as an occupation of La Paz and Ensenada.

## republic-of-peru: FAIL
1. /keyframe_review/0-1 (1821-1824) shrink Peru to 120 km round Lima. Protectorate of Peru page: "the coast and Northern Peru were under republican command"; the royalists held "the rest of the country" (capital Cuzco). This is a wrong correction over several hundred thousand km2. Redraw as the coast and the north (Tumbes, Piura, Lambayeque, La Libertad, Cajamarca, Amazonas, Ancash, Lima, Ica; Maynas if supported), Lima conf 3, north conf 2; /ledger/0 the same; /ledger/1 the remainder. spanish-empire (am-06) must widen its 1821-07 loss.
2. Tumbes, Jaen, Maynas: keyframes 2 (1825 ok) and 3 leave them to Gran Colombia until 1829; pages call them "Peruvian territories" that Gran Colombia claimed, and the armistice "recognized" them as Peruvian; spanish-empire already gives them to Peru in 1824-12. Agree with gran-colombia (preferred: Peruvian throughout, 1829 events become the end of a contest).
3. Tarata: republic-of-chile returns it 1925-09 (conf 3); Peru keeps it occupied to 1929. Add a 1925-09 occupation_end for Tarata. Chile also records a 1929 Tacna loss that Peru (sovereign) does not mirror: tell Chile's owner.
4. Missing Chilean occupations: Moquegua (Chile /ledger/16, 1880-1884) and Arequipa (from 29 October 1883, War of the Pacific page), Puno.
Thin: Callao 1826 (conf 1), Leticia 1928 (conf 1), Loja/Zamora end 1942 (conf 1), 1825 Amazon loss to Bolivia and 1853 Brazil cells (page silent). Area: infobox 1,285,216 km2 vs 1,302,751 (ratio 1.01). Confirmed: 1821-07 found, 1829 armistice, 1864 Chincha, Tarapaca 1879/1883, Lima 1881/1883-10-29, Treaty of Lima 3 June 1929.

## first-mexican-empire: fix
1. /ledger/5: the 1823-07 loss of Central America comes after the dissolve (1823-03), and federated-republic-of-mexico starts 1823-11: March-November 1823 is held by nobody. Preferred: federated-republic-of-mexico starts 1823-03 (Provisional Government; "power passed over to the Provisional Government of Mexico"), the empire's dissolve hands over the whole 1823 shape, the Central America loss moves to federated-republic-of-mexico (and the Central American found counterpart with it).
2. /ledger/4: Chiapas is handed to Mexico here and gained again by federated-republic-of-mexico /ledger/1 from nobody in 1824. Preferred: Chiapas out of this dissolve and out of federated-republic-of-mexico /ledger/0, a 1823-03 loss of Chiapas to nobody here (conf 1).
3. /ledger/0 region lacks California, Nevada, Utah, Arizona that keyframe 0 adds; make them the same.
Thin: /ledger/1 Chiapas 1822 (conf 1). Area: 4,429,000 km2 (1821) vs 3,628,049 (ratio 0.82), acknowledged. Confirmed: 27 September 1821; 5 January 1822; 19 March 1823; 1 July 1823.

## gran-colombia: fix
1. /ledger/4 (1822 gain of Tumbes/Jaen/Maynas from republic-of-peru, conf 1) has no mirror: Peru holds only Lima in 1822 and spanish-empire gives the land to Peru in 1824. Keyframe 2 is "ok" though its own note calls the land "a claim that Peru held". Settle with Peru (see above).
2. /ledger/0 and keyframe 0 (1819-1820) use all of Cliopatria's New Granada 1820 shape; new-granada's merge hands over only its core. Page: in 1821 "many areas of the country remained in royalist hands". Use new-granada's region and add a 1821 gain of the rest from spanish-empire (conf 1).
3. Panama: the page has Espinar reincorporating the isthmus (undated) before Alzuru's separation of 9 July 1831; add that gain (conf 1) and a 1831-07 loss to nobody.
Cross: spanish-empire has no loss of Panama 1821-11 (am-06). Thin: Carabobo date (conf 1), the 1819-1821 bridge. Area: 3,064,800 km2 (undated) vs 2,846,241 (1822; ratio 0.93); the 1824 shape (4.32 M) correctly cut. Confirmed: Panama November 1821; Guayaquil 19 January - 21 July 1829; Armistice of Piura 10 July 1829; Ecuador 13 May 1830; Panama 26 September 1830.

## united-provinces-of-central-america: fix
1. /ledger/8: the dissolve hands El Salvador to guatemala; El Salvador declared independence from the federation only on 30 January 1841 (page). Restrict to Guatemala and add a 1839-04 loss of El Salvador to republic-of-el-salvador (or extend to 1841-01).
2. /keyframe_review/1 is ok though Costa Rica is out 1829-04..1831-02 (/ledger/2-3); mark adjust with the note (page: seceded "without separating itself", "sin separarse").
3. Rulers: 1824 empty between Delgado (1823) and Arce (1825).
Area: 520,000 km2 (undated) vs 443,683 (ratio 0.85), acknowledged. Confirmed: 1 July 1823; 1 April 1829 / February 1831; 30 April, 26 October, 15 November 1838; 17 April 1839.

## federated-republic-of-mexico: fix
1. Applied: /ledger/29 conf 3 -> 2 (see above).
2. /ledger/1: Chiapas gained twice (see first-mexican-empire 2); the region is all Chiapas although its text excludes the Soconusco.
3. /identity/start 1823-11 leaves the Provisional Government (1823-03..11) uncovered (see first-mexican-empire 1).
4. /ledger/13 note says the Texas remnant "is now contested with the United States", but no contest_start exists; the US dossier holds all of Texas from 1845-12 (its /ledger/39) while this dossier loses the remnant only in 1848-05 (/ledger/26). Add 1845-12 contest_start / 1848-05 contest_end with united-states-of-america. /ledger/28 (parts of Colorado, Kansas, Oklahoma, Wyoming) has no US mirror beyond the New Mexico province.
5. Keyframes 3-5 (1836-1845) keep a northern rump separate from centralist-mexico on Cliopatria's word; the Centralist page describes one country with a new constitution. Orchestrator decision (author flagged it).
Thin (budget: 13 shapes, up to 9 pages; author used 11): Yucatan 1846-1848 inside this dossier's shapes; San Juan de Ulua 1825, 1842 north transfer, 1848 evacuations, 1867 Puebla/Chihuahua ends (conf 1); rulers stop at 1835. Area: no infobox area on First Mexican Republic; Centralist infobox 4,350,000 (undated) vs 3,188,401 (ratio 0.73; corrected shape ~4.5 M), acknowledged. Confirmed: Chiapas 1824; Tampico July-September 1829; 22 August 1846; Gadsden 30 June 1854.

## Cross-dossier mismatches to route
- am-06 spanish-empire: add Panama loss 1821-11 (gran-colombia), Tampico occupation 1829 and Veracruz occupation 1861-12..1862-04 (federated-republic-of-mexico); widen the 1821-07 Peru loss; the 1824-12 loss to Peru disagrees with Peru on Tumbes/Jaen/Maynas.
- am-07 united-states-of-america: 1845-12 gain of all Texas vs Mexico's 1848-05 loss of the Texas remnant.
- am-08 republic-of-chile: Tarata 1925 and Tacna 1929 readings vs Peru.
- am-08 new-granada: its 1819 handover (core) vs gran-colombia's found region (all of New Granada).
