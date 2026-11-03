# Review of batch eu-11-c (Kingdom of Mercia, Kingdom of Lindsey)

Reviewed 2026-10-25 by the Phase B adversarial reviewer. Both dossiers validate with 0 errors and 0 warnings (also with --resolve). Pages opened: Mercia, Egbert of Wessex, Offa of Mercia, Æthelflæd, Wulfhere of Mercia, Kingdom of Lindsey. Neighbour dossiers read (ledger lines naming Mercia or Lindsey): kingdom-of-wessex, kingdom-of-kent, kingdom-of-essex, kingdom-of-east-anglia, kingdom-of-sussex, wihtgar, hwicce, brythons, kingdom-of-powys, kingdom-of-gwynedd, kingdom-of-gwent, viking-settlements, anglo-saxon-england and the rest of the Context list; kingdom-of-northumbria, danelaw, cornwall and kingdom-of-seisyllwg are not written yet.

## kingdom-of-mercia: fail

Every confidence-3 event I opened is on its page with its year (628 Hwicce, 656, 658, 679, 764, 829, 830, 877, 886, 911, 917, 918 and December 918); the Cliopatria faults (hegemony drawn as annexation, missing 656-660 and 830-839 shapes, the 884-925 residue) are found and corrected. It fails on missing events: the vassal spans for Kent and East Anglia run straight through the breaks that the dossier's own Offa page (Kent) and the neighbour dossiers record, and Mercia's own client status under Wessex 879-918, which its infobox states, is only a rename. One small fix applied by the reviewer (dissolve region without Oxford).

