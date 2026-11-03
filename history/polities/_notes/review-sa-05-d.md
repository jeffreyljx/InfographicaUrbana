# Review of batch sa-05-d (2026-10-24)

Reviewer: adversarial reviewer, Phase B. Dossiers: maratha-empire, thanjavur-maratha-kingdom, sikhs, carnatic-sultanate. The machine copy is history/notes/phase-b/reviews/sa-05-d.json.

The validator (`--resolve`) gives 0 errors for all four. Warnings, all on maratha-empire: kolhapur-state and janjira-state have no dossier yet (both are listed under counterparts_needing_dossiers), and the gazetteer cannot resolve Karwar.

## Verdicts

| slug | verdict | why |
| --- | --- | --- |
| maratha-empire | thin | 6+ spot checks confirmed; one note quote corrected. Shape changes of 1748, 1752 (Chhattisgarh/Nagpur), 1780-1794 and 1814 are unexplained (page budget spent); the Delhi chain lacks the 1760 loss to the Afghans. |
| thanjavur-maratha-kingdom | fix (fixed by reviewer) | Occupation retyped and the vassal mirror added; spot checks confirmed. |
| sikhs | pass | Every confidence-3 event confirmed on Banda Singh Bahadur; one confidence-1 bridge (1711) for a gap-filler. |
| carnatic-sultanate | thin | Shapes explained and spot checks confirmed, but no event covers Hyder Ali's 1780-84 occupation, the Maratha hold on Trichinopoly 1741-43 or the Chanda Sahib years; rulers are empty although the page has a Nawab table. |

## maratha-empire

Spot checks (WebFetch):
- /ledger/22 Malwa, 7 January 1738 (Baji Rao I): confirmed.
- /ledger/23 Khargone and Handia (Baji Rao I): confirmed. The sentence has no year; the 1739 comes from the battle paragraph.
- /ledger/28 Orissa 1752 (Maratha invasions of Bengal): confirmed.
- /ledger/42, 43, 45: Deogaon (17 December 1803), Surji-Anjangaon (30 December 1803) and Rajghat (24 December 1805): all confirmed on Second Anglo-Maratha War.
- /ledger/46, 48, 49: Poona (13 June 1817), Gwalior (5 November 1817, 'Shinde surrendered Rajasthan') and Nagpur (9 January 1818): all confirmed on Third Anglo-Maratha War.
- /ledger/29, 32, 39: Delhi August 1757, Delhi August 1760, Gwalior 1783 (Maratha Empire): confirmed. The Gwalior note quoted a sentence that is not on the page. **Applied:** the note now quotes 'In 1783, Mahadaji besieged the fort of Gwalior and conquered it' and names the holder ('Chhatar Singh, the Jat ruler of Gohad').

Area: the infobox gives 2,500,000 km2 for 1760; the 1757 shape is 1,016,560 km2 (ratio 0.41). This is acknowledged in /keyframe_review/17 and in the notes, and resolved as tribute land that is not drawn.

Thin (for a gap-filler):
1. The Bhonsle conquests (Nagpur/Deogarh, Berar, Chhattisgarh) are most of the 1748 and 1752 growth. The ledger has only Orissa, yet /ledger/49 loses Nagpur in 1818, land that no event ever gained.
2. The 1780, 1783, 1792, 1794 and 1814 shape changes are unexplained. The Maratha-Mysore wars entry has a zone but no contest events.
3. Delhi is gained in 1757 and gained again in 1760 with no loss in between (the Afghans held it in 1760 per the page). The 1761 loss is at confidence 1.
4. Bassein/Salsette (/ledger/21, confidence 1) is probably 1737/1739, not 1738 (Battle of Vasai). There is no Portuguese mirror.
5. Gujarat 1738 is at confidence 1, and so are the 1691-1717 bridges.
6. The Nagar Haveli loss of 1783 is missing, though portuguese-empire records the gain at confidence 3.
7. Before 1674, bijapur-sultanate records events with maratha-empire (1656, 1659, 1660, 1673) before this dossier starts. Either start the dossier earlier (the infobox gives Rajgad as capital from 1647) or re-route those events; the orchestrator should decide.
8. Capitals have a gap in 1699 (flagged by the author).

