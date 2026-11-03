# Review of batch sa-01-c (2026-10-18)

The reviewer opened nine pages with WebFetch: the author's eight, plus Nanda_Empire and Shaishunaga_dynasty. The validator (`--resolve`) reports 0 errors and 0 warnings for all six dossiers. Overlaps were measured with `tools/gazetteer.py` on the current neighbour files.

| slug | verdict |
| --- | --- |
| magadha-haryanka-dynasty | fail (5 region and identity findings, plus thin) |
| janapada-of-vajji | pass |
| janapada-of-vatsa | thin |
| janapada-of-pancala | pass |
| janapada-of-surasena | thin |
| janapada-of-matsya | fix (applied by the reviewer) |

## magadha-haryanka-dynasty: fail
Every dated event that was spot-checked is on its page: 468 (Vajjika League), 481-480 (Basham, on the Ajatashatru page), 413 (Haryanka infobox; the Shaishunaga page says 'Established 413 BCE'), the Udayin capital move (undated) and the ruler list. The failures are in the land.
1. `/ledger/8` (the -450 gain of Cedi, confidence 1). The region is Cliopatria's Cedi disc: 18 cells, and 0 of them are inside the dossier's own `/keyframe_review/3/correction`, because the Allahabad 80 km minus removes all of them. janapada-of-cedi dissolves at -451 with counterpart null and has moved Cedi to Bundelkhand. No page that was opened mentions Cedi. Fix: delete the event, or point its region at Cedi's corrected land intersected with keyframe 3 and have Cedi name this dossier.
2. `/ledger/7` and `/keyframe_review/3` (Kasi-Kosala). The gain covers only the Cliopatria Kosala and Kasi discs (43 cells). janapada-of-kosala hands over its Awadh correction (231 cells), and 58 of those cells lie outside keyframe 3 (80.90-82.62E 25.22-28.41N), so they become nobody's from -450. Fix: use Kosala's `/keyframe_review/1/correction` as the gain region and add it to the union in keyframe 3, and to `/ledger/9`.
3. `/keyframe_review/0` is marked ok, but it breaks the handover from janapada-of-magadha. Magadha's last shape has 107 cells, this dossier's first has 125, and they share 78: 29 cells vanish and 47 appear in -500 with no event. The Cliopatria -500 and -480 shapes also cross the Ganga into the Vajji polygon (13 cells, 85.28-86.71E 25.42-25.82N), against the Vajjika page's Ganga boundary. Fix: set the verdict to adjust, take Magadha's -530 correction minus the Vajji polygon, and apply the same minus to keyframe 1.
4. `/identity/predecessors/0/land` is only the Magadha disc, though its text says Anga is included. Fix: use Magadha's -530 correction.
5. `/identity/rulers/0` starts Bimbisara at -544, before the dossier's start of -500. Fix: clip to -500 (or the orchestrator moves the boundary). In `/identity/rulers/1/note`, the Ajatashatru table reads 493-461, not 493-462.

Thin, by design under the 1-2 page budget (the author used 4 pages):
- The -480 growth of 215 cells (south of Anga, down to 21.5N) rests on a confidence-1 event whose counterpart, 'the smaller kingdoms', is a page phrase. Use 'nobody' unless a page names a state.
- The -450 growth adds 689 cells (about 174,000 km2) over the -468 keyframe, and only about 39 of them are explained.
- The capital move (-460) and the found (-500) are confidence 1.

Pages to try: Magadha, Udayin, Kosala.

## janapada-of-vajji: pass
The reviewer tried to break:
- the 468 annexation and contest end (confirmed);
- the 481 contest start (confirmed, Basham);
- the 484 war start (confirmed);
- the four boundaries (confirmed);
- the capital inside the polygon (yes);
- whether a gazetteer region could replace the polygon (none: no Videha, Mithila, Tirhut or Vaishali);
- overlaps.

The 13-cell overlap with the Magadha/Haryanka shapes is on their side (finding 3 above). The 3 cells shared with Malla are negligible: the Mallas were league members. The Videha predecessor still needs a dossier (sa-01-x).

## janapada-of-vatsa: thin
Both events are confidence-1 bridges, and the page dates nothing. Its statements were all confirmed as the notes report them: annexed by Avanti; Pradyota holding Udayana; Maniprabha at Kausambi; infobox c. 700 to c. 300 BCE; south of the Ganga; Allahabad division.

Advisory: the Cliopatria disc lies north of the Ganga (Pratapgarh). The 80 km Allahabad circle is defensible because the page names the Allahabad division, but it overlaps Kosala's correction by 9 cells and the Kasi disc by 4. The infobox's 'Preceded by: Kuru Kingdom' is not recorded.

Cross-dossier: janapada-of-avanti takes only the 15-cell disc, not Vatsa's 80-cell correction, so 65 cells are nobody's from -450. That is to be fixed in the Avanti dossier.

Pages to try: Pradyota dynasty, Udayana (king).

## janapada-of-pancala: pass
Confirmed: the annexation under Mahapadma Nanda in the mid-4th century (header c. 340 BCE; the Nanda page has the empire from c. 345 and Mahapadma c. 345-340); the region names; both capitals, inside the correction.

Cross-dossier: the -404..-340 keyframe overlaps Cliopatria's Shaishunaga shape by 27 cells around Kanpur. The Pancala page supports Pancala there, so the Shaishunaga dossier should cut those cells.

## janapada-of-surasena: thin
The end (-334) is confidence 1 and the page is silent. The Nanda Empire page says the Surasenoi 'were subordinates to the king of the Prasii', which could raise the counterpart to confidence 2. The Mathura circle overlaps the Matsya correction by 6 cells; the author flagged it, and it still needs settling.

## janapada-of-matsya: fix (applied)
The dissolve at -350 named nanda-empire, but the Nanda Empire page gives 'Established: c. 345 BCE'. The Shaishunaga page (413-345 BCE) lists Matsya under 'Preceded by'. The reviewer changed `/ledger/1/counterpart` and `/identity/successors/0/slug` to magadha-shaishunaga-dynasty and appended a cited note. The file re-validated with 0 errors and 0 warnings. The Shaishunaga dossier must add the -350 gain, because its Cliopatria shape holds none of Matsya.

## For the orchestrator
- Rule 2: Magadha under the Haryanka, Shaishunaga and Nanda dynasties is one state split across four dossiers, and the -544/-500 boundary needs a decision.
- janapada-of-cedi (Banda, Rewa) and janapada-of-avanti (Maheshwar) use places the gazetteer lacks, so their shapes do not resolve.
