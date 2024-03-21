import sys
sys.path.append('filer')
from diverse.konstanter import *
from diverse.sql_kommandoer import *
from diverse.api import fetchAnsatteData
from init.rolle import *
from init.arbeidsoppgave import *

# Inserts Actors and Medvirkende into respectively Ansatte, Skuespillere and Medvirkende
def init_ansatte(teaterStykke):
    data = fetchAnsatteData(teaterStykke)
    skuespillere = data['skuespillere']
    medvirkende = data['medvirkende']
    insert_ansatte(skuespillere, True, teaterStykke=teaterStykke)
    insert_ansatte(medvirkende, False, teaterStykke=teaterStykke)
    
def insert_ansatte(ansatte, erSkuespillere, teaterStykke):
    if erSkuespillere:
        tabellNavn = 'Skuespiller'
    else:
        tabellNavn = 'Medvirkende'

    for index,ansatt in enumerate(ansatte):
        navn = ansatt['navn']
        # Antar at samme navn betyr samme person
        insertCommand =f'''INSERT INTO ANSATT (Navn)
                        SELECT "{navn}"
                        WHERE NOT EXISTS (SELECT 1 FROM ANSATT WHERE Navn = '{navn}');
                               '''
        manuelInsetning(insertCommand)
        ansattID = velgVerdierFraTabell('Ansatt', 'AnsattID', f'Navn = "{navn}"')[0][0]
        settInnVerdierITabell(tabellNavn, '(AnsattID)', f'({ansattID})')
        if erSkuespillere:
            insert_roller(skuespiller=ansatt, ansattID=ansattID, teaterStykke=teaterStykke)
        else:
            insert_arbeidsoppgave(index=index, teaterStykke=teaterStykke,medvirker=ansatt, ansattID=ansattID)