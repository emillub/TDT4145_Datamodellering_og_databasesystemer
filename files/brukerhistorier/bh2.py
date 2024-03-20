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



navn = "Navn Navnesen"
tlf = 123456789
adr = "Adressen 1"
kundeid = nyKunde(navn,tlf,adr)
filer = [HOVEDSCENEN_FIL, GAMLE_SCENE_FIL]
for index,fil in enumerate(filer):
    ordreDato = f"2024-01-0{1+index}" #lager nydato og dermed ny ordre
    ordreKlokkeslett = "08:00"
    ordreid = nyOrdre(ordreDato,ordreKlokkeslett,kundeid)

    data = scanFil(fil)
    dato = data['dato']
    salID = getSalIDFraNavn(data['sal'])
    teaterstykkeID = getTeaterStykkeIDFraSalID(salID)
    oppsetningID = getOppsetningIDFraDatoOgStykke(salID,dato)
    for sete in data['solgteSeter']:
        seteID = getSeteIDFromSete(sete)
        nyBillett(seteID,oppsetningID, GRUPPE_10,ordreid,teaterstykkeID)

