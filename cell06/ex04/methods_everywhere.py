#!/usr/bin/env python3
import sys

def shrink(eight):
    print(eight[:8])
def enlarge(eight):
    if len(eight) < 8:
        z = 8-len(eight)
        eight += 'Z'*z
    print(eight)
if len(sys.argv) < 2:
    print("none")
else:
    for j in sys.argv[1:]:
        if len(j) > 8:
            shrink(j)
        elif len(j) < 8:
            enlarge(j)
        else:
            print(j)

