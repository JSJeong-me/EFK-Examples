# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aVFFNMhilneBqcI84jSt0xVCnJqc7FI3
"""

import sys
import os
import json
import time
import datetime
from os.path import abspath, dirname, join
cur_path = os.path.dirname(str(sys.argv[0]))
if cur_path:
  cur_path += "/"

log_file = cur_path + 'log.json'

log_json = dict()
log_json["Data"] = {}

def main():
  i = 0

  while True:
      i = i + 1
      print(i)
      log_json['Data']['Count']=i
      log_json['Created'] = datetime.datetime.utcnow().isoformat()

      with open(log_file, "a") as f:
        json.dump(log_json, f)#. ensure ascii=False)
        f.write("＼n")
        time.sleep(3)

main()



