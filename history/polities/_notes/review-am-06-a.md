# Review of batch am-06-a (Portuguese Empire)

Reviewer: adversarial review, Phase B, 2026-10-19. Dossier: history/polities/portuguese-empire.json. Verdict: **thin** (valid and honest; five small fixes applied by the reviewer; the ledger still leaves the largest Brazilian moves at confidence 1 within the spent 14-page budget).

## Mechanical checks

validate_dossier.py --resolve: valid, 0 errors, 2 expected warnings (Cabinda vassal_start lasting to 1910; the intentionally empty correction of portuguese-empire_1619). Both Cliopatria rows (Portuguese Empire, Portuguese Colonies; shared Wikidata Q200464) are in cliopatria_names and all 80 shapes have a verdict; the 10 new keyframes carry from, to and a correction. Ledger sorted; found 1415 = start, dissolve 1910 = end; capitals contiguous (Rio inside the 1805-1820 bboxes); certainty 1415-1910 contiguous; family 'portugal' is a colours.json family.

## Fixes applied by the reviewer

- **/ledger/56, /ledger/57, /ledger/58, /ledger/59 (region), /ledger/64/region/union/1, /wars/5/zones/0**: The Guarani War contest, the 1756-1759 occupation and the 1777 cession used the gazetteer region 'Jesuit Missions', which also covers Argentine Misiones and Paraguayan Itapua and Misiones, while their own text says the seven missions east of the Uruguay River.
  - Evidence: Guarani War (S3): 'The boundary drawn up between the two nations was the Uruguay River, with Portugal possessing the land east of the river'; 'The seven Jesuit missions east of the Uruguay River, known as the Misiones Orientales'. First Treaty of San Ildefonso (S4): 'Portugal ceded ... the Misiones Orientales'. regions.jsonl: Jesuit Missions = Misiones (Argentina) + Itapua + Misiones (Paraguay) + north-west Rio Grande do Sul.
  - Applied: Region set to {"intersect": [{"region": "Jesuit Missions"}, {"admin1": "Rio Grande do Sul", "country": "Brazil"}]} with the existing text (the Misiones Orientales only).

- **/ledger/66/region**: The 1 October 1777 gain of the whole admin-1 Rio Grande do Sul re-added the Misiones Orientales that /ledger/64 cedes to Spain in the same month, so the missions would be painted Portuguese from 1777 to 1801.
  - Evidence: S4: 'Portugal ceded Colonia del Sacramento, the associated island of San Gabriel and the Misiones Orientales, while Spain acknowledged Portuguese control of Southern Brazil'.
  - Applied: Region set to {"minus": [{"admin1": "Rio Grande do Sul", "country": "Brazil"}, {"region": "Jesuit Missions"}]}, text 'Rio Grande do Sul, reoccupied by 1777, without the Misiones Orientales that the same treaty ceded to Spain'.

- **/ledger/74 (was /ledger/75)**: contest_start for the Banda Oriental was dated 20 January 1817 (Montevideo) although the page and the dossier's own war entry start the fighting with the invasion of August 1816.
  - Evidence: Cisplatina (S12): 'in August 1816 they invaded the Banda Oriental, with the intention of destroying the protector and his revolution'; the infobox also gives 'invaded ... 1816'; /wars/8 runs from 1816.
  - Applied: Year 1816, month 8, note rewritten to lead with the invasion; event moved before the 1817 occupation_end to keep the ledger sorted (later indices unchanged).

- **/ledger/45/counterpart**: The 1698 loss of Mombasa and the Zanzibar coast named a free-text counterpart 'Imamate of Oman (Yaruba)' although the Cliopatria row yarubid-dynasty (1626-1743, modern countries Oman, Tanzania, UAE) exists, as the author's own report says.
  - Evidence: polities.csv row yarubid-dynasty; Portuguese Mozambique (S8, quoted in the note): 'the Arab seizure of Portugal's key foothold at Fort Jesus on Mombasa Island ... in 1698'.
  - Applied: Counterpart set to 'yarubid-dynasty' (me-10 must carry the 1698 gain).

