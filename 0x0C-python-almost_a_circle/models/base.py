#!/usr/bin/python3
"""
This module defines a Base class that serves as the base for other classes in the project.
It includes methods for JSON string conversion, file saving, and object creation from dictionary.
"""

import json

class Base:
    """
    Base class for the project
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

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        :param json_string: JSON string to convert
        :return: list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new instance of the class using a dictionary of attributes.

        :param dictionary: dictionary of attributes
        :return: new instance of the class
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a file in JSON string format.

        :return: list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                json_string = f.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    def save_to_file_csv(cls, list_objs):
        """
        Save a list of objects to a CSV file.

        :param list_objs: list of objects to save
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as f:
            writer = csv.writer(f)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of instances from a CSV file.

        :return: list of instances
        """
        filename = cls.__name__ + ".csv"
        instances = []
        with open(filename, mode="r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                instance = cls.from_csv_row(row)
                instances.append(instance)
        return instances
