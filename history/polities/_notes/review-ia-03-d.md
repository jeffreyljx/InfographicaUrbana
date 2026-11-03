# Review of batch ia-03-d (Central Asian khanates, part d)

Reviewer, 2026-10-19. Dossiers: khanate-of-kokand, dzungar-khanate, hotaki-dynasty, kalmyk-khanate, oirat-confederation. The machine copy is history/notes/phase-b/reviews/ia-03-d.json.

All five validate with `--resolve`, with no errors. Before the review, khanate-of-kokand had warnings for tashkent-state and kara-kyrgyz-khanate (listed as needed dossiers) and dzungar-khanate had one for yarkent-khanate (now fixed). Context dossiers read: kazakh-khanate, khanate-of-bukhara, khoshut-khanate, eastern-moghulistan, nogai-horde, four-oirats and the other ia-02/ia-03 neighbours that exist. The qing-dynasty, russian-empire, safavid-dynasty, afsharid-iran, ottoman-empire and emirate-of-bukhara dossiers do not exist yet, so events against them are exceptions.

## Verdicts

| slug | verdict | in short |
| --- | --- | --- |
| dzungar-khanate | fail | Two problems I did not fix: the 1677 gain from khoshut-khanate, and the missing 1696 loss of Hami. I changed the counterpart slug of the 1680 event. |
| khanate-of-kokand | thin | All six spot checks confirmed. The 1809 and 1822 growths are confidence-1 bridges. |
| hotaki-dynasty | thin | All six spot checks confirmed. I lowered 1723 to confidence 1. The 1718 Sistan-Balochistan gain is a bridge. |
| kalmyk-khanate | thin | I lowered the 1634 confidence from 3 to 2. The 1636 and 1738 growths are bridges, and the Russian treaties are missing. |
| oirat-confederation | fix | I lowered the 1628 split from confidence 3 to 2. The split region is advisory only. The 1634 break is accepted. |

## Decision on the Oirat/Dzungar partition: accepted

Both pages put the break at 1634: the Oirat page has "Disestablished: 1634" and the Dzungar page has "Established: 1634". So oirat-confederation runs 1609-1634 and dzungar-khanate 1634-1757, as the author proposes. This leaves one task for the **kazakh-khanate** author. That dossier's /ledger/24 (the 1643 contest_start) and /ledger/25-26 (the 1658 contest_end and loss) must name `dzungar-khanate`, not `oirat-confederation`.

## dzungar-khanate (fail)

1. **Applied.** /ledger/6/counterpart and /wars/1/belligerents/1: changed `yarkent-khanate` to `eastern-moghulistan`. The eastern-moghulistan dossier is the "Yarkent Khanate (Eastern Moghulistan)", and its /ledger/4 is the mirroring 1680 loss to dzungar-khanate. I updated the notes sentence to match. yarkent-khanate does not need a dossier.
2. **Blocking: /ledger/4 (1677 gain of "Dzungaria" from khoshut-khanate).** Dzungaria is already inside the dossier's own keyframe dzungar-khanate_1658 (839,091 km2, drawn 1658-1676), so the event moves no land. khoshut-khanate (1637-1717, Qinghai and Tibet) never held Dzungaria and has no 1677 loss. Ochirtu's Khoshuts were an Oirat group inside the land already drawn. The Galdan page gives the year as 1678: "In 1678 Galdan forced Ochirtu to flee to Kokonur and established hegemony over the Oirats". Fix: drop the gain and keep the war with empty zones and a note, or use a string counterpart and a region outside the 1658-1676 keyframe.
3. **Blocking: the 1696 loss of Hami is missing.** The Dzungar page, which the author opened, says: "Abdullah Tarkhan Beg of Hami also rebelled in 1696 and defected to the Qing dynasty". It also has "In 1698, Qing troops were stationed in Hami". The notes and the report say no page dates a loss of Hami, which is wrong. Fix: add a 1696 loss of `{place: Hami, km: r}` with counterpart qing-dynasty (Hami is in the gazetteer). Then mark the keyframes from 1696 on as adjust, minus Hami, or explain in a note why Hami stays Dzungar.
4. **Advisory: /ledger/17 note.** The Kazakh-Dzungar Wars page says the 1723 campaign "also captured Khujand, Samarkand, and Andijan, occupying the Fergana Valley", but the note calls these raids. Either add an occupation of Fergana, mirrored in khanate-of-kokand, or justify the reading.
5. **Advisory: /ledger/23.** The 1757 loss of the Tarim Basin is confirmed on the Galdan page ("The Dzungars kept control over the Tarim Basin until 1757"). But the land went to the Aq Taghliq khojas, and the Qing pacified it only in 1759. Name that regime, or say why the counterpart is qing-dynasty.
6. Spot checks, all confirmed: 1658 Semirechye (Kazakh-Dzungar Wars page); 1680 Tarim and 1696 Outer Mongolia (Dzungar page); August 1688 Khalkha (Galdan page, 3 August); 1745 Jetisu and Tashkent ("controlled Jetisu and Tashkent until 1745"); 1757 Tarim (Galdan page).
7. Area: the infobox gives 3,600,000 km2 for 1650. The Cliopatria row alive in 1650 is 839,091 km2 (ratio 4.29), and the dossier's own 1650 keyframe is 365,737 km2. /keyframe_review/1 acknowledges this (the infobox figure equals the 1687-1695 peak), and I accept it.
8. Thin: Turfan's undated defection to the Qing; the Dzungar hold on Jetisu between 1636 and 1658; how far into Tibet the Dzungars held in 1717-1720.

## khanate-of-kokand (thin)

