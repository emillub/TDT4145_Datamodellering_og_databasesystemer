import sys
sys.path.append('files')
from common.constants import *
from common.sql_utils import *
from init.sete import getKjopteSeterFraOppsetning

def insert_billett(seteid,oppsetningid,bType,ordreid,teaterstykkeid):
    if(getBillettID(seteid,oppsetningid,bType,ordreid,teaterstykkeid) != []):
        print("Billett eksisterer")
        return
    elif (seteid in getKjopteSeterFraOppsetning(oppsetningid)):
        print("Sete er allerede kjøpt")
        return
    insertValuesIntoTable('Billett', '(SeteID, OppsetningID, Type, OrdreID,TeaterStykkeID)', f'({seteid}, {oppsetningid}, "{bType}", {ordreid}, {teaterstykkeid})')

def getBillettID(seteid,oppsetningid,bType,ordreid,teaterstykkeid):
    res = selectValuesFromTable('Billett', 'BillettID',f'SeteID = {seteid} AND OppsetningID = {oppsetningid} AND Type = "{bType}" AND OrdreID = {ordreid} AND TeaterStykkeID = {teaterstykkeid}')
    if len(res) == 1:
        res = res[0][0]
    return res

def nyBillett(seteid,oppsetningid,bType,ordreid,teaterstykkeid):
    insert_billett(seteid,oppsetningid,bType,ordreid,teaterstykkeid)
    return getBillettID(seteid,oppsetningid,bType,ordreid,teaterstykkeid)