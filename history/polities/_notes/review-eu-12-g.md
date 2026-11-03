# Review of batch eu-12-g (taifas of Arcos, Carmona, Granada, Morón, Murcia, Niebla)

Reviewer: Phase B adversarial reviewer, 2026-10-25. Machine copy: history/notes/phase-b/reviews/eu-12-g.json.

Mechanical: validate_dossier.py --resolve gives 0 errors on all six; Granada has 2 warnings (counterpart taifa-of-malaga, no dossier; listed by the author). No Cliopatria row of these states is in data/README.md. Families (caliphate) are valid; capitals fall inside the shapes' bboxes, or a circle was added where Cliopatria's outline misses the town (Carmona 1147, Niebla all). No infobox on the six Taifa pages gives an area (checked on each), so no factor-of-two test was possible except Murcia 1152.

## Verdicts

- taifa-of-arcos: fix (applied by reviewer). /wars/0 ran 1053-1068 although the Taifa page lists Muhammad II al-Qaim as ruler of Arcos 1053-1068/9 and the first period 'from 1011 to 1068'; narrowed to 1068. Ledger events 0-3 confirmed on the Taifa page. Thin: extent of the 1143-1145 restored taifa.
- taifa-of-carmona: fix (applied by reviewer). /wars/1 outcome cites Ibn Hamusk and 1161, which are on the Carmona, Spain page ('briefly occupied by Ibn Hamusk, before reverting to the Almohads in 1161'), not the Taifa page; a sentence naming the source was appended to the war note. Ledger 0-3 confirmed.
- taifa-of-granada: thin. All seven spot checks confirmed (1013, 1028-1029 Cabra and Jaén, 30 August 1036, al-Funt 1038, Málaga 1056, Tamim 1073, September 1090). Thin: the 1085 loss (/ledger/8, confidence 1, about 14,000 km2, counterpart unnamed) and the 1041 end of the Almería vassalage (/ledger/5, confidence 1); the land won 'to the west' in 1039 and from Almería in 1038 has no event. Minor: /keyframe_review/4 removes Málaga from the 1072 shape for 1072 too (lost 1073), one year early.
- taifa-of-moron: pass. Tried: 1010 founding (page 'around 1010'), 1066 conquest by Seville, years of the two shapes, capital inside the outline, Córdoba mirror (Córdoba uses 1013, its side to fix). Nothing broke.
- taifa-of-murcia: fail. Back to the author with:
  1. /ledger/14 (confidence 3) and /keyframe_review/7 give Ibn Hud the Valencia region in 1228; the Ibn Hud page says he took most of al-Andalus 'except Valencia, where he was opposed by Zayyan ibn Mardanish', the Taifa of Valencia page says Zayyan 'remained independent of Ibn Hud', and the Almohad dossier gives Valencia to taifa-of-valencia. Drop Valencia. 'Andalusia' also includes Andújar, Baeza and Martos, Castilian from 1225 (kingdom-of-castile ledger/43).
  2. /ledger/19: an unsourced confidence-1 loss of all Andalusia except Córdoba to 'nobody' in 1236 double-counts Granada (1237, /ledger/20) and Almería (Ibn Hud 'assassinated in January 1238 at the gates of Almería'; Almería to the Emirate of Granada in 1238 per the Almohad dossier). Replace with dated, named losses.
  3. /ledger/4: a 1091 loss to the Almoravids of land already lost to Seville in 1078 (/ledger/3; page 'From 1078 until 1091 ... forcible control of Seville'). Delete; it is Seville's loss.
  4. /ledger/7: Valencia under Ibn Mardanish from 1147 (Taifa of Valencia page: Ibn 'Iyad died August 1147 and passed Valencia's forces to him; rulers 'Ibn Mardanish: 1147-1172'), not 1152; /keyframe_review/4 (1147-1151, Murcia core, ok) must take Valencia.
  5. /ledger/8: Alicante 'from taifa-of-denia' in 1152, but the Dénia dossier has no state 1076-1224 (and the Almohad dossier also takes Dénia from taifa-of-denia in 1152).
  6. /keyframe_review/5 and /6: Cliopatria 77,869 and 70,031 km2 cut to 27,800 km2 (Murcia, Valencia, Alicante) on page silence; the cut drops Castellón province although the Ibn Mardanish page puts Montornés castle under him in 1147/8, and the Taifa of Valencia page has him 'ruler of the eastern part of al-Andalus'. Keep Cliopatria (unverified) or bound the realm with a page first.
  7. /ledger/11: confidence 3 on Valencia and Alicante with a source naming only Murcia; cite the Taifa of Valencia page or lower to 2.
  8. /keyframe_review/9: the 1241 shape is cut to the post-1245 outline for all of 1241-1249, so Lorca, Mula and Cartagena go in 1241 and again in 1244-1245.
  9. /ledger/18: contest_end in 1236 with kingdom-of-castile, whose dossier ends in 1235.
  Confirmed: 1078 Seville, 1165 Fahs al-Jullab, 1172 Almohads (year), Córdoba 1236, Granada 1237, Alcaraz April 1243, Lorca and Mula 1244, Cartagena spring 1245.
- taifa-of-niebla: fix (applied by reviewer). /ledger/4 (1234 gain from the Almohads) lowered from confidence 3 to 2: the author's own note doubts the counterpart, and the Ibn Hud page and the Almohad dossier (ledger/46, October 1228) have the Almohads out of Iberia from 1228. Other checks confirmed (1023, 1053 'The battle was lost and Niebla fell under the control of Seville in 1053', 1150, 1262).

## Cross-dossier matrix (summary; full list in the JSON)

Matched: Córdoba founding losses for Arcos 1011, Carmona 1013, Granada 1013, Murcia 1011, Niebla 1023; Almoravid gain of Granada September 1090; Almoravid loss of Niebla 1145; Almohad gain of Murcia 1172; Almohad 1228 losses of Murcia, Almería and the rest to Murcia.
Mismatch: Morón founding 1010 vs Córdoba 1013; Carmona and Niebla 1150 vs Almohad 1152 (confidence-1 bridges, af-02 to fix); Murcia 1145 vs Almoravid 1147; Murcia 1091 vs Almoravid 1092 (both should name Seville); Murcia's 1152 Dénia from a non-existent taifa-of-denia (and the Almohads take Dénia the same year); Murcia's 1228 Valencia vs Almohad's Valencia to taifa-of-valencia; Murcia's 1236 'nobody'; Niebla's 1234 gain from the Almohads vs the Almohad/Murcia 1228 transfer.
Missing: Almoravid losses of Arcos and Carmona c. 1143; Almohad gain of Arcos 1145; Córdoba loss of Jaén to Granada c. 1028; Castile's contest with Murcia 1231-1235 (Jerez).
Exceptions: everything with taifa-of-seville, -almeria, -valencia, crown-of-castile, emirate-of-granada (eu-12, not written yet) and taifa-of-malaga (needs a dossier, eu-12-x).
