# Review of batch xx-01-a (Cultures 6000 to 3400 BCE, part a)

Reviewer: adversarial review, 2026-10-18. Machine copy: history/notes/phase-b/reviews/xx-01-a.json.

## Summary

| slug | verdict | blocking findings | reviewer-applied fixes |
| --- | --- | --- | --- |
| anatolian-neolithic | thin | 0 | 0 |
| atlantic-megalith-builders | thin | 0 | 0 |
| badarian-culture | pass | 0 | 0 |
| cardial-ware-culture | fix | 0 | 2 |
| cucuteni-trypillia-culture | thin | 0 | 0 |
| faiyum-merimde-neolithic | pass | 0 | 0 |
| funnelbeaker-culture | fix | 0 | 1 |
| ghassulian | fix | 0 | 1 |
| halaf-culture | thin | 0 | 0 |
| hassuna-culture | pass | 0 | 0 |
| lengyel-culture | fail | 1 | 0 |
| linear-pottery-culture | fail | 2 | 2 |
| maadi-culture | fix | 0 | 2 |
| naqada-culture | pass | 0 | 0 |
| pottery-neolithic-levant | thin | 0 | 0 |
| samarra-culture | pass | 0 | 0 |
| sredny-stog-culture | fix | 0 | 1 |
| starcevo-koros-cris-culture | thin | 0 | 0 |
| ubaid-period | fail | 3 | 0 |
| uruk-period | pass | 0 | 0 |
| vinca-culture | thin | 0 | 0 |
| yamnaya-culture | fail | 1 | 1 |

