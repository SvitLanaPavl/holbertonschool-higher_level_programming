#!/usr/bin/python3
"""Object is instance of the specified class"""


def is_same_class(obj, a_class):
    """True if the object exactly an instance of the specified class"""
    return type(obj) is a_class