- Spot checks, all confirmed: 1709 founding (Kokand page); 1765 Tashkent ("temporarily took control of Tashkent in 1765 before Ablay Khan retook it"); 1853 Ak-Mechet; September 1861 Yany-Kurgan; June 1864 Turkestan; 29 June 1865 Tashkent.
- The Kokand page has no 1868 treaty and no protectorate, so the author is right to add no vassal event.
- Area: the infobox gives 647,497 km2 for the late 1830s against 475,816 km2 in Cliopatria (ratio 0.73). This is acknowledged.
- Advisory: Shymkent, taken in 1864 on the second attack (Russian conquest page), has no loss event. Only keyframe 1864b records it.
- Thin, for gap-fillers:
  - /ledger/9: the 1822 growth of 301,000 km2. Try the Umar Khan and Madali Khan pages for the dates of the steppe forts.
  - /ledger/8: the 1809 Syr Darya lands.
  - /ledger/5-6: the Uroteppa contest of 1785 and 1788. Also, Abd al-Rahim Biy "briefly occupied Khujand, Urateppe, and the remnants of Samarkand" in the 1720s-1730s (Kokand page), which has no event.
  - Bukhara's seizure of Istaravshan and Khujand and Kokand's tribute in 1839-1842. These are in /wars/1 but have no ledger events.
  - The reigns of 1858-1862 and 1863-1865.

## hotaki-dynasty (thin)

- **Applied:** /ledger/12 (Shiraz, Kashan, 1723), confidence lowered from 2 to 1. The Mahmud page gives no year.
- Advisory: keyframe hotaki-dynasty_1722 draws Shiraz and Kashan from 1722, but the ledger has them in 1723. Align the two.
- Spot checks, all confirmed:
  - 21 April 1709 revolt (Hotak infobox).
  - October 1721 Kerman ("easily conquered the Kirman town but failed to take its citadel on October 1721").
  - 23 October 1722 Isfahan.
  - Khorramabad in November 1726 and the agreement of October 1727 (Ashraf page).
  - Ashraf fled Isfahan on 13 November 1729.
  - Kandahar fell on 24 March 1738 (Hotak infobox).
- Area: the infobox gives none.
- Thin:
  - /ledger/4: the 1718 Sistan, Balochistan and Makran gain (about 400,000 km2) is a confidence-1 bridge.
  - /wars/4: the siege of Kandahar has a zone but no contest_start for 1737. Its page did not load for the author.
  - The west edge of the 1727-1733 shape.

## kalmyk-khanate (thin)

- **Applied:** /ledger/2 and /ledger/3 (1634), confidence lowered from 3 to 2. The Nogai page dates the defeat ("Conquered by the Kalmyk Khanate: 1634"; "1634 major defeat of Nogais by Kalmyks") but names no land.
- Advisory: keyframe kalmyk-khanate_1632 is marked ok for 1632-1635, but the 1634 gain of the Small Horde strip (25,293 km2) reaches the map only in 1636.
- Spot checks, all confirmed: 1630 arrival; about 1632 the first Nogai group broken up; 1634; October 1771 abolition.
- Area: the infobox gives none.
- Mismatch to fix in the other dossier: **nogai-horde** /ledger/14 dates its loss to the Kalmyks 1636 at confidence 1. The Nogai page's infobox says 1634, so that side should move to 1634.
- Thin:
  - /ledger/4: the 1636 growth of 105,000 km2 is a gain from "nobody". The Kalmyk page has the Oirats "expelling ... the Nogai Horde", so the counterpart is probably nogai-horde.
  - /ledger/5: the 1738 growth.
  - The Russian oaths and treaties ("Numerous oaths and treaties were signed", undated).
  - No capital.

## oirat-confederation (fix)

- **Applied:** /ledger/1 (the 1628 split), confidence lowered from 3 to 2. The page dates the move ("In 1628, the Torghut chief Khoo Orlug ... moved westward across the Kazakh steppes") but names no land.
- Advisory: the split's region is the Kalmyk Khanate's Volga shape, land the Oirat Confederation never held. Its mirror, kalmyk-khanate's found event, is dated 1630 and names nogai-horde. In the note, say that the split carries people and no Oirat land, and align the year or the mirror.
- Spot checks, all confirmed: the 1609-1616 campaigns (Dzungar page); 1628; "Disestablished: 1634".
- Thin: the 1609 founding is a confidence-1 bridge; the union of about 1620.

## Cross-dossier matrix (summary)

- **Matched:**
  - Dzungar with kazakh-khanate: 1684, 1687, the 1723 occupation and its 1745 end.
  - Dzungar with eastern-moghulistan: 1680, after my fix.
  - Dzungar with khoshut-khanate: Tibet in 1717.
  - Kokand with khanate-of-bukhara: 1709, and the Uroteppa contest of 1734-1785.
  - Kokand with kazakh-khanate: 1765, 1809 and 1822.
  - Kalmyk with nogai-horde: the 1632 contest.
  - Oirat with Dzungar: the 1634 handoff.
- **Mismatch:**
  - kazakh-khanate 1643 and 1658: the counterpart slug is wrong (fix on the Kazakh side).
  - nogai-horde: 1636 against 1634 (fix on the Nogai side).
  - Oirat 1628 split against Kalmyk 1630 found.
- **Missing:**
  - Dzungar 1677: khoshut-khanate has no mirror.
  - Dzungar 1696: the loss of Hami.
- **Exceptions:**
  - Counterpart dossiers not yet written: qing-dynasty, russian-empire, safavid-dynasty, afsharid-iran, ottoman-empire, emirate-of-bukhara.
  - Counterparts listed as needing dossiers: khalkha-khanates, kumul-khanate, tashkent-state, kara-kyrgyz-khanate, and a suggested altishahr-khojas (1757-1759).
  - Counterpart "nobody": the Kalmyk gains of 1636 and 1738.
