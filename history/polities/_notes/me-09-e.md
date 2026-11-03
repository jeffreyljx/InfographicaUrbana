# Notes of batch me-09-e (Phase B, 2026-10-25)

Six dossiers: beylik-of-karaman, beylik-of-isfendiyar, beylik-of-aydin, beylik-of-karasi, beylik-of-hamid, ahi-republic. All validate with 0 errors and 0 warnings under `--resolve`. 15 distinct pages opened (Karamanids, Anatolian beyliks, Bayezid I, Mehmed II (Mehmed the Conqueror), Murad II, Candar dynasty, Aydinids, Smyrniote crusades, Ottoman Interregnum, Mehmed I, Karasids, Orhan I, Hamidids, Beylik of Teke, Ahis). No page failed to load. Two pages (Ottoman Interregnum, Mehmed I) said nothing on Aydin and are listed as thin.

Method note: the Cliopatria shape changes were attributed to counterparts by diffing the H3 cells of each year against the neighbours (tools/gazetteer.py cells), so the "gain" and "loss" counterparts of confidence-1 events come from the grid, not from a page.

## Row decisions

- Beylik of Isfendiyar and Beylik of Sinop (shared Q2096678): different states. Sinop is the Pervaneid emirate of Sinop (1277-1322, Anatolian beyliks table; beylik-of-sinop dossier), annexed by the Candars in 1322; beylik-of-isfendiyar is the Candar state (1291-1461). Not merged. As the kastamonu author and the me-09-f reviewer asked, `Kastamonu` is added to the cliopatria_names of beylik-of-isfendiyar; its three shapes are reviewed there (kastamonu_1305 for 1309-1313, kastamonu_1314 for 1314-1321, kastamonu_1333 as an alias of beylik-of-isfendiyar_1333).
- Karaman, Aydin, Karasi, Hamid, Ahi: one dossier per Cliopatria Name. Starts and ends follow the pages, not Cliopatria: Karaman 1255-1487 (Cliopatria 1305-1467), Candar 1291-1461 (1305-1462), Aydin 1308-1426 (1305-1428), Karasi 1296-1345 (1305-1343), Hamid 1301-1391 (1305-1343), Ahi 1290-1362 (1305-1362).

