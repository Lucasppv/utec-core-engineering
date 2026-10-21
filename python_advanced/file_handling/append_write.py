#!/usr/bin/env python3
"""
Módul para añadir texto al final de un archivo.
"""


def append_write(filename="", text=""):
    """Añade una cadena a un archivo UTF-8
    y retorna los caracteres añadidos."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
