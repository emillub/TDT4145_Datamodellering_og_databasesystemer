import sys
sys.path.append('files')
from common.constants import *
from common.sql_utils import *

def init_oppsetninger(teaterstykke):
    for oppsetningsDato in teaterstykke['oppsetninger']:
        insertValuesIntoTable('Oppsetning', '(Dato, TeaterStykkeID)', f'(\"{oppsetningsDato}\", {teaterstykke["id"]})')
    
def getOppsetningIDFraDatoOgStykke(teaterstykkeid, dato):
    res = selectValuesFromTable('Oppsetning', 'OppsetningID', f'(Dato = "{dato}" AND TeaterStykkeID = {teaterstykkeid})')
    if len(res)==1:
        res = res[0][0]
    return res
