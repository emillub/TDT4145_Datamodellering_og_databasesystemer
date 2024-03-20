import sys
sys.path.append('files')
from common.constants import *
from common.sql_utils import *

def insert_ordre(dato,klokkeslett,kundeid):
    if(getOrdreID(dato,klokkeslett,kundeid) != []):
        print("Ordre finnes fra før")
        return
    insertValuesIntoTable('Ordre', '(Dato, Klokkeslett, KundeID)', f'("{dato}", "{klokkeslett}",{kundeid})')

def getOrdreID(dato,klokkeslett,kundeid):
    res = selectValuesFromTable('Ordre', 'OrdreID', f'(Dato = "{dato}" AND Klokkeslett = "{klokkeslett}" AND KundeID = {kundeid})')
    if len(res) == 1:
        res = res[0][0]
    return res

def nyOrdre(dato,klokkeslett,kundeid):
    insert_ordre(dato,klokkeslett,kundeid)
    return getOrdreID(dato,klokkeslett,kundeid)