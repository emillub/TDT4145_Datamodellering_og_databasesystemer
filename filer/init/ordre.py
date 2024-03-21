import sys
sys.path.append('filer')
from diverse.konstanter import *
from diverse.sql_kommandoer import *

def insert_ordre(dato,klokkeslett,kundeid):
    if(hentOrdreID(dato,klokkeslett,kundeid) != []):
        print("Ordre finnes fra før")
        return
    settInnVerdierITabell('Ordre', '(Dato, Klokkeslett, KundeID)', f'("{dato}", "{klokkeslett}",{kundeid})')

def hentOrdreID(dato,klokkeslett,kundeid):
    res = velgVerdierFraTabell('Ordre', 'OrdreID', f'(Dato = "{dato}" AND Klokkeslett = "{klokkeslett}" AND KundeID = {kundeid})')
    if len(res) == 1:
        res = res[0][0]
    return res

def nyOrdre(dato,klokkeslett,kundeid):
    insert_ordre(dato,klokkeslett,kundeid)
    return hentOrdreID(dato,klokkeslett,kundeid)