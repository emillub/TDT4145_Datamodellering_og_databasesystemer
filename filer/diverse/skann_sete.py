import sys
sys.path.append('filer')
from diverse.konstanter import *
from diverse.sql_kommandoer import *
from init.sal import hentSalIDFraNavn,hentSalKapasitet
from init.sete import hentAntallRaderForOmraade

def inneholderOmraderEllerDato(linje):
    return any((not c.isdigit() and c!='x') for c in linje) # Sjekker om linje inneholder dato eller område

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

    salid = hentSalIDFraNavn(sal['navn'])
    kapasitet = hentSalKapasitet(salid)

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
                    radNr =hentAntallRaderForOmraade(salid,omraade)
                continue
            rad = linje
            radLengde = len(rad)
            seteNr = kapasitet - radLengde - telteSeter
            for seteIndex, sete in enumerate(rad):
                seteNr +=1 
                if resetStolNrPerRad:
                    seteNr = seteIndex +1
                if(sete == '1'):
                    oppsetning['solgteSeter'].append((radNr,seteNr,omraade,sal['id']))
                telteSeter += 1
            radNr-=1
    return oppsetning
