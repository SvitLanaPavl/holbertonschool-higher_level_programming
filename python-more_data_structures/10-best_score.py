#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_value = max(a_dictionary.values())
    best_key = [key for key, value in a_dictionary.items() if value == max_value]
    if not best_key:
        return None
    else:
        return best_key[0]
