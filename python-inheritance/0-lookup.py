#!/usr/bin/python3
def lookup(obj):
    """Returns a list of available attributes"""
    attrs = []
    for attr in dir(obj):
        attrs.append(attr)
    return attrs
