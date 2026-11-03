# Review of batch eu-03-x (Roman Republic additions)

Reviewer, 2026-10-19. Machine copy: history/notes/phase-b/reviews/eu-03-x.json. Validator: 28 files, 0 errors, 0 warnings (before and after the reviewer's edits).

Verdicts: pass = nothing to change; fix = accepted, findings marked applied were made by the reviewer and the rest are small author fixes; thin = honest but gaps for a gap-filler; fail = a blocking finding goes back to the author.

## Batch-level

- No page failed to load. Lusitanians, Kingdom of Noricum and the 'Siege of Capua (211 BC)' article were opened by the reviewer in addition to the author's pages.
- The 16 dossiers kept from the 2026-10-18 run all fail on one blocking defect: keyframe_review is empty for states Cliopatria lacks. The fix is mechanical (keyframes from the found/loss regions) and needs no new pages; the spot checks of their ledgers found no fabricated event (one note error, samnites /ledger/10, corrected).
- Applied by the reviewer and re-validated (0 errors, 0 warnings): type umbrella->state in 11 kept dossiers; family -> colours.json key in 15 (italic, gallic, venetic, latin -> italy; celtic, iberian -> iberia; greek -> hellenistic); capua /ledger/2 confidence 1->2; aequi /ledger/1-2 confidence 1->2; samnites /ledger/10 note; lusitanians identity.wikipedia; syracuse /ledger/11-12 and sertorian-hispania /ledger/3-4 counterpart slugs.
- Most unmatched events are on roman-republic's side (eu-03-b): it names string counterparts ('Arverni and Allobroges', 'Gallic tribes (...)', 'Messapii and Sallentini') or carthage where the new slugs exist, and it models the Samnites, Lucanians, Umbri and Insubres as vassals after dates where these dossiers dissolve. The orchestrator should decide one convention (vassal tint vs dissolve) and route both sides.
- Land claimed twice inside this batch: capua and samnites (Caserta, -424..-343); insubres and cenomani (Brescia, Cremona, Mantova, -400..-197); adriatic-veneti and cenomani (Verona, -400..-89); boii and senones (Rimini, -390..-283); picentes' 390 loss and umbri's (same provinces).
- Wikidata ids in the kept dossiers were never verified (wikidata.org unreachable); the 12 new dossiers carry null.

## arverni: pass

- thin `/ledger/0`: Founding year: the page gives only the first record (207 BC, 'end of the 3rd century BC'); -250 is a confidence-1 placeholder. Try: https://en.wikipedia.org/wiki/Luernius
- thin `/ledger/1`: Date and places of the Arvernian clientele (Vellavii, Gabali, Cadurci, Eleuteti) and the extent of the Luernius/Bituitus hegemony. Try: https://en.wikipedia.org/wiki/Cadurci
- spot checks: /ledger/2 confirmed (Bituitus); /ledger/3 confirmed (Allobroges); /ledger/4 confirmed (Arverni); /ledger/7 confirmed (Arverni)

## allobroges: pass

- thin `/ledger/0`: Founding: 218 is the first dated mention (Hannibal), confidence 1. Try: https://en.wikipedia.org/wiki/Gallia_Narbonensis
- spot checks: /ledger/0 confirmed (Allobroges); /ledger/1 confirmed (Allobroges); /ledger/2 confirmed (Battle_of_Vindalium); /ledger/3 confirmed (Allobroges); /ledger/4 confirmed (Allobroges)

## ligures: pass

- thin `/ledger/0`: Start -500 is a placeholder (the page gives a Middle Bronze Age culture area, no polity date). Try: https://en.wikipedia.org/wiki/Ligures
- thin `/ledger/4`: The Piedmont tribes (Taurini, Statielli 173, Bagienni) go to Rome with the 155 loss; the page only says 'By the mid-2nd century BC the Italian Ligures were subdued'. Try: https://en.wikipedia.org/wiki/Taurini
- spot checks: /ledger/1 confirmed (Ligures); /ledger/2 confirmed (Ligures); /ledger/3 confirmed (Ligures); /ledger/4 confirmed (Ligures)

## bruttii: fix

-  `/ledger (new, between /ledger/4 and /ledger/5)`: The peace after Pyrrhus, a land loss, is missing; the notes call it undated. Evidence: Bruttii page: 'After Pyrrhus was expelled in 275 BC, the Bruttii were compelled to purchase peace by the surrender of one-half of the great forest of Sila.' Fix: Add a loss c. -272 (or -275), counterpart roman-republic, region a disc on the Sila plateau (about 16.55E 39.30N, 25 km, text 'one-half of the great forest of Sila'), confidence 2, source the Bruttii page; mention it in the keyframe_review/3 note (small, inside one shape).
-  `/ledger (new, -272 and -215)`: No subject-ally tie to Rome between the Pyrrhic peace and the defection to Hannibal. Evidence: roman-republic /ledger/24 (-272 vassal_start): 'the Lucanians and Bruttians reduced to subjection in a ten-year campaign (272)'; Bruttii page: they 'rebelled and allied with Hannibal after the Battle of Cannae'. Fix: Add vassal_start -272 counterpart roman-republic (confidence 2) and vassal_end -215 at the defection; ask eu-03-b to name bruttii in its -272 vassal_start.
- thin `/ledger/1`: Date of the occupation of Hipponium, Terina and Thurii ('less than 30 years after their first revolt'); -340 is a bridge. Try: https://en.wikipedia.org/wiki/Hipponium
- thin `/ledger/3`: Return of Terina after Alexander's death (bridge, confidence 1); the Bruttii page dates the death 326, the Alexander page 331. Try: https://en.wikipedia.org/wiki/Terina
- thin `/ledger/5`: Peace with Rome c. 272 (confidence 1). Try: https://en.wikipedia.org/wiki/Bruttium
- spot checks: /ledger/0 confirmed (Bruttii); /ledger/2 confirmed (Alexander_I_of_Epirus); /ledger/3 confirmed (Alexander_I_of_Epirus); /ledger/6 confirmed (Bruttii); /ledger/7 confirmed (Bruttii); /ledger/8 confirmed (Bruttii)

## helvetii: pass

- thin `/ledger/0`: Start -100 is a placeholder ('late 2nd century BC' for the move south). Try: https://en.wikipedia.org/wiki/Tigurini
- spot checks: /ledger/0 confirmed (Helvetii); /ledger/1 confirmed (Battle_of_Bibracte); /ledger/2 confirmed (Battle_of_Bibracte); /ledger/3 confirmed (Helvetii)

## aedui: pass

- thin `/ledger/0`: Start -150 is the alliance date ('around 150-140 BC'), not the tribe's. Try: https://en.wikipedia.org/wiki/Bibracte
- thin `/ledger/1`: Client ties (Segusiavi, Mandubii) undated; -100 is a placeholder. Try: https://en.wikipedia.org/wiki/Segusiavi
- thin `(no event)`: Ariovistus's seizure of land in 61 (Magetobriga): the author reads the Ariovistus page as taking 'a third of Aedui land', the Sequani page says Sequani land; no event either way in aedui. Try: https://en.wikipedia.org/wiki/Ariovistus
- spot checks: /ledger/0 confirmed (Aedui); /ledger/2 confirmed (Aedui); /ledger/4 confirmed (Battle_of_Alesia); /ledger/5 confirmed (Aedui)

## sequani: thin

- thin `/ledger/0`: Start -100 is a placeholder (confidence 1). Try: https://en.wikipedia.org/wiki/Vesontio
- thin `/ledger/2`: The end in 52 is a confidence-1 bridge; the Sequani page gives only the 12,000-man contingent in the 52 revolt (that quote is on the Sequani page, not the cited Alesia page, which never names the Sequani). Try: https://en.wikipedia.org/wiki/Sequani
- thin `/ledger/3`: Dissolve 52 (confidence 1); incorporation into Gallia Belgica 'under Augustus' is undated. Try: https://en.wikipedia.org/wiki/Gallia_Belgica
- thin `/keyframe_review/1`: Placing the c. 70 loss in Haut-Rhin is the author's reading ('Part of their territory was occupied around 70 BC'); the page does not say which part. Try: https://en.wikipedia.org/wiki/Ariovistus
- spot checks: /ledger/1 confirmed (Sequani); /ledger/2 confirmed (Sequani); /ledger/2 confirmed (Battle_of_Alesia); /ledger/3 confirmed (Sequani)

## messapii: pass

- thin `/ledger/0`: Start -550 rests on the attestation of Messapic (mid-6th century), confidence 1. Try: https://en.wikipedia.org/wiki/Iapygians
- thin `(no event)`: Archidamus III at Manduria (342-338) is on the page but unplaced; Daunians and Peucetians are not drawn. Try: https://en.wikipedia.org/wiki/Peucetians
- spot checks: /ledger/1 confirmed (Messapii); /ledger/2 confirmed (Messapii); /ledger/3 confirmed (Messapii); /ledger/4 confirmed (Messapii)

## kingdom-of-noricum: fix

-  `/keyframe_review/0/correction`: The shape takes all of Oberosterreich and Niederosterreich, including the land north of the Danube (Muhlviertel, Waldviertel, Weinviertel) and the Vienna basin, about a fifth of the 65,000 km2. Evidence: Noricum page: borders were 'the Danube to the north ... Pannonia to the east and southeast'; the correction's own text says 'the Danube to the north'. Fix: Subtract the land north of the Danube and east of the Wienerwald from the keyframe correction and from the matching regions in /ledger/0, /ledger/3, /ledger/4 and the successor land (a minus of a named region or, failing one, a polygon north of the river); optionally add the Slovenian fringe the page names ('part of Slovenia').
- thin `/identity/end`: The Kingdom of Noricum infobox gives 'c. 200 BC-c. 50 AD'; the dossier ends at 16 BC with the province (noted by the author). Try: https://en.wikipedia.org/wiki/Kingdom_of_Noricum
- spot checks: /ledger/0 confirmed (Noricum); /ledger/1 confirmed (Battle_of_Noreia); /ledger/2 confirmed (Battle_of_Noreia); /ledger/3 confirmed (Noricum)

## capua: fix

- [applied]  `/ledger/2/confidence`: The 216 defection was confidence 1 with the note 'neither page gives the year'. Evidence: Siege of Capua (211 BC) page: the defection 'after the Battle of Cannae in 216 BC was perhaps the most significant of his gains'. Fix: Confidence 2 and the note and /keyframe_review/1/note corrected (done by the reviewer).
-  `/ledger/0 (cross-dossier)`: Capua's independent Campanian state (Caserta, -424..-343) is also claimed by samnites, which gains all of Campania from the Etruscans at -424 and loses it to Rome only at -338; etruscans -424 names samnites, not capua. Evidence: Capua page: 'In about 424 BC, Capua was captured by the Samnites' and 'in 343 BC, it sought Roman help against its conquerors'; samnites /ledger/1 and /ledger/4; etruscans /ledger/9. Fix: No change needed in capua; samnites must exclude Caserta (see samnites) and etruscans' -424 loss should name capua for Caserta. Listed here so the pair is fixed together.
- spot checks: /ledger/0 confirmed (Capua); /ledger/1 confirmed (First_Samnite_War); /ledger/2 confirmed (Siege_of_Capua_(211_BC)); /ledger/3 confirmed (Siege_of_Capua_(211_BC)); /ledger/4 confirmed (Siege_of_Capua_(211_BC)); /ledger/5 confirmed (Siege_of_Capua_(211_BC))

## cantabri: pass

- thin `/ledger/0`: Start -200 is a placeholder (Cantabrian mercenaries with Hannibal, undated). Try: https://en.wikipedia.org/wiki/Cantabri
- spot checks: /ledger/0 confirmed (Cantabri); /ledger/1 confirmed (Cantabrian_Wars); /ledger/2 confirmed (Cantabrian_Wars); /ledger/3 confirmed (Cantabri)

## cenomani: fix

-  `/ledger (new, -225, -200, -197)`: The alliance with Rome and its breach, on the cited page, are missing; the war 'Cisalpine Gallic revolt (200-197 BC)' has no ledger events. Evidence: Cenomani (Cisalpine Gaul) page: after Telamon (225) Rome 'won the Cenomani as allies' (formal amicitia); 'By 200 BC the Cenomani had gone over to the anti-Roman side' and joined the attack on Placentia; in 197 Roman envoys 'secured at least their neutrality' and the Cenomani attacked the Insubres from behind. Fix: Add vassal_start -225 (counterpart roman-republic, confidence 2), vassal_end -200 and contest_start -200 / contest_end -197 (or vassal_start -197) with the same page; ask eu-03-b to mirror the tie (the author already flagged roman-republic's side).
- thin `/ledger/0`: Settlement -400 (confidence 1; Williams 'no later than the early 4th century BC'). Try: https://en.wikipedia.org/wiki/Cenomani_(Cisalpine_Gaul)
- thin `/ledger/1`: Year of the Cremona colony on Cenoman land (218 is taken from roman-republic, confidence 1). Try: https://en.wikipedia.org/wiki/Cremona
- spot checks: /ledger/0 confirmed (Cenomani_(Cisalpine_Gaul)); /ledger/1 confirmed (Cenomani_(Cisalpine_Gaul)); /ledger/2 confirmed (Cenomani_(Cisalpine_Gaul)); /wars/0 confirmed (Cenomani_(Cisalpine_Gaul))

## adriatic-veneti: fail

- [blocking]  `/keyframe_review`: Empty for a state Cliopatria lacks: the dossier has no shape. Evidence: research-brief s.6: for such states 'every keyframe is a new one'; check 4 cannot run; the author listed it as a gap. Fix: Add one keyframe per period (shape_id adriatic-veneti_<from>, from, to, verdict adjust, correction = found region minus later losses, source = the event's page); no new pages needed.
- [applied]  `/identity/type`: 'umbrella' for a land-holding people. Evidence: schema: umbrella is 'never coloured as territory'. Fix: state (done by the reviewer).
- [applied]  `/identity/family`: 'venetic' is not a colours.json family. Evidence: schema: family must be a key of colours.json families. Fix: italy (done by the reviewer).
-  `/ledger/1`: The 181 loss of Aquileia is land the Veneti never hold in this dossier. Evidence: Aquileia (13.37E) lies outside the found region 'Venetia' (gazetteer bbox ends at 12.95E) and beyond the Tagliamento, which the Adriatic Veneti page gives as their eastern limit ('reached up to the Tagliamento river'); the page names the colony (181 BC) but not whose land it took. Fix: Drop the loss, or extend the shape to the Isonzo with a page that puts Aquileia's site in Venetic land.
-  `/ledger (new, -238)`: The c. 238 alliance with Rome is missing. Evidence: Adriatic Veneti page: 'They established amicitia with Rome against the Gauls c. 238 BC'; roman-republic /ledger/47 vassal_start adriatic-veneti -238 and /ledger/139 vassal_end -89. Fix: Add vassal_start -238 counterpart roman-republic (confidence 2) and vassal_end -89 beside the dissolve.
-  `/ledger/0/region`: 'Venetia' includes Verona province, which cenomani holds -400..-89. Evidence: Cenomani (Cisalpine Gaul) page: 'Verona also lay within their territory', eastern limit 'the Tartaro, or perhaps the Adige'. Fix: From c. -400 (the Gallic settlement) draw Venetia minus Verona west of the Adige, in the keyframes.
-  `/identity/wikidata`: Q210113 was not verified (wikidata.org unreachable). Evidence: No page opened in either run gives the id. Fix: Check or null it.
- thin `/ledger/2`: The 89 date comes from the Insubres page; the Veneti page names the Lex Pompeia without a year. Try: https://en.wikipedia.org/wiki/Lex_Pompeia_de_Transpadanis
- spot checks: /ledger/0 confirmed (Adriatic_Veneti); /ledger/1 confirmed (Adriatic_Veneti); /ledger/2 confirmed (Insubres)

## aequi: fail

- [blocking]  `/keyframe_review`: Empty for a state Cliopatria lacks: the dossier has no shape. Evidence: research-brief s.6: for such states 'every keyframe is a new one'; check 4 cannot run; the author listed it as a gap. Fix: Add one keyframe per period (shape_id aequi_<from>, from, to, verdict adjust, correction = found region minus later losses, source = the event's page); no new pages needed.
- [applied]  `/identity/type`: 'umbrella' for a land-holding people. Evidence: schema: umbrella is 'never coloured as territory'. Fix: state (done by the reviewer).
- [applied]  `/identity/family`: 'italic' is not a colours.json family. Evidence: schema: family must be a key of colours.json families. Fix: italy (done by the reviewer).
- [applied]  `/ledger/1, /ledger/2`: Confidence 1 on years the Aequi page gives. Evidence: Aequi page: 'Their chief center is said to have been taken by the Romans about 484 BC'; 'the Battle of Mount Algidus (458 BC)'. Fix: Confidence 2 (done by the reviewer).
- thin `(no event)`: The chief centre taken about 484 and again 'about 90 years later' is drawn as contest only; a small loss could be placed if a page names the centre. Try: https://en.wikipedia.org/wiki/Alba_Fucens
- spot checks: /ledger/1 confirmed (Aequi); /ledger/2 confirmed (Aequi); /ledger/3 confirmed (Aequi); /ledger/5 confirmed (Aequi)

## boii: fail

- [blocking]  `/keyframe_review`: Empty for a state Cliopatria lacks: the dossier has no shape. Evidence: research-brief s.6: for such states 'every keyframe is a new one'; check 4 cannot run; the author listed it as a gap. Fix: Add one keyframe per period (shape_id boii_<from>, from, to, verdict adjust, correction = found region minus later losses, source = the event's page); no new pages needed.
- [applied]  `/identity/family`: 'gallic' is not a colours.json family. Evidence: schema: family must be a key of colours.json families. Fix: italy (done by the reviewer).
-  `/ledger (new, -225 and -218)`: The 225 submission and its end in 218 are missing; roman-republic's -225 vassal_start, -218 vassal_end and -218 loss to boii have no mirror. Evidence: Boii (Cisalpine Gaul) page: 'After Telamon the Boii made their first formal submission to Rome by treaty'; they allied with Hannibal 'before the Battle of the Trebia' (218). Fix: Add vassal_start -225 and vassal_end -218 (counterpart roman-republic, confidence 2); either add a -218 gain mirroring roman-republic /ledger/57 or ask eu-03-b to drop that loss.
-  `/ledger/0/region`: 'Emilia' resolves to all of Emilia-Romagna, including Rimini, which senones holds -390..-283. Evidence: gazetteer: Emilia = Bologna ... Ravenna + Rimini; senones /ledger/0 region Rimini + Pesaro e Urbino + Ancona; the Boii page puts them 'between the river and the Apennines'. Fix: Use Emilia minus Rimini (and keep Ravenna/Forli only if a page gives them to the Boii rather than the Lingones).
-  `/ledger/8`: The 191 loss gives Rome all of Emilia. Evidence: Boii page: Rome 'took only about half their territory'. Fix: Keep the loss (the Boii vanish after 191) but say so in the keyframe note; confidence 3 is fine for the year.
- spot checks: /ledger/0 confirmed (Boii_(Cisalpine_Gaul)); /ledger/3 confirmed (Boii_(Cisalpine_Gaul)); /ledger/5 confirmed (Boii_(Cisalpine_Gaul)); /ledger/8 confirmed (Boii_(Cisalpine_Gaul))

## celtiberians: fail

- [blocking]  `/keyframe_review`: Empty for a state Cliopatria lacks: the dossier has no shape. Evidence: research-brief s.6: for such states 'every keyframe is a new one'; check 4 cannot run; the author listed it as a gap. Fix: Add one keyframe per period (shape_id celtiberians_<from>, from, to, verdict adjust, correction = found region minus later losses, source = the event's page); no new pages needed.
- [applied]  `/identity/type`: 'umbrella' for a land-holding people. Evidence: schema: umbrella is 'never coloured as territory'. Fix: state (done by the reviewer).
- [applied]  `/identity/family`: 'celtic' is not a colours.json family. Evidence: schema: family must be a key of colours.json families. Fix: iberia (done by the reviewer).
-  `/identity/wikidata`: Q207335 was not verified (wikidata.org unreachable). Evidence: No page opened gives the id. Fix: Check or null it.
- thin `/ledger/1`: Which part of Celtiberia fell in 195 (Zaragoza is the author's choice; the page says 'part of Celtiberia'). Try: https://en.wikipedia.org/wiki/Cato_the_Elder
- spot checks: /ledger/1 confirmed (Celtiberians); /ledger/4 confirmed (Celtiberians); /ledger/6 confirmed (Numantine_War); /ledger/9 confirmed (Numantine_War)

## insubres: fail

- [blocking]  `/keyframe_review`: Empty for a state Cliopatria lacks: the dossier has no shape. Evidence: research-brief s.6: for such states 'every keyframe is a new one'; check 4 cannot run; the author listed it as a gap. Fix: Add one keyframe per period (shape_id insubres_<from>, from, to, verdict adjust, correction = found region minus later losses, source = the event's page); no new pages needed.
- [applied]  `/identity/family`: 'gallic' is not a colours.json family. Evidence: schema: family must be a key of colours.json families. Fix: italy (done by the reviewer).
-  `/ledger/0/region`: 'Lombardy' includes Brescia, Cremona and Mantova east of the Oglio, the Cenomani's land. Evidence: Insubres page: their land lay 'between the Ticino and the Oglio'; cenomani /keyframe_review/0 holds Brescia, Cremona, Mantova, Verona -400..-219. Fix: Use Lombardy minus Brescia, Cremona and Mantova in every Insubrian region (found, losses, keyframes, successor land).
-  `/ledger/0/counterpart`: Found -400 from nobody, but etruscans /ledger/14 loses Lombardy to insubres at -396. Evidence: Etruscan page cited there: 'from 396 BC: Invasion of the Celts into the Po Valley'. Fix: Agree with etruscans: found -396 with counterpart etruscans, or ask eu-03 to make the etruscans loss counterpart nobody.
-  `/ledger/7`: The Insubres end at 197, but roman-republic holds them as a vassal 197-89 (/ledger/80, /ledger/138). Evidence: Insubres page: 'The Insubres submitted in 197 BC'; Rome bound them 'by a treaty (foedus)'; 'The lex Pompeia of 89 BC granted Latin rights'. Fix: Either continue the dossier to -89 with vassal_start -197 (end -89, like cenomani) or ask eu-03-b to drop the vassal tie; the two must agree.
- spot checks: /ledger/1 confirmed (Insubres); /ledger/2 confirmed (Insubres); /ledger/4 confirmed (Insubres); /ledger/6 confirmed (Insubres)

## latin-league: fail

- [blocking]  `/keyframe_review`: Empty for a state Cliopatria lacks: the dossier has no shape. Evidence: research-brief s.6: for such states 'every keyframe is a new one'; check 4 cannot run; the author listed it as a gap. Fix: Add one keyframe per period (shape_id latin-league_<from>, from, to, verdict adjust, correction = found region minus later losses, source = the event's page); no new pages needed.
- [applied]  `/identity/type`: 'umbrella' for a land-holding people. Evidence: schema: umbrella is 'never coloured as territory'. Fix: state (done by the reviewer).
- [applied]  `/identity/family`: 'latin' is not a colours.json family. Evidence: schema: family must be a key of colours.json families. Fix: italy (done by the reviewer).
- thin `/identity/capitals/1`: Aricia as league centre is not on the Latin League page (confidence 1). Try: https://en.wikipedia.org/wiki/Aricia
- spot checks: /ledger/0 confirmed (Latin_League); /ledger/2 confirmed (Roman_expansion_in_Italy); /ledger/3 confirmed (Latin_League); /ledger/5 confirmed (Latin_War)

## lucanians: fail

- [blocking]  `/keyframe_review`: Empty for a state Cliopatria lacks: the dossier has no shape. Evidence: research-brief s.6: for such states 'every keyframe is a new one'; check 4 cannot run; the author listed it as a gap. Fix: Add one keyframe per period (shape_id lucanians_<from>, from, to, verdict adjust, correction = found region minus later losses, source = the event's page); no new pages needed.
- [applied]  `/identity/type`: 'umbrella' for a land-holding people. Evidence: schema: umbrella is 'never coloured as territory'. Fix: state (done by the reviewer).
- [applied]  `/identity/family`: 'italic' is not a colours.json family. Evidence: schema: family must be a key of colours.json families. Fix: italy (done by the reviewer).
-  `/ledger (new, c. -390 and -356)`: bruttii's found (-356, counterpart lucanians) has no mirror: the Lucanians never hold the Bruttian land. Evidence: lucanians /ledger/0 region is Basilicata only; bruttii predecessors note: 'The Lucanians probably gained dominance over the Bruttian peninsula' after 390 (Bruttii page). Fix: Add a gain c. -390 of the Bruttian peninsula (Cosenza province, confidence 1-2, Bruttii page) and a loss -356 to bruttii, or ask the bruttii author to make the found counterpart nobody.
-  `/ledger/4`: The Lucanians end at 272, but roman-republic holds them as a vassal 272-91 (/ledger/24, /ledger/129) and has no gain of Lucania. Evidence: Lucanians page: 'reduced to subjection in a ten-year campaign (272)', then 'espoused the cause of Hannibal (216)' and fought in the Social War (91-88). Fix: Agree with eu-03-b: either continue as a vassal to -91 (vassal_start -272) or have roman-republic record a gain -272.
-  `/ledger/0/counterpart`: 'Oenotrians, Chones and Lauternoi' has no dossier and is not in counterparts_needing_dossiers. Evidence: The Lucanians page names them only as peoples pushed into the interior. Fix: Use counterpart nobody, or list them for a dossier.
- thin `/identity/capitals/0`: Grumentum is not a Lucanian capital on the page (confidence 1, flagged). Try: https://en.wikipedia.org/wiki/Lucania
- spot checks: /ledger/0 confirmed (Lucanians); /ledger/1 confirmed (Lucanians); /ledger/3 confirmed (Pyrrhic_War); /ledger/4 confirmed (Lucanians)

## lusitanians: fail

- [blocking]  `/keyframe_review`: Empty for a state Cliopatria lacks: the dossier has no shape. Evidence: research-brief s.6: for such states 'every keyframe is a new one'; check 4 cannot run; the author listed it as a gap. Fix: Add one keyframe per period (shape_id lusitanians_<from>, from, to, verdict adjust, correction = found region minus later losses, source = the event's page); no new pages needed.
- [applied]  `/identity/type`: 'umbrella' for a land-holding people. Evidence: schema: umbrella is 'never coloured as territory'. Fix: state (done by the reviewer).
- [applied]  `/identity/family`: 'iberian' is not a colours.json family. Evidence: schema: family must be a key of colours.json families. Fix: iberia (done by the reviewer).
- [applied]  `/identity/wikipedia`: The article was 'Lusitanian War', the war, not the people. Evidence: The Lusitanians page exists: 'The Lusitanians were an Indo-European-speaking people living in the far west of the Iberian Peninsula'. Fix: wikipedia: Lusitanians (done by the reviewer); wikidata Q1133423 may be the war's item: check it.
-  `/ledger/0/region`: 'Lusitania' resolves to all of Portugal (and more), including the Alentejo and Algarve south of the Tagus and the Minho north of the Douro; the dossier's own text says 'north of the Tagus'. Evidence: Lusitanians page: they 'lived between the rivers Douro and Tagus, in most of today's Beira and Estremadura regions of central Portugal' and in 'some areas of the Extremadura region (Spain)'. Fix: Draw the land between the Douro and the Tagus plus Caceres (named districts/provinces), in found, loss and keyframes.
- thin `/ledger/1`: Conflict with Rome from 193 BC (Lusitanians page: they 'fought the Romans' from 193 BCE) is not in the ledger; the contest starts 155. Try: https://en.wikipedia.org/wiki/Lusitanians
- spot checks: /ledger/0 confirmed (Lusitanian_War); /ledger/1 confirmed (Lusitanian_War); /ledger/2 confirmed (Lusitanian_War)

## picentes: fail

- [blocking]  `/keyframe_review`: Empty for a state Cliopatria lacks: the dossier has no shape. Evidence: research-brief s.6: for such states 'every keyframe is a new one'; check 4 cannot run; the author listed it as a gap. Fix: Add one keyframe per period (shape_id picentes_<from>, from, to, verdict adjust, correction = found region minus later losses, source = the event's page); no new pages needed.
- [applied]  `/identity/type`: 'umbrella' for a land-holding people. Evidence: schema: umbrella is 'never coloured as territory'. Fix: state (done by the reviewer).
- [applied]  `/identity/family`: 'italic' is not a colours.json family. Evidence: schema: family must be a key of colours.json families. Fix: italy (done by the reviewer).
-  `/ledger/1`: The 390 loss to the Senones (Rimini, Pesaro e Urbino, Ancona) is land picentes never holds; umbri holds the same three provinces and loses them to the Senones in the same year (and senones' found names umbri). Evidence: picentes /ledger/0 region is Macerata, Fermo, Ascoli Piceno, Teramo; umbri /ledger/0 and /ledger/1; Picentes page: 'In 390 BC, the Senoni Gauls ... occupied Picenum north of the Esino river' and Picene land runs from the Foglia (so not Rimini). Fix: Make picentes and umbri agree: either picentes' found region takes Ancona province (south of the Foglia) and loses only the strip north of the Esino, with umbri giving it up, or drop this event. If kept, confidence 2 (the Picentes page dates it).
-  `/ledger (new, -299 and -268)`: The 299 treaty with Rome is missing. Evidence: Picentes page: 'When in 299 BC the Romans captured Nequinum, they also concluded a treaty with the Picentes'; roman-republic /ledger/13 vassal_start picentes -299 and /ledger/29 vassal_end -268. Fix: Add vassal_start -299 and vassal_end -268 (counterpart roman-republic, confidence 2).
-  `/identity/successors/1`: senones is listed as a successor, but it took a strip in 390, 122 years before the end. Evidence: picentes /ledger/1. Fix: Remove it from successors (the loss event carries the transfer).
- spot checks: /ledger/0 confirmed (Picentes); /ledger/1 confirmed (Picentes); /ledger/2 confirmed (Picentes); /ledger/3 confirmed (Picentes)

## sabines: fail

- [blocking]  `/keyframe_review`: Empty for a state Cliopatria lacks: the dossier has no shape. Evidence: research-brief s.6: for such states 'every keyframe is a new one'; check 4 cannot run; the author listed it as a gap. Fix: Add one keyframe per period (shape_id sabines_<from>, from, to, verdict adjust, correction = found region minus later losses, source = the event's page); no new pages needed.
- [applied]  `/identity/type`: 'umbrella' for a land-holding people. Evidence: schema: umbrella is 'never coloured as territory'. Fix: state (done by the reviewer).
- [applied]  `/identity/family`: 'italic' is not a colours.json family. Evidence: schema: family must be a key of colours.json families. Fix: italy (done by the reviewer).
-  `/ledger/1`: The 753 loss to roman-kingdom rests on legend and no page gives a land transfer; roman-kingdom has no mirror (its -753 found is from nobody). Evidence: Sabines page: 'the Sabine and Roman states merged' (Livy, legend, undated); Roman Kingdom page: joint kingdom with Titus Tatius, 'does not say that any Sabine land was added to Rome'. Fix: Remove the event (and the 15-km disc from the found region), or get roman-kingdom to agree.
-  `/ledger (new, c. -585)`: roman-kingdom /ledger/3 gains from sabines in 585 (Tarquinius Priscus); sabines has no mirror. Evidence: Roman expansion in Italy page: 'Tarquinius Priscus fought the Sabines (in about 585/584 BC)'. Fix: Add the mirror loss -585 (counterpart roman-kingdom, the same land as roman-kingdom's gain, confidence 2) or ask eu-03 to drop the gain.
- thin `/ledger/2`: The 504 Sabine war rests on the Roman-Etruscan Wars page (confidence 1; not opened by the reviewer). Try: https://en.wikipedia.org/wiki/Roman%E2%80%93Etruscan_Wars
- spot checks: /ledger/0 confirmed (Sabines); /ledger/1 not on page (Sabines); /ledger/3 confirmed (Roman_expansion_in_Italy); /ledger/4 confirmed (Sabines)

## samnites: fail

- [blocking]  `/keyframe_review`: Empty for a state Cliopatria lacks: the dossier has no shape. Evidence: research-brief s.6: for such states 'every keyframe is a new one'; check 4 cannot run; the author listed it as a gap. Fix: Add one keyframe per period (shape_id samnites_<from>, from, to, verdict adjust, correction = found region minus later losses, source = the event's page); no new pages needed.
- [applied]  `/identity/type`: 'umbrella' for a land-holding people. Evidence: schema: umbrella is 'never coloured as territory'. Fix: state (done by the reviewer).
- [applied]  `/identity/family`: 'italic' is not a colours.json family. Evidence: schema: family must be a key of colours.json families. Fix: italy (done by the reviewer).
- [applied]  `/ledger/10/note`: The note said 'The Samnites defeated Rome at Camerinum' (298). Evidence: Samnite Wars page places Camerinum in the 310 Etruscan campaign; it gives 298 as 'the year the Third Samnite War broke out'. Fix: Note corrected (done by the reviewer); the year and confidence 3 stand.
-  `/ledger/1, /ledger/4`: Campania gained from the Etruscans at -424 and lost to Rome at -338 includes Caserta, which the new capua dossier holds as an independent Campanian state -424..-343: the two dossiers claim the same land. Evidence: Capua page: 'In about 424 BC, Capua was captured by the Samnites' ... 'in 343 BC, it sought Roman help against its conquerors'; the -338 loss quotes Capua's own 'submission to Rome in 338 BC'. Fix: Draw samnites' Campania minus Caserta from -424 (or add a split -424 to capua), and make the -338 loss the rest of Campania with a page for it; ask eu-03 to make etruscans' -424 loss name capua for Caserta.
-  `/ledger/13`: Samnites end at 290, but roman-republic holds them as a vassal 290-91 (/ledger/17, /ledger/128). Evidence: Samnites page: 'the Samnites were subjugated in 290 BC' and 'would still side against the Romans' later. Fix: Agree with eu-03-b: continue to -91 as a vassal, or have roman-republic record a gain at -290.
- spot checks: /ledger/2 confirmed (Samnites); /ledger/5 confirmed (Samnite_Wars); /ledger/6 confirmed (Samnite_Wars); /ledger/7 confirmed (Samnite_Wars); /ledger/10 confirmed (Samnite_Wars); /ledger/11 confirmed (Samnite_Wars)

## senones: fail

- [blocking]  `/keyframe_review`: Empty for a state Cliopatria lacks: the dossier has no shape. Evidence: research-brief s.6: for such states 'every keyframe is a new one'; check 4 cannot run; the author listed it as a gap. Fix: Add one keyframe per period (shape_id senones_<from>, from, to, verdict adjust, correction = found region minus later losses, source = the event's page); no new pages needed.
- [applied]  `/identity/family`: 'gallic' is not a colours.json family. Evidence: schema: family must be a key of colours.json families. Fix: italy (done by the reviewer).
- thin `/ledger/0`: Start -390 (confidence 1): the page places the settlement only 'in the 4th century BC'. Try: https://en.wikipedia.org/wiki/Senones
- spot checks: /ledger/0 confirmed (Senones); /ledger/1 confirmed (Roman_expansion_in_Italy); /ledger/3 confirmed (Boii_(Cisalpine_Gaul)); /ledger/4 confirmed (Senones)

## sertorian-hispania: fail

- [blocking]  `/keyframe_review`: Empty for a state Cliopatria lacks: the dossier has no shape. Evidence: research-brief s.6: for such states 'every keyframe is a new one'; check 4 cannot run; the author listed it as a gap. Fix: Add one keyframe per period (shape_id sertorian-hispania_<from>, from, to, verdict adjust, correction = found region minus later losses, source = the event's page); no new pages needed.
- [applied]  `/ledger/3, /ledger/4`: Contest counterpart was the string "Pompey's army (Sullan government)". Evidence: Pompey commanded the Sullan government's army, i.e. roman-republic; the Sertorian War page: 'Sullan victory'. Fix: counterpart: roman-republic (done by the reviewer).
- spot checks: /ledger/0 confirmed (Sertorian_War); /ledger/2 confirmed (Sertorian_War); /ledger/3 confirmed (Sertorian_War); /ledger/5 confirmed (Sertorian_War)

## syracuse: fail

- [blocking]  `/keyframe_review`: Empty for a state Cliopatria lacks: the dossier has no shape. Evidence: research-brief s.6: for such states 'every keyframe is a new one'; check 4 cannot run; the author listed it as a gap. Fix: Add one keyframe per period (shape_id syracuse_<from>, from, to, verdict adjust, correction = found region minus later losses, source = the event's page); no new pages needed.
- [applied]  `/identity/family`: 'greek' is not a colours.json family. Evidence: schema: family must be a key of colours.json families. Fix: hellenistic (done by the reviewer).
-  `/ledger (new, -263 and -215)`: Hiero II's alliance with Rome is drawn only as a loss; the vassal tie is missing. Evidence: Hiero II page: 'in 263 he concluded a treaty with Rome, by which he was to rule over the south-east of Sicily'; Siege of Syracuse page: 'a close ally of Rome during the long reign of King Hiero II'; roman-republic /ledger/36 vassal_start syracuse -263 and /ledger/61 vassal_end -215. Fix: Add vassal_start -263 and vassal_end -215 (counterpart roman-republic, confidence 3).
-  `/ledger (new, -311)`: carthage /ledger/14 gains from syracuse in 311 (Himera River); no mirror. Evidence: Agathocles page: 'In 311 BC Agathocles was defeated in the Battle of the Himera River' and was besieged in Syracuse; it names no territorial loss. Fix: Add a loss -311 of the land carthage gains (confidence 2) or ask af-02 to soften carthage's gain.
-  `/ledger (new, -397/-392)`: The war 'Wars of Dionysius I with Carthage' (-397..-392) has no contest events; carthage has contest_start -398 and contest_end -393 with syracuse. Evidence: Dionysius I page: war with Carthage '397 BC to 392 BC with mixed success'. Fix: Add contest_start -397 and contest_end -392 with the war's zone.
- [applied]  `/ledger/11, /ledger/12`: Counterpart was the string 'Kingdom of Epirus (Pyrrhus)'. Evidence: kingdom-of-epirus.json exists (-370..-167). Fix: counterpart: kingdom-of-epirus (done by the reviewer); epirus has no matching occupation events (routed).
- thin `/ledger/0 to /ledger/1`: 733-405 is a 25-km disc, yet the Syracuse page says the colony 'subjugated nearby territories' and its rulers 'dominated much of Sicily' (Gelon, Hieron I); Himera 480 and the Athenian expedition are absent. Try: https://en.wikipedia.org/wiki/Gelon
- thin `/ledger/4`: What happened to the Italian and Adriatic holdings after 367 (confidence 1). Try: https://en.wikipedia.org/wiki/Dionysius_II_of_Syracuse
- thin `/ledger/10`: The 289 loss to Carthage (confidence 1): the Pyrrhic War page says Carthage was 'expanding eastward in Sicily following the death of Agathocles' in 289. Try: https://en.wikipedia.org/wiki/Hicetas
- spot checks: /ledger/0 confirmed (Syracuse,_Sicily); /ledger/2 confirmed (Dionysius_I_of_Syracuse); /ledger/5 confirmed (Agathocles_of_Syracuse); /ledger/8 confirmed (Agathocles_of_Syracuse); /ledger/9 confirmed (Agathocles_of_Syracuse); /ledger/16 confirmed (Hiero_II_of_Syracuse); /ledger/18 confirmed (Siege_of_Syracuse_(213%E2%80%93212_BC)); /ledger/19 confirmed (Siege_of_Syracuse_(213%E2%80%93212_BC))

## umbri: fail

- [blocking]  `/keyframe_review`: Empty for a state Cliopatria lacks: the dossier has no shape. Evidence: research-brief s.6: for such states 'every keyframe is a new one'; check 4 cannot run; the author listed it as a gap. Fix: Add one keyframe per period (shape_id umbri_<from>, from, to, verdict adjust, correction = found region minus later losses, source = the event's page); no new pages needed.
- [applied]  `/identity/type`: 'umbrella' for a land-holding people. Evidence: schema: umbrella is 'never coloured as territory'. Fix: state (done by the reviewer).
- [applied]  `/identity/family`: 'italic' is not a colours.json family. Evidence: schema: family must be a key of colours.json families. Fix: italy (done by the reviewer).
-  `/ledger/5`: The Umbri end at c. 260, but roman-republic holds them as a vassal 260-90 (/ledger/38, /ledger/135) and records no gain of Umbria. Evidence: Umbri page: 'completed their conquest of Umbria by approximately 260 BC'; 'granted citizenship in 90 BC'. Fix: Agree with eu-03-b: either roman-republic gains Umbria at -260, or umbri continues as a vassal to -90.
-  `/ledger/0/region`: Shares Rimini, Pesaro e Urbino and Ancona with picentes' 390 loss (see picentes). Evidence: Senones page: 'displacing the Umbrians'; Picentes page: the Senones 'occupied Picenum north of the Esino'. Fix: Agree the split with picentes (umbri keeps Rimini and Pesaro north of the Foglia; Ancona south of the Esino is Picene).
- thin `/identity/capitals/0`: Iguvium is not named as a capital on the page (confidence 1, flagged). Try: https://en.wikipedia.org/wiki/Iguvine_Tablets
- spot checks: /ledger/1 confirmed (Senones); /ledger/2 confirmed (Umbri); /ledger/3 confirmed (Picentes); /ledger/5 confirmed (Umbri)

## volsci: fail

- [blocking]  `/keyframe_review`: Empty for a state Cliopatria lacks: the dossier has no shape. Evidence: research-brief s.6: for such states 'every keyframe is a new one'; check 4 cannot run; the author listed it as a gap. Fix: Add one keyframe per period (shape_id volsci_<from>, from, to, verdict adjust, correction = found region minus later losses, source = the event's page); no new pages needed.
- [applied]  `/identity/type`: 'umbrella' for a land-holding people. Evidence: schema: umbrella is 'never coloured as territory'. Fix: state (done by the reviewer).
- [applied]  `/identity/family`: 'italic' is not a colours.json family. Evidence: schema: family must be a key of colours.json families. Fix: italy (done by the reviewer).
-  `/wars/0/belligerents`: The Roman-Volscian wars (-534..-304) list roman-republic, which begins in -509, for the regal years. Evidence: Roman Kingdom page: Tarquinius Superbus (534-509) 'waged a number of wars against Rome's neighbours, including against the Volsci'. Fix: Add roman-kingdom to the belligerents (or start the republican war at -509).
-  `/ledger/4`: The 304 loss has no mirror in roman-republic (which gains from samnites and aequi in 304, not volsci). Evidence: Volsci page: 'their territories were taken over by and assimilated into the growing republic by 304 BC'. Fix: Ask eu-03-b to add a -304 gain from volsci (routed).
- thin `/identity/capitals/1`: Privernum is a placeholder (not on the Volsci page; the page names Antium as the Antiates' capital). Try: https://en.wikipedia.org/wiki/Privernum
- spot checks: /ledger/0 confirmed (Roman_Kingdom); /ledger/1 confirmed (Volsci); /ledger/3 confirmed (Roman_expansion_in_Italy); /ledger/4 confirmed (Volsci)

## Cross-dossier matrix (unmatched only)

- arverni -200 vassal_start -> Vellavii, Gabali, Cadurci and Eleuteti (Arvernian clients): exception. listed in the author's counterparts_needing_dossiers.
- arverni -52 vassal_end -> Vellavii, Gabali, Cadurci and Eleuteti (Arvernian clients): exception. listed in the author's counterparts_needing_dossiers.
- arverni -52 loss -> roman-republic: mismatch. roman-republic names the string 'Gallic tribes (Helvetii, Suebi, Belgae, Veneti, Arverni)'; eu-03-b should name arverni (and aedui, sequani) at -52.
- allobroges -121 loss -> roman-republic: mismatch. roman-republic names the string 'Arverni and Allobroges'; eu-03-b should name allobroges (arverni lose no land in 121).
- ligures -177 loss -> roman-republic: missing. roman-republic has contest -238..-155 with Ligures but no gain of Luna/Lucca; route to eu-03-b.
- ligures -155 loss -> roman-republic: missing. roman-republic has no -155 gain from ligures (author flagged); route to eu-03-b.
- bruttii -356 found -> lucanians: missing. lucanians never holds the Bruttian land and has no -356 loss/split; fix in lucanians (see its findings) or make the found counterpart nobody.
- bruttii -340 gain -> greek-city-states: missing. greek-city-states (eu-01) has no loss of Hipponium/Terina/Thurii c. 340; bruttii's event is confidence 1; route to eu-01.
- bruttii -332 loss -> kingdom-of-epirus: mismatch. epirus gains in 334 from the string 'Bruttii'; the Alexander I page puts the taking of Terina after the 332 treaty, so bruttii's -332 is right; eu-02 should move its gain to -332 and name bruttii.
- bruttii -331 gain -> kingdom-of-epirus: mismatch. epirus loses to lucanians in 331; bruttii's return of Terina is a confidence-1 bridge; eu-02 could add bruttii as counterpart for Terina.
- bruttii -215 gain -> roman-republic: missing. roman-republic has no -215 loss of Consentia; route to eu-03-b.
- bruttii -203 loss -> roman-republic: mismatch. roman-republic gains Bruttium in 203 from carthage (author flagged); eu-03-b should name bruttii.
- helvetii -58 loss -> roman-republic: mismatch. roman-republic names the string 'Gallic tribes (Helvetii, ...)'; eu-03-b should name helvetii.
- aedui -100 vassal_start -> Segusiavi and Mandubii (Aeduan clients): exception. listed in the author's counterparts_needing_dossiers.
- aedui -52 vassal_end -> Segusiavi and Mandubii (Aeduan clients): exception. listed in the author's counterparts_needing_dossiers.
- aedui -52 loss -> roman-republic: mismatch. string counterpart 'Gallic tribes (...)' in roman-republic; eu-03-b should name aedui.
- sequani -70 loss -> Ariovistus (Germanic settlers): exception. listed in the author's counterparts_needing_dossiers.
- sequani -52 loss -> roman-republic: mismatch. string counterpart 'Gallic tribes (...)' in roman-republic; eu-03-b should name sequani.
- messapii -267 loss -> roman-republic: mismatch. roman-republic names the string 'Messapii and Sallentini'; eu-03-b should name messapii.
- messapii -266 loss -> roman-republic: mismatch. roman-republic names the string 'Messapii and Sallentini'; eu-03-b should name messapii.
- kingdom-of-noricum -16 loss -> roman-empire: exception. roman-empire (group eu-04) has not been written yet.
- capua -424 found -> etruscans: mismatch. etruscans loses Capua to samnites, not capua; samnites gains all Campania incl. Caserta; see samnites findings (overlap -424..-343).
- capua -343 loss -> roman-republic: missing. roman-republic has no -343 gain (or vassal tie) for Capua (author flagged); route to eu-03-b.
- capua -216 gain -> roman-republic: mismatch. roman-republic loses Capua and the south to carthage in 216; eu-03-b should name capua for Caserta.
- capua -211 loss -> roman-republic: mismatch. roman-republic retakes Capua from carthage in 211; eu-03-b should name capua.
- cantabri -19 loss -> roman-empire: exception. roman-empire (group eu-04) has not been written yet.
- cenomani -218 loss -> roman-republic: missing. roman-republic has no gain of Cremona from cenomani (its -218 gain is from carthage); route to eu-03-b.
- cenomani -89 loss -> roman-republic: mismatch. roman-republic -89 gain from nobody (lex Pompeia); eu-03-b could name cenomani, or record vassal_start -225/vassal_end -89.
- adriatic-veneti -181 loss -> roman-republic: missing. roman-republic has no -181 gain; and Aquileia lies outside the Veneti's shape (see adriatic-veneti findings): drop rather than mirror.
- lucanians -450 found -> Oenotrians, Chones and Lauternoi (indigenous peoples of Oenotria): missing. counterpart is a free string with no dossier and is not listed for one; use nobody or list it.
- lucanians -272 loss -> roman-republic: mismatch. roman-republic treats Lucania as a vassal 272-91, not a gain; the two must agree (see lucanians findings).
- picentes -390 loss -> senones: mismatch. senones' found names umbri; umbri loses the same provinces in 390; picentes never held them (see picentes findings).
- sabines -753 loss -> roman-kingdom: missing. roman-kingdom -753 is a found from nobody; the event is legend, confidence 1: drop it.
- samnites -338 loss -> roman-republic: missing. roman-republic has no -338 gain of Campania from samnites; and Caserta belongs to capua then (see samnites findings).
- samnites -291 loss -> roman-republic: missing. roman-republic has no -291 gain of Venusia; route to eu-03-b.
- syracuse -289 loss -> carthage: missing. carthage (af-02) has no -289 gain from syracuse; syracuse's event is confidence 1; route to af-02.
- syracuse -278 occupation_start -> kingdom-of-epirus: missing. kingdom-of-epirus (eu-02) has no occupation of Syracuse 278-276 (it has a -277 gain of Eryx from carthage); route to eu-02 (counterpart slug fixed by the reviewer).
- syracuse -276 occupation_end -> kingdom-of-epirus: missing. as above; route to eu-02.
- syracuse -263 loss -> roman-republic: mismatch. roman-republic records a vassal_start of syracuse, not a gain; syracuse should add the vassal tie (see findings) and eu-03-b a gain for the land outside Hiero's kingdom.
- umbri -260 loss -> roman-republic: mismatch. roman-republic treats Umbria as a vassal 260-90; the two must agree.
- volsci -304 loss -> roman-republic: missing. roman-republic gains from samnites and aequi in 304, not volsci; route to eu-03-b.
- roman-republic -299 vassal_start -> picentes: missing. picentes lacks vassal_start -299 (see picentes)
- roman-republic -290 vassal_start -> samnites: missing. samnites dissolves at -290 instead (see samnites)
- roman-republic -272 vassal_start -> lucanians: missing. lucanians dissolves at -272 instead (see lucanians); the note also names the Bruttians
- roman-republic -263 vassal_start -> syracuse: missing. syracuse lacks the vassal tie (see syracuse)
- roman-republic -260 vassal_start -> umbri: missing. umbri dissolves at -260 instead
- roman-republic -238 vassal_start -> adriatic-veneti: missing. adriatic-veneti lacks vassal_start -238 (see adriatic-veneti)
- roman-republic -225 vassal_start -> boii: missing. boii lacks vassal_start -225 (see boii)
- roman-republic -218 loss -> boii: missing. boii has no -218 gain
- roman-republic -197 vassal_start -> insubres: missing. insubres dissolves at -197 instead (see insubres)
- roman-kingdom -585 gain -> sabines: missing. sabines has no -585 loss (see sabines)
- etruscans -396 loss -> insubres: missing. insubres' found is -400 from nobody
- etruscans -396 loss -> adriatic-veneti: missing. adriatic-veneti has no -396 gain (Adria); route to eu-03 (etruscans) or add a gain
- carthage -311 gain -> syracuse: missing. syracuse has no -311 loss (see syracuse)
- kingdom-of-epirus -334 gain -> lucanians: missing. lucanians has no -334 loss to epirus (Heraclea)
