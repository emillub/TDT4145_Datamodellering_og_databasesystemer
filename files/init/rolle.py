import sys
sys.path.append('files')
from common.constants import *
from common.sql_utils import *

def insert_roller(skuespiller, ansattID,teaterStykke):
    for rolleNavn in skuespiller['roller']:
            insertValuesIntoTable('Rolle', '(Navn)', f'("{rolleNavn}")')
            rolleID = selectValuesFromTable('Rolle', 'RolleID', f'Navn = "{rolleNavn}"')[0][0]
            insertValuesIntoTable('HarRolle', '(RolleID,AnsattID)',f'({rolleID},{ansattID})')
            insert_RolleIAkt(rolleNavn,rolleID,teaterStykke)
            

def insert_RolleIAkt(rollenavn,rolleID,teaterStykke):
    if len(teaterStykke['akter']) == 1:
        deltarIAkter = {1}
    else: 
        deltarIAkter = teaterStykke['rolleIAkt'][rollenavn]
    for aktNummer in deltarIAkter:
         insertValuesIntoTable('RolleIAkt', '(RolleID, TeaterStykkeID, Nummer)', f'({rolleID},{teaterStykke["id"]}, {aktNummer})')
    