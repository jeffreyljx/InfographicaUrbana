# Review of batch am-07-a (2026-10-19)

Reviewer: adversarial review, Phase B. One dossier: history/polities/english-colonial-empire.json (Cliopatria 'English Colonial Empire', 27 shapes, page budget 9). Validator: 0 errors, 0 warnings with --resolve, before and after the reviewer's edits.

## Verdict: thin

Every confidence-3 event I opened is on its page with its year (six spot checks plus extras from the same pages). The dossier is honest about the composite row, the double drawing with British Colonial Empire and British Empire, Willoughbyland's 120 km2 and Belize. What it lacks: the Treaty of Hartford mirror and the Connecticut valley, the French occupation of Madras in 1746-1749 (on a page it cites), and keyframe consistency for Eleuthera, the Bahamas and Surat; 16 confidence-1 events remain gaps.

## What I tried

- Mechanical: schema, ordering (ledger sorted; found 1607-05 at start; dissolve 1779 at end), 28 keyframe verdicts for 27 shapes plus the 1607 new keyframe, certainty 1607-1712 and 1713-1779 contiguous, wars inside the life, family 'britain' in colours.json.
- Geometry: I read the 27 Cliopatria polygons and listed every part outside mainland North America, and tested places (Hartford, Eleuthera, Nassau, St. Augustine) against each shape.
- Cross-checks against new-netherland, spanish-empire, portuguese-empire, morocco, haudenosaunee, saadi-sultanate, itza-mayans and dutch-suriname.

## Area check

English overseas possessions has no infobox and no area (confirmed). The part areas that can be checked are acknowledged and corrected: Willoughbyland 120 km2 on the page against about 23,400 km2 drawn 1653-1669 (keyframes 13-15 cut it to a 10 km Suriname-river buffer); Belize drawn whole (about 23,500 km2) from 1670, cut to 60 km round Belize City.

## Findings (fixes)

### /ledger/38/counterpart (applied by reviewer)

- What: The 1667 loss of Suriname named dutch-republic although the dossier dutch-suriname exists and founds the colony on 26 February 1667 with english-colonial-empire as counterpart and predecessor.
- Why: history/polities/dutch-suriname.json /ledger/1 (found, 1667-02, counterpart english-colonial-empire) and identity.predecessors; the Willoughbyland page: 'Surinam was captured by the Dutch Admiral Abraham Crijnssen.'
- Fix: counterpart dutch-suriname (done, with a reviewer tag in the note). The author may add month 2 if a page they open gives it.

### /ledger/1/note (applied by reviewer)

- What: The Surat note cites the page's 1608 without saying that the same page's timeline gives 1612.
- Why: English overseas possessions: body 'The East India Company's traders settled at Surat in 1608'; timeline '1612 Surat, India'.
- Fix: Conflict appended to the note (done).

### /keyframe_review/27/note (applied by reviewer)

- What: The 1778 note says 'Madras alone remains', but the shape has a second part, one cell of about 27 km2 at 10.82N 79.86E (Nagore, by Nagapattinam), new in 1778.
- Why: Cliopatria geometry of English Colonial Empire 1778-1779: two polygons, centroids (12.95N 80.24E) about 797 km2 and (10.82N 79.86E) about 27 km2; shapes.csv bbox south edge 10.6837.
- Fix: Note corrected (done). The ledger still lacks the 1778 gain of Nagore (see thin).

### /ledger (after /ledger/23, 1650-09); /keyframe_review/12, /13, /14, /15 corrections; /ledger/21/region (for the author)

