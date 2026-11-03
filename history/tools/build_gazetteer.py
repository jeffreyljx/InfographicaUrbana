#!/usr/bin/env python3
"""Build gazetteer v0 (data/gazetteer/*.jsonl) from Natural Earth 10m and the H3 land grid.

Run from a scratch directory:  python3 -I tools/build_gazetteer.py [countries|admin1|rivers|lakes|places|all]

Inputs (downloaded by the gazetteer agent, 18 Oct 2026):
    /tmp/claude-0/work/gazetteer/ne_10m_admin_0_countries/        258 countries and territories
    /tmp/claude-0/work/gazetteer/ne_10m_admin_1_states_provinces/ 4,596 first-level units
    /tmp/claude-0/work/gazetteer/ne_10m_rivers_lake_centerlines/  1,473 line segments
    /tmp/claude-0/work/gazetteer/ne_10m_lakes/                    1,355 lakes
    /tmp/claude-0/work/gazetteer/ne_10m_populated_places/         7,342 places
    data/grid/land_r5.txt                                         the land grid (tools/grid.py)

Outputs, one JSON object per line, cells as runs of indices into data/grid/land_r5.txt
(the anchors' convention: "start-end" inclusive or a single integer; grid.from_runs expands):
    countries.jsonl  {name, iso_a3, adm0_a3, alt_names, n_cells, cells}
    admin1.jsonl     {name, country, adm0_a3, iso, type, region, alt_names, n_cells, cells}
    rivers.jsonl     {name, alt_names, n_cells, cells}        cells the line passes through
    lakes.jsonl      {name, alt_names, n_cells, cells}        cells whose centre is on the lake
    places.jsonl     {name, country, lon, lat, pop, cell, alt_names, source}

Cells of a country, province or lake are the land cells whose centre falls inside it
(grid.shape_cells, which also keeps the centroid cell of a unit smaller than one cell).
A river's cells are the land cells its centreline passes through (sampled every ~1 km).
A place's cell is the land cell containing the point, or the nearest land cell within two
rings for a coastal point whose own cell centre is at sea (then "cell_moved": true).

Knowledge added by the agent: EXTRA_PLACES (historical cities absent from Natural Earth,
coordinates to about 0.05 degree, "source": "knowledge") and the alias tables below.
"""
import collections
import json
import math
import os
import sys
import time
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import h3  # noqa: E402
import shapefile  # noqa: E402  (pyshp)
from shapely.geometry import shape  # noqa: E402

import grid  # noqa: E402

OUT = HERE.parent / "data" / "gazetteer"
WORK = Path("/tmp/claude-0/work/gazetteer")
RES = grid.RES

LATIN = ["de", "es", "fr", "it", "nl", "pt", "sv", "pl", "hu", "tr", "id", "vi"]

# ----------------------------------------------------------------------------
# Knowledge tables
# ----------------------------------------------------------------------------

COUNTRY_ALIASES = {
    "Czechia": ["Czech Republic", "Czechoslovakia"],
    "Myanmar": ["Burma"],
    "eSwatini": ["Swaziland", "Eswatini"],
    "Iran": ["Persia"],
    "Thailand": ["Siam"],
    "Sri Lanka": ["Ceylon"],
    "Ethiopia": ["Abyssinia"],
    "Cambodia": ["Kampuchea"],
    "Dem. Rep. Congo": ["Zaire", "Belgian Congo", "DRC", "Congo-Kinshasa", "DR Congo"],
    "Congo": ["Congo-Brazzaville", "French Congo"],
    "Benin": ["Dahomey"],
    "Ghana": ["Gold Coast"],
    "Burkina Faso": ["Upper Volta"],
    "Zimbabwe": ["Rhodesia", "Southern Rhodesia"],
    "Zambia": ["Northern Rhodesia"],
    "Malawi": ["Nyasaland"],
    "Tanzania": ["Tanganyika"],
    "Namibia": ["South West Africa"],
    "Taiwan": ["Formosa"],
    "Mongolia": ["Outer Mongolia"],
    "Jordan": ["Transjordan"],
    "Belize": ["British Honduras"],
    "Guyana": ["British Guiana"],
    "Suriname": ["Dutch Guiana", "Surinam"],
    "Indonesia": ["Dutch East Indies", "Netherlands Indies"],
    "Bangladesh": ["East Pakistan", "East Bengal"],
    "Timor-Leste": ["East Timor"],
    "North Macedonia": ["Macedonia (country)", "Republic of Macedonia", "FYROM"],
    "United Kingdom": ["Britain", "Great Britain", "UK", "U.K."],
    "United States of America": ["United States", "USA", "US", "U.S.", "U.S.A."],
    "Russia": ["Russian Federation", "Soviet Union (Russia)"],
    "S. Sudan": ["South Sudan"],
    "W. Sahara": ["Western Sahara", "Spanish Sahara"],
    "N. Cyprus": ["Northern Cyprus", "Turkish Republic of Northern Cyprus"],
    "Bosnia and Herz.": ["Bosnia", "Bosnia-Herzegovina"],
    "Côte d'Ivoire": ["Ivory Coast", "Cote d'Ivoire"],
    "Vatican": ["Holy See", "Vatican City"],
    "Palestine": ["West Bank and Gaza", "Palestinian territories"],
    "Faeroe Is.": ["Faroe Islands", "Faroes"],
    "Netherlands": ["Holland", "The Netherlands"],
    "Germany": ["Deutschland"],
    "Turkey": ["Türkiye", "Turkiye"],
    "Vietnam": ["Viet Nam"],
    "Laos": ["Lao PDR"],
    "Syria": ["Syrian Arab Republic"],
    "South Korea": ["Korea, South", "Republic of Korea"],
    "North Korea": ["Korea, North", "DPRK"],
    "Macao": ["Macau"],
    "Brunei": ["Brunei Darussalam"],
    "Cabo Verde": ["Cape Verde"],
    "Gambia": ["The Gambia"],
    "Bahamas": ["The Bahamas"],
    "Eq. Guinea": ["Equatorial Guinea"],
    "Central African Rep.": ["Central African Republic", "CAR", "Ubangi-Shari"],
    "Dominican Rep.": ["Dominican Republic"],
    "Fr. Polynesia": ["French Polynesia", "Tahiti"],
    "New Caledonia": ["Nouvelle-Calédonie"],
    "Solomon Is.": ["Solomon Islands"],
    "Marshall Is.": ["Marshall Islands"],
    "Cook Is.": ["Cook Islands"],
    "Pitcairn Is.": ["Pitcairn Islands"],
    "Turks and Caicos Is.": ["Turks and Caicos Islands"],
    "Cayman Is.": ["Cayman Islands"],
    "U.S. Virgin Is.": ["United States Virgin Islands", "US Virgin Islands"],
    "British Virgin Is.": ["British Virgin Islands"],
    "St. Kitts and Nevis": ["Saint Kitts and Nevis"],
    "St. Vin. and Gren.": ["Saint Vincent and the Grenadines"],
    "Antigua and Barb.": ["Antigua and Barbuda"],
    "St. Pierre and Miquelon": ["Saint Pierre and Miquelon"],
    "St-Martin": ["Saint Martin"],
    "St-Barthélemy": ["Saint Barthelemy"],
    "Fr. S. Antarctic Lands": ["French Southern and Antarctic Lands"],
    "Heard I. and McDonald Is.": ["Heard Island and McDonald Islands"],
    "Br. Indian Ocean Ter.": ["British Indian Ocean Territory", "Chagos"],
    "Indian Ocean Ter.": ["Indian Ocean Territories", "Christmas Island and Cocos"],
    "U.S. Minor Outlying Is.": ["United States Minor Outlying Islands"],
    "Wallis and Futuna Is.": ["Wallis and Futuna"],
    "Åland": ["Aland", "Aland Islands"],
    "Hong Kong": ["Hong Kong S.A.R."],
    "Greenland": ["Kalaallit Nunaat"],
    "Egypt": ["Misr"],
    "Morocco": ["Maroc", "Al-Maghrib"],
    "Algeria": ["Algérie"],
    "Libya": ["Libia"],
    "Lebanon": ["Liban"],
    "Spain": ["España"],
    "Hungary": ["Magyarország"],
    "Austria": ["Österreich"],
    "Switzerland": ["Schweiz", "Suisse", "Helvetia"],
    "Ireland": ["Éire", "Eire", "Republic of Ireland"],
    "Japan": ["Nippon", "Nihon"],
    "China": ["People's Republic of China", "PRC"],
    "India": ["Bharat"],
    "Pakistan": ["West Pakistan"],
    "Israel": ["Eretz Israel"],
    "Saudi Arabia": ["Saudi"],
    "United Arab Emirates": ["UAE", "Trucial States"],
    "Ukraine": ["Ukraina"],
    "Belarus": ["Byelorussia", "White Russia"],
    "Moldova": ["Moldavia (republic)"],
    "Georgia": ["Sakartvelo"],
    "Armenia": ["Hayastan"],
    "Kyrgyzstan": ["Kirghizia"],
    "Tajikistan": ["Tadzhikistan"],
    "Turkmenistan": ["Turkmenia"],
    "Uzbekistan": ["Uzbek SSR"],
    "Kazakhstan": ["Kazakh SSR"],
    "Serbia": ["Republic of Serbia"],
    "Montenegro": ["Crna Gora"],
    "Croatia": ["Hrvatska"],
    "Slovenia": ["Slovenija"],
    "Slovakia": ["Slovak Republic"],
    "Poland": ["Polska"],
    "Lithuania": ["Lietuva"],
    "Latvia": ["Latvija"],
    "Estonia": ["Eesti"],
    "Finland": ["Suomi"],
    "Sweden": ["Sverige"],
    "Norway": ["Norge"],
    "Denmark": ["Danmark"],
    "Iceland": ["Ísland"],
    "Greece": ["Hellas", "Ellada"],
    "Albania": ["Shqipëria"],
    "Bulgaria": ["Bălgarija"],
    "Romania": ["România", "Rumania"],
    "Cyprus": ["Kypros"],
    "Malta": ["Melita"],
    "Portugal": ["Portucale"],
    "Mexico": ["México"],
    "Peru": ["Perú"],
    "Brazil": ["Brasil"],
    "Haiti": ["Saint-Domingue"],
    "Philippines": ["Pilipinas", "Philippine Islands"],
    "Papua New Guinea": ["PNG"],
    "New Zealand": ["Aotearoa"],
    "Australia": ["Commonwealth of Australia"],
    "Somaliland": ["British Somaliland"],
    "Somalia": ["Italian Somaliland"],
    "Djibouti": ["French Somaliland"],
    "Eritrea": ["Eritrea (Italian)"],
    "Mozambique": ["Portuguese East Africa"],
    "Angola": ["Portuguese West Africa"],
    "Madagascar": ["Malagasy Republic"],
    "Lesotho": ["Basutoland"],
    "Botswana": ["Bechuanaland"],
    "Mali": ["French Sudan"],
    "Guinea-Bissau": ["Portuguese Guinea"],
    "Guinea": ["French Guinea"],
    "Sierra Leone": [],
    "Togo": ["Togoland"],
    "Cameroon": ["Kamerun", "Cameroun"],
    "Gabon": [],
    "Uganda": ["Buganda (protectorate)"],
    "Kenya": ["British East Africa"],
    "Rwanda": ["Ruanda"],
    "Burundi": ["Urundi"],
    "Iraq": ["Irak"],
    "Kuwait": ["Koweit"],
    "Oman": ["Muscat and Oman"],
    "Yemen": ["North and South Yemen"],
    "Bahrain": ["Bahrein"],
    "Qatar": [],
    "Afghanistan": [],
    "Nepal": [],
    "Bhutan": ["Druk Yul"],
    "Maldives": ["Maldive Islands"],
    "Malaysia": ["Malaya (federation)"],
    "Singapore": ["Singapura", "Temasek"],
    "Fiji": ["Fiji Islands"],
    "Tonga": ["Friendly Islands"],
    "Samoa": ["Western Samoa"],
    "Vanuatu": ["New Hebrides"],
    "Kiribati": ["Gilbert Islands"],
    "Tuvalu": ["Ellice Islands"],
    "Puerto Rico": ["Porto Rico"],
    "Cuba": [],
    "Jamaica": [],
    "Trinidad and Tobago": ["Trinidad"],
    "Guatemala": [],
    "Honduras": [],
    "El Salvador": [],
    "Nicaragua": [],
    "Costa Rica": [],
    "Panama": ["Panamá"],
    "Colombia": ["New Granada (republic)"],
    "Venezuela": [],
    "Ecuador": [],
    "Bolivia": ["Upper Peru"],
    "Chile": [],
    "Argentina": ["Argentine Republic"],
    "Uruguay": ["Banda Oriental"],
    "Paraguay": [],
    "Canada": ["Dominion of Canada"],
    "Italy": ["Italia"],
    "France": ["République française"],
    "Belgium": ["Belgique", "België"],
    "Luxembourg": ["Luxemburg"],
    "Liechtenstein": [],
    "Monaco": [],
    "Andorra": [],
    "San Marino": [],
    "Gibraltar": [],
    "Isle of Man": ["Mann"],
    "Jersey": [],
    "Guernsey": [],
}

