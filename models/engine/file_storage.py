#!/usr/bin/python3
"""
Module that serializes instances to a JSON file and deserializes JSON file to instances
"""
import json

from models.base_model import BaseModel


class FileStorage():
    """Class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dict __objects"""
        return self.__objects

    def new(self, obj):
        """set in __object obj with key objclassname.id"""
        obj_name = obj.__class__.__name__
        self.__objects[f"{obj_name}.{obj.id}"] = obj

    def save(self):
        """serialize __objects to JSON file __file_path"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fil:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, fil)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
