#!/usr/bin/env python3
"""Source of data/gazetteer/regions.jsonl v0: historical regions named in words, as region specs.

Run from a scratch directory:  python3 -I tools/regions_src.py   (then tools/gazetteer.py check)

This file wrote v0 on 18 Oct 2026 from the gazetteer agent's knowledge. Later additions go
straight into regions.jsonl (one JSON object per line, see data/gazetteer/README.md); rerunning
this script rewrites only the entries defined here and keeps any other entry already in the file.

Each entry: name, alt_names, spec (the shared region grammar: country, admin1, place with km,
polygon, union, minus, intersect, region), confidence 1-3 (3: the modern units match the
historical region well; 2: a fair approximation; 1: a rough one) and a note on what was approximated.
Country and admin-1 spellings are Natural Earth 10m's (see tools/build_gazetteer.py).
"""
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "data" / "gazetteer" / "regions.jsonl"


def C(name):
    return {"country": name}


def A(name, country):
    return {"admin1": name, "country": country}


def As(country, *names):
    return {"union": [A(n, country) for n in names]} if len(names) > 1 else A(names[0], country)


def P(name, km, country=None):
    d = {"place": name, "km": km}
    if country:
        d["country"] = country
    return d


def U(*specs):
    return {"union": list(specs)}


def M(a, *b):
    return {"minus": [a] + list(b)}


def I(*specs):
    return {"intersect": list(specs)}


def R(name):
    return {"region": name}


def PG(points):
    return {"polygon": points}


REGIONS = []


def reg(name, alt, spec, conf, note=""):
    REGIONS.append({"name": name, "alt_names": alt, "spec": spec, "confidence": conf, "note": note})


USA = "United States of America"

# ----------------------------------------------------------------------------
# Central Asia, Iran and Afghanistan
# ----------------------------------------------------------------------------
reg("Khorasan", ["Greater Khorasan", "Khurasan", "Khorassan"],
    U(As("Iran", "Razavi Khorasan", "North Khorasan", "South Khorasan"),
      As("Afghanistan", "Hirat", "Badghis", "Faryab", "Jawzjan", "Balkh", "Samangan", "Sari Pul", "Ghor"),
      As("Turkmenistan", "Mary", "Ahal")), 2,
    "Greater Khorasan: the four quarters of Nishapur, Merv, Herat and Balkh. Turkmenistan's Ahal (Nisa) and Lebap are border cases; Lebap is left out.")
reg("Iranian Khorasan", ["Khorasan (Iran)", "Khorasan province"],
    As("Iran", "Razavi Khorasan", "North Khorasan", "South Khorasan"), 3, "The three Iranian provinces of the former Khorasan province.")
reg("Transoxiana", ["Mawarannahr", "Ma wara al-Nahr", "Transoxania", "Mawara'un-nahr"],
    U(M(C("Uzbekistan"), A("Karakalpakstan", "Uzbekistan"), A("Khorezm", "Uzbekistan")),
      M(C("Tajikistan"), A("Gorno-Badakhshan", "Tajikistan")),
      As("Kyrgyzstan", "Osh", "Jalal-Abad", "Batken"),
      A("South Kazakhstan", "Kazakhstan")), 2,
    "Land between the Oxus and the Jaxartes: Uzbekistan without Khwarezm, lowland Tajikistan, the Kyrgyz Fergana and Kazakhstan's Turkistan region.")
reg("Sogdia", ["Sogdiana", "Sughd", "Soghd"],
    U(As("Uzbekistan", "Samarkand", "Bukhoro", "Kashkadarya", "Navoi", "Jizzakh"), A("Leninabad", "Tajikistan")), 2,
    "The Zarafshan and Kashka Darya valleys; Navoi reaches far north into the desert.")
reg("Bactria", ["Tokharistan", "Tukharistan", "Bactriana", "Balkh (region)"],
    U(As("Afghanistan", "Balkh", "Samangan", "Baghlan", "Kunduz", "Takhar", "Badakhshan"),
      A("Surkhandarya", "Uzbekistan"), As("Tajikistan", "Khatlon", "Dushanbe", "Tadzhikistan Territories")), 2,
    "Both banks of the upper Oxus between the Hindu Kush and the Hisar range.")
reg("Margiana", ["Merv oasis", "Marv (region)"], A("Mary", "Turkmenistan"), 2, "The Merv oasis; Mary province is wider than the oasis.")
reg("Khwarezm", ["Khwarazm", "Chorasmia", "Khorezm", "Khwarizm", "Khiva (khanate core)"],
    U(As("Uzbekistan", "Khorezm", "Karakalpakstan"), A("Tashauz", "Turkmenistan")), 2,
    "The lower Oxus delta; Karakalpakstan includes the dry Aral bed and the Ustyurt.")
reg("Fergana", ["Fergana Valley", "Ferghana", "Farghana", "Fergana basin"],
    U(As("Uzbekistan", "Ferghana", "Andijon", "Namangan"), As("Kyrgyzstan", "Osh", "Jalal-Abad", "Batken"),
      A("Leninabad", "Tajikistan")), 2, "Tajikistan's Sughd also holds the upper Zarafshan.")
reg("Ustrushana", ["Osrushana", "Sutrushana"], A("Jizzakh", "Uzbekistan"), 2, "")
reg("Chach", ["Shash", "Tashkent oasis"], As("Uzbekistan", "Tashkent", "Sirdaryo"), 2, "")
reg("Semirechye", ["Zhetysu", "Jetisu", "Seven Rivers", "Yetisu"],
    U(As("Kazakhstan", "Almaty", "Almaty City", "Zhambyl"), As("Kyrgyzstan", "Chuy", "Talas", "Ysyk-Köl")), 2, "")
reg("Kazakh Steppe", ["Kazakh steppe", "Dasht-i Kipchak (east)", "Great Steppe (Kazakh)"],
    M(C("Kazakhstan"), As("Kazakhstan", "South Kazakhstan", "Zhambyl", "Almaty", "Almaty City", "Qyzylorda", "Mangghystau")), 2, "")
reg("Pontic Steppe", ["Pontic-Caspian steppe", "Wild Fields (broad)", "South Russian steppe"],
    U(As("Ukraine", "Odessa", "Mykolayiv", "Kherson", "Zaporizhzhya", "Dnipropetrovs'k", "Donets'k", "Luhans'k", "Kirovohrad"),
      As("Russia", "Rostov", "Krasnodar", "Stavropol'", "Kalmyk", "Astrakhan'", "Volgograd", "Crimea")), 2,
    "Crimea is filed under Russia in Natural Earth's admin-1 table.")
reg("Dasht-i Kipchak", ["Kipchak steppe", "Desht-i Qipchaq", "Cumania"], U(R("Kazakh Steppe"), R("Pontic Steppe")), 1, "")
reg("Mangyshlak", ["Mangghystau", "Mangistau"], A("Mangghystau", "Kazakhstan"), 3, "")
reg("Sistan", ["Sakastan", "Drangiana", "Seistan", "Zarang (region)"],
    U(I(A("Sistan and Baluchestan", "Iran"), PG([[59.5, 29.5], [63.5, 29.5], [63.5, 32.0], [59.5, 32.0]])),
      A("Nimroz", "Afghanistan")), 2, "The Helmand delta basin.")
reg("Baluchistan", ["Balochistan", "Gedrosia (broad)"], U(A("Baluchistan", "Pakistan"), A("Sistan and Baluchestan", "Iran")), 2, "")
reg("Makran", ["Gedrosia", "Mekran"],
    I(R("Baluchistan"), PG([[57.0, 24.5], [67.5, 24.5], [67.5, 27.2], [57.0, 27.2]])), 1, "The coastal strip of Baluchistan.")
reg("Kabulistan", ["Kabul (region)", "Kabul valley"], As("Afghanistan", "Kabul", "Parwan", "Kapisa", "Logar", "Wardak", "Laghman"), 2, "")
reg("Zabulistan", ["Zabul (region)", "Ghazni (region)"], As("Afghanistan", "Ghazni", "Zabul"), 2, "")
reg("Ghur", ["Ghor", "Ghor (region)"], A("Ghor", "Afghanistan"), 3, "")
reg("Guzgan", ["Juzjan", "Jowzjan (region)", "Gozgan"], As("Afghanistan", "Jawzjan", "Faryab", "Sari Pul"), 2, "")
reg("Badakhshan", ["Badakshan"], U(A("Badakhshan", "Afghanistan"), A("Gorno-Badakhshan", "Tajikistan")), 3, "")
reg("Pamir", ["Pamirs", "Pamir Mountains"], A("Gorno-Badakhshan", "Tajikistan"), 2, "The Afghan Wakhan and Chinese Pamir are left out.")
reg("Arachosia", ["Harauvatish", "Kandahar (region)"], As("Afghanistan", "Kandahar", "Zabul", "Uruzgan", "Hilmand"), 2, "")
reg("Aria", ["Herat (region)", "Haraiva"], A("Hirat", "Afghanistan"), 2, "")
reg("Gandhara", ["Gandara", "Peshawar valley", "Purushapura (region)"],
    U(P("Peshawar", 110, "Pakistan"), P("Taxila", 60), P("Jalalabad", 70, "Afghanistan")), 2,
    "The Peshawar valley with Taxila and the lower Kabul valley.")
reg("Media", ["Mada", "Median heartland"],
    As("Iran", "Hamadan", "Markazi", "Qazvin", "Zanjan", "Tehran", "Alborz", "Qom", "Kermanshah", "Kordestan"), 2, "Media proper around Ecbatana; Atropatene is separate.")
reg("Atropatene", ["Media Atropatene", "Iranian Azerbaijan", "Azarbaijan (Iran)", "Adurbadagan"],
    As("Iran", "East Azarbaijan", "West Azarbaijan", "Ardebil", "Zanjan"), 2, "")
reg("Persis", ["Pars", "Fars (region)", "Parsa"], As("Iran", "Fars", "Bushehr"), 3, "")
reg("Parthia", ["Parthava", "Parthia proper"], U(As("Iran", "Semnan", "North Khorasan"), A("Ahal", "Turkmenistan")), 2, "Parthia proper south of the Kopet Dag, not the Arsacid empire.")
reg("Hyrcania", ["Varkana", "Gorgan (region)", "Jurjan"], As("Iran", "Golestan", "Mazandaran"), 2, "")
reg("Tabaristan", ["Mazandaran (historical)"], A("Mazandaran", "Iran"), 3, "")
reg("Daylam", ["Gilan (region)", "Deylam"], A("Gilan", "Iran"), 2, "")
reg("Khuzestan", ["Susiana", "Arabistan", "Khuzistan"], A("Khuzestan", "Iran"), 3, "")
reg("Elam", ["Elamite lands", "Haltamti"], As("Iran", "Khuzestan", "Ilam", "Lorestan", "Kohgiluyeh and Buyer Ahmad", "Fars"), 2, "Susiana plus the Anshan highlands.")
reg("Carmania", ["Kerman (region)", "Kirman"], A("Kerman", "Iran"), 3, "")
reg("Luristan", ["Lorestan (region)", "Lur country"], As("Iran", "Lorestan", "Ilam"), 2, "")
reg("Kurdistan", ["Kurdish lands", "Greater Kurdistan"],
    U(As("Iran", "Kordestan", "Kermanshah"), As("Iraq", "Arbil", "As-Sulaymaniyah", "Dihok"),
      As("Turkey", "Diyarbakir", "Mardin", "Van", "Hakkari", "Sirnak", "Siirt", "Bitlis", "Mus", "Agri", "Batman", "Bingöl", "Tunceli"),
      A("Hasaka (Al Haksa)", "Syria")), 2, "")

# ----------------------------------------------------------------------------
# Anatolia and the Caucasus
# ----------------------------------------------------------------------------
reg("Eastern Thrace", ["Turkish Thrace", "East Thrace", "European Turkey"], As("Turkey", "Edirne", "Kirklareli", "Tekirdag", "Istanbul"), 3,
    "Istanbul province straddles the Bosporus; it is counted here.")
reg("Anatolia", ["Asia Minor", "Anadolu", "Anatolian peninsula"], M(C("Turkey"), R("Eastern Thrace")), 3, "")
reg("Cilicia", ["Kilikya", "Cilician plain"], As("Turkey", "Adana", "Mersin", "Osmaniye"), 3, "")
reg("Cappadocia", ["Kapadokya", "Katpatuka"], As("Turkey", "Nevsehir", "Kayseri", "Aksaray", "Nigde", "Kirsehir", "Yozgat", "Sivas"), 2, "The Roman province; the tourist Cappadocia is Nevsehir alone.")
reg("Pontus", ["Pontos", "Pontic coast"], As("Turkey", "Samsun", "Ordu", "Giresun", "Trabzon", "Rize", "Gümüshane", "Bayburt", "Amasya", "Tokat", "Sinop"), 2, "")
reg("Bithynia", ["Bithynia and Nicomedia"], As("Turkey", "Kocaeli", "Sakarya", "Yalova", "Bursa", "Bilecik", "Düzce", "Bolu"), 2, "")
reg("Paphlagonia", [], As("Turkey", "Kastamonu", "Sinop", "Çankiri", "Bartın", "Karabük", "Zinguldak"), 2, "Natural Earth spells Zonguldak 'Zinguldak'.")
reg("Galatia", ["Galatian highlands"], As("Turkey", "Ankara", "Kinkkale", "Çorum", "Yozgat", "Eskisehir"), 2, "")
reg("Phrygia", ["Phrygian highlands"], As("Turkey", "Eskisehir", "Kütahya", "Afyonkarahisar", "Usak"), 2, "")
reg("Lydia", ["Lydian kingdom core", "Maeonia"], As("Turkey", "Manisa", "Izmir", "Usak"), 2, "")
reg("Ionia", ["Ionian coast"], As("Turkey", "Izmir", "Aydin"), 2, "")
reg("Caria", [], As("Turkey", "Mugla", "Aydin"), 2, "")
reg("Lycia", [], U(A("Mugla", "Turkey"), I(A("Antalya", "Turkey"), PG([[28.5, 35.9], [30.6, 35.9], [30.6, 37.2], [28.5, 37.2]]))), 2, "")
reg("Pamphylia", [], A("Antalya", "Turkey"), 2, "")
reg("Pisidia", [], As("Turkey", "Isparta", "Burdur"), 2, "")
reg("Lycaonia", [], As("Turkey", "Konya", "Karaman"), 2, "")
reg("Mysia", [], As("Turkey", "Balikesir", "Çanakkale"), 2, "")
reg("Troad", ["Troas", "Biga peninsula"], A("Çanakkale", "Turkey"), 2, "")
reg("Armenian Highlands", ["Greater Armenia", "Armenia (historical)", "Armenia Major", "Historic Armenia"],
    U(As("Turkey", "Erzurum", "Kars", "Agri", "Van", "Bitlis", "Mus", "Erzincan", "Iğdir", "Ardahan", "Bingöl", "Tunceli", "Elazig"),
      C("Armenia"), A("Naxçıvan Autonomous Republic", "Azerbaijan")), 2, "")
reg("Lesser Armenia", ["Armenia Minor"], As("Turkey", "Sivas", "Malatya", "Erzincan"), 1, "")
reg("Cilician Armenia", ["Armenian Kingdom of Cilicia", "Armenian Cilicia"], As("Turkey", "Adana", "Mersin", "Osmaniye", "K. Maras", "Hatay"), 2, "")
reg("Commagene", [], As("Turkey", "Adiyaman", "K. Maras", "Gaziantep"), 2, "")
reg("Osroene", ["Edessa (region)", "Osrhoene"], A("Sanliurfa", "Turkey"), 2, "")
reg("Sophene", [], As("Turkey", "Elazig", "Tunceli", "Bingöl"), 1, "")
reg("Jazira", ["Upper Mesopotamia", "Al-Jazira", "Jazirah"],
    U(As("Turkey", "Sanliurfa", "Mardin", "Diyarbakir", "Batman", "Sirnak"),
      As("Syria", "Hasaka (Al Haksa)", "Ar Raqqah", "Dayr Az Zawr"),
      As("Iraq", "Ninawa", "Dihok", "Sala ad-Din", "At-Ta'mim")), 2, "")
reg("Transcaucasia", ["South Caucasus", "Caucasus (south)"], U(C("Georgia"), C("Armenia"), C("Azerbaijan")), 3, "")
reg("North Caucasus", ["Ciscaucasia", "Caucasus (north)"],
    As("Russia", "Dagestan", "Chechnya", "Ingush", "North Ossetia", "Kabardin-Balkar", "Karachay-Cherkess", "Stavropol'", "Adygey", "Krasnodar"), 3, "")
reg("Caucasus", ["Caucasia"], U(R("North Caucasus"), R("Transcaucasia")), 3, "")
reg("Circassia", ["Cherkessia", "Adyghe lands"], As("Russia", "Krasnodar", "Adygey", "Karachay-Cherkess", "Kabardin-Balkar"), 2, "")
reg("Dagestan", ["Daghestan"], A("Dagestan", "Russia"), 3, "")
reg("Chechnya", ["Chechnya and Ingushetia"], As("Russia", "Chechnya", "Ingush"), 3, "")
reg("Kartli", ["Iberia (Caucasus) core", "Eastern Georgia (Kartli)"], As("Georgia", "Shida Kartli", "Kvemo Kartli", "Tbilisi", "Mtskheta-Mtianeti"), 3, "")
reg("Caucasian Iberia", ["Iberia (Caucasus)", "Kartli-Kakheti", "Eastern Georgia"], U(R("Kartli"), A("Kakheti", "Georgia")), 2, "")
reg("Kakheti", [], A("Kakheti", "Georgia"), 3, "")
reg("Colchis", ["Egrisi", "Lazica", "Western Georgia"],
    As("Georgia", "Imereti", "Samegrelo-Zemo Svaneti", "Guria", "Ajaria", "Abkhazia", "Racha-Lechkhumi-Kvemo Svaneti"), 2, "")
reg("Abkhazia", ["Abkhazeti", "Abasgia"], A("Abkhazia", "Georgia"), 3, "")
reg("Mingrelia", ["Samegrelo", "Megrelia"], A("Samegrelo-Zemo Svaneti", "Georgia"), 3, "Includes Upper Svaneti.")
reg("Imereti", ["Imeretia"], A("Imereti", "Georgia"), 3, "")
reg("Adjara", ["Ajaria", "Achara"], A("Ajaria", "Georgia"), 3, "")
reg("Samtskhe", ["Meskheti", "Samtskhe-Javakheti"], A("Samtskhe-Javakheti", "Georgia"), 3, "")
reg("Nakhchivan", ["Nakhichevan", "Naxcivan"], A("Naxçıvan Autonomous Republic", "Azerbaijan"), 3, "")
reg("Karabakh", ["Nagorno-Karabakh (with surrounding districts)", "Artsakh", "Qarabag"],
    As("Azerbaijan", "Yukhari Garabakh Economic Region", "Kalbajar-Lachin Economic Region"), 2, "Natural Earth's economic regions.")
