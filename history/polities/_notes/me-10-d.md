# me-10-d notes (written 2026-10-25 by the Phase B agent for batch me-10-d)

Dossiers written: zand-dynasty (23 events, 11 keyframes, 6 pages), bahrain (4 events, 4 keyframes, 3 pages), kuwait (11 events, 12 keyframes, 4 pages), house-of-khalifa (10 events, 5 keyframes, 4 pages; History of Bahrain, Bahrain and Nasr Al-Madhkur are shared with bahrain). All validate with 0 errors and 0 warnings, also with --resolve. No page failed to load. All text comes through WebFetch's extraction (a model summary of the page), so quotes are the excerpts it returned; a few of its dates carried a "context" caveat and those events are confidence 2.

## Rows merged, split or judged wrong

- kuwait: Cliopatria's "Kuwait" (1757-1872, 1991-2024) and "State of Kuwait" (1961-1989) share Wikidata Q817 and are read as ONE state; one dossier under the earlier slug covers both Names and adds keyframes for the missing 1873-1960 and 1990. DUPLICATE: polities/state-of-kuwait.json (me-10-k) covers 1961-1991 of the same state and should be deleted or made a pointer.
- bahrain: Cliopatria's "Bahrain" (1757-1845, Q398, shared with Kingdom of Bahrain) is NOT one state with the kingdom. Its 1757-1782 shape is the Persian-dependent Bahrain of the Al Madhkur (1753-1783), the dossier `bahrain`; its 1820-1845 shapes (72,705 km2) are the Eastern Province of Saudi Arabia (Al-Ahsa, Qatif, Dammam), the same cells as the Emirate of Diriyah's 1819 shape, and are judged wrong. The continuous Bahraini state under the Al Khalifa is `house-of-khalifa` (1783-1971, with new keyframes for 1800-1802 and the protectorate 1895-1971); the Kingdom of Bahrain (me-10-l) continues it and should start in 1971 (Cliopatria's row starts in 1973).
- zand-dynasty: Cliopatria 1748-1793; the pages date the dynasty 1751-1794, so the 1748 shape is premature and a 1794 keyframe is added. All Karim Khan shapes include Khorasan and Sistan and Baluchestan, which the Zand Iran page excludes; corrected.

## Not settled

- Zand: no page opened dates Karim Khan's conquests of 1751-1760 (Azerbaijan against Azad Khan Afghan, Urmia, Kurdistan, Gilan, Mazandaran, Kerman); the 1752 and 1757 shape steps are unverified (gap-filler: "Azad Khan Afghan", "Mohammad Hasan Khan Qajar"). The seat before 1762 is not named. The vassalage of the Caucasian khanates (1760-1779) is confidence 1 at both ends. The Zand dynasty page is a stub; the Zand Iran page carries the narrative; the Zand Iran page has no infobox area, so no area comparison was possible.
- Bahrain: who held Al-Ahsa, Qatif and Dammam in 1820-1845 (no page opened says; the History of Bahrain page has the Egyptians taking the peninsula in 1830 and Faisal bin Turki taking Al-Ahsa and Saihat in the 1840s). The Qatar tie (Al Bidda) 1843-1868 rests on one sentence; its end is confidence 1. The Qatari-Bahraini War's years are not on the page.
- Kuwait: the Sheikhdom's extent before 1913 (the Kuwait page has no sentence on it); the 1805-1819 outline; the Wahhabi attacks of the 1790s-1810s; a rulers list (the pages date only some reigns).

## Vassalage and protection belongs in the suzerain's ledger (schema: counterpart is the vassal)

To be recorded by the owners of: ottoman-empire (Kuwait a nominal vassal from 1871, Basra Vilayet 1875, autonomous kaza by the 1913 draft); kingdom-of-great-britain (Kuwait 23 January 1899-19 June 1961; Bahrain May 1861-August 1971, agreements of 1868, 1880, 1892); muhammad-ali-dynasty (Bahrain tributary from c. 1830); emirate-of-nejd (Bahrain tribute from 1843, 4,000 krones from 25 July 1851). The Zand dossier records the Al Madhkur's Bahrain as its vassal 1753-1783 (counterpart `bahrain`).

## Gazetteer names needed

Zubarah (Qatar, the Utub base at about 51.03E 25.98N): used in house-of-khalifa as a 30 km radius. Everything else resolved.

## Counterparts needing dossiers

- Emirate of Bani Khalid (rulers of Eastern Arabia from 1670; the Utub took Kuwait from them): suggested slug emirate-of-bani-khalid.
- Sheikhdom of Bushehr (the Al Madhkur, independent from January 1751 per the Nasr Al-Madhkur page, a Zand vassal in 1775, defected to the Qajar c. 1791-1792): suggested slug sheikhdom-of-bushehr.

## Disagreements between pages

Basra surrendered on 20 April 1776 (Siege page) or 16 April (Karim Khan page). The Khalifa move to Bahrain is 1797 (History of Bahrain) or 1799 (Bahrain). The Bani Utbah war with Nasr Al-Madhkur is 1782 (History of Bahrain) or 17 May 1783 (Nasr Al-Madhkur page); the conquest was complete on 28 July 1783. Ahmed Al Fateh died 18 July 1795 (House of Khalifa table) or 1796. The Zand Iran page says Karim Khan founded his dynasty in 1760, the infoboxes say 1751. The Anglo-Ottoman Convention is dated 29 July 1913 on the Kuwait infobox but the Sheikhdom of Kuwait page says the draft was not signed before the First World War.

## Repair of zand-dynasty after review me-10-d (2026-10-25, author)

Reviewer verdict fail; all five fixes applied and re-validated (0 errors, 0 warnings with --resolve; 36 events, 9 sources, 12 keyframes). Pages re-opened with WebFetch: Agha Mohammad Khan Qajar (four reads), Zand Iran, Karim Khan Zand, Azad Khan Afghan, Tabriz Khanate, Khanates of the Caucasus.

What changed:
- Isfahan, November 1788 (fix 1): ledger loss 1788/11 (confidence 2) and a keyframe correction: zand-dynasty_1788 now holds 1788 only and has no Isfahan (Isfahan is the 20 October gain and the November loss); new keyframe zand-dynasty_1789 (1789-1790) equals the 1791 shape; a confidence-1 loss of 1788 takes northern Yazd and Kohgiluyeh out of the 1788 shape. The first correction of the 1788 shape also left a third of Razavi Khorasan in; it is removed.
- North-west and west 1779-1788 (fix 2): added losses for Mazandaran (2 April 1779, year contextual, 2), Semnan (1781, 2), Qazvin and Zanjan (1782, 2), Hamadan stays 1785 (2), Chahar Mahall and Bakhtiari (July 1785, 2); at confidence 1 (bridging, page silent): Azerbaijan (c. 1780, counterpart khanates-of-the-caucasus, as the qajar-dynasty ledger records the 1791 gain from them), Lorestan, Ilam and Khuzestan (c. 1780, nobody), Sabzevar (c. 1780, afsharid-iran), Alborz, Qom and Markazi (1785), the Kurdish country (1785), Golestan (c. 1785). Replaying the ledger from the corrected 1780 shape leaves one cell unexplained against the 1789 shape (checked with the gazetteer). I chose events over correcting the 1780 keyframe: the loss dates are the pages' where they exist and the 1780 shape is Cliopatria's for Karim Khan's reign, which the Tabriz Khanate page supports for Azerbaijan to 1779.
- 1757 jump (fix 3): years-change adjusts: the 1752 shape holds 1751-1759, the 1757 shape from 1760 (the ledger's 1760 gain). A confidence-1 gain of 1752 bridges the 1748 core to the 1752 shape. Khorasan and Sistan are removed from the 1748 and 1752 shapes as from the later ones.
- Keyframe order (fix 4): 1776 before 1780. Rulers 1-7 cite the Zand dynasty page (fix 5).

Corrected from the reviewer's reading or the earlier ledger:
- Semnan, Qumis, Damghan, Shahrud and Bastam were dated 1785 with Hamadan; the page puts them in the narrative of 1781 (after the January 1781 reconciliation, before the Russian landing of August), so they are now 1781 at confidence 2.
- I disagree with the reviewer's reading that Agha Mohammad reached Isfahan on 30 November: three reads of the Agha Mohammad Khan page give the sentence "Agha Mohammad Khan, learning of this, marched rapidly towards Isfahan, which led Jafar Khan withdraw to Shiraz once again and reached the city on 30 November" an ambiguous subject, and two reads take it as Jafar Khan reaching Shiraz ("Agha Mohammad then returned to Tehran rather than attacking Shiraz again"). Both readings put the Zand out of Isfahan by 30 November, so the event is dated 1788/11, confidence 2, with both readings in its note.
- The 1757 shape: the reviewer allowed either a years-change or a bridging gain; I chose the years-change because the Azad Khan Afghan page has the Qajar holding Isfahan, Tabriz and Urmia by June 1757, which weighs against a Zand realm of all Iran that year. The Karim Khan Zand lead ("all of Iran except Khorasan and Balochistan" 1751-1779) is retrospective and undated; the pages disagree.

Still thin or silent (not fixable from the pages opened):
- No page dates a Zand conquest of 1751-1760 (Azad Khan Afghan gives Shiraz taken 29 November 1754, Azad's power 1752-1757 and the Qajar's gains of 1757 only). The 1752 shape is unverified apart from Khorasan; the Isfahan holding of 1754-1759 is doubtful.
- The Khanates of the Caucasus page dates neither the Zand vassalage nor its end (coins in Karim Khan's name, undated). The Tabriz Khanate page: the Donboli pledged to Karim Khan in 1763, Najaf Qoli Khan governor of Tabriz 1769, Sadiq Khan Shaqaqi took Tabriz in 1787, the Qajar destroyed the Sarab Khanate in 1791; it does not say when Zand authority ended.
- The seat of 1751-1761 stays unnamed (Karim Khan Zand page: only "returned to Isfahan in January 1751"; Shiraz as capital undated).
- Isfahan changed hands more often than the ledger shows: the page has Jafar Khan re-capture it in 1785-86 while Agha Mohammad was against the Bakhtiari, and a Qajar governor (Jafar Qoli Khan, then Ali Qoli) afterwards; those steps are undated and not entered.

Cross-dossier (not mine to edit): qajar-dynasty starts in 1789 and gains Fars only in 1794 (Shiraz fell 21 July 1792); it does record Mazandaran 1779, Gilan and Qazvin/Zanjan 1782, Hamadan 1785 and the 1791 Azerbaijan gain from khanates-of-the-caucasus, which match these losses. afsharid-iran gives the Zand everything outside Khorasan in 1748 against the Zand start of 1751; Sabzevar is entered here as a loss to afsharid-iran. Local Azerbaijani khanates (Tabriz, Sarab, Urmia, Khoy) have no dossier and are carried as khanates-of-the-caucasus.
