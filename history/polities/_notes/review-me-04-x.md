# Review of batch me-04-x (additions: Anatolia, Levant, Arabia)

Reviewer, 2026-10-19. 25 dossiers, all new (cliopatria_names []). Validator with --resolve: 0 errors; 8 warnings, all on awsan (region name "Awsan" missing from the gazetteer). Spot checks: 4 per dossier (6 for qedar, 5 for moab), weighted to confidence-3 and land-moving events; no confidence-3 event was found fabricated or mis-dated.

Verdicts: arzawa fix, kizzuwatna thin, aram-damascus thin, ugarit pass, amurru pass, moab fail, ammon thin, edom thin, hamath pass, awsan pass, yamhad pass, alashiya thin, qatna pass, isuwa thin, hayasa-azzi pass, lihyan pass, bit-agusi pass, carchemish pass, kaska fix, tarhuntassa thin, sam-al pass, gurgum pass, kummuh fail, kammanu fail, qedar thin.

Fixes the reviewer applied in place (each with a note "[Reviewer me-04-x, 2026-10-19: ...]" and re-validated): arzawa /ledger/7/region, kizzuwatna /identity/successors/0/land, moab /ledger/7 year, ammon /ledger/3 year, edom /ledger/3 year (-609 to -605), kaska /identity/capitals (placeholder removed).

## Cross-cutting

- The David-era vassalages that kingdom-of-israel (me-04-a) carries for moab, ammon, edom and aram-damascus (-1000..-930) have no mirror here. The author called them out of scope and wrote that the Moab page is silent on David; it is not (Moab page: David "made the Moabites tributary"; Mesha page: Moab stayed under Solomon, d. c. 931; Edom page: "From that time Edom remained a vassal of Israel", then a dependency of Judah until the revolt against Jehoram; Ammon page: siege of Rabbah, all Ammonite cities conquered).
- The Babylonian vassalage of Moab, Ammon and Edom was dated -609 (c1); the Nebuchadnezzar II page brings Syria and Israel under Babylon after Carchemish in 605. Moved to -605 by the reviewer. The neo-babylonian-empire dossier (me-02) instead has a -609 direct gain of the Levant; route to me-02.
- Kummuh and Kammanu: in 712 Sargon II gave Mutallu of Kummuh only the city of Melid; Kammanu itself was annexed by Assyria (Kummuh and Kammanu pages). Both dossiers give all of Malatya Province to Kummuh. Both fail on this one point.
- Moab fails on keyframe/ledger consistency: the first keyframe (Karak only) never holds Madaba, which the ledger loses in -890, and leaves the capital Dibon outside the shape for 400 years.
- Overlaps with the neo-hittite-states hull (carchemish, bit-agusi, sam-al, gurgum, kummuh, kammanu) and the double -740 Arpad loss are flagged by the author; the renderer rule is still open.

## arzawa: fix

