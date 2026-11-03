# Review of batch sa-05-g (2026-10-25)

Dossiers: talpur-dynasty (thin), khairpur-state (fail). Validator (`--resolve`): 0 errors, 0 warnings for both, before and after the reviewer's edit. Neighbour dossiers read (ledger greps): british-empire, east-india-company, british-raj, durrani-empire, durrani-dynasty, principality-of-kandahar, kalhora-dynasty, khanate-of-kalat, bahawalpur-state, islamic-republic-of-pakistan, sikh-empire, emirate-of-afghanistan, kashmir-and-jammu, kingdom-of-marwar, mughal-empire. russian-empire has no dossier yet (eu-17 not run); it has no bearing on these two states.

Pages opened by the reviewer: Talpur_dynasty, Battle_of_Miani, British_conquest_of_Sindh, Khairpur_(princely_state), Karachi, Umarkot, Shikarpur,_Sindh.

## talpur-dynasty: thin (one fix applied by the reviewer)

What I tried and could not break: the 1783 found (Talpur page: 'established by Mir Fateh Ali Khan in 1783, after he overthrew the Kalhora dynasty in the Battle of Halani'); the 1839 loss of Karachi (Talpur page: 'The British conquered Karachi in 1839'); Miani 17 February 1843 (Miani page); Dubba 24 March 1843 (Talpur and Miani pages); the 1843 annexation at confidence 2 (British conquest infobox: 'Annexation of Sindh into the Bombay Presidency within British India', undated); Shah Shuja's 1832 invasion (Talpur page). The Cliopatria diagnosis holds against shapes.csv: 1822 and 1836 have bbox 60.98-73.98 E (Balochistan), 1840 and 1846-1894 have bbox 71.2-76.2 E, 34.1-37.1 N (Gilgit-Baltistan). Area: the Talpur page's 'over 100,000 square kilometers' (body text, not the infobox, no year) against 535,464 km2 for 1822-1835, ratio 5.4, acknowledged and resolved (verdict wrong, Sindh only). Capital Hyderabad (68.37 E, 25.38 N) is inside the 1820 bbox.

Applied by the reviewer:
- /ledger/1: month 2 added (Karachi page: 'The British East India Company captured Karachi on 3 February 1839 after HMS Wellesley opened fire and quickly destroyed Manora Fort'); https://en.wikipedia.org/wiki/Karachi added to sources. Re-validated: 0 errors, 0 warnings.

Not applied (for a gap-filler):
- /ledger/0 and a missing 1795 gain: the found region (all of Sind) includes Karachi, which was Kalat's until 1795. Karachi page: 'In 1770s, Karachi came under the control of the Khan of Kalat' and 'In 1795, Karachi was annexed by the Talpurs'. Write the found region as Sind minus the Karachi disc, add a 1795 gain of Karachi (30 km) from khanate-of-kalat at confidence 2 citing the Karachi page. The khanate-of-kalat dossier (/ledger/12) holds Karachi to 1843 and loses it to talpur-dynasty in 1843 at confidence 1; it should move to 1795.
- Umerkot/Tharparkar: Umarkot page: 'Amarkot was annexed by Jodhpur State in 1779 from the Kalhora Nawab of Sindh'; the Talpurs captured it at an undated time and 'Umerkot and its fort was traded to the British in 1843 by the Maharaja of Jodhpur'. The found region gives the Thar frontier to the Talpurs from 1783. A gap-filler should date the Talpur capture (Kingdom of Marwar or Tharparkar District pages) and add the gain from kingdom-of-marwar, or cut Umerkot out of the found region.
- Shikarpur and the Durrani frontier in upper Sindh (Shikarpur was Durrani; the Shikarpur, Sindh page is silent on the transfer). Try https://en.wikipedia.org/wiki/Shikarpur_District or the Principality of Kandahar page.
- Advisory: keyframes 6-15 (1846-1894) carry a 70 km Khairpur disc as the correction of a talpur-dynasty shape after the dossier's end (text says 'None for this dossier'). If the compiler does not clip corrections to start..end, Khairpur would be drawn twice (talpur-dynasty and khairpur-state). Consider stating instead that the shapes belong to no Talpur state (Gilgit-Baltistan, for kashmir-and-jammu / the Gilgit owners), or that the compiler must clip.

