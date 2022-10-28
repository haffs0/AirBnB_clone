#!/usr/bin/pythonee
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Representation of base model class"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): key/value pairs of attributes.
        """

        time_form = "%Y-%m-%dT%H:%M:%S:.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_form)
                else:
                    self.__dict__[k] = v

    def save(self):
        """Update updated_at with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance."""
        ret_dict = self.__dict__.copy()
        ret_dict["created_at"] = self.created_at.isoformat()
        ret_dict["updated_at"] = self.updated_at.isoformat()
        ret_dict["__class__"] = self.__class__.__name__
        return ret_dict

    def __str__(self):
        """Return the print / str representation of the BaseModel instance."""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
