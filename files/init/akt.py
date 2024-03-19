import sqlite3
import sys
sys.path.append('files')
from common.constants import *
from common.sql_utils import *

def init_akter(teaterStykke):
    for nummer,aktnavn in enumerate(teaterStykke['akter']):
        if aktnavn == '':
            aktnavn = f"Akt {nummer+1}"
        insertValuesIntoTable('Akt', '(TeaterStykkeID, Nummer, Navn)', f'({teaterStykke["id"]},{nummer+1}, \"{aktnavn}\")')