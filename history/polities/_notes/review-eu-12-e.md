# Review of batch eu-12-e (Iberia and the taifas, part e)

Reviewer, 2026-10-25. Dossiers: county-of-osona, county-of-ampuria, taifa-of-alpuente, taifa-of-badajoz, taifa-of-denia. Validator: 0 errors on all five; resolve warnings only for Berguedà, Alpuente, Dénia and the slug taifa-of-majorca. Neighbour dossiers that exist and were read: almoravid-dynasty, almohad-caliphate, emirate-of-cordoba, county-of-ribagorza, holy-roman-empire; every other context polity is owned by an eu-12 or eu-13 part that has not run yet.

Findings marked [blocking] must be done by the author before the dossier is accepted; findings marked applied were done by the reviewer in place (dossier re-validated).

## county-of-osona: FAIL

Area: the infobox gives no area; the keyframe notes say so (Cliopatria max 2329.0 km2).

Findings:
- `/keyframe_review/0 and /ledger/2` (not applied) [blocking] Missing events: the new keyframe county-of-osona_798 (798-989) and the 827 rename draw Osona as a held county through 827-878, but the page says it was taken in the 826 rebellion and stayed depopulated and outside Frankish control until 879; the dossier never mentions 826 or 879. Evidence: https://en.wikipedia.org/wiki/County_of_Osona: 'After the rebellion of 826, during which Guillemó and Aissó succeeded in taking it'; 'Osona remained depopulated and outside of Frankish control until 879.'; 'In 879, Wilfred the Hairy began the repopulation of the county'. The list's 'Counts of Barcelona: 827-939' is the title, not rule over the land. Fix: Add a loss in 826 or 827 (counterpart the rebels of Aissó and Guillemó, then nobody for the abandoned land; confidence 3, the page dates it), a gain in 879 (Wilfred the Hairy's repopulation, counterpart nobody, confidence 3), a war for the revolt of 826-827 with its zone; end keyframe county-of-osona_798 at 826 and start a new keyframe in 879 (nothing drawn 827-878); move the 'counts of Barcelona' rename from 827 to 879.
- `/ledger/0/counterpart` (applied) The found event named emirate-of-cordoba as counterpart, but the page has the region abandoned in 798. Evidence: https://en.wikipedia.org/wiki/County_of_Osona: 'Louis of Aquitaine ordered Borrell, a Goth, to enter the abandoned region'; the emirate-of-cordoba dossier has no 798 loss. Fix: Counterpart set to 'nobody' (done by the reviewer, note appended; dossier re-validated, 0 errors).

Thin (for a gap-filler):
- `/ledger/4, /ledger/6, /ledger/8` The Manresa additions and losses (1003, 1040, 1056) are confidence 1 and may be wrong in direction; the page gives no year for 'the addition of the County of Manresa'. Also the 1035-1054 interval of Guisla de Lluçà (page failed for the author). Try: https://ca.wikipedia.org/wiki/Comtat_de_Manresa

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/County_of_Osona: confirmed (798, 'abandoned region'; counterpart corrected)
- `/ledger/2` https://en.wikipedia.org/wiki/County_of_Osona: not on page as claimed: the text has Osona depopulated and outside Frankish control 826-879
- `/ledger/3` https://en.wikipedia.org/wiki/County_of_Osona: confirmed ('In 990, the small pagus of Berga was detached from it and granted to Cerdanya.')
- `/ledger/5` https://en.wikipedia.org/wiki/County_of_Osona: confirmed (1035, Berenguer Ramon I, Guisla)
- `/ledger/9` https://en.wikipedia.org/wiki/County_of_Osona: confirmed (1107 dowry of Jimena to Bernard III of Besalú)
- `/ledger/10-11` https://en.wikipedia.org/wiki/County_of_Osona: confirmed (infobox 1111; 'Osona returned to Barcelona')

## county-of-ampuria: FAIL

Area: the infobox gives no area; the keyframe notes say so (Cliopatria max 928.1 km2).

