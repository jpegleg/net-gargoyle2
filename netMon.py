import threading
import time

import netGargoyle as ngr

shared_resource = False

lock = threading.Lock()

global conti
conti = 1

def lasthash():
  while conti > 0:
    ngr.checkdiff()
    shared_resource = True
    time.sleep(1)

def monitor():
  while shared_resource == False:
    time.sleep(1)
  ngr.timeslice()
  print(timestamp, f'Thread {threading.currentThread().name} - Detected shared_resource = False')
  time.sleep(1)


if __name__ == '__main__':
  checker = threading.Thread(target=lasthash, name='Checker')
  mon = threading.Thread(target=monitor, name='Mon')

  checker.start()
  mon.start()
