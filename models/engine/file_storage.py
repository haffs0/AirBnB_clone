#!/usr/bin/python3
"""Define the file storage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Representation of abstract storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_cls_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_cls_name, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = FileStorage.__objects
        odict = {obj: obj_dict[obj].to_dict() for obj in obj_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(odict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for value in obj_dict.values():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
