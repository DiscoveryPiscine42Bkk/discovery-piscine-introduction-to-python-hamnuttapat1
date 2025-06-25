#!/usr/bin/env python3
import sys 
if len(sys.argv) <2 :
    print("none")
else:
    for i in range(1, len(sys.argv)):
       
        if "ism" not in sys.argv[i]:
            print(f"{sys.argv[i]}ism")