import sqlite3
import sys
sys.path.append('files')

from common.constants import *
from common.sql_utils import *


def init_seter(sal):
    seteIndexISal = 1
    for omraade in sal['omraader']:
        for omradenavn,raderOgSeter in omraade.items():
            omraadeValue = f'"{omradenavn}"'
            if omradenavn == '':
                omraadeValue = 'NULL'
            if isinstance(raderOgSeter,tuple):
                rader = raderOgSeter[0]
                seter = raderOgSeter[1]
                for radNr in range (rader):
                    for s in range (seter):
                        init_sete(seteIndexISal,radnr=radNr+1, setenr=s+1, omraade=omraadeValue, sal=sal)
                        seteIndexISal+=1
            else:
                for radNr,antallSeter in enumerate(raderOgSeter):
                    for s in range(antallSeter):
                        init_sete(seteIndexISal,radNr+1, setenr=s+1, omraade=omraadeValue, sal=sal)
                        seteIndexISal+=1

def init_sete(seteIndexISal,radnr,setenr,omraade,sal):
    antallSiffer = len(str(sal['kapasitet']))
    seteID = int(str(sal['id']) + str(seteIndexISal).zfill(antallSiffer))
    if(sal == HOVED_SCENE):
        setenr = seteIndexISal
        if setenr in HOVED_SCENE['blankeSeter']:
            return
        
    insertValuesIntoTable("Sete", "(SeteID ,RadNr, SeteNr, Område, SalID)", f'({seteID},{radnr}, {setenr}, {omraade},{sal["id"]})')

def getAntallRaderPerOmraade(salid):
    return manualCommanSqlSelect(f'SELECT Område, COUNT(DISTINCT RadNr) FROM Sete WHERE SalID = {salid} GROUP BY Område')

def getAntallRaderForOmraade(salid, omraade):
    return manualCommanSqlSelect(f'SELECT COUNT(DISTINCT RadNr) FROM Sete WHERE (SalID = {salid} AND Område = "{omraade}") GROUP BY Område')[0][0]

def getSeteIDFromSete(sete):
    radnr = sete[0]
    setenr = sete[1]
    omraade = sete[2]
    salid = sete[3]
    return selectValuesFromTable('Sete', 'SeteID', f'(RadNr = {radnr} AND SeteNr = {setenr} AND Område = "{omraade}" AND SalID = {salid})')[0][0]