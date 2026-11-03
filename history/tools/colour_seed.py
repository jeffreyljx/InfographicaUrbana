"""Seed table for history/colours.json (EmpireMap). Data only; tools/colour.py `seed` turns it into the registry.

Every FIXED row is (slug, L, C, h, family, group, note) with the colour given in OKLCH
(L lightness 0..1, C chroma, h hue in degrees). The slug is the polities.csv slug
(tools/slug.py rule, with the -2 suffix where polities.csv disambiguates). `group`
names the state a Cliopatria row belongs to when several rows are one state (the
thirteen French regimes, the Delhi Sultanate's dynasties, the British colonial rows):
rows of one group share a colour and are never reported as a clash with each other.
`family` names the hue family in FAMILIES; a row whose hue sits outside its family's
range says why in its note.

Conventions followed (master-plan.md, Colours): Rome red, Byzantium purple, France blue,
England and Britain pink-red, Spain yellow-orange, Portugal green, the Ottomans olive,
Russia dark green, the Mongols warm brown, the Chinese dynasties a warm family (Han
vermilion, Tang gold, Song teal-green, Ming deep red, Qing imperial yellow).
"""

# Hue ranges are OKLCH degrees, [start, end]; end < start means the range wraps through 0.
FAMILIES = {
    "rome": {"hue": [300, 35], "note": "Rome red; Western Rome crimson-orange; Eastern Rome and Byzantium Tyrian purple, a red-purple so it sits beside Rome's red on the wheel; the Byzantine successor states lighter purples; the Latin Empire lilac; the Gallic Empire light orange"},
    "china": {"hue": [15, 110], "note": "the imperial sequence in warm hues: Shang bronze, Zhou ochre, Han vermilion, Sui orange, Tang gold, Ming deep red, Qing imperial yellow, PRC vermilion-red; the Song's teal-green (165) is the plan's choice, Qin slate and the ROC's blue are convention's"},
    "china-division": {"hue": [200, 340], "note": "the Three Kingdoms, Jin and the Southern dynasties in cool hues so the many coexisting states read apart; Shu Han is crimson because it claims the Han"},
    "steppe": {"hue": [200, 290], "note": "Xiongnu, Xianbei, Rouran, the Göktürks (sky blue, as the name says), Uyghurs, Khazars, Liao, Jin, Seljuks and Huns in slate blues and indigos; the Avars cyan, the Kazakhs turquoise"},
    "mongol": {"hue": [30, 130], "note": "warm browns and ochres: Mongol Empire brown, Yuan lighter brown, Golden Horde ochre-gold, Ilkhanate rust, Chagatai pale olive, Timurids terracotta, Crimea light orange-tan, Oirats light olive-green; the Blue and White Hordes by name"},
    "persia": {"hue": [170, 235], "note": "teals from Elam and the Medes to the Islamic Republic; the Parthians and Khwarezm green-teal"},
    "hellenistic": {"hue": [225, 280], "note": "Macedon and the Diadochi in blues, the Greek city-states and modern Greece Aegean light blue; the Ptolemies take Egypt's gold"},
    "caliphate": {"hue": [120, 165], "note": "Rashidun green, Umayyad pale green (the white banner), Abbasid dark grey-green (the black banner), Fatimid green, Córdoba pale green beside the Umayyads, Sokoto green"},
    "islam-west": {"hue": [10, 125], "note": "the Maghreb dynasties, the Egypt-Syria sultanates and the Ottomans in oranges, browns and olives: Almohad brown, Marinid brick, Morocco red, Almoravid yellow-olive, Ayyubid olive-yellow, Mamluk tan, Ottoman olive (moved from green because Russia is dark green), Turkey light olive; Saudi Arabia deep green (160) is the exception"},
    "britain": {"hue": [350, 15], "note": "England and Britain pink-red, the colonial rows a lighter pink; Scotland saltire blue and Ireland green are the exceptions"},
    "france": {"hue": [250, 275], "note": "France blue for every French regime, the colonial rows lighter blue, the Franks blue-violet; Burgundy wine (330), the Netherlands orange (50) and Belgium yellow (100) are the exceptions"},
    "germany": {"hue": [235, 305], "note": "Prussia and Germany slate-black (low chroma), Bavaria light blue, the Holy Roman Empire pale lilac, Switzerland violet, the German colonies grey-lilac; Saxony green is the exception"},
    "austria": {"hue": [0, 10], "note": "Habsburg Austria red-white-red"},
    "iberia": {"hue": [40, 80], "note": "Castile and Spain yellow-orange, Aragon orange"},
    "portugal": {"hue": [140, 155], "note": "Portugal green, the empire a lighter green"},
    "italy": {"hue": [145, 170], "note": "Italy green from Sardinia-Piedmont to the Republic; Venice terracotta (25), Genoa orange (30) and the Papal States yellow (95) by convention"},
    "nordic": {"hue": [235, 255], "note": "Sweden blue, Norway navy, Finland light blue; Denmark vermilion-orange (38) and its colonies' pale tint are the exceptions"},
    "russia": {"hue": [140, 160], "note": "Russia dark green from Moscow to the Federation, Kievan Rus lighter green; Novgorod pale rose (350) and the USSR deep red (25) by convention and by its neighbours"},
    "east-europe": {"hue": [270, 360], "note": "Poland rose, Hungary violet, Serbia indigo, Georgia violet; Lithuania turquoise-cyan (200), Czechoslovakia teal (185) and Ukraine yellow (95) are the exceptions"},
    "balkans": {"hue": [40, 75], "note": "Bulgaria tan-orange and the Second Empire deep orange-brown (the greens belong to Russia and the Ottoman olive); Greece light Aegean blue, Romania blue and Yugoslavia blue-indigo sit in the blues"},
    "india": {"hue": [280, 340], "note": "Maurya violet, Satavahana orchid, Chola deep violet, Rashtrakuta indigo, Pala and Vijayanagara magenta; Gupta terracotta, Kushan yellow-olive, Ghaznavid ochre; the Delhi Sultanate and the Mughals green (Islamic convention), Marathas saffron, Sikhs Khalsa navy, the Republic saffron, Pakistan and Bangladesh green"},
    "japan": {"hue": [340, 15], "note": "Japan deep crimson in every period (the lighter reds and pinks around it belong to the USSR, the PRC and the British colonies)"},
    "korea": {"hue": [160, 260], "note": "Goguryeo deep green-teal, Balhae light cyan, Goryeo green-teal, Joseon blue, the Republic blue, the DPRK dark blue; Baekje coral and Silla gold by the usual Korean map convention"},
    "southeast-asia": {"hue": [25, 120], "note": "Khmer brick, the Burmese kingdoms olive, Đại Việt yellow-olive, the Nguyễn yellow, Vietnam orange-gold, Majapahit and Indonesia red; Siam orchid (315), Ayutthaya rose (335) and Srivijaya sea blue (230) are the exceptions"},
    "americas": {"hue": [0, 360], "note": "national colours: USA navy-indigo, Canada red, Mexico green, Brazil green, Argentina light blue, Colombia blue, Venezuela light blue, Chile blue, Peru red; Inca terracotta, Aztec jade"},
    "pacific": {"hue": [130, 260], "note": "Australia green, New Zealand navy"},
    "africa": {"hue": [30, 120], "note": "the Sahel empires gold and ochre, Songhai red-brown, Kush ochre-brown, Axum olive, Ethiopia gold, South Africa gold; Bornu magenta (320) and Nigeria green (150) are the exceptions"},
    "egypt": {"hue": [75, 95], "note": "pharaonic Egypt sand gold, the Ptolemies lighter gold; modern Egypt burnt orange (50)"},
    "near-east": {"hue": [20, 100], "note": "Sumer clay ochre, Akkad and Assyria red-brown, Lydia gold, Armenia orange, Palmyra desert gold; Babylon blue (265), Hittites magenta-violet (320), Phoenicia Tyrian purple (335) and Carthage Punic purple-indigo (285), Israel blue (250) and Jerusalem pale rose (345) by convention"},
}

# The 24-hue wheel for polities without a fixed colour: hue every 15 degrees from 0, three
# lightness variants; chroma is clipped to the sRGB gamut per hue when the tool builds it.
WHEEL = {
    "hues": list(range(0, 360, 15)),
    "variants": {
        "light": {"L": 0.80, "C": 0.10, "use": "the densest regions: minor states of the Holy Roman Empire, the taifas, the Warring States, the Rus principalities"},
        "mid": {"L": 0.70, "C": 0.12, "use": "the default"},
        "deep": {"L": 0.58, "C": 0.13, "use": "large or isolated states"},
    },
    "note": "assign prefers the variant its crowding rule gives a polity and falls back to the others; a colour is never reused for two polities that touch in any anchor year when the wheel has room",
}

def _rows(slugs, L, C, h, family, group, note):
    return [(s, L, C, h, family, group, note) for s in slugs]

FIXED = []
F = FIXED.append

# ---- Rome and its successors ------------------------------------------------------------
FIXED += _rows(["roman-kingdom", "roman-republic", "roman-empire"], 0.58, 0.17, 25, "rome", "rome",
               "Rome red; Kingdom, Republic and Empire are one state")
F(("western-roman-empire", 0.56, 0.16, 18, "rome", None,
               "crimson-orange beside Rome's red: a successor that claims continuity"))
FIXED += _rows(["eastern-roman-empire", "byzantine-empire"], 0.48, 0.14, 340, "rome", "byzantium",
               "Byzantium purple: Tyrian, a red-purple, so it neighbours Rome's red on the wheel; the Eastern Roman and Byzantine rows are one state")
F(("nicaean-empire", 0.58, 0.12, 325, "rome", None, "claims Byzantine continuity: a lighter purple"))
F(("empire-of-trebizond", 0.74, 0.09, 330, "rome", None,
               "Byzantine successor: light red-purple"))
F(("despotate-of-epirus", 0.66, 0.10, 310, "rome", None, "Byzantine successor: light violet"))
F(("latin-empire", 0.68, 0.10, 285, "rome", None, "crusader Constantinople: lilac, at the far end of the family"))
F(("gallic-empire", 0.7, 0.12, 40, "rome", None,
               "Roman breakaway: light orange"))
F(("palmyrene-empire", 0.72, 0.12, 80, "near-east", None,
               "Palmyra desert gold"))
F(("kingdom-of-jerusalem", 0.80, 0.10, 110, "near-east", None, "pale gold-green: the crusader cross or on argent (moved off pale rose, which is Novgorod's in the same centuries, and kept greener than the Papal States' yellow)"))

# ---- China ----------------------------------------------------------------------------
F(("shang-dynasty", 0.52, 0.10, 62, "china", None, "bronze, darker and yellower than Assyria's red-brown of the same centuries"))
F(("zhou-dynasty", 0.64, 0.12, 70, "china", None, "ochre"))
FIXED += _rows(["qin", "qin-dynasty"], 0.42, 0.03, 250, "china", "qin",
               "Qin black (the water element's colour) lifted to slate so labels read; the state of Qin and the Qin dynasty are one state")
FIXED += _rows(["han-dynasty", "han-2", "xin-dynasty"], 0.60, 0.17, 30, "china", "han",
               "Han vermilion; Liu Bang's Kingdom of Han (Hán, slug han-2) and the Xin interregnum keep it, as Wu Zhou keeps the Tang's")
F(("shu-han", 0.55, 0.15, 15, "china", None, "claims the Han: crimson beside vermilion"))
FIXED += _rows(["cao-cao", "cao-wei"], 0.56, 0.11, 285, "china-division", "wei",
               "Wei blue-violet; Cao Cao's warlord state became the Wei")
