import sys
sys.path.append('files')
from common.scan_seats import *
from init.kunde import *
from init.ordre import *
from init.sal import *
from init.oppsetning import *
from init.sete import *
from init.billett import *
from init.teaterStykke import *



kundeid = ordreid = 0

insert_kunde(kundeid, 12345678, "Ola Norman", "Adressen 1")
ordreDato = "2024-01-01"
ordreKlokkeslett = "08:00"
insert_ordre(ordreDato, ordreKlokkeslett, kundeid)

filer = [HOVEDSCENEN_FIL, GAMLE_SCENE_FIL]

for fil in filer:
    data = scanFil(fil)
    dato = data['dato']
    salID = getSalIDFraNavn(data['sal'])
    teaterstykkeID = getTeaterStykkeIDFraSalID(salID)
    oppsetningID = getOppsetningIDFraDatoOgSal(salID,dato)
    ordreid = getOrdre(ordreDato,ordreKlokkeslett,kundeid)
    for sete in data['solgteSeter']:
        seteID = getSeteIDFromSete(sete)
        insert_billett(seteID,oppsetningID, GRUPPE_10_HONNOR,ordreid,teaterstykkeID)


# scanFil(GAMLE_SCENE_FIL)