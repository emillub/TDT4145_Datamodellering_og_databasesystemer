import sys
sys.path.append('files')
from common.sql_utils import *
from init.sete import *

print(getKjopteSeter("2024-02-03",2))
print(getRaderMedXLedigeSeter(10,"2024-02-03",2))
print(getLedigeSeterPaRadMedXLedigeSeter(10,"2024-02-03",2))

def kjopBilletter():

    query = f'''
    SELECT RadNr
    FROM Sete 
    JOIN (SELECT VisesISal FROM TeaterStykke WHERE TeaterStykkeID = 2) AS t ON Sete.SalID = t.VisesISal
    WHERE SeteID NOT IN (
        SELECT SeteID
        FROM Oppsetning 
        JOIN (SELECT SeteID, OppsetningID AS o FROM Billett) AS b ON Oppsetning.OppsetningID = b.o
        WHERE (Dato = '2024-02-03' AND TeaterStykkeID = 2)
    )
    GROUP BY RadNr
    HAVING COUNT(*) > 10;
    '''
    print(manualSelect(query))

# kjopBilletter()

    