# aliases for places that Natural Earth has under their modern name; keyed by the NE NAME
# (ascii-insensitive) and the NE ADM0NAME
PLACE_ALIASES = {
    ("Istanbul", "Turkey"): ["Constantinople", "Byzantium", "Konstantinopolis", "Tsargrad"],
    ("Xian", "China"): ["Chang'an", "Xi'an", "Changan", "Daxing", "Haojing"],
    ("Luxor", "Egypt"): ["Thebes (Egypt)", "Waset", "Diospolis Magna", "Karnak"],
    ("Hotan", "China"): ["Khotan", "Yutian"],
    ("Kuqa", "China"): ["Kucha", "Kuche", "Qiuci"],
    ("Turpan", "China"): ["Turfan"],
    ("Trabzon", "Turkey"): ["Trebizond", "Trapezus", "Trapezunt"],
    ("Edirne", "Turkey"): ["Adrianople", "Hadrianopolis"],
    ("Izmir", "Turkey"): ["Smyrna"],
    ("Antakya", "Turkey"): ["Antioch", "Antiochia", "Antioch on the Orontes"],
    ("Thessaloniki", "Greece"): ["Salonica", "Thessalonica", "Salonika", "Selanik"],
    ("Durrës", "Albania"): ["Dyrrachium", "Durazzo", "Epidamnos", "Durres"],
    ("Kaliningrad", "Russia"): ["Königsberg", "Konigsberg", "Królewiec"],
    ("Gdańsk", "Poland"): ["Danzig", "Gdansk"],
    ("Wrocław", "Poland"): ["Breslau", "Wroclaw"],
    ("Lviv", "Ukraine"): ["Lwów", "Lemberg", "Lvov", "Lwow"],
    ("Szczecin", "Poland"): ["Stettin"],
    ("Volgograd", "Russia"): ["Tsaritsyn", "Stalingrad"],
    ("Saint Petersburg", "Russia"): ["Petrograd", "Leningrad", "St. Petersburg", "St Petersburg"],
    ("St. Petersburg", "Russia"): ["Petrograd", "Leningrad", "Saint Petersburg"],
    ("Sanliurfa", "Turkey"): ["Edessa", "Urfa", "Şanlıurfa"],
    ("Tokyo", "Japan"): ["Edo"],
    ("Shenyang", "China"): ["Mukden", "Shengjing", "Fengtian"],
    ("Guangzhou", "China"): ["Canton", "Panyu"],
    ("Jakarta", "Indonesia"): ["Batavia", "Sunda Kelapa", "Jayakarta"],
    ("Yangon", "Myanmar"): ["Rangoon", "Dagon"],
    ("Kolkata", "India"): ["Calcutta"],
    ("Mumbai", "India"): ["Bombay"],
    ("Chennai", "India"): ["Madras"],
    ("Patna", "India"): ["Pataliputra"],
    ("Nusaybin", "Turkey"): ["Nisibis"],
    ("Ho Chi Minh City", "Vietnam"): ["Saigon", "Gia Dinh", "Prey Nokor"],
    ("Mexico City", "Mexico"): ["Tenochtitlan", "México-Tenochtitlan", "Ciudad de México", "Tenochtitlán"],
    ("Cusco", "Peru"): ["Cuzco", "Qosqo"],
    ("Hamadan", "Iran"): ["Ecbatana", "Hagmatana"],
    ("Kayseri", "Turkey"): ["Caesarea", "Mazaca", "Caesarea Mazaca"],
    ("Konya", "Turkey"): ["Iconium", "Ikonion"],
    ("Erzurum", "Turkey"): ["Theodosiopolis", "Karin"],
    ("Malatya", "Turkey"): ["Melitene"],
    ("Diyarbakir", "Turkey"): ["Amida", "Diyarbakır"],
    ("Samsun", "Turkey"): ["Amisos", "Amisus"],
    ("Sinop", "Turkey"): ["Sinope"],
    ("Bursa", "Turkey"): ["Prusa"],
    ("Ankara", "Turkey"): ["Ancyra", "Angora"],
    ("Balkh", "Afghanistan"): ["Bactra", "Zariaspa"],
    ("Herat", "Afghanistan"): ["Aria", "Alexandria Ariana"],
    ("Kandahar", "Afghanistan"): ["Alexandria Arachosia", "Qandahar"],
    ("Samarkand", "Uzbekistan"): ["Maracanda", "Afrasiab", "Samarqand"],
    ("Bukhara", "Uzbekistan"): ["Bokhara", "Buxoro"],
    ("Tashkent", "Uzbekistan"): ["Chach", "Shash", "Binkath"],
    ("Beijing", "China"): ["Peking", "Dadu", "Khanbaliq", "Zhongdu", "Yanjing", "Beiping", "Jicheng"],
    ("Nanjing", "China"): ["Nanking", "Jiankang", "Jinling", "Yingtian", "Jianye"],
    ("Hangzhou", "China"): ["Lin'an", "Hangchow"],
    ("Kaifeng", "China"): ["Bianjing", "Bianliang", "Daliang", "Dongjing"],
    ("Luoyang", "China"): ["Loyang"],
    ("Datong", "China"): ["Pingcheng"],
    ("Taiyuan", "China"): ["Jinyang"],
    ("Anyang", "China"): ["Yin", "Yinxu"],
    ("Chengdu", "China"): ["Chengtu"],
    ("Hanoi", "Vietnam"): ["Thang Long", "Thăng Long", "Dong Kinh", "Jiaozhi", "Đại La"],
    ("Hue", "Vietnam"): ["Phu Xuan", "Huế"],
    ("Nha Trang", "Vietnam"): ["Kauthara"],
    ("Bago", "Myanmar"): ["Pegu", "Hanthawaddy"],
    ("Bangkok", "Thailand"): ["Thonburi", "Krung Thep"],
    ("Seoul", "South Korea"): ["Hanseong", "Hanyang", "Wiryeseong", "Gyeongseong", "Keijo"],
    ("Kaesong", "North Korea"): ["Gaegyeong", "Songdo"],
    ("Nara", "Japan"): ["Heijo-kyo", "Heijō"],
    ("Kyoto", "Japan"): ["Heian-kyo", "Heian", "Miyako"],
    ("Osaka", "Japan"): ["Naniwa"],
    ("Fukuoka", "Japan"): ["Hakata"],
    ("Naha", "Japan"): ["Shuri"],
    ("Cairo", "Egypt"): ["Fustat", "Al-Qahira", "Heliopolis"],
    ("Alexandria", "Egypt"): ["Iskandariya", "Alexandria (Egypt)"],
    ("Aswan", "Egypt"): ["Syene", "Elephantine"],
    ("Algiers", "Algeria"): ["Al-Jaza'ir", "Icosium", "Alger"],
    ("Tripoli", "Libya"): ["Oea", "Tarabulus", "Tripoli (Libya)"],
    ("Marrakesh", "Morocco"): ["Marrakech"],
    ("Fez", "Morocco"): ["Fès", "Fas"],
    ("Mogadishu", "Somalia"): ["Muqdisho"],
    ("Axum", "Ethiopia"): ["Aksum"],
    ("Kumasi", "Ghana"): ["Coomassie"],
    ("Benin City", "Nigeria"): ["Edo (city)", "Ubinu"],
    ("Timbuktu", "Mali"): ["Tombouctou", "Timbuctoo"],
    ("Gao", "Mali"): ["Kawkaw"],
    ("Zanzibar", "Tanzania"): ["Unguja", "Stone Town"],
    ("Mombasa", "Kenya"): ["Mvita"],
    ("Rome", "Italy"): ["Roma"],
    ("Milan", "Italy"): ["Milano", "Mediolanum"],
    ("Venice", "Italy"): ["Venezia", "Venetia"],
    ("Florence", "Italy"): ["Firenze", "Florentia"],
    ("Naples", "Italy"): ["Napoli", "Neapolis"],
    ("Genoa", "Italy"): ["Genova", "Genua"],
    ("Turin", "Italy"): ["Torino", "Augusta Taurinorum"],
    ("Syracuse", "Italy"): ["Siracusa", "Syracusae"],
    ("Marseille", "France"): ["Massalia", "Massilia", "Marseilles"],
    ("Lyon", "France"): ["Lugdunum", "Lyons"],
    ("Paris", "France"): ["Lutetia"],
    ("Reims", "France"): ["Rheims", "Durocortorum"],
    ("Cologne", "Germany"): ["Köln", "Colonia Agrippina", "Koln"],
    ("Vienna", "Austria"): ["Wien", "Vindobona"],
    ("Prague", "Czechia"): ["Praha"],
    ("Prague", "Czech Republic"): ["Praha"],
    ("Bratislava", "Slovakia"): ["Pressburg", "Pozsony"],
    ("Budapest", "Hungary"): ["Buda", "Pest", "Ofen", "Aquincum"],
    ("Belgrade", "Serbia"): ["Beograd", "Singidunum"],
    ("Belgrade", "Republic of Serbia"): ["Beograd", "Singidunum"],
    ("Sofia", "Bulgaria"): ["Serdica", "Sredets"],
    ("Plovdiv", "Bulgaria"): ["Philippopolis"],
    ("Skopje", "Macedonia"): ["Üsküb", "Scupi"],
    ("Skopje", "North Macedonia"): ["Üsküb", "Scupi"],
    ("Split", "Croatia"): ["Spalato", "Aspalathos"],
    ("Dubrovnik", "Croatia"): ["Ragusa"],
    ("Zadar", "Croatia"): ["Zara"],
    ("Pula", "Croatia"): ["Pola"],
    ("Kotor", "Montenegro"): ["Cattaro"],
    ("Shkodër", "Albania"): ["Scutari", "Shkodra", "Shkoder"],
    ("Vlorë", "Albania"): ["Valona", "Vlora", "Aulon", "Vlore"],
    ("Bucharest", "Romania"): ["București"],
    ("Iasi", "Romania"): ["Jassy", "Iași"],
    ("Chisinau", "Moldova"): ["Kishinev", "Chișinău"],
    ("Kiev", "Ukraine"): ["Kyiv"],
    ("Kyiv", "Ukraine"): ["Kiev"],
    ("Odessa", "Ukraine"): ["Odesa", "Hacıbey"],
    ("Dnipro", "Ukraine"): ["Dnipropetrovsk", "Yekaterinoslav"],
    ("Dnipropetrovsk", "Ukraine"): ["Dnipro", "Yekaterinoslav"],
    ("Kharkiv", "Ukraine"): ["Kharkov"],
    ("Kerch", "Ukraine"): ["Panticapaeum"],
    ("Kerch", "Russia"): ["Panticapaeum"],
    ("Feodosiya", "Ukraine"): ["Caffa", "Kaffa", "Theodosia", "Feodosia"],
    ("Feodosiya", "Russia"): ["Caffa", "Kaffa", "Theodosia", "Feodosia"],
    ("Kazan", "Russia"): ["Qazan"],
    ("Astrakhan", "Russia"): ["Hajji Tarkhan", "Xacitarxan"],
    ("Moscow", "Russia"): ["Moskva"],
    ("Novgorod", "Russia"): ["Veliky Novgorod", "Holmgard"],
    ("Tbilisi", "Georgia"): ["Tiflis"],
    ("Yerevan", "Armenia"): ["Erivan", "Erevan"],
    ("Baku", "Azerbaijan"): ["Bakı"],
    ("Ganja", "Azerbaijan"): ["Gandzak", "Elisabethpol", "Kirovabad"],
    ("Derbent", "Russia"): ["Bab al-Abwab", "Darband"],
    ("Tabriz", "Iran"): ["Tauris"],
    ("Tehran", "Iran"): ["Teheran"],
    ("Isfahan", "Iran"): ["Esfahan", "Ispahan", "Spahan"],
    ("Esfahan", "Iran"): ["Isfahan", "Ispahan", "Spahan"],
    ("Qazvin", "Iran"): ["Kazvin"],
    ("Mashhad", "Iran"): ["Meshed"],
    ("Neyshabur", "Iran"): ["Nishapur", "Nishabur"],
    ("Gorgan", "Iran"): ["Jurjan", "Astarabad"],
    ("Zaranj", "Afghanistan"): ["Zarang"],
    ("Ghazni", "Afghanistan"): ["Ghazna"],
    ("Peshawar", "Pakistan"): ["Purushapura"],
    ("Multan", "Pakistan"): ["Mulasthana"],
    ("Delhi", "India"): ["Dilli", "Indraprastha", "Shahjahanabad"],
    ("Agra", "India"): ["Akbarabad"],
    ("Allahabad", "India"): ["Prayagraj", "Prayag"],
    ("Varanasi", "India"): ["Benares", "Kashi", "Banaras"],
    ("Hyderabad", "India"): ["Golconda", "Bhagyanagar"],
    ("Bijapur", "India"): ["Vijayapura"],
    ("Mysore", "India"): ["Mysuru"],
    ("Kozhikode", "India"): ["Calicut"],
    ("Kochi", "India"): ["Cochin"],
    ("Thiruvananthapuram", "India"): ["Trivandrum"],
    ("Puducherry", "India"): ["Pondicherry"],
    ("Colombo", "Sri Lanka"): ["Kolamba"],
    ("Kandy", "Sri Lanka"): ["Senkadagala"],
    ("Dhaka", "Bangladesh"): ["Dacca", "Jahangirnagar"],
    ("Vientiane", "Laos"): ["Viangchan"],
    ("Luang Prabang", "Laos"): ["Louangphabang", "Muang Sua"],
    ("Melaka", "Malaysia"): ["Malacca"],
    ("Palembang", "Indonesia"): ["Srivijaya"],
    ("Makassar", "Indonesia"): ["Ujung Pandang", "Gowa"],
    ("Manila", "Philippines"): ["Maynila", "Tondo"],
    ("Singapore", "Singapore"): ["Temasek", "Singapura"],
    ("Ulaanbaatar", "Mongolia"): ["Urga", "Ulan Bator", "Niislel Khüree"],
    ("Hohhot", "China"): ["Huhehaote", "Guihua"],
    ("Guatemala City", "Guatemala"): ["Kaminaljuyu", "Guatemala"],
    ("Quito", "Ecuador"): ["Kitu"],
    ("Cuenca", "Ecuador"): ["Tomebamba"],
    ("Lima", "Peru"): ["Ciudad de los Reyes"],
    ("Sucre", "Bolivia"): ["La Plata", "Chuquisaca", "Charcas"],
    ("Santo Domingo", "Dominican Republic"): ["Ciudad Trujillo"],
    ("Havana", "Cuba"): ["La Habana"],
    ("New York", "United States of America"): ["New Amsterdam", "Manhattan", "New York City"],
    ("Albany", "United States of America"): ["Fort Orange", "Beverwijck"],
    ("Pittsburgh", "United States of America"): ["Fort Duquesne", "Fort Pitt"],
    ("Detroit", "United States of America"): ["Fort Detroit", "Fort Pontchartrain"],
    ("Chicago", "United States of America"): ["Fort Dearborn"],
    ("Winnipeg", "Canada"): ["Fort Garry", "Red River Colony"],
    ("Québec", "Canada"): ["Quebec City", "Stadacona", "Quebec"],
    ("Quebec", "Canada"): ["Quebec City", "Stadacona", "Québec"],
    ("Montréal", "Canada"): ["Montreal", "Ville-Marie", "Hochelaga"],
    ("Montreal", "Canada"): ["Montréal", "Ville-Marie", "Hochelaga"],
    ("Jacksonville", "United States of America"): ["Fort Caroline"],
    ("Veracruz", "Mexico"): ["Villa Rica de la Vera Cruz"],
    ("Mérida", "Mexico"): ["T'ho", "Merida (Yucatan)"],
    ("Toledo", "Spain"): ["Toletum"],
    ("Córdoba", "Spain"): ["Cordoba", "Corduba", "Qurtuba"],
    ("Seville", "Spain"): ["Sevilla", "Hispalis", "Ishbiliya"],
    ("Granada", "Spain"): ["Gharnata"],
    ("Zaragoza", "Spain"): ["Saragossa", "Caesaraugusta", "Saraqusta"],
    ("Cádiz", "Spain"): ["Gades", "Cadiz"],
    ("Tarragona", "Spain"): ["Tarraco"],
    ("Mérida", "Spain"): ["Emerita Augusta", "Merida (Spain)"],
    ("Lisbon", "Portugal"): ["Lisboa", "Olisipo"],
    ("Porto", "Portugal"): ["Oporto", "Portus Cale"],
    ("London", "United Kingdom"): ["Londinium"],
    ("York", "United Kingdom"): ["Jorvik", "Eboracum"],
    ("Chester", "United Kingdom"): ["Deva"],
    ("Bath", "United Kingdom"): ["Aquae Sulis"],
    ("Trondheim", "Norway"): ["Nidaros"],
    ("Tartu", "Estonia"): ["Dorpat"],
    ("Tallinn", "Estonia"): ["Reval"],
    ("Klaipėda", "Lithuania"): ["Memel", "Klaipeda"],
    ("Klaipeda", "Lithuania"): ["Memel"],
    ("Toruń", "Poland"): ["Thorn", "Torun"],
    ("Poznań", "Poland"): ["Posen", "Poznan"],
    ("Turku", "Finland"): ["Åbo", "Abo"],
    ("Vyborg", "Russia"): ["Viipuri", "Viborg"],
    ("Plzeň", "Czechia"): ["Pilsen", "Plzen"],
    ("Plzeň", "Czech Republic"): ["Pilsen", "Plzen"],
    ("Niš", "Serbia"): ["Naissus", "Nis"],
    ("Niš", "Republic of Serbia"): ["Naissus", "Nis"],
    ("Veliko Tarnovo", "Bulgaria"): ["Tarnovo", "Turnovo", "Tarnovgrad"],
    ("Bilhorod-Dnistrovskyi", "Ukraine"): ["Akkerman", "Cetatea Albă", "Tyras"],
    ("Alor Setar", "Malaysia"): ["Kedah (town)"],
    ("Bandar Seri Begawan", "Brunei"): ["Brunei Town", "Brunei (city)"],
    ("Banda Aceh", "Indonesia"): ["Aceh (city)", "Kutaraja"],
    ("Surakarta", "Indonesia"): ["Solo"],
    ("Mazar-i-Sharif", "Afghanistan"): ["Mazar-e Sharif", "Mazar"],
    ("Mary", "Turkmenistan"): ["Merv (modern town)"],
    ("Urgench", "Uzbekistan"): ["Urganch", "New Urgench"],
    ("Dushanbe", "Tajikistan"): ["Stalinabad"],
    ("Almaty", "Kazakhstan"): ["Alma-Ata", "Verny"],
    ("Astana", "Kazakhstan"): ["Nur-Sultan", "Akmola", "Tselinograd"],
    ("Bishkek", "Kyrgyzstan"): ["Frunze", "Pishpek"],
    ("Ashgabat", "Turkmenistan"): ["Ashkhabad", "Poltoratsk"],
    ("Khujand", "Tajikistan"): ["Leninabad", "Khodjent", "Alexandria Eschate"],
    ("Taraz", "Kazakhstan"): ["Talas (city)", "Dzhambul", "Aulie-Ata"],
    ("Termez", "Uzbekistan"): ["Tirmidh", "Termiz"],
    ("Urumqi", "China"): ["Ürümqi", "Dihua"],
    ("Ürümqi", "China"): ["Urumqi", "Dihua"],
    ("Kashgar", "China"): ["Kashi", "Shule"],
    ("Hami", "China"): ["Kumul", "Qomul"],
    ("Dunhuang", "China"): ["Shazhou"],
    ("Zhangye", "China"): ["Ganzhou"],
    ("Wuwei", "China"): ["Liangzhou", "Guzang"],
    ("Lanzhou", "China"): ["Jincheng"],
    ("Xining", "China"): ["Shanzhou"],
    ("Lhasa", "China"): ["Lasa"],
    ("Dali", "China"): ["Taihe", "Yangjumie"],
    ("Kunming", "China"): ["Yunnanfu", "Tuodong"],
    ("Nanning", "China"): ["Yongzhou"],
    ("Fuzhou", "China"): ["Foochow", "Minzhou"],
    ("Quanzhou", "China"): ["Zaiton", "Zayton"],
    ("Xiamen", "China"): ["Amoy"],
    ("Ningbo", "China"): ["Mingzhou"],
    ("Suzhou", "China"): ["Wu (city)", "Gusu"],
    ("Yangzhou", "China"): ["Guangling"],
    ("Wuhan", "China"): ["Hankou", "Wuchang", "Hanyang"],
    ("Changsha", "China"): [],
    ("Jinan", "China"): [],
    ("Qufu", "China"): ["Lu (capital)"],
    ("Handan", "China"): ["Zhao (capital)"],
    ("Linzi", "China"): ["Qi (capital)"],
    ("Zibo", "China"): ["Linzi"],
    ("Xianyang", "China"): ["Qin capital"],
    ("Liaoyang", "China"): ["Dongjing (Liao)", "Xiangping"],
    ("Harbin", "China"): [],
    ("Changchun", "China"): ["Hsinking", "Xinjing"],
    ("Dalian", "China"): ["Dairen", "Port Arthur", "Lüshun"],
    ("Taipei", "Taiwan"): ["Taihoku"],
    ("Tainan", "Taiwan"): ["Fort Zeelandia", "Taiwan-fu"],
    ("Pyongyang", "North Korea"): ["Pyeongyang", "Heijo"],
    ("Gyeongju", "South Korea"): ["Seorabeol", "Gyeongju (Silla)"],
    ("Busan", "South Korea"): ["Pusan"],
    ("Incheon", "South Korea"): ["Chemulpo"],
    ("Hakodate", "Japan"): [],
    ("Sapporo", "Japan"): [],
    ("Kagoshima", "Japan"): ["Satsuma (castle town)"],
    ("Nagasaki", "Japan"): ["Dejima"],
    ("Kamakura", "Japan"): [],
}

