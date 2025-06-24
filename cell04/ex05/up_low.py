#!/usr/bin/env python3
word = input("Give me a word: ")
for i in word:
    if i.isupper():
        print(i.lower(), end="")
    elif i.islower():
        print(i.upper(), end="")
    else:
        print(i, end="")