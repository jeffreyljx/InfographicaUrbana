# Review of jk-01-c (adversarial reviewer, 2026-10-18)

Machine copy: history/notes/phase-b/reviews/jk-01-c.json. All three dossiers validate (`--resolve`: 0 errors, 0 warnings, before and after the reviewer's edits). Neighbours read: ashikaga-shogunate and ryukyu-kingdom. Not yet written: russian-empire (eu-17), joseon (jk-02) and empire-of-japan (jk-01), so events against them count as exceptions.

## warring-states-japan: fail
Blocking:
1. **Kaga drawn twice, 1488-1580** (/keyframe_review/2-15). The 1488 loss and 1580 gain against kaga-ikko-ikki span thirteen shapes, all marked ok, and none of them removes Kaga. kaga-ikko-ikki_1488 draws the same cells. Fix: mark the shapes 1497-1564 adjust, each minus the Kaga region of /ledger/4. Do the same for the 1572 shape (1572-1578; its 1572-only correction already removes the Ashikaga remnant, so add Kaga to that minus). Split 1475-1496 at 1488 and 1579-1581 at 1581.
2. **Eastern half unexplained in 1600** (/keyframe_review/19). The area goes from about 325,000 km2 to 165,165 km2 and no event in this ledger removes the eastern half. tokugawa-shogunate /ledger/0 founds the Tokugawa on it with this state as counterpart. Fix: add a 1600 loss to tokugawa-shogunate, region `{"cliopatria":"Tokugawa Shogunate","year":1600}`, source Sekigahara, confidence 2.
3. **Capital outside the shape** (/identity/capitals/0). Kyoto, 1467-1572, sits inside the Ashikaga remnant (ashikaga-shogunate_1468 bbox), which this dossier excludes, and the entry cites no page. Fix: end the entry in 1467 or cite a seat inside the shapes.

Applied by the reviewer: /wars/2/from 1569 to 1570 (Sengoku timeline: '1570: ... the beginning of the Ishiyama Hongan-ji War').

Advisory:
- /ledger/13 quotes the Imjin page's 'withdrew to the peninsula's southern coastal regions', but that sentence is about 1597-98. The 1593 date rests on Azuchi-Momoyama: 'by January 1593'.
- /ledger/7 cites the Azuchi-Momoyama infobox line 'captures Kyoto: October 18, 1573', which is the page's own error (1568).

Thin:
- 1468 gain at confidence 1.
- 1552 Oshima cells.
- 1580 Kaga year.
- The 1597 second invasion.
- No Iga ikki (1477-1581) or Yamashiro ikki (1485-1493) events. The Sengoku timeline dates both ends of each, so the author's [1485, 1485] for yamashiro-ikki is wrong.

Spot checks, all confirmed: the Onin War (17 Dec 1477), Sengoku 1488, Azuchi-Momoyama (2 Sep 1573; January 1593), the Imjin War infobox and the 1592 dates, Sekigahara. No infobox area on any page.

## tokugawa-shogunate: thin
Applied by the reviewer: a source was added to the 14 shogun entries that lacked one. The page's shogun table matches the years.

To settle:
- The ryukyu-kingdom counterparts disagree: this dossier names ryukyu-kingdom for 1609-1611, while ryukyu-kingdom names satsuma-domain; the vassalage ends in 1868/1 here and in 1872/10 there. This is the orchestrator's decision.
- The 1855 Sakhalin contest has no war entry. Add a 'Sakhalin condominium' entry for 1855-1868, or give a reason in the note.
- Advisory: Amami is drawn twice in 1609-1610 (the K3 keyframe from 1609, the gain 1611). This is small and inside one shape's span.

Thin:
- Six confidence-1 events: Amami 1611; East Ezo 1799 and 1822 (the return was 1821); Hokkaido 1856 (usually 1855); the 1868 Ryukyu and Sakhalin ends.
- The Boshin War split is unverified (page budget).

Spot checks, all confirmed: 1603; the Ryukyu invasion dates (Mar-May 1609); Shimoda 1855; the 3 Jan 1868 end; the Hakodate bugyo page is silent, as the author says. No infobox area.

## kaga-ikko-ikki: thin
Applied by the reviewer: /wars/1/from 1569 to 1570.

Advisory: the Kanazawa 50 km circle clipped to Ishikawa overreaches into southern Noto. 'Kaga Province' has been requested from the gazetteer.

Thin:
- The end year 1580 (confidence 1; the Kaga Province page gives none).
- The seat (Oyama/Kanazawa Gobo).
- The start, 1486 or 1488.

Spot checks: Sengoku 1488 confirmed; the Ikko-ikki page's 1486 confirmed; Kaga Province names Shibata Katsuie with no year (confidence 1 is honest).
