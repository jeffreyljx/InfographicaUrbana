# Review of batch eu-19-f (Caucasus part f), 2026-10-31 brief, run 2026-11-01

Validator: all six dossiers 0 errors before and after the reviewer's edits. Warnings are counterpart slugs without dossiers (transcaucasian-democratic-federative-republic, avar-khanate, and, after the edits, southwest-caucasian-republic and centrocaspian-dictatorship).

Pages opened: Samtskhe-Saatabago; Principality of Svaneti; Agha Mohammad Khan; Persian expedition of 1796; Caucasian Imamate; Caucasian War; Gimry; First Republic of Armenia; Azerbaijan Democratic Republic; Armenian–Azerbaijani war (1918–1920).

Verdicts: samtskhe-saatabago fix (reviewer applied it); principality-of-svaneti FAIL; khanates-of-the-caucasus thin; caucasian-imamate thin; armenia FAIL; azerbaijan-democratic-republic fix (reviewer applied it).

## samtskhe-saatabago: fix (applied)
- Applied: /identity/rulers/0 Qvarqvare II `from` 1451 -> 1465. The span started before the dossier's life (1465). The note says he was atabeg from 1451.
- Spot checks, all confirmed on the Samtskhe-Saatabago page:
  - 1465 Paravani separation ("In 1465 he defeated Georgian King George VIII at the battle near Paravani lake and separated from Georgia.").
  - 1535 invasion and annexation ("In 1535 King Bagrat III ... invaded Samtskhe"; "Georgians had annexed Principality of Samtskhe.").
  - 1535 Adjara and Lazeti to Rostom Gurieli.
  - Adjara under Mzetchabuk.
- Thin:
  - kingdom-of-kartli has Samtskhe as its vassal 1481-1483 (vassal_start c3, vassal_end c2). Samtskhe's ledger has no mirror, and the Samtskhe page is silent. Try Constantine II of Georgia.
  - The 1545-1625 Ottoman-vassal phase is not drawn (the author flagged it).
- Cross-checks:
  - kingdom-of-georgia dates the loss of Samtskhe to 1463 (c2). This dossier says 1465 (c2, confirmed on its page). Two years apart.
  - kingdom-of-imereti (gain of Samtskhe, 1535) and principality-of-guria (gain of Adjara, 1535) have no mirror events. Route to eu-19.