# Historical places absent from Natural Earth: (name, country, lat, lon, [alt names]).
# Coordinates from the agent's knowledge, about 0.05 degree.
EXTRA_PLACES = [
    # Central Asia, Iran, Caucasus
    ("Merv", "Turkmenistan", 37.66, 62.19, ["Marv", "Alexandria Margiana", "Antiochia in Margiana", "Marw"]),
    ("Gurganj", "Turkmenistan", 42.33, 59.15, ["Konye-Urgench", "Old Urgench", "Kunya-Urgench", "Urganj"]),
    ("Nisa", "Turkmenistan", 37.99, 58.19, ["Parthaunisa", "Mithradatkert"]),
    ("Karakorum", "Mongolia", 47.20, 102.85, ["Kharkhorin", "Qaraqorum", "Karakoram (Mongolia)"]),
    ("Ai-Khanoum", "Afghanistan", 37.16, 69.41, ["Alexandria on the Oxus", "Ai Khanum"]),
    ("Maimana", "Afghanistan", 35.92, 64.78, ["Maymana", "Meymaneh"]),
    ("Shibarghan", "Afghanistan", 36.67, 65.75, ["Sheberghan"]),
    ("Khost", "Afghanistan", 33.34, 69.92, []),
    ("Bamyan", "Afghanistan", 34.82, 67.83, ["Bamiyan"]),
    ("Panjakent", "Tajikistan", 39.50, 67.61, ["Penjikent", "Panjikent"]),
    ("Otrar", "Kazakhstan", 42.85, 68.30, ["Farab", "Utrar"]),
    ("Balasagun", "Kyrgyzstan", 42.75, 75.25, ["Burana", "Quz Ordu"]),
    ("Suyab", "Kyrgyzstan", 42.80, 75.20, ["Ak-Beshim"]),
    ("Almaliq", "China", 44.13, 80.80, ["Almalik", "Almalyk"]),
    ("Beshbalik", "China", 44.08, 89.20, ["Beiting", "Bishbaliq"]),
    ("Gaochang", "China", 42.85, 89.53, ["Qocho", "Karakhoja", "Kara-Khoja"]),
    ("Karashahr", "China", 42.06, 86.57, ["Yanqi", "Agni"]),
    ("Khara-Khoto", "China", 41.77, 101.15, ["Heicheng", "Etzina"]),
    ("Shangdu", "China", 42.36, 116.18, ["Xanadu", "Kaiping"]),
    ("Linhuang", "China", 43.97, 119.24, ["Shangjing (Liao)", "Liao Shangjing", "Bairin Left Banner"]),
    ("Huining", "China", 45.52, 126.98, ["Shangjing (Jin)", "Jin Shangjing", "Acheng"]),
    ("Ji'an", "China", 41.13, 126.19, ["Gungnae", "Guonei", "Jian (Goguryeo)"]),
    ("Ye", "China", 36.33, 114.65, ["Yecheng", "Linzhang"]),
    ("Rey", "Iran", 35.59, 51.43, ["Rayy", "Rhages", "Shahr-e Rey", "Ray"]),
    ("Soltaniyeh", "Iran", 36.43, 48.80, ["Sultaniyya", "Sultaniyeh", "Soltaniyya"]),
    ("Tus", "Iran", 36.49, 59.52, ["Tous"]),
    ("Hecatompylos", "Iran", 36.17, 54.35, ["Shahr-e Qumis", "Damghan"]),
    ("Susa", "Iran", 32.19, 48.26, ["Shush", "Shushan"]),
    ("Shushtar", "Iran", 32.05, 48.86, []),
    ("Gondeshapur", "Iran", 32.29, 48.52, ["Jundishapur", "Gundeshapur"]),
    ("Persepolis", "Iran", 29.93, 52.89, ["Parsa", "Takht-e Jamshid"]),
    ("Pasargadae", "Iran", 30.19, 53.17, []),
    ("Istakhr", "Iran", 29.98, 52.91, ["Estakhr"]),
    ("Firuzabad", "Iran", 28.85, 52.57, ["Gur", "Ardashir-Khwarrah"]),
    ("Bishapur", "Iran", 29.78, 51.57, []),
    ("Hormuz", "Iran", 27.10, 56.46, ["Hormoz", "Ormuz"]),
    ("Siraf", "Iran", 27.67, 52.34, []),
    ("Ani", "Turkey", 40.51, 43.57, []),
    ("Manzikert", "Turkey", 39.15, 42.54, ["Malazgirt"]),
    ("Sarai", "Russia", 47.18, 47.45, ["Old Sarai", "Sarai Batu", "Selitrennoye"]),
    ("New Sarai", "Russia", 48.68, 45.35, ["Sarai Berke", "Tsarev", "Sarai al-Jadid"]),
    ("Bolgar", "Russia", 54.97, 49.05, ["Bolghar", "Great Bolgar", "Bulgar"]),
    ("Itil", "Russia", 46.03, 47.87, ["Atil", "Samosdelka"]),
    ("Sarkel", "Russia", 47.73, 42.15, []),
    ("Tmutarakan", "Russia", 45.22, 36.72, ["Taman", "Tamatarcha"]),
    ("Azov", "Russia", 47.11, 39.42, ["Tana", "Azak"]),
    ("Chersonesus", "Ukraine", 44.61, 33.49, ["Korsun", "Chersonese"]),
    ("Bakhchysarai", "Ukraine", 44.75, 33.86, ["Bakhchisaray", "Bağçasaray"]),
    ("Sudak", "Ukraine", 44.85, 34.97, ["Soldaia", "Sugdea"]),
    ("Staraya Ladoga", "Russia", 60.00, 32.30, ["Ladoga", "Aldeigjuborg"]),
    ("Suzdal", "Russia", 56.42, 40.45, []),
    ("Rostov Veliky", "Russia", 57.19, 39.42, ["Rostov the Great"]),
    ("Novgorod-Seversky", "Ukraine", 52.00, 33.27, ["Novhorod-Siverskyi"]),
    ("Pereyaslav", "Ukraine", 50.07, 31.45, ["Pereiaslav"]),
    ("Halych", "Ukraine", 49.12, 24.73, ["Galich"]),
    ("Volodymyr", "Ukraine", 50.85, 24.32, ["Volodymyr-Volynskyi", "Vladimir-Volynsky"]),
    ("Kilia", "Ukraine", 45.45, 29.27, ["Kiliya"]),
    ("Ochakiv", "Ukraine", 46.61, 31.54, ["Özi", "Ochakov"]),
    ("Olbia", "Ukraine", 46.69, 31.90, []),
    ("Polotsk", "Belarus", 55.49, 28.77, ["Polatsk"]),
    ("Turov", "Belarus", 52.07, 27.75, []),
    ("Novogrudok", "Belarus", 53.60, 25.83, ["Navahrudak"]),
    ("Trakai", "Lithuania", 54.64, 24.93, []),
    ("Cesis", "Latvia", 57.31, 25.27, ["Wenden", "Cēsis"]),
    # Mesopotamia and the Levant
    ("Babylon", "Iraq", 32.54, 44.42, ["Babil"]),
    ("Ctesiphon", "Iraq", 33.09, 44.58, ["Seleucia-Ctesiphon", "Al-Mada'in"]),
    ("Seleucia on the Tigris", "Iraq", 33.10, 44.52, ["Seleucia"]),
    ("Ur", "Iraq", 30.96, 46.10, ["Tell el-Muqayyar"]),
    ("Uruk", "Iraq", 31.32, 45.64, ["Warka", "Erech"]),
    ("Nippur", "Iraq", 32.13, 45.23, []),
    ("Lagash", "Iraq", 31.41, 46.41, ["Tell al-Hiba"]),
    ("Kish", "Iraq", 32.54, 44.61, ["Tell al-Uhaymir"]),
    ("Assur", "Iraq", 35.46, 43.26, ["Ashur", "Qal'at Sherqat"]),
    ("Nimrud", "Iraq", 36.10, 43.33, ["Kalhu", "Calah"]),
    ("Nineveh", "Iraq", 36.36, 43.15, ["Ninua"]),
    ("Hatra", "Iraq", 35.59, 42.72, []),
    ("Kufa", "Iraq", 32.03, 44.40, ["Al-Kufah"]),
    ("Wasit", "Iraq", 32.18, 46.30, []),
    ("Mari", "Syria", 34.55, 40.89, ["Tell Hariri"]),
    ("Ebla", "Syria", 35.80, 36.80, ["Tell Mardikh"]),
    ("Ugarit", "Syria", 35.60, 35.78, ["Ras Shamra"]),
    ("Palmyra", "Syria", 34.55, 38.27, ["Tadmur", "Tadmor"]),
    ("Dura-Europos", "Syria", 34.75, 40.73, []),
    ("Apamea", "Syria", 35.42, 36.40, []),
    ("Bosra", "Syria", 32.52, 36.48, ["Bostra"]),
    ("Harran", "Turkey", 36.87, 39.03, ["Carrhae"]),
    ("Hattusa", "Turkey", 40.02, 34.62, ["Hattusha", "Boğazkale"]),
    ("Gordion", "Turkey", 39.65, 31.99, ["Gordium"]),
    ("Ephesus", "Turkey", 37.94, 27.34, ["Efes"]),
    ("Pergamon", "Turkey", 39.12, 27.18, ["Pergamum", "Bergama"]),
    ("Miletus", "Turkey", 37.53, 27.28, ["Miletos"]),
    ("Sardis", "Turkey", 38.49, 28.04, ["Sardes"]),
    ("Troy", "Turkey", 39.96, 26.24, ["Troia", "Ilion", "Hisarlik"]),
    ("Halicarnassus", "Turkey", 37.04, 27.43, ["Bodrum"]),
    ("Nicaea", "Turkey", 40.43, 29.72, ["İznik", "Iznik"]),
    ("Nicomedia", "Turkey", 40.77, 29.92, ["İzmit", "Izmit"]),
    ("Tyre", "Lebanon", 33.27, 35.20, ["Sur", "Tyr", "Sour"]),
    ("Byblos", "Lebanon", 34.12, 35.65, ["Jbeil", "Gubla"]),
    ("Acre", "Israel", 32.93, 35.08, ["Akko", "Akka", "Ptolemais"]),
    ("Jaffa", "Israel", 32.05, 34.75, ["Yafo", "Joppa"]),
    ("Caesarea Maritima", "Israel", 32.50, 34.89, ["Caesarea (Israel)"]),
    ("Jericho", "Palestine", 31.87, 35.44, []),
    ("Gerasa", "Jordan", 32.28, 35.89, ["Jerash"]),
    ("Petra", "Jordan", 30.33, 35.44, ["Raqmu"]),
    ("Qatif", "Saudi Arabia", 26.56, 50.01, ["Al-Qatif"]),
    ("Marib", "Yemen", 15.42, 45.34, ["Ma'rib"]),
    ("Zafar", "Yemen", 14.21, 44.40, ["Dhafar"]),
    ("Shabwa", "Yemen", 15.37, 47.02, []),
    ("Shibam", "Yemen", 15.93, 48.63, []),
    # Egypt and Africa
    ("Memphis", "Egypt", 29.85, 31.25, ["Men-nefer", "Mit Rahina"]),
    ("Amarna", "Egypt", 27.65, 30.90, ["Akhetaten", "Tell el-Amarna"]),
    ("Tanis", "Egypt", 30.98, 31.88, []),
    ("Sais", "Egypt", 30.97, 30.77, []),
    ("Avaris", "Egypt", 30.79, 31.82, ["Tell el-Dab'a", "Pi-Ramesses"]),
    ("Abydos", "Egypt", 26.18, 31.92, []),
    ("Naukratis", "Egypt", 30.90, 30.59, []),
    ("Pelusium", "Egypt", 31.04, 32.54, []),
    ("Hierakonpolis", "Egypt", 25.10, 32.78, ["Nekhen"]),
    ("Naqada", "Egypt", 25.90, 32.72, []),
    ("Kerma", "Sudan", 19.60, 30.41, []),
    ("Napata", "Sudan", 18.54, 31.83, ["Jebel Barkal", "Karima"]),
    ("Meroe", "Sudan", 16.94, 33.72, ["Meroë"]),
    ("Old Dongola", "Sudan", 18.22, 30.74, ["Dongola (old)"]),
    ("Soba", "Sudan", 15.52, 32.68, []),
    ("Adulis", "Eritrea", 15.26, 39.66, []),
    ("Zeila", "Somalia", 11.36, 43.47, ["Saylac"]),
    ("Lalibela", "Ethiopia", 12.03, 39.04, []),
    ("Sofala", "Mozambique", -20.17, 34.73, []),
    ("Great Zimbabwe", "Zimbabwe", -20.27, 30.93, []),
    ("Mapungubwe", "South Africa", -22.20, 29.39, []),
    ("Khami", "Zimbabwe", -20.15, 28.37, []),
    ("Kilwa", "Tanzania", -8.96, 39.51, ["Kilwa Kisiwani"]),
    ("Lamu", "Kenya", -2.27, 40.90, []),
    ("Gedi", "Kenya", -3.31, 40.02, []),
    ("Pate", "Kenya", -2.08, 41.03, []),
    ("Koumbi Saleh", "Mauritania", 15.77, -7.98, ["Kumbi Saleh"]),
    ("Oualata", "Mauritania", 17.30, -7.03, ["Walata"]),
    ("Awdaghust", "Mauritania", 17.42, -10.40, ["Tegdaoust", "Audaghost"]),
    ("Niani", "Guinea", 11.38, -8.55, []),
    ("Djenne", "Mali", 13.91, -4.55, ["Jenne", "Jenne-jeno", "Djenné"]),
    ("Ife", "Nigeria", 7.48, 4.56, ["Ile-Ife"]),
    ("Oyo-Ile", "Nigeria", 8.98, 4.33, ["Old Oyo", "Katunga"]),
    ("Ngazargamu", "Nigeria", 13.07, 12.38, ["Birnin Gazargamo"]),
    ("Mbanza Kongo", "Angola", -6.27, 14.25, ["São Salvador", "Sao Salvador"]),
    ("Loango", "Congo", -4.65, 11.82, []),
    ("Bilma", "Niger", 18.69, 12.92, []),
    ("Sijilmasa", "Morocco", 31.28, -4.28, []),
    ("Volubilis", "Morocco", 34.07, -5.55, []),
    ("Tahert", "Algeria", 35.37, 1.32, ["Tihert", "Tagdemt"]),
    ("Carthage", "Tunisia", 36.85, 10.33, ["Karthago", "Carthago", "Qart-hadasht"]),
    ("Cyrene", "Libya", 32.82, 21.86, ["Shahhat"]),
    ("Leptis Magna", "Libya", 32.64, 14.29, ["Lebda"]),
    ("Sabratha", "Libya", 32.79, 12.48, []),
    ("Germa", "Libya", 26.53, 13.06, ["Garama"]),
    ("Zawila", "Libya", 26.17, 15.12, []),
    # Greece and the Balkans
    ("Sparta", "Greece", 37.07, 22.43, ["Sparti", "Lacedaemon"]),
    ("Corinth", "Greece", 37.94, 22.93, ["Korinthos"]),
    ("Mycenae", "Greece", 37.73, 22.76, []),
    ("Delphi", "Greece", 38.48, 22.50, []),
    ("Olympia", "Greece", 37.64, 21.63, []),
    ("Pella", "Greece", 40.76, 22.52, []),
    ("Thebes", "Greece", 38.32, 23.32, ["Thiva", "Thebes (Greece)"]),
    ("Chalcis", "Greece", 38.46, 23.60, ["Chalkida"]),
    ("Knossos", "Greece", 35.30, 25.16, []),
    ("Pliska", "Bulgaria", 43.39, 27.13, []),
    ("Preslav", "Bulgaria", 43.16, 26.82, ["Veliki Preslav"]),
    ("Ohrid", "North Macedonia", 41.12, 20.80, []),
    ("Stari Ras", "Serbia", 43.12, 20.60, ["Ras"]),
    ("Sirmium", "Serbia", 44.97, 19.61, ["Sremska Mitrovica"]),
    ("Viminacium", "Serbia", 44.73, 21.22, []),
    ("Kruje", "Albania", 41.51, 19.79, ["Kruja", "Krujë"]),
    ("Salona", "Croatia", 43.54, 16.48, ["Solin"]),
    ("Sarmizegetusa Regia", "Romania", 45.62, 23.31, ["Sarmizegetusa"]),
    ("Targoviste", "Romania", 44.93, 25.46, ["Târgoviște"]),
    ("Curtea de Arges", "Romania", 45.14, 24.68, ["Curtea de Argeș"]),
    # Western and central Europe
    ("Avignon", "France", 43.95, 4.81, []),
    ("Laon", "France", 49.56, 3.62, []),
    ("Soissons", "France", 49.38, 3.33, []),
    ("Narbonne", "France", 43.18, 3.00, ["Narbo"]),
    ("Arles", "France", 43.68, 4.63, ["Arelate"]),
    ("Vienne", "France", 45.52, 4.87, []),
    ("Aachen", "Germany", 50.78, 6.08, ["Aix-la-Chapelle", "Aquisgrana"]),
    ("Trier", "Germany", 49.75, 6.64, ["Augusta Treverorum", "Trèves", "Treves"]),
    ("Worms", "Germany", 49.63, 8.36, []),
    ("Speyer", "Germany", 49.32, 8.43, []),
    ("Fulda", "Germany", 50.55, 9.68, []),
    ("Bamberg", "Germany", 49.89, 10.89, []),
    ("Konstanz", "Germany", 47.66, 9.18, ["Constance"]),
    ("Paderborn", "Germany", 51.72, 8.75, []),
    ("Hildesheim", "Germany", 52.15, 9.95, []),
    ("Goslar", "Germany", 51.91, 10.43, []),
    ("Quedlinburg", "Germany", 51.79, 11.14, []),
    ("Meissen", "Germany", 51.16, 13.47, []),
    ("Weimar", "Germany", 50.98, 11.33, []),
    ("Stralsund", "Germany", 54.31, 13.09, []),
    ("Frankfurt an der Oder", "Germany", 52.35, 14.55, ["Frankfurt (Oder)"]),
    ("Wittenberg", "Germany", 51.87, 12.65, []),
    ("Hedeby", "Germany", 54.49, 9.57, ["Haithabu"]),
    ("Elblag", "Poland", 54.16, 19.40, ["Elbing", "Elbląg"]),
    ("Malbork", "Poland", 54.04, 19.03, ["Marienburg"]),
    ("Gniezno", "Poland", 52.53, 17.60, []),
    ("Sandomierz", "Poland", 50.68, 21.75, []),
    ("Przemysl", "Poland", 49.78, 22.77, ["Przemyśl"]),
    ("Nitra", "Slovakia", 48.31, 18.09, []),
    ("Esztergom", "Hungary", 47.80, 18.74, ["Gran"]),
    ("Carnuntum", "Austria", 48.12, 16.87, []),
    ("Aquileia", "Italy", 45.77, 13.37, []),
    ("Spoleto", "Italy", 42.73, 12.74, []),
    ("Capua", "Italy", 41.10, 14.21, []),
    ("Amalfi", "Italy", 40.63, 14.60, []),
    ("Urbino", "Italy", 43.73, 12.64, []),
    ("Jelling", "Denmark", 55.76, 9.42, []),
    ("Ribe", "Denmark", 55.33, 8.76, []),
    ("Birka", "Sweden", 59.34, 17.54, []),
    ("Thingvellir", "Iceland", 64.26, -21.12, ["Þingvellir"]),
    ("Kirkwall", "United Kingdom", 58.98, -2.96, []),
    ("Scone", "United Kingdom", 56.42, -3.43, []),
    ("Dunfermline", "United Kingdom", 56.07, -3.46, []),
    ("Bamburgh", "United Kingdom", 55.61, -1.71, []),
    ("Berwick-upon-Tweed", "United Kingdom", 55.77, -2.00, ["Berwick"]),
    ("Winchester", "United Kingdom", 51.06, -1.31, []),
    ("Tamworth", "United Kingdom", 52.63, -1.69, []),
    ("Colchester", "United Kingdom", 51.89, 0.90, ["Camulodunum"]),
    ("St Albans", "United Kingdom", 51.75, -0.34, ["Verulamium"]),
    ("Shrewsbury", "United Kingdom", 52.71, -2.75, []),
    ("Hastings", "United Kingdom", 50.86, 0.57, []),
    ("Caernarfon", "United Kingdom", 53.14, -4.27, ["Caernarvon"]),
    ("Pembroke", "United Kingdom", 51.67, -4.92, []),
    ("Tara", "Ireland", 53.58, -6.61, ["Hill of Tara"]),
    ("Cashel", "Ireland", 52.52, -7.89, []),
    ("Armagh", "United Kingdom", 54.35, -6.65, []),
    ("Iona", "United Kingdom", 56.33, -6.42, []),
    ("Jaca", "Spain", 42.57, -0.55, []),
    ("Tortosa", "Spain", 40.81, 0.52, []),
    ("Numantia", "Spain", 41.81, -2.44, []),
    ("Italica", "Spain", 37.44, -6.05, []),
    ("Guimaraes", "Portugal", 41.44, -8.29, ["Guimarães"]),
    ("Silves", "Portugal", 37.19, -8.44, []),
    # South Asia
    ("Taxila", "Pakistan", 33.74, 72.79, ["Takshashila"]),
    ("Thatta", "Pakistan", 24.75, 67.92, []),
    ("Khairpur", "Pakistan", 27.53, 68.76, []),
    ("Mohenjo-daro", "Pakistan", 27.33, 68.14, ["Mohenjo Daro"]),
    ("Harappa", "Pakistan", 30.63, 72.86, []),
    ("Jaisalmer", "India", 26.92, 70.91, []),
    ("Chittorgarh", "India", 24.88, 74.63, ["Chittor"]),
    ("Kannauj", "India", 27.05, 79.92, ["Kanauj", "Kanyakubja"]),
    ("Ayodhya", "India", 26.80, 82.20, ["Saketa"]),
    ("Nalanda", "India", 25.14, 85.44, []),
    ("Rajgir", "India", 25.03, 85.42, ["Rajagriha"]),
    ("Mandu", "India", 22.35, 75.40, ["Mandavgad"]),
    ("Daulatabad", "India", 19.94, 75.21, ["Devagiri"]),
    ("Satara", "India", 17.69, 74.00, []),
    ("Old Goa", "India", 15.50, 73.91, ["Goa (city)", "Goa"]),
    ("Hampi", "India", 15.33, 76.46, ["Vijayanagara"]),
    ("Srirangapatna", "India", 12.42, 76.69, ["Seringapatam"]),
    ("Mahabalipuram", "India", 12.62, 80.19, ["Mamallapuram"]),
    ("Kannur", "India", 11.87, 75.37, ["Cannanore"]),
    ("Polonnaruwa", "Sri Lanka", 7.94, 81.00, []),
    # South-east Asia
    ("Mrauk U", "Myanmar", 20.59, 93.19, ["Mrohaung"]),
    ("Bagan", "Myanmar", 21.17, 94.86, ["Pagan"]),
    ("Ava", "Myanmar", 21.86, 95.98, ["Inwa"]),
    ("Amarapura", "Myanmar", 21.90, 96.05, []),
    ("Prome", "Myanmar", 18.82, 95.22, ["Pyay", "Sri Ksetra"]),
    ("Taungoo", "Myanmar", 18.94, 96.43, ["Toungoo"]),
    ("Thaton", "Myanmar", 16.92, 97.37, []),
    ("Mergui", "Myanmar", 12.44, 98.60, ["Myeik"]),
    ("Haripunjaya", "Thailand", 18.58, 99.01, ["Lamphun", "Hariphunchai"]),
    ("Angkor", "Cambodia", 13.43, 103.87, ["Yasodharapura", "Angkor Thom"]),
    ("Hariharalaya", "Cambodia", 13.35, 103.98, ["Roluos"]),
    ("Sambor Prei Kuk", "Cambodia", 12.87, 105.05, ["Isanapura"]),
    ("Longvek", "Cambodia", 11.80, 104.73, ["Lovek"]),
    ("Oudong", "Cambodia", 11.81, 104.74, ["Udong"]),
    ("Co Loa", "Vietnam", 21.11, 105.87, ["Cổ Loa"]),
    ("Hoa Lu", "Vietnam", 20.28, 105.90, ["Hoa Lư"]),
    ("Indrapura", "Vietnam", 15.95, 108.30, ["Dong Duong"]),
    ("Simhapura", "Vietnam", 15.80, 108.25, ["Tra Kieu"]),
    ("My Son", "Vietnam", 15.76, 108.12, ["Mỹ Sơn"]),
    ("Vijaya", "Vietnam", 13.90, 109.10, ["Cha Ban", "Do Ban"]),
    ("Quy Nhon", "Vietnam", 13.78, 109.22, ["Qui Nhon"]),
    ("Panduranga", "Vietnam", 11.57, 108.99, ["Phan Rang"]),
    ("Oc Eo", "Vietnam", 10.25, 105.15, ["Óc Eo"]),
    ("Ha Tien", "Vietnam", 10.38, 104.48, ["Hà Tiên"]),
    ("Hai Phong", "Vietnam", 20.86, 106.68, ["Haiphong", "Hải Phòng"]),
    ("Kedah", "Malaysia", 6.12, 100.37, ["Kedah (Bujang Valley)"]),
    ("Hoima", "Uganda", 1.43, 31.35, ["Bunyoro (capital)"]),
    ("Trowulan", "Indonesia", -7.56, 112.38, ["Majapahit (capital)", "Wilwatikta"]),
    ("Singhasari", "Indonesia", -7.89, 112.66, ["Singosari", "Tumapel"]),
    ("Demak", "Indonesia", -6.89, 110.64, []),
    ("Banten", "Indonesia", -6.04, 106.15, ["Old Banten", "Bantam"]),
    ("Banda Neira", "Indonesia", -4.53, 129.90, ["Banda", "Banda Islands"]),
    ("Tidore", "Indonesia", 0.68, 127.42, []),
    ("Jolo", "Philippines", 6.05, 121.00, ["Sulu (town)"]),
    # East Asia
    ("Asuka", "Japan", 34.47, 135.82, ["Fujiwara-kyo"]),
    ("Kamakura", "Japan", 35.32, 139.55, []),
    ("Dazaifu", "Japan", 33.51, 130.52, []),
    ("Hiraizumi", "Japan", 38.99, 141.11, []),
    ("Azuchi", "Japan", 35.15, 136.14, []),
    ("Shuri", "Japan", 26.22, 127.72, ["Shuri (Ryukyu)"]),
    ("Buyeo", "South Korea", 36.28, 126.91, ["Sabi"]),
    ("Gongju", "South Korea", 36.45, 127.12, ["Ungjin"]),
    ("Ganghwa", "South Korea", 37.75, 126.49, []),
    # Americas
    ("Teotihuacan", "Mexico", 19.69, -98.84, ["Teotihuacán"]),
    ("Tula", "Mexico", 20.06, -99.34, ["Tollan", "Tula de Allende"]),
    ("Cholula", "Mexico", 19.06, -98.30, []),
    ("Monte Alban", "Mexico", 17.04, -96.77, ["Monte Albán"]),
    ("Mitla", "Mexico", 16.92, -96.36, []),
    ("Texcoco", "Mexico", 19.51, -98.88, ["Tetzcoco"]),
    ("Tzintzuntzan", "Mexico", 19.63, -101.58, []),
    ("El Tajin", "Mexico", 20.45, -97.38, ["El Tajín"]),
    ("Palenque", "Mexico", 17.48, -92.05, []),
    ("Calakmul", "Mexico", 18.11, -89.81, []),
    ("Uxmal", "Mexico", 20.36, -89.77, []),
    ("Chichen Itza", "Mexico", 20.68, -88.57, ["Chichén Itzá"]),
    ("Mayapan", "Mexico", 20.63, -89.46, ["Mayapán"]),
    ("Tulum", "Mexico", 20.21, -87.43, []),
    ("Coba", "Mexico", 20.49, -87.73, ["Cobá"]),
    ("San Lorenzo Tenochtitlan", "Mexico", 17.75, -94.76, ["San Lorenzo (Olmec)"]),
    ("La Venta", "Mexico", 18.10, -94.04, []),
    ("Tres Zapotes", "Mexico", 18.47, -95.44, []),
    ("Xochicalco", "Mexico", 18.80, -99.30, []),
    ("Cacaxtla", "Mexico", 19.24, -98.34, []),
    ("Tikal", "Guatemala", 17.22, -89.62, []),
    ("El Mirador", "Guatemala", 17.75, -89.92, []),
    ("Iximche", "Guatemala", 14.74, -90.99, ["Iximché"]),
    ("Q'umarkaj", "Guatemala", 15.02, -91.22, ["Utatlan", "Gumarcaj", "Utatlán"]),
    ("Tayasal", "Guatemala", 16.93, -89.89, ["Nojpeten", "Flores (Peten)"]),
    ("Quirigua", "Guatemala", 15.27, -89.04, ["Quiriguá"]),
    ("Copan", "Honduras", 14.84, -89.14, ["Copán"]),
    ("Caracol", "Belize", 16.76, -89.12, []),
    ("Lamanai", "Belize", 17.76, -88.65, []),
    ("Tazumal", "El Salvador", 13.98, -89.68, []),
    ("Caral", "Peru", -10.89, -77.52, []),
    ("Chavin de Huantar", "Peru", -9.59, -77.18, ["Chavín de Huántar", "Chavin"]),
    ("Moche", "Peru", -8.17, -78.99, ["Huacas de Moche"]),
    ("Chan Chan", "Peru", -8.10, -79.07, []),
    ("Sipan", "Peru", -6.80, -79.60, ["Sipán"]),
    ("Kuelap", "Peru", -6.42, -77.92, ["Kuélap"]),
    ("Wari", "Peru", -13.07, -74.18, ["Huari"]),
    ("Vilcabamba", "Peru", -13.11, -73.00, ["Espíritu Pampa"]),
    ("Machu Picchu", "Peru", -13.16, -72.55, []),
    ("Pachacamac", "Peru", -12.26, -76.90, []),
    ("Nazca", "Peru", -14.83, -74.94, ["Nasca"]),
    ("Tiwanaku", "Bolivia", -16.55, -68.67, ["Tiahuanaco"]),
    ("Cahokia", "United States of America", 38.66, -90.06, []),
    ("Moundville", "United States of America", 33.00, -87.63, []),
    ("Etowah", "United States of America", 34.13, -84.81, []),
    ("Spiro", "United States of America", 35.31, -94.57, []),
    ("Pueblo Bonito", "United States of America", 36.06, -107.96, ["Chaco Canyon"]),
    ("Mesa Verde", "United States of America", 37.18, -108.49, []),
    ("Acoma", "United States of America", 34.90, -107.58, []),
    ("Jamestown", "United States of America", 37.21, -76.78, []),
    ("Plymouth Colony", "United States of America", 41.96, -70.67, ["Plymouth (Massachusetts)"]),
    ("Williamsburg", "United States of America", 37.27, -76.71, []),
    ("Roanoke", "United States of America", 35.88, -75.66, ["Roanoke Colony"]),
    ("St. Mary's City", "United States of America", 38.19, -76.43, []),
    ("Vincennes", "United States of America", 38.68, -87.53, []),
    ("Kaskaskia", "United States of America", 37.92, -89.92, []),
    ("Michilimackinac", "United States of America", 45.78, -84.73, ["Mackinac"]),
    ("Fort Niagara", "United States of America", 43.26, -79.06, ["Niagara"]),
    ("Fort Ticonderoga", "United States of America", 43.84, -73.39, ["Ticonderoga"]),
    ("Oswego", "United States of America", 43.46, -76.51, []),
    ("Natchitoches", "United States of America", 31.76, -93.09, []),
    ("Arkansas Post", "United States of America", 34.02, -91.35, []),
    ("Sainte Genevieve", "United States of America", 37.98, -90.05, ["Ste. Genevieve"]),
    ("Fort Vancouver", "United States of America", 45.63, -122.66, ["Vancouver (Washington)"]),
    ("Fort Ross", "United States of America", 38.51, -123.25, []),
    ("Astoria", "United States of America", 46.19, -123.83, ["Fort Astoria"]),
    ("Port-Royal", "Canada", 44.71, -65.61, ["Port Royal", "Annapolis Royal"]),
    ("Louisbourg", "Canada", 45.92, -59.97, []),
    ("York Factory", "Canada", 57.00, -92.30, []),
    ("Nootka", "Canada", 49.59, -126.62, ["Yuquot", "Nootka Sound"]),
    ("Port Royal (Jamaica)", "Jamaica", 17.94, -76.84, []),
    # Added 1 Nov 2026 by the gazetteer run for the Phase C unresolved names: coordinates read from the page named in the comment
    # (en.wikipedia.org/wiki/<page>, opened with WebFetch on 1 Nov 2026), not from memory; about 0.001-0.01 degree.
    ("Péronne", "France", 49.9292, 2.9325, []),  # Péronne,_Somme
    ("Montargis", "France", 47.9978, 2.7333, []),  # Montargis
    ("Abbeville", "France", 50.1058, 1.8358, []),  # Abbeville
    ("Boulogne-sur-Mer", "France", 50.7264, 1.6147, ["Boulogne"]),  # Boulogne-sur-Mer
    ("Lleida", "Spain", 41.6167, 0.6333, ["Lérida", "Lerida"]),  # Lleida
    ("Şebinkarahisar", "Turkey", 40.2886, 38.4233, ["Sebinkarahisar", "Shebin Karahisar", "Karahisar-i Sharki"]),  # Şebinkarahisar
    ("Bernburg", "Germany", 51.8, 11.733, ["Bernburg (Saale)"]),  # Bernburg
    ("Vic-le-Comte", "France", 45.6439, 3.2467, []),  # Vic-le-Comte
    ("Dessau", "Germany", 51.8333, 12.25, ["Dessau-Roßlau", "Dessau-Rosslau"]),  # Dessau
    ("Ratzeburg", "Germany", 53.7, 10.75, []),  # Ratzeburg
    ("Larsa", "Iraq", 31.2858, 45.8536, ["Senkereh", "Tell as-Senkereh", "Larsam"]),  # Larsa
    ("Gerdkuh", "Iran", 36.1619, 54.1569, ["Gerdkoh", "Gird Kuh", "Gerdkuh Castle"]),  # Gerdkuh
    ("Zerbst", "Germany", 51.9681, 12.0844, ["Zerbst/Anhalt"]),  # Zerbst
    ("Maheshwar", "India", 22.1167, 75.35, ["Mahishmati", "Mahesvar"]),  # Maheshwar
    ("Roquebrune-Cap-Martin", "France", 43.7628, 7.4631, ["Roquebrune", "Roccabruna"]),  # Roquebrune-Cap-Martin
    ("Menton", "France", 43.775, 7.5, ["Mentone"]),  # Menton
    ("Umma", "Iraq", 31.6672, 45.8875, ["Tell Jokha", "Gishban"]),  # Umma
    ("Kalimpong", "India", 27.06, 88.47, ["Dalimkot"]),  # Kalimpong
    ("Alamut", "Iran", 36.4447, 50.5861, ["Alamut Castle", "Alamut Valley"]),  # Alamut_Castle
    ("Suakin", "Sudan", 19.1025, 37.33, ["Sawakin", "Suakim"]),  # Suakin
    ("Akwidaa", "Ghana", 4.75, -2.017, ["Akwida", "Fort Dorothea"]),  # Akwidaa
    ("Groenlo", "Netherlands", 52.0411, 6.6172, ["Grol"]),  # Groenlo
    ("Rudkhan", "Iran", 37.0644, 49.24, ["Rudkhan Castle", "Rudkhan-i Gilan"]),  # Rudkhan_Castle
    ("Dénia", "Spain", 38.8444, 0.1111, ["Denia"]),  # Dénia
    ("Jalore", "India", 25.35, 72.6167, ["Jalor", "Jalore Fort"]),  # Jalore
    ("Köthen", "Germany", 51.7511, 11.9736, ["Köthen (Anhalt)", "Cöthen", "Kothen", "Koethen"]),  # Köthen
    ("Princes Town", "Ghana", 4.7936, -2.1347, ["Princess Town", "Groß Friedrichsburg", "Gross Friedrichsburg", "Fort Gross Friedrichsburg"]),  # Princes_Town,_Ghana
    ("Isin", "Iraq", 31.885, 45.2686, ["Ishan al-Bahriyat", "Ishan Bahriyat"]),  # Isin
    ("Monemvasia", "Greece", 36.6878, 23.0556, ["Monembasia", "Malvasia", "Monemvasía"]),  # Monemvasia
    ("Agde", "France", 43.3108, 3.4758, ["Agathe", "Agathe Tyche"]),  # Agde
    ("Gaeta", "Italy", 41.217, 13.567, ["Gaëta", "Caieta"]),  # Gaeta
    ("Thasos", "Greece", 40.683, 24.65, ["Thassos"]),  # Thasos
    ("Gytheio", "Greece", 36.7617, 22.565, ["Gythium", "Gytheion", "Gythion"]),  # Gytheio
    ("Hyères", "France", 43.1199, 6.1316, ["Hyeres", "Olbia (Gaul)"]),  # Hyères
    ("Mayyafariqin", "Turkey", 38.1422, 41.0014, ["Silvan", "Martyropolis", "Maiyafariqin"]),  # Silvan,_Diyarbakır
    ("Kalinjar", "India", 24.9997, 80.4852, ["Kalanjara", "Kalinjara", "Kalinjar Fort"]),  # Kalinjar_Fort
    ("Arguin", "Mauritania", 20.6, -16.45, ["Arguin Island", "Arguim", "Banc d'Arguin"]),  # Arguin
    ("Bautzen", "Germany", 51.1814, 14.4242, ["Budyšin", "Budissin", "Budissin Land", "Bautzen/Budyšin"]),  # Bautzen
    ("Nagaon", "India", 26.3504, 92.6796, ["Nowgong"]),  # Nagaon
    ("Amlapura", "Indonesia", -8.447, 115.615, ["Karangasem", "Karangasem Regency capital"]),  # Amlapura
    ("Breda", "Netherlands", 51.5889, 4.7758, []),  # Breda
    ("Cephalonia", "Greece", 38.265, 20.5525, ["Kefalonia", "Kefallinia", "Cefalonia"]),  # Cephalonia
    ("Junagadh", "India", 21.5222, 70.4579, ["Junagarh", "Girnar"]),  # Junagadh
    ("Metztitlán", "Mexico", 20.6, -98.7667, ["Metztitlan"]),  # Metztitlán
    ("Sena", "Mozambique", -17.4417, 35.0272, ["Sena (Mozambique)"]),  # Sena,_Mozambique
    ("Zakynthos", "Greece", 37.8, 20.75, ["Zante", "Zacynthus"]),  # Zakynthos
    ("Anomabu", "Ghana", 5.1667, -1.1167, ["Anomabo", "Fort William (Anomabu)"]),  # Anomabu
    ("Beyin", "Ghana", 4.985, -2.5869, ["Fort Apollonia", "Apollonia"]),  # Beyin
    ("Château-Thierry", "France", 49.0333, 3.4, ["Chateau-Thierry"]),  # Château-Thierry
    ("Mehrgarh", "Pakistan", 29.383, 67.617, ["Mehrgarh culture site"]),  # Mehrgarh
    ("Mértola", "Portugal", 37.6403, -7.6611, ["Mertola"]),  # Mértola
    ("Nagaur", "India", 27.2, 73.73, ["Nagore"]),  # Nagaur
    ("Pokhran", "India", 26.92, 71.92, ["Pokaran"]),  # Pokhran
    ("Provins", "France", 48.5604, 3.299, []),  # Provins
    ("Skyros", "Greece", 38.8725, 24.525, ["Skiros", "Scyros"]),  # Skyros
    ("Champaner", "India", 22.8125, 73.8872, ["Champaner-Pavagadh", "Pavagadh"]),  # Champaner
    ("Masyaf", "Syria", 35.0653, 36.3422, ["Masyad", "Masyaf Castle"]),  # Masyaf
    ("Naju", "South Korea", 35.033, 126.717, ["Naju-si"]),  # Naju
    ("Anahilapataka", "India", 23.85, 72.125, ["Anhilwara", "Anhilwad Patan", "Anahilavada", "Anahilapura", "Patan (Gujarat)", "Anhilvad"]),  # Patan,_Gujarat
    ("Barbastro", "Spain", 42.0361, 0.1264, []),  # Barbastro
    ("Ciudad Real", "Spain", 38.9833, -3.9167, ["Calatrava la Nueva"]),  # Ciudad_Real
    ("Khajuraho", "India", 24.85, 79.925, ["Khajuraha", "Khajrao"]),  # Khajuraho
    ("Orlamünde", "Germany", 50.7753, 11.5314, ["Orlamuende", "Orlamunde"]),  # Orlamünde
    ("Thane", "India", 19.1972, 72.9722, ["Thana", "Tana"]),  # Thane
    ("Shangcai", "China", 33.262, 114.264, ["Shangcai County", "Upper Cai"]),  # Shangcai_County
    ("Ada", "Ghana", 5.783, 0.633, ["Ada Foah", "Kongensten", "Fort Kongensten"]),  # Ada_Foah
    ("Aegina", "Greece", 37.73, 23.49, ["Egina", "Aigina", "Aigina island"]),  # Aegina
    ("Antibes", "France", 43.5808, 7.1239, ["Antipolis"]),  # Antibes
    ("Idar", "India", 23.839, 73.002, ["Idar State", "Idar (Gujarat)"]),  # Idar,_Gujarat
    ("Mandalgarh", "India", 25.2, 75.1, ["Mandalgarh Fort"]),  # Mandalgarh
    ("Troezen", "Greece", 37.483, 23.35, ["Troezen", "Troizen", "Trizina", "Troizina"]),  # Troezen
    ("Venlo", "Netherlands", 51.367, 6.167, []),  # Venlo
    ("Albarracín", "Spain", 40.4083, -1.4394, ["Albarracin"]),  # Albarracín
    ("Alpuente", "Spain", 39.8778, -1.0139, ["Alpuente Taifa"]),  # Alpuente
    ("Arta", "Greece", 39.165, 20.9875, ["Ambracia", "Árta", "Arta (Greece)"]),  # Arta,_Greece
    ("Douai", "France", 50.3714, 3.08, ["Douay"]),  # Douai
    ("Hulst", "Netherlands", 51.283, 4.05, []),  # Hulst,_Netherlands
    ("Orchies", "France", 50.4756, 3.245, []),  # Orchies
    ("Sas van Gent", "Netherlands", 51.2278, 3.7972, []),  # Sas_van_Gent
    ("Badme", "Eritrea", 14.7261, 37.8033, ["Badme town"]),  # Badme
    ("Elmina", "Ghana", 5.0833, -1.35, ["Edina", "São Jorge da Mina", "Elmina Castle"]),  # Elmina
    ("Mount Abu", "India", 24.5925, 72.7083, ["Abu", "Arbuda"]),  # Mount_Abu
    ("Nadol", "India", 25.3669, 73.45, ["Naddula", "Nadole"]),  # Nadol
    ("Pylos", "Greece", 36.9139, 21.6964, ["Pylus", "Navarino", "Pilos"]),  # Pylos
    ("Shire", "Ethiopia", 14.1, 38.283, ["Inda Selassie", "Inda Silase", "Shire Inda Selassie"]),  # Shire,_Ethiopia
    ("Teshie", "Ghana", 5.5833, -0.1, []),  # Teshie
    ("Yoshino", "Japan", 34.3961, 135.8575, ["Yoshino Nara", "Yoshino-cho"]),  # Yoshino,_Nara
    ("Komenda", "Ghana", 5.05, -1.4894, ["Fort Komenda", "Komenda Fort"]),  # Fort_Komenda
    ("Sankt Wendel", "Germany", 49.467, 7.167, ["St. Wendel", "St Wendel"]),  # Sankt_Wendel
    ("Aydhab", "Egypt", 22.3167, 36.4667, ["Aidhab", "Aidab", "Aydab"]),  # Aydhab
    ("Aschersleben", "Germany", 51.75, 11.467, []),  # Aschersleben
    ("Asilah", "Morocco", 35.4667, -6.0333, ["Arzila", "Arcila", "Asilah (Morocco)"]),  # Asilah
    ("Blois", "France", 47.5939, 1.3281, []),  # Blois
    ("Echt", "Netherlands", 51.1, 5.883, ["Echt-Susteren", "Echt (Netherlands)"]),  # Echt,_Netherlands
    ("Głogów", "Poland", 51.6589, 16.0803, ["Glogow", "Glogau"]),  # Głogów
    ("Kythira", "Greece", 36.2575, 22.9975, ["Cythera", "Kythera", "Cerigo", "Kithira"]),  # Kythira
    ("Lemnos", "Greece", 39.9167, 25.25, ["Limnos", "Lemnos island"]),  # Lemnos
    ("Adab", "Iraq", 31.9473, 45.6263, ["Bismaya", "Tell Bismaya", "Udab", "Usab"]),  # Adab_(city)
    ("Agrigento", "Italy", 37.3125, 13.575, ["Akragas", "Acragas", "Girgenti", "Agrigentum"]),  # Agrigento
    ("Fivizzano", "Italy", 44.233, 10.133, []),  # Fivizzano
    ("Pontremoli", "Italy", 44.383, 9.883, []),  # Pontremoli
    ("Minab", "Iran", 27.135, 57.0781, ["Old Hormuz", "Naband", "Minab (Iran)"]),  # Minab
    ("Montabaur", "Germany", 50.4375, 7.8258, []),  # Montabaur
    ("Ostend", "Belgium", 51.2258, 2.9194, ["Oostende", "Ostende"]),  # Ostend
    ("Saint-Jean-Pied-de-Port", "France", 43.165, -1.2356, ["Donibane Garazi", "St-Jean-Pied-de-Port"]),  # Saint-Jean-Pied-de-Port
    ("Spinalonga", "Greece", 35.2975, 25.7381, ["Kalydon", "Spinalonga island"]),  # Spinalonga
    ("Velizh", "Russia", 55.6, 31.183, []),  # Velizh
    ("Vendôme", "France", 47.7936, 1.0664, ["Vendome"]),  # Vendôme
    ("Wieluń", "Poland", 51.2206, 18.57, ["Wielun"]),  # Wieluń
    ("Bathinda", "India", 30.23, 74.9519, ["Tabarhindah", "Tabar-i-hind", "Bhatinda", "Bathinda Fort"]),  # Bathinda
    ("Nuwakot", "Nepal", 27.9108, 85.1453, ["Nuwakot Gadhi", "Nuwakot District"]),  # Nuwakot_District
    ("Dhar", "India", 22.5972, 75.3042, ["Dhar (Madhya Pradesh)", "Dhara"]),  # Dhar
    ("Gdov", "Russia", 58.7333, 27.8333, ["Gdow"]),  # Gdov
    ("Jinju", "South Korea", 35.2, 128.0833, ["Chinju", "Jinju-si"]),  # Jinju
    ("Kombolcha", "Ethiopia", 11.0867, 39.7367, ["Kombolcha (Ethiopia)"]),  # Kombolcha
    ("Kufstein", "Austria", 47.5833, 12.1667, []),  # Kufstein
    ("Lüneburg", "Germany", 53.2525, 10.4144, ["Luneburg", "Lueneburg", "Lüneburg (Germany)"]),  # Lüneburg
    ("Merta", "India", 26.65, 74.0333, ["Merta City", "Merta (India)"]),  # Merta_City
    ("Orchomenus", "Greece", 38.483, 22.983, ["Orchomenos", "Orchomenus (Boeotia)", "Orchomenos (Boeotia)"]),  # Orchomenus_(Boeotia)
    ("Slivnitsa", "Bulgaria", 42.85, 23.033, ["Slivnica"]),  # Slivnitsa
    ("Stade", "Germany", 53.6008, 9.4764, ["Stade (Germany)"]),  # Stade
    ("Xincai", "China", 32.7449, 114.965, ["Xincai County", "New Cai"]),  # Xincai_County
    ("Almenar", "Spain", 41.7986, 0.5689, ["Almenar (Lleida)"]),  # Almenar
    ("Assin Fosu", "Ghana", 5.7, -1.2778, ["Assin Foso", "Assin Fosu (Ghana)"]),  # Assin_Fosu
    ("Boppard", "Germany", 50.2314, 7.5908, ["Baudobriga"]),  # Boppard
    ("Cieszyn", "Poland", 49.7484, 18.6332, ["Teschen", "Tesin"]),  # Cieszyn
    ("Divriği", "Turkey", 39.3667, 38.1167, ["Divrigi", "Divriği (Turkey)"]),  # Divriği
    ("Gramvousa", "Greece", 35.6111, 23.5792, ["Gramvoussa", "Grambousa"]),  # Gramvousa
    ("Graus", "Spain", 42.1875, 0.3342, []),  # Graus
    ("Jebba", "Nigeria", 9.1539, 4.8119, ["Jebba (Nigeria)"]),  # Jebba
    ("Kalisz", "Poland", 51.7575, 18.08, ["Kalisch", "Kalisz (Poland)"]),  # Kalisz
    ("Loulan", "China", 40.5276, 89.8406, ["Loulan Kingdom", "Kroraina", "Krorän"]),  # Loulan
    ("Mazara del Vallo", "Italy", 37.65, 12.583, ["Mazara"]),  # Mazara_del_Vallo
    ("Mechelen", "Belgium", 51.0278, 4.4806, ["Malines"]),  # Mechelen
    ("Methoni", "Greece", 36.8217, 21.7069, ["Modon", "Methone"]),  # Methoni,_Messenia
    ("Mykonos", "Greece", 37.4589, 25.3642, ["Mikonos", "Mykonos island"]),  # Mykonos
    ("Nafplio", "Greece", 37.5658, 22.8, ["Nauplia", "Nafplion", "Napoli di Romania", "Nauplion"]),  # Nafplio
    ("Olivenza", "Spain", 38.6858, -7.1008, ["Olivença", "Olivenca"]),  # Olivenza
    ("Oświęcim", "Poland", 50.0381, 19.2214, ["Oswiecim", "Auschwitz"]),  # Oświęcim
    ("Pereslavl-Zalessky", "Russia", 56.733, 38.85, ["Pereslavl Zalessky", "Pereslavl-Zalesskiy", "Pereslavl"]),  # Pereslavl-Zalessky
    ("Qalhat", "Oman", 22.6994, 59.3694, ["Calatu", "Kalhat", "Qalhat (Oman)"]),  # Qalhat
    ("Raisen", "India", 23.33, 77.8, ["Raisen Fort", "Raisen (India)"]),  # Raisen
    ("Siewierz", "Poland", 50.4733, 19.2331, ["Sewerien"]),  # Siewierz
    ("Sorrento", "Italy", 40.6261, 14.3761, ["Surrentum"]),  # Sorrento
    ("Toszek", "Poland", 50.45, 18.517, ["Tost"]),  # Toszek
    ("Wadelai", "Uganda", 2.783, 31.5, []),  # Wadelai
    ("Wismar", "Germany", 53.9, 11.467, ["Wismar (Germany)"]),  # Wismar
    ("Wiślica", "Poland", 50.3467, 20.6736, ["Wislica"]),  # Wiślica
    ("Bhadrajun", "India", 25.6, 72.8669, ["Bhadrajun Fort"]),  # Bhadrajun
    ("Ypres", "Belgium", 50.8508, 2.885, ["Ieper"]),  # Ypres
    ("Alaşehir", "Turkey", 38.35, 28.517, ["Alasehir", "Philadelphia (Lydia)", "Philadelphia in Lydia"]),  # Alaşehir
    ("Axim", "Ghana", 4.8667, -2.2333, ["Fort Santo Antonio", "Axim (Ghana)"]),  # Axim
    ("Banda, Uttar Pradesh", "India", 25.483, 80.333, ["Banda", "Banda (India)", "Banda (Uttar Pradesh)"]),  # Banda,_Uttar_Pradesh
    ("Bazhong", "China", 31.868, 106.748, ["Bazhong (Sichuan)"]),  # Bazhong
    ("Brandenburg an der Havel", "Germany", 52.417, 12.533, ["Brandenburg", "Brennabor", "Brandenburg (Havel)"]),  # Brandenburg_an_der_Havel
    ("Chartres", "France", 48.456, 1.484, ["Carnutes", "Autricum"]),  # Chartres
    ("Civitella del Tronto", "Italy", 42.767, 13.667, []),  # Civitella_del_Tronto
    ("Gagron", "India", 24.6279, 76.183, ["Gagron Fort", "Gagraun"]),  # Gagron_Fort
    ("Hanwella", "Sri Lanka", 6.88, 80.0875, ["Hanwella (Sri Lanka)"]),  # Hanwella
    ("Kish Island", "Iran", 26.535, 53.975, ["Kish", "Qeys", "Qays", "Kish (Iran)", "Kais", "Kis"]),  # Kish_Island
    ("Lamezia Terme", "Italy", 38.9667, 16.3, ["Terina", "Lamezia"]),  # Lamezia_Terme
    ("Lentini", "Italy", 37.283, 15.0, ["Leontinoi", "Leontini"]),  # Lentini
    ("Manfredonia", "Italy", 41.633, 15.917, ["Sipontum", "Siponto"]),  # Manfredonia
    ("Monzón", "Spain", 41.91, 0.19, ["Monzon"]),  # Monzón
    ("Policoro", "Italy", 40.2, 16.6667, ["Heraclea Lucaniae", "Herakleia (Lucania)"]),  # Policoro
    ("Prüm", "Germany", 50.2081, 6.4244, ["Pruem", "Prum", "Prüm Abbey"]),  # Prüm
    ("Rajouri", "India", 33.3767, 74.3122, ["Rajauri", "Rajapura", "Rajori"]),  # Rajouri
    ("Ranthambore", "India", 26.0203, 76.455, ["Ranthambhore", "Ranthambore Fort", "Ranthambhor"]),  # Ranthambore_Fort
    ("Rattenberg", "Austria", 47.4389, 11.8933, []),  # Rattenberg
    ("Rewa", "India", 24.5381, 81.2953, ["Rewa (Madhya Pradesh)", "Rewa (India)"]),  # Rewa,_Madhya_Pradesh
    ("Samos", "Greece", 37.75, 26.8333, ["Samos island"]),  # Samos
    ("Shaizar", "Syria", 35.2678, 36.5667, ["Qalat Shaizar", "Sheizar"]),  # Shaizar
    ("Sibari", "Italy", 39.7508, 16.4514, ["Sybaris", "Thurii", "Sibari (Cassano)"]),  # Sibari
    ("Sirohi", "India", 24.885, 72.8625, ["Sirohi (India)"]),  # Sirohi
    ("Sobrance", "Slovakia", 48.74, 22.18, ["Sobrance (Slovakia)"]),  # Sobrance
    ("Strzegom", "Poland", 50.9611, 16.3444, ["Striegau"]),  # Strzegom
    ("Taba", "Egypt", 29.4917, 34.8944, ["Taba (Egypt)", "Taba Heights"]),  # Taba,_Egypt
    ("Środa Śląska", "Poland", 51.15, 16.583, ["Sroda Slaska", "Neumarkt in Schlesien"]),  # Środa_Śląska
    ("Junnar", "India", 19.2072, 73.8742, ["Junner"]),  # Junnar
    ("Karwar", "India", 14.8, 74.13, ["Karwar (India)", "Carwar"]),  # Karwar
    ("Kłodzko", "Poland", 50.4386, 16.655, ["Klodzko", "Glatz"]),  # Kłodzko
    ("Mahuli", "India", 19.4795, 73.2383, ["Mahuli Fort", "Mahuli (India)"]),  # Mahuli_Fort
    ("Rethymno", "Greece", 35.3689, 24.4739, ["Rethymnon", "Retimo", "Rethymno (Crete)"]),  # Rethymno
    ("Anklam", "Germany", 53.85, 13.683, ["Anklam (Germany)"]),  # Anklam
    ("Basavakalyan", "India", 17.8728, 76.9497, ["Kalyani", "Kalyana", "Kalyani Chalukya capital"]),  # Basavakalyan
    ("Beikthano", "Myanmar", 20.0039, 95.3794, ["Beikthano-myo", "Vishnu city"]),  # Beikthano
    ("Bouillon", "Belgium", 49.7955, 5.068, ["Bouillon (Belgium)"]),  # Bouillon,_Belgium
    ("Buncrana", "Ireland", 55.1364, -7.4561, []),  # Buncrana
    ("Castletownbere", "Ireland", 51.652, -9.909, ["Castletown Berehaven", "Castletownbere (Ireland)"]),  # Castletownbere
    ("Cefalù", "Italy", 38.035, 14.0211, ["Cefalu"]),  # Cefalù
    ("Chaeronea", "Greece", 38.495, 22.8475, ["Chaironeia", "Chaeroneia"]),  # Chaeronea
    ("Châteaudun", "France", 48.0717, 1.3387, ["Chateaudun"]),  # Châteaudun
    ("Cobh", "Ireland", 51.8511, -8.2967, ["Cove of Cork"]),  # Cobh
    ("Corycus", "Turkey", 36.4667, 34.15, ["Korykos", "Kızkalesi", "Kizkalesi", "Corycus (Turkey)"]),  # Kızkalesi
    ("Dan Sai", "Thailand", 17.28, 101.1467, ["Dan Sai (Thailand)"]),  # Dan_Sai_district
    ("Dendermonde", "Belgium", 51.0333, 4.1, ["Termonde"]),  # Dendermonde
    ("Elten", "Germany", 51.8711, 6.1597, ["Elten (Emmerich)"]),  # Elten
    ("Epidaurus", "Greece", 37.5978, 23.0744, ["Epidauros", "Epidavros"]),  # Epidaurus
    ("Erice", "Italy", 38.0369, 12.5864, ["Eryx"]),  # Erice
    ("Hanko", "Finland", 59.8283, 22.9658, ["Hangö", "Hango", "Hanko (Finland)"]),  # Hanko,_Finland
    ("Hawija", "Iraq", 35.325, 43.7722, ["Hawijah", "Al-Hawija"]),  # Hawija
    ("Hondarribia", "Spain", 43.3667, -1.7958, ["Fuenterrabía", "Fuenterrabia", "Hondarribia (Spain)"]),  # Hondarribia
    ("Kengtung", "Myanmar", 21.2917, 99.6083, ["Kyaingtong", "Chiang Tung", "Kentung", "Kengtung (Myanmar)"]),  # Kengtung
    ("Lectoure", "France", 43.9353, 0.6219, []),  # Lectoure
    ("Lier", "Belgium", 51.1333, 4.5667, ["Lierre", "Lier (Belgium)"]),  # Lier,_Belgium
    ("Mehran", "Iran", 33.1208, 46.1642, ["Mehran (Iran)"]),  # Mehran,_Ilam
    ("Menen", "Belgium", 50.8, 3.117, ["Menin", "Menen (Belgium)"]),  # Menen
    ("Naarden", "Netherlands", 52.2953, 5.1622, ["Naarden (Netherlands)"]),  # Naarden
    ("Nafpaktos", "Greece", 38.3939, 21.8306, ["Naupactus", "Lepanto", "Nafpaktos (Greece)"]),  # Nafpaktos
    ("Naxos", "Greece", 37.0875, 25.4039, ["Naxos island", "Naxos (Cyclades)"]),  # Naxos
    ("Orbetello", "Italy", 42.4428, 11.2247, ["Orbetello (Italy)"]),  # Orbetello
    ("Piombino", "Italy", 42.9167, 10.5333, ["Piombino (Italy)"]),  # Piombino
    ("Radom", "Poland", 51.4036, 21.1567, ["Radom (Poland)"]),  # Radom
    ("Riom", "France", 45.8944, 3.1133, ["Riom (Puy-de-Dôme)"]),  # Riom
    ("Saarlouis", "Germany", 49.317, 6.75, ["Saarlouis (Germany)", "Fort Louis"]),  # Saarlouis
    ("Samothrace", "Greece", 40.45, 25.5875, ["Samothraki", "Samothrake"]),  # Samothrace
    ("Sariñena", "Spain", 41.783, -0.167, ["Sarinena"]),  # Sariñena
    ("Selfkant", "Germany", 51.017, 5.917, ["Selfkant (Germany)"]),  # Selfkant
    ("Sinjar", "Iraq", 36.3225, 41.8642, ["Singara", "Shingal", "Sinjar (Iraq)"]),  # Sinjar
    ("Skiathos", "Greece", 39.1667, 23.4833, ["Skiathos island"]),  # Skiathos
    ("Skopelos", "Greece", 39.117, 23.717, ["Skopelos island"]),  # Skopelos
    ("Socotra", "Yemen", 12.51, 53.92, ["Soqotra", "Suqutra", "Socotra island"]),  # Socotra
    ("Suderwick", "Germany", 51.867, 6.5, ["Süderwick"]),  # Suderwick
    ("Tabas", "Iran", 33.5961, 56.9281, ["Tabas (Iran)"]),  # Tabas
    ("Taormina", "Italy", 37.8522, 15.2919, ["Tauromenium"]),  # Taormina
    ("Tarhuna", "Libya", 32.4339, 13.6344, ["Tarhunah"]),  # Tarhuna
    ("Tauste", "Spain", 41.9167, -1.25, []),  # Tauste
    ("Tegea", "Greece", 37.4553, 22.4205, ["Tegea (Arcadia)"]),  # Tegea
    ("Tilantongo", "Mexico", 17.25, -97.283, ["Tilantongo (Mixtec)"]),  # Tilantongo
    ("Tournai", "Belgium", 50.6056, 3.3881, ["Doornik", "Tournay"]),  # Tournai
    ("Tsorona", "Eritrea", 14.6213, 39.195, []),  # Tsorona
    ("Valenciennes", "France", 50.3581, 3.5233, []),  # Valenciennes
    ("Zalambessa", "Ethiopia", 14.5258, 39.3858, ["Zalanbessa"]),  # Zalambessa
    ("Świdnica", "Poland", 50.85, 16.483, ["Swidnica", "Schweidnitz"]),  # Świdnica
    ("Świebodzin", "Poland", 52.25, 15.533, ["Swiebodzin", "Schwiebus"]),  # Świebodzin
    ("Aasiaat", "Greenland", 68.7097, -52.8694, ["Egedesminde", "Aasiaat (Greenland)"]),  # Aasiaat
    ("Abu Hamed", "Sudan", 19.5433, 33.3378, ["Abu Hamad"]),  # Abu_Hamed
    ("Afrin", "Syria", 36.5083, 36.8692, ["Afrin (Syria)"]),  # Afrin,_Syria
    ("Amersfoort", "Netherlands", 52.15, 5.383, ["Amersfoort (Netherlands)"]),  # Amersfoort
    ("Aversa", "Italy", 40.967, 14.2, ["Aversa (Italy)"]),  # Aversa
    ("Bad Homburg vor der Höhe", "Germany", 50.2167, 8.6, ["Bad Homburg", "Homburg vor der Höhe"]),  # Bad_Homburg_vor_der_Höhe
    ("Bad Orb", "Germany", 50.217, 9.35, []),  # Bad_Orb
    ("Bagnone", "Italy", 44.3153, 9.9956, []),  # Bagnone
    ("Bassano del Grappa", "Italy", 45.7667, 11.7342, ["Bassano"]),  # Bassano_del_Grappa
    ("Beaufort Castle", "Lebanon", 33.3244, 35.532, ["Qalat al-Shaqif", "Belfort"]),  # Beaufort_Castle,_Lebanon
    ("Bram", "France", 43.2436, 2.1153, ["Bram (Aude)"]),  # Bram,_Aude
    ("Burg Stargard", "Germany", 53.4833, 13.3, ["Stargard (Mecklenburg)"]),  # Burg_Stargard
    ("Carrara", "Italy", 44.0792, 10.1, ["Carrara (Italy)"]),  # Carrara
    ("Chabanais", "France", 45.875, 0.7206, []),  # Chabanais
    ("Confolens", "France", 46.0144, 0.6733, ["Confolens (Charente)"]),  # Confolens
    ("Crema", "Italy", 45.3633, 9.6869, ["Crema (Lombardy)"]),  # Crema,_Lombardy
    ("Czeladź", "Poland", 50.3333, 19.0833, ["Czeladz"]),  # Czeladź
    ("Dixcove", "Ghana", 4.8, -1.95, ["Dix Cove", "Fort Metal Cross"]),  # Dixcove
    ("Elbistan", "Turkey", 38.2014, 37.1883, ["Elbistan (Turkey)"]),  # Elbistan
    ("Este", "Italy", 45.233, 11.667, ["Este (Veneto)", "Ateste"]),  # Este,_Veneto
    ("Feltre", "Italy", 46.0186, 11.91, []),  # Feltre
    ("Freising", "Germany", 48.4028, 11.7489, ["Freising (Germany)"]),  # Freising
    ("Gela", "Italy", 37.067, 14.25, ["Gela (Sicily)"]),  # Gela
    ("Gersfeld", "Germany", 50.45, 9.9167, ["Gersfeld (Rhön)"]),  # Gersfeld
    ("Gorizia", "Italy", 45.9333, 13.6167, ["Gorz", "Görz", "Gorica"]),  # Gorizia
    ("Halberstadt", "Germany", 51.8958, 11.0467, []),  # Halberstadt
    ("Hoym", "Germany", 51.783, 11.3, []),  # Hoym
    ("Igboho", "Nigeria", 8.8333, 3.75, ["Igboho (Nigeria)"]),  # Igboho
    ("Kamaran", "Yemen", 15.35, 42.5833, ["Kamaran island", "Kamaran Island"]),  # Kamaran
    ("Khan Tengri", "Kyrgyzstan", 42.2108, 80.175, ["Khan Tengri Peak"]),  # Khan_Tengri
    ("Knin", "Croatia", 44.0414, 16.1986, []),  # Knin
    ("Kobuleti", "Georgia", 41.8111, 41.7753, ["Kobuleti (Georgia)"]),  # Kobuleti
    ("Koźle", "Poland", 50.3353, 18.1458, ["Kozle", "Cosel"]),  # Koźle
    ("Kyburg", "Switzerland", 47.4585, 8.7435, ["Kyburg Castle", "Kiburg"]),  # Kyburg_Castle
    ("Lefkada", "Greece", 38.717, 20.65, ["Leucas", "Lefkas", "Santa Maura", "Leukas"]),  # Lefkada
    ("Legnica", "Poland", 51.2083, 16.1603, ["Liegnitz"]),  # Legnica
    ("Lienz", "Austria", 46.8297, 12.7697, []),  # Lienz
    ("Loudun", "France", 47.0106, 0.0844, []),  # Loudun
    ("Maniitsoq", "Greenland", 65.4167, -52.9, ["Sukkertoppen"]),  # Maniitsoq
    ("Massa", "Italy", 44.033, 10.133, ["Massa (Tuscany)", "Massa-Carrara"]),  # Massa,_Tuscany
    ("Melos", "Greece", 36.6875, 24.4325, ["Milos", "Milos island"]),  # Milos
    ("Mestre", "Italy", 45.4906, 12.2381, ["Venezia-Mestre"]),  # Mestre
    ("Minden", "Germany", 52.2883, 8.9167, ["Minden (Westphalia)"]),  # Minden
    ("Mixquic", "Mexico", 19.2249, -98.9643, ["San Andrés Mixquic"]),  # Mixquic
    ("Montbéliard", "France", 47.51, 6.8, ["Montbeliard", "Mömpelgard"]),  # Montbéliard
    ("Motozintla", "Mexico", 15.3708, -92.2483, ["Motozintla de Mendoza"]),  # Motozintla
    ("Nanortalik", "Greenland", 60.1419, -45.2433, ["Nennortalik"]),  # Nanortalik
    ("Neuburg an der Donau", "Germany", 48.733, 11.183, ["Neuburg"]),  # Neuburg_an_der_Donau
    ("Oropos", "Greece", 38.3, 23.75, ["Oropus"]),  # Oropos
    ("Pazin", "Croatia", 45.2403, 13.9367, ["Mitterburg", "Pisino"]),  # Pazin
    ("Perast", "Montenegro", 42.4869, 18.6992, []),  # Perast
    ("Preveza", "Greece", 38.9575, 20.7517, []),  # Preveza
    ("Qeqertarsuatsiaat", "Greenland", 63.0889, -50.6778, ["Fiskenæsset", "Fiskenaesset", "Fiskenæs"]),  # Qeqertarsuatsiaat
    ("Racibórz", "Poland", 50.0833, 18.2333, ["Raciborz", "Ratibor"]),  # Racibórz
    ("Rethel", "France", 49.5106, 4.3667, []),  # Rethel
    ("Roermond", "Netherlands", 51.2, 5.983, ["Roermond (Netherlands)"]),  # Roermond
    ("Rovinj", "Croatia", 45.0833, 13.6333, ["Rovigno"]),  # Rovinj
    ("Ruffec", "France", 46.0294, 0.2, ["Ruffec (Charente)"]),  # Ruffec,_Charente
    ("Safed", "Israel", 32.9658, 35.4983, ["Safad", "Tzfat", "Zefat", "Tsefat"]),  # Safed
    ("Salamis", "Greece", 37.9333, 23.5, ["Salamis island", "Salamis Island", "Salamina", "Salamina island"]),  # Salamis_Island
    ("Sanafir Island", "Saudi Arabia", 27.93, 34.71, ["Sanafir"]),  # Sanafir_Island
    ("Saverdun", "France", 43.2356, 1.5753, []),  # Saverdun
    ("Serpeysk", "Russia", 54.3353, 34.9889, ["Serpeisk"]),  # Serpeysk
    ("Sevsk", "Russia", 52.15, 34.5, ["Sevsk (Russia)"]),  # Sevsk
    ("Shama", "Ghana", 5.017, -1.633, ["Shama (Ghana)", "Sama"]),  # Shama,_Ghana
    ("Sidi Ifni", "Morocco", 29.3833, -10.1667, ["Ifni", "Santa Cruz de Mar Pequeña"]),  # Sidi_Ifni
    ("Suide", "China", 37.503, 110.263, ["Suide County"]),  # Suide_County
    ("Suncheon", "South Korea", 34.9506, 127.4875, ["Suncheon-si", "Sunchon (South Korea)"]),  # Suncheon
    ("Sutri", "Italy", 42.233, 12.283, ["Sutrium"]),  # Sutri
    ("Tiran Island", "Saudi Arabia", 27.9567, 34.5619, ["Tiran"]),  # Tiran_Island
    ("Trubchevsk", "Russia", 52.567, 33.767, []),  # Trubchevsk
    ("Vasai", "India", 19.47, 72.8, ["Bassein", "Baçaim", "Vasai-Virar"]),  # Vasai
    ("Vrgorac", "Croatia", 43.2, 17.3667, []),  # Vrgorac
    ("Wattala", "Sri Lanka", 6.983, 79.883, ["Wattala (Sri Lanka)"]),  # Wattala
    ("Wernigerode", "Germany", 51.835, 10.7853, []),  # Wernigerode
    ("Xochimilco", "Mexico", 19.275, -99.1389, []),  # Xochimilco
    ("Yan'an", "China", 36.65, 109.494, ["Yanan", "Yan'an (China)"]),  # Yan'an
    ("Zhalanashkol", "Kazakhstan", 45.5655, 82.1548, ["Lake Zhalanashkol", "Zhalanashkol (Kazakhstan)"]),  # Lake_Zhalanashkol
    ("Zhumadian", "China", 33.0139, 114.0219, []),  # Zhumadian
    ("Ruili", "China", 24.018, 97.856, ["Ruili (China)"]),  # Ruili
    ("Hawar Islands", "Bahrain", 25.6469, 50.7761, ["Hawar"]),  # Hawar_Islands
    ("Ksar es-Seghir", "Morocco", 35.8419, -5.5586, ["Alcácer Ceguer", "Alcacer Ceguer", "Ksar es Seghir", "Ksar-es-Seghir"]),  # Ksar_es-Seghir
    ("Dwarka", "India", 22.2464, 68.9667, ["Dwaraka", "Dvaraka"]),  # Dwarka
    ("Eupen", "Belgium", 50.6333, 6.0333, []),  # Eupen
    ("Malmedy", "Belgium", 50.417, 6.017, []),  # Malmedy
    ("Moree", "Ghana", 5.1333, -1.2, ["Moree (Ghana)", "Fort Amsterdam (Kormantin)"]),  # Moree,_Ghana
    ("Oldenzaal", "Netherlands", 52.317, 6.933, ["Oldenzaal (Netherlands)"]),  # Oldenzaal
    ("Coevorden", "Netherlands", 52.667, 6.75, ["Coevorden (Netherlands)"]),  # Coevorden
    ("Delfzijl", "Netherlands", 53.3333, 6.9167, ["Delfzijl (Netherlands)"]),  # Delfzijl
    ("Deventer", "Netherlands", 52.25, 6.15, ["Deventer (Netherlands)"]),  # Deventer
    ("Enschede", "Netherlands", 52.225, 6.8925, ["Enschede (Netherlands)"]),  # Enschede
    ("Nijmegen", "Netherlands", 51.8475, 5.8625, ["Nijmegen (Netherlands)", "Nimwegen", "Nijmegen Quarter"]),  # Nijmegen
    ("Ootmarsum", "Netherlands", 52.4072, 6.8994, ["Ootmarsum (Netherlands)"]),  # Ootmarsum
    ("Steenwijk", "Netherlands", 52.7889, 6.1267, ["Steenwijk (Netherlands)"]),  # Steenwijk
    ("Zutphen", "Netherlands", 52.14, 6.195, ["Zutphen (Netherlands)"]),  # Zutphen
    ("Guastalla", "Italy", 44.9167, 10.6667, []),  # Guastalla
    ("Megara", "Greece", 37.9964, 23.3444, ["Megara (Greece)"]),  # Megara
    ("Phalodi", "India", 27.131, 72.364, ["Phalodi (India)"]),  # Phalodi
    ("Alcañiz", "Spain", 41.0511, -0.1336, ["Alcaniz"]),  # Alcañiz
    ("Alghero", "Italy", 40.56, 8.315, ["Alghero (Italy)"]),  # Alghero
    ("Kafartab", "Syria", 35.4592, 36.5953, ["Kafr Tab", "Kafartab (Syria)"]),  # Kafartab
    ("Senya Beraku", "Ghana", 5.3878, -0.4925, ["Senya Bereku", "Fort Goede Hoop", "Senya Beraku (Ghana)"]),  # Senya_Beraku
    ("Tinos", "Greece", 37.617, 25.133, ["Tenos", "Tinos island"]),  # Tinos
    ("Xàtiva", "Spain", 38.9903, -0.5211, ["Xativa", "Játiva", "Jativa"]),  # Xàtiva
    ("Koroni", "Greece", 36.7949, 21.9629, ["Coron", "Corone", "Koroni (Messenia)"]),  # Koroni
    ("Qit'at Jaradah", "Bahrain", 26.178, 50.9, ["Qitat Jaradah", "Qit'at ash Shajarah", "Qit'at Jaradah island"]),  # Qit'at_Jaradah
    ("Kitzbühel", "Austria", 47.4464, 12.3919, ["Kitzbuhel"]),  # Kitzbühel
    ("Butre", "Ghana", 4.8231, -1.9169, ["Butri", "Fort Batenstein", "Butre (Ghana)"]),  # Butre,_Ghana
    ("Takoradi", "Ghana", 4.9167, -1.7667, ["Sekondi-Takoradi", "Takoradi (Ghana)", "Sekondi Takoradi"]),  # Sekondi-Takoradi
    ("Imbros", "Turkey", 40.1608, 25.8444, ["Gökçeada", "Gokceada", "Imroz"]),  # Imbros
    ("Tenedos", "Turkey", 39.8219, 26.0289, ["Bozcaada"]),  # Tenedos
    ("Mantineia", "Greece", 37.6176, 22.3929, ["Mantinea", "Mantinea (Arcadia)"]),  # Mantinea
    ("Ascalon", "Israel", 31.6639, 34.5458, ["Ashkelon", "Ashkelon National Park", "Askalon", "Ascalon (Israel)"]),  # Ashkelon_National_Park
    ("Barmer", "India", 25.75, 71.38, ["Barmer (India)"]),  # Barmer,_Rajasthan
    ("Buka", "Papua New Guinea", -5.4219, 154.6728, ["Buka (Papua New Guinea)", "Buka town", "Buka Island"]),  # Buka,_Papua_New_Guinea
    ("Chifra", "Ethiopia", 11.6039, 40.0166, ["Chifra (Ethiopia)", "Chifra woreda"]),  # Chifra_(woreda)
    ("Gex", "France", 46.3333, 6.0578, ["Gex (France)"]),  # Gex,_Ain
    ("Hasankeyf", "Turkey", 37.717, 41.417, ["Hisn Kayfa", "Hasan Keyf", "Hisn Kayfa (Hasankeyf)"]),  # Hasankeyf_District
    ("Janjira", "India", 18.2996, 72.9644, ["Murud-Janjira", "Janjira Fort", "Murud Janjira"]),  # Murud-Janjira
    ("Kexholm", "Russia", 61.05, 30.133, ["Priozersk", "Käkisalmi", "Kakisalmi", "Korela"]),  # Priozersk
    ("Laguardia", "Spain", 42.5533, -2.585, ["Laguardia (Álava)", "Biasteri"]),  # Laguardia,_Álava
    ("Landau", "Germany", 49.2, 8.117, ["Landau in der Pfalz", "Landau (Germany)"]),  # Landau
    ("Majnoon Island", "Iraq", 31.0842, 47.4542, ["Majnoon Islands", "Majnun Island"]),  # Majnoon_Island
    ("Megalopolis", "Greece", 37.4, 22.1333, ["Megalopoli"]),  # Megalopolis,_Greece
    ("Qadmus", "Syria", 35.1014, 36.1611, ["Al-Qadmus", "Qadmus (Syria)", "Qadmus Castle", "al-Qadmus"]),  # Al-Qadmus
    ("Kahf", "Syria", 35.0407, 36.083, ["Al-Kahf", "Al-Kahf Castle", "Qalaat al-Kahf", "Kahf (Syria)", "al-Kahf"]),  # Al-Kahf_Castle
    # Added 3 Nov 2026 by the second gazetteer gap-fill (the 47 names the test compile of 2 Nov left unresolved). Same rule as 1 Nov:
    # coordinates read from the page named in the comment (en.wikipedia.org/wiki/<page> unless the comment starts with another
    # language code; opened with WebFetch on 3 Nov 2026), not from memory. Only the canonical article title gives the infobox
    # coordinates through WebFetch (a redirect title, e.g. Woldia for Weldiya, returns none); de.wikipedia pages show them as a
    # GeoHack link, which is where the decimals of the de entries come from. 25 places; the rest are listed in the README.
    ("Weldiya", "Ethiopia", 11.8306, 39.6, ["Woldia", "Woldiya", "Welidiya"]),  # Weldiya
    ("Usvyaty", "Russia", 55.7486, 30.7556, []),  # Usvyaty,_Usvyatsky_District,_Pskov_Oblast (Usvyaty alone is a disambiguation page)
    ("Ullaiqah", "Syria", 35.1769, 36.1222, ["Aleika", "Aleika Castle", "Aliqa", "Al-Ullaiqah", "Ullaiqah Castle"]),  # Aleika_Castle (the Nizari castle near Tartus, not a town)
    ("Rusafa", "Syria", 35.0331, 36.3025, ["Al-Rusafa (Syria)", "Rusafa (Masyaf)", "Ar-Rusafa", "Rusafa Castle"]),  # Al-Rusafa,_Syria (Masyaf Subdistrict, Hama; the Nizari castle, not Resafa near Raqqa)
    ("Khawabi", "Syria", 34.9728, 36.0022, ["Qalaat al-Khawabi", "Qala'at al-Khawabi", "Khawabi Castle", "La Coible", "Al-Khawabi"]),  # Khawabi (infobox title Khawabi Castle, Tartus Governorate)
    ("Lambsar", "Iran", 36.5476, 50.2273, ["Lambsar Castle", "Lamasar", "Lamiasar", "Lamasar Castle"]),  # Lambsar_Castle
    ("Oyón", "Spain", 42.5058, -2.4364, ["Oion", "Oyón-Oion", "Oyon-Oion"]),  # Oyón-Oion
    ("Nevel", "Russia", 56.033, 29.917, ["Nevel (town)"]),  # Nevel_(town) (Nevel alone is a disambiguation page)
    ("Mirebeau", "France", 46.7858, 0.1825, ["Mirebeau (Vienne)", "Mirebeau-en-Poitou", "Mirebeau, Vienne"]),  # Mirebeau (the commune in Vienne, Nouvelle-Aquitaine)
    ("Kaulsdorf", "Germany", 50.633, 11.433, ["Kaulsdorf (Saale)", "Kaulsdorf an der Saale"]),  # Kaulsdorf_(Saale) (Saalfeld-Rudolstadt, Thuringia; the Berlin district Kaulsdorf is a different place)
    ("Saqqaq", "Greenland", 70.0097, -51.9458, []),  # Saqqaq
    ("Dolon Nur", "China", 42.183, 116.467, ["Dolonnur", "Dolonnuur", "Dolon-Nur", "Duolun", "Duolun Town"]),  # Duolun_County (infobox coordinates of the county; Dolonnur town is the seat)
    ("Haj Omran", "Iraq", 36.6581, 45.0397, ["Haji Omeran", "Haji Omaran", "Hajj Umran", "Haj Umran"]),  # Haji_Omeran
    ("Barentu", "Eritrea", 15.1167, 37.6, ["Barentu (Eritrea)"]),  # Barentu,_Eritrea (Barentu alone is a disambiguation page)
    ("Sikyon", "Greece", 38.0, 22.733, ["Sicyon", "Sikyona", "Sicyon (Corinthia)"]),  # Sikyona (the modern village, formerly Vasiliko, beside the ancient site; the Sicyon page prints no coordinates)
    ("Phlius", "Greece", 37.8455, 22.6463, ["Phleius", "Phlious"]),  # de: Phleius (GeoHack 37.845472 N 22.646333 E)
    ("Decelea", "Greece", 38.1528, 23.7942, ["Dekeleia", "Dekelea"]),  # de: Dekeleia (GeoHack 38.152778 N 23.794167 E; the en Decelea page prints none)
    ("Coronea", "Greece", 38.3925, 22.9569, ["Koroneia", "Coroneia", "Koroneia (Boeotia)"]),  # de: Koroneia (GeoHack 38.3925 N 22.956944 E; the en Coroneia (Boeotia) page prints none)
    ("Cempoala", "Mexico", 19.4472, -96.4042, ["Zempoala (Veracruz)", "Cempoala (Veracruz)"]),  # de: Zempoala (title Cempoala; GeoHack 19.447222 N 96.404167 W; Totonac city in Veracruz)
    ("Cuitlahuac", "Mexico", 19.2878, -99.0075, ["Cuitláhuac (Tláhuac)", "Tláhuac", "Tlahuac"]),  # de: Tláhuac (GeoHack 19.28781 N 99.00753 W; the Tláhuac altepetl; Cuitláhuac, Veracruz is another place)
    ("Bonampak", "Mexico", 16.7319, -91.0681, []),  # de: Bonampak (GeoHack 16.731944 N 91.068056 W; the en page prints none)
    ("Sawankhalok", "Thailand", 17.3167, 99.8317, ["Sawankhaloke"]),  # de: Sawankhalok (GeoHack 17.316667 N 99.831667 E; the en page prints none)
    ("Halin", "Myanmar", 22.4833, 95.85, ["Halingyi", "Halin (Myanmar)"]),  # de: Halin (GeoHack 22.483333 N 95.85 E; the Pyu city)
    ("Keta", "Ghana", 5.9031, 0.9868, ["Keta (Ghana)"]),  # Keta_Municipal_District (infobox coordinates of the district, capital Keta; the Keta page prints none; the lake Keta Lagoon is a lakes.jsonl row)
    ("Monfragüe", "Spain", 39.8286, -6.0506, ["Castillo de Monfragüe", "Monfragüe Castle"]),  # Parque Nacional de Monfragüe (the one coordinate pair on the page is the Cueva del Castillo de Monfragüe, on the castle hill of the Order of Monfragüe; the page prints no centre for the park)
]