## khairpur-state: fail

- /identity/end, /ledger/1, /ledger/2: the state ends at its accession to Pakistan (3 October 1947: loss to islamic-republic-of-pakistan and dissolve, both confidence 3). The Khairpur page: 'Princely state of Pakistan (1947-1955)' and 'Disestablished: 30 September 1955'; the dossier's own note says 'the state formally lasted to 30 September 1955'. The sibling princely states of Pakistan, bahawalpur-state and khanate-of-kalat, both run to October 1955 and dissolve into Pakistan. Fix: end {year 1955, month 9}; remove the 1947 loss (the accession is a vassal relation that islamic-republic-of-pakistan records as vassal_start khairpur-state 1947-10 and vassal_end 1955-9); move the dissolve to 1955-9 with counterpart islamic-republic-of-pakistan quoting 'fully amalgamated into West Pakistan in 1955'; extend keyframe 0, the capital and certainty to 1955; last ruler George Ali Murad to 1954 (infobox '1947-1954'). This is a mis-dated confidence-3 dissolve against its own page, hence fail; if the orchestrator instead settles on Pakistan's current model (gain at accession, as Pakistan does for Bahawalpur in 1947 and Kalat in 1948) the dossier can stand, but then bahawalpur-state and khanate-of-kalat must end at accession too.
- Thin: Ali Murad 'was later accused of plotting against the British, and so was stripped of his lands in upper Sindh' (Talpur page, undated): the first-years shape is too small and the loss is unrecorded. Try https://en.wikipedia.org/wiki/Ali_Murad_Khan_Talpur or the Khairpur District page for the year and the districts (unverified by the reviewer; not on the Khairpur page).
- Spot checks: found 1843 confirmed (Miani page: 'Napier had already secured the cooperation of the Amir of Khairpur, Mir Ali Murad Talpur, through promises of land and titles'); accession 3 October 1947 confirmed; area 15,730 km2 confirmed (no year); dissolve 1947 contradicted by 'Disestablished: 30 September 1955'.

## Cross-dossier matrix

| event | mirror | status |
| --- | --- | --- |
| talpur 1783 found from kalhora-dynasty | kalhora-dynasty 1783 loss to talpur-dynasty | matched |
| talpur 1839-2 loss Karachi to british-empire | british-empire / east-india-company: no 1839 gain of Karachi | missing (route to sa-06 / EIC owner) |
| talpur (missing) 1795 gain Karachi from khanate-of-kalat | khanate-of-kalat 1843 loss Karachi to talpur-dynasty (c1) | mismatch: page gives 1795 |
| talpur 1843-2 contest_start / 1843-3 contest_end british-empire | british-empire 1843-2 / 1843-3; east-india-company 1843-2 / 1843-3 | matched |
| talpur 1843-3 loss Sind minus Khairpur to british-empire | british-empire 1843 gain all Sind; east-india-company 1843-3 gain all Sind | mismatch on land: both British dossiers take Khairpur |
| talpur 1843-3 split khairpur-state | khairpur-state 1843-3 found from talpur-dynasty | matched |
| durrani-empire 1783 vassal_start / 1818 vassal_end talpur-dynasty | overlord-side events; Talpur notes mention the tribute | exception (schema: overlord records) |
| principality-of-kandahar 1818-8 vassal_start / 1826-8 vassal_end talpur-dynasty | overlord-side | exception |
| british-empire 1838 vassal_start / 1843 vassal_end talpur-dynasty | overlord-side; Talpur wars note has the 1838 residency treaty | exception |
| khairpur-state 1947-10 loss to islamic-republic-of-pakistan | Pakistan: no Khairpur event | missing (and model conflict, see above) |
| khairpur-state as British vassal 1843-1947 | british-empire: none; british-raj: only the blanket 'Princely states of India (paramountcy)' 1858-1947 | missing in british-empire 1843-1858 |

Project-level problem for the orchestrator: islamic-republic-of-pakistan gains bahawalpur-state (1947-10) and khanate-of-kalat (1948-3) at accession while both dossiers run to October 1955, a double claim for 1947-1955; khairpur-state follows Pakistan's model. One model is needed for the princely states of Pakistan (recommended: vassal 1947-1955, merge 1955).
