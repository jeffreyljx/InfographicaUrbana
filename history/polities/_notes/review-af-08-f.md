# Review of batch af-08-f (Partition and independence, part f)

Reviewer, 2026-10-19 (run 2026-10-20). Dossiers: republic-of-tunisia, ghana, democratic-republic-of-the-congo, federal-republic-of-somalia, guinea, madagascar, state-of-katanga, south-kasai, free-republic-of-the-congo. Neighbour dossiers read (ledger grep): french-africa, british-africa, belgian-congo, ethiopia, republic-of-cote-d-ivoire, republic-of-liberia. The other Context polities of the author's brief section 6 have no file yet (groups not run: french-fifth-republic eu-22, estado-novo eu-21, and the af-08 parts incl. british-gold-coast, italian-africa, zaire).

Mechanical: validator --resolve, 0 errors on all nine before and after the reviewer's edits; warnings only for the slugs british-togoland (ghana /ledger/1) and somaliland (somalia /ledger/5), both listed by the author as counterparts needing dossiers. Every Cliopatria shape has a verdict (Tunisia 6, Ghana 4 + new 1957, DRC 6 + new 1973-1995 on the Zaire shape, Somalia 2, Guinea 2 + new 1958, Madagascar 2). Families exist in colours.json. Capitals inside the shapes' bboxes. Rulers contiguous.

## Verdicts

| slug | verdict | in short |
| --- | --- | --- |
| republic-of-tunisia | pass | 20 Mar 1956, 25 Jul 1957 (infobox), Bizerte 19 Jul 1961 - 15 Oct 1963 all on the pages; area 151,479 vs 163,610 (0.93) |
| ghana | fix (applied) | found region overlapped the British Togoland gain of the same day; reviewer wrote it as Ghana minus Volta |
| democratic-republic-of-the-congo | fix | Sankuru loss dated January 1961 by the reviewer; author to add Equateur to the Second Congo War zones and the 1 August 1964 rename |
| federal-republic-of-somalia | fix (applied) | 1969 rename raised to confidence 2 (intro: 'seized power in 1969 and established the Somali Democratic Republic') |
| guinea | fix | reviewer added the page to six rulers without a source; wikidata Q983 is Equatorial Guinea's id (author to set Guinea's own, believed Q1006, after checking) |
| madagascar | pass | 26 Jun 1960, Dec 1975 (infobox 'Socialist state: 30 December 1975'), area 616,267 vs 592,796 (1.04) |
| state-of-katanga | thin | the January 1962 regain of the Manono strip (c1) is contradicted by its page; extent of the north unknown |
| south-kasai | pass | 9 Aug 1960 (infobox; Congo Crisis 8 Aug), 5 Oct 1962, 'a much smaller portion of territory' all on the pages |
| free-republic-of-the-congo | thin | Sankuru dated January 1961 by the reviewer; the Manono strip loss of January 1962 (c1) is mis-dated |

## Findings

### ghana
- /ledger/0/region (APPLIED). The found region was the whole of Ghana, which already contains the Volta Region gained from british-togoland in /ledger/1 the same day, so the land had two counterparts. Gold Coast page: 'On 6 March 1957, the Colony of Gold Coast gained independence as the state of Ghana'; Ghana page: '... and British Togoland were unified as one single independent dominion'. Rewritten as {"minus": [Ghana, Volta]} exactly like the dossier's own predecessor land; note appended.
- Not a fault, for the record: the British Togoland page says only 'part of which became its Volta Region'; the northern section lies in today's Northern and Upper East regions, so admin1 Volta under-draws the trust territory (confidence 2 is right).