reg("Shirvan", ["Sharvan"], As("Azerbaijan", "Daghlig Shirvan Economic Region", "Absheron Economic Region", "Aran Economic Region", "Guba-Khachmaz Economic Region"), 1, "")
reg("Arran", ["Aran (Caucasus)", "Albania (Caucasus) core"], As("Azerbaijan", "Aran Economic Region", "Ganja-Gazakh Economic Region"), 1, "")
reg("Caucasian Albania", ["Albania (Caucasus)", "Aghvank", "Arran and Shirvan"], U(C("Azerbaijan"), A("Dagestan", "Russia")), 1, "")

# ----------------------------------------------------------------------------
# Greece and the Balkans
# ----------------------------------------------------------------------------
reg("Thrace", ["Thracia", "Thraki", "Trakya"],
    U(R("Eastern Thrace"), As("Bulgaria", "Haskovo", "Kardzhali", "Smolyan", "Plovdiv", "Pazardzhik", "Stara Zagora", "Sliven", "Yambol", "Burgas"),
      A("Anatoliki Makedonia kai Thraki", "Greece")), 2, "Natural Earth bundles Greek Thrace with East Macedonia in one region.")
reg("Macedonia (region)", ["Macedonia", "Makedonia", "Macedonia (historical region)"],
    U(As("Greece", "Kentriki Makedonia", "Dytiki Makedonia", "Anatoliki Makedonia kai Thraki", "Ayion Oros"),
      C("North Macedonia"), A("Blagoevgrad", "Bulgaria")), 2, "The whole geographic region; the Greek east region also carries Thrace.")
reg("Ancient Macedon", ["Macedon", "Kingdom of Macedon (core)", "Lower Macedonia"], As("Greece", "Kentriki Makedonia", "Dytiki Makedonia"), 2, "")
reg("Epirus", ["Epeiros", "Ipeiros"], U(A("Ipeiros", "Greece"), As("Albania", "Gjirokastër", "Vlorë")), 2, "")
reg("Thessaly", ["Thessalia"], A("Thessalia", "Greece"), 3, "")
reg("Attica", ["Attiki", "Attika"], A("Attiki", "Greece"), 3, "")
reg("Peloponnese", ["Peloponnesus", "Morea", "Peloponnisos"],
    I(U(A("Peloponnisos", "Greece"), A("Dytiki Ellada", "Greece")),
      PG([[20.9, 36.2], [23.7, 36.2], [23.7, 37.95], [23.0, 38.1], [22.4, 38.25], [21.7, 38.45], [21.1, 38.4], [20.9, 37.5]])), 2,
    "Achaea and Elis come from the West Greece region, cut south of the Gulf of Corinth.")
reg("Crete", ["Kriti", "Candia"], A("Kriti", "Greece"), 3, "")
reg("Cyprus (island)", ["Cyprus", "Kypros", "Kibris"], U(C("Cyprus"), C("N. Cyprus"), C("Akrotiri"), C("Dhekelia"), C("Cyprus U.N. Buffer Zone")), 3, "")
reg("Central Greece", ["Sterea Ellada", "Roumeli", "Rumelia (Greek)"], A("Stereá Elláda", "Greece"), 3, "Includes Euboea.")
reg("Boeotia", ["Boiotia", "Viotia"], I(A("Stereá Elláda", "Greece"), PG([[22.6, 38.0], [24.0, 38.0], [24.0, 38.65], [22.6, 38.65]])), 1, "")
reg("Euboea", ["Evia", "Euboia", "Negroponte"], I(A("Stereá Elláda", "Greece"), PG([[23.3, 37.9], [24.7, 37.9], [24.7, 39.1], [22.9, 39.1], [22.9, 38.75], [23.3, 38.6]])), 1, "")
reg("Ionian Islands", ["Heptanese", "Ionioi Nisoi", "Eptanisa"], A("Ionioi Nisoi", "Greece"), 3, "")
reg("Aegean Islands", ["Aegean (islands)", "Cyclades and Dodecanese and North Aegean"], As("Greece", "Notio Aigaio", "Voreio Aigaio"), 3, "")
reg("Cyclades", ["Kyklades"], I(A("Notio Aigaio", "Greece"), PG([[24.2, 36.3], [26.3, 36.3], [26.3, 37.9], [24.2, 37.9]])), 2, "")
reg("Dodecanese", ["Dodekanisa", "Southern Sporades"], I(A("Notio Aigaio", "Greece"), PG([[26.3, 35.6], [28.4, 35.6], [28.4, 37.3], [26.3, 37.3]])), 2, "")
reg("Rhodes", ["Rodos"], PG([[27.6, 35.8], [28.3, 35.8], [28.3, 36.5], [27.6, 36.5]]), 3, "")
reg("Illyria", ["Illyricum", "Illyrian lands"], U(C("Albania"), C("Montenegro"), C("Bosnia and Herz."), R("Dalmatia")), 1, "")
reg("Dalmatia", ["Dalmatian coast", "Dalmacija"], As("Croatia", "Splitsko-Dalmatinska", "Zadarska", "Šibensko-Kninska", "Dubrovacko-Neretvanska"), 3, "")
reg("Istria", ["Istra"], U(A("Istarska", "Croatia"), I(C("Slovenia"), PG([[13.4, 45.3], [14.2, 45.3], [14.2, 45.7], [13.4, 45.7]]))), 2, "")
reg("Slavonia", ["Slavonija"], As("Croatia", "Osjecko-Baranjska", "Vukovarsko-Srijemska", "Brodsko-Posavska", "Viroviticko-Podravska"), 2, "")
reg("Bosnia (region)", ["Bosnia proper", "Bosna"], M(C("Bosnia and Herz."), R("Herzegovina")), 2, "")
reg("Herzegovina", ["Hercegovina", "Hum", "Zachlumia"], As("Bosnia and Herzegovina", "Herzegovina-Neretva", "West Herzegovina", "Trebinje"), 2, "")
reg("Vojvodina", ["Voivodina"], As("Serbia", "Severno-Backi", "Južno-Backi", "Zapadno-Backi", "Severno-Banatski", "Srednje-Banatski", "Južno-Banatski", "Sremski"), 3, "")
reg("Banat", ["Banat of Temeswar"],
    U(As("Serbia", "Severno-Banatski", "Srednje-Banatski", "Južno-Banatski"), As("Romania", "Timis", "Caras-Severin", "Arad")), 2, "Arad county reaches north of the Mures.")
reg("Rascia", ["Raska", "Sandzak (core)"], A("Raški", "Serbia"), 2, "")
reg("Moesia", ["Moesia Superior and Inferior", "Mysia (Balkan)"],
    U(As("Bulgaria", "Vidin", "Montana", "Vratsa", "Pleven", "Lovech", "Veliko Tarnovo", "Gabrovo", "Ruse", "Razgrad", "Targovishte", "Shumen", "Silistra", "Dobrich", "Varna"),
      As("Serbia", "Borski", "Zajecarski", "Nišavski", "Pomoravski", "Podunavski", "Branicevski", "Grad Beograd", "Šumadijski", "Pirotski", "Toplicki", "Jablanicki", "Pcinjski")), 2, "")
reg("Dobruja", ["Dobrogea", "Dobrudja", "Scythia Minor"], U(As("Romania", "Constanta", "Tulcea"), As("Bulgaria", "Dobrich", "Silistra")), 3, "")
reg("Oltenia", ["Lesser Wallachia", "Little Wallachia"], As("Romania", "Dolj", "Gorj", "Mehedinti", "Olt", "Vâlcea"), 3, "")
reg("Muntenia", ["Greater Wallachia", "Wallachia proper"],
    As("Romania", "Arges", "Braila", "Buzau", "Calarasi", "Dâmbovita", "Giurgiu", "Ialomita", "Ilfov", "Bucharest", "Prahova", "Teleorman"), 3, "")
reg("Wallachia", ["Tara Romaneasca", "Walachia", "Vlachia", "Ungro-Wallachia"], U(R("Oltenia"), R("Muntenia")), 3, "")
reg("Romanian Moldavia", ["Western Moldavia", "Moldova (Romanian region)", "Moldavia (Romania)"],
    As("Romania", "Bacau", "Botosani", "Galati", "Iasi", "Neamt", "Suceava", "Vaslui", "Vrancea"), 3, "")
reg("Moldavia", ["Principality of Moldavia", "Moldavia (historical)", "Bogdania", "Moldova (principality)"],
    U(R("Romanian Moldavia"), C("Moldova"), A("Chernivtsi", "Ukraine")), 2, "The principality at its widest, with Bessarabia and Bukovina; Budjak is left out.")
reg("Transnistria", ["Pridnestrovie", "Left bank of the Dniester (Moldova)"],
    As("Moldova", "Transnistria", "Stîngă Nistrului", "Camenca", "Grigoriopol", "Bender"), 2, "Natural Earth's Moldovan districts east of the Dniester.")
reg("Budjak", ["Budzhak", "Bugeac", "Southern Bessarabia"],
    I(A("Odessa", "Ukraine"), PG([[28.2, 45.2], [30.3, 45.2], [30.3, 46.6], [29.3, 46.9], [28.2, 46.9]])), 2, "")
reg("Bessarabia", ["Basarabia", "Bessarabia governorate"], U(M(C("Moldova"), R("Transnistria")), R("Budjak")), 2, "")
reg("Bukovina", ["Bucovina", "Bukowina"], U(A("Suceava", "Romania"), A("Chernivtsi", "Ukraine")), 3, "")
reg("Crimea", ["Crimean peninsula", "Taurica", "Tauris", "Krym", "Crimean Khanate (core)"], As("Russia", "Crimea", "Sevastopol"), 3,
    "Natural Earth's admin-1 table files Crimea under Russia (de facto); the gazetteer follows the file, not a political view.")
reg("Transylvania", ["Ardeal", "Erdely", "Siebenburgen", "Transylvania proper", "Transilvania"],
    As("Romania", "Alba", "Bistrita-Nasaud", "Brasov", "Cluj", "Covasna", "Harghita", "Hunedoara", "Mures", "Sibiu", "Salaj"), 3, "The historical principality; see Transylvania (broad) for the 1920 cession.")
reg("Crisana", ["Crişana", "Partium (core)", "Körösvidék"], As("Romania", "Bihor", "Arad"), 2, "")
reg("Maramures", ["Maramureș", "Maramaros"], As("Romania", "Maramures", "Satu Mare"), 2, "")
reg("Transylvania (broad)", ["Transylvania with Crisana, Maramures and Banat", "Transylvania (1920)", "Hungarian Transylvania"],
    U(R("Transylvania"), R("Crisana"), R("Maramures"), As("Romania", "Timis", "Caras-Severin")), 2, "")
reg("Dacia", ["Roman Dacia", "Dacia Traiana"], U(R("Transylvania"), R("Banat"), R("Oltenia"), R("Crisana"), R("Maramures")), 2, "")
reg("Galicia (eastern Europe)", ["Galicia (Austrian)", "Galicia and Lodomeria", "Galizien", "Halychyna (broad)", "Galicja"],
    U(As("Ukraine", "L'viv", "Ivano-Frankivs'k", "Ternopil'"), As("Poland", "Subcarpathian", "Lesser Poland")), 2, "The Austrian crownland; Lesser Poland reaches beyond its western edge.")
reg("Eastern Galicia", ["Halychyna", "Red Ruthenia", "Galicia (Ukraine)"], As("Ukraine", "L'viv", "Ivano-Frankivs'k", "Ternopil'"), 3, "")
reg("Volhynia", ["Volyn", "Wolhynien", "Lodomeria", "Wolyn"], As("Ukraine", "Volyn", "Rivne", "Zhytomyr"), 2, "")
reg("Podolia", ["Podillia", "Podole"], As("Ukraine", "Khmel'nyts'kyy", "Vinnytsya"), 2, "")
reg("Zaporizhia", ["Zaporozhia", "Wild Fields (core)", "Zaporozhian Sich lands"], As("Ukraine", "Zaporizhzhya", "Dnipropetrovs'k", "Kherson", "Kirovohrad"), 2, "")
reg("Sloboda Ukraine", ["Slobozhanshchyna", "Sloboda Ukraina"], As("Ukraine", "Kharkiv", "Sumy"), 2, "")
reg("Donbas", ["Donbass", "Donets basin"], As("Ukraine", "Donets'k", "Luhans'k"), 3, "")
reg("Novorossiya", ["New Russia", "Novorossiya governorate"],
    As("Ukraine", "Odessa", "Mykolayiv", "Kherson", "Zaporizhzhya", "Dnipropetrovs'k", "Donets'k", "Luhans'k", "Kirovohrad"), 2, "Without Crimea.")
reg("Kievan core", ["Kiev region (historical)", "Middle Dnieper", "Kyiv land", "Rus' heartland"],
    As("Ukraine", "Kiev", "Kiev City", "Chernihiv", "Zhytomyr", "Cherkasy", "Poltava"), 2, "")
reg("Transcarpathia", ["Carpathian Ruthenia", "Zakarpattia", "Subcarpathian Rus", "Ruthenia (Carpathian)"], A("Transcarpathia", "Ukraine"), 3, "")
reg("White Ruthenia", ["Belarus (historical)", "Byelorussia", "White Russia"], C("Belarus"), 3, "")
reg("Polesia", ["Polesie", "Polissia", "Pripet Marshes"], U(As("Belarus", "Brest", "Gomel"), As("Ukraine", "Volyn", "Rivne")), 1, "")
reg("Samogitia", ["Zemaitija", "Zmudz", "Lower Lithuania"], As("Lithuania", "Telšiai", "Šiauliai", "Klaipedos", "Taurages"), 2, "")
reg("Lithuania proper", ["Aukstaitija (broad)", "Lithuania (ethnic)"], C("Lithuania"), 2, "")

# ----------------------------------------------------------------------------
# Central and northern Europe
# ----------------------------------------------------------------------------
reg("Bohemia", ["Cechy", "Bohmen", "Böhmen", "Čechy"],
    M(C("Czechia"), As("Czech Republic", "Jihomoravský", "Olomoucký", "Zlínský", "Moravskoslezský")), 2, "Vysočina (split between Bohemia and Moravia) is counted in Bohemia.")
reg("Moravia", ["Morava", "Mahren", "Mähren"], As("Czechia", "Jihomoravský", "Olomoucký", "Zlínský"), 2, "The Moravian-Silesian region is filed under Silesia.")
reg("Silesia", ["Slask", "Schlesien", "Slezsko", "Śląsk"], U(As("Poland", "Lower Silesian", "Opole", "Silesian"), A("Moravskoslezský", "Czechia")), 2, "The eastern part of the Silesian voivodeship is historically Lesser Poland.")
reg("Lower Silesia", ["Niederschlesien", "Dolny Slask"], A("Lower Silesian", "Poland"), 3, "")
reg("Upper Silesia", ["Oberschlesien", "Gorny Slask"], U(As("Poland", "Opole", "Silesian"), A("Moravskoslezský", "Czechia")), 2, "")
reg("Pomerania", ["Pommern", "Pomorze"], U(As("Poland", "Pomeranian", "West Pomeranian"), A("Mecklenburg-Vorpommern", "Germany")), 2, "Mecklenburg-Vorpommern brings Mecklenburg with Hither Pomerania.")
reg("Pomerelia", ["Gdansk Pomerania", "Eastern Pomerania", "Pomorze Gdanskie"], A("Pomeranian", "Poland"), 2, "")
reg("Prussia (region)", ["Prussia (historical region)", "Prusy", "Ducal and Royal Prussia", "Old Prussia"],
    U(A("Kaliningrad", "Russia"), As("Poland", "Warmian-Masurian", "Pomeranian", "Kuyavian-Pomeranian")), 2, "Kuyavia proper is not Prussian.")
reg("East Prussia", ["Ostpreussen", "Ducal Prussia", "Ostpreußen"], U(A("Kaliningrad", "Russia"), A("Warmian-Masurian", "Poland")), 2, "Without the Klaipeda region.")
reg("West Prussia", ["Westpreussen", "Royal Prussia", "Westpreußen"], As("Poland", "Pomeranian", "Kuyavian-Pomeranian"), 2, "")
reg("Warmia", ["Ermland", "Warmia (bishopric)"], I(A("Warmian-Masurian", "Poland"), PG([[19.3, 53.6], [21.3, 53.6], [21.3, 54.5], [19.3, 54.5]])), 2, "")
reg("Masuria", ["Masuren", "Mazury"], I(A("Warmian-Masurian", "Poland"), PG([[20.4, 53.3], [22.9, 53.3], [22.9, 54.5], [21.3, 54.5], [21.3, 53.6]])), 2, "")
reg("Greater Poland", ["Wielkopolska", "Polonia Maior"], As("Poland", "Greater Poland", "Lubusz"), 2, "")
reg("Lesser Poland", ["Malopolska", "Polonia Minor", "Małopolska"], As("Poland", "Lesser Poland", "Świętokrzyskie", "Subcarpathian", "Lublin"), 2, "The historical province, wider than the voivodeship.")
reg("Masovia", ["Mazovia", "Mazowsze"], As("Poland", "Masovian", "Łódź"), 2, "")
reg("Kuyavia", ["Kujawy"], A("Kuyavian-Pomeranian", "Poland"), 2, "")
reg("Podlachia", ["Podlasie", "Podlaskie"], A("Podlachian", "Poland"), 3, "")
reg("Livonia", ["Livland", "Swedish Livonia", "Governorate of Livonia", "Vidzeme and southern Estonia"],
    U(As("Latvia", "Vidzeme", "Riga"), As("Estonia", "Tartu", "Valga", "Võru", "Põlva", "Viljandi", "Pärnu", "Jõgeva", "Saare")), 2, "")
