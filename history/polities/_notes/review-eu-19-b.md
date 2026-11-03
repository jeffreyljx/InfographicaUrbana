# Review of batch eu-19-b (Caucasus, part b)

Reviewer run of 2026-11-01 (brief filled 2026-10-31). Dossiers: caucasian-albania, caucasian-iberia, lazica, georgia, balasagan. Validator: 0 errors on all five (warnings: albania war before the life; lazica/georgia 'no verdict' for Georgia-row shapes reviewed in sibling dossiers, which I confirmed: georgia_567 in lazica, georgia_638 in georgia (wrong), georgia_724..980 in kingdom-of-abkhazia).

Spot checks: 19 recorded (Iberia /ledger/2 and georgia /ledger/12, 15-17 also read and confirmed) on 11 pages (Caucasian Albania, Kingdom of Iberia, Iberian War, Lazica, Lazic War, Polemon II of Pontus, Democratic Republic of Georgia, Georgia (country), War in Abkhazia (1992-1993), Russo-Georgian War, Balasagan). Every event checked says on the page what its note claims, with the year. No fabricated or mis-dated event found.

Reviewer edit: georgia /ledger/4/counterpart 'United Kingdom (British occupation force)' -> 'united-kingdom' (dossier exists); re-validated, read back.

## caucasian-albania: thin
Area: No infobox area; text gives 23,000 km2 before 387 and about 45,000 km2 after (Cliopatria 74,782: ratio 1.66). Factor 2.18 acknowledged in keyframe_review/0 but not resolved.
Spot checks: /ledger/1 confirmed; /ledger/4 confirmed; /ledger/5 confirmed; /ledger/6 confirmed
Findings:
- `/wars/0` (open): Pompey's campaign (-66..-65) lies before the state's start (-63), so the war is outside the life (validator warning, flagged by the author but not resolved). Evidence: Caucasian Albania page: Albania 'first appears in history as a vassal state in the empire of Tigranes the Great (95-56 BC)' and Lucullus/Pompey reach it in 69-65 BC; the start -63 is only Cliopatria's first shape (ledger/0 confidence 1). Fix: Either move identity.start and the found event back to at least -66 with a new keyframe caucasian-albania_-66 (-66..-64, the Cliopatria -63 outline minus Karabakh), or drop /wars/0 (the campaign is already in caucasian-iberia /wars/0 and the Roman dossiers).
- `/ledger/2` (open): The 387 eastern lowlands (Mil/Mughan/Paytakaran, Caspian coast) are gained from 'nobody' at confidence 1, but this land was not stateless: Paytakaran was an Armenian province until 387 and the page bounds Albania 'by the Caspian Sea to the east' from the start. Evidence: kingdom-of-armenia /ledger/39 drops its eastern strip in 387 to sasanian-empire; ledger/0 text of this dossier says Albania was bounded by the Caspian before 387 while keyframes -63..386 stop at 48.4E, short of the coast. Fix: Open the Paytakaran (or Partition of Armenia) page; name kingdom-of-armenia or sasanian-empire as counterpart for Paytakaran, and either mark the pre-387 keyframes adjust to reach the Caspian coast or say why not.
- `/ledger/1` (open): The 387 gain of Karabakh from kingdom-of-armenia has no mirror: the Armenian dossier loses its 387 land to roman-empire and sasanian-empire only. Evidence: kingdom-of-armenia /ledger/38-39 (387 losses to roman-empire and sasanian-empire, the eastern strip c1); Caucasian Albania page: 'Albania with Sassanid help was able to seize from Armenia all the right bank of the river Kura up to river Araxes'. Fix: Route to kingdom-of-armenia (eu-19): add a 387 loss of Artsakh/Utik (region Karabakh) with counterpart caucasian-albania, or re-point /ledger/39. No change needed here.
For a gap-filler:
- `/keyframe_review/0`: Area 2.18x the page's 'approximately 23,000 km2' for the original territory (Cliopatria 50,113; about 46,500 after the Karabakh cut); acknowledged in the note but left unresolved. Try https://en.wikipedia.org/wiki/Caucasian_Albania
- `/ledger/0`: Start year -63 is Cliopatria's (confidence 1); the page has the kingdom as Tigranes' vassal 95-56 BC and fighting Pompey 66-65 BC. Try https://en.wikipedia.org/wiki/Pompey%27s_Georgian_campaign
- `/ledger/2`: 387 eastern gain (94 cells, Mil/Mughan/Paytakaran) at confidence 1 from 'nobody'. Try https://en.wikipedia.org/wiki/Paytakaran
- `/ledger/3`: Capital move Qabala to Partaw dated 387 at confidence 1; the page says both 'after the partition' and 'In the 5th century'. Try https://en.wikipedia.org/wiki/Barda,_Azerbaijan

