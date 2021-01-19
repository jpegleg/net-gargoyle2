import re
import subprocess
import sqlite3

from subprocess import *

def interact():
  global conn
  global c
  conn = sqlite3.connect('gargoyle.db')
  c = conn.cursor()
  print("The DB connection is now open.")
  
def createtable():
  c.execute('''CREATE TABLE nethash
            (date text, nhash text, phash text, nstate)''')
  c.execute("INSERT INTO nethash VALUES (timestamp, nhash, phash, nstate)")
  conn.commit()
  conn.close()
  
def printdb():
  for row in c.execute('SELECT * FROM nethash'):
    print(row)
     
def insertstat():
  try:
    interact
    sqlite_insert_with_param = """INSERT INTO nethash
                      (date, nhash, phash, nstate)
                      VALUES (?, ?, ?, ?);"""
     
    data_tuple = (date, nhash, phash, nstate)
    c.execute(sqlite_insert_with_param, data_tuple)
    conn.commit()
    conn.close()
    
  except sqlite.Error as error:
    print("Failed to insert into gargoyle.db sqlite table nethash with:", error)
    
  finally:
    if (conn):
      conn.close()
      print("The DB connection is now closed.")
      
#### WIP
