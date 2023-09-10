#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for index, value in enumerate(my_list):
            if index < x:
                print(value, end="")
                i += 1
            else:
                break
        print()
        return i
    except IndexError:
        print()
        return i