- What: No mirror of new-netherland's 1650 loss (Treaty of Hartford, 19 September 1650, confidence 3) to this dossier, and the Connecticut valley (Hartford, Windsor, Wethersfield) is in none of this dossier's corrected shapes before 1670: the 1636 Connecticut gain is clipped to Cliopatria's cells, which hold Saybrook and New Haven but not Hartford.
- Why: new-netherland /ledger/7 (1650-09 loss, counterpart english-colonial-empire, region intersect NN 1648 with Connecticut/Massachusetts, 26 cells). Geometry: Hartford and Windsor fall outside every English Colonial Empire shape 1636-1662 and inside from 1670; New Netherland's 1648 shape overlaps the English 1648 shape by 0 km2 and the 1653 shape by about 106 km2, so the 26 cells are drawn by nobody 1650-1669. The Thirteen Colonies page (in sources) has Connecticut 'established 1636'.
- Fix: Add a 1650 month-9 gain, counterpart new-netherland, region {intersect: [{cliopatria: New Netherland, year: 1648}, {admin1: Connecticut}]} minus the 1653 New Netherland shape, source https://en.wikipedia.org/wiki/Treaty_of_Hartford_(1650), confidence 3 if the page is opened; add the same cells to the corrections of keyframes 1653, 1659 and 1662 (and say in the 1636-1648 notes that the English Connecticut River towns are drawn as Dutch until 1650 by Cliopatria).

### /ledger (after /ledger/52); /keyframe_review/25; /wars (for the author)

- What: The French capture of Madras (September 1746, returned 1749) is missing, although it is on a page in sources[] and the author's notes list it; Madras is about 60 percent of the 1713-1761 shape.
- Why: Madras Presidency: 'In September 1746, Fort St George was captured by the French, who ruled Madras as a part of French India until 1749, when Madras was handed back to the British under the terms of the Treaty of Aix-la-Chappelle of the previous year.'
- Fix: Add occupation_start 1746 month 9 and occupation_end 1749, counterpart french-india, region {place: Chennai, km: 30} intersected with the 1713 shape, source the Madras Presidency page, confidence 3; add the war (War of the Austrian Succession / First Carnatic War, 1746-1748) with Madras as its zone; mention it in keyframe 25's note.

### /ledger/26, /ledger/43/region, /keyframe_review/12-/keyframe_review/24 corrections (for the author)

- What: Eleuthera is gained in 1648 at confidence 3 but is in no keyframe (Cliopatria never draws Eleuthera or New Providence), and the 1673 gain is the whole Bahamas while the keyframes keep only Cliopatria's southern cells (Long Island, Acklins, Mayaguana, Inagua, plus Turks and Caicos).
- Why: Geometry: points at Eleuthera (25.2N 76.2W) and Nassau (25.06N 77.35W) fall outside every shape; the Bahamas parts of the 1673-1712 shapes have centroids 21.1-23.2N. English overseas possessions: 'when the Eleutheran Adventurers left Bermuda to settle on the island of Eleuthera' (1648).
- Fix: Add the three Eleuthera admin-1 regions to the corrections of keyframes 1648 to 1702 (as was done for Saint Kitts and Montserrat), or drop the 1648 gain; narrow /ledger/43 to {intersect: [{country: The Bahamas}, {cliopatria: English Colonial Empire, year: 1673}]} or correct the keyframes to the settled islands (New Providence, Eleuthera) with a page.

### /ledger/1, /keyframe_review/1-/keyframe_review/14 (for the author)

- What: Surat is gained in 1608 but appears in no keyframe until 1662: 54 years of an event with no trace, and the gain is a trading factory in a Mughal city rather than land.
- Why: Geometry: the Surat part (21.06N 72.90E, about 938 km2) exists only in the 1662-1686 shapes; English overseas possessions: traders 'settled at Surat in 1608' (timeline: 1612).
- Fix: Either date the gain to 1662 at confidence 1 as Cliopatria's and say the factory dates from 1608/1612, or add the Surat cells to the 1609-1659 corrections; better, mark keyframes 1662-1683 adjust to remove Surat (a factory, not a territory) and drop /ledger/1 and /ledger/49 to a note.

### /keyframe_review/5/correction (for the author)

- What: The 1626-1628 correction adds Nevis (country St. Kitts and Nevis) from 1626 although the ledger dates Nevis 1628, and omits Barbados, which the ledger gains in 1625 and Cliopatria draws only from 1629.
- Why: English overseas possessions: 'Nevis, settled 1628'; geometry: the Barbados part (13.18N 59.51W) first appears in the 1629 shape.
- Fix: Add {country: Barbados} to the 1626 correction and say in the note that Nevis is included from 1626 for want of a smaller region (or use the Saint Kitts disc only).

### /identity/capitals/0 (for the author)

