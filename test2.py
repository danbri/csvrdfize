#!/usr/bin/env python

import sys
sys.path.append("./lib") 
from uritemplate import expand
from csvrdfize import generateTurtle

def main():

  t1_cfg = { 
    'fn': 'samples/look-inside-art/rembrandt-paintings.csv',
    'tf': 'samples/look-inside-art/map-art.ttlt',
    'mf': 'samples/look-inside-art/art.json' 
  }

  print generateTurtle( t1_cfg )  

if __name__ == "__main__":
    main()
