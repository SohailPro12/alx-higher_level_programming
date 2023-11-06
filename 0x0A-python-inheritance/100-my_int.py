#!/usr/bin/python3
"""
Modul with the MyInt class.
"""


class MyInt:
    """inherts from int"""
    def __init__(self, n):
        self.n =  n
    def __str__(self):
    """str imp"""
        return f"{int(self.n)}"
