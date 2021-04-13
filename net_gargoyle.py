'''linux honeypot/HIDS module with sqlite for linux'''
import subprocess
import sqlite3
import hashlib
from datetime import datetime
import psutil

def procs():
    '''Use psutil to do a ps process list of all processes then make a hash of it.'''
    global PSTATE
    PSTATE = set()
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        PSTATE.add(proc)
    PSTATE = str(PSTATE)
    global PHASH
    PHASH = hashlib.sha256(PSTATE.encode('utf-8')).hexdigest()

def nets():
    '''Use linux coreutil to list network EST and LISTEN then make a hash of it.'''
    global NSTATE
    NSTATE = set()
    process = subprocess.Popen(('ss', '-tanu'), stdout=subprocess.PIPE)
    output = process.communicate()
    process.wait()
    NSTATE.add(output)
    NSTATE = str(NSTATE)
    global NHASH
    NHASH = hashlib.sha256(NSTATE.encode('utf-8')).hexdigest()

def lasthash():
    '''Check the last recorded network hash in the sqlite database.'''
    timeslice()
    print(TIMESTAMP, " compare last NHASH and NHASH and updatedb if different.")
    for row in C.execute('select NHASH from nethash order by "date text" DESC;'):
        global LHASH
        LHASH = row
    CONN.commit()
    CONN.close()
    timeslice()
    print(TIMESTAMP, " net-gargoyle2: The DB CONNection is now closed.")

def timeslice():
    '''Make a global TIMESTAMP with datetime module.'''
    global TIMESTAMP
    TIMESTAMP = datetime.now()
    return(TIMESTAMP)

def interact():
    '''Open up the sqlite db CONNection.'''
    global CONN
    CONN = sqlite3.connect('gargoyle.db')
    global C
    C = CONN.cursor()
    timeslice()
    print(TIMESTAMP, " net-gargoyle2: The DB CONNection is now open.")

def createtable():
    '''Create an empty table for the program.'''
    interact()
    C.execute('''CREATE TABLE nethash
                        (date text, NHASH text, PHASH text, NSTATE, PSTATE)''')
    CONN.commit()
    CONN.close()
    timeslice()
    print (TIMESTAMP, " net-gargoyle2: The DB CONNection is now closed.")

def printdb():
    '''Print the entire sqlite db to STDOUT.'''
    timeslice()
    print(TIMESTAMP, " net-gargoyle2: Contents of nethash table printing...")
    for row in C.execute('SELECT * FROM nethash'):
        print(row)
    CONN.commit()
    CONN.close()
    timeslice()
    print(TIMESTAMP, " net-gargoyle2: The DB CONNection is now closed.")

def insertstat():
    '''Insert the current network and ps data into the database.'''
    try:
        sqlite_insert_with_param = """INSERT INTO nethash
                                            (date, NHASH, PHASH, NSTATE, PSTATE)
                                            VALUES (?, ?, ?, ?, ?);"""
        timeslice()
        procs()
        nets()
        data_tuple = (TIMESTAMP, NHASH, PHASH, NSTATE, PSTATE)
        C.execute(sqlite_insert_with_param, data_tuple)
        CONN.commit()
        CONN.close()

    except sqlite3.Error as error:
        timeslice()
        print(TIMESTAMP, " net-gargoyle2: Failed to insert into gargoyle.db NHASH table:", error)

    finally:
        if (CONN):
            CONN.close()
            timeslice()
            print(TIMESTAMP, " net-gargoyle2: The DB CONNection is now closed.")

def checkdiff():
    '''Compare the last hash pulled from the DB to the current network state hash.'''
    interact()
    lasthash()
    nets()
    try:
        nhx = str(LHASH)
        
    except (ValueError, RuntimeError, TypeError, NameError) as error:
        timeslice()
        print(TIMESTAMP, " net-gargoyle2: Check gargoyle.db for a valid last entry, LHASH.",error)
    
    try:
        nhq = (nhx[2:-3])
        
    except (ValueError, RuntimeError, TypeError, NameError) as error:
        timeslice()
        print(TIMESTAMP, " net-gargoyle2: Check gargoyle.db for a valid last entry, LHASH.",error)
        
    print('my LHASH is', nhq)
    print('my NHASH is', NHASH)
    if (nhq == NHASH):
        timeslice()
        print(TIMESTAMP, ' net-gargoyle2: Network state is the same <<< No action.')
    else:
        timeslice()
        print(TIMESTAMP, ' net-gargoyle2: Network change detected >>> Updating db...')
        interact()
        insertstat()

if __name__ == '__main__':
    '''Print some helpful messages if executed instead of imported.'''
    print("This script is not intended to be invoked directly.")
    print("Instead, use net_mon.py or another script that imports this file, net_gargoyle.py")
    print("Or use systemd: systemctl start net-gargle")
