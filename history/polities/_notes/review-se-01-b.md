# Review of batch se-01-b (Chenla, Land Chenla, Water Chenla, Lavo Kingdom, Haripunjaya)

Reviewed 2026-10-18 by the adversarial reviewer. Validator (`--resolve`): all five valid, 0 errors; warnings only for counterpart slugs without a dossier (dvaravati, tambralinga). Pages opened: Chenla, Jayavarman II, Lavo Kingdom, Haripunjaya. Neighbour dossiers read: funan, champa (the other Context polities are not written yet).

Summary: no fabricated event and no mis-dated year found; every spot-checked date is on its page, including both confidence-3 events (water-chenla 780 Kumbhupura, lavo-kingdom 1388). The recurring defect is quotation: phrases in single quotes are often paraphrases of the page. The reviewer corrected those it verified (marked applied). Remaining items are non-blocking suggestions and gaps for a gap-filler.

## chenla: fix

Area: infobox None km2 (year None), Cliopatria 427021 km2, ratio None. The Chenla infobox has no area row (checked); the dossier says so in keyframes 0, 3 and 4.

Findings:
- `/identity/successors/0/land/text, /ledger/6/note` (applied by reviewer): Quote 'Land Chenla is placed in Isan (northeast Thailand)' is not the page's wording. Evidence: Chenla page: 'Land Chenla is located in Isan (northeast Thailand).' Fix: Replaced 'placed in' with 'located in' (2 places).
- `/identity/capitals/1/note` (applied by reviewer): Composite quote 'Bhavavarman I resided at Bhavapura, probably near modern Thala Barivat' is not on the page; the fact is. Evidence: Chenla page: '...his predecessor Bhavavarman I still resided at Bhavapura, a place which probably is located in the vicinity of the modern town of Thala Barivat' (13 33 N, 105 57 E; the dot 105.95/13.53 agrees). Fix: Replaced with the page's words.
- `/ledger/5, /keyframe_review/3, /keyframe_review/4` (for the author, non-blocking): The 656 gain of the four north-western provinces (Banteay Meanchey, Siem Reap, Oddar Meanchey, Battambang, about 35,000 km2) is land the dossier already draws as Chenla's from 627 (chenla_627 and chenla_641 take the whole Funan shape), so the ledger gains the same land twice and the gain leaves no trace in any keyframe. Evidence: Chenla page: 'the kingdom of Zhenla had conquered different principalities in Northwestern Cambodia' after 31 January 656; funan_546 bbox reaches 14.04 N and chenla_555 starts at 13.08 N, so their union covers all four provinces. Fix: Either cut the four provinces from the chenla_627 correction and from a 641-655 keyframe (new keyframe 656-707 with the full outline), or drop the gain and keep the sentence in the chenla_641 note. Non-blocking: the drawn map is the same either way.
- `/identity/capitals/2, /keyframe_review/0, /keyframe_review/1` (for the author, non-blocking): Isanapura (Sambor Prei Kuk, 12.87 N) is the capital from 600, but the 550-626 shapes stop at 13.08 N, so the capital dot lies outside its own state for 27 years; the author noted it but kept the shape. Evidence: shapes.csv chenla_555 and chenla_617 bbox south edge 13.079; Chenla page 'established their capital city at Isanapura (Sambhupura) by about 600'. Fix: Adjust chenla_555 (600-616) and chenla_617 to union the Kampong Thom province (admin1 'Kâmpóng Thum', Cambodia) from 600, or say in the note why the dot may sit outside. Non-blocking.

