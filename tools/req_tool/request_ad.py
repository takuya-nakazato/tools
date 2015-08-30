# -*- coding: utf-8 -*-
#usage python request_ad.py URL roop_times max_wait_time outputfile

import sys
import urllib2
import random
import time
import re
from datetime import datetime
from xml.etree.ElementTree import *

argvs = sys.argv

# URL = argvs[1]
URL = "http://xp1.zedo.com/jsc/xp2/fns.vast?n=2696&c=36/2&d=17&s=3&v=vast2&pu=__page-url__&ru=__referrer__&pw=__player-width__&ph=__player-height__&z=__random-number__"
LOOPS = int(argvs[2])
TIME = int(argvs[3])
OUTFILE = argvs[4]

adid_list = [2346008, 2346009, 2346010, 2346011, 2346012]

def get_res(i):
  time = get_current_time
  try:
    res = urllib2.urlopen(URL)
    dict = {"res": res.read(), "status": res.code, "msg": res.msg, "time": time}
  except urllib2.HTTPError, e:
    dict = {"res": None, "status": e.code, "msg": e.reason, "time": time}
  return dict

def get_current_time():
    return datetime.now().strftime('%Y/%m/%d %H:%M:%S:%f')

def get_adid(xmlString):
    return fromstring(xmlString).find(".//Ad").get("id")

def check_adid(adid):
    if not int(adid) in adid_list: return True
    else: return None

if __name__ == "__main__":

  error_lsit = []
  if re.search( "vast", URL ):  vast = True
  else:  vast = False

  f = open(OUTFILE,"w")

  for i in range(LOOPS):
    if i>0:  time.sleep(random.uniform(0,TIME))
    res = get_res(i)
    if vast: adid = get_adid(res["res"])
    else: adid = ""
    if adid != "":
        if check_adid(adid): error_lsit.append(str(i))
    log = str(res["status"]) + "," + res["msg"] + "," + adid + "\n"
    f.write(str(i) + "," + get_current_time() + "," + log)
    print str(i) + ": " + log,

  f.close()
  print "\nFinished.\n"

  f = open("uncorrect_log.txt", "a")
  for num in error_lsit:
      f.write(str(num) + "\n")
  f.close()