## thanjavur-maratha-kingdom

Applied fixes, verified on the Thanjavur Maratha kingdom page:
- The 1773 loss and 1776 gain to carnatic-sultanate are now occupation_start and occupation_end. The Carnatic records an occupation, and the schema has the owner record the same event with the roles reversed. The page says Thanjavur was 'occupied' and the king 'deposed until ... reinstatement in 1776'.
- Added a vassal_start in 1762 (confidence 3: 'a tripartite treaty that imposed a fixed annual tribute payable by Thanjavur to the Nawab of Arcot') and a vassal_end in 1799 (confidence 2: 'Under the treaty of 1799, Serfoji ceded civil and military administration to the Company'). Both have counterpart carnatic-sultanate and mirror carnatic-sultanate /ledger/7 and /ledger/11.
- The dossier re-validates with 0 errors and 0 warnings. Your notes file (_notes/sa-05-d.md) still describes the old loss and gain; update it if you touch it.

Spot checks: found early 1676, 1773, 1776, and the 1799 treaty: all confirmed. There is no area on the page.

Thin: the Kollidam assignment to Santaji in 1677 (ceded or delegated?), Devikottai 1749 and the 1771 siege (page silent), and the undated 2-3 cell differences between shapes (small).

## sikhs

Spot checks on Banda Singh Bahadur: Samana (November 1709), Sirhind (12-14 May 1710), First Lohgarh loss (December 1710), Second Lohgarh recapture (March 1712), the Jammu hills (1713) and Gurdas Nangal (March to 7 December 1715): all confirmed. Type rebel is right. `wikipedia: "Sikhs"` follows the schema (Cliopatria's field).

Thin: /ledger/4, the 1711 loss of Sirhind (a confidence-1 bridge). Try First Battle of Lohgarh.

Mirror: mughal-empire has none of Banda's events. That is the mughal-empire group's fix, not this dossier's.

## carnatic-sultanate

Spot checks on Carnatic Sultanate: independence 1710 (infobox), Madurai annexed 1736, the 1740 Maratha descent on Arcot, and the Carnatic Treaty of 26 July 1801: all confirmed. There is no area on the page.

Thin:
- Hyder Ali's invasion and occupation, 1780-1784 (Second Anglo-Mysore War).
- The Maratha garrison at Trichinopoly 1741-1743 and Anwaruddin's appointment.
- The Second Carnatic War: Chanda Sahib, Nawab 1749-1752 in the page's table, and Clive's taking of Arcot in 1751. The zones are empty with an explanation.
- Wallajah's undated cessions ('had to surrender much of his territory').
- `rulers` is empty, although the page has a Nawab table with reign years. The notes call the page silent on reign years, which is not so.

## Cross-dossier matrix (summary)

**Matched:**
- Bijapur 1675 (x2) and 1677 (x2).
- Mughal: 1680 contest, 1698 Jinji, 1700 Satara, 1707 contest end, 1738 Malwa, 1710 Carnatic.
- Durrani: 1758/1759 contest and 1761 contest end.
- Carnatic-Maratha: 1740-41.
- Carnatic-Thanjavur: 1762 vassal, 1773-76 occupation and 1799 vassal end (after the reviewer's fixes).
- English Colonial Empire: Chingleput 1763.

**Missing on the neighbour's side:**
- mughal-empire: Maratha 1706, 1719 and Gujarat 1738; every Sikh event.
- durrani-empire: Delhi 1760/1761.
- portuguese-empire: Bassein.
- maratha-empire is itself missing the 1783 Nagar Haveli loss (portuguese-empire records the gain).

**Mismatches:**
- Delhi 1771 (Maratha, from mughal-empire) against 1772 (Mughal, from 'Rohilla Afghans').
- Delhi 1757 (Maratha) against Mughal 1760 (a non-slug successor).
- bijapur-sultanate events with maratha-empire in 1656-1673, before its 1674 start.
- The Mughal 1744 confidence-1 loss to maratha-empire has no Maratha mirror.

**Exceptions** (no dossier yet): british-empire, hyderabad-state, nawabs-of-bengal, nayaks-of-madurai, nayaks-of-thanjavur, kolhapur-state, janjira-state, Chhatrasal (kingdom-of-panna) and Gohad.
