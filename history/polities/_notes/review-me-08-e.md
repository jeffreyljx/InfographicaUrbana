# Review of batch me-08-e (Phase B)

Reviewer run 2026-10-20 (brief dated 2026-10-19). Machine copy: history/notes/phase-b/reviews/me-08-e.json.

All five dossiers validate with 0 errors (--resolve warnings: unknown counterpart slugs listed in counterparts_needing_dossiers, and the three empty Ghaznavid corrections by design). Spot checks: every confidence-3 event opened was on its page with its year, except the 1082 Zabid event, which both Yemeni dossiers type as a contest although the page says the Sulayhids captured the city. No infobox in the batch gives an area.

## ghaznavid-empire: fail

### Findings

- `/ledger/33/region`: The 1162 loss names only Ghazni and Zabulistan (about 36,000 km2), but the dossier's own keyframes drop from the 1152 shape minus Iran (about 929,000 km2, valid to 1161) to the 1162 keyframe (the 1177 shape minus Multan, about 100,000 km2): about 760,000 km2 (Kabul, Bamyan, Kandahar and Bust, Helmand, Nimruz, Farah, Baluchistan, Sindh) leave with no event.
  - Evidence: Gazetteer resolve: minus[1152 shape, Iran] = 3,673 cells; union[Ghazni, Zabulistan] = 143 cells; 1177 shape minus Multan = 394 cells. Ghaznavids page: 'Ghazni and Zabulistan were lost to a group of Oghuz Turks' (no year); Khusrau Malik page: Ghazni seized 1161/2 and Lahore became his new capital. No ledger event between 1152 and 1162 removes the rest of Afghanistan or Baluchistan.
  - Fix: Either widen /ledger/33 to the whole lost land, e.g. {"minus":[{"minus":[{"cliopatria":"Ghaznavid Empire","year":1152},{"country":"Iran"}]},{"cliopatria":"Ghaznavid Empire","year":1177}],"text":"Ghazni, Zabulistan and the Afghan lands; the Ghaznavids kept Lahore and the Punjab"}, or (better) add separate losses: Bust/Zamindawar and Ghazna to the Ghurids in the 1150-1151 campaign (Ghurid page; Ghazni sacked 'for seven days'), the rest with the 1161/2 Ghuzz seizure, confidence 1-2 where the pages give no year.
- `/ledger/14`: Multan is gained in October 1010 and never lost, yet the new keyframe 1162 (and the 1177 correction) cut Multan; there is no loss event for about 45,000 km2.
  - Evidence: Ghurid dynasty page as quoted in keyframe 15: Muhammad of Ghor 'captured Multan from the Carmathians' in 1175, so the Qarmatians had retaken it from the Ghaznavids at some undated time; the ghurid-dynasty dossier records 1175 gain counterpart 'Qarmatians of Multan'.
  - Fix: Add a loss of Multan ({"place":"Multan","km":150}) with counterpart 'Qarmatians of Multan' (the string the ghurid dossier uses), confidence 1, at the latest year the 1152 and 1162 keyframes allow (before 1162), and say in the note that the pages give no year; list the gap in notes.
