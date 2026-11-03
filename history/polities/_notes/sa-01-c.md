# sa-01-c: what could not be settled

Six dossiers, written 2026-10-18 from eight Wikipedia pages (Haryanka dynasty, Bimbisara, Ajatashatru, Vajjika League, Matsya (tribe), Pañcāla, Surasena, Vatsa). No page failed to load. Page budget was 1-2 per state: the five janapadas used 1 page each (Vajji 2 including Ajatashatru); the Haryanka dossier used 4 (its own article gives no date for Anga, Vajji or Kosala, so the Bimbisara, Ajatashatru and Vajjika League pages were opened).

## All five janapadas (Matsya, Pancala, Surasena, Vajji, Vatsa)
- Cliopatria draws each as a disc of about 4,000-5,500 km2; all sixteen Mahajanapada rows are the same kind of disc. Each page names a far larger country, so every shape is `adjust`. The corrected regions are my reading of the page's place names (radii round Alwar, Jaipur, Mathura, Allahabad, Kannauj, Kanpur; the gazetteer's Rohilkhand; a ten-point polygon for the Vajjika League's four stated boundaries). No page gives an area, so no infobox comparison was possible.
- `start` is -600, Cliopatria's first year, with a confidence-1 `found` event. The pages date the origin earlier (Matsya c. 1400 BCE, Pancala c. 1100, Surasena and Vatsa c. 700); that earlier life belongs to the Vedic janapadas additions (sa-01-x).
- Coordinates of capitals not in the gazetteer (Bairat, Kampilya, Ahichchhatra, Kausambi, Vaishali) are approximate and mine; the pages give none.

## Matsya, Pancala, Surasena: extended past Cliopatria's -405
- Cliopatria ends the three rows in -405. Its Shaishunaga shape (-404..-334) holds none of their cells; its Nanda shape from -333 holds all of them. Without an extension the land is stateless -404..-334. The dossiers therefore add a keyframe `<slug>_-404` and end at the page's date: Matsya -350 (infobox c. 350 BCE, "eventually conquered by the empire of Magadha"), Pancala -340 (infobox c. 340; text "annexed ... during the reign of Mahapadma Nanda in the mid-4th century BCE"), Surasena -334 (confidence 1; the page's infobox says c. 300 BCE, which would overlap the Nanda and Maurya shapes).
- Counterpart for all three is `nanda-empire`; only Pancala's page names the Nandas. The Nanda dossier (other part of sa-01) should carry the matching gains, and unless it starts before -333 there are gaps of 16 (Matsya), 6 (Pancala) and 0 (Surasena) years.

## Vajji
- Cliopatria's Vajji row ends -481 but its "Mahajanapadas" row (slug `mahajanapadas`, -480..-451, 5,163.5 km2, bbox identical to Vajji's) repeats the shape. The page has the league beaten and annexed by 468 BCE, so Vajji runs to -468 with a new keyframe `janapada-of-vajji_-480`; the `mahajanapadas` dossier (another part) should treat that row as Vajji and not as a state.
- Contest -481..-468: the pages give a feud 484-468 and Basham's campaigns of 485 and 481-480, but not when ground was first taken; the contest starts with the second campaign.
- Predecessor `videha` has no Cliopatria row and no dossier (the page: "Preceded by Videha"; Maha-Videha "around 800 BCE").

