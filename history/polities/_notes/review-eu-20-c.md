# Review of batch eu-20-c (2026-10-31)

Adversarial review of the six eu-20-c dossiers. Validator: 0 errors, 0 warnings for all six, before and after the reviewer's edits (--resolve). Spot checks were opened with WebFetch on the pages named below; budget 4 events per dossier (all six states have 20 or fewer Cliopatria shapes). Small fixes verified on a page were applied in place and are marked applied; the rest go back to the author or a gap-filler.

Summary: Baden fix (applied), Württemberg thin, Salzburg thin, Hesse FAIL (Hanau held as a rump 1807-1813 against the dossier's own certainty note and keyframes), Italian Republic thin, Etruria fix (applied).

## electorate-of-baden: fix

Area: infobox None km2 (None), Cliopatria 7391 km2, ratio None; acknowledged True. No infobox area on the Electorate of Baden page; the author says so in keyframe notes.

Findings:
- `/ledger/4/region (and /ledger/0/region, /keyframe_review/0/correction, /keyframe_review/1/correction)` (APPLIED by reviewer). The note names the imperial cities Biberach and Wimpfen but the region held only Schliengen, and both towns lie east of the Cliopatria shape (bbox ends 8.78 E). Evidence: German mediatisation, table 3 under Baden: 'Biberach an der Riß; Gengenbach; Offenburg; Pfullendorf; Überlingen; Wimpfen; Zell am Harmersbach'. Fix: Added circles Biberach (9.79 E 48.10 N, 8 km) and Wimpfen (9.16 E 49.23 N, 5 km) to the gain, the found region and both corrections; note says Wimpfen's fate after 1803 is not on the page.

Gaps for a gap-filler:
- `/ledger/6`: Extent of the Breisgau and 'other territories' of 26 December 1805 (Freiburg 30 km circle is a placement; the land enters the Grand Duchy's 1806 shape). Try: https://en.wikipedia.org/wiki/Further_Austria
- `/ledger/5`: Which Palatine districts (Heidelberg, Mannheim, Ladenburg?) Baden took in 1803; the Heidelberg circle is a reading. Try: https://en.wikipedia.org/wiki/Reichsdeputationshauptschluss

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Electorate_of_Baden: confirmed: 'In 1803, the Imperial diet bestowed the office of Prince-elector to Charles Frederick'; month 4 from the Recess
- `/ledger/1` https://en.wikipedia.org/wiki/German_mediatisation: confirmed: table 1 under Baden 'Constance', table 2 'Petershausen; Salem', table 3 'Pfullendorf; Überlingen'
- `/ledger/5` https://en.wikipedia.org/wiki/Electorate_of_Baden: confirmed: 'received the Bishopric of Constance, part of the Electorate of the Palatinate, and other smaller districts'
- `/ledger/6` https://en.wikipedia.org/wiki/Electorate_of_Baden: confirmed: 'later in 1805, when the Peace of Pressburg occurred, he obtained Breisgau'; Pressburg page dates it 26 December 1805
- `/ledger/2-3` https://en.wikipedia.org/wiki/German_mediatisation: confirmed: 'Speyer: right bank; Strasbourg: right bank', 'Odenheim and Bruchsal', Gengenbach, Offenburg, Zell am Harmersbach

## electorate-of-wurttemberg: thin

Area: infobox None km2 (None), Cliopatria 9898 km2, ratio None; acknowledged True. No infobox area; acknowledged.

Findings:
- `/ledger (new event 1805-12 before /ledger/2)` (for the author). The Pressburg gain is missing although the page the author cited states it and habsburg-monarchy carries the mirror loss (L121, 1805-12, 'the scattered Austrian holdings in Swabia', counterpart electorate-of-wurttemberg); the Baden dossier records its equivalent. Evidence: Electorate of Württemberg page: 'in the Peace of Pressburg in December 1805 the elector was rewarded with various parts of Further Austria in the Swabian Circle and with other lands in the area'. Fix: Add a gain 1805-12, counterpart habsburg-monarchy (or further-austria), confidence 2, region the Austrian Swabian lands once a page names them (e.g. Hohenberg/Rottenburg, Ehingen, Altdorf), as Baden did with a placement circle.
- `/ledger/1/region` (for the author). Ten circles for fourteen places: Weil (der Stadt), Schöntal, Heiligkreuztal and Rottenmünster have none (the last two sit near Zwiefalten and Rottweil). Evidence: German mediatisation tables 2-3 under Württemberg list 'Ellwangen; Heiligkreuztal; Rottenmünster; Schöntal; Zwiefalten' and nine cities incl. 'Weil'. Fix: Add circles at Weil der Stadt (8.87 E 48.75 N) and Schöntal (9.50 E 49.33 N), or note they fall inside the shape.

Gaps for a gap-filler:
- `/ledger (1805-12 gain)`: The Further Austrian lands in Swabia ceded to Württemberg at Pressburg, by name. Try: https://en.wikipedia.org/wiki/Further_Austria
- `/keyframe_review/0`: No area figure on the page to test the 9,898 km2 shape (only the 1803 increase of about 850 sq mi). Try: https://en.wikipedia.org/wiki/Duchy_of_W%C3%BCrttemberg

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Electorate_of_W%C3%BCrttemberg: confirmed: 'In 1803, the Imperial diet raised the Duchy of Württemberg to an Electorate'
- `/ledger/1` https://en.wikipedia.org/wiki/German_mediatisation: confirmed: abbeys Ellwangen, Heiligkreuztal, Rottenmünster, Schöntal, Zwiefalten and cities Aalen, Esslingen, Giengen, Heilbronn, Reutlingen, Rottweil, Schwäbisch Gmünd, Schwäbisch Hall, Weil; the Württemberg page gives 'nine free imperial cities ... about 850 square miles'
- `/ledger/2` https://en.wikipedia.org/wiki/Electorate_of_W%C3%BCrttemberg: confirmed: 'On 1 January 1806, Duke Frederick III was given the title of King of Württemberg'; infobox ruler 1803-1806

## electorate-of-salzburg: thin

Area: infobox None km2 (None), Cliopatria 8669 km2, ratio None; acknowledged True. No infobox area; acknowledged.

Findings:
- `/wars/0/zones and /wars/0/note` (APPLIED by reviewer). The war note said 'no campaign took its ground' and the zones were empty, but the Salzburg page the author cited says French troops entered in October 1805. Evidence: Electorate of Salzburg page: 'When in October 1805 French troops again moved in during the War of the Third Coalition'. Fix: Zone set to the Salzburg region with the page's words; note corrected.
- `/ledger (new events 1805-10 and 1805-12)` (for the author). The French occupation of October to December 1805 is not in the ledger. Evidence: Same sentence on the Electorate of Salzburg page; the page gives no withdrawal date. Fix: Add occupation_start 1805-10 (counterpart first-french-empire, region Salzburg (region), confidence 2) and an occupation_end at the Pressburg transfer or the French withdrawal once a page dates it.
- `/ledger/5/counterpart and /ledger/7/counterpart` (for the author). Counterpart austrian-empire, while the dossier that carries the mirror is habsburg-monarchy (L124, 1805-12, gain of the Electorate of Salzburg); austrian-empire has no dossier and its row starts 1806. Evidence: habsburg-monarchy ledger L124 '1805-12 gain cp=electorate-of-salzburg'. Fix: Optional: name habsburg-monarchy for the 26 December 1805 loss so the pair matches, or leave austrian-empire and let the eu-20 Austrian Empire author mirror it.

Gaps for a gap-filler:
- `/ledger/3-4`: Which Eichstätt and Passau parts were Salzburg's in 1803-1805 (the Recess page lists Passau under Bavaria). Try: https://en.wikipedia.org/wiki/Prince-Bishopric_of_Passau
- `/ledger (1805-10)`: French occupation of Salzburg October to December 1805, with an end date. Try: https://en.wikipedia.org/wiki/Electorate_of_Salzburg

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Electorate_of_Salzburg: confirmed: 'Colloredo ... formally resigned in favour of Ferdinand on 11 February 1803'; infobox 'Archbishopric secularized: February 11, 1803'
- `/ledger/1` https://en.wikipedia.org/wiki/Electorate_of_Salzburg: confirmed: infobox 'Raised to Electorate: April 27, 1803'
- `/ledger/5` https://en.wikipedia.org/wiki/Peace_of_Pressburg_(1805): confirmed: 'the Austrian Empire annexed the Electorate of Salzburg', signed 26 December 1805; Salzburg page: 'The lands of the former archbishopric with Berchtesgaden passed to the Austrian Empire'
- `/ledger/6` https://en.wikipedia.org/wiki/Electorate_of_Salzburg: confirmed: 'the Eichstätt and Passau territories were annexed by the Kingdom of Bavaria'
- `/ledger/2-4` https://en.wikipedia.org/wiki/Electorate_of_Salzburg: confirmed: 'Augmented by the Berchtesgaden Provostry and parts of the former prince-bishoprics of Eichstätt and Passau'

## electorate-of-hesse: fail

Area: infobox None km2 (None), Cliopatria 13749 km2, ratio None; acknowledged True. No infobox area on the Electorate of Hesse page; acknowledged.

Findings:
- `/ledger/3/region and /ledger/4/region` (BLOCKING, for the author). The ledger leaves the Electorate holding Hanau as an unoccupied rump from July 1807 to November 1813: the occupation of the whole 1805 shape ends in 1807-7 (L3) but the loss to Westphalia (L4) excludes the Hanau circle, so Hanau reverts to the Electorate. This contradicts the dossier's own certainty note ('1806-1813 the state held no land') and the 1814 and 1815 keyframes (kept without Hanau, with no loss event between 1805 and 1814), and L7 then 'gains' Hanau again in 1820. Evidence: Kingdom of Westphalia page (quoted in L4): Westphalia took the Electorate 'excluding Hanau, Schmalkalden and Catzenellnbogen'; Electorate page: in 1806 Napoleon 'occupied his country and expelled him'; Fulda page (same pattern): 'Fulda was taken over by the French ... In 1810 it was given to the Grand Duchy of Frankfurt'. Fix: Either keep Hanau under the French occupation (L3 region = minus(1805 shape, Hanau circle)) and close it when a page dates Hanau's return, or record its loss in 1807 (French administration) and 1810 (Grand Duchy of Frankfurt, already in counterparts_needing_dossiers) with a source; then make the 1813-1820 sequence (L5, K2, K3, L7) consistent with whichever date the page gives for Hanau's return.
- `/ledger/1/region` (for the author). The placeholder (Cliopatria 1803 shape within 60 km of Mainz) takes in Hanau (about 48 km from Mainz), which Hesse-Kassel had held since 1736, so the 1803 gain claims old land. Evidence: Hanau page: 'Those parts of his county belonging to the County of Hanau-Münzenberg, which included Hanau, were inherited by the Landgrave of Hesse-Kassel' (1736). The Electorate page gives only 'some former French territory around Mainz'. Fix: Replace the placeholder by the 1803 gains once a page names them, or exclude the old Hanau lands from it; keep confidence 2 and say the region is a placeholder.
- `/identity/rulers/1 and /identity/rulers/2` (APPLIED by reviewer). William II and Frederick William had no source. Evidence: Electorate of Hesse infobox: '1821–1847: William II', '1847–1866: Frederick William'; 'William I died on 27 February 1821 and was succeeded by his son, William II'; 'had become Elector on his father's death (20 November 1847)'. Fix: Source added (Electorate of Hesse page).

Gaps for a gap-filler:
- `/ledger/7`: The +3,285 km2 of 1820 (Hanau, Schmalkalden and the eastern lands) from an unnamed counterpart at confidence 1; Hanau and Schmalkalden were old Hesse-Kassel lands, probably restored in 1813-1815, so the 1814 and 1815 keyframes may need adjust rather than a 1820 gain. Try: https://en.wikipedia.org/wiki/Grand_Duchy_of_Frankfurt
- `/ledger/1`: The actual 1803 compensation (the Recess's award to Hesse-Kassel; the German mediatisation page has no Hesse-Kassel row). Try: https://en.wikipedia.org/wiki/Reichsdeputationshauptschluss
- `/keyframe_review/4-5`: 1820 and 1840 shapes unverified (page budget). Try: https://en.wikipedia.org/wiki/Electorate_of_Hesse

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Electorate_of_Hesse: confirmed: 'in 1803 he was compensated for these losses with some former French territory around Mainz' (region is a placeholder, see fixes)
- `/ledger/2` https://en.wikipedia.org/wiki/Electorate_of_Hesse: confirmed: 'after the Battle of Jena-Auerstedt, the latter ... occupied his country and expelled him' (1806)
- `/ledger/6` https://en.wikipedia.org/wiki/Prince-Bishopric_of_Fulda: confirmed: 'occupied by Austria from 1813 and by Prussia from 1815 ... gave it to the Electorate of Hesse in 1815'
- `/ledger/8` https://en.wikipedia.org/wiki/Electorate_of_Hesse: confirmed: 'the Electorate was at once overrun with Prussian troops; Kassel was occupied (20 June)'
- `/ledger/10` https://en.wikipedia.org/wiki/Electorate_of_Hesse: confirmed: 'By the Peace of Prague, Hesse-Kassel was annexed to Prussia'; infobox 1866 (month 8 from the kingdom-of-prussia dossier, flagged)

## italian-republic: thin

Area: infobox 53000 km2 (1808), Cliopatria 47106 km2, ratio 0.89; acknowledged True. Infobox '1808: 20,500 sq mi (53,000 km2)'; page text 'At its peak, the kingdom covered 84,000 square kilometers' vs 1811-1813 shape 84,881 (1.01). The corrected 1808 land (about 89,000 km2) is 1.68 times the infobox; the author resolves it against the infobox in notes.

Findings:
- `/ledger/6/confidence` (APPLIED by reviewer). Confidence 3 with the whole Bozen province, while the page names only the land 'up to the city of Bolzano'. Evidence: Kingdom of Italy (Napoleonic): 'gaining as reward all the southern Tirol up to the city of Bolzano'; the department 'mainly corresponds to the province of Trentino including the city of Bolzano'. Fix: Lowered to 2 with a note. The author may also narrow the region to Trento plus the Bolzano area.
- `/ledger (new gain 1808) and /ledger/7/region` (for the author). Ragusa is missing: the dossier's notes say the Kingdom page never lists it among the gains, but the page says it was annexed in spring 1808 and later ceded by Italy at Schönbrunn. Evidence: Kingdom of Italy (Napoleonic): 'The conquered Republic of Ragusa was annexed in spring 1808 by General Auguste de Marmont'; 'which in turn ceded Istria, Dalmatia and Ragusa to France'; Illyrian Provinces page (author's quote): 'adjudicated to the Napoleonic Kingdom of Italy in 1805 and 1808'. Fix: Add a gain 1808 (spring), counterpart republic-of-ragusa (a polities.csv row), region the Dubrovnik coast (admin1 Dubrovacko-Neretvanska or a circle), confidence 2; add Ragusa to the 1810 loss region and to the 1808 and 1809 corrections; fix the sentence in notes.
- `/ledger (new loss 1806) and /ledger/2/region` (for the author). The 1806 loss of Massa and Carrara and the gain of Cattaro are missing. Evidence: Kingdom of Italy (Napoleonic): the Kingdom gained the Venetian territories 'with Cattaro, though it lost Massa and Carrara'. Fix: Add a loss of Massa and Carrara in 1806 (counterpart: the Principality of Lucca and Piombino, no row; see counterparts_needing_dossiers) and add the Bay of Kotor to the 1806 gain and corrections, or say in a note why not.

Gaps for a gap-filler:
- `/wars/2 and /ledger`: The 1813-1814 campaign: the Austrian advance into Venetia and Illyria from late 1813, the Neapolitan occupation of the Marches and Romagna (early 1814) and the Mincio (8 February 1814) are not ledger events (contest/occupation). Try: https://en.wikipedia.org/wiki/War_of_the_Sixth_Coalition
- `/ledger/8`: The 1814 partition: the whole 1812 shape is given to austrian-empire at confidence 2, but the Legations and the Marches returned to the Papal States and Modena to its duke (papal-states L39 has a 1814 gain of 'the restored state'). Try: https://en.wikipedia.org/wiki/Kingdom_of_Lombardy%E2%80%93Venetia

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Kingdom_of_Italy_(Napoleonic): confirmed: 'The Kingdom of Italy was born on 17 March 1805'
- `/ledger/2` https://en.wikipedia.org/wiki/Kingdom_of_Italy_(Napoleonic): confirmed: 'Napoleon annexed to Italy the territory of the former Republic of Venice, as announced on 30 March 1806, and ratified on 1 May' (Cattaro and Massa-Carrara omitted, see fixes)
- `/ledger/3` https://en.wikipedia.org/wiki/Kingdom_of_Italy_(Napoleonic): confirmed: 'On 2 April 1808, following the dissolution of the Papal States, the Kingdom annexed the present-day Marches'
- `/ledger/6` https://en.wikipedia.org/wiki/Kingdom_of_Italy_(Napoleonic): confirmed date ('The final territorial change came into effect on 10 June 1810'); region broader than the page, confidence lowered
- `/ledger/7` https://en.wikipedia.org/wiki/Kingdom_of_Italy_(Napoleonic): confirmed: 'Italy lost Istria and the never fully incorporated Dalmatia' (10 June 1810); Ragusa omitted
- `/ledger/9` https://en.wikipedia.org/wiki/Kingdom_of_Italy_(Napoleonic): confirmed: 'Eugène surrendered on 23 April ... the Austrians, who occupied Milan on 28 April'

## kingdom-of-etruria: fix

Area: infobox 15200 km2 (1808), Cliopatria 23128 km2, ratio 1.52; acknowledged True. Infobox area is dated 1808, after the kingdom's end; acknowledged in keyframe note.

Findings:
- `/identity/rulers/1 and /identity/rulers/2` (APPLIED by reviewer). Charles Louis and Maria Luisa had no source. Evidence: Kingdom of Etruria infobox: '1803–1807: Louis II'; '1803–1807: Maria Luisa'; body: 'his underage son Charles Louis succeeded him'. Fix: Source added (Kingdom of Etruria page).
- `/identity/predecessors` (for the author). The infobox lists the State of the Presidi as a predecessor, which the dossier omits while its certainty note calls the Presidi edge unchecked. Evidence: Kingdom of Etruria infobox: Predecessor 'Grand Duchy of Tuscany' and 'State of the Presidi'. Fix: Add the State of the Presidi as a predecessor (no polities.csv row; see counterparts_needing_dossiers) with the land round Orbetello, or say in notes why not.

Gaps for a gap-filler:
- `/keyframe_review/1`: Whether Lucca, Piombino, Elba and the Presidi lie inside the 23,128 km2 shape (infobox 15,200 km2 for 1808, ratio 1.52, acknowledged). Try: https://en.wikipedia.org/wiki/State_of_the_Presidi

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Kingdom_of_Etruria: confirmed: 'created by the Treaty of Aranjuez, signed at Aranjuez, Spain on 21 March 1801'
- `/ledger/1` https://en.wikipedia.org/wiki/Kingdom_of_Etruria: confirmed: 'In 1807, Napoleon dissolved the kingdom and integrated it into France'; infobox 'Disestablished: December 10, 1807'
- `/ledger/2` https://en.wikipedia.org/wiki/Kingdom_of_Etruria: confirmed: as /ledger/1

## Cross-dossier matrix

- electorate-of-baden 1803 found (counterpart margraviate-of-baden) -> margraviate-of-baden 1803 dissolve: matched. 
- electorate-of-baden 1803 gain (counterpart prince-bishopric-of-constance) -> prince-bishopric-of-constance 1803 dissolve: matched. dissolve with successor electorate-of-baden
- electorate-of-baden 1803 gain (counterpart prince-bishopric-of-speyer) -> prince-bishopric-of-speyer 1803 dissolve: matched. right-bank lands round Bruchsal
- electorate-of-baden 1803 gain (counterpart prince-bishopric-of-strasbourg) -> prince-bishopric-of-strasbourg 1803 dissolve: matched. 
- electorate-of-baden 1803 gain (counterpart holy-roman-empire-minor-states) -> holy-roman-empire-minor-states 1803 loss: matched. HRE minor states L108 (month 2 vs 4)
- electorate-of-baden 1803 gain (counterpart duchy-of-bavaria) -> none: missing. duchy-of-bavaria (eu-09) has no 1803 loss of the right-bank Palatinate (Heidelberg/Mannheim) to Baden
- electorate-of-baden 1805 gain (counterpart further-austria) -> further-austria 1805 dissolve: matched. also habsburg-monarchy L122 1805-12 loss cp electorate-of-baden
- electorate-of-baden 1805 dissolve (counterpart grand-duchy-of-baden) -> none: exception. grand-duchy-of-baden belongs to eu-20, not yet written
- electorate-of-wurttemberg 1803 found (counterpart duchy-of-wurttemberg) -> duchy-of-wurttemberg 1803 dissolve: matched. month 2 vs 4
- electorate-of-wurttemberg 1803 gain (counterpart holy-roman-empire-minor-states) -> holy-roman-empire-minor-states 1803 loss: matched. HRE minor states L107
- habsburg-monarchy 1805 loss (counterpart electorate-of-wurttemberg) -> none: missing. habsburg-monarchy L121 (Swabian holdings) has no gain in electorate-of-wurttemberg: fix on the Württemberg side
- electorate-of-wurttemberg 1805 dissolve (counterpart kingdom-of-wurttemberg) -> none: exception. eu-20, not yet written
- electorate-of-salzburg 1803 found (counterpart prince-archbishopric-of-salzburg) -> prince-archbishopric-of-salzburg 1803 dissolve: matched. 
- electorate-of-salzburg 1803 gain (counterpart prince-provostry-of-berchtesgaden) -> prince-provostry-of-berchtesgaden 1803 dissolve: matched. 
- electorate-of-salzburg 1803 gain (counterpart prince-bishopric-of-eichstatt) -> prince-bishopric-of-eichstatt 1802 dissolve: matched. within a year
- electorate-of-salzburg 1803 gain (counterpart prince-bishopric-of-passau) -> prince-bishopric-of-passau 1803 dissolve: matched. Passau's dissolve names duchy-of-bavaria with electorate-of-salzburg among successors
- electorate-of-salzburg 1805 loss (counterpart austrian-empire) -> habsburg-monarchy 1805 gain: mismatch. land and date agree; Salzburg names austrian-empire (not written), habsburg-monarchy L124 carries the gain
- electorate-of-salzburg 1805 loss (counterpart kingdom-of-bavaria) -> none: exception. kingdom-of-bavaria (eu-20) not written; duchy-of-bavaria ends 1805-12 without it
- habsburg-monarchy 1803 vassal_start (counterpart electorate-of-salzburg) -> none: mismatch. habsburg-monarchy L116/L123 make Salzburg a Habsburg vassal 1803-1805; no page opened supports it (an Imperial electorate under a Habsburg prince); route to eu-09
- electorate-of-hesse 1803 found (counterpart landgraviate-of-hesse-kassel) -> landgraviate-of-hesse-kassel 1803 dissolve: matched. 
- electorate-of-hesse 1803 gain (counterpart electorate-of-mainz) -> none: missing. electorate-of-mainz (eu-09) has no loss to Hesse-Kassel; the land is unlocated on both sides
- holy-roman-empire-minor-states 1803 loss (counterpart electorate-of-hesse) -> none: mismatch. HRE minor states L109 gives the Duchy of Westphalia, right-bank Worms and Friedberg to electorate-of-hesse; those went to Hesse-Darmstadt (kingdom-of-prussia L50 takes the Duchy of Westphalia from grand-duchy-of-hesse in 1815); route to eu-09
- electorate-of-hesse 1806 occupation_start (counterpart first-french-empire) -> none: exception. eu-20, not yet written
- electorate-of-hesse 1807 loss (counterpart kingdom-of-westphalia) -> none: exception. eu-20, not yet written
- electorate-of-hesse 1813 gain (counterpart kingdom-of-westphalia) -> none: exception. eu-20, not yet written
- electorate-of-hesse 1815 gain (counterpart kingdom-of-prussia) -> none: missing. kingdom-of-prussia (eu-09) has no Fulda event 1815
- electorate-of-hesse 1820 gain (counterpart unnamed (page silent)) -> none: exception. confidence 1, gap
- electorate-of-hesse 1866 occupation_start (counterpart kingdom-of-prussia) -> none: missing. kingdom-of-prussia has no 1866 occupation of Hesse-Kassel
- electorate-of-hesse 1866 loss (counterpart kingdom-of-prussia) -> kingdom-of-prussia 1866 gain: matched. prussia L66 1866-8
- italian-republic 1802 found (counterpart cisalpine-republic) -> none: exception. eu-20, not yet written
- italian-republic 1806 gain (counterpart habsburg-monarchy) -> habsburg-monarchy 1805 loss: matched. habsburg L120 1805-12 Venetia, Istria and Dalmatia
- italian-republic 1808 gain (counterpart papal-states) -> papal-states 1808 loss: matched. papal L37 1808-4
- italian-republic 1810 gain (counterpart kingdom-of-bavaria) -> none: exception. eu-20, not yet written
- italian-republic 1810 loss (counterpart first-french-empire) -> none: exception. eu-20, not yet written
- italian-republic 1814 loss (counterpart austrian-empire) -> none: exception. eu-20 not written; papal-states L39 1814 gain names first-french-empire for the restored state, while this dossier gives the Legations and Marches to Austria
- kingdom-of-etruria 1801 found (counterpart grand-duchy-of-tuscany) -> none: exception. eu-20, not yet written
- kingdom-of-etruria 1807 loss (counterpart first-french-empire) -> none: exception. eu-20, not yet written

## Problems and routing

- No page failed to load; the Principality of Hanau and Hanau pages loaded but are silent on 1806-1815.
- Reviewer fixes applied in place and re-validated (0 errors, 0 warnings with --resolve): electorate-of-baden (Biberach, Wimpfen), electorate-of-hesse (ruler sources), electorate-of-salzburg (war zone), italian-republic (L6 confidence 3 to 2), kingdom-of-etruria (ruler sources).
- eu-09 neighbour dossiers need fixes: holy-roman-empire-minor-states L109 gives Hesse-Darmstadt's 1803 awards to electorate-of-hesse; habsburg-monarchy L116/L123 treat Salzburg as a Habsburg vassal; duchy-of-bavaria lacks the 1803 Palatinate loss to Baden; electorate-of-mainz lacks a loss to Hesse-Kassel; kingdom-of-prussia lacks Fulda 1815 and the 1866 occupation of Hesse-Kassel.
- Most Context neighbours (eu-20: austrian-empire, kingdom-of-bavaria, first-french-empire, grand-duchy-of-tuscany, kingdom-of-westphalia and others) are not written yet; their mirrors are counted as exceptions.

Counterparts needing dossiers: State of the Presidi (state-of-the-presidi, 1557-1801); Principality of Lucca and Piombino (took Massa and Carrara from the Kingdom of Italy in 1806) (principality-of-lucca-and-piombino, 1805-1814).
Gazetteer names used as coordinates by the reviewer: Biberach an der Riß, Wimpfen.
