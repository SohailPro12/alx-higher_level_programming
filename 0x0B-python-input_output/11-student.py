#!/usr/bin/python3

"""
Module of Student class.
"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """initiliaze args"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return the attrs that were given"""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        mydict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                mydict[key] = value
        return mydict

    def reload_from_json(self, json):
        """reaload form a file and replace attr"""
        for key, value in json.items():
            if key is self.__dict__:
                self.__dict__[key] = value

