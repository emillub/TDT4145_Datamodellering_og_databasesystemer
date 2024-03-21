import requests
import sys
sys.path.append('filer')
from diverse.konstanter import *

# Henter data fra API
def fetchData(url):
    response = requests.get(url)
    return response.json()

# Henter liste over alle ansatte, returnerer som 2d-liste: [skuespillere, medvirkende]
def fetchAnsatteData(teaterStykke):
    skuespillere = []
    data = fetchData(teaterStykke['apiURL'])
    actorDataList = data[0]["acf"]["actors_list"]
    for index,skuespiller in enumerate(actorDataList):
        navn = skuespiller["actor"]["title"]["rendered"]
        rolleData = skuespiller["sub_title"]
        if rolleData == '':
            roller = [navn]
        else:
            roller = [rolle.strip() for rolle in rolleData.split("/")]
            if 'Trønder' in roller:
                roller = [' / '.join(roller)]
        skuespillere.append({'navn' : navn,
                            'roller' : roller,
                            'id' : index+1})
    
    medvirkende = []
    medvirkendeDataList = data[0]["acf"]["artistic_team_list"]
    for index,medvirker in enumerate(medvirkendeDataList):
        navn =  medvirker["member"]["title"]["rendered"]
        oppgave = medvirker["sub_title"]
        medvirkende.append({'navn' : navn,
                            'oppgave' : oppgave,
                            'id' : len(skuespillere)+index+1})
        
    return {'skuespillere': skuespillere, 'medvirkende' : medvirkende}

fetchAnsatteData(KONGSEMNENE)