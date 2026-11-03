# Review of batch me-06-x (Parthia and the Sasanians, additions)

Reviewed 2026-10-19 by the Phase B adversarial reviewer. Nine new dossiers, none with a Cliopatria row. All nine validate with `--resolve` (no errors, no warnings), before and after the reviewer's edits. Spot checks: 4 per dossier, 36 in all, every one confirmed on the page (WebFetch). No fabricated or mis-dated confidence-3 event was found. The failures are structural: missing vassal records, shapes that overlap a neighbour without saying so, and one land span the page contradicts.

Verdicts: persis **fail**, elymais **fail**, characene **fail**, hatra **fail**, kingdom-of-kinda **thin**, bahram-chobin **fail**, vistahm **thin**, vologases-vi **fail**, osroes-i **fail**.

## What runs through the batch

- **Vassal status is missing from the vassals' own ledgers.** Persis, Elymais, Characene and Hatra are each called a Parthian vassal on their own pages (infobox status 'frequently a vassal of the Parthian Empire' for Characene and Hatra; 'ruled as vassal kings of the Parthian Empire' for Persis; 'frequently a vassal under Parthian control' for Elymais). None of the four has a vassal_start or vassal_end. parthian-empire carries vassal_start for persis (-135), elymais (-140) and characene (-122), none for hatra. The same omission was blocking for lakhmid-kingdom and ghassanids in the me-06-d review, and it is blocking here. Each fix is two events (the years are in the fixes).
- **Overlaps nobody acknowledged** (gazetteer intersections): osroes-i's Babylonia contains 34,400 km2 of characene (110-129). bahram-chobin's Babylonia contains 73,300 km2 of the Lakhmid shape of 510-601. elymais's Khuzestan sits in the Seleucid shape for -147 to -145. vologases-vi's Seleucia disc stays in place to 228 while sasanian-empire holds Mesopotamia from 224 and Ctesiphon, across the river, from 226.
- **Rebel states and their counterparts**: none of the four rebel states has mirror events in parthian-empire or sasanian-empire. The author flagged this; route it to those gap-fillers (cross_checks in the JSON).
- **Reviewer edits applied** (re-validated; each note tagged '[Reviewer me-06-x, 2026-10-19: ...]'): hatra /wars/4/to 241 to 240; bahram-chobin /wars/0/from 589 to 590 and /ledger/2 confidence 3 to 2; vistahm /wars/0/to 597 to 596; osroes-i /ledger/1-3 confidence 3 to 2.

## Per dossier

### persis: fail

