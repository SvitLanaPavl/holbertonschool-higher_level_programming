#!/usr/bin/python3
"""To JSON string"""
import json


def from_json_string(my_str):
    """Returns an object represented by JSON str"""
    return json.loads(my_str)
