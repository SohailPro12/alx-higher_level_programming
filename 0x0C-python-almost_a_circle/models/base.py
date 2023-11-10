#!/usr/bin/python3

"""
Module of Base class.
"""


class Base:
    """
    It keeps track of the number of objects created
    and assigns a unique id to each object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Parameters:
        id (int): The id to assign to the object.

        Returns:
        None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects