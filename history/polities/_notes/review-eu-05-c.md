# Review of batch eu-05-c (Byzantium, part c)

Reviewer run, 2026-10-19. Validator (`--resolve`): all five dossiers valid, 0 errors, 0 warnings. Pages re-read by the reviewer: Theodore Komnenos Doukas, Battle of Klokotnitsa, Nikephoros I Komnenos Doukas, Carlo I Tocco, Despotate of Epirus, Butrint, Otto de la Roche, War of the Euboeote Succession, Battle of Halmyros, Duchy of Athens, Emirate of Crete, Siege of Chandax, History of Cyprus, Cyprus (theme), Cyprus, Leo Gabalas, Rhodes. Neighbour dossiers read (ledger grep): byzantine-empire, nicaean-empire, latin-empire, principality-of-achaea, rhodes, eastern-roman-empire. Context dossiers that do not exist yet were treated as owned by groups that have not run: republic-of-venice, thessaly, ottoman-empire, house-of-anjou-sicily, second-bulgarian-empire, kingdom-of-serbia, sultanate-of-rum, despotate-of-arta, crown-of-aragon, republic-of-florence, kingdom-of-thessalonica, catalan-company, principality-of-valona(-and-kanina), empire-of-thessalonica, albanian-principalities, negroponte.

| slug | verdict | why |
| --- | --- | --- |
| despotate-of-epirus | fail | /ledger/28 (confidence 3) misstates its page; two more ledger fixes; one counterpart fixed by the reviewer |
| duchy-of-athens | pass | 6 of 7 events confirmed on their pages; thin only within the budget |
| emirate-of-crete | pass | 5 of 6 events confirmed |
| cyprus-condominium | thin | both events confirmed; the 875-883 Cliopatria gap is unexplained |
| domain-of-rhodes | pass | 4 of 4 events confirmed; confidence 1 on the founding is honest |

## despotate-of-epirus: fail

Spot checks: /ledger/6 (Platamon 1218), /ledger/9 (Thessalonica, December 1224), /ledger/11 (Adrianople 1225, Despotate page), /ledger/16 (Klokotnitsa 9 March 1230), /ledger/29 (Butrinto to Charles 1279), /ledger/54 (Arta 1416) and /ledger/55 (Glarentza 1421) were confirmed. /ledger/28 was not.

1. **/ledger/28 (blocking, left to the author).** The 1278 gain of Butrint names house-of-anjou-sicily as the loser and calls the allies "the anti-Angevin coalition". The Nikephoros I page says "The coalition of Charles of Anjou, Nikephoros, and the latter's half-brother John I Doukas of Thessaly ... gained several cities, including Butrinto in 1278". The Butrint page says "In 1274, Byzantine forces re-entered Butrint" and that the two "allied against Byzantine Emperor Michael, and together drove the Byzantines from the area in 1278". Fix: set the counterpart to byzantine-empire, rewrite the note in the page's words, cite and list https://en.wikipedia.org/wiki/Butrint. byzantine-empire then needs a 1278 loss of Butrint and a 1274 gain from house-of-anjou-sicily.
2. **/ledger/55/counterpart (applied by the reviewer).** The counterpart was principality-of-achaea; it is now "Oliverio Franco". The Carlo I Tocco page says "in 1421 Carlo bought permanent possession of it from Oliverio Franco", "who had seized it from the Achaean prince Centurione II Zaccaria three years earlier", and the Achaea ledger has the 1418 loss to "Oliverio Franco". Re-validated with 0 errors and 0 warnings.
3. **/ledger/23/region.** The February 1258 loss to kingdom-of-sicily includes Dyrrhachium, which /ledger/21 already ceded to Nicaea in 1256, and the note admits it. nicaean-empire ledger 51 loses the same towns to Sicily in 1258, so the land changes hands twice. Fix: drop Durrës and any other town held by Nicaea since 1256, or fold the dowry into /ledger/24's note.
4. **Missing 1259 loss of Prilep.** Epirus regains Prilep in 1257 (/ledger/22), and nicaean-empire ledger 52 retakes it in 1259 after Pelagonia. Epirus has only the 1259-1260 occupation pair, so Prilep returns to Epirus in 1260 and stays there until 1272. Fix: add a 1259 loss to nicaean-empire before /ledger/25.

