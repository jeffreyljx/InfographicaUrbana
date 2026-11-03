# Review of batch me-10-x (additions: Ottomans and the modern Middle East)

Reviewer: adversarial review, 2026-10-25. Brief: history/briefs/reviewer-brief.md with the orchestrator adjustments (reviewer may apply small verified fixes; spot-check budget 4 per dossier; thin judged against the 2-5 page budget of the additions batch).

Mechanical: `validate_dossier.py --resolve` on all 13 files: no errors, no warnings, every region resolves. After the reviewer edits the six edited files re-validate clean.

## Verdicts

| slug | verdict |
| --- | --- |
| british-mandate-for-palestine | fix |
| mamluk-iraq | fix |
| islamic-state | fail |
| kurdistan-region | fix |
| autonomous-administration-of-north-and-east-syria | fail |
| mamluk-beys-of-egypt | fix |
| sheikhdom-of-acre | fix |
| emirate-of-mount-lebanon | fix |
| houthis | pass |
| southern-transitional-council | pass |
| palestinian-national-authority | thin |
| sharifate-of-mecca | thin |
| emirate-of-bani-khalid | pass |

Blocking findings are marked [blocking]; [non-blocking] findings are for the author or for routing to another group; "applied" findings were made by the reviewer in the dossier.

## british-mandate-for-palestine: fix

- `/ledger/3/counterpart` The 1948 West Bank loss named kingdom-of-jordan, but the neighbours route that land through the palestinians polity. Why: palestinians ledger/0 (1948-05 found, cp british-mandate-for-palestine, the West Bank) and kingdom-of-jordan ledger/4 (1948-05 occupation_start of the West Bank, cp palestinians); the Mandatory Palestine page: "Transjordan seizing and subsequently annexing the West Bank". Fix: Counterpart set to palestinians (reviewer applied; validator passes). (applied)
- `/ledger/4` [non-blocking] The Gaza loss to kingdom-of-egypt has no mirror in kingdom-of-egypt. Why: kingdom-of-egypt has only contest_start (ledger/2, 1948-05) and vassal_start all-palestine-government (ledger/3, 1948-09). Fix: Route to kingdom-of-egypt's group: add occupation_start 1948-05 of the Gaza Strip, cp british-mandate-for-palestine. Nothing to change here.
- `/ledger/1` [non-blocking] Mirror in french-mandate-for-syria-and-lebanon names a string. Why: french-mandate-for-syria-and-lebanon ledger/7 (1923-03 loss, Sea of Galilee) has counterpart 'Mandatory Palestine'. Fix: Route: change that counterpart to british-mandate-for-palestine (author flagged it).

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Mandatory_Palestine: confirmed: "In July 1920, a British civilian administration headed by a High Commissioner replaced the military administration."
- `/ledger/1` https://en.wikipedia.org/wiki/Paulet%E2%80%93Newcombe_Agreement: confirmed: "approved with some caveats by the French and British governments on 7 March 1923"; boundary moved "to include the entire Sea of Galilee and the Yarmuk valley"; 20 villages incorporated
- `/ledger/2` https://en.wikipedia.org/wiki/Mandatory_Palestine: confirmed: Israel would "encompass about 78% of the territory of the former British Mandate"
- `/ledger/5` https://en.wikipedia.org/wiki/Mandatory_Palestine: confirmed: "At midnight on 14/15 May 1948, the Mandate for Palestine expired"

