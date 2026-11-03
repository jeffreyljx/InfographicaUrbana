# Review of batch ea-04-b (Tibetan Empire, Nanzhao, Tibetans, Dachanghe)

Reviewer: adversarial reviewer, Phase B, 2026-10-19. Machine copy: `history/notes/phase-b/reviews/ea-04-b.json`.

Mechanical: all four dossiers validate with `--resolve`, 0 errors, 0 warnings (before and after the reviewer's edits). Ledgers sorted, found/dissolve at the life bounds, contests paired, certainty spans cover the lives, capitals inside the first shapes' bboxes (Lhasa 91.1 E 29.6 N; Dali 100.18 E 25.7 N). Rulers of tibetan-empire match the List of emperors of Tibet page (including Songtsen Gampo's second span 655-660).

Verdicts: tibetan-empire **fail** (one blocking finding left for the author; four small fixes applied), nanzhao **fail** (missing vassal events), tibetans **thin** (one small fix applied), dachanghe **pass**.

## tibetan-empire: fail

Applied by the reviewer (each note carries a `[Reviewer ea-04-b ...]` sentence):

1. `/ledger/8, 10, 12, 13, 14` (670, 673, 679, 687, 692): region `union(Tarim Basin, Dzungaria, Turfan-Hami) minus 666 shape` trimmed to `Tarim Basin minus 666 shape`. The 670 event resolved to 4819 cells, only 2945 in the Tarim; the Gaochang and Beshbalik discs were wholly inside. Protectorate page: 'In 670 the Tibetan Empire routed a Tang army at the Battle of Dafei River and attacked Gumo as well as captured Qiuci'; no Tibetan capture of Xizhou or Tingzhou/Beiting before 790; 'Anxi and Beiting were left relatively unmolested' after 764. The dossier's own 674/682 corrections already remove Dzungaria and Turfan-Hami.
2. `/ledger/7` (666 Khotan): counterpart `kingdom-of-khotan` (dossier life 851-1006) replaced by the name `Yutian (Kingdom of Khotan)`.
3. `/ledger/4` (638): counterpart `nobody` -> `tuyuhun`, mirroring tuyuhun /ledger/9; Tuyuhun page: 'The Tuyuhun Empire lost much of its territory in southern Gansu to Tibetans' (no year); the page added to `sources[]`. Confidence stays 1.
4. `/ledger/36` (790 western Tarim): confidence 3 -> 2; the page has only 'by 790' and says it is unclear what happened to Shule, Shache and Gumo.

Left for the author (blocking):

5. `/ledger/31` and `/keyframe_review/20, 21, 22` corrections: Shazhou and Guazhou are Tibetan from 764 (all 42 cells of a 60 km Dunhuang disc are inside the 764 gain and each 768/772/783 correction), so the 786 gain of Dunhuang (`/ledger/34`) is a no-op. Guiyi Circuit page: 'Around the 770s or the 780s, Shazhou ... was occupied by the Tibetans'; 'From the beginning of Tibetan rule over Dunhuang (786)'. Fix: subtract `{"place": "Dunhuang", "km": 200}` from the 764 gain and from the 768, 772 and 783 corrections, so the west end of the corridor comes with the 786 event; say so in the notes.

Non-blocking, routed to ea-04-a: tang-dynasty has no mirror for the 717-749 Aksu/Stone City contest, the 747 Gilgit loss, the 749 Stone City loss, the 757 gain, the 763 Yanqi gain and the 786 Dunhuang gain; its Chang'an occupation is 18 November 763 against October 763 here (Sino-Tibetan relations page: 'In October of 763 A.D'). Kashmir (sa-03) has 656, 661, 747 and 748 events against tibetan-empire with no mirror; the author flagged them; the 748 Ladakh/Baltistan loss there and the 757 gain here (both confidence 1) need one date.

Thin: 628 (527,000 km2), 638, 656 and 757 events are confidence 1; the Hexi cities between Liangzhou 764 and Shazhou 786 are undated; the 783 and 821/822 border courses are not on any opened page.

Spot checks (Protectorate, Tibetan Empire, Sino-Tibetan relations, Guiyi Circuit, List of emperors of Tibet): 670, 673, 677, 679, 687, 692, Lesser Bolu 710/722/737/747, 749, 763 Yanqi, October 763, 786, 787, 'by 790', 790 Beiting, 792, Khotan 665-670 and 842 all confirmed on the pages. Area: infobox 4,600,000 km2 (800) against Cliopatria 3,856,365 km2 (tibetan-empire_793), ratio 0.84, acknowledged in the 793 keyframe note.

## nanzhao: fail

Blocking, left for the author:

1. No vassal events at all, and the notes do not say why. tibetan-empire has `vassal_start nanzhao` 754 and `vassal_end` 794; tang-dynasty has `vassal_start` 738, `vassal_end` 751, `vassal_start` 794, `vassal_end` 902. Nanzhao page: 'By the end of 754, Geluofeng had established an alliance with the Tibetans against the Tang that would last until 794'; he 'accepted a Tibetan title and acted as part of the Tibetan Empire'; 'In 794, he launched the battle of Shenchuan to break up with Tibet and switched sides to the Tang'; later 'an amicable tributary relationship with the Tang'; Tang title 'Prince of Yunnan' 738. Tianbao War page: he 'had proclaimed himself Eastern Emperor and had broken with the Tang court', 'sworn younger brother' of Me Aktsom. Add: 738 vassal_start tang-dynasty; 751 vassal_end tang-dynasty; 754 vassal_start tibetan-empire; 794 vassal_end tibetan-empire; 794 vassal_start tang-dynasty; 902 vassal_end tang-dynasty (regions: the Nanzhao shape of the year).

Non-blocking: `/ledger/11` note quotes 'at various points', not on the Annan page (it has 'Prior to Li Hu's arrival, Nanzhao had already seized Bozhou' and 'Nanzhao's forces moved around and seized Yongzhou'). Annan 863-866 is an occupation here and a loss/gain in tang-dynasty (route to ea-04-a). tang-dynasty has no mirror for 750, 754, 755, 756, 829-830 and 873-875.

Thin: the 755 step (376,000 km2, confidence 1) and the Guizhou/Guangxi/Vietnamese lands 755-865; the Pyu war has no zone.

Spot checks (Tianbao War, Nanzhao, Annan pages): 750, 754, 756, 779 (infobox), January 863, fall 866, 873-874, 875, 902 all confirmed. No infobox area on the Nanzhao page.

## tibetans: thin

Applied: `/ledger/3` (850 Tarim loss) confidence 2 -> 1 (the note itself says the page dates it only 'by the mid-9th century').

Left for a gap-filler: `/keyframe_review/5` (tibetans_960) loses about 19,000 km2 on the southern edge (27.35 -> 27.62 N) with no ledger event, and kamarupa-kingdom /ledger/19 has a 960 gain from tibetans (confidence 1); add the mirror loss at confidence 1, and note the 1139 return. Tingzhou and Luntai under the Tibetan general Kongre until 866 (Guiyi page) are not drawn. Ngari/Guge (c. 912), Maryul (c. 930) and Xiliangfu (by 906) stay inside the polygon until their dossiers exist.

Cross-group: tang-dynasty gains the Hexi cities (848 from tibetan-empire, which ended 842; 850 and 861 from tibetans) while this dossier names 'Guiyi Circuit (Zhang Yichao)'; tang's 851 Xizhou gain from tibetans has no land here (Guiyi page names no previous holder). kingdom-of-khotan founds 851 from tibetan-empire; it should name tibetans, and the Khotan part of this 850 loss could go to kingdom-of-khotan in 851. The orchestrator should decide whether Guiyi land is tang-dynasty's or a guiyi-circuit dossier's.

Spot checks (Guiyi Circuit, History of Tibet): 848, 850, 861 and 1249 confirmed (the 1249 sentence carries 'citation needed' on the page).

## dachanghe: pass

Tried: the 902 mirror with nanzhao (matched), the 928 and 929 renames and the 937 end on the Nanzhao and Dali Kingdom pages (confirmed; the Dali Kingdom page's 903-927 / 927-928 / 928-937 dates are recorded in the dossier), the single keyframe (nanzhao_900 carried to 937, stated). Could not break it. The kingdom-of-dali dossier (not yet written) must start in 937 with a new keyframe for 937-946, since Cliopatria's row begins in 947.
