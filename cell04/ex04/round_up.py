#!/usr/bin/env python3
a = float(input("Give me a number: "))
if a > int(a):
    print(int(a) + 1)
elif a < int(a):
    print(int(a) - 1)
else:
    print(int(a))
