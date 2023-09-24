#!/usr/bin/python3
"""Adds items to a file"""
import sys


if __name__ == '__main__':
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__(' 6-load_from_json_file').load_from_json_file

    try:
        list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        list = []
    save_to_json_file(list + sys.argv[1:], "add_item.json")