F(("eastern-wu", 0.60, 0.11, 150, "china-division", None, "Wu green"))
F(("western-jin", 0.60, 0.10, 275, "china-division", None, "Jin indigo, continuing Wei's blue (the row runs through the Eastern Jin)"))
F(("liu-song-dynasty", 0.60, 0.10, 290, "china-division", None, "Southern dynasties: a chain of purples"))
F(("southern-qi", 0.62, 0.10, 305, "china-division", None, "Southern dynasties: a chain of purples"))
F(("liang-dynasty", 0.62, 0.10, 320, "china-division", None, "Southern dynasties: a chain of purples"))
F(("chen-dynasty", 0.62, 0.10, 335, "china-division", None, "Southern dynasties: a chain of purples"))
F(("northern-wei", 0.62, 0.10, 205, "china-division", None, "Tuoba Wei: cyan, the steppe end of the division hues"))
F(("sui-dynasty", 0.62, 0.15, 72, "china", None, "orange-gold, before the Tang's gold (Armenia holds the lighter orange in the same decades)"))
F(("tang-dynasty", 0.76, 0.15, 90, "china", None, "Tang gold"))
F(("later-tang", 0.70, 0.13, 80, "china", None, "claims the Tang: a deeper gold"))
FIXED += _rows(["northern-song", "southern-song"], 0.62, 0.11, 165, "china", "song",
               "Song teal-green (the plan's choice, outside the warm range); Northern and Southern Song are one state")
F(("liao-dynasty", 0.58, 0.09, 265, "steppe", None, "Khitan Liao slate blue"))
F(("kara-khitans", 0.66, 0.08, 250, "steppe", None, "the Liao's successor in Central Asia: lighter slate blue"))
F(("western-xia", 0.70, 0.09, 75, "china", None, "Tangut Xia tan"))
F(("great-jin", 0.55, 0.11, 235, "steppe", None,
               "Jurchen Jin steel blue"))
FIXED += _rows(["ming-dynasty", "southern-ming"], 0.48, 0.15, 22, "china", "ming", "Ming deep red")
FIXED += _rows(["later-jin-dynasty", "qing-dynasty"], 0.82, 0.15, 95, "china", "qing",
               "Qing imperial yellow; the Manchu Later Jin was renamed Qing in 1636, one state")
FIXED += _rows(["yuan-dynasty", "northern-yuan", "mongol-khanate"], 0.56, 0.10, 65, "mongol", "yuan",
               "Yuan: a lighter Mongol brown beside the Mongol Empire's; the Northern Yuan and Mongol Khanate rows continue it")
FIXED += _rows(["republic-of-china", "empire-of-china"], 0.50, 0.13, 255, "china", "roc",
               "ROC blue (the blue sky of the flag); Yuan Shikai's 1916 empire is the same state")
F(("kuomintang", 0.5, 0.13, 255, "china", "roc",
               "the Kuomintang government of 1917-1929: the same state's blue"))
F(("people-s-republic-of-china", 0.58, 0.20, 32, "china", "prc", "PRC vermilion-red; the USSR is a deeper red, told apart by lightness (distance 0.13)"))
FIXED += _rows(["communist-party-of-china", "chinese-communists"], 0.58, 0.2, 32, "china", "prc",
               "the rebels who founded the PRC take its colour")

# ---- Mongols and the steppe --------------------------------------------------------------
F(("mongol-empire", 0.50, 0.10, 50, "mongol", None, "Mongol warm brown"))
F(("golden-horde", 0.68, 0.13, 80, "mongol", None, "ochre-gold, by name"))
F(("blue-horde", 0.50, 0.09, 240, "mongol", None, "deep slate blue, by name (Sweden and Joseon hold the mid blues of the same centuries)"))
F(("white-horde", 0.76, 0.08, 90, "mongol", None,
               "pale straw, by name"))
F(("ilkhanate", 0.58, 0.11, 38, "mongol", None, "rust"))
F(("chagatai-khanate", 0.76, 0.07, 110, "mongol", None,
               "pale olive"))
F(("timurid-empire", 0.62, 0.11, 18, "mongol", None, "terracotta, lighter than the Ming's red next door"))
FIXED += _rows(["four-oirats", "oirat-confederation", "dzungar-khanate"], 0.7, 0.09, 130, "mongol", "oirat",
               "Oirat light olive-green")
F(("crimean-khanate", 0.76, 0.1, 45, "mongol", None,
               "light orange-tan, kept off the Golden Horde's ochre and Poland's rose"))
F(("kazakh-khanate", 0.64, 0.10, 200, "steppe", None, "turquoise, the Kazakh colour"))
F(("kazakhstan", 0.58, 0.12, 205, "steppe", None, "turquoise, the flag"))
F(("xiongnu", 0.55, 0.09, 258, "steppe", None,
               "slate blue"))
F(("xianbei", 0.64, 0.08, 220, "steppe", None, "light slate"))
F(("rouran-khaganate", 0.52, 0.09, 300, "steppe", None, "deep purple (the Liu Song hold the lighter one in the same decades)"))
F(("gokturk-khaganate", 0.70, 0.11, 235, "steppe", None, "sky blue: Gök means sky-blue"))
F(("eastern-gokturks", 0.60, 0.10, 225, "steppe", None, "a deeper sky blue"))
F(("western-gokturks", 0.74, 0.09, 250, "steppe", None, "a lighter sky blue"))
F(("uyghur-khaganate", 0.68, 0.09, 215, "steppe", None, "light steel blue"))
F(("khazaria", 0.62, 0.09, 265, "steppe", None, "slate indigo"))
FIXED += _rows(["huns", "hunnic-empire"], 0.50, 0.10, 265, "steppe", "huns", "deep indigo-blue, kept off Western Rome's crimson, Byzantium's purple and Cao Wei's indigo")
F(("white-huns", 0.76, 0.07, 300, "steppe", None,
               "pale violet, by name"))
F(("avar-khaganate", 0.62, 0.10, 212, "steppe", None,
               "cyan, kept off the Franks' blue-violet, the Huns' indigo and Lombard Italy's green"))
FIXED += _rows(["great-seljuk-empire", "seljuk-dynasty"], 0.60, 0.10, 245, "steppe", "seljuk", "Seljuk blue (the Turkic sky-blue family)")
F(("sultanate-of-rum", 0.70, 0.08, 250, "steppe", None, "the Seljuks of Rum: lighter blue"))
F(("kushan-empire", 0.62, 0.12, 100, "india", None, "yellow-olive (a Yuezhi state, outside the India range)"))

