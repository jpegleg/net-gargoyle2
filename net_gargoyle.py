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
    # This stores every running process in a single field in the db.
    # Pehaps ugly to extract from, but comprehensive.
    # This may be the most interesting part of net-gargoyle.
    # But feel free to change it to be more specific etc.
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        PSTATE.add(proc)
    PSTATE = str(PSTATE)
    global PHASH
    PHASH = hashlib.sha256(PSTATE.encode('utf-8')).hexdigest()

def nets():
    '''Use linux coreutil to list network EST and LISTEN then make a hash of it.'''
    global NSTATE
    NSTATE = set()
    # Change this to whatever network data or program you wish.
    # What is used here is for capturing all UDP and TCP connections.
    # It is subprocess.Popen, you can switch it out, perhaps use
    # the os module (import it first) then call os.system.
    # You might, for example, use what I have commented here
    # to just capture LISTEN connections:
    #  process = 'ss -tanu | grep LISTEN | awk \'{ print $5 }\'''
    #  NSTATE = str(os.system(process))
    process = subprocess.Popen(('ss', '-tanu'), stdout=subprocess.PIPE)
    output = process.communicate()
    process.wait()
    NSTATE.add(output)
    NSTATE = str(NSTATE)
    global NHASH
    NHASH = hashlib.sha256(NSTATE.encode('utf-8')).hexdigest()

def lasthash(TXID):
    '''Check the last recorded network hash in the sqlite database.'''
    timeslice()
    print(TIMESTAMP, TXID, " compare last NHASH and NHASH and updatedb if different.")
    for row in C.execute('select NHASH from nethash order by "date text" DESC;'):
        global LHASH
        LHASH = row
    CONN.commit()
    CONN.close()
    timeslice()
    print(TIMESTAMP, TXID, " net-gargoyle2: The DB CONNection is now closed.")

def timeslice():
    '''Make a global TIMESTAMP with datetime module.'''
    global TIMESTAMP
    TIMESTAMP = datetime.now()
    return(TIMESTAMP)

def interact(TXID):
    '''Open up the sqlite db CONNection.'''
    global CONN
    CONN = sqlite3.connect('gargoyle.db')
    global C
    C = CONN.cursor()
    timeslice()
    print(TIMESTAMP, TXID, " net-gargoyle2: The DB CONNection is now open.")

def createtable(TXID):
    '''Create an empty table for the program.'''
    interact(TXID)
    C.execute('''CREATE TABLE nethash
                        (date text, NHASH text, PHASH text, NSTATE, PSTATE)''')
    CONN.commit()
    CONN.close()
    timeslice()
    print (TIMESTAMP, TXID, " net-gargoyle2: The DB CONNection is now closed.")

def printdb(TXID):
    '''Print the entire sqlite db to STDOUT.'''
    timeslice()
    print(TIMESTAMP, TXID, " net-gargoyle2: Contents of nethash table printing...")
    for row in C.execute('SELECT * FROM nethash'):
        print(row)
    CONN.commit()
    CONN.close()
    timeslice()
    print(TIMESTAMP, TXID, " net-gargoyle2: The DB CONNection is now closed.")

def insertstat(TXID):
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
        print(TIMESTAMP, TXID, " net-gargoyle2: Failed to insert into gargoyle.db NHASH table:", error)

    finally:
        if (CONN):
            CONN.close()
            timeslice()
            print(TIMESTAMP, TXID, " net-gargoyle2: The DB CONNection is now closed.")

def checkdiff(TXID):
    '''Compare the last hash pulled from the DB to the current network state hash.'''
    interact(TXID)
    lasthash(TXID)
    nets()
    try:
        nhx = str(LHASH)

    except (ValueError, RuntimeError, TypeError, NameError) as error:
        timeslice()
        print(TIMESTAMP, TXID, " net-gargoyle2: Check gargoyle.db for a valid last entry, LHASH.",error)

    try:
        nhq = (nhx[2:-3])

    except (ValueError, RuntimeError, TypeError, NameError) as error:
        timeslice()
        print(TIMESTAMP, TXID, " net-gargoyle2: Check gargoyle.db for a valid last entry, LHASH.",error)
    retime = timeslice()
    print(retime, TXID, 'my LHASH is', nhq)
    print(retime, TXID, 'my NHASH is', NHASH)
    if (nhq == NHASH):
        timeslice()
        print(TIMESTAMP, TXID, ' net-gargoyle2: Network state is the same <<< No action.')
    else:
        timeslice()
        print(TIMESTAMP, TXID, ' net-gargoyle2: Network change detected >>> Updating db...')
        interact(TXID)
        insertstat(TXID)

if __name__ == '__main__':
    '''Print some helpful messages if executed instead of imported.'''
    print("This script is not intended to be invoked directly.")
    print("Instead, use net_mon.py or another script that imports this file, net_gargoyle.py")
    print("Or use systemd: systemctl start net-gargle")
