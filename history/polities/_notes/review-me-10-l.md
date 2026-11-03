# Review of batch me-10-l (2026-10-25, adversarial reviewer)

All six dossiers validate (0 errors). Spot checks: 31 events opened on 9 pages (Syria, Syrian civil war, Golan Heights, Egypt, Sinai Peninsula, Halaib Triangle, United Arab Emirates, Bahrain, Qatar v. Bahrain, Hawar Islands, Qatar, South Yemen). No fabricated event was found: every confidence-3 event I opened says what its note claims, with the year. The machine copy is history/notes/phase-b/reviews/me-10-l.json.

| slug | verdict | why |
| --- | --- | --- |
| syria | thin | Two small fixes applied by the reviewer. The government's 2016-2017 recapture of the desert and the Euphrates is missing (the islamic-state dossier now has the mirror losses), plus three region fixes that are not blocking. |
| arab-republic-of-egypt | fail | The Halaib Triangle overlaps Sudan from 1971 to 1999, against the dossier's own 2000 gain. The 1973 and 1975 "gains" from Israel have no mirror. |
| united-arab-emirates | fix | The reviewer removed an occupation_start dated 30 Nov 1971, before the state existed. The 1974 Saudi treaty is a lead. |
| kingdom-of-bahrain | fail | The 2001 Hawar "gain from Qatar" has no mirror. The page dates the award to Bahrain to 1939, so Hawar belongs in the keyframes from 1971. |
| state-of-qatar | pass | All four checks confirmed. It stays consistent with Bahrain once Bahrain is fixed. |
| people-s-democratic-republic-of-yemen | pass | All four checks confirmed. The Kamaran mirror is missing on north-yemen's side. |

## Fixes applied by the reviewer (re-validated, 0 errors)
- syria /ledger/13 (2014 loss to islamic-state): confidence 3 lowered to 2. The Syria page says "large parts of Eastern Syria" and names neither Raqqa nor Deir ez-Zor.
- syria /ledger/15 (May 2015 loss to islamic-state): the region is now intersect(Syrian Desert, Syria). The gazetteer's Syrian Desert also covers Iraq's Al-Anbar and Jordan's Mafraq and Ma'an.
- united-arab-emirates: the old /ledger/0 is removed. It was an occupation_start by pahlavi-dynasty dated 1971-11, before the state's start of 1971-12, over islands outside the UAE shape. trucial-states ledger/4 records the seizure as a loss and pahlavi-dynasty ledger/15 as a gain. The ISLANDS sentence in the notes field is amended to match.

## arab-republic-of-egypt: back to the author (blocking)
1. **Halaib Triangle** (/keyframe_review/0-3, /ledger/13). The keyframes keep the 20,580 km2 Triangle in Egypt for 1971-1999 with verdict ok. Yet the ledger gains it from Sudan in January 2000, and republic-of-sudan unions it into Sudan from 1956 to 1999. Halaib page: Halaib "participated in all Sudanese elections until the last Sudanese election in the late 1980s"; "joint control ... until 1992"; "In January 2000, Sudan withdrew its forces".
   - Fix: for 1971-1999, set each correction to minus(<shape>, intersect(country Egypt, lon 35.7 lat 22.6 km 120)), the spec Sudan uses, which resolves.
   - Change the 1973 and 1983 verdicts to adjust.
   - Add a new keyframe arab-republic-of-egypt_2000 (2000-2023) with the Triangle in.
2. **/ledger/3 (1973-10) and /ledger/7 (1975)** are typed as gains from state-of-israel. The land is already Egypt's under the Sinai hatch, and Israel's dossier has no loss for either year (it occupies the Sinai from 1967 to 1982). Fix: retype both as occupation_end.
3. Not blocking: /ledger/6 ends the hatch on a 25 km band on both banks. The band should be the west-bank pocket only: minus(Suez Canal 25 km, Sinai).
- Leads: the Tiran and Sanafir transfer to Saudi Arabia (2016-2017) is in neither dossier. The stages of the Sinai withdrawal from 1979 to 1982 are also missing.

