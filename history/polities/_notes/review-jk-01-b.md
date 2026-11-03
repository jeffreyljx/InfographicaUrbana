# Review: batch jk-01-b (Japan, part b), Phase B, 2026-10-18

Reviewer: adversarial review pass. Six dossiers: chuzan, hokuzan, nanzan, kenmu-restoration, ashikaga-shogunate, ryukyu-kingdom. Validator (--resolve): 0 errors in all six; warnings are unknown counterparts southern-court and satsuma-domain (listed by the author) and gazetteer misses Yoshino, Amami Islands, Yaeyama Islands. The one Context polity (warring-states-japan) has no dossier yet (group jk-01, part not run), so its side of the cross-checks is an exception. kamakura-shogunate and shunten-dynasty dossiers exist and were grepped for the mirror events.

Pages re-opened by the reviewer: Chūzan, Hokuzan, Nanzan, Kenmu Restoration, Nanboku-chō period, Ashikaga shogunate (twice), Ōnin War, Ryukyu Kingdom, Invasion of Ryukyu. No page failed. No infobox gives an area, so no area ratio could be computed for any dossier (the author said so in every keyframe note).

## Verdicts

| slug | verdict | why |
| --- | --- | --- |
| chuzan | fail | Ming tributary relation of 1372 (dated on the Hokuzan and Nanzan pages, and quoted in the dossier's own ruler note) is not in the ledger |
| hokuzan | thin | border moves all explained; Ming tributary status 'shortly afterwards' has no year on the page |
| nanzan | thin | border moves all explained; Ming tributary status has no clean start year (Ofusato at the Ming court in 1388) |
| kenmu-restoration | fix (applied by reviewer) | contest_end confidence 3 to 2; Genkō War clipped to the regime's life |
| ashikaga-shogunate | fix (applied by reviewer) | 1468 loss confidence 2 to 1 (no page gives 1468); three confidence-1 events listed as thin |
| ryukyu-kingdom | fail | no vassal events for the Satsuma vassalage 1609-1872, the Japanese domain 1872-1879, or the Ming/Qing tributary status, all on the infobox; Miyako drawn from 1497 although the page annexes the Sakishima Islands in 1500 |

## chuzan: fail

Blocking:
- /ledger (after /ledger/1): missing vassal_start / vassal_end for the Ming tributary relation. Hokuzan page and Nanzan page: 'Chūzan entered a tributary relationship with Ming dynasty China in 1372'; the dossier's own /identity/rulers/2/note: 'The first Ming envoys arrived in 1372, which began tributary relations with China'. The schema counts a tributary as a vassal (rule 4) and the project's dossiers record the mirror on the vassal side (elam to akkadian-empire, babylonia to assyria, odrysian-kingdom to macedonian-empire). Fix: add `vassal_start` 1372, counterpart `ming-dynasty`, region `{"cliopatria": "Chüzan", "year": 1314}`, confidence 3, source the Hokuzan (or Chūzan) page; and `vassal_end` 1429, counterpart `ming-dynasty`, note 'the relation passes to the Ryukyu Kingdom'. (Ming's Cliopatria row starts 1375; the vassal_start can stay at 1372 with a note.)

Spot checks (all confirmed): /ledger/4 1416 gain (Hokuzan page: Hananchi 'conquered by Shō Hashi, King of Chūzan in 1416'); /ledger/7 1429 gain (Nanzan page: 'Shō Hashi ... seized the opportunity to take Nanzan', 'Nanzan in 1429'); /ledger/9 1429 dissolve (Chūzan infobox 'Ryukyuan unification: 1429', 'Succeeded by: Ryukyu Kingdom'); /ledger/1 1350 rename (Chūzan king table Satto 1350-1397; infobox 1355-1397, Seii overthrown 'around 1349-1355').

Not faults: the Chūzan page does mention 'the political capital at Shuri' (the dossier notes say it does not); the Ryukyu Kingdom timeline puts the move in 1429, so Urasoe to 1429 stands. The 80 km2 of the 1402 shape over the 1314 core is within one grid cell (thin by design).

## hokuzan: thin

No fault found. Tried: found 1314 (page: 'Hokuzan first came into being in 1314'), the 1416 contest and dissolve (page: 'conquered Hokuzan in 1416', 'Nakijin castle fell, and the king and his closest vassals committed suicide'), the end year against the Chūzan page (1419; flagged by the author), capital Nakijin inside the shape's bbox, the mirror in chuzan (/ledger/4 gain 1416) and shunten-dynasty (split 1314).
Thin: the Ming tributary relation. Hokuzan page: 'Hokuzan and Nanzan were granted similar commercial status shortly afterwards' (after 1372), 'only nine tribute missions were sent from Hokuzan to China'; no year. A vassal_start counterpart ming-dynasty at confidence 1 or a page with the first Hokuzan mission year is wanted (try https://en.wikipedia.org/wiki/Sanzan_period).

## nanzan: thin

No fault found. Tried: found 1314, the end in 1429 against Cliopatria's 1401 (page: no absorption before 1429; 'Ryukyu unification: 1429'), the contest events, capital inside the shape, mirrors in chuzan and shunten-dynasty.
Cross-check note: chuzan /ledger/7 gains Nanzan from nanzan in 1429, while nanzan /ledger/3 dissolves with counterpart ryukyu-kingdom and successor ryukyu-kingdom (Nanzan infobox 'Succeeded by: Ryūkyū Kingdom'). Chūzan itself dissolves into ryukyu-kingdom the same year, so the land ends in the same place; recorded as an exception, no change required. If the authors want the trio uniform, hokuzan's pattern (dissolve counterpart chuzan) is the model.
Thin: the Ming tributary relation. Nanzan page: 'Nanzan was granted similar commercial status shortly afterwards' (after 1372); 'Ofusato ... presented himself to the Chinese Imperial Court in 1388'; Taromai invested in 1415. A vassal_start counterpart ming-dynasty (1388 at confidence 2, or an earlier year from another page) to 1429 is wanted.

## kenmu-restoration: fix (applied by the reviewer)

Applied:
- /ledger/3 confidence 3 to 2. The page: 'On February 25, 1336, Ashikaga Takauji entered the capital and the Kenmu Restoration ended' names the capital, not the Kantō half of the zone union(Kanto, Kansai).
- /wars/0/from 1331 to 1333. The war began before the regime's life (start 1333-05); the infobox gives 'Genkō War begins: 1333' and the kamakura-shogunate dossier carries the 1331-1333 contest. Note appended.

Spot checks (all confirmed): /ledger/3 (sentence above); /ledger/2 ('On November 17, 1335, Tadayoshi issued a message in his brother's name asking all samurai to join the Ashikaga'; the dossier's 'the page does not say what the message ordered' undersells the page but the reading is right); /ledger/0 (infobox 'Siege of Kamakura: May 18, 1333'; 'When the Hōjō garrison at Rokuhara was destroyed in 1333'); /ledger/4 ('ultimately overthrown when Takauji became Shōgun and founded the Ashikaga Shogunate in 1336').
Mirrors: kamakura-shogunate /ledger/13 dissolve 1333-05 counterpart kenmu-restoration (matched); ashikaga-shogunate /ledger/2 gain 1336-08 from kenmu-restoration (matched). The 1335-36 contest names ashikaga-shogunate before that dossier's start (1336-08); accepted as the Ashikaga party, no mirror expected.
Thin by design: the 320,516 km2 outline is the realm claimed; the Kantō rising of 1335 (Hōjō Tokiyuki) is in a note only.

## ashikaga-shogunate: fix (applied by the reviewer)

Applied:
- /ledger/8 confidence 2 to 1. Neither the Ashikaga shogunate page ('does not mention 1468'; Ōnin War '1467-1477') nor the Ōnin War page (its only 1468 event is Yoshimi changing sides) gives 1468; the year is Cliopatria's, as the note itself says. Note appended.

Spot checks (all confirmed): /ledger/3 (Nanboku-chō: 'Go-Daigo escaped from the capital in January 1337 ... set up the Southern Court among the mountains of Yoshino'); /ledger/4 ('imperial resistance collapsed with the defeat of the Kikuchi clan in 1381'; 1385 'the last Kyūshū provincial domain declared its allegiance to the regime'); /ledger/5 ('On November 19, 1392, Emperor Go-Kameyama renounced the Japanese Imperial Treasures'); /ledger/9 (Ōnin War: Ōuchi Masahiro 'left the area on 17 December 1477'); /ledger/10 (infobox 'Ashikaga shogunate abolished: 2 September 1573'; 'finally destroyed in 1573 when Nobunaga drove Yoshiaki out of Kyoto'); /ledger/7 ('Then in May 1467, a Yamana mansion was attacked').
Thin (confidence 1 or uncovered): /ledger/2 (1336 gain of the whole Kenmu realm; the page gives no extent); /ledger/6 (1459 Dōnan gain; Koshamain page does not tie the land to the shogunate); /ledger/8 (1468 loss, year from Cliopatria); the Kantō under the Kamakura-fu and Kyushu under the Tandai are not on any page opened; the Ming investiture of Yoshimitsu (1402-1549 tally trade) is not on the Ashikaga page, and whether Japan is drawn as a Ming tributary is a project-level call.
Routing: /ledger/7 is a contest with warring-states-japan from May 1467, a year before that polity's Cliopatria start (1468); the warring-states-japan author must start at 1467 or carry the matching contest, and must carry the 1468 gain and the 1573 takeover of the Kyoto remnant.
Accepted: /ledger/0 (Kyushu contest 1336, no month, sorts before the August found event; Tatarahama 1336 is on the page; counterpart southern-court is dated 1337-1392 in the author's report, so the counterpart dossier should begin with Go-Daigo's loyalists in 1336 or the event should move to 1337). Rulers have real interregna (1357-59, 1425-28, 1443-49, 1565-68).

## ryukyu-kingdom: fail

Blocking:
1. /ledger (after /ledger/6): no vassal_start / vassal_end for the Satsuma vassalage. Ryukyu Kingdom infobox: 'Vassal state of the Satsuma Domain (1609–1872)'; body: 'The Ryukyu Kingdom became a vassal state of the Satsuma Domain of Japan after the invasion of Ryukyu in 1609'; timeline 1611: 'Kings of Ryukyu become vassals to the daimyō of the Satsuma Domain'; Invasion of Ryukyu infobox: 'Territorial changes: Ryukyu becomes a vassal state'. The author routed it to a satsuma-domain dossier that does not exist (and jk-01-x's scope treats the Edo han as internal units, so it may never be written). Fix: add `vassal_start` 1609 (month 5, the fall of Shuri) or 1611 (the surrender documents), counterpart `satsuma-domain` (or `tokugawa-shogunate`, whichever the group settles; say which in the note), region `{"union": [{"cliopatria": "Ryukyu Kingdom", "year": 1519}, {"region": "Yaeyama Islands"}]}`, confidence 3, source the Ryukyu Kingdom page; `vassal_end` 1872-10 with the same counterpart.
2. /ledger (after /ledger/8): the 1872-1879 status 'Domain of the Empire of Japan (1872–1879)' (infobox) is only a rename. Fix: `vassal_start` 1872-10 counterpart `empire-of-japan`, `vassal_end` 1879-03 counterpart `empire-of-japan`, same region, source the Ryukyu Kingdom page.
3. /ledger (from /ledger/0): no tributary events for 'Tributary state of the Ming dynasty (1429–1644)', 'Tributary state of the Southern Ming (1644–1646)', 'Tributary state of the Qing dynasty (1646–1872)' (infobox). Fix: vassal_start/vassal_end pairs with counterparts `ming-dynasty` (1429-1644), `southern-ming` (1644-1646, optional) and `qing-dynasty` (1646-1872), confidence 3. If the project decides tributaries of the Ming are not drawn, the orchestrator should say so for all Sinosphere dossiers; until then the infobox status is data the dossier must carry.
4. /keyframe_review/2 and /ledger/4: the 1497 keyframe keeps Cliopatria's Miyako cell from 1497 with the note 'The page gives no conquest or submission date for Miyako', but the page's timeline reads '1500 – Sakishima Islands annexed by Ryukyu', and the Sakishima Islands are the Miyako and Yaeyama groups. Fix: either correct ryukyu-kingdom_1497 (1497-1499) to the 1429 outline plus Amami without the Miyako cell and make the 1500 gain region the Sakishima Islands (Miyako plus Yaeyama), or keep Miyako from 1497 on another page that dates it and say why the 1500 entry does not cover it.

Spot checks (all confirmed): /ledger/2 ('In 1447, King Shō Shitatsu conquered Amami Oshima'); /ledger/5 ('The Satsuma fleet arrived at Amami Ōshima on April 7'); /ledger/6 ('On May 4, Shō Nei left Shuri Castle, and on May 5, some Satsuma officers entered the castle'); /ledger/7 (timeline 1611 'Satsuma annexes the Amami and Tokara Islands'); /ledger/8 (infobox 'Reorganized into Ryukyu Domain: 16 October 1872'); /ledger/9 (body 27 March 1879, infobox 4 April 1879); /ledger/1 (timeline 'Shō Hashi moves the capital to Shuri Castle'); /ledger/4 confirmed for the year and Yaeyama, incomplete for Miyako (finding 4).
Thin: Kume and the Amami islands other than Amami Ōshima are undated (flagged by the author); no ruler strip.

## Cross-dossier matrix

| event | mirror | status |
| --- | --- | --- |
| chuzan 1314 found from shunten-dynasty | shunten-dynasty 1314 dissolve to chuzan | matched |
| hokuzan 1314 found from shunten-dynasty | shunten-dynasty 1314 split hokuzan | matched |
| nanzan 1314 found from shunten-dynasty | shunten-dynasty 1314 split nanzan | matched |
| chuzan 1416 gain from hokuzan | hokuzan 1416 dissolve, counterpart and successor chuzan | matched |
| chuzan 1429 gain from nanzan | nanzan 1429 dissolve, counterpart ryukyu-kingdom | exception (same-year handover through chuzan to ryukyu-kingdom) |
| chuzan 1429 dissolve to ryukyu-kingdom | ryukyu-kingdom 1429 found from chuzan | matched |
| kenmu-restoration 1333-05 gain from kamakura-shogunate | kamakura-shogunate 1333-05 dissolve to kenmu-restoration | matched |
| kenmu-restoration 1336-02 dissolve to ashikaga-shogunate | ashikaga-shogunate 1336-08 gain from kenmu-restoration | matched |
| ashikaga-shogunate 1459 gain from nobody | - | exception (nobody) |
| ashikaga-shogunate 1468 loss to warring-states-japan | no dossier | exception (group jk-01 part not run) |
| ashikaga-shogunate 1573 dissolve to warring-states-japan | no dossier | exception (group jk-01 part not run) |
| ashikaga-shogunate 1336-1392 contests with southern-court | no dossier | exception (author's counterparts_needing_dossiers) |
| ryukyu-kingdom 1447, 1500 gains from nobody | - | exception (nobody) |
| ryukyu-kingdom 1611 loss to satsuma-domain | no dossier | exception (author's counterparts_needing_dossiers) |
| ryukyu-kingdom 1879 dissolve to empire-of-japan | no dossier | exception (group jk-01 part not run) |
| ryukyu-kingdom vassal of satsuma-domain 1609-1872 | neither side | missing |
| ryukyu-kingdom domain of empire-of-japan 1872-1879 | neither side | missing |
| ryukyu-kingdom tributary of ming-dynasty / qing-dynasty | neither side | missing |
| chuzan tributary of ming-dynasty 1372-1429 | neither side | missing |
| hokuzan, nanzan tributaries of ming-dynasty | neither side, undated | missing (thin) |

## Gazetteer names needed

Yoshino (place; ashikaga-shogunate, kenmu-restoration), Amami Islands (region; ryukyu-kingdom), Yaeyama Islands (region; ryukyu-kingdom); and, if finding 4 is taken, Sakishima Islands or Miyako Islands (region; ryukyu-kingdom).
