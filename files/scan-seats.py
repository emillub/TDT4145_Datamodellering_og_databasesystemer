"""
    Leser solgte seter fra filer gitt

    Parametere:
    fil (str): Stien til filen som skal leses

    Returnerer:
    solgteSeter (Dict): Dictionary for solgte seter i en gitt oppsetning på formatet {dato: {område: [(radnr,setenr)]}}
"""

import sqlite3


def inneholderOmraderEllerDato(line):
    return any((not c.isdigit() and c!='x') for c in line) # Sjekker om linje inneholder dato eller område

def scanHovedScenen():
    fil = 'txt/hovedscenen.txt'
    kapasitet = 524
    rader = 22 # teller med Galleri
    forestillinger = {}
    stolerIForegaendeRader = 0
    with open(fil, 'r') as f:
        linjer = f.readlines()
        radIndexOffset = rader
        for radIndex, rad in enumerate(linjer):
            rad = rad.strip() # Fjerner tomrom fra linje
            if inneholderOmraderEllerDato(rad):
                radIndexOffset +=1
                if 'Dato' in rad:
                    dato = rad.strip('Dato ')
                    forestillinger[dato] = {
                        'sal' : 'Hovedscenen',
                        'solgteSeter' : {},
                        'xSeter' : {}
                    }
                else:
                    omraade = rad
                    forestillinger[dato]['solgteSeter'][omraade] = []
                    forestillinger[dato]['xSeter'][omraade] = []
                    print(f"Område: {rad}")
                continue

            xer = 0
            print(len(rad))
            for seteIndex,sete in enumerate(rad):
                seteNr = kapasitet-stolerIForegaendeRader-seteIndex
                if sete == '1':
                    forestillinger[dato]['solgteSeter'][omraade].append((radIndexOffset-radIndex, seteNr))
                elif sete == 'x':
                    forestillinger[dato]['xSeter'][omraade].append((radIndexOffset-radIndex, seteNr))
            stolerIForegaendeRader+=len(rad)
        f.close()
    return forestillinger

def scanGamleScenen():
    fil = 'txt/gamle-scene.txt'
    kapasitet = 524
    rader = 22 # teller med Galleri
    forestillinger = {}
    stolerIForegaendeRader = 0
    with open(fil,'r') as f:
        radIndexOffset = -1 # Passer på at linjer som inneholder tekst ikke regnes som en stolrad
        forestillinger = {}
        omraade = None
        seteIndexOffset = 1
        for radIndex, linje in enumerate(f.readlines()):
            seteIndexOffset = -1
            linje = linje.strip() # Fjerner tomrom fra linje
            linjeHarBokstaver = any((not c.isdigit() and c!='x') for c in linje) # Sjekker om linje inneholder dato eller område
            if linjeHarBokstaver:
                radIndexOffset +=1
                if 'Dato' in linje:
                    dato = linje.strip('Dato ')
                    forestillinger[dato] = {
                        'sal' : 'Hovedscenen',
                        'solgteSeter' : {},
                        'xSeter' : {}
                    }
                else:
                    if omraade is not None: 
                        radIndexOffset = radIndex

                    omraade = linje
                    forestillinger[dato]['solgteSeter'][omraade] = []
                    forestillinger[dato]['xSeter'][omraade] = []
                    print(f"Område: {linje}")
                continue

            for seteIndex,sete in enumerate(linje):
                seteNr = seteIndex-seteIndexOffset
                radNr = radIndex-radIndexOffset
                insertSete(0,radNr,seteNr,omraade)
                if(sete == '1'):
                    forestillinger[dato]['solgteSeter'][omraade].append((radNr, seteNr))
        return forestillinger

def insertSete(salId, radnr, setenr,omrade):
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()

    cursor.execute('''
            SELECT COUNT(*) FROM Sete;
        ''')
    try:
        cursor.execute(f'''
                    INSERT INTO Sete (RadNR, SeteNR, Område, SalID) VALUES {int(radnr)},{int(setenr)},"{omrade}", {salId});
                    ''')
    except:
        print("Error")
    con.commit()
    con.close()

def insertDefaultBruker():
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    cursor.execute(f'''
                INSERT INTO Kunde (KundeID, TelefonNr, Navn, Adresse) VALUES (0, 12345678, "Ola Normann", "Adresseveien 1");
                ''')
    con.commit()
    con.close()

def insertDefaultOrdre():
    klokkeslett = "08:00"
    dato = "2024-01-01"
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    cursor.execute(f'''
                INSERT INTO Ordre VALUES (0, "{dato}", "{klokkeslett}", {0});
                ''')
    con.commit()
    con.close()

def insertBillett(seteID,oppsetningID,type,ordreID,teaterStykkeID):
    con = sqlite3.connect("./teater.db")
    cursor = con.cursor()
    cursor.execute(f'''
                INSERT INTO BILLETT (SeteID,OppsetningID,Type,OrdreID,TeaterStykkeID) VALUES ({seteID},{oppsetningID},{type},{ordreID},{teaterStykkeID});
                ''')
    con.commit()
    con.close()

print(scanHovedScenen())
print(scanGamleScenen())
                

insertDefaultBruker()
insertDefaultOrdre()




            
            

# print(lesSolgteSeterFraFil('txt/hovedscenen.txt',False))