#!/usr/bin/env python

import sys
sys.path.append("./lib") 
from uritemplate import expand
from csvrdfize import generateTurtle

def main():

  t1_cfg = { 
    'fn': 'samples/simple-weather-observation/t1.csv',
    'tf': 'samples/simple-weather-observation/map1.ttlt',
    'mf': 'samples/simple-weather-observation/t1.json' 
  }

  print generateTurtle( t1_cfg )  

if __name__ == "__main__":
    main()
