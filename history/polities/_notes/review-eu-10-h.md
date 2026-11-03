# Review of batch eu-10-h (France, part h)

Reviewed 2026-10-25 by the adversarial reviewer. The validator gives 0 errors on all five dossiers; house-of-bourbon has 5 warnings, all for the place 'Vendôme', which the gazetteer lacks. No Context neighbour dossier exists yet, so every external mirror is an exception and is routed below. Spot checks used WebFetch on Wikipedia.

| slug | verdict |
| --- | --- |
| comtat-venaissin | thin |
| house-of-bourbon | fail |
| house-of-valois-anjou | thin |
| county-of-bearn | fail |
| huguenots | pass |

## comtat-venaissin: thin

Area: The infobox has no area, and the dossier notes say so. (Cliopatria max 2437.2 km2).

Gaps for a gap-filler:
- `/ledger/4`: End of the 1663 French occupation (bridged in the same year at confidence 1). The Comtat page lists only '1663, 1668, 1768-1774'. Try: https://fr.wikipedia.org/wiki/Comtat_Venaissin ; https://en.wikipedia.org/wiki/Treaty_of_Pisa_(1664)
- `/ledger/6`: End of the 1668 occupation (bridged in the same year at confidence 1). The author notes that a 1688-1689 occupation is not on the page. Try: https://fr.wikipedia.org/wiki/Comtat_Venaissin
- `/keyframe_review/1 and /keyframe_review/2`: No page dates the one-cell additions in 1352 and 1385. The Valreas exclave ('purchased by Pope John XXII', per the Comtat page) has no year, so no event. Try: https://en.wikipedia.org/wiki/Valr%C3%A9as

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Comtat_Venaissin): confirmed: 'The Comtat became a Papal territory in 1274'; infobox 'Annexed as a Papal state: 1274'
- `/ledger/1` (https://en.wikipedia.org/wiki/Comtat_Venaissin): confirmed: Venasque 'replaced as capital by Carpentras in 1320'
- `/ledger/2` (https://en.wikipedia.org/wiki/Comtat_Venaissin): confirmed: 'Avignon was sold to the papacy by Joanna I, Queen of Naples and Countess of Provence, in 1348'
- `/ledger/3, /ledger/5, /ledger/7, /ledger/8` (https://en.wikipedia.org/wiki/Comtat_Venaissin): confirmed: 'It was invaded by French troops in 1663, 1668 and 1768-1774'
- `/ledger/9` (https://en.wikipedia.org/wiki/Comtat_Venaissin): confirmed: infobox 'Reversed into France by plebiscite: 14 September 1791'

## house-of-bourbon: fail

Area: The House of Bourbon page is a dynasty page with no area field. (Cliopatria max 74304.4 km2).

Findings:
- `/ledger/2, /keyframe_review/1, /keyframe_review/2` (for the author): Blocking: the La Marche loss is dated 1362, and the 1333 and 1352 keyframes are marked ok with La Marche in them. By the pages the author opened, La Marche left the ducal line in 1341, when Louis I's younger son James took it. Nothing changed hands in 1362: the county passed from James I to his son within the same cadet line. Evidence: County of La Marche list: 'Louis I of Bourbon (1322-1341)', then 'James I of Bourbon (1341-1362)'. Duke of Bourbon table: Peter I is duke 1341-1356. House of Bourbon page: 'The remaining line of Bourbons henceforth descended from James I, Count of La Marche, the younger son of Louis I, Duke of Bourbon.' The ledger note says 'The page gives no kinship between the dukes and the La Marche line', but the House page gives it. The K2 note itself says La Marche went to James I, 'not to the dukes Peter I and Louis II'. Fix: Move the loss to 1341. Use counterpart county-of-la-marche, or 'James I of Bourbon, Count of La Marche'. Change the 1333 keyframe to adjust: the Cliopatria 1333 shape, held 1333-1341 only. Add a new keyframe for 1342-1351 and change the 1352 keyframe to adjust. Both take the Cliopatria 1363 shape (the Bourbonnais alone). Rewrite the K2, K3 and ledger notes.
- `/ledger/5, /keyframe_review/11, /keyframe_review/12` (for the author): Blocking (same rule as above): the dossier counts La Marche from 1477 under Peter II (Pierre de Beaujeu), who was not duke until 1488. In 1341 the dossier treats La Marche held by a cadet as a loss. The two cases follow opposite rules. Evidence: Duke of Bourbon table: Peter II is duke 1488-1503. La Marche list: 'Peter II of Bourbon (1477-1503)'. The K11 note itself says 'he held it first in his own right'. Fix: State one rule in notes. If the rule is the ducal domain, which the rest of the dossier uses: date the La Marche gain to 1488, when Peter II became duke, with the 1477 confiscation from Jacques d'Armagnac in the note. Drop new keyframe K11 (1477-1481) and keep K12 (1482-1491) as Cliopatria's 1482 shape until 1487, with the 1492 shape from 1488. If the rule is the whole house: keep 1477, but then La Marche stays until the Armagnac marriage (1435/1438) and the 1362 loss is dropped.
- `/keyframe_review/17 and /ledger (between /ledger/7 and /ledger/8)` (for the author): Blocking: the Vendome duchy enters the dossier in 1523 (new keyframe 1523-1554, capital Vendome from 1524) with no ledger event. The only events near it are the August 1523 loss of the Bourbon lands and the 1527 rename. Evidence: Rule 4: between two keyframes the ledger must explain a change in extent. The House page dates the hand-over of the senior line to 1527: 'The senior line of the House of Bourbon became extinct in the male line in 1527'; 'In 1514, Charles, Count of Vendome had his title raised to Duke of Vendome'. From August 1523 Charles III held nothing in France. Fix: Add a gain of the Vendome land, with counterpart 'Duchy of Vendome (Bourbon-Vendome branch)', in the year the dossier passes to that branch: 1527 with the rename, as the House page dates it. Start K17 and the Vendome capital in that year, and say in the notes what the state holds in 1523-1526 (nothing, or Charles III in exile).
- `/identity/rulers` (for the author): The ruler strip has a gap between 1523 and 1555. Its 1555 entry is Jeanne III of Navarre (an Albret). Antoine de Bourbon, joint ruler from 25 May 1555, has no entry. Evidence: Brief rule 9: rulers must be contiguous. House page: 'Antoine became King of Navarre, on the northern side of the Pyrenees, by marriage in 1555'. Jeanne d'Albret page: Jeanne and her husband 'became joint rulers of Navarre' on 25 May 1555. Fix: Add the Bourbon-Vendome heads, Charles, Duke of Vendome (to 1537) and Antoine (1537-1562), from a page. Or end the strip in 1523 and restart it in 1555 with Antoine and Jeanne, and say so in a note.
- `/ledger/4/counterpart` (for the author): The 1416 Auvergne gain names county-of-auvergne as the counterpart. The page says the land came 'with the death of John of Valois', that is John, Duke of Berry, who held Auvergne as a duchy. Evidence: Duke of Bourbon page: 'In 1416, with the death of John of Valois, the Dukes of Bourbon were simultaneously Dukes of Auvergne.' Cliopatria's County of Auvergne row has no shape between 1407 and 1439, and its 1440 shape is 706 km2, so that dossier is unlikely to hold a 1416 loss. Fix: Use counterpart 'Duchy of Auvergne (John, Duke of Berry)', or agree the counterpart with the eu-10 author of county-of-auvergne. Not blocking.

Gaps for a gap-filler:
- `/keyframe_review/5, /keyframe_review/6, /keyframe_review/7`: Dates for the Beaujolais (about 1400) and Dombes (about 1402) acquisitions behind the 1385-1407 shape steps. The keyframes are marked 'unverified: page budget'. Try: https://en.wikipedia.org/wiki/Principality_of_Dombes ; https://fr.wikipedia.org/wiki/Beaujolais_(province)

Spot checks:
- `/ledger/1` (https://en.wikipedia.org/wiki/County_of_La_Marche): confirmed at confidence 2: 'in 1327, La Marche passed into the hands of the House of Bourbon'. The list dates the exchange to 1322, and the author flags the conflict.
- `/ledger/2` (https://en.wikipedia.org/wiki/County_of_La_Marche): mis-dated: the list puts James I of Bourbon in 1341-1362, and the House of Bourbon page calls him 'the younger son of Louis I'. The county left the dukes in 1341, not 1362.
- `/ledger/4` (https://en.wikipedia.org/wiki/Duke_of_Bourbon): confirmed: 'In 1416, with the death of John of Valois, the Dukes of Bourbon were simultaneously Dukes of Auvergne.'
- `/ledger/6` (https://en.wikipedia.org/wiki/Charles_III,_Duke_of_Bourbon): confirmed: 'On 10 May 1505, the fifteen-year-old Charles de Bourbon married the fourteen-year-old Suzanne de Bourbon.'
- `/ledger/7` (https://en.wikipedia.org/wiki/Charles_III,_Duke_of_Bourbon): confirmed: 'In August 1523, all the disputed lands were sequestered from Bourbon.'
- `/ledger/8` (https://en.wikipedia.org/wiki/House_of_Bourbon): confirmed: 'The senior line of the House of Bourbon became extinct in the male line in 1527'
- `/ledger/9, /ledger/10, /ledger/11` (https://en.wikipedia.org/wiki/Jeanne_d%27Albret): confirmed: 'On 25 May 1555, Henry II of Navarre died, at which time Jeanne and her husband became joint rulers of Navarre'; she is styled Countess of Foix and of Bigorre, 1555-1572.

## house-of-valois-anjou: thin

Area: The House of Valois-Anjou page infobox has no area field. (Cliopatria max 63319.1 km2).

Findings:
- `/ledger/8/month` (applied by reviewer): Added month 1 to the 1431 Lorraine gain. Evidence: René of Anjou infobox: Duke of Lorraine (jure uxoris, co-ruler Isabella) '25 January 1431 - 28 February 1453'. Fix: month: 1, with a sentence added to the note. Re-validated: 0 errors, 0 warnings.
- `/keyframe_review/9/note` (applied by reviewer): The note said 'the René page does not say who ruled Lorraine after 1453'. The page does say it. Evidence: René page: 'René now made over the government of Lorraine to his son John, who was, however, only formally installed as Duke of Lorraine on the death of René's wife Isabella in 1453'; the infobox gives John II as successor. Fix: Rewrote that sentence with the quote and René's reign dates, and said that no ledger event records the 1453 transfer yet.
- `/ledger/8/note` (for the author): The note says 'Cliopatria adds the land only in 1440, which fits the captivity', but keyframe 6 (1431-1439) adds Lorraine from 1431. Evidence: Internal contradiction between the note and /keyframe_review/6/correction. Fix: Delete the sentence or reconcile it with K6. Not blocking.

Gaps for a gap-filler:
- `/keyframe_review/9 and /ledger (after /ledger/8)`: The 1453 change of hands in Lorraine has no event. The René page dates it: René's Lorraine reign ends 28 February 1453 and his son John (II) succeeds. Add a loss to duchy-of-lorraine in 1453 at confidence 3. Alternatively, if the dynasty dossier keeps Lorraine under John II and Nicholas (both Valois-Anjou), give an end year from a page. Try: https://en.wikipedia.org/wiki/Ren%C3%A9_of_Anjou ; https://en.wikipedia.org/wiki/John_II,_Duke_of_Lorraine
- `/keyframe_review/5, /keyframe_review/7, /keyframe_review/8`: Maine leaves in 1429, is back by 1440 and leaves again in 1450, with no events (keyframes marked 'unverified: page budget'). The René page has 'At the death of his brother Louis III in 1435, he succeeded to the Duchy of Anjou and County of Maine'. Missing: the English occupation of Maine and the county's grant to Charles of Maine. Try: https://en.wikipedia.org/wiki/Maine_(province) ; https://en.wikipedia.org/wiki/Charles_IV,_Duke_of_Anjou
- `/ledger/2`: Touraine is gained in 1370 at confidence 2 and never lost. Try: https://en.wikipedia.org/wiki/Duke_of_Touraine
- `/ledger/9`: The René page says 'King Louis XI seized Anjou and Bar', but the occupation covers Anjou only. Bar's seizure and its hand-over (to René II, 1480 or later) are not recorded. Try: https://en.wikipedia.org/wiki/Duchy_of_Bar

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/House_of_Valois-Anjou): confirmed: 'In 1356, Philip's son and heir, king John II, gave the County of Anjou to his son Louis'
- `/ledger/3` (https://en.wikipedia.org/wiki/County_of_Provence): confirmed: 'Thus in 1382, when she died, two pretenders claimed to inherite Provence, Louis of Anjou and Charles of Naples'
- `/ledger/6` (https://en.wikipedia.org/wiki/County_of_Provence): confirmed: 'This led, in 1388, to the separation of the city of Nice and its corresponding administrative division (the viguerie)'
- `/ledger/7, /ledger/8` (https://en.wikipedia.org/wiki/Ren%C3%A9_of_Anjou): confirmed: 'When Louis of Bar died in 1430, René inherited the duchy of Bar'; 'The next year, on his father-in-law's death, he succeeded to the duchy of Lorraine' (infobox from 25 January 1431)
- `/ledger/11, /ledger/12` (https://en.wikipedia.org/wiki/Ren%C3%A9_of_Anjou): confirmed: 'René died on 10 July 1480 at Aix'; the 1474 will 'left Bar to his grandson René II, Duke of Lorraine'
- `/ledger/13` (https://en.wikipedia.org/wiki/County_of_Provence): confirmed: 'On December 10, 1481, Count Charles III of Provence dictated a will naming King Louis XI of France as his universal heir'

## county-of-bearn: fail

Area: The Béarn page infobox has no area. The corrected shape (Béarn region of 31 cells plus the 17-cell polygon, about 12,000 km2) is about three times Cliopatria's area, and no note acknowledges it. (Cliopatria max 3806.1 km2).

Findings:
- `/keyframe_review/1..5/correction, /ledger/4/region, /identity/successors/0/land` (for the author): Blocking: from 1379 every correction is union(Béarn, Cliopatria's County of Béarn polygon). That union leaves out the core of Bigorre, which /ledger/1 gains at confidence 3: 13 of the 20 Hautes-Pyrénées cells (about 3,300 km2, bbox -0.25..0.21 E), including Tarbes and Lourdes. The keyframes never draw land the ledger says was gained. Evidence: Gazetteer resolve: Cliopatria County of Béarn 1450 = 17 cells, bbox 0.27-0.93 E. Hautes-Pyrénées minus (Béarn ∪ that polygon) = 13 cells, bbox -0.25..0.21 E. Tarbes is at 0.08 E. Gaston III page: '26 conventions were signed between Fébus and Bigorrian communities, and Tarbes was the last to cede on 27 November 1379.' The K2 note calls the polygon 'Bigorre and the Nebouzan', but it lies east of Bigorre's core. Fix: Add {"admin1": "Hautes-Pyrénées", "country": "France"} to the union in K1-K5, in /ledger/4/region and in the successor land. Make the matching change in house-of-bourbon /ledger/9. Correct the K2 note: the polygon is eastern Hautes-Pyrénées and the Nébouzan or Comminges.
- `/keyframe_review/0 -> /keyframe_review/1` (for the author): The Haute-Garonne (Nébouzan) cells of the Cliopatria polygon enter in 1379 with no event. /ledger/1 gains only Hautes-Pyrénées. Evidence: The Gaston III page names 'the small but strategic province of Nébouzan' among the house's holdings, without a date. K0 (1347-1378) is Béarn alone. Fix: Either include the Nébouzan from 1347 in K0, as the house's land, or add an event with its year. Part of the blocking correction fix above.
- `/keyframe_review/0/correction (region 'Béarn')` (for the author): The region 'Béarn' resolves in the gazetteer to all of Pyrénées-Atlantiques: 31 cells, about 7,840 km2, bbox -1.57..-0.04 E. That includes Labourd, Lower Navarre and Soule, which the dossier's own text puts outside Béarn ('bordered by Soule and Lower Navarre to the west'). With the polygon added, the drawn shape is about 12,000 km2, three times Cliopatria's 3,806 km2, and no note says so. Evidence: Gazetteer resolve: region Bearn (confidence 2) matched admin1 Pyrénées-Atlantiques. Fix: Ask for a refined gazetteer region (listed under gazetteer_names_needed), or subtract the Basque provinces in the corrections. Acknowledge the area in the K0 note. Not blocking on its own.

Gaps for a gap-filler:
- `/ledger/1 and /keyframe_review/2..5`: Who held Bigorre after 1390. The Gaston III page says the 1390 Treaty of Toulouse was made 'in exchange for gold payment and the temporary cession of Bigorre' and that Fébus 'received a life annuity for Bigorre'. The dossier keeps Bigorre until 1555 with no page for 1391-1554. Try: https://en.wikipedia.org/wiki/County_of_Bigorre
- `/keyframe_review/5`: Béarn 1453-1554 is carried forward at confidence 1: the union with Navarre under the Foix-Grailly and Albret kings is missing. Try: https://en.wikipedia.org/wiki/Catherine_of_Navarre ; https://en.wikipedia.org/wiki/Kingdom_of_Navarre

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/B%C3%A9arn): confirmed: 'On 25 September 1347, he declared to an envoy of Philip VI that Bearn was a land that he' 'had from God and from no man in the world'
- `/ledger/1` (https://en.wikipedia.org/wiki/Gaston_III,_Count_of_Foix): confirmed: 'Tarbes was the last to cede on 27 November 1379'
- `/ledger/2` (https://en.wikipedia.org/wiki/Gaston_III,_Count_of_Foix): confirmed: died 1 August 1391; Estates of Béarn on 8 August 1391; Charles VI's letters patent of 20 December 1391
- `/ledger/3` (https://en.wikipedia.org/wiki/B%C3%A9arn): confirmed: 'transferring his court from Orthez to Pau in 1464'
- `/ledger/4` (https://en.wikipedia.org/wiki/Jeanne_d%27Albret): confirmed: 25 May 1555 joint accession

## huguenots: pass

Area: The Huguenots page is not a state page and has no area. Tried and could not break: the years and months, the contest pair against the war zones, La Rochelle lying just outside the Cliopatria polygon (46.17 N against 46.15 N), and K2 holding to 1629 only. (Cliopatria max 1916.0 km2).

Spot checks:
- `/ledger/0` (https://en.wikipedia.org/wiki/Siege_of_La_Rochelle): confirmed: 'In 1621, Louis re-established Catholicism in the formerly Huguenot region of Béarn' 'resulting in an uprising led by Henri de Rohan and his brother Soubise'
- `/ledger/1` (https://en.wikipedia.org/wiki/Siege_of_La_Rochelle): confirmed: 'On September 10, the first cannon shots were fired by La Rochelle against royal troops at Fort Louis' (infobox 10 September 1627)
- `/ledger/2, /ledger/3` (https://en.wikipedia.org/wiki/Siege_of_La_Rochelle): confirmed: 'the city surrendered on 28 October 1628.'
- `/ledger/4` (https://en.wikipedia.org/wiki/Huguenots): confirmed: 'Even before the Edict of Alès (1629), Protestant rule was dead'; rebellions 'between 1621 and 1629'

## Cross-dossier matrix

- comtat-venaissin 1348 gain <- capetian-house-of-anjou: **exception**. eu-10: counterpart's dossier not written yet (owning group has not run). Its ledger should hold a 1348 sale of Avignon.
- comtat-venaissin 1663 occupation_start <- kingdom-of-france: **exception**. eu-10: counterpart's dossier not written yet (owning group has not run). The 1663 and 1668 ends are bridged at confidence 1.
- comtat-venaissin 1668 occupation_start <- kingdom-of-france: **exception**. eu-10: counterpart's dossier not written yet (owning group has not run). The 1663 and 1668 ends are bridged at confidence 1.
- comtat-venaissin 1768 occupation_start <- kingdom-of-france: **exception**. eu-10: counterpart's dossier not written yet (owning group has not run). The 1663 and 1668 ends are bridged at confidence 1.
- house-of-bourbon 1327 gain <- kingdom-of-france: **exception**. eu-10: counterpart's dossier not written yet (owning group has not run). La Marche was exchanged for Clermont; the page dates it 1322 or 1327.
- house-of-bourbon 1362 loss <- Bourbon-La Marche (cadet line of the Counts of La Marche): **exception**. Counterpart listed for a new dossier (county-of-la-marche). The event is mis-dated: the pages give 1341, when James I, the younger son of Louis I, took La Marche.
- house-of-bourbon 1372 gain <- County of Forez (Anne of Auvergne): **exception**. Counterpart listed for a new dossier (county-of-forez).
- house-of-bourbon 1416 gain <- county-of-auvergne: **exception**. eu-10: counterpart's dossier not written yet (owning group has not run). The counterpart is doubtful: the page says the land came with the death of John of Valois (Duke of Berry), and Cliopatria's County of Auvergne row has no shape for 1407-1439.
- house-of-bourbon 1477 gain <- kingdom-of-france: **exception**. eu-10: counterpart's dossier not written yet (owning group has not run). Louis XI confiscated La Marche from Jacques d'Armagnac in 1477. Peter II held it but was duke only from 1488 (see fixes).
- house-of-bourbon 1523 loss <- kingdom-of-france: **exception**. eu-10: counterpart's dossier not written yet (owning group has not run). Sequestration of August 1523; merged into the royal domain in 1531.
- house-of-bourbon 1555 gain <- county-of-bearn: **matched** (mirror county-of-bearn 1555 dissolve). Same month and the same region spec on both sides. Both omit Bigorre's core around Tarbes (county-of-bearn finding).
- house-of-bourbon 1555 gain <- county-of-foix: **exception**. eu-10: counterpart's dossier not written yet (owning group has not run). Cliopatria's County of Foix 1552-1555 shape (30,484 km2, from -1.44 E) also covers Béarn and the Albret south-west. The Foix dossier's 1555 end must agree with this dossier's split of the land across /ledger/9-11.
- house-of-bourbon 1555 gain <- Kingdom of Navarre and the House of Albret (Henry II of Navarre): **exception**. Counterpart listed for a new dossier (house-of-albret). Its years should end in 1555, not run 1555-1589.
- house-of-valois-anjou 1370 gain <- county-of-touraine: **exception**. eu-10: counterpart's dossier not written yet (owning group has not run).
- house-of-valois-anjou 1382 gain <- capetian-house-of-anjou: **exception**. eu-10: counterpart's dossier not written yet (owning group has not run). Its ledger should end Provence in 1382, with Joanna I's death and Louis I's succession.
- house-of-valois-anjou 1382 contest_start <- kingdom-of-naples: **exception**. eu-13: counterpart's dossier not written yet (owning group has not run). Union of Aix, 1382-1387.
- house-of-valois-anjou 1388 loss <- county-of-savoy: **exception**. eu-13: counterpart's dossier not written yet (owning group has not run). Nice and the Terres Neuves, 1388.
- house-of-valois-anjou 1430 gain <- Duchy of Bar (Louis, Cardinal of Bar): **exception**. Counterpart listed for a new dossier (duchy-of-bar).
- house-of-valois-anjou 1431 gain <- duchy-of-lorraine: **exception**. eu-09: counterpart's dossier not written yet (owning group has not run). Cliopatria's Duchy of Lorraine row also draws 1431-1439 (17,366 km2), overlapping K6. That row resumes in 1453, which fits the missing 1453 loss (thin).
- house-of-valois-anjou 1474 occupation_start <- kingdom-of-france: **exception**. eu-10: counterpart's dossier not written yet (owning group has not run). Bar is also seized according to the René page, but is not recorded.
- house-of-valois-anjou 1480 loss <- kingdom-of-france: **exception**. eu-10: counterpart's dossier not written yet (owning group has not run). Anjou reunited to the royal domain.
- house-of-valois-anjou 1480 loss <- duchy-of-lorraine: **exception**. eu-09: counterpart's dossier not written yet (owning group has not run). Bar to René II.
- county-of-bearn 1379 gain <- Bigorre (the communities of Bigorre): **exception**. Counterpart listed for a new dossier (county-of-bigorre). The page has Bigorre lost to Fébus at Brétigny (1360), so the 1379 counterpart may be the English side (kingdom-of-england, eu-11).
- huguenots 1628 loss <- kingdom-of-france: **exception**. eu-10: counterpart's dossier not written yet (owning group has not run). La Rochelle surrendered on 28 October 1628.

## Gazetteer names needed

- Vendôme (place, house-of-bourbon): 1.07 E 47.79 N. Used in K17-K20 and /ledger/12. K17 resolves to nothing until it is added. Loir-et-Cher admin1 resolves (27 cells), but it is larger than the duchy.
- Béarn (region, county-of-bearn): Refine: now all of Pyrénées-Atlantiques (31 cells, -1.57..-0.04 E), including Labourd, Lower Navarre and Soule. Béarn proper is the eastern part around Pau, Orthez, Oloron and Morlaàs.
- Bigorre (region, county-of-bearn): Around Tarbes and Lourdes, roughly the western Hautes-Pyrénées.
- Nébouzan (region, county-of-bearn): Around Saint-Gaudens, south Haute-Garonne.
- La Marche (region, house-of-bourbon): Creuse and northern Haute-Vienne.
- Forez (region, house-of-bourbon): Loire department around Montbrison.
- Barrois (region, house-of-valois-anjou): Duchy of Bar around Bar-le-Duc (Meuse).
- Saintonge (region, huguenots): Coastal Charente-Maritime south of the Charente.
- Aunis (region, huguenots): Around La Rochelle.

## Counterparts needing dossiers

- County of La Marche (Bourbon-La Marche line) (`county-of-la-marche`, [1341, 1527]): Separate from the dukes from 1341 (James I); Armagnac 1435-1477; seized by Francis I in 1527.
- County of Forez (`county-of-forez`, [None, 1372]): Passed to Louis II of Bourbon by marriage, 1372.
- Duchy of Bar (`duchy-of-bar`, [None, 1480]): René's from 1430; to René II of Lorraine by the 1474 will.
- County of Bigorre (`county-of-bigorre`, [None, 1379]): Ceded to Fébus in 1379; its status after 1390 is open.
- Albret domain / Kingdom of Navarre north of the Pyrenees (`house-of-albret`, [1484, 1555]): The author listed 1555-1589, but this counterpart gives the land to house-of-bourbon in 1555, so its life ends then. 1484 is approximate and needs a page.
- Huguenot strongholds of the south-west and Languedoc (`huguenots`, [1621, 1629]): Not a new dossier: one rebel polity, one dossier. A gap-filler should add Montauban, Montpellier (to 1622), Castres and Nîmes to the existing huguenots dossier, not create huguenot-strongholds.

## Problems

- No page failed to load. The reviewer edited history/polities/house-of-valois-anjou.json (/ledger/8 month, /keyframe_review/9 note) and re-validated it: 0 errors, 0 warnings.
- None of the 33 Context dossiers in section 6 of the author's brief exists yet, so every external counterpart is an exception. The batch's one internal pair, Béarn and Bourbon in 1555, matches.
