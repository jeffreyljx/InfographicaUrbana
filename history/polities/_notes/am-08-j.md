# am-08-j notes (written 2026-10-19)

Group: six owned states. Four dossiers written (jamaica, republic-of-trinidad-and-tobago, antigua-and-barbuda, barbados), all validate with 0 errors and 0 warnings, also with --resolve. Two owned slugs get no dossier because the earlier-slug dossiers already merged them (see below). Pages opened in this run: Jamaica, Trinidad and Tobago, Antigua and Barbuda, Barbados, West Indies Federation, West Indies Associated States (6 pages, 2 per written state). No page failed.

## communist-cuba (Cliopatria "Communist Cuba", Q241) - no dossier written
history/polities/republic-of-cuba.json already lists both Names ("Republic of Cuba", "Communist Cuba") in cliopatria_names and reviews communist-cuba_1960 and communist-cuba_2024 (verdict ok; validates). Its notes argue one state (the Cuba page has "officially the Republic of Cuba" with no name change, and the 1960 shape is the 1957 shape plus the Sierra Maestra). A second dossier under communist-cuba would double-draw the same shapes, so none was written. Colour agent: map the Name "Communist Cuba" to republic-of-cuba.

## federated-republic-of-brazil (Cliopatria "Federated Republic of Brazil", Q155) - no dossier written
history/polities/brazilian-republic.json already lists all four Names (Brazilian Republic, Unitary State of Brazil, Federated Republic of Brazil, Republic of Brazil) and reviews federated-republic-of-brazil_1967 and _1983 (verdict ok; validates); its ledger has the 1964 coup, the 1967 relabel and the 1985 return of civilians as rename events. One state, one dossier; none written here. Colour agent: map "Federated Republic of Brazil" to brazilian-republic. Things that dossier lists as unopened and I did not touch (not mine): the 1967 constitution date, Fernando de Noronha and Trindade.

## jamaica
- Cliopatria starts Jamaica in 1963; independence was 6 August 1962 (Jamaica page, "Granted: 6 August 1962"). New keyframe jamaica_1962 (1962..1962) repeats the 1963 shape. Shape area 13,346 km2 against infobox 10,991 km2 (ratio 1.21).
- Cliopatria's British Colonial Empire shape holds all 51 Jamaica cells to 1962 and none from 1963: the british-colonial-empire dossier (eu-11) should carry the matching loss in August 1962. The found event names colony-of-jamaica (written in parallel by another agent) as counterpart.
- West Indies Federation: the Jamaica page gives 1958 and "a referendum ... a slight majority voting to leave" without a year; the Federation page gives September 1961 (54 percent), dissolution 31 May 1962. Both opened.
- Disagreement not settled: Cayman Islands and Turks and Caicos "attached to Jamaica" - Federation page says they separated from Jamaica in 1962; the colony-of-jamaica dossier reads 4 July 1959 from the Colony of Jamaica infobox (a page I did not open). Neither is in the Jamaica shape.
- Page silent: any Pedro Bank or Navassa claim; no wars coded.

## republic-of-trinidad-and-tobago
- Cliopatria 1963 start; independence 31 August 1962. New keyframe _1962. Area 6,177 against infobox 5,131 km2 (ratio 1.20). Cliopatria's Name says "Republic" from 1963; the republic is 1 August 1976 (rename event).
- Shape holds 23 of the country's 24 grid cells; the British shape holds the same 23 to 1962. Loss belongs in british-colonial-empire (eu-11).
- Disagreement between pages: the T&T infobox ends the island's Federation province on 14 January 1962 (PNM resolution); the Federation page gives dissolution 31 May 1962. Both recorded.
- Page silent on the Venezuelan maritime treaty and the Barbados arbitration; Cliopatria's neighbour list shows venezuela 1963-2024 within 25 km; no contest coded.

## antigua-and-barbuda
- Start 1967 (associated state, 27 February 1967) follows Cliopatria and the page; sovereign 1 November 1981 is a rename event (same state, same colour). The associated-state period 1967-1981 is a UK client relation: the vassal_start (1967) and vassal_end (1981), counterpart "antigua-and-barbuda", belong in the british-colonial-empire dossier (eu-11).
- Cliopatria's shape (586 km2, 6 vertices, bbox 16.94-17.19 N) is Antigua only; Barbuda and Redonda are outside it although the page makes both part of the state (union with Antigua 1 August 1860; Redonda 26 March 1872, parish of Saint John). Verdict adjust for both shapes: union with admin1 Barbuda and admin1 Redonda (both resolve in the gazetteer). Cliopatria's British shape holds neither cell, so those two cells have no Cliopatria source state.
- Overlap 1967-1968: the British shape still holds Antigua's cell (and Barbados' cell).
- Infobox area 440 km2 against 586 (ratio 1.33).
- Page silent: Barbuda secession moves before the recent, undated movement; the Redonda Annexation Act is undated.

## barbados
- Cliopatria 1967 start; independence 30 November 1966 (Barbados page, infobox "30 November 1966"); new keyframe barbados_1966. Republic 30 November 2021 (rename event). Area 735 km2 against infobox 439 km2 (ratio 1.67, inside a factor of two).
- British shape keeps Barbados' cell to 1968: overlap 1967-1968, loss should be dated November 1966 in the british-colonial-empire dossier.
- The Federation page gives Barbados' independence only as "1966"; the day rests on the Barbados page.

## For other groups
- Colonial predecessors with no dossier (Cliopatria has no row; the am-08-x scope names them): colony of Trinidad and Tobago (1797 capitulation, 1802 cession, 1889 union of the two islands, per the T&T page), colony of Barbados (first settlement 17 February 1627), Antigua (Leeward Islands colony). Until they exist, the found events use british-colonial-empire as counterpart.
- west-indies-federation and colony-of-jamaica exist (another agent); west-indies-federation lists republic-of-trinidad-and-tobago as successor. It does not list barbados or antigua-and-barbuda (it names british-colonial-empire for the remaining islands to 1962).
- Gazetteer: every name used resolves; none needed.
