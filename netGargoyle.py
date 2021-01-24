'''linux honeypot/HIDS module with sqlite for linux'''
import subprocess
import sqlite3
import os
import psutil
import hashlib
import string

from subprocess import *
from datetime import datetime


def procs():
  '''Use psutil to do a ps process list of all processes then make a hash of it.'''
  global pstate
  pstate = set()
  for proc in psutil.process_iter(['pid', 'name', 'username']):
    pstate.add(proc)
  pstate = str(pstate)
  global phash
  phash = hashlib.sha256(pstate.encode('utf-8')).hexdigest()

def nets():
  '''Use linux coreutil to list network EST and LISTEN then make a hash of it.'''
  global nstate
  nstate = set()
  process = subprocess.Popen(('ss', '-tanu'), stdout=subprocess.PIPE)
  output, error = process.communicate()
  process.wait()
  nstate.add(output)
  nstate = str(nstate)
  global nhash
  nhash = hashlib.sha256(nstate.encode('utf-8')).hexdigest()

def lasthash():
    '''Check the last recorded network hash in the sqlite database.'''
  global lhash
  timeslice()
  print(timestamp, " net-gargoyle2: compare last nhash with current nhash and updatedb if different.")
  for row in c.execute('select nhash from nethash order by "date text" DESC;'):
    lhash = row
  conn.commit()
  conn.close()
  timeslice()
  print(timestamp, " net-gargoyle2: The DB connection is now closed.")

def timeslice():
  '''Make a global timestamp with datetime module.'''
  global timestamp
  timestamp = datetime.now()
  return(timestamp)

def interact():
  '''Open up the sqlite db connection.'''
  global conn
  global c
  conn = sqlite3.connect('gargoyle.db')
  c = conn.cursor()
  timeslice()
  print(timestamp, " net-gargoyle2: The DB connection is now open.")

def createtable():
  '''Create an empty table for the program.'''
  interact()
  c.execute('''CREATE TABLE nethash
            (date text, nhash text, phash text, nstate, pstate)''')
  conn.commit()
  conn.close()
  timeslice()
  print (timestamp, " net-gargoyle2: The DB connection is now closed.")

def printdb():
  '''Print the entire sqlite db to STDOUT.'''
  timeslice()
  print(timestamp, " net-gargoyle2: Contents of nethash table printing...")
  for row in c.execute('SELECT * FROM nethash'):
    print(row)
  conn.commit()
  conn.close()
  timeslice()
  print(timestamp, " net-gargoyle2: The DB connection is now closed.")

def insertstat():
  '''Insert the current network and ps data into the database.'''
  try:
    sqlite_insert_with_param = """INSERT INTO nethash
                      (date, nhash, phash, nstate, pstate)
                      VALUES (?, ?, ?, ?, ?);"""
    timeslice()
    procs()
    nets()
    data_tuple = (timestamp, nhash, phash, nstate, pstate)
    c.execute(sqlite_insert_with_param, data_tuple)
    conn.commit()
    conn.close()

  except sqlite3.Error as error:
    timeslice()
    print(timestamp, " net-gargoyle2: Failed to insert into gargoyle.db sqlite table nethash with:", error)

  finally:
    if (conn):
      conn.close()
      timeslice()
      print(timestamp, " net-gargoyle2: The DB connection is now closed.")

def checkdiff():
  '''Compare the last hash pulled from the DB to the current network state hash.'''
  interact()
  lasthash()
  nets()
  nhx = str(lhash)
  nhq = (nhx[2:-3])
  print('my lhash is', nhq)
  print('my nhash is', nhash)
  if (nhq == nhash):
    timeslice()
    print(timestamp, ' net-gargoyle2: Network state is the same.')
  else:
    timeslice()
    print(timestamp, ' net-gargoyle2: Found network state change from nhq to nhash. Updating db...')
    interact()
    insertstat()
