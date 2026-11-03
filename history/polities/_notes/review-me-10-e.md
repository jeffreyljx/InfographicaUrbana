# Review of batch me-10-e (2026-10-25)

Reviewer: adversarial review, Phase B. Dossiers: qajar-dynasty, persian-socialist-soviet-republic, muhammad-ali-dynasty, imamate-of-yemen, qatar-dynasty. All five validated with 0 errors and 0 warnings under `--resolve` before and after the reviewer's fixes. Machine copy: `history/notes/phase-b/reviews/me-10-e.json`.

| slug | verdict | reviewer fixes applied | open items |
| --- | --- | --- | --- |
| qajar-dynasty | fix | Herat counterpart; Gulistan region | Herat type (gain vs occupation); thin list |
| persian-socialist-soviet-republic | fix | coup/treaty order in /ledger/2 note | none |
| muhammad-ali-dynasty | fail | 1820 Nubia counterpart to nobody | Ottoman vassal mirror; Kordofan counterpart; Greek war, Crete and Morea; Tihama 1833 mirror; notes |
| imamate-of-yemen | thin | none | 1814 founding, 1815 growth, Tihama 1840-48, 1818 mirror |
| qatar-dynasty | fix | contest split 1851/1867; misquote corrected | 1820 founding at confidence 1 |

## qajar-dynasty: fix (fixed by the reviewer)

Spot checks (all confirmed): /ledger/13 Ganja 15 January 1804, /ledger/16 Baku 8 February 1806, /ledger/17 Gulistan (infobox cession; war end 24 October 1813), /ledger/20 Tabriz 24 October 1827, /ledger/22 Turkmenchay 2 February 1828 ceding Erivan and Nakhichevan, /ledger/3 Kerman 'fell on 24 October' (year 1794 from the lead), /ledger/11 Kartli-Kakheti 12 September 1801, /ledger/24 and /ledger/26 Herat 25 October 1856 and Treaty of Paris 4 March 1857, /ledger/28-30 Tabriz 1909, Urmia and Khoi 1910, Urmia 4 January 1915, /ledger/45 Anzali and Gilan May 1920.

Area: Qajar Iran infobox 1,300,000 km2 (1873) against Cliopatria 1873 1,624,460 km2, ratio 1.25; acknowledged in /keyframe_review/16. The 1895 Indonesian polygon and the 1915-1921 cut-outs are caught and corrected.

Applied:
- /ledger/24 and /ledger/26: counterpart emirate-of-afghanistan changed to principality-of-herat. The Anglo-Persian War page says Herat had 'declared itself independent' under 'its own rebellious emir'; emirate-of-afghanistan takes Herat from principality-of-herat only on 27 May 1863. principality-of-herat added to /wars/4/belligerents.
- /ledger/17: the Gulistan loss covered all of Azerbaijan, Nakhchivan included, which /ledger/22 loses again in 1828. Region now Azerbaijan minus admin1 Nakhchivan.

