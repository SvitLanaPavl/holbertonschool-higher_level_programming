#!/usr/bin/python3
import json
"""Base class module"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string represenation through serialization
        
        Args:
            list_dictionaries: a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