## Vatsa
- The page is silent on every date. The end -451 (to `janapada-of-avanti`, matching that dossier's gain c. 450) is Cliopatria's row end, confidence 1. The infobox "c. 300 BCE" does not fit the page's own text (Avanti first, then Magadha under Shishunaga).
- Cliopatria's Haryanka shape from -450 contains all of Vatsa's disc, which the page does not support; the Haryanka dossier cuts it out.

## Haryanka dynasty
- START: infobox "Established: 544 BCE", Bimbisara "founder"; Cliopatria's row and this dossier start -500, after janapada-of-magadha ends -501. A reviewer may prefer to end that dossier at -545 and start this one at -544.
- END: infobox 413 BCE (succession box 425); Cliopatria's shape runs to -405 and its Shaishunaga row starts -404. This dossier ends -413; the Shaishunaga dossier should start in 413 or -412..-405 is a gap.
- Keyframes: -500 ok; -480 adjusted to -480..-469; new -468..-451 (adds the Vajjika country and the Mallas); -450 adjusted to -450..-413 (adds the whole Vajji polygon, removes Vatsa). Unverified: the southern and eastern fringe of the -480 shape down to 21.3N, and the 335,215 km2 total of the -450 shape (no page gives an area or boundary).
- Confidence-1 events: the 500 `found`, the -480 gain of "the smaller kingdoms" (counterpart now nobody), the -460 capital move to Pataliputra (page: "during the reign of Udayin", undated), the -450 gains of Kasi-Kosala and Cedi (the pages date neither; Cliopatria's shape boundary is used). Cedi was kept only because no page gives it to anyone else (superseded: the Cedi gain is deleted, see the repair section at the end).
- The Magadha-Kosala war over Kashi (after Bimbisara's murder, peace treaty, Vajira) is listed with empty zones and Ajatashatru's reign as its span; the page dates nothing in it, so no contest is drawn.
- Chronology: the Mahavamsa dates on the Haryanka infobox differ by 1-3 years from the Bimbisara and Ajatashatru pages, and the short chronology (Bimbisara r. 457-405) is about 90 years later. The map follows the Haryanka page and Cliopatria. The ruler strip is the infobox list; Darshaka (437) is in the page body but not the infobox.
- The Anga annexation (c. 530) is in the janapada-of-magadha dossier; this dossier inherits it.

## Gazetteer names wanted
Vaishali, Kaushambi, Bairat / Viratanagara, Kampilya, Ahichchhatra, Champa (Anga) (places); Terai, Videha / Mithila, Matsya, Panchala, Braj, North Bihar (regions); Mahananda (river).

## Repair of magadha-haryanka-dynasty (2026-10-18, reviewer verdict fail)
Pages re-read with WebFetch: Haryanka dynasty (infobox 'Established: 544 BCE', 'Disestablished: 413 BCE', '544-492 BCE: Bimbisara'; Pataliputra 'during the reign of Udayin', undated), Ajatashatru (regnal table 'Ajatashatru 493 BCE-461 BCE'; body 'c. 492 to 460 BCE'; 'not only conquered Vaishali but also Kasi-Kosala'; neither Chedi nor Cedi appears), Vajjika League (league 'bounded to the north, east, south, and west, respectively, by the Himalaya mountains and the Mahananda, Ganga, and Sadanira rivers'). One new page: Magadha ('expanded to include most of Bihar and Bengal with the conquest of Vajjika League and Anga, respectively'; undated; no area; no Kasi, Kosala, Cedi, Malla; Pataliputra undated). That makes five pages against the 1-2 budget.
Applied (all six findings):
- Ledger Cedi gain (-450) deleted. Cliopatria's Cedi disc is 18 cells, none inside the dossier's shape (the Allahabad 80 km cut takes them all), and no page mentions Cedi. Cedi's fate is unknown; its land is nobody's from -451, which matches janapada-of-cedi (dissolve, counterpart null). I did not point the event at Cedi's corrected land, so the Cedi author has nothing to change.
- Kasi-Kosala: the gain region is janapada-of-kosala's /keyframe_review/1/correction (231 cells); the same spec is in the union of the -450 keyframe and of the dissolve. The -450 shape is now 1,323 cells (about 345,000 km2, unverified).
- Keyframe 0 is adjust: janapada-of-magadha's -530 correction minus the Vajji polygon = 92 cells (the minus takes out 15 of Magadha's 107; its Patna 45 km circle crosses the Ganga). The found event has the same region. Keyframe 1 carries the same minus. predecessors[0].land is Magadha's -530 correction. Bimbisara's `from` is -500 and the 544 stays in his note. Ajatashatru's note now reads 493-461 (regnal table).
Where I differ from the reviewer:
- Keyframe 1: the reviewer asked for the minus alone. I also union Magadha's -530 land into it, because Cliopatria's -480 shape omits 16 cells of that land and they would vanish at -480 with no event, the same fault finding 3 names for -500. The -480 gain region is therefore the -480 shape minus Magadha's land and the Vajji polygon (251 cells), counterpart nobody (reviewer's thin advice), confidence 1.
- Ledger 8 (new, not asked): the -450 shape adds 722 cells over -468; the Kosala-Kasi gain explains 222, and 500 cells (80.94-88.53E 21.49-27.74N) are explained by no page opened. A confidence-1 gain from nobody bridges them so every border move has an event. If the reviewer prefers the gap to a bridge, delete ledger 8 and cut those cells from the -450 correction.
- The Kosala gain region is Kosala's correction in full, as asked; 9 of its cells lie in the Allahabad 80 km circle that the -450 keyframe leaves to Vatsa, so the keyframe holds 222 of the event's 231 cells. The cause is the Vatsa circle (Avanti takes only 15 of Vatsa's 80 cells), not this dossier.
Still thin, by design under the budget: the Pataliputra move (no year on any page opened; pages to try: Udayin), the -500 found (Cliopatria's boundary; the page has 544; orchestrator decision), the Kasi-Kosala year (the Magadha page does not date it either; page to try: Kosala), the 345,000 km2 total.
For other authors: janapada-of-magadha's correction overlaps the Vajji polygon by 15 cells; janapada-of-kosala's overlaps Vatsa's Allahabad circle by 9; janapada-of-avanti takes 15 of Vatsa's 80 cells; the Shaishunaga dossier should start at 413 to close the -412..-405 gap. One cell (86.69E 21.86N) is in Cliopatria's -480 shape but not its -450 shape.
