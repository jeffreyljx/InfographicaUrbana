# Review af-02-f (2026-10-19)

Reviewer: adversarial review of regency-of-algiers, karamanli-dynasty, ottoman-tripolitania, emirate-of-abdelkader, ali-burghul. Neighbour dossiers read: beylik-of-tunis, morocco, spanish-empire (the other Context polities are not written yet). Validator `--resolve`: all five valid, 0 warnings (re-run after the reviewer's edits).

Spot checks (WebFetch): Oran, Invasion of Algiers in 1830, Regency of Algiers (truncated in the 1710 sentence for the reviewer too), Karamanli dynasty, Fezzan, Tripolitanian civil war, First Barbary War, Ottoman Tripolitania, Italo-Turkish War, Emirate of Abdelkader, Treaty of Tafna, French conquest of Algeria. Every checked event said what its note claims, with the year. No infobox in the batch gives an area; each dossier says so.

## regency-of-algiers: fix (applied by the reviewer)
- Applied: `/ledger/4-6` counterpart kingdom-of-spain -> spanish-empire, and kingdom-of-spain removed from `/wars/1/belligerents`. The spanish-empire dossier keeps Oran to 1792 (keyframes 51-55 add the cells back for 1778-1791) and records the 1792 loss with regency-of-algiers as counterpart. The kingdom-of-spain dossier (eu-12) should leave the Oran cells of its 1778-1795 shapes to spanish-empire.
- Applied: `/keyframe_review/0` verdict ok -> adjust, from 1706 to 1707, with an "unchanged" correction, so the 1706 shape (Cliopatria span 1706-1708) no longer overlaps the new 1708 keyframe (Oran page: "Spanish sovereignty lasted until 1708").
- Thin: the 1756 and 1807 Algerian-Tunisian wars (in beylik-of-tunis wars with regency-of-algiers as belligerent) and the 1756-1807 tributary relation are missing here; Touggourt and Ouargla ("tributaries until 1830", Regency page) lie south of every shape and have no vassal events; `/ledger/0` found 1706 is confidence 1 (Cliopatria's year).
- Minor, not a fault: the 1710 "rename" is a title change (deys take the title of pasha), not a change of the state's name.

## karamanli-dynasty: fix
- `/identity/rulers/3` "Ali Pasha (Ali Burghul) 1793-1795" contradicts ali-burghul (the usurper drawn as his own rebel state); give the Karamanli claimant instead (Ali I, expelled 30 July 1793, in exile at Tunis until January 1795). Non-blocking.
- Thin: `/ledger/1` (1713, c1), `/ledger/3` (1794 Tunisian strip, c1, mirror in beylik-of-tunis also c1), Derna after June 1805.
- Checked and not broken: 1711 coup and ruler dates, Burghul's 1793-1795 occupation, Derna April-May 1805 and the 10 June 1805 treaty (infobox 4 June, noted), "By 1807 ... all the tribes of Cyrenaica and the Fezzan", Fezzan "1811/1812" with no occupier named (c2 honest), 26 May 1835. Keyframes 1807 and 1811 rest on those sentences.

## ottoman-tripolitania: pass
Tried: 1835 direct control, 1865 eyalet to vilayet, the five sanjaks, Cyrenaica 1863/1871/1888 (administrative, in notes), 3-21 October 1911 captures, Treaty of Ouchy 18 October 1912; the Somaliland stray (shapes.csv bbox of the 1840 and 1859 shapes reaches 10.06 N, 45.1 E) is real and cut by the corrections; the 1835 hand-over matches karamanli-dynasty; certainty is contiguous 1835-1912. Could not break it.

## emirate-of-abdelkader: thin
- The keyframes shrink by about 14,500 km2 (1837 -> 1840) and 18,800 km2 (1840 -> 1842) with no loss event in the ledger (only the 1839 contest_start over the whole land); french-algeria will need the matching gains. Add dated losses (Tagdemt, Mascara, Tlemcen 1841-1842; the Smala 1843) from https://en.wikipedia.org/wiki/Emir_Abdelkader or the battle pages.
- `/ledger/7-8` 1846 at confidence 1; Mejdana (Setif) and Ziban (Biskra) undated; Clausel's December 1835 attack on Mascara (conquest page) not in the ledger.
- All dated events checked were confirmed (27 Nov 1832, 26 Feb 1834, January 1836, 30 May 1837 and "approximately two thirds of Algeria", 23 Dec 1847).

## ali-burghul: pass
All dates checked on the Tripolitanian civil war page (29-30 July 1793, 30 September 1794, 19-20 January 1795); the gain/loss pair matches karamanli-dynasty. Djerba needs a gazetteer entry.

## Cross-dossier
Matched: Oran 1708/1732/1792 with spanish-empire (1792 after the fix); Tripoli 1793/1795 between karamanli-dynasty and ali-burghul; the 1794 Tunisian strip with beylik-of-tunis; the 1835 hand-over between karamanli-dynasty and ottoman-tripolitania. Exceptions (counterpart not written yet): ottoman-empire (1713), french-algeria (1830, 1846), italian-africa (1912), the Fezzan Awlad Muhammad (1807, 1811). Counterparts needing dossiers: beylik-of-constantine, awlad-muhammad-dynasty, senussi-order, beylik-of-titteri / Kabylia.
