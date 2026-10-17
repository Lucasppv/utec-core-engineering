#!/usr/bin/env python3

def uppercase(str):
    for char in str:
        code = ord(char)
        if code >= 97 and code <= 122:
            code = code - 32
        print(chr(code), end="")
    print()
