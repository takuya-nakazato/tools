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
    log = "  "+str(i+1)+":\t"+str(res.code)+"\t"+res.msg
    print log
  except urllib2.HTTPError, e:    
    log = "  "+str(i+1)+":\t"+str(e.code)+"\t"+e.reason
    print log

  f.write(log+"\n")


def write_now(msg):
  
  now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
  f.write("\n"+msg+":  "+now+"\n\n")

	
if __name__ == "__main__":

  print "\nRequest", LOOPS, "times.\n"
  f = open("log.txt","w")
  write_now("Start");

  for i in range(LOOPS):
    req(i)
  
  write_now("End")
  f.close()

  print "\nFinished.\n"

