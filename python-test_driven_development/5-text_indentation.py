#!/usr/bin/python3
"""Prints a text with two new lines after . ? and :"""


def text_indentation(text):
    """Prints two new lines after specific characters"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        new_text = ""
        new_line = False
        for i, chr in enumerate(text):
            if chr in ".?:":
                if i < len(text) - 1:
                    new_text += chr + "\n\n"
                    new_line = True
                else:
                    new_text += chr
            else:
                if chr == " " and new_line:
                    continue
                new_text += chr
                if chr != " ":
                    new_line = False
    print(new_text, end="")
