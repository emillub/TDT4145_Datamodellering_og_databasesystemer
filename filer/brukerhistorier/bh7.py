import sqlite3
import sys
sys.path.append('filer')
from diverse.sql_kommandoer import hentSkuespillereISammeAktogStykke


#Her kan man endre skuespillernavn for å se medskuespillere og teaterstykke. 
navn = 'Jo Saberniak'

SkuespillereOgStykke = hentSkuespillereISammeAktogStykke(navn)
print(f'Skuespiller: {navn}:')
print('--------------------------')
for i in range(len(SkuespillereOgStykke)):
        print(f'MedSkuespiller: {SkuespillereOgStykke[i][0]} || TeaterStykke: {SkuespillereOgStykke[i][1]}')
