# Review eu-12-j: kingdom-of-portugal

Reviewed on 2026-10-31 against the reviewer brief, with the orchestrator's adjustments: the Sonnet-draft weighting, a 14-page budget, 6 spot checks, and small fixes allowed.

## Verdict: thin

The dossier validates (0 errors; 6 warnings, all for the gazetteer place Olivenza). 47 keyframes cover all 46 Cliopatria shapes plus one new one (1143). Every spot-checked event is on its page with its year: Lisbon and Santarém 1147, Silves 1189/1191, the Algarve 1249, Alcañices 1297, the 1580 crisis, the Restoration War, the War of the Oranges, the 1810-1811 Lines, and the Kingdom infobox dates. None was fabricated or mis-dated at confidence 3.
The area matches: the infobox gives 90,000 km2 for 1300 and Cliopatria 91,911 km2 (ratio 1.02).
The modelling is sound: one state across all dynasties; the 1580-1640 personal union as a loss and gain against iberian-union; overseas cells left to the empire and colony dossiers; the 1706 and 1810 shapes recorded as occupations.
The verdict is thin because the main 12th- and 13th-century border moves are confidence-1 Cliopatria bridges (1169, 1177, 1188, 1227, 1241), and the 1807-1809 French occupations are missing.

## Fixes applied by the reviewer
- `/ledger/8`: Alcácer do Sal gain dated 1220 at confidence 1 (Cliopatria's step), three years after the almohad-caliphate dossier's 1217 loss. Evidence: Almohad Caliphate page: 'the loss of Alcácer do Sal to the Kingdom of Portugal in 1217 was an exception'; almohad-caliphate /ledger/41 is a 1217 loss to kingdom-of-portugal. Done: Year 1217, confidence 2, source Almohad_Caliphate (added to sources[]); notes of keyframes 7 and 8 say Cliopatria draws it three years late. Revalidated: 0 errors.
- `/identity/rulers/0/from`: Afonso I's span starts in 1139, before the dossier's start (1143). Evidence: Brief check 2: ruler spans must lie inside the life; the dossier starts at Zamora 1143 (Kingdom page text). Done: from 1143; note says reign counted from 1139. Revalidated.

## Fixes for the author (not applied, not blocking)
- `/ledger (new, 1668-02)`: Missing loss of Hermisende to Spain at the Treaty of Lisbon (1668), on a page the author opened. Not blocking: one village, outside modern Portugal, so no keyframe changes. Evidence: Portuguese Restoration War infobox: 'Portugal cedes Ceuta and Hermisende to Spain' (Ceuta belongs to the portuguese-morocco and portuguese-empire dossiers). Fix: Add {year 1668, month 2, type loss, counterpart kingdom-of-spain, region {place Hermisende (Zamora, about 41.97 N 6.89 W), km 10, text 'Hermisende'}, confidence 2, source Portuguese_Restoration_War}. Spain's dossier needs the mirror gain.
- `/keyframe_review/13-31, /keyframe_review/32, /keyframe_review/35`: Olivenza (Portuguese 1297-1801 in the ledger) is dropped by the intersect-with-Portugal corrections for 1415-1708, and kept by the ok-verdict 1709 and 1812 shapes after its 1801 loss. Not blocking: one cell, and the author flags it. Evidence: Keyframe 13 note: 'Olivenza ... drops out of the intersect'; keyframe 35 note: 'Cliopatria still holds Olivenza's cell, lost in 1801 ... left alone'. Fix: Once the gazetteer has Olivenza: union the 1415-1706 corrections with {place Olivenza, km 15}, and make 1812 (and the 1801-1808 part of 1709) adjust, minus Olivenza.

## For the gap-filler
- `/ledger/3`: 1169 Alentejo gain (+32 cells) is a confidence-1 Cliopatria bridge with no town or year on the page. Gerald the Fearless took Évora (1165) and the Alentejo towns in 1165-1169. Page to try: https://en.wikipedia.org/wiki/Gerald_the_Fearless
- `/ledger/4, /ledger/5`: The 1177 and 1188 Alentejo losses are confidence-1 bridges; the almohad-caliphate dossier has no mirror, and has 1188 as a loss to kingdom-of-leon. The Almohad page places the reconquest of southern Portugal in 1190-1191 ('won back territory lost in 1189'), so the dates are probably Cliopatria's. Page to try: https://en.wikipedia.org/wiki/Almohad_Caliphate
- `/ledger/9`: 1227 Portalegre/Elvas gain at confidence 1 (the Almohad mirror is also confidence 1). Page to try: https://en.wikipedia.org/wiki/Elvas
- `/ledger/10`: 1241 Baixo Alentejo and eastern Algarve gain (+60 cells) at confidence 1. The Almohad page gives 'Beja in 1234 (to Portugal)' and 'Silves in 1242 (to Portugal)'; split the bridge into dated gains. Page to try: https://en.wikipedia.org/wiki/Almohad_Caliphate
- `/ledger/27`: The 1708 end of the Madrid-corridor occupation is confidence 1 (Cliopatria's shape end). The Allied army held Madrid only from June to August 1706, and the Portuguese front collapsed at Almansa (April 1707). Page to try: https://en.wikipedia.org/wiki/Battle_of_Almansa
- `/ledger (1807-1809)`: No occupation events for Junot's invasion (Lisbon occupied November 1807 to the Convention of Sintra, August 1808) or Soult's (Porto, March-May 1809). The author's note says no page opened dates them, but the Lines of Torres Vedras page has 'In March 1809, Marshal Soult led a new French expedition' and 'Treaty of Fontainebleau in October 1807'. Page to try: https://en.wikipedia.org/wiki/Invasion_of_Portugal_(1807)
- `/wars/8/zones`: The French invasions war has zones only for 1810-1811; add the 1807-1808 and 1809 zones with the new occupations. Page to try: https://en.wikipedia.org/wiki/Second_Battle_of_Porto

## Spot checks
- `/ledger/1` (https://en.wikipedia.org/wiki/Afonso_I_of_Portugal): confirmed ('in 1147 he seized Santarém and Lisbon from the Moors'; no month)
- `/ledger/2` (https://en.wikipedia.org/wiki/Afonso_I_of_Portugal): confirmed (footnote: 'the city was taken on 15 May 1147'; almoravid-dynasty has 15 March from another page, as the author flags)
- `/ledger/6, /ledger/7` (https://en.wikipedia.org/wiki/Sancho_I_of_Portugal): confirmed ('took Silves in 1189'; 'Silves was again lost to the Moors in 1191')
- `/ledger/11` (https://en.wikipedia.org/wiki/Afonso_III_of_Portugal): confirmed ('with the conquest of the Algarve in 1249'; title from 1249; Treaty of Badajoz 1267, Guadiana border)
- `/ledger/13` (https://en.wikipedia.org/wiki/Treaty_of_Alcañices): confirmed ('gained Olivença', 1297, no month; no Riba-Côa town named)
- `/ledger/18-21` (https://en.wikipedia.org/wiki/1580_Portuguese_succession_crisis): confirmed (June 1580 Santarém; rule to 25 August 1580; Cortes of Tomar 1581; exile government 'until 1583')
- `/ledger/22, /ledger/24, /ledger/25` (https://en.wikipedia.org/wiki/Portuguese_Restoration_War): confirmed (1 December 1640; Montijo 26 May 1644; 13 February 1668). The page also names the Hermisende cession, which the ledger lacks.
- `/ledger/28-30` (https://en.wikipedia.org/wiki/War_of_the_Oranges): confirmed (20 May-9 June 1801; Olivença and Juromenha surrendered; 6 June 1801 'cede Olivenza to Spain')
- `/ledger/32, /ledger/33` (https://en.wikipedia.org/wiki/Lines_of_Torres_Vedras): confirmed (Almeida August 1810; Lines 11 October; back in Spain April 1811)
- `/ledger/12, /ledger/14, /ledger/37` (https://en.wikipedia.org/wiki/Kingdom_of_Portugal): confirmed (infobox: Coimbra until 1255, Lisbon 1255-1910; Avis 15 October 1385; Revolution 5 October 1910; Zamora misprinted 1139 in the infobox, as the author flags)

## Cross-dossier matrix
- kingdom-of-portugal 1143 found (county-of-portugal) / county-of-portugal 1143 dissolve: **matched**. The county ends at Zamora 1143.
- kingdom-of-portugal 1147 gain (almoravid-dynasty) / almoravid-dynasty 1147 loss: **matched**. Lisbon; almoravid has October 1147.
- kingdom-of-portugal 1147 gain (almoravid-dynasty) / almoravid-dynasty 1147 loss: **matched**. Santarém: May here (Afonso I footnote), March in almoravid-dynasty. Same year; the integrator picks the month.
- kingdom-of-portugal 1169 gain (almohad-caliphate) / almohad-caliphate - loss: **missing**. Confidence-1 bridge on both sides' terms; almohad-caliphate (af-02) has no 1165-1169 loss to Portugal.
- kingdom-of-portugal 1177 loss (almohad-caliphate) / almohad-caliphate - gain: **missing**. Confidence 1; the Almohad page dates the reconquest to 1190-1191.
- kingdom-of-portugal 1188 loss (almohad-caliphate) / almohad-caliphate 1188 loss: **mismatch**. Both sides at confidence 1 and pointing opposite ways: Portugal loses the northern Alentejo to the Almohads, and the Almohads lose land to kingdom-of-leon in the same year.
- kingdom-of-portugal 1189 gain (almohad-caliphate) / almohad-caliphate 1189 loss: **matched**. Silves.
- kingdom-of-portugal 1191 loss (almohad-caliphate) / almohad-caliphate 1191 gain: **matched**. Silves, July 1191 in almohad.
- kingdom-of-portugal 1217 gain (almohad-caliphate) / almohad-caliphate 1217 loss: **matched**. Alcácer do Sal. Was 1220 in the draft; the reviewer moved it to 1217 from the Almohad Caliphate page.
- kingdom-of-portugal 1227 gain (almohad-caliphate) / almohad-caliphate 1227 loss: **matched**. Both at confidence 1.
- kingdom-of-portugal 1241 gain (Muslim rulers of the Algarve and Alentejo (not named on the page)) / almohad-caliphate - loss: **exception**. almohad-caliphate removes its Iberian cells after October 1228; the taifa-of-niebla shapes (6.96-6.40 W) do not reach the Algarve. The free-text counterpart is accepted.
- kingdom-of-portugal 1249 gain (Muslim rulers of the Algarve and Alentejo (not named on the page)) / taifa-of-niebla - loss: **exception**. Same reasoning as 1241. crown-of-castile records Castile's Algarve claim and its 1263 return only in notes, with no event.
- kingdom-of-portugal 1297 gain (crown-of-castile) / crown-of-castile - loss: **missing**. Olivenza at Alcañices. crown-of-castile (eu-12) has no 1297 event; route to its author.
- kingdom-of-portugal 1419 gain (nobody) / portuguese-empire 1419 gain: **mismatch**. Madeira is claimed as a gain by both dossiers. Draw it once: the integrator or am-06 decides between metropole and empire.
- kingdom-of-portugal 1427 gain (nobody) / portuguese-empire 1427 gain: **mismatch**. The Azores, double-claimed as above.
- kingdom-of-portugal 1581 loss (iberian-union) / iberian-union - merge: **exception**. No iberian-union dossier yet (eu-12; listed). kingdom-of-spain models the union as a 1580 merge into iberian-union, and Portugal as a 1581 loss: the iberian-union author should reconcile 1580/1581 and loss/merge.
- kingdom-of-portugal 1640 gain (iberian-union) / iberian-union - split: **exception**. No dossier yet; kingdom-of-spain splits from iberian-union in December 1640, consistent with this event.
- kingdom-of-portugal 1668 loss (kingdom-of-spain) / kingdom-of-spain - gain: **missing**. Hermisende is ceded in 1668 (Restoration War infobox); the event is missing on both sides (proposed fix).
- kingdom-of-portugal 1706 occupation_start (kingdom-of-spain) / kingdom-of-spain - occupation_start: **missing**. kingdom-of-spain (eu-12) has no 1706 occupation of the Madrid corridor by Portugal. Its 1706 loss to pro-habsburg-spain covers the Aragon lands.
- kingdom-of-portugal 1708 occupation_end (kingdom-of-spain) / kingdom-of-spain - occupation_end: **missing**. As above. The year is confidence 1 here.
- kingdom-of-portugal 1801 loss (kingdom-of-spain) / kingdom-of-spain 1801 gain: **matched**. Olivenza, June 1801, on both sides.
- kingdom-of-portugal 1810 occupation_start (first-french-empire) / first-french-empire - occupation_start: **exception**. No dossier yet (eu-20); listed.
- kingdom-of-portugal 1811 occupation_end (first-french-empire) / first-french-empire - occupation_end: **exception**. No dossier yet (eu-20).
- kingdom-of-portugal 1910 dissolve (portuguese-republic) / portuguese-republic - found: **exception**. No dossier yet (eu-20); listed.
- yarubid-dynasty 1643 gain (kingdom-of-portugal) / kingdom-of-portugal - loss: **mismatch**. Sohar 1643 and Muscat 1650 are overseas, and this dossier leaves them to portuguese-empire. me-10 should name portuguese-empire. The author flagged it.
- yarubid-dynasty 1698 gain (kingdom-of-portugal) / kingdom-of-portugal - loss: **mismatch**. The Mombasa events (contest 1696-1698, gain 1698, loss 1728) also name kingdom-of-portugal. They should name portuguese-empire or the East African colony dossier. The author did not flag these.
- marinid-sultanate 1415 loss (kingdom-of-portugal) / kingdom-of-portugal - gain: **mismatch**. Ceuta 1415, Ksar es-Seghir 1458 and Tangier 1465 name kingdom-of-portugal; portuguese-morocco has 1415, 1458 and 1471. af-02 should name portuguese-morocco, and Tangier is 1465 there against 1471 here.

## Routing
- crown-of-castile (eu-12): add the 1297 loss of Olivenza to kingdom-of-portugal.
- kingdom-of-spain (eu-12): add the 1706 occupation of the Madrid corridor by kingdom-of-portugal, and the 1668 gain of Hermisende.
- yarubid-dynasty (me-10): its Sohar, Muscat and Mombasa events should name portuguese-empire, or the colony dossier, instead of kingdom-of-portugal.
- marinid-sultanate (af-02): its Ceuta, Ksar es-Seghir and Tangier losses should name portuguese-morocco; Tangier is 1465 there against 1471 in portuguese-morocco.
- portuguese-empire (am-06) and integrator: Madeira (1419) and the Azores (1427) are gains in both dossiers; draw them once.
- almohad-caliphate (af-02): no mirror for the 1169 and 1177 Alentejo moves; its 1188 loss to kingdom-of-leon meets a Portuguese 1188 loss to the Almohads (both confidence 1).

Gazetteer names needed: Olivenza, Boulogne-sur-Mer, Hermisende (all places).