reg("Old Livonia", ["Terra Mariana", "Medieval Livonia", "Livonian Confederation", "Livonia (medieval)"], U(C("Latvia"), C("Estonia")), 3, "")
reg("Courland", ["Kurland", "Kurzeme", "Duchy of Courland and Semigallia", "Courland and Semigallia"], As("Latvia", "Kurzeme", "Zemgale"), 3, "")
reg("Semigallia", ["Zemgale", "Semgallen"], A("Zemgale", "Latvia"), 3, "")
reg("Latgale", ["Latgalia", "Polish Livonia", "Inflanty"], A("Latgale", "Latvia"), 3, "")
reg("Osel", ["Saaremaa", "Ösel", "Oesel"], A("Saare", "Estonia"), 3, "")
reg("Ingria", ["Ingermanland", "Izhora", "Ingermanlandia"], As("Russia", "Leningrad", "City of St. Petersburg"), 2, "")
reg("Karelia", ["Karjala"], U(A("Karelia", "Russia"), As("Finland", "North Karelia", "South Karelia")), 2, "The Karelian Isthmus (Leningrad oblast) is left out.")
reg("Lapland", ["Sapmi", "Sápmi", "Lappland"], U(A("Lapland", "Finland"), A("Finnmark", "Norway"), A("Norrbotten", "Sweden"), A("Murmansk", "Russia")), 2, "")
reg("Scania", ["Skane", "Skaneland", "Skåne", "Skåneland"], As("Sweden", "Skåne", "Blekinge", "Halland"), 3, "")
reg("Gotland", [], A("Gotland", "Sweden"), 3, "")
reg("Jutland", ["Jylland", "Jutland peninsula"], As("Denmark", "Nordjylland", "Midtjylland", "Syddanmark"), 2, "Syddanmark includes Funen.")
reg("Schleswig", ["Slesvig", "Duchy of Schleswig", "Sonderjylland"], U(A("Schleswig-Holstein", "Germany"), A("Syddanmark", "Denmark")), 1, "")
reg("Holstein", [], I(A("Schleswig-Holstein", "Germany"), PG([[8.0, 53.3], [11.3, 53.3], [11.3, 54.4], [8.0, 54.4]])), 2, "")
reg("Mecklenburg", [], A("Mecklenburg-Vorpommern", "Germany"), 2, "")
reg("Brandenburg", ["Mark Brandenburg", "Margraviate of Brandenburg"], As("Germany", "Brandenburg", "Berlin"), 3, "")
reg("Saxony", ["Sachsen", "Electorate of Saxony", "Kingdom of Saxony"], A("Sachsen", "Germany"), 3, "")
reg("Old Saxony", ["Saxony (early medieval)", "Stem Duchy of Saxony", "Saxon lands"],
    As("Germany", "Niedersachsen", "Sachsen-Anhalt", "Nordrhein-Westfalen", "Bremen", "Hamburg", "Schleswig-Holstein"), 1, "")
reg("Thuringia", ["Thuringen", "Thüringen"], A("Thüringen", "Germany"), 3, "")
reg("Franconia", ["Franken"], U(P("Nuremberg", 90, "Germany"), P("Würzburg", 70, "Germany"), P("Bamberg", 60, "Germany")), 1, "")
reg("Swabia", ["Schwaben", "Alamannia", "Alemannia"], U(A("Baden-Württemberg", "Germany"), P("Augsburg", 80, "Germany")), 1, "")
reg("Bavaria", ["Bayern"], A("Bayern", "Germany"), 3, "")
reg("Archduchy of Austria", ["Austria (archduchy)", "Austria proper", "Upper and Lower Austria"], As("Austria", "Niederösterreich", "Oberösterreich", "Wien"), 3, "")
reg("Tyrol", ["Tirol", "County of Tyrol"], U(A("Tirol", "Austria"), As("Italy", "Bozen", "Trento")), 3, "")
reg("South Tyrol", ["Trentino-Alto Adige", "Sudtirol", "Südtirol"], As("Italy", "Bozen", "Trento"), 3, "")
reg("Carinthia", ["Karnten", "Kärnten"], A("Kärnten", "Austria"), 3, "")
reg("Styria", ["Steiermark"], A("Steiermark", "Austria"), 2, "Lower Styria (Slovenia) is left out.")
reg("Carniola", ["Krain", "Kranjska"], C("Slovenia"), 2, "")
reg("Salzburg (region)", ["Archbishopric of Salzburg", "Salzburg"], A("Salzburg", "Austria"), 3, "")
reg("Alsace", ["Elsass", "Elsaß"], As("France", "Bas-Rhin", "Haute-Rhin"), 3, "")
reg("Lorraine", ["Lothringen", "Duchy of Lorraine"], As("France", "Meurthe-et-Moselle", "Meuse", "Moselle", "Vosges"), 3, "")
reg("Rhineland", ["Rheinland"], As("Germany", "Rheinland-Pfalz", "Saarland", "Nordrhein-Westfalen"), 1, "")
reg("Palatinate", ["Pfalz", "Electoral Palatinate", "Rhenish Palatinate"], A("Rheinland-Pfalz", "Germany"), 2, "")
reg("Westphalia", ["Westfalen"], A("Nordrhein-Westfalen", "Germany"), 2, "")
reg("Hesse", ["Hessen"], A("Hessen", "Germany"), 3, "")
reg("Baden", [], I(A("Baden-Württemberg", "Germany"), PG([[7.4, 47.5], [9.3, 47.5], [9.0, 48.5], [8.6, 49.9], [7.5, 49.9]])), 1, "")
reg("Wurttemberg", ["Württemberg", "Wuerttemberg"], M(A("Baden-Württemberg", "Germany"), R("Baden")), 1, "")
reg("Savoy", ["Savoie", "Duchy of Savoy (core)"], As("France", "Savoie", "Haute-Savoie"), 3, "")
reg("European Netherlands", ["Netherlands (European)", "Netherlands proper"],
    M(C("Netherlands"), As("Netherlands", "Bonaire", "Saba", "St. Eustatius")), 3, "Natural Earth files the Caribbean municipalities under the Netherlands.")
reg("Low Countries", ["Netherlands (historical)", "Benelux", "Seventeen Provinces"], U(C("Belgium"), R("European Netherlands"), C("Luxembourg")), 3, "")
reg("Flanders", ["Vlaanderen", "Flandre", "Flemish region"], U(A("Flemish", "Belgium"), A("Nord", "France"), A("Zeeland", "Netherlands")), 2, "")
reg("County of Flanders", ["Flanders (county)"], U(As("Belgium", "West Flanders", "East Flanders"), A("Nord", "France"), A("Zeeland", "Netherlands")), 2, "")
reg("Wallonia", ["Walloon region", "Wallonie"], A("Walloon", "Belgium"), 3, "")
reg("Brabant", ["Duchy of Brabant"], U(As("Belgium", "Flemish Brabant", "Walloon Brabant", "Brussels", "Antwerp"), A("Noord-Brabant", "Netherlands")), 2, "")
reg("Hainaut", ["Hennegau", "County of Hainaut"], U(A("Hainaut", "Belgium"), A("Nord", "France")), 2, "")
reg("Holland", ["County of Holland"], As("Netherlands", "Noord-Holland", "Zuid-Holland"), 3, "")
reg("Frisia", ["Friesland", "Frisian coast"],
    U(As("Netherlands", "Friesland", "Groningen"),
      I(A("Niedersachsen", "Germany"), PG([[6.5, 53.0], [9.0, 53.0], [9.0, 53.9], [6.5, 53.9]])),
      I(A("Schleswig-Holstein", "Germany"), PG([[8.2, 54.2], [9.0, 54.2], [9.0, 55.0], [8.2, 55.0]]))), 2, "")
reg("Guelders", ["Gelre", "Duchy of Guelders", "Gelderland (historical)"], As("Netherlands", "Gelderland", "Limburg"), 2, "")
reg("Metropolitan France", ["France (metropolitan)", "Hexagone", "European France"],
    M(C("France"), As("France", "Guadeloupe", "Martinique", "Guyane française", "La Réunion", "Mayotte")), 3, "")
reg("Gaul", ["Gallia", "Transalpine Gaul", "Gallia Transalpina"],
    U(M(R("Metropolitan France"), A("Corse", "France")), C("Belgium"), C("Luxembourg"), C("Switzerland"), R("European Netherlands"),
      As("Germany", "Rheinland-Pfalz", "Saarland")), 2, "The three Gauls with Narbonensis; Germany west of the Rhine is approximated by two states.")
reg("Cisalpine Gaul", ["Gallia Cisalpina", "Northern Italy", "Po valley"],
    As("Italy", "Piemonte", "Lombardia", "Veneto", "Emilia-Romagna", "Liguria", "Friuli-Venezia Giulia", "Trentino-Alto Adige", "Valle d'Aosta"), 2, "")
reg("Aquitaine", ["Aquitania", "Duchy of Aquitaine", "Guyenne and Gascony"],
    U(A("Nouvelle-Aquitaine", "France"),
      As("France", "Gers", "Hautes-Pyrénées", "Haute-Garonne", "Tarn-et-Garonne", "Lot", "Tarn", "Puy-de-Dôme", "Cantal", "Allier", "Haute-Loire")), 2,
    "The duchy at its widest, with Gascony and Auvergne.")
reg("Guyenne", ["Guienne"], As("France", "Gironde", "Dordogne", "Lot-et-Garonne", "Lot", "Tarn-et-Garonne", "Aveyron"), 2, "")
reg("Gascony", ["Gascogne", "Vasconia"], As("France", "Landes", "Gers", "Pyrénées-Atlantiques", "Hautes-Pyrénées", "Lot-et-Garonne", "Haute-Garonne"), 2, "")
reg("Burgundy", ["Duchy of Burgundy", "Bourgogne"], As("France", "Côte-d'Or", "Saône-et-Loire", "Yonne", "Nièvre"), 3, "The duchy; see Franche-Comté for the county.")
reg("Franche-Comté", ["County of Burgundy", "Free County of Burgundy", "Franche-Comte"], As("France", "Doubs", "Jura", "Haute-Saône", "Territoire de Belfort"), 3, "")
reg("Lyonnais", ["Lyon (region)"], As("France", "Rhône", "Loire"), 3, "")
reg("Dauphine", ["Dauphiné", "Dauphiny"], As("France", "Isère", "Drôme", "Hautes-Alpes"), 3, "")
reg("Provence", ["Provincia", "County of Provence"], A("Provence-Alpes-Côte-d'Azur", "France"), 2, "Includes the County of Nice and the Comtat Venaissin.")
reg("Kingdom of Burgundy (Arles)", ["Kingdom of Arles", "Arelat", "Upper and Lower Burgundy", "Burgundy (kingdom)"],
    U(R("Provence"), R("Dauphine"), R("Savoy"), R("Franche-Comté"), R("Lyonnais"),
      I(C("Switzerland"), PG([[5.9, 45.8], [7.6, 45.8], [7.6, 47.4], [5.9, 47.4]]))), 1, "")
reg("Lotharingia", ["Lothair's kingdom", "Middle Francia (north)", "Lotharingia (kingdom)"],
    U(R("Lorraine"), R("Alsace"), C("Luxembourg"), C("Belgium"), R("European Netherlands"), As("Germany", "Nordrhein-Westfalen", "Rheinland-Pfalz", "Saarland")), 2, "")
reg("Middle Francia", ["Lotharii Regnum", "Lothair I's kingdom"], U(R("Lotharingia"), R("Kingdom of Burgundy (Arles)"), R("Cisalpine Gaul"), R("Central Italy")), 1, "")
reg("Normandy", ["Normandie", "Duchy of Normandy"], A("Normandie", "France"), 3, "")
reg("Brittany", ["Bretagne", "Armorica", "Duchy of Brittany"], U(A("Bretagne", "France"), A("Loire-Atlantique", "France")), 3, "")
reg("Languedoc", ["Occitania (core)", "Langue d'oc"], As("France", "Hérault", "Gard", "Aude", "Lozère", "Tarn", "Haute-Garonne", "Ariège", "Aveyron", "Haute-Loire", "Ardèche"), 2, "")
reg("Roussillon", ["Northern Catalonia", "Rosselló"], A("Pyrénées-Orientales", "France"), 3, "")
reg("Septimania", ["Gothia", "Gallia Narbonensis (west)"], As("France", "Hérault", "Gard", "Aude", "Lozère", "Pyrénées-Orientales"), 2, "")
reg("Ile-de-France", ["Île-de-France", "Paris region", "Francia (Capetian core)"], A("Île-de-France", "France"), 3, "")
reg("Champagne", ["County of Champagne"], As("France", "Marne", "Aube", "Haute-Marne", "Ardennes"), 3, "")
reg("Picardy", ["Picardie"], As("France", "Somme", "Aisne", "Oise"), 3, "")
reg("Artois", ["County of Artois"], A("Pas-de-Calais", "France"), 3, "")
reg("Poitou", ["County of Poitou"], As("France", "Vienne", "Deux-Sèvres", "Vendée"), 3, "")
reg("Anjou", ["County of Anjou"], A("Maine-et-Loire", "France"), 3, "")
reg("Maine (France)", ["County of Maine", "Maine (French province)"], As("France", "Sarthe", "Mayenne"), 3, "")
reg("Touraine", [], A("Indre-et-Loire", "France"), 3, "")
reg("Berry", ["Duchy of Berry"], As("France", "Cher", "Indre"), 3, "")
reg("Orleanais", ["Orléanais"], As("France", "Loiret", "Loir-et-Cher", "Eure-et-Loir"), 2, "")
reg("Limousin", [], As("France", "Haute-Vienne", "Corrèze", "Creuse"), 3, "")
reg("Auvergne", [], As("France", "Puy-de-Dôme", "Cantal", "Allier", "Haute-Loire"), 3, "")
reg("Bourbonnais", [], A("Allier", "France"), 3, "")
reg("Bearn", ["Béarn"], A("Pyrénées-Atlantiques", "France"), 2, "The department also holds the French Basque country.")
reg("County of Nice", ["Nice (county)", "Nizza"], A("Alpes-Maritimes", "France"), 3, "")
reg("Comtat Venaissin", ["Avignon (papal)", "Comtat"], A("Vaucluse", "France"), 3, "")
reg("Pale of Calais", ["Calais (English)"], P("Calais", 30, "France"), 2, "")
reg("Corsica", ["Corse"], A("Corse", "France"), 3, "")
reg("Piedmont", ["Piemonte"], A("Piemonte", "Italy"), 3, "")
reg("Lombardy", ["Lombardia"], A("Lombardia", "Italy"), 3, "")
reg("Venetia", ["Veneto", "Terraferma"], A("Veneto", "Italy"), 3, "")
reg("Friuli", ["Friuli-Venezia Giulia"], A("Friuli-Venezia Giulia", "Italy"), 3, "")
reg("Liguria", [], A("Liguria", "Italy"), 3, "")
reg("Emilia-Romagna", ["Emilia", "Romagna"], A("Emilia-Romagna", "Italy"), 3, "")
reg("Tuscany", ["Toscana", "Tuscia", "Etruria"], A("Toscana", "Italy"), 3, "")
reg("Umbria", [], A("Umbria", "Italy"), 3, "")
reg("Marche", ["Marches", "March of Ancona"], A("Marche", "Italy"), 3, "")
reg("Latium", ["Lazio"], A("Lazio", "Italy"), 3, "")
reg("Abruzzo", ["Abruzzi"], As("Italy", "Abruzzo", "Molise"), 3, "")
reg("Campania", [], A("Campania", "Italy"), 3, "")
reg("Apulia", ["Puglia"], A("Apulia", "Italy"), 3, "")
reg("Calabria", ["Bruttium"], A("Calabria", "Italy"), 3, "")
reg("Basilicata", ["Lucania"], A("Basilicata", "Italy"), 3, "")
reg("Sicily", ["Sicilia"], A("Sicily", "Italy"), 3, "")
reg("Sardinia", ["Sardegna"], A("Sardegna", "Italy"), 3, "")
reg("Central Italy", ["Italia centrale"], As("Italy", "Toscana", "Umbria", "Marche", "Lazio"), 3, "")
reg("Papal States", ["States of the Church", "Stato Pontificio"], As("Italy", "Lazio", "Umbria", "Marche", "Emilia-Romagna"), 2, "The states at their widest, with the Legations.")
reg("Kingdom of Naples (region)", ["Mezzogiorno (mainland)", "Southern Italy", "Naples (kingdom)", "Regno"],
    As("Italy", "Campania", "Apulia", "Calabria", "Basilicata", "Abruzzo", "Molise"), 3, "")
reg("Two Sicilies", ["Mezzogiorno", "Kingdom of the Two Sicilies (region)"], U(R("Kingdom of Naples (region)"), R("Sicily")), 3, "")

# ----------------------------------------------------------------------------
# Iberia and the British Isles
# ----------------------------------------------------------------------------
reg("Hispania", ["Iberia", "Iberian Peninsula", "Spain and Portugal"],
    U(M(C("Spain"), As("Spain", "Las Palmas", "Santa Cruz de Tenerife", "Ceuta", "Melilla")),
      M(C("Portugal"), As("Portugal", "Azores", "Madeira")), C("Gibraltar"), C("Andorra")), 3, "")
reg("Lusitania", ["Hispania Lusitania"],
    U(M(C("Portugal"), As("Portugal", "Azores", "Madeira", "Braga", "Viana do Castelo", "Vila Real", "Bragança", "Porto")),
      As("Spain", "Badajoz", "Cáceres", "Salamanca")), 2, "")
