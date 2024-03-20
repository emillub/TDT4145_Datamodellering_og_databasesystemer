import sqlite3
import sys
sys.path.append('files')

from common.constants import *
from common.sql_utils import *
from init.oppsetning import getOppsetningIDFraDatoOgStykke


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
    return manualSelect(f'SELECT Område, COUNT(DISTINCT RadNr) FROM Sete WHERE SalID = {salid} GROUP BY Område')

def getAntallRaderForOmraade(salid, omraade):
    return manualSelect(f'SELECT COUNT(DISTINCT RadNr) FROM Sete WHERE (SalID = {salid} AND Område = "{omraade}") GROUP BY Område')[0][0]

def getSeteIDFromSete(sete):
    radnr = sete[0]
    setenr = sete[1]
    omraade = sete[2]
    salid = sete[3]
    return selectValuesFromTable('Sete', 'SeteID', f'(RadNr = {radnr} AND SeteNr = {setenr} AND Område = "{omraade}" AND SalID = {salid})')[0][0]

def getLedigeSeterPaRad(omrade,rad,oppsetningID):
    kjopteSeter = str(getKjopteSeterFraOppsetning(oppsetningID)).strip('[').strip(']')
    query = f'''
        SELECT *
        FROM Sete JOIN 
        (SELECT VisesISal FROM Oppsetning NATURAL JOIN TeaterStykke WHERE OppsetningID = {oppsetningID}) 
        ON VisesISal = Sete.SalID 
        WHERE (Område IN ("{omrade}") AND RadNr IN ({rad}) AND SeteID NOT IN ({kjopteSeter}))
    '''
    return manualSelect(query)

def getRaderMedXLedigeSeterForDatoOgStykke(x,dato, stykkeID):
    return getRaderMedXLedigeSeterForOppsetning(x,getOppsetningIDFraDatoOgStykke(dato,stykkeID))

def getRaderMedXLedigeSeterForOppsetning(x,oppsetningID):
    kjopteSeter = str(getKjopteSeterFraOppsetning(oppsetningID)).strip('[').strip(']')
    
    query = f'''
        SELECT Område, RadNr
        FROM Sete JOIN 
        (SELECT VisesISal FROM Oppsetning NATURAL JOIN TeaterStykke WHERE OppsetningID = {oppsetningID}) 
        ON VisesISal = Sete.SalID 
        WHERE SeteID NOT IN ({kjopteSeter})
        GROUP BY Område, RadNr
        HAVING Count(*) >= {x}'''
    return manualSelect(query)

def getKjopteSeterFraDatoOgStykkeID(dato, stykkeID):
    query = f'''
        SELECT SeteID
        FROM Sete
        NATURAL JOIN (
            SELECT SeteID
            FROM Oppsetning 
            JOIN (SELECT SeteID, OppsetningID FROM Billett) AS b ON Oppsetning.OppsetningID = b.OppsetningID
            WHERE (Dato = "{dato}" AND TeaterStykkeID = {stykkeID})
        )
    '''

    return [sete[0] for sete in manualSelect(query)]

def getKjopteSeterFraOppsetning(oppsetningid):
    query = f'''
        SELECT SeteID
        FROM Billett
        WHERE OppsetningID = {oppsetningid}
    '''
    return [sete[0] for sete in manualSelect(query)]