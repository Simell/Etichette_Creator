#!/bin/python3


import sqlite3
from sqlite3 import Error
import os


#debug
print("simone")



def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()


def crea_table():
    try:  
        c.execute("""CREATE TABLE indirizzi 
                (file)""")
        print("tabella creata")
    except Error as e:
        
        print(e)


def inserimento_dati():
   #print( os.listdir('Indirizzi_Spedizioni'))
    for i in os.listdir('Indirizzi_SpedizioniDocx'):
        c.execute("INSERT INTO indirizzi (file) values(?)", (i,))
    print("dati inseriti")




# tutte le variabili 
conn = sqlite3.connect(r"indirizzi.db")
c = conn.cursor()
#crea_table()
inserimento_dati()
conn.commit()