### democratic-republic-of-the-congo
- /ledger/5 (APPLIED). Sankuru loss was undated at confidence 1. Free Republic of the Congo page places 'Gizenga's authority was also established over the Sankuru District of Kasai Province' between 'By 10 January, Stanleyville forces had occupied northern Katanga as far in as Manono' and 'Around then, control had been consolidated in Goma and the northern Kivu region'. Now year 1961, month 1, confidence 2. Mirror free-republic-of-the-congo /ledger/2 changed the same way.
- /ledger/17, /ledger/18 and /wars/3/zones (NOT APPLIED, non-blocking). The note says the MLC's north is 'not named' and is not drawn; the Second Congo War page names it: 'a government offensive in Equateur Province along the Ubangi River was repulsed near Libenge by MLC forces' and the MLC 'was reported in the north of the country' in November 1998. Fix: add {"admin1": "Équateur", "country": "Democratic Republic of the Congo"} (gazetteer spelling) to the contest_start, contest_end and war zones, and correct the note.
- /ledger between 11 and 12 (NOT APPLIED, non-blocking). Missing rename: the DRC infobox has 'Democratic Republic: 1 August 1964' (Republic of the Congo to Democratic Republic of the Congo). Fix: add a rename event 1964-08, confidence 3, source the DRC page.
- Integrator: 'zaire' is listed in section 10 of the author's brief as a state another af-08 part writes; this dossier's new 1973-1995 keyframe points at the Zaire shape. Keep one of the two (the author flagged it).

### federal-republic-of-somalia
- /ledger/2 (APPLIED). Rename to the Somali Democratic Republic at confidence 1; the Somalia intro says Siad Barre 'seized power in 1969 and established the Somali Democratic Republic'. Confidence 2, note extended. No month on the page (the coup was 21 October).

### guinea
- /identity/rulers/1-6 (APPLIED). Six rulers had no source; each read on the Guinea page ('Sékou Touré died on 26 March 1984'; Beavogui 'was to serve as interim president'; Conté 'remained in power until his death on 23 December 2008'; Camara 'seized control in a coup'; 'Sékouba Konaté flew from Lebanon to run the country'; Condé 'won the election' 2010, overthrown 2021; Doumbouya 'seized control of state television', sworn in as interim president 1 October 2021). Source added: https://en.wikipedia.org/wiki/Guinea.
- /identity/wikidata (NOT APPLIED, non-blocking). Q983 is the id Cliopatria also gives equatorial-guinea (data/README.md collision list), and the author's own notes say the two are different states; keeping it gives two dossiers one Wikidata id. Guinea's own item is believed to be Q1006 (Guinea-Bissau is Q1007 in polities.csv); wikidata.org and the page-information view were unreachable for the reviewer, so verify before changing.

### state-of-katanga and free-republic-of-the-congo
- state-of-katanga /ledger/2 and free-republic-of-the-congo /ledger/7 (NOT APPLIED, confidence 1, mis-dated). Both put the return of the Manono strip to Katanga in January 1962. The Free Republic page: 'Gizenga returned to Stanleyville in September 1961 to rally armed forces to retake northern Katanga. The invasion failed', so the Stanleyville forces had already lost the strip before September 1961; the page does not say to whom. The UN Operation in the Congo page has '400 Ethiopians and Indians in Manono' on the eve of Operation Rampunch (August 1961). Fix: date the loss before September 1961 (year 1961, ordered after the January occupation) and name the holder from a page; until then the counterpart state-of-katanga is unsupported.
- state-of-katanga /ledger/1: 'By 10 January, Stanleyville forces had occupied northern Katanga as far in as Manono without facing resistance' (confirmed). 'Without resistance' and the State of Katanga page ('did not enjoy full support throughout the province and was constantly plagued by ethnic strife in its northernmost region') suggest the north was Balubakat land, not Katangese; keyframe note already says the north is unknown.
- free-republic-of-the-congo /ledger/2 (APPLIED): Sankuru, as for the DRC.

