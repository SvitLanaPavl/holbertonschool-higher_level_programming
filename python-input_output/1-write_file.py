#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """Write a string to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
