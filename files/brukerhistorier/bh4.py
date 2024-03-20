import sys
sys.path.append('files')
from common.scan_seats import *
from common.sql_utils import *

# Henter informasjon gjennom en SQLquery basert på brukerhistorie.
# Query er definert i hentForestillingOgSolgteBilleter()-funksjon

# Her kan man endre dato for å se hvilke forestillinger som er satt opp.
dato = "2024-02-03"

Oppsetninger = hentForestillingOgSolgteBilletter(dato)
for el in Oppsetninger:
    print(f'TeaterStykke: {el[0]} || SolteBilletter: {el[1]}')