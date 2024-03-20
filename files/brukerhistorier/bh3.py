import sys
sys.path.append('files')
from common.sql_utils import *
from common.constants import *
from init.sete import *
from init.kunde import *
from init.ordre import *
from init.billett import *

oppretterBruker = True
while oppretterBruker:
    print("La oss lage en kundeprofil til deg!")
    try:
        navn = input("Hva heter du? ")
        tlf = int(input("Hva er tlf. nr ditt? "))
        adr = input("Hva er adressen din? ")
    except:
        print("Oops noe gikk galt")
        continue

    oppretterBruker = False
    kundeid = nyKunde(navn,tlf,adr)

oppsetningDato = "2024-02-03"
stykkeID = STORST_AV_ALT_ER_KJAERLIGHETEN['id']
antallBilletter = 9
oppsetning = getOppsetningIDFraDatoOgStykke(stykkeID,oppsetningDato)
ledigerader = getRaderMedXLedigeSeterForOppsetning(antallBilletter,oppsetning)
ordreDato = "2024-02-01"
ordreKlokkeslett = "13:28"
raderString = f'Det er {len(ledigerader)} rader med {antallBilletter} ledige stoler\n'
for index,omraadeOgrad in enumerate(ledigerader):
    raderString += f'[{index}] : {omraadeOgrad}\n' 
print(raderString)
velgRad = 'Velg en rad ved å skrive inn tallet til venstre for raden: '

while True:
    try:
        omraadeOgrad = ledigerader[int(input(velgRad))]
        print(omraadeOgrad)
    except:
        print("Oops noe gikk galt")
        continue
    
    ordreId = nyOrdre(ordreDato,ordreKlokkeslett, kundeid)
    ledigeSeter = getLedigeSeterPaRad(omraadeOgrad[0], omraadeOgrad[1],oppsetning)
    billetter = []
    for sete in ledigeSeter:
        billetter.append(nyBillett(sete[0],oppsetning,ORDNIAER,ordreId, stykkeID))
        if len(billetter) == antallBilletter:
            break
    
    print(f"Kjøpte {antallBilletter} til {STORST_AV_ALT_ER_KJAERLIGHETEN['navn']} i område {omraadeOgrad[0]} på rad {omraadeOgrad[1]}")
    break

    