# Notes: group jk-01-b (Japan, part b), Phase B, 2026-10-18

Six dossiers written: chuzan, hokuzan, nanzan, kenmu-restoration, ashikaga-shogunate, ryukyu-kingdom. All validate (0 errors). Pages opened with WebFetch, all in this run: Ashikaga shogunate, Nanboku-chō period, Ōnin War, Koshamain, Sengoku period, Kenmu Restoration, Chūzan, Hokuzan, Nanzan, Ryukyu Kingdom, Invasion of Ryukyu (11 pages, no failures). None of the infoboxes gives an area, so no infobox/Cliopatria ratio could be computed for any of the six; each keyframe note says so.

## Cliopatria rows to correct

- Nanzan 1395..1401 and Chüzan 1402..1428: Cliopatria ends Nanzan in 1401 and adds the Nanzan cell to Chüzan from 1402 (gazetteer: Chüzan 1402 contains Nanzan 1395, one H3 cell). Every page opened keeps Nanzan independent to 1429. Fixed in nanzan (years to 1429) and chuzan (cell removed).
- Hokuzan: Cliopatria keeps Hokuzan to 1421 and merges it into Chüzan in 1422; the Hokuzan page and the Ryukyu Kingdom page say Nakijin fell in 1416 (the Chūzan page says 1419, the Nanzan page implies 1419). Dossiers follow 1416; new keyframe chuzan_1416.
- Kenmu Restoration 1333..1343: the regime ended on 25 February 1336 (Kenmu page) and the Ashikaga shogunate dates from 11 August 1336; Cliopatria's Ashikaga row starts 1344. New keyframe ashikaga-shogunate_1336 (1336..1343) carries the same outline.
- Ashikaga Shogunate ends 1571 in Cliopatria, 2 September 1573 on the page: new keyframe ashikaga-shogunate_1572.
- Ryukyu Kingdom row stops at 1520; the kingdom lasted to 1872 and the Ryukyu Domain to 1879. The dossier runs to 1879 with new keyframes 1447, 1500 and 1611; the Cliopatria shapes get 'adjust' verdicts (Amami from 1447, Yaeyama from 1500).
- Ashikaga 1344..1458 is the claimed national realm, not ground held (Southern Court in Kyushu to 1385 and Yoshino to 1392; Kantō under Kamakura-fu). Kept as 'ok' with the contest events; the Kantō, the Kōga kubō and the Kyushu Tandai are not on any page opened (page budget).
- Ashikaga 1459..1467 includes the southern Oshima Peninsula (Twelve Garrisons of Dōnan); the Koshamain page does not say the shogunate claimed it (gain at confidence 1).
- Ashikaga 1540 and 1564 trims (100 km2 and 176 km2): no page dates them and they resolve to the same grid cells as the neighbouring shapes; no events.

## Pages that disagree

- Fall of Hokuzan: 1416 (Hokuzan, Ryukyu Kingdom) against 1419 (Chūzan; Nanzan 'ten years earlier').
- Chūzan page: Bunei's succession 1395 (text) against 1398 (table); Seii overthrown 'around 1349-1355'; Shishō's accession about 1407 (five years after 1402) while Bunei was invested in 1406.
- Nanzan page: Shōsatto 1314-1398 (table) against 1337-1396 (infobox); Taromai 1414?-1429 against 1415-1429.
- Kenmu page: Genkō War begins 1333 (infobox) against 1331 (text); the era counted 1334-1336 (Southern reckoning) or 1334-1338 (Northern).
- Ashikaga page: Takauji's reign 1338-1357 (text) against 1338-1358 (infobox).
- Ryukyu Kingdom page: Shō Shin 1477 or 1478; annexation 27 March 1879 (text) against 4 April 1879 (infobox); Satsuma invasion 5 April 1609 (infobox) against the day-by-day account (Amami 7 April, Shuri entered 5 May); Tokara Islands annexed in 1611 on that page but not on the Invasion page.

## Needs a dossier from another group

- southern-court: the Southern Court at Yoshino, 1337-1392 (Nanboku-chō page); counterpart of the Kyushu and Yoshino contests in ashikaga-shogunate and a successor of kenmu-restoration.
- satsuma-domain: counterpart of the 1609 contest, the 1611 loss and (since the fix of 2026-10-18) the vassal_start 1609-05 / vassal_end 1872-10 now carried in ryukyu-kingdom. No dossier exists and jk-01-x may treat the han as internal units; if so, rename the counterpart to tokugawa-shogunate in those events (the dates stand).
- Ming, Southern Ming and Qing: the vassal side is now in the dossiers (chuzan 1372-1429; ryukyu-kingdom 1429-1644 Ming, 1644-1646 Southern Ming, 1646-1872 Qing); the ming-dynasty, southern-ming and qing-dynasty dossiers may carry the mirror. Hokuzan and Nanzan are not yet recorded (see Fixes).
- warring-states-japan (group jk-01, exists): should carry the 1468 gain from, and the 1573 gain from, ashikaga-shogunate, and the contest 1467-1477 at Kyoto.
- empire-of-japan (exists): counterpart of the 1879 dissolve of ryukyu-kingdom.

## Gazetteer names missing

