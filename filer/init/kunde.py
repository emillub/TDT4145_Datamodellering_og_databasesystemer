import sys
sys.path.append('filer')
from diverse.konstanter import *
from diverse.sql_kommandoer import *

def insert_kunde(navn,tlf,adr):
    if(hentKundeID(navn,tlf)) != []:
        print("Kunde finnes fra før")
        return
    settInnVerdierITabell('Kunde', '(TelefonNr, Navn, Adresse)', f'({tlf}, \"{navn}\",\"{adr}\")')

def hentKundeID(navn, tlf):
    res = velgVerdierFraTabell('Kunde', 'KundeID', f'Navn = \"{navn}\" AND TelefonNr = {tlf}')
    if len(res) == 1:
        res = res[0][0]
    return res

def nyKunde(navn,tlf,adr):
    insert_kunde(navn,tlf,adr)
    return hentKundeID(navn,tlf)