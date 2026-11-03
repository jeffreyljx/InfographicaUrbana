# Review of batch af-02-e (Wattasid dynasty, Saadi Sultanate, Morocco, Beylik of Tunis)

Reviewer, 2026-10-19. Validator: all four valid with --resolve (0 errors). Remaining warnings are the counterparts that have no dossier yet (dila-iya-sultanate, pashalik-of-timbuktu, sahrawi-arab-democratic-republic), the open Timbuktu vassalage and Western Sahara occupation, and the Chafarinas region, which is smaller than one cell. The machine copy is history/notes/phase-b/reviews/af-02-e.json.

Verdicts: wattasid-dynasty **fix** (fixed by the reviewer), saadi-sultanate **fail**, morocco **fix** (one fix applied, the others non-blocking), beylik-of-tunis **thin** (one fix applied).

Spot checks: every page opened says what the notes claim, with the year. No event is fabricated, and no confidence-3 event is mis-dated.

## Reviewer edits (applied, re-validated, read back)
- wattasid-dynasty /keyframe_review/0: the 1468 shape was kept for 1468-1471, before the dossier's own 1472 start ('Established: 1472'). The correction now says it holds from 1472 to 1474, and the note says so. If a hole in 1465-1471 is not wanted, the start has to move to 1468 with a page.
- morocco /ledger/13: the 1860 Ifni loss now names spanish-empire, not kingdom-of-spain. The mirror already exists at spanish-empire /ledger/104.
- beylik-of-tunis /identity/rulers/11: as-Sadiq's reign is capped at 1881, the dossier's end. The note says he reigned until 1882.

## saadi-sultanate: fail
1. **BLOCKING: the 1641 rump is not explained by ledger events.** saadi-sultanate_1629 is marked ok for 1629-1639, and the new 1641-1659 keyframe is Marrakech-Tensift-Al Haouz alone. About 350,000 km2 therefore leave the realm, and only /ledger/21 explains any of it: Fez and Meknes (60 km each) and Rabat-Sale, about 30,000 km2, lost to the Dila'iya. The Souss and the Draa, the Tafilalt, the Tangier-Tetouan coast, the Gharb, the Middle Atlas and the east have no loss event.
   - The Dila'iya page, which the author opened, says that after 1613 'the Sus, until Draa River' was under the Zaouia of Illigh and 'the Tafilalt' under the Alawites.
   - morocco /ledger/0 founds the Alawi state at Sijilmasa in 1631, so the Tafilalt is claimed by both dossiers in 1631-1640.
   - morocco /ledger/3 gains the whole north and the Middle Atlas from dila-iya in 1668, far more than this dossier ever loses to it.
   - Fix: mark /keyframe_review/10 adjust, removing the Tafilalt from 1631 and the Souss-Draa from the year a page gives (bridging at confidence 1 if none). Add a 1631 loss of the Tafilalt to morocco, a loss of the Souss-Draa to zawiya-of-illigh, and a widened 1641 loss to dila-iya that matches morocco /ledger/3.
2. /ledger/22: the dissolve in 1659 gives Marrakesh to morocco, but morocco /ledger/4 gains it in July 1668 from 'nobody'. The Saadi page says the last sultan was 'assassinated and usurped by his maternal uncle'. Fix: name the 1659-1668 holder the same way in both dossiers.
3. /keyframe_review/4: the 1582 shape is said to hold for 1583-1590, and the 1556 shape ends in 1581, so 1582 has no Saadi shape. Fix: say which shape draws 1582.
4. Thin, not faults: La Mamora 1614 and the Asilah handovers (1550, 1577, 1589) are missing. The 1556-57 Taghaza occupation is not drawn.

Confirmed on the page: Agadir 1541 and Safi/Azemmour the same year; Fez 28 January 1549; Tlemcen June 1550 to February 1551; Fez January and September 1554; Touat and Gourara 1583; Taghaza 1586; Timbuktu 30 May 1591; Djenne 1592; Larache November 1610; direct control of the Sudan given up in 1618; the Dila'iya hold Fez, Meknes and Sale by 1641; end in 1659.

