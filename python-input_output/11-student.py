#!/usr/bin/python3
"""Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation"""
        if attrs is None:
            return self.__dict__
        else:
            json_data = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_data[attr] = getattr(self, attr)
            return json_data

    def reload_from_json(self, json):
        """Replaces all attributes of the student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
