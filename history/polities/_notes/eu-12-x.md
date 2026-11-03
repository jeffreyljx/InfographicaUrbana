# eu-12-x notes (Iberia and the taifas, additions batch)

Written 2026-10-25. Eleven new dossiers for states Cliopatria lacks (all `cliopatria_names: []`, every keyframe new with verdict `adjust`), and two dossiers from eu-12-a kept unchanged (banu-qasi, rebellion-of-umar-ibn-hafsun). All validate with 0 errors and 0 warnings. `--resolve` warnings remain only where the gazetteer lacks a real place name (lerida 20, albarracin 11, calatrava 17, mertola 12; the rest 0).

Each dossier's own `notes` field holds the page conflicts for that state; this file lists what the reviewer and the reconciler must act on.

## Read first: double-bookings and counterpart-string mismatches

1. gibraltar vs kingdom-of-spain / kingdom-of-great-britain. Both of those dossiers book Gibraltar and Menorca as a Spain loss and a British gain on 13 July 1713 and nothing for 1704-1713. The Gibraltar dossier starts at the 1704 capture, draws 1704-1713 as contested and as a colony tint, and so duplicates the 6.8 km2 the Great Britain dossier draws as direct land. Choose: keep gibraltar (type colony) and delete the Gibraltar part of the British gain, or drop gibraltar. The end year 2026 is the current year; its final vassal_end and dissolve events (confidence 1) exist only to satisfy the validator.
2. bonapartist-spain vs first-french-empire. The kingdom-of-spain dossier books the 1808, 1810, 1812 and 1813 changes with first-french-empire as counterpart; bonapartist-spain books the same land to Joseph's client kingdom with kingdom-of-spain as counterpart and first-french-empire as suzerain (vassal tint). Replace first-french-empire by bonapartist-spain in those four Spanish events (military governments stay French). 1808-1813 is outside the group's era to 1789; written because eu-12-m asked for it.
3. banu-marwan-of-badajoz. The caliphate-of-cordoba dossier uses the counterpart string "Ibn Marwan of Badajoz" for its 930 gain; map it to banu-marwan-of-badajoz. The emirate-of-cordoba dossier has no matching 875 loss (not checked). The taifa-of-badajoz dossier starts 1009 although the Badajoz page says 1021 or 1031.
4. fihrid-governors-of-al-andalus. The umayyad-caliphate (750 loss) and emirate-of-cordoba (756 founding, 757 gain) dossiers use the string "Fihrid governors of al-Andalus". The 757 gain should be split (south 756, centre and north 779-783) in line with the Abd al-Rahman I page.
5. jahwarid-taifa-of-cordoba. Cliopatria's taifa-of-cordoba row is the later 1147-1249 state. The taifa-of-seville dossier books its 1070 gain with counterpart taifa-of-cordoba; map it to jahwarid-taifa-of-cordoba.
6. taifa-of-majorca vs almoravid-dynasty / almohad-caliphate. Those dossiers count the Banu Ghaniya's Balearics as theirs throughout (1115, 1185, 1187, 1203). taifa-of-majorca books 1147-1185 and 1187-1203 as independent per the Taifa page; the Almoravid dossier should cede the islands in 1147. The crown-of-aragon dossier books the 1229 conquest from almohad-caliphate.
7. taifa-of-lerida. The taifa-of-zaragoza dossier already books the c. 1040 loss and the 1078-1081 contest with this slug. County-of-barcelona should carry the parias from 1045 and the 1149 Catalan capture (lerida ends in 1102 on the Lleida page; the Almoravids held it by walis to 1149).
8. lordship-of-albarracin. crown-of-aragon should carry the matching 1284 gain; kingdom-of-navarre is Cliopatria's 1139-1428 row (vassal relation 1167-1172).
9. spanish-march.json (795-897) exists from eu-07-x; it is not part of this batch. Check that it does not duplicate the Upper March material in banu-qasi.

## Per state: not settled

