# Review of batch me-05-e (2026-10-19)

Adversarial review of greco-bactrian-kingdom, kingdom-of-cappadocia, ankhwennefer and nabataeans. All four validate with --resolve (0 errors, 0 warnings). Spot checks were made through WebFetch (a model's reading of the page). The reviewer made one edit: greco-bactrian-kingdom /ledger/5-7, counterpart maurya-empire changed to nobody (re-validated).

Verdicts: greco-bactrian-kingdom **thin**, kingdom-of-cappadocia **fail**, ankhwennefer **thin**, nabataeans **fail**.

## greco-bactrian-kingdom: thin

Area: infobox 2500000 km2 (-184), Cliopatria 685135 km2, ratio 0.27; Keyframe -203 note gives the ratio and adds the Indian conquests in a new keyframe -180 (about 0.98 M km2); the infobox figure is read as a maximum.

Findings:
- `/ledger/5, /ledger/6, /ledger/7 (counterpart)` (APPLIED by reviewer): The c. 190-175 invasion of north-west India and the 180 gain named maurya-empire as counterpart, a state that had ended in 185 and did not hold that land. Evidence: Greco-Bactrian Kingdom page: the invasion came 'a few years after the Mauryan empire had been overthrown by the Shunga dynasty'; maurya-empire dossier ends -185 (L15 dissolve to shunga-empire) and loses the outer empire, the north-west included, to nobody in -225 (L13); Cliopatria's Maurya shapes from -225 start at 77.1 E, east of the Punjab. Fix: Counterpart set to 'nobody' on all three events (contest pair kept consistent); a reviewer sentence added to the /ledger/6 note. Re-validated: 0 errors, 0 warnings.
- `/keyframe_review/7 and /ledger/11`: Non-blocking: keyframe -164 is 'ok' and drops Margiana and Aria (740 cells, west and east, -170k km2) in 164, but the ledger loses them only in -158; the eastern part of the drop has no event. Evidence: Eucratides I page: 'Having taken Tapuria and Margiana from Demetrius in about 170 BC' and 'From 162-158 BCE, Eucratides lost the satrapies of Aria and Margiana to Mithridates I of Parthia'; shapes.csv -170 1,364,110 km2 -> -164 1,194,248 km2. Fix: Either mark keyframe -164 adjust (union of the -164 shape with Margiana and Aria, years -164..-158) or record Margiana's loss at c. 170 as a loss (the page says 'taken', not contested) and Aria in 162-158; name what goes in the east.
- `/ledger/13`: Non-blocking cross-dossier mismatch: the -144 loss of Sogdia and Fergana goes to yuezhi, but the yuezhi dossier gains Sogdia only in -130 (L7) and the indo-scythians dossier founds in -144 with greco-bactrian-kingdom as counterpart, quoting the same 'Around 140 BC, eastern Scythians (the Saka...)' sentence this note quotes. Evidence: yuezhi L7 -130 gain (Yuezhi page); indo-scythians L0 -144 found, counterpart greco-bactrian-kingdom; Heliocles I page table: 'Yuezhi occupation, loss of Ai-Khanoum' 155-130 BCE. Fix: Reconcile with ia-01 (yuezhi) and sa-02 (indo-scythians): split the -144 loss between indo-scythians (the Amu Darya strip) and whoever the yuezhi dossier says held Sogdia 144-131, or move it to -130.

Gaps for a gap-filler:
- `/ledger/4`: Confidence 1: when Euthydemus took Sogdia and Fergana (203 is Cliopatria's year). Try https://en.wikipedia.org/wiki/Sogdia
- `/ledger/9`: Confidence 1: Eucratides' Indian conquests (+373k km2 in 170 beyond the 180 lands) and which Indo-Greek kings lost them. Try https://en.wikipedia.org/wiki/Indo-Greek_Kingdom
- `/ledger/13`: Confidence 1: the 144 loss of Sogdia/Fergana and its taker (Saka or Yuezhi); the Heliocles table dates a Yuezhi occupation and the loss of Ai-Khanoum to 155-130. Try https://en.wikipedia.org/wiki/Ai-Khanoum
- `/ledger/15`: Confidence 1: year of Heliocles' move to the Kabul valley (the main page states the move, undated). Try https://en.wikipedia.org/wiki/Heliocles_I
- `/ledger/16`: Confidence 1: the end (infobox c. 120, Cliopatria 127) and the hand-over of the land south of the Hindu Kush to the Indo-Greeks. Try https://en.wikipedia.org/wiki/Indo-Greek_Kingdom
- `/keyframe_review/7`: Which year Margiana and Aria went to Parthia (c. 170 vs 162-158) so keyframe -164 and /ledger/11 agree. Try https://en.wikipedia.org/wiki/Mithridates_I_of_Parthia

Spot checks: `/ledger/0` confirmed (Greco-Bactrian_Kingdom); `/ledger/6` confirmed (Demetrius_I_of_Bactria); `/ledger/11` confirmed (Eucratides_I); `/ledger/14` confirmed (Heliocles_I); `/ledger/15` confirmed (Greco-Bactrian_Kingdom).

## kingdom-of-cappadocia: fail

Area: infobox None km2 (None), Cliopatria 91738 km2, ratio None; The main page has no infobox area (checked); the author says so.

Findings:
- `/ledger (no vassal events)`: Blocking: the dossier records no client relation, though the author's own main page dates one for the whole period 95 BC to AD 17, and two neighbour dossiers record it. Evidence: Kingdom of Cappadocia infobox: 'Client kingdom of the Roman Republic and Roman Empire (95 BCE-17 AD)'; roman-republic L134 vassal_start -90 (counterpart kingdom-of-cappadocia); roman-empire L3 vassal_start -27 and L29 vassal_end 18. Fix: Add vassal_start roman-republic -95 (Sulla installs Ariobarzanes I), vassal_end roman-republic -27 and vassal_start roman-empire -27, vassal_end roman-empire at the end (17), region the kingdom's shape, source the main page; ask roman-republic to move its -90 to -95 or explain.
- `/keyframe_review (hole -87..-78)`: Blocking: Cliopatria has no Cappadocia shape for -87..-78 (rows -91..-88, then -77..-67); the dossier neither bridges the hole with a new keyframe nor explains why the kingdom disappears for ten years. Evidence: shapes.csv rows kingdom-of-cappadocia_-91 (to -88) and _-77; kingdom-of-pontus L31 occupation_end -85: Sulla 'demanded that Mithridates restore the kings of Bithynia and Cappadocia'; the nabataeans dossier in this batch bridges its own -25..-20 hole. Fix: Add a new keyframe kingdom-of-cappadocia_-87 (from -87, to -78, correction = the -91 shape, text saying it bridges the gap), with the occupation of 90/89-85 recorded as below.
- `/ledger (Pontic events), /wars`: Blocking: none of the kingdom-of-pontus events naming Cappadocia is mirrored (vassal_start -101, vassal_end -97, contest -91..-90, occupation_start -90, occupation_end -85), and the wars list lacks the First Mithridatic War, in which Cappadocia was occupied. Evidence: kingdom-of-pontus L16-L20, L31 (Kingdom of Pontus and First Mithridatic War pages); the dossier's notes admit it 'does not mirror them'; this dossier's own contest -95..-92 has no counterpart on kingdom-of-pontus. Fix: Mirror the Pontic vassalage 101-97 and the occupation 90-85 (or 89-85 with a page), add the First Mithridatic War with its zone, and reconcile the -95..-92 contest with kingdom-of-pontus; source https://en.wikipedia.org/wiki/First_Mithridatic_War.
- `/ledger/2`: Non-blocking: the -126 gain of Lycaonia and Cilicia names kingdom-of-pergamon, which ends in -129 with its loss to Cappadocia dated -129 (three years apart); the page says the Romans added the land. Evidence: Ariarathes V page: 'Lycaonia and Cilicia were added by the Romans to the dominions of his family' (no year; he was killed in 130 in the war against Aristonicus); kingdom-of-pergamon L16 -129 loss. Fix: Date the gain -129 and mark keyframe -126 adjust for -129..-127, or keep -126 with counterpart roman-republic and ask that dossier for the mirror.
- `/identity/rulers/0, /identity/rulers/1`: Non-blocking: Ariaramnes (-280) and Ariarathes III (-255) start before the dossier's start (-239); rulers must lie inside the life. Evidence: identity.start -239; rulers[0].from -280, rulers[1].from -255. Fix: Clip both to -239, or move the start with a page that dates independence (the main page: 'during the reign of Ariarathes III (c. 255-220 BC)').

Gaps for a gap-filler:
- `/ledger/0`: Confidence 1: the year of independence (page: during Ariarathes III, c. 255-220; infobox 'Founded by Ariarathes I: 331 BC'). Try https://en.wikipedia.org/wiki/Ariarathes_III_of_Cappadocia
- `/ledger/1`: Confidence 1: the 188 gain from the Seleucids (Apamea settlement?). Try https://en.wikipedia.org/wiki/Treaty_of_Apamea
- `/ledger/2`: Confidence 1: year of the Roman grant of Lycaonia and Cilicia. Try https://en.wikipedia.org/wiki/Aristonicus
- `/ledger/3`: Confidence 1: the -110 eastern strip to Pontus; no mirror on kingdom-of-pontus. Try https://en.wikipedia.org/wiki/Kingdom_of_Pontus
- `/ledger/6`: Confidence 1: end of the 95-92 contest. Try https://en.wikipedia.org/wiki/Mithridates_VI_of_Pontus
- `/ledger/7`: Confidence 1: the -77 return of the eastern strip; no mirror on kingdom-of-pontus. Try https://en.wikipedia.org/wiki/Third_Mithridatic_War
- `/ledger/8`: Confidence 1: the -63 strip to Commagene (Pompey's settlement). Try https://en.wikipedia.org/wiki/Commagene

Spot checks: `/ledger/2` confirmed (Ariarathes_V_of_Cappadocia); `/ledger/4` confirmed (Kingdom_of_Cappadocia); `/ledger/9` confirmed (Archelaus_of_Cappadocia); `/ledger/10` confirmed (Archelaus_of_Cappadocia); `/ledger/11` confirmed (Kingdom_of_Cappadocia).

## ankhwennefer: thin

Area: infobox None km2 (None), Cliopatria 176124 km2, ratio None; No area on the Ankhwennefer infobox (checked).

Findings:
- `/ledger/2, /ledger/4`: Non-blocking cross-dossier mismatch: the contest runs -197..-186 here and -195..-191 on ptolemaic-kingdom (L50, L51). Evidence: Ankhwennefer page: 'In 197 or 196 BC, the Ptolemies launched a counter-offensive and retook Lycopolis'; 'The war continued until c. 186 BC'. ptolemaic-kingdom: 'heavy fighting from 195 to 191 BC'. Fix: Leave as is (both read their pages); the ptolemaic-kingdom group may align or say so.

Gaps for a gap-filler:
- `/ledger (199 and 197)`: The 199 loss of Thebes and the c. 197 regain of the Thebaid, which ptolemaic-kingdom records (L45 gain -199, L49 loss -197) and the Ankhwennefer page mentions undated ('the rebels lost their capital of Thebes either shortly before or after Ankhwennefer's accession'; 'Despite having regained the Thebaid'). Within the 1-2 page budget: thin by design. Try https://en.wikipedia.org/wiki/Ptolemaic_Kingdom
- `/keyframe_review/0`: Outline for -205..-198 is the borrowed -197 shape; no page gives one. Try https://en.wikipedia.org/wiki/Ptolemy_V_Epiphanes

Spot checks: `/ledger/0` confirmed (Horwennefer); `/ledger/1` confirmed (Ankhwennefer_(pharaoh)); `/ledger/3` confirmed (Ankhwennefer_(pharaoh)); `/ledger/5` confirmed (Ankhwennefer_(pharaoh)).

## nabataeans: fail

Area: infobox None km2 (None), Cliopatria 126171 km2, ratio None; Nabataean Kingdom infobox has no area (checked); the author says the Nabataeans page has none either.

Findings:
- `/ledger (no vassal events); /notes`: Blocking: the Roman client relation from 62 BC is left out on the claim that 'this dossier cannot record it with the validator's pairing rule'; that is wrong, and roman-empire records it (vassal_start -27, vassal_end 106) with no mirror here. Evidence: Nabataean Kingdom page: Aretas 'recognized Roman supremacy over Nabataea' and the kingdom 'became a client kingdom under the influence of Rome' (after the 62 BC campaign); Aretas III page: 'in 62 BCE Scaurus marched on Petra'. tools/validate_dossier.py pairs a _start with a later _end of the same counterpart string and only warns on an open vassal_start that lasts to the end. Fix: Add vassal_start roman-republic -62, vassal_end roman-republic -27, vassal_start roman-empire -27, vassal_end roman-empire 106 (region the whole kingdom), and remove the sentence in notes.
- `/ledger/5 and /keyframe_review/10-16`: Blocking: the -91 loss of the Negev and Edom to Judea (confidence 1, 'kept only so that the corrected -91 keyframe is explained') is undone at -63 by corrections that add Edom, Moab and the Negev back, with no gain event between; the notes say the pages show the kingdom intact around Petra, the Negev and Moab until 106. Evidence: Ledger has no gain of Edom or the Negev between /ledger/5 (-91) and /ledger/11 (106); keyframes -91, -85, -77, -72 add only Moab and Gilead; keyframe -63 adds Edom, Moab and the Negev. Fix: Either drop /ledger/5 and add Edom and the Negev to the corrections of keyframes -91 to -66 (consistent with the notes), or add a dated, sourced gain that brings them back.
- `/ledger (no -24 gain)`: Blocking: the lihyan dossier ends with the Nabataean annexation (L4 loss and L5 dissolve -24, counterpart nabataeans) and this dossier has no mirror; its keyframes already draw Hegra and Dedan from -164 (bbox south to 26.19 N), overlapping Lihyan to -24. Evidence: lihyan L4: 'The Nabataean annexation of Lihyan was around 24 BC' (Lihyan page), region 110 km around Dedan (37.93 E, 26.62 N); nabataeans keyframe -164 note: 'the northern Hejaz around Hegra'. Fix: Add gain -24 from lihyan (the Dedan/AlUla oasis as the lihyan dossier draws it, source https://en.wikipedia.org/wiki/Lihyan) and take the oasis out of the keyframes before -24, or cite a page that makes Hegra Nabataean earlier.
- `/ledger/9`: Non-blocking: the note says the Aretas III page is 'silent on any loss in 63'; the page says the opposite. Evidence: Aretas III page: after the 62 BCE settlement Aretas 'would retain all Nabataean territory and possessions'; the Nabataean Kingdom page gives Damascus as Nabataean 85-71 only and no Roman seizure in 63. Fix: Rewrite the note to say the page contradicts a loss; keep the -63 loss of Damascus and the Hauran only with a page that dates it (try https://en.wikipedia.org/wiki/Damascus or https://en.wikipedia.org/wiki/Decapolis), otherwise mark keyframe -63 adjust to keep the Hauran. roman-republic has no mirror either way.
- `/ledger/10`: Non-blocking cross-dossier mismatch: the -27 loss of the Sinai coast names roman-empire, which records a vassal_start of the whole kingdom in -27, not a gain. Evidence: roman-empire L5 vassal_start -27 (counterpart nabataeans). Fix: Keep the loss only with a page; otherwise drop it and mark keyframe -27 adjust to keep the coast.

Gaps for a gap-filler:
- `/ledger/1`: Confidence 1: Gilead to Judea in 144. Try https://en.wikipedia.org/wiki/Hasmonean_dynasty
- `/ledger/2`: Confidence 1: the 126 Negev and Sinai coast. Try https://en.wikipedia.org/wiki/Nabataean_Kingdom
- `/ledger/3`: Confidence 1: year of Jannaeus' capture of Moab and Gilead. Try https://en.wikipedia.org/wiki/Alexander_Jannaeus
- `/ledger/5`: Confidence 1: the 91 Negev/Edom loss (see the blocking finding). Try https://en.wikipedia.org/wiki/Alexander_Jannaeus
- `/ledger/9`: Confidence 1: when Damascus and the Hauran left Nabataean rule. Try https://en.wikipedia.org/wiki/Damascus
- `/ledger/10`: Confidence 1: the 27 Sinai coast loss. Try https://en.wikipedia.org/wiki/Aelius_Gallus
- `/keyframe_review/15`: When Bosra became Nabataean (added in 6 with no event). Try https://en.wikipedia.org/wiki/Bosra

Spot checks: `/ledger/4` confirmed (Nabataean_Kingdom); `/ledger/6` confirmed (Aretas_III); `/ledger/7` confirmed (Aretas_III); `/ledger/8` confirmed (Aretas_III); `/ledger/11` confirmed (Arabia_Petraea); `/ledger/9` not on page (the page contradicts a loss; confidence 1, so a fix, not a fabrication) (Aretas_III).

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| greco-bactrian-kingdom -256 found -> seleucid-empire | seleucid-empire -245 loss | mismatch | 11 years apart: 256 is the Greco-Bactrian infobox, 245 the seleucid page ('around 245 BC, although the exact date is far from certain'); flagged by the author. Route to me-05 (seleucid-empire) and this dossier to agree on one year. |
| greco-bactrian-kingdom -208 contest_start -> seleucid-empire | seleucid-empire -209 vassal_start | mismatch | Seleucid side records Bactria as a vassal -209..-188 (L43, L56, Roman-Seleucid War page); the Greco-Bactrian main page says only that Antiochus 'finally decided to recognize the new ruler'. No contest on the seleucid side. Route to seleucid-empire. |
| greco-bactrian-kingdom -203 gain -> nobody | -   | exception | nobody. |
| greco-bactrian-kingdom -180 gain -> nobody | maurya-empire -185 dissolve | exception | Was maurya-empire (no mirror; ended -185, lost the north-west to nobody in -225); reviewer set counterpart to nobody for L5-L7. |
| greco-bactrian-kingdom -170 gain -> indo-greeks | -   | exception | indo-greeks owned by me-05-f, not run yet; the indo-greeks dossier must start c. 180 and mirror this. |
| greco-bactrian-kingdom -158 loss -> parthian-empire | -   | exception | parthian-empire owned by me-06-a, not run yet (also the -170..-158 contest). |
| greco-bactrian-kingdom -144 loss -> yuezhi | yuezhi -130 gain | mismatch | yuezhi gains Sogdia only in -130; indo-scythians L0 founds -144 with counterpart greco-bactrian-kingdom (Saka). Route to ia-01 and sa-02. |
| greco-bactrian-kingdom -130 loss -> yuezhi | yuezhi -130 gain | matched | yuezhi L7 -130 (Sogdia and north Bactria); its L8 -126 takes Bactria south of the Oxus, which this dossier loses in -130: 4 years apart for the southern half. |
| greco-bactrian-kingdom -127 dissolve -> indo-greeks | -   | exception | indo-greeks owned by me-05-f, not run yet. |
| indo-scythians -144 found -> greco-bactrian-kingdom | greco-bactrian-kingdom -144 loss | mismatch | Greco-Bactrian -144 loss names yuezhi, not indo-scythians. |
| kingdom-of-cappadocia -239 found -> seleucid-empire | seleucid-empire -239 loss | matched | Both confidence 1. |
| kingdom-of-cappadocia -188 gain -> seleucid-empire | seleucid-empire -188 loss | matched | Both confidence 1. |
| kingdom-of-cappadocia -126 gain -> kingdom-of-pergamon | kingdom-of-pergamon -129 loss | mismatch | Three years apart, and kingdom-of-pergamon ends -129; the page says the Romans added the land. |
| kingdom-of-cappadocia -110 loss -> kingdom-of-pontus | kingdom-of-pontus   | missing | No -110 gain on kingdom-of-pontus. |
| kingdom-of-cappadocia -95 contest_start -> kingdom-of-pontus | kingdom-of-pontus -91 contest_start | mismatch | Different contests: -95..-92 here, -91..-90 (Tigranes) on pontus; neither mirrored. |
| kingdom-of-pontus -101 vassal_start -> kingdom-of-cappadocia | kingdom-of-cappadocia   | missing | Also vassal_end -97; not mirrored. |
| kingdom-of-pontus -90 occupation_start -> kingdom-of-cappadocia | kingdom-of-cappadocia   | missing | Occupation -90..-85 not mirrored; Cliopatria hole -87..-78 unbridged. |
| kingdom-of-cappadocia -77 gain -> kingdom-of-pontus | kingdom-of-pontus   | missing | No -77 loss on kingdom-of-pontus. |
| kingdom-of-cappadocia -63 loss -> kingdom-of-commagene | -   | exception | kingdom-of-commagene owned by me-06-b, not run yet. |
| roman-republic -90 vassal_start -> kingdom-of-cappadocia | kingdom-of-cappadocia   | missing | Main page infobox: client kingdom 95 BCE-17 AD; not mirrored. |
| roman-empire -27 vassal_start -> kingdom-of-cappadocia | kingdom-of-cappadocia   | missing | Also vassal_end 18; not mirrored. |
| kingdom-of-cappadocia -25 gain -> roman-empire | roman-empire   | missing | No -25 loss of Cilicia Tracheia on roman-empire (Amyntas of Galatia held it to 25 BC; galatia ends -26). |
| kingdom-of-cappadocia 17 dissolve -> roman-empire | roman-empire 18 gain | matched | Within one year (Archelaus d. AD 17). |
| ankhwennefer -205 found -> ptolemaic-kingdom | ptolemaic-kingdom -205 loss | matched |  |
| ptolemaic-kingdom -199 gain -> ankhwennefer | ankhwennefer   | missing | Thebes retaken Dec 199; not on the pages ankhwennefer opened (thin by budget). |
| ptolemaic-kingdom -197 loss -> ankhwennefer | ankhwennefer   | missing | Thebaid regained c. 197; ankhwennefer has only a contest_start -197. |
| ankhwennefer -197 contest_start -> ptolemaic-kingdom | ptolemaic-kingdom -195 contest_start | mismatch | Two years; ends -186 here, -191 on ptolemaic-kingdom. |
| ankhwennefer -191 loss -> ptolemaic-kingdom | ptolemaic-kingdom -191 gain | matched |  |
| ankhwennefer -186 dissolve -> ptolemaic-kingdom | ptolemaic-kingdom -186 gain | matched |  |
| nabataeans -144 loss -> judea | -   | exception | judea owned by me-05-f, not run yet (also -96 loss, -93 gain, -91 loss). |
| nabataeans -85 gain -> seleucid-empire | seleucid-empire -66 loss | mismatch | 19 years apart; the Aretas III page dates Damascus to 85; seleucid-empire's -66 is Cliopatria only. Route to me-05 (seleucid-empire). |
| nabataeans -72 loss -> kingdom-of-armenia | -   | exception | kingdom-of-armenia owned by eu-19-a, not run yet (also the -69 gain). |
| nabataeans -63 loss -> roman-republic | roman-republic   | missing | No mirror on roman-republic; the Aretas III page says Aretas kept all his territory in 62. |
| nabataeans -27 loss -> roman-empire | roman-empire -27 vassal_start | mismatch | Roman-empire records a client relation, not a gain of the Sinai coast. |
| roman-empire -27 vassal_start -> nabataeans | nabataeans   | missing | Also vassal_end 106; not mirrored (author's pairing-rule claim is wrong). |
| lihyan -24 loss -> nabataeans | nabataeans   | missing | Also lihyan dissolve -24; no gain on nabataeans, whose keyframes already cover Dedan/Hegra from -164. |
| qedar -343 dissolve -> nabataeans | nabataeans -169 found | mismatch | qedar's dissolve names nabataeans 174 years before the Nabataean dossier starts; qedar side to fix (counterpart nobody, or a later year). |
| nabataeans 106 dissolve -> roman-empire | roman-empire 106 gain | matched |  |

## Problems

- WebFetch returns a small model's answer, not page text: spot checks rest on those answers.
- Reviewer edited history/polities/greco-bactrian-kingdom.json (ledger 5-7 counterpart maurya-empire -> nobody, one note sentence); re-validated 0 errors, 0 warnings; read back.
- Not written yet (exceptions): indo-greeks and judea (me-05-f), parthian-empire (me-06-a), kingdom-of-commagene (me-06-b), kingdom-of-osroene, himyarite-kingdom, antigonid-macedonia, kingdom-of-armenia (eu-19-a).
- Neighbour fixes routed: seleucid-empire (-245 vs -256 secession; -209..-188 Bactrian vassalage unsupported by the Greco-Bactrian page; -66 loss to nabataeans should be 85); roman-republic (no nabataeans event for 62/63; Cappadocia vassal_start -90 vs page 95); roman-empire (no -25 loss of Cilicia Tracheia); kingdom-of-pontus (no -110 gain / -77 loss for Cappadocia); qedar (-343 dissolve to nabataeans); yuezhi and indo-scythians (who took Sogdia in -144).
