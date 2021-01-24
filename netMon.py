import threading
import time
import sqlite3
import sys

import netGargoyle as ngr

shared_resource = False

lock = threading.Lock()

class Gargoyle():
  def __init__(self,name,interval,normstate):
    '''Gargoyle class has three properties: name, interval, and normstate'''
    self.name = name # gargoyle.db
    self.interval = interval # 1
    self.normstate = normstate # 67883f5f0d2945ac53a909bac8fa2ce73029468e07820fd409a5f85ecf2a0924

  def lasthash(self):
    '''check the current network state hash against the previous network state hash'''
    while conti > 0:
      ngr.checkdiff()
      print ("Normal state is defined by script argument as >>>",self.normstate)
      shared_resource = True
      time.sleep(myGargoyle.interval)

global conti
conti = 1

if __name__ == '__main__':
  intv = int(sys.argv[1])
  global norm
  norm = str(sys.argv[2])
  myGargoyle = Gargoyle('gargoyle.db',intv,norm)
  checker = threading.Thread(target=myGargoyle.lasthash(), name='Checker')
  checker.start()
