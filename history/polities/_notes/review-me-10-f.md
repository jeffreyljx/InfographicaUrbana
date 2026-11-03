# Review of batch me-10-f (2026-10-25)

Reviewer: adversarial reviewer, Phase B. Machine copy: history/notes/phase-b/reviews/me-10-f.json.
Validator (with --resolve): 0 errors in all five dossiers; warnings are the expected "no verdict" shapes of the Nejd split, the united-kingdom/sultanate-of-egypt/kingdom-of-hejaz-and-nejd counterparts without dossiers, and the islands that resolve to no cells.

| dossier | verdict | in one line |
| --- | --- | --- |
| emirate-of-nejd | thin | All ten spot checks hold; the 1853 doubling (+495,000 km2) and the 1866/1873/1877/1885/1890 moves are confidence-1 bridges. |
| third-saudi-state | fail | The Asir highlands (Abha, 1920 in asir) have no gain; the 1922 Asir vassal conflicts with asir's 1926. |
| emirate-of-jabal-shammar | thin | Spot checks hold; the 1885 and 1890 keyframe growth has no event here (Nejd has the losses). |
| trucial-states | fix (applied by reviewer) | The Buraimi occupation pair was Omani land on the page; changed to a contest pair, which now matches the Saudi dossier. |
| khedivate-of-egypt | fail | The 1885 loss gives the Red Sea and Somali coasts to the Mahdists; Zeila/Berbera, Massawa (Italy), Suakin (to 1899), and the 1882-83 Mahdist gains have no events. |

## emirate-of-nejd: thin
Spot checks (confirmed): /ledger/0 (Nejd page, "reconquest of Riyadh from Ottoman-Egyptians forces in 1824"), /3 (Jabal Shammar, vassal 1836-1848), /5 (Expedition page, recall "in April 1840"), /9 and /10 (Nejd page, Mesaimeer June 1851, peace of 25 July), /14 (Unification, "from 1871"), /18 (Muhammad bin Abdullah, "In 1887 he annexed Najd"), /22 (Mulayda, 21 January 1891), /6 and /7 (Faisal page).
Area: no infobox area in the served page (re-fetched); Cliopatria peak 1,116,421 km2 (1853). Acknowledged in notes.
Advisory (not blocking): /ledger/9-10 name house-of-khalifa as the owner of Qatar, but the exact mirror is qatar-dynasty /ledger/2-3; house-of-khalifa records only a contest at Al Bidda.
Thin (for a gap-filler): /ledger/11 (1853, +495,000 km2, no page), /13 (1866), /15 (1873), /16 (1877), /17 (1885), /19 (1890), /1 (1825), /12 (1865), /20 (1891); capital names and a ruler strip (try House of Saud, Abdullah bin Faisal Al Saud, History of Saudi Arabia).

## third-saudi-state: fail
Spot checks (confirmed): /0 (Emirate of Riyadh, 13 January 1902), /2 (13 April 1906), /4 (al-Hasa 1913), /5 (Darin, 26 December 1915), /10 (2 November 1921), /13 (2 December 1922, "29th parallel"), /14-16 (Hejaz campaign 29 August 1924, Mecca 13 October 1924, Medina 9 December 1925), /19 (8 January 1926).
Blocking:
1. Missing 1920 gain of Abha and the Asir highlands. asir /ledger/7 (Asir Province page, "The Saudis took control of the regional capital Abha in 1920", confidence 2) has no mirror here, and /keyframe_review/7 keeps Cliopatria's 1924 outline (south to 16.4 N, with the highlands) as "unchanged" with no event for them. Fix: add {1920, gain, asir, region {minus:[{cliopatria:"Asir",year:1917},{region:"Tihama"}]}, Asir Province page, confidence 2}, and union the highlands into the 1920 and 1922 corrections (or date the gain 1924 with a page).
2. /ledger/11 vassal_start asir 1922 (confidence 1, no year on the page) contradicts asir /ledger/12 (Saudi suzerainty 1926 with kingdom-of-hejaz-and-nejd, confidence 3) and stays unpaired. Fix: delete it and remove the Idrisid Tihama from the 1924 correction instead of tinting it.
Advisory: /ledger/13 Uqair polygon (46.5-48.5 E, 28-29 N) also covers Kuwait's 28.83-29.0 N strip (State of Kuwait 1961 outline, drawn by kuwait 1923-1960) and the Neutral Zone; kuwait records no loss. Write it as {minus:[polygon,{cliopatria:"State of Kuwait",year:1973}]}.
Thin: /ledger/1 (1905), /ledger/12 (1922 northern lands).