- taifa-of-malaga (1026-1239, four periods booked as loss/gain pairs): Zirid conquest 1056 or 1057; end 1238 or 1239; the 1035 Algeciras succession as annexation or division; Carmona conquest undated; Ceuta and Tangier not Malaga's on any page.
- taifa-of-lerida: no boundary on any page, so extents are readings (two 45 km circles); who held Lerida between the war's end and late 1081; Tujibid walis before 1039 (tujibids-of-zaragoza).
- taifa-of-majorca: start 1076 chosen (infobox says 1018); Sulayman's dates conflict between pages; the Banu Ghaniya's North African state (Bougie, Constantine, Algiers) needs an Africa-group dossier.
- gibraltar: Treaty text not opened; end of the 1704-05 siege and 1967/1969 events beyond one line not opened; British Menorca is the next candidate.
- lordship-of-albarracin: no town list on either page; end set to the 1284 conquest (a pretender survived to 1300); 1168 suggested by eu-12-g is on neither page.
- banu-marwan-of-badajoz: extent is a reading (Badajoz province and Portalegre district); Merida in 915 unknown; no ruler list opened.
- order-of-calatrava: Order typed a state; the rendering may prefer a vassal tint of the Crown of Castile. All three seats are drawn at Ciudad Real coordinates because Calatrava is not in the gazetteer. Santiago (undated acquisitions), Alcantara, Montesa, Avis/Christ, Templars and Hospitallers not written.
- taifa-of-mertola: founding 1031, 1033 or c. 1037; Seville conquest 1044 or 1044-45; Ibn Qasi dates differ; territory beyond the town unknown.
- bonapartist-spain: 1809 fronts, the extent of Joseph's authority in the Old Castile and Leon military zones, and the 1812 return to Madrid (confidence 1) not on the pages; Joseph's accession 15 June or 25 July 1808.
- fihrid-governors-of-al-andalus: Septimania part of the 751 shape; the Franks took it 759-760 per the Emirate dossier, not on the pages opened; Yusuf's death 759 or later; the rebellious lords of the Upper March 777-783 need a dossier.
- jahwarid-taifa-of-cordoba: end 1070 (text) or 1091 (infobox); territory beyond the city (the page says only 'Córdoba and its vicinity', so the extent is Cliopatria's 9,813 km2 shape, see Repairs); who held the Beja strip of Cliopatria's 1028-1033 shape from December 1031 to 1033; the Caliphate of Cordoba page returned a banner only.

## Gazetteer names needed

Lleida, Barbastro, Graus, Monzon, Almenar, Sarinena (taifa-of-lerida); Albarracin; Ciudad Real, Alcaniz, Monfragüe (order-of-calatrava); Mertola. (The kept banu-qasi note lists further names eu-12-a needed; its --resolve now shows 0 warnings.)

## Pages that failed

Ahmad_ibn_Qasi, Jahwarids, Ibrahim_ibn_Hajjaj, Emirate_of_Menorca (404); Balearic_Islands_expedition (disambiguation page; the 1113-1115 page was used); Caliphate_of_Córdoba (banner only).

## States not written

- Morisco rebels of the Alpujarras (1568-12 to 1571-03, type rebel, counterpart kingdom-of-spain): the Rebellion and Aben Humeya pages were opened, but the gazetteer lacks the Alpujarras, Béznar, Lecrín, Órgiva, Galera and Serón and the pages give no boundary; left for a later batch.
- Kingdom of Viguera (c. 970-c. 1005), British Menorca, County of Girona (thin page), Lords of Toledo, Banu Hajjaj of Seville, Emirate of Menorca (page 404), Tujibids, Taifa of Lisbon (one year), the military orders other than Calatrava.

## Repairs after review (2026-10-25)

- jahwarid-taifa-of-cordoba (verdict fail, one finding, applied). The 35 km circle (about 3,850 km2) rested on a false premise: I had written that Cliopatria's 1031-1071 Córdoba shapes were 'drawn as a wider (Hammudid-era) realm'. shapes.csv gives caliphate-of-cordoba_1034 (1034-1065, 9,813 km2) and _1066 (1066-1071, 9,788 km2), both bbox -5.82..-3.97 E, 37.38..38.55 N, and the caliphate-of-cordoba dossier marks both 'wrong' and hands the shape to this state. The Taifa of Córdoba page was opened again (https://en.wikipedia.org/wiki/Taifa_of_C%C3%B3rdoba): no infobox area, 'Córdoba and its vicinity' only, no Jaén, Écija, Carmona or Almodóvar. Changed: keyframe 0 correction and note, identity predecessor and successor land, ledger 0-2 and the war zone now read {"cliopatria": "Caliphate of Córdoba", "year": 1034, "text": ...}. Validates, 0 errors, 0 warnings, --resolve included. Drawn area now about 9,800 km2, ratio 1.0 to Cliopatria.
- Where I keep a reservation: the page cannot size 'vicinity', so 9,813 km2 is Cliopatria's reading accepted because the neighbour dossier agrees, not a verified extent (confidence stays 3 on the dated events, which are the page's own). Cliopatria's 1028-1033 shape (15,032 km2, to -8.14 E) held a Beja strip that the caliphate-of-cordoba dossier says left in 1033 (Taifa of Mértola); no opened page says who held it from December 1031, so this dossier draws the 1034 shape from 1031 and the strip is nobody's here. The fetch tool rendered the infobox heading as 'Taifa Republic of Córdoba, c. 1037', against 1031 in the infobox body and the text; 1031 kept.
- For the reconciler: taifa-of-seville /ledger/13 (1070 gain, counterpart taifa-of-cordoba, region the admin-1 province of Córdoba, about 13.8 thousand km2) should map its counterpart to jahwarid-taifa-of-cordoba and its region to the same Cliopatria 1034 shape (or this dossier should widen to the province, which no page supports). Seville's /ledger/14-15 and 19 (Córdoba lost 1075, regained 1078, lost 1091) concern Córdoba after this state's end and are not touched.
