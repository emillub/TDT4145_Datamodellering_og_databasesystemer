import sys
sys.path.append('filer')
from diverse.skann_sete import *
from diverse.sql_kommandoer import *

# Henter informasjon gjennom en SQLquery basert på brukerhistorie.
# Query er definert i hentForestillingOgSolgteBilleter()-funksjon

# Her kan man endre dato for å se hvilke forestillinger som er satt opp.
dato = "2024-02-03"

Oppsetninger = hentForestillingOgSolgteBilletter(dato)
for el in Oppsetninger:
    print(f'TeaterStykke: {el[0]} || SolteBilletter: {el[1]}')