# Review of batch am-08-b (the republics from 1810, part b), 2026-10-19

Reviewer: adversarial review per history/briefs/reviewer-brief.md with the orchestrator's adjustments (Sonnet-era drafts, page budgets, 4 spot checks per dossier, small reviewer-applied fixes). Machine copy: history/notes/phase-b/reviews/am-08-b.json.

Mechanical: all seven dossiers validate with `--resolve` (0 errors, 0 warnings), before and after the reviewer's edits. Ledgers sorted, events inside the life, found/dissolve at start/end, certainty contiguous over each life, rulers contiguous. Keyframe counts match shapes.csv plus the declared new keyframes.

| slug | verdict | why |
| --- | --- | --- |
| rio-de-la-plata | thin | Chaco out in 1814 and back in 1820 (about 200,000 km2) with no event; small 1822/1828 changes noted as unexplained |
| federal-league | pass | 4 spot checks confirmed; Rio Grande do Sul slice removal argued on the Misiones Orientales page |
| republic-of-entre-rios | pass | all 4 events confirmed on the page; area overshoot acknowledged |
| cundinamarca | thin | 90 percent of the outline (the plains) on no page; Chocó mirror missing against new-granada |
| guayaquil-junta | fix (applied) | war years clipped to the State's life |
| republic-of-chile | pass | 6 spot checks confirmed, area ratio 1.06 acknowledged; three confidence-1 gaps listed as thin |
| empire-of-brazil | fail | owner-side occupation mirrors for Paraguay's Mato Grosso hold missing; north-of-Apa strip in the 1868/1870 corrections four years before its 1872 gain |

## rio-de-la-plata (thin)
Spot checks (UP page): /ledger/3 treaty with Paraguay 12 October 1811, /ledger/4 name adopted 22 November 1811, /ledger/6 Alvear in Montevideo 23 June 1814, /ledger/8 Guayabos 10 January 1815; /ledger/12 Republic of Entre Ríos 29 September 1820 (ER page). All confirmed. Infobox has no area (population only), as KF1 says.

Thin:
- /keyframe_review/3 and /5: the 1812 shape minus the 1814 shape, less Uruguay and Rio Grande do Sul, is about 208,900 km2 (Chaco province 108,500, Santiago del Estero 52,400, northern Santa Fe 31,400, by the gazetteer); about 199,000 km2 of it is back in the 1820 shape. KF3 says only "and the Chaco with it" (unverified: page budget) and KF5 is silent about the return. Either mark 1814 and 1815 adjust to keep the Chaco (a nominal claim over unconquered land), or add a 1814 loss and a 1820 gain with counterpart nobody at confidence 1. Page to try: Gran_Chaco.
- /keyframe_review/6 and /7: +19,000 km2 in 1822 and the southern edge moving from 37.1 S to 41.1 S in 1828 are unexplained (noted by the author).
- /ledger/1 (Charcas 1811, confidence 1) and /ledger/18 (dissolve 1833, confidence 1).
Cross-check: /ledger/3 loses Paraguay to paraguay, but paraguay's 1811 found and gain name spanish-empire, and Paraguay is never inside this dossier's found region or keyframes, so this is the loss of a claim. Low priority.
Banda Oriental: /ledger/6 gains Montevideo (40 km) in 1814 but /ledger/8 loses the whole Banda Oriental in 1815; federal-league's 1814 found already holds the Eastern Bank. A Montevideo region in /ledger/8 (and federal-league /ledger/2) would be exact. Not blocking.

## federal-league (pass)
Spot checks: /ledger/0 Union of the Free Peoples 1814, /ledger/3 Portuguese invasion August 1816, /ledger/4 Montevideo taken 20 January 1817 (FL page), /ledger/5 "In 1820, the Eastern Bank was fully captured by Portuguese Brazil" (UP page). All confirmed. No infobox area. Tried and could not break: the member list (Córdoba with La Rioja, Corrientes, Entre Ríos, Misiones, the Eastern Province, Santa Fe), the end in 1820, the Rio Grande do Sul slice at confidence 2.
Remark: /ledger/4's note says Montevideo was "occupied, not yet annexed" while the type is loss; portuguese-empire (am-06) has no 1817 event at all. Either side may record it as an occupation; routed as a missing mirror.

## republic-of-entre-rios (pass)
Spot checks on the Republic of Entre Ríos page: established 29 September 1820, disestablished 28 September 1821, Corrientes autonomous 12 October 1821, Hereñú at Concepción del Uruguay 23 October 1821, capital Concepción del Uruguay. All four events confirmed. Area: the lead gives about 166,980 km2; the author's union of Entre Ríos and Corrientes is about 214,000 km2 (ratio 1.28), acknowledged in the notes.

## cundinamarca (thin)
Spot checks on the state's page: Lozano 24 March 1811, Ventaquemada 2 December 1812, Popayán January 1814, Pasto May 1814, annexation December 1814 (12 December in the presidents table). All confirmed. The page conflicts on independence (July or August 1813); /ledger/2 is at confidence 2, which is right.
Thin:
- About 90 percent of the outline (Meta and Vichada plains) is on no page, and the 1814 outline is reused for 1811-1813. Acknowledged.
- new-granada /ledger/2 gains the Province of Chocó from cundinamarca in 1813 (Colombian War of Independence page table: "Cundinamarca Province of Chocó (1811-1813)"). This dossier never holds Chocó and has no 1813 loss. Add Chocó to the 1811-1813 extent with a 1813 loss to new-granada (confidence 2), or new-granada changes its counterpart. The state's own page names no province.

