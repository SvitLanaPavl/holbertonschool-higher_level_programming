#!/usr/bin/python3
"""MyList inherits from list"""


class MyList(list):
    """The class inherits from list"""

    def print_sorted(self):
        """Sorts the list"""
        print(sorted(self))
