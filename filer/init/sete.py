import sqlite3
import sys
sys.path.append('filer')

from diverse.konstanter import *
from diverse.sql_kommandoer import *
from init.oppsetning import hentOppsetningIDFraDatoOgStykke


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
        
    settInnVerdierITabell("Sete", "(SeteID ,RadNr, SeteNr, Område, SalID)", f'({seteID},{radnr}, {setenr}, {omraade},{sal["id"]})')

def hentAntallRaderPerOmraade(salid):
    return manuelValg(f'SELECT Område, COUNT(DISTINCT RadNr) FROM Sete WHERE SalID = {salid} GROUP BY Område')

def hentAntallRaderForOmraade(salid, omraade):
    return manuelValg(f'SELECT COUNT(DISTINCT RadNr) FROM Sete WHERE (SalID = {salid} AND Område = "{omraade}") GROUP BY Område')[0][0]

def hentSeteIDFromSete(sete):
    radnr = sete[0]
    setenr = sete[1]
    omraade = sete[2]
    salid = sete[3]
    return velgVerdierFraTabell('Sete', 'SeteID', f'(RadNr = {radnr} AND SeteNr = {setenr} AND Område = "{omraade}" AND SalID = {salid})')[0][0]

def hentLedigeSeterPaRad(omrade,rad,oppsetningID):
    kjopteSeter = str(hentKjopteSeterFraOppsetning(oppsetningID)).strip('[').strip(']')
    query = f'''
        SELECT *
        FROM Sete JOIN 
        (SELECT VisesISal FROM Oppsetning NATURAL JOIN TeaterStykke WHERE OppsetningID = {oppsetningID}) 
        ON VisesISal = Sete.SalID 
        WHERE (Område IN ("{omrade}") AND RadNr IN ({rad}) AND SeteID NOT IN ({kjopteSeter}))
    '''
    return manuelValg(query)

def hentRaderMedXLedigeSeterForDatoOgStykke(x,dato, stykkeID):
    return hentRaderMedXLedigeSeterForOppsetning(x,hentOppsetningIDFraDatoOgStykke(dato,stykkeID))

def hentRaderMedXLedigeSeterForOppsetning(x,oppsetningID):
    kjopteSeter = str(hentKjopteSeterFraOppsetning(oppsetningID)).strip('[').strip(']')
    
    query = f'''
        SELECT Område, RadNr
        FROM Sete JOIN 
        (SELECT VisesISal FROM Oppsetning NATURAL JOIN TeaterStykke WHERE OppsetningID = {oppsetningID}) 
        ON VisesISal = Sete.SalID 
        WHERE SeteID NOT IN ({kjopteSeter})
        GROUP BY Område, RadNr
        HAVING Count(*) >= {x}'''
    return manuelValg(query)

def hentKjopteSeterFraDatoOgStykkeID(dato, stykkeID):
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

    return [sete[0] for sete in manuelValg(query)]

def hentKjopteSeterFraOppsetning(oppsetningid):
    query = f'''
        SELECT SeteID
        FROM Billett
        WHERE OppsetningID = {oppsetningid}
    '''
    return [sete[0] for sete in manuelValg(query)]