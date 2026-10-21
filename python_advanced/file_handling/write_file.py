#!/usr/init/env python3
"""
Módulo que contiene una función para escribir texto en un archivo.
"""


def write_file(filename="", text=""):
    """Escribe una cadena en un archivo UTF-8 y
    retorna los caracteres escritos.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