- place 'Yoshino' (Yoshino mountains, Nara Prefecture, about 34.37 N 135.86 E): ashikaga-shogunate, kenmu-restoration.
- region 'Amami Islands' (Amami Ōshima, Kikai, Tokunoshima, Okinoerabu, Yoron; about 27-28.5 N 128-130 E): ryukyu-kingdom.
- region 'Yaeyama Islands' (Ishigaki, Iriomote, Yonaguni and neighbours; about 24-24.5 N 123-124.5 E): ryukyu-kingdom.
- Note: the gazetteer's {admin1: Okinawa} (region 'Ryukyu') resolves to a bbox reaching 28.37 N and 129.57 E, further north than Okinawa Prefecture; whoever maintains it should check whether Amami cells leaked in.

## Not settled

- Kume (and Kerama) in the Cliopatria Ryukyu shape: undated on the pages. Miyako is settled (see Fixes): 1500 with the Sakishima Islands.
- Amami: only Amami Ōshima is dated (1447); the other northern islands are drawn with it at confidence 2.
- No ruler strip for the Ryukyu Kingdom (the king table was not read in full).
- Capital coordinates for Urasoe, Nakijin, Ōzato and Shuri are approximate and not from a page.
- Ledger ordering in ashikaga-shogunate: the 1336 Kyushu contest has no month and so sorts before the 11 August found event.
- Validator pairing is by counterpart string only; the Kyushu and Yoshino contests both use 'southern-court' and end in start order (1385 then 1392), so the pairing is consistent.

## Fixes after review (2026-10-18, the fix pass for the review of jk-01-b)

Reviewer verdicts: chuzan fail, ryukyu-kingdom fail; hokuzan and nanzan thin; kenmu-restoration and ashikaga-shogunate fix (applied by the reviewer, not touched here). Pages re-opened with WebFetch: Chūzan, Ryukyu Kingdom, Miyako Islands (no history section, nothing usable), Sakishima Islands. Both dossiers validate with 0 errors.

chuzan
- Added vassal_start 1372 / vassal_end 1429, counterpart ming-dynasty, region the 1314 core, confidence 3, as the reviewer asked. Source: the Chūzan page ('The first Ming dynasty envoys arrived in Okinawa in 1372, marking the beginning of tributary relations with China'); the end cites the Ryukyu Kingdom infobox ('Tributary state of the Ming dynasty (1429–1644)'). Both are on the vassal side with the suzerain as counterpart, the elam to akkadian-empire pattern. Agreed with the reviewer; nothing disputed. The vassal region does not grow with the 1416 Hokuzan gain (the 1314 core as instructed); a renderer tinting the whole state should read the relation as the state's, not the core's.

ryukyu-kingdom
- Satsuma: vassal_start 1609-05 / vassal_end 1872-10, counterpart satsuma-domain (not tokugawa-shogunate: the infobox names Satsuma, and the contest and loss events already use it), region Okinawa + Miyako + Yaeyama (the Amami Islands pass outright in 1611). Year 1609 is the infobox's; month 5 is the fall of Shuri (Invasion page). The timeline puts the kings' vassalage in 1611; both dates are in the note.
- Domain of the Empire of Japan: vassal_start 1872-10 / vassal_end 1879-03, counterpart empire-of-japan (infobox 'Domain of the Empire of Japan (1872–1879)'). The rename of 1872 stays and points to it.
- Tributaries: ming-dynasty 1429-1644, southern-ming 1644-1646 (optional in the review, included because the infobox lists it), qing-dynasty 1646-1872, all confidence 3 except the Qing end (2). I disagree with nothing but note the page's own conflict: the infobox ends the Qing tribute in 1872, the body has the last tributary envoy in 1874 and Japan ordering the tribute to end in 1875. The infobox year is used.
- Miyako: took the reviewer's first option. The Ryukyu Kingdom page has no Miyako event but '1500: Sakishima Islands annexed by Ryukyu'; the Sakishima Islands page says they 'include the Miyako Islands and the Yaeyama Islands'. ryukyu-kingdom_1497 now removes Cliopatria's Miyako cell (1497-1499); the 1500 gain is union(Miyako Islands, Yaeyama Islands), confidence 2 (year the Ryukyu page's, the Miyako reading from the second page). The Sakishima page also has a Miyako chief paying tribute to Satto of Chūzan (Miyako unified 1365; tribute undated within Satto's reign 1350-1397): a tributary link before 1500, not recorded as an event because no page dates it to a year and it is not annexation. If a later reader wants it, it would be a vassal pair between chuzan and a Miyako counterpart ('nobody' has no vassal semantics).
- Gazetteer name added: 'Miyako Islands' (region; Miyako-jima, Irabu, Shimoji, Ikema, Tarama and neighbours, about 24.6-25.0 N 124.6-125.5 E).

Still thin, not done in this pass
- hokuzan and nanzan: no Ming vassal events. The Ryukyu Kingdom page's footnote now gives the years: 'Nanzan and Hokuzan also entered into tributary relationships with Ming China, in 1380 and 1383 respectively'. A vassal_start counterpart ming-dynasty at 1380 (nanzan) and 1383 (hokuzan) with vassal_end 1429 / 1416 (the Hokuzan conquest) can be added from that page; not applied because the verdicts were thin and the dossiers were not to be touched.
- chuzan: 80 km2 of the 1402 shape over the 1314 core is still unexplained (Sanzan period page not opened).
- ryukyu-kingdom: only Amami Ōshima is dated (1447); Kikai, Tokunoshima, Okinoerabu and Yoron undated (Amami Islands page not opened); no ruler strip (List of kings of Ryukyu not opened).
