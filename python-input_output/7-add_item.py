#!/usr/bin/python3
"""Adds items to a file"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__(' 6-load_from_json_file').load_from_json_file

open("add_item.json", "w", encoding="utf-8")
try:
    list = load_from_json_file("add_item.json")
except ValueError:
    list = []

# adding args
for arg in sys.argv[1:]:
    list.append(arg)

# save to json
save_to_json_file(list, "add_item.json")
