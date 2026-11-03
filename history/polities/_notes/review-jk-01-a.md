# Review: batch jk-01-a (Japan, part a) — 2026-10-18

Reviewer: adversarial review per history/briefs/reviewer-brief.md, with the orchestrator's adjustments (budget-aware thin, 4 spot checks per dossier, small verified fixes applied in place). Validator: 0 errors on all six before and after the reviewer's edits. No Context polities; no counterpart dossier (emishi, yamato, mongol-empire, kenmu-restoration, chuzan, hokuzan, nanzan) exists yet, so cross-checks are among the six dossiers. Pages opened (14): Asuka period, Emishi, Nara period, Thirty-Eight Years' War, Heian period, Toi invasion, Former Nine Years' War, Genpei War, Northern Fujiwara, Gosannen War, Kamakura shogunate, Mongol invasions of Japan, Shunten dynasty, Eiso dynasty. None of the six pages carries an infobox area.

| slug | verdict | blocking (author) | applied by reviewer |
| --- | --- | --- | --- |
| asuka-japan | pass | none (advisory: dissolve region, follows Nara) | none |
| nara-japan | fail | Akita foothold dropped in 710 | /wars/2/to 811 -> 794 |
| heian-japan | fail | Miyagi and Akita missing at the start; Genpei contest zones | /wars/0/from 774 -> 794 |
| northern-fujiwara | fix | none | /wars/0/from 1083 -> 1087 |
| kamakura-shogunate | fail | Mongol contest blended 1275-1280 | ruler sources; /keyframe_review/0 text |
| shunten-dynasty | fix | none | /ledger/0 counterpart 'Tenson dynasty' |

## Blocking findings (author to fix)

1. **nara-japan /keyframe_review/0 and /ledger/0/region — the Akita foothold vanishes in 710.** asuka /ledger/2 gains {place: Akita, km: 50} in 709 (Emishi page: 'In 709, the fort of Ideha was created close to present day Akita'; 'the intervening territory between Akita and the northwestern countries of Japan was not under government control'). The gazetteer puts 0 of that circle's 21 cells inside the Nara 710 or Heian 793/800/814 shapes (all 21 are inside the Northern Fujiwara 1094 shape). Asuka dissolves with the 705 shape only, Nara founds on its 710 shape with KF0 'ok', and no event loses Akita. Fix: KF0 to adjust with {"union": [{"cliopatria": "Nara Japan", "year": 710}, {"place": "Akita", "km": 50}]}, same union in Nara /ledger/0/region and Asuka /ledger/3/region (and /identity/successors/0/land); or a dated loss with a page (Akita Castle 733 says it was kept: https://en.wikipedia.org/wiki/Akita_Castle).
2. **heian-japan /keyframe_review/0-2 and /ledger/0/region — Nara's northern land is missing at the start.** 29 of Miyagi's 32 cells lie outside the Heian 793 and 800 shapes (26 are inside 814). The 794 contest zone covers them to 811, but in 811-813 the Sendai plain and Taga are in no shape and no event. Akita is outside every Heian shape before the 1062 keyframe. Fix: add {"admin1": "Miyagi", "country": "Japan"} to KF0, KF1 and /ledger/0/region; add {"place": "Akita", "km": 50} to KF0, KF1, KF2 and /ledger/0/region (unless Nara records a loss).
3. **heian-japan /ledger/13, /ledger/16, /wars/6/zones — the Genpei contest pair has two different zones.** contest_start 1180 names Kanto + Yamanashi; contest_end April 1185 names Chugoku + Shikoku + Kyushu. Pairing is by counterpart only, so the eastern blend never closes and the western theatre (1183: Munemori took Antoku 'to the west'; 'a temporary Court at Dazaifu'; Yashima) is never opened. The counterpart kamakura-shogunate starts in December 1185, so it cannot hold a mirror, and the Minamoto held the Kantō for over four years (Genpei page: 'June 20, 1180 – April 25, 1185'; Yoritomo 'made it to the provinces of Kai and Kōzuke'), which the research brief treats as a land-holding rebel. Fix: one zone per pair (east 1180-06 to its end; west 1183-07 to 1185-04 with its own counterpart string, e.g. 'Taira clan (western court)'); and either begin kamakura-shogunate in 1180 with the Kantō as its found region (its own /ledger/0 note: 'Yoritomo had risen at Kamakura in 1180') and record the mirrors, or use the name 'Minamoto clan' as counterpart and list it under counterparts_needing_dossiers as a rebel state 1180-1185.
4. **kamakura-shogunate /ledger/9-10 — Mongol contest drawn 1274-11 to 1281-08.** The page dates the landings (Tsushima from 4 November 1274, Hakata 19 November 1274; Tsushima 9 June 1281, Iki 14 June 1281, typhoon 15 August 1281) and says nothing of holding either island in between; the dossier's own war note says they were 'overrun in both invasions for days'. Fix: two pairs, 1274-11 to 1274-11 and 1281-06 to 1281-08, same zone and counterpart.

