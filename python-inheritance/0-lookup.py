#!/usr/bin/python3
def lookup(obj):
    attrs = []
    for attr in dir(obj):
        attrs.append(attr)
    return attrs
