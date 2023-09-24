#!/usr/bin/python3
"""Save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an obj to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
