def lesSolgteSeterFraFil(fil):
    with open(fil,'r') as f:
        radIndexOffset =0 #Paser på at linjer som inneholder tekst ikke regnes som en stolrad
        solgteSeter = {}
        for radIndex, linje in enumerate(f.readlines()):
            linje = linje.strip() # Fjerner tomrom fra linje
            linjeHarBokstaver = any(not c.isdigit() for c in linje)
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
                if(sete == '1'):
                    solgteSeter[dato][omraade].append((radIndex,seteIndex))
        return solgteSeter