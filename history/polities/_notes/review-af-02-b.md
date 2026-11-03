# Review of af-02-b (Carthage and the Maghreb, part b), 2026-10-19

Reviewer: adversarial review, Phase B. Machine copy: history/notes/phase-b/reviews/af-02-b.json.
Validator (--resolve): 0 errors in all six; warnings: numidia 2 (masaesyli has no dossier), kharijites 1 (Jebel Nafusa not in gazetteer).
Neighbour dossiers read: mauretania, carthage, roman-republic. The other Context polities have no file yet (groups not run).
No page opened gives an infobox area for any of the six (Numidia, Emirate of Nekor, Fihrids, Kharijites, Rustamid dynasty, Barghawata).

| slug | verdict | why |
| --- | --- | --- |
| kingdom-of-numidia | fix | 2 fixes applied by the reviewer; 3 cross-dossier items for the author (not blocking) |
| emirate-of-nekor | pass | 6 spot checks confirmed; gaps are conf-1 bridges |
| fihrids | fix | Jebel Nafusa drawn by both fihrids and kharijites 752-756 (not blocking) |
| kharijites | thin | 1 fix applied; 64,000 km2 of eastern Algeria in the 757 shape that no event gains |
| rustamid-dynasty | fail | the page's 880s contraction to Tahert is ignored; the 812 cession is misquoted |
| barghawata-conference | fix | last ruler given a 99-year reign (not blocking) |

## kingdom-of-numidia (fix)
Spot checks, all confirmed: /ledger/1 (Masinissa), /ledger/2 'by 158 BC', /ledger/3 152 BC, /ledger/7 112 BC (Jugurtha: 'defeated and killed Adherbal in 112 BC'), /ledger/8 105 BC, /ledger/9 46 BC.
Applied by the reviewer (re-validated, 0 errors):
- /ledger/6/region: the 116 split gave 'Adherbal (eastern Numidia)' the western half (clio -110 minus -91). The Jugurthine War page: Jugurtha got 'the better, more fertile and populous western half of Numidia'. Now {place Constantine, km 150}, the same land /ledger/7 merges back.
- /wars/1/from: -112 changed to -111 (infobox 'Date: 111-105 BC'; the Senate 'declared war on Jugurtha in 111 BC').
For the author (not blocking):
- No vassal pair with roman-republic, although roman-republic /ledger/63 (-201) and /ledger/145 (-46) record Numidia as a client. The Numidia page: 'an ally of Rome' that 'later alternated between being a Roman province and a Roman client state'. Add the pair, or argue it is an ally only and ask eu-03 to drop theirs.
- No vassal pair with mauretania (mauretania /ledger/1 -203, /ledger/3 -148). Masinissa page: Bokkar 'had become a vassal of Masinissa'. Add vassal_start -202 (counterpart mauretania) and vassal_end -148 (conf 1).
- /keyframe_review/0 draws the Algerian coast from -202, but carthage /ledger/53 loses it only in -197 and no event here gains it. Settle this with carthage (see below).
Thin: the western Numidia boundary of 105 (Mulucha or 5.3 E); the Roman Africa frontier after 146; the rump under Masinissa II and Arabio to 40 BC (infobox: 'Annexed by the Roman Empire 25 BC').

## emirate-of-nekor (pass)
Emirate of Nekor page, all confirmed: 710 founding and client status 710-750, 760/761 founding of Nekor, 931 'the Umayyad's vassal, al-Mu'ayyad' and the sack, Ya'la ibn al-Fatuh about 1015 ('maintained their rule until the city was destroyed'), destruction 1080-1081. The end in 1081 against the infobox's 1015 is argued from the page's text and accepted.
Tried and could not break: capitals inside the bbox, keyframe trims of 1-8 percent, Cordoba and Umayyad pairs (both groups not run).
Thin: /ledger/6 (contest_end 932, conf 1, a year after /wars/2 ends in 931) and /ledger/7 (vassal_end 934, conf 1).

