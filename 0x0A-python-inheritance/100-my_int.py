#!/usr/bin/python3
"""
Modul with the MyInt class.
"""


class MyInt(int):
    """inherts from int"""
    def __eq__(self, other):
        """not equal"""
        return super().__ne__(other)

    def __ne__(self, other):
        """equal"""
        return super().__eq__(other)
