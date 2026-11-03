# Review of batch me-05-a (Achaemenids and Seleucids, part a)

Reviewer, 2026-10-19. Validator: 0 errors on all four (5 warnings on achaemenid-empire for counterparts without dossiers, all listed by the author). Spot checks were made with WebFetch on the pages named; small fixes were applied in place and re-validated (marked applied).

## median-kingdom: thin

Area: infobox 2800000 km2 (-585), Cliopatria 2243378 km2, ratio 0.8. Cliopatria median-kingdom_-600 (600-551) against the infobox '585 BC: 2,800,000 km2'; corrected outline about 1.86 M km2 (0.66), stated in the keyframe note.

Findings:
- `/ledger/1/counterpart, /ledger/7, /ledger/8, /ledger/9` (applied by reviewer): Four events named achaemenid-empire as counterpart in 615-550, before that dossier's start (-550). Evidence: achaemenid-empire identity.start is -550 and its predecessors note says 'Persia itself, Cyrus' kingdom of Anshan (king since 559), is not a Cliopatria row'; the Medes page: 'In 553 BCE, Cyrus the Great, the King of Persia, a Median vassal, revolted'. No mirror can exist in the Achaemenid ledger before its life. Fix: Counterpart set to 'Persia (kingdom of Anshan)' on /ledger/1, 7, 8, 9 (the 550 loss stays achaemenid-empire); a kingdom-of-anshan dossier is listed under counterparts_needing_dossiers.
- `/notes` (applied by reviewer): The notes did not record that the Median dynasty page gives the realm as reaching Central Asia, which bears on the removal of Afghanistan and Pakistan in both keyframes. Evidence: Median dynasty page: 'stretching from the eastern banks of the Halys River in Anatolia to Central Asia'. The correction rests on the Medes page ('from northeastern Iran to the Kızılırmak') and Cyrus' eastern campaigns of 545-540 (Cyrus the Great page), which remain good grounds. Fix: Sentence appended to /notes naming the conflict and the grounds for the correction.
- `/identity/rulers/0` (for the author): Cyaxares is dated from -625, ten years before the state's start (-615). Evidence: Brief section 2.2: rulers inside the life. The author notes it. Fix: Leave until the life is extended back (see thin); otherwise clamp to -615 with the reign in the note.

Gaps for a gap-filler:
- `/ledger (missing)`: No contest pair with Lydia for the Median-Lydian war 590-585 and the Halys border; lydia /ledger/8-9 has contest_start 590 and contest_end 585 with median-kingdom (confidence 2, Lydia page). Page: https://en.wikipedia.org/wiki/Battle_of_the_Eclipse
- `/ledger/5`: Manna gain at 600, confidence 1. The Scythia dossier's page dates the Median annexation of Mannai to 616 and Urartu to 'the c. 590s BC'; scythia /ledger/8 books a loss of Sakez near Lake Urmia and Urartu to median-kingdom at 600 that this ledger does not mirror. Urartu is not in this ledger at all. Page: https://en.wikipedia.org/wiki/Scythians
- `/ledger/3`: Gain of an Assyrian strip at 612 against neo-assyrian-empire /ledger/55, a loss of Assur to the Medes at 614 (confidence 2); the Assyrian heartland goes to Babylon at 612 (/ledger/56). Add a 614 gain of Assur or reconcile. Page: https://en.wikipedia.org/wiki/Neo-Assyrian_Empire
- `/ledger/0`: Found at 615, confidence 1; the page dates Cyaxares from 625 and the dynasty from 700 (Herodotus). Extending the life would also take the Scythian hegemony 652-625 (scythia /ledger/4, /ledger/6) into this dossier. Page: https://en.wikipedia.org/wiki/Cyaxares
- `/ledger/1`: Vassal_start of Persis at 615, confidence 1 (no page dates the Median conquest of Persia; 'Phraortes subjugated the Persians' is on the Median dynasty page, undated). Page: https://en.wikipedia.org/wiki/Anshan_(Persia)
- `/ledger/6`: Anatolia to the Halys at 600, confidence 1: the Median dynasty page names the Halys but gives no year; the Halys border was fixed in 585 (Lydia dossier). Page: https://en.wikipedia.org/wiki/Battle_of_the_Eclipse