# ---- Persia ---------------------------------------------------------------------------
F(("elam", 0.54, 0.08, 170, "persia", None,
               "deep green-teal"))
F(("median-kingdom", 0.66, 0.10, 185, "persia", None, "light teal"))
F(("achaemenid-empire", 0.55, 0.11, 200, "persia", None, "Achaemenid teal"))
F(("parthian-empire", 0.62, 0.1, 178, "persia", None,
               "green-teal"))
F(("sasanian-empire", 0.50, 0.12, 195, "persia", None, "deep teal"))
F(("safavid-dynasty", 0.60, 0.12, 205, "persia", None, "teal"))
F(("afsharid-iran", 0.5, 0.1, 230, "persia", None,
               "blue-teal"))
F(("zand-dynasty", 0.68, 0.09, 175, "persia", None,
               "pale green-teal"))
F(("qajar-dynasty", 0.55, 0.11, 215, "persia", None,
               "blue-teal"))
F(("pahlavi-dynasty", 0.60, 0.10, 192, "persia", None, "teal"))
F(("islamic-republic-of-iran", 0.52, 0.12, 195, "persia", None,
               "deep teal (moved off the flag's green: Pakistan is green)"))
FIXED += _rows(["khwarezmid-dynasty", "khwarezmid-empire"], 0.6, 0.11, 175, "persia", "khwarezm",
               "Khwarezm green-teal")

# ---- The Greek world -------------------------------------------------------------------
F(("mycenaean-greece", 0.70, 0.08, 230, "hellenistic", None, "pale Aegean blue"))
F(("greek-city-states", 0.78, 0.09, 230, "hellenistic", None,
               "Aegean light blue"))
FIXED += _rows(["macedonian-empire", "antigonid-macedonia"], 0.55, 0.12, 255, "hellenistic", "macedon", "Macedonian blue; the Antigonid row is the same kingdom")
F(("seleucid-empire", 0.66, 0.09, 240, "hellenistic", None,
               "light blue"))
F(("greco-bactrian-kingdom", 0.75, 0.08, 275, "hellenistic", None, "pale blue-violet"))
F(("indo-greeks", 0.72, 0.08, 290, "hellenistic", None, "pale violet"))
F(("ptolemaic-kingdom", 0.74, 0.12, 95, "egypt", None, "Hellenistic Egypt keeps Egypt's gold, lighter"))
FIXED += _rows(["first-hellenic-republic", "kingdom-of-greece", "third-hellenic-republic"], 0.68, 0.10, 230, "hellenistic", "greece",
               "Greece light Aegean blue (every modern Greek regime)")

# ---- Caliphates and the Islamic world -------------------------------------------------------
F(("rashidun-caliphate", 0.62, 0.12, 140, "caliphate", None, "green"))
F(("umayyad-caliphate", 0.76, 0.09, 130, "caliphate", None,
               "pale green: the Umayyad white banner"))
FIXED += _rows(["abbasid-caliphate", "abbasid-caliphate-buyid-dynasty"], 0.42, 0.07, 160, "caliphate", "abbasid",
               "dark grey-green: the Abbasid black banner lifted so labels read")
F(("fatimid-caliphate", 0.58, 0.13, 148, "caliphate", None,
               "Fatimid green"))
FIXED += _rows(["emirate-of-cordoba", "caliphate-of-cordoba"], 0.78, 0.1, 120, "caliphate", "cordoba",
               "Umayyad Córdoba, a pale green beside the Umayyad hue; emirate and caliphate are one state")
F(("sokoto-caliphate", 0.60, 0.10, 150, "caliphate", None, "green"))
F(("almoravid-dynasty", 0.66, 0.11, 105, "islam-west", None,
               "yellow-olive, kept off Portugal's and the Fatimids' greens"))
F(("almohad-caliphate", 0.52, 0.10, 50, "islam-west", None, "brown (moved from green: Portugal and Castile are its neighbours)"))
F(("marinid-sultanate", 0.50, 0.12, 35, "islam-west", None, "dark brick (Majapahit holds the lighter red in the same centuries)"))
F(("saadi-sultanate", 0.62, 0.12, 15, "islam-west", None, "light brick"))
F(("morocco", 0.50, 0.15, 25, "islam-west", None, "Alaouite Morocco: flag red"))
F(("ayyubid-sultanate", 0.62, 0.10, 100, "islam-west", None, "Saladin's yellow banner: olive-yellow"))
F(("mamluk-sultanate", 0.70, 0.09, 60, "islam-west", None, "tan"))
FIXED += _rows(["ottoman-empire", "ottoman-tripolitania"], 0.55, 0.10, 115, "islam-west", "ottoman",
               "Ottoman olive: moved from green because Russia is dark green and they are neighbours")
F(("republic-of-turkey", 0.66, 0.1, 115, "islam-west", None,
               "light olive beside the Ottoman olive (the flag's red would clash with the USSR's)"))
FIXED += _rows(["emirate-of-diriyah", "emirate-of-nejd", "kingdom-of-hejaz-and-nejd", "kingdom-of-saudi-arabia"], 0.42, 0.11, 160, "islam-west", "saudi",
               "Saudi green, deep and bluish so the Ottoman olive stays apart: the three Saudi states")
F(("state-of-israel", 0.54, 0.11, 232, "near-east", None, "flag blue, a deeper sky-blue (Romania holds the mid blue at 250)"))
F(("kingdom-of-israel", 0.66, 0.09, 250, "near-east", None, "blue, lighter than the modern state's"))

# ---- Britain and its empire ------------------------------------------------------------
F(("anglo-saxon-england", 0.72, 0.10, 5, "britain", None, "pale pink-red"))
F(("kingdom-of-wessex", 0.68, 0.12, 8, "britain", None, "Wessex, the kingdom that became England: lighter pink-red"))
F(("kingdom-of-england", 0.7, 0.14, 355, "britain", None,
               "England pink-red, light enough to stand apart from Habsburg red across the Calais border"))
