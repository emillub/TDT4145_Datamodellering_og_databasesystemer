"""
    Leser solgte seter fra filer gitt

    Parametere:
    fil (str): Stien til filen som skal leses

    Returnerer:
    solgteSeter (Dict): Dictionary for solgte seter i en gitt oppsetning på formatet {dato: {område: [(radnr,setenr)]}}
"""

def lesSolgteSeterFraFil(fil, resetOnNewArea):
    with open(fil,'r') as f:
        radIndexOffset = -1 # Passer på at linjer som inneholder tekst ikke regnes som en stolrad
        solgteSeter = {}
        omraade = None
        seteIndexOffset = 1
        for radIndex, linje in enumerate(f.readlines()):
            if resetOnNewArea:
                seteIndexOffset = -1
            linje = linje.strip() # Fjerner tomrom fra linje
            linjeHarBokstaver = any((not c.isdigit() and c!='x') for c in linje) # Sjekker om linje inneholder dato eller område
            if linjeHarBokstaver:
                radIndexOffset +=1
                if 'Dato' in linje:
                    dato = linje.strip('Dato ')
                    solgteSeter[dato] = {}
                else:
                    if resetOnNewArea and omraade is not None: 
                        radIndexOffset = radIndex

                    omraade = linje
                    solgteSeter[dato][omraade] = []
                    print(f"Område: {linje}")
                continue
            if not resetOnNewArea:
                seteIndexOffset -= len(linje) -1
                print(seteIndexOffset)
                print(f'Antall seter ({len(linje)})')


            for seteIndex,sete in enumerate(linje):
                if(sete =='x'):
                    seteIndexOffset+=1
                elif(sete == '1'):
                    solgteSeter[dato][omraade].append((radIndex-radIndexOffset,seteIndex-seteIndexOffset))
        return solgteSeter
    
print(lesSolgteSeterFraFil('txt/hovedscenen.txt',False))