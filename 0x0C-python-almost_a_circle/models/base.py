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