F(("kingdom-of-great-britain", 0.58, 0.16, 0, "britain", None, "Great Britain and the United Kingdom (one Cliopatria row to 2024): deeper pink-red"))
FIXED += _rows(["british-empire", "british-colonial-empire", "british-raj", "british-africa", "british-east-africa", "british-gold-coast",
                "british-cape-colony", "british-ceylon", "british-overseas-territories"], 0.70, 0.12, 3, "britain", "british-empire",
               "the empire's lighter pink for every colonial row")
F(("kingdom-of-scotland", 0.62, 0.10, 255, "britain", None, "saltire blue"))
FIXED += _rows(["irish-free-state", "eire"], 0.62, 0.13, 145, "britain", "ireland", "Ireland green")
F(("canada", 0.55, 0.16, 28, "americas", None,
               "flag red, deeper than the empire's pink in Newfoundland"))
F(("commonwealth-of-australia", 0.62, 0.10, 140, "pacific", None, "green (gold would clash with the Dutch East Indies' orange on New Guinea)"))
F(("new-zealand", 0.50, 0.10, 255, "pacific", None, "flag navy"))
F(("south-africa", 0.62, 0.11, 70, "africa", None, "gold"))

# ---- France -----------------------------------------------------------------------------
FIXED += _rows(["kingdom-of-france", "french-first-republic", "french-directory", "french-consulate", "first-french-empire",
                "bourbon-kingdom-of-france", "french-second-republic", "second-french-empire", "french-third-republic", "free-french",
                "french-fourth-republic", "french-fifth-republic"], 0.55, 0.14, 260, "france", "france",
               "France blue for every French regime: one state since 990")
F(("vichy-france", 0.68, 0.09, 260, "france", "france", "the collaborationist regime: a paler France blue; the Free French keep the full blue"))
FIXED += _rows(["french-africa", "french-indochina", "french-algeria", "french-india", "french-louisiana", "french-colony-of-guiana",
                "french-mandate-for-syria-and-lebanon", "first-french-colonial-empire", "new-france", "france-antarctique"], 0.68, 0.11, 258, "france", "france-empire",
               "the French colonial rows: a lighter France blue")
F(("west-franks", 0.56, 0.1, 255, "france", None,
               "West Francia, France's predecessor"))
FIXED += _rows(["kingdom-of-the-franks", "merovingian-empire", "carolingian-empire"], 0.60, 0.11, 272, "france", "franks",
               "the Frankish kingdom blue-violet; the Merovingian and Carolingian rows are the same realm")
F(("duchy-of-burgundy", 0.50, 0.12, 330, "france", None, "Burgundy wine"))
FIXED += _rows(["kingdom-of-belgium", "belgian-congo"], 0.72, 0.13, 100, "france", "belgium", "Belgium yellow (black-yellow-red); the Congo row is the same state's colony")

# ---- Germany, Austria, the Low Countries, Switzerland ------------------------------------------
FIXED += _rows(["east-franks", "kingdom-of-germany", "holy-roman-empire"], 0.74, 0.07, 300, "germany", "hre",
               "pale lilac; East Francia, the Kingdom of Germany and the Empire are one realm (an association after 1648, per the standard)")
FIXED += _rows(["duchy-of-prussia", "brandenburg-prussia", "kingdom-of-prussia"], 0.45, 0.03, 250, "germany", "prussia", "Prussian black lifted to slate")
FIXED += _rows(["north-german-confederation", "german-empire", "weimar-republic", "nazi-germany", "federal-republic-of-germany",
                "federated-republic-of-germany"], 0.40, 0.03, 250, "germany", "germany",
               "Germany charcoal-slate (the flag's black); one state from 1867 to 2024")
F(("german-democratic-republic", 0.64, 0.03, 270, "germany", None,
               "light grey"))
F(("german-africa", 0.56, 0.04, 300, "germany", "germany-empire",
               "the German colonial rows: grey-lilac"))
FIXED += _rows(["duchy-of-bavaria", "kingdom-of-bavaria"], 0.66, 0.09, 235, "germany", "bavaria", "Bavarian light blue")
FIXED += _rows(["electorate-of-saxony", "kingdom-of-saxony"], 0.58, 0.10, 150, "germany", "saxony", "Saxony green")
FIXED += _rows(["house-of-habsburg", "habsburg-monarchy", "austrian-empire", "austria-hungary", "republic-of-austria", "second-republic-of-austria"],
               0.56, 0.17, 0, "austria", "austria",
               "Austria red-white-red, from the Habsburg lands to the Second Republic")
F(("swiss-confederation", 0.6, 0.13, 305, "germany", None,
               "violet: the flag's red belongs to Austria and Venice next door"))
FIXED += _rows(["dutch-republic", "batavian-republic", "napoleonic-batavia-republic", "sovereign-principality-of-the-united-netherlands", "netherlands",
                "dutch-east-indies", "dutch-cape-colony", "dutch-ceylon", "dutch-gold-coast", "new-netherland", "netherlands-antilles"],
               0.60, 0.16, 50, "france", "netherlands", "Netherlands orange, deeper than Spain's yellow-orange; the colonial rows share it")

# ---- Italy ------------------------------------------------------------------------------
FIXED += _rows(["kingdom-of-sardinia", "kingdom-of-italy", "republic-of-italy", "italian-africa"], 0.6, 0.14, 162, "italy", "italy",
               "Italy green, bluer than the olives of the Ottomans and Turkey and lighter than Russia's; Sardinia-Piedmont became Italy (the Kingdom of Italy row 587..1946 merges Lombard, Carolingian, Napoleonic and Savoyard Italy and needs splitting)")
F(("republic-of-venice", 0.66, 0.1, 25, "italy", None,
               "Venetian red lightened to terracotta so Austria's red stays apart"))
F(("republic-of-genoa", 0.64, 0.11, 30, "italy", None,
               "Genoa's red cross, lightened to orange so Spanish Milan, Austria and the Horde at Caffa stay apart"))
F(("papal-states", 0.8, 0.11, 95, "italy", None,
               "papal yellow (white and gold); the Empire's lilac is next door"))

