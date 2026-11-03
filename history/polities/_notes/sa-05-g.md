# sa-05-g notes (Mughals and Marathas, part g)

Owned: talpur-dynasty. Added as a direct counterpart that no row covers: khairpur-state (new). Both validate with 0 errors, 0 warnings, and `--resolve` reports nothing unresolved. Nine pages were opened (budget 9): Talpur dynasty, Conquest of Sindh (opened by mistake; it is the 711 conquest), Battle of Miani, History of Sindh, Khairpur (princely state), Jammu and Kashmir (princely state), Gilgit-Baltistan, Khanate of Kalat, British conquest of Sindh. `Annexation_of_Sindh` returned url_not_found.

## talpur-dynasty (Cliopatria 'Talpur Dynasty' 1820..1894, 15 shapes)

- The state is the Talpur Mirs of Sindh, 1783-1843. Cliopatria starts it 37 years late and ends it in 1894 (the year Ali Murad of Khairpur died). The dossier runs 1783-1843 and adds a 1783-1819 keyframe.
- Shapes: 1820 adjust (Sindh with 189 cells of Punjab/Rajasthan/Gujarat, missing 175 Sind cells); 1822 and 1836 wrong (Sindh plus 1,305-1,306 of 1,336 Balochistan cells, 535,464 and 528,678 km2 against the infobox 'over 100,000 square kilometers'; Kalat page: Mehrab Khan 1817-1839, Kalat 1835 area 560,000 km2); 1840 and 1846-1890 (ten shapes) wrong, they are Gilgit-Baltistan outlines (Gilgit-Baltistan page: Skardu taken by the Dogras by 1840, Gilgit 1842-1860, Gilgit Agency 1888-89); 1842 adjust (Sindh plus Gilgit-Baltistan). Someone in sa-06 (kashmir-and-jammu) or the Gilgit/Hunza owners should check what these Gilgit outlines were meant for; the 1840 start matches the Dogra conquest of Baltistan.
- Ledger has seven events: 1783 found (Halani), 1839 loss of Karachi, Miani and Dubba (Feb-Mar 1843) as contest_start/end, 1843 loss of Sindh less Khairpur, split of Khairpur, dissolve.
- Page silent / unsettled: the day of the annexation (month 3 is the last battle); the extent of the Talpur state outside the Sind province (Shikarpur, Sukkur, Rohri, Umerkot, Thar frontier, Bahawalpur, Multan, Sikh claims all absent from the pages opened); dates of the Durrani tribute (the Durrani dossier already has 1783 vassal_start and 1818 vassal_end for this slug); the Talpur page's own 1832 sentence on Khairpur gives Ali Murad where the Khairpur page has Rustam; Mirpur Khas and Tando Muhammad Khan branches have no land on any page.
- Mirror events other dossiers should check: british-empire / east-india-company have no gain for Karachi in 1839 (this dossier records the loss); british-empire records the 1843 gain of the whole Sind province, which includes Khairpur; british-empire already holds a 1838 vassal_start for this slug (the political residency treaty; British conquest page).
- Not opened for budget: Sikh Empire (frontier on Shikarpur), Bahawalpur, Durrani Empire / Principality of Kandahar, First Anglo-Afghan War, Karachi. A gap-filler with these would settle the Talpur frontier before 1839.

## khairpur-state (new, no Cliopatria row)

- Written from the same four pages (no extra budget). One keyframe: a 70 km disc round Khairpur (15,427 km2) for the infobox area 15,730 km2 (no year). Events (as repaired 2026-10-25, see the repair section): 1843 found (from talpur-dynasty) and the dissolve at 30 September 1955 into islamic-republic-of-pakistan; the 3 October 1947 accession is not an event of this dossier (a vassal relation, recorded by the overlord).
- Start 1843 is a modelling choice to avoid double claims with the Talpur dossier; the pages say Established 1783 and a British treaty of 1832 recognised it as independent. Open: lands lost in upper Sindh after 1845 (undated), the Miani page's Ali Murad exiled to Burma (cannot be the Khairpur ruler), ruler-table disagreements.
- British suzerainty (infobox 'Princely state under British Raj (1838-1947)') should be a vassal_start / vassal_end in british-empire and british-raj with counterpart khairpur-state; islamic-republic-of-pakistan should record the vassal relation 1947-10 to 1955-9 and the 1955-9 merger with this slug (the original line said 'the 1947 gain'; superseded by the repair).