Gaps (for a gap-filler):
- `/ledger/1`: Confidence 1 for the 598 start of the Funan war; the page does give 'At the end of the sixth century, Bhavavarman and Citrasena (royal title: Mahendravarman) attacked Funan together', which supports c. 598 at confidence 2 (the Funan dossier's mirror is also confidence 1; raise both together). Try: https://en.wikipedia.org/wiki/Chenla
- `/ledger/5`: The names of the north-western principalities Jayavarman I conquered (counterpart is a description, not a slug). Try: https://en.wikipedia.org/wiki/Jayavarman_I

Spot checks:
- `/ledger/0` confirmed (https://en.wikipedia.org/wiki/Chenla): 'whose base was Champassak in about 550'; infobox 'Vassal of Funan: 550'.
- `/ledger/4` confirmed (https://en.wikipedia.org/wiki/Chenla): Infobox 'Independence: 627'; 'attacked Funan together and subdued it around 627-649'; New Book of Tang: Isanavarman I 'managed to absorb the ancient territories of Funan'.
- `/ledger/5` confirmed (https://en.wikipedia.org/wiki/Chenla): 'conquered different principalities in Northwestern Cambodia', after 31 January 656.
- `/ledger/6, /ledger/7` confirmed (https://en.wikipedia.org/wiki/Chenla): 'shortly after 706, the country was split into' Land and Water Chenla; '(after 6 February 707) Zhenla came to be divided in two realms'; infobox 'Separation into Land-Water: c. 707'; 'Both parts sent tribute to China in 717'.

## lavo-kingdom: fix

Area: infobox 170000 km2 (year None), Cliopatria 126307 km2, ratio 0.74. Infobox 'Total: 170,000 km2' with no year (checked). Cliopatria 126-143k km2 for 648-1187 (ratio 0.74-0.84); the 1241 shape 42,717 km2 (ratio 0.25) is acknowledged in keyframe 11 as against an undated peak.

Findings:
- `/ledger/4/note, /keyframe_review/5/note` (applied by reviewer): Quote 'Tambralinga held Lavo as a tributary through 930-946' is not on the page. Evidence: Lavo page infobox 'Tambralinga vassal: 927-946'; the ruler table lists Kampoch '930-946?' 'As a tributary state of Tambralinga'. Fix: Replaced with the infobox row and the table's words.
- `/ledger/3/note, /wars/1` (applied by reviewer): Quote 'Lavo was annexed by Tambralinga from the south in 928' is not the page's wording. Evidence: Lavo page: '...left it open to annexation by Tambralinga from the south in 928'. Fix: Replaced with the page's words (2 places).
- `/keyframe_review/7/note` (applied by reviewer): Quote of the Haripunjaya page 'installed his brother Chadachota as king there' is not its wording. Evidence: Haripunjaya page: 'annexed Lavo in 1052 and appointed his brother, Chadachota, the king of Lavo'. Fix: Replaced with the page's words.
- `/ledger/3, /ledger/4, /keyframe_review/4, /keyframe_review/5` (for the author, non-blocking): 928-945 is drawn as a loss of the whole of Lavo to Tambralinga, but the page's infobox and table call Lavo a vassal/tributary of Tambralinga with its own king (Kampoch); as a loss the land is blank until a tambralinga dossier exists. Evidence: Lavo page: infobox 'Tambralinga vassal: 927-946'; table 'As a tributary state of Tambralinga'; text 'left it open to annexation by Tambralinga from the south in 928'. Fix: Consider keeping Lavo's keyframe through 928-945 (no loss/gain) and asking the tambralinga dossier for vassal_start/vassal_end lavo-kingdom 928/946; or keep the loss and say why annexation is preferred over the infobox's vassalage. Non-blocking (the page supports both words).

Gaps (for a gap-filler):
- `/ledger/12`: A page dating the 1375 strip lost to Ayutthaya (confidence 1, bridged from Cliopatria). Try: https://en.wikipedia.org/wiki/Ayutthaya_Kingdom
- `/keyframe_review/10, /keyframe_review/11`: The extent of Lavo after 1218 (the 1241 outline is a third of the 1187 one); the infobox 170,000 km2 is undated. Try: https://seshat-db.com/core/polity/th_lavo_k_2/
- `/keyframe_review/8`: Who held the isthmus bulge south to 10.1 N in 1056-1187 (no page names a southern conquest). Try: https://en.wikipedia.org/wiki/Tambralinga

Spot checks:
- `/ledger/13` confirmed (https://en.wikipedia.org/wiki/Lavo_Kingdom): 'After Ayutthaya Kingdom was officially established in 1351, Lavo was annexed into Ayutthaya in 1388'; confidence 3 holds.
- `/ledger/5` confirmed (https://en.wikipedia.org/wiki/Lavo_Kingdom): 'his appointment as governor by Suryavarman I is conventionally dated to 1006'; other dates on the page (946, 1001, around 1005, 1011-1014) are noted by the author.
- `/ledger/6` confirmed (https://en.wikipedia.org/wiki/Lavo_Kingdom): 'In 1052, Lavo passed out of Angkorian control when it was conquered by Haripunjaya'; infobox 'Reclaimed by Suphannabhum/ Haripunjaya: 1052'.
- `/ledger/9, /ledger/10` confirmed (https://en.wikipedia.org/wiki/Lavo_Kingdom): Infobox 'Lavapura of Angkor: 1181-1218' and 'Lavapura of Phraek Si Racha: 1218-1351'; 'Jayavarman VII appointed his kinsman Narupatidnavarman to govern Lavapura'.
- `/ledger/3` confirmed (https://en.wikipedia.org/wiki/Lavo_Kingdom): 'annexation by Tambralinga from the south in 928'; quote wording fixed.

## haripunjaya: thin

Area: infobox None km2 (year None), Cliopatria 143044 km2, ratio None. No area row in the Haripunjaya infobox (checked); the dossier says so.

Findings:
- `/ledger/5/note, /wars/1/outcome` (applied by reviewer): Quote 'annexed Lavo in 1052 and installed his brother Chadachota as king there' is not the page's wording. Evidence: Haripunjaya page: 'annexed Lavo in 1052 and appointed his brother, Chadachota, the king of Lavo'. Fix: Replaced with the page's words (2 places).

Gaps (for a gap-filler):
- `/ledger/7, /keyframe_review/3`: The largest border move of the state (1188: 143k to 55k km2, about 88,000 km2 to the Khmer Empire) is confidence 1 with both the Haripunjaya and Khmer Empire pages silent; a page dating Angkor's hold on the Tak/upper Ping lands (or saying Cliopatria's outline is wrong) is needed. Try: https://en.wikipedia.org/wiki/Jayavarman_VII
- `/ledger/1`: The northern realm beyond Lamphun (Lampang, Chiang Mai basin) is a confidence-1 gain from the Camadevi legends, undated. Try: https://en.wikipedia.org/wiki/Camadevi
- `/ledger/6`: The end of Haripunjaya's hold on Lavo (1082, confidence 1, bridged to Narai I's capital move). Try: https://en.wikipedia.org/wiki/Lavo_Kingdom
- `/keyframe_review/1`: Any source for the 143,044 km2 outline south to 15.9 N (Seshat th_haribhunjaya_k failed to load for the author). Try: https://seshat-db.com/core/polity/th_haribhunjaya_k/

Spot checks:
- `/ledger/0` confirmed (https://en.wikipedia.org/wiki/Haripu%C3%B1jaya): Infobox 'More probable founding of Haripunjaya: 750'; 'the actual beginning is placed at around 750 AD'; chronicle 'between 629-57 AD'.
- `/ledger/5` confirmed (https://en.wikipedia.org/wiki/Haripu%C3%B1jaya): 'annexed Lavo in 1052 and appointed his brother, Chadachota, the king of Lavo' (quote fixed).
- `/ledger/8` confirmed (https://en.wikipedia.org/wiki/Haripu%C3%B1jaya): 'In 1292 the city was besieged and captured by Mangrai'; infobox 'Besieged and captured by Ngoenyang: 1281' (flagged by the author); 'Phraya Yi Ba ... was forced to flee south to Lampang'.
- `/ledger/4` confirmed (https://en.wikipedia.org/wiki/Haripu%C3%B1jaya): Monarch list: Traphaka 924-927, 'Uchitta jakraphad, King of Lavo' 927-930: a change of line in 927.
- `/ledger/7` not on page (https://en.wikipedia.org/wiki/Haripu%C3%B1jaya): Nothing on 1188, Tak or a Khmer loss; the dossier says so and keeps the event at confidence 1 (honest, not fabricated).

## land-chenla: fix

Area: infobox None km2 (year None), Cliopatria 183796 km2, ratio None. Shares the Chenla article; no infobox area.

Findings:
- `/identity/predecessors/0/land/text, /keyframe_review/0/note, /ledger/0/note` (applied by reviewer): Quote 'Land Chenla is placed in Isan (northeast Thailand)' is not the page's wording. Evidence: Chenla page: 'Land Chenla is located in Isan (northeast Thailand).' Fix: Replaced 'placed in' with 'located in' (3 places).
- `/identity/successors/0/land/text, /ledger/1/note` (applied by reviewer): Quote 'Land Chenla kept its integrity under Jayavarman II' is not the page's wording. Evidence: Chenla page: 'Land Chenla maintained its integrity under Jayavarman II, who proclaimed the Khmer Empire in 802.' Fix: Replaced 'kept' with 'maintained' (2 places).

Spot checks:
- `/ledger/0` confirmed (https://en.wikipedia.org/wiki/Chenla): Split 'shortly after 706' / 'after 6 February 707'; 'Land Chenla is located in Isan (northeast Thailand)'.
- `/ledger/1` confirmed (https://en.wikipedia.org/wiki/Chenla): 'Land Chenla maintained its integrity under Jayavarman II, who proclaimed the Khmer Empire in 802'; infobox 'Jayavarman II proclaimed as chakravatin: 802'.
- `/wars/0` confirmed (https://en.wikipedia.org/wiki/Chenla): Land Zhenla 'sent an embassy to China in 717, aided Mai Thuc Loan's rebellion against the Chinese (722-723)'.
- `/identity/capitals/0` confirmed (https://en.wikipedia.org/wiki/Chenla): 'Tatsuo Hoshino placed Wendan's outer capital at Mueang Fa Daet Song Yang in Kalasin province'; dot at Kalasin town, inside the land-chenla_718 bbox; last mission 798 on the page.

## water-chenla: fix

Area: infobox None km2 (year None), Cliopatria 243130 km2, ratio None. Shares the Chenla article; no infobox area.

Findings:
- `/identity/successors/0/land/text` (applied by reviewer): Quote 'much of Cambodia fell under the orbit of the Shailendra dynasty of Srivijaya' is not the page's wording. Evidence: Jayavarman II page: 'much of the area fell under the orbit of the Shailendra dynasty of Srivijaya' (undated). Fix: Replaced 'Cambodia' with 'the area'.
- `/identity/capitals/0` (for the author, non-blocking): The capital dot is the centroid of the Cliopatria shape, not a site: a made-up location shown as a capital for 83 years. Evidence: Chenla page gives Vyadhapura (Pelliot) and Baladityapura/Aninditapura (Coedes) without locating either; the dossier note admits the dot is the shape centre. Fix: Use a located candidate with a page (Vyadhapura is usually placed at Ba Phnom, Prey Veng; see the Vyadhapura or Ba Phnom article) or keep the dot and mark it as a placeholder in the map legend. Non-blocking.

Gaps (for a gap-filler):
- `/ledger/3, /keyframe_review/1`: Whether Water Chenla ended c. 790 (Chenla page) or survived as a Javanese vassal under Jayavarman II to 802 (his infobox 'King of Lower Chenla (Water Chenla)', 'Reign: c. AD 780-802'); 790-801 is drawn by nobody until a srivijaya dossier adds it (srivijaya_718 reaches only 9.86 N). Try: https://en.wikipedia.org/wiki/Shailendra_dynasty

Spot checks:
- `/ledger/1` confirmed (https://en.wikipedia.org/wiki/Jayavarman_II): 'In 780, the Javanese Shailendra dynasty launched a naval attack on the city of Kumbhupura in Kratie province'; confidence 3 holds (year and province on the page).
- `/ledger/3` confirmed (https://en.wikipedia.org/wiki/Chenla): 'The last of Water Chenla's kings seems to have been killed'; 'the polity incorporated into the Javanese monarchy around the year 790'; infobox 'Javanese invasion: 790'.
- `/wars/1` confirmed (https://en.wikipedia.org/wiki/Chenla): Sdok Kak Thom: 'Jayavarman II and his son Indrayudha defeated a Cham army in 790'.
- `/ledger/0` confirmed (https://en.wikipedia.org/wiki/Chenla): Split c. 707; 'Water Chenla is situated on the Tonle Sap area in Cambodia'.

## Cross-dossier matrix

| event | mirror | status | note |
| --- | --- | --- | --- |
| chenla 550 found funan | funan 550 loss | matched | Both draw an independent Chenla from 550, but the Chenla infobox reads 'Vassal of Funan: 550' and 'Independence: 627': route to funan (se-01-a) to consider vassal_start/vassal_end chenla 550/627 in place of the loss. |
| chenla 598 contest_start funan | funan 598 contest_start | matched | Same zone; both confidence 1. |
| chenla 627 contest_end funan | funan 627 contest_end | matched |  |
| chenla 627 gain funan | funan 627 dissolve | matched | Funan dissolves to chenla in 627. |
| chenla 656 gain northwestern Cambodian principalities | northwestern Cambodian principalities None None | exception | Unnamed principalities, no polity; the land is already Chenla's from 627 in this dossier (finding). |
| chenla 707 split land-chenla | land-chenla 707 found | matched |  |
| chenla 707 split water-chenla | water-chenla 707 found | matched |  |
| land-chenla 802 dissolve khmer-empire | khmer-empire None gain | exception | khmer-empire (se-01, other part): group has not run yet (no file in history/polities/); listed by the author. |
| water-chenla 780 contest_start srivijaya | srivijaya None contest_start | exception | srivijaya (island South-east Asia group): group has not run yet (no file in history/polities/); listed by the author. |
| water-chenla 790 contest_end srivijaya | srivijaya None contest_end | exception | As above. |
| water-chenla 790 dissolve srivijaya | srivijaya None gain | exception | srivijaya must carry the gain (or vassal_start) of Water Chenla's land c. 790 and its end in 802, or the land is blank 790-801; listed by the author. |
| lavo-kingdom 648 found dvaravati | dvaravati None None | exception | No row, no dossier; listed for se-01-x. |
| lavo-kingdom 925 contest_start haripunjaya | haripunjaya 925 contest_start | matched |  |
| lavo-kingdom 927 contest_end haripunjaya | haripunjaya 927 contest_end | matched |  |
| lavo-kingdom 928 loss tambralinga | tambralinga None gain | exception | No row, no dossier; listed (finding: the page calls it vassalage). |
| lavo-kingdom 946 gain tambralinga | tambralinga None loss | exception | As above. |
| lavo-kingdom 1006 loss khmer-empire | khmer-empire None gain | exception | khmer-empire: group has not run yet (no file in history/polities/). It should also carry vassal_start lavo-kingdom 946 (infobox 'Angkor vassal: 946-1052') and its end. |
| lavo-kingdom 1052 gain khmer-empire | khmer-empire None loss | exception | khmer-empire: group has not run yet (no file in history/polities/). |
| lavo-kingdom 1181 loss khmer-empire | khmer-empire None gain | exception | khmer-empire: group has not run yet (no file in history/polities/). |
| lavo-kingdom 1218 gain khmer-empire | khmer-empire None loss | exception | khmer-empire: group has not run yet (no file in history/polities/). |
| lavo-kingdom 1351 loss ayutthaya-kingdom | ayutthaya-kingdom None found | exception | ayutthaya-kingdom (se-01, other part): group has not run yet (no file in history/polities/). |
| lavo-kingdom 1375 loss ayutthaya-kingdom | ayutthaya-kingdom None gain | exception | As above; confidence 1. |
| lavo-kingdom 1388 dissolve ayutthaya-kingdom | ayutthaya-kingdom None gain | exception | As above. |
| haripunjaya 750 found dvaravati | dvaravati None None | exception | No row, no dossier; listed. |
| haripunjaya 750 gain Lawa chiefdoms of Raming Nakhon (Khun Luang Wilangka) | Lawa chiefdoms None None | exception | Legendary, no polity; confidence 1. |
| haripunjaya 925 contest_start lavo-kingdom | lavo-kingdom 925 contest_start | matched |  |
| haripunjaya 927 contest_end lavo-kingdom | lavo-kingdom 927 contest_end | matched |  |
| haripunjaya 1052 vassal_start lavo-kingdom | lavo-kingdom 1052 gain | matched | The overlord records the vassalage (schema); Lavo's own ledger has the 1052 regain from Angkor 'conquered by Haripunjaya', consistent. |
| haripunjaya 1082 vassal_end lavo-kingdom | lavo-kingdom 1082 capital_move | matched | Bridged to Narai I's new line and capital move; confidence 1. |
| haripunjaya 1188 loss khmer-empire | khmer-empire None gain | exception | khmer-empire: group has not run yet (no file in history/polities/); confidence 1, page silent. |
| haripunjaya 1292 dissolve lan-na-kingdom | lan-na-kingdom None gain | exception | lan-na-kingdom (se-01, other part): group has not run yet (no file in history/polities/); its Cliopatria row starts 1294, so it or a ngoenyang dossier must carry the 1292 gain. |

## Problems

- Neighbour dossiers: of the six Context polities in the author's brief section 6 only funan and champa exist in history/polities/; khmer-empire, pagan-kingdom, sukhothai-kingdom and ayutthaya-kingdom are not written yet (their group has not run), so their counterparts are exceptions. srivijaya and lan-na-kingdom also have no file.
- Reviewer applied small quote-wording fixes (verified on the pages) to all five dossiers: chenla (2), land-chenla (2 phrases, 5 places), water-chenla (1), lavo-kingdom (3), haripunjaya (1). All five re-validate with 0 errors and were read back after the write; no other file in history/ was edited apart from this review's notes and report.
- Pattern for the author model: phrases inside single quotes are often paraphrases of the page ('placed in' for 'located in', 'kept' for 'maintained', 'Cambodia' for 'the area', invented 'held Lavo as a tributary through 930-946'); no fabricated event or mis-dated year was found.
- No page failed to load for the reviewer. Pages opened: Chenla, Jayavarman II, Lavo Kingdom, Haripunjaya.
