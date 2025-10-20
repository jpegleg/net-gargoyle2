'''Imports net_gargoyle.py directly to use the functions and creates a template class and thread.'''
import threading
import time
import sys
import uuid
import net_gargoyle as netg

class RealRun():
    '''actually run all of the core functions once'''
    def __init__(self, realrun, network, printeda, printedb):
        self.realrun = realrun
        self.network = network
        self.printeda = printeda
        self.printedb = printedb

    def testrun(self):
        '''finally just run each core function'''
        txid = uuid.uuid4()
        netg.createtable(txid)
        netg.interact(txid)
        netg.insertstat(txid)
        netg.interact(txid)
        netg.checkdiff(txid)
        netg.interact(txid)
        netg.printdb(txid)


if __name__ == '__main__':
    TESTRUN = RealRun('realrun', 'network', 'printeda', 'printedb')
    RUNTESTS = threading.Thread(target=TESTRUN.testrun(), name='TesterPerson')
    RUNTESTS.start()