## Non-blocking findings (author's choice)

- **Northern Fujiwara vassal tint (heian /ledger/12, /ledger/17; kamakura /ledger/1, /ledger/4).** Confidence 1, and the cited page says the opposite ('keep their independence vis-à-vis Kyoto by the strength of their warrior bands'). northern-fujiwara has no mirror vassal events. Either source it (Hidehira as Chinjufu-shōgun and governor of Mutsu: https://en.wikipedia.org/wiki/Fujiwara_no_Hidehira) and add vassal_start/vassal_end with heian-japan and kamakura-shogunate to northern-fujiwara, or delete the pairs. kamakura /ledger/4 is confidence 3 for the end of a confidence-1 relation.
- **Heian end vs Kamakura start months.** Heian ends 1185-04 and Kamakura begins 1185-12, which leaves eight months with neither state. Align them, and decide this together with blocking item 3.
- **Kamakura rulers are not contiguous.** There is no shogun for 1185-1192, 1199-1202 or 1219-1226, yet the page lists the shikken regents from 1203. Note the gaps, or fill them.
- **Kenmu counterpart.** kenmu-restoration (Cliopatria from 1333) cannot carry a 1331 contest_start unless that dossier begins in 1331. This is for the jk-01 part that writes it.
- **Heian 1062-1086 direct rule (/ledger/10, /keyframe_review/3).** This is confidence 2 over the whole Northern Fujiwara shape, but the Former Nine Years' War page gives only 'Imperial victory' and no territorial change. Consider the Kiyohara as a vassal tint, as in 850-1051 (https://en.wikipedia.org/wiki/Kiyohara_clan).

## Applied by the reviewer (re-validated, 0 errors)

- nara-japan /wars/2/to: 811 -> 794. heian-japan /wars/0/from: 774 -> 794. northern-fujiwara /wars/0/from: 1083 -> 1087. Wars must lie inside the life (brief check 2); the full spans are kept in each war's note.
- kamakura-shogunate /identity/rulers/1..8: added source https://en.wikipedia.org/wiki/Kamakura_shogunate. The page's list ('Minamoto no Yoriie, r. 1202–1203' ... 'Prince Morikuni, r. 1308–1333') matches every entry.
- kamakura-shogunate /keyframe_review/0/correction/text: 'holds from December 1185 to 1188' -> 'to September 1189' (Hiraizumi entered 3 October 1189).
- shunten-dynasty /ledger/0/counterpart: 'tenson-dynasty' -> 'Tenson dynasty'. The line is legendary and no dossier is planned, so the source's name is used (clears the validator warning).

## Spot checks (all dates confirmed on the pages)

- **Asuka:** 538, 694, 709 (Ideha), 710.
- **Nara:** 710, 724 (Taga), 758 (Momonofu), 5 September 774 (Monou), 784.
- **Heian:** 802, 811, 27 March to 20 May 1019 (Toi), 1062 (Kuriyagawa), 25 April 1185. The 1087 vassal claim is not on the page.
- **Northern Fujiwara:** 1087; 1 September, 2-3 October and 14 October 1189; Gosannen 1083-1089 (disputed).
- **Kamakura:** December 1185, 21 August 1192, 2-4 November 1274, 15 August 1281, 1331, 18 May 1333, the shogun list.
- **Shunten:** 1187, 1259, 1314, the reign tables.

## Thin (by budget; for a gap-filler)

- **Asuka:** the 6th-century northern limit and the Hayato; Tsushima and Iki outside the shapes.
- **Nara:** Dewa 712, Akita Castle 733, the Hayato 720.
- **Heian:** the c. 850 vassal tint (c1); Northern Fujiwara titles (c1); the Kiyohara six districts; the Shiwa and Isawa castles.
- **Northern Fujiwara:** the southern limit against 'Mutsu and Dewa' (Cliopatria 38.67 N); reign years.
- **Kamakura:** Ezo and the Andō; Rokuhara; the 1221 confiscations.
- **Shunten:** the extent beyond Urasoe (2,186 km2 shape against Okinawa Island's ~1,207 km2, acknowledged); the 1264/1266 tribute.

## Gazetteer

Neither 'Tsushima' nor 'Iki' resolves (the validator reports only Tsushima, but 'Iki' also fails: "unknown region 'Iki'"). Both are used in heian-japan and kamakura-shogunate.