reg("Andalusia", ["Andalucia", "Andalucía"], A("Andalucía", "Spain"), 3, "")
reg("Baetica", ["Hispania Baetica"], As("Spain", "Andalucía", "Badajoz"), 2, "")
reg("Catalonia", ["Catalunya", "Cataluña", "Principality of Catalonia"], A("Cataluña", "Spain"), 3, "")
reg("Castile", ["Castilla"], As("Spain", "Castilla y León", "Castilla-La Mancha", "Madrid", "Cantabria", "La Rioja"), 2, "")
reg("Old Castile", ["Castilla la Vieja"], As("Spain", "Castilla y León", "Cantabria", "La Rioja"), 2, "")
reg("New Castile", ["Castilla la Nueva"], As("Spain", "Castilla-La Mancha", "Madrid"), 2, "")
reg("Leon (region)", ["Kingdom of Leon (core)", "León", "Leon"], As("Spain", "León", "Zamora", "Salamanca"), 2, "")
reg("Asturias", ["Asturies"], A("Asturias", "Spain"), 3, "")
reg("Galicia (Spain)", ["Galicia (Iberia)", "Gallaecia", "Galiza"], As("Spain", "La Coruña", "Lugo", "Orense", "Pontevedra"), 3, "")
reg("Basque Country", ["Euskal Herria", "Vasconia (Basque)", "Pais Vasco (broad)"], U(A("País Vasco", "Spain"), A("Navarra", "Spain"), A("Pyrénées-Atlantiques", "France")), 2, "")
reg("Navarre", ["Navarra", "Kingdom of Navarre (core)"], A("Navarra", "Spain"), 3, "")
reg("Aragon", ["Aragón"], A("Aragón", "Spain"), 3, "")
reg("Valencia (region)", ["Kingdom of Valencia", "Pais Valencia", "Valenciana"], A("Valenciana", "Spain"), 3, "")
reg("Murcia", ["Kingdom of Murcia"], A("Murcia", "Spain"), 3, "")
reg("Balearic Islands", ["Baleares", "Islas Baleares", "Majorca and Minorca"], A("Islas Baleares", "Spain"), 3, "")
reg("Extremadura", [], A("Extremadura", "Spain"), 3, "")
reg("Canary Islands", ["Canarias", "Canaries"], As("Spain", "Las Palmas", "Santa Cruz de Tenerife"), 3, "")
reg("Algarve", ["Gharb al-Andalus"], A("Faro", "Portugal"), 3, "")
reg("Alentejo", [], A("Alentejo", "Portugal"), 3, "")
reg("Celtiberia", [], As("Spain", "Soria", "Guadalajara", "Teruel", "Cuenca", "Zaragoza"), 1, "")
reg("Tarraconensis", ["Hispania Tarraconensis", "Hispania Citerior"], M(R("Hispania"), R("Baetica"), R("Lusitania")), 1, "")
reg("England", ["Anglia"], As("United Kingdom", "East", "East Midlands", "Greater London", "North East", "North West", "South East", "South West", "West Midlands", "Yorkshire and the Humber"), 3, "")
reg("Wales", ["Cymru", "Cambria"], As("United Kingdom", "East Wales", "West Wales and the Valleys"), 3, "")
reg("Scotland", ["Alba", "Caledonia"], As("United Kingdom", "Eastern", "Highlands and Islands", "North Eastern", "South Western"), 3, "Natural Earth's four Scottish NUTS regions.")
reg("Northern Ireland", ["Ulster (six counties)"], A("Northern Ireland", "United Kingdom"), 3, "")
reg("Ireland (island)", ["Ireland", "Hibernia", "Eire (island)", "Erin"], U(C("Ireland"), A("Northern Ireland", "United Kingdom")), 3, "")
reg("Great Britain", ["Britain", "Britain (island)", "Britannia"], U(R("England"), R("Wales"), R("Scotland")), 3, "")
reg("Roman Britain", ["Britannia (province)"], U(R("England"), R("Wales")), 2, "")
reg("Ulster", ["Ulaidh"], U(A("Northern Ireland", "United Kingdom"), As("Ireland", "Donegal", "Cavan", "Monaghan")), 3, "")
reg("Munster", ["Mumhan"], As("Ireland", "Cork", "Kerry", "Limerick", "Clare", "Waterford", "North Tipperary", "South Tipperary"), 3, "")
reg("Leinster", ["Laighin"], As("Ireland", "Dublin", "Dún Laoghaire–Rathdown", "Fingal", "South Dublin", "Kildare", "Meath", "Wicklow", "Wexford", "Carlow", "Kilkenny", "Laoighis", "Offaly", "Westmeath", "Longford", "Louth"), 3, "")
reg("Connacht", ["Connaught"], As("Ireland", "Galway", "Mayo", "Sligo", "Leitrim", "Roscommon"), 3, "")
reg("The Pale", ["Pale (Ireland)", "English Pale"], P("Dublin", 50, "Ireland"), 2, "")
reg("Cornwall", ["Kernow", "Dumnonia (west)"], A("Cornwall", "United Kingdom"), 3, "")
reg("Kent", ["Kingdom of Kent", "Cantia"], As("United Kingdom", "Kent", "Medway"), 3, "")
reg("Sussex", ["Kingdom of Sussex"], As("United Kingdom", "East Sussex", "West Sussex", "Brighton and Hove"), 3, "")
reg("Essex (kingdom)", ["Kingdom of Essex", "East Saxons"], As("United Kingdom", "Essex", "Southend-on-Sea", "Thurrock", "Hertfordshire"), 2, "")
reg("Wessex", ["West Saxons", "Kingdom of Wessex"],
    U(A("South West", "United Kingdom"), As("United Kingdom", "Hampshire", "Isle of Wight", "Southampton", "Portsmouth", "West Berkshire", "Reading", "Wokingham", "Oxfordshire")), 2, "Wessex at its height, including Cornwall and Devon.")
reg("Mercia", ["Kingdom of Mercia"],
    U(A("West Midlands", "United Kingdom"), A("East Midlands", "United Kingdom"),
      As("United Kingdom", "Cheshire East", "Cheshire West and Chester", "Gloucestershire", "Oxfordshire", "Buckinghamshire", "Bedford", "Central Bedfordshire", "Hertfordshire")), 2, "")
reg("Northumbria", ["Kingdom of Northumbria", "Bernicia and Deira"],
    U(A("North East", "United Kingdom"), A("Yorkshire and the Humber", "United Kingdom"),
      As("United Kingdom", "Cumbria", "Lancashire", "Scottish Borders", "East Lothian", "Midlothian", "Edinburgh", "West Lothian")), 2, "")
reg("East Anglia", ["Kingdom of East Anglia"], As("United Kingdom", "Norfolk", "Suffolk", "Cambridgeshire", "Peterborough"), 3, "")
reg("Scottish Highlands", ["Highlands", "Highlands and Islands"], A("Highlands and Islands", "United Kingdom"), 3, "")
reg("Northern Isles", ["Orkney and Shetland"], As("United Kingdom", "Orkney", "Shetland Islands"), 3, "")
reg("Hebrides", ["Western Isles", "Outer Hebrides", "Eilean Siar"], A("Eilean Siar", "United Kingdom"), 2, "The Inner Hebrides sit inside Highland and Argyll and Bute.")
reg("Strathclyde", ["Kingdom of Strathclyde", "Alt Clut", "Cumbria (kingdom)"],
    As("United Kingdom", "Glasgow", "North Lanarkshire", "South Lanarkshire", "Renfrewshire", "East Renfrewshire", "Inverclyde", "West Dunbartonshire", "East Dunbartonshire", "North Ayshire", "East Ayrshire", "South Ayrshire", "Dumfries and Galloway", "Argyll and Bute"), 2, "")
reg("Lothian", [], As("United Kingdom", "East Lothian", "Midlothian", "West Lothian", "Edinburgh"), 3, "")
reg("Isle of Man", ["Mann", "Ellan Vannin"], C("Isle of Man"), 3, "")
reg("Channel Islands", ["Jersey and Guernsey"], U(C("Jersey"), C("Guernsey")), 3, "")

# ----------------------------------------------------------------------------
# Russia, Siberia and Mongolia
# ----------------------------------------------------------------------------
reg("Siberia", ["Sibir"], U(As("Russia", "Siberian", "Far Eastern"), As("Russia", "Tyumen'", "Khanty-Mansiy", "Yamal-Nenets", "Kurgan")), 2, "Natural Earth's Siberian and Far Eastern districts plus the Siberian part of the Urals district.")
reg("Western Siberia", ["West Siberia", "West Siberian Plain"], As("Russia", "Tyumen'", "Khanty-Mansiy", "Yamal-Nenets", "Kurgan", "Omsk", "Novosibirsk", "Tomsk", "Kemerovo", "Altay", "Gorno-Altay"), 2, "")
reg("Eastern Siberia", ["East Siberia"], As("Russia", "Krasnoyarsk", "Irkutsk", "Buryat", "Chita", "Tuva", "Khakass", "Sakha (Yakutia)"), 2, "")
reg("Russian Far East", ["Far East (Russia)", "Far Eastern Federal District"], A("Far Eastern", "Russia"), 3, "")
reg("Transbaikal", ["Zabaykalye", "Dauria", "Transbaikalia"], As("Russia", "Buryat", "Chita"), 3, "")
reg("Primorye", ["Primorsky Krai", "Maritime Province", "Ussuri region"], A("Primor'ye", "Russia"), 3, "")
reg("Outer Manchuria", ["Russian Manchuria", "Amur and Primorye", "Priamurye"], As("Russia", "Primor'ye", "Amur", "Yevrey", "Khabarovsk"), 2, "Khabarovsk krai reaches far north of the Amur.")
reg("Kamchatka", [], A("Kamchatka", "Russia"), 3, "")
reg("Chukotka", ["Chukchi peninsula"], A("Chukchi Autonomous Okrug", "Russia"), 3, "")
reg("Sakhalin", ["Karafuto", "Sakhalin island"], I(A("Sakhalin", "Russia"), PG([[141.0, 45.8], [145.0, 45.8], [145.0, 54.6], [141.0, 54.6]])), 3, "")
reg("Kuril Islands", ["Kurils", "Chishima"], I(A("Sakhalin", "Russia"), PG([[145.2, 43.0], [157.0, 43.0], [157.0, 51.5], [145.2, 51.5]])), 2, "")
reg("Yakutia", ["Sakha", "Yakut lands"], A("Sakha (Yakutia)", "Russia"), 3, "")
reg("Urals", ["Ural region", "Ural mountains region"], As("Russia", "Sverdlovsk", "Chelyabinsk", "Perm'", "Bashkortostan", "Orenburg", "Udmurt"), 2, "")
reg("Volga region", ["Povolzhye", "Middle and Lower Volga"], As("Russia", "Tatarstan", "Samara", "Saratov", "Ul'yanovsk", "Penza", "Volgograd", "Astrakhan'", "Nizhegorod", "Chuvash", "Mariy-El", "Mordovia"), 2, "")
reg("Muscovy (core)", ["Grand Duchy of Moscow (core)", "Moscow region (historical)", "Muscovy"], P("Moscow", 300, "Russia"), 2, "")
reg("Novgorod Land", ["Novgorod Republic (core)", "Novgorod lands", "Russian North (west)"], As("Russia", "Novgorod", "Leningrad", "Pskov", "Vologda", "Arkhangel'sk", "Karelia", "City of St. Petersburg"), 2, "")
reg("Vladimir-Suzdal", ["Zalesye", "Rostov-Suzdal", "Suzdalia", "North-eastern Rus"], As("Russia", "Vladimir", "Ivanovo", "Yaroslavl'", "Kostroma", "Moskovskaya", "Moskva", "Tver'", "Nizhegorod"), 2, "")
reg("Ryazan", ["Ryazan land"], A("Ryazan'", "Russia"), 3, "")
reg("Tver", ["Tver land"], A("Tver'", "Russia"), 3, "")
reg("Pskov", ["Pskov land"], A("Pskov", "Russia"), 3, "")
reg("Smolensk", ["Smolensk land"], A("Smolensk", "Russia"), 3, "")
reg("Chernigov", ["Chernihiv land", "Severia"], U(A("Chernihiv", "Ukraine"), As("Russia", "Bryansk", "Kursk")), 2, "")
reg("Kazan (region)", ["Kazan Khanate (core)", "Middle Volga", "Volga Bulgaria"], As("Russia", "Tatarstan", "Chuvash", "Mariy-El", "Udmurt", "Ul'yanovsk"), 2, "")
reg("Astrakhan (region)", ["Astrakhan Khanate (core)", "Lower Volga"], A("Astrakhan'", "Russia"), 3, "")
reg("Kalmykia", ["Kalmyk steppe"], A("Kalmyk", "Russia"), 3, "")
reg("Bashkiria", ["Bashkortostan"], A("Bashkortostan", "Russia"), 3, "")
reg("Pomorye", ["Russian North", "White Sea coast", "Pomorie"], As("Russia", "Arkhangel'sk", "Murmansk", "Nenets"), 2, "")
reg("Altai", ["Altay", "Altai Mountains"], U(As("Russia", "Altay", "Gorno-Altay"), A("East Kazakhstan", "Kazakhstan"), As("Mongolia", "Bayan-Ölgiy", "Hovd")), 2, "")
reg("Tuva", ["Tannu Tuva", "Uriankhai"], A("Tuva", "Russia"), 3, "")
reg("Khakassia", ["Yenisei Kyrgyz lands", "Minusinsk basin"], A("Khakass", "Russia"), 3, "")
reg("Mongolian Plateau", ["Greater Mongolia", "Mongolia (geographic)"], U(C("Mongolia"), A("Inner Mongol", "China")), 2, "")
reg("Inner Mongolia", ["Nei Mongol", "Inner Mongol"], A("Inner Mongol", "China"), 3, "")
reg("Outer Mongolia", ["Khalkha", "Mongolia (country)"], C("Mongolia"), 3, "")
reg("Western Mongolia", ["Oirat lands", "Dzungar homeland (east)", "Khovd region"], As("Mongolia", "Uvs", "Hovd", "Bayan-Ölgiy", "Dzavhan", "Govi-Altay"), 2, "")
reg("Eastern Mongolia", ["Khalkha (east)", "Dornod steppe"], As("Mongolia", "Dornod", "Sühbaatar", "Hentiy"), 2, "")
reg("Gobi", ["Gobi desert"], U(As("Mongolia", "Ömnögovi", "Dornogovi", "Dundgovi", "Govi-Altay"), I(A("Inner Mongol", "China"), PG([[97.0, 37.5], [112.0, 37.5], [112.0, 43.5], [97.0, 43.5]]))), 2, "")
reg("Orkhon Valley", ["Otuken", "Ötüken", "Karakorum (region)"], P("Karakorum", 150, "Mongolia"), 2, "")
reg("Hulunbuir", ["Hulun Buir", "Barga"], I(A("Inner Mongol", "China"), PG([[115.5, 47.0], [126.5, 47.0], [126.5, 53.5], [115.5, 53.5]])), 2, "")

# ----------------------------------------------------------------------------
# China, Korea and Japan
# ----------------------------------------------------------------------------
reg("Hexi Corridor", ["Hexi", "Gansu Corridor", "Hexi corridor"],
    I(A("Gansu", "China"), PG([[92.5, 38.3], [96.0, 37.8], [100.0, 36.8], [102.7, 36.0], [104.2, 36.3], [104.0, 37.6], [101.5, 39.5], [99.0, 41.0], [96.5, 42.0], [93.5, 42.2], [92.0, 40.5]])), 2,
    "Gansu north-west of the Yellow River, from Lanzhou to Dunhuang.")
reg("Tarim Basin", ["Southern Xinjiang", "Nanjiang", "Altishahr", "Kashgaria", "Eastern Turkestan (south)"],
    I(A("Xinjiang", "China"), PG([[73.5, 39.0], [75.5, 36.5], [80.0, 35.0], [92.0, 37.0], [96.5, 39.0], [96.0, 42.4], [92.0, 43.2], [88.0, 42.6], [84.0, 42.4], [80.0, 42.2], [76.0, 40.8]])), 2, "")
reg("Dzungaria", ["Junggar", "Zungharia", "Northern Xinjiang", "Beijiang"], M(A("Xinjiang", "China"), R("Tarim Basin")), 2, "Includes the Turfan and Hami depressions east of the Tianshan.")
reg("Turfan-Hami", ["Uyghuristan", "Eastern Xinjiang", "Turpan and Hami", "Kingdom of Qocho (region)"], I(A("Xinjiang", "China"), PG([[87.5, 41.5], [96.5, 41.5], [96.5, 44.0], [87.5, 44.0]])), 2, "")
reg("Xinjiang", ["Eastern Turkestan", "East Turkestan", "Chinese Turkestan", "Western Regions", "Xiyu"], A("Xinjiang", "China"), 3, "")
reg("Manchuria", ["Northeast China", "Dongbei", "Three Northeastern Provinces"], As("China", "Liaoning", "Jilin", "Heilongjiang"), 3, "")
reg("Greater Manchuria", ["Manchuria (greater)", "Manchuria with Outer Manchuria and eastern Inner Mongolia"],
    U(R("Manchuria"), R("Outer Manchuria"), I(A("Inner Mongol", "China"), PG([[115.5, 41.5], [126.5, 41.5], [126.5, 53.5], [115.5, 53.5]]))), 2, "")
reg("Ordos", ["Ordos Loop", "Ordos Plateau", "Hetao (south)"], I(C("China"), PG([[106.3, 37.2], [111.5, 37.2], [111.5, 40.9], [106.3, 40.9]])), 2, "The land inside the Yellow River loop.")
reg("Hetao", ["Yellow River bend", "Hetao plain"], I(C("China"), PG([[105.5, 40.0], [112.0, 40.0], [112.0, 41.3], [105.5, 41.3]])), 2, "")
reg("Liaodong", ["Liaodong peninsula", "Eastern Liaoning"], I(A("Liaoning", "China"), PG([[121.3, 38.6], [124.9, 39.4], [125.6, 41.4], [123.8, 42.6], [122.2, 42.4], [121.5, 40.6]])), 2, "Liaoning east of the Liao river.")
reg("Liaoxi", ["Western Liaoning"], M(A("Liaoning", "China"), R("Liaodong")), 2, "")
reg("Lingnan", ["Liangguang", "Two Guangs", "Nanyue (core)", "Far South (China)"], U(As("China", "Guangdong", "Guangxi", "Hainan"), C("Hong Kong"), C("Macao")), 3, "")
reg("Jiangnan", ["Lower Yangtze (south bank)", "Wu (region)", "Yangtze delta (south)"],
    I(As("China", "Jiangsu", "Anhui", "Zhejiang", "Shanghai"), PG([[115.8, 27.0], [123.0, 27.0], [123.0, 31.3], [121.0, 31.6], [119.5, 32.05], [118.6, 32.0], [117.5, 31.0], [116.0, 30.2], [115.8, 29.5]])), 2, "")