- `/keyframe_review/5/correction`: Keyframe 5 says the 1028 shape 'stands for 1030-1033' and keeps Ray (72%), while /ledger/21 loses Ray to the Kakuyids in 1030; keyframe 7 keeps Ray to 1039 and /ledger/27 loses it again in 1037 with no regain in between.
  - Evidence: Mas'ud I page (as quoted in /ledger/21 and /ledger/27): the Kakuyid Muhammad 'in 1030 wrested Ray from the Ghaznavids' and 'In 1037/8 ... once again occupied Ray'; 'once again' implies a Ghaznavid recovery (governor of Jibal 1033, invasion of western Iran 1035), which the ledger lacks.
  - Fix: Add a gain of Ray from the Kakuyids between the two losses (1033 or 1035, confidence 1-2, Mas'ud I page) and make keyframe 5 a correction that drops Rey 100 km for the years before that regain (a new keyframe 1030-1032 = minus[1028 shape, Rey 100 km]), so ledger and keyframes agree.
- `/ledger/33/counterpart` (applied by reviewer): Counterpart 'oghuz-turks' names a dossier that ends in 1055; the 1161/2 Ghuzz band at Ghazni is not that state.
  - Evidence: oghuz-turks dossier identity end 1055; ghurid-dynasty /ledger/2 (1173) names 'Ghuzz Turks'; Khusrau Malik page: 'a group of Oghuz Turks seized the Ghaznavid capital of Ghazni'.
  - Fix: Changed to 'Ghuzz Turks' in /ledger/33 and in /wars/14/belligerents (reviewer edit, validated).
- `/ledger/16/counterpart`: The 1011 and 1060 gains in Ghor (/ledger/16, /ledger/30) and the 1148-1152 contest (/ledger/31, /ledger/32) name ghurid-dynasty, whose dossier starts in 1152; no mirror can exist.
  - Evidence: ghurid-dynasty identity start 1152; its ledger has events with ghaznavid-empire only in 1179 and 1186. The notes call the 1011/1060 counterpart 'the pre-Ghurid chiefs of Ghur'.
  - Fix: Use a free-text counterpart such as 'Ghur chiefs (Shansabanids)' for 1011 and 1060, or ask sa-04 to start ghurid-dynasty earlier (Sayf al-Din Suri 1148, Ala al-Din Husayn 1150-1151) so the 1148-1152 contest has a mirror.
- `/keyframe_review/2/correction`: The 1000-1014 correction removes only Khwarazm but keeps Sistan, all of Ghor and part of Multan from 1000, while the ledger gains them in 1002, 1011 and 1010; the 1011 Ghor gain (/ledger/16) is itself 'read from the Cliopatria shape', which is circular.
  - Evidence: Author's own keyframe 2 note: 'Sistan (1002), all of Ghor (the page's expedition is 1011) and part of Multan (1006-1010) are in the shape years before the page's dates'.
  - Fix: Either cut Ghor and Multan from the 1000 correction (and Sistan for 1000-1001 via a new keyframe) or say in the correction text that the shape is tolerated for those years and lower /ledger/16 to confidence 1.

### Gaps (thin)

- `/ledger/7`: Year of the Samanid cession of Khorasan (999 at confidence 1). Page to try: https://en.wikipedia.org/wiki/Samanid_Empire
- `/ledger/29`: Seljuk captures of Herat, Sistan, Pushang and Ghur after Dandanaqan are undated and have no loss events; Balkh and Tukharistan (lost by the 1059 peace) have none either. Page to try: https://en.wikipedia.org/wiki/Mawdud_of_Ghazni
- `/identity/rulers`: Rulers 1040-1059 (Muhammad, Mawdud, Mas'ud II, Ali, Abd al-Rashid, Toghrul, Farrukhzad) and 1115-1117 (Shirzad, Arslan-Shah) are missing, so the list is not contiguous. Page to try: https://en.wikipedia.org/wiki/Arslan-Shah_of_Ghazni
- `/ledger/30`: Outcome of the 1060 Ghur expedition (gain at confidence 2 on a page that gives no outcome). Page to try: https://en.wikipedia.org/wiki/Ibrahim_of_Ghazni

### Spot checks

- `/ledger/17` (https://en.wikipedia.org/wiki/Mahmud_of_Ghazni): confirmed: 'defeated the rebels on 3 July 1017, and captured Gurganj'
- `/ledger/22` (https://en.wikipedia.org/wiki/Mahmud_of_Ghazni): confirmed: Mas'ud 'first captured Hamadan and then advanced to Isfahan, which was seized in January 1030'
- `/ledger/20` (https://en.wikipedia.org/wiki/Mahmud_of_Ghazni): confirmed: 'On 26 May 1029, Mahmud entered Ray without resistance'
- `/ledger/8` (https://en.wikipedia.org/wiki/Mahmud_of_Ghazni): confirmed: 28 November 1001 and 'Gandhara and Peshawar annexed' (the battle table says 27 November)
- `/ledger/10` (https://en.wikipedia.org/wiki/Mahmud_of_Ghazni): confirmed: 'In 1002, Mahmud invaded Sistan and dethroned Khalaf ibn Ahmad'
- `/ledger/14` (https://en.wikipedia.org/wiki/Mahmud_of_Ghazni): confirmed: 'In October 1010 ... successfully subdued Multan'
- `/ledger/19` (https://en.wikipedia.org/wiki/Mahmud_of_Ghazni): confirmed: 'Sindh paid tribute from 1026 until his death in 1030 AD'
- `/ledger/29` (https://en.wikipedia.org/wiki/Battle_of_Dandanaqan): confirmed: 23 May 1040, 'Khorasan annexed by the Seljuks'; Ghaznavids page: 'lost all the Ghaznavid lands in Persia and Central Asia'
- `/ledger/0` (https://en.wikipedia.org/wiki/Ghaznavids): confirmed: 'conquered the city from the local Lawik rulers in 962'
- `/ledger/33` (https://en.wikipedia.org/wiki/Khusrau_Malik): confirmed: 'In 1161/2, a group of Oghuz Turks seized the Ghaznavid capital of Ghazni'
- `/ledger/36` (https://en.wikipedia.org/wiki/Khusrau_Malik): confirmed: 'In 1179/80 he seized Peshawar'

Area: infobox none; Cliopatria max 2994471.7 km2. Neither the Ghaznavids page nor the Mahmud page gives an area; keyframe notes say so.

## sulayhid-dynasty: fail

### Findings

- `/ledger/8`: The 1082 event is a contest_start ('marches on Zabid ... recaptured Asma'), but the cited page says the Sulayhids took Zabid in 1082; the Sulayhid reconquest of Zabid and the Tihama (about 22,500 km2) is missing and keyframe 3 (1067-1098, highlands only) is wrong for those years.
  - Evidence: Ali al-Sulayhi page: 'In 1082, al-Mukkaram led a Sulayhid force against Zabid, quickly capturing the city and Asma, forcing al-Ahwal to flee' to the Dahlak islands, and Ibn Shihab was restored as governor; Zabid page: 'her son stormed Zabid and freed her'. Najahid page: 'In 1087, Said al-Ahwal returned to Zabid but was killed that same year by Ahmed al-Mukkaram'; 'Jayyash returned to Zabid disguised as an Indian' (undated; Jayyash 1080-1089 in the succession list).
  - Fix: Make /ledger/8 a gain from najahid-dynasty (same region, confidence 3, Ali page); replace the contest pair with a loss of Zabid to the Najahids at their return (1087 or Jayyash's undated return by 1089, confidence 1-2) or a contest 1087-1089; add a new keyframe 1082-<loss year> = keyframe 3 plus {"union":[{"admin1":"Al Hudaydah","country":"Yemen"},{"place":"Zabid","km":80}]} and split keyframe 3's span; update /wars/2/outcome. Mirror the same in najahid-dynasty.
- `/keyframe_review/1/correction`: The 1056 shape (Cliopatria 1056-1065) is marked wrong and corrected to the 1062 peak shape without saying its years, so for 1056-1061 it overlaps the new keyframe sulayhid-dynasty_1047 (Haraz core).
  - Evidence: Schema: a correction that changes the years 'says so in text'; the note says 1047-1061 is the Haraz core.
  - Fix: Add to the correction text: 'years 1062-1065 only; 1056-1061 is keyframe sulayhid-dynasty_1047'.

### Gaps (thin)

- `/keyframe_review/3`: Between the 1062-1066 peak (about 245,000 km2) and the 1067-1098 highlands (about 30,000 km2) only the Tihama (about 22,500 km2) is lost in the ledger; Sa'dah, Hajjah, Amran, al-Jawf, Ma'rib, al-Bayda, Shabwah, Abyan, Taiz and Aden-Lahij leave with no event (author marks the keyframe low confidence). Page to try: https://en.wikipedia.org/wiki/Arwa_al-Sulayhi
- `/ledger/13`: Who took Sana'a after 1098, and when (confidence 1). Page to try: https://en.wikipedia.org/wiki/Hamdanid_sultans_of_Yemen
- `/ledger/7`: End of the Sulayhid tutelage of Mecca (1067, confidence 1). Page to try: https://en.wikipedia.org/wiki/Sharif_of_Mecca

### Spot checks

- `/ledger/2` (https://en.wikipedia.org/wiki/Sulayhid_dynasty): confirmed: 'The Ma'nids of Aden were defeated in 1062 and forced to pay tribute'
- `/ledger/3` (https://en.wikipedia.org/wiki/Sulayhid_dynasty): confirmed: 'Ali also controlled San'a since 1063'
- `/ledger/9` (https://en.wikipedia.org/wiki/Sulayhid_dynasty): confirmed: Zurayids 'came to power in 1083, at first as Sulayhid tributaries'
- `/ledger/15` (https://en.wikipedia.org/wiki/Sulayhid_dynasty): confirmed: 'With her death in 1138 ... the Sulayhid era came to an end'
- `/ledger/1` (https://en.wikipedia.org/wiki/Ali_al-Sulayhi): confirmed: Zabid and the Tihamah 'later in 1062'
- `/ledger/5` (https://en.wikipedia.org/wiki/Ali_al-Sulayhi): confirmed: Hejaz late 1063, Mecca 'by 1064', client king
- `/ledger/8` (https://en.wikipedia.org/wiki/Ali_al-Sulayhi): not on page as claimed: the page says al-Mukarram captured Zabid in 1082 and al-Ahwal fled; the event is typed as a contest

Area: infobox none; Cliopatria max 75389.7 km2. No infobox area; keyframe 1 compares the shape with Yemen's area.

## najahid-dynasty: fail

### Findings

- `/ledger/3`: 1082 is a contest_start, but the cited page says the Sulayhids captured Zabid in 1082 and the Najahid prince fled to Dahlak; the Najahid loss of Zabid and the Tihama is missing, and /ledger/4 (contest_end 1087) hides the return.
  - Evidence: Ali al-Sulayhi page: 'In 1082, al-Mukkaram led a Sulayhid force against Zabid, quickly capturing the city and Asma, forcing al-Ahwal to flee' (to Dahlak); Najahid page: 'In 1087, Said al-Ahwal returned to Zabid but was killed that same year'; 'Jayyash returned to Zabid disguised as an Indian' (undated).
  - Fix: Make /ledger/3 a loss to sulayhid-dynasty in 1082 (confidence 3, Ali page) and /ledger/4 a gain from sulayhid-dynasty at the return (1087, or by 1089 under Jayyash, confidence 1-2); state in the correction text of the 1072 and 1085 keyframes that the Najahids are landless from 1082 to the return. Keep it in step with sulayhid-dynasty.
- `/identity/rulers` (applied by reviewer): Sa'id al-Ahwal, listed on the page 1062-1080, was missing, leaving 1060-1080 without a ruler, and the Jayyash note wrongly said no ruler is listed for those years.
  - Evidence: Najahid page succession list: 'Sa'id al-Ahwal 1062-1080', 'Abu't-Tami Jayyash 1080-1089'; Najah 1022-1060 in the infobox.
  - Fix: Added {name: Sa'id al-Ahwal, from 1060, to 1080, source Najahid page} and corrected the Jayyash note (reviewer edit, validated).
- `/keyframe_review/1/correction`: The 1066 shape (1066-1071) is corrected to the Tihama for all its years, but the ledger has the Najahids landless until the 1067 gain.
  - Evidence: /ledger/2 gain 1067; capitals note: Sulayhids held Zabid 1062-1067.
  - Fix: Say 'years 1067-1071' in the correction text.

### Gaps (thin)

- `/ledger/2`: Year of the Najahid return to Zabid between 1062 and 1067 (no page dates it). Page to try: https://en.wikipedia.org/wiki/Sa%27id_al-Ahwal
- `/keyframe_review/0`: Extent of the emirate beyond Zabid and the Tihama (all six Cliopatria shapes are marked wrong; the page gives no borders). Page to try: https://en.wikipedia.org/wiki/Tihamah

### Spot checks

- `/ledger/0` (https://en.wikipedia.org/wiki/Najahid_dynasty): confirmed: established 1022; 'The last Ziyadid king died in 1018'
- `/ledger/1` (https://en.wikipedia.org/wiki/Ali_al-Sulayhi): confirmed: Zabid and the Tihamah taken 'later in 1062'
- `/ledger/2` (https://en.wikipedia.org/wiki/Zabid): confirmed: 'In 1067 ... Sa'id Ibn Najah, the prince of Zabid' attacked Ali
- `/ledger/5` (https://en.wikipedia.org/wiki/Zabid): confirmed: 'the Mahdids took over Zabid in 1158'; Najahid page: last sovereign killed by Ali ibn Mahdi in 1158
- `/ledger/3` (https://en.wikipedia.org/wiki/Ali_al-Sulayhi): not on page as claimed: the page has Zabid captured in 1082, not only besieged

Area: infobox none; Cliopatria max 215442.1 km2. No infobox area; all six Cliopatria shapes are marked wrong (all-Yemen union) and corrected to the Tihama (about 22,500 km2), explained in the keyframe notes.

## uyunid-emirate: fail

### Findings

- `/ledger/2`: The split (1137), merge (1191) and split (1209) events (/ledger/2-4) name 'Uyunid principality of al-Hasa', which the dossier's own notes say 'is not a state', and every keyframe keeps al-Hasa (Hofuf 100 km, about 31,000 of the about 66,000 km2 corrected shape) through 1137-1190 and 1209-1252: ledger and keyframes contradict.
  - Evidence: Schema: 'split: part of the state becomes a new state named in counterpart'. Uyunid page: 'his state was divided into two' (531 AH; the parts were al-Hasa and Qatif), 'Mohammed bin Abi al-Hussain united Qatif and Al-Hasa' (587-605 AH), 'The state was divided again after his assassination in 605 H'. Keyframes 0-3 all union Hofuf 100 km.
  - Fix: Either (a) delete /ledger/2-4 and describe the two divisions and the reunion in notes (and in certainty if wanted), keeping one Uyunid state as Cliopatria does, or (b) keep the splits, remove Hofuf 100 km from the keyframes for 1137-1190 and 1209-1252 with new keyframes, and list the al-Hasa branch under counterparts_needing_dossiers. (a) fits the page and the author's notes.

### Gaps (thin)

- `/keyframe_review/0`: The page says 'the state extended to Kuwait' under al-Fadhl and 'the Uyunids' territory stretched from Najd to the Syrian desert' under Muhammad b. Ahmad (undated); no event or keyframe carries either. Page to try: https://en.wikipedia.org/wiki/Eastern_Arabia
- `/ledger/2`: Borders of the two halves after 1137 and 1209 (confidence 1). Page to try: https://en.wikipedia.org/wiki/Al-Ahsa_Oasis
- `/wars/1`: What the 1235 Salghurid invasion took (Bahrain islands?). Page to try: https://en.wikipedia.org/wiki/Salghurids
- `/identity/rulers`: No rulers given; the page lists the emirs. Page to try: https://en.wikipedia.org/wiki/Uyunid_dynasty

### Spot checks

- `/ledger/0` (https://en.wikipedia.org/wiki/Uyunid_dynasty): confirmed: 'In 1077-1078 ... Abdullah bin Ali Al Uyuni defeated the Qarmatians in Bahrain'; infobox founded 1076
- `/ledger/1` (https://en.wikipedia.org/wiki/Uyunid_dynasty): confirmed: 'Then in 513 AH, the capital went back to Qatif'
- `/ledger/2` (https://en.wikipedia.org/wiki/Uyunid_dynasty): confirmed: 'In 531 AH ... his state was divided into two'
- `/ledger/3` (https://en.wikipedia.org/wiki/Uyunid_dynasty): confirmed: 'In the years 587 - 605 AH, Mohammed bin Abi al-Hussain united Qatif and Al-Hasa'
- `/ledger/5` (https://en.wikipedia.org/wiki/Uyunid_dynasty): confirmed: 'It then fell to the Usfurids of Banu Uqayl in 651 AH (1253 CE)'

Area: infobox none; Cliopatria max 73691.6 km2. No infobox area.

## zurayid-dynasty: fail

### Findings

- `/keyframe_review/1/correction`: Keyframe 0 (1083-1138) is the Cliopatria speck (about 2,800 km2, Aden and the Lahij oasis), but keyframes 1 and 2 (1139-1174) use the whole Aden and Lahij governorates plus Ibb (about 21,000 km2); the only event between is the Ibb gain (about 6,000 km2), so about 12,000 km2 of Lahij governorate arrive unexplained. /ledger/0 (found) also uses the whole governorates, contradicting keyframe 0.
  - Evidence: Gazetteer resolve: 1085 shape = 11 cells; union[`Adan, Lahij] = 59 cells; Ibb = 24 cells. Zurayids page: the coastal line held Lahij until 1150 ('Ali will later be killed in the battle of Za'za' in Lahij in 1150, displacing them out of Lahij').
  - Fix: Use one Lahij throughout: either keyframes 1 and 2 = {"union":[{"cliopatria":"Zurayid dynasty","year":1085},{"admin1":"Ibb","country":"Yemen"}]} and /ledger/0 region = the 1085 shape, or keyframe 0 = the Aden and Lahij governorates (as /ledger/0) with a note.
- `/ledger/1/year`: The highland towns are gained in 1139 'page silent on the year', but the page dates the purchase 'a decade later' than the 1138 war.
  - Evidence: Zurayids page: 'The two lines met in open warfare in 1138' ... 'A decade later the ruler Muhammad bin Saba bought a number of important Sulayhid fortresses and towns' and married the last Sulayhid queen; 'Among them were Dhu Jibla, al-Takar, Ibb and Habb.'
  - Fix: Move the gain to c. 1148 (confidence 1, quote 'a decade later'), the 1139 keyframe's from-year with it, and use counterpart 'nobody' or the Sulayhid remnant in the note (the Sulayhid dossier ends 1138).
- `/ledger/2`: The 1150 merge names 'Zurayid coastal line (al-Mas'ud)', a branch already drawn inside this dossier's keyframes; merge means absorbing another state.
  - Evidence: Schema: 'merge: this state absorbs or is absorbed into counterpart'; keyframe 0 already holds Aden and Lahij for both lines.
  - Fix: Delete the merge and describe the civil war's end in notes, or keep it only if the coastal line becomes a separate dossier.

### Gaps (thin)

- `/keyframe_review/1`: 'After the defeat of Al-Msaod branch, The Zurayid sphere of power stretched from Taiz to Dhofar' (Zurayids page): no event or keyframe; also the Ayyubid conquest of the highlands (Turan-Shah, 1173-1174). Page to try: https://en.wikipedia.org/wiki/Turan-Shah
- `/ledger/1`: Exact year of the highland purchase (see fix). Page to try: https://en.wikipedia.org/wiki/Muhammad_ibn_Saba

### Spot checks

- `/ledger/0` (https://en.wikipedia.org/wiki/Zurayids): confirmed: 'The brothers were placed in power in 1083'
- `/ledger/2` (https://en.wikipedia.org/wiki/Zurayids): confirmed: Za'za' in Lahij in 1150
- `/ledger/3` (https://en.wikipedia.org/wiki/Zurayids): confirmed: 'When the Ayyubids conquered Aden on 22 June 1174 the rule of the Zurayids ended'
- `/ledger/1` (https://en.wikipedia.org/wiki/Zurayids): mis-dated: the page says 'a decade later' (c. 1148), confidence 1

Area: infobox none; Cliopatria max 3310.4 km2. No infobox area.

## Cross-dossier matrix

- ghaznavid-empire 962 found (lawik-dynasty) -> no mirror: exception - listed in counterparts_needing_dossiers
- ghaznavid-empire 978 gain (Rukkhaj and Bust (local rulers)) -> no mirror: exception - free-text local rulers
- ghaznavid-empire 986 contest_start (hindu-shahis) -> hindu-shahis 986 contest_start: matched
- ghaznavid-empire 988 gain (hindu-shahis) -> hindu-shahis 991 loss: mismatch - Laghman to Peshawar: 988 (Sabuktigin page) vs 991 in hindu-shahis; both sides flagged in notes
- ghaznavid-empire 998 gain (samanid-empire) -> no mirror: exception - samanid-empire not written yet (owning group has not run)
- ghaznavid-empire 999 gain (samanid-empire) -> no mirror: exception - samanid-empire not written yet
- ghaznavid-empire 1001 gain (hindu-shahis) -> hindu-shahis 1001 loss: matched - Gandhara/Peshawar
- ghaznavid-empire 1002 gain (saffarid-dynasty) -> no mirror: exception - saffarid-dynasty not written yet; its Cliopatria row ends 899, the dossier must run to 1002/3 for this mirror
- ghaznavid-empire 1006 contest_start (emirate-of-multan) -> emirate-of-multan 1006 contest_start: matched
- ghaznavid-empire 1008 gain (hindu-shahis) -> hindu-shahis 1014 loss: mismatch - Punjab: Ghaznavid gain 1008 (and again 1021) vs hindu-shahis contest 1008-1009 and loss 1014, dissolve 1026
- ghaznavid-empire 1010 gain (emirate-of-multan) -> emirate-of-multan 1010 loss: matched
- ghaznavid-empire 1011 gain (ghurid-dynasty) -> no mirror: mismatch - ghurid-dynasty starts 1152; counterpart outside its life (also 1060 gain and 1148-1152 contest)
- ghaznavid-empire 1017 gain (ma-munid-dynasty) -> no mirror: exception - listed in counterparts_needing_dossiers
- ghaznavid-empire 1021 gain (hindu-shahis) -> no mirror: missing - no hindu-shahis loss in 1020-1022 (it has 1014 loss, 1026 dissolve)
- ghaznavid-empire 1026 vassal_start (sind-habbari-dynasty) -> sind-habbari-dynasty 1026 contest_end: mismatch - Mahmud page: Sindh tributary 1026-1030; sind-habbari dissolves 1026 (successor soomra-dynasty); vassal_start is overlord-side by schema
- ghaznavid-empire 1029 gain (buyid-dynasty) -> buyid-dynasty 1029 loss: matched - month differs (26 May vs March/April), flagged by author
- ghaznavid-empire 1030 loss (kakuyids) -> no mirror: missing - kakuyids dossier has no event with ghaznavid-empire (Ray 1030)
- ghaznavid-empire 1030 gain (kakuyids) -> no mirror: missing - kakuyids dossier lacks the loss of Hamadan and Isfahan (January 1030)
- ghaznavid-empire 1034 loss (Harun of Khwarazm (breakaway governor)) -> oghuz-turks 1041 gain: mismatch - oghuz-turks gains Khwarezm from ghaznavid-empire in 1041; Mas'ud I page has Harun independent in 1034, so the oghuz counterpart should be the Altuntashid rulers
- ghaznavid-empire 1034 loss (seljuk-dynasty) -> no mirror: exception - seljuk-dynasty (me-09) not written yet
- ghaznavid-empire 1037 loss (kakuyids) -> no mirror: missing - no Kakuyid regain of Ray in 1037/8 in kakuyids
- ghaznavid-empire 1040 loss (great-seljuk-empire) -> no mirror: exception - great-seljuk-empire (me-09) not written yet
- ghaznavid-empire 1060 gain (ghurid-dynasty) -> no mirror: mismatch - ghurid-dynasty starts 1152
- ghaznavid-empire 1162 loss (Ghuzz Turks) -> ghurid-dynasty 1173 gain: exception - counterpart corrected from oghuz-turks (ends 1055) to the free-text Ghuzz Turks used by ghurid-dynasty
- ghaznavid-empire 1179 loss (ghurid-dynasty) -> ghurid-dynasty 1179 gain: matched - Peshawar
- ghaznavid-empire 1186 dissolve (ghurid-dynasty) -> ghurid-dynasty 1186 gain: matched - Lahore
- lohara-dynasty 1015 contest_start (ghaznavid-empire) -> no mirror: mismatch - lohara records contests with the Ghaznavids in 1015 and 1021; ghaznavid-empire has the 1015 war with empty zones and no 1021 war
- sulayhid-dynasty 1047 found (rassids) -> no mirror: exception - rassids listed in counterparts_needing_dossiers
- sulayhid-dynasty 1062 gain (najahid-dynasty) -> najahid-dynasty 1062 loss: matched
- sulayhid-dynasty 1062 vassal_start (Ma'nids of Aden) -> no mirror: exception - manids-of-aden listed in counterparts_needing_dossiers
- sulayhid-dynasty 1063 gain (rassids) -> no mirror: exception - no dossier, listed
- sulayhid-dynasty 1064 vassal_start (sharifate-of-mecca) -> no mirror: exception - planned in me-08-x, not written
- sulayhid-dynasty 1067 loss (najahid-dynasty) -> najahid-dynasty 1067 gain: matched
- sulayhid-dynasty 1082 contest_start (najahid-dynasty) -> najahid-dynasty 1082 contest_start: mismatch - both sides agree but both misread the Ali page: 1082 is a Sulayhid gain / Najahid loss of Zabid
- sulayhid-dynasty 1083 vassal_start (zurayid-dynasty) -> no mirror: exception - overlord-side by schema; zurayid-dynasty carries no mirror, as the schema intends
- sulayhid-dynasty 1098 loss (hamdanids-of-sanaa) -> no mirror: exception - listed in counterparts_needing_dossiers
- sulayhid-dynasty 1138 dissolve (zurayid-dynasty) -> zurayid-dynasty 1139 gain: matched - within one year; the Zurayid page puts the purchase c. 1148
- fatimid-caliphate 1048 vassal_start (sulayhid-dynasty) -> no mirror: exception - overlord-side; Sulayhid Sana'a 1063 vs Fatimid tie 1048 noted by author
- najahid-dynasty 1022 found (ziyadid-dynasty) -> no mirror: exception - ziyadid-dynasty not written yet; Cliopatria row 866-1138 overlaps the Najahids
- najahid-dynasty 1158 dissolve (mahdids) -> no mirror: exception - Zabid Mahdids listed in counterparts_needing_dossiers; Cliopatria mahdids row is Omani
- uyunid-emirate 1077 found (qarmatians) -> qarmatians 1077 dissolve: matched - qarmatians contest 1067-1077 and dissolve 1077 with counterpart uyunid-emirate
- uyunid-emirate 1137 split (Uyunid principality of al-Hasa) -> no mirror: exception - not a state (see fix); same for 1191 merge and 1209 split
- uyunid-emirate 1253 dissolve (usfurids) -> no mirror: exception - listed in counterparts_needing_dossiers
- zurayid-dynasty 1083 found (sulayhid-dynasty) -> sulayhid-dynasty 1083 vassal_start: matched - Aden from the Ma'nids under Sulayhid tutelage
- zurayid-dynasty 1150 merge (Zurayid coastal line (al-Mas'ud)) -> no mirror: exception - branch of the same state (see fix)
- zurayid-dynasty 1174 dissolve (ayyubid-sultanate) -> no mirror: exception - ayyubid-sultanate not written yet (Cliopatria row from 1177)

## Problems

- No page failed to load. No infobox in the batch gives an area, so every area_check is without a ratio.
- The reviewer brief's mirror rule for vassal_start (a vassal_start in the vassal's ledger) contradicts the schema ('counterpart is the vassal itself in both events'); vassal events recorded only by the overlord are counted as exceptions here.
- Reviewer edits applied and validated: ghaznavid-empire /ledger/33 and /wars/14 counterpart oghuz-turks -> 'Ghuzz Turks'; najahid-dynasty /identity/rulers Sa'id al-Ahwal added and the Jayyash note corrected.
- Cross-batch routing: kakuyids (Ray 1030/1037, Jibal 1030 missing), hindu-shahis (988 vs 991, Punjab 1008/1014/1021), sind-habbari-dynasty (tribute 1026-1030 vs dissolve 1026), oghuz-turks (Khwarezm 1041 counterpart should be the Altuntashids, not ghaznavid-empire), ghurid-dynasty sa-04 (start 1152 leaves 1011/1060/1148-1152 Ghur events without a mirror), lohara-dynasty (1015/1021 contests).