Open (not blocking):
- principality-of-herat records Herat 1856-57 as an occupation, this dossier as gain/loss. Pick one; if occupation, change both events and mark /keyframe_review/11 adjust.
- Thin: /ledger/8 and /ledger/10 (1796 and 1797 khanates at confidence 1; the Agha Mohammad Khan page puts Ganja's submission in 1795 and has the Russians occupying Baku in 1796); /ledger/21, /ledger/33, /ledger/46, /ledger/47 (withdrawal dates at confidence 1); no contest for Mohammad Shah's siege of Herat 1837-38 (principality-of-herat has it; try Siege_of_Herat_(1838)); no war entry for the Ottoman-Persian War of 1821-1823; the 1822 shape is 21,863 km2 smaller than 1811-1821 with no event or note.

## persian-socialist-soviet-republic: fix (fixed by the reviewer)

Spot checks on the one page: foundation May 1920 (the intro's June flagged by the author), Rasht, Gilan only, end September 1921: confirmed. Applied: /ledger/2 note said Reza Khan's coup came several days after the treaty; the page has it 'several days beforehand'. Now 'before'. No infobox area.

## muhammad-ali-dynasty: fail (back to the author)

Spot checks: /ledger/0 (17 May 1805), /ledger/3 (July 1820, 'Nubia at once submitted'), /ledger/4 (Sennar without a battle, Kordofan after a hard fight), /ledger/6 (Acre 27 May 1832), /ledger/8 (Kutahya: the cited war page gives only the Syrian provinces; Crete and the Hijaz are on the Muhammad Ali of Egypt page, Adana and Itcheli on the History page, 14 May 1833), /ledger/13 (27 November 1840, Crete and the Hijaz renounced): all confirmed as events.

Applied: /ledger/3 counterpart funj-sultanate changed to nobody. The funj-sultanate dossier (/ledger/15) confines the Funj to the Gezira from 1802, and the Muhammad Ali of Egypt page says Sennar's former territories had broken into rival kingdoms.

To fix (author):
1. No vassal relation to the Ottomans. ottoman-empire /ledger/159 (vassal_start 1805), /ledger/181 (vassal_start 1833-5) and /ledger/185 (vassal_end 1840-11) name this state. Add vassal_start 1805-5 (Egypt, counterpart ottoman-empire) and close it at the end of the dossier; say in the notes how the 1833 gain and 1840 losses relate to the Ottoman vassal events for Syria.
2. /ledger/4 gives Kordofan to funj-sultanate, but sultanate-of-darfur /ledger/6 loses Kordofan to this state on 19 August 1821 and funj-sultanate /ledger/20 loses only Sennar and the Gezira. Split it: Sennar and Gezira from funj-sultanate (1821-6), Kordofan from sultanate-of-darfur (1821-8).
3. /wars/2 (Greek war) has empty zones and does not say no ground changed hands. The dossier's own main page: Muhammad Ali 'was appointed governor of Crete in 1821', which he had 'occupied with a small Egyptian force'; Ibrahim landed in the Morea in March 1825 and was recalled after the convention of early August 1828. Add zones; add occupation_start/occupation_end for the Morea (counterpart first-hellenic-republic); add Crete from 1821 or explain why it starts in 1833. The notes' line that no page dates Egyptian rule of Crete is wrong.
4. No mirror of imamate-of-yemen /ledger/2 (Tihama lost to Egypt in 1833; Yemen Eyalet page). Add the gain and its end.
5. The notes say the Hejaz and Najd of 1811-1833 are Ottoman 'in the Ottoman and Diriyah dossiers'. emirate-of-diriyah /ledger/18-29 gives them to this state; only ottoman-empire takes them. Correct the sentence (the Diriyah/Ottoman disagreement goes to the orchestrator).
6. No area check recorded: the History page has no infobox. Say so in a keyframe note.

Thin: /ledger/11 and /ledger/15 (Najd and Hasa 1840-42 at confidence 1; the Emirate of Nejd page has the re-invasion, Faisal a prisoner 'for the second time in 1838', and the withdrawal after the 1840 Convention, so the dates are probably 1837-38 and 1840-41); /ledger/16 (1865 dissolve, Cliopatria bridge).

## imamate-of-yemen: thin

Spot checks: /ledger/1 (Qasimid page: 'regain them temporarily in 1818'), /ledger/2 (Yemen Eyalet: 1833), /ledger/3 (Yemen Vilayet: Sana'a capital 1872): confirmed. /ledger/0 is honestly at confidence 1. No infobox area on any page, as the notes say.

Gaps for a gap-filler: the 1814 founding (Cliopatria's restart); why the 1815 shape adds Sa'dah, Jizan and Najran; who held the Tihama in 1840-1848; the 1818 regain names emirate-of-diriyah, whose ledger keeps the Tihama until its 1818 dissolve to muhammad-ali-dynasty (the Qasimid page credits the imam himself). Within the 5-page budget (4 used).

## qatar-dynasty: fix (fixed by the reviewer)

Spot checks: /ledger/1 (Al Khor November 1847, Fuwayrit 17 November), /ledger/2 (Najd's 'temporary dominion over Qatar', June 1851), /ledger/3 (25 July 1851, 'abstain from interference in Qatari affairs'), the 1872 dissolve (January 1872 province in Najd): confirmed.

Area: Qatar infobox 11,581 km2 (modern) against Cliopatria 1820 24,587 km2, ratio 2.12. Acknowledged and resolved in /keyframe_review/0 (Saudi coast and Ras al-Khaimah patch dropped).

Applied:
- The house-of-khalifa contest ran from November 1847 to 1868, through the 1851-1867 peace, against the dossier's own wars list. Added contest_end 1851-7 (the peace of 25 July 1851 returned Al Bidda to Ali bin Khalifa) and contest_start 1867 (Doha and Al Wakrah sacked in 1867), both from the History of Qatar page.
- The 1872 dissolve note quoted words not on the page. Now the page's words: 'By January 1872, the Ottomans had incorporated Qatar into their dominion' and 'designated a province in Najd under the control of the sanjak of Najd'. (The Qatar page says the Al Thani 'submitted to Ottoman rule in 1871'.)

Thin: the 1820 founding at confidence 1; Bahraini overlordship 1851-1867 (the May 1861 treaty recognised Qatar 'as a dependent of Bahrain') belongs to house-of-khalifa.

## Cross-dossier matrix (summary; full list in the JSON)

- Matched: qajar 1796 gain / afsharid-iran 1796 dissolve; qajar 1920 loss and 1921 gain / persian-socialist-soviet-republic 1920 gain and 1921 loss; muhammad-ali 1821 gain / funj-sultanate 1821-6 loss (Sennar and the Gezira); imamate-of-yemen 1872 dissolve / ottoman-empire 1873 gain (one year).
- Mismatch: qajar 1856-57 Herat gain/loss against principality-of-herat occupation; sultanate-of-darfur 1821 Kordofan loss against muhammad-ali's funj counterpart; muhammad-ali 1833 gain and 1840 losses against ottoman-empire vassal_start/vassal_end; emirate-of-diriyah losses 1811-1818 to muhammad-ali against muhammad-ali's contest and ottoman-empire's gains; ottoman-empire 1914 vassal_end names muhammad-ali-dynasty (ends 1865; should be khedivate-of-egypt); qatar 1872 dissolve to ottoman-empire against ottoman-empire's 1873 gain of Qatar from emirate-of-nejd.
- Missing: ottoman-empire carries none of the Ottoman occupations of Persia (1915 Urmia and Tabriz, 1916 Kermanshah and Hamadan, 1918 Azerbaijan); ottoman-empire 1805 vassal_start has no mirror in muhammad-ali; muhammad-ali 1832 occupation of Syria has no Ottoman mirror; imamate-of-yemen 1818 gain has no Diriyah loss; imamate-of-yemen 1833 loss has no muhammad-ali gain; principality-of-herat's 1837-38 siege has no qajar contest.
- Exceptions (counterpart not yet written): russian-empire, khanates-of-the-caucasus, zand-dynasty, british-empire, british-colonial-empire, republics-of-the-soviet-union, emirate-of-nejd, house-of-khalifa.
