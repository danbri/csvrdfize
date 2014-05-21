#!/usr/bin/env python

# DISCLAIMER: Sample code only. Do not recycle for production. http://xkcd.com/327/ etc.

import sys
import rdflib
import logging
import csv
import json
from pprint import pprint

sys.path.append("./lib") # tmp for uritemplate
from uritemplate import expand

# config
logging.basicConfig()
logging.disable(logging.WARNING) # complains due to {template} syntax within URIs



def main():
  t1_cfg = { 'fn': 'samples/simple-weather-observation/t1.csv',
        'tf': 'samples/simple-weather-observation/map1.ttlt',
        'mf': 'samples/simple-weather-observation/t1.json' }
  print generateTurtle(t1_cfg)  

def generateTurtle(cfg):
  fn = cfg['fn']
  tf = cfg['tf']
  mf = cfg['mf']
  meta = {}
  txt = ""
  g = rdflib.Graph()
  result = g.parse(tf, format='turtle')
  with open(mf) as json_data:
    meta = json.load(json_data)
    json_data.close()
  ifile  = open(fn, "rb")
  reader = csv.reader(ifile)
  txt +=  "@base\t"+meta['baseuri']+" .\n" # e.g. @base               <http://data.example.org/wow/data/weather-observations/> .
  rownum = 0
  for row in reader:
      if rownum == 0:
          header = row
      else:
          colnum = 0
          rowvalmap = {}
          # print "# ROW: ", row
          for col in row:
              sn = meta['columns'][colnum]['short_name']
              rowvalmap[sn] = row[colnum]
              colnum += 1
          # print "# rowvalmap: ", rowvalmap
          for subj, pred, obj in g:
             # print "# RDFTMP: ", subj, pred, obj
             mysub = expand(subj, rowvalmap)
             myobj = expand(obj, rowvalmap)
             s = "<"+  mysub+  "> "+  "<"+  pred+  "> "
             if type(myobj) == rdflib.term.Literal:
                s += "\"" +myobj+  "\" ."
             else:
                s += "<" +myobj+  "> ."
             txt += s + "\n"
             # colnum += 1
      rownum += 1
  ifile.close()
  return txt


if __name__ == "__main__":
    main()
