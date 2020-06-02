#!/usr/bin/env python3

import random
from platform import python_version
import time
from urllib.request import  urlopen
import sys
from multiprocessing import Pool, TimeoutError

# Verifies user is using Python3.
if python_version()[0:3] < '3.0':
    print('\n\u001b[31m[FATAL] This only works with Python3!\u001b[33m\n\nIf you have python3, then run Python3 cygwin-mirrors.py\n \u001b[0m')
    sys.exit(1)
 
 # Url of mirrors & other things required by the M.P pool.map
mirrors_url = "http://cygwin.com/mirrors.lst"
test_file = "/x86_64/setup.ini"
block_sz = 8096
 
 # Configuration of how the tested URL's will list themselves as such
def test_host(hostentry):
  host = hostentry["host"]
  sys.stdout.flush()
  start_time = time.time()
  try:
    test = urlopen(host[0] + test_file, timeout=3)
    test.read(block_sz)
    time_spent = time.time() - start_time
    hostentry["time"] = time_spent
    print("\u001b[37;1m%.4f \u001b[36m%40s" % (time_spent, host[1]))
  except IOError:
    hostentry["time"] = 9999
    print("\u001b[31mRESPONSE ERROR:\u001b[0m %s TIMED OUT" % host[1])
  return hostentry
 
if __name__ == '__main__':
 
  mirrors = [
    #    {"host": "",
    #     "time": 1
    #  }
  ]
  
  # Script intro & mirror list identification
  print("\n\n\u001b[0m[*] ———    \u001b[34;1mCygwin Mirror Tester \u001b[0m")
  print("\u001b[0m[*] ———    \u001b[0m\u001b[32;1mbit.ly/CL_OM\u001b[0m")
  print("\u001b[0m[*] ———    \u001b[0mTyler J. Kline \u001b[0m")
  print("\u001b[0m[*] ———    \u001b[0mVersion: 1.0 \u001b[0m \n\n")
  time.sleep(1.5)
  print("\u001b[0m[*] \u001b[34;1mFetching and parsing Cygwin mirrors....\u001b[0m")
  time.sleep(2.2)
  sys.stdout.flush()
  u = urlopen(mirrors_url)
  for line in u:
    strline = str(line)[2:-3]
    host = strline.split(";")
    if host[0].startswith("http://"):
      mirrors.append({"host": host, "time": 9999})
  print("\u001b[0m[*] \u001b[37;1m%d links successfully retrieved!\u001b[0m" % len(mirrors))
  time.sleep(1.5)
  print("\n\n\u001b[0m[*] \u001b[34;1mTesting %d mirrors...\u001b[0m\n" % len(mirrors))
  time.sleep(2)
  random.shuffle(mirrors)
 
  max_hosts_to_try = 150
  testn = 1
 
  num_processors = len(mirrors) / 2.0
  with Pool(processes=int(num_processors)) as pool:
    result = pool.map(test_host, mirrors)
    mirrors = result
    
    mirrors = sorted(mirrors, key=lambda entry: entry["time"])

  # The configuration of the 6 fastest server result
  print("\u001b[0m\u001b[33;1m\n\n-----------------------------------------------------\u001b[0m\n\n\u001b[31;1mTOP 6 QUICKEST MIRROR SERVERS\n\u001b[0m")
  sys.stdout.flush()

  for i in range(6):
    mirror = mirrors[i]
    host_info = mirror["host"]
    if mirror["time"] < 9999:
      print("\u001b[0m\u001b[32m %.6f seconds\u001b[0m, \u001b[35;1m%15s\u001b[0m, \u001b[33m%23s\u001b[0m" % (mirror["time"], host_info[3], host_info[0]), file=sys.stderr)