Mechanical checks: all 22 dossiers validate with 0 errors and resolve every region (one warning: yamnaya-culture's catacomb-culture counterpart has no dossier, listed). Years in order, found and dissolve at start and end, one soft certainty span per life, families in colours.json, no capitals or rulers. Every spot-checked event was read on its cited page; none was fabricated. The faults are in the geometry: keyframes that contradict their own ledger, and land drawn by two batch dossiers at once.

## Findings by dossier

### anatolian-neolithic: thin

- Thin, /ledger/2: Confidence-1 dissolve in 5000 BCE (Hacilar I 'dating after 5000 BC' is read as newcomers); Anatolia is blank from 5000 BCE because the Anatolian Chalcolithic has no dossier (try https://en.wikipedia.org/wiki/Prehistory_of_Anatolia)
- Spot checks: /ledger/0 confirmed (%C3%87atalh%C3%B6y%C3%BCk); /ledger/1 confirmed (%C3%87atalh%C3%B6y%C3%BCk); /ledger/1 confirmed (Hacilar); /ledger/2 confirmed (Hacilar).

### atlantic-megalith-builders: thin

- Thin, /ledger/3: Confidence-1 end in 3000 BCE is the dossier's choice; the Megalith page runs the tradition on (henges c. 3000 BC, Los Millares, 'c. 1200 BC: Last vestiges'), so Brittany, Ireland and Britain go blank from 3000 BCE (try https://en.wikipedia.org/wiki/Neolithic_British_Isles)
- Thin, /ledger/1/region: Alentejo is drawn from 4300 BCE; the page's 4300 entry names only Cadiz (Alberite), Evora's Zambujeiro is 'c. 4000 BC' and Almendres 'c. 6000 BC ... Possibly' (try https://en.wikipedia.org/wiki/Almendres_Cromlech)
- Spot checks: /ledger/0 confirmed (Megalith); /ledger/1 confirmed (Megalith); /ledger/2 confirmed (Megalith); /keyframe_review/0/correction confirmed (Megalith).

### badarian-culture: pass

- Spot checks: /ledger/0 confirmed (Badarian_culture); /ledger/1 confirmed (Badarian_culture); /keyframe_review/0/correction confirmed (Badarian_culture).
- Tried and could not break: years, hand-over to Naqada (44/54 cells inside naqada-culture_-4000), region against the page.

### cardial-ware-culture: fix

- **/ledger/1/region, /keyframe_review/1/correction, /ledger/2/region** (applied by reviewer). Tangier (60 km) was drawn as Cardial from 5600 BCE, but the page dates the north-west African Neolithic after this dossier's 5500 BCE end. Evidence: Cardium pottery page: the earliest Neolithic remains in Northwest Africa 'had European Neolithic ancestry (c. 5400 BC)'; infobox 'c. 6400 BC - c. 5500 BC'. Fix: Removed {"place": "Tangier", "km": 60} from the three specs and the 'south to Morocco' clause from their text; reviewer note on /ledger/1.
- **/ledger/1/confidence** (applied by reviewer). The 5600 BCE western gain is at confidence 2 but its year is not on the page. Evidence: Page: 'identical to those for Iberia c. 5500 cal BC', spread '2,000 km ... in probably no more than 100-200 years'; no date for Provence or Languedoc; keyframe 1's note: '5600 BCE is this dossier's placement of its start'. Research brief: 1 when bridging a silence. Fix: Lowered to 1.
- Thin, /ledger/1: A dated arrival of the Cardial in Liguria, Provence and Languedoc (now confidence 1) (try https://en.wikipedia.org/wiki/Neolithic_Europe)
- Thin, /identity/end: The western Mediterranean Neolithic after 5500 BCE (Epicardial, Danilo, Stentinello, Chassey, Iberian Neolithic) has no dossier; blank until 4800 BCE (try https://en.wikipedia.org/wiki/Neolithic_Europe)
- Spot checks: /ledger/0 confirmed (Cardium_pottery); /ledger/1 confirmed (year is a placement; confidence lowered) (Cardium_pottery); /ledger/2 confirmed (Cardium_pottery).

### cucuteni-trypillia-culture: thin

- **/ledger/3/counterpart and /identity/successors** (advisory, for the author). The dissolve names yamnaya-culture as heir, but the Yamnaya dossier takes none of this land in 3000 BCE (it already draws Odessa and Kirovohrad from 3200, and the forest-steppe, Moldova and Romania go to nobody); identity.successors is empty and the note still says 'The Yamnaya has no dossier yet'. Evidence: Overlap computed with the gazetteer: 228 of 1,052 cells of cucuteni-trypillia-culture_-4100 lie in yamnaya-culture_-3200; the other 824 enter no keyframe in 3000 BCE. Cucuteni page: 'third wave of Kurgan expansion between 3000-2800 BC' (the proponents' view). Yamnaya page lists Cucuteni-Trypillia under 'Preceded by'. Fix: Once yamnaya-culture carries the 3000 BCE gain of Odessa and Kirovohrad (see its finding), add {"slug": "yamnaya-culture", "land": Odessa + Kirovohrad} to successors and drop the stale sentence; the rest of the land goes to nobody.
- Thin, /ledger/0: Confidence-1 found (counterpart LBK from the LBK page's successor list); start 4800 (infobox) vs 5050 (lead) vs 5800 (chart) (try https://en.wikipedia.org/wiki/Bug-Dniester_culture)
- Spot checks: /ledger/0 confirmed (Cucuteni%E2%80%93Trypillia_culture); /ledger/1 confirmed (Cucuteni%E2%80%93Trypillia_culture); /ledger/2 confirmed (Cucuteni%E2%80%93Trypillia_culture); /ledger/3 confirmed (Cucuteni%E2%80%93Trypillia_culture).
- Area: page 350,000 km2, drawn about 266,050 km2, ratio 0.76, acknowledged.

### faiyum-merimde-neolithic: pass

- **/identity/wikipedia** (advisory, for the author). identity.wikipedia is 'Prehistoric Egypt', which is not among the sources; the batch notes attribute 'Merimde 5000-4200' to the Prehistoric Egypt page, but the cited sentence is on the Faiyum A culture page. Evidence: Faiyum A culture page: 'From about 5000 to 4200 BC the Merimde culture, so far only known from Merimde Beni Salama ... flourished in Lower Egypt.' Fix: Either set identity.wikipedia to 'Faiyum A culture' or add the Prehistoric Egypt page to sources; correct the notes file's attribution.
- Spot checks: /ledger/0 confirmed (Faiyum_A_culture); /ledger/1 confirmed (Faiyum_A_culture); /ledger/1 confirmed (Merimde_culture); /ledger/3 confirmed (Merimde_culture).

### funnelbeaker-culture: fix

- **/ledger/1/confidence** (applied by reviewer). The 3300 BCE loss of the eastern and southern groups (about 487,000 km2, the largest move in the batch) is at confidence 2 but its year is a placement. Evidence: Funnelbeaker page: replaced 'gradually' 'From the middle of the 4th millennium BCE', eastern and southern groups replaced 'in the late 4th millennium BCE'; 3300 BCE is used on the page only for copper decline and oil plants. The dossier's own notes: 'the 3300 BCE contraction is a placement'. Fix: Lowered to 1 with a reviewer note.
- Thin, /ledger/1: A dated replacement of the TRB by the Globular Amphora culture in Poland, Bohemia and central Germany (try https://en.wikipedia.org/wiki/Globular_Amphora_culture)
- Spot checks: /ledger/0 confirmed (Funnelbeaker_culture); /ledger/1 confirmed (year is a placement; confidence lowered) (Funnelbeaker_culture); /ledger/2 confirmed (Funnelbeaker_culture).

### ghassulian: fix

- **/ledger/1/note and /notes** (applied by reviewer). The page's lead ends the culture c. 3500 BC against the infobox's 3800 BC; the dossier did not flag it. Evidence: Ghassulian page: infobox 'c. 4400-3800 BC'; lead 'c. 4400 - c. 3500 BC'; body 'ended ca. 3800 BC'. Fix: Added the disagreement to the dissolve note and the notes field; 3800 kept.
- Spot checks: /ledger/0 confirmed (Ghassulian); /ledger/1 confirmed (Ghassulian).

### halaf-culture: thin

- Thin, /ledger/3: Confidence-1 year for the Halaf on the Tigris piedmont (Arpachiyah, Nineveh, Tepe Gawra undated on the page; the year is the end of the Tell Hassuna layers) (try https://en.wikipedia.org/wiki/Tell_Arpachiyah)
- Spot checks: /ledger/0 confirmed (Halaf_culture); /ledger/1 confirmed (Domuztepe); /ledger/2 confirmed (Halaf_culture); /ledger/3 confirmed (Halaf_culture); /ledger/4 confirmed (Halaf_culture).
- Tried and could not break: the 5300-5100 overlap with the northern Ubaid is the Ubaid's mismatch (its gain predates this dossier's page-backed 5100 end); see ubaid-period.

### hassuna-culture: pass

- Spot checks: /ledger/0 confirmed (Hassuna_culture); /ledger/0 confirmed (Tell_Hassuna); /ledger/1 confirmed (Tell_Hassuna).
- Tried and could not break: hand-over to Halaf (matched 5350); the Samarra overlap at As Sulaymaniyah is flagged and page-backed (both pages list Tell Shemshara).

### lengyel-culture: fail

- **/keyframe_review/0/correction** (BLOCKING, for the author). Keyframe 0 draws Bohemia (233 cells), Kuyavian-Pomeranian (78) and Greater Poland (126) as Lengyel from 5000 BCE, while linear-pottery-culture_-5000 and _-4800 (the Stroked Pottery phase) hold the same land to 4500 BCE: about 110,000 km2 drawn by both for 500 years, unflagged. Evidence: Lengyel page: 'Also closely related are the Stroke-ornamented ware and Rossen cultures, adjacent to the north and west, respectively'; Bohemia appears only for the end: 'ending with phase IV, e.g., in Bohemia represented by the Jordanow/Jordansmuhler culture'; Poland is undated (captions at 4100 BC and c. 4000 BC). LBK page: 'Stroked Pottery culture (Stichbandkeramik (SBK), 5000-4500 BC) evolved in central Europe'. Fix: Remove Bohemia, Kuyavian-Pomeranian and Greater Poland from keyframe 0 (its spec is the shape at 5000 BCE); add a gain in -4500 from linear-pottery-culture, confidence 1, 'page silent', for those three, so /ledger/1 can still pass them to the Funnelbeaker in 4100. Keep Moravia (Austrian/Moravian Painted Ware) from 5000; the LBK must drop it (its finding).
- **/ledger/1** (advisory, for the author). Bohemia passes to the Funnelbeaker in 4100 BCE although the page has Lengyel phase IV in Bohemia (Jordanow) to the culture's 4000 BC end. Evidence: 'It flourished from 5000 to 4000 BC, ending with phase IV, e.g., in Bohemia represented by the Jordanow/Jordansmuhler culture.' Fix: Consider keeping Bohemia to the 4000 BCE dissolve and handing only Kuyavia and Greater Poland over in 4100.
- Thin, /keyframe_review/0/correction: Slavonia (46 cells) is drawn but the page names Croatia only for Sopot finds; Lengyel pottery is listed for 'western Hungary, the Czech Republic, Slovakia, Austria, Poland, and Slovenia' (try https://en.wikipedia.org/wiki/Sopot_culture)
- Spot checks: /ledger/0 confirmed (Lengyel_culture); /ledger/1 confirmed (Lengyel_culture); /ledger/2 confirmed (Lengyel_culture); /keyframe_review/0/correction not on page (Lengyel_culture).

### linear-pottery-culture: fail

- **/ledger/1/confidence** (applied by reviewer). The 5300 BCE spread down the Rhine, Elbe, Oder and Vistula is at confidence 2 but the year is a placement. Evidence: The note: 'the year is the midpoint of that spread' ('1,500 km ... in 360 years'); research brief: 1 when bridging a silence. Fix: Lowered to 1.
- **/ledger/2/confidence** (applied by reviewer). Confidence 3 for a 5300 BCE event whose page year is 5330. Evidence: LBK page: 'At around 5330 BC, the classical Alfold culture of the LBK appeared to the north of the Koros culture'; the note itself opens '5330 BCE'. 5300 is the rounded hand-over year matching the Starcevo's Koros end. Fix: Lowered to 2.
- **/keyframe_review/3/correction (and /keyframe_review/4/correction, /ledger/9/region)** (BLOCKING, for the author). {"country": "Czechia"} keeps Moravia (Jihomoravsky, Zlinsky, Olomoucky, Moravskoslezsky: 90 cells) to 4500 BCE, although /ledger/6 hands it to the Lengyel in 5000 BCE and lengyel-culture_-5000 draws it. Evidence: Gazetteer: 90 of the 418 cells of /ledger/6 remain in linear-pottery-culture_-5000; Lengyel page: 'Austrian/Moravian Painted Ware I and II' subgroups. Fix: Subtract the four Moravian units from keyframes 3 and 4 (e.g. {"minus": [..., {"union": [the four admin1]}]}) and from the dissolve region.
- **/keyframe_review/3/correction** (BLOCKING, for the author). Keyframe 3 (from 5000 BCE) already lacks the Alfold (195 cells), but /ledger/7 dates its loss 4940 BCE at confidence 3. Evidence: LBK page: the Alfold culture 'flourished until about 4940'; gazetteer: 0 of the 195 cells of /ledger/7 are in linear-pottery-culture_-5000, all 195 in _-5200. Fix: A keyframe spec is the shape at its first year: add the Alfold admin-1 units of /ledger/2 back to keyframe 3 so /ledger/7 removes them in 4940 (or split keyframe 3 at 4940).
- **/ledger/8** (advisory, for the author). The Dniester loss names Cucuteni-Trypillia for 722 cells, but cucuteni-trypillia-culture_-4800 holds only 407 of them; L'viv, Ivano-Frankivs'k and the rest go to nobody. Evidence: Gazetteer intersection of /ledger/8/region with the Cucuteni keyframe 0. Fix: Split the event: the Cucuteni part with that counterpart, the rest with counterpart nobody (both confidence 1).
- Thin, /ledger/1: Dated arrival on the Rhine, Elbe, Oder and Vistula (now confidence 1) (try https://en.wikipedia.org/wiki/Linear_Pottery_culture)
- Thin, /ledger/4: Confidence-1 eastern extension to the Dniester and Moldova (try https://en.wikipedia.org/wiki/Bug-Dniester_culture)
- Thin, /ledger/8: Confidence-1 end of the eastern LBK ('The end of the Eastern Linear Pottery culture and the LBK is less certain') (try https://en.wikipedia.org/wiki/Cucuteni%E2%80%93Trypillia_culture)
- Spot checks: /ledger/0 confirmed (Linear_Pottery_culture); /ledger/1 confirmed (year is a placement; confidence lowered) (Linear_Pottery_culture); /ledger/2 mis-dated (5330 on the page; confidence lowered to 2) (Linear_Pottery_culture); /ledger/3 confirmed (Linear_Pottery_culture); /ledger/5 confirmed (Linear_Pottery_culture); /ledger/7 confirmed (Linear_Pottery_culture); /ledger/9 confirmed (Linear_Pottery_culture).

### maadi-culture: fix

- **/ledger/1/confidence** (applied by reviewer). Confidence 3 with a region the page does not name: the dissolve region adds the Fayyum, which the page names only as the Maadian's Neolithic origin. Evidence: Maadi page: 'The cultures of Lower Egypt were replaced by Upper Egypt and Naqada culture by the end of Naqada II circa 3200 BCE'; it 'emerged from the earliest Neolithic sites of the Nile Valley, in the Faiyum region and at Merimda Beni Salama and el-Omari'; the word Delta does not appear. Fix: Lowered to 2.
- **/ledger/0/confidence** (applied by reviewer). The 3800 BCE start is at confidence 2 but the year is the midpoint of Naqada I, not a page year. Evidence: Maadi page: 'first identified during the second part of Naqada I'; Naqada page 'about 3900-3650 BC'; the note: 'the year is the midpoint of that phase'. Fix: Lowered to 1.
- Thin, /ledger/0: A dated start of the Maadi-Buto culture (now confidence 1); Lower Egypt is blank 4200..3800 BCE (try https://en.wikipedia.org/wiki/Buto)
- Spot checks: /ledger/0 confirmed (year is a midpoint; confidence lowered) (Maadi_culture); /ledger/1 confirmed (Maadi_culture).

### naqada-culture: pass

- Spot checks: /ledger/0 confirmed (Naqada_culture); /ledger/1 confirmed (Naqada_culture); /ledger/2 confirmed (Naqada_culture); /ledger/3 confirmed (Maadi_culture); /ledger/4 confirmed (Naqada_culture).
- Tried and could not break: keyframe 1 adds 803 cells against the 808-cell Maadi gain (consistent); the hand-over counterpart early-dynastic-period-of-egypt is owned by me-03, not yet run.

### pottery-neolithic-levant: thin

- Thin, /ledger/2: Confidence-1 dissolve in 4400 BCE bridging Wadi Rabah's 4500 end and the Ghassulian's 4400 start (try https://en.wikipedia.org/wiki/Tel_Tsaf)
- Thin, /keyframe_review/0: The Yarmukian (infobox 6400-6000 BC) is carried to 5500 BCE; the Lodian/Jericho IX and Nizzanim of 6000-5500 are undated on both pages (try https://en.wikipedia.org/wiki/Prehistory_of_the_Levant)
- Spot checks: /ledger/0 confirmed (Yarmukian_culture); /ledger/1 confirmed (Wadi_Rabah_culture); /ledger/2 confirmed (Wadi_Rabah_culture); /keyframe_review/1/correction confirmed (Wadi_Rabah_culture).

### samarra-culture: pass

- Spot checks: /ledger/0 confirmed (Samarra_culture); /ledger/1 confirmed (Samarra_culture); /keyframe_review/0/correction confirmed (Samarra_culture).
- Tried and could not break: the 500-year overlap with ubaid-period_-5300 is the Ubaid's fault (finding there); the Hassuna overlap is flagged and page-backed.

### sredny-stog-culture: fix

- **/ledger/1/counterpart** (applied by reviewer). The 3500 BCE dissolve named yamnaya-culture as heir, but the Yamnaya dossier starts in 3400 on the Don-Volga and reaches the Dnieper only in 3200, so no dossier takes this land 3500..3201 BCE. Evidence: Yamnaya page: Anthony 'suggested that the Yamnaya culture (3300-2600 BC) originated in the Don-Volga area at c. 3400 BC'; 'the early Yamnaya horizon spread quickly across the Pontic-Caspian steppes between c. 3400 and 3200 BC'; the Sredny Stog page's 'when the Yamnaya culture expanded westward replacing Sredny Stog' is kept in the note. Fix: Counterpart set to nobody (the author's own second option), stale 'no dossier yet' sentence removed, reviewer note added. Mykhailivka (3600-3000) or Repin would be the heirs when written.
- Thin, /keyframe_review/0/correction: The page extends the culture 'to the delta of the Danube River' in the west; Mykolaiv and Odessa are not drawn (try https://en.wikipedia.org/wiki/Sredny_Stog_culture)
- Spot checks: /ledger/0 confirmed (Sredny_Stog_culture); /ledger/1 confirmed (Sredny_Stog_culture).

### starcevo-koros-cris-culture: thin

- **/ledger/1/region** (advisory, for the author). The 5400 BCE loss to the Vinca names 434 cells, 123 of which keyframe 1 (5400-5300) still draws as Starcevo (the Belgrade 150 km and Timisoara/Deva circles reach into the Szeged and Tuzla circles). Evidence: Gazetteer: /ledger/1 region against starcevo-koros-cris-culture_-5400 = 123/434 cells. Fix: Write the loss as {"minus": [keyframe 0 spec, keyframe 1 spec]} so the ledger loses only what the keyframe drops.
- Thin, /ledger/3: Confidence-1 dissolve of the north-west Balkans in 5300 BCE; the Starcevo proper runs 'between c. 5500 and 4500 BCE' (infobox to c. 4500 BCE) and the late Starcevo is undrawn (try https://en.wikipedia.org/wiki/Star%C4%8Devo_culture)
- Spot checks: /ledger/0 confirmed (Star%C4%8Devo%E2%80%93K%C3%B6r%C3%B6s%E2%80%93Cri%C8%99_culture); /ledger/1 confirmed (Vin%C4%8Da_culture); /ledger/2 confirmed (Star%C4%8Devo%E2%80%93K%C3%B6r%C3%B6s%E2%80%93Cri%C8%99_culture); /ledger/3 confirmed (Star%C4%8Devo%E2%80%93K%C3%B6r%C3%B6s%E2%80%93Cri%C8%99_culture).

### ubaid-period: fail

- **/keyframe_review/3/correction** (BLOCKING, for the author). Keyframe 3 drops the Gulf coast (Kuwait City 80 km, Al Jubayl 100 km: 115 cells, about 29,000 km2) in 4300 BCE with no ledger event. Evidence: Gazetteer: _-5300 to _-4300 removes 1,039 cells, /ledger/4 explains 924. Ubaid page: Gulf Ubaid pottery 'reaching a peak around 5300 BC and continuing into the fifth millennium' (no end date). Fix: Add a loss of the two Gulf radii to nobody in the year chosen (confidence 1, page silent on the end), or keep them in keyframe 3 to the 4000 BCE dissolve.
- **/keyframe_review/2/correction** (BLOCKING, for the author). Keyframe 2 (from 5300) already draws 117 of the 148 cells of the 4800 BCE Samarra gain (/ledger/3) while samarra-culture holds them to 4800 (131-cell overlap for 500 years), and the other 31 cells of the gain never enter a keyframe. Evidence: Gazetteer: /ledger/3 against ubaid-period_-5300 = 117/148, against _-4300 = 0; samarra-culture_-5500 x ubaid-period_-5300 = 131 cells over 5300..4800. Samarra page: 'roughly dated to between 5500 and 4800 BCE'. Fix: Keyframe 2's spec is the shape at 5300 BCE: subtract {"place": "Samarra", "km": 110} from it, let /ledger/3 add it in 4800, and keep it in keyframe 3 if the middle Tigris stays Ubaid after 4300 (else add a loss).
- **/ledger/2** (BLOCKING, for the author). The north is gained from halaf-culture in 5300 BCE, but halaf-culture dissolves in 5100 BCE: 473 cells drawn by both for 200 years (rule 3 mismatch; flagged as the transitional period, not resolved). Evidence: Halaf page infobox 'c. 6,100-5,100 BC'; Ubaid page phase table: Ubaid 2 'Halaf-Ubaid Transitional 5200-5100' and Ubaid 3 'Northern Ubaid 5100-4900' after Pournelle 2003 (5200-4600 after Harris 2021), against the text's 'about 5300 to 4300 BC'. Fix: Move /ledger/2 to -5100 citing the phase table (Pournelle), with keyframe 1 to -5101 and keyframe 2 from -5100 (shape_id ubaid-period_-5100), so it mirrors the Halaf dissolve.
- Thin, /ledger/3: Confidence-1 Ubaid on the middle Tigris (year is the Samarra page's end) (try https://en.wikipedia.org/wiki/Tell_es-Sawwan)
- Thin, /ledger/5: Confidence-1 terminal Ubaid in Susiana (try https://en.wikipedia.org/wiki/Susa)
- Spot checks: /ledger/0 confirmed (Ubaid_period); /ledger/1 confirmed (Ubaid_period); /ledger/2 confirmed (Ubaid_period); /ledger/4 confirmed (Ubaid_period); /ledger/5 confirmed (Ubaid_period).

### uruk-period: pass

- **/ledger/4** (advisory, for the author). Khuzestan (262 cells) is handed to elam in 3200 BCE, but elam's 3200 found draws only Susa 40 km (no counterpart, no predecessor) and gains Khuzestan in 2700 from nobody. Evidence: elam.json /ledger/0 (-3200, found, {place: Susa, km: 40}) and /ledger/1 (-2700 gain Khuzestan, nobody). Fix: Route to me-01: elam's found should name uruk-period as counterpart and predecessor; either Elam takes Khuzestan in 3200 or this event narrows to Susa and the rest goes to nobody. Not a fault of this dossier's sources (the year is Cliopatria's, confidence 1).
- Spot checks: /ledger/0 confirmed (Uruk_period); /ledger/1 confirmed (Uruk_period); /ledger/2 confirmed (Uruk_period); /ledger/3 confirmed (Uruk_period); /ledger/5 confirmed (Uruk_period).
- Tried and could not break: keyframe deltas all explained (+221, +70, -736 against events of 221, 70, 736 cells).

### vinca-culture: thin

- Thin, /keyframe_review/0/correction: The page names 'western-central Romania (Oltenia and Transylvania)', eastern Croatia and northern Montenegro; Oltenia, eastern Croatia and Montenegro are not drawn (try https://en.wikipedia.org/wiki/Vin%C4%8Da_culture)
- Spot checks: /ledger/0 confirmed (Vin%C4%8Da_culture); /ledger/1 confirmed (Vin%C4%8Da_culture); /ledger/2 confirmed (Vin%C4%8Da_culture).

### yamnaya-culture: fail

- **/ledger/0/confidence** (applied by reviewer). Confidence 3 for a start the page dates two ways and a region the page does not name. Evidence: Yamnaya page: infobox 'c. 3300-2600 BC' against Anthony's 'originated in the Don-Volga area at c. 3400 BC'; Rostov, Volgograd and Kalmykia stand in for the 'Don-Volga area' (the dossier's own notes). Fix: Lowered to 2.
- **/keyframe_review/1/correction and /ledger/1/region** (BLOCKING, for the author). The 'Pontic Steppe' region takes the Odessa and Kirovohrad oblasts (228 cells, about 58,000 km2) in 3200 BCE, while cucuteni-trypillia-culture holds them to its 3000 BCE dissolve (which names this dossier as heir): both draw them 3200..3000, unflagged, and no 3000 BCE gain mirrors the Cucuteni hand-over. Evidence: Gazetteer: cucuteni-trypillia-culture_-4100 x yamnaya-culture_-3200 = 228 cells (Kirovohrad 96, Odessa 132) over 3200..3000. Cucuteni page: infobox 'c. 4800 to 3000 BC', 'third wave of Kurgan expansion between 3000-2800 BC'. Yamnaya page infobox lists Cucuteni-Trypillia under 'Preceded by'. Fix: Subtract {"admin1": "Odessa", "country": "Ukraine"} and {"admin1": "Kirovohrad", "country": "Ukraine"} from keyframe 1 and /ledger/1; add a gain in -3000 from cucuteni-trypillia-culture for the two (confidence 2, Cucuteni page); add cucuteni-trypillia-culture to identity.predecessors with that land.
- Spot checks: /ledger/0 confirmed (confidence lowered to 2) (Yamnaya_culture); /ledger/1 confirmed (Yamnaya_culture); /ledger/2 confirmed (Yamnaya_culture).

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| hassuna-culture -5350 dissolve (halaf-culture) | halaf-culture -5350 gain | matched | Mosul 100 km; 125 of Hassuna's 277 cells pass to the Halaf, the As Sulaymaniyah circle stays with the Samarra |
| samarra-culture -5500 found (nobody) | hassuna-culture -5350 dissolve | exception | Overlap of 101 cells (As Sulaymaniyah circle) 5500..5350, flagged in hassuna-culture's notes; both culture pages list Tell Shemshara, so co-presence is page-backed |
| halaf-culture -5450 loss (nobody) | - | exception | counterpart nobody (Domuztepe abandoned) |
| ubaid-period -5300 gain (halaf-culture) | halaf-culture -5100 dissolve | mismatch | 200 years apart; 473 cells drawn by both 5300..5100 (finding on ubaid-period /ledger/2) |
| ubaid-period -4800 gain (samarra-culture) | samarra-culture -4800 dissolve | mismatch | Years match but ubaid-period_-5300 already draws 117 of the 148 cells from 5300 (131-cell overlap with samarra-culture 5300..4800); 31 cells never drawn (finding on ubaid-period) |
| ubaid-period -5500 gain (nobody) | - | exception | counterpart nobody |
| ubaid-period -4300 loss (nobody) | - | exception | counterpart nobody; northern Late Chalcolithic listed under counterparts_needing_dossiers |
| ubaid-period -4300 gain (nobody) | - | exception | counterpart nobody (Susiana) |
| ubaid-period -4000 dissolve (uruk-period) | uruk-period -4000 found | matched | 998/998 cells |
| uruk-period -3800 gain (nobody) | - | exception | counterpart nobody |
| uruk-period -3500 gain (nobody) | - | exception | counterpart nobody |
| uruk-period -3400 loss (sumerian-city-states) | sumerian-city-states -3400 found | mismatch | Year matches; sumerian-city-states (me-01) has no counterpart on its found and no predecessor: it should name uruk-period |
| uruk-period -3200 loss (elam) | elam -3200 found | mismatch | Year matches; elam (me-01) takes only Susa 40 km in 3200 and Khuzestan from nobody in 2700, with no counterpart or predecessor: land disagrees (262 cells vs Susa) |
| pottery-neolithic-levant -4400 dissolve (ghassulian) | ghassulian -4400 found | matched | 103/107 cells |
| badarian-culture -4000 dissolve (naqada-culture) | naqada-culture -4000 found | matched | 44/54 cells (desert edge of the Asyut radius dropped) |
| maadi-culture -3200 dissolve (naqada-culture) | naqada-culture -3200 gain | matched | 808/808 cells |
| naqada-culture -3000 dissolve (early-dynastic-period-of-egypt) | - | exception | counterpart owned by me-03, not yet run |
| faiyum-merimde-neolithic -5000 gain (nobody) | - | exception | counterpart nobody |
| faiyum-merimde-neolithic -4400 loss (nobody) | - | exception | counterpart nobody |
| starcevo-koros-cris-culture -5400 loss (vinca-culture) | vinca-culture -5400 found | matched | 383/434 cells; the Vinca's Csongrad also overlaps Starcevo keyframe 1 (148 cells, 5400..5300), flagged by the author |
| starcevo-koros-cris-culture -5300 loss (linear-pottery-culture) | linear-pottery-culture -5300 gain | matched | 83/173 cells (the rest of the Szeged radius is Vinca land) |
| linear-pottery-culture -5300 gain (nobody) | - | exception | counterpart nobody |
| linear-pottery-culture -5200 gain (nobody) | - | exception | counterpart nobody (two events: Paris Basin and Netherlands; Dniester) |
| linear-pottery-culture -5000 loss (lengyel-culture) | lengyel-culture -5000 found | mismatch | Year and region match (418/418 in lengyel-culture_-5000), but the LBK keyframe keeps Moravia (90 cells), and the Lengyel also draws Bohemia, Kuyavia and Greater Poland that the LBK keeps to 4500: 527 cells drawn by both 5000..4500 (findings on both) |
| linear-pottery-culture -4940 loss (nobody) | - | exception | counterpart nobody (Tisza culture listed under counterparts_needing_dossiers) |
| linear-pottery-culture -4800 loss (cucuteni-trypillia-culture) | cucuteni-trypillia-culture -4800 found | mismatch | Year matches; only 407 of the 722 cells lie in cucuteni-trypillia-culture_-4800 (land disagrees) |
| lengyel-culture -4100 loss (funnelbeaker-culture) | funnelbeaker-culture -4100 found | matched | 437/437 cells inside funnelbeaker-culture_-4100 (its found names nobody, acceptable for a multi-source found) |
| funnelbeaker-culture -3300 loss (nobody) | - | exception | counterpart nobody (Globular Amphora listed under counterparts_needing_dossiers) |
| cardial-ware-culture -5600 gain (nobody) | - | exception | counterpart nobody |
| atlantic-megalith-builders -4300 gain (nobody) | - | exception | counterpart nobody |
| atlantic-megalith-builders -3700 gain (nobody) | - | exception | counterpart nobody |
| cucuteni-trypillia-culture -4100 gain (nobody) | - | exception | counterpart nobody (12 cells overlap sredny-stog-culture, negligible) |
| cucuteni-trypillia-culture -3000 dissolve (yamnaya-culture) | yamnaya-culture -3200 gain | mismatch | yamnaya-culture takes Odessa and Kirovohrad (228 cells) in 3200 from nobody, 200 years before this hand-over, and nothing in 3000; the other 824 Cucuteni cells go to nobody (finding on yamnaya-culture) |
| sredny-stog-culture -3500 dissolve (nobody (was yamnaya-culture)) | yamnaya-culture -3400 found | exception | Fixed by the reviewer: counterpart set to nobody; the Yamnaya starts on the Don-Volga in 3400 and reaches the Dnieper in 3200, so the Dnieper steppe is nobody's 3500..3201 (flagged by the author) |
| yamnaya-culture -3200 gain (nobody) | - | mismatch | Counterpart nobody, but 228 of the cells are cucuteni-trypillia-culture's until 3000 (see above) |
| yamnaya-culture -2600 dissolve (catacomb-culture) | - | exception | catacomb-culture and poltavka-culture have no dossier; listed under counterparts_needing_dossiers |

## Problems

- No page failed to load (27 WebFetch reads of the authors' own sources). Culture pages carry no infobox areas, so area_check is empty except for Cucuteni-Trypillia (350,000 km2 on the page, ratio 0.76, acknowledged).
- Per the orchestrator's adjustment (it overrides section 5 of the reviewer brief), the reviewer applied 10 small verified fixes in 7 dossiers: confidence levels in linear-pottery-culture (/ledger/1, /ledger/2), yamnaya-culture (/ledger/0), maadi-culture (/ledger/0, /ledger/1), funnelbeaker-culture (/ledger/1), cardial-ware-culture (/ledger/1); Tangier removed from cardial-ware-culture; a note on the lead's 3500 BC end in ghassulian; sredny-stog-culture's dissolve counterpart set to nobody. All 7 re-validate with 0 errors (yamnaya keeps its one catacomb-culture warning); originals kept in /tmp/claude-0/work/review-xx-01-a/backup/.
- Overlaps inside the batch were measured with tools/gazetteer.py on the keyframe specs (H3 r5 cells, about 252.9 km2 each); hand-over years where both sides include the same year were ignored.
- Mismatches against me-01 dossiers (sumerian-city-states, elam) need routing to me-01: neither names uruk-period as counterpart or predecessor, and elam takes only Susa in 3200 BCE.
- yamnaya-culture (3400-2600 BCE) lies after this group's 3400 BCE horizon; reassign it if a later steppe group owns that period (author's note).