reg("Guanzhong", ["Wei River valley", "Qin heartland", "Shaanxi plain", "Guanzhong plain"], I(A("Shaanxi", "China"), PG([[106.3, 33.9], [110.6, 33.9], [110.6, 35.3], [106.3, 35.3]])), 2, "")
reg("Sichuan (region)", ["Sichuan", "Shu", "Ba-Shu", "Sichuan basin"], As("China", "Sichuan", "Chongqing"), 3, "")
reg("Yunnan (region)", ["Yunnan", "Dian", "Nanzhao heartland"], A("Yunnan", "China"), 3, "")
reg("Guizhou (region)", ["Guizhou", "Qian"], A("Guizhou", "China"), 3, "")
reg("Zhongyuan", ["Central Plain", "North China Plain", "Central Plains"], As("China", "Henan", "Shandong", "Hebei", "Shanxi", "Beijing", "Tianjin"), 2, "")
reg("Hebei (region)", ["Hebei", "Zhili", "Yan (core)"], As("China", "Hebei", "Beijing", "Tianjin"), 3, "")
reg("Shandong (region)", ["Shandong", "Qi and Lu", "Qi (state core)"], A("Shandong", "China"), 3, "")
reg("Shanxi (region)", ["Shanxi", "Jin (region)"], A("Shanxi", "China"), 3, "")
reg("Shaanxi (region)", ["Shaanxi", "Qin (region)"], A("Shaanxi", "China"), 3, "")
reg("Henan (region)", ["Henan", "Zhongzhou"], A("Henan", "China"), 3, "")
reg("Huguang", ["Hubei and Hunan", "Chu (core)"], As("China", "Hubei", "Hunan"), 3, "")
reg("Jiangxi (region)", ["Jiangxi", "Gan (region)"], A("Jiangxi", "China"), 3, "")
reg("Fujian (region)", ["Fujian", "Min (region)", "Minyue"], A("Fujian", "China"), 3, "")
reg("Zhejiang (region)", ["Zhejiang", "Yue (core)", "Wuyue (core)"], A("Zhejiang", "China"), 3, "")
reg("Gansu (region)", ["Gansu", "Longyou", "Longxi"], A("Gansu", "China"), 3, "")
reg("Qinghai (region)", ["Qinghai", "Kokonor", "Amdo (core)"], A("Qinghai", "China"), 3, "")
reg("Ningxia (region)", ["Ningxia", "Western Xia heartland"], A("Ningxia", "China"), 3, "")
reg("Tibet", ["Tibetan Plateau", "Bod", "Greater Tibet"], As("China", "Xizang", "Qinghai"), 2, "Kham's Sichuan and Yunnan parts are left out.")
reg("Central Tibet", ["U-Tsang", "Ü-Tsang", "Tibet Autonomous Region", "Xizang"], A("Xizang", "China"), 2, "")
reg("Amdo", [], U(A("Qinghai", "China"), I(A("Gansu", "China"), PG([[100.5, 33.5], [104.0, 33.5], [104.0, 36.0], [100.5, 36.0]]))), 2, "")
reg("Kham", ["Eastern Tibet"], I(As("China", "Xizang", "Sichuan", "Yunnan", "Qinghai"), PG([[94.0, 27.5], [103.0, 27.5], [103.0, 34.0], [94.0, 34.0]])), 1, "")
reg("Taiwan (island)", ["Taiwan", "Formosa"], C("Taiwan"), 3, "")
reg("Hainan (region)", ["Hainan", "Qiongzhou"], A("Hainan", "China"), 3, "")
reg("Korea", ["Korean Peninsula", "Joseon (whole)", "Choson", "Hanguk"], U(C("South Korea"), C("North Korea")), 3, "")
reg("Silla (core)", ["Gyeongsang", "Silla heartland"], As("South Korea", "North Gyeongsang", "South Gyeongsang", "Busan", "Daegu", "Ulsan"), 2, "")
reg("Baekje (core)", ["Chungcheong and Jeolla", "Baekje heartland"], As("South Korea", "North Chungcheong", "South Chungcheong", "Daejeon", "Sejong", "North Jeolla", "South Jeolla", "Gwangju"), 2, "")
reg("Gaya", ["Gaya confederacy", "Kaya"], I(A("South Gyeongsang", "South Korea"), PG([[127.6, 34.5], [129.3, 34.5], [129.3, 35.9], [127.6, 35.9]])), 1, "")
reg("Gyeonggi", ["Seoul region", "Hanseong (region)"], As("South Korea", "Gyeonggi", "Seoul", "Incheon"), 3, "")
reg("Gangwon", ["Kangwon"], U(A("Gangwon", "South Korea"), A("Kangwŏn-do", "North Korea")), 3, "")
reg("Hamgyong", ["Hamgyeong", "Northeast Korea"], As("North Korea", "Hamgyŏng-bukto", "Hamgyŏng-namdo", "Ryanggang", "Rasŏn"), 3, "")
reg("Pyongan", ["Pyeongan", "Northwest Korea"], As("North Korea", "P'yŏngan-bukto", "P'yŏngan-namdo", "P'yŏngyang", "Chagang-do"), 3, "")
reg("Hwanghae", [], As("North Korea", "Hwanghae-bukto", "Hwanghae-namdo"), 3, "")
reg("Jeju", ["Tamna", "Cheju"], A("Jeju", "South Korea"), 3, "")
reg("Hokkaido", ["Ezo", "Yezo", "Hokkaidō"], A("Hokkaido", "Japan"), 3, "")
reg("Tohoku", ["Mutsu and Dewa", "Oshu", "Northern Honshu"], A("Tohoku", "Japan"), 3, "")
reg("Kanto", ["Kantō", "Kanto plain"], A("Kanto", "Japan"), 3, "")
reg("Chubu", ["Chūbu", "Central Honshu"], A("Chubu", "Japan"), 3, "")
reg("Kansai", ["Kinki", "Kinai"], A("Kinki", "Japan"), 3, "")
reg("Chugoku", ["Chūgoku", "Western Honshu"], A("Chugoku", "Japan"), 3, "")
reg("Shikoku", [], A("Shikoku", "Japan"), 3, "")
reg("Kyushu", ["Kyūshū"], U(A("Kyushu", "Japan"), As("Japan", "Nagasaki", "Saga")), 3, "Two prefectures carry no region value in Natural Earth and are added by name.")
reg("Ryukyu", ["Okinawa", "Ryukyu Islands", "Loochoo", "Liuqiu"], A("Okinawa", "Japan"), 3, "")

# ----------------------------------------------------------------------------
# South Asia
# ----------------------------------------------------------------------------
reg("Deccan", ["Deccan plateau", "Dakshina", "Dakhin"], As("India", "Maharashtra", "Karnataka", "Telangana", "Andhra Pradesh", "Goa"), 2, "The states of the plateau, including their coasts.")
reg("Bengal", ["Bangla", "Bengal (undivided)", "Vanga", "Gauda (broad)"], U(A("West Bengal", "India"), C("Bangladesh")), 3, "")
reg("Punjab", ["Panjab", "Land of Five Rivers", "Punjab (undivided)"], U(As("Pakistan", "Punjab", "F.C.T."), As("India", "Punjab", "Haryana", "Chandigarh")), 2, "")
reg("Sindh", ["Sind", "Sindhu"], A("Sind", "Pakistan"), 3, "")
reg("Gujarat (region)", ["Gujarat", "Gurjaratra", "Lata"], As("India", "Gujarat", "Dadra and Nagar Haveli and Daman and Diu"), 3, "")
reg("Malwa", ["Malwa plateau", "Avanti", "Malava"], I(As("India", "Madhya Pradesh", "Rajasthan"), PG([[74.0, 22.0], [78.5, 22.0], [78.5, 25.0], [75.0, 25.2], [74.0, 24.0]])), 2, "")
reg("Kashmir", ["Jammu and Kashmir (princely state)", "Kashmir (whole)"],
    U(As("India", "Jammu and Kashmir", "Ladakh"), As("Pakistan", "Azad Kashmir", "Northern Areas"), C("Siachen Glacier")), 2, "Aksai Chin (inside China's Xinjiang row) is left out.")
reg("Kashmir Valley", ["Vale of Kashmir", "Kashmir proper"], P("Srinagar", 70, "India"), 2, "")
reg("Rajputana", ["Rajasthan", "Rajput states"], A("Rajasthan", "India"), 3, "")
reg("Saurashtra", ["Kathiawar", "Kathiawad"], I(A("Gujarat", "India"), PG([[68.8, 20.6], [72.4, 20.6], [72.4, 22.6], [70.8, 23.4], [68.8, 23.2]])), 2, "")
reg("Kutch", ["Kachchh", "Cutch"], I(A("Gujarat", "India"), PG([[68.0, 22.6], [71.8, 22.6], [71.8, 24.7], [68.0, 24.7]])), 2, "")
reg("Mewar", ["Udaipur (state)", "Medapata"], U(P("Udaipur", 90, "India"), P("Chittorgarh", 60, "India")), 2, "")
reg("Marwar", ["Jodhpur (state)"], P("Jodhpur", 150, "India"), 2, "")
reg("Magadha", [], U(P("Patna", 120, "India"), P("Gaya", 80, "India")), 2, "")
reg("Bihar (region)", ["Bihar"], A("Bihar", "India"), 3, "")
reg("Awadh", ["Oudh", "Kosala (core)", "Avadh"], I(A("Uttar Pradesh", "India"), PG([[79.5, 25.4], [83.5, 25.4], [83.5, 28.5], [79.5, 28.5]])), 2, "")
reg("Doab", ["Ganges-Yamuna Doab", "Ganga-Jamuna Doab"], I(A("Uttar Pradesh", "India"), PG([[77.3, 25.3], [81.5, 25.3], [81.9, 26.5], [79.0, 29.5], [77.3, 30.3]])), 1, "")
reg("Rohilkhand", ["Katehr"], P("Bareilly", 90, "India"), 2, "")
reg("Bundelkhand", ["Jejakabhukti"], I(As("India", "Uttar Pradesh", "Madhya Pradesh"), PG([[77.8, 23.8], [81.0, 23.8], [81.0, 26.2], [77.8, 26.2]])), 1, "")
reg("Odisha", ["Orissa", "Kalinga", "Utkala"], A("Odisha", "India"), 3, "")
reg("Gondwana", ["Gond country"], U(A("Chhattisgarh", "India"), I(A("Madhya Pradesh", "India"), PG([[78.0, 21.5], [82.0, 21.5], [82.0, 24.0], [78.0, 24.0]]))), 1, "")
reg("Vidarbha", ["Berar"], I(A("Maharashtra", "India"), PG([[75.8, 19.0], [80.5, 19.0], [80.5, 22.0], [75.8, 22.0]])), 2, "")
reg("Konkan", ["Konkan coast", "Aparanta"], I(As("India", "Maharashtra", "Goa", "Karnataka"), PG([[72.5, 14.5], [73.3, 14.5], [74.5, 16.5], [73.8, 19.5], [72.5, 20.5]])), 1, "")
reg("Karnataka (region)", ["Karnataka", "Mysore (state)", "Kannada country", "Karnata"], A("Karnataka", "India"), 3, "")
reg("Andhra", ["Telugu country", "Andhra and Telangana"], As("India", "Andhra Pradesh", "Telangana"), 3, "")
reg("Telangana (region)", ["Telangana", "Golconda (region)"], A("Telangana", "India"), 3, "")
reg("Tamilakam", ["Tamil country", "Tamilagam", "Dravida"], As("India", "Tamil Nadu", "Kerala", "Puducherry"), 2, "")
reg("Tamil Nadu (region)", ["Tamil Nadu", "Madras Presidency (core)", "Carnatic (south)"], A("Tamil Nadu", "India"), 3, "")
reg("Kerala (region)", ["Kerala", "Malabar coast", "Chera country", "Malabar"], A("Kerala", "India"), 3, "")
reg("Coromandel", ["Coromandel Coast", "Cholamandalam"], I(As("India", "Tamil Nadu", "Andhra Pradesh", "Puducherry"), PG([[79.0, 8.0], [81.0, 8.0], [81.0, 16.5], [79.3, 16.5], [79.0, 12.0]])), 1, "")
reg("Carnatic", ["Karnatak (Arcot)", "Carnatic (Nawab's)"], U(A("Tamil Nadu", "India"), I(A("Andhra Pradesh", "India"), PG([[78.0, 12.5], [80.5, 12.5], [80.5, 16.5], [78.0, 16.5]]))), 1, "")
reg("Mysore (region)", ["Mysore", "Mysore kingdom (core)"], I(A("Karnataka", "India"), PG([[74.5, 11.5], [78.5, 11.5], [78.5, 14.0], [74.5, 14.0]])), 2, "")
reg("Khandesh", [], I(A("Maharashtra", "India"), PG([[74.0, 20.3], [76.5, 20.3], [76.5, 21.8], [74.0, 21.8]])), 2, "")
reg("Assam (region)", ["Assam", "Kamarupa", "Ahom kingdom", "Brahmaputra valley"], A("Assam", "India"), 3, "")
reg("Northeast India", ["Seven Sister States"], A("Northeast", "India"), 3, "")
reg("Ladakh", ["Maryul", "Little Tibet"], A("Ladakh", "India"), 3, "")
reg("Sri Lanka (island)", ["Ceylon", "Lanka", "Taprobane", "Serendib", "Sri Lanka"], C("Sri Lanka"), 3, "")
reg("Jaffna", ["Jaffna peninsula", "Jaffna kingdom (core)"], I(C("Sri Lanka"), PG([[79.5, 9.3], [80.7, 9.3], [80.7, 10.0], [79.5, 10.0]])), 2, "")
reg("Kandy (region)", ["Kandyan kingdom", "Kandy"], P("Kandy", 60, "Sri Lanka"), 2, "")
reg("Chittagong (region)", ["Chittagong", "Chattogram"], A("Chittagong", "Bangladesh"), 3, "")
reg("Sylhet (region)", ["Sylhet", "Srihatta"], A("Sylhet", "Bangladesh"), 3, "")
reg("Arakan", ["Rakhine", "Rakhine State"], A("Rakhine", "Myanmar"), 3, "")
reg("Baltistan", ["Little Tibet (Baltistan)", "Skardu region"], I(A("Northern Areas", "Pakistan"), PG([[74.5, 34.5], [77.5, 34.5], [77.5, 36.0], [74.5, 36.0]])), 2, "")
reg("Gilgit", ["Dardistan", "Gilgit region"], M(A("Northern Areas", "Pakistan"), R("Baltistan")), 2, "")
reg("Khyber Pakhtunkhwa", ["North-West Frontier Province", "NWFP", "KPK"], As("Pakistan", "K.P.", "F.A.T.A."), 3, "")
reg("Pashtunistan", ["Pakhtunkhwa (broad)", "Pashtun lands"],
    U(As("Pakistan", "K.P.", "F.A.T.A."), As("Afghanistan", "Nangarhar", "Kunar", "Laghman", "Paktya", "Paktika", "Khost", "Kandahar", "Zabul", "Hilmand", "Ghazni", "Uruzgan", "Kabul", "Logar", "Wardak")), 1, "")

# ----------------------------------------------------------------------------
# South-east Asia
# ----------------------------------------------------------------------------
reg("Tonkin", ["Bac Ky", "Bắc Kỳ", "Northern Vietnam", "Dai Viet (core)", "Jiaozhi", "Giao Chi", "Annam (Tang protectorate core)"],
    I(C("Vietnam"), PG([[101.5, 19.8], [106.0, 19.8], [108.3, 20.7], [108.3, 23.6], [101.5, 23.6]])), 2, "Vietnam north of the Ninh Binh - Thanh Hoa line.")
reg("Annam", ["Trung Ky", "Trung Kỳ", "Central Vietnam", "Annam (protectorate)"],
    I(C("Vietnam"), PG([[103.0, 10.9], [110.0, 10.9], [110.0, 20.7], [106.0, 19.8], [103.0, 19.8]])), 2, "")
reg("Cochinchina", ["Nam Ky", "Nam Kỳ", "Southern Vietnam", "Cochin China"], I(C("Vietnam"), PG([[103.5, 8.0], [110.0, 8.0], [110.0, 11.6], [103.5, 11.6]])), 2, "")
reg("Champa", ["Chămpa", "Lin-yi", "Linyi", "Cham lands"],
    I(C("Vietnam"), PG([[105.8, 18.1], [108.2, 18.1], [110.0, 16.0], [110.0, 10.8], [107.3, 10.6], [106.8, 11.7], [107.5, 13.5], [107.2, 15.0], [106.2, 17.0]])), 2, "The coast from the Hoanh Son pass to Phan Thiet.")
