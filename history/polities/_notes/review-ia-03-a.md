# Review of batch ia-03-a (kazakh-khanate)

Reviewer, 2026-10-19. Verdict: **fail** (one blocking finding, not applied: an unexplained 1475 gain of 729 cells). Two small fixes applied by the reviewer (slug small-horde to nogai-horde; Sayram notes); the dossier re-validates with --resolve, no errors or warnings.

## What was tried

- Validator --resolve: valid, 0 warnings, before and after the reviewer's edits.
- Keyframe walk on the H3 grid (corrected shape of each keyframe against the next, with the ledger events between): every step is explained except 1468 to 1475 (+729 cells, no event) and 1519 to 1521 (-131 Qyzylorda cells, an artefact of whole-admin1 corrections).
- Capitals against the drawn shapes: Sozaq (1465-1468) and Saraishyq (1511-1520) fall outside.
- Spot checks on 5 pages, 15 events or groups, all confidence-3 events among them: all confirmed except the reading of Sayram's retaking (confidence 1, note fixed).
- Area: no infobox area; acknowledged by the author.
- Cross-checks against the neighbour dossiers that exist (khanate-of-sibir, nogai-horde, moghulistan, timurid-empire; mongol-khanate, golden-horde, kapisa and eastern-chagatai-khanate carry no Kazakh events).

## Findings