Findings:
- `/keyframe_review/2 and /ledger/3` (not applied) [blocking] Unexplained halving and a gain the page contradicts: the dossier draws the three-cell 1003 outline (with Peralada, 833 km2) for 813-816 and 989-999, accepts Cliopatria's two-cell 1000 shape (404 km2) as 'ok' with no loss event, then regains Peralada in 1003 at confidence 1 from a 'County of Peralada (Pedralbes)', although the page puts Peralada inside Empúries from 813. Evidence: https://en.wikipedia.org/wiki/County_of_Emp%C3%BAries: 'Around 813, Empúries, with Peralada, became a separate county under Ermenguer.' The event's own note says 'The page is silent on a 1003 gain (it says the county enclosed Peralada from 813)'. shapes.csv: county-of-ampuria_1000 404.4 km2, _1003 832.7 km2. Fix: Mark county-of-ampuria_1000 'adjust' with correction {"cliopatria": "County of Ampuria", "year": 1003, "text": "Empúries with Peralada, as the county had been since about 813"}; delete /ledger/3; drop 'County of Peralada (Pedralbes)' from counterparts_needing_dossiers.
- `/ledger/4/region` (not applied) [non-blocking] The 1014-1019 contest zone is the whole of Cliopatria's County of Rosellón on one sentence that says only 'invaded'. Evidence: https://en.wikipedia.org/wiki/County_of_Roussillon: 'In 1014, Hugh I of Empúries invaded Roussillon, but in 1019 a pact was signed making the two counties permanently separate entities.' No ground is named. Fix: Use {"border_band": {"a": "county-of-ampuria", "b": "county-of-rosellon", "year": 1014, "width": 2}} or keep the county with the note; confidence stays 2.
- `/identity/rulers/6-7` (not applied) [non-blocking] Rulers not contiguous: William 848-850, Odalric 852-858 (gap 850-852). Evidence: Brief check 9: rulers contiguous. Fix: Say in the ruler's note that the page leaves 850-852 open, or close the gap from the page.

Thin (for a gap-filler):
- `/keyframe_review/6` The County of Barcelona page says Ramon Berenguer III 'conquered part of the County of Empúries', undated; no event. The other small Cliopatria changes (1028, 1040, 1126, 1169, 1177, 1188, 1236, 1279, 1344, about 100 km2 each) are outline noise, thin by design within the 9-page budget. Try: https://en.wikipedia.org/wiki/Ramon_Berenguer_III,_Count_of_Barcelona

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/County_of_Emp%C3%BAries: confirmed ('In 817, Empúries was merged with the County of Roussillon, a union which lasted until 989.')
- `/ledger/2` https://en.wikipedia.org/wiki/County_of_Emp%C3%BAries: confirmed ('At the death of Gausfred I in 989, Roussillon and Empúries were separated.')
- `/ledger/5` https://en.wikipedia.org/wiki/County_of_Roussillon: confirmed (1014 invasion, 1019 pact)
- `/ledger/8` https://en.wikipedia.org/wiki/County_of_Emp%C3%BAries: confirmed (1325 sale to Peter IV of Ribagorza)
- `/ledger/9` https://en.wikipedia.org/wiki/County_of_Emp%C3%BAries: confirmed (1341 trade for Prades; apanage of the Crown of Aragon)
- `/ledger/3` https://en.wikipedia.org/wiki/County_of_Emp%C3%BAries: not on page (confidence 1 bridge; page contradicts it, see fixes)

## taifa-of-alpuente: PASS

Area: the infobox gives no area; the keyframe notes say so (Cliopatria max 2878.5 km2).

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Taifa_of_Alpuente: confirmed (infobox 'Conquered by the Almoravids: 1106')
- `/ledger/0` https://en.wikipedia.org/wiki/Taifa_of_Alpuente: confirmed (taifa 'from around 1009 to 1106'; infobox 1009; confidence 2 is honest)
- `/keyframe_review/4/note` https://en.wikipedia.org/wiki/Alpuente: confirmed ('In 1103, Alpuente fell under the Almoravid dynasty.')
- `/identity/capitals/0` https://en.wikipedia.org/wiki/Alpuente: confirmed (39.87778 N, 1.01389 W; outside Cliopatria's bbox 39.967-40.355 N, so the 25 km district added to every correction is right)

