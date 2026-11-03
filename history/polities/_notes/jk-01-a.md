# Notes: group jk-01-a (Japan, part a) — 2026-10-18

Six dossiers: asuka-japan, nara-japan, heian-japan, northern-fujiwara, kamakura-shogunate, shunten-dynasty. Fourteen pages opened; all six validate with 0 errors. Pages per state: Asuka 2, Nara 2 (+1 shared), Heian 5 (+2 shared), Northern Fujiwara 2, Kamakura 2 (+2 shared), Shunten 2.

## Conventions used across the group
- Transition years follow the pages, not Cliopatria: Asuka 538-710, Nara 710-794, Heian 794-1185, Kamakura 1185-1333, Northern Fujiwara 1087-1189, Shunten/Eiso 1187-1314. Each successor's `found` falls in the predecessor's `dissolve` year (one-year overlap, as the Tang example does for 907).
- Counterpart `emishi` (no Cliopatria row) carries every frontier gain and the Thirty-Eight Years' War contest in Asuka, Nara and Heian, and the c. 850-1051 vassal tint over the northern Emishi domains in Heian. Either jk-01-x writes an `emishi` dossier or the renderer reads these as from nobody.
- Counterpart `yamato` (Asuka's predecessor, before 540) is assumed for the jk-01-x Yamato dossier; reconcile the slug.
- `Tsushima` and `Iki` are used as `{"region": ...}` names the gazetteer lacks: Tsushima Province (island, 129.3 E 34.4 N, ~700 km2) and Iki Province (island, 129.7 E 33.8 N, ~140 km2). Tsushima lies outside the bbox of every Asuka, Nara and Heian shape; it is added to all Heian keyframes on the Toi invasion page's 'Tsushima and Iki provinces' (1019) and noted (not corrected) for Asuka and Nara.

## asuka-japan
- Cliopatria 540-709 vs page 538-710: new keyframe 538-539; 705 shape extended to 710. The 705 break is unexplained (identical area).
- Northern limit (38.2 N) is generous for the 6th century; forts on the Sendai plain date from 724 (Emishi page). Unverified beyond budget.
- Not on pages: Hayato, Naniwa/Ōmi courts, Abe no Hirafu's 659-660 voyages, the provinces of the Taika and Taihō systems.

## nara-japan
- Cliopatria 710-792 vs page 710-794; 788 break unexplained.
- Not on pages: Hayato rebellion 720, Dewa 712, Akita Castle 733, Azamaro's 780 revolt (only 'Even Taga Castle was not spared'), planned Silla expedition, island tribute.

## heian-japan
- Cliopatria 793-1187 vs page 794-1185. 814 shape: the step is Aterui's 802 surrender (Isawa added as a 40 km radius on Hiraizumi; Shiwa castle 803 is not on the pages). 800 and 1177 breaks unexplained.
- Northern story is a reading of thin pages: Emishi domains as vassal tint c. 850-1051 (confidence 1); Former Nine Years' War contest 1051-1062 with the Abe clan; new keyframe 1062-1086 with the Abe lands direct (confidence 2); Northern Fujiwara loss 1087 (the vassal tint 1087-1185 was removed in the review fix, see below).
- Genpei War: now two contest pairs, east (Kantō, Yamanashi) 1180-1185 against 'Minamoto clan' and west (Chūgoku, Shikoku, Kyūshū) 1183-1185 against 'Taira clan (western court)'; neither counterpart has a dossier yet (see the review fix).
- Not on pages: Gangyō 878, Masakado 939-940 (under a year; no rebel dossier), Sumitomo (undated), Isawa/Shiwa castles, Hiraizumi move. Disagreement: Heiji Rebellion 1159 (page) vs 1160 (usual).

## northern-fujiwara
- Cliopatria 1094-1191 vs page 1087-1189: new keyframe 1087-1093; 1188 shape cut to October 1189. The lead's '1094–1104' span is unexplained.
- Southern limit: the page says they ruled Mutsu and Dewa provinces (which reach the Sendai plain and Shōnai) while Cliopatria stops them at ~38.7 N; unverified: page budget.
- No reign years on the page: no ruler strip. Abe (to 1062) and Kiyohara (1062-1087) have no row; a gap-filler may prefer state dossiers (slugs abe-clan, kiyohara-clan).
- Gosannen War page gives dates 1083-1089 (disputed), stalemate; nothing on Kiyohira's succession.

## kamakura-shogunate
- Cliopatria 1188-1332 vs pages 1185 (or 1192)-May 1333; Ōshū step is October 1189, not 1192; 1326 break unexplained (regency change). 1188 shape is 13% larger than Heian's last (islands, coastline), no conquest.
- Mongol counterpart is `mongol-empire` (Cliopatria row to 1293) though the page names the Yuan dynasty; contest over Tsushima, Iki, Hakata in two short pairs (1274-11; 1281-06 to 1281-08). Jōkyū 1221: one-year contest over Kansai with 'Retired Emperor Go-Toba (Kyoto court)' as a named counterpart. Genkō War counterpart kenmu-restoration should carry the matching 1331-1333 contest.
- Not on pages: Rokuhara/Chinzei deputies, 1221 confiscations, Ezo and the Andō, third Mongol invasion, Yoritomo at Kamakura 1180.

## shunten-dynasty
- One dossier for Shunten (1187-1259) and Eiso (1259-) lines, ending 1314 at the Sanzan split because Cliopatria's 'Chüzan' row (slug chuzan, 1314-1428; note the ü) carries the last Eiso kings. The chuzan dossier (another jk-01 part) should link shunten-dynasty as predecessor and treat Satto's 1350 accession as a rename.
- Eiso's accession: 1259 (dynasty), 1260 (king table), c. 1261 ('seven years' after c. 1254) on the Eiso page.
- Urasoe as capital is a reading (lord of Urasoe; Satto 'Governor of Urasoe'). Shape 2,186 km2 vs Okinawa Island ~1,200 km2; extent unverified ('paramount chiefs').
- Not on pages: 1264 Kumejima/Kerama/Iheya and 1266 Amami tribute, Tomari office, Yuan contacts 1291/1296. Tenson predecessor is legendary (slug tenson-dynasty used, no dossier planned).

## Pages
- Failed once: https://en.wikipedia.org/wiki/Thirty-Eight_Years%27_War (URL_NOT_FOUND); the same title with a literal apostrophe loaded and is the URL cited.

## Review fix (jk-01-a-fixed, 2026-10-18)
Pages re-opened: Akita Castle (new), Emishi, Genpei War, Fujiwara no Hidehira (new), Mongol invasions of Japan, Kamakura shogunate. Touched: nara-japan, heian-japan, kamakura-shogunate; all validate with 0 errors. Asuka (pass), Northern Fujiwara (fix) and Shunten (fix) were not touched.

### Changed
- nara-japan: /keyframe_review/0 ok -> adjust with {union: Nara 710 + Akita 50 km}; same union in /ledger/0/region; /keyframe_review/1 (788), the dissolve region (plus Miyagi) and the predecessor/successor land carry the foothold too. Pages: Emishi 'In 709, the fort of Ideha was created close to present day Akita' (no loss on the page); Akita Castle 'In 733, the fort on the Mogami River was moved north', abolition 'decided ... in 770 but withdrew ... ten years later', abandoned c. 1050. Dewa Country dates to 708 on that page, not 712.
- heian-japan: Miyagi and Akita added to /keyframe_review/0 and /1 and to /ledger/0/region (Akita only to /keyframe_review/2), predecessor land likewise. Genpei: east pair 1180 to 1185-04 with 'Minamoto clan'; new west pair 1183 to 1185-04 with 'Taira clan (western court)'; /wars/6 has both zones and three belligerents. Vassal pair over the Northern Fujiwara (1087-1185) deleted. Dissolve and identity.end moved to 1185-12 (the Genpei page's December 1185 grant) so that Heian and Kamakura abut; KF5 text follows.
- kamakura-shogunate: Mongol contest split into 1274-11 (start and end) and 1281-06 to 1281-08, same zone; vassal pair over the Northern Fujiwara (1185-12 to 1189-10) deleted; the unsourced 'risen at Kamakura in 1180' removed from /ledger/0; shogun gaps (1185-1192, 1199-1202, 1219-1226) noted on the rulers.

### Disagreements and choices (with the page)
- No month for the Genpei pairs. The reviewer proposed 1180-06 and 1183-07; the Genpei page gives 'June 20, 1180' only as the war's start (infobox), dates the eastern campaign ('made it to the provinces of Kai and Kōzuke') to 1180 and says the war 'resume[d] in the spring of 1183'; it gives no month for the Taira leaving Kyoto, Kamakura or the Juei edict. Years only.
- The east pair stays open to April 1185 although 'For nearly two years, the war ceased' (1181-1183): the Kantō stayed Minamoto land and the page gives 'Minamoto clan victory' in 1185; the blend is the stand-in for a rebel-held Kantō until a 'Minamoto clan' dossier exists. If one is written, replace the pair with loss/gain events.
- Vassal tint over the Northern Fujiwara deleted, not sourced. The Hidehira page: 'official imperial governor for Mutsu Province as of 1181' but 'controlled his territory independently of the central government'; no Chinjufu-shōgun, tribute or submission. The Northern Fujiwara page: 'keep their independence vis-à-vis Kyoto'. No mirror events in northern-fujiwara are therefore needed.
- Kamakura not started in 1180: the Kamakura page does not mention 1180 ('the prevailing theory was that the year was 1185'), so the Kantō 1180-1185 goes to a 'Minamoto clan' counterpart dossier.
- Asuka not touched (verdict pass): its /ledger/3/region and /identity/successors/0/land still name the 705 shape only, so the Akita foothold gained in its /ledger/2 is carried by the Nara found region alone. The reviewer's optional asuka edit is left to the orchestrator.
- Mongol 1274 end is confidence 2: the page dates the landing (19 November) and the battle (20 November) but gives the withdrawal only as 'By morning, most of the Yuan ships had disappeared' (and a diary 'entry for 6 November 1274' that cannot be a post-landing date).
- Not acted on (thin): Kiyohara as a vassal tint for 1062-1086, c. 850 Emishi tint, Isawa and Shiwa castle dates, Ezo/Andō, Rokuhara, 1221 confiscations.
