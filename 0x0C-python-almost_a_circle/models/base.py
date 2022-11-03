#!/usr/bin/python3
"""
Module contains class Base

@private class __nb_objects, & class constructor __init__
Returns: JSON str repr of list dictionaries
Saves JSON str of instance dict into file
Returns: Python obj of JSON string repr
Returns: instance with  already set attr
Returns: list of instances
Saves to CSV & loads from CSV file
"""


import json
import csv


class Base():
    """
    defines class -> Base
    Class Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
    Static Methods:
        to_json_string(list_dictionaries)   from_json_string(json_string)
    Class Methods:
        save_to_file(cls, list_objs)    save_to_file_csv(cls, list_objs)
        load_from_file(cls)             load_from_file_csv(cls)
        create(cls, **dictionary)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Init id, ++class attribute if no id & set as id"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns: JSON str repr of list dict"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns; Python obj of JSON str representation"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save-> json strings of all instances into file"""
        objs = []
        if list_objs is not None:
            for o in list_objs:
                objs.append(cls.to_dictionary(o))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as F:
            F.write(cls.to_json_string(objs))

    @classmethod
    def create(cls, **dictionary):
        """Returns-> instance with attr set initially """
        if cls.__name__ == "Square":
            replica = cls(1)
        if cls.__name__ == "Rectangle":
            replica = cls(1, 1)
        replica.update(**dictionary)
        return replica

    @classmethod
    def load_from_file(cls):
        """Returns: list of instances"""
        filenamee = cls.__name__ + ".json"
        e = []
        try:
            with open(filenamee, "r") as F:
                instances = cls.from_json_string(F.read())
            for i, dic in enumerate(instances):
                e.append(cls.create(**instances[i]))
        except Exception as ex:
            pass
        return e

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as F:
            writer = csv.writer(F)
            for o in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([o.id, o.width, o.height, o.x, o.y])
                if cls.__name__ == "Square":
                    writer.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        ob = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='') as F:
            Rf = csv.Rf(F)
            for row in Rf:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                           "width": int(row[1]),
                           "height": int(row[2]),
                           "x": int(row[3]),
                           "y": int(row[4])}
                if cls.__name__ == "Square":
                    dic = {"id": int(row[0]),
                           "size": int(row[1]),
                           "x": int(row[2]),
                           "y": int(row[3])}
                o = cls.create(**dic)
                ob.append(o)
        return ob
