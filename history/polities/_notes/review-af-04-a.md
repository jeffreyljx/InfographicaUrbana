# Review of batch af-04-a (Forest states, part a)

Reviewer, 2026-10-19. Machine copy: history/notes/phase-b/reviews/af-04-a.json. Validator (--resolve): 0 errors in all five dossiers; warnings are gazetteer misses for fort towns and slugs of unwritten counterparts.

## Verdicts

### dutch-gold-coast: thin
- Area: page None km2 (year None), Cliopatria 15701 km2, ratio None; No area on the page; the author says so in notes and K2/K11.
- APPLIED `/notes`: Note (b) said the Dutch tribute to the Ashanti is carried in the Ashanti dossier as vassal events with this state as counterpart; the Ashanti ledger has no dutch-gold-coast event and the batch notes say it is deliberately not a vassal event. Evidence: ashanti-empire.json ledger (23 events) has no counterpart dutch-gold-coast; _notes/af-04-a.md 'Not done on purpose': 'The Dutch tribute to the Ashanti for Elmina ... is not a vassal event'. Fix: Sentence rewritten to say it is not a vassal event in either dossier.
- TO DO `/ledger (missing, between /ledger/9 and /ledger/11)`: No Dutch events for Carlsborg (Cape Coast) 1659-1664, although danish-gold-coast /ledger/1 records its 1659 sale to the Dutch; the Danish loss has no mirror. Evidence: Danish Gold Coast page (opened by the author, in this dossier's sources): Samuel Schmidt 'In 1659 ... sold it and all Danish stations to the Dutch'; Carlsborg handed to the Swedish Africa Company on 10 December 1660; Swedish Gold Coast page: Carlsborg Dutch 1663, English 9 May 1664. Not blocking: Cape Coast lies inside the 12 km circles of Elmina and Moree, so the drawn land does not change. Fix: Add 1659 gain (counterpart danish-gold-coast, place Cape Coast km 12, source Danish_Gold_Coast), 1660-12 loss (swedish-empire), 1663 gain and 1664-05 loss (english-colonial-empire), source Swedish_Gold_Coast; also mirror the Danish 1660/1661 Christiansborg events (Osu Castle page: 'In 1660, control passed to the Netherlands but it was soon lost to Denmark-Norway') or say in the note why not.
- TO DO `/ledger/13`: Counterpart swedish-empire for the 1665 Dutch gain of Fort Witsen is a guess: the note itself says how it reached the Dutch is on neither page, and the Swedish page has it 'ceded 1658'. Evidence: Swedish Gold Coast page (author's source note): Fort Witsen 'founded 1653, ceded 1658'; Dutch Gold Coast page table: Takoradi, Fort Witsen, 1665, 'Originally built by the Swedes', no seller named. Fix: Use counterpart 'unknown holder of Fort Witsen 1658-1665' (plain name) or the 1658 recipient if a page names it; keep year 1665, confidence 2.
- Thin `/keyframe_review/12`: The 1788 step (+3,000 km2, 13 cells) has no dated event; nine cells round Sekondi, Moree and Apam are kept unverified. Try: https://en.wikipedia.org/wiki/Fort_Orange_(Ghana)
- Thin `/ledger/1, /ledger/5, /ledger/9`: Cape Coast and Anomabu 1637-1652 at confidence 1: who held them before and after. Try: https://en.wikipedia.org/wiki/Cape_Coast_Castle
- Thin `/ledger/29, /ledger/30`: Senya Beraku lost to the Akyem 1811 and regained 1816, confidence 1. Try: https://en.wikipedia.org/wiki/Fort_Goede_Hoop
- Thin `/ledger (Carlsborg 1659-1664)`: The mirror events listed under fixes. Try: https://en.wikipedia.org/wiki/Swedish_Gold_Coast
- Spot checks: /ledger/3 confirmed; /ledger/12 confirmed; /ledger/21 confirmed; /ledger/31 confirmed; /ledger/32 confirmed; /ledger/35 confirmed

### danish-gold-coast: fail
- Area: page 10000 km2 (year None), Cliopatria 976 km2, ratio 0.1; 'over 10,000 square kilometres' of influence in the text, no year; acknowledged in K1 (influence, not enclaves).
- TO DO `/keyframe_review/3/correction`: The correction of the 1744 keyframe (span 1744-1848) adds Keta, Ada and Teshie, so forts founded in 1784 and 1787 are drawn from 1744, 40 years early, and the 1784/1787 gains (/ledger/12, /ledger/13) add nothing. Evidence: Danish Gold Coast page: Fort Prinsensten (Keta) and Fort Kongensten (Ada) founded 1784, Fort Augustaborg (Teshie) 1787. A correction describes the shape at the keyframe; three 12 km circles (about 1,350 km2) roughly double the 718 km2 shape for 1744-1783. Blocking: wrong shape correction. Fix: Make K3 the 1744 shape unchanged (verdict ok, note why) and let /ledger/12 and /ledger/13 add the forts; or add a new keyframe danish-gold-coast_1784 (from 1784, to 1848) carrying the union. K4 (1849) stays as it is.
- TO DO `/ledger/14/counterpart and /identity/successors/0/slug`: british-gold-coast is the 1850 successor here, while the Dutch dossier uses british-colonial-empire for the British coast of 1868 and the batch notes say british-gold-coast starts in 1873. Evidence: dutch-gold-coast /ledger/31-32 counterpart british-colonial-empire; _notes/af-04-a.md: 'british-gold-coast starts 1873'. The Danish page does say the forts were 'incorporated into the British Gold Coast'. Fix: Use one slug for British coastal land before 1873 in both dossiers (british-colonial-empire, unless af-08 starts british-gold-coast before 1850); not blocking.
- Thin `/keyframe_review/3`: The 1744 contraction (1,349 to 718 km2, cells near Ningo) has no event. Try: https://en.wikipedia.org/wiki/Akwamu
- Thin `/ledger/3, /ledger/4`: Christiansborg to the Dutch 1660 and back 1661, confidence 1 (Osu page vs Swedish page 1663). Try: https://en.wikipedia.org/wiki/Osu_Castle
- Spot checks: /ledger/1 confirmed; /ledger/2 confirmed; /ledger/6 confirmed; /ledger/8 confirmed; /ledger/9 confirmed; /ledger/10 confirmed; /ledger/14 confirmed

### ashanti-empire: thin
- Area: page 250000 km2 (year None), Cliopatria 186800 km2, ratio 0.75; 'over 250,000 square kilometers' in the text, no year; compared with the 1762 peak in K1.
- TO DO `/ledger/7, /ledger/10`: Akyem (Eastern region) is gained twice, 1742 and 1765, with no loss or revolt between. Evidence: Opoku Ware I page: 'Two years later [after 1740], the Ashanti incorporated the Akyem states of Abuakwa and Kotoku'; the Osei Kwadwo page has Akyem Abuakwa conquered in June 1765, so it broke away in between. Fix: Add the break-away (a loss of Akyem Abuakwa, year from a page, confidence 1 if undated) or turn 1742 into vassal_start and 1765 into the gain; not blocking (the land is Ashanti in both readings).
- TO DO `/keyframe_review/9/correction`: The Fomena losses (Central, Eastern, Brong Ahafo, Obuasi) are removed for the whole 1873-1884 keyframe, so 1873 is drawn without them although the treaty is of 13 February 1874; /ledger/16-17 then remove nothing. Evidence: Treaty of Fomena page: signed 13 February 1874; Kumasi taken 4 February 1874. One year early; not blocking. Fix: K9 correction minus Central only (the 1831 Pra border) and let /ledger/16-17 do the 1874 losses, or add a new keyframe 1874-1884.
- TO DO `/ledger/17/region`: admin1 Brong Ahafo also covers Ahafo, which the Ashanti took from Aowin in 1719-1722 (/ledger/1) and kept; the Fomena page names only 'Brong'. Evidence: Treaty of Fomena page: 'This also resulted in the independence of the states of Brong, Gonja, and Dagomba'; Opoku Ware I page: Ahafo claimed from Aowin 1719-1722. Fix: Narrow the region to the Bono (Techiman) and Banda country, or say in the note that Ahafo is wrongly included; not blocking.
- Thin `/ledger/3, /ledger/20`: Wassa as tributary 1726-1874, confidence 1: the Opoku Ware page says only 'In 1726, Ashanti invaded Wassa'. Try: https://en.wikipedia.org/wiki/Wassa_people
- Thin `/ledger/21`: Gyaman's release in 1895, confidence 1. Try: https://en.wikipedia.org/wiki/Gyaman
- Thin `/keyframe_review/12`: The 1895 loss of the Ivory Coast part and the post-1874 break-up (Dwaben, Wassa, Gyaman) are undated. Try: https://en.wikipedia.org/wiki/Mensa_Bonsu
- Thin `/keyframe_review/4, /keyframe_review/5`: Togo cells removed on an undated 'neutral zone' sentence. Try: https://en.wikipedia.org/wiki/Osei_Kwadwo
- Spot checks: /ledger/0 confirmed; /ledger/1 confirmed; /ledger/7 confirmed; /ledger/9 confirmed; /ledger/13 confirmed; /ledger/15 confirmed; /ledger/16 confirmed; /ledger/17 confirmed; /ledger/22 confirmed

### oyo-empire: thin
- Area: page 150000 km2 (year 1680), Cliopatria 29176 km2, ratio 0.19; Acknowledged in K3 and resolved: infobox judged too high for 1680.
- APPLIED `/ledger/14/confidence`: Dahomey's release in 1823 was at confidence 3 though the cited Oyo page does not date the defeat that ended the hegemony and the Dahomey page disagrees with itself (1823 infobox, 1827 text). Evidence: Oyo Empire page: 'In 1823, Dahomey was reported to have raided villages that were under the protection of Oyo' and, without a year, 'The Oyo army was decisively defeated, ending Oyo's hegemony over Dahomey'. Fix: Confidence lowered to 2 with a reviewer note in the event note.
- Thin `/ledger/5, /ledger/8, /ledger/11, /ledger/12`: The Cliopatria steps of 1670, 1734, 1752 and 1769 are confidence-1 placeholders with no dating page. Try: https://en.wikipedia.org/wiki/Alaafin_of_Oyo
- Thin `/ledger/0, /ledger/3`: The 1300 founding (page: 'only estimated') and the 1609 return from exile (undated Ofinran), confidence 1. Try: https://en.wikipedia.org/wiki/Old_Oyo
- Thin `/keyframe_review/8`: The 1769 shape overlaps the Ashanti 1769 shape between 0.1 and 0.7 E and reaches the Volta coast; unresolved. Try: https://en.wikipedia.org/wiki/Dahomey
- Spot checks: /ledger/6 confirmed; /ledger/7 confirmed; /ledger/9 confirmed; /ledger/13 confirmed; /ledger/14 mis-dated: year not on the cited page for the defeat; confidence lowered to 2; /ledger/15 confirmed

### freetown-colony: pass
- Area: page 82.48 km2 (year None), Cliopatria 3430 km2, ratio 41.6; The infobox figure is the modern municipality; the author says it is no comparison and calls the shape unverified.
- Thin `/ledger/1`: The 1788 purchase from King Tom and regent Naimbana is undated on both pages (confidence 1); the 3,430 km2 extent is unverified. Try: https://en.wikipedia.org/wiki/Sierra_Leone_Company
- Spot checks: /ledger/0 confirmed; /ledger/2 confirmed; /ledger/3 confirmed; /ledger/4 confirmed; /ledger/6 confirmed

## Cross-dossier matrix

- dutch-gold-coast 1637 gain portuguese-empire -> portuguese-empire None None: missing. portuguese-empire has no 1637 loss of Elmina (its Gold Coast events are 1481 gain and 1642 loss).
- dutch-gold-coast 1640 gain portuguese-empire -> portuguese-empire 1642 loss: mismatch. Shama 1640 here; the Portuguese dossier folds it into a 1642 loss of 'the rest of the Portuguese Gold Coast' with counterpart dutch-republic, not dutch-gold-coast.
- dutch-gold-coast 1642 gain portuguese-empire -> portuguese-empire 1642 loss: mismatch. Year and land agree (Axim-Sekondi); the Portuguese side names dutch-republic as counterpart.
- dutch-gold-coast 1647 gain english-colonial-empire -> english-colonial-empire None None: missing. Egya: English post built and lost in 1647; no event in the English dossier.
- dutch-gold-coast 1664 loss english-colonial-empire -> english-colonial-empire None None: missing. Axim and Egya to the English 1664; English dossier has no Gold Coast event 1641-1672.
- dutch-gold-coast 1665 gain english-colonial-empire -> english-colonial-empire None None: missing. De Ruyter takes Cormantin and Axim; no English loss.
- dutch-gold-coast 1656 gain swedish-empire -> swedish-empire None None: exception. swedish-empire (eu-14) not written yet; swedish-gold-coast listed in counterparts_needing_dossiers.
- dutch-gold-coast 1665 gain swedish-empire -> swedish-empire None None: exception. Not written yet; counterpart itself doubtful (Fort Witsen 'ceded 1658').
- dutch-gold-coast 1687 gain brandenburg-prussia -> brandenburg-prussia None None: exception. brandenburg-prussia (eu-09) not written yet; also 1698, 1711, 1712, 1721 events.
- dutch-gold-coast 1782 loss british-colonial-empire -> british-colonial-empire None None: exception. eu-11 not run; also 1782 gain, 1784 gain, 1785 loss, 1868 loss and gain.
- dutch-gold-coast 1868 contest_start fante-confederacy -> fante-confederacy None None: exception. Listed in counterparts_needing_dossiers.
- dutch-gold-coast 1872 dissolve british-gold-coast -> british-gold-coast None None: exception. af-08 not run.
- danish-gold-coast 1659 loss dutch-gold-coast -> dutch-gold-coast None None: missing. Same batch: the Dutch ledger has no Carlsborg/Cape Coast gain in 1659 (Danish page: Schmidt sold it 'and all Danish stations to the Dutch').
- danish-gold-coast 1660 loss dutch-gold-coast -> dutch-gold-coast None None: missing. Same batch, confidence 1: Christiansborg to the Dutch 1660 (Osu page), no Dutch event.
- danish-gold-coast 1661 gain dutch-gold-coast -> dutch-gold-coast None None: missing. Same batch, confidence 1: no Dutch loss.
- danish-gold-coast 1679 loss portuguese-empire -> portuguese-empire None None: missing. Christiansborg sold to the Portuguese (Danish page: 1680-1682); no Portuguese gain.
- danish-gold-coast 1683 gain portuguese-empire -> portuguese-empire None None: missing. Bought back February 1683; no Portuguese loss.
- danish-gold-coast 1685 loss english-colonial-empire -> english-colonial-empire None None: missing. Frederiksborg bought by the English (Fort Royal); no English gain.
- danish-gold-coast 1658 found swedish-empire -> swedish-empire None None: exception. eu-14 not run.
- danish-gold-coast 1693 loss akwamu -> akwamu None None: exception. Listed in counterparts_needing_dossiers (af-04-x); also 1694 gain.
- danish-gold-coast 1850 dissolve british-gold-coast -> british-gold-coast None None: exception. af-08 not run; slug inconsistent with the Dutch 1868 events (british-colonial-empire).
- ashanti-empire 1701 found denkyira -> denkyira None None: exception. Listed (af-04-x).
- ashanti-empire 1873 contest_start british-gold-coast -> british-gold-coast None None: exception. af-08 not run; also 1874 contest_end and loss, 1896 dissolve.
- ashanti-empire 1722 gain Aowin -> Aowin None None: exception. Plain-name counterparts (Aowin, Bono, Wassa, Gyaman, Gonja, Banda, Akyem, Ga-Adangbe, Dagbon, Fante, Brong): no dossiers expected; Wassa, Gyaman, Gonja, Dagbon, Bono, Akyem listed.
- oyo-empire 1535 loss nupe-kingdom -> nupe-kingdom None None: missing. nupe-kingdom (af-03-x, written) has only found 1531, loss and dissolve 1835: no 1535 gain of Oyo.
- oyo-empire 1609 gain nupe-kingdom -> nupe-kingdom None None: missing. No Nupe loss; Oyo side is confidence 1 (bridge year).
- oyo-empire 1817 loss ilorin-emirate -> sokoto-caliphate 1824 gain: mismatch. Oyo: Ilorin secedes under Afonja 1817 (Oyo page). sokoto-caliphate /ledger/12 has a 1824 gain of Ilorin with counterpart oyo-empire; the Oyo page says Ilorin joined Sokoto in 1823 after Afonja's death, so the Sokoto event should name ilorin-emirate (or Afonja) and 1823. ilorin-emirate has no dossier and is listed.
- oyo-empire 1835 dissolve ilorin-emirate -> sokoto-caliphate 1836 gain: matched. Within a year; Sokoto's 1836 gain of the old Oyo core names oyo-empire, Oyo names ilorin-emirate (an emirate of Sokoto).
- oyo-empire 1748 vassal_start dahomey -> dahomey None None: exception. Listed (af-04-x); also 1728 contest, 1823 vassal_end.
- oyo-empire 1300 found ife-empire -> ife-empire None None: exception. Listed (af-04-x).
- freetown-colony 1808 dissolve british-colonial-empire -> british-colonial-empire None None: exception. eu-11 not run; 1787-1791 counterparts are the Koya Temne (plain name).

## Gazetteer names needed

Ada Akwidaa Anomabu Apam Axim Beyin Butre Cormantin Dixcove Egya Elmina Igboho Keta Komenda Moree Ningo Princess Town Senya Beraku Shama Takoradi Teshie

## Problems

- ilorin-emirate: the author assigns it to af-03, which has already run (af-03-a/b/x notes exist) without writing it; route to af-04-x or a gap-filler.
- Missing mirrors in neighbour dossiers already written by other groups: english-colonial-empire (am-07) has no Gold Coast events for 1647, 1664, 1665 or 1685; portuguese-empire has no 1637 Elmina loss, no 1679/80-1683 Christiansborg episode, and names dutch-republic for the 1642 Gold Coast loss; nupe-kingdom (af-03-x) lacks the 1535 gain and 1609 loss of Oyo; sokoto-caliphate /ledger/12 dates the gain of Ilorin 1824 from oyo-empire.
- Dutch Gold Coast page contradicts itself on the Brandenburg purchase (body 1717, table 1721); the Brandenburger page gives 1721, so /ledger/21 stands.
- In counterparts_needing_dossiers the years for Denkyira, Akwamu, Dahomey and Ife are mine for routing, not checked on a page.
- Reviewer applied two small fixes (oyo-empire /ledger/14 confidence 3 to 2; dutch-gold-coast /notes sentence (b)); both files re-validated with 0 errors.
- No page failed to load.
