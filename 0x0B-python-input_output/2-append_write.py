#!/usr/bin/python3
"""Function Appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string of a text file"""
    with open(filename, 'a') as fichier:
        return fichier.write(text)
