import sys

sys.path.append('files')
from common.sql_utils import *

informasjon = hentTeaterstykkeSkueSpillerRolle()
for el in informasjon:
    print(f'TeaterStykke: {el[0]} || Skuespiller: {el[1]} || Rolle: {el[2]}')
    