Not faults:
- No infobox area exists; the author says so (KF1).
- The 1340-1356 and 1359-1367 gaps in the capitals and rulers fall in years when the state held no land. They are explained in the notes.
- The confidence-1 events /ledger/4, 5, 17, 19, 36 and 51 are listed as thin.
- The 1411 merge with house-of-tocco and the 1359/1416 events with despotate-of-arta need those sibling dossiers (eu-05, not yet written) to agree.

## duchy-of-athens: pass

Confirmed:
- 1205 founding (infobox).
- Thebes, taken by Henry on 8 May 1209 and Othon's "by around 1211".
- Karydi, May/June 1258.
- The ducal title "did not become official until 1260".
- Walter of Brienne chosen "in mid-1309".
- Halmyros, 15 March 1311.

Within the 5-page budget, the one-cell Cliopatria changes of 1236, 1241, 1272 and 1279 and the omitted ruler strip are thin by design.

Contest start: the war page has Guy join the coalition "from the summer of 1256". The Duchy starts its Attica-Boeotia contest at the 1258 invasion; Achaea starts it in 1256. Both cite pages, and the orchestrator should pick one. The Argolid and the 1311 end (Catalan continuity) are open questions for the orchestrator that the author raised; they are not faults of this dossier.

## emirate-of-crete: pass

Confirmed:
- 824 or 827/828.
- Theoktistos' occupation of "much of the island" (842-843) and the slaughter of the troops he left behind.
- June or July 960, autumn 960 to spring 961.
- 6 March 961.

Thin (by design): Aegina ("Cretan rule extended as far north as Aegina"), the jizya-paying Cyclades and a possible occupation of Athens c. 896-902 are undated and not drawn. No infobox area exists.

## cyprus-condominium: thin

Both events are confirmed: the 688 agreement of Abd al-Malik and Justinian II, and Niketas Chalkoutzes in 965. Cliopatria leaves the island empty in 875-883, and the dossier keeps that hole. History of Cyprus says only that both sides "recovered control over the island for short periods thereafter". A gap-filler should date Basil I's reoccupation (c. 874) and cover 875-883 with an occupation pair or a new keyframe. Area: the Cyprus infobox gives 9,251 km2 against Cliopatria's 11,437.5 km2 (ratio 1.24), within the factor-of-two limit.

## domain-of-rhodes: pass

Confirmed:
- The 1204 founding, honestly at confidence 1.
- The Genoese seizure of 1248, with the Rhodes page's "1248-1250".
- The Nicaean eviction and province (1250).

Area: 2,169 km2 against 1,400.68 km2 (ratio 1.55), acknowledged. The Nicaean suzerainty is "surmised ... at some point" and undated, so nicaean-empire's dated 1233 vassal_start should be confidence 1.

## Mismatches to route to other dossiers

- **byzantine-empire:**
  - The Cyprus gain should be 965, not 960.
  - Rhodes: add a 1204 loss to domain-of-rhodes and a 1261 gain from nicaean-empire. The 1314 loss to domain-of-rhodes is unsupported.
  - Add a 1278 loss of Butrint.
  - Add a 1336 gain of Epirote Thessaly and Ioannina from despotate-of-epirus; at present it gains all Thessaly from thessaly in 1333.
- **nicaean-empire:**
  - Adrianople is 1227; the Despotate of Epirus page gives 1225.
  - The 1233 Rhodes vassalage should be confidence 1.
- **latin-empire:**
  - No loss of Thebes in 1209-1211.
  - The Ravennika homage of Othon (1209) is disputed on the Otto de la Roche page.
- **principality-of-achaea:**
  - The contest starts in 1256 against 1258 here.
  - The 1371 loss of Corinth and the 1388 vassal_end name duchy-of-athens, which ends in 1311.