## taifa-of-badajoz: FAIL

Area: the infobox gives no area; the keyframe notes say so (Cliopatria max 106876.9 km2).

Findings:
- `/keyframe_review/7` (not applied) [blocking] Keyframe and ledger disagree: the ledger loses the land north of about 40 N in 1055 (/ledger/4), but keyframe taifa-of-badajoz_1056 (1056-1065, 95,654 km2, bbox to 40.94 N) is 'ok' and still draws it; the note itself says 'the page's 1055 loss is not yet drawn here'. Evidence: shapes.csv taifa-of-badajoz_1056 95,653.7 km2 bbox -9.572,37.7707,-4.6379,40.9384; _1066 65,261.2 km2 to 39.967 N. Brief check 4. Fix: Mark taifa-of-badajoz_1056 'adjust' with the whole corrected shape: {"union": [{"intersect": [{"cliopatria": "Taifa of Badajoz", "year": 1056}, {"cliopatria": "Taifa of Badajoz", "year": 1066}]}, {"place": "Coimbra", "km": 40, "country": "Portugal"}], "text": "the taifa after the 1055 losses, still holding Coimbra until 1064"}.
- `/ledger/4/region` (not applied) [blocking] Coimbra is lost twice: the 1055 region (1055 shape minus 1066 shape) contains Coimbra (40.21 N), which /ledger/7 loses again in July 1064 after the siege. Evidence: https://en.wikipedia.org/wiki/Taifa_of_Badajoz: '... losing significant parts of its territory south of the Mondego River (south of Coimbra)' (no city named); Siege of Coimbra (1064): Ferdinand 'entered the city on 9 July 1064'. Fix: Region of /ledger/4: {"minus": [{"minus": [{"cliopatria": "Taifa of Badajoz", "year": 1055}, {"cliopatria": "Taifa of Badajoz", "year": 1066}]}, {"place": "Coimbra", "km": 40, "country": "Portugal"}], "text": ...}. The Ferdinand I of León page may date the Lamego (1057) and Viseu (1058) conquests that make up this strip.

Thin (for a gap-filler):
- `/ledger/3` Lisbon retaken from Sabur's sons: page says only 'soon' (confidence 1). Try: https://en.wikipedia.org/wiki/Aftasid_dynasty
- `/keyframe_review/3-7` The Abbadid (Seville) conquests of Badajoz land and Cliopatria's changes of 1018, 1028, 1034 (+5,200 km2), 1040 (-6,100) and 1056 (-5,100) carry no events (thin by design within the 5-page budget); and the direction of the 1055 loss (page: 'south of the Mondego'). Try: https://en.wikipedia.org/wiki/Ferdinand_I_of_Le%C3%B3n

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Taifa_of_Badajoz: confirmed ('Sabur was succeeded in 1022 by his vizier, Abdallah ibn al-Aftas')
- `/ledger/4` https://en.wikipedia.org/wiki/Taifa_of_Badajoz: confirmed year and tribute ('In 1055 Badajoz became a tributary of the Kingdom of León-Castile'); land is the author's reading, confidence 2 honest
- `/ledger/8` https://en.wikipedia.org/wiki/Taifa_of_Badajoz: confirmed ('In 1094 the Almoravids occupied Badajoz')
- `/ledger/10` https://en.wikipedia.org/wiki/Taifa_of_Badajoz: confirmed (second taifa 1144-1150; infobox 'Conquered by the Almohads: 1150')

## taifa-of-denia: FAIL

Area: the infobox gives no area; the keyframe notes say so (Cliopatria max 48074.0 km2).

