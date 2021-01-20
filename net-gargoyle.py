import re
import subprocess
import sqlite3
import os
import psutil
import hashlib

from subprocess import *
from datetime import datetime


def procs():
  global pstate
  pstate = set()
  for proc in psutil.process_iter(['pid', 'name', 'username']):
    print(proc)
    pstate.add(proc)
  pstate = str(pstate)
  global phash
  phash = hashlib.sha256(pstate.encode('utf-8')).hexdigest()

def nets():
  global nstate
  nstate = set()
  process = subprocess.Popen(('ss', '-tanu'), stdout=subprocess.PIPE)
  output, error = process.communicate()
  process.wait()
  nstate.add(output)
  nstate = str(nstate)
  global nhash
  nhash = hashlib.sha256(nstate.encode('utf-8')).hexdigest()
  
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
                      (date, nhash, phash, nstate, pstate)
                      VALUES (?, ?, ?, ?, ?);"""
    timeslice()
    procs()
    mets()
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
