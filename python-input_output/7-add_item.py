#!/usr/bin/python3
"""Adds items to a file"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__(' 6-load_from_json_file').load_from_json_file


def add_items_to_file(filename, items):
    """Adds items to a file"""
    my_list = load_from_json_file(filename)
    if my_list is None:
        my_list = []
    for item in items:
        my_list.append(item)
    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    items = sys.argv[1:]

add_items_to_file("add_item.json", items)
