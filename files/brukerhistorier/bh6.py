import sqlite3

con = sqlite3.connect("./teater.db")
cursor = con.cursor()
cursor.execute('''SELECT TS.navn AS ForestillingsNavn, O.dato AS Dato, COUNT(B.BillettID) AS AntallSolgtePlasser
                FROM Oppsetning AS O
                JOIN TeaterStykke  AS TS ON O.TeaterStykkeID = TS.TeaterStykkeID
                LEFT JOIN Billett  AS B ON O.OppsetningID = B.OppsetningID
                GROUP BY O.OppsetningID
                ORDER BY AntallSolgtePlasser DESC;
                ''')
data = cursor.fetchall()
con.close()
for i in data:
    print(f'ForestillingsNavn: {i[0]} || Dato: {i[1]} || Antall solgte plasser: {i[2]}')
