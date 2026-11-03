# Review of batch me-09-e (Phase B, 2026-10-25)

Reviewer: adversarial review of beylik-of-karaman, beylik-of-isfendiyar, beylik-of-aydin, beylik-of-karasi, beylik-of-hamid, ahi-republic. All six validate (0 errors, 0 warnings with --resolve) before and after the reviewer's edits. Neighbours read: every Context polity of the author's brief except republic-of-genoa (no dossier yet; its group has not run).

Verdicts: beylik-of-karaman **fail**, beylik-of-isfendiyar **fail**, beylik-of-aydin **fix**, beylik-of-karasi **fix**, beylik-of-hamid **thin**, ahi-republic **thin**. `fix` here means fixed by the reviewer (applied: true); `fail` goes back to the author; `thin` goes to a gap-filler.

## beylik-of-karaman: fail

Findings:
- `/ledger (between /ledger/10 and /ledger/11)` (open, for the author): Missing event: Bayezid I took Akşehir, Niğde and the capital Konya from Karaman in the 1390 campaign, then accepted peace in 1391; the ledger goes from 1363 to 1397 with Konya as capital throughout. Evidence: Bayezid I page (in this dossier's sources): 'In a single campaign over the summer and fall of 1390 ... overwhelmed the remaining beyliks ... as well as taking the cities of Akşehir and Niğde, as well as their capital Konya from the Karaman'; 'Bayezid accepted peace proposals from Karaman (1391)'. Fix: Add a 1390 loss (counterpart ottoman-empire, regions Akşehir, Niğde and Konya, confidence 2, source Bayezid I) and, for 1391, either a gain back of Konya at confidence 1 (the page does not say Konya was returned) or say in the note what the 1391 peace left; adjust keyframe beylik-of-karaman_1385 and the Konya capital span to match.
- `/wars/1/from` (applied by reviewer): War 'Bayezid I's campaigns against the Karamanids' started in 1391; the page's campaign is 1390. Evidence: Bayezid I page: 'In a single campaign over the summer and fall of 1390 ...' (Konya, Akşehir, Niğde taken from Karaman). Fix: from: 1390 (done by the reviewer).
- `/ledger/1/region/union/1/lat` (applied by reviewer): Ermenek drawn at lat 36.44, 22 km south of the town. Evidence: Ermenek page: '36°38′20″N 32°53′33″E' (36.639 N, 32.892 E); the armenian-kingdom-of-cilicia dossier also uses 36.64. Fix: lat 36.64 (done by the reviewer).
- `/ledger (1410-1414)` (open, for the author): No mirror for the germiyanids dossier's Kütahya events (contest 1410-1411, loss to Karaman 1411 at confidence 3, gain back 1414). Evidence: germiyanids /ledger/12: 'In 1411, Kütahya fell to Mehmed II of Karaman (r. 1398-1399, 1402-1420)' (Germiyanids page); author's notes list it as out of budget. Fix: Add 1410 contest_start, 1411 contest_end + gain (Kütahya, 30 km, counterpart germiyanids) and 1414 loss to germiyanids, citing the Germiyanids page.
- `/ledger (1305, 1335)` (open, for the author): The ilkhanate dossier records vassal_start 1305 and vassal_end 1335 with beylik-of-karaman (and a 1305 loss); this ledger has no vassal events ('suzerain side, not repeated here'). Evidence: Reviewer brief 2.3: a vassal_start of X must be a vassal_start in X's ledger with this state as counterpart. The Karamanids page names emir Chupan driving the Karamanids out of Konya. Fix: Add vassal_start (counterpart ilkhanate) and vassal_end 1335 at the ilkhanate's confidence, or note why the Karamanids were not Ilkhanid vassals so that ia-02 drops its events.

Gaps for a gap-filler:
- `/ledger/7`: 1326 gain of the Beyşehir strip (confidence 1; the eshrefids dossier loses it to the ilkhanate in 1326, the ilkhanate has no loss to Karaman) (try https://en.wikipedia.org/wiki/Eshrefids)
- `/ledger/9`: 1352 loss of the strip north-west of Konya (confidence 1, counterpart nobody) (try https://en.wikipedia.org/wiki/Karamanids)
- `/ledger/10`: 1363 regain of the same strip (confidence 1) (try https://en.wikipedia.org/wiki/Murad_I)
- `/ledger`: Alaeddin Ali's capture of Beyşehir 'which had been an Ottoman city' (Karamanids page, undated) and Ibrahim Bey's march on Ankara and Kütahya (try https://en.wikipedia.org/wiki/Murad_I)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Karamanids: confirmed ('gave the town of Larende (now Karaman ...) and Ermenek (c. 1260)')
- `/ledger/11` https://en.wikipedia.org/wiki/Bayezid_I: confirmed ('In 1397, Bayezid defeated the emir of Karaman in Akçay, killing him and annexing his territory'); the same page's 1390 loss of Konya is missing from the ledger
- `/ledger/13` https://en.wikipedia.org/wiki/Mehmed_the_Conqueror: confirmed ('captured both Karaman (Larende) and Konya in 1466')
- `/ledger/15` https://en.wikipedia.org/wiki/Karamanids: confirmed (infobox 'Annexation of Konya: 1468')
- `/ledger/17` https://en.wikipedia.org/wiki/Karamanids: confirmed ('terminated by the Ottomans in 1487'; infobox 'Rump state (1474-1487)', 'Silifke (1474-1487)')

Area: The Karamanids page has no area; the author says so. Largest Cliopatria shape 100,291 km2.

## beylik-of-isfendiyar: fail

Findings:
- `/keyframe_review/13 and /wars/2` (open, for the author): Keyframe beylik-of-isfendiyar_1407 (1407-1458) is marked ok and the war 'İsfendiyar's revolt against Murad II' says 'no land change is named', but the Candar page names one: Çankırı and Tosya passed to the Ottomans before the 1423 revolt. Evidence: Candar dynasty page: 'When one of his sons, Kasım claimed control over Çankırı and Tosya' and declared them Ottoman territory; the realm split again; İsfendiyar revolted against Murad II, lost at Bolu and 'retreated to Sinop in 1423'. Fix: Add a loss of Çankırı and Tosya (counterpart ottoman-empire, confidence 2, year the page allows, at the latest 1423, source Candar dynasty); mark the 1407 shape adjust with a correction that removes the southern lobe from that year; give the war a zone and correct its outcome.
- `/keyframe_review/11/note and /wars/0/note` (applied by reviewer): The Bayezid I page was paraphrased as 'moved against Kastamonu and Sinop'; it says he conquered both. Evidence: Bayezid I page: 'Bayezid moved north against Kastamonu, which had given refuge to many fleeing from his forces, and conquered both that city as well as Sinop.' The Candar page instead has İsfendiyar as an autonomous vassal at Sinop. Fix: Quote the page and say that the two pages disagree (done by the reviewer). The keyframe still follows the Candar page; the author may keep that reading at confidence 2.
- `/ledger (1309-1335, 1391-1402, 1402)` (open, for the author): No vassal events, although the Candar page states three overlordships. Evidence: Candar page: Süleyman I ruled 'under the authority of the Ilkhanate' until Abu Sa'id's death (1335); in 1391 İsfendiyar 'recognized the suzerainty of Bayezid I and became an Ottoman vassal'; in 1402 he 'recognized the authority of ... Timur'. The ilkhanate dossier carries the 1309-1335 vassalage under kastamonu and beylik-of-sinop instead. Fix: Add vassal_start/vassal_end ilkhanate (1309 or the year the page allows, to 1335), ottoman-empire (1391-1402) and timurid-empire (1402, end as the pages allow), at confidence 2.

Gaps for a gap-filler:
- `/ledger/4`: date of the southern lobe (Çankırı, Tosya, Kalecik), drawn by Cliopatria in 1344 (confidence 1) (try https://en.wikipedia.org/wiki/Çankırı)
- `/keyframe_review/9`: the 1383-1385 division (Kötürüm Bayezid at Sinop, Süleyman at Kastamonu with Murad I's backing) is not drawn (try https://en.wikipedia.org/wiki/Murad_I)

Spot checks:
- `/ledger/2` https://en.wikipedia.org/wiki/Candar_dynasty: confirmed (infobox 'Eflani 1291-1309; Kastamonu 1309-1398; Sinop 1398-1461')
- `/ledger/3` https://en.wikipedia.org/wiki/Anatolian_beyliks: confirmed (table 'Pervâneid | Sinop | 1277-1322')
- `/ledger/5` https://en.wikipedia.org/wiki/Candar_dynasty: confirmed (1391 assault on Kastamonu, death of Süleyman II, İsfendiyar a vassal); the Bayezid I page adds that Sinop was conquered too
- `/ledger/7` https://en.wikipedia.org/wiki/Candar_dynasty: confirmed (Timur confirmed 'Kastamonu, Kalecik, Tosya, and Çankırı', 1402)
- `/ledger/8` https://en.wikipedia.org/wiki/Candar_dynasty: confirmed (1461, Mehmed II with Kızıl Ahmed 'captured Sinop')

Area: No area on the Candar page. Largest Cliopatria shape 49,106 km2.

## beylik-of-aydin: fix

Findings:
- `/identity/capitals/0, /ledger/0,5,6,7,8, /keyframe_review/0-6 (15 discs)` (applied by reviewer): Birgi, the capital, was placed at 27.70 E 38.20 N, about 32 km west of the town, so its 25 km disc did not contain Birgi. Evidence: Birgi page: '38°15′18″N 28°03′54″E' (38.255 N, 28.065 E), Ödemiş district, İzmir Province. Fix: lon 28.065, lat 38.255 in all 15 discs and the notes (done by the reviewer).

Gaps for a gap-filler:
- `/keyframe_review/5`: Mehmed I's capture of İzmir (his infobox lists 'Capture of İzmir' and 'Campaign of Aydinids', undated); the ottoman-empire dossier takes İzmir province in 1415 (try https://en.wikipedia.org/wiki/Cüneyd_Bey)
- `/ledger/6`: who restored the beylik in 1402 and whether Smyrna came back to it after the Timurid siege (try https://en.wikipedia.org/wiki/Siege_of_Smyrna)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Aydinids: confirmed (infobox 'Split from the Germiyanids: 1308'; Ephesus taken 'in October 1304')
- `/ledger/1` https://en.wikipedia.org/wiki/Aydinids: confirmed ('From 1317-1329, the Aydinids besieged Smyrna')
- `/ledger/4` https://en.wikipedia.org/wiki/Smyrniote_crusades: confirmed (Pallene 13 May 1344, harbour fortress taken 'later that year', acropolis held; Latin until 1402)
- `/ledger/5` https://en.wikipedia.org/wiki/Bayezid_I: confirmed ('In a single campaign over the summer and fall of 1390, Bayezid conquered the beyliks of Aydin, Saruhan and Menteshe')
- `/ledger/7` https://en.wikipedia.org/wiki/Aydinids: confirmed (infobox 'Annexation by the Ottoman Empire: 1426'; Junayd 1405-1426)

Area: No area on the Aydinids page. Largest Cliopatria shape 7,982 km2.

## beylik-of-karasi: fix

Findings:
- `/ledger/1, /ledger/2, /ledger/3, /keyframe_review/1-3, /wars/0` (applied by reviewer): The Karasids page was quoted as 'between 1302 and 1308, Karasi expanded into Lesser Mysia'; the full sentence dates the Byzantine campaign to 1302-1308 and puts Karasi's expansion after it, so the 1302-1308 contest and the 1308 gain are not dated by the page. Evidence: Karasids page: 'Following the Byzantine campaign in western Anatolia allied with Catalan Company and Alans between 1302 and 1308, Karasi expanded into Lesser Mysia and reached south bordering the Sarukhanids.' Fix: Full quote in the five notes, the 1302/1308 notes reworded, the three events lowered to confidence 1 (done by the reviewer). A gap-filler may move the gain toward Cliopatria's 1326 if a page dates it.

Gaps for a gap-filler:
- `/ledger/3`: year of the expansion into Lesser Mysia (after 1308; Cliopatria 1326) and the Byzantine mirror loss (try https://en.wikipedia.org/wiki/Catalan_Company)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Anatolian_beyliks: confirmed ('Karasid Beylik | Founder: Karasi Bey | Balıkesir, later Bergama and Çanakkale | 1296-1357')
- `/ledger/3` https://en.wikipedia.org/wiki/Karasids: mis-dated (the 1302-1308 span is the Byzantine campaign's; fixed to confidence 1)
- `/ledger/4` https://en.wikipedia.org/wiki/Orhan_I: confirmed ('In 1345, there was a change of strategy'; Pergamum and Palaeocastro (Balıkesir) annexed)

Area: No area on the Karasids page. The author's note that the infobox 'Area' excludes Artaki, Pegae, Adramytion, Pergamon and Dardanellia could not be confirmed (the summary returned no Area field); harmless, notes only. Largest Cliopatria shape 30,226 km2.

## beylik-of-hamid: thin

Gaps for a gap-filler:
- `/keyframe_review/3, /keyframe_review/4`: Who held the Cliopatria 1333 shape (Denizli, Burdur and Afyon country) in 1333-1391: this dossier keeps it with Isparta Province to 1391 on one sentence ('Their territory became the Ottoman Sanjak of Hamid, roughly corresponding to the present-day Isparta Province'), while the germiyanids dossier gains it in 1333 and 1344 and its page puts 'Denizli and Karahisar' in Yakub I's domain. The two dossiers draw the same cells for up to 58 years. (try https://en.wikipedia.org/wiki/Germiyanids)
- `/identity/rulers`: the 1324-1327 gap between Dündar and Khidr (Timurtash's Ilkhanid occupation is the likely reason; no page opened says so) (try https://en.wikipedia.org/wiki/Timurtash)
- `/ledger`: the sale of Akşehir and Beyşehir to Murad I (Hamidids page, undated) and the ilkhanate's vassal_start 1305 / vassal_end 1335 with beylik-of-hamid, unmatched here (try https://en.wikipedia.org/wiki/Murad_I)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Beylik_of_Teke: confirmed ('established by a branch of the Hamidid dynasty in 1321'; 'a split of territories between two brothers')
- `/ledger/2` https://en.wikipedia.org/wiki/Hamidids: confirmed ('The Hamidid beylik was annexed by the Ottoman sultan Bayezid I in 1391'); the Bayezid I page puts the campaign in 1390, within one year
- `/identity/capitals/0` https://en.wikipedia.org/wiki/Anatolian_beyliks: confirmed ('Hamidids | Founder: Hamid Beg | Eğirdir | 1300-1391')

Area: No km2 on the page. 'Roughly Isparta Province' (under 10,000 km2) against the 57,555 km2 1305 shape (with Antalya) is a factor above 5 but describes the later sanjak; the Teke split of 1321 explains most of it, and the author says so in KF0-KF3. Largest Cliopatria shape 57,555 km2.

## ahi-republic: thin

Gaps for a gap-filler:
- `/ledger (c. 1290)`: vassal_start ilkhanate c. 1290 (the page says the Ahis declared 'their semi-independence under Mongol suzerainty') and its end; neither this dossier nor the ilkhanate dossier records it. The author left it to the ilkhanate, but the rule needs it on both sides. (try https://en.wikipedia.org/wiki/Ilkhanate)
- `/ledger/1`: how long the 1354 Ottoman hold lasted (drawn as an occupation to 1362; the page says 'briefly annexed' and that the Ahis 'tried to restore their independence after Orhan's death') (try https://en.wikipedia.org/wiki/Ankara)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Ahis: confirmed ('declare their semi-independence under Mongol suzerainty', about 1290)
- `/ledger/1` https://en.wikipedia.org/wiki/Ahis: confirmed ('In 1354, Ankara was briefly annexed by Orhan')
- `/ledger/3` https://en.wikipedia.org/wiki/Ahis: confirmed ('in 1362 Murad I ended the political power of Ahis and they became the part of Ottoman Empire')

Area: The Ahis page has no area (the summary found no infobox; the dossier cites 'infobox: end 1362', which is in the body, a wording slip). The Cliopatria shape omits Ankara; the author adds a 25 km disc. Largest Cliopatria shape 4,421 km2.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| beylik-of-karaman 1260 gain (sultanate-of-rum) | sultanate-of-rum 1260 loss | mismatch | Rum's 1260 loss of the west goes to mongol-empire (c1); no loss of Larende and Ermenek to Karaman. The armenian-kingdom-of-cilicia dossier also gives Ermenek to Karaman in 1260 (/ledger/17), so Ermenek has two donors. Route to me-09 (sultanate-of-rum). |
| beylik-of-karaman 1260 gain (armenian-kingdom-of-cilicia) | armenian-kingdom-of-cilicia 1260 loss | matched | Mut (cilicia /ledger/15, /ledger/17). |
| beylik-of-karaman 1277 contest_start (sultanate-of-rum) | sultanate-of-rum 1277 contest_start | matched | Konya; Rum ends the contest in 1277, Karaman in 1278 (within a year). |
| beylik-of-karaman 1308 gain (sultanate-of-rum) | sultanate-of-rum 1308 dissolve | matched | Rum dissolves in 1308 and names beylik-of-karaman as successor for Konya and the plateau. |
| beylik-of-karaman 1326 gain (ilkhanate) | ilkhanate   | missing | Confidence 1. eshrefids loses the Beyşehir land to the ilkhanate in 1326; the ilkhanate has neither the gain nor a loss to Karaman. Route to ia-02. |
| beylik-of-karaman 1333 gain (nobody) | -   | exception | Counterpart nobody (also 1352 loss and 1363 gain, confidence 1). |
| beylik-of-karaman 1390 loss (missing) (ottoman-empire) | ottoman-empire   | missing | Neither side records Bayezid I's 1390 capture of Konya, Akşehir and Niğde (Bayezid I page). Karaman fix; route the mirror to me-10. |
| beylik-of-karaman 1397 loss (ottoman-empire) | ottoman-empire   | missing | ottoman-empire has no 1397 gain of Karaman. Route to me-10. |
| beylik-of-karaman 1402 gain (ottoman-empire) | ottoman-empire 1402 loss | mismatch | ottoman-empire /ledger/25 loses to the string 'Anatolian beyliks restored by Timur (Karaman, Germiyan, Aydın and others)', not to the slugs. Route to me-10. |
| beylik-of-karaman 1466 contest_start (ottoman-empire) | ottoman-empire   | missing | No Ottoman contest 1466-1468. Route to me-10. |
| beylik-of-karaman 1468 loss (ottoman-empire) | ottoman-empire 1468 gain | mismatch | Matched in year; the Ottoman gain takes Karaman admin1 whole, including the Taurus rump this dossier keeps to 1487. |
| beylik-of-karaman 1487 loss (ottoman-empire) | ottoman-empire   | missing | No Ottoman 1487 gain of the rump. Route to me-10. |
| germiyanids 1411 loss (beylik-of-karaman) | beylik-of-karaman   | missing | Kütahya to Karaman 1411 (c3) and back 1414; Karaman has neither. Karaman fix. |
| ilkhanate 1305 vassal_start (beylik-of-karaman) | beylik-of-karaman   | mismatch | ilkhanate /ledger/11-12 (loss + vassal_start 1305) and /ledger/22 (vassal_end 1335), confidence 1; Karaman has none. |
| beylik-of-isfendiyar 1309 gain (kastamonu) | kastamonu 1309 loss | matched |  |
| beylik-of-isfendiyar 1322 gain (beylik-of-sinop) | beylik-of-sinop 1322 loss | matched |  |
| beylik-of-isfendiyar 1344 gain (nobody) | -   | exception | Southern lobe, confidence 1. |
| beylik-of-isfendiyar 1391 loss (ottoman-empire) | ottoman-empire   | missing | No Ottoman 1391 gain of Kastamonu (the Bayezid I page also has Sinop taken). Route to me-10. |
| beylik-of-isfendiyar 1402 gain (ottoman-empire) | ottoman-empire 1402 loss | mismatch | Ottoman /ledger/25 string counterpart. Route to me-10. |
| beylik-of-isfendiyar 1423 loss (missing) (ottoman-empire) | ottoman-empire   | missing | Çankırı and Tosya to the Ottomans before 1423 (Candar page); neither side has it. |
| beylik-of-isfendiyar 1461 loss (ottoman-empire) | ottoman-empire 1462 gain | matched | Within a year. |
| ilkhanate 1309 vassal_start (kastamonu / beylik-of-sinop) | beylik-of-isfendiyar   | mismatch | The ilkhanate's 1309/1305-1335 vassals kastamonu and beylik-of-sinop should read beylik-of-isfendiyar after 1309/1322 (Candar page); Isfendiyar has no vassal events. Route to ia-02 and the author. |
| beylik-of-aydin 1308 found (germiyanids) | germiyanids   | missing | Aydin splits from the Germiyanids in 1308 (Aydinids infobox); germiyanids has no loss or split to Aydin and does not hold the Aydin shape 1305-1307. Route to me-09-f. |
| beylik-of-aydin 1329 gain (defenders of Smyrna (not named on the page)) | -   | exception | Holder not named on any page (also the 1317-1329 contest). |
| beylik-of-aydin 1344 loss (Crusade of 1344 (holders of Smyrna)) | -   | exception | No dossier; listed in counterparts_needing_dossiers (crusader-smyrna). |
| beylik-of-aydin 1390 loss (ottoman-empire) | ottoman-empire   | missing | No Ottoman 1390 gain of Aydin, Saruhan or Menteshe. Route to me-10. |
| beylik-of-aydin 1402 gain (ottoman-empire) | ottoman-empire 1402 loss | mismatch | Ottoman string counterpart. Route to me-10. |
| beylik-of-aydin 1426 loss (ottoman-empire) | ottoman-empire 1415 gain | mismatch | No Ottoman gain of Aydin in 1425-1427; ottoman-empire /ledger/30 instead takes İzmir and Manisa admin1 from beylik-of-saruhan in 1415 (c1), which covers Birgi and Ephesus while this dossier keeps them to 1426. Route to me-10. |
| beylik-of-karasi 1308 gain (byzantine-empire) | byzantine-empire   | missing | No Byzantine loss of Lesser Mysia (1308 here at c1, 1326 in Cliopatria); also no mirror of the 1302-1308 contest. Route to eu-05. |
| beylik-of-karasi 1345 loss (ottoman-empire) | ottoman-empire 1346 gain | matched | Within a year. |
| beylik-of-hamid 1321 split (beylik-of-teke) | beylik-of-teke 1321 found | matched |  |
| beylik-of-hamid 1391 loss (ottoman-empire) | ottoman-empire   | missing | No Ottoman gain of Hamid (Bayezid I page: 1390). Route to me-10. |
| germiyanids 1333 gain (beylik-of-hamid) | beylik-of-hamid   | mismatch | Germiyan gains Hamid land in 1333 and 1344 (c1); Hamid keeps Isparta and the 1333 shape to 1391. Both draw the same cells; reconcile (me-09-f and this author). |
| ilkhanate 1305 vassal_start (beylik-of-hamid) | beylik-of-hamid   | mismatch | ilkhanate /ledger/7-8, /ledger/20 (c1); Hamid has none. |
| ahi-republic 1354 occupation_start (ottoman-empire) | ottoman-empire   | missing | ottoman-empire's 1354 gain is Gallipoli; no Ankara occupation. Route to me-10. |
| ahi-republic 1362 loss (ottoman-empire) | ottoman-empire 1363 gain | matched | Within a year. |
| ahi-republic 1290 vassal_start (missing) (ilkhanate) | ilkhanate   | missing | Mongol suzerainty c. 1290 (Ahis page) is on neither side. |

## Gazetteer names

- Birgi (beylik-of-aydin): place; 28.065 E 38.255 N (Birgi page; the author's 27.70 E 38.20 N was 32 km off)
- Ermenek (beylik-of-karaman): place; 32.892 E 36.639 N (Ermenek page; the author's hint said 36.44 N)
- Mut (beylik-of-karaman): place; about 33.43 E 36.645 N
- Silifke (beylik-of-karaman): place; about 33.93 E 36.38 N
- Eflani (beylik-of-isfendiyar): place; about 32.96 E 41.43 N
- Safranbolu (beylik-of-isfendiyar): place (notes only)
- Tosya (beylik-of-isfendiyar): place
- Kalecik (beylik-of-isfendiyar): place
- Lesser Mysia (beylik-of-karasi): region (text only)

## Counterparts needing dossiers

- Crusader (later Hospitaller) Smyrna (crusader-smyrna, 1344-1402): Smyrniote crusades page: 'Latin reconquest of Smyrna which they hold until 1402'; the author proposed 1344-1374 (hospitaller-rhodes takes it in 1374 under a string counterpart). Group me-09-x.

## Problems and routing

- No page failed to load. WebFetch returns summaries; quotes above are those the summaries returned verbatim.
- Reviewer applied small fixes (validated afterwards, read back after more than ten seconds): beylik-of-aydin Birgi coordinates (15 discs + notes); beylik-of-karaman Ermenek latitude and war /wars/1 start 1390; beylik-of-karasi full quote of the Lesser Mysia sentence and confidence 2->1 on /ledger/1-3; beylik-of-isfendiyar Bayezid I quote in /keyframe_review/11 and /wars/0 notes.
- ottoman-empire (me-10) lacks most mirrors of this batch: 1390 Anatolian campaign (Aydin, Saruhan, Menteshe, Hamid, Teke, Germiyan; Konya, Akşehir, Niğde from Karaman), 1391 Kastamonu (and Sinop), 1397 Karaman, 1402 losses to slugs instead of a string, 1426 Aydin, 1466 Karaman contest, 1487 Karaman rump, 1354 Ankara; its 1415 İzmir/Manisa gain overlaps beylik-of-aydin to 1426.
- germiyanids (me-09-f) and beylik-of-hamid draw the same Isparta/Denizli/Afyon cells 1333-1391; germiyanids lacks the 1308 Aydin split; Karaman lacks germiyanids' Kütahya events.
- ilkhanate (ia-02): vassal counterparts kastamonu/beylik-of-sinop for 1309-1335 should be beylik-of-isfendiyar; its 1305 vassal_start/loss with beylik-of-karaman and beylik-of-hamid have no mirror; no Ahi suzerainty; no 1326 Eshrefid gain.
- byzantine-empire (eu-05): no loss of Lesser Mysia to Karasi.
