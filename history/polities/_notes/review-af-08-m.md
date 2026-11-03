# Review of batch af-08-m (2026-10-24)

Reviewer: adversarial review, Phase B. Validator (`--resolve --json`): all eight dossiers valid, no errors; one warning (seychelles /ledger/1/region "Outer Islands" resolves to no cells, a grid/gazetteer issue). Spot checks were made with WebFetch on the pages cited; every quoted sentence that was checked is on its page with the year given. No reviewer edits were made to any dossier.

| slug | verdict |
| --- | --- |
| people-s-republic-of-angola | fail (missing 1994 regain of Huambo) |
| unita | fail (missing 1976 and 1994 losses of Huambo; KF0 to KF1 unexplained) |
| republic-of-cabo-verde | pass |
| sao-tome-and-principe | pass |
| seychelles | pass |
| republic-of-djibouti | pass |
| zimbabwe-rhodesia | pass |
| front-for-the-restoration-of-unity-and-democracy | pass |

## people-s-republic-of-angola: fail

Blocking (not applied):
- /ledger/6 (1993-03 loss of Huambo to unita, c3) has no reversal before /ledger/8 (2002-04 gain of the Bie plateau). As written, Huambo province is out of Angola from 1993 to 2002. The Huambo page (https://en.wikipedia.org/wiki/Huambo): "A large offensive gave back to the Government the control of Huambo on 9 November" (1994; the conflict "flared up again in August 1994"). The Angolan Civil War page the author opened already says: "the government's military successes in 1994 forced UNITA to sue for peace" and "By November 1994, the government had taken control of 60% of the country." Fix: add {year 1994, month 11, type gain, counterpart unita, region {admin1 Huambo, country Angola}, confidence 3, source https://en.wikipedia.org/wiki/Huambo}, add the Huambo page to sources; the notes' guess "retaking of Huambo (1999-2000?)" is wrong and should go. Optional: the same page has "The Government retook the town of Bailundo in October 1999" (UNITA's later stronghold in Huambo province), a candidate 1999-10 event if a Bailundo region is drawn.

Thin (gap-filler):
- /ledger/1 (1975 South African occupation, c2, Cunene): the Border War page says "By early November, the three SADF columns had captured eighteen major towns and cities" and "penetrated more than 500 km into Angola"; Cunene alone understates Operation Savannah. Page to try: https://en.wikipedia.org/wiki/Operation_Savannah_(Angola).
- /ledger/4 and /ledger/5 (1981 and 1988, c1, Cunene as a bridge): page to try https://en.wikipedia.org/wiki/Operation_Protea (Ondjiva/Xangongo, August 1981) and the Lusaka Accord withdrawal.

Checked and holding: found 11 November 1975 (Angola infobox "Granted: 11 November 1975"; Alvor Agreement sentence); 9 August 1975 Calueque, 25 October decision, withdrawal "commenced in February 1976 and formally ended a month later" (Border War page); Huambo 55-day battle, control 7 March 1993, "By August 1993, UNITA had gained control over 70% of Angola"; infobox 11 November 1975 - 4 April 2002 (Civil War page); April 2002 ceasefire and August 2002 armed wing given up (UNITA page). Area: infobox 1,246,700 km2 against 1,257,376 km2 (ratio 1.01), acknowledged. The Cabinda adjustment of the 2024 shape is right (2024 bbox stops at 5.89 S). Predecessor portuguese-angola dissolves on 1975-11 to this slug: matched.

## unita: fail

Blocking (not applied):
- /keyframe_review/0 (1975, Huambo) to /keyframe_review/1 (1976-2002, Bie plateau): no ledger event explains the loss of Huambo. Huambo page: "However, the MPLA took the city back on 8 February 1976 with the help of Cuban troops." Fix: add {year 1976, month 2, type loss, counterpart people-s-republic-of-angola, region {admin1 Huambo, country Angola}, confidence 3, source https://en.wikipedia.org/wiki/Huambo}. If Angola keeps the 1975 found of UNITA at Huambo without a loss, no Angola mirror is needed; otherwise add the matching gain in Angola.
- After /ledger/2 (1993-03 gain of Huambo): no loss of Huambo before the 2002 dissolve. Huambo page: government control of Huambo restored "on 9 November" 1994. Fix: add {year 1994, month 11, type loss, counterpart people-s-republic-of-angola, region {admin1 Huambo, country Angola}, confidence 3, source Huambo page}; end the second Huambo capital in 1994, not 1993 (/identity/capitals/1 "to": 1994).

Thin:
- /identity/capitals: gap 1976-1991 (Jamba, Cuando Cubango: "UNITA later moved to Jamba in Angola's southeastern province of Cuando Cubango", no year on the UNITA page). Page to try: https://en.wikipedia.org/wiki/Jamba,_Cuando_Cubango.
- /keyframe_review/1: UNITA's solid territory in the 1980s was the south-east (Cuando Cubango) around Jamba, not only the Bie plateau; the 1994-1999 strongholds were Bailundo and Andulo ("The Government retook the town of Bailundo in October 1999", Huambo page). Pages to try: Jamba page, https://en.wikipedia.org/wiki/Andulo.

Checked and holding: "UNITA also was nearly destroyed in November 1975", the Huambo government, "controlled much of the highland's interior, notably the Bie Plateau", the April 2002 ceasefire and August 2002 end of the armed wing (UNITA page); Huambo 1993 (Civil War page). Type rebel and family africa are right. Note: the author lists the "Democratic People's Republic of Angola" as needing its own dossier, but this dossier already carries it in alt_names and as KF0; a separate dossier would double the 1975 Huambo land.

## republic-of-cabo-verde: pass

Tried: found 5 July 1975 (infobox "Granted: 5 July 1975"; "received instruments of independence from Portugal on 5 July 1975"), 1462 settlement at Santiago, 1951 overseas province, Praia capital since 1770, ten islands: all on the Cape Verde page. Area: infobox 4,033 km2 against 9,427 km2 (ratio 2.34), acknowledged and resolved by removing the Comoros (shapes.csv modern_countries "Cabo Verde;Comoros", bbox to 45.15 E). Remark (not blocking): the note's "the gap being the Comoros" does not add up (9,427 - 1,659 = 7,768, still 1.9 times the infobox); the remaining excess is within a factor of two. No union with Guinea-Bissau on the page, so none recorded: correct. Could not break it.

## sao-tome-and-principe: pass

Tried: "Granted: 12 July 1975", the Pinto da Costa sentence, settlements 1493 and 1500, the 2001 joint exploration agreement with Nigeria (no border change): all on the page. Area 964 km2 against 1,485 km2 (ratio 1.54), acknowledged. One page within the 1-2 page budget; no border event exists to miss.

## seychelles: pass

Tried: "Independence declared: 29 June 1976"; "In 1976, Seychelles gained independence from the United Kingdom as a republic"; "Seychelles became a separate crown colony from Mauritius in 1903" (Seychelles page); "On 23 June 1976, these islands were returned to the Seychelles, which became independent as a republic on 29 June 1976" (BIOT page, also giving 8 November 1965 for the detachment). Area 457 km2 against 258.6 km2 (ratio 0.57), acknowledged; the misplaced Cliopatria shape is the known problem and is adjusted. /ledger/1 could be confidence 3 (the page names the islands and the day). The gain's counterpart kingdom-of-great-britain has no dossier (owned by a European group that has not run yet); BIOT is listed as needing a dossier.

## republic-of-djibouti: pass

Tried: "Independence from France: 27 June 1977", the 8 May 1977 referendum and 98.8%, infobox 23,200 km2 (Djibouti page); 21 November 1991 Obock assault, "The FRUD seized all military posts in the north of the country and laid siege to the city of Tadjoura and Obock" (undated, 3-4 January 1992 and February 1992 around it), 5 July 1993 counter-offensive, 26 December 1994 Abb'a agreement, 12 May 2001 (Civil War page). Area ratio 0.95, acknowledged. Mirrors with the FRUD dossier all match. Thin, optional: the 2008 Eritrean occupation of Ras Doumeira (not on the pages opened; small; no keyframe moves): https://en.wikipedia.org/wiki/Djiboutian%E2%80%93Eritrean_border_conflict. Note the Civil War infobox gives 31 October 1991 - 26 December 1994; the contest_start in 1991-11 is dated by the Obock assault, acceptable.

## zimbabwe-rhodesia: pass

Tried: "existed from 1 June 1979 to 18 April 1980", the 11 December 1979 law quotation, Lancaster House "signed on 21 December 1979", "Capital: Salisbury", no area on the page (Zimbabwe Rhodesia page); "a civil conflict from July 1964 to December 1979", infobox 4 July 1964 - 12 December 1979, ceasefire 21 December 1979, "Under the agreement of March 1978, the country was renamed Zimbabwe-Rhodesia" (Bush War page). The end in 1979 is argued from the page's own law quotation and the 1980-82 Cliopatria years are handed on: honest. Mirror: republic-of-zimbabwe found 1980-04 from zimbabwe-rhodesia (within one year; Dec 1979 - Apr 1980 British rule is noted in successors).

## front-for-the-restoration-of-unity-and-democracy: pass

Tried: all six events against the Civil War and FRUD pages (founded 1991; Obock 21 November 1991; the seized northern posts; 5 July 1993; 26 December 1994 at Aba'a; radical wing's agreement in 2001). Obock + Tadjourah as "the north" is a wide reading and carried at confidence 2 with soft certainty: honest. Thin, optional: no capital (Assa-Gueyla base has no coordinates); the 1991 and 1994 years have no keyframe (contest only).

## Cross-dossier matrix

- Angola found 1975-11 from portuguese-angola: portuguese-angola /ledger/28 dissolve 1975-11 to this slug: matched.
- Angola occupation_start/end by south-africa 1975-11, 1976-03, 1981, 1988: south-africa.json exists and has no event naming Angola: missing on the south-africa side (af-08 part that owns south-africa).
- Angola contest_start 1975-11 / unita contest_start 1975-11: matched. Angola loss 1993-03 / unita gain 1993-03: matched. contest_end 2002-04 both: matched. Angola gain 2002-04 / unita dissolve 2002-04: exception (dissolve stands for the loss).
- Missing on both sides: Huambo back to the government 1994-11 (and unita's 1976-02 loss).
- Djibouti / FRUD: contest_start 1991-11, loss/gain 1992, gain/loss 1993-07, contest_end 1994-12: all matched.
- Djibouti found from french-fifth-republic, Cabo Verde and Sao Tome found from estado-novo, Seychelles found and gain from kingdom-of-great-britain: no dossier yet (groups eu-22, eu-21 and the UK's European group not run): exception.
- zimbabwe-rhodesia found from rhodesia (af-08 part not yet written): exception; dissolve 1979-12 to republic-of-zimbabwe, whose found is 1980-04: matched.

## Gazetteer

Outer Islands (Seychelles admin1) resolves to no cells; the author's list (Aldabra, Farquhar Group, Desroches, Jamba, Calueque, Assa-Gueyla, Mount Mabla) stands; add Bailundo (place, Huambo province) and Andulo (place, Bie province) for the UNITA fixes.
