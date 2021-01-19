import re
import subprocess
import sqlite3

from subprocess import *
from datetime import datetime

def timeslice():
  global timestamp
  timestamp = datetime.now()
  return(timestamp)

def interact():
  global conn
  global c
  conn = sqlite3.connect('gargoyle.db')
  c = conn.cursor()
  timeslice()
  print(timestamp, " net-gargoyle2: The DB connection is now open.")

def createtable():
  interact()
  c.execute('''CREATE TABLE nethash
            (date text, nhash text, phash text, nstate, pstate)''')
  conn.commit()
  conn.close()
  timeslice()
  print (timestamp, " net-gargoyle2: The DB connection is now closed.")

def printdb():
  timeslice()
  print(timestamp, " net-gargoyle2: Contents of nethash table printing...")
  for row in c.execute('SELECT * FROM nethash'):
    print(row)
  conn.commit()
  conn.close()
  timeslice()
  print(timestamp, " net-gargoyle2: The DB connection is now closed.")

def insertstat():
  try:
    sqlite_insert_with_param = """INSERT INTO nethash
                      (date, nhash, phash, nstate)
                      VALUES (?, ?, ?, ?, ?);"""
    timeslice()
    data_tuple = (timestamp, nhash, phash, nstate, pstate)
    c.execute(sqlite_insert_with_param, data_tuple)
    conn.commit()
    conn.close()

  except sqlite.Error as error:
    timeslice()
    print(timestamp, " net-gargoyle2: Failed to insert into gargoyle.db sqlite t                                                                                                                                                             able nethash with:", error)

  finally:
    if (conn):
      conn.close()
      timeslice()
      print(timestamp, " net-gargoyle2: The DB connection is now closed.")

      
#### WIP
