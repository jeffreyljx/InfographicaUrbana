# Review of batch me-08-c (Qarmatians, Fatimid Caliphate, Buyid dynasty), 2026-10-19

Machine copy: history/notes/phase-b/reviews/me-08-c.json. All three dossiers validate with 0 errors. Before the review they had 5 warnings, all for counterpart slugs that have no dossier yet (ikhshidid-dynasty, uqaylid-dynasty, kakuyid-dynasty). Every Cliopatria shape has a verdict.

Verdicts: qarmatians **fail**, fatimid-caliphate **fail**, buyid-dynasty **thin**. The reviewer applied the small fixes listed below.

## Qarmatians: fail
- **/ledger/5 (blocking).** The 903 gain of Suhar (150 km circle) is never lost. The Abu Sa'id al-Jannabi page says Sohar was "briefly captured after several attempts", with no date. No keyframe draws Suhar, and buyid-dynasty gains the same circle in 972, so the two dossiers overlap from 972 to 1077. Fix: drop the gain, or end it soon after 903 with a loss or a contest pair.
- /ledger/4 (minor, not blocking): the 903 gain of Hofuf repeats land the 899 found already holds. Say in the note that Hajar was lost and retaken inside the 900-903 contest.
- Thin: the 980 drop from 64,680 to 6,700 km2 (Qatar and the UAE coast) has no event; this is acknowledged and was unverified within the 5-page budget. Also thin: the end of Bahrain's 1058 breakaway and the 968 Damascus tribute.
- Spot checks (Abu Sa'id, Al-Hasan al-A'sam, Qarmatians pages): 899, 900, 903 (Hajar), 971, 978, 1058 and 1077 were confirmed. The Suhar event is overstated.
- Cross-check: fatimid-caliphate gains Ramla (972) and Palestine (978) "from the Qarmatians", but this ledger only contests Damascus and Ramla and never holds them. One side must change. The Al-Hasan al-A'sam page supports a 971 Qarmatian capture of Damascus (25 August) and a sack of Ramla (5 September).

## Fatimid Caliphate: fail
- **Morocco (blocking).** /ledger/13 gains all Morocco in 933 and nothing ever loses it. Keyframe 5 (947-959) drops Morocco, about 194,000 km2 less than the 936 shape. Add a loss in 947 or 948 to caliphate-of-cordoba (Idrisid page: the Umayyads "occupied the rest of northern Morocco" under Abul-'Aysh, 948-954).
- **/ledger/31 (blocking).** The 975 loss of {region: Levant} to byzantine-empire has three problems:
  - The page sentence is real ("retook most of Palestine and Syria, leaving only Tripoli in Fatimid control"), but the region includes Tripoli.
  - By this dossier's own ledger the Fatimids had already lost Damascus in 971, and nothing regains the coast or Syria from Byzantium, although keyframes 8-11 draw them.
  - byzantine-empire.json has no event in 975.

  Fix: recast it as a contest pair with byzantine-empire (975-976), or narrow it and add the regain.
- **/ledger/2 (blocking).** Tahert is gained in 911 from rustamid-dynasty, but that dossier dissolves in 909 after losing Tahert to the Fatimids, and keyframe 0 already draws Tahert from 909. Add a 909 gain and write 911 as a retaking from rebels.
- **Byblos (blocking, small).** /ledger/43 gains it in 1089, and keyframe 17 draws it to 1110. Keyframe 18 drops it, but no event loses it. Add the crusader capture with its year from a page.
- **Tartus.** byzantine-empire has a 995 gain and a 1028 loss of Tartus against the Fatimids. Add the mirrors.
- **Applied by the reviewer:** /ledger/13 confidence 3 to 2 (the page names no territory); /ledger/49 and /ledger/50 confidence 3 to 2 (Gaza is not on the Kingdom of Jerusalem page).
- Thin, honestly flagged by the author:
  - the confidence-1 ends of the Kalbid (1044), Sulayhid (1065) and Hejaz (1171) ties;
  - Aleppo 1015-1038+;
  - the crusader capture of Jaffa, Arsuf, Caesarea, Acre and Beirut;
  - the Syrian coast 1028-1089;
  - the Sidon year (the page says 1111; check the siege page).
- Area: the infobox gives 4.1 M km2 with no year, against 1.95 M for the largest shape (ratio 0.47). This is acknowledged in the keyframe 1 note and accepted.
- Spot checks:
  - 914, 931, 969, 970, 972 (Ramla), 1089 and 1153 (Ascalon): confirmed.
  - 933: no territory named.
  - 975: on the page, but overdrawn and unpaired.
- Cross-checks for other groups:
  - idrisids (af-02) contests Fez in 917, where this dossier writes vassalage (the page supports vassalage). It also writes a 925 gain and 927 loss where this dossier writes a contest (the page supports the gain and loss, so the Fatimid side should change). It lacks the 938-948 and 958-974 vassalage.
  - zirid-dynasty (af-02) lacks its own vassal tie to Cairo (972-1048).
  - aghlabid-dynasty names fatimid-caliphate as a counterpart in 907, before the Fatimid start.

## Buyid dynasty: thin
- **Applied by the reviewer:**
  - Kerman. It was a 1028 loss (confidence 1, Cliopatria's date) to great-seljuk-empire, which did not yet exist. It is now 1041 (confidence 2): the Qavurt page says he "defeated the Buyid ruler's army in Kerman and Makran in around 1041 CE". The source was added, the ledger re-sorted (now /ledger/17), and Kerman added to the corrections of keyframes 9 (1028-1033) and 10 (1034-1039).
  - /ledger/14 confidence 3 to 2: the Majd al-Dawla page dates the Hamadan capture to 1023, but not Isfahan.
- Thin:
  - Keyframe 12 (1046-1055) drops Khuzestan, but no event loses it and the correction does not restore it. Check Abu Kalijar.
  - Oman (972) is never lost. The Qavurt page has him depose the Buyid governor, with no date.
  - The 1062 counterpart is supported by the Qavurt page ("Shiraz and its surroundings were handed over to Qavurt Bey").
  - Also thin: the Hasanwayhids, the Samanid frontier, and Khuzestan and Basra in the 980s.
- Routing, not blocking: the dossier adopts the shape of the "Abbasid Caliphate/Buyid Dynasty" row (947-969) without its Name, while that slug is assigned to another part of me-08. The orchestrator should pick one owner.
- Area: the infobox gives 1.6 M km2 (est. 980), against 1.31 M for the 980 shape (ratio 0.82). Fine.
- Spot checks (Buyid dynasty, Majd al-Dawla, Qavurt pages): 945, 967, 979, 980, 981, 997, 1023 (Hamadan) and 1029 (Ray, March/April) were confirmed. The 1028 Kerman date was wrong and has been corrected.
