# Review of batch eu-12-m: kingdom-of-spain

Reviewed 2026-10-25 by the eu-12-m adversarial reviewer. Machine copy: history/notes/phase-b/reviews/eu-12-m.json.

**Verdict: fail.** It goes back to the author for two blocking findings (1 and 2). Both are cross-dossier conflicts that draw land twice. The rest of the dossier holds up. The 25 events spot-checked on 8 pages were confirmed, apart from two mis-dated confidence-1 events. The 1529-1555 swap with the Habsburg Monarchy row is real: shapes.csv lists Czechia in kingdom-of-spain_1529 and Belgium and the Netherlands in habsburg-monarchy_1529. The Italian corrections for 1718-1808 are argued from the pages. The area agrees: 506,030 km2 in the infobox against 506,537 km2 in the 1976-2024 shapes.

Mechanical: validate_dossier.py --resolve gives 0 errors and 6 warnings. The warnings are the slugs spanish-puerto-rico, spanish-sahara and spanish-morocco, which have no dossier. All 63 Cliopatria shapes have a verdict, and the new keyframe for 1705 carries from, to and a correction. The ledger is sorted. The capitals and the certainty spans are contiguous. No fix was applied by the reviewer.

## Blocking

1. **Colonies drawn twice, 1877-1898** (/keyframe_review/49-54, /ledger/45-47, 51-54). Keyframe 1877 keeps Cuba, Puerto Rico, the Philippines, Guam, the Marianas, the Carolines, Palau and Fernando Po in the Spain shape as a "vassal tint". The spanish-empire dossier (am-06) corrects its keyframes 1873, 1877 and 1878 to hold exactly this land to 10 December 1898. It sells the islands to Germany on 12 February 1899 (its ledger/124) and dissolves into kingdom-of-spain. captaincy-general-of-cuba and spanish-east-indies record no vassal relation to kingdom-of-spain. The eu-12 scope asks for "the Spanish and Portuguese metropoles distinct from their overseas empires". On areas, the 1877 shape is 984k km2 and the 1890 shape 1,294k km2, against a metropole of about 496k km2.
   - Fix: correct keyframes 1877, 1880, 1885, 1890, 1895 and 1898 to the metropole plus this dossier's own African land.
   - Delete the vassal events 45-47 and 51-53, and the duplicate 1899 sale (54).
   - Add a 1899-02 gain from spanish-empire of Fernando Po, Annobon and Ifni.
2. **Protectorates outlive the kingdom's land** (/ledger/63, /ledger/64). /ledger/62 hands everything to second-spanish-republic on 14 April 1931, yet Spanish Morocco and Spanish Sahara stay this dossier's vassals to 1956 and 1975. The morocco dossier names francoist-spain for 1956, 1958 and 1969. Fix: vassal_end for both at 1931-04, and leave the 1956 and 1975 ends to the Republic and Franco dossiers.

## Non-blocking fixes

3. /ledger/10: the 1640 split of Portugal is iberian-union's event. After the 1580 merge (/ledger/9), Spain itself never gets its land back. Use counterpart iberian-union for Spain's 1640 re-emergence.
4. /ledger/19: Luxembourg is dated 1691 from the shape (confidence 1). The Siege of Luxembourg (1684) page has the surrender signed on 3 June 1684, during a siege that ran "from 27 April to 7 June 1684", and France's ledger/137 has 1684-06. Re-date the event, and mark keyframe 1683 adjust.
5. /ledger/49: the Sahara interior is dated 1890 at confidence 1, but the Spanish Sahara page gives the 1886 Adrar treaty and "an 1887 decree extended Spanish jurisdiction 150 miles inland". Re-date to 1887. Also give the interior the same relation as the coast, which is a vassal under spanish-sahara while the interior is a direct gain.
6. /ledger/6-7: dutch-republic is named in 1568 and 1572, but that dossier starts in 1582. Name the rebels, and union-of-utrecht from 1579.
7. /ledger/25: the 1706 event is written as a loss to dutch-republic. The page says "an Anglo-Dutch condominium for the remainder of the conflict", and /ledger/28 loses the same land again in 1713. Make it an occupation_start, ending at the 1713/1714 transfer.
8. The Canary Islands are in no shape 1516-1872. Ceuta enters only in 1778 (Spanish from 1640), and Melilla only flickers in from 1912. Add them to the corrections.
9. /ledger/0: the 1516 gain sorts before the found event. Its counterpart, habsburg-monarchy, never held the Low Countries.

## Thin, within the 14-page budget

These are the confidence-1 events 3, 7, 23, 24, 37, 43, 55 and 59, plus events that are missing altogether. For each, the page to try is in the JSON.
- Menorca 1798-1802.
- Olivenza 1801.
- War of Devolution and Franco-Dutch War: the French occupations of Franche-Comte (1668, 1674) and Ghent (1678), and the return of Charleroi and other towns in 1678 (France ledger/118-133).
- The French occupation of Girona and Palamos, 1694-1697.
- The War of the Pyrenees.
- Chafarinas 1848, and the Hispano-Moroccan War 1859-1860 (morocco ledger/10-12).
- Rulers, and the capital before 1561.

## Cross-dossier routing

- **kingdom-of-france:** matched for 1659, 1668, 1678 and 1697. It disagrees on Luxembourg (1684 against 1691). Its occupations and returns of 1642, 1668, 1674, 1678 and 1694 are not mirrored here.
- **eu-09 (union-of-utrecht, dutch-republic):** these name habsburg-netherlands, which has no dossier, as the Spanish side from 1579 to 1713. This dossier holds the Low Countries 1516-1706 as Spain's own land. The orchestrator must pick one owner.
- **republic-of-the-rif and cuban-nationalists:** matched within a year. If fix 1 is made, cuban-nationalists should name spanish-empire instead.
- **morocco:** the 1912 entry is a loss to kingdom-of-spain, while this dossier records a protectorate of spanish-morocco. They disagree on type.
- **Other counterparts:** habsburg-monarchy, kingdom-of-portugal, kingdom-of-great-britain, house-of-savoy, first-french-empire, the other eu-12 parts and the Republic and Franco rows have no dossier yet, so they count as exceptions.