reg("Red River Delta", ["Song Hong delta", "Tonkin delta"], P("Hanoi", 80, "Vietnam"), 2, "")
reg("Mekong Delta", ["Cuu Long delta", "Mekong Delta (Vietnam)"], I(C("Vietnam"), PG([[104.3, 8.3], [107.2, 8.3], [107.2, 11.0], [104.3, 11.0]])), 2, "")
reg("Angkor (region)", ["Angkor", "Khmer heartland", "Siem Reap region"], P("Angkor", 120, "Cambodia"), 2, "")
reg("Lan Xang (core)", ["Luang Prabang (kingdom)", "Lan Xang"], P("Luang Prabang", 150, "Laos"), 2, "")
reg("Champasak", ["Bassac", "Southern Laos"], As("Laos", "Champasak", "Saravan", "Attapu", "Xékong"), 2, "")
reg("Siam (core)", ["Central Thailand", "Chao Phraya basin", "Ayutthaya (region)", "Siam"], A("Central", "Thailand"), 2, "")
reg("Lanna", ["Lan Na", "Northern Thailand", "Chiang Mai (kingdom)"], A("Northern", "Thailand"), 2, "")
reg("Isan", ["Northeast Thailand", "Khorat Plateau", "Isaan"], A("Northeastern", "Thailand"), 3, "")
reg("Southern Thailand", ["Thai peninsula", "Nakhon Si Thammarat (region)"], A("Southern", "Thailand"), 3, "")
reg("Pattani", ["Patani", "Patani sultanate (core)"], As("Thailand", "Pattani", "Yala", "Narathiwat"), 3, "")
reg("Peninsular Malaysia", ["Malaya", "Federation of Malaya", "British Malaya", "West Malaysia"], M(C("Malaysia"), As("Malaysia", "Sabah", "Sarawak", "Labuan")), 3, "")
reg("Malay Peninsula", ["Golden Chersonese", "Malay peninsula (whole)"], U(R("Peninsular Malaysia"), A("Southern", "Thailand"), C("Singapore")), 2, "")
reg("Malacca (state)", ["Melaka", "Malacca"], A("Melaka", "Malaysia"), 3, "")
reg("Kedah", ["Kedah (state)", "Queda"], A("Kedah", "Malaysia"), 3, "")
reg("Johor", ["Johore"], A("Johor", "Malaysia"), 3, "")
reg("Upper Burma", ["Ava (region)", "Pagan (region)", "Dry Zone (Burma)"], As("Myanmar", "Mandalay", "Sagaing", "Magway"), 2, "")
reg("Lower Burma", ["Pegu (region)", "Ramannadesa", "Hanthawaddy (region)", "Mon country"], As("Myanmar", "Bago", "Yangon", "Ayeyarwady", "Mon"), 2, "")
reg("Shan States", ["Shan", "Shan plateau"], A("Shan", "Myanmar"), 3, "")
reg("Tenasserim", ["Tanintharyi"], A("Tanintharyi", "Myanmar"), 3, "")
reg("Kachin", ["Kachin State"], A("Kachin", "Myanmar"), 3, "")
reg("Sumatra", ["Sumatera", "Suvarnadvipa"], As("Indonesia", "Aceh", "Sumatera Utara", "Sumatera Barat", "Riau", "Kepulauan Riau", "Jambi", "Sumatera Selatan", "Bengkulu", "Lampung", "Bangka-Belitung"), 3, "")
reg("Java", ["Jawa", "Yavadvipa"], As("Indonesia", "Jawa Barat", "Jawa Tengah", "Jawa Timur", "Banten", "Jakarta Raya", "Yogyakarta"), 3, "")
reg("Borneo", ["Kalimantan (island)", "Kalimantan"], U(As("Indonesia", "Kalimantan Barat", "Kalimantan Tengah", "Kalimantan Selatan", "Kalimantan Timur"), As("Malaysia", "Sabah", "Sarawak", "Labuan"), C("Brunei")), 3, "")
reg("Sulawesi", ["Celebes"], As("Indonesia", "Sulawesi Utara", "Sulawesi Tengah", "Sulawesi Selatan", "Sulawesi Tenggara", "Sulawesi Barat", "Gorontalo"), 3, "")
reg("Moluccas", ["Maluku", "Spice Islands", "Maluku Islands"], As("Indonesia", "Maluku", "Maluku Utara"), 3, "")
reg("Lesser Sunda Islands", ["Nusa Tenggara", "Lesser Sundas"], U(As("Indonesia", "Bali", "Nusa Tenggara Barat", "Nusa Tenggara Timur"), C("Timor-Leste")), 3, "")
reg("New Guinea", ["Papua (island)", "Irian"], U(As("Indonesia", "Papua", "Papua Barat"), C("Papua New Guinea")), 3, "")
reg("Luzon", [], I(C("Philippines"), PG([[119.5, 12.3], [124.5, 12.3], [124.5, 19.0], [119.5, 19.0]])), 2, "")
reg("Visayas", ["Visayan Islands"], I(C("Philippines"), PG([[121.5, 9.0], [126.2, 9.0], [126.2, 12.3], [121.5, 12.3]])), 2, "")
reg("Mindanao", [], I(C("Philippines"), PG([[118.5, 4.5], [127.0, 4.5], [127.0, 9.9], [121.5, 9.0]])), 2, "Includes the Sulu archipelago.")
reg("Sulu", ["Sulu archipelago", "Sulu sultanate (core)"], I(C("Philippines"), PG([[118.7, 4.5], [122.3, 4.5], [122.3, 6.6], [118.7, 6.6]])), 2, "")
reg("Aceh", ["Atjeh", "Achin"], A("Aceh", "Indonesia"), 3, "")
reg("Minangkabau", ["West Sumatra", "Pagaruyung (core)"], A("Sumatera Barat", "Indonesia"), 3, "")
reg("Srivijaya (core)", ["Palembang (region)", "Srivijaya"], P("Palembang", 150, "Indonesia"), 2, "")
reg("Mataram (Java)", ["Central Java (historical)", "Mataram"], As("Indonesia", "Jawa Tengah", "Yogyakarta"), 2, "")
reg("Majapahit (core)", ["Majapahit", "Trowulan (region)", "East Java (historical)"], P("Trowulan", 120, "Indonesia"), 2, "")

# ----------------------------------------------------------------------------
# Mesopotamia, the Levant and Arabia
# ----------------------------------------------------------------------------
reg("Mesopotamia", ["Iraq (historical)", "Bilad al-Rafidayn", "Land between the rivers", "Mesopotamia (whole)"],
    U(C("Iraq"), As("Syria", "Hasaka (Al Haksa)", "Dayr Az Zawr", "Ar Raqqah"), As("Turkey", "Sanliurfa", "Mardin", "Diyarbakir", "Batman", "Sirnak"), C("Kuwait")), 2, "")
reg("Assyria", ["Assur (region)", "Athura", "Adiabene (broad)", "Assyrian heartland"],
    U(As("Iraq", "Ninawa", "Dihok", "Arbil", "At-Ta'mim", "Sala ad-Din"), A("Hasaka (Al Haksa)", "Syria")), 2, "")
reg("Babylonia", ["Lower Mesopotamia", "Sawad", "Chaldea", "Sumer and Akkad"],
    As("Iraq", "Baghdad", "Babil", "Karbala'", "An-Najaf", "Al-Qādisiyyah", "Wasit", "Maysan", "Dhi-Qar", "Al-Muthannia", "Al-Basrah", "Diyala"), 2, "")
reg("Sumer", ["Shumer", "Lower Babylonia", "Sumerian city-states"], As("Iraq", "Dhi-Qar", "Al-Muthannia", "Al-Qādisiyyah", "Al-Basrah", "Maysan", "An-Najaf"), 2, "")
reg("Akkad", ["Agade (region)", "Upper Babylonia", "Akkadian heartland"], As("Iraq", "Baghdad", "Babil", "Diyala", "Karbala'", "Wasit"), 2, "")
reg("Levant", ["Greater Syria", "Bilad al-Sham", "Sham", "Syria (historical)", "al-Sham", "Mashriq (west)"],
    U(C("Syria"), C("Lebanon"), C("Israel"), C("Palestine"), C("Jordan"), A("Hatay", "Turkey")), 3, "")
reg("Phoenicia", ["Phoenician coast", "Canaan (coast)"], U(C("Lebanon"), As("Syria", "Tartus", "Lattakia")), 2, "")
reg("Judea", ["Judaea", "Yehud", "Judah (core)", "Judean hills"], U(C("Palestine"), A("Jerusalem", "Israel"), P("Hebron", 40), P("Jerusalem", 40)), 2, "Palestine's West Bank also carries Samaria; the Roman province is 'Roman Judaea'.")
reg("Roman Judaea", ["Judaea (province)", "Syria Palaestina", "Holy Land", "Palestine (region)", "Eretz Israel", "Cisjordan"], U(C("Israel"), C("Palestine")), 2, "")
reg("Samaria", ["Shomron"], I(C("Palestine"), PG([[34.9, 31.85], [35.6, 31.85], [35.6, 32.6], [34.9, 32.6]])), 2, "")
reg("Galilee", ["Galil", "Northern District (Israel)"], A("HaZafon", "Israel"), 2, "")
reg("Negev", ["Naqab", "Southern District (Israel)"], A("HaDarom", "Israel"), 2, "")
reg("Golan", ["Golan Heights", "Gaulanitis"], PG([[35.55, 32.65], [36.0, 32.65], [36.05, 33.1], [35.9, 33.4], [35.6, 33.35]]), 2,
    "Natural Earth's Quneitra unit is a sliver, so the plateau is drawn as a polygon.")
reg("Hauran", ["Auranitis", "Hawran"], U(As("Syria", "As Suwayda'", "Dar`a", "Quneitra"), A("Irbid", "Jordan")), 2, "")
reg("Transjordan", ["Emirate of Transjordan", "Jordan (east bank)", "Oultrejordain"], C("Jordan"), 3, "")
reg("Moab", [], As("Jordan", "Karak", "Madaba"), 2, "")
reg("Edom", ["Idumea", "Nabataea (core)"], As("Jordan", "Tafilah", "Ma`an", "Aqaba"), 2, "")
reg("Ammon", ["Ammonite lands"], As("Jordan", "Amman", "Balqa", "Zarqa"), 2, "")
reg("Gilead", [], As("Jordan", "Irbid", "Ajlun", "Jarash", "Balqa"), 2, "")
reg("Canaan", ["Land of Canaan", "Southern Levant"],
    U(C("Israel"), C("Palestine"), C("Lebanon"), As("Jordan", "Irbid", "Ajlun", "Jarash", "Balqa", "Amman", "Madaba", "Karak"), As("Syria", "Quneitra", "Dar`a")), 1, "")
reg("Damascus (region)", ["Ghouta", "Damascene", "Damascus"], P("Damascus", 80, "Syria"), 2, "")
reg("Aleppo (region)", ["Aleppo", "Halab (region)"], P("Aleppo", 80, "Syria"), 2, "")
reg("Coele-Syria", ["Beqaa", "Bekaa valley"], A("Beqaa", "Lebanon"), 1, "")
reg("Syrian Desert", ["Badiyat al-Sham", "Hamad"], U(A("Al-Anbar", "Iraq"), As("Syria", "Homs (Hims)", "Dayr Az Zawr"), As("Jordan", "Mafraq", "Ma`an")), 1, "")
reg("Hejaz", ["Hijaz", "Al-Hijaz"], As("Saudi Arabia", "Makkah", "Al Madinah", "Tabuk"), 3, "")
reg("Nejd", ["Najd", "Central Arabia"], As("Saudi Arabia", "Ar Riyad", "Al Quassim", "Ha'il"), 3, "")
reg("Al-Ahsa", ["Hasa", "Al-Hasa", "Eastern Province (Saudi)", "Bahrayn (mainland)", "Lahsa"], A("Ash Sharqiyah", "Saudi Arabia"), 3, "")
reg("Bahrain (historical)", ["Bahrayn (region)", "Greater Bahrain", "Bahrain (medieval region)"], U(C("Bahrain"), C("Qatar"), A("Ash Sharqiyah", "Saudi Arabia")), 2, "")
reg("Asir", ["Asir and Jizan", "`Asir"], As("Saudi Arabia", "`Asir", "Jizan", "Najran", "Al Bahah"), 3, "")
reg("Yemen", ["Arabia Felix", "Yemen (country)", "Al-Yaman"], C("Yemen"), 3, "")
reg("Greater Yemen", ["Yemen (historical)", "Yemen with Asir and Najran"], U(C("Yemen"), As("Saudi Arabia", "`Asir", "Jizan", "Najran")), 2, "")
reg("Hadramawt", ["Hadhramaut", "Hadramout", "Hadramaut"], As("Yemen", "Hadramawt", "Shabwah", "Al Mahrah"), 3, "")
reg("Tihama", ["Tihamah", "Red Sea coastal plain"], U(As("Yemen", "Al Hudaydah", "Hajjah"), A("Jizan", "Saudi Arabia")), 2, "")
reg("Aden (region)", ["Aden Protectorate (west)", "South Yemen (core)", "Aden"], As("Yemen", "`Adan", "Lahij", "Abyan"), 3, "")
reg("Oman", ["Oman (country)", "Magan", "Mazun"], C("Oman"), 3, "")
reg("Oman (historical)", ["Oman proper with the Trucial coast", "Greater Oman"], U(C("Oman"), C("United Arab Emirates")), 2, "")
reg("Dhofar", ["Zufar"], A("Dhofar", "Oman"), 3, "")
reg("Trucial Coast", ["Trucial States", "Pirate Coast", "Trucial Oman"], C("United Arab Emirates"), 3, "")
reg("Arabia", ["Arabian Peninsula", "Jazirat al-Arab"], U(C("Saudi Arabia"), C("Yemen"), C("Oman"), C("United Arab Emirates"), C("Qatar"), C("Bahrain"), C("Kuwait")), 3, "")
reg("Sinai", ["Sinai Peninsula"], As("Egypt", "Janub Sina'", "Shamal Sina'"), 3, "")

# ----------------------------------------------------------------------------
# Egypt and Africa
# ----------------------------------------------------------------------------
reg("Lower Egypt", ["Nile Delta", "Delta (Egypt)", "Ta-Mehu"],
    As("Egypt", "Al Iskandariyah", "Al Buhayrah", "Kafr ash Shaykh", "Al Gharbiyah", "Al Minufiyah", "Al Qalyubiyah", "Ad Daqahliyah", "Dumyat", "Ash Sharqiyah", "Bur Sa`id", "Al Isma`iliyah", "Al Qahirah", "Al Jizah", "Matruh"), 2, "Matruh brings the Mediterranean desert coast.")
reg("Upper Egypt", ["Said", "Sa'id", "Thebaid (broad)", "Ta-Shemau"],
    As("Egypt", "Bani Suwayf", "Al Fayyum", "Al Minya", "Asyut", "Suhaj", "Qina", "Luxor", "Aswan", "Al Bahr al Ahmar", "Al Wadi at Jadid"), 2, "")
reg("Nile Valley (Egypt)", ["Egypt (Nile valley and delta)", "Egypt proper"], M(C("Egypt"), As("Egypt", "Matruh", "Al Wadi at Jadid", "Janub Sina'", "Shamal Sina'", "Al Bahr al Ahmar")), 2, "")
reg("Fayyum", ["Faiyum", "Fayum"], A("Al Fayyum", "Egypt"), 3, "")
reg("Western Desert", ["Libyan Desert (Egypt)", "Egyptian oases"], As("Egypt", "Al Wadi at Jadid", "Matruh"), 3, "")
reg("Nubia", ["Nubia (Nile between the cataracts)", "Nubian Nile"], U(As("Sudan", "Northern", "River Nile"), A("Aswan", "Egypt")), 2, "")
reg("Lower Nubia", ["Wawat"], U(A("Aswan", "Egypt"), I(A("Northern", "Sudan"), PG([[30.0, 21.0], [34.0, 21.0], [34.0, 22.2], [30.0, 22.2]]))), 2, "")
reg("Kush", ["Upper Nubia", "Kingdom of Kush (core)", "Napata and Meroe"], As("Sudan", "Northern", "River Nile", "Khartoum"), 2, "")
reg("Nilotic Sudan", ["Funj (core)", "Sennar (sultanate core)", "Gezira (broad)", "Central Sudan"], As("Sudan", "Khartoum", "Gezira", "White Nile", "Blue Nile", "Sennar", "River Nile"), 2, "")
reg("Darfur", ["Dar Fur"], A("Darfur", "Sudan"), 3, "")
reg("Kordofan", ["Kurdufan"], A("Kordofan", "Sudan"), 3, "")
reg("Beja country", ["Eastern Sudan", "Red Sea Hills"], As("Sudan", "Red Sea", "Kassala"), 2, "")
reg("Maghreb", ["Greater Maghreb", "Barbary", "Northwest Africa", "Barbary Coast"], U(C("Morocco"), C("Algeria"), C("Tunisia"), C("Libya"), C("W. Sahara"), C("Mauritania")), 2, "")
reg("Maghreb (core)", ["Maghrib", "Barbary (core)", "Morocco, Algeria and Tunisia"], U(C("Morocco"), C("Algeria"), C("Tunisia")), 3, "")
reg("Tripolitania", ["Tarabulus (region)"], As("Libya", "An Nuqat al Khams", "Az Zawiyah", "Al Jifarah", "Tajura' wa an Nawahi al Arba", "Al Marqab", "Misratah", "Mizdah", "Ghadamis", "Surt"), 2, "")
reg("Cyrenaica", ["Barqa", "Pentapolis (broad)", "Cirenaica"], As("Libya", "Benghazi", "Al Marj", "Al Jabal al Akhdar", "Al Qubbah", "Al Butnan", "Ajdabiya", "Al Kufrah"), 3, "")
reg("Fezzan", ["Phazania", "Fazzan"], As("Libya", "Sabha", "Murzuq", "Wadi al Hayaa", "Ash Shati'", "Ghat", "Al Jufrah"), 3, "")
reg("Ifriqiya", ["Africa (medieval)", "Ifriqiyah"],
    U(C("Tunisia"), R("Tripolitania"), As("Algeria", "Constantine", "Annaba", "Skikda", "Guelma", "Souk Ahras", "El Tarf", "Tébessa", "Jijel", "Mila", "Oum el Bouaghi", "Khenchela", "Batna", "Sétif", "Béjaïa", "Bordj Bou Arréridj", "M'Sila", "Biskra")), 2, "")
reg("Africa Proconsularis", ["Africa (Roman province)", "Zeugitana and Byzacena", "Roman Africa"],
    U(C("Tunisia"), R("Tripolitania"), As("Algeria", "Constantine", "Annaba", "Skikda", "Guelma", "Souk Ahras", "El Tarf", "Tébessa")), 2, "")
reg("Numidia", ["Numidian kingdom"],
    As("Algeria", "Constantine", "Annaba", "Skikda", "Guelma", "Souk Ahras", "El Tarf", "Tébessa", "Jijel", "Mila", "Oum el Bouaghi", "Khenchela", "Batna", "Sétif", "Béjaïa", "Bordj Bou Arréridj", "M'Sila", "Biskra", "Bouira", "Tizi Ouzou", "Boumerdès", "Alger", "Blida", "Médéa", "Djelfa"), 1, "")
reg("Mauretania", ["Mauretania (Roman)", "Moorish kingdom"],
    U(C("Morocco"), As("Algeria", "Oran", "Tlemcen", "Aïn Témouchent", "Sidi Bel Abbès", "Mostaganem", "Relizane", "Mascara", "Saïda", "Tiaret", "Chlef", "Aïn Defla", "Tissemsilt", "Tipaza", "Alger", "Blida", "Médéa")), 1, "")
reg("Kabylia", ["Kabylie"], As("Algeria", "Tizi Ouzou", "Béjaïa", "Bouira", "Boumerdès"), 3, "")
reg("Oranais", ["Oran (region)", "Western Algeria", "Tlemcen (kingdom core)"], As("Algeria", "Oran", "Tlemcen", "Aïn Témouchent", "Sidi Bel Abbès", "Mostaganem", "Mascara", "Relizane", "Saïda"), 2, "")
reg("Constantinois", ["Constantine (region)", "Beylik of Constantine", "Eastern Algeria"], As("Algeria", "Constantine", "Annaba", "Skikda", "Guelma", "Souk Ahras", "El Tarf", "Mila", "Jijel", "Oum el Bouaghi", "Sétif", "Batna", "Tébessa", "Khenchela"), 2, "")
reg("Rif", ["Rif mountains", "Er Rif"], As("Morocco", "Taza - Al Hoceima - Taounate", "Tanger - Tétouan"), 2, "")
reg("Sous", ["Sus", "Souss"], A("Souss - Massa - Draâ", "Morocco"), 2, "")
reg("Tafilalt", ["Tafilalet", "Sijilmasa (region)"], A("Meknès - Tafilalet", "Morocco"), 1, "")
reg("Sahara", ["Sahara desert", "Great Desert"],
    I(U(C("Algeria"), C("Libya"), C("Egypt"), C("Mauritania"), C("Mali"), C("Niger"), C("Chad"), C("Sudan"), C("Morocco"), C("W. Sahara"), C("Tunisia")),
      PG([[-17.5, 16.0], [-5.0, 16.0], [15.0, 16.0], [25.0, 16.0], [37.0, 17.0], [37.0, 31.0], [25.0, 31.0], [10.0, 33.0], [-5.0, 31.0], [-13.0, 27.0], [-17.5, 21.0]])), 2, "")
