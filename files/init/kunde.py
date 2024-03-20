import sys
sys.path.append('files')
from common.constants import *
from common.sql_utils import *

def insert_kunde(navn,tlf,adr):
    if(getKundeID(navn,tlf)) != []:
        print("Kunde finnes fra før")
        return
    insertValuesIntoTable('Kunde', '(TelefonNr, Navn, Adresse)', f'({tlf}, \"{navn}\",\"{adr}\")')

def getKundeID(navn, tlf):
    res = selectValuesFromTable('Kunde', 'KundeID', f'Navn = \"{navn}\" AND TelefonNr = {tlf}')
    if len(res) == 1:
        res = res[0][0]
    return res

def nyKunde(navn,tlf,adr):
    insert_kunde(navn,tlf,adr)
    return getKundeID(navn,tlf)