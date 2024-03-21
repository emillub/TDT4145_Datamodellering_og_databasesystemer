import sys
sys.path.append('filer')
from diverse.konstanter import *
from diverse.sql_kommandoer import *

def insert_roller(skuespiller, ansattID,teaterStykke):
    for rolleNavn in skuespiller['roller']:
            settInnVerdierITabell('Rolle', '(Navn)', f'("{rolleNavn}")')
            rolleID = velgVerdierFraTabell('Rolle', 'RolleID', f'Navn = "{rolleNavn}"')[0][0]
            settInnVerdierITabell('HarRolle', '(RolleID,AnsattID)',f'({rolleID},{ansattID})')
            insert_RolleIAkt(rolleNavn,rolleID,teaterStykke)
            
def hentRolleIAkt(rolleID,nummer,teaterStykkeID):
    string = f'SELECT * from RolleIAkt where (RolleID="{rolleID}" AND TeaterStykkeID={teaterStykkeID} AND Nummer={nummer});'
    res = manuelValg(string)
    return res

def insert_RolleIAkt(rollenavn,rolleID,teaterStykke):
    if len(teaterStykke['akter']) == 1:
        deltarIAkter = {1}
    else: 
        deltarIAkter = teaterStykke['rolleIAkt'][rollenavn]
    for aktNummer in deltarIAkter:
        if len(hentRolleIAkt(rolleID,aktNummer,teaterStykke["id"]))==0:
            settInnVerdierITabell('RolleIAkt', '(RolleID, TeaterStykkeID, Nummer)', f'({rolleID},{teaterStykke["id"]}, {aktNummer})')
    