- **/ledger (missing events)** (to do): Blocking: the ledger has no vassal_start or vassal_end with counterpart parthian-empire, so a state that was a Parthian vassal for some 360 of its 374 years carries no record of it, and parthian-empire /ledger/15 (vassal_start persis -135) and /ledger/65 (vassal_end persis 215) have no mirror. Evidence: Kings of Persis page: the kings 'ruled as vassal kings of the Parthian Empire'; Strabo has the early kings Seleucid tributaries 'until c.140 BC, when the Parthians conquered the region'; the frataraka Wadfradad II (fl. 138 BC) 'was made a vassal of the Iranian Parthian (Arsacid) Empire'. The dossier's own war /wars/0 says Mithridates I 'made Persis a Parthian vassal'. Fix: Add vassal_start, counterpart parthian-empire, year -138, region Persis, confidence 2, source Kings_of_Persis (Wadfradad II, fl. 138 BC; Strabo c. 140 BC), and vassal_end, counterpart parthian-empire, at 224 (or at 215 if the orchestrator settles the 215-224 overlap in favour of sasanian-empire). Route the year differences (-135 against -138, 215 against 224) to the parthian-empire gap-filler.
- thin /identity/capitals/0: the Fratarakas' own seat (Persepolis traditionally, Susa per Kritt) for -150 to -132 (try https://en.wikipedia.org/wiki/Fratarakas)
- thin /ledger/3: a settled end for the 215-224 overlap with sasanian-empire /ledger/0 (found persis 215) and parthian-empire /ledger/64-65 (Persis to Ardashir 215); 211 cells (about 53,000 km2) of Persis lie in the Sasanian 215 shape (try https://en.wikipedia.org/wiki/Ardashir_I)
- spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed
- area: No Cliopatria shape and no infobox area (Kings of Persis infobox: only a map of the 'approximate extent'); the author says so. The keyframe is the gazetteer's Persis, 620 cells, about 156,800 km2.

### elymais: fail

- **/ledger (missing events)** (to do): Blocking: no vassal_start or vassal_end with counterpart parthian-empire for the restored kingdom of -82 to 222, although /ledger/2's own note says 'the restored state is a Parthian vassal, not independent'. Evidence: Elymais page, intro: Elymais was 'frequently a vassal under Parthian control'; 'From 140/139 BC, Elymais was then under direct Parthian control for several decades, with occasional rebellions, until around 82 BC.' parthian-empire /ledger/12 has vassal_start elymais -140 and /ledger/68 vassal_end elymais 224; the elymais ledger mirrors neither. Fix: Add vassal_start, counterpart parthian-empire, year -82 (with the gain), region Khuzestan, confidence 2, source Elymais, and vassal_end, counterpart parthian-empire, at 222 (with the dissolve). The parthian-empire gap-filler must turn its -140 vassal_start into a gain of Khuzestan (direct rule -140 to -82), add the -82 loss and vassal_start, and move the vassal_end to 222 or note the two-year difference.
- **/keyframe_review/0** (to do): The -147 to -141 shape (Khuzestan) overlaps the seleucid-empire Cliopatria shape of -164..-145 on 248 cells (about 62,700 of 66,300 km2) for -147 to -145, and the seleucid-empire ledger has no loss of Susiana to elymais. Evidence: Gazetteer: intersect of region Khuzestan with Seleucid Empire -147 = 248 cells. seleucid-empire ledger: no Elymais, Susa or Khuzestan event between -164 and -141. Fix: Non-blocking for this dossier: say in the keyframe note that the Seleucid shape keeps Susiana to -145, and route a 147 BC loss of Khuzestan to elymais to the seleucid-empire gap-filler.
- thin /identity/capitals/0: the royal seat: the infobox says Susa but the text says 'Susa lay to the east of the territory of Elymais' (try https://en.wikipedia.org/wiki/Seleucia_on_the_Hedyphon)
- thin /keyframe_review/1: the provinces Massabatice (Masabadhan), Corbiane and Gabiane, which the page names but the shape does not place (try https://en.wikipedia.org/wiki/Elymais)
- spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed
- area: No Cliopatria shape; Elymais infobox gives no area. Keyframes are the gazetteer's Khuzestan, about 66,300 km2.

### characene: fail

- **/ledger (missing events)** (to do): Blocking: no vassal_start or vassal_end with counterpart parthian-empire, though Characene was a Parthian vassal from 124 BC to its end; parthian-empire /ledger/21 (vassal_start characene -122) and /ledger/67 (vassal_end characene 224) have no mirror. Evidence: Characene page: infobox status 'Autonomous state, frequently a vassal of the Parthian Empire'; Characene and Hyspaosines pages: 'In 124 BC, however, Hyspaosines accepted Parthian suzerainty, and continued to rule Characene as a vassal.' Fix: Add vassal_start, counterpart parthian-empire, year -124, region as the found event, confidence 3 (both pages give the year), source Hyspaosines, and vassal_end, counterpart parthian-empire, at 222 with the dissolve. Route -124 (not -122) and 222 (not 224) to the parthian-empire gap-filler.
- **/ledger/1** (to do): The occupation of Babylon in 127 BC (occupation_start and occupation_end, counterpart parthian-empire) has no mirror in the parthian-empire ledger, and the author's notes do not list it among the events parthian-empire must carry. Evidence: Hyspaosines page: 'Hyspaosines briefly occupied the Parthian city of Babylon in 127 BC'; 'at the start of November 127 BC, the Parthian general Timarchus recaptured it.' parthian-empire ledger: no event with counterpart characene before -122. Fix: Non-blocking for this dossier: add the pair to the notes' list for parthian-empire (occupation_start and occupation_end, counterpart characene, -127, region Babil).
- thin /keyframe_review/0: Bahrain and Failaka as parts of the realm: the Characene page says 'The realm of the kingdom included the islands Failaka and Bahrain'; no years on the page (try https://en.wikipedia.org/wiki/Mazun)
- thin /wars/1: Attambelos VII's submission to Trajan in 115-116 (a brief Roman client status); the war has empty zones (try https://en.wikipedia.org/wiki/Trajan%27s_Parthian_campaign)
- spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed
- area: No Cliopatria shape; Characene infobox gives no area. Keyframe Al-Basrah + Maysan + Kuwait, 206 cells, about 52,100 km2.

### hatra: fail

- **/ledger (missing events)** (to do): Blocking: Hatra is drawn as independent for its whole life; no vassal pair with parthian-empire exists in this ledger or in the parthian-empire ledger. Evidence: Kingdom of Hatra page: infobox status 'Autonomous state, frequently a vassal of the Parthian Empire'; text: 'mostly under Parthian suzerainty'. Sanatruq I page: 'He was granted the title of king by his Parthian overlord Vologases IV (r. 147-191)'. The author's notes ask parthian-empire for the pair but this dossier has none of its own. Fix: Add vassal_start, counterpart parthian-empire, at 116 (the dossier's start; confidence 1 for the year, since the page gives none) and vassal_end at 224 (the Parthian fall), region {place: Hatra, km: 60}, source Kingdom_of_Hatra; route the same pair (counterpart hatra) to the parthian-empire gap-filler.
- **/wars/4/to** (applied by reviewer): The war 'Shapur I's conquest of Hatra' ran to 241, after the dossier's end (240). Evidence: Kingdom of Hatra page: 'finally conquered after the 240/41 capture of its capital'; the dossier ends in 240 (rule 2: wars inside the life). Fix: to: 240, with a note.
- thin /ledger/0: a dated founding: the found event is confidence 1 (start set at Trajan's siege, 116/117; infobox 'Established: 2nd century CE'; first lords 128/29) (try https://en.wikipedia.org/wiki/Hatra)
- thin /keyframe_review/0: the kingdom's territory: a 60 km placeholder disc; no page names its land (try https://en.wikipedia.org/wiki/Parthian_Empire)
- thin /wars/4: the Roman alliance or vassalage under Gordian III (Sanatruq II 'became a vassal of the Romans under Gordian III', no year) (try https://en.wikipedia.org/wiki/Roman%E2%80%93Persian_Wars)
- spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /wars/3 confirmed
- area: No Cliopatria shape; no infobox area. Placeholder 60 km disc, about 11,000 km2, acknowledged as confidence 1.

### kingdom-of-kinda: thin

- thin /wars/0: al-Harith's capture of the Lakhmid capital al-Hira (an occupation of lakhmid-kingdom land) has no event; both pages date it only to 'Sometime during the reign of the Sasanian king Kavad I (r. 498-531)' (try https://en.wikipedia.org/wiki/Lakhmids)
- thin /identity/predecessors/0: Himyarite suzerainty over Hujr and the Ma'add (no vassal pair here or in himyarite-kingdom); the Kinda page has 'with support from Himyar' only (try https://en.wikipedia.org/wiki/Himyarite_Kingdom)
- thin /ledger: the Byzantine federate status under al-Harith (Kingdom of Kindah page: the Kinda 'had become federates of the empire'; no year on the pages read) (try https://en.wikipedia.org/wiki/Kingdom_of_Kindah)
- thin /identity/capitals/0: the seat for 450-528: Qaryat al-Faw is the Kingdom page's 'likely' capital but the Qaryat al-Faw page has the Kinda abandon it about 300 (try https://en.wikipedia.org/wiki/Qaryat_al-Faw)
- spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /wars/0 confirmed; /identity/capitals/0 confirmed
- area: No Cliopatria shape; Kingdom of Kindah infobox gives no area. Keyframe is the gazetteer's Nejd, 2,180 cells, about 551,000 km2, acknowledged as a soft tribal hegemony; it touches the Lakhmid Cliopatria shape on one cell only.

### bahram-chobin: fail

- **/keyframe_review/0/correction** (to do): Blocking: the 590 shape's Babylonia overlaps the lakhmid-kingdom Cliopatria shape alive in 590 (lakhmid-kingdom_510, 510-601) on 290 cells, about 73,300 km2 (39 percent of Babylonia's 186,100 km2), and neither the note nor any page says Bahram held the Lakhmid land. Evidence: Gazetteer: intersect of region Babylonia with Lakhmid Kingdom 590 = 290 cells, bbox 42.88-46.96 E, 29.09-32.54 N; the union Babylonia + Media + Iranian Khorasan has 2,304 cells of which 2,014 lie in the Sasanian 590 shape. The Bahram Chobin page says only that he held Ctesiphon and Mesopotamia. Fix: Use {"minus": [{"region": "Babylonia"}, {"cliopatria": "Lakhmid Kingdom", "year": 590}]} in /keyframe_review/0, in /ledger/0's region, in /ledger/1's region and in the predecessor and successor land.
- **/wars/0/from** (applied by reviewer): The war 'Sasanian civil war of 589-591' started in 589, before the dossier's start (590). Evidence: Rule 2 (wars inside the life); the civil war page has the war break out in 589, the Bahram Chobin page has him declare himself king in summer 590. Fix: from: 590, with a note that the war broke out in 589.
- **/ledger/2/confidence** (applied by reviewer): Confidence 3 on the dissolve, whose region (Media and Iranian Khorasan) the cited Blarathon page does not name. Evidence: Battle of Blarathon page: date 'August 591', 'near Ganzak'; Bahram fled 'east to Nisapur'; no land of Bahram's named. Fix: confidence 2.
- thin /keyframe_review/0: Atropatene (Adurbadagan), which the Bahram Chobin page lists among his northern commands; the 589-590 land of the revolt before the summer-590 accession (try https://en.wikipedia.org/wiki/Sasanian_civil_war_of_589%E2%80%93591)
- spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /identity/capitals/0 confirmed
- area: No Cliopatria shape; a person's article, no area. The 590 keyframe is about 583,000 km2, of which about 73,000 km2 lie in the Lakhmid shape (see fix 1).

### vistahm: thin

- **/wars/0/to** (applied by reviewer): The war 'Revolt of Vistahm' ran to 597, after the dossier's end (596). Evidence: Rule 2 (wars inside the life); the Vistahm page: 'it required another expedition by Smbat in the next year to finally end the rebellion' (undated). Fix: to: 596, with a note on the undated final expedition.
- thin /keyframe_review/0: Ray (in the gazetteer's Media): the Vistahm page's coin caption reads 'Coin of Vistahm, minted at Ray in 595/6', but the note says Media is not drawn (try https://en.wikipedia.org/wiki/Vistahm)
- thin /ledger/0: the outbreak year (590/1 or 594/5 on the infobox) and the year of Vistahm's death (596 or 600) (try https://en.wikipedia.org/wiki/Khosrow_II)
- spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /keyframe_review/0 confirmed; /wars/0 confirmed
- area: No Cliopatria shape; no area on the page. Keyframe about 600,000 km2 (Khorasan 558,000 + Tabaristan + Ardabil disc); 273 cells (about 69,000 km2) of Khorasan lie east of the Sasanian 591 shape, consistent with the page's 'from the Oxus river'.

### vologases-vi: fail

- **/keyframe_review/0** (to do): Blocking: the Seleucia disc is drawn to 228, but the Vologases VI page itself says he ruled Seleucia only until 221/2; the note credits that date to the Artabanus IV page alone. Drawn to 228 the disc overlaps the sasanian-empire, which takes the Parthian west at /ledger/4 (224) and moves its court to Ctesiphon, across the Tigris from Seleucia, at /ledger/5 (226). Evidence: Vologases VI page: 'Vologases VI continued to rule Seleucia until 221/2'; 'coin mints of him even appear in Mesopotamia until 228'; Ardashir 'must have driven out or defeated Vologases in Mesopotamia soon after 228'. Artabanus IV page: 'would rule a small principality centered around Seleucia until 221/2'. Fix: End the Seleucia keyframe at 222 and either dissolve the state in 222 (counterpart parthian-empire, Artabanus IV; successors parthian-empire) or keep the life to 228 with no drawn land after 222 and say so; correct the note's attribution. Keep the coins to 228 in the note.
- thin /keyframe_review/0: the extent of the Seleucia principality (60 km placeholder disc) (try https://en.wikipedia.org/wiki/Seleucia)
- spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed (infobox death 228), but the same page ends his rule of Seleucia in 221/2: see fix 1
- area: No Cliopatria shape; no area on the page. Placeholder 60 km disc, about 11,000 km2.

### osroes-i: fail

- **/ledger/1** (to do): Blocking: the 116 loss and the 117 gain (/ledger/2) against roman-empire have no mirror. The roman-empire dossier records Trajan's hold on Ctesiphon as occupation_start 115 (/ledger/70) and occupation_end 117 (/ledger/71) against parthian-empire; parthian-empire records occupation_start 116 (/ledger/53) and occupation_end 117 (/ledger/54) against roman-empire. Nobody records a gain or loss with osroes-i. Evidence: Osroes I page: 'In 116, Trajan captured Seleucia and Ctesiphon'; Trajan 'installed Osroes I's son Parthamaspates on the throne at Ctesiphon'; 'After Trajan's death in 117, the Parthians removed Parthamaspates from the throne and reinstated Osroes I.' That is a client king, not an annexation, and the author's notes do not mention the Roman side. Fix: Rewrite /ledger/1-2 as occupation_start (116) and occupation_end (117), counterpart roman-empire, region Babylonia (or Seleucia and Ctesiphon discs); merge /keyframe_review/0-1 into one 110-129 shape (the land stays Osroes', hatched in 116); route to the roman-empire and parthian-empire gap-fillers that Babylonia's owner in 116-117 is osroes-i.
- **/keyframe_review/0/correction** (to do): Blocking: Babylonia includes 136 cells (about 34,400 km2) of characene's land (Al-Basrah + Maysan + Kuwait, 52,100 km2), 66 percent of that kingdom, which was alive in 110-129; the double claim is not acknowledged. The same applies to /keyframe_review/1 and the ledger regions. Evidence: Gazetteer: intersect of region Babylonia with the characene keyframe union = 136 cells, bbox 46.46-48.41 E, 29.28-32.66 N. The Osroes I page names only 'the western part of the empire, including Mesopotamia'. Fix: Use {"minus": [{"region": "Babylonia"}, {"union": [{"admin1": "Al-Basrah", "country": "Iraq"}, {"admin1": "Maysan", "country": "Iraq"}]}]} in both keyframes, the ledger regions and the predecessor and successor land, or say why Characene is drawn inside Osroes' land.
- **/ledger/1/confidence** (applied by reviewer): Confidence 3 on /ledger/1, /ledger/2 and /ledger/3 with region Babylonia, which the Osroes I page does not name. Evidence: The page names Seleucia and Ctesiphon (116, 117) and no land at all for 129. Fix: confidence 2 on all three.
- thin /ledger/0: the start: the page's lead says he 'ruled the western portion of the Parthian Empire from 109 to 129, with a one-year interruption'; the dossier starts in 110 (within a year; consider 109) (try https://en.wikipedia.org/wiki/Vologases_III)
- spot checks: /ledger/0 confirmed (the lead says 109 to 129; 110 is within a year); /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed
- area: No Cliopatria shape; no area on the page. Keyframes are the gazetteer's Babylonia, about 186,000 km2, of which 116,000 km2 lie in the Parthian 110 shape and 34,000 km2 in characene (see fix 2).

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| parthian-empire -135 vassal_start (persis) | none | missing | No vassal_start in persis; pages give c. 140/138 BC (Kings of Persis). Blocking fix in persis; year to settle in parthian-empire. |
| parthian-empire 215 vassal_end (persis) | persis 224 dissolve | mismatch | Persis runs to 224 (Kings of Persis infobox); parthian-empire and sasanian-empire /ledger/0 (found persis 215) give Persis to Ardashir in 215; 53,000 km2 claimed twice 215-224. Author flagged; orchestrator to settle. |
| persis 224 dissolve (sasanian-empire) | sasanian-empire 215 found | mismatch | Same overlap seen from the persis side. |
| persis -150 found (seleucid-empire) | none | exception | The corrected Seleucid and Parthian keyframes of -164..-145 do not hold Persis; no mirror needed. |
| elymais -147 found (seleucid-empire) | none | mismatch | seleucid-empire_-164 (to -145) holds 62,700 km2 of Khuzestan; no Seleucid loss of Susiana to elymais. Route to seleucid-empire (me-05). |
| elymais -140 loss (parthian-empire) | parthian-empire -140 vassal_start | mismatch | Elymais page: direct Parthian control 140/139 to c. 82 BC, so parthian-empire needs a gain, not a vassal_start, at -140. Author flagged. |
| elymais -82 gain (parthian-empire) | none | missing | No -82 loss or vassal_start in parthian-empire. Author flagged. |
| parthian-empire -140 vassal_start (elymais) | none | missing | No vassal_start in elymais (the vassal period is -82 to 222 on the page). Blocking fix in elymais. |
| parthian-empire 224 vassal_end (elymais) | elymais 222 dissolve | mismatch | Two years apart: Elymais infobox 221/222; parthian-empire 224. |
| elymais 222 dissolve (sasanian-empire) | sasanian-empire 224 gain | mismatch | sasanian-empire /ledger/1 takes Susiana in 224 from parthian-empire, not from elymais in 222. |
| characene -127 occupation_start (parthian-empire) | none | missing | No occupation of Babylon by characene in parthian-empire; not in the author's routing list. |
| characene -127 occupation_end (parthian-empire) | none | missing | As above (November 127 BC, Timarchus). |
| parthian-empire -122 vassal_start (characene) | none | mismatch | No vassal_start in characene; the Characene and Hyspaosines pages give 124 BC. Blocking fix in characene; parthian-empire should move to -124. |
| parthian-empire 224 vassal_end (characene) | characene 222 dissolve | mismatch | Two years apart: Characene infobox 'Sasanian conquest: 222 AD'. |
| characene 222 dissolve (sasanian-empire) | sasanian-empire 224 gain | mismatch | sasanian-empire /ledger/1 takes Mesene in 224 from parthian-empire. |
| sasanian-empire 240 gain (hatra) | hatra 240 dissolve | matched | Hatra falls 240 (240/41) on both sides. |
| sasanian-empire 226 contest_start (hatra) | none | mismatch | hatra has the 226-227 attempt as a war without zones (no ground taken, Ardashir I page); one side should change. Author flagged. |
| hatra 116 vassal (none) (parthian-empire) | none | missing | No vassal pair on either side though the Kingdom of Hatra page says 'frequently a vassal of the Parthian Empire'. Blocking fix in hatra; route to parthian-empire. |
| kingdom-of-kinda 450 found (nobody) | none | exception | Counterpart nobody; Himyarite sponsorship not in himyarite-kingdom (thin). |
| kingdom-of-kinda 528 dissolve (nobody) | none | exception | No successor on the pages. |
| bahram-chobin 590 found (sasanian-empire) | none | missing | sasanian-empire has no 590 loss to bahram-chobin. Author flagged; route to sasanian-empire (me-06-c). |
| bahram-chobin 591 loss (sasanian-empire) | none | missing | No 591 gain from bahram-chobin in sasanian-empire. Author flagged. |
| bahram-chobin 591 dissolve (sasanian-empire) | none | missing | No August 591 gain in sasanian-empire. Author flagged. |
| bahram-chobin 590 found (sasanian-empire) | lakhmid-kingdom 590 keyframe lakhmid-kingdom_510 | mismatch | Babylonia overlaps the Lakhmid 510-601 shape by 73,300 km2; unacknowledged. Blocking fix in bahram-chobin. |
| vistahm 591 found (sasanian-empire) | none | missing | No 591 loss to vistahm in sasanian-empire. Author flagged. Iranian Khorasan is also in bahram-chobin's 591 keyframe (to August 591). |
| vistahm 596 dissolve (sasanian-empire) | none | missing | No 596 gain from vistahm in sasanian-empire. Author flagged. |
| vologases-vi 213 found (parthian-empire) | none | missing | parthian-empire has no 213 loss of Seleucia to vologases-vi. |
| vologases-vi 213 contest_start (parthian-empire) | none | missing | No contest with vologases-vi in parthian-empire (213-216). Author flagged. |
| vologases-vi 228 dissolve (sasanian-empire) | sasanian-empire 224 gain | mismatch | sasanian-empire /ledger/4 holds Mesopotamia from 224 (court at Ctesiphon 226); the Vologases VI page ends his rule of Seleucia in 221/2. Blocking fix in vologases-vi. |
| osroes-i 110 found (parthian-empire) | none | missing | parthian-empire has no 110 loss of the west to osroes-i. Author flagged. |
| osroes-i 116 loss (roman-empire) | roman-empire 115 occupation_start | mismatch | roman-empire /ledger/70 occupation_start 115 and parthian-empire /ledger/53 occupation_start 116 name parthian-empire, not osroes-i, and are occupations, not a gain. Blocking fix in osroes-i. |
| osroes-i 117 gain (roman-empire) | roman-empire 117 occupation_end | mismatch | roman-empire /ledger/71 occupation_end 117 against parthian-empire; no loss to osroes-i. |
| osroes-i 129 dissolve (parthian-empire) | none | missing | parthian-empire has no 129 gain from osroes-i. Author flagged. |
| osroes-i 110 found (parthian-empire) | characene 110 keyframe characene_-141 | mismatch | Babylonia overlaps characene's land by 34,400 km2 in 110-129; unacknowledged. Blocking fix in osroes-i. |

## Gazetteer names wanted (not used in region specs)

Charax Spasinu, Qaryat al-Faw, al-Hira, Yamama, Failaka.

## Problems

- No dossier in the batch has a Cliopatria shape or an infobox area, so every area_check is null with acknowledged true; region areas are from the gazetteer.
- Most of the cross-dossier fixes belong to parthian-empire (me-06-a), sasanian-empire (me-06-c), roman-empire and seleucid-empire; this batch could not edit them. The cross_checks list each one.
- WebFetch did not return the Osroes I infobox; the lead's '109 to 129' was used instead.
- Reviewer edits applied on the mount and re-validated (no errors or warnings): hatra /wars/4/to, bahram-chobin /wars/0/from and /ledger/2/confidence, vistahm /wars/0/to, osroes-i /ledger/1-3/confidence; each note carries a '[Reviewer me-06-x, 2026-10-19: ...]' tag.
