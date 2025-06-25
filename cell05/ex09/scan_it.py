# !/usr/bin/env python3
import sys

if len(sys.argv) == 3:
    find = sys.argv[2] 
    word = sys.argv[3] 
    count = word.count(find)
    if count == 0:
        print("none")
    else:
        print(count)

else:
    print("none")