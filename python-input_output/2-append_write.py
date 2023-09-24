#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """Append a string at the end of the text file"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
