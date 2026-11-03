# Review of batch me-10-d (2026-10-25)

Adversarial review of zand-dynasty, bahrain, kuwait and house-of-khalifa. The validator (with --resolve) gives 0 errors and 0 warnings for all four. I opened 11 pages with WebFetch: Agha Mohammad Khan Qajar, Siege of Basra (1775-1776), Zand Iran, Zand dynasty, History of Bahrain, Nasr Al-Madhkur, Bahrain, History of Kuwait, Saudi Arabian-Kuwaiti neutral zone, Kuwait, House of Khalifa. Machine copy: history/notes/phase-b/reviews/me-10-d.json.

## Verdicts

- zand-dynasty: FAIL. Back to the author.
- bahrain: FIX, made by the reviewer (keyframe 0 changed to adjust for the years).
- kuwait: FIX, made by the reviewer (ledger 8 confidence lowered from 3 to 2).
- house-of-khalifa: FIX, made by the reviewer (sources added to 11 rulers).

## zand-dynasty (fail)

Spot checks: the Basra siege, surrender and occupation (1775-1779), "by 1760", Gilan 1782, Isfahan retaken 20 October 1788, Shiraz 21 July 1792 and the 1794 end are all confirmed. No event is fabricated. The failure is about keyframes and the ledger disagreeing, and the missing events are on a page the author already opened (Agha Mohammad Khan Qajar), so the page budget does not excuse them.

1. Keyframe 7 (1788 shape, 899,495 km2) to keyframe 8 (1791 shape, 620,798 km2): about 279,000 km2 north of 32.3N leave the realm with no loss event. The only event between them is the 1788/10 gain of Isfahan. The page continues: "Agha Mohammad Khan, learning of this, marched rapidly towards Isfahan, which led Jafar Khan withdraw to Shiraz once again and reached the city on 30 November." Add a loss of Isfahan in 1788/11 (cp qajar-dynasty, confidence 2) and stop keyframe 7 drawing the Isfahan half after that date.
2. Keyframe 5 (1780 shape) to keyframe 7 (1788 shape): the north-west and north are lost with no events. These are Azerbaijan, Zanjan, Qazvin, Mazandaran, Golestan, Kurdistan and Kermanshah. The ledger has only Gilan, Tehran, Hamadan with Semnan, and Isfahan. The page has Qazvin and Zanjan seized in 1782 and Mazandaran conquered from Agha Mohammad's brothers (c. 1779). Azerbaijan's khanates were subdued by the Qajar only in spring 1791, so they were not Zand after 1779. Add the losses, or correct keyframe 5.
3. Keyframe 2 (1757 shape) against ledger 2 (the 1760 gain): the realm doubles in the 1757 shape three years before the ledger gains it. The note admits this but changes nothing. Either make it a years-change adjust from 1760, or add a bridging confidence-1 gain in 1757.
4. Non-blocking: keyframe_review lists 1780 before 1776, so swap them. Rulers 1-7 have no source; the Zand dynasty page covers them.
5. Cross-dossier: qajar-dynasty starts in 1789 but is the counterpart of the Zand losses of 1782-1788. qajar-dynasty gains Fars only in 1794, but Shiraz fell on 21 July 1792. ottoman-empire has no event for the 1776-1779 Basra occupation. afsharid-iran gives the Zand everything but Khorasan in 1748, but Zand starts in 1751 and its 1760 gain names afsharid-iran.
6. Thin: the 1751-1752 step and the 1751-1760 conquests (try Azad Khan Afghan, Mohammad Hasan Khan Qajar), the Caucasian khanates (confidence 1 at both ends), and the seat before 1762.
7. Area: neither infobox gives an area, which the author acknowledged.

## bahrain (fix applied)

All four events are confirmed: 1753 on the Bahrain, History of Bahrain and Nasr Al-Madhkur pages; 17 May 1783; 28 July 1783. Keyframe 0 was "ok" although the dossier begins in 1753 and the shape in 1757, which left 1753-1756 with no keyframe. It is now an adjust with the correction "years change only, holds 1753 to July 1783", quoting the Bahrain and History of Bahrain pages. Area: 881.5 km2 against an infobox 786.8 km2 (1.12). For the orchestrator:
- The capital, Bushehr, lies outside the only shape. The dossier is in substance the Bahrain holding of the Sheikhdom of Bushehr.
- Keyframes 1-3 (1820-1845) are marked wrong and fall outside the dossier's life. The compiler must clip them.

## kuwait (fix applied)

Confirmed: 1752, the 1913 convention (80 km, autonomous kaza; 29 July 1913 on the infobox), Jahra on 10 October 1920, Uqair on 2 December 1922, 19 April 1923, the 1965 partition agreement taking effect 25 July 1966, and 2 August 1990. Ledger 8 (the 1966 gain) was confidence 3, but the Neutral Zone page does not say which part went to Kuwait. It is now confidence 2 and the note says why. Area: 17,395 km2 against an infobox 17,818 km2 (0.98).

Advisory: the 1923 gain from kingdom-of-iraq takes the 1961 shape minus the 80 km circle. That includes the south-west settled by Uqair with Nejd, and kingdom-of-iraq has no mirror event.

Cross-dossier:
- ottoman-empire draws Kuwait as its own land 1873-1900 (a gain from emirate-of-nejd, then a loss to kuwait in 1900). This should be a vassal_start.
- kingdom-of-saudi-arabia and kuwait each record a gain from the other for the 1966 partition.
- iraqi-republic names state-of-kuwait for the 1990-1991 occupation.
- Duplicate: state-of-kuwait.json (me-10-k) should be retired, as the author says.

Thin: the extent before 1913.

## house-of-khalifa (fix applied)

Confirmed: 28 July 1783, the 1797 move (the Bahrain page says 1799), the Omani invasions of 1800 and 1802, Al Bidda in 1843, and the May-July 1851 attack and peace. The rulers table matches the House of Khalifa page, and that page is now cited on all 12 rulers.

The 1799 loss of Zubarah rests on the family's move and on Cliopatria; no page says Zubarah was given up, so confidence 2 is generous. qatar-dynasty founds in 1820 on land "from house-of-khalifa" (confidence 1), against "nobody" here.

Thin:
- The 1868 end of the Al Bidda tie (confidence 1).
- The 1847-1851 and 1867-1868 contests that qatar-dynasty records with this state.
- Wahhabi suzerainty 1802-1811, which emirate-of-diriyah records at confidence 1.
- sultanate-of-oman has no mirror for 1800-1802.

Area: 881.5 km2 against 786.8 km2 (1.12).
