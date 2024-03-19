import sqlite3
import sys
sys.path.append('files')
from common.constants import *
from common.sql_utils import *


# Inserts teaterstykke into database
def init_teaterStykke(teaterStykke):
    visesISal = teaterStykke['visesI']['id']
    insertValuesIntoTable("TeaterStykke", '(TeaterStykkeID, Navn, StartTid, Forfatter, VisesISal)', f'({teaterStykke["id"]},\"{teaterStykke["navn"]}\", \"{teaterStykke["startTid"]}\",\"{teaterStykke["forfatter"]}\",{visesISal})')

def getTeaterStykkeIDFraSalID(salID):
    return selectValuesFromTable('TeaterStykke', 'TeaterStykkeID', f'VisesISal = {salID}')[0][0]