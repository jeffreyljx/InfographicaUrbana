# Review of batch jk-01-x (Japan additions), 2026-10-19

Reviewer: adversarial reviewer jk-01-x. Machine copy: history/notes/phase-b/reviews/jk-01-x.json.
Validator (--resolve): 0 errors in all nine dossiers; 8 warnings, all southern-court's unknown place 'Yoshino'.
Spot checks: 4-9 events per dossier, all confidence-3 events in the sample confirmed on the page; no fabricated event found.
Area: none of these states has a Cliopatria shape, and no opened infobox (Republic of Ezo, Satsuma Domain, Matsumae Domain, Southern Court, Yamato polity, Emishi, Ainu people) gives an area.

## Verdicts

| slug | verdict | why |
| --- | --- | --- |
| emishi | thin | 6 events confirmed (709, 724, 758, 774-09, 802, 811). heian-japan's vassal_start emishi 850 / vassal_end 1051 not mirrored; 478 extent confidence 1; 802-1051 one shape. |
| abe-clan | pass | 1051-1062, Kuriyagawa, Koromo, Onikiribe, the six districts all on the pages. |
| yamato | thin | 350, 527, 528 confirmed (Iwai Rebellion page); 250 confirmed (Kofun period). Five confidence-1 events. Reviewer fixed /ledger/1 note (Yamato polity page calls Kibi 'an important ally', not a rival). Unapplied: /ledger/11 gain from 'nobody' should be from the vassals whose tints end the same year; vassal counterparts without dossiers should be explained in notes. |
| southern-court | thin | 1337-01, 1351, 1362, 1385, 1392-11 confirmed (Nanboku-chō page). Land is a Yoshino circle for 55 years; Kyushu Seiseifu (Prince Kaneyoshi, 1361-1372) not drawn. |
| minamoto-clan | thin | 1180-06, Fujigawa 9 Nov 1180, 1185-04, 1185-12 confirmed. One shape (Kanto + Kai) for 1180-1185; the 1183-1185 expansion is not drawn. |
| satsuma-domain | pass | 1600, 1609 (4 Mar, 7 Apr, 25 Apr, 5 May), 1871 confirmed; Kagoshima admin1 is mainland-only in the gazetteer, so Amami (1611, confidence 1) does not overlap the 1600 shape. |
| matsumae-domain | fix | Reviewer fixed /ledger/13 and identity.end month 7 to 8: 'July 14, 1871' on the Matsumae Domain page is the Japanese-calendar date; Abolition of the han system page: 'In August 1871 ... Imperial Edict'. Source added. Other checks (1590, 1672, 1789-05, 1855, 1868-12 x2) confirmed. |
| republic-of-ezo | fix | Reviewer added matsumae-domain to successors (Wajinchi, June 1869), mirroring matsumae-domain's 1869-06 gain (Matsumae Domain page: request to reinstate the domain 24 June 1869). Dates 3/18/28 Dec 1868, Apr 1869, 26-27 Jun 1869 confirmed. |
| ainu | fail | See below: three blocking ledger/keyframe contradictions. All nine spot-checked events confirmed on their pages. |

## ainu: blocking findings (back to the author)

1. /keyframe_review/4 and a missing 1822 event. Eastern Ezo (Tokugawa 1799 minus 1798: 129 cells, 32,624 km2) stays lost 1799-1854, but matsumae-domain /ledger/7 tints the Ainu of eastern Ezo again from 1822 and tokugawa-shogunate /ledger/8 loses it in 1822. From 1822 to 1854 no dossier holds the land. Fix: a 1822 gain from tokugawa-shogunate (confidence 1, mirror) and split KF4 at 1822.
2. /keyframe_review/5. KF5 (1855-1875) keeps all the Kurils, but tokugawa-shogunate /ledger/9 gains the southern Kurils in 1855 and its 1856 shape holds 13 Kuril cells (3,288 km2; intersect(Kuril Islands, Tokugawa Shogunate 1856), bbox 145.47-148.65 E, 43.8-45.38 N). Fix: a 1855 loss of that intersect to tokugawa-shogunate (Treaty of Shimoda page) and remove it from KF5.
3. /ledger/14. The 1869 loss of 'Hokkaido' to empire-of-japan loses land not held since 1855 (/ledger/13; KF5 is northern Sakhalin plus Kurils); empire-of-japan has no mirror. Fix: drop it into notes, or model 1855 as a tint and 1869 as the loss.