- What: The capital is London, outside every shape of the state (check 9: a capital inside the shapes).
- Why: capitals: London 51.51N 0.13W, 1607-1779; the shapes lie between 4.7N and 57.2N, 93W and 88E, none in Britain.
- Fix: Minor: keep London only if the renderer is told to skip a capital outside the shapes (say so in the note), or leave the metropole's seat to kingdom-of-england and give the colony's seat where a page names one.

## Thin: for a gap-filler

- /ledger/14, /ledger/39: Sierra Leone cells 1629-1669 (gain and loss at confidence 1): who held Sherbro and when. Try https://en.wikipedia.org/wiki/Sherbro_Island
- /ledger/25, /ledger/44, /keyframe_review/9, /keyframe_review/23: Gold Coast: the 1640 cell is near Kormantin (5.29N 0.97W), lost to the Dutch in 1665 (no event), then Cape Coast from 1664/1670 and Accra 1673. Try https://en.wikipedia.org/wiki/Cape_Coast_Castle
- /ledger/27, /ledger/50, /ledger/54, /ledger/29: Virginia's growth in 1648 and 1687 and Carolina's in 1653 and 1702 (confidence 1). Try https://en.wikipedia.org/wiki/Colony_of_Virginia
- /ledger/51, /ledger/53, /keyframe_review/24: Hudson Bay posts: 1687 York Factory area, 1696 loss (counterpart new-france, no war), the 1702 James Bay post (no event); the French expedition of 1686 and the 1697 battle are not in the ledger or wars (King William's War / Nine Years' War missing from wars). Try https://en.wikipedia.org/wiki/York_Factory
- /ledger/43: The Bahamas: which islands were English from 1670 (New Providence) and why Cliopatria draws the southern islands. Try https://en.wikipedia.org/wiki/History_of_the_Bahamas
- /keyframe_review/5-/keyframe_review/24 (Saint Kitts, Antigua, Montserrat): French captures of English Saint Kitts (1666, 1689) and of Antigua and Montserrat (1666-1667), and the English taking of the French half in 1702: no events, and the corrections draw the whole island throughout. Try https://en.wikipedia.org/wiki/History_of_Saint_Kitts_and_Nevis
- /keyframe_review/5 (cells at 17.7N 64.7W, 1626-1712): Three cells on Saint Croix drawn English 1626-1628 and 1632-1712 with no event; the island was English only until about 1650 (then Spanish and French). Try https://en.wikipedia.org/wiki/History_of_Saint_Croix
- /keyframe_review/21, /keyframe_review/23: The Anguilla cell (1691-1699) has no gain or loss event; the page dates English Anguilla from 1650. Try https://en.wikipedia.org/wiki/History_of_Anguilla
- /ledger/15, /keyframe_review/6: The 1629-1632 Acadia and Cape Breton holdings were Scottish ventures (Sir William Alexander at Port Royal, Ochiltree at Baleine), not English; the gain counts them as English at confidence 2. Try https://en.wikipedia.org/wiki/Scottish_colonization_of_the_Americas
- /ledger/59, /ledger/60, /keyframe_review/26: Masulipatnam: taken from the French in 1759 and ceded by the Nizam; the 1763 gain and 1778 loss are Cliopatria's years at confidence 1. Try https://en.wikipedia.org/wiki/Northern_Circars
- /keyframe_review/27: Nagore (10.82N 79.86E) appears in 1778 with no event (counterpart likely thanjavur-maratha-kingdom). Try https://en.wikipedia.org/wiki/Nagore
- /ledger/56, /ledger/57, /ledger/61: Row bookkeeping events (1713 split, 1762 Bombay, 1779 dissolve) at confidence 1; they need eu-11 and sa-06 to agree, not a page. Try https://en.wikipedia.org/wiki/British_Empire

## Spot checks

