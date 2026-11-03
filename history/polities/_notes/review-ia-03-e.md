# Review of batch ia-03-e (2026-10-19)

Reviewer: adversarial review, Phase B. Dossiers: durrani-empire, emirate-of-bukhara, emirate-of-afghanistan, durrani-dynasty. Neighbours read: khanate-of-bukhara, khanate-of-khiva, khanate-of-kokand, kazakh-khanate (the other Context polities are not written yet). Validator: 0 errors in all four; warnings are only counterpart slugs of states with no dossier yet (all in the author's counterparts list).

| slug | verdict | blocking |
| --- | --- | --- |
| durrani-empire | fail | /ledger/22 Balkh 1768 at confidence 3 |
| emirate-of-bukhara | thin | none (one keyframe fix, missing mirrors) |
| emirate-of-afghanistan | thin | none (three small fixes, the north undated) |
| durrani-dynasty | fail | /ledger/3-4 give Kandahar to the emirate in 1843 |

## durrani-empire: fail

1. /ledger/22 (blocking). The 1768 gain of Balkh from khanate-of-bukhara (confidence 3) is wrong in year and counterpart. Ahmad Shah Durrani page: Hajji Bi of Maimana sought Ahmad Shah's aid "to reclaim Balkh" in 1751 and was made "governor of Balkh"; by summer 1752 "Balkh was restored to the rule of the Maimana Khanate"; in 1755-1756 Ahmad Shah "declared a new governor of Balkh, Nawab Khan Alakozai". In 1768 Shah Murad invaded, Ahmad Shah advanced "affirming his authority in ... Balkh", and Shah Murad "recognized Afghan control over Balkh". Balkh came from the Qataghanids in 1752, not from Bukhara in 1768; khanate-of-bukhara has no 1768 loss; the 1757 keyframe already holds Balkh. Fix: Balkh gained summer 1752 (counterpart Qataghan, or inside the Maimana vassal region with direct rule from 1755-56); 1768 becomes a contest_start/contest_end with khanate-of-bukhara with no land change.
2. /ledger/14. Nishapur 1755: the page has Abbas Quli of the "Qara Bayat Amirdom" submit on 17 June 1755, the city rebel, a one-week siege, "The city was then plundered", and Abbas Quli "allowed to return to Nishapur as governor". The note's "took the city" is not on the page; the counterpart is not Afsharid Iran; the corrections 1752-1794 take Razavi Khorasan out entirely, so the gain is never drawn. Fix: vassal_start Qara Bayat Amirdom 1755 (end 1796), or keep Nishapur in the corrections.
3. /ledger/23 and /ledger/24 (applied by the reviewer). The note quoted "Within 1769"; the page says "Within the year, Ahmad Shah occupied Badakhshan and Sultan Shah was executed" after a letter of December 1769. Confidence 3 lowered to 2, quote corrected, file re-validated.
4. /keyframe_review/4-7. Sind and Baluchistan are removed as vassal land, but Badakhshan (vassal 1753-1769), the Maimana lands (vassal from 1752) and Kunduz (no event) stay in as direct land from 1757. Treat them alike or explain.
5. Thin: no events for the north, Hazarajat and the Derajat leaving before the 1818 keyframe; Lahore/eastern Punjab before 1772; Multan 1772-1818; the 1823 vassal ends (confidence 1: the Principality of Kandahar page has Sindh and Balochistan breaking away "in August 1826"); Nishapur 1796 (confidence 1).
6. Confirmed on the page: /ledger/5, 10, 13, 19, 36, 37, 38, 42. Area: infobox about 2,000,000 km2 (no year) against Cliopatria 2,195,448 (1763), ratio 0.91, acknowledged.

## emirate-of-bukhara: thin

1. /keyframe_review/9 (non-blocking fix). The 1868-1917 keyframe is the whole 1918 shape with Gorno-Badakhshan, while all earlier corrections remove it and /ledger/10 gains it c. 1878; make it minus Gorno-Badakhshan.
2. Missing mirrors of written neighbours: occupation of Kokand June-August 1842 (khanate-of-kokand /ledger/11-12), Uroteppa contest 1788-1866 (kokand /ledger/6, /ledger/21), Khiva strip October 1873 (khanate-of-khiva /ledger/21), Tashqurghan 1850 (emirate-of-afghanistan /ledger/6 names this state as loser). The author flagged all but the last.
3. Thin: Gorno-Badakhshan gained whole for "Darvaz (c 1878)"; Shughnan, Roshan and Karategin undated; the emir's rump in Eastern Bukhara after 31 August 1920; Shahrisabz c 1870 already inside every shape; no vassal events for the Russian protectorate (left to russian-empire, the open convention question).
4. Confirmed: /ledger/0, 1, 4, 6, 7, 8, 11, 13. Area: no infobox area; the successor BPSR has 182,193 km2 (1922) against Cliopatria 1919 218,997, ratio 0.83, acknowledged.

## emirate-of-afghanistan: thin

1. /ledger/19. Same region spec as /ledger/18 (Cliopatria 1895 minus 1894), so the same cells are gained twice; give the 1895 Bashgal/Nasrat cession its own region or merge.
2. /ledger/6. Tashqurghan 1850 "from emirate-of-bukhara": the Dost Mohammad page names no loser; the First Anglo-Afghan War infobox lists Tashqurghan (Khulm) and the Maimana Khanate as belligerents of their own; Bukhara has no mirror; and Samangan is already in every keyframe from 1828.
3. /ledger/12. The Gandamak cessions (Quetta+120 km) lie outside every keyframe (cut to modern Afghanistan), so Pishin and Sibi are never drawn as lost; add them to the 1846-1879 corrections or say so.
4. Thin: the 1823-1827 to 1828 keyframe jump has no gain events; the north and Hazarajat are kept as "unverified: page budget" against the page's own list of separate states; land mismatch with durrani-dynasty in August 1839; Third Anglo-Afghan War, Wakhan 1895, Dokalim 1912.
5. Confirmed: /ledger/3, 4, 8, 9, 10, 12, 16 (the Panjdeh circle covers Kushka and Ak-Tepe, the page's two ends). Area: no infobox area; Cliopatria 644,005.

## durrani-dynasty: fail

1. /ledger/3, /ledger/4, /identity/successors/0 (blocking). Kandahar, Helmand and Uruzgan go to emirate-of-afghanistan in April 1843 at confidence 3, but the Principality of Kandahar infobox has "Liberation of Kandahar: 9 August 1842", the emirate dossier excludes Kandahar until November 1855, and this dossier's own successor text says Kohan Dil Khan re-established the principality. Fix: 1842-08 loss of Kandahar, Helmand and Uruzgan to principality-of-kandahar; the 1843 loss and dissolve cover Kabul and Ghazni only; add principality-of-kandahar to successors; cut Kandahar from the 1842 keyframe after August.
2. /keyframe_review/1 (non-blocking). The 1839 keyframe (Kabul, Ghazni, Kandahar) and the 1840 keyframe (all Afghanistan without Herat and Nuristan) differ by about 0.4 M km2 with no event; make them agree.
3. Confirmed: /ledger/0, 1, 2; /ledger/3 for Kabul only. Area: no area on the Durrani dynasty page.

## Cross-dossier matrix (summary)

Matched: khanate-of-bukhara dissolve 1785 / emirate-of-bukhara found 1785; emirate-of-bukhara loss 1823 / khanate-of-khiva gain 1823 (Merv); durrani-empire dissolve 1823 / emirate-of-afghanistan found 1823.
Mismatched (land): emirate-of-afghanistan loss 1839-08 / durrani-dynasty found 1839-08; emirate-of-afghanistan gain 1843-04 / durrani-dynasty loss 1843-04 (Kandahar).
Missing: durrani-empire occupation 1763 (no mirror in khanate-of-kokand: route to its author); durrani-empire gain 1768 (no loss in khanate-of-bukhara; the fix is in durrani-empire); khanate-of-khiva loss 1873-10, khanate-of-kokand occupation 1842 and contest 1788-1866 (no mirror in emirate-of-bukhara); emirate-of-afghanistan gain 1850 (no loss in emirate-of-bukhara).
Exceptions: every event with afsharid-iran, qajar-dynasty (me-10), mughal-empire, sikh-confederacy, sikh-empire, talpur-dynasty, maratha-empire (sa-05), british-raj (sa-06), russian-empire (eu-17), kingdom-of-afghanistan (not run), and the states in the author's counterparts list.
