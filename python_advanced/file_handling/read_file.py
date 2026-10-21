#!/usr/bin/env python3
"""
Módulo que contiene una función para leer archivos de texto.
"""


def read_file(filename=""):
    """Lee un archivo de texto codificado en UTF-8 y lo imprime en stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