## kingdom-of-bahrain: back to the author (blocking)
/ledger/3 enters the March 2001 award of the Hawar Islands (less Janan) and Qit'at Jaradah as a gain from state-of-qatar. Qatar never held the islands and its ledger has no loss for them. The Qatar v. Bahrain page has "1939: British government decides ownership in favour of Bahrain" and the Court's "16 of the 17 elements ... to Bahrain". As written, /ledger/5 also takes Janan away from Bahrain, but Bahrain's shape never held Janan.
- Fix: set the 1971, 1973 and 2024 keyframes to adjust, with the correction union(Cliopatria Kingdom of Bahrain 1973, region Hawar Islands).
- Delete /ledger/3, or keep it for Qit'at Jaradah alone with counterpart nobody at confidence 2.
- Keep /ledger/4 and /ledger/5, which match Qatar's gains.

## syria: thin (for a gap-filler)
- Missing: the government's recapture of the east from the Islamic State. That covers Palmyra (2016 and March 2017) and Deir ez-Zor and Abu Kamal (September to November 2017). Without these events, /ledger/15 leaves about a third of Syria out of the government's land until December 2024. islamic-state ledger/12 (2016) and ledger/19 (2017-11) already have the mirror losses, cited to the Deir ez-Zor campaign (2017-2019) page.
- Missing: the 2012 losses of eastern Aleppo and Eastern Ghouta to the opposition, which /ledger/16 (2016) and /ledger/19 (2018) undo. Also missing: the 2018 recapture of Daraa and Quneitra and the March 2020 Idlib line. The author listed these as gaps.
- Not blocking: /ledger/21 (March 2019) puts a 40 km circle on Abu Kamal, which the Syrian army took in November 2017. The circle should be about 10 km on Al-Baghuz Fawqani, on the east bank.
- Not blocking: /ledger/19 uses "Damascus (region)", an 80 km circle around Damascus. Use Douma at 12 km instead.
- Not blocking: /ledger/7 ends the Golan occupation only on "Golan minus Quneitra", while /ledger/4 is a gain. As a result the Quneitra cells of the Golan polygon keep the 1973 hatch with no end. Either widen /ledger/7 to the whole Golan or retype /ledger/4 as occupation_end, in both dossiers.

## united-arab-emirates, state-of-qatar, PDRY
- UAE lead: the 1974 Treaty of Jeddah with Saudi Arabia (Khor al-Udeid / Sabkhat Matti). The page says only "formally demarcating the frontiers", and the author had one page of budget left. The counterpart "Ras al-Khaimah" has no dossier; it is added to counterparts_needing_dossiers.
- Qatar: nothing to change. The Saudi border (1965, 1992, 2001) is an optional lead; the shape does not move.
- PDRY: nothing to change. Kamaran 1972 ("until 1972, when North Yemen seized it") has no gain in north-yemen; route that to north-yemen's author. The location of the 1979 war is an optional lead.

## Cross-dossier mirrors to route to other authors
- lebanon: the Syrian occupation of Mount Lebanon, from 1976-10 to 2005-4.
- state-of-israel: the west-bank pocket of 1973-1974 and Taba from 1982 to 1989. Also consider whether Israel's 1974 Quneitra loss should be an occupation_end.
- north-yemen: the gain of Kamaran in 1972.
- islamic-state (written after this batch): its 2016 and 2017-11 losses to syria await Syrian gains.

## Area checks
None of the six infobox areas has a year. Each ratio is the infobox area against the Cliopatria shape, and every one was acknowledged by the author.

| dossier | ratio | infobox km2 | Cliopatria km2 |
| --- | --- | --- | --- |
| Syria | 1.01 | 185,180 | 186,752 |
| Egypt | 1.00 | 1,010,408 | 1,011,241 |
| UAE | 0.93 | 83,600 | 77,581 |
| Bahrain | 1.12 | 786.8 | 881.5 |
| Qatar | 1.10 | 11,581 | 12,778 |
| PDRY | 1.09 | 287,490 | 313,160 |

Syria's 2014 shape is 118,734 km2, a ratio of 0.64. It is acknowledged in /keyframe_review/6 and corrected to the whole country.
