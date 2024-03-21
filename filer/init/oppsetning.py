import sys
sys.path.append('filer')
from diverse.konstanter import *
from diverse.sql_kommandoer import *

def init_oppsetninger(teaterstykke):
    for oppsetningsDato in teaterstykke['oppsetninger']:
        settInnVerdierITabell('Oppsetning', '(Dato, TeaterStykkeID)', f'(\"{oppsetningsDato}\", {teaterstykke["id"]})')
    
def hentOppsetningIDFraDatoOgStykke(teaterstykkeid, dato):
    res = velgVerdierFraTabell('Oppsetning', 'OppsetningID', f'(Dato = "{dato}" AND TeaterStykkeID = {teaterstykkeid})')
    if len(res)==1:
        res = res[0][0]
    return res
