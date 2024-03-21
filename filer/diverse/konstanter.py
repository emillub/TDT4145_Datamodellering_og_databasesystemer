DATABASE_PATH = './teater.db'
HOVEDSCENEN_FIL ='txt/hovedscenen.txt'
GAMLE_SCENE_FIL ='txt/gamle-scene.txt'

ORDNIAER = 'Ordinær'
HONNOR = 'Honnør'
STUDENT = 'Student'
BARN = 'Barn'
GRUPPE_10 = 'Gruppe 10'
GRUPPE_10_HONNOR = 'Gruppe honnør 10'


#Teaterstykker
# Format: {
#     id: id i databasen,
#     navn: navn på sal/scene,
#     kapasitet : antall billetter som kan selges,
#     omraader : liste over områder på formatet:
#       { områdenavn : (rader, seterPerRad)} eller
#       { områdenavn : [Rad1AntallSeter,Rad2AntallSeter...]}
# }


HOVED_SCENE = {
    'id' : 1,
    'navn' : "Hovedscenen",
    'kapasitet' : 524,
    'omraader' : [
        {'Parkett' : (18,28)},
        {'Galleri' : (4,5)}],
    'blankeSeter' : [467,468, 469,470,495, 496,497, 498]
}

GAMLE_SCENE = {
    'id' : 2,
    'navn' : "Gamle Scene",
    'kapasitet' : 332,
    'omraader' : [
        {'Parkett' : [18,16,17,18,18,17,18,17,17,14]},
        {'Balkong' : [28,27,22,17]},
        {'Galleri': [33,18,17]}
        ]}

STUDIO_SCENEN = {
    'id' : 3,
    'navn' : "Studio Scenen",
    'kapasitet' : 150,
    'omraader' : []}

TEATER_KJELLEREN = {
    'id' : 4,
    'navn' : "Teater Kjelleren",
    'kapasitet' : 60,
    'omraader' : []}

TEATER_CAFEEN = {
    'id' : 5,
    'navn' : "Teater Caféen",
    'kapasitet' : 100,
    'omraader' : []}

SALER = [HOVED_SCENE, GAMLE_SCENE, STUDIO_SCENEN, TEATER_KJELLEREN, TEATER_CAFEEN]

#Teaterstykker
# Format: {
#     id: id i databasen,
#     apiurl : url til data fra api,
#     navn: tittel på stykke,
#     startTid : klokkeslett,
#     forfatter : navn på forfatter,
#     visesI : Hvilken sal det vises i
#     akter : liste over akt navn, dersom en akt heter '' kalles den Akt + aktid,
#     rolleIAkt : map over roller og hvilke akter de er med i
# }

KONGSEMNENE = {
    'id' : 1,
    'apiURL' : "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=kongsemnene",
    'navn' : "Kongsemnene",
    'startTid' : "18:30",
    'forfatter' : "Henrik Ibsen",
    'akter' : ['','','','',''],
    'visesI' : HOVED_SCENE,
    'oppsetninger' : ["2024-02-01", "2024-02-02", "2024-02-03", "2024-02-05", "2024-02-06"],
    'rolleIAkt': {
        "Haakon Haakonssønn" : {1,2,3,4,5},
        "Inga fra Vartejg (Haakons mor)" : {1,3},
        "Skule jarl" : {1,2,3,4,5},
        "Fru Ragnhild (Skules hustru)" : {1,5},
        "Margrete (Skules datter)" : {1,2,3,4,5},
        "Sigrid (Skules søster)": {1,2,5},
        "Ingebjørg" : {4},
        "Biskop Nikolas" : {1,2,3},
        "Gregorius Jonssønn" : {1,2,3,4,5},
        "Paal Flida / Trønder" : {1,2,3,4,5},
        "Baard Bratte / Trønder" : {2},
        "Jatgeir Skald": {4},
        "Dagfinn Bonde" : {1,2,3,4,5},
        "Peter (prest og Ingebjørgs sønn)" : {3,4,5},    

    },
    'priser' : {
        ORDNIAER: 450,
        HONNOR: 380,
        STUDENT: 280,
        BARN: 280,
        GRUPPE_10: 420,
        GRUPPE_10_HONNOR: 360 
    }
}

STORST_AV_ALT_ER_KJAERLIGHETEN = {
    'id' : 2,
    'apiURL' : "https://www.trondelag-teater.no/wp-json/wp/v2/performances?slug=storst-av-alt-er-kjaerligheten",
    'navn' : "Størst av alt er kjærligheten",
    'startTid' : "19:30",
    'forfatter' : "Jonas Corell Petersen",
    'akter' : [''],
    'visesI' : GAMLE_SCENE,
    'oppsetninger' : ["2024-02-03", "2024-02-06", "2024-02-07", "2024-02-12", "2024-02-13", "2024-02-14"],
    'rolleIAkt' : {
        "Sunniva Du Mond Nordal" : {1},
        "Jo Saberniak" : {1},
        "Marte M. Steinholt" : {1},
        "Tor Ivar Hagen" : {1},
        "Trond-Ove Skrødal" : {1},
        "Natalie Grøndahl Tangen": {1},
        "Åsmund Flaten" : {1} 
    },
    'priser' : {
        ORDNIAER: 350,
        HONNOR: 300,
        STUDENT: 220,
        BARN: 220,
        GRUPPE_10: 320,
        GRUPPE_10_HONNOR: 270
    }
}

TEATERSTYKKER = [KONGSEMNENE, STORST_AV_ALT_ER_KJAERLIGHETEN]


