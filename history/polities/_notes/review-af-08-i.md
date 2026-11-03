# Review: batch af-08-i (2026-10-25)

Reviewer: adversarial review of seven dossiers (af-08-i, Partition and independence part i). Validator: 0 errors on all seven; 3 warnings, all the gazetteer name 'Kagera Salient' (tanzania). Machine copy of this review: history/notes/phase-b/reviews/af-08-i.json.

## Verdicts
- republic-of-senegal: pass. Tried: 20 Aug 1960 secession (Mali Federation page, midnight session), infobox 196,722 km2 vs 200,762 (1.02), Senegambia 1 Feb 1982 - 30 Sep 1989, Casamance since 1982 / 30 Dec 2004 / unfinished 2025, Dakar 14°40'N 17°25'W. Mirror: mali-federation split 1960-08. Nothing broke.
- republic-of-the-congo: pass. Confirmed 15 Aug 1960, People's Republic 31 Dec 1969 - 15 Mar 1992 (infobox), last-quarter-1998 militia seizures, 29 Dec 1999 surrender of 2,000 Ninja and Cocoye rebels; infobox 342,000 km2 vs 345,888 (1.01). Thin: wikidata null (Q971 unverifiable), the 1993-94 war, the June-October 1997 Brazzaville fighting not recorded as a contest.
- republic-of-the-niger: pass. Confirmed 3 Aug 1960, 18 Dec 1958, 2005 ICJ award (16 islands to Niger, nine to Benin; 24 islands in the earlier sentence), Tuareg rebellions 1990-95 and 2007-09; infobox 1,267,000 km2 vs 1,178,830 (0.93). Thin: the 2013 ICJ Burkina Faso-Niger frontier judgment is not on the Niger page (reviewer's recollection; pixel-scale).
- sierra-leone: pass. Confirmed 27 Apr 1961, 19 Apr 1971, 23 Mar 1991, 'large swathes ... eastern and southern', March 1993 recapture of Koidu and Kono, 'by 1994 ... much of the diamond-rich Eastern Province', 18 Jan 2002; area 73,252 vs 74,220 (1.01). Thin: the confidence-1 return of rebel areas in 2002.
- revolutionary-united-front: thin (by design, three pages). All five spot checks confirmed, including 'In 2001, UN forces moved into rebel-held areas'. Missing: ground held 1995-2000 (January 1995 SIEROMCO/Sierra Rutile seizures, RUF base near Bo destroyed in 1996, May 1997 - March 1998 AFRC junta in Freetown), no headquarters, Lome accord dated both 27 March and 7 July 1999 on the civil war page.
- tanzania: fix (two fixes applied by the reviewer, file re-validated):
  1. /ledger/2 counterpart sultanate-of-zanzibar -> people-s-republic-of-zanzibar-and-pemba. The sultanate dossier ends with the 12 Jan 1964 revolution; the People's Republic dossier now exists and records merge 1964-04 with tanzania; the Tanganyika page: 'officially joined with the People's Republic of Zanzibar' on 26 April 1964.
  2. /ledger/6 occupation_start moved 1979-01 -> 1979-04. The Uganda-Tanzania War page: Kampala 'secured' on 11 April, 'In the following months, the TPDF occupied Uganda'; republic-of-uganda has contest Jan-Apr and occupation from April. The occupation of all of Uganda from the 21 January crossing overstated the land.
  Not applied, non-blocking, for the orchestrator:
  3. Kagera Salient: contest here, occupation in republic-of-uganda (L2/L3), same land and dates. Pick one type for both.
  4. Mafia Island: british-east-africa loses it to tanzania 1961-12 (its L1), but tanzania names only british-africa as predecessor and its 1961/1963 keyframes lack the island (in Cliopatria it sits in BEA 1961-62 and probably in the Zanzibar shape 1963-66). Add british-east-africa as predecessor (land: Mafia Island) and say so in K0/K1. Under 0.1% of the area.
  Thin: occupation_end (confidence 1; the war page is silent on the withdrawal, confirmed); the Tanzania page does give presidents with years (Nyerere 1962-1985, Mwinyi 1985-1995, Mkapa 1995-2005, Kikwete 2005-2015, Magufuli 2015-2021, Samia since 2021), contrary to the notes, so rulers could be added; Lake Nyasa not on the page.
  Confirmed: 9 Dec 1961, 9 Dec 1962, 26 Apr 1964 (Articles 22 Apr, Act 25 Apr), 29 Oct 1964, Kagera (30 Oct / 1 Nov 1978, 1,900 km2, 'By early January' ejected), Dodoma official 1996; infobox 947,303 km2 vs 886,212 (0.94).
- people-s-democratic-republic-of-algeria: pass. Confirmed 5 Jul 1962, Sand War from 25 Sep 1963, posts of Hassi Beida and Tindjoub, Tindouf offensive 13 Oct, ceasefire 30 Oct, Malian officer 4 Nov, 'No territorial changes', OAU treaty 20 Feb 1964, ratification 1989; dispute over 'portions of Algeria's Tindouf and Béchar provinces' (zone at confidence 2 is honest); infobox 2,381,741 km2 vs 2,323,775 (0.98).

## Cross-dossier matrix
| event | mirror | status |
| --- | --- | --- |
| senegal 1960 found <- mali-federation | mali-federation 1960-08 split | matched |
| congo 1960 found <- french-fifth-republic | none (eu-22 not run; FEA -> FFR 1958) | exception |
| niger 1960 found <- french-fifth-republic | none (eu-22 not run; FWA -> FFR 1958) | exception |
| niger 2005 gain <- republic-of-benin | none in republic-of-benin.json | missing: route to Benin's author (loss 2005, islands) |
| sierra-leone 1961 found <- british-africa | british-africa ends 1960 (successor listed) | exception (inherited Cliopatria gap) |
| sierra-leone <-> RUF 1991 loss, 1993 gain, 1994 loss, 2002 gain | RUF gain/loss/gain/loss, same months | matched |
| tanzania 1961 found <- british-africa | british-africa successor tanzania, ends 1960 | exception |
| british-east-africa 1961 loss (Mafia) -> tanzania | tanzania found, no BEA predecessor | mismatch (small) |
| tanzania 1964 gain <- PR Zanzibar and Pemba | merge 1964-04 | matched after fix |
| tanzania 1978 contest (Kagera) | uganda 1978-10 occupation_start | mismatch on type |
| tanzania 1979-04 occupation_start / 1979-06 end (Uganda) | uganda 1979-04 / 1979-06 | matched after fix |
| algeria 1962 found <- french-fifth-republic | none (eu-22) | exception |
| algeria 1963 Sand War contest (morocco) | morocco.json: war, no zone, no contest | mismatch: route to af-02; the Sand War page supports a contest |

## Gazetteer
- Kagera Salient (region), tanzania.

## Counterparts still without dossiers
- armed-forces-revolutionary-council (1997-1998), senegambia-confederation (umbrella 1982-1989), alliance-of-sahel-states (umbrella 2023-). The People's Republic of Zanzibar now exists as people-s-republic-of-zanzibar-and-pemba.