1. **BLOCKING** (for the author) `/keyframe_review/2/correction (and /keyframe_review/3-5, /ledger between 1470 and 1496)`
   - What: The 1475-1496 corrections keep 729 cells (about 184,000 km2: Qyzylorda 407, South Kazakhstan 264, Zhambyl 36 cells; 61.0-71.2E, 37.6-46.6N, the middle and lower Syr Darya) that Cliopatria moves from its Timurid shape to the Kazakh shape in 1475, but no ledger event gains them, and the 1496 loss to the Shaybanids (680 of these cells) gives away land the ledger never gained.
   - Why: Keyframe walk with the gazetteer: corrected 1468 keyframe 4,499 cells, corrected 1475 keyframe 5,220 cells (+729, -8); the only event 1469-1481 is the 1470 Sibir gain, which covers none of the 729. All 729 lie in Cliopatria's 1474 Timurid shape, and 270 of them are also inside the timurid-empire dossier's 1475 correction (Transoxiana), so they are claimed twice 1475-1496. The Kazakh Khanate page only says that in the 1495-1496 division 'the Kazakh rulers retained control over several cities of northern Turkestan' and that the Shaybanids held Otrar, Yasi, Arkuq and Uzgend; it gives no year for a Kazakh hold.
   - Fix: Add a gain (year 1475, Cliopatria's, confidence 1 unless a Janibek/Burunduk Khan page dates it) with counterpart timurid-empire or the Uzbek heirs of Abu'l-Khayr (listed under counterparts_needing_dossiers), region {"intersect": [{"minus": [{"cliopatria": "Kazakh Khanate", "year": 1475}, {"cliopatria": "Kazakh Khanate", "year": 1474}]}, {"country": "Kazakhstan"}], "text": "several cities of northern Turkestan"}; or, if no page supports a Kazakh hold before 1496, subtract these cells from the 1475-1492 corrections and shrink the 1496 loss accordingly. Tell the timurid-empire owner (ia-02) about the 270 doubly claimed cells.

2. **non-blocking** (applied by reviewer) `/ledger/15/counterpart, /ledger/16/counterpart, /ledger/17/counterpart, /wars/3/belligerents/1`
   - What: Counterpart slug small-horde does not and will not exist: the nogai-horde dossier is written as one state for both Cliopatria rows.
   - Why: history/polities/nogai-horde.json identity.cliopatria_names = ['Nogai Horde', 'Small Horde'] (shared Wikidata Q631210, merged under the earlier slug as the brief requires).
   - Fix: Changed small-horde to nogai-horde in the four places (Cliopatria region names 'Small Horde' left as they are); re-validated with --resolve: valid, no warnings.

3. **non-blocking** (applied by reviewer) `/ledger/27/note, /ledger/26/note, /keyframe_review/22/note`
   - What: The notes said the Kazakh-Dzungar Wars page has Sayram 'retaken after a local revolt' as if by the Kazakhs; the page has Galdan recapture it.
   - Why: Kazakh-Dzungar Wars page: Sayram taken in 1684 after failed sieges in 1681 and 1683; the townspeople revolted and destroyed the Dzungar garrison, after which Galdan returned and recaptured the city; Tauke recaptured Tashkent in 1688. No Kazakh retaking of Sayram is dated.
   - Fix: Rewrote the three notes to say this; the 1687 gain stays at confidence 1 as Cliopatria's year (listed under thin).

4. **non-blocking** (for the author) `/identity/capitals/0`
   - What: The first capital Sozaq (68.5E, 44.0N, 1465-1468) lies outside the 1465-1467 keyframe, which is Cliopatria's 1468 Chu-Talas core (bbox 70.11-76.61E).
   - Why: Point-in-shape check on the H3 grid: Sozaq cell out of the corrected 1465 keyframe (it is within about 35 km of the 1468 keyframe).
   - Fix: Add Sozaq to the 1465 keyframe correction (e.g. union with {"lon": 68.5, "lat": 44.0, "km": 50, "text": "Sozaq (c. 1465-1469)"}) or say in the capital's note why the seat lies outside the drawn core.

5. **non-blocking** (for the author) `/identity/capitals/2 and /ledger/6`
   - What: Saraishyq (51.7E, 47.5N), capital 1511-1520, lies outside every Kazakh keyframe 1502-1528, including the 1521 shape, and the nogai-horde dossier has Kasym take Saray-Juk only in 1520.
   - Why: Point-in-shape check: Saraishyq cell out of the 1502, 1512-1520 and 1521 keyframes; nogai-horde/ledger/1: 'Kasym successfully captured the Nogai capital Saray-Juk in 1520'. The infobox does say 'Saraishyq (1511-1521)' (confirmed), so the event is not fabricated.
   - Fix: Note the conflict at /ledger/6 (infobox 1511 against the 1520 capture) and either start the Saraishyq seat in 1520 or add Saraishyq to the 1520-1528 drawing through the 1521 Nogai gain region; consider confidence 2 for /ledger/6.

6. **non-blocking** (for the author) `/ledger/5/region and /keyframe_review/8, /keyframe_review/9, /keyframe_review/10 (correction)`
   - What: The whole-admin1 union (South Kazakhstan + Qyzylorda) overshoots Cliopatria's 1521 shape by 131 cells (130 in Qyzylorda), which then drop out in 1521 with no event.
   - Why: Keyframe walk: corrected 1519 keyframe minus Cliopatria 1521 shape = 131 cells, 130 of them in Qyzylorda admin1; no loss event in 1521.
   - Fix: Intersect the admin1 union with {"cliopatria": "Kazakh Khanate", "year": 1521} in /ledger/5/region and in the three corrections.

7. **non-blocking** (for the author) `/ledger/2 and /keyframe_review/1`
   - What: The corrected 1468 keyframe (1468-1474) already shows the steppe that the ledger gains only in 1470, and the khanate-of-sibir dossier loses it in 1468 (two years apart).
   - Why: Kazakh Khanate page: 'Around 1470, the Kazakh tribes, led by Janibek and Kerei, settled in what is now Kazakhstan'; khanate-of-sibir/ledger/6 dates the loss 1468 (Abu'l-Khayr's death).
   - Fix: Date the gain 1468 with the page's 'around 1470' in the note (agreeing with the keyframe and with Sibir), or keep 1470 and have the Sibir owner move its loss; either way the two dossiers must agree within a year.

8. **non-blocking** (for the author) `/ledger (no vassal events)`
   - What: The ledger has no vassal events for the Kazakh jüzes' submission to Russia (Junior 1731, Middle 1740), the Dzungar overlordship (1734-1742) or the Qing (1757); the author left them to the overlords' dossiers.
   - Why: Reviewer brief check 3 expects the subordinate's ledger to mirror a vassal_start with the overlord as counterpart; the schema's wording ('this state's vassal', counterpart = the vassal) points the other way. The author's notes item 9 flag the choice.
   - Fix: Orchestrator to rule on the convention; if mirrors are required, add vassal_start/vassal_end pairs here (counterparts russian-empire, dzungar-khanate, qing-dynasty) from the Kazakh Khanate, Jüz and Abylai Khan pages already in sources.

## Thin (confidence 1 or unverified spans; for a gap-filler)

- `/ledger/3`: 1487 Sibir steppe (1,326 cells) is Cliopatria's year. Try https://en.wikipedia.org/wiki/Janibek_Khan
- `/ledger/5`: year of the Uzbek handover of the Syr Darya lands (bridged to 1510). Try https://en.wikipedia.org/wiki/Kasym_Khan
- `/ledger/10`: Semirechye gain from the Moghuls dated only by Cliopatria (1521). Try https://en.wikipedia.org/wiki/Tarikh-i-Rashidi
- `/ledger/11`: Tashkent and northern Kyzylkum in 1521; Tashkent page has the city Shaybanid in the 16th century. Try https://en.wikipedia.org/wiki/Tashkent
- `/ledger/14`: end of the Semirechye struggle (1565 bridged to Abdurashid's death). Try https://en.wikipedia.org/wiki/Haqnazar_Khan
- `/ledger/20`: loss of Tawakkul's Samarkand-Andijan conquests (Cliopatria 1609). Try https://en.wikipedia.org/wiki/Esim_Khan
- `/ledger/27`: Kazakh return of Sayram (Cliopatria 1687; the page has Galdan retake it). Try https://en.wikipedia.org/wiki/Tauke_Khan
- `/ledger/28`: 1718 Irtysh strip to the Tsardom: the Russian fort behind it. Try https://en.wikipedia.org/wiki/Semey
- `/ledger/29`: 1721 northern strip to Russia. Try https://en.wikipedia.org/wiki/Omsk
- `/ledger/31`: 1738 Orenburg country to Russia. Try https://en.wikipedia.org/wiki/Orenburg
- `/ledger/35`: 1769 upper Irtysh and Altai edge to Russia. Try https://en.wikipedia.org/wiki/Ust-Kamenogorsk
- `/ledger/37`: 1791 Aral, lower Syr Darya and Ustyurt to Khiva (725 cells). Try https://en.wikipedia.org/wiki/Khanate_of_Khiva
- `/ledger/38`: 1809 Sayram-Shymkent-Turkestan lands to Kokand (259 cells). Try https://en.wikipedia.org/wiki/Turkistan_(city)
- `/ledger/39`: 1822 Talas, Taraz and Syr Darya lands to Kokand (396 cells), dated only 'the 1820s'. Try https://en.wikipedia.org/wiki/Taraz
- `/ledger/40`: 1822 lower Syr Darya strip back from Khiva (47 cells). Try https://en.wikipedia.org/wiki/Kyzylorda
- `/ledger/42`: Junior jüz takeover dated by bridging to 1824. Try https://en.wikipedia.org/wiki/Lesser_J%C3%BCz
- `/ledger/46`: end of the Junior jüz occupation tied to 1847. Try https://en.wikipedia.org/wiki/Bukey_Horde
- `/keyframe_review/12, /keyframe_review/13`: 1529-1571 flat shape although the page has the Kazakhs 'completely uprooted' after 1533-1534 (unverified: page budget). Try https://en.wikipedia.org/wiki/Haqnazar_Khan

## Spot checks

- `/ledger/2`: confirmed ('Around 1470, the Kazakh tribes, led by Janibek and Kerei, settled in what is now Kazakhstan') (https://en.wikipedia.org/wiki/Kazakh_Khanate)
- `/ledger/1, /ledger/6, /ledger/12 (capital_move, confidence 3)`: confirmed (infobox: Sozaq c. 1465-1469; Syghanaq 1469-1511; Saraishyq 1511-1521; Syghanaq 1521-1599) (https://en.wikipedia.org/wiki/Kazakh_Khanate)
- `/ledger/4`: confirmed (division around 1495-1496; Shaybanids hold Otrar, Yasi, Arkuq and Uzgend) (https://en.wikipedia.org/wiki/Kazakh_Khanate)
- `/ledger/9`: confirmed (end of Kasym's reign: Yaik River basin in the northwest; right bank of the Syr Darya including Tashkent, Turkestan and Sayram) (https://en.wikipedia.org/wiki/Kazakh_Khanate)
- `/ledger/17`: confirmed (by 1569 Haqq Nazar's raids; the Manghit nomads east of the Ural absorbed) (https://en.wikipedia.org/wiki/Kazakh_Khanate)
- `/ledger/18`: confirmed (1597 revolt of Abd al-Mu'min, Tawakkul takes Tashkent, Turkistan, Andijan and Samarqand, fails at Bukhara) (https://en.wikipedia.org/wiki/Kazakh_Khanate)
- `/ledger/21, /ledger/22`: confirmed (Yesim captured Tashkent twice, in 1611 and 1613) (https://en.wikipedia.org/wiki/Kazakh_Khanate)
- `/ledger/23 (confidence 3)`: confirmed (1643 Battle of Orbulaq in the Orbulaq gorge on the Ili, Jetisu) (https://en.wikipedia.org/wiki/Kazakh%E2%80%93Dzungar_Wars)
- `/ledger/25`: confirmed (victories on the Chu and Talas consolidated the border from the Talas to the Ayagöz; eastern Semirechye and the upper Irtysh land dependent in the 1650s; 1658 is in the link title, and the Kazakh-Dzungar Wars page has 1658) (https://en.wikipedia.org/wiki/Dzungar_Khanate)
- `/ledger/26 (confidence 3)`: confirmed (Sayram captured in 1684 after failed sieges in 1681 and 1683) (https://en.wikipedia.org/wiki/Kazakh%E2%80%93Dzungar_Wars)
- `/ledger/27`: not on page as noted: the page has Galdan recapture Sayram after the revolt; note rewritten (confidence 1, not blocking) (https://en.wikipedia.org/wiki/Kazakh%E2%80%93Dzungar_Wars)
- `/ledger/32`: confirmed ('The Dzungars controlled Jetisu and Tashkent until 1745') (https://en.wikipedia.org/wiki/Dzungar_Khanate)
- `/ledger/33, /ledger/34 (confidence 3)`: confirmed (Irdana Biy 'temporarily took control of Tashkent in 1765 before Ablay Khan retook it') (https://en.wikipedia.org/wiki/Khanate_of_Kokand)
- `/ledger/43`: confirmed (rebellion 1837-1847, 'national liberation character') (https://en.wikipedia.org/wiki/Kenesary_Kasymov)
- `/ledger/47 (confidence 3)`: confirmed ('the last khan of the Kazakh Khanate'; killed in battle against Kyrgyz manaps in 1847; infobox Disestablished 1847) (https://en.wikipedia.org/wiki/Kenesary_Kasymov)

## Cross-dossier matrix

- kazakh-khanate 1465 found, counterpart moghulistan: **missing** (mirror: moghulistan None None). Predecessor land: the 533 cells of the Kazakh 1468 core all lie in Cliopatria's 1467 Moghulistan shape; moghulistan.json has no loss to the Kazakhs and no kazakh-khanate successor. Route to the moghulistan owner (ia-02).
- kazakh-khanate 1470 gain, counterpart khanate-of-sibir: **mismatch** (mirror: khanate-of-sibir 1468 loss). Two years apart (page: around 1470; Sibir: Abu'l-Khayr's death 1468); same land (Cliopatria 1482 minus 1481).
- kazakh-khanate 1475 gain (missing), counterpart timurid-empire: **missing** (mirror: timurid-empire None None). No event on either side for the 729 Syr Darya cells Cliopatria moves from Timurid to Kazakh in 1475; 270 of them are inside both the kazakh-khanate and timurid-empire 1475 corrections (double claim). See fix 1.
- kazakh-khanate 1487 gain, counterpart khanate-of-sibir: **matched** (mirror: khanate-of-sibir 1487 loss)
- kazakh-khanate 1496 loss, counterpart shaybanids: **exception**. counterpart dossier not written yet; group ia-03 (shaybanids) has not run
- kazakh-khanate 1510 gain, counterpart shaybanids: **exception**. counterpart dossier not written yet; group ia-03 (shaybanids) has not run
- kazakh-khanate 1520 contest_start, counterpart nogai-horde: **matched** (mirror: nogai-horde 1520 contest_start)
- kazakh-khanate 1521 contest_end, counterpart nogai-horde: **matched** (mirror: nogai-horde 1521 contest_end)
- kazakh-khanate 1521 gain, counterpart nogai-horde: **matched** (mirror: nogai-horde 1521 loss)
- kazakh-khanate 1521 gain, counterpart western-moghulistan: **exception**. counterpart dossier not written yet; group ia-03 (western-moghulistan) has not run
- kazakh-khanate 1521 gain, counterpart khanate-of-bukhara: **exception**. counterpart dossier not written yet; group ia-03 (khanate-of-bukhara) has not run
- kazakh-khanate 1568 contest_start, counterpart nogai-horde: **matched** (mirror: nogai-horde 1568 contest_start). Counterpart slug corrected from small-horde by the reviewer.
- kazakh-khanate 1569 contest_end, counterpart nogai-horde: **mismatch** (mirror: nogai-horde 1572 contest_end). Three years apart; the Kazakh side is page-backed (Kazakh Khanate page: by 1569 the Manghits east of the Ural absorbed), the nogai side is confidence 1 (Cliopatria step). Route to the nogai-horde owner (ia-02) to move to 1569.
- kazakh-khanate 1569 gain, counterpart nogai-horde: **mismatch** (mirror: nogai-horde 1572 loss). As above: 1569 (page) against 1572 (Cliopatria, confidence 1).
- kazakh-khanate 1597 gain, counterpart khanate-of-bukhara: **exception**. counterpart dossier not written yet; group ia-03 (khanate-of-bukhara) has not run
- kazakh-khanate 1609 loss, counterpart khanate-of-bukhara: **exception**. counterpart dossier not written yet; group ia-03 (khanate-of-bukhara) has not run
- kazakh-khanate 1658 loss, counterpart oirat-confederation: **exception**. counterpart dossier not written yet; group ia-03 (oirat-confederation) has not run
- kazakh-khanate 1684 loss, counterpart dzungar-khanate: **exception**. counterpart dossier not written yet; group ia-03 (dzungar-khanate) has not run
- kazakh-khanate 1687 gain, counterpart dzungar-khanate: **exception**. counterpart dossier not written yet; group ia-03 (dzungar-khanate) has not run
- kazakh-khanate 1718 loss, counterpart tsardom-of-russia: **exception**. counterpart dossier not written yet; group eu-16 (tsardom-of-russia) has not run
- kazakh-khanate 1721 loss, counterpart russian-empire: **exception**. counterpart dossier not written yet; group eu-17 (russian-empire) has not run
- kazakh-khanate 1723 occupation_start, counterpart dzungar-khanate: **exception**. counterpart dossier not written yet; group ia-03 (dzungar-khanate) has not run
- kazakh-khanate 1738 loss, counterpart russian-empire: **exception**. counterpart dossier not written yet; group eu-17 (russian-empire) has not run
- kazakh-khanate 1745 occupation_end, counterpart dzungar-khanate: **exception**. counterpart dossier not written yet; group ia-03 (dzungar-khanate) has not run
- kazakh-khanate 1769 loss, counterpart russian-empire: **exception**. counterpart dossier not written yet; group eu-17 (russian-empire) has not run
- kazakh-khanate 1784 loss, counterpart Tashkent state (Yunus Khoja): **exception**. No dossier; listed in the author's counterparts_needing_dossiers (suggested slug tashkent-state-of-yunus-khoja); switch the counterpart string to that slug once it exists.
- kazakh-khanate 1791 loss, counterpart khanate-of-khiva: **exception**. counterpart dossier not written yet; group ia-03 (khanate-of-khiva) has not run
- kazakh-khanate 1809 loss, counterpart khanate-of-kokand: **exception**. counterpart dossier not written yet; group ia-03 (khanate-of-kokand) has not run
- kazakh-khanate 1822 loss, counterpart khanate-of-kokand: **exception**. counterpart dossier not written yet; group ia-03 (khanate-of-kokand) has not run
- kazakh-khanate 1822 gain, counterpart khanate-of-khiva: **exception**. counterpart dossier not written yet; group ia-03 (khanate-of-khiva) has not run
- kazakh-khanate 1822 occupation_start, counterpart russian-empire: **exception**. counterpart dossier not written yet; group eu-17 (russian-empire) has not run; Middle jüz
- kazakh-khanate 1824 occupation_start, counterpart russian-empire: **exception**. counterpart dossier not written yet; group eu-17 (russian-empire) has not run; Junior jüz
- kazakh-khanate 1837 occupation_end, counterpart russian-empire: **exception**. counterpart dossier not written yet; group eu-17 (russian-empire) has not run
- kazakh-khanate 1847 occupation_end, counterpart russian-empire: **exception**. counterpart dossier not written yet; group eu-17 (russian-empire) has not run

## Gazetteer names needed

Sayram, Sygnak, Sozak, Saraishyq (places; text and capitals only).

