# -problem3_6.py *- coding: utf-8 -*-

import sys

txtfile = sys.argv[1]
ctfile = sys.argv[2]

text = open(txtfile)
ct = open(ctfile, 'w')

for line in text:
    line = line.strip("\n")
    ct.write(str(len(line))+"\n")
    
text.close()
ct.close()
