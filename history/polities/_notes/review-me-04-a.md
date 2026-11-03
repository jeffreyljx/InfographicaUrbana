# Review of batch me-04-a (Hittites, Levant, Israel, part a)

Reviewer, 2026-10-19. The machine copy is history/notes/phase-b/reviews/me-04-a.json. Validator: 0 errors in all six dossiers; the warnings are counterpart slugs that me-04-x will write, all of them listed by the author.

| slug | verdict |
| --- | --- |
| hittites | thin |
| mitanni | fail |
| neo-hittite-states | fail |
| philistia | fail |
| phoenicia | fail |
| kingdom-of-israel | fail |

## hittites: thin

Validator 0 errors, 9 warnings (counterpart slugs of me-04-x states, all listed under counterparts_needing_dossiers). Five spot checks on the Hittites, Mitanni and treaty pages held (1400, 1345, 1258, 1185, 1180). Reviewer applied three small fixes (one confidence, the Šamuḫa/Hattusa capital years, a misquoted infobox). Thin within its 5-page budget: 11 events at confidence 1 (Syrian vassals, Arzawa, Amurru/Kadesh, Nihriya). The -1180 hand-over to neo-hittite-states does not meet that dossier's -1175 found; the finding sits on neo-hittite-states.

Findings:

- `/ledger/18/confidence` (applied by reviewer): The -1258 contest_end is at confidence 3, but its zone (Homs, Tartus, North Lebanon) is not named on any page. Evidence: Treaty page: 'ratified in the 21st year of Ramesses II's reign (1258 BC)' and 'established boundaries for the two conflicting claims', with no region named. The Hittites page says only 'southern Canaan'. Fix: Confidence 3 to 2, with a reviewer remark added to the note.
- `/identity/capitals/1/to, /identity/capitals/2/from` (applied by reviewer): The capital spans (Šamuḫa to -1350, Hattusa from -1349) do not agree with the -1350 capital_move at /ledger/3. Evidence: Hittites infobox: 'Capital-in-exile: Šamuḫa (1400–1350 BC)'. The first move (/ledger/1, -1400) uses the convention that the move year is the new capital's from. Fix: Šamuḫa to -1351, Hattusa from -1350.
- `/ledger/25/note` (applied by reviewer): The note quotes an infobox 'c. 1210–1180 BC' for Suppiluliuma II that the cited Hittites page does not carry. Evidence: Hittites page: 'Suppiluliuma II's reign began in c. 1207 BC and ended coinciding with the collapse of the Hittite Empire'. Fix: Replaced with the page's words. The year -1180 stands ('Hattusa was burnt to the ground sometime around 1180 BC').

Gaps for a gap-filler:

