# Review of batch eu-02-x (2026-10-19)

Adversarial review of the eleven additions dossiers of group eu-02 (Hellenistic world). Machine copy: history/notes/phase-b/reviews/eu-02-x.json. The validator (--resolve) gave 0 errors for all eleven before and after the reviewer's edits; warnings are only the unknown names Acarnania and Gytheio.

## Verdicts

### boeotian-league: fail

- To do (author) at `/ledger (missing, after /ledger/6)`: No vassal pair for the Antigonid overlordship of Boeotia 236-196, which antigonid-dynasty carries as /ledger/30 (vassal_start -236, counterpart 'Boeotian League', confidence 3) and /ledger/60 (vassal_end -196). Evidence: Demetrius II Aetolicus page, opened by the reviewer: 'In 236 BC, he invaded Boeotia, making the Boeotians submit immediately.' The author's notes admit the overlap ('antigonid-dynasty and this dossier overlap on Boeotia 236-196') but a missing mirror is not one of the brief's accepted exceptions. Fix: Add vassal_start -236 counterpart antigonid-dynasty, region Boeotia, confidence 3, source https://en.wikipedia.org/wiki/Demetrius_II_Aetolicus (quote above); add vassal_end -196 counterpart antigonid-dynasty from the Second Macedonian War page (Isthmian proclamation of 196, as antigonid-dynasty /ledger/60); add the Demetrius II page to sources.
- To do (author) at `/ledger/6`: vassal_end of the Aetolian membership dated -244 at confidence 1 as a bridge, when a page dates its end. Evidence: Demetrius II Aetolicus page: at his accession he dealt the Aetolian-Achaean coalition 'severe blows, wresting Boeotia from their alliance', and invaded Boeotia in 236. Fix: Move /ledger/6 to -236 (it then pairs with the new Antigonid vassal_start), confidence 2, source the Demetrius II page.
- To do (author) at `/ledger/0 and /keyframe_review/0`: Boeotia 315-304 is claimed by three dossiers: this one (keyframe 315-224, found from macedonian-empire), macedonian-empire (keeps Boeotia to its /ledger/65, a 304 loss of 'Corinth ... Boeotia ... Euboea' to antigonid-dynasty) and antigonid-dynasty (/ledger/2, 304 gain of Boeotia from macedonian-empire); macedonian-empire has no 315 loss to this dossier. Evidence: Cross-dossier read of macedonian-empire and antigonid-dynasty ledgers; the Demetrius I page (opened) says only that in 304 he 'reinstated the Corinthian League', and the author's notes list the 304 gain and 301 loss as unrepeated. Fix: Either record 304 vassal_start / 301 vassal_end with antigonid-dynasty (Demetrius I page) and say in the found note that macedonian-empire keeps Cassander's hold, or explain in a keyframe note why the league, not Cassander, holds Boeotia 315-304; route the mirrors to eu-02-a.
- Thin at `/ledger/6`: end of the c. 245 Aetolian membership (confidence 1) (try https://en.wikipedia.org/wiki/Demetrius_II_Aetolicus)
- Thin at `/ledger/8`: Megara's return to the Achaean League (203 or 193 on the page; achaean-league records no regain of Megara) (try https://en.wikipedia.org/wiki/Philopoemen)
- Spot checks: /ledger/3 confirmed; /ledger/4 confirmed; /ledger/7 confirmed; /ledger/11 confirmed; /ledger/9 confirmed; /ledger/5 confirmed
- Area: The Boeotian League page has no area (its infobox is the modern regional unit's); no Cliopatria row; the author's gazetteer figure for Boeotia (about 3,500 km2, 14 cells) is plausible.

### acarnanian-league: fix

- Applied by reviewer at `/keyframe_review/1 and new /keyframe_review/2`: Keyframe acarnanian-league_-230 ran to -169 without the southern part, although /ledger/4 returns the south to the League in -189. Evidence: Brief check 4: keyframes and ledger must agree; the Acarnania page: 'Under the Romans, or probably a little earlier, the river Achelous formed the boundary between Acarnania and Aetolia', and Leucas 'was separated from Acarnania' only after Perseus's defeat (168). Fix: Applied: keyframe -230 now ends -190; new keyframe acarnanian-league_-189 (-189..-169, region Acarnania with Leucas, verdict adjust, source Acarnania page). Re-validated with --resolve: 0 errors.
- Thin at `/ledger/4`: the year the southern cantons (Stratos, Oeniadae) returned from Aetolia (confidence 1, borrowed from aetolian-league's 189) (try https://en.wikipedia.org/wiki/Oeniadae)
- Thin at `/wars/0`: the year and side of the Acarnanian capitulation in the Second Macedonian War (try https://en.wikipedia.org/wiki/Second_Macedonian_War)
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/5 confirmed; /ledger/7 confirmed
- Area: Acarnania page body (no infobox): 'about 1,571 square miles (4,070 km2)'; matches the author's figure. No Cliopatria row; 'Acarnania' is not in the gazetteer.

### tylis: fix

- Applied by reviewer at `/ledger/0 and /ledger/1`: Found and dissolve at confidence 3 on an 80 km disc (about 20,000 km2) that no page gives. Evidence: Comontorius page: no territory, only 'a Celtic king in Thrace'; Tylis page: 'The text gives no size or area'. Brief check 7: confidence 3 with a region the page does not name is lowered to 2. Fix: Applied: both events confidence 2, with a reviewer note; years unchanged (278 and 212 are on the Comontorius and Cavarus pages).
- Thin at `/keyframe_review/0`: any extent of the kingdom (thin by design within the 1-2 page budget; the disc is a placeholder) (try https://en.wikipedia.org/wiki/Thrace)
- Thin at `/ledger/0`: the Byzantine tribute (undated on the Comontorius page) and who took the land in 212 (try https://en.wikipedia.org/wiki/Byzantium)
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /keyframe_review/0 confirmed
- Area: No page gives an area; no Cliopatria row; the 80 km disc (about 20,000 km2) is acknowledged as a placeholder in the keyframe note.

### scordisci: fix

- Applied by reviewer at `/keyframe_review/1/to`: The last keyframe ended -9 while the state ends -8 with the annexation, leaving the end year without a shape. Evidence: Scordisci page: 'With the suppression of the Pannonian revolts of 11-8 BC their territory was annexed.' Fix: Applied: to -8.
- Applied by reviewer at `/wars/1/from`: War 'Scordisci raids on Roman Macedonia' started -120 although its outcome cites the 141 BC defeat of the Romans. Evidence: Scordisci page: 'In 141 BC the Scordisci defeated the Romans on their own account.' Fix: Applied: from -141.
- Thin at `/ledger/1`: the stages of 2nd-century growth to the maximum (confidence 1, '200' stands for the century) (try https://en.wikipedia.org/wiki/Moesia)
- Thin at `/keyframe_review/1`: Burebista's subjugation of the Scordisci ('he later subdued them', undated on the page) is not in the ledger (try https://en.wikipedia.org/wiki/Burebista)
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/4 confirmed; /wars/0 confirmed
- Area: The Scordisci page has no infobox or area; no Cliopatria row; the Serbia-plus-Drina shape (about 71,600 km2 plus the band) is acknowledged as an approximation.

### macedonian-republics: fix

- Applied by reviewer at `/keyframe_review/1/to`: The last keyframe ended -149 while the republics end -148. Evidence: Macedonia (Roman province) page: 'After defeating Andriscus near Pydna in 148 BC' and 'The date of the establishment of the province in autumn 148 BC'. Fix: Applied: to -148.
- Spot checks: /ledger/0 confirmed (168 implied by placement after Pydna; confidence 2 is right); /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed
- Area: Macedonia (Roman province) infobox gives 'Established: 146 BC' and no area; no Cliopatria row; Ancient Macedon region (about 25,500 km2) stands in.

### league-of-the-islanders: fail

- To do (author) at `/ledger/0 and /ledger/1`: The patron of 314 is antigonid-dynasty, whose life starts in -306 (its /ledger/0 found from macedonian-empire); Antigonus I's realm is inside macedonian-empire until that dossier's /ledger/63 split in 306. Evidence: antigonid-dynasty identity.start = -306; macedonian-empire /ledger/63 (306 split to antigonid-dynasty). A counterpart that does not exist for 8 of the relation's 27 years cannot carry the mirror. Fix: Name macedonian-empire as counterpart of /ledger/0 and /ledger/1 and add the 306 hand-over (vassal_end macedonian-empire, vassal_start antigonid-dynasty, confidence 2, League page: the League continued 'despite the defeat and death of Antigonus at the Battle of Ipsus'), or start the vassal relation in 306 and say so.
- To do (author) at `/ledger/5 and /ledger/6`: The islands go to greek-city-states in 260 and come back from antigonid-dynasty in 200, but neither dossier holds them in between (greek-city-states has no 260 gain, antigonid-dynasty no 201 gain of the Cyclades). Evidence: Cross-dossier read; League page: 'In 201 BC, during the Cretan War, Philip V of Macedon subdued the Cyclades at the head of his fleet.' Fix: Add a 201 loss to antigonid-dynasty (gain for it) or make the 200 gain's counterpart greek-city-states; route the mirrors to eu-01 and eu-02-a.
- Thin at `/ledger/4`: end of Ptolemaic hegemony (confidence 1, c. 260 bridge) (try https://en.wikipedia.org/wiki/Chremonidean_War)
- Thin at `/ledger/5`: who held the Cyclades 260-201 (confidence 1 placeholder) (try https://en.wikipedia.org/wiki/Battle_of_Andros)
- Thin at `/ledger/6`: whom Rhodes took the islands from in c. 200 (confidence 1) (try https://en.wikipedia.org/wiki/Cretan_War_(205%E2%80%93200_BC))
- Spot checks: /ledger/0 confirmed; /ledger/3 confirmed; /ledger/6 confirmed; /ledger/8 confirmed
- Area: The page gives no area; no Cliopatria row; the Cyclades region stands in (acknowledged).

### thessalian-league-roman-era: fix

- Applied by reviewer at `/keyframe_review/0/to`: The only keyframe ended -147 while the League is dissolved in -146. Evidence: Thessalian League page: Rome 'tolerated [it] until 146 BCE, when the Roman commander Mummius razed the city of Corinth' and disbanded the leagues. Fix: Applied: to -146.
- Applied by reviewer at `/wars/0`: The Second Macedonian War (200-197) lay outside the state's life (validator warning) with the League as a belligerent before it existed. Evidence: Thessalian League page: 'Rome established Thessaly as a koinon, Federal League' at the end of the Second Macedonian War, in 196. Fix: Applied: war entry removed, reason added to notes (the war is in antigonid-dynasty and roman-republic).
- Thin at `/ledger/3`: the return of the Thessalian towns occupied in 191 (confidence 1, c. 185) (try https://en.wikipedia.org/wiki/Philip_V_of_Macedon)
- Spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/4 confirmed; /ledger/5 confirmed
- Area: No page gives an area; no Cliopatria row after 353; Thessaly region (about 12,400 km2) stands in.

### macedon-281-277: thin

- To do (author) at `/keyframe_review/0/correction and /ledger/0`: Thessaly is left out of Keraunos's realm although kingdom-of-lysimachus /ledger/23 hands 'Macedon, Thessaly and Thrace' to him in 281; no dossier holds Thessaly 281-277 (antigonid-dynasty loses it to Pyrrhus in 274 with no earlier gain). Evidence: Cross-dossier read; the Keraunos page (opened) gives no territory either way, so this is a land disagreement, not a fault of a page. Fix: Either add {region: Thessaly} minus a Demetrias disc to keyframe -281 (and -279) and /ledger/0, or explain in the keyframe note who held Thessaly; routed as a mismatch, not blocking.
- Thin at `/ledger/5`: who held Lysimachia and the Thracian coast after 279 (confidence 1 bridge) (try https://en.wikipedia.org/wiki/Antigonus_II_Gonatas)
- Thin at `/keyframe_review/0`: Thessaly 281-277 and the capital (no page names one; Pella unsourced) (try https://en.wikipedia.org/wiki/Pyrrhus_of_Epirus)
- Spot checks: /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed (the page does not itself say Sosthenes deposed Antipater; the Antipater page does); /ledger/7 confirmed
- Area: No page gives an area; no Cliopatria row for 281-278; shapes are regions (41,500 then 25,500 km2), acknowledged.

### league-of-free-laconians: pass

- Thin at `/ledger/3`: how Nabis's 192 hold on Gythium ended (confidence 1; the League page says Nabis retook Gythium, so a loss/gain pair inside 192 would also fit) (try https://en.wikipedia.org/wiki/Nabis)
- Thin at `/keyframe_review/1`: the 24 member cities (Pausanias's list is empty on the page) (try https://en.wikipedia.org/wiki/Gytheio)
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/5 confirmed; /ledger/6 confirmed; /ledger/7 confirmed
- Area: The page gives no area; no Cliopatria row; two 15 km discs shared with peloponnesian-league.

### dalmatae: fix

- Applied by reviewer at `/identity/capitals/0/to`: Delminium's capital span ended -156, a year before its destruction. Evidence: Dalmatae page: 'The first Dalmatian war in 156-155 BC finished with the destruction of capital Delminium by consul Scipio Nasica'. Fix: Applied: to -155.
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/4 confirmed; /ledger/5 confirmed; /ledger/6 confirmed; /ledger/8 confirmed
- Area: The Dalmatae page has no infobox or area; no Cliopatria row; the Dalmatia region (12,100 km2) stands in; the overlap with Cliopatria's Roman Republic shape 150-40 BC is flagged in the keyframe note.

### league-of-corinth: fix

- Applied by reviewer at `/ledger/2 (removed)`: A 331 'gain' of Sparta (30 km disc) from peloponnesian-league that the page does not support, in an umbrella dossier that holds no territory; peloponnesian-league keeps Sparta to 192 and has no mirror. Evidence: League of Corinth page: Sparta's appeal was 'agreed on condition that the Lacedaemonians now joined the League of Corinth'; the page does not say Sparta joined (the author's note says the same). Fix: Applied: event removed, reason added to notes. Re-validated: 0 errors.
- Spot checks: /ledger/0 confirmed (infobox 338/337; mid 337 camp near Corinth); /ledger/1 confirmed (infobox ruler list: 336 BC Alexander III); /ledger/2 not on page (Sparta joining is not stated; event removed); /ledger/3 confirmed
- Area: Umbrella with no keyframes; the infobox lists no area.

## Cross-dossier matrix (unmatched and mismatched only)

- boeotian-league -315 found (macedonian-empire): missing. macedonian-empire keeps Boeotia (Cassander) to its 304 loss to antigonid-dynasty (/ledger/65); no 315 loss to the league. Overlap 315-304. Route to eu-02-a.
- boeotian-league -287 gain (antigonid-dynasty): missing. antigonid-dynasty has no 287 loss of Boeotia (Thebes page: 'recovered its autonomy from Demetrius in 287 BC'). Route to eu-02-a.
- boeotian-league -245 vassal_start (aetolian-league): missing. aetolian-league /ledger/5 (-245 gain, confidence 1) explicitly excludes Boeotia; no client tint. Route to eu-02-a.
- boeotian-league -244 vassal_end (aetolian-league): missing. No mirror; the Demetrius II page puts the end at 236 (see boeotian-league fixes).
- antigonid-dynasty -236 vassal_start (Boeotian League): missing. antigonid-dynasty /ledger/30 (confidence 3, Demetrius II page) has no mirror in boeotian-league: boeotian-league's fault (fail).
- antigonid-dynasty -196 vassal_end (Boeotian League): missing. antigonid-dynasty /ledger/60; no mirror in boeotian-league.
- boeotian-league -193 loss (achaean-league): missing. achaean-league has no regain of Megara (the author's notes say 192; not found in its ledger). Route to eu-02-a.
- acarnanian-league -314 found (macedonian-empire): missing. No Acarnanian event in macedonian-empire; low priority (Cassander's reorganisation).
- acarnanian-league -250 loss (kingdom-of-epirus): missing. kingdom-of-epirus has no c. 250 gain of north Acarnania with Leucas. Route to Epirus's group (eu-02-b).
- acarnanian-league -230 gain (kingdom-of-epirus): missing. kingdom-of-epirus has only a -231 loss of Ambracia to aetolian-league; no 230 loss of Acarnania.
- acarnanian-league -189 gain (aetolian-league): mismatch. aetolian-league /ledger/26 (-189, confidence 1) loses the central Greek cantons to greek-city-states, not Acarnania; both sides are bridges.
- acarnanian-league -168 loss (roman-republic): missing. roman-republic's 167 gain is Epirus from molossians (/ledger/73); Leucas absent. Route to eu-03.
- tylis -278 found (odrysian-kingdom): mismatch. odrysian-kingdom ends -281 (/ledger/20 dissolve to 'Celts of Comontorius (Tylis)', Seuthopolis sacked 281); tylis starts 278 (Comontorius page). Three years apart; both dates are on pages. Odrysian's counterpart should become slug tylis or nobody.
- macedonian-republics -168 found (antigonid-dynasty): mismatch. antigonid-dynasty /ledger/70 dissolves to roman-republic, not to the republics; change its counterpart to macedonian-republics.
- league-of-the-islanders -314 vassal_start (antigonid-dynasty): mismatch. antigonid-dynasty starts -306; the patron of 314-306 is inside macedonian-empire (see fixes).
- league-of-the-islanders -287 vassal_end (antigonid-dynasty): missing. antigonid-dynasty has no Cyclades events. Route to eu-02-a.
- league-of-the-islanders -260 loss (greek-city-states): missing. Confidence-1 placeholder; greek-city-states has no 260 gain of the Cyclades.
- league-of-the-islanders -200 gain (antigonid-dynasty): missing. antigonid-dynasty has no 201 conquest or 200 loss of the Cyclades.
- league-of-the-islanders -200 vassal_start (rhodes): missing. rhodes has no hegemony over the Second League. Route to Rhodes's group (eu-02-b).
- league-of-the-islanders -167 vassal_end (rhodes): mismatch. rhodes /ledger/3 ends a vassal relation in 167 but with 'Caria and Lycia', not the Islanders.
- thessalian-league-roman-era -196 vassal_start (roman-republic): missing. roman-republic has no 196 protection of Thessaly. Route to eu-03.
- thessalian-league-roman-era -191 occupation_start (antigonid-dynasty): mismatch. antigonid-dynasty /ledger/62 records a gain (its own note says 'Macedon occupies Thessalian towns'); one side should change type.
- thessalian-league-roman-era -185 occupation_end (antigonid-dynasty): mismatch. antigonid-dynasty /ledger/64 records a loss; type mismatch as above.
- thessalian-league-roman-era -146 dissolve (roman-republic): mismatch. roman-republic /ledger/81 gains the Achaean League's lands in 146; Thessaly is not in it (and Thessaly may already be in its 148 Macedonia gain).
- macedon-281-277 -281 found (kingdom-of-lysimachus): mismatch. kingdom-of-lysimachus /ledger/23 (string 'Ptolemy Keraunos (Macedon and Thrace, 281-279)') includes Thessaly; macedon-281-277 omits it. Change the string to the slug and settle Thessaly.
- league-of-free-laconians -195 vassal_start (achaean-league): missing. achaean-league has no protectorate over the Free Laconians. Route to eu-02-a.
- dalmatae -76 loss (roman-republic): missing. roman-republic has no 76 gain of Salona. Route to eu-03.
- dalmatae -33 dissolve (roman-republic): missing. roman-republic has no 33 gain of Dalmatia, and its Cliopatria shape already covers Dalmatia from 150 BC (author's finding). Route to eu-03.

## Other notes

- Reviewer edited seven dossiers in place (acarnanian-league, tylis, scordisci, macedonian-republics, thessalian-league-roman-era, dalmatae, league-of-corinth); each re-validated with 0 errors and was read back after the write.
- league-of-corinth is type 'umbrella'; reviewer brief 2.9 says an umbrella is never a dossier of its own, but latin-league and mahajanapadas set the precedent: the orchestrator should decide whether it stays.
- thessalian-league-roman-era is the same institution as thessalian-league (eu-01-x, -374..-353) refounded after 143 years; kept as a separate state (a new state on the same land), but the colour agent should give them one colour or the orchestrator should merge.
- Neighbour dossiers name the new states by string; they should switch to the slugs: antigonid-dynasty ('Boeotian League', 'Thessalian League', 'Sosthenes (Macedon, 279-277)'), achaean-league ('Boeotian League'), aetolian-league ('Acarnanian League'), kingdom-of-lysimachus ('Ptolemy Keraunos (Macedon and Thrace, 281-279)'), roman-republic ('Macedonian merides (four client republics)'), peloponnesian-league ('League of Free Laconians'), illyrian-kingdom ('Dalmatae'), odrysian-kingdom ('Celts of Comontorius (Tylis)').
- Seen in passing, not this batch: macedonian-empire /ledger/61 (-307 loss of Attica to antigonid-dynasty) falls a year before antigonid-dynasty's start (-306).
- Context polities in section 6 with files: carthage, cimmerian-bosporus, greek-city-states, kingdom-of-kush, mamertines, maurya-empire, nanda-empire, roman-republic, scythia; only greek-city-states and roman-republic touch this batch. The rest (achaemenid-empire, atropatene, greco-bactrian-kingdom, kingdom-of-armenia, kingdom-of-bithynia, kingdom-of-pergamon, kingdom-of-pontus, laomedon, perdiccas, ptolemaic-kingdom, seleucid-empire) are owned by groups that have not run. The real counterparts (antigonid-dynasty, aetolian-league, achaean-league, kingdom-of-epirus, macedonian-empire, kingdom-of-lysimachus, odrysian-kingdom, illyrian-kingdom, rhodes, peloponnesian-league) were read too.
- No page failed to load for the reviewer. Every spot-checked event was on its page with its year except league-of-corinth's 331 Sparta gain (removed).