## Gazetteer

No names needed: Sind (Pakistan), Khairpur, Karachi and Hyderabad (Pakistan) all resolve.

## Repair of khairpur-state (2026-10-25, reviewer verdict fail)

Pages reopened or opened for the repair: Khairpur (princely state), Talpur dynasty, Khairpur District, Khairpur (town), Mir Ali Murad Khan Talpur, Mir Sohrab Khan Talpur. Failed: https://en.wikipedia.org/wiki/Ali_Murad_Khan_Talpur (url_not_found; the right title is Mir_Ali_Murad_Khan_Talpur). validate_dossier.py --resolve: 0 errors, 0 warnings.

Applied (finding 1, the fail):
- /identity/end is now 1955-9. Khairpur page, reopened: 'Princely state of Pakistan (1947-1955)', 'Accession to Pakistan: 3 October 1947', 'Disestablished: 30 September 1955', 'fully amalgamated into West Pakistan in 1955'.
- The 1947-10 loss to islamic-republic-of-pakistan is deleted; the dissolve moved to 1955-9 with counterpart islamic-republic-of-pakistan, confidence 3, quoting the amalgamation and noting that the page does not mention One Unit (bahawalpur-state and khanate-of-kalat use 14 October 1955).
- /keyframe_review/0/to, /identity/capitals/0/to and /certainty/0/to are 1955. Last ruler George Ali Murad to 1954 (infobox 'George Ali Murad Khan Talpur II 1947-1954'); the page names no ruler for 1954-1955.
- The successor note for islamic-republic-of-pakistan now describes the vassal period and the merger. Sources: Khairpur (town), Khairpur District, Mir Ali Murad Khan Talpur and Mir Sohrab Khan Talpur added.

Not applied, with reasons (finding 2, thin, and the two thin items):
- Loss of Ali Murad's upper-Sindh lands and the enlarged 1843 keyframe. The Khairpur (town) page now gives a date: Ali Murad 'helped the British in 1845-7 during the Turki campaign' but 'was later accused of plotting against the British in 1851-2' and 'was stripped of his lands in upper Sindh by the British East India Company', leaving 'mostly Khairpur city, and its immediate environs'. It names no district and no area, and no page gives the year of the stripping itself; the Khairpur princely state, Khairpur District and Mir Ali Murad Khan Talpur pages are silent. The reviewer's fix was conditional ('once a page gives them'); a loss with no region would remove unplaced land, so none is written. Open as a gap. Leads, not facts: bahawalpur-state /ledger/1 (Sabzalkot and Bhung given to the Nawab, 1847-48) and the Mir Sohrab Khan Talpur page ('captured ... the Sabzal Kot region from the Nawab of Bahawalpur'); no page opened links them to Ali Murad and the dates differ.
- Start at 1832. The Mir Ali Murad Khan Talpur page: treaty of 4 April 1832 'recognised the political individuality of Khairpur', reign 4 April 1832 - 2 April 1894. I keep 1843: starting in 1832 means cutting Khairpur out of the talpur-dynasty shape (Sind) in 1832, which edits a dossier this repair does not touch (verdict thin). The notes now carry the dates for whoever revises both.

Disagreement with the reviewer's text: the review says islamic-republic-of-pakistan 'records as vassal_start khairpur-state 1947-10 / vassal_end 1955-9'. It does not; its ledger has no Khairpur event (grep of the file today), and its own notes list Khairpur among the states without a dossier and its accession date as unresolved. The fix stands as a recommendation to the Pakistan owner: record vassal_start 1947-10, vassal_end 1955-9 and a gain 1955-9 with khairpur-state. The wider conflict stays open: Pakistan gains bahawalpur-state (1947-10) and khanate-of-kalat (1948-3) at accession while both of those run to 14 October 1955.

