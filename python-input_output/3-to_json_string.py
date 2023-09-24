#!/usr/bin/python3
"""To JSON string"""
import json


def to_json_string(my_obj):
    """Returns JSON representation of an object"""
    try:
        json_string = json.dumps(my_obj)
        return json_string
    except Exception as e:
        # if the object cannot be serialized, no exceptions
        pass