# River aliases keyed by the English name used in rivers.jsonl
RIVER_ALIASES = {
    "Amu Darya": ["Oxus", "Amu", "Jayhun", "Amudarya"],
    "Syr Darya": ["Jaxartes", "Sayhun", "Syrdarya", "Syr"],
    "Euphrates": ["Al Furat", "Firat", "Purattu"],
    "Tigris": ["Dijla", "Dicle", "Idiglat"],
    "Nile": ["Nil", "Iteru"],
    "Blue Nile": ["Abay"],
    "White Nile": ["Bahr al-Jabal"],
    "Indus": ["Sindhu", "Sindh (river)"],
    "Ganges": ["Ganga"],
    "Brahmaputra": ["Yarlung Tsangpo", "Jamuna"],
    "Yangtze": ["Chang Jiang", "Changjiang", "Yangzi", "Yangtze River"],
    "Yellow": ["Yellow River", "Huang He", "Hwang Ho", "Huanghe"],
    "Grande": ["Rio Grande", "Rio Bravo", "Rio Bravo del Norte"],
    "Paraná River": ["Parana", "Paraná", "Parana River"],
    "Syr Dar": ["Syr Darya", "Jaxartes", "Sayhun", "Syrdarya", "Syr"],
    "Red of the South": ["Red River (USA)", "Red River of the South"],
    "Red": ["Red River", "Red River (Vietnam)", "Song Hong", "Hong", "Red River of the North"],
    "Hari": ["Hari Rud", "Harirud", "Tejen", "Harī Rūd"],
    "Kızılırmak": ["Halys", "Kizilirmak", "Kizil Irmak"],
    "Büyük Menderes": ["Maeander", "Meander", "Buyuk Menderes"],
    "Rhône": ["Rhone", "Rhodanus"],
    "Mureș": ["Mures", "Maros"],
    "São Francisco": ["Sao Francisco"],
    "Panj": ["Pyandzh", "Panj (upper Oxus)"],
    "Yarkand": ["Yarkand River", "Yarkant"],
    "Jinsha": ["Jinsha Jiang", "upper Yangtze"],
    "Pearl": ["Zhu Jiang", "Pearl River"],
    "Western Bug": ["Bug", "Buh"],
    "Northern Dvina": ["Dvina (Northern)", "Severnaya Dvina"],
    "Kherlen": ["Kerulen", "Herlen"],
    "Yarlung": ["Yarlung Tsangpo", "Tsangpo"],
    "Chao Phraya": ["Menam"],
    "Sutlej": ["Satluj", "Hesidros"],
    "Jhelum": ["Hydaspes", "Vitasta"],
    "Chenab": ["Acesines", "Chandrabhaga"],
    "Ravi": ["Hydraotes", "Iravati"],
    "Beas": ["Hyphasis", "Vipasa"],
    "Kaveri": ["Cauvery", "Kaveri River"],
    "Krishna": ["Kistna"],
    "Godavari": [],
    "Narmada": ["Nerbudda"],
    "Yamuna": ["Jumna"],
    "Ghaghara": ["Karnali", "Gogra"],
    "Mahanadi": [],
    "Chambal": [],
    "Tapti": ["Tapi"],
    "Karkheh": ["Choaspes"],
    "Karun": ["Pasitigris"],
    "Qezel Uzan": ["Qizil Uzun", "Sefid Rud (upper)"],
    "Atbarah": ["Atbara"],
    "Tekezé": ["Tekeze", "Setit"],
    "Awash": [],
    "Omo": [],
    "Chari": ["Shari"],
    "Logone": [],
    "Yobe": ["Komadugu Yobe"],
    "Black Volta": ["Mouhoun"],
    "White Volta": ["Nakambe"],
    "Volta": [],
    "Komoé": ["Comoe", "Komoe"],
    "Bani": [],
    "Sokoto": [],
    "Kasai": ["Kasaï"],
    "Lualaba": ["upper Congo"],
    "Ubangi": ["Oubangui"],
    "Kwango": ["Cuango"],
    "Cuanza": ["Kwanza"],
    "Cunene": ["Kunene"],
    "Okavango": ["Cubango"],
    "Kafue": [],
    "Luangwa": [],
    "Shire": [],
    "Ruvuma": ["Rovuma"],
    "Rufiji": [],
    "Vaal": [],
    "Oum Er-Rbia": ["Oum er-Rbia", "Umm al-Rabi"],
    "Moulouya": ["Muluya"],
    "Sebou": ["Sebu"],
    "Severn": ["Sabrina"],
    "Meuse": ["Maas", "Mosa"],
    "Moselle": ["Mosel", "Mosella"],
    "Main": ["Moenus"],
    "Weser": ["Visurgis"],
    "Inn": ["Aenus"],
    "Mur": ["Mura"],
    "Drina": [],
    "Great Morava": ["Morava", "Margus"],
    "Warta": ["Warthe"],
    "Prypiat": ["Pripyat", "Prypiat'", "Pripet"],
    "Desna": [],
    "Donets": ["Seversky Donets", "Siverskyi Donets"],
    "Kuban": ["Hypanis (Kuban)"],
    "Kama": [],
    "Oka": [],
    "Belaya": [],
    "Vyatka": [],
    "Pechora": [],
    "Tobol": [],
    "Ishim": ["Esil"],
    "Irtysh": ["Ertis", "Irtish"],
    "Ob": ["Ob'"],
    "Yenisey": ["Yenisei", "Enisei"],
    "Angara": [],
    "Selenga": ["Selenge"],
    "Onon": [],
    "Ingoda": [],
    "Shilka": [],
    "Argun": ["Ergun", "Argun'"],
    "Songhua": ["Sungari"],
    "Nen": ["Nonni", "Nen Jiang"],
    "Ussuri": ["Wusuli"],
    "Liao": ["Liao He", "Liao River"],
    "Luan": ["Luan He"],
    "Fen": ["Fen He"],
    "Wei": ["Wei He", "Wei River"],
    "Han": ["Han River", "Han Shui", "Han Jiang"],
    "Huai": ["Huai He", "Huai River"],
    "Xiang": ["Xiang Jiang"],
    "Gan": ["Gan Jiang"],
    "Min": ["Min Jiang"],
    "Jialing": ["Jialing Jiang"],
    "Wu": ["Wu Jiang"],
    "Yuan": ["Yuan Jiang"],
    "Xi": ["Xi Jiang", "West River"],
    "Nanpan": [],
    "Hongshui": [],
    "Tarim": ["Tarim River"],
    "Ili": ["Ili River", "Yili"],
    "Naryn": [],
    "Nakdong": ["Naktong"],
    "Tumen": ["Duman", "Tumen River"],
    "Yalu": ["Amnok", "Yalu River"],
    "Chindwin": [],
    "Sittong": ["Sittaung"],
    "Salween": ["Thanlwin", "Nu Jiang"],
    "Mekong": ["Lancang", "Mekong River"],
    "Mun": [],
    "Chi": [],
    "Mae Klong": [],
    "Ping": [],
    "Yom": [],
    "Kapuas": [],
    "Mahakam": [],
    "Barito": [],
    "Fly": [],
    "Sepik": [],
    "Murray": ["Murray River"],
    "Darling": ["Darling River"],
    "Mississippi": ["Mississippi River"],
    "Missouri": ["Missouri River"],
    "Ohio": ["Ohio River"],
    "Tennessee": ["Tennessee River"],
    "Arkansas": ["Arkansas River"],
    "Platte": ["Platte River"],
    "Colorado": ["Colorado River"],
    "Columbia": ["Columbia River"],
    "Snake": ["Snake River"],
    "Sacramento": ["Sacramento River"],
    "San Joaquin": [],
    "Gila": ["Gila River"],
    "Pecos": [],
    "Brazos": [],
    "Sabine": ["Sabine River"],
    "Canadian": ["Canadian River"],
    "Wabash": [],
    "Illinois": ["Illinois River"],
    "Cumberland": ["Cumberland River"],
    "Alabama": ["Alabama River"],
    "Tombigbee": [],
    "Chattahoochee": [],
    "Savannah": ["Savannah River"],
    "Potomac": ["Potomac River"],
    "Susquehanna": [],
    "Delaware": ["Delaware River"],
    "Hudson": ["Hudson River"],
    "Connecticut": ["Connecticut River"],
    "James": ["James River"],
    "Roanoke": ["Roanoke River"],
    "Saint John": ["St. John"],
    "Ottawa": ["Ottawa River", "Outaouais"],
    "Saguenay": [],
    "Churchill": ["Churchill River"],
    "Nelson": ["Nelson River"],
    "Saskatchewan": ["Saskatchewan River"],
    "North Saskatchewan": [],
    "South Saskatchewan": [],
    "Assiniboine": [],
    "Winnipeg": ["Winnipeg River"],
    "Athabasca": [],
    "Peace": ["Peace River"],
    "Slave": ["Slave River"],
    "Mackenzie": ["Mackenzie River"],
    "Liard": [],
    "Fraser": ["Fraser River"],
    "Yukon": ["Yukon River"],
    "Amazon": ["Amazonas", "Solimões", "Amazon River"],
    "Negro": ["Rio Negro"],
    "Madeira": ["Rio Madeira"],
    "Purus": [],
    "Jurua": ["Juruá"],
    "Ucayali": [],
    "Marañón": ["Maranon"],
    "Napo": [],
    "Putumayo": ["Içá"],
    "Japurá": ["Caquetá", "Japura"],
    "Xingu": [],
    "Tapajós": ["Tapajos"],
    "Tocantins": [],
    "Araguaia": [],
    "Orinoco": ["Orinoco River"],
    "Meta": [],
    "Apure": [],
    "Caroní": ["Caroni"],
    "Magdalena": ["Magdalena River"],
    "Cauca": [],
    "Essequibo": [],
    "Paraguay": ["Rio Paraguay", "Paraguay River"],
    "Uruguay": ["Rio Uruguay", "Uruguay River"],
    "Pilcomayo River": ["Pilcomayo"],
    "Bermejo": [],
    "Salado": ["Rio Salado"],
    "Desaguadero": [],
    "Beni": [],
    "Mamoré": ["Mamore"],
    "Bío Bío": ["Biobio", "Bio Bio"],
    "Grijalva": [],
    "Usumacinta": [],
    "Balsas": [],
    "Lerma": [],
    "Yaqui": [],
    "Conchos": [],
    "Motagua": [],
    "Coco": ["Segovia", "Wanks"],
    "San Juan": ["San Juan River"],
    "Dnieper": ["Dnipro", "Dnepr", "Borysthenes", "Dnieper River"],
    "Dniester": ["Dnister", "Nistru", "Tyras (river)"],
    "Don": ["Tanais", "Don River"],
    "Volga": ["Itil (river)", "Rha", "Volga River"],
    "Ural": ["Yaik", "Jaik", "Ural River"],
    "Daugava": ["Western Dvina", "Dvina (Western)", "Düna", "Zapadnaya Dvina"],
    "Neris": ["Vilija"],
    "Msta": [],
    "Svir": [],
    "Glomma": ["Glåma"],
    "Dalälven": ["Dalalven"],
    "Tana": ["Tana River"],
    "Jubba": ["Juba"],
    "Shebelle": ["Shabelle", "Webi Shabeelle"],
    "Genale": ["Ganale"],
    "Euphrates": ["Al Furat", "Firat", "Purattu", "Fırat"],
    "Tigris": ["Dijla", "Dicle", "Idiglat"],
    "Nile": ["Nil", "Iteru", "Nile River"],
    "Blue Nile": ["Abay", "Abbai"],
    "White Nile": ["Bahr al-Jabal", "Albert Nile"],
    "Indus": ["Sindhu", "Sindh (river)", "Indus River"],
    "Ganges": ["Ganga", "Ganges River"],
    "Brahmaputra": ["Jamuna", "Brahmaputra River"],
    "Irrawaddy": ["Ayeyarwady", "Irrawaddy River"],
    "Amu Darya": ["Oxus", "Amu", "Jayhun", "Amudarya", "Amu Darya River"],
    "Danube": ["Donau", "Dunaj", "Dunav", "Duna", "Dunarea", "Ister", "Danube River"],
    "Rhine": ["Rhein", "Rijn", "Rhenus", "Rhine River"],
    "Elbe": ["Labe", "Albis"],
    "Oder": ["Odra"],
    "Vistula": ["Wisla", "Wisła", "Weichsel"],
    "Loire": ["Liger"],
    "Seine": ["Sequana"],
    "Garonne": ["Garumna"],
    "Dordogne": [],
    "Vienne": ["Vienne (river)"],
    "Marne": [],
    "Doubs": [],
    "Ebro": ["Iberus"],
    "Tagus": ["Tajo", "Tejo"],
    "Douro": ["Duero"],
    "Guadalquivir": ["Baetis"],
    "Guadiana": ["Anas"],
    "Po": ["Padus", "Eridanos"],
    "Adige": ["Etsch"],
    "Maritsa": ["Evros", "Meriç", "Hebrus"],
    "Sava": ["Save (Sava)"],
    "Drava": ["Drau"],
    "Tisza": ["Tisa", "Theiss"],
    "Olt": ["Aluta"],
    "Prut": ["Pruth"],
    "Southern Bug": ["Boh", "Hypanis", "Pivdennyi Buh"],
    "Kura": ["Mtkvari", "Cyrus"],
    "Aras": ["Araxes", "Araks"],
    "Helmand": ["Hilmand", "Etymander"],
    "Zeravshan": ["Zarafshan", "Polytimetus"],
    "Lena": ["Lena River"],
    "Amur": ["Heilong Jiang", "Heilongjiang", "Amur River"],
    "Orkhon": ["Orhon"],
    "Niger": ["Joliba", "Kwara", "Niger River"],
    "Senegal": ["Senegal River"],
    "Gambia": ["Gambia River"],
    "Benue": ["Benue River"],
    "Congo": ["Zaire (river)", "Congo River"],
    "Zambezi": ["Zambeze", "Zambezi River"],
    "Limpopo": ["Limpopo River"],
    "Orange": ["Gariep", "Orange River"],
    "Atrek": ["Atrak"],
    "Pearl": ["Zhu Jiang", "Pearl River"],
    "Xi": ["Xi Jiang", "West River"],
    "Mekong": ["Lancang"],
    "Irrawaddy": ["Ayeyarwady"],
    "Salween": ["Thanlwin", "Nu"],
    "Red": ["Red River (Vietnam)", "Song Hong", "Hong"],
    "Danube": ["Donau", "Dunaj", "Dunav", "Duna", "Dunarea", "Ister"],
    "Rhine": ["Rhein", "Rijn", "Rhenus"],
    "Elbe": ["Labe", "Albis"],
    "Oder": ["Odra"],
    "Vistula": ["Wisla", "Wisła", "Weichsel"],
    "Dnieper": ["Dnipro", "Dnepr", "Borysthenes"],
    "Dniester": ["Dnister", "Nistru", "Tyras (river)"],
    "Don": ["Tanais"],
    "Volga": ["Itil (river)", "Rha"],
    "Ural": ["Yaik", "Jaik"],
    "Daugava": ["Western Dvina", "Dvina (Western)", "Düna"],
    "Neman": ["Nemunas", "Memel (river)", "Niemen"],
    "Prut": ["Pruth"],
    "Southern Bug": ["Boh", "Hypanis"],
    "Loire": ["Liger"],
    "Seine": ["Sequana"],
    "Rhone": ["Rhône", "Rhodanus"],
    "Garonne": ["Garumna"],
    "Ebro": ["Iberus"],
    "Tagus": ["Tajo", "Tejo"],
    "Douro": ["Duero"],
    "Guadalquivir": ["Baetis"],
    "Guadiana": ["Anas"],
    "Po": ["Padus", "Eridanos"],
    "Tiber": ["Tevere", "Tiberis"],
    "Adige": ["Etsch"],
    "Thames": ["Tamesis"],
    "Severn": ["Sabrina"],
    "Humber": [],
    "Shannon": [],
    "Maritsa": ["Evros", "Meriç", "Hebrus"],
    "Vardar": ["Axios"],
    "Sava": ["Save"],
    "Drava": ["Drau"],
    "Tisza": ["Tisa", "Theiss"],
    "Mures": ["Maros", "Mureș"],
    "Olt": ["Aluta"],
    "Siret": [],
    "Kizilirmak": ["Halys", "Kızılırmak"],
    "Sakarya": ["Sangarius"],
    "Buyuk Menderes": ["Maeander", "Meander", "Büyük Menderes"],
    "Kura": ["Mtkvari", "Cyrus"],
    "Aras": ["Araxes", "Araks"],
    "Helmand": ["Hilmand", "Etymander"],
    "Hari": ["Hari Rud", "Harirud", "Tejen"],
    "Murghab": ["Murgab"],
    "Zeravshan": ["Zarafshan", "Polytimetus"],
    "Ili": [],
    "Chu": [],
    "Irtysh": ["Ertis"],
    "Ob": [],
    "Yenisey": ["Yenisei"],
    "Lena": [],
    "Amur": ["Heilong Jiang", "Heilongjiang"],
    "Songhua": ["Sungari"],
    "Liao": ["Liao He"],
    "Yalu": ["Amnok"],
    "Tumen": ["Duman"],
    "Han": ["Han River"],
    "Wei": ["Wei He"],
    "Huai": ["Huai He"],
    "Tarim": [],
    "Orkhon": ["Orhon"],
    "Selenga": ["Selenge"],
    "Kerulen": ["Kherlen"],
    "Niger": ["Joliba", "Kwara"],
    "Senegal": [],
    "Gambia": [],
    "Benue": [],
    "Congo": ["Zaire (river)"],
    "Zambezi": ["Zambeze"],
    "Limpopo": [],
    "Orange": ["Gariep"],
    "Shebelle": ["Shabelle"],
    "Juba": ["Jubba"],
    "Mississippi": [],
    "Missouri": [],
    "Ohio": [],
    "Tennessee": [],
    "Arkansas": [],
    "Red (USA)": [],
    "Rio Grande": ["Rio Bravo"],
    "Colorado": [],
    "Columbia": [],
    "Snake": [],
    "Sacramento": [],
    "Hudson": [],
    "Saint Lawrence": ["St. Lawrence", "Saint-Laurent"],
    "Saskatchewan": [],
    "Mackenzie": [],
    "Yukon": [],
    "Amazon": ["Amazonas", "Solimões"],
    "Orinoco": [],
    "Magdalena": [],
    "Parana": ["Paraná"],
    "Paraguay": [],
    "Uruguay": [],
    "Sao Francisco": ["São Francisco"],
    "Tocantins": [],
    "Madeira": [],
    "Negro": ["Rio Negro"],
    "Murray": [],
    "Darling": [],
    "Jordan": ["Nahr al-Urdun"],
    "Orontes": ["Asi", "Al Asi"],
    "Litani": ["Leontes"],
    "Karun": [],
    "Sefid Rud": ["Sefid", "Safid Rud"],
    "Atrek": ["Atrak"],
    "Gorgan": [],
}


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------