Area: infobox 25585 (None), shape 24300, ratio 0.95, acknowledged True. No Cliopatria row; compared with the dossier shape (about 24,300 km2 by cells, author's figure). Body also gives 26,625.6 km2 for 1931.

## mamluk-iraq: fix

- `/ledger/2, /ledger/3` [non-blocking] Basra 1776-1779 is a loss and a regain here, an occupation in the zand-dynasty dossier, and that dossier names ottoman-empire as the counterpart. Why: Siege of Basra (1775-1776) page: garrison "surrendered on 20 April 1776"; "It remained occupied until 1779 when the Zands withdrew"; zand-dynasty ledger/8 occupation_start 1776-04 and ledger/10 occupation_end 1779, both cp ottoman-empire. Fix: Make ledger/2 occupation_start and ledger/3 occupation_end (cp zand-dynasty), keep keyframe 1776 as is; route to zand-dynasty's group to name mamluk-iraq.
- `/ledger/5, /ledger/6` [non-blocking] Sulaymaniyah 1818-1823 is a contest here; the page calls it an occupation, and qajar-dynasty has no event. Why: Mamluk dynasty (Iraq) page: "the Iranian invasion of Iraq and the occupation of Sulaymaniyah in 1818". Fix: Consider occupation_start/occupation_end with cp qajar-dynasty; route the mirror to qajar-dynasty's group.
- `/ledger/1, /ledger/4, /ledger/9` [non-blocking] No mirror in ottoman-empire for the autonomous pashalik (1704 found, 1705 Basra, 1780 Shahrizor, 1831 end). Why: ottoman-empire ledger has no event naming mamluk-iraq. Fix: Route to ottoman-empire's owner: vassal_start (autonomous) 1704/1750 and vassal_end 1831, as the author suggested.

Thin (for a gap-filler):
- `/keyframe_review/0` Baban emirate (Sulaymaniyah) and the Jalili dynasty of Mosul as counterparts (listed by the author) (try https://en.wikipedia.org/wiki/Baban)

Spot checks:
- `/ledger/2` https://en.wikipedia.org/wiki/Siege_of_Basra_(1775%E2%80%931776): confirmed: "surrendered on 20 April 1776"
- `/ledger/3` https://en.wikipedia.org/wiki/Siege_of_Basra_(1775%E2%80%931776): confirmed: "It remained occupied until 1779 when the Zands withdrew"
- `/ledger/4` https://en.wikipedia.org/wiki/Mamluk_dynasty_(Iraq): confirmed: Sulayman "acquired the governorship of Baghdad, Basrah, and Shahrizor in 1780"
- `/ledger/9` https://en.wikipedia.org/wiki/Mamluk_dynasty_(Iraq): confirmed: "The arrival of the Sultan's new governor in Baghdad in 1831 signaled the beginning of a direct Ottoman rule in Iraq"
- `/ledger/5` https://en.wikipedia.org/wiki/Mamluk_dynasty_(Iraq): confirmed: "the occupation of Sulaymaniyah in 1818"

Area: infobox None (None), shape 385000, ratio None, acknowledged True. No infobox area on the Mamluk dynasty (Iraq) page; no Cliopatria row; the shape (about 385,000 km2 by cells) includes the desert west of the Euphrates, noted as a soft edge.

## islamic-state: fail

- `/ledger/3/confidence` Confidence 3 for the whole Anbar governorate; the page says at least 70%. Why: War in Iraq (2013-2017): "seized at least 70% of Al Anbar Governorate by June 2014", "Fallujah, Al Qaim and half of Ramadi". Fix: Lowered to 2 (reviewer applied). (applied)
- `/ledger/4/confidence` Confidence 3 for the whole of Ninawa and Salah ad-Din; the page says Samarra, Balad, Dujail and Tuz Khurmatu were not taken, and Sinjar (Ninawa) was Kurdish until August. Why: Northern Iraq offensive (June 2014): ISIL "captured ten towns in Saladin Governorate, but not Tuz Khurmatu, Dujail, Balad, Samarra". Fix: Lowered to 2 (reviewer applied). Also subtract Samarra/Balad and the Sinjar disc from K1 so that ledger/6 (Sinjar, 2014-08) is a real gain. (applied)
- `/ledger (missing events)` [blocking] Six autonomous-administration-of-north-and-east-syria gains from islamic-state have no mirror here: Kobani 2014-09 (gain here) and 2015-01, Tell Abyad and Ayn Issa 2015-06, Tishrin Dam 2015-12, Shaddadi 2016-02, Raqqa governorate 2017. Why: AANES ledger/2-6 and /11, each sourced (Siege of Kobani, Tell Abyad offensive (2015): town captured 16 June 2015, Manbij offensive (2016): "In late December 2015, the SDF captured the Tishrin Dam", SDF page). Fix: Add the gain/losses with cp autonomous-administration-of-north-and-east-syria and the same regions and months.
- `/keyframe_review/2, /keyframe_review/3` [blocking] The 2015 and 2016-2017 shapes overlap land the same author gives to AANES in the same years. Why: K2 (2015) holds the whole Raqqa governorate (AANES holds Tell Abyad 45 km and Ayn Issa 25 km from June 2015), an "Al Hasakah 60 km" disc (AANES draws the whole Hasakah governorate from 2014; Hasakah city was YPG/government) and a Manbij 60 km disc that reaches Kobani (about 53 km away, AANES from 2015-01); K3 (2016-2017) holds all of Raqqa governorate including Tell Abyad and Ayn Issa. Fix: Subtract the AANES-held regions (AANES K2-K4) from K2/K3; replace the Al Hasakah disc with the southern pockets (Shaddadi, 40.73 E 36.06 N, al-Hawl) until 2016-02.
- `/ledger/12` [blocking] The 2016 loss (c1) gives Manbij to syria; AANES took Manbij from IS on 12 August 2016. Why: Manbij offensive (2016): "the SDF declared the city fully captured" after ISIL left on 12 August; AANES ledger/8. Fix: Split: Manbij 2016-08 loss to AANES (c3); keep Palmyra (and al-Bab) to syria at c1; drop the Al Hasakah disc (see above).
- `/ledger/19` [blocking] The 2017-11 loss gives the whole Deir ez-Zor governorate to syria; AANES ledger/13 takes the east bank from IS in the same month. Why: Deir ez-Zor campaign (2017-2019) (AANES ledger/13 note): SDF ground operation from 8 September 2017 "north and east of the Euphrates", reaching the Iraqi border on 25 November. Fix: Limit ledger/19 to the west bank (Deir ez-Zor governorate minus the AANES east-bank polygon) and add a loss of the east-bank polygon to AANES, except the Hajin pocket kept to 2018-12.
- `/keyframe_review/4` [non-blocking] The 2018 shape (Abu Kamal 70 km) includes Abu Kamal city and the west bank, which ledger/19 gives to syria in November 2017. Why: K4 note: only the Euphrates (Hajin) pocket is meant; War in Iraq page: "Iraq captured ISIL's last two strongholds of Al-Qa'im and Rawah on 17 November". Fix: Intersect K4 (and ledger/21, AANES ledger/18) with the east-bank polygon; mention the Badiya pockets in the note.
- `/ledger/8` [non-blocking] The May 2015 Ramadi gain changes nothing: K1 already holds all of Anbar, and republic-of-iraq records no 2015 loss. Why: War in Iraq: "half of Ramadi" held in June 2014; Ramadi captured late May 2015. Fix: Subtract the government-held half of Ramadi from K1 (or note that the event completes a city already half held).

Thin (for a gap-filler):
- `/ledger/2` date of the 2014 capture of Deir ez-Zor governorate (c1, bridging; the Islamic State page does not mention it) (try https://en.wikipedia.org/wiki/Deir_ez-Zor_offensive_(April%E2%80%93July_2014))
- `/ledger/12` dates of the 2016 losses of Palmyra, al-Bab and Jarabulus (c1, bridging) (try https://en.wikipedia.org/wiki/Palmyra_offensive_(March_2016))

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Islamic_State: confirmed: "In April 2013, having expanded into Syria"; "Raqqa in Syria was under IS control from 2013"
- `/ledger/3` https://en.wikipedia.org/wiki/War_in_Iraq_(2013%E2%80%932017): confirmed date; region overstated ("at least 70%"): confidence lowered to 2
- `/ledger/4` https://en.wikipedia.org/wiki/Northern_Iraq_offensive_(June_2014): confirmed dates (Mosul 10 June, Tikrit 11 June); region overstated: confidence lowered to 2
- `/ledger/6` https://en.wikipedia.org/wiki/Northern_Iraq_offensive_(June_2014): confirmed: early August 2014 offensive "within days captured the town of Sinjar"
- `/ledger/10` https://en.wikipedia.org/wiki/War_in_Iraq_(2013%E2%80%932017): confirmed: "ISIL forces lost Sinjar on November 13 to Kurdish forces" (2015)
- `/ledger/22` https://en.wikipedia.org/wiki/Battle_of_Baghuz_Fawqani: confirmed: final victory declared 23 March 2019; "the territorial end of IS's self-declared caliphate"

Area: infobox 56000 (2014), shape 242000, ratio 4.3, acknowledged True. No infobox area on the Islamic State page; 56,000 km2 is the War in Iraq page's Iraqi peak (populated area); the 2014 shape is about 242,000 km2 by cells including Raqqa and Deir ez-Zor; the K1 note acknowledges both page figures (56,000 vs 40% of Iraq, about 175,000).

## kurdistan-region: fix

- `/identity/end/year` The Region is alive today but the dossier ended in 2024. Why: Schema: end is "for a state alive today, the current year"; the Kurdistan Region page describes a current entity; the other modern dossiers of this batch end in 2026. Fix: Set to 2026, with keyframe_review/2/to, capitals/0/to and certainty/0/to (reviewer applied; validator passes). Note that republic-of-iraq ends 2024. (applied)
- `/ledger/1` [non-blocking] iraqi-republic regains the three governorates in 2005-10; this dossier keeps them (rename). Why: iraqi-republic ledger/14 (2005-10 gain, cp kurdistan-region); the author flagged it as republic-of-iraq. Fix: Route to iraqi-republic's group: replace that gain with vassal_start (federal region, 15 October 2005) or drop it.
- `/ledger/3` [non-blocking] republic-of-iraq records only Kirkuk lost to the Region in 2014; this event also takes Khanaqin/Jalawla, Bashiqa, Makhmur and Sinjar. Why: Kurdistan Region page: Peshmerga "took control of most disputed areas, including Kirkuk, Khanaqin, Jalawla, Bashiqa, Sinjar and Makhmur". Fix: Route: add these places to republic-of-iraq ledger/3 (or a second loss).

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Kurdistan_Region: confirmed: infobox "Autonomy founded: 19 May 1992"
- `/ledger/1` https://en.wikipedia.org/wiki/Kurdistan_Region: confirmed: infobox "Federal region established: 15 October 2005"
- `/ledger/2` https://en.wikipedia.org/wiki/Northern_Iraq_offensive_(June_2014): confirmed: Peshmerga took Kirkuk on 13 June "after government forces abandoned their posts"
- `/ledger/3` https://en.wikipedia.org/wiki/Kurdistan_Region: confirmed: disputed areas incl. Kirkuk, Khanaqin, Jalawla, Bashiqa, Sinjar and Makhmur (2014)

Area: infobox 46862 (None), shape 36900, ratio 1.27, acknowledged True. No Cliopatria row; shape of the three governorates about 36,900 km2 by cells (author); acknowledged in the keyframe note.

## autonomous-administration-of-north-and-east-syria: fail

- `/keyframe_review/1` [blocking] The 2014 shape adds the whole Hasakah governorate (about 23,000 km2) with no gain event; K0 is four discs. Why: Only ledger/1 (2014-01 rename, no region) lies between K0 and K1; the K1 note itself says "ISIL and the government held parts"; syria ledger/11 loses the whole governorate to this state in 2012, so the found event and K0 disagree with the neighbour. Fix: Either add a gain of the Jazira (2012-2014, c1/c2) or keep the discs, and in every case subtract the IS-held south (Shaddadi 45 km disc, al-Hawl) until 2016-02 and Hasakah city until 2016-08, so that ledger/6 and ledger/9 are real gains.
- `/keyframe_review/8` [blocking] The 2026 shape drops Kobani (30 km disc) and the Tishrin Dam disc with no event; ledger/25 loses only Raqqa and Deir ez-Zor. Why: AANES page (2026): "the governorates of Raqqa and Deir ez-Zor immediately handed over"; "leaving the DAANES as a rump state in Al-Hasakah Governorate"; Kobani is not named. Fix: Add Kobani and the Tishrin disc to ledger/25 (c2, the page's "rump state in Al-Hasakah") or a separate 2026-01 loss, or keep them in K8.
- `/ledger/18, /ledger/19` [non-blocking] The Hajin and Baghuz gains are Abu Kamal discs (70 km, 25 km) that take in the west bank and Abu Kamal city, held by the Syrian government since November 2017; the keyframes draw only the east-bank polygon. Why: islamic-state ledger/19 (2017-11, Abu Kamal to syria); AANES K4-K7 corrections hold the Deir ez-Zor east-bank polygon, not the discs. Fix: Intersect both regions with the east-bank polygon (the Hajin pocket).
- `/ledger/2 - /ledger/6, /ledger/8, /ledger/13` [non-blocking] The IS-side mirrors of these gains are missing or name syria (see islamic-state). Why: islamic-state has no Kobani, Tell Abyad, Tishrin or Shaddadi event; its ledger/12 and ledger/19 give Manbij and Deir ez-Zor to syria. Fix: Fix on the islamic-state side; nothing to change here once it is done.
- `/ledger/15, /ledger/21` [non-blocking] Turkey's mirrors name syria (de jure owner). Why: republic-of-turkey ledger/8 (2018-01) and ledger/9 (2019-10) occupation_start, cp syria. Fix: Accept as an exception (the map agrees); no change.

Thin (for a gap-filler):
- `/keyframe_review/6` dates of the October 2019 Syrian Army deployments to Manbij and Kobani (the K6 note says undated) (try https://en.wikipedia.org/wiki/2019_Turkish_offensive_into_north-eastern_Syria)
- `/capitals/0` year of the move of the seat from Qamishli to Ayn Issa (try https://en.wikipedia.org/wiki/Ayn_Issa)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Autonomous_Administration_of_North_and_East_Syria: confirmed: "In July 2012, the YPG established control in the towns of Kobanî, Amuda and Afrin"
- `/ledger/4` https://en.wikipedia.org/wiki/Tell_Abyad_offensive_(2015): confirmed: border crossing 15 June, town 16 June 2015; Ayn Issa 23 June
- `/ledger/5` https://en.wikipedia.org/wiki/Manbij_offensive_(2016): confirmed: "In late December 2015, the SDF captured the Tishrin Dam"
- `/ledger/8` https://en.wikipedia.org/wiki/Manbij_offensive_(2016): confirmed: city declared captured after 12 August 2016
- `/ledger/24` https://en.wikipedia.org/wiki/Autonomous_Administration_of_North_and_East_Syria: confirmed: "On 9 December, SNA fighters captured the city of Manbij"
- `/ledger/25` https://en.wikipedia.org/wiki/Autonomous_Administration_of_North_and_East_Syria: confirmed: offensive 13 January 2026, ceasefire 18 January, Raqqa and Deir ez-Zor handed over, "rump state in Al-Hasakah Governorate"

Area: infobox None (None), shape 57000, ratio 1.24, acknowledged True. Infobox has no area figure; the SDF page's "about 25% of Syria" (2022, about 46,000 km2) against the 2019 shape of about 57,000 km2 by cells, acknowledged in the K6 note.

## mamluk-beys-of-egypt: fix

- `/ledger/5/month` The 1775 campaign starts in April, not May. Why: Daher al-Umar page: Gaza "surrendered on 1 April 1775"; Jaffa besieged from 3 April, taken 20 May; Acre 30 May; Abu al-Dhahab died 10 June 1775. Fix: Month set to 4 (reviewer applied; same in sheikhdom-of-acre ledger/13). (applied)
- `/ledger/5, /ledger/6` [non-blocking] sheikhdom-of-acre records losses of Gaza, Ramla, Jaffa and Acre to this state (1775-05) and a regain of Acre (1775-06); this dossier records only a contest. Why: sheikhdom-of-acre ledger/14-16. Fix: Align the two: either occupation_start (1775-04/05) and occupation_end (1775-06) here with the Acre side kept, or contest on both sides. Say who holds Gaza, Ramla and Jaffa after June 1775 (the Acre ledger leaves them to this state).
- `/ledger/7/note` [non-blocking] The quoted sentence is not on the Ottoman Egypt page. Why: The page says: "the joint rule was maintained until 1786, when an expedition was sent by the Porte to restore Ottoman supremacy in Egypt"; the year and fact are confirmed. Fix: Replace the quote with the page's wording.
- `/ledger/1, /ledger/4` [non-blocking] The Hejaz 1770-1772 is drawn here and by sharifate-of-mecca, with no relation between the two. Why: sharifate-of-mecca K1 (1201-1802) covers the Hejaz and has no 1770-1772 event; ottoman-empire has no mirror either. Fix: Route: record the sharifate as this state's vassal 1770-1772 (vassal_start in both) or note the overlap.

Thin (for a gap-filler):
- `/ledger/4` date and manner of the 1772 loss of the Hejaz (c1, bridging) (try https://en.wikipedia.org/wiki/Muhammad_Bey_Abu_al-Dhahab)
- `/identity/end` the 1798-1811 phase (Murad Bey in Upper Egypt, return 1801-1805, 1811 massacre): flagged by the author (try https://en.wikipedia.org/wiki/Muhammad_Ali_of_Egypt)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Ottoman_Egypt: confirmed: (1769) "Egypt was declared independent, and the pasha given 48 hours to quit the country"
- `/ledger/1` https://en.wikipedia.org/wiki/Ali_Bey_al-Kabir: confirmed: "In 1770 he gained control of the Hejaz"
- `/ledger/7` https://en.wikipedia.org/wiki/Ottoman_Egypt: confirmed year (1786 expedition); quoted wording not on page
- `/ledger/8` https://en.wikipedia.org/wiki/Murad_Bey: confirmed: "in 1791, only five years after their expulsion by Hasan Pasha, the duumvirate returned to Cairo"

Area: infobox None (None), shape 1000000, ratio None, acknowledged True. Ottoman Egypt infobox gives population only; the Egypt shape (about 1.0 million km2 by cells) counts the deserts and Sinai, acknowledged in the keyframe note.

## sheikhdom-of-acre: fix

- `/ledger/13/month` The 1775 contest starts in April. Why: Daher al-Umar page: Gaza "surrendered on 1 April 1775". Fix: Month set to 4 (reviewer applied). (applied)
- `/keyframe_review/6` [non-blocking] Sidon (held from 1771, ledger/8) leaves the 1775 shape with no loss event. Why: Daher al-Umar page: after Abu al-Dhahab's death (10 June 1775) "the Ottomans took Sidon". Fix: Add a 1775 loss of Saida 25 km to ottoman-empire, confidence 2.
- `/ledger/14 - /ledger/16` [non-blocking] Losses to mamluk-beys-of-egypt with no gain on the other side (see mamluk-beys-of-egypt). Why: mamluk-beys-of-egypt ledger/5-6 record only a contest. Fix: Align with the beys dossier; add the return of Gaza, Ramla and Jaffa to ottoman-empire after June 1775 if that is the reading.
- `/ledger (all ottoman-empire events)` [non-blocking] No mirror in ottoman-empire for any gain or loss. Why: ottoman-empire ledger has no event naming sheikhdom-of-acre; the author notes the multazim status is open. Fix: Route to ottoman-empire's owner (vassal_start 1730/1768 to 1776, or occupation).

Thin (for a gap-filler):
- `/ledger/10` date of the 1772 loss of Jaffa (c1, bridging) (try https://en.wikipedia.org/wiki/Jaffa)
- `/ledger/12` end of the Metawali alliance (c1) (try https://en.wikipedia.org/wiki/Nasif_al-Nassar)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Daher_al-Umar: confirmed: "In 1730, Daher took over Tiberias"
- `/ledger/3` https://en.wikipedia.org/wiki/Daher_al-Umar: confirmed: "took Acre by force, probably in 1744"; multazim July 1746
- `/ledger/5` https://en.wikipedia.org/wiki/Daher_al-Umar: confirmed: 1757, "Haifa, Tira, and Tantura, and the adjoining Mount Carmel"
- `/ledger/8` https://en.wikipedia.org/wiki/Daher_al-Umar: confirmed: Sidon captured 11 June 1771 (withdrew 20 June, reoccupied 23 October 1771)
- `/ledger/9` https://en.wikipedia.org/wiki/Daher_al-Umar: confirmed: "captured Jaffa in August 1771"
- `/ledger/11` https://en.wikipedia.org/wiki/Daher_al-Umar: confirmed: "recaptured Jaffa on 16 February 1773"
- `/ledger/21` https://en.wikipedia.org/wiki/Daher_al-Umar: confirmed: Deir Hanna "fell on 22 July 1776"

Area: infobox None (None), shape None, ratio None, acknowledged True. No article for the polity; Daher al-Umar page gives no area.

## emirate-of-mount-lebanon: fix

- `/ledger/1/confidence` Confidence 3 for a region (all of Mount Lebanon governorate and Nabatiyah) the page does not name for 1589. Why: Fakhr al-Din II page: "the iltizam of the Sidon and Beirut nahiyas and the port of Beirut from 14 July 1589"; Chouf, Matn, Jurd and Jabal Amil only in 1591-1594; Keserwan in 1606. Fix: Lowered to 2 (reviewer applied). (applied)
- `/keyframe_review/1, /keyframe_review/2` [non-blocking] K1 and K2 use the whole Mount Lebanon governorate, which includes the Keserwan, so the 1606 Keserwan gain (ledger/3) changes nothing. Why: Fakhr al-Din II page: "In the course of the fighting, Fakhr al-Din took over the Keserwan" (1606). Fix: Draw K1/K2 as the Chouf, Matn and Jurd (Mount Lebanon minus Keserwan and Jbeil) and let ledger/3 add the Keserwan.
- `/ledger/5/month` Month missing. Why: Fakhr al-Din II page: "In September 1626, he captured the fortress of Salamiyah". Fix: Month 9 added (reviewer applied). (applied)
- `/keyframe_review/3` [non-blocking] Ajlun (30 km disc) is in K3 and lost in ledger/7 but never gained. Why: K3 note: "held Ajlun". Fix: Add a gain of Ajlun (c2, Fakhr al-Din II page) in the 1620s.
- `/ledger/11/confidence, /ledger/12/confidence` Confidence 3 for the whole North Lebanon governorate; the page names Jabal Amil, Koura, Sidon and Beirut. Why: Bashir Shihab II page: "In 1832, Muhammad Ali rewarded Bashir by extending the latter's jurisdiction to include Jabal Amil", Koura, Sidon and Beirut. Fix: Lowered to 2 (reviewer applied); better, replace North Lebanon with Koura. (applied)
- `/ledger/11, /ledger/12` [non-blocking] No mirror in muhammad-ali-dynasty or ottoman-empire. Why: muhammad-ali-dynasty ledger/11 (1832-05) and ledger/20 (1840-11) do not name this state. Fix: Route: vassal_start of this emirate by muhammad-ali-dynasty 1832-1840 would carry the grant.

Thin (for a gap-filler):
- `/ledger/6` Latakia: the page dates the Jableh/Latakia tax farms 1628-1629 and the Tripoli appointment 1627 "according solely to Duwayhi" (try https://en.wikipedia.org/wiki/Fakhr_al-Din_II)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Fakhr_al-Din_II: confirmed date (14 July 1589); region overstated, confidence lowered
- `/ledger/2` https://en.wikipedia.org/wiki/Fakhr_al-Din_II: confirmed: "In July 1602" sanjak-bey of Safed; iltizam of Acre, Tiberias and Safed shortly before
- `/ledger/3` https://en.wikipedia.org/wiki/Fakhr_al-Din_II: confirmed: 1606 with Ali Janbulad against Yusuf; took over the Keserwan
- `/ledger/4` https://en.wikipedia.org/wiki/Fakhr_al-Din_II: confirmed: Battle of Anjar 1623, control extended to the Beqaa
- `/ledger/5` https://en.wikipedia.org/wiki/Fakhr_al-Din_II: confirmed: September 1626 Salamiyah, then Hama and Homs (month added)
- `/ledger/10` https://en.wikipedia.org/wiki/Bashir_Shihab_II: confirmed: Beqaa conquered under his son Khalil (1821)
- `/ledger/11` https://en.wikipedia.org/wiki/Bashir_Shihab_II: confirmed year 1832; region wider than the page

Area: infobox None (None), shape None, ratio None, acknowledged True. Page silent on area (author notes).

## houthis: pass

- `/ledger (all gains)` [non-blocking] republic-of-yemen mirrors only the 2014-09 contest; the other gains have none, and the 2026 gains fall after republic-of-yemen's 2024 end. Why: republic-of-yemen ledger/3 is its only event with this state. Fix: Route to republic-of-yemen's group. Nothing to change here.

Thin (for a gap-filler):
- `/ledger/4` Amran 2014 (c1): the insurgency page has no 2014 Amran sentence (try https://en.wikipedia.org/wiki/Battle_of_Amran)
- `/ledger/9` the Houthi withdrawal from Aden and Lahij (c1): the war page does not date it (try https://en.wikipedia.org/wiki/Battle_of_Aden_(2015))
- `/ledger/12` western Marib line of April 2022 (c1) (try https://en.wikipedia.org/wiki/Marib_campaign)
- `/keyframe_review/3` the west coast (Mokha 2017, Hodeidah coast 2018-2021) is not drawn: the shape keeps all of former North Yemen to 2026 (try https://en.wikipedia.org/wiki/Hodeidah_offensive)

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Houthi_insurgency_in_Yemen: confirmed: entered Saada 19 March, city 24 March, own administration 26 March 2011
- `/ledger/2` https://en.wikipedia.org/wiki/Houthi_insurgency_in_Yemen: confirmed: "On November 9 ... break through defense lines", Kuhlan Ash Sharaf, toward Midi
- `/ledger/3` https://en.wikipedia.org/wiki/Houthi_insurgency_in_Yemen: confirmed: September-October 2012, "expanding their control in Sanaa Governorate and other areas around the capital"
- `/ledger/13` https://en.wikipedia.org/wiki/Yemeni_civil_war_(2014%E2%80%93present): confirmed: 10 September 2026 entry, "The Houthis recaptured Mokha"
- `/ledger/14` https://en.wikipedia.org/wiki/Yemeni_civil_war_(2014%E2%80%93present): confirmed: Perim Island 11 September 2026; Hanish Islands in the same paragraph
- `/ledger/8` https://en.wikipedia.org/wiki/Yemeni_civil_war_(2014%E2%80%93present): confirmed: "By 25 March, Lahij fell to the Houthis"

Area: infobox None (None), shape None, ratio None, acknowledged True. Rebel polity, no infobox area; the war page's "all of former North Yemen except for eastern Marib" is the shape.

## southern-transitional-council: pass

- `/ledger (all gains and losses)` [non-blocking] republic-of-yemen mirrors only the 2018-02 Aden contest; the 2026 events fall after its 2024 end. Why: republic-of-yemen ledger/5. Fix: Route to republic-of-yemen's group. Nothing to change here.

Spot checks:
- `/ledger/1` https://en.wikipedia.org/wiki/Southern_Transitional_Council: confirmed: "Beginning on 28 January 2018, forces loyal to the STC seized control"
- `/ledger/4` https://en.wikipedia.org/wiki/Southern_Transitional_Council: confirmed: Riyadh Agreement 5 November 2019 "in exchange for the STC withdrawing militarily from Aden"
- `/ledger/6` https://en.wikipedia.org/wiki/Southern_Transitional_Council: confirmed: self-governance 26 April 2020
- `/ledger/8` https://en.wikipedia.org/wiki/Southern_Transitional_Council: confirmed: offensive from 2 December 2025, most of six governorates by 8 December
- `/ledger/9` https://en.wikipedia.org/wiki/Southern_Transitional_Council: confirmed: Hadramawt and Al-Mahrah retaken 2-4 January 2026
- `/ledger/10` https://en.wikipedia.org/wiki/Southern_Transitional_Council: confirmed: Abyan and Shabwah 6-7 January 2026

Area: infobox None (None), shape None, ratio None, acknowledged True. No infobox area.

## palestinian-national-authority: thin

- `/ledger/4` [non-blocking] state-of-israel's 2005 Gaza occupation_end names the 1948-1950 palestinians polity. Why: state-of-israel ledger/39 (2005-09, cp palestinians). Fix: Route: that counterpart should be palestinian-national-authority; also add Israel-side events for 1994 and 1995.

Thin (for a gap-filler):
- `/keyframe_review/0, /keyframe_review/1` Gaza 1994-2005: the page says the PA governed 60% of the strip until 2005 ("from 60 percent to 100 percent"), but the shape is the whole strip, so ledger/4 changes nothing (try https://en.wikipedia.org/wiki/Israeli_settlement)
- `/ledger/1` Areas A and B: towns and redeployment dates (Nov-Dec 1995, Hebron 1997, Wye 1998); eight 9 km discs stand in (try https://en.wikipedia.org/wiki/Area_C_(West_Bank))
- `/ledger` Hebron Protocol (1997) and Wye River Memorandum (1998) not opened (try https://en.wikipedia.org/wiki/Hebron_Protocol)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Palestinian_National_Authority: confirmed: "formed on 4 May 1994, pursuant to the Gaza–Jericho Agreement"
- `/ledger/4` https://en.wikipedia.org/wiki/Palestinian_National_Authority: confirmed: 2005, Gaza share "from 60 percent to 100 percent"
- `/ledger/5` https://en.wikipedia.org/wiki/Palestinian_National_Authority: confirmed: Gaza "taken over by Hamas on 14 June 2007"
- `/ledger/6` https://en.wikipedia.org/wiki/Palestinian_National_Authority: confirmed: 5 January 2013 order to use "State of Palestine"

Area: infobox None (None), shape 2365, ratio None, acknowledged True. No infobox area; Area A 18% and B 22% of the West Bank on the page against about 2,000 km2 of discs plus Gaza (365 km2), acknowledged.

## sharifate-of-mecca: thin

- `/keyframe_review/1` [non-blocking] The 1201 shape jumps from Mecca (40 km) to the Hejaz polygon (about 170,000 km2) with only a rename (no region) in the ledger. Why: Sharifate of Mecca page: "By circa 1200, a sharif by the name of Qatadah ibn Idris seized power"; "the descendants of ... Qatada ruled over Mecca, Medina and the Tihamah"; the extent (Al-'Ula, Al Lith, Khaybar) is for the 19th century. Fix: Add a gain (confidence 1) carrying the Hejaz polygon, or keep Mecca alone until a dated extension.
- `/ledger (vassal events)` [non-blocking] No vassal events, though five dossiers name this state as their vassal or victim. Why: ikhshidid-dynasty ledger/6 and /14 (944-969), sulayhid-dynasty ledger/5 and /7 (1064-1067), ayyubid-sultanate ledger/1 and /17 (1174-1238), rasulid-dynasty ledger/1 (1238 gain of Mecca); the page names Ayyubid, Mamluk (from 1350) and Ottoman (1517) suzerainty. Fix: Add vassal_start/vassal_end pairs (cp ikhshidid-dynasty 967-969, sulayhid-dynasty 1064-1067, ayyubid-sultanate 1174-1238, mamluk-sultanate, ottoman-empire 1517-1916) and a 1238 event for the Rasulids; this also settles the Hejaz overlap the author flagged.
- `/ledger/2, /ledger/3` [non-blocking] emirate-of-diriyah names other counterparts. Why: emirate-of-diriyah ledger/12 (1803 gain of Mecca, cp ottoman-empire) and ledger/21 (1813-01 loss of Mecca, cp muhammad-ali-dynasty). Fix: Route: diriyah should name sharifate-of-mecca in 1803; the 1813 regain may name muhammad-ali-dynasty here.

Thin (for a gap-filler):
- `/keyframe_review/1` any dated extension of the sharifs' rule beyond Mecca (Medina, Yanbu, Taif) between 1200 and 1800 (try https://en.wikipedia.org/wiki/Qatadah_ibn_Idris)
- `/ledger` the Emirate of Medina (Husaynid sharifs) as a separate counterpart (author listed) (try https://en.wikipedia.org/wiki/Medina)

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Sharifate_of_Mecca: confirmed: infobox "967-980: Ja'far ibn Muhammad"; Kafur installed a sharif "in about 964"
- `/ledger/1` https://en.wikipedia.org/wiki/Sharifate_of_Mecca: confirmed: "By circa 1200 ... Qatadah ibn Idris seized power"
- `/ledger/2` https://en.wikipedia.org/wiki/Sharifate_of_Mecca: confirmed: "In 1803 the Wahhabis ... attacked Mecca" (page also says 1801)
- `/ledger/3` https://en.wikipedia.org/wiki/Sharifate_of_Mecca: confirmed: Tusun "occupied Medina in 1812 and Mecca in 1813"
- `/ledger/4` https://en.wikipedia.org/wiki/Sharifate_of_Mecca: confirmed: "from about 967 to 1916, when it became the Kingdom of Hejaz"

Area: infobox None (None), shape 170000, ratio None, acknowledged True. No area on the page; the Hejaz polygon trimmed to about 170,000 km2, acknowledged in the K1 note.

## emirate-of-bani-khalid: pass

- `/ledger/3, /ledger/4, /ledger/5` [non-blocking] The mirrors in emirate-of-diriyah and emirate-of-nejd disagree. Why: emirate-of-diriyah ledger/4-8 name the string 'Bani Khalid Emirate' and date the Hasa gain 1795 (this dossier 1793, the Bani Khalid page: 'deposed the Al 'Ura'yir in 1793'); diriyah has no 1818 loss of Hasa; emirate-of-nejd ledger/2 takes Hasa in 1830 from nobody. Fix: Route: diriyah to name emirate-of-bani-khalid and reconcile 1793/1795; nejd ledger/2 to name emirate-of-bani-khalid. Nothing to change here.

Spot checks:
- `/ledger/0` https://en.wikipedia.org/wiki/Bani_Khalid: confirmed: "expelled Ottoman forces from the cities and towns in 1670"
- `/ledger/3` https://en.wikipedia.org/wiki/Bani_Khalid: confirmed: "deposed the Al 'Ura'yir in 1793"
- `/ledger/4` https://en.wikipedia.org/wiki/Bani_Khalid: confirmed: Ottomans conquered al-Hasa and al-Qatif and reinstated the Al 'Uray'ir (1818)
- `/ledger/5` https://en.wikipedia.org/wiki/Bani_Khalid: confirmed: "another battle with the Subay' and the Al Saud in 1830, ended the rule of the Bani Khalid"

Area: infobox None (None), shape 20700, ratio None, acknowledged True. No area on the page; two discs about 20,700 km2 by cells; the wider claims of the lead are noted and not drawn.

## Cross-dossier matrix (everything not matched)

| event | mirror | status | note |
| --- | --- | --- | --- |
| british-mandate-for-palestine 1923 gain cp french-mandate-for-syria-and-lebanon | french-mandate-for-syria-and-lebanon 1923 loss | mismatch | french-mandate-for-syria-and-lebanon ledger/7 (1923-03 loss of the Sea of Galilee) names the string 'Mandatory Palestine'; change it to british-mandate-for-palestine |
| british-mandate-for-palestine 1948 loss cp kingdom-of-egypt | - | missing | kingdom-of-egypt has contest_start (ledger/2, 1948-05, Beersheba/Gaza vs state-of-israel) and vassal_start all-palestine-government (ledger/3, 1948-09) but no occupation of Gaza from the Mandate; add occupation_start 1948-05 Gaza Strip cp british-mandate-for-palestine |
| mamluk-iraq 1705,1780 gain cp ottoman-empire | - | missing | ottoman-empire (written before this additions batch) has no event naming this state; route to its owner: add vassal_start (autonomous) or the matching loss/gain (the author flagged the c. 1750 recognition of Sulayman Abu Layla) |
| mamluk-iraq 1776 loss cp zand-dynasty | zand-dynasty 1776 occupation_start | mismatch | zand-dynasty ledger/8 records occupation_start of Basra 1776-04 but names ottoman-empire; mamluk-iraq records a loss. Siege of Basra page: "It remained occupied until 1779". Align: occupation_start/occupation_end in both, zand naming mamluk-iraq |
| mamluk-iraq 1779 gain cp zand-dynasty | zand-dynasty 1779 occupation_end | mismatch | zand-dynasty ledger/10 occupation_end 1779 names ottoman-empire; mamluk-iraq records a gain from zand-dynasty |
| islamic-state 2015 gain cp republic-of-iraq | republic-of-iraq 2014 loss | mismatch | republic-of-iraq has no 2015 loss of Ramadi: its 2014 Anbar loss (ledger/2, "Fallujah, Al Qaim and half of Ramadi") and islamic-state K1 already hold Ramadi, so the May 2015 gain is a no-op on both sides |
| islamic-state 2016 loss cp syria | - | mismatch | syria has no 2016 gain from islamic-state; and autonomous-administration-of-north-and-east-syria ledger/8 gains Manbij from islamic-state on 2016-08 (Manbij offensive (2016) page), while this event gives Manbij to syria |
| islamic-state 2017 loss cp syria | autonomous-administration-of-north-and-east-syria 2017 gain | mismatch | syria has no 2017 gain from islamic-state; autonomous-administration-of-north-and-east-syria ledger/13 gains the east-of-Euphrates part of Deir ez-Zor from islamic-state on 2017-11, while this event gives the whole governorate to syria |
| autonomous-administration-of-north-and-east-syria 2014 loss cp islamic-state | - | missing | islamic-state (same batch, same author) has no event for the Kobani gain of 2014-09; add it there with cp autonomous-administration-of-north-and-east-syria |
| autonomous-administration-of-north-and-east-syria 2015 gain cp islamic-state | - | missing | islamic-state (same batch, same author) has no event for the Kobani loss of 2015-01; add it there with cp autonomous-administration-of-north-and-east-syria |
| autonomous-administration-of-north-and-east-syria 2015 gain cp islamic-state | - | missing | islamic-state (same batch, same author) has no event for the Tell Abyad / Ayn Issa loss of 2015-06; add it there with cp autonomous-administration-of-north-and-east-syria |
| autonomous-administration-of-north-and-east-syria 2015 gain cp islamic-state | - | missing | islamic-state (same batch, same author) has no event for the Tishrin Dam loss of 2015-12; add it there with cp autonomous-administration-of-north-and-east-syria |
| autonomous-administration-of-north-and-east-syria 2016 gain cp islamic-state | - | missing | islamic-state (same batch, same author) has no event for the Shaddadi loss of 2016-02; add it there with cp autonomous-administration-of-north-and-east-syria |
| autonomous-administration-of-north-and-east-syria 2016 gain cp islamic-state | islamic-state 2016 loss | mismatch | islamic-state ledger/12 (2016, c1) gives Manbij to syria; this event (Manbij offensive page: SDF declared the city captured on 12 August 2016) gives it to this state |
| autonomous-administration-of-north-and-east-syria 2016 gain cp syria | - | missing | syria has no 2016 event for Hasakah city; its ledger/11 (2012) already loses the whole Hasakah governorate to this state |
| autonomous-administration-of-north-and-east-syria 2017 gain cp islamic-state | islamic-state 2017 loss | mismatch | islamic-state ledger/19 (2017-11) gives the whole Deir ez-Zor governorate to syria; this event takes the east bank from islamic-state |
| autonomous-administration-of-north-and-east-syria 2018 loss cp republic-of-turkey | republic-of-turkey 2018 occupation_start | exception | republic-of-turkey ledger/8 records occupation_start of Afrin 2018-01 with cp syria (the de jure owner); the map agrees (Afrin leaves this state, Turkey occupies it) |
| autonomous-administration-of-north-and-east-syria 2019 loss cp republic-of-turkey | republic-of-turkey 2019 occupation_start | exception | republic-of-turkey ledger/9 records occupation_start of Tell Abyad - Ras al-Ayn 2019-10 with cp syria (the de jure owner); the map agrees |
| autonomous-administration-of-north-and-east-syria 2024 loss cp Syrian National Army | - | exception | counterpart 'Syrian National Army' has no dossier (string counterpart) |
| autonomous-administration-of-north-and-east-syria 2026 loss cp syria | - | exception | syria ends 2024 (Cliopatria horizon; renamed 2024-12); the January 2026 handover has no counterpart dossier alive in 2026 (author flagged the 2024 horizon) |
| mamluk-beys-of-egypt 1770,1772 gain/loss cp ottoman-empire | - | missing | ottoman-empire (written before this additions batch) has no event naming this state; route to its owner: add vassal_start (autonomous) or the matching loss/gain; the Hejaz is also drawn by sharifate-of-mecca (K1) with no 1770-1772 event |
| mamluk-beys-of-egypt 1771,1771,1786,1791 occupation_start/occupation_end/loss/gain cp ottoman-empire | - | missing | ottoman-empire (written before this additions batch) has no event naming this state; route to its owner: add vassal_start (autonomous) or the matching loss/gain |
| mamluk-beys-of-egypt 1798 loss cp french-directory | - | exception | Cliopatria row French Directory (1796-1799); its group has not run yet |
| sheikhdom-of-acre 1738 gain cp Ahmad al-Husayn | - | exception | counterpart 'Ahmad al-Husayn' has no dossier (string counterpart) |
| sheikhdom-of-acre 1740,1744,1757,1771,1771,1771,1772,1773,1775 gain/loss cp ottoman-empire | - | missing | ottoman-empire (written before this additions batch) has no event naming this state; route to its owner: add vassal_start (autonomous) or the matching loss/gain |
| sheikhdom-of-acre 1767,1775 vassal_start/vassal_end cp Metawalis of Jabal Amil | - | exception | counterpart 'Metawalis of Jabal Amil' has no dossier (string counterpart) |
| sheikhdom-of-acre 1775 loss cp mamluk-beys-of-egypt | mamluk-beys-of-egypt 1775 contest_start | mismatch | mamluk-beys-of-egypt ledger/5-6 record only contest_start/contest_end (1775-04 to 1775-06) over Gaza, Jaffa and Acre; this dossier records losses and a regain. Align: occupation or contest on both sides |
| sheikhdom-of-acre 1775 loss cp mamluk-beys-of-egypt | mamluk-beys-of-egypt 1775 contest_start | mismatch | mamluk-beys-of-egypt ledger/5-6 record only contest_start/contest_end (1775-04 to 1775-06) over Gaza, Jaffa and Acre; this dossier records losses and a regain. Align: occupation or contest on both sides |
| sheikhdom-of-acre 1775 gain cp mamluk-beys-of-egypt | mamluk-beys-of-egypt 1775 contest_start | mismatch | mamluk-beys-of-egypt ledger/5-6 record only contest_start/contest_end (1775-04 to 1775-06) over Gaza, Jaffa and Acre; this dossier records losses and a regain. Align: occupation or contest on both sides |
| emirate-of-mount-lebanon 1589,1602,1623,1626,1627,1633,1799,1821 gain/loss cp ottoman-empire | - | missing | ottoman-empire (written before this additions batch) has no event naming this state; route to its owner: add vassal_start (autonomous) or the matching loss/gain |
| emirate-of-mount-lebanon 1606 gain cp Yusuf Sayfa | - | exception | counterpart 'Yusuf Sayfa' has no dossier (string counterpart) |
| emirate-of-mount-lebanon 1832 gain cp muhammad-ali-dynasty | - | missing | muhammad-ali-dynasty ledger/11 (1832-05 occupation_start of Syria from ottoman-empire) has no grant naming this state |
| emirate-of-mount-lebanon 1840 loss cp ottoman-empire | - | missing | ottoman-empire has no event; muhammad-ali-dynasty ledger/20 (1840-11) loses Syria to ottoman-empire without naming this state |
| houthis 2011,2011,2012,2014,2014,2015,2022 gain cp republic-of-yemen | - | missing | republic-of-yemen has only contest_start 2014-09 (ledger/3) with this state; add the matching losses (Saada and Al Jawf 2011, Hajjah 2011-11, round Sanaa 2012, Sanaa 2014-09, the north 2015-02, western Marib 2022-04) |
| houthis 2026,2026 gain cp republic-of-yemen | - | exception | republic-of-yemen ends 2024 (Cliopatria horizon); no counterpart dossier alive in 2026 (author flagged) |
| southern-transitional-council 2018,2019,2020,2020,2022,2025 gain/loss cp republic-of-yemen | - | missing | republic-of-yemen has only contest_start 2018-02 Aden (ledger/5) with this state; no loss/gain mirrors |
| southern-transitional-council 2026,2026,2026 loss cp republic-of-yemen | - | exception | republic-of-yemen ends 2024; the January 2026 events have no counterpart alive in 2026 |
| palestinian-national-authority 1995 gain cp state-of-israel | - | missing | state-of-israel has no 1995 (Oslo II) event naming this state, nor a 1994 one for Gaza-Jericho (this state found cp none, predecessor state-of-israel) |
| palestinian-national-authority 2005 gain cp state-of-israel | state-of-israel 2005 occupation_end | mismatch | state-of-israel ledger/39 (2005-09 occupation_end of the Gaza Strip) names 'palestinians' (the 1948-1950 polity); it should name palestinian-national-authority |
| sharifate-of-mecca 1803 loss cp emirate-of-diriyah | emirate-of-diriyah 1803 gain | mismatch | emirate-of-diriyah ledger/12 (1803 gain of Mecca) names ottoman-empire, not this state |
| sharifate-of-mecca 1813 gain cp emirate-of-diriyah | emirate-of-diriyah 1813 loss | mismatch | emirate-of-diriyah ledger/21 (1813-01 loss of Mecca) names muhammad-ali-dynasty; this dossier regains from emirate-of-diriyah |
| emirate-of-bani-khalid 1793 loss cp emirate-of-diriyah | emirate-of-diriyah 1795 gain | mismatch | emirate-of-diriyah ledger/7 gains Hasa in 1795 from the string 'Bani Khalid Emirate' (2 years after this 1793 loss; ledger/5 Qatif 1794); fix the string to emirate-of-bani-khalid and reconcile 1793/1795 |
| emirate-of-bani-khalid 1818 gain cp emirate-of-diriyah | - | missing | emirate-of-diriyah has no 1818 loss of Hasa; its dissolve (ledger/29, 1818-09) names muhammad-ali-dynasty |
| iraqi-republic 2005 gain cp kurdistan-region | kurdistan-region 2005 rename | mismatch | iraqi-republic ledger/14 regains the three governorates in 2005-10; kurdistan-region keeps them (2005 rename only). Author flagged it as republic-of-iraq; it is iraqi-republic. Replace with vassal_start (federal region) or drop |
| ikhshidid-dynasty 944 vassal_start cp sharifate-of-mecca | - | missing | ikhshidid-dynasty ledger/6; sharifate-of-mecca has no vassal events (and 944 precedes the sharifate start of 967: start the vassalage at 967 on both sides) |
| ikhshidid-dynasty 969 vassal_end cp sharifate-of-mecca | - | missing | ikhshidid-dynasty ledger/14; sharifate-of-mecca has no vassal events |
| sulayhid-dynasty 1064 vassal_start cp sharifate-of-mecca | - | missing | sulayhid-dynasty ledger/5; sharifate-of-mecca has no vassal events |
| sulayhid-dynasty 1067 vassal_end cp sharifate-of-mecca | - | missing | sulayhid-dynasty ledger/7; sharifate-of-mecca has no vassal events |
| ayyubid-sultanate 1174 vassal_start cp sharifate-of-mecca | - | missing | ayyubid-sultanate ledger/1; sharifate-of-mecca has no vassal events |
| ayyubid-sultanate 1238 vassal_end cp sharifate-of-mecca | - | missing | ayyubid-sultanate ledger/17; sharifate-of-mecca has no vassal events |
| rasulid-dynasty 1238 gain cp sharifate-of-mecca | - | missing | rasulid-dynasty ledger/1 takes Mecca from this state; sharifate-of-mecca has no loss or vassal event in 1237-1239 |
| syria 2012 loss cp autonomous-administration-of-north-and-east-syria | autonomous-administration-of-north-and-east-syria 2012 found | mismatch | syria ledger/11 loses the whole Hasakah governorate in 2012; the AANES found event takes only four discs (Afrin, Kobani, Amuda, Qamishli) and K1 adds the governorate in 2014 with no event |
| syria 2017 loss cp autonomous-administration-of-north-and-east-syria | autonomous-administration-of-north-and-east-syria 2017 gain | mismatch | syria ledger/18 loses Raqqa governorate to AANES in 2017-10, but syria already lost it to islamic-state (ledger/13, 2014); AANES gains it from islamic-state |
| syria 2019 loss cp autonomous-administration-of-north-and-east-syria | autonomous-administration-of-north-and-east-syria 2019 gain | mismatch | syria ledger/21 loses Baghuz (Abu Kamal 40 km) to AANES in 2019-03; AANES gains it from islamic-state (ledger/19); syria should drop it or record the 2017 recapture of Abu Kamal from islamic-state instead |
| emirate-of-nejd 1830 gain cp nobody | emirate-of-bani-khalid 1830 dissolve | mismatch | emirate-of-nejd ledger/2 takes Hasa in 1830 from nobody; emirate-of-bani-khalid dissolves into emirate-of-nejd in 1830 (Bani Khalid page: battle with the Subay' and the Al Saud in 1830). Set the Nejd counterpart to emirate-of-bani-khalid |

Matched: 29 entries; repeated routing entries are grouped (years list).

## Problems

- The Context table in section 6 of the author brief lists 39 distant neighbours (Adal Sultanate, Austria-Hungary, Bali, ...); 26 have dossiers, none is a counterpart of this batch, so the cross-checks used the counterparts actually named: ottoman-empire, republic-of-iraq, iraqi-republic, syria, republic-of-turkey, kingdom-of-jordan, kingdom-of-egypt, palestinians, state-of-israel, french-mandate-for-syria-and-lebanon, zand-dynasty, qajar-dynasty, republic-of-yemen, emirate-of-diriyah, emirate-of-nejd, muhammad-ali-dynasty, gaza-hamas, ayyubid-sultanate, ikhshidid-dynasty, sulayhid-dynasty, rasulid-dynasty.
- ottoman-empire (written before this additions batch) mirrors none of the autonomous polities carved out of it here (mamluk-iraq, mamluk-beys-of-egypt, sheikhdom-of-acre, emirate-of-mount-lebanon, sharifate-of-mecca): route a set of vassal_start/vassal_end events to its owner.
- syria, republic-of-iraq, republic-of-yemen, republic-of-turkey and state-of-israel end in 2024 while AANES, houthis, southern-transitional-council, palestinian-national-authority and (after this review) kurdistan-region run to 2026; their 2025-2026 events have no living counterpart.
- The reviewer applied small fixes in place (orchestrator permission): british-mandate-for-palestine ledger/3 counterpart; kurdistan-region end 2026; islamic-state ledger/3-4 confidence; mamluk-beys-of-egypt ledger/5 and sheikhdom-of-acre ledger/13 month; emirate-of-mount-lebanon ledger/1, /11, /12 confidence and ledger/5 month. All six files re-validate with no errors or warnings.
- No page failed to load. Some "page to try" titles under thin are suggestions not opened by the reviewer.
- cross_checks: events with the same counterpart, status and note are grouped into one entry with a years list (event.year is the first).