Spot checks:
- `/ledger/9 and /ledger/10` https://en.wikipedia.org/wiki/Median_dynasty: confirmed: 'In 550 BC, the Median capital, Ecbatana, was conquered by the Persian king Cyrus II'
- `/ledger/3` https://en.wikipedia.org/wiki/Median_dynasty: confirmed: 'By 612 BC, the Medes became strong enough to overthrow the declining Assyrian empire in alliance with the Babylonians.'
- `/ledger/7` https://en.wikipedia.org/wiki/Medes: confirmed: 'In 553 BCE, Cyrus the Great, the King of Persia, a Median vassal, revolted against the Median king.'
- `/ledger/2 and /ledger/4` https://en.wikipedia.org/wiki/Medes: confirmed: 'destroyed the strife-riven Neo-Assyrian Empire between 616 and 609 BCE'
- `/ledger/6` https://en.wikipedia.org/wiki/Medes: confirmed (undated, as the note says): 'to the Kızılırmak River in Anatolia'

## achaemenid-empire: thin

Area: infobox 5500000 km2 (-500), Cliopatria 5552560 km2, ratio 1.01. Infobox '500 BC: 5,500,000 km2' against achaemenid-empire_-500; matches the author's figure.

Findings:
- `/ledger/32/region, /ledger/33/region, /ledger/34/region, /keyframe_review/7/correction` (applied by reviewer): The Cyprus sub-region carried the text 'Cyprus, seized from Amasis II before the Egyptian campaign', copied from the 525 event into the 387 treaty, the 350-343 revolt and the 383 keyframe. Evidence: The quote belongs to /ledger/10 (Cambyses II page); the King's Peace and the Artaxerxes III events do not say it. Fix: Nested text set to 'Cyprus' in the four places; /ledger/10 unchanged.
- `/ledger/11` (applied by reviewer): Vassal_start of Cyrene and Barca at 525 at confidence 1 with 'Page undated', but the Cyrenaica page dates it. Evidence: Cyrenaica page: 'In 525 BC, after conquering Egypt, the Achaemenid (Persian) army of Cambyses II seized the Pentapolis'. Fix: Source set to the Cyrenaica page (added to sources[]), confidence 2, note rewritten with the quote. The type and counterpart still disagree with greek-city-states /ledger/15 (a loss of Cyrenaica to this state, 'established a satrapy'): see cross_checks.
- `/keyframe_review/6/correction and /ledger (missing 412)` (for the author): The 404 correction removes Ionia ('Ionia is still out until 387') and the ledger has no Persian gain in Ionia before 387, but delian-league /ledger/23 books 'the Persian reconquest of most of Ionia' in 412 as a loss to this state (confidence 3). Evidence: Peloponnesian War page (opened by the reviewer): 'In 412 BC, this led to the Persian reconquest of most of Ionia.' Against it, this dossier's Peace of Antalcidas page ('the return of firm Persian control over Ionia') and greek-city-states /ledger/22-23 (Ionian cities gained from the League in 404, lost to Persia in 387). Fix: Not blocking: a source conflict between neighbours. Either add a 412 gain of Ionia from delian-league (confidence 2) and drop Ionia from the 404 correction, or keep 387 and have delian-league /ledger/23 changed; the orchestrator picks one model for the three dossiers.
- `/identity/rulers/1..9` (for the author): Nine of the ten rulers carry no source. Evidence: Brief section 2.9: rulers cite a page. Cyrus (/identity/rulers/0) cites the Achaemenid Empire page; the rest have none. Fix: Add the page each reign comes from (the Achaemenid Empire infobox gives only the first and last king).
- `/ledger/40/region/text` (for the author): The text says 'Syria, Phoenicia and Palestine with the Cilician coast' but the geometry (333 outline minus 331 outline minus Egypt) also carries the Libyan strip regained in 343. Evidence: Cliopatria achaemenid-empire_-333 reaches 18.73E (Cyrenaica); _-331 starts at 37.65E; /ledger/35 gains the Thirtieth Dynasty's Libyan coast and no other event loses it. macedonian-empire /ledger/26 gains Cyrenaica in 332. Fix: Add 'and the Libyan coast' to the text.