# ---- Scandinavia ------------------------------------------------------------------------
FIXED += _rows(["greenland", "danish-gold-coast", "danish-india"], 0.76, 0.08, 55, "nordic", "denmark-empire",
               "the Danish colonial rows: a pale Dannebrog tint turned to apricot (the Gold Coast forts sit between Dutch orange and British pink)")
FIXED += _rows(["kingdom-of-denmark", "kalmar-union", "norway-denmark", "denmark-norway", "denmark"], 0.62, 0.16, 38, "nordic", "denmark",
               "Dannebrog red warmed to vermilion-orange so Austria's and Britain's reds stay apart; the Kalmar Union and the unions with Norway were Danish-led")
FIXED += _rows(["kingdom-of-sweden", "swedish-empire", "united-kingdoms-of-sweden-and-norway"], 0.58, 0.11, 240, "nordic", "sweden", "Sweden blue")
FIXED += _rows(["old-kingdom-of-norway", "kingdom-of-norway"], 0.45, 0.12, 250, "nordic", "norway", "Norway navy")
F(("republic-of-finland", 0.75, 0.08, 240, "nordic", None, "light blue"))

# ---- Russia and eastern Europe -------------------------------------------------------------
FIXED += _rows(["grand-principality-of-moscow", "tsardom-of-russia", "russian-empire", "russian-republic", "russian-federation"], 0.45, 0.10, 150, "russia", "russia",
               "Russia dark green, from Moscow to the Federation")
FIXED += _rows(["kievan-rus", "rus"], 0.62, 0.10, 150, "russia", "rus", "Kievan Rus: a lighter green")
F(("novgorod-republic", 0.76, 0.09, 350, "russia", None,
               "pale rose (the greens are the Rus's, the blues Sweden's, the ochres the Horde's)"))
FIXED += _rows(["republics-of-the-soviet-union", "union-of-soviet-socialist-republics"], 0.42, 0.15, 25, "russia", "ussr",
               "USSR deep red")
F(("ukraine", 0.75, 0.13, 95, "east-europe", None, "flag yellow"))
FIXED += _rows(["kingdom-of-poland", "polish-lithuanian-commonwealth", "republic-of-poland"], 0.66, 0.13, 350, "east-europe", "poland", "Poland rose (red and white), a shade deeper than England's pink")
F(("grand-duchy-of-lithuania", 0.7, 0.11, 200, "east-europe", None,
               "turquoise-cyan (the violets are Hungary's and Poland's, the blues the Horde's and Sweden's)"))
FIXED += _rows(["principality-of-hungary", "kingdom-of-hungary", "hungarian-republic", "hungarian-people-s-republic", "hungary"], 0.6, 0.11, 310, "east-europe", "hungary",
               "Hungary violet (the flag's green and red both collide with neighbours)")
F(("czechoslovakia", 0.62, 0.10, 185, "east-europe", None, "teal"))
FIXED += _rows(["united-principalities-of-moldavia-and-wallachia", "kingdom-of-romania", "socialist-republic-of-romania", "romania"], 0.60, 0.10, 250, "balkans", "romania",
               "Romania blue")
FIXED += _rows(["yugoslavia", "socialist-federal-republic-of-yugoslavia"], 0.5, 0.12, 270, "balkans", "yugoslavia",
               "Yugoslavia blue-indigo")
FIXED += _rows(["grand-principality-of-serbia", "kingdom-of-serbia", "serbian-empire", "serbs", "serbia", "serbia-montenegro", "republic-of-serbia"], 0.48, 0.11, 275, "east-europe", "serbia",
               "Serbia indigo")
F(("first-bulgarian-empire", 0.66, 0.12, 65, "balkans", None, "tan-orange: the greens belong to Russia and the Ottoman olive"))
F(("second-bulgarian-empire", 0.58, 0.13, 45, "balkans", None,
               "deep orange-brown, kept off the Golden Horde's ochre"))
FIXED += _rows(["principality-of-bulgaria", "kingdom-of-bulgaria", "people-s-republic-of-bulgaria", "republic-of-bulgaria"], 0.62, 0.12, 60, "balkans", "bulgaria",
               "modern Bulgaria: orange-tan")
F(("kingdom-of-georgia", 0.52, 0.12, 295, "east-europe", None,
               "violet (the flag's crimson is Timur's and Byzantium's)"))
F(("kingdom-of-armenia", 0.66, 0.13, 55, "near-east", None, "orange (the flag), kept off Rome's red"))

# ---- India ------------------------------------------------------------------------------
F(("maurya-empire", 0.55, 0.10, 300, "india", None, "violet"))
F(("satavahana-dynasty", 0.65, 0.10, 310, "india", None, "orchid"))
F(("gupta-empire", 0.65, 0.13, 35, "india", None, "terracotta"))
F(("pala-empire", 0.60, 0.11, 335, "india", None, "magenta"))
F(("rashtrakuta-dynasty", 0.68, 0.09, 275, "india", None, "light indigo (the Franks hold the mid one in the same centuries)"))
F(("chola-empire", 0.50, 0.12, 290, "india", None, "deep violet"))
F(("vijayanagara-empire", 0.55, 0.12, 320, "india", None, "magenta-purple"))
F(("ghaznavid-empire", 0.58, 0.11, 80, "india", None, "ochre"))
FIXED += _rows(["mamluk-dynasty", "khalji-dynasty", "tughlaq-dynasty", "lodi-dynasty"], 0.55, 0.10, 140, "india", "delhi",
               "Delhi Sultanate green: five dynasties, one state")
F(("sur-empire", 0.66, 0.10, 130, "india", None, "the Sur interruption of the Mughals: lighter green"))
F(("mughal-empire", 0.48, 0.11, 135, "india", None, "Mughal green, deeper than the Portuguese Empire's"))
F(("maratha-empire", 0.65, 0.15, 55, "india", None, "saffron"))
FIXED += _rows(["sikh-confederacy", "sikh-empire"], 0.45, 0.1, 265, "india", "sikh",
               "Khalsa navy blue (the yellow is the Qing's)")
F(("republic-of-india", 0.75, 0.14, 55, "india", None, "saffron"))
F(("islamic-republic-of-pakistan", 0.45, 0.12, 150, "india", None,
               "flag green"))