Non-blocking: mirror matsumae-domain's vassal_start/vassal_end ainu (1672, 1799, 1822, 1855) here; /ledger/1 counterpart 'yuan-dynasty' in 1264 predates the Yuan row (1294); use mongol-empire with a 1293/1294 handoff.

## Cross-dossier matrix (summary; full list in the JSON)

Matched: emishi 709/724/758/802 losses with asuka-japan, nara-japan, heian-japan gains; emishi to abe-clan 1051; yamato to asuka-japan 538; shimazu-clan to satsuma-domain 1600; satsuma-domain and ryukyu-kingdom 1609 vassalage, 1611 Amami, 1871/1872 vassal end; matsumae-domain and republic-of-ezo December 1868; republic-of-ezo to empire-of-japan June 1869; southern-court and ashikaga-shogunate contests (Kyushu 1336/1337, Yoshino 1337-1392).

Routed to sister dossiers (other jk-01 parts):
- heian-japan: counterpart strings 'Abe clan' and 'Minamoto clan' should be the slugs abe-clan and minamoto-clan; no 1180 loss to minamoto-clan (only a contest); vassal tint over emishi 850-1051 not mirrored in emishi.
- kamakura-shogunate: found counterpart and predecessors should include minamoto-clan.
- ashikaga-shogunate: no occupation events for the southern-court Kyoto occupations (1351-1352, 1362); no 1457 loss to ainu; 1459 regain from 'nobody' against ainu's 1458 loss; contest with southern-court opened in 1336 before the court exists.
- tokugawa-shogunate: 'nobody' as counterpart for the Ezo gains 1799, 1822, 1855, 1856 where ainu exists; no 1807 Sakhalin gain; 1609/1611 Ryukyu events duplicate satsuma-domain's.
- empire-of-japan: no 1868-12 loss to republic-of-ezo (contest from 1869-01 instead); gains all Ezo including the Wajinchi in 1869-06 while matsumae-domain regains the Wajinchi; Kurils at 1877 against the 1875 treaty; nothing for the 1871 end of satsuma-domain and matsumae-domain.
- warring-states-japan: no handover of the Wajinchi to matsumae-domain in 1590.

## Design question for the orchestrator

satsuma-domain and matsumae-domain are han inside the Tokugawa realm (and inside empire-of-japan 1868-1871), typed 'state' with no recorded relation to the suzerain, so their cells are claimed twice. The schema has no internal-unit type: either the suzerain dossiers record a vassal (sub-unit) relation for each han, or the renderer draws han only as sub-units.

## Gazetteer names needed

Yoshino (place, southern-court); Oshima Peninsula (region, would replace the Wajinchi polygon in matsumae-domain, ainu, republic-of-ezo); Amami Islands (region, satsuma-domain); Miyakonojo, Matsumae, Esashi (places; coordinate circles used now).

## Thin items for gap-fillers

- emishi: 802-811 northward advance (Isawa, Shiwa castles): Isawa_Castle. 478 extent: Mutsu_Province.
- yamato: 425 Kawachi move (Kawachi_Province), 450 eastern reach (Inariyama_Sword), 528 Kibi (Kibi_Province).
- southern-court: Kyushu Seiseifu and other strongholds (Prince_Kaneyoshi); 1352 recovery of Kyoto (Kannō_disturbance).
- minamoto-clan: 1183-1185 expansion (Battle_of_Ichi-no-Tani); Yoshinaka (Minamoto_no_Yoshinaka).
- satsuma-domain: Amami 1611 year (Amami_Islands); ruler 1600-1602.
- matsumae-domain: 1807-1821 relocation and Hakodate bugyō direct rule (Hakodate_bugyō, Matsumae_clan); 1822 return.
- republic-of-ezo: extent beyond the three towns (Battle_of_Hakodate).
- ainu: Russian northern Kurils, Shimoda 1855 (Treaty_of_Shimoda), 1807 western Ezo (Ezo).

## Pages

Opened by the reviewer (2026-10-19): Emishi, Thirty-Eight Years' War, Former Nine Years' War, Abe no Yoritoki, Iwai Rebellion, Kofun period, Yamato polity, Nanboku-chō period, Southern Court, Genpei War, Battle of Fujigawa, Invasion of Ryukyu, Satsuma Domain, Matsumae Domain, Republic of Ezo, Ainu people, History of Hokkaido, Koshamain, Shakushain's revolt, Menashi–Kunashir rebellion, Abolition of the han system. Two URL spellings failed once and loaded with the other spelling.