reg("Sahel", ["Sahel belt", "Sudanic belt (north)"],
    I(U(C("Mauritania"), C("Senegal"), C("Mali"), C("Burkina Faso"), C("Niger"), C("Nigeria"), C("Chad"), C("Sudan"), C("Eritrea"), C("Ethiopia"), C("Cameroon"), C("Gambia")),
      PG([[-17.5, 12.5], [-17.5, 17.5], [0.0, 17.5], [15.0, 17.0], [25.0, 17.0], [38.0, 17.0], [40.0, 15.0], [38.0, 12.0], [25.0, 11.0], [15.0, 11.5], [5.0, 12.0], [-5.0, 12.5]])), 2, "")
reg("Swahili Coast", ["Zanj coast", "Azania (coast)", "Swahili coast", "Zanj"],
    U(As("Somalia", "Banaadir", "Shabeellaha Hoose", "Jubbada Hoose"), A("Coast", "Kenya"),
      As("Tanzania", "Tanga", "Pwani", "Dar-Es-Salaam", "Lindi", "Mtwara", "Zanzibar South and Central", "Zanzibar West", "Kaskazini-Unguja", "Kaskazini-Pemba", "Kusini-Pemba"),
      As("Mozambique", "Cabo Delgado", "Nampula")), 2, "")
reg("Zanzibar", ["Unguja and Pemba", "Zanzibar islands", "Zanzibar (islands)"], As("Tanzania", "Zanzibar South and Central", "Zanzibar West", "Kaskazini-Unguja", "Kaskazini-Pemba", "Kusini-Pemba"), 3, "The islands; the sultanate's coastal strip is the Swahili Coast.")
reg("Horn of Africa", ["The Horn", "Somali peninsula (broad)"], U(C("Somalia"), C("Somaliland"), C("Djibouti"), C("Eritrea"), C("Ethiopia")), 3, "")
reg("Abyssinia", ["Ethiopia (historical)", "Habesha lands", "Ethiopian Empire (core)"], M(C("Ethiopia"), As("Ethiopia", "Somali", "Afar")), 2, "")
reg("Ethiopian Highlands", ["Abyssinian highlands", "Amhara and Tigray"], As("Ethiopia", "Tigray", "Amhara", "Addis Ababa"), 2, "")
reg("Tigray (region)", ["Tigray", "Axum (region)", "Aksumite heartland", "Tigray and Eritrea"], U(A("Tigray", "Ethiopia"), C("Eritrea")), 2, "")
reg("Shewa", ["Shoa", "Shawa"], P("Addis Ababa", 150, "Ethiopia"), 2, "")
reg("Harar (region)", ["Harar", "Hararghe", "Harar emirate"], P("Harar", 100, "Ethiopia"), 2, "")
reg("Afar", ["Danakil", "Afar Triangle"], U(A("Afar", "Ethiopia"), A("Debubawi Keyih Bahri", "Eritrea")), 3, "")
reg("Ogaden", ["Somali Region (Ethiopia)", "Ethiopian Somali region"], A("Somali", "Ethiopia"), 3, "")
reg("Somaliland", ["British Somaliland", "Northern Somalia"], C("Somaliland"), 3, "")
reg("Puntland", ["Majeerteen (core)"], As("Somalia", "Bari", "Nugaal", "Mudug"), 2, "")
reg("Benadir", ["Banaadir coast", "Mogadishu coast"], As("Somalia", "Banaadir", "Shabeellaha Dhexe", "Shabeellaha Hoose"), 2, "")
reg("African Great Lakes", ["Great Lakes (Africa)", "Interlacustrine region", "Great Lakes region (Africa)"],
    U(C("Uganda"), C("Rwanda"), C("Burundi"), As("Tanzania", "Kagera", "Mwanza", "Mara", "Geita", "Shinyanga", "Simiyu", "Kigoma"), As("Kenya", "Nyanza", "Western")), 2, "")
reg("Buganda", ["Kingdom of Buganda", "Ganda country"], P("Kampala", 100, "Uganda"), 2, "")
reg("Bunyoro", ["Bunyoro-Kitara"], P("Hoima", 80, "Uganda"), 1, "")
reg("Katanga", ["Shaba"], A("Katanga", "Democratic Republic of the Congo"), 3, "")
reg("Kongo", ["Kingdom of Kongo (core)", "Lower Congo", "Bakongo lands"],
    U(A("Bas-Congo", "Democratic Republic of the Congo"), As("Angola", "Zaire", "Uíge", "Cabinda"), I(C("Congo"), PG([[11.0, -5.5], [15.5, -5.5], [15.5, -3.5], [11.0, -3.5]]))), 2, "")
reg("Kasai", ["Kuba (region)", "Kasaï"], As("Democratic Republic of the Congo", "Kasaï-Occidental", "Kasaï-Oriental"), 2, "")
reg("Luba (region)", ["Luba kingdom (core)", "Luba"], I(A("Katanga", "Democratic Republic of the Congo"), PG([[22.5, -10.0], [28.5, -10.0], [28.5, -5.0], [22.5, -5.0]])), 1, "")
reg("Lunda (region)", ["Lunda empire (core)", "Lunda"], I(U(A("Katanga", "Democratic Republic of the Congo"), As("Angola", "Lunda Norte", "Lunda Sul", "Moxico")), PG([[18.0, -13.0], [26.0, -13.0], [26.0, -6.5], [18.0, -6.5]])), 1, "")
reg("Zambezia", ["Lower Zambezi", "Zambezi valley (lower)", "Rios de Sena"], As("Mozambique", "Zambezia", "Tete", "Sofala", "Manica"), 2, "")
reg("Mutapa", ["Monomotapa", "Mwenemutapa (core)"], U(As("Zimbabwe", "Mashonaland Central", "Mashonaland East", "Mashonaland West", "Harare"), As("Mozambique", "Tete", "Manica", "Sofala")), 1, "")
reg("Zimbabwe Plateau", ["Mashonaland and Matabeleland", "Zimbabwe (region)"], C("Zimbabwe"), 2, "")
reg("Mashonaland", ["Shona country"], As("Zimbabwe", "Mashonaland Central", "Mashonaland East", "Mashonaland West", "Harare"), 3, "")
reg("Matabeleland", ["Ndebele kingdom (core)", "Matabele country"], As("Zimbabwe", "Matabeleland North", "Matabeleland South", "Bulawayo"), 3, "")
reg("Cape (region)", ["Cape Colony (core)", "The Cape", "Cape Province"], As("South Africa", "Western Cape", "Eastern Cape", "Northern Cape"), 2, "")
reg("Natal", ["KwaZulu-Natal", "Zululand and Natal"], A("KwaZulu-Natal", "South Africa"), 3, "")
reg("Zululand", ["Zulu kingdom (core)", "KwaZulu"], I(A("KwaZulu-Natal", "South Africa"), PG([[30.5, -29.0], [33.0, -29.0], [33.0, -26.8], [30.5, -26.8]])), 2, "")
reg("Transvaal", ["South African Republic (core)", "Transvaal Province"], As("South Africa", "Gauteng", "Limpopo", "Mpumalanga", "North West"), 3, "")
reg("Orange Free State", ["Free State", "Orange River Colony", "Orange River Sovereignty"], A("Free State", "South Africa"), 3, "")
reg("Basutoland", ["Lesotho"], C("Lesotho"), 3, "")
reg("Bechuanaland", ["Botswana", "Tswana country"], C("Botswana"), 3, "")
reg("Namaqualand", ["Little and Great Namaqualand"], I(U(A("Northern Cape", "South Africa"), C("Namibia")), PG([[16.0, -31.0], [20.0, -31.0], [20.0, -25.5], [16.0, -25.5]])), 1, "")
reg("Ndongo", ["Ndongo and Matamba", "Angola (kingdom core)"], As("Angola", "Luanda", "Bengo", "Cuanza Norte", "Malanje"), 2, "")
reg("Benguela (region)", ["Benguela", "Ovimbundu highlands", "Bié plateau"], As("Angola", "Benguela", "Huambo", "Bié", "Cuanza Sul"), 2, "")
reg("Gold Coast", ["Ghana (colony)"], C("Ghana"), 3, "")
reg("Ashanti", ["Asante", "Asante (core)"], As("Ghana", "Ashanti", "Brong Ahafo"), 2, "")
reg("Dahomey", ["Benin (country)", "Abomey (kingdom)"], C("Benin"), 3, "The modern country; the Fon kingdom is its south.")
reg("Yorubaland", ["Yoruba country"], U(As("Nigeria", "Oyo", "Ogun", "Lagos", "Osun", "Ondo", "Ekiti", "Kwara"), I(C("Benin"), PG([[1.5, 6.2], [3.9, 6.2], [3.9, 9.5], [1.5, 9.5]]))), 2, "")
reg("Igboland", ["Igbo country", "Biafra (core)"], As("Nigeria", "Anambra", "Enugu", "Imo", "Abia", "Ebonyi"), 3, "")
reg("Benin (kingdom)", ["Edo kingdom", "Benin Empire (core)", "Bini"], As("Nigeria", "Edo", "Delta"), 2, "")
reg("Niger Delta", ["Oil Rivers"], As("Nigeria", "Rivers", "Bayelsa", "Delta", "Akwa Ibom"), 3, "")
reg("Hausaland", ["Hausa states", "Kasar Hausa", "Hausa Bakwai"], U(As("Nigeria", "Kano", "Katsina", "Sokoto", "Zamfara", "Kaduna", "Jigawa", "Kebbi"), As("Niger", "Maradi", "Zinder")), 2, "")
reg("Bornu", ["Kanem-Bornu (core)", "Borno"], U(As("Nigeria", "Borno", "Yobe"), As("Chad", "Kanem", "Lac"), A("Diffa", "Niger")), 2, "")
reg("Kanem", [], As("Chad", "Kanem", "Lac", "Barh El Gazel"), 2, "")
reg("Wadai", ["Ouaddai", "Wadai sultanate"], As("Chad", "Ouaddaï", "Wadi Fira", "Sila"), 2, "")
reg("Baguirmi", ["Bagirmi"], A("Chari-Baguirmi", "Chad"), 2, "")
reg("Senegambia", ["Senegal and Gambia"], U(C("Senegal"), C("Gambia")), 3, "")
reg("Futa Toro", ["Fouta Toro", "Takrur"], I(C("Senegal"), PG([[-16.5, 15.5], [-12.5, 15.5], [-12.5, 16.8], [-16.5, 16.8]])), 1, "")
reg("Futa Jallon", ["Fouta Djallon", "Fuuta Jaloo"], As("Guinea", "Labé", "Mamou"), 2, "")
reg("Manden", ["Mali Empire (core)", "Mande heartland", "Manding"], U(As("Mali", "Koulikoro", "Ségou", "Sikasso", "Kayes", "Bamako"), A("Kankan", "Guinea")), 1, "")
reg("Niger Bend", ["Middle Niger", "Songhai heartland", "Inland Niger Delta (broad)"], As("Mali", "Timbuktu", "Gao", "Mopti"), 2, "")
reg("Songhai (core)", ["Gao (region)", "Songhay"], As("Mali", "Gao", "Timbuktu"), 2, "")
reg("Azawad", ["Northern Mali"], As("Mali", "Timbuktu", "Gao", "Kidal"), 3, "")
reg("Air", ["Aïr", "Air Mountains", "Agadez (sultanate)"], A("Agadez", "Niger"), 3, "")
reg("Wagadu", ["Ghana Empire (core)", "Awkar"], U(As("Mauritania", "Hodh ech Chargui", "Hodh el Gharbi", "Assaba"), A("Kayes", "Mali")), 1, "")
reg("Jolof", ["Wolof country", "Jolof Empire (core)"], As("Senegal", "Louga", "Thiès", "Diourbel", "Dakar", "Saint-Louis", "Kaolack", "Fatick"), 2, "")
reg("Imerina", ["Merina kingdom (core)", "Central Madagascar"], P("Antananarivo", 120, "Madagascar"), 2, "")
reg("Tanganyika", ["German East Africa (core)", "Tanzania mainland", "Tanganyika Territory"], M(C("Tanzania"), R("Zanzibar")), 3, "")
reg("French West Africa", ["AOF", "Afrique occidentale française"], U(C("Senegal"), C("Mali"), C("Mauritania"), C("Guinea"), C("Côte d'Ivoire"), C("Burkina Faso"), C("Benin"), C("Niger")), 3, "")
reg("French Equatorial Africa", ["AEF", "Afrique équatoriale française"], U(C("Gabon"), C("Congo"), C("Central African Rep."), C("Chad")), 3, "")
reg("Italian East Africa", ["Africa Orientale Italiana"], U(C("Ethiopia"), C("Eritrea"), C("Somalia")), 3, "")
reg("Anglo-Egyptian Sudan", ["Sudan (condominium)"], U(C("Sudan"), C("S. Sudan")), 3, "")
reg("Equatoria", ["Southern Sudan"], C("S. Sudan"), 2, "")
reg("Bahr el Ghazal", ["Bahr al-Ghazal"], I(C("S. Sudan"), PG([[24.0, 5.5], [30.0, 5.5], [30.0, 10.0], [24.0, 10.0]])), 1, "")
reg("Spanish Morocco", ["Spanish protectorate in Morocco"], As("Morocco", "Tanger - Tétouan", "Taza - Al Hoceima - Taounate"), 1, "")

# ----------------------------------------------------------------------------
# The Americas
# ----------------------------------------------------------------------------
reg("Yucatan", ["Yucatan Peninsula", "Yucatán", "Yucatán Peninsula"], U(As("Mexico", "Yucatán", "Campeche", "Quintana Roo"), C("Belize"), A("Petén", "Guatemala")), 3, "")
reg("Valley of Mexico", ["Basin of Mexico", "Anahuac (core)", "Mexico basin"], As("Mexico", "Distrito Federal", "México"), 2, "")
reg("Central Mexico", ["Mesa Central", "Altiplano Central (Mexico)", "Mexican highlands"],
    As("Mexico", "Distrito Federal", "México", "Morelos", "Tlaxcala", "Puebla", "Hidalgo", "Querétaro", "Guanajuato", "Michoacán"), 2, "")
reg("Oaxaca", ["Oaxaca (region)", "Zapotec and Mixtec country"], A("Oaxaca", "Mexico"), 3, "")
reg("Michoacan", ["Michoacán", "Tarascan state (core)", "Purepecha country"], A("Michoacán", "Mexico"), 3, "")
reg("Chiapas", [], A("Chiapas", "Mexico"), 3, "")
reg("Guatemalan Highlands", ["Altos de Guatemala", "K'iche' and Kaqchikel country"],
    As("Guatemala", "Quiché", "Huehuetenango", "Totonicapán", "Quezaltenango", "San Marcos", "Sololá", "Chimaltenango", "Sacatepéquez", "Guatemala", "Baja Verapaz", "Alta Verapaz"), 2, "")
reg("Peten", ["Petén", "Maya lowlands (south)"], A("Petén", "Guatemala"), 3, "")
reg("Maya Lowlands", ["Maya lowlands", "Maya area (lowlands)"], U(As("Mexico", "Yucatán", "Campeche", "Quintana Roo", "Tabasco"), C("Belize"), A("Petén", "Guatemala")), 2, "")
reg("Mesoamerica", ["Mesoamerican culture area"],
    U(M(C("Mexico"), As("Mexico", "Baja California", "Baja California Sur", "Sonora", "Chihuahua", "Coahuila", "Nuevo León", "Tamaulipas", "Durango", "Sinaloa", "Zacatecas", "San Luis Potosí")),
      C("Guatemala"), C("Belize"), C("El Salvador"), C("Honduras"),
      I(C("Nicaragua"), PG([[-87.8, 10.6], [-85.5, 10.6], [-85.5, 13.5], [-87.8, 13.5]])), A("Guanacaste", "Costa Rica")), 2, "")
reg("Gulf Coast (Mexico)", ["Olmec heartland (broad)", "Totonac country", "Veracruz and Tabasco"], As("Mexico", "Veracruz", "Tabasco"), 3, "")
reg("Bajio", ["Bajío"], As("Mexico", "Guanajuato", "Querétaro", "Aguascalientes"), 2, "")
reg("Nueva Galicia", ["New Galicia"], As("Mexico", "Jalisco", "Nayarit", "Zacatecas", "Aguascalientes", "Colima"), 2, "")
reg("Nueva Vizcaya", ["New Biscay"], As("Mexico", "Durango", "Chihuahua"), 2, "Sinaloa and Sonora belonged to it before 1733.")
reg("Nuevo Santander", ["Tamaulipas (colonial)"], U(A("Tamaulipas", "Mexico"), I(A("Texas", USA), PG([[-100.0, 25.8], [-96.5, 25.8], [-96.5, 28.5], [-100.0, 28.5]]))), 2, "")
reg("Sonora y Sinaloa", ["Nueva Navarra", "Sonora and Sinaloa"], As("Mexico", "Sonora", "Sinaloa"), 3, "")
reg("Baja California (peninsula)", ["Antigua California", "Lower California", "Baja California"], As("Mexico", "Baja California", "Baja California Sur"), 3, "")
reg("Alta California", ["Upper California", "California (Mexican province)"], As(USA, "California", "Nevada", "Utah", "Arizona"), 2, "Arizona south of the Gila was Sonora; the Wyoming and Colorado slivers are left out.")
reg("New Mexico (province)", ["Santa Fe de Nuevo Mexico", "Nuevo México"],
    U(A("New Mexico", USA), I(A("Arizona", USA), PG([[-115.0, 33.0], [-109.0, 33.0], [-109.0, 37.0], [-115.0, 37.0]])),
      I(A("Colorado", USA), PG([[-109.1, 36.9], [-102.0, 36.9], [-102.0, 38.5], [-109.1, 38.5]]))), 2, "")
