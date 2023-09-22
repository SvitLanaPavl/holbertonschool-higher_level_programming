#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """True if the obj is an instance of a class
    that inherited from the specified class"""
    if isinstance(obj, a_class) and not issubclass(a_class, obj.__class__):
        return True
    return False