- `/ledger/5, /ledger/6, /ledger/7`: -1345 gains and vassals in Syria (Syrian city-states, Ugarit, Amurru) at confidence 1: the Suppiluliuma I page gives no years (try https://en.wikipedia.org/wiki/Amurru_kingdom)
- `/ledger/11, /ledger/12, /ledger/22`: Mursili II's Arzawa conquest and the vassal treaties with Mira-Kuwaliya, Hapalla and the Seha River Land, dated -1300 at confidence 1 (try https://en.wikipedia.org/wiki/Arzawa)
- `/ledger/13, /ledger/14, /ledger/16, /ledger/17`: Amurru and Kadesh 1275/1274 at confidence 1, copied from new-kingdom-of-egypt (try https://en.wikipedia.org/wiki/Battle_of_Kadesh)
- `/ledger/19`: -1220 loss to assyria at confidence 1. The Assyria dossier has no mirror gain (try https://en.wikipedia.org/wiki/Battle_of_Nihriya)
- `/ledger/10`: -1305 end of Mitanni's vassalage at confidence 1 (try https://en.wikipedia.org/wiki/Shattiwaza)
- `/wars`: Mycenaean-greece records contests with the Hittites in western Anatolia (-1315 Arzawa revolt, -1240 Wilusa, -1220). This ledger has no mirror contest events (the author explained: the pages are silent) (try https://en.wikipedia.org/wiki/Ahhiyawa)
- `/identity`: No rulers strip; no Tarhuntassa capital (Muwatalli II); Tudhaliya IV's Cyprus annexation and Kizzuwatna's incorporation are not drawn (try https://en.wikipedia.org/wiki/List_of_Hittite_kings)

Spot checks: /ledger/2 confirmed; /ledger/4 confirmed; /ledger/18 confirmed (year; region not on page, confidence lowered); /ledger/20 confirmed; /ledger/25 confirmed.

Area: Hittites infobox has no area (population 200,000+ only); confirmed by reviewer (Cliopatria max 321568 km2).

## mitanni: fail

Validator clean. Four spot checks held (1350, 1345, 1327, 1250). It fails on two counts. The Hittite vassalage of 1330–1305, which hittites.json records in this same batch, is missing here. The Assyrian vassalage and the Assyrian capture of Washukanni and the Khabur cities, which the Mitanni page states, are missing, and the capital is kept at Washukanni to the end.

Findings:

- `/ledger (after /ledger/5)`: No vassal_start by hittites at -1330 and no vassal_end at -1305. hittites /ledger/8 and /ledger/10 record both with counterpart mitanni. Evidence: Mitanni page: Shattiwaza 'c. 1330–1305 BC', 'Shattiwaza becomes a vassal of the Hittite king in exchange for help retaking part of the Mitanni territory'. Fix: Add vassal_start counterpart 'hittites' at -1330 (confidence 2, Mitanni page, region {"cliopatria":"Mitanni","year":-1300}) and vassal_end at -1305 (confidence 1).
- `/ledger (around -1300), /identity/capitals/0, /keyframe_review/6/note`: The keyframe note says Mitanni is an Assyrian vassal from Adad-nirari I, but the ledger has no vassal event. The Assyrian capture of Washukanni and the Khabur cities is missing (assyria /ledger/15 has the gain at -1300). Washukanni stays capital to -1250. The author's notes say the page keeps the rump on the Khabur to the end. Evidence: Mitanni page: Shattuara 'took an oath as a vassal' and 'paid Adad-nirari regular tribute'. In Wasashatta's revolt the Assyrians 'took Washukanni, Amasakku, Kahat, Shuru, Nabula, Hurra and Shuduhu'. Fix: Add vassal_start counterpart 'assyria' at -1300 (confidence 2; the page gives no year) and vassal_end at -1250. Add a loss to assyria at -1300 (confidence 1-2) of the Washukanni (Tell Fekheriye 40.03,36.83) and Kahat (Tell Barri, about 41.1,36.7) area, to mirror assyria /ledger/15. End Washukanni as capital at -1301, or say in the capital's note why it stays. Correct the notes file.
- `/ledger/7, /ledger/8`: The final annexation is at -1250 here and at -1244 in assyria /ledger/16, six years apart. The infobox has 'Disestablished: c. 1260 BC'. Evidence: Mitanni page: Shattuara II's revolt 'around 1250 BC'; Shalmaneser I 'annexed the kingdom' (no year). Fix: Keep -1250 (page) and route to me-02 to move assyria's gain to -1250. Mirror listed in cross_checks.

Gaps for a gap-filler:

- `/ledger/1`: -1500 gain from assyria at confidence 1 (Cliopatria's year). The page dates Shaushtatar's sack of Assur to 'c. 1450', and the dossier's own war /wars/1 is at -1450 (try https://en.wikipedia.org/wiki/Shaushtatar)
- `/wars/0`: new-kingdom-of-egypt has contest_start/contest_end with mitanni at -1445/-1438. This ledger has no contest pair, though war /wars/0 has a zone (try https://en.wikipedia.org/wiki/Thutmose_III)
- `/ledger/5`: Rename to Hanigalbat at confidence 1 (page gives no year) (try https://en.wikipedia.org/wiki/Hanigalbat)

Spot checks: /ledger/3 confirmed; /ledger/4 confirmed; /ledger/6 confirmed; /ledger/7 confirmed.

Area: Mitanni infobox has no area; confirmed by reviewer (Cliopatria max 189149 km2).

## neo-hittite-states: fail

Validator clean. Four spot checks held (c. 1175, 740, 738, 717). It fails on two counts. The -1175 found leaves five years between the Hittite hand-over at -1180 and this state's start. The -800..-741 keyframe overlaps the Neo-Assyrian -800 shape with no vassal event, although the Carchemish page, which the author opened, gives the tribute.

Findings:

- `/ledger/0, /identity/start`: Found at -1175, but hittites /ledger/23 and /ledger/25 hand the land to neo-hittite-states at -1180. For five years the land belongs to a state that does not exist yet. Evidence: Carchemish page: the mini-empire 'c. 1175 to 975 BC'. Kuzi-Teshub 'claimed the title of Great King after the fall of Hatti' and was the son of Talmi-Teshub, a contemporary of the last Hittite king. Hittites page: Hattusa 'burnt to the ground sometime around 1180 BC'. Fix: Start at -1180 (identity.start, /ledger/0, /keyframe_review/0 shape_id and from, capitals/0/from, certainty/0/from), citing 'after the fall of Hatti'. Otherwise make the Hittite -1180 loss counterpart 'nobody' and found -1175 from nobody.
- `/keyframe_review/4`: The -800..-741 keyframe is left as an overlap with neo-assyrian-empire's -800 shape, with no vassal event. That dossier gains the cells at -800 from 'Aram-Damascus and the western states (page silent)'. Evidence: Carchemish page: Sangara 'paid tribute to Kings Ashurnasirpal II and Shalmaneser III', 'probably at some time before 868 BC'. The dossier's own war /wars/0 runs -868..-848 with no zones. Fix: Add vassal_start counterpart 'neo-assyrian-empire' at -868 (confidence 2 for Carchemish, Carchemish page; region the -900 shape) and vassal_end at -717 with the dissolve, so the overlap draws as a tributary tint. me-02 should mirror it and take these cells out of its -800 gain or mark them as vassal.

Gaps for a gap-filler:

- `/ledger`: No dated falls for Melid, Gurgum, Kummuh, Sam'al or Hamath. Thin by design: budget 1-2 pages, 3 used (try https://en.wikipedia.org/wiki/Melid)
- `/ledger`: Gurgum and Kummuh tribute after 740 (try https://en.wikipedia.org/wiki/Gurgum)

Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/2 confirmed (Pattin annexed in the Hama campaign; 738 is the provinces' year); /ledger/3 confirmed.

Area: Neo-Hittite states page has no infobox (author); not re-fetched (Cliopatria max 25034 km2).

## philistia: fail

Validator 0 errors, 2 warnings (aram-damascus, listed). Five spot checks held (734, 711, 701, 609, 604). The Philistines page supports the author's -734 occupation reading over the Neo-Assyrian 'gain', so that disagreement is routed to me-02. It fails because the united-monarchy vassalage, which kingdom-of-israel records in this batch, has no mirror here, and because the -1150 found overlaps New Kingdom Egypt's Gaza coast to -1136.

Findings:

- `/ledger (after /ledger/0)`: No vassal_start by kingdom-of-israel at -1000 and no vassal_end at -930. kingdom-of-israel /ledger/2 and /ledger/9 record both with counterpart philistia. Evidence: United-monarchy page: David's sphere expanded 'to control the weaker client states of Philistia, Moab, Edom and Ammon' (biblical account; no year). Fix: Add vassal_start counterpart 'kingdom-of-israel' at -1000 and vassal_end at -930, both confidence 1, region {"cliopatria":"Philistia","year":-1000}.
- `/ledger/0`: Founded at -1150 on land taken from new-kingdom-of-egypt, but that dossier keeps the Gaza coast to -1136 and gives it to 'nobody' (new-kingdom-of-egypt /ledger/22). Both dossiers draw Gaza from -1150 to -1137. Evidence: new-kingdom-of-egypt /ledger/22: 'c. 1136: the Gaza coast, the last Egyptian holding on the Cliopatria -1150 shape, goes with the rest of Egyptian Canaan'. Philistines page: settled 'around 1175 BC'; Medinet Habu inscription 'c. 1150 BC'. Fix: Either found at -1150 without the Gaza area and add a gain from new-kingdom-of-egypt at -1136 (confidence 2) for it, with me-03 changing its -1136 counterpart to philistia; or ask me-03 to take Gaza out of its -1150 shape.

Gaps for a gap-filler:

- `/ledger/1, /ledger/2, /ledger/3`: The -1000 and -900 cuts are Cliopatria's, at confidence 1. The mirror gains are missing in kingdom-of-israel (finding on that dossier) (try https://en.wikipedia.org/wiki/Philistines)
- `/identity/capitals/0`: No capital on any page (Gaza nominal) (try https://en.wikipedia.org/wiki/Gaza_City)

Spot checks: /ledger/6 confirmed (734 Gaza conquered; page does not say annexed); /ledger/7 confirmed; /ledger/8 confirmed ('Ten years later'; tribute from Ashdod, Ashkelon, Gaza, Ekron); /ledger/10 confirmed; /ledger/12 confirmed (604/603).

Area: author reports no infobox area; Philistines page not showing one (Cliopatria max 10865 km2).

## phoenicia: fail

Validator clean. Four spot checks held (738, 677, 585-573, 539); the reviewer lowered -539 to confidence 2. It fails on four counts. The western colonies of -900..-675 are claimed twice, here and in af-02's phoenician-colonies (and carthage from -814), and the -675 split has no mirror. The -615 return of the north and Sidon has no page and conflicts with the -609 transfer of the west from neo-assyrian-empire to neo-babylonian-empire. The vassalage under Assyria (738) and Babylon (573–539) is missing, although the pages state it. The Kition cells appear at -615 without an event and are claimed by phoenician-colonies' kition hand-over.

Findings:

- `/ledger/11/confidence` (applied by reviewer): The -539 loss is at confidence 3, but the page gives 539 as the year Cyrus took Babylon and no year for the Phoenician cities. Evidence: Phoenicia page: 'In 539 BC, Cyrus the Great ... took Babylon'; the Phoenicians 'yield[ed] themselves to the Persians' (no year). Fix: Confidence 3 to 2, with a reviewer remark added to the note.
- `/ledger/1, /ledger/2, /ledger/3, /ledger/6, /keyframe_review/2-4`: Western colonies (Tunisia, Sicily, Sardinia, Iberia, Cyprus) are gained from nobody at -900, -800 and -750 and split to phoenician-colonies at -675. But phoenician-colonies (af-02, type colony) is founded at -900 with Kition and Gadir, gains the west at -700 and -675, has no predecessor and no event with counterpart phoenicia. carthage is founded at -814. The same cells are claimed by two or three dossiers. Evidence: phoenician-colonies /ledger/0: 'Late 10th century BC: Tyre begins to plant colonies' (found -900). carthage /ledger/0: 'Carthage was settled around 814 BC'. The author's notes leave the split-or-drop decision to the reviewer. Fix: Reviewer's decision: drop the colonies from this dossier. Give keyframes -900, -800 and -750 verdict adjust, with correction {"intersect":[{"cliopatria":"Phoenicia","year":Y},{"region":"Levant"}]} (the homeland). Delete /ledger/1, /ledger/2, /ledger/3 and /ledger/6. The -675, -650 and -530 'wrong' verdicts stand. Say in notes that the colonies are drawn by phoenician-colonies and carthage.
- `/ledger/7, /keyframe_review/9`: The -615 gain from neo-assyrian-empire (confidence 1, no page) has no mirror. neo-assyrian-empire /ledger/58 and neo-babylonian-empire /ledger/3 send the west ('Transpotamia') from Assyria to Babylon at -609. Evidence: Phoenicia page (reviewer fetch): no date for any regained independence after Assyria; 'Phoenician cities revolted several times throughout the reigns of the first Babylonian kings'. Fix: Delete /ledger/7. Keep the Assyrian provinces (north from -738, Sidon from -677) out of the dossier. Correct the -615 keyframe to the homeland minus the north and the Sidon circle, valid to -539. If a page shows Sidon or Arwad restored, add that gain with its page.
- `/ledger (at -738)`: No vassal_start by neo-assyrian-empire, although the page, in the sentence the dossier cites, makes Tyre and Byblos tributaries from 738. Evidence: Phoenicia page: 'By 738 BC, most of the Levant, including northern Phoenicia, was annexed; only Tyre and Byblos ... remained tributary states outside of direct Assyrian control'. Tiglath-Pileser III page: Tyre paid tribute after Arpad's fall, and 'Tiglath-Pileser also captured Tyre' (732). Fix: Add vassal_start counterpart 'neo-assyrian-empire' at -738 (confidence 3; region: the homeland minus the north) and vassal_end at -609 (confidence 1, the empire's end). me-02 should mirror it.
- `/ledger/9 (after)`: No vassal_start by neo-babylonian-empire at -573 and no vassal_end at -539. neo-babylonian-empire /ledger/8 and /ledger/11 record both with counterpart phoenicia; this ledger has only contest_end -573. Evidence: Phoenicia page: a 'period of Babylonian rule'. Tyre page (author's note): 'It came under Babylonian rule in 572 BC'. neo-babylonian-empire /ledger/8: Tyre 'eventually surrendered to him in 573 BC'. Fix: Add vassal_start counterpart 'neo-babylonian-empire' at -573 (confidence 2) and vassal_end at -539 (confidence 2), on the homeland.
- `/keyframe_review/9/correction, /ledger/10`: The -615 keyframe adds the Kition cells of Cyprus (valid -615..-571) with no gain event; the -675 split sent all non-Levant cells, Cyprus included, to phoenician-colonies. phoenician-colonies /ledger/3 gives Kition to a kition dossier at -616, and twenty-sixth-dynasty-of-egypt /ledger/4 takes 'the Phoenician cells of Cyprus' from phoenicia at -570. Evidence: Phoenicia page (reviewer fetch): Cyprus, Kition, Amasis and 570 are not mentioned. Fix: Drop the Cyprus cells from the -615 correction and delete /ledger/10 and keyframe -570. Route the 26th dynasty's -570 counterpart to kition (me-04-x).

Gaps for a gap-filler:

- `/ledger`: Tyre and Sidon pages came back thin. No Hiram I territory and no Assyrian tribute dates before 738 (try https://en.wikipedia.org/wiki/Hiram_I)
- `/ledger/5`: Sidon's later status (Babylonian king, Persian vassal kingdom) after its 677 annexation (try https://en.wikipedia.org/wiki/Sidon)

Spot checks: /ledger/4 confirmed; /ledger/5 confirmed; /ledger/8 confirmed (585-573); /ledger/11 confirmed year via Babylon 539; no Phoenician date (confidence lowered).

Area: Phoenicia infobox has no area (Established 2000 BC, Roman annexation 64 BC); confirmed by reviewer (Cliopatria max 35130 km2).

## kingdom-of-israel: fail

Validator 0 errors, 10 warnings (moab, ammon, edom, aram-damascus, all listed). Five spot checks held on the Samaria and united-monarchy pages (1047, 931, 880, 732, 722). It fails on three counts. Saul's capital Gibeah, and Jerusalem from -1008, lie in the Judah cells that the -1047 keyframe removes until -1000. The two Philistine losses to Israel (-1000, -900) have no mirror gains here, and their cells are either already in Israel's -1047 shape or enter the -900 shape with no event. The Assyrian vassal kingdom of 732–722, which the author's own Tiglath-Pileser III page states and neo-assyrian-empire records at confidence 3, is missing.

Findings:

- `/identity/capitals/0, /identity/capitals/2, /keyframe_review/0/correction`: Gibeah (35.23,31.83; -1047..-1011) and Jerusalem (35.23,31.78; from -1008) lie in Kingdom of Judah -900 cells. /keyframe_review/0 and /ledger/0 remove those cells until the /ledger/1 gain of -1000, so the capital is outside the state. Evidence: Gazetteer: intersect(Judah -900, 3 km at Gibeah) = 1 cell; intersect(the -1047 correction, same circle) = 0 cells. Page: 'Throughout the monarchy of Saul, the capital is in Gibeah'; David 'rules from c. 1000 to 961 BCE'; the page gives no year for Jerusalem. Fix: Add Benjamin (for example {"lon":35.23,"lat":31.83,"km":15}) to the -1047 correction and found region. Start Jerusalem at -1000 and keep Mahanaim to -1001, or move the /ledger/1 union to -1008 with a page.
- `/ledger (at -1000 and -900), /keyframe_review/0, /keyframe_review/3`: There are no gains mirroring philistia /ledger/1 (-1000 loss to kingdom-of-israel) or /ledger/2 (-900 loss). 8 of the 11 inland cells of Philistia -1150 are already inside Israel's -1047 keyframe, so both dossiers draw them -1047..-1001. The 9 northern coastal cells Philistia loses at -900 enter Israel's -900 shape (verdict ok) with no event. Evidence: Gazetteer: intersect(Philistia -1150, Israel -1000 minus Judah -900) = 8 cells (35.14-35.52 E, 32.02-33.13 N). intersect(minus(Philistia -1000, Philistia -900), Israel -900) = 9 cells (34.92-35.40 E, 32.46-33.03 N). intersect(Philistia -1000, the -930 keyframe) = 0 cells. Fix: Remove Philistia's -1150 cells from the -1047 correction and add a gain from philistia at -1000 (confidence 1) for them. Add a gain from philistia at -900 (confidence 1) for the coastal cells, and note it on /keyframe_review/3.
- `/ledger (at -732 and -722)`: No vassal_start by neo-assyrian-empire at -732 and no vassal_end at -722, although the author's Tiglath-Pileser III source says so. neo-assyrian-empire /ledger/16 (confidence 3) and /ledger/18 record both with counterpart kingdom-of-israel. Evidence: Tiglath-Pileser III page: he 'divided [Israel] in half', annexing the north 'as the province Megiddo' and 'subjugating the southern portion as a vassal kingdom' (732). Fix: Add vassal_start counterpart 'neo-assyrian-empire' at -732 (confidence 3, Tiglath-Pileser III page, region Samaria) and vassal_end at -722 (confidence 2).

Gaps for a gap-filler:

- `/wars/1`: Mesha's revolt (-840) has a war zone but no ledger event, and Omri's subjugation of Moab is not drawn (try https://en.wikipedia.org/wiki/Mesha_Stele)
- `/ledger/2-6, /ledger/9-13`: The united-monarchy vassals (Philistia, Moab, Ammon, Edom, Aram) are at confidence 1: the page presents them as the biblical account, with no years (try https://en.wikipedia.org/wiki/Aram-Zobah)
- `/ledger/16, /ledger/17`: Hazael's Gilead contest 842-796 at confidence 1 (try https://en.wikipedia.org/wiki/Hazael)
- `/identity`: No rulers strip (try https://en.wikipedia.org/wiki/Kings_of_Israel_and_Judah)

Spot checks: /ledger/0 confirmed; /ledger/7 confirmed; /ledger/15 confirmed; /ledger/18 confirmed; /ledger/19 confirmed (722 in one passage, c. 720 elsewhere).

Area: neither the united-monarchy nor the Samaria infobox has an area; confirmed by reviewer (Cliopatria max 20072 km2).

## Cross-dossier matrix: rows that are not matched

- hittites -1330 vassal_start (mitanni) <-> none: missing. mitanni has no vassal_start by hittites (nor the -1305 vassal_end); fix on mitanni
- hittites -1220 loss (assyria) <-> none: missing. assyria (me-02) has no gain from hittites near -1220 (Nihriya); route to me-02 or change counterpart
- hittites -1180 loss (neo-hittite-states) <-> neo-hittite-states -1175 found: mismatch. 5 years apart; fix on neo-hittite-states (start -1180) or Hittite counterpart nobody
- mitanni -1350 loss (assyria) <-> assyria -1363 gain: mismatch. 13 years apart; page: Ashur-uballit I (1365-1330) 'in the middle of the 14th century'; route to me-02 and mitanni to agree
- assyria -1300 gain (mitanni) <-> none: missing. Mitanni page supports it (Wasashatta's revolt: Washukanni, Kahat taken); fix on mitanni
- mitanni -1250 loss (assyria) <-> assyria -1244 gain: mismatch. 6 years apart; infobox c. 1260, Shattuara II revolt c. 1250; route to me-02
- neo-hittite-states -1175 found (hittites) <-> hittites -1180 loss: mismatch. see hittites -1180
- neo-hittite-states -740 loss (neo-assyrian-empire) <-> neo-assyrian-empire -740 gain: mismatch. year and land agree; NAE names the counterpart 'Arpad' not neo-hittite-states; me-02 to relabel
- neo-hittite-states -738 loss (neo-assyrian-empire) <-> neo-assyrian-empire -738 gain: mismatch. year agrees; NAE counterpart 'Pattin'; me-02 to relabel
- neo-hittite-states -717 loss (neo-assyrian-empire) <-> neo-assyrian-empire -717 gain: mismatch. year agrees; NAE counterpart 'Carchemish'; me-02 to relabel
- neo-assyrian-empire -800 gain (Aram-Damascus and the western states (page silent)) <-> neo-hittite-states None None: mismatch. NAE -800 shape overlaps the neo-hittite-states -800..-741 keyframe with no event on either side; NHS to add vassal_start -868 (Carchemish tribute), me-02 to mirror
- philistia -1150 found (new-kingdom-of-egypt) <-> new-kingdom-of-egypt -1136 loss: mismatch. NK keeps the Gaza coast to -1136 and gives it to nobody; overlap -1150..-1137
- philistia -1000 loss (kingdom-of-israel) <-> none: missing. no gain from philistia in kingdom-of-israel; 8 cells already in Israel's -1047 keyframe (overlap)
- philistia -900 loss (kingdom-of-israel) <-> none: missing. no gain in kingdom-of-israel; 9 coastal cells enter Israel's -900 shape without an event
- philistia -734 occupation_start (neo-assyrian-empire) <-> neo-assyrian-empire -734 gain: mismatch. flagged by author; reviewer sides with occupation (Philistines page: TP III 'occupied the remaining kingdoms, including Philistia'; kings kept as vassals). me-02 to change its gain to occupation_start (end -609)
- philistia -711 loss (neo-assyrian-empire) <-> none: missing. NAE has no gain of Gath at -711; route to me-02
- philistia -609 occupation_start (twenty-sixth-dynasty-of-egypt) <-> none: missing. 26th dynasty has only a contest with NBE at -609; route to me-03
- phoenicia -900 gain (nobody) <-> phoenician-colonies -900 found: mismatch. double claim of western colonies -900..-675 (also carthage from -814); reviewer: drop from phoenicia
- phoenicia -800 gain (nobody) <-> carthage -814 found: mismatch. Tunisia cells claimed by phoenicia and carthage
- phoenicia -750 gain (nobody) <-> none: mismatch. western cells also in phoenician-colonies
- phoenicia -738 loss (neo-assyrian-empire) <-> neo-assyrian-empire -738 gain: mismatch. year agrees; NAE counterpart 'Pattin' (Simirra province); me-02 to add a gain from phoenicia
- phoenicia -677 loss (neo-assyrian-empire) <-> neo-assyrian-empire -675 gain: mismatch. 2 years; Esarhaddon page gives 677 (reviewer confirmed); me-02 to move to -677
- phoenicia -675 split (phoenician-colonies) <-> none: missing. phoenician-colonies has no event or predecessor naming phoenicia
- phoenicia -615 gain (neo-assyrian-empire) <-> none: missing. no NAE loss; conflicts with NAE/NBE -609 transfer of the west; delete
- neo-assyrian-empire -738 vassal_start (phoenicia) <-> none: missing. neither side records Tyre/Byblos tributary from 738 (Phoenicia page)
- neo-babylonian-empire -573 vassal_start (phoenicia) <-> none: missing. phoenicia lacks vassal_start -573 and vassal_end -539
- kingdom-of-israel -1000 vassal_start (philistia) <-> none: missing. philistia has no vassal_start by kingdom-of-israel
- kingdom-of-israel -732 loss (neo-assyrian-empire) <-> neo-assyrian-empire -732 gain: mismatch. NAE's -732 gain of Galilee/Transjordan is labelled counterpart Aram-Damascus; me-02 to add a gain from kingdom-of-israel
- neo-assyrian-empire -732 vassal_start (kingdom-of-israel) <-> none: missing. kingdom-of-israel lacks vassal_start -732 / vassal_end -722

## Problems

- Following the orchestrator's adjustment to the brief, the reviewer applied small fixes: three to hittites.json (/ledger/18 confidence, the capitals/1-2 years, the /ledger/25 note quote) and one to phoenicia.json (/ledger/11 confidence). Each file was re-validated (0 errors) and read back. Every other finding is applied: false.
- Decisions the author asked of the reviewer: Phoenicia's Cliopatria row is trimmed, not split (drop the western cells, which phoenician-colonies and carthage draw). Philistia -734: the occupation reading stands and neo-assyrian-empire (me-02) should change its gain.
- kingdom-of-judah and tabal-kingdom are not on disk (parallel me-04 parts), so their mirrors are counted as exceptions.
- Fixes routed to other groups: me-02 (assyria -1220, -1250, -1300; neo-assyrian-empire -711 Gath, the -732 Israel counterpart, -738 Phoenicia, the -677 Sidon year, counterpart labels Arpad/Pattin/Carchemish, the -800 overlap with neo-hittite-states, the vassal mirrors), me-03 (new-kingdom-of-egypt -1136 Gaza counterpart; twenty-sixth-dynasty-of-egypt -609 occupation of Philistia, the -570 Kition counterpart), af-02 (phoenician-colonies has no event naming phoenicia).
- WebFetch answers are small-model summaries of the pages; the quotes are as returned. Every page loaded.
