# Review of batch ia-01-e (2026-10-18 brief, run 2026-10-19)

Dossiers: turks, turgesh, kimek-kipchak-confederation, oghuz-turks. The machine copy is history/notes/phase-b/reviews/ia-01-e.json.

The validator (`--resolve`) gives 0 errors on all four. Its only warnings are counterpart slugs with no dossier (second-turkic-khaganate, pechenegs), and both are listed under counterparts needing dossiers.

Pages opened: Western Turkic Khaganate, Türgesh, Muslim conquest of Transoxiana, Battle of Talas, Karluks, Kimek-Kipchak confederation, Cumans, Oghuz Yabgu State, Oghuz Turks. Every spot-checked event is on its page with its year. I found no fabricated or mis-dated confidence-3 event.

Neighbour dossiers present: khazaria and yenisei-kyrgyz. Neither has a territorial event with these states. I also read western-gokturks for the turks start. Every other Context polity is unwritten, which is an exception under the brief.

## turks: fail (back to the author)

The events themselves check out: 666, 677, 679 and 699/700 are all on the WTK page. The faults are in identity and counterparts:

1. **/ledger/0 and /identity/predecessors.** The 666 founding takes its land from western-gokturks. That dossier ends in 657, hands its land to tang-dynasty, and lists no turks successor. The Tang example gains Dzungaria and Semirechye in 657. WTK page: Mishe and Buzhen were Tang proxies.
   Fix: make the counterpart tang-dynasty and add tang-dynasty to predecessors.
2. **Tang vassalage missing.** WTK infobox: "Vassal of the Tang dynasty (657–742)". Text: "Empress Wu Zetian sent Yuanqing and Böri westward in 685 ... as proxy rulers".
   Fix: add vassal_start and vassal_end against tang-dynasty, for 666-677 and 685-690/698, or explain why not.
3. **/ledger/4.** The 698 dissolve hands Semirechye and Chach to turgesh. But turgesh founds on a 150 km Taraz core in 699 and gains Semirechye and Chach from tang-dynasty in 703, so the two dossiers disagree on who held that land in 699-702.
   Fix: make the two agree.
4. **/identity/capitals/0.** Suyab is the capital for 666-698, but the WTK page says "From 679 to 719 ... Suyab was one of the Four Garrisons of Anxi".
   Fix: end Suyab at 678.
5. **/ledger/1.** The 674 Dzungaria gain names counterpart nobody, but the Tang example holds Dzungaria from 657.
6. **Wikidata.** Q2118293 is shared with oghuz-turks while the dossier's wikipedia is the Western Turkic Khaganate. I could not check it, because wikidata.org is unreachable.

Area: the WTK infobox gives 3.5 M km2 for 630, when there is no turks shape. The dossier says so.

## turgesh: thin (one fix applied by the reviewer)

- **Applied.** /identity/rulers/1-8 had no source. I added the Türgesh page, whose khagan list matches every reign in the dossier. Re-validated: 0 errors.
- **Missing: 740 vassal_start and 744 vassal_end, counterpart tang-dynasty.** Page: "In 740 Kül-chor submitted to the Tang dynasty"; "captured and executed by the Tang in 744". The author asked the Tang dossier to carry this, but turgesh's own ledger needs it too.
- **Missing: Tang control in 751 and 753.** Battle of Talas page: in 751 the Tang "consolidated Chinese control over the Turgesh"; in 753 the Tang "appointed a Turgesh khan".
- **Beshbalik and Turpan (/keyframe_review/2-4, /ledger/9).** The 703-735 corrections draw both towns as Turgesh. But the same page says "In 735 the Turgesh attacked Ting Prefecture (Jimsar County)", which was Tang. The Tang example holds Xi Prefecture (Turfan) from 640.
  Fix: take Beshbalik and Turpan out, or explain. Settle this with ea-04.
