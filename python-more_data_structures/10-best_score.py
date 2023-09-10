#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_value = max(a_dictionary.values())
    best_key = list(key for key, value in a_dictionary.items() if value == max_value)
    return best_key[0] if best_key else None
