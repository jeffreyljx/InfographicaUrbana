# Review: batch se-01-i

Adversarial review, 2026-10-19, of kingdom-of-luang-phrabang, vientiane, konbaung-dynasty, thonburi-kingdom, chiangmai and tay-son-dynasty (authors' notes: _notes/se-01-i.md). Validator: 0 errors in all six; the warnings are the expected unknown counterpart slugs and suzerain-only vassal_starts. Every confidence-3 event I opened was on its page with its year; the faults are keyframe/ledger contradictions and wrong counterparts, not invented events.

Verdicts: kingdom-of-luang-phrabang **fix**, vientiane **pass**, konbaung-dynasty **fail**, thonburi-kingdom **fail**, chiangmai **fail**, tay-son-dynasty **fail**.

Reviewer edits (small, checked on the page, re-validated): kingdom-of-luang-phrabang 1885 keyframe set to ok and new keyframe kingdom-of-luang-phrabang_1889; tay-son-dynasty /ledger/26 confidence 1 to 2, /ledger/32 confidence 3 to 2.

## kingdom-of-luang-phrabang: fix

Area: infobox None (None), Cliopatria 160851, ratio None. No area on the page (checked); the dossier says so.

Findings:

- `/keyframe_review/12` (applied by reviewer): The 1885 keyframe's correction removed the Sipsong Chau Tai (Lai Chau, Dien Bien, Son La, Lao Cai, Yen Bai: 77 per cent of that union, about 24 per cent of the shape) for the whole span 1885-1889, contradicting the ledger's own 7 April 1889 loss (/ledger/6) and the keyframe's note ('the shape should lose them in 1889'). Evidence: Sip Song Chau Tai page: 'It became an autonomous part of the French protectorate of Tonkin ... in 1889'; Pavie's treaty with Deo Van Tri 'on 7 April 1889'. Cliopatria's 1885 shape runs 1885-1889. Fix: Reviewer applied: 1885 keyframe set to ok (no correction, note amended); new keyframe kingdom-of-luang-phrabang_1889 (from 1889, to 1889, verdict adjust) carries the removal, source the Sip Song Chau Tai page. Validates with 0 errors.

Gaps for a gap-filler:

- `/ledger/4`: 1793 occupation_start at confidence 1: the ruler list gives 'Siamese occupation (179.. - 2 June 1794)' with the start year garbled; a page that dates the second Siamese (or Vientiane) occupation of Luang Prabang (try https://en.wikipedia.org/wiki/History_of_Laos)
- `/ledger/1`: Muang Phuan vassal_start 1707 has no end, and Xiangkhoang is drawn as direct land in every keyframe while the ledger calls it a tributary; the Kingdom of Vientiane page says Muang Phuan 'seceded' and was later annexed by the Nguyen (undated) (try https://en.wikipedia.org/wiki/Muang_Phuan)
- `/keyframe_review/7`: Bokeo and Louang Namtha restored for 1783-1888 on no page (the Chiang Mai page lists Luang Namtha only as a Chiang Mai claim); Houaphan (Sam Neua) and the Sipsong Chau Tai, drawn as direct land 1709-1888, rest on Cliopatria (the Sip Song Chau Tai page says they paid tribute to several powers) (try https://en.wikipedia.org/wiki/Houaphanh_province)

Spot checks: `/ledger/0` confirmed (Kingdom_of_Luang_Phrabang); `/ledger/1` confirmed (Kingdom_of_Luang_Phrabang); `/ledger/2` confirmed (Kingdom_of_Luang_Phrabang); `/ledger/5` confirmed (Kingdom_of_Luang_Phrabang); `/ledger/6` confirmed (Sip_Song_Chau_Tai)

## vientiane: pass

Area: infobox None (None), Cliopatria 172608, ratio None. No area on the page (checked); the dossier says so.

What I tried: Spot-checked the 1778-1779 Siamese conquest (Thonburi page: invasion ordered 1778, fell March 1779), the December 1826 start and the 1828 annexation; checked the shape against Thonburi/Ayutthaya shapes (no overlap; Nakhon Ratchasima outside); capitals inside the bbox; lan-xang and rattanakosin mirrors. The /ledger/1 split with counterpart kingdom-of-luang-phrabang duplicates lan-xang's own split (lan-xang treats Vientiane as its continuation); harmless, noted in cross_checks.

Gaps for a gap-filler:

- `/keyframe_review/1`: The Khorat Plateau half of the shape (Isan from Nong Khai to Surin, 85 per cent of Surin, and Ubon) is Cliopatria's outline with no page support; Nakhon Ratchasima is correctly outside it (Anouvong 'took Nakhon Ratchasima in January' 1827). A page on the Lao muang of Isan under Vientiane and Champasak would settle the southern edge (try https://en.wikipedia.org/wiki/Isan)

Spot checks: `/ledger/2` confirmed (Thonburi_Kingdom); `/ledger/3` confirmed (Kingdom_of_Vientiane); `/ledger/4` confirmed (Kingdom_of_Vientiane); `/ledger/6` confirmed (Kingdom_of_Vientiane)

## konbaung-dynasty: fail

Area: infobox 794000 (1824), Cliopatria 675755, ratio 1.17. 1824 is in Cliopatria's Burma row (797,916 km2); the last Konbaung shape (1815-1819) is 675,755; the gap (Manipur, Assam) is acknowledged in /keyframe_review/13.

Findings:

- `/ledger/3` (for the author): The 1754 gain names counterpart shan-states, whose dossier and Cliopatria row end in 1563, and draws the whole Shan admin-1 (and /keyframe_review/3-4 draw 100 per cent of it) where the page says only 'Nearer Shan States had been reacquired since 1754'. Evidence: Sino-Burmese War page: 'Nearer Shan States had been reacquired since 1754'; Konbaung-Hanthawaddy War page: homage 'from the nearer sawbwas' as far north as Momeik. Cliopatria's 1757 and 1762 Konbaung shapes cover 65 per cent of Shan; the 1754-1756 corrections cover 100 per cent, so the map drops 35 per cent of Shan in 1757 with no loss. Fix: Region: the nearer Shan states only (the Shan cells of the 1757 shape, e.g. Shan minus the trans-Salween east and the north), in the event and in the 1754 and 1755 keyframe corrections; counterpart 'nobody' or a named sawbwa group with a note (shan-states ended 1563).
- `/keyframe_review/9` (for the author): The 1769 shape (669,238 km2, ok) adds 35 per cent of Shan and 57 per cent of Kachin (about 100,000 km2, 15 per cent of the shape) over the 1765 keyframe with no gain in the ledger; only a contest with the Qing (1765-1769) is recorded. Evidence: Sino-Burmese War page: in 1758-59 Alaungpaya 'sent an expedition to the farther Shan States' to 'reestablish Burmese authority' (present-day northern Kachin and northern and eastern Shan); after the 1769 treaty Burma kept Koshanpye and authority 'as far as Kenghung'. The Konbaung dynasty page says the Shan states 'paid tribute' and 'were never directly controlled', and the burma dossier draws Shan and Kachin as vassal tints from 1820. Fix: Add a 1758 or 1759 event for the farther Shan states and northern Kachin (counterpart qing-dynasty), as vassal_start if they are drawn as tributaries (to agree with burma's 1820 vassal_start of the Shan and Kachin principalities) or as gain if direct; mark the 1757 keyframe adjust (or add a 1759 keyframe) so the shapes and the ledger agree.
- `/keyframe_review/10` (for the author): Chiang Saen (Chiang Rai) is Burmese 1775-1804 on the pages but in no Konbaung keyframe (1775 shape covers 3 per cent of Lanna), and the ledger has no 1804 loss; chiangmai's /ledger/10 gain of Chiang Rai from konbaung-dynasty in 1804 has no mirror, and chiangmai removes Chiang Rai from its 1775 and 1783 shapes as Burmese land, so nobody holds it 1775-1803. Evidence: Burmese-Siamese War (1775-1776) page: the Burmese 'regroup at Chiang Saen' (1775); Kingdom of Chiang Mai page: Bodawpaya's 1785 army came 'from Burmese-held Chiang Saen' and 'Chiang Mai forces under Thammalangka managed to capture Chiang Saen in 1804'. Fix: Mark the 1775, 1785 (new), 1788 and 1794 keyframes adjust with Chiang Rai (Chiang Saen) added through 1803, and add a 1804 loss to chiangmai citing the Kingdom of Chiang Mai page.
- `/ledger` (for the author): No event for the Tavoy episode of 1791-1793: rattanakosin-kingdom /ledger/9 records a 1793 loss of the Tenasserim coast to konbaung-dynasty, which has no mirror here; the wars list also stops at 1786 (no 1787, 1792-1793, 1797-1798, 1802-1804 or 1809-1812 Burmese-Siamese wars, no Manipur campaigns of 1758-1770). Evidence: Cross-check against rattanakosin-kingdom; the chiangmai dossier itself records Burmese contests in 1785-1788 and 1797-1798 that konbaung lacks in its wars. Fix: Open the Burmese-Siamese War (1792-1794) page; record the Siamese hold of Tavoy (occupation or loss) and its 1793 recovery, and add the later wars with their zones (empty where no ground changed hands).
- `/ledger/25` (for the author): The 1767 occupation_start and occupation_end name ayutthaya-kingdom, which dissolves on 7 April 1767; the owner side has no occupation event. Evidence: ayutthaya-kingdom /ledger/66 dissolve 1767-4 (counterpart thonburi-kingdom); Burmese-Siamese War (1765-1767) page: Ayutthaya 'fell to the Burmese on 7 April 1767', Phraya Tak 'reconquered Ayutthaya-Thonburi area in November 1767'. Fix: Either end the occupation with counterpart thonburi-kingdom (whose found event in December 1767 takes the area) or record it as a 1767-4 gain and 1767-11 loss; route the mirror to se-01-e.
- `/ledger/40` (for the author): The 1819 dissolve (confidence 1) is a Cliopatria row boundary, not an end: the page has the dynasty 'from 1752 to 1885' and 'Annexed into British Raj: 29 November 1885'. Evidence: Konbaung dynasty page infobox and lead. burma /ledger/0 founds 1820 with counterpart konbaung-dynasty, so the two dossiers agree with each other. Fix: No change by the author unless the orchestrator merges the rows; give konbaung-dynasty and burma one colour and family (the author asked for this).

Gaps for a gap-filler:

- `/identity/rulers`: No ruler strip (Alaungpaya, Naungdawgyi, Hsinbyushin, Singu, Phaungka, Bodawpaya) (try https://en.wikipedia.org/wiki/List_of_Burmese_monarchs)
- `/ledger/38`: Manipur (1814) and Assam (1817) are 'acquired' on the page but were puppet rulers; Burma held only part of Assam; confidence 2 is honest, a page could make them vassal_start (try https://en.wikipedia.org/wiki/Burmese_invasions_of_Assam)

Spot checks: `/ledger/0` confirmed (Konbaung_dynasty); `/ledger/9` confirmed (Konbaung–Hanthawaddy_War); `/ledger/7` confirmed (Konbaung–Hanthawaddy_War); `/ledger/16` confirmed (Burmese–Siamese_War_(1765–1767)); `/ledger/17` confirmed (Burmese–Siamese_War_(1765–1767)); `/ledger/20` confirmed (Burmese–Siamese_War_(1765–1767)); `/ledger/29` confirmed (Burmese–Siamese_War_(1775–1776)); `/ledger/36` confirmed (Konbaung_dynasty); `/ledger/38` confirmed (Konbaung_dynasty)

## thonburi-kingdom: fail

Area: infobox None (None), Cliopatria 360015, ratio None. No area on the page (only a 1780 sphere-of-influence map).

Findings:

- `/keyframe_review/3` (for the author): The 1775 and 1781 keyframes (ok) draw Lampang (58 per cent), Lamphun (77 per cent) and Nan (87 per cent) as direct Thonburi land from 1775, but the ledger has no gain for them: only vassal_start nan (/ledger/9) and vassal_start chiangmai (/ledger/10); konbaung-dynasty's 1775 loss of 'Lanna' names chiangmai as the only counterpart. Nan is a vassal in the ledger and direct land in the shape. Evidence: Thonburi Kingdom page: Chiang Mai seized in January 1775 and 'The princedom of Nan also came under the power of Thonburi in 1775' (a princedom, i.e. tributary). The 1770-1774 keyframe removes exactly these three provinces. Fix: Add a 1775-1 gain from konbaung-dynasty for the Lampang and Lamphun cells of the shape (and ask konbaung to split its 1775 loss between chiangmai and thonburi-kingdom), and either mark the 1775 and 1781 keyframes adjust without Nan (leaving the vassal tint) or turn the Nan vassal_start into a gain.
- `/keyframe_review/1` (for the author): Every keyframe 1769-1782 draws Pattani, Yala and Narathiwat (100, 100 and 93 per cent) as direct land while the ledger records only a tributary relation 1769-1776 (/ledger/2, confidence 2) ended in 1776 (/ledger/12, confidence 1); rattanakosin-kingdom founds in 1782 without the Pattani region and gains it only in 1786, so the Malay north flickers out of Siam at the 1782 seam. Evidence: Thonburi Kingdom page: the sultanates 'sent tributes to Thonburi in 1769'; the dossier's own 1770 keyframe note says they were tributary, not direct land. Fix: Mark the 1769, 1770, 1775 and 1781 keyframes adjust minus Pattani, Yala and Narathiwat (the vassal tint remains for 1769-1776).

Gaps for a gap-filler:

- `/ledger/12`: 1776 vassal_end of Pattani at confidence 1 (the page says only that Pattani 'ignored' Taksin's 1776 request) (try https://en.wikipedia.org/wiki/Pattani_Kingdom)
- `/ledger/16`: 1779 occupation_end of Champasak at confidence 1 (try https://en.wikipedia.org/wiki/Kingdom_of_Champasak)

Spot checks: `/ledger/0` confirmed (Thonburi_Kingdom); `/ledger/1` confirmed (Thonburi_Kingdom); `/ledger/4` confirmed (Thonburi_Kingdom); `/ledger/5` confirmed (Thonburi_Kingdom); `/ledger/15` confirmed (Thonburi_Kingdom)

## chiangmai: fail

Area: infobox None (None), Cliopatria 65306, ratio None. No area on the page (checked).

Findings:

- `/ledger/2` (for the author): The 1777 loss of 'the Chiang Mai basin' to nobody and its 1797 regain (/ledger/6), both confidence 3, have no trace in the keyframes: the 1775, 1783 and 1804 corrections keep the basin (the 60-km disk is 90 per cent inside the corrected shape, about 29 per cent of it) through 1777-1796. Evidence: Kingdom of Chiang Mai page: 'Chiang Mai was abandoned for twenty years from 1777 to 1797'; 'Kawila entered Chiang Mai in March 1797'. The page describes an abandoned city, not land that left the realm; the dossier already records the move of the seat to Lampang (identity.capitals). Fix: Either drop the loss/gain pair and keep the abandonment in the capitals strip and notes (preferred: no other state took the land), or add new keyframes for 1777-1782 and 1783-1796 without the basin.
- `/identity/end` (for the author): The dossier runs to December 1899 while Cliopatria's Rattanakosin shapes already draw Chiang Mai (99 per cent) from 1885; rattanakosin-kingdom /ledger/32 gains the land in 1899, so 1885-1899 is drawn by both. Evidence: Author's own problem note; rattanakosin-kingdom ledger 1899 vassal_end and gain. Fix: Orchestrator to settle: rattanakosin-kingdom's 1885-1898 keyframes should drop the Chiang Mai cells (tint), keeping chiangmai to 1899.

Gaps for a gap-filler:

- `/identity/rulers`: No ruler strip (Kawila 1782/1802-1816, Thammalangka, Kawilorot, Inthawichayanon 1873-1897 and the 1870-1873 gap) (try https://en.wikipedia.org/wiki/Chiang_Mai_monarchs)

Spot checks: `/ledger/1` confirmed (Burmese–Siamese_War_(1775–1776)); `/ledger/2` confirmed (Thonburi_Kingdom); `/ledger/6` confirmed (Kingdom_of_Chiang_Mai); `/ledger/10` confirmed (Kingdom_of_Chiang_Mai); `/ledger/13` confirmed (Kingdom_of_Chiang_Mai); `/ledger/14` confirmed (Kingdom_of_Chiang_Mai)

## tay-son-dynasty: fail

Area: infobox None (None), Cliopatria 213887, ratio None. No area on the page (checked).

Findings:

- `/ledger/22` (for the author): The 1789 gain of Tonkin and the 1791 gain of the northern uplands (/ledger/23) name counterpart le-dynasty, whose dossier and Cliopatria row end in 1571; trinh-lords (Dang Ngoai to 1787) dissolves in 1787 with tay-son-dynasty as counterpart but this ledger has no gain of Tonkin from trinh-lords, and the 1788 keyframe already holds the Red River delta before the 1789 gain. Evidence: le-dynasty identity end 1571; trinh-lords /ledger/16 dissolve 1787 cp tay-son-dynasty; Tay Son dynasty page: 'He marched to the north ... in 1786' and defeated the Trinh, infobox 'Le dynasty collapsed: 3 February 1789'. Fix: Gain Tonkin from trinh-lords in 1786-1788 (matching its 1787 dissolve), keep the 1788-1789 Qing contest, and give the 1791 uplands step counterpart nobody (or trinh-lords) at confidence 1; or ask the orchestrator for a Le restoration dossier (1786-1789) and name it.
- `/keyframe_review/3` (for the author): The 1778 keyframe (Cliopatria 1778-1787) removes Thuan Hoa and Gia Dinh for its whole span; the 1782 keyframe overrides only 1782-1785, so 1786-1787 are drawn without Thuan Hoa (gained 1786, /ledger/14) and without Gia Dinh (held 1782 to September 1788, /ledger/9 and /ledger/18). Evidence: Correction text says '1778-1781' but carries no from/to; Gia Long page: Saigon captured by Nguyen Anh 'on 7 September 1788'. Fix: Add a new keyframe 1786-1787 (the 1778 shape with Thuan Hoa and Gia Dinh) or extend the 1782 keyframe to 1787 and add Thuan Hoa from 1786.
- `/keyframe_review/12` (for the author): The 1801-1802 keyframe keeps Quang Tri and Quang Binh, but /ledger/32 loses them (with Hue) in May 1801. Evidence: Nguyen dynasty page names only Phu Xuan ('He seized the capital (Phu Xuan) on 3 May 1801, and Quang Toan retreated north'). Fix: Make the two agree: narrow /ledger/32 to Thua Thien - Hue, or remove Quang Tri and Quang Binh in the 1801 keyframe.
- `/ledger/32` (applied by reviewer): Confidence 3 with Quang Tri and Quang Binh, which the page does not name. Evidence: Nguyen dynasty page names Phu Xuan only. Fix: Reviewer applied: confidence lowered to 2, note amended.
- `/ledger/26` (applied by reviewer): 1794 loss of Khanh Hoa at confidence 1 ('page silent') although the cited Gia Long page dates it. Evidence: Gia Long page: in 1794 the Nguyen won 'a successful campaign in the Nha Trang region' and built the citadel at Duyen Khanh, which held off a Tay Son siege in May 1794. Fix: Reviewer applied: confidence raised to 2, note amended.

Gaps for a gap-filler:

- `/ledger/2`: 1775 gain of Quang Nam to Khanh Hoa at confidence 1 (Nguyen Nhac page undated) (try https://en.wikipedia.org/wiki/Nguyễn_Nhạc)
- `/ledger/16`: 1787 contest_end with the Trinh at confidence 1 (try https://en.wikipedia.org/wiki/Trịnh_lords)
- `/ledger/23`: 1791 northern uplands (Lang Son, Cao Bang, Ha Giang, Tuyen Quang) at confidence 1, Cliopatria only (try https://en.wikipedia.org/wiki/Quang_Trung)
- `/ledger/27`: 1796 loss of Phu Yen at confidence 1 (try https://en.wikipedia.org/wiki/Gia_Long)
- `/ledger/29`: 1800 regain of Quy Nhon at confidence 1 (Gia Long page: 'quickly lost' after 1799) (try https://en.wikipedia.org/wiki/Gia_Long)
- `/keyframe_review/1`: Central Highlands (Gia Lai, Kon Tum, Dak Lak) in the 1775 shape on no page (try https://en.wikipedia.org/wiki/Central_Highlands_(Vietnam))

Spot checks: `/ledger/6` confirmed (Trịnh–Nguyễn_War); `/ledger/9` confirmed (Quang_Trung); `/ledger/18` confirmed (Gia_Long); `/ledger/22` confirmed (Tây_Sơn_dynasty); `/ledger/28` confirmed (Nguyen_dynasty); `/ledger/32` confirmed for Phu Xuan on 3 May 1801; Quang Tri and Quang Binh not on page (confidence lowered) (Nguyen_dynasty)

## Cross-dossier matrix (non-matched rows)

- kingdom-of-luang-phrabang 1707 vassal_start muang-phuan: **exception**. no dossier; in the author's counterparts_needing_dossiers
- kingdom-of-luang-phrabang 1791 occupation_start rattanakosin-kingdom: **missing**. schema: the occupier records the same event; rattanakosin-kingdom has none (route to se-01-j, already listed in its review)
- kingdom-of-luang-phrabang 1792 occupation_end rattanakosin-kingdom: **missing**. schema: the occupier records the same event; rattanakosin-kingdom has none (route to se-01-j, already listed in its review)
- kingdom-of-luang-phrabang 1793 occupation_start rattanakosin-kingdom: **missing**. schema: the occupier records the same event; rattanakosin-kingdom has none (route to se-01-j, already listed in its review)
- kingdom-of-luang-phrabang 1794 occupation_end rattanakosin-kingdom: **missing**. schema: the occupier records the same event; rattanakosin-kingdom has none (route to se-01-j, already listed in its review)
- kingdom-of-luang-phrabang 1889 loss french-indochina: **exception**. french-indochina owned by se-03, not written yet
- kingdom-of-luang-phrabang 1893 dissolve french-indochina: **exception**. as above; 1894 unclaimed (Cliopatria's French Indochina takes Laos from 1895)
- vientiane 1707 split kingdom-of-luang-phrabang: **mismatch** (mirror kingdom-of-luang-phrabang 1707 found). LP founds from lan-xang, not from vientiane; lan-xang carries the split itself; harmless duplicate, no change required
- konbaung-dynasty 1752 found restored-hanthawaddy-kingdom: **exception**. no dossier; listed; also asked for by se-01-g
- konbaung-dynasty 1753 gain restored-hanthawaddy-kingdom: **exception**. no dossier; listed
- konbaung-dynasty 1754 gain restored-hanthawaddy-kingdom: **exception**. no dossier; listed
- konbaung-dynasty 1755 gain restored-hanthawaddy-kingdom: **exception**. no dossier; listed
- konbaung-dynasty 1756 gain restored-hanthawaddy-kingdom: **exception**. no dossier; listed
- konbaung-dynasty 1757 gain restored-hanthawaddy-kingdom: **exception**. no dossier; listed
- konbaung-dynasty 1754 gain shan-states: **mismatch**. shan-states dossier ends 1563; counterpart must change (see konbaung /ledger/3)
- konbaung-dynasty 1763 loss ayutthaya-kingdom: **missing**. ayutthaya-kingdom has no 1763 regain of Tavoy (page: Udaungza seized Tavoy in late 1763 and 'the coast returned to Siamese rule'); route to se-01-e
- konbaung-dynasty 1763 gain lan-na: **mismatch**. lan-na runs to 1775-1 with no 1763 loss or vassal event; Cliopatria's Lan Na row ends 1761; route to se-01-h
- konbaung-dynasty 1765 vassal_start kingdom-of-luang-phrabang: **exception**. schema: the suzerain records vassal events
- konbaung-dynasty 1765 vassal_start vientiane: **exception**. schema: the suzerain records vassal events
- konbaung-dynasty 1767 occupation_start ayutthaya-kingdom: **mismatch** (mirror ayutthaya-kingdom 1767 dissolve). owner dissolves 1767-4; no occupation mirror; see konbaung /ledger/25
- konbaung-dynasty 1814 gain manipur: **exception**. no dossier; listed
- konbaung-dynasty 1817 gain ahom-kingdom: **exception**. no dossier; listed
- chiangmai 1804 gain konbaung-dynasty: **missing**. konbaung-dynasty has no 1804 loss of Chiang Saen (see konbaung /keyframe_review/10)
- rattanakosin-kingdom 1793 loss konbaung-dynasty: **missing**. konbaung-dynasty has no Tavoy event 1791-1793
- thonburi-kingdom 1768 gain phimai: **exception**. rival regime, no dossier; listed
- thonburi-kingdom 1769 gain nakhon-si-thammarat: **exception**. rival regime, no dossier; listed
- thonburi-kingdom 1770 gain chao-phra-fang: **exception**. rival regime, no dossier; listed
- thonburi-kingdom 1775 vassal_start chiangmai: **exception**. schema: the suzerain records vassal events
- chiangmai 1892 loss british-raj: **exception**. british-raj owned by sa-06, not written yet
- tay-son-dynasty 1778 loss nguyen-dynasty: **mismatch** (mirror nguyen-dynasty 1788 found). nguyen-dynasty starts 1788-9 and nguyen-lords dissolves 1777: Nguyen Anh's Gia Dinh 1778-1782 and 1783-1788 is in no dossier; route to se-01-h/se-01-j (extend nguyen-dynasty back to 1778-1780 or nguyen-lords forward)
- tay-son-dynasty 1782 gain nguyen-dynasty: **mismatch**. as 1778
- trinh-lords 1787 dissolve tay-son-dynasty: **missing**. tay-son-dynasty has no gain of Tonkin from trinh-lords (see tay-son /ledger/22)
- tay-son-dynasty 1789 gain le-dynasty: **mismatch**. le-dynasty ends 1571
- tay-son-dynasty 1791 gain le-dynasty: **mismatch**. le-dynasty ends 1571

Matched: kingdom-of-luang-phrabang 1707 found lan-xang; vientiane 1707 found lan-xang; vientiane 1828 dissolve rattanakosin-kingdom; konbaung-dynasty 1760 gain ayutthaya-kingdom; konbaung-dynasty 1765 gain ayutthaya-kingdom; konbaung-dynasty 1775 loss chiangmai; konbaung-dynasty 1785 gain kingdom-of-mrauk-u; konbaung-dynasty 1819 dissolve burma; thonburi-kingdom 1767 found ayutthaya-kingdom; thonburi-kingdom 1778 occupation_start kingdom-of-champasak; thonburi-kingdom 1779 occupation_end kingdom-of-champasak; thonburi-kingdom 1782 dissolve rattanakosin-kingdom; chiangmai 1775 found lan-na; chiangmai 1775 gain konbaung-dynasty; chiangmai 1899 dissolve rattanakosin-kingdom; tay-son-dynasty 1773 gain nguyen-lords; tay-son-dynasty 1775 gain nguyen-lords; tay-son-dynasty 1777 gain nguyen-lords; tay-son-dynasty 1786 gain trinh-lords; tay-son-dynasty 1788 loss nguyen-dynasty; tay-son-dynasty 1794 loss nguyen-dynasty; tay-son-dynasty 1796 loss nguyen-dynasty; tay-son-dynasty 1799 loss nguyen-dynasty; tay-son-dynasty 1800 gain nguyen-dynasty; tay-son-dynasty 1801 loss nguyen-dynasty; tay-son-dynasty 1802 dissolve nguyen-dynasty.

## Problems

- No page failed to load (12 Wikipedia pages fetched).
- Reviewer brief section 2 says reviewers do not edit dossiers; under the orchestrator's adjustment I applied three small verified edits: kingdom-of-luang-phrabang (1885 keyframe to ok, new kingdom-of-luang-phrabang_1889 keyframe), tay-son-dynasty /ledger/26 confidence 1 to 2 and /ledger/32 confidence 3 to 2. Both files re-validated with 0 errors and were read back after 12 seconds.
- Vassal events are recorded by the suzerain only (schema text for vassal_start); missing vassal mirrors are marked exception, not faults.
- konbaung-dynasty (to 1819) and burma (from 1820) are one state split at a Cliopatria row boundary; the two dossiers agree on the handoff but disagree on the status of the Shan and Kachin lands (direct in konbaung, vassal in burma).
- Chiang Mai 1885-1899 is drawn by both chiangmai and the Rattanakosin keyframes; orchestrator to settle with se-01-j.
- Neighbour dossiers not yet written (counted as exceptions): qing-dynasty (ea-08), british-empire and british-raj (sa-06), tibet (ea-06), panthay-rebellion (ea-08), kelantan and french-indochina (se-03), sultanate-of-kedah, sultanate-of-malacca and sultanate-of-perak (se-02).
