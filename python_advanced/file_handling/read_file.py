#!/usr/bin/env python3

def read_file(filename=""):
    with open(filename, encodign="utf-8") as f:
        print(f.read(), end="")