reg("Texas (region)", ["Tejas", "Texas", "Coahuila y Tejas (north)"], A("Texas", USA), 3, "")
reg("Louisiana", ["Louisiana Purchase", "Louisiana Territory", "Louisiana (purchase)"],
    As(USA, "Louisiana", "Arkansas", "Missouri", "Iowa", "Oklahoma", "Kansas", "Nebraska", "South Dakota", "North Dakota", "Minnesota", "Montana", "Wyoming", "Colorado"), 2,
    "The purchase of 1803 by whole states: Montana, Wyoming and Colorado overshoot west, Minnesota east of the Mississippi was not included.")
reg("French Louisiana", ["Louisiane", "Mississippi basin (French claim)", "Louisiana (French colony)"],
    U(R("Louisiana"), As(USA, "Illinois", "Indiana", "Wisconsin", "Mississippi", "Alabama", "Tennessee", "Kentucky", "Ohio", "Michigan")), 1, "")
reg("Lower Louisiana", ["Basse-Louisiane"], As(USA, "Louisiana", "Mississippi", "Arkansas"), 2, "")
reg("Illinois Country", ["Pays des Illinois", "Upper Louisiana", "Haute-Louisiane"], As(USA, "Illinois", "Missouri", "Indiana"), 2, "")
reg("Ohio Country", ["Ohio Valley", "Ohio Territory (colonial)"], U(As(USA, "Ohio", "Indiana", "West Virginia"), P("Pittsburgh", 150, USA)), 2, "")
reg("Northwest Territory", ["Old Northwest", "Territory Northwest of the River Ohio"], As(USA, "Ohio", "Indiana", "Illinois", "Michigan", "Wisconsin", "Minnesota"), 2, "")
reg("Oregon Country", ["Columbia District", "Oregon Territory (broad)"],
    U(As(USA, "Oregon", "Washington", "Idaho"), A("British Columbia", "Canada"), I(A("Montana", USA), PG([[-116.1, 44.3], [-112.0, 44.3], [-112.0, 49.0], [-116.1, 49.0]]))), 2, "British Columbia north of 54 40 overshoots.")
reg("Pacific Northwest", ["Cascadia"], U(As(USA, "Oregon", "Washington", "Idaho"), A("British Columbia", "Canada")), 3, "")
reg("Alaska", ["Russian America"], A("Alaska", USA), 3, "")
reg("Hawaii", ["Sandwich Islands", "Hawaiian Islands"], A("Hawaii", USA), 3, "")
reg("Florida", ["La Florida", "East Florida (broad)"], A("Florida", USA), 3, "")
reg("West Florida", ["Florida Occidental"],
    U(I(A("Florida", USA), PG([[-87.7, 29.5], [-85.0, 29.5], [-85.0, 31.1], [-87.7, 31.1]])),
      I(As(USA, "Alabama", "Mississippi", "Louisiana"), PG([[-91.7, 30.0], [-85.0, 30.0], [-85.0, 31.1], [-91.7, 31.1]]))), 2, "")
reg("New England", [], As(USA, "Maine", "New Hampshire", "Vermont", "Massachusetts", "Rhode Island", "Connecticut"), 3, "")
reg("Mid-Atlantic", ["Middle Colonies"], As(USA, "New York", "New Jersey", "Pennsylvania", "Delaware", "Maryland"), 3, "")
reg("American South", ["The South (US)", "Dixie", "Confederate states (broad)"],
    As(USA, "Virginia", "North Carolina", "South Carolina", "Georgia", "Florida", "Alabama", "Mississippi", "Louisiana", "Tennessee", "Kentucky", "Arkansas", "Texas"), 2, "")
reg("Thirteen Colonies", ["Original states", "British America (thirteen colonies)"],
    As(USA, "New Hampshire", "Massachusetts", "Rhode Island", "Connecticut", "New York", "New Jersey", "Pennsylvania", "Delaware", "Maryland", "Virginia", "North Carolina", "South Carolina", "Georgia", "Maine", "Vermont"), 2, "")
reg("Great Plains", ["Plains"], I(U(C(USA), C("Canada")), PG([[-104.5, 26.0], [-97.0, 26.0], [-96.0, 43.0], [-96.0, 53.5], [-114.0, 53.5], [-110.0, 40.0], [-104.5, 32.0]])), 1, "")
reg("Iroquoia", ["Haudenosaunee homeland", "Iroquois country", "Six Nations country"], P("Syracuse", 150, USA), 2, "")
reg("Great Lakes region", ["Great Lakes (region)", "Pays d'en Haut"], U(As(USA, "Michigan", "Wisconsin", "Ohio", "Illinois", "Indiana", "Minnesota", "New York", "Pennsylvania"), A("Ontario", "Canada")), 2, "")
reg("Rupert's Land", ["Ruperts Land", "Hudson's Bay Company lands", "Hudson Bay drainage"],
    U(As("Canada", "Manitoba", "Saskatchewan", "Alberta", "Nunavut"),
      I(As("Canada", "Ontario", "Québec"), PG([[-95.5, 49.0], [-79.0, 49.5], [-70.0, 50.5], [-64.0, 52.0], [-64.0, 63.0], [-80.0, 63.0], [-95.5, 60.0]]))), 2, "Alberta and Nunavut overshoot the watershed.")
reg("Acadia", ["Acadie", "Nova Scotia (French)"], U(As("Canada", "Nova Scotia", "New Brunswick", "Prince Edward Island"), A("Maine", USA)), 2, "Maine was disputed.")
reg("Canada (St Lawrence)", ["Lower Canada", "Province of Quebec (1763)", "Canada (New France core)", "Canada East"],
    I(A("Québec", "Canada"), PG([[-80.0, 44.5], [-64.0, 44.5], [-64.0, 50.5], [-80.0, 50.5]])), 2, "")
reg("Upper Canada", ["Canada West", "Ontario (southern)"], I(A("Ontario", "Canada"), PG([[-95.5, 41.5], [-74.0, 41.5], [-74.0, 47.5], [-85.0, 50.0], [-95.5, 50.0]])), 2, "")
reg("New France", ["Nouvelle-France"], U(R("Canada (St Lawrence)"), R("Acadia"), R("Illinois Country"), R("Great Lakes region")), 1, "")
reg("Newfoundland", ["Newfoundland (island)", "Terre-Neuve"], I(A("Newfoundland and Labrador", "Canada"), PG([[-60.0, 46.5], [-52.0, 46.5], [-52.0, 52.0], [-60.0, 52.0]])), 3, "")
reg("Labrador", [], M(A("Newfoundland and Labrador", "Canada"), R("Newfoundland")), 3, "")
reg("Maritimes", ["Maritime Provinces"], As("Canada", "Nova Scotia", "New Brunswick", "Prince Edward Island"), 3, "")
reg("Canadian Prairies", ["Prairie Provinces", "Prairies"], As("Canada", "Manitoba", "Saskatchewan", "Alberta"), 3, "")
reg("Greenland", ["Kalaallit Nunaat", "Norse Greenland (broad)"], C("Greenland"), 3, "")
reg("Vinland", ["L'Anse aux Meadows"], I(A("Newfoundland and Labrador", "Canada"), PG([[-56.5, 50.5], [-55.0, 50.5], [-55.0, 51.8], [-56.5, 51.8]])), 1, "")
reg("Hispaniola", ["Santo Domingo (island)", "Española", "Haiti (island)"], U(C("Haiti"), C("Dominican Rep.")), 3, "")
reg("Greater Antilles", [], U(C("Cuba"), C("Haiti"), C("Dominican Rep."), C("Jamaica"), C("Puerto Rico"), C("Cayman Is.")), 3, "")
reg("Lesser Antilles", ["Caribbees", "Windward and Leeward Islands"],
    U(C("Trinidad and Tobago"), C("Grenada"), C("St. Vin. and Gren."), C("Barbados"), C("Saint Lucia"), C("Dominica"), C("Montserrat"), C("Antigua and Barb."),
      C("St. Kitts and Nevis"), C("Anguilla"), C("British Virgin Is."), C("U.S. Virgin Is."), C("St-Martin"), C("Sint Maarten"), C("St-Barthélemy"),
      As("France", "Guadeloupe", "Martinique"), C("Aruba"), C("Curaçao")), 2, "")
reg("Bahamas (archipelago)", ["Lucayan archipelago", "Bahamas"], U(C("Bahamas"), C("Turks and Caicos Is.")), 3, "")
reg("Quito (region)", ["Audiencia of Quito (highlands)", "Ecuadorian Sierra", "Kingdom of Quito"],
    As("Ecuador", "Pichincha", "Imbabura", "Cotopaxi", "Tungurahua", "Chimborazo", "Azuay", "Cañar", "Loja", "Carchi", "Bolivar"), 2, "")
reg("New Granada (core)", ["Muisca country", "Bogota highlands", "Cundinamarca and Boyaca"], As("Colombia", "Cundinamarca", "Boyacá", "Santander", "Norte de Santander", "Tolima", "Huila", "Bogota"), 2, "")
reg("Antioquia", [], A("Antioquia", "Colombia"), 3, "")
reg("Darien", ["Darién", "Isthmus of Darien"], U(A("Darién", "Panama"), I(A("Chocó", "Colombia"), PG([[-78.0, 7.0], [-76.5, 7.0], [-76.5, 8.8], [-78.0, 8.8]]))), 2, "")
reg("Panama (isthmus)", ["Isthmus of Panama", "Castilla del Oro", "Panama"], C("Panama"), 3, "")
reg("Guianas", ["The Guianas", "Guayana", "Guiana"],
    U(C("Guyana"), C("Suriname"), A("Guyane française", "France"), As("Venezuela", "Delta Amacuro", "Bolívar"), I(C("Brazil"), PG([[-60.0, 1.0], [-50.0, 1.0], [-50.0, 5.5], [-60.0, 5.5]]))), 2, "")
reg("Llanos", ["Orinoco plains", "Los Llanos"], U(As("Venezuela", "Apure", "Barinas", "Guárico", "Portuguesa", "Cojedes", "Anzoátegui", "Monagas"), As("Colombia", "Arauca", "Casanare", "Meta", "Vichada")), 2, "")
reg("Amazonia", ["Amazon basin", "Amazon rainforest", "Amazonas (region)"],
    U(As("Brazil", "Amazonas", "Pará", "Acre", "Rondônia", "Roraima", "Amapá"), As("Peru", "Loreto", "Ucayali", "Madre de Dios"),
      As("Colombia", "Amazonas", "Caquetá", "Putumayo", "Guainía", "Vaupés", "Guaviare"),
      As("Ecuador", "Napo", "Orellana", "Pastaza", "Morona Santiago", "Sucumbios", "Zamora Chinchipe"), As("Bolivia", "Pando", "El Beni"), A("Amazonas", "Venezuela")), 2, "")
reg("Chimor", ["Chimu kingdom", "North coast of Peru", "Moche country"], As("Peru", "La Libertad", "Lambayeque", "Áncash", "Piura", "Tumbes"), 2, "")
reg("Cuzco region", ["Cusco region", "Inca heartland", "Cuzco (region)"], As("Peru", "Cusco", "Apurímac"), 2, "")
reg("Cuzco (100 km)", ["Cusco (100 km)", "Cuzco valley"], P("Cusco", 100, "Peru"), 3, "")
reg("Altiplano", ["Collao", "Qullasuyu (core)", "Titicaca basin (broad)", "Bolivian Altiplano"], U(As("Bolivia", "La Paz", "Oruro", "Potosí"), A("Puno", "Peru")), 2, "")
reg("Titicaca basin", ["Lake Titicaca region", "Collasuyo (north)"], U(A("Puno", "Peru"), A("La Paz", "Bolivia")), 2, "")
reg("Charcas", ["Upper Peru", "Audiencia of Charcas", "Alto Peru"], As("Bolivia", "Chuquisaca", "Potosí", "Oruro", "La Paz", "Cochabamba"), 2, "")
reg("Atacama", ["Atacama desert", "Litoral (Bolivian)", "Norte Grande"], U(As("Chile", "Antofagasta", "Atacama", "Tarapacá", "Arica y Parinacota"), I(A("Potosí", "Bolivia"), PG([[-69.7, -23.0], [-66.0, -23.0], [-66.0, -20.0], [-69.7, -20.0]]))), 2, "")
reg("Araucania", ["Araucanía", "Mapuche country", "Arauco", "Wallmapu (Chile)"], As("Chile", "La Araucanía", "Bío-Bío", "Los Ríos", "Los Lagos", "Ñuble"), 2, "")
reg("Central Chile", ["Chile (colonial core)", "Zona Central"], As("Chile", "Región Metropolitana de Santiago", "Valparaíso", "Libertador General Bernardo O'Higgins", "Maule", "Coquimbo"), 3, "")
reg("Patagonia", [], U(As("Argentina", "Neuquén", "Río Negro", "Chubut", "Santa Cruz", "Tierra del Fuego"), As("Chile", "Aisén del General Carlos Ibáñez del Campo", "Magallanes y Antártica Chilena")), 3, "")
reg("Tierra del Fuego", [], U(A("Tierra del Fuego", "Argentina"), I(A("Magallanes y Antártica Chilena", "Chile"), PG([[-75.0, -56.0], [-63.0, -56.0], [-63.0, -52.3], [-75.0, -52.3]]))), 3, "")
reg("Pampas", ["Pampa", "Rio de la Plata hinterland"], As("Argentina", "Buenos Aires", "Ciudad de Buenos Aires", "La Pampa", "Santa Fe", "Córdoba", "Entre Ríos"), 2, "")
reg("Gran Chaco", ["Chaco"], U(As("Argentina", "Chaco", "Formosa", "Santiago del Estero", "Salta"), As("Paraguay", "Boquerón", "Alto Paraguay", "Presidente Hayes"), As("Bolivia", "Santa Cruz", "Tarija")), 2, "")
reg("Banda Oriental", ["Cisplatina", "Uruguay (region)", "Provincia Oriental"], C("Uruguay"), 3, "")
reg("Jesuit Missions", ["Misiones (Jesuit)", "Guarani missions", "Misiones Orientales"], U(A("Misiones", "Argentina"), As("Paraguay", "Itapúa", "Misiones"), I(A("Rio Grande do Sul", "Brazil"), PG([[-56.5, -29.5], [-53.5, -29.5], [-53.5, -27.5], [-56.5, -27.5]]))), 2, "")
reg("Rio de la Plata (region)", ["Platine region", "Río de la Plata", "River Plate"], U(R("Pampas"), C("Uruguay"), C("Paraguay")), 2, "")
reg("Cuyo", [], As("Argentina", "Mendoza", "San Juan", "San Luis"), 3, "")
reg("Tucuman (colonial)", ["Gobernacion del Tucuman", "Tucumán (province, colonial)", "Argentine Northwest (broad)"], As("Argentina", "Tucumán", "Salta", "Jujuy", "Catamarca", "La Rioja", "Santiago del Estero", "Córdoba"), 2, "")
reg("Minas Gerais", [], A("Minas Gerais", "Brazil"), 3, "")
reg("Bahia", ["Captaincy of Bahia"], A("Bahia", "Brazil"), 3, "")
reg("Pernambuco (region)", ["Dutch Brazil (core)", "New Holland (Brazil)", "Pernambuco"], As("Brazil", "Pernambuco", "Paraíba", "Rio Grande do Norte", "Alagoas"), 2, "")
reg("Northeast Brazil", ["Nordeste"], As("Brazil", "Maranhão", "Piauí", "Ceará", "Rio Grande do Norte", "Paraíba", "Pernambuco", "Alagoas", "Sergipe", "Bahia"), 3, "")
reg("Sao Paulo (region)", ["São Paulo", "Paulista captaincy"], A("São Paulo", "Brazil"), 3, "")
reg("Southern Brazil", ["Sul (Brazil)", "Brazilian South"], As("Brazil", "Paraná", "Santa Catarina", "Rio Grande do Sul"), 3, "")
reg("Grao-Para", ["Grão-Pará", "State of Maranhão and Grão-Pará", "Maranhao and Para"], As("Brazil", "Pará", "Amazonas", "Amapá", "Roraima", "Maranhão"), 2, "")
reg("Mato Grosso (region)", ["Mato Grosso"], As("Brazil", "Mato Grosso", "Mato Grosso do Sul"), 3, "")

# ----------------------------------------------------------------------------
# Oceania
# ----------------------------------------------------------------------------
reg("Van Diemen's Land", ["Tasmania"], A("Tasmania", "Australia"), 3, "")
reg("Swan River Colony", ["Perth (region)", "Western Australia (settled core)"], P("Perth", 150, "Australia"), 2, "")
reg("North Island (NZ)", ["North Island", "Te Ika-a-Maui"], A("North Island", "New Zealand"), 3, "")
reg("South Island (NZ)", ["South Island", "Te Waipounamu"], A("South Island", "New Zealand"), 3, "")
reg("Tahiti", ["Society Islands (core)"], P("Papeete", 60), 3, "")
reg("Melanesia", [], U(C("Papua New Guinea"), C("Solomon Is."), C("Vanuatu"), C("Fiji"), C("New Caledonia")), 3, "")
reg("Polynesia", ["Polynesian triangle"], U(C("Samoa"), C("American Samoa"), C("Tonga"), C("Fr. Polynesia"), C("Cook Is."), C("Niue"), C("Tuvalu"), C("Wallis and Futuna Is."), C("Pitcairn Is."), A("Hawaii", USA), C("New Zealand")), 2, "")
reg("Micronesia (region)", ["Micronesia", "Caroline, Marshall, Mariana and Gilbert islands"], U(C("Micronesia"), C("Palau"), C("Marshall Is."), C("Kiribati"), C("Nauru"), C("Guam"), C("N. Mariana Is.")), 3, "")


def main():
    existing = {}
    if OUT.exists():
        with open(OUT, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    row = json.loads(line)
                    existing[row["name"]] = row
    mine = {r["name"]: r for r in REGIONS}
    if len(mine) != len(REGIONS):
        dup = [n for n in mine if sum(1 for r in REGIONS if r["name"] == n) > 1]
        print("duplicate names in regions_src.py: %s" % dup, file=sys.stderr)
        sys.exit(1)
    rows = list(REGIONS) + [r for n, r in existing.items() if n not in mine]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    tmp = OUT.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False, separators=(",", ":")))
            f.write("\n")
    os.replace(tmp, OUT)
    print("wrote %s: %d regions (%d from this file, %d kept from the previous file)" % (OUT, len(rows), len(REGIONS), len(rows) - len(REGIONS)))


if __name__ == "__main__":
    main()