def norm(s):
    s = unicodedata.normalize("NFKD", str(s))
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return " ".join(s.lower().replace("'", "").replace("`", "").replace("-", " ").split())


def clean_names(primary, candidates):
    """Dedupe alternative names: non-empty, not -99, not equal to the primary (ignoring case/accents)."""
    seen = {norm(primary)}
    out = []
    for c in candidates:
        if c is None:
            continue
        for part in str(c).split("|"):
            part = part.strip()
            if not part or part in ("-99", "None") or part.startswith("-99"):
                continue
            k = norm(part)
            if not k or k in seen:
                continue
            seen.add(k)
            out.append(part)
    return out


def ascii_only(names):
    """Keep names whose characters are Latin script (after NFKD), so the file stays small."""
    out = []
    for n in names:
        s = unicodedata.normalize("NFKD", n)
        s = "".join(ch for ch in s if not unicodedata.combining(ch))
        if all(ord(ch) < 0x250 for ch in s):
            out.append(n)
    return out


def cells_to_runs(cells_h3, land):
    idx = [land[c] for c in cells_h3 if c in land]
    return grid.to_runs(idx), len(idx)


def area_cells(geom, land):
    """Land cells of an areal geometry as (runs, n, moved).

    grid.shape_cells gives the cells whose centre is inside the shape (plus the centroid cell of
    a shape smaller than one cell). When none of those is a land cell (Gibraltar, Monaco, Macao,
    an atoll), the nearest land cell within two rings of the centroid is used and moved is True.
    """
    cells = grid.shape_cells(geom, RES)
    runs, n = cells_to_runs(cells, land)
    if n:
        return runs, n, False
    polys = grid.prepare_polygons(geom)
    if not polys:
        return [], 0, False
    best = max(polys, key=lambda p: p.area)
    c = best.centroid if best.contains(best.centroid) else best.representative_point()
    c0 = h3.latlng_to_cell(c.y, c.x, RES)
    for k in (1, 2):
        ring = [x for x in h3.grid_ring(c0, k) if x in land]
        if ring:
            near = min(ring, key=lambda x: haversine_km(c.y, c.x, *h3.cell_to_latlng(x)))
            return [land[near]], 1, True
    return [], 0, False