## fihrids (fix)
Spot checks confirmed: Feb 745 (Handhala 'consented to return to Damascus in February 745'), 752 reconquest, 757 Kairouan, infobox 'Dissolution: 757'. The cut of eastern Algeria follows the page's own words: 'the western Maghreb - Morocco and eastern Algeria - remained out of his reach'.
For the author (not blocking): /keyframe_review/3 and /keyframe_review/4 keep the Jebel Nafusa, which kharijites /keyframe_review/1 gives to the Ibadite remnants ('driving their remnants south into the Jebel Nafusa'). Subtract it once the gazetteer has the name.
Thin: /ledger/1 (751 loss, conf 1, Cliopatria's year).

## kharijites (thin)
Spot checks confirmed: 752 loss, 757 Tripoli ('In 757, Ibadis seized Tripoli and captured Kairouan the next year'), 757 Kairouan (Warfajuma), 758 Ibadite Kairouan, 761 ('Driven out by an Abbasid army in 761').
Applied by the reviewer: the 751 shape is now 'valid only in 751' and the Jebel Nafusa keyframe is kharijites_752 (from 752). Before, Tripolitania was drawn in both dossiers in 752, against this dossier's own 752 loss.
For the author or a gap-filler: /keyframe_review/2 keeps about 64,000 km2 of eastern Algeria. The 757 gains come from the Fihrids, who never held it, so no event gains it. Cut it, as fihrids does, or find a page.
Thin: /ledger/0 (start 751, conf 1).

## rustamid-dynasty (fail)
- BLOCKING, /keyframe_review/1 (and /keyframe_review/0 from 880). The Rustamid dynasty page reads: 'However, its area contracted to Tahert and the area surrounding it by the 880s.' The dossier keeps the unchanged 469,781 km2 outline to 909 and has no loss event. The very next sentence, which the dossier uses ('Despite this, the spiritual authority of the Rustamid imams extended beyond its territory...'), places the Aures, Zab and Jabal Nafusa outside the territory after the contraction.
  Needed: a loss by 880 (conf 2); a new keyframe 880-909 for Tahert and its surroundings; /keyframe_review/0 valid to 879; an area note.
- /wars/1 and /notes misquote the 812 peace. The page says 'Aghlabid Emir Abdallah ibn Ibrahim made peace with the Rustamids by ceding Tripolitania'; the dossier writes 'made peace by ceding Tripolitania, recipient unnamed'. Needed: an 812 gain of Tripolitania from aghlabid-dynasty (conf 2), and a decision on whether the Libyan third belongs before 812.
- /keyframe_review/0 note: the shape stops at 0.19 W, while the page has the territory 'until Tlemcen in the west' (about 1.3 W). Not blocking.
Confirmed: 777 election, 789/790 Idrisid attack, 909 capture of Tahert.

## barghawata-conference (fix)
Spot checks confirmed: 744 (Barghawata page), 1058 Aghmat and contact, Ibn Yasin killed '1058 or 1059', 'By 1060, however, they were conquered by Abu Bakr ibn Umar'.
Also confirmed:
- The 990-1000 Umayyad war is honestly flagged as a reading of 'end of the 10th century'.
- The cut of the exclave near the Strait is unsupported either way, and is said to be.
- wikidata is null because Cliopatria's Q7903 is Casablanca's.
For the author (not blocking): /identity/rulers/5 gives Abu Mansur Isa 961-1060, but the page has '?961-?' and he acceded at 22. Do not stretch his reign to the state's end.

## Cross-dossier matrix (summary; full list in the JSON)
Matched:
- Numidia -105 loss = mauretania -105 gain.
- Numidia -46 loss = roman-republic -46 gain.
- All four Fihrid/Kharijite transfers (751, 752, 757 x2).
Mismatch or missing:
- carthage /ledger/53 (-197 loss of the Libyan and Algerian coast, conf 1) against Numidia -158. Carthage should date its Tripolitanian loss -158 and add a -152 loss.
- roman-republic -201/-46 vassal pair, with no mirror in Numidia.
- mauretania -203/-148 vassal pair, with no mirror in Numidia.
- mauretania /ledger/6 gains from kingdom-of-numidia in -45, after Numidia's -46 dissolve. Its counterpart should be Masinissa II's kingdom or roman-republic.
- The Rustamid 812 cession appears in neither ledger.
Exceptions (groups not run): umayyad-caliphate (me-07), caliphate-of-cordoba (eu-12), abbasid-caliphate and fatimid-caliphate (me-08), almoravid-dynasty and aghlabid-dynasty (af-02, other parts), masaesyli (af-02-x).
