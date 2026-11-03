# Review of batch sa-03-b (2026-10-19)

Reviewer for harsha-s-empire, kashmir and khadga-dynasty. All three validate (`--resolve` is clean apart from two warnings: harsha /wars/2 lies outside the state's life; khadga's deva-dynasty has no dossier). Spot checks were weighted to confidence-3 events and to the events that move the most land. Every event checked says what its note claims; nothing is fabricated or mis-dated.

Verdicts: harsha-s-empire **fail** (keyframe/ledger and cross-dossier overlaps), kashmir **thin** (reviewer fixed the ruler strip and the Lohkot source; periphery events are confidence 1; Karkota merge pending), khadga-dynasty **fail** (625-655 keyframe overlaps gauda-kingdom and harsha-s-empire).

## harsha-s-empire: fail

Area: infobox 1000000 km2 (648), Cliopatria 965211 km2, ratio 0.97, acknowledged True. Pushyabhuti dynasty infobox '648 est.: 1,000,000 km2' against the 644-646 shape; the Harsha page gives no area.

Findings:
- `/keyframe_review/0/correction` [for the author]: The 606-611 keyframe draws only Haryana, but /ledger/0 gains Kannauj (Uttar Pradesh) in 606 and maukhari-dynasty dissolves in 606 with harsha-s-empire as the counterpart. So no dossier holds the Maukhari land in 606-611, and /ledger/3 gains it a second time in 612 from a free-text counterpart. Evidence: maukhari-dynasty /ledger/4: 606 dissolve, counterpart harsha-s-empire, region = Maukhari 602 shape minus West Bengal, Bangladesh, Odisha and Chhattisgarh. The Harsha page gives no year for Kannauj ('He eventually made Kanyakubja ... his imperial capital') and does not say he took over the Maukhari kingdom. Fix: Make the 606-611 correction at least the union of Haryana and the /ledger/0 Kannauj circle, so the ledger and the keyframe agree. Set /ledger/3's counterpart to 'nobody' ('insubordinate kings of northern India (Xuanzang)' is not a polity). Agree with maukhari-dynasty whether its land passes in 606 or by 612; if 612, its dissolve region must shrink to Kannauj (route that to maukhari-dynasty's author).
- `/ledger/8/region` [for the author]: The 637 gain from Gauda (Harsha 644 shape intersected with Bengal) and the 644 keyframe ('ok') include the Vanga and Samatata cells (Dhaka, Khulna, Chittagong, Barisal) that this author's khadga-dynasty holds for 625-716. Two dossiers claim about 90,000 km2 in 637-647, with no relation between them. Evidence: Gauda page: 'Gauda was soon divided amongst Harshavardhana and Bhaskarvarmana of Kamarupa'; it does not say which part each received. Khadga page: 'ruled the areas of Vanga and Samatata in ancient Bengal from 625 CE to 716 CE'. The Harsha page does not mention Bengal or Kamarupa. Fix: Subtract {"cliopatria": "Khadga Dynasty", "year": 656} from the 637 gain region and from the 633 and 644 corrections from 637 on (the 644 verdict becomes adjust). Harsha's share is then West Bengal outside Karnasuvarna, which kamarupa-kingdom gains in 637. Alternatively, if a page supports it, record the Khadgas as Harsha's vassals with a vassal pair in both dossiers.
- `/ledger` [for the author]: Missing vassal_start and vassal_end for the Later Guptas of Magadha (606-647). later-gupta-dynasty records both, and Harsha's 612-646 shapes draw Magadha as direct land. Evidence: later-gupta-dynasty /ledger/8 (606 vassal_start, counterpart harsha-s-empire, region Magadha, quoting the Later Gupta page: 'they ruled as Harsha's vassals') and /ledger/9 (647 vassal_end). That dossier also gains Magadha from maukhari-dynasty in 606, so Magadha is drawn twice. I did not open the Later Gupta page; the Pushyabhuti page does not mention Magadha or Madhavagupta. Fix: Add a vassal_start (606, counterpart later-gupta-dynasty, region {"region": "Magadha"}, source https://en.wikipedia.org/wiki/Later_Gupta_dynasty) and a vassal_end (647). Either subtract Magadha from the 612-646 corrections or say in a note that the vassal is drawn by later-gupta-dynasty.
- `/ledger/6` [for the author]: The 619 loss of the strip south of the Narmada to chalukya-dynasty has no mirror: chalukya-dynasty records no gain from Harsha, and its war entry says no land changed hands. Evidence: chalukya-dynasty war 'Pulakeshin II's war with Harsha': 'No land changed hands, so no contest is drawn'. Its gains of Maharashtra (623, kalachuris-of-mahishmati) and Madhya Pradesh/Gujarat (633, 'Malavas, Latas and Gurjaras') cover the same land. The /ledger/6 note itself says 'The page does not say Harsha ever held land south of it; the strip is Cliopatria's'. Fix: Either remove the strip in the 612 correction as a Cliopatria error (a removal by correction needs no event) and delete /ledger/6, or keep the loss and route the matching 619 gain to chalukya-dynasty. Say which in notes.
- `/ledger/0` [for the author]: /ledger/0 (606 gain) and /ledger/1 (606 vassal_start) have no month, so they sort before the found event of April 606: a gain and a vassalage before the state exists. Evidence: /ledger/2 found has month 4. Fix: Give /ledger/0 and /ledger/1 month 4 (or later), or order them after the found event.
- `/wars/2` [for the author]: Wang Xuance's 648-649 expedition lies outside the state's life (606-647); this is the validator's warning. Evidence: Validator: 'span 648..649 lies outside the state's life 606..647'. Fix: Move it to the tang-dynasty and arunasva-kannauj dossiers, or drop it here.
- `/ledger/6/note` [applied by reviewer]: The quote 'appears to have acquired control of a large part of western Deccan to the south of the Narmada river' was attributed to the Harsha page; it is on the Pulakeshin II page. Evidence: Harsha page (WebFetch): the page contains no sentence about the western Deccan south of the Narmada. Pulakeshin II page: 'Pulakeshin appears to have acquired control of a large part of western Deccan to the south of the Narmada river.' Fix: Note now reads "...; Pulakeshin II page: Pulakeshin 'appears to have acquired control...'" (re-validated).

Thin (for a gap-filler):
- `/ledger/0`: The year Harsha took Kannauj (confidence 1; the year is borrowed from maukhari-dynasty). Try https://en.wikipedia.org/wiki/Kannauj
- `/ledger/7`: The year the capital moved to Kanyakubja (626 is a placeholder midpoint). Try https://en.wikipedia.org/wiki/Kannauj
- `/ledger/9`: The year of Valabhi's submission (640, borrowed from maitraka-dynasty). Try https://en.wikipedia.org/wiki/Dhruvasena_II
- `/ledger/1`: Kamarupa as vassal or ally (confidence 1; kamarupa-kingdom has no vassal event). Try https://en.wikipedia.org/wiki/Bhaskaravarman
- `/keyframe_review/1`: Sindh, Nepal, Kalinga/Odisha (Majumdar's 'Saurashtra, Kannauj and Orissa' core) are not dated. Try https://en.wikipedia.org/wiki/Great_Tang_Records_on_the_Western_Regions

Spot checks:
- `/ledger/2` https://en.wikipedia.org/wiki/Harsha: confirmed: 'Reign: April 606 - 647'; 'crowned him emperor at an assembly in April 606'
- `/ledger/3` https://en.wikipedia.org/wiki/Harsha: confirmed: 'R.K. Mookerji and C.V. Vaidya have dated Harsha conquests to 606-612 CE' (the page adds that wars went on for several more years)
- `/ledger/5` https://en.wikipedia.org/wiki/Pulakeshin_II: confirmed: 'between November 618 CE and February 619 CE'; 'Bijapur-Mumbai grant inscription, dated 4 April 619 CE'
- `/ledger/6` https://en.wikipedia.org/wiki/Harsha: confirmed ('Narmada River designated as the border'); the western-Deccan quote is from the Pulakeshin II page (attribution fixed)
- `/ledger/8` https://en.wikipedia.org/wiki/Gauda_Kingdom: confirmed: 'approximately between 593 and 636'; 'Gauda was soon divided amongst Harshavardhana and Bhaskarvarmana'; no share given
- `/ledger/12` https://en.wikipedia.org/wiki/Pushyabhuti_dynasty: confirmed: Harsha 'Died: 647'; Pushyabhuti 'He died without an heir'

## kashmir: thin

Area: infobox 222236 km2 (1342), Cliopatria 201742 km2, ratio 0.91, acknowledged True. Kashmir Sultanate infobox (the Kashmir and Karkota pages give no area). The corrected outline is about 90,000 km2 (0.40 of the infobox). /keyframe_review/24 acknowledges and resolves this: the Sultanate page calls the state 'primarily based in the Kashmir Valley' and says Ladakh was a tributary 'later subdued'.

Findings:
- `/identity/rulers` [applied by reviewer]: 42 of 47 reigns had no source, and the strip had gaps at 934-935, 936-937, 1123-1128, 1155-1165, 1172-1235 and 1273-1301 although the pages date those reigns. Evidence: Utpala table: Partha (2nd reign) 934-935, Chakravarman (3rd reign) 936-937. Lohara page: 'Jayasimha succeeded his father in 1128'; 'followed by his son Paramanuka, and then his grandson Vantideva (ruled 1165-72)'; 'Vuppadeva was succeeded in 1181 by his brother Jassaka, who was then succeeded by his son Jagadeva in 1199'; 'His death came by poison in 1212 or 1213'; 'Rajadeva, survived until 1235'; Laksmandadeva's reign 'began in 1273'; 'By 1286 ... Simhadeva, came to the throne'; 'Simhadeva survived until 1301'. Fix: Applied by the reviewer: each reign now cites its dynasty page (Karkota, Utpala or Lohara). Inserted Partha (2nd reign), Chakravarman (3rd reign), Paramanuka, Vuppadeva, Jassaka, Jagadeva, Rajadeva, Laksmandadeva and Simhadeva, and set Sussala's end to 1128. The strip now runs without gaps from 625 to 1339 (56 reigns). Re-validated.
- `/ledger/15/source` [applied by reviewer]: The 1015 date relied on a link label because the Siege of Lohkot page 'would not load'. It loads at the URL with '(1015)'. Evidence: https://en.wikipedia.org/wiki/Siege_of_Lohkot_(1015): 'Summer - Winter 1015', 'Lohkot Fort, Tosa Maidan, Kashmir', Ghaznavid Empire against the Lohara dynasty, 'Inconclusive'. Fix: Applied by the reviewer: source switched to that page, the note now quotes it, and the page is added to sources[]. The notes field still says the page failed; the author may tidy that.
- `/ledger/18/region` [for the author]: The note says 'Ladakh and Gilgit-Baltistan dropped', but the region subtracts only Ladakh, Baltistan and the Valley. The gazetteer's Baltistan is Northern Areas within 74.5-77.5 E, 34.5-36 N, so Gilgit is a separate region and its cells stay in the 860-959 and 1152-1339 corrections. The 960 drop of 'Gilgit-Baltistan (63)' cells has no event (/keyframe_review/13 mentions only Ladakh and a Jammu trim). Evidence: gazetteer regions.jsonl: Gilgit = {minus: [Northern Areas, Baltistan]}. shapes.csv: 860 bbox starts at 73.70 E (Gilgit town is 74.3 E, 35.9 N). Utpala page: 'frontier territories remained outside Kashmir sovereignty'. Fix: Add {"region": "Gilgit"} to the subtracted union in /ledger/12, /ledger/18 and the corrections from /keyframe_review/11 on, or keep Gilgit and add the 960 loss and 1152 gain events, saying so in the notes.
- `/identity/predecessors` [for the author]: Cross-dossier double claim: karkota-dynasty (another sa-03 part) also draws the Kashmir Valley for 625-855 (found 625 from alchon-huns, dissolve 855 to utpala-dynasty). alchon-huns /ledger/20 gives its Kashmir valley in 630 to karkota-dynasty, not to kashmir. Evidence: karkota-dynasty keyframes 625-850 (Valley, Poonch, Gilgit, Punjab hills, 118,000 km2 in 656) and its notes ('the two rows draw the two halves of the same realm ... must be reconciled'). The kashmir notes say the same. The research brief: a dynasty that replaces a dynasty on the same land is a rename, which the kashmir dossier follows. Fix: Orchestrator decision; neither author can fix it alone. Recommended: fold the Karkota Dynasty row (and, once written, Utpala Dynasty 960-1002 and Lohara Dynasty 1003-1259) into kashmir's cliopatria_names with their shapes reviewed, and retire karkota-dynasty as a separate state (or give it 625-855 and start kashmir in 855). Make alchon-huns /ledger/20 and kashmir /ledger/0 agree on slug and year (625 or 630).

Thin (for a gap-filler):
- `/ledger/4`: Who took the Himachal and Jammu hills in 732, and who returned them in 772 (/ledger/9); both are confidence 1 against nobody. Try https://en.wikipedia.org/wiki/Katoch
- `/ledger/7`: A dated Tibetan takeover of Ladakh and Baltistan (748, confidence 1). Try https://en.wikipedia.org/wiki/History_of_Ladakh
- `/ledger/5`: Year and land of Yashovarman's submission (736-749, confidence 1). Try https://en.wikipedia.org/wiki/Yashovarman
- `/ledger/12`: 860, 1056, 1152 and 1210 Cliopatria jumps (/ledger/12, /17, /18, /19) are confidence 1 with no counterpart named. Try https://en.wikipedia.org/wiki/Rajatarangini
- `/ledger`: Mongol overlordship: 'Kashmir became a Mongol dependency some time after 1235' (Kashmir Sultanate page). Under the brief a vassal_start belongs in both ledgers; neither kashmir nor mongol-empire has it. Try https://en.wikipedia.org/wiki/Mongol_invasions_of_India
- `/keyframe_review/0`: Himachal Pradesh, Jammu and Pir Panjal cells, and the 902-959 and 1210-1227 extents, are 'unverified: page budget' (budget of 9 pages spent). Try https://en.wikipedia.org/wiki/Durlabhavardhana

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Karkota_dynasty: confirmed: 'Established: 625'; 'Kalhana assigns a regnal span of thirty-six years from 625 to 661/2'
- `/ledger/10` https://en.wikipedia.org/wiki/Utpala_dynasty: confirmed: 'Founded by Avantivarman in 855, it replaced the Karkota dynasty'
- `/ledger/12` https://en.wikipedia.org/wiki/Utpala_dynasty: confirmed quote: 'Rajatarangini records no military activity during his reign and frontier territories remained outside Kashmir sovereignty'
- `/ledger/14` https://en.wikipedia.org/wiki/Samgramaraja: confirmed: 'upon the death of Didda on 8 August 1003'
- `/ledger/15` https://en.wikipedia.org/wiki/Siege_of_Lohkot_(1015): confirmed: 'Summer - Winter 1015' (source fixed by reviewer)
- `/ledger/16` https://en.wikipedia.org/wiki/Samgramaraja: confirmed: 'In 1021, Mahmud again attempted to invade Kashmir'
- `/ledger/22` https://en.wikipedia.org/wiki/Lohara_dynasty: confirmed: Rinchan 'claimed the throne for himself in 1320 and reigned until 1323'; Sultanate infobox 'Conversion of Rinchan Shah: December 1320'
- `/ledger/26` https://en.wikipedia.org/wiki/Kashmir: confirmed: 'Hindu rule in Kashmir ended in 1339 with the rise of the Shah Mir dynasty'; Sultanate: 'The Shah Miris ruled from 1339'

## khadga-dynasty: fail

Area: infobox None km2 (None), Cliopatria 90427 km2, ratio None, acknowledged True. Neither the Khadga nor the Samatata page gives an area; the author says so.

Findings:
- `/keyframe_review/0/correction` [for the author]: The new 625-655 keyframe draws the whole 656 outline (Vanga and Samatata, about 90,400 km2) from 625. gauda-kingdom's 612-637 keyframe holds the same Bangladesh cells to 637, and harsha-s-empire's 637 gain (Harsha 644 shape intersected with Bengal) holds them for 637-647. Three dossiers claim the land, with no relation between them; the author's notes only ask the colour agent to check. Evidence: Khadga page: 'emerged as a powerful kingdom of Bengal between the fall of Gauda Kingdom and the rise of the Pala Empire'. Samatata page: 'The Khadgas were originally from Vanga but later conquered Samatata'; '6th century-7th century: Gauda Kingdom'. Gauda page: Shashanka ruled 'approximately between 593 and 636'. gauda-kingdom /keyframe_review/2 (612-637) unions the Gauda 602 shape (Bangladesh 234 cells). Fix: Keep the 625 found event (infobox, confirmed). Then either (a) draw 625-636 as a Gauda dependency, with a vassal_start in 625 and a vassal_end in 637 (counterpart gauda-kingdom, confidence 1, citing the Khadga page's 'between the fall of Gauda Kingdom ...'), route the mirror events to gauda-kingdom, and use the full 656 outline from 637; or (b) keep the keyframe and route to gauda-kingdom a trim of its 612-637 keyframe (minus the Khadga 656 outline from 625). Either way, harsha-s-empire's 637 gain must exclude this land (harsha-s-empire /ledger/8). Say in notes which you chose.

Thin (for a gap-filler):
- `/keyframe_review/0`: The year the Khadgas conquered Samatata ('originally from Vanga but later conquered Samatata', undated). A minor state, thin by design (2 shapes, 1-2 pages). Try https://en.wikipedia.org/wiki/History_of_Bengal
- `/keyframe_review/3`: Who held Vanga and Samatata in 716-749, before the Pala row (Deva dynasty, no dossier), and Udirnakhadga's reign. Try https://en.wikipedia.org/wiki/Deva_dynasty

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Khadga_dynasty: confirmed: infobox 'Established: 625 CE'; 'ruled the areas of Vanga and Samatata in ancient Bengal from 625 CE to 716 CE'
- `/ledger/1` https://en.wikipedia.org/wiki/Khadga_dynasty: confirmed: 'Disestablished: 716 CE'; 'It was succeeded by the 8th-9th century Buddhist Deva dynasty'
- `/keyframe_review/1` https://en.wikipedia.org/wiki/Samatata: confirmed: districts 'Sylhet ... Dhaka ... Comilla, Noakhali ... Barisal, Khulna district' match the outline
- `/identity/capitals/0` https://en.wikipedia.org/wiki/Khadga_dynasty: confirmed: 'Karmanta Vasaka (present-day Barakamata, Comilla district)'; coordinates fall inside the 656 bbox

## Cross-dossier matrix

- harsha-s-empire 606 gain (maukhari-dynasty) -> maukhari-dynasty 606 dissolve: **mismatch**. Year matches, land does not: Harsha takes the Kannauj circle (150 km) and draws only Haryana in 606-611, while Maukhari hands over its whole realm (Uttar Pradesh, Bihar, Jharkhand, Nepal) in 606.
- harsha-s-empire 606 vassal_start (kamarupa-kingdom) -> none: **missing**. kamarupa-kingdom (sa-02) records only the 606-637 alliance war against Gauda, no vassalage. Harsha's events are confidence 1, and the pages disagree (Pushyabhuti page: 'overlordship', Kamarupa page: alliance).
- harsha-s-empire 612 gain (insubordinate kings of northern India (Xuanzang)) -> none: **exception**. The counterpart is free text, not a polity; it should be 'nobody'. The region double-counts the Maukhari land (606) and Magadha (later-gupta-dynasty's vassal).
- harsha-s-empire 619 loss (chalukya-dynasty) -> none: **missing**. chalukya-dynasty's war entry says 'No land changed hands'; its 623 (Maharashtra) and 633 (Madhya Pradesh and Gujarat) gains name other counterparts.
- harsha-s-empire 637 gain (gauda-kingdom) -> gauda-kingdom 637 dissolve: **matched**. gauda-kingdom lists harsha-s-empire as a successor for Bengal outside Karnasuvarna (kamarupa-kingdom gains Karnasuvarna in 637). But Harsha's region overlaps khadga-dynasty (see below).
- harsha-s-empire 637 gain (gauda-kingdom) -> khadga-dynasty 625 found: **mismatch**. Both dossiers (same author) draw Vanga and Samatata (Dhaka, Khulna, Chittagong, Barisal) for 637-647.
- harsha-s-empire 640 vassal_start (maitraka-dynasty) -> maitraka-dynasty 640 vassal_start: **matched**. Both are c. 640 at confidence 1.
- harsha-s-empire 647 vassal_end (maitraka-dynasty) -> maitraka-dynasty 647 vassal_end: **matched**. 
- harsha-s-empire 647 vassal_end (kamarupa-kingdom) -> none: **missing**. As for the 606 vassal_start.
- later-gupta-dynasty 606 vassal_start (harsha-s-empire) -> none: **missing**. harsha-s-empire has no Later Gupta vassalage (606-647, Magadha) and draws Magadha as its own land.
- later-gupta-dynasty 647 vassal_end (harsha-s-empire) -> none: **missing**. As above.
- kashmir 656 loss (tibetan-empire) -> none: **exception**. tibetan-empire is owned by ea-04, which has not run yet.
- kashmir 732 loss (nobody) -> none: **exception**. Counterpart nobody (confidence 1).
- kashmir 736 vassal_start (kannauj-varman-dynasty) -> none: **exception**. kannauj-varman-dynasty (another sa-03 part) is not written yet.
- kashmir 748 loss (tibetan-empire) -> none: **exception**. ea-04 has not run yet.
- kashmir 749 vassal_end (kannauj-varman-dynasty) -> none: **exception**. Not written yet.
- kashmir 772 gain (nobody) -> none: **exception**. Also 860, 1152 and 1210 gains and the 1056 loss: counterpart nobody, confidence 1.
- kashmir 625 found (None) -> karkota-dynasty 625 found: **mismatch**. Both dossiers draw the Kashmir Valley for 625-855. alchon-huns /ledger/20 loses the valley in 630 to karkota-dynasty. This needs an orchestrator merge decision (see problems).
- kashmir 1236 vassal_start (mongol-empire) -> none: **missing**. 'Kashmir became a Mongol dependency some time after 1235' (Kashmir Sultanate page). Neither ledger has it; the kashmir author deferred it to mongol-empire and chagatai-khanate, whose dossiers lack it too.
- khadga-dynasty 625 found (None) -> gauda-kingdom 637 dissolve: **mismatch**. gauda-kingdom holds the same Bangladesh cells to 637 (keyframe 612-637), and Khadga draws them from 625.
- khadga-dynasty 716 dissolve (deva-dynasty) -> none: **exception**. deva-dynasty has no dossier; it is listed in counterparts_needing_dossiers (sa-03-x).

## Problems for the orchestrator

- kashmir vs karkota-dynasty (and the utpala-dynasty and lohara-dynasty rows, not yet written): the two dossiers draw the Kashmir Valley for 625-855. Both authors flagged it. The orchestrator must decide on a merge (recommended: one state, kashmir, with the Karkota, Utpala and Lohara Dynasty rows added to its cliopatria_names and their shapes reviewed) before the colour and compile steps.
- harsha-s-empire, khadga-dynasty and gauda-kingdom: the Bengal core (about 90,000 km2) is claimed by gauda-kingdom to 637, by khadga-dynasty from 625, and by harsha-s-empire for 637-647. The fix is routed to the sa-03-b author; it may need a trim in gauda-kingdom.
- harsha-s-empire vs maukhari-dynasty and later-gupta-dynasty: the Maukhari land in 606-611 is drawn by no one, and Magadha in 612-647 is drawn twice (Harsha's own land and the Later Gupta vassal).
- WebFetch of https://en.wikipedia.org/wiki/Ladakh was refused by the permission classifier, so the Ladakh-based events (/ledger/1, /2, /7 in kashmir; all confidence 1-2) were not spot-checked.
- Reviewer edits (validated, read back): kashmir /identity/rulers (sources and nine missing reigns), kashmir /ledger/15 source plus a sources[] entry, harsha-s-empire /ledger/6 note attribution.
