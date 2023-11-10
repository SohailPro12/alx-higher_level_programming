# models/base.py
"""
This module defines a Base class that serves as the base for other classes in the project.
"""

import json

class Base:
    """
    Base class for the project. It includes methods for JSON string conversion and file saving.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.

        Args:
            id: id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        :param list_dictionaries: list of dictionaries to convert
        :return: JSON string representation of the list of dictionaries
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a file in JSON string format.

        :param list_objs: list of objects to save
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    def from_json_string(json_string):
        """return json string"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json_string
