# Review of batch am-07-x (2026-10-19)

Adversarial review of the sixteen additions dossiers (states Cliopatria lacks: Rupert's Land, the Thirteen Colonies, Russian America, the Canadas, Newfoundland, the Pacific and Maritime colonies, the Floridas). The machine copy is history/notes/phase-b/reviews/am-07-x.json.

## Summary

- Validator: 16 of 16 valid, 0 errors, 0 warnings under --resolve.
- Spot checks: 69 events opened on the cited pages (weighted to confidence 3 and the largest land moves); all confirmed as the page reads. No fabricated or mis-dated event found.
- Verdicts: pass 8 (russian-america, province-of-canada, colony-of-vancouver-island, colony-of-british-columbia, british-east-florida, colony-of-cape-breton-island, colony-of-new-brunswick, colony-of-prince-edward-island); thin 8 (rupert-s-land, thirteen-colonies, province-of-quebec, upper-canada, lower-canada, dominion-of-newfoundland, british-west-florida, colony-of-nova-scotia). No fail.
- Thin here means: a border move the pages give (or the counterpart's dossier holds) is not in the ledger; nothing in these dossiers is wrong as written, but each item below is work for the author or a gap-filler. Applied: false unless marked.
- Reviewer fix applied: rupert-s-land /keyframe_review/2/note (area acknowledgement), re-validated.

## rupert-s-land: thin

- **/keyframe_review/2/note** (applied by reviewer): The 1821-1861 shape is about twice the area the Rupert's Land page gives, and the note said only 'No area on either page'.
  - Evidence: Rupert's Land page: 'spanned an area of about 3,861,400 square kilometres'; the 1821 correction resolves to 28,847 cells (about 7.3 M km2 by cell count, 7.7 M km2 by cell area), ratio 1.9-2.0, because the North-Western Territory is added.
  - Fix: Appended an area-check sentence to the note naming the ratio and its cause (North-Western Territory added; gazetteer overshoot into Alberta and Nunavut). Validated: 0 errors, 0 warnings.
- **/ledger/8** (to do): The Convention of 1818 is recorded only as a loss; the land the United States ceded north of the 49th parallel (the Missouri/Milk River drainage) has no gain, and the 1670 shape already draws all of Alberta and Saskatchewan.
  - Evidence: Convention of 1818 page: 'the United States ceded the northernmost edge of the Missouri Territory north of the 49th parallel'; the united-states-of-america dossier has /ledger/35 (1819.1 loss to british-colonial-empire, Alberta and Saskatchewan) with no gain on this side.
  - Fix: Add a gain 1818.10 counterpart united-states-of-america (confidence 2): the Missouri-drainage strip north of 49 N in southern Alberta and Saskatchewan (e.g. intersect Alberta/Saskatchewan with a polygon about 114-104 W, 49-49.8 N, text from the page), and minus that strip from the /keyframe_review/0 correction.
- **/ledger** (to do): No mirror for the two Hudson's Bay Company leases recorded in this batch: russian-america /ledger/6 and /ledger/8 (vassal_start 1839, vassal_end 1867.10, counterpart rupert-s-land) and colony-of-vancouver-island /ledger/1 and /ledger/2 (vassal_start 1849.1, vassal_end 1859, counterpart rupert-s-land).
  - Evidence: Reviewer brief 2.3: a vassal_start of X is a vassal_start in X's ledger with this state as counterpart; this ledger has no event in 1839, 1849, 1859 or 1867 (Russian America page: HBC 'was leased the southern edge of Russian America in 1839'; Colony of Vancouver Island page: 'The company had leased the island from Britain during 1849-1859').
  - Fix: Either add vassal_start/vassal_end pairs here (1839 and 1867.10 counterpart russian-america, region the leased mainland coast south of Cape Spencer; 1849.1 and 1859 counterpart colony-of-vancouver-island, region the island) or, if a lease is not to be drawn as vassalage, drop the four events from russian-america and colony-of-vancouver-island and say so in their notes. All three dossiers must agree.
- Gap /ledger: Red River Colony grant of 1811 (Selkirk) and the dated posts the HBC page lists without years (Fort Albany); the end of the 1821 licence (1859) that the author lists as a gap (try https://en.wikipedia.org/wiki/Red_River_Colony)
- Gap /ledger/3: York Factory 1694/1695 have no mirror in new-france (the HBC page dates them; new-france has only the 1697 raid) (try https://en.wikipedia.org/wiki/Hudson%27s_Bay_Company)
- Spot checks confirmed: /ledger/4, /ledger/8, /ledger/9, /ledger/10, /ledger/12, /ledger/13.
- Area: No Cliopatria row. Page body area (no year) against the dossier's own 1818-1820 shape (5.03 M km2 by cell count; 5.56 M by cell area): ratio 1.30-1.44, acknowledged in the 1670 and 1818 notes; the 1821-1861 shape reaches 1.9-2.0 because the North-Western Territory is added, now acknowledged (reviewer fix).

## thirteen-colonies: thin

- **/keyframe_review/5** (to do): Maine is left out of Massachusetts from its absorption to 1776, and the author's notes say 'the pages say nothing about their attachment', which is not so.
  - Evidence: Thirteen Colonies page: the Province of Maine (patent 1622) was 'absorbed by Massachusetts Bay Colony by 1658' and Maine 'remained a part of Massachusetts until achieving statehood in 1820'. The united-states-of-america dossier's /ledger/0 (1776.7 found, counterpart thirteen-colonies) includes Maine, so the successor land disagrees.
  - Fix: Add a gain (counterpart nobody, confidence 2, year 1658 'by 1658' per the page) of Maine (admin1 Maine, at least the settled coast south of the Penobscot) to Massachusetts; split /keyframe_review/5 at 1658 and add Maine to every later keyframe and to identity.successors; correct the sentence in the notes.
- **/keyframe_review/9** (to do): Vermont is left out although the united-states-of-america dossier has /ledger/2 (1777 loss of Vermont to vermont-republic), i.e. the successor holds Vermont in 1776.
  - Evidence: Province of New York page: the Dutch claim taken over in 1664 covered 'present-day New York, New Jersey, Delaware, and Vermont'.
  - Fix: Either add Vermont (as New York's claim, soft) to the 1664 gain and the later keyframes, or state in the notes why it is left out and ask the USA dossier to match.
- Gap /ledger/2: Virginia's settled extent 1607-1700 (confidence 1: the whole state from the 1624 royal charter is bridging) (try https://en.wikipedia.org/wiki/Colony_of_Virginia)
- Gap /keyframe_review/0: Settled extent of each colony before 1763 (all keyframes 1624-1762 draw whole modern states); the French and Indian War front 1754-1763 (try https://en.wikipedia.org/wiki/French_and_Indian_War)
- Spot checks confirmed: /ledger/1, /ledger/9, /ledger/10, /ledger/11, /ledger/13, /ledger/15, /ledger/16.
- Area: No area on the Thirteen Colonies page and no Cliopatria row; the 1768-1776 shape is 862k km2 (cell area), plausible for the thirteen states west to the Proclamation Line plus Kentucky and West Virginia, minus Maine and Vermont (see fixes).

## russian-america: pass

- Gap /ledger/8: End of the 1839 RAC-HBC lease (confidence 1, ended at the 1867 transfer by bridging); see also the rupert-s-land finding on the missing mirror (try https://en.wikipedia.org/wiki/RAC%E2%80%93HBC_Agreement)
- Spot checks confirmed: /ledger/0, /ledger/1, /ledger/3, /ledger/5, /ledger/6.
- Area: Russian America infobox garbled (no area); Alaska Purchase figure 1,518,800 km2 quoted by the author against the 1799-1867 shape (1.47 M km2 cell area).

## province-of-quebec: thin

- **/ledger/3** (to do): After the 1783 loss the British posts south of the lakes are not recorded as held (occupation) until 1796.
  - Evidence: Province of Quebec page: the areas south of the Great Lakes 'were later ceded to the newly established United States' in 1783 and 'The British kept a military presence there until 1796'.
  - Fix: Add occupation_start 1783.9 counterpart united-states-of-america for the western posts (Detroit, Mackinac, Niagara, Oswego as discs), carried into upper-canada at 1791.12 and ended there in 1796 (Jay Treaty).
- Gap /wars: The 1775-1776 American invasion of Quebec (Montreal held by the Continental Army November 1775 - June 1776): no war, contest or occupation (try https://en.wikipedia.org/wiki/Invasion_of_Quebec_(1775))
- Gap /keyframe_review/0: The 1763 boundaries (45th parallel, Lake Nipissing, St John River) and Anticosti/Magdalen Islands; the 1774 shape is 4.2 times the 1763 one where the Quebec Act page says 'threefold' (acknowledged in the author's notes) (try https://en.wikipedia.org/wiki/Royal_Proclamation_of_1763)
- Spot checks confirmed: /ledger/1, /ledger/2, /ledger/3, /ledger/4.
- Area: No area on the page; 1763 shape 467k km2, 1774 shape 1.94 M km2 (cell area); the 4.2x jump against the page's 'threefold' is flagged in the author's notes.

## upper-canada: thin

- **/ledger/6** (to do): The American occupation of southwestern Upper Canada after the Battle of the Thames (October 1813) to the end of the war is missing; only Detroit's loss is recorded.
  - Evidence: War of 1812 page: 'They had occupied southwestern Upper Canada after they defeated Colonel Henry Procter at Moraviantown in October' and 'the Americans retained the captured post at Fort Malden near Amherstburg until the British complied with the treaty'.
  - Fix: Add occupation_start 1813.10 counterpart united-states-of-america (Essex and Kent: Amherstburg/Fort Malden to Moraviantown, confidence 2) and occupation_end 1815 (confidence 1 or 2; the page gives no date), and draw it in /keyframe_review/2 as occupation; add the zone to the War of 1812 entry.
- Gap /ledger/0: The British-held western posts on American soil 1791-1796 (Detroit, Mackinac, Niagara, Oswego) handed over under the Jay Treaty (try https://en.wikipedia.org/wiki/Jay_Treaty)
- Spot checks confirmed: /ledger/1, /ledger/4, /ledger/5, /ledger/7, /ledger/8, /ledger/9.
- Area: Infobox 258,999 km2 (1836) against the gazetteer 'Upper Canada' region (453,703 km2 by cell count, 497k by cell area): ratio 1.75-1.92, acknowledged in /keyframe_review/0/note.

## lower-canada: thin

- **/ledger/1** (to do): The 1825 transfer of the Gulf north shore from the Saint-Jean River to Blanc-Sablon from Newfoundland to Lower Canada is missing (here and in dominion-of-newfoundland).
  - Evidence: Labrador boundary dispute page: the British North America (Seigniorial Rights) Act 1825 'moved Lower Canada's border east from the Saint-Jean River to Blanc-Sablon'.
  - Fix: Add a gain 1825 counterpart dominion-of-newfoundland (the Côte-Nord coast from the Saint-Jean River, about 64.3 W, to Blanc-Sablon, 57.1 W, as a coastal polygon intersected with Québec; confidence 2), cite the Labrador boundary dispute page, and add it to /keyframe_review/1 (split at 1825); the 'Canada (St Lawrence)' region stops at 64 W.
- Spot checks confirmed: /ledger/0, /ledger/1, /ledger/2.
- Area: Infobox 534,185 km2 (1839) against the 1809-1841 shape (467k km2 cell area): within range.

## province-of-canada: pass

- Spot checks confirmed: /ledger/0, /ledger/2, /identity/capitals.
- Area: No area on the page; the shape (964k km2) is the union of the Upper Canada and Lower Canada shapes.

## dominion-of-newfoundland: thin

- **/ledger/4** (to do): The 1825 loss of the Gulf north shore west of Blanc-Sablon to Lower Canada is missing, though the dossier cites the Labrador boundary dispute page that gives it.
  - Evidence: Labrador boundary dispute page: the 1825 Act 'moved Lower Canada's border east from the Saint-Jean River to Blanc-Sablon'.
  - Fix: Add a loss 1825 counterpart lower-canada (mirror of the lower-canada fix) and trim the Labrador-coast polygon of /keyframe_review/4 to start at Blanc-Sablon from 1825 (split the keyframe).
- **/wars** (to do): King William's War on the island (the 1696-1697 Avalon Peninsula Campaign) is not recorded.
  - Evidence: Colony of Newfoundland page: in 1696 'the French and allied Mi'kmaq armed forces wiped out all but a handful of English settlements' (Avalon Peninsula Campaign, King William's War 1688-1697).
  - Fix: Add the war with new-france and a contest_start 1696 / contest_end 1697 over the English shore (the Avalon disc of /keyframe_review/0).
- Gap /identity/capitals/0: Cuper's Cove as the seat 1610-1824 is the researcher's reading; St. John's was the seat long before 1825 (try https://en.wikipedia.org/wiki/History_of_St._John%27s,_Newfoundland_and_Labrador)
- Gap /ledger: French captures of St. John's (1708, 1762) and the French Shore (1713/1783/1904), listed by the author as gaps (try https://en.wikipedia.org/wiki/Battle_of_Signal_Hill)
- Spot checks confirmed: /ledger/0, /ledger/1, /ledger/4, /ledger/6, /ledger/7, /ledger/8, /ledger/11.
- Area: Infobox 405,212 km2 (no year; the 1927-1949 extent) against the 1927-1949 shape (392k km2 cell area); acknowledged in /keyframe_review/5/note.

## colony-of-vancouver-island: pass

- Gap /ledger/4: contest_end 1866.11 at confidence 1 is a structural handover of the San Juan dispute to the united colony; nothing for a gap-filler to find (try https://en.wikipedia.org/wiki/Pig_War_(1859))
- Spot checks confirmed: /ledger/0, /ledger/1, /ledger/3, /ledger/5.
- Area: No area on the page; the island polygon is 29k km2 against the island's 31k km2.

## colony-of-british-columbia: pass

- Gap /ledger/6: contest_start 1866.11 at confidence 1 is the inherited San Juan dispute; structural (try https://en.wikipedia.org/wiki/Pig_War_(1859))
- Spot checks confirmed: /ledger/0, /ledger/2, /ledger/4, /ledger/7, /ledger/8.
- Area: No area on either page; the 1866-1871 shape is the province of British Columbia (932k km2 cell area).

## british-west-florida: thin

- **/keyframe_review/0** (to do): The northern boundary move from 31 N to 32 28' N (Yazoo to Chattahoochee) is not in the ledger or the keyframes; it roughly doubles the province for its last fourteen years. The author flagged it as 'not on the pages'.
  - Evidence: West Florida page: 'In 1767, the British moved the northern boundary to the 32 28' north latitude', 'extending from the Yazoo to the Chattahoochee River'; 'The northern boundary was arbitrarily set at the 31st parallel north.'
  - Fix: Add a gain 1767 counterpart nobody (Mississippi and Alabama between 31 N and 32.47 N, from the Mississippi to the Chattahoochee, confidence 2, citing the West Florida page), split /keyframe_review/0 at 1767, and carry the strip through the 1779-1781 keyframes and the losses.
- Spot checks confirmed: /ledger/3, /ledger/4, /ledger/5, /identity/end.
- Area: No area on the page; the drawn 63k km2 lacks the 1767 strip to 32 28' N (see fixes).

## british-east-florida: pass

- Spot checks confirmed: /ledger/1, /keyframe_review/0.
- Area: No area on the page; 126k km2 for Florida east of the Apalachicola is plausible.

## colony-of-nova-scotia: thin

- **/ledger/2** (to do): Sunbury County (1765) and its eastern-Maine claim to the Penobscot are missing; the author lists them as 'page silent', but the page he cites gives them.
  - Evidence: Nova Scotia page: 'In 1765, the county of Sunbury was created. This included the territory of present-day New Brunswick and eastern Maine as far as the Penobscot River.'
  - Fix: Add a contest_start 1765 counterpart thirteen-colonies (Massachusetts) over Maine east of the Penobscot (soft; confidence 2) and its end (1783 Treaty of Paris, St Croix line; confidence 1 unless a page is found), and correct the gap entry.
- **/ledger/0** (to do): 1710-1713 is a cession here (found with the whole peninsula from 1710) but an occupation in new-france (/ledger/33 occupation_end 1713.4 counterpart british-colonial-empire).
  - Evidence: Nova Scotia page: the 1710 siege of Port Royal ended French rule in peninsular Acadia and 'the Treaty of Utrecht in 1713 formally recognized British rule'.
  - Fix: Either keep the 1710 start and ask the new-france author (group am-07) to record 1710 as a loss, or model 1710-1712 as occupation and add a 1713.4 gain counterpart new-france; the two dossiers must agree.
- Gap /ledger: British occupation of Ile Royale (Cape Breton) after Louisbourg 1758 to 1763: new-france /ledger/59 ends it in 1763 with no British-side event (try https://en.wikipedia.org/wiki/Siege_of_Louisbourg_(1758))
- Spot checks confirmed: /ledger/0, /ledger/2, /ledger/3, /ledger/5, /ledger/7, /ledger/8.
- Area: The page is the modern province article (no colonial area); the 1820-1867 shape (52k km2) matches the province (55k km2).

## colony-of-cape-breton-island: pass

- Spot checks confirmed: /ledger/0, /ledger/1.
- Area: Infobox 10,513 km2 (text 10,311) against the 10k km2 polygon.

## colony-of-new-brunswick: pass

- Spot checks confirmed: /ledger/0, /ledger/1.
- Area: Text area 72,908 km2 against the gazetteer New Brunswick (67.5k by count, 73k by cell area); acknowledged in the keyframe note.

## colony-of-prince-edward-island: pass

- Spot checks confirmed: /ledger/0, /ledger/1, /ledger/2.
- Area: Text land area 5,686 km2 against the gazetteer island (5,311 km2 by count); acknowledged.

## Cross-dossier matrix (summary)

81 territorial events: {'mismatch': 31, 'missing': 11, 'exception': 20, 'matched': 19}. Matched pairs inside the batch (Nova Scotia with its three daughter colonies, Quebec with Upper and Lower Canada and Newfoundland, the 1841 union, the 1866 union, the 1863 BC enlargement) all agree in year and land.

- mismatch: rupert-s-land /ledger/2 1686 loss (new-france) vs new-france 1686 gain: counterpart string differs (the other side names english-colonial-empire); same land and year: reconcile the string (new-france /ledger/23)
- missing: rupert-s-land /ledger/3 1694 loss (new-france): new-france has no 1694 capture of York Factory (HBC page: captured 1694); route to the new-france author
- missing: rupert-s-land /ledger/4 1695 gain (new-france): new-france has no 1695 loss of York Factory (HBC page: recovered the next year)
- mismatch: rupert-s-land /ledger/5 1697 loss (new-france) vs new-france 1697 gain: counterpart string differs (the other side names english-colonial-empire); same land and year: reconcile the string (new-france /ledger/27)
- mismatch: rupert-s-land /ledger/6 1713 gain (new-france) vs new-france 1713 loss: counterpart string differs (the other side names british-colonial-empire); same land and year: reconcile the string (new-france /ledger/37)
- mismatch: rupert-s-land /ledger/8 1818 loss (united-states-of-america) vs united-states-of-america 1819 gain: counterpart string differs (the other side names british-colonial-empire); same land and year: reconcile the string (USA /ledger/34, 1819.1 ratification vs 1818.10 signing)
- missing: united-states-of-america /ledger/35 1819 loss (british-colonial-empire): USA cedes the Missouri drainage north of 49 N; no gain in rupert-s-land (fix listed under rupert-s-land)
- mismatch: rupert-s-land /ledger/13 1870 loss (canada) vs canada 1870 gain: counterpart string differs (the other side names 'hudson-s-bay-company-lands'); same land and year: reconcile the string (canada /ledger/1); canada should name rupert-s-land
- mismatch: thirteen-colonies /ledger/9 1664 gain (new-netherland) vs new-netherland 1664 loss: counterpart string differs (the other side names english-colonial-empire); same land and year: reconcile the string (new-netherland /ledger/15,16,18)
- mismatch: thirteen-colonies /ledger/10 1673 loss (new-netherland) vs new-netherland 1673 gain: counterpart string differs (the other side names english-colonial-empire); same land and year: reconcile the string (new-netherland /ledger/20)
- mismatch: thirteen-colonies /ledger/11 1674 gain (new-netherland) vs new-netherland 1674 loss: counterpart string differs (the other side names english-colonial-empire); same land and year: reconcile the string (new-netherland /ledger/22, 1674.11 handover vs 1674.3 treaty)
- mismatch: thirteen-colonies /ledger/15 1763 gain (spanish-florida) vs spanish-florida 1763 loss: counterpart string differs (the other side names british-colonial-empire); same land and year: reconcile the string (spanish-florida /ledger/7)
- missing: russian-america /ledger/4 1814 occupation_start (kingdom-of-hawai-i): kingdom-of-hawai-i has no Fort Elizabeth event 1813-1818; route to its author
- missing: russian-america /ledger/5 1817 occupation_end (kingdom-of-hawai-i): as above
- missing: russian-america /ledger/6 1839 vassal_start (rupert-s-land): same batch: rupert-s-land has no 1839 event (fix listed under rupert-s-land)
- missing: russian-america /ledger/8 1867 vassal_end (rupert-s-land): same batch; confidence 1
- mismatch: russian-america /ledger/9 1867 loss (united-states-of-america) vs united-states-of-america 1867 gain: counterpart string differs (the other side names russian-empire); same land and year: reconcile the string (USA /ledger/71)
- mismatch: province-of-quebec /ledger/3 1783 loss (united-states-of-america) vs united-states-of-america 1783 gain: counterpart string differs (the other side names british-colonial-empire); same land and year: reconcile the string (USA /ledger/12)
- mismatch: upper-canada /ledger/2 1812 gain (united-states-of-america) vs united-states-of-america 1812 contest_*: USA records Michigan as a contest (/ledger/27, counterpart british-colonial-empire), not a loss of Mackinac; the two ledgers model the war differently and use different counterpart strings
- mismatch: upper-canada /ledger/4 1812 gain (united-states-of-america) vs united-states-of-america 1812 contest_*: USA /ledger/27 contest_start 1812.8 (Michigan) counterpart british-colonial-empire, not a loss; the two ledgers model the war differently and use different counterpart strings
- mismatch: upper-canada /ledger/5 1813 occupation_start (united-states-of-america) vs united-states-of-america 1813 contest_*: USA /ledger/28 contest_start 1813.4 (Ontario) counterpart british-colonial-empire, not an occupation; the two ledgers model the war differently and use different counterpart strings
- mismatch: upper-canada /ledger/6 1813 loss (united-states-of-america) vs united-states-of-america 1813 contest_*: USA has no 1813 gain of Detroit (its contest runs 1812.8-1815.2); the two ledgers model the war differently and use different counterpart strings
- mismatch: upper-canada /ledger/7 1813 occupation_end (united-states-of-america) vs united-states-of-america 1813 contest_*: USA has no 1813.12 event; the two ledgers model the war differently and use different counterpart strings
- mismatch: upper-canada /ledger/9 1815 loss (united-states-of-america) vs united-states-of-america 1815 contest_*: USA /ledger/30-31 contest_end 1815.2, not gains; the two ledgers model the war differently and use different counterpart strings
- missing: upper-canada /ledger/8 1813 gain (united-states-of-america): USA has no loss or contest for Fort Niagara (December 1813)
- mismatch: province-of-canada /ledger/2 1867 loss (canada) vs canada 1867 found: counterpart string differs (the other side names british-colonial-empire); same land and year: reconcile the string (canada /ledger/0)
- mismatch: dominion-of-newfoundland /ledger/1 1713 gain (new-france) vs new-france 1713 loss: counterpart string differs (the other side names british-colonial-empire); same land and year: reconcile the string (new-france /ledger/35)
- mismatch: dominion-of-newfoundland /ledger/2 1763 gain (new-france) vs new-france 1763 loss: counterpart string differs (the other side names british-colonial-empire); same land and year: reconcile the string (new-france /ledger/62, Canada ceded; the Labrador coast is not named there)
- missing: dominion-of-newfoundland /ledger/8 1927 gain (canada): canada (am-07-d) has no 1927 loss of the Labrador interior (nor the 1902 contest); route to am-07-d
- missing: colony-of-vancouver-island /ledger/1 1849 vassal_start (rupert-s-land): same batch: rupert-s-land has no 1849 event (fix listed under rupert-s-land)
- missing: colony-of-vancouver-island /ledger/2 1859 vassal_end (rupert-s-land): same batch
- mismatch: colony-of-british-columbia /ledger/8 1871 loss (canada) vs canada 1871 gain: counterpart string differs (the other side names british-colonial-empire); same land and year: reconcile the string (canada /ledger/2)
- mismatch: british-west-florida /ledger/1 1763 gain (new-france) vs new-france 1763 loss: counterpart string differs (the other side names british-colonial-empire); same land and year: reconcile the string (new-france /ledger/64)
- mismatch: british-west-florida /ledger/3 1779 loss (spanish-florida) vs spanish-florida 1779 contest_start: spanish-florida records a contest from 1779 (/ledger/8) and the gain only in 1783 (/ledger/10), counterpart british-colonial-empire; the conquests were made from Louisiana (spanish-louisiana has no 1779-1783 event): agree on who holds the land 1779-1783
- mismatch: british-west-florida /ledger/4 1780 loss (spanish-florida) vs spanish-florida 1779 contest_start: spanish-florida records a contest from 1779 (/ledger/8) and the gain only in 1783 (/ledger/10), counterpart british-colonial-empire; the conquests were made from Louisiana (spanish-louisiana has no 1779-1783 event): agree on who holds the land 1779-1783
- mismatch: british-west-florida /ledger/5 1781 loss (spanish-florida) vs spanish-florida 1783 gain: spanish-florida records a contest from 1779 (/ledger/8) and the gain only in 1783 (/ledger/10), counterpart british-colonial-empire; the conquests were made from Louisiana (spanish-louisiana has no 1779-1783 event): agree on who holds the land 1779-1783
- mismatch: british-east-florida /ledger/1 1783 loss (spanish-florida) vs spanish-florida 1783 gain: counterpart string differs (the other side names british-colonial-empire); same land and year: reconcile the string (spanish-florida /ledger/10)
- mismatch: colony-of-nova-scotia /ledger/0 1710 found (new-france) vs new-france 1713 occupation_end: new-france models 1710-1713 as a British occupation (/ledger/33) ended by cession (/ledger/34); here the land is Nova Scotia's from 1710 (fix listed)
- mismatch: colony-of-nova-scotia /ledger/2 1763 gain (new-france) vs new-france 1763 loss: counterpart string differs (the other side names british-colonial-empire); same land and year: reconcile the string (new-france /ledger/63; /ledger/59 ends a British occupation of Ile Royale that no British-side dossier starts)
- mismatch: colony-of-nova-scotia /ledger/8 1867 loss (canada) vs canada 1867 found: counterpart string differs (the other side names british-colonial-empire); same land and year: reconcile the string (canada /ledger/0)
- mismatch: colony-of-new-brunswick /ledger/1 1867 loss (canada) vs canada 1867 found: counterpart string differs (the other side names british-colonial-empire); same land and year: reconcile the string (canada /ledger/0)
- mismatch: colony-of-prince-edward-island /ledger/2 1873 loss (canada) vs canada 1873 gain: counterpart string differs (the other side names british-colonial-empire); same land and year: reconcile the string (canada /ledger/3)

## Problems for the orchestrator

- Validator: all 16 dossiers 0 errors, 0 warnings under --resolve. No fabricated or mis-dated event found: 69 spot checks across the 16 dossiers, every one confirmed on the page (WebFetch summaries).
- Reviewer applied one fix: rupert-s-land /keyframe_review/2/note now acknowledges the ratio 1.9-2.0 against the page's 3,861,400 km2 (re-validated, read back).
- Counterpart strings: about 25 mirrors exist but under different strings (british-colonial-empire, english-colonial-empire, hudson-s-bay-company-lands, russian-empire on the other side; the colony slugs of this batch here). The orchestrator should decide whether the other groups (new-france, new-netherland, spanish-florida, canada, united-states-of-america) re-point to these colony dossiers.
- Missing mirrors on other groups' dossiers: new-france lacks York Factory 1694/1695; kingdom-of-hawai-i lacks Fort Elizabeth 1814-1817; canada lacks the 1927 Labrador award and the 1902 contest; united-states-of-america lacks Fort Niagara 1813 and records the War of 1812 as contests where upper-canada records gains and occupations; spanish-florida dates its West Florida gain to 1783 where british-west-florida loses the land 1779-1781.
- Gazetteer: the 'Rupert's Land' region includes the whole of Nunavut (the Arctic Archipelago, never part of the 1670 grant) and Alberta; the 'Canada (St Lawrence)' region stops at 64 W, so the post-1825 Lower Canada north shore cannot be drawn without a polygon.
- The Colony_of_Nova_Scotia URL lands on the modern Nova Scotia article (no colonial infobox); the New Brunswick and Prince Edward Island colony pages also carry modern-province infoboxes.
- None of the section-6 Context polities of the author's brief is a counterpart of this batch (they are distant states); of them only democratic-people-s-republic-of-korea, empire-of-japan, french-louisiana, haudenosaunee and itza-mayans have dossiers. The cross-checks used the real counterparts instead: new-france, new-netherland, spanish-florida, spanish-louisiana, canada, united-states-of-america, kingdom-of-hawai-i. british-colonial-empire (eu-11) and british-empire (sa-06) have no dossier yet.