F(("people-s-republic-of-bangladesh", 0.55, 0.12, 160, "india", None, "flag green, lighter and bluer than Pakistan's"))

# ---- Japan and Korea -----------------------------------------------------------------------
FIXED += _rows(["asuka-japan", "nara-japan", "heian-japan", "kamakura-shogunate", "ashikaga-shogunate", "warring-states-japan", "tokugawa-shogunate",
                "empire-of-japan", "japan"], 0.46, 0.15, 345, "japan", "japan",
               "Japan deep crimson: the rising sun's red darkened because the USSR, the PRC, Austria's Tianjin concession and the British colonies hold the lighter reds and pinks around it")
F(("goguryeo", 0.52, 0.11, 160, "korea", None,
               "deep green-teal"))
F(("baekje", 0.66, 0.12, 25, "korea", None,
               "coral"))
FIXED += _rows(["silla", "unified-silla"], 0.62, 0.13, 95, "korea", "silla", "Silla gold")
F(("balhae", 0.74, 0.09, 210, "korea", None,
               "light cyan, kept off the Liao's slate and Goryeo's green-teal"))
F(("goryeo", 0.66, 0.11, 160, "korea", None, "green-teal, kept off the Jurchen Jin's steel blue"))
FIXED += _rows(["joseon", "korean-empire"], 0.52, 0.10, 268, "korea", "joseon", "Joseon blue, deeper and more violet than Sweden's")
F(("republic-of-korea", 0.62, 0.13, 248, "korea", None, "flag blue, lighter than France's"))
F(("democratic-people-s-republic-of-korea", 0.42, 0.10, 250, "korea", None, "dark blue (the flag's red would clash with the PRC's)"))

# ---- South-east Asia -----------------------------------------------------------------------
F(("khmer-empire", 0.60, 0.13, 35, "southeast-asia", None, "Angkor brick"))
F(("ayutthaya-kingdom", 0.64, 0.11, 335, "southeast-asia", None, "rose, beside Siam's orchid"))
FIXED += _rows(["rattanakosin-kingdom", "kingdom-of-thailand"], 0.62, 0.12, 315, "southeast-asia", "siam",
               "Siam orchid (the flag's blue is France's, next door in Indochina); Rattanakosin and Thailand are one state")
F(("pagan-kingdom", 0.64, 0.11, 118, "southeast-asia", None,
               "olive"))
F(("first-toungoo-empire", 0.68, 0.11, 100, "southeast-asia", None, "light olive-yellow"))
F(("konbaung-dynasty", 0.54, 0.12, 120, "southeast-asia", None, "deep olive"))
FIXED += _rows(["le-dynasty", "ai-viet"], 0.60, 0.11, 115, "southeast-asia", "dai-viet", "Đại Việt (slug ai-viet by the slug rule) yellow-olive; the Lê row is the same state")
F(("nguyen-dynasty", 0.70, 0.14, 80, "southeast-asia", None, "Nguyễn imperial yellow, deeper than the Qing's"))
FIXED += _rows(["democratic-republic-of-vietnam", "socialist-republic-of-vietnam"], 0.64, 0.15, 65, "southeast-asia", "vietnam",
               "Vietnam orange-gold: the flag's red is the PRC's next door, so the star's yellow leads")
F(("republic-of-vietnam", 0.76, 0.14, 95, "southeast-asia", None, "South Vietnam: the flag's yellow"))
F(("srivijaya", 0.62, 0.10, 230, "southeast-asia", None, "sea blue"))
F(("majapahit", 0.55, 0.14, 25, "southeast-asia", None, "red (the red-white banner)"))
F(("republic-of-indonesia", 0.52, 0.16, 15, "southeast-asia", None,
               "flag red, deeper than the Dutch orange it replaced"))

# ---- The Americas --------------------------------------------------------------------------
F(("united-states-of-america", 0.4, 0.13, 285, "americas", None,
               "navy-indigo, dark enough to stand apart from France's blue in Louisiana and Germany's charcoal in the Rhineland"))
F(("confederate-states-of-america", 0.60, 0.03, 250, "americas", None, "Confederate grey"))
FIXED += _rows(["first-mexican-empire", "federated-republic-of-mexico", "centralist-mexico", "second-mexican-empire", "mexico"], 0.58, 0.13, 135, "americas", "mexico",
               "Mexico green, lighter than Russian America's dark green")
F(("aztec-triple-alliance", 0.50, 0.10, 160, "americas", None, "jade"))
F(("inca-empire", 0.52, 0.12, 20, "americas", None, "terracotta (gold would clash with the Spanish Empire's yellow-orange)"))
FIXED += _rows(["empire-of-brazil", "brazilian-republic", "unitary-state-of-brazil", "federated-republic-of-brazil", "republic-of-brazil"], 0.50, 0.14, 135, "americas", "brazil",
               "Brazil green, deeper than the Portuguese Empire's")
FIXED += _rows(["gran-colombia", "new-granada", "republic-of-new-granada", "granadine-confederation", "united-states-of-colombia", "republic-of-colombia"],
               0.52, 0.12, 252, "americas", "colombia",
               "Colombia blue (the flag's yellow is squeezed between the Spanish Empire's yellow-orange and Portuguese Brazil's green in 1820)")
FIXED += _rows(["rio-de-la-plata", "argentine-confederation", "argentine-republic"], 0.78, 0.08, 230, "americas", "argentina", "Argentine light blue")
F(("republic-of-chile", 0.46, 0.12, 262, "americas", None,
               "deep blue"))
F(("republic-of-peru", 0.58, 0.15, 15, "americas", None, "red"))
FIXED += _rows(["republic-of-venezuela", "venezuela"], 0.66, 0.11, 245, "americas", "venezuela",
               "light blue")
FIXED += _rows(["kingdom-of-spain", "spanish-empire", "iberian-union", "first-spanish-republic", "second-spanish-republic", "francoist-spain", "spanish-nationalists"],
               0.72, 0.15, 70, "iberia", "spain", "Spain yellow-orange (the Iberian Union row is the Spanish crown's)")