## caucasian-iberia: thin
Area: Kingdom of Iberia infobox gives no area; author says so in keyframe notes.
Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/3 confirmed; /ledger/4 confirmed
Findings:
- `/keyframe_review/0` (open): The new keyframe -302..-64 is the Kartli core (about 19,000 km2 by the gazetteer) and the next keyframe (-63) is Cliopatria's 35,868 km2, but no ledger event explains the near doubling (Kakheti, Javakheti, the upper Kura). Evidence: Gazetteer 'Kartli' = Shida Kartli + Kvemo Kartli + Tbilisi + Mtskheta-Mtianeti; shapes.csv caucasian-iberia_-63 = 35,868 km2; ledger has no event between -302 and 482. Fix: Add a confidence-1 gain at -63 (counterpart nobody or kingdom-of-armenia, 'bridged to Cliopatria') naming the added land, or describe the -302 keyframe as the Cliopatria -63 outline with an approximate note.
For a gap-filler:
- `/keyframe_review/0`: Extent of Iberia -302..-64 and the 2nd-century BC conquests from or losses to Armenia (Gogarene), none dated; 2 of 5 budget pages unused. Try https://en.wikipedia.org/wiki/Pharnavaz_I_of_Iberia
- `/ledger/5`: Dissolve 533 at confidence 1 (Cliopatria's year); the page abolishes the monarchy in 580 and gives 'Direct Sassanid Persian rule' 523-580. Try https://en.wikipedia.org/wiki/Bakur_III_of_Iberia

## lazica: thin
Area: Lazica infobox (131-697, capital Archaeopolis) gives no area.
Spot checks: /ledger/1 confirmed; /ledger/3 confirmed; /ledger/5 confirmed; /ledger/6 confirmed
Findings:
- `/identity` (open): lazica and kingdom-of-lazica share Wikidata Q136884 and the author finds them one state, yet keeps two dossiers with a bookkeeping dissolve 637 / found 638, against the brief's rule (one dossier under the earlier slug with both Names). Evidence: Author's brief section 6 rule on shared Wikidata ids; lazica /ledger/7 (637 dissolve, confidence 1) and kingdom-of-lazica /ledger/0 (638 found, confidence 1); Lazica page infobox 131-697. Fix: Orchestrator decision: merge kingdom-of-lazica into lazica (cliopatria_names Lazica, Georgia, Kingdom of Lazica; end 697 or 777) or accept the split and record why in notes.
- `/ledger/1` (open): Lazica holds the Colchian coast -63..62 while kingdom-of-pontus gains Colchis from 'nobody' in -31 and holds it to 62; the two dossiers overlap for 93 years and the 62 loss here is to roman-empire while roman-empire gains from kingdom-of-pontus. Evidence: Polemon II of Pontus page: Polemon II 'succeeded his mother as the sole ruler of Pontus, Colchis and Cilicia' (38) and 'In 62 ... Pontus, including Colchis, became a Roman province'; kingdom-of-pontus /ledger/51 (-31 gain cp nobody) and /ledger/52 (62 dissolve to roman-empire); roman-empire /ledger/45. Fix: Agree the owner of Colchis -31..62 with me-05: either a lazica loss/vassal to kingdom-of-pontus at -31 (and the 62 loss counterpart kingdom-of-pontus/roman-empire to match), or kingdom-of-pontus records Colchis as a vassal or names lazica as counterpart.
For a gap-filler:
- `/ledger/0`: Start -63 is Cliopatria's (confidence 1); the page gives 'from about the 1st century BC' and 131 (Arrian). Try https://en.wikipedia.org/wiki/Colchis
- `/ledger/2`: 306 gain of about 6,400 km2 from roman-empire at confidence 1 with no Roman mirror; no page dates it. Try https://en.wikipedia.org/wiki/Abasgia
- `/keyframe_review/10`: 546-566 bridged at confidence 1: Persian-held places in the Lazic War (Petra 541-551, Archaeopolis, Uthimereos, Souania) undated. Try https://en.wikipedia.org/wiki/Siege_of_Petra_(550%E2%80%93551)
- `/ledger/7`: 637 hand-over at confidence 1 to kingdom-of-lazica; 577-637 bridged. Try https://en.wikipedia.org/wiki/Lazica

## georgia: fix
Area: Georgia (country) infobox 69,700 km2 (Geography 67,900); DRG infobox 75,110 km2 (1918) vs 70,484 (0.94) and 107,600 km2 (1919) vs 72,873 (0.68), all inside a factor of two and quoted correctly by the author.
Spot checks: /ledger/0 confirmed; /ledger/4 confirmed; /ledger/10 confirmed; /ledger/14 confirmed; /ledger/18 confirmed
Findings:
- `/ledger/4/counterpart` (applied): Counterpart was the free name 'United Kingdom (British occupation force)' although a united-kingdom dossier exists. Evidence: history/polities/united-kingdom.json (1801-2024); DRG page: 'British-held Batumi remained out of Georgia's control until 1920' and 'Batum was finally incorporated into the republic after the British evacuated the area in 1920'. Fix: Set counterpart to 'united-kingdom' (done; re-validated, 0 errors). The united-kingdom dossier still needs the matching Batum record (see cross_checks).
- `/ledger/5/region` (open): The December 1920 Lori neutral-zone gain uses the whole admin1 Lori (about 3,800 km2, Vanadzor included) while keyframe georgia_1920 is 'ok' and holds only 2 of Lori's 15 cells; region and keyframe disagree. Evidence: keyframe_review/3 note: 'two Lori cells are in'; DRG page: the neutral zone was 'reoccupied by Georgia after the fall of the Armenian Republic at the end of 1920'. Fix: Draw the neutral zone narrowly (a disk of about 20 km on Alaverdi, 44.66E 41.10N, or the Borchalo/Lori uchastok if the gazetteer gains it) and mark georgia_1920 adjust for Dec 1920-Mar 1921, or lower the gain to the 2 Cliopatria cells. Non-blocking.
- `/ledger/9` (open): The South Ossetia contest_start is year-only 1991 and sorts before the 1991.4 re-founding, so the war starts while the state has no land (the fighting began on 5 January 1991 under the Georgian SSR). Evidence: republic-of-south-ossetia /ledger/1 (5 January 1991); this dossier /ledger/10 (gain 9 April 1991). Fix: Give the contest month 4 and place it after /ledger/10 (the war carried into the new state), and ask georgian-soviet-socialist-republic to hold the January-April 1991 part. Non-blocking.
For a gap-filler:
- `/ledger/2`: 1919 gain of Akhaltsikhe/Akhalkalaki from ottoman-empire at confidence 1 (undated on the DRG page); Artvin, Ardahan, Zaqatala, Sochi and the 1921 cessions undrawn. Try https://en.wikipedia.org/wiki/Treaty_of_Kars
- `/keyframe_review/1`: Treaty of Batum (4 June 1918) cessions to the Ottomans not opened; Adjara alone is removed for 1918-1919. Try https://en.wikipedia.org/wiki/Treaty_of_Batum

## balasagan: thin
Area: No area on the page; Cliopatria's 638 shape is the Albania 509 outline; author trims it to a 90 km disk on the Mughan (about 11,000 km2) and says why.
Spot checks: /ledger/1 confirmed; /keyframe_review/0 confirmed
Findings:
- `/ledger/0` (open): Balasagan is founded in 638 out of sasanian-empire, but sasanian-empire records no loss or split of the Mughan in 638 and holds Albania to 644, so the two dossiers overlap on the Mughan 638-644. Evidence: sasanian-empire /ledger/61 (510 gain of Albania) and no later Albanian loss until rashidun-caliphate /ledger/38 (644 gain of 'almost the whole of the South Caucasus' cp sasanian-empire); Balasagan page: 'Nothing is known about the Kingdom of Balasagan'. Fix: Orchestrator decision: drop balasagan (author's suggestion), or have sasanian-empire (me-06) record a 638 loss/split of the Mughan plain to balasagan and rashidun-caliphate name balasagan for the c. 645 conquest.
For a gap-filler:
- `/ledger/0`: Found 638 at confidence 1 (Cliopatria's year); the page attests the province from Shapur I (240-270) and gives no event in 638. Try https://en.wikipedia.org/wiki/Balasagan
- `/identity/capitals`: No capital given; the page says the 'main hub may have been at the fortress of Khursan' (no coordinates). Try https://en.wikipedia.org/wiki/Balasagan

## Cross-dossier matrix
- caucasian-albania 387 gain cp=kingdom-of-armenia -> kingdom-of-armenia 387 loss: mismatch. Armenia's 387 losses (ledger/38-39) name roman-empire and sasanian-empire (eastern strip, c1), not caucasian-albania; route to eu-19 kingdom-of-armenia.
- caucasian-albania 387 gain cp=nobody -> -  : exception. Counterpart 'nobody' at c1 for the Mil/Mughan/Paytakaran lowlands; dubious (Paytakaran was Armenian until 387); see albania fixes.
- caucasian-albania 510 dissolve cp=sasanian-empire -> sasanian-empire 510 gain: matched. sasanian-empire ledger/61.
- caucasian-iberia 533 dissolve cp=sasanian-empire -> sasanian-empire 534 gain: matched. sasanian-empire ledger/66; one year apart.
- caucasian-iberia 482 contest_start cp=sasanian-empire -> sasanian-empire  : missing. sasanian-empire has no contest with caucasian-iberia for 482-502 or 523-532 (only vassal_end 524 and contest with eastern-roman-empire 526-532); not a required mirror, routed to me-06 for information.
- lazica 62 loss cp=roman-empire -> roman-empire 62 gain: mismatch. roman-empire ledger/45 gains 'Pontus, including Colchis' from kingdom-of-pontus; flagged by author.
- lazica 306 gain cp=roman-empire -> roman-empire  : missing. No roman-empire loss 300-310; lazica event is c1 bridged.
- lazica 528 occupation_start cp=sasanian-empire -> sasanian-empire  : missing. Owner-side record; sasanian-empire has no occupation_start cp lazica (Shorapani and Skanda, 528-532); route to me-06.
- lazica 532 occupation_end cp=sasanian-empire -> sasanian-empire  : missing. As above.
- lazica 637 dissolve cp=kingdom-of-lazica -> kingdom-of-lazica 638 found: matched. Same state per both dossiers; merge pending orchestrator.
- kingdom-of-pontus -31 gain cp=nobody -> lazica  : mismatch. Pontus holds Colchis -31..62 (Polemon I/II) while lazica holds the Colchian coast -63..62: overlap; route to me-05 and eu-19-b.
- georgia 1918 found cp=transcaucasian-democratic-federative-republic -> -  : exception. No dossier yet; listed by author in counterparts_needing_dossiers (eu-19-x).
- georgia 1919 gain cp=ottoman-empire -> ottoman-empire  : missing. ottoman-empire has 1918 gain from russian-republic and 1919.4 loss of Kars to armenia, no loss to georgia; route to me-10.
- georgia 1920 gain cp=united-kingdom -> united-kingdom  : missing. Counterpart re-typed by reviewer to the existing slug; united-kingdom has no Batum occupation/loss 1918-1920; route to its group.
- georgia 1920 gain cp=armenia -> armenia  : missing. armenia dissolves 1920.12 to armenian-soviet-socialist-republic with no loss of the Lori neutral zone to georgia; route to eu-19 armenia.
- georgia 1918 contest_start cp=armenia -> armenia 1918 contest_start: mismatch. armenia ledger/5-6 name the counterpart 'Democratic Republic of Georgia' (should be slug georgia) and end the contest 1918.12; georgia ends it 1919.1.
- georgia 1921 loss cp=georgian-soviet-socialist-republic -> georgian-soviet-socialist-republic 1921 gain: matched. GSSR ledger/0 (1921.2 found cp georgia) and ledger/1 (1921.3 gain).
- republics-of-the-soviet-union 1921 gain cp=georgia -> georgia 1921 loss: mismatch. RSU ledger/9 gains from georgia in 1921.2; georgia's loss names georgian-soviet-socialist-republic (1921.3); route to eu-17.
- georgian-soviet-socialist-republic 1921 gain cp=georgia -> georgia  : missing. GSSR ledger/2 c1 gain of the Artvin Okrug from georgia; georgia draws no Artvin; flagged by author.
- georgia 1991 gain cp=georgian-soviet-socialist-republic -> georgian-soviet-socialist-republic 1991 dissolve: matched. GSSR ledger/7 dissolve 1991.4 has no counterpart; suggest 'georgia'.
- georgia 1993 loss cp=republic-of-abkhazia -> republic-of-abkhazia 1993 gain: matched. republic-of-abkhazia ledger/2 (1993.9). Contest end differs: 1993.9 here, 1994 there (within a year).
- georgia 2008 occupation_start cp=russian-federation -> -  : exception. russian-federation (eu-22) has not run yet.
- georgia 2008 loss cp=republic-of-abkhazia -> republic-of-abkhazia 2008 gain: matched. Upper Kodori; republic-of-abkhazia ledger/4.
- georgia 2008 loss cp=republic-of-south-ossetia -> republic-of-south-ossetia 2008 gain: matched. Akhalgori; republic-of-south-ossetia ledger/3.
- balasagan 638 found cp=sasanian-empire -> sasanian-empire  : mismatch. No sasanian loss/split in 638; sasanian holds Albania incl. the Mughan to 644: overlap.
- balasagan 645 dissolve cp=rashidun-caliphate -> rashidun-caliphate 644 gain: mismatch. rashidun-caliphate ledger/38 gains the South Caucasus from sasanian-empire in 644, not from balasagan.

## Problems
- lazica and kingdom-of-lazica (eu-19-c) are one state (Q136884) by both authors; merge needs an orchestrator decision across batches.
- georgia is one dossier for 1918-1921 and 1991-2024 (consistent with the georgian-soviet-socialist-republic dossier); orchestrator may split.
- balasagan: Cliopatria's row reuses the Albania outline and the page says nothing is known of the kingdom; orchestrator may drop it (overlaps sasanian-empire 638-644).
- Reviewer edit: georgia /ledger/4/counterpart set to 'united-kingdom'; file re-validated (0 errors) and read back.
- WebFetch returns summaries; quotes were requested verbatim and matched the authors' notes. No page failed to load for the reviewer.