## guayaquil-junta (fix, applied by the reviewer)
Spot checks on the State of Quito page: 9 October 1811 and "Just two days later, Quito proclaimed its total independence"; jurisdiction "over the central and northern Sierra, as well as the Esmeraldas coastline"; Guayaquil and Cuenca refused the Junta; Ibarra 1 December 1812; Montes and Aymerich restored the colonial government. /ledger/0, 1, 2, 3 confirmed (/ledger/1 has no date on the page, confidence 2 is right). No infobox.
Applied: /wars/1 (Ecuadorian War of Independence) ran 1809-1822, outside the life 1811-1812; now 1811-1812 with a note on the wider war. Re-validated.
Thin: whether the State claimed the Oriente (the trimmed 232 Amazonian cells).

## republic-of-chile (pass)
Spot checks: /ledger/9 Chiloé "incorporated in 1826" and /ledger/30 Easter Island 9 September 1888 (Chile page); /ledger/10 Fuerte Bulnes 1843 and /ledger/23 treaty of 23 July 1881, Tierra del Fuego west of 68°34' Chilean (Boundary treaty page); /ledger/11 Mulchén fort December 1861 - May 1862 and /ledger/25 Santa María's "Today the whole Araucanía is subjugated" of 1 June [1883] (Occupation of Araucanía page). All confirmed. Area: infobox 756,101.96 km2 against 803,137 km2 (ratio 1.06), acknowledged; the Antarctic claim is outside every shape and said so.
Tried and could not break: the 1815-1816 gap with the 1814 loss and 1817 gain mirrored in spanish-empire; status-only adjusts of the War of the Pacific outlines with occupation events; the 1904, 1925 and 1929 treaty steps.
Thin: /keyframe_review/4 (+46,000 km2 of Atacama coast in 1822, unverified: page budget); /ledger/16 and /29 Moquegua at confidence 1; /ledger/24 Aisén at confidence 1 with counterpart nobody (the same treaty's Magallanes names argentine-confederation) and no event for the 1902 award.
Cross-check: spanish-empire has no 1820 loss for Valdivia (/ledger/8). Routed to am-06.

## empire-of-brazil (fail)
Spot checks: /ledger/5 Salvador 2 July 1823 and /ledger/6 "at the beginning of 1824" (Brazilian War of Independence page); /ledger/14 Republic of Piratini 11 September 1836 and /ledger/19 Ponche Verde 1 March 1845 (Ragamuffin War page); /ledger/24 Treaty of Ayacucho 27 March 1867, 102,400 km2 to Amazonas (Treaty of Ayacucho page); /ledger/26 Humaitá 25 July 1868 and /ledger/27 Loizaga-Cotegipe Treaty 9 January 1872 (Paraguayan War page). All confirmed. Area: infobox 8,337,218 km2 (1889) against 8,356,869 km2, ratio 1.002.
Applied by the reviewer (re-validated):
- /wars/5: 'rio-de-la-plata' removed from the Paraguayan War belligerents (that state ended in 1833; Argentina is argentine-confederation, already listed).
- /ledger/6: confidence 3 to 2; the page gives "the beginning of 1824", no month.
For the author (blocking):
1. /ledger/21, 22, 23, 25: the Paraguayan hold on southern Mato Grosso (1864-12 to 1868) and on São Borja-Uruguaiana (1865-06 to 1865-09) is recorded as contest events, but the paraguay dossier has occupation_start/occupation_end with empire-of-brazil (paraguay /ledger/4, 6, 7, 10), and the schema says the owner records the same occupation with the roles reversed (the am-08-a review expects these mirrors here). Add occupation_start 1864-12 (Mato Grosso do Sul), occupation_start 1865-06 and occupation_end 1865-09 (Rio Grande do Sul), occupation_end 1868 (confidence 1), counterpart paraguay, same regions as paraguay's events. The contests may stay, paired.
2. /keyframe_review/11 and /12 corrections and /ledger/27: the 87,250 km2 strip north of the Apa (intersect of Paraguay 1822 with Brazil; 0 cells of the 1866 shape, all 345 cells of the 1868 shape) is Brazilian in the outline from 1868 but gained only on 9 January 1872, with no earlier event. Either subtract it from both corrections so it changes hands at /ledger/27, or add a 1868 event that takes it (occupation_start counterpart paraguay, ended in 1872-01 beside the gain) and route the mirror to paraguay. Paraguay's 1868/1870 corrections also drop the strip four years early; whichever choice is made, both dossiers should agree.
Thin: /ledger/20 (the 1853 north-west Amazon jump, +207,000 km2, confidence 1; the Empire page also lists a 1859 treaty with Venezuela that KF8 does not mention); /ledger/4 (Maranhão and Pará, no date on the page); /ledger/25 (end of the Paraguayan hold, confidence 1); the extra ~60,000 km2 of the 1868 Amazon addition over the treaty's 102,400 km2, and the 1877 Roraima cells.
Optional: paraguay /ledger/9 and /12 (Allied invasion contest 1866-04 to 1870-03) have no ledger mirror here; /wars/5 carries the zone.

## Cross-dossier routing
- Missing on am-06 dossiers: spanish-empire (Valdivia 1820 loss to republic-of-chile; any event for the State of Quito 1811-1812), portuguese-empire (Montevideo 1817).
- new-granada (am-08-a) /ledger/2 Chocó 1813: mirror missing in cundinamarca (see above).
- Exceptions (am-08 parts not run yet): bolivia, republic-of-peru, argentine-confederation, oriental-republic-of-uruguay, riograndense-republic.
- Counterparts needing dossiers (am-08-x): mapuche, cabanagem-rebels, confederation-of-the-equator, free-province-of-guayaquil.
- Gazetteer names: Mulchén, Tarata, Chiloé, Easter Island, Juan Fernández, Purificación.