FIXED += _rows(["kingdom-of-castile", "crown-of-castile"], 0.78, 0.15, 75, "iberia", "castile",
               "Castile, Spain's predecessor: the same yellow-orange, lighter")
FIXED += _rows(["kingdom-of-aragon", "crown-of-aragon"], 0.66, 0.15, 48, "iberia", "aragon",
               "Aragon orange")
FIXED += _rows(["county-of-portugal", "kingdom-of-portugal", "portuguese-republic", "estado-novo", "portugal"], 0.55, 0.12, 145, "portugal", "portugal", "Portugal green")
FIXED += _rows(["portuguese-empire", "portuguese-colonies", "portuguese-africa", "portuguese-ceylon"], 0.64, 0.12, 150, "portugal", "portugal-empire", "the Portuguese colonial rows: lighter green")

# ---- Africa ------------------------------------------------------------------------------
F(("kingdom-of-kush", 0.54, 0.12, 80, "africa", None,
               "ochre-brown"))
F(("kingdom-of-axum", 0.66, 0.1, 110, "africa", None,
               "olive"))
FIXED += _rows(["ethiopian-empire", "ethiopia"], 0.72, 0.15, 88, "africa", "ethiopia",
               "Ethiopia gold, warmer than Belgium's yellow")
F(("ghana-empire", 0.64, 0.13, 60, "africa", None, "gold, the land of gold"))
F(("mali-empire", 0.60, 0.14, 85, "africa", None, "gold"))
F(("songhai-empire", 0.48, 0.13, 45, "africa", None, "dark red-brown, kept off Mali's gold and apart from the Inca terracotta"))
F(("bornu-empire", 0.58, 0.11, 320, "africa", None, "magenta (the greens and blues around it are taken)"))
F(("ashanti-empire", 0.66, 0.14, 90, "africa", None, "gold, the Golden Stool"))
F(("federal-republic-of-nigeria", 0.60, 0.12, 150, "africa", None, "flag green"))
FIXED += _rows(["early-dynastic-period-of-egypt", "old-kingdom-of-egypt", "middle-kingdom-of-egypt", "new-kingdom-of-egypt", "twenty-second-dynasty-of-egypt",
                "twenty-sixth-dynasty-of-egypt", "thirtieth-dynasty-of-egypt"], 0.70, 0.12, 82, "egypt", "egypt-pharaonic",
               "pharaonic Egypt sand gold: one state for three thousand years")
FIXED += _rows(["muhammad-ali-dynasty", "khedivate-of-egypt", "kingdom-of-egypt", "republic-of-egypt", "united-arab-republic", "arab-republic-of-egypt"],
               0.52, 0.13, 55, "egypt", "egypt-modern",
               "modern Egypt burnt orange")
F(("carthage", 0.5, 0.12, 285, "near-east", None,
               "Punic purple-indigo, beside Phoenicia's Tyrian purple"))
FIXED += _rows(["phoenicia", "phoenician-colonies"], 0.55, 0.12, 335, "near-east", "phoenicia", "Tyrian purple, the Phoenicians' own dye")

# ---- The ancient Near East ------------------------------------------------------------------
F(("sumerian-city-states", 0.66, 0.11, 70, "near-east", None, "clay ochre"))
F(("akkadian-empire", 0.55, 0.13, 30, "near-east", None, "red-brown"))
F(("babylonia", 0.60, 0.11, 270, "near-east", None, "Babylon blue (the Ishtar Gate)"))
F(("neo-babylonian-empire", 0.52, 0.12, 272, "near-east", None,
               "deeper Babylon blue"))
F(("assyria", 0.56, 0.12, 42, "near-east", None,
               "Assyria red-brown"))
FIXED += _rows(["neo-assyrian-empire", "assyrian-egypt"], 0.48, 0.14, 30, "near-east", "neo-assyria", "deeper red-brown")
F(("hittites", 0.66, 0.1, 320, "near-east", None,
               "magenta-violet (the warm hues are Egypt's and Assyria's, the blue is Babylon's)"))
F(("lydia", 0.68, 0.14, 102, "near-east", None,
               "Lydian gold"))

# The neighbour rule's threshold (Euclidean distance in OKLab) and its justification; colour.py seed copies
# both into colours.json "rules". Set after measuring the palette on the anchors (see colours-README.md).
MIN_DISTANCE = 0.10
MIN_DISTANCE_WHY = ("0.10 in OKLab is about five just-noticeable differences (one is roughly 0.02 here), the point at which two fills "
    "separated by a thin outline read as different colours at a glance. Measured with this tool: Tableau 10's closest pair "
    "(teal and grey) is 0.084 and its median pair 0.185; ColorBrewer Pastel1's closest pair is 0.044. On this wheel, hues 15 "
    "degrees apart at one lightness sit 0.025-0.038 apart, 60 degrees apart 0.10-0.13, and the three lightness variants of one "
    "hue 0.10 (light/mid) and 0.12 (mid/deep), so 0.10 means: a different hue family, or a clearly different lightness. The "
    "vassal tint sits 0.12-0.15 from its suzerain's colour, so it is always told from the state itself; the contested blend "
    "sits half the pair's distance (0.05 at the minimum) from each claimant, which is why it carries a hatch. Capacity: the "
    "72-colour wheel holds 17 mutually distinct colours at 0.10 (22 at 0.08, 10 at 0.12, 7 at 0.14), and the greedy colouring "
    "of the 1,129 polities without a fixed colour over the union of all 120 anchor years' adjacency (plus the polity table's "
    "25 km neighbours) clears 0.10 for every polity and 0.12 for all but 3, then fails for 43 at 0.14 and 130 at 0.16. The 415 "
    "fixed conventional colours were tuned by hand until every neighbouring pair in every anchor year cleared 0.10; at 0.12, "
    "57 neighbouring pairs of the conventional palette would fall short (Hungary beside Romania, Spain beside the Papal States, "
    "the Avars beside Lombard Italy), so 0.12 would cost about a fifth of the conventions. Every fixed and wheel colour also "
    "keeps at least 0.107 from the neutral grey and 0.18 from a pale basemap.")