_RIVER_ALIAS_NORM = {norm(k): v for k, v in RIVER_ALIASES.items()}


def reader(name):
    return shapefile.Reader(str(WORK / name / (name + ".shp")))


def write_jsonl(path, rows):
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False, separators=(",", ":")))
            f.write("\n")
    os.replace(tmp, path)
    print("wrote %s: %d rows, %.1f KB" % (path.name, len(rows), path.stat().st_size / 1024), file=sys.stderr)


# ----------------------------------------------------------------------------
# Builders
# ----------------------------------------------------------------------------

def build_countries(land):
    t = time.time()
    r = reader("ne_10m_admin_0_countries")
    fields = [f[0] for f in r.fields[1:]]
    rows = []
    for sr in r.iterShapeRecords():
        d = dict(zip(fields, sr.record))
        name = d["NAME"]
        if name == "Antarctica":
            continue
        iso = d["ISO_A3"]
        if iso == "-99":
            iso = d["ISO_A3_EH"] if d["ISO_A3_EH"] != "-99" else d["ADM0_A3"]
        alts = clean_names(name, [d["NAME_LONG"], d["ADMIN"], d["FORMAL_EN"], d["NAME_EN"], d["NAME_ALT"],
                                  d["GEOUNIT"], d["SUBUNIT"], d["BRK_NAME"], d["NAME_CIAWF"], d["NAME_SORT"],
                                  d["ABBREV"]] + [d["NAME_" + k.upper()] for k in LATIN]
                           + COUNTRY_ALIASES.get(name, []))
        alts = ascii_only(alts)
        geom = shape(sr.shape.__geo_interface__)
        runs, n, moved = area_cells(geom, land)
        row = {"name": name, "iso_a3": iso, "adm0_a3": d["ADM0_A3"], "type": d["TYPE"],
               "continent": d["CONTINENT"], "alt_names": alts, "n_cells": n, "cells": runs}
        if moved:
            row["cell_moved"] = True
        rows.append(row)
    rows.sort(key=lambda x: x["name"])
    write_jsonl(OUT / "countries.jsonl", rows)
    print("countries: %d rows, %d cells, %.0f s" % (len(rows), sum(x["n_cells"] for x in rows), time.time() - t),
          file=sys.stderr)


