import sqlite3
import sys
sys.path.append('filer')
from diverse.konstanter import *
from diverse.sql_kommandoer import *

def init_akter(teaterStykke):
    for nummer,aktnavn in enumerate(teaterStykke['akter']):
        if aktnavn == '':
            aktnavn = f"Akt {nummer+1}"
        settInnVerdierITabell('Akt', '(TeaterStykkeID, Nummer, Navn)', f'({teaterStykke["id"]},{nummer+1}, \"{aktnavn}\")')