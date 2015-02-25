# -*- coding: utf-8 -*-
#usage python requester.py URL roops max_wait_time

import sys
import urllib2
import random
import time
from datetime import datetime

argvs = sys.argv

URL = argvs[1]
LOOPS = int(argvs[2])
TIME = int(argvs[3])

def req(i):

  time.sleep(random.uniform(0,TIME))

  try:
    res = urllib2.urlopen(URL) 
    log = str(i+1)+": "+str(res.code)+" "+res.msg
    print log
  except urllib2.HTTPError, e:    
    log = str(i+1)+": "+str(e.code)+" "+e.reason
    print log

  f.write(log+"\n")

	
if __name__ == "__main__":

  print "\nRequest", LOOPS, "times.\n"

  f = open("log.txt","w")
  now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
  f.write("start:  "+now+"\n\n")

  for i in range(LOOPS):
    req(i)

  now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
  f.write("\nfinish: "+now+"\n")
  f.close()

  print "\nFinished.\n"