Fixes:
- `/ledger/16, /ledger/22` (not applied): The Kent vassalage is one span 764-825, which the dossier's own source contradicts for 776-785 and 796-798; the four Kent events have no Mercian mirror. Evidence: Offa of Mercia page: 'there is no evidence for Offa's authority over Kent until 785' and 'Mercian control lasted until 796, the year of Offa's death'. The kingdom-of-kent dossier has vassal_end 776 (c2), vassal_start 785 (c3), vassal_end 796 (c3, Eadberht Praen) and vassal_start 798 (c3, Coenwulf installs Cuthred), all with counterpart kingdom-of-mercia. The author's notes call this 'left as found'. Fix: Add vassal_end kingdom-of-kent 776 (c2, Otford, Offa page), vassal_start 785 (c3, Offa page), vassal_end 796 (c3, Offa page) and vassal_start 798 (c3, from the Coenwulf of Mercia page or the page the Kent dossier cites), region Kingdom of Kent 762 each; keep 764 and 825. Optionally the 688-691 Oswine episode the Kent dossier has (c2/c1).
- `/ledger/20, /ledger/24` (not applied): The East Anglia vassalage runs 794-825 without the 796-c.799 independence the East Anglia dossier records. Evidence: kingdom-of-east-anglia /ledger/2 vassal_end 796 (c2: 'Infobox: independent 796 to c. 799; Eadwald's revival after Offa') and /ledger/3 vassal_start 799 (c2, Coenwulf suppresses Eadwald), both counterpart kingdom-of-mercia. The Offa page is silent on it ('not on page'), so the Mercia author could not see it, but the mirror is missing. Fix: Add vassal_end kingdom-of-east-anglia 796 and vassal_start 799 (c2, citing https://en.wikipedia.org/wiki/Kingdom_of_East_Anglia), or say in notes why Mercia keeps the relation through 796-799.
- `/ledger/35, /ledger/37` (not applied): Mercia's client status under Wessex 879-918 is recorded only as two rename events, with no vassal_start/vassal_end pair against kingdom-of-wessex. Evidence: Mercia page infobox (read 2026-10-25): 'Independent kingdom (527-879) Client state of Wessex (879-918)'; body: 'From about 883 until his death in 911 Æthelred, Lord of the Mercians, ruled Mercia under the overlordship of Wessex'; Æthelflæd page: 'In 883, he made a grant with the consent of King Alfred, thus acknowledging Alfred's lordship.' The kingdom-of-wessex dossier has /ledger/25 vassal_start kingdom-of-mercia 880 (c2) and /ledger/33 vassal_end 918 (c3). Fix: Add vassal_start 879 (or 880, to agree with Wessex within a year), counterpart kingdom-of-wessex, region {cliopatria: Kingdom of Mercia, year: 880}, c3 from the Mercia infobox; add vassal_end 918 (month 12, before the dissolve), counterpart kingdom-of-wessex. Keep the renames for the title changes.
- `/ledger/8` (not applied): The Isle of Wight loss to Sussex is dated 666 (Cliopatria's year, c1) while both neighbours date the gift to 661, and the Meon valley that went with it is in neither the gain nor the loss. Evidence: Wulfhere of Mercia page: 'raided the Isle of Wight in 661', then 'He subsequently gave both the island and the territory of the Meonware ... to his godson King Æthelwealh' (no year); lead: 'He conquered the Isle of Wight and the Meon valley and gave them to King Æthelwealh'. wihtgar /ledger/1: vassal_start kingdom-of-sussex 661 (c3, 'conquered the island in 661 and gave overlordship to his godson'); kingdom-of-sussex /ledger/2: gain from kingdom-of-mercia 661 (the Meonwara). Fix: Move the loss to 661 (c2, cite https://en.wikipedia.org/wiki/Kingdom_of_Sussex or the Isle of Wight page the wihtgar dossier cites) and mark keyframe kingdom-of-mercia_661 adjust without the island, or keep 666 and say why in the note; add the Meon valley (a place region on the Meon) to the 661 gain and to the loss.
- `/ledger/12` (not applied): The 705 gain on the Welsh border names only kingdom-of-powys, but Gwynedd and Gwent record losses to Mercia in the same year. Evidence: kingdom-of-gwynedd /ledger/5: 705 loss to kingdom-of-mercia, 'the Dee plain and Vale of Clwyd ... seven cells (1,770 km2)' (c1); kingdom-of-gwent /ledger/2: 705 loss to kingdom-of-mercia, the Archenfield cell (c1); kingdom-of-powys /ledger/2: 705 loss (c1). Fix: Split the 705 gain into three (counterparts kingdom-of-gwynedd, kingdom-of-powys, kingdom-of-gwent), each the intersection of minus(Mercia 705, Mercia 692) with that neighbour's previous shape; all stay c1.
- `/keyframe_review/17/correction` (not applied): The 800 correction subtracts Wessex 806 instead of Wessex 787, so the three Thames cells west of London enter Mercia in 800 with no event, while the Wessex dossier loses them to Mercia in 806. Evidence: kingdom-of-wessex /ledger/12: '806: three cells of the Thames west of London pass to Mercia in Cliopatria' (c1); Mercia's ledger has no 806 event and its 802 vassal_end is the only Wessex event between 786 and 825. Fix: Subtract Wessex 787 in the 800 correction (Wessex was a client to 802) and add a 806 gain from kingdom-of-wessex (c1, minus(Wessex 783, Wessex 806)), or explain the 800 date.
- `/identity/predecessors` (not applied): Predecessors are empty although anglo-saxon-england (state, 441-533) names kingdom-of-mercia as its successor with the land of Mercia's 534 shape. Evidence: anglo-saxon-england successors[0]: kingdom-of-mercia, land {cliopatria: Kingdom of Mercia, year: 534}, '104 of Mercia's 105 first cells'. Mercia's notes justify the empty list only for Sub-Roman Britain, Hwicce and Lindsey. Mercia also starts 527 while anglo-saxon-england dissolves in 533 with no split for Mercia, so the land is claimed twice in 527-533. Fix: Add predecessor anglo-saxon-england with land {cliopatria: Kingdom of Mercia, year: 534}; report the 527-533 overlap so anglo-saxon-england gets a 527 split for Mercia (as it has for Essex) or Mercia's notes say why not.
- `/ledger/43/region, /identity/successors/0/land` (applied by reviewer): The dissolve region and the successor land used the whole 880 shape, including Oxford, which Edward had taken in 911 (the dossier's own /ledger/40 and keyframe 917). Evidence: Æthelflæd page: 'When Æthelred died, Edward took control of the Mercian towns of London and Oxford and their hinterlands.' Keyframe kingdom-of-mercia_917 correction is minus(Mercia 880, Oxford 20 km) plus Derby and Leicester. Fix: First union member replaced by {minus: [Mercia 880, place Oxford 20 km]} in both places, texts updated; file re-validated (0 errors, 0 warnings with --resolve) and read back.

Thin (for a gap-filler):
- `/ledger/1, /ledger/3`: 617 and 628 growth beyond the Hwicce at c1, counterpart brythons guessed from the neighbour list; no page dates the Cheshire/Staffordshire/Shropshire advance (https://en.wikipedia.org/wiki/Penda_of_Mercia)
- `/ledger/15`: 757 Thames border strip (c1): Cynewulf's recovery is undated inside his reign (https://en.wikipedia.org/wiki/Cynewulf_of_Wessex)
- `/ledger/21`: 802 end of the Wessex overlordship (c1); the Egbert page says Beorhtric's 'dependency on Mercia continued into the reign of Cenwulf' (https://en.wikipedia.org/wiki/Beorhtric_of_Wessex)
- `/ledger/28`: 840 Essex-London addition (c1); the Egbert page only says Wiglaf 'may also have brought Essex back into the Mercian orbit' (https://en.wikipedia.org/wiki/Beorhtwulf_of_Mercia)
- `/ledger/30`: 866 north-east Midlands and Lindsey loss (c1) before the 867-868 Nottingham episode (https://en.wikipedia.org/wiki/Great_Heathen_Army)
- `/keyframe_review/18`: Coenwulf 796-821 (Kent 798, East Anglia 799), Ceolwulf I, Beornwulf: the 806-824 shape is unverified (page budget) (https://en.wikipedia.org/wiki/Coenwulf_of_Mercia)
- `/identity/rulers`: ruler strip omitted (page budget) (https://en.wikipedia.org/wiki/List_of_monarchs_of_Mercia)
- `/ledger/34`: the 877 partition line and the 886-890 boundary with the Danelaw (Watling Street) are not described; 875-879 shapes are corrected only to the western half (https://en.wikipedia.org/wiki/Treaty_of_Alfred_and_Guthrum)

Spot checks:
- `/ledger/2`: confirmed on https://en.wikipedia.org/wiki/Mercia ('when Penda incorporated the formerly West Saxon territories of Hwicce into his kingdom' (628, Cirencester))
- `/ledger/4`: confirmed on https://en.wikipedia.org/wiki/Mercia (Peada murdered spring 656; 'Oswiu assumed direct control of the whole of Mercia')
- `/ledger/5`: confirmed on https://en.wikipedia.org/wiki/Mercia ('A Mercian revolt in 658 threw off Northumbrian domination')
- `/ledger/34`: confirmed on https://en.wikipedia.org/wiki/Mercia ('In 877 the Danes seized the eastern part of Mercia, which became part of the Danelaw.')
- `/ledger/26`: confirmed on https://en.wikipedia.org/wiki/Egbert_of_Wessex ('In 829, Ecgberht invaded Mercia and drove Wiglaf ... into exile'; 830 Wiglaf regained independence (/ledger/27 confirmed too))
- `/ledger/16`: confirmed on https://en.wikipedia.org/wiki/Offa_of_Mercia (764 Rochester grant with Heahberht as king of Kent; same page: no evidence of authority over Kent until 785, control lasted until 796 (see fix 1))
- `/ledger/38`: confirmed on https://en.wikipedia.org/wiki/%C3%86thelfl%C3%A6d (886 Alfred occupied London 'which had been in Viking hands' and 'handed control of London over to Æthelred'; /ledger/40 (911 London and Oxford), /ledger/41 (917 Derby), /ledger/42 (918 Leicester) and /ledger/43 (12 June 918 death, early December 918 deposition) confirmed on the same page)

Area: The Mercia infobox gives no area. Cliopatria's 96,899 km2 (800-805) and 84,530 (788-799) include Wessex, Kent, Sussex and East Anglia drawn as annexed; the author acknowledges and corrects this in keyframes 741-806.

## kingdom-of-lindsey: thin

Valid and honest within its 5-page budget: the found year and the 625 Paulinus sentence are on the page, the five shapes are one outline, and the c1 end is said to be Cliopatria's year. Thin by design; the gap-filler list is below. Two small unapplied fixes.

Fixes:
- `/identity/predecessors` (not applied): Predecessors are empty although Lindsey's land lies in anglo-saxon-england's shape (state, 441-533) and Lindsey's life starts in 450, inside it; that dossier has splits for Deira (450), Kent (455) and Essex (527) but none for Lindsey, and omits Lindsey from its successors. Evidence: anglo-saxon-england /ledger/0 found region text 'the Saxon-held east of lowland Britain: East Anglia, Lincoln...'; its successors are Mercia, Wessex, East Anglia and Deira only. Fix: Add predecessor anglo-saxon-england with land {cliopatria: Kingdom of Lindsey, year: 534}, and route a 450 split for Lindsey to the anglo-saxon-england owner (or say in notes why Lindsey's 450-533 land is outside that shape).
- `/identity/successors/0/note, /ledger/1/note` (not applied): The quote 'at times part of Deira, Northumbria, and especially Mercia' was not found in that form on the page. Evidence: Kingdom of Lindsey page as fetched 2026-10-25: 'It was from time to time effectively part of Deira' and 'under the alternating control of Northumbria and Mercia'. Fix: Quote the page's wording or mark the phrase as a paraphrase.

Thin (for a gap-filler):
- `/ledger/1`: the end of the kingdom (625 is Cliopatria's year, c1): Edwin's conquest and the Paulinus/Blecca mission (625 or 628) (https://en.wikipedia.org/wiki/Edwin_of_Northumbria)
- `/identity/successors`: whether Lindsey went on as a subject kingdom (Aldfrið's pedigree late in Offa's reign; Mercian client after 679) that could carry vassal tints to the 8th century (https://en.wikipedia.org/wiki/Tribal_Hidage)
- `/identity/rulers`: no kings with years (Critta, Blecca, Aldfrið) (https://en.wikipedia.org/wiki/Paulinus_of_York)

Spot checks:
- `/ledger/0`: confirmed on https://en.wikipedia.org/wiki/Kingdom_of_Lindsey ('from about 450, Lindsey was one of the lesser kingdoms')
- `/ledger/1`: confirmed on https://en.wikipedia.org/wiki/Kingdom_of_Lindsey (625 Paulinus 'received by the praefectus of Lindum'; the page dates no end, as the c1 note says)
- `/identity/capitals/0`: confirmed on https://en.wikipedia.org/wiki/Kingdom_of_Lindsey ('It is believed that Roman Lindum (Lincoln) was the capital of Lindsey'; Lincoln (-0.54, 53.23) inside the 623 shape bbox)
- `/keyframe_review/4/note`: confirmed on https://en.wikipedia.org/wiki/Kingdom_of_Lindsey (the page also gives 'Paulinus's mission to Lindsey of 628 CE')

Area: The Lindsey page has no infobox and no area; all five shapes are 3,933-3,976 km2 (outline noise), as the keyframe notes say.

## Cross-dossier matrix

- kingdom-of-mercia 617 gain (brythons) / brythons 617 loss: matched. both c1, Cliopatria cells
- kingdom-of-mercia 628 gain (hwicce) / hwicce 628 dissolve: matched. Hwicce dissolves to Mercia as client
- kingdom-of-mercia 628 gain (brythons) / brythons 628 loss: matched. both c1
- kingdom-of-wessex 628 loss (kingdom-of-mercia) / none: mismatch. Wessex /ledger/3 (c1) loses three upper-Thames cells to Mercia; Mercia's 628 gains name hwicce and brythons only
- kingdom-of-mercia 656 loss (kingdom-of-northumbria) / none: exception. kingdom-of-northumbria has no dossier yet (eu-11 part not run)
- kingdom-of-mercia 658 gain (kingdom-of-northumbria) / none: exception. no Northumbria dossier yet
- kingdom-of-mercia 661 gain (wihtgar) / wihtgar 661 vassal_start: mismatch. wihtgar has no event with Mercia: it goes straight to vassal of kingdom-of-sussex in 661
- kingdom-of-mercia 664 vassal_start (kingdom-of-essex) / kingdom-of-essex 664 vassal_start: matched. 
- kingdom-of-mercia 666 loss (kingdom-of-sussex) / kingdom-of-sussex 661 gain: mismatch. 5 years apart; Sussex's gain is the Meonwara (with the island per wihtgar); Mercia fix 4
- kingdom-of-mercia 674 contest_start (kingdom-of-northumbria) / none: exception. no Northumbria dossier yet
- kingdom-of-mercia 679 gain (kingdom-of-northumbria) / none: exception. no Northumbria dossier yet; contest_end 679 likewise
- kingdom-of-mercia 705 gain (kingdom-of-powys) / kingdom-of-powys 705 loss: matched. all c1
- kingdom-of-gwynedd 705 loss (kingdom-of-mercia) / none: mismatch. Mercia's 705 gain names only Powys (fix 5)
- kingdom-of-gwent 705 loss (kingdom-of-mercia) / none: mismatch. Mercia's 705 gain names only Powys (fix 5)
- kingdom-of-kent 688 vassal_start (kingdom-of-mercia) / none: missing. Kent c2 (Oswine with Mercian backing) and 691 vassal_end c1; nothing in Mercia
- kingdom-of-mercia 726 vassal_start (kingdom-of-wessex) / none: missing. Wessex dossier has no Mercian overlordship 726-752; route to kingdom-of-wessex
- kingdom-of-mercia 752 vassal_end (kingdom-of-wessex) / none: missing. route to kingdom-of-wessex
- kingdom-of-essex 750 loss (kingdom-of-mercia) / none: missing. Essex c1: London to Mercia c. 750; Mercia keeps London inside the subtracted Essex 665 shape to 825
- kingdom-of-mercia 757 loss (kingdom-of-wessex) / none: missing. Mercia c1; nothing in Wessex
- kingdom-of-mercia 764 vassal_start (kingdom-of-kent) / kingdom-of-kent 764 vassal_start: matched. 
- kingdom-of-kent 776 vassal_end (kingdom-of-mercia) / none: missing. also Kent 785 vassal_start, 796 vassal_end, 798 vassal_start (c3); Mercia fix 1
- kingdom-of-mercia 771 gain (kingdom-of-sussex) / kingdom-of-sussex 771 loss: matched. Sussex dissolves 772 with successor Mercia
- kingdom-of-mercia 779 gain (kingdom-of-wessex) / none: missing. Bensington; nothing in Wessex
- kingdom-of-mercia 786 vassal_start (kingdom-of-wessex) / none: missing. nothing in Wessex 786-802
- kingdom-of-mercia 794 vassal_start (kingdom-of-east-anglia) / kingdom-of-east-anglia 794 vassal_start: matched. 
- kingdom-of-east-anglia 796 vassal_end (kingdom-of-mercia) / none: missing. and 799 vassal_start; Mercia fix 2
- kingdom-of-mercia 802 vassal_end (kingdom-of-wessex) / none: missing. nothing in Wessex
- kingdom-of-wessex 806 loss (kingdom-of-mercia) / none: mismatch. Mercia's 800 correction lets the cells in at 800 with no event (fix 6)
- kingdom-of-mercia 825 vassal_end (kingdom-of-kent) / kingdom-of-kent 825 vassal_end: matched. 
- kingdom-of-mercia 825 vassal_end (kingdom-of-essex) / kingdom-of-essex 825 vassal_end: matched. 
- kingdom-of-mercia 825 vassal_end (kingdom-of-east-anglia) / kingdom-of-east-anglia 825 vassal_end: matched. 
- kingdom-of-mercia 825 loss (kingdom-of-wessex) / kingdom-of-wessex 825 gain: matched. Sussex and Surrey
- kingdom-of-mercia 829 loss (kingdom-of-wessex) / kingdom-of-wessex 829 gain: matched. 
- kingdom-of-mercia 830 gain (kingdom-of-wessex) / kingdom-of-wessex 830 loss: matched. 
- kingdom-of-mercia 840 gain (kingdom-of-wessex) / kingdom-of-wessex 840 loss: matched. both c1
- kingdom-of-mercia 852 vassal_start (kingdom-of-gwynedd) / none: missing. Gwynedd has no Mercian overlordship 852-881; route to kingdom-of-gwynedd
- kingdom-of-mercia 881 vassal_end (kingdom-of-gwynedd) / none: missing. route to kingdom-of-gwynedd
- kingdom-of-mercia 866 loss (viking-settlements) / viking-settlements 866 gain: matched. both c1
- kingdom-of-mercia 868 loss (viking-settlements) / none: mismatch. viking-settlements has no 868 event; it has a 874 gain from Mercia instead
- viking-settlements 874 gain (kingdom-of-mercia) / kingdom-of-mercia 874 rename: mismatch. Mercia treats 874 as a rename (Ceolwulf II) with no loss; land lost only in 877 to danelaw
- kingdom-of-mercia 875 loss (kingdom-of-wessex) / none: missing. London/Essex to Alfred c. 875 (c2); Wessex has no 875 gain, and the Æthelflæd page says London was in Viking hands before 886
- kingdom-of-mercia 877 loss (danelaw) / none: exception. danelaw has no dossier yet (eu-11 part not run)
- kingdom-of-wessex 880 vassal_start (kingdom-of-mercia) / kingdom-of-mercia 879 rename: mismatch. Mercia has no vassal_start/vassal_end against Wessex for 879-918 (fix 3); Wessex 918 vassal_end likewise unmirrored
- kingdom-of-mercia 886 gain (kingdom-of-wessex) / kingdom-of-wessex 886 gain: mismatch. Wessex gains London from danelaw in 886 and records no hand-over to Mercia
- kingdom-of-mercia 911 loss (kingdom-of-wessex) / kingdom-of-wessex 911 gain: matched. London and Oxford
- kingdom-of-mercia 917 gain (danelaw) / none: exception. no danelaw dossier yet; 918 Leicester likewise
- kingdom-of-mercia 918 dissolve (None) / kingdom-of-wessex 918 gain: matched. Wessex dates it to June (Æthelflæd's death), Mercia to December (Ælfwynn deposed)
- anglo-saxon-england 533 dissolve (kingdom-of-mercia) / none: mismatch. anglo-saxon-england names Mercia as successor; Mercia's predecessors are empty and it starts in 527 (fix 7)
- kingdom-of-lindsey 625 dissolve (None) / none: exception. successor kingdom-of-northumbria has no dossier yet
- anglo-saxon-england 450 split (kingdom-of-lindsey) / none: missing. anglo-saxon-england has no split or successor for Lindsey, whose life starts in 450 inside its shape

## Problems

- Neighbour dossiers kingdom-of-northumbria, danelaw, cornwall and kingdom-of-seisyllwg do not exist yet; their mirrors are counted as exceptions (group part not run).
- Routing for already-written neighbours: kingdom-of-wessex lacks Mercia's 726-752 and 786-802 overlordship, the 757 and 779 border-strip moves, the 875 and 886 London moves; kingdom-of-gwynedd lacks the 852-881 Mercian overlordship; viking-settlements lacks a 868 Nottingham event; anglo-saxon-england lacks a split for Lindsey (450) and for Mercia (527).
- The Mercia and Lindsey pages carry no area, so no area ratio could be computed.
- The Danelaw page cited for Mercia /ledger/41 was not opened; Derby 917 was confirmed on the Æthelflæd page instead.
- Pages opened by the reviewer (6): Mercia, Egbert of Wessex, Offa of Mercia, Æthelflæd, Wulfhere of Mercia, Kingdom of Lindsey. None failed.
