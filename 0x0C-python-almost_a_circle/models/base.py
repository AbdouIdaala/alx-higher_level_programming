#!/usr/bin/python3
"""import module"""
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON formatted string.

        Args:
            list_dictionaries (list of dict):
            A list of dictionaries to be converted.

        Returns:
            str: A JSON formatted string representing the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file.

        Args:
            list_objs (list): A list of objects to be saved to a JSON file.
        """
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(list_dicts)
        with open(cls.__name__+".json", mode='w', encoding='UTF-8') as f:
            f.write(json_str)
