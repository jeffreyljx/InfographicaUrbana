# Review of batch eu-11-d (kingdom-of-wessex, dal-riata, kingdom-of-brycheiniog)

Reviewed 2026-10-25. Machine copy: history/notes/phase-b/reviews/eu-11-d.json. Validator: all three valid, no errors (before and after the reviewer's edits); warnings are counterpart slugs not yet written (picts, ulaid, lordship-of-brecon) and three open-ended Wessex vassal_starts that run to 927.
Pages were read through WebFetch (model summaries): Wessex, Egbert, Edward the Elder, Alfred the Great, Battle of Deorham, Ine of Wessex, Kingdom of Sussex, Dál Riata, Oengus I of the Picts, Kenneth MacAlpin, Brycheiniog, Hywel Dda, Bernard de Neufmarché, Rhys ap Tewdwr, Gruffydd ap Llywelyn. Cell counts come from history/tools/gazetteer.py resolve.

## kingdom-of-wessex: fail

Findings (applied = edited by the reviewer; not applied = for the author):
- `/ledger/1` [applied] Deorham gain (577) at confidence 3 although the page does not name the land drawn. Evidence: Battle_of_Deorham names only Gloucester, Cirencester and Bath; the region is the Cliopatria delta (Bath-Bristol, Wiltshire, east Somerset) and Gloucester-Cirencester are not in it (they go to Hwicce). Fix: Confidence lowered to 2 with a note.
- `/ledger/9` [applied] Sussex vassal_end dated 718 (Cliopatria's year, confidence 1) against the kingdom-of-sussex dossier's 715. Evidence: Kingdom_of_Sussex infobox: 'Subject to Wessex: c. 686 - c. 715', 'Client state of Wessex (686-715)'; text: 'Sussex evidently broke away from West Saxon domination some time before 722'. Fix: Year set to 715, confidence 2, source Kingdom_of_Sussex added to sources[] and cited.
- `/keyframe_review/2` [NOT applied] Keyframes kingdom-of-wessex_577, _587, _628 and _666 are drawn with 7 cells (about 1,770 km2) of Somerset east of the Parrett from 577, and the ledger has no gain for Cenwealh's conquest of Somerset (c. 658) or for western Somerset (by 681-685); a land-moving event is missing and two dossiers disagree on the land. Evidence: Wessex page (opened by the author): 'Cenwealh ... was able to expand West Saxon territory in Somerset at the expense of the Britons'; 'Centwine is known to have fought and won battles against the Britons'. dumnonia /ledger/1: 658 loss to kingdom-of-wessex, confidence 3 (Battle_of_Peonnum: 'annexing eastern and central Somerset'); dumnonia /ledger/2: 685 loss, confidence 2 ('western Somerset up to the Bristol Channel'). Gazetteer: Wessex 577 and 705 shapes contain 7 Somerset cells, Wessex 710 contains 13, Wessex 666/705 share 0 cells with Dumnonia 602. Result: 602-657 both dossiers draw east Somerset; 685-709 neither draws west Somerset. Fix: Correct the 577-657 keyframes to {minus: [<Wessex shape>, {admin1: Somerset, country: United Kingdom}]} (Natural Earth Somerset leaves Bath and North East Somerset in Wessex); add gain 658 counterpart dumnonia, region {minus: [{admin1: Somerset}, {cliopatria: Dumnonia, year: 602}]}, source Battle_of_Peonnum (confidence 3) or the Wessex page (2); add gain 685 counterpart dumnonia, region {intersect: [{cliopatria: Dumnonia, year: 602}, {admin1: Somerset}]}, confidence 2, and add those cells to the 685-709 corrections (keyframes _666 split at 685, _686, _692, _705); add the Peonnum war.
- `/keyframe_review/19` [NOT applied] The 830-839 correction (Wessex 840 shape) drops the 16 Essex cells that the 825-829 keyframes draw as West Saxon, and no ledger event explains it. Evidence: Gazetteer: Wessex 830 shape intersect Kingdom of Essex 661 = 16 cells; Wessex 840 shape intersect Essex 661 = 0. Egbert page: 'Wessex retained control of the south-eastern kingdoms, with the possible exception of Essex'; 'In 830, Mercia regained its independence under Wiglaf'. Fix: Add loss 830 of {cliopatria: Kingdom of Essex, year: 661} to kingdom-of-mercia (confidence 2, Egbert page), or keep Essex in the 830-839 correction and put the loss in 840 (Cliopatria's year, confidence 1).
- `/ledger/34` [NOT applied] vassal_start counterpart is a placeholder ('Welsh kings Hywel Dda, Clydog and Idwal Foel') covering two states; no vassal_end. Evidence: Hywel_Dda page: Hywel and Clydog 'jointly submitted to Edward the Elder of England in 918' (King of Seisyllwg 909-920); Edward_the_Elder page adds Idwal Foel (Gwynedd). Both slugs exist (kingdom-of-seisyllwg in polities.csv, kingdom-of-gwynedd dossier). Fix: Split into vassal_start kingdom-of-seisyllwg (region Kingdom of Seisyllwg 918) and vassal_start kingdom-of-gwynedd (region Kingdom of Gwynedd 918); say in each note that the relation runs to 927 and passes to England.
- `/ledger/22/note` [NOT applied] The note says the Alfred page never describes the Mercian relationship (page silent); it does. Evidence: Alfred_the_Great: after the treaty with Guthrum 'Alfred succeeded to Ceolwulf's kingdom consisting of western Mercia'. Fix: Quote that sentence; consider dating the start to the end of Ceolwulf II's rule (c. 879-883) at confidence 2, keeping 884 only if no page gives a year.
- `/identity/rulers` [NOT applied] Ruler list has gaps (534-642, 672-686, 688-689, 726-802, 839-871). Evidence: Reviewer brief 2.9: rulers, where given, are contiguous. Fix: Fill the gaps from the Wessex page's list of kings (or List of monarchs of Wessex), or say in notes that the strip is partial.
- `/ledger` [NOT applied] No mirror for kingdom-of-gwent /ledger/3 (926 loss to kingdom-of-wessex, confidence 3: Hereford agreement, border at the Wye, Cantref Coch / Forest of Dean). Evidence: kingdom-of-gwent dossier, Kingdom_of_Gwent page as cited there; Gwent notes that no Cliopatria cell changes. Fix: Add gain 926 counterpart kingdom-of-gwent, region {lon: -2.55, lat: 51.8, km: 12, text: 'Forest of Dean east of the Wye'}, or a note that the land is already inside the Wessex 926 shape.

Thin (for a gap-filler):
- `/ledger/2` 587 loss of the Bristol-Gloucester cells to Hwicce: Cliopatria's year, page silent (confidence 1) (try https://en.wikipedia.org/wiki/Hwicce)
- `/ledger/3` 628 upper Thames loss to Mercia: Cliopatria's year (confidence 1); the Battle of Cirencester (628) is the obvious source (try https://en.wikipedia.org/wiki/Battle_of_Cirencester)
- `/ledger/10` 806 three-cell Thames loss to Mercia (confidence 1); also the 752 Burford and 779 Bensington border moves (keyframe 13) (try https://en.wikipedia.org/wiki/Battle_of_Bensington)
- `/ledger/18` 830 end of the Northumbrian submission (confidence 1) (try https://en.wikipedia.org/wiki/Northumbria)
- `/ledger/21` Brycheiniog vassal from 'the 880s' (confidence 1, decade only); the Alfred page dates the southern Welsh commendation 'comparatively early in his reign' after Asser (try https://en.wikipedia.org/wiki/Asser)
- `/ledger/22` English Mercia vassal start 884 (confidence 1; see fix) (try https://en.wikipedia.org/wiki/%C3%86thelred,_Lord_of_the_Mercians)
- `/identity/capitals/0` Winchester as capital for 519-927 is unsourced (Wessex infobox blank; Æthelstan page: no fixed capital) (try https://en.wikipedia.org/wiki/Winchester)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Battle_of_Deorham: confirmed (577; Gloucester, Cirencester, Bath); region not named, confidence lowered to 2
- `/ledger/4` https://en.wikipedia.org/wiki/Ine_of_Wessex: confirmed ('conquered by Cædwalla in 686')
- `/ledger/9` https://en.wikipedia.org/wiki/Kingdom_of_Sussex: mis-dated (718 against the infobox's c. 715; fixed)
- `/ledger/12` https://en.wikipedia.org/wiki/Wessex: confirmed ('In 825 or 826 ... Ellendun ... seizing control of Surrey, Sussex, Kent and Essex from the Mercians')
- `/ledger/15` https://en.wikipedia.org/wiki/Egbert,_King_of_Wessex: confirmed (829, Wiglaf exiled, London mint, King of Mercia)
- `/ledger/17` https://en.wikipedia.org/wiki/Egbert,_King_of_Wessex: confirmed ('In 830, Mercia regained its independence under Wiglaf')
- `/ledger/19` https://en.wikipedia.org/wiki/Alfred_the_Great: confirmed (Wareham occupied, then Exeter)
- `/ledger/22` https://en.wikipedia.org/wiki/Alfred_the_Great: note misreports the page (it says Alfred 'succeeded to Ceolwulf's kingdom consisting of western Mercia'); year 884 not on page (confidence 1 as declared)
- `/ledger/23` https://en.wikipedia.org/wiki/Alfred_the_Great: confirmed ('in 886, Alfred reoccupied the city of London')
- `/ledger/26` https://en.wikipedia.org/wiki/Edward_the_Elder: confirmed (911, Mercian lands around London and Oxford)
- `/ledger/27` https://en.wikipedia.org/wiki/Edward_the_Elder: confirmed (Bedford occupied 915)
- `/ledger/29` https://en.wikipedia.org/wiki/Edward_the_Elder: confirmed (917: Northampton, Cambridge and East Anglia submit)
- `/ledger/31` https://en.wikipedia.org/wiki/Wessex: confirmed ('In 918 Æthelflæd died and Edward took over direct control of Mercia')
- `/ledger/36` https://en.wikipedia.org/wiki/Wessex: confirmed (infobox 'Unification of the Angles, Saxons and Danes: 12 July 927')

Area: The Wessex infobox has no area field; no comparison possible.

## dal-riata: fix

Findings (applied = edited by the reviewer; not applied = for the author):
- `/ledger/7/region` [applied] The 850 merge and dissolve events drew the whole 644 shape, including the Inner Hebrides the dossier itself loses to the Vikings in 847. Evidence: Keyframe dal-riata_847 (847-849) is {minus: [Dál Riata 644, Viking settlements 840]}; /ledger/6 loses that land in 847. Fix: Region of /ledger/7 and /ledger/8 set to {minus: [{cliopatria: Dál Riata, year: 644}, {cliopatria: Viking settlements, year: 840}]}, text kept.
- `/wars/0/belligerents` [applied] Degsastan (603) named kingdom-of-northumbria, which did not yet exist (Cliopatria's Northumbria row starts 612). Evidence: The war's own outcome quotes 'Æthelfrith of Bernicia'; kingdom-of-bernicia is a polities.csv slug (555-633). Fix: Belligerent set to kingdom-of-bernicia with a note.
- `/identity/rulers` [NOT applied] Five rulers with large gaps (501-574, 608-629, 642-811, 835-841). Evidence: Reviewer brief 2.9: rulers, where given, are contiguous. Fix: Fill from the Dál Riata page's king list or say in notes that the strip is partial (non-blocking).

Thin (for a gap-filler):
- `/ledger/1` 612 Skye gain is Cliopatria's year (confidence 1); the page: 'Dál Riata did expand to include Skye', possibly under Áedán's son Gartnait (try https://en.wikipedia.org/wiki/Gartnait_mac_%C3%81ed%C3%A1in)
- `/ledger/3` 644 loss of the Antrim land is Cliopatria's year (confidence 1); the Dál Riata page ties a loss of lands to Mag Rath (637), worth checking for the date (try https://en.wikipedia.org/wiki/Battle_of_Moira)
- `/keyframe_review/8` 850-899 of Cliopatria's row (Picts/Alba precursor) has no dossier owner (try https://en.wikipedia.org/wiki/Kingdom_of_Alba)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/D%C3%A1l_Riata: confirmed (infobox Established 498, Preceded by Ulaid)
- `/ledger/1` https://en.wikipedia.org/wiki/D%C3%A1l_Riata: confirmed undated as declared (confidence 1)
- `/ledger/4` https://en.wikipedia.org/wiki/Oengus_I_of_the_Picts: confirmed (736, Creic and Dunadd taken and burnt)
- `/ledger/5` https://en.wikipedia.org/wiki/Oengus_I_of_the_Picts: confirmed (741 'smiting'; Dál Riata page 'under Pictish overlordship by 741')
- `/ledger/6` https://en.wikipedia.org/wiki/D%C3%A1l_Riata: confirmed ('may record the conquest of the Inner Hebrides ... by Vikings in 847')
- `/ledger/7` https://en.wikipedia.org/wiki/Kenneth_MacAlpin: confirmed (King of Dál Riada 841-850; conquered the Picts 843-850; lists end around 850)

Area: The Dál Riata infobox has no area field.

## kingdom-of-brycheiniog: fix

Findings (applied = edited by the reviewer; not applied = for the author):
- `/certainty/0/note` [applied] Quoted 'No boundaries are described' as the page's words; the phrase is not on the page (also in /keyframe_review/1/note). Evidence: Brycheiniog page fetched twice: neither 'boundary' nor 'boundaries' appears. Fix: Both notes reworded to say the page describes no boundaries, without the quotation.

Thin (for a gap-filler):
- `/ledger/1` 1056 absorption into Gruffydd ap Llywelyn's Wales (confidence 1; his page never names Brycheiniog) (try https://en.wikipedia.org/wiki/Kingdom_of_Deheubarth)
- `/ledger/3` 1072 loss of two eastern cells to Norman England (confidence 1); the Bernard page says he 'already held Castell Dinas which had probably been built by the Earl of Hereford before 1075' (try https://en.wikipedia.org/wiki/William_FitzOsbern,_1st_Earl_of_Hereford)
- `/keyframe_review/2` Hywel Dda 'King of Brycheiniog: c. 930 - 950' (Hywel Dda infobox, confirmed) is in no ledger: Brycheiniog needs a loss/gain pair to kingdom-of-seisyllwg/deheubarth, or that dossier a vassal pair (try https://en.wikipedia.org/wiki/Hywel_Dda)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Brycheiniog: confirmed (infobox 'Founded by Brychan Brycheiniog: c.450')
- `/ledger/2` https://en.wikipedia.org/wiki/Gruffydd_ap_Llywelyn: confirmed (died 5 August 1063; realm 'divided again into the traditional kingdoms'; page does not name Brycheiniog, confidence 2 fair)
- `/ledger/4` https://en.wikipedia.org/wiki/Bernard_de_Neufmarch%C3%A9: confirmed (invasion shortly after the 1088 settlement; Glasbury charter autumn 1088)
- `/ledger/5` https://en.wikipedia.org/wiki/Rhys_ap_Tewdwr: confirmed (died April 1093, Brecon; 'slain by the Frenchmen who were inhabiting Brycheiniog')
- `/ledger/6` https://en.wikipedia.org/wiki/Brycheiniog: confirmed ('conquered and pacified by the Normans between 1088 and 1095'; 'Bernard's Lordship of Brecknock')

Area: The Brycheiniog infobox has no area field.

## Why kingdom-of-wessex fails

Two land-moving events are missing: Cenwealh's Somerset conquest (c. 658) and western Somerset (by 685), which the Wessex page itself supports and the dumnonia dossier records (confidence 3 and 2), and the 830 (or 840) loss of Essex that the keyframes draw without an event. The rest of the dossier held up: 14 events checked on their pages, all confirmed except the Sussex year (fixed) and the 884 note (misreads the Alfred page).

## Cross-dossier matrix

- kingdom-of-wessex 519 found / anglo-saxon-england -> anglo-saxon-england 533 dissolve: mismatch. Wessex starts 519 on land the anglo-saxon-england dossier holds to 533 (no split at 519): 15-year overlap, flagged by the author. Route to the anglo-saxon-england owner (split at 519) or move the Wessex start to 534.
- kingdom-of-wessex 577 gain / brythons -> brythons 577 loss: matched. 
- kingdom-of-wessex 587 loss / hwicce -> hwicce 587 gain: matched. both confidence 1
- kingdom-of-wessex 628 loss / kingdom-of-mercia -> none: exception. kingdom-of-mercia not written yet (eu-11 part not run)
- dumnonia 658 loss / kingdom-of-wessex -> none: missing. dumnonia /ledger/1 (confidence 3, Battle_of_Peonnum) has no gain in Wessex; Wessex draws east Somerset from 577. See Wessex fix /keyframe_review/2.
- dumnonia 685 loss / kingdom-of-wessex -> none: missing. dumnonia /ledger/2 (confidence 2): western Somerset; Wessex takes it only in 710 with Devon, so 685-709 nobody draws it.
- kingdom-of-wessex 686 vassal_start / kingdom-of-sussex -> kingdom-of-sussex 686 vassal_start: matched. 
- kingdom-of-wessex 686 gain / wihtgar -> wihtgar 686 dissolve: matched. 
- kingdom-of-wessex 686 occupation_start / kingdom-of-kent -> kingdom-of-kent 686 occupation_start: matched. 
- kingdom-of-wessex 688 occupation_end / kingdom-of-kent -> kingdom-of-kent 687 occupation_end: matched. within one year
- kingdom-of-wessex 710 gain / dumnonia -> dumnonia 710 loss: matched. 
- kingdom-of-wessex 715 vassal_end / kingdom-of-sussex -> kingdom-of-sussex 715 vassal_end: matched. Wessex year moved from 718 to 715 by the reviewer (Kingdom_of_Sussex infobox).
- kingdom-of-wessex 806 loss / kingdom-of-mercia -> none: exception. kingdom-of-mercia not written yet
- kingdom-of-wessex 825 vassal_start / cornwall -> none: exception. cornwall not written yet (eu-11 part not run)
- kingdom-of-wessex 825 gain / kingdom-of-mercia -> none: exception. Surrey and Sussex from Mercia; kingdom-of-mercia not written yet
- kingdom-of-wessex 825 gain / kingdom-of-kent -> kingdom-of-kent 825 dissolve: matched. 
- kingdom-of-wessex 825 gain / kingdom-of-essex -> kingdom-of-essex 825 dissolve: matched. Wessex has no later loss of Essex although its 830-839 shape drops it (see fix /keyframe_review/19).
- kingdom-of-wessex 829 gain / kingdom-of-mercia -> none: exception. kingdom-of-mercia not written yet
- kingdom-of-wessex 829 vassal_start / kingdom-of-northumbria -> none: exception. kingdom-of-northumbria not written yet
- kingdom-of-wessex 830 loss / kingdom-of-mercia -> none: exception. kingdom-of-mercia not written yet
- kingdom-of-wessex 876 contest_start / viking-settlements -> none: exception. viking-settlements (eu-14) not written yet; also 892-896
- kingdom-of-wessex 880 vassal_start / kingdom-of-brycheiniog -> none: exception. schema puts vassal events in the suzerain's ledger only; Brycheiniog notes acknowledge it
- kingdom-of-wessex 884 vassal_start / kingdom-of-mercia -> none: exception. kingdom-of-mercia not written yet; also 911 gain and 918 vassal_end/gain
- kingdom-of-wessex 886 gain / danelaw -> none: exception. danelaw not written yet; also 915, 917, 918 and 927 gains and the 915-918 contest
- kingdom-of-wessex 918 vassal_start / Welsh kings Hywel Dda, Clydog and Idwal Foel -> none: exception. placeholder counterpart; should be kingdom-of-seisyllwg (not written) and kingdom-of-gwynedd (vassal event belongs in the suzerain's ledger only)
- kingdom-of-gwent 926 loss / kingdom-of-wessex -> none: missing. Gwent /ledger/3 (confidence 3, Forest of Dean east of the Wye) has no gain in Wessex; see Wessex fix.
- dal-riata 498 found / ulaid -> none: exception. ulaid listed in counterparts_needing_dossiers (eu-11-x)
- dal-riata 612 gain / picts -> none: exception. picts listed in counterparts_needing_dossiers (eu-11-x); also the 736-741 contest and the 850 merge
- dal-riata 642 loss / strathclyde -> none: exception. strathclyde not written yet (eu-11 part not run)
- dal-riata 644 loss / ulaid -> none: exception. ulaid listed in counterparts_needing_dossiers
- dal-riata 847 loss / viking-settlements -> none: exception. viking-settlements (eu-14) not written yet
- kingdom-of-brycheiniog 450 found / brythons -> brythons 540 split: mismatch. brythons splits Brycheiniog off in 540 (Cliopatria's year, confidence 1) while Brycheiniog starts c. 450 (infobox): 90-year overlap. Route to the brythons owner (split at 450).
- kingdom-of-brycheiniog 1056 loss / kingdom-of-gwynedd -> kingdom-of-gwynedd 1055 gain: matched. within one year; both confidence 1
- kingdom-of-brycheiniog 1063 gain / kingdom-of-gwynedd -> kingdom-of-gwynedd 1063 loss: matched. 
- kingdom-of-brycheiniog 1072 loss / norman-england -> none: exception. norman-england not written yet
- kingdom-of-brycheiniog 1088 contest_start / lordship-of-brecon -> none: exception. lordship-of-brecon listed in counterparts_needing_dossiers; also the 1093 contest_end and loss
- kingdom-of-brycheiniog 930 loss / kingdom-of-seisyllwg -> none: missing. Expected event, not in either ledger: Hywel Dda 'King of Brycheiniog c. 930-950' is in no ledger; kingdom-of-seisyllwg not written yet

## Problems

- WebFetch returns a model summary of each page; quotes in this review are as returned, not verified verbatim.
- Reviewer edits (allowed by the orchestrator for small verified fixes) were made in all three dossiers: Wessex /ledger/1 confidence, /ledger/9 year and source; Dál Riata /ledger/7-8 region, /wars/0 belligerent; Brycheiniog two note rewordings. All three re-validate with no errors.
- Cross-dossier overlaps routed to other owners: anglo-saxon-england holds the Wessex core to 533 (Wessex from 519); brythons holds Brycheiniog to 540 (Brycheiniog from c. 450).
- dumnonia and kingdom-of-wessex disagree on Somerset 577-709 (dumnonia follows Battle_of_Peonnum); the Wessex fix is listed, the dumnonia side looks right.
- kingdom-of-sussex records vassal_start/vassal_end with counterpart kingdom-of-wessex in the vassal's own ledger, against the schema's meaning (counterpart is the vassal); for the Sussex owner.
- Cliopatria rows needing owners: Dál Riata 850-899 (Picts/Alba precursor) and Wessex 928-935 (kingdom-of-england should start 927).

Gazetteer names needed: Dunadd (place, dal-riata), Talgarth (place, kingdom-of-brycheiniog), Brecon (place, kingdom-of-brycheiniog), Glasbury (place, kingdom-of-brycheiniog), Wareham (place, kingdom-of-wessex), Brycheiniog (region, kingdom-of-brycheiniog), Forest of Dean (region, kingdom-of-gwent)
