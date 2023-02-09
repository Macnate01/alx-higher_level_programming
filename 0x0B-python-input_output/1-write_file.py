#!/usr/bin/python3
"""Defines a function file-writing."""


def write_file(filename="", text=""):
    """Write a string to a UTF"""
    with open(filename, "w", encoding="utf-8") as fichier:
        return fichier.write(text)