## Spot checks (all on the cited page unless said)
- Tunisia: /ledger/0 20 Mar 1956, /ledger/1 'Republic declaration: 25 July 1957' (infobox), /ledger/2 19 Jul 1961 (infobox), /ledger/3-4 'The French finally handed Bizerte over on 15 October 1963'. All confirmed.
- Ghana: /ledger/0 6 Mar 1957 (Gold Coast and Ghana pages), /ledger/1 plebiscite 9 May 1956, 58 percent, 'Annexed ... to form part of the Dominion of Ghana: 6 March 1957', /ledger/2 republic 1 Jul 1960. Confirmed.
- DRC: /ledger/0 30 Jun 1960, /ledger/1 11 Jul 1960, /ledger/9 5 Oct 1962, /ledger/10 17 Jan 1963, /ledger/12 Dragon Rouge 24 Nov 1964, /ledger/13 1971, /ledger/14-15 24 Oct 1996 - May 1997 (Lubumbashi 19 April, Kabila president 17 May), /ledger/17-18 2 Aug 1998 - 18 Jul 2003. Confirmed; /ledger/5 dated by the reviewer.
- Somalia: /ledger/0-1 26 Jun and 1 Jul 1960, /ledger/3-4 '13 July 1977 - 23 March 1978', /ledger/5 May 1991, /ledger/6 August 2012. Confirmed.
- Guinea: /ledger/0 'Guinea declared independence from France on 2 October 1958'. Confirmed.
- Madagascar: /ledger/0 'full independence on 26 June 1960'; /ledger/1 infobox 'Socialist state: 30 December 1975'. Confirmed.
- Katanga: /ledger/0 11 Jul 1960, /ledger/1 'By 10 January', /ledger/3 17 Jan 1963 (infobox 'Dissolution: 21 January 1963'). Confirmed; /ledger/2 contradicted (above).
- South Kasai: /ledger/0 'Unilateral secession: 9 August 1960', /ledger/1 Mulopwe 16 July (1961), /ledger/2-3 'On 5 October 1962, central government troops again arrived in Bakwanga'. Confirmed.
- Free Republic: /ledger/0 12 Dec 1960, /ledger/1 'On 24 December, Stanleyville troops occupied Bukavu', /ledger/4 Manono by 10 Jan 1961, /ledger/5 Maniema (October 1961 paragraph), /ledger/8 'Disestablished: 16 January 1962'. Confirmed.

## Area
Tunisia 151,479 / 163,610 = 0.93; Ghana 240,759 / 240,000 = 1.00; DRC 2,307,837 / 2,345,409 = 0.98; Somalia 646,088 / 637,657 = 1.01; Guinea 245,676 / 245,857 = 1.00; Madagascar 616,267 / 592,796 = 1.04; Katanga gazetteer 411,721 / infobox 496,871 = 0.83 (no Cliopatria row); South Kasai and Free Republic have no infobox area. All acknowledged in keyframe notes.

## Gaps for a gap-filler (thin by budget, not faults)
- DRC: Simba-held extent 1964 (https://en.wikipedia.org/wiki/Simba_rebellion); Shaba I 1977 and Shaba II 1978 (https://en.wikipedia.org/wiki/Shaba_I, https://en.wikipedia.org/wiki/Shaba_II); M23 in Goma Nov-Dec 2012 (https://en.wikipedia.org/wiki/M23_rebellion); Kwilu rebellion (https://en.wikipedia.org/wiki/Kwilu_rebellion).
- Katanga: how much of the north the state held, and who took Manono from the Stanleyville forces in 1961 (https://en.wikipedia.org/wiki/Katanga_Province).
- South Kasai: extent held (https://en.wikipedia.org/wiki/South_Kasai offers none; try https://en.wikipedia.org/wiki/Albert_Kalonji).
- Somalia: Ethiopian intervention 2006-2009 extent (https://en.wikipedia.org/wiki/War_in_Somalia_(2006%E2%80%932009)).
- Madagascar: Scattered Islands claim (https://en.wikipedia.org/wiki/Scattered_Islands_in_the_Indian_Ocean), claim only.

## Cross-dossier matrix
Matched: Tunisia found 1956-03 / french-africa loss 1956-03; DRC found 1960-06 / belgian-congo split 1960-06; Somalia gain 1960-07 / british-africa loss 1960-06; Ogaden contest 1977-07 to 1978-03 both sides with ethiopia; all eleven DRC-rebel pairs (Katanga, South Kasai, Free Republic) and the two Katanga-Free Republic Manono pairs (the 1962 pair mis-dated on both sides). Exceptions (counterpart group not run, or listed as needing a dossier): Ghana found / british-gold-coast; Ghana gain / british-togoland; Somalia found / italian-africa; Somalia loss 1991 / somaliland; Guinea and Madagascar found and Tunisia's Bizerte gain / french-fifth-republic.
