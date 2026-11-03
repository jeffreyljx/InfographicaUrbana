# Review of batch eu-11-b (Kent, Sussex, Wihtgar, Deira, East Anglia, Essex)

Reviewer: Phase B adversarial reviewer, 2026-10-25. Machine copy: history/notes/phase-b/reviews/eu-11-b.json.

Mechanical: all six dossiers validate with `--resolve`, 0 errors, 0 warnings (before and after the reviewer's edits). Shapes, `cliopatria_names` and keyframe verdicts match `shapes.csv`/`polities.csv`. Neighbour dossiers on disk: kingdom-of-bernicia (read); rheged, franks, salian-franks, burgundian-kingdom, aquitaine (no events naming this batch). Mercia, Wessex, Northumbria, Lindsey, Brythons, Anglo-Saxon England, Danelaw, Viking settlements: not written yet (other eu-11 parts / eu-14), so their mirrors are exceptions.

Pages opened by the reviewer: Kingdom of Kent, Battle of Ellendun, Kingdom of Sussex, Wihtwara, Deira, Battle of Hatfield Chase, Kingdom of East Anglia, Great Heathen Army, Kingdom of Essex, Wulfhere of Mercia, Bernicia. None failed.

## Verdicts

| slug | verdict | why |
| --- | --- | --- |
| kingdom-of-kent | fix (applied by reviewer) | Events confirmed; reviewer added the 676 Mercian invasion to `wars` and the infobox's 769 date to /ledger/10's note |
| kingdom-of-sussex | fix (applied by reviewer) | Events confirmed; reviewer quoted the infobox status line in the successor note; end-year choice routed to Mercia |
| wihtgar | pass | 534, 661, 686 all on the Wihtwara page; area 380 km2 vs 507.8 (1.34) acknowledged |
| kingdom-of-deira | **fail** | 604 typed as a vassal relation; the pages say Æthelfrith *united* the kingdoms, and the Bernicia dossier records a 604 merge, so the land is drawn twice 604-611 |
| kingdom-of-east-anglia | pass | 794, 825, 865-866 Thetford, 869 confirmed; Stour cut matches Essex; Cliopatria's 866 Viking cut rejected with page support |
| kingdom-of-essex | fix (applied by reviewer) | Events confirmed; reviewer noted two infobox/page conflicts in the event notes |

## kingdom-of-kent (fix, applied)

Spot checks (Kingdom_of_Kent unless noted): /ledger/3 686 'In 686 Kent was conquered by Cædwalla of Wessex' confirmed; /ledger/6 'by 689–690 East Saxon kings under Mercian overlordship were active in West Kent' confirmed; /ledger/9 'in 764, he gained supremacy over Kent and ruled it through client kings' confirmed; /ledger/11 'Offa firmly re-established his authority over Kent in 785' confirmed; /ledger/13 'reconquered Kent in 798 ... installed his brother Cuthred' confirmed; /ledger/15 Battle_of_Ellendun 'September 825 ... conquering Sussex ..., Kent, and Essex' confirmed.

Applied:
- /ledger/10 (776 vassal_end, confidence 2): the infobox status line is 'Independent kingdom (c. 455–764, 769–785, 796–798); Client state of Mercia (764–769, 785–796, 798–825)', so the infobox ends the first client period in 769. The note now says so; 776 (Otford, page text) is kept.
- /wars: the page has 'in 676 the Mercian king ... led an attack that destroyed many Kentish churches'; added 'Mercian invasion of Kent (676)', zones empty (no land changed).

Not a fault, for the record: the page says 'After Cuthred's death in 807, Coenwulf ruled Kent directly' and the Offa page has Kent as 'an ordinary province' in 785-789, but the infobox calls both periods 'Client state of Mercia', so the vassal tint is defensible. Infobox has no area. Æthelred (866-871, infobox only) stays unexplained, as the author flagged.

Thin (confidence 1 bridges): /ledger/2 616 end of Kentish overlordship over Essex (try Sæberht_of_Essex); /ledger/7 691 end of Oswine's Mercian-backed rule (try Oswine_of_Kent); /ledger/8 692 end of Swæfheard in west Kent (try Swæfheard_of_Kent).

## kingdom-of-sussex (fix, applied)

Spot checks (Kingdom_of_Sussex): /ledger/1 491 Andredadsceaster confirmed; /ledger/2 Wulfhere_of_Mercia 'Wulfhere raided the Isle of Wight in 661' and 'subsequently gave both the island and the territory of the Meonware' confirmed (the year is the page's sequence, confidence 2 is right); /ledger/5 and /ledger/6 infobox 'Subject to Wessex: c. 686 – c. 715' confirmed; /ledger/7 'In 771, King Offa of Mercia conquered the territory of the Haestingas' confirmed; /ledger/8 'By 772 he apparently controlled the whole of the Kingdom of Sussex' confirmed.

Applied: /identity/successors/0/note now quotes the infobox status line 'Independent kingdom (477–686, 715–771, 796–827) Client state of Wessex (686–715, 827–860) Client state of Mercia (771–796)'.

Not blocking, for the orchestrator and the Mercia author: the same author kept Kent (and Essex, East Anglia) as Mercian clients to 825 on their infoboxes but dissolves Sussex in 772, although the Sussex infobox has it as a Mercian client to 796. The text and the Ellendun page ('Sussex (hitherto under direct Mercian rule)') support the 772 end, so it stands; the kingdom-of-mercia dossier must then draw Sussex as direct Mercian land 772-825 and say so. Infobox has no area; the 1.44 gazetteer comparison is in the keyframe notes.

## wihtgar (pass)

Spot checks (Wihtwara): /ledger/0 'received the island from Cerdic's son Cynric in 534' confirmed; /ledger/1 'in 661 Wulfhere of Mercia conquered the Isle of Wight' (and Æthelwealh) confirmed; /ledger/2 and /ledger/3 'an invasion in 686 by King Cædwalla of Wessex', 'After this point, the island became a part of Wessex' confirmed. Area: '147-square-mile (380 km2)' (body text) against 507.8 km2 = 1.34, acknowledged in keyframes 2-3. Cliopatria's 523 start and 691 end are both corrected on the page. Within its 1-2 page budget the 544-661 silence is thin by design.

## kingdom-of-deira (fail)

Blocking, not applied:
- /ledger/1, /ledger/2, /ledger/3. The ledger has Deira as a Bernician vassal 604-612 (vassal_start/vassal_end, confidence 2/1) and then a merge into Northumbria in 612 (confidence 1, Cliopatria bridge). The pages say a union, not a vassal relation. Deira page: 'Æthelfrith of Bernicia, who united the two kingdoms into Northumbria' and the infobox has 'Shared crown with Bernicia: 604'. Bernicia page: 'united Deira with his own kingdom by force around 604'. The neighbour dossier kingdom-of-bernicia records `604 merge` with counterpart kingdom-of-deira over the Cliopatria Deira 592 shape. As written, Bernicia takes the land as its own from 604 while Deira draws it as a vassal tint until 611. **Fix:** make /ledger/1 a `merge` (604, counterpart kingdom-of-bernicia, confidence 2, Deira page). Delete /ledger/2 and /ledger/3: no page gives 612. Set /keyframe_review/4 (kingdom-of-deira_592) to `adjust`, with the text 'Deira 592-603; from c. 604 part of Æthelfrith's united kingdom'. Keep 633 gain / 634 dissolve. If the author prefers Kirby's 'cooperative arrangement', the Bernicia dossier must change instead. Either way the two dossiers must agree.

Applied:
- /ledger/4 and /ledger/5 confidence 3 to 2. Both events' region is the Cliopatria 633 shape, which holds 17 cells of Lindsey and the Elmet side. Battle_of_Hatfield_Chase names only Bernicia and Deira ('Edwin's cousin Osric took over Deira'), never mentions Lindsey, and lists 'Kingdom of Elmet' on the Gwynedd-Mercian side.

Not blocking: /keyframe_review/5 (633 shape, verdict ok, 18,451 km2, 1.42 times the 592 shape). With Elmet fighting against Edwin at Hatfield and Lindsey unmentioned, consider `adjust` to the 592 outline or 'minus Cliopatria Kingdom of Lindsey (617 shape)'. The author flagged it as unverified.

Spot checks: /ledger/0 infobox 'Established: c. 450' confirmed; /ledger/1 date confirmed, type contradicted; /ledger/4 '12 October 633' confirmed, region not named; /ledger/5 Bernicia 'from 634 onward' confirmed. Infobox has no area.

## kingdom-of-east-anglia (pass)

Spot checks (Kingdom_of_East_Anglia): /ledger/1 'in 794, Offa of Mercia had the East Anglian king Æthelberht executed and then took control of the kingdom' confirmed; /ledger/3 infobox 'Client state of Mercia (794–796; c. 799–825)' confirmed; /ledger/4 'restored by a rebellion against Mercia led by Æthelstan in 825' confirmed; /ledger/6 Great_Heathen_Army 'They spent the winter of 865–866 at Thetford, before marching north to capture York in November 866' confirmed; /ledger/7 'In 869, the Great Army returned to East Anglia, conquering it and killing its king' confirmed. The Stour frontier ('the River Stour historically dividing it from the East Saxons') supports removing north Essex, which kingdom-of-essex adds back. Infobox has no area or capital.

Thin: /ledger/0 founding 534 at confidence 1 ('Established: 6th century'); try Wuffingas.

## kingdom-of-essex (fix, applied)

Spot checks: /ledger/0 infobox 'Established: 527' confirmed; /ledger/1 'exercise some authority in Essex shortly after 604' confirmed; /ledger/3 Wulfhere_of_Mercia 'Sigehere and Sæbbi ... "rulers ... under Wulfhere, king of the Mercians"' (664) confirmed; /ledger/6 'by the mid-8th century, much of the kingdom, including London, had fallen to Mercia' confirmed (confidence 1 is honest); /ledger/8 'in 825 ceded the kingdom to Ecgberht, King of Wessex' confirmed. Keyframe 4's 'London fell within the East Saxons' territory' is on the Wulfhere page (665-668), not the Essex page.

Applied:
- /ledger/3: the note now records the conflicting infobox 'Independent kingdom (527–709) Client state of Mercia (709–825)'. 664 is kept on Bede via the Wulfhere page.
- /ledger/4: the note now records that the Essex page puts the west Kent episode in 'the 8th century'. 689 follows the Kent and Wihtred pages.

Thin: /ledger/2 616 (try Sæberht_of_Essex); /ledger/5 692 (try Swæfheard_of_Kent); /ledger/6 c. 750 London to Mercia (try Æthelbald_of_Mercia, London charters of the 730s).

## Cross-dossier matrix (summary)

Matched inside the batch: Kent and Essex 604/616 Kentish overlordship; Kent and Essex 689/692 East Saxon occupation of west Kent; Sussex and Wihtgar 661/686 vassal pair. Mismatch: Deira 604 vassal_start against Bernicia 604 merge; Deira 612 vassal_end has no Bernician mirror. Exceptions (no dossier yet): every Mercia, Wessex, Northumbria, Brythons and Viking-settlements mirror. The full list is in the JSON.

## For the orchestrator

1. Vassal direction: these dossiers write a subordinate's vassal events with the overlord as counterpart (reviewer brief check 3). The schema text says the counterpart is the vassal in both events. The compiler must tell the two readings apart, for example by whether `region` is the dossier's own land.
2. The new early keyframes overlap Cliopatria's Anglo-Saxon England shapes (441..533): Kent 455-489, Sussex 477-489, Deira 450-533 and Essex 527-533. Kent and Sussex found with counterpart nobody. The anglo-saxon-england author must give up these lands.
3. kingdom-of-bernicia (another batch) has no event for its own absorption into Northumbria (612/616), yet it records a 633 gain from Northumbria.