def build_admin1(land):
    t = time.time()
    r = reader("ne_10m_admin_1_states_provinces")
    fields = [f[0] for f in r.fields[1:]]
    rows = []
    for i, sr in enumerate(r.iterShapeRecords()):
        d = dict(zip(fields, sr.record))
        name = (d["name"] or "").strip() or (d["name_en"] or "").strip() or (d["gn_name"] or "").strip() \
            or (d["woe_name"] or "").strip()
        if not name:
            continue
        if d["admin"] == "Antarctica":
            continue
        alts = clean_names(name, [d["name_alt"], d["name_local"], d["name_en"], d["woe_name"], d["gn_name"],
                                  d["gns_name"], d["abbrev"]] + [d["name_" + k] for k in LATIN])
        alts = ascii_only(alts)
        geom = shape(sr.shape.__geo_interface__)
        runs, n, moved = area_cells(geom, land)
        row = {"name": name, "country": d["admin"], "adm0_a3": d["adm0_a3"], "iso": d["iso_3166_2"],
               "type": d["type_en"] or d["type"], "region": d["region"] or "",
               "alt_names": alts, "n_cells": n, "cells": runs}
        if moved:
            row["cell_moved"] = True
        rows.append(row)
        if (i + 1) % 500 == 0:
            print("  admin1 %d/%d, %.0f s" % (i + 1, len(r), time.time() - t), file=sys.stderr)
    rows.sort(key=lambda x: (x["country"], x["name"]))
    write_jsonl(OUT / "admin1.jsonl", rows)
    print("admin1: %d rows, %d cells, %.0f s" % (len(rows), sum(x["n_cells"] for x in rows), time.time() - t),
          file=sys.stderr)