- **Confidence-1 events.** 715 (contest_end) and 745 (loss to the Tang), plus Zhetysu drawn alone for 745-765.
- **Spot checks.** 703, 719, 728, 732, 736 and 766 are all confirmed.
- **Area.** The infobox has no area. The correction draws about 0.9 M km2 against Cliopatria's 4.03 M km2; the keyframe notes explain the gap (Cliopatria's shape is Second Turkic Mongolia).

## kimek-kipchak-confederation: thin

**Spot checks.** All confirmed:
- 880: infobox 880–1035.
- 1056 Oghuz lands: "Rus chronicles under the year 1054 ... Oguz ... pushed by Kipchaks"; "After seizing the Oguz lands".
- 1056 Pontic steppe: the Cumans meet the Rus' in 1055.
- 1241: "Cuman control over the Pontic steppes ended".

**Open finding.** After the 1055 rename this dossier is the Cumans, and the Cumans page runs the confederation "from the Danube in the west to Taraz". The 1056-1235 shapes stop at 37.8 E and are marked ok. The author flagged that eu-16's Halych-Volhynia occupation row holds that steppe; route it to eu-16 and ia-01-g, then mark the keyframes adjust with the Pontic Steppe.

**Gaps.** Seven confidence-1 events. The biggest:
- 1072 gain of +0.79 M km2 from nobody (try Volga Bulgaria).
- 1227 loss of -1.45 M km2 to the Mongols, a decade before the pages.

The rest:
- 1220 loss (Irtysh and Altai to the Mongols).
- 1147 loss (Qara Khitai).
- 1210 loss (Khwarezm).
- 896 gain (Pechenegs).
- 1055 rename.

Two smaller gaps:
- The Tamim placeholder sits about 150 km south of the southern shore of Lake Balkhash.
- The Naiman displacement from the Altai has no event.

**Area.** No page gives one; the dossier says so.

## oghuz-turks: thin

**Spot checks.** 750, 985, 1041 and 1043 are confirmed on the Oghuz Yabgu State page. The 970 quote (Sari-su, Turgai, Emba) is confirmed on the Oghuz Turks page.

**/wars/1 (800-850).** The zones are empty, but the war's own outcome says the Oghuz took the lower Syr Darya and Aral steppes. The page: "At the beginning of the 9th century ... captured the lower course of the Syr Darya river and the Aral steppes". The keyframes draw that land as Oghuz from 750, following the Oghuz Turks page ("700s").
Fix: give the war a zone, then either keep the 750-799 keyframes with a note or adjust them and add a gain from kangar-union around 800. A Kangar or Pecheneg page might settle the date.

**Confidence-1 events.** The 801 capital move and the 970 gain.

**End year.** The infobox says 1055. The text has the state "perhaps disappearing" after 1043 and ended "by the 12th century". The author flagged this.

**Area.** The infobox has none.

## Cross-dossier matrix (summary)

- **Matched:** the 1056 kimek gain from oghuz-turks against the 1055 oghuz loss.
- **Mismatches:**
  - turks found 666 against western-gokturks, which ends in 657 with its land going to the Tang.
  - turks 674 gain from nobody, while the Tang example holds Dzungaria from 657.
  - turks 679 loss of Kucha to the Tang, while the Tang example's 679 gain names tibetan-empire.
  - turks dissolve 698 against turgesh found 699: the land differs.
- **Missing:** the turgesh 740-744 Tang vassalage.
- **Exceptions (groups not yet run, or no dossier):** tang-dynasty (ea-04), umayyad-caliphate (me-07), qarlugs (ia-01-f), seljuk-dynasty and great-seljuk-empire (me-09), ghaznavid-empire (me-08), khwarezmid-empire (me-09), kara-khitans (ia-01), mongol-empire (ia-02), second-turkic-khaganate, pechenegs.

## Gazetteer names needed

Navekat, Yangikent, Jend, Imak, Tamim. All are places: capitals or names in notes.