- APPLIED `/ledger/7/region`: The dissolve region was the whole Cliopatria Hittites -1300 shape (321,568 km2, the successor empire), not Arzawa's own land. Evidence: Arzawa page: 'The Kingdom of Arzawa was located in Western Anatolia'; the worked example's dissolve region is the state's own last land. Fix: Replaced with the union of the -1300 loss (/ledger/6/region), the Arzawa lands in western Anatolia; note appended.
- thin `/ledger/2`: c1 bridge: no page dates the end of the c. 1400 subjugation (Tarhundaradu's Amarna-era independence) (try https://en.wikipedia.org/wiki/Tarhundaradu)
- spot checks: `/ledger/1` confirmed; `/ledger/3` confirmed; `/ledger/6` confirmed; `/ledger/7` confirmed
- area: No infobox area; author quotes ~19,000 km2 (core) and ~98,000 km2 (c. 1370 union), both researcher readings.

## kizzuwatna: thin

- APPLIED `/identity/successors/0/land`: Successor land was the whole Cliopatria Hittites -1400 shape, which (by the dossier's own keyframe note) has no Cilician cell. Evidence: Kizzuwatna page: 'situated primarily in the Cilician Plain'; 'remained within the Hittite Empire for 200 years'. Fix: Set to {region: Cilicia} with the same text; note appended.
- thin `/ledger/2`: c1: Tudhaliya I's treaty with Sunassura is undated on the Kizzuwatna page; the page also calls Kizzuwatna a Hittite strategic partner after it, so -1400..-1350 may be Hittite vassalage (the hittites dossier draws Cilicia as Hittite from -1400) (try https://en.wikipedia.org/wiki/Tudhaliya_I)
- thin `/ledger/3`: c1: the absorption into Hatti is undated (page: rebelled under Suppiluliuma I, then stayed in the empire) (try https://en.wikipedia.org/wiki/Suppiluliuma_I)
- thin `/ledger/4`: c1 dissolve bridged to Suppiluliuma's accession (try https://en.wikipedia.org/wiki/Suppiluliuma_I)
- spot checks: `/ledger/0` confirmed; `/ledger/1` confirmed; `/ledger/2` confirmed (page gives no year; bridge declared); `/ledger/3` confirmed (page gives no year; bridge declared)
- area: No infobox; Cilicia region ~30,000 km2 vs page limits Taurus/Amanus/sea: consistent.

## aram-damascus: thin

- TO DO `/ledger`: No Assyrian vassalage before the 732 annexation, although the neo-assyrian-empire dossier has vassal_start "Aram-Damascus" -773 (c3) and vassal_end -732 (c3). Evidence: Aram-Damascus page: 'Rezin had been a tributary of Tiglath-Pileser III'; Tiglath-Pileser III page lists 'the Aramean kingdom of Aram-Damascus' among the states paying tribute after the Arpad victory (740). Fix: Add vassal_start neo-assyrian-empire (-773 to mirror me-02, or -740 from the Tiglath-Pileser III page, c2) and vassal_end -732 before the loss; me-02 and this dossier must agree on the start year.
- thin `/ledger/1`: c1: Hazael's Transjordan gains undated (page: seized Israelite territory east of the Jordan); his expansion is not drawn in the single 368-year keyframe (try https://en.wikipedia.org/wiki/Ben-Hadad_III)
- thin `/ledger/2`: c1: Gath siege undated on the Hazael page (try https://en.wikipedia.org/wiki/Gath_(city))
- thin `/keyframe_review/0`: one shape for -1100..-732; the David-era vassalage carried by kingdom-of-israel (-1000..-930) has no mirror here (try https://en.wikipedia.org/wiki/Aram-Zobah)
- thin `/ledger/3`: c1 contest_end -830 (philistia): bridged, no page dates it (try https://en.wikipedia.org/wiki/Aram-Damascus)
- thin `/ledger/4`: c1 contest_end -796 (kingdom-of-israel): bridged, no page dates it (try https://en.wikipedia.org/wiki/Aram-Damascus)
- spot checks: `/ledger/0` confirmed (late 12th century); `/ledger/1` confirmed (undated on page; bridge declared); `/ledger/5` confirmed; `/ledger/6` confirmed
- area: No infobox area; Damascus district + Golan ~19,000 km2 reading.

## ugarit: pass

- thin `/ledger/0`: c1 start: page gives the kingdom's height (c. 1450-1185), not a founding; Middle Bronze kingdom (Mari era) not covered (try https://en.wikipedia.org/wiki/Ugarit)
- thin `/ledger/1`: c1: Hittite submission dated by Niqmaddu II's reign only (try https://en.wikipedia.org/wiki/Niqmaddu_II)
- spot checks: `/ledger/0` confirmed (height c. 1450); `/ledger/1` confirmed (Niqmaddu II c. 1350-1315 became Hittite vassal); `/ledger/2` confirmed (c. 1185; 1192-1190 destruction); `/ledger/3` confirmed
- area: Page text: 'controlled about 2,000 km2 on average', 'roughly equivalent to the modern Latakia Governorate'; keyframe 1,770 km2; ratio 0.89; acknowledged in keyframe note.

## amurru: pass

- thin `/ledger/0`: c1: Abdi-Ashirta's earlier Amurru (fl. 14th c.) not dated (try https://en.wikipedia.org/wiki/Abdi-Ashirta)
- thin `/ledger/7`: c1: return to Hittite vassalage after Kadesh; the Benteshina page failed to load for the author (try https://en.wikipedia.org/wiki/Muwatalli_II)
- spot checks: `/ledger/0` confirmed (c. 1350-1315); `/ledger/1` confirmed (Aziru styled himself governor of Amurru for Egypt; undated); `/ledger/2` confirmed (around 1350-1345); `/ledger/8` confirmed (c. 1200)
- area: No infobox area; page: Tartus to Byblos and the Homs Gap, which the union follows.

## moab: fail

- APPLIED `/ledger/7/year`: Babylonian vassalage dated -609 (c1), before Babylon reached the Levant. Evidence: Nebuchadnezzar II page: the 605 BC Carchemish victory 'resulted in all of Syria and Israel coming under the control of the Neo-Babylonian Empire'. Fix: Year set to -605, source the Nebuchadnezzar II page, note appended.
- TO DO `/keyframe_review/0`: Keyframe/ledger inconsistency: moab_-1250 (-1250..-851) is Karak only, yet /ledger/2 has Moab lose Madaba to Israel in -890, land the keyframe never held; and the capital Dibon (35.78 E, 31.50 N, north of the Arnon) lies outside the shape (Karak cells end at 31.38 N) for the whole -1250..-851 span. Evidence: Mesha Stele (author's note): 'Omri took the land of Madeba' implies Moab held it before; Moab page: capital Dibon; gazetteer: Karak bbox 30.9-31.38 N, Madaba 31.51-31.67 N. Fix: Either draw -1250..-891 as {region: Moab} and add a keyframe -890..-851 of Karak plus a Dibon circle (Dibon stayed Moabite: Mesha "the Dibonite"), or drop the -890 loss and add a Dibon circle to moab_-1250; the -890 loss region should then exclude Dibon.
- TO DO `/ledger`: No mirror of kingdom-of-israel's vassal_start moab -1000 / vassal_end moab -930; the author's note says the Moab page is silent on David, which is wrong. Evidence: Moab page: David 'made the Moabites tributary' (2 Samuel 8:2); Mesha page: David conquered Moab, it stayed under Solomon (died c. 931 BC), Omri later recovered it. Fix: Add vassal_start kingdom-of-israel -1000 c1 and vassal_end -930 c1 citing the Mesha page; correct the notes sentence.
- thin `/ledger/8`: c1: Moab drawn free from 587 to 400 with no overlord; Ammon page puts Nebuchadnezzar's devastation in the 580s and the Moab page has Moab "exiled to Babylon"; the Babylonian and Persian status 587-400 needs a page (try https://en.wikipedia.org/wiki/Achaemenid_Empire)
- thin `/ledger/1`: c1 arithmetic bridge (850 minus forty years) for Omri's conquest (try https://en.wikipedia.org/wiki/Omri)
- thin `/ledger/6`: c1 bridge to the end of Assyria (try https://en.wikipedia.org/wiki/Moab)
- thin `/ledger/2`: c1 loss -890 (kingdom-of-israel): bridged, no page dates it (try https://en.wikipedia.org/wiki/Moab)
- thin `/ledger/7`: c1 vassal_start -605 (neo-babylonian-empire): bridged, no page dates it (try https://en.wikipedia.org/wiki/Moab)
- spot checks: `/ledger/3` confirmed (c. 850 BC); `/ledger/5` confirmed (734); `/ledger/7` mis-dated (609 vs 605); fixed; `/ledger/8` confirmed (587 rebellion); `/ledger/9` confirmed (Collapsed c. 400 BCE)
- area: No infobox area; Karak ~3,300 km2, Moab region ~4,000 km2.

## ammon: thin

- APPLIED `/ledger/3/year`: Babylonian vassalage dated -609 (c1), before Babylon reached the Levant. Evidence: Nebuchadnezzar II page: the 605 BC Carchemish victory brought 'all of Syria and Israel' under Babylonian control. Fix: Year set to -605, source the Nebuchadnezzar II page, note appended.
- TO DO `/ledger`: No mirror of kingdom-of-israel's vassal_start ammon -1000 / vassal_end -930. Evidence: Ammon page: David's war 'ended in a war and a year-long siege of Rabbah' with 'all the Ammonite cities being conquered and plundered' (undated). Fix: Add vassal_start (or occupation) kingdom-of-israel -1000 c1 and its end -930 c1, or explain why not.
- thin `/ledger/2`: c1 bridge to the end of Assyria (try https://en.wikipedia.org/wiki/Ammon)
- thin `/ledger/3`: c1 vassal_start -605 (neo-babylonian-empire): bridged, no page dates it (try https://en.wikipedia.org/wiki/Ammon)
- spot checks: `/ledger/0` confirmed (flourishes 11th century BC); `/ledger/1` confirmed (734 Sanipu vassal of Tiglath-Pileser III); `/ledger/3` mis-dated (609 vs 605); fixed; `/ledger/5` confirmed (Babylonian province after devastation in the 580s)
- area: No infobox area; Ammon region ~11,600 km2 (Arnon to Jabbok per page).

## edom: thin

- APPLIED `/ledger/3/year`: Babylonian vassalage dated -609 (c1), before Babylon reached the Levant. Evidence: Nebuchadnezzar II page: the 605 BC Carchemish victory brought 'all of Syria and Israel' under Babylonian control. Fix: Year set to -605, source the Nebuchadnezzar II page, note appended.
- TO DO `/ledger`: Israelite and Judahite overlordship missing although the Edom page states it; kingdom-of-israel has vassal_start edom -1000 / vassal_end -930. Evidence: Edom page: David and Joab defeated the Edomites; 'From that time Edom remained a vassal of Israel'; after the split Edom became a dependency of Judah; 'Edom revolted against Jehoram and elected a king of its own'. Fix: Add vassal_start kingdom-of-israel -1000 / vassal_end -930, vassal_start kingdom-of-judah -930 / vassal_end at Jehoram's reign (c. -848, from the Jehoram of Judah page), c1-c2.
- thin `/ledger/2`: c1 bridge to the end of Assyria (try https://en.wikipedia.org/wiki/Edom)
- thin `/ledger/4`: c1: the 587 'rebellion' is only on the Nebuchadnezzar page; the Edom page ties 587/86 to Judah's destruction (try https://en.wikipedia.org/wiki/Jehoram_of_Judah)
- thin `/ledger/3`: c1 vassal_start -605 (neo-babylonian-empire): bridged, no page dates it (try https://en.wikipedia.org/wiki/Edom)
- spot checks: `/ledger/0` confirmed (Seti I c. 1215 BC); `/ledger/1` confirmed (734); `/ledger/5` confirmed (conquered by Nabonidus c. 553 BC); `/ledger/6` confirmed
- area: No infobox area; Edom region clipped by a lon/lat box (polygon used only as a clip).

## hamath: pass

- thin `/ledger/0`: c1 start at first attestation (853); the page calls Hama the capital of a Syro-Hittite state before that (Neo-Hittite/Aramaean phase not covered) (try https://en.wikipedia.org/wiki/Syro-Hittite_states)
- spot checks: `/ledger/0` confirmed (853 first Assyrian mention); `/ledger/1` confirmed (Luhuti incorporated around 796 BC); `/ledger/2` confirmed (738: Kullania, Hatarikka, Simirra taken from Hama); `/ledger/5` confirmed (razed c. 720 BC)
- area: No infobox area; 60 km circle ~11,000 km2, plus Idlib ~5,300 km2 in -796..-739.

## awsan: pass

- spot checks: `/ledger/0` confirmed (8th century BC); `/ledger/1` confirmed (destroyed by Saba, late 7th century); `/ledger/2` confirmed (territory divided between Qataban and Hadhramaut)
- area: No infobox area; region 'Awsan' not in the gazetteer (8 resolve warnings, flagged by author).

## yamhad: pass

- thin `/ledger/3`: c1 end of the vassal network (try https://en.wikipedia.org/wiki/Hattusili_I)
- spot checks: `/ledger/0` confirmed (c. 1810 BC); `/ledger/1` confirmed (1777 BC Tuttul); `/ledger/4` confirmed (Alalakh c. 1650 BC); `/ledger/5` confirmed (c. 1524, Parshatatar)
- area: Infobox 43,000 km2 (1750 BC) vs keyframe yamhad_-1777 33,900 km2; acknowledged. Remark: that keyframe starts at -1777 with the vassal lands the ledger adds only at -1752.

## alashiya: thin

- thin `/ledger/0`: c1 start at the first dated mention (try https://en.wikipedia.org/wiki/Enkomi)
- thin `/ledger/1`: the Alashiya page has a treaty of submission, not annexation; loss rests on the Tudhaliya IV page's "conquest": consider vassal_start; the hittites dossier has no Cyprus event (try https://en.wikipedia.org/wiki/Suppiluliuma_II)
- thin `/ledger/2`: c1 end; fate of Cyprus after the Hittite campaigns and the Iron Age kingdoms (Kition, Salamis) missing (try https://en.wikipedia.org/wiki/Kition)
- spot checks: `/ledger/0` confirmed (around 1400 BC); `/ledger/1` confirmed year; page says treaty of submission; `/ledger/2` confirmed (page silent on the end; bridge declared)
- area: No infobox area; whole island ~7,600 km2 as declared maximal reading.

## qatna: pass

- thin `/ledger/2`: c1 end of Mitanni vassalage bridged to Thutmose III (try https://en.wikipedia.org/wiki/Thutmose_III)
- thin `/ledger/4`: c1 end of Egyptian vassalage (try https://en.wikipedia.org/wiki/Amarna_letters)
- spot checks: `/ledger/0` confirmed (around 2000 BC); `/ledger/1` confirmed (16th century); `/ledger/3` confirmed (c. 1446 BC); `/ledger/5` confirmed (sack after 1340, before c. 1334)
- area: No infobox area; ~22,500 km2 reading of upper Orontes to Palmyra.

## isuwa: thin

- thin `/ledger/0`: c1 start at -1400 although the Isuwa page says Isuwa 'came under Hittite sovereignty towards 1600 BC'; the life could start c. -1600 as a Hittite vassal (try https://en.wikipedia.org/wiki/Isuwa)
- thin `/ledger/1`: c1 Mitanni vassalage bridged (try https://en.wikipedia.org/wiki/Shaushtatar)
- spot checks: `/ledger/0` confirmed (hostile in Suppiluliuma's father's time); `/ledger/2` confirmed; `/ledger/3` confirmed; `/ledger/4` confirmed (early twelfth century)
- area: No infobox area; Elazig + Tunceli reading.

## hayasa-azzi: pass

- thin `/ledger/0`: c1 start (14th-century conflict) (try https://en.wikipedia.org/wiki/Hayasa-Azzi)
- thin `/ledger/1`: c1: Suppiluliuma's treaty with Hakkana undated (try https://en.wikipedia.org/wiki/Suppiluliuma_I)
- spot checks: `/ledger/1` confirmed (vassal treaty with Hakkana; undated); `/ledger/2` confirmed (1315 BCE); `/ledger/5` confirmed (submission the year after the tenth year); `/ledger/6` confirmed (end of the 13th century)
- area: No infobox area; four Turkish provinces reading.

## lihyan: pass

- thin `/ledger/0`: c1 start (6th century) (try https://en.wikipedia.org/wiki/Dedan)
- thin `/ledger/3`: c1 rename: page gives 4th century (traditional) or late 6th (Rohmer and Charloux) (try https://en.wikipedia.org/wiki/Lihyan)
- spot checks: `/ledger/0` confirmed (bridge declared); `/ledger/1` confirmed (c. 552 BC); `/ledger/3` confirmed (dating disputed, declared); `/ledger/4` confirmed (Caskel: around 24 BC)
- area: No infobox area; 110 km circle ~34,000 km2 vs page domain Yathrib to the Levant (declared modest).

## bit-agusi: pass

- thin `/ledger/3`: c1: Aram-Damascus supremacy over Bit Agusi is a reading of the stage list (try https://en.wikipedia.org/wiki/Bit_Agusi)
- thin `/ledger/5`: c1: Aleppo's addition undated (try https://en.wikipedia.org/wiki/Sefire_steles)
- spot checks: `/ledger/0` confirmed (early 9th century); `/ledger/1` confirmed (858 BCE); `/ledger/6` confirmed (743 siege); `/ledger/8` confirmed (Arpad captured 740, two provinces)
- area: No infobox area; 50 km circle then Aleppo region ~18,000 km2.

## carchemish: pass

- thin `/ledger/3`: c1: Great Kingdom extent undated and unbounded (try https://en.wikipedia.org/wiki/Kuzi-Teshub)
- thin `/ledger/4`: c1 end of the Great Kingdom (try https://en.wikipedia.org/wiki/Syro-Hittite_states)
- thin `/ledger/6`: c1: Sangara tribute dated by reign (try https://en.wikipedia.org/wiki/Ashurnasirpal_II)
- spot checks: `/ledger/0` confirmed (text 'siege and conquest by Suppiluliuma I (c. 1345 BC)'; infobox c. 1321, noted by author); `/ledger/2` confirmed (c. 1175); `/ledger/6` confirmed (Sangara 870-848); `/ledger/8` confirmed (717 BC)
- area: No infobox area; 60/90 km circles.

## kaska: fix

- APPLIED `/identity/capitals/0`: A placeholder capital (named "none") drew a seat at 37.8 E 40.9 N for a tribal union with no capital. Evidence: Kaskians page names no capital: the Kaska were 'loosely affiliated' tribes; schema: capitals empty for stateless entities. Fix: capitals set to []; note appended.
- thin `/ledger/2`: c1 contest end bridged to the Hittite collapse (try https://en.wikipedia.org/wiki/Kaskians)
- thin `/ledger/3`: c1 dissolve bridged to Tiglath-Pileser I (assyria dossier 1112) (try https://en.wikipedia.org/wiki/Tiglath-Pileser_I)
- spot checks: `/ledger/0` confirmed (c. 1450 BC, Hantili II); `/ledger/1` confirmed (Tudhaliya's 3rd campaign); `/ledger/3` confirmed (late 12th century; bridge declared); `/wars/1` confirmed (c. 1330 burning of Hattusa)
- area: No infobox area; Pontus region ~60,000 km2 reading.

## tarhuntassa: thin

- TO DO `/identity/start`: From -1280 to Kurunta's appointment Tarhuntassa was the Hittite capital, i.e. the Hittite state itself, not a separate kingdom; the dossier draws a second state over Hittite land for those years. Evidence: Tarhuntassa page: 'Muwatalli II moved the Hittite capital from Hattusa to Tarhuntassa'; 'Muwatalli II's son Mursili III later moved the capital back'; 'Hattusili III ... appointed Muwatalli's son Kurunta as king in Tarhuntassa'. Fix: Start the life at Kurunta's appointment (bridge -1267, with found and vassal_start hittites there) and route the capital period to the hittites dossier (me-04-a) as capital_move events; or say in notes why the capital period is drawn separately.
- thin `/ledger/0`: all four events are c1 bridges; site and borders unknown (try https://en.wikipedia.org/wiki/Kurunta)
- thin `/ledger/2`: c1: Suppiluliuma II's attack undated (try https://en.wikipedia.org/wiki/Suppiluliuma_II)
- thin `/ledger/1`: c1 vassal_start -1267 (hittites): bridged, no page dates it (try https://en.wikipedia.org/wiki/Tarhuntassa)
- thin `/ledger/3`: c1 dissolve -1180 (nobody): bridged, no page dates it (try https://en.wikipedia.org/wiki/Tarhuntassa)
- spot checks: `/ledger/0` confirmed (early 13th century; bridge); `/ledger/1` confirmed (undated; bridge); `/ledger/2` confirmed (undated; bridge); `/ledger/3` confirmed (page silent; bridge)
- area: No infobox area; ~47,000 km2 placeholder from proposed sites, declared.

## sam-al: pass

- thin `/keyframe_review/0`: gains from Carchemish, Quwe and Adana and the Ya'udi union undated, not drawn (try https://en.wikipedia.org/wiki/Kilamuwa_Stela)
- spot checks: `/ledger/0` confirmed (by 920 BC); `/ledger/1` confirmed (825 BC); `/ledger/2` confirmed (717 BC); `/ledger/3` confirmed (717 BC)
- area: Infobox 1200-609 BC vs body 920/717 noted by author; no area.

## gurgum: pass

- spot checks: `/ledger/0` confirmed (Larama I c. 950 BC); `/ledger/1` confirmed (Muwatalli II submitted, Shalmaneser III); `/ledger/3` confirmed (743, tributary after); `/ledger/5` confirmed (711 annexed, renamed Marqas)
- area: No infobox area; K. Maras province ~13,400 km2 reading.

## kummuh: fail

- TO DO `/ledger/6/region`: The 712 gain hands Kummuh the whole Malatya Province (11,100 km2); the pages give it only the city of Melid. Evidence: Kummuh page: 'After Sargon II dismembered Melid, the city of Melid itself was given to Kummuh king Muttallu'; Kammanu page: 'Kammanu was annexed by Assyria and the city of Melid was placed under the rule of Mutallu'. Fix: Gain region = the city of Melid (e.g. {lon 38.36, lat 38.38, km 20} at Arslantepe); keyframe kummuh_-712 = Adiyaman plus that circle; the same for /ledger/7-9 regions, /wars/1 zone and the successor land.
- TO DO `/ledger/8`: Confidence 3 on a region (Adiyaman plus all Malatya) that the page does not name. Evidence: Kummuh page names Kummuh and the city of Melid only. Fix: After the region fix, keep 3 only for the Kummuh core; otherwise lower to 2.
- thin `/ledger/0`: c1 start at first tribute (866) (try https://en.wikipedia.org/wiki/Kummuh)
- thin `/ledger/2`: c1 bridge (middle of the 8th century) (try https://en.wikipedia.org/wiki/Sarduri_II)
- thin `/ledger/4`: c1 end of Urartian tribute (try https://en.wikipedia.org/wiki/Sarduri_II)
- spot checks: `/ledger/0` confirmed (866 BCE); `/ledger/3` confirmed (around 750 BCE); `/ledger/6` not on page as drawn (city of Melid, not the province); `/ledger/8` confirmed year (708); region overstated
- area: No infobox area; keyframe kummuh_-712 17,700 km2 includes ~11,100 km2 of Malatya not supported by the page.

## kammanu: fail

- TO DO `/ledger/3`: The 712 loss gives all of Kammanu (Malatya Province) to Kummuh; the page says Kammanu was annexed by Assyria and only the city of Melid went to Mutallu. Evidence: Kammanu page: 'Kammanu was annexed by Assyria and the city of Melid was placed under the rule of Mutallu, king of Kummuh'; Kummuh page: 'Sargon II dismembered Melid'. Fix: Split: loss of {minus: [Malatya Province, Melid circle]} to neo-assyrian-empire plus loss of the Melid circle to kummuh; dissolve counterpart neo-assyrian-empire; successors both, with those lands.
- thin `/ledger/1`: earlier Assyrian tribute (Tiglath-Pileser I; Shalmaneser III) undated and not drawn (try https://en.wikipedia.org/wiki/Melid)
- spot checks: `/ledger/0` confirmed (c. 1200); `/ledger/1` confirmed (719 BC); `/ledger/2` confirmed (infobox 712); `/ledger/3` not on page as drawn (annexed by Assyria; only Melid city to Mutallu)
- area: No infobox area; Malatya Province ~11,100 km2.

## qedar: thin

- TO DO `/ledger/2`: Vassalage ended in -733 and restarted in -716, drawing Qedar free for 17 years, but the 733 revolt was crushed and Samsi stayed under Assyrian supervision. Evidence: Tiglath-Pileser III page: 'In 733, Tiglath-Pileser campaigned against the Qedarites'; Šamši 'was allowed to stay in control under Assyrian supervision'. Fix: Drop the -733 vassal_end and -716 vassal_start (keep the 733 war), or restart the vassalage at -733/-732.
- TO DO `/ledger/8/year`: Expansion placed at -445 (c1) although the page dates it to Darius I and Xerxes I (522-465). Evidence: Qedar page: the expansion 'under Darius I and Xerxes I' put the Qedarites 'in control of the Negev'. Fix: Move the gain and keyframe qedar_-445 to a year inside 522-465 (e.g. -480, Xerxes I) and keep c1.
- thin `/ledger/9`: c1 end (343, "might possibly"); infobox runs to the 1st century BC (absorbed by the Nabataeans) (try https://en.wikipedia.org/wiki/Nabataean_Kingdom)
- thin `/ledger/5`: c1 Assyrian suzerainty after 645 bridged (try https://en.wikipedia.org/wiki/Ashurbanipal)
- thin `/keyframe_review/1`: 231,000 km2 deliberately generous reading at c1 (try https://en.wikipedia.org/wiki/Nehemiah)
- thin `/ledger/0`: c1 found -853 (nobody): bridged, no page dates it (try https://en.wikipedia.org/wiki/Qedar)
- thin `/ledger/6`: c1 vassal_end -609 (neo-assyrian-empire): bridged, no page dates it (try https://en.wikipedia.org/wiki/Qedar)
- thin `/ledger/8`: c1 gain -445 (achaemenid-empire): bridged, no page dates it (try https://en.wikipedia.org/wiki/Qedar)
- thin `/ledger/10`: c1 loss -343 (achaemenid-empire): bridged, no page dates it (try https://en.wikipedia.org/wiki/Qedar)
- thin `/ledger/11`: c1 dissolve -343 (nabataeans): bridged, no page dates it (try https://en.wikipedia.org/wiki/Qedar)
- spot checks: `/ledger/0` confirmed (853 Qarqar); `/ledger/1` confirmed (738 Zabibe); `/ledger/2` confirmed revolt; but vassalage continued (see fix); `/ledger/3` confirmed (716); `/ledger/7` confirmed (539, Cyrus); `/ledger/8` mis-dated c1 (Darius I/Xerxes I)
- area: No infobox area; Al Jawf 105,000 km2 core, 231,000 km2 expanded, both researcher readings.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| arzawa -1400 vassal_start (hittites) | hittites -1400 gain | mismatch | Same year, different type: hittites draws Arzawa as annexed (gain) in -1400, arzawa as vassal; hittites has no -1370 loss for Arzawa's c. 1370 independence and expansion. route: me-04-a |
| arzawa -1370 gain (western Anatolian states (the page names none)) | - | exception | Counterpart "western Anatolian states" (Mira, Hapalla, Seha River Land, Wilusa) has no dossier; listed in counterparts_needing_dossiers. |
| arzawa -1300 loss (hittites) | hittites -1300 gain | matched |  |
| kizzuwatna -1480 vassal_start (mitanni) | - | missing | mitanni has no Kizzuwatna event. route: me-04 (mitanni) |
| kizzuwatna -1350 loss (hittites) | - | mismatch | hittites has no Kizzuwatna event and draws Cilicia as Hittite from -1400 (in its -1400 shape per its note), against kizzuwatna's -1350 absorption. route: me-04-a |
| aram-damascus -732 loss (neo-assyrian-empire) | neo-assyrian-empire -732 gain | matched | NAE -732 vassal_end + gain "Aram-Damascus". |
| ugarit -1345 vassal_start (hittites) | hittites -1345 vassal_start | matched |  |
| amurru -1350 vassal_start (new-kingdom-of-egypt) | - | missing | new-kingdom-of-egypt has no Amurru vassal event (only syrian-city-states -1447..-1352). route: me-03 |
| amurru -1345 vassal_start (hittites) | hittites -1345 vassal_start | matched |  |
| amurru -1275 vassal_start (new-kingdom-of-egypt) | new-kingdom-of-egypt -1275 gain | mismatch | Same year; NKE records a gain from hittites of Homs/Tartus (direct land), amurru a vassalage to Egypt. route: me-03 |
| amurru -1274 vassal_start (hittites) | hittites -1274 vassal_start | matched | Also amurru -1200 vassal_end vs hittites -1180 vassal_end (20-year mismatch; page: c. 1200). |
| moab -890 vassal_start (kingdom-of-israel) | kingdom-of-israel -930 vassal_end | mismatch | Israel ends its Moab vassalage in -930 and has no Omri-era re-subjugation (-890) or Medeba occupation. route: me-04-a |
| moab -890 loss (kingdom-of-israel) | - | missing | No Israelite gain of Medeba c. 890 in kingdom-of-israel. route: me-04-a |
| moab -850 gain (kingdom-of-israel) | - | missing | No Israelite loss of Medeba c. 850 in kingdom-of-israel. route: me-04-a |
| moab -734 vassal_start (neo-assyrian-empire) | neo-assyrian-empire -734 vassal_start | matched | NAE "Judah, Edom, Moab and Ammon". |
| moab -605 vassal_start (neo-babylonian-empire) | neo-babylonian-empire -609 gain | mismatch | Year moved by the reviewer from -609 to -605; NBE has no vassal_start for Moab/Ammon/Edom but a -609 direct gain of the Levant (Nebuchadnezzar II page: Levant control from 605/604). route: me-02 |
| ammon -605 vassal_start (neo-babylonian-empire) | neo-babylonian-empire -609 gain | mismatch | Year moved by the reviewer from -609 to -605; NBE has no vassal_start for Moab/Ammon/Edom but a -609 direct gain of the Levant (Nebuchadnezzar II page: Levant control from 605/604). route: me-02 |
| edom -605 vassal_start (neo-babylonian-empire) | neo-babylonian-empire -609 gain | mismatch | Year moved by the reviewer from -609 to -605; NBE has no vassal_start for Moab/Ammon/Edom but a -609 direct gain of the Levant (Nebuchadnezzar II page: Levant control from 605/604). route: me-02 |
| ammon -734 vassal_start (neo-assyrian-empire) | neo-assyrian-empire -734 vassal_start | matched |  |
| ammon -585 loss (neo-babylonian-empire) | - | missing | NBE has no Ammon annexation in the 580s. route: me-02 |
| edom -734 vassal_start (neo-assyrian-empire) | neo-assyrian-empire -734 vassal_start | matched |  |
| edom -553 loss (neo-babylonian-empire) | neo-babylonian-empire -553 gain | mismatch | NBE -553 gain (counterpart nobody) is a circle at Tayma, not Edom; no Edom event. route: me-02 |
| hamath -796 gain (Luhuti (Lu'ash)) | - | exception | Luhuti (Lu'ash) has no dossier; listed in counterparts_needing_dossiers. |
| hamath -738 loss (neo-assyrian-empire) | neo-assyrian-empire -738 gain | mismatch | NAE -738 gains the Idlib/Hatay union from "Pattin"; hamath loses Idlib (Luhuti) to NAE the same year. Tiglath-Pileser III page: the three provinces "had been under the rule of the Neo-Hittite kingdom of Hama" and Pattin was annexed separately: both claims partly right; the land split needs settling. route: me-02 |
| hamath -738 vassal_start (neo-assyrian-empire) | neo-assyrian-empire -738 vassal_start | matched | NAE "Hama". |
| hamath -720 loss (neo-assyrian-empire) | neo-assyrian-empire -720 gain | matched | NAE "Hama" -720 vassal_end + gain. |
| awsan -625 loss (sabaeans) | sabaeans -625 gain | matched |  |
| yamhad -1777 gain (Shamshi-Adad I's kingdom (the page does not name Tuttul's previous holder)) | - | exception | Counterpart is Shamshi-Adad I's kingdom (no slug); the assyria dossier (me-02) may hold Tuttul. |
| yamhad -1752 vassal_start (Syrian vassal kingdoms (Ebla, Mamma, Ugarit, Alalakh, Carchemish)) | - | exception | Counterparts are the Syrian vassal kingdoms (Ebla III, Mamma, Ugarit, Alalakh, Carchemish): no dossiers for those years; ugarit starts -1450. |
| yamhad -1524 loss (mitanni) | mitanni -1500 gain | mismatch | mitanni has no Aleppo gain at -1524; its nearest is a -1500 gain from nobody of its western shape. route: me-04 (mitanni) |
| alashiya -1200 loss (hittites) | - | missing | hittites has no Cyprus event. route: me-04-a |
| qatna -1550 vassal_start (mitanni) | - | missing | mitanni has no Qatna vassal event. route: me-04 (mitanni) |
| qatna -1446 vassal_start (new-kingdom-of-egypt) | new-kingdom-of-egypt -1447 vassal_start | matched | NKE counterpart "syrian-city-states" -1447. |
| qatna -1337 loss (hittites) | hittites -1345 gain | mismatch | hittites -1345 gain "syrian-city-states" (c1) vs qatna -1337 (page: sack after 1340, before c. 1334). route: me-04-a |
| isuwa -1400 vassal_start (mitanni) | - | missing | mitanni has no Isuwa event. route: me-04 (mitanni) |
| isuwa -1350 vassal_start (hittites) | - | missing | hittites has no Isuwa event. route: me-04-a |
| hayasa-azzi -1348 vassal_start (hittites) | - | missing | hittites has no Hayasa-Azzi event. route: me-04-a |
| hayasa-azzi -1311 vassal_start (hittites) | - | missing | hittites has no Hayasa-Azzi event. route: me-04-a |
| lihyan -552 occupation_start (neo-babylonian-empire) | neo-babylonian-empire -553 gain | mismatch | NBE -553 gain (nobody) is Tayma only; no occupation of Dedan 552-543. route: me-02 |
| lihyan -24 loss (nabataeans) | - | exception | nabataeans (me-05) has no dossier yet. |
| bit-agusi -858 vassal_start (neo-assyrian-empire) | neo-hittite-states -868 vassal_start | mismatch | NAE has no Bit Agusi vassal event; the neo-hittite-states hull starts vassalage in -868 for the whole hull. route: me-02, me-04-a |
| bit-agusi -823 vassal_start (aram-damascus) | - | missing | aram-damascus has no vassal_start over Bit Agusi (c1 reading in bit-agusi). route: this batch (aram-damascus) |
| bit-agusi -740 loss (neo-assyrian-empire) | neo-assyrian-empire -740 gain | matched | NAE "Arpad" -740; neo-hittite-states also has a -740 loss of Arpad (double count flagged by author). |
| carchemish -1345 vassal_start (hittites) | hittites -1327 gain | mismatch | hittites (and mitanni -1327 loss) put Carchemish's fall in -1327 as direct Hittite land; carchemish has a -1345 vassal kingdom (Carchemish page text c. 1345, infobox c. 1321). route: me-04-a |
| carchemish -870 vassal_start (neo-assyrian-empire) | neo-hittite-states -868 vassal_start | mismatch | NAE has no Carchemish vassal event; the hull dossier has -868. route: me-02 |
| carchemish -717 loss (neo-assyrian-empire) | neo-assyrian-empire -717 gain | matched |  |
| tarhuntassa -1267 vassal_start (hittites) | - | missing | hittites has no Tarhuntassa event or capital entry. route: me-04-a |
| sam-al -825 vassal_start (neo-assyrian-empire) | - | missing | NAE has no Sam'al event. route: me-02 |
| sam-al -717 loss (neo-assyrian-empire) | - | missing | NAE has no Sam'al annexation (717). route: me-02 |
| gurgum -858 vassal_start (neo-assyrian-empire) | - | missing | NAE has no Gurgum event. route: me-02 |
| gurgum -743 vassal_start (neo-assyrian-empire) | - | missing | NAE has no Gurgum event. route: me-02 |
| gurgum -711 loss (neo-assyrian-empire) | - | missing | NAE has no Gurgum annexation (711). route: me-02 |
| kummuh -866 vassal_start (neo-assyrian-empire) | - | missing | NAE has no Kummuh event. route: me-02 |
| kummuh -750 vassal_start (kingdom-of-urartu) | - | exception | kingdom-of-urartu (eu-19) has not run yet. |
| kummuh -738 vassal_start (neo-assyrian-empire) | - | missing | NAE has no Kummuh event. route: me-02 |
| kummuh -712 gain (kammanu) | kammanu -712 loss | matched | Both sides overstate the land (whole Malatya Province vs the city of Melid): see the kummuh and kammanu fixes. |
| kummuh -708 loss (neo-assyrian-empire) | - | missing | NAE has no Kummuh annexation (708). route: me-02 |
| kammanu -719 vassal_start (neo-assyrian-empire) | - | missing | NAE has no Kammanu event. route: me-02 |
| kammanu -712 loss (kummuh) | kummuh -712 gain | mismatch | Mirrored inside the batch, but the Kammanu page gives the land to Assyria, only Melid city to Kummuh; NAE has no event. route: this batch, me-02 |
| qedar -738 vassal_start (neo-assyrian-empire) | - | missing | NAE has no Qedar event (only the Mu'na after 734). route: me-02 |
| qedar -716 vassal_start (neo-assyrian-empire) | - | missing | NAE has no Qedar event (only the Mu'na after 734). route: me-02 |
| qedar -645 vassal_start (neo-assyrian-empire) | - | missing | NAE has no Qedar event (only the Mu'na after 734). route: me-02 |
| qedar -539 vassal_start (achaemenid-empire) | achaemenid-empire -539 gain | mismatch | achaemenid-empire -539 gain is the Neo-Babylonian empire, no Qedar vassal event. route: me-05 |
| qedar -445 gain (achaemenid-empire) | - | missing | achaemenid-empire has no loss to Qedar (gain made under Persian authority). route: me-05 |
| qedar -343 loss (achaemenid-empire) | - | missing | achaemenid-empire has no gain from Qedar in -343. route: me-05 |
| kingdom-of-israel -1000 vassal_start (moab) | moab | missing | No mirror in moab (nor the -930 vassal_end). Author: out of scope; the Moab, Mesha, Ammon and Edom pages do mention David's conquest. Route: this batch (moab). |
| kingdom-of-israel -1000 vassal_start (ammon) | ammon | missing | No mirror in ammon (nor the -930 vassal_end). Author: out of scope; the Moab, Mesha, Ammon and Edom pages do mention David's conquest. Route: this batch (ammon). |
| kingdom-of-israel -1000 vassal_start (edom) | edom | missing | No mirror in edom (nor the -930 vassal_end). Author: out of scope; the Moab, Mesha, Ammon and Edom pages do mention David's conquest. Route: this batch (edom). |
| kingdom-of-israel -1000 vassal_start (aram-damascus) | aram-damascus | missing | No mirror in aram-damascus (nor the -930 vassal_end). Author: out of scope; the Moab, Mesha, Ammon and Edom pages do mention David's conquest. Route: this batch (aram-damascus). |
| neo-assyrian-empire -773 vassal_start (Aram-Damascus) | aram-damascus | missing | No vassal_start in aram-damascus; nor the -732 vassal_end. Route: this batch (aram-damascus), years to agree with me-02. |
| neo-assyrian-empire -800 gain (Aram-Damascus and the western states) | aram-damascus | missing | c1 gain in NAE; aram-damascus has no loss or vassalage c. 800. Route: me-02 / this batch. |
