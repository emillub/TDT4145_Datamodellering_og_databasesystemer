import sys
sys.path.append('filer')
from diverse.konstanter import *
from diverse.sql_kommandoer import *
from init.sete import hentKjopteSeterFraOppsetning

def insert_billett(seteid,oppsetningid,bType,ordreid,teaterstykkeid):
    if(hentBillettID(seteid,oppsetningid,bType,ordreid,teaterstykkeid) != []):
        print("Billett eksisterer")
        return
    elif (seteid in hentKjopteSeterFraOppsetning(oppsetningid)):
        print("Sete er allerede kjøpt")
        return
    settInnVerdierITabell('Billett', '(SeteID, OppsetningID, Type, OrdreID,TeaterStykkeID)', f'({seteid}, {oppsetningid}, "{bType}", {ordreid}, {teaterstykkeid})')

def hentBillettID(seteid,oppsetningid,bType,ordreid,teaterstykkeid):
    res = velgVerdierFraTabell('Billett', 'BillettID',f'SeteID = {seteid} AND OppsetningID = {oppsetningid} AND Type = "{bType}" AND OrdreID = {ordreid} AND TeaterStykkeID = {teaterstykkeid}')
    if len(res) == 1:
        res = res[0][0]
    return res

def nyBillett(seteid,oppsetningid,bType,ordreid,teaterstykkeid):
    insert_billett(seteid,oppsetningid,bType,ordreid,teaterstykkeid)
    return hentBillettID(seteid,oppsetningid,bType,ordreid,teaterstykkeid)