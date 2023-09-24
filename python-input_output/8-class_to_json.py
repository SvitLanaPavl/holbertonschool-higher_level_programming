#!/usr/bin/python3
"""Dictionary Description"""


def class_to_json(obj):
    """Returns dictionary description"""
    json_dict = {}
    for attr in obj.__dict__:
        value = getattr(obj, attr)
        if isinstance(value, list):
            json_dict[attr] = [class_to_json(item) for item in value]
        elif isinstance(value, dict):
            json_dict[attr] = [class_to_json(value)]
        elif isinstance(value, str):
            json_dict[attr] = value
        elif isinstance(value, int):
            json_dict[attr] = value
        elif isinstance(value, bool):
            json_dict[attr] = value
        else:
            raise TypeError("Attribute {} is not serializable.".format(attr))
    return json_dict
