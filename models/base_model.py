#!usr/bin/python3
"""
Base Module for AirBnB clone Project
"""

from datetime import datetime
from uuid import uuid4
import models

class BaseModel():
    """
    BaseModel Class
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the class BaseModel
        """
        if kwargs:
            for key in kwargs:
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                        kwargs[key], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """return str representation"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dict"""
        gdict = self.__dict__.copy()
        gdict["created_at"] = self.created_at.isoformat()
        gdict["updated_at"] = self.updated_at.isoformat()
        gdict["__class__"] = self.__class__.__name__
        return gdict
