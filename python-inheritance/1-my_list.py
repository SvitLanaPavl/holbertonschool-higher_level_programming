#!/usr/bin/python3
"""MyList inherits from list"""


class MyList(list):
    """the class inherits from list"""

    def print_sorted(self):
        """Sorts the list"""
        self.sort()
        print(self)