- **/notes**: The notes flagged the overlap with Cliopatria's Kingdom of Portugal row only for Ceuta, Madeira, the Azores and the 1502 coast; that row also draws the Gulf and Oman coast in 1507-1705 and Angola and Mozambique in 1824-1910, the very land the new keyframes portuguese-empire_1824, _1885, _1891 and _1895 restore.
  - Evidence: shapes.csv: kingdom-of-portugal_1507 to _1640 (1507-1705) list Oman, UAE, Saudi Arabia, Yemen; kingdom-of-portugal_1824 to _1856 189,000-193,000 km2 'Portugal;Mozambique;Angola'; _1885 1,142,246 km2; _1890 1,426,308 km2; _1895 to _1908 1.94 M km2 (Angola, Mozambique, Portugal).
  - Applied: Appended a paragraph 'KINGDOM OF PORTUGAL ROW' to the notes naming those shapes and leaving the choice of row to eu-12 and the compile step.

After the edits the dossier re-validates with the same two warnings. The re-sort moved the contest_start to /ledger/74; the 1817 occupation_end is now /ledger/75; indices below 74 and above 75 are unchanged.

## Spot checks (6 events, more confirmed incidentally)

- /ledger/9, https://en.wikipedia.org/wiki/Portuguese_Empire: confirmed: 'By July 1511, Albuquerque had captured Malacca' (month 7 is the page's bound). Same fetch confirmed /ledger/0 'In 1415 an attack was made on Ceuta', /ledger/3 'discovered in 1456 and settled in 1462' and /ledger/79 'proclaimed the independence of Brazil on 7 September 1822'.
- /ledger/32, https://en.wikipedia.org/wiki/Dutch%E2%80%93Portuguese_War: confirmed: the paragraph opening 'In 1645, most of Dutch Brazil revolted' continues 'Still in that year, the Dutch abandoned São Luís'. Same page confirmed /ledger/27 ('Malacca finally succumbed in 1641'), /ledger/28 (August 1641 alliance, 'captured Luanda and Benguela'), /ledger/30 ('before the end of 1642, the rest of Portuguese Gold Coast followed'), /ledger/34 ('final expulsion from Recife in 1654'), /ledger/36-37 ('captured Colombo in 1656 and drove the last Portuguese from Ceylon in 1658').
- /ledger/44, https://en.wikipedia.org/wiki/Colonial_Brazil: confirmed: 'In 1679, Manuel Lobo founded Colónia do Sacramento on the margin opposite to Buenos Aires'. Same page confirmed /ledger/19 (1549, Tome de Sousa, Salvador) and /ledger/21-23 (Guanabara 1555, Rio founded 1565, last French expelled 1567); infobox 8,100,200 km2.
- /ledger/54, https://en.wikipedia.org/wiki/Bandeirantes: confirmed (confidence 2 is right): 'With the Treaty of Madrid (13 January 1750) ...'; Portugal's de facto control over most of the Southeast, South and Central West 'was recognized by the Treaties of Madrid in 1750 and San Ildefonso in 1777'. The note's quote is condensed and the page does not name the Amazon or Rondonia.
- /ledger/76 (was /ledger/77) and /ledger/74 (was /ledger/75), https://en.wikipedia.org/wiki/Cisplatina: confirmed for the 1821 gain ('In 1821, the Provincia Oriental ... was annexed as a province', assembly of 18 July 1821); mis-dated contest_start (page: 'in August 1816 they invaded the Banda Oriental'), fixed to 1816-08.
- /ledger/64, /ledger/65, /ledger/66, https://en.wikipedia.org/wiki/First_Treaty_of_San_Ildefonso: confirmed: signed 1 October 1777; 'Portugal ceded Colonia del Sacramento, the associated island of San Gabriel and the Misiones Orientales, while Spain acknowledged Portuguese control of Southern Brazil and returned Santa Catarina island'; 'by 1777, Portugal reoccupied Rio Grande do Sul'. The page also has the February 1777 capture of Santa Catarina and the July 1777 surrender of Colonia, not in the ledger (thin).

## Area

The Portuguese Empire article has no infobox area field; the figure is the article's 'At its greatest extent in 1820, the area under its control was approximately 5.5 million square kilometres'. Compared with portuguese-empire_1820 (8,087,194 km2); acknowledged in /keyframe_review/52 and the author's problems. Colonial Brazil's infobox 8,100,200 km2 against 7,832,514 km2 (1778-1804) is 0.97, as the author says.

