DATABASE_PATH = './teater.db'

HOVED_SCENE = {
    'navn' : "Hovedscenen",
    'kapasitet' : 524,
    'omraader' : [
        {'' : (18,28)},
        {'Galleri' : (4,5)}
        ]}

GAMLE_SCENE = {
    'navn' : "Gamle Scene",
    'kapasitet' : 320,
    'omraader' : [
        {'Parkett' : [18,16,17,18,18,17,18,17,17,14]},
        {'Balkong' : [28,27,22,17]},
        {'Galleri': [33,18,17]}
        ]}

SALER = [HOVED_SCENE, GAMLE_SCENE]

KONGSEMNENE = {
    'navn' : "Kongsemnene",
    'startTid' : "18:30",
    'forfatter' : "Henrik Ibsen",
    'akter' : ['','','','','']
}
STORST_AV_ALT_ER_KJAERLIGHETEN = {
    'navn' : "Størst av alt er kjærligheten",
    'startTid' : "19:30",
    'forfatter' : "Jonas Corell Petersen",
    'akter' : ['']
}