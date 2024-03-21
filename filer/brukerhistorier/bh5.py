import sys

sys.path.append('filer')
from diverse.sql_kommandoer import *

informasjon = hentTeaterstykkeSkueSpillerRolle()
for el in informasjon:
    print(f'TeaterStykke: {el[0]} || Skuespiller: {el[1]} || Rolle: {el[2]}')
    