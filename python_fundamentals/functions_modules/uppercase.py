#!/usr/bin/env python3


def uppercase(str):
    res = ""
    for c in str:
        code = ord(c)
        res += chr(code - 32) if 97 <= code <= 122 else c
    print(res, end="")