- /ledger/30: https://en.wikipedia.org/wiki/English_overseas_possessions: confirmed: 'conquered by the English Commonwealth under Oliver Cromwell in 1655'
- /ledger/32: https://en.wikipedia.org/wiki/English_overseas_possessions: confirmed: 'On 11 May 1661, the marriage treaty ... transferred Bombay into the possession of England'
- /ledger/35 (also /ledger/34, /ledger/45, /ledger/46): https://en.wikipedia.org/wiki/Province_of_New_York: confirmed: infobox 'Surrender of New Netherland: 29 September 1664', Fort Orange 24 September; New Amsterdam 27 August (infobox 28 August); Dutch return 'July 1673'; infobox 'Treaty of Westminster: 5 March 1674'
- /ledger/16 (also /ledger/19): https://en.wikipedia.org/wiki/Treaty_of_Saint-Germain-en-Laye_(1632): confirmed: 'On 19 July 1629, an English fleet under the command of David Kirke'; signed March 29, 1632, returned 'Quebec, Acadia and Cape Breton Island'
- /ledger/24: https://en.wikipedia.org/wiki/Madras_Presidency: confirmed: purchase of Madrasapatnam 1639, grant from the Raja of Chandragiri, infobox 'Ceded by Vijaynagar governor: 1639'
- /ledger/28 (also /ledger/38): https://en.wikipedia.org/wiki/Willoughbyland: confirmed: 'founded in 1650 by Lord Willoughby', 'around 30,000 acres (120 km2)', captured by Crijnssen (1667, no month on the page)
- /ledger/26, /ledger/52, /ledger/37, /ledger/12, /ledger/17, /ledger/18, /ledger/48, /ledger/1 (extras from the same page): https://en.wikipedia.org/wiki/English_overseas_possessions: confirmed: Eleuthera 1648, Calcutta 1690, Mahim/Sion/Dharavi/Wadala 1665-1666, Nevis 1628, Antigua and Montserrat 1632, Tangier abandoned 1684; Surat 1608 in the body but 1612 in the timeline (c2, note amended)

## Cross-dossier matrix

