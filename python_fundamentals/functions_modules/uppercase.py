#!/usr/bin/env python3


def uppercase(n_str):
    res = ""
    for c in n_str:
        if 97 <= ord(c) <= 122:
            res += chr(ord(c) - 32)
        else:
            res += c
    print(res)
