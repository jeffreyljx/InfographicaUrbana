# Review of batch af-04-x (Forest states, additions)

Reviewer, 2026-10-19. 30 new dossiers (no Cliopatria rows). Validator: 30/30 valid, 0 errors before and after the reviewer's edits. Verdicts: pass 13, fix 9, thin 8, fail 0. No fabricated or mis-dated confidence-3 event was found in 130 spot checks; the exceptions are minor and fixed: one quote cited to the wrong page (bono-state 1723 loss) and two notes that called a page silent when it was not (akwamu on the 1694 return of Christiansborg, kingdom-of-lagos on Ashipa 1600-1630).

Verdict meaning in this run: fix = the reviewer made the change in the dossier (applied: true) and re-validated it; findings marked Advisory are non-blocking suggestions (applied: false); thin = valid and honest but a land question is open for a gap-filler (budget 2-5 pages per state).

## benin-empire: fix
- APPLIED `/ledger/5`: Missing mirror of the kingdom-of-lagos tributary tie (Lagos vassal of Benin 1630-1830 in that dossier). Evidence: History of Lagos: "The Oba of Benin appointed him as ruler of Eko"; Ashipa "initiated a payment of tribute that would not be abolished until 1830". The Benin notes said the Lagos tie was on no page opened. Fix: Added vassal_start (1630, c1) and vassal_end (1830, c2) counterpart kingdom-of-lagos, source History_of_Lagos, added to sources.
- APPLIED `/wars/2/to`: British Benin Expedition ran to 1899, outside the life (ends February 1897). Evidence: Benin Expedition of 1897 infobox: 9-18 February 1897; the 1899 Benin Territories Expedition came after the kingdom ended. Fix: Set to 1897 with a note.
- open `/keyframe_review/3/correction`: Advisory (non-blocking): the 1600-1896 stand-in keeps Ondo and Ekiti to 1896, overlapping ibadan-republic K1 (Oyo+Osun+Ekiti, 1860-1892) and the Ekiti Parapo era. Evidence: Benin page: the empire "gradually shrank in size" after Ehengbuda (undated); Ibadan page: an empire "extending over much of northern and eastern Yorubaland" 1860s-1890s. Fix: A gap-filler may drop Ekiti (and the north of Ondo) from Benin by the 19th century.
- thin `/ledger/4`: The post-Ehengbuda shrinking: what was lost and when (confidence 1). (try https://en.wikipedia.org/wiki/Ehengbuda)
- spot checks: /ledger/1 confirmed (Benin_Empire); /ledger/3 confirmed (Esigie); /ledger/4 confirmed (Benin_Empire); /ledger/7 confirmed (Benin_Expedition_of_1897); /ledger/9 confirmed (Benin_Empire)
- area: Infobox has no area figure (map caption only: extent of Benin in 1625); no Cliopatria row.

## dahomey: fix
- APPLIED `/ledger/6`: Dahomey carried no tributary relation to Oyo although the Dahomey page and the oyo-empire dossier (vassal_start dahomey 1748, vassal_end 1823) have it. Evidence: Dahomey page: "Dahomey became a tributary of the Oyo from 1732 until 1823"; infobox "vassal state of the Oyo Empire (1730-1823)"; elsewhere "since 1748". Fix: Added vassal_start (1730, c2) and vassal_end (1823, c2), counterpart oyo-empire, source Dahomey page; the three start years are in the note.
- open `/identity/end`: Advisory (non-blocking): the dossier ends in January 1894 although the infobox has "Disestablished: 1904" (French protectorate 1894-1904). Evidence: Dahomey page: "The kingdom was reduced and made a French protectorate in 1894"; infobox Disestablished 1904. The author explains the choice in notes. Fix: Either keep the 1894 end (as explained) or continue to 1904 as a French vassal once a French dossier exists.
- thin `/ledger/5`: Year of the Whydah exiles' attempt to retake the coast (confidence 1). (try https://en.wikipedia.org/wiki/Kingdom_of_Whydah)
- spot checks: /ledger/0 confirmed (Dahomey); /ledger/1 confirmed (Dahomey); /ledger/2 confirmed (Agaja); /ledger/3 confirmed (Agaja); /ledger/4 confirmed (Agaja); /ledger/7 confirmed (Agaja); /ledger/10 confirmed (Dahomey); /ledger/13 confirmed (First_Franco-Dahomean_War); /ledger/17 confirmed (Dahomey)
- area: infobox 10000 km2 (1700) vs stand-in 9852 km2, ratio 0.99. Stand-in K1 (56 km circle round Abomey, 1620-1723) sized to the infobox 10,000 km2 of 1700; no Cliopatria row.

## ife-empire: pass
- thin `/ledger/1`: Year of the 14th-century expansion (bridged to 1300, confidence 1). (try https://en.wikipedia.org/wiki/Oranmiyan)
- thin `/ledger/2`: Ife page does not call Oyo a vassal; Oyo-Ile inside Ife is a reading (confidence 1). (try https://en.wikipedia.org/wiki/Oyo_Empire)
- spot checks: /ledger/0 confirmed (Ife_Empire); /ledger/1 confirmed (Ife_Empire); /ledger/3 confirmed (Ife_Empire); /ledger/4 confirmed (Ife_Empire); /ledger/2 not on page (honest: confidence 1, note says the page does not call Oyo a tributary) (Ife_Empire)
- area: infobox 52000 km2 (1350) vs stand-in 56000 km2, ratio 1.08. Infobox "Mid 14th century: 52,000 km2"; author's stand-in K1 about 56,000 km2; no Cliopatria row.

## akwamu: fix
- APPLIED `/ledger/6`: Missing 1694 return of Christiansborg to the Danes; the danish-gold-coast dossier has the 1694 gain from akwamu, and the author's note said the page was silent. Evidence: Akwamu page: "The fort was held by Akwamu for about a year, during which trade continued under the Danish flag." Fix: Added loss 1694, counterpart danish-gold-coast, Accra 12 km, confidence 2, source Akwamu page.
- APPLIED `/ledger/10/counterpart`: Counterpart was the string "Akyem and their allies"; akyem-abuakwa now exists and records the 1730 gain from akwamu. Evidence: Akwamu page: "Akyem forces, allied with formerly subordinate and oppressed vassals, invaded" (1730-31); Akyem Abuakwa infobox: "Conquest of Akwamu: 1730". Fix: Counterpart set to akyem-abuakwa, note extended.
- thin `/ledger/0`: Founding year (infobox "16th century"; 1629 is the first map reference). (try https://en.wikipedia.org/wiki/Akwamu)
- thin `/ledger/12`: How and when the independent kingdom ended (infobox 1886 only; confidence 1). (try https://en.wikipedia.org/wiki/Gold_Coast_(British_colony))
- spot checks: /ledger/1 confirmed (Akwamu); /ledger/2 confirmed (Akwamu); /ledger/3 confirmed (Akwamu); /ledger/5 confirmed (Akwamu); /ledger/7 confirmed (Akwamu); /ledger/8 confirmed (Akwamu); /ledger/10 confirmed (Akwamu)
- area: No Cliopatria row and no infobox area on the Akwamu page; nothing to compare (stand-in shapes only).

## denkyira: pass
- thin `/ledger/0`: Start year: the infobox lists ruler spans "?-c. 1632, c. 1632-c. 1637, c. 1637-1695, 1695-1701", so the kingdom existed before c. 1632; 1650 (confidence 1) is probably late. (try https://en.wikipedia.org/wiki/Denkyira)
- spot checks: /ledger/1 confirmed (Denkyira); /ledger/2 confirmed (Denkyira); /ledger/3 confirmed (Battle_of_Feyiase); /ledger/4 confirmed (Denkyira)
- area: No Cliopatria row and no infobox area on the Denkyira page; nothing to compare (stand-in shapes only).

## bono-state: fix
- APPLIED `/ledger/4/source`: The 1723 loss quoted the Bono Manso page ("Bono-Manso was destroyed in 1723 by Opoku Ware I") but cited the Bono State page, which has no such sentence. Evidence: Bono State page has only "Bono was defeated in 1723, ending its independence"; the quoted sentence and the Techiman rump are on the Bono Manso page. Fix: Source set to the Bono Manso page (already in sources), note extended.
- thin `/ledger/0`: Founding year (infobox 11th-13th century, bridged to 1100). (try https://en.wikipedia.org/wiki/Bono_Manso)
- spot checks: /ledger/1 confirmed (Bono_State); /ledger/2 confirmed (Bono_State); /ledger/3 confirmed (Bono_State); /ledger/4 confirmed (on the Bono Manso page, not the Bono State page cited; source corrected) (Bono_Manso); /ledger/5 confirmed (Bono_Manso)
- area: No Cliopatria row and no infobox area on the Bono State page; nothing to compare (stand-in shapes only).

## nri-kingdom: thin
- thin `/ledger/0`: Founding year (9th-century burials only). (try https://en.wikipedia.org/wiki/Eze_Nri)
- thin `/ledger/1`: Extent of the late-16th-century sphere (confidence 1; Igboland stand-in for ritual influence). (try https://en.wikipedia.org/wiki/Nri-Igbo)
- thin `/ledger/2`: What was lost after 1700 and to whom (confidence 1). (try https://en.wikipedia.org/wiki/Eze_Nri)
- spot checks: /ledger/0 confirmed (Nri_Kingdom); /ledger/1 confirmed (Nri_Kingdom); /ledger/2 confirmed (Nri_Kingdom); /ledger/3 confirmed (Nri_Kingdom)
- area: Infobox has no area (caption: area of influence); no Cliopatria row.

## aro-confederacy: pass
- open `/keyframe_review/1/correction`: Advisory (non-blocking): Abia + Igboland (about 40,000 km2, 1800-1902) overlaps nri-kingdom (Awka circle, to 1910) and the niger-coast-protectorate Igboland from 1900. Evidence: Aro page: influence "across much of Eastern Nigeria and parts of neighboring hinterlands of the Benue valleys" - a trade network, not a frontier. Fix: Renderers: treat as soft; a gap-filler may narrow it to the named Aro settlements.
- spot checks: /ledger/0 confirmed (Aro_Confederacy); /ledger/1 confirmed (Aro_Confederacy); /ledger/2 confirmed (Anglo-Aro_War); /ledger/3 confirmed (Anglo-Aro_War); /ledger/4 confirmed (Aro_Confederacy)
- area: No Cliopatria row and no infobox area on the Aro Confederacy page; nothing to compare (stand-in shapes only).

## brandenburger-gold-coast: pass
- thin `/ledger/8`: Holder of Fort Dorothea after 1717 (confidence 1). (try https://en.wikipedia.org/wiki/Fort_Dorothea)
- spot checks: /ledger/0 confirmed (Brandenburger_Gold_Coast); /ledger/1 confirmed (Brandenburger_Gold_Coast); /ledger/2 confirmed (Brandenburger_Gold_Coast); /ledger/5 confirmed (Brandenburger_Gold_Coast); /ledger/6 confirmed (Brandenburger_Gold_Coast); /ledger/7 confirmed (Brandenburger_Gold_Coast); /ledger/9 confirmed (Brandenburger_Gold_Coast)
- area: No Cliopatria row and no infobox area on the Brandenburger Gold Coast page; nothing to compare (stand-in shapes only).

## swedish-gold-coast: pass
- spot checks: /ledger/0 confirmed (Swedish_Gold_Coast); /ledger/4 confirmed (Swedish_Gold_Coast); /ledger/6 confirmed (Swedish_Gold_Coast); /ledger/9 confirmed (Swedish_Gold_Coast); /ledger/10 confirmed (Swedish_Gold_Coast)
- area: No Cliopatria row and no infobox area on the Swedish Gold Coast page; nothing to compare (stand-in shapes only).

## niger-coast-protectorate: fix
- APPLIED `/ledger/1, /ledger/2, /ledger/14`: Losses to this protectorate in bonny-kingdom (1886), kingdom-of-opobo (1887) and nri-kingdom (1911) had no mirror gain. Evidence: Bonny Kingdom page: "In February 1886 a protectorate treaty was concluded between Bonny and Britain"; Opobo rulers table: Jaja I to "September 1887"; Nri page: "until 1911, when an expedition carried out by British colonial troops forced the reigning eze Nri". Fix: Added gains 1886/2 (c3), 1887/9 (c1) and 1911 (c3) with the three pages added to sources.
- open `/keyframe_review/0/correction`: Advisory (non-blocking): the 1884 shape already contains Bonny and Opobo (their own dossiers keep them independent to 1886 and 1887), and the 1906 shape contains Ogun State, where the Egba United Government stays independent to 1914. Evidence: Bonny page (1886 treaty); Abeokuta page: Egba lands "incorporated into the colony of Nigeria by the British" in 1914. Fix: Either carve the Bonny and Opobo circles out of K0 until 1886/1887 and the Abeokuta circle out of K4 until 1914, or leave the overlap to the renderer.
- spot checks: /ledger/0 confirmed (Niger_Coast_Protectorate); /ledger/3 confirmed (Niger_Coast_Protectorate); /ledger/7 confirmed (Southern_Nigeria_Protectorate); /ledger/8 confirmed (Royal_Niger_Company); /ledger/13 confirmed (Lagos_Colony); /ledger/15 confirmed (Southern_Nigeria_Protectorate)
- area: Neither the Niger Coast nor the Southern Nigeria page gives an area; no Cliopatria row (british-africa aggregate, af-08).

## ijebu-kingdom: thin
- thin `/ledger/0`: Founding year ("around the 15th century", bridged to Ife's 1420). (try https://en.wikipedia.org/wiki/Awujale_of_Ijebuland)
- thin `/ledger/3`: Status 1892-1906: this dossier ends the kingdom in 1892 (loss+dissolve to lagos-colony) while lagos-colony holds ijebu-kingdom as a protectorate (vassal_start 1892, vassal_end 1906); the Ijebu infobox names the Southern Nigeria Protectorate as successor and says the kingdom was "later annexed" (undated). Align the two dossiers (vassal to 1906, or a gain in lagos-colony). (try https://en.wikipedia.org/wiki/Ijebu_Ode)
- spot checks: /ledger/0 confirmed (Ijebu_Kingdom); /ledger/1 confirmed (Ijebu_Ode); /ledger/2 confirmed (Ijebu_Kingdom); /ledger/3 confirmed (Ijebu_Kingdom)
- area: No Cliopatria row and no infobox area on the Ijebu Kingdom page; nothing to compare (stand-in shapes only).

## ibadan-republic: thin
- thin `/ledger/1`: The 1860s-1890s empire: the page says "extending over much of northern and eastern Yorubaland" (the region could be confidence 2) but names no town or year; the Ijaye and Kiriji wars are not used. (try https://en.wikipedia.org/wiki/Kiriji_War)
- thin `/ledger/2`: Status 1893-1906: loss+dissolve here vs lagos-colony vassal_start/vassal_end ibadan-republic 1893-1906 ("the Ibadan area became a British Protectorate"); align the two dossiers. (try https://en.wikipedia.org/wiki/Ibadan)
- spot checks: /ledger/0 confirmed (Ibadan); /ledger/1 confirmed (Ibadan); /ledger/2 confirmed (Ibadan); /ledger/3 confirmed (Ibadan)
- area: The Ibadan page gives only the 1952 city area (103.8 km2); no state area; no Cliopatria row.

## lagos-colony: pass
- spot checks: /ledger/0 confirmed (Lagos_Colony); /ledger/1 confirmed (Lagos_Colony); /ledger/2 confirmed (Lagos_Colony); /ledger/5 confirmed (Lagos_Colony); /ledger/6 confirmed (Lagos_Colony); /ledger/12 confirmed (Lagos_Colony)
- area: No Cliopatria row and no infobox area on the Lagos Colony page; nothing to compare (stand-in shapes only).

## royal-niger-company: thin
- thin `/keyframe_review/0/correction`: The chartered sphere: two 50 km circles (Onitsha, Lokoja) are far smaller than the Company's territories; the 1897 Nupe (Bida) campaign and the Igala/Idah treaties are not in the ledger. (try https://en.wikipedia.org/wiki/Bida_Emirate)
- thin `/ledger/2`: Which lands went south (Onitsha is the researcher's reading). (try https://en.wikipedia.org/wiki/Northern_Nigeria_Protectorate)
- spot checks: /ledger/0 confirmed (Royal_Niger_Company); /ledger/1 confirmed (Ilorin); /ledger/2 confirmed (Royal_Niger_Company); /ledger/3 confirmed (Royal_Niger_Company)
- area: No Cliopatria row and no infobox area on the Royal Niger Company page; nothing to compare (stand-in shapes only).

## kingdom-of-allada: pass
- open `/keyframe_review/0/correction`: Advisory (non-blocking): the shapes leave the Whydah coast out from 1200, but the Ardra page says Allada "maintained control of some sea ports such as Offra, Jaquin and Whydah" and the Whydah page has Whydah independent only "in the late 17th century". Evidence: Kingdom of Ardra and Kingdom of Whydah pages as quoted. Fix: A gap-filler may hold Whydah as Allada's vassal (or inside Allada) to the late 17th century.
- thin `/ledger/0`: Founding year (12th or 13th century). (try https://en.wikipedia.org/wiki/Kingdom_of_Ardra)
- spot checks: /ledger/0 confirmed (Kingdom_of_Ardra); /ledger/1 confirmed (Kingdom_of_Ardra); /ledger/3 confirmed (Kingdom_of_Ardra); /ledger/5 confirmed (Kingdom_of_Ardra)
- area: No Cliopatria row and no infobox area on the Kingdom of Ardra page; nothing to compare (stand-in shapes only).

## kingdom-of-whydah: fix
- APPLIED `/ledger/1, /ledger/3`: Missing mirror of akwamu's vassal_start/vassal_end kingdom-of-whydah (1702-1727). Evidence: Akwamu page: "Little Popo was captured in April, followed by the seizure of Whydah in May"; "it remained tributary to Akwamu for over two decades". Fix: Added vassal_start 1702/5 and vassal_end 1727/2, counterpart akwamu, confidence 2; Akwamu page added to sources.
- open `/wars/0/to`: Advisory (non-blocking): the conquest war runs to 1734, past the dissolve in 1727 (the exiles' resistance, matching the dahomey contest 1730-1734). Evidence: Agaja page: "The other Whydah faction was defeated by Agaja in 1734". Fix: Keep, or end the war in 1727 and leave 1730-1734 to the dahomey contest.
- thin `/ledger/0`: Status 1580 to the late 17th century: the page says Whydah "became independent in the late 17th century" (from Allada, by the Ardra page's ports); the dossier draws it independent from 1580. (try https://en.wikipedia.org/wiki/Kingdom_of_Ardra)
- spot checks: /ledger/0 confirmed (Kingdom_of_Whydah); /ledger/2 confirmed (Agaja); /ledger/5 confirmed (Kingdom_of_Whydah)
- area: Infobox has no area; the page gives a coastline of about 16 km in 1700; no Cliopatria row.

## kingdom-of-porto-novo: fix
- APPLIED `/ledger/2, /ledger/3`: Missing mirror of dahomey's vassal_start/vassal_end kingdom-of-porto-novo (1861-1863). Evidence: Dahomey page: "In 1861, the kingdom of Porto-Novo, one of Dahomey's tributaries, was bombarded by the Royal Navy"; French protectorate 1863. Fix: Added vassal_start 1861 and vassal_end 1863, counterpart dahomey, source Dahomey page (already in sources).
- open `/identity/end`: Advisory (non-blocking): the dossier dissolves the kingdom in 1863 at the French protectorate, but the page has it "incorporated into the French colony of Dahomey and its dependencies" in 1883 (the author explains the choice). Evidence: Porto-Novo page as quoted. Fix: Keep (explained) or continue to 1883 as a French vassal once a French dossier exists.
- open `/ledger/1`: Advisory (non-blocking): the 1861 British bombardment is given to lagos-colony, which has no matching contest and was only annexed on 6 August 1861; the page gives no month and says only "the British, who were active in nearby Nigeria". Evidence: Porto-Novo page; Lagos Colony page. Fix: Either add the contest to lagos-colony or use a plain-string counterpart ("British Royal Navy").
- thin `/ledger`: Tribute to Oyo ("Porto-Novo was once a tributary of the Yoruba Oyo Empire", undated) is not in the ledger. (try https://en.wikipedia.org/wiki/Oyo_Empire)
- spot checks: /ledger/0 confirmed (Porto-Novo); /ledger/1 confirmed (Porto-Novo); /ledger/4 confirmed (Porto-Novo); /ledger/5 confirmed (Porto-Novo)
- area: No Cliopatria row and no infobox area on the Porto-Novo page; nothing to compare (stand-in shapes only).

## warri-kingdom: pass
- open `/identity/end`: Advisory (non-blocking): the dossier ends at the 16 July 1884 treaty; the page dates the end of autonomy to the 1894 defeat of Nana Olomu (the author explains the choice). Evidence: Warri page: "led to Nana's defeat by the Royal Navy, ending Warri's autonomy". Fix: Keep (explained) or extend to 1894 as a vassal of the protectorate.
- spot checks: /ledger/0 confirmed (Warri_Kingdom); /ledger/1 confirmed (Warri_Kingdom); /ledger/2 confirmed (Warri_Kingdom)
- area: No Cliopatria row and no infobox area on the Warri Kingdom page; nothing to compare (stand-in shapes only).

## egba-united-government: fix
- APPLIED `/wars/1`: The Adubi War (1918) lay outside the dossier life (1830-1914); validator warning. Evidence: Abeokuta page: the Adubi War, 1918; the dossier ends in 1914. Fix: Removed from wars; it stays in the 1914 dissolve note; a line added to notes.
- open `/wars/0/zones`: Advisory (non-blocking): the Egba-Dahomey wars (1843-1864) have empty zones although the ledger has the 1851 contest at Abeokuta. Evidence: Abeokuta page: 1851 Battle of Abeokuta and 1864. Fix: Put the Abeokuta circle in the zones.
- spot checks: /ledger/0 confirmed (Abeokuta); /ledger/1 confirmed (Abeokuta); /ledger/3 confirmed (Egba_United_Government); /ledger/4 confirmed (Abeokuta)
- area: infobox 6000 km2 (1830) vs stand-in 6082 km2, ratio 1.01. Stand-in 44 km circle fitted to the infobox 6,000 km2 (1830); no Cliopatria row.

## ilorin-emirate: thin
- APPLIED `/ledger/1, /ledger/4`: The emirate's place in the Sokoto Caliphate was missing although the Ilorin page dates it; sokoto-caliphate records a 1824 gain of Ilorin. Evidence: Ilorin page: Abd al-Salam "pledged allegiance to the Sokoto Caliphate in 1823"; Emirate page: "Ilorin became an emirate of the Sokoto Caliphate under the authority of Gwandu". Fix: Added vassal_start 1823 (c3) and vassal_end 1897 (c2), counterpart sokoto-caliphate, source Ilorin page.
- thin `/keyframe_review/0`: The 1835 end of Oyo: oyo-empire dissolves in 1835 to ilorin-emirate (its last shape, 66,305 km2) and sokoto-caliphate gains Oyo-Ile in 1836, but this dossier has no gain; the Emirate page has "Ilorin's forces attacked and burned down Oyo-Ile" (undated) and the Ilorin page the Oyo-Borgu defeat c. 1835 that "marked the end of Oyo". (try https://en.wikipedia.org/wiki/Oyo_Empire)
- spot checks: /ledger/0 confirmed (Ilorin); /ledger/2 confirmed (Ilorin_Emirate); /ledger/3 confirmed (Ilorin); /ledger/5 confirmed (Ilorin)
- area: Only the modern metropolis area (765 km2) on the Ilorin page; no Cliopatria row.

## bonny-kingdom: pass
- spot checks: /ledger/0 confirmed (Bonny_Kingdom); /ledger/1 confirmed (Bonny_Kingdom); /ledger/2 confirmed (Bonny_Kingdom)
- area: No Cliopatria row and no infobox area on the Bonny Kingdom page; nothing to compare (stand-in shapes only).

## kingdom-of-opobo: thin
- thin `/ledger/1`: End of independence: the page has only the change of ruler in September 1887 (confidence 1); Jaja's deportation and the protectorate treaty are not on it. (try https://en.wikipedia.org/wiki/Jaja_of_Opobo)
- spot checks: /ledger/0 confirmed (Opobo); /ledger/1 confirmed as the date of the ruler change only (confidence 1, honest) (Opobo)
- area: No Cliopatria row and no infobox area on the Opobo page; nothing to compare (stand-in shapes only).

## old-calabar: pass
- spot checks: /ledger/0 confirmed (Old_Calabar); /ledger/1 confirmed (Old_Calabar)
- area: No Cliopatria row and no infobox area on the Old Calabar page; nothing to compare (stand-in shapes only).

## igala-kingdom: pass
- thin `/ledger/0`: Founding year ("16th century"). (try https://en.wikipedia.org/wiki/Attah_Igala)
- thin `/ledger/1`: How the kingdom passed to the British (only the rulers heading "Ata who ruled during British occupation" from 1900); whether Idah went to Southern or Northern Nigeria. (try https://en.wikipedia.org/wiki/Idah)
- spot checks: /ledger/0 confirmed (Igala_Kingdom); /ledger/1 confirmed (Igala_Kingdom)
- area: No Cliopatria row and no infobox area on the Igala Kingdom page; nothing to compare (stand-in shapes only).

## sierra-leone-colony-and-protectorate: thin
- thin `/keyframe_review/0/correction`: 1808-1895 is the Freetown peninsula only; the colony's 19th-century additions (Sherbro, Bonthe, Bullom shore, Isles de Los, Koya) are not on the pages opened, and the predecessor freetown-colony's 1796 Cliopatria shape (3,430 km2) is larger. (try https://en.wikipedia.org/wiki/Sherbro_Island)
- spot checks: /ledger/0 confirmed (Colony_of_Sierra_Leone); /ledger/1 confirmed (Sierra_Leone_Protectorate); /ledger/2 confirmed (Colony_of_Sierra_Leone)
- area: Neither the Colony nor the Protectorate page gives an area (map caption 1899 only); no Cliopatria row for these years.

## kingdom-of-lagos: fix
- APPLIED `/ledger/1/note`: The note said the page is silent on the year Ashipa was appointed; the Oba of Lagos list dates Ashipa 1600-1630 ("not crowned"). Evidence: Oba of Lagos page: the list begins with Ashipa (1600-1630), not crowned; Ado (1630-1669) first King of Lagos. Fix: Note corrected; benin-empire now carries the mirror vassal events (1630, 1830).
- thin `/ledger/0`: Start: 1630 (first crowned king) vs Ashipa 1600-1630 vs infobox 1716 vs "16th century"; a gap-filler may move the start (and the Benin tie) to c. 1600. (try https://en.wikipedia.org/wiki/Oba_of_Lagos)
- spot checks: /ledger/0 confirmed (Oba_of_Lagos); /ledger/1 confirmed (History_of_Lagos); /ledger/2 confirmed (History_of_Lagos); /ledger/3 confirmed (History_of_Lagos)
- area: No Cliopatria row and no infobox area on the History of Lagos / Oba of Lagos page; nothing to compare (stand-in shapes only).

## fante-confederacy: pass
- thin `/ledger/2`: End of the contest with the Dutch (confidence 1; the expedition page does not name the Fante). (try https://en.wikipedia.org/wiki/Dutch_Gold_Coast)
- spot checks: /ledger/0 confirmed (Fante_Confederacy); /ledger/1 confirmed (Fante_Confederacy); /ledger/3 confirmed (Fante_Confederacy)
- area: No Cliopatria row and no infobox area on the Fante Confederacy page; nothing to compare (stand-in shapes only).

## gyaman: pass
- thin `/ledger/0`: Founding year ("17th century"). (try https://en.wikipedia.org/wiki/Bondoukou)
- spot checks: /ledger/1 confirmed (Gyaaman); /ledger/2 confirmed (Gyaaman); /ledger/5 confirmed (Gyaaman); /ledger/7 confirmed (year on Gyaaman page; 13 November from Bondoukou page) (Gyaaman); /ledger/10 confirmed (Gyaaman); /ledger/11 confirmed (Gyaaman)
- area: No Cliopatria row and no infobox area on the Gyaaman page; nothing to compare (stand-in shapes only).

## akyem-abuakwa: thin
- thin `/ledger`: Asante period: the ashanti-empire dossier gains Akyem in 1742 and 1765 but this dossier holds Abuakwa independent 1730-1852 (the page is silent; the overlap is acknowledged in notes). (try https://en.wikipedia.org/wiki/Akyem)
- thin `/ledger/0`: Founding year ("at least the 16th century"). (try https://en.wikipedia.org/wiki/Kyebi)
- spot checks: /ledger/0 confirmed (Akyem_Abuakwa); /ledger/1 confirmed (Akyem_Abuakwa); /ledger/2 confirmed (Akyem_Abuakwa)
- area: No Cliopatria row and no infobox area on the Akyem Abuakwa page; nothing to compare (stand-in shapes only).

## Cross-dossier matrix: mismatches and missing mirrors
- dahomey 1730 vassal_start (counterpart oyo-empire) -> oyo-empire 1748 vassal_start: mismatch. Pages disagree: Dahomey infobox 1730, text 1732 and 1748; oyo-empire uses 1748. Reviewer added the Dahomey side. Also contest 1726 (Agaja page, 14 April 1726) here vs oyo-empire 1728.
- ife-empire 1300 vassal_start (counterpart oyo-empire) -> oyo-empire 1300 found: mismatch. oyo-empire founds Oyo-Ile in 1300 with counterpart ife-empire but carries no vassal tie to Ife; this side is confidence 1.
- ife-empire 1420 vassal_end (counterpart oyo-empire) -> oyo-empire None None: mismatch. oyo-empire (af-04-a) has nothing in 1420.
- ife-empire 1420 loss (counterpart oyo-empire) -> oyo-empire None None: mismatch. Ife loses Oyo and Jebba to Oyo in 1420; oyo-empire has no 1420 gain (route to af-04-a).
- swedish-gold-coast 1660 gain (counterpart dutch-gold-coast) -> dutch-gold-coast None None: missing. dutch-gold-coast has no 1660 loss of Carlsborg to the Swedes (Swedish page table: Swedish again 10 December 1660).
- swedish-gold-coast 1663 loss (counterpart dutch-gold-coast) -> dutch-gold-coast 1665 gain: mismatch. dutch-gold-coast has no 1663 gain of Carlsborg; its 1665 gain from swedish-empire is Fort Witsen at Takoradi, which the Swedish page has ceded in 1658 (route to af-04-a).
- ijebu-kingdom 1892 loss (counterpart lagos-colony) -> lagos-colony 1892 vassal_start: mismatch. Same land, different status: loss+dissolve here, protectorate (vassal to 1906) in lagos-colony. Listed as thin for ijebu-kingdom.
- ibadan-republic 1893 loss (counterpart lagos-colony) -> lagos-colony 1893 vassal_start: mismatch. Same land, different status: loss+dissolve here, protectorate (vassal to 1906) in lagos-colony. Listed as thin for ibadan-republic.
- lagos-colony 1892 vassal_start (counterpart ijebu-kingdom) -> ijebu-kingdom 1892 loss: mismatch. See ijebu-kingdom 1892.
- lagos-colony 1893 vassal_start (counterpart ibadan-republic) -> ibadan-republic 1893 loss: mismatch. See ibadan-republic 1893.
- lagos-colony 1906 vassal_end (counterpart ijebu-kingdom) -> None None None: mismatch. The vassal (ijebu-kingdom / ibadan-republic) dissolved in 1892/1893 in its own dossier.
- lagos-colony 1906 vassal_end (counterpart ibadan-republic) -> None None None: mismatch. The vassal (ijebu-kingdom / ibadan-republic) dissolved in 1892/1893 in its own dossier.
- ilorin-emirate 1823 vassal_start (counterpart sokoto-caliphate) -> sokoto-caliphate 1824 gain: mismatch. sokoto-caliphate (af-03) records Ilorin as a gain in 1824, not a vassal; reviewer added the Ilorin side as vassal (Ilorin page: allegiance 1823).
- gyaman 1740 vassal_start (counterpart ashanti-empire) -> ashanti-empire 1732 vassal_start: mismatch. Gyaaman page 1740-1741 vs ashanti-empire 1732 (string counterpart "Gyaman"); flagged by the author.
- gyaman 1817 vassal_end (counterpart ashanti-empire) -> ashanti-empire 1895 vassal_end: mismatch. Gyaaman page: independence c. 1817, reconquest 1818-19, occupation to 1874; ashanti-empire keeps Gyaman a vassal to 1895.
- gyaman 1819 occupation_start (counterpart ashanti-empire) -> ashanti-empire None None: missing. ashanti-empire has no occupation of Gyaman (Gyaaman page: 1819 province under military occupation).
- gyaman 1874 occupation_end (counterpart ashanti-empire) -> ashanti-empire None None: missing. Gyaaman page: autonomy after the 1874 British invasion of Kumasi.
- oyo-empire 1835 dissolve (counterpart ilorin-emirate) -> None None None: missing. oyo-empire hands its last shape (66,305 km2) to ilorin-emirate, which has no gain; sokoto-caliphate gains Oyo-Ile in 1836. Listed as thin for ilorin-emirate.
- ashanti-empire 1742 gain (counterpart Akyem (Abuakwa, Kotoku)) -> akyem-abuakwa None None: missing. akyem-abuakwa has no Asante-period loss (page silent); also 1765 gain. Listed as thin; ashanti-empire should use the slug akyem-abuakwa.
- freetown-colony 1808 dissolve (counterpart british-colonial-empire) -> sierra-leone-colony-and-protectorate 1808 found: mismatch. freetown-colony (af-04-a) should name sierra-leone-colony-and-protectorate as successor.
- kingdom-of-porto-novo 1861 contest_start (counterpart lagos-colony) -> lagos-colony None None: missing. lagos-colony has no Porto-Novo contest; advisory in both.

## Problems and routing
- No page failed to load for the reviewer; Kingdom_of_Lagos and Kingdom_of_Porto-Novo titles were not retried (the authors used sibling pages).
- Reviewer applied small verified fixes in place (re-validated, read back): akwamu, benin-empire, bono-state, dahomey, egba-united-government, ilorin-emirate, kingdom-of-lagos, kingdom-of-porto-novo, kingdom-of-whydah, niger-coast-protectorate; each edit carries "Reviewer af-04-x (2026-10-19)" in its note.
- Route to af-04-a: oyo-empire has no 1420 gain from ife-empire and dates the Dahomey tribute 1748 / contest 1728 (Dahomey page: 1730-1732 / Agaja page 1726); ashanti-empire should use slugs bono-state, gyaman, akyem-abuakwa and has no Gyaman occupation 1819-1874 (Gyaaman page); dutch-gold-coast should use swedish-gold-coast and brandenburger-gold-coast, lacks the 1660 loss and 1663 gain of Carlsborg, and its 1665 Witsen gain contradicts the Swedish page (ceded 1658); freetown-colony successor should be sierra-leone-colony-and-protectorate.
- Route to af-03: sokoto-caliphate records Ilorin as a 1824 gain; ilorin-emirate now records it as a vassal from 1823 (Ilorin page).
- Within this batch, ijebu-kingdom and ibadan-republic end in 1892/1893 with a loss to lagos-colony while lagos-colony holds them as protectorates to 1906; same author, needs one model (listed as thin, not failed).
- Overlapping stand-ins (renderer to decide): benin-empire 1600-1896 vs ibadan-republic 1860-1892 (Ekiti); aro-confederacy (Igboland) vs nri-kingdom and niger-coast-protectorate; niger-coast-protectorate 1884 shape vs bonny-kingdom/kingdom-of-opobo to 1886/1887 and its 1906 shape vs egba-united-government to 1914; akyem-abuakwa vs ashanti-empire 1742-1852.

Gazetteer places still needed: Akwamufie, Akwidaa, Anomabu, Assin Fosu, Beyin, Butre, Elmina, Ilaro, Jebba, Komenda, Princess Town.
