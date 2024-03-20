import sqlite3
import sys
sys.path.append('files')
from common.sql_utils import hentSkuespillereISammeAktogStykke


#Her kan man endre skuespillernavn for å se medskuespillere og teaterstykke. 
navn = 'Jo Saberniak'

SkuespillereOgStykke = hentSkuespillereISammeAktogStykke(navn)
print(f'Skuespiller: {navn}:')
print('--------------------------')
for i in range(len(SkuespillereOgStykke)):
        print(f'MedSkuespiller: {SkuespillereOgStykke[i][1]} || TeaterStykke: {SkuespillereOgStykke[i][2]}')
