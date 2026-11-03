# af-08-m notes (Partition and independence, part m)

Run of 2026-10-24. Six owned states and two rebel dossiers written; all validate (python3 -I tools/validate_dossier.py, with --resolve: one warning, Seychelles outer islands resolve to no cell). Every page opened loaded on the first try. Pages opened (14): Angola, South African Border War, Angolan Civil War, UNITA, Cape Verde, Comoros, Sao Tome and Principe, Seychelles, British Indian Ocean Territory, Djibouti, Djiboutian Civil War, Front for the Restoration of Unity and Democracy, Zimbabwe Rhodesia, Rhodesian Bush War.

## Cliopatria rows that are wrong (and what the dossier does)

- Republic of Cabo Verde (1976-2023, 2024): the shape is Cape Verde plus the Comoros (bbox 25.35 W to 45.15 E, 13.02 S to 17.26 N; 9,427 km2 against 4,033 km2 on the page). Both shapes adjusted: minus the Comoros. The Comoros have no Cliopatria row: they need a dossier (independence from France 6 July 1975; Mayotte stayed French).
- Seychelles (1976-2023, 2024): drawn 0.1 degree west of Mahe, no land cell. Both adjusted to the Natural Earth country polygon. At the project grid the country is one cell; the outer islands (Aldabra, Farquhar, Desroches, returned from BIOT on 23 June 1976) vanish.
- People's Republic of Angola 2024: the shape lacks Cabinda (stops at 5.89 S); adjusted by union with Cabinda. Cliopatria's Estado Novo row carries a 6,894 km2 Cabinda patch for 1979-2024 that overlaps Angola's 1976-2023 shape: eu-21 should drop it.
- Zimbabwe Rhodesia 1979-1982: the state lasted 1 June to 11 December 1979 (the page's quoted law); 1980-1982 belong to the Republic of Zimbabwe (18 April 1980), whose own Cliopatria row starts in 1983. Verdict adjust, years only. All three Rhodesian rows (Rhodesia 1967-78, this one, Zimbabwe from 1983) hold the same 392,765 km2 shape.
- Republic of Djibouti starts 1979 but independence is 27 June 1977: new keyframe 1977-78. The French Fifth Republic row (1961-2023) still contains all of Djibouti (the 86 cells of the country lie inside it in 1970 and 1980): eu-22 should remove it, like Algeria.
- Angola, Cabo Verde, Sao Tome and Principe: independence years (11 Nov, 5 Jul, 12 Jul 1975) precede Cliopatria's first year (1976); new 1975 keyframes. In 1975 Cliopatria's Estado Novo 1967-1975 shape (bbox 28.8 W to 127.2 E) still holds all of them.

## Not settled

- Angola: South African occupation. Settled in the repair run of 2026-10-24 (see below): 1975-76 placed by the Operation Savannah page, 1981-08 by the Operation Protea page (Cunene), 1988-08 by the Tripartite Accord (Angola) page. Still open: no page opened states a continuous occupation of Cunene between September 1981 and 1988, and none gives the day the 1984 Lusaka Accord withdrawal was completed; the 1981-88 span is a bridge.
- UNITA: its extent by year. The pages give Huambo (taken 7 March 1993), the Bie Plateau (1975-2002), and "70% of Angola" in August 1993, which no region expresses. Jamba (Cuando Cubango) is now a capital for 1976-1992 (Jamba page), and Bailundo for 1994-1999 (Huambo and Bailundo pages), but no page opened gives the land UNITA held around either, so none is drawn: the Jamba page gives the headquarters, its coordinates and the capture on 24 December 1999, the Andulo page says nothing of the war. The government retook Huambo on 9 November 1994 and Bailundo in October 1999 (Huambo page); the earlier guess of 1999-2000 for Huambo is withdrawn.
- The Angola page does not date the renaming to the Republic of Angola (1992): no rename event.
- Zimbabwe Rhodesia: the page's infobox runs to 18 April 1980, its law quotation ends the independent state on 11 December 1979; the dossier ends in 1979. The Bush War page says the country was renamed Zimbabwe-Rhodesia under the March 1978 agreement and dates the election to 24 April 1979, the Zimbabwe Rhodesia page dates the presidential vote to 28 May 1979. Neither page gives an area.
- Djibouti: the 2008 Djibouti-Eritrea clash at Ras Doumeira was not opened (budget); the Ethiopian border agreement of about 1997 is undated on the civil-war page. The 1992 Cliopatria shape differs from 1979 by 0.4% with no event.
- FRUD: the page gives no territory and no founding month; Obock and Tadjourah are a wide reading of "the north"; the Assa-Gueyla base has no coordinates so no capital is recorded.
- Seychelles: the page is silent on the 1965 detachment and 1976 return of the outer islands (read on the BIOT page). BIOT is a UK territory: counterpart is kingdom-of-great-britain.
- Sao Tome and Principe: one page (budget); no border event since 1975.

## Needs a dossier from someone else

- Comoros (1975-2024), no Cliopatria row.
- British Indian Ocean Territory (1965-2024), direct counterpart for Seychelles (1965-76) and Mauritius.
- The FNLA (partner of the 1975 Huambo government). The "Democratic People's Republic of Angola" itself stays an alt name and the 1975 keyframe of the unita dossier (a separate dossier would double the 1975 Huambo land, as the reviewer notes).

## Gazetteer names needed

Aldabra, Farquhar Group, Desroches (places, Seychelles outer islands); Jamba (Cuando Cubango, Angola); Calueque (Cunene, Angola); Assa-Gueyla (Djibouti); Mount Mabla (region, northern Djibouti). Added in the repair run: Bailundo (place, Huambo province, 12.19583 S, 15.85556 E, used as a capital of unita; the Bailundo page); Jamba is now used with coordinates 17.45583 S, 22.61306 E (Jamba page). Andulo (place, Bie province, 11.48 S, 15.83 E) is not used by any dossier.

## Budget

States: Angola 2 pages for the state (Angola, South African Border War) plus Angolan Civil War and UNITA shared with the rebel dossier unita; Cabo Verde 2 (Cape Verde, Comoros); Sao Tome 1; Seychelles 2; Djibouti 2 (Djibouti, Djiboutian Civil War) plus the FRUD page for the rebel dossier; Zimbabwe Rhodesia 2.

## Repair run of 2026-10-24 (reviewer findings for people-s-republic-of-angola and unita)

Applied (both dossiers validate with --resolve, 0 errors, 0 warnings):
- Angola: added gain of Huambo from unita, 1994-11 (Huambo page: "A large offensive gave back to the Government the control of Huambo on 9 November"; the page leaves the year to be inferred from "The armed conflict flared up again in August 1994"; the Civil War page: "By November 1994, the government had taken control of 60% of the country"). Rewrote the 2002-04 gain as the Bie plateau minus Huambo. Added the mirror of unita's 1975 found and 1976 loss: loss of Huambo 1975-11 (c2) and gain 1976-02 (c3, Huambo page: "the MPLA took the city back on 8 February 1976"). Withdrew the guess of 1999-2000.
- unita: added loss of Huambo 1976-02 and 1994-11 (both c3, Huambo page); second Huambo capital now ends 1994; capitals now Huambo 1975-76, Jamba 1976-92 (Jamba page: "Jamba served as UNITA's headquarters from 1976 until 1992"), Huambo 1992-94, Bailundo 1994-99. Keyframes now follow the ledger: 1975 Huambo; 1976-1992 plateau without Huambo; 1993-1994 plateau with Huambo; 1995-2002 plateau without Huambo. Dissolve region and successor land: plateau minus Huambo.
- Thin items tried: Operation Savannah page gave the towns captured in 1975 (Xangongo, Lubango, Moçâmedes, Benguela, Lobito, Luso), so the 1975-76 occupation is now the provinces Cunene, Huíla, Namibe, Benguela and a 50 km disc at Luena (not Cuanza Sul, where the advance was stopped, nor Cuando Cubango); Operation Protea page dates the 1981 occupation of Cunene to August (c3); the Tripartite Accord (Angola) page dates the withdrawal ("left Angola by 30 August 1988"), so the 1988 end is 1988-08. Operation Askari and Lusaka Accords pages opened for the bridge years. The page "Lusaka_Accord" is the 1974 Portugal-FRELIMO accord, not used.

Not applied, and why:
- The optional Bailundo event of October 1999 (and the capture of Jamba on 24 December 1999): the ledger has no earlier UNITA gain of either place to reverse, and the 1994 Angola gain uses the province Huambo as the reviewer prescribed, which already contains Bailundo; the facts are in the capital notes. A gap-filler who draws UNITA's 1994-99 land can add them.
- A drawn UNITA area around Jamba (1976-92) and at Bailundo (1994-99): the Jamba and Andulo pages give no extent, and I would be inventing a radius.
- The reviewer's reading that the 1994 gain is the whole province: kept as prescribed, with the caveat in the event note (Bailundo stayed with UNITA until 1999).

Disagreements between pages: Border War page says the SADF withdrawal "commenced in February 1976 and formally ended a month later"; the Operation Savannah page says the SADF "finally departed Angola in early January 1976" (at Luso); the Border War page's March is kept. Lusaka Protocol: Civil War page "signed ... on 31 October 1994", ceasefire "on 20 November"; Huambo page "The war ended formally on 20 November 1994 with the signature of the Lusaka Protocol".

