import sqlite3
import requests
import sys
sys.path.append('files')
from common.constants import *
from common.sql_utils import *
from common.api_service import fetchAnsatteData
from init._table_init import init_table

# Inserts Actors and Medvirkende into respectively Ansatte, Skuespillere and Medvirkende
def init_ansatte(teaterStykke):
    data = fetchAnsatteData(teaterStykke)
    skuespillere = data['skuespillere']
    medvirkende = data['medvirkende']

    for index,skuespiller in enumerate(skuespillere):
        navn = skuespiller['navn']
        
        # Antar at samme navn betyr samme person
        insertCommand =f'''INSERT INTO ANSATT (Navn)
                        SELECT "{navn}"
                        WHERE NOT EXISTS (SELECT 1 FROM ANSATT WHERE Navn = '{navn}');
                               '''
        manualCommandSqlInsert(insertCommand)
        selectCondition = f'Navn = "{navn}"'
        ansattID = fetchAllValuesFromTable('Ansatt', 'AnsattID', selectCondition)[0][0]

        insertValuesIntoTable('Skuespiller', '(AnsattID)', f'({ansattID})')


    for index,medvirker in enumerate(medvirkende):
        navn = medvirker['navn']
        oppgave = medvirker['oppgave']
        oppgaveID = int(str(teaterStykke['id'])+str(index))
        # Antar at samme navn betyr samme person
        insertCommand =f'''INSERT INTO ANSATT (Navn)
                        SELECT "{navn}"
                        WHERE NOT EXISTS (SELECT 1 FROM ANSATT WHERE Navn = '{navn}');
                               '''
        manualCommandSqlInsert(insertCommand)
        selectCondition = f'Navn = "{navn}"'
        ansattID = fetchAllValuesFromTable('Ansatt', 'AnsattID', selectCondition)[0][0]
        insertValuesIntoTable('Medvirkende', '(AnsattID)', f'({ansattID})')
        insertValuesIntoTable('Arbeidsoppgave', '(OppgaveID, Navn, TeaterStykkeID)', f'({oppgaveID},\"{(oppgave)}\", {teaterStykke["id"]})')
        insertValuesIntoTable('HarOppgave', '(OppgaveID, AnsattID)', f'({oppgaveID}, {ansattID})')