## principality-of-svaneti: FAIL
- Not applied (missing events): the ledger has no vassal events, although the page states both suzerainties.
  - Infobox: "subject of Kingdom of Imereti" (1463-1833) and "vassal of Russian Empire" (1833-1857).
  - Text: "both branches accepted nominal Russian suzerainty in 1833".
  - The author's notes say vassal events "belong to the suzerains' dossiers". That is a misreading: the mirror rule needs the vassal_start in both ledgers.
  - Fix part 1: add vassal_start 1833 (month 11 if the Svaneti page's 26 November 1833 holds), counterpart russian-empire, region the 1830 shape, confidence 3. Add vassal_end 1858 (or 1857) before the dissolve.
  - Fix part 2: add vassal_start 1721 counterpart kingdom-of-imereti, with vassal_end at 1810 (Imereti annexed 20 February 1810) or 1833 (the infobox). The note should say which and why.
  - Mark the 1834-1858 keyframe as vassal status in its `text`.
- Spot checks, all confirmed:
  - 1720s Dadeshkeliani ("emerged as the eventual winners by the 1720s"). Confidence 1 is honest.
  - 1857 Baryatinsky order ("ordered Svaneti to be subdued by armed force").
  - 1858 abolition ("the principality was abolished and converted into a district").
  - The infobox suzerainty lines.
- Cross-check: principality-of-mingrelia has a 1721 loss of Upper Svaneti to principality-of-svaneti. Svaneti's `found` names kingdom-of-imereti. The two disagree on who lost the land; the Svaneti page has Mingrelia take Lower Svaneti, not Upper. Route to eu-19.

## khanates-of-the-caucasus: thin
- Applied: /ledger/2 (1791 loss to qajar-dynasty) raised from confidence 1 to 2 and re-sourced to Agha Mohammad Khan.
  - The note said no page opened dated this. The Agha Mohammad Khan page, which the author opened, says he "marched into Azerbaijan in the spring of 1791".
  - On that campaign he made the Talysh Khanate acknowledge Qajar authority, "forced the Sarab Khanate into submission", "subdued the Ardabil Khanate" and appointed a governor of Khoy and Tabriz.
  - This also matches qajar-dynasty's 1791 gain.
- Spot checks, confirmed:
  - May 1795 invasion; Shusha 8 July-9 August 1795.
  - Derbent stormed 10 May 1796; "By mid-June Zubov's troops had overrun—without any resistance—most of the territory of modern-day Azerbaijan".
  - November 1796 withdrawal (no day on the page).
  - "formally crowned in 1796".
- Thin:
  - /ledger/1, the 1788 gain from zand-dynasty (the doubling to 194,383 km2), is still confidence 1. zand-dynasty records a loss of Azerbaijan to the khanates around 1780 (c1) and Zand overlordship 1760-1779 (c1). This dossier has no vassal pair to mirror it.
  - Pages to try: Tabriz Khanate, Urmia Khanate, Khoy Khanate.
- Cross-checks:
  - zand 1780 vs khanates 1788: mismatch.
  - qajar-dynasty's 1797 gain from the khanates comes after this dossier's 1796 end: mismatch.
  - russian-empire's 1796 occupation_start names qajar-dynasty, but the land invaded is the khanates' (this dossier's 1796-05 contest with russian-empire): mismatch on counterpart.

## caucasian-imamate: thin
- Applied:
  - /identity/capitals/0 Gimry moved from 42.4 N 46.85 E (about 40 km off) to 42.7572 N 46.8456 E, from the Gimry page; the page is added to `sources`.
  - Quotes corrected to the pages' wording in /ledger/1, /ledger/2 (note and region text), /ledger/3 and /keyframe_review/4/correction/text. For example, the page has "Shamil accepted, dissolving the Imamate", not "and the Imamate was dissolved".
- Spot checks, confirmed:
  - 1828 infobox.
  - Hamzat Bek "had previously secured the allegiance of the Avar Khanate".
  - 28 August 1843 Untsukul, then "In the next four weeks, Shamil captured every Russian outpost in Avaria except one".
  - 1859 surrender.
- Thin (page budget 1-2, spent):
  - The ledger gains Avaria twice: 1832 from avar-khanate and 1843 from russian-empire, with no loss or occupation in between. The keyframes also show Avaria inside the Imamate throughout 1832-1858.
  - Fix: the Russian hold on Avaria/Khunzakh after Hamzat Bek's death (1834) should be an occupation_start or loss, with the 1843 event as its end.
  - The Caucasian War page adds that "by 1841 the Imamate incorporated the lands of the liquidated Avar Khanate".
  - Pages to try: Hamzat Bek, Avar Khanate, Imam Shamil.
  - Also unexplained: the 1836 loss of 3,304 km2 (west edge 44.37 -> 44.68 E) and the 1856-59 contraction (Vedeno, Gunib).
  - The Caucasian War has empty zones and no contest events, although ground changed hands.
- Cross-check: russian-empire has no 1843 loss of Avaria (route to eu-17). Its 1859 gain matches the dissolve.

## armenia (First Republic of Armenia): FAIL
- Applied:
  - Counterpart "Democratic Republic of Georgia" -> `georgia` (the DRG dossier, 1918-2024) in /ledger/5, /ledger/6 and /wars/1/belligerents. georgia's 7 December 1918 / January 1919 contest pair mirrors it.
  - /ledger/7 (Kars, 1919): counterpart `nobody` -> `southwest-caucasian-republic`, month 4.
    - The note said the page does not name Kars's holder. It does: "The Southwest Caucasus Republic administered the entire Kars and Batum oblasts" and the page records "its capitulation by Armenian and British forces on 10 April 1919".
    - The Southwest Caucasian Republic needs a dossier.
- Not applied (missing event, blocking):
  - The page says "On 30 October, the Turkish army occupied the city of Kars", but the ledger has no loss or occupation of Kars in 1920.
  - /keyframe_review/2 says the page gives "not ... the date of the loss". It does.
  - As written, the dissolve passes the whole 1919 shape, Kars included, to the Armenian SSR.
  - Fix: add a loss (or occupation_start) on 1920-10, counterpart the Turkish National Movement (the author's suggested slug grand-national-assembly-of-turkey), region admin1 Kars, confidence 3. Say in the 1920 keyframe that Kars (and the land ceded at Alexandropol) went to Turkey. Take Kars out of the dissolve region.
  - The infobox 1920 area is 27,000-30,044 km2 against the shape's 40,911.
- Spot checks, confirmed:
  - November 1918 Ottoman evacuation, "+16,000 km2".
  - June 1919 Nakhichevan.
  - Turkish invasion 28 September 1920.
  - Zangezur ceded November 1920.
  - Handover 2 December 1920.
  - Treaty of Alexandropol 3 December 1920.
- Area:
  - 1919: the infobox "(after the Armistice of Mudros)" gives 45,325 km2 against the shape's 40,911 (0.90).
  - 1918: 11,396 km2 against 16,537 (1.45). The author acknowledged it.
- Cross-checks:
  - ottoman-empire has no loss for the November 1918 evacuation (route to me-10).
  - ottoman-empire's 19 April 1919 loss of Kars names armenia, while this page has the Southwest Caucasian Republic holding Kars: mismatch on counterpart.
  - georgia's 1920-12 gain of the Lori neutral zone from armenia has no Armenian mirror; the page calls Lori "a neutral zone under British supervision".
  - azerbaijan-soviet-socialist-republic has no contest events with armenia (1920).

## azerbaijan-democratic-republic: fix (applied)
- Applied:
  - /ledger/1 counterpart "Baku defenders (Dunsterforce and the Centrocaspian Dictatorship)" -> `centrocaspian-dictatorship`. The page names the "Centro Caspian Dictatorship (1 August 1918 – 15 September 1918)", which needs a dossier.
  - /wars/1 belligerent "Soviet 11th Army" -> `russian-soviet-federative-socialist-republic`.
- Spot checks, confirmed:
  - Baku entered 15 September 1918.
  - Allied arrival 17 November 1918.
  - Mughan Soviet Republic 15 May 1919.
  - "British forces left on 19 August 1919".
  - "ceased to exist on 28 April 1920".
- Area: the infobox gives 99,908.87 km2 (1918) against the shape's 87,458 (0.875). Acknowledged.
- Thin:
  - The Karabakh contest_start (1918-11, c1; Andranik's seizure is undated on the page).
  - The Mughan contest_end (c1).
  - The 1918 keyframe is "ok" though its note says the shape includes claimed Nakhchivan and Zangezur and a strip of Iran. Consider `adjust`.
- Cross-check: british-colonial-empire has no occupation of Baku 1918-1919 (route to eu-11).