## Thin: what a gap-filler should find

- /ledger/67: The 1778 jump of 1.28 M km2 in the Amazon (Amazonas 4,587 of 6,010 cells) rests on a confidence-1 gain; neither San Ildefonso nor El Pardo describes the Amazon frontier. Page to try: https://en.wikipedia.org/wiki/Treaty_of_Madrid_(13_January_1750)
- /keyframe_review/52: The 1820 shape holds 251 of 477 Jesuit Missions cells (the Misiones Orientales) with no ledger event: the Portuguese seizure of the seven missions in 1801 (War of the Oranges, Treaty of Badajoz) is absent; the author flagged it. Page to try: https://en.wikipedia.org/wiki/War_of_the_Oranges
- /ledger/65: S4 says Cevallos 'captured the island of Santa Catarina in February' 1777; the ledger has only its October return as a gain of the whole admin-1, of land never lost. Add occupation_start (spanish-empire, February 1777, the island) and make the October event its occupation_end, with the island as region. Page to try: https://en.wikipedia.org/wiki/First_Treaty_of_San_Ildefonso
- /ledger/66: The 1777 gain of Rio Grande do Sul from spanish-empire has no earlier loss: the Spanish hold of the southern Rio Grande from the 1762-1763 war to 1776 ('by 1777, Portugal reoccupied Rio Grande do Sul', S4) is not in the ledger. Page to try: https://en.wikipedia.org/wiki/Spanish%E2%80%93Portuguese_War_(1776%E2%80%931777)
- /ledger/46, /ledger/47, /ledger/61: Colonia del Sacramento swings of 1706 (Spanish siege of 1705), 1713 (return under the Utrecht settlement) and 1763 (Treaty of Paris) are confidence 1. Page to try: https://en.wikipedia.org/wiki/Colonia_del_Sacramento
- /ledger/42, /ledger/43, /ledger/48 to /ledger/53: Growth of the Brazilian interior 1670-1748 (Minas Gerais, Cuiaba, Goias, Mato Grosso, the Guapore) is eight confidence-1 gains; S14 is silent on the places and years. Page to try: https://en.wikipedia.org/wiki/Brazilian_Gold_Rush
- /ledger/11, /ledger/14: Pasai 1521-1529 at confidence 1 with sultanate-of-aceh as counterpart; check whether the fort was taken from Samudera Pasai rather than Aceh and date its loss. Page to try: https://en.wikipedia.org/wiki/Samudera_Pasai_Sultanate
- /ledger/12: Dili 1526 at confidence 1 (S1 gives Timor only as discovered in 1512). Page to try: https://en.wikipedia.org/wiki/Portuguese_Timor
- /ledger/15: Malacca hinterland loss of 1529 to sultanate-of-johor at confidence 1. Page to try: https://en.wikipedia.org/wiki/Portuguese_Malacca
- /ledger/24: The 1572 growth of the Brazilian coast (and the extents of the 15 captaincies of 1534-1536) at confidence 1. Page to try: https://en.wikipedia.org/wiki/Captaincies_of_Brazil
- /ledger/63: Angola's 1772 coastal strip (Luanda to Benguela) at confidence 1. Page to try: https://en.wikipedia.org/wiki/History_of_Angola
- /ledger/77 (was /ledger/78) and /identity/capitals/1: The court's return to Lisbon is dated 1822 at confidence 1; the capital list ends Rio in 1821 without a page. Page to try: https://en.wikipedia.org/wiki/John_VI_of_Portugal
- /ledger/80: Flores and Solor ceded to the Dutch in 1859 at confidence 1, sourced to Portuguese India, which does not give the treaty. Page to try: https://en.wikipedia.org/wiki/Treaty_of_Lisbon_(1859)
- /ledger (1507-1650): No event for Muscat and the Oman coast, which Cliopatria's Kingdom of Portugal row draws in 1507-1705; if the compile step gives that land to this dossier it needs gain and loss events. Page to try: https://en.wikipedia.org/wiki/Muscat

## Cross-dossier matrix

