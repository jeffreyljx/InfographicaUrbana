# Notes for group eu-11-b (Kent, Sussex, Wihtgar, Deira, East Anglia, Essex)

Written 2026-10-25 by the Phase B research agent. Six dossiers, all validate with 0 errors and 0 warnings (also with --resolve). 17 distinct Wikipedia pages were opened (Kingdom of Kent, Offa of Mercia, Cædwalla of Wessex, Wihtred of Kent, Battle of Ellendun, Kingdom of Essex, Æthelberht of Kent, Kingdom of Sussex, Wihtwara, Wulfhere of Mercia, Deira, Edwin of Northumbria, Æthelfrith of Northumbria, Bernicia, Battle of Hatfield Chase, Kingdom of East Anglia, Great Heathen Army). One URL failed once (Caedwalla with the Æ spelled in the path) and loaded under Caedwalla_of_Wessex. The pages were shared between dossiers; some states went one or two pages over the 1-2 / 5 page budgets because a shared page carried the facts (Wihtgar 3, Essex 7, Kent 7).

## Conventions I used that the reviewer should know

- Vassal events are written from the vassal's side as well, following reviewer-brief check 3 and the practice of other Phase B dossiers: in a subordinate's ledger `vassal_start`/`vassal_end` carry the OVERLORD as `counterpart`. The overlord's dossier must hold the mirror (vassal_start with counterpart = this slug). Where the subordinate is the suzerain (Kent over Essex 604-616; Sussex over the Isle of Wight 661-686) the counterpart is the vassal. A compiler that reads `counterpart` as the vassal in every case would get the subordinate events backwards.
- Occupation events: the owner records them with the occupier as counterpart (Kent 686-687 by Wessex; Kent's west 689-692 by Essex); Essex records the occupier's side.
- Start years follow the infobox where one is given (Kent c. 455, Sussex 477, Wihtgar 534, Deira c. 450, Essex 527), not Cliopatria's 490/490/523/534/534; each such start has a new keyframe that carries the Cliopatria outline back. East Anglia's page gives only "6th century", so 534 stays (confidence 1).
- Several end years differ from Cliopatria on the page's own dates: Kent 825 (Cliopatria 762), Essex 825 (665), Sussex 772 (771), Wihtgar 686 (691), Deira 634 (633), East Anglia 869 (same).

## Per state

### kingdom-of-kent
- Cliopatria row ends 762 and its Mercia shape grows in 763; the page keeps Kent a kingdom with its own kings to 825. The Mercian supremacy is in the ledger as vassal pairs (764-776, 785-796, 798-825). **Mercia's dossier must carry the mirror pairs or Kent will be drawn twice.** Wessex's dossier needs the 686 occupation and the 825 gain.
- New keyframes: 455-489 (years only), 692-704 (Cliopatria has no Kent shape under Wihtred), 763-825.
- The infobox gives no area, so the area comparison could not be made (the outline is the modern county, 4,349 km2 against the gazetteer's 3,035 km2 for the region Kent: 1.43 times, within a factor of two).
- Not placed on a year: East Kent's annexation of West Kent ("sixth century"); Æthelberht's wider overlordship ("everything south of the Humber"); the 694 border cession to Ine (the Wihtred page: "It seems likely"). The Kent page's last king (Æthelred 866-871) is unexplained.
- The 776 Otford outcome is disputed between the Kent page (rebels seem to have prevailed) and the Offa page (unknown; tradition says Mercian win).

### kingdom-of-sussex
- Cliopatria's outline reaches Southampton Water (9 cells beyond the county); the Sussex page gives Hampshire land only through Wulfhere's gift of the Meonwara (661, Wulfhere page), so the outline is cut to the county and the Meon valley added by a 661 gain (confidence 2).
- Gap 692-717 is filled (Sussex under West Saxon rule c. 686-c. 715, with its own kings). Wessex needs the mirror vassal pair.
- Ends 772 on "By 772 he apparently controlled the whole of the Kingdom of Sussex". After that the pages disagree: Sussex infobox "subject to Mercia 771 to c. 796, Wessex again from c. 827, full integration 860"; Ellendun page "hitherto under direct Mercian rule" in 825. 796-827 is not settled and belongs to the Mercia and Wessex dossiers.
- Ine's campaigns of 722/725 rest on the Sussex page alone (Ine of Wessex page not opened). Ælle's bretwalda overlordship is undated.
- No capital on the page ("unlikely that they would have had a capital in Sussex"): Chichester is a placeholder.

### wihtgar
- Cliopatria 523..691 is trimmed to 534..686 (Wihtwara page: Chronicle 534; Cædwalla's invasion 686). Wihtgar "may be fictitious". Status 544-661 is unrecorded. 661-665 bridged. Sussex dossier carries the mirror vassal pair (661, 686).
- Capital: none named; a placeholder dot at the island's centre.
- Infobox area 380 km2 against 507.8 km2 (1.34).

### kingdom-of-deira
- Repaired 2026-10-25 after review eu-11-b (verdict fail). Details in "Repairs after review" below. As now written: found c. 450, merge with Bernicia 604 (confidence 2), gain 633, dissolve 634. The 604 union mirrors kingdom-of-bernicia /ledger/1 (604 merge, counterpart kingdom-of-deira, same Cliopatria Deira 592 land).
- Cliopatria draws Deira 534-611 and 633 only (Northumbria 612-632 covers both Deira and Bernicia). The dossier is founded at the infobox c. 450, merged with Bernicia in 604, restored for Osric at 633 and ends 634 when Oswald reunites Northumbria. The Northumbria dossier needs the mirror events for the 633 loss and the 634 gain of the Deira 592 outline.
- The 534 and 546 shapes carry five cells of Pennine dales that the page puts beyond the "western edge of the Vale of York" and that Cliopatria itself gives to the Brythons from 555; both are set to the 555 outline.
- The 633 shape (18,451 km2, 17 cells of Cliopatria's Lindsey and 8 cells of dales/Elmet) is no longer used: Osric's Deira is the 592 outline (see below).
- Elmet (the British kingdom west of Deira) has no Cliopatria row and no dossier in this group: needs one.
- Edwin's death: 632 (table) or 633 (text); 12 or 14 October.
- Capital: Malton and York from the page's "may have centred on"; both flagged.
- No area in the infobox.

### kingdom-of-east-anglia
- All four Cliopatria shapes include 8-9 cells of north Essex south of the Stour (Colchester). The page's Stour frontier and the Essex page both put those in Essex; they are cut here and added to Essex. 
- The 866-869 shape's Thetford cut for the Viking settlements is not supported: the army wintered at Thetford in 865-866 and marched to York.
- 800-839 is filled (Mercian client c. 799-825, independent from 825). The 799 date is the infobox's "c. 799".
- No founding year (534 is Cliopatria's, confidence 1), no capital, no area, no king list with reign years (rulers omitted). Rædwald's overlordship south of the Humber (Bede) is undated; the 825 appeal to Egbert of Wessex is not recorded as a protectorate because the infobox keeps East Anglia independent. Successor viking-settlements 870-877, Danelaw from 878 (Cliopatria).

### kingdom-of-essex
- Cliopatria 534..665 omits north-east Essex (8 cells, with Colchester) and ends at 665 when its Mercia shape takes over; the page has the kingdom to 825 under Mercian overlordship from 664 (Bede: Sigehere and Sæbbi "under Wulfhere") and Mercia holding London by the mid-8th century. The loss of London and Middlesex is dated c. 750 at confidence 1 ("mid-8th century").
- Mirror events needed: Mercia (vassal 664; London c. 750), Wessex (825 gain), Kent (this batch added Kent's 604-616 overlordship over Essex and the 689-692 west Kent episode).
- The Danelaw dossier takes Essex after the Treaty of Alfred and Guthrum (878-886 on the page). Intermittent control of Surrey is undated.
- No capital on the page; London and Colchester are placeholders. The king list is from the page's table (joint kings overlap).

## Region names the gazetteer lacks
Deira (historical region); Elmet (historical region); West Kent; London and Middlesex as a unit; places Chichester, Pevensey, Thetford, Dunwich, Rochester, Canterbury, Malton, Brough. All were handled with admin1/coordinates in the dossiers, so none produced a resolve warning.

## Repairs after review eu-11-b (2026-10-25, kingdom-of-deira only)
Pages re-opened for the repair: Deira, Bernicia, Æthelfrith of Northumbria, Edwin of Northumbria, Battle of Hatfield Chase (the same five as the first run, so the page budget is unchanged). Northumbria was not opened: the events that would have needed it are deleted.
- /ledger/1, /ledger/2, /ledger/3 (blocking, applied). The 604 vassal_start, the 612 vassal_end and the 612 merge into Northumbria are replaced by one `merge` in 604 (counterpart kingdom-of-bernicia, region Cliopatria Deira 592, source the Deira page, confidence 2). Deira page: "After his death, Deira was subject to king Æthelfrith of Bernicia, who united the two kingdoms into Northumbria"; infobox "Shared crown with Bernicia: 604". Bernicia page: "united Deira with his own kingdom by force around 604" and "ruled the two kingdoms (united as Northumbria)". Æthelfrith page: "gained control of Deira around 604; the circumstances of this are unknown"; it does not call Deira a subordinate and presents the kingdoms as joined under one ruler. No page gives 612, so the two 612 events (confidence-1 Cliopatria bridges) are gone, not re-sourced. The reviewer's thin items for them (Bernicia, Northumbria pages) are closed by deletion; the Bernicia page has no 612.
- Kirby's "cooperative arrangement" (Æthelfrith page: "a formalization of an existing relationship") is a reading of the same 604 event, not a different date, so the Bernicia dossier did not have to change; it is kept in the merge note. The Deira sentence "Deira was subject to king Æthelfrith" speaks of the king, and its verb is "united"; I read it as a union under one crown, not as a client kingdom.
- /keyframe_review/4 (kingdom-of-deira_592): verdict adjust, text "Deira 592-603; from c. 604 part of Æthelfrith's united kingdom". The shape stops at 603 so Bernicia's 604 merge and the Deira keyframe no longer draw the same cells; Cliopatria's 604-611 Deira cells are therefore Bernicia's on the map.
- /ledger/4 and /ledger/5 (confidence 3 to 2, applied by the reviewer; kept at 2). /keyframe_review/5 (non-blocking): I took the reviewer's second option and changed the verdict to adjust, with the Cliopatria Deira 592 outline as the correction. Reason, from the pages re-opened: Hatfield Chase says "the kingdom was divided between its constituent kingdoms of Bernicia and Deira" and "Edwin's cousin Osric took over Deira"; the Edwin page says "Osric ... in Deira", has Edwin expelling Ceretic from Elmet and ruling "Bernicia, Deira and much of eastern Mercia"; Lindsey, Craven and Lincoln are on none of the pages (Deira, Edwin, Hatfield Chase) and Elmet is named only on Edwin's opponents' side in the Hatfield infobox. The 633 shape's 17 Lindsey cells and 8 Elmet/dales cells therefore have no page behind them for Osric. I chose the 592 outline rather than "minus Lindsey 617" because the 8 dales/Elmet cells are unsupported too. The ledger regions of /ledger/2 and /ledger/3 (now gain 633 and dissolve 634), the 634 keyframe and the successor land (identity.successors/0) were changed to the same outline; confidence stays 2 because no page names Deira's western boundary.
- What I leave open: who held the Lindsey and Elmet-side land in 633-634 (Edwin's gains; no page says). It is for the Lindsey and Northumbria authors, and Cliopatria's Lindsey 617 shape is the nearest outline. No disagreement with the reviewer on any finding.
- Neighbour check (not touched, another batch): kingdom-of-bernicia /ledger/1 still reads 604 merge with counterpart kingdom-of-deira, region Cliopatria Deira 592, so the two dossiers now agree. The reviewer's orchestrator note 3 (Bernicia has no event for its own absorption into Northumbria, yet records a 633 gain from Northumbria) stands and is Bernicia's author's to settle.
