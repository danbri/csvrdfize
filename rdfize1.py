#!/usr/bin/env python

# DISCLAIMER: Sample code only. Do not recycle for production. http://xkcd.com/327/ etc.

import sys
sys.path.append("./lib") # tmp for uritemplate
import rdflib
import logging
import csv
from uritemplate import expand

logging.basicConfig()
logging.disable(logging.WARNING) # complains due to {template} syntax within URIs

# Load mapping template, CSV data, metadata.
g = rdflib.Graph()
result = g.parse("map1.ttlt", format='turtle')
fn = 't1.csv'

meta = { 
  'primary_key': '<site/22580943/date-time/{sample-time}>',
  'baseuri': '<http://data.example.org/wow/data/weather-observations/>',
  'columns': 
  [  
     { 'short_name': 'sample-time' },
     { 'short_name': 'air-temp',
       'predicate': 'def-op:airTemperature_C', 
       'datatype' : 'xsd:double' },
     { 'short_name': 'dew-point',
       'datatype': 'xsd:double' }
  ]
}

ifile  = open(fn, "rb")
reader = csv.reader(ifile)

print "@base\t", meta['baseuri'], " ." # e.g. @base               <http://data.example.org/wow/data/weather-observations/> .
# Emit N-Triple-esque Turtle
rownum = 0
for row in reader:
    if rownum == 0:
        header = row
    else:
        colnum = 0
        rowvalmap = {}
        print "# ROW: ", row
        for col in row:
            sn = meta['columns'][colnum]['short_name']
            print "# COL:" , colnum, "SN: ", sn
            rowvalmap[sn] = row[colnum]
            colnum += 1
        print "# rowvalmap: ", rowvalmap
        for subj, pred, obj in g:
           print "# RDFTMP: ", subj, pred, obj
           mysub = expand(subj, rowvalmap)
           myobj = expand(obj, rowvalmap)
           s = "<"+  mysub+  "> "+  "<"+  pred+  "> "
           if type(myobj) == rdflib.term.Literal:
              s += "\"" +myobj+  "\" ."
           else:
              s += "<" +myobj+  "> ."
           print s
           print 
           # colnum += 1
    rownum += 1
    print "\n"
ifile.close()
