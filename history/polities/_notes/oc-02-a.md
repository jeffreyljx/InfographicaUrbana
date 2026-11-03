# Notes from batch oc-02-a (Australia, New Zealand and the colonial Pacific, part a)

Run of 2026-10-18. Pages opened (WebFetch, 13 distinct): Australia, Territory of Papua, Territory of New Guinea, New Guinea campaign, Australian Antarctic Territory, Papua New Guinea, Bougainville Civil War, New Zealand, Realm of New Zealand, Western Samoa Trust Territory, Republic of Hawaii, New Hebrides, New Caledonia. No page failed. Dossiers written and validated (0 errors): commonwealth-of-australia, papua-new-guinea, new-zealand, republic-of-hawai-i, new-hebrides, new-caledonia, plus the rebel state bougainville-interim-government. Python run as `python3 -I history/tools/validate_dossier.py <file> --resolve`; the only warnings are the gazetteer's (see the end) and counterpart slugs with no dossier yet.

## commonwealth-of-australia

- Cliopatria row 1905-2024 is the mainland and Tasmania; it begins four years after federation (1 January 1901), omits Papua (1906) and the New Guinea mandate (1914 occupation, 17 December 1920), draws the Allied-held part of New Guinea in 1943-1945 (and 50 and 292 cells of Indonesian New Guinea in 1944 and 1945, which was Dutch), and carries 34 cells of Papua New Guinea (29 on Bougainville) from 1946 to 2023, overlapping the Papua New Guinea row from 1976. Keyframes rebuilt: 1901, 1906, 1920 (also for 1943-1945), 1946 (to 1975), 1976.
- Papua/New Guinea split into provinces is mine (no page gives the boundary); Southern Highlands is in neither 1906-1919 shape.
- Undated, therefore not entered: Norfolk Island, Christmas Island, Cocos (Keeling), Ashmore and Cartier, Coral Sea Islands, Heard and McDonald; the Northern Territory (1911) and ACT (1911) are internal. Pages to try: 'Territories of Australia', 'Norfolk Island', 'Cocos (Keeling) Islands', 'Christmas Island', 'Heard Island and McDonald Islands'. All are 1-5 cells.
- The Antarctic Territory (24 August 1936, about 5.9 M km2, claim recognised by four states) is entered as a gain, but the grid has no Antarctic cells and the region name 'Australian Antarctic Territory' is not in the gazetteer.
- The 1942-1945 contest zones use the New Guinea provinces whole; the page dates only some captures (Buna, Gona, Sanananda by 22 January 1943; Salamaua-Lae to 16 September 1943; Huon Peninsula to 1 March 1944; New Britain to 21 August 1945; campaign end 15 August 1945). Hollandia, Aitape, Sansapor and Wewak are not on the page.
- Page disagreements: mandate 17 December 1920 (Territory of New Guinea) against 9 or 19 May 1921 (Papua New Guinea page); independence 15 September (two territory pages) against 16 September 1975 (PNG page, used). Papua: letters patent 18 March 1902, Papua Act commencing 1 September 1906 (used), 'took over the administration ... in 1905' (Australia page).
- Counterpart slugs to be written by oc-02-x (guessed from slugify): colony-of-new-south-wales, colony-of-victoria, colony-of-queensland, colony-of-south-australia, colony-of-western-australia, colony-of-tasmania, british-new-guinea, german-new-guinea. empire-of-japan (jk-01) should mirror the 1942-1945 contest.

## papua-new-guinea

- Cliopatria 1946-1975 is the Territory of Papua and New Guinea (administrative union 1 July 1949), not a state: verdict wrong, land carried by commonwealth-of-australia; the state begins on 16 September 1975 (new keyframe 1975). The 1946 shape also misses 91 cells of the modern country (all of Bougainville, parts of New Ireland, New Britain and Milne Bay), 31 of which are in Australia's 1946 row. If the project would rather draw the territory as a type colony under its own name, this dossier's 1946 verdict can be reversed, but then Australia must stop holding the land.
- The 1 September 1975 declaration of independence by 'the government of Bougainville' is on the PNG page without name, end or land; not entered. Page to try: 'Republic of the North Solomons'.
- The BRA/BIG held Bougainville from early 1990: written as the rebel dossier bougainville-interim-government (Bougainville Civil War page only). Not on the page: the day of the May 1990 declaration, the capital, the end of the BIG (the end year 2001 is the peace agreement; the ABG was elected in 2005), the March 1990 withdrawal date. The PNG-held 'north and southwest' of 1991-92 is a contest over the whole province, not a drawn zone.

## new-zealand

- Written as the Dominion/Realm from 26 September 1907; the Colony of New Zealand (1841-1907, the New Zealand Wars, Kermadec 1886) is left to colony-of-new-zealand (oc-02-x). Cliopatria's row starts the year after the Statute of Westminster Adoption Act (25 November 1947) and lacks the Chatham Islands and every dependency; the direct shape is rebuilt in steps 1907, 1920, 1925, 1948, 1962, 1965, 1974.
- The first two pages are silent on Western Samoa; a third page (Western Samoa Trust Territory) was opened (over the 1-2 page budget). The page gives no exact day for the August 1914 landing or for independence in 1962.
- Not on any page: the Ross Dependency limits, the previous holder of Tokelau (kingdom-of-great-britain is a reading), the dates of the Chatham and subantarctic islands. Free-association clients (Cook Islands 1965, Niue 1974) are entered as vassal_start without a vassal_end (relation continues); their dossiers (cook-islands, niue) and german-samoa and samoa do not exist yet.

## republic-of-hawai-i

- One page. Cliopatria 1895-1897 is the Kingdom's last shape; the page gives 4 July 1894 to 12 August 1898, so keyframes for 1894 and 1898 are added. The page has no area and says nothing about islands beyond the main group. The 1893 treaty and its failure are not on the page.

## new-hebrides

- One page (opened twice). Type colony, jointly ruled; the British and French dossiers should record it as a shared colony and not hold the land directly. Cliopatria 1890-1982 and Vanuatu from 1983 leave 1981-1982 to this row though independence was 30 July 1980 (verdict cuts it). Not on the page: the American base at Espiritu Santo, the 1980 Santo secession, the 1914 protocol, any area. Franceville (9 August 1889 to June 1890) has no dossier.

## new-caledonia

- One page. The Cliopatria 'New Caledonia' row (1856-1859) is a French overseas aggregate, mislabelled (see the dossier); both shapes are declared wrong and replaced by the island group from 1853. The aggregate may duplicate french-india and french-indochina; the France dossiers' authors should check. The capital's early history and the dating of the Loyalty Islands and Isle of Pines annexations are not on the page. Free France 1940 changes no border.

## Gazetteer names needed

- Buka (place, island north of Bougainville, Papua New Guinea; used in papua-new-guinea and bougainville-interim-government).
- Ross Dependency (region, New Zealand's Antarctic claim; used in new-zealand; no land cells in the grid).
- Australian Antarctic Territory (region, Antarctic sector 45 E-160 E south of 60 S excluding Adelie Land; used in commonwealth-of-australia; no land cells in the grid).
