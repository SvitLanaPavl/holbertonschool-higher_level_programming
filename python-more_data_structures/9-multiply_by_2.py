#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    new_dictionary.update(
        (key, value * 2) for key, value in new_dictionary.items()
    )
    return new_dictionary