- english-colonial-empire 1608 gain (mughal-empire) <-> mughal-empire  loss: exception. mughal-empire (sa-05) not written yet
- english-colonial-empire 1629 gain (new-france) <-> new-france  loss: exception. /ledger/15 and /ledger/16 (July); new-france is written by another am-07 part in parallel, not on disk
- english-colonial-empire 1632 loss (new-france) <-> new-france  gain: exception. /ledger/19 (March); new-france not written yet
- english-colonial-empire 1639 gain (vijayanagara-empire) <-> vijayanagara-empire  loss: exception. vijayanagara-empire not written; its Cliopatria row ends 1571, the page's infobox names a Vijaynagar governor
- new-netherland 1650 loss (english-colonial-empire) <-> english-colonial-empire  gain: missing. new-netherland /ledger/7 (1650-09, Treaty of Hartford, c3, 26 Connecticut-valley cells) has no mirror here; fix listed
- english-colonial-empire 1655 gain (spanish-empire) <-> spanish-empire 1655 loss: matched. spanish-empire /ledger/32 (c2)
- english-colonial-empire 1661 gain (portuguese-empire) <-> portuguese-empire 1661 loss: mismatch. Tangier and Bombay: portuguese-empire /ledger/38 and /ledger/39 have the losses in 1661 but name kingdom-of-england as counterpart; the land is drawn by this row, so the Portuguese side should name english-colonial-empire
- english-colonial-empire 1664 gain (new-netherland) <-> new-netherland 1664 loss: matched. /ledger/34-/ledger/36 against new-netherland /ledger/14-/ledger/17 (contest 27 August, losses 8 and 24 September)
- english-colonial-empire 1664 gain (new-netherland) <-> new-netherland 1664 loss: matched. /ledger/33 Delaware (no month) against new-netherland /ledger/18 (1664-10)
- english-colonial-empire 1665 gain (portuguese-empire) <-> portuguese-empire  loss: missing. /ledger/37 Mahim, Sion, Dharavi, Wadala 1665-1666 (c2): no 1665 loss in portuguese-empire; route to its author
- english-colonial-empire 1667 loss (dutch-suriname) <-> dutch-suriname 1667 found: matched. after the reviewer's counterpart fix; dutch-suriname /ledger/1 (1667-02, counterpart english-colonial-empire)
- english-colonial-empire 1670 loss (nobody) <-> nobody  none: exception. /ledger/39 Sierra Leone cells, counterpart nobody (c1)
- english-colonial-empire 1673 loss (new-netherland) <-> new-netherland 1673 gain: matched. ours July (page), theirs 9 August New Style (c2): same event, calendar difference
- english-colonial-empire 1674 gain (new-netherland) <-> new-netherland 1674 loss: matched. ours 5 March (treaty, infobox), theirs 10 November (handover); same year, flagged by both authors
- english-colonial-empire 1684 loss (morocco) <-> morocco 1684 gain: matched. morocco /ledger/6 (1684-02, c3)
- english-colonial-empire 1687 loss (mughal-empire) <-> mughal-empire  gain: exception. Surat (c1); mughal-empire not written
- english-colonial-empire 1690 gain (mughal-empire) <-> mughal-empire  loss: exception. Calcutta (c3); mughal-empire not written
- english-colonial-empire 1696 loss (new-france) <-> new-france  gain: exception. Hudson Bay post (c1); new-france not written
- haudenosaunee 1701 loss (english-colonial-empire) <-> english-colonial-empire  gain: mismatch. haudenosaunee /ledger/22 (Nanfan Treaty, 19 July 1701, c3) loses the beaver hunting grounds to this dossier; no shape of this row reaches that land and no gain exists here: it was a deed of a claim. Either the Haudenosaunee side uses counterpart nobody (claim only) or this dossier adds a claim event; route to am-05
- spanish-empire 1704 loss (english-colonial-empire) <-> english-colonial-empire  gain: mismatch. spanish-empire /ledger/38 (Georgia/Apalachee missions destroyed 1702-1704, c2) names this dossier; this row draws no land in southern Georgia in 1700-1712 (0 km2 overlap), so the Spanish side should use nobody or a Creek counterpart, or this dossier adds the raids as a Queen Anne's War zone without a gain; route to am-06-b
- english-colonial-empire 1713 split (british-colonial-empire) <-> british-colonial-empire  merge: exception. eu-11 not written
- english-colonial-empire 1746 occupation_start (french-india) <-> french-india  occupation_start: missing. the French occupation of Madras 1746-1749 is missing on this side (fix listed); french-india (sa-06) not written
- english-colonial-empire 1762 loss (british-empire) <-> british-empire  gain: exception. Bombay row hand-over (c1); sa-06 not written
- english-colonial-empire 1763 gain (carnatic-sultanate) <-> carnatic-sultanate  loss: exception. Chingleput (c2); sa-05 not written
- english-colonial-empire 1763 gain (hyderabad-state) <-> hyderabad-state  loss: exception. Masulipatnam (c1); sa-05 not written
- english-colonial-empire 1778 loss (british-empire) <-> british-empire  gain: exception. Masulipatnam row hand-over (c1); sa-06 not written
- english-colonial-empire 1779 dissolve (british-empire) <-> british-empire  gain: exception. Madras row hand-over (c1); sa-06 not written

## Problems

- No page failed. Pages opened: English overseas possessions, Province of New York, Treaty of Saint-Germain-en-Laye (1632), Madras Presidency (twice), Willoughbyland.
- Three small fixes applied by the reviewer (/ledger/38 counterpart, /ledger/1 note, /keyframe_review/27 note); the dossier re-validates with 0 errors and 0 warnings (--resolve).
- Verdict thin rather than fail: every confidence-3 event checked is on its page with its year; the unapplied findings (Treaty of Hartford mirror and the Connecticut valley, the 1746-1749 French occupation of Madras, Eleuthera/Bahamas and Surat keyframe consistency) are missing or inconsistent events, none a fabrication or a factor-of-two area. A gap-filler with the Treaty of Hartford and Madras Presidency pages can close the first two.
- Neighbour dossiers on disk and read: new-netherland, spanish-empire, portuguese-empire, morocco, saadi-sultanate, haudenosaunee, itza-mayans, and dutch-suriname (not in the context list but the Suriname counterpart). The rest of the context list (new-france, mughal-empire, british-colonial-empire, british-empire, french-india, carnatic-sultanate, hyderabad-state, dutch-republic and the others) is not written yet.
- Mismatches to route to other groups: portuguese-empire (counterpart kingdom-of-england for Bombay and Tangier; no 1665 loss), haudenosaunee /ledger/22 (Nanfan deed counterpart), spanish-empire /ledger/38 (1704 mission frontier counterpart).
