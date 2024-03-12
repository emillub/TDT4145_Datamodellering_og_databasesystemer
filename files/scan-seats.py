"""
    Leser solgte seter fra filer gitt

    Parametere:
    fil (str): Stien til filen som skal leses

    Returnerer:
    solgteSeter (Dict): Dictionary for solgte seter i en gitt oppsetning på formatet {dato: {område: [(radnr,setenr)]}}
"""
def lesSolgteSeterFraFil(fil):
    with open(fil,'r') as f:

        radIndexOffset = -1 #Paser på at linjer som inneholder tekst ikke regnes som en stolrad
        solgteSeter = {}
        for radIndex, linje in enumerate(f.readlines()):
            seteIndexOffset = -1
            linje = linje.strip() # Fjerner tomrom fra linje
            linjeHarBokstaver = any((not c.isdigit() and c!='x') for c in linje)
            if linjeHarBokstaver:
                radIndexOffset +=1
                if 'Dato' in linje:
                    dato = linje.strip('Dato ')
                    solgteSeter[dato] = {}
                else:
                    omraade = linje
                    solgteSeter[dato][omraade] = []
                    print(f"Område: {linje}")
                continue

            for seteIndex,sete in enumerate(linje):
                if(sete =='x'):
                    seteIndexOffset+=1
                elif(sete == '1'):
                    solgteSeter[dato][omraade].append((radIndex-radIndexOffset,seteIndex-seteIndexOffset))
        return solgteSeter
    
print(lesSolgteSeterFraFil('txt/gamle-scene.txt'))