Findings:
- `/ledger/2-3` (not applied) [blocking] The Sardinian occupation has a counterpart that no dossier can mirror and a region about five times what the page says: counterpart 'Sardinia (the Sardinian judicates)' is not a slug although the judicates have rows and will have dossiers (eu-13), and the region intersect(Dénia 1015, Sardinia) resolves to 83 cells, about 21,000 km2, 38.97-41.21 N, the whole island, while the page says 'a military camp in the north of the island for one year'. Evidence: https://en.wikipedia.org/wiki/Taifa_of_D%C3%A9nia: 'The taifa settled a military camp in the north of the island for one year.' Gazetteer: that intersect is 83 cells; Cliopatria's Giudicato of Logudoro (27 cells) and Gallura (14 cells) hold the north in 1014-1040. Keyframe 1 note wrongly says the shape includes only 'the north of Sardinia'. Fix: Region: {"intersect": [{"region": "Sardinia"}, {"union": [{"cliopatria": "Giudicato of Logudoro", "year": 1015}, {"cliopatria": "Giudicato of Gallura", "year": 1015}]}], "text": "a military camp in the north of the island"}; counterpart giudicato-of-logudoro (and a second occupation pair for giudicato-of-gallura, or name it in the note); fix the keyframe 1 note.
- `/ledger/2/confidence` (applied) Confidence 3 with a region the page does not name (whole island against 'the north of the island'). Evidence: https://en.wikipedia.org/wiki/Taifa_of_D%C3%A9nia: 'north of the island'. Fix: Lowered to 2 by the reviewer, note appended; re-validated 0 errors.
- `/ledger/11/confidence` (applied) Confidence 3 for the 1227 loss although the infobox names no land ('Remnants') and two other pages opened by the author put the conquest in 1244. Evidence: https://en.wikipedia.org/wiki/Taifa_of_D%C3%A9nia: infobox 'Remnants conquered by Aragon: 1227'; the dossier's own note: 'The Xàtiva page has the city captured only in 1244'. Fix: Lowered to 2 by the reviewer, note appended; re-validated 0 errors.
- `/ledger/1/counterpart` (not applied) [non-blocking] The Balearic Islands are gained from 'nobody', but they were a caliphal province: Cliopatria's Caliphate of Córdoba 1012 shape holds all 19 Balearic cells. Evidence: Gazetteer: intersect(Caliphate of Córdoba 1012, Balearic Islands) = 19 cells = the whole region. The page says the navy was used 'to take control of the Balearic Islands' in 1015. Fix: Counterpart caliphate-of-cordoba (the caliphate-of-cordoba dossier then needs a 1015 loss of the Balearic Islands to taifa-of-denia).
- `/ledger/4-5/region` (not applied) [non-blocking] Region is a 60 km radius round the city of Valencia, but the page says Mujahid captured 'the southern part' of the Valencia taifa. Evidence: https://en.wikipedia.org/wiki/Taifa_of_D%C3%A9nia: 'In the 1020s Mujāhid took advantage of the death of the regents of the taifa of Valencia to capture the southern part' (quoted in the event's own note). Fix: Draw the southern part of the Valencia taifa (for example the Xúquer valley round Alzira and Xàtiva, both in the gazetteer), not the city.
- `report counterparts_needing_dossiers` (not applied) [non-blocking] taifa-of-majorca is listed with years 1076-1203 but this dossier names it as a client from 1050 (/ledger/6). Evidence: /ledger/6 vassal_start 1050 counterpart taifa-of-majorca. Fix: List taifa-of-majorca from 1050 (as Dénia's client) or name the 1050-1075 client 'Balearic Islands (governor Ibn Aglab)'.

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Taifa_of_D%C3%A9nia: confirmed (1015, Balearic Islands; counterpart questioned)
- `/ledger/2` https://en.wikipedia.org/wiki/Taifa_of_D%C3%A9nia: confirmed year; region overstated (north of the island only); confidence lowered to 2
- `/ledger/9` https://en.wikipedia.org/wiki/Taifa_of_D%C3%A9nia: confirmed ('until the conquest by the taifa of Zaragoza in 1076'; infobox 1076-1081)
- `/ledger/8` https://en.wikipedia.org/wiki/Taifa_of_Majorca: confirmed ('The first taifa lasted for about 50 years (1076-1116)'; preceded by Taifa of Dénia; Ibn Aglab al-Murtada 1076-1093)
- `/ledger/11` https://en.wikipedia.org/wiki/Taifa_of_D%C3%A9nia: confirmed year on the infobox ('Remnants conquered by Aragon: 1227'); land not named; confidence lowered to 2

## Cross-dossier matrix

- county-of-osona 990 loss / county-of-berga -> no mirror: **exception**. county-of-berga is owned by another eu-12 part that has not run yet; it needs a 990 gain of the pagus of Berga (Berguedà) from county-of-osona.
- county-of-osona 1003 loss / County of Manresa -> no mirror: **exception**. Listed by the author as needing a dossier; confidence 1. The page has Manresa 'subsumed within Osona'; the reviewer doubts a separate Manresa dossier is needed (see notes).
- county-of-osona 1040 gain / County of Manresa -> no mirror: **exception**. As above, confidence 1.
- county-of-osona 1056 loss / County of Manresa -> no mirror: **exception**. As above, confidence 1.
- county-of-osona 1111 loss / county-of-barcelona -> no mirror: **exception**. county-of-barcelona not written yet (eu-12 part not run); it needs a 1111 gain of Osona. Also the 826/827 loss and 879 gain the reviewer asks for need nothing from neighbours (counterpart nobody / rebels).
- county-of-ampuria 817 merge / county-of-rosellon -> no mirror: **exception**. county-of-rosellon not written yet. Cliopatria's Rosellón starts in 896, so Empúries land 817-895 has no owner unless the county-of-rosellon dossier starts by 817 and merges Empúries then.
- county-of-ampuria 989 split / county-of-rosellon -> no mirror: **exception**. county-of-rosellon should record a split in 989 with counterpart county-of-ampuria and cut the Empúries cells from 989 (Cliopatria cuts them from 1000).
- county-of-ampuria 1003 gain / County of Peralada (Pedralbes) -> no mirror: **missing**. No such state on the page (Peralada was part of Empúries from 813); the reviewer asks for this event to be deleted rather than a dossier written.
- county-of-ampuria 1410 loss / crown-of-aragon -> no mirror: **exception**. crown-of-aragon not written yet; needs a 1410 gain of Empúries (escheat 1410-1436).
- taifa-of-alpuente 1106 loss / almoravid-dynasty -> no mirror: **missing**. almoravid-dynasty (af-02, written) has Valencia 1102 and Zaragoza 1110 but no gain of Alpuente; route to af-02: add a 1106 gain from taifa-of-alpuente (Taifa of Alpuente infobox 'Conquered by the Almoravids: 1106'; town page 1103).
- taifa-of-badajoz 1022 loss / Taifa of Lisbon (Banu Sabur) -> no mirror: **exception**. Listed in counterparts_needing_dossiers (taifa-of-lisbon, 1022).
- taifa-of-badajoz 1022 gain / Taifa of Lisbon (Banu Sabur) -> no mirror: **exception**. As above; confidence 1.
- taifa-of-badajoz 1055 loss / kingdom-of-leon -> no mirror: **exception**. kingdom-of-leon not written yet; needs the 1055 gain (minus the Coimbra district) and a vassal_start for taifa-of-badajoz in 1055.
- taifa-of-badajoz 1064 loss / kingdom-of-leon -> no mirror: **exception**. kingdom-of-leon not written yet; needs the July 1064 gain of Coimbra.
- taifa-of-badajoz 1094 loss / almoravid-dynasty -> almoravid-dynasty 1094 gain: **matched**. almoravid-dynasty /ledger/19.
- taifa-of-badajoz 1144 gain / almoravid-dynasty -> almoravid-dynasty 1145 loss: **matched**. almoravid-dynasty /ledger/31, within one year.
- taifa-of-badajoz 1150 loss / almohad-caliphate -> almohad-caliphate 1152 gain: **mismatch**. almohad-caliphate /ledger/12 is a confidence-1 bridge in 1152; the Taifa of Badajoz infobox says 'Conquered by the Almohads: 1150'. Route to af-02: move it to 1150.
- taifa-of-denia 1015 gain / nobody -> no mirror: **mismatch**. Should be caliphate-of-cordoba (Cliopatria's caliphate holds the Balearics in 1012); caliphate-of-cordoba (eu-12, not written) then needs a 1015 loss.
- taifa-of-denia 1015 occupation_start / Sardinia (the Sardinian judicates) -> no mirror: **missing**. Counterpart is not a slug; the judicates (eu-13, not run) need occupation_start/end 1015-1016 by taifa-of-denia in the north of the island.
- taifa-of-denia 1017 occupation_start / taifa-of-valencia -> no mirror: **exception**. taifa-of-valencia not written yet; needs occupation_start 1017 / occupation_end 1021 by taifa-of-denia of the southern part of the taifa.
- taifa-of-denia 1050 vassal_start / taifa-of-majorca -> no mirror: **exception**. taifa-of-majorca listed in counterparts_needing_dossiers (but with years from 1076).
- taifa-of-denia 1076 loss / taifa-of-majorca -> no mirror: **exception**. As above.
- taifa-of-denia 1076 loss / taifa-of-zaragoza -> no mirror: **exception**. taifa-of-zaragoza not written yet; needs a 1076 gain of the Dénia mainland (to 1081, then Tortosa 1081-1092 per the Dénia infobox).
- taifa-of-denia 1224 gain / almohad-caliphate -> no mirror: **missing**. almohad-caliphate (af-02) has no 1224 loss to taifa-of-denia (its Iberian end is the October 1228 loss to taifa-of-murcia). Route to af-02. Also almohad-caliphate /ledger/17, a confidence-1 1152 gain from taifa-of-denia, has no mirror: this dossier has no Dénia state 1077-1223 and marks Cliopatria's Dénia 1147-1151 shape wrong; that gain should name the holder of that land (taifa-of-murcia per the author's reading).
- taifa-of-denia 1227 loss / crown-of-aragon -> no mirror: **exception**. crown-of-aragon not written yet. Warn its author: the Dénia infobox says 1227 but the Xàtiva and Dénia town pages put the conquest in 1244; the land of Cliopatria's Dénia shapes 1147-1151 and 1236-1249 (marked wrong) has no owner in any dossier and must be claimed by taifa-of-murcia, crown-of-aragon or crown-of-castile.

## Problems

- No page failed for the reviewer. WebFetch returns a model summary, so quotes are the tool's fragments.
- The reviewer applied three small fixes in place (taifa-of-denia /ledger/2 and /ledger/11 confidence 3 to 2; county-of-osona /ledger/0 counterpart to nobody); both files re-validate with 0 errors.
- Four of five dossiers fail on unapplied blocking findings (Osona missing the 826-879 loss of the county; Empúries keyframe 1000 vs the 1003 Peralada gain; Badajoz keyframe 1056 vs the 1055 loss and Coimbra lost twice; Dénia's Sardinian occupation counterpart and region). Each fix is specific and short.
- af-02 routing: almoravid-dynasty lacks a 1106 gain of Alpuente; almohad-caliphate should move its taifa-of-badajoz gain from 1152 to 1150, add a 1224 loss to taifa-of-denia, and re-point its 1152 gain from taifa-of-denia.
- The author's counterparts County of Manresa, County of Girona and County of Peralada are not endorsed: Manresa and Peralada were parts of Osona and Empúries on the pages; Girona is Cliopatria's County of Barcelona row (Wikipedia title 'Girona').
