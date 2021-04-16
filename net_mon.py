import time
import json
import sys
import os

import net_gargoyle as netg

LOCK = threading.Lock()

with open("./gargoyle.json", "r") as f:
    gconfig = json.load(f)

maxStartSize = int(gconfig["MAXSTARTSIZE"])
maxRunSize = int(gconfig["MAXRUNSIZE"])

class Gargoyle():
    '''gargoyle.db object with check interval and reference hash'''
    def __init__(self, name, interval, norm_state):
        '''Gargoyle class has three properties: name, interval, and norm_state.'''
        self.name = name # gargoyle.db
        self.interval = interval # 1
        self.norm_state = norm_state # a SHA256 hash reference or other str

    def lasthash(self):
        '''Check the current network STATE hash against the previous network STATE hash.'''
        while True:
            netg.checkdiff()
            print ("Normal STATE is defined by script argument as >>>", self.norm_state)
            if os.stat("/opt/net-gargoyle/workspace/gargoyle.db").st_size >= maxRunSize:
                TIMESTAMP = netg.timeslice()
                print (TIMESTAMP," net-gargoyle2: Max run size detected, rotating gargoyle.db")
                backup = 'cp /opt/net-gargoyle/workspace/gargoyle.db /opt/net-gargoyle/g_$(date +%Y%m%d%H%M%S).db'
                os.system(backup)
                os.remove("/opt/net-gargoyle/workspace/gargoyle.db")
                netg.createtable()
                netg.interact()
                netg.insertstat()
            time.sleep(GARGOYLE.interval)

if __name__ == '__main__':
    INTV = int(sys.argv[1])
    global NORM
    NORM = str(sys.argv[2])
    GARGOYLE = Gargoyle('gargoyle.db', INTV, NORM)
    EXISTS = os.path.isfile('/opt/net-gargoyle/workspace/gargoyle.db')

    if EXISTS:
        if os.stat("/opt/net-gargoyle/workspace/gargoyle.db").st_size == 0:
            netg.createtable()
            netg.interact()
            netg.insertstat()
        if os.stat("/opt/net-gargoyle/workspace/gargoyle.db").st_size >= maxStartSize:
            os.remove("/opt/net-gargoyle/workspace/gargoyle.db")
            netg.createtable()
            netg.interact()
            netg.insertstat()
        CHECKER = threading.Thread(target=GARGOYLE.lasthash(), name='Checker')
        CHECKER.start()
    else:
        netg.createtable()
        netg.interact()
        netg.insertstat()
        CHECKER = threading.Thread(target=GARGOYLE.lasthash(), name='Checker')
        CHECKER.start()
