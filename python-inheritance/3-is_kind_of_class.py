#!/usr/bin/python3
"""Checking if the obj is instance of or an instance of the class that's inherited"""


def is_kind_of_class(obj, a_class):
    """True if the obj is an instance of or the obj is an instacne of
    the class that inherited from the specified class"""
    return isinstance(obj, a_class) or issubclass(obj.__class__, a_class)