Gaps for a gap-filler:
- `/ledger (missing 479)`: No loss of Chios, Lesbos and Samos after Mycale; greek-city-states /ledger/17 gains 'the Aegean islands freed at Mycale' from this state in 479. Page: https://en.wikipedia.org/wiki/Battle_of_Mycale
- `/wars/7`: First Persian invasion of Greece has empty zones; the 490 campaign took Naxos and Eretria and the Cyclades (check and add zones, or say no ground was held). Page: https://en.wikipedia.org/wiki/First_Persian_invasion_of_Greece
- `/ledger/7 and /ledger/13`: The east (540) and the Indus (515) are gained from 'nobody', while janapada-of-gandhara (/ledger/1 loss 535, /ledger/2 dissolve 518) and janapada-of-kamboja (/ledger/1 loss 530, /ledger/2 dissolve 501) name this state; years differ by 3-5. Page: https://en.wikipedia.org/wiki/Achaemenid_conquest_of_the_Indus_Valley
- `/ledger/5`: Cilicia at 542, confidence 1 (page silent). Page: https://en.wikipedia.org/wiki/Cilicia
- `/ledger/8`: Phoenicia at 539, confidence 1 (phoenicia /ledger/8 has 539 at confidence 2: cite its page). Page: https://en.wikipedia.org/wiki/Phoenicia
- `/ledger/21`: Macedonian vassalage ends 479, confidence 1 (macedonian-empire /ledger/2 has 479 at confidence 3: 'Incorporated into the Persian Empire: 492-479 BC'). Page: https://en.wikipedia.org/wiki/Macedonia_(ancient_kingdom)
- `/ledger/30`: Cyrene and Barca vassal_end 404, confidence 1. Page: https://en.wikipedia.org/wiki/Cyrene,_Libya
- `/ledger/31`: Indus lost 404, confidence 1 (Cliopatria only). Page: https://en.wikipedia.org/wiki/Achaemenid_conquest_of_the_Indus_Valley
- `/ledger/33`: Phoenician and Cypriot revolt dated 350, confidence 1 (page: 'soon after' 351). Page: https://en.wikipedia.org/wiki/Sidon
- `/ledger/37 and /ledger/38`: Western Anatolia lost 333, confidence 1: which satrapies fell after Granicus (334) and Issus (333). Page: https://en.wikipedia.org/wiki/Battle_of_the_Granicus
- `/ledger/40`: Levant lost 332, confidence 1: Tyre and Gaza 332 are on macedonian-empire /ledger/25-26. Page: https://en.wikipedia.org/wiki/Siege_of_Tyre_(332_BC)
- `/ledger/43`: Ecbatana 330, confidence 1. Page: https://en.wikipedia.org/wiki/Darius_III
- `/keyframe_review/5..7`: The Persian position in Ionia 412-387 and Cyprus under Evagoras (about 391-381) are unsettled (author's own gap). Page: https://en.wikipedia.org/wiki/Ionia

Spot checks:
- `/ledger/2` https://en.wikipedia.org/wiki/Cyrus_the_Great: confirmed: 'Cyrus occupied the capital at Sardis, conquering the Lydian kingdom in 546 BC.' (infobox 547 noted by the author)
- `/ledger/3` https://en.wikipedia.org/wiki/Cyrus_the_Great: confirmed: 'Commagene was incorporated into Persia in 546 BC.'
- `/ledger/4 and /ledger/6` https://en.wikipedia.org/wiki/Cyrus_the_Great: confirmed: 'He ended his conquest of the area in 542 BC'; 'By the year 540 BC, Cyrus captured Elam and its capital, Susa.'
- `/ledger/12` https://en.wikipedia.org/wiki/Twenty-seventh_Dynasty_of_Egypt: confirmed: 'defeated by Cambyses II at the Battle of Pelusium in the eastern Nile Delta in May of 525'
- `/ledger/13` https://en.wikipedia.org/wiki/Darius_the_Great: confirmed: 'Darius conquered the lands surrounding the Indus River in 515 BCE.'
- `/ledger/20 and /ledger/22` https://en.wikipedia.org/wiki/Greco-Persian_Wars: confirmed: 'expelling Persian garrisons from Sestos in 479 BC and from Byzantium in 478 BC.'
- `/ledger/24` https://en.wikipedia.org/wiki/Greco-Persian_Wars: confirmed: 'In 466 BC, the League achieved a double victory in the Battle of the Eurymedon, which completely liberated Ionia.'
- `/ledger/29` https://en.wikipedia.org/wiki/Twenty-seventh_Dynasty_of_Egypt: confirmed: 'a satrapy of the Achaemenid Empire between 525 and 404 BC'; Amyrtaeus expelled the Persians from Memphis in 405
- `/ledger/35` https://en.wikipedia.org/wiki/Achaemenid_Empire: confirmed: infobox 'Reconquest of Egypt: 343 BC'

## kingdom-of-bithynia: thin

Area: infobox None km2 (None), Cliopatria 30213 km2, ratio None. The infobox has no Area field (checked); every keyframe note says so.

Gaps for a gap-filler:
- `/ledger/2`: The 279 growth (11,900 km2) is a confidence-1 bridge from the Seleucid outline; no page dates it. Page: https://en.wikipedia.org/wiki/Nicomedes_I_of_Bithynia
- `/ledger/4`: Byzantium's Asiatic territory seized in 220 (confirmed on the Prusias I page), but the peace of 219 that ended the Byzantine-Rhodian war may have returned it (Polybius); check and add a 219 loss if so. The place (Chalcedon) is the researcher's reading. Page: https://en.wikipedia.org/wiki/Prusias_I_of_Bithynia
- `/ledger (missing)`: Prusias I's undated gains from Heraclea Pontica (Cierus renamed Prusias) and his wars with Attalus I; the 183 peace with Eumenes II at Cyzicus. Both are on the Prusias I page without years. Page: https://en.wikipedia.org/wiki/Prusias_I_of_Bithynia
- `/ledger/6 and /ledger/7`: Paphlagonia occupied 127-94 at confidence 1; the partition with Mithridates VI is undated on the pages opened and is usually placed about 108 BC. Page: https://en.wikipedia.org/wiki/Paphlagonia
- `/ledger/0`: Found 333, confidence 1 (Cliopatria's year; 'established in the 4th century BC'). Page: https://en.wikipedia.org/wiki/Bas_of_Bithynia
- `/identity/rulers`: No ruler list (the author's own gap). Page: https://en.wikipedia.org/wiki/Kingdom_of_Bithynia

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Kingdom_of_Bithynia: confirmed: 'assumed the Greek title basileus (meaning "king") in 297 BC'
- `/ledger/4` https://en.wikipedia.org/wiki/Prusias_I_of_Bithynia: confirmed: 'he fought a war against Byzantium in 220 BC, seizing its Asiatic territory.'
- `/ledger/5` https://en.wikipedia.org/wiki/Prusias_I_of_Bithynia: confirmed: 'Philip V granted him the cities of Kios and Myrleia in 202 BC.'
- `/ledger/8` https://en.wikipedia.org/wiki/Kingdom_of_Bithynia: confirmed: 'Mithridates VI invaded Bithynia, defeating Nicomedes IV in 90 BC, annexing his kingdom.'
- `/ledger/10` https://en.wikipedia.org/wiki/First_Mithridatic_War: confirmed: 'captured Bythinia without opposition'; the same paragraph: 'This swift conquest of Asia through Phrygia took place in early 88.'
- `/ledger/12` https://en.wikipedia.org/wiki/Kingdom_of_Bithynia: confirmed: infobox 'Nicomedes IV bequeathed the Kingdom of Bithynia to the Roman Republic: 74 BC'

## cyrenaica: fail

Area: infobox None km2 (None), Cliopatria 116348 km2, ratio None. The infobox has no area (checked). Magas' shape is 3.5 times the Pentapolis; this is said in the keyframe note and bridged at confidence 1.

Findings:
- `/keyframe_review/0/correction, /ledger/1, /ledger/3` (for the author): The dossier draws Cyrenaica as its own state 331-305 with no event putting it under Ptolemy, although its own source makes it Ptolemaic before the 305 revolt; the 300 loss 'passes back to Ptolemy I's Egypt' with no earlier Ptolemaic holding in the ledger. Evidence: Magas of Cyrene page (opened by the reviewer): 'The predecessor of Magas in Cyrene, the Ptolemaic governor named Ophellas'; infobox 'Predecessor: Ophellas (until 308 BC)'; the dossier itself quotes 'Ptolemy exercised direct control over Cyrene' after 308. macedonian-empire /ledger/43, /46, /49 give 'Egypt and Libya' (Cyrenaica named) to ptolemaic-kingdom in 323/321. Fix: Add a loss (or vassal_start) to ptolemaic-kingdom at 308 at the latest (confidence 2, Magas page), or at 322 at confidence 1 for Ophellas' appointment; make 305 the revolt (gain from ptolemaic-kingdom with the contest_start), keep the 300 contest_end and loss; correct keyframe 0's text to the years the land was not Ptolemaic.
- `/ledger/8, /ledger/9, /identity/end, /keyframe_review/2` (for the author): The 96 loss to roman-republic and dissolve disagree with roman-republic, which books Cyrenaica as a vassal from 96 and annexes it from cyrenaica in 74, after this dossier has ended. Evidence: roman-republic /ledger/125 vassal_start cyrenaica -96 (confidence 2: 'Rome accepted it but preferred to leave administration to local rulers'), /ledger/154 gain from cyrenaica -74 (confidence 3), /ledger/155 vassal_end -74. Cyrenaica page: 'by 78 BC it was organized as one administrative province together with Crete'; infobox 'Roman province (74 BC-643 AD)'. Fix: Recommended: turn /ledger/8 into a vassal_start with roman-republic at 96 (confidence 3), move the end to 74 with a loss to roman-republic and the dissolve, and end keyframe 2 in 75; or the orchestrator keeps 96 and roman-republic drops its vassal pair and takes the land at 96.
- `/ledger/0` (for the author): Found at 331 with counterpart nobody, while macedonian-empire /ledger/26 books Cyrenaica as a gain from achaemenid-empire in 332 and achaemenid-empire /ledger/40's geometry loses the Libyan coast in 332. Evidence: Cyrenaica page: 'The Persians were followed by Alexander the Great in 332 BC, who received tribute from the cities after taking Egypt.' The dossier's own note calls it 'a vassal event for the Macedonian Empire's dossier', but no vassal event exists on either side. Fix: Add vassal_start of macedonian-empire at 331 (confidence 2) here and ask eu-02 to turn the Cyrenaica part of macedonian-empire /ledger/26 into the matching vassal_start.

Gaps for a gap-filler:
- `/ledger/6`: Reunion with Egypt at 247, confidence 1: Magas died 250, Demetrius the Fair and Berenice II follow, no year for the reunion on the pages. Page: https://en.wikipedia.org/wiki/Berenice_II
- `/ledger/7`: Ptolemy Apion's separate kingdom at 110, confidence 1 (Cliopatria's year). Page: https://en.wikipedia.org/wiki/Ptolemy_Apion
- `/ledger/5`: Hinterland of Magas' kingdom (62,000 km2 beyond the Pentapolis), confidence 1. Page: https://en.wikipedia.org/wiki/Magas_of_Cyrene
- `/certainty/0`: No Carthaginian frontier (Altars of the Philaeni). Page: https://en.wikipedia.org/wiki/Arae_Philaenorum

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Cyrenaica: confirmed: 'Alexander the Great in 332 BC, who received tribute from the cities after taking Egypt'
- `/ledger/1` https://en.wikipedia.org/wiki/Magas_of_Cyrene: confirmed: 'Shortly after Ptolemy declared himself king (c.305 BC), the Cyrenaeans rebelled.'
- `/ledger/2` https://en.wikipedia.org/wiki/Magas_of_Cyrene: confirmed: 'Around 300 BC, Ptolemy dispatched Magas, then about 20 years old, to reconquer Cyrene.'
- `/ledger/4` https://en.wikipedia.org/wiki/Magas_of_Cyrene: confirmed: infobox 'Reign: 276-250 BC' as King of Cyrene; dates 283-280 and 276/274 discussed
- `/ledger/8` https://en.wikipedia.org/wiki/Cyrenaica: confirmed: 'dying without heirs in 96 BC, bequeathed it to the Roman Republic'

## Cross-dossier matrix

- exception: median-kingdom -615 vassal_start (Persia (kingdom of Anshan)) <-> -. Was achaemenid-empire (before its start); reviewer set the non-slug counterpart. Dossier suggested: kingdom-of-anshan.
- missing: median-kingdom -615 contest_start (neo-assyrian-empire) <-> neo-assyrian-empire. neo-assyrian-empire has no contest pair with median-kingdom (it has losses only).
- mismatch: median-kingdom -612 gain (neo-assyrian-empire) <-> neo-assyrian-empire -614 loss. NA /ledger/55: Assur lost to the Medes in 614 (c2); NA /ledger/56 gives the heartland to neo-babylonian-empire in 612. Median gains a Zagros strip in 612 and never Assur.
- missing: median-kingdom -609 contest_end (neo-assyrian-empire) <-> neo-assyrian-empire. No contest_end on the Assyrian side.
- exception: median-kingdom -600 gain (Manna (Mannaean states)) <-> -. No dossier (author lists manna). The Scythians page dates the Mannai annexation to 616.
- missing: scythia -600 loss (median-kingdom) <-> median-kingdom. scythia /ledger/8 loses Sakez near Lake Urmia and Urartu to the Medes; median-kingdom books the same area as a gain from Manna and has no Urartu.
- mismatch: scythia -652 vassal_start (median-kingdom) <-> median-kingdom. scythia /ledger/4 (652) and /ledger/6 (625) put Media under Scythian hegemony before median-kingdom's start (-615); needs a mirror only if the Median life is extended back.
- missing: lydia -590 contest_start (median-kingdom) <-> median-kingdom. lydia /ledger/8-9 contest 590-585 (Halys border); no Median contest pair.
- exception: median-kingdom -600 gain (Anatolian peoples east of the Halys) <-> -. Non-slug counterpart.
- exception: median-kingdom -553 contest_start (Persia (kingdom of Anshan)) <-> -. Was achaemenid-empire; changed with /ledger/7 and /ledger/9.
- matched: median-kingdom -550 loss (achaemenid-empire) <-> achaemenid-empire -550 gain. achaemenid /ledger/1 (c3) and /ledger/0 found.
- matched: achaemenid-empire -546 gain (lydia) <-> lydia -546 loss. lydia /ledger/13 (c3). lydia /ledger/11-12 also has a contest 547-546 with achaemenid-empire that this ledger lacks.
- mismatch: achaemenid-empire -542 gain (greek-city-states) <-> greek-city-states -547 loss. GCS /ledger/12 takes Ionia in 547 ('conquest of all the Ionian cities in 547 BC'); Cyrus page: Harpagus ended the conquest in 542. Five years apart; pick one.
- matched: achaemenid-empire -540 gain (elam) <-> elam -539 dissolve. elam /ledger/32 (c2).
- mismatch: achaemenid-empire -540 gain (nobody) <-> janapada-of-kamboja -530 loss. Kamboja /ledger/1 (530, c1) and janapada-of-gandhara /ledger/1 (535, c2) lose land to achaemenid-empire; this ledger names nobody.
- matched: achaemenid-empire -539 gain (phoenicia) <-> phoenicia -539 loss. phoenicia /ledger/8-9 (c2); this side is c1.
- matched: achaemenid-empire -539 gain (neo-babylonian-empire) <-> neo-babylonian-empire -539 dissolve. NBE /ledger/12 (c3).
- mismatch: achaemenid-empire -525 gain (twenty-sixth-dynasty-of-egypt) <-> twenty-sixth-dynasty-of-egypt -545 loss. Cyprus: 26th /ledger/5 dates the loss to 545 (Cyprus page), this dossier 525 (Cambyses II page). Flagged by the author.
- mismatch: achaemenid-empire -525 vassal_start (cyrene-and-barca) <-> greek-city-states -525 loss. GCS /ledger/15 books Cyrenaica as a loss to achaemenid-empire ('seized the Pentapolis', 'established a satrapy'); this side is a vassal of a counterpart with no dossier. One model for both.
- matched: achaemenid-empire -525 gain (twenty-sixth-dynasty-of-egypt) <-> twenty-sixth-dynasty-of-egypt -525 loss. 26th /ledger/6-7 (c3). But twenty-seventh-dynasty-of-egypt /ledger/1 draws Egypt 525-404 as an occupation by achaemenid-empire: Egypt drawn twice (author flagged).
- mismatch: achaemenid-empire -515 gain (nobody) <-> janapada-of-gandhara -518 dissolve. Gandhara /ledger/2 ends in 518 into achaemenid-empire; this side 515 from nobody.
- matched: achaemenid-empire -512 vassal_start (macedonian-empire) <-> macedonian-empire -512 vassal_start. macedonian /ledger/1.
- missing: achaemenid-empire -499 contest_start (greek-city-states) <-> greek-city-states. Ionian Revolt 499-493 and the occupation 480-479 (/ledger/16-19) have no mirror in greek-city-states.
- mismatch: achaemenid-empire -479 loss (greek-city-states) <-> greek-city-states -479 gain. GCS /ledger/17 gains the Aegean islands (Chios, Lesbos, Samos) at Mycale; this side loses only Sestos (and Byzantium 478, which GCS does not gain).
- matched: achaemenid-empire -479 vassal_end (macedonian-empire) <-> macedonian-empire -479 vassal_end. macedonian /ledger/2.
- mismatch: achaemenid-empire -466 loss (greek-city-states) <-> greek-city-states. No 466 gain in GCS; delian-league /ledger/1 already counts Ionia among its allies from 478, so Ionia is Persian and League-tinted 478-466.
- missing: delian-league -412 loss (achaemenid-empire) <-> achaemenid-empire. DL /ledger/23 (c3, Peloponnesian War page, confirmed by the reviewer): Persian reconquest of most of Ionia in 412. achaemenid-empire keeps Ionia out until 387 (keyframe 6), as greek-city-states does.
- mismatch: achaemenid-empire -460 contest_start (revolt-of-inaros-ii) <-> revolt-of-inaros-ii -460 contest_start. Inaros' contest pair names twenty-seventh-dynasty-of-egypt, not achaemenid-empire (Egypt model).
- mismatch: achaemenid-empire -404 loss (twenty-eighth-dynasty-of-egypt) <-> twenty-eighth-dynasty-of-egypt -404 found. 28th /ledger/0 founds from twenty-seventh-dynasty-of-egypt; twenty-seventh /ledger/9 ends the occupation by achaemenid-empire in 404 (Egypt model).
- matched: achaemenid-empire -387 gain (greek-city-states) <-> greek-city-states -387 loss. GCS /ledger/23 (c3).
- matched: achaemenid-empire -343 gain (thirtieth-dynasty-of-egypt) <-> thirtieth-dynasty-of-egypt -343 loss. 30th /ledger/3-5. thirty-first-dynasty-of-egypt /ledger/1 again draws 343-332 as an occupation (Egypt model).
- missing: achaemenid-empire -334 contest_start (macedonian-empire) <-> macedonian-empire. Macedonian side has gains, no contest pair.
- matched: achaemenid-empire -333 loss (macedonian-empire) <-> macedonian-empire -334 gain. macedonian /ledger/23-24 (334, 333).
- matched: achaemenid-empire -332 loss (macedonian-empire) <-> macedonian-empire -332 gain. macedonian /ledger/25-26; /ledger/26 includes Cyrenaica, which cyrenaica founds in 331 with counterpart nobody.
- matched: achaemenid-empire -331 loss (macedonian-empire) <-> macedonian-empire -331 gain. macedonian /ledger/30.
- matched: achaemenid-empire -330 loss (macedonian-empire) <-> macedonian-empire -330 gain. macedonian /ledger/31-32.
- mismatch: achaemenid-empire -330 split (bessus-artaxerxes-v) <-> macedonian-empire -329 gain. macedonian /ledger/33 gains Bactria and Sogdia from achaemenid-empire in 329, after its end (330); should name bessus-artaxerxes-v (no dossier yet) or nobody. Flagged by the author.
- mismatch: moab -400 dissolve (achaemenid-empire) <-> achaemenid-empire. Neighbour side: moab /ledger/9 ends into achaemenid-empire c. 400; this dossier holds the Levant from 539, so no event is needed here; moab's counterpart is the issue.
- mismatch: kingdom-of-bithynia -333 found (achaemenid-empire) <-> achaemenid-empire -333 loss. Land: achaemenid /ledger/37 (337 outline minus 333 outline) gives the same Bithynian cells to macedonian-empire in 333.
- exception: kingdom-of-bithynia -279 gain (seleucid-empire) <-> -. seleucid-empire not written yet (me-05, later part).
- exception: kingdom-of-bithynia -220 gain (Byzantium) <-> -. No dossier; listed by the author.
- exception: kingdom-of-bithynia -202 gain (antigonid-macedonia) <-> -. polities.csv row, dossier not written yet.
- exception: kingdom-of-bithynia -127 occupation_start (paphlagonia) <-> -. paphlagonia not written yet (me-05).
- exception: kingdom-of-bithynia -90 occupation_start (kingdom-of-pontus) <-> -. kingdom-of-pontus not written yet (me-05); also /ledger/9-11.
- matched: kingdom-of-bithynia -74 loss (roman-republic) <-> roman-republic -74 gain. roman /ledger/153 (c3).
- mismatch: cyrenaica -331 found (nobody) <-> macedonian-empire -332 gain. macedonian /ledger/26 gains Cyrenaica from achaemenid-empire in 332, /ledger/43-49 passes it to ptolemaic-kingdom 323/321; cyrenaica is its own state 331-305.
- exception: cyrenaica -305 contest_start (ptolemaic-kingdom) <-> -. ptolemaic-kingdom not written yet (me-05); also /ledger/2-7.
- mismatch: cyrenaica -96 loss (roman-republic) <-> roman-republic -96 vassal_start. roman /ledger/125 vassal_start 96, /ledger/154 gain from cyrenaica 74, /ledger/155 vassal_end 74: the Roman dossier needs cyrenaica alive to 74.

## Problems

- Byzantine-Rhodian war page would not load (URL_NOT_FOUND for two spellings); the possible 219 restitution of Byzantium's Asiatic land by Prusias I is left as a thin item, unverified.
- Egypt model conflict (author flagged): achaemenid-empire draws Egypt 525-404 and 343-332 as its own land; twenty-seventh-dynasty-of-egypt, thirty-first-dynasty-of-egypt, revolt-of-inaros-ii and twenty-eighth-dynasty-of-egypt (me-03) draw it as an occupation of the Egyptian dynasty. One model must win before rendering.
- Ionia 412-387: delian-league (412 Persian reconquest, c3) disagrees with greek-city-states and achaemenid-empire (Persian only from 387). Orchestrator to choose.
- Cyrenaica 525-331: greek-city-states, achaemenid-empire (now c2 vassal of cyrene-and-barca), macedonian-empire (gain 332) and cyrenaica (found 331, nobody) disagree on who holds it; the cyrene-and-barca dossier would decide it.
- Reviewer applied small fixes in place (median-kingdom counterparts and notes; achaemenid-empire Cyprus texts and /ledger/11 source and confidence); both re-validate with 0 errors and were read back after writing.