## morocco: fix
- Non-blocking: /ledger/10, /ledger/11, /ledger/12 and /wars/2 name kingdom-of-spain for 1848-1860, but spanish-empire holds Spain's African posts until its 1899 dissolve. The orchestrator should settle once which Spain dossier owns them.
- Non-blocking: /ledger/25 occupies all of Western Sahara from 1976. Mauritania held the southern third until 1979, and the Morocco page says 'In 1979, Mauritania relinquished its claim'. Fix: give the 1976 occupation the Moroccan share only, and add a 1979 occupation of Tiris al-Gharbiyya.
- Thin:
  - /keyframe_review/11: the Tarfaya strip (about 28k km2) leaves the shape in 1885 with no ledger event. The Spanish protectorate page dates its recognition as Spanish to 1904 and its inclusion in the protectorate to 1912, so a dated loss is possible.
  - The 1672 capital move is at confidence 1.
  - Spain occupied Tetouan from 1860 until the indemnity was paid; there is no occupation pair.
  - Moulay Isma'il's recaptures of Mamora, Larache and Asilah have no events.
- Area: infobox 446,550 km2 against 406,464 km2 for the 2024 shape (ratio 0.91), acknowledged.
- Confirmed on the page: 1631; Fez June 1666; Marrakesh July 1668; Tangier 7 February 1684; Chafarinas 1848; Wad-Ras 26 April 1860; Tangier zone 1912 (confidence 2, with a disagreement between pages); Treaty of Fez 30 March 1912; Spanish zone 27 November 1912; 2 March and 7 April 1956; Tangier Protocol 29 October 1956; title of King 1957; Angra de Cintra 1 April 1958; Ifni 5 January 1969.

## wattasid-dynasty: fix (by the reviewer)
- Confirmed: 1472; north only ('the south being divided into several principalities'); Melilla 1497; Penon 1508; Fez 28 January 1549; Abu Hassun's Fez of 1554 and its loss in September 1554.
- Thin: Spain lost the Penon in 1522, which no opened page says. The dossier keeps the Penon Castilian through 1554.
- Route: the infobox gives 'Vassal of the Ottoman Empire from 1545'. The vassal pair belongs in ottoman-empire (me-10), with a mirror here.

## beylik-of-tunis: thin
- /ledger/1: the 1794 frontier strip (+8.4k km2) is at confidence 1 and comes from Cliopatria only; the Tripolitanian civil war page has no land transfer. In 1794 Tripoli was held by Ali Burghul, not the Karamanlis.
- Non-blocking: Burghul's occupation of Djerba on 30 September 1794 is on the page and in the war's zone, but has no occupation pair. Fix: occupation_end 1795-1 at confidence 1.
- Area: the protectorate page gives 155,000 km2 against 87,905 km2 for the shape (0.57), acknowledged in /keyframe_review/11.
- Confirmed on the page: 15 July 1705; the invasion of 24 April 1881; Bardo 12 May 1881.
- Route:
  - The Ottoman suzerainty pair goes to me-10.
  - The protectorate of 1881-1956 goes to af-08. Rule 4 (vassal tint) would keep the Bey's land as a French vassal, not dissolve it; the same question applies to Morocco 1912-1956.

## Cross-dossier
- Matched:
  - Wattasid and Saadi, 1549 and both 1554 events.
  - morocco and english-colonial-empire, Tangier 1684.
  - morocco and portuguese-empire, Mazagan 1769.
  - morocco and spanish-empire, Ifni 1860 (after the reviewer's edit).
- Missing on the neighbour's side:
  - zayyanid-dynasty has no Saadi occupation of Tlemcen in 1550-1551.
  - spanish-empire has no 1610 Larache gain.
- Mismatched inside the batch:
  - The Saadi dissolve of 1659 against Morocco's Marrakesh of 1668.
  - Morocco's found of 1631 against the Saadi Tafilalt.
  - The Saadi 1641 loss to the Dila'iya against Morocco's 1668 gain from them.
