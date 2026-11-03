# Review of batch me-05-x (additions: states Cliopatria lacks)

Reviewed 2026-10-19 by the adversarial reviewer. 18 dossiers, all new states (no Cliopatria rows; page budget 1-5 by the author's brief). The validator (--resolve) passed all 18 with no errors or warnings, before and after the reviewer's edits.

## Verdicts

| slug | verdict | short reason |
| --- | --- | --- |
| cyrene-and-barca | pass | spot checks hold; one confidence-1 bridge (Barca) |
| lycian-league | fix | Brutus's occupation now names the Liberators (applied) |
| kingdom-of-antiochus-hierax | fix | Sardis longitude, ruler span, battle note (applied) |
| hecatomnid-caria | pass | spot checks hold; Ada I's second reign undrawn (thin) |
| tetrarchy-of-galilee-and-peraea | pass | spot checks hold |
| tetrarchy-of-philip | fix | Hauran stand-in overlaps Antipas's Gilead in Irbid (author) |
| kingdom-of-herod-agrippa-i | fix | 39 source switched (applied); capital 37-40 missing (author) |
| itureans | fail | Damascus stand-in contradicted by the page; Lebanon includes the Phoenician coast |
| maccabean-judea | pass | all five checks confirmed |
| kingdom-of-emesa | pass | all four checks confirmed |
| cyrene-under-ptolemy-viii | pass | all five checks confirmed |
| revolt-of-timarchus | pass | checks confirmed; Babylonia year confidence 1 |
| phoenician-and-cypriot-rebels | thin | half the ledger confidence 1 (start undated); ruler span fixed (applied) |
| bessus-artaxerxes-v | pass | checks confirmed |
| cleopatra-ii-alexandria | fix | war start moved inside the life (applied) |
| tarcondimotid-dynasty | fail | duplicate of tarcondimotid-kingdom; 31 BC vassal_end contradicts the page |
| harsiesi | pass | checks confirmed |
| yehud-medinata | fix | 538 'gain' marker removed (applied) |

Verdict 'fix' with every finding applied means fixed by the reviewer; tetrarchy-of-philip and kingdom-of-herod-agrippa-i keep unapplied, non-blocking findings for the author. 'fail' goes back to the author (itureans) or to the orchestrator (tarcondimotid-dynasty, duplicate).

## cyrene-and-barca: pass

Thin (for a gap-filler):
- `/ledger/1`: How Barca and the other Pentapolis cities came under Cyrene before 525 (confidence 1 bridge; counterpart 'Barca (city-state)' has no dossier) (try https://en.wikipedia.org/wiki/Barca_(ancient_city))

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Cyrene,_Libya: confirmed: 'founded Cyrene in 631 BC, under the leadership of Battus I'
- `/ledger/2` https://en.wikipedia.org/wiki/Cyrenaica: confirmed: 'In 525 BC, after conquering Egypt, the Achaemenid (Persian) army of Cambyses II seized the Pentapolis'; satrapy 'for about the next two centuries'
- `/ledger/3` https://en.wikipedia.org/wiki/Arcesilaus_IV_of_Cyrene: confirmed: 'Arcesilaus, along with his son, were killed by the Cyrenaean citizens in 440 BC'; 'a narrow democracy'; 'client king under Persian authority'
- `/ledger/4` https://en.wikipedia.org/wiki/Cyrenaica: confirmed: 'The Persians were followed by Alexander the Great in 332 BC, who received tribute from the cities'; infobox 'Republic (440-322 BC)' (the Cyrene page puts Alexander's Egypt in 331 and says the cities 'did not come under Macedonian control')

Area: No infobox area on Cyrenaica or Cyrene pages; 525-333 drawn as Cliopatria Cyrenaica -331 (30,697 km2), 631-526 as a 45 km circle round Cyrene; plausible for the Pentapolis.

## lycian-league: fix

Findings:
- `/ledger/3, /ledger/4, /wars/0/belligerents` (applied by reviewer). The 42 BC occupation of Xanthos named roman-republic as occupier, but the occupier was Brutus's Liberators' faction, which the roman-republic dossier treats as a separate counterpart fighting the Republic in 43-42. Evidence: Xanthos page: 'In 42 BC, during the Liberators' civil war, Brutus came to Lycia to obtain funds before the Battle of Philippi. He besieged Xanthos after the Lycian League refused to contribute.' roman-republic /ledger/188 and /ledger/191 use the counterpart string "Liberators' faction (Brutus and Cassius)". Fix: Counterpart of both occupation events and the war belligerent set to "Liberators' faction (Brutus and Cassius)"; re-validated clean.

Thin (for a gap-filler):
- `/ledger/4`: End of Brutus's occupation (confidence 1; page silent) (try https://en.wikipedia.org/wiki/Liberators%27_civil_war)
- `/ledger/5, /ledger/6`: 27 BC hand-over of the protectorate from Republic to Principate is a constitutional bridge (confidence 1) (try https://en.wikipedia.org/wiki/Lycia_et_Pamphylia)
- `/ledger (new)`: First and Second Mithridatic Wars (88-81) and whether Cibyra's tetrapolis was League land are undated on the pages (try https://en.wikipedia.org/wiki/First_Mithridatic_War)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Lycian_League: confirmed: 'Lycia was granted autonomy as a protectorate of Rome in 168 BC'
- `/ledger/1` https://en.wikipedia.org/wiki/Lycia: confirmed: 'awarded to Rhodes in the Peace of Apamea in 188 BC', 'taking it back in 168 BC'; senate decree of 169 'gave the Carians and the Lycians their freedom'
- `/ledger/3` https://en.wikipedia.org/wiki/Xanthos: confirmed (year); counterpart corrected: 'In 42 BC, during the Liberators' civil war, Brutus came to Lycia'
- `/ledger/8` https://en.wikipedia.org/wiki/Lycian_League: confirmed: 'In 43 AD the emperor Claudius annexed Lycia'; the page contradicts itself on whether the League was dissolved or retained, as the author noted

Area: No area on the Lycian League or Lycia pages; drawn as gazetteer region Lycia (Teke peninsula).

## kingdom-of-antiochus-hierax: fix

Findings:
- `/identity/capitals/0/lon` (applied by reviewer). Sardis was placed at longitude 26.03, in the Aegean off Karaburun, outside the state's land. Evidence: Sardis page: '38°29′18″N 28°02′25″E'. Fix: lon set to 28.04; note extended; re-validated clean.
- `/identity/rulers/0/to` (applied by reviewer). Ruler span (to -226) ran past the state's end (-228). Evidence: Brief rule 2: rulers inside the life; Seleucus II page: Hierax 'killed by robbers in c. 226 BC' after losing all land by 228. Fix: to set to -228 with a note; re-validated clean.
- `/ledger/5/note` (applied by reviewer). Note called the battle near Sardis 'the last battle'; the page puts the last fight at the Harpasus in Caria. Evidence: Attalus I page: battle 'near Sardis in the spring of 228 BC' is one of three later battles; the campaign ended 'in Caria at the Battle of the Harpasus'. Fix: Note rewritten; year 228 kept.

Thin (for a gap-filler):
- `/ledger/1`: First campaigns of the War of the Brothers (Lydia, Sardis) undated; the Seleucus II page says Seleucus 'was unable to take Sardis', which also supports Sardis as Hierax's seat (try https://en.wikipedia.org/wiki/War_of_the_Brothers)

Spot checks:
- `/ledger/2` https://en.wikipedia.org/wiki/Seleucus_II_Callinicus: confirmed: 'After two years of stalemate, the brothers met at the Battle of Ancyra around 237 BC'
- `/ledger/3` https://en.wikipedia.org/wiki/Seleucus_II_Callinicus: confirmed: 'After this Seleucus left the country beyond the Taurus to his brother' (no own year; dated by Ancyra)
- `/ledger/5` https://en.wikipedia.org/wiki/Attalus_I: confirmed year: 'near Sardis in the spring of 228 BC'; note corrected (last battle was the Harpasus)
- `/ledger/6` https://en.wikipedia.org/wiki/Attalus_I: confirmed: 'Attalus gained putative control over all of Seleucid Asia Minor north of the Taurus Mountains'

Area: Rebel kingdom; person pages give no area. Drawn as Seleucid -239 shape inside Anatolia minus Cilicia.

## hecatomnid-caria: pass

Thin (for a gap-filler):
- `/ledger/2`: Year of the move from Mylasa to Halicarnassus (confidence 1) (try https://en.wikipedia.org/wiki/Mausoleum_at_Halicarnassus)
- `/ledger/8`: When Lycia and the Dodecanese left Hecatomnid control (confidence 1 bridge to 334) (try https://en.wikipedia.org/wiki/Pixodarus)
- `/identity/end`: Ada I's second reign under Alexander (334 to between 334 and 323 per the dynasty page) is not drawn; a vassal pair against macedonian-empire would cover it (try https://en.wikipedia.org/wiki/Ada_of_Caria)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Hecatomnid_dynasty: confirmed: 'Hecatomnus therefore became satrap of Caria c. 395 - c. 392 BCE'; 'ruled with considerable autonomy as a hereditary dynasty'
- `/ledger/4` https://en.wikipedia.org/wiki/Hecatomnid_dynasty: confirmed (undated): 'Greek islands of the Dodecanese such as Rhodes after their participation in the Social War against Athens'; 355 from the war's end, confidence 2 is right
- `/ledger/5` https://en.wikipedia.org/wiki/Siege_of_Halicarnassus: confirmed: 'fought between Alexander the Great and the Achaemenid Persian Empire in 334 BC'
- `/ledger/7` https://en.wikipedia.org/wiki/Siege_of_Halicarnassus: confirmed: infobox 'Territorial changes: Alexander captures Caria'; 'Alexander committed the government of Caria to Ada'

Area: No area on the dynasty page ('rulers of Caria and surrounding areas c. 395 - c. 330 BCE'); drawn as gazetteer Caria, Lycia, Dodecanese.

## tetrarchy-of-galilee-and-peraea: pass

Thin (for a gap-filler):
- `/ledger/2`: Year Antipas moved his seat to Tiberias (confidence 1, 14 is a lower bound) (try https://en.wikipedia.org/wiki/Tiberias)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Herodian_tetrarchy: confirmed: 'Herod Antipas, Archelaus' brother, became Tetrarch of Galilee and Perea'; infobox 'Sepphoris later Tiberias'
- `/ledger/3` https://en.wikipedia.org/wiki/Herodian_tetrarchy: confirmed: 'Herod Antipas ruled Galilee and Perea until 39 CE'
- `/ledger/4` https://en.wikipedia.org/wiki/Herodian_tetrarchy: confirmed: 'After the banishment of Herod Antipas in 39 CE Herod Agrippa I became also ruler of Galilee and Perea'
- `/ledger/5` https://en.wikipedia.org/wiki/Herodian_tetrarchy: confirmed (39 banishment)

Area: No area on the pages; Galilee + Gilead stand-ins. Gilead includes Jordan's Irbid governorate, which tetrarchy-of-philip also claims (see that dossier).

## tetrarchy-of-philip: fix

Findings:
- `/ledger/0-4/region, /keyframe_review/0/correction, /identity/successors` (for the author). The 'Hauran' stand-in includes Jordan's Irbid governorate, which tetrarchy-of-galilee-and-peraea (Gilead stand-in) also holds from -4 to 34: two dossiers of this batch claim the same cells for 38 years, and Irbid (Gadara, Abila, Capitolias) was Decapolis land, not Philip's. Evidence: Gazetteer: Hauran = As Suwayda' + Dar`a + Quneitra (Syria) + Irbid (Jordan); Gilead = Irbid + Ajlun + Jarash + Balqa. Herodian tetrarchy page lists Philip's districts as 'Iturea, Trachonitis, Batanea, Gaulanitis, Auranitis and Paneas', all north and east of the Yarmuk. Fix: Replace {"region":"Hauran"} by {"union":[{"admin1":"As Suwayda'","country":"Syria"},{"admin1":"Dar`a","country":"Syria"},{"admin1":"Quneitra","country":"Syria"}]} in every region of this dossier (and in kingdom-of-herod-agrippa-i's 37 grant), keeping Golan.

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Herodian_tetrarchy: confirmed: 'Philip ruled Iturea, Trachonitis, Batanea, Gaulanitis, Auranitis and Paneas as a tetrarch until his death in 34 CE'
- `/ledger/2` https://en.wikipedia.org/wiki/Herodian_tetrarchy: confirmed: 34 CE death
- `/ledger/3` https://en.wikipedia.org/wiki/Herodian_tetrarchy: confirmed: 'when his territories became briefly part of the Roman province of Syria'
- `/ledger/4` https://en.wikipedia.org/wiki/Herodian_tetrarchy: confirmed: 'in 37 CE were given to Herod Agrippa I with the title of king' (successor)

Area: No area on the pages; Golan + Hauran stand-ins (Hauran overreaches into Jordan, see fix).

## kingdom-of-herod-agrippa-i: fix

Findings:
- `/ledger/4/source` (applied by reviewer). The 39 gain at confidence 3 cited the Herod Agrippa page, which dates the grant of 'Galilee and Perea in 40' (text and infobox). Evidence: Herodian tetrarchy page: 'After the banishment of Herod Antipas in 39 CE Herod Agrippa I became also ruler of Galilee and Perea'. Fix: Source set to the Herodian tetrarchy page and the note rewritten to quote it and record the Herod Agrippa page's 40; re-validated clean.
- `/identity/capitals` (for the author). No capital for 37-40 (Jerusalem starts 41). Evidence: Brief rule 2: capitals contiguous over the life; the dossier's capitals start at 41 while the state starts at 37. Fix: Add a capital for 37-40 (Caesarea Philippi/Paneas, Philip's former capital per the Herodian tetrarchy infobox, at confidence of a reading) or say in /notes that no page names one.
- `/ledger/0, /ledger/1, /keyframe_review/0` (for the author). The 37-38 shape inherits the 'Hauran' stand-in that reaches into Jordan's Irbid governorate, which tetrarchy-of-galilee-and-peraea still holds until 39. Evidence: See tetrarchy-of-philip finding. Fix: Use the Syrian admin1 units for Philip's former lands, as in the tetrarchy-of-philip fix.

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Herod_Agrippa: confirmed: 'in 37 by obtaining the old tetrarchies of Philip and Lysanias'
- `/ledger/1` https://en.wikipedia.org/wiki/Herodian_tetrarchy: confirmed: Philip's lands 'in 37 CE were given to Herod Agrippa I with the title of king'
- `/ledger/4` https://en.wikipedia.org/wiki/Herodian_tetrarchy: confirmed 39 on the Herodian tetrarchy page; the cited Herod Agrippa page says 40 (source switched)
- `/ledger/5` https://en.wikipedia.org/wiki/Herod_Agrippa: confirmed: 'he was endowed with the former territories of Herod Archelaus'; Herodian tetrarchy: 'in 41 CE ... King of Iudaea'
- `/ledger/8` https://en.wikipedia.org/wiki/Herod_Agrippa: confirmed: 'Agrippa I died unexpectedly in 44'; 'Claudius made it a Roman province with Cuspius Fadus as procurator'

Area: No area on the pages; the 41-44 realm is the union of the tetrarchies and Judea, Samaria, Caesarea and the northern Negev.

## itureans: fail

Findings:
- `/ledger/5/region, /keyframe_review/2/correction, /ledger/6-7, /identity/successors/0/land` (for the author). The 23-20 BC shape adds the gazetteer 'Damascus (region)' (an 80 km circle round Damascus, 72 cells, about 18,000 km2), which contains Damascus itself, whereas the page places Zenodorus's extra lands 'south of Damascus (Ulatha and Paneas)'; the area roughly triples on a confidence-1 event with counterpart 'nobody'. Evidence: Zenodorus son of Lysanias page: 'areas south of Damascus (Ulatha and Paneas, both, we are told, west of Trachonitis)'; Ituraea page: 'About 23 BC, Iturea with the adjacent provinces fell into the hands of a chief named Zenodorus' (a change of ruler, not a dated gain from nobody). Gazetteer: 'Damascus (region)' = {place: Damascus, km: 80, country: Syria}. Fix: Replace the stand-in by Ulatha and Paneas: {"lon": 35.69, "lat": 33.15, "km": 20} (Banias is not in the gazetteer) (Paneas and the Huleh) with text naming both; give the event a counterpart the page supports or make it a rename (Zenodorus) and drop the gain.
- `/ledger/0/region, /keyframe_review/0-2/correction` (for the author). The base is drawn as the whole country of Lebanon, which includes the Phoenician coastal cities (Tyre, Sidon, Berytus) that were never Iturean, and overlaps the Roman province of Syria from 64 BC. Evidence: Ituraea page: 'It extended from Mount Lebanon across the plain of Marsyas to the Anti-Lebanon Mountains in Syria, with its centre in Chalcis ad Libanum'; Itureans page: 'from their base around Mount Lebanon and the Beqaa Valley'. Fix: Use {"union":[{"admin1":"Beqaa","country":"Lebanon"},{"admin1":"Mount Lebanon","country":"Lebanon"}]} (plus an Anti-Lebanon polygon if wanted) instead of {"country":"Lebanon"}.
- `/ledger/0/region vs /keyframe_review/0/correction` (for the author). The first keyframe (-105..-104) includes Galilee but the found event's region is Lebanon only, so Galilee appears with no event. Evidence: K0 correction = Lebanon + Galilee; /ledger/0 region = Lebanon; the next Galilee event is the 103 loss. Fix: Add Galilee to the found region (with the judea dossier's reading in text) or drop it from K0 and from the 105-103 contest.

Thin (for a gap-filler):
- `/ledger/0`: Origin and founding year of the Iturean principality (confidence 1) (try https://en.wikipedia.org/wiki/Herod_of_Chalcis)
- `/ledger (new)`: Pompey's settlement of 64-63 BC (Ptolemy son of Mennaeus as Roman client) and the Roman client status 63-20: no vassal events at all (try https://en.wikipedia.org/wiki/Third_Mithridatic_War)
- `/ledger/2, /ledger/3`: End of Aristobulus I's campaign and the Galilee loss (confidence 1, mirrors judea) (try https://en.wikipedia.org/wiki/Aristobulus_I)
- `/ledger/5`: Zenodorus's lands and the 23 BC confiscation of Trachonitis/Auranitis (judea gains Hauran in 22) (try https://en.wikipedia.org/wiki/Zenodorus_son_of_Lysanias)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Ituraea: confirmed: 'In 105 BCE, Hasmonean leader Aristobulus I campaigned against Iturea'
- `/ledger/4` https://en.wikipedia.org/wiki/Zenodorus_son_of_Lysanias: confirmed: lease 'as far back as the time of his father's execution (36 BCE)', 'initially paying rent to Cleopatra'
- `/ledger/5` https://en.wikipedia.org/wiki/Ituraea: sentence confirmed ('About 23 BC, Iturea with the adjacent provinces fell into the hands of a chief named Zenodorus') but it is a change of ruler; the Damascus region drawn is contradicted by 'areas south of Damascus' on the Zenodorus page
- `/ledger/6` https://en.wikipedia.org/wiki/Ituraea: confirmed: 'Three years later, at the death of Zenodorus, Augustus gave Iturea to Herod the Great'

Area: No area on the pages. Drawn: Lebanon (35 cells, about 8,900 km2) for -103..-24, then Lebanon + Damascus (region) (about 27,000 km2) for -23..-20: a factor of three on a confidence-1 stand-in, not acknowledged as a size change.

## maccabean-judea: pass

Thin (for a gap-filler):
- `/ledger/6`: Year of the Ekron grant and the three Samaritan toparchies (confidence 1) (try https://en.wikipedia.org/wiki/Jonathan_Apphus)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Maccabean_Revolt: confirmed: 'rebelling in 167 BCE and seeking independence'
- `/ledger/2` https://en.wikipedia.org/wiki/Maccabean_Revolt: confirmed: 'In 164 BCE, the Maccabees captured Jerusalem'
- `/ledger/3` https://en.wikipedia.org/wiki/Maccabean_Revolt: confirmed: 'Judas Maccabeus died in 160 BCE at the Battle of Elasa'; infobox 'Seleucid authority in major cities reestablished from 160-152 BCE'
- `/ledger/5` https://en.wikipedia.org/wiki/Maccabean_Revolt: confirmed: 'From 152-141 BCE, the rebels achieved a state of informal autonomy akin to a vassal'
- `/ledger/7` https://en.wikipedia.org/wiki/Maccabean_Revolt: confirmed: 'Demetrius II exempted Judea from payment of taxes in 142 BCE, essentially acknowledging its independence'

Area: Rebel state; drawn on Cliopatria Judea -144 (5,733 km2), the earliest Judea outline; the page gives no area.

## kingdom-of-emesa: pass

Thin (for a gap-filler):
- `/ledger/2`: Year Iamblichus I moved the capital from Arethusa to Emesa (confidence 1) (try https://en.wikipedia.org/wiki/Iamblichus_(phylarch))
- `/ledger (new)`: Pompey's 63 settlement, Antony's execution of Iamblichus I (31) and Nero's grant of Sophene are undated on the one page (try https://en.wikipedia.org/wiki/Sohaemus_of_Emesa)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Emesene_dynasty: confirmed: 'Sampsiceramus I captured and killed the penultimate Seleucid King Antiochus XIII Asiaticus in 64 BC'; 'a Roman client dynasty of Arab priest-kings known to have ruled by 46 BC from Arethusa'
- `/ledger/4` https://en.wikipedia.org/wiki/Emesene_dynasty: confirmed: 'From 30 BC until 20 BC, the Emesene Kingdom was dissolved and became an autonomous community'
- `/ledger/5` https://en.wikipedia.org/wiki/Emesene_dynasty: confirmed: 'Later in 20 BC, Octavian, now as the Roman emperor Augustus, restored the Emesene Kingdom to Iamblichus II'
- `/ledger/8` https://en.wikipedia.org/wiki/Emesene_dynasty: confirmed: 'after his death in 78, the Kingdom most probably was absorbed by the Roman Province of Syria'; infobox 'likely between 72 and 78/79'

Area: No area on the page; it gives the bounds (Beqaa to the Palmyra border, Yabrud to Arethusa, Heliopolis), which the two circles follow.

## cyrene-under-ptolemy-viii: pass

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Ptolemy_VIII_Physcon: confirmed: 'he was expelled in turn in 163 BC'; 'As a result of Roman intervention, Ptolemy VIII was awarded control of Cyrene' (award undated, confidence 2 right)
- `/ledger/3` https://en.wikipedia.org/wiki/Ptolemy_VIII_Physcon: confirmed: 'He regained control over Cyrene by the end of 162 BC'
- `/ledger/4` https://en.wikipedia.org/wiki/Ptolemy_VIII_Physcon: confirmed: 'He launched a military expedition to Cyprus in 161 BC'; 'lasted up to a year'
- `/ledger/7` https://en.wikipedia.org/wiki/Ptolemy_VIII_Physcon: confirmed: besieged 'at Lapethus and was captured' after the 154 BC embassy; 'persuaded to withdraw from Cyprus, in exchange for continued possession of Cyrenaica'
- `/ledger/8` https://en.wikipedia.org/wiki/Ptolemy_VIII_Physcon: confirmed: 'On his return to Alexandria in 145 BC'

Area: Drawn on Cliopatria Cyrenaica -110 (116,348 km2); the Cyrenaica infobox lists 'Kingdom (... 163-96 BC ...)', which this dossier and cyrenaica share without overlap.

## revolt-of-timarchus: pass

Thin (for a gap-filler):
- `/ledger/2`: Year Timarchus extended his realm into Babylonia (confidence 1; 161 follows seleucid-empire) (try https://en.wikipedia.org/wiki/Timarchus)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Timarchus: confirmed: infobox 'Reign: 163-160 BC'; proclamation undated (confidence 2 right)
- `/ledger/1` https://en.wikipedia.org/wiki/Timarchus: confirmed: 'He was appointed satrap of Media in western Iran when Antiochus IV Epiphanes became king in 175 BC'
- `/ledger/4` https://en.wikipedia.org/wiki/Demetrius_I_Soter: confirmed: 'Demetrius defeated and killed Timarchus in 160 BC'
- `/ledger/5` https://en.wikipedia.org/wiki/Timarchus: confirmed: 'Demetrius defeated and killed Timarchus in 160 BC, and the Seleucid empire was temporarily united again'

Area: Rebel kingdom; no area on the pages. Media minus Atropatene, plus Babylonia from 161.

## phoenician-and-cypriot-rebels: thin

Findings:
- `/identity/rulers/0/from` (applied by reviewer). Ruler span (from -351) started before the state (-350). Evidence: Brief rule 2: rulers inside the life; Tennes page 'r. c. 351 - c. 346'. Fix: from set to -350 with a note; re-validated clean.
- `/identity/capitals` (for the author). No capital for -345..-343 (Sidon ends -346; the Cypriot rump lasts to -343). Evidence: Capital coverage check: Sidon -350..-346 only. Fix: Add the Cypriot seat (e.g. Salamis) for -345..-343 or say in /notes that no page names one.

Thin (for a gap-filler):
- `/ledger/0, /ledger/1, /ledger/3`: Start of the revolt: no page dates it (confidence 1; the Sidon page has Phoenicia invaded in 351) (try https://en.wikipedia.org/wiki/Tennes)
- `/ledger/2`: Cyprus's revolt and its kings (Pnytagoras, Evagoras II) undated (confidence 1) (try https://en.wikipedia.org/wiki/Evagoras_II)
- `/ledger/4`: Fall of Sidon: the Artaxerxes III page gives no year; 346 rests on the Mentor page's capture (try https://en.wikipedia.org/wiki/Sidon)

Spot checks:
- `/ledger/2` https://en.wikipedia.org/wiki/Artaxerxes_III: confirmed (undated, confidence 1 right): 'Soon after this Egyptian defeat, Phoenicia, Anatolia and Cyprus declared their independence from Persian rule'
- `/ledger/4` https://en.wikipedia.org/wiki/Mentor_of_Rhodes: confirmed: 'he was unable to defeat Artaxerxes' army, and was captured in 346 BC'
- `/ledger/5` https://en.wikipedia.org/wiki/Artaxerxes_III: confirmed: 'In 343 BC, Artaxerxes committed responsibility for the suppression of the Cyprian rebels to Idrieus'; 'Idrieus succeeded in reducing Cyprus'
- `/ledger/6` https://en.wikipedia.org/wiki/Artaxerxes_III: confirmed: Egypt reconquered 'probably in 340 or 339 BC', as the author's notes say

Area: Rebel coalition; no area on the pages. Phoenicia (Lebanon + Syrian coast) and Cyprus.

## bessus-artaxerxes-v: pass

Thin (for a gap-filler):
- `/ledger/2`: Start of Alexander's pursuit into Bactria (confidence 1) (try https://en.wikipedia.org/wiki/Wars_of_Alexander_the_Great)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Bessus: confirmed: 'In the autumn of 330, at the Bactrian capital of Bactra, Bessus declared himself King of Kings of the Achaemenid Empire'
- `/ledger/1` https://en.wikipedia.org/wiki/Bessus: confirmed: 'His domain encompassed Bactria, the main center; Sogdia, administered by officers such as Spitamenes and Oxyartes' (wider realm narrowed by design, explained in notes)
- `/ledger/3` https://en.wikipedia.org/wiki/Bessus: confirmed: 'Bessus was arrested by his Sogdian officers, who included Spitamenes, Dataphernes, and Catanes'
- `/ledger/5` https://en.wikipedia.org/wiki/Bessus: confirmed: infobox 'Reign: 330-329 BC', 'Died: 329 BC Ecbatana'

Area: Rebel claimant; no area. Bactria + Sogdia.

## cleopatra-ii-alexandria: fix

Findings:
- `/wars/0/from` (applied by reviewer). War started in -132, before the state's start (-131). Evidence: Brief rule 2: wars inside the life; Cleopatra II page: 'led a rebellion against Ptolemy VIII in 132/1 BC' and 'drove him and Cleopatra III out of Alexandria at the end of 131 BC'. Fix: from set to -131 with a note; re-validated clean.

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Cleopatra_II_of_Egypt: confirmed: 'drove him and Cleopatra III out of Alexandria at the end of 131 BC'
- `/ledger/1` https://en.wikipedia.org/wiki/Cleopatra_II_of_Egypt: confirmed: 'Ptolemy VIII had retained the allegiance of parts of Egypt and gradually expanded his control from there'
- `/ledger/3` https://en.wikipedia.org/wiki/Cleopatra_II_of_Egypt: confirmed: 'In 127 BC, he took over Alexandria, Cleopatra II being forced to flee to Syria'
- `/ledger/5` https://en.wikipedia.org/wiki/Cleopatra_II_of_Egypt: confirmed: 'Cleopatra II ruled in Alexandria as sole ruler until 127 BC'

Area: Rebel regime; Alexandria 40 km circle; no area on the page.

## tarcondimotid-dynasty: fail

Findings:
- `/identity/slug` (for the author). Duplicate state: history/polities/tarcondimotid-kingdom.json (written by eu-04-x at 13:07, reviewed fail in review-eu-04-x) is the same Tarcondimotid client kingdom of Upper Cilicia, -38..17, from the same single page; this dossier (13:41) was created without finding it. Evidence: Both cite only https://en.wikipedia.org/wiki/Tarcondimotus_I; tarcondimotid-kingdom identity 'Tarcondimotid Kingdom' -38..17, dissolve 17 to roman-empire; eu-04-x notes '## tarcondimotid-kingdom'. Fix: Keep one dossier (orchestrator to choose the slug; tarcondimotid-kingdom is the earlier and is named in eu-04-x's review). Carry this dossier's -66 start (Pompey's toparchy, which the eu-04-x reviewer asked for) and vassal pairs into it and delete the other file.
- `/ledger/3` (for the author). The 31 BC vassal_end (confidence 1) says the page is silent on 31-20 BC and leaves the land outside Roman clientage for eleven years, but the page says the dynasty kept its land as a toparchy under Octavian. Evidence: Tarcondimotus I page: Octavian 'would strip him of the royal title within the year', though Philopator 'appears to have retained his position as toparch of Upper Cilicia'; 'In 20 BC, Augustus restored the royal title to Tarcondimotus II'. Fix: Replace /ledger/3 by a rename at -30 (royal title stripped, toparchy kept); hand the client relation over at -27 (vassal_end roman-republic, vassal_start roman-empire, the convention used elsewhere); make -20 a rename (title restored) instead of a vassal_start.
- `/identity/capitals` (for the author). No capital for -66..-20 (Anazarbos only from -19). Evidence: Tarcondimotus I page: 'The core of Tarcondimotus' territory comprised the cities of Anazarbus and Castabala'. Fix: Add Castabala (Hierapolis-Castabala, about 36.20 E 37.25 N) or Anazarbus from -66.

Thin (for a gap-filler):
- `/ledger (new)`: Parthian invasion of 40 BC and the border with Cilicia Trachea (try https://en.wikipedia.org/wiki/Anazarbus)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Tarcondimotus_I: confirmed: 'was confirmed as toparch by Pompey in or after 66 BC'
- `/ledger/2` https://en.wikipedia.org/wiki/Tarcondimotus_I: confirmed: 'was formally recognized as king by Mark Antony c.38 BC'
- `/ledger/3` https://en.wikipedia.org/wiki/Tarcondimotus_I: not on page as claimed: the note says the page is silent on 31-20, but it says Philopator 'appears to have retained his position as toparch of Upper Cilicia'
- `/ledger/4` https://en.wikipedia.org/wiki/Tarcondimotus_I: confirmed: 'In 20 BC, Augustus restored the royal title to Tarcondimotus II'
- `/ledger/5` https://en.wikipedia.org/wiki/Tarcondimotus_I: confirmed: 'the last Tarcondimotid king who died in AD 17'; 'Tiberius resolved the question by incorporating the territory directly within the Roman provincial system'

Area: No area on the page; Osmaniye province plus a 35 km circle at Anazarbos.

## harsiesi: pass

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Harsiesi: confirmed: 'Harsiesi captured Thebes in the summer of 131 BC'; infobox 'Reign: 131-130 BC' (Ptolemy VIII page: 'in August or September of 131 BC')
- `/ledger/2` https://en.wikipedia.org/wiki/Harsiesi: confirmed: 'Ptolemy's forces recaptured the city in November of the same year'
- `/ledger/3` https://en.wikipedia.org/wiki/Harsiesi: confirmed: 'Harsiesi led the rebellion until his death, which likely occurred in September 130 BC'; 'ruling only in the southern part of Upper Egypt', which supports the 130 rump
- `/ledger/4` https://en.wikipedia.org/wiki/Harsiesi: confirmed (as /ledger/3)

Area: Rebel; 80 km circle round Thebes ('the southern part of Upper Egypt'); no area on the page.

## yehud-medinata: fix

Findings:
- `/ledger/2` (applied by reviewer). A 538 'gain from nobody' of the province's own land was a marker for the return of the deportees: no land moved, and a gain is drawn as newly acquired land. Evidence: Yehud Medinata page: Cyrus 'decreed that the deportees in Babylon could return to Yehud'; the author's own note: 'No change of land is recorded'. Fix: Event removed; the 538 return moved into /ledger/0's note and /notes updated; re-validated clean.

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Yehud_Medinata: confirmed: 'Upon the Persian conquest of Babylon in 539 BCE, the Achaemenid Empire established its own Yehud province'; infobox 'c. 539 BCE-c. 332 BCE'
- `/ledger/1` https://en.wikipedia.org/wiki/Yehud_Medinata: confirmed: 'one of twenty provinces or administrative subunits in the large satrapy of Eber-nari'
- `/ledger/2 (removed)` https://en.wikipedia.org/wiki/Yehud_Medinata: confirmed as a population event, not a land change: 'Sheshbazzar, the governor of Yehud appointed by Cyrus in 538'
- `/ledger/3` https://en.wikipedia.org/wiki/Yehud_Medinata: confirmed: 'Mizpah continued as the provincial capital for over a century'; 'From 445 BCE onwards, it was once more the main city of Yehud'

Area: No area on the page ('from around Bethel in the north to near Hebron in the south'; population about 30,000); the circles (about 3,800 km2) are a generous reading, acknowledged in the keyframe note.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| cyrene-and-barca -525 gain (Barca (city-state)) | - | exception | No dossier; listed in counterparts_needing_dossiers (barca). |
| cyrene-and-barca -525 vassal_start (achaemenid-empire) | achaemenid-empire -525 vassal_start | matched | achaemenid-empire /ledger/11. |
| cyrene-and-barca -332 vassal_end (achaemenid-empire) | achaemenid-empire -404 vassal_end | mismatch | achaemenid-empire /ledger/30 ends the tint in 404 (confidence 1, page silent); Cyrenaica page: satrapy 'for about the next two centuries' after 525 and Alexander's tribute in 332. Route to me-05-a: move to 332 (or 330 with the empire's end). |
| cyrene-and-barca -332 dissolve (cyrenaica) | cyrenaica -332 found | matched | cyrenaica /ledger/0 found -332 (its counterpart 'nobody' could name cyrene-and-barca; me-05-a). |
| lycian-league -168 gain (rhodes) | rhodes -167 loss | mismatch | rhodes /ledger/4 loses the Peraia/Lycia in 167 to 'nobody' (and /ledger/3 vassal_end 'Caria and Lycia (tributary communities)'); Lycia page: 'taking it back in 168 BC'. Route to eu-02-b: name lycian-league as counterpart; year within one. |
| lycian-league -168 vassal_start (roman-republic) | - | missing | roman-republic has no Lycian vassal events, and its /ledger/156 (-74) gains Lycia from 'Isaurians and Cilician pirates' at confidence 3, which contradicts the League's autonomous Lycia 168-43 BC ('granted autonomy as a protectorate of Rome in 168 BC ... until becoming a Roman province in 43 AD'). Route to eu-03-b. |
| lycian-league -42 occupation_start (Liberators' faction (Brutus and Cassius)) | - | exception | Counterpart corrected by the reviewer from roman-republic; the Liberators have no dossier (roman-republic contests them 43-42 by name, zones without Lycia). |
| lycian-league -27 vassal_end (roman-republic) | - | missing | Convention hand-over; roman-republic has no Lycian events (eu-03-b). |
| lycian-league -27 vassal_start (roman-empire) | - | missing | roman-empire lists other clients at -27 (judea, cappadocia, commagene...) but not lycian-league. Route to eu-04-a. |
| lycian-league 43 loss (roman-empire) | - | missing | roman-empire has no AD 43 gain of Lycia or vassal_end lycian-league. Route to eu-04-a. |
| kingdom-of-antiochus-hierax -240 contest_start (seleucid-empire) | - | missing | seleucid-empire has no Hierax events between 241 and 227. Route to me-05-c (author already asked). |
| kingdom-of-antiochus-hierax -237 gain (seleucid-empire) | - | missing | seleucid-empire needs the 237 loss of Asia Minor beyond the Taurus (Seleucus II page: 'left the country beyond the Taurus to his brother'). me-05-c. |
| kingdom-of-antiochus-hierax -230 contest_start (kingdom-of-pergamon) | kingdom-of-pergamon -230 contest_start | mismatch | kingdom-of-pergamon /ledger/2 names seleucid-empire; should name kingdom-of-antiochus-hierax. Route to me-05-d. |
| kingdom-of-antiochus-hierax -228 loss (kingdom-of-pergamon) | kingdom-of-pergamon -227 gain | mismatch | kingdom-of-pergamon /ledger/3-4 (-227) name seleucid-empire and gain only Pergamon -225 minus -279 (about 31,000 km2), while Hierax loses all Seleucid Asia Minor north of the Taurus to Pergamon ('putative control'). Counterpart name and land disagree; year within one. Route to me-05-d (and the land not taken by Pergamon back to seleucid-empire, me-05-c). |
| hecatomnid-caria -392 vassal_start (achaemenid-empire) | - | missing | achaemenid-empire has no Hecatomnid events. Route to me-05-a. |
| hecatomnid-caria -362 gain (achaemenid-empire) | - | missing | achaemenid-empire has no Lycia transfer to the Hecatomnids (Hecatomnid page: 'gaining control of Lycia after the Revolt of the Satraps'). me-05-a. |
| hecatomnid-caria -355 gain (rhodes) | - | missing | rhodes has no event 360-350; needs the loss to hecatomnid-caria after the Social War. Route to eu-02-b (author asked). |
| hecatomnid-caria -334 loss (macedonian-empire) | macedonian-empire -334 gain | mismatch | macedonian-empire /ledger/23 gains Caria, Lycia (and the coast) in May 334 from achaemenid-empire; Caria, Lycia and the Dodecanese should name hecatomnid-caria. Route to eu-02-a. |
| hecatomnid-caria -334 vassal_end (achaemenid-empire) | - | missing | me-05-a. |
| tetrarchy-of-galilee-and-peraea -4 found (judea) | judea -4 split | matched | judea /ledger/34. |
| tetrarchy-of-galilee-and-peraea -4 vassal_start (roman-empire) | - | missing | roman-empire lists judea as client from -27 but not the tetrarchies after the 4 BC split. Route to eu-04-a. |
| tetrarchy-of-galilee-and-peraea 39 loss (kingdom-of-herod-agrippa-i) | kingdom-of-herod-agrippa-i 39 gain | matched | kingdom-of-herod-agrippa-i /ledger/4. |
| tetrarchy-of-philip -4 found (judea) | judea -4 split | matched | judea /ledger/35. |
| tetrarchy-of-philip -4 vassal_start (roman-empire) | - | missing | eu-04-a. |
| tetrarchy-of-philip 34 loss (roman-empire) | - | missing | roman-empire has no AD 34 gain of Philip's lands (Herodian tetrarchy: 'became briefly part of the Roman province of Syria'). eu-04-a. |
| kingdom-of-herod-agrippa-i 37 gain (roman-empire) | - | missing | roman-empire has no AD 37 loss of Philip's former lands. eu-04-a. |
| kingdom-of-herod-agrippa-i 37 gain (Tetrarchy of Lysanias (Abilene)) | - | exception | No dossier; listed in counterparts_needing_dossiers. |
| kingdom-of-herod-agrippa-i 37 vassal_start (roman-empire) | roman-empire 41 vassal_start | mismatch | roman-empire /ledger/34 opens a client 'judea' in 41 (judea dossier ends AD 6); it should be kingdom-of-herod-agrippa-i from 37. Route to eu-04-a. |
| kingdom-of-herod-agrippa-i 41 gain (roman-empire) | - | missing | roman-empire has no AD 41 loss of Judea, Samaria and Idumea (only the vassal_start 'judea'). eu-04-a. |
| kingdom-of-herod-agrippa-i 44 loss (roman-empire) | roman-empire 44 gain | mismatch | roman-empire /ledger/36-37 (44 vassal_end and gain) name judea; rename to kingdom-of-herod-agrippa-i. eu-04-a. |
| itureans -105 contest_start (judea) | - | missing | judea has no contest with the Itureans, only the -103 gain (me-05-f). |
| itureans -103 loss (judea) | judea -103 gain | matched | judea /ledger/9. |
| itureans -23 gain (nobody) | - | exception | Counterpart nobody, but the region is contested in this review (fail finding). |
| itureans -20 loss (judea) | - | missing | judea has -22 gain of Hauran from roman-empire and nothing in -20; Ituraea page: 'at the death of Zenodorus, Augustus gave Iturea to Herod the Great'. Route to me-05-f. |
| maccabean-judea -167 contest_start (seleucid-empire) | seleucid-empire -164 contest_start | mismatch | seleucid-empire /ledger/63 opens the contest in 164 against 'judea'; Maccabean Revolt page: rebellion 'in 167 BCE'. Route to me-05-c: 167, counterpart maccabean-judea. |
| maccabean-judea -164 gain (seleucid-empire) | - | missing | me-05-c: no loss of Jerusalem in 164 or regain in 160. |
| maccabean-judea -152 vassal_start (seleucid-empire) | - | missing | me-05-c: 'From 152-141 BCE, the rebels achieved a state of informal autonomy akin to a vassal'. |
| maccabean-judea -142 vassal_end (seleucid-empire) | seleucid-empire -143 loss | mismatch | seleucid-empire /ledger/68-69 (-143) name judea; this dossier's land passes to judea at -142. Name and year within one; me-05-c. |
| kingdom-of-emesa -64 vassal_start (roman-republic) | - | missing | eu-03-b. |
| kingdom-of-emesa -30 loss (roman-republic) | - | missing | eu-03-b (Emesene dynasty page: 'From 30 BC until 20 BC, the Emesene Kingdom was dissolved'). |
| kingdom-of-emesa -20 gain (roman-empire) | - | missing | eu-04-a. |
| kingdom-of-emesa 78 loss (roman-empire) | - | missing | eu-04-a. |
| cyrene-under-ptolemy-viii -163 gain (ptolemaic-kingdom) | ptolemaic-kingdom -163 loss | mismatch | ptolemaic-kingdom /ledger/57 names cyrenaica (whose dossier has no 163-145 events); rename to cyrene-under-ptolemy-viii. Route to me-05-b. |
| cyrene-under-ptolemy-viii -161 contest_start (ptolemaic-kingdom) | ptolemaic-kingdom -161 contest_start | mismatch | ptolemaic-kingdom /ledger/58-61 (161, 160, 154) name cyrenaica; me-05-b. |
| cyrene-under-ptolemy-viii -145 loss (ptolemaic-kingdom) | ptolemaic-kingdom -145 gain | mismatch | ptolemaic-kingdom /ledger/62 names cyrenaica; me-05-b. |
| cyrene-under-ptolemy-viii -162 contest_start (Ptolemy Sempetesis (rebel governor)) | - | exception | No dossier; listed in counterparts_needing_dossiers. |
| revolt-of-timarchus -163 gain (seleucid-empire) | seleucid-empire -161 loss | mismatch | seleucid-empire /ledger/65 loses Media and Babylonia in 161 (confidence 1) to 'Timarchus (Media and Babylonia)'; Timarchus infobox 'Reign: 163-160 BC'. Route to me-05-c: Media in 163, counterpart revolt-of-timarchus. |
| revolt-of-timarchus -160 loss (seleucid-empire) | seleucid-empire -160 gain | mismatch | seleucid-empire /ledger/66 names 'Timarchus (Media and Babylonia)'; rename to revolt-of-timarchus (me-05-c). |
| phoenician-and-cypriot-rebels -350 gain (achaemenid-empire) | achaemenid-empire -350 contest_start | mismatch | achaemenid-empire /ledger/33 has only a contest; no loss of Phoenicia and Cyprus to the rebels. Route to me-05-a. |
| phoenician-and-cypriot-rebels -350 contest_start (achaemenid-empire) | achaemenid-empire -350 contest_start | matched | achaemenid-empire /ledger/33. |
| phoenician-and-cypriot-rebels -346 loss (achaemenid-empire) | - | missing | achaemenid-empire has no 346 regain of Phoenicia (Mentor page: 'captured in 346 BC'). me-05-a. |
| phoenician-and-cypriot-rebels -343 contest_end (achaemenid-empire) | achaemenid-empire -343 contest_end | matched | achaemenid-empire /ledger/34 (no gain of Cyprus alongside; me-05-a). |
| bessus-artaxerxes-v -330 gain (achaemenid-empire) | achaemenid-empire -330 split | matched | achaemenid-empire /ledger/44 split; its region (Afghanistan, Uzbekistan and more) is wider than this dossier's Bactria + Sogdia; the author asks me-05-a to narrow it. |
| bessus-artaxerxes-v -329 loss (macedonian-empire) | macedonian-empire -329 gain | mismatch | macedonian-empire /ledger/33 gains Bactria and Sogdia in 329 from achaemenid-empire (dissolved July 330); should name bessus-artaxerxes-v. Route to eu-02-a. |
| cleopatra-ii-alexandria -131 gain (ptolemaic-kingdom) | ptolemaic-kingdom -132 contest_start | mismatch | ptolemaic-kingdom /ledger/63 has a contest from 132 against the string 'Cleopatra II' and no loss of Alexandria; rename to cleopatra-ii-alexandria and add the loss (me-05-b). |
| cleopatra-ii-alexandria -127 loss (ptolemaic-kingdom) | ptolemaic-kingdom -127 contest_end | mismatch | ptolemaic-kingdom /ledger/64 names 'Cleopatra II'; needs the 127 gain of Alexandria (me-05-b). |
| tarcondimotid-dynasty -66 vassal_start (roman-republic) | - | missing | roman-republic has no Tarcondimotid events (eu-03-b); this dossier duplicates tarcondimotid-kingdom (eu-04-x). |
| tarcondimotid-dynasty 17 loss (roman-empire) | - | missing | roman-empire has no AD 17 gain of Upper Cilicia (eu-04-a; also flagged by review-eu-04-x). |
| harsiesi -131 gain (ptolemaic-kingdom) | - | missing | ptolemaic-kingdom has no Harsiesi events (Harsiesi page: 'captured Thebes in the summer of 131 BC'). Route to me-05-b. |
| harsiesi -131 loss (ptolemaic-kingdom) | - | missing | me-05-b: Thebes regained 'in November of the same year'. |
| harsiesi -130 loss (ptolemaic-kingdom) | - | missing | me-05-b. |
| yehud-medinata -539 vassal_start (achaemenid-empire) | - | missing | achaemenid-empire has no Yehud events; it holds the land directly from its 539 conquest of Babylon (me-05-a may add the province tint or leave Yehud as detail). |
| yehud-medinata -332 dissolve (macedonian-empire) | macedonian-empire -332 gain | matched | macedonian-empire /ledger/25 gains the Levant in 332 from achaemenid-empire; the land agrees, the counterpart is the empire not the province. |

## Problems

- tarcondimotid-dynasty (me-05-x, written 13:41) duplicates tarcondimotid-kingdom (eu-04-x, written 13:07, reviewed fail): one state, two dossiers. The orchestrator should pick one slug, merge (this dossier has the -66 start the eu-04-x reviewer asked for) and delete the other.
- The author's cross-dossier requests route some fixes to the wrong parts: ptolemaic-kingdom is me-05-b (not me-05-d), kingdom-of-pergamon is me-05-d (not me-05-b), macedonian-empire is eu-02-a (not me-05-c). The cross_checks notes use the owners from the briefs' owned tables.
- Most mirrors are missing because the counterparts (achaemenid-empire me-05-a, seleucid-empire me-05-c, ptolemaic-kingdom me-05-b, kingdom-of-pergamon me-05-d, judea me-05-f, macedonian-empire eu-02-a, rhodes eu-02-b, roman-republic eu-03-b, roman-empire eu-04-a) were written before these additions and use 'nobody', string names or the wrong slug; they are routed in cross_checks, not counted against this batch.
- roman-republic /ledger/156 (-74) gains Lycia from 'Isaurians and Cilician pirates' at confidence 3, contradicting the Lycian League's autonomy 168 BC-43 AD; eu-03-b should drop Lycia from that region.
- Reviewer applied 7 small fixes in place (lycian-league, kingdom-of-antiochus-hierax x3, phoenician-and-cypriot-rebels, cleopatra-ii-alexandria, kingdom-of-herod-agrippa-i, yehud-medinata); each re-validated clean and was read back after the write.
- WebFetch returns a summary, not the page text; quotations in spot checks are as the summariser returned them. No page failed to load in this review.

## Gazetteer names needed

- Xanthos (place), used in lycian-league
- Patara (place), used in lycian-league
- Myra (place), used in lycian-league
- Tlos (place), used in lycian-league
- Pinara (place), used in lycian-league
- Olympos (place), used in lycian-league
- Peraea (region), used in tetrarchy-of-galilee-and-peraea
- Iturea (region), used in tetrarchy-of-philip, itureans
- Trachonitis (region), used in tetrarchy-of-philip
- Batanea (region), used in tetrarchy-of-philip
- Paneas (place), used in tetrarchy-of-philip, itureans
- Ulatha (region), used in itureans
- Anti-Lebanon (region), used in itureans, kingdom-of-herod-agrippa-i
- Chalcis ad Libanum (place), used in itureans
- Abila (place), used in kingdom-of-herod-agrippa-i
- Lod (place), used in maccabean-judea
- Mount Ephraim (region), used in maccabean-judea
- Modein (place), used in maccabean-judea
- Emesa (place), used in kingdom-of-emesa
- Anazarbos (place), used in tarcondimotid-dynasty
- Mizpah (place), used in yehud-medinata
- Mylasa (place), used in hecatomnid-caria
- Castabala (Hierapolis-Castabala) (place), used in tarcondimotid-dynasty
- Mount Amanus (region), used in tarcondimotid-dynasty
- Arethusa (Rastan) (place), used in kingdom-of-emesa
- Lapethus (place), used in cyrene-under-ptolemy-viii
- Banias (Paneas) (place), used in itureans, tetrarchy-of-philip

## Counterparts needing dossiers

- Barca (city-state) (suggested barca, [-560, -515])
- Tetrarchy of Lysanias (Abilene) (suggested tetrarchy-of-lysanias, [-40, 37])
- Ptolemy Sempetesis (rebel governor of Cyrene) (suggested ptolemy-sempetesis-cyrene, [-162, -162])
- Kingdom of Chalcis (Herod of Chalcis, Agrippa II) (suggested kingdom-of-chalcis, [41, 92])
- Kingdom of Soemus (Iturea, 38-49) (suggested kingdom-of-soemus, [38, 49])
- Revolt of Spitamenes (Sogdia) (suggested revolt-of-spitamenes, [-329, -328])
- Liberators' faction (Brutus and Cassius) (suggested liberators-faction, [-43, -42])
