import sqlite3
import sys
sys.path.append('filer')
from diverse.konstanter import *
from diverse.sql_kommandoer import *


# Inserts teaterstykke into database
def init_teaterStykke(teaterStykke):
    visesISal = teaterStykke['visesI']['id']
    settInnVerdierITabell("TeaterStykke", '(TeaterStykkeID, Navn, StartTid, Forfatter, VisesISal)', f'({teaterStykke["id"]},\"{teaterStykke["navn"]}\", \"{teaterStykke["startTid"]}\",\"{teaterStykke["forfatter"]}\",{visesISal})')

def hentTeaterStykkeIDFraSalID(salID):
    res = velgVerdierFraTabell('TeaterStykke', 'TeaterStykkeID', f'VisesISal = {salID}')
    if len(res) == 1:
        res = res[0][0]
    return res