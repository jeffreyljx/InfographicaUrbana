# Review of batch sa-03-a

Reviewer run of 2026-10-19 (adversarial review, Phase B). The machine copy is history/notes/phase-b/reviews/sa-03-a.json.

Validator: all seven dossiers valid, no errors. Warnings only for counterparts with no dossier yet (eastern-chalukyas, pushyabhuti-dynasty, hindu-shahis). None of the seven Wikipedia pages has an infobox area, so no area ratio could be computed.

## chalukya-dynasty: thin

Findings:
- [for the author] `/ledger/4`: The 626 gain from vishnukundina-dynasty gains again the Vengi land (Andhra Pradesh minus the later shapes) already gained at /ledger/2 in 616, and is two years after the neighbour's end. Evidence: vishnukundina-dynasty /ledger/4 dissolves in 624 (confidence 3) with chalukya-dynasty as counterpart; /ledger/2 and /ledger/4 here carry the same Andhra region; the Pulakeshin II page dates neither the Kunala battle nor the conquest. Fix: Keep only Telangana in /ledger/4 and date it 624 to meet vishnukundina /ledger/4, or say in the note why 626.
- [for the author] `/ledger`: No vassal events for the Western Gangas, though their dossier makes them Chalukya feudatories. Evidence: western-ganga-dynasty /ledger/6 vassal_start 550 and /ledger/7 vassal_end 753 name chalukya-dynasty; Pulakeshin II page: 'the Gangas again accepted the Chalukya suzerainty' (no year); the Chalukya page lists 'the Gangas' among the feudatories. Fix: Add vassal_start (counterpart western-ganga-dynasty, year agreed with the neighbour, at or after 543) and vassal_end 753.
- [for the author] `/ledger`: No event for the Nala land, though nala-dynasty dissolves to this state. Evidence: nala-dynasty /ledger/3: dissolve c. 580, counterpart chalukya-dynasty ('Kirtivarman I destroys the Nalas', Aihole); the Chalukya page does not mention the Nalas. Fix: Add a confidence-1 gain or vassal_start c. 580 from nala-dynasty (Kirtivarman I page), or tell the nala-dynasty owner to change its counterpart; Cliopatria's 555-601 shape stops at 81 E, short of Bastar.
- [for the author] `/ledger/7`: The 633 gain draws all of Madhya Pradesh and the whole Gujarat region, including Saurashtra (the Maitraka core), well beyond the keyframe. Evidence: Keyframe /keyframe_review/6 (633, verdict ok) has a north edge at 22.9 N (shapes.csv bbox); Madhya Pradesh reaches 26.9 N; maitraka-dynasty holds Saurashtra to 776; the Pulakeshin II page has only Lata under a Chalukya governor (643 Kheda plate). Fix: Wrap the region in {"intersect": [{"cliopatria": "Chalukya Dynasty", "year": 633}, ...]}.
- [for the author] `/keyframe_review/12, /keyframe_review/13, /ledger/19`: The 753 loss of the north (about 600,000 km2) falls inside keyframe 750, which runs to 754, and no keyframe covers 757, the year of the dissolve. Evidence: /keyframe_review/12 keeps the 750 shape (minus Madhya Pradesh and Gujarat) for 750-754; /ledger/19 removes the rest in 753 (Dantidurga page: 'defeated the Chalukyas in 753'); /keyframe_review/13 is the Cliopatria 755 shape, 755-756; /ledger/21 dissolves in 757 ('retained control over his southern provinces up to the year 757'). Fix: Set /keyframe_review/12 to=752 and give the 755 shape from=753 to=757 (a new keyframe or from/to on /keyframe_review/13).

