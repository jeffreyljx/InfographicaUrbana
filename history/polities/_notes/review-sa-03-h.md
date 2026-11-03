# Review of batch sa-03-h (2026-10-19)

The batch has three dossiers: kakatiya-dynasty, yadava-dynasty and kayastha-principality-of-ambadeva. The validator (with --resolve) gives no errors and no warnings for any of them. All three fail. Most of the dating holds up: of 19 spot checks, every confidence-3 event and every large land move I opened says what its note claims. The failures come from regions and keyframes:

- the Ambadeva principality is drawn in the wrong place;
- Nellore is handled inconsistently in kakatiya-dynasty and kayastha-principality-of-ambadeva;
- two Yadava keyframes contradict the dossier's own ledger, and its 1260 keyframe adds land with no event.

I edited no dossier, because every fix is a region or keyframe change. The machine copy of this review is history/notes/phase-b/reviews/sa-03-h.json.

Pages opened: Ganapati_Deva, Prataparudra_II, Kakatiya_dynasty, Rudrama_Devi, Ambadeva (not in the authors' sources), Seuna_dynasty, Singhana_II, Malik_Kafur, Ramachandra_(Yadava_dynasty) and Qutbuddin_Mubarak_Shah. Cell counts come from tools/gazetteer.py resolve on the dossiers' own region specs.

## kakatiya-dynasty: fail

Confirmed on the pages:
- 1163 sovereignty, and Orugallu established in 1195.
- Vela-nadu by 1201, and Kalinga lost "Sometime before 1217".
- Kolanu taken in 1231, and Nellore lost at Muttukuru in 1263.
- Naga-deva at Nellore 1271-1275.
- Raichur in 1294 (Raichur Fort inscription).
- Mulikinadu annexed in 1309.
- The siege of Warangal ended in February 1310, and Warangal fell on 9 November 1323 (infobox).

The keyframes agree with the ledger for the delta (1201 and 1231), the Kalinga lobe (1217) and the 1294 lobe.

Faults:
1. **Ambadeva's land is misplaced** (/ledger/16, 17, 20, 21 and the war zone). It is drawn as {place: Ongole, km: 120}, coastal Prakasam and southern Guntur, and 59 of its 162 cells overlap the 1201 Vela-nadu gain. The author's own Prataparudra II page says Ambadeva retreated "southwards to the Mulikinadu region" from Tripurantakam. The Ambadeva page names his capital Valluru-pattana and the Gandikota fort. Its 1287 Attirala inscription lists "Valluru-pattana, Gandikota, Muliki-nadu, Renadu, Pendekallu, Sakili, Eruva, and Pottapi-nadu", which is the Kadapa country. Redraw the region there (Proddatur about 90 km as a stand-in), and cite and list https://en.wikipedia.org/wiki/Ambadeva.
2. **Nellore is lost twice**: to the Pandyas in 1263 (/ledger/11) and to Ambadeva in 1281 (/ledger/16), with no regain in between. Naga-deva's rule of 1271-1275 is a vassal relation, not direct land. The Rudrama Devi page has Tiru-kalatti-deva II ruling Nellore c. 1279-1283 until "another Choda chief Manuma-Gandagopala displaced him". Drop Nellore from the 1281 loss.
3. **/ledger/19 is mis-dated** (confidence 1). The Nellore recapture is 1290 on the Ambadeva page ("In 1290 CE, Rudrama's successor Prataparudra defeated Manuma-Gandagopala"), not 1298. The 1297-98 inscription belongs to the second expedition, against Raja-Gandagopala's alliance with the Pandyas.
4. **The 1291 gain of Tripurantakam is missing.** The Ambadeva page dates his last record there to 13 June 1291 and the Kakatiya chiefs' first record to 11 August 1291.
5. **Two counterparts are free text and not listed** in counterparts_needing_dossiers: "Rulers of Kolanu in Vengi" and "Naga-deva of Nellore".

Thin within the 5-page budget, not faults:
- K1 (1177): about 265 cells outside Telangana have no event. The Kalinga lobe is Ganapati's campaign, after 1199.
- Kampili's occupation of the west is undated.
- The five districts ceded in 1318 are not named.
- Three confidence-1 bridges remain (1208, 1274, 1323).

There is no infobox area to compare.

## yadava-dynasty: fail

Confirmed on the pages:
- Kalyani c. 1187.
- 1212, 1213 and 1220 on the Singhana II page.
- Kolhapur "Around 1216" ("before 1217").
- Raichur 1294, with the annexation after 1296.
- The 1296 raid.
- Kafur's annexation in 1313 and his recall in 1315.
- April 1317 and Harapaladeva's execution.

Faults:
1. **K2 contradicts the ledger.** K2 (1236) is Cliopatria's 1236 shape minus Malwa and Lata. That shape lacks 117 of the 200 cells of the 1212 Hoysala gain and 69 of the 132 cells of the 1216 Kolhapur gain. About 186 cells therefore vanish in 1236 with no loss event, and 104 of them return in 1260, although K2's note says "Kolhapur and the Hoysala north stay Yadava". Make K2 the union of the 1236 shape with the 1212 and 1216 regions, minus Malwa and Lata, or shrink those regions. The Kolhapur 100 km disc reaches the Konkan coast and Goa, which are gained only in 1260.
2. **K3 adds land with no event.** Between 1236 and 1260 the corrected shape gains 919 cells and loses 47, and the only event is the confidence-1 Konkan gain. The Ramachandra page puts Tripuri (Tewar near Jabalpur), Vajrakara (Vairagad) and Bhandagara (Bhandara) under Ramachandra, r. c. 1271-1311. So the Chhattisgarh, Jabalpur and eastern Vidarbha lobes (about 96,000 km2) are drawn at least 11 years before the page allows. In addition, 84 Andhra cells and about 99 Karnataka cells of the Kakatiya lobe become Yadava at 1260 with no event. Trim these from K3 and add gains after 1271, or source the 1260 date.
3. **K4 brings back Malwa.** K4 (1314) is the raw shape, which holds the 16 Malwa cells K3 trims. Trim them in K4 too.
4. **"Shankha of Lata"** is a free-text counterpart and is not listed.

Thin:
- The 1198 vassalage of Ganapati: the Singhana II page has it, the Ganapati Deva page does not. The author's choice is recorded; a gap-filler should decide.
- The 1260 Konkan gain is confidence 1. The page describes curbing a rebellion, not an annexation.
- The Hoysala war is dated "late 1180s" here and c. 1191 in hoysala-kingdom.
- The 1316 restoration is a bridge.
- The ruler strip starts only in 1210.

There is no infobox area to compare.

## kayastha-principality-of-ambadeva: fail

The author did not open the Ambadeva article. It contradicts the dossier's shape and capital:
1. **Shape and capital are wrong.** The capital was Valluru-pattana, not Tripurantakam, and the land was the Kadapa country (the 1287 Attirala inscription list), not Ongole 120 km.
2. **Nellore is counted twice**, as direct land taken from the Kakatiyas and as a vassal. In 1281 Nellore was in Telugu Choda hands, not Kakatiya. Keep it as a vassal only, with counterpart telugu-chodas-of-nellore (the Rudrama page calls Manuma-Gandagopala "another Choda chief").
3. **The Nellore events are mis-dated**: 1298 should be 1290.
4. **The 1291 loss of Tripurantakam is missing**: defeated "in mid-1291", last record 13 June 1291. Tripurari-deva II "may have ruled the territory lost by Amba-deva". Say who held the Kadapa core from 1291 to 1309.

Confirmed: the "Sometime before 1281" bound, the 1291-92 army sent to Tripurantakam, and the 1309 expedition to Mulikinadu.

## Cross-dossier mismatches outside this batch

- chola-empire /ledger/34 sends Vengi to kakatiya-dynasty in 1177 (confidence 1), against 1201 and 1231 here. Its /ledger/39 loses Vengi and Nellore to pandya-empire by 1250.
- eastern-ganga-kingdom /ledger/11 gains the Kalinga lobe in 1260 from nobody, against the 1217 loss to eastern-ganga-kingdom here.
- hoysala-kingdom /ledger/10-11 has c. 1191 against "late 1180s" here.
- All Delhi events (khalji-dynasty, tughlaq-dynasty) and Pandya events (pandya-empire) wait for sa-04.
