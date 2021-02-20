'''Imports net_gargoyle.py directly to use the functions and creates a template class and thread.'''
import threading
import time
import sys

import net_gargoyle as netg

LOCK = threading.Lock()

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
            time.sleep(GARGOYLE.interval)

    def makenew(self):
        '''Make a new database and insert the current state.'''
        netg.interact()
        netg.createtable()
        netg.insertstat()
        netg.timeslice()
        print (netg.timestamp, " - New nhash table ", self.name, self.interval, self.norm_state)

if __name__ == '__main__':
    INTV = int(sys.argv[1])
    global NORM
    NORM = str(sys.argv[2])
    GARGOYLE = Gargoyle('gargoyle.db', INTV, NORM)
    CHECKER = threading.Thread(target=GARGOYLE.lasthash(), name='Checker')
    CHECKER.start()
