import sys
sys.path.append('files')
from common.constants import *
from common.sql_utils import *
from init.sal import getSalIDFraNavn, getSalKapasitet
from init.sete import getAntallRaderForOmraade, getAntallRaderPerOmraade

HOVEDSCENEN_FIL ='txt/hovedscenen.txt'
GAMLE_SCENE_FIL ='txt/gamle-scene.txt'

def inneholderOmraderEllerDato(line):
    return any((not c.isdigit() and c!='x') for c in line) # Sjekker om linje inneholder dato eller område

def scanFil(fil):
    if fil == HOVEDSCENEN_FIL:
        sal = HOVED_SCENE
    else:
        sal = GAMLE_SCENE

    oppsetning = {
        'dato' : str,
        'sal' : sal['navn'],
        'solgteSeter' : []
    }

    resetStolNrPerRad = True
    if sal == HOVED_SCENE:
        resetStolNrPerRad = False

    salid = getSalIDFraNavn(sal['navn'])
    kapasitet = getSalKapasitet(salid)
    radPerOmraade = getAntallRaderPerOmraade(salid)

    with open(fil, 'r') as f:
        linjer = f.readlines()
        telteSeter = 0
        for linjeIndex, linje in enumerate(linjer):
            linje = linje.strip() # Fjerner tomrom fra linje
            if inneholderOmraderEllerDato(linje):
                if 'Dato' in linje:
                    oppsetning['dato'] = linje.strip('Dato ')
                else:
                    omraade = linje
                    radNr = getAntallRaderForOmraade(salid,omraade)
                continue
            rad = linje
            radLengde = len(rad)
            seteNr = kapasitet - radLengde - telteSeter
            for seteIndex, sete in enumerate(rad):
                seteNr +=1 
                if resetStolNrPerRad:
                    seteNr = seteIndex +1
                print(radNr, kapasitet - telteSeter)
                if(sete == '1'):
                    oppsetning['solgteSeter'].append((radNr,seteNr,omraade,sal['id']))
                telteSeter += 1
            radNr-=1
                
        print(oppsetning)

                

# insertDefaultBruker()
# insertDefaultOrdre()




            
            

# print(lesSolgteStolrFraFil('txt/hovedscenen.txt',False))