Only haudenosaunee exists among the Context dossiers and it is not a counterpart, so no mirror could be read. Every territorial event is an exception (counterpart nobody, a counterpart listed for a new dossier, or a counterpart whose group has not run). Points the counterpart groups must meet:

- 1581 loss spanish-empire (exception): /ledger/25: no spanish-empire dossier yet (owned by am-06 (b/c), not run yet); expected mirror is a gain in its ledger; the Iberian Union is modelled as a loss of all overseas land to spanish-empire in 1581 and its return on 1 December 1640 (personal union, S11); am-06-b/c must carry the matching 1581 gain and 1640 loss or a personal-union tint
- 1640 gain spanish-empire (exception): /ledger/26: no spanish-empire dossier yet (owned by am-06 (b/c), not run yet); expected mirror is a loss in its ledger; the Iberian Union is modelled as a loss of all overseas land to spanish-empire in 1581 and its return on 1 December 1640 (personal union, S11); am-06-b/c must carry the matching 1581 gain and 1640 loss or a personal-union tint
- 1817 occupation_end first-french-empire (exception): /ledger/75: French Guiana returned in 1817, after first-french-empire's last year (1814); the dossier's note says the land goes to the Bourbon Kingdom of France. eu-20 must take the 1817 return in bourbon-kingdom-of-france (1815-1847) or in the first-french-empire dossier's notes; the counterpart is kept as first-french-empire so the occupation pair stays matched in the validator.
- 1821 gain federal-league (mismatch): /ledger/76: gain of the Banda Oriental in July 1821 from federal-league, whose Cliopatria row ends in 1819 (Wikipedia: Federal League 1815-1820). No federal-league dossier yet (am-08). The mirror can only be federal-league's dissolve or last loss in 1819-1820; am-08 should end the league with the Banda Oriental passing to portuguese-empire (Tacuarembo, 1820) so that the 1821 gain is within one year, or the author re-dates the gain to 1820 (Cliopatria adds Uruguay in the 1820 shape) and keeps 1821 as the formal annexation in the note.

The full matrix (75 events) is in history/notes/phase-b/reviews/am-06-a.json.

## What I tried and could not break

- The pre-1502 keyframes and the Iberian Union model (loss 1581, gain 1640) are flagged by the author as overlaps to settle in the compile step.
- Keyframe corrections that change mid-span ('Goa from 1510', 'without Ceylon from 1658') follow the worked example's convention, with the ledger dating the change.
- Every confidence-3 quote I opened (Malacca, Maranhao, Colonia 1679, San Ildefonso, Cisplatina, Dutch-Portuguese War dates, Guarani War) is on the page as quoted; dates that differ from the scholarly record (Colonia 1679, Sao Luis 1645, Malacca 'by July 1511') are the pages' own.

## Other problems

- Only one Context dossier exists (haudenosaunee), and it is not a counterpart; every counterpart of this ledger is owned by a group that has not written it yet (am-06-b/c, am-08, eu-09, eu-11, eu-20, ea-07, sa-04, sa-05, se-02, se-03, af-02, me-10), so all mirrors are exceptions and the matrix lists the mirror each one needs.
- Reviewer applied five fixes in place (regions of the Seven Missions events, the 1777 Rio Grande do Sul region, the 1816 contest_start, the yarubid-dynasty slug, a notes paragraph on the Kingdom of Portugal row); the dossier re-validates with the same two expected warnings. Ledger indices from 74 to 78 shifted by the re-sort: 74 is the 1816 contest_start, 75 the 1817 occupation_end.
- Cliopatria's Kingdom of Portugal row (eu-12) draws Angola and Mozambique in 1824-1910 and the Gulf and Oman coast in 1507-1705; this dossier's new keyframes 1824-1895 duplicate the African land. eu-12 and the compile step must choose one row.
- federal-league (am-08) ends in 1819 in Cliopatria but this ledger takes the Banda Oriental from it in July 1821; first-french-empire (eu-20) ends in 1814 but is the counterpart of the 1817 return of French Guiana. Both need handling when those groups run.
- portuguese-colonies (owned by sa-06) is merged into this dossier; sa-06 should not write a second dossier and the colour agent should alias it.