Gaps for a gap-filler:
- `/ledger/1`: 602 Pallava border step at confidence 1; no page dates it (try https://en.wikipedia.org/wiki/Mahendravarman_I)
- `/ledger/3`: 623 Maharashtra step at confidence 1 (Kalachuri dossier has c. 625) (try https://en.wikipedia.org/wiki/Kalachuris_of_Mahishmati)
- `/ledger/5, /ledger/6, /ledger/11, /ledger/20`: Kalinga and Dakshina Kosala vassalage, years bridged at confidence 1; the Kosala counterpart should be a slug (panduvamshi-dynasty) once written (try https://en.wikipedia.org/wiki/Panduvamshis_of_Dakshina_Kosala)
- `/ledger/7`: 633 Lata/Malava/Gurjara submission undated (confidence 1) (try https://en.wikipedia.org/wiki/Gurjaras_of_Lata)
- `/ledger/16, /ledger/17`: Vikramaditya II's Kanchi campaign at confidence 1 (try https://en.wikipedia.org/wiki/Nandivarman_II)
- `/keyframe_review/7, /keyframe_review/8`: 642-655 interregnum: how far the Pallava occupation reached beyond Vatapi (try https://en.wikipedia.org/wiki/Narasimhavarman_I)

Spot checks: /ledger/9 confirmed; /ledger/10 confirmed; /ledger/13 confirmed; /ledger/19 confirmed; /ledger/2 confirmed; /ledger/21 confirmed; /ledger/8 confirmed.

## maukhari-dynasty: thin

Findings:
- [for the author] `/keyframe_review/0-2, /ledger, /ledger/4`: Magadha is drawn Maukhari from 554 to 606, against the Later Gupta dossier, which has the Maukharis take it c. 575 and lose it back c. 606. Evidence: later-gupta-dynasty /ledger/3 loss 575 and /ledger/7 gain 606 name maukhari-dynasty ('Sharvavarman invaded Magadha circa 575 CE', Later Gupta page); this dossier has no 575 gain and dissolves all its land to harsha-s-empire; the Maukhari page dates neither (author flagged 'unverified, page budget'). Fix: Cut Magadha from the 554-574 keyframes, add a 575 gain of Magadha with counterpart later-gupta-dynasty, and give Magadha to later-gupta-dynasty in 606 (the rest to harsha-s-empire).
- [for the author] `/ledger/2`: The counterpart 'Devagupta of Malwa' is the Later Gupta Devagupta, whose state already has a dossier; the report asks for a new 'later-guptas-of-malwa'. Evidence: later-gupta-dynasty /ledger/6: 'He defeated Devagupta, Mahasenagupta's son and successor in Malwa' (605); the Maukhari page: Grahavarman 'was killed in battle by Devagupta of Malwa'. Fix: Set counterpart later-gupta-dynasty (consider occupation_start rather than loss: Kannauj was held for months before Harsha), and drop the later-guptas-of-malwa request.

Gaps for a gap-filler:
- `/keyframe_review/0`: Magadha 554-575 and the reign years of four kings (try https://en.wikipedia.org/wiki/Later_Gupta_dynasty)
- `/ledger/4`: 606-611: who held Kannauj before Harsha's Cliopatria start (612) (try https://en.wikipedia.org/wiki/Harsha)

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed.

## turk-shahis: thin

Findings:
- [applied by reviewer] `/ledger/3`: Confidence 3 on a treaty year the page does not give. Evidence: Turk Shahi page: the treaty followed Ubayd Allah ibn Abi Bakra's appointment 'in 673'; the treaty itself is undated. Fix: Lowered to 2 by the reviewer (note appended).
- [applied by reviewer] `/ledger/2`: The 666 Gandhara gain named western-gokturks, a state its own dossier ends in 657. Evidence: western-gokturks identity end 657 (dissolve to tang-dynasty); alchon-huns /ledger/19: '625: The Western Turks took Khuttal and Kapisa-Gandhara, establishing the Yabghus of Tokharistan'; Turk Shahi page: Tong Yabghu's Turks 'occupied Gandhara as far as the Indus River from circa 625 AD'. Fix: Counterpart set to tokhara-yabghus by the reviewer (note appended); tokhara-yabghus needs the matching 666 loss (routed in cross_checks).
- [applied by reviewer] `/wars/0, /wars/4`: Two wars ran outside the life (653-673 and 870-878 for a state of 665-870). Evidence: identity start 665, end 870. Fix: Clamped by the reviewer to 665-673 and 870-870.
- [for the author] `/ledger/11, /ledger/12, /keyframe_review/10`: The state renamed in 822 does not end in 870: the dossier records a capital move to Udabhandapura in the year it dissolves, to a capital it never holds. Evidence: Hindu Shahi infobox 'Kabul (822-870); Udabhandapura (870-1001)'; 'founded by Kallar in c. 822 CE after overthrowing Lagaturman'; Turk Shahi infobox 665-822. The one-state rule keeps a dynasty change on the same land as a rename. Fix: Settle the split with sa-03-x, who write the Shahis: either end this dossier in 822 (rename becomes dissolve to hindu-shahis, shapes 822-874 marked wrong) or keep the 870 split and drop /ledger/11; record the choice in notes.
- [for the author] `/ledger/4`: The 680 loss to zunbils gives away Zabulistan and Arachosia, but zunbils' found takes Zabulistan only and gains Arachosia from 'nobody' in 692. Evidence: zunbils /ledger/0 region Zabulistan; zunbils /keyframe_review/0 adds Turk Shahis 682 ∩ Arachosia; zunbils /ledger/1 (692, confidence 1) counterpart nobody. Fix: Make the two sides name the same land: either this loss is Zabulistan only, or the zunbils found carries its 680 keyframe region.

Gaps for a gap-filler:
- `/ledger`: No vassal events for Yabghu suzerainty over Kabul and Zabul (tokhara-yabghus /ledger/5-6, 718-758; Turk Shahi page: Chinese sources 'describe the Kabul Turks as vassals of the Yabghus of Tokharistan'), nor for the Tang titles and the al-Mahdi submission c. 775-785 (try https://en.wikipedia.org/wiki/Tokhara_Yabghus)

Spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/3 confirmed with the year softened; /ledger/5 confirmed; /ledger/9 confirmed; /ledger/10 confirmed; /ledger/11 confirmed.

## karkota-dynasty: thin

Gaps for a gap-filler:
- `/keyframe_review/4-7`: Gilgit (Little Palur) inside the 656-849 shapes: Patola Shahi, then Tibetan (737) and Tang (747) per the dossier's own war; the +4,000 km2 step of 751 is unexplained (try https://en.wikipedia.org/wiki/Patola_Shahis)
- `/wars/1`: Lalitaditya's campaigns: the Karkota page gives Stein and Sen ('mythology') against Goetz ('historical fact'); the Kannauj war with Yashovarman is the one most often accepted (try https://en.wikipedia.org/wiki/Yashovarman)

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed.

## pandya-dynasty: thin

Findings:
- [applied by reviewer] `/identity/rulers`: The ruler strip stopped at 880 (the note said later kings were not on the page) and Sendan overlapped Arikesari by ten years. Evidence: Pandya page table: Parantaka Viranarayana 'c. 880-900/905 CE', Maravarman Rajasimha II 'c. 900-920 CE'; Sendan 'c. 620-650 CE', Arikesari 'c. 640-670 CE'. Fix: Added by the reviewer: Parantaka Viranarayana 880-900, Maravarman Rajasimha II 900-915; Sendan cut to 640 with a note.
- [for the author] `/ledger`: No gain for the Kalabhra land that kalabhra-dynasty hands to this state in 601. Evidence: kalabhra-dynasty /ledger/3: dissolve 601, counterpart pandya-dynasty, region 'the middle Kaveri band that remained Kalabhra between the Pandya country and the Pallava frontier'; this dossier draws only the Cliopatria Pandya shape. Fix: Add a 601 gain from kalabhra-dynasty with that land (confidence 1), or have the kalabhra owner name late-pallava-empire or nobody.

Gaps for a gap-filler:
- `/ledger/0`: 592 found at confidence 1 (Kadungon c. 560-590 on the page) (try https://en.wikipedia.org/wiki/Kadungon)
- `/ledger/1`: 765 Kongu conquest reign-dated (confidence 1); counterpart is a name (try https://en.wikipedia.org/wiki/Kongu_Nadu)
- `/wars/2`: Sena II's sack of Madurai and the 9th-century Sinhalese wars have no events (anuradhapura war 833-862 names this state) (try https://en.wikipedia.org/wiki/Sena_II_of_Anuradhapura)

Spot checks: /ledger/4 confirmed; /ledger/5 confirmed; /ledger/3 confirmed; /ledger/2 confirmed as a proposal; /ledger/1 confirmed.

## gauda-kingdom: thin

Findings:
- [for the author] `/ledger/2, /ledger/0, /keyframe_review/0`: The 602 gain moves no land: the 554 found and the 554-601 keyframe already hold the whole Gauda 602 shape; its counterpart later-gupta-dynasty holds only Malwa in 575-604 and has no 602 loss. Evidence: /keyframe_review/0 correction = union(Gauda 602 shape, Maukhari 555 ∩ Bengal); later-gupta-dynasty keyframes 575 and 597 are Malwa only; Shashanka page: 'drove the later Guptas ... out of the region' after Mahasenagupta (c. 562-601), 'By 605 C.E. ... had established' the kingdom. Fix: Either cut the land taken in 602 out of the 554-601 keyframe and found (and name who held it), or recast /ledger/2 so it carries no land and no Later Gupta counterpart.
- [for the author] `/identity/predecessors/0, /ledger/0`: Found from gupta-empire, whose dossier dissolves in 554 to maukhari-dynasty and does not list gauda-kingdom among its successors. Evidence: gupta-empire /ledger/32: 554 dissolve, counterpart maukhari-dynasty; successors maukhari-dynasty, later-gupta-dynasty, pushyabhuti-dynasty. maukhari-dynasty cuts Bengal out of its 554 land. Fix: Route to the gupta-empire owner to name gauda-kingdom for Bengal, or take the found from maukhari-dynasty; record which in notes.

Gaps for a gap-filler:
- `/ledger/3`: Odisha expansion undated (confidence 1); the Shailodbhava plates of Kongoda acknowledge Shashanka (try https://en.wikipedia.org/wiki/Shailodbhava_dynasty)
- `/ledger/0`: Gauda before Shashanka (554-593): pages silent (try https://en.wikipedia.org/wiki/Gauda_(region))

Spot checks: /ledger/1 confirmed; /ledger/2 confirmed (undated); /ledger/3 confirmed (undated); /ledger/4 confirmed (undated).

## zunbils: thin

Findings:
- [applied by reviewer] `/wars/0, /wars/2`: Two wars ran outside the life (653-711 and 861-871 for a state of 680-870). Evidence: identity start 680, end 870. Fix: Clamped by the reviewer to 680-711 and 861-870.
- [for the author] `/ledger/0`: The found takes Zabulistan only, while turk-shahis /ledger/4 hands over Zabulistan and Arachosia and this dossier's own 680 keyframe adds Arachosia. Evidence: /keyframe_review/0 correction = union(Zabulistan, Turk Shahis 682 ∩ Arachosia); turk-shahis /ledger/4 region Zabulistan + Arachosia. Fix: Give /ledger/0 the /keyframe_review/0 region (or align with turk-shahis as agreed).

Gaps for a gap-filler:
- `/ledger/1`: 692 reach to Kandahar undated (confidence 1); Zunbils page: 'at times' Rakhwad and Bost (try https://en.wikipedia.org/wiki/Zunbils)
- `/ledger/2`: 866 Saffarid step not on the page (confidence 1); Ya'qub's campaigns of 865-870 (try https://en.wikipedia.org/wiki/Ya%27qub_ibn_al-Layth_al-Saffar)
- `/wars/0`: Arab wars (671 Bost, 698 Army of Destruction) have zones but no contest events (try https://en.wikipedia.org/wiki/Ubayd_Allah_ibn_Abi_Bakra)

Spot checks: /ledger/3 confirmed; /ledger/0 confirmed; /ledger/1 not on page as dated; /ledger/2 not on page.

## Cross-dossier matrix

- chalukya-dynasty 543 found (kadamba-empire) -> kadamba-empire 540 dissolve: mismatch. Three years apart; the Chalukya page: established 543, footnote 'c. 540' for the Kadamba takeover. One side should move (author flagged).
- chalukya-dynasty 602 gain (late-pallava-empire) -> late-pallava-empire 602 loss: matched. Both confidence 1.
- chalukya-dynasty 616 gain (vishnukundina-dynasty) -> vishnukundina-dynasty 616 loss: matched. 
- chalukya-dynasty 623 gain (kalachuris-of-mahishmati) -> kalachuris-of-mahishmati 625 dissolve: mismatch. Two years apart (author flagged).
- chalukya-dynasty 626 gain (vishnukundina-dynasty) -> vishnukundina-dynasty 624 dissolve: mismatch. Two years apart; the Chalukya gain also repeats the 616 Vengi land.
- chalukya-dynasty 626 vassal_start (Dakshina Kosala) -> none: exception. Name counterpart; the Panduvamshis have no dossier (nala-dynasty names panduvamshi-dynasty as a successor).
- chalukya-dynasty 633 gain (Malavas, Latas and Gurjaras) -> none: exception. Name counterpart; the region overreaches into maitraka-dynasty's Saurashtra (fix /ledger/7).
- chalukya-dynasty 641 loss (eastern-chalukyas) -> none: exception. Listed in counterparts_needing_dossiers (sa-03-x).
- chalukya-dynasty 753 loss (rashtrakuta-dynasty) -> none: exception. rashtrakuta-dynasty belongs to another sa-03 part not yet written; same for 750 loss and 757 dissolve.
- nala-dynasty 580 dissolve (chalukya-dynasty) -> chalukya-dynasty None None: missing. No Chalukya event for the Nala land.
- western-ganga-dynasty 550 vassal_start (chalukya-dynasty) -> chalukya-dynasty None None: missing. No Ganga vassal_start/vassal_end (550-753) in the Chalukya ledger.
- maukhari-dynasty 554 found (gupta-empire) -> gupta-empire 554 dissolve: matched. 
- maukhari-dynasty 585 vassal_start (pushyabhuti-dynasty) -> none: exception. Listed in counterparts_needing_dossiers.
- maukhari-dynasty 605 loss (Devagupta of Malwa) -> later-gupta-dynasty 605 loss: mismatch. Devagupta is later-gupta-dynasty's king (its /ledger/6); it has no Kannauj gain or occupation in 605.
- maukhari-dynasty 606 dissolve (harsha-s-empire) -> none: exception. harsha-s-empire is another sa-03 part not yet written (Cliopatria starts 612).
- later-gupta-dynasty 575 loss (maukhari-dynasty) -> maukhari-dynasty None None: missing. Magadha c. 575 has no Maukhari gain; Maukhari draws Magadha from 554.
- later-gupta-dynasty 606 gain (maukhari-dynasty) -> maukhari-dynasty 606 dissolve: mismatch. Maukhari dissolves all its land to harsha-s-empire; Magadha should go to later-gupta-dynasty.
- gauda-kingdom 554 found (gupta-empire) -> gupta-empire 554 dissolve: mismatch. gupta-empire hands its land to maukhari-dynasty and does not list gauda-kingdom.
- gauda-kingdom 602 gain (later-gupta-dynasty) -> later-gupta-dynasty None None: missing. later-gupta-dynasty holds only Malwa 575-604; the gain is also already inside the gauda found.
- gauda-kingdom 637 dissolve (kamarupa-kingdom) -> kamarupa-kingdom 637 gain: matched. Harsha's share is an exception (not written).
- turk-shahis 665 found (alchon-huns) -> alchon-huns 670 dissolve: mismatch. Five years apart (author flagged); the Turk Shahi and Nezak pages give 665.
- turk-shahis 666 gain (tokhara-yabghus) -> tokhara-yabghus None None: missing. Counterpart corrected by the reviewer from western-gokturks (ended 657); tokhara-yabghus needs a 666 Gandhara loss (it receives Gandhara via western-gokturks from alchon-huns 625).
- turk-shahis 680 loss (zunbils) -> zunbils 680 found: mismatch. Same year; land differs (Zabulistan+Arachosia vs Zabulistan).
- turk-shahis 870 loss (saffarid-dynasty) -> none: exception. saffarid-dynasty (me-08) not written yet; same for zunbils 866 loss and 870 dissolve.
- turk-shahis 870 dissolve (hindu-shahis) -> none: exception. Listed in counterparts_needing_dossiers (sa-03-x); split year to be settled (822 or 870).
- white-huns 560 loss (turk-shahis) -> turk-shahis None None: mismatch. turk-shahis starts 665 and marks the 561-643 shape wrong (Nezak country, drawn in alchon-huns); the white-huns owner should change the counterpart.
- tokhara-yabghus 718 vassal_start (Khuttal, Chaghaniyan, Kabul and Zabul) -> turk-shahis None None: missing. Name counterpart there; no Yabghu vassal events in turk-shahis or zunbils.
- zunbils 680 found (turk-shahis) -> turk-shahis 680 loss: matched. Land differs, see above.
- zunbils 692 gain (nobody) -> none: exception. Confidence 1.
- karkota-dynasty 625 found (alchon-huns) -> alchon-huns 630 loss: mismatch. Five years apart; Karkota page 'Established: 625' (verified); alchon-huns side is confidence 1.
- karkota-dynasty 855 dissolve (utpala-dynasty) -> none: exception. utpala-dynasty is another sa-03 part not yet written.
- pandya-dynasty 592 found (kalabhra-dynasty) -> kalabhra-dynasty 592 loss: matched. 
- kalabhra-dynasty 601 dissolve (pandya-dynasty) -> pandya-dynasty None None: missing. No Pandya gain for 'the middle Kaveri band'.
- pandya-dynasty 897 loss (chola-empire) -> none: exception. chola-empire is another sa-03 part not yet written; same for the 910-915 occupation and 915 dissolve.
- pandya-dynasty 825 loss (Venad) -> none: exception. Listed in counterparts_needing_dossiers (venad).

## Other problems

- No page failed to load. No Wikipedia page of the seven states has an infobox area, so no area ratio could be computed (the authors say so).
- The author's counterparts_needing_dossiers asks for 'yabghus-of-tokharistan' and 'later-guptas-of-malwa'; both exist already as tokhara-yabghus and later-gupta-dynasty. Dropped here.
- Hindu Shahis: the years in counterparts_needing_dossiers are [822,1026] or [870,1026] depending on the split year turk-shahis settles with sa-03-x (rename 822 versus dissolve 870).
- Kashmir: Karkota (625-855), the Cliopatria 'Kashmir' row (626-1343, sa-03) and utpala-dynasty (855-) are dynasties of one state on the same land; the one-state rule would make them one dossier with rename events. Group-level decision for sa-03.
- white-huns /ledger/15 (560 loss of Kabulistan to turk-shahis) contradicts turk-shahis and alchon-huns (Nezak to 665/670): route to the white-huns owner.
- The fetch tool reported the Maukhari infobox capital field as blank where the dossier's capital note says 'Infobox capital: Kanyakubja'; the body names Kanyakubja, so it is not recorded as a fault.
- Reviewer edits made in place and re-validated: turk-shahis (/ledger/2 counterpart, /ledger/3 confidence, /wars/0 and /wars/4 years), zunbils (/wars/0 and /wars/2 years), pandya-dynasty (/identity/rulers).
