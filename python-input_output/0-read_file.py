#!/usr/bin/python3
"""Text file reading"""


def read_file(filename=""):
    """Reads the text file"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
