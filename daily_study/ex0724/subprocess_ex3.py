# -*- coding: utf-8 -*-
import sys

if len(sys.argv) != 2:
    print "Usage: {} IP_ADDRESS".format(sys.argv[0])    

#print "sys.argv", sys.argv
for i in range(len(sys.argv)):
    print "argv[{}]: {}".format(i, sys.argv[i])
    #if sys.argv[1] == "-l":
        #echo_cnt = sys.argv()