## emirate-of-jabal-shammar: thin
Spot checks (confirmed): /0, /2, /4, /6 (page gives 1902 and 1904; 13 January 1902 used), /8, /11 (text 2 November, infobox 3 November 1921).
Thin: keyframes 1885 (+86,000 km2) and 1890 (+153,000 km2) have no event here; emirate-of-nejd /ledger/17 and /19 hold the mirror losses (confidence 1), so add the two mirror gains with the same regions. Also /1 (1877), /5 (al-Jawf, Tayma, Khaybar), /7 (1905), /9 (1916), all confidence 1.
The 1836-1848 vassalage is recorded only in emirate-of-nejd (schema convention); not counted as a fault.

## trucial-states: fix, applied by the reviewer
The Buraimi Dispute page says the Saudi guards "occupied Hamasa, one of three Omani villages in the oasis". The occupation is Oman's (kingdom-of-saudi-arabia /ledger/8-9 already record it against sultanate-of-oman), so /ledger/2-3 became contest_start/contest_end over the oasis (war "Buraimi Dispute" zone), matching kingdom-of-saudi-arabia /ledger/7 and /10. /ledger/1's quote was corrected to the page's words ("not to dispose of any territory except to Britain"). Re-validated: 0 errors.
Spot checks (confirmed): /0 (8 January 1820), /1 (6-8 March 1892), /4 (29-30 November 1971), /5 (1 December 1971), /6 (2 December 1971).
Area: no infobox area on the page. Thin: the undated division of the oasis (try Treaty of Jeddah (1974)).

## khedivate-of-egypt: fail
Spot checks: /4 Darfur 1874, /6 Harar 11 October 1875, /11 Tel el-Kebir September 1882, /12 Hewett Treaty 1884, /20 19 December 1914 confirmed; /3 Bogos confirmed (the extract cut the year); /16 year confirmed but its region is not on the page.
Area: infobox 5,000,000 km2 ("inhabited areas only"; Egypt with deserts 994,000 km2) against the 1877-1884 shape 3,002,652 km2, ratio 0.60, acknowledged.
Blocking:
1. /ledger/16 (1885 loss to mahdist-state, confidence 3) gives the Mahdists every land outside Egypt, including the Red Sea and Somali coasts. The Turco-Egyptian Sudan page names only the fall of Khartoum; the Khedivate page says the Massawa province "was taken over by the Kingdom of Italy shortly thereafter"; Suakin stayed Egyptian to 10 July 1899 (anglo-egyptian-sudan /ledger/2); mahdist-state /ledger/6 leaves out Wadi Halfa and Suakin. Restrict the region to the Sudan interior and lower it to 2 unless a page names the land (same for /17 and the Mahdist War zone).
2. Missing losses: Zeila and Berbera in 1884 (keyframe 1884 removes them with no event), Massawa to Italy in 1885 (kingdom-of-italy or italian-africa), Kordofan 1882 and Darfur 1883 (mahdist-state /ledger/1-2), Suakin to anglo-egyptian-sudan in July 1899.
3. Keyframe khedivate-of-egypt_1885 (Egypt only) must keep Suakin and Wadi Halfa until 1899 and split there.
Advisory: Harar 1884: emirate-of-harar /ledger/3 says the land came from british-colonial-empire.
Thin: /8 Equatoria and Bahr el Ghazal, /9 Zeila and Berbera (confidence 1), the 1896-1898 reconquest and the 1899 condominium.

## Cross-dossier matrix (summary; full list in the JSON)
- Matched: Nejd and Jabal Shammar 1877, 1887, 1891; Jabal Shammar and third-saudi-state 1902, 1905, 1906, 1921; khedivate and muhammad-ali-dynasty 1865/66, sultanate-of-darfur 1874, emirate-of-harar 1875, mahdist-state 1881; trucial-states and kingdom-of-saudi-arabia 1952/1955 (after the fix).
- Mismatches for other groups: ottoman-empire (Hasa 1873 against Nejd's 1871; 'emirate-of-nejd' in 1913; 'muhammad-ali-dynasty' vassal to 1914 against khedivate-of-egypt; no Nejd vassalage 1843-1891); muhammad-ali-dynasty (gain/loss 1838-1841 against Nejd's occupation 1837-1840); kingdom-of-hejaz, asir, kuwait (slug 'emirate-of-nejd' for 1918-1925); kuwait (no loss at Uqair); emirate-of-harar (1884 counterpart); ethiopian-empire (no Bogos or 1875-1884 war events, af-01); house-of-khalifa (no tribute to Najd); qatar-dynasty against house-of-khalifa over the owner of Qatar in 1851.
- Exceptions: united-kingdom, sultanate-of-egypt (no dossiers, listed); pahlavi-dynasty, united-arab-emirates, kingdom-of-hejaz-and-nejd (rows exist, dossiers not written yet); nobody.