def _line_cells(geom, res=RES, step_deg=0.01):
    """Cells a line passes through: sample vertices after densifying to ~1 km."""
    import shapely
    dense = shapely.segmentize(geom, step_deg)
    cells = set()
    coords = shapely.get_coordinates(dense)
    for x, y in coords:
        cells.add(h3.latlng_to_cell(float(y), float(x), res))
    return cells


def build_rivers(land):
    t = time.time()
    r = reader("ne_10m_rivers_lake_centerlines")
    fields = [f[0] for f in r.fields[1:]]
    groups = collections.OrderedDict()
    for sr in r.iterShapeRecords():
        d = dict(zip(fields, sr.record))
        name = (d["name_en"] or "").strip() or (d["name"] or "").strip()
        if not name:
            continue
        geom = shape(sr.shape.__geo_interface__)
        g = groups.setdefault(name, {"cells": set(), "alts": [], "cla": set(), "km": 0.0})
        g["cells"] |= _line_cells(geom)
        g["alts"].extend([d["name"], d["name_alt"], d["name_en"]] + [d["name_" + k] for k in LATIN])
        g["cla"].add(d["featurecla"])
        g["km"] += shapely_length_km(geom)
    rows = []
    for name, g in groups.items():
        alts = ascii_only(clean_names(name, g["alts"] + _RIVER_ALIAS_NORM.get(norm(name), [])))
        runs, n = cells_to_runs(g["cells"], land)
        rows.append({"name": name, "alt_names": alts, "kind": sorted(g["cla"]), "length_km": round(g["km"]),
                     "n_cells": n, "cells": runs})
    rows.sort(key=lambda x: x["name"])
    write_jsonl(OUT / "rivers.jsonl", rows)
    print("rivers: %d names, %.0f s" % (len(rows), time.time() - t), file=sys.stderr)


def shapely_length_km(geom):
    import shapely
    total = 0.0
    for line in (geom.geoms if hasattr(geom, "geoms") else [geom]):
        c = shapely.get_coordinates(line)
        for (x0, y0), (x1, y1) in zip(c[:-1], c[1:]):
            total += haversine_km(y0, x0, y1, x1)
    return total


def haversine_km(lat1, lon1, lat2, lon2):
    p = math.pi / 180
    a = 0.5 - math.cos((lat2 - lat1) * p) / 2 + math.cos(lat1 * p) * math.cos(lat2 * p) * (1 - math.cos((lon2 - lon1) * p)) / 2
    return 12742 * math.asin(math.sqrt(a))


def build_lakes(land):
    t = time.time()
    r = reader("ne_10m_lakes")
    fields = [f[0] for f in r.fields[1:]]
    groups = collections.OrderedDict()
    for sr in r.iterShapeRecords():
        d = dict(zip(fields, sr.record))
        name = (d["name_en"] or "").strip() or (d["name"] or "").strip()
        if not name:
            continue
        geom = shape(sr.shape.__geo_interface__)
        g = groups.setdefault(name, {"cells": set(), "alts": []})
        g["cells"] |= grid.shape_cells(geom, RES)
        g["alts"].extend([d["name"], d["name_alt"], d["name_abb"], d["name_en"]] + [d["name_" + k] for k in LATIN])
    rows = []
    for name, g in groups.items():
        alts = ascii_only(clean_names(name, g["alts"]))
        runs, n = cells_to_runs(g["cells"], land)
        rows.append({"name": name, "alt_names": alts, "n_cells": n, "cells": runs})
    rows.sort(key=lambda x: x["name"])
    write_jsonl(OUT / "lakes.jsonl", rows)
    print("lakes: %d names, %.0f s" % (len(rows), time.time() - t), file=sys.stderr)


def place_cell(lat, lon, land):
    c = h3.latlng_to_cell(lat, lon, RES)
    if c in land:
        return land[c], False
    best = None
    for k in (1, 2):
        ring = [x for x in h3.grid_ring(c, k) if x in land]
        if ring:
            best = min(ring, key=lambda x: haversine_km(lat, lon, *h3.cell_to_latlng(x)))
            return land[best], True
    return None, True


def build_places(land):
    t = time.time()
    r = reader("ne_10m_populated_places")
    fields = [f[0] for f in r.fields[1:]]
    alias_index = {}
    for (n, c), alts in PLACE_ALIASES.items():
        alias_index.setdefault((norm(n), norm(c)), []).extend(alts)
    rows = []
    for rec in r.iterRecords():
        d = dict(zip(fields, rec))
        name = d["NAME"]
        country = d["ADM0NAME"]
        lat, lon = float(d["LATITUDE"]), float(d["LONGITUDE"])
        alts = clean_names(name, [d["NAMEALT"], d["NAMEPAR"], d["NAMEASCII"], d["NAME_EN"], d["MEGANAME"],
                                  d["LS_NAME"]] + [d["NAME_" + k.upper()] for k in LATIN]
                           + alias_index.get((norm(name), norm(country)), []))
        alts = ascii_only(alts)
        cell, moved = place_cell(lat, lon, land)
        row = {"name": name, "country": country, "admin1": d["ADM1NAME"], "lon": round(lon, 4), "lat": round(lat, 4),
               "pop": int(d["POP_MAX"]) if d["POP_MAX"] not in (None, "") else None,
               "capital": d["FEATURECLA"], "cell": cell, "alt_names": alts, "source": "ne"}
        if moved:
            row["cell_moved"] = True
        rows.append(row)
    for name, country, lat, lon, alts in EXTRA_PLACES:
        cell, moved = place_cell(lat, lon, land)
        row = {"name": name, "country": country, "admin1": "", "lon": lon, "lat": lat, "pop": None,
               "capital": "Historic site", "cell": cell, "alt_names": alts, "source": "knowledge"}
        if moved:
            row["cell_moved"] = True
        rows.append(row)
    rows.sort(key=lambda x: (x["name"], x["country"]))
    write_jsonl(OUT / "places.jsonl", rows)
    print("places: %d rows (%d from knowledge), %.0f s" % (len(rows), len(EXTRA_PLACES), time.time() - t),
          file=sys.stderr)


def main(argv):
    what = argv[1] if len(argv) > 1 else "all"
    land = grid.land_cells(RES)
    print("land grid: %d cells" % len(land), file=sys.stderr)
    if what in ("countries", "all"):
        build_countries(land)
    if what in ("admin1", "all"):
        build_admin1(land)
    if what in ("rivers", "all"):
        build_rivers(land)
    if what in ("lakes", "all"):
        build_lakes(land)
    if what in ("places", "all"):
        build_places(land)


if __name__ == "__main__":
    main(sys.argv)