## beylik-of-karaman (5 pages)
- New keyframes: 1255-1304 (the 1305 shape projected back), 1308-1313 (the 1314 shape from the Karamanid conquest of Konya in 1308; the sultanate-of-rum dossier hands over 'Konya and the plateau' in 1308), 1468-1487 (the Taurus rump at Mut and Silifke: the 1467 shape in Mersin province).
- Disagreements: 1397 annexation (Bayezid I page) against the infobox's vassal period 1398-1402 (ledger follows the annexation); Larende and Konya taken in 1466 (Mehmed II) against 'Annexation of Konya: 1468' (infobox) - drawn contested 1466-1468; ruler table against body (Mehmed I 1277/1278, Karim al-Din 1262/1263; Alaattin Ali II overlaps Mehmed II).
- Unverified (page silent, confidence 1 or ok with note): the 1326 strip (30 cells, Cliopatria takes it from the Eshrefids' row), the 1333/1352/1363 strip north-west of Konya (29-31 cells), all shape changes after 1363 (grid noise). (Fix pass: the Kutahya episode 1410-1414 is now mirrored from the Germiyanids page.)
- Open: the Mamluk episodes (Tarsus, Konya), the 1293 siege of Alanya, the 1261 march on Konya, the extent of the beylik restored in 1402.

## beylik-of-isfendiyar (4 pages)
- New keyframes: 1291-1304, 1322-1332 (Eflani + Kastamonu + annexed Sinop), 1391-1401 (the realm less the Kastamonu country, held by the Ottomans). The Cliopatria 1344 jump (48.8k km2) is the Kastamonu row folded in (120 cells) plus 30 cells round Cankiri and Tosya; the Candar page undated.
- The 1309 Kastamonu conquest is dated by the infobox capital (Kastamonu 1309-1398) and the beyliks table (Chobanids end 1309); the 1322 Sinop annexation by the table row 'Pervaneid | Sinop | 1277-1322' (the Candar page says 'annexed Safranbolu and Sinop' without a year).
- Open: what the Ottomans held beyond Kastamonu 1391-1402 (confidence 2); the 1383 division of the dynasty (Kötürüm Bayezid at Sinop) and its reunion 1385; infobox Kastamonu to 1398 against Suleyman II's death there in 1391.

## beylik-of-aydin (6 pages, two thin)
- Cliopatria's 27-cell shape lacks the capital Birgi and Smyrna; Birgi (25 km disc, lon 27.70 lat 38.20) and, for 1329-1343, Izmir (20 km) are added in the corrections.
- Founding 1308 (infobox) rather than 1305; Ephesus was taken in October 1304 by Mehmed Bey as a Germiyanid vassal. End 1426 (infobox) against 1425 (beyliks table) and Cliopatria 1428.
- Disagreements: Smyrna conquered 'at the beginning of the 14th century' (Smyrniote crusades) against besieged 1317-1329 (Aydinids); crusader conquest 1344 against 1348; Umur's dates (table 1334-1348, crusades infobox 1343-1348). The earlier holders of Smyrna are named on no page (counterpart is a text string); the 1344 conquerors have no dossier (hospitaller-rhodes uses the same string 'Crusade of 1344 (holders of Smyrna)' for its 1374 gain).
- Open: the Ottoman annexation of 1425/1426 (no page), the 1402 restoration (the table resumes; Timur is not named for Aydin), the move of the capital to Ayasulug (no year).

## beylik-of-karasi (3 pages)
- End 1345 from the Orhan I page ('In 1345, there was a change of strategy'); the Karasids infobox offers 1348/9 and about 1335, the beyliks table 1357, the ottoman-empire dossier 1346. Start 1296 (table). The northern Lesser Mysia expansion is dated 1302-1308 on the Karasids page (Cliopatria 1326, from the Byzantine Empire); the 1326 shape is used from 1308.
- The infobox 'Area' excludes Artaki, Pegae, Adramytion, Pergamon and Dardanellia, which sits badly with the capital Bergama and Dursun's offer of Balikesir, Bergama and Edremit; unresolved. No ruler strip (undated list).

## beylik-of-hamid (3 pages)
- Overrides Cliopatria twice: the Teke split is 1321 (Beylik of Teke page), and the beylik lasts to 1391 over 'roughly the present-day Isparta Province' (Hamidids page), not to 1343. Conflict with the germiyanids dossier (gains from Hamid in 1333 and 1344, confidence 1, Cliopatria only): both now draw the Isparta cells; reconcile with the pages side by side.
- Open: the sale of Akşehir and Beyşehir to Murad I (undated), the capital (Egirdir from the beyliks table), the ruler gaps.

## ahi-republic (2 pages)
- The Cliopatria shape (16 cells) lies south-west of Ankara and omits the city; a 25 km disc round Ankara is added. Start about 1290 (page), end 1362 (Murad I); the 1354 annexation by Orhan is an occupation to 1362. The Mongol suzerainty (about 1290, no end) is not carried in the ilkhanate dossier.

## For the orchestrator / other groups (mirrors that are missing)
- ottoman-empire (me-10): gain Karaman 1397 and loss 1402; gain Aydin 1390 and loss 1402; gain Kastamonu country 1391 (Candar) and loss 1402; gain Hamid 1391; gain Karasi 1345 (dossier: 1346); gain Ahi 1362 (dossier: 1363, with a 1354 occupation); gain Candar 1461 (dossier: 1462); Karaman 1468 should leave the Taurus rump out until 1487 (new keyframe beylik-of-karaman_1468), then gain it in 1487.
- ilkhanate (ia-02): vassal counterparts beylik-of-sinop and kastamonu for 1309-1335 should read beylik-of-isfendiyar (Candar page: Suleyman I reigned under Ilkhanate authority until Abu Said's death); add ahi-republic (Mongol suzerainty about 1290); the Karaman 1326 strip has no Ilkhanid loss; beylik-of-karaman now carries vassal_start 1305 / vassal_end 1335 with counterpart ilkhanate (confidence 1), beylik-of-isfendiyar the same for 1309-1335 (confidence 2).
- byzantine-empire (eu-05): no loss for the Lesser Mysia coast (1308 here, 1326 in Cliopatria) and none for Ephesus 1304.
- germiyanids (me-09-f): the Hamid gains of 1333 and 1344 and the 1363 Ankara lobe conflict with beylik-of-hamid and ahi-republic; (the Kutahya episode is now mirrored in beylik-of-karaman, fix pass).
- Crusader holders of Smyrna 1344-1374 have no dossier (suggested slug crusader-smyrna, group me-09-x).

## Gazetteer names needed
Birgi, Ermenek, Mut, Silifke, Eflani, Safranbolu, Tosya, Kalecik (places; coordinates used instead where not in places.jsonl).

## Fix pass (author, after the review of 2026-10-25; both dossiers still validate, 0 errors, 0 warnings under --resolve)
Pages reopened: Karamanids, Bayezid I, Germiyanids, Abu Sa'id Bahadur Khan, Akşehir (coordinates), Eshrefids, Murad I, Mehmed I (Karaman section); Candar dynasty, Battle of Bolu, Murad II, Mehmed I, Çankırı (Isfendiyar section). Nothing fixed from memory.

### beylik-of-karaman (fail -> fixed)
- Applied: 1390 loss of Akşehir, Niğde and Konya to Bayezid I (confidence 2; Bayezid I page 'their capital Konya from the Karaman'); 1391 gain back at confidence 1 because the page says only 'Bayezid accepted peace proposals from Karaman (1391)', no terms (delete it, its capital_move and keyframe beylik-of-karaman_1391 if a better page shows Konya stayed Ottoman to 1397). Keyframe 1385 now 1385-1389, new keyframes 1390 and 1391-1396; the Konya capital span is split (1307-1389, 1391-1467) with Larende in 1390 as a reading; war 'Bayezid I's campaigns' has the three cities as zone. Akşehir has no gazetteer place: coordinates of the Akşehir page (38°21′27″N 31°24′59″E) used, name listed below.
- Applied: Kütahya mirror: contest_start September 1410, contest_end and gain 1411 (confidence 3), loss 1414, from the Germiyanids page ('In 1411, Kütahya fell to Mehmed II of Karaman'; 'Mehmed Chelebi reinstated Yakub's rule in Germiyan in 1414'); new keyframe beylik-of-karaman_1411 (1411-1413), keyframe 1407 now adjust (years), new war 'Karaman, Germiyan and the Ottomans over Kütahya (1410-1415)' (the Karamanids infobox 'Ottoman-Karamanid War 1413-1415', Mehmed I infobox 'Campaign of Karamanids (1414)').
- Applied: vassal_start 1305 and vassal_end 1335 (month 11) with counterpart ilkhanate, confidence 1, mirroring ia-02. I did not drop them: the Karamanids page has the Ilkhanid governors Chupan and Timurtash driving the Karamanids out of Konya and dates the Karamanid expansion 'after the fall of the Ilkhanids in the 1330s', but never calls them vassals; the year 1305 is Cliopatria's. If ia-02 drops its events, drop these.
- Applied by the reviewer and kept: Ermenek lat 36.64; war from 1390.
- Thin, reopened and still thin: the Eshrefids page says only that the dynasty 'ended when Mubariz al-Din Mehmed was executed by Timurtash' and names no Karamanid successor, so the 1326 strip stays at confidence 1 (the Ilkhanate has still no matching loss; route to ia-02); the 1352 and 1363 strip stays at confidence 1 (Karamanids reign table: Şemseddin 1350-1352, Hacı Sufi Musa's second reign from 1352, Alaattin Ali 1361-1398; Murad I page silent on the strip). Alaeddin Ali's capture of Beyşehir 'which had been an Ottoman city' (Karamanids page) stays undated; the Akşehir page says only that Akşehir and Beyşehir were the Ottoman-Karamanid border 'changing hands several times'. İbrahim's march on Ankara and Kütahya is a 1443-44 raid with no land change (Karamanids page); the Murad I page does not mention it. The Frenkyazısı battle is 1386 on the Karamanids infobox and 1387 on the Murad I infobox, no detail on either.
- Disagreement: none with the reviewer's reading; the only choice was the 1391 gain back (confidence 1), and I took the reviewer's first option because the infobox keeps Konya as capital 'Konya (1307–1468)' without a break.

### beylik-of-isfendiyar (fail -> fixed)
- The land change the review named is real but dated differently. Candar page: 'Kasım claimed control over Çankırı and Tosya and declared the incorporation of these provinces to the Ottoman Empire'; İsfendiyar then 'revolted against the new sultan Murad II ... retreated to Sinop in 1423'. Battle of Bolu page: while Murad II was occupied with Mustafa Çelebi (accession 1421, execution 20 February 1423) İsfendiyar 'took Tosya, Çankırı, and Kalecik from them'; defeated at Bolu in 1423, Ottoman troops occupied Küre, he sent his son to ask for peace, terms not given. I therefore record a loss in 1421 and a gain in 1422, both confidence 1, instead of a single loss in 1423 at confidence 2: the pages put the lobe back in İsfendiyar's hands before the 1423 battle and give no year for the Ottoman hold (the Mehmed I page's infobox 'Conquest of Candar dynasty', no year, suggests it began in Mehmed I's reign, so 1421 is the shortest hold the pages allow). Keyframe 1407 is adjust (years); new one-year keyframe 1421 removes the lobe; the war is renamed 'İsfendiyar's revolt against Murad II and the Battle of Bolu' (1421-1423) with the lobe as zone and the outcome corrected. Küre is not drawn (extent and tenure unknown).
- Applied: vassal_start/vassal_end ilkhanate 1309-1335 (confidence 2; Candar page 'until the death of their ruler Abu Sa'id', 30 November 1335 on the Abu Sa'id page), ottoman-empire 1391-1402 for the Sinop country (confidence 2; 'became an Ottoman vassal'; the Bayezid I page has Sinop conquered, kept as a disagreement), timurid-empire 1402-1403 (start confidence 2; the end year 1403 is the timurid-empire dossier's date for Timur leaving Anatolia, confidence 1, because the Candar page says only 'Following the departure of Timur from Anatolia during the Ottoman Interregnum').
- Applied by the reviewer and kept: the Bayezid I quote and the statement that the pages disagree about Sinop.
- Thin, reopened: the Çankırı page is silent on the Candar and Ottoman history, so the 1344 lobe stays at confidence 1 (Cliopatria only). The 1383 division is on the Candar page ('Kötürüm Bayezid Bey retreated to Sinop, which led to the division of the Beylik of Candar'; 1385: 'On Kötürüm Bayezid's death in 1385, his son Süleyman succeeded him as Süleyman II') and was Süleyman's revolt with Murad I's support; it divides one dynasty and is not drawn.

### For the orchestrator
- ottoman-empire (me-10): in addition to the mirrors listed above: gain Akşehir/Niğde/Konya 1390 and loss 1391 (Karaman, confidence 1 on the loss); gain of the Isfendiyar lobe (Çankırı, Tosya, Kalecik) 1421 and loss 1422; vassal Sinop country 1391-1402 (beylik-of-isfendiyar); Küre occupied 1423.
- ia-02: ilkhanate's 1309-1335 vassals for the Candar land should be beylik-of-isfendiyar; timurid-empire has no vassal of beylik-of-isfendiyar 1402-1403 (this dossier's mirror) and its 1403 'Anatolia is left' date is what the Candar vassal_end borrows.
- germiyanids (me-09-f): its Kütahya events 1410, 1411 and 1414 are now mirrored (matched, same years).
- Gazetteer names needed: Akşehir (place; 38.358 N 31.416 E; in beylik-of-karaman only as coordinates).
