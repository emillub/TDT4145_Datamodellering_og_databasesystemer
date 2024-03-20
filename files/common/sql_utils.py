import sqlite3
import sys

import requests
sys.path.append('files')
from common.constants import *

def insertValuesIntoTable(table, valueNames, values):
    con = sqlite3.connect(DATABASE_PATH)
    cursor = con.cursor()
    command = f'INSERT INTO {table} {valueNames} VALUES {values}'
    try:
        cursor.execute(command)
        con.commit()
    except Exception as e:
        print(command)

        print(e)
    con.close()

def selectValuesFromTable(table, values, condition = None):
    con = sqlite3.connect(DATABASE_PATH)
    cursor = con.cursor()
    command = f'SELECT {values} FROM {table}'
    if condition != None:
        command += f' WHERE {condition};'
    try:
        cursor.execute(command)
        res = cursor.fetchall()
    except Exception as e:
        print(command)
        print(e)
        res = None
    con.close()
    return res

def manualInsert(command):
    con = sqlite3.connect(DATABASE_PATH)
    cursor = con.cursor()
    try:
        cursor.execute(command)
        con.commit()
    except Exception as e:
        print(command)
        print(e)
    con.close()

def manualSelect(command):
    con = sqlite3.connect(DATABASE_PATH)
    cursor = con.cursor()
    try:
        cursor.execute(command)
        res = cursor.fetchall()

    except Exception as e:
        print(command)
        print(e)
        res = None
    con.close()
    return res
