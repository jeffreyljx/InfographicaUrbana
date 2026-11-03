# Review: batch se-01-a (2026-10-18)

Adversarial review of the six se-01-a dossiers. Validator (--resolve): 0 errors in all six; warnings only for the gazetteer places Beikthano and Halin (pyu-city-states) and the placeholder slug van-lang (au-lac). Every page named below was opened with WebFetch on 2026-10-18.

Verdicts: champa **fix**, pyu-city-states **fail**, funan **thin**, early-ly-dynasty **pass**, au-lac **pass**, trung-sisters **pass**. Here `fix` means the reviewer made the fix; `fail` goes back to the author.

## champa: fix

Area: The Champa infobox has no area (only population, AD 800); the dossier says so in keyframes 1 and 8. Post-1471 Cliopatria shapes (8,027 and 7,917 km2) are marked wrong and replaced by province unions (~21,000 km2), explained. (Cliopatria max 130300 km2).

Findings:

- `/ledger/3/region, /ledger/4/region, /wars/1/zones/0` (applied by reviewer). The 446 Liu Song occupation was placed at Simhapura (Trà Kiệu, 'in the Thu Bồn valley'), but the page puts the captured capital near Huế, and the dossier's own capitals have Kandapurpura near Huế until 604 (Simhapura only from 605). Evidence: Lâm Ấp page: the Liu Song 'led by Tan Hezhi invaded Lâm Ấp, captured Lâm Ấp's capital (near modern Huế)' (February 446). Fix: region {place: 'Hue', km: 60, country: 'Vietnam', text: "Lâm Ấp's capital (near modern Huế)"} in all three places; confidence of /ledger/3 kept at 3 (year and place both on the page).
- `/ledger/14/note, /identity/capitals/3/note` (applied by reviewer). The quoted sentence 'In 875, Indravarman II moved the capital to Indrapura (and established a Buddhist dynasty)' is not on the Champa page; the facts are. Evidence: Champa page: 'In 875, a new Buddhist dynasty founded by Indravarman II (r. ? – 893) moved the capital or the major center of Champa to the north again'; 'Indravarman II established the city of Indrapura, near My Son and ancient Simhapura'. Fix: Replaced the composite quote with the page's two sentences (and the page's own 'Golden Age' sentence in /ledger/14).
- `/ledger (1695–1832), /keyframe_review/25` (not blocking, for the author). No vassal event on Champa's side for the Thuận Thành client state, which the dossier draws as plain Champa from 1695 to 1832; the tint is left entirely to nguyen-lords and nguyen-dynasty. Evidence: Panduranga page: 'From 1695 onward, Panduranga had been reduced to a client state of the Nguyen domain', 'according to a following treaty signed in 1712'. Reviewer brief check 3 expects a vassal relation to appear in both ledgers. Fix: Either add vassal_start 1695 (counterpart nguyen-lords) with its vassal_end when the lords fall, then vassal_start/vassal_end under nguyen-dynasty to 1832, citing the Panduranga page; or note that by the schema the suzerain alone carries the tint and the orchestrator accepts that. Not blocking.
- `/ledger/29, /ledger/30, /wars/6` (not blocking, for the author). Counterpart yuan-dynasty is outside its Cliopatria life in 1283–1285: the row 'Yuan Dynasty' is 1294–1374; Cliopatria's 'Mongol Empire' (mongol-empire, 1206–1293) covers China then. Evidence: history/data/polities.csv rows yuan-dynasty 1294..1374 and mongol-empire 1206..1293. Fix: Keep yuan-dynasty only if its dossier starts by 1271 (route the occupation to whichever group owns it); otherwise use mongol-empire. Not blocking.

Gaps for a gap-filler:

- `/ledger/10`: Who held Kauthara and Panduranga before 757 (counterpart 'nobody', confidence 1); the gain names three coastal provinces (~16,500 km2) while keyframe 7 adopts Cliopatria's 875 shape, +52,400 km2 over the 641 shape (south edge 11.47 to 10.38 N), so most of the added (inland) area has no named event. Try https://en.wikipedia.org/wiki/Kauthara
- `/ledger/2`: Outcome of Fan Wen's 347 war (the Hoành Sơn frontier); the Lâm Ấp page records only the attack (confidence 1). Try https://en.wikipedia.org/wiki/Rinan_Commandery
- `/ledger/4, /ledger/6, /ledger/17`: End years of the 446 and 605 occupations and of the 982 Vietnamese presence at Indrapura (989), all confidence 1. Try https://en.wikipedia.org/wiki/L%C3%AA_Ho%C3%A0n
- `/ledger (1044, 1312–1326)`: The 1044 Lý Thái Tông sack of Vijaya and the 1312–1326 Trần vassalage (author's gaps, 'page silent'). Try https://en.wikipedia.org/wiki/L%C3%BD_Th%C3%A1i_T%C3%B4ng
- `/keyframe_review/19`: The Cham highland rump after 1471 that 'submitted to Thánh Tông as vassals' is not drawn. Try https://en.wikipedia.org/wiki/Champa%E2%80%93%C4%90%E1%BA%A1i_Vi%E1%BB%87t_War_(1471)

Spot checks:

- `/ledger/38`: confirmed. 'Northern Champa (now Quảng Nam, Quảng Ngãi and north of Phú Yên) was annexed'; Vijaya fell March 22, 1471; expedition set out November 28, 1470 (/ledger/36). (https://en.wikipedia.org/wiki/Champa%E2%80%93%C4%90%E1%BA%A1i_Vi%E1%BB%87t_War_(1471))
- `/ledger/27`: confirmed. 'From 1203 to 1220, Champa as a Khmer province was ruled by a puppet government'. (https://en.wikipedia.org/wiki/Khmer%E2%80%93Cham_wars)
- `/ledger/28`: confirmed. 'voluntary Khmer evacuation of Champa in 1220'. (https://en.wikipedia.org/wiki/Khmer%E2%80%93Cham_wars)
- `/ledger/19, /ledger/20`: confirmed. 1145 sack of Vijaya; 1149 ended the occupation of northern Champa. (https://en.wikipedia.org/wiki/Khmer%E2%80%93Cham_wars)
- `/ledger/21`: confirmed. 'in June 1177 Jaya Indravarman IV ... launched a surprise naval assault on Angkor'; recovery by 1181 (Khmer–Cham wars). (https://en.wikipedia.org/wiki/Champa)
- `/ledger/18`: confirmed. 1069 invasion, Vijaya burned, Rudravarman III captured, Địa Lý, Ma Linh, Bố Chính ceded, now Quảng Bình and Quảng Trị. (https://en.wikipedia.org/wiki/L%C3%BD_Th%C3%A1nh_T%C3%B4ng)
- `/ledger/31, /ledger/34, /ledger/35`: confirmed. 1306 Ô and Lý; 1402 Thăng, Hoa, Tư, Nghĩa and Tân Ninh to the Hồ; the return placed after the 1406 Ming invasion. (https://en.wikipedia.org/wiki/Champa%E2%80%93%C4%90%E1%BA%A1i_Vi%E1%BB%87t_War_(1367%E2%80%931390))
- `/ledger/41, /ledger/42, /ledger/40`: confirmed. 1653 Kauthara lost; 1692 Nguyễn Phúc Chu invades, Trấn Thuận Thành; 1611 'annexing the entire Kauthara Principality' honestly read as Phú Yên at confidence 2. (https://en.wikipedia.org/wiki/Panduranga_(Champa))
- `/ledger/29, /ledger/30`: confirmed. February 1283 capture of Vijaya; Mongols repelled by June 1285. (https://en.wikipedia.org/wiki/Champa)
- `/ledger/12, /ledger/13`: confirmed. 'seized Nghệ An in 803'; 'recovered lost regions in 809'. (https://en.wikipedia.org/wiki/Champa)
- `/ledger/44`: confirmed. Infobox November 1832, body August 1832; noted in the dossier. (https://en.wikipedia.org/wiki/Champa)
- `/ledger/3`: not on page. Year confirmed (February 446) but the place is wrong: capital 'near modern Huế', not Simhapura; fixed by the reviewer. (https://en.wikipedia.org/wiki/L%C3%A2m_%E1%BA%A4p)
- `/ledger/14`: confirmed. 875 confirmed; quoted words not on the page; fixed by the reviewer. (https://en.wikipedia.org/wiki/Champa)
- `/ledger/1`: confirmed. 'In 248, Lâm Ấp force invaded from the south, seized most of Rinan'. (https://en.wikipedia.org/wiki/L%C3%A2m_%E1%BA%A4p)

## pyu-city-states: fail

Area: No infobox area on the Pyu city-states page; the dossier says so. (Cliopatria max 116187 km2).

Findings:

- `/keyframe_review/3, /keyframe_review/4, /keyframe_review/5, /keyframe_review/6` (BLOCKING, for the author). Keyframes 850, 860, 960 (verdict ok) and 1040 (years only) keep Cliopatria shapes that still contain Halin and the Mu valley, so the map gives Halin back to the Pyu from 850 to 1044 with no gain event after the 832 loss (/ledger/6) and keyframe 2. Evidence: shapes.csv: pyu-city-states_850 is 111,322 km2 against 116,187 for the 84 shape, the 4,865 km2 difference being Pagan's first shape (the author's own K3 note), with the same bbox 94.41–96.95 E, 18.35–24.01 N, so Halin (22.47 N 95.82 E) is inside it. The K3 note concedes 'Halin's region should also be absent (see the 832 keyframe); within precision', but an 80-km circle is about 20,000 km2, some 18% of the shape. Fix: Make keyframes 3–6 adjust with correction {"minus": [{"cliopatria": "Pyu City-States", "year": Y}, {"place": "Halin", "km": 80, "country": "Myanmar"}], "text": ...} for Y = 850, 860, 960, 1040; or, if the author decides Nanzhao only raided ('destroying the city of Halin in 832'), drop the 832 loss and keyframe 2 and keep the raid as a war zone.
- `/ledger/5` (not blocking, for the author). The 763 loss to Nanzhao (circle lon 96.2, lat 24.6, 150 km) overlaps the north of the 84 shape (the circle reaches 23.25 N, the shape 24.01 N), but no keyframe removes that land for 763–831 (keyframe 1: 'unchanged, 84–831'). Evidence: Pyu page: 'By 763, the Nanzhao king Ko-lo-feng had conquered the upper Irrawaddy Valley'; the event note itself says the land is 'mostly outside Cliopatria's Pyu shape'. Fix: Either add a keyframe 763–831 minus the overlap, or move the circle north of 24.0 N and say in the note that the loss lies outside the drawn realm. Not blocking.
- `/ledger/10/region/text` (not blocking, for the author). The dissolve's region text lists 'the Minbu plain' as Pyu land still outside Pagan in 1044, but the Pagan page puts riverine Minbu inside Pagan by then. Evidence: Pagan page: by 1044 Pagan comprised 'roughly the present districts of Mandalay, Meiktila, Myingyan, Kyaukse, Yamethin, Magwe, Sagaing' plus riverine parts of Minbu and Pakkoku. Fix: Drop 'and the Minbu plain' from the text. Not blocking.

Gaps for a gap-filler:

- `/ledger/8, /ledger/9`: A page dating the 860 and 960 shrinkages (Cliopatria staging of Pagan’s growth, confidence 1). Try https://en.wikipedia.org/wiki/Early_Pagan_Kingdom
- `/ledger/1, /ledger/2`: Dates for Halin becoming and ceasing to be the premier city (confidence 1). Try https://en.wikipedia.org/wiki/Halin
- `/ledger (808–832)`: Whether Nanzhao ruled the Pyu ('conquering the Pyu city-states in the 820s', title 'Ruler of the Pyu' by 808): a vassal tint or a gain. Try https://en.wikipedia.org/wiki/Sri_Ksetra_Kingdom

Spot checks:

- `/ledger/0`: confirmed. Infobox 'Beikthano founded: c. 180 BCE'. (https://en.wikipedia.org/wiki/Pyu_city-states)
- `/ledger/3`: confirmed. Vikrama dynasty launched the calendar on 22 March 638. (https://en.wikipedia.org/wiki/Pyu_city-states)
- `/ledger/4`: confirmed. Infobox '2nd Sri Ksetra Dynasty founded: 25 March 739'. (https://en.wikipedia.org/wiki/Pyu_city-states)
- `/ledger/5`: confirmed. 'By 763, the Nanzhao king Ko-lo-feng had conquered the upper Irrawaddy Valley'. (https://en.wikipedia.org/wiki/Pyu_city-states)
- `/ledger/6`: confirmed. 'conquering the Pyu city-states in the 820s and destroying the city of Halin in 832'; 3,000 prisoners; 835 return. (https://en.wikipedia.org/wiki/Nanzhao)
- `/ledger/7`: confirmed. Infobox 'Founding of kingdom: 23 December 849'; 'Pyinbya fortified the city in 849 AD'. (https://en.wikipedia.org/wiki/Pagan_Kingdom)
- `/ledger/10`: confirmed. 'In December 1044, a Pagan prince named Anawrahta came to power'; Pyu page: 'to the mid-11th century'. (https://en.wikipedia.org/wiki/Pagan_Kingdom)

## funan: thin

Area: No infobox area on the Funan page; the dossier says so. All four Cliopatria shapes are identical. (Cliopatria max 245198 km2).

Findings:

- `/ledger/2` (not blocking, for the author). The 550 'loss' of Champasak to Chenla removes land that no Funan keyframe contains (the author's K2 note: Champasak 'lies north of this shape'), so it changes nothing drawn and mis-types a dependency's secession as a land loss. Evidence: Funan infobox 'Chenla secession: 550 CE'; but the Chenla page's infobox has 'Vassal of Funan: 550' and 'Independence: 627', and its text calls Chenla 'a vassal of the Kingdom of Funan, which had sent an embassy to China in 616 or 617'. Fix: Model Chenla as Funan's vassal (vassal_start/vassal_end, counterpart chenla, region Champasak), choosing between the two pages (vassalage 550–627 per the Chenla infobox, or ending in 550 per the Funan infobox with a start year from another page) and noting the other; agree the years with the chenla dossier (se-01). Not blocking.

Gaps for a gap-filler:

- `/ledger/1, /ledger/4`: Names and years of the isthmus tributaries (generic counterpart 'isthmus polities (Dunsun and others)', confidence 1); the Funan page attributes the isthmus conquests to 'Funanese kings of the 2nd century', not specifically to Fan Shiman's 220. Try https://en.wikipedia.org/wiki/Langkasuka
- `/ledger/3`: The start of Chenla's campaigns against Funan: 598 is bridged from a temple date (the Chenla page ties 598 only to a temple; 'At the end of the sixth century, Bhavavarman and Citrasena ... attacked Funan'). Try https://en.wikipedia.org/wiki/Bhavavarman_I

Spot checks:

- `/ledger/0`: confirmed. Infobox 'Establishment: 50 CE'. (https://en.wikipedia.org/wiki/Funan)
- `/ledger/2`: confirmed. Infobox 'Chenla secession: 550 CE' (contradicted by the Chenla infobox; see fix). (https://en.wikipedia.org/wiki/Funan)
- `/ledger/6`: confirmed. Infobox 'Chenla conquest: 627 CE'; Book of Sui passage '...who annexed Funan and possessed it'; New Book of Tang 'in the beginning of the Zhenguan era (627–649)'. (https://en.wikipedia.org/wiki/Funan)
- `/ledger/1`: confirmed. Fan Shiman reign A.D. 220–228, apex of power, attacked more than ten kingdoms; honest at confidence 1. (https://en.wikipedia.org/wiki/Funan)
- `/ledger/3, /ledger/5`: confirmed. 'attacked Funan together and subdued it around 627–649'; 598 is a temple date, honest at confidence 1. (https://en.wikipedia.org/wiki/Chenla)

## early-ly-dynasty: pass

Area: No infobox area; the dossier says so. (Cliopatria max 92427 km2).

Gaps for a gap-filler:

- `/keyframe_review/1`: The 561 trim of the northern edge (23.30 to 23.04 N, about 2,100 km2) has no event; small, noted by the author. Try https://en.wikipedia.org/wiki/Chen_dynasty
- `/ledger/7`: The year of the move to Phong Châu (cited in a reference note without a year; confidence 1). Try https://en.wikipedia.org/wiki/L%C3%BD_Ph%E1%BA%ADt_T%E1%BB%AD

Spot checks:

- `/ledger/0`: confirmed. 'in February 544, Lý Bí was declared emperor of Nam Việt'; Early Lý infobox 544–602. (https://en.wikipedia.org/wiki/L%C3%BD_Nam_%C4%90%E1%BA%BF)
- `/ledger/1`: confirmed. 'In October of 544 the Liang dynasty sent an army to reoccupy Jiaozhou'. (https://en.wikipedia.org/wiki/L%C3%BD_Nam_%C4%90%E1%BA%BF)
- `/ledger/2`: confirmed. 'in the winter of 545, Chen surprised the capital during the monsoon season'. (https://en.wikipedia.org/wiki/L%C3%BD_Nam_%C4%90%E1%BA%BF)
- `/ledger/3`: confirmed. 'In February 548, he relinquished imperial authority'; Early Lý note: 'On April 13, 548, Triệu Quang Phục ascended the throne'. (https://en.wikipedia.org/wiki/L%C3%BD_Nam_%C4%90%E1%BA%BF)
- `/ledger/4, /ledger/5`: confirmed. 'eventually drove the Chinese out from Vạn Xuân in 550' (the 557 alternative is noted). (https://en.wikipedia.org/wiki/L%C3%BD_Nam_%C4%90%E1%BA%BF)
- `/ledger/6`: confirmed. 'In 571, Lý Phật Tử broke the truce and attacked Triệu Quang Phục's domain'. (https://en.wikipedia.org/wiki/Early_L%C3%BD_dynasty)
- `/ledger/8`: confirmed. 'In 602, Lý Phật Tử bribed money to governor ... Lệnh Hồ Hy'; 'surrendered to the Sui'. (https://en.wikipedia.org/wiki/Early_L%C3%BD_dynasty)

## au-lac: pass

Area: No infobox area; the dossier says so. The 206–179 BC overlap with Cliopatria’s Nanyue shapes is flagged in the notes. (Cliopatria max 140776 km2).

Gaps for a gap-filler:

- `/ledger`: The Qin campaigns against the Yue and any tributary interval under Nanyue 204–179 BC (page silent; budget 1–2 pages used). Try https://en.wikipedia.org/wiki/Qin_campaign_against_the_Baiyue

Spot checks:

- `/ledger/0`: confirmed. 'Founded in 257 BCE by a figure called Thục Phán'; infobox 'Established: 257/208 BCE'; preceded by Nam Cương and Văn Lang. (https://en.wikipedia.org/wiki/%C3%82u_L%E1%BA%A1c)
- `/ledger/1`: confirmed. 'in 179 BC Zhao Tuo marched southward and successfully annexed Âu Lạc'; Âu Lạc lead 'succumbed to the state of Nanyue in 179 BCE'. (https://en.wikipedia.org/wiki/Nanyue)

## trung-sisters: pass

Area: No infobox area; the dossier says so. (Cliopatria max 99740 km2).

Spot checks:

- `/ledger/0`: confirmed. 'In the 16th year of the Jianwu era (40 AD)'; 'In the spring, the second month'; 'sixty-five strongholds'; infobox reign 40–43. (https://en.wikipedia.org/wiki/Tr%C6%B0ng_sisters)
- `/ledger/1`: confirmed. Under 'Nhâm Dần [Renyin, 42 AD]': 'In the spring, the first month, Ma advanced'; the Hou Hanshu '(40 CE)' conflict is noted. (https://en.wikipedia.org/wiki/Tr%C6%B0ng_sisters)
- `/ledger/2`: confirmed. 43: 'in the fourth month ... beheaded Zheng Ce, Zheng Er' and 'The first month of next year (43 CE)'; no month given, as the note says. (https://en.wikipedia.org/wiki/Tr%C6%B0ng_sisters)
- `/ledger/4`: confirmed. 'In the 10th month, Yuan [went] southwards and entered' Jiuzhen, 19th Jianwu year (43 CE). (https://en.wikipedia.org/wiki/Tr%C6%B0ng_sisters)

## Cross-dossier matrix

No counterpart dossier exists yet, so the rows are exceptions routed to the owning groups; the Tang rows are checked against the worked example.

| event | counterpart | status | note |
| --- | --- | --- | --- |
| champa 248 gain | eastern-wu (loss) | exception | eastern-wu.json not written yet (group ea-03 has not run); it must carry the loss |
| champa 347 gain | western-jin (loss) | exception | western-jin.json not written yet (group ea-03 has not run); it must carry the loss |
| champa 446 occupation_start | liu-song-dynasty (occupation_start) | exception | liu-song-dynasty.json not written yet (group ea-03 has not run); it must carry the occupation_start |
| champa 446 occupation_end | liu-song-dynasty (occupation_end) | exception | liu-song-dynasty.json not written yet (group ea-03 has not run); it must carry the occupation_end |
| champa 605 occupation_start | sui-dynasty (occupation_start) | exception | sui-dynasty.json not written yet (group ea-03 has not run); it must carry the occupation_start |
| champa 605 occupation_end | sui-dynasty (occupation_end) | exception | sui-dynasty.json not written yet (group ea-03 has not run); it must carry the occupation_end |
| champa 757 gain | nobody (loss) | exception | counterpart nobody (no Cliopatria row; author: Cham principalities) |
| champa 803 gain | tang-dynasty (loss) | missing | tang-dynasty.json not written yet (ea-04 copies _example-tang-dynasty.json); the example's ledger has no Champa/Nghệ An event in 803 or 809: ea-04 must add the loss of Nghệ An/Hà Tĩnh in 803 |
| champa 809 loss | tang-dynasty (gain) | missing | tang-dynasty.json not written yet (ea-04 copies _example-tang-dynasty.json); the example's ledger has no Champa/Nghệ An event in 803 or 809: ea-04 must add the gain (recovery) in 809 |
| champa 982 occupation_start | ngo-dynasty (occupation_start) | exception | ngo-dynasty.json not written yet (group se-01 has not run); it must carry the occupation_start |
| champa 989 occupation_end | ngo-dynasty (occupation_end) | exception | ngo-dynasty.json not written yet (group se-01 has not run); it must carry the occupation_end |
| champa 1069 loss | ngo-dynasty (gain) | exception | ngo-dynasty.json not written yet (group se-01 has not run); it must carry the gain |
| champa 1145 occupation_start | khmer-empire (occupation_start) | exception | khmer-empire.json not written yet (group se-01 has not run); it must carry the occupation_start |
| champa 1149 occupation_end | khmer-empire (occupation_end) | exception | khmer-empire.json not written yet (group se-01 has not run); it must carry the occupation_end |
| champa 1177 occupation_start | khmer-empire (occupation_start) | exception | khmer-empire.json not written yet (group se-01 has not run); it must carry the occupation_start |
| champa 1181 occupation_end | khmer-empire (occupation_end) | exception | khmer-empire.json not written yet (group se-01 has not run); it must carry the occupation_end |
| champa 1190 occupation_start | khmer-empire (occupation_start) | exception | khmer-empire.json not written yet (group se-01 has not run); it must carry the occupation_start |
| champa 1191 occupation_end | khmer-empire (occupation_end) | exception | khmer-empire.json not written yet (group se-01 has not run); it must carry the occupation_end |
| champa 1203 loss | khmer-empire (gain) | exception | khmer-empire.json not written yet (group se-01 has not run); it must carry the gain |
| champa 1220 gain | khmer-empire (loss) | exception | khmer-empire.json not written yet (group se-01 has not run); it must carry the loss |
| champa 1283 occupation_start | yuan-dynasty (occupation_start) | exception | yuan-dynasty.json not written yet; Cliopatria's Yuan row starts 1294 (mongol-empire 1206–1293): the owning group must start Yuan by 1271 or the counterpart becomes mongol-empire |
| champa 1285 occupation_end | yuan-dynasty (occupation_end) | exception | yuan-dynasty.json not written yet; Cliopatria's Yuan row starts 1294 (mongol-empire 1206–1293): the owning group must start Yuan by 1271 or the counterpart becomes mongol-empire |
| champa 1306 loss | ngo-dynasty (gain) | exception | ngo-dynasty.json not written yet (group se-01 has not run); it must carry the gain |
| champa 1402 loss | ngo-dynasty (gain) | exception | ngo-dynasty.json not written yet (group se-01 has not run); it must carry the gain |
| champa 1406 gain | ngo-dynasty (loss) | exception | ngo-dynasty.json not written yet (group se-01 has not run); it must carry the loss |
| champa 1471 loss | le-dynasty (gain) | exception | le-dynasty.json not written yet (group se-01 has not run); it must carry the gain |
| champa 1611 loss | nguyen-lords (gain) | exception | nguyen-lords.json not written yet (group se-01 has not run); it must carry the gain |
| champa 1653 loss | nguyen-lords (gain) | exception | nguyen-lords.json not written yet (group se-01 has not run); it must carry the gain |
| champa 1692 occupation_start | nguyen-lords (occupation_start) | exception | nguyen-lords.json not written yet (group se-01 has not run); it must carry the occupation_start |
| champa 1694 occupation_end | nguyen-lords (occupation_end) | exception | nguyen-lords.json not written yet (group se-01 has not run); it must carry the occupation_end |
| champa 1832 dissolve | nguyen-dynasty (gain) | exception | nguyen-dynasty.json not written yet (group se-01 has not run); it must carry the gain |
| pyu-city-states 763 loss | nanzhao (gain) | exception | nanzhao.json not written yet; owning group not in the author's context table (Yunnan/Lingnan group, ea-?), which has not run; it must carry the gain |
| pyu-city-states 832 loss | nanzhao (gain) | exception | nanzhao.json not written yet; owning group not in the author's context table (Yunnan/Lingnan group, ea-?), which has not run; it must carry the gain |
| pyu-city-states 849 loss | pagan-kingdom (gain) | exception | pagan-kingdom.json not written yet (se-01); its Cliopatria row starts 850, so it must start in December 849 to carry the gain |
| pyu-city-states 860 loss | pagan-kingdom (gain) | exception | pagan-kingdom.json not written yet (group se-01 has not run); it must carry the gain |
| pyu-city-states 960 loss | pagan-kingdom (gain) | exception | pagan-kingdom.json not written yet (group se-01 has not run); it must carry the gain |
| pyu-city-states 1044 dissolve | pagan-kingdom (gain) | exception | pagan-kingdom.json not written yet (group se-01 has not run); it must carry the gain |
| funan 220 vassal_start | isthmus polities (Dunsun and others) (vassal_start) | exception | isthmus polities (Dunsun and others): no polity row; listed in the author's counterparts_needing_dossiers |
| funan 550 loss | chenla (gain) | exception | chenla.json not written yet (se-01); Chenla's Cliopatria row starts 555 and its page gives 'Vassal of Funan: 550', 'Independence: 627': the two dossiers must agree on loss vs vassalage |
| funan 627 vassal_end | isthmus polities (Dunsun and others) (vassal_end) | exception | isthmus polities (Dunsun and others): no polity row; listed in the author's counterparts_needing_dossiers |
| funan 627 dissolve | chenla (gain) | exception | chenla.json not written yet (group se-01 has not run); it must carry the gain |
| early-ly-dynasty 545 occupation_start | liang-dynasty (occupation_start) | exception | liang-dynasty.json not written yet (group ea-03 has not run); it must carry the occupation_start |
| early-ly-dynasty 550 occupation_end | liang-dynasty (occupation_end) | exception | liang-dynasty.json not written yet (group ea-03 has not run); it must carry the occupation_end |
| early-ly-dynasty 602 dissolve | sui-dynasty (gain) | exception | sui-dynasty.json not written yet (group ea-03 has not run); it must carry the gain |
| au-lac -179 dissolve | nanyue (gain) | exception | nanyue.json not written yet; owning group not in the author's context table (Yunnan/Lingnan group, ea-?), which has not run; it must carry the gain |
| trung-sisters 43 loss | han-dynasty (gain) | exception | han-dynasty.json not written yet (ea-02); as government side of a rebel state it must carry the contest 42–43 and the recovery of Jiaozhi, Jiuzhen and Rinan in 43 |
| trung-sisters 43 loss | han-dynasty (gain) | exception | han-dynasty.json not written yet (ea-02); as government side of a rebel state it must carry the contest 42–43 and the recovery of Jiaozhi, Jiuzhen and Rinan in 43 |
| trung-sisters 43 dissolve | han-dynasty (gain) | exception | han-dynasty.json not written yet (ea-02); as government side of a rebel state it must carry the contest 42–43 and the recovery of Jiaozhi, Jiuzhen and Rinan in 43 |

## Gazetteer names needed

- Beikthano (place, pyu-city-states)
- Halin (place, pyu-city-states)

## Counterparts needing dossiers

- Văn Lang (Hùng kings, Lạc Việt): `van-lang` [-700, -258]
- Nam Cương (Âu Việt realm of Thục Phán): `nam-cuong` [None, -258]
- Isthmus polities tributary to Funan (Dunsun and others): `dunsun` [100, 627]
- Mon city-states of lower Burma (Michen, Thaton): `mon-city-states` [825, 1057]

## Problems

- No neighbour dossier exists yet: none of the 23 Context polities of the author's brief section 6 (nor nanzhao, nanyue, yuan-dynasty, nguyen-dynasty) has a file in history/polities/, so every cross-check is an exception (counterpart's group has not run), except tang-dynasty, checked against _example-tang-dynasty.json, which lacks the 803/809 Nghệ An events.
- Reviewer applied two small fixes to history/polities/champa.json (446 occupation place; 875 quotes), re-validated with 0 errors and 0 warnings and read back; no other dossier edited.
- No page failed to load for the reviewer. The author's Fan Shiman and 1069-war pages were not retried.
