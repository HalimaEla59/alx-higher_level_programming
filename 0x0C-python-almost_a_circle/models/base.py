#!/usr/bin/python3
"""class Base, base of all classes of this project"""
import json
import os.path
import csv


class Base:
    """class Base to manage id attribute of all classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init func of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json representation of str"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves to file"""
        try:
            jFile = cls.to_json_string([x.to_dictionary() for x in list_objs])
        except:
            jFile = "[]"
        with open(cls.__name__+'.json', 'w', encoding='utf-8') as f:
            f.write(jFile)

    @staticmethod
    def from_json_string(json_string):
        """returns string from json string"""
        if json_string is None or json_string == "[]":
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns class instance from dictionary of attributes"""
        if dictionary:
            if cls.__name__ == "Square":
                new = cls(1)
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instance"""
        if not os.path.isfile(cls.__name__+'.json'):
            return []
        else:
            with open(cls.__name__+.'json', "r", encoding="utf-8") as f:
                listD = cls.from_json_string(f.read())
            return [cls.create(**d) for